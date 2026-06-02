Thus,

$$
\begin{array} { r } { \mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) } . } \end{array}
$$

To compute $\mathbf { r } ^ { ( k ) }$ , we multiply by $A$ and subtract b to obtain

$$
A \mathbf { x } ^ { ( k ) } - \mathbf { b } = A \mathbf { x } ^ { ( k - 1 ) } - \mathbf { b } + t _ { k } A \mathbf { v } ^ { ( k ) }
$$

or

$$
\mathbf { r } ^ { ( k ) } = \mathbf { r } ^ { ( k - 1 ) } - t _ { k } A \mathbf { v } ^ { ( k ) } .
$$

Thus,

$$
\langle \mathbf { r } ^ { ( k ) } , \mathbf { r } ^ { ( k ) } \rangle = \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k ) } \rangle - t _ { k } \langle A \mathbf { v } ^ { ( k ) } , \mathbf { r } ^ { ( k ) } \rangle = - t _ { k } \langle \mathbf { r } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle .
$$

Further,from Eq.(7.29),

$$
\langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle = t _ { k } \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle ,
$$

so

$$
\begin{array} { r l } & { s _ { k } = - \frac { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { r } ^ { ( k ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } = - \frac { \langle \mathbf { r } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } } \\ & { \qquad = \frac { ( 1 / t _ { k } ) \langle \mathbf { r } ^ { ( k ) } , \mathbf { r } ^ { ( k ) } \rangle } { ( 1 / t _ { k } ) \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } = \frac { \langle \mathbf { r } ^ { ( k ) } , \mathbf { r } ^ { ( k ) } \rangle } { \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } . } \end{array}
$$

In summary, we have the formulas:

$$
\mathbf { r } ^ { ( 0 ) } = \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } ; \quad \mathbf { v } ^ { ( 1 ) } = \mathbf { r } ^ { ( 0 ) } ;
$$

and, for $k = 1 , 2 , \ldots , n ,$

$$
\begin{array} { r l } & { t _ { k } = \frac { \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } , } \\ & { \mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + t _ { k } \mathbf { v } ^ { ( k ) } , } \\ & { \mathbf { r } ^ { ( k ) } = \mathbf { r } ^ { ( k - 1 ) } - t _ { k } A \mathbf { v } ^ { ( k ) } , } \\ & { \quad s _ { k } = \frac { \langle \mathbf { r } ^ { ( k ) } , \mathbf { r } ^ { ( k ) } \rangle } { \langle \mathbf { r } ^ { ( k - 1 ) } , \mathbf { r } ^ { ( k - 1 ) } \rangle } , } \\ & { ( k + 1 ) = \mathbf { r } ^ { ( k ) } + s _ { k } \mathbf { v } ^ { ( k ) } . } \end{array}
$$

Rather than presenting an algorithm for the conjugate gradient method using these for-mulas, we extend the method to include preconditioning.If the matrix $A$ is ill-conditioned, the conjugate gradient method is highly susceptible to.rounding errors. So,although the exact answer should be obtained in $\pmb { n }$ steps, this is not usually the case. As a direct method the conjugate gradient method is not as good as Gaussian elimination with pivoting. The main use of the conjugate gradient method is as an iterative method applied to a betterconditioned system. In this case an acceptable approximate solution is often obtained in about $\sqrt { n }$ steps.

To apply the method to a better-conditioned system, we want to select a nonsingular conditioning matrix $C$ so that

$$
\tilde { A } = C ^ { - 1 } A ( C ^ { - 1 } ) ^ { t }
$$

is beter conditioned.To simplify the notation,we will use the matrix $C ^ { \cdots t }$ to refer to $( C ^ { - 1 } ) ^ { t }$

Consider the linear system

$$
\tilde { A } \tilde { \mathbf { x } } = \tilde { \mathbf { b } } ,
$$

where $\tilde { \mathbf { x } } = C ^ { t } \mathbf { x }$ and ${ \tilde { \mathbf { b } } } = C ^ { - 1 } \mathbf { b }$ .Then

$$
\tilde { A } \tilde { \mathbf { x } } = ( C ^ { - 1 } A C ^ { - t } ) ( C ^ { t } \mathbf { x } ) = C ^ { - 1 } A \mathbf { x } .
$$

Thus, we could solve $\tilde { A } \tilde { \mathbf { x } } = \tilde { \mathbf { b } }$ for $\tilde { \mathbf { x } }$ and then obtain $\mathbf { x }$ by multiplying by $C ^ { - t }$ . However, instead of rewriting equations (7.30) using $\tilde { \mathbf { r } } ^ { ( k ) } , \tilde { \mathbf { v } } ^ { ( k ) } , \tilde { t } _ { k } , \tilde { \mathbf { x } } ^ { ( k ) }$ ,and $\tilde { s } _ { k }$ , we incorporate the preconditioning implicitly.

Since

$$
\tilde { \mathbf { x } } ^ { ( k ) } = C ^ { t } \mathbf { x } ^ { ( k ) } ,
$$

we have

$$
\tilde { \mathbf { r } } ^ { ( k ) } = \tilde { \mathbf { b } } - \tilde { A } \tilde { \mathbf { x } } ^ { ( k ) } = C ^ { - 1 } \mathbf { b } - ( C ^ { - 1 } A C ^ { - \iota } ) C ^ { \iota } \mathbf { x } ^ { ( k ) } = C ^ { - 1 } ( \mathbf { b } - A \mathbf { x } ^ { ( k ) } ) = C ^ { - 1 } \mathbf { r } ^ { ( k ) } .
$$

Let $\tilde { \mathbf { v } } ^ { ( k ) } = C ^ { t } \mathbf { v } ^ { ( k ) }$ and $\mathbf { w } ^ { ( k ) } = C ^ { - 1 } \mathbf { r } ^ { ( k ) }$ . Then

$$
\begin{array} { r } { \tilde { s } _ { k } = \frac { \langle \tilde { \mathbf { r } } ^ { ( k ) } , \tilde { \mathbf { r } } ^ { ( k ) } \rangle } { \langle \tilde { \mathbf { r } } ^ { ( k - 1 ) } , \tilde { \mathbf { r } } ^ { ( k - 1 ) } \rangle } = \frac { \langle C ^ { - 1 } \mathbf { r } ^ { ( k ) } , C ^ { - 1 } \mathbf { r } ^ { ( k ) } \rangle } { \langle C ^ { - 1 } \mathbf { r } ^ { ( k - 1 ) } , C ^ { - 1 } \mathbf { r } ^ { ( k - 1 ) } \rangle } , } \end{array}
$$

so

$$
\begin{array} { r } { \tilde { s } _ { k } = \frac { \langle \mathbf { w } ^ { ( k ) } , \mathbf { w } ^ { ( k ) } \rangle } { \langle \mathbf { w } ^ { ( k - 1 ) } , \mathbf { w } ^ { ( k - 1 ) } \rangle } . } \end{array}
$$

Thus,

$$
\tilde { t } _ { k } = \frac { \langle \tilde { \mathbf { r } } ^ { ( k - 1 ) } , \tilde { \mathbf { r } } ^ { ( k - 1 ) } \rangle } { \langle \tilde { \mathbf { v } } ^ { ( k ) } , \tilde { A } \tilde { \mathbf { v } } ^ { ( k ) } \rangle } = \frac { \langle C ^ { - 1 } \mathbf { r } ^ { ( k - 1 ) } , C ^ { - 1 } \mathbf { r } ^ { ( k - 1 ) } \rangle } { \langle C ^ { t } \mathbf { v } ^ { ( k ) } , C ^ { - 1 } A C ^ { - t } C ^ { t } \mathbf { v } ^ { ( k ) } \rangle } = \frac { \langle \mathbf { w } ^ { ( k - 1 ) } , \mathbf { w } ^ { ( k - 1 ) } \rangle } { \langle C ^ { t } \mathbf { v } ^ { ( k ) } , C ^ { - 1 } A \mathbf { v } ^ { ( k ) } \rangle }
$$

and

$$
\begin{array} { r } { \tilde { t } _ { k } = \frac { \langle \mathbf { w } ^ { ( k - 1 ) } , \mathbf { w } ^ { ( k - 1 ) } \rangle } { \langle \mathbf { v } ^ { ( k ) } , A \mathbf { v } ^ { ( k ) } \rangle } . } \end{array}
$$

Further,

$$
\tilde { \mathbf { x } } ^ { ( k ) } = \tilde { \mathbf { x } } ^ { ( k - 1 ) } + \tilde { t } _ { k } \tilde { \mathbf { v } } ^ { ( k ) } , \quad \mathsf { s o } \quad C ^ { t } \mathbf { x } ^ { ( k ) } = C ^ { t } \mathbf { x } ^ { ( k - 1 ) } + \tilde { t } _ { k } C ^ { t } \mathbf { v } ^ { ( k ) }
$$

and

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } + \tilde { t } _ { k } \mathbf { v } ^ { ( k ) } .
$$

Continuing,

$$
\tilde { \mathbf { r } } ^ { ( k ) } = \tilde { \mathbf { r } } ^ { ( k - 1 ) } - \tilde { t } _ { k } \tilde { A } \tilde { \mathbf { v } } ^ { ( k ) } ,
$$

so

$$
{ \cal C } ^ { - 1 } { \bf r } ^ { ( k ) } = { \cal C } ^ { - 1 } { \bf r } ^ { ( k - 1 ) } - \tilde { t } _ { k } { \cal C } ^ { - 1 } A { \cal C } ^ { - t } \tilde { v } ^ { ( k ) } , \qquad { \bf r } ^ { ( k ) } = { \bf r } ^ { ( k - 1 ) } - \tilde { t } _ { k } A { \cal C } ^ { - t } { \cal C } ^ { t } { \bf v } ^ { ( k ) } ,
$$

and

$$
\mathbf { r } ^ { ( k ) } = \mathbf { r } ^ { ( k - 1 ) } - \tilde { t } _ { k } A \mathbf { v } ^ { ( k ) } .
$$

Finally,

$$
\begin{array} { r } { \tilde { \mathbf { v } } ^ { ( k + 1 ) } = \tilde { \mathbf { r } } ^ { ( k ) } + \tilde { s } _ { k } \tilde { \mathbf { v } } ^ { ( k ) } \quad \mathrm { a n d } \quad C ^ { t } \mathbf { v } ^ { ( k + 1 ) } = C ^ { - 1 } \mathbf { r } ^ { ( k ) } + \tilde { s } _ { k } C ^ { t } \mathbf { v } ^ { ( k ) } , } \end{array}
$$

so

$$
\mathbf { v } ^ { ( k + 1 ) } = C ^ { - t } C ^ { - 1 } \mathbf { r } ^ { ( k ) } + \tilde { s } _ { k } \mathbf { v } ^ { ( k ) } = C ^ { - t } \mathbf { w } ^ { ( k ) } + \tilde { s } _ { k } \mathbf { v } ^ { ( k ) } .
$$

The preconditioned conjugate gradient method is based on using equations (7.31)-(35) in the order (7.32), (7.33),(7.34),(7.31), (7.35). Algorithm7.5 implements this procedure.

# Preconditioned Conjugate Gradient Method

To solve $\pmb { A } \mathbf { x } = \mathbf { b }$ given the preconditioning matrix $C ^ { - 1 }$ and the initial approximation $\mathbf { x } ^ { ( 0 ) }$ ：

INPUT the number of equations and unknowns $\pmb { n }$ ; the entries $a _ { i j }$ ， $1 \leq i , j \leq n$ of the matrix $\pmb { A }$ ; the entries $b _ { j }$ ， $1 \leq j \leq n$ of the vector $\mathbf { b }$ ; the entrie $\mathsf { s } \ \gamma _ { i j } , \mathsf { l } \ \le i , j \ \le n$ of the preconditioning matrix $\sum - 1$ , the entries $x _ { i }$ ， $1 \leq i \leq n$ of the initial approximation $\mathbf { x } = \mathbf { x } ^ { ( 0 ) }$ ， the maximum number of iterations $N$ ; tolerance TOL.

OUTPUT the approximate solution $x _ { 1 } , \ldots . x _ { n }$ and the residual $r _ { 1 } , \ldots r _ { n }$ or a message that the number of iterations was exceeded.

Step 1 Set $\begin{array} { r l } & { \mathrm {  ~ \cdot ~ } \mathbf { r } =  { \mathbf { b } } - A  { \mathbf { x } } ; ( C o m p u t e \ \mathbf { r } ^ { ( 0 ) } . ) } \\ & { \mathrm {  ~ \cdot ~ } \mathbf { w } = C ^ { - 1 }  { \mathbf { r } } ; ( N o t e \colon  { \mathbf { w } } =  { \mathbf { w } } ^ { ( 0 ) } ) } \\ & { \mathrm {  ~ \cdot ~ } \mathbf { v } = C ^ { - t }  { \mathbf { w } } ; ( N o t e \colon  { \mathbf { v } } =  { \mathbf { v } } ^ { ( 1 ) } ) } \\ & { \alpha = \sum _ { j = 1 } ^ { n } w _ { j } ^ { 2 } . } \end{array}$

Step 2 Set $k = 1$

Step 3 While $( k \leq N )$ do Steps 4--7.

Step 4If $\| \mathbf { v } \| < T O L$ ,then OUTPUT(‘Solution vector'; $x _ { 1 } , \ldots , x _ { n } )$ ； OUTPUT(‘with residual'; $r _ { 1 } , \ldots , r _ { n } )$ ； (The procedure was successful.) STOP

Step 5 Set $\mathbf { u } = A \mathbf { v }$ ； $( N o t e ; { \mathbf { u } } = A { \mathbf { v } } ^ { ( k ) } )$

$$
t = \frac { \alpha } { \sum _ { j = 1 } ^ { n } v _ { j } u _ { j } } ; ( N o t e \cdot t = t _ { k } )
$$

$$
\begin{array} { r l } & { \mathbf { x } = \mathbf { x } + t \mathbf { v } ; ( N o t e \colon \mathbf { x } = \mathbf { x } ^ { ( k ) } ) } \\ & { \mathbf { r } = \mathbf { r } - t \mathbf { u } ; ( N o t e \colon \mathbf { r } = \mathbf { r } ^ { ( k ) } ) } \\ & { \mathbf { w } = C ^ { - 1 } \mathbf { r } ; ( N o t e \colon \mathbf { w } = \mathbf { w } ^ { ( k ) } ) } \\ & { \beta = \sum _ { j = 1 } ^ { n } w _ { j \cdot } ^ { 2 } ( N o t e \colon \beta = \langle \mathbf { w } ^ { ( k ) } , \mathbf { w } ^ { ( k ) } \rangle ) } \end{array}
$$

Step 6If $| \beta | < T O L$ then if $\| \mathbf { r } \| < T O L$ then OUTPUT(‘Solution vector'; $x _ { 1 } , \ldots , x _ { n } )$ ； OUTPUT(with residual'; $r _ { 1 } , \ldots , r _ { n } )$ ； (The procedure was successful.) STOP

$$
\begin{array} { l } { \mathfrak { c } = \beta / \alpha ; ( s = s _ { k } ) } \\ { \mathbf { v } = C ^ { - t } \mathbf { w } + s \mathbf { v } ; ( N o t e \cdot \mathbf { v } = \mathbf { v } ^ { ( k + 1 ) } ) } \\ { \alpha = \beta ; ( U p d a t e \alpha . ) } \\ { k = k + 1 . } \end{array}
$$

