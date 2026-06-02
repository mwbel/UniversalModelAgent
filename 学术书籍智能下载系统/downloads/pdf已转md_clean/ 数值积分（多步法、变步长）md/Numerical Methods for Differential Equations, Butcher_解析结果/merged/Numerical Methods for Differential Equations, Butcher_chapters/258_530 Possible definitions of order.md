# 530 Possible definitions of order

Traditional methods for the approximation of differential equations are designed with a clear-cut interpretation in mind. For example, linear multistep methods are constructed on the assumption that, at the beginning of each step, approximations are available to the solution and to the derivative at a sequence of step points; the calculation performed by the method is intended to obtain approximations to these same quantities but advanced one step ahead. In the case of Runge–Kutta methods, only the approximate solution value at the beginning of a step is needed, and at the end of the step this is advanced one time step further.

We are not committed to these interpretations for either linear multistep or Runge–Kutta methods. For example, in the case of Adams methods, the formulation can be recast so that the data available at the start and finish of a step is expressed in terms of backward difference approximations to the derivative values or in terms of other linear combinations which approximate Nordsieck vectors. For Runge–Kutta methods the natural interpretation, in which $y _ { n }$ is regarded as an approximation to $y ( x _ { n } )$ , is not the only one possible. As we have seen in Subsection 389, the generalization to effective order is such an alternative interpretation.

For a general linear method, the $r$ approximations, $y _ { i } ^ { \lfloor n - 1 \rfloor }$ , $i = 1 , 2 , \dots , r$ , are imported into step $n$ and the $r$ corresponding approximations, $y _ { i } ^ { \left[ n \right] }$ , are exported at the end of the step. We do not specify anything about these quantities except to require that they are computable from an approximation to $y ( x _ { n } )$ and, conversely, the exact solution can be recovered, at least approximately, from y [i $y _ { i } ^ { [ n - 1 ] }$ , $i = 1 , 2 , \dots , r$ .

This can be achieved by associating with each input quantity, $y _ { i } ^ { \lfloor n - 1 \rfloor }$ , a generalized Runge–Kutta method,

$$
S _ { i } = \frac { c ^ { ( i ) } \enspace | \enspace { \cal A } ^ { ( i ) }  } { b _ { 0 } ^ { ( i ) } \enspace | \enspace b ^ { ( i ) T } \enspace } .
$$

Write $s _ { i }$ as the number of stages in $S _ { i }$ . The aim will be to choose these input approximations in such a way that if y[n−1]i is computed using Si applied to $y ( x _ { n - 1 } )$ , for $i = 1 , 2 , \dots , r$ , then the output quantities computed by the method, $y _ { i } ^ { [ n ] }$ , are close approximations to $S _ { i }$ applied to $y ( x _ { n } )$ , for $i = 1 , 2 , \dots , r$ .

We refer to the sequence of $r$ generalized Runge–Kutta methods $S _ { 1 } , S _ { 2 } , \ldots , S _ { r }$ as a ‘starting method’ for the general linear method under consideration and written as $S$ . It is possible to interpret each of the output quantities computed by the method, on the assumption that $S$ is used as a starting method, as itself a generalized Runge–Kutta method with a total of $s + s _ { 1 } + s _ { 2 } + \cdot \cdot \cdot + s _ { r }$ stages. It is, in principle, a simple matter to calculate the Taylor expansion for the output quantities of these methods and it is also a simple matter to calculate the Taylor expansion of the result found by shifting the exact solution forward one step. We write $S M$ for the vector of results formed by carrying out a step of $M$ based on the results of computing initial approximations using $S$ . Similarly, $_ { E S }$ will denote the vector of approximations formed by advancing the trajectory forward a time step $h$ and then applying each member of the vector of methods that constitutes $S$ to the result of this.

A restriction is necessary on the starting methods that can be used in practice. This is that at least one of $S _ { 1 }$ , $S _ { 2 } , \ldots ,$ $S _ { r }$ , has a non-zero value for the corresponding $b _ { 0 } ^ { ( i ) }$ . If $b _ { 0 } ^ { ( i ) } = 0$ , for all $i = 1$ , $2$ , $\cdot \cdot \cdot$ , $r$ , then it would not be possible to construct preconsistent methods or to find a suitable finishing procedure, $F ^ { \dagger }$ say, such that $S F$ becomes the identity method.

Accordingly, we focus on starting methods that are non-degenerate in the following sense.

Definition 530A A starting method $S$ defined by the generalized Runge– Kutta methods (530a), for $i \ = \ 1$ , 2, . . . , $r$ , is ‘degenerate’ if $b _ { 0 } ^ { ( i ) } = 0$ , for $i = 1$ , 2, . . . , $r$ , and ‘non-degenerate’ otherwise.

Definition 530B Consider a general linear method $M$ and a non-degenerate starting method $S$ . The method $M$ has order $p$ relative to $S$ if the results found from $S M$ and $E S$ agree to within $O ( ^ { p + 1 } )$ .

Definition 530C A general linear method $M$ has order $p$ if there exists a non-degenerate starting method $S$ such that $M$ has order $p$ relative to $S$ .

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0007_pages_0421-0484/auto/images/b516c4a268f24f380928fcb6e327a5875a866e56f0e2239c19ad64fdd4b4de8f.jpg)  
Representation of local truncation error

In using Definition 530C, it is usually necessary to construct, or at least to identify the main features of, the starting method $S$ which gives the definition a practical meaning. In some situations, where a particular interpretation of the method is decided in advance, Definition 530B is used directly. Even though the Taylor series expansions, needed to analyse order, are straightforward to derive, the details can become very complicated. Hence, in Subsection 532, we will build a framework for simplifying the analysis. In the meantime we consider the relationship between local and accumulated error.
