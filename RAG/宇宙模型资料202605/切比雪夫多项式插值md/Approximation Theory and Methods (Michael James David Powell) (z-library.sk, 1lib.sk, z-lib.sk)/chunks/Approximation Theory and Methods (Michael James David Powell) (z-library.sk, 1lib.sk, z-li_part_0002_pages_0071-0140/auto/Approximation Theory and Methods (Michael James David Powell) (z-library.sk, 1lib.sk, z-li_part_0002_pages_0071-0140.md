1, 2, 3, 4, and let $f$ have the values $f ( 0 ) = 0$ ， $f ( 1 ) = 1$ ， $f ( 2 ) = 3$ ， $f ( 3 ) = 4$ and $f ( 4 ) = 4$ .First calculate the polynomials $\{ r ( j , 2 , 0 , x )$ ， $0 \leqslant x \leqslant 4$ ； $j = 0 , 1 , 2 \}$ ,and then obtain the rational function $\{ r ( 0 , 2 , 2 , x ) ; 0 \leqslant x \leqslant 4 \}$ that interpolates the data by applying the given extension of equation (5.15) three times.

# The uniform convergence of polynomial approximations

# 6.1 The Weierstrass theorem

In Chapter 4 the approximation of the function

$$
f ( x ) = 1 / ( 1 + x ^ { 2 } ) , \qquad - 5 \leqslant x \leqslant 5 ,
$$

by polynomials of various degrees was considered. Each polynomial was calculated by Lagrange interpolation,and we found that, for equally spaced interpolation points,increasing the degree of the polynomial makes the accuracy of the approximation worse. For the Chebyshev interpolation points,however, Table 4.4 suggests that the calculated polynomial approximations converge uniformly to the function (6.1). It is interesting to ask whether there are functions in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that are so awkward that, even if Chebyshev interpolation points are used, the Lagrange interpolation method for polynomials of higher and higher degree gives a sequence of approximations that fails to converge uniformly. It is proved in Chapter 17 that such awkward functions do exist.

Suppose，however， that instead of defining each polynomial by Lagrange interpolation,we use some other method of calculation.Can we then generate a sequence of polynomial approximations to any function $f \in \mathcal { C } [ a , b ]$ such that uniform convergence is obtained. It is shown in Section 6.3 that the Bernstein approximation method is suit-able. Hence we obtain a constructive proof of the following well-known theorem.

# Theorem 6.1 (Weierstrass)

For any $f \in \mathcal { C } [ a , b ]$ and for any $\pmb \varepsilon > 0$ ,there exists an algebraic polynomial of the form

$$
p ( x ) = c _ { 0 } + c _ { 1 } x + . . . + c _ { n } x ^ { n } , \qquad a \leqslant x \leqslant b ,
$$

such that the bound

$$
\| f - p \| _ { \infty } \leqslant \varepsilon
$$

is satisfied.

Proof. The work of the next two sections provides a proof of this theorem.□

# 6.2 Monotone operators

Our method of proof of Theorem 6.1 depends on an interesting and remarkable property of monotone operators,which is explained in this section. The operator $\pmb { L }$ from $\mathcal { C } [ a , b ]$ to $\mathcal { C } [ a , b ]$ is defined to be monotone if it satisfies the following condition. Let $f$ and $\pmb { g }$ be any two functions in $\mathcal { C } [ a , b ]$ ， such that the inequality

$$
f ( x ) \geqslant g ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is obtained. Then the functions $L f$ and $L g$ must satisfy the condition

$$
( L f ) ( x ) \geqslant ( L g ) ( x ) , \qquad a \leqslant x \leqslant b .
$$

We note that, if $L$ is a linear operator, then the monotonicity condition is equivalent to the following simpler form. For allnon-negative functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ ,the function $L f$ must be non-negative also.

Monotone operators are useful to us because,given an infinite sequence of linear monotone operators, $\{ L _ { i } ; i = 0 , 1 , 2 , \ldots \}$ say, each one being from ${ \mathcal { C } } [ a , b ]$ to $\mathcal { C } [ a , b ] .$ ，there is a very simple test to discover whether or not the sequence of functions $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges uniformly to $f$ for all $f$ in $\mathcal { C } [ a , b ]$ .This test is the subject of our next theorem,and it is applied in Section 6.3 to the Bernstein operators in order to establish the Weierstrass theorem.

# Theorem 6.2

Let $\{ L _ { i } ; i = 0 , 1 , 2 , \ldots \}$ be a sequence of linear monotone operators from $\mathcal { C } [ a , b ]$ to $\mathcal { C } [ a , b ]$ .Then, if the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges uniformly to $f$ for the functions

$$
f ( x ) = x ^ { k } , \qquad a \leqslant x \leqslant b ,
$$

where $\dot { k } = 0$ ，1 or 2, then the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , . . . \}$ convergesuniformly to $f$ for all $f$ in $\mathcal { C } [ a , b ]$

Proof. The method of proof of the theorem is indicated in Figure 6.1. We let $\pmb { \xi }$ be any fixed point of $[ a , b ] ,$ we let $\pmb { q _ { \mathrm { \pmb { u } } } }$ be a quadratic function that is wholly above $f ,$ and we let $\pmb q _ { 1 }$ be a quadratic function that is wholly below $f ,$ where these functions are such that the difference $ { \boldsymbol { q } } _ { \mathrm { u } } ( \pmb { \xi } ) -  { \boldsymbol { q } } _ { \mathrm { l } } ( \pmb { \xi } )$ is small. The operator $L _ { n }$ is applied to the functions $q _ { \mathrm { u } } , f$ and $\pmb { q } _ { 1 }$ . Because, by hypothesis,the sequence $\{ L _ { i } f ; i = 0 , 1 , 2 , \ldots \}$ converges to $f$ when $f$ is a quadratic function, we can ensure that $L _ { n } q _ { \mathrm { { u } } }$ and $L _ { n } q _ { 1 }$ are very close to $\pmb { q _ { \mathrm { u } } }$ and $\pmb q _ { 1 }$ respectively by choosing a large value of $\pmb { n }$ .Moreover，the monotonicity of the operator $L _ { n }$ ensures that the function $L _ { n } f$ is bounded below by $L _ { n } q _ { 1 }$ and is bounded above by $L _ { n } q _ { \mathrm { { u } } }$ . Hence $( L _ { n } f ) ( \xi )$ must be close to $f ( \xi )$ . Thus the limit

$$
\operatorname* { l i m } _ { n  \infty } ( L _ { n } f ) ( \xi ) = f ( \xi )
$$

is proved for any fixed $\pmb { \xi }$ in $[ a , b ]$ . The details of the method of proof of equation (6.7), which are given below,establish the uniform convergence condition

$$
\operatorname* { l i m } _ { n \to \infty } \| f - L _ { n } f \| _ { \infty } = 0 ,
$$

which is stronger than the pointwise result (6.7).

Given $f \in { \mathcal { C } } [ a , b ] ,$ we let $\pmb \varepsilon$ be any positive number,and we choose $\pmb { \delta } > 0$ such that, if $\left| x _ { 1 } - x _ { 2 } \right| \leqslant \delta _ { \cdot }$ ，then the bound

$$
\left| f ( x _ { 1 } ) - f ( x _ { 2 } ) \right| \leqslant \varepsilon ,
$$

is obtained. Next we let $\pmb { \xi }$ be any fixed point of $[ a , b ] ,$ , and we note that $\pmb { \delta }$ is

![](images/8c4cb92aa8c3e1115d3f8c80a848755c314dc67ff3630f1dc4c8072250fe062a.jpg)  
Figure 6.1. The proof of the monotone operator theorem.

independent of $\xi .$ The quadratic functions $\pmb q _ { \mathbf { u } }$ and $\pmb { q } _ { 1 }$ are defined by the equations

$$
\begin{array} { r l } & { q _ { \mathbf { u } } ( x ) = f ( \xi ) + \varepsilon + 2 \| f \| _ { \infty } ( x - \xi ) ^ { 2 } / \delta ^ { 2 } \big ] , \quad a \leqslant x \leqslant b . } \\ & { \ q _ { 1 } ( x ) = f ( \xi ) - \varepsilon - 2 \| f \| _ { \infty } ( x - \xi ) ^ { 2 } / \delta ^ { 2 } \big \} , } \end{array}
$$

It follows from condition (6.9) that the inequality

$$
q _ { \mathrm { u } } ( x ) { \geq } f ( x )
$$

holds when $\vert x - \xi \vert \leqslant \delta$ ，Moreover, this inequality is also obtained when $| x - \xi | > \delta$ because of the definition of $\| f \| _ { \infty }$ . Similarly the condition

$$
q _ { 1 } ( x ) \leqslant f ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is satisfied also. Therefore the monotonicity of the operators gives the bounds

$$
( L _ { n } q _ { 1 } ) ( x ) \leqslant ( L _ { n } f ) ( x ) \leqslant ( L _ { n } q _ { \mathsf { u } } ) ( x ) , \qquad a \leqslant x \leqslant b ,
$$

for all non-negative integers $\pmb { n }$

In order to ensure that $\pmb { n }$ is large enough to prove the theorem, we express the functions $\pmb { q _ { \mathrm { u } } }$ and $\pmb q _ { 1 }$ as linear combinations of the polynomials ${ p } _ { 0 } , { p } _ { 1 }$ and $_ { p _ { 2 } }$ ,which are defined by the equation

$$
p _ { k } ( x ) = x ^ { k } , \qquad a \leqslant x \leqslant b .
$$

The definitions (6.10) give expressions of the form

$$
\begin{array} { r } { q _ { \mathbf { u } } = c _ { 0 } ( \pmb { \xi } ) p _ { 0 } + c _ { 1 } ( \pmb { \xi } ) p _ { 1 } + c _ { 2 } ( \pmb { \xi } ) p _ { 2 } } \\ { q _ { 1 } = c _ { 3 } ( \pmb { \xi } ) p _ { 0 } + c _ { 4 } ( \pmb { \xi } ) p _ { 1 } + c _ { 5 } ( \pmb { \xi } ) p _ { 2 } \} , } \end{array}
$$

and there exists a number $M ,$ that depends on $\delta , \varepsilon$ and $f$ but not on $\xi ,$ such that the bounds

$$
\left| c _ { i } ( \xi ) \right| \leqslant M , \qquad i = 0 , 1 , \ldots , 5 ,
$$

are obtained. By hypothesis, we can let $\pmb { N }$ be an integer such that the conditions

$$
\begin{array} { r } { \| p _ { k } - L _ { n } p _ { k } \| _ { \infty } \leqslant \varepsilon / M , \qquad k = 0 , 1 , 2 , } \end{array}
$$

hold for all $\begin{array} { r } { n \geqslant N . } \end{array}$ It is important to note that $\pmb { N }$ is also independent of $\xi .$ Inequality (6.17) is useful to us because,by combining it with expressions (6.15) and (6.16),and by using both the linearity of the operator $L _ { n }$ and the triangle inequality for norms,we deduce the bounds

$$
\begin{array} { c } { \| q _ { \mathrm { u } } - L _ { n } q _ { \mathrm { u } } \| _ { \infty } \leqslant 3 \varepsilon } \\ { \| q _ { \mathrm { l } } - L _ { n } q _ { \mathrm { l } } \| _ { \infty } \leqslant 3 \varepsilon } \end{array} \biggr \} .
$$

Expressions (6.13),(6.18) and (6.10) are applied in sequence to give the bound

$$
\begin{array} { r } { ( L _ { n } f ) ( \xi ) \leqslant ( L _ { n } q _ { \mathrm { u } } ) ( \xi ) } \\ { \leqslant q _ { \mathrm { u } } ( \xi ) + 3 \varepsilon } \\ { = f ( \xi ) + 4 \varepsilon . } \end{array}
$$

Similarly, by making use of $\pmb q _ { 1 }$ instead of $\pmb { q _ { \mathrm { u } } }$ , we deduce the inequality

$$
( L _ { n } f ) ( \xi ) \geqslant f ( \xi ) - 4 \varepsilon .
$$

We write expressions (6.19) and (6.20) in the form

$$
\left| f ( \xi ) - ( L _ { n } f ) ( \xi ) \right| \leqslant 4 \varepsilon , \qquad n \geqslant N .
$$

Because $\pmb { N }$ and $\pmb \varepsilon$ are independent of $\xi ,$ it follows that the stronger condition

$$
\| f - L _ { n } f \| _ { \infty } \leqslant 4 \varepsilon , \qquad n \geqslant N ,
$$

also holds. We recall that our proof has established the existence of $\pmb { N }$ for any positive $\pmb \varepsilon$ . Therefore the required limit (6.8) is obtained for any $f$ in $\mathcal { C } [ \alpha , b ]$ □

# 6.3 The Bernstein operator

The Bernstein operator $B _ { n }$ is from ${ \mathcal { C } } [ a , b ]$ to the subspace $\mathcal { P } _ { n }$ of polynomials of degree $\pmb { n }$ ,and it is defined for all positive integral values of $\pmb { n }$ . In the case when the range $[ a , b ]$ is the interval[0,1], it is specified by the equation

$$
( B _ { n } f ) ( x ) = \sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } f ( k / n ) , \qquad 0 \leqslant x \leqslant 1 .
$$

In order to simplify notation, we assume for the rest of this chapter that the range of the variable is $0 \leqslant x \leqslant 1$ .

The Bernstein approximation (6.23) is similar to the Lagrange polynomial approximation (4.7) in two ways. Both approximation operators are linear,and in both cases the polynomial approximation that is chosen from $\mathcal { P } _ { n }$ depends just on the value of $f$ at $( n + 1 )$ discrete points of $[ a , b ]$

However, unlike Lagrange interpolation, the approximation $B _ { n } f$ may not equal $f$ when $f$ is in ${ \mathcal P } _ { n }$ .For example, suppose that $f$ is the polynomial in $\mathcal { P } _ { n }$ that takes the value one at $x = k / n$ and that is zero at the points $\{ x = j / n ; j = 0 , 1 , \ldots , n ; j \neq k \}$ Then $( B _ { n } f ) ( x )$ is a multiple of $x ^ { k } ( 1 -$ $\pmb { x } ) ^ { n - k }$ ，which is positive at thepoints $\{ x = j / n ; j = 1 , 2 , . . . , n - 1 \}$ The main advantage of Bernstein approximation over Lagrange interpolation is given in the next theorem.

# Theorem 6.3

For all functions $f$ in $\mathcal { C } [ 0 , 1 ] ,$ , the sequence $\{ B _ { n } f ; n = 1 , 2 , 3 , . . . \}$ converges uniformly to $f ,$ where $B _ { n }$ is defined by equation (6.23).

Proof. The definition (6.23) shows that $B _ { n }$ is a linear operator. It shows also that, if $f ( x )$ is non-negative for $0 \leqslant x \leqslant 1$ ， then $( B _ { n } f ) ( x )$ is nonnegative for $0 \leqslant x \leqslant 1$ . Hence $B _ { n }$ is both linear and monotone. It follows from Theorem 6.2 that we need only establish that the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| B _ { n } f - f \| _ { \infty } = 0
$$

is obtained when $f$ is a quadratic polynomial. Therefor, for $j = 0 , 1 , 2$ ， we consider the error of the Bernstein approximation to the function

$$
f ( x ) = x ^ { j } , \qquad 0 \leqslant x \leqslant 1 .
$$

For $j = 0$ ，we find for all $_ n$ that $B _ { n } f$ is equal to $f$ by the binomial theorem. When $j = 1$ , the definition of $B _ { n }$ gives the equation

$$
\begin{array} { l } { ( B _ { n } f ) ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \frac k n } \\ { = \displaystyle \sum _ { k = 1 } ^ { n } \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } } \\ { = x \displaystyle \sum _ { k = 0 } ^ { n - 1 } \frac { ( n - 1 ) ! } { k ! ( n - 1 - k ) ! } x ^ { k } ( 1 - x ) ^ { n - 1 - k } . } \end{array}
$$

Hence again $B _ { n } f$ is equal to $f$ by the binomial theorem. To continue the proof we make use of the identity

$$
\sum _ { k = 0 } ^ { n } { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } { \bigg ( } { \frac { k } { n } } { \bigg ) } ^ { 2 } = { \frac { n - 1 } { n } } x ^ { 2 } + { \frac { 1 } { n } } x ,
$$

which is straightforward to establish. For the case when $j = 2$ in equation (6.25), it gives the value

$$
\| B _ { n } f - f \| _ { \infty } = \operatorname* { m a x } _ { 0 \leqslant x \leqslant 1 } \left| { \frac { n - 1 } { n } } x ^ { 2 } + { \frac { 1 } { n } } x - x ^ { 2 } \right| = { \frac { 1 } { 4 n } } ,
$$

and it is important to note that the right-hand side tends to zero as $_ n$ tends to infinity. Hence the limit (6.24) is achieved for all $f \in \mathcal { P } _ { 2 }$ ，which completes the proof of the theorem.□

It follows from this theorem that,for any $f \in \mathcal { C } [ 0 , 1 ]$ and for any $\pmb \varepsilon > 0$ ， there exists $_ n$ such that the inequality

$$
\| f - B _ { n } f \| _ { \infty } \leqslant \varepsilon
$$

holds.Hence condition (6.3） can be satisfied by letting $\begin{array} { r } { p = B _ { n } f , } \end{array}$ which proves the Weierstrass theorem in the case when $[ a , b ]$ is [0, 1].

The general case,when $[ a , b ]$ may be different from [0,1],does not introduce any extra difficulties if one thinks geometrically. Imagine a function $f$ from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，that we wish to approximate to accuracy $\pmb \varepsilon$ ， plotted on graph paper. We may redefine the units on the $\pmb { x }$ -axis by a linear transformation, so that the range of interest becomes [O, 1],and we leave the plotted graph of $f$ unchanged. We apply the Bernstein operator (6.23) to the plotted function of the new variable,choosing $\pmb { n }$ to be so large that the approximation is accurate to $\pmb \varepsilon$ .We then draw the graph of the calculated approximation, and we must find that no error in the $\boldsymbol { y }$ -direction exceeds $\pmb \varepsilon$ . There are now two plotted curves. We leave them unchanged and revert to the original labelling on the $\pmb { x }$ -axis. Hence we find an approximating function that completes the proof of Theorem 3.1.

The Bernstein operator is seldom applied in practice, because the rate of convergence of $B _ { n } f$ to $f$ is usually too slow to be useful. For example, equation (6.28) shows that, in order to approximate the function $f ( x ) = x ^ { 2 }$ on [0,1] to accuracy $1 0 ^ { - 4 }$ , it is necessary to let $n = 2 5 0 0$ .However, equation (6.23) has an important application to automatic design. Here one takes advantage of the fact that the function values $\{ f ( k / n )$ ； $k =$ $0 , 1 , \ldots , n \}$ that occur on the right-hand side of the equation define $B _ { n } f$ Moreover, for any polynomial $p \in \mathcal { P } _ { n }$ ，there exist function values such that $B _ { n } f$ is equal to $p$ 、Hence the numbers $\{ f ( k / n ) ; k = 0 , 1 , . . . , n \}$ provide a parameterization of the elements of ${ \mathcal { P } } _ { n }$ .It is advantageous in design to try different polynomials by altering these parameters, because the changes to $B _ { n } f$ that occur when the parameters are adjusted separately are smooth peaked functions that one can easily become accustomed to in interactive computing.

# 6.4 The derivatives of the Bernstein approximations

The Bernstein operator possesses another property which is as remarkable as the uniform convergence result that is given in Theorem 6.3. It is that, if $f$ is in $\mathcal { C } ^ { ( k ) } [ 0 , 1 ]$ , which means that $f$ has a continuous kth derivative, then, not only does $B _ { n } f$ converge uniformly to $f ,$ but also the derivatives of $B _ { n } f$ converge uniformly to the derivatives of $f ,$ for all orders of derivative up to and including $k$ . We prove this result in the case when $k = 1$ .

# Theorem 6.4

Let $f$ be a continuously differentiable function in $\mathcal { C } [ 0 , 1 ]$ .Then the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| f ^ { \prime } - ( B _ { n } f ) ^ { \prime } \| _ { \infty } = 0
$$

is obtained, where $B _ { n }$ is the Bernstein operator.

Proof. By applying Theorem 6.3 to the function $f ^ { \prime }$ ， we see that the sequence $\{ B _ { n } ( f ^ { \prime } ) ; n = 1 , 2 , 3 , . . . \}$ converges uniformly to $f ^ { \prime }$ . It is therefore sufficient to prove that the limit

$$
\operatorname* { l i m } _ { n  \infty } \| B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } \| _ { \infty } = 0
$$

is obtained. One of the subscripts is chosen to be $n + 1$ in order to help the algebra that follows.

Values of the function $( B _ { n + 1 } f ) ^ { \prime }$ can be found by differentiating the right-hand side of the definition (6.23). This is done below,and then the calculated expression is rearranged by using the divided difference nota-tion of Chapter 5,followed by an application of Theorem 5.1. Hence we obtain the equation

$$
\begin{array} { r l r } { ( B _ { n + 1 } f ) ^ { \prime } ( x ) = \displaystyle \sum _ { k = 0 } ^ { n + 1 } \frac { ( n + 1 ) ! } { ( k - 1 ) ! ( n + 1 - k ) ! } x ^ { k - 1 } ( 1 - x ) ^ { n + 1 - k } f \Bigl ( \frac { k } { n + 1 } \Bigr ) } \\ & { } & { \qquad - \displaystyle \sum _ { k = 0 } ^ { n } \frac { ( n + 1 ) ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl ( \frac { k } { n + 1 } \Bigr ) } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { n } \frac { ( n + 1 ) ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \Bigl \{ f \Bigl ( \frac { k + 1 } { n + 1 } \Bigr ) - f \Bigl ( \frac { k } { n + 1 } \Bigr ) \Bigr \} } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl [ \frac { k } { n + 1 } , \frac { k + 1 } { n + 1 } \Bigr ] } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f \Bigl [ \frac { k } { n + 1 } , \frac { k } { n + 1 } \Bigr ] } \\ & { } & { \qquad = \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } f ( \xi _ { k } ) , \qquad ( 6 . 3 ; } \end{array}
$$

where $\xi _ { k }$ is in the interval

$$
\frac { k } { n + 1 } \leqslant \xi _ { k } \leqslant \frac { k + 1 } { n + 1 } , \qquad k = 0 , 1 , \ldots , n .
$$

By using the definition (6.23) again, it follows that the modulus of the

value of the function $[ B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } ]$ at the point $x$ is bounded by the expression

$$
\begin{array} { r l r } & { } & { \bigg | \displaystyle \sum _ { k = 0 } ^ { n } \frac { n ! } { k ! ( n - k ) ! } x ^ { k } ( 1 - x ) ^ { n - k } \bigg [ f ^ { \prime } \Big ( \frac { k } { n } \Big ) - f ^ { \prime } ( \xi _ { k } ) \bigg ] \bigg | } \\ & { } & { \displaystyle \leqslant \operatorname* { m a x } _ { k = 0 , 1 , \dots , n } \bigg | f ^ { \prime } \Big ( \frac { k } { n } \Big ) - f ^ { \prime } ( \xi _ { k } ) \bigg | \leqslant \omega \Big ( \frac { 1 } { n + 1 } \Big ) , } \end{array}
$$

where $\pmb { \omega }$ is the modulus of continuity of the function $f ^ { \prime }$ . The last inequality is obtained from the fact that $k / n$ ,like $\xi _ { k }$ , is in the interval $[ k / ( n + 1 )$ ， $( k + 1 ) / ( n + 1 ) ]$ . Because this last inequality is independent of $\pmb { x }$ ,we have established the condition

$$
\| B _ { n } ( f ^ { \prime } ) - ( B _ { n + 1 } f ) ^ { \prime } \| _ { \infty } \leqslant \omega \Big ( \frac { 1 } { n + 1 } \Big ) .
$$

Therefore the limit (6.31) is proved.□

It is worth noting that the middle line of equation (6.32) implies that, if the function $f$ increases strictly monotonically, then the polynomial $B _ { n + 1 } f$ also increases strictly monotonically. The Bernstein method is excellent for providing a polynomial approximation that preserves any smooth qualitative properties of the function that is being approximated. It is also useful for obtaining a differentiable approximation to a non-differentiable function, and for some other smoothing applications.

# 6 Exercises