Step 8If $( k > n )$ then OUTPUT (The maximum number of iterations was exceeded.'); (The procedure was unsuccessful.) STOP.

The next example illustrates the calculations in an easy problem.

The linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ given by

$$
\begin{array} { c c } { 4 x _ { 1 } + 3 x _ { 2 } } & { = 2 4 , } \\ { 3 x _ { 1 } + 4 x _ { 2 } - x _ { 3 } = 3 0 , } \\ { - } & { x _ { 2 } + 4 x _ { 3 } = - 2 4 } \end{array}
$$

has solution $( 3 , 4 , - 5 ) ^ { t }$ and was considered in Example 3 of Section 7.3. In that example, both the Gauss-Seidel method and SOR method were used. We will use the conjugate gradient method with no preconditioning, so $C = C ^ { - 1 } = I$ Let $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ .Then

$$
\begin{array} { r l } & { \mathbf { r } ^ { ( 0 ) } = \mathbf { b } - A \mathbf { x } ^ { ( 0 ) } = \mathbf { b } = ( 2 4 , 3 0 , - 2 4 ) ^ { t } ; } \\ & { \quad \mathbf { w } = C ^ { - 1 } \mathbf { r } ^ { ( 0 ) } = ( 2 4 , 3 0 , - 2 4 ) ^ { t } ; } \\ & { \quad \mathbf { v } ^ { ( 1 ) } = C ^ { - t } \mathbf { w } = ( 2 4 , 3 0 , - 2 4 ) ^ { t } ; } \\ & { \quad \alpha = \langle \mathbf { w } , \mathbf { w } \rangle = 2 0 5 2 . } \end{array}
$$

We start the first iteration with $k \simeq 1$ . Then

$$
\mathbf { u } = A \mathbf { v } ^ { ( 1 ) } = ( 1 8 6 . 0 , 2 1 6 . 0 , - 1 2 6 . 0 ) ^ { t } ;
$$

$$
t _ { 1 } = \frac { \alpha } { \langle \mathbf { v } ^ { ( 1 ) } , \mathbf { u } \rangle } = 0 . 1 4 6 9 0 7 2 1 6 5 ;
$$

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + t _ { 1 } \mathbf { v } ^ { ( 1 ) } = ( 3 . 5 2 5 7 7 3 1 9 6 , 4 . 4 0 7 2 1 6 4 9 5 , - 3 . 5 2 5 7 7 3 1 9 6 ) ^ { t } ;
$$

$$
{ \begin{array} { l } { \mathbf { r } ^ { ( 1 ) } = \mathbf { r } ^ { ( 0 ) } - t _ { 1 } \mathbf { u } = ( - 3 . 3 2 4 7 4 2 2 7 , - 1 . 7 3 1 9 5 8 7 6 , - 5 . 4 8 9 6 9 0 7 2 ) ^ { t } ; } \\ { \mathbf { w } = C ^ { - 1 } \mathbf { r } ^ { ( 1 ) } = \mathbf { r } ^ { ( 1 ) } ; } \\ { \displaystyle \beta = \langle \mathbf { w } , \mathbf { w } \rangle = 4 4 . 1 9 0 2 9 6 5 1 ; } \\ { s _ { 1 } = { \frac { \beta } { \alpha } } = 0 . 0 2 1 5 3 5 2 3 2 2 2 ; } \\ { \displaystyle \mathbf { v } ^ { ( 2 ) } = C ^ { - t } \mathbf { w } + s _ { 1 } \mathbf { v } ^ { ( 1 ) } = ( - 2 . 8 0 7 8 9 6 6 9 7 , - 1 . 0 8 5 9 0 1 7 9 3 , - 6 . 0 0 6 5 3 6 2 9 3 ) } \end{array} }
$$

Set

$$
\alpha = \beta = 4 4 . 1 9 0 2 9 6 5 1 .
$$

We are now ready to begin the second iteration. We have

$$
\begin{array} { r l } & { \mathbf { u } = A \mathbf { v } ^ { ( 2 ) } = ( - 1 4 . 4 8 9 2 9 2 1 7 , - 6 . 7 6 0 7 6 0 9 6 7 , - 2 2 . 9 4 0 2 4 3 3 8 ) ^ { t } ; } \\ & { t _ { 2 } = 0 . 2 3 7 8 1 5 7 5 5 8 ; } \\ & { \mathbf { x } ^ { ( 2 ) } = ( 2 . 8 5 8 0 1 1 1 2 1 , 4 . 1 4 8 9 7 1 9 3 9 , - 4 . 9 5 4 2 2 2 1 6 4 ) ^ { t } ; } \\ & { \mathbf { r } ^ { ( 2 ) } = ( 0 . 1 2 1 0 3 9 6 9 8 , - 0 . 1 2 4 1 4 3 2 8 1 , - 0 . 0 3 4 1 3 9 4 0 2 ) ^ { t } ; } \end{array}
$$

$$
\mathbf { w } = { C ^ { - 1 } } { \mathbf { r } } ^ { ( 2 ) } = { \mathbf { r } } ^ { ( 2 ) } ;
$$

$$
\beta = 0 . 0 3 1 2 2 7 6 6 1 4 8 ;
$$

$$
s _ { 2 } = 0 . 0 0 0 7 0 6 6 6 3 3 1 6 3 ;
$$

$$
\mathbf { v } ^ { ( 3 ) } = ( 0 . 1 1 9 0 5 5 4 5 0 4 , - 0 . 1 2 4 9 1 0 6 4 8 0 , - 0 . 0 3 8 3 8 4 0 0 0 8 6 ) ^ { t } .
$$

Set

$$
\alpha = \beta = 0 . 0 3 1 2 2 7 6 6 1 4 8 .
$$

Finally, the third iteration gives

$$
\begin{array} { r l } & { \mathbf { u } = A \mathbf { v } ^ { ( 3 ) } = ( 0 . 1 0 1 4 8 9 8 9 7 6 , - 0 . 1 0 4 0 9 2 2 0 9 9 , - 0 . 0 2 8 6 2 4 } \\ & { t _ { 3 } = 1 . 1 9 2 6 2 8 0 0 8 ; } \\ & { \mathbf { x } ^ { ( 3 ) } = ( 2 . 9 9 9 9 9 9 9 9 8 , 4 . 0 0 0 0 0 0 0 2 , - 4 . 9 9 9 9 9 9 9 9 8 ) ^ { t } ; } \\ & { \mathbf { r } ^ { ( 3 ) } = ( 0 . 3 6 \times 1 0 ^ { - 8 } , 0 . 3 9 \times 1 0 ^ { - 8 } , - 0 . 1 4 1 \times 1 0 ^ { - 8 } ) ^ { t } . } \end{array}
$$

Since $\mathbf { x } ^ { ( 3 ) }$ is nearly the exact solution,rounding eror did not significantly effect the result. In Example 3 of Section 7.3,the Gauss-Seidel method required 34 iterations,and the SOR method, with $\omega = 1 . 2 5$ , required 14 iterations for an accuracy of $1 0 ^ { - 7 }$ . It should be noted, however, that in this example, we are really comparing a direct method to iterative methods.

The next example illustrates the effect of preconditioning on a poorly conditioned matrix.In this example and subsequentlyweuse $D ^ { - 1 / 2 }$ torepresent thediagonal matrix whose entries are the reciprocals of the square roots of the diagonal entries of the coefficient matrix $A$

# EXAMPLE 3

The linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ with

$$
A = { \left[ \begin{array} { l l l l l } { 0 . 2 } & { 0 . 1 } & { 1 } & { 1 } & { 0 } \\ { 0 . 1 } & { 4 } & { - 1 } & { 1 } & { - 1 } \\ { 1 } & { - 1 } & { 6 0 } & { 0 } & { - 2 } \\ { 1 } & { 1 } & { 0 } & { 8 } & { 4 } \\ { 0 } & { - 1 } & { - 2 } & { 4 } & { 7 0 0 } \end{array} \right] } \quad { \mathrm { a n d } } \quad \mathbf { b } = { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 3 } \\ { 4 } \\ { 5 } \end{array} \right] }
$$

has the solution

x\* = (7.859713071,0.4229264082,-0.07359223906,-0.5406430164,0.01062616286).

The matrix $A$ is symmetric and positive definite but is ill-conditioned with condition number $K _ { \infty } ( A ) = 1 3 9 6 1 . 7 1$ . We will use tolerance O.O1 and compare the results obtained from the Jacobi, Gauss-Seidel,and SOR(with $\omega = 1 . 2 5 )$ iterative methods and from the con-jugate gradient method with $C ^ { - 1 } = I$ . Then we precondition by choosing $C ^ { - 1 }$ as $D ^ { - 1 / 2 }$ ， the diagonal matrix whose diagonal entries are the reciprocal of the positive square roots of the diagonal entries of the positive definite matrix $A$ . The results are presented in Table 7.5.The preconditioned conjugate gradient method gives the most accurate approximation with the smallest number of iterations. ■

Table 7.5   

