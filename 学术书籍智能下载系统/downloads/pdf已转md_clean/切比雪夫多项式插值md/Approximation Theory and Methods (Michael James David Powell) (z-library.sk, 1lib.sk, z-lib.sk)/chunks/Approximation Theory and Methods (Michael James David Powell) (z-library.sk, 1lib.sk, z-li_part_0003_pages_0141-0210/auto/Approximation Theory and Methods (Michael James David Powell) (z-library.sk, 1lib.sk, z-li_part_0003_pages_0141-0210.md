Proof. Equations (11.17) and (11.24) imply that the coefficients of the required approximation (11.15) have the values

$$
{ c } _ { i } ^ { * } = ( \phi _ { i } , f ) / \| \phi _ { i } \| ^ { 2 } , \qquad i = 0 , 1 , \ldots , n ,
$$

which proves the theorem.□

Often the space $\mathcal { A }$ is defined by a sequence of independent basis functions $\{ \psi _ { i } ; i = 0 , 1 , \ldots , n \}$ , say.For example, if $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ ,then $\psi _ { i }$ may be the function $\{ \psi _ { i } ( x ) = x ^ { i }$ ； $a \leqslant x \leqslant b \}$ . For $i = 0 , 1 , \ldots , n$ ,we let $\mathcal { A } _ { i }$ be the linear space that is spanned by the functions $\{ \psi _ { j } ; j = 0 , 1 , \ldots , i \}$ ， in order to describe a general method for choosing an orthogonal basis of $\mathcal { A }$

We let $\phi _ { 0 }$ be the function $\psi _ { 0 }$ .For $i \geqslant 1$ we let $\bar { \psi _ { i } }$ be any member of $\mathcal { A } _ { i }$ that is not in $\mathcal { A } _ { i - 1 }$ , and we let $q _ { i } ^ { * }$ be the best approximation from $\mathcal { A } _ { i - 1 }$ to ${ \bar { \psi } } _ { i } .$ We define $\phi _ { i }$ by the equation

$$
\phi _ { i } = { \bar { \psi } } _ { i } - q _ { i } ^ { * } .
$$

Because Theorem 11.1 states that $\phi _ { i }$ is orthogonal to all elements of $\mathcal { A } _ { i - 1 }$ ， the condition

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad j < i ,
$$

is satisfied.Hence the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ , that are obtained from this construction,are an orthogonal basis of $\mathcal { A }$

This construction is particularly useful if we are given an element $f$ and an infinite sequence of functions $\{ \psi _ { i } ; i = 0 , 1 , 2 , \ldots \}$ in a Hilbert space $\mathcal { B }$ ， and we wish to make the error $\| f - p \|$ less than a prescribed accuracy $\pmb { \delta }$ ， where $p$ is a linear combination of the first $( n + 1 )$ terms of the sequence, and where the value of $\pmb { n }$ is not known in advance,because it is to be the smallest integer that is allowed by the required accuracy. The main advantage of the construction is that the definition of the orthogonal functions $\{ \phi _ { i } ; i = 0 , 1 , 2 , \ldots \}$ does not depend on $\pmb { n }$ . Hence the coefficients (11.31） are also independent of $\pmb { n }$ .For $i = 0 , 1 , 2 , \dots$ ，we define $p _ { i } ^ { * }$ to be the function

$$
p _ { i } ^ { * } = \sum _ { j = 0 } ^ { i } \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } \phi _ { j } .
$$

Because Theorem 11.2 shows that this function is the best approximation to $f$ from the linear space $\mathcal { A } _ { i }$ that is spanned by the functions $\{ \psi _ { j } ; j =$ $0 , 1 , \ldots , i \}$ ，we require $_ n$ to be the least integer that satisfies the condition

$$
\left\| f - { p _ { n } ^ { * } } \right\| \leqslant \delta .
$$

In fact it is not necessary to calculate each of the approximations (11.34),because equation (11.14) implies that expression (11.35) is equivalent to the inequality

$$
\| p _ { n } ^ { * } \| ^ { 2 } \geqslant \| f \| ^ { 2 } - \delta ^ { 2 } .
$$

Therefore we have only to choose $_ n$ so that $\| p _ { n } ^ { * } \|$ is sufficiently large. Because the orthogonality conditions and the definition (11.34) imply the equation

$$
\big \| p _ { n } ^ { * } \big \| ^ { 2 } = \sum _ { j = 0 } ^ { n } { \big ( } \phi _ { j } , f { \big ) } ^ { 2 } / \big \| \phi _ { j } \big \| ^ { 2 } ,
$$

it follows that the required value of $_ n$ can be calculated by summing the terms $\{ ( \phi _ { j } , f ) ^ { 2 } / \| \phi _ { j } \| ^ { 2 } ; j = 0 , 1 , 2 , . . . \} ,$ ， until the bound

$$
\sum _ { j = 0 } ^ { n } \frac { \left( \phi _ { j } , f \right) ^ { 2 } } { \left\| \phi _ { j } \right\| ^ { 2 } } { \geqslant } \| f \| ^ { 2 } - \delta ^ { 2 }
$$

is satisfied.

# 11.4 The recurrence relation for orthogonal polynomials

An important special case of least squares approximation is when the set of approximating functions $\boldsymbol { \mathscr { A } }$ is the linear space $\mathcal { P } _ { n }$ of all polynomials of degree at most $_ n$ . In the case of approximation on a point set, where the scalar product has the value (11.6), we take the point of view that ‘polynomial' means the vector that is obtained by evaluating the polynomial at the discrete points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ .This point of view is tenable when the number of different discrete points is greater than $_ n$ ， so we assume that this condition is satisfied,in order that the work of this section is relevant to both continuous and discrete least squares approximations.

Orthogonal polynomials can be constructed by the method that is described immediately after Theorem 11.2, where the basis functions are $\{ \psi _ { i } ( x ) = x ^ { i } ; i = 0 , 1 , \ldots , n \}$ . A version of this construction, that comes from a particular choice of the function $\bar { \psi _ { i } }$ in equation (11.32), is highly useful in practice, because it gives the following three-term recurrence relation.

# Theorem 11.3

Let $\scriptstyle \phi _ { 0 }$ be the constant function

$$
\phi _ { 0 } ( x ) = 1 , \qquad a \leqslant x \leqslant b .
$$

For $j \equiv 0$ ,let $\alpha _ { j }$ be the scalar

$$
\alpha _ { j } = ( \phi _ { j } , x \phi _ { j } ) / \big \| \phi _ { j } \big \| ^ { 2 } ,
$$

where $x \phi _ { j }$ is the polynomial $\{ x \phi _ { j } ( x ) ; a \leqslant x \leqslant b \}$ .Let $\phi _ { 1 }$ be the linear function

$$
\phi _ { 1 } ( x ) = ( x - \alpha _ { 0 } ) \phi _ { 0 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

For $j \geqslant 1$ ,let $\beta _ { j }$ be the scalar

$$
\beta _ { j } = \mathopen { } \mathclose \bgroup \left\| \phi _ { j } \aftergroup \egroup \right\| ^ { 2 } / \mathopen { } \mathclose \bgroup \left\| \phi _ { j - 1 } \aftergroup \egroup \right\| ^ { 2 } ,
$$

and let $\phi _ { j + 1 }$ be defined by the three-term recurrence relation

$$
\phi _ { j + 1 } ( x ) = ( x - \alpha _ { j } ) \phi _ { j } ( x ) - \beta _ { j } \phi _ { j - 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

Then, for each $j ,$ , the function $\phi _ { j }$ is a polynomial of degree $j ,$ the coefficient of $x ^ { j }$ being unity. Moreover, the polynomials $\{ \phi _ { j } ; j = 0 , 1 , 2 , \ldots \}$ are orthogonal.

Proof. The first statement of the theorem is an immediate consequence of the definitions (11.39), (11.41) and (11.43). To establish the orthogonality conditions, we show that the definitions (11.41) and (11.43) are equivalent to the construction (11.32) where $\bar { \psi _ { i } }$ is the polynomial $x \phi _ { i - 1 }$ · Because we proceed by induction, we assume that the functions $\left\{ \phi _ { i } ; i = \right.$ $0 , 1 , \ldots , j \}$ ，defined in the statement of the theorem,are orthogonal. Therefore, by applying Theorem 11.2 to equation (11.32),it follows that the polynomial

$$
\phi _ { j + 1 } ( x ) = x \phi _ { j } ( x ) - \sum _ { i = 0 } ^ { j } \frac { \left( \phi _ { i } , x \phi _ { j } \right) } { \left\| \phi _ { i } \right\| ^ { 2 } } \phi _ { i } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is orthogonal to $\{ \phi _ { i } ; i = 0 , 1 , \ldots , j \}$ . The definition of $\pmb { \alpha _ { 0 } }$ shows that this equation is equivalent to expression (11.41) when $j = 0$ .Hence it remains to prove that the functions (11.43) and (11.44) are the same when $j \geqslant 1$

Therefore we consider the terms under the summation sign of expression (11.44). When $i = j$ we find the term $\alpha _ { j } \phi _ { j } ( x )$ ， which is present in equation (11.43). When $i \leqslant j - 2$ , we make use of the relation

$$
\begin{array} { c } { { ( \phi _ { i } , x \phi _ { j } ) = ( x \phi _ { i } , \phi _ { j } ) } } \\ { { { } } } \\ { { = 0 , } } \end{array}
$$

which holds because $\phi _ { j }$ is orthogonal to every polynomial in $\mathscr { P } _ { j - 1 }$ . Hence it is correct that $\phi _ { i } ( x )$ is absent from equation (11.43) for $i \leqslant j - 2$ .The remaining term of the sum depends on the identity

$$
\begin{array} { r l } {  { ( \phi _ { j - 1 } , x \phi _ { j } ) = ( x \phi _ { j - 1 } , \phi _ { j } ) } } \\ & { = ( \phi _ { j } , \phi _ { j } ) + ( x \phi _ { j - 1 } - \phi _ { j } , \phi _ { j } ) } \\ & { = \| \phi _ { j } \| ^ { 2 } , } \end{array}
$$

which holds because $( x \phi _ { j - 1 } - \phi _ { j } )$ isin $\boldsymbol { \mathcal { P } } _ { j - 1 }$ . It follows that equation

(11.43) contains the correct multiple of $\phi _ { j - 1 }$ , which completes the proof that expressions (11.43) and (11.44) are equivalent.□

When this theorem is applied in practice,to obtain the best polynomial approximation to an element $f$ of a Hilbert space, it is usual to calculate the coefficient

$$
c _ { j } ^ { \ast } = ( \phi _ { j } , f ) / \| \phi _ { j } \| ^ { 2 }
$$

immediately after $\phi _ { j }$ is determined. At the end of the fitting procedure, it is suffcient to provide the values of the parameters $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ $\{ \alpha _ { j } ; j = 0 , 1 , \ldots , n - 1 \}$ and $\{ \beta _ { j } ; j = 1 , 2 , \ldots , n - 1 \}$ .Therefore the storage space that holds $\phi _ { j - 1 }$ may be re-used by $\phi _ { j + 1 }$ when formula (11.43) is applied,which is important sometimes in discrete calculations that have very many data. After the polynomial approximation is found, it may be necessary to calculate its value at several general points of the range $a \leqslant x \leqslant b$ .For each value of $\pmb { x } .$ ,the numbers $\{ \phi _ { j } ( x ) ; j = 0 , 1 , \ldots , n \}$ are obtained in sequence from the three-term recurrence relation, and then $p ^ { * } ( x )$ is determined by the equation

$$
p ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } ( x ) .
$$

# 11 Exercises

11.1 Let $\mathscr { A }$ be a finite-dimensional linear subspace of a Hilbert space $\mathcal { B }$ ,and,for any $f$ in ${ \mathcal { B } } _ { : }$ let $X ( f )$ be the best approximation in $\pmb { \mathcal { A } }$ to $f ,$ with respect to the 2-norm that is induced by the scalar product. Prove that $\pmb { X }$ is a linear operator, that it is a projection, and that $\| X \| _ { 2 } = 1$ .

11.2 Let $f \in \mathcal { C } [ - 5 , 5 ]$ ，and let $\mathscr { A }$ be the linear space of dimension seven that contains all even polynomials in $\mathcal { P } _ { 1 2 }$ . Show that there are many elements of $\mathscr { A }$ that minimize the expression

$$
\sum _ { j = - 5 } ^ { 5 } \big [ f ( j ) - p ( j ) \big ] ^ { 2 } , \qquad p \in \mathcal { A } ,
$$

but that there is only one optimal set of function values $\{ p ( j )$ ； $j = - 5 , - 4 , \dots , 5 \}$

11.3 Let $f$ be the function $\{ f ( x ) = x ^ { 2 } ; 0 \leqslant x \leqslant 1 \}$ , and let $\{ p ^ { * } ( x ) = c _ { 0 } ^ { * } +$ $c _ { 1 } ^ { * } x ; 0 \leqslant x \leqslant 1 \}$ be the linear polynomial that minimizes the integral

$$
\int _ { 0 } ^ { 1 } \left[ f ( x ) - p ( x ) \right] ^ { 2 } \mathrm { d } x , \qquad p \in \mathcal { P } _ { 1 } .
$$

Calculate the coefficients $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the normal equations (11.17),and verify that $p ^ { * }$ satisfies equation (11.14).

11.4 Suppose that one has to use a computer to calculate the coefficients $c _ { 0 }$ and $c _ { 1 }$ that minimize the sum of squares of residuals of the inconsistent linear equations

$$
\begin{array} { c } { ( 1 + \varepsilon ) c _ { 0 } + 2 c _ { 1 } = 5 + 2 \varepsilon } \\ { \ } \\ { 2 c _ { 0 } + ( 4 + \varepsilon ) c _ { 1 } = 1 0 - \varepsilon } \\ { \ } \\ { \varepsilon c _ { 0 } = 3 \varepsilon } \\ { \ } \\ { \varepsilon c _ { 1 } = \varepsilon . } \end{array}
$$

Suppose also that the constant $\pmb \varepsilon$ is so small that $\varepsilon ^ { 2 }$ is less than the relative accuracy of the computer arithmetic. Show that, if the normal equations are formed, then the matrix of the system can be exactly singular,but, if one makes the substitution $c _ { 0 } =$ $\bar { c } _ { 0 } - 2 c _ { 1 }$ in order to work with $\bar { c } _ { 0 }$ and $c _ { 1 }$ instead of with $c _ { 0 }$ and $c _ { 1 }$ ， then it is possible to achieve moderate accuracy.

11.5 Use the three-term recurrence relation of Theorem 11.3 to calculate the polynomials $\{ \phi _ { k } \in \mathcal { P } _ { k } ; k = 0 , 1 , 2 , 3 \}$ that are orthogonal on the point set $\{ 0 , 1 , 3 \}$ ，which means that they satisfy the conditions

$$
\phi _ { j } ( 0 ) \phi _ { k } ( 0 ) + \phi _ { j } ( 1 ) \phi _ { k } ( 1 ) + \phi _ { j } ( 3 ) \phi _ { k } ( 3 ) = 0 , \qquad j \neq k .
$$

You should find that the cubic polynomial $\phi _ { 3 }$ is zero on the point set $\{ 0 , 1 , 3 \}$

11.6 For any $f$ in $\mathcal { C } [ \alpha , b ]$ let $X ( f )$ be the linear polynomial that minimizes the expression

$$
\int _ { a } ^ { b } [ f ( x ) - p ( x ) ] ^ { 2 } { \mathrm { d } } x , \qquad p \in { \mathcal { P } } _ { 1 } .
$$

Prove that, if the $\infty$ -norm is used in $\mathcal { C } [ \alpha , b ]$ ,then the norm of the operator $X$ has the value $\| \boldsymbol { X } \| _ { \infty } = \frac { 5 } { 3 }$

11.7 For $i = 0 , 1 , 2 , 3$ ，let $\phi _ { i }$ be the function that is obtained by drawing straight lines between the function values $\{ \phi _ { i } ( j ) =$ $\delta _ { i j } ; j = 0 , 1 , 2 , 3 \}$ . Thus $\{ \phi _ { i } ; i = 0 , 1 , 2 , 3 \}$ is a basis of the space of linear splines that is called $\mathcal { S } ( 1 , 0 , 1 , 2 , 3 )$ in Section 3.4. Let $f$ be the piecewise constant function $\{ f ( x ) = 1$ ， $0 \leqslant x \leqslant 1$ ； $f ( x ) = 0$ ， $1 < x \leqslant 3 \}$ . Use the normal equations (11.17) to calculate the coefficients $\{ c _ { i } ^ { * } ; i = 0 , 1 , 2 , 3 \}$ that minimize the integral

$$
\int _ { 0 } ^ { 3 } \left[ f ( x ) - \sum _ { i = 0 } ^ { 3 } c _ { i } ^ { * } \phi _ { i } ( x ) \right] ^ { 2 } \mathrm { d } x .
$$

Plot the function $\{ \sum c _ { i } ^ { * } \phi _ { i } ( x ) ; 0 \leqslant x \leqslant 3 \}$

11.8 Let $f$ be the function $\{ f ( x ) = 2 x - 1 ; 0 \leqslant x \leqslant 1 \}$ . Find the smallest value of $_ n$ such that a function of the form

$$
p ( x ) = \sum _ { k = 0 } ^ { n } c _ { k } \cos { ( k \pi x ) } , \qquad 0 \leqslant x \leqslant 1 ,
$$

satisfies the condition

$$
\int _ { 0 } ^ { 1 } [ f ( x ) - p ( x ) ] ^ { 2 } ~ \mathrm { d } x < 1 0 ^ { - 4 } .
$$

11.9 Given the values $T _ { 0 } ( x )$ and $T _ { 1 } ( x )$ of the first two Chebyshev polynomials, the recurrence relation

$$
T _ { k + 1 } ( x ) = 2 x T _ { k } ( x ) - T _ { k - 1 } ( x ) , \qquad k = 1 , 2 , 3 , \ldots ,
$$

is applied to calculate $T _ { n } ( x )$ where $_ n$ is large.Show that,if $T _ { 0 } ( x )$ and $T _ { 1 } ( x )$ are exact, but if every arithmetic operation can cause an absolute error of $\pm \eta$ ,then the error in $T _ { n } ( x )$ when $x = 1$ is at most $\scriptstyle { \frac { 3 } { 2 } } \eta n ( n - 1 )$ . Investigate whether larger errors can occur for any other value of $x$ in the interval $[ - 1 , 1 ]$

11.10 Let $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$ be finite-dimensional linear subspaces of a Hilbert space $\mathcal { B }$ ，and let $X _ { 1 }$ and $X _ { 2 }$ be the linear projection operators from $\mathcal { B }$ to $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$ respectively, that give the best approximations in these spaces with respect to the norm of the Hilbert space. For any $f _ { 1 }$ in $\mathcal { B }$ ，let the sequence $\{ f _ { k }$ ； $k = 1 , 2 , 3 , \ldots \}$ be defined by the equation $\{ f _ { k + 1 } = X _ { 2 } ( X _ { 1 } f _ { k } ) ; k =$ $1 , 2 , 3 , \ldots \}$ . Prove that the sequence converges to the best approximation to $f _ { 1 }$ in the intersection of the spaces $\mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 2 }$

# 12

# Properties of orthogonal polynomials

# 12.1 Elementary properties

Orthogonal polynomials have several uses in addition to the method of calculating least squares approximations that has just been described.For example, we find in Section 12.2 that they are important to the construction of some efficient formulae for the numerical calculation of integrals. First, however, some of their elementary properties are established.Unless it is stated otherwise,it is assumed that each orthogonal polynomial is defined on the range $a \leqslant x \leqslant b$ .However,by taking the point of view that is mentioned at the beginning of Section 11.4, it follows that some of the results of this chapter are also valid in the case when the range of $x$ is a set of discrete points.

# Theorem 12.1

Let $\mathcal { B }$ be a Hilbert space that contains the subspace $\mathcal { P } _ { n }$ of algebraic polynomials of degree $\pmb { n }$ .Let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a sequence of non-zero polynomials,where each $\phi _ { i }$ is in $\mathcal { P } _ { i } ,$ and where the orthogonality conditions

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad i \neq j ,
$$

hold (Theorem 11.3 shows that these conditions can be satisfied). Then the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ are linearly independent. Moreover, if $\psi _ { k }$ is any polynomial in $\mathcal { P } _ { k }$ that is orthogonal to the elements of $\mathcal { P } _ { k - 1 }$ ， where $k$ is any integer from $[ 1 , n ]$ ,then the equation

$$
\psi _ { k } ( x ) = c \phi _ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is obtained for some constant $^ { c }$

Proof. To prove the first part of the theorem, we have to show that, if the scalars $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ satisfy the equation

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } = 0 ,
$$

where O is the zero function, then they are all equal to zero. Because expression (12.3) implies the equations

$$
\sum _ { i = 0 } ^ { n } \lambda _ { i } ( \phi _ { j } , \phi _ { i } ) = 0 , \qquad j = 0 , 1 , \ldots , n ,
$$

and because $( \phi _ { j } , \phi _ { j } )$ is positive if $\phi _ { j }$ is a non-zero function, it follows from the orthogonality conditions (12.1） that the coefficients $\begin{array} { r l } { \{ \lambda _ { j } ; ~ j = } \end{array}$ $0 , 1 , \ldots , n \}$ are zero,which is the first required result.

This result is useful to the second part of the theorem, because it shows that the functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , k \}$ are a basis of $\mathcal { P } _ { k }$ . Therefore we may express $\psi _ { k }$ in the form

$$
\psi _ { k } = \sum _ { i = 0 } ^ { k } \mu _ { i } \phi _ { i } ,
$$

which gives the equations

$$
( \phi _ { j } , \psi _ { k } ) = \sum _ { i = 0 } ^ { k } \mu _ { i } ( \phi _ { j } , \phi _ { i } ) , \qquad j = 0 , 1 , \ldots , k - 1 .
$$

Hence condition (12.1) and the orthogonality properties of $\psi _ { k }$ imply that the parameters $\{ \mu _ { j } ; j = 0 , 1 , \ldots , k - 1 \}$ are zero. It follows from expression (12.5) that equation (12.2) is satisfied, where $^ c$ is equal to $\pmb { \mu _ { k } }$ □

Another elementary property of orthogonal polynomials, that is required in the next section, is as follows.

# Theorem 12.2

Let. $\phi _ { k }$ be a non-zero polynomial that is in $\mathcal { P } _ { k } ,$ ，and that is orthogonal to the elements of $\mathcal { P } _ { k - 1 }$ . Then $\phi _ { k }$ has exactly $k$ real and distinct zeros in the open interval $a < x < b$

Proof. Let $r$ be the number of sign changes of the function $\{ \phi _ { k } ( x )$ ； $a \leqslant x \leqslant b \}$ . There is a non-zero polynomial in $\mathcal { P } _ { r } , \psi _ { r }$ say,such that the inequality

$$
\phi _ { k } ( x ) \psi _ { r } ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b ,
$$

holds, the product $\phi _ { k } ( x ) \psi _ { r } ( x )$ being zero if and only if $\pmb { x }$ is a zero of $\phi _ { k }$ .It follows from the definition (11.2) of the scalar product that $\left( \phi _ { k } , \psi _ { r } \right)$ is positive. Therefore, because of the orthogonality properties of $\phi _ { k } , r$ is not less than $k$ .Hence $\phi _ { k }$ has at least $k$ distinct zeros in the open interval $a < x < b$ .The number of zeros cannot exceed $k$ because $\phi _ { k }$ is a non-zero element of $\mathcal { P } _ { k }$ .Therefore the theorem is true.□

The extension of this result to the discrete case is not difficult, but it is different from the other extensions that have been made in a fundamental way. In all other theorems it does not matter if the approximating function is known only on the set $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ，where the scalar product has the value (11.6),but now we use the fact that polynomials are defined for all values of the variable $x$ .In the statement of the discrete version of Theorem 12.2 we require $k < m$ ，and we let $[ a , b ]$ be any interval that contains the points $\{ x _ { j } ; j = 1 , 2 , \ldots , m \}$ . The proof of the theorem is unchanged,and $\psi _ { r }$ is still constructed so that inequality (12.7) holds for all $x$ in $[ a , b ]$ . It follows that the $k$ real roots of the polynomial $\phi _ { k }$ are usually not in the point set $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ,but they are in the shortest interval that contains the data points.

Theorem 12.1 shows that all functions $\phi _ { k }$ that satisfy the conditions of Theorem 12.2 are the same,except for a scaling factor. Therefore, the roots of $\phi _ { k }$ depend only on the integer $k$ and the definition of the scalar product.

# 12.2 Gaussian quadrature

Many formulae for approximating definite integrals have the form

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \mathrm { d } x \approx \sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) ,
$$

where $\{ w ( x ) ; a \leqslant x \leqslant b \}$ is a fixed positive weight function, where $f$ is in $\mathcal { C } [ \alpha , b ] .$ ,where $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ is a set of real coefficients,and where the abscissae are in ascending order

$$
a \leqslant x _ { 0 } < x _ { 1 } < . ~ . ~ . < x _ { k } \leqslant b .
$$

Hence the integral is estimated from $( k + 1 )$ point evaluations of $f .$ One of the most useful methods for choosing the parameters $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ and $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ is to force the condition that equation (12.8) is exact when $f$ is in a suitable linear subspace $\mathscr { A }$ of ${ \mathcal { C } } [ a , b ]$

For example, if the points $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ are given, then we may obtain the coeffcients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ by letting $\mathscr { A }$ be the space $\mathcal { P } _ { k }$ · We recall from Chapter 4 that, when $f$ is in $\mathcal { P } _ { k }$ , it can be expressed in the form

$$
f ( x ) = \sum _ { i = 0 } ^ { k } l _ { i } ( x ) f ( x _ { i } ) , \qquad a \leqslant x \leqslant b ,
$$

where $\{ l _ { i } ( x ) ; a \leqslant x \leqslant b \}$ is the cardinal function (4.3). It follows from the properties of cardinal functions that the two sides of expression (12.8) are equal when $c _ { i }$ has the value

$$
c _ { i } = \int _ { a } ^ { b } w ( x ) l _ { i } ( x ) \mathrm { d } x , \qquad i = 0 , 1 , \dots , k .
$$

Any other choice of $c _ { i }$ causes an error in the approximation (12.8) when $f$ is the cardinal polynomial $\{ l _ { i } ( x ) ; a \leqslant x \leqslant b \}$