6.1 For any $f \in \mathcal { C } [ a , b ]$ ,let $X f$ be the linear polynomial that inter-polates $f ( x _ { 0 } )$ and $f ( x _ { 1 } )$ ,where $x _ { 0 }$ and $\pmb { x } _ { 1 }$ are fixed points of $[ a , b ]$ such that $\pmb { x } _ { 0 } < \pmb { x } _ { 1 }$ . Prove that the operator $\pmb { X }$ is monotone if and only if $\scriptstyle x _ { 0 } = a$ and $x _ { 1 } = b$

6.2 By using the identity

$$
k ^ { 2 } = ( k - 1 ) ( k - 2 ) + 3 ( k - 1 ) + 1 ,
$$

prove that the Bernstein approximation to the function $\{ f ( { \pmb x } ) =$ $x ^ { 3 } ; 0 \leqslant x \leqslant 1 \}$ is the polynomial

$$
p ( x ) = { \frac { ( n - 1 ) ( n - 2 ) } { n ^ { 2 } } } x ^ { 3 } + { \frac { 3 ( n - 1 ) } { n ^ { 2 } } } x ^ { 2 } + { \frac { 1 } { n ^ { 2 } } } x , \qquad 0 \leqslant x \leqslant 1 .
$$

Note that the method of calculation can be generalized to show that, if $f \in \mathcal P _ { r }$ and if $n > r ,$ ,then the approximation $B _ { n } f$ is also in $\mathcal { P } _ { r }$

6.3 Let ${ \pmb p } = { \pmb B } _ { 6 } f ,$ where $B _ { n } f$ is the Bernstein approximation (6.23) to a function $f$ in $\mathcal { C } [ 0 , 1 ]$ .Express the function values $\{ p ( j / 6 ) ; j =$ $0 , 1 , \ldots , 6 \}$ as linear combinations of the numbers $\{ f ( j / 6 )$ ；

$j = 0 , 1 , \ldots , 6 \}$ .Hence show that, if $p$ is the polynomial in ${ \mathcal { P } } _ { 6 }$ that satisfies the conditions $p ( { \frac { 1 } { 2 } } ) = 1$ and $\{ p ( j / 6 ) = 0$ ； $j = 0$ ,1,2,4,5, $6 \}$ ，then $f$ takes the values $f ( 0 ) = f ( 1 ) = 0 .$ $\textstyle f ( { \frac { 1 } { 6 } } ) = f ( { \frac { 5 } { 6 } } ) = 2 0 / 3$ ， $f ( \scriptstyle { \frac { 1 } { 3 } } ) = f ( \frac { 2 } { 3 } ) = - 3 0 8 / 1 5$ and $f ( \scriptstyle { \frac { 1 } { 2 } } ) = 3 0$

6.4 Let $\pmb { n }$ and $\boldsymbol { r }$ be positive integers, where $n \geqslant r ,$ let $f$ be a function in $\mathcal { C } ^ { ( r ) } [ 0 , 1 ] ,$ and let $p _ { n } = B _ { n } f$ be the Bernstein polynomial (6.23). By expressing the derivative $p _ { n } ^ { ( r ) } ( 0 )$ as a linear combination of the function values $\{ f ( k / n ) ; k = 0 , 1 , \ldots , r \}$ ,prove that the equation

$$
p _ { n } ^ { ( r ) } ( 0 ) = \frac { n ! } { n ^ { r } ( n - r ) ! } f ^ { ( r ) } ( \xi )
$$

is satisfied, where $\xi$ is in the interval $[ 0 , r / n ]$ .Deduce that $\smash { p _ { n } ^ { ( r ) } }$ （0） tends to $f ^ { ( r ) } ( 0 )$ as $_ n$ tends to infinity.

Prove that the error at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ of the Bernstein approximation $B _ { n } f$ to the function $\{ f ( x ) = | x - { \frac { 1 } { 2 } } |$ ； $0 \leqslant x \leqslant 1 \}$ is of order of magnitude $n ^ { - \frac { 1 } { 2 } }$

6.6 Consider the function

$$
\phi _ { n k } ( x ) = { \frac { n ! } { k ! ( n - k ) ! } } x ^ { k } ( 1 - x ) ^ { n - k } , \qquad 0 \leqslant x \leqslant 1 ,
$$

that occurs in the definition of the approximation (6.23). Investigate its properties, giving particular attention to the case when $_ n$ is large.You should find that $\phi _ { n k }$ has one peak at $x = k / n$ ， and that the width of the peak becomes narrower as $\pmb { n }$ tends to infinity. Let $\xi$ and $\pmb { \eta }$ be any two fixed points of [O,1], where $\xi$ is rational, and let the ratio $\phi _ { n k } ( \eta ) / \phi _ { n k } ( \xi )$ be calculated for an infinite sequence of pairs $( k , n )$ such that $\xi = k / n$ .Prove that the ratio tends to zero.

6.7 Let $L _ { n }$ be a linear monotone operator from $\mathcal { C } [ 0 , 1 ]$ to $\mathcal { C } [ 0 , 1 ] ,$ ， where $L _ { n } f$ depends only on the function values $\{ f ( k / n )$ ； $k =$ $0 , 1 , \ldots , n \}$ ,and let $L _ { n }$ have the property that, if $f \in { \mathcal { C } } ^ { ( 2 ) } [ 0 , 1 ] ,$ then the bound

$$
\| f - L _ { n } f \| _ { \infty } \leqslant c \| f ^ { \prime \prime } \| _ { \infty }
$$

is satisfied, where the number $c$ is independent of $f .$ By consider-ing a quadratic function that is positive on most of the range [0,1], show that $c$ is not less than $1 / 8 n ^ { 2 }$ .Further, show that the value $c = 1 / 8 n ^ { 2 }$ can be achieved by letting $L _ { n } f$ be a piecewise linear function.

6.8 By applying the technique that is used to prove Theorem 6.2, show that, if $f \in { \mathcal { C } } ^ { ( 2 ) } [ 0 , 1 ] ,$ , then the error of the approximation (6.23) satisfies the bound

$$
\| f - B _ { n } f \| _ { \infty } \leqslant [ 1 / 8 n ] \| f ^ { \prime \prime } \| _ { \infty } .
$$

Note that this bound holds as an equation when $f$ is the function $\{ f ( x ) = x ^ { 2 } ; 0 \leqslant x \leqslant 1 \} .$

9 By extending the proof of Theorem 6.4 show that, if $f \in$ $\mathcal { C } ^ { ( 2 ) } [ 0 , 1 ] ,$ ， then the limit

$$
\operatorname* { l i m } _ { n \to \infty } \| f ^ { \prime \prime } - ( B _ { n } f ) ^ { \prime \prime } \| _ { \infty } = 0
$$

is obtained.

6.10 Let $\{ f ( x , y ) ; 0 \leqslant x \leqslant 1 ; 0 \leqslant y \leqslant 1 \}$ be a continuous function of two variables,and let the function $B _ { n } f$ be obtained by applying the Bernstein approximation method to each of the variables of $f .$ Therefore $( B _ { n } f ) ( x , y )$ has the value

$$
\sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } { \frac { ( n ! ) ^ { 2 } } { j ! ( n - j ) ! k ! ( n - k ) ! } } x ^ { j } ( 1 - x ) ^ { n - j } y ^ { k } ( 1 - y ) ^ { n - k } f { \biggl ( } { \frac { j } { n } } , { \frac { k } { n } } { \biggr ) } ,
$$

where $0 \leqslant x \leqslant 1$ and $0 \leqslant y \leqslant 1$ . Prove that the infinite sequence $\{ B _ { n } f ; n = 0 , 1 , 2 , . . . \}$ converges uniformly to $f .$

# 7

# The theory of minimax approximation

# 7.1 Introduction to minimax approximation

We recall from Chapter 1 that the best minimax approximation from a set $\mathcal { A }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is the element of $\mathscr { A }$ that minimizes the expression

$$
\| f - p \| _ { \infty } = \operatorname* { m a x } _ { a \leqslant x \leqslant b } { \big | } f ( x ) - p ( x ) { \big | } , \qquad p \in { \mathcal { A } } .
$$

In this chapter we study the conditions that are satisfied by a best approximation， when $\mathscr { A }$ is a linear space. We note that they take a particularly simple form if $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ of algebraic polynomials of degree at most $_ n$ . In fact this form is obtained in the more general case when $\mathscr { A }$ satisfies the‘Haar condition',which is defined in Section 7.3.In Section 7.4 some further useful properties of best minimax approximations are proved in the case when the Haar condition is obtained, including the result that the best approximation is unique. The Haar condition also provides an excellent method for calculating best approximations,called the exchange algorithm, which is described in Chapter 8 and analysed in Chapter 9.

The theory that is developed for the case when $\mathscr { A }$ is any finitedimensional linear space comes from asking the following question. Let $p ^ { * }$ be a trial approximation from $\mathcal { A }$ to $f .$ Can we find a change to $p ^ { * }$ that reduces the maximum error of the trial approximation? In other words, we seek an element $p$ in $\mathcal { A }$ such that the inequality

$$
\| f - ( p ^ { * } + \theta p ) \| _ { \infty } < \| f - p ^ { * } \| _ { \infty }
$$

is satisfied for some value of the scalar parameter $\pmb \theta$ .Figure 7.1 gives an example to explain this point of view.

In the figure the function $f ,$ which is shown in each of the four parts, is to be approximated by a straight line,so $\mathcal { A }$ is the space $\mathcal { P } _ { 1 }$ . Three trial approximaticns,namely $p _ { 1 } ^ { * } , p _ { 2 } ^ { * }$ and $\pmb { p } _ { 3 } ^ { * }$ , are shown. The vertical lines in the figure indicate where the error function of each approximation takes its maximum value. We see that the straight line $p _ { 1 } ^ { * }$ is not optimal, because the maximum error is reduced if the line is raised. The straight line $\pmb { p } _ { 2 } ^ { * }$ is not optimal either, because the maximum error can be reduced by rotating the line in a counter-clockwise direction. The straight line $\pmb { p } _ { 3 } ^ { * }$ ， however, is the best approximation from $\mathcal { P } _ { 1 }$ to $f .$ We find in Section 7.3 that the characteristic property of a best straight line approximation is that the maximum error is achieved at three points of $[ a , b ]$ with alternating sign.

![](images/e8705c55ae5be159ffc0b5ae19e8b58bb26dfe47637ac706b6e15d1d8fef3adf.jpg)  
Figure 7.1. Minimax approximation by a straight line.

Figure 7.1 suggests that, to discover if a trial approximation is optimal, one only need consider the extreme values of the error function $\{ f ( x ) -$ $p ^ { * } ( x )$ ； $a \leqslant x \leqslant b \}$ . This remark is made rigorous in the next section. It follows that we can find a function, $\pmb { g }$ say, to add to the function of Figure 7.1,such that the best approximation is unchanged,but the best approximation from $\mathcal { P } _ { 1 }$ to $\pmb { g }$ is not the zero function. This remark is important, because it shows that in general a best minimax operator from $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ to $\mathcal { A }$ is not a linear operator. Therefore the algorithms for calculating best approximations are iterative procedures.

# 7.2 The reduction of the error of a trial approximation

We let $p ^ { * }$ be a trial approximation from $\mathcal { A }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ , and we try to improve the approximation by satisfying condition (7.2). The set of points at which the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

takes its extreme values is important, and we call it $\mathcal { Z } _ { \mathbf { M } }$ This set is characterized by the condition

$$
\begin{array} { r } { \big | e ^ { * } ( x ) \big | = \big \| e ^ { * } \big \| _ { \infty } , \qquad x \in \mathcal { Z } _ { \bf M } . } \end{array}
$$

We suppose first that $p ^ { * }$ is not optimal. We let $( p ^ { * } + \theta p )$ be a best approximation. Hence the reduction (7.2) is obtained, and the points in $\mathcal { Z } _ { \mathbf { M } }$ satisfy the inequality

$$
| e ^ { * } ( x ) - \theta p ( x ) | < | e ^ { * } ( x ) | , \qquad x \in \mathcal { Z } _ { \mathsf { M } } .
$$

We assume without loss of generality that $\pmb \theta$ is positive.Therefore expression (7.5) shows that, if $\pmb { x }$ is in $\mathcal { L } _ { \mathbf { M } } .$ ,then the sign of $e ^ { * } ( x )$ is the same as the sign of $p ( { \pmb x } )$ . It follows that $p ^ { * }$ is a best minimax approximation from $\mathscr { A }$ to $f$ if there is no function $p$ in $\mathscr { A }$ that satisfies the condition

$$
[ f ( x ) - p ^ { * } ( x ) ] p ( x ) > 0 , \qquad x \in \mathcal { Z } _ { \bf M } .
$$

In the remainder of this section the converse result is proved, namely that, if inequality (7.6) holds for some $p$ in $\scriptstyle { \mathcal { A } }$ , then there exists a positive value of $\pmb \theta$ that gives the reduction (7.2).

Because of the way in which the exchange algorithm works，we generalize the problem of minimizing $\| f - p \| _ { \infty } ,$ ，to the problem of

minimizing the expression

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } | f ( x ) - p ( x ) | , \qquad p \in \mathcal { A } ,
$$

where $\mathcal { Z }$ is any closed subset of $[ a , b ]$ , which may be $[ a , b ]$ itself, but in the exchange algorithm the set $\mathcal { X }$ is composed of a finite number of points. The next theorem allows $\mathcal { Z }$ to be general.

# Theorem 7.1

Let $\mathscr { A }$ be a linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ let $f$ be any function in $\mathcal { C } [ a , b ] ,$ let $\mathcal { Z }$ be any closed subset of $[ a , b ]$ let $p ^ { * }$ be any element of $\scriptstyle { \mathcal { A } } ,$ ， and let $\mathcal { Z } _ { \mathbf { M } }$ be the set of points of $\mathcal { Z }$ at which the error $\{ | f ( x ) - p ^ { * } ( x ) |$ ； $x \in$ $\mathcal { Z } \}$ takes its maximum value.Then $p ^ { * }$ is an element of $\mathscr { A }$ that minimizes expression (7.7) if and only if there is no function $p$ in $\pmb { \mathcal { A } }$ that satisfies condition (7.6).

Proof. The remarks made in the first paragraph of this section prove the ‘if’ part of the theorem，when $\mathcal { Z }$ is the whole interval $[ a , b ]$ It is straightforward to extend these remarks to the case when $\mathcal { Z }$ is a subset of $[ a , b ]$ .Therefore, it remains to show that, if condition (7.6) is obtained, then the inequality

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| < \operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) \right|
$$

holds for some value of $\pmb \theta _ { : }$ ，where $e ^ { * }$ is the error function (7.3).

We let $\pmb \theta$ be positive,and we must ensure that it is not too large.For example, if we improve the approximation $p _ { 1 } ^ { * }$ in Figure 7.1 by raising the straight line approximation, then we must be careful not to raise it too far. In order to avoid detailed consideration of the size of $p$ when we find a suitable value of $\pmb \theta$ , we assume without loss of generality that the condition

$$
| p ( x ) | \leqslant 1 , \qquad a \leqslant x \leqslant b ,
$$

holds. We have to give particular care to any values of $\pmb { x }$ for which the signs of $e ^ { * } ( x )$ and $p ( x )$ are opposite. Therefore the set $\mathcal { Z } _ { 0 }$ is defined to contain the elements $\pmb { x }$ that satisfy the condition

$$
p ( x ) e ^ { * } ( x ) \leqslant 0 , \qquad x \in { \mathcal { Z } } .
$$

Because this set is closed, and because $\mathcal { Z } _ { 0 }$ and $\mathcal { Z } _ { \mathbf { M } }$ have no points in common, the number

$$
d = \operatorname* { m a x } _ { x \in \mathcal { X } _ { 0 } } \left| e ^ { * } ( x ) \right|
$$

satisfies the bound

$$
d < \operatorname* { m a x } _ { x \in \mathcal { X } } | e ^ { * } ( x ) | .
$$

If $\mathcal { X } _ { 0 }$ is empty, we define $^ d$ to be zero. We prove that inequality (7.8) is obtained when $\pmb \theta$ has the positive value

$$
\begin{array} { r } { \theta = \frac { 1 } { 2 } [ \underset { x \in \mathcal { X } } { \operatorname* { m a x } } \left| e ^ { * } ( x ) \right| - d ] . } \end{array}
$$

Because the set $\mathcal { Z }$ is closed, we may let $\xi$ be an element of $\mathcal { X }$ that satisfies the equation

$$
\left| e ^ { * } ( \xi ) - \theta p ( \xi ) \right| = \operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| .
$$

If $\xi$ is in $\mathcal { X } _ { 0 }$ , the bound

$$
\operatorname* { m a x } _ { x \in \mathcal { X } } \left| e ^ { * } ( x ) - \theta p ( x ) \right| = \left| e ^ { * } ( \xi ) \right| + \left| \theta p ( \xi ) \right| \leqslant d + \theta
$$

is obtained, where the last term depends on expressions (7.11) and (7.9). Hence condition (7.8) follows from inequality (7.12) and equation (7.13). Alternatively, when $\xi$ is not in $\mathcal { X } _ { 0 }$ ,the signs of the terms $e ^ { * } ( \xi )$ and $p ( \xi )$ are the same, which gives the strict inequality

$$
\left| e ^ { * } ( \xi ) - \theta p ( \xi ) \right| < \operatorname* { m a x } { [ | e ^ { * } ( \xi ) | , | \theta p ( \xi ) | ] } .
$$

Again it follows that condition (7.8) is satisfied. The proof of the theorem is complete.□

This theorem justifies the remark, made in Section 7.1, that, to find out if a trial approximation is optimal, one only need consider the extreme values of the error function. Specifically, one should ask if condition (7.6) holds for some function $\pmb { p }$ in $\mathcal { A }$

# 7.3 The characterization theorem and the Haar condition

If the set $\boldsymbol { \mathcal { A } }$ of approximating functions is the space $\mathcal { P } _ { n }$ of algebraic polynomials of degree at most $\pmb { n }$ ， then it is rather easy to test whether condition (7.6) can be.obtained. We make use of the fact that a function in $\mathcal { P } _ { n }$ has at most $_ n$ sign changes. Therefore,if the error function $[ f ( x ) - p ^ { * } ( x ) ]$ changes sign more than $\pmb { n }$ times as $x$ ranges over $\mathcal { L } _ { \mathbf { M } } ,$ ,then $p ^ { * }$ is a best approximation. Conversely, if the number of sign changes does not exceed $_ n$ , then we can choose the zeros of a polynomial in ${ \mathcal { P } } _ { n }$ so that condition (7.6) is satisfied. This result is usually called the minimax characterization theorem, and it is stated formally below.

It is useful to express the theorem in a form that applies to a class of functions that includes polynomials as a special case. The usual way of defining this class is to identify the properties of polynomials that are used in the proof of the characterization theorem. They are the following two conditions:

(1) If an element of $\mathcal { P } _ { n }$ has more than $\pmb { n }$ zeros, then it is identically zero.

(2) Let $\{ \zeta _ { j } ; j = 1 , 2 , \ldots , k \}$ be any set of distinct points in the open interval $( a , b )$ ,where $k \leqslant n$ .There exists an element of ${ \mathcal P _ { n } }$ that changes sign at these points,and that has no other zeros. Moreover, there is a function in ${ \mathcal { P } } _ { n }$ that has no zeros in $[ a , b ]$

The following two properties of polynomials are required later:

(3) If a function in $\mathcal { P } _ { n }$ ,that is not identically zero, has j zeros,and if $\pmb { k }$ of these zeros are interior points of $[ a , b ]$ at which the function does not change sign, then the number $( j + k )$ is not greater than $_ n$   
(4) Let $\{ \xi _ { j } ; j = 0 , 1 , \ldots , n \}$ be any set of distinct points in $[ a , b ] ,$ and let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be any basis of $\mathcal { P } _ { n }$ . Then the $( n + 1 ) \times$ $( n + 1 )$ matrix whose elements have the values $\{ \phi _ { i } ( \pmb { \xi } _ { j } )$ ； $i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ is non-singular.

An $( n + 1 )$ -dimensional linear subspace $\pmb { \mathcal { A } }$ of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ is said to satisfy the‘Haar condition’ if these four statements remain true when $\mathcal { P } _ { n }$ is replaced by the set $\mathcal { A }$ Equivalently,any basis of $\mathscr { A }$ is called a ‘Chebyshev set'. Spaces that satisfy the Haar condition are studied in Appendix A. It is proved that properties (1), (3) and (4) are equivalent, and that these properties imply condition (2). It is usual to define the Haar condition in terms of the first property. Thus $\pmb { \mathcal { A } }$ satisfies the Haar condition if and only if,for every non-zero $p$ in $\mathcal { A } ,$ ， the number of roots of the equation $\{ p ( x ) = 0$ ； $a \leqslant x \leqslant b \}$ is less than the dimension of $\mathcal { A }$

# Theorem 7.2 (Characterization Theorem)

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ that satisfies the Haar condition,and let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .Then $p ^ { * }$ is the best minimax approximation from $\mathscr { A }$ to $f ,$ if and only if there exist $( n + 2 )$ points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ ,such that the conditions

$$
\begin{array} { r l } & { a \leqslant \xi _ { 0 } ^ { * } < \xi _ { 1 } ^ { * } < \ldots < \xi _ { n + 1 } ^ { * } \leqslant b , } \\ & { \left| f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) \right| = \left\| f - p ^ { * } \right\| _ { \infty } , \qquad i = 0 , 1 , \ldots , n + 1 , } \end{array}
$$

and

$$
f ( \xi _ { i + 1 } ^ { * } ) - p ^ { * } ( \xi _ { i + 1 } ^ { * } ) = - [ f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) ] , \qquad i = 0 , 1 , \dots , n ,
$$

are obtained.

Proof. We let $\mathcal { Z }$ be the interval $[ a , b ]$ in Theorem 7.1. The present theorem is proved in the way that is described in the first paragraph of this section, by making use of the properties (1) and (2) that are stated above, which hold when $\pmb { \mathcal { A } }$ satisfies the Haar condition.□

One important application of this theorem is to prove the minimum property of Chebyshev polynomials. We recall from equation (4.26) that the Chebyshev polynomial $T _ { n }$ is the polynomial of degree $_ n$ that is defined on the interval [-1,1] by the equation

$$
T _ { n } ( x ) = \cos { ( n \theta ) } , \qquad x = \cos { \theta } , \qquad 0 \leqslant \theta \leqslant \pi .
$$

The minimum property is sufficiently useful to be stated as a theorem.

# Theorem 7.3

Let the range of $_ { x }$ be[-1,1],and let $\pmb { n }$ be any positive integer. The polynomial $( { \frac { 1 } { 2 } } ) ^ { n - 1 } T _ { n }$ is the member of $\mathcal { P } _ { n }$ whose $\infty$ -norm is least, subject to the condition that the coefficient of $x ^ { n }$ is equal to one.

Proof. One way of identifying the required polynomial is to seek the values of the coeffcients $\{ c _ { i } ; i = 0 , 1 , \ldots , n - 1 \}$ that minimize the expression

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \left. x ^ { n } + \sum _ { i = 0 } ^ { n - 1 } c _ { i } x ^ { i } \right. .
$$

We see that this approach is equivalent to finding the best approximation from $\scriptstyle { \mathcal { P } } _ { n - 1 }$ to the function $\{ x ^ { n } ; - 1 \leqslant x \leqslant 1 \}$ . It follows from Theorem 7.2 that $( { \frac { 1 } { 2 } } ) ^ { n - 1 } T _ { n }$ is the required polynomial, if the coefficientof $x ^ { n }$ is one, and if there exist points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n \}$ in $[ - 1 , 1 ]$ ,arranged in ascending order, such that the equations

$$
T _ { n } ( \xi _ { i } ) = ( - 1 ) ^ { n - i } \big \| T _ { n } \big \| _ { \infty } , \qquad i = 0 , 1 , \ldots , n ,
$$