<table><tr><td>Method</td><td>Number of Iterations</td><td>x(k）</td><td>ix*-x1）</td></tr><tr><td>Jacobi</td><td>49</td><td>(7.86277141, 0.42320802,-0.07348669, -0.53975964,0.01062847)t</td><td>0.00305834</td></tr><tr><td>Gauss-Seidel</td><td>15</td><td>(7.83525748, 0.42257868,-0.07319124, -0.53753055,0.01060903)</td><td>0.02445559</td></tr><tr><td>SOR (ω = 1.25)</td><td>7</td><td>(7.85152706, 0.42277371，-0.07348303, -0.53978369,0.01062286)</td><td>0.00818607</td></tr><tr><td>Conjugate Gradient</td><td>5</td><td>(7.85341523, 0.42298677,-0.07347963, -0.53987920,0.008628916)</td><td>0.00629785</td></tr><tr><td>Conjugate Gradient (Preconditioned)</td><td>4</td><td>(7.85968827, 0.42288329, -0.07359878, -0.54063200, 0.01064344)&#x27;</td><td>0.00009312</td></tr></table>

The preconditioned conjugate gradient method is often used in the solution of large linear systems in which the matrix is sparse and positive definite. These systems must be solved to approximate solutions to boundary-value problems in ordinary-differential equations (Sections 11.3,11.4,11.5). The larger the system, the more impressive the con-jugate gradient method becomes since it significantly reduces the number of iterations required. In these systems,the preconditioning matrix $C$ is approximately equal to $L$ in the Choleski factorization $L L ^ { t }$ of $A$ . Generally, small entries in $A$ are ignored and Choleski's method is applied to obtain what is called an incomplete $L L ^ { t }$ factorization of $A$ . Thus, $C ^ { - t } C ^ { - 1 } \approx A ^ { - 1 }$ and a good approximation is obtained. More information about the conjugate gradient method can be found in Kelley [Kelley].

# ExErcise Set 7.5

1. The linear system

$$
\begin{array} { c } { { x _ { 1 } + \displaystyle \frac { 1 } { 2 } x _ { 2 } = \displaystyle \frac { 5 } { 2 1 } , } } \\ { { \displaystyle \frac { 1 } { 2 } x _ { 1 } + \displaystyle \frac { 1 } { 3 } x _ { 2 } = \displaystyle \frac { 1 1 } { 8 4 } } } \end{array}
$$

has solution $( x _ { 1 } , x _ { 2 } ) ^ { t } = ( 1 / 6 , 1 / 7 ) ^ { t }$

a. Solve the linear system using Gaussan elimination with two-digit rounding arithmetic.   
b. Solve the linear system using the conjugate gradient method $\mathbf { \bar { \rho } } ( C = C ^ { - 1 } = I .$ ）with twodigit rounding arithmetic.   
c. Which method gives the better answer?   
d. Choose $C ^ { - 1 } = D ^ { - 1 / 2 }$ . Does this choice improve the conjugate gradient method?

2. The linear system

$$
\begin{array} { l l l } { 0 . 1 x _ { 1 } + 0 . 2 x _ { 2 } = 0 . 3 , } \\ { \qquad } \\ { 0 . 2 x _ { 1 } + 1 1 3 x _ { 2 } = 1 1 3 . 2 } \end{array}
$$

has solution $( x _ { 1 } , x _ { 2 } ) ^ { t } = ( 1 , 1 ) ^ { t }$ . Repeat the directions for Exercise 1 on this linear system.

3. The linear system

$$
{ \begin{array} { c } { x _ { 1 } + { \frac { 1 } { 2 } } x _ { 2 } + { \frac { 1 } { 3 } } x _ { 3 } = { \frac { 5 } { 6 } } , } \\ { { \frac { 1 } { 2 } } x _ { 1 } + { \frac { 1 } { 3 } } x _ { 2 } + { \frac { 1 } { 4 } } x _ { 3 } = { \frac { 5 } { 1 2 } } , } \\ { { \frac { 1 } { 3 } } x _ { 1 } + { \frac { 1 } { 4 } } x _ { 2 } + { \frac { 1 } { 5 } } x _ { 3 } = { \frac { 1 7 } { 6 0 } } } \end{array} }
$$

has solution $( 1 , - 1 , 1 ) ^ { t }$

a. Solve the linear system using Gaussian elimination with three-digit rounding arithmetic.   
b. Solve the linear system using the conjugate gradient method with three-digit rounding arithmetic.   
c. Does pivoting improve the answer in (a)?   
d. Repeat part (b) using $C ^ { - 1 } = D ^ { - 1 / 2 }$ . Does this improve the answer in (b)?

4.Repeat Exercise 3 using single-precision arithmetic on a computer.

5. Perform only two steps of the conjugate gradient method with $C = C ^ { - 1 } = I$ on each of the following linear systems. Compare the results in parts (b), (c), (d),and $\mathbf { \eta } ( \mathbf { f } )$ to those obtained in Exercises 1,2,and 5 of Section 7.3.

$$
\begin{array} { r l r l } { { 3 } x _ { 1 } - } & { x _ { 2 } + } & { x _ { 3 } = 1 , } & & { \mathbf { b } . \quad 1 0 x _ { 1 } - } & { x _ { 2 } } \\ & { - x _ { 1 } + 6 x _ { 2 } + 2 x _ { 3 } = 0 , } & & { - x _ { 1 } + 1 0 x _ { 2 } - } & { 2 x _ { 3 } = 7 , } \\ & { } & { x _ { 1 } + 2 x _ { 2 } + 7 x _ { 3 } = 4 , } & & { - } & { 2 x _ { 2 } + 1 0 x _ { 3 } = 6 . } \\ & { } & { 1 0 x _ { 1 } + } & { 5 x _ { 2 } } & { = 6 , } & { 4 x _ { 1 } + } & { x _ { 2 } - } & { x _ { 3 } + } \\ & { } & { 5 x _ { 1 } + 1 0 x _ { 2 } - 4 x _ { 3 } } & { = 2 5 , } & & { x _ { 1 } + 4 x _ { 2 } - } & { x _ { 3 } - } & { x _ { 4 } = - 1 , } \\ & { - } & { 4 x _ { 2 } + 8 x _ { 3 } - x _ { 4 } = - 1 1 , } & & { - x _ { 1 } - } & { x _ { 2 } + 5 x _ { 3 } + } & { x _ { 4 } = 0 , } \\ & { } & { - } & { x _ { 3 } + 5 x _ { 4 } = - 1 1 . } & & { x _ { 1 } - } & { x _ { 2 } + } & { x _ { 3 } + 3 x _ { 4 } = 1 . } \end{array}
$$

$$
\begin{array} { r l r } { { 4 } x _ { 1 } + ~ x _ { 2 } + ~ x _ { 3 } + ~ } & { x _ { 5 } = 6 , } \\ { ~ x _ { 1 } + 3 x _ { 2 } + ~ x _ { 3 } + ~ x _ { 4 } ~ } & { = 6 , } \\ { ~ x _ { 1 } + ~ x _ { 2 } + 5 x _ { 3 } - ~ x _ { 4 } - ~ x _ { 5 } = 6 , } \\ { ~ x _ { 2 } - ~ x _ { 3 } + 4 x _ { 4 } ~ } & { = 6 , } \\ { ~ x _ { 1 } ~ } & { - ~ x _ { 3 } + ~ } & { + 4 x _ { 5 } = 6 . } \end{array}
$$

$$
\begin{array} { r l r l r l } & { 4 x _ { 1 } - } & { x _ { 2 } } & { - } & { x _ { 4 } } & & { = 0 , } \\ & { - x _ { 1 } + 4 x _ { 2 } - } & { x _ { 3 } } & { - } & { x _ { 5 } } & { = 5 , } \\ & { - } & { x _ { 2 } + 4 x _ { 3 } } & & { - } & { x _ { 6 } = 0 , } \\ & { - x _ { 1 } } & & { + 4 x _ { 4 } - } & { x _ { 5 } } & { = 6 , } \\ & { - } & { x _ { 2 } } & { - } & { x _ { 4 } + 4 x _ { 5 } - } & { x _ { 6 } = - 2 , } \\ & { - } & { x _ { 3 } } & & { - } & { x _ { 5 } + 4 x _ { 6 } = 6 . } \end{array}
$$

6.Repeat Exercise 5 using $C ^ { - 1 } = D ^ { - 1 / 2 }$ .

7.Repeat Exercise 5 with $T O L = 1 0 ^ { - 3 }$ in the ${ l } _ { \infty }$ norm. Compare the results in parts $( { \mathfrak { b } } )$ ，(c)， (d）, and (f) to those obtained in Exercises 3,4,and 7 of Section 7.3.

8.Repeat Exercise 7 using $C ^ { - 1 } = D ^ { - 1 / 2 }$ .

9.Use (i) the Jacobi Method,(ii) the Gauss-Seidel method,(ii) the SOR method with $\omega = 1 . 3$ ， and (iv) the conjugate gradient method and preconditioning with $C ^ { - 1 } = D ^ { - 1 / 2 }$ to find solutions to the linear system $\pmb { A } \mathbf { x } = \mathbf { b }$ to within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm.

a.

$$
a _ { i , j } = \left\{ \begin{array} { l l } { 4 , } & { \mathrm { w h e n } ~ j = i ~ \mathrm { a n d } ~ i = 1 , 2 , \ldots , 1 6 , } \\ & { } \\ { \qquad \quad } \\ { - 1 , } & { \mathrm { w h e n } \left\{ \begin{array} { l l } { j = i + 1 ~ \mathrm { a n d } ~ i = 1 , 2 , 3 , 5 , 6 , 7 , 9 , 1 0 , 1 1 , 1 3 , 1 4 , 1 5 , } \\ { j = i - 1 ~ \mathrm { a n d } ~ i = 2 , 3 , 4 , 6 , 7 , 8 , 1 0 , 1 1 , 1 2 , 1 4 , 1 5 , 1 6 , } \\ { j = i + 4 ~ \mathrm { a n d } ~ i = 1 , 2 , \ldots , 1 2 , } \\ { j = i - 4 ~ \mathrm { a n d } ~ i = 5 , 6 , \ldots , 1 6 , } \\ { 0 , } & { \mathrm { o t h e r w i s e } } \end{array} \right. } \end{array} \right.
$$

and

b.

$$
a _ { i , j } = \{ \begin{array} { l l } { \displaystyle { { j = i + 1 \mathrm { ~ a n d ~ } i = \{ 1 , 2 , 3 , 4 , 6 , 7 , 8 , 9 , 1 1 , 1 2 , 1 3 , 1 4 , } _ { }  } }  \\ { \displaystyle { 1 6 , 1 7 , 1 8 , 1 9 , 2 1 , 2 2 , 2 3 , 2 4 , } } \\ { \displaystyle { - 1 , } } \\ { \displaystyle { { \mathrm { ~ w h e n } \{ \begin{array} { l l } { \displaystyle { j = i - 1 \mathrm { ~ a n d ~ } i = \{ 2 , 3 , 4 , 5 , 7 , 8 , 9 , 1 0 , 1 2 , 1 3 , 1 4 , 1 5 , } } \\ { \displaystyle { 1 7 , 1 8 , 1 9 , 2 0 , 2 2 , 2 3 , 2 4 , 2 5 , } } \\ { \displaystyle { j = i + 5 \mathrm { ~ a n d ~ } i = 1 , 2 , \dots , 2 0 , } } \\ { \displaystyle { j = i - 5 \mathrm { ~ a n d ~ } i = 6 , 7 , \dots , 2 5 , } } \end{array}  } } } \end{array} 
$$

and

$$
 { \mathbf { b } } = ( 1 , 0 , - 1 , 0 , 2 , 1 , 0 , - 1 , 0 , 2 , 1 , 0 , - 1 , 0 , 2 , 1 , 0 , - 1 , 0 , 2 , 1 , 0 , - 1 , 0 , 2 , 1 , 0 , - 1 , 0 , 2 ) ^ { t }
$$

c.

$$
a _ { i , j } = \left\{ \begin{array} { l l } { 2 i , } & { \mathrm { w h e n } j = i \mathrm { ~ a n d ~ } i = 1 , 2 , \dots , 4 0 , } \\ { } \\ { - 1 , } & { \mathrm { w h e n } \left\{ { j = i + 1 \mathrm { ~ a n d } i = 1 , 2 , \dots , 3 9 , } \right. } \\ { } \\ { 0 , } & { \mathrm { o t h e r w i s e } } \end{array} \right.
$$

and $b _ { i } = 1 . 5 i - 6$ ,for each $i = 1 , 2 , \dots , 4 0$

10.Solve the linear system in Exercise 12(a) and $( 6 )$ of Section 7.3 using the conjugate gradient method with $C ^ { - 1 } = I$

11.Let

$$
A _ { 1 } = \left[ { \begin{array} { r r r r r } { 4 } & { - 1 } & { 0 } & { 0 } \\ { - 1 } & { 4 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 4 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { 4 } \end{array} } \right] , \quad - I = \left[ { \begin{array} { r r r r r } { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - 1 } \end{array} } \right] ,
$$

$$
\begin{array} { r } { 0 = \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] . } \end{array}
$$

Form the $1 6 \times 1 6$ matrix $A$ in partitioned form,

$$
\begin{array} { r } { A = \left[ \begin{array} { c c c c } { A _ { 1 } } & { - I } & { 0 } & { 0 } \\ { - I } & { A _ { 1 } } & { - I } & { 0 } \\ { 0 } & { - I } & { A _ { 1 } } & { - I } \\ { 0 } & { 0 } & { - I } & { A _ { 1 } } \end{array} \right] . } \end{array}
$$

Let $ { \mathbf { b } } = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0 , 1 , 2 , 3 , 4 , 5 , 6 ) ^ { t } .$

a. Solve $\pmb { A } \mathbf { x } = \mathbf { b }$ using the conjugate gradient method with tolerance 0.05.   
$\mathbf { b } _ { \bullet }$ Solve $\mathbf { A } \mathbf { x } = \mathbf { b }$ using the preconditioned conjugate gradient method with $C ^ { - 1 } = D ^ { - 1 / 2 }$ and tolerance 0.05.   
c. Is there any tolerance for which the methods of part (a) and part (b) require a different number of iterations?

12.Use the transpose properties given in Theorem 6.13 to prove Theorem 7.30.

13.a.Show that an $A$ -orthogonal set of nonzero vectors associated with a positive definite matrix is linearly independent. b. Show that if $\{ \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 2 ) } , \dots , \mathbf { v } ^ { ( n ) } \}$ is a set of $A$ -orthogonal nonzero vectors in $\mathbb { R }$ and $\pmb { z } ^ { t } \mathbf { v } ^ { ( i ) } = \pmb { 0 }$ ,for each $i = 1 , 2 , \dots , n$ , then ${ \pmb z } = { \pmb 0 }$

14.Prove Theorem 7.33 using mathematical induction as folows:

a.Show that $\left. \mathbf { r } ^ { ( 1 ) } , \mathbf { v } ^ { ( 1 ) } \right. = 0$   
b. Assume that $\left\{ \mathbf { r } ^ { ( k ) } , \mathbf { v } ^ { ( j ) } \right\} = 0$ ,for each $k \leq l$ and $j = 1 , 2 , \dots , k .$ and show that this implies that $\left. \mathbf { \dot { r } } ^ { ( \ell + 1 ) } , \mathbf { v } ^ { ( j ) } \right. = 0$ ,for each $j = 1 , 2 , \dots , l$   
c. Show that $\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. = 0$

# 7.6 Survey of Methods and Software

In this chapter we have studied iterative techniques to approximate the solution of linear systems. We began with the Jacobi method and the Gauss-Seidel method to introduce the iterative methods. Both methods require an arbitrary initial approximation $\mathbf { x } ^ { ( 0 ) }$ and generate a sequence of vectors $\mathbf { x } ^ { ( i + 1 ) }$ using an equation of the form

$$
\begin{array} { r } { \mathbf { x } ^ { ( i + 1 ) } = T \mathbf { x } ^ { ( i ) } + \mathbf { c } . } \end{array}
$$

It was noted that the method will converge if and only if the spectral radius of the iteration matrix $\rho ( T ) < 1$ , and the smaller the spectral radius, the faster the convergence. Analysis of the residual vectors of the Gauss-Seidel technique led to the SOR iterative method, which involves a parameter $\omega$ to speed convergence.

These iterative methods and modifications are used extensively in the solution of lin-ear systems which arise in the numerical solution of boundary value problems and partial differential equations (see Chapters 1 and 12). These systems are often very large, on the order of 10000 equations in 1Ooo unknowns,and are sparse with their nonzero entries in predictable positions. The iterative methods are also useful for other large sparse systems and are easily adapted for efficient use on parallel computers.

Almost all commercial and public domain packages that contain iterative methods for the solution of a linear system of equations require a preconditioner to be used with the method.Faster convergence of iterative solvers is often achieved by using a preconditioner. A preconditioner produces an equivalent system of equations that hopefully exhibits better convergence characteristics than the original system. The IMSL Library has the subroutine PCGRC, which is a preconditioned conjugate gradient method. The NAG Library has several subroutines,which are prefixed F11, for the iterative solution of linear systems. All of the subroutines are based on Krylov subspaces. Saad [Sa2] has a detailed description of Krylov subspace methods. The packages LINPACK and LAPACK contain only direct methods for the solution of linear systems; however, the packages do contain many subroutines that are used by the iterative solvers. The public domain packages $\mathbf { I M L + } +$ ,ITPACK, SLAP,and Templates,contain iterative methods.MATLAB contains several iterative methods that are also based on Krylov subspaces.For example, the command $x = \mathrm { P C G } ( A , b )$ executes the preconditioned conjugate gradient method to solve the linear system $A x = b$ Some optional input parameters for PCG are, TOL a tolerance for convergence, MAXIT the maximum number of iterations,and M a preconditioner.

The concepts of condition number and poorly conditioned matrices were introduced in Section 7.4. Many of the subroutines for solving a linear system or for factoring a matrix into an $L U$ factorization include checks for il-conditioned matrices and also give an estimate of the condition number.

The subroutine SGETRF in LAPACK factors the real matrix $A$ into an $L U$ factorization and gives the row ordering for the permutation matrix $P$ ，where $P A = L U$ .The subroutine SGECON gives the reciprocal of the condition number of $A$ using the $L U$ factorization computed by SGETRF. LAPACK also has subroutines to estimate the condition number for special matrices. For example, SPOTRF performs the Choleski factorization of a positive definite matrix A,and SPOCON estimates the reciprocal of the condition number using the Choleski factorization computed by SPOTRF.

The IMSL Library has subroutines that estimate the condition number. For example, the subroutine LFCRG computes an $L U$ factorization $P A = L U$ of the matrix $A$ and also gives an estimate of the condition number. The NAG Library has similar subroutines.

LAPACK, LINPACK, the IMSL Library, and the NAG Library have subroutines that improve on a solution to a linear system that is poorly conditioned. The subroutines test the condition number and then use iterative refinement to obtain the most accurate solution possible given the precision of the computer.

More information on the use of iterative methods for solving linear systems can be found in Varga [Var], Young [Y], Hageman and Young [HY],and in the recent book by Axelsson [Ax]. Iterative methods for large sparse systems are discussed in Barrett et al [Barr], Hackbusch [Hac], Kelley [Kelley], and Saad [Sa2].

CHAPTER

8

# Approximation Theory

Ho of uniform material, the length of the spring is a linear function of that force. We can write the linear function as F(l) = k(l - E), where F(l) represents the force required to stretch the spring l units, the constant E represents the length of the spring with no force applied, and the constant $\pmb { k }$ is the spring constant.

![](images/48d7aaa481e7e36221c7a5ce2115db6213a1e352cccc0e45f8a976fc8dbde6c0.jpg)

![](images/6ba74fe67ab18219021260b7704cb495135f38bf72475e4ec776f8366264e2eb.jpg)

Suppose we want to determine the spring constant for a spring that has initial length 5.3 in. We apply forces of 2, 4, and 6 Ib to the spring and find that its length increases to 7.0, 9.4, and 12.3 in., respectively. A quick examination shows that the points (0, 5.3), (2, 7.0), (4, 9.4), and (6, 12.3) do not quite lie in a straight line. Although we could simply use one random pair of these data points to approximate the spring constant, it would seem more reasonable to find the line that best approximates all the data points to determine the constant. This type of approxima-tion will be considered in this chapter, and this spring application can be found in Exercise 7 of Section 8.1.

The study of approximation theory involves two general types of problems. One problem arises when a function is given explicitly, but we wish to find a“simpler” type of function, such as a polynomial, that can be used to determine approximate values of the given function. The other problem in approximation theory is concerned with fitting functions to given data and finding the “best" function in a certain class to represent the data.

Both problems have been touched upon in Chapter 3. The Taylor polynomial of degree n about the number xo is an excellent approximation to an (n+1)-times differentiable function $f$ in a small neighborhood of $x _ { 0 }$ . The Lagrange interpolating polynomials, or, more generally, osculatory polynomials, were discussed both as approximating polynomials and as polynomials to fit certain data. Cubic splines were also discussed in that chapter. In this chapter, limitations to these techniques are considered, and other avenues of approach are discussed.

# 8.1 Discrete Least Squares Approximation

Consider the problem of estimating the values of a function at nontabulated points, given the experimental data in Table 8.1.

Table 8.1   

<table><tr><td>Xi</td><td>Xi</td><td>yi</td></tr><tr><td>1</td><td>1.3</td><td>6</td></tr><tr><td>2</td><td>3.5</td><td>7</td></tr><tr><td>3</td><td>4.2</td><td>8 12.5</td></tr><tr><td>4</td><td>5.0</td><td>9</td></tr><tr><td>5</td><td>7.0</td><td>10 15.6</td></tr></table>

Figure 8.1 shows a graph of the values in Table 8.1. From this graph, it appears that the actual relationship between $\pmb { x }$ and y is linear. The likely reason that no line precisely fits the data is because of errors in the data. So it is unreasonable to require that the approximating function agree exactly with the data. In fact, such a function would introduce oscillations that were not originally present. For example, the ninth degree interpolating polynomial on the data shown in Figure 8.2 is obtained in Maple using the commands

>p:=interp([1,2,3,4,5,6,7,8,9,10], [1.3,3.5,4.2,5.0,7.0,8.8,10.1,12.5,13.0,15.6],x);   
>plot({p}, $\tt { x } { = } 1$ ..10);

This polynomial is clearly a poor predictor of information between a number of the data points. A beter approach would be to find the “best”(in some sense) approximating line, even if it does not agree precisely with the data at any point.

![](images/b4e50a1a2e6c1ed49c648203c146378644f3daeac6eca326f29e0be9e8c097b7.jpg)  
Figure 8.1

![](images/ce4e97a57d7ef94d54eaf7119c5ef3ffe7360819a7dee05f91ba421a85c102a5.jpg)  
Figure 8.2

Let $a _ { 1 } x _ { i } + a _ { 0 }$ denote the ith value on the approximating line and $y _ { i }$ be the ith given $y -$ value. The problem of finding the equation of the best linear approximation in the absolute sense requires that values of $a _ { 0 }$ and $a _ { 1 }$ be found to minimize

$$
E _ { \infty } ( a _ { 0 } , a _ { 1 } ) = \operatorname* { m a x } _ { 1 \leq i \leq 1 0 } \{ | y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) | \} .
$$

This is commonly called a minimax problem and cannot be handled by elementary techniques.

Another approach to determining the best linear approximation involves finding values of $a _ { 0 }$ and $a _ { 1 }$ to minimize

$$
{ \cal E } _ { 1 } ( a _ { 0 } , a _ { 1 } ) = \sum _ { i = 1 } ^ { 1 0 } | y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) | .
$$

This quantity is called the absolute deviation. To minimize a function of two variables, we need to set its partial derivatives to zero and simultaneously solve the resulting equations. In the case of the absolute deviation, we need to find $a _ { 0 }$ and $a _ { 1 }$ with

$$
0 = \frac { \partial } { \partial a _ { 0 } } \sum _ { i = 1 } ^ { 1 0 } | y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) | \quad \mathrm { a n d } \quad 0 = \frac { \partial } { \partial a _ { 1 } } \sum _ { i = 1 } ^ { 1 0 } | y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) | .
$$

The diffculty is that the absolute-value function is not differentiable at zero,and we may not be able to find solutions to this pair of equations.

The least squares approach to this problem involves determining the best approximating line when the error involved is the sum of the squares of the differences between the $y$ -values on the approximating line and the given $y$ -values.Hence, constants $a _ { 0 }$ and $a _ { 1 }$ must be found that minimize the least squares error:

$$
{ \cal E } _ { 2 } ( a _ { 0 } , a _ { 1 } ) = \sum _ { i = 1 } ^ { 1 0 } [ y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) ] ^ { 2 } .
$$

The least squares method is the most convenient procedure for determining best linear approximations,but there are also important theoretical considerations that favor it. The minimax approach generally assigns too much weight to a bit of data that is badly in error,whereas the absolute deviation method does not give sufficient weight to a point that is considerably out of line with the approximation. The least squares approach puts substantially more weight on a point that is out of line with the rest of the data but will not allow that point to completely dominate the approximation. An additional reason for considering the least squares approach involves the study of the statistical distribution of error. (See [Lar, pp. 463-481].)

The general problem of fitting the best least squares line to a collection of data $\{ ( x _ { i } , y _ { i } ) \} _ { i = 1 } ^ { m }$ involves minimizing the total error,

$$
E \equiv E _ { 2 } ( a _ { 0 } , a _ { 1 } ) = \sum _ { i = 1 } ^ { m } \left[ y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) \right] ^ { 2 } ,
$$

with respect to the parameters $a _ { 0 }$ and $a _ { 1 }$ . For a minimum to occur, we need

$$
0 = { \frac { \cdot \partial } { \partial a _ { 0 } } } \sum _ { i = 1 } ^ { m } [ ( y _ { i } - ( a _ { 1 } x _ { i } - a _ { 0 } ) ] ^ { 2 } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - a _ { 1 } x _ { i } - a _ { 0 } ) ( - 1 )
$$

and

$$
0 = \frac { \partial } { \partial a _ { 1 } } \sum _ { i = 1 } ^ { m } [ y _ { i } - ( a _ { 1 } x _ { i } + a _ { 0 } ) ] ^ { 2 } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - a _ { 1 } x _ { i } - a _ { 0 } ) ( - x _ { i } ) .
$$

These equations simplify to the normal equations:

$$
a _ { 0 } \cdot m + a _ { 1 } \sum _ { i = 1 } ^ { m } x _ { i } = \sum _ { i = 1 } ^ { m } y _ { i } \quad { \mathrm { a n d } } \quad a _ { 0 } \sum _ { i = 1 } ^ { m } x _ { i } + a _ { 1 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } x _ { i } y _ { i } .
$$

The solution to this system of equations is

$$
a _ { 0 } = { \frac { \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } \sum _ { i = 1 } ^ { m } y _ { i } - \sum _ { i = 1 } ^ { m } x _ { i } y _ { i } \sum _ { i = 1 } ^ { m } x _ { i } } { m \left( \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } \right) - \left( \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } \right) ^ { 2 } } }
$$

