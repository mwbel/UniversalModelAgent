# 542 Runge–Kutta stability

For methods of types 1 and 2, a reasonable design criterion is that its stability region should be similar to that of a Runge–Kutta method. The reasons for this are that Runge–Kutta methods not only have convenient stability properties from the point of view of analysis but also that they have stability properties that are usually superior to those of alternative methods. For example, A-stability is inconsistent with high order for linear multistep methods but is available for Runge–Kutta methods of any order.

The stability matrix for a general linear method has the form

$$
M ( z ) = V + z B ( I - z A ) ^ { - 1 } U
$$

and the characteristic polynomial is

$$
\Phi ( w , z ) = \operatorname* { d e t } ( w I - M ( z ) ) .
$$

In general this is a complicated function, in which the coefficients of powers of $w$ are rational functions of $z$ . To obtain stability properties as close to those of a Runge–Kutta method as possible we will seek methods for which $\Phi ( w , z )$ factorizes as in the following definition.

Definition 542A A general linear method $( A , U , B , V )$ has ‘Runge–Kutta stability’ if the characteristic polynomial given by (542a) has the form

$$
\begin{array} { r } { \Phi ( w , z ) = w ^ { r - 1 } ( w - R ( z ) ) . } \end{array}
$$

For a method with Runge–Kutta stability, the rational function $R ( z )$ is known as the ‘stability function’ of the method.

We will usually abbreviate ‘Runge–Kutta stability’ by ‘RK stability’. We present two examples of methods satisfying this condition with $p = q = r =$ $s = 2$ and with $c = [ 0 \quad 1 ] ^ { \intercal } .$ . The first is of type 1 and is assumed to have the form

$$
[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { a _ { 2 1 } } { b _ { 1 1 } } \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} ] \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \\ { 1 - V _ { 1 2 } } & { V _ { 1 2 } } \\ { b _ { 1 1 } } & { b _ { 1 2 } } \end{array} ] .
$$

The assumption that $U = I$ is not a serious restriction because, if $U$ is nonsingular, an equivalent method can be constructed with $U = I$ and $B$ and $V$ replaced by $U B$ and $U V U ^ { - 1 }$ , respectively. The form chosen for $V$ makes it of rank $^ { 1 }$ and preconsistent for the vector $c = [ 1 \quad 1 ] ^ { \prime }$ .

By the stage order conditions, it is found that

$$
\phi ( z ) = ( I - z A ) \exp ( c z ) = \left[ \begin{array} { c } { { 1 } } \\ { { 1 + ( 1 - a _ { 2 1 } ) z + \frac { 1 } { 2 } z ^ { 2 } } } \end{array} \right] .
$$

To find $B$ , we have

$$
B z \exp ( c z ) = ( \exp ( z ) I - V ) \phi ( z ) + O ( z ^ { 3 } ) .
$$

Write the coefficients of $z$ and $z ^ { 2 }$ in separate columns and we deduce that

$$
\begin{array} { r } { B \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { 1 - V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { \frac { 1 } { 2 } ( 1 - V _ { 1 2 } ) } \\ { 2 - V _ { 1 2 } - a _ { 2 1 } + a _ { 2 1 } V _ { 1 2 } } & { 2 - a _ { 2 1 } - \frac { 1 } { 2 } V _ { 1 2 } } \end{array} \right] , } \end{array}
$$

so that

$$
B = \left[ \begin{array} { c c } { \frac { 1 } { 2 } - \frac { 1 } { 2 } V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { \frac { 1 } { 2 } ( 1 - V _ { 1 2 } ) } \\ { - \frac { 1 } { 2 } V _ { 1 2 } + a _ { 2 1 } V _ { 1 2 } } & { 2 - a _ { 2 1 } - \frac { 1 } { 2 } V _ { 1 2 } } \end{array} \right] .
$$

To achieve RK stability, impose the requirement that the stability function $V + z B ( I - z A ) ^ { - 1 }$ has zero determinant and it is found that $a _ { 2 1 } = 2$ and $\begin{array} { r } { V _ { 1 2 } = \frac { 1 } { 2 } } \end{array}$ .

This gives the method

$$
[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { 2 } { \frac { 5 } { 4 } } \quad \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 1 } \\ { \frac { 1 } { 2 } } & { \frac { 1 } { 4 } } \\ { \frac { 3 } { 4 } } & { - \frac { 1 } { 4 } } \end{array} ] \frac { 1 } { 2 } \quad \frac { 1 } { 2 } ] .
$$

