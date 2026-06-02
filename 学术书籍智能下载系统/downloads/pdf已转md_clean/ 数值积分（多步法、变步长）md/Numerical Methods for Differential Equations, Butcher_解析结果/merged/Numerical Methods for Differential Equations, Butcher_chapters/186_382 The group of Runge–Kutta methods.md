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