and

$$
a _ { 1 } = \frac { m \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } y _ { i } - \sum _ { i = 1 } ^ { m } x _ { i } \sum _ { i = 1 } ^ { m } y _ { i } } { m \left( \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } \right) - \left( \displaystyle \sum _ { i = 1 } ^ { m } x _ { i } \right) ^ { 2 } } .
$$

# EXAMPLE 1

Consider the data presented in Table 8.1. To find the least squares line approximating this data,extend the table and sum the columns,as shown in the third and fourth columns of Table 8.2.

Table 8.2   

<table><tr><td>Xi</td><td>yi</td><td>x²</td><td>xiyi</td><td>P(xi)= 1.538xi- 0.360</td></tr><tr><td>1</td><td>1.3</td><td>1</td><td>1.3</td><td>1.18</td></tr><tr><td>2</td><td>3.5</td><td>4</td><td>7.0</td><td>2.72</td></tr><tr><td>3</td><td>4.2</td><td>9</td><td>12.6</td><td>4.25</td></tr><tr><td>4</td><td>5.0</td><td>16</td><td>20.0</td><td>5.79</td></tr><tr><td>5</td><td>7.0</td><td>25</td><td>35.0</td><td>7.33</td></tr><tr><td>6</td><td>8.8</td><td>36</td><td>52.8</td><td>8.87</td></tr><tr><td>7</td><td>10.1</td><td>49</td><td>70.7</td><td>10.41</td></tr><tr><td>8</td><td>12.5</td><td>64</td><td>100.0</td><td>11.94</td></tr><tr><td>9</td><td>13.0</td><td>81</td><td>117.0</td><td>13.48</td></tr><tr><td>10</td><td>15.6</td><td>100</td><td>156.0</td><td>15.02</td></tr><tr><td>55</td><td>81.0</td><td>385</td><td>572.4</td><td>E=</td></tr></table>

The normal equations (8.1) and (8.2) imply that

$$
a _ { 0 } = { \frac { 3 8 5 ( 8 1 ) - 5 5 ( 5 7 2 . 4 ) } { 1 0 ( 3 8 5 ) - ( 5 5 ) ^ { 2 } } } = - 0 . 3 6 0
$$

and

$$
a _ { 1 } = \frac { 1 0 ( 5 7 2 . 4 ) - 5 5 ( 8 1 ) } { 1 0 ( 3 8 5 ) - ( 5 5 ) ^ { 2 } } = 1 . 5 3 8 ,
$$

so $P ( x ) = 1 . 5 3 8 x - 0 . 3 6 0$ . The graph of this line and the data points are shown in Figure 8.3.The approximate values given by the least squares technique at the data points are in Table 8.2. □

![](images/f1a1e9de50d8e1f136db70b0d31a61d17776f61e51f800cbe6c53ce141674c71.jpg)  
Figure 8.3

The general problem of approximating a set of data $\{ ( x _ { i } , y _ { i } ) \mid i = 1 , 2 , \ldots , m \}$ ,with an algebraic polynomial

$$
P _ { n } ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 } ,
$$

of degree $n < m - 1$ , using the least squares procedure is handled in a similar manner. We choose the constants $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ to minimize the least squares error

$$
\begin{array} { r l } & { E _ { 2 } = \displaystyle \sum _ { i = 1 } ^ { m } ( y _ { i } - P _ { n } ( x _ { i } ) ) ^ { 2 } } \\ & { = \displaystyle \sum _ { i = 1 } ^ { m } y _ { i } ^ { 2 } - 2 \sum _ { i = 1 } ^ { m } P _ { n } ( x _ { i } ) y _ { i } + \sum _ { i = 1 } ^ { m } ( P _ { n } ( x _ { i } ) ) ^ { 2 } } \\ & { = \displaystyle \sum _ { i = 1 } ^ { m } y _ { i } ^ { 2 } - 2 \sum _ { i = 1 } ^ { m } \left( \sum _ { j = 0 } ^ { n } a _ { j } x _ { i } ^ { j } \right) y _ { i } + \sum _ { i = 1 } ^ { m } \left( \sum _ { j = 0 } ^ { n } a _ { j } x _ { i } ^ { j } \right) ^ { 2 } } \\ & { = \displaystyle \sum _ { i = 1 } ^ { m } y _ { i } ^ { 2 } - 2 \sum _ { j = 0 } ^ { n } a _ { j } \left( \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { j } \right) + \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } a _ { j } a _ { k } \left( \sum _ { i = 1 } ^ { m } x _ { i } ^ { j - k } \right) . } \end{array}
$$

As in the linear case, for $E$ to be minimized it is necessary that $\partial E / \partial a _ { j } = 0$ , for each $j = 0 , 1 , \ldots , n$ . Thus, for each $j$ ，

$$
0 = \frac { \partial E } { \partial a _ { j } } = - 2 \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { j } + 2 \sum _ { k = 0 } ^ { n } a _ { k } \sum _ { i = 1 } ^ { m } x _ { i } ^ { j + k } .
$$

This gives $n + 1$ normal equations in the $n + 1$ unknowns $a _ { j }$ ，

$$
\sum _ { k = 0 } ^ { n } a _ { k } \sum _ { i = 1 } ^ { m } x _ { i } ^ { j + k } = \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { j } , \quad { \mathrm { f o r } } \operatorname { e a c h } j = 0 , 1 , \dots , n .
$$

It is helpful to write the equations as follows:

$$
a _ { 0 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 0 } + a _ { 1 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 1 } + a _ { 2 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } + \cdot \cdot \cdot + a _ { n } \sum _ { i = 1 } ^ { m } x _ { i } ^ { n } = \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { 0 } ,
$$

$$
a _ { 0 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 1 } + a _ { 1 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 } + a _ { 2 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 3 } + \cdot \cdot \cdot + a _ { n } \sum _ { i = 1 } ^ { m } x _ { i } ^ { n + 1 } = \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { 1 } ,
$$

$$
a _ { 0 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { n } + a _ { 1 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { n + 1 } + a _ { 2 } \sum _ { i = 1 } ^ { m } x _ { i } ^ { n + 2 } + \cdot \cdot \cdot + a _ { n } \sum _ { i = 1 } ^ { m } x _ { i } ^ { 2 n } = \sum _ { i = 1 } ^ { m } y _ { i } x _ { i } ^ { n } .
$$

These normal equations have a unique solution provided that the $x _ { i }$ are distinct (see Exercise 14).

# EXAMPLE 2

Fit the data in Table 8.3 with the discrete least squares polynomial of degree 2.For this problem, $n = 2$ ， $m = 5$ ,and the three normal equations are

$$
5 a _ { 0 } + \mathrm { ~ \small ~ \beta ~ } 2 . 5 a _ { 1 } + \mathrm { ~ \small ~ 1 . 8 7 5 a _ { 2 } = 8 . 7 6 8 0 } ,
$$

$$
2 . 5 a _ { 0 } + 1 . 8 7 5 a _ { 1 } + 1 . 5 6 2 5 a _ { 2 } = 5 . 4 5 1 4
$$

$$
1 . 8 7 5 a _ { 0 } + 1 . 5 6 2 5 a _ { 1 } + 1 . 3 8 2 8 a _ { 2 } = 4 . 4 0 1 5 .
$$

Table 8.3   

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>xi</td><td>0</td><td>0.25</td><td>0.50</td><td>0.75</td><td>1.00</td></tr><tr><td>y</td><td>1.0000</td><td>1.2840</td><td>1.6487</td><td>2.1170</td><td>2.7183</td></tr></table>

We can solve this system using a CAS. In Maple, we first define the equations

>eq1: $= 5 * \mathsf { a } 0 + 2 . 5 * \mathsf { a } 1 + 1 . 8 7 5 * \mathsf { a } 2 = 8 . 7 6 8 0 ;$ >eq2: $\bullet 2$ · $5 * 2 0 + 1$ .875\*a1+1.5625\*a2 $\mathtt { \beta } = 5$ .4514;>eq3: $\mathit { \Pi } = 1$ .875\*a0+1.5625\*a1+1.3828\*a2=4.4015;

To solve the system we enter

$$
> { \tt s o l v e } ( \left\{ { \tt e q 1 , e q 2 , e q 3 } \right\} , \left\{ { \tt a 0 , a 1 , a 2 } \right\} ;
$$

which gives, with Digits: $= 5$ ；

$$
a _ { 0 } = 1 . 0 0 5 1 , \quad a _ { 1 } = 0 . 8 6 4 6 8 , \quad \mathrm { a n d } \quad a _ { 2 } = 0 . 8 4 3 1 6 .
$$

Thus, the least squares polynomial of degree 2 fiting the preceding data is $P _ { 2 } ( x ) =$ $1 . 0 0 5 1 + 0 . 8 6 4 6 8 x + 0 . 8 4 3 1 6 x ^ { 2 }$ , whose graph is shown in Figure 8.4. At the given values of $x _ { i }$ we have the approximations shown in Table 8.4.

The total error,

$$
E _ { 2 } = \sum _ { i = 1 } ^ { 5 } ( y _ { i } - P ( x _ { i } ) ) ^ { 2 } = 2 . 7 4 \times 1 0 ^ { - 4 } ,
$$

is the least that can be obtained by using a polynomial of degree at most 2.

![](images/55dd188189c98f89e5b385f44efcf900a8f049cbf16c7e0a2fd385f776b50be5.jpg)  
Figure 8.4

# Table 8.4

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Xi</td><td>0</td><td>0.25</td><td>0.50</td><td>0.75</td><td>1.00</td></tr><tr><td>yi</td><td>1.0000</td><td>1.2840</td><td>1.6487</td><td>2.1170</td><td>2.7183</td></tr><tr><td>P(xi)</td><td>1.0051</td><td>1.2740</td><td>1.6482</td><td>2.1279</td><td>2.7129</td></tr><tr><td>yi-P(xi)</td><td>-0.0051</td><td>0.0100</td><td>0.0004</td><td>-0.0109</td><td>0.0054</td></tr></table>

Maple has a function called fit in the stats library to compute discrete least squares approximations. We can compute the approximation in Example 2 using the Mapie code

>with(stats)

>xvals: $\mathbf { \eqcirc }$ [0,0.25,0.5,0.75,1];   
>yvals: $\eqsim$ [1,1.284,1.6487,2.117,2.7183];   
>z:=fit[leastsquare[[x,y],y=a\*x^2 + b\*x + c，{a,b,c} ]] ([xvals,yvals]);

Maple returns the result

$$
z : = y = . 8 4 3 6 5 7 1 4 2 9 x ^ { 2 } + . 8 6 4 1 8 2 8 5 7 1 x + 1 . 0 0 5 1 3 7 1 4 3
$$

To obtain an approximation $y ( 1 . 7 )$ , we enter

>evalf(subs $( \textbf { x } = \textbf { 1 . 7 } , z ) )$ ；

to get $y = 4 . 9 1 2 4 1 7 1 4 3$ ·

Occasionally it is appropriate to assume that the data are exponentially related. This requires the approximating function to be of the form

$$
y = b e ^ { a x }
$$

or

$$
y = b x ^ { a } ,
$$

for some constants $\pmb { a }$ and $b$ . The difficulty with applying the least squares procedure in a situation of this type comes from attempting to minimize

$$
E = \sum _ { i = 1 } ^ { m } ( y _ { i } - b e ^ { a x _ { i } } ) ^ { 2 } , \quad { \mathrm { i n ~ t h e ~ c a s e ~ o f ~ E q . ~ } } ( 8 . 4 ) ,
$$

or

$$
E = \sum _ { i = 1 } ^ { m } ( y _ { i } - b x _ { i } ^ { a } ) ^ { 2 } , \quad { \mathrm { i n ~ t h e ~ c a s e ~ o f ~ } } \operatorname { E q . } ( 8 . 5 ) .
$$

The normal equations associated with these procedures are obtained from either

$$
0 = { \frac { \partial E } { \partial b } } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - b e ^ { a x _ { i } } ) ( - e ^ { a x _ { i } } )
$$

and

$$
0 = \frac { \partial E } { \partial a } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - b e ^ { a x _ { i } } ) ( - b x _ { i } e ^ { a x _ { i } } ) , \quad \mathrm { i n ~ t h e ~ c a s e ~ o f ~ E q . ~ ( 8 . 4 ) }
$$

or

$$
0 = { \frac { \partial E } { \partial b } } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - b x _ { i } ^ { a } ) ( - x _ { i } ^ { a } )
$$