Gaussian quadrature formulae extend this idea, for their parameter values $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ and $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ are such that the approximation (12.8) is exact when $f$ is in $\mathscr { P } _ { 2 k + 1 }$ . The abscissae $\{ x _ { i } ; i =$ $0 , 1 , \ldots , k \}$ may be calculated by satisfying a system of non-linear equations,but the purpose of this section is to show that they are the zeros of an orthogonal polynomial.

# Theorem 12.3

Let the points $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ in the quadrature formula (12.8) be the zeros of a polynomial $\phi _ { k + 1 }$ of degree $( k + 1 )$ that satisfies the orthogonality conditions

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { P } _ { k } ,
$$

where $\{ w ( x ) ; a \leqslant x \leqslant b \}$ is any integrable function. Let the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ have the values (12.11), where $l _ { i }$ is defined by equation (4.3). Then the approximation (12.8) is exact when $f$ is any polynomial in $\mathscr { P } _ { 2 k + 1 }$

Proof. If $f$ is in $\mathscr { P } _ { 2 k + 1 }$ , it may be expressed in the form

$$
f ( x ) = p ( x ) \phi _ { k + 1 } ( x ) + q ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $\phi _ { k + 1 }$ is given in the statement of the theorem,and where $p$ and $q$ are in $\mathcal { P } _ { k }$ . Because $\phi _ { k + 1 }$ is orthogonal to $p$ ,we have the equation

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \mathrm { d } x = \int _ { a } ^ { b } w ( x ) q ( x ) \mathrm { d } x .
$$

Because the abscissae $\left\{ x _ { i } ; i = 0 , 1 , \ldots , k \right\}$ are zeros of $\phi _ { k + 1 }$ , the identity

$$
\sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) = \sum _ { i = 0 } ^ { k } c _ { i } q ( x _ { i } )
$$

is satisfed.Because $\pmb q$ isin $\mathcal { P } _ { k }$ ，it follows from the definition of the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ that the right-hand sides of expressions (12.14) and (12.15) are equal. Therefore the left-hand sides are equal, which is the required result.□

When formula (12.8) is applied,it is usual for some errors to be present in the function values {f(xi); i = O,1,...,k}, due, for example,to the rounding errors of computer arithmetic. It is therefore advantageous if the sum

$$
\| c \| _ { 1 } = \sum _ { i = 0 } ^ { k } { \big | } c _ { i } { \big | }
$$

is small. However,in order that equation (12.8) is exact when $f$ is a constant function,it is necessary to satisfy the equation

$$
\int _ { a } ^ { b } w ( x ) \mathop { } \mathrm { d } x = \sum _ { i = 0 } ^ { k } c _ { i } .
$$

Therefore expression (12.16） is least if and only if the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ all have the same sign. Our next theorem shows that Gaussian quadrature formulae give this useful property.

# Theorem 12.4

If the approximation (12.8) is exact for allfunctions $f$ in $\mathscr { P } _ { 2 k + 1 }$ ， and if $w$ is positive, then each of the coefficients $\{ c _ { i } ; i = 0 , 1 , \ldots , k \}$ is positive.

Proof. If we let $f$ be the polynomial

$$
f ( x ) = [ l _ { i } ( x ) ] ^ { 2 } , \qquad a \leqslant x \leqslant b ,
$$

where $l _ { i }$ is the cardinal function (4.3),then the left-hand side of expression (12.8) is positive,and the right-hand side is equal to $c _ { i } .$ Because $f$ is in $\mathscr { P } _ { 2 k + 1 }$ , it follows that $c _ { i }$ is positive.□

Gaussian quadrature formulae are not very convenient for adaptive numerical integration procedures, where the user specifies the accuracy that he requires in the calculated estimate of his integral. In these procedures the error of each approximation to the integral is estimated automatically,and the method of integration is refined until it seems that the required accuracy is achieved.In Gaussian quadrature formulae the positions of the abscissae $\{ x _ { i } ; i = 0 , 1 , \ldots , k \}$ make it difficult to use previously calculated values of the integrand after each refinement process. Despite this disadvantage, Gaussan methods are found in many automatic integration algorithms.Moreover, if the integrand takes so long to calculate that one has to manage with not more than about four terms in the sum (12.8), then frequently a Gaussian formula is the best one to apply. Thus there is another reason for continuing the study of orthogonal polynomials.

# 12.3 The characterization of orthogonal polynomials

The recurrence relation of Theorem 11.3 is not always the most convenient method for calculating orthogonal polynomials. Some other highly useful techniques come from the following characterization theorem.

# Theorem 12.5

Let $\{ w ( x ) ; a \leqslant x \leqslant b \}$ be any continuous function. The function $\phi _ { k + 1 }$ in $\mathcal { C } [ a , b ]$ satisfies the orthogonality conditions

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { P } _ { k } ,
$$

if and only if there exists a $( k + 1 )$ - times differentiable function $\{ u ( x ) ; a \leqslant$ $x \leqslant b \}$ that satisfies the equations

$$
w ( x ) \phi _ { k + 1 } ( x ) = u ^ { ( k + 1 ) } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

and

$$
u ^ { ( i ) } ( a ) = u ^ { ( i ) } ( b ) = 0 , \qquad i = 0 , 1 , \ldots , k .
$$

Proof. If equations (12.20) and (12.21) hold, then integration by parts gives the identity

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k + 1 } ( x ) p ( x ) \mathrm { d } x = ( - 1 ) ^ { k + 1 } \int _ { a } ^ { b } u ( x ) p ^ { ( k + 1 ) } ( x ) \mathrm { d } x .
$$

Therefore, because of the term $p ^ { ( k + 1 ) } ( x )$ ,the orthogonalitycondition (12.19) is obtained when $p$ is in $\mathcal { P } _ { k }$

Conversely,when equation (12.19) is satisfied, we let $\pmb { u }$ be defined by expression (12.20), where the constants of integration are chosen to give the values

$$
u ^ { ( i ) } ( a ) = 0 , \qquad i = 0 , 1 , \ldots , k .
$$

Expression (12.20) is substituted in the integral (12.19).For each integer j in $[ 0 , k ] ,$ we let ${ \pmb p } = { \pmb p } _ { j }$ be the polynomial

$$
p _ { j } ( x ) = ( b - x ) ^ { j } , \qquad a \leqslant x \leqslant b ,
$$

and we apply integration by parts $( j + 1 )$ times to the left-hand side of expression (12.19). Thus we obtain the equation

$$
\begin{array} { l } { { [ ( - 1 ) ^ { j } u ^ { ( k - j ) } ( x ) p _ { j } ^ { ( j ) } ( x ) ] _ { a } ^ { b } } } \\ { { \displaystyle \quad + ( - 1 ) ^ { j + 1 } \int _ { a } ^ { b } u ^ { ( k - j ) } ( x ) p _ { j } ^ { ( j + 1 ) } ( x ) \mathrm { d } x = 0 . } } \end{array}
$$

Because $p _ { j } ^ { ( j + 1 ) }$ is zero,i follows that ${ \pmb u } ^ { ( k - j ) } ( { \pmb b } )$ is zero for $j = 0 , 1 , \ldots , k ,$ which completes the proof of the theorem.□

In order to apply this theorem to generate orthogonal polynomials, it is necessary to identify a function $\pmb { u }$ ,satisfying the conditions(12.21),such that the function $\phi _ { k + 1 }$ ,defined by equation (12.2O), is a polynomial of degree $( k + 1 )$ . There is no automatic method of identification,but in many important cases the required function $\pmb { u }$ is easy to recognize. For example, if we satisfy the equations (12.21) by leting $\pmb { u }$ be the function

$$
u ( x ) = ( x - a ) ^ { k + 1 } ( x - b ) ^ { k + 1 } , \qquad a \leqslant x \leqslant b ,
$$

then it follows that $\phi _ { k + 1 }$ is in $\mathcal { P } _ { k + 1 }$ when the weight function w is constant. In other words the polynomials

$$
\phi _ { j } ( x ) = \frac { d ^ { j } } { d x ^ { j } } [ ( x - a ) ^ { j } ( x - b ) ^ { j } ] , \qquad j = 0 , 1 , 2 , \ldots ,
$$

satisfy the orthogonality conditions

$$
\int _ { a } ^ { b } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \neq j .
$$

Many of the families of orthogonal polynomials that have been given special names can be obtained from Theorem 12.5.Each family is characterized by a weight function $\{ w ( x ) ; a \leqslant x \leqslant b \}$ . For example, if $\pmb { \alpha }$ and $\beta$ are real constants that are both greater than minus one, then the polynomials $\{ \phi _ { j } ; j = 0 , 1 , 2 , \ldots \}$ that satisfy the orthogonality conditions

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x } = 0 , \qquad i \neq j ,
$$

are called Jacobi polynomials.In this case we require the function (12.20) to be a polynomial of degree $( k + 1 )$ multiplied by the weight function $\{ ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } ; - 1 \leqslant x \leqslant 1 \}$ . Therefore we let $\pmb { u }$ be the function

$$
u ( x ) = ( 1 - x ) ^ { \alpha + k + 1 } ( 1 + x ) ^ { \beta + k + 1 } , \qquad - 1 \leqslant x \leqslant 1 .
$$

Because condition (12.21） is satisfied, it follows that the Jacobi polynomials are defined by the equation

$$
\begin{array} { r } { \phi _ { j } ( x ) = ( 1 - x ) ^ { - \alpha } ( 1 + x ) ^ { - \beta } \displaystyle \frac { \mathrm { d } ^ { j } } { \mathrm { d } x ^ { j } } \left[ ( 1 - x ) ^ { \alpha + j } ( 1 + x ) ^ { \beta + j } \right] , } \\ { j = 0 , 1 , 2 , \ldots , } \end{array}
$$

which is called Rodrigue's formula.

In the special case when the range of $x$ is[-1,1] and when $\alpha = \beta = 0$ ， the Jacobi polynomials are called the Legendre polynomials. If instead, for this range of $x _ { i }$ we let $\alpha = \beta = - \frac { 1 } { 2 }$ ，then we obtain the Chebyshev polynomials, that we met for the first time in Chapter 4.Further attention is given to the Chebyshev polynomials in the next section, because they provide least squares approximation operators that are important to the work of Chapter 17.

We may allow the range of $\pmb { x }$ to be infinite in Theorem 12.5, provided that the integral (12.19) is well defined. For example,because it is necessary sometimes to integrate functions that decay exponentially, there is a need for Gaussian quadrature formulae of the type

$$
\int _ { 0 } ^ { \infty } \mathrm { e } ^ { - x } f ( x ) \mathrm { d } x \approx \sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } ) .
$$

Therefore, in order to make use of Theorem 12.3,we seek polynomials $\{ \phi _ { j } \in \mathcal { P } _ { i } ; j = 0 , 1 , 2 , . . . \}$ that satisfy the conditions

$$
\int _ { 0 } ^ { \infty } \mathrm { e } ^ { - x } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \ne j ,
$$

which are called Laguerre polynomials. If $\pmb { u }$ is the function

$$
u \left( x \right) = \mathrm { e } ^ { - x } x ^ { k + 1 } , \qquad 0 \leqslant x < \infty ,
$$

in Theorem 12.5, then the conditions (12.21） are obtained,and the function $\phi _ { k + 1 }$ ，defined by equation (12.20)，is in $\mathcal { P } _ { k + 1 }$ .Hence the Laguerre polynomials have the values

$$
\phi _ { j } ( x ) = \mathtt { e } ^ { x } { \frac { \mathrm { d } ^ { j } } { \mathrm { d } x ^ { j } } } ( \mathtt { e } ^ { - x } x ^ { j } ) , \qquad j = 0 , 1 , 2 , \ldots . . . .
$$

Similarly, the Hermite polynomials

$$
\phi _ { j } ( x ) = { \bf e } ^ { x ^ { 2 } } { \frac { { \bf d } ^ { j } } { { \bf d } x ^ { j } } } ( { \bf e } ^ { - x ^ { 2 } } ) , \qquad j = 0 , 1 , 2 , \ldots ,
$$

obey the orthogonality conditions

$$
\int _ { - \infty } ^ { \infty } \mathbf { e } ^ { - x ^ { 2 } } \phi _ { i } ( x ) \phi _ { j } ( x ) \mathrm { d } x = 0 , \qquad i \neq j .
$$

It is possible to deduce from each of the expressions (12.31), (12.35) and (12.36) that each family of orthogonal polynomials satisfies a three term recurrence relation. Thus,in these three cases, algebraic expressions can be found for the coefficients $\{ \alpha _ { j } ; ~ j = 0 , 1 , 2 , \ldots \}$ and $\{ \beta _ { j } ; j =$ $1 , 2 , 3 , \ldots \}$ that occur in Theorem 11.3.

# 12.4 The operator $\pmb { R _ { n } }$

The operator $\scriptstyle { R _ { n } }$ is a linear projection from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ .For each $f$ in $\mathcal { C } [ - 1 , 1 ] , R _ { n } f$ is defined to be the element of ${ \mathcal { P } } _ { n }$ that minimizes the expression

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ^ { 2 } ) ^ { - \frac { 1 } { 2 } } [ f ( x ) - p ( x ) ] ^ { 2 } \mathrm { d } x } , \qquad p \in \mathscr { P } _ { n } .
$$

Therefore Theorem 11.2 shows that $\scriptstyle R _ { n } f$ is the function

$$
R _ { n } f = \sum _ { j = 0 } ^ { n } { \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } } \phi _ { j } ,
$$

where the scalar product has the value

$$
( \phi _ { j } , f ) = \int _ { - 1 } ^ { 1 } \big ( 1 - x ^ { 2 } \big ) ^ { - \frac { 1 } { 2 } } \phi _ { j } ( x ) f ( x ) \ : \mathrm { d } x ,
$$

provided that the polynomials $\left\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , \ldots , n \right\}$ are mutually orthogonal. Three properties of $\scriptstyle { R _ { n } }$ that are proved later are that its norm is quite small, it is closely related to Fourier approximation, and, if $f$ is in $\mathcal { P } _ { n + 1 }$ ，then $\scriptstyle R _ { n } f$ is the best minimax approximation from $\mathcal { P } _ { n }$ to $f .$ The calculation of $\scriptstyle { R _ { n } f }$ is helped by the fact that the functions $\{ \phi _ { j } ; j =$ $0 , 1 , \ldots , n \}$ in equation (12.39) are Chebyshev polynomials,which is established in the next theorem.

# Theorem 12.6

The Chebyshev polynomials

$$
T _ { j } ( x ) = \cos { ( j \theta ) } , \qquad x = \cos { \theta } ,
$$

satisfy the orthogonality conditions

$$
\int _ { - 1 } ^ { 1 } { ( 1 - x ^ { 2 } ) ^ { - { \frac { 1 } { 2 } } } T _ { j } ( x ) T _ { k } ( x ) } \mathrm { d } x = 0 , \qquad j \neq k .
$$

Prcof. By letting $\scriptstyle { \pmb { x } } = \cos { \pmb { \theta } }$ in the integral (12.42),it follows that the integral has the value

$$
{ \begin{array} { r l } & { { \displaystyle \int _ { 0 } ^ { \pi } \cos \left( j \theta \right) \cos \left( k \theta \right) \mathrm { d } \theta } } \\ & { \quad = { \frac { 1 } { 2 } } \displaystyle \int _ { 0 } ^ { \pi } \left\{ \cos \left[ ( j + k ) \theta \right] + \cos \left[ ( j - k ) \theta \right] \right\} \mathrm { d } \theta } \\ & { \quad = 0 , \quad \quad j \neq k , } \end{array} }
$$

which is the required result.□

It is now straightforward to deduce that $\scriptstyle R _ { n } f$ is the best minimax approximation from $\mathcal { P } _ { n }$ to $f$ when $f$ is a polynomial of degree $( n + 1 )$ .In this case the error function $\left( f - R _ { n } f \right)$ is in $\mathscr { P } _ { n + 1 }$ and, by Theorem 11.1, it is orthogonal to all elements of $\mathcal { P } _ { n }$ .Hence,by Theorem 12.1,it is a multiple of a polynomial that is independent of $f .$ Theorem 12.6 shows that we may let this fixed polynomial be $T _ { n + 1 }$ . Therefore the approximation $\scriptstyle { R _ { n } f }$ satisfies the characterization condition, given in Theorem 7.2,for the best minimax approximation from $\mathcal { P } _ { n }$ to $f .$

When we claimed that the norm of the operator $\scriptstyle { R _ { n } }$ is quite small, we did not have in mind the operator norm that is induced by the definition

$$
\left\| f \right\| = ( f , f ) ^ { \frac 1 2 } , \qquad f \in \mathcal { C } [ - 1 , 1 ] ,
$$

where the scalar product has the value (12.4O). This case is rather uninteresting, because equation (11.14) and the fact that $\scriptstyle { R _ { n } }$ is a projection imply that $\left\| R _ { n } \right\|$ is one. Instead, the following theorem gives the value of $\left\| R _ { n } \right\|$ that is induced by the maximum norm

$$
\| f \| _ { \infty } = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | f ( x ) | , \qquad f \in { \mathcal { C } } [ - 1 , 1 ] .
$$

# Theorem 12.7

The norm of the operator $\scriptstyle { R _ { n } }$ has the value

$$
\begin{array} { l } { \displaystyle \| R _ { n } \| _ { \infty } = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } \left| \frac { \sin { \big [ ( n + \frac { 1 } { 2 } ) \theta \big ] } } { \sin { ( \frac { 1 } { 2 } \theta ) } } \right| \mathrm { d } \theta } \\ { \displaystyle \quad = \frac { 1 } { 2 n + 1 } + \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \frac { 1 } { j } \tan { \left( \frac { j \pi } { 2 n + 1 } \right) } , } \end{array}
$$

with respect to the $\infty$ -norm (12.45).

Proof. Not all of the steps of the proof are given explicitly, because the details are rather tedious.First we let the functions $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ in the definition (12.39) be the Chebyshev polynomials $\{ T _ { j } ; j = 0 , 1 , \dots , n \}$ We make the change of variable $\scriptstyle { \pmb { x } } = \cos { \pmb { \theta } }$ in the integrals that occur, and we calculate the denominators of expression (12.39) analytically. Thus, for all values of $t$ in $[ 0 , \pi ] ,$ . we obtain the equation

$$
\begin{array} { r } { ( R _ { n } f ) ( \cos t ) = \displaystyle \frac { 2 } { \pi } \sum _ { j = 0 } ^ { n } \int _ { \theta = 0 } ^ { \pi } \cos \big ( j \theta \big ) f ( \cos \theta ) \mathrm { d } \theta \cos ( j t ) } \\ { = \displaystyle \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } f ( \cos \theta ) \sum _ { j = 0 } ^ { n } \cos \big ( j \theta \big ) \cos \big ( j t \big ) \mathrm { d } \theta , } \end{array}
$$

where the prime on the summation sign indicates that the first term is halved. The required value of $\| R _ { n } \|$ is the least upper bound on expression (12.47） subject to the conditions $0 \leqslant t \leqslant \pi$ and $\| f \| _ { \infty } \leqslant 1$ By taking the supremum over $f ,$ we deduce the value

$$
\left\| R _ { n } \right\| = \operatorname* { m a x } _ { t } \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } \bigg | \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \cos \left( j t \right) \bigg | \ \mathrm { d } \theta .
$$

We express the product cos $( j \pmb \theta )$ cos $\left( j t \right)$ in terms of cos $[ j ( \pmb \theta + t ) ]$ and

cos $[ j ( \pmb \theta - \pmb t ) ] ,$ , and we extend the range of integration. Hence we obtain the bound

$$
\begin{array} { l } { \displaystyle \| R _ { n } \| \leqslant \operatorname* { m a x } _ { t } \frac { 1 } { 2 \pi } \int _ { \theta = - \pi } ^ { \pi } \left\{ \left| \sum _ { j = 0 } ^ { n } \cos \left[ j ( \theta + t ) \right] \right| \right. } \\ { \displaystyle \left. + \left| \sum _ { j = 0 } ^ { n } \cos \left[ j ( \theta - t ) \right] \right| \right\} \mathrm { d } \theta . } \end{array}
$$

By periodicity the right-hand side of this inequality is independent of $t .$ Therefore, because expressions (12.48) and (12.49) are equal when $\pmb { t = 0 }$ ， we have the identity

$$
\left\| R _ { n } \right\| = \frac { 2 } { \pi } \int _ { \theta = 0 } ^ { \pi } \left| \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \right| \mathrm { d } \theta .
$$

The first part of expression (12.46) now follows from the elementary equation

$$
\sum _ { j = 0 } ^ { n } \cos { ( j \theta ) } = \textstyle { \frac { 1 } { 2 } } \sin { [ ( n + \textstyle { \frac { 1 } { 2 } } ) \theta ] } / \sin { ( \textstyle { \frac { 1 } { 2 } } \theta ) } .
$$

We see that this result implies that the zeros of the integrand (2.50) occur when $\pmb \theta$ has the values

$$
\theta _ { k } = k \pi / ( n + \textstyle { \frac { 1 } { 2 } } ) , \qquad k = 0 , 1 , \ldots , n .
$$

We let $\theta _ { n + 1 } = \pi ;$ , in order to obtain from equation (12.50) the expression

$$
\left\| R _ { n } \right\| = { \frac { 2 } { \pi } } \sum _ { k = 0 } ^ { n } \left( - 1 \right) ^ { k } \int _ { \theta _ { k } } ^ { \theta _ { k + 1 } } \sum _ { j = 0 } ^ { n } \cos \left( j \theta \right) \mathbf { d } \theta .
$$

Thus, by analytic integration, by exchanging the orders of summation, and by giving special attention to the contribution from $j = 0$ , the equation

$$
\begin{array} { r l r } & { } & { \left\| { \cal R } _ { n } \right\| = \displaystyle \frac { 1 } { 2 n + 1 } + \sum _ { j = 1 } ^ { n } \frac { 2 } { j \pi } \sum _ { k = 0 } ^ { n } \left( - 1 \right) ^ { k } \left[ \sin \left( j \theta \right) \right] _ { \theta _ { k } } ^ { \theta _ { k + 1 } } } \\ & { } & { = \displaystyle \frac { 1 } { 2 n + 1 } + \sum _ { j = 1 } ^ { n } \frac { 4 } { j \pi } \sum _ { k = 1 } ^ { n } \left( - 1 \right) ^ { k + 1 } \sin \left( \frac { j k \pi } { n + \frac { 1 } { 2 } } \right) } \end{array}
$$

is satisfied. By expressing the sine terms of this equation as imaginary parts of exponential functions, one can deduce the identity

$$
\sum _ { k = 1 } ^ { n } { \bigl ( } - 1 { \bigr ) } ^ { k + 1 } \sin { \biggl ( } { \frac { j k \pi } { n + { \frac { 1 } { 2 } } } } { \biggr ) } = { \frac { 1 } { 2 } } \tan { \biggl ( } { \frac { j \pi } { 2 n + 1 } } { \biggr ) } .
$$

Therefore the last line of expression (12.46) is implied by equation (12.54).□

Some values of $\| R _ { n } \|$ were calculated from equation (12.46). They are given in Table 12.1.They are so similar to the norms that are listed in the last column of Table 4.5, that the norms do not provide a good reason for preferring the operator $\scriptstyle { R _ { n } }$ to an interpolation method for calculating a polynomial approximation to a function $f .$ The main reason for our interest in the values of $\| R _ { n } \|$ is given in Chapter 17.

# 12 Exercises

