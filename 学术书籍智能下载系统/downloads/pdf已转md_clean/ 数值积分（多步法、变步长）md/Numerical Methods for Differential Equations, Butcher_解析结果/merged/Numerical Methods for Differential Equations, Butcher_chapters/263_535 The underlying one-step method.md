# 535 The underlying one-step method

In much the same way as a formal one-step method could be constructed as an underlying representation of a linear multistep method, as in Subsection 422, a one-step method can be constructed with the same underlying relationship to a general linear method. Consider a general linear method $( A , U , B , V )$ and suppose that the preconsistency vector is $u$ . We can ask if it is possible to find $\xi \in X ^ { r }$ and $\eta \in X _ { 1 } ^ { s }$ , such that (532e) and (532f) hold exactly but with $E$ replaced by $\theta \in X _ { 1 }$ ; that is, such that

$$
\begin{array} { r } { \eta ( t ) = A ( \eta D ) ( t ) + U \xi ( t ) , } \\ { ( \theta \xi ) ( t ) = B ( \eta D ) ( t ) + V \xi ( t ) , } \end{array}
$$

for all $t \in T ^ { \# }$ . In this case we can interpret $\theta$ as representing an underlying one-step method. The notional method represented by $\theta$ is not unique, because another solution can be found equal to ${ \widehat { \theta } } = \phi ^ { - 1 } \theta \phi$ , where $\phi \in X _ { 1 }$ is arbitrary. We see this by multiplying both sides of (535a) and (535b) by $\phi ^ { - 1 }$ to arrive at the relations

$$
\begin{array} { r } { \widehat { \eta } ( t ) = A ( \widehat { \eta } D ) ( t ) + U \widehat { \xi } ( t ) , } \\ { ( \widehat { \theta } \widehat { \xi } ) ( t ) = B ( \widehat { \eta } D ) ( t ) + V \widehat { \xi } ( t ) , } \end{array}
$$

with ${ \widehat { \xi } } = \phi ^ { - 1 } \xi$ . We want to explore the existence and uniqueness of the underlying one-step method subject to an additional assumption that some particular component of $\xi$ has a specific value. As a step towards this aim, we remark that (535a) and (535b) transform in a natural way if the method itself is transformed in the sense of Subsection 501. That is, if the method $( A , U , B , V )$ is transformed to $( A , U T ^ { - 1 } , T B , T V T ^ { - 1 } )$ , and (535a) and 535b) hold, then, in the transformed method, $\xi$ transforms to $T \xi$ and $\theta$ transforms to $T \theta T ^ { - 1 }$ . Thus

$$
\begin{array} { c } { { \eta ( t ) = A ( \eta D ) ( t ) + ( U T ^ { - 1 } ) ( T \xi ) ( t ) , } } \\ { { \ } } \\ { { ( ( T \theta T ^ { - 1 } ) ( T \xi ) ) ( t ) = T B ( \eta D ) ( t ) + V ( T \xi ) ( t ) . } } \end{array}
$$

This observation means that we can focus on methods for which $u = e _ { 1 }$ , the first member of the natural basis for $\mathbb { R } ^ { r }$ , in framing our promised uniqueness result.

Theorem 535A Let $( A , U , B , V )$ denote a consistent general linear method such that $u = e _ { 1 }$ and such that

$$
U = [ \mathbf { 1 } \quad \widetilde { U } ] , \qquad V = \left[ \begin{array} { l l } { 1 } & { \widetilde { v } ^ { \intercal } } \\ { 0 } & { \widetilde { V } } \end{array} \right] ,
$$

where $1 \not \in \sigma ( \overset { \sim } { V } )$ . Then there exists a unique solution to (535a) and (535b) for which $\xi _ { 1 } = 1$ .

Proof. By carrying out a further transformation if necessary, we may assume without loss of generality that $\widetilde { V }$ is lower triangular. The conditions satisfied by $\xi _ { i } ( t )$ $i = 2 , 3 , \ldots , r$ ), $\eta _ { i } ( t )$ ( $i = 1 , 2 , \dots , s$ ) and $\theta ( t )$ can now be written in the form