and

$$
0 = \frac { \partial E } { \partial a } = 2 \sum _ { i = 1 } ^ { m } ( y _ { i } - b x _ { i } ^ { a } ) ( - b ( \ln x _ { i } ) x _ { i } ^ { a } ) , \quad \mathrm  i n ~ t h e ~ c a s e ~ o f ~ E q . ~ ( 8 . 
$$

No exact solution to either of these systems in $a$ and $b$ can generally be found.

The method that is commonly used when the data are suspected to be exponentially related is to consider the logarithm of the approximating equation:

$$
\ln y = \ln b + a x
$$

and

$$
\ln y = \ln b + a \ln x ,
$$

In either case, a linear problem now appears, and solutions for ln $b$ and $a$ can be obtained by appropriately modifying the normal equations (8.1) and (8.2).

However, the approximation obtained in this manner is not the least squares approximation for the original problem, and this approximation can in some cases differ significantly from the least squares approximation to the original problem. The application in Exercise 13 describes such a problem. This application will be reconsidered as Exercise 7 in Section 10.3,where the exact solution to the exponential least squares problem is approximated by using methods suitable for solving nonlinear systems of equations.

# EXAMPle 3

# Table 8.5

Consider the collection of data in the first three columns of Table 8.5.   

<table><tr><td>i</td><td>Xi</td><td>yi</td><td>ln yi</td><td>x</td><td>xi ln yi</td></tr><tr><td>1</td><td>1.00</td><td>5.10</td><td>1.629</td><td>1.0000</td><td>1.629</td></tr><tr><td>2</td><td>1.25</td><td>5.79</td><td>1.756</td><td>1.5625</td><td>2.195</td></tr><tr><td>3</td><td>1.50</td><td>6.53</td><td>1.876</td><td>2.2500</td><td>2.814</td></tr><tr><td>4</td><td>1.75</td><td>7.45</td><td>2.008</td><td>3.0625</td><td>3.514</td></tr><tr><td>5</td><td>2.00</td><td>8.46</td><td>2.135</td><td>4.0000</td><td>4.270</td></tr><tr><td>7.50</td><td></td><td></td><td>9.404</td><td>11.875</td><td>14.422</td></tr></table>

If $x _ { i }$ is graphed with In $y _ { i }$ , the data appear to have a linear relation, so it is reasonable to assume an approximation of the form

$$
y = b e ^ { a x } \quad { \mathrm { o r } } \quad { \mathrm { l n ~ } } y = { \mathrm { l n ~ } } b + a x .
$$

Extending the table and summing the appropriate columns gives the remaining data in Table 8.5.

Using the normal equations (8.1) and (8.2),

$$
a = { \frac { ( 5 ) ( 1 4 . 4 2 2 ) - ( 7 . 5 ) ( 9 . 4 0 4 ) } { ( 5 ) ( 1 1 . 8 7 5 ) - ( 7 . 5 ) ^ { 2 } } } = 0 . 5 0 5 6
$$

and

$$
\ln b = { \frac { ( 1 1 . 8 7 5 ) ( 9 . 4 0 4 ) - ( 1 4 . 4 2 2 ) ( 7 . 5 ) } { ( 5 ) ( 1 1 . 8 7 5 ) - ( 7 . 5 ) ^ { 2 } } } = 1 . 1 2 2 .
$$

Since $b = e ^ { 1 . 1 2 2 } = 3 . 0 7 1$ ,the approximation assumes the form

$$
y = 3 . 0 7 1 e ^ { 0 . 5 0 5 6 x } ,
$$

which,at the data points, gives the values in Table 8.6. (See Figure 8.5.)

# Table 8.6

<table><tr><td>i</td><td>X</td><td>yi</td><td>3.071e0.5056xi</td></tr><tr><td>1</td><td>1.00</td><td>5.10</td><td>5.09</td></tr><tr><td>2</td><td>1.25</td><td>5.79</td><td>5.78</td></tr><tr><td>3</td><td>1.50</td><td>6.53</td><td>6.56</td></tr><tr><td>4</td><td>1.75</td><td>7.45</td><td>7.44</td></tr><tr><td>5</td><td>2.00</td><td>8.46</td><td>8.44</td></tr></table>

![](images/13e8e1de2a91c536df437a63ceaaae2df8dfbf5fb84021df3073253fdcaaf983.jpg)  
Figure 8.5

# ExErcise Set 8.1

1.Compute the linear least squares polynomial for the data of Example 2.

2.Compute the least squares polynomial of degree 2 for the data of Example 1,and compare the total error $E$ for the two polynomials.

3. Find the least squares polynomials of degrees 1,2,and 3 for the data in the folowing table. Compute the error $E$ in each case. Graph the data and the polynomials.

<table><tr><td>Xi</td><td>1.0</td><td>1.1</td><td>1.3</td><td>1.5</td><td>1.9</td><td>2.1</td></tr><tr><td>yi</td><td>1.84</td><td>1.96</td><td>2.21</td><td>2.45</td><td>2.94</td><td>3.18</td></tr></table>

4. Find the least squares polynomials of degrees 1, 2,and 3 for the data in the following table. Compute the error $E$ in each case. Graph the data and the polynomials.

<table><tr><td>xi</td><td>0</td><td>0.15</td><td>0.31</td><td>0.5</td><td>0.6</td><td>0.75</td></tr><tr><td>yi</td><td>1.0</td><td>1.004</td><td>1.031</td><td>1.117</td><td>1.223</td><td>1.422</td></tr></table>

5.Given the data:

<table><tr><td>4.2 x:4.0 102.56 yi</td><td>4.5 113.18 130.11 142.05 167.53 195.14 224.87 256.73 299.50 326.72</td><td>4.7</td><td>5.1</td><td>5.5</td><td>5.9</td><td>6.3</td><td>6.8</td><td>7.1</td></tr></table>

a.Construct the least squares polynomial of degree 1, and compute the error.

b.Construct the least squares polynomial of degree 2,and compute the error.

c. Construct the least squares polynomial of degree 3,and compute the error.

d. Construct the least squares approximation of the form $b e ^ { a x }$ , and compute the error.

e.Construct the least squares approximation of the form $b x ^ { a }$ , and compute the error.

6. Repeat Exercise 5 for the following data.

<table><tr><td>xi</td><td>0.2</td><td>0.3</td><td>0.6</td><td>0.9</td><td>1.1</td><td>1.3</td><td>1.4</td><td>1.6</td></tr><tr><td>yi</td><td>0.050446</td><td>0.098426</td><td>0.33277</td><td>0.72660</td><td>1.0972</td><td>1.5697</td><td>1.8487</td><td>2.5015</td></tr></table>

7.In the lead example of this chapter, an experiment was described to determine the spring constant $k$ in Hooke's law:

$$
F ( l ) = k ( l - E ) .
$$

The function $F$ is the force required to stretch the spring $l$ units, where the constant $E = 5 . 3$ in. is the length of the unstretched spring.

a. Suppose measurements are made of the length $l$ , in inches,for applied weights $F ( l )$ ,in pounds,as given in the following table.

<table><tr><td></td></tr><tr><td>F(l) 1</td></tr><tr><td>2 7.0</td></tr><tr><td>4 9.4</td></tr><tr><td>6 12.3</td></tr><tr><td></td></tr></table>

Find the least squares approximation for $k$ b.Additional measurements are made, giving more data:

<table><tr><td colspan="2"></td></tr><tr><td>F(1)</td><td>1</td></tr><tr><td>3</td><td>8.3</td></tr><tr><td>5</td><td>11.3</td></tr><tr><td>8</td><td>14.4</td></tr><tr><td>10</td><td>15.9</td></tr></table>

Compute the new least squares approximation for $k$ . Which of (a)or(b) best fits the total experimental data?

8.The follwing list contains homework grades and the final-examination grades for 30 numerical analysis students. Find the equation of the least squares line for this data,and use this line to determine the homework grade required to predict minimal A $( 9 0 \% )$ and D $( 6 0 \% )$ grades on the final.

<table><tr><td>Homework</td><td>Final Homework</td><td>Final</td></tr><tr><td>302 45</td><td>323</td><td>83</td></tr><tr><td>325</td><td>72 337</td><td>99</td></tr><tr><td>285 54</td><td>337</td><td>70</td></tr><tr><td>339 54</td><td>304</td><td>62</td></tr><tr><td>334 79</td><td>319</td><td>66</td></tr><tr><td>322 65</td><td>234</td><td>51</td></tr><tr><td>331 99</td><td>337</td><td>53</td></tr><tr><td>279 63</td><td>351</td><td>100</td></tr><tr><td>316 65</td><td>339</td><td>67</td></tr><tr><td>347 99</td><td>343</td><td>83</td></tr><tr><td>343 83</td><td>314</td><td>42</td></tr><tr><td>290 74</td><td>344</td><td>79</td></tr><tr><td>326</td><td>76 185</td><td>59</td></tr><tr><td>233</td><td>57 340</td><td>75</td></tr><tr><td>254</td><td>45 316</td><td>45</td></tr></table>

9. The following table lists the college grade-point averages of 20 mathematics and computer sci-ence majors, together with the scores that these students received on the mathematics portion of the ACT(American College Testing Program) test while in high school. Plot these data, and find the equation of the least squares line for this data.

<table><tr><td>ACT score</td><td>Grade-point ACT average score</td><td>Grade-point average</td></tr><tr><td>28</td><td>3.84 29</td><td>3.75</td></tr><tr><td>25</td><td>3.21</td><td>28 3.65</td></tr><tr><td>28</td><td>3.23 27</td><td>3.87</td></tr><tr><td>27</td><td>3.63</td><td>3.75</td></tr><tr><td>28</td><td>29 3.75 21</td><td>1.66</td></tr><tr><td>33</td><td>3.20 28</td><td>3.12</td></tr><tr><td>28</td><td>3.41 28</td><td>2.96</td></tr><tr><td>29</td><td>3.38 26</td><td>2.92</td></tr><tr><td>23</td><td>3.53 30</td><td></td></tr><tr><td>27</td><td>2.03 24</td><td>3.10 2.81</td></tr></table>

10. The following set of data, presented to the Senate Antitrust Subcommitee, shows the compar-ative crash-survivability characteristics of cars in various classes. Find the least squares line that approximates these data. (The table shows the percent of accident-involved vehicles in which the most severe injury was fatal or serious.)

<table><tr><td>Type</td><td>Average Weight</td><td>Percent Occurrence</td></tr><tr><td>1. Domestic luxury regular</td><td>4800 1b</td><td>3.1</td></tr><tr><td>2. Domestic intermediate regular</td><td>3700 1b</td><td>4.0</td></tr><tr><td>3.Domestic economy regular</td><td>3400 1b</td><td>5.2</td></tr><tr><td>4.Domestic compact</td><td>2800 1b</td><td>6.4</td></tr><tr><td>5.Foreign compact</td><td>1900 1b</td><td>9.6</td></tr><tr><td></td><td></td><td></td></tr></table>

11. To determine a relationship between the number of fish and the number of species of fish in samples taken for a portion of the Great Barrier Reef, P. Sale and R. Dybdahl [SD] fit a linear least squares polynomial to the following collection of data, which were collected in samples over a 2-year period. Let $\pmb { x }$ be the number of fish in the sample and y be the number of species in the sample.

<table><tr><td>x</td><td>y</td><td>x</td><td>y</td><td>X</td><td>y</td></tr><tr><td>13</td><td>11</td><td>29</td><td>12</td><td>60</td><td>14</td></tr><tr><td>15</td><td>10</td><td>30</td><td>14</td><td>62</td><td>21</td></tr><tr><td>16</td><td>11</td><td>31</td><td>16</td><td>64</td><td>21</td></tr><tr><td>21</td><td>12</td><td>36</td><td>17</td><td>70</td><td>24</td></tr><tr><td>22</td><td>12</td><td>40</td><td>13</td><td>72</td><td>17</td></tr><tr><td>23</td><td>13</td><td>42</td><td>14</td><td>100</td><td>23</td></tr><tr><td>25</td><td>13</td><td>55</td><td>22</td><td>130</td><td>34</td></tr></table>

Determine the linear least squares polynomial for these data.

12. To determine a functional relationship between the attenuation coefficient and the thickness of a sample of taconite, V. P. Singh [Si] fits a collection of data by using a linear least squares polynomial. The following collection of data is taken from a graph in that paper. Find the linear least squares polynomial fiting these data.

<table><tr><td>Thickness (cm)</td><td>Attenuation coefficient (dB/cm)</td></tr><tr><td>0.040</td><td>26.5</td></tr><tr><td>0.041</td><td>28.1</td></tr><tr><td>0.055</td><td>25.2</td></tr><tr><td>0.056</td><td>26.0</td></tr><tr><td>0.062</td><td>24.0</td></tr><tr><td>0.071</td><td>25.0</td></tr><tr><td>0.071</td><td>26.4</td></tr><tr><td>0.078</td><td>27.2</td></tr><tr><td>0.082</td><td>25.6</td></tr><tr><td>0.090</td><td>25.0</td></tr><tr><td>0.092</td><td>26.8</td></tr><tr><td>0.100</td><td>24.8</td></tr><tr><td>0.105</td><td>27.0</td></tr><tr><td>0.120</td><td>25.0</td></tr><tr><td>0.123</td><td>27.3</td></tr><tr><td>0.130</td><td>26.9</td></tr><tr><td>0.140</td><td>26.2</td></tr></table>

13. In a paper dealing with the efficiency of energy utilization of the larvae of the modest sphinx moth (Pachysphinx modesta),L. Schroeder [Schr1] used the following data to determine a relation between $W$ , the live weight of the larvae in grams, and $R$ , the oxygen consumption of the larvae in milliliters/hour. For biological reasons, it is assumed that a relationship in the form of $R = b W ^ { a }$ exists between $W$ and $R$

a.Find the logarithmic linear least squares polynomial by using

$$
\ln R = \ln b + a \ln W .
$$

b.Compute the error associated with the approximation in part (a):

$$
E = \sum _ { i = 1 } ^ { 3 7 } ( R _ { i } - b W _ { i } ^ { a } ) ^ { 2 } .
$$

c. Modify the logarithmic least squares equation in part (a) by adding the quadratic term $c ( \ln W _ { i } ) ^ { 2 }$ ,and determine the logarithmic quadratic least squares polynomial.

d.Determine the formula for and compute the error associated with the approximation in part (c).

<table><tr><td>W</td><td>R</td><td>W</td><td>R</td><td>W</td><td>R</td><td>W</td><td>R</td><td>W</td><td>R</td></tr><tr><td>0.017</td><td>0.154</td><td>0.025</td><td>0.23</td><td>0.020</td><td>0.181</td><td>0.020</td><td>0.180</td><td>0.025</td><td>0.234</td></tr><tr><td>0.087</td><td>0.296</td><td>0.111</td><td>0.357</td><td>0.085</td><td>0.260</td><td>0.119</td><td>0.299</td><td>0.233</td><td>0.537</td></tr><tr><td>0.174</td><td>0.363</td><td>0.211</td><td>0.366</td><td>0.171</td><td>0.334</td><td>0.210</td><td>0.428</td><td>0.783</td><td>1.47</td></tr><tr><td>1.11</td><td>0.531</td><td>0.999</td><td>0.771</td><td>1.29</td><td>0.87</td><td>1.32</td><td>1.15</td><td>1.35</td><td>2.48</td></tr><tr><td>1.74</td><td>2.23</td><td>3.02</td><td>2.01</td><td>3.04</td><td>3.59</td><td>3.34</td><td>2.83</td><td>1.69</td><td>1.44</td></tr><tr><td>4.09</td><td>3.58</td><td>4.28</td><td>3.28</td><td>4.29</td><td>3.40</td><td>.5.48</td><td>4.15</td><td>2.75</td><td>1.84</td></tr><tr><td>5.45</td><td>3.52</td><td>4.58</td><td>2.96</td><td>5.30</td><td>3.88</td><td></td><td></td><td>4.83</td><td>4.66</td></tr><tr><td>5.96</td><td>2.40</td><td>4.68</td><td>5.10</td><td></td><td></td><td></td><td></td><td>5.53</td><td>6.94</td></tr></table>

14. Show that the normal equations (8.3) resulting from discrete least squares approximation yield a symmetric and nonsingular matrix and hence have a unique solution. [Hint: Let $A = ( a _ { i j } )$ ， where

$$
a _ { i j } = \sum _ { k = 1 } ^ { m } x _ { k } ^ { i + j - 2 }
$$

and $x _ { 1 } , x _ { 2 } , \ldots , x _ { m }$ are distinct with $n < m - 1$ . Suppose $\pmb { A }$ is singular and that $\mathfrak { c } \neq \mathbf { 0 }$ is such that $\mathbf { c } ^ { t } A \mathbf { c } = \mathbf { 0 }$ . Show that the $\pmb { n }$ th-degree polynomial whose coeficients are the coordinates of c has more than $\pmb { n }$ roots,and use this to establish a contradiction.]

# 8.2Orthogonal Polynomials and Least Squares Approximation

The previous section considered the problem of least squares approximation to fit a collction of data. The other approximation problem mentioned in the introduction concerns the approximation of functions.

Suppose $f \in C [ a , b ]$ and that a polynomial $P _ { n } ( x )$ of degree at most $\pmb { n }$ is required that will minimize the error

$$
\int _ { a } ^ { b } [ f ( x ) - P _ { n } ( x ) ] ^ { 2 } d x .
$$

To determine a least squares approximating polynomial; hat is,a polynomial to minimize this expression, let

$$
P _ { n } ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 } = \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } ,
$$

