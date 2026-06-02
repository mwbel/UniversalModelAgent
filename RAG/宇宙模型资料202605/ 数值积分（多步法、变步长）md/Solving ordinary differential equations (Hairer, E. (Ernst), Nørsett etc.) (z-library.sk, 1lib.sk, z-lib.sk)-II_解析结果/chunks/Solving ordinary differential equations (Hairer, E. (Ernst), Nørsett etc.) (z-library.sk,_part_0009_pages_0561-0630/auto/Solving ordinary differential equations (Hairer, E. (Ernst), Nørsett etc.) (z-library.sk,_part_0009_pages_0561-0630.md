# Properties of the Exact Flow

Every solution of the system (8.1) satisfies (8.1c) and (8.3a). It therefore lies on the manifold

$$
\mathcal { M } = \{ ( p , q ) | g ( q ) = 0 , G ( q ) H _ { p } ( p , q ) = 0 \} .
$$

Extracting $\lambda$ from (8.3b) (this is possble,if (8.4) is satisfied),and inserting the resulting expression into (8.1b), yields a differential equation on the manifold $\mathcal { M }$ . The situation here is completely analogous to that of (1.22) of Sect. VII.1.

Symplecticity. Our next aim is to extend the result of Theorem I.14.12 to constrained Hamiltonian systems. We consider the differential 2-form

$$
\omega ^ { 2 } = \sum _ { I = 1 } ^ { n } d p ^ { I } \wedge d q ^ { I }
$$

$p ^ { I }$ and $q ^ { I }$ denote the components of the vectors $p$ and $q$ , respectively). The flow of the system (8.1), mapping an initial value $( p _ { 0 } , q _ { 0 } ) \in \mathcal { M }$ onto $( p ( t ) , q ( t ) ) \in \mathcal { M }$ ， is denoted by $\varphi _ { t }$ . For a differentiable function $g : { \mathcal { M } }  { \mathcal { M } }$ we further denote by $g ^ { * } \omega ^ { 2 }$ the differential 2-form,defined by

$$
( g ^ { * } \omega ^ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } ) = \omega ^ { 2 } \big ( g ^ { \prime } ( p , q ) \xi _ { 1 } , g ^ { \prime } ( p , q ) \xi _ { 2 } \big ) .
$$

This is formally identical to Definition I.14.11, but here we are only interested in the case where $\xi _ { 1 }$ and $\xi _ { 2 }$ lie in the tangent space

$$
T _ { ( p , q ) } { \mathcal { M } } = { \Big \{ } ( u , v ) \ | \ G ( q ) v = 0 , \ { \frac { d } { d q } } { \big ( } G ( q ) H _ { p } ( p , q ) { \big ) } v + G ( q ) H _ { p p } ( p , q ) u = 0 { \Big \} }
$$

of the manifold (8.5).

Theorem 8.1. The flow $\varphi _ { t } : { \mathcal { M } }  { \mathcal { M } }$ of the system (8.1) is $a$ symplectic transformation on $\ M , i . e .$ ，

$$
( \varphi _ { t } ^ { * } \omega ^ { 2 } ) ( \xi _ { 1 } , \xi _ { 2 } ) = \omega ^ { 2 } ( \xi _ { 1 } , \xi _ { 2 } )
$$

for all $t$ ,for all $( p , q )$ , and for all $\xi _ { 1 } , \xi _ { 2 }$ lying in the tangent space $T _ { ( p , q ) } { \mathcal { M } }$

Proof.For $\xi \in T _ { ( p , q ) } M$ the tangent vector $\xi ^ { t } = \varphi _ { t } ^ { \prime } ( p , q ) \xi \in T _ { ( p ( t ) , q ( t ) ) } \mathcal { M }$ is a solution of the variational equation

$$
\begin{array} { l } { { \displaystyle \dot { \delta p } ^ { I } = - \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } H } { \partial q ^ { I } \partial p ^ { J } } ( p , q ) \cdot \delta p ^ { J } - \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } H } { \partial q ^ { I } \partial q ^ { J } } ( p , q ) \cdot \delta q ^ { J } } } \\ { { \displaystyle \qquad - \sum _ { K = 1 } ^ { m } \lambda ^ { K } \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } g ^ { K } } { \partial q ^ { I } \partial q ^ { J } } ( p , q ) \cdot \delta q ^ { J } - \sum _ { K = 1 } ^ { m } \frac { \partial g ^ { K } } { \partial q ^ { I } } ( q ) \cdot \delta \lambda ^ { K } } } \\ { { \displaystyle \dot { \delta q } ^ { I } = \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } H } { \partial p ^ { I } \partial p ^ { J } } ( p , q ) \cdot \delta p ^ { J } + \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } H } { \partial p ^ { I } \partial q ^ { J } } ( p , q ) \cdot \delta q ^ { J } } , }  \end{array}
$$

where the $\delta \lambda ^ { K }$ (for $K = 1 , \ldots , m )$ are obtained by differentiation of (8.3b). We now compute the time derivative of $\omega ^ { 2 } \big ( \xi _ { 1 } ^ { t } , \xi _ { 2 } ^ { t } \big )$ . The terms, not depending on $\lambda$ or $\delta \lambda$ , vanish by Theorem I.14.12. We therefore get

$$
\begin{array} { c } { { \displaystyle { \displaystyle \frac { d } { d t } \omega ^ { 2 } ( \xi _ { 1 } ^ { t } , \xi _ { 2 } ^ { t } ) = - \Big ( \sum _ { K = 1 } ^ { m } \lambda ^ { K } \sum _ { I , J = 1 } ^ { n } \frac { \partial ^ { 2 } q ^ { K } ( q ) } { \partial q ^ { I } \partial q ^ { J } } d q ^ { J } \wedge d q ^ { I } } } } \\ { { + \sum _ { K = 1 } ^ { m } d \lambda ^ { K } \wedge \Big ( \sum _ { I = 1 } ^ { n } \frac { \partial g ^ { K } ( q ) } { \partial q ^ { I } } d q ^ { I } \Big ) \big ) ( \xi _ { 1 } ^ { t } , \xi _ { 2 } ^ { t } ) . } } \end{array}
$$

Due to the symmetry of the second partial drivatives, the first expression of the right-hand side of Eq.(8.7) vanishes. The second expression also vanishes, because $\xi _ { 2 } ^ { t }$ lies in the tangent space $T _ { ( p ( t ) , q ( t ) ) } \mathcal { M }$ .Hence, $\omega ^ { 2 } \big ( \xi _ { 1 } ^ { t } , \xi _ { 2 } ^ { t } \big )$ is constant, what proves the statement of the theorem. □

Preservation of the Hamiltonian. Differentiation of $H ( p ( t ) , q ( t ) )$ with respect to time yields

$$
- H _ { p } ^ { T } H _ { q } - H _ { p } ^ { T } G ^ { T } \lambda + H _ { q } ^ { T } H _ { p } ,
$$

with all expressions evaluated at $( p ( t ) , q ( t ) )$ . The first term cancels with the last one,and the remaining term vanishes, because $G ( q ) H _ { p } ( p , q ) = 0$ on the solution manifold. Consequently, the Hamiltonian function ${ \tilde { H } } ( { \bar { p } } , q )$ is constant along solutions of (8.1).

# First Order Symplectic Method

We shall now discuss in some detail the feasibility, the convergence, and the symplecticity of a simple first order method. The presented ideas will be useful for a better understanding of the later discussion of higher order methods.

Inspired by (I.16.54), we consider the following discretization of (8.1):

$$
\begin{array} { r l } & { \widehat { p } _ { 1 } = p _ { 0 } - h \big ( H _ { q } ( \widehat { p } _ { 1 } , q _ { 0 } ) + G ^ { T } ( q _ { 0 } ) \lambda _ { 1 } \big ) } \\ & { q _ { 1 } = q _ { 0 } + h H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } ) } \\ & { \ 0 = g ( q _ { 1 } ) . } \end{array}
$$

The numerical approximation $( \widehat { p } _ { 1 } , q _ { 1 } )$ satisfies the constraint (8.1c), but not (8.3a). Therefore, we append the projection

$$
\begin{array} { c } { p _ { 1 } = \widehat { p } _ { 1 } - h G ^ { T } ( q _ { 1 } ) \mu } \\ { 0 = G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) , } \end{array}
$$

so that method $\left( 8 . 8 \mathsf { a - e } \right)$ yields approximations that stay in the manifold $\mathcal { M }$ of Eq. (8.5).

Existence of the Numerical Solution. We consider a slightly more general system than (8.8). If the initial values are not consistent, we replace the relations (8.8c) and (8.8e) by

$$
\begin{array} { l } { { g ( q _ { 1 } ) = g ( q _ { 0 } ) + h G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) } } \\ { { G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) = G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) . } } \end{array}
$$

We shall show that the nonlinear system (8.8a,b), (8.9a) has a locally unique solution. Inspired by the proof of Theorem 3.1 we write

$$
g ( q _ { 1 } ) - g ( q _ { 0 } ) = \int _ { 0 } ^ { 1 } g _ { q } \big ( { q } _ { 0 } + \tau ( q _ { 1 } - q _ { 0 } ) \big ) d \tau \cdot ( q _ { 1 } - q _ { 0 } ) .
$$

Inserting $g ( q _ { 1 } )$ from (8.9a) and $q _ { 1 }$ from (8.8b) and dividing by $h$ yields

$$
G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) = \int _ { 0 } ^ { 1 } g _ { q } \big ( q _ { 0 } + \tau ( q _ { 1 } - q _ { 0 } ) \big ) d \tau \cdot H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } ) .
$$

We next develop $H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } )$ as

$$
H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } ) = H _ { p } ( p _ { 0 } , q _ { 0 } ) - h \int _ { 0 } ^ { 1 } H _ { p p } \big ( p _ { 0 } + \sigma ( \widehat { p } _ { 1 } - p _ { 0 } ) , q _ { 0 } \big ) d \sigma \big ( H _ { q } ( \widehat { p } _ { 1 } , q _ { 0 } ) + G ^ { T } ( q _ { 0 } ) \lambda _ { 1 } \big ) .
$$

Inserting this formula into (8.10),an integration by parts shows that (8.9a) is equivalent to

$$
\begin{array} { c } { { 0 = \displaystyle \int _ { 0 } ^ { 1 } ( 1 - \tau ) g _ { q q } \big ( q _ { 0 } + \tau ( q _ { 1 } - q _ { 0 } ) \big ) d \tau \cdot \big ( H _ { p } ( p _ { 0 } , q _ { 0 } ) , H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } ) \big ) \qquad ( 8 . 1 1 ) } } \\ { { \displaystyle - \int _ { 0 } ^ { 1 } g _ { q } \big ( q _ { 0 } + \tau ( q _ { 1 } - q _ { 0 } ) \big ) d \tau \int _ { 0 } ^ { 1 } H _ { p p } \big ( p _ { 0 } + \sigma ( \widehat { p } _ { 1 } - p _ { 0 } ) , q _ { 0 } \big ) d \sigma \big ( H _ { q } ( \widehat { p } _ { 1 } , q _ { 0 } ) + G ^ { T } ( q _ { 0 } ) \lambda _ { 1 } \big ) } } \end{array}
$$

This is a linear system for $\lambda _ { 1 }$ and allows us to express $\lambda _ { 1 }$ smoothly in terms of $\widehat { p } _ { 1 } , q _ { 1 }$ ，and of the initial values $p _ { 0 } , q _ { 0 }$ . We insert the resulting expression for $\lambda _ { 1 }$ into (8.8a). Hence, (8.8a,b) becomes a nonlinear system for ${ \widehat { p } } _ { 1 } , q _ { 1 }$ ，which, for sufficiently small $h$ , has a unique solution close to $p _ { 0 } , q _ { 0 }$ (Implicit Function Theorem). It is interesting to note that, for $h  0$ , the value $\lambda _ { 1 }$ from (8.11) does not converge to $\lambda ( 0 )$ , given by (8.3b),but to the solution $\lambda _ { 0 }$ of

$$
0 = \frac { 1 } { 2 } g _ { q q } ( H _ { p } , H _ { p } ) - G H _ { p p } ( H _ { q } + G ^ { T } \lambda _ { 0 } ) .
$$

Here,allfunctions are evaluated at the initial value $( p _ { 0 } , q _ { 0 } )$

The existence of the solution $( p _ { 1 } , \mu )$ to the system (8.8d),(8.9b) follows from the Newton-Kantorovich Theorem (Ortega & Rheinboldt 1970) with initial approximation $p _ { 1 } : = \widehat { p } _ { 1 }$ ,and $\mu = 0$ , or also from the Implicit Function Theorem.

We have not only shown that the system (8.8) possesses a locally unique solution, but we have also seen that the replacement of (8.8c,e) by (8.9) extends the definition of the method to arbitrary initial values (close to $M$ ). We thus have

found a one-step method

$$
{ \binom { p _ { 1 } } { q _ { 1 } } } = { \binom { p _ { 0 } } { q _ { 0 } } } + h \Phi \left( { \binom { p _ { 0 } } { q _ { 0 } } } , h \right)
$$

in $\mathbb { R } ^ { 2 n }$ , which reduces to (8.8) on the manifold $\ M$ . For smooth functions $g$ and $H$ also $\Phi$ is smooth, and the classical theory (convergence, asymptotic expansions, ...） can be applied to this method.

Convergence of Order 1. It is sufficient to show that the local error is of size $\mathcal { O } ( h ^ { 2 } )$ . The convergence then follows from Theorem II.3.6 applied to (8.12). From the above investigation on the existence of the numerical solution we know that $\widehat { p } _ { 1 } = p _ { 0 } + \mathcal { O } ( h )$ ， $q _ { 1 } = q _ { 0 } + \mathcal { O } ( h )$ ，and $\lambda _ { 1 } = \lambda _ { 0 } + \mathcal { O } ( h )$ . Consequently, we have from (8.8a,b) that

$$
q _ { 1 } = q ( t _ { 0 } + h ) + \mathcal { O } ( h ^ { 2 } ) , \qquad \widehat { p } _ { 1 } = p ( t _ { 0 } + h ) - h G ^ { T } ( q _ { 0 } ) \delta \lambda + \mathcal { O } ( h ^ { 2 } )
$$

with $\delta \lambda = \lambda _ { 0 } - \lambda ( t _ { 0 } )$ . The disturbing term $h G ^ { T } ( q _ { 0 } ) \delta \lambda$ is eliminated by the pro-jection (8.8d,e). This can be seen as follows: from (8.13) and (8.8d) we know that $p _ { 1 } = p ( t _ { 0 } + h ) - G ^ { T } ( q _ { 0 } ) \nu + \mathcal { O } ( h ^ { 2 } )$ , so that

$$
G \big ( q ( t _ { 0 } + h ) \big ) H _ { p } \big ( p ( t _ { 0 } + h ) - G ^ { T } ( q _ { 0 } ) \nu , q ( t _ { 0 } + h ) \big ) = \mathcal { O } ( h ^ { 2 } ) .
$$

By (8.4) and the Implicit Function Theorem this implies $\nu = \mathcal { O } ( h ^ { 2 } )$ , and the local error for both components ( $p$ and $q$ ) is of size $\mathcal { O } ( h ^ { 2 } )$

Symplecticity. Differentiation of the relations (8.8a,b) shows that (we use upper indices for the components)

$$
\begin{array} { c } { { d \widehat { p } _ { 1 } ^ { I } = d p _ { 0 } ^ { I } - h \displaystyle \sum _ { J = 1 } ^ { n } \displaystyle \sum _ { \widetilde { \partial } q ^ { I } \partial p ^ { J } } ^ { \partial ^ { 2 } H } ( \widehat { p } _ { 1 } , q _ { 0 } ) d \widehat { p } _ { 1 } ^ { J } - h \displaystyle \sum _ { J = 1 } ^ { n } \displaystyle \frac { \partial ^ { 2 } H } { \partial q ^ { I } \partial q ^ { J } } ( \widehat { p } _ { 1 } , q _ { 0 } ) d q _ { 0 } ^ { J } } } \\ { { - h \displaystyle \sum _ { K = 1 } ^ { m } \lambda _ { 1 } ^ { K } \displaystyle \sum _ { J = 1 } ^ { n } \displaystyle \frac { \partial ^ { 2 } g ^ { K } } { \partial q ^ { I } \partial q ^ { J } } ^ { ( } q _ { 0 } ) d q _ { 0 } ^ { J } - h \displaystyle \sum _ { K = 1 } ^ { m } \displaystyle \frac { \partial g ^ { K } } { \partial q ^ { I } } ^ { ( } q _ { 0 } ) d \lambda _ { 1 } ^ { K } } } \\ { { d q _ { 1 } ^ { I } = d q _ { 0 } ^ { I } + h \displaystyle \sum _ { J = 1 } ^ { n } \displaystyle \frac { \partial ^ { 2 } H } { \partial p ^ { I } \partial p ^ { J } } ^ { ( } \widehat { p } _ { 1 } , q _ { 0 } ) d \widehat { p } _ { 1 } ^ { J } + h \displaystyle \sum _ { J = 1 } ^ { n } \displaystyle \frac { \partial ^ { 2 } H } { \partial p ^ { I } \partial q ^ { J } } ^ { ( } \widehat { p } _ { 1 } , q _ { 0 } ) d q _ { 0 } ^ { J } . } } \end{array}
$$

Taking the exterior product of the first formula with $d q _ { 0 } ^ { I }$ ,and of the second formula with $d \widehat { p } _ { 1 } ^ { I }$ , several terms cancel out (as in the proof of Theorem 8.1) and we obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { I = 1 } ^ { n } d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 0 } ^ { I } = \sum _ { I = 1 } ^ { n } d p _ { 0 } ^ { I } \wedge d q _ { 0 } ^ { I } - h \sum _ { I , J = 1 } ^ { n } \widehat { \partial } q ^ { I } \partial p ^ { J } } ( \widehat { p } _ { 1 } , q _ { 0 } ) d \widehat { p } _ { 1 } ^ { J } \wedge d q _ { 0 } ^ { I } }  \\ { { \displaystyle \sum _ { I = 1 } ^ { n } d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } = \sum _ { I = 1 } ^ { n } d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 0 } ^ { I } + h \sum _ { I , J = 1 } ^ { n } \widehat { \partial } p ^ { I } \partial q ^ { J } } ( \widehat { p } _ { 1 } , q _ { 0 } ) d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 0 } ^ { J } . }  \end{array}
$$

Summing up both formulas yields

$$
\sum _ { I = 1 } ^ { n } d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } = \sum _ { I = 1 } ^ { n } d p _ { 0 } ^ { I } \wedge d q _ { 0 } ^ { I } ,
$$

what proves that the method $\left( 8 . 8 \mathsf { a - c } \right)$ is symplectic. In order to show that also the projection (8.8d,e) is symplectic, we compute

$$
d p _ { 1 } ^ { I } = d \widehat { p } _ { 1 } ^ { I } - h \sum _ { K = 1 } ^ { m } \mu ^ { K } \sum _ { J = 1 } ^ { n } \frac { \partial ^ { 2 } g ^ { K } } { \partial q ^ { I } \partial q ^ { J } } ( q _ { 1 } ) d q _ { 1 } ^ { J } - h \sum _ { K = 1 } ^ { m } \frac { \partial g ^ { K } } { \partial q ^ { I } } ( q _ { 1 } ) d \mu ^ { K } ,
$$

and we obtain as above (using $g ( q _ { 1 } ) = 0$ ）that

$$
\sum _ { I = 1 } ^ { n } d p _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } = \sum _ { I = 1 } ^ { n } d \widehat { p } _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } .
$$

Equations (8.14) and (8.15) together show that the complete procedure (8.8a-e) is symplectic.

# SHAKE and RATTLE

These algorithms have been designed for problems with separable Hamiltonian

$$
{ \cal H } ( p , q ) = \frac { 1 } { 2 } p ^ { T } { \cal M } ^ { - 1 } p + { \cal U } ( q )
$$

(constant matrix $M$ ),and are very popular in molecular dynamics simulation. Observe that for this Hamiltonian the problem (8.1) becomes the second order diferential equation $M q ^ { \prime \prime } = - U _ { q } ( q ) - G ^ { T } ( q ) \lambda$ with constraint (8.1c).

SHAKE.This method,due to Ryckaert, Ciccoti & Berendsen (1977),isgiven by

$$
\begin{array} { c } { { q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = - h ^ { 2 } M ^ { - 1 } \big ( U _ { q } \big ( q _ { n } \big ) + G ^ { T } \big ( q _ { n } \big ) \lambda _ { n } \big ) } } \\ { { 0 = g \big ( q _ { n + 1 } \big ) . } } \end{array}
$$

In the absence of constraints it is identical to Stormer's method (Sect.III.1O), which in molecular dynamics applications is often referred the Verlet method (Verlet 1967). The $p$ -components are approximated by $p _ { n } = M ( q _ { n + 1 } - q _ { n - 1 } ) / 2 h$ .For an implementation of this 2-step method a stabilized version is recommended (see the end of Sect.III.10).

RATTLE. Denoting $p _ { n + 1 / 2 } : = p _ { n } - ( h / 2 ) ( U _ { q } ( q _ { n } ) + G ^ { T } ( q _ { n } ) \lambda _ { n } )$ , the SHAKE al-gorithm can be rewritten in the form

$$
\begin{array} { c } { { p _ { n + 1 / 2 } = p _ { n } - \displaystyle \frac { h } { 2 } \big ( U _ { q } ( q _ { n } ) + G ^ { T } ( q _ { n } ) \lambda _ { n } \big ) } } \\ { { q _ { n + 1 } = q _ { n } + h M ^ { - 1 } p _ { n + 1 / 2 } } } \\ { { 0 = g \big ( q _ { n + 1 } \big ) . } } \end{array}
$$

The definition of $p _ { n + 1 }$ as in the SHAKE method requires the knowledge of $q _ { n + 2 }$ In order toavoidthis difficulty, Andersen (1983)suggests todefine $p _ { n + 1 }$ by

$$
\begin{array} { c } { { p _ { n + 1 } = p _ { n + 1 / 2 } - \displaystyle \frac { h } { 2 } \big ( { \cal U } _ { q } ( q _ { n + 1 } ) + G ^ { T } ( q _ { n + 1 } ) \mu _ { n } \big ) } } \\ { { 0 = G ( q _ { n + 1 } ) { \cal M } ^ { - 1 } p _ { n + 1 } , } } \end{array}
$$

so that also the hidden constraint (8.3a) is satisfied. These two equations constitute a linear system for $\left( p _ { n + 1 } , \mu _ { n } \right)$

Extension to General Hamiltonian Functions. It was observed by Jay (1994) that the RATTLE algorithm can be extended to general Hamiltonian functions as follows: for consistent values $( p _ { n } , q _ { n } ) \in { \mathcal { M } }$ define

$$
\begin{array} { c } { { p _ { n + 1 / 2 } = p _ { n } - \displaystyle \frac { h } { 2 } \big ( H _ { q } \big ( p _ { n + 1 / 2 } , q _ { n } \big ) + G ^ { T } \big ( q _ { n } \big ) \lambda _ { n } \big ) } } \\ { { q _ { n + 1 } = q _ { n } + \displaystyle \frac { h } { 2 } \big ( H _ { p } \big ( p _ { n + 1 / 2 } , q _ { n } \big ) + H _ { p } \big ( p _ { n + 1 / 2 } , q _ { n + 1 } \big ) \big ) } } \\ { { 0 = g \big ( q _ { n + 1 } \big ) , } } \\ { { p _ { n + 1 } = p _ { n + 1 / 2 } - \displaystyle \frac { h } { 2 } \big ( H _ { q } \big ( p _ { n + 1 / 2 } , q _ { n + 1 } \big ) + G ^ { T } \big ( q _ { n + 1 } \big ) \mu _ { n } \big ) } } \\ { { 0 = G \big ( q _ { n + 1 } \big ) H _ { p } \big ( p _ { n + 1 } , q _ { n + 1 } \big ) . } } \end{array}
$$

This is the special case $s \approx 2$ of the Lobatto IIIA-IIIB pair to be discussed below.

The equations $( 8 . 1 9 \mathrm { a - c } )$ constitute a nonlinear system for the unknowns Pn+1/2，qn+1, and Xn. In the same way as for the method (8.8) we can reformulate Eq.(8.19c) in such a way that $\lambda _ { n }$ can be expressed smoothly in terms of $p _ { n } , \ q _ { n } , \ p _ { n + 1 / 2 } , \ q _ { n + 1 }$ ，and $h$ . Hence, the numerical solution exists, is locally unique,and depends smoothly on $h$ and on the initial values $( p _ { n } , q _ { n } )$ . The same is true for the system $_ { ( 8 . 1 9 \mathrm { d } , \mathsf { e } ) }$ . If the equations $_ { ( 8 . 1 9 \mathrm { c } , \mathsf { e } ) }$ are replaced by (8.9), we get a smooth extension of the method (8.19),defined on a neighbourhood of $\ M$ in R2n

Theorem 8.2. The numerical method (8.19) is symmetric, convergent of order 2, and symplectic.

Proof. a) We consider the more general situation, where $_ { ( 8 . 1 9 \mathrm { c } , \mathsf { e } ) }$ is replaced by (8.9). Replacing then $h$ by $- h$ , and exchanging $( p _ { n } , q _ { n } )$ with $( p _ { n + 1 } , q _ { n + 1 } )$ and

$\lambda _ { n }$ with $\boldsymbol { \mu } _ { n }$ , we obtain

$$
\begin{array} { c } { { p _ { n + 1 / 2 } = p _ { n + 1 } + \displaystyle \frac { h } { 2 } \Big ( H _ { q } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) + G ^ { T } ( q _ { n + 1 } ) \mu _ { n } \Big ) } } \\ { { q _ { n } = q _ { n + 1 } - \displaystyle \frac { h } { 2 } \Big ( H _ { p } ( p _ { n + 1 / 2 } , q _ { n + 1 } ) + H _ { p } ( p _ { n + 1 / 2 } , q _ { n } ) \Big ) } } \\ { { g ( q _ { n } ) = g ( q _ { n + 1 } ) - h G ( q _ { n + 1 } ) H _ { p } ( p _ { n + 1 } , q _ { n + 1 } ) } } \\ { { p _ { n } = p _ { n + 1 / 2 } + \displaystyle \frac { h } { 2 } \Big ( H _ { q } ( p _ { n + 1 / 2 } , q _ { n } ) + G ^ { T } ( q _ { n } ) \lambda _ { n } \Big ) } } \\ { { \vdots ( q _ { n } ) H _ { p } ( p _ { n } , q _ { n } ) = G ( q _ { n + 1 } ) H _ { p } ( p _ { n + 1 } , q _ { n + 1 } ) . } } \end{array}
$$

These are exactly the same equations as those of (8.19a,b,d) and (8,9), proving that even the extension of the method to a neighbourhood of $\mathcal { M }$ is symmetric.

b) We consider the method (8.19) as a mapping $( p _ { n } , q _ { n } ) \mapsto ( p _ { n + 1 } , q _ { n + 1 } )$ on the manifold $\mathcal { M }$ of Eq. (8.5). The same considerations as for (8.8) show that (8.19) is a method of order at least one. Since it is symmetric, its order has to be even (Sect.II.8). This proves that (8.19) is a convergent method of order 2.

c) The fact that the method (8.19) defines a symplectic transformation on $M$ can be proved as for (8.8) (see Leimkuhler & Skeel (1994) for the case of a separable Hamiltonian (8.16)). We do not give details here, because the symplecticity of (8.19) also follows from Theorem 8.5 below. □

Remark 8.3. In a step by step application of method (8.19) the projection (8.19d,e) can be avoided at those points, where the value $p _ { n + 1 }$ is not needed for output. Indeed,from the second step on we can replace (8.19a) by

$p _ { n + 1 / 2 } = p _ { n - 1 / 2 } - \frac { h } { 2 } \left( H _ { q } ( p _ { n + 1 / 2 } , q _ { n } ) + H _ { q } ( p _ { n - 1 / 2 } , q _ { n } ) + G ^ { T } ( q _ { n } ) ( \lambda _ { n } + \mu _ { n - 1 } ) \right)$ without changing the numerical approximations $q _ { n }$ and $\mathcal { P } _ { n + 1 / 2 }$ . The same trick is possible for method (8.8).

# The Lobatto IIIA-IIIB Pair

Partitioned Runge-Kutta methods are well suited for unconstrained Hamiltonian systems (see Sect.II.16). We shall investigate here, how these methods can be extended to the constrained system (8.1). We consider

$$
\begin{array}{c} \begin{array} { l } { { \displaystyle { P _ { \imath } = p _ { 0 } + h \sum _ { \imath = 1 } ^ { s } a _ { \imath \jmath } k _ { \jmath } } , ~ } } \\ { { ~ } } \\ { { \displaystyle p _ { 1 } = p _ { 0 } + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } k _ { \imath } , ~ } } \\ { { ~ } } \\ { { \displaystyle k _ { \imath } = - \frac { \partial H } { \partial q } ( P _ { \imath } , Q _ { \imath } ) - G ^ { T } ( Q _ { \imath } ) \Lambda _ { \imath } , ~ } } \end{array} \ q _ { \imath } = q _ { 0 } + h \sum _ { \imath = 1 } ^ { s } \widehat { a } _ { \imath } \ell _ { \jmath } ,   \end{array}
$$

where $b _ { \imath } , a _ { \imath \jmath }$ and $\widehat { b } _ { \iota } , \widehat { a } _ { \iota \jmath }$ are the coeficients of two Runge-Kutta schemes (c.f., Eq.(II.16.26)). For the moment,the values $\Lambda _ { \imath }$ $( i = 1 , \ldots , s )$ are not yet specified. There are several possibilities to do this. One can either define them by $\Lambda _ { \imath } =$ $\lambda ( P _ { \imath } , Q _ { \imath } )$ ，where $\lambda ( p , q )$ is the function given by (8.3b),or one can define them implicitly by adding the conditions $G ( Q _ { \imath } ) H _ { p } ( P _ { \imath } , Q _ { \imath } ) = 0$ or $g ( Q _ { \imath } ) = 0$

We are interested in symplectic schemes. Therefore it is natural to consider methods satisfying the conditions of Theorem II.16.10.

Lemma 8.4. If the coefficients of (8.20) satisfy

$$
\begin{array} { r l } & { \boldsymbol { b } _ { \iota } = \widehat { \boldsymbol { b } } _ { \iota } , \qquad i = 1 , \dots , s } \\ & { \boldsymbol { b } _ { \iota } \widehat { \boldsymbol { a } } _ { \iota \ j } + \widehat { \boldsymbol { b } } _ { \jmath } \boldsymbol { a } _ { \jmath \iota } - \boldsymbol { b } _ { \iota } \widehat { \boldsymbol { b } } _ { \jmath } = 0 , \qquad i , j = 1 , \dots , s , } \end{array}
$$

then we have the following relation for the expressions in (8.20):

$$
\sum _ { l = 1 } ^ { n } d p _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } - \sum _ { I = 1 } ^ { n } d p _ { 0 } ^ { I } \wedge d q _ { 0 } ^ { I } = h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \sum _ { K = 1 } ^ { m } \Big ( \sum _ { I = 1 } ^ { n } \frac { \partial g ^ { K } } { \partial q ^ { I } } ( Q _ { \iota } ) d Q _ { \iota } ^ { I } \Big ) \wedge d \Lambda _ { \iota } ^ { K } .
$$

