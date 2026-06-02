# 356 AN-stability

Linear stability analysis is based on the linear test problem

$$
y ^ { \prime } ( x ) = q y ( x ) ,
$$

so that

$$
y _ { n } = R ( z ) y _ { n - 1 } ,
$$

where $z = h q$ . Even though this analysis provides useful information about the behaviour of a numerical method when applied to a stiff problem, even more is learned from generalizing this analysis in two possible ways. The first

of these generalizations allows the linear factor $q$ to be time-dependent so that the test problem becomes

$$
y ^ { \prime } ( x ) = q ( x ) y ( x ) .
$$

A second generalization, which we explore in Subsection 357, allows the differential equation to be non-linear.

When (356a) is numerically solved using an implicit Runge–Kutta method $( A , b ^ { \prime } , c )$ , the stage values satisfy the equations

$$
Y _ { i } = y _ { n - 1 } + \sum _ { j = 1 } ^ { s } a _ { i j } h q ( x _ { n - 1 } + h c _ { j } ) Y _ { j } , \qquad i = 1 , 2 , \dots , s ,
$$

and the output result is

$$
y _ { n } = y _ { n - 1 } + \sum _ { i = 1 } ^ { s } b _ { i } h q ( x _ { n - 1 } + h c _ { i } ) Y _ { i } .
$$

Let $Z$ denote the diagonal matrix given by

$$
{ \cal Z } = \left[ \begin{array} { c c c c c } { { h q ( x _ { n - 1 } + h c _ { 1 } ) } } & { { 0 } } & { { \cdots } } & { { 0 } } \\ { { 0 } } & { { h q ( x _ { n - 1 } + h c _ { 2 } ) } } & { { \cdots } } & { { 0 } } \\ { { \vdots } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdots } } & { { h q ( x _ { n - 1 } + h c _ { s } ) } } \end{array} \right] ~ ,
$$

This makes it possible to write the vector of stage values in the form

$$
Y = y _ { n - 1 } { \bf 1 } + A Z Y ,
$$

so that

$$
Y = ( I - A Z ) ^ { - 1 } \mathbf { 1 } y _ { n - 1 } .
$$

The output value is given by

$$
y _ { n } = y _ { n - 1 } + b ^ { \mathsf { T } } Z Y = \left( 1 + b ^ { \mathsf { T } } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } \right) y _ { n - 1 } = R ( Z ) y _ { n - 1 } .
$$

The function $R ( Z )$ introduced here is the non-autonomous generalization of the linear stability function.

We are mainly concerned with situations in which the stage abscissae are distinct and where they do not interfere with the stages of adjoining steps. This means that we can regard the diagonal elements of $Z$ as different from each other and independent of the values in the steps that come before or after the current step. With this in mind, we define a non-autonomous counterpart of A-stability that will guarantee that we obtain stable behaviour as long as the real part of $q ( x )$ is never positive. This is appropriate because the exact solution to (356a) is never increasing under this assumption, and we want to guarantee that this property carries over to the computed solution.

Definition 356A A Runge–Kutta method $( A , b ^ { \prime } , c )$ is ‘AN-stable’ if the function

$$
R ( Z ) = 1 + b ^ { \intercal } Z ( I - A Z ) ^ { - 1 } \mathbf { 1 } ,
$$

where $Z = \operatorname { d i a g } \left( \left[ z _ { 1 } \quad z _ { 2 } \quad \cdots \quad z _ { s } \right] \right)$ is bounded in magnitude by 1 whenever $z _ { 1 }$ , $z _ { 2 }$ , . . . , $z _ { s }$ are in the left half-plane.