12.1 Let $\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , 2 , . . . \}$ be a sequence of orthogonal polynomials,and let $\{ \xi _ { j k } ; \ k = 1 , 2 , \ldots , j \}$ be the zeros of $\phi _ { j } .$ By considering equation (11.43） when $\{ x = \xi _ { j k }$ ； $k = 1 , 2 , \ldots , j \} _ { }$ ， prove by induction that, for all positive integers $j ,$ there is a zero of $\phi _ { j }$ in each of the intervals $\{ ( \pmb { \xi } _ { j + 1 } \pmb { \mathrm { \varepsilon } } _ { k } , \pmb { \xi } _ { j + 1 } \pmb { \mathrm { \varepsilon } } _ { k + 1 } )$ ； $k = 1 , 2 , \ldots , j \}$ ·

12.2 Calculate the coefficients $\boldsymbol { w } _ { 0 } , \boldsymbol { w } _ { 1 } , \boldsymbol { x } _ { 0 }$ and $\pmb { x } _ { 1 }$ that make the approximation

$$
\int _ { 0 } ^ { 1 } x f ( x ) \mathrm { d } x \approx w _ { 0 } f ( x _ { 0 } ) + w _ { 1 } f ( x _ { 1 } )
$$

exact when $f$ is any cubic polynomial. Verify your solution by letting $f$ be a general cubic polynomial.

12.3 Let $f$ be a function in $\mathcal { C } ^ { ( 2 k + 2 ) } [ a , b ] ,$ , and let the approximation (12.8) be a Gaussian quadrature formula.Therefore the error of the approximation is unchanged if a polynomial $\pmb { p }$ of degree $( 2 k + 1 )$ is subtracted from $f .$ By letting $\pmb { p }$ be the function in $\mathscr { P } _ { 2 k + 1 }$ that satisfies the conditions $\{ p ( x _ { i } ) = f ( x _ { i } )$ ； $i = 0 , 1 , \ldots , k \}$ and $\{ p ^ { \prime } ( x _ { i } ) = f ^ { \prime } ( x _ { i } )$ ； $i = 0 , 1 , \ldots , k \}$ ，and by using an extension of Theorem 4.2, prove that the error has the value

$$
\int _ { a } ^ { b } w ( x ) \prod _ { j = 0 } ^ { k } \left( x - x _ { j } \right) ^ { 2 } \mathrm { d } x f ^ { ( 2 k + 2 ) } ( \xi ) / ( 2 k + 2 ) ! ,
$$

where $\pmb { \xi }$ is a point of $[ a , b ]$

12.4 Use equation (12.36) to generate the first six Hermite polynomials,and verify that they satisfy a three-term recurrence relation of the form that is given in Theorem 11.3.

Table 12.1. Some values of $\| R _ { n } \|$   

<table><tr><td>R.l n</td><td></td><td>n Rl</td></tr><tr><td>2</td><td>1.6422</td><td>12 2.2940</td></tr><tr><td>4</td><td>1.8801</td><td>14 2.3542</td></tr><tr><td>6</td><td>2.0290</td><td>16 2.4065</td></tr><tr><td>8</td><td>2.1377</td><td>18 2.4529</td></tr><tr><td>10</td><td>2.2234</td><td>20 2.4945</td></tr></table>

12.5 Let $\bar { p }$ be a function in $\mathcal { P } _ { k }$ ,and let $\pmb { n }$ be an integer in the range $[ 0 , k - 1 ]$ . Let the telescoping procedure of Section 8.4 be applied $( k - n )$ times to derive from $\bar { p }$ a polynomial $\pmb { p }$ in ${ \mathcal P _ { n } }$ . Prove that $p$ is the function $\pmb { R _ { n } } \bar { p }$ ，where the operator $\scriptstyle { R _ { n } }$ is defined in Section 12.4.

12.6 For any $f$ in $\mathcal { C } [ - 1 , 1 ]$ ,let $L _ { n } f$ be the polynomial in ${ \mathcal { P } } _ { n }$ that interpolates $f$ at the Chebyshev points (4.27). Given that the largest value of the sum

$$
\sum _ { k = 0 } ^ { n } { \big | } l _ { k } ( x ) { \big | } , \qquad - 1 \leqslant x \leqslant 1 ,
$$

occurs when $x = - 1$ and 1, where $l _ { k }$ is the cardinal function (4.3), deduce that the $\infty$ -norm of the operator $L _ { n }$ has the value

$$
\| L _ { n } \| _ { \infty } = { \frac { 1 } { n + 1 } } \sum _ { j = 0 } ^ { n } \tan \left[ { \frac { ( j + { \frac { 1 } { 2 } } ) \pi } { 2 ( n + 1 ) } } \right] .
$$

12.7 Let $\{ \phi _ { j } \in \mathcal { P } _ { j } ; j = 0 , 1 , 2 , . . . \}$ be a sequence of polynomials that are orthogonal with respect to a positive integrable weight function $\{ w ( x )$ ； $a \leqslant x \leqslant b \}$ ，and let $\{ \xi _ { j k } ; k = 1 , 2 , \ldots , j \}$ be the zeros of $\phi _ { j }$ .Deduce from the theory of Gaussian quadrature that, if $\pmb { p }$ is in $\mathcal { P } _ { j } ,$ then the inequality

$$
\int _ { a } ^ { b } { \left[ p ( x ) \right] ^ { 2 } } w ( x ) \mathrm { d } x \leqslant \int _ { a } ^ { b } w ( x ) \mathrm { d } x \operatorname* { m a x } _ { 1 \leqslant k \leqslant j + 1 } { \left[ p ( \xi _ { j + 1 } _ { k } ) \right] ^ { 2 } }
$$

is satisfied. For any function $f$ in ${ \mathcal { C } } [ a , b ] ,$ let $p _ { j } ^ { * }$ be the best minimax approximation from $\mathcal { P } _ { j }$ to $f ,$ let $L f$ be the element of $\mathcal { P } _ { j }$ that interpolates $f$ at the zeros of $\phi _ { j + 1 }$ ，and let $p$ be the polynomial $( p _ { j } ^ { * } - L _ { j } f )$ . Thus,using the triangle inequality

$$
\| f - L _ { j } f \| _ { 2 } \leqslant \| f - p _ { j } ^ { * } \| _ { 2 } + \| p \| _ { 2 } ,
$$

obtain the‘Erdos Turan theorem'

$$
\operatorname* { l i m } _ { j \to \infty } \int _ { a } ^ { b } { \left[ f ( x ) - ( L _ { j } f ) ( x ) \right] ^ { 2 } } w ( x ) \mathrm { d } x = 0 .
$$

12.8 Let $[ a , b ]$ be the interval $[ - 1 , \ 1 ] ,$ and let $w$ be the function $\{ w ( x ) = x ^ { 2 }$ ； $- 1 \leqslant x \leqslant 1 \}$ . Prove that,if $\pmb { k }$ is even, then the function

$$
\phi _ { k + 1 } ( x ) = { \frac { 1 } { x ^ { 2 } } } { \frac { \mathrm { d } ^ { k + 1 } } { \mathrm { d } x ^ { k + 1 } } } [ ( 1 - x ^ { 2 } ) ^ { k + 1 } ( 1 + x ^ { 2 } ) ] , \qquad - 1 \leqslant x \leqslant 1 ,
$$

is in $\mathcal { P } _ { k + 1 }$ ,and satisfies the orthogonality condition (12.19).Find a similar definition of a polynomial $\phi _ { k + 1 }$ that satisfies equation

(12.19)when $\pmb { k }$ is odd. Check that your definition is correct when $k = 3$

12.9Prove that the Legendre polynomials

$$
\phi _ { j } ( x ) = { \frac { \mathbf { d } ^ { j } } { \mathbf { d } x ^ { j } } } [ ( x ^ { 2 } - 1 ) ^ { j } ] , \qquad - 1 \leqslant x \leqslant 1 , \qquad j = 0 , 1 , 2 , \ldots ,
$$

satisfy the three-term recurrence relation

$$
\phi _ { j + 1 } ( x ) = ( 4 j + 2 ) x \phi _ { j } ( x ) - 4 j ^ { 2 } \phi _ { j - 1 } ( x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

A good method of solution comes from expressing each term in the form

The middle term has this form, because the Leibniz formula for calculating the jth derivative of a product gives the identity

$$
\frac { \mathrm { d } ^ { j - 1 } } { \mathrm { d } x ^ { j - 1 } } \left\{ \frac { \mathrm { d } } { \mathrm { d } x } \left[ x ( x ^ { 2 } - 1 ) ^ { j } \right] \right\} = x \phi _ { j } ( x ) + j \frac { \mathrm { d } ^ { j - 1 } } { \mathrm { d } x ^ { j - 1 } } [ ( x ^ { 2 } - 1 ) ^ { j } ] .
$$

12.10Prove that the Legendre polynomials, defined in Exercise 12.9, satisfy the equation

$$
( x ^ { 2 } - 1 ) \phi _ { j } ^ { \prime } ( x ) = j x \phi _ { j } ( x ) - 2 j ^ { 2 } \phi _ { j - 1 } ( x ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

A convenient expression for the term $( x ^ { 2 } - 1 ) \phi _ { j } ^ { \prime } ( x )$ can be obtained by regarding the right-hand side of the definition

$$
\phi _ { j + 1 } ( x ) = { \frac { \mathrm { d } ^ { j + 1 } } { \mathrm { d } x ^ { j + 1 } } } [ ( x ^ { 2 } - 1 ) ^ { j + 1 } ]
$$

as the $( j + 1 ) \operatorname { t h }$ derivative of the product $( x ^ { 2 } - 1 ) \times ( x ^ { 2 } - 1 ) ^ { j } .$ Investigate extensions of the formulae of this exercise and the previous one to the Jacobi polynomials that are defined in Section 12.3.

# 13

# Approximation to periodic functions

# 13.1 Trigonometric polynomials

In many branches of science and engineering, periodic functions occur naturally,and there is a need to estimate periodic functions from measured data.Because the variable $x$ may be scaled if necessary,we assume that the functions $f$ that occur are in the space $\mathcal { C } _ { 2 \pi } ,$ which is the set of all continuous functions from ${ \mathcal { R } } ^ { 1 }$ to $\mathcal { R } ^ { 1 }$ that satisfy the periodicity condition

$$
f ( x + 2 \pi ) = f ( x ) , \qquad - \infty < x < \infty .
$$

In approximation calculations the set $\mathcal { A }$ of approximating functions is composed usually of functions of the form

$$
q \left( x \right) = \frac { 1 } { 2 } a _ { 0 } + \sum _ { j = 1 } ^ { n } \left[ a _ { j } \cos \left( j x \right) + b _ { j } \sin \left( j x \right) \right] , \qquad -
$$

where $\{ a _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\{ b _ { j } ; j = 1 , 2 , \ldots , n \}$ are real parameters. If $\pmb { n }$ is fixed, then $\mathcal { A }$ is a linear subspace of $\mathcal { C } _ { 2 \pi }$ of dimension $( 2 n + 1 )$ ,which we denote by ${ \mathcal { Q } } _ { n }$ . It is called the space of trigonometric polynomials of degree $\pmb { n }$ . The actual degree of the trigonometric polynomial (13.2) is the greatest integer $j$ such that at least one of the coefficients $a _ { j }$ and $b _ { j }$ is non-zero.

It is important to note that, if $j$ and $k$ are non-negative integers whose sum is not greater than $\pmb { n }$ ,then the function $\left\{ \cos ^ { \mathrm { i } } x \sin ^ { \mathrm { k } } x ; - \infty < x < \infty \right\}$ is in ${ \mathcal { Q } } _ { n }$ Thus,if $\pmb { p }$ isin ${ \mathcal { Q } } _ { m }$ and $\pmb q$ is in $\mathcal { Q } _ { n }$ ，then the product function $\{ p ( x ) q ( x ) ; - \infty < x < \infty \}$ is in $\mathcal { Q } _ { m + n }$ . We note also that the zero function is the only element of ${ \mathcal { Q } } _ { n }$ that has more than $_ { 2 n }$ zeros in the interval $[ 0 , 2 \pi )$

It is usual to calculate an approximation from ${ \mathcal { Q } } _ { n }$ to $f$ by a least squares algorithm. The main methods that are used are studied in this chapter.

First,however, it is proved that,by choosing $\pmb { n }$ to be sufficiently large, it is possible to approximate any continuous periodic function to arbitrarily high accuracy by a trigonometric polynomial.

# Theorem 13.1

For any $f$ in $\mathcal { C } _ { 2 \pi }$ and for any $\pmb \varepsilon > 0$ ,there exists a polynomial of the form (13.2) that satisfies the condition

$$
\| f - q \| _ { \infty } \leqslant \varepsilon ,
$$

where $_ n$ is a finite integer.

Proof. The function $f$ is the sum of the even and odd functions $f _ { 1 }$ and $f _ { 2 }$ that are defined by the equations

$$
\begin{array} { r l } { f _ { 1 } ( x ) = \frac { 1 } { 2 } [ f ( x ) + f ( - x ) ] , } & { \quad - \infty < x < \infty } \\ { f _ { 2 } ( x ) = \frac { 1 } { 2 } [ f ( x ) - f ( - x ) ] , } & { \quad - \infty < x < \infty } \end{array} \biggr \} .
$$

We show that $f _ { 1 }$ can be approximated to accuracy $\scriptstyle { \frac { 1 } { 4 } } \varepsilon$ and that $f _ { 2 }$ can be approximated to accuracy $\scriptstyle { \frac { 3 } { 4 } } \varepsilon$ .Thus inequality (13.3) is satisfied when $q$ is the sum of the two approximations.

In order to find a suitable approximation to $f _ { 1 }$ , we let ${ \pmb g } _ { 1 }$ be the function

$$
g _ { 1 } ( \cos x ) = f _ { 1 } ( x ) , \qquad 0 \leqslant x \leqslant \pi ,
$$

which is in $\mathcal { C } [ - 1 , 1 ]$ . Hence,by Theorem 6.1, there is an algebraic polynomial ${ p } _ { 1 }$ that satisfies the condition

$$
\begin{array} { r } { \big | g _ { 1 } ( t ) - p _ { 1 } ( t ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad - 1 \leqslant t \leqslant 1 . } \end{array}
$$

It follows that the inequality

$$
\begin{array} { r } { \big | g _ { 1 } ( \cos x ) - p _ { 1 } ( \cos x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant \pi , } \end{array}
$$

holds. We define the function $\{ q _ { 1 } ( x ) ; - \infty < x < \infty \}$ to be the trigonometric polynomial $\{ p _ { 1 } ( \cos x ) ; - \infty < x < \infty \}$ .Hence the required bound

$$
\| f _ { 1 } - q _ { 1 } \| _ { \infty } \leqslant \frac { 1 } { 4 } \varepsilon
$$

is a consequence of expressions (13.5) and (13.7),and the fact that $f _ { 1 }$ and $\pmb q _ { 1 }$ are even functions in $\mathcal { C } _ { 2 \pi } .$

In order to obtain a suitable approximation to $f _ { 2 }$ we note that the values $f _ { 2 } ( 0 )$ and $f _ { 2 } ( \pmb { \pi } )$ are both zero.We let $x _ { 0 }$ be the largest number in the interval $[ 0 , { \frac { 1 } { 2 } } \pi ]$ such that the inequality

$$
\begin{array} { r } { \big | f _ { 2 } ( x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant x _ { 0 } , } \end{array}
$$

is satisfied,and we let $x _ { 1 }$ be the smallest number in $[ \tilde { \frac { 1 } { 2 } \pi } , \pi ]$ that is allowed by the condition

$$
\begin{array} { r } { \big | f _ { 2 } ( x ) \big | \leqslant \frac { 1 } { 4 } \varepsilon , \qquad x _ { 1 } \leqslant x \leqslant \pi . } \end{array}
$$

Further, $f _ { 3 }$ is the even function in $\mathcal { C } _ { 2 \pi }$ that takes the values

$$
f _ { 3 } ( x ) = \left\{ \begin{array} { l l } { f _ { 2 } ( x _ { 0 } ) / \sin x _ { 0 } , } & { 0 \leqslant x \leqslant x _ { 0 } , } \\ { f _ { 2 } ( x ) / \sin x , } & { x _ { 0 } \leqslant x \leqslant x _ { 1 } , } \\ { f _ { 2 } ( x _ { 1 } ) / \sin x _ { 1 } , } & { x _ { 1 } \leqslant x \leqslant \pi , } \end{array} \right.
$$

on $[ 0 , \pi ]$ .By applying to $f _ { 3 }$ the method that was used to approximate $f _ { 1 }$ ,it follows that there is an even trigonometric polynomial, $\pmb { q _ { 3 } }$ say, such that the inequality

$$
\| f _ { 3 } - q _ { 3 } \| _ { \infty } \leqslant \frac { 1 } { 4 } \varepsilon
$$

holds.We show that the function $\{ q _ { 2 } ( x ) = \sin x q _ { 3 } ( x ) ; - \infty < x < \infty \}$ is a sufficiently accurate approximation to $f _ { 2 }$ . When $\pmb { x }$ is in $[ 0 , x _ { 0 } ]$ we have the bound

$$
\begin{array} { r l } & { \left| f _ { 2 } ( x ) - q _ { 2 } ( x ) \right| = \left| f _ { 2 } ( x ) - \sin x q _ { 3 } ( x ) \right| } \\ & { \qquad \leqslant \left| f _ { 2 } ( x ) \right| + \left| \sin x f _ { 3 } ( x ) \right| + \sin x \left| f _ { 3 } ( x ) - q _ { 3 } ( x ) \right| } \\ & { \qquad \leqslant \frac { 3 } { 4 } \varepsilon , } \end{array}
$$

where the last line depends on the definitions of $x _ { 0 } , f _ { 3 }$ and $\pmb { q } _ { 3 }$ . Similarly this bound is satisfied when $\pmb { x }$ is in $[ x _ { 1 } , \pi ]$ .Moreover, when $x$ is in $[ x _ { 0 } , x _ { 1 } ] ,$ the inequality

$$
\begin{array} { l } { { \left| f _ { 2 } ( x ) - q _ { 2 } ( x ) \right| = \sin { x } \left| f _ { 3 } ( x ) - q _ { 3 } ( x ) \right| } } \\ { { \leqslant \frac { 1 } { 4 } \varepsilon } } \end{array}
$$

holds. Because these remarks give the condition

$$
\big | f _ { 2 } ( x ) - q _ { 2 } ( x ) \big | \leqslant \frac { 3 } { 4 } \varepsilon , \qquad 0 \leqslant x \leqslant \pi ,
$$

the required bound

$$
\| f _ { 2 } - q _ { 2 } \| _ { \infty } \leqslant \frac { 3 } { 4 } \varepsilon
$$

follows from the fact that $f _ { 2 }$ and $q _ { 2 }$ are both odd functions in $\mathcal { C } _ { 2 \pi }$ The theorem is proved.□

# 13.2 The Fourier series operator $\pmb { S _ { n } }$

$S _ { n }$ is an operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ . For each $f$ in $\mathcal { C } _ { 2 \pi }$ ,the function $s _ { n } f$ is defined to be the trigonometric polynomial that minimizes the least squares distance function

$$
d ( f , q ) = \left[ \int _ { - \pi } ^ { \pi } \{ f ( x ) - q ( x ) \} ^ { 2 } \mathrm { d } x \right] ^ { \frac { 1 } { 2 } } , \qquad q \in { \mathcal { Q } } _ { n } .
$$

Therefore $S _ { n }$ is a linear projection. It has several interesting theoretical properties.For example, it is proved in Chapter 17 that $\| \boldsymbol { S _ { n } } \| _ { \infty }$ is less than or equal to the norm of any other linear projection from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that leaves functions in ${ \mathcal { Q } } _ { n }$ unchanged. Moreover,almost all of the usual algorithms for calculating trigonometric approximations are derived from $\pmb { S _ { n } }$

In order to apply the results of Chapter 11 to $\pmb { S _ { n } }$ we let $( f , g )$ be the scalar product

$$
( f , g ) = \int _ { - \pi } ^ { \pi } f ( x ) g ( x ) \mathrm { d } x ,
$$

for all functions $f$ and $\pmb { g }$ in $\mathcal { C } _ { 2 \pi } ,$ which is consistent with the distance function (13.17). We note that the orthogonality conditions

$$
\left. { \begin{array} { l } { \displaystyle \int _ { - \pi } ^ { \pi } \cos \left( j x \right) \cos \left( k x \right) \mathrm { d } x = 0 , \quad \ j \neq k } \\ { \displaystyle \int _ { - \pi } ^ { \pi } \sin \left( j x \right) \sin \left( k x \right) \mathrm { d } x = 0 , \quad \ j \neq k } \\ { \displaystyle \int _ { - \pi } ^ { \pi } \cos \left( j k \right) \sin \left( k x \right) \mathrm { d } x = 0 } \end{array} } \right\} ,
$$

are satisfied, where $j$ and $\pmb { k }$ are any non-negative integers, which give the following expressions for the coefficients of the trigonometric polynomial $\textstyle S _ { n } f .$

# Theorem 13.2

The trigonometric polynomial (13.2） minimizes the distance function (13.17) if and only if the coefficients have the values

and

$$
a _ { j } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \cos \left( j \theta \right) \mathrm { d } \theta , \qquad j = 0 , 1 , \ldots , n ,
$$

$$
b _ { j } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \sin \left( j \theta \right) \mathrm { d } \theta , \qquad j = 1 , 2 , \ldots , n .
$$

Proof. The orthogonality conditions (13.19) and Theorem 11.2 imply that the required coefficients satisfy the equations

and

$$
\begin{array} { r l } & { \frac { 1 } { 2 } a _ { 0 } = ( f , \cos { \{ 0 . \} } ) / ( \cos { \{ 0 . \} } , \cos { \{ 0 . \} } ) , } \\ & { a _ { j } = ( f , \cos { \{ j . \} } ) / ( \cos { \{ j . \} } , \cos { \{ j . \} } ) , \quad \ j = 1 , 2 , \ldots , n , } \end{array}
$$

$$
b _ { j } = ( f , \sin \{ j . \} ) / ( \sin \{ j . \} , \sin \{ j . \} ) , \qquad j = 1 , 2 , \ldots , n ,
$$

where cos $\{ j . \}$ and sin $\{ j . \}$ are the functions $\{ \cos { ( j x ) } ; - \infty < x < \infty \}$ and $\{ \sin { ( j x ) } ; - \infty < x < \infty \}$ respectively. The values (13.20) and (13.21) follow from the definition of the scalar product, where each denominator is integrated analytically.□

Because Theorem 13.1 implies that the least value of expression (13.17) tends to zero as $^ { n }$ tends to infinity, one expects the sequence of trigonometric polynomials $\{ S _ { n } f ; n = 1 , 2 , 3 , . . . \}$ to converge uniformly to $f ,$ except perhaps in some pathological cases. However, the convergence properties are not shown well by Theorem 13.2. Therefore another expression for $s _ { n }$ is derived that shows explicitly the relation between $s _ { n } f$ and $f _ { - }$

# Theorem 13.3

The value of $s _ { n } f$ at the point $\pmb { x }$ is the expression

$$
( S _ { n } f ) ( x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } { \frac { \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] } { 2 \sin \left( { \frac { 1 } { 2 } } \theta \right) } } f ( x + \theta ) \mathrm { d } \theta .
$$

Proof. By substituting the values (13.20) and(13.21) in equation (13.2), and by reversing the order of integration and summation, we deduce the identity

$$
\begin{array} { r l } { ( S _ { n } f ) ( x ) = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left\{ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \left[ \cos { ( j x ) } \cos { ( j \theta ) } \right. \right. } & { { } } \\ { \displaystyle \left. \left. + \sin { ( j x ) } \sin { ( j \theta ) } \right] \right\} f ( \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left\{ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \cos { [ j ( \theta - x ) ] } \right\} f ( \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \left[ \frac { 1 } { 2 } + \displaystyle \sum _ { j = 1 } ^ { n } \cos { ( j \theta ) } \right] f ( x + \theta ) \mathrm { d } \theta } \\ { \displaystyle } & { { } = \displaystyle \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } \frac { \sin { [ ( n + \frac { 1 } { 2 } ) \theta ] } } { 2 \sin { ( \frac { 1 } { 2 } \theta ) } } f ( x + \theta ) \mathrm { d } \theta , } \end{array}
$$

where in the fourth line we have changed the variable of integration by the addition of the parameter $\pmb { x }$ , and where the last line depends on equation (12.51). This is the required result.□

It is interesting to consider equation (13.25) when $\pmb { n }$ tends to infinity. If $_ \pmb { \alpha }$ and $\beta$ are any two fixed points of the range $[ - \pi , \pi ]$ ,and if the interval $[ \alpha , \beta ]$ does not contain zero, then the rapid periodic oscillations of the function $\{ \sin { [ ( n + \frac { 1 } { 2 } ) \theta ] } ; - \pi \leqslant \theta \leqslant \pi \}$ cause the integral

$$
{ \frac { 1 } { \pi } } \int _ { \alpha } ^ { \beta } \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] { \frac { f ( x + \theta ) } { 2 \sin \left( { \frac { 1 } { 2 } } \theta \right) } } \mathrm { d } \theta
$$

to tend to zero. It follows that $( S _ { n } f ) ( x )$ tends to be dominated by the behaviour of $\left\{ f ( x + \theta ) ; - \pi \leqslant \theta \leqslant \pi \right\}$ when $| \pmb \theta |$ is small. It therefore seems plausible that the limit as $\pmb { n }$ tends to infinity of expression (13.25) is unchanged if $f ( x + \theta )$ is replaced by $f ( x )$ . When this suggestion is valid, then it is easy to deduce that $\{ ( S _ { n } f ) ( x ) ; n = 1 , 2 , 3 , . . . \}$ converges to $f ( x )$ ， but it is shown in Chapter 17 that there exist functions $f$ in $\mathcal { C } _ { 2 \pi }$ such that the sequence of maximum errors $\{ \| f - S _ { n } f \| _ { \infty }$ ； $n = 1 , 2 , 3 , \ldots \}$ fails to tend to zero. In Chapter 16, however, it is proved that $\{ S _ { n } f ; n = 1 , 2 , 3 , . . . \}$ does converge uniformly to $f ,$ provided that some mild smoothness conditions are satisfied.

We may use Theorem 13.3 to obtain the value of $\| \pmb { S _ { n } } \| _ { \infty }$ . Expression (13.25) shows that, if $f$ is in $\mathcal { C } _ { 2 \pi }$ and if $\| f \| _ { \infty }$ is not greater than one, then the least upper bound on $| ( S _ { n } f ) ( x ) |$ has the value

$$
{ \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } \left| { \frac { \sin { [ ( n + { \frac { 1 } { 2 } } ) \theta ] } } { 2 \sin { ( { \frac { 1 } { 2 } } \theta ) } } } \right| { \bf d } \theta .
$$

Because this expression is independent of $\pmb { x }$ , it must be equal to $\| \boldsymbol { S _ { n } } \| _ { \infty }$ It follows from Theorem 12.7 that the equation

$$
\| S _ { n } \| _ { \infty } = \| R _ { n } \| _ { \infty } , \qquad n = 1 , 2 , 3 , \ldots ,
$$

is satisfied. Therefore Theorem 3.1 and Table 12.1 imply that when $n = 2 0$ , for example, the error $\| S _ { 2 0 } f - f \| _ { \infty }$ is within the factor 3.4945 of the least maximum error that can be achieved when $f$ is approximated by a trigonometric polynomial of degree twenty. Results of this kind help to justify the attention that is given to the approximation operator ${ \pmb S } _ { n }$ ·

The coefficients (13.20) and (13.21) of the trigonometric polynomial $s _ { n } f$ have some useful properties. We see that ${ \pmb a } _ { j }$ and $b _ { j }$ are independent of $\pmb { n }$ . We derive some other properties from the equation

$$
\| f - S _ { n } f \| _ { 2 } ^ { 2 } + \| S _ { n } f \| _ { 2 } ^ { 2 } = \| f \| _ { 2 } ^ { 2 } ,
$$

which is a special case of equation (11.14). Because analytic integration and the orthogonality conditions (13.19) imply that the 2-norm of the function (13.2) has the value

$$
\| q \| _ { 2 } = { \biggl [ } { \textstyle \frac { 1 } { 2 } } \pi a _ { 0 } ^ { 2 } + \pi ~ \sum _ { j = 1 } ^ { n } ~ ( a _ { j } ^ { 2 } + b _ { j } ^ { 2 } ) { \biggr ] } ^ { \frac { 1 } { 2 } } ,
$$

it follows from equation (13.30) that the coefficients (13.20) and (13.21) satisfy the condition

$$
{ \scriptstyle { \frac { 1 } { 2 } } } \pi a _ { 0 } ^ { 2 } + \pi \sum _ { j = 1 } ^ { n } ( a _ { j } ^ { 2 } + b _ { j } ^ { 2 } ) \leqslant \int _ { - \pi } ^ { \pi } [ f ( x ) ] ^ { 2 } { \mathrm { d } } x ,
$$

which is known as ‘Bessel's inequality'. Hence the sequences $\{ a _ { j } ; j =$ $0 , 1 , 2 , \ldots \}$ and $\{ b _ { j } ; j = 1 , 2 , 3 , . . . \}$ tend to zero. Further, the difference between the two sides of expression (13.32) is a measure of the accuracy of the approximation $s _ { n } f$ to $f ,$ because equation (13.30) shows that the difference is equal to $\| f - S _ { n } f \| _ { 2 } ^ { 2 }$ . Theorem 13.1 and the definition of $\pmb { S } _ { n }$ imply that the sequence { $\left\| f - S _ { n } f \right\| _ { 2 }$ ； $n = 1 , 2 , 3 , \ldots \}$ converges to zero. Therefore inequality (13.32) becomes an equality in the limit as $\pmb { n }$ tends to infinity.

# 13.3 The discrete Fourier series operator

It happens often in practice that, instead of knowing the value of $f ( x )$ for all $\pmb { x }$ in $[ - \pi , \pi ] ,$ ，the function is given on only a discrete set of points. Even when $f ( x )$ can be calculated for any $x _ { i }$ , it may be necessary to make numerical approximations to the integrals (13.20) and (13.21). Therefore,in this section, we consider the important problem of obtaining an approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi } ,$ using only the equally spaced function values

$$
f { \left( \frac { 2 \pi k } { N } \right) } , \qquad k = 0 , 1 , \dots , N - 1 .
$$

By periodicity the value of $f ( 2 \pi k / N )$ is known for all integral values of $k$ · There is no loss of generality in supposing that $f ( 0 )$ is available, because,if we are given the function values

$$
f { \left( \frac { 2 \pi k } { N } + \alpha \right) } , \qquad k = 0 , 1 , \ldots , N - 1 ,
$$

for some constant $_ \alpha$ ,then the change of variable $\pmb \theta = \pmb x - \pmb \alpha$ can be made. The data (13.34） are suitable for the approximation of the function $\{ f ( \theta + \alpha ) ; - \infty < \theta < \infty \}$ ，which gives a trigonometric polynomial in $\pmb \theta .$ Hence the approximation is also trigonometric polynomial in $x$

The‘discrete Fourier series approximation' from $\mathcal { Q } _ { n }$ to the function $f$ is obtained from the data (13.33). It has the form (13.2)，where the coefficients $\{ a _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\{ b _ { j } ; j = 1 , 2 , \ldots , n \}$ are defined by replacing the integrals of expressions (13.20) and (13.21) by estimates of the form

$$
\frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } g ( \theta ) \mathrm { d } \theta \approx \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } g \Big ( \frac { 2 \pi k } { N } \Big ) .
$$

Hence the coefficients have the values

$$
a _ { j } = \frac 2 N \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } N \bigg ) \cos \bigg ( \frac { 2 \pi j k } N \bigg ) , \qquad j = 0 , 1 , \ldots , n ,
$$

and

$$
b _ { j } = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } { N } \bigg ) \sin \bigg ( \frac { 2 \pi j k } { N } \bigg ) , \qquad j = 1 , 2 , \ldots , n .
$$