If the Hamiltonian is separable $( i . e . , \ H ( p , q ) = T ( p ) + U ( q ) )$ ， then the condition (8.22) alone implies the above relation.

Proof. We compute the expression $\begin{array} { r } { D = \sum _ { I } d p _ { 1 } ^ { I } \wedge d q _ { 1 } ^ { I } - \sum _ { I } d p _ { 0 } ^ { I } \wedge d q _ { 0 } ^ { I } } \end{array}$ following the lines of the proof of Theorem II.16.6 (see also the proof of Theorem II.16.10). All terms cancel with exception of those originating from the presence of $G ^ { T } ( Q _ { \imath } ) \Lambda _ { \imath }$ in (8.20c). We thus obtain

$$
D = - h \sum _ { \iota = 1 } ^ { \boldsymbol { s } } b _ { \iota } \sum _ { K = 1 } ^ { m } \Bigl ( \Lambda _ { \iota } ^ { K } \sum _ { I , J = 1 } ^ { n } \frac { \partial ^ { 2 } g ^ { K } } { \partial q ^ { J } \partial q ^ { I } } ( Q _ { \iota } ) d Q _ { \iota } ^ { J } \wedge d Q _ { \iota } ^ { I } + \sum _ { I = 1 } ^ { n } \frac { \partial g ^ { K } } { \partial q ^ { I } } ( Q _ { \iota } ) d \Lambda _ { \iota } ^ { K } \wedge d Q _ { \iota } ^ { I } \Bigr ) .
$$

Due to the symmetry of the second derivative of $g ^ { K }$ the term involving $d Q _ { \imath } ^ { J } \wedge d Q _ { \imath } ^ { I }$ vanishes identically. This proves the statement of the lemma. □

We are interested in partitioned Runge-Kuta methods that satisfy:

. the numerical solution stays on the manifold $\mathcal { M }$ of Eq. (8.5);   
. the numerical flow $( p _ { 0 } , q _ { 0 } ) \mapsto ( p _ { 1 } , q _ { 1 } )$ is a symplectic transformation on $\mathcal { M }$ ； the order of convergence is higher than 2. If the values $\Lambda _ { \iota }$ are determined by the condition

$$
g ( Q _ { \ i } ) = 0 \qquad \mathrm { f o r } \quad i = 1 , \ldots , s ,
$$

then we have $\textstyle \sum _ { I } \partial g ^ { K } / \partial q ^ { I } ( Q _ { \iota } ) d Q _ { \iota } ^ { I } = 0$ , and it follows from Lemma 8.4 that the method (8.20) is symplectic,if (8.21) and (8.22) are satisfied. Hence, the second item holds. Here we see the importance of the conditions (8.23). Solving the index reduced system (8.1a,b),(8.3b) by a symplectic method would in general not result in a symplectic numerical flow on $\mathcal { M }$

How can we achieve the first item, in particular the condition $g ( q _ { 1 } ) = 0 \colon$ The idea is to require the method $\widehat { b } _ { \iota } , \widehat { a } _ { \iota \jmath }$ to be stifly accurate,i.e.,

$$
\widehat { a } _ { s _ { 3 } } = \widehat { b } _ { \jmath } \qquad \mathrm { f o r } \quad \jmath = 1 , \dots , s .
$$

In this case we have $q _ { 1 } = Q _ { s }$ ,and $g ( q _ { 1 } ) = 0$ is automatically satisfied by (8.23). The condition (8.24) together with (8.22) implies that (assuming nonzero $\widehat { b } _ { \iota }$ ）

$$
a _ { \imath s } = 0 \qquad \mathrm { f o r } \quad i = 1 , \ldots , s ,
$$

and the nonlinear system (8.20a,c),(8.23) no longer depends on $\Lambda _ { s }$ . This parameter, however, appears in the definition of $p _ { 1 }$ in Eq.(8.20b) via $k _ { s }$ . There it can be used to impose the constraint $G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) = 0$

Due to the condition (8.25) a new difficulty arises. If we consider $_ { ( 8 . 2 0 \mathbf { b } , \mathbf { c } ) }$ as definition of the quantities $p _ { 1 } , q _ { 1 } , k _ { \imath } , \ell _ { \imath }$ ，the remaining equations (8.2Oa) and (8.23)are a nonlinearsystemfor $P _ { 1 } , \dots , P _ { s } , Q _ { 1 } , \dots , Q _ { s } , \Lambda _ { 1 } , \dots , \Lambda _ { s - 1 }$ . Counting the number of equations of this system $( 2 s n + s m )$ and the number of unknowns $( 2 s n + ( s - 1 ) m )$ , one is readily convinced that this nonlinear system will usually not have a solution. The idea (Jay 1994,1996) is to require

$$
\widehat { a } _ { 1 \ j } = 0 \qquad \mathrm { f o r } \quad j = 1 , \ldots , s ,
$$