hold. The recurrence relation (4.25) implies that the coefficient of $x ^ { n }$ is correct. Moreover,the definition (7.2O) shows that equation (7.22） is satisfied if we let each $\xi _ { i }$ have the value cos $[ ( n - i ) \pi / n ]$ .The theorem is proved.□

The main reason for letting $\mathcal { Z }$ be any closed subset of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ in the statement of Theorem 7.1, is that the exchange algorithm requires the case when $\mathcal { Z }$ contains just $( n + 2 )$ points. In descriptions of the exchange algorithm it is usual to call such a set of points a ‘reference'.We use this term also,and we let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be the points of the reference. We assume that always these points are in ascending order

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b .
$$

The following corollary of Theorem 7.1 is used on every iteration of the exchange algorithm.

# Theorem 7.4

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, and let $f$ be any function in $\mathcal { C } [ \alpha , b ]$ Then $p ^ { * }$ is the function in $\mathscr { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - p ( \xi _ { i } ) | , \qquad p \in \mathcal { A } ,
$$

if and only if the equations

$$
f ( \xi _ { i + 1 } ) - p ^ { * } ( \xi _ { i + 1 } ) = - [ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ] , \qquad i = 0 , 1 , \dots , n ,
$$

are satisfied.

Proof. We follow the method of proof of Theorem 7.2,except that we let $\mathcal { Z }$ be the point set $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ，instead of the interval $[ a , b ]$ □

The function $p ^ { * }$ that minimizes expression (7.24) may be calculated from the equations (7.25). It is usual to let $\pmb { h }$ be the value of $[ f ( \xi _ { 0 } ) -$ $\begin{array} { r } { p ^ { \ast } ( \xi _ { 0 } ) ] , } \end{array}$ and to choose a basis of $\mathcal { A } , \{ \phi _ { j } ; j = 0 , 1 , \dots , n \}$ say. It follows that the coefficients of the function

$$
p ^ { * } ( x ) = \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

satisfy the equations

$$
f ( \xi _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

which is a linear system in the unknowns $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ and $\pmb { h }$ Because Theorem 7.4 shows that these equations have a solution for all functions $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，the matrix of the system is non-singular. Hence only one element of $\mathscr { A }$ minimizes expression (7.24). A more general and more useful method of proving uniqueness is given in the next section.

# 7.4 Uniqueness and bounds on the minimax error

Suppose that the conditions of Theorem 7.2 hold, that $p ^ { * }$ and $q ^ { * }$ are both best minimax approximations from $\mathscr { A }$ to $f ,$ and that conditions (7.17),(7.18) and (7.19) are satisfied. We let $r ^ { * }$ be the function $( q ^ { * } - p ^ { * } )$ ， and we consider the numbers

$$
\begin{array} { r } { r ^ { * } ( \xi _ { i } ^ { * } ) = [ f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) ] - [ f ( \xi _ { i } ^ { * } ) - q ^ { * } ( \xi _ { i } ^ { * } ) ] , \smallskip } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

Because $\| f - q ^ { * } \| _ { \infty }$ and $\| f - p ^ { * } \| _ { \infty }$ are equal, it follows from equation (7.18)

that either $r ^ { * } ( \xi _ { i } ^ { * } )$ is zero,or its sign is the same as the sign of $[ f ( \xi _ { i } ^ { * } ) -$ $p ^ { * } ( \xi _ { i } ^ { * } ) ]$ .Hence equation (7.19) provides information about the signs of the terms of the sequence $\{ r ^ { * } ( \xi _ { i } ^ { * } ) ; i = 0 , 1 , \dots , n + 1 \}$ . It can be deduced from this information that $r ^ { * }$ is identically zero. Hence the best minimax approximation from $\mathscr { A }$ to $f$ is unique. The method of proving that $r ^ { * }$ is identically zero is a general one that has several applications. Therefore it is stated in the following theorem.

# Theorem 7.5

Let $r$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ and let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, such that the conditions

$$
( - 1 ) ^ { i } r ( \xi _ { i } ) \geqslant 0 , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

are satisfied. Then $r$ has at least $( n + 1 )$ zeros in $[ a , b ] ,$ provided that any double zero is counted twice, where a double zero is a zero that is strictly inside $[ a , b ] ,$ at which $r$ does not change sign.

Proof. Let $\mathscr { F }$ and $\mathscr { J }$ be the sets

$$
\begin{array} { r l } { \mathcal { G } = \{ i \colon r ( \xi _ { i } ) \neq 0 , \quad } & { { } i = 0 , 1 , \ldots , n + 1 \} } \\ { \mathcal { J } = \{ j \colon r ( \xi _ { j } ) = 0 , \quad } & { { } j = 0 , 1 , \ldots , n + 1 \} } \end{array} ,
$$

and let $n ( { \mathcal { F } } )$ and $n ( { \mathcal { F } } )$ be the number of elements in each set.The theorem is trivial if $n ( { \mathcal { F } } )$ is zero or one. Otherwise we consider the number of zeros in the interval $[ \xi _ { k } , \xi _ { l } ] ,$ where $k$ and $\iota$ are both in $\pmb { \mathcal { F } }$ ,and where no other element of $\mathscr { F }$ is in the range $[ k , l ]$ Condition (7.29) implies that the numbers $r ( \xi _ { k } )$ and $r ( \xi _ { l } )$ have the same sign if $( l - k )$ is even,and they have opposite signs if $( l - k )$ is odd.Hence the number of zeros of $r$ in the interval $[ \xi _ { k } , \xi _ { l } ]$ is at least one more than the number of points of the set $\{ \xi _ { j } ; j \in \mathcal { J } \}$ that are in this interval, provided that any double zero is counted twice. Because the number of pairs $[ \xi _ { k } , \xi _ { l } ]$ that have this property is $[ n ( { \mathcal { I } } ) - 1 ]$ , it follows that the total number of zeros of $r$ in $[ a , b ]$ is at least $[ n ( { \mathcal { I } } ) + n ( { \mathcal { J } } ) - 1 ] ,$ ，which is the required result.□

Hence we obtain the uniqueness theorem for best approximation in the 8-norm.

# Theorem 7.6

Let $\boldsymbol { \mathcal { A } }$ be a linear subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition.Then, for any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ，there is just one best minimax approximation from $\mathscr { A }$ to $f .$

Proof. The remarks in the first paragraph of this section and Theorem 7.5 imply that, if $p ^ { * }$ and $q ^ { * }$ are both best approximations, then the function $( p ^ { * } - q ^ { * } )$ has at least $( n + 1 )$ zeros in $[ a , b ] ,$ provided that any double zero is counted twice. It follows from property (3) of Section 7.3, which is obtained when the Haar condition is satisfied, that the functions $p ^ { * }$ and $q ^ { * }$ are the same.□

Another interesting property of the Haar condition，which is the subject of Exercise 7.9, is that, if $\mathscr { A }$ is any finite-dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ that does not satisfy the Haar condition, then there are functions $f$ in $\mathcal { C } [ \alpha , b ]$ that have several best approximations in $\mathcal { A } .$

Theorem 7.5 is also useful for obtaining lower bounds on the least value of expression (7.1). Suppose that an iterative method for calculating a best approximation produces a trial approximation $p ^ { * }$ ,and that the conditions (7.17),(7.18) and (7.19) are almost satisfied. Then we usually have available a reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ,such that the signs of the terms $\{ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , n + 1 \}$ alternate.In this case the following theorem applies.

# Theorem 7.7

Let the conditions of Theorem 7.2 hold, let $p ^ { * }$ be any element of $\mathcal { A } ,$ and let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a reference, such that the condition

$$
\begin{array} { r } { \mathrm { s i g n } [ f ( \xi _ { i + 1 } ) - p ^ { * } ( \xi _ { i + 1 } ) ] = - \mathrm { s i g n } [ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ] , \smallskip } \\ { i = 0 , 1 , \ldots , n , } \end{array}
$$

is satisfied. Then the inequalities

$$
\begin{array} { r l } { \underset { i = 0 , 1 , \ldots , n + 1 } { \operatorname* { m i n } } \left| f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) \right| \leqslant \underset { p \in \mathcal { A } } { \operatorname* { m i n } } \underset { i = 0 , 1 , \ldots , n + 1 } { \operatorname* { m a x } } \left| f ( \xi _ { i } ) - p ( \xi _ { i } ) \right| } & { } \\ { \leqslant \underset { p \in \mathcal { A } } { \operatorname* { m i n } } \left\| f - p \right\| _ { \infty } } & { } \\ { } & { \leqslant \left\| f - p ^ { * } \right\| _ { \infty } } \end{array}
$$

are obtained. Moreover, the first inequality is strict unless all the numbers $\{ | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | ; i = 0 , 1 , \ldots , n + 1 \}$ are equal.

Proof. The third inequality of expression(7.32) holds because $p ^ { * }$ is in $\scriptstyle { \mathcal { A } } ,$ ， and the second one holds because the reference is a subset of $[ a , b ]$ .In order to prove the first inequality, we suppose that there exists a function $q ^ { * }$ in $\pmb { \mathcal { A } }$ that satisfies the condition

$$
\operatorname* { m i n } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | \geqslant \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } | f ( \xi _ { i } ) - q ^ { * } ( \xi _ { i } ) | .
$$

If $q ^ { * }$ is equal to $p ^ { * }$ ，, then expression (7.33） shows that the numbers $\{ | f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) | ; i = 0 , 1 , \ldots , n + 1 \}$ are all the same.Thus the first part of condition (7.32) can hold as an equation. Alternatively, let us suppose that $p ^ { * }$ is not equal to $q ^ { * }$ , but that inequality (7.33) is satisfied.As in the first paragraph of this section, we let $r ^ { * }$ be the function $( q ^ { * } - p ^ { * } )$ . Because condition (7.33） implies that the numbers (7.28) have the same sign properties as before,we deduce from Theorem 7.5 and from the Haar condition that the functions $p ^ { * }$ and $q ^ { * }$ are the same,which is a contradiction. The theorem is proved.□

It is useful to note that, if $p ^ { * }$ is the best minimax approximation from $\pmb { \mathcal { A } }$ to $f ,$ and if the reference in the statement of the last theorem is the set of points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ that occurs in conditions (7.17),(7.18) and (7.19),then all the inequalities of expression (7.32) are satisfied as equations.

# 7 Exercises

7.1 For any $f$ in $\mathcal { C } [ \alpha , b ]$ ,let $X ( f )$ be the best minimax approximation in $\mathcal { P } _ { n }$ to $f .$ Construct an example to show that the operator $\pmb { X }$ is not linear.

7.2 Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \alpha , b ] .$ let $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ be a basis of $\scriptstyle { \mathcal { A } }$ ,let $p ^ { * }$ be a best approximation from $\pmb { \mathcal { A } }$ to a function $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ ,and let $\mathcal { Z } _ { \mathbf { M } }$ be the set that is defined by equations (7.3) and (7.4). Prove that, if $\mathcal { Z } _ { \mathbf { M } }$ contains just the discrete points $\left\{ \xi _ { j } ; j = 1 , 2 , \ldots , r \right\}$ ,and if $\pmb { H }$ is the $( n +$ $1 ) \times r$ -dimensional matrix whose elements have the values $\{ \phi _ { i } ( \xi _ { j } ) ; i = 0 , 1 , \ldots , n ; j = 1 , 2 , \ldots , r \}$ ,then the rank of $\pmb { H }$ is less than $r$

7.3 Let $\pmb { \mathcal { A } }$ be a finite-dimensional linear subspace of $\mathcal { C } [ \alpha , b ]$ ,let $p ^ { * }$ be a trial approximation from $\pmb { \mathcal { A } }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ ,and let $\mathcal { Z } _ { \mathbf { M } }$ be the set that is defined by equations (7.3) and (7.4). Prove that $p ^ { * }$ is a best approximation from $\mathscr { A }$ to $f ,$ if there exist points $\left\{ \xi _ { j } ; j = 1 , 2 , \ldots , r \right\}$ in $\mathcal { Z } _ { \mathbf { M } }$ and non-zero multipliers $\{ \sigma _ { j } ; j =$ $1 , 2 , \ldots , r \}$ , such that, for all functions $\phi$ in $\scriptstyle { \mathcal { A } } ,$ ， the equation

$$
\sum _ { j = 1 } ^ { r } \sigma _ { j } \phi ( \xi _ { j } ) = 0
$$

holds,and such that the sign conditions

$$
\sigma _ { j } [ f ( \xi _ { j } ) - p ^ { * } ( \xi _ { j } ) ] \geqslant 0 , \qquad j = 1 , 2 , \ldots , r ,
$$

are satisfied.

7.4 Let $\pmb { n }$ be a positive integer, and let $\mathscr { A }$ be the linear space of dimension $( 2 n + 1 )$ that is spanned by the trigonometric functions $\left\{ \cos { \left( j x \right) } , - \pi + \varepsilon \leqslant x \leqslant \pi - \varepsilon ; j = 0 , 1 , \ldots , n \right\}$ and $\left\{ \sin { ( j x ) } , - \pi + \varepsilon \leqslant x \leqslant \pi - \varepsilon ; j = 1 , 2 , \ldots , n \right\} .$ ，where $\pmb \varepsilon$ isa constant from the interval $[ 0 , \pi )$ . Prove that $\pmb { \mathcal { A } }$ satisfies the Haar condition if $\pmb \varepsilon$ is positive.By considering the case when $\pmb \varepsilon$ is zero, show that conditions (1) and (2） of Section 7.3 are not equivalent.

Calculate the best approximation to the function $\{ f ( x ) = \left| x + { \frac { 1 } { 2 } } \right|$ ；   
$- 1 \leqslant x \leqslant 1 \}$ by a quadratic polynomial.

7.6 Let the conditions of Theorem 7.6 be satisfied. Prove the theorem by showing that, if $q ^ { * }$ and $r ^ { * }$ are best approximations from $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ a , b ] ,$ and if $\pmb { \xi }$ is any solution of the equation $\left| f ( \xi ) - p ^ { * } ( \xi ) \right| = \| f - p ^ { * } \| _ { \infty } ,$ ，where $p ^ { * }$ is the approximation $^ { \frac { 1 } { 2 } } ( q ^ { * } + r ^ { * } )$ ,then $q ^ { * } ( \xi )$ is equal to $r ^ { * } ( \pmb { \xi } )$

7.7 Let $\mathscr { A }$ be the space $\mathcal { P } _ { 2 }$ ,let $f$ be the function $\{ f ( x ) = x ^ { 3 }$ ； $0 \leqslant x \leqslant 1 \}$ ， and let the points $\{ \xi _ { i } ; i = 0 , 1 , 2 , 3 \}$ have the values ${ \xi _ { 0 } } = 0 . 0$ ， $\xi _ { 1 } = 0 . 3$ ， $\xi _ { 2 } = 0 . 8$ and $\xi _ { 3 } = 1 . 0$ . Calculate the polynomial $p ^ { * }$ that minimizes expression (7.24).Hence the first line of expression (7.32） is satisfied as an equation. Calculate all the terms of inequality (7.32)，using Theorem 7.3 to obtain the least maximum error $d ^ { * } = \operatorname* { m i n } \left\{ \| f - p \| _ { \infty } ; p \in \mathcal { A } \right\}$ .You should find that expression (7.32） gives close upper and lower bounds on $d ^ { * }$ .

7.8 Show that the three-dimensional linear space $\mathscr { A }$ that is spanned bythefunctions $\{ \phi _ { 0 } ( { \pmb x } ) = 1$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ ， $\begin{array} { r } { \{ \phi _ { 1 } ( { \pmb x } ) = } \end{array}$ cos $( 2 x )$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ and $\left\{ \phi _ { 2 } ( x ) = \sin \left( 3 x \right) \right.$ ； $\scriptstyle - { \frac { 1 } { 6 } } \pi \leqslant x \leqslant { \frac { 1 } { 2 } } \pi \}$ satisfies the Haar condition. It is sufficient to prove that property (4) of Section 7.3 is obtained. Show also that there is no function in $\mathscr { A }$ that is zero at the left-hand end of the range, $- \frac { 1 } { 6 } \pi ,$ and that has no other zeros. It is most unusual for a space that satisfies the Haar condition to have this property.

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that does not satisfy the Haar condition. By using condition (4) of Section 7.3 and Exercise 7.3,show that there exists $f$ in ${ \mathcal { C } } [ a , b ]$ and a best approximation $p ^ { * }$ from $\mathscr { A }$ to $f ,$ such that the set ${ \mathcal { Z } } _ { \mathbf { M } } = \{ x : | f ( x ) - p ^ { * } ( x ) | = \| f - p ^ { * } \| _ { \infty } \}$ contains fewer than $( n + 2 )$ points. Let $\bar { p }$ be a non-zero function in $\mathscr { A }$ that is zero at the points of $\mathcal { Z } _ { \mathbf { M } }$ .By modifying $f$ if necessary, deduce from Exercise 7.3 that it is possible for $( p ^ { * } + \theta \bar { p } )$ to be a best approximation from $\mathscr { A }$ to $f$ for a range of values of the number $\pmb \theta _ { \mathrm { i } }$ , which proves that not every element of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ has a best minimax approximation in $\mathcal { A } .$

7.10 In a discrete minimax calculation the numbers $\{ f _ { i } ; i =$ $1 , 2 , \ldots , m \}$ and $\{ \phi _ { i j } ; i = 1 , 2 , \ldots , m ; j = 0 , 1 , \ldots , n \}$ are given, andone requiresthe values ofthe parameters $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ that minimize the expression

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \bigg | f _ { i } - \sum _ { j = 0 } ^ { n } \phi _ { i j } \lambda _ { j } \bigg | .
$$

Investigate the relevance of the theory of this chapter to this calculation. Hence show that the least value of the expression max $: [ \left. 2 - 4 \lambda _ { 1 } - 5 \lambda _ { 2 } \right. , \left. 3 - 5 \lambda _ { 1 } - 6 \lambda _ { 2 } \right. , \left. 4 - 6 \lambda _ { 1 } - 8 \lambda _ { 2 } \right. ]$ is equal to $\scriptstyle { \frac { 2 } { 7 } }$

# The exchange algorithm

# 8.1 Summary of the exchange algorithm

Let $f$ be a function in ${ \mathcal { C } } [ a , b ] ,$ and let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition.The exchange algorithm calculates the element of $\mathscr { A }$ that minimizes the maximum error

$$
\| f - p \| _ { \infty } = \operatorname* { m a x } _ { a \leqslant x \leqslant b } | f ( x ) - p ( x ) | , \qquad p \in \mathcal { A } .
$$

Instead of trying to reduce the error of each trial approximation, the algorithm adjusts a reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ , so that it converges to a point set $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ ， that satisfies the conditions of Theorem 7.2. The adjustments are made by an iterative procedure.

In order to begin the calculation,an initial reference is chosen.It can be any set of points that satisfies the condition

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b ,
$$

but a particular choice that is suitable when $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ is given in Section 8.4. At the start of each iteration a reference is available that is different from the references of all previous iterations.The calculations of each iteration are as follows.

We let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be the reference at the start of an iteration. First the function $p$ in $\mathscr { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \big | f ( \xi _ { i } ) - p ( \xi _ { i } ) \big | , \qquad p \in \mathcal { A } ,
$$

is calculated. Theorem 7.4 shows that the coefficients of $p$ may be found by solving the linear system of equations

$$
f ( \xi _ { i } ) - p ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

where,as in equation (7.27), $\pmb { h }$ is also defined by the linear system. It follows from Theorem 7.7 that the bounds

$$
\lvert h \rvert \leqslant \lVert f - p ^ { * } \rVert _ { \infty } \leqslant \lVert f - p \rVert _ { \infty }
$$

are satisfied, where $p ^ { * }$ is the required best approximation from $\mathcal { A }$ to $f .$ In order to make use of the right-hand bound,and in order to obtain a suitable change to the reference, the error function

$$
e ( x ) = f ( x ) - p ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is considered.

A typical error function in the case ${ n = 3 }$ is shown in Figure 8.1. We see that equation (8.4) is satisfied,and that consequently $_ e$ has at least $_ { n }$ turning points. The positions of the extrema,which are called $\eta _ { 1 } , \eta _ { 2 }$ and $\pmb { \eta _ { 3 } }$ in the figure,are estimated by evaluating the error function at several points of $[ a , b ]$ . It is necessary in practice to obtain these points automa-tically in an effcient way. Suitable methods are based on local quadratic fits to the error function,but we assume that the abscissae of the extrema can be found exactly. We let $\pmb { \eta }$ be a point that satisfes the equation

$$
\left| f ( \eta ) - p ( \eta ) \right| = \| f - p \| _ { \infty } .
$$

The calculation finishes if the difference

$$
\delta = \left| f ( \eta ) - p ( \eta ) \right| - \left| h \right|
$$

is sufficiently small, because inequality (8.5) implies the bound

$$
\| f - p \| _ { \infty } \leqslant \| f - p ^ { * } \| _ { \infty } + \delta .
$$

Otherwise the reference is changed in order to begin another iteration. In the ‘one-point exchange algorithm’ the new reference, $\begin{array} { r } { \{ \xi _ { i } ^ { + } ; i = 0 , } \end{array}$ $1 , \ldots , n + 1 \}$ say, contains $\pmb { \eta }$ and $( n + 1 )$ of the points $\{ \xi _ { i } ; i = 0 , 1 , \ldots ,$ $n + 1 \}$ ，which are specified in the next section. The most important property of the change of reference is that the quantity $| h |$ ,which is called the levelled reference error, increases strictly monotonically from iteration to iteration.

![](images/fb41900dda36b867e87768be799afa864668b8f2c9a49d2ee3648a81681ddf6a.jpg)  
Figure 8.1. An error function of the exchange algorithm.

Because it is convenient to regard the levelled reference error as a function of the reference, we use the notation

$$
h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ) = | h | .
$$

It is helpful to take the point of view that the purpose of the change of reference is to increase the value of $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ .Because expres-sion (8.8) is small only if the levelled reference error is close to the bound $\| f - p ^ { * } \| _ { \infty }$ ofinequality (8.5)， it is advantageous to make $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ as large as possible. Thus the exchange algorithm is a method of solving a maximization problem,where the variables are the points of the reference. The structure of $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ,however, is such that it is inefficient to use one of the superlinearly convergent algorithms that are available in subroutine libraries for general maximization calculations.

# 8.2 Adjustment of the reference

As in the previous section,we consider an iteration of the exchange algorithm that calculates a function $p$ in $\mathscr { A }$ by solving the equations (8.4),and that changes the reference from $\{ \xi _ { i } ; i = 0 , 1 , \ldots ,$ $n + 1 \}$ to $\{ \xi _ { i } ^ { + } ; i = 0 , 1 , \ldots , n + 1 \}$ . The method of choosing the new reference depends on Theorem 7.7,for it states conditions that imply the increase

$$
h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } ) > h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )
$$

in the levelled reference error. The theorem shows that it is sufficient if the conditions

$$
\begin{array} { r l } & { \mathsf { s i g n } \left[ f ( \xi _ { i + 1 } ^ { + } ) - p ( \xi _ { i + 1 } ^ { + } ) \right] } \\ & { \quad = - \mathsf { s i g n } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] , \qquad i = 0 , 1 , \ldots , n , } \end{array}
$$

and

$$
\begin{array} { r } { \big | f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \big | \geqslant \big | h \big | , \qquad i = 0 , 1 , \ldots , n + 1 , } \end{array}
$$

are satisfied, provided that at least one of the numbers $\{ \vert f ( \pmb { \xi } _ { i } ^ { + } ) - p ( \pmb { \xi } _ { i } ^ { + } ) \vert$ ； $i = 0 , 1 , \ldots , n + 1 \}$ is greater than $| h |$ .Hence,several ways of obtaining an increase in the levelled reference error are suggested by Figure 8.1.

