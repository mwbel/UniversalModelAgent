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
