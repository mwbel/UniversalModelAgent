# 112 Stiff differential equations

Many differential equation systems of practical importance in scientific modelling exhibit a distressing behaviour when solved by classical numerical methods. This behaviour is distressing because these systems are characterized by very high stability, which can turn into very high instability when approximated by standard numerical methods. We have already seen examples of stiff problems, in Subsections 102 and 104, and of course there are many more such examples. The concept of the ‘one-sided Lipschitz condition’ was mentioned in Subsection 110 without any explanation. Stiff problems typically have large Lipschitz constants, but many have more manageable one-sided Lipschitz constants, and this can be an aid in obtaining realistic growth estimates for the effect of perturbations.

We confine ourselves to problems posed on an inner product space. Thus we assume that there exists an inner product on $\mathbb { R } ^ { N }$ denoted by $\langle u , v \rangle$ , and that the norm is defined by $\| u \| ^ { 2 } = \langle u , u \rangle$ .

Definition 112A The function f satisfies a ‘one-sided Lipschitz condition’, with ‘one-sided Lipschitz constant’ l if for $a l l x \in [ a , b ]$ and $a l l u , v \in \mathbb { R } ^ { N } ,$

$$
\langle f ( x , u ) - f ( x , v ) , u - v \rangle \leq l \| u - v \| ^ { 2 } .
$$

It is possible that the function $f$ could have a very large Lipschitz constant but a moderately sized, or even negative, one-sided Lipschitz constant. The advantage of this is seen in the following result.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/e7f68e229af62882ede24da454c5abfb9966990dc6e200fc5e51b776db818b68.jpg)

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0001_pages_0001-0070/auto/images/70566a35b72b86ad7795b1debf17114d7e5eb9210cc26f255e4c60b9f65e3e2a.jpg)

Proof. We have

$$
\begin{array} { l } { \displaystyle \frac { d } { d x } \| y ( x ) - z ( x ) \| ^ { 2 } = \frac { d } { d x } \langle y ( x ) - z ( x ) , y ( x ) - z ( x ) \rangle } \\ { = 2 \langle f ( x , y ( x ) ) - f ( x , z ( x ) ) , y ( x ) - z ( x ) \rangle } \\ { \leq 2 l \| y ( x ) - z ( x ) \| ^ { 2 } . } \end{array}
$$

Multiply by $\exp \big ( - 2 l ( x - x _ { 0 } ) \big )$ and it follows that

$$
\frac { d } { d x } \big ( \exp \big ( - 2 l ( x - x _ { 0 } ) \big ) \| y ( x ) - z ( x ) \| ^ { 2 } \big ) \leq 0 ,
$$

so that $\exp \big ( - 2 l ( x - x _ { 0 } ) \big ) \| y ( x ) - z ( x ) \| ^ { 2 }$ is non-increasing.

Note that the problem described in Subsection 102 possesses the one-sided Lipschitz condition with ${ \mathit { l } } = 0$ .

Even though stiff differential equation systems are typically non-linear, there is a natural way in which a linear system arises from a given non-linear system. Since stiffness is associated with the behaviour of perturbations to a given solution, we suppose that there is a small perturbation $\epsilon Y ( x )$ t o a solution $y ( x )$ . The parameter $\epsilon$ is small, in the sense that we are interested only in asymptotic behaviour of the perturbed solution as this quantity approaches zero. If $y ( x )$ is replaced by $y ( x ) + \epsilon Y ( x )$ in the differential equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

and the solution expanded in a series in powers of $\epsilon$ , with $\epsilon ^ { 2 }$ and higher powers replaced by zero, we obtain the system

$$
y ^ { \prime } ( x ) + \epsilon Y ^ { \prime } ( x ) = f ( x , y ( x ) ) + \epsilon { \frac { \partial f } { \partial y } } Y ( x ) .
$$

Subtract (112a) from (112b) and cancel out $\epsilon$ , and we arrive at the equation governing the behaviour of the perturbation,

$$
Y ^ { \prime } ( x ) = \frac { \partial f } { \partial y } Y ( x ) = J ( x ) Y ( x ) ,
$$

say. The ‘Jacobian matrix’ $J ( x )$ has a crucial role in the understanding of problems of this type; in fact its spectrum is sometimes used to characterize stiffness. In a time interval $\Delta x ,$ chosen so that there is a moderate change in the value of the solution to (112a), and very little change in $J ( x ) ,$ the eigenvalues of $J ( x )$ determine the growth rate of components of the perturbation. The existence of one or more large and negative values of $\lambda \Delta x ,$ $\mathrm { f o r } \ \lambda \in \sigma ( J ( x ) )$ , the spectrum of $J ( x )$ , is a sign that stiffness is almost certainly present. If $J ( x )$ possesses complex eigenvalues, then we interpret this test for stiffness as the existence of $\mathrm { ~ a ~ } \lambda = \mathrm { { R e } } \lambda + i \mathrm { { I m } } \lambda \in \sigma ( J ( x ) )$ such that Reλ∆x is negative with large magnitude.

# Exercises 11

11.1 Show how to modify Theorem 110C so that the Lipschitz condition holds only in a neighbourhood of $y _ { 0 }$ and where the solution is only required to exist on $[ a , b ]$ , where $\widetilde { b }$ satisfies $a < \widetilde { b } \le b$ .

11.2 By finding two vectors $\alpha$ and $\beta$ so that the system

$$
\begin{array} { r } { y ^ { \prime } ( x ) = \left[ \begin{array} { c c c } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] y ( x ) + \left[ \begin{array} { c } { \sin ( x ) } \\ { 0 } \\ { \cos ( x ) } \end{array} \right] , } \end{array}
$$

has a solution of the form ${ \widehat { y } } ( x ) = \sin ( x ) \alpha + \cos ( x ) \beta$ , find the general solution to this problem.