Section 13.4 describes a way of organizing the calculation of these coefficients,so that they can all be found in only of order $N \log _ { 2 } N$ operations,provided that $N$ is a power of two. The technique is so successful that it is applied frequently for very large values of $\pmb { N }$ and $_ n$ The next theorem shows that the estimate (13.35) has some remarkably strong properties.

# Theorem 13.4

If $_ { g }$ is the function $\{ \cos { \left( j \theta \right) } ; - \infty < \theta < \infty \}$ , where $j$ is any integer that is not a positive or negative integral multiple of $N ,$ orif $\pmb { g }$ is the function $\{ \sin { ( j \theta ) } ; - \infty < \theta < \infty \}$ ，where $j$ is any integer, then the approximation (13.35) is exact.

Proof. It is clear that the estimate (13.35) is exact when $\pmb { g }$ is a constant function. In all other cases that are given in the statement of the theorem, the left-hand side of the estimate is zero, and adding or subtracting a multiple of $\pmb { N }$ to the integer $j$ does not alter the terms of the sum (13.35). Hence it is sufficient to establish the equations

$$
\sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } { N } \right) = 0 , \qquad j = 1 , 2 , \ldots , N - 1 ,
$$

and

$$
\sum _ { k = 0 } ^ { N - 1 } \sin \left( { \frac { 2 \pi j k } { N } } \right) = 0 , \qquad j = 1 , 2 , \ldots , N .
$$

Expression (13.38) holds,because, by substituting $\theta { = } 2 \pi j / N$ and $\pmb { n } = \pmb { N }$ in equation (12.51), we find the identity

$$
\begin{array} { c } { { \frac { 1 } { 2 } + \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \displaystyle \frac { 2 \pi j k } { N } \right) = \frac { 1 } { 2 } \sin \left[ ( 2 N + 1 ) \pi j / N \right] / \sin \left( \pi j / N \right) } } \\ { { \frac { 1 } { 2 } { } + \displaystyle \sum _ { j = 1 } ^ { N - 1 } \sum _ { j = 1 , 2 , . . . , N - 1 . } } } \end{array}
$$

Expression (13.39) follows from the symmetry properties of the sine function.□

Another method that suggests itself, for calculating an approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi }$ from the function values (13.33), is to minimize the sum of squares

$$
\sum _ { k = 0 } ^ { N - 1 } \bigg [ f \bigg ( \frac { 2 \pi k } { N } \bigg ) - q \bigg ( \frac { 2 \pi k } { N } \bigg ) \bigg ] ^ { 2 } , \qquad q \in \mathcal { Q } _ { n } .
$$

In this case it is appropriate to define the scalar product

$$
( f , g ) = \sum _ { k = 0 } ^ { N - 1 } f \biggl ( \frac { 2 \pi k } { N } \biggr ) g \biggl ( \frac { 2 \pi k } { N } \biggr ) ,
$$

between periodic functions that are defined on the point set $\{ 2 \pi j / N ; j$ integral}. Minimizing expression (13.41） determines the coeffcients of $\pmb q$ uniquely only if the number of coefficients does not exceed the number of data. Therefore we assume that the inequality

$$
\scriptstyle n < { \frac { 1 } { 2 } } N
$$

is satisfied. Because expressions (13.38) and (13.39) imply the orthogonality conditions

$$
\left. \begin{array} { l l } { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } N \right) \cos \left( \frac { 2 \pi l k } N \right) = 0 , } } & { { j \neq l } } \\ { { } } & { { } } \\ { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \sin \left( \frac { 2 \pi j k } N \right) \sin \left( \frac { 2 \pi l k } N \right) = 0 , } } & { { j \neq l } } \\ { { } } & { { } } \\ { { \displaystyle \sum _ { k = 0 } ^ { N - 1 } \cos \left( \frac { 2 \pi j k } N \right) \sin \left( \frac { 2 \pi l k } N \right) = 0 } } & { { } } \end{array} \right\} ,
$$

when the integers $j$ and $\iota$ are in the interval $[ 0 , { \scriptstyle { \frac { 1 } { 2 } } } N - { \scriptstyle { \frac { 1 } { 2 } } } ] ,$ , it is straightforward to obtain from Theorem 11.2 the function in ${ \mathcal { Q } } _ { n }$ that minimizes expression (13.41). We find that its coefficients have the values (13.36) and (13.37). Therefore this method of calculating $\pmb q$ is equivalent to the discrete Fourier series method. Hence，if $\begin{array} { r } { n < \frac { 1 } { 2 } N , } \end{array}$ then the discrete Fourier series operator is a projection, and it maps functions in ${ \mathcal { Q } } _ { n }$ into themselves. However, these projection properties are not obtained if $\begin{array} { r } { n \geqslant \frac { 1 } { 2 } N . } \end{array}$

# 13.4 Fast Fourier transforms

In this section we consider the calculation of the coefficients (13.36) and (13.37), when $N$ is a power of two, and when the value of $\pmb { n }$ is close to ${ \scriptstyle { \frac { 1 } { 2 } } } N .$ If each sum is evaluated separately, then the number of computer operations is of order $N ^ { 2 }$ ,but we can do better. For example, consider the two coefficients $a _ { j }$ and $\begin{array} { r } { a _ { 2 } ^ { \perp } N { _ { - } } j { * } } \end{array}$ Because the second coefficient has the value

$$
a _ { \scriptscriptstyle { 2 N - j } } = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f \bigg ( \frac { 2 \pi k } { N } \bigg ) ( - 1 ) ^ { k } \cos \bigg ( \frac { 2 \pi j k } { N } \bigg ) ,
$$

it follows that, if we sum separately over the odd and the even values of $\pmb { k }$ in expression (13.36), then we can obtain both $a _ { j }$ and $\alpha _ { 2 } ^ { 1 } N { - } j$ using little more work than the calculation of $a _ { j }$ alone. The FFT (fast Fourier transform) method is a development of this remark.

In order to describe it, we let $a [ m , \alpha , j ]$ and $b [ m , \alpha , j ]$ be the sums

$$
a [ m , \alpha , j ] = \frac { 2 } { m } \sum _ { k = 0 } ^ { m - 1 } f \Big ( \frac { 2 \pi k } { m } + \alpha \Big ) \cos \Big ( \frac { 2 \pi j k } { m } \Big )
$$

and

$$
b [ m , \alpha , j ] = \frac { 2 } { m } \sum _ { k = 0 } ^ { m - 1 } f \Big ( \frac { 2 \pi k } { m } + \alpha \Big ) \sin \Big ( \frac { 2 \pi j k } { m } \Big ) .
$$

They are useful because only a smal amount of work is required to obtain $a [ 2 m , \alpha , j ]$ and $b [ 2 m , \alpha , j ]$ from the numbers $a [ m , \alpha , j ] , a [ m , \alpha +$ $\pi / m , j ] , \ b [ m , \alpha , j ]$ and $b [ m , \alpha + \pi / m , j ]$ ， and because they are the required coefficients when $m = N$ and $\alpha = 0$ . The value of $a [ 2 m , \alpha , j ]$ is defined by the equation

$$
\begin{array} { r l } { \alpha [ 2 m , \alpha , j ] = \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { 2 m - 1 } f \left( \frac { \pi k } { m } + \alpha \right) \cos { \left( \frac { \pi j k } { m } \right) } } & { } \\ { = \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { m - 1 } f \left( \frac { 2 \pi k } { m } + \alpha \right) \cos { \left( \frac { 2 \pi j k } { m } \right) } } & { } \\ { + \displaystyle \frac { 1 } { m } \sum _ { k = 0 } ^ { m - 1 } f \left( \frac { 2 \pi k } { m } + \frac { \pi } { m } + \alpha \right) \cos { \left( \frac { 2 \pi j k } { m } + \frac { \pi j } { m } \right) } } & { } \\ { = \frac { 1 } { 2 } \alpha [ m , \alpha , j ] + \frac { 1 } { 2 } \cos { \left( \frac { \pi j } { m } \right) } \alpha [ m , \alpha + \pi / m , j ] } & { } \\ { ~ - \frac { 1 } { 2 } \sin { \left( \frac { \pi j } { m } \right) } b [ m , \alpha + \pi / m , j ] . } & { } \end{array}
$$

Similarly the identity

$$
\begin{array} { l } { { b [ 2 m , \alpha , j ] = \frac { 1 } { 2 } b [ m , \alpha , j ] + \frac { 1 } { 2 } \sin \Big ( \displaystyle \frac { \pi j } { m } \Big ) a [ m , \alpha + \pi / m , j ] } } \\ { { \phantom { b } } } \\ { { \phantom { b } + \frac { 1 } { 2 } \cos \Big ( \displaystyle \frac { \pi j } { m } \Big ) b [ m , \alpha + \pi / m , j ] } } \end{array}
$$

is satisfied, which is used to evaluate $b [ 2 m , \alpha , j ]$ . It is important to note that the definitions (13.46) and (13.47) imply the equations

$$
\begin{array} { l }  { a [ m , \alpha , j ] = a [ m , \alpha , m - j ] \atop b [ m , \alpha , j ] = - b [ m , \alpha , m - j ] \Big \} , } \end{array}
$$

and that $b [ m , \alpha , j ]$ is zero when $j = { \textstyle \frac { 1 } { 2 } } m$

The FFT method begins by setting the numbers

$$
a [ 1 , \alpha , 0 ] = 2 f ( \alpha ) ,
$$

where the values of $_ { \pmb { \alpha } }$ are the numbers in the set $\scriptstyle \{ 2 \pi k / N , k =$ $0 , 1 , \ldots , N - 1 \}$ . Then an iterative process is applied, where each itera-tion depends on the value of $^ { m }$ ,which initially has the value one.At the beginning of each iteration the numbers $\{ a [ m , \alpha , j ]$ ； $\scriptstyle 0 \leqslant j \leqslant { \frac { 1 } { 2 } } m \}$ and $\{ b [ m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } m \}$ are available,where the second set is empty until $m \geqslant 4$ , and where the range of $_ \alpha$ is the set $\left\{ 2 \pi k / N ; k = 0 , 1 , \ldots \right.$ ，

$N / m - 1 \}$ . The iteration uses equations (13.48), (13.49) and (13.50) to calculate the coefficients $\{ a [ 2 m , \alpha , j ] ; 0 \leqslant j \leqslant m \}$ and $\{ b [ 2 m , \alpha , j ] ; 0 < j <$ $m \}$ ,where the new range of $_ { \pmb { \alpha } }$ is the set $\{ 2 \pi k / N ; k = 0 , 1 , \ldots , N / 2 m - 1 \}$ Because the term $( \alpha + \pi / m )$ occurs in the formulae (13.48) and (13.49), all the data that are available at the beginning of the iteration are necessary. All terms that are not available explicitly as data are either zero or are obtained from equation (13.5O).At the end of the iteration the value of $^ { m }$ is multiplied by two and is tested. If the new value is less than $N ,$ then a new iteration is begun. Otherwise,when $m = N ,$ all the required values of the coefficients are found.Because the number of computer operations of each iteration of this process is of order $N ,$ ,the total work of the FFT method is only of order $N \log _ { 2 } N .$

The FFT method can be extended to the case when $\pmb { N }$ has the value

$$
N = r _ { 1 } r _ { 2 } \ldots r _ { t } ,
$$

where the terms $\{ r _ { s } ; s = 1 , 2 , \ldots , t \}$ are any integers that are greater than one. Then $t$ iterations of a process are applied, each iteration being similar to the one that is described in the previous paragraph. Initially the parameters (13.51) are set as before,and $^ { m }$ is equal to one. The later values of $^ { m }$ are defined by multiplying $^ { m }$ by $\boldsymbol { r } _ { s }$ at the end of each iteration, where $\pmb { s }$ is the number of the iteration. At the start of the sth iteration, the numbers $\{ a [ m , \alpha , j ] ; 0 \leqslant j \leqslant \frac { 1 } { 2 } m \}$ and $\{ b [ m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } m \}$ are known, where,as before,the range of $_ { \pmb { \alpha } }$ is the set $\scriptstyle \{ 2 \pi k / N $ ； $k = 0 , 1 , \ldots ,$ $N / m - 1 \}$ . The iteration calculates the terms $\{ a [ r _ { s } m , \alpha , j ] ; 0 \leqslant j \leqslant \frac { 1 } { 2 } r _ { s } m \}$ and $\{ b [ r _ { s } m , \alpha , j ] ; 0 < j < \frac { 1 } { 2 } r _ { s } m \}$ ，where the new range of $_ { \pmb { \alpha } }$ is the set $\left\{ 2 \pi k / N ; k = 0 , 1 , \ldots , N / ( r _ { s } m ) - 1 \right\}$ . Hence,after $t$ iterations, the required coefficients are found.

In order to calculate $a [ r m , \alpha , j ]$ and $b [ r m , \alpha , j ]$ , we replace $^ { m }$ by rm in the definitions (13.46) and (13.47).The sums over $k$ are split into $r$ parts, where in each part the value of $k$ (modulo $r$ ） is constant.Thus we find expressions for $a [ r m , \alpha , j ]$ and $b [ r m , \alpha , j ] ,$ in terms of $a [ m , \alpha + 2 \pi l / r m , j ]$ and $b [ m , \alpha + 2 \pi l / r m , j ]$ where $l$ takes the values $l = 0 , 1 , \ldots , ( r - 1 ) ,$ ， which are suitable for the change to the range of $\pmb { \alpha }$ that is made by the iteration. Because the greatest new value of $j$ is $\scriptstyle { \frac { 1 } { 2 } } r _ { s } m$ , it happens sometimes that $j$ exceeds $_ { m }$ ， It is therefore important to note that the definitions (13.46) and (13.47), not only provide the equations (13.50), but also they give the identities

$$
\begin{array} { c } { { a \left[ m , \alpha , j + m \right] = a \left[ m , \alpha , j \right] } } \\ { { b \left[ m , \alpha , j + m \right] = b \left[ m , \alpha , j \right] } } \end{array} \biggr \} .
$$

It is helpful to work through a simple example,in order to verify that all the formulae that are needed by the general FFT method have been mentioned.

# 13 Exercises

.1 Let $j$ and $\pmb { n }$ be positive integers such that $j \leqslant 2 n$ .Show that there is a non-zero function in ${ \mathcal { Q } } _ { n }$ that has zeros at any $j$ distinct points of the interval $[ 0 , 2 \pi )$ . A convenient method is to express the required function as the product of functions from $\mathcal { Q } _ { 1 }$ .Hence develop a procedure, that is analogous to Lagrange interpolation, for calculating the function $q$ in ${ \mathcal { Q } } _ { n }$ that satisfies the conditions $\{ q ( \xi _ { i } ) = f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , 2 n \}$ where the function values $\{ f ( \xi _ { i } ) ; i = 0 , 1 , \ldots , 2 n \}$ are given,and where the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , 2 n \}$ are all different and are all in $[ 0 , 2 \pi )$ · Further, prove that no non-zero element of ${ \mathcal { Q } } _ { n }$ has more than $_ { 2 n }$ zeros in $[ 0 , 2 \pi )$

13.2Let $f$ be the odd function in $\mathcal { C } _ { 2 \pi }$ that satisfies the equation

$$
f ( x ) = 1 - ( 4 / \pi ^ { 2 } ) ( x - { \textstyle \frac { 1 } { 2 } } \pi ) ^ { 2 } , \qquad 0 \leqslant x \leqslant \pi .
$$

Calculate the Fourier series approximation to $f ,$ and deduce the identity

$$
1 + ( { \textstyle { \frac { 1 } { 3 } } } ) ^ { 6 } + ( { \textstyle { \frac { 1 } { 5 } } } ) ^ { 6 } + ( { \textstyle { \frac { 1 } { 7 } } } ) ^ { 6 } + \dots = \pi ^ { 6 } / 9 6 0
$$

from Bessel's inequality.

13.3 Let $_ n$ be a fixed positive integer, let $\bar { \pmb { S } } [ n , N ]$ be the linear operator from $\mathcal { C } _ { 2 \pi }$ to ${ \mathcal { Q } } _ { n }$ that is equivalent to the discrete Fourier method of Section 13.3,and let $f$ be any function in $\mathcal { C } _ { 2 \pi }$ .Prove that the limit

$$
\operatorname* { l i m } _ { N  \infty } \| \bar { S } [ n , N ] f - S _ { n } f \| _ { \infty } = 0
$$

is obtained, where $s _ { n }$ is the Fourier series operator that is defined in Section 13.2.

13.4 Given the function values $f ( 0 ) = 0 . 2 , f ( \textstyle { \frac { 1 } { 2 } } \pi ) = 0 . 2 5 , f ( \pi ) = 1 . 0$ and $f ( 1 _ { 2 } ^ { \frac { 1 } { 2 } } \pi ) = 0 . 5$ ，use the discrete Fourier method to obtain an approximation to $f$ of the form

$$
\begin{array} { r } { q ( x ) = \frac { 1 } { 2 } a _ { 0 } + a _ { 1 } \cos x + b _ { 1 } \sin x + a _ { 2 } \cos ( 2 x ) , \qquad - \infty < x < \infty . } \end{array}
$$

Let $\bar { \pmb q }$ be the function

$$
\bar { q } ( x ) = { \textstyle \frac { 1 } { 2 } } a _ { 0 } + a _ { 1 } \cos x + b _ { 1 } \sin x + { \textstyle \frac { 1 } { 2 } } a _ { 2 } \cos ( 2 x ) , \qquad - \infty < x <
$$

Explain why $\bar { q }$ interpolates the data but $q$ does not.

13.5 Let $\bar { \pmb { S } } [ \pmb { n } , \pmb { N } ]$ be the operator that is defined in Exercise 13.3, and let $\pmb { D } _ { \pmb { \lambda } }$ be the operator from $\mathcal { C } _ { 2 \pi }$ to $\mathcal { C } _ { 2 \pi }$ such that, for any $f$ in $\mathcal { C } _ { 2 \pi } , D _ { \lambda } f$ is the function

$$
( D _ { \lambda } f ) ( x ) = f ( x + \lambda ) , \qquad - \infty < x < \infty .
$$

Prove that $\bar { \cal S } [ n , 2 N ]$ is the operator

$$
\bar { S } [ n , 2 N ] = { \textstyle \frac { 1 } { 2 } } \{ \bar { S } [ n , N ] + D _ { - \pi / N } \bar { S } [ n , N ] D _ { \pi / N } \} .
$$

Relate this equation to the FFT method.

13.6 Apply the FFT method to calculate an approximation in $\mathcal { Q } _ { 3 }$ to the data

$$
\begin{array} { l l l } { { f ( 0 ) } } & { { = - 0 . 1 1 2 1 7 8 } } & { { f ( \pi ) \quad \quad = - 0 . 3 2 1 4 1 2 } } \\ { { f ( \pi / 4 ) } } & { { = \quad 1 . 0 7 9 6 5 9 } } & { { f ( 5 \pi / 4 ) = - 0 . 5 2 8 1 1 3 } } \\ { { f ( \pi / 2 ) } } & { { = \phantom { - } 2 . 1 7 2 6 6 7 } } & { { f ( 3 \pi / 2 ) = - 0 . 5 6 2 3 2 6 } } \\ { { f ( 3 \pi / 4 ) = } } & { { 0 . 3 7 6 6 0 7 } } & { { f ( 7 \pi / 4 ) = - 0 . 4 6 6 2 6 1 , } } \end{array}
$$

using the results of the previous two exercises to check your calculation.

13.7 State and prove a characterization theorem for the best minimax approximation from ${ \mathcal { Q } } _ { n }$ to a function $f$ in $\mathcal { C } _ { 2 \pi } ,$ that is analogous to Theorem 7.2.

13.8Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that takes the values

$$
f ( x ) = \lvert x - \xi \rvert , \qquad \xi - \varepsilon \leqslant x \leqslant \xi + \varepsilon ,
$$

where $\pmb { \xi }$ is a fixed number, and where $\pmb \varepsilon$ is a positive constant that is much less than $\pmb { \pi }$ 、Prove that the limit

$$
\operatorname* { l i m } _ { n  \infty } { ( S _ { n } f ) ( \xi ) = f ( \xi ) }
$$

is obtained, and that, if $f$ satisfies the Lipschitz condition

$$
\left| f ( x _ { 1 } ) - f ( x _ { 0 } ) \right| \leqslant L \left| x _ { 1 } - x _ { 0 } \right|
$$

for all real numbers $\scriptstyle x _ { 0 }$ and $x _ { 1 }$ ,where $L$ is a constant, then the difference $\left| f ( \xi ) - ( S _ { n } f ) ( \xi ) \right|$ is of order $1 / n$

3.9 Deduce from Exercises 13.3 and 13.5 that the inequality $\| { \bar { S } } [ n , N ] \| _ { \infty } \geqslant \| S _ { n } \| _ { \infty }$ is satisfied.

13.10Prove the analogy of Theorem 6.2 for trigonometric approximation, namely that, if $\left\{ G _ { k } ; k = 1 , 2 , 3 , . . . \right\}$ is a sequence of linear monotone operators from $\mathcal { C } _ { 2 \pi }$ to $\ell _ { 2 \pi }$ ，then the sequence $\{ G _ { k } f ; k = 1 , 2 , 3 , . . . \}$ converges uniformly to $f$ for all $f$ in $\mathcal { C } _ { 2 \pi }$ if and only if it converges uniformly for the functions $\{ f ( x ) =$

# Exercises

$1 ; - \infty < x < \infty \} , \quad \{ f ( x ) = \cos x ; - \infty < x < \infty \} ,$ and $\{ f ( x ) =$ sin $x ; - \infty < x < \infty \}$ . By establishing that the Fejer operator

$$
G _ { k } = \frac { 1 } { k } \left[ S _ { 0 } + S _ { 1 } + \ldots + S _ { k - 1 } \right]
$$

is monotone, where $s _ { n }$ is still the Fourier series operator, deduce another proof of Theorem 13.1.

# 14

# The theory of best $\pmb { L _ { 1 } }$ approximation

# 14.1 Introduction to best $\pmb { L _ { 1 } }$ approximation

In Chapter 1 we noted that a best $L _ { 1 }$ approximation from a subset $\mathscr { A }$ of $\mathcal { C } [ a , b ]$ to a function $f$ in $\mathcal { C } [ a , b ]$ is an element of $\mathcal { A }$ that minimizes the expression

$$
\| f - p \| _ { 1 } = \int _ { a } ^ { b } { \bigl | } f ( x ) - p ( x ) { \bigr | } \mathrm { d } x , \qquad p \in { \mathcal { A } } .
$$

The theory that is given in this chapter is for the frequently occurring case when $\mathcal { A }$ is a linear space. Necessary and sufficient conditions for the function $p ^ { * }$ in $\mathcal { A }$ to be a best $L _ { 1 }$ approximation to $f$ are given in the next section. They have the interesting property that all the dependence on $f$ is contained in the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { - 1 , } & { f ( x ) < p ^ { * } ( x ) } \\ { 0 , } & { f ( x ) = p ^ { * } ( x ) } \\ { 1 , } & { f ( x ) > p ^ { * } ( x ) , } \end{array} \right. \quad a \leqslant x \leqslant b .
$$

It follows,therefore, that if $p ^ { * }$ is a best approximation to $f ,$ and if $f$ is changed in any way that leaves the sign function (14.2) unaltered, then $p ^ { * }$ remains a best approximation to $f .$ A similar result holds in the discrete case,where we require the function in $\mathscr { A }$ that minimizes the expression

$$
\sum _ { t = 1 } ^ { m } \big | f ( x _ { t } ) - p ( x _ { t } ) \big | , \qquad p \in \mathcal { A } ,
$$

where $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ is a set of data points in $[ a , b ]$ . This property explains the statement, made in Chapter 1, that, if there are a few gross errors in the data $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ ,then the magnitudes of these errors make no difference to the final approximation.