One method is to let each point of the new reference be an extremum of the error function (8.6). In this case the error curve of Figure 8.1 gives the reference $\left\{ \xi _ { 0 } , \eta _ { 1 } , \eta _ { 2 } , \eta _ { 3 } , \xi _ { 4 } \right\}$ ， and we note that conditions (8.12） and (8.13)are obtained. Methods that can change every reference point on every iteration are usually more efficient than the one-point exchange algorithm, in the sense that fewer iterations are required to reduce the number (8.8) to less than a prescribed tolerance.We give our attention, however, to the one-point method, because it is interesting to discover the way in which it achieves a fast rate of convergence.An advantage of the one-point method is that the work of solving the equations (8.4) may be reduced, by using techniques for updating matrix factorizations.

In the one-point exchange algorithm, we let $\xi _ { q }$ be the point that leaves the old reference to make room for $\pmb { \eta }$ .For example,in Figure 8.1,because $\pmb { \eta _ { 1 } }$ is the solution of equation (8.7),we let $q = 1$ , in order that the new reference is the set $\left\{ \xi _ { 0 } , \eta _ { 1 } , \xi _ { 2 } , \xi _ { 3 } , \xi _ { 4 } \right\}$ .No other choice of $q$ allows condition (8.12) to be satisfed. Provided that $| h |$ is positive, it is true generally that condition (8.12) and the value of $\pmb { \eta }$ determine the point that leaves the reference uniquely. The case when $| h |$ is zero can occur only on the first iteration,and then any value of $\pmb q$ gives the increase (8.11).

When $| h |$ is positive,and when $\pmb { \eta }$ is inside the interval $[ \xi _ { 0 } , \xi _ { n + 1 } ] ,$ the value of $\pmb q$ is such that the signs of $[ f ( \eta ) - p ( \eta ) ]$ and $[ f ( \pmb { \xi } _ { q } ) - p ( \pmb { \xi } _ { q } ) ]$ are the same,and no point of the old reference is between $\xi _ { q }$ and $\pmb { \eta }$ .When $\pmb { \eta } < \pmb { \xi } _ { 0 }$ ， then $\xi _ { q }$ is either $\pmb { \xi _ { 0 } }$ or $\xi _ { n + 1 }$ . We let $q$ be zero if the signs of $[ f ( \eta ) - p ( \eta ) ]$ and $[ f ( \pmb { \xi } _ { 0 } ) - p ( \pmb { \xi } _ { 0 } ) ]$ are the same, otherwise it is necessary to let $q$ be $( n + 1 )$ .A similar rule determines the value of $q$ when $\pmb { \eta }$ is greater than $\xi _ { n + 1 }$ ·

The description of the one-point exchange algorithm is now complete. An example of its use is given in the next section,and some of its convergence properties are studied in Chapter 9.

# 8.3 An example of the iterations of the exchange algorithm

In order to show the convergence properties of the one-point exchange algorithm, this section describes the numerical results that are obtained when $\mathcal { A }$ is the two-dimensional linear space of functions of the form

$$
p ( x ) = \lambda _ { 0 } x + \lambda _ { 1 } x ^ { 2 } , \qquad 0 \leqslant x \leqslant \pi / 2 ,
$$

when $f$ is the function

$$
f ( x ) = \sin x , \qquad 0 \leqslant x \leqslant \pi / 2 ,
$$

and when the reference of the first iteration contains the points {0.5,1.0, $\pi / 2 \}$ .Because $p ( 0 )$ is equal to $f ( 0 )$ for all values of the coefficients $\lambda _ { 0 }$ and $\lambda _ { 1 }$ ,the first point of the reference is positive throughout the calculation. Because the only extrema of the error $\{ f ( { \pmb x } ) - { \pmb p } ( { \pmb x } ) _ { \pmb \mathrm { \| } }$ $0 \leqslant x \leqslant \pi / 2 \}$ occur near $\xi _ { 0 }$ and $\xi _ { 1 }$ , the point $\pi / 2$ never leaves the reference.Hence the error function shown in Figure 8.2 is typical, and we let $\pmb { \eta _ { 0 } }$ and $\pmb { \eta } _ { 1 }$ be the abscissae of its turning points. Therefore,if another iteration is required, its reference is either $\{ \eta _ { 0 } , \xi _ { 1 } , \xi _ { 2 } \}$ or $\{ \xi _ { 0 } , \eta _ { 1 } , \xi _ { 2 } \}$ ，where the one that is chosen depends on which is the larger of the numbers $\left| e ( \eta _ { 0 } ) \right|$ and $\left| e ( \eta _ { 1 } ) \right|$

Tables 8.1 and 8.2 give the levelled reference errors and the extrema that occur on the first five iterations. We note that the levelled reference errors increase strictly monotonically and that the values of $\| f - p \| _ { \infty }$ decrease monotonically. Both these sequences seem to be converging rapidly to the same limit. Hence inequality (8.5） provides excellent bounds on the least maximum error. For example,after only three iterations,we find that the bounds

![](images/370b9bf3720c651e41bd93622b727169f9fccbb19f1d97ad749fac8799cc9706.jpg)  
Figure 8.2. An error function of the example of Section 8.3.

Table 8.1. The references of the example of Section 8.3   

<table><tr><td>Iteration</td><td>50</td><td>51</td><td>5</td><td>h(50,51,52）</td></tr><tr><td>1</td><td>0.500 000</td><td>1.000 000</td><td>1.570 796</td><td>0.013 998 30</td></tr><tr><td>2</td><td>0.298 938</td><td>1.000 000</td><td>1.570 796</td><td>0.016 978 02</td></tr><tr><td>3</td><td>0.298 938</td><td>1.104 968</td><td>1.570 796</td><td>0.017 482 78</td></tr><tr><td>4</td><td>0.283880</td><td>1.104 968</td><td>1.570 796</td><td>0.017 501 65</td></tr><tr><td>5</td><td>0.283 880</td><td>1.106 124</td><td>1.570 796</td><td>0.017 501 72</td></tr></table>

Table 8.2. The extrema of the error function of the example of Section 8.3   

<table><tr><td>Iteration</td><td>no</td><td>e(no)</td><td>n1</td><td>e(n1)</td></tr><tr><td>1</td><td>0.298 938</td><td>-0.019 659 29</td><td>1.133 035</td><td>0.016 193 66</td></tr><tr><td>2</td><td>0.279 792</td><td>-0.017 039 99</td><td>1.104 968</td><td>0.018 391 16</td></tr><tr><td>3</td><td>0.283 880</td><td>-0.017 521 06</td><td>1.106 316</td><td>0.017 483 03</td></tr><tr><td>4</td><td>0.283 733</td><td>-0.017 501 66</td><td>1.106 124</td><td>0.017 501 83</td></tr><tr><td>5</td><td>0.283 733</td><td>-0.017 501 72</td><td>1.106 124</td><td>0.017 501 72</td></tr></table>

$$
0 . 0 1 7 4 8 2 7 8 \leqslant \left\| f - p ^ { * } \right\| \leqslant 0 . 0 1 7 5 2 1 0 6
$$

are satisfied. Further, the maximum error of the approximation that is calculated on the fifth iteration agrees with the least maximum error to eight decimal places.It is highly satisfactory to obtain this accuracy in so few iterations.

Another interesting feature of the tables is that the abscissae $\pmb { \eta _ { 0 } }$ and $\pmb { \eta } _ { 1 }$ of the extrema of the error function are rather insensitive to the changes that are made to the points of the reference. It is proved in the next chapter that this property holds generally,and that it provides the fast rate of convergence.

We note also that the set $\pmb { \mathcal { A } }$ of the example does not satisfy the Haar condition, because many members of $\mathscr { A }$ have two zeros in the range $[ 0 , \pi / 2 ]$ .One of these zeros is always at $\scriptstyle x = 0$ .Hence the Haar condition is obtained on the range $[ \alpha , \pi / 2 ]$ ，where $\pmb { \alpha }$ is any fixed positive number that is less than $\pi / 2$ . It does not matter in this example that the Haar condition is not obtained. In general, however,before applying the exchange algorithm, one should check that $\mathscr { A }$ satisfies the Haar condition, because it is important to the remark that equation (8.4) defines the function $p$ that minimizes expression (8.3).

# 8.4 Applications of Chebyshev polynomials to minimax approximation

A very nice property of the exchange algorithm, which is proved in Chapter 9,is that, if the Haar condition holds,then convergence is obtained from any initial reference.However, some initial references are better than others,if one wishes to avoid the calculation of approximations whose errors are much larger than necessary. The problem of choosing a good initial reference is similar to the problem of choosing good interpolation points,which was considered in Chapter 4.When $\mathscr { A }$ is the space $\mathcal { P } _ { n }$ ，a suitable initial reference can be obtained from the properties of Chebyshev polynomials. Specifically,if the range of $x$ is [-1,1], we let the points of the initial reference have the values

$$
\xi _ { i } = \cos { [ ( n + 1 - i ) \pi / ( n + 1 ) ] } , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

because this choice has the following property.

# Theorem 8.1

Let $f \in \mathcal { C } [ - 1 , 1 ]$ ,and let $\pmb { p } \in \mathcal { P } _ { n }$ be the approximation to $f$ that is calculated by an iteration of the exchange algorithm, where the reference contains the points (8.17). If $f$ is a polynomial of degree $( n + 1 )$ ,then $p$ is the best minimax approximation from ${ \mathcal P _ { n } }$ to $f .$

Proof. Equation (8.17) and the definition of the Chebyshev polynomial $T _ { n + 1 }$ imply the values

$$
T _ { n + 1 } ( \xi _ { i } ) = ( - 1 ) ^ { n + 1 - i } , \qquad i = 0 , 1 , \dots , n + 1 .
$$

Because $( f - p )$ is in $\mathcal { P } _ { n + 1 }$ , it follows from equation (8.4) that the error function $\left( f - p \right)$ is a multiple of $T _ { n + 1 }$ .Therefore,by the Characterization Theorem 7.2, $p$ is the best approximation from $\mathcal { P } _ { n }$ to $f .$ □

Theorem 8.1 is useful, not only when $f$ is in $\mathcal { P } _ { n + 1 }$ , but also when $f$ is infinitely differentiable,and its Taylor series

$$
f ( x ) = \sum _ { j = 0 } ^ { \infty } \frac { x ^ { j } } { j ! } f ^ { ( j ) } ( 0 ) , \qquad - 1 \leqslant x \leqslant 1 ,
$$

is rapidly convergent. In this case it happens often that the error of the best approximation from $\mathcal { P } _ { n }$ to $f$ is dominated by the error that comes from the term $x ^ { n + 1 } f ^ { ( n + 1 ) } ( 0 ) / ( n + 1 ) !$ . Theorem 8.1 shows that the reference (8.17) makes this contribution to the error as small as possible. Moreover,by regarding the calculation of $\pmb { p }$ in Theorem 8.1 as a linear operator from $\mathcal { C } [ - 1 , 1 ]$ to $\mathcal { P } _ { n }$ ,and by finding the norm of this operator, it follows from Theorem 3.1 that the ratio of $\| f - p \|$ to the least maximum error is bounded by a small multiple of ln $\pmb { n }$ ，for all functions $f$ in $\mathcal { C } [ - 1 , 1 ]$

The reference points (8.17） are appropriate only for the interval [-1,1]. For the general range $[ a , b ] ,$ , it is helpful to recall the discussion, given in Section 6.3,of suitable changes to the Bernstein operator when [0,1] is replaced by $[ a , b ]$ .We again think of $[ a , b ]$ as an interval on the $x$ -axis of the graph of the function $\{ f ( x ) ; a \leqslant x \leqslant b \}$ ,and now we apply a linear transformation to the variable, so that this interval can be relabelled as[-1,1]. The points (8.17) are suitable for the new range of $\pmb { x }$ If we express them in terms of the original variable we have the values

$$
\begin{array} { c } { { \xi _ { i } = \frac { 1 } { 2 } ( a + b ) + \frac { 1 } { 2 } ( b - a ) \cos \Big [ \frac { ( n + 1 - i ) \pi } { ( n + 1 ) } \Big ] , } } \\ { { i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

which is therefore a suitable reference for the general range $[ a , b ]$ ,when $\pmb { \mathcal { A } }$ is the space $\mathcal { P } _ { n }$

Another application of Chebyshev polynomials to minimax approximation is that they provide a technique that is called ‘telescoping'. In order to describe it, we suppose that we have an approximation

$$
\bar { p } ( x ) = \bar { c } _ { 0 } + \bar { c } _ { 1 } x + . . . + \bar { c } _ { n + 1 } x ^ { n + 1 } , \qquad - 1 \leqslant x \leqslant 1 ,
$$

from $\mathcal { P } _ { n + 1 }$ to a function $\mathsf { \Omega } _ { | f \mathbf { i n } } \mathcal { C } [ - 1 , 1 ] ,$ , but that there is a possibility that an approximation from $\mathcal { P } _ { n }$ may be sufficiently accurate. For instance,we may have the bound

$$
\left\| f - { \bar { p } } \right\| \leqslant { \bar { \varepsilon } } ,
$$

but we may be able to accept any approximation $p$ that satisfies the condition

$$
\| f - p \| \leqslant \varepsilon ,
$$

where $\pmb \varepsilon$ is greater than $\pmb { \bar { \varepsilon } }$ It follows from the triangle inequality for norms that $p$ is an adequate approximation if the bound

$$
\left\| p - { \bar { p } } \right\| \leqslant \varepsilon - { \bar { \varepsilon } }
$$

is obtained.This inequality is useful because it gives some freedom in the approximating function that does not depend on $f .$ In particular we ask whether it allows $p$ to be in $\mathcal { P } _ { n }$ .Theorem 7.3 shows that the answer is affirmative if and only if the condition

$$
\begin{array} { r } { \big | \bar { c } _ { n + 1 } \big | ( \frac { 1 } { 2 } ) ^ { n } \big | \big | T _ { n + 1 } \big | \big | \leqslant \varepsilon - \bar { \varepsilon } } \end{array}
$$

holds.Therefore, because the norm of $T _ { n + 1 }$ is one, it is appropriate to test the inequality

$$
\left| { \bar { c } } _ { n + 1 } \right| \leqslant 2 ^ { n } ( \varepsilon - { \bar { \varepsilon } } ) .
$$

If it is satisfed, then $\bar { p }$ may be replaced by the approximation

$$
p = \bar { p } - \bar { c } _ { n + 1 } \bigl ( \frac 1 2 \bigr ) ^ { n } T _ { n + 1 } ,
$$

which is in $\mathcal { P } _ { n }$ . Hence we obtain the bound

$$
\| f - p \| \leqslant \bar { \varepsilon } + ( \frac { 1 } { 2 } ) ^ { n } \bigl | \bar { c } _ { n + 1 } \bigr | ,
$$

which may allow the procedure to be repeated to give a sufficiently accurate approximation in $\mathcal { P } _ { n - 1 }$

# 8.5 Minimax approximation on a discrete point set

It happens sometimes that it is not possible or not convenient to calculate the function $f$ in $\mathcal { C } [ \alpha , b ]$ ,that is to be approximated,at any point of the range $[ a , b ]$ Instead $f$ may be known on a set of points $\{ x _ { i } ; i =$ $1 , 2 , \ldots , m \}$ ,that are in ascending order

$$
a \leqslant x _ { 1 } < x _ { 2 } < . ~ . ~ < x _ { m } \leqslant b .
$$

In this case the function $p$ in $\mathscr { A }$ that minimizes the discrete maximum error

$$
\operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \big | f ( x _ { i } ) - p ( x _ { i } ) \big | , \qquad p \in \mathcal { A } ,
$$

may be required. If $\mathscr { A }$ is a linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and if $^ { m }$ is greater than the dimension of $\mathcal { A } _ { : }$ , then the exchange algorithm is an excellent procedure for calculating this approximation. We let each reference be a subset of $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ On each iteration the equations (8.4) are solved to define the trial approximation $p$ .Instead of expression (8.5),the bounds

$$
\left| h \right| \leqslant \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ^ { * } ( x _ { i } ) \right| \leqslant \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ( x _ { i } ) \right|
$$

hold, where $p ^ { * }$ is still the required approximation. Now the point that is brought into the reference is an element of the set $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ that satisfies the equation

$$
\left| f ( \eta ) - p ( \eta ) \right| = \operatorname* { m a x } _ { i = 1 , 2 , \ldots , m } \left| f ( x _ { i } ) - p ( x _ { i } ) \right| ,
$$

instead of equation (8.7). The procedure for changing the reference is the same as before.

One advantage of the calculation in the discrete case is that it is much easier to prove convergence.

# Theorem 8.2

Let $\mathcal { A }$ be a finite-dimensional subspace of $\mathcal { C } [ a , b ]$ that satisfies the Haar condition. Let $\{ x _ { i } ; i = 1 , 2 , \dots , m \}$ be a set of distinct points from $[ a , b ] ,$ ，where $^ { m }$ is not less than the dimension of $\mathcal { A } .$ For any $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] .$ , let the one-point exchange algorithm be applied to calculate the element of $\mathscr { A }$ that minimizes expression (8.3O). Then the required approximation to $f$ is obtained in a finite number of iterations.

Proof. The calculation ends if both parts of expression (8.31） are satisfied as equations. Otherwise the procedure for changing the reference causes the levelled reference errors to increase strictly monotonically.The number of different levelled reference errors is at most the number of different references,but this number is finite.Therefore the calculation of the algorithm is a finite process.□

It would not be sensible to obtain from the theorem an upper bound on the number of iterations of the algorithm, because the bound would be very pessimistic. Instead, the main value of the theorem is to show that the exchange algorithm terminates in an important special case, provided that one takes suitable precautions against the effects of computer rounding errors.

Because there is a need sometimes to solve minimax approximation calculations when $\mathcal { A }$ does not satisfy the Haar condition, it is useful to note that, in the discrete case, the calculation can be expressed as a linear programming problem. We let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\mathcal { A }$ ,and we express a general element of $\mathcal { A }$ in the form

$$
p = \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } .
$$

The least value of expression (8.30) is the smallest real number $\pmb \theta$ that satisfies the conditions

$$
- \theta \leqslant f ( x _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x _ { i } ) \leqslant \theta , \qquad i = 1 , 2 , \ldots , m ,
$$

for some values of the coefficients $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ . Therefore the variables of the linear programming calculation are $\pmb \theta$ and $\{ \lambda _ { j } ; ~ j =$ $0 , 1 , \ldots , n \}$ ，the objective function is $\pmb \theta$ ，and the constraints are the conditions (8.34).The final values of the variables $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ are the coefficients of the function in $\mathcal { A }$ that minimizes expression (8.30).

Basically the one-point exchange algorithm is a standard linear pro-gramming procedure for solving the dual version of the linear programming calculation that has just been mentioned. However, the Haar condition is useful, because it allows the point that leaves the reference to be found from the sign properties of the current error function,which gives a geometric point of view of the algorithm. Several advantages are lost if one supposes instead that minimax approximation is a special case of linear programming. In particular it is less easy to make use of the fact that the functions $f$ and $p$ are in $\mathcal { C } [ \alpha , b ] .$ ，which is important to the convergence theory of the next chapter.

# 8 Exercises

8.1 Let the exchange algorithm be applied to calculate the best approximation from $\mathcal { P } _ { n }$ to a function $f$ in ${ \mathcal { C } } [ a , b ]$ . Prove that the levelled reference error (8.10) is the modulus of the divided difference $f [ \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ]$ multiplied by a number that is independent of $f .$ In particular, show that when $n = 1$ the levelled reference error is the expression

8.2 The exchange algorithm is applied to calculate the best approximation from $\mathcal { P } _ { 1 }$ to a convex function in $\mathcal { C } [ \alpha , b ]$ .(The function $f$ is convex if, for any $\scriptstyle x _ { 0 }$ and $x _ { 1 }$ in $[ a , b ]$ and any $\pmb \theta$ in [0,1], the inequality

$$
f ( \theta x _ { 0 } + [ 1 - \theta ] \dot { x } _ { 1 } ) \leqslant \theta f ( x _ { 0 } ) + ( 1 - \theta ) f ( x _ { 1 } )
$$

is satisfied.) Show that, if the initial reference includes the points ${ \pmb \xi } _ { 0 } = { \pmb a }$ and $\pmb { \xi } _ { 2 } = \pmb { b }$ ,then at most two iterations are required.

Show that the best approximation from $\mathcal { P } _ { 2 }$ to the function $\{ f ( x ) = 1 4 4 / ( x + 2 )$ ； $0 \leqslant x \leqslant 6 \}$ is the quadratic $\{ p ^ { * } ( x ) = 6 9 -$ $2 0 x + 2 x ^ { 2 }$ ； $0 \leqslant x \leqslant 6 \}$ , and that the extreme values of the error function occur at the points $\xi _ { 0 } ^ { * } = 0$ ， $\pmb { \xi } _ { 1 } ^ { * } = 1$ ， $\pmb { \xi } _ { 2 } ^ { * } = 4$ and $\pmb { \xi } _ { 3 } ^ { \ast } = 6$ Let the exchange algorithm be used to calculate $p ^ { * }$ , and let the reference points of an iteration have the values ${ \xi _ { 0 } } = 0$ ， $\xi _ { 1 } = 1 + \alpha _ { : }$ ， $\pmb { \xi } _ { 2 } = 4 + \pmb { \beta }$ ， $\xi _ { 3 } = 6$ .Prove that, if $\pmb { \alpha }$ and $\beta$ are so small that one can neglect terms of order $\alpha ^ { 2 } , \alpha \beta$ and $\beta ^ { 2 }$ , then the function $\{ p ( { \pmb x } )$ ； $0 \leqslant x \leqslant 6 \}$ that satisfies equation (8.4) is equal to $p ^ { * }$

8.4 Let the iterations of the one-point exchange algorithm calculate the sequence of approximations $\{ p _ { k } ; ~ k = 1 , 2 , 3 , . . . \}$ from a linear space $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ . Construct an example to show that the errors {b $^ { \mathsf { c } } - p _ { k } \| _ { \infty }$ ； $k = 1 , 2 , 3 , \ldots \}$ do not always decrease monotonically.

8.5 Let $_ n$ be a non-negative integer. Show that the definition of the approximation $p$ to $f$ in Theorem 8.1 can be regarded as a linear operator from $\mathcal { C } [ - 1$ ,1] to ${ \mathcal { P } } _ { n }$ . Show also that, when $\pmb { n } = 2$ ,the ∞-norm of this operator has the value $\frac { 5 } { 3 }$

3.6 A polynomial approximation $\{ p ( x ) ; - 1 \leqslant x \leqslant 1 \}$ to the function $\{ f ( x ) = \ln \left( 1 + { \frac { 1 } { 2 } } x \right)$ ； $- 1 \leqslant x \leqslant 1 \}$ is required that satisfies the condition $\| f - p \| _ { \infty } { \leqslant } 0 . 0 1$ . One method of calculation is to take sufficient terms in the Taylor series expansion of $f$ about $\boldsymbol { x } = 0$ ， and then to reduce the degree of the polynomial by the telescoping procedure that is described in Section 8.4. Show that this method gives a polynomial of degree three.

8.7 Apply the discrete version of the one-point exchange algorithm to calculate the best approximation from $\mathcal { P } _ { 1 }$ to the following seven function values: $f ( 0 ) = 0 . 3$ ， $f ( 1 ) = 4 . 2$ ， $f ( 2 ) = 0 . 1$ ， $f ( 3 ) =$ 3.4, $f ( 4 ) = 5 . 7 , f ( 5 ) = 4 . 9$ ,and $f ( 6 ) = 5 . 7$ . Let the initial reference be the set of points $\{ 0 , 3 , 6 \}$

8.8 Let $\mathscr { A }$ be a linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and let the one-point exchange algorithm be applied to calculate the best approximation from $\mathscr { A }$ to a function $f$ in $\mathcal { C } [ \alpha , b ]$ Let $p _ { k }$ and $p _ { k + 1 }$ be the approximations to $f$ that are calculated by any two consecutive iterations of the algorithm, and let $\xi$ be any point that is in the references of both iterations. Prove that the differences $[ f ( \pmb { \xi } ) - p _ { k } ( \pmb { \xi } ) ]$ and $[ f ( \pmb { \xi } ) - p _ { \pmb { k } + 1 } ( \pmb { \xi } ) ]$ have the same sign.

Find an extension to the one-point exchange algorithm for the following calculation. Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition, let $\{ \zeta _ { i } ; i =$ $1 , 2 , \ldots , l \}$ be fixed points in $[ a , b ]$ where $1 \leqslant l \leqslant n$ ,and let $f$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ . Calculate the elenient of $\mathcal { A }$ that minimizes the error { $\| f - p \| _ { \infty } ; p \in \mathcal { A } \}$ subject to the interpolation conditions $\{ p ( \zeta _ { i } ) = f ( \zeta _ { i } ) ; i = 1 , 2 , . . . , l \}$ .One difficulty in the extension is finding a suitable rule for the change of reference.It is helpful to preserve the sign properties that are the subject of Exercise 8.8.

8.10 Investigate the following extension to the exchange algorithm for the case when $\mathcal { A }$ is an $( n + 1 )$ -dimensional subspace of ${ \mathcal { C } } [ a , b ]$ that need not satisfy the Haar condition. Let each reference contain $( n + 3 )$ points.Given the reference $\left\{ \xi _ { i } ; i = 0 , 1 , \ldots , \right.$ $n + 2 \}$ ,let $p _ { k }$ be the function in $\mathcal { A }$ that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 2 } \big | f ( \xi _ { i } ) - p ( \xi _ { i } ) \big | , \qquad p \in \mathcal { A } .
$$

Let $\xi _ { q }$ be the point such that ${ p } _ { k }$ also minimizes this expression when the range of $i$ excludes the value $i = q$ .The reference for the next iteration is obtained by replacing $\xi _ { q }$ by a number $\pmb { \eta }$ that satisfies the equation $\left| f ( \eta ) - p _ { k } ( \eta ) \right| = \| f - p _ { k } \| _ { \infty }$ . Because bounds of the form (8.5) are still valid, the procedure continues until the bounds show that sufficient accuracy is obtained.

# The convergence of the exchange algorithm

# 9.1 The increase in the levelled reference error

The method of proof of Theorem 8.2 depends so strongly on the fact that the number of different references is finite in the discrete case, that it is not useful for analysing the convergence properties of the one-point exchange algorithm that is described in Sections 8.1 and 8.2, where the purpose of the calculation is to obtain the element of $\mathscr { A }$ that minimizes the maximum value of the error function on the interval $a \leqslant x \leqslant b$ .We begin the analysis of the continuous case by finding an expression for the increase in the levelled reference error. This work gives an alternative proof of part of Theorem 7.7.

The levelled reference error is defined by the equations (8.4),but these equations also include the unknown coeficients of the approximation $p$ In order to remove this dependence, we let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\mathcal { A } ,$ ，and we eliminate the coefficients $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ from the equations

$$
f ( \xi _ { i } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i } ) = ( - 1 ) ^ { i } h , \qquad i = 0 , 1 , \dots , n + 1 .
$$

Because there are $( n + 2 )$ points in a reference, there exist multipliers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \} ,$ , not all zero, that satisfy the conditions

$$
\sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } \phi _ { j } ( \xi _ { i } ) = 0 , \qquad j = 0 , 1 , \ldots , n .
$$

Hence $h$ is defined by the equation

$$
\sum _ { i = 0 } ^ { n + 1 } ( - 1 ) ^ { i } \sigma _ { i } h = \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } f ( \xi _ { i } ) .
$$