so that $Q _ { 1 } = q _ { 0 }$ ,and the condition (8.23) is automatically verified for $i \simeq 1$ (we always assume consistent initial values). By (8.22) this implies (for nonzero $\widehat { b } _ { \iota }$ ）

$$
a _ { \imath 1 } = b _ { 1 } \qquad \mathrm { f o r } \quad i = 1 , \ldots , s .
$$

The Runge-Kutta matrices $\widehat { A }$ and $A$ are both singular. Let $\widehat { A } _ { 0 }$ be the $( s - 1 ) \times s$ submatrix of $\widehat { A }$ obtained by deleting its first row,and let $A _ { 0 }$ be the $s \times ( s - 1 )$ submatrix of $A$ formed by the first $s - 1$ columns of $A$ ． In order to be able to prove the existence of a numerical solution of (8.2O), (8.23),we require that the $( s - 1 ) \times ( s - 1 )$ matrix

$$
{ \widehat { A } } _ { 0 } A _ { 0 } \qquad { \mathrm { i s ~ i n v e r t i b l e . } }
$$

We now extend the method to arbitrary initial values as follows: we replace condition (8.23) by

$$
g ( Q _ { \ i } ) = g ( q _ { 0 } ) + { \widehat c } _ { \ i } h G ( q _ { 0 } ) H _ { p } ( p _ { 0 } , q _ { 0 } ) \qquad \mathrm { f o r } \quad i = 1 , \dots , s ,
$$

$\begin{array} { r } { ( \widehat { c } _ { \iota } = \sum _ { \ j } \widehat { a } _ { \iota \ j } ) } \end{array}$ and the condition $G ( q _ { 1 } ) H _ { p } ( p _ { 1 } , q _ { 1 } ) = 0$ by (8.9b). Similar to Equation (8.10) we use

$$
g ( Q _ { \imath } ) - g ( q _ { 0 } ) = h \int _ { 0 } ^ { 1 } g _ { q } \big ( q _ { 0 } + \tau ( Q _ { \imath } - q _ { 0 } ) \big ) d \tau \cdot \sum _ { \jmath = 1 } ^ { s } \widehat { a } _ { \imath _ { \jmath } } H _ { p } ( P _ { \jmath } , Q _ { \jmath } ) .
$$

Then we develop

$$
\begin{array} { l } { { \displaystyle H _ { p } ( P _ { \jmath } , Q _ { \jmath } ) = H _ { p } ( p _ { 0 } , Q _ { \jmath } ) } } \\ { { \displaystyle - \ h \int _ { 0 } ^ { 1 } H _ { p p } \big ( p _ { 0 } + \sigma ( P _ { \jmath } - p _ { 0 } ) , Q _ { \jmath } \big ) d \sigma \cdot \sum _ { r = 1 } ^ { s - 1 } a _ { \jmath r } \big ( H _ { q } ( P _ { r } , Q _ { r } ) + G ^ { T } ( Q _ { r } ) \Lambda _ { r } \big ) , } } \end{array}
$$

and insert this relation into (8.29). As in Eq.(8.11) we get a linear system for $\Lambda _ { 1 } , \ldots , \Lambda _ { s - 1 }$ which, for $h = 0$ , has the solution $\Lambda _ { r } ^ { 0 }$ given by

$$
\begin{array} { l } { { \displaystyle 0 = \frac { \widehat c _ { _ 1 } ^ { 2 } } { 2 } g _ { q q } ( H _ { p } , H _ { p } ) + \biggl ( \sum _ { j = 1 } ^ { s } \widehat a _ { \iota _ { j } } \widehat c _ { _ { j } } \biggr ) G H _ { p q } H _ { p } } } \\ { { \displaystyle - \sum _ { r = 1 } ^ { s - 1 } \biggl ( \sum _ { j = 1 } ^ { s } \widehat a _ { \iota _ { j } } a _ { \jmath r } \biggr ) G H _ { p p } \bigl ( H _ { q } + G ^ { T } \Lambda _ { r } ^ { 0 } \bigr ) } . } \end{array}
$$

Here all functions are evaluated at $( p _ { 0 } , q _ { 0 } )$ . Due to (8.28) and (8.4) this system can be solved for $\Lambda _ { r } ^ { 0 }$ . The Implicit Function Theorem then guarantees the existence of a locally unique solution of the method (8.20), (8.23),and the existence of a smooth extension to a neighbourhood of $\ M$

The question is now: do there exist high order methods having al these properties?

Theorem 8.5. The $s$ -stage Lobatto IIIA-IIB pair (Lobatto IIIA in the role of $\widehat { b } _ { \iota } , \widehat { a } _ { \iota \jmath }$ ， and Lobatto IIIB in the role of $b _ { \imath } , a _ { \imath \jmath }$ ; see Sect. IV.5 for their definition) satisfies (8.21), (8.22), (8.24), (8.25),(8.26),(8.27), and (8.28).

Proof. Properties (8.21),(8.24),(8.25),(8.26),and (8.27) follow immediately from the definition of the methods. The symplecticity condition (8.22） has first been proved by Sun Geng (1993). We let $d _ { \iota \ j } = b _ { \iota } \widehat { a } _ { \iota \ j } + \widehat { b } _ { \jmath } a _ { \jmath \iota } - b _ { \iota } \widehat { b } _ { \jmath }$ and compute for $k = 1 , \hdots , s$

$$
\sum _ { \jmath = 1 } ^ { s } d _ { \imath \jmath } c _ { \jmath } ^ { k - 1 } = b _ { \imath } \frac { c _ { \imath } ^ { k } } { k } + \frac { b _ { \imath } } { k } ( 1 - c _ { \imath } ^ { k } ) - b _ { \imath } \frac { 1 } { k } = 0 .
$$

Here we have exploited the fact that the Lobatto IIIA method satisfies $C ( s )$ and the Lobatto IIIB method satisfies $D ( s )$ (see Table IV.5.13). Since the abscissae $c _ { 1 } , \ldots , c _ { s }$ of the Lobato quadrature are distinct, the above Vandermonde type sys-tem has a unique solution $d _ { \imath j } = 0$ . This proves (8.22).

We next show that

$$
\sum _ { k = 1 } ^ { s - 1 } \Bigl ( \sum _ { j = 1 } ^ { s } \widehat { a } _ { \iota _ { j } } a _ { \jmath _ { k } } \Bigr ) c _ { k } ^ { q - 2 } = \frac { c _ { \iota } ^ { q } } { q ( q - 1 ) } \qquad \mathrm { f o r } i , q = 2 , \ldots , s .
$$

This means that $\widehat { A } _ { 0 } A _ { 0 } V = W$ ，where $V$ and $W$ are nonsingular Vandermonde type matrices. This obviously implies (8.28). For $q = 2 , \ldots , s - 1$ Eq. (8.30) fol-lows from the fact that the methods Lobatto IIIA and IIB satisfy $C ( s )$ and $C ( s -$ 2)espetiels $\begin{array} { r } { \delta _ { \iota } : = \sum _ { k } \sum _ { \jmath } \widehat { a } _ { \iota \jmath } a _ { \jmath k } c _ { k } ^ { s - 2 } - } \end{array}$ $c _ { \iota } ^ { s } / s ( s - 1 )$ vanish for all $i$ . By (8.26) and $c _ { 1 } = 0$ we have $\delta _ { 1 } = 0$ . Because of $\widehat { a } _ { s \jmath } = \widehat { b } _ { \jmath } = b _ { \jmath }$ and $c _ { s } = 1$ , the condition $\delta _ { s } = 0$ is nothing else than an order condition (order $s$ ),which is satisfied (Sect.IV.5). Since the Lobatto IIIA and IIIB methods satisfy $D ( s - 2 )$ and $D ( s )$ ， respectively, it holds $\begin{array} { r } { \sum _ { \ i } b _ { \ i } c _ { \ i } ^ { m - 1 } \delta _ { \ i } = 0 } \end{array}$ for $m = 1 , \ldots , s - 2$ . This proves that also $\delta _ { 2 } , \ldots , \delta _ { s - 1 }$ vanish, so that all relations of (8.30) are established. □

It still remains to discuss the order of convergence of the Lobato IIA-IIB pair. Since we have succeeded in embedding the method into a one-step method that is defined in a whole neighbourhood of $\mathcal { M }$ , the convergence theory of Sect.II.3 can be applied. We only have to investigate the local error of the method. Each of the methods has classical order $2 s - 2$ (Sect.IV.5),and it follows from Exercise 4 that, considered as partitioned Runge-Kutta method, the pair has also order $2 s - 2$ . It has been shown in Jay (1994) that the presence of constraints (8.1c) does not reduce the order. The proof of this superconvergence result is very technical and long. Therefore we do not reproduce it here.

# Composition Methods

Another possibility for obtaining high order symplectic methods for the system (8.1） is by composition of low order methods. The idea goes back to Yoshida (1990),and has been extended to constrained systems by Reich (1996).

Consider the second order symmetric method (8.19) and denote its extension to a neighbourhood of $\mathcal { M }$ by $\Phi _ { h }$ . We shall study the following composition

$$
\Phi _ { c _ { 1 } h } \circ \Phi _ { c _ { 2 } h } \circ \Phi _ { c _ { 1 } h } .
$$

The method (8.31） represents a one-step method, defined in a neighbourhood of $\mathcal { M }$ ．For initial values on $\mathcal { M }$ ，the numerical solution stays on $M$ .Moreover, the composition (8.31) is symplectic and symmetric. Observe that the projections (8.19d,e) can be avoided in an implementation of this method (see Remark 8.3). Concerning its order we have the following result.

Theorem 8.6. Let $\Phi _ { h }$ be the mapping $( p _ { 0 } , q _ { 0 } ) \mapsto ( p _ { 1 } , q _ { 1 } )$ ,defined by (8.19). If

$$
2 c _ { 1 } + c _ { 2 } = 1 , \qquad 2 c _ { 1 } ^ { 3 } + c _ { 2 } ^ { 3 } = 0 ,
$$

the composition method (8.31) is of order 4.

1f $\Phi _ { h }$ represents a one-step method that is symmetric, of order $p = 2 k$ ，and defined in a neighbourhood of $\mathcal { M }$ , then the relations

$$
2 c _ { 1 } + c _ { 2 } = 1 , \qquad 2 c _ { 1 } ^ { p + 1 } + c _ { 2 } ^ { p + 1 } = 0 ,
$$

imply that the composition (8.31) is of order $p + 2$

Proof. We let $y _ { 0 } = ( p _ { 0 } , q _ { 0 } ) ^ { T }$ and $y ( t ) = \left( p ( t ) , q ( t ) \right) ^ { T }$ . The local error of the method (8.19) satisfies

$$
y ( t _ { 0 } + h ) - \Phi _ { h } ( y _ { 0 } ) = d ( y _ { 0 } ) h ^ { 3 } + \mathcal { O } ( h ^ { 4 } ) .
$$

Since the basic method is of the form $\Phi _ { h } ( y _ { 0 } ) = y _ { 0 } + h \Psi ( y _ { 0 } , h )$ , we have that

$$
y \big ( t _ { 0 } + ( 2 c _ { 1 } + c _ { 2 } ) h \big ) - \Phi _ { c _ { 1 } h } \circ \Phi _ { c _ { 2 } h } \circ \Phi _ { c _ { 1 } h } ( y _ { 0 } ) = ( 2 c _ { 1 } ^ { 3 } + c _ { 2 } ^ { 3 } ) d ( y _ { 0 } ) h ^ { 3 } + \mathcal { O } ( h ^ { 4 } ) .
$$

The conditions (8.32) then imply that the method (8.31) is at least of order 3. Since it is symmetric, it has to be of order 4. The proof is easily adapted to the higher order situation. □

A solution of (8.32) is given by

$$
c _ { 1 } = { \frac { 1 } { 2 - \sqrt [ 3 ] { 2 } } } , \qquad c _ { 2 } = - { \frac { \sqrt [ 3 ] { 2 } } { 2 - \sqrt [ 3 ] { 2 } } } ,
$$

which shows that the intermediate step in the composition (8.31) is a ‘back step' (negative step size $c _ { 2 } h$ ).

The result of Theorem 8.6 allows us to construct symplectic integrators for (8.1)of an arbitrary even order. However, the resulting method of order $p = 2 k$ requires $3 ^ { k - 1 }$ applications of the basic method (8.19).

In the case of unconstrained Hamiltonian systems it is known that better methods can be obtained by compositions of the form

$$
\Phi _ { c _ { 1 } h } \circ \Phi _ { c _ { 2 } h } \circ . . . \circ \Phi _ { c _ { s - 1 } h } \circ \Phi _ { c _ { s } h } \circ \Phi _ { c _ { s - 1 } h } \circ . . . \circ \Phi _ { c _ { 2 } h } \circ \Phi _ { c _ { 1 } h }
$$

(see Yoshida 1990,McLachlan 1995,Sanz-Serna & Calvo 1994)． Reich (1996) studies the extension of these methods to constrained Hamiltonian systems and finds that additional order conditions are necessary. His investigation relies on a “backward error analysis” for integrators on manifolds.

# Backward Error Analysis (for ODEs)

Although backward analysis is a perfectly straightforward concept there is strong evidence that a training in classical mathema-tics leaves one unprepared to adopt it.

(J.H. Wilkinson, NAG Newsletter 2/85)

In Sect.II.16 we have briefly explained the idea of backward error analysis for the symplectic Euler method. Here we present an extension to general one-step methods for ordinary differential equations. Consider

$$
y ^ { \prime } = f ( y ) , \qquad y ( 0 ) = y _ { 0 } ,
$$

and let $y _ { 0 } \mapsto y _ { 1 }$ be an arbitrary one-step method for (8.35). We assume that $f ( y )$ and the method are sufficiently often differentiable,so that the local error can be expanded into a Taylor series as

$$
y _ { 1 } - y ( h ) = d _ { p + 1 } ( y _ { 0 } ) h ^ { p + 1 } + \ldots + d _ { N } ( y _ { 0 } ) h ^ { N } + { \mathcal { O } } ( h ^ { N + 1 } ) .
$$

Theorem 8.7. Consider a one-step method of order $p$ , and assume the local error to be given by (8.36). Then there exist functions $f _ { \boldsymbol { \jmath } } ( \boldsymbol { y } )$ $( f o r ~ j = p , \dots , N )$ ，such that

$$
y _ { 1 } - \widetilde { y } ( h ) = \mathcal { O } ( h ^ { N + 1 } ) ,
$$

where $\widetilde { y } ( t )$ is the solution of the perturbed differential equation

$$
\widetilde { y } ^ { \prime } = f ( \widetilde { y } ) + h ^ { p } f _ { p } ( \widetilde { y } ) + \ldots + h ^ { N - 1 } f _ { N - 1 } ( \widetilde { y } ) , \qquad \widetilde { y } ( 0 ) = y _ { 0 } ,
$$

Remark. If the function $f ( y ) + h ^ { p } f _ { p } ( y ) + \ldots + h ^ { N - 1 } f _ { N - 1 } ( y )$ satisfies a Lipschitz condition, the proof of Theorem I.3.4 shows that $y _ { n } - \widetilde { y } ( n h ) = \mathcal { O } ( h ^ { N } )$ on bounded intervals. This implies that the numerical approximation $y _ { n }$ is much closer to the solution of(8.38) than to that of (8.35). Hence,the study of the system (8.38) yields new insight into the behaviour of the numerical solution.

Proof. As a consequence of the nonlinear variation-of-constants formula (Theorem I.14.5) we have

$$
\widetilde { y } ( h ) = y ( h ) + \int _ { 0 } ^ { h } \frac { \partial y } { \partial y _ { 0 } } \big ( h , s , \widetilde { y } ( s ) \big ) \cdot \Big ( h ^ { p } f _ { p } \big ( \widetilde { y } ( s ) \big ) + . . . + h ^ { N } f _ { N } \big ( \widetilde { y } ( s ) \big ) \Big ) d s ,
$$

where $y ( t , t _ { 0 } , y _ { 0 } )$ denotes the solution of (8.35） corresponding to initial values $y ( t _ { 0 } ) = y _ { 0 }$ . Expanding the above integral into a Taylor series we obtain

$$
\widetilde { y } ( h ) - y ( h ) = h ^ { p + 1 } f _ { p } ( y _ { 0 } ) + h ^ { p + 2 } \Big ( f _ { p + 1 } + \frac { 1 } { 2 } f _ { p } ^ { \prime } f + \frac { 1 } { 2 } f ^ { \prime } f _ { p } \Big ) ( y _ { 0 } ) + \ldots .
$$

The condition (8.37) implies that the coeffcients of (8.39) have to agree with those of (8.36) up to a certain order. We thus get $f _ { p } ( y ) = d _ { p + 1 } ( y ) , f _ { p + 1 } ( y ) = d _ { p + 2 } ( y ) -$ $\left( f _ { p } ^ { \prime } ( y ) f ( y ) + f ^ { \prime } ( y ) f _ { p } ( y ) \right) / 2$ , etc. The essential observation is that the coefficient of $h ^ { j + 1 }$ in (8.39) contains $f _ { \boldsymbol { \jmath } } ( \boldsymbol { y } )$ as linear term and further expressions that only depend on $f _ { \imath } ( \boldsymbol { y } )$ with $i < j$ . Hence, the functions $f _ { \boldsymbol { \jmath } } ( \boldsymbol { y } )$ are recursively determined by the above comparison. □

Example 8.8. For an illustration of the above theorem we consider the Volterra-Lotka differential equation

$$
u ^ { \prime } = u ( v - 1 ) , \qquad v ^ { \prime } = v ( 2 - u ) .
$$

This system possesses the first integral

$$
I ( u , v ) = 2 \ln u - u + \ln v - v ,
$$

implying that the solutions are all periodic. Some of them are plotted in the left upper picture of Fig.8.1.

We apply three different numerical methods to this differential equation. The first one is the well-known explicit Euler method $y _ { n + 1 } = y _ { n } + h f ( y _ { n } )$ . The right upper picture of Fig.8.1 shows the numerical solution and the exact solution (solid

![](images/4128e888c699c9dbe2616e1a8e79db12d45419090ad506f23d043a021308ce21.jpg)  
Fig.8.1. Solutions of the perturbed differential equation for various methods

line） for the initial value $u _ { 0 } = 2 . 7 2 5$ ， $v _ { 0 } = 1$ . Moreover, we have included the solutions of the perturbed differential equation (8.38) for $N \simeq 1$ (dashed-dotted line) and for $N \approx 2$ (dotted line). For the explicit Euler method,Eq.(8.38) reads

$$
\widetilde { y } ^ { \prime } = f ( \widetilde { y } ) - \frac { h } { 2 } \big ( f ^ { \prime } f \big ) ( \widetilde { y } ) + \frac { h ^ { 2 } } { 1 2 } \big ( f ^ { \prime \prime } ( f , f ) + 4 f ^ { \prime } f ^ { \prime } f \big ) ( \widetilde { y } ) .
$$

We nicely observe the good agreement of the numerical solution with the exact solution of the perturbed system, even for the rather large step size $h = 0 . 1 2$

The left lower picture shows the same experiment for the implicit Euler method $y _ { n + 1 } = y _ { n } + h f ( y _ { n + 1 } )$ . The perturbed differential equation is obtained from(8.42) by replacing $h$ by $- h$ (this is, because the explicit Euler method is the adjoint method of the implicit Euler method).

The third method is the symplectic Euler method (see Eq.(8.45) below), which for the problem (8.40) is defined by

$$
u _ { n + 1 } = u _ { n } + h u _ { n } ( v _ { n + 1 } - 1 ) , \qquad v _ { n + 1 } = v _ { n } + h v _ { n + 1 } ( 2 - u _ { n } ) .
$$

The first term of the perturbed differential equation is

$$
\begin{array} { c } { { \widetilde { u } ^ { \prime } = \widetilde { u } ( \widetilde { v } - 1 ) - h \widetilde { u } ( \widetilde { u } \widetilde { v } - 4 \widetilde { v } + \widetilde { v } ^ { 2 } + 1 ) / 2 } } \\ { { \widetilde { v } ^ { \prime } = \widetilde { v } ( 2 - \widetilde { u } ) + h \widetilde { v } ( \widetilde { u } \widetilde { v } - 5 \widetilde { u } + \widetilde { u } ^ { 2 } + 4 ) / 2 . } } \end{array}
$$

The qualitative behaviour of this method is quite different from that of the previous methods. One can prove that the system (8.43) has a first integral close to $I ( u , v )$ (Exercise 5). Hence the solutions are periodic,as it is the case for the original unperturbed system.

Example 8.9. For the Hamiltonian system (without constraints)

$$
q ^ { \prime } = H _ { p } ( p , q ) , \qquad p ^ { \prime } = - H _ { q } ( p , q )
$$

the method (8.8) becomes

$$
\begin{array} { r } { q _ { 1 } = q _ { 0 } + h H _ { p } ( p _ { 1 } , q _ { 0 } ) , \qquad p _ { 1 } = p _ { 0 } - h H _ { q } ( p _ { 1 } , q _ { 0 } ) . } \end{array}
$$

A similar method (implicit in $q$ and explicit in $p$ ) has been considered in Sect. II.16, Formula (II.16.54). There we have computed the first terms of the perturbed differential equation (8.38),and we have noticed with surprise that it is also Hamiltonian. The same computation can be done here. We find that the perturbed differential equation for (8.45) is of the form

$$
\widetilde { q } ^ { \prime } = \widetilde { H } _ { p } ( \widetilde { p } , \widetilde { q } ) , \qquad \widetilde { p } ^ { \prime } = - \widetilde { H } _ { q } ( \widetilde { p } , \widetilde { q } )
$$

with (for $N \Leftarrow 2$ ）

$$
\widetilde { H } = H - \frac { h } { 2 } H _ { p } H _ { q } + \frac { \hbar ^ { 2 } } { 1 2 } \Big ( H _ { p p } H _ { q } ^ { 2 } + H _ { q q } H _ { p } ^ { 2 } + 4 H _ { p q } H _ { p } H _ { q } \Big ) .
$$

For notational convenience we have assumed that $p$ and $q$ are scalars. However, with a suitable interpretation of the appearing expressions, the formula is also valid for problems with more than one degree of freedom.

Example 8.10. The second order method (8.19), when applied to the unconstrained system (8.44),becomes

$$
\begin{array} { l } { { q _ { 1 } = q _ { 0 } + { \displaystyle \frac { h } { 2 } } \Big ( H _ { p } ( p _ { 1 / 2 } , q _ { 0 } ) + H _ { p } ( p _ { 1 / 2 } , q _ { 1 } ) \Big ) } } \\ { { p _ { 1 } = p _ { 0 } - { \displaystyle \frac { h } { 2 } } \Big ( H _ { q } ( p _ { 1 / 2 } , q _ { 0 } ) + H _ { q } ( p _ { 1 / 2 } , q _ { 1 } ) \Big ) , } } \end{array}
$$

where $p _ { 1 / 2 } = p _ { 0 } - ( h / 2 ) H _ { q } ( p _ { 1 / 2 } , q _ { 0 } )$ . Computing the dominant term of its local error, we see that the perturbed differential equation (8.38) is, for $N \approx 2$ ， given by

$$
\begin{array} { r l r } {  { \widetilde { q } ^ { \prime } = H _ { p } ( \widetilde { p } , \widetilde { q } ) + \frac { \hbar ^ { 2 } } { 2 4 } \Bigl ( - H _ { p p p } H _ { q } ^ { 2 } + 2 H _ { p p q } H _ { p } H _ { q } + 2 H _ { p q q } H _ { p } ^ { 2 } } } \\ & { } & { + \ 2 H _ { p q } H _ { p q } H _ { p } + 4 H _ { p p } H _ { q q } H _ { p } \Bigr ) ( \widetilde { p } , \widetilde { q } ) } \\ & { } & { \widetilde { p } ^ { \prime } = - H _ { q } ( \widetilde { p } , \widetilde { q } ) + \frac { \hbar ^ { 2 } } { 2 4 } \Bigl ( H _ { p p q } H _ { q } ^ { 2 } - 2 H _ { p q q } H _ { p } H _ { q } - 2 H _ { q q q } H _ { p } ^ { 2 } } \\ & { } & { - \ 2 H _ { p q } H _ { p q } H _ { q } + 2 H _ { p p } H _ { q q } H _ { q } - 6 H _ { p q } H _ { q q } H _ { p } \Bigr ) ( \widetilde { p } , \widetilde { q } ) . } \end{array}
$$

One easily verifies that this is a Hamiltonian system (8.46) with

$$
\widetilde { H } = H + \frac { \hbar ^ { 2 } } { 2 4 } \Bigl ( 2 H _ { q q } H _ { p } ^ { 2 } - H _ { p p } H _ { q } ^ { 2 } + 2 H _ { p q } H _ { p } H _ { q } \Bigr ) .
$$

A Short Survey on Further Results. A further elaboration of backward error analysis for ordinary differential equations would take us beyond the scope of this chapter. We therefore collect some interesting results without going into details.

First of all, the mystery of the foregoing examples is well understood. In the situation, where the differential equation (8.35) is a Hamiltonian system, and where a symplectic integration method is applied, the perturbed system (8.38) is again Hamiltonian for all $N$ . This result is proved by Hairer (1994),where explicit formulas for the functions $f _ { \boldsymbol { \jmath } } ( \boldsymbol { y } )$ in terms of elementary differentials are provided, and where an explicit formula for the perturbed Hamiltonian is given. This explicit rep-resentation guarantees that $\widetilde { \cal H } ( p , q )$ is uniquely defined on regions where $H ( p , q )$ is defined.Different proofs of this result can be found in Reich (1996) and Benettin & Giorgilli (1994).

If the function $f$ in (8.35) is infinitely differentiable, then the truncation index $N$ in Theorem 8.7 is arbitrary. In general, the series (8.38) diverges as $N  \infty$ and the constants hidden in the $\mathcal { O } ( h ^ { N + 1 } )$ bounds of (8.37) tend to infinity with $N$ ，even if $f$ is analytic. Therefore, it is interesting to find rigorous bounds on $y _ { 1 } - \widetilde { y } ( h )$ for an optimally chosen $N$ . Such results have been found independently by Benettin & Giorgilli(1994) and Hairer & Lubich (1996).As a consequence,one can show that for symplectic integrations the Hamiltonian remains bounded (with error of size $\mathcal { O } ( h ^ { p } ) ,$ over exponentially long times.Moreover, KAM theory can be applied to get more insight into the long-time behaviour of symplectic numerical schemes.

# Backward Error Analysis on Manifolds

Consider the constrained Hamiltonian system (8.1)，and a numerical one-step method which yields approximations $\left( p _ { n } , q _ { n } \right)$ staying on the manifold $\mathcal { M }$ of Eq.(8.5). Can we extend the above backward error analysis for ODEs to this situation?

There are at least two ways to achieve this goal. The first one is to introduce local coordinates in order to obtain an unconstrained Hamiltonian system. The backward analysis for ODEs can then be applied to the one-step method written in local coordinates.

The second approach allows us to construct the perturbed Hamiltonian directly in the original coordinates. For the special case of separable Hamiltonians,this approach is due to Reich (1996). We shall explain it for the first and second order methods (8.8) and (8.19).

Backward Error Analysis for the Method (8.8). Consider first the subsystem $\left( 8 . 8 { \sf a - c } \right)$ . The projection step (8.8d,e) will be treated later. In Eq.(8.11) the value $\lambda _ { 1 }$ has been expressed in terms of $\widehat { p } _ { 1 } , q _ { 1 } , p _ { 0 } , q _ { 0 }$ , even for inconsistent initial values. Inserting this function into (8.8a), the Eqs.(8.8a,b) represent two relations between the variable $\widehat { p } _ { 1 } , q _ { 1 } , p _ { 0 } , q _ { 0 }$ ，and $h$ ．By the Implicit Function Theorem these two relations allow us to express $\left( p _ { 0 } , q _ { 1 } \right)$ in terms of $( \widehat { p } _ { 1 } , q _ { 0 } )$ ,and $h$ . Consequently, the solution $\lambda _ { 1 }$ of Eq. (8.11) can be written as a function of $\left( \widehat { p } _ { 1 } , q _ { 0 } , h \right)$ . We denote it by

$$
\lambda _ { 1 } = \lambda ( \widehat { p } _ { 1 } , q _ { 0 } , h ) ,
$$

so that the system (8.8a,b) becomes

$$
\begin{array} { r l } & { \widehat { p } _ { 1 } = p _ { 0 } - h \big ( H _ { q } ( \widehat { p } _ { 1 } , q _ { 0 } ) + G ^ { T } ( q _ { 0 } ) \lambda ( \widehat { p } _ { 1 } , q _ { 0 } , h ) \big ) } \\ & { q _ { 1 } = q _ { 0 } + h H _ { p } ( \widehat { p } _ { 1 } , q _ { 0 } ) , } \end{array}
$$

and the constraint (8.9a) is automatically satisfied by the definition of $\lambda ( \widehat { p } _ { 1 } , q _ { 0 } , h )$ We now consider the Hamiltonian function

$$
\begin{array} { r } { \mathcal { H } ( p , q ) = H ( p , q ) + g ( q ) ^ { T } \lambda ( p , q , h ) , } \end{array}
$$

where $\lambda ( p , q , h )$ is the function defined in (8.48). The corresponding Hamiltonian system is

$$
\begin{array} { r l } & { \boldsymbol { q } ^ { \prime } = H _ { p } ( p , q ) + \boldsymbol { g } ( \boldsymbol { q } ) ^ { T } \boldsymbol { \lambda } _ { p } ( p , q , h ) } \\ & { \boldsymbol { p } ^ { \prime } = - H _ { q } ( p , q ) - \boldsymbol { G } ^ { T } ( \boldsymbol { q } ) \boldsymbol { \lambda } ( p , q , h ) - \boldsymbol { g } ( \boldsymbol { q } ) ^ { T } \boldsymbol { \lambda } _ { q } ( p , q , h ) . } \end{array}
$$

The main observation is now that, for initial values satisfying $g ( q _ { 0 } ) = 0$ , the numerical solution $\left( \widehat { p } _ { 1 } , q _ { 1 } \right)$ of (8.49) is exactly the same as the numerical solution of the symplectic Euler method (8.45) applied to the (unconstrained) Hamiltonian system (8.51). Therefore, Example 8.9 shows that the numerical solution $( \widehat { p } _ { \stackrel { 1 } { \sim } } , q _ { 1 } )$ is $\mathcal { O } ( h ^ { 4 } )$ -close to the exact solution of (8.46),where in the definition of $H$ the function $H$ has to be replaced by $\mathcal { H }$ od Eq. (8.50).

The projection step (8.8d,e) can be treated similarly. The solution $\mu$ of (8.8d), (8.9b) depends on ${ \widehat { p } } _ { 1 } , q _ { 1 }$ ,and $h$ (the dependence on $p _ { 0 } , q _ { 0 }$ can be omitted,because the relations $_ { ( 8 . 8 \mathrm { a } , \mathrm { b } ) }$ allow us to express them in terms of $\widehat { p } _ { 1 } , q _ { 1 }$ ,and $h$ ). Due to the relation (8.8d) we can also consider $\mu$ as a function of $p _ { 1 } , q _ { 1 } , h$ ，i.e., $\mu =$ $\mu ( p _ { 1 } , q _ { 1 } , h )$ . We now consider the Hamiltonian

$$
{ \mathcal { G } } ( p , q ) = g ( q ) ^ { T } \mu ( p , q , h ) ,
$$

and the corresponding Hamiltonian system

$$
\begin{array} { r l } & { { \boldsymbol { q } } ^ { \prime } = { \boldsymbol { g } } ( { \boldsymbol { q } } ) ^ { T } { \boldsymbol { \mu } } _ { p } ( p , q , h ) } \\ & { { \boldsymbol { p } } ^ { \prime } = - { \boldsymbol { G } } ^ { T } ( { \boldsymbol { q } } ) { \boldsymbol { \mu } } ( p , q , h ) - { \boldsymbol { g } } ( { \boldsymbol { q } } ) ^ { T } { \boldsymbol { \mu } } _ { q } ( p , q , h ) . } \end{array}
$$

If $g ( q _ { 1 } ) = 0$ , the numerical approximation $p _ { 1 }$ , computed from (8.8d), i.e., $p _ { 1 } =$ $\widehat { p } _ { 1 } - h G ^ { T } ( q _ { 1 } ) \mu ( p _ { 1 } , q _ { 1 } , h )$ , is identical to the numerical solution of (8.45),applied to the system (8.53) with initial values $( \widehat { p } _ { 1 } , q _ { 1 } )$ . Again, we obtain from Exam-ple 8.9 that the numerical solution $\big ( \underline { { p } } _ { 1 } , q _ { 1 } \big )$ is $\mathcal { O } ( h ^ { 4 } )$ -close to the exact solution of (8.46),where in the definition of $H$ the function $H$ has to be replaced by $\mathcal { G }$ of Eq. (8.52). We summarize our findings in the following theorem.

Theorem 8.11. Consider the one-step method (8.8) and assume that the initial values are consistent, i.e., $( p _ { 0 } , q _ { 0 } ) \in \mathcal { M }$ . Then it holds

$$
p _ { 1 } - \widetilde { p } ( h ) = \mathcal { O } ( h ^ { 4 } ) , \qquad q _ { 1 } - \widetilde { q } ( h ) = \mathcal { O } ( h ^ { 4 } ) ,
$$

where $\widetilde { p } ( t ) , \widetilde { q } ( t )$ is the solution of the Hamiltonian system (8.46) with

$$
\widetilde { H } = \widehat { H } + \widehat { G } + \frac { h } { 2 } \big \{ \widehat { H } , \widehat { G } \big \} + \frac { h ^ { 2 } } { 1 2 } \Big ( \big \{ \widehat { H } , \{ \widehat { H } , \widehat { G } \} \big \} + \big \{ \widehat { G } , \{ \widehat { G } , \widehat { H } \} \big \} \Big )
$$

where

$$
\begin{array} { r l } & { \widehat { H } = \mathcal { H } - \displaystyle \frac { h } { 2 } \mathcal { H } _ { p } \mathcal { H } _ { q } + \frac { h ^ { 2 } } { 1 2 } \Big ( \mathcal { H } _ { p p } \mathcal { H } _ { q } ^ { 2 } + \mathcal { H } _ { q q } \mathcal { H } _ { p } ^ { 2 } + 4 \mathcal { H } _ { p q } \mathcal { H } _ { p } \mathcal { H } _ { q } \Big ) } \\ & { \widehat { G } = \mathcal { G } - \displaystyle \frac { h } { 2 } \mathcal { G } _ { p } \mathcal { G } _ { q } + \frac { h ^ { 2 } } { 1 2 } \Big ( \mathcal { G } _ { p p } \mathcal { G } _ { q } ^ { 2 } + \mathcal { G } _ { q q } \mathcal { G } _ { p } ^ { 2 } + 4 \mathcal { G } _ { p q } \mathcal { G } _ { p } \mathcal { G } _ { q } \Big ) , } \end{array}
$$

and $\mathcal { H }$ and $\mathcal { G }$ are given by (8.50) and (8.52), respectively. Here,the poisson bracket $\{ H , G \}$ of two functions $H , G : \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }  \mathbb { R }$ is given by $\{ H , G \} : =$ $H _ { p } G _ { q } - H _ { q } G _ { p }$ (see Eq. (I1.16.65)).

Proof. We consider the one-step method (8.8) as a composition of the mappings $( p _ { 0 } , q _ { 0 } ) \mapsto ( { \widehat { p } } _ { 1 } , q _ { 1 } )$ and $( \widehat { p } _ { 1 } , q _ { 1 } ) \mapsto ( p _ { 1 } , q _ { 1 } )$ . Neglecting terms of size $\mathcal { O } ( h ^ { 4 } )$ ,both mappings can be interpreted as the $h$ -flow of Hamiltonian systems. The statement thus follows from the Campbell-Baker-HausdorffFormula (II.16.83). □

Backward Error Analysis for the Method (8.19). We consider the solution $\lambda _ { 0 }$ of (8.19a,b), (8.9a) as a function of $p _ { 1 / 2 } , q _ { 0 }$ ,and $h$ ,i.e., $\lambda _ { 0 } = \lambda ( p _ { 1 / 2 } , q _ { 0 } , h )$ , and the solution $\mu _ { 0 }$ of (8.19d), (8.9b) as a function of $p _ { 1 } , q _ { 1 }$ and $h$ ,i.e., $\dot { \mu } _ { 0 } = \mu ( p _ { 1 } , q _ { 1 } , h )$ The method (8.19) can therefore be written as the composition of

$$
\begin{array} { c } { { p _ { 1 / 2 } = p _ { 0 } - \displaystyle \frac { h } { 2 } \Big ( H _ { q } \big ( p _ { 1 / 2 } , q _ { 0 } \big ) + G ^ { T } \big ( q _ { 0 } \big ) \lambda \big ( p _ { 1 / 2 } , q _ { 0 } , h \big ) \Big ) } } \\ { { q _ { 1 } = q _ { 0 } + \displaystyle \frac { h } { 2 } \Big ( H _ { p } \big ( p _ { 1 / 2 } , q _ { 0 } \big ) + H _ { p } \big ( p _ { 1 / 2 } , q _ { 1 } \big ) \Big ) } } \\ { { \widehat { p } _ { 1 } = p _ { 1 / 2 } - \displaystyle \frac { h } { 2 } \Big ( H _ { q } \big ( p _ { 1 / 2 } , q _ { 1 } \big ) + G ^ { T } \big ( q _ { 1 } \big ) \lambda \big ( p _ { 1 / 2 } , q _ { 1 } , h \big ) \Big ) } } \end{array}
$$

with the projection step

$$
p _ { 1 } = \widehat { p } _ { 1 } - \frac { h } { 2 } G ^ { T } ( q _ { 1 } ) \nu ( p _ { 1 } , q _ { 1 } , h ) ,
$$

where $\nu ( p _ { 1 } , q _ { 1 } , h ) = \mu ( p _ { 1 } , q _ { 1 } , h ) - \lambda ( p _ { 1 / 2 } , q _ { 1 } , h )$ . We see that, for consistent initial values $( p _ { 0 } . q _ { 0 } ) \in \mathcal { M }$ ,(8.54) is identical to (8.47) with $H ( p , q )$ replaced by

$$
\begin{array} { r } { \mathcal { H } ( p , q ) = H ( p , q ) + g ( q ) ^ { T } \lambda ( p , q , h ) , } \end{array}
$$

and the projection step (8.55) can be interpreted as method (8.45) with Hamiltonian function

$$
\mathcal { G } ( \boldsymbol { p } , \boldsymbol { q } ) = \frac { 1 } { 2 } \boldsymbol { g } ( \boldsymbol { q } ) ^ { T } \boldsymbol { \nu } ( \boldsymbol { p } , \boldsymbol { q } , \boldsymbol { h } ) .
$$

In the same way as for the first order method we get:

Theorem 8.12. Consider the method (8.19) and assume consistent initial values $( p _ { 0 } , q _ { 0 } ) \in \mathcal { M }$ . Then it holds

$$
p _ { 1 } - \widetilde { p } ( h ) = \mathcal { O } ( h ^ { 4 } ) , \qquad q _ { 1 } - \widetilde { q } ( h ) = \mathcal { O } ( h ^ { 4 } ) ,
$$

where $\widetilde { p } ( t ) , \widetilde { q } ( t )$ is the solution of the Hamiltonian system (8.46) with

$$
\widetilde { H } = \widehat { H } + \widehat { G } + \frac { h } { 2 } \big \{ \widehat { H } , \widehat { G } \big \} + \frac { h ^ { 2 } } { 1 2 } \bigg ( \big \{ \widehat { H } , \{ \widehat { H } , \widehat { G } \} \big \} + \big \{ \widehat { G } , \{ \widehat { G } , \widehat { H } \} \big \} \bigg )
$$

where

$$
\begin{array} { r l } & { \widehat { H } = \mathcal { H } + \displaystyle \frac { h ^ { 2 } } { 2 4 } \Big ( 2 \mathcal { H } _ { q q } \mathcal { H } _ { p } ^ { 2 } - \mathcal { H } _ { p p } \mathcal { H } _ { q } ^ { 2 } + 2 \mathcal { H } _ { p q } \mathcal { H } _ { p } \mathcal { H } _ { q } \Big ) } \\ & { \widehat { G } = \mathcal { G } - \displaystyle \frac { h } { 2 } \mathcal { G } _ { p } \mathcal { G } _ { q } + \displaystyle \frac { h ^ { 2 } } { 1 2 } \Big ( \mathcal { G } _ { p p } \mathcal { G } _ { q } ^ { 2 } + \mathcal { G } _ { q q } \mathcal { G } _ { p } ^ { 2 } + 4 \mathcal { G } _ { p q } \mathcal { G } _ { p } \mathcal { G } _ { q } \Big ) , } \end{array}
$$

and $\mathcal { H }$ and $\mathcal { G }$ are given by (8.56) and (8.57), respectively.

The above two theorems show that, for consistent initial values, the numerical solution of the considered methods is (up to a certain order) the exact solution of an unconstrained perturbed Hamiltonian system. The perturbed Hamiltonian is defined in a neighbourhood of the manifold, so that all backward error analysis results for ODEs can be applied.

# Exercises

1. (Jay 1995). The system (1.46) is equivalent to

$$
\begin{array} { c } { { q ^ { \prime } = u } } \\ { { \ ( M ( q ) u ) ^ { \prime } = M _ { q } ( q ) ( u , u ) + f ( q , u ) - G ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) . } } \end{array}
$$

In the case where (1.46) is obtained from the Lagrangian function ${ \mathcal { L } } ( q , { \dot { q } } ) =$ $\begin{array} { r } { \frac { 1 } { 2 } \dot { q } ^ { T } M ( q ) \dot { q } - U ( q ) } \end{array}$ ,show that $f ( q , u )$ always contains the term $- M _ { q } ( q ) ( u , u )$ (Coriolis forces), which thus cancels out in the formulation (8.58).

2. Show that the example(2.1a-c) is of the form (8.1a-c) with Hamiltonian

$$
H ( p , q ) = ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) / 2 + q _ { 2 } .
$$

If we compute $\lambda$ from(2.3),and insert it into (2.1a,b), the resulting differential equation is no longer Hamiltonian.

3. Give a second proof of Theorem 8.1 by applying Theorem I.14.12.

Hint (Reich 1996). Let $\lambda = \lambda ( p , q )$ be defined by (8.3b) and consider the unconstrained Hamiltonian system with Hamiltonian

$$
H ( p , q ) + g ( q ) ^ { T } \lambda ( p , q ) ,
$$

whose flow reduces to that of (8.1) along the constraint manifold $\ M$ ·

4. Consider a partitioned Runge-Kutta method applied to a partitioned ordinary differential equation (without constraints). Suppose that both methods are based on the same quadrature formula of order $p$ ， that the first method satisfies $C ( \eta ) , D ( \xi )$ ， and that the second method satisfies $C ( \widehat { \eta } ) , D ( \widehat { \xi } )$ .Prove that the pair has order

$$
\operatorname* { m i n } \Bigl ( p , 2 \operatorname* { m i n } ( \eta , \widehat { \eta } ) + 2 , \operatorname* { m i n } ( \eta , \widehat { \eta } ) + \operatorname* { m i n } ( \xi , \widehat { \xi } ) + 2 , \operatorname* { m i n } ( \eta + \xi , \widehat { \eta } + \widehat { \xi } ) + 1 \Bigr ) .
$$

Conclude that the Lobatto IIIA-IIB pair has order $2 s - 2$

Hint. Apply the ideas of the proof of Theorem II.7.4 for the verification of the order conditions (Sect. I.15).

5. Compute a first integral of the differential equation (8.43). What is the reason for the existence of such an invariant?

Hint. With the transformation $u \ : = \ : e ^ { p }$ ， $v \simeq e ^ { q }$ you will get a Hamiltonian system.

$$
\widetilde { I } ( u , v ) = I ( u , v ) + h \big ( ( u + v ) ^ { 2 } - 1 0 u - 8 v + 8 \ln u + 2 \ln v \big ) \big / 4 .
$$

![](images/e6347f32732f8e7543a27890fffa4a0c1286d144ca48ab6e86a5c4929655aca9.jpg)

lso geht alles zu Ende allhicr: Feder, Tinte, Tobak und auch wir. Zum lerztenmal wird cingetunkt, Dann kommt der grofc

schwarzc

(W. Busch,Bilder zur Jobsiade 1872)

# Appendix. Fortran Codes

During the preparation of this book several programs have been developed for solving stiff and differential-algebraic problems of the form

$$
M y ^ { \prime } = f ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 } ,
$$

where $M$ is a constant square matrix. If $M$ is singular, the problem is differentialalgebraic. In this case the initial values have to be consistent.

The implicit Runge-Kutta code RADAU5 and its extension RADAUP can be applied to higher index $( \geq 2 )$ problems as well, whereas the Rosenbrock code RODAS and the exptrapolation code SEULEX are suited for explicit stiff differential equations and index 1 problems. The codes SDIRK4, ROS4,and SODEX are still available, but have not been updated.

In the case where $M$ is not a constant matrix, suitable transformations and/or introduction of new variables allow us to bring every implicit differential equation to the form (A.1). If the problem is originally in one of the following forms

$$
B ( y ) y ^ { \prime } = f ( x , y ) , \qquad y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) , \qquad B ( y ) y ^ { \prime \prime } = f ( x , y , y ^ { \prime } ) ,
$$

or the like, then the eficiency of the code can be increased by seting some parameters. This will be explained later in this appendix.

Communication with the code during integration can be done with help of the user-supplied subroutine SOLOUT. This is illustrated in the driver below. Further applications of this subroutine are discussed at the end of this appendix.

Experiences with all of our codes are welcome. The programs can be obtained by anonymous ftp (from“ftp.unige.ch” in the directory “pub/doc/math”or from "http://www.unige.ch/math/folks/hairer/").

Address: Section de Mathématiques, Case postale 240, CH-1211 Geneve 24, Switzerland E-mail: Ernst.Hairer@math.unige.chGerhard.Wanner $@$ math.unige.ch

# Driver for the Code RADAU5

“The van der Pol equation problem is so much harder than the rest ..." (L.F. Shampine 1987)

We consider the van der Pol equation

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = y _ { 2 } } & & { y _ { 1 } ( 0 ) = 2 } \\ & { y _ { 2 } ^ { \prime } = \left( \left( 1 - y _ { 1 } ^ { 2 } \right) y _ { 2 } - y _ { 1 } \right) / \varepsilon } & & { y _ { 2 } ( 0 ) = - 0 . 6 6 } \end{array}
$$

with $\varepsilon = 1 0 ^ { - 6 }$ on the interval [0,2]. The subroutines FVPOL, JVPOL compute the right-hand side of this differential equation and its Jacobian. The subroutine SOLOUT is used to print the solution at equidistant points.

C   
C link driver radau5 decsol dc-decsol or   
C link driver radau5 lapack lapackc dc-lapack   
C IMPLICIT REAL\*8 (A-H,0-Z)   
C --- PARAMETERS FOR RADAU5 (FULL JACOBIAN) PARAMETER（ $\mathtt { N D = 2 }$ ,LWORK=4\*ND\*ND+12\*ND+20,LIWORK=3\*ND+20) DIMENSION Y(ND）,WORK(LWORK）,IWORK（LIWORK） EXTERNAL FVPOL,JVPOL,SOLOUT   
C --- PARAMETER IN THE DIFFERENTIAL EQUATION $\tt R P A R = 1$ .0D-6   
C --- DIMENSION OF THE SYSTEM $\aleph = 2$   
C --- COMPUTE THE JACOBIAN ANALYTICALLY $\texttt T J A C = 1$   
C --- JACOBIAN IS A FULL MATRIX $M L J A C = N$   
C --- DIFFERENTIAL EQUATION IS IN EXPLICIT FORM IMA $\mathtt { S } { = } 0$   
C --- OUTPUT ROUTINE IS USED DURING INTEGRATION IOUT $\mathbf { \bar { \Pi } } { } = 1$   
C --- INITIAL VALUES ${ \tt X } { = } 0$ .0D0 $\yen (1)=2$ .0D0 $\yen (2)=-0$ .66D0   
C --- ENDPOINT OF INTEGRATION $\tt X E N D = 2$ .0D0   
C --- REQUIRED TOLERANCE RTOL $\mathbf { \lambda } = \mathbf { 1 }$ .0D-4 ATOL $\mathbf { = 1 }$ ： $O D O + R T O I =$ ITOL $\mathtt { \mathtt { = 0 } }$   
C --- INITIAL STEP SIZE ${ \tt H } = 1 . 0 \tt { D } { - 6 }$   
C --- SET DEFAULT VALUES D0 $\tt T = 1$ ,20 IWORK(I) $\mathtt { \mathtt { = 0 } }$ WORK(I) $\mathtt { = 0 }$ .D0 END DO   
C --- CALL OF THE SUBROUTINE RADAU5 CALL RADAU5(N,FVPOL,X,Y,XEND,H, $^ +$ RTOL,ATOL,ITOL, $^ { + }$ JVPOL,IJAC,MLJAC,MUJAC, $^ +$ FVPOL,IMAS,MLMAS,MUMAS, $^ +$ SOLOUT,IOUT, + WORK,LWORK,IWORK,LIWORK,RPAR,IPAR,IDID   
C --- PRINT FINAL SOLUTION WRITE (6,99) X,Y(1),Y(2)   
99 FORMAT(1X,'X =',F5.2,; Y =',2E18.10)   
C --- PRINT STATISTICS WRITE （6,90） RTOL 90 FORMAT(' rtol=',D8.2) WRITE (6,91） （IWORK(J),J=14,20) 91 FORMAT(' fcn=',I5,' jac=',I4,' step=',I4,' accpt=',I4, + ） rejct=',I3,' dec=',I4,' sol=',5) STOP END   
C SUBROUTINE SOLOUT (NR,XOLD,X,Y,CONT,LRC,N,RPAR,IPAR,IRTRN)   
C --- PRINTS SOLUTION AT EQUIDISTANT OUTPUT-POINTS BY USING "CONTF IMPLICIT REAL $\yen 8$ (A-H,0-Z) DIMENSION Y(N),CONT(LRC) COMMON /INTERN/XOUT IF （NR.EQ.1） THEN WRITE (6,99) X,Y(1),Y(2),NR-1 XOUT $\mathtt { = 0 }$ .2D0 ELSE 10 CONTINUE IF （X.GE.XOUT） THEN   
C --- CONTINUOUS OUTPUT FOR RADAU5 WRITE （6,99) XOUT,CONTR5(1,XOUT,CONT,LRC), + CONTR5(2,XOUT,CONT,LRC),N-1 XOUT=XOUT $\mathtt { + 0 }$ .2D0 GOTO 10 END IF END IF 99 FORMAT(1X,'X =',F5.2,' Y =',2E18.10,' NSTEP =',I4) RETURN END   
C SUBROUTINE FVPOL $( \mathtt { N } , \mathtt { X } , \mathtt { Y } , \mathtt { F } , \mathtt { R P A R } , \mathtt { I P A R }$ ）   
C --- RIGHT-HAND SIDE OF VAN DER POL'S EQUATION IMPLICIT REAL $\yen 8$ (A-H,0-Z) DIMENSION Y(N),F(N) $\mathbb { F } \left( 1 \right) { = } \mathbb { Y }$ (2) $\mathrm { \Delta F \left( 2 \right) = \left( \left( 1 - Y \left( 1 \right) \ast \ast 2 \right) \ast Y \left( 2 \right) - Y \left( 1 \right) \right) / R P A R }$ RETURN END   
C SUBROUTINE JVPOL $( \mathbb { N } , \mathbb { X } , \mathbb { Y }$ ,DFY,LDFY,RPAR,IPAR)   
C --- JACOBIAN OF VAN DER POL'S EQUATION IMPLICIT REAL $\yen 8$ （A-H,0-Z) DIMENSION Y(N),DFY(LDFY,N) DFY(1,1) $\mathtt { = 0 }$ .0D0 DFY(1,2) $\mathbf { \equiv } \mathbf { 1 }$ .0D0 ${ \sf O F Y } \left( 2 , 1 \right) = \left( - 2 . 0 \mathrm { D } 0 * \mathrm { Y } \left( \mathrm { \bf ~ 1 } \right) * \mathrm { Y } \left( 2 \right) - 1 . 0 \mathrm { D } 0 \right) / \mathrm { R P A R }$ $\mathtt { D F Y } \left( 2 , 2 \right) = \left( \mathtt { 1 } \ . 0 \mathtt { D 0 } \ – \mathtt { Y } \left( \mathtt { 1 } \right) * * 2 \right) / \mathtt { R P }$ AR RETURN END

The result, obtained on a Sun SPARKstation 20,is the following:

$\tt { X } = 0 . 0 0$ Y= 0.2000000000E+01 -0.6600000000E+00 NSTEP = 0   
$\texttt { X } = \texttt { 0 } . 2 0$ Y= 0.1858210825E+01 -0.7575052373E+00 NSTEP = 10   
$\tt { X } = 0 . 4 0$ Y= 0.1693217727E+01 -0.9068995621E+00 NSTEP 11   
$\tt { X } = 0 . 6 0$ Y= 0.1484573110E+01 -0.1233017457E+01 NSTEP 13   
$\tt { X } = 0 . 8 0$ Y = 0.1083921362E+01 -0.6195010714E+01 NSTEP $\mathbf { \equiv }$ 21   
X = 1.00 Y = -0.1863641256E+01 0.7535196392E+00 NSTEP = 144   
X = 1.20 Y = -0.1699715970E+01 0.8997232240E+00 NSTEP $=$ 145   
X = 1.40 Y = -0.1493380698E+01 0.1213958018E+01 NSTEP $\cong$ 147   
X = 1.60 Y = -0.1120822309E+01 0.4373266499E+01 NSTEP = 153   
x = 1.80 Y= 0.1869064482E+01 -0.7496053261E+00 NSTEP = 275   
x = 2.00 Y = 0.1706171005E+01 -0.8928020961E+00 NSTEP $=$ 276   
X = 2.00 Y = 0.1706171005E+01 -0.8928020961E+00   
rto1=0.10D-03   
fcn= 2263 jac= 182 step= 293 accpt $\mathbf { \equiv }$ 276 rejct= 9 dec= 251 sol= 662

# Subroutine RADAU5

Implicit Runge-Kutta code based on the 3-stage Radau IIA method, given in Table IV.5.6. Details on the implementation are described in Section IV.8.

SUBROUTINE RADAU5(N,FCN,X,Y,XEND,H,+ RTOL,ATOL,ITOL,+ JAC ,IJAC,MLJAC,MUJAC,$^ { + }$ MAS,IMAS,MLMAS,MUMAS,$^ +$ SOLOUT,IOUT,+ WORK,LWORK,IWORK ,LIWORK,RPAR,IPAR,IDID)CC NUMERICAL SOLUTION OF A STIFF (OR DIFFERENTIAL ALGEBRAIC)C SYSTEM OF FIRST ORDER ORDINARY DIFFERENTIAL EQUATIONSC $\mathbb { M } { * } \mathbb { Y } ^ { \prime } { = } \mathbb { F } \left( \mathbb { X } , \mathbb { Y } \right)$ ：C THE SYSTEM_CAN BE (LINEARLY） IMPLICIT (MASS-MATRIX M .NE. I）C OR EXPLICIT $( M = I )$ ）：C THE METHOD USED IS AN IMPLICIT RUNGE-KUTTA METHOD (RADAU IIA)C OF ORDER 5 WITH STEP SIZE CONTROL AND CONTINUOUS OUTPUT.C C.F. SECTION IV.8CC AUTHORS: E. HAIRER AND G. WANNERC UNIVERSITE DE GENEVE， DEPT. DE MATHEMATIQUESC CH-1211 GENEVE 24， SWITZERLANDC E-MAIL: HAIRERQDIVSUN.UNIGE.CH， WANNER@DIVSUN.UNIGE.CHCC THIS CODE IS PART OF THE BOOK:C E. HAIRER AND G. WANNER， SOLVING ORDINARY DIFFERENTIALC EQUATIONS II. STIFF AND DIFFERENTIAL-ALGEBRAIC PROBLEMS.C SPRINGER SERIES IN COMPUTATIONAL MATHEMATICS 14，C SPRINGER-VERLAG 1991， SECOND EDITION 1996.CC VERSION OF SEPTEMBER 30，1995CC INPUT PARAMETERSCC N DIMENSION OF THE SYSTEMCC FCN NAME （EXTERNAL） OF SUBROUTINE COMPUTING THEC VALUE OF $\mathbb { F } ( \mathbb { X } , \mathbb { Y } )$ ：C SUBROUTINE FCN(N,X,Y,F,RPAR,IPAR)C REAL $\yen 8$ X,y(N),f(N)C $\mathbb { F } ( \mathbf { 1 } ) \equiv \ldots$ EtC.C RPAR，IPAR （SEE BELOW)CC X INITIAL X-VALUECC Y(N) INITIAL VALUES FOR Y

XEND FINAL X-VALUE (XEND-X MAY BE POSITIVE OR NEGATIVE)  
H INITIAL STEP SIZE GUESS;FOR STIFF EQUATIONS WITH INITIAL TRANSIENT,$\mathtt { H } = 1$ .D0/(NORM OF F')，USUALLY 1.D-3 OR 1.D-5，IS GOOD.THIS CHOICE IS NOT VERY IMPORTANT， THE STEP SIZE ISQUICKLY ADAPTED.（IF ${ \tt H } { = } 0$ .D0，THE CODE PUTS ${ \bf H } = 1 . { \bf D } { \bf - } 6 $ .  
RTOL,ATOL RELATIVE AND ABSOLUTE ERROR TOLERANCES. THEYCAN BE BOTH SCALARS OR ELSE BOTH VECTORS OF LENGTH N.  
ITOL SWITCH FOR RTOL AND ATOL:ITOL $\mathtt { = 0 }$ :BOTH RTOL AND ATOL ARE SCALARS.THE CODE KEEPS，ROUGHLY， THE LOCAL ERROR OFY(I） BELOW RTOL $^ *$ ABS(Y(I)) $+ \tt A T O L$ ITOL=1: BOTH RTOL AND ATOL ARE VECTORS.THE CODE KEEPS THE LOCAL ERROR OF Y(I） BELOWR $\mathbf { \cdot } \mathbf { \bar { 0 } } \mathbf { \bar { L } } \left( \mathbf { \bar { I } } \right) { \ast } \mathbf { \bar { A } } \mathbf { B } \mathbf { S } \left( \mathbf { \check { Y } } \left( \mathbf { \bar { I } } \right) \right) { + } \mathbf { \bar { A } } \mathbf { \bar { T } } \mathbf { 0 } \mathbf { \bar { L } } \left( \mathbf { \bar { I } } \right)$ ：  
JAC NAME （EXTERNAL） OF THE SUBROUTINE WHICH COMPUTESTHE PARTIAL DERIVATIVES OF $\mathbb { F } ( \mathbb { X } , \mathbb { Y } )$ WITH RESPECT TO Y(THIS ROUTINE IS ONLY CALLED IF $\texttt { T J A C = 1 }$ ； SUPPLYA DUMMY SUBROUTINE IN THE CASE $\mathtt { T J A C = 0 }$ ）.FOR $\texttt { T J A C = 1 }$ ， THIS SUBROUTINE MUST HAVE THE FORMSUBROUTINE JAC(N,X,Y,DFY,LDFY,RPAR,IPAR)REAL $^ { * 8 }$ X,Y(n),DFy(ldFy,n)DFY $( \mathbf { 1 } , \mathbf { 1 } ) \mathbf { = }$ ：LDFY， THE COLUMN-LENGTH OF THE ARRAY， ISFURNISHED BY THE CALLING PROGRAM.IF(MLJAC.EQ.N） THE JACOBIAN IS SUPPOSED TOBE FULL AND THE PARTIAL DERIVATIVES ARESTORED IN DFY ASDFY(I,J) $\mathbf { \equiv } =$ PARTIAL F(I) / PARTIAL Y(J)ELSE， THE JACOBIAN IS TAKEN AS BANDED ANDTHE PARTIAL DERIVATIVES ARE STOREDDIAGONAL-WISE ASDFY(I-J+MUJAC+1,J) $=$ PARTIAL F(I) / PARTIAL Y(J).  
IJAC SWITCH FOR THE COMPUTATION OF THE JACOBIAN:$\mathtt { T J A C = 0 }$ :JACOBIAN IS COMPUTED INTERNALLY BY FINITEDIFFERENCES， SUBROUTINE "JAC" IS NEVER CALLED.$\texttt { T J A C = 1 }$ :JACOBIAN IS SUPPLIED BY SUBROUTINE JAC.  
MLJAC SWITCH FOR THE BANDED STRUCTURE OF THE JACOBIAN:MLJAC=N: JACOBIAN IS A FULL MATRIX. THE LINEARALGEBRA IS DONE BY FULL-MATRIX GAUSS-ELIMINATION.O<=MLJAC<N: MLJAC IS THE LOWER BANDWITH OF JACOBIANMATRIX ( $> =$ NUMBER OF NON-ZERO DIAGONALS BELOWTHE MAIN DIAGONAL）.  
MUJAC UPPER BANDWITH OF JACOBIAN MATRIX （ $> =$ NUMBER OF NON-ZERO DIAGONALS ABOVE THE MAIN DIAGONAL）.NEED NOT BE DEFINED IF MLJA $\therefore C = N$ ：MAS,IMAS,MLMAS， AND MUMAS HAVE ANALOG MEANINGSFOR THE "MASS MATRIX" (THE MATRIX "M" OF SECTION IV.8):  
MAS NAME （EXTERNAL） OF SUBROUTINE COMPUTING THE MASS-MATRIX M.IF IMA $\scriptstyle { \mathfrak { S } } = 0$ ，THIS MATRIX IS ASSUMED TO BE THE IDENTITYMATRIX AND NEEDS NOT TO BE DEFINED;

SUPPLY A DUMMY SUBROUTINE IN THIS CASE.IF $I M A S = 1$ ，THE SUBROUTINE MAS IS OF THE FORMSUBROUTINE MAS(N,AM,LMAS,RPAR,IPAR)REAL\*8 AM(LMAS,N)${ \tt A M } ( \bf { \tt 1 } , \bf { 1 } ) =$ IF (MLMAS.EQ.N） THE MASS-MATRIX IS STOREDAS FULL MATRIX LIKE$\mathtt { A M ( I , J ) } \ = \ \mathtt { M ( I , J ) }$ ELSE， THE MATRIX IS TAKEN AS BANDED AND STOREDDIAGONAL-WISE AS$\mathtt { A M ( I - J + M U M A S + 1 , J ) \ } = \mathtt { M ( I , J ) } .$ IMAS GIVES INFORMATION ON THE MASS-MATRIX:$I M A S = 0$ :M IS SUPPOSED TO BE THE IDENTITYMATRIX，MAS IS NEVER CALLED.$I M A S = 1$ : MASS-MATRIX IS SUPPLIED.MLMAS SWITCH FOR THE BANDED STRUCTURE OF THE MASS-MATRIX:MLMA: ${ \tt S } { = } { \tt N }$ : THE FULL MATRIX CASE. THE LINEARALGEBRA IS DONE BY FULL-MATRIX GAUSS-ELIMINATION$_ { 0 } < = \mathtt { M L M A S } < \mathtt { N }$ : MLMAS IS THE LOWER BANDWITH OF THEMATRIX ( $> =$ NUMBER OF NON-ZERO DIAGONALS BELOWTHE MAIN DIAGONAL）.MLMAS IS SUPPOSED TO BE .LE. MLJAC.MUMAS UPPER BANDWITH OF MASS-MATRIX （ $> =$ NUMBER OF NON-ZERO DIAGONALS ABOVE THE MAIN DIAGONAL）.NEED NOT BE DEFINED IF MLMAS=N.MUMAS IS SUPPOSED TO BE .LE. MUJAC.SOLOUT NAME （EXTERNAL） OF SUBROUTINE PROVIDING THENUMERICAL SOLUTION DURING INTEGRATION.IF IOUT $\mathbf { \delta } = 1$ ，IT IS CALLED AFTER EVERY SUCCESSFUL STEP.SUPPLY A DUMMY SUBROUTINE IF IOUT $\mathtt { = 0 }$ .IT MUST HAVE THE FORMSUBROUTINE SOLOUT (NR,XOLD,X,Y,CONT,LRC,N,RPAR,IPAR,IRTRN)REAL $\yen 8$ X,Y(N),CONT(LRC)SOLOUT FURNISHES THE SOLUTION "Y" AT THE NR-THGRID-POINT "X" （THEREBY THE INITIAL VALUE ISTHE FIRST GRID-POINT)."XOLD" IS THE PRECEEDING GRID-POINT."IRTRN" SERVES TO INTERRUPT THE INTEGRATION. IF IRTRNIS SET <O， RADAU5 RETURNS TO THE CALLING PROGRAM.CONTINUOUS OUTPUT: --DURING CALLS TO "SOLOUT"， A CONTINUOUS SOLUTIONFOR THE INTERVAL [XOLD,X] IS AVAILABLE THROUGHTHE FUNCTION>>>CONTR5(I,S,CONT,LRC） <<<WHICH PROVIDES AN APPROXIMATION TO THE I-THCOMPONENT OF THE SOLUTION AT THE POINT S. THE VALUES SHOULD LIE IN THE INTERVAL [XOLD,X].DO NOT CHANGE THE ENTRIES OF CONT(LRC)， IF THEDENSE OUTPUT FUNCTION IS USED.IOUT SWITCH FOR CALLING THE SUBROUTINE SOLOUT:IOUT $\mathtt { = 0 }$ :SUBROUTINE IS NEVER CALLEDIOUT $\mathbf { = 1 }$ : SUBROUTINE IS AVAILABLE FOR OUTPUT.CC WORK ARRAY OF WORKING SPACE OF LENGTH "LWORK".

Appendix.Fortran CodesWORK(1），WORK(2）,..，WORK(2O） SERVE AS PARAMETERSFOR THE CODE. FOR STANDARD USE OF THE CODEWORK(1),..,WORK(2O) MUST BE SET TO ZERO BEFORECALLING. SEE BELOW FOR A MORE SOPHISTICATED USE.WORK(21),..,WORK(LWORK) SERVE AS WORKING SPACEFOR ALL VECTORS AND MATRICES."LWORK" MUST BE AT LEAST$N _ { 4 } + ( \mathrm { L J A C + L M A S + 3 + L E + 1 2 } ) + 2 0$ WHERE$L J A C = N$ IF MLJAC=N (FULL JACOBIAN)LJAC=MLJAC+MUJAC+1 IF MLJAC<N (BANDED JAC.）AND$L M A S { = } 0$ IF $I M A S = 0$ $L M A S = N$ IF $I M A S = 1$ AND MLMAS=N (FULL)LMAS=MLMAS $+$ MUMAS+1 IF MLMAS<N (BANDED MASS-M.）AND$\tt L E { = } \tt N$ IF MLJ ${ \mathsf { A C } } { \mathsf { = N } }$ (FULL JACOBIAN)LE=2\*MLJAC+MUJAC+1 IF MLJAC<N (BANDED JAC.）IN THE USUAL CASE WHERE THE JACOBIAN IS FULL AND THEMASS-MATRIX IS THE INDENTITY $\tan A S = 0$ ，THE MINIMUMSTORAGE REQUIREMENT IS$\tt L W O R K \ = \ 4 * \tt N * N + 1 2 * N + 2 0 \ .$ IF IWORK(9) $= M 1 > 0$ THEN "LWORK" MUST BE AT LEAST$\mathtt { N } * \left( \mathtt { L J A C } + \mathtt { 1 } \mathtt { 2 } \right) + \left( \mathtt { N } \mathtt { - } \mathtt { M } \mathtt { 1 } \right) * \left( \mathtt { L M A S } + \mathtt { 3 } * \mathtt { L E } \right) + \mathtt { 2 0 }$ WHERE IN THE DEFINITIONS OF LJAC，LMAS AND LE THENUMBER N CAN BE REPLACED BY $\pmb { \mathbb { N } } .$ -M1.LWORK DECLARED LENGHT OF ARRAY 'WORK".IWORK INTEGER WORKING SPACE OF LENGHT "LIWORK".IWORK(1),IWORK(2),...,IWORK(2O） SERVE AS PARAMETERSFOR THE CODE.FOR STANDARD USE,SET IWORK(1),.,IWORK(2O） TO ZERO BEFORE CALLING.IWORK(21),...,IWORK(LIWORK) SERVE AS WORKING AREA."LIWORK" MUST BE AT LEAST $3 * \mathbb { N } + 2 0$ LIWORK DECLARED LENGHT OF ARRAY "IWORK".RPAR， IPAR REAL AND INTEGER PARAMETERS (OR PARAMETER ARRAYS） WHICHCAN BE USED FOR COMMUNICATION BETWEEN YOUR CALLINGPROGRAM AND THE FCN， JAC， MAS，SOLOUT SUBROUTINES.SOPHISTICATED SETTING OF PARAMETERSSEVERAL PARAMETERS OF THE CODE ARE TUNED TO MAKE IT WORKWELL. THEY MAY BE DEFINED BY SETTING WORK(1),..AS WELL AS IWORK(1),.. DIFFERENT FROM ZERO.FOR ZERO INPUT， THE CODE CHOOSES DEFAULT VALUES:IWORK（1） IF IWORK(1).NE.O， THE CODE TRANSFORMS THE JACOBIANMATRIX TO HESSENBERG FORM. THIS IS PARTICULARLYADVANTAGEOUS FOR LARGE SYSTEMS WITH FULL JACOBIAN.IT DOES NOT WORK FOR BANDED JACOBIAN (MLJAC<N)AND NOT FOR IMPLICIT SYSTEMS （ $I M A S = 1$ ）：IWORK(2) THIS IS THE MAXIMAL NUMBER OF ALLOWED STEPS.THE DEFAULT VALUE (FOR IWORK $( 2 ) = 0$ ） IS 100000.IWORK(3） THE MAXIMUM NUMBER OF NEWTON ITERATIONS FOR THE

SOLUTION OF THE IMPLICIT SYSTEM IN EACH STEP.THE DEFAULT VALUE (FOR IWORK(3) $\mathtt { = 0 }$ )IS 7.  
IWORK(4） IF IWORK(4）.EQ.O THE EXTRAPOLATED COLLOCATION SOLUTIONIS TAKEN AS STARTING VALUE FOR NEWTON'S METHOD.IF IWORK(4).NE.O ZERO STARTING VALUES ARE USED.THE LATTER IS RECOMMENDED IF NEWTON'S METHOD HASDIFFICULTIES WITH CONVERGENCE (THIS IS THE CASE WHENNSTEP IS LARGER THAN NACCPT $^ +$ NREJCT； SEE OUTPUT PARAM.）.DEFAULT IS IWORK $( 4 ) = 0$ ：THE FOLLOWING 3 PARAMETERS ARE IMPORTANT FORDIFFERENTIAL-ALGEBRAIC SYSTEMS OF INDEX > 1.THE FUNCTION-SUBROUTINE SHOULD BE WRITTEN SUCH THATTHE INDEX 1,2,3 VARIABLES APPEAR IN THIS ORDER.IN ESTIMATING THE ERROR THE INDEX 2 VARIABLES AREMULTIPLIED BY H，THE INDEX 3 VARIABLES BY $\mathtt { H } * * 2$   
IWORK(5） DIMENSION OF THE INDEX 1 VARIABLES （MUST BE $\gamma \circ$ .FORODE'S THIS EQUALS THE DIMENSION OF THE SYSTEM.DEFAULT IWORK(5) $\tt { \tt = N }$   
IWORK（6） DIMENSION OF THE INDEX 2 VARIABLES. DEFAULT IWORK $( 6 ) = 0$   
IWORK（7） DIMENSION OF THE INDEX 3 VARIABLES． DEFAULT IWORK $( 7 ) = 0$ ·  
IWORK（8） SWITCH FOR STEP SIZE STRATEGYIF IWORK(8).EQ.1 MOD. PREDICTIVE CONTROLLER （GUSTAFSSON)IF IWORK(8).EQ.2 CLASSICAL STEP SIZE CONTROLTHE DEFAULT VALUE （FOR IWORK $( 8 ) = 0$ IS IWORK $( 8 ) = 1$ THE CHOICE IWORK(8).EQ.1 SEEMS TO PRODUCE SAFER RESULTS;FOR SIMPLE PROBLEMS， THE CHOICE IWORK(8）.EQ.2 PRODUCESOFTEN SLIGHTLY FASTER RUNSIF THE DIFFERENTIAL SYSTEM HAS THE SPECIAL STRUCTURE THAT$\tt { Y } ( I ) \cdot \tt { \tau } = \tt { Y } ( I + M 2 )$ FOR $\mathbb { I } { = } 1 , \ldots , \mathbb { M } { \bf 1 }$ ，WITH M1 A MULTIPLE OF M2，A SUBSTANTIAL GAIN IN COMPUTERTIMECAN BE ACHIEVED BY SETTING THE PARAMETERS IWORK(9） AND IWORK（10）.E.G.， FOR SECOND ORDER SYSTEMS $\mathbb { P } ^ { \star } { \equiv } \mathbb { V }$ ， $\mathbb { V } ^ { \prime } { \ = } \mathbb { G } \left( \mathbb { P } \mathrm { , } \mathbb { V } \right)$ ，WHERE $\mathtt { P }$ AND $v$ AREVECTORS OF DIMENSION $\mathbb { N } / 2$ ，ONE HAS TO PUT $\mathtt { M 1 } = \mathtt { M 2 } = \mathtt { N } / 2$ ：FOR M1>O SOME OF THE INPUT PARAMETERS HAVE DIFFERENT MEANINGS:- JAC: ONLY THE ELEMENTS OF THE NON-TRIVIAL PART OF THEJACOBIAN HAVE TO BE STOREDIF （MLJAC.EQ.N-M1) THE JACOBIAN IS SUPPOSED TO BE FULLDFY(I,J) $=$ PARTIAL $\mathbb { F } ( \mathbb { I } { + } \mathbb { M } \mathbb { 1 } )$ / PARTIAL Y(J)FOR $\tt T = 1$ ， $\mathbb { N } \cdot$ -M1 AND ${ \bar { \mathbf { \zeta } } } = 1$ ,N.ELSE，THE JACOBIAN IS BANDED（ $\mathbb { M } 1 = \mathbb { M } 2 \ast \mathbb { M } \mathbb { M } )$ DFY $( I - J + M U J A C + 1$ ， $J + \kappa * M 2$ ）= PARTIAL F $\because ( I + M 1 )$ ）/PARTIAL Y(FOR $\tt { I } { = } 1$ ,M $1 \mathbb { L } J \mathbb { A } \mathbb { C } + \mathbb { M } \mathbb { U } J \mathbb { A } \mathbb { C } + 1$ AND ${ \bar { \jmath } } { = } 1$ ,M2 AND $\mathtt { K } { = } 0$ ,MM.- MLJAC: MLJAC=N-M1: IF THE NON-TRIVIAL PART OF THE JACOBIAN IS I$_ { 0 < = \mathbb { M } L \mathbb { J } \mathbb { A } \mathbb { C } < \mathbb { N } - \mathbb { M } \mathbb { 1 } }$ : IF THE $( \mathbb { M } \mathbb { M } + 1 )$ ）SUBMATRICES （FOR $\mathtt { K } = 0$ ,MM)PARTIAL F( $I + M 1$ ）/ PARTIAL $Y ( J + K * M 2 )$ ，I, ${ \bar { \jmath } } { = } 1$ ,M2ARE BANDED，MLJAC IS THE MAXIMAL LOWER BANDWIDTHOF THESE MM+1 SUBMATRICES- MUJAC: MAXIMAL UPPER BANDWIDTH OF THESE $\mathbb { M } \mathbb { M } + 1$ SUBMATRICESNEED NOT BE DEFINED IF MLJA $\complement = \lambda$ -M1- MAS: IF $I M A S = 0$ THIS MATRIX IS ASSUMED TO BE THE IDENTITY ANDNEED NOT BE DEFINED. SUPPLY A DUMMY SUBROUTINE IN THIS CASIIT IS ASSUMED THAT ONLY THE ELEMENTS OF RIGHT LOWER BLOCK(DIMENSION N-M1 DIFFER FROM THAT OF THE IDENTITY MATRIX.IF (MLMAS.EQ.N-M1） THIS SUBMATRIX IS SUPPOSED TO BE FULL$\mathtt { A M ( I , J ) } = \mathtt { M ( I + M 1 , J + M 1 ) }$ FOR $\tt T = 1$ ,N-M1 AND $J = 1 , N - M 1$ ：ELSE，THE MASS MATRIX IS BANDED$\mathbb { A } \mathbb { M } \left( \mathbb { I } { - } \mathbb { J } { + } \mathbb { M } \mathbb { U } \mathbb { M } \mathbb { A } \mathbb { S } { + } { + } { \mathrm { 1 } } { \mathrm { , ~ } } \mathbb { J } \right) ~ = ~ \mathbb { M } \left( \mathbb { I } { + } \mathbb { M } \mathbb { 1 } { \mathrm { ~ , ~ } } \mathbb { J } { + } \mathbb { M } \mathbb { 1 } \right)$ -MLMAS: MLMAS ${ \tt = N }$ -M1: IF THE NON-TRIVIAL PART OF M IS FULLO<=MLMAS<N-M1: LOWER BANDWIDTH OF THE MASS MATRIX- MUMAS: UPPER BANDWIDTH OF THE MASS MATRIXNEED NOT BE DEFINED IF MLMA: ${ \boldsymbol { \ S } } { = } \mathbb { N }$ -M1  
IWORK(9) THE VALUE OF M1. DEFAULT $\yen 120$   
IWORK(1O） THE VALUE OF M2. DEFAULT $M _ { 2 } = M _ { 1 }$   
WORK(1） UROUND， THE ROUNDING UNIT， DEFAULT 1.D-16.  
WORK(2) THE SAFETY FACTOR IN STEP SIZE PREDICTION,DEFAULT 0.9D0.  
WORK(3) DECIDES WHETHER THE JACOBIAN SHOULD BE RECOMPUTED;INCREASE WORK(3），TO O.1 SAY，WHEN JACOBIAN EVALUATIONSARE COSTLY. FOR SMALL SYSTEMS WORK(3) SHOULD BE SMALLER(0.001DO， SAY). NEGATIV WORK(3) FORCES THE CODE TOCOMPUTE THE JACOBIAN AFTER EVERY ACCEPTED STEP.DEFAULT 0.001D0.  
WORK(4) STOPPING CRITERION FOR NEWTON'S METHOD， USUALLY CHOSEN <1SMALLER VALUES OF WORK(4） MAKE THE CODE SLOWER， BUT SAFEFDEFAULT 0.03D0.  
WORK(5） AND WORK(6） : IF WORK(5）< HNEW/HOLD < WORK(6)，THEN THESTEP SIZE IS NOT CHANGED. THIS SAVES， TOGETHER WITH ALARGE WORK(3）， LU-DECOMPOSITIONS AND COMPUTING TIME FORLARGE SYSTEMS. FOR SMALL SYSTEMS ONE MAY HAVEWORK(5) $\mathbf { = 1 }$ .D0，WORK(6) $\mathbf { = 1 }$ .2D0，FOR LARGE FULL SYSTEMSWORK(5) $\mathtt { = 0 }$ .99D0，WORK(6) $\mathtt { = 2 }$ .DO MIGHT BE GOOD.DEFAULTS WORK(5) $\mathbf { \equiv } 1$ .DO，WORK(6) $\mathbf { \equiv } 1$ .2D0.  
WORK(7) MAXIMAL STEP SIZE， DEFAULT XEND- $\pmb { \check { \check { \Lambda } } }$   
WORK(8)， WORK(9）PARAMETERS FOR STEP SIZE SELECTIONTHE NEW STEP SIZE IS CHOSEN SUBJECT TO THE RESTRICTIONWORK(8） $\Leftarrow$ HNEW/HOLD $\bullet =$ WORK(9)DEFAULT VALUES: WORK(8) $\mathtt { = 0 }$ .2D0，WORK(9) $= 8$ .D0OUTPUT PARAMETERSX X-VALUE FOR WHICH THE SOLUTION HAS BEEN COMPUTED（AFTER SUCCESSFUL RETURN $\tt X = \tt X$ END).Y(N) NUMERICAL SOLUTION AT XH PREDICTED STEP SIZE OF THE LAST ACCEPTED STEPIDID REPORTS ON SUCCESSFULNESS UPON RETURN:IDID= 1 COMPUTATION SUCCESSFULIDID= 2 COMPUT. SUCCESSFUL (INTERRUPTED BY SOLOUT)$\mathtt { T D T D = - 1 }$ INPUT IS NOT CONSISTENT,$\mathtt { T D T D } = - 2$ LARGER NMAX IS NEEDED,$I D I D = - 3$ STEP SIZE BECOMES TOO SMALL,IDID=-4 MATRIX IS REPEATEDLY SINGULAR.

<table><tr><td>C</td><td>IWORK(14）</td><td>NFCN</td><td>NUMBER OF FUNCTION EVALUATIONS</td><td></td><td>（THOSE FOR NUMERICAL</td></tr><tr><td>C</td><td></td><td></td><td> EVALUATION OF THE JACOBIAN ARE NOT COUNTED)</td><td></td><td>(EITHER ANALYTICALLY</td></tr><tr><td>C</td><td>IWORK（15）</td><td>NJAC</td><td>NUMBER OF JACOBIAN EVALUATIONS</td><td></td><td></td></tr><tr><td>C</td><td></td><td></td><td>OR NUMERICALLY)</td><td></td><td></td></tr><tr><td>C</td><td>IWORK（16）</td><td>NSTEP</td><td>NUMBER OF COMPUTED STEPS</td><td></td><td></td></tr><tr><td>C</td><td>IWORK（17）</td><td>NACCPT</td><td>NUMBER OF ACCEPTED STEPS</td><td></td><td></td></tr><tr><td>C</td><td>IWORK(18)</td><td>NREJCT</td><td>NUMBER </td><td> OF REJECTED STEPS (DUE TO ERROR TEST）,</td><td></td></tr><tr><td>C</td><td></td><td></td><td></td><td>(STEP REJECTIONS IN THE FIRST STEP ARE NOT COUNTED)</td><td></td></tr><tr><td>C</td><td>IWORK(19)</td><td>NDEC</td><td></td><td>NUMBER OF LU-DECOMPOSITIONS OF BOTH MATRICES</td><td></td></tr><tr><td>C</td><td>IWORK（20）</td><td>NSOL</td><td></td><td>NUMBER OF FORWARD-BACKWARD SUBSTITUTIONS， OF BOTH</td><td></td></tr><tr><td>C</td><td></td><td></td><td></td><td>SYSTEMS; THE NSTEP FORWARD-BACKWARD SUBSTITUTIONS,</td><td></td></tr><tr><td>C</td><td></td><td></td><td></td><td>NEEDED FOR STEP SIZE SELECTION， ARE NOT COUNTED</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# Subroutine RADAUP

With the option IWORK $( 1 1 ) \ = \ 3$ this code is mathematically equivalent to RADAU5. The only difference is that explicit sums have been replaced by loops, and that the coefficients of the method have been put into arrays. This makes the code a little bit slower (in particular for small problems), but has the advantage that the coefficients of the method can be easily changed. At the moment, the coefcients of the Radau IIA methods of orders 5, 9,and 13 are available by setting IwoRk(11） equal to 3, 5,and 7, respectively. The calling list is the same as for RADAU5.

SUBROUTINE RADAUP(N,FCN,X,Y,XEND,H,   
+ RTOL,ATOL,ITOL,   
+ JAC ,IJAC,MLJAC,MUJAC,   
+ MAS ,IMAS,MLMAS,MUMAS,   
+ SOLOUT,IOUT,   
+ WORK ,LWORK,IWORK,LIWORK,RPAR,IPAR,IDID)

# Subroutine RODAS

This is an implementation of the Rosenbrock method described in Section VI.3.It also satisfies the algebraic order conditions and can thus be applied to differentialalgebraic problems of index 1. The calling list is:

SUBROUTINE RODAS(N,FCN,IFCN,X,Y,XEND,H,   
$\star$ RTOL,ATOL,ITOL,   
$\mathbf { + }$ JAC ,IJAC,MLJAC,MUJAC,DFX,IDFX,   
$\mathbf { + }$ MAS ,IMAS,MLMAS,MUMAS,   
$\star$ SOLOUT,IOUT,   
+ WORK,LWORK,IWORK,LIWORK,RPAR,IPAR,IDID)

Compared to RADAU5 we have three additional parameters. IFcn indicates whether the right-hand side $f ( x , y )$ of the problem (A.1) is independent of $\boldsymbol { x }$ or not. In the case that $f$ depends on $\boldsymbol { x }$ ， the code needs the partial drivative $\partial f / \partial x$ .This can be provided numerically (set IDFx $\qquad = \ 0$ and supply a dummy subroutine for DFx) or analytically. In the latter case, one has to set IDFx $\textbf { = 1 }$ and one has to supply a subroutine computing $\partial f / \partial x$ . Of course, the meaning of the woRk and IwORK parameters are not all the same as for RADAU5. They are decscibed in the comments of the code.

# Subroutine SEULEX

This is an extrapolation code based on the linearly implicit Euler method (Sections IV.9 and VI.4). A dense output has been included in cooperation with A. Ostermann. The meaning of the input parameters is the same as for RODAs. The woRK and IwoRk parameters are decscibed in the comments of the code.

<table><tr><td>SUBROUTINE SEULEX(N,FCN,IFCN,X,Y,XEND,H,</td></tr><tr><td>+ RTOL,ATOL,ITOL,</td></tr><tr><td>+ JAC ,IJAC,MLJAC,MUJAC,</td></tr><tr><td>MAS,IMAS,MLMAS,MUMAS, +</td></tr><tr><td>+ SOLOUT,IOUT, WORK,LWORK,IWORK,LIWORK,RPAR,IPAR,IDID) +</td></tr></table>

# Problems with Special Structure

If the first $m _ { 1 }$ equations of (A.1) are of the form

$$
y _ { \imath } ^ { \prime } = y _ { \imath + m _ { 2 } } \qquad \mathrm { f o r } \quad i = 1 , \ldots , m _ { 1 }
$$

with $m _ { 1 }$ being an integer multiple of $m _ { 2 }$ , and the remaining equations do not de-pend explicitly on $y _ { m _ { 1 } + 1 } ^ { \prime } , \ldots , y _ { n } ^ { \prime }$ , it is recommended to set the parameters IWoRK(9) and IWORk(10） equal to $m _ { 1 }$ and $m _ { 2 }$ ，respectively. This implies a more efficient treatment of the arising linear systems and is,in particular, advantageous for a large value of $m _ { 1 }$

If IwoRk(9） is set to a nonzero value, care has to be taken with the definition of the subroutines JAc and MAs. Only the nontrivial part of the Jacobian (i.e., the rows with indices $m _ { 1 } + 1 , \ldots , n )$ have to be computed and stored in an array of dimension $( n - m _ { 1 } ) \times n$ . Similarly, only the right lower block (of dimension $n - m _ { 1 } )$ of the matrix $M$ has to be defined in the subroutine MAs.However, the subroutine FcN must contain the definition of all components of $f ( x , y )$ , in particular also the statement $\mathtt { F } ( \mathtt { I } ) \ = \ \mathtt { Y } \left( \mathtt { I } \mathtt { + } \mathtt { M } 2 \right)$ for $\mathbf { I = 1 } , \ldots , \mathbb { M } 1$ . Banded options are still possible. Typical situations, where (A.2) arises,are the following:

${ \pmb y } ^ { \prime \prime } = { \pmb f } ( { \pmb x } , { \pmb y } , { \pmb y } ^ { \prime } )$ . With the new variable $z = y ^ { \prime }$ the system becomes

$$
\begin{array} { l } { { y ^ { \prime } = z } } \\ { { z ^ { \prime } = f ( x , y , z ) , } } \end{array}
$$

which is of the form (A.1). If $\boldsymbol { y } \in \mathbb { R } ^ { m }$ ,both parameters IwoRk(9） and IWORK(10) have to be set equal to $m$ . Banded option can be used, if both $\partial f / \partial y$ and $\partial f / \partial y ^ { \prime }$ are banded.

$C ( x , y ) y ^ { \prime } { = } f ( x , y )$ . Again we introduce $z = y ^ { \prime }$ , so that this problem becomes equivalent to

$$
\begin{array} { l } { { y ^ { \prime } = z } } \\ { { 0 = C ( x , y ) z - f ( x , y ) . } } \end{array}
$$

Both parameters IwoRk(9） and IwoRk(1o） have to be set equal to the dimension of $y$ . If only a few components of $y ^ { \prime }$ are multiplied by non-constant terms, then it may be more efficient to introduce new variables only for these components.

$C ( x , y ) y ^ { \prime \prime } { } = f ( x , y , y ^ { \prime } )$ . With the new variables $z = y ^ { \prime }$ and $u = z ^ { \prime } = y ^ { \prime \prime }$ ， this problem can be written in the form (A.1) as follows

$$
\begin{array} { r c l } { { } } & { { } } & { { y ^ { \prime } = z } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { z ^ { \prime } = u } } \\ { { } } & { { } } & { { 0 = C ( x , y ) u - f ( x , y , z ) . } } \end{array}
$$

Here $m _ { 2 }$ is equal to the dimension of $y$ ,and $m _ { 1 } = 2 m _ { 2 }$

# Use of SOLOUT and of Dense Output

The subroutine SOLOUT, supplied by the user, is called after every accepted step and provides the solution over the whole step (dense output). This possibility can be used for tabulating the solution at prescribed output points (see the driver for RADAU5 above) or for graphical presentation of the solution. Further applications are the following:

Event location. Suppose we want to determine $\boldsymbol { x }$ such that $g ( x , y ( x ) ) = 0$ , where $y ( x )$ is the solution of (A.1). During integration one can check in the subroutine SOLOUT whether the values $g ( x _ { \imath - 1 } , y _ { \imath - 1 } )$ and $g ( x _ { \imath } , y _ { \imath } )$ change sign. If this occurs,the dense output (which is available for all of our codes) can be used to localize the zero of $g { \big ( } x , y ( x ) { \big ) }$ ． This procedure is very useful for problems with discontinuous right-hand side (see Sect.II.6).

Projection. An efcient way for solving higher index differential-algebraic equa-tions is index-reduction combinded with projection. If one applies a stiff (or non-stiff) code straightforwardly to an index-reduced problem, the obtained numerical solution will suffer from the so-called “drift-off" effect. In order to avoid this driftoff, it is recommended to project the numerical solution after every step onto the solution manifold of the problem. This can be conveniently done with help of the subroutine SOLOUT.

# Bibliography

This bibliography includes the publications referred to in the text. Italic numbers in square brackets following a reference indicate the sections where the reference is cited.

R.Abraham,J.E.Marsden & T.Ratiu (1983): Manifolds,Tensor Analysis,and Applications. Applied Mathematical Sciences vol. 75, Springer-Verlag 1983； second edition 1988, 654 pp. [VII.1]   
M.Abramowitz & I.A. Stegun (1964): Handbook of mathematical functions. Dover,1000 pages. [IV.2], [IV.4], [IV.12], [IV.13], [IV.14]   
C.A. Addison (1979): Implementing a stiff method based upon the second derivative formulas. Techn. Rep.130/79,Dept. of Comput. Sc., Univ. of Toronto, Canada. [V.3], [V.5]   
R.C.Aiken ed. (1985): Stiff computation. Oxford, Univ. Press, 462pp. [IV.1], [IV.3], [IV.8], [V.5]   
G. Akilov, see L. Kantorovich & G. Akilov.   
R. Alexander (1977): Diagonally implicit Runge-Kutta methods for stiff O.D.E.'s. SIAM J. Numer. Anal., vol. 14, pp. 1006-1021. [IV.3], [IV.6]   
R. Alexander (1997): Reliability of software for stiff initial value problems. To appear in SIAMJ. Sci. Comput. [IV.10]   
T.Alishenas (1992): Zur numerischen Behandlung， Stabilisierung durch Projektion und Modellierung mechanischer Systeme mit Nebenbedingungen und Invarianten. Dissertation, Stockholm, TRITA-NA-9202. [VII.2]   
T. Alishenas & O. Olafsson (1994): Modeling and velocity stabilization of constrained mechanical systems. BIT, vol. 34, pp. 455-483. [VII.2]   
R. Alt (1971): Methodes A-stables pour l'intégration de systemes différentiels mal conditionnés. These, Univ. Paris VI. [IV.6]   
H.C. Andersen (1983): Rattle: a “velocity"version of the Shake algorithm for molecular dynamics calculations. J. Comput. Phys., vol. 52, pp. 24-34. [VI1.8]   
G.C. Andrews,see also M.K. Ormrod & G.C. Andrews.   
C.Arévalo,C.Fuhrer & G.Soderlind (1996): Stabilized multistep methods for index 2 Euler-Lagrange DAEs. BIT, vol. 36, pp. 1-13. [VII.6]   
S.Arimoto, see J. Nagumo, S. Arimoto & S. Yoshizawa.   
M. Arnold (1993): Stability of numerical methods for differential-algebraic equations of higher index. Applied Numerical Mathematics, vol. 13, pp. 5-14. [Vl.1]

M.Arnold (1995): Half-explicit Runge-Kutta methods with explicit stages for differentialalgebraic systems of index 2. Submitted for publication. [Vi1.6], [VI1.7]

V.I. Arnol'd (1979): Matematiceskie metody klassiceskoi mechaniki. Nauka, Moskva; English translation: Springer Verlag 1984,1989. [VII.1]

W.E. Arnoldi (1951): The principle of minimized iterations in the solution of the matrix eigenvalue problem. Quart. Appl. Math., vol. 9, pp. 17-29. [IV.10]

U. Ascher (1989): On numerical diferential algebraic problems with application to semiconductor device simulation. SIAM J. Numer. Anal., vol. 26, pp.517-538. [VI1.4]

U. Ascher & G. Bader (1986): Stability of collocation at Gaussian points. SIAM J. Numer. Anal., vol. 23, pp. 412-422. [IV.13]

U.M. Ascher, H. Chin & S. Reich (1994): Stabilization of DAEs and invariant manifolds. Numer. Math., vol. 67, pp.131-149. [VII.2]

U.Ascher & L.R.Petzold (1991): Projected implicit Runge-Kutta methods for diffrentialalgebraic equations. SIAM J. Numer. Anal., vol. 28, pp. 1097-1120. [VII.4]

M.Athans & P.L.Falb (1966): Optimal Control. McGraw-Hill Book Company, New York, 879pp. [VII.]

W. Auzinger, R. Frank,& F. Macsek (1990): Asymptotic error expansions for stiff equations: the implicit Euler scheme. SIAM J. Numer. Anal., vol. 27, pp. 67-104. [VI.5]

O. Axelsson (1969): A class of A-stable methods.BIT,vol. 9,pp. 185-199. [IV.3], [IV.5]

O. Axelsson (1972): A note on a class of strongly A-stable methods. BIT, vol. 12, pp. 1-4. [IV.5]

G.Bader & P. Deuflhard (1983): A semi-implicit mid-point rule for stiff systems of ordinary differential equations. Numer. Math., vol. 41, pp. 373-398. [IV.9], [IV.10], [VII.6]

G.Bader, see also U.Ascher & G.Bader;E.Hairer, G.Bader& Ch.Lubich.

C. Baiocchi & M. Crouzeix (1989): On the equivalence of A-stability and G-stability. Appl. Numer. Math., vol.5, pp. 19-22. [V.6]

M. Bakker (1971): Analytical aspects of a minimax problem (Dutch), Technical Note TN 62, Mathematical Centre, Amsterdam.

L.A. Bales, O.A. Karakashian & S.M. Serbin (1988): On the Ao -acceptability of rational approximations to the exponential function with only real poles.BIT, vol. 28,pp. 70-79. [IV.4]

G.P. Barker, A. Berman & R.J. Plemmons (1978): Positive diagonal solutions to the Lya-punov equations. Linear and Multilinear Algebra, vol. 5, pp. 249-256. [IV.14]

J. Baumgarte (1972): Stabilization of constraints and integrals of motion in dynamical systems. Comp. Meth. Appl. Mech. Eng., vol. 1, pp. 11-16. [VII.2]

G.Benetin & A. Giorgili (1994): On the Hamilonian interpolation of near to the identity symplectic mappings with application to symplectic integration algorithms. J. Statist. Phys.,vol. 74,pp. 1117-1143.[VII.8]

H.J.C.Berendsen, see also J.-P. Ryckaert, G. Ciccotti & H.J.C. Berendsen.

A.Berman, see G.P. Barker, A. Berman & R.J. Plemmons.

S.Bernstein (1914): Sur la definition et les propriétés des fonctions analytiques d'une variable réelle. Math. Annalen, vol. 75, pp. 449-468. [IV.11]

S.Bernstein (1928): Sur les fonctions absolument monotones. Acta Mathematica, vol. 51, pp. 1-66. [IV.11]

M. Berzins & R.M. Furzeland (1985): A user's manual for SPRINT- a versatile software package for solving systems of algebraic, ordinary and partial diferential equations: part 1-algebraic and ordinary diffrential equations. Thornton Research Centre, Shell Research Ltd. TNER.85.058. [V.5], [VII.3]

T.A. Bickart (1977): An eficient solution process for implicit Runge-Kutta methods. SIAM J. Numer. Anal., vol.14,1022-1027. [iV.8]

T.A.Bickart & W.B.Rubin (1974): Composite multistep methods and stiff stability. In: Stiff Differential Systems,R.A. Willoughby (ed.), Plenum Press,New York. {V.3]

T.A. Bickart, see also H.M. Sloate & T.A. Bickart.

G.Birkhoff & R.S. Varga (1965): Discretization errors for well-set Cauchy problems, I. J. Math. Phys., vol. 44, pp. 1-23. [IV.5]

A.Bjorck (1983): A block QR algorithm for partitioning stiff differential systems. BIT, vol. 23, pp. 329-345. [IV.10]

A. Bjorck (1984): Some methods for separating stiff components in initial value problems. In: Numerical Analysis, Dundee 1983,D.F Griffiths,ed., Lecture Notes in Math. 1066, Springer Verlag, pp.30-43. [IV.10]

C.Bolley & M. Crouzeix (1978): Conservation de la positivité lors de la discretisation des problemes d'évolution paraboliques. R.A.I.R.O. Analyse numérique, vol. 12, pp. 237- 245. [IV.11]

V.G.Boltyanskii, see L.S.Pontryagin, V.G. Boltyanski,R.V. Gamkrelidze & E.F. Mishchenko.

V.Brasey (1992): A half-explicit Runge-Kutta method of order 5 for solving constrained mechanical systems. Computing, vol. 48, pp. 191-201. [VI1.6]

V.Brasey (1994): Half-explicit method for semi-explicit differential-algebraic equations of index 2. These N°2664, Sect. Math., Univ. de Geneve. [VI1.7]

V.Brasey & E. Hairer (1993): Half-explicit Runge-Kutta methods for differential-algebraic systems of index 2. SIAM J. Numer. Anal., vol. 30, pp. 538-552. [VI1.6]

K.E. Brenan (1983): Stability and convergence of diference approximations for higher-index diferential-algebraic systems with applications in trajectory control. Doctoral thesis, Dep. Math., Univ. of California,Los Angeles. [VII.1]

K.E.Brenan, S.L. Campbell & L.R. Petzold (1989): Numerical solution of initial-value problemsinfeenialgebicions.rthHlland,wYork,p.l.1], [VII.3], [VI1.7]

K.E. Brenan & L.R. Engquist (1988): Backward diferentiation approximations of nonlinear differential/algebraic equations,and Supplement. Math. Comp.， vol. 51, pp. 659-676, pp. S7-S16. [VII.3]

K.E.Brenan & L.R. Petzold (1989): The numerical solution of higher index differential-/algebraic equations by implicit Runge-Kutta methods. SIAM J. Numer. Anal., vol. 26, pp. 976-996. [VII.4]

PN.Brown,G.D.Byrne & A.C. Hindmarsh (1989): VODE: a variable coefficient ODE solver. SIAMJ. Sci. Stat. Comput., vol. 10, pp. 1039-1051. [V.5]

T.D. Bui, see P. Kaps, S.W.H. Poon & T.D. Bui.

J.M.Burgers (1948): A mathematical model illustrating the theory of turbulence. Advances in appl. mech., vol. 1, pp.171-199. [V.8], [VI.6]

K. Burrage (1978): High order algebraically stable Runge-Kutta methods. BIT, vol. 18, pp. 373-383. [IV.5], [IV.13]

K.Burrage (1978): A special family of Runge-Kutta methods for solving stiff differential equations. BIT, vol. 18, pp. 22-41. [IV.5], [IV.6], [IV.8]

K.Burrage (1982): Efficiently implementable algebraically stable Runge-Kutta methods. SIAMJ. Numer. Anal., vol. 19, pp. 245-258. [IV.13]

K.Burrage (1987): High order algebraically stable multistep Runge-Kutta methods. SIAM J. Numer. Anal., vol. 24, pp. 106-115. [V.9]

K.Burrage (1988): Order properties of implicit multivalue methods for ordinary differential equations. IMA J. Numer. Anal., vol. 8, pp. 43-69. [V.9]

K.Burrage & J.C.Butcher (1979): Stability criteria for implicit Runge-Kutta methods. SIAM J. Numer. Anal., vol. 16, pp. 46-57. [IV.12]

K.Burrage & J.C. Butcher (198O): Non-linear stability of a general class of differential equation methods. BIT, vol. 20, pp. 185-203. [IV.12], [V.9]

K.Burrage, J.C. Butcher & FH. Chipman (198O): An implementation of singly-implicit Runge-Kutta methods.BIT, vol. 20, pp. 326-340. [IV.8]

K.Burrage & W.H.Hundsdorfer (1987): The order of B -convergence of algebraically stable Runge-Kutta methods. BIT, vol. 27, pp. 62-71. [IV.15]

J.C. Butcher (1964): Implicit Runge-Kutta processes. Math. Comput., vol. 18, pp. 50-64. [IV.5]

J.C. Butcher (1964): Integration processes based on Radau quadrature formulas. Math. Comput., vol. 18, pp. 233-244. [IV.5]

J.C.Butcher (1975): A stability property of implicit Runge-Kutta methods. BIT, vol. 15, Pp. 358-361. [IV.12]

J.C.Butcher (1976): On the implementation of implicit Runge-Kutta methods.BIT, vol. 6, Pp. 237-240. [IV.8]

J.C.Butcher (1977): On A-stable implicit Runge-Kuta methods. BIT, vol.17, pp. 375-378. [IV.5]

J.C.Butcher (1979): A transformed implicit Runge-Kutta method. J. Assoc. Comput. Mach., vol. 26, pp. 731-738. [IV.8]

J.C.Butcher (1981): A generalization of singly-implicit methods. BIT, vol. 21, pp.175-189. [V3]

J.C.Butcher (1982): A short proof concerning $B$ -stability. BIT,vol.22,pp.528-529.[IV12]

J.C.Butcher (1987): Linear and non-linear stability for general linear methods. BIT,vol. 27, pp. 182-189. [V.9]

J.C.Butcher (1987): The equivalence of algebraic stability and AN-stability. BIT, vol. 27, pp. 510-533. [V9]

J.C.Butcher (1987): The numerical analysis of ordinary differential equations. Runge-Kutta and general linear methods. John Wiley & Sons, 512pp. [IV.12]

J.C.Butcher (1990): Order, stepsize and stiffness switching. Computing. vol 44,p.209-220. [IV.2]

J.C.Butcher, see also K. Burrage & J.C. Butcher; K.Burrage,J.C.Butcher & FH. Chipman.

G.D.Byrne & A.C. Hindmarsh (1975): A polyalgorithm for the numerical solution of ordinary differential equations. ACM Trans. Math. Software, vol. 1, pp. 71-96. [V.5]

G.D. Byrne & A.C. Hindmarsh (1987): Stiff ODE solvers: a review of current and coming attractions. J. of Comput. Physics, vol. 70, pp. 1-62. [IV.10]

G.D. Byrne, see also P.N. Brown, G.D. Byrne & A.C. Hindmarsh.

D.A. Calahan (1968): A stable, accurate method of numerical integration for nonlinear systems.Proc.IEEE, vol. 56, p. 744. [IV.7]

A. Callender, D.R. Hartree & A.Porter (1936): Time-lag in a control system. Phil. Trans. of the Royal Society (London), Series A, vol. 235, pp. 415-444. [IV.2]

M.P. Calvo, see also J.M. Sanz-Serna & M.P. Calvo.

S.L.Campbell(1982): Singular Systems of Differential Equations I1. Pitman,London. [VI1.1] S.L.Campbel (1989): A computational method for general higher index singular systems of diffrential equations. IMACs Transactions Scientific Computing, vol. 1.2, pp.555-560. [VI1.2]

S.L. Campbell(1993): Least squares completions for nonlinear differential algebraic equations. Numer. Math., vol. 65, pp. 77-94. [VII.2]

S.L Campbell (1995): High index differential algebraic equations. J. Mech. Struct. & Machines,vol. 23, pp.199-222. [VII.1]

S.L. Campbell & C.W. Gear (1995): The index of general nonlinear DAEs. Numer. Math., vol. 72, pp. 173-196. [VII.1]

S.L. Campbell & E. Moore (1995): Constraint preserving integrators for general nonlinear higher index DAEs. Numer. Math., vol. 69, pp. 383-399. [VIl.2]

S.L. Campbell, see also K.E. Brenan, S.L. Campbell & L.R. Petzold.

J. Carr, D.B. Duncan & C.H. Walshaw (1995): Numerical approximation of a metastable system. IMA J. Numer. Anal., vol. 15, pp. 505-521. [IV.10]

JR. Cash (1976): Semi-implicit Runge-Kutt procedures with eror estimates for the numerical integration of stiff systems of ordinary differential equations. JACM, vol. 23, pp. 455-460. [IV.7]

J.R.Cash (1979): Diagonally implicit Runge-Kutta formulae with error estimates. J. Inst. Math. Applics, vol. 24, pp. 293-301. [IV.6]

J.R. Cash (1979): Stable recursions, with applications to the numerical solution of stiff systems. Academic Press,223 pp. [V.2]

J.R. Cash (1980): On the integration of stiff systems of O.D.E.s using extended backward differentiation formulae. Numer. Math., vol. 34, pp. 235-246. [V.3]

J.R.Cash (1981): Second derivative extended backward differentiation formulas for the numerical integration of of stiff systems. SIAM J. Numer. Anal. vol. 18, pp. 21-36. [V.3]

J.R. Cash (1983): The integration of stiff initial value problems in ODEs using modified extended backward differentiation formulas. Comp. & Maths. with Appls., vol. 9, No. 5, pp. 645-657. [V.3], [V.5]

J.R. Cash & S. Considine (1992): An MEBDF code for stiff initial value problems.ACM Tans. Math. Software,vol. 18, No.2, pp. 142-158. [V.5]

P.E.Chase (1962): Stability properties of Predictor-Corrector methods for ordinary differential equations, J. Assoc. Comput. Mach., vol. 9, pp.457-468. [V.1]

P.L. Chebyshev (Tchebychef) (1854): Theorie des mécanismes connus sous le nom de parallelogrammes.Mém. de 1'Acad. Imp. St.-Pétersbourg, tome VI (1854), pp.539-568; Oeuvres Tome I, pp.111-143. [IV.2]

H. Chin, see also U.M. Ascher, H. Chin & S. Reich.

F.H.Chipman (1971): A-stable Runge-Kuta processs.BIT,vol. 11, pp.384-388. [IV.5]

FH. Chipman (1976): A note on implicit A -stable RK methods with parameters. BIT, vol.16, pp. 223-227. [IV.5]

F.H. Chipman, see also K. Burrage, J.C.Butcher & FH. Chipman.

G. Ciccoti, see also J.-P. Ryckaert, G. Ciccoti & H.J.C. Berendsen.

K.Clark (1988): A structural form for higher index semistate equations I: Theory and ap-plications to circuit and control theory. Linear Alg. Appl., vol. 98, pp.169-197. [VI.i]

L. Collatz (195o): Numerische Behandlung von Diffrentialgleichungen. Grundlehren, Springer Verlag, Band LX (later editions and translations). [IV.10], [IV.15]

P. Collet, J.-P. Eckmann, H. Epstein & J. Stubbe (1993):Analyticity for the Kuramoto-Sivashinsky equation. Physica D, vol. 67, pp. 321-326. [IV.10]

S. Considine, see also J.R.Cash & S. Considine.

G.J. Cooper (1985): Reducible Runge-Kutt methods. BIT, vol.25,pp. 675-680. [IV.12]

G.J. Cooper(1986): On the existence of solutions for algebraically stable Runge-Kutta methods. IMA J. Numer. Anal., vol. 6, pp.325-330. [IV.14]

G.J. Cooper & A. Sayfy (1979): Semiexplicit A-stable Runge-Kutta methods. Math. of Comp., v0l. 33, pp. 541-556. [IV.6]

G.J. Cooper & A. Sayfy (1983): Additive Runge-Kutta methods for stiff ordinary differential equations. Math. of Comp., vol. 40, pp. 207-218. [IV.7]

R.Courant, K. Friedrichs & H.Lewy (1928): Ueber die partiellen Diffrenzengleichungen der mathematischen Physik. Math. Ann., vol. 100, pp. 32-74. [IV.2]

R.Courant, see A. Hurwitz & R. Courant.

G. Cramer (175O): Introduction a l'analyse des lignes courbes algebriques. Geneve, 1750. [V.3]

R.L. Crane & R.W. Klopfenstein (1965): A predictor-corrector algorithm with an increased range of absolute stability. J. ACM, vol. 12, pp.227-241. . [V.1]

M. Crouzeix (1975): Sur l'approximation des équations differentielles operationnelles liné- aires par de méthodes de Runge-Kutta. These, Univ. Paris VI. [IV.6]

M.Crouzeix (1979): Sur la $B$ -stabilité des methodes de Runge-Kutta. Numer.Math., vol. 32, pp. 75-82. [IV.12]

M. Crouzeix,W.H. Hundsdorfer & M.N. Spijker (1983): On the existence of solutions to the algebraic equations in implicit Runge-Kutta methods. BIT, vol. 23, pp. 84-91. [IV.14]

M. Crouzeix & P.A. Raviart (1976): Approximation des équations d'évolution lineaires par des methodes a pas multiples. C.R. Acad. Sc. Paris, Ser. A 283, pp. 367-370. [V.7]

M.Crouzeix & P.A. Raviart (1980): Approximation des problemes d'évolution. Unpublished Lecture Notes,Université de Rennes. [IV.6], [IV.14], [V.7]

M. Crouzeix & F. Ruamps (1977): On rational approximations to the exponential. R.A.I.R.O. Analyse Numérique, vol. 11, pp. 241-243. [IV.4]

M. Crouzeix, see also C.Baiocchi & M. Crouzeix; C.Bolley & M. Crouzeix.

C.W. Cryer (1973): A new class of highly stable methods. $A _ { 0 }$ -stable methods.BIT, vol. 13, pp.153-159. [V.2]

A.R. Curtis (1983): Jacobian matrix properties and their impact on choice of software for stiff ODE systems. IMA J. Numer. Anal., vol. 3, pp. 397-415. [IV.10]

C.F. Curtiss & J.O. Hirschfelder (1952): Integration of stiff equations.Proc. Nat. Acad. Sci., vol. 38, pp.235-243. [IV.1]

G.Dahlquist (1951): Fehlerabschitzungen bei Differenzenmethoden zur numerischen Inte-gration gewohnlicher Differentialgleichungen. ZAMM, vol. 31, pp. 239-240. [V.1]

G.Dahlquist (1956): Convergence and stability in the numerical integration of ordinary differential equations. Math. Scand., vol. 4, pp. 33-53. [V.7]

G.Dahlquist (1963): A special stability problem for linear multistep methods. BIT, vol. 3, pp. 27-43. [IV.3], [IV.9], [IV.12], [V.1], [V.6]

G. Dahlquist (1975): Error analysis for a class of methods for stiff nonlinear initial value problems. Numerical Analysis, Dundee 1975,Lecture Notes in Math.,No. 506, pp. 60- 74. [IV.12], [V.6]

G. Dahlquist (1978): $G$ -stability is equivalent to $A$ -stability. BIT,vol. 18,pp.384-401. [IV.13], [V.6]

G.Dahlquist (1978): Positive functions and some applications to stability questions for numerical methods. In: Recent Advances in Numerical Analysis, C. de Boor & G.H. Golub (eds.),Academic Press,New York, pp. 1-19. [IV.5]

G.Dahlquist (1983): On one-leg multistep methods. SIAMJ. Numer. Anal., vol. 20, pp.1130- 1138. [V.6], [V.7], [V.9]

G.Dahlquist &R.Jeltsch (1979): Generalized disks of contractivity for explicit and implicit Runge-Kutta methods. TRITA-NA Report 7906. [IV.12], [IV.13]

G.Dahlquist & R. Jeltsch (1987): Reducibility and contractivity of Runge-Kutta methods revisited. Report Nr. 46, Inst. f. Geometrie u. Prakt. Math., RWTH Aachen. [IV12]

G. Dahlquist, H. Mingyou & R. LeVeque (1983): On the uniform power-boundedness of a family of matrices and the applications to one-leg and linear multistep methods. Numer. Math., vol. 42, pp. 1-13. [V.7]

G. Dahlquist & G. Soderlind (1982): Some problems related to stiff nonlinear differential systems. In: Computing Methods in Applied Sciences and Engineering, V.R. Glowinski & J.L.Lions (eds.),North-Holland, INRIA [V.7]

G. Dahlquist, see also G. Soderlind & G. Dahlquist.

J.W. Daniel & R.E. Moore (1970); Computation and theory in ordinary diferential equa-tions,W.H. Freeman and Company, 172 pp. [V.4]

P.J. Davis (1963): Interpolation and approximation. Blaisdell 1963; Dover 1975. [V.3]

K.Dekker (1981): Stability of linear multistep methods on the imaginary axis.BIT,vol. 21, Pp. 66-79. [V.4]

K. Dekker (1982): On the iteration error in algebraically stable Runge-Kutta methods. Re-port NW 138/82, Math. Centrum, Amsterdam. [IV.14]

K.Deker (1984): Eror bounds for the solution to the algebraic equations in Runge-Kutta methods.BIT, vol. 24, pp. 347-356. [IV.14]

K.Dekker & E.Hairer (1985): A necessary condition for BSI-stability.BIT,vol.25,pp.285- 288. [IV.14]

K.Dekker, J.F.B.M. Kraaijevanger & J. Schneid (1990): On the relation between algebraic stability and B-convergence for Runge-Kutta methods. Numer. Math., vol. 57, pp.249- 262. [iv.15]

K. Dekker & J.G. Verwer (1984): Stability of Runge-Kutta methods for stiff nonlinear differential equations. North-Holland,Amsterdam-New-York-Oxford.[IV.12], [IV.14], [IV.15]

K. Dekker, see also M.Z. Liu, K. Dekker & M.N. Spijker.

P. Deuflhard (1983): Order and stepsize control in extrapolation methods. Numer. Math., vol. 41, pp. 399-422. [IV.9]

P.Deuflhard (1985): Recent progress in extrapolation methods for ordinary differential equations. SIAM Review, vol. 27, pp. 505-535. [IV.9]

P.Deuflhard,E. Hairer & J. Zugck (1987): One-step and extrapolation methods for diferential-algebraic systems. Numer. Math., vol. 51, pp. 501-516. [VI.5]

P.Deufhard & U.Nowak (1987): Extrapolation integrators for quasilinear implicit ODs In P.Deufard&BEngquist (eds.)，LagecaleSientificComputing.irkse Boston. [VI.5], [VI.6]

P.Deuflhard, see also G.Bader & P.Deuflhard.

G.A. Di Marzo (1992): RODAS5(4), methodes de Rosenbrock d'ordre 5(4) adaptees aux problemes diffrentiels-algebriques. Mémoire de diplome en Mathématiques, Universite de Geneve 1992. [IV.10], [VI.4]

J.R.Dormand & P.J. Prince (1980): A family of embedded Runge-Kutta formulae. J. Comp. Appl. Math., vol. 6, pp. 19-26. [IV.2]

A.A.Dorodnicyn (1947): Asymptotic solution of the van der Pol equation. Prikl. Mat. i Meh., vol. 11, pp. 313-328; Translations AMS, Ser. 1, vol. 4, pp. 1-23. [VI.1]

B.L. Ehle (1968) :High order A-stable methods for the numerical solution of systems of DEs. BIT, vol. 8, pp. 276-278. [IV.3], [IV.4], [IV.5]

B.L. Ehle (1969) :On Padé approximations to the exponential function and A-stable methods for the numerical solution of initial value problems. Research Report CSRR 2010, Dept. AACs, Univ. of Waterloo, Ontario, Canada. [IV.3], [IV.5]

B.L. Ehle (1973): A-stable methods and Padé approximations to the exponential. SIAM J. Math. Anal., vol. 4, pp. 671-680. [IV.4], [IV.5]

B.L. Ehle & Z. Picel (1975): Two-parameter, arbitrary order, exponential approximations for stiff equations. Math. Comput., vol. 29, pp.501-511. [IV.5]

E. Eich (1993): Convergence results for a coordinate projection method applied to mechanical systems with algebraic constraints. SIAM J. Numer. Anal., vol. 30, pp.1467-1482. [VI1.2]

R.England (1982): Some hybrid implicit stifflystable methods forordinarydiferential equa-tions. In: Numerical Analysis, Proc. Mexico, (ed. J.P. Hennart),Lecture Notes in Math., No. 909,Springer Verlag, pp. 147-158. [V.3]

L.R.Engquist, see K.E. Brenan & L.R.Engquist.

W.H.Enright (1974): Optimal second derivative methods for stiff systems. In: Stiff Differential Systems, ed. by R.A. Willoughby, Plenum Press,New York. (V.3]

W.H. Enright (1974): Second derivative multistep methods for stiff ordinary differential equations, SIAM J. Numer. Anal., vol. 11, pp. 321-331. [V.3]

W.H. Enright (1978): Improving the efciency ofmatrix operations in the numerical solution of stiff ordinary differential equations. ACM Trans. on Math. Software, vol. 4, pp. 127- 136. [IV.8]

W.H. Enright & TE. Hull (1976): Comparing numerical methods for the solution of stiff systems of ODEs arising in chemistry. In: Numerical methods for differential systems, recent developments in_algorithms, software and applications,L.Lapidus & W.E. Schiesser, Eds.,Academic Press, New York,1976, pp. 45-66. [IV.10]

W.H. Enright, T.E. Hull & B.Lindberg (1975): Comparing numerical methods for stiff systems of ODEs.BIT, vol. 15, pp. 10-48. [IV.10]

W.H. Enright & M.S. Kamel (1979): Automatic partitioning of stiff systems and exploiting the resulting structure. ACM TOMS, vol. 5, pp. 374-385. [IV.10]

M.A. Epton, see R.F. Sincovec, A.M. Erisman, E.L. Yip & M.A. Epton.

A.M. Erisman, see R.F Sincovec, A.M. Erisman, E.L. Yip & M.A. Epton.

L. Euler (1737): De fractionibus continuis dissertatio. Comm. acad. sc. Petrop., vol.9. pp. 98-137; Opera Omnia vol. XIV, pp. 187-215 (vide $\ S 7$ . [IV.13]

L.Euler (1752): Elementa doctrinae solidorum. Nov. comm. acad. sci. Petropolitanae vol. 4, p. 109-140; Opera Omnia vol. XXVI, pp. 71-93. [IV.4]

P.L.Falb, see M. Athans & P.L.Falb.

L.Fejer (1933): Mechanische Quadraturen mit positiven Coteschen Zahlen. Math. Zeitschrift, vol. 37, pp. 287-309. [IV.13]

A.Feng, C.D. Holland & S.E. Gallun (1984): Development and comparison of a generalized semi-implicit Runge-Kutta method with Gear's method for systems of coupled differential and algebraic equations. Comp. & Chem. Eng., vol. 8, pp. 51-59. (VI.4]

J.Field& R.M. Noyes (1974); Oscillations in chemical systems.IV: Limit cycle behavior in a model of a real chemical reaction. J. Chem. Phys., vol. 60, pp. 1877-1884. [IV.10]

R.Frank,J. Schneid & C.W. Ueberhuber (1981): The concept of $B$ -convergence. SIAM J. Numer. Anal., vol.18, pp. 753-780. [IV.15]

R.Frank,J. Schneid & C.W. Ueberhuber (1985): Stability properties ofimplicit Runge-Kutta methods. SIAM J. Numer. Anal., vol. 22, pp. 497-514. [IV.14], [IV.15]

R.Frank, J. Schneid & C.W. Ueberhuber (1985): Order results for implicit Runge-Kutta methods applied to stif systems. SIAM J. Numer. Anal., vol. 22, pp. 515-534. [IV.14], [IV.15]

R.Frank, see also W. Auzinger, R.Frank,& F.Macsek.

J.N.Franklin (1959): Numerical stability in digital and analogue computation for diffusion problems. J. Math. Phys., vol 37, pp. 305-315. [IV.2]

A.Friedli (1978): Verallgemeinerte Runge-Kutta Verfahren zur Losung steifer Diffrentialgleichungssysteme. Oberwolfach Conference 1976,Lecture Notes in Math. 631, pp. 35- 50. [IV.11]

K. Friedrichs, see R. Courant, K. Friedrichs & H. Lewy.

C.Fuhrer (1988): Differential-algebraische Gleichungssysteme in mechanischen Mehrkirpersystemen: Theorie, numerische Ansitze und Anwendungen. Doctoral thesis, Technische Universitat Minchen [VI.2].

C.Fuhrer & B.J.Leimkuhler (1991): Numerical solution of differential-algebraic equations for constrained mechanical motion. Numer. Math., vol. 59, pp. 55-69. [VIl.2]

C.Fuhrer, see also C. Arévalo, C. Fuhrer & G. Soderlind.

H.Fujita & T. Kato (1964): On the Navier-Stokes initial value problem. I. Arch. Rat. Mech. Anal.,vol. 16, pp. 269-315. [V.8]

R.M.Furzeland, see M. Berzins & R.M. Furzeland.

B.G. Galerkin (1915): Series expansions for some cases of equilibria of plates and beams (Russian). Vestnik Ingenerov Petrograd, H.10. [IV 10]

S.E. Gallun, see A. Feng, C.D. Holland & S.E. Gallun.

R.V. Gamkrelidze,see L.S. Pontryagin, V.G.Boltyanski,R.V. Gamkrelidze & E.F. Mishchenko.

F.R. Gantmacher (1954): Teorya Matrits. Two volumes, Gosudarstv. Izdat. Techn.-Teor. Lit., Moscva 1953； translations: Chelsea NY 1959, Interscience NY and London 1959,D. Verl.d.Wiss. Berlin 1958/59,Dunod Paris 1966. [VI1.1]

C.W. Gear (1971): Numerical initial value problems in ordinary diffrential equations, Prentice Hall,253 pp. [V.2], [V.5]

C.W. Gear (1971): Simultaneous numerical solution of differential-algebraic equations. IEEE Trans. Circuit Theory, vol. CT-18, pp. 89-95. [VI.2]

C.W.Gear (1982): Automaticdetection and treatment ofoscilltory andor stiffodinary differential equations. In: Numerical integration of differential equations, Lecture Notes in Math., vol. 968, pp.190-206. [IV.1]

C.W. Gear (1988): Diffrential-algebraic equation index transformations. SIAM J. Sci. Stat. Comput., vol. 9, pp. 39-47. [VII.4]

C.W. Gear (199o): Diferential-algebraic equations, indices, and integral algebraic equations. SIAM J. Numer. Anal., vol. 27. [VII.1]

C.W.Gear, G.KGupta & BLeimkuhler (1985): Automatic integrationof Euler-Lagrange equations with constraints.J.Comp.Appl.Math.,vol.12&13,pp.77-90.[VI.1], [VI1.3], [VI1.7]

C.W. Gear, H.H. Hsu &L. Petzold (1981): Differential-algebraic equations revisited. Proc. Numerical Methods for Solving Stif Initial Value Problems, Oberwolfach,BRD. [VII.3]

C.W. Gear & L.R. Petzold (1983): Differential/algebraic systems and matrix pencils. In: Matrix Pencils, B. Kagstrom & A. Ruhe (eds.),Lecture Notes in Math. 973, Springer Verlag, pp.75-89. [VII.1]

C.W. Gear & L.R. Petzold (1984): ODE methods for the solution of differential/algebraic systems. SIAM J. Numer. Anal., vol. 21, pp. 716-728. [VII.1], [VII.3]

C.W. Gear & Y. Saad (1983): Iterative solution of linear equations in ODE codes. SIAM J. Sci. Stat. Comput., vol. 4, pp. 583-601. [IV.10]

C.W. Gear, see also S.L. Campbell & C.W. Gear.

E.Gekeler (1979): Uniform stability of linear multistep methods in Galerkin prodecures for parabolic problems. J. Math. Sciences, vol. 2, pp. 651-667. [V.7]

E.Gekeler (1984): Discretization Methods for Stable Initial Value Problems.Lecture Notes in Math., No. 1044, Springer Verlag. [V.7]

Y. Genin (1974): An algebraic approach to A-stable linear multistep-multiderivative inte-gration formulas. BIT, vol. 14, pp. 382-406. [V.4]

D.R.A. Giles (1978): A comparison of three problem-oriented simulation programs for dynamic mechanical systems. Thesis, Univ. Waterloo, Ontario. [VIl.7]

A. Giorgilli, see also G.Benettin & A. Giorgili.

G.H. Golub & C.F. Van Loan (1989): Matrix Computations. Second edition, John Hopkins Univ. Press, Baltimore and London. [VII.1]

B.A. Gottwald (1977): MISS- Ein einfaches Simulations-System fir biologische und chemische Prozesse, EDV in Medizin und Biologie, vol. 3, pp. 85-90. [IV.10]

A.R. Gourlay (197O): A note on trapezoidal methods for the solution of initial value problems. Math. of Comp., vol. 24, pp. 629-633. [IV.3]

J.A. van de Griend &JFB.M. Kraaijevanger (1986): Absolute monotonicityof rational fonc-tions occuring in the numerical study of initial value problems. Numer. Math. vol. 49, pp. 413-424. [IV.11]

E. Griepentrog & R. M'rz (1986): Differential-algebraic equations and their numerical treatment. Teubner Texte zur Math.,Band 88. [VI.1], [VII.1], [VII.3]

R.D.Grigoieff(197): Numerik ewohnlicherifferentalgleichungen,d.2,eshiverfahren. Teubner Studienbucher, 411 Seiten“mit 49 Figuren, 32 Tabellen und zahlreichen Beispielen". [V.1]

R.D. Grigorieff & J. Schroll (1978): Uber $A ( \alpha )$ -stabile Verfahren hoher Konsistenzordnung. Computing, vol. 20, pp. 343-350. [V.2]

A. Guillou & B. Lago (1961): Domaine de stabilité associé aux formules d'integration numérique d'équations différentielles,a pas séparés et d pas liés. Recherche de formules a grand rayon de stabilité.ler Congr. Assoc.Fran. Calcul, AFCAL,Grenoble, Sept.1960, pp. 43-56. [IV.2]

A. Guillou & J.L. Soulé (1969): La résolution numérique des problemes différentiels aux conditions initiales par des methodes de collocation. R.1.R.O., vol. R-3, pp. 17-44. [V.3]

G.K. Gupta, see C.W. Gear, G.K. Gupta & B.Leimkuhler.

K. Gustafsson (1991): Control theoretic techniques for stepsize selection in explicit Runge-Kutta methods. ACM Trans. Math. Soft., vol.17, pp. 533-554. [IV.2]

K.Gustafsson (1994): Control-theoretic techniques for stepsize selection in implicit Runge-Kuta methods. ACM Trans. Math. Soft., vol. 20, pp. 496-517. [IV.8]

K. Gustafsson, M. Lundh & G. Soderlind (1988): A PI stepsize control for the numerical solution of ordinary differential equations. BIT, vol. 28, pp. 270-287. [IV.2]

E.Hairer (1980: Highest possible order of algebraically stable diagonally implicit Runge-Kuta methods. BIT, vol. 20, pp. 254-256. [IV.13]

E. Hairer (1982): Constructive characterization of $A$ -stable approximations to exp z and its connection with algebraically stable Runge-Kutta methods. Numer. Math.,vol. 39, pp. 247-258. [IV.5]

E. Hairer (1986): A- and $B$ -stability for Runge-Kutta methods - characterizations and equivalence. Numer.Math., vol. 48, pp. 383-389. [IV.13]

E. Hairer (1994): Backward analysis of numerical integrators and symplectic methods. Annals of Numer. Math., vol.1,pp.107-132. [VI1.8]   
E.Hairer, G. Bader & Ch. Lubich (1982): On the stability of semi-implicit methods for ordinary diffrential equations. BIT,vol. 22, pp. 211-232. [IV.9], [Iv.11]   
E.Hairer & Ch.Lubich (1988): Extrapolation at stiff differential equations. Numer. Math., vol. 52, pp. 377-400. [VI.5]   
E.Hairer & Ch.Lubich (1988b): On extrapolation methods for stiff and differential-algebraic equations. Teubner Texte zur Mathematik, Band 104, Teubner,Leipzig, pp. 64-73. [VI.5]   
E.Hairer & Ch. Lubich (1996): The life-span of backward error analysis for numerical integrators. Numer. Math. [VI1.8]   
E.Hairer, Ch.Lubich & M. Roche (1988): Eror of Runge-Kuta methods for stiff problems studied via differential algebraic equations. BIT, vol. 28, pp. 678-70o. [VI.3]   
E. Hairer,Ch.Lubich & M. Roche (1989): Error of Rosenbrock methods for stiffproblems studied via differential algebraic equations. BIT, vol. 29, pp. 77-90. [V1.3]   
E.Hairer, Ch. Lubich & M. Roche (1989): The numerical solution of differential-algebraic systems by Runge-Kutta methods (abbreviated as HLR89). Lecture Notes in Math. 1409, Springer Verlag. [VI.1], [VII.1], [VII.3], [VII.4], [VII.5],[VII.7]   
E. Hairer & A. Ostermann (1990): Dense output for extrapolation methods. Numer. Math., vol. 58, pp. 419-439. [VI.5]   
E. Hairer & H. Turke (1984): The equivalence of $B$ -stability and $A$ -stability. BIT, vol. 24, pp. 520-528. [IV.5], [IV.13]   
E. Hairer & G. Wanner (1981): Algebraically stable and implementable Runge-Kutta methods of high order. SIAMJ. Numer. Anal., vol.18, pp.1098-1108. [IV.5], [IV.13]   
E.Hairer & G. Wanner (1982): Characterization of non-linearly stable implicit Runge-Kutta methods.In:Numerical integration of differential equations,Lecture Notes in Math, vol. 968,pp.207-219. [IV.5],[IV.13]   
E.Hairer & G. Wanner (1995): Analysis by its history. Undergraduate Texts in Mathematics, Springe-Verlag New York. [IV.4],   
E. Hairer &G. Wanner (1996): Ona generalization of atheorem ofvon Neumann.To appear in ZAMM. [IV.12]   
E. Hairer & M. Zennaro (1996): On error growth functions of Runge-Kutta methods. To appear in Appl. Numer. Math. [IV.11], [IV.12]   
E.Hairer,see also V.Brasey&E.Hairer;K.Dekker&E.Hairer; P.Deuflhard,E.Hairer& J. Zugck; G. Wanner, E. Hairer & S.P. Nprsett.   
G. Hall (1985): Equilibrium states of Runge-Kutta schemes. ACM Trans. Math. Software, vol.11, pp.289-301. [IV.1], [IV.2]   
G. Hall (1986): Equilibrium states of Runge-Kuta schemes, part II. ACM Trans. Math. Software,vol.12,pp.183-192. [IV.2]   
G.Hall & D.J. Higham (1988): Analysis of stepsize selection schemes for Runge-Kutta codes. IMA J. Numer. Anal., vol. 8, pp.305-310. [IV.2]   
G.Hall, see also D.J. Higham & G. Hall.   
R.W.Hamming (1959): Stable predictor-corrector methods for ordinary differential equations. J. ACM, vol. 6, pp. 37-47. [V.1]

R.W.HansonSmith, see D.S.Watkins & R.W. HansonSmith.

D.R. Hartree, see A. Callender, D.R. Hartree & A. Porter.

E.J. Haug (1989): Computer-aided Kinematics and Dynamics of Mechanical Systems. Allyn & Bacon, Boston. [VI1.7]

E.J. Haug,see also R.A. Wehage & E.J. Haug.

F. Hausdorff (1921): Summationsmethoden und Momentfolgen. Math. Zeitschrift, vol. 9, Pp. 74-109 and pp. 280-299. [IV.11]

P.Henrici (1962): Discrete Variable Methods in Ordinary Differential Equations. Wiley, New York. [V.7]

D. Henry (1981): Geometric Theory of Semilinear Parabolic Equations. Springer Lecture Notes in Mathematics 840. [V.8]

Ch. Hermite (1873): Sur la fonction exponentielle. Comptes rendus de 1'Acad. Sciences, vol. 77, pp. 18-24,74-79,226-233,285-293. (Euvres, tome III, pp.150-181. [IV.3]

K.L.Hiebert, see L.F. Shampine & K.L. Hiebert.

D.J. Higham & G. Hall (1990): Embedded Runge-Kutta formulae with stable equilibrium states. J. of Comp.and Appl. Math., vol. 29, pp. 25-33. [IV.2]

D.J. Higham (1989): Analysis of the Enright-Kamel partitioning method for stiff ordinary differential equations. IMA J. Numer. Anal., vol. 9, pp. 1-14. [IV.10]

D.J. Higham, see also G. Hall& D.J. Higham.

A.C.Hindmarsh (1980): LSODE and LSODI, two new initial value ordinary differential equation solvers. ACM-SIGNUM Newsletter 15, pp. 10-11. [IV.10], [V.5], [VII.3]

A.C. Hindmarsh (1983): ODEPACK, a systematized collection of ode solvers. In Scientific Computing, R.S. Stepleman et al. (eds.), North-Holland, Amsterdam, pp. 55-64. [V.5]

A.C.Hindmarsh,see also P.N. Brown, G.D.Byrme & A.C. Hindmarsh; G.D. Byrne & A.C. Hindmarsh.

J.O.Hirschfelder,see C.F. Curtiss & J.O.Hirschfelder.

E. Hofer (1976): A partially implicit method for large stiff systems of ODE's with only few equations introducing smalltime-constants. SIAMJ. Numer. Anal., vol. 13, pp. 645-663. [iv.10]

C.D.Holland,see A. Feng, C.D. Holland & S.E. Gallun.

E. Hopf (1950): The partial differential equation $u _ { t } + u u _ { x } = \mu u _ { x x }$ . Comm. on Pure and Appl. Math.,vol.3, pp.201-230. [VI.5], [VI.6]

P.J.van der Houwen (1968): Finite diffrence methods for solving partial differential equations. MC Tract 20, Math. Centrum,Amsterdam. [IV.2]

P.J. van der Houwen (1973): One-step methods with adaptive stability functions for the integration of differential equations.Lecture Notes in Mathematics No. 333, Springer-Verlag,Berlin, pp.164-174. [IV.7]

P.J. van der Houwen (1977): Construction of integration formulas for initial value problems. North Holland series in Applied Math. and Mech., 269 pp. [IV.2], [IV.11]

P.J. van der Houwen& B.P.Sommeijer (1980): On the internal stability ofexplicit,m-stage Runge-Kutta methods for large m -values. Z. Angew. Math. Mech., vol. 60, pp. 479-485. [1V.2]

H.H. Hsu, see C.W.Gear,H.H. Hsu & L. Petzold.

T.E.Hull,see W.H.Enright & T.E.Hull; W.H.Enright,T.E.Hull&B.Lindberg.

W.H. Hundsdorfer (1985): The numerical solution of nonlinear stiff initial value problems: an analysis of one step methods. CWI Tract, Nr.12, Mathematisch Centrum, Amsterdam. [IV.11], [IV.12], [IV.14]

W.H. Hundsdorfer (1986): Stability and $B$ -convergence of linearly implicit Runge-Kutta methods. Numer. Math., vol. 50, pp. 83-95. [IV.15]

W.H. Hundsdorfer & M.N. Spijker (1981): A note on $B$ -stability of Runge-Kutta methods. Numer. Math., vol. 36, pp. 319-331. [IV.12]

W.H. Hundsdorfer & M.N. Spijker (1987): On the algebraic equations in implicit Runge-Kutta methods. SIAM J. Numer. Anal., vol. 24, pp. 583-594. [IV.14]

W.H. Hundsdorfer & B.I. Steininger (1991): Convergence of linear multistep and one-leg methods for stiff nonlinear initial value problems. BIT vol. 31, p.124-143. [V.6], [V.7]

W.H. Hundsdorfer, see also K. Burrage & W.H. Hundsdorfer; M. Crouzeix, W.H. Hundsdorfer & M.N. Spijker; J.G. Verwer, W.H. Hundsdorfer & B.P. Sommeijer.

A.Hurwitz & R. Courant (1925): Funktionentheorie. 2. Aufl., Verlag von Julius Springer, Berlin. [V.4]

A.F.Huxley,see A.L. Hodgkin & A.F. Huxley.

A. Iserles (1981): Generalized order star theory, in : Padé approximations and its applications.Amsterdam 1980, ed. M.G. de Bruin & H. van Rossum,Lecture Notes in Math. #888. [IV.4]

A. Iserles & S,P. Nprsett (1984): A proof of the first Dahlquist barrier by order stars.BIT, vol. 24, pp. 529-537. [V.4]

A. Iserles & G. Strang (1983): The optimal accuracy of difference schemes. Trans. Am. Math. Soc., vol. 277, pp. 779-803. [IV.4]

A.Iserles & R.A Williamson (1983): Stability and accuracy of semi-discretized finite difference methods. IMA J. Numer. Anal., vol. 4, pp. 289-307. [IV.4]

C.G.J. Jacobi (1826): Ueber Gauss' neue Methode die Werthe der Integrale naherungsweise zu finden.Journ.f.reine u. angew. Math., vol.I, pp.301-308; Werke Vol. VI (1981), pp. 1-11. [IV.5]

L. Jay (1993): Convergence of a class of Runge-Kutta methods for differential-algebraic systems of index 2, BIT, vol. 33, pp.137-150. [VI1.4]

L. Jay (1994): Runge-Kutta type methods for index three differential-algebraic equations with applications to Hamiltonian systems. Thesis No.2658, Univ. Geneve. [VI1.8]

L. Jay (1995): Structure-preserving integrators. Submitted for publication. [VI.8]

L. Jay (1996): Symplectic partitioned Runge-Kutta methods for constrained Hamiltonian systems.SIAM J. Numer. Anal., vol. 33, pp. 368-387. [VI.8]

R. Jeltsch (1976): Stiff stability and its relation to $A _ { 0 }$ - and $A ( 0 )$ -stability, SIAMJ. Numer. Anal.,vol.13, pp. 8-17. [V.2]

R. Jeltsch (1976): Note on A-stability of multistep multiderivative methods. BIT, vol.16, Pp. 74-78. [V.4]

R. Jeltsch (1978): Stability on the imaginary axis and A-stability of linear multistep methods. BIT, vol. 18,pp. 170-174. [V.4]

R.Jeltsch (1988): Order barriers for diference schemes for linear and nonlinear hyperbolic problems. In: Numerical Analysis 1987,D.F Grifiths & G.A. Watson (eds.), Pitman Research Notes in Math., No.170,pp.157-175. [IV.4]

R.Jeltsch & O.Nevanlinna (1978): Largest disk of stability of explicit Runge-Kutta methods. BIT, vol. 18, pp. 500-502. [IV.4]

R.Jeltsch & O.Nevanlinna (1981): Stability of explicit time discretizations for solving initial value problems. Numer. Math., vol. 37, pp. 61-91; Corrigendum: Numer. Math., vol. 39, p.155. [IV.4]

R.Jeltsch & O. Nevanlinna (1982): Stability and accuracy of time discretizations for initial value problems. Numer. Math., vol. 40, pp. 245-296. [IV.4], [V.2], [V.4]

R.Jeltsch, see also G.Dahlquist & R. Jeltsch.

M.S.Kamel, see W.H. Enright & M.S. Kamel.

L.Kantorovich & G. Akilov (1959): Functional Analysis in Normed Spaces. Fizmatgiz, Moscow (German translation: Akademic- Verlag, Berlin, 1964). [V1.3]

P.Kaps (1977): Modifizierte Rosenbrockmethoden der Ordnungen 4,5 und 6 zur numerischen Integration steifer Differentialgleichungen. Dissertation, Univ. Innsbruck. [IV.7]

P.Kaps & A. Ostermann (1989): Rosenbrock methods using few LU-decompositions. IMA J. Numer. Anal., vol. 9, pp. 15-27. [IV.7]

P. Kaps & A. Ostermann (1990): $L ( \alpha )$ -stable variable order Rosenbrock-methods. in: K. Strehmel, ed., Numerical treatment of diffrential equations, Teubner Texte zur Mathematik, Band 121, p. 80-91. [IV.7]

P. Kaps, S.W.H. Poon & T.D. Bui (1985): Rosenbrock methods for stiff ODEs: a comparison of Richardson extrapolation and embedding technique. Computing, vol. 34, pp. 17-40. [IV.7]

P. Kaps & P. Rentrop (1979): Generalized Runge-Kutta methods of order four with stepsize control for stiff ordinary differential equations. Numer. Math., vol. 33, pp. 55-68. [IV.7]

P.Kaps & G. Wanner (1981): A study of Rosenbrock-type methods of high order. Numer. Math., vol. 38, pp. 279-298. [IV.7]

O.A.Karakashian, see L.A. Bales, O.A. Karakashian & S.M. Serbin.

T. Kato (1960): Estimation of iterated matrices, with application to the von Neumann condition. Numer. Math., vol. 2, pp. 22-29. [V.7]

T.Kato (1966): Perturbation Theory for Linear Operators. Grudlehren der math. Wissenschaften,Bd. 132, Springer Verlag,Berlin. [V.7]

T. Kato, see H. Fujita & T. Kato.

S.L. Keeling (1989): On implicit Runge-Kutta methods with a stability function having distinct real poles. BIT,vol. 29,pp. 91-109. [IV.4]

M.D. Kirszbraun (1934): Ueber die zusammenziehenden und Lipschitzschen Transformationen. Fund. Math., vol. 23, pp.77-108. [IV.12]

R.W. Klopfenstein, see R.L. Crane & R.W. Klopfenstein.

A.K. Kong, see R.D. Skeel & A.K. Kong.

J.F.B.M. Kraaijevanger (1985): $B$ -convergence of the implicit midpoint rule and the trapezoidal rule. BIT, vol. 25, pp. 652-666. [IV.15]

J.F.B.M. Kraaijevanger (1986): Absolute monotonicity of polynomials occuring in the numerical solution of initial value problems. Numer. Math., vol. 48, pp. 303-322. [IV.11]

J.FB.M. Kraaijevanger (1991): A characterization of Lyapunov diagonal stability using Hadamard products. Linear Alg. Appl., vol. 151, pp.245-254. [IV.14]

J.F.B.M. Kraaijevanger & J. Schneid (1991): On the unique solvability of the Runge-Kutta equations. Numer. Math., vol. 59, pp. 129-157. [IV.14], [IV.15]

J.F.B.M. Kraaijevanger, see also K.Dekker, J.F.B.M. Kraaijevanger & J. Schneid; J.A. van de Griend & J.FB.M. Kraaijevanger; M.Z. Liu & J.FB.M. Kraaijevanger.

H.O.Kreiss (1962): Uber die Stabilitatsdefinition fir Differenzengleichungen die partielle Differentialgleichungen approximieren. BIT, vol. 2, pp. 153-181. [V.7]

FT. Krogh (1966): Predictor-Corrector methods of high order with improved stability characteristics. J. Assoc. Comput. Mach., vol. 13, pp. 374-385. [V.1]

L.Kronecker (1874): Uber Schaaren von quadratischen und bilinearen Formen. Akad. der Wiss.Berlin 19.Jan.1874,Werke vol.I, pp.351-413. [VII.1]

L.Kronecker (1890): Algebraische Reduction der Schaaren bilinearer Formen. Akad. der Wiss.Berlin27.Nov1890,Werkevol.Il2,p.141-15.VI.1]

V.I. Krylov(1959): Priblizhennoe Vychislenie Integralov. Goz.Izd.Fiz.-Mat.Lit., Moscow. English translation: Approximate calculation of integrals. Macmillan, New York,1962. [V.3]

P. Kunkel & V. Mehrmann (1995): Canonical forms for linear diferential-algebraic equations with variable coeffcients. J. Comp. Appl. Math., vol. 56, pp. 225-251. [VI1.1]

P.Kunkel & V.Mehrmann (1996): Regular solutions of nonlinear differential-algebraic equations and their numerical determination. Preprint, TU Chemnitz-Zwickau. [VI.2]

M.A. Kurdi (1974): Stable high order methods for time discretization of stiff differential equations. Thesis, Univ. of California. [IV.6]

A. Kvrng (1990): Runge-Kutta methods applied to fully implicit differential-algebraic equations of index 1. Math. Comp., vol. 54, pp. 583-625. [VI1.5]

B. Lago, see A. Guillou & B.Lago.

JL.Lagrange (1776): Sur l’usage des fractions continues dans le calcul integral. Nouv. Mem. de 1Acad. royale du Sc. et Belles-Lettres de Berlin, Oeuvres Tome quatrieme, pp. 301-332. [IV.3]

J.L.Lagrange (1788): Méchanique analitique. Paris, chez la Veuve Desaint, Libraire, MD-CCLXXXVIII, avec approbation et privilege du Roi. Oeuvres vol. 11 et 12. [IV.1]

S.Lang (1962): Introduction todiferentiable manifolds.John Wiley1962; third and enlarged edition: Diferential and Riemannian manifolds. Graduate Texts in Mathematics, Springer 1995. [VII.1]

J.D.Lawson (1967): Generalized Runge-Kutta processes for stable systems with large Lipschitz constants. SIAM J. Numer. Anal., vol. 4, pp. 372-380. [IV.9]

V.I.Lebedev (1989): Explicit diffrence schemes with time-variable steps for solving stif systems of Equations. Sov. J. Numer. Anal. Math. Modelling 1989, vol. .4, N2, pp.111- 135. [IV.2]

V.I.Lebedev (1994): How to solve stiffsystems of differential equations by explicit methods. In: Numerical methods and applications, ed. by G.I. Marchuk, pp.45-80,CRC Press 1994. [IV.2]

V.I. Lebedev (1995): Extremal polynomials with restrictions and optimal algorithms. Manuscript, Russian Academy of Science,Moscow. [IV.2]

V.I.Lebedev & S.I. Finogenov (1976): On the utilization of ordered Tchebychef parameters in iterative methods.Zh.Vychisl. Mat.MatFiziki vol.16,Nr.4 pp.895-910,(in Russian). [IV.2]

V.I.Lebedev & A.A. Medovikov (1994): Explicit methods of second order for the solution of stiff systems ofordinary diferential equations (russian). Manuscript, Russian Academy of Science,Moscow. [IV.2]

B. van Leer, see P. Sonneveld & B. van Leer.

B.Leimkuhler, see C.Fuhrer & B.Leimkuhler; C.W. Gear, G.K. Gupta & B.Leimkuhler.

B.J.Leimkuhler & R.D. Skeel (1994): Symplectic numerical integrators in constrained Hamiltonian systems. J. Comput. Phys., vol. 112, pp. 117-125. [VI.8]

M.-N.Le Roux (1980): Méthodes multipas pour des équations paraboliques non lineaires. Numer. Math., vol. 35, pp. 143-162. [V.8]

R.J.LeVeque & L.N. Trefethen (1984): On the resolvent condition in the Kreiss matrix theorem. BIT, vol. 24, pp. 584-591. [V.7]

R.LeVeque,see also G. Dahlquist, H. Mingyou & R. LeVeque.

H. Lewy,see R. Courant, K.Friedrichs & H Lewy.

I.Lie(1990): The stability function for multistep collocation methods. Numer. Math., vol.57, Pp. 779-787. [V.3]

I Lie & S.P. Ngrsett (1989): Superconvergence for multistep collocation. Math. of Comput., vol. 52, pp. 65-79. [V.3]

B.Lindberg (1971): On smoothing and extrapolation for the trapezoidal rule.BIT,vol. 11, pp. 29-52. [IV.9]

B.Lindberg (1972): A simple interpolation algorithm for improvement of the numerical solution of a differential equation. SIAM J. Numer. Anal., vol. 9, pp. 662-668. [VI.5]

B.Lindberg (1974): On a dangerous property of methods for stiffdifferential equations. BIT, vol. 14, pp. 430-436. [IV.3]

B.Lindberg,see also W.H. Enright, T.E. Hull &B.Lindberg.

W.Liniger (1956): Zur Stabilitat der numerischen Integrationsmethoden fur Differentialgleichungen. These, Université de Lausanne, 95 p. [V.6]

W.Liniger & R.A. Willoughby (1970): Efficient integration methods for stiff systems of ordinary differential equations. SIAM J. Numer. Anal., vol. 7, pp. 47-66. [IV.8]

W. Liniger, see also O. Nevanlinna & W. Liniger; F. Odeh & W.Liniger.

M.Z. Liu, K. Dekker & M.N. Spijker (1987): Suitability of Runge-Kutta methods. J. Comp Appl. Math., vol. 91, pp. 53-63. [IV.14]

M.Z.Liu & J.F.B.M. Kraaijevanger (1988): On the solvability of the systems of equations arising in implicit Runge-Kutta methods. BIT, vol. 28, pp. 825-838. [IV.14]

C.F. Van Loan, see G.H. Golub & C.F. Van Loan.

L.Lopez & D. Trigiante (1989): A projection method for the numerical solution of linear systems in separable stiff differential equations.Intern. J. Computer Math.,vol. 30, pp. 191-206. [IV.10]

P.Lotstedt (1985): Discretization of singular perturbation problems by BDF methods. Re-port No.99, Uppsala Univ., Dept. of Comp. Sci. [VI.2]

P.Lotstedt (1985): On the relation between singular perturbation problems and differentialalgebraic equations. Report No.100, Uppsala Univ., Dept. of Comp. Sci. [VI.2]

P.Lotstedt & L. Petzold (1986): Numerical solution of nonlinear differential equations with algebraic constraints I: Convergence results for backward diferentiation formulas. Math. Comput., vol 46, pp. 491-516. [VI.3]

Ch.Lubich (1988): Convolution quadrature and discretized operational calculus I. Numer. Math., vol. 52, pp. 129-145. [V.7]

Ch.Lubich (1989): Linearly implicit extrapolation methods for differential-algebraic systems. Numer. Math., vol. 55, pp. 197-211. [VI.6] [VII.1]

Ch. Lubich (1989): $h ^ { 2 }$ -extrapolation methods for diffrential-algebraic systems of index 2. Impact Comput. Sc. Eng., vol. 1, pp. 260-268. [ViI.7], [VI1.6]

Ch.Lubich (1991): On the convergence of multistep methods for nonlinear stiff differential equations.Numer. Math., vol. 58, pp.839-853,and Erratum (Numer. Math., vol. 61, pp. 277-279) [V.7], [V.8], [VI.2]

Ch.Lubich (1991): Extrapolation integrators for constrained multibody systems.Impact Comp. Sci. Eng.,vol.3, pp. 213-234. [VII.2]

Ch.Lubich (1991): On projected Runge-Kutta methods for diferential-algebraic equations. BIT, vol.31, pp. 545-550. [VII.5]

Ch.Lubich (1993): Integration of stiff mechanical systems by Runge-Kuta methods. ZAMP, vol. 44, pp. 1022-1053. [VII.7]

Ch.Lubich,see also E.Hairer,G.Bader & Ch.Lubich; E.Hairer & Ch.Lubich; E.Hairer, Ch.Lubich & M.Roche.

Ch.Lubich, U. Nowak, U. Pohle & Ch. Engstler (1992): MEXX-numerical software for the integration of constrained mechanical multibody systems. Preprint SC 92-12, Konrad-Zuse-Zentrum, Berlin. [VI.7]

Ch.Lubich & A. Ostermann (1993): Runge-Kutta methods for parabolic equations and convolution quadrature. Math. Comp., vol. 60, pp. 105-131. [V.8]

Ch.Lubich & M. Roche (1990): Rosenbrock methods for diferential-algebraic systems with solution-dependent singular matrix multiplying the derivative. Computing,vol. 43, pp. 325-342. [VI.6]

M.Lundh, see K. Gustafsson, M.Lundh & G. Soderlind.

F. Macsek, see W. Auzinger, R.Frank,& F.Macsek.

D.W. Manning (1981): A computer technique for simulating dynamic multibody systems based on dynamic formalism. Thesis, Univ. Waterloo, Ontario. [VI1.7]

M.Marden (1966): Geometry of polynomials. Mathematical Surveys, American Mathematical Society, Providence,Rhode Island, 2nd edition, 243 p. [V.7]

A.A. Markov (1890): On a question of Mendeleiev. Petersb. Proceedings LXII, 1-24 (Russian). [IV.2]

J.E. Marsden, see R. Abraham, J.E. Marsden & T. Ratiu.

R.Marz (1989): Index-2 differential-algebraic equations. Results in Mathematics,vol. 15, Pp. 149-171. [VI.1]

R.Marz (1990): Higher index diferential-algebraic equations: Analysis and numerical treatment.BanachCenterPubl.,24,umer.Anal.andathodelling,pp.199-22.1], [VII.3]

R.März, see also E. Griepentrog & R. März.

W.S.Massey (1980): Singular homology theory. Graduate Texts in Mathematics 70,Springer Verlag,265 pp. [IV.4]

R.I. McLachlan (1995): On the numerical integration of ordinary differential equations by symmetric composition methods. SIAM J. Sci. Comput., vol. 16, pp. 151-168. [VI.8]

V. Mehrmann, see also P. Kunkel & V. Mehrmann.

M.L. Michelsen (1976): Semi-implicit Runge-Kutta methods for stiff systems, program description and application examples.Inst. f. Kemiteknik, Danmarks tekniske Hgjskole, Lyngby. [VI.4]

K. Miller & R.N. Miller (1981): Moving finite elements. I. SIAM J. Numer. Anal., vol.18, Pp.1019-1032. [VI.6]

H. Mingyou, see G. Dahlquist, H. Mingyou & R.LeVeque.

G.J. Minty (1962): On a simultaneous solution of a certain system of linear inequalities. Proc.Amer. Math. Soc.,vol.13, pp.11-12. [IV.12]

E.F.Mishchenko,see L.S. Pontryagin, V.G. Boltyanskii,R.V. Gamkrelidze & E.F. Mishchenko.

J.I. Montijano (1983): Estudio de los metodos SIRK para la resolucion numérica de ecuaciones diferenciales de tipo stiff. Thesis, Univ. Zaragoza. [IV.14]

E. Moore, see also S.L. Campbell& E. Moore.

R.E.Moore, see J.W. Daniel & R.E. Moore.

K.W. Morton, see R.D. Richtmyer & K.W. Morton.

H.N. Muilthei (1982): Maximale Konvergenzordnung bei der numerischen Losung von An-fangswertproblemen mit Splines. Numer. Math., vol. 39, pp. 449-463. [V.3]

H.N. Multhei (1982): A-stabile Kollokationsverfahren mit mehrfachen Knoten. Computing, vol. 29, pp. 51-61. [V.3]

S.Muller, A. Prohl, R. Rannacher & S. Turek (1994): Implicit time-discretization of the nonstationary incompressble Navier-Stokes equations. Proc.10th GAMM-Workshop, Kiel,W. Hackbusch & G. Wittum eds., Vieweg. [IV.3]

A. Murua (1995): Partitioned half-explicit Runge-Kutta methods for diferential-algebraic systems of index 2. Submitted for publication. [VI1.6], [VI1.7]

C.L. Navier (1823): Mémoire sur les lois du mouvement des fuides (lu a l'Acad.le 18 mars 1822). Paris, Mém. de 'Acad. Royale des Sciences, Tome VI, pp. 389-440. [V.8]

J. von Neumann (1951): Eine Spektraltheorie fir allgemeine Operatoren eines unitären Raumes. Math. Nachrichten, vol. 4, pp. 258-281. [IV.11]

O. Nevanlinna (1976): On the logarithmic norms of a matrix. Report HTKK-MAT-A94, Helsinki Univ. of Tech. [VI.3]

O. Nevanlinna (1976): On error bounds for G-stable methods. BIT, vol. 16, pp. 79-84. [V.6]

O. Nevanlinna (1977): On the numerical integration of nonlinear initial value problems by linear multistep methods. BIT, vol. 17, pp. 58-71. [V.8]

O. Nevanlinna (1985): Matrix valued versions of a result of von Neumann with an applica-tion to time discretization. J. Comput. Appl. Math., vol. 12& 13, pp. 475-489. [V.7]

O. Nevanlinna & W.Liniger (1978): Contractive methods for stiff differential equations, I. BIT, vol. 18, pp. 457-474. [V.7]

O.Nevanlinna & W.Liniger (1979): Contractive methods for stiff differential equations, II. BIT, vol. 19, pp. 53-72. [V.7]

O.Nevanlinna & F. Odeh (1981): Multiplier techniques for linear multistep methods. Numer. Funct. Anal. Optim., vol. 3, pp. 377-423. [V.8]

O. Nevanlinna,see also R. Jeltsch & O.Nevanlinna.

K. Nipp & D. Stoffer (1995): Invariant manifolds and global error estimates of numerical integration schemes applied to stiff systems of singular perturbation type - Part I: RKmethods. Numer. Math., vol.70, pp.245-257. [VI.3]

S.P. Nprset (1974): Multiple Padé approximations to the exponential function. Report No. 4/74,Dept. of Math., Univ. of Trondheim, Norway. [IV.4]

S.P. Nprsett (1974): Semi-explicit Runge-Kutta methods. Report No. 6/74, Dept. of Math., Univ. of Trondheim,Norway. [IV.6]

S.P. Ngrsett (1975): Runge-Kutta methods with coeffcients depending on the Jacobian. Re-port No. 1/75, Dept. of Math., Univ. of Trondheim, Norway. [IV.7]

S.P. Norsett (1975): C-polynomials for rational approximations to the exponential function. Numer. Math., vol. 25, pp.39-56. [IV.3]

S.P. Nprsett(1976): Runge-Kutta methods with a multiple real eigenvalue only. BIT,vol.16, pp. 388-393. [IV.8]

S.P. Nprsett & G. Wanner (1979): The real-pole sandwich for rational approximations and oscillation equations. BIT, vol. 19, pp. 79-94. [IV.3], [IV.4]

S.P.Nprsett & G. Wanner (1981): Perturbed collocation and Runge-Kutta methods. Numer. Math., vol. 38, pp. 193-208. [IV.5], [IV.13]

S.P. Nprsett & A. Wolfbrandt (1977): Attainable order of rational approximations to the exponential function with only real poles. BIT, vol. 17, pp. 200-208. [IV.4]

S.P.Ngrsett & A.Wolfbrandt (1979): Order conditions for Rosenbrock types methods. Numer. Math., vol. 32, pp. 1-15. [IV.7]

S,P. Nprsett, see also A. Iserles & S,P. Nprsett; I. Lie & S.P. Nprsett; G. Wanner, E. Hairer & S.P. Norsett.

U. Nowak, see P.Deuflhard & U. Nowak.

R.M. Noyes, see J. Field & R.M. Noyes.

F. Odeh & W.Liniger (1977): Non-linear fixed-h stability of linear multistep formulae. J. Math. Anal. Appl., vol. 61, pp. 691-712. [V.8]

F. Odeh, see also O. Nevanlinna & F. Odeh.

. Olafsson, see also T. Alishenas & O. Olafsson.

R.E. O'Malley (1974): Introduction to Singular Perturbations. Academic Press, New York. [VI.3]

M.K.Ormrod & G.C. Andrews (1986): Advent: a simulation program for constrained planar kinematic and dynamic systems.Publications of the Amer. Soc. of Mech. Eng., 86-DET-97. [VI1.7]

J.M. Ortega & W.C.Rheinboldt (197O): Iterative Solution of Nonlinear Equations in Several Variables. Academic Press, NewYork. [VI.3], [VII.3], [VII.4], [VI.8]

A. Ostermann (1988): Ueber die Wahl geeigneter Approximationen an die Jacobimatrix bei linear-impliziten Runge-Kutt-Verfahren.Dissertation, Univ. Innsbruck,pp. 66.[IV.11]

A. Ostermann (1990): Continuous extensions of Rosenbrock-type methods. Computing, vol. 44, pp. 59-68. [VI.4]

A. Ostermann, see also E. Hairer & A. Ostermann; P. Kaps & A. Ostermann, Ch.Lubich & A. Ostermann.

H. Padé (1892): Sur la representation approchee d'une fonction par des fractions rationneles.Premiere These ("A Monsieur Hermite"),Ann. Ec.Norm.Sup. (3),vol.9,Supp. 3-93, Oeuvres pp. 72-165. [IV.3]

H.Padé(1899): Memoire sur les developpements enfractions continues de lafonction exponentielle pouvant servir d'introduction d la theorie des fractions continues algébriques. Ann. Ec. Norm. Sup. (3), vol. 16, pp.395-426; Oeuvres pp. 231-262. [IV.3]

M.A. Parseval (1799): Private communication to S.F. Lacroix. See: Lacroix, Traite des différences et des séries,Paris 1800, p.377,or Traité du calcul diff. et du calcul int., $2 ^ { \mathsf { e } }$ ed, vol. 3,p.394, Paris 1819. Also published in Paris Mémoires présentés par divers savants a l'acad. d. sc., vol 1,(1806), p. 639.

A. Pazy (1983): Semigroups of Linear Operators and Applications to Partial Differential Equations. Appl. Math. Sciences 44, Springer Verlag. [V.7]

F.Peherstorfer (1981): Characterization of positive quadrature formulas. SIAM J. Math. Anal., vol. 12, pp. 935-942. [IV.13]

O.Perron (1913): Die Lehre von den Kettenbriichen. Teubner, 520 pp., 3rd ed., repr. 1977. [IV.13]

L.R. Petzold (1982): A description of DAsSL: A Differential/Algebraic System Solver. Proceedings of IMACs World Congress,Montreal, Canada. [VII.3], [VI.7]

L.R. Petzold (1983): Automatic selection of methods for solving stiff and nonstiff systems of ordinary diferential equations. SIAM J. Sci. Stat. Comp., vol. 4, pp.136-148. [IV.2]

L.R.Petzold (1986): Order results for implicit Runge-Kutta methods applied to diferential/algebraic systems. SIAMJ. Numer. Anal., vol. 23, pp. 837-852. [VI.1], [VI.4]

L.R. Petzold, see also U. Ascher & L.R. Petzold; K.E. Brenan, S.L. Campbell& L.R. Petzold; K.E. Brenan & L.R. Petzold; C.W. Gear, H.H. Hsu & L. Petzold; C.W. Gear & L.R. Petzold; P.Lotstedt & L. Petzold.

Z. Picel, see B.L. Ehle & Z. Picel.

R.J. Plemmons, see G.P. Barker,A. Berman & R.J. Plemmons.

B.van der Pol(1926): On “Relaxation Oscillations". Phil.Mag.,vol.2,pp.978-992; reprduced in: B.van der Pol,Selected Scientific Papers,vol.I,North-HollandPubl. Comp. Amsterdam (1960). [VI.1]

G. P6lya & G. Szego (1925): Aufgaben und Lehrsatze aus der Analysis. Two volumes, Grundlehren Band XX, Springer Verlag, many later editions and translations. [IV.4]

L.S.Pontryagin, V.G. Boltyanskii, R.V. Gamkrelidze & E.F. Mishchenko (1961): The mathematical theory of optimal processs. Fizmatgiz Moscow, english translations: Wiley 1962,Pergamon Press 1964; german translation: Oldenbourg 1964. [VI1.1]

S.W.H. Poon, see P. Kaps, S.W.H. Poon & T.D. Bui.

A.Porter, see A. Callender, D.R. Hartree & A. Porter.

F.A. Potra (1995): Runge-Kutta integrators for multibody dynamics. Mechanics of Structures and Machines,vol. 23, pp.181-197. [VII.2]

FA. Potra & W.C.Rheinboldt (1990): Differential-geometric techniques for solving diferential algebraic equations. In E.J. Haug & R.C. Deyo, eds, Real-Time Integration of Mechanical System Simulation, Springer-Verlag, Berlin, pp.155-191. {VI1.2]

FA. Potra & W.C. Rheinboldt (1991): On the numerical solution of Euler-Lagrange equations. Mech. Struct.& Mech., vol. 19(1), pp. 1-18. [VI1.2]

WH.Press,B.FaeyS..Tukolsy&WVetering(1986989): Numeical eci pes,the art od scientific computing (FORTRAN version). Cambridgre University Press, 702 pp. [v.10]

P.J. Prince, see J.R.Dormand & P.J. Prince.

A. Prothero & A. Robinson (1974): On the stability and accuracy of one-step methods for solving stiff systems of ordinary differential equations. Math. of Comput.， vol. 28, pp. 145-162. [IV.3], [IV.15]

V. Puiseux (1850): Recherches sur les fonctions algebriques. Journal de Math. vol 15, pp. 365-480. [V.4]

T. Ratiu, see R. Abraham, J.E. Marsden & T. Ratiu.

P.A. Raviart, see M. Crouzeix & P.A. Raviart.

S. Reich (1996): Symplectic integration of constrained Hamiltonian systems by composition methods. SIAMJ. Numer. Anal., vol. 33, pp. 475-491. [VI.8]

S.Reich (1996): On higher-order semi-explicit symplectic partitioned Runge-Kutta methods for constrained Hamiltonian systems. Numer. Math. [VI1.8]

S. Reich, see also U.M. Ascher, H. Chin & S. Reich.

M.Reimer (1967): Zur Theorie der linearen Differenzenformeln. Math. Zeitschr., vol. 95, pp. 373-402. [V.4]

E.Ya. Remez (1957): General computation methods of Chebyshev approximation. UkSSR Acad. Sci. Publ., Kiev 1957 (in Russian).

P. Rentrop, M. Roche & G. Steinebach (1989): The application of Rosenbrock-Wanner type methods with stepsize control in differential-algebraic equations. Numer. Math., vol. 55, pp. 545-563. [Vi.1], [VI.4]

P. Rentrop, see also P. Kaps & P. Rentrop.

JD. Reymond (1989): Implementation des methodes Radau IIA d'ordre 7 et 9. Diploma thesis, Univ. Geneva. [IV.10]

W.C. Rheinboldt (1984): Differential-algebraic systems as differential equations on mani-folds. Math. Comp., vol. 43, pp. 473-482. [VII.1]

W.C.Rheinboldt,see J.M. Ortega & W.C. Rheinboldt; F.A. Potra & W.C.Rheinboldt.

R.D.Richtmyer & K.W. Morton (1967): Difference Methods for Initial-Value Problems. Wiley-Interscience. [V.7]

B. Riemann (1857): Allgemeine Voraussetzungen und Hilfsmittel fir die Untersuchung von Functionen unbeschränkt veranderlicher Groβen. J. f. d. r. u. angew. Math., vol. 54, pp. 101-104; Werke pp. 81-84. [V.4]

R.E.Roberson & R.Schwertassek (1988): Dynamics of Multibody Systems. Springer Verlag. [VI1.7]

B.C.Robertson (1987): Detecting stiffness with explicit Runge-Kutta formulas. Rep.193/87, Dept. Comp. Sci., University of Toronto. [IV.2]

H.H. Robertson (1966): The solution of a set of reaction rate equations. In: J. Walsh ed.: Numer. Anal., an Introduction, Academ. Press, pp.178-182. [IV.1], [IV.10]

A.Robinson,see A.Prothero & A. Robinson.

M. Roche (1988): Rosenbrock methods for diferential algebraic equations. Numer. Math., vol. 52, pp. 45-63. [VI.4]

M. Roche (1988): Runge-Kutta and Rosenbrock methods for differential-algebraic equations and stiff ODEs. Doctoral thesis, Universite de Geneve. [VII.5]

M. Roche (1989): Runge-Kutta methods for differential algebraic equations. SIAM J. Numer. Anal., vol. 26, pp. 963-975. [VI.4]

M. Roche,see also E. Hairer, Ch. Lubich & M. Roche; Ch.Lubich & M.Roche; P. Rentrop, M.Roche & G. Steinebach.

H.H. Rosenbrock (1962/63): Some general implicit processes for the numerical solution of diffe rential equations. Computer J.,vol. 5, pp. 329-330. [IV.7]

F Ruamps, see M. Crouzeix & F. Ruamps.

W.B.Rubin, see T.A. Bickart & W.B.Rubin.

J.-P. Ryckaert, G. Ciccoti & H.J.C. Berendsen (1977): Numerical integration of the carte-sian equations of motion of a system with constraints: molecular dynamics of n-alkanes. J. Comput. Phys., vol. 23, pp.327-341. [VII.8]

Y. Saad (1981): Krylov subspace methods for solving large unsymmetric linear systems. Math. Comp., vol. 37, pp.105-126. [IV.10]

Y. Saad (1982): The Lanczos biorthogonalization algorithm and other oblique projection methods for solving large unsymmetric systems. SIAM J. Numer. Anal., vol. 19, pp. 485- 506. [Iv.10]

Y. Saad, see also C.W. Gear & Y. Saad.

I.W. Sandberg & H. Sichman (1968): Numerical integration of systems of stiff nonlinear differential equations. The Bell System Technical Journal, vol. 47, pp. 511-527. [IV.12]

J.M. Sanz-Serna & M.P. Calvo (1994): Numerical Hamiltonian Problems. Appl. Math. and Math. Comput. 7, Chapman & Hall, 207pp. [VI1.8]

V.K. Saul'ev (1960): Integration of parabolic type equations with the method of nets (in Russian). Moscow, Fizmatgiz 1960. [IV.2]

A. Sayfy, see G.J. Cooper & A. Sayfy.

E. Schafer (1975): A new approach to explain the “High Iradiance Responses” of photomorphogenesis on the basis of phytochrome.J. of Math. Biology， vol. 2, pp. 41-56. [1V.10]

W. Schiehlen, ed. (1990): Multibody systems handbook. Springer Verlag, Berlin. [VI.7]

R. Scherer (1979): A necessary condition for $B$ -stability.BIT,vol.19,pp.111-115.[IV.3], [1v.12]

J. Schneid (1987): $B$ -convergence of Lobatto IIC formulas. Numer. Math., vol. 51, pp. 229- 235. [IV.15]

J. Schneid,see also K.Dekker, J.F.B.M. Kraaijevanger & J. Schneid; R.Frank,J. Schneid & C.W. Ueberhuber; J.F.B.M.Kraaijevanger & J. Schneid.

C.Schneider (1991): ROW-methods adapted todiferential-algebraic systems.Math.Comp., vol. 56, pp. 201-213. [VI.4]

C. Schneider (1991b): Private communication. [VI.4]

C.Schneider (1993): Analysis ofthe linearly implicit mid-point rule for differential-algebraic equations. Electronic Transactions on Numerical Analysis,vol. 1, pp.1-10. [VI.5]

I.J. Schoenberg (1953): On a Theorem of Kirszbraun and Valentine. Amer. Math. Monthly, vol. 60, pp. 620-622. [IV.12]

S. Scholz (1989): Order barriers for the $B$ -convergence of ROW methods. Computing, vol. 41, pp. 219-235. [IV.15]

S. Scholz, see also J.G. Verwer & S. Scholz.

J. Schroll, see R.D. Grigorieff & J. Schroll.

J. Schur (1918): Uber Potenzreihen,die im Innern des Einheitskreises beschrinkt sind.J. Reine u. angew. Math., vol. 147, pp. 205-232. [V.3]

R.Schwertassek, see R.E. Roberson & R.Schwertassek.

S.M. Serbin, see L.A. Bales, O.A. Karakashian & S.M. Sebin.

L.F. Shampine (1977): Stiffness and nonstiff differential equation solvers, I: detectingstiff-ness with Runge-Kutta methods. ACM TOMS, vol. 3, pp. 44-53. [IV.2]

L.F. Shampine (1980): Implementation of implicit formulas for the solution of ODEs. SIAM J. Sci. Stat. Comput., vol. 1, pp.103-118. [IV.8]

L.F. Shampine (1981): Evaluation of a test set for stiff ODE solvers. ACM Trans. Math. Soft.,vol. 7, pp. 409-420. [IV.10]

L.F. Shampine (1982): Implementation of Rosenbrock methods. ACM Trans. Math. Soft., vol. 8, pp. 93-113. [IV.7]

L.F. Shampine (1986): Conservation laws and the numerical solution of ODEs. Comp. Maths. Appls., vol. 12B., pp.1287-1296. [VI1.2]

L.F. Shampine (1987): Control of step size and order in extrapolation codes. J. Comp. Appl. Math., vol. 18, pp.3-16. [IV.9]

L.F. Shampine & K.L. Hiebert (1977): Detecting stiffness with the Fehlberg (4,5) formulas. Comp. & Maths. with Appls., vol. 3, pp. 41-46. [IV.2]

L.F. Shampine & H.A. Watts (1979): DEPAC -- design of a user oriented package of ODE solvers. Report SAND-79-2374, Sandia Nat. Lab., Albuquerque, New Mexico. [V.5]

H. Sichman, see I.W. Sandberg & H. Sichman.

R.F. Sincovec, A.M. Erisman, E.L. Yip & M.A. Epton (1981): Analysis of descriptor systems using numerical algorithms. IEEE Trans. Aut. Control, AC-26, pp. 139-147. [VI.3]

R.D. Skeel, see also B.J. Leimkuhler & R.D. Skeel.

R.D. Skeel & A.K. Kong (1977): Blended linear multistep methods. ACM TOMS,vol. 3, Pp. 326-343. [V.2], [V.3], [V.5]

H.M.Sloate & T.A. Bickart (1973): A-stable composite multistep methods. J. ACM, vol. 20, pp. 7-26. [V.3]

P.E. Sobolevskii (1959): On non-stationary equations of hydrodynamics for viscous fluid. Doklady Akad.Nauk USSR, vol. 128, pp. 45-48. [V.8]

G.Soderlind (1981): On the effcient solution of nonlinear equations in numerical methods for stiff differential systems.Report TRITA-NA-8114,Royal Inst.of Tech.,Stockholm. [1v.10]

G. Soderlind (1989): A multi-urpose system for the numerical integration of ODEs. Appl. Math. Comp., vol. 31, pp. 346-360. [VI.6]

G.Soderlind & G.Dahlquist (1981): Error propagation and stiff differential systems of sin-gular perturbation type. Rep. TRITA-NA-8108, Royal Inst. of Tech., Stockholm. $I V I . 2 ]$

G.Soderlind, see also C. Arévalo, C.Fuhrer & G. Soderlind; G. Dahlquist & G. Soderlind; K.Gustafsson, M.Lundh & G. Soderlind.

B.P.Sommeijer & J.G. Verwer (1980): A performance evaluation of a class of Runge-Kutta-Chebyshev methods for solving semi-discrete parabolic differential equations. Report NW91/80, Mathematisch Centrum, Amsterdam. [IV.2]

B.P. Sommeijer (1991): RKC, a nearly-stiff ODE solver. Available from netlib $@$ orml.gov, send rkc.f from ode. [IV.2], [IV.10]

B.P. Sommeijer, see P.J. van der Houwen & B.P. Sommeijer; J.G. Verwer, W.H. Hundsdorfer & B.P. Sommeijer.

A.Sommerfeld (1942): Vorlesungen iiber theoretische Physik.Bd.1., Mechanik; translated from the 4th german ed.: Acad. Press. [IV.1], [VII.1]

P. Sonneveld & B. van Leer (1985): A minimax problem along the imaginary axis. Nieuw Archief V. Wiskunde (4), vol. 3, pp. 19-22. [IV.2]

G. Sottas (1984): Dynamic adaptive selection between explicit and implicit methods when solving ODE's. Report, Sect. de math., Univ. Geneve. [IV.2]

G. Sottas & G. Wanner (1982): The number of positive weights of a quadrature formula. BIT, vol. 22, pp. 339-352. [IV.13]

J.L. Soulé, see A. Guillou & J.L. Soulé.

M.N. Spijker (1983): Contractivity in the numerical solution of initial value problems. Numer. Math., vol. 42, pp. 271-290. [IV.11]

M.N.Spijer(1985):Feasibilityndcontrativiy inimpicit Runge-Kutamethods.J.Comp. Appl. Math.,vol. 12 et 13,pp. 563-578. [1V.14]

M.N. Spijker (1985): Stepsize restrictions for stability of one-step methods in the numerical solution of initial value problems. Math. Comp., vol. 45, pp. 377-392. [IV.11]

M.N. Spijker (1986): The relevance of algebraic stability in implicit Runge-Kutta methods. Teubner Texte zur Mathematik 82 (K. Strehmel, ed.), pp. 158-164. [IV. 15]

M.N.Spijker (1991): On a conjecture by LeVeque and Trefethen related to the Kreiss matrix theorem. BIT, vol. 31, pp. 551-555. [V.7]

M.N. Spijker, see also M. Crouzeix,W.H. Hundsdorfer & M.N. Spijker; W.H.Hundsdorfer & M.N. Spijker; M.Z. Liu, K. Dekker & M.N. Spijker.

I.A. Stegun, see M. Abramowitz & I.A. Stegun.

T. Steihaug & A. Wolfbrandt (1979): An attempt to avoid exact Jacobian and nonlinear equations in the numerical solution of stiff diferential equations. Math. Comp., vol. 33, pp. 521-534. [IV.7]

G. Steinebach (1995): Order-reduction of ROW-methods for DAEs and method of lines ap-plications. Preprint, TH Darmstadt. [VI.4]

G. Steinebach,see P. Rentrop, M. Roche & G. Steinebach.

B.I. Steininger, see W.H. Hundsdorfer & B.I. Steininger.

V. Steklov (1916): On the approximate computation of definite integrals with the help of so-called mechanical quadrature I. Convergence of mechanical quadrature formulas. Petrograd,Bull. Acad. Sciences, ser. VI, vol.10, pp.169-186 (russian). See also same Journal vol. 11 (1917), pp. 557-558 for a french explanation. [IV.13]

H.J. Steter (1968): Improved absolute stability of predictor-corrector schemes. Computing, vol. 3, pp. 286-296. [V.1]

H.J. Stetter (1973): Analysis of discretization methods for ordinary diffrential equations. Springer,Berlin. [IV.3], [IV.9], [IV.12]

G.W. Stewart (1972): On the sensitivity of the eigenvalue problem $\boldsymbol { A } \boldsymbol { x } = \lambda \boldsymbol { B } \boldsymbol { x }$ . SIAM J. Numer. Anal., vol. 9, pp. 669-686. [VI.1]

T.J. Stieltjes (1884): Quelques recherches sur la Théorie des quadrature dites mécaniques. Annales Scientif. de 'Ecole Norm. Sup., troisieme série, tome I, pp. 409-426. [IV.12]

G.G. Stokes (1845): On the theories of the internal friction of fluids in motion, and the equilibrium and motion of elastic solids. Cambr.Phil. Soc. Trans., vol. 8. Republished in: G.G. Stokes,Mathematical and Physical Papers, vol. 1, Cambridge 1880. [V.8]

D. Stoffer, see also K. Nipp & D. Stoffer.

G. Strang,see A. Iserles & G. Strang.

K. Strehmel & R. Weiner (1982): Behandlung steifer Anfangswertprobleme gewohnlicher Diferentialgleichungenmitdaptiven RungeKua etoden.Computingl. 153-165. [IV.11]

K. Strehmel & R.Weiner (1987): $B$ -convergence results for linearly implicit one step methods. BIT, vol. 27, pp. 264-281. [IV.11], [IV.15]

Sun Geng (1993): Symplectic partitioned Runge-Kutta methods. J. Comput. Math., vol. 11, pp. 365-372. [VI.8]

A.G. Sveshnikov, see A.N. Tikhonov, A.B. Vasil'eva & A.G. Sveshnikov.

G. Szego (1939): Orthogonal Polynomials. AMs Coll. Publ., vol. XXII, 403pp. [V.13]

G. Szego,see also G. P6lya & G. Szego.

E. Tadmor (1981): The equivalence of $L _ { 2 }$ -stability， the resolvent condition, and strict Hstability. Lin. Alg. and its Applics., vol. 41, pp. 151-159. [V.7]

P.G. Thomsen, see S.P. Nprsett & P.G. Thomsen.

A.N. Tikhonov (1952): Systems of differential equations containing small parameters in the derivatives.Mat. Sb. (Russian), vol. 31 (73), pp. 575-586. [VI.3]

A.N. Tikhonov,A.B. Vasil'eva & A.G. Sveshnikov (1985):Differential Equations. Trans. from the Russian by A.B. Sossinskij. Springer Verlag, 238pp. [V1.3]

L.N. Trefethen, see R.J. LeVeque & L.N. Trefethen.

D. Trigiante, see L. Lopez & D. Trigiante.

H.Türke,see E.Hairer& H.Turke.

C.W.Ueberhuber, see R.Frank, J. Schneid & C.W. Ueberhuber.

R.Vanselow (1979): Stabilitats-und Fehleruntersuchungen bei numerischen Verfahren zur Losung steifer nichtlinearer Anfangswertprobleme. Diplomarbeit, Sektion Mathematik, TU-Dresden. [IV.12]

JM. Varah (1979): On the eficient implementation of implicit Runge-Kutta methods. Math. Comp., vol. 33, pp. 557-561. [IV.8]

R.S. Varga, see G. Birkhoff & R.S. Varga.

A.B. Vasil'eva (1963): Asymptotic behaviour of solutions to certain problems involving nonlinear differential equations containing a small parameter multiplying the highest derivatives.Usp. Mat. Nauk (Russian), vol. 18, pp.15-86. English translation: Russian Math. Surveys, vol.18, Nr. 3, pp.13-84. [VI.3]

A.B. Vasil'eva, se also A.N. Tikhonov, A.B. Vasil'eva & A.G. Sveshnikov.

M.V. van Veldhuizen (1984): $D$ -stability and Kaps-Rentrop methods. Computing vol. 32, pp. 229-237. [IV.7], [VI.4]

L. Verlet (1967): Computer "experiments” on classical fluids. I. Thermodynamical properties of Lennard-Jones molecules.Physical Review, vol. 159,pp.98-103. [VI1.8]

J.G. Verwer (1980): On generalized Runge-Kutta methods using an exact Jacobian at a nonstep point. ZAMM, vol. 60, pp. 263-265. [IV.7]

J.G. Verwer (1996): Explicit Runge-Kutta methods for parabolic partial diferential equations. To appear in Applied Numerical Mathematics. [IV.2]

J.G. Verwer, W.H. Hundsdorfer & B.P. Sommeijer (1990): Convergence properties of the Runge-Kutta-Chebyshev method. Numer. Math., vol. 57, pp. 157-178. [IV.2]

J.G. Verwer & S. Scholz (1983): Rosenbrock methods and time-lagged Jacobian matrices. Beiträge zur Numer. Math., vol. 11, pp. 173-183. [IV.7]

J.G. Verwer, see also K. Dekker & J.G. Verwer.

P.P. Wakker (1985): Extending monotone and non-expansive mappings by optimization. Cahiers du C.E.R.O., vol. 27, pp. 141-149. [IV.12]

G. Wanner (1976): A short proof on nonlinear A-stability. BIT,vol.16, pp.226-227. [IV.12]

G. Wanner (1980): Characterization of all A-stable methods of order 2m-4.BIT,vol. 20, pp. 367-374. [IV.5]

G.Wanner, E.Hairer & S.P. Nprsett (1978): Order stars and stability theorems. BIT, vol.18, pp. 475-489. [IV.4], [IV.6], [V.4]

G.Wanner, E. Hairer & S.P. Nprsett (1978):When $I$ -stability implies A-stability. BIT, vol. 18, p. 503. [IV.4]

G. Wanner, see alsoE.Hairer & G. Wanner; P. Kaps & G. Wanner; S.P.Nprsett& G. Wanner; G. Sottas & G. Wanner.

W. Wasow (1965): Asymptotic expansions for ordinary diferential equations. Interscience, John Wiley& Sons,New York,263pp. [VI.3]

D.S. Watkins & R.W. HansonSmith (1983): The numerical solution of sparably stiff systems by precise partitioning. ACM trans. Math. Soft., vol. 9, pp. 293-301. [IV.10]

H.A. Watts, see L.F. Shampine & H.A. Watts.

R.A. Wehage & E.J. Haug (1982): Generalized coordinate partitioning for dimension reduction in analysis of constrained dynamic systems.J. Mechanical Design, vol. 104, pp. 247- 255. [VII.2]

K. Weierstrass (1868): Zur Theorie der bilinearen und quadratischen Formen. Akad. der Wiss. Berlin 18.Mai. 1868,Werke vol. II, pp. 19-44. [VI.1]

R.Weiner, see K. Strehmel & R.Weiner.

D.V. Widder (1946): The Laplace Transform. Princeton University Press,London. [IV.11]

O.B. Widlund (1967): A note on unconditionall stable linear multistep methods. BIT, vol.7, pp. 65-70. [IV.3], [v.1], [V.2]

J.H. Wilkinson (1965): The Algebraic Eigenvalue Problem. Clarendon Press, Oxford, 662 p. [IV.2]

R.A Williamson, see A. Iserles & R.A Williamson.

R.A. Willoughby (ed.) (1974): Stif Differential Systems.Plenum Press, New York. [IV.1]

R.A. Willoughby, see also W.Liniger & R.A. Willoughby.

A. Wolfbrandt (1977): A study of Rosenbrock processes with respect to order conditions and stiff stability.Thesis, Chalmers Univ. of Techn., Goteborg,Sweden.[IV.4], [IV.7]

A.Wolfbrandt, see also S.P. Nprsett & A. Wolfbrandt; T. Steihaug & A. Wolfbrandt.

K. Wright (197O): Some relationships between implicit Runge-Kutta, collocation and Lanczos T methods, and their stability properties. BIT, vol. 10, pp.217-227. [IV.3]

J. Yen (1993): Constrained equations of motion in multibody dynamics as ODEs on mani-folds. SIAM J. Numer. Anal., vol. 30, pp. 553-568. [VII.2]

E.L. Yip, see R.F. Sincovec, A.M. Erisman, E.L. Yip & M.A. Epton.

H. Yoshida (1990): Construction of higher order symplectic integrators. Phys. Lett. A, Vol.150, p.262-268. [VII.8]

S. Yoshizawa, see J. Nagumo, S. Arimoto & S. Yoshizawa.

Yuan Chzao Din (1958): Some diffrence schemes of solution of first boundary problem for linear diferential equations with partial derivatives, (in Russian) Thesis cand.phys. math. Sc., Moscov MGU 1958.

E.C. Zeeman (1972): Diffrential equations for the heartbeat and nerve impulse. Published in Towards a theoretical biology (Edited C.H. Waddington) Edinburgh University Press, Volume 4, pp. 8-67. Reprinted in Catastrophe theory, Selected papers 1972-1977, Addison-Wesley 1977, pp. 81-140. [IV.10]

J. Zugck,see P. Deufhard, E. Hairer & J. Zugck.

# Symbol Index

A order star, 51, 285.   
A@J tensor product, 216, 331.   
B relative order star, 59, 67,287.   
$B ( p )$ simplifying assumption, 71, 363.   
$C$ error constant, 42, 248,262.   
$C ( \eta )$ simplifying assumption, 71, 363.   
$\mathbb { C } ^ { + }$ positive half plane, 52.   
C- negative half plane, 56.   
$C ( \mu )$ companion matrix, 323.   
DAT,DAT2 sets of differential algebraic trees, 410, 507.   
DAT DAT2 sets of differential algebraic trees,410, 507.   
$D A T _ { z }$ ， $D A T 2 _ { z }$ sets of differential algebraic trees, 410, 507.   
$D ( \xi )$ simplifying assumption, 71.   
$D _ { A } ( \boldsymbol { \xi } )$ simplifying assumption, 363.   
$D _ { B } ( \boldsymbol { \xi } )$ simplifying assumption, 363.   
$d i$ differentiation index, 455.   
$D _ { r }$ disc of radius $\pmb { r }$ ,254.   
$E ( y )$ $E$ -polynomial, 43, 96.   
$F ( t )$ elementary differential,106, 410, 508.   
Fourier transform, 255.   
$H ( p , q )$ Hamilton function, 543.   
$K _ { a } ( s )$ Peano kernel, 254.   
$\bar { \kappa ( Z ) }$ stability function for $y ^ { \prime } { = } \lambda ( x ) y$ ,185.   
LDAT, LDAT2 sets of differential algebraic trees, 411, 509.   
$L D A T _ { y }$ ， $L D A T 2 _ { y }$ sets of differential algebraic trees,411, 509.   
$L D A T _ { z } ^ { * }$ ， $L D A T 2 _ { z }$ sets of differential algebraic trees, 411,509.   
$\ell _ { \ i } ( t )$ Lagrange polynomial, 499.   
$L ( q , \dot { q } )$ Lagrange function, 13, 463.   
$L _ { s } ( x )$ Laguerre polynomial, 96.   
$L T _ { q }$ set of labelled trees of order $q$ ,106.   
$P$ projection, 494.   
$p _ { D }$ differentiation order, 315.   
$p i$ perturbation index, 459.   
$p _ { I }$ interpolation order, 315.   
P(x） (shifted) Legendre polynomial, 78, 202. $Q$ projection, 494.   
Q(μ,S） characteristic polynomial, 282,291.   
Rkj(2） Padé approximation, 48.   
$R ( \dot { z } )$ stability function,16,40,41,108,132.   
r(） coefficient of discrete resolvent, 332,353, 385.   
r(s,） discrete resolvent, 332, 353.   
$S$ stability domain, 16, 241.   
$S ^ { s c a l }$ scaled stability domain, 60.   
$S ( Z )$ stability matrix, 353.   
$S _ { \alpha }$ sector of $A ( \alpha )$ -stability, 250.   
$S ( \mu )$ stability matrix, 290.   
$T$ kinetic energy, 463, 531.   
$T$ set of trees, 116.   
$T _ { m } ( z )$ Chebyshev polynomial, 31.   
$T W$ set of trees for $W$ -methods, 115.   
T(m,S） property $T$ ,81.   
$U$ potential energy, 463,533.   
ullD norm,218.   
norm in product space, 216, 218.   
ulG norm in product space, 330.   
lla inner product norm, 307,356.   
αD(A-1) coercivity coefficient, 215.   
α(A-1) coercivity coefficient, 215.   
8D（x） differentiation error, 314.   
local error,226,227,228,323.   
8(c） interpolation error, 314.   
SLM(x) linear multistep error, 322.   
oL（） one-leg error, 314.   
μ（A) logarithmic norm,168.   
$\mu ( \zeta )$ multiplier, 343.   
$\nu$ one-sided Lipschitz constant, 180,215, 305,339.   
$\varrho$ threshold factor, 176.   
$\varrho ( t )$ order of a tree,410, 508.   
$\varrho ( \zeta )$ generating polynomial, 240.   
$\sigma ( \zeta )$ generating polynomial, 240.   
$\varphi _ { B } ( \ell )$ error growth function, 193.   
R(c error growth function (linear problems),169.   
V backward difference operator, 242.

# Subject Index

$A$ -acceptable approximations, 43.   
$A$ -stability of multistep methods, 241. of one-step methods,42f. of Padé approximations, 58. of rational approximations, 56f. of SDIRK methods, 97. via positive functions,87.   
$A ( 0 )$ -stable multistep methods,250.   
$A _ { 0 }$ -stable multistep methods,251.   
$A ( \alpha )$ -stability of BDF methods, 251. of blended methods,267. of Enright methods,263. of extrapolation methods,137, 139. of modified EBDF methods,270. of multistep methods,250. of multistep Radau methods, 276. of RK methods, 45. of second derivative BDF methods, 265.   
$A ( \alpha )$ -stable multistep methods of high order,251f.   
absolutely monotonic functions, 178.   
acceleration level, 465.   
accuracy barriers for linear multistep methods,254f.   
Adams methods,242f, 249,266.   
adjoint differential equation, 462, 467.   
algebraic criterion for $G$ -stability, 309.   
algebraic stability, of general linear methods, 356f. of multivalue methods,366f. of RK methods,181f, 188,206,232.   
amplifier, 376f, 379.   
Andrews’ squeezer mechanism, 530f.   
$A N$ -stability, of RK methods 184f, 200. of general linear methods,360.   
asymptotic expansions, 135,428f, 433, 525f.   
asymptotic solution of van der Pol's equation, 372.   
automatic stiffness detection, 21.   
backward differentiation formulas, see BDF   
backward error analysis for ODEs, 555f. on manifolds, 559f.   
Bader-Deuflhard method,134f.   
Baumgarte stabilization, 470.   
$B$ -convergence, 225. of $G$ -stable one-leg methods,316. of multistep methods,368f. of order r,231. of RK methods, 225f. of trapezoidal rule, 234. of variable step sizes,230.   
BDF methods,2-3,239,246, 259,266,280, 285,296,308,477, 481,528, 538.   
BEAM,146,153,155f,159,300,302.   
beam equation, 8f, 11f, 20, 38f, 46,146.   
BECKDO, 149f,152, 155f,300.   
Becker-Doring model, 149f.   
Bernstein's inequality, 324.   
$\beta$ -blocked multistep methods, 527.   
blended multistep methods, 266.   
boundary layer terms,389.   
BRUSS,148,155f,159f,300,302.   
Brusselator, 6, 19,31, 148.   
BRUSS-2D,151f,157f,160,300.   
$B$ -stability of Radau IIA, 199. of RK methods, 180f, 188,201. of Rosenbrock methods,200.   
Burgers equation, 349f, 443f, 448.   
Cary Grant’s part, 62.   
Cash's algorithm,268.   
characteristic equation for general linear methods,291. for linear multistep methods,240. for multistep RK methods,282. for predictor-corrector schemes, 244.   
characterization of algebraically stable methods,209. of positive quadrature formulas,205.   
Chebyshev method, 31f. of second order, 34f.   
Chebyshev polynomial, 31f.   
chemical reactions, 3.   
Christoffel-Darboux formula,130.   
circuits,4,376,379.   
coercivity coefficient 215,368.   
collocation methods for index 2 DAE,498. multi-step, 270f. one-step,47,78. projected, 503. singly implicit, 129.   
companion matrix, 323.   
comparing stability domains, 58.   
comparison between Chebyshev methods,160. between extrapolation methods,159f. between IRK methods,158f. between Radau codes, 158f. between Rosenbrock codes,158f.   
composite multistep methods, 267.   
composition methods 50, 554f.   
consistent initial values for index 1,374,378. for index 2, 456. for mechanical systems, 535.   
constrained mechanical system, 464,469f, 4 524,543.   
construction of IRK methods, 83.   
continued fraction representation, 50, 85.   
continued fractions related to quadrature fol mulas, 201f.   
continuous solution, see ‘dense output'   
contractivity for linear problems,167f. in general norms, 175. see also $^ { \bullet } B$ -stability'   
control problems,461f.   
convergence for linear problems,321f. for nonlinear problems,339f. of $A$ -stable multistep methods, 317f. of BDF for index 2,486. vi μun vpuvit Iu) IIvuIvuv, Jz1. of multistep methods for index 2,489. of multistep methods for SPP,383f. of RK for index 1,380. of RK for index 2 DAE,496f,504. of RK methods for DAE, 394f. of RK methods for SPP, 402. of symplectic methods, 547,549. see also $i \ B$ -convergence'   
coordinate partitioning, 476, 478f.   
counter-examples for existence, 217. for index definitions,460f. for stability properties, 199.   
criterion for $G$ -stability, 309.   
CUSP, 147,300, 302.   
cusp catastrophe, 147.   
DAE, 373, 451. overdetermined, 477.   
Dahlquist's first barrier, 299.   
Dahlquist's second barrier, 247,286,297,299   
Dahlquist's test equation, 16, 240.   
damped Chebyshev methods, 32f.   
Daniel-Moore conjecture, 51, 286, 294,298, 364.   
DASSL,481, 538, 541.   
DEABM, 5, 6.   
DEBDF,301f.   
dense output, 576. of DAE extrapolation methods, 438f. of DAE Rosenbrock methods,422. of Enright methods, 263f. of multistep collocation methods, 272. of SDIRK4, 100.   
derivative feedback (D), 28.   
derivative array equations, 478.   
descriptor form, 464.   
diagonally implicit RK methods,91f.   
difference-corrected BDF, 528.   
differential-algebraic equations,see DAE.   
differential equations linear, 167, 321. nonlinear, 180,339. of singular perturbation type, 371f. on manifolds, 457,474f, 544. perturbed, 556. quasilinear, 442, 576. second order, 575. stiff,2f. Witn invariants, 4 / ∠I.   
differentiation index,455,478.   
differentiation error, 314. order, 315,319.   
diffusion, 6.   
DIRK,61,91f,208,221.   
disc theorem, 58, 254.   
discrete resolvent, 332.   
discrete variation of constants formula, 332, 348f.   
$D J$ -reducible RK methods, 187.   
dominant invariant subspace, 161.   
DOPRI5,3,19,22f,25f,30,143,153f,469, 471. for mechanical system, 537.   
DOP853,11f,18,20,26,29. for mechanical system, 537.   
Dormand & Prince methods,27.   
Dorodnicyn's asymptotic formula, 374.   
drift-off phenomenon, 468f.   
dual order stars,295.   
DUMKA, 34f.   
efficiency diagram,154f,159f,301f,537,539.   
EKBWH-method,163f.   
elastic beam, 146.   
electrical circuits,4, 376, 379.   
elementary differentials, 106. for index 1 DAE,410. for index 2 DAE,508.   
embedded formula for RADAU5, 123.   
Enright & Kamel method,163f.   
Enright methods,261f,266,275f.   
$E$ -polynomial, 43, 96f. for Padé approximation,70.   
$\varepsilon$ -embedding method,374,382,407,426.   
$\varepsilon$ -expansions for SPP for exact solution, 388. for RK solution, 392f.   
equivalence between stability concepts,186,188. of $A$ and $B$ stability, 211. of $A$ and $G$ -stability, 310f.   
error local,226,228f,405,494. global 226,321,328,399,403f.   
error bounds for one-leg methods,314f.   
error constant, 247,286f. of rational approximations,42,52,61,67. of second derivative multistep methods, 262 for SDBDF methods,265.   
eIrur gruwu iuncuon, 1yəl, zuu, ∠∠y. for linear problems,169f. superexponential, 171,194.   
error propagation, 229.   
Euler equations, 463.   
Euler's method 2,15,45,58. explicit, 2, 15, 556. half-explicit, 519, 525. implicit,3,45,169,247,491, 557. symplectic, 545, 557.   
Euler's polyhedral formula, 57.   
EULSIM, 140, 160.   
existence of multistep solutions,306f, 482. of numerical RK solutions,215f,397,521, 546.   
expansion of SPP solutions, 388f.   
experiments with multistep codes,300.   
explicit Adams methods,242f. Euler method,2,15. Runge-Kutta methods,16. midpoint rule, 245,249. Nystrom methods,245.   
exponential fitting points,56.   
extended BDF methods,267.   
extended multistep methods,267f.   
extrapolation methods,18,131. for index 1 DAE,426f. for quasilinear DAE,447. GBS, 18.   
E5,145,153f,300f.   
first integral, 472   
Fortran codes, 565.   
Fourier transform, 148,255. fast (FFT), 149, 157.   
Gauss methods,71,181,184,198,200,220, 226,504.   
Gaussian quadrature formulas, 202.   
Gear & Saad method, 161f.   
general linear methods,290f. algebraic stability of,356f.   
generalized multistep methods, 261.   
generating polynomials,240.   
GGL formulation of mechanical system, 465, 478.   
global error, 226. expansion for SPP, 399. for Prothero & Robinson problem,328. of linear multistep methods, 321. of one-leg methods,322.   
Graeco-Roman transformation, 256.   
Green's function, 9.   
GRK4A, 110.   
Gron wall lemma, 460.   
$G$ -stability, of one-leg methods,307f. of BDF2 method, 308,312. of general linear methods, 356.   
half-explicit methods,519f. extrapolation methods, 525. multistep methods,527. Runge-Kutta methods, 520.   
Hamiltonian function, 473,543. perturbed, 558.   
Hamiltonian systems,472f. constrained, 543f. perturbed, 558.   
hanging rope, 13f.   
HEM5, 538.   
Hermite interpolation,271.   
Hessenberg form, 122.   
HEX5, 538.   
hidden manifold, 454.   
high order $A ( \alpha )$ -stable multistep methods, 251f.   
high oscillations, 11.   
HIHA5,method of Higham & Hall, 26f.   
HIRES,144f,152f,159f,300f.   
HLR89,459   
hump,113,405.   
hybrid multistep methods,267.   
hyperbolic problems, 37,51.   
implementation of extrapolation schemes, 139f. of IRK methods,118f. of Rosenbrock methods, 111.   
implicit Adams methods,243. Euler method,3,45,169,247,491. midpoint rule,131,306. Milne-Simpson methods, 245,249. RK methods,40f, 71f.   
implicit differential equations $\mathbf { \bar { \boldsymbol { M } } } \mathbf { \boldsymbol { u } } ^ { \prime } = \varphi ( \mathbf { \boldsymbol { u } } )$ ，103,127,141,376,378f, 408,426. $M ( u ) u ^ { \prime } { = } \varphi ( u )$ ,442f, 460, 576. $F ( u ^ { \prime } , u ) = 0$ ,452, 459, 478.   
inconsistent initial values for DAE Rosenbrock methods,422f.   
index,452f. differentiation, 454f. index 1,371f,374,445,455,459,< 537. index 2, 456, 458,460, 464, 519, 537. index 3,456,458,464,537. of nilpotency, 454. perturbation, 459.   
index reduction, 468f.   
inexact Jacobian, 114.   
influence of perturbations,218, 484,493.   
integral feedback (I),28.   
interpolation error, 314. order, 315,319.   
invariants, 472.   
IRK(DAE), 376.   
irreducible RK methods, 187.   
$I$ -stability, 43.   
Jeltsch-Nevanlinna theorem, 60,289.   
kinetic energy,8f,463, 531. of mechanical systems, 531, 541.   
Kirchhoff's law, 376.   
Kreiss matrix theorem,323.   
Kreiss problem, 542.   
KS,148f,300,302.   
Kuramoto-Sivashinsky equation, 148.   
Kuntzmann-Butcher methods,42f,71.   
labelled trees,105,411,509.   
LADAMS, 301f,304.   
Lagrange multipliers,196f,464.   
Lagrange theory, 8,13, 463.   
Lagrange-Hamilton principle, 463.   
Laguerre polynomials 96, 129f.   
Lebedev's realization, 33.   
Legendre polynomials,71,78, 202.   
LIMEX, 448.   
linear problems contractivity, 167f. index, 452f, 455.   
linearly implicit Euler method,138f. Euler for index 1 DAE,426f. Euler for quasilinear DAE, 448. midpoint rule, 134f, 441. RK method,102.   
Lipschitz constant, 23. one-sided, 180.   
Lobatto IIA methods,42f,75f,185，211, 222,226,504.   
Lobatto IA-IB pair, 549f, 563.   
Lobatto IIB methods,75f,185,211,222 226.   
Lobatto IIIC methods,75f,184，198,220 223,226,403f, 504.   
local coordinates,475.   
local error,226, 228f, 485,494.   
local state space form, 474.   
logarithmic norm 168,390.   
LSODE,143,153f,300f.   
LSODI, 481.   
$L$ -stability, 44. of SDIRK methods, 98.   
manifold, 457.   
matrix pencil, 452, 466.   
MEBDF,303f.   
mechanical system, 463, 530f.   
METAN1, 140.   
metastability, 150.   
MEXX for mechanical system, 538.   
midpoint rule,245,249.   
Milne-Simpson methods,245,249.   
monotonically labelled trees,105,411, 509.   
Montaigne's ruff, 287.   
moving finite elements,442f.   
multibody mechanisms,530.   
multiderivative multistep methods,282.   
multiple real-pole approximations,67, 98f.   
multiplier, 342f. and nonlinearities, 346. construction of, 344f.   
multistep collocation methods,270f. as general linear method, 272. $G$ -stability of, 361.   
multistep methods, 239f. $\beta$ -blocked, 527. for index 1,382f. for index 2, 481. for quasilinear DAE,446f. of Radau type, 273.   
multistep Runge-Kutta methods, 281,362.   
multistep twin, 306.   
Ai-icr Ωtairon oauotiong 251 non-autonomous ODE,103,141,408.   
nonlinear perturbations,172.   
number of positive weights of QF, 203f.   
numerical experiments, 143,300,403t, 536t.   
numerical work and poles,283.   
Nystrom methods, 245.   
ODE, see differential equations.   
ODEX, 6,7.   
one-leg multistep methods,305f. error bounds for, 314.   
one-sided Lipschitz condition,180f, 215,305, 339, 356.   
one-sided Lipschitz constant, 180.   
one-step methods, 1f.   
optimal control problems,461f, 467.   
optimal stability regions, 31f.   
order conditions for DAE Rosenbrock methods,415. for index 2 DAE,506f,512,523. for Rosenbrock methods,104f. for SDIRK methods,91f.. for second derivative multistep methods, 261.   
order of a tree,410, 508.   
order of $B$ -convergence, 231.   
order of a quadrature formula, 202.   
order reduction, 225. for Rosenbrock methods,236.   
order stars, 51f. dual, 295. for BDF2, 285. for general linear methods, 290. for multistep methods,279,284f. for one-step methods, 51. for Padé approximations, 53. for SDIRK methods,55,101. relative, 59,69, 287.   
order tableau for DAE extrapolation methods,431f, 441.   
OREGO,144,152f,159,300f.   
Oregonator, 13.   
overdetermined DAE, 477.   
Padé approximations to $e ^ { z }$ ,48f, 170.   
parabolic problems,31f, 349f.   
Parseval identity,255,259.   
partitioned Rosenbrock methods,425.   
partitioning methods,160.   
Peano kernel, 254f.   
pendulum, 463f, 468, 474.   
perturbation index, 459.   
perturbations of linear quations, 348.

of RK solutions,219,398. perturbed asymptotic expansions, 428f, 434, 448. perturbed differential equation, 556. perturbed Hamiltonian system, 558. PHEM56, 538. PI step size control, 28. PLATE,146,152f,300f. plate differential equation,146. poles representing numerical work, 283. position level, 464. positive functions, 86f, 313. positive quadrature formulas,183,201,205. potential energy, 8f, 463, 533. of mechanical systems, 533,541. preconsistency, 359. predictive controller, 124. predictor-corrector schemes, 244. principal root, 285. principal sheet, 285,292. projected collocation methods, 503. projected Runge-Kutta methods, 502, 515f. projection methods,160. for DAE,470f. for ODEs with invariants,473. projections (index 2),487,494f. property $C$ ,288f. property $T$ ,81. proportional feedback (P), 28. Prothero-Robinson problem,153, 225,328, 427. quasilinear differential equation, 442f, 576. index 1, 445. Radau IA,72,184,220,226,403f,504. Radau IIA,74,184,197,220,226,403f,504. Radau methods of multistep type, 273. RADAUP, 158f, 574. RADAU5,4f,46,118f,143,153f,379, 566f. for mechanical system, 539,541. rational approximations with real poles,61. RATTLE,548f. real-pole sandwich,62. red-black reduction,165. reduced system,372, 374,388. reducible RK methods,187f. region of absolute stability,see ‘stability domain' region of step-control stability, 26f. regular matrix pencil, 452, 466.

relative order star, 59,69,287.   
relative separation, 161.   
resolvent (discrete),332.   
Riemann surfaces,279f.   
RKC,36,143, 153f.   
RKF4(5), 25.   
RKF5(4), 24, 26.   
ROBER,144,152f,159,300f.   
Robertson reaction, 3,18,144.   
RODAS,143,153f, 158f,420f, 574.   
RODAS5,143,158f, 422.   
root locus curve, 241f. for BDF methods,246. for Enright methods, 263. for explicit Adams methods, 243. for implicit Adams methods, 243. for Miine-Simpson methods, 245. for Nystrom methods, 245f. for SDBDF methods,265.   
ROS4, 143.   
Rosenbrock methods,172f. comparisons, 158f. contractivity, 172f. for stiff problems,102,102f. for DAE, 407f, 447. order reduction, 236. with inexact Jacobian, 114.   
rotation number, 204.   
Routh criterion, 89.   
Runge-Kutta methods explicit, 16. for index 1 problems,375. for index 2 DAE,492f. for quasilinear DAE, 446f. for SPP, 392f. half-explicit, 520. implicit, 40f, 71f. projected, 502,515f.   
savings in linear algebra, 540.   
scaled stability domain, 60.   
Schur's criterion, 278.   
SC-stability, 24f. for Dormand & Prince methods,27.   
SDBDF, 265.   
SDIRK code, 128.   
SDIRK method,42,44,91,183,208,403 504.   
SDIRK4,100,143,158f.   
SECDER,303f.   
second Dahlquist barrier, 247,254.   
second derivative BDF methods,265.   
second derivative multistep methods,261.   
separably stiff problems,161.   
SEULEX,140,143,153f,160, 575.   
SHAKE, 548.   
simplified Newton, 119f,490.   
simplifying assumptions,71,80f,183, 206f, 363. for index 2 DAE,514.   
singly diagonally implicit RK methods,91.   
singly implicit RK methods,128f.   
singular perturbation problems,371f, 433.   
SIRK-methods,128f.   
smoothing step for extrapolation, 133.   
SODEX,140, 143,160.   
SOLOUT, 576.   
SPP, see singular perturbation problems.   
SPRINT,301f,304,481.   
$S$ -reducible RK methods,188.   
stability analysis for Euler's method,15. for explicit RK methods, 16f. for modified EBDF methods,269. for multistep methods,240f. for multistep Radau methods, 274f. for multistep Runge-Kutta methods, 281f.   
stability domain,16. cross-shaped 39. of Bader-Deuflhard method, 134. of BDF methods,246. of modified EBDF methods,270. of Chebyshev methods, 32f. of DOPRI methods,17. of Enright methods,263. of ERK methods, 17. of explicit Adams methods,243. of extrapolated Euler, 139. of extrapolated trapezoidal rule,132. of GBS extrapolation,19. of implicit Adams methods,243. of implicit Euler method, 246. of Milne-Simpson methods, 246. of multistep methods,240f. of multistep Radau methods, 276. of Nystrom methods, 246. of Padé approximations,52. of predictor-corrector schemes, 245.   
stability function $R ( z )$ ,16,84. of Chebyshev methods,32f. of collocation method, 47. of DIRK methods, 61. of DOPRI5, 17, 26. of DOP853, 18. of extrapolation methods,132f. of IRK methods,40, 84. of order $\geq s$ ,47. of Rosenbrock methods,108. of SDIRK methods, 67, 96f.   
stability function for $y ^ { \prime } = \lambda ( x ) y$ of IRK methods, 184f.   
stability region, see stability domain.   
stabilization Baumgarte, 470. by projection, 470. velocity, 471f.   
stabilized explicit methods, 31f.   
stage order,226,369.   
starting values for Newton iteration,120.   
state space form,374f, 474.   
state space form method, 375f, 383.   
step size selection, 123f. predictive, 124.   
step-control stability, 24f.   
stiff, 1f.   
stiff eigenvalues,161.   
stiff eigenvectors,161.   
stiff mechanical system, 541.   
stiff stability of multistep methods, 250.   
stiff-detest, 144.   
stiffly accurate, 227,552. RK methods,45, 376. Rosenbrock methods, 418f. SDIRK methods, 92f.   
stiffness, 2, 151. detection, 21.   
stopping criterion,120. for Enright & Kamel method,164.   
STRIDE, 129.   
Sullivan, Leon, 9.   
superconvergence, 500, 554.   
superexponential, 171,194.   
super-future point, 267.   
symplecticity, 544, 547.   
symplectic methods,543f. Euler,545,561. Lobatto IIA-IB, 550,563. second order, 548f, 558,561f.   
tangent space parametrization, 476.   
Taylor expansion for index 2 DAE,508f. of DAE Rosenbrock solution, 412f.