In order to introduce the characterization theorem,we consider first the approximation of a strictly monotonic function $f$ in ${ \mathcal { C } } [ a , b ]$ by a constant function $p$ ,where the value of the constant is to be determined. Thus $\mathscr { A }$ is a linear space of dimension one. The value of expression (14.1), when $p$ is the function $\{ p ( x ) = f ( \xi )$ ； $a \leqslant x \leqslant b \}$ , is the total area of the shaded regions of Figure 14.1. We require the value of $\pmb { \xi }$ that minimizes this area. The figure shows that, if we replace $p$ by the function $\{ p ( { \pmb x } ) =$ $f ( \xi ) + \varepsilon \mathrm { ~ ; ~ } a \leqslant x \leqslant b \}$ ,where $\pmb \varepsilon$ is small, then the change to the area of the left-hand shaded region is approximately ${ \pmb \varepsilon } \left( { \pmb \xi } - { \pmb a } \right)$ ,and the change to the area of the other shaded region is approximately $- \varepsilon ( b - \xi )$ , which gives a total change of about $2 \varepsilon \left( \xi - \textstyle { \frac { 1 } { 2 } } [ a + b ] \right)$ . Therefore, if $\begin{array} { r } { \xi < \frac { 1 } { 2 } [ a + b ] . } \end{array}$ we can reduce $\| f - p \| _ { 1 }$ by letting $\pmb \varepsilon$ be positive, and, if $\begin{array} { r } { \xi > \frac { 1 } { 2 } [ a + b ] , } \end{array}$ , there exists a negative value of $\pmb \varepsilon$ that reduces the error. It follows that the required approximation is the constant function $\{ p ( x ) = f ( { \textstyle \frac { 1 } { 2 } } [ a + b ] )$ ； $a \leqslant x \leqslant b \}$ This approximation is optimal because the measures of the sets $\{ x \colon f ( x ) <$ $p ( { \pmb x } ) \}$ and $\{ x \colon f ( x ) > p ( x ) \}$ are equal. Thus we have an example of a condition for a best approximation that depends just on the sign of the error function.

Another useful property of this example is that, if we know in advance that $f$ is monotonic, then the calculation of $f ( x )$ at the single point $x = { \textstyle { \frac { 1 } { 2 } } } ( a + b )$ provides all the data that are needed to determine the best approximation. It is shown in Section 14.3 that this property generalizes to the case when $\mathcal { A }$ satisfies the Haar condition.

# 14.2 The characterization theorem

The following theorem gives the basic necessary and sufficient condition for the function $p ^ { * }$ to be a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ It is an extension of the example of the last section. It includes a condition

![](images/1bda995631250fd4f271c669fe9b9b0b7427b156eb3323bedd9932b0fb200738.jpg)  
Figure 14.1. The value of $\| f - p \| _ { 1 }$

on the set of zeros of the function $\{ f ( x ) - p ^ { * } ( x )$ ； $a \leqslant x \leqslant b $ ,that fails only in pathological cases.

# Theorem 14.1

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ a , b ]$ . Let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,and let $p ^ { * }$ be any element of $\mathcal { A } ,$ ， such that the set

$$
{ \mathcal { L } } = \{ x : f ( x ) = p ^ { * } ( x ) , a \leqslant x \leqslant b \}
$$

is either empty or is composed of a finite number of intervals and discrete points. Then $p ^ { * }$ is a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ if and only if the inequality

$$
{ \biggl | } \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x { \biggr | } \leqslant \int _ { { \mathcal { Z } } } \left| p ( x ) \right| \mathrm { d } x
$$

is satisfied for all $p$ in $\scriptstyle { \mathcal { A } } ,$ where $s ^ { * }$ is the function (14.2).

Proof. If condition (14.5) does not hold for all functions $p$ in $\mathcal { A } .$ we let $p$ be an element of $\mathscr { A }$ such that the number

$$
\eta = \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x - \int _ { \mathcal { Z } } \left| p ( x ) \right| \mathrm { d } x
$$

is positive,and such that the normalization condition

$$
\| p \| _ { \infty } = 1
$$

holds. We prove that $p ^ { * }$ is not a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f$ by showing that, if the number $\pmb \theta$ is suficiently small and positive,then the inequality

$$
\| f - ( p ^ { * } + \theta p ) \| _ { 1 } < \| f - p ^ { * } \| _ { 1 }
$$

is obtained. The upper bound on $\pmb \theta$ depends on the set

$$
\mathcal { Z } _ { \theta } = \{ x : 0 < \left| f ( x ) - p ^ { * } ( x ) \right| \leqslant \theta , a \leqslant x \leqslant b \} .
$$

We require $\pmb \theta$ to be so small that the condition

$$
\int _ { \mathcal { X } _ { \theta } } \mathrm { d } x < \frac { 1 } { 2 } \eta
$$

is satisfied,which is possible because of the restrictions on $\mathcal { Z }$ that are given in the statement of the theorem.We let $\mathcal { X } _ { \mathbf { R } }$ be the set that contains the points of $[ a , b ]$ that are neither in $\mathcal { Z }$ nor in $\mathcal { Z } _ { \pmb { \theta } }$ .Inequality(14.8） is proved by dividing the range of integration in the definition

$$
\| f - ( p ^ { * } + \theta p ) \| _ { 1 } = \int _ { a } ^ { b } { \bigl | } f ( x ) - p ^ { * } ( x ) - \theta p ( x ) { \bigr | } \mathrm { d } x
$$

into the three parts $\mathcal { X } , \mathcal { X } _ { \theta }$ and $\mathcal { L } _ { \mathbf { R } }$ . The definition (14.4) gives the identity

$$
\begin{array} { r } { \mathopen { } \mathclose \bgroup \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \aftergroup \egroup \right| = \theta \mathopen { } \mathclose \bgroup \left| p ( x ) \aftergroup \egroup \right| , \qquad x \in \mathcal { L } , } \end{array}
$$

condition (14.7) provides the bound

$$
\begin{array} { r l } & { \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \right| \leqslant \left| f ( x ) - p ^ { * } ( x ) \right| + \theta \left| p ( x ) \right| } \\ & { \quad \leqslant \left| f ( x ) - p ^ { * } ( x ) \right| + \theta [ 2 - s ^ { * } ( x ) p ( x ) ] , \qquad x \in \mathcal { Z } _ { \theta } , } \end{array}
$$

and equations (14.7) and (14.9) imply that, when $x$ is in $\mathcal { Z } _ { \mathbf { R } }$ ,the sign of $\{ f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \}$ is the same as the sign of $\{ f ( x ) - p ^ { * } ( x ) \}$ ,which gives the relation

$$
{ \big | } f ( x ) - p ^ { * } ( x ) - \theta p ( x ) { \big | } = { \big | } f ( x ) - p ^ { * } ( x ) { \big | } - \theta s ^ { * } ( x ) p ( x ) , \qquad x \in \mathcal { X } _ { \mathbf { R } } .
$$

Therefore it follows from equations (14.2) and (14.11) that the condition

$$
\begin{array} { l } { \displaystyle \left\| f - ( p ^ { * } + \theta p ) \right\| _ { 1 } \leqslant \left\| f - p ^ { * } \right\| _ { 1 } + \theta \displaystyle \int _ { \mathcal { X } } \left| p ( x ) \right| \mathrm { d } x - \theta \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x } \\ { \displaystyle \qquad + 2 \theta \displaystyle \int _ { \mathcal { X } _ { \theta } } \mathrm { d } x } \end{array}
$$

is obtained. Inequality (14.8) is now a consequence of expressions (4.6) and (14.1O),which proves the first half of the theorem.

To prove the second part of the theorem, we let $\pmb q$ be a general element of $\mathcal { A } _ { : }$ we let $p$ be the function $( p ^ { * } - q )$ , which is also in $\mathcal { A } ,$ and we deduce from inequality (14.5） that the distance $\| f - q \| _ { 1 }$ is not less than the distance $\| f - p ^ { * } \| _ { 1 }$ . Specifically, from expressions (14.2),(14.4) and (14.5) we obtain the relation

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \left| f ( x ) - q ( x ) \right| \mathrm { d } x \geqslant \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) [ f ( x ) - q ( x ) ] \mathrm { d } x + \displaystyle \int _ { x } | f ( x ) - q ( x ) | \mathrm { d } x } \\ { \displaystyle = \int _ { a } ^ { b } s ^ { * } ( x ) [ f ( x ) - p ^ { * } ( x ) ] \mathrm { d } x + \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) [ p ^ { * } ( x ) - q ( x ) ] \mathrm { d } x } \\ { \displaystyle \quad + \displaystyle \int _ { x } | p ^ { * } ( x ) - q ( x ) | \mathrm { d } x } \\ { \displaystyle = \| f - p ^ { * } \| _ { 1 } + \displaystyle \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x + \displaystyle \int _ { x } | p ( x ) | \mathrm { d } x } \\ { \displaystyle \geqslant \| f - p ^ { * } \| _ { 1 } , } \end{array}
$$

where the first line depends on the property $\{ s ^ { * } ( x ) = 0 , x \in \mathcal { X } \}$ .Because this inequality shows that $q$ is not a better $L _ { 1 }$ approximation than $p ^ { * }$ ,the theorem is proved.□

Frequently the set $\mathcal { Z } ,$ ,defined by equation (14.4),contains only a finite number of discrete points. In this case, because the right-hand side of

expression (14.5) is zero, $p ^ { * }$ is a best $\scriptstyle { L _ { 1 } }$ approximation from $\mathcal { A }$ to $f$ if and only if the condition

$$
( s ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } ,
$$

holds,where $s ^ { * }$ is the function (14.2),and where $( s ^ { * } , p )$ is the scalar product

$$
( s ^ { * } , p ) = \int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x .
$$

Scalar products are mentioned, because it is interesting to compare a best approximation in the 1-norm with the best approximation in the 2-norm. We recall from Theorem 11.1 that the condition for $p ^ { * }$ to be the function in $\mathscr { A }$ that minimizes the expression

$$
\| f - p \| _ { 2 } = { \bigg [ } \int _ { a } ^ { b } { \left[ f ( x ) - p ( x ) \right] ^ { 2 } } \mathrm { d } x { \bigg ] } ^ { \frac { 1 } { 2 } } , \qquad p \in { \mathcal { A } } ,
$$

is the equation

$$
( f - p ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } .
$$

Therefore,to minimize the 2-norm of the error,we require the error function to be orthogonal to every element of $\mathcal { A } _ { : }$ ，but, to minimize the 1-norm of the error,it is the sign function (14.2) that has to be orthogonal to every element of $\mathscr { A }$

The reason for the similarity between these characterization theorems is that expressions (14.1) and(14.19) are both special cases of the $q$ -norm error

$$
\| f - p \| _ { q } = { \biggl [ } \int _ { a } ^ { b } { \bigl | } f ( x ) - p ( x ) { \bigr | } ^ { q } ~ \mathrm { d } x { \biggr ] } ^ { 1 / q } , \qquad p \in { \mathcal { A } } ,
$$

where $\pmb q$ is a real constant that is not less than one.In order to develop this remark, we let $p ^ { * }$ be an element of $\mathcal { A }$ that minimizes expression (14.21), we let $p$ be any element of $\mathcal { A } _ { : }$ , and we let $\phi$ be the function

$$
\phi \left( \theta \right) = \int _ { a } ^ { b } \left| f ( x ) - p ^ { * } ( x ) - \theta p ( x ) \right| ^ { q } \mathrm { d } x , \qquad - \infty < \theta < \infty .
$$

It follows that $\phi ( \theta )$ is least when $\pmb \theta$ is zero. Therefore, if $\phi$ is differentiable, the term $\phi ^ { \prime } ( 0 )$ must be zero. This derivative can be calculated when $q$ is greater than one.Hence we obtain the condition

$$
\int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) | f ( x ) - p ^ { * } ( x ) | ^ { q - 1 } \mathrm { d } x = 0 , \qquad p \in \mathcal { A } ,
$$

on $p ^ { * }$ ， where $s ^ { * }$ is the function (14.2). We note that, when $q = 2$ , this condition is the same as equation (14.20). Moreover, if we let $q$ tend to one,then the conditions (14.17) and (14.23) on $p ^ { * }$ become the same. Thus the similarity between the characterization theorems 11.1 and 14.1 is explained.

Two uses of Theorem 14.1 are as follows. The proof of the first part of the theorem provides a constructive method for obtaining an approximation from $\mathcal { A }$ to $f$ that is better than $p ^ { * }$ if condition (14.5） is not satisfied. Secondly, the theorem can be used sometimes to calculate the best approximation directly. For example, in the approximation problem that is shown in Figure 14.1, the required approximation is the function $\{ p ^ { * } ( x ) = f ( { \textstyle \frac { 1 } { 2 } } [ a + b ] )$ ； $a \leqslant x \leqslant b \}$ ，because then the sign function (14.2) satisfies the characterization condition (14.5).

# 14.3 Consequences of the Haar condition

As in the case of minimax approximation,one can say much more about the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ if the linear space $\mathcal { A }$ satisfies the Haar condition. We refer to the properties (1)-(4)of the Haar condition that are stated in the second paragraph of Section 7.3.First we prove a theorem on the number of zeros of the error function of a best $L _ { 1 }$ approximation, that is applied in two ways.It helps to show that the best approximation is unique. Moreover, it is used to generalize our earlier remark, that the best $L _ { 1 }$ approximation can be calculated sometimes by interpolation at points of the range $[ a , b ] ,$ that are independent of the function that is being approximated.

# Theorem 14.2

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition,and let $f$ be any function in $\mathcal { C } [ a , b ]$ .If $p ^ { * }$ is a best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f ,$ and if the number of zeros of the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is finite, then $e ^ { * }$ changes sign at least $( n + 1 )$ times.

Proof. Suppose that $e ^ { * }$ has a finite number of zeros,and that it changes sign fewer than $( n + 1 )$ times. Then,by property (2) of Section 7.3, there exists a function $\pmb { p }$ in $\mathcal { A } _ { : }$ ,such that the product $s ^ { * } ( x ) p ( x )$ is positive for all values of $x$ in $[ a , b ]$ ,except for the zeros of $e ^ { * }$ , where $s ^ { * }$ is the function (14.2). Hence the integral (14.18) is positive,but the right-hand side of expression (14.5) is zero,because $\mathcal { Z }$ has measure zero.Therefore $p ^ { * }$ fails to satisfy the characterization theorem 14.1. This contradiction proves the theorem.□

One application of this theorem is to show that the best $L _ { 1 }$ approximation is unique when the Haar condition is satisfied.

# Theorem 14.3

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition. Then, for any $f$ in $\mathcal { C } [ a , b ]$ ,there is just one best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$

Proof. Let $q ^ { * }$ and $r ^ { * }$ be best $L _ { 1 }$ approximations from $\mathcal { A }$ to $f ,$ and let $p ^ { * }$ be the function $\scriptstyle { \frac { 1 } { 2 } } ( q ^ { * } + r ^ { * } )$ . We consider the inequality

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } \left| f ( x ) - p ^ { * } ( x ) \right| \mathrm { d } x = \int _ { a } ^ { b } \left| \frac { 1 } { 2 } [ f ( x ) - q ^ { * } ( x ) ] + \frac { 1 } { 2 } [ f ( x ) - r ^ { * } ( x ) ] \right| \mathrm { d } x } \\ { \displaystyle \qquad \leqslant \frac { 1 } { 2 } \int _ { a } ^ { b } \left| f ( x ) - q ^ { * } ( x ) \right| \mathrm { d } x + \frac { 1 } { 2 } \int _ { a } ^ { b } \left| f ( x ) - r ^ { * } ( x ) \right| \mathrm { d } x , \qquad ( 1 4 ) \mathrm { d } x , } \end{array}
$$

which depends on the definition of the modulus of a number.Because the right-hand side is the least distance from $\mathcal { A }$ to $f ,$ and because $p ^ { * }$ is in $\mathcal { A } ,$ this inequality is satisfied as an equation. Therefore, because allfunctions are in ${ \mathcal { C } } [ a , b ]$ , the identity

$$
{ \big | } f ( x ) - p ^ { * } ( x ) { \big | } = { \textstyle { \frac { 1 } { 2 } } } { \big | } f ( x ) - q ^ { * } ( x ) { \big | } + { \textstyle { \frac { 1 } { 2 } } } { \big | } f ( x ) - r ^ { * } ( x ) { \big | }
$$

holds for all $x$ in $[ a , b ]$ .In particular,when $f ( x )$ is equal to $p ^ { * } ( x )$ ,then both $q ^ { * } ( x )$ and $r ^ { * } ( x )$ must be equal to $f ( x )$ . It follows from Theorem 14.2 that the function $\{ q ^ { * } ( x ) - r ^ { * } ( x )$ ； $a \leqslant x \leqslant b \}$ has at least $( n + 1 )$ zeros. Therefore the Haar condition implies that the functions $q ^ { * }$ and $r ^ { * }$ are the same.□

Most algorithms for calculating best $L _ { 1 }$ approximations aim to find the zeros of the error function. Often the number of zeros is exactly $( n + 1 )$ ， where $( n + 1 )$ is the dimension of $\mathcal { A } .$ .For example, this case occurs if $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ if $f$ is in $\mathcal { C } ^ { ( n + 1 ) } [ a , b ] .$ and if the derivative $f ^ { ( n + 1 ) } ( x )$ is positive for all $x$ in $[ a , b ]$ . Therefore the following theorem is useful.

# Theorem 14.4

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition,and let $f$ be a function in $\mathcal { C } [ a , b ]$ such that the error function (14.24) has exactly $( n + 1 )$ zeros, where $p ^ { * }$ is the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ . Then the positions of the zeros do not depend on $f .$

Proof. Let $s ^ { * }$ be the function (14.2),and let the zeros of the error function $\{ f ( x ) - p ^ { * } ( x ) ; a \leqslant x \leqslant b \}$ be at the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ .Let $\pmb { g }$ be a function in $\mathcal { C } [ a , b ]$ such that the error function

$$
d ^ { * } ( x ) = g ( x ) - q ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

also has exactly $( n + 1 )$ zeros, where $q ^ { * }$ is the best $L _ { 1 }$ approximation from $\mathcal { A }$ to ${ \pmb g }$ . Let these zeros be at the points $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ ,and let $t ^ { * }$ be the function