$$
( 1 - \widetilde { V } _ { i , i } ) \xi _ { i } ( t ) = \sum _ { j = 1 } ^ { s } b _ { i j } ( \eta D ) ( t ) + \sum _ { j = 2 } ^ { i - 1 } \widetilde { V } _ { i - 1 , j - 1 } \xi _ { j } ( t ) ,
$$

$$
\eta _ { i } ( t ) = \sum _ { j = 1 } ^ { s } a _ { i j } ( \eta D ) ( t ) + 1 ( t ) + \sum _ { j = 2 } ^ { r } \widetilde { U } _ { i , j - 1 } \xi _ { j } ( t ) ,
$$

$$
\theta ( t ) = \sum _ { j = 1 } ^ { s } b _ { 1 j } ( \eta D ) ( t ) + 1 ( t ) + \sum _ { j = 2 } ^ { r } \widetilde v _ { j - 1 } \xi _ { j } ( t ) .
$$

In each of these equations, the right-hand sides involve only trees with order lower than $r ( t )$ or terms with order $r ( t )$ which have already been evaluated. Hence, the result follows by induction on $r ( t )$ . 

The extension of the concept of underlying one-step method to general linear methods was introduced in Stoffer (1993).

Although the underlying one-step method is an abstract structure, it has practical consequences. For a method in which $\rho ( \overset { \sim } { V } ) < 1$ , the performance of a large number of steps, using constant stepsize, forces the local errors to conform to Theorem 535A. When the stepsize needs to be altered, in accordance with the behaviour of the computed solution, it is desirable to commence the step following the change, with input approximations consistent with what the method would have expected if the new stepsize had been used for many preceding steps. Although this cannot be done precisely, it is possible for some of the most dominant terms in the error expansion to be adjusted in accordance with this requirement. With this adjustment in place, it becomes possible to make use of information from the input vectors, as well as information computed within the step, in the estimation of local truncation errors. It also becomes possible to obtain reliable information that can be used to assess the relative advantages of continuing the integration with an existing method or of moving onto a higher order method. These ideas have already been used to good effect in Butcher and Jackiewicz (2003) and further developments are the subject of ongoing investigations.

# Exercises 53

53.1 A numerical method of the form

$$
\begin{array} { r l } & { \cdot _ { 1 } ^ { [ n ] } = y _ { n - 1 } + h \widehat { a } _ { 1 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { a } _ { 1 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h a _ { 1 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h a _ { 1 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \\ & { \cdot _ { 2 } ^ { [ n ] } = y _ { n - 1 } + h \widehat { a } _ { 2 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { a } _ { 2 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h a _ { 2 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h a _ { 2 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \\ & { \qquad \quad + h a _ { 2 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h a _ { 2 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) } \\ & { \qquad \quad + h \widehat { b } _ { 1 } f \big ( x _ { n - 2 } + h c _ { 1 } , Y _ { 1 } ^ { [ n - 1 ] } \big ) + h \widehat { b } _ { 2 } f \big ( x _ { n - 2 } + h c _ { 2 } , Y _ { 2 } ^ { [ n - 1 ] } \big ) } \\ & { \qquad \quad + h b _ { 1 } f \big ( x _ { n - 1 } + h c _ { 1 } , Y _ { 1 } ^ { [ n ] } \big ) + h b _ { 2 } f \big ( x _ { n - 1 } + h c _ { 2 } , Y _ { 2 } ^ { [ n ] } \big ) , } \end{array}
$$

is sometimes known as a ‘two-step Runge–Kutta method’. Find conditions for this method to have order 4.

53.2 Find an explicit fourth order method ( $a _ { 1 1 } = a _ { 1 2 } = a _ { 2 2 } = 0$ ) of the form given by Exercise 53.1.

53.3 Find an A-stable method of the form given by Exercise 53.1.