and define, as shown in Figure 8.6,

$$
E \equiv E ( a _ { 0 } , a _ { 1 } , \dots , a _ { n } ) = \int _ { a } ^ { b } \left( f ( x ) - \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } \right) ^ { 2 } d x .
$$

![](images/e56e71782cf37a0efe9c0199531fbcbeb012a59f8a6d202a96238d00579927c3.jpg)  
Figure 8.6

The problem is to find real coefficients $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ that will minimize $E$ . A neces-sary condition for the numbers $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ to minimize $E$ is that

$$
{ \frac { \partial E } { \partial a _ { j } } } = 0 , \quad { \mathrm { f o r } } \operatorname { e a c h } j = 0 , 1 , \dots , n .
$$

Since

$$
E = \int _ { a } ^ { b } [ f ( x ) ] ^ { 2 } d x - 2 \sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { k } f ( x ) d x + \int _ { a } ^ { b } \left( \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } \right) ^ { 2 } d x ,
$$

we have

$$
{ \frac { \partial E } { \partial a _ { j } } } = - 2 \int _ { a } ^ { b } x ^ { j } f ( x ) d x + 2 \sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x .
$$

Hence, to find $P _ { n } ( x )$ ,the $( n + 1 )$ linear normal equations

$$
\sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = \int _ { a } ^ { b } x ^ { j } f ( x ) d x , \quad { \mathrm { f o r } } { \mathrm { c a c h } } j = 0 , 1 , \dots , n ,
$$

must be solved for the $( n + 1 )$ unknowns $a _ { j }$ . The normal equations always have a unique solution provided $f \in C [ a , b ]$ .(See Exercise 15.)

# EXAMPLE 1

Find the least squares approximating polynomial of degree 2 for the function $f ( x ) =$ sin $\pi x$ on the interval [O,1]. The normal equations for $P _ { 2 } ( x ) = a _ { 2 } x ^ { 2 } + a _ { 1 } x + a _ { 0 } $ are

$$
\begin{array} { c } { { a _ { 0 } \displaystyle \int _ { 0 } ^ { 1 } 1 d x + a _ { 1 } \int _ { 0 } ^ { 1 } x d x + a _ { 2 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } d x = \int _ { 0 } ^ { 1 } \sin \pi x d x , } } \\ { { { } } } \\ { { a _ { 0 } \displaystyle \int _ { 0 } ^ { 1 } x d x + a _ { 1 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } d x + a _ { 2 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 3 } d x = \int _ { 0 } ^ { 1 } x \sin \pi x d x , } } \\ { { { } } } \\ { { a _ { 0 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 2 } d x + a _ { 1 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 3 } d x + a _ { 2 } \displaystyle \int _ { 0 } ^ { 1 } x ^ { 4 } d x = \int _ { 0 } ^ { 1 } x ^ { 2 } \sin \pi x d x . } } \end{array}
$$

Performing the integration yields

$$
\iota _ { 0 } + \frac { 1 } { 2 } a _ { 1 } + \frac { 1 } { 3 } a _ { 2 } = \frac { 2 } { \pi } , \frac { 1 } { 2 } a _ { 0 } + \frac { 1 } { 3 } a _ { 1 } + \frac { 1 } { 4 } a _ { 2 } = \frac { 1 } { \pi } , \frac { 1 } { 3 } a _ { 0 } + \frac { 1 } { 4 } a _ { 1 } + \frac { 1 } { 5 } a _ { 2 } = \frac { \pi ^ { 2 } - 4 } { \pi ^ { 3 } } .
$$

These three equations in three unknowns can be solved to obtain

$$
a _ { 0 } = { \frac { 1 2 \pi ^ { 2 } - 1 2 0 } { \pi ^ { 3 } } } \approx - 0 . 0 5 0 4 6 5 \quad { \mathrm { a n d } } \quad a _ { 1 } = - a _ { 2 } = { \frac { 7 2 0 - 6 0 \pi ^ { 2 } } { \pi ^ { 3 } } } \approx 4 . 1 2 2 5 1 .
$$

Consequently, the least squares polynomial approximation of degree 2 for $f ( x ) = \sin \pi x$ on [0,1] is $P _ { 2 } ( x ) = - 4 . 1 2 2 5 1 x ^ { 2 } + 4 . 1 2 2 5 1 x - 0 . 0 5 0 4 6 5 . { \mathrm { ( S e e } }$ Figure 8.7 on page 500.

Example 1 illustrates the difficulty in obtaining a least squares polynomial approximation. An $( n + 1 ) \times ( n + 1 )$ linear system for the unknowns $a _ { 0 } , \ldots , a _ { n }$ must be solved, and the coefficients in the linear system are of the form

$$
\int _ { a } ^ { b } x ^ { j + k } d x = { \frac { b ^ { j + k + 1 } - a ^ { j + k + 1 } } { j + k + 1 } } ,
$$

![](images/e4745f03ff17206939ab634bfb58401b3cd1a1c18200c8e4d4673b796ff4ed58.jpg)  
Figure 8.7

a linear system that does not have an easily computed numerical solution. The matrix in the linear system is known as a Hilbert matrix, which is a clasic example for demonstrating roundoff error difficulties. (See Exercise 6 of Section 7.4.)

Another disadvantage is similar to the situation that occurred when the Lagrange polynomials were first introduced in Section 3.1. The calculations that were performed in obtaining the best $\pmb { n }$ th-degree polynomial, $P _ { n } ( x )$ , do not lessen the amount of work required to obtain $P _ { n + 1 } ( x )$ , the polynomial of next higher degree.

A different technique to obtain least squares approximations will now be considered. This turns out to be computationally efficient, and once $P _ { n } ( x )$ is known, it is easy to determine $P _ { n + 1 } ( x )$ . To facilitate the discussion, we need some new concepts.

# Definition 8.1

The set of functions $\{ \phi _ { 0 } , \ldots , \phi _ { n } \}$ is said to be linearly independent on $[ a , b ]$ if, whenever

$$
c _ { 0 } \phi _ { 0 } ( x ) + c _ { 1 } \phi _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } \phi _ { n } ( x ) = 0 , \quad \mathrm { f o r ~ a l l } \ x \in [ a , b ] ,
$$

we have $c _ { 0 } = c _ { 1 } = \cdot \cdot \cdot = c _ { n } = 0$ . Otherwise the set of functions is said to be linearly dependent.

# Theorem 8.2

If $\phi _ { j } ( x )$ is a polynomial of degree $j$ , for each $j = 0 , 1 , \ldots , n$ ,then $\{ \phi _ { 0 } , \ldots , \phi _ { n } \}$ is linearly independent on any interval $[ a , b ]$

Proof Suppose $c _ { 0 } , \ldots , c _ { n }$ are real numbers for which

$$
P ( x ) = c _ { 0 } \phi _ { 0 } ( x ) + c _ { 1 } \phi _ { 1 } ( x ) + \cdot \cdot \cdot + c _ { n } \phi _ { n } ( x ) = 0 , \quad \mathrm { f o r ~ a l l ~ } x \in [ a , b ] .
$$

The polynomial $P ( x )$ vanishes on $[ a , b ]$ , so it must be the zero polynomial, and the coefficients of all the powers of $x$ are zero. In particular, the coefficient of $x ^ { n }$ is zero. Since

$c _ { n } \phi _ { n } ( x )$ is the only term in $P ( x )$ that contains $x ^ { n }$ ,we must have $c _ { n } = 0$ and

$$
P ( x ) = \sum _ { j = 0 } ^ { n - 1 } c _ { j } \phi _ { j } ( x ) .
$$

In this representation of $P ( x )$ ， the only term that contains a power of $x ^ { n - 1 }$ is $c _ { n - 1 } \phi _ { n - 1 } ( x )$ , so this term must also be zero and

$$
P ( x ) = \sum _ { j = 0 } ^ { n - 2 } c _ { j } \phi _ { j } ( x ) .
$$

In like manner, the remaining constants $C _ { n - 2 } , C _ { n - 3 } , \ldots , c _ { 1 } , c _ { 0 }$ are all zero, which implies that $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } \}$ is linearly independent. ■ ■ 1

# EXAMPLE 2

Let $\phi _ { 0 } ( x ) = 2 , \phi _ { 1 } ( x ) = x - 3$ ,and $\phi _ { 2 } ( x ) = x ^ { 2 } + 2 x + 7 \qquad $ By Theorem 8.2, $\displaystyle \{ \phi _ { 0 } , \phi _ { 1 } , \phi _ { 2 } \}$ is linearly independent on any interval $[ a , b ]$ . Suppose $Q ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 }$ . We will show that there exist constants $c _ { 0 } , c _ { 1 }$ ,and $c _ { 2 }$ such that $Q ( x ) = c _ { 0 } \phi _ { 0 } ( x ) + c _ { 1 } \phi _ { 1 } ( x ) + c _ { 2 } \phi _ { 2 } ( x )$ · First note that

$$
1 = \frac { 1 } { 2 } \phi _ { 0 } ( x ) , \quad x = \phi _ { 1 } ( x ) + 3 = \phi _ { 1 } ( x ) + \frac { 3 } { 2 } \phi _ { 0 } ( x ) ,
$$

and

$$
\begin{array} { l } { { \displaystyle x ^ { 2 } = \phi _ { 2 } ( x ) - 2 x - 7 = \phi _ { 2 } ( x ) - 2 \left[ \phi _ { 1 } ( x ) + \frac { 3 } { 2 } \phi _ { 0 } ( x ) \right] - 7 \left[ \frac { 1 } { 2 } \phi _ { 0 } ( x ) \right] } } \\ { { \displaystyle \quad = \phi _ { 2 } ( x ) - 2 \phi _ { 1 } ( x ) - \frac { 1 3 } { 2 } \phi _ { 0 } ( x ) . } } \end{array}
$$

Hence,

$$
\begin{array} { l } { { Q ( x ) = a _ { 0 } \left[ \displaystyle \frac { 1 } { 2 } \phi _ { 0 } ( x ) \right] + a _ { 1 } \left[ \phi _ { 1 } ( x ) + \displaystyle \frac { 3 } { 2 } \phi _ { 0 } ( x ) \right] + a _ { 2 } \left[ \phi _ { 2 } ( x ) - 2 \phi _ { 1 } ( x ) - \displaystyle \frac { 1 3 } { 2 } \phi _ { 0 } ( x ) \right] } } \\ { { \mathrm { } } } \\ { { { } = \left( \displaystyle \frac { 1 } { 2 } a _ { 0 } + \displaystyle \frac { 3 } { 2 } a _ { 1 } - \displaystyle \frac { 1 3 } { 2 } a _ { 2 } \right) \phi _ { 0 } ( x ) + [ a _ { 1 } - 2 a _ { 2 } ] \phi _ { 1 } ( x ) + a _ { 2 } \phi _ { 2 } ( x ) , } } \end{array}
$$

so any quadratic polynomial can be expressed as a linear combination of $\phi _ { 0 } ( x ) , \phi _ { 1 } ( x )$ ,and $\phi _ { 2 } ( x )$ ·

The situation illustrated in Example 2 holds in a much more general seting. Let $\prod _ { n }$ be the set of all polynomials of degree at most n. The following result is used extensively in many applications of linear algebra. Its proof is considered in Exercise 13.

f $\{ \phi _ { 0 } ( x ) , \phi _ { 1 } ( x ) , \ldots , \phi _ { n } ( x ) \}$ is a collection of linearly independent polynomials in $\prod _ { n }$ ， then any polynomial in $\prod _ { n }$ can be written uniquely as a linear combination of $\phi _ { 0 } ( x )$ ， $\phi _ { 1 } ( x ) , \ldots , \phi _ { n } ( x )$

To discuss general function approximation requires the introduction of the notions of weight functions and orthogonality.

# Definition 8.4

An integrable function $w$ is called a weight function on the interval $I$ if $w ( x ) \geq 0$ ,for all $x$ in $I$ ,but $w ( x ) \not \equiv 0$ on any subinterval of $I$

The purpose of a weight function is to assign varying degrees of importance to approximations on certain portions of the interval. For example, the weight function