$$
t ^ { * } ( x ) = \left\{ \begin{array} { c c } { - 1 , } & { g ( x ) < q ^ { * } ( x ) } \\ { 0 , } & { g ( x ) = q ^ { * } ( x ) } \\ { 1 , } & { g ( x ) > q ^ { * } ( x ) , } \end{array} \right. \quad a \leqslant x \leqslant b .
$$

We have to show that the sets $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ and $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ are the same. The method of proof depends on the Haar condition, and on the fact that Theorem 14.1 gives the equations

$$
\int _ { a } ^ { b } s ^ { * } ( x ) p ( x ) \mathrm { d } x = \int _ { a } ^ { b } t ^ { * } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { A } .
$$

We also require two consequences of Theorem 14.2, namely that the error functions (14.24) and (14.27) both change sign at their zeros,and that $e ^ { * } ( a )$ and $d ^ { * } ( a )$ are both non-zero.

We assume without loss of generality that $\xi _ { 0 } \leqslant \eta _ { 0 }$ ,and that the signs of $e ^ { * } ( a )$ and $d ^ { * } ( a )$ are the same. Because of property (2) of Section 7.3, we may let $\pmb { p }$ be a function in $\mathcal { A }$ that changes sign at the points $\{ \xi _ { i } ; i =$ $1 , 2 , \ldots , n \}$ ,and that has no other zeros.We choose the overall sign of $p$ so that the signs of $p ( a )$ and $e ^ { * } ( a )$ are opposite. We consider the equation

$$
\int _ { a } ^ { b } [ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x ) \mathrm { d } x = 0 ,
$$

which follows from condition (14.29). The sign of the integrand is important. Our assumptions imply that $[ s ^ { * } ( x ) - t ^ { * } ( x ) ]$ is zero when $\pmb { x }$ is in the interval $[ a , \xi _ { 0 } )$ . Further, in the range $( \xi _ { 0 } , b ]$ ,the product $s ^ { * } ( x ) p ( x )$ is positive,except on a set of measure zero,namely the poit set $\{ \xi _ { i }$ ； $i = 1 , 2 , \ldots , n \}$ .Moreover,the definitions (14.2) and (14.28) show that,if $s ^ { * } ( x ) p ( x )$ is positive, then the product $[ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x )$ is non-negative. By combining all these remarks, we deduce that the inequality

$$
[ s ^ { * } ( x ) - t ^ { * } ( x ) ] p ( x ) \geqslant 0 , \qquad a \leqslant x \leqslant b ,
$$

is satisfied. It follows from equation (14.30) that the function $\{ \pmb { s } ^ { * } ( \pmb { x } ) -$ $t ^ { * } ( x )$ ； $a \leqslant x \leqslant b $ is zero almost everywhere. Therefore the sets $\{ \xi _ { i }$ ； $i = 0 , 1 , \ldots , n \}$ and $\{ \eta _ { i } ; i = 0 , 1 , \ldots , n \}$ are the same.□

This theorem provides the main method for calculating best $\mathbf { { { L } } _ { 1 } }$ approximations to continuous functions. One begins by assuming that the error function will change sign only $( n + 1 )$ times. In this case, because the zeros of the error function are independent of $f ,$ they may be found by detailed consideration of $\mathcal { A } .$ An approximation from $\mathscr { A }$ to $f$ is calculated by interpolation at these zeros,and then a check is made to find out if its error function satisfies the assumption. If the assumption holds, then the required approximation has been found.Otherwise a more elaborate approximation algorithm is necessary, for example a linear programming method of the type that is described in Section 15.4. The interpolation points for the case when $\mathcal { A }$ is the space ${ \mathcal P _ { n } }$ are given in the next section. Some applications of this method are given in Chapters 15 and 24.

# 14.4 The $\pmb { L _ { 1 } }$ interpolation points for algebraic polynomials

In order to apply the algorithm for calculating best $L _ { 1 }$ approximations, that is described in the previous paragraph, it is necessary to identify the interpolation points that are the subject of Theorem 14.4. The interpolation points for the important special case when $\mathcal { A }$ is the space $\mathcal { P } _ { n }$ are given in the next theorem.

# Theorem 14.5

Let the conditions of Theorem 14.4 be satisfied, where $\mathscr { A }$ is the space $\mathcal { P } _ { n } ,$ ,and where $[ a , b ]$ is the interval [-1,1]. Then the zeros of the error function

$$
e ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad - 1 \leqslant x \leqslant 1 ,
$$

have the values

$$
\xi _ { i } = \cos \bigg [ \frac { ( n + 1 - i ) \pi } { n + 2 } \bigg ] , \qquad i = 0 , 1 , \ldots , n .
$$

Proof. Theorem 14.2 implies that the error function (14.32) changes sign at its zeros. Therefore, because of the characterization theorem 14.1, it is sufficient to prove that the equation

$$
\int _ { - 1 } ^ { 1 } s ^ { * } ( x ) p ( x ) \mathrm { d } x = 0
$$

holds for all polynomials $p$ in $\mathcal { P } _ { n }$ where $s ^ { * }$ is the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { 1 , } & { - 1 < x < \xi _ { 0 } } \\ { ( - 1 ) ^ { i } , } & { \xi _ { i - 1 } < x < \xi _ { i } , \quad \quad i = 1 , 2 , \ldots , n , } \\ { ( - 1 ) ^ { n + 1 } , } & { \xi _ { n } < x < 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

The numbers $s ^ { * } ( - 1 )$ and $s ^ { * } ( 1 )$ are defined to be zero,in order that the function

$$
\sigma ( \theta ) = s ^ { * } ( \cos \theta ) , \qquad 0 \leqslant \theta \leqslant \pi ,
$$

satisfes some periodicity conditions. We extend $\sigma$ to the infinite range by defining $\left\{ \sigma ( - \theta ) = - \sigma ( \theta ) ; 0 \leqslant \theta \leqslant \pi \right\}$ ,and by letting $\pmb { \sigma }$ be a $2 \pi$ -periodic function. It follows from equations (14.33) and (14.35) that the graph of $\{ \sigma ( \theta ) ; \ - \infty < \theta < \infty \}$ is a square wave that changes sign when $\pmb \theta$ is any integral multiple of $\pi / ( n + 2 )$ .Hence the condition

$$
\sigma \bigg ( \theta + \frac { \pi } { n + 2 } \bigg ) = - \sigma ( \theta ) , \qquad - \infty < \theta < \infty ,
$$

is obtained.

It will be shown that, if the change of variables $\left\{ x = \cos \theta ; 0 \leqslant \theta \leqslant \pi \right\}$ is made in the integral (14.34), then condition (14.37) enables equation (14.34) to be proved when $p$ is any one of the Chebyshev polynomials

$$
T _ { j } ( x ) = \cos { ( j \cos ^ { - 1 } x ) } , \qquad - 1 \leqslant x \leqslant 1 , \qquad j = 0 , 1 , \ldots , n .
$$

Because these polynomials are a basis of $\mathcal { P } _ { n }$ , we complete the proof of the theorem by establishing the equations

$$
\int _ { - 1 } ^ { 1 } s ^ { * } ( x ) T _ { j } ( x ) \mathrm { d } x = 0 , \qquad j = 0 , 1 , \dots , n .
$$

The identity

$$
\begin{array} { l } { \displaystyle \int _ { - 1 } ^ { 1 } s ^ { * } ( x ) T _ { i } ( x ) \mathrm { d } x = \int _ { 0 } ^ { \pi } s ^ { * } ( \cos \theta ) \cos \left( j \theta \right) \sin \theta \mathrm { d } \theta } \\ { = \frac { 1 } { 2 } \displaystyle \int _ { 0 } ^ { \pi } \sigma ( \theta ) \{ \sin \left[ ( j + 1 ) \theta \right] - \sin \left[ ( j - 1 ) \theta \right] \} \mathrm { d } \theta } \\ { = \frac { 1 } { 4 } \displaystyle \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \{ \sin \left[ ( j + 1 ) \theta \right] - \sin \left[ ( j - 1 ) \theta \right] \} \mathrm { d } \theta } \end{array}
$$

is satisfied, where the last line depends on the fact that $\pmb { \sigma }$ is an odd function. Therefore it is sufficient to show that the integrals

$$
I _ { k } = \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \sin \left( k \theta \right) \mathrm { d } \theta , \qquad k = 0 , 1 , \ldots , n + 1 ,
$$

are zero.We use the periodicity of the integrand of $I _ { k }$ ，then condition (14.37),and then the fact that $\pmb { \sigma }$ is odd, to deduce the equation

$$
\begin{array} { l } { { I _ { k } = \displaystyle { \int _ { - \pi } ^ { \pi } \sigma \Big ( \theta + \frac { \pi } { n + 2 } \Big ) \sin \left[ k \Big ( \theta + \frac { \pi } { n + 2 } \Big ) \right] \mathrm { d } \theta } } } \\ { { \displaystyle { \quad = - \cos \left( \frac { k \pi } { n + 2 } \right) \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \sin \left( k \theta \right) \mathrm { d } \theta } } } \\ { { \displaystyle { \qquad - \sin \left( \frac { k \pi } { n + 2 } \right) \int _ { - \pi } ^ { \pi } \sigma ( \theta ) \cos \left( k \theta \right) \mathrm { d } \theta } } } \\ { { \displaystyle { \quad = - \cos \left( \frac { k \pi } { n + 2 } \right) I _ { k } , \qquad k = 0 , 1 , \dots , n + 1 . } } } \end{array}
$$

Because the factor $- \cos { [ k \pi / ( n + 2 ) ] }$ is not equal to one, it follows that $I _ { k }$ is zero,which gives the required result.□

We note that the points (14.33) are the abscissae of the extrema of the Chebyshev polynomial $T _ { n + 2 }$ . We note also that the extension of Theorem 14.5,to the case when the range of the variable is $[ a , b ] ,$ is that the zeros of the error function occur at the points

$$
\xi _ { i } = \textstyle { \frac { 1 } { 2 } } ( a + b ) + \textstyle { \frac { 1 } { 2 } } ( b - a ) \cos { \left[ \frac { ( n + 1 - i ) \pi } { n + 2 } \right] } , \qquad i = 0 , 1 , \ldots , n .
$$

Therefore the polynomial in $\mathcal { P } _ { n }$ that minimizes the $L _ { 1 }$ error

$$
\int _ { a } ^ { b } \left| f ( x ) - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { P } _ { n } ,
$$

may be calculated by satisfying the conditions $\{ p ( \xi _ { i } ) = f ( \xi _ { i } ) ; \ i = 0 , 1 ,$ $\cdots , n \}$ ， provided that the error function of the resultant approximation changes sign just at the interpolation points.

# 14 Exercises

14.1 Find the best $L _ { 1 }$ approximation to the function $\{ f ( x ) = x ^ { 3 }$ ； $1 \leqslant$ $x \leqslant 2 \}$ by a multiple of the quadratic polynomial $\{ p ( x ) = x ^ { 2 }$ ； $1 \leqslant x \leqslant 2 \}$ in the following two different ways. Firstly calculate the integral

$$
\eta ( a ) = \int _ { 1 } ^ { 2 } \left| x ^ { 3 } - a x ^ { 2 } \right| \mathrm { d } x
$$

analytically,and obtain the required value of $^ { a }$ from the equation $\eta ^ { \prime } ( a ) = 0$ . Secondly calculate the number $^ { b }$ such that the integral of the function $\{ x ^ { 2 } \sin { ( b - x ) } ; 1 \leqslant x \leqslant 2 \}$ is zero. You should find that $b = a$

14.2 Let $\mathcal { A }$ be the three-dimensional linear space of functions in $\mathcal { C } [ - 1 , 1 ]$ that are composed of two straight line segments that join at $x = 0$ .In other words $\mathcal { A }$ is the space of splines of degree one that have only one interior knot,at the point $x = 0$ . Calculate the element of $\mathcal { A }$ that minimizes the integral

$$
\int _ { - 1 } ^ { 1 } \left| x ^ { 2 } - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { A } .
$$

14.3 Let $\mathscr { A }$ be the one-dimensional linear space that contains al multiples of the function $\{ p ( x ) = x - c ; - 1 \leqslant x \leqslant 1 \}$ where $^ { c }$ is a constant. Prove that,if $^ { c }$ is non-zero, then each function in $\mathcal { C } [ - 1 , 1 ]$ has only one best $L _ { 1 }$ approximation in $\mathcal { A }$

14.4 Let $\mathscr { A }$ be the two-dimensional linear subspace of $\mathcal { C } [ 0 , 1 ]$ that is spanned by the functions $\{ \phi _ { 0 } ( x ) = 1$ ； $0 \leqslant x \leqslant 1 \}$ and $\smash { \{ \phi _ { 1 } ( x ) = x ^ { 2 } \} }$ ； $0 \leqslant x \leqslant 1 \}$ . Calculate the points $\xi _ { 0 }$ and $\xi _ { 1 }$ such that, if $p ^ { * } \in \mathcal A ,$ if $f \in { \mathcal { C } } [ 0 , 1 ] .$ ,and if the error function $e ^ { * } { = } f { - } p ^ { * }$ changes sign just at the points $\xi _ { 0 }$ and $\xi _ { 1 }$ , then $p ^ { * }$ is the best $L _ { 1 }$ approximation to $f$ from $\mathcal { A }$ 、Hence show that the least value of the integral

$$
\int _ { 0 } ^ { 1 } \left| x - p ( x ) \right| \mathrm { d } x , \qquad p \in \mathcal { A } ,
$$

is equal to $\scriptstyle { \frac { 1 } { 4 } } ( { \sqrt { 5 } } - 2 )$

14.5 Let $\mathscr { A }$ be the set of monic polynomials in $\mathcal { P } _ { n + 1 }$ ， which means that the coefficient of $x ^ { n + 1 }$ is one,and let the range of the variable be[-1,1].Deduce from Theorem 14.5 that the norm $\{ \| p \| _ { 1 } ; p \in \mathcal { A } \}$ is least when $p$ is the function $\{ p ( x ) = T _ { n + 2 } ^ { \prime } ( x ) / [ 2 ^ { n + 1 } ( n + 2 ) ]$ $- 1 \leqslant x \leqslant 1 \}$ . Hence obtain the bound

$$
\| p \| _ { 1 } \geqslant 2 ^ { - n } , \qquad p \in { \mathcal { A } } ,
$$

and verify that it is correct by applying Theorem 14.5 directly in the case when $n = 1$

14.6 Let $f$ be a function in $\mathcal { C } [ - 1 , 1 ]$ that is identically zero on the intervals $[ - 1 , - c ]$ and $[ c , 1 ] ,$ , but that is positive on the interval $( - c , c )$ ，where $\pmb { c }$ is a positive constant. Prove that the zero function is a best $L _ { 1 }$ approximation from $\mathcal { P } _ { 2 }$ to $f$ if and only if $c \leqslant { \frac { 1 } { 4 } } ( { \sqrt { 5 - 1 } } )$

14.7 Let $p ^ { * }$ be the linear function $\{ p ^ { * } ( x ) = x ; - 1 \leqslant x \leqslant 1 \}$ ,and let $f$ be a function in $\mathcal { C } [ - 1 , 1 ]$ ，such that the error $\{ e ^ { * } ( x ) = f ( x ) -$ $p ^ { * } ( x )$ ； $- 1 \leqslant x \leqslant 1 \}$ changes sign just at the points $x = 0$ and $\pm 1 / \sqrt { 2 }$ . It follows from Theorem 14.5 that $p ^ { * }$ is the best $L _ { 1 }$ approximation to $f$ from $\mathcal { P } _ { 2 }$ .By choosing a suitable $f ,$ show that $p ^ { * }$ need not be a best $L _ { 1 }$ approximation to $f$ from the space of rational functions that is called $\boldsymbol { \bar { \mathcal { A } } } _ { 1 1 }$ in Exercise 10.1.

14.8 Let $\mathscr { A }$ be a finite-dimensional linear subspace of $\mathcal { C } ^ { ( 1 ) } [ a , b ]$ that satisfies the Haar condition， let $f$ be any fixed function in $\mathcal { C } ^ { ( 1 ) } [ a , b ] ,$ and let $p ^ { * }$ be the best $L _ { 1 }$ approximation from $\mathcal { A }$ to $f .$ Prove that there exist positive constants $^ c$ and $^ d$ such that the inequality

$$
\| f - p \| _ { 1 } \geqslant \| f - p ^ { * } \| _ { 1 } + \operatorname* { m i n } { [ c \| p - p ^ { * } \| _ { 1 } ^ { 2 } , d \| p - p ^ { * } \| _ { 1 } ] }
$$

is satisfied for all $p \in { \mathcal { A } } .$ Show, however, that this condition need not be obtained if the function $f$ is continuous but not differentiable.

14.9 Let $q ^ { * }$ be the best $L _ { 1 }$ approximation from the space $\mathcal { Q } _ { n }$ of trigonometric polynomials to a function $f$ in $\mathcal { C } _ { 2 \pi }$ 、Show that the error function $( f - q ^ { * } )$ has at least $( 2 n + 2 )$ zeros in the interval $[ 0 , 2 \pi )$ . Further, show that, if the number of zeros in this interval is equal to $( 2 n + 2 )$ , then the spacing between adjacent zeros is constant.

14.10 Let the linear subspace $\mathscr { A }$ of $\mathcal { C } [ a , b ]$ be composed of splines of degree one whose knots are fixed. Prove that each function in $\mathcal { C } [ a , b ]$ has only one best $L _ { 1 }$ approximation in $\mathcal { A } .$

# An application of $\pmb { L _ { 1 } }$ approximation and the discrete case

# 15.1 A useful example of $\pmb { L _ { 1 } }$ approximation

A particular $L _ { 1 }$ approximation problem is solved in this section, in order to demonstrate the method of calculation when the number of sign changes of the error function is equal to the dimension of $\scriptstyle { \mathcal { A } } ,$ and in order to provide a result that is required in Section 15.2. The problem is to calculate the value of the expression

$$
\operatorname* { m i n } _ { b _ { 1 } , b _ { 2 } , \ldots , b _ { n } } \int _ { 0 } ^ { \pi } \left| x - \sum _ { k = 1 } ^ { n } b _ { k } \sin { ( k x ) } \right| \mathrm { d } x ,
$$

where the quantities $\left\{ b _ { k } ; k = 1 , 2 , \ldots , n \right\}$ are real parameters. We see that it is equivalent to finding the best $L _ { 1 }$ approximation to the function $\left\{ f ( x ) = x ; 0 \leqslant x \leqslant \pi \right\}$ from the $\pmb { n }$ -dimensional linear space $\mathcal { A } ,$ ，that is spanned by the functions $\left\{ \phi _ { k } ( x ) = \sin { ( k x ) } ; 0 \leqslant x \leqslant \pi ; k = 1 , 2 , \ldots , n \right\}$

We take the optimistic view that this problem can be solved by the procedure that is described at the end of Section 14.3.Therefore we seek points $\left\{ \xi _ { i } ; i = 1 , 2 , \ldots , n \right\}$ ,satisfying the conditions

$$
0 < \xi _ { 1 } < \xi _ { 2 } < . ~ . ~ . < \xi _ { n } < \pi ,
$$

such that the equation

$$
\int _ { 0 } ^ { \pi } s ^ { * } ( x ) p ( x ) \mathrm { d } x = 0 , \qquad p \in \mathcal { A } ,
$$

holds, where $\pmb { s } ^ { * }$ is the sign function

$$
s ^ { * } ( x ) = \left\{ \begin{array} { l l } { 1 , } & { 0 < x < \xi _ { 1 } } \\ { ( - 1 ) ^ { i } , } & { \xi _ { i } < x < \xi _ { i + 1 } , } \\ { ( - 1 ) ^ { n } , } & { \xi _ { n } < x < \pi . } \end{array} \right. \quad i = 1 , 2 , \ldots , n - 1
$$

Because the integrals (14.41) are zero,it is suitable to replace $\pmb { n }$ by $( n - 1 )$

in the definition of $\pmb { \sigma } _ { : }$ ， given in the proof of Theorem 14.5,and to let $\{ s ^ { * } ( x ) ; 0 \leqslant x \leqslant \pi \}$ be the function $\{ \sigma ( \theta ) ; 0 \leqslant \theta \leqslant \pi \}$ .Thus the values

$$
\xi _ { i } = i \pi / ( n + 1 ) , \qquad i = 1 , 2 , \ldots , n ,
$$

cause equation (15.3) to be satisfied.It follows that, if $p ^ { * }$ is an element of $\mathcal { A }$ that is defined by the interpolation conditions

$$
p ^ { * } ( \xi _ { i } ) = f ( \xi _ { i } ) = \xi _ { i } , \qquad i = 1 , 2 , \ldots , n ,
$$

and if the error function

$$
e ^ { * } ( x ) = x - p ^ { * } ( x ) , \qquad 0 \leqslant x \leqslant \pi ,
$$

has no other zeros in the open interval $( 0 , \pi )$ , where a double zero at any $\xi _ { i }$ would count as an extra zero,then $p ^ { * }$ is the approximation that provides the least value of expression (15.1).

In order to prove that the equations (15.6) have a solution, we recall, from the proof of Theorem 5.4, that it is sufficient to show that the zero function is the only element of $\mathscr { A }$ that vanishes at the interpolation points. If this condition is not satisfied, then an odd trigonometric polynomial of degree $\pmb { n }$ has $_ n$ zeros in the interval $( 0 , \pi )$ ,and therefore it has $( 2 n + 1 )$ zeros in $( - \pi , \pi )$ ，which is a contradiction. Hence the equation (15.6) defines $p ^ { * }$ uniquely. We now consider the number of zeros of the function (15.7).

We see that the first derivative of $e ^ { * }$ is an even trigonometric polynomial of degree at most $\pmb { n }$ .Therefore it is zero at not more than $\pmb { n }$ points of the open interval $( 0 , \pi )$ . Hence the error function itself has at most $( n + 1 )$ zeros in the closed interval $[ 0 , \pi ]$ .We know already, however, that $e ^ { * }$ is zero at the interpolation points and at $\scriptstyle x = 0$ . Therefore there are no extra zeros.It follows that the coefficients of the function $p ^ { * }$ in $\mathcal { A } ,$ , that is defined by the interpolation conditions (15.6),are the values of the parameters $\{ b _ { i } ; i = 1 , 2 , \ldots , n \}$ ,that minimize expression (15.1).

Next we make the very useful observation that there is no need to calculate the coefficients of $p ^ { * }$ .The reason is that equation(15.3),and the definitions of $\{ s ^ { * } ( x ) ; 0 \leqslant x \leqslant \pi \}$ and the interpolation points,give the identity

$$
\begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { \pi } \left| x - p ^ { * } ( x ) \right| \mathrm { d } x = \left| \displaystyle \int _ { 0 } ^ { \pi } s ^ { * } ( x ) \big [ x - p ^ { * } ( x ) \big ] \mathrm { d } x \right| } \\ & { \quad \quad \quad = \displaystyle \left| \displaystyle \int _ { 0 } ^ { \pi } s ^ { * } ( x ) x \mathrm { d } x \right| . } \end{array}
$$

Therefore expression (15.1) has the value

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { \pi } \left. x - p ^ { * } ( x ) \right. \mathrm { d } x = \left. \sum _ { j = 0 } ^ { n } \left( - 1 \right) ^ { j } \int _ { j \pi / ( n + 1 ) } ^ { ( j + 1 ) \pi / ( n + 1 ) } x \mathrm { d } x \right. } \\ { \displaystyle \qquad = \pi ^ { 2 } / 2 ( n + 1 ) , } \end{array}
$$

which is the required result. This example shows that the interpolation procedure for calculating best $L _ { 1 }$ approximations can be used sometimes when $\mathcal { A }$ does not satisfy the Haar condition.

# 15.2 Jackson's first theorem

Equation (15.9) is important to the following question. Let $f$ be any function in $\mathcal { C } _ { 2 \pi }$ that is continuously differentiable; find the smallest number $c ( n )$ that satisfies the condition

$$
\operatorname* { m i n } _ { q \in \mathcal { Q } _ { n } } \| f - q \| _ { \infty } \leqslant c \left( n \right) \| f ^ { \prime } \| _ { \infty } ,
$$

and that is independent of $f ,$ where ${ \mathcal { Q } } _ { n }$ is the space of trigonometric polynomials of degree at most $\pmb { n }$ . In this section it is proved that $c ( n )$ has the value $\pmb { \pi } / 2 ( \pmb { n } + 1 )$ , which is ‘Jackson's first theorem'.We note that, if it is necessary to approximate $f$ by a trigonometric polynomial to given accuracy,and if the norm $\| f ^ { \prime } \| _ { \infty }$ is known, then the theorem gives an upper bound on the least value of $n$ that may be used. Usually, however, this upper bound is so high that it is of no practical value.Two reasons for studying Jackson's first theorem are that it shows a way of relating errors in function approximation to derivatives,and it is the basis of the work of the next chapter.

In order to relate $f$ to $f ^ { \prime }$ , when $f$ is in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) } ,$ we make use of the formula

$$
f ( x ) = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( \theta ) \operatorname { d } \theta + { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \theta f ^ { \prime } ( \theta + x + \pi ) \operatorname { d } \theta ,
$$

which may be verified by integration by parts. We require also the fact that, if $\pmb { g }$ is any function in $\mathcal { C } _ { 2 \pi } ,$ and if $q$ is any element of ${ \mathcal { Q } } _ { n }$ ,then the function

$$
\psi ( x ) = \int _ { - \pi } ^ { \pi } q ( \theta ) g ( \theta + x ) \mathrm { d } \theta , \qquad - \infty < x < \infty ,
$$

is also in ${ \mathcal { Q } } _ { n }$ . This statement holds because periodicity gives the equation

$$
\psi ( x ) = \int _ { - \pi } ^ { \pi } q ( \theta - x ) g ( \theta ) { \bf d } \theta ,
$$

and because $q ( \pmb \theta - \pmb x )$ may be expressed in the form

$$
q ( \theta - x ) = \frac { 1 } { 2 } a _ { 0 } ( \theta ) + \sum _ { j = 1 } ^ { n } a _ { j } ( \theta ) \cos { ( j x ) } + b _ { j } ( \theta ) \sin { ( j x ) } .
$$

In the proof of Jackson's theorem, which is given below, we let $\pmb { g }$ be the function

$$
g ( x ) = f ^ { \prime } ( x + \pi ) , \qquad - \infty < x < \infty .
$$

# Theorem 15.1 (Jackson I)

For allfunctions $f$ in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ and for all non-negative integers $\pmb { n }$ ,the inequality

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { n } } \| f - q \| _ { \infty } \leqslant { \frac { \pi } { 2 ( n + 1 ) } } \| f ^ { \prime } \| _ { \infty }
$$

is satisfied, where ${ \mathcal { Q } } _ { n }$ is the linear space of trigonometric polynomials of degree at most $\pmb { n }$

Proof. We express $f$ in the form (15.11). Because the first integral in this expression is independent of $\pmb { x } .$ ，and because the space ${ \mathcal { Q } } _ { n }$ includes constant functions, we just have to consider trigonometric approximations to the function

$$
{ \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } \theta f ^ { \prime } ( \theta + x + \pi ) \mathrm { d } \theta , \qquad - \infty < x < \infty .
$$

Therefore,by using the remark that expression (15.12) is a trigonometric polynomial, we obtain the bound

$$
\begin{array} { r l } & { \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \left\| f - q \right\| _ { \infty } \leqslant \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \underset { x } { \operatorname* { m a x } } \left| \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left[ \theta - q \left( \theta \right) \right] f ^ { \prime } \left( \theta + x + \pi \right) \mathrm { d } \theta \right| } \\ & { \quad \quad \quad \leqslant \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \left| \theta - q \left( \theta \right) \right| \mathrm { d } \theta \left\| f ^ { \prime } \right\| _ { \infty } , \quad \quad \quad \left( 1 \right) } \end{array}
$$

where the last line is elementary. Because the work of Section 15.1 gives the equation

$$
\operatorname* { m i n } _ { q \in \mathcal { Q } _ { n } } \int _ { - \pi } ^ { \pi } \left. \theta - q ( \theta ) \right. { \bf d } \theta = \frac { \pi ^ { 2 } } { \left( n + 1 \right) } ,
$$

it follows that Theorem 15.1 is true.

The factor $\pmb { \pi } / 2 ( \pmb { n } + 1 )$ that occurs in inequality (15.16) cannot be decreased. In order to prove this statement, we consider a function $f$ in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ that takes the values

$$
f ( j \pi / [ n + 1 ] ) = ( - 1 ) ^ { j } , \qquad j = 0 , \pm 1 , \pm 2 , \ldots .
$$

For any $\pmb \varepsilon > 0$ , it is possible to choose $f$ so that it also satisfies the condition

$$
\| f ^ { \prime } \| _ { \infty } { \leqslant } 2 ( n + 1 ) ( 1 + \varepsilon ) / \pi .
$$

We let $q ^ { * }$ be a best approximation from ${ \mathcal { Q } } _ { n }$ to $f .$ If the distance $\| f - q ^ { * } \| _ { \infty }$ is less than one,then equation (15.20) implies that the sign of $q ^ { * } ( j \pi / [ n + 1 ] )$ is the same as the sign of $( - 1 ) ^ { j }$ .Hence $q ^ { * }$ has a zero in each of the intervals $\{ [ ( j - 1 ) \pi / ( n + 1 ) , j \pi / ( n + 1 ) ] ; j = 1 , 2 , \ldots , 2 n + 2 \} ,$ .which is not possible because $q ^ { * }$ is in ${ \mathcal { Q } } _ { n }$ . It follows that the inequality

$$
\begin{array} { r l } { \underset { q \in \mathcal { Q } _ { n } } { \operatorname* { m i n } } \| f - q \| _ { \infty } \geqslant 1 } & { } \\ { \geqslant \frac { \pi } { 2 ( n + 1 ) ( 1 + \varepsilon ) } \| f ^ { \prime } \| _ { \infty } } & { } \end{array}
$$

is satisfied. Therefore, because $\pmb \varepsilon$ can be arbitrarily small, Jackson's first theorem gives the least value of $c ( n )$ , that is independent of $f ,$ and that is such that inequality (15.1O） holds for all continuously differentiable functions in $\mathcal { C } _ { 2 \pi }$

# 15.3 Discrete $\pmb { L _ { 1 } }$ approximation

In data-fitting calculations,where the element of $\mathscr { A }$ that minimizes expression (14.3) is required, there is a characterization theorem that is similar to Theorem 14.1. It is stated in a form that allows different weights to be given to the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$

# Theorem 15.2

Let the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ ,and fixed positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ be given. Let $\mathscr { A }$ be a linear space of functions that are defined on the point set $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ Let $p ^ { * }$ be any element of $\scriptstyle { \mathcal { A } } ,$ let $\mathcal { Z }$ contain the points of $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ that satisfy the condition

$$
p ^ { * } ( x _ { t } ) = f ( x _ { t } ) ,
$$

and let $s ^ { * }$ be the sign function