We require the properties of the numbers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ that are given in the next theorem.

# Theorem 9.1

Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition, let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a set of points from $[ a , b ]$ that are in ascending order

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < \ldots < \xi _ { n + 1 } \leqslant b ,
$$

and let $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ be a set of real multipliers,that are not all zero,and that satisfy the equation

$$
\sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } p ( \xi _ { i } ) = 0 ,
$$

for all functions $p$ in $\mathcal { A }$ . Then every multiplier is non-zero,and their signs alternate.

Proof. Let $k$ be an integer in $[ 0 , n ]$ .Because of the fourth property of linear spaces that satisfy the Haar condition, given in Section 7.3,we may let $\pmb { p }$ be the element of $\mathscr { A }$ that is defined by the interpolation conditions

$$
p \left( \xi _ { i } \right) = 0 , \qquad i = 0 , 1 , \ldots , n + 1 , \qquad i \neq k , \qquad i \neq k + 1 ,
$$

and

$$
p ( \xi _ { k } ) = 1 .
$$

It follows from condition (1) of Section 7.3 that equation (9.6) gives all the zeros of the function $p$ Hence $p ( \xi _ { k + 1 } )$ is positive. Because the choice of $p$ and equation (9.5) imply the identity

$$
\sigma _ { k } + \sigma _ { k + 1 } p ( \xi _ { k + 1 } ) = 0 ,
$$

it follows that either $\pmb { \sigma } _ { \pmb { k } }$ and $\pmb { \sigma } _ { k + 1 }$ are both zero,or they are both non-zero and their signs are opposite. This statement holds for $k = 0 , 1 , \ldots , n$ Therefore the theorem is true.□

We deduce from the theorem and from equation (9.3) that the levelled reference error has the value

$$
\begin{array} { l } { { \displaystyle h \left( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { n + 1 } \right) = \Biggl \vert \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } f ( \xi _ { i } ) \Biggl \vert \Biggl / \sum _ { i = 0 } ^ { n + 1 } \left. \sigma _ { i } \right. } } \\ { { \displaystyle \qquad = \Biggl \vert \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } \lbrack f ( \xi _ { i } ) - p ( \xi _ { i } ) \rbrack \Biggl \vert \Biggl / \sum _ { i = 0 } ^ { n + 1 } \left. \sigma _ { i } \right. } , } \end{array}
$$

where the last line depends on equation (9.5). Suitable values of the multipliers $\{ \sigma _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ may be obtained from the co-factors of the matrix of the equations (9.2). We make the definition

$$
\begin{array} { l } { { \sigma _ { i } = ( - 1 ) ^ { i } \operatorname* { d e t } \left[ \Phi ( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { i - 1 } , \xi _ { i + 1 } , \dots , \xi _ { n + 1 } ) \right] , } } \\ { { \qquad i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

where $\Phi ( \zeta _ { 0 } , \zeta _ { 1 } , \ldots , \zeta _ { n } )$ is the square matrix whose elements are the numbers $\{ \phi _ { j } ( \zeta _ { i } ) ; i = 0 , 1 , \ldots , n ; j = 0 , 1 , \ldots , n \}$ .The fourth property of Section 7.3 states that each $\pmb { \sigma _ { i } }$ is non-zero. Thus the first line of equation (9.9) expresses the levelled reference error in a way that is independent of $p$

In order to relate $h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } )$ to $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ , where we are using the notation of Section 8.1, we let $\{ \sigma _ { i } ^ { + } ; i = 0 , 1 , \ldots , n + 1 \}$ be the numbers that are obtained by replacing the old reference points by the new reference points in the definition (9.1O). Therefore equation (9.9) gives the value

$$
h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \ldots , \xi _ { n + 1 } ^ { + } ) = \overbrace { \vphantom { \int _ { 0 } ^ { 0 } } \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } ^ { + } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] } ^ { \left| \sum _ { i = 0 } ^ { n + 1 } \sigma _ { i } ^ { + } \left[ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right] \right| } ,
$$

where $p$ is any element of $\mathcal { A }$ We let $p$ be the approximation that is defined by equation (8.4),and we recall that the new reference satisfies the sign conditions (8.12). It follows from Theorem 9.1 that the numerator of expression (9.11) has the value

$$
\sum _ { i = 0 } ^ { n + 1 } \big | \sigma _ { i } ^ { + } [ f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) ] \big | .
$$

Now, in the one-point exchange algorithm, $\left| f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right|$ is equal to $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ,unless $\xi _ { i } ^ { + }$ is the point $\pmb { \eta }$ that satisfies equation (8.7), in which case $\left| f ( \xi _ { i } ^ { + } ) - p ( \xi _ { i } ^ { + } ) \right|$ is equal to $\| f - p \|$ . We let $\xi _ { r } ^ { + }$ be the point of the new reference that is equal to $\pmb { \eta }$ .Hence the new levelled reference error is the expression

$$
\begin{array} { l } { { \displaystyle h ( \xi _ { 0 } ^ { + } , \xi _ { 1 } ^ { + } , \dots , \xi _ { n + 1 } ^ { + } ) } \ ~ } \\ { { \displaystyle h ( \xi _ { 0 } , \xi _ { 1 } , \dots , \xi _ { n + 1 } ) \sum _ { i = 0 \atop i \neq r } ^ { n + 1 } \left| { \boldsymbol \sigma } _ { i } ^ { + } \right| + \left\| { \boldsymbol f } - { \boldsymbol p } \right\| \left| { \boldsymbol \sigma } _ { r } ^ { + } \right| } \ ~ } \\ { { \displaystyle ~ = \frac { h + r } { \sum _ { i = 0 } ^ { n + 1 } \left| { \boldsymbol \sigma } _ { i } ^ { + } \right| } } . } \end{array}
$$

This result provides the alternative proof of the statement that the levelled reference errors increase, if the calculation of the exchange algorithm continues because the right-hand side of expression (8.5) is greater than the left-hand side.

# 9.2 Proof of convergence

It is straightforward to deduce from equation (9.13) that the functions $p$ in $\mathcal { A } ,$ ， that are calculated by the iterations of the exchange algorithm, converge to the best minimax approximation from $\mathscr { A }$ to $f ,$ provided that each $\left| \sigma _ { r } ^ { + } \right|$ is bounded away from zero. This condition is satisfied, but in order to prove it we require the technical result that is given in the next theorem.

# Theorem 9.2

Let $\mathscr { A }$ be an $( n + 1 )$ -dimensional subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ that satisfies the Haar condition,and,for any $f$ in $\mathcal { C } [ a , b ] .$ , let the one-point exchange algorithm be applied to calculate the best approximation from $\mathscr { A }$ to $f .$ Then，for any initial reference $\{ \xi _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ ，there exists a positive number $\pmb { \delta }$ ,such that on each iteration the points of the reference satisfy the bounds

$$
\xi _ { i + 1 } - \xi _ { i } \geqslant \delta , \qquad i = 0 , 1 , \ldots , n .
$$

Proof. The method that is used to change the reference ensures that the points of each reference are distinct. Therefore it is sufficient to rule out the possibility that, for a subsequence of references, two points tend to become coincident. We suppose that this happens and deduce a contradiction. Because all references are in a closed and bounded subset of $\mathcal { R } ^ { n + 2 }$ ，the hypothesis implies that there is a subsequence of the subsequence that converges to a set $\{ \bar { \xi } _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ that contains at most $( n + 1 )$ distinct points.

Let $\left| h _ { k } \right|$ be the levelled reference error of the kth iteration. Although $\lvert h _ { 1 } \rvert \mathrm { m a y }$ be zero,it follows from inequality (8.11) that $\left| h _ { 2 } \right|$ is positive, and that the sequence $\{ | h _ { k } | ; k = 1 , 2 , 3 , . . . \}$ increases strictly monotonically. The contradiction that is obtained from the set $\{ \bar { \xi } _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ is that a large value of $k$ exists, such that $\left| h _ { k } \right|$ is less than $\left| h _ { 2 } \right|$

Because the Haar condition implies that there is a function in $\mathcal { A }$ that interpolates $f$ at any $( n + 1 )$ points of $[ a , b ] ,$ we may let $\bar { p }$ be a function in $\mathcal { A }$ that satisfies the equations

$$
\bar { p } ( \bar { \xi } _ { i } ) = f ( \bar { \xi } _ { i } ) , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

It is important to note that $\bar { p }$ does not depend on the iteration number. Because $f$ and $\bar { p }$ are both in $\mathcal { C } [ \alpha , b ] .$ ,there exists a positive number $\pmb \varepsilon$ such that the inequality

$$
\left| ( f - { \bar { p } } ) ( x _ { 2 } ) - ( f - { \bar { p } } ) ( x _ { 1 } ) \right| < \left| h _ { 2 } \right|
$$

holds, where $x _ { 1 }$ and $x _ { 2 }$ are any two points of $[ a , b ]$ that satisfy the bound

$$
\left| x _ { 1 } - x _ { 2 } \right| < \varepsilon .
$$

We let $\pmb { k }$ be the number of an iteration whose reference satisfies the conditions

$$
\left| \xi _ { i } - { \bar { \xi } } _ { i } \right| < \varepsilon , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

Therefore, we may let $x _ { 1 } = \xi _ { i }$ and $x _ { 2 } = \bar { \xi } _ { i }$ in expression (9.16), which, because of equation (9.15), gives the inequality

$$
| f ( \xi _ { i } ) - \bar { p } ( \xi _ { i } ) | < | h _ { 2 } | , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

It follows that the bound

$$
\operatorname* { m i n } _ { p \in \mathcal { A } } \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \left| f ( \xi _ { i } ) - p ( \xi _ { i } ) \right| < \left| h _ { 2 } \right|
$$

is obtained. The required contradiction is a consequence of the fact that the left-hand side of this expression is the definition of $\left| h _ { k } \right|$ □

In order to prove that $\left| \sigma _ { r } ^ { + } \right|$ is bounded away from zero, we let $\pmb { \delta }$ be the number that is mentioned in the statement of Theorem 9.2,and we let $\mathcal { Z } = \left\{ { z } \right\}$ be the subset of vectors in $\mathcal { R } ^ { n + 1 }$ whose components, $\{ \zeta _ { i } ; i =$ $0 , 1 , \ldots , n \}$ say, satisfy the conditions

$$
a \leqslant \zeta _ { 0 } \leqslant \zeta _ { 1 } \leqslant . ~ . ~ \leqslant \zeta _ { n } \leqslant b ,
$$

and

$$
\zeta _ { i } \cdots \zeta _ { i - 1 } \geqslant \delta , \qquad i = 1 , 2 , \ldots , n .
$$

Because $\mathcal { Z }$ is compact,and because the functions in $\mathscr { A }$ are continuous, the expression

$$
\begin{array} { r l r } { \big \vert \mathbf { d e t } \Phi ( \zeta _ { 0 } , \zeta _ { 1 } , \ldots , \zeta _ { n } ) \big \vert , } & { { } } & { z \in \mathcal { Z } , } \end{array}
$$

achieves its minimum value, $^ { m }$ say, where $\Phi$ is defined immediately after equation (9.1O). It follows from the fourth property of Section 7.3 and from Theorem 9.2, that the inequality

$$
| \sigma _ { i } | \geqslant m > 0 , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

is satisfied on every iteration. Moreover, the definition (9.10) implies a constant upper bound of the form

$$
\left| \sigma _ { i } \right| \leqslant M , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

We are now ready to use equation (9.13) to deduce the convergence of the exchange algorithm.

# Theorem 9.3

Let the conditions of Theorem 9.2 be satisfied,and let $p _ { k }$ be the function in $\mathscr { A }$ that is calculated by the kth iteration of the exchange algorithm. Then the sequence $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ converges to the best minimax approximation from $\pmb { \mathcal { A } }$ to $f , p ^ { * }$ say.

Proof. Expressons (9.13),(9.24) and (9.25) imply the relation

$$
\left| h _ { k + 1 } \right| \geqslant \frac { ( n + 1 ) M \vert h _ { k } \vert + m \| f - p _ { k } \| } { ( n + 1 ) M + m } .
$$

Subtracting $\left| h _ { k } \right|$ from each side gives the bound

$$
\left| h _ { k + 1 } \right| - \left| h _ { k } \right| \geqslant \frac { m } { ( n + 1 ) M + m } \left[ \left\| f - p _ { k } \right\| - \left| h _ { k } \right| \right] .
$$

The sequence $\{ | h _ { k } | ; k = 1 , 2 , 3 , . . . \}$ increases monotonically and is bounded above by the condition

$$
\left| h _ { k } \right| \leqslant \left\| f - p ^ { * } \right\| \leqslant \left\| f - p _ { k } \right\| .
$$

Therefore the left-hand side of expression (9.27) tends to zero.Because inequality (9.28) shows that $[ \| f - p _ { k } \| - | h _ { k } | ]$ is non-negative,it follows that the right-hand side of expression (9.27) also tends to zero. Thus, using inequality (9.28) once more,we find the limit

$$
\operatorname* { l i m } _ { k \to \infty } \| f - p _ { k } \| = \| f - p ^ { * } \| .
$$

Hence the functions $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ are bounded,and therefore they remain in a compact subset of $\mathcal { A }$ ，Therefore the sequence $\{ p _ { k } ; k =$ $1 , 2 , 3 , \ldots 3$ has at least one limit point. Equation (9.29) shows that each limit point is a best approximation, while Theorem 7.6 states that the best approximation is unique. It follows,by using compactness again, that the sequence $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$ converges to $p ^ { * }$ .□

# 9.3 Properties of the point that is brought into the reference

There are many examples in numerical analysis of procedures that always converge, but whose rate of convergence is so slow that the procedure is hardly ever useful. The calculation of Section 8.3, however, shows that the exchange algorithm can perform very well. The work of the next two sections explains the excellent convergence properties of the one-point exchange algorithm，assuming some differentiability and regularity properties that are often achieved in practice.

We continue to let $p ^ { * }$ be the best approximation to $f$ in $\mathcal { C } [ a , b ]$ from an $( n + 1 )$ -dimensional linear space $\mathcal { A }$ that satisfies the Haar condition. We assume that the maximum value of the modulus of the error function

$$
e ^ { * } ( x ) = f ( x ) - p ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

occurs at only $( n + 2 )$ points of $[ a , b ]$ , namely $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \dots , n + 1 \}$ . We assume that all functions are twice continuously differentiable. If $\boldsymbol { \xi } _ { 0 } ^ { * }$ is at $^ { a }$ ,we require the first derivative $e ^ { * \prime } ( a )$ to be non-zero, and, if $\xi _ { n + 1 } ^ { * }$ is at $^ { b }$ ，

we require $e ^ { * \prime } ( b )$ to be non-zero. For all other points in the set $\{ \xi _ { i } ^ { * } ; i =$ $0 , 1 , \ldots , n + 1 \nmid$ ， we require the second derivative $e ^ { * \prime \prime } ( \xi _ { i } ^ { * } )$ to be nonzero.

We let $\{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \} , \left| h _ { k } \right|$ and $p _ { k }$ be the reference points, the levelled reference error and the calculated approximation of the kth iteration of the exchange algorithm. Therefore the equations

$$
| f ( \xi _ { i k } ) - p _ { k } ( \xi _ { i k } ) | = | h _ { k } | , \qquad i = 0 , 1 , \ldots , n + 1 ,
$$

are satisfied. Theorem 9.3 shows that,as $k$ tends to infinity, $p _ { k }$ and $\left| h _ { k } \right|$ tend to $p ^ { * }$ and $\| f - p ^ { * } \|$ respectively,and Theorem 9.2 states that the points of each reference stay apart.It follows from the first assumption of the previous paragraph and from equation (9.31) that the sequence of references $[ \{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ ； $k = 1 , 2 , 3 , \ldots ]$ converges to the set $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ . The following theorem gives some properties of the way in which each reference is changed. These properties are used in Section 9.4 to bound the rate of convergence of the sequence of approximations $\{ p _ { k } ; k = 1 , 2 , 3 , . . . \}$

# Theorem 9.4

Given the assumptions and using the notation that are stated in the previous two paragraphs, there exists an integer $\pmb { K }$ and a constant $c$ such that the following conditions are obtained for all $k \geqslant K .$ Let $\xi _ { q k + 1 } =$ $\eta$ be the point that is brought into the reference by the kth iteration of the exchange algorithm. If $\xi _ { q } ^ { * }$ is one of the end points of the interval $[ a , b ] .$ ， then $\xi _ { q k + 1 }$ is equal to ${ \xi } _ { q } ^ { * }$ . Otherwise the bound

$$
\left| \xi _ { q } ^ { * } - \xi _ { q k + 1 } \right| \leqslant c \left\| p ^ { * } - p _ { k } \right\|
$$

is satisfied.

Proof. Because the sequence of references converges to $\{ \xi _ { i } ^ { * } ; i =$ $0 , 1 , \ldots , n + 1 \}$ , we may choose $\pmb { K }$ so that, for all $k \geqslant K ,$ ，the point that leaves the reference of the kth iteration to make room for $\xi _ { q k + 1 } = \eta$ is the point $\xi _ { q k }$ .Further,if $e ^ { * \prime } ( a )$ is non-zero, we may also require $\pmb { K }$ to satisfy the condition that,for all $k \geqslant K ,$ ,there are no stationary points of the error function $\{ e _ { k } ( x ) = f ( x ) - p _ { k } ( x )$ $a \leqslant x \leqslant b \}$ in a small fixed neighbourhood of $^ a$ Hence, if $\xi _ { q } ^ { * } = a$ ,then the point $\xi _ { q k + 1 }$ is equal to ${ \xi } _ { q } ^ { * }$ for sufficiently large $k$ ，A similar result holds if $\xi _ { q } ^ { * } = b$ In all other cases $\xi _ { q k + 1 }$ is the abscissa of an extreme point of the error function $e _ { k }$ , that is close to ${ \xi } _ { q } ^ { * }$ when $k$ is large.It remains to prove that in this case condition (9.32) is obtained.

The conditions of the theorem imply that there exist positive constants $\pmb \varepsilon$ and $^ d$ such that, if $\pmb { \xi } _ { q } ^ { * }$ is one of the points $\{ \xi _ { i } ^ { * } ; i = 0 , 1 , \ldots , n + 1 \}$ at which $e ^ { * }$ is stationary, then the inequality

$$
\begin{array} { r } { | e ^ { * \prime \prime } ( x ) | \geqslant d , \qquad \xi _ { q } ^ { * } - \varepsilon \leqslant x \leqslant \xi _ { q } ^ { * } + \varepsilon , } \end{array}
$$

holds. We increase $\kappa$ if necessary so that, for $k \geq K$ ， the point $\xi _ { q k + 1 }$ is always in the interval $[ \xi _ { q } ^ { * } - \varepsilon , \xi _ { q } ^ { * } + \varepsilon ]$ . Therefore, because $e ^ { * \prime } ( \xi _ { q } ^ { * } )$ is zero, expression (9.33) gives the bound

$$
\left| e ^ { * \prime } ( \xi _ { q k + 1 } ) \right| \geqslant d | \xi _ { q } ^ { * } - \xi _ { q k + 1 } | .
$$

The definitions of $\xi _ { q k + 1 } , e ^ { * }$ and $e _ { k }$ imply that the left-hand side of this inequality has the value

$$
\left| e ^ { \ast \prime } ( \xi _ { q k + 1 } ) - e _ { k } ^ { \prime } ( \xi _ { q k + 1 } ) \right| = \big | p ^ { \ast \prime } ( \xi _ { q k + 1 } ) - p _ { k } ^ { \prime } ( \xi _ { q k + 1 } ) \big | .
$$

Hence the condition

$$
\big | \xi _ { q } ^ { * } - \xi _ { q k + 1 } \big | \leqslant ( 1 / d ) \big | \big | p ^ { * \prime } - p _ { k } ^ { \prime } \big | \big |
$$

is satisfied. Because $\pmb { \mathcal { A } }$ is a finite-dimensional linear space, there exists a constant $\pmb { D }$ such that the inequality

$$
\| p ^ { \prime } \| { \leqslant } D \| p \| , \qquad p \in { \mathcal { A } } ,
$$

holds. It follows from condition (9.36) that the theorem is true, where $^ { c }$ is the number $\scriptstyle { D / d }$ □

In order to apply the theorem,it is necessary to relate the difference $( p ^ { * } - p _ { k } )$ to the positions of the reference points $\{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ The following result is suitable.

# Theorem 9.5

There exists a constant $\bar { c }$ such that the inequality

$$
\left\| p ^ { * } - p _ { k } \right\| \leqslant \bar { c } \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \left| e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i k } ) \right|
$$

is satisfied, where the notation is defined earlier in this section.

Proof. We let $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ be a basis of $\scriptstyle { \mathcal { A } }$ we express $p ^ { * }$ and ${ p } _ { k }$ in the form

$$
\begin{array} { l l } { { p ^ { * } ( x ) = \displaystyle \sum _ { j = 0 } ^ { n } \lambda _ { j } ^ { * } \phi _ { j } ( x ) , } } & { { \quad a \leqslant x \leqslant b } } \\ { { } } & { { } } \\ { { p _ { k } ( x ) = \displaystyle \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( x ) , } } & { { \quad a \leqslant x \leqslant b } } \end{array} \biggr \} ,
$$

and we recall that the numbers $\{ \lambda _ { j } ; j = 0 , 1 , \ldots , n \}$ and $h _ { k }$ are defined by the equations

$$
f ( \xi _ { i k } ) - \sum _ { j = 0 } ^ { n } \lambda _ { j } \phi _ { j } ( \xi _ { i k } ) = ( - 1 ) ^ { i } h _ { k } , \qquad i = 0 , 1 , \ldots , n + 1 .
$$

The matrix of this system is bounded away from singularity for allvalues of $k$ , because,due to the definition (9.10),the modulus of the determinant of the matrix has the value

$$
\left| \sum _ { i = 0 } ^ { n + 1 } { ( - 1 ) ^ { i } \sigma _ { i } } \right| = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| \geqslant ( n + 2 ) m ,
$$

where the last two steps depend on Theorem 9.1 and inequality (9.24). Therefore,if we define the numbers $\{ \alpha _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ by the equations

$$
\alpha _ { i } - \sum _ { j = 0 } ^ { n } { \bf \Phi } ( \lambda _ { j } - \lambda _ { j } ^ { * } ) \phi _ { j } ( \xi _ { i k } ) = { \bf \Phi } ( - 1 ) ^ { i } ( h _ { k } - h ^ { * } ) , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

where $h ^ { * }$ is the minimax error of the approximation $p ^ { * }$ that satisfies the conditions

$$
f ( \xi _ { i } ^ { * } ) - p ^ { * } ( \xi _ { i } ^ { * } ) = ( - 1 ) ^ { i } h ^ { * } , \qquad i = 0 , 1 , \dots , n + 1 ,
$$

and if we take the point of view that the system (9.42) is used to express the differences $\{ \lambda _ { j } - \lambda _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ and $( h _ { k } - h ^ { * } )$ in terms of the numbers $\{ \alpha _ { i } ; i = 0 , 1 , \ldots , n + 1 \}$ , it follows that the bound

$$
\operatorname* { m a x } _ { j = 0 , 1 , \dots , n } \left| \lambda _ { j } - \lambda _ { j } ^ { * } \right| \leqslant \bar { d } \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \left| \alpha _ { i } \right|
$$

is satisfied for some constant $\bar { d } .$ Equation (9.39), (9.40),(9.42) and (9.43) imply that $\pmb { \alpha } _ { i }$ has the vaiue

$$
\begin{array} { l } { { \alpha _ { i } = f ( \xi _ { i k } ) - p ^ { * } ( \xi _ { i k } ) - ( - 1 ) ^ { i } h ^ { * } } } \\ { { \mathrm { } = e ^ { * } ( \xi _ { i k } ) - e ^ { * } ( \xi _ { i } ^ { * } ) , \qquad i = 0 , 1 , \dots , n + 1 , } } \end{array}
$$

and expression (9.39) gives the bound

$$
\| p ^ { * } - p _ { k } \| _ { \infty } \leqslant \sum _ { j = 0 } ^ { n } \left| \lambda _ { j } - \lambda _ { j } ^ { * } \right| \| \phi _ { j } \| _ { \infty } .
$$

Therefore,inequality (9.38) is a consequence of condition (9.44), where $\bar { c }$ has the value

$$
\bar { c } = \bar { d } \sum _ { j = 0 } ^ { n } \| \phi _ { j } \| _ { \infty } .
$$

The theorem is proved.

# 9.4 Second-order convergence

In order to prove that the one-point exchange algorithm has a second-order rate of convergence,we note that Theorem 9.4 and the form of $e ^ { * }$ imply that, for $k \geqslant K ,$ ，the difference $\left| e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) \right|$ is bounded above by a multiple of $\| p ^ { * } - p _ { k } \| ^ { 2 }$ . Thus,for sufficiently large $k$ ， each iteration reduces one of the terms that occurs on the right-hand side of inequality (9.38). Because each iteration changes only one reference point,as many as $( n + 2 )$ iterations may be necessary to make a substantial improvement to the calculated approximations. Even then a better approximation need not be obtained, because of the remote possibility that at the beginning of the sequence of iterations the calculated approximation is equal to $p ^ { * }$ , but this situation is not recognized because the reference is wrong. Therefore it is not possible to prove that the sequence $\{ \| p ^ { * } - p _ { k } \|$ ； $k = 1 , 2 , 3 , \ldots \}$ converges to zero in a regular way. Instead, the following theorem gives a useful property of the changes that are made to the references.

# Theorem 9.6

Let the conditions of Theorem 9.4 be satisfed. There exists an integer $\kappa$ and a constant $\beta$ such that the sequence $\left\{ \rho _ { k } ; k = K , K + 1 , \ldots \right\}$ converges monotonically to zero, and such that the inequality

$$
\rho _ { k + n + 2 } \leqslant \beta \rho _ { k } ^ { 2 } , \qquad k \geqslant K ,
$$

is satisfied, where $\rho _ { k }$ is the expression

$$
\rho _ { k } = \operatorname* { m a x } _ { i = 0 , 1 , \ldots , n + 1 } \big | e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i k } ) \big | .
$$

Proof. The discussion that is given immediately before Theorem 9.4 shows that the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ converges to zero. In order to prove that the sequence is monotonic, we let $K , c$ and $\bar { c }$ have the values that are given in Theorems 9.4 and 9.5,and we increase $\pmb { K }$ if necessary so that the bound

$$
( c \bar { c } ) ^ { 2 } \rho _ { k } \| e ^ { * \prime \prime } \| _ { \infty } \leqslant 2 , \qquad k \geqslant K ,
$$

is obtained. The definition (9.49) implies the relation

$$
\rho _ { k + 1 } \leqslant \operatorname* { m a x } { [ \rho _ { k } , | e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) | ] } ,
$$

where $\xi _ { q k + 1 }$ is still the point that is brought into the reference by the kth iteration of the exchange algorithm.Therefore, if ${ \xi } _ { q } ^ { * }$ is an end point of the interval $[ a , b ]$ ，the condition $\rho _ { k + 1 } \leqslant \rho _ { k }$ is an immediate consequence of Theorem 9.4. Otherwise,we use the Taylor series expansion of the function $\{ e ^ { * } ( x ) ; a \leqslant x \leqslant b \}$ about the point $x = \xi _ { q } ^ { * }$ to deduce the inequality

$$
\begin{array} { r l } & { \| e ^ { * } ( \xi _ { q } ^ { * } ) - e ^ { * } ( \xi _ { q k + 1 } ) \| \leqslant \frac { 1 } { 2 } ( \xi _ { q } ^ { * } - \xi _ { q k + 1 } ) ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \frac { 1 } { 2 } c ^ { 2 } \| p ^ { * } - p _ { k } \| ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \frac { 1 } { 2 } ( c \bar { c } ) ^ { 2 } \rho _ { k } ^ { 2 } \| e ^ { * \prime \prime } \| _ { \infty } } \\ & { \qquad \leqslant \rho _ { k } , } \end{array}
$$

Therefore the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ does decrease monotonically.

In order to establish inequality (9.48), we let $k$ be an integer that is not less than $\kappa$ ，and we let $q ( j )$ be the index of the point that leaves the reference $\{ \xi _ { i j } ; i = 0 , 1 , \ldots , n + 1 \}$ on the $j _ { \mathbf { \ L } } ( \mathbf { h }$ iteration. Because the set $\{ q ( j ) ; j = k , k + 1 , \ldots , k + n + 2 \}$ contains $( n + 3 )$ terms,and because at most $( n + 2 )$ of these terms are different, we let $\boldsymbol { r }$ and $\pmb { s }$ be integers that satisfy the conditions $k \leqslant r < s \leqslant k + n + 2$ and $q ( r ) = q ( s ) = t ,$ ,say,and we reduce $\pmb { s }$ if necessary so that the integer $t$ does not occur in the set $\{ q ( j ) ; j = r + 1 , r + 2 , \ldots , s - 1 \}$ .The point $\xi _ { t } ^ { * }$ is not equal to $^ { a }$ or $^ { b }$ ， because,if it were, then Theorem 9.4 would imply that the sth iteration would fail to change the reference.

We consider the difference $( \xi _ { t s + 1 } - \xi _ { t s } )$ ，which is the change to a reference point on the sth iteration. Because $\xi _ { t s }$ is equal to $\xi _ { t r + 1 }$ ,expressions (9.32), (9.38) and (9.49) give the bound

$$
\begin{array} { r l } & { \left| { \xi _ { t s + 1 } - \xi _ { t s } } \right| \leqslant c [ \| p ^ { * } - p _ { s } \| + \| p ^ { * } - p _ { r } \| ] } \\ & { \qquad \leqslant c \bar { c } ( \rho _ { s } + \rho _ { r } ) } \\ & { \qquad \leqslant 2 c \bar { c } \rho _ { k } . } \end{array}
$$

We make use of the fact that $\xi _ { t s + 1 }$ is the abscissa of an extremum of the error function $\{ e _ { s } ( x ) = f ( x ) - p _ { s } ( x )$ ； $a \leqslant x \leqslant b \}$ to deduce the inequality

$$
\begin{array} { r } { \big | e _ { s } ( \xi _ { t s + 1 } ) - e _ { s } ( \xi _ { t s } ) \big | \leqslant \frac { 1 } { 2 } \bar { \beta } \big | \xi _ { t s + 1 } - \xi _ { t s } \big | ^ { 2 } , } \end{array}
$$

where $\bar { \beta }$ is a constant upper bound on the norms $\{ \| e _ { j } ^ { \prime \prime } \| _ { \infty } ; j \geqslant K \}$ . Because of the sign conditions that are satisfied when the exchange algorithm adjusts a reference, the equation

$$
| e _ { s } ( \xi _ { t s + 1 } ) - e _ { s } ( \xi _ { t s } ) | . = \| e _ { s } \| _ { \infty } - | h _ { s } |
$$

holds, and we recall that $\| e _ { s } \| _ { \infty }$ is an upper bound on the least maximum error $\| e ^ { * } \| _ { \infty }$ . Therefore, expressions (9.53), (9.54) and (9.55) imply the relation

$$
\big \| e ^ { * } \big \| _ { \infty } - \big | h _ { s } \big | \leqslant 2 \bar { \beta } ( c \bar { c } \rho _ { k } ) ^ { 2 } .
$$

The final part of the proof depends on the value of $\left| h _ { s } \right|$ that can be obtained from equation (9.9), when $\pmb { p }$ is the polynomial $p ^ { * }$ . By increasing $\pmb { K }$ if necessary, so that for all $\pmb { s } \geqslant \pmb { K }$ and for $i = 0 , 1 , \ldots , n + 1$ ,the signs of $e ^ { * } ( \xi _ { i s } )$ and $e ^ { * } ( \xi _ { i } ^ { * } )$ are the same, we find the value

$$
\begin{array} { l } { { \displaystyle \left| h _ { s } \right| = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| \left| e ^ { * } ( \xi _ { i s } ) \right| \bigg / \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| } } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| [ \left| e ^ { * } ( \xi _ { i } ^ { * } ) \right| - \left| e ^ { * } ( \xi _ { i } ^ { * } ) - e ^ { * } ( \xi _ { i s } ) \right| ] \bigg / \sum _ { i = 0 } ^ { n + 1 } \left| \sigma _ { i } \right| } } \\ { { \displaystyle ~ \leqslant \left\| e ^ { * } \right\| _ { \infty } - \rho _ { s } m / [ ( n + 1 ) M + m ] } , } \end{array}
$$

