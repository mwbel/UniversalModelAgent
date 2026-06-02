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