$$
\begin{array} { r } { s ^ { * } ( x _ { t } ) = \left\{ \begin{array} { l l } { 1 , } & { f ( x _ { t } ) > p ^ { * } ( x _ { t } ) } \\ { 0 , } & { f ( x _ { t } ) = p ^ { * } ( x _ { t } ) } \\ { - 1 , } & { f ( x _ { t } ) < p ^ { * } ( x _ { t } ) , } \end{array} \right. \quad t = 1 , 2 , \ldots , m . } \end{array}
$$

Then $p ^ { * }$ is a function in $\mathcal { A }$ that minimizes the expression

$$
\sum _ { t = 1 } ^ { m }  w _ { t } | f ( x _ { t } ) - p ( x _ { t } ) | , \quad \quad p \in \mathcal { A } ,
$$

if and only if the inequality

$$
\biggl | \sum _ { t = 1 } ^ { m } w _ { t } s ^ { * } ( x _ { t } ) p ( x _ { t } ) \biggr | \leqslant \sum _ { x _ { t } \in \mathcal { Z } } w _ { t } \bigl | p ( x _ { t } ) \bigr |
$$

holds for all $p$ in $\mathscr { A }$

Proof. The method of proof is similar to the proof of Theorem 14.1. If condition (15.26) is not satisfied,we consider replacing the approximation $p ^ { * }$ by $( p ^ { * } + \theta p )$ , where $| \pmb \theta |$ is so small that, if $\scriptstyle { \pmb { x } } _ { t }$ is not in $\mathcal { Z } ,$ , the sign of $\{ f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta p ( x _ { t } ) \}$ is the same as the sign of $s ^ { * } ( x _ { t } )$ . It follows that the replacement changes the value of expression (15.25) by the amount

$$
- \theta \sum _ { t = 1 } ^ { m } w _ { t } s ^ { * } ( x _ { t } ) p ( x _ { t } ) + \theta \sum _ { x _ { t } \in \mathcal { X } } w _ { t } \big | p ( x _ { t } ) \big | .
$$

Therefore, if the left-hand side of expression (15.26) is larger than the right-hand side,one may choose the sign of $\pmb \theta$ so that $( p ^ { * } + \theta p )$ is a better approximation than $p ^ { * }$

Conversely,if condition (15.26) is obtained for all $p$ in $\mathcal { A } _ { : }$ ， then, by replacing the integrals in expression (14.15) by weighted sums, it follows that $p ^ { * }$ is a best discrete $L _ { 1 }$ approximation to the data.□

The following theorem shows that there is a function $p ^ { * }$ in $\mathcal { A }$ that minimizes expression (15.25),and that is such that the set $\mathcal { Z }$ of Theorem 15.2 contains at least $( n + 1 )$ points, where $( n + 1 )$ is the dimension of $\mathscr { A }$ Therefore many algorithms for calculating best discrete $L _ { 1 }$ approximations seek a set $\mathcal { Z }$ that allows an optimal function $p ^ { * }$ to be obtained by interpolation.

# Theorem 15.3

Let the function values $\{ f ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ and fixed positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ be given. Let $\mathcal { A }$ be a linear subspace of ${ \mathcal { R } } ^ { m }$ ， where the components of each vector $p$ in $\mathcal { A }$ have the values $\{ p ( x _ { t } ) ; t =$ $1 , 2 , \ldots , m \}$ . Then there exists an element $p ^ { * }$ in $\{ \mathcal { A } ,$ ，that minimizes expression (15.25),and that has the property that the zero vector is the only element $p$ in $\mathcal { A }$ that satisfies the conditions $\{ p ( x _ { t } ) = 0 ; x _ { t } \in \mathcal { X } \}$ ,where the set $\mathcal { Z }$ is defined in Theorem 15.2.

Proo0f.  Let $p ^ { * }$ be a best weighted $L _ { 1 }$ approximation from $\mathcal { A }$ to the data, but suppose that there exists a non-zero element $q$ in $\mathcal { A }$ that satisfies the condition

$$
q ( x _ { t } ) = 0 , \qquad x _ { t } \in \mathcal { X } .
$$

We consider the function

$$
\psi ( \theta ) = \sum _ { t = 1 } ^ { m } w _ { t } \big | f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta q ( x _ { t } ) \big | , \qquad - \infty < \theta < \infty ,
$$

where $\pmb \theta$ is a real variable. It is a continuous, piecewise linear function of $\theta _ { \mathrm { i } }$ that tends to infinity when $| \theta |$ becomes large,and that takes its least value when $\pmb \theta$ is zero, because $p ^ { * }$ is a best approximation. Moreover, equation (15.28) implies that two different line segments of $\psi$ do not join at $\pmb \theta = 0$ Therefore $\psi$ is constant in a neighbourhood of $\pmb \theta = 0$ If $\pmb \theta$ is increased from zero, then $\psi ( \theta )$ remains constant until a value of $\pmb \theta$ is reached that satisfies the conditions

$$
\left. { \begin{array} { l } { f ( x _ { t } ) - p ^ { * } ( x _ { t } ) - \theta q ( x _ { t } ) = 0 } \\ { q ( x _ { t } ) \neq 0 } \end{array} } \right\}
$$

for some value of $t .$ Let this value of $\pmb \theta$ be ${ \bar { \theta } } .$ Because $\psi ( { \overline { { \theta } } } )$ is equal to $\psi ( 0 )$ ， the function $( p ^ { * } + { \bar { \theta } } q )$ is another best weighted $L _ { 1 }$ approximation from $\mathscr { A }$ to the data. Equation (15.28) implies that the residuals $\{ f ( x _ { t } ) -$ $( p ^ { * } + \bar { \theta } q ) ( x _ { t } ) ; x _ { t } \in \mathcal { Z } \}$ are zero.Further,another zero residual is obtained from the first line of expression (15.30). Hence our construction increases the number of zeros of a best approximation. Because the construction can be applied recursively,it follows that the theorem is true.□

This theorem shows that the calculation of a best discrete $L _ { 1 }$ approximation can be regarded as a search for suitable interpolation points in the set of data points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ . A systematic method of searching is needed,and also it is necessary to test whether a trial set of interpolation points gives a best approximation.The condition (15.26) is not suitable in practice,because it has to be satisfied for every element of ${ \mathcal { A } } .$ All of these problems can be solved quite routinely, because the complete calculation is a linear programming problem.

# 15.4 Linear programming methods

In order to show that the best discrete $L _ { 1 }$ approximation calculation is a linear programming problem, we let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a basis of the space $\mathcal { A }$ of approximations,and we write the expression (15.25), whose least value is required, in the form

$$
\sum _ { t = 1 } ^ { m }  w _ { t } | f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) | ,
$$

where the parameters $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ are some of the variables of the linear programming calculation.We also introduce two new variables for each data point,which we call $\{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2$ ， $\dots , m \}$ . They have to satisfy both the non-negativity conditions

$$
\begin{array} { r } { u _ { t } \geqslant 0 } \\ { v _ { t } \geqslant 0 } \end{array} , \qquad t = 1 , 2 , \ldots , m ,
$$

and the bounds

$$
- v _ { t } \leqslant f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \leqslant u _ { t } , \qquad t = 1 , 2 , \ldots , m .
$$

Therefore,if, for any values of the coefficients $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ ,the variables $\pmb { u } _ { t }$ and $v _ { t }$ are chosen to minimize the sum $\left( u _ { t } + v _ { t } \right)$ ， then the equation

$$
u _ { t } + v _ { t } = \left| f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \right|
$$

is satisfied. It follows that we require the least value of the expression

$$
\sum _ { t = 1 } ^ { m } w _ { t } ( u _ { t } + v _ { t } ) ,
$$

subject to the constraints (15.32） and (15.33) on the values of the variables $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \} , \{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2 ,$ $\cdots , m \}$ ,which is a linear programming calculation.

Because the use of a general linear programming procedure is less efficient than one that is adapted to the calculation of the last paragraph,it is helpful to think of the linear programming method geometrically. The constraints define a convex polyhedron of feasible points in the space of the variables,and there is a solution to the calculation at a vertex of the polyhedron. The characteristic properties of a vertex are that it is feasible, and it is on the boundary of as many linearly independent constraints as there are variables, namely $( 2 m + n + 1 )$ . Because each of the variables $\{ u _ { t } ; t = 1 , 2 , \ldots , m \}$ and $\{ v _ { t } ; t = 1 , 2 , \ldots , m \}$ has to occur in at least one of the independent constraints, the equations

$$
\begin{array} { l } { { u _ { t } = \displaystyle \operatorname* { m a x } \left[ 0 , f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) \right] \Bigg \} } } \\ { { v _ { t } = \displaystyle \operatorname* { m a x } \left[ 0 , \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) - f ( x _ { t } ) \right] \Bigg ) , } } \end{array} \quad t = 1 , 2 , \ldots , m ,
$$

are satisfied at every vertex.The remaining $( n + 1 )$ constraints that hold as equations have the form

$$
f ( x _ { t } ) = \sum _ { i = 0 } ^ { n } \lambda _ { i } \phi _ { i } ( x _ { t } ) , \qquad t \in \mathcal { T } ,
$$

where $\mathcal { T }$ is a subset of the integers $\left\{ 1 , 2 , \ldots , m \right\}$ . Because $\mathcal { T }$ contains $( n + 1 )$ elements,and because the constraints that define a vertex are linearly independent, we have another explanation of Theorem 15.3.

At the beginning of an iteration of the simplex method for solving a linear programming calculation, the variables are set to the coordinates of a vertex of the polyhedron. If it is not possible to reduce the function (15.35) by moving along one of the edges of the polyhedron that meet at the vertex, then the current values of the variables $\{ \lambda _ { i } ; i = 0 , 1 , \ldots , n \}$ are the ones that minimize the function (15.31). Thus there is a test for optimality which is more useful than condition (15.26),because it depends on a finite number of inequalities.

An edge of the polyhedron is defined to be in the intersection of the boundaries of $( 2 m + n )$ linearly independent constraints. One way of generating an edge from a vertex is to give up one of the conditions (15.36),but these edges are irrelevant because they always lead to increases in the objective function (15.35).Therefore we have to consider only edges that satisfy expression (15.36),and that are defined by $\pmb { n }$ independent equations from the system (15.37). We let $\mathcal { T } _ { \mathtt { E } }$ be the set of indices of the independent equations. Hence $\mathcal { T } _ { \mathtt { E } }$ is a subset of $\mathcal { T } .$ Except for a constant scaling factor， there is a unique non-trivial solution $\{ \bar { \lambda } _ { i } ; i = 0 , 1 , \ldots , n \}$ to the conditions

$$
\sum _ { i = 0 } ^ { n } \bar { \lambda } _ { i } \phi _ { i } ( x _ { t } ) = 0 , \qquad t \in \mathcal { T } _ { \mathsf { E } } .
$$

If $\{ \lambda _ { i } = \hat { \lambda } _ { i } ; i = 0 , 1 , \ldots , n \}$ is the solution of the system (15.37), then, at a general point on the edge, the equations $\left\{ \lambda _ { i } = \hat { \lambda } _ { i } + \alpha \bar { \lambda } _ { i } \right.$ ； $i = 0 , 1 , \ldots , n \}$ are obtained,where $\pmb { \alpha }$ is a real parameter. Moreover,the objective function (15.35) has the value

$$
\psi ( \alpha ) = \sum _ { t = 1 } ^ { m } w _ { t } \bigg | f ( x _ { t } ) - \sum _ { i = 0 } ^ { n } ( \hat { \lambda } _ { i } + \alpha \bar { \lambda } _ { i } ) \phi _ { i } ( x _ { t } ) \bigg | .
$$

Suppose that, at the vertex where equations (15.36) and(15.37) hold, it is found that the objective function is reduced if a move is made along the edge that is defined by equations (15.36) and (15.38). The far end of the edge in the $( 2 m + n + 1 )$ -dimensional space of the variables is reached when one of the terms $\{ f ( x _ { t } ) - \sum \lambda _ { i } \phi _ { i } ( x _ { t } ) ; t = 1 , 2 , \ldots , m \}$ in expression (15.36) changes sign.At this point the term that changes sign is zero. Hence another interpolation condition of the form (15.37) is satisfied, which implies that the point is another vertex of the polyhedron. A standard linear programming procedure would have to begin a new iteration at this vertex. However, because our purpose is to make the function (15.31) as smallas possible, it is sensible to continue to change $_ { \alpha }$ until the function (15.39) reaches its least value. Hence we are searching along a locus that is composed of straight line segments in the space of the variables.Because the optimal point on the locus is also a vertex of the polyhedron of feasible points,all other features of the standard simplex method can be retained. The technique of choosing $\pmb { \alpha }$ to minimize expression (15.39) on every iteration can provide large gains in effciency, especially when the linear programming calculation is obtained by discretizing the continuous problem that is studied in Chapter 14.

One reason for discretizing a continuous problem is that it may not be possible to minimize expression (14.1) by the method that is described at the end of Section 14.3, because the error function of the best approximation may have too many zeros.A standard technique in this case is to apply a linear programming procedure to minimize the sum (15.31) instead,where the weights $\{ w _ { t } ; t = 1 , 2 , \dots , m \}$ and the data points $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ are chosen so that expression (15.31) is an adequate approximation to the integral (14.1). It is not appropriate to use a high order integration formula, because the integrand has first derivative discontinuities,and because the discretization forces $( n + 1 )$ zeros of the final error function $\left\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \right\}$ to be in the point set $\{ x _ { t } ; t =$ $1 , 2 , \ldots , m \}$ . Therefore usually $_ m$ has to be large.

An extension of this linear programming method provides a useful algorithm that can be applied directly to the minimization of the continuous $L _ { 1 }$ distance function (14.1). It comes from the remark that, in the linear programming procedure,expression (15.39) can be replaced by the integral

$$
\int _ { a } ^ { b } \Big | f ( x ) - \sum _ { i = 0 } ^ { n } \big ( \hat { \lambda } _ { i } - \alpha \bar { \lambda } _ { i } \big ) \phi _ { i } ( x ) \Big | \mathrm { d } x ,
$$

in order to determine the value of $\pmb { \alpha }$ that is most appropriate to the continuous calculation. Each iteration begins with a trial approximation, $\pmb { \hat { p } }$ say, to $f ,$ that has the property that the set

$$
{ \mathcal { L } } = \{ x : f ( x ) = { \hat { p } } ( x ) ; a \leqslant x \leqslant b \}
$$

contains at least $\pmb { n }$ points.A subset $\mathcal { L } _ { \mathrm { E } }$ is chosen that is composed of exactly $\pmb { n }$ points of $\mathscr { Z }$ and $\bar { p }$ is defined to be a non-zero function in $\mathscr { A }$ that satisfies the equations $\{ \bar { p } ( x ) = 0 ; x \in \mathcal { X } _ { \mathrm { E } } \}$ .The iteration replaces $\pmb { \hat { p } }$ by $\left( \hat { p } + \alpha \bar { p } \right)$ ，where $\pmb { \alpha }$ has the value that minimizes the norm $\| f - \hat { p } - \alpha \bar { p } \| _ { 1 }$ ， which is equal to expression (15.4O). Then another iteration is begun. Most of the details are taken from the linear programming method that has been described already, but an important difference is the need to evaluate integrals. It is therefore worth noting that, because the calculation of $_ \alpha$ is itself an $L _ { 1 }$ approximation problem, the required value depends only on integrals of $\bar { p }$ and on the sign properties of the error function $\left( f - \hat { p } - \alpha \bar { p } \right)$ . Exercise 15.6 gives an example of the use of this algorithm.

# 15 Exercises

15.1Let $f$ be the function in $\mathcal { C } _ { 2 \pi }$ that takes the values $\{ f ( x ) = x$

$- { \scriptstyle { \frac { 1 } { 2 } } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ and $\{ f ( x ) = \pi - x ; { \frac { 1 } { 2 } } \pi \leqslant x \leqslant { \frac { 3 } { 2 } } \pi \}$ . Prove that the equation

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { 1 } } \int _ { 0 } ^ { 2 \pi } { \big | } f ( x ) - q ( x ) { \big | } \mathrm { d } x = \pi ^ { 2 } / 1 8
$$

is satisfied.

15.2 Deduce directly from expressions (15.18) and (15.19) that the term ${ \frac { 1 } { 2 } } \pi / ( n + 1 )$ that occurs in inequality (15.16) is optimal.

15.3 Let $\mathscr { A }$ be any linear space of functions that are defined on the point set $\{ x _ { t } ; t = 1 , 2 , \ldots , m \}$ ,where the dimension of $\mathscr { A }$ is less than m. Prove that there exist function values $\{ f ( x _ { t } ) ; t = 1 , 2 ,$ $\cdots , m \}$ and positive weights $\{ w _ { t } ; t = 1 , 2 , \ldots , m \}$ such that more than one element of $\mathscr { A }$ minimizes expression (15.25). Construct an example of non-uniqueness of best discrete $L _ { 1 }$ approximations in the case when $\mathscr { A }$ is the space $\mathcal { P } _ { 2 }$

15.4 The polynomial $\{ p ( x ) = 1 6 x - { x ^ { 2 } } ; 1 \leqslant x \leqslant 8 \}$ is one of several functions in $\mathcal { P } _ { 3 }$ that minimizes the expression

$$
\sum _ { i = 1 } ^ { 8 } \ w _ { i } \vert f ( x _ { i } ) - p ( x _ { i } ) \vert , \qquad p \in \mathcal { P } _ { 3 } ,
$$

where the data have the values $w _ { 1 } = w _ { 8 } = 1$ ， $w _ { 3 } = w _ { 6 } = w _ { 7 } = 2$ ， $w _ { 2 } = w _ { 4 } = w _ { 5 } = 3 ,$ $f ( 1 ) = 1 5$ ， $f ( 2 ) = 3 1$ ， $f ( 3 ) = 3 9$ ， $f ( 4 ) \dot { = } 4 6$ ， $f ( 5 ) = 5 8$ ， $f ( 6 ) = 6 0$ ， $f ( 7 ) = 6 2$ ，and $f ( 8 ) = 6 4$ . Find another function in $\mathcal { P } _ { 3 }$ that minimizes this expression.

15.5 The best $L _ { 1 }$ approximation in $\mathcal { P } _ { 1 }$ is required to the data $f ( 0 ) =$ $^ { - 3 5 }$ ， $f ( 1 ) = - 5 6$ ， $f ( 2 ) = 0$ ， $f ( 3 ) = - 1 6 ,$ ， $f ( 4 ) = - 3$ ， $f ( 5 ) = 4$ ， $f ( 6 ) = 1 0$ ， $f ( 7 ) = 5 3$ and $f ( 8 ) = 6 9$ ，where all the weights are equal to one.Calculate it by the method that is described in Section 15.4,where on the first iteration the only point of the set $\{ \boldsymbol { x } _ { t } ; t \in \mathcal { T } _ { \mathtt { E } } \}$ is $\scriptstyle x = 0$

15.6 Let the algorithm that is described in the last paragraph of Section 15.4 be applied to calculate the best $L _ { 1 }$ approximation from $\mathcal { P } _ { 1 }$ to the function $\{ f ( x ) = x ^ { 2 } ; - 1 \leqslant x \leqslant 1 \}$ Investigate the rate at which the zeros of the error function $\left( f - \hat { p } \right)$ converge to the points $\pm \frac { 1 } { 2 }$ that are given by Theorem 14.5.You should find that, if an iteration adjusts a zero to $\left( { \frac { 1 } { 2 } } + \varepsilon \right)$ ,where $\pmb \varepsilon$ is small, then, when the zero is adjusted again two iterations later, the difference between its new value and $\textstyle { \frac { 1 } { 2 } }$ is of order $\pmb { \varepsilon } ^ { 4 }$

15.7 Theorem 15.3 does not have an analogue in the continuous case. Prove this remark by finding a finite-dimensional linear subspace $\mathscr { A }$ of $\mathcal { C } [ a , b ] ,$ and a function $f$ in $\mathcal { C } [ a , b ]$ , such that every best $L _ { 1 }$ approximation from $\mathscr { A }$ to $f$ has fewer than $( n + 1 )$ zeros,where $( n + 1 )$ is the dimension of $\pmb { \mathcal { A } }$

15.8Let the function values $\{ f ( x _ { i } ) = f ( i ) ; i = 0 , 1 , 2 , 3 , 4 \}$ be given, and let $p ^ { * }$ be a polynomial in $\mathcal { P } _ { 2 }$ that minimizes the expression

$$
\sum _ { i = 0 } ^ { 4 } | f ( i ) - p ( i ) | , \qquad p \in \mathscr { P } _ { 2 } .
$$

Prove that $p ^ { * } ( 0 )$ and $p ^ { * } ( 4 )$ are equal to $f ( 0 )$ and $f ( 4 )$ respectively.

15.9 Let $\boldsymbol { \bar { \mathcal { A } } } _ { 0 , 1 }$ be the set of functions in $\mathcal { C } [ - 1 , 4 ]$ that have the form $\{ \alpha / ( 1 + \beta x ) ; - 1 \leqslant x \leqslant 4 \}$ ，where $\pmb { \alpha }$ and $\beta$ are real parameters.

Calculate the function $p ^ { * }$ that minimizes the weighted sum

$$
\begin{array} { r } { \big \vert 9 - p ( - 1 ) \big \vert + M \big \vert 8 - p ( 0 ) \big \vert + \big \vert 4 - p ( 4 ) \big \vert , \qquad p \in \bar { \mathcal { A } } _ { 0 , 1 } , } \end{array}
$$

where the weight $M$ is so large that the condition $p ^ { * } ( 0 ) = 8$ is obtained. The purpose of this exercise is to show that Theorem 15.3 does not extend to rational approximation on a discrete point set.

15.10Investigate the convergence properties of the algorithm that is described in the last paragraph of Section 15.4, in the case when the choice of $\mathcal { Z } _ { \mathrm { E } }$ is governed by the rule that no point shall remain in $\mathcal { L } _ { \mathrm { E } }$ for more than $_ n$ iterations. You may assume that all functions are continuously differentiable,that $\mathscr { A }$ satisfies the Haar condition,and that every error function that is calculated has exactly $( n + 1 )$ zeros.

# The order of convergence of polynomial approximations

# 16.1 Approximations to non-differentiable functions

In the first three sections of this chapter we consider the error of the best minimax approximation from ${ \mathcal { Q } } _ { n }$ 'to a function $f$ in $\mathcal { C } _ { 2 \pi } .$ Specifically we study the dependence on $\pmb { n }$ of the number

$$
\operatorname* { m i n } _ { q \in { \mathcal { Q } } _ { n } } \| f - q \| _ { \infty } = E _ { n } ( f ) ,
$$

say. Section 16.4 extends the work to best minimax approximations from $\mathcal { P } _ { n }$ to functions in $\mathcal { C } [ - 1 , 1 ]$ .Most of the theory depends on the bound

$$
E _ { n } ( f ) \leqslant \frac { \pi } { 2 ( n + 1 ) } \| f ^ { \prime } \| _ { \infty } , \qquad f \in \mathcal { C } _ { 2 \pi } ^ { ( 1 ) } ,
$$

which is given in Theorem 15.1. The purpose of this section is to show that, by elementary analysis, one can deduce from inequality (16.2) some bounds on $E _ { n } ( f )$ ,that hold when $f$ is non-differentiable.

The technique that is used depends on a differentiable function that is close to $f .$ We let $\pmb { \delta }$ be a small positive number, and we let $\phi$ be the function

$$
\phi \left( x \right) = { \frac { 1 } { 2 \delta } } \int _ { x - \delta } ^ { x + \delta } f ( \theta ) { \mathrm { d } } \theta , \qquad - \infty < x < \infty ,
$$

which is in $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ for any $f$ in $\mathcal { C } _ { 2 \pi }$ . The derivative of $\phi$ has the value

$$
\phi ^ { \prime } ( x ) = { \frac { 1 } { 2 \delta } } [ f ( x + \delta ) - f ( x - \delta ) ] , \qquad - \infty < x < \infty ,
$$

and $\phi$ tends to $f$ if $\pmb { \delta }$ tends to zero. The proof of the following theorem depends on both of these properties.

Theorem 16.1 (Jackson II)

Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that satisfies the Lipschitz condition

$$
\big | f ( x _ { 1 } ) - f ( x _ { 0 } ) \big | \leqslant M | x _ { 1 } - x _ { 0 } | ,
$$

for all real numbers $x _ { 1 }$ and $x _ { 0 }$ ，where $M$ is a constant. Then expression (16.1) is bounded by the inequality

$$
E _ { n } ( f ) \leqslant \pi M / 2 ( n + 1 ) .
$$

Proof. For every function $\phi$ in $\mathcal { C } _ { 2 \pi }$ the inequality

$$
\begin{array} { r l } & { { E } _ { n } ( f ) \leqslant \| f - q ^ { * } \| _ { \infty } } \\ & { \qquad \leqslant \| f - \phi \| _ { \infty } + \| \phi - q ^ { * } \| _ { \infty } } \\ & { \qquad = \| f - \phi \| _ { \infty } + { E } _ { n } ( \phi ) } \end{array}
$$

is satisfied, where $q ^ { * }$ is the best approximation from ${ \mathcal { Q } } _ { n }$ to $\phi$ . We let $\phi$ be the function (16.3). Therefore condition (16.5) gives the bound

$$
\begin{array} { l } { \displaystyle \| f - \phi \| _ { \infty } = \operatorname* { m a x } _ { \boldsymbol { x } } \frac { 1 } { 2 \delta } \left| \int _ { \boldsymbol { x } - \delta } ^ { \boldsymbol { x } + \delta } f ( \boldsymbol { x } ) - f ( \theta ) \mathrm { d } \theta \right| } \\ { \displaystyle \leqslant \operatorname* { m a x } _ { \boldsymbol { x } } \frac { M } { 2 \delta } \int _ { \boldsymbol { x } - \delta } ^ { \boldsymbol { x } + \delta } \left| \boldsymbol { x } - \theta \right| \mathrm { d } \theta } \\ { \displaystyle = \frac { 1 } { 2 } M \delta . } \end{array}
$$

Moreover expressions (16.4) and (16.5) imply the inequality

$$
\| \phi ^ { \prime } \| _ { \infty } \leqslant M .
$$

Therefore,if we replace $f$ by $\phi$ in condition (16.2), it follows from inequalities (16.7) and (16.8) that the bound

$$
\begin{array} { r } { E _ { n } ( f ) \leqslant \frac { 1 } { 2 } M \delta + \pi M / 2 ( n + 1 ) } \end{array}
$$

is satisfied. Because $\pmb { \delta }$ can be arbitrarily small, the required result (16.6) is implied by expression (16.10).□

Expression (16.2) also implies a bound on $E _ { n } ( f )$ ,when $f$ is a continuous function that does not satisfy a Lipschitz condition.

Theorem 16.2 (Jackson III) For every function $f$ in $\mathcal { C } _ { 2 \pi } ,$ the inequality

$$
E _ { n } ( f ) \leqslant \frac { 3 } { 2 } \omega \left( \frac { \pi } { n + 1 } \right)
$$

is obtained, where $\pmb { \omega }$ is the modulus of continuity of $f$

Proof. We again substitute the function (16.3) in expression (16.7). Instead of inequality (16.8), however, we have the bound

$$
\begin{array} { l } { \displaystyle \| f - \phi \| _ { \infty } = \underset { \displaystyle x } { \mathrm { m a x } } \frac { 1 } { 2 \delta } \left| \int _ { x - \delta } ^ { x + \delta } f ( x ) - f ( \theta ) \mathrm { d } \theta \right| } \\ { \displaystyle \leqslant \operatorname* { m a x } _ { \displaystyle x } \frac { 1 } { 2 \delta } \int _ { x - \delta } ^ { x + \delta } \omega \big ( | x - \theta | \big ) \mathrm { d } \theta } \\ { \displaystyle \leqslant \omega \big ( \delta \big ) . } \end{array}
$$

Moreover, because equation (16.4) implies the condition

$$
\begin{array} { c } { { \| \phi ^ { \prime } \| _ { \infty } \leqslant \omega \left( 2 \delta \right) / 2 \delta } } \\ { { \leqslant \omega \left( \delta \right) / \delta , } } \end{array}
$$

where the last line is an elementary property of the modulus of continuity, expression (16.2) gives the bound

$$
E _ { n } ( \phi ) { \leqslant } \frac { \pi } { 2 ( n + 1 ) \delta } { \omega } ( \delta ) .
$$

It follows from condition (16.7) that the inequality

$$
E _ { n } ( f ) \leqslant \biggl [ 1 + \frac { \pi } { 2 ( n + 1 ) \delta } \biggr ] \omega ( \delta )
$$

is satisfied.Therefore,to complete the proof of the theorem,it is sufficient to let $\delta$ have the value $\pi / ( n + 1 )$ .□

We note that inequality (16.11) gives a proof of Theorem 13.1, for it shows that $E _ { n } ( f )$ tends to zero as $_ n$ tends to infinity. Further,extending inequality (16.11） to approximation by algebraic polynomials,which is done in Theorem 16.5，gives another proof of the Weierstrass Theorem 6.1.

In fact inequality (16.11) remains true if the constant $\textstyle { \frac { 3 } { 2 } }$ is replaced by the value one. The following example shows that the parameters $c _ { 1 }$ and $c _ { 2 }$ in the bound

$$
E _ { n } ( f ) \leqslant c _ { 1 } \omega ( c _ { 2 } \pi / [ n + 1 ] ) , \qquad f \in \mathcal { C } _ { 2 \pi } ,
$$

cannot both be less than one.

Let $c _ { 2 }$ be from $( { \textstyle { \frac { 1 } { 2 } } } , 1 )$ ,let $\varepsilon$ have the value

$$
\varepsilon = ( 1 - c _ { 2 } ) \pi / ( n + 1 ) ,
$$

and let $\dot { f }$ be a function in $\mathcal { C } _ { 2 \pi }$ that satisfies the following conditions. For each integer $j , f$ does not change sign on the interval $[ j \pi / ( n + 1 ) - { \textstyle { \frac { 1 } { 2 } } } \pmb { \varepsilon } .$ ， $j \pi / { \left( n + 1 \right) } + { \textstyle \frac { 1 } { 2 } } \varepsilon ] _ { \cdot }$ and $f$ is zero on the interval $[ j \pi / ( n + 1 ) + { \textstyle \frac { 1 } { 2 } } \varepsilon .$ ， $( j + 1 )$ $\pi / ( n + 1 ) { - } \frac { 1 } { 2 } \varepsilon ]$ .The equations

$$
\| f \| _ { \infty } = 1
$$

and

$$
f ( j \pi / [ n + 1 ] ) = ( - 1 ) ^ { j } , \qquad j = 0 , \pm 1 , \pm 2 , . . . ,
$$

hold.A suitable function is shown in Figure 16.1. Expressions (16.18) and (16.19) imply that the zero function is a best approximation from ${ \mathcal { Q } } _ { n }$ to $f ,$ because otherwise a best approximation would change sign $( 2 n + 2 )$ times in $[ 0 , 2 \pi ]$ . Hence $E _ { n } ( f )$ is equal to one. Moreover, Figure 16.1 shows that $\pmb { \omega } ( \pmb { \pi } / [ n + 1 ] - \pmb { \varepsilon } )$ is also equal to one. Therefore substituting the value (16.17) gives the equation

$$
E _ { n } ( f ) = \omega ( c _ { 2 } \pi / [ n + 1 ] ) .
$$

Thus, if $c _ { 2 } < 1$ in inequality (16.16), then $\pmb { c } _ { 1 }$ is not less than one.

# 16.2 The Dini-Lipschitz theorem

The Dini-Lipschitz theorem identifies a quite general class of functions $f$ in $\mathcal { C } _ { 2 \pi } ,$ such that $\pmb { S _ { n } f }$ converges uniformly to $f$ as $\pmb { n }$ tends to infinity, where $S _ { n }$ is the Fourier series operator that is defined in Section 13.2. Because the method of proof depends on Theorem 3.1, we require an upper bound on $\| \pmb { S _ { n } } \|$ .Therefore we recall from Section 13.2 that the norm has the value

$$
\left\| S _ { n } \right\| = { \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } \left| { \frac { \sin \left[ ( n + { \frac { 1 } { 2 } } ) \theta \right] } { \sin \left( { \frac { 1 } { 2 } } \theta \right) } } \right| \mathrm { d } \theta .
$$

The integrand is bounded above by $( 2 n + 1 )$ and by ${ \pmb \pi } / \theta ;$ ，where the first bound is a consequence of equation (12.51),and where the second bound follows from the elementary inequality

$$
\sin \left( { \textstyle { \frac { 1 } { 2 } } } \theta \right) \geqslant \theta / \pi , \qquad 0 \leqslant \theta \leqslant \pi .
$$

Therefore the relation

$$
\begin{array} { c } { { \displaystyle { \left\| S _ { n } \right\| \leqslant \frac { 1 } { \pi } \int _ { 0 } ^ { \mu } \left( 2 n + 1 \right) \mathbf { d } \theta + \frac { 1 } { \pi } \int _ { \mu } ^ { \pi } \frac { \pi } { \theta } \mathbf { d } \theta } } } \\ { { = ( 2 n + 1 ) \mu / \pi + \ln \pi - \ln \mu } } \end{array}
$$

![](images/fd21cd815769caf8b379af7daf1b42928ac306846085bfb923382bad6c09b9bb.jpg)  
Figure 16.1. A function that satisfes equation (16.20).

is satisfied for all $\pmb { \mu }$ in $( 0 , \pi )$ . In particular, the value $\pmb { \mu } = \pi / ( 2 n + 1 )$ gives the bound

$$
\left\| S _ { n } \right\| \leqslant 1 + \ln { \left( 2 n + 1 \right) } ,
$$

which is sufficient to prove the following theorem.

Theorem 16.3 (Dini-Lipschitz)

If $f$ is any function in $\mathcal { C } _ { 2 \pi }$ whose modulus of continuity satisfies the condition

$$
\operatorname * { l i m } _ { \delta  0 } | \omega ( \delta ) \ln \delta | = 0 ,
$$

then the sequence of Fourier series approximations $\{ S _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$

Proof. By applying Theorem 3.1, then Theorem 16.2,and then expression (16.24),we deduce the bound

$$
\begin{array} { l } { \displaystyle \| f - S _ { n } f \| _ { \infty } \leqslant [ 1 + \| S _ { n } \| ] E _ { n } ( f ) } \\ { \displaystyle \leqslant \frac { 3 } { 2 } [ 1 + \| S _ { n } \| ] \omega \Big ( \frac { \pi } { n + 1 } \Big ) } \\ { \displaystyle \leqslant \frac { 3 } { 2 } [ 2 + \ln { ( 2 n + 1 ) } ] \omega \Big ( \frac { \pi } { n + 1 } \Big ) . } \end{array}
$$

Because the elementary inequality

$$
\ln { \left( 2 n + 1 \right) } < \ln { \left( 2 \pi \right) } + \left| \ln { \left( \frac { \pi } { n + 1 } \right) } \right|
$$

and condition (16.25) imply that the right-hand side of expression (16.26) tends to zero as $_ n$ tends to infinity, it follows that the theorem is true.□

One reason why the theorem is useful is that it is often easy to show that a continuous function satisfies condition (16.25). However, condition (16.25) is not necessary for the uniform convergence of the Fourier series. It is not possible to strengthen the theorem by improving the bound (16.24), because $\| S _ { n } \|$ is bounded below by a multiple of ln n. Specifically, equation (16.21) and elementary arithmetic give the inequality

$$
\begin{array} { l } { \displaystyle \| S _ { n } \| > \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \int _ { ( j - 1 ) \pi / ( n + \frac { 1 } { 2 } ) } ^ { j \pi / ( n + \frac { 1 } { 2 } ) } \left| \frac { \sin { \left[ ( n + \frac { 1 } { 2 } ) \theta \right] } } { \theta } \right| \mathrm { d } \theta } \\ { \displaystyle > \frac { 2 } { \pi } \sum _ { j = 1 } ^ { n } \frac { n + \frac { 1 } { 2 } } { j \pi } \int _ { ( j - 1 ) \pi / ( n + \frac { 1 } { 2 } ) } ^ { j \pi / ( n + \frac { 1 } { 2 } ) } \left| \sin { \left[ ( n + \frac { 1 } { 2 } ) \theta \right] } \right| \mathrm { d } \theta } \\ { \displaystyle = ( 4 / \pi ^ { 2 } ) \sum _ { j = 1 } ^ { n } \frac { 1 } { j } } \\ { \displaystyle > ( 4 / \pi ^ { 2 } ) \ln { ( n + 1 ) } , } \end{array}
$$

which is important to the work of the next chapter.

# 16.3 Some bounds that depend on higher derivatives

It is interesting that Theorems 16.1 and 16.2 apply to Lipschitz continuous and to continuous functions,because they are derived from an inequality, namely expression (16.2), that is valid when $f$ is continuously differentiable.In this section we move in the other direction,for, given that $f$ can be differentiated more than once,we deduce a bound on $E _ { n } ( f )$ that is stronger than expression (16.2). Our main result is analogous to Theorem 3.2, but it is a little more difficult to prove, because, if $r$ is a trigonometric polynomial, then the indefinite integral of $r$ is also a trigonometric polynomial only if the constant term of $r$ is zero.

Theorem 16.4 (Jackson IV)

If the function $f$ is in the space $\mathcal { C } _ { 2 \pi } ^ { ( k ) }$ ， then the error of the best approximation from ${ \mathcal { Q } } _ { n }$ to $f$ satisfies the condition

$$
E _ { n } ( f ) \leqslant { \bigg ( } { \frac { \pi } { 2 n + 2 } } { \bigg ) } ^ { k } \| f ^ { ( k ) } \| _ { \infty } .
$$

Proof. First we establish the bound

$$
E _ { n } ( f ) \leqslant \frac { \pi } { 2 n + 2 } \| f ^ { \prime } - r \| _ { \infty } ,
$$

where $r$ is any function in ${ \mathcal { Q } } _ { n }$ ,and then the proof is completed by induction on $k$ .We obtain inequality (16.30) by extending the proof of Theorem 15.1. If $f ^ { \prime }$ is replaced by $( f ^ { \prime } - r )$ in the second integral of equation (15.11), the right-hand side of this equation is changed by the amount

$$
- \frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \theta r \left( \theta + x + \pi \right) { \bf d } \theta = \phi ( x ) ,
$$

say. We may express $r ( \theta + x + \pi )$ in terms of cos $( j \pmb { \theta } )$ ,sin $( j \pmb \theta )$ ,cos $( j x )$ and sin $( j x )$ ，for $j = 0 , 1 , \ldots , n$ , and we may integrate over $\pmb \theta$ analytically, which shows that the function $\{ \phi ( x ) , - \infty < x < \infty \}$ is in ${ \mathcal { Q } } _ { n }$ . It follows from equation (15.11),and from the fact that the first term on the right-hand side of this equation is a constant, that $E _ { n } ( f )$ is equal to the maximum error of the best approximation from ${ \mathcal { Q } } _ { n }$ to the function

$$
\frac { 1 } { 2 \pi } \int _ { - \pi } ^ { \pi } \theta [ f ^ { \prime } ( \theta + x + \pi ) - r ( \theta + x + \pi ) ] \mathrm { d } \theta , \qquad - \infty < x < \infty ,
$$

where $r$ is any element of ${ \mathcal { Q } } _ { n }$ .Hence inequality (15.18) remains valid if $f ^ { \prime }$ is replaced by $( f ^ { \prime } - r )$ . Therefore the required condition (16.30） is a consequence of expression (15.19).

To begin the inductive part of the proof, we suppose that inequality (16.29)is satisfied when $k$ is replaced by $( k - 1 )$ . It follows from expression (16.3O) and from the inductive hypothesis that the bound

$$
\begin{array} { c } { { E _ { n } ( f ) \displaystyle \leqslant \frac { \pi } { 2 n + 2 } \displaystyle \operatorname* { m i n } _ { r \in \mathcal { Q } _ { n } } \| f ^ { \prime } - r \| _ { \infty } } } \\ { { \displaystyle = \frac { \pi } { 2 n + 2 } E _ { n } ( f ^ { \prime } ) } } \\ { { \displaystyle \leqslant \left( \frac { \pi } { 2 n + 2 } \right) ^ { k } \| f ^ { ( k ) } \| _ { \infty } } } \end{array}
$$

is obtained, which is the general step of the inductive argument. Because Theorem 15.1 states that inequality(16.29) holds when $k = 1$ ,the proof is complete.□

One fundamental difference between Theorems 3.2 and 16.4 is that Theorem 16.4 does not require the condition $k \leqslant n$ It is therefore interesting to consider the consequences of inequality (16.29) when $k$ is larger than $_ n$ .For example, if $f$ is an infinitely differentiable function whose derivatives are bounded, if we let $n = 1$ ,and if we take the limit of inequality (16.29) as $\pmb { k }$ tends to infinity, then it follows that $E _ { 1 } ( f )$ is zero. Thus the function $f$ is in the space $\mathcal { Q } _ { 1 }$ , which can also be proved from the fact that the derivatives of the Fourier series expansion of $f$ are equal to the derivatives of $f .$ The more usual application of Theorem 16.4, however, is when a bound on $\| f ^ { ( k ) } \| _ { \infty }$ is known,and a trigonometric polynomial approximation to $f$ is required,whose maximum error does not exceed a given tolerance.Inequality (16.29) provides a value of $n$ such that a trigonometric polynomial from ${ \mathcal { Q } } _ { n }$ is suitable.

# 16.4 Extensions to algebraic polynomials

In this section we deduce from Theorems 16.1 and 16.2 some useful bounds on the least maximum error

$$
d _ { n } ^ { \ast } \left( g \right) = \operatorname* { m i n } _ { p \in \mathscr { P } _ { n } } \left\| g - p \right\| _ { \infty } ,
$$

where $\pmb { g }$ is a function in $\mathcal { C } [ - 1 , 1 ]$ . It is necessary to relate approximation by algebraic polynomials to best approximation by trigonometric polynomials.The following technique is used,which is similar to one that occurs in the proof of Theorem 13.1.

Given $_ g$ in $\mathcal { C } [ - 1 , 1 ]$ , we let $f$ be the function in $\mathcal { C } _ { 2 \pi }$ that is defined by the equation

$$
f ( x ) = g ( \cos x ) , \qquad - \infty < x < \infty .
$$

We let $q ^ { * }$ be an approximation to $f$ from ${ \mathcal { Q } } _ { n }$ that satisfies the condition

$$
E _ { n } ( f ) = \| f - q ^ { * } \| _ { \infty } .
$$

Because $f$ is an even function, it follows that $q ^ { * }$ is also even, but the theory that has been given does not include a proof of this statement. Instead we note that, if $\{ q ^ { * } ( x ) ; - \infty < x < \infty \}$ is not even, then $\{ q ^ { * } ( - x )$ ； $- \infty < x <$ $\infty \}$ and hence $\scriptstyle { \frac { 1 } { 2 } } [ q ^ { * } ( x ) + q ^ { * } ( - x ) ] ; \ - \infty < x < \infty \}$ are also best approxima-tions from ${ \mathcal { Q } } _ { n }$ to $f .$ Therefore,in the hypothetical case when there is some freedom in $q ^ { * }$ , we can choose $q ^ { * }$ to be an even function, which gives an expansion of the form

$$
q ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } c _ { j } ( \cos x ) ^ { j } , \qquad - \infty < x < \infty ,
$$

where each $c _ { j }$ is a real coeficient. Therefore the algebraic polynomial

$$
p ^ { * } ( t ) = \sum _ { j = 0 } ^ { n } c _ { j } t ^ { j } , \qquad - 1 \leqslant t \leqslant 1 ,
$$

satisfies the equation

$$
q ^ { * } ( x ) = p ^ { * } ( \cos x ) , \qquad - \infty < x < \infty .
$$

It follows from equations (16.34), (16.35), (16.36) and (16.39) that the inequality

$$
\begin{array} { r l } & { d _ { n } ^ { * } \left( g \right) \leqslant \left\| g - p ^ { * } \right\| _ { \infty } } \\ & { \qquad = \underset { - \infty < x < \infty } { \operatorname* { m a x } } \left| f ( x ) - q ^ { * } ( x ) \right| } \\ & { \qquad = E _ { n } ( f ) } \end{array}
$$

is obtained. In fact this inequality is satisfied as an equation for all $_ { g }$ in $\mathcal { C } [ - 1 , 1 ]$ . It is important to the proof of the following theorem.

Theorem 16.5 (Jackson V)

For all functions $_ { g }$ in $\mathcal { C } [ - 1 , 1 ] ,$ ,the least maximum error (16.34) satisfies the bound

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \frac { 3 } { 2 } \omega _ { g } \biggl ( \frac { \pi } { n + 1 } \biggr ) ,
$$

where $\omega _ { g }$ is the modulus of continuity of $\pmb { g }$ 、Further,if the Lipschitz condition

$$
\big | g ( t _ { 1 } ) - g ( t _ { 0 } ) \big | \leqslant M _ { g } \big | t _ { 1 } - t _ { 0 } \big |
$$

holds for all $t _ { 0 }$ and $t _ { 1 }$ in[−1,1], then $d _ { n } ^ { * } ( g )$ is bounded by the inequality

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \pi M _ { g } / 2 ( n + 1 ) .
$$

Proof. The bound (16.41) is a corollary of Theorem 16.2 and condition (16.40), provided that the inequality

$$
\omega _ { f } \Big ( \frac { \pi } { n + 1 } \Big ) \leqslant \omega _ { g } \Big ( \frac { \pi } { n + 1 } \Big )
$$

is obtained, where $\omega _ { f }$ is the modulus of continuity of the function (16.35). In order to establish this inequality we require the elementary relation

$$
\begin{array} { r } { \left| \cos \theta _ { 1 } - \cos \theta _ { 0 } \right| \leqslant \left| \theta _ { 1 } - \theta _ { 0 } \right| . } \end{array}
$$

Thus the bound

$$
\begin{array} { r l } & { \omega _ { g } \Bigg ( \displaystyle \frac { \pi } { n + 1 } \Bigg ) = \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| g ( \theta _ { 1 } ) - g ( \theta _ { 0 } ) \right| } \\ & { \qquad \geqslant \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| g ( \cos \theta _ { 1 } ) - g ( \cos \theta _ { 0 } ) \right| } \\ & { \qquad = \underset { | \theta _ { 1 } - \theta _ { 0 } | \in \pi / ( n + 1 ) } { \operatorname* { m a x } } \left| f ( \theta _ { 1 } ) - f ( \theta _ { 0 } ) \right| } \\ & { \qquad = \omega _ { f } \Bigg ( \frac { \pi } { n + 1 } \Bigg ) } \end{array}
$$

is satisfied, where $f$ is the function (16.35). Therefore the first part of the theorem is true.

In order to prove the second part, we note that inequality (16.42) and the method of proof of inequality (16.44) imply the relation

$$
\begin{array} { r } { \left| f ( x _ { 1 } ) - f ( x _ { 0 } ) \right| \leqslant \omega _ { f } ( \left| x _ { 1 } - x _ { 0 } \right| ) } \\ { \leqslant \omega _ { g } ( \left| x _ { 1 } - x _ { 0 } \right| ) } \\ { \leqslant M _ { g } \left| x _ { 1 } - x _ { 0 } \right| . } \end{array}
$$

Therefore condition (16.43) is a consequence of the bound (16.40) and Theorem 16.1.□

One important corollary of the theorem is the extension of Theorem 15.1 to algebraic polynomials. Because the Lipschitz condition

$$
\big | g ( t _ { 1 } ) - g ( t _ { 0 } ) \big | \leqslant \| g ^ { \prime } \| _ { \infty } \big | t _ { 1 } - t _ { 0 } \big |
$$

is satisfied if $\pmb { g }$ is in $\mathcal { C } ^ { ( 1 ) } [ - 1 , 1 ]$ , expression (16.43) implies the bound

$$
d _ { n } ^ { \ast } \left( g \right) \leqslant \frac { \pi } { 2 ( n + 1 ) } \| g ^ { \prime } \| _ { \infty } .
$$

Therefore inequality (3.19） is valid. Specifically, if the range $[ a , b ]$ is $[ - 1 , 1 ] .$ , we may let $^ c$ have the value ${ \scriptstyle { \frac { 1 } { 2 } } } \pi .$ It follows from Theorem 3.2 that the condition

$$
d _ { n } ^ { * } ( g ) \leqslant \frac { ( n - k ) ! { ( \frac { 1 } { 2 } \pi ) } ^ { k } } { n ! } \| g ^ { ( k ) } \| _ { \infty } , \qquad n \geqslant k ,
$$

is obtained by all functions $\pmb { g }$ in the space $\mathcal { C } ^ { ( k ) } [ - 1 , 1 ]$

We consider whether a bound that is stronger than inequality (16.50) can be found by applying the method of proof of Theorem 16.5 to the bound (16.29). First we let $k = 2$ .Expressions (16.40) and (16.29) imply the relation

$$
d _ { n } ^ { * } \left( g \right) \leqslant \left( \frac { \pi } { 2 n + 2 } \right) ^ { 2 } \left\| f ^ { \prime \prime } \right\| _ { \infty } ,
$$

where $f$ is still the function (16.35). Hence, in order to deduce a condition of the form (16.50), it is necessary to bound $\| f ^ { \prime \prime } \| _ { \infty }$ by a multiple of $\| g ^ { \prime \prime } \| _ { \infty }$ Here the method breaks down, however. For example, if $\pmb { g }$ is the function $\left\{ g ( x ) = x ; - 1 \leqslant x \leqslant 1 \right\}$ ,then $\| g ^ { \prime \prime } \| _ { \infty }$ is zero but $\| f ^ { \prime \prime } \| _ { \infty }$ is one.Therefore the close relation between minimax approximation by trigonometric and algebraic polynomials,which is shown in Theorem 16.5,does not extend to bounds that depend on higher derivatives.

# 16 Exercises

16.1 Find values of $_ n$ such that $E _ { n } ( f )$ is less than $1 0 ^ { - 4 }$ for each of the following three functions $f$ :(i) the function defined in Exercise 15.1,(ii) the function defined in Exercise 13.2,and (ii) a function in $\mathcal { C } _ { 2 \pi }$ that is infinitely differentiable and that satisfies the condition $\| f ^ { ( k ) } \| _ { \infty } \leqslant 1 0 ^ { k }$ , for all positive integers $k$

16.2 Let $c _ { 2 } ( n )$ be a number such that the condition ${ \cal E } _ { n } ( \phi ) \leqslant$ $\phi$ $c _ { 2 } ( n ) \| \phi ^ { \prime \prime } \| _ { \infty }$ beuo163) is satisfied, where $\phi$ is any function in $f$ is anyfunction in $\mathcal { C } _ { 2 \pi } ^ { ( 2 ) }$ Byletting $\mathcal { C } _ { 2 \pi } ^ { ( 1 ) }$ then $E _ { n } ( f )$ is bounded by the inequality $\begin{array} { r } { E _ { n } ( f ) \leqslant [ 2 c _ { 2 } ( n ) ] ^ { \frac { 1 } { 2 } } \| f ^ { \prime } \| _ { \infty } . } \end{array}$

16.3Give an example to show that the value of $c _ { 2 } ( n )$ in the inequality

$$
E _ { n } ( \phi ) \leqslant c _ { 2 } ( n ) \| \phi ^ { \prime \prime } \| _ { \infty } , \qquad \phi \in \mathcal { C } _ { 2 \pi } ^ { ( 2 ) } ,
$$

is at least $\pi ^ { 2 } / [ 8 ( n + 1 ) ^ { 2 } ]$

16.4 Let $f$ be a function in $\mathcal { C } ^ { ( 1 ) } [ 0 , 1 ]$ and let $B _ { n } f$ be the Bernstein approximation (6.23). Deduce from the equation

$$
( f - B _ { n } f ) ( x ) = \sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } { \biggl [ } f ( x ) - f { \biggl ( } { \frac { k } { n } } { \biggr ) } { \biggr ] }
$$

that, when $n = 2$ , the inequality

$$
\| f - B _ { 2 } f \| _ { \infty } \leqslant \frac { 8 } { 2 7 } \| f ^ { \prime } \| _ { \infty }
$$

is satisfied. Compare the bound (16.5O) in the case when $k = 1$ and $n = 2$ ， after allowing for the change to the range of the variable.

16.5 By following the method of proof of Theorem 3.2,obtain from condition （16.49）a bound on $d _ { n } ^ { * } ( g )$ that is stronger than inequality (16.5O),and that is valid when $n = k - 1$ .Deduce from Theorems 4.2 and 7.3 that the least number $c ( n )$ that satisfies the inequality

$$
d _ { n } ^ { * } \left( g \right) \leqslant c \left( n \right) \| g ^ { ( n + 1 ) } \| _ { \infty } , \qquad g \in \mathcal { C } ^ { ( n + 1 ) } [ - 1 , 1 ] ,
$$

has the value $c ( n ) = 1 / 2 ^ { n } ( n + 1 ) !$

16.6 By showing that the function $\{ p ( x ) = \sin { ( n x ) } / { n } ; - \infty < x < \infty \}$ is the element of ${ \mathcal { Q } } _ { n }$ whose minimax norm is least subject to the condition $p ^ { \prime } ( 0 ) = 1$ ， prove that the inequality $\| p ^ { ( k ) } \| _ { \infty } \leqslant n ^ { k } \| p \| _ { \infty }$ holds for all trigonometric polynomials $p$ in $\mathcal { Q } _ { n }$

16.7 Let $f$ be a function in $\mathcal { C } _ { 2 \pi }$ that has the form $\{ f ( x ) = | x | ^ { \frac { 1 } { 2 } } \}$ in a neighbourhood of the origin. Deduce from Exercise 16.6 that $E _ { n } ( f )$ is bounded below by a multiple of $\left( n ^ { 2 } \| f \| _ { \infty } \right) ^ { - 1 / 3 }$ . Compare the bound that is given by Theorem 16.2.

16.8 Theorem 16.4 shows that the constant $c _ { 2 } ( n )$ of Exercise 16.2 may be given the value $[ { \pmb \pi } / ( 2 n + 2 ) ] ^ { 2 }$ . Deduce from the proofs of Theorems 15.1 and 16.4 that smaller values of $c _ { 2 } ( n )$ exist, giving attention to the conditions on $f ^ { \prime }$ that make $E _ { n } ( f ^ { \prime } )$ close to $[ { \pi } / { ( 2 n + 2 ) } ] \| f ^ { \prime \prime } \| _ { \infty }$

16.9Prove that the inequality

$$
E _ { n } ( f ) \leqslant { \biggl [ } 1 + { \frac { ( 2 n + 2 ) ^ { 2 } c _ { 2 } ( n ) } { 2 \pi ^ { 2 } } } { \biggr ] } \omega { \biggl ( } { \frac { \pi } { n + 1 } } { \biggr ) }
$$

is satisfied, for all functions $f$ in $\mathcal { C } _ { 2 \pi }$ where $c _ { 2 } ( n )$ is the constant of Exercise 16.2.A suitable method is to replace $\phi$ in the proof of Theorem 16.2 by the function

$$
\phi ( x ) = \int _ { - \delta } ^ { \delta } f ( x + \theta ) ( \delta - | \theta | ) { \mathrm d } \theta / \delta ^ { 2 } , \qquad - \infty < x < \infty .
$$

Hence Exercise 16.8 implies that the constant $\frac { 3 } { 2 }$ in the statement of Theorem 16.2 is not optimal.

16.10By considering a case when the best minimax approximation in $\mathcal { P } _ { 2 }$ to a function $\pmb { g }$ in $\mathcal { C } [ - 1 , 1 ]$ is the zero function, show that, if $^ { c }$ is a constant that satisfies the condition

$$
d _ { n } ^ { * } ( g ) \leqslant c \| g ^ { \prime } \| _ { \infty } , \qquad g \in { \mathcal { C } } ^ { ( 1 ) } [ - 1 , 1 ] ,
$$

then $c$ is not less than $\textstyle { \frac { 1 } { 3 } }$ .Further,by considering a case when the best approximation is a straight line, show that the lower bound on $^ { c }$ can be increased to $( 6 - 4 \sqrt { 2 } )$