$$
w ( x ) = \frac { 1 } { \sqrt { 1 - x ^ { 2 } } }
$$

places less emphasis near the center of the interval $( - 1 , 1 )$ and more emphasis when $\left| x \right|$ is near 1 (see Figure 8.8). This weight function is used in the next section.

![](images/85e759a33c605eb9b205495f17d507b81599aa478ac9173f03e8c363fd64eb4b.jpg)  
Figure 8.8

Suppose $\left\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } \right\}$ is a set of linearly independent functions on $[ a , b ]$ ， $w$ is a weight function for $[ a , b ]$ ,and, for $f \in C [ a , b ]$ , a linear combination

$$
P ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } \phi _ { k } ( x )
$$

is sought to minimize the error

$$
E ( a _ { 0 } , \dots , a _ { n } ) = \int _ { a } ^ { b } w ( x ) \biggl [ f ( x ) - \sum _ { k = 0 } ^ { n } a _ { k } \phi _ { k } ( x ) \biggr ] ^ { 2 } d x .
$$

This problem reduces to the situation considered at the beginning of this section in the special case when $w ( x ) \equiv 1$ and $\phi _ { k } ( x ) = x ^ { k }$ ,for each $k = 0 , 1 , \ldots , n$

The normal equations associated with this problem are derived from the fact that for each $j = 0 , 1 , \ldots , n .$ ，

$$
0 = { \frac { \partial E } { \partial a _ { j } } } = 2 \int _ { a } ^ { b } w ( x ) \Biggl [ f ( x ) - \sum _ { k = 0 } ^ { n } a _ { k } \phi _ { k } ( x ) \Biggr ] \phi _ { j } ( x ) d x .
$$

The system of normal equations can be written

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \phi _ { j } ( x ) \ d x = \sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } w ( x ) \phi _ { k } ( x ) \phi _ { j } ( x ) \ d x , \quad { \mathrm { f o r ~ } } j = 0 , 1 , \dots , n .
$$

If the functions $\phi _ { 0 } , \phi _ { 1 } , . . . , \phi _ { n }$ can be chosen so that

$$
\int _ { a } ^ { b } w ( x ) \phi _ { k } ( x ) \phi _ { j } ( x ) d x = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { w h e n ~ } } j \neq k , } \\ { \alpha _ { j } > 0 , } & { { \mathrm { w h e n ~ } } j = k , } \end{array} \right. }
$$

then the normal equations reduce to

$$
\int _ { a } ^ { b } w ( x ) f ( x ) \phi _ { j } ( x ) d x = a _ { j } \int _ { a } ^ { b } w ( x ) [ \phi _ { j } ( x ) ] ^ { 2 } d x = a _ { j } \alpha _ { j } ,
$$

for each $j = 0 , 1 , \ldots , n$ ,and are easily solved to give

$$
a _ { j } = \frac { 1 } { \alpha _ { j } } \int _ { a } ^ { b } w ( x ) f ( x ) \phi _ { j } ( x ) d x .
$$

Hence the least squares approximation problem is greatly simplified when the functions $\phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n }$ are chosen to satisfy the orthogonality condition in Eq. (8.7). The remainder of this section is devoted to studying collections of this type.

# Definition 8.5

$\{ \phi _ { 0 } , \phi _ { 1 } , . . . , \phi _ { n } \}$ is said to be an orthogonal set of functions for the interval $[ a , b ]$ with respect to the weight function $w$ if

$$
\int _ { a } ^ { b } w ( x ) \phi _ { j } ( x ) \phi _ { k } ( x ) d x = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { w h e n ~ } } j \neq k , } \\ { \alpha _ { k } > 0 , } & { { \mathrm { w h e n ~ } } j = k . } \end{array} \right. }
$$

If, in addition, $\alpha _ { k } = 1$ for each $k = 0 , 1 , \ldots , n$ , the set is said to be orthonormal.

This definition, together with the remarks preceding it, produces the following theorem.

# Theorem 8.6

f $\{ \phi _ { 0 } , \ldots , \phi _ { n } \}$ is an orthogonal set of functions on an interval $[ a , b ]$ with respect to the weight function $w$ , then the least squares approximation to $f$ on $[ a , b ]$ with respect to ${ \pmb w }$ is

$$
P ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } \phi _ { k } ( x ) ,
$$

where, for each $k = 0 , 1 , \ldots , n$

$$
a _ { k } = { \frac { \int _ { a } ^ { b } w ( x ) \phi _ { k } ( x ) f ( x ) d x } { \int _ { a } ^ { b } w ( x ) [ \phi _ { k } ( x ) ] ^ { 2 } d x } } = { \frac { 1 } { \alpha _ { k } } } \int _ { a } ^ { b } w ( x ) \phi _ { k } ( x ) f ( x ) d x .
$$

Although Definition 8.5 and Theorem 8.6 allow for broad classes of orthogonal functions, only orthogonal sets of polynomials will be considered. The next theorem, which is based on the Gram-Schmidt process, describes how to construct orthogonal polynomials on $[ a , b ]$ with respect to a weight function $w$

# Theorem 8.7

The set of polynomial functions $\{ \phi _ { 0 } , \phi _ { 1 } , . . . , \phi _ { n } \}$ defined in the following way is orthogonal on $[ a , b ]$ with respect to the weight function $\pmb { w }$

$$
\phi _ { 0 } ( x ) \equiv 1 , \quad \phi _ { 1 } ( x ) = x - B _ { 1 } , \quad \mathrm { f o r e a c h } x \mathrm { i n } [ a , b ] ,
$$

where

$$
B _ { 1 } = \frac { \int _ { a } ^ { b } x w ( x ) [ \phi _ { 0 } ( x ) ] ^ { 2 } d x } { \int _ { a } ^ { b } w ( x ) [ \phi _ { 0 } ( x ) ] ^ { 2 } d x } ,
$$

and when $k \geq 2$ ，

$$
\phi _ { k } ( x ) = ( x - B _ { k } ) \phi _ { k - 1 } ( x ) - C _ { k } \phi _ { k - 2 } ( x ) , \quad \mathrm { f o r ~ e a c h ~ } x \mathrm { ~ i n ~ } [ a ,
$$

where

$$
B _ { k } = { \frac { \int _ { a } ^ { b } x w ( x ) [ \phi _ { k - 1 } ( x ) ] ^ { 2 } d x } { \int _ { a } ^ { b } w ( x ) [ \phi _ { k - 1 } ( x ) ] ^ { 2 } d x } }
$$

and

$$
C _ { k } = \frac { \int _ { a } ^ { b } x w ( x ) \phi _ { k - 1 } ( x ) \phi _ { k - 2 } ( x ) d x } { \int _ { a } ^ { b } w ( x ) [ \phi _ { k - 2 } ( x ) ] ^ { 2 } d x } .
$$

Theorem 8.7 provides a recursive procedure for constructing a set of orthogonal polynomials. The proof of this theorem follows by applying mathematical induction to the degree of the polynomial $\phi _ { n } ( x )$

For any $n > 0$ ,the set of polynomial functions $\{ \phi _ { 0 } , \ldots , \phi _ { n } \}$ given in Theorem 8.7 is linearly independent on $[ a , b ]$ and

$$
\int _ { a } ^ { b } w ( x ) \phi _ { n } ( x ) Q _ { k } ( x ) d x = 0 ,
$$

for any polynomial $Q _ { k } ( x )$ of degree $k < n$

Proof Since $\phi _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ ,Theorem 8.2 implies that $\{ \phi _ { 0 } , \ldots , \phi _ { n } \}$ is a linearly independent set.

Let $Q _ { k } ( x )$ be a polynomial of degree $k$ . By Theorem 8.3 there exist numbers Co,... , Ck such that

$$
Q _ { k } ( x ) = \sum _ { j = 0 } ^ { k } c _ { j } \phi _ { j } ( x ) .
$$

Thus,

$$
\int _ { a } ^ { b } w ( x ) Q _ { k } ( x ) \phi _ { n } ( x ) d x = \sum _ { j = 0 } ^ { k } c _ { j } \int _ { a } ^ { b } w ( x ) \phi _ { j } ( x ) \phi _ { n } ( x ) d x = \sum _ { j = 0 } ^ { k } c _ { j } \cdot 0 = 0 ,
$$

since $\phi _ { n }$ is orthogonal to $\phi _ { j }$ for each $j = 0 , 1 , \ldots , k$

The set of Legendre polynomials, $\{ P _ { n } ( x ) \}$ , is orthogonal on $[ - 1 , 1 ]$ with respect to the weight function $w ( x ) \equiv 1$ . The classical definition of the Legendre polynomials requires that $P _ { n } ( 1 ) = 1$ for each $\pmb { n }$ ,and a recursive relation is used to generate the polynomials when $n \geq 2$ . This normalization will notbe needed in our discussion, and the least squares approximating polynomials generated in either case are essentially the same.

Using the recursive procedure of Theorem 8.7 with $P _ { 0 } ( x ) \equiv 1$ gives

$$
B _ { 1 } = { \frac { \int _ { - 1 } ^ { 1 } x \ d x } { \int _ { - 1 } ^ { 1 } \ d x } } = 0 \quad { \mathrm { a n d } } \quad P _ { 1 } ( x ) = ( x - B _ { 1 } ) P _ { 0 } ( x ) = x .
$$

Also,

$$
B _ { 2 } = { \frac { \int _ { - 1 } ^ { 1 } x ^ { 3 } d x } { \int _ { - 1 } ^ { 1 } x ^ { 2 } d x } } = 0 \quad { \mathrm { a n d } } \quad C _ { 2 } = { \frac { \int _ { - 1 } ^ { 1 } x ^ { 2 } d x } { \int _ { - 1 } ^ { 1 } 1 d x } } = { \frac { 1 } { 3 } } ,
$$

So

$$
P _ { 2 } ( x ) = ( x - B _ { 2 } ) P _ { 1 } ( x ) - C _ { 2 } P _ { 0 } ( x ) = ( x - 0 ) x - \frac { 1 } { 3 } \cdot 1 = x ^ { 2 } - \frac { 1 } { 3 } .
$$

The higher-degree Legendre polynomials shown in Figure 8.9 are derived in the same maner. Although theintegration can be tedious,it is not difficult with aCAS.For example, the Maple command int used to compute the integrals $B _ { 3 }$ and $C _ { 3 }$ ：

$> \mathrm { B } 3 : = \mathrm { i n t } ( \mathbf { x } * ( \mathbf { x } \cdot 2 - 1 / 3 ) \cdot 2 , \mathbf { x } { = } - 1 , . 1 ) / \mathrm { i n t } ( ( \mathbf { x } ^ { - } 2 - 1 / 3 ) \cdot 2 , \mathbf { x } { = } - 1 , . 1 ) ;$ >C3: int $\left( \mathbf { x } * \left( \mathbf { x } \hat { } 2 \mathbf { - } 1 / 3 \right) * \mathbf { x } \right.$ ,x=-1..1)/int(x2,x=-1..1);

![](images/eef6900a34b7e784e32095d32dbaafcc7266494d37d56836baacb417f404f62a.jpg)  
Figure 8.9

gives $B _ { 3 } = 0$ and $\begin{array} { r } { C _ { 3 } = \frac { 4 } { 1 5 } } \end{array}$ . Thus,

$$
P _ { 3 } ( x ) = x P _ { 2 } ( x ) - { \frac { 4 } { 1 5 } } P _ { 1 } ( x ) = x ^ { 3 } - { \frac { 1 } { 3 } } x - { \frac { 4 } { 1 5 } } x = x ^ { 3 } - { \frac { 3 } { 5 } } x .
$$

$\begin{array} { r } { P _ { 4 } ( x ) = x ^ { 4 } - \frac { 6 } { 7 } x ^ { 2 } + \frac { 3 } { 3 5 } } \end{array}$ and $P _ { 5 } ( x ) = x ^ { 5 } - { \textstyle { \frac { 1 0 } { 9 } } } x ^ { 3 } +$ $\frac { 5 } { 2 1 } x$

The Legendre polynomials were mentioned in Section 4.7, where their roots were used as the nodes in Gaussian quadrature.

# EXERCISE SET 8.2

1.Find the linear least squares polynomial approximation to $f ( x )$ on the indicated interval if

$$
\begin{array} { l l l } { { f ( x ) = x ^ { 2 } + 3 x + 2 , } } & { { [ 0 , 1 ] ; } } & { { \mathrm { ~ b . ~ } \quad f ( x ) = x ^ { 3 } , \quad [ 0 , 2 ] ; } } \\ { { \displaystyle f ( x ) = \frac { 1 } { x } , \quad [ 1 , 3 ] ; } } & { { \mathrm { ~ d . ~ } \quad f ( x ) = e ^ { x } , \quad [ 0 , 2 ] ; } } \\ { { \displaystyle f ( x ) = \frac { 1 } { 2 } \cos x + \frac { 1 } { 3 } \sin 2 x , \quad [ 0 , 1 ] ; } } & { { \mathrm { ~ f . ~ } \quad f ( x ) = x \ln x , \quad [ 1 , 3 ] . } } \end{array}
$$

2. Find the least squares polynomial approximation of degree two to the functions and intervals in Exercise 1.

3.Find the linear least squares polynomial approximation on the interval $\left[ - 1 , 1 \right]$ for the following functions.

$$
{ \begin{array} { l l l } { f ( x ) = x ^ { 2 } - 2 x + 3 } & { } & { \qquad \mathbf { b } . \quad f ( x ) = x ^ { 3 } } \\ { f ( x ) = { \cfrac { 1 } { x + 2 } } } & { } & { \qquad \mathbf { d } . \quad f ( x ) = e ^ { x } } \\ { f ( x ) = { \cfrac { 1 } { 2 } } \cos x + { \cfrac { 1 } { 3 } } \sin 2 x } & { } & { \qquad \mathbf { f } . \quad f ( x ) = \ln ( x + 2 ) } \end{array} }
$$

4. Find the least squares polynomial approximation of degree 2 on the interval $[ - 1 , 1 ]$ for the functions in Exercise 3.

5.Compute the error $E$ for the approximations in Exercise 3.

6.Compute the error $E$ for the approximations in Exercise 4.

7.Use the Gram-Schmidt process to construct $\phi _ { 0 } ( x ) , \phi _ { 1 } ( x ) , \phi _ { 2 } ( x )$ ,and $\phi _ { 3 } ( x )$ for the following intervals.

a.[0,1] b.[0,2] c.[1,3]

8.Repeat Exercise 1 using the results of Exercise 7.

9.Repeat Exercise 2 using the results of Exercise 7.

10. Obtain the least squares approximation polynomial of degree 3 for the functions in Exercise l using the results of Exercise 7.

11. Use the Gram-Schmidt procedure to calculate $L _ { 1 } , L _ { 2 }$ ,and $L _ { 3 }$ ，where $\{ L _ { 0 } ( x ) , L _ { 1 } ( x ) , L _ { 2 } ( x )$ ， $L _ { 3 } ( x ) \}$ is an orthogonal set of polynomials on $( 0 , \infty )$ with respect to the weight functions $w ( x ) = e ^ { - x }$ and $L _ { 0 } ( x ) \equiv 1$ . The polynomials obtained from this procedure are called the Laguerre polynomials.

12. Use the Laguerre polynomials calculated in Exercise 11 to compute the least squares polynomials of degree one, two, and three on the interval $( 0 , \infty )$ with respect to the weight function $w ( x ) = e ^ { - x }$ for the following functions:

$$
f ( x ) = x ^ { 2 } \qquad { \bf b } . \quad f ( x ) = e ^ { - x } \qquad { \bf c } . \quad f ( x ) = x ^ { 3 } \qquad { \bf d } . \quad f ( x ) = e ^ { - 2 x } \qquad 
$$

13.Suppose $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } \}$ is any linearly independent set in $\prod _ { n }$ . Show that for any elemen！ $Q \in \prod _ { n }$ , there exist unique constants $c _ { 0 } , c _ { 1 } , \ldots , c _ { n }$ ,such that