where the second line depends on the properties of $e ^ { * }$ ,and where the last line depends on the definition (9.49) and on the bounds (9.24) and(9.25). Because expressons (9.56) and (9.57) imply the inequality

$$
\rho _ { s } \leqslant 2 [ ( n + 1 ) M + m ] \bar { \beta } ( c \bar { c } \rho _ { k } ) ^ { 2 } / m ,
$$

and because the sequence $\{ \rho _ { k } ; k = K , K + 1 , \ldots \}$ decreases monotonically, the theorem is proved.□

Theorems 9.5 and 9.6 show that the differences $\{ \| p ^ { * } - p _ { k } \|$ ； $k = K ,$ $\kappa +$ $1 , \ldots . \}$ are less than the corresponding terms of the sequence $\{ \bar { c } \rho _ { k } ; k =$ $K , K + 1 , \ldots \} ,$ . which converges to zero monotonically at an $( n + 2 )$ -step quadratic rate. This is about the strongest result that can be expected from an algorithm that changes only one reference point on each iteration, and it explains the rate of convergence that is achieved.

# 9 Exercises

9.1 Let the exchange algorithm be used to calculate the best approximation to the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant 1 \}$ by a multiple of the function $\{ p ( x ) = x ; 0 \leqslant x \leqslant 1 \}$ . Let $\xi _ { 0 1 }$ be any interior point of the interval [0,1] and let $\xi _ { 1 1 } = 1$ ,where $\left\{ \xi _ { 0 k } , \xi _ { 1 k } \right\}$ is the reference of the kth iteration. Prove that $\xi _ { 1 k } = 1$ for all values of $k$ ,and that the sequence $\{ \xi _ { 0 k } ; k = 1 , 2 , 3 , . . . \}$ converges to the limit $\xi _ { 0 } ^ { * } =$ $\sqrt { 2 } - 1$ at a quadratic rate, which means that there is a constant $^ { c }$ such that the condition

$$
\begin{array} { r } { \big | \xi _ { 0 k + 1 } - \xi ^ { * } \big | \leqslant c \big | \xi _ { 0 k } - \xi ^ { * } \big | ^ { 2 } , \qquad k = 1 , 2 , 3 , \ldots , } \end{array}
$$

is satisfied.

9.2 Let $f$ be a function in $\mathcal { C } ^ { ( n + 1 ) } [ a , b ] ,$ let $\mathscr { A }$ be the space ${ \mathcal { P } } _ { n }$ , and let $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ be the levelled reference error that is defined in Section 8.1. Deduce from Theorem 4.2 that there exists a constant $^ c$ such that the bound

$$
h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } ) \leqslant c \operatorname* { m i n } _ { i = 0 , 1 , \ldots , n } \big | \xi _ { i + 1 } - \xi _ { i } \big | \big \| f ^ { ( n + 1 ) } \big \| _ { \infty }
$$

is obtained, which provides an easy proof of Theorem 9.2 in this special case.

9.3 Deduce from the proof of Theorem 9.3 that there exists a constant $\pmb \theta$ in the open interval (O,1) such that the inequality

$$
[ \left\| { f - p ^ { * } } \right\| - | h _ { k + 1 } | ] \leqslant \theta [ \left\| { f - p ^ { * } } \right\| - | h _ { k } | ]
$$

holds on every iteration of the one-point exchange algorithm.

9.4 Let $\mathscr { A }$ be a finite-dimensional linear subspace of ${ \mathcal { C } } [ a , b ]$ that satisfies the Haar condition, and let $f$ be any function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$

Prove that there exists a positive number $^ { c }$ such that the inequality

$$
\| f - p \| _ { \infty } - \| f - p ^ { * } \| _ { \infty } \geqslant c \| p - p ^ { * } \| _ { \infty }
$$

is satisfied for all $\pmb { p }$ in $\mathcal { A }$ ,where $p ^ { * }$ is the best approximation from $\mathcal { A }$ to $f .$

Section 8.2 mentions several procedures for changing the reference of the exchange algorithm on each iteration.Let the version be used that adjusts every reference point to a local extremum of the error function $\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \}$ , subject to the conditions (8.12) and (8.13),and where one of the points of the new reference is a solution $\pmb { \eta }$ of equation (8.7). Prove that, if the conditions of Theorem 9.4 are satisfied, then this version of the exchange algorithm gives the quadratic rate of convergence

$$
\| p ^ { * } - p _ { k + 1 } \| \leqslant \mu \| p ^ { * } - p _ { k } \| ^ { 2 } , \qquad k = 1 , 2 , 3 , \ldots ,
$$

where $\pmb { \mu }$ is a constant.

9.6 Let $\mathcal { A }$ be an $( n + 1 )$ -dimensional linear subspace of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ,and let $f$ be a function in ${ \mathcal { C } } [ a , b ]$ . Let $[ \{ \xi _ { i k } ; i = 0 , 1 , \ldots , n + 1 \}$ ； $k =$ $1 , 2 , 3 , \ldots ]$ be an infinite sequence of references such that the numbers

$$
\big | h _ { k } \big | = \operatorname* { m i n } _ { p \in \mathcal { A } } \operatorname* { m a x } _ { i = 0 , 1 , \dots , n + 1 } \big | f ( \xi _ { i k } ) - p ( \xi _ { i k } ) \big | , \qquad k = 1 , 2 , 3 , \dots ,
$$

increase strictly monotonically. By considering the case when $\mathscr { A }$ is the two-dimensional space that is spanned by the functions $\{ \phi _ { 0 } ( x ) = x ; 0 \leqslant x \leqslant 2 \}$ and $\displaystyle \{ \phi _ { 1 } ( x ) = \mathbf { e } ^ { x }$ ； $0 \leqslant x \leqslant 2 \}$ ，and when $f$ is the function $\{ f ( x ) = x ^ { 2 }$ ； $0 \leqslant x \leqslant 2 \}$ ，show that, if $\mathcal { A }$ does not satisfy the Haar condition, then the differences $[ \{ \xi _ { i + 1 k } - \xi _ { i k } ; i =$ $0 , 1 , \ldots , n \}$ ； $k = 1 , 2 , 3 , \ldots ]$ may not be bounded away from zero.

9.7

In order to avoid consideration of the whole of the error function $\{ f ( x ) - p ( x ) ; a \leqslant x \leqslant b \}$ ，there is a version of the one-point exchange algorithm in which the point that leaves the reference is specified at the beginning of each iteration.Let this point be $\xi _ { q }$ The new reference point is found usually by searching from $\xi _ { q }$ in the direction that causes the error $\left| f ( x ) - p ( x ) \right|$ to increase,until an extreme value of the error function is found. Let the conditions of Theorem 9.2 be satisfied, except that this version of the exchange algorithm is used. Let $\mathscr { A }$ and $f$ be such that each error function has exactly $\pmb { n }$ extrema in the open interval $( a , b )$ . Let $\xi _ { 0 } = a$ and $\xi _ { n + 1 } = b$ throughout the calculation,and let the sequence of values of $\pmb q$ be a cyclic sequence of the integers $\left\{ 1 , 2 , \ldots , n \right\}$ .Hence each new reference point is used for exactly $_ n$ iterations. Prove that the calculated approximations converge to the best minimax approximation from $\mathscr { A }$ to $f .$

8 Let the conditions of Theorem 9.4 be satisfied.If an optimization algorithm is applied to maximize the levelled reference error $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ ，thenthesecondderivativesof $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ with respect to the reference points are important, excluding any reference points that become fixed at $^ { a }$ or $^ { b }$ By letting $\boldsymbol { p } = \boldsymbol { p } ^ { * }$ in equation (9.9), in order to express $h ( \xi _ { 0 } , \xi _ { 1 } , \ldots , \xi _ { n + 1 } )$ in terms of the differences $\{ f ( \xi _ { i } ) - p ^ { * } ( \xi _ { i } ) ; i =$ $0 , 1 , \ldots , n + 1 \}$ ， prove that the important off-diagonal terms of the second derivative matrix all tend to zero.

).9 In practice it is inefficient to try to calculate extrema of functions exactly. Therefore investigate some useful ways of relaxing the condition (8.7) on the point that is brought into the reference by each iteration of the one-point exchange algorithm. It is advantageous if the proposed methods preserve the convergence theorems of this chapter.

9.10 Let the conditions of Theorem 9.4 be satisfied, except that in a neighbourhood of one interior reference point, $\pmb { \xi } _ { l } ^ { \ast }$ say, the error function of the best approximation satisfies the equation $\begin{array} { r } { \big | e ^ { * } ( x ) \big | = \big | e ^ { * } ( \xi _ { l } ^ { * } ) \big | - \big | x - \xi _ { l } ^ { * } \big | ^ { \alpha } , } \end{array}$ where $_ { \pmb { \alpha } }$ is a constant in the range (O,2),and where the singularity is due entirely to the function $f .$ Investigate the effect of the singularity on the rate of convergence of the one-point exchange algorithm.

# Rational approximation by the exchange algorithm

# 10.1 Best minimax rational approximation

It is noted in Chapter 3 that polynomials are not suitable for approximating a function of the form shown in Figure 1.1, because no polynomial that is slowly varying when $| x |$ is large can include naturally a sharp peak near the centre of the range of the variable.However,it is easy to obtain this kind of behaviour by letting the approximating function have the form

$$
r ( x ) = p _ { m } ( x ) / q _ { n } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

where $p _ { m } ( x )$ and $q _ { n } ( x )$ are polynomials of degrees $_ { m }$ and $_ n$ respectively. If in the case of Figure 1.1 it is known that the slope of the function to be approximated tends to a constant non-zero value when $x$ becomes large, then it is appropriate to let $m = n + 1$

We use the notation $\{ a _ { i } ; i = 0 , 1 , \dots , m \}$ and $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ for the coefficients of $p _ { m } ( x )$ and $q _ { n } ( x )$ . Thus the function (10.1） is the expression

$$
r ( x ) = \frac { a _ { 0 } + a _ { 1 } x + \ldots + a _ { m } x ^ { m } } { b _ { 0 } + b _ { 1 } x + \ldots + b _ { n } x ^ { n } } , \qquad a \leqslant x \leqslant b .
$$

Because $r ( x )$ remains unchanged if $p ( x )$ and $q ( x )$ are replaced by $c p ( x )$ and $c q ( x )$ ，where $c$ is any non-zero constant, the parameters of $r$ provide $( m + n + 1 )$ degrees of freedom. It is therefore appropriate to compare the approximation (1o.2） with a polynomial approximation from $\mathscr { P } _ { m + n }$ For example, if $f$ is the exponential function $\{ e ^ { x } ; - 1 \leqslant x \leqslant 1 \}$ ， then the least maximum error of an approximation from ${ \mathcal { P } } _ { 4 }$ is 0.000 547, but the least maximum error of a rational approximation when $m = n = 2$ is only O.Ooo O87. This gain in accuracy is remarkable,because the exponential function is not particularly well suited to approximation by a rational function. In many other cases much greater improvements are achieved.

We let $\mathcal { A } _ { m n }$ be the set of rational functions of the form (10.2). Because it is not a linear space, the calculation of rational approximations is harder than the calculation of polynomial approximations. There is, however, a useful extension of the exchange algorithm that does not require much extra work.As in the polynomial case, a sequence of approximations is found, that is expected to converge to the rational function that minimizes the greatest value of the error function. References are still used, each reference being a set of points $\{ \xi _ { i } ; i = 0 , 1 , \ldots , m + n + 1 \}$ that satisfies the conditions

$$
a \leqslant \xi _ { 0 } < \xi _ { 1 } < . . . < \xi _ { m + n + 1 } \leqslant b .
$$

For each trial reference the approximating function, $r _ { k }$ say, that minimizes the expression

$$
\operatorname* { m a x } _ { i = 0 , 1 , \ldots , m + n + 1 } | f ( \xi _ { i } ) - r ( \xi _ { i } ) | , \qquad r \in \bar { \mathcal { A } } _ { m n } ,
$$

is calculated, where $k$ is the iteration number,and where $\bar { \mathcal { A } } _ { m n }$ is the subset of $\mathcal { A } _ { m n }$ whose elements satisfy the condition that they are bounded in $[ a , b ]$ . In the one-point exchange algorithm,one point of the reference is replaced by a solution $\pmb { \eta }$ of the equation

$$
\left| f ( \pmb { \eta } ) - r _ { k } ( \pmb { \eta } ) \right| = \| f - r _ { k } \| ,
$$

where the point that leaves the reference is selected in the way that is described in Chapter 8. Then another iteration is begun.

The following theorem gives the equations that are used for the calculation of $r _ { k }$

# Theorem 10.1

Let $\bar { \mathcal { A } } _ { m n }$ be the set of rational functions of the form (10.2), whose denominators have no zeros in $[ a , b ] ,$ let $\{ \xi _ { i } ; i = 0 , 1 , \ldots , m + n + 1 \}$ be a reference that satisfies the conditions (1O.3),and let $f$ be in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ .If $r _ { k }$ is in $\mathcal { \bar { A } } _ { m n }$ ,and if the equations

$$
r _ { k } ( \xi _ { i } ) + ( - 1 ) ^ { i } h _ { k } = f ( \xi _ { i } ) , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

hold for some constant $h _ { k } ,$ then $r _ { k }$ is the element of $\mathcal { \bar { A } } _ { m n }$ that minimizes expression (10.4).

Proof. Because expression (10.4) has the value $\left| h _ { k } \right|$ when $r$ is equal to $r _ { k }$ ， it is sufficient to show that, if $\bar { r }$ is a function in $\mathcal { \bar { A } } _ { m n }$ that satisfies the condition

$$
\operatorname* { m a x } _ { i = 0 , 1 , \ldots , m + n + 1 } | f ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) | \leqslant | h _ { k } | ,
$$

then $\tilde { r }$ is equal to $r _ { k }$ .Expressions (10.6) and (10.7) imply that each of the terms $\{ [ f ( \xi _ { i } ) - r _ { k } ( \xi _ { i } ) ] - [ f ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) ] ; ~ i = 0 , ~ 1 , \ldots , m + n + 1 \}$ is either zero or has the sign of $( - 1 ) ^ { i } h _ { k }$ . It follows from Theorem 7.5 that the function $\left( \hat { r } - r _ { k } \right)$ has at least $( m + n + 1 )$ zeros in $[ a , b ]$ .However, we may express this function as the ratio of two polynomials,where the degree of the numerator is at most $( m + n )$ . Therefore $\bar { r }$ is equal to $r _ { k }$ □

If the conditions of Theorem 10.1 hold,and if $r ^ { * }$ is a best approximation from $\bar { \mathcal { A } } _ { m n }$ to $f ,$ then it follows from Theorem 10.1 and from the definition of a best approximation that the bounds

$$
\left| h _ { k } \right| \leqslant \left\| f - r ^ { * } \right\| \leqslant \left\| f - r _ { k } \right\|
$$

