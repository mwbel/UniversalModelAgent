# 385 A generalization of $G _ { 1 }$

It will be convenient to build an algebraic system similar to $G _ { 1 }$ , but possessing, in addition to the group structure, a vector space structure. We cannot exactly achieve all of this, but we can achieve almost all of it. The way we go about this is to add to $T$ an additional member, known as the ‘empty tree’ and denoted by $\emptyset$ . The augmented set of trees will be denoted by $T ^ { \# }$ . We write $G$ for the set of mappings $T ^ { \# }  \mathbb { R }$ and $G _ { 1 }$ for the set of those members of $G$ for which $\varnothing$ maps to 1. We define the operation $G _ { 1 } \times G \to G$ just as for the group operation except that the coefficient of $\alpha ( t )$ in the formula for $( \alpha \beta ) ( t )$ is $\beta ( \emptyset )$ . With this understanding we retain the associativity property, in cases where it makes sense. That is, if $\alpha , \beta \in G _ { 1 }$ and $\gamma \in G$ , then

$$
( \alpha \beta ) \gamma = \alpha ( \beta \gamma ) .
$$

Furthermore, left-multiplication by an element of $G _ { 1 }$ is linear in the sense that

$$
\alpha ( \beta + \gamma ) = \alpha \beta + \alpha \gamma ,
$$

whenever $\alpha \in G _ { 1 }$ and $\beta , \gamma \in G$ . Furthermore,

$$
\alpha ( c \beta ) = c \alpha \beta ,
$$

where, for a scalar $c$ , $c \beta$ is the mapping that takes $t$ to $c \beta ( t )$ for all $t \in T ^ { \# }$ .

The generalization we have introduced has a simple significance in terms of Runge–Kutta tableaux and methods. Instead of computing the output value from a step of computation by the formula

$$
y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } F _ { i } ,
$$

where $y _ { 0 }$ is the input value and $F _ { 1 }$ , $F _ { 2 }$ , . . . , $F _ { s }$ are stage derivatives, we can replace (385a) by

$$
b _ { 0 } y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } { \cal F } _ { i } .
$$

To express this in a tableau, we place the coefficient $b _ { 0 }$ in the spare space at the left of the last line. Thus, the tableau would have the form

$$
\begin{array}{c} { \left| \begin{array} { l l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \cdots } & { a _ { 1 s } } \\ { c _ { 2 } } \\ { \vdots } \\ { c _ { s } } \\ { b _ { 0 } } \end{array} \right| } { a _ { 2 1 } }  & { a _ { 2 2 } } & { \cdots } & { a _ { 2 s } } \\ { { \left| \begin{array} { l l l l l } { \vdots } & { } & { \vdots } & { } & { \vdots } \\ { a _ { s 1 } } & { a _ { s 2 } } & { \cdots } & { a _ { s s } } \\ { b _ { 1 } } & { b _ { 2 } } & { \cdots } & { b _ { s } } \end{array} \right| } } \end{array} 
$$

As a Runge–Kutta method, to be used in the conventional manner as a onestep method for advancing the solution of a differential equation, this makes no sense at all, if $b _ { 0 } \neq 1$ . Indeed, the method would not even be covariant with respect to shifts of origin. However, the process of computing with a single step of this contrived method may play an important role as part of a more sophisticated computation. An important example of a generalized Runge–Kutta method is given by the one-stage tableau

$$
{ \frac { 0 \left| 0 } { 0 \right| 1 } } \ .
$$

This method does nothing other than computing $h$ multiplied by the derivative of the input value. Combined with linear operations, all Runge–Kutta methods can be built up from this basic method. The elementary weights associated with this method are given by

$$
\Phi ( t ) = { \left\{ \begin{array} { l l } { 1 , } & { t = \tau , } \\ { 0 , } & { t \neq \tau . } \end{array} \right. }
$$