$$
Q ( x ) = \sum _ { k = 0 } ^ { n } c _ { k } \phi _ { k } ( x ) .
$$

14.Show that if $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } \}$ is an orthogonal set of functions on $[ a , b ]$ with respect to the weight function $\pmb { w }$ ,then $\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } \}$ is a linearly independent set.

15. Show that the normal equations (8.6) have aunique solution.[Hint: Show that the only solution for the function $f ( x ) \equiv 0$ is $a _ { j } = 0$ ， $j = 0$ ,1,...,n. Multiply Eq. (8.6) by $a _ { j }$ ,and sum over all $j$ . Interchange the integral sign and the summation sign to obtain $\begin{array} { r } { \int _ { a } ^ { b } [ P ( x ) ] ^ { 2 } d x = 0 } \end{array}$ . Thus, $P ( { \pmb x } ) \equiv 0$ ， $\mathbf { s o } a _ { j } = \mathbf { 0 }$ ,for $j = 0 , \ldots , n$ .Hence,the coefficient matrix is nonsingular,and there is a unique solution to Eq. (8.6).]

# 8.3 Chebyshev Polynomials and Economization of Power Series

The Chebyshev polynomials $\{ T _ { n } ( x ) \}$ are orthogonal on $( - 1 , 1 )$ with respect to the weight function $w ( x ) = ( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ . Although they can be derived by the method in the previous section, it is easier to give their definition and then show that they satisfy the required orthogonality properties.

For $x \in [ - 1 , 1 ]$ , define

$$
T _ { n } ( x ) = \cos [ n \operatorname { a r c c o s } x ] , \quad { \mathrm { f o r ~ e a c h } } n \geq 0 .
$$

It is not obvious from this definition that for each $\pmb { n }$ ， $T _ { n } ( x )$ is a polynomial in $x$ , but we will now show that it is. First note that

$$
T _ { 0 } ( x ) = \cos 0 = 1 \quad { \mathrm { a n d } } \quad T _ { 1 } ( x ) = \cos ( \operatorname { a r c c o s } x ) = x .
$$

For $n \geq 1$ ,we introduce the substitution $\theta = \operatorname { a r c c o s } x$ to change this equation to

$$
T _ { n } ( \theta ( x ) ) \equiv T _ { n } ( \theta ) = \cos ( n \theta ) , \quad \mathrm { w h e r e } ~ \theta \in [ 0 , \pi ] .
$$

A recurrence relation is derived by noting that

$$
T _ { n + 1 } ( \theta ) = \cos ( n \theta ) \cos \theta - \sin ( n \theta ) \sin \theta
$$

and

$$
T _ { n - 1 } ( \theta ) = \cos ( n \theta ) \cos \theta + \sin ( n \theta ) \sin \theta .
$$

Adding these equations gives

$$
T _ { n + 1 } ( \theta ) = 2 \cos ( n \theta ) \cos \theta - T _ { n - 1 } ( \theta ) .
$$

Returning to the variable $\pmb { x }$ , we have, for $n \geq 1$ ，

$$
T _ { n + 1 } ( x ) = 2 x \cos ( n \operatorname { a r c c o s } x ) - T _ { n - 1 } ( x )
$$

or

$$
T _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) .
$$

Since $T _ { 0 } ( x ) = 1$ and $T _ { 1 } ( x ) = x$ , the recurrence relation implies that $T _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ with leading coefficient $2 ^ { n - 1 }$ , when $n \geq 1$

The next three Chebyshev polynomials are

$$
\begin{array} { l l l } { { T _ { 2 } ( x ) = 2 x T _ { 1 } ( x ) - T _ { 0 } ( x ) = 2 x ^ { 2 } - 1 , } } \\ { { \nonumber } } \\ { { T _ { 3 } ( x ) = 2 x T _ { 2 } ( x ) - T _ { 1 } ( x ) = 4 x ^ { 3 } - 3 x , } } \end{array}
$$

and

$$
T _ { 4 } ( x ) = 2 x T _ { 3 } ( x ) - T _ { 2 } ( x ) = 8 x ^ { 4 } - 8 x ^ { 2 } + 1 .
$$

The graphs of $T _ { 1 } , T _ { 2 } , T _ { 3 }$ ,and $T _ { 4 }$ are shown in Figure 8.10.

To show the orthogonality of the Chebyshev polynomials,consider

$$
\int _ { - 1 } ^ { 1 } { \frac { T _ { n } ( x ) T _ { m } ( x ) } { \sqrt { 1 - x ^ { 2 } } } } d x = \int _ { - 1 } ^ { 1 } { \frac { \cos ( n \operatorname { a r c c o s } x ) \cos ( m \operatorname { a r c c o s } x ) } { \sqrt { 1 - x ^ { 2 } } } } d x .
$$

![](images/a51681cc585e5e77704fd2ecb6ec0bc1e00b263ce4c08098d932733d2c883d6f.jpg)  
Figure 8.10

Reintroducing the substitution $\theta = \operatorname { a r c c o s } x$ gives

$$
d \theta = - { \frac { 1 } { \sqrt { 1 - x ^ { 2 } } } } d x
$$

and

$$
\int _ { - 1 } ^ { 1 } { \frac { T _ { n } ( x ) T _ { m } ( x ) } { \sqrt { 1 - x ^ { 2 } } } } d x = - \int _ { \pi } ^ { 0 } \cos ( n \theta ) \cos ( m \theta ) d \theta = \int _ { 0 } ^ { \pi } \cos ( n \theta ) \cos ( m \theta ) d \theta .
$$

Suppose $n \neq m$ . Since

$$
\cos ( n \theta ) \cos ( m \theta ) = { \frac { 1 } { 2 } } [ \cos ( n + m ) \theta + \cos ( n - m ) \theta ] ,
$$

we have

$$
\begin{array} { l } { \displaystyle \int _ { - 1 } ^ { 1 } \frac { T _ { n } ( x ) T _ { m } ( x ) } { \sqrt { 1 - x ^ { 2 } } } d x = \frac { 1 } { 2 } \int _ { 0 } ^ { \pi } \cos ( ( n + m ) \theta ) d \theta + \frac { 1 } { 2 } \int _ { 0 } ^ { \pi } \cos ( ( n - m ) \theta ) d \theta } \\ { \displaystyle = \left[ \frac { 1 } { 2 ( n + m ) } \sin ( ( n + m ) \theta ) + \frac { 1 } { 2 ( n - m ) } \sin ( ( n - m ) \theta ) \right] _ { 0 } ^ { \pi } } \\ { \displaystyle = 0 . } \end{array}
$$

By a similar technique, it can be shown that when $n = m$ ，

$$
\int _ { - 1 } ^ { 1 } { \frac { [ T _ { n } ( x ) ] ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } d x = { \frac { \pi } { 2 } } , \quad \operatorname { f o r } \operatorname { e a c h } n \geq 1 .
$$

The Chebyshev polynomials are used to minimize approximation error. We will see how they are used to solve two problems of this type:

1.an optimal placing of interpolating points to minimize the error in Lagrange interpolation;   
2. a means of reducing the degree of an approximating polynomial with minimal loss of accuracy.

The next result concerns the zeros and extreme points of $T _ { n }$ vrem 8.9 The Chebyshev polynomial $T _ { n } ( x )$ of degree $n \geq 1$ has $\pmb { n }$ simple zeros in [-1,1] at

$$
{ \bar { x } } _ { k } = \cos { \left( { \frac { 2 k - 1 } { 2 n } } \pi \right) } , \quad { \mathrm { f o r ~ e a c h ~ } } k = 1 , 2 , \ldots , n .
$$

Moreover, $T _ { n } ( x )$ assumes its absolute extrema at

$$
{ \bar { x } } _ { k } ^ { \prime } = \cos \left( { \frac { k \pi } { n } } \right) \quad { \mathrm { w i t h } } \quad T _ { n } ( { \bar { x } } _ { k } ^ { \prime } ) = ( - 1 ) ^ { k } , \quad { \mathrm { f o r ~ e a c h } } \quad k = 0 , 1 , \ldots , n .
$$

Proof If we let

$$
\bar { x } _ { k } = \cos \bigg ( \frac { 2 k - 1 } { 2 n } \pi \bigg ) , \quad \mathrm { f o r } \ k = 1 , \dot { 2 } , \ldots , n ,
$$

then

$$
{ \mathrm { \Omega } } _ { n } ^ { \prime } ( { \bar { x } } _ { k } ) = \cos ( n \operatorname { a r c c o s } { \bar { x } } _ { k } ) = \cos \left( n \operatorname { a r c c o s } \left( \cos \left( { \frac { 2 k - 1 } { 2 n } } \pi \right) \right) \right) = \cos \left( { \frac { 2 k - 1 } { 2 } } \pi \right) = \cos ( n \pi )
$$

and each $\bar { x } _ { k }$ is a distinct zero of $T _ { n }$ . Since $T _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ , all zeros of $T _ { n } ( x )$ must be of this form.

To show the second part, first note that

$$
T _ { n } ^ { \prime } ( x ) = { \frac { d } { d x } } [ \cos ( n \operatorname { a r c c o s } x ) ] = { \frac { n \sin ( n \operatorname { a r c c o s } x ) } { \sqrt { 1 - x ^ { 2 } } } } ,
$$

and that, when $k = 1 , 2 , \ldots , n - 1$ ，

$$
T _ { n } ^ { \prime } ( \bar { x } _ { k } ^ { \prime } ) = \frac { n \sin \left( n \operatorname { a r c c o s } \left( \cos \left( \frac { k \pi } { n } \right) \right) \right) } { \sqrt { 1 - \left[ \cos \left( \frac { k \pi } { n } \right) \right] ^ { 2 } } } = \frac { n \sin ( k \pi ) } { \sin \left( \frac { k \pi } { n } \right) } = 0 .
$$

Since $T _ { n } ( x )$ is a polynomial of degree $\pmb { n }$ , its derivative $T _ { n } ^ { \prime } ( x )$ is a polynomial of degree $( n - 1 )$ , and all the zeros of $T _ { n } ^ { \prime } ( x )$ occur at these $n  1$ points. The only other possibilities for extrema of $T _ { n } ( x )$ occur at the endpoints of the interval [-1,1]; that is, at $\bar { x } _ { 0 } ^ { \prime } = 1$ and at $\hat { x } _ { n } ^ { \prime } = - 1$ . Since for any $k = 0 , 1 , \ldots , n$ ,we have

$$
T _ { n } ( \bar { x } _ { k } ^ { \prime } ) = \cos \left( n \operatorname { a r c c o s } \left( \cos \left( \frac { k \pi } { n } \right) \right) \right) = \cos ( k \pi ) = ( - 1 ) ^ { k } ,
$$

a maximum occurs at each even value of $k$ and a minimum at each odd value.

The monic (polynomials with leading coefficient 1) Chebyshev polynomials $\tilde { T } _ { n } ( x )$ are derived from theChebyshev polynomial Tn(x)by dividing by the leading coefcient 2n-1. Hence,

$$
\tilde { T } _ { 0 } ( x ) = 1 \quad \mathrm { a n d } \quad \tilde { T } _ { n } ( x ) = \frac { 1 } { 2 ^ { n - 1 } } T _ { n } ( x ) , \quad \mathrm { f o r e a c h } n \geq 1 .
$$

The recurrence relationship satisfied by the Chebyshev polynomials implies that

$$
\begin{array} { l } { { \displaystyle \tilde { T } _ { 2 } ( x ) = x \tilde { T } _ { 1 } ( x ) - \frac { 1 } { 2 } \tilde { T } _ { 0 } ( x ) \quad \mathrm { a n d } } } \\ { { \displaystyle \tilde { T } _ { n + 1 } ( x ) = x \tilde { T } _ { n } ( x ) - \frac { 1 } { 4 } \tilde { T } _ { n - 1 } ( x ) , \quad \mathrm { f o r e a c h } n \ge 2 . } } \end{array}
$$

The graphs of $\tilde { T _ { 1 } } , \tilde { T _ { 2 } } , \tilde { T _ { 3 } } , \tilde { T _ { 4 } }$ ,and $\tilde { \tau } _ { 5 }$ are shown in Figure 8.11.

Because $\tilde { T } _ { n } ( x )$ is just a multiple of $T _ { n } ( x )$ , Theorem 8.9 implies that the zeros of $\tilde { T } _ { n } ( x )$ also occur at

$$
\bar { x } _ { k } = \cos \bigg ( \frac { 2 k - 1 } { 2 n } \pi \bigg ) , \quad \mathrm { f o r } \operatorname { e a c h } k = 1 , 2 , \ldots , n ,
$$

![](images/39cba110d14328d2cb5d905942a3dcc00192a4b5f5a6f4c4dc0cb37e7fb20341.jpg)  
Figure 8.11

and the extreme values of $\tilde { T } _ { n } ( x )$ ,for $n \geq 1$ ,occur at

$$
\bar { x } _ { k } ^ { \prime } = \cos \bigg ( \frac { k \pi } { n } \bigg ) , \quad \mathrm { w i t h } \quad \tilde { T } _ { n } ( \bar { x } _ { k } ^ { \prime } ) = \frac { ( - 1 ) ^ { k } } { 2 ^ { n - 1 } } , \quad \mathrm { f o r } \mathrm { e a c h } k = 0 , 1 , 2 , \dots , n .
$$

Let $\smash { \widetilde { \Pi } } _ { n }$ denote the set of allmonic polynomials of degree n. The relation expressed in Eq. (8.13) leads to an important minimization property that distinguishes $\tilde { T } _ { n } ( x )$ from the other members of $\widetilde { \Pi } _ { n }$ ·

Theorem 8.10

The polynomials of the form $\tilde { T } _ { n } ( x )$ ,when $n \geq 1$ , have the property that

$$
\frac { 1 } { 2 ^ { n - 1 } } = \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | \widetilde { T } _ { n } ( x ) | \leq \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | P _ { n } ( x ) | , \quad \mathrm { f o r ~ a l l } \ P _ { n } ( x ) \in \widetilde { \prod } _ { n } .
$$

Moreover, equality can occur only if $\boldsymbol { P _ { n } } \equiv \boldsymbol { \tilde { T _ { n } } }$

Proof Suppose $P _ { n } ( x ) \in { \widetilde { \prod } } _ { n }$ and

$$
\operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | P _ { n } ( x ) | \leq \frac { 1 } { 2 ^ { n - 1 } } = \operatorname* { m a x } _ { x \in [ - 1 , 1 ] } | \tilde { T } _ { n } ( x ) | .
$$

Let $Q = \tilde { T } _ { n } - P _ { n }$ . Since $\tilde { T } _ { n } ( x )$ and $P _ { n } ( x )$ are both monic polynomials of degree $n$ ， $Q ( x )$ is a polynomial of degree at most $( n - 1 )$ . Moreover, at the extreme points of $\tilde { T } _ { n } ( x )$ ，

$$
\mathcal { Q } ( \bar { x } _ { k } ^ { \prime } ) = \tilde { T } _ { n } ( \bar { x } _ { k } ^ { \prime } ) - P _ { n } ( \bar { x } _ { k } ^ { \prime } ) = \frac { ( - 1 ) ^ { k } } { 2 ^ { n - 1 } } - P _ { n } ( \bar { x } _ { k } ^ { \prime } ) .
$$