To derive a type 2 method with RK stability, carry out a similar calculation but with

$$
A = \left[ \begin{array} { c c } { { \lambda } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { \lambda } } \end{array} \right] .
$$

In this case, the method is

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \frac { \frac { \lambda } { 1 + 2 \lambda } } { \frac { 5 - 2 \lambda + 1 2 \lambda ^ { 2 } + 8 \lambda ^ { 3 } } { 4 + 8 \lambda } } \frac { \lambda } { \frac { 1 } { 4 } - \lambda ^ { 2 } } \frac { 0 } { \frac { 1 } { 2 } + \lambda } \frac { 1 } { \frac { 1 } { 2 } - \lambda } \right] ,
$$

or, with $\begin{array} { r } { \lambda = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ , for L-stability,

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c c c c c } { 1 - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 1 } & { 0 } \\ { \frac { 6 + 2 \sqrt { 2 } } { 7 } } & { 1 - \frac { \sqrt { 2 } } { 2 } } & { 0 } & { 1 } \\ { \frac { 7 3 - 3 4 \sqrt { 2 } } { 2 8 } } & { \frac { 4 \sqrt { 2 } - 5 } { 4 } } & { \frac { 3 - \sqrt { 2 } } { 2 } } & { \frac { \sqrt { 2 } - 1 } { 2 } } \\ { \frac { 8 7 - 4 8 \sqrt { 2 } } { 2 8 } } & { \frac { 3 4 \sqrt { 2 } - 4 5 } { 2 8 } } & { \frac { 3 - \sqrt { 2 } } { 2 } } & { \frac { \sqrt { 2 } - 1 } { 2 } } \end{array} \right] .
$$

Type 3 and type 4 methods do not exist with RK stability, and will not be explored in detail in this section. We do, however, give a single example of each. For the type 3 method we have

$$
[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} ] = [ \frac { 0 } { - \frac { 3 } { 8 } } \begin{array} { c c c c } { 0 } & { 0 } & { | } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { - \frac { 3 } { 8 } } & { - \frac { 3 } { 8 } } & { - \frac { 3 } { 4 } } & { \frac { 7 } { 4 } } \\ { - \frac { 7 } { 8 } } & { \frac { 9 } { 8 } } & { - \frac { 3 } { 4 } } & { \frac { 7 } { 4 } } \end{array} ] .
$$

This method is designed for parallel computation in the sense that the two stages do not depend on each other, because $A = 0$ , and hence they can be evaluated in parallel. Is there any advantage in the use of methods like this? Of course, the answer will depend on the specific coefficients in the method but, in the case of (542d), we might wish to compare it with the type 1 method given by (542b) whose error constant has magnitude $\frac { 1 } { 6 }$ . In contrast, (542d) has error constant $\textstyle { \frac { 1 9 } { 2 4 } }$ which is equivalent to $\textstyle { \frac { 1 9 } { 9 6 } }$ 6 when adjusted for the sequential cost of one $f$ evaluation per step. Thus, in this case, the type 3 method is less efficient even under the assumption of perfect speed-up.

The type 4 method

$$
\begin{array}{c} { \left[ \begin{array} { l l } { A } & { U } \\ { B } & { V } \end{array} \right] } = { \left[ \begin{array} { l l l l } { { \frac { 3 - { \sqrt { 3 } } } { 2 } } } & { 0 } & { 1 } & { 0 } \\ { { \frac { 0 } { 2 } } } & { { \frac { 3 - { \sqrt { 3 } } } { 2 } } } & { 0 } & { 1 } \\ { { \frac { 1 8 - 1 1 { \sqrt { 3 } } } { 4 } } } & { { \frac { 7 { \sqrt { 3 } } - 1 2 } { 4 } } } \\ { { \frac { 2 2 - 1 3 { \sqrt { 3 } } } { 4 } } } & { { \frac { 9 { \sqrt { 3 } } - 1 2 } { 4 } } } \end{array} \right] } { \frac { 3 - 2 { \sqrt { 3 } } } { 2 } }  & { { \frac { 2 { \sqrt { 3 } } - 1 } { 2 } } } \end{array} 
$$

is found to be A-stable with the additional property that its stability matrix has zero spectral radius at infinity. Just as for the type 3 method we have introduced, while the advantages of this type of method are not clear, results found by Singh (1999) are encouraging.

For type 1 and 2 methods, increasing order presents great challenges in the solution of the order conditions combined with RK stability requirements. For an account of the techniques used to find particular methods of orders up to 8, see Butcher and Jackiewicz (1996, 1998).