It is interesting that a simple necessary and sufficient condition exists for AN-stability. In Theorem 356C we state this criterion and prove it only in terms of necessity. Matters become complicated if the method can be reduced to a method with fewer stages that gives exactly the same computed result. This can happen, for example, if there exists $j ~ \in ~ \{ 1 , 2 , \ldots , s \}$ such that $b _ { j } = 0$ , and furthermore, $a _ { i j } = 0$ for all $i = 1 , 2 , \dots , s$ , except perhaps for $i = j$ . Deleting stage $j$ has no effect on the numerical result computed in a step. We make a detailed study of reducibility in Subsection 381, but in the meantime we identify ‘irreducibility in the sense of Dahlquist and Jeltsch’, or ‘DJ-irreducibility’, (Dahlquist and Jeltsch, 1979) as the property that a tableau cannot be reduced in the sense of Definition 356B.

Definition 356B A Runge–Kutta method is ‘DJ-reducible’ if there exists a partition of the stages

$$
\{ 1 , 2 , \ldots , s \} = S \cup S _ { 0 } ,
$$

with $S _ { 0 }$ non-empty, such that if $i \in S$ and $j \in S _ { 0 }$ ,

$$
b _ { j } = 0 \ a n d \ a _ { i j } = 0 .
$$

The ‘reduced method’ is the method formed by deleting all stages numbered by members of the set $S _ { 0 }$ .

The necessary condition to be given in Theorem 356C will be strengthened under DJ-irreducibility in Corollary 356D.

Theorem 356C Let $( A , b ^ { \prime } , c )$ be an implicit Runge–Kutta method. Then the method is AN-stable only if

$$
b _ { j } \geq 0 , \qquad j = 1 , 2 , \ldots , s ,
$$

and the matrix

$$
M = \mathrm { d i a g } ( b ) A + A ^ { \top } \mathrm { d i a g } ( b ) - b b ^ { \top }
$$

is positive semi-definite.

Proof. If $b _ { j } < 0$ then choose $Z = - t \mathrm { d i a g } ( e _ { j } )$ , for $t$ positive. The value of $R ( Z )$ becomes

$$
R ( Z ) = 1 - t b _ { j } + O ( t ^ { 2 } ) ,
$$

which is greater than $^ { 1 }$ for $t$ sufficiently small. Now consider $Z$ chosen with purely imaginary components

$$
Z = i \mathrm { d i a g } ( v t ) ,
$$

where $v$ has real components and $t$ is a small positive real. We have

$$
\begin{array} { c } { { R ( Z ) = 1 + i t b ^ { \top } \mathrm { d i a g } ( v ) { \bf 1 } - t ^ { 2 } b ^ { \top } \mathrm { d i a g } ( v ) A \mathrm { d i a g } ( v ) { \bf 1 } + O ( t ^ { 3 } ) } } \\ { { { } } } \\ { { = 1 + i t b ^ { \top } v - t ^ { 2 } v ^ { \top } \mathrm { d i a g } ( b ) A v + O ( t ^ { 3 } ) , } } \end{array}
$$

so that

$$
| R ( Z ) | ^ { 2 } = 1 - t ^ { 2 } v ^ { \top } M v + O ( t ^ { 3 } ) .
$$

Since this cannot exceed $^ { 1 }$ for $t$ small and any choice of $v$ , $M$ is positive semi-definite. 

Since there is no practical interest in reducible methods, we might look at the consequences of assuming a method is irreducible. This result was published in Dahlquist and Jeltsch (1979):

Corollary 356D Under the same conditions of Theorem 356C, with the additional assumption that the method is DJ-irreducible,

$$
b _ { j } > 0 , \qquad j = 1 , 2 , \ldots , s .
$$

Proof. Suppose that for $i \leq \overline { { s } }$ , $b _ { i } > 0$ , but that for $i > { \overline { { s } } }$ , $b _ { i } = 0$ . In this case, $M$ can be written in partitioned form as

$$
\begin{array} { r } { M = \left[ \begin{array} { c c } { \overline { { M } } } & { N } \\ { N ^ { \top } } & { 0 } \end{array} \right] } \end{array}
$$

and this cannot be positive semi-definite unless $N = 0$ . This implies that

$$
a _ { i j } = 0 , \quad { \mathrm { w h e n e v e r ~ } } i \leq { \overline { { s } } } < j ,
$$

implying that the method is reducible to a method with only $\overline { { s } }$ stages.