are satisfied. Thus,again the exchange algorithm provides upper and lower bounds on the least maximum error. Expression (10.8) shows also that $r _ { k }$ is the required approximation if $\left\| f - r _ { k } \right\|$ is equal to $\left| h _ { k } \right|$ ，which provides a sufficient condition for a best approximation that is analogous to the Characterization Theorem 7.2.

Because only one chapter of this book is given to the study of rational approximations, we leave many interesting questions open. For example, we do not even prove that for each $f$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ there is a best approximation from $\bar { \mathcal { A } } _ { m n }$ . In fact a best approximation always exists,and it is unique except for common factors that may occur in its numerator and denominator. These factors may depend on $x$ For example, if $f$ is the constant function whose value is one, then expression (1O.1） is a best rational approximation from $\boldsymbol { \bar { \mathcal { A } } } _ { m n } ,$ ，provided that the polynomials $p _ { m }$ and $q _ { n }$ are the same and have no roots in $[ a , b ]$

Section 10.2 considers the calculation of $r _ { k }$ and $h _ { k }$ by solving the equations (10.6). In Section 10.3 the convergence of the exchange algorithm is studied,and we find that the algorithm may fail. Therefore a more reliable method for calculating best rational approximations is mentioned briefly at the end of the chapter.

# 10.2 The best approximation on a reference

We let the coefficients of the required approximation $r _ { k }$ be $\{ a _ { j } ; j = 0 , 1 , \ldots , m \}$ and $\{ b _ { j } ; j = 0 , 1 , \ldots , n \}$ as in expression (10.2). We ensure that $r _ { k }$ is in $\bar { \mathcal { A } } _ { m n }$ by satisfying the condition

$$
b _ { 0 } + b _ { 1 } x + \ldots + b _ { n } x ^ { n } > 0 , \qquad a \leqslant x \leqslant b .
$$

Therefore the system (10.6) is equivalent to the equations

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 0 } ^ { m } a _ { j } \xi _ { i } ^ { j } = \left[ f ( \xi _ { i } ) - ( - 1 ) ^ { i } h _ { k } \right] \sum _ { j = 0 } ^ { n } b _ { j } \xi _ { i } ^ { j } , } } \\ { { \ i = 0 , 1 , \dots , m + n + 1 . } } \end{array}
$$

They are not linear because not only the coefficients of $r _ { k }$ but also the value of $h _ { k }$ are to be determined.

The usual way of solving these equations begins by eliminating the coefficients $\{ a _ { j } ; j = 0 , 1 , \ldots , m \}$ by making use of the identities

$$
\sum _ { i = 0 } ^ { m + n + 1 } \xi _ { i } ^ { l } \prod _ { \stackrel { j = 0 } { j \neq i } } ^ { m + n + 1 } \frac 1 { ( \xi _ { j } - \xi _ { i } ) } = 0 , \qquad l = 0 , 1 , \ldots , m + n ,
$$

which are a consequence of equation (4.11). Thus expression (10.10) provides the equations

$$
\begin{array} { r l } { \displaystyle \sum _ { i = 0 } ^ { m + n + 1 } \big [ f ( \xi _ { i } ) - ( - 1 ) ^ { i } h _ { k } \big ] \bigg [ \sum _ { j = 0 } ^ { n } b _ { j } \xi _ { i } ^ { j + l } \bigg ] } & { } \\ { \displaystyle \qquad \times \bigg [ \prod _ { j = 0 } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { j } - \xi _ { i } ) } \bigg ] = 0 , \qquad l = 0 , 1 , \dots , n , } \end{array}
$$

which we write in matrix form

$$
A { \bf b } - h _ { k } B { \bf b } = 0 ,
$$

where $\mathbf { b }$ is the vector whose components are the coefficients $\{ b _ { j }$ ； $j = 0 , 1 , \ldots , n \}$ ,and where $\pmb { A }$ and $\pmb { B }$ are square matrices whose elements have the values

$$
A _ { l j } = \sum _ { i = 0 } ^ { m + n + 1 } f ( \xi _ { i } ) \xi _ { i } ^ { j + l } \bigg [ \prod _ { s = 0 \atop s \ne i } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } \bigg ]
$$

and

$$
B _ { l j } = \sum _ { i = 0 } ^ { m + n + 1 } { ( - 1 ) ^ { i } \xi _ { i } ^ { j + l } \left[ \prod _ { \stackrel { s = 0 } { s \neq i } } ^ { m + n + 1 } { \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } } \right] } ,
$$

for $l = 0 , 1 , \ldots , n$ and $j = 0 , 1 , \ldots , n$

A non-zero vector b satisfies equation (10.13) if and only if the matrix $\left( A - h _ { k } B \right)$ is singular. Therefore the only values of $h _ { k }$ that are allowed by the system (10.6) are solutions of the generalized eigenvalue problem

$$
\operatorname* { d e t } ( A - h _ { k } B ) = 0 .
$$

Expressions (10.14) and (10.15） show that the matrices $\pmb { A }$ and $\pmb { B }$ are symmetric. Moreover the following condition is obtained.

# Theorem 10.2 The matrix $\pmb { B }$ is positive definite.

Proof. We let c be any vector in $\mathcal { R } ^ { n + 1 }$ that is not identically zero. It is sufficient to prove that the inequality

$$
\mathbf { c } ^ { \mathrm { { T } } } B \mathbf { c } > 0
$$

is satisfied. We let $\pmb { u }$ be the polynomial

$$
u ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i } , \qquad a \leqslant x \leqslant b ,
$$

and we note that not all of the numbers $\{ u ( \xi _ { i } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ are zero, even if $m = 0$ ·

The definition of $\pmb { B }$ and expression (10.3) give the equation

$$
\begin{array} { l } { { \displaystyle { \bf c } ^ { \bf T } B { \bf c } = \sum _ { l = 0 } ^ { n } \sum _ { j = 0 } ^ { n } c _ { l } c _ { j } \sum _ { i = 0 } ^ { m + n + 1 } \left( - 1 \right) ^ { i } \xi _ { i } ^ { j + l } \prod _ { s = 0 } ^ { m + n + 1 } \frac { 1 } { ( \xi _ { s } - \xi _ { i } ) } } } \\ { ~ } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { m + n + 1 } \sum _ { l = 0 } ^ { n } \sum _ { j = 0 } ^ { n } \sum _ { \ell = 0 } ^ { n } \left( c _ { l } \xi _ { i } ^ { l } \right) \left( c _ { j } \xi _ { i } ^ { j } \right) \prod _ { s = 0 } ^ { m + n + 1 } \frac { 1 } { \left| \xi _ { s } - \xi _ { i } \right| } } } \\ { { \displaystyle ~ = \sum _ { i = 0 } ^ { m + n + 1 } \left[ u \left( \xi _ { i } \right) \right] ^ { 2 } \sum _ { \scriptstyle s = 0 } ^ { m + n + 1 } \frac { 1 } { \left| \xi _ { s } - \xi _ { i } \right| } } . } \end{array}
$$

Therefore the theorem is true.

The theorem implies that the matrix $\pmb { B }$ has a square root $B ^ { \frac { 1 } { 2 } }$ ,which is real, symmetric and non-singular. Therefore we may express equation (10.16) in the form

$$
( B ^ { - \frac { 1 } { 2 } } A B ^ { - \frac { 1 } { 2 } } - h _ { k } I ) = 0 .
$$

Because the matrix $B ^ { - \frac { 1 } { 2 } } A B ^ { - \frac { 1 } { 2 } }$ is symmetric, it follows that all values of $h _ { k }$ that satisfy condition (1O.16) are real, and the number of different roots of this equation is at most $( n + 1 )$ . For each of these roots a non-zero vector $\mathbf { b }$ can be found that satisfies equation (1O.13),and then the coefficients $\{ a _ { j } ; j = 0 , \ 1 , \dots , m \}$ are defined uniquely by the system (10.10).

