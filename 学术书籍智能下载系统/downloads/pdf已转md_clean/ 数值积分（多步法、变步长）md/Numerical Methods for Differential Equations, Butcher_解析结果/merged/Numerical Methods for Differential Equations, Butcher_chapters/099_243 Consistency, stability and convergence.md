# 243 Consistency, stability and convergence

Suppose we attempt the numerical solution of the simple differential equation $y ^ { \prime } ( x ) = 0$ , with exact solution $y ( x ) = 1$ , using the linear multistep method characterized by the pair of polynomials $\lfloor \alpha , \beta \rfloor$ . If the exact answer has already been found for $k$ steps in a row, it seems to be a desirable property of the method that the exact value is also found in one further step. This computed value is equal to $\alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k }$ . For this expression to have the value $^ { 1 }$ is equivalent to the assumption that $\alpha ( 1 ) = 0$ or, what is equivalent, that $\rho ( 1 ) = 0$ . Because of its fundamental importance, this property will be given the name ‘preconsistency’.

Another interpretation of preconsistency can be found in terms of the covariance of the numerical method with respect to a translation. By a translation we mean the replacing of an autonomous initial value problem $y ^ { \prime } ( x ) \ = \ f { \big ( } y ( x ) { \big ) }$ , $y ( x _ { 0 } ) ~ = ~ y _ { 0 }$ , by a related problem $z ^ { \prime } ( x ) ~ = ~ f ( z ( x ) + v )$ , $z ( x _ { 0 } ) = y _ { 0 } - v$ . For the exact solutions to these problems, the value of $z$ will always equal the value of $y$ with the vector $v$ subtracted. In considering a numerical solution to each of these problems, we can do the calculation in terms of $y$ and then carry out the translation afterwards; or we can do the transformation first and carry out the numerical approximation using the $z$ values. By ‘covariance’ we mean that the two numerical results are exactly the same.

It is easy to verify that the only way this can be guaranteed to happen, if the calculations are carried out using a linear multistep method, is for the method to be preconsistent.

For a preconsistent method it is desirable that the exact solution can also be found for another simple differential initial value problem: the problem given by $y ^ { \prime } ( x ) = 1$ , $y ( 0 ) = 0$ . For every step, the value of $f ( y _ { n } )$ is precisely 1. Substitute these into (242a), and it is found that

$$
n h = \sum _ { i = 1 } ^ { k } \alpha _ { i } h ( n - i ) + h \sum _ { i = 1 } ^ { k } \beta _ { i } ,
$$

implying that

$$
n \left( 1 - \sum _ { i = 1 } ^ { k } \alpha _ { i } \right) = \sum _ { i = 1 } ^ { k } \beta _ { i } - \sum _ { i = 1 } ^ { k } i \alpha _ { i } .
$$

The left-hand side vanishes for a preconsistent method, whereas the righthand side can be written in the form $\beta ( 1 ) + \alpha ^ { \prime } ( 1 )$ . A ‘consistent method’ is a method that satisfies the condition that $\beta ( 1 ) + \alpha ^ { \prime } ( 1 ) = 0$ , in addition to satisfying the preconsistency condition $\alpha ( 1 ) = 0$ .

No matter how precise numerical approximations to the solution to a differential equation might be, this precision has no ultimate benefit unless the effect on later step values of small errors is bounded. Later steps are effected by the introduction of a perturbation in step $m$ both through their dependence on $y _ { m }$ itself and through their dependence on $h f ( x _ { m } , y _ { m } )$ . To simplify the discussion we exclude the second cause of error dependence by restricting ourselves to a simple ‘quadrature’ type of problem in which $y ^ { \prime } ( x ) = f ( x )$ . This will mean that the difference between the unperturbed and perturbed problem will satisfy the even simpler equation $y ^ { \prime } ( x ) = 0$ . Consider the difference equation satisfied by the numerical solution just for the perturbation itself. This difference equation is

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } .
$$

A linear multistep method is said to be ‘stable’ if all solutions to the difference equation (243a) are bounded as $n \longrightarrow \infty$ .

From the theory of linear difference equations, we know exactly when this will be the case. It is necessary and sufficient that all zeros of the polynomial $\rho$ lie in the closed unit disc $\{ z : | z | \leq 1 \}$ and that all repeated zeros lie in the open unit disc $\{ z : | z | < 1 \}$ . Because the zeros of $\alpha$ are the reciprocals of those of $\rho$ we can equally state these conditions as (i) all zeros of $\alpha$ lie outside the open unit disc, and (ii) all repeated zeros of $\alpha$ lie outside the closed unit disc.

‘Convergence’ refers to the ability of a method to approximate the solution to a differential equation to any required accuracy, if sufficiently many small steps are taken. Of course, any numerical result computed by a linear multistep method will depend not only on the particular coefficients of the method and the differential equation, but also on the procedure used to obtain starting values. In the formal definition of this concept, we will not impose any conditions on how the starting values are approximated except to require that, as $h  0$ , the errors in the starting values tend to zero. Because the exact solution is continuous, this is equivalent to requiring that the starting values all converge to the initial value specified for the problem.

Divide the interval $[ x _ { 0 } , { \overline { { x } } } ]$ into $n$ steps each of size $h = ( \overline { { x } } - x _ { 0 } ) / n$ , for every positive integer $n$ . Solve a standard initial value problem using starting values $y _ { 0 }$ , $y _ { 1 }$ , $\cdot \cdot \cdot$ , $y _ { k - 1 }$ which depend on $h$ and converge to $y ( x _ { 0 } )$ as $h  0$ . Let the error in the approximation computed at $\scriptstyle { \overline { { x } } }$ be denoted by $\epsilon _ { n }$ . The method is convergent if necessarily $\epsilon _ { n } \to 0$ as $n \longrightarrow \infty$ .

We discuss this property, and its relationship to other concepts introduced in this subsection, in Chapter 4. In the meantime, we state without proof the important result expressed in the following.

Theorem 243A A linear multistep method is convergent if and only if it is stable and consistent.