Several different rational approximations may be generated in this way, but only one of them can satisfy inequality (1O.9). To prove this statement we let $r _ { k }$ and $\bar { r }$ be two approximations that are obtained from the solutions $h _ { k }$ and $\bar { h }$ of equation (10.16). It follows from the equations (10.6),and from the similar equations that define F, that the numbers $\{ r _ { k } ( \xi _ { i } ) - \bar { r } ( \xi _ { i } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ are all zero or their signs alternate. Therefore,if both $r _ { k }$ and $\tilde { r }$ have no singularities in $[ a , b ]$ ， then the difference $( r _ { k } - { \bar { r } } )$ has at least $( m + n + 1 )$ zeros. Hence $r _ { k }$ is equal to $\bar { r } .$

In order to reduce the time that is spent by the exchange algorithm on calculating approximations that fail to satisfy condition (10.9),it is helpful to carry forward from the previous iteration the number $h _ { k - 1 }$ ，because usually it is a good initial estimate of the required root of equation (10.16). One of the exercises at the end of this chapter shows that the required root is not necessarily the one of least modulus.

# 10.3 Some convergence properties of the exchange algorithm

Many of the convergence properties of the exchange algorithm in the rational case are similar to the ones that are obtained when $\mathcal { A }$ isa linear space that satisfies the Haar condition. In particular our next theorem shows that the levelled reference errors $\left\{ \left| h _ { k } \right| ; k = 1 , 2 , 3 , . . . \right\}$ increase strictly monotonically.

# Theorem 10.3

Let the approximation $r _ { k }$ and the number $h _ { k }$ satisfy the conditions of Theorem 10.1, where $f$ is a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ;$ let $e _ { k }$ be the error function

$$
e _ { k } ( x ) = f ( x ) - r _ { k } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

and let the points $\{ \xi _ { i } ^ { + } ; i = 0 , 1 , \ldots , m + n + 1 \}$ of the reference that is calculated for the $( k + 1 ) \mathrm { t h }$ iteration satisfy the following three conditions: $( a )$ they are in ascending order

$$
a \leqslant \xi _ { 0 } ^ { + } < \xi _ { 1 } ^ { + } < . . . < \xi _ { m + n + 1 } ^ { + } \leqslant b ;
$$

$( b )$ the inequalities

$$
\big | e _ { k } ( \xi _ { i } ^ { + } ) \big | \geqslant \big | h _ { k } \big | , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

hold and at least one of them is strict; and $( c )$ the signs of the numbers $\{ e _ { k } ( \xi _ { i } ^ { + } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ alternate. Let the number $h _ { k + 1 }$ and the approximation $r _ { k + 1 }$ from $\bar { \mathcal { A } } _ { m n }$ be defined by the equations

$$
r _ { k + 1 } ( \xi _ { i } ^ { + } ) + ( - 1 ) ^ { i } h _ { k + 1 } = f ( \xi _ { i } ^ { + } ) , \qquad i = 0 , 1 , \dots , m + n + 1 .
$$

Then the inequality

$$
\left| h _ { k + 1 } \right| > \left| h _ { k } \right|
$$

is satisfied.

Proof. Suppose that condition (10.25) is not obtained. Then expressions (10.23) and (10.24) imply the bounds

$$
\big | e _ { k + 1 } ( \xi _ { i } ^ { + } ) \big | \leqslant \big | e _ { k } ( \xi _ { i } ^ { + } ) \big | , \qquad i = 0 , 1 , \ldots , m + n + 1 ,
$$

where $e _ { k + 1 }$ is the error function

$$
e _ { k + 1 } ( x ) = f ( x ) - r _ { k + 1 } ( x ) , \qquad a \leqslant x \leqslant b .
$$

We consider the sequence $\{ e _ { k } ( \xi _ { i } ^ { + } ) - e _ { k + 1 } ( \xi _ { i } ^ { + } ) ; i = 0 , 1 , \ldots , m + n + 1 \}$ It follows from expression (10.26)，from Theorem 7.5,and from the definitions (10.21) and (10.27),that the function $\left( r _ { k + 1 } - r _ { k } \right)$ has at least $( m + n + 1 )$ zeros in $[ a , b ]$ .Therefore the functions $r _ { k + 1 }$ and $r _ { k }$ are the same. In particular, for $i = 0 , 1 , \ldots , m + n + 1$ , the error $\big | e _ { k } \big ( \xi _ { i } ^ { + } \big ) \big |$ is equal to $\left| e _ { k + 1 } ( \xi _ { i } ^ { + } ) \right|$ . Hence, because one of the conditions (10.23) is satisfied as a strict inequality,it follows from equation (10.24) that the increase (10.25) is obtained. This conclusion contradicts the hypothesis that is made at the beginning of the proof. Therefore the theorem is true.□

This theorem allows us to extend Theorem 8.2 to the rational case, provided that on each iteration a solution of the equations (10.6) can be calculated that satisfies condition (1O.9). Hence we find that, if the interval $a \leqslant x \leqslant b$ is replaced by a set of discrete points, then the strategy of forcing the levelled reference error to increase on each iteration can provide the best approximation. Usually satisfactory convergence is obtained in the continuous case also.

However, we noted earlier that the exchange algorithm fails occasion-ally. The form of the failure is that sometimes none of the values of $h _ { k }$ that solve equation (1O.16) gives an approximating function that satisfies condition (10.9). Its cause is closely related to the fact that, if the function

$$
r ^ { * } ( x ) = p ^ { * } ( x ) / q ^ { * } ( x ) , \qquad a \leqslant x \leqslant b ,
$$

is the best approximation to a function $f \mathrm { f r o m } \ { \mathcal { C } } [ a , b ] ,$ , then sometimes the number of different values of $\pmb { x }$ that satisfy the equation

$$
\left| f ( x ) - r ^ { * } ( x ) \right| = \left\| f - r ^ { * } \right\|
$$

is less than $( m + n + 2 )$ . This case occurs only if the best approximation is ‘defective', which means that the actual degree of $p ^ { * }$ is less than $^ { m }$ and the actual degree of $q ^ { * }$ is less than $\pmb { n }$ ·

For example, suppose that $m = n = 2$ , and that the rational function

$$
r ^ { * } ( x ) = \frac { a _ { 0 } + a _ { 1 } x } { b _ { 0 } + b _ { 1 } x } , \qquad a \leqslant x \leqslant b ,
$$

is bounded. Let $f$ be a function in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ such that equation (10.29) holds for only five values of $x , \{ \xi _ { i } ; i = 0$ ,1,2,3,4} say,where the signs of the numbers $\{ f ( \xi _ { i } ) - r ^ { * } ( \xi _ { i } ) ; i = 0 , 1 , 2 , 3 , 4 \}$ alternate. We claim that $r ^ { \ast }$ is a best approximation to $f .$ To prove this statement we suppose that F is even better. The method of proof of Theorem 10.1 implies that $( r ^ { * } - { \bar { r } } )$ is the ratio of two cubic polynomials that has four zeros. Hence $\bar { r } = r ^ { * }$ ,which confirms that $r ^ { * }$ is a best approximation.

In order to show that the exchange algorithm can break down, we let $m = n = 1$ , we let the reference contain the four points $\{ - 4 , - 1 , 1 , 4 \}$ ,and we choose a function $f$ that has the values $f ( - 4 ) = 0 , f ( - 1 ) = 1 , f ( 1 ) = 1$ and $f ( 4 ) = 0$ .This data has been chosen because the function $r$ in $\boldsymbol { \bar { \mathcal { A } } } _ { 1 1 }$ that minimizes expression (10.4) is the constant function

$$
\begin{array} { r } { r ( x ) = \frac { 1 } { 2 } , \qquad a \leqslant x \leqslant b . } \end{array}
$$

Therefore the conditions (10.6） are not obtained. The solutions of equation (10.16) are the values $h _ { k } = - 0 . 4$ and $h _ { k } = 0 . 4$ .They give the rational approximations $( 1 . 6 - 0 . 2 x ) / ( 2 - x )$ and $( 1 . 6 + 0 . 2 x ) / ( 2 + x ) .$ ， which satisfy the equations (10.6). However, both approximations are unacceptable because they contain singularities in the range of $x$

Some computer programs that apply the exchange algorithm do not abandon the calculation when this kind of difficulty occurs. Instead they may try different references or they may reduce the values of $^ { m }$ or $_ n$ However, there may not be a computer program of this kind that treats all cases successfully.

# 10.4 Methods based on linear programming

Many of the difficulties that occur sometimes, when the exchange algorithm is used to calculate the best rational approximation to a function $f$ in $\mathcal { C } [ a , b ] ,$ ，are due to the fact that the system of equations (10.6) is not linear in the unknowns.However, if we let $h$ be an estimate of the least maximum error, then the problem of finding out whether the estimate is too low or too high can be reduced to a set of linear conditions. Specifically,there is an approximation of the form (10.2) that satisfies the bound

$$
| f ( x ) - r ( x ) | \leqslant h , \qquad a \leqslant x \leqslant b ,
$$

if and only if there exist values of the coefficients $\{ a _ { i } ; i = 0 , 1 , \ldots , m \}$ and $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ such that the inequalities

$$
q ( x ) > 0 , \qquad a \leqslant x \leqslant b ,
$$

and

$$
\begin{array} { l l } { { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) } } \\ { { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) } } \end{array} \quad \quad x \in X ,
$$

are obtained, where $\boldsymbol { x }$ is the range of $x$ ，and where $p$ and $q$ are the numerator and denominator of $r .$ Because $r$ is unchanged if $p$ and $q$ are multiplied by a constant, we may replace expression (10.33) by the condition

$$
q ( x ) \geq \delta , \qquad x \in X ,
$$

where $\pmb { \delta }$ is any positive constant.

The notation $\pmb { X }$ is used for the range of $x$ , because,in order to apply linear programming methods, it is usual to replace the range $a \leqslant x \leqslant b$ by a set of discrete points. We suppose that this has been done. Then calculating whether an approximation $p / q$ satisfies conditions (10.34) and (10.35） is a standard linear programming procedure. Many trial values of $\pmb { h }$ may be used, and they can be made to converge to the least maximum error by a bracketing and bisection procedure.Whenever $h$ exceeds the least maximum error, the linear programming calculation gives feasible coefficients for $p$ and $\pmb q .$ provided that the discretization of $\pmb { X }$ in condition (10.35) does not cause inequality (10.33) to fail.

This procedure has the property that, even if $\pmb { h }$ is much larger than necessary, then it is usual for several of the conditions (10.34) to be satisfied as equations. It would be better, however, if the maximum error of the calculated approximation $p / q$ were less than $\pmb { h }$ A way of achieving this useful property is to replace expression (10.34) by the conditions

$$
\begin{array} { r l } & { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) + \varepsilon } \\ & { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) + \varepsilon } \end{array} \quad \quad x \in X ,
$$

where $\pmb \varepsilon$ is an extra variable. Moreover, the overall scaling of $\pmb { p }$ and $\pmb q$ is fixed by the equation

$$
b _ { 0 } + b _ { 1 } \zeta + b _ { 2 } \zeta ^ { 2 } + . . . + b _ { n } \zeta ^ { n } = 1 ,
$$

where $\pmb { \zeta }$ is any fixed point of $X ,$ the value $\zeta = 0$ being a common choice. For each trial value of $\pmb { h }$ the variable $\pmb \varepsilon$ is minimized,subject to the conditions (10.36) and (10.37) on the variables $\{ a _ { i } ; i = 0 , 1 , \ldots , m \} ,$ $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ and $\pmb \varepsilon$ , which is still a linear programming calculation.

It is usual to omit condition (10.35) from this calculation,and to choose $h$ to be greater than the least maximum error.In this case the final value of $\pmb \varepsilon$ is negative.Hence condition (1O.35） is unnecessary，because expression (10.36) implies that $q ( x )$ is positive for all $x \in X .$ If the calculated value of $\pmb \varepsilon$ is zero, then usually $p / q$ is the best approximation, but very occasionally there are difficulties due to $p ( { \pmb x } )$ and $q ( x )$ both being zero for a value of $x$ in $X .$ If $\pmb \varepsilon$ is positive, then the conditions (10.34) and (10.35） are inconsistent, so $h$ is less than the least maximum error. Equation (10.37） is important because,if it is left out,and if the conditions (1O.36) are satisfied for a negative value of $\pmb \varepsilon$ ,then $\pmb \varepsilon$ can be made arbitrarily large and negative by scaling all the variables of the linear programming calculation by a sufficiently large positive constant. Hence the purpose of condition (10.37) is to ensure that $\pmb \varepsilon$ is bounded below.

The introduction of $\pmb \varepsilon$ gives an iterative method for adjusting $\pmb { h }$ A high value of $\pmb { h }$ is required at the start of the first iteration. Then $p , q$ and $\pmb \varepsilon$ are calculated by solving the linear programming problem that has just been described. The value of $\pmb { h }$ is replaced by the maximum error of the current approximation $p / q$ . Then a new iteration is begun. It can be shown that the calculated values of $\pmb { h }$ converge to the least maximum error from above.This method is called the ‘differential correction algorithm'.

A simple device provides a large reduction in the number of iterations that are required by this procedure.It is to replace the conditions (10.36) of the linear programming calculation by the inequalities

$$
\begin{array} { r l } & { p ( x ) - f ( x ) q ( x ) \leqslant h q ( x ) + \varepsilon \bar { q } ( x ) } \\ & { f ( x ) q ( x ) - p ( x ) \leqslant h q ( x ) + \varepsilon \bar { q } ( x ) } \end{array} \biggr \} , \qquad x \in X ,
$$

where $\bar { q } ( { \pmb x } )$ is a positive function that is an estimate of the denominator of the best approximation. On the first iteration we let $\bar { q } ( { \pmb x } )$ be the constant function whose value is one, but on later iterations it is the denominator of the approximation that gave the current value of $\pmb { h } .$ .Some fundamental questions on the convergence of this method are still open in the case when the range of $x$ is the interval $[ a , b ]$

# 10 Exercises

10.1 Let $f$ be a function in $\mathcal { C } [ a , b ] ,$ and let $r ^ { * } = p ^ { * } / q ^ { * }$ and $\bar { r } = \bar { p } / \bar { q }$ be functions in $\mathcal { \bar { A } } _ { m n }$ that satisfy the condition $\left\| \boldsymbol { f } - \boldsymbol { \bar { r } } \right\| _ { \infty } < \| \boldsymbol { f } - \boldsymbol { r } ^ { * } \| _ { \infty } ,$ where $q ^ { * } ( x )$ and $\bar { q } ( x )$ are positive for all $\pmb { x }$ in $[ a , b ]$ .Let $r$ be the rational function $\{ [ p ^ { * } ( x ) + \theta \bar { p } ( x ) ] / [ q ^ { * } ( x ) + \theta \bar { q } ( x ) ] ;$ $a \leqslant x \leqslant b \}$ ， where $\pmb \theta$ is a positive number. Prove that the inequality $\| f - r \| _ { \infty } <$ $\| f - r ^ { * } \| _ { \infty }$ is satisfied. Allowing $\pmb \theta$ to change continuously gives a set of rational approximations that is useful to some theoretical work.

10.2 Let $r ^ { * }$ be an approximation from $\bar { \mathcal { A } } _ { m n }$ to a function $f$ in $\mathcal { C } [ a , b ] ,$ and let $\mathcal { Z } _ { \mathbf { M } }$ be the set of points $\{ x : | f ( x ) - r ^ { * } ( x ) | = \| f - r ^ { * } \| _ { \infty } ;$ $a \leqslant x \leqslant b $ .Prove that, if $\bar { r }$ is a function in $\mathcal { \bar { A } } _ { m n }$ that satisfies the sign conditions

$$
\begin{array} { r } { \big [ f ( x ) - r ^ { * } ( x ) \big ] \big [ \bar { r } ( x ) - r ^ { * } ( x ) \big ] > 0 , \qquad x \in \mathcal { Z } _ { \mathsf { M } } , } \end{array}
$$

then there exists a positive number $\pmb \theta$ such that the approximation $r ,$ defined in Exercise 10.1,gives the reduction $\| f - r \| _ { \infty } <$ $\| f - r ^ { * } \| _ { \infty }$ in the error function. Thus Theorem 7.1 can be extended to rational approximation.

10.3 Let $f$ be a function in $\mathcal { C } [ 0 , 6 ]$ that takes the values $f ( \xi _ { 0 } ) = f ( 0 ) =$ 0.0, $f ( \xi _ { 1 } ) = f ( 2 ) = 1 . 0$ ， $f ( \xi _ { 2 } ) = f ( 5 ) = 1 . 6 $ and $f ( \xi _ { 3 } ) = f ( 6 ) = 2 . 0$ Calculate and plot the two functions in the set $\mathcal { A } _ { 1 1 }$ that satisfy the equations (10.10).

10.4 Prove that the function $\{ r ^ { * } ( x ) = { \frac { 3 } { 4 } } x$ ； $- 1 \leqslant x \leqslant 1 \}$ is the best approximation to $\{ f ( x ) = x ^ { 3 }$ ； $- 1 \leqslant x \leqslant 1 \}$ from the set $\vec { \mathcal { A } } _ { 2 1 }$ ,but that it is not the best approximation from the set $\displaystyle \overline { { \mathcal { A } } } _ { 1 2 }$

10.5 Prove that,if in the iteration that is described in the last paragraph of this chapter, the function $\bar { q }$ is the denominator of a best approximation, and $\pmb { h }$ is any real number that is greater than the least maximum error, then the iteration calculates directly a function $p / q$ that is a best approximation.

10.6 Let $r ^ { * } = p ^ { * } / q ^ { * }$ be a function in $\mathcal { \bar { A } } _ { m n }$ such that the only common factors of $p ^ { * }$ and $q ^ { * }$ are constants,and let the defect $\pmb { d }$ be the smaller of the integers $\left\{ m - \right.$ (actual degree of $p ^ { * }$ ， $n -$ (actual degree of $q ^ { * } ) \}$ .Prove that, if $\left\{ \xi _ { i } ; \ : i = 1 , 2 , \ldots , k \right\}$ is any set of distinct points in $( a , b )$ ,where $k \leqslant m + n - d$ ， then there exists a function $\bar { r }$ in $\bar { \mathcal { A } } _ { m n }$ such that the only zeros of the function $( { \bar { r } } - r ^ { * } )$ are simple zeros at the points $\{ \xi _ { i } ; i = 1 , 2 , \ldots , k \}$ .Hence deduce from Exercise 10.2 a characterization theorem for minimax rational approximation that is analogous to Theorem 7.2.

10.7 Let $f$ be a function that takes the values $f ( \xi _ { 0 } ) = f ( 0 . 0 ) = 1 2$ ， $f ( \xi _ { 1 } ) = f ( 1 ) = 8 ,$ $f ( \xi _ { 2 } ) = f ( 2 ) = - 1 2$ ，and $f ( \xi _ { 3 } ) = f ( 3 ) = - 7$ . Calculate the two functions in the set $\mathcal { A } _ { 1 1 }$ that satisfy the equations (10.10). Note that the function that does not have a singularity in the interval [O,3] is derived from the solution $h _ { k }$ of equation (10.16) that has the larger modulus.

10.8 Investigate the calculation of the function in $\mathcal { \bar { A } } _ { 1 1 }$ that minimizes expression (10.4),where the data have the form $f ( \xi _ { 0 } ) = f ( - 4 ) =$ $\varepsilon _ { 0 } , f ( \xi _ { 1 } ) = f ( - 1 ) = 1 + \varepsilon _ { 1 }$ ， $f ( \xi _ { 2 } ) = f ( 1 ) = 1 + \varepsilon _ { 2 } .$ ,and $f ( \xi _ { 3 } ) = f ( 4 ) =$ $\pmb { \varepsilon _ { 3 } }$ ， and where the moduli of the numbers $\{ \varepsilon _ { i } ; i = 0 , 1 , 2 , 3 \}$ are very small.

10.9 Let $f \in { \mathcal { C } } [ a , b ] .$ let $\pmb { X }$ be a set of discrete points from $[ a , b ] ,$ and let $r ^ { * } = p ^ { * } / q ^ { * }$ be a best approximation from $\mathcal { A } _ { m n }$ to $f$ on $X ,$ subject to the conditions $\{ q ^ { * } ( x ) > 0 ; x \in X \}$ and $q ^ { * } ( \zeta ) = 1$ ,where $\pmb { \zeta }$ is a point of $\boldsymbol { x }$ .Let the version of the differential correction algorithm that depends on condition (10.36) be applied to calculate $r ^ { * }$ ，where $\pmb { h }$ is chosen and adjusted in the way that is described in Section 10.5. Prove that on each iteration the calculated value of $\pmb \varepsilon$ satisfies the bound

$$
\varepsilon \leqslant - ( h - \| f - r ^ { * } \| ) \operatorname* { m i n } _ { x \in X } q ^ { * } ( x ) .
$$

Hence show that, if the normalization condition (10.37) keeps the variables $\{ b _ { i } ; i = 0 , 1 , \ldots , n \}$ bounded throughout the calculation, then the sequence of values of $h$ converges to $\| f - r ^ { * } \|$

10.10Prove that, if the points $\{ \xi _ { i } ; i = 0 , 1 , 2 , 3 \}$ are in ascending order, and if the function values $\left\{ f ( \xi _ { i } ) ; i = 0 , 1 , 2 , 3 \right\}$ increase strictly monotonically, then one of the solutions $r _ { k }$ in the set $\mathcal { A } _ { 1 1 }$ to the equations (1O.6) has no singularities in the range $[ \xi _ { 0 } , \xi _ { 3 } ] _ { : }$ ,and the other solution has a singularity in the interval $( \xi _ { 1 } , \xi _ { 2 } )$ .

# 11

# Least squares approximation

# 11.1 The general form of a linear least squares calculation

Given a set $\boldsymbol { \mathscr { A } }$ of approximating functions that is a subset of $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ] ,$ ， and given a fixed positive function $\{ w ( x ) ; a \leqslant x \leqslant b \} ,$ ，which we call a‘weight function',we define the element $p ^ { * }$ of $\mathscr { A }$ to be a best weighted least squares approximation from $\mathscr { A }$ to $f ,$ if $p ^ { * }$ minimizes the expression

$$
\int _ { a } ^ { b } w ( x ) [ f ( x ) - p ( x ) ] ^ { 2 } \mathrm { d } x , \qquad p \in \mathcal { A } .
$$

Often $\scriptstyle { \mathcal { A } }$ is a finite-dimensional linear space. We study the conditions that $p ^ { * }$ must satisfy in this case, and we find that there are some fast numerical methods for calculating $p ^ { * }$

It is convenient to express the properties that are obtained by $p ^ { * }$ in terms of scalar products. For each $f$ and $\pmb { g }$ in $\mathcal { C } [ \boldsymbol { a } , \boldsymbol { b } ]$ we let $( f , g )$ be the scalar product

$$
( f , g ) = \int _ { a } ^ { b } w ( x ) f ( x ) g ( x ) \mathrm { d } x ,
$$

which satisfies all the conditions that are stated in the frst paragraph of Section 2.4. Therefore we introduce the norm

$$
\| f \| = ( f , f ) ^ { \frac { 1 } { 2 } } , \qquad f \in { \mathcal { C } } [ a , b ] ,
$$

and, in accordance with the ideas of Chapter 1, we define the distance from $f$ to $\pmb { g }$ to be $\| f - g \|$ . Hence expression (11.1) is the square of the distance

$$
\| f - p \| = ( f - p , f - p ) ^ { \frac { 1 } { 2 } } , \qquad p \in \mathcal { A } .
$$

Therefore the required approximation $p ^ { * }$ is a ‘best' approximation from $\mathscr { A }$ to $f .$ It follows from Theorem 1.2 that, if $\pmb { \mathcal { A } }$ is a finite-dimensional linear space, then a best approximation exists. Further, because the method of proof of Theorem 2.7 shows that the norm (11.3) is strictly convex, it follows from Theorem 2.4 that only one function in $\mathscr { A }$ minimizes expression (11.1).

One of the main advantages of the scalar product notation is that the theory that is developed applies,not only to continuous least squares approximation problems, but also to discrete ones.Discrete calculations occur, for example, when one requires an approximation to a function $f$ in ${ \mathcal { C } } [ a , b ]$ ,but, instead of being able to calculate $f ( x )$ for any $x$ in $a \leqslant x \leqslant b$ ， one can only measure the value of $f ( x )$ ，where the measuring process includes a random error.Let the values of $\pmb { x }$ at which the measurements are taken be $\{ x _ { j } ; j = 1 , 2 , \dots , m \}$ ,let $y _ { j }$ be the measured value of $f ( x _ { j } )$ ， and let the variance of the measurement be $1 / w _ { j } .$ If $\mathcal { A } _ { 0 }$ is the set of approximating functions,and if the random errors have a normal distribution, then it is appropriate for statistical reasons to seek the function $p _ { 0 } ^ { * }$ in $\mathcal { A } _ { 0 }$ that minimizes the weighted sum of squares

$$
\sum _ { j = 1 } ^ { m } w _ { j } [ y _ { j } - p _ { 0 } ( x _ { j } ) ] ^ { 2 } , \qquad p _ { 0 } \in \mathcal { A } _ { 0 } .
$$

It happens often that one minimizes this expression even when the distribution of data errors is not normal, because the numerical methods for calculating $\boldsymbol { p } _ { 0 } ^ { * }$ are easy to apply when $\mathcal { A } _ { 0 }$ is a linear space.

We wish to introduce scalar products in such a way that expression (11.5) is analogous to the square of the distance (11.4). However, the definition

$$
( f , g ) = \sum _ { j = 1 } ^ { m } w _ { j } f ( x _ { j } ) g ( x _ { j } )
$$

is unacceptable,because in this case expression (11.3) fails to satisfy the axioms of a norm,due to the fact that $( f , f )$ is zero for some functions $f$ that are not identically zero.Instead we take note of the fact that the data $\{ y _ { j } ; j = 1 , 2 , \dots , m \}$ define a vector $y$ in $\mathcal { R } ^ { m }$ .For each ${ p } _ { 0 }$ in $\scriptstyle { \mathcal { A } } _ { 0 }$ ,we let $X ( p _ { 0 } )$ be the vector in ${ \mathcal { R } } ^ { m }$ whose components have the values $\{ p _ { 0 } ( x _ { j } ) ; j =$ $1 , 2 , \ldots , m \}$ , and we let $\mathcal { A }$ be the set $\{ X ( p _ { 0 } ) ; p _ { 0 } \in \mathcal { A } _ { 0 } \}$ ,which is a subset of ${ \mathcal { R } } ^ { m }$ .Calculating the function $p _ { 0 } ^ { * }$ in $\mathcal { A } _ { 0 }$ that minimizes expression (11.5) is equivalent to obtaining the vector $p ^ { * }$ in $\mathscr { A }$ that gives the least value of the sum of squares

$$
\sum _ { j = 1 } ^ { m } w _ { j } \big [ y _ { j } - p _ { j } \big ] ^ { 2 } , \qquad p \in \mathcal { A } ,
$$

where $\{ p _ { j } ; j = 1 , 2 , \ldots , m \}$ are the components of $p$ . We can now let the scalar product $( u , v )$ have the value

$$
( u , v ) = \sum _ { j = 1 } ^ { m } w _ { j } u _ { j } v _ { j }
$$

for any vectors $\pmb { u }$ and $v$ in ${ \mathcal { R } } ^ { m }$ ， and we let $\left\| u \right\|$ be $( u , u ) ^ { \frac { 1 } { 2 } }$ . Hence the calculation of $p ^ { * }$ becomes a best approximation problem,where we require to minimize the distance

$$
\| y - p \| = ( y - p , y - p ) ^ { \frac { 1 } { 2 } } , \qquad p \in \mathcal { A } .
$$

In the usual case when $\mathcal { A } _ { 0 }$ is a linear subspace of $\mathcal { C } [ a , b ] .$ then $\mathscr { A }$ is a finite-dimensional linear subspace of ${ \mathcal { R } } ^ { m }$ .Hence Theorems 1.2 and 2.4 imply that a unique element of $\mathcal { A }$ minimizes expression (11.9).

Because expressions(11.4) and (11.9) are both distances in a Hilbert space,and because some highly useful properties are satisfied when the set of approximating functions is a linear space,we study the following problem.Let $\mathscr { A }$ be a finite-dimensional linear subspace of a Hilbert space ${ \mathcal { B } } .$ For any $f$ in $\mathcal { B }$ ,calculate the best approximation from $\mathscr { A }$ to $f .$

# 11.2 The least squares characterization theorem

The following characterization theorem shows that the solution to the problem that is stated in the last paragraph may be regarded as an orthogonal projection onto the set of approximating functions, where the elements $f$ and $\pmb { g }$ of a Hilbert space are defined to be orthogonal if the scalar product $( f , g )$ is zero.

# Theorem 11.1

Let $\mathscr { A }$ be a linear subspace of a Hilbert space $\mathcal { B }$ , and let $f$ be any element of $\mathcal { B }$ . The point $p ^ { * }$ in $\mathscr { A }$ is the best approximation from $\mathscr { A }$ to $f$ if and only if the error $e ^ { * } { = } f { - } p ^ { * }$ satisfies the orthogonality conditions

$$
( e ^ { * } , p ) = 0 , \qquad p \in \mathcal { A } .
$$

Proof. Suppose first that $( e ^ { * } , p )$ is non-zero for some $p$ in $\mathcal { A } .$ .Then the square of the distance from $( p ^ { * } + \lambda p )$ to $f$ is the expression

$$
\left\| f - p ^ { * } - \lambda p \right\| ^ { 2 } = \left\| f - p ^ { * } \right\| ^ { 2 } - 2 \lambda \left( e ^ { * } , p \right) + \lambda ^ { 2 } \left\| p \right\| ^ { 2 } ,
$$

where $\pmb { \lambda }$ is a real parameter. The value of $\pmb { \lambda }$ that minimizes expression (11.11) is not equal to zero. Therefore $p ^ { * }$ is not the best approximation from $\mathscr { A }$ to $f .$

Conversely, suppose that $( e ^ { * } , p )$ is zero for all $\pmb { p }$ in $\mathcal { A } .$ Let $q ^ { * }$ be any element of $\mathcal { A }$ ，From the properties of scalar products we deduce the equation

$$
\begin{array} { r l } & { \| f - q ^ { * } \| ^ { 2 } - \| f - p ^ { * } \| ^ { 2 } } \\ & { \quad = \| q ^ { * } \| ^ { 2 } - \| p ^ { * } \| ^ { 2 } - 2 ( f , q ^ { * } ) + 2 ( f , p ^ { * } ) } \\ & { \quad = \| q ^ { * } - p ^ { * } \| ^ { 2 } + 2 ( f - p ^ { * } , p ^ { * } - q ^ { * } ) . } \end{array}
$$

The last term is zero by hypothesis. Hence we obtain the bound

$$
\begin{array} { c } { \| f - q ^ { * } \| ^ { 2 } = \| f - p ^ { * } \| ^ { 2 } + \| q ^ { * } - p ^ { * } \| ^ { 2 } } \\ { \geqslant \| f - p ^ { * } \| ^ { 2 } , } \end{array}
$$

which holds for all $q ^ { * }$ in ${ \mathcal { A } } .$ Therefore $p ^ { * }$ is the best approximation.

Figure 11.1 presents a geometric view of this theorem. The point $p ^ { * }$ is the best approximation from ${ \mathcal { A } } \tan f .$ The point $q ^ { * }$ is any other point of $\mathcal { A }$ The orthogonality condition is shown by the standard symbol for a right-angle. Moreover, the first line of expression (11.13） states that Pythagoras's Theorem is obtained by the points of Figure 11.1, namely the square of the distance from $f$ to $q ^ { * }$ is equal to the square of the distance from $f$ to $p ^ { * }$ plus the square of the distance from $q ^ { * }$ to $p ^ { * }$ ·

Expression (11.13) is useful in two other ways. It provides an alter-native proof of the uniqueness of the best approximation,for it shows that $\| f - q ^ { * } \|$ is larger than $\| f - p ^ { * } \|$ if $q ^ { * }$ is not equal to $p ^ { * }$ . Secondly, by letting $q ^ { * }$ be the zero element, we obtain the equation

$$
\| f \| ^ { 2 } { \cdot } = \| p ^ { * } \| ^ { 2 } + \| f - p ^ { * } \| ^ { 2 } .
$$

Some interesting consequences of this equation are found later.

# 11.3 Methods of calculation

In order to calculate a best least squares approximation from a linear space $\mathcal { A } _ { : }$ , we choose a set of functions, $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ say, that span $\mathcal { A } .$ . Often a set of basis functions is present in the definition of $\mathcal { A } .$ We continue to let $p ^ { * }$ be the best approximation. Therefore we require the values of the coefficients $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ in the expression

$$
p ^ { * } = \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } .
$$

![](images/0c50b4b75d7ea9b87fd6f8e727e26a92e7541240a4a1080991f48f47380cc4a3.jpg)  
Figure 11.1. A geometric view of the least squares characterization theorem.

We suppose that the elements $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ are linearly independent, which is equivalent to supposing that the dimension of $\mathcal { A }$ is $( n + 1 )$ ， in order that the problem of determining these coefficients has a unique solution. Because every element of $\mathscr { A }$ is a linear combination of the basis elements,it follows from Theorem 11.1 that expression (11.15) is the best approximation from $\mathscr { A }$ to $f$ if and only if the conditions

$$
\left( \phi _ { i } , f - \sum _ { j = 0 } ^ { n } c _ { j } ^ { * } \phi _ { j } \right) = 0 , \qquad i = 0 , 1 , \ldots , n ,
$$

are satisfied. They can be written in the form

$$
\sum _ { j = 0 } ^ { n } \big ( \phi _ { i } , \phi _ { j } \big ) c _ { j } ^ { * } = \big ( \phi _ { i } , f \big ) , \qquad i = 0 , 1 , \dots , n .
$$

Thus we obtain a square system of linear equations in the required coefficients, that are called the ‘normal equations’ of the least squares calculation.

The normal equations may also be derived by expressing a general element of $\mathscr { A }$ in the form

$$
p = \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ,
$$

where $\{ c _ { i } ; i = 0 , 1 , \ldots , n \}$ is a set of real parameters. Their values have to be chosen to minimize the expression

$$
( f - p , f - p ) = ( f , f ) - 2 \sum _ { i = 0 } ^ { n } c _ { i } ( \phi _ { i } , f ) + \sum _ { i = 0 } ^ { n } \sum _ { j = 0 } ^ { n } c _ { i } c _ { j } ( \phi _ { i } , \phi _ { j } ) .
$$

Therefore, for $i = 0 , 1 , \ldots , n$ ， the derivative of this expression with respect to $c _ { i }$ must be zero.These conditions are just the normal equations.

We note that the matrix of the system (11.17) is symmetric.Further, if $\{ z _ { i } ; i = 0 , 1 , \ldots , n \}$ is a set of real parameters, the identity

$$
\sum _ { i \mathop { = } 0 } ^ { n } \sum _ { j \mathop { = } 0 } ^ { n } z _ { i } z _ { j } ( \phi _ { i } , \phi _ { j } ) = \biggl ( \sum _ { i \mathop { = } 0 } ^ { n } z _ { i } \phi _ { i } , \sum _ { j \mathop { = } 0 } ^ { n } z _ { j } \phi _ { j } \biggl )
$$

holds. Because the right-hand side is the square of $\big \| \sum z _ { i } \phi _ { i } \big \|$ , it is zero only if all the parameters are zero. Hence the matrix of the system (11.17) is positive definite. Therefore there are many good numerical procedures for solving the normal equations. The technique of calculating the required coefficients $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ from the normal equations suggests itself. Often this is an excellent method, but sometimes it causes unnecessary loss of accuracy.

For example, suppose that we have to approximate a function $f$ in $\mathcal { C } [ 1 , 3 ]$ by a linear function

$$
p ^ { * } ( x ) = c _ { 0 } ^ { * } + c _ { 1 } ^ { * } x , \qquad 1 \leqslant x \leqslant 3 ,
$$

and that we are given measured values of f on the point set {xi =i; i = 1,2,3}.Let the data be y1 = 2.0≈f(1.0),y2=2.8≈f(2.0),and y3=4.2 = f(3.0),where the variances of the measurements are 1/M, 0.1 and 0.1 respectively. In order to demonstrate the way in which accuracy can be lost, we let M be much larger than ten. The normal equations are the system

$$
{ \binom { M + 2 0 } { M + 5 0 } } M + 5 0 \atop { M + 1 3 0 } { \binom { c _ { 0 } ^ { * } } { c _ { 1 } ^ { * } } } = { \binom { 2 M + 7 0 } { 2 M + 1 8 2 } } ,
$$

which has the solution

$$
\begin{array} { l } { { c _ { 0 } ^ { * } = 0 . 9 6 M / ( M + 2 ) } } \\ { { c _ { 1 } ^ { * } = ( 1 . 0 4 M + 2 . 8 ) / ( M + 2 ) } } \end{array} \biggr \} .
$$

We note that there is no cancellation in expression (11.23), even if $M$ is large.In this case the values of $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ are such that the difference $\left[ p ^ { * } ( 1 . 0 ) - y _ { 1 } \right]$ is small,and the remaining degree of freedom in the coeffcients is fixed by the other two measurements of $f .$ However, to take an extreme case, suppose that $M$ has the value ${ 1 0 } ^ { 9 }$ , and that we try to obtain $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the system (11.22),on a computer whose relative accuracy is only six decimals.When the matrix elements of the normal equations are formed, their values are dominated so strongly by $M$ that the important information in the measurements $y _ { 2 }$ and $y _ { 3 }$ is lost. Hence it is not possible to obtain accurate values of $c _ { 0 } ^ { * }$ and $c _ { 1 } ^ { * }$ from the calculated normal equations by any numerical procedure.

One reason for the loss of precision is that high relative accuracy in the matrix elements of the normal equations need not provide similar accuracy in the required solution $\{ c _ { j } ^ { * } ; j = 0 , 1 , \ldots , n \}$ .However, similar accuracy is always obtained if the system (11.17) is diagonal. Therefore many successful methods for solving linear least squares problems are based on choosing the functions $\{ \phi _ { j } ; j = 0 , 1 , \ldots , n \}$ so that the conditions

$$
( \phi _ { i } , \phi _ { j } ) = 0 , \qquad i \neq j .
$$

are satisfied,in order that the matrix of the normal equations is diagonal. In this case we say that the basis functions are orthogonal. When $\mathscr { A }$ is the space ${ \mathcal { P } } _ { n }$ of algebraic polynomials,a useful technique for generating orthogonal basis functions is by means of a three-term recurrence relation,which is described in the next section.

In the example that gives the system (11.22), is a subspace of $\mathcal { R } ^ { 3 }$ ,and its basis vectors have the components

$$
\phi _ { 0 } = { \binom { 1 } { 1 } } \quad { \mathrm { a n d } } \quad \phi _ { 1 } = { \binom { 1 } { 2 } } .
$$

One way of making the basis vectors orthogonal is to replace $\phi _ { 1 }$ by the vector

$$
\begin{array} { r } { \bar { \phi } _ { 1 } = \phi _ { 1 } - \alpha \phi _ { 0 } , } \end{array}
$$

where $_ { \pmb { \alpha } }$ has the value $( M + 5 0 ) / ( M + 2 0 )$ . In this case the coefficients of the required least squares approximation

$$
p ^ { * } = \bar { c } _ { 0 } \phi _ { 0 } + \bar { c } _ { 1 } \bar { \phi } _ { 1 }
$$

satisfy the diagonal normal equations

$$
\left( { { \cal M } + 2 0 \atop 5 0 } \right) _ { M + 2 0 } ^ { \cal ( 0 ) } { \left( { { \overline { { c } } } _ { 0 } } \right) } = \left( { 2 { \cal M } + 7 0 \atop 5 2 M + 1 4 0 } \right) ,
$$

which gives the values

$$
\begin{array} { l } { \bar { c } _ { 0 } = ( 2 M + 7 0 ) / ( M + 2 0 ) } \\ { \bar { c } _ { 1 } = ( 1 . 0 4 M + 2 . 8 ) / ( M + 2 ) } \end{array} \biggr \} .
$$

Of course this calculation is equivalent to the earlier one in exact arithmetic. However, if we let $M = 1 0 ^ { 9 }$ again,and if the calculation is carried out on a six-decimal floating point computer, then we avoid the serious loss of accuracy that occurred before.

In general the use of orthogonal basis functions is recommended, because it happens frequently that information is lost when the normal equations are constructed. The form of the best least squares approxima-tion when the basis functions are orthogonal is suficiently important to be stated as a theorem.

# Theorem 11.2

Let $\mathcal { A }$ be a linear subspace of a Hilbert space $\mathcal { B }$ that is spanned by the basis functions $\{ \phi _ { i } ; i = 0 , 1 , \ldots , n \}$ . If the orthogonality condition (11.24) is satisfied,then,for any $f$ in $\mathcal { B }$ ,the best approximation from $\mathscr { A }$ to $f$ is the function

$$
p ^ { * } = \sum _ { j = 0 } ^ { n } \frac { ( \phi _ { j } , f ) } { \| \phi _ { j } \| ^ { 2 } } \phi _ { j } .
$$