# Part I

Classical dynamics

# Linear dynamical systems

Linear dynamical systems and their discrete counterparts, linear maps, have complete explicit solutions. In the former case these are the basis for approximating the motion near points of equilibrium of nonlinear systems. A similar theory for maps elucidates the motion surrounding periodic orbits,as a consequence of the Poincare section, to be introduced in chapter 2.We shallfirst review the motion of nonconservative systems and then consider the restrictions peculiar to Hamiltonian systems. The importance of the linear flow on a torus, discussed in section 1.3,will manifest itself fully only through the study of integrable systems in chapter 6but it providesaready example ofthe concept ofergodicitytobe developed in chapter 3. Even more important, as a point of departure for the study of chaotic motion, is the study of linear maps of the torus in section 1.4. In spite of the elementary nature of the mathematical techniques employed,it willthus befound that this initial chapteris the germor the whole of Part I.

A dynamical system is defined as a set of $N$ first-order differential equations in $N$ variables $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { N } )$ (these are said to determine a point in phase space, the Euclidean space $\mathbb { R } ^ { N }$ ,unless otherwise stated):

$$
d \mathbf { x } / d t \equiv \dot { \mathbf { x } } = \mathbf { f } ( \mathbf { x } , t ) .
$$

The system willbe autonomous if the vector field f is independent of $t$ ,the time. A solution of the dynamical system is a vector function $\mathbf { x } ( \mathbf { x } _ { 0 } , t )$ satisfying (1.1) and the initial condition

$$
\mathbf { x } ( \mathbf { x } _ { 0 } , 0 ) = \mathbf { x } _ { 0 } .
$$

Often we omit the dependence on the initial condition and refer to the solution simply as ${ \bf x } ( t )$

An important class of solutions is that of the points of equilibrium $\mathbf { x } _ { e }$ for which $\mathbf { f } ( \mathbf { x } , t ) = 0$ .The expression of the vector field in a Taylor series,

$$
\mathbf { f } ( \mathbf { x } , t ) = { \frac { \partial \mathbf { f } ( \mathbf { x } _ { \mathrm { e } } , t ) } { \partial \mathbf { x } } } ( \mathbf { x } - \mathbf { x } _ { \mathrm { e } } ) + { \frac { 1 } { 2 } } ( \mathbf { x } - \mathbf { x } _ { \mathrm { e } } ) { \frac { \partial ^ { 2 } \mathbf { f } ( \mathbf { x } _ { \mathrm { e } } , t ) } { \partial \mathbf { x } ^ { 2 } } } ( \mathbf { x } - \mathbf { x } _ { \mathrm { e } } ) + \cdots
$$

(where df/dx is the Jacobian matrix), can be truncated soas to yield a good approximation of the motion near equilibrium, even if the Taylor series does not converge. For an autonomous field the first approximation to the dynamical system is brought into the form

$$
\dot { \mathbf { x } } = \mathcal { A } \mathbf { x }
$$

by changing the origin of coordinates to $\mathbf { X } _ { \mathrm { e } }$ and defining the dynamical matrix $\mathcal { A } = \hat { \sigma } \mathbf { f } ( 0 ) / \hat { \sigma } \mathbf { x }$ .In the remainder of this chapter we will study the solutions of the linear system (1.4), without any reference to the possible nonlinear systems that it may approximate.

# 1.1 General linear systems

The solution of the linear system (1.4) is simply

$$
\mathbf { x } ( \mathbf { x } _ { 0 } , t ) = \exp ( t \mathcal { A } ) \mathbf { x } _ { 0 } ,
$$

as follows from the series expansion of the exponential matrix

$$
\exp ( t \mathcal { A } ) = 1 + t \mathcal { A } + \frac { t ^ { 2 } } { 2 } \mathcal { A } ^ { 2 } + \cdots + \frac { t ^ { n } } { n ! } \mathcal { A } ^ { n } + \cdots .
$$

The general solution of the linear system is a linear superposition of $N$ linearly independent solutions $\{ \mathbf { x } ^ { 1 } ( t ) , \ldots , \mathbf { x } ^ { N } ( t ) \}$

$$
{ \mathbf x } ( t ) = \sum _ { n = 1 } ^ { N } C _ { n } { \mathbf x } ^ { n } ( t ) ,
$$

where the coefficients $C _ { n }$ are determined by the initial condition.

The nature of the flow around the equilibrium at the origin depends exclusively on the eigenvalues $\left. \lambda _ { 1 } , \ldots , \lambda _ { N } \right.$ of the dynamical matrix. Ifall the eigenvaluesare real and nondegenerate, the matrix can be diagonalized by a real linear transformation. This wil also diagonalize the solution matrix $\mathrm { e x p } ( t \mathcal { A } )$ ,the eigenvalues of which are $\{ \exp ( t \lambda _ { 1 } ) , \ldots , \exp ( t \lambda _ { N } ) \} .$ Given $\xi _ { n } ,$ the eigenvectors of $\mathcal { A }$ , we then have $N$ independent solutions:

$$
\begin{array} { r } { { \bf x } ^ { n } ( t ) = \exp { ( \lambda _ { n } t ) } \xi _ { n } . } \end{array}
$$

A simple example from Arnold (1973) helps to bring home the idea: Let

$$
\scriptstyle \mathcal { A } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] }
$$

in an arbitrary basis (e1,e2). The eigenvalues are then {2,O), with eigenvectors 51 =e1 +e2 and 52=e1 -e2. In the basis of (51,52) the

solution matrix is just

$$
{ \left[ \begin{array} { l l } { \exp ( 2 t ) } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } ,
$$

so the general solution is

$$
\begin{array} { c } { { \mathbf x ( t ) = c _ { 1 } ( 1 , 1 ) \exp ( 2 t ) + c _ { 2 } ( 1 , - 1 ) } } \\ { { = ( c _ { 1 } \exp ( 2 t ) + c _ { 2 } , c _ { 1 } \exp ( 2 t ) - c _ { 2 } ) . } } \end{array}
$$

If there are any complex eigenvalues, the dynamical matrix can be diagonalized only by a complex linear transformation. It is thus useful to complexify the dynamical system. This procedure is also valid for the general system (1.1), which takes the form

$$
\dot { { \mathbf { z } } } = { \mathbf { f } } ( { \mathbf { z } } , t ) ,
$$

where z belongs to $\mathbf { C } ^ { N }$ a space of $N$ complex variables. So if the vectors $\left\{ \mathbf { e } _ { 1 } , \ldots , \mathbf { e } _ { n } \right\}$ form abasis in thereal space $\mathbb { R } ^ { N }$ the vectors $\{ { \bf e } _ { 1 } + i \bf { 0 } , \ldots , { \bf e } _ { N }$ $+ i 0 \}$ form a basis in $\mathbf { C } ^ { N }$ The expansion of an arbitrary complex vector,

$$
\zeta = \sum _ { n = 1 } ^ { N } z _ { n } \mathbf { e } _ { n } ,
$$

is then obtained from the rule for the multiplication of a vector by a scalar:

$$
( u + i v ) ( \xi + i \pmb { \eta } ) = ( u \xi - v \pmb { \eta } ) + i ( v \xi + u \pmb { \eta } ) .
$$

The vector $\xi + i 0$ will hereafter be abbreviated $\xi$

The vector field f is still a set of real functions, so that its complex conjugate field $\mathbf { f } ^ { * }$ is given by

$$
\mathbf { f } ^ { * } ( \mathbf { z } , t ) = \mathbf { f } ( \mathbf { z } ^ { * } , t ) .
$$

This leads to the fundamental property of the complexified system: If ${ \bf z } ( { \bf z } _ { 0 } , t )$ is a solution, then ${ \mathbf { z } } ^ { * } ( { \boldsymbol { \mathbf { \mathit { x } } } } _ { 0 } , t )$ is also a solutionas shown in $\mathrm { f i g } \langle \widetilde { 1 . 1 } . \rangle \mathrm { f } \mathbf { \mathrm { \pmb { z } } } _ { 0 }$ is real, the uniqueness theorem for differential equations entails that $\overline { { { \bf { z } } ( { \bf { z } } _ { 0 } , t ) } }$ is real for all time. In the specific case of the linear system

$$
\dot { \mathbf { z } } = \mathcal { A } \mathbf { z } ,
$$

with $\mathcal { A }$ a real matrix, the equality

$$
\mathcal { A } ( \mathbf { x } + i \mathbf { y } ) = \mathcal { A } \mathbf { x } + i \mathcal { A } \mathbf { y }
$$

implies that, if ${ \bf \delta z } ( { \bf z } _ { 0 } , t )$ is a solution of the system (1.13), then the real and imaginary parts are solutions of the real system(1.4).Therefore,wecan find the real solutions from the complex solutions and vice versa; that is,

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/a508dbcc1bdbc106e0766419ee4480c2ea8e932c6644219468b9aeb2b0212951.jpg)  
FigC1.i.)he vectorfeldiseal; ten (zt)beingacomplex soutiolie that $\overline { { { \pmb { x } } ^ { * } ( { \pmb { x } } _ { 0 } , t ) } }$ is also a solution.

we have

$$
{ \bf z } ( { \bf z } _ { 0 } , t ) = { \bf x } ( { \bf x } _ { 0 } , t ) + i { \bf y } ( { \bf y } _ { 0 } , t ) .
$$

The reader should consult Arnold (1973) for a fuller discussion of complexification.

The solutions of the complex system(1.13)are of the same form as the real solutions. Therefore, there is a complex solution $\exp ( { \lambda _ { n } t } ) \zeta _ { n }$ for every eigenvalue $\lambda _ { n }$ ,whether real or complex,and the general solution is

$$
\mathbf { z } ( t ) = \sum _ { n = 1 } ^ { N } C _ { n } \exp ( \lambda _ { n } t ) \boldsymbol { \zeta } _ { n } .
$$

The complex conjugate of this expression is also a general solution,

$$
{ \bf z } ^ { * } ( t ) = \sum _ { n = 1 } ^ { N } C _ { n } ^ { * } \exp ( \lambda _ { n } ^ { * } t ) \zeta _ { n } ^ { * } ,
$$

so complex eigenvalues must come in pairs $\lambda _ { n } , \lambda _ { n } ^ { * }$ with corresponding eigenvectors $\zeta _ { n } , \zeta _ { n } ^ { * }$ We conclude that,if the numberof real eigenvalues is $N _ { \scriptscriptstyle \mathrm { R } }$ and the number of pairs ofcomplex eigenvectors is $N _ { \mathbf { C } }$ $N = N _ { \mathrm { R } } + 2 N _ { \mathrm { C } } )$ the general solution of a real system with distinct eigenvalues is

$$
{ \mathbf x } ( t ) = \sum _ { n = 1 } ^ { N _ { \mathbb { R } } } a _ { n } \exp ( \lambda _ { n } t ) { \boldsymbol \xi } _ { n } + \sum _ { n = 1 } ^ { N _ { C } } \operatorname { R e } \big \{ C _ { n } \exp ( \lambda _ { n } t ) { \boldsymbol \zeta } _ { n } \big \} ,
$$

where $\operatorname { R e } { \{ \begin{array} { l } {  } \end{array} \} }$ denotes the real part of a complex number. Each real eigenvector determines motion along a line, whereas complex eigenvectors give rise to motion in a plane.

# Exercise

Decomposing $\zeta _ { j } = \xi _ { j } + i \eta _ { j }$ and $\lambda _ { j } = \alpha _ { j } + i \omega _ { j }$ ,show that

$$
\begin{array} { r } { \pmb { \xi } _ { j } ( t ) = e ^ { \alpha _ { j } t } \big [ \cos ( \omega _ { j } t ) \pmb { \xi } _ { j } - \sin ( \omega _ { j } t ) \pmb { \eta } _ { j } \big ] , } \\ { \pmb { \eta } _ { j } ( t ) = e ^ { \alpha _ { j } t } \big [ \sin ( \omega _ { j } t ) \pmb { \xi } _ { j } + \cos ( \omega _ { j } t ) \pmb { \eta } _ { j } \big ] , } \end{array}
$$

so that, using $\xi _ { j }$ and $\eta _ { j }$ as basis vectors, the projection of the initial condition onto the $( \xi _ { j } , \eta _ { j } )$ plane $x _ { j } \xi _ { j } + y _ { j } \eta _ { j }$ is given by

$$
\begin{array} { r l } & { x _ { j } ( t ) = e ^ { \alpha _ { j } t } [ \cos ( \omega _ { j } t ) x _ { j } ( 0 ) + \sin ( \omega _ { j } t ) y _ { j } ( 0 ) ] , } \\ & { y _ { j } ( t ) = e ^ { \alpha _ { j } t } [ - \sin ( \omega _ { j } t ) x _ { j } ( 0 ) + \cos ( \omega _ { j } t ) y _ { j } ( 0 ) ] . } \end{array}
$$

This is the product of a contraction $e ^ { \alpha _ { j } \tau }$ (or expansion if $\alpha _ { j } > 0$ ) composed with a rotation by the angle $\omega _ { j } t$ (fig.(1.2).)

The origin is a stable or-unstable focus in the plane of motion determined by a general complex eigenvalue. If the eigenvalue is purely imaginary, the origin will be a centre surrounded by circles in the eigencoordinates,or ellipses in general coordinates.In the case of real eigenvalues the orbits are

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/c24a91fa3ccfb821493d2df85275462fcc243a74dc6488a660e9c9c29adee879.jpg)  
Fig1.2.)Linear motion in the plane with a general complex eigenvalue is the product of an exponential contraction or expansion composed with a rotation. (a) $\alpha < 0 ;$ $\omega < 0 ,$ (b) $\alpha > 0 ;$ $\omega < 0$

given by

$$
x _ { 2 } = c x _ { 1 } ^ { \lambda _ { 2 } / \lambda _ { 1 } } .
$$

If $\lambda _ { 2 } / \lambda _ { 1 } < 0$ ,the origin will be a saddle point,whereas $\lambda _ { 1 } < \lambda _ { 2 } < 0$ determines a stable node and $0 < \lambda _ { 1 } < \lambda _ { 2 }$ an unstable node. All these possibilities appear in $\textcircled{1}$

Eigenvalue degeneracies may be an obstacle to the diagonalization of the dynamical matrix.This is not a problem for the hermitian or unitary matrices that commonly turn up in physics, but the matrices arising in dynamical systems can be quite general. The crucial factor is the rank of the matrix $\{ \mathcal { A } - \lambda \mathbf { 1 } \}$ ,where $\lambda$ is one of the eigenvalues. If $\lambda$ is nondegenerate, rank $\left\{ \mathcal A - \lambda \mathbf l \right\} = N - 1$ ,and there exists an eigenvector corresponding to $\lambda$ If $\lambda$ is $\mu$ -fold degenerate and rank $\left\{ { \mathcal { A } } - \lambda \mathbf { 1 } \right\} = N - \mu , \lambda$ will be the eigenvalue of $\mu$ linearly independent eigenvectors.However, if rank $\left\{ \mathcal A - \lambda \mathbf I \right\} = N - \nu$ where $\nu < \mu$ ,there will be only $\nu$ eigenvectors corresponding to $\lambda$ . In this case the matrix cannot be diagonalized.

Example. The matrix

$$
\mathcal { A } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } ,
$$

fora horizontal shear in the plane, has the doubly degenerate eigenvalue 1. Rank $\left\{ \mathcal { A } - 1 \right\} = 1$ $\mathcal { A }$ cannot be diagonalized. Its unique eigenvector is $( 1 , 0 )$

In general the best that we can do is to reduce the dynamical matrix to its normal form, where each eigenvector corresponds to a Jordan block:

$$
\pmb { \mathscr { B } } = \left[ \begin{array} { l l l l l } { \lambda } & { 1 } & { } & { } & { 0 } \\ { . } & { \lambda } & { 1 } & { } & { } \\ { } & { } & { . } & { . } & { } \\ { 0 } & { } & { } & { \lambda } & { 1 } \end{array} \right] .
$$

Thesum ofthedimensions ofallthe Jordan blockscorresponding toa given eigenvalue will be $\mu$ ,theorderof itsdegeneracy.

The dynamics of a system with degenerate eigenvalues can be reduced by a linear transformation to the dynamics of individual blocks. To calculate $\exp ( \mathcal { B } t )$ we follow Arnold (1973)in writing $\mathcal { B } = \lambda \mathbf { 1 } + \mathcal { F }$ with

$$
\mathcal { I } = \left[ \begin{array} { c c c c } { 0 } & { 1 } & & & { 0 } \\ & { 0 } & { 1 } & \\ & & { \ddots } & { \ddots } \\ & & & { 1 } \\ { 0 } & & & & { 0 } \end{array} \right] .
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/7965a852ff07bfebb1e9b4e327e0bee5d856ec7678ae803838aca5f32bccd6d2.jpg)  
Fig1.3.Typical linear motions in aplane. (a) Stable focus; (b) unstable focus; (c) centre; (d) stable node; (e) unstable node; (f) saddle.

The matrix exp(Jt) is easily calculated by observing that S operates on the basis vectors $\{ \mathbf { e } _ { 1 } , \ldots , \mathbf { e } _ { N } \}$ through the simple shift $0  \mathbf { e } _ { 1 }  \mathbf { e } _ { 2 } \cdots  \mathbf { e } _ { n }$ · Therefore, ${ \mathcal { F } } ^ { k }$ operates the shift $\mathbf { e } _ { m - k }  \mathbf { e } _ { m }  \mathbf { e } _ { m + k }$ that is,

$$
\mathcal { S } ^ { k } = \left[ \begin{array} { l l l l } { 0 } & { \cdots } & { 1 } & { 0 } \\ & & & { \ddots } & \\ & & { \ddots } & & { 1 } \\ & & & & { \vdots } \\ { 0 } & & & & { \partial } \end{array} \right]
$$

and $\mathcal { I } ^ { N } = 0 .$ The series representation of exp $( \mathcal { F } t )$ thus leads immediately to

$$
e ^ { \boldsymbol { \mathscr { S } } t } = \left[ \begin{array} { c c c c c c } { 1 } & { t } & { t ^ { 2 } / 2 } & { \cdots } & { t ^ { n - 1 } / ( n - 1 ) ! } \\ & { \ddots } & { \ddots } & { \ddots } & & { \vdots } \\ & & & & { t ^ { 2 } / 2 } \\ & & & & { t } \\ { 0 } & & { \cdot } & & { 1 } & { } \end{array} \right] .
$$

# Exercise

Show that if two matrices $\mathcal { A }$ and $\mathcal { B }$ commute, then

$$
e ^ { \mathcal { A } + \mathcal { P } } = e ^ { \mathcal { A } } e ^ { \mathcal { P } } .
$$

Combining (1.25) and (1.26), we conclude that the evolution of a Jordan block is given by

$$
e ^ { \mathcal { R } } = \left[ \begin{array} { c c c c } { e ^ { \lambda t } } & { t e ^ { \lambda t } } & { \dots } & { t ^ { n - 1 } e ^ { \lambda t } / ( n - 1 ) ! } \\ & { e ^ { \lambda t } } & { \ddots } & { \vdots } \\ & & { \ddots } & { t e ^ { \lambda t } } \\ { 0 } & & & { e ^ { \lambda t } } \end{array} \right] .
$$

Example(Arold,1973).Considerthedamicalsemotaineothe Nth-order differential equation

$$
x ^ { ( N ) } = a _ { 1 } x ^ { ( N - 1 ) } + \cdots + a _ { N - 1 } \dot { x } + a _ { N } x ,
$$

through the identification of each derivative with a coordinate: $x ^ { ( n ) } =$ $d ^ { n } x / d t ^ { n } = x _ { n }$ This linear system has the dynamical matrix

$$
\mathcal { A } = \left[ \begin{array} { c c c c } { 0 } & { 1 } & & & { 0 } \\ & & & & \\ & { \ddots } & { \ddots } & & \\ & & & { 0 } & { 1 } \\ { a _ { n } } & { \cdots } & { a _ { 2 } } & { a _ { 1 } } \end{array} \right] .
$$

The trial solution $\exp ( \lambda t ) x _ { 0 }$ for equation (1.29) leads to the algebraic equation

$$
\lambda ^ { N } = a _ { 1 } \lambda ^ { N - 1 } + \cdots + a _ { N } ,
$$

with solutions 𝜆1,..,k， with k ≤N. No matter how degenerate the eigenvalue $\lambda$ maybe,it illesodtegectorof(29)：

$$
\left( e ^ { \lambda t } x _ { 0 } , \ldots , { \frac { d ^ { N - 1 } } { d t ^ { N - 1 } } } e ^ { \lambda t } x _ { 0 } \right) _ { t = 0 } = ( x _ { 0 } , \ldots , \lambda ^ { N - 1 } x _ { 0 } ) ,
$$

Thus,inthisteachegeeateigelueillespodtingle Jordan block.

In this section we have gone through all the ways in which a linear system can be reduced to a set of simpler linear systems.To conclude, we note that the flow of a linear system ${ \bf X } ( { \bf x } _ { 0 } , t )$ defines a linear map $\mathbf { x } _ { 0 } \to \mathbf { x }$ for all $t$ according to (1.5).overselyny l

$$
\mathbf { x } ^ { \prime } = \mathcal { F } \mathbf { x }
$$

with positive eigenvalues can be interpreted as the flow after a unit of time of an autonomous dynamical system defined by the dynamical matrix ${ \mathcal { A } } = \ln { \mathcal { F } }$ . The result of following the flow for $k$ units of time is the same as that of $k$ iterations of the map. General flows always define maps, but the reciprocal equivalence rarely holds. It does not apply to many nonlinear maps obtained as ‘Poincare sections’ in chapter 2. In particular these may have negative eigenvalues, denoting reflection of the motion across the origin in the direction of the eigenvector. In this case it is only the square of the linearized map that can be fitted by a real flow.

# 1.2 Linear Hamiltonian systems

Hamiltonian systems are characterized by a Hamiltonian function $H ( \mathbf { x } , t ) =$ $H ( \mathbf { p } , \mathbf { q } , t )$ of an even number of variables $\mathbf { p } = ( p _ { 1 } , \ldots , p _ { L } )$ and $\mathbf { q } = ( q _ { 1 } , \dots , q _ { L } )$ where $L$ is known as the number of freedoms. The dynamical system is defined by Hamilton's equations:

$$
{ \dot { \bf p } } = - \frac { \partial H } { \partial { \bf q } } , \qquad { \dot { \bf q } } = \frac { \partial H } { \partial { \bf p } } .
$$

If the Hamiltonian is independent of time, the system is autonomous and $H ( \pmb { \mathsf { p } } , \pmb { \mathsf { q } } )$ is a constant or integral of the motion:

$$
\frac { d H } { d t } { = } \frac { \partial H } { \partial \mathbf { p } } \dot { \mathbf { p } } + \frac { \partial H } { \partial \mathbf { q } } \dot { \mathbf { q } } = 0 .
$$

The system (1.33)can be linearized, which is tantamount toapproimt ing the Hamiltonian by the quadratic form (x.xx)/2, where x is the Hessian matrix

$$
\mathcal H = \frac { \partial ^ { 2 } H } { \partial { \bf x } \partial { \bf x } } .
$$

A linear Hamiltonian system thus has the form

$$
\dot { \mathbf { x } } = \mathcal { F } \mathcal { H } \mathbf { x } ,
$$

where $\mathcal { J }$ is the $( 2 L \times 2 L )$ -dimensional matrix

$$
\mathscr { J } = \left[ \frac { 0 } { 1 } \vdots - \frac { 1 } { 0 } \right] .
$$

Defining ${ \mathcal { J } } ^ { \prime }$ as the transposed matrix, we verify immediately that $\mathcal { J } ^ { \prime } = \mathcal { J } ^ { - 1 } = - \mathcal { J } .$ The product $\mathcal { J } \mathcal { H }$ will be referred to as the Hamiltonian matrix.

The symplectic area of the parallelogram defined by two vectors $\pmb { \xi } = ( \xi _ { \mathfrak { p } } , \xi _ { \mathfrak { q } } )$ and $\pmb { \eta } = ( \pmb { \eta } _ { \mathrm { p } } , \pmb { \eta } _ { \mathrm { q } } )$ is given by the skew product

$$
\xi \wedge \eta = ( { \mathcal { J } } \xi ) \cdot \eta = \sum _ { k = 1 } ^ { L } ( \xi _ { p k } \eta _ { q k } - \xi _ { q k } \eta _ { p k } ) ,
$$

where the dot indicates the ordinary scalar product.(See Arnold,978,ora complete discussion of skew products and exterior algebra.) Geometrically this measures the algebraic sum of the areas of the parallelograms formed by the projections of $\xi$ and $\pmb { \eta }$ onto the $L$ conjugate planes with coordinates $p _ { k }$ and $q _ { k } ( \mathrm { f i g } { \left( 1 . 4 \right) }$ The symplectic areais conserved byalinear Hamiltonian

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/b0475fc6d128dbe1812bbd8c1aa9e964abd7be660f6e18b94d44a2f9e3c7b3dc.jpg)  
Fig(1.4.) The symplectic area of a closed curve in phase space is the algebraic sum of the areas of its projections onto all the canonical conjugate planes. In the case of the parallelogram formed by two vectors 5and n,this is the skew product 5^ n.

flow, since

$$
\begin{array} { r l } & { \cfrac { d } { d t } ( \xi \wedge \eta ) = ( { \mathcal { J } } { \dot { \xi } } ) \cdot \eta + ( { \mathcal { J } } \xi ) \cdot { \dot { \eta } } } \\ & { \qquad = ( { \mathcal { J } } { \mathcal { J } } { \mathcal { H } } \xi ) \cdot \eta + ( { \mathcal { J } } \xi ) \cdot ( { \mathcal { J } } { \mathcal { H } } \eta ) = 0 . } \end{array}
$$

# Exercises

1. Prove that $\xi \wedge \eta = - \eta \wedge \xi$ and hence $\xi \wedge \xi = 0$   
2. Show that any vector $\xi$ defines a unique $( 2 L - 1 )$ -dimensional plane, which is skew-orthogonal to $\xi$ ,that is, $\xi \wedge \pmb { \eta } = 0$ for all vectors $\pmb { \eta }$ in the plane. Use the similar results for the scalar product, but note that the plane includes $\xi$ because of exercise 1.

Area invariance is a fundamental result for Hamiltonian systems.For a start it providesapurely algebraicconditionfor the matrix $\mathcal { M } = \exp ( \mathcal { A } t )$ to describe a Hamiltonian flow: We must have

$$
( \mathcal { J } \mathcal { M } \xi ) ^ { * } ( \mathcal { M } \eta ) = ( \mathcal { J } \xi ) ^ { * } \eta ,
$$

which reduces to

$$
{ \mathcal { M } } ^ { \prime } { \mathcal { J } } { \mathcal { M } } = { \mathcal { J } } ,
$$

the definition of a symplectic matrix.

For a nonlinear system, $\mathcal { M }$ is the Jacobian matrix of the full canonical transformation generated by the Hamiltonian flow, so that (1.41) must hold for all points in the phase space. Taking the determinant of both sides of (1.41) yields

$$
\operatorname* { d e t } ( \mathcal { M } ) = \pm 1 .
$$

If $\mathcal { M } = \exp \left( \mathcal { J } \mathcal { H } \mathcal { \ell } \right)$ $\operatorname* { d e t } ( \mathcal { M } )$ will be continuous in t, so from the initial condition at $t = 0$ ,we have

$$
\operatorname* { d e t } ( \mathcal { M } ) = 1
$$

for a Hamiltonian flow. This is the diferential form of Liouville's theorem.

# Exercise

A point transformation does not mix the pand theqcoordinates.Its matrix therefore has the form

$$
{ \begin{array} { r } { { \left[ \frac { { \mathcal { A } } } { { \mathbf { \overline { { \mathbf { 0 } } } } } } ; \frac { { \mathbf { 0 } } } { { \mathcal { B } } } \right] } . } \end{array} }
$$

Show that the condition for this to be symplectic is that sB' =.'B=1.   
Thus, $\mathcal { B } = \mathcal { A }$ if $\mathcal { A }$ is unitary.

Next we deduce that, if y ≠ O is an eigenvalue of a symplectic matrix M, then y-1 is also an eigenvalue. The characteristic polynomial P(y) can be written in the forms

$$
\begin{array} { l } { { \displaystyle { \bf P } ( \gamma ) = \operatorname* { d e t } [ \mathcal { M } - \gamma { \bf 1 } ] = \operatorname* { d e t } [ \mathcal { J } ^ { - 1 } \mathcal { M } ^ { \prime - 1 } \mathcal { J } - \gamma { \bf 1 } ] = \operatorname* { d e t } [ \mathcal { M } ^ { \prime - 1 } - \gamma { \bf 1 } ] } } \\ { { \displaystyle ~ = \frac { ( - \gamma ) ^ { 2 L } } { \operatorname* { d e t } ( \mathcal { M } ^ { \prime } ) } \operatorname* { d e t } [ \mathcal { M } ^ { \prime } - \gamma ^ { - 1 } { \bf 1 } ] = \frac { \gamma ^ { 2 L } } { \operatorname* { d e t } ( \mathcal { M } ) } \operatorname* { d e t } [ \mathcal { M } - \gamma ^ { - 1 } { \bf 1 } ] . \qquad \quad \mathrm { ( \gamma  \gamma \mathrm { ~ \gamma ^ \mathrm { - ~ 1 ~ 2 ~ } ~ ) } } } } \end{array}
$$

Thus,

$$
P ( \gamma ) = \pm \gamma ^ { 2 L } P ( \dot { \gamma } ^ { - 1 } ) ,
$$

and if $\gamma _ { 0 }$ is a root of $P ( \gamma )$ ,so is $\gamma _ { 0 } ^ { - 1 }$ .Incidentally this shows that the sign is never negative in (1.42), even if $\mathcal { M }$ has negative eigenvalues.

The implication is that the nonzero eigenvalues of the Hamiltonian matrix $\mathcal { J } \mathcal { H }$ always come in pairs $( \lambda , - \lambda )$ Combining the condition that $\mathcal { H }$ is real,ch $( \lambda , \lambda ^ { * } )$ as simultaneous pairs, we elicit the four types of eigenvalue for the Hamiltonian matrix:)

1. Zero eigenvalues   
2. Pairs of real eigenvalues $\pm \lambda$   
3. Pairs of purely imaginary eigenvalues $\pm i \omega$   
4. Quartets of complex eigenvalues ±α±iω

A linear Hamiltonian system with only one freedom must fallinto one of the first three categories (though category 1 is the trivial system in this case). Their presence is also inevitable if the number of freedoms is odd.

It may seem that any excess of real or jimaginary eigenvalues will move into the complex plane after a smal general quadratic perturbation of the Hamiltonian. However,this requires the simultaneous exit offour eigenvalues from the real or the imaginary axis,so it is only when two pairs of eigenvalues inclass(ii)or (ii)degenerate that they canformacomplex quartet. In a one-parameter family of systems this event, illustrated in fig.1.5Swil occur at isolated values of the parameter. The necessary and sufficient conditions are provided in Arnold (1978,sec.4.2). Thus,eal and imaginary eigenvalues are stable in the family of Hamiltonian systems. Another waytoseethisis that twopairs ofeigenvalues on anaxis havetwo freedoms' in which to move,just as a single quartet in the plane. Only the zero eigenvalue has zero probability of showing up in a randomly picked quadratic Hamiltonian.A property that is usually resistant toa given class of perturbations of the system is described as generic. The system with generic properties is itself called generic or ‘structurally stable.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/056d26027c35a82633925dd9354c305ec9ab8b6ac54b81e42aade42b0adec91c.jpg)  
Fig.1.5JReal eigenvaluesandimaginary eigenvaluesarestructurally stable because it is required that two pairs of eigenvalues leave the axis simultaneously.

Generic Hamiltonian matrices do not have eigenvalue degeneracies and can therefore be diagonalized by a linear transformation.The condition for the transformed system to stillbe Hamiltonian is that the transformation be symplectic.Thus,in the new system we must have the skew products among the basis vectors

$$
{ \hat { \bf p } } _ { i } \wedge { \hat { \bf q } } _ { j } = \delta _ { i j } ; \qquad { \hat { \bf p } } _ { i } \wedge { \hat { \bf p } } _ { j } = { \hat { \bf q } } _ { i } \wedge { \hat { \bf q } } _ { j } = 0 ,
$$

just as in the old system. This condition holds for the eigenvectors of the Hamiltonian matrix. In the case of a pair of real eigenvalues $\lambda _ { 1 }$ and $\lambda _ { 2 }$ ,the symplectic area of the parallelogram defined by the corresponding eigenvectors $\xi _ { 1 } , \xi _ { 2 }$ would be multiplied by expl $[ \lambda _ { 1 } + \lambda _ { 2 } ) t ]$ after a time $t$ if it were not zero.So we can take these eigenvectors as the new axes $\hat { { \bf p } } _ { 1 }$ and $\hat { { \bf p } } _ { 2 }$ On the other hand, symplectic areas in the plane of $\xi _ { 1 }$ and $\xi _ { - 1 }$ corresponding to the eigenvalues $\pm \lambda _ { 1 }$ are conserved,enabling us to choose $\xi _ { - 1 }$ as the new $\hat { \bf q } _ { 1 }$ axis,apart from normalization.In the case of imaginary eigenvalues $\omega _ { j }$ ,thenew $( \hat { \pmb { \mathsf { p } } } _ { j } , \hat { \pmb { \mathsf { q } } } _ { j } )$ plane is just the $( \xi _ { j } , \eta _ { j } )$ ,corresponding to the real and imaginary part of the eigenvector $\zeta _ { j }$ ,as in (1.19).

# Exercise

Show that the choice of basis vectors $\left( \hat { p } _ { 1 } , \hat { p } _ { 2 } \right) = \left( \xi , \eta \right)$ in (1.19) for the eigenvalue $\alpha + i \omega$ and $( \hat { q } _ { 1 } , \hat { q } _ { 2 } ) = ( \xi ^ { \prime } , \pmb { \eta } ^ { \prime } )$ for the eigenvalue $- \alpha + i \omega$ implies the invariance of the symplectic area of any parallelogram in the $\left( \hat { p } _ { 1 } , \hat { p } _ { 2 } , \hat { q } _ { 1 } , \hat { q } _ { 2 } \right)$ subspace.

The normal forms for the quadratic Hamiltonians that generate these independent submatrices are of three types:

1. Real eigenvalues $\begin{array} { r l } & { H = - \lambda p _ { 1 } q _ { 1 } } \\ & { ( \pm i \omega ) ; H = \pm ( \omega / 2 ) ( p _ { 1 } ^ { 2 } + q _ { 1 } ^ { 2 } ) } \\ & { ( \pm \alpha \pm i \omega ) ; H = - \alpha ( p _ { 1 } q _ { 1 } + p _ { 2 } q _ { 2 } ) + \omega ( p _ { 1 } q _ { 2 } - } \end{array}$   
2. Imaginary eigenvalues (±iω): H= ±(ω/2)(p² +q²)   
3. Complex eigenvalues   
$p _ { 2 } q _ { 1 } )$

Generic quadratic Hamiltonians can be reduced to a linear superposition of these simple forms.

# Exercises

1. Show that the symplectic transformation, which rotates each pair of conjugate axes by $\pi / 4$ ,takes the Hamiltonian of type 3 into the form

$$
H = - \frac { \alpha } { 2 } ( p _ { 1 } ^ { 2 } - q _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } - q _ { 2 } ^ { 2 } ) + \omega ( p _ { 1 } q _ { 2 } - p _ { 2 } \dot { q } _ { 1 } ) .
$$

2. Show that (1.47) describes the quadratic approximation for the Hamiltonian of a spherical pendulum near the unstable equilibrium, in coordinates that rotate around the vertical axis. (This interpretation was communicated to me by J. Koiller.)

Isolated degeneracies may occur in a typical one-parameter family of Hamiltonians. Some of the Jordan blocks that result are generic, that is, structurally stable with respect to small variations of the family.The normal form of the Hamiltonian for each of these blocks is given in Arnold (1978, app. 6) as

4. Zero eigenvalues (0): $\begin{array} { r } { H = \pm \frac { 1 } { 2 } q _ { 1 } ^ { 2 } } \end{array}$   
5. Real eigenvalues $( \pm \lambda )$ $H = - \lambda ( p _ { 1 } q _ { 1 } + p _ { 2 } q _ { 2 } ) + p _ { 1 } q _ { 2 }$   
6. Imaginary eigenvalues $( \pm i \omega )$ $H = \pm \frac { 1 } { 2 } ( q _ { 1 } ^ { 2 } / \omega ^ { 2 } + q _ { 2 } ^ { 2 } ) - \omega ^ { 2 } p _ { 1 } q _ { 2 } + p _ { 2 } q _ { 1 }$

The same reference also provides the generic Jordan blocks in two parameter families.

# 1.3 Linear flow on a torus

All of the eigenvalues of a linear Hamiltonian system may well be imaginary.This is the only possbility that leads to stable motion near the origin,since the other alternatives imply the existence of a positive real part of at least one of the eigenvalues. Choosing the (pj,qj) coordinate axes along the real and imaginary parts of the Leigenvectors \$j,the equations of

motion take the form

$$
\dot { p } _ { j } = - \omega _ { j } q _ { j } , \qquad \dot { q } _ { j } = \omega _ { j } p _ { j } .
$$

Transforming to canonical polar coordinates [action-angle variables $( \mathbf { I } , \pmb { \theta } )$

$$
p _ { j } = ( 2 I _ { j } ) ^ { 1 / 2 } \sin \theta _ { j } , \qquad q _ { j } = ( 2 I _ { j } ) ^ { 1 / 2 } \cos \theta _ { j } ,
$$

the system reduces to

$$
\begin{array} { r } { \dot { I } _ { j } = 0 , \qquad \dot { \theta } _ { j } = \omega _ { j } . } \end{array}
$$

For a system with a single freedom, $t =$ const defines a circle. In a twofreedom system ${ \bf l } =$ const is the direct product of two circles,that is,a twodimensional torus in the four-dimensional phase space. The two angular coordinates $\theta _ { j } \pm 2 \pi = \theta _ { j }$ specify the ‘latitude and longitude' on the torus,as shown in fig.1.6a.In the $( \theta _ { 1 } , \theta _ { 2 } )$ coordinate plane, each of the $2 \pi$ -sided squares shown in fig..6b js an image of the torus. The solution of the system is an orbit that winds itself around the torus, while in the $( \theta _ { 1 } , \theta _ { 2 } )$ coordinates it is|a straight line.

In the general case the $L$ -dimensional surface,defined by ${ \bf I } =$ const, has $L$ independent irreducible circuits orresponding to the displacement of $2 \pi$ for each of the angles $\theta _ { j }$ This surfaoe is an L torus.The orbits wind around the $L$ torus, though they are parallel straight lines in the space of the $\pmb \theta$ coordinates.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/665236c3046d4653e9b4b73bab9f6505afa4942892d64bc6ffc9a16686dfa8dd.jpg)  
Fig1.6.)Theorbitsof (1.5o),which wind around the torus (a),are straight lines in the angular coordinates (b).

A notable way to study motion on the torus is to consider the repeated traversals of an orbit through the ‘meridian' $\theta _ { 1 } = 0 { \mathrm { ~ } } ( { \mathrm { m o d } } 2 \pi ) .$ ，that is,the Poincare section of the torus. The latitudes of the intersections for the solutions of (1.50) will be

$$
{ \theta } _ { 2 k } = { \theta } _ { 2 0 } + k { \alpha } ,
$$

where $\alpha = 2 \pi \omega _ { 2 } / \omega _ { 1 }$ (fig[1.7).)The mapping $\theta _ { 2 }  \theta _ { 2 } ^ { \prime } = \theta _ { 2 } + \alpha$ for all the points of the circle is known as the Poincareé map,a uniform translation in this instance.

There will be two distinct cases. If $\omega _ { 2 } / \omega _ { 1 } = r / s$ with $r$ and s mutually prime integers, then $\theta _ { 2 } s = \theta _ { 2 0 }$ .The orbits of successive iterations of the Poincare map will be a set of $s$ equally spaced points. An orbit of (1.50) draws out a finite set of parallel segments in a $2 \pi$ -sided square. The alternative is that $\omega _ { 2 } / \omega _ { 1 }$ is irrational,in che $\theta _ { 2 k } \neq \theta _ { 2 0 }$ for all $k ;$ that is, the orbit on the torus never closes.

It is easy to show that such an orbit is dense on the circle: Following Arnold (1973)we divide the circle into $k$ equal semiopen intervals. Among the first $k + 1$ images of $\theta _ { 2 0 }$ ,at least two will share the same interval. Let these two points be $\theta _ { 2 0 } + p \alpha$ and $\theta _ { 2 0 } + q \alpha$ with $s = p - q > 0$ Thus,

$$
| s \alpha | ( \mathrm { m o d } 2 \pi ) < 2 \pi / k ,
$$

implying that some point in the sequence $\theta _ { 2 0 } + j s \alpha$ comes within the

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/67bb0d12a35e412ce99165ec370d931c336e6239cafdcb79159c9403e8e0663d.jpg)  
Fig.1.7.SSuccessive intersections of an orbit with the line 02 =2πk define its orbit under the Poincare map.

distance $\varepsilon = 2 \pi / k$ ofany point inthecircle.Sinceεmaybechosenarbitrarily small, the obit ise

Itfollows that theorbits for the linearmotionon the torusarealsodense. In the case of an $L$ torus,this willbe the caseif te $L$ frequencies are rationally inependenttat isoncoditiott

$$
k _ { 1 } \omega _ { 1 } + \cdots + k _ { L } \omega _ { L } = 0 ,
$$

if and only if $k _ { 1 } = \dots = k _ { L } = 0$

Let us now consider anarbitrary finite function $f ( \theta )$ defined on the torus. Adenseorbit willsamplepointsdemocraticallinitsayalongthetorus so it is plausible that the time average

$$
\overline { { f } } ( \pmb { \theta } _ { 0 } ) = \operatorname* { l i m } _ { T  \infty } \frac { 1 } { T } \int _ { 0 } ^ { T } f ( \pmb { \theta } ( \pmb { \theta } _ { 0 } , t ) ) d t
$$

exists and that it equals the spatial average:

$$
\overline { { f } } ( \pmb \theta _ { 0 } ) = ( 2 \pi ) ^ { - L } \int f ( \pmb \theta ) d \pmb \theta .
$$

This equality is verified for harmonic functions $f ( \pmb \theta ) = \mathrm { e x p } ( i \mathbf k \cdot \pmb \theta )$ where $\mathbf { k }$ is an integer vector,for rationally independent frequencies. We then have

$$
\frac { 1 } { T } \int _ { 0 } ^ { T } d t \exp ( i \mathbf { k } \cdot ( \pmb { \theta } _ { 0 } + \omega t ) ) d t = \frac { \exp ( i \mathbf { k } \cdot \pmb { \theta } _ { 0 } ) } { i ( \mathbf { k } \cdot \pmb { \omega } ) T } [ \exp ( i \mathbf { k } \cdot \pmb { \omega } T ) - 1 ] .
$$

The function in the square brackets is bounded,so the limit of the right side is zero if $\mathbf k \neq 0$ ，whereas (1.55) is trivially verified if $\mathbf k = 0$ .Since both averages are linear,(1.55) is also valid for any trigonometric polynomial and hence for any truncation of the Fourier representation of an arbitrary function $f ( \pmb \theta )$ The extension of the proof of the coincidence of averages to infinite trigonometric series is given by Arnold (1982, sec.11).

The equality of time and spatial averages is a characteristic of ergodic motion.It implies the uniform partition of trajectories, which means that,as well as penetrating any finite region $D$ of the torus (i.e., being dense), the time they spend in such a region is proportional to its area. To prove this property we choose $f ( \pmb \theta )$ to be the characteristic function for the region, equal to one in D and zero outside of D. So if μ(D) is the area of D and $\tau ( D , T , \pmb { \theta } _ { 0 } )$ is the total time that the trajectory stays in $D$ in the interval $( 0 , T )$ ， we obtain from (1.54)

$$
\operatorname* { l i m } _ { T \to \infty } \frac { \tau ( D , T , \theta _ { 0 } ) } { T } { = } \frac { \mu ( D ) } { \mu ( \mathrm { t o r u s } ) } { = } \frac { \mu ( D ) } { 4 \pi ^ { 2 } } .
$$

This result is also true, of course, for an $L$ torus if we define $\mu$ to be the $L$ -dimensional volume.

# 1.4 Linear maps on the torus

Are there linear maps on the torus that are more interesting than mere translations? In particular,can one find motion with an isolated fixed point as in the plane? Let us consider the case of the circle.The periodic condition, that lattice points transform among themselves, cannot be satisfied if the origin is a stable fixed point. So the map would have the form

$$
\theta _ { 2 } ^ { \prime } = n \theta _ { 2 } \qquad ( \mathrm { m o d } 2 \pi ) .
$$

Though it is of some interest, this is not a one-to-one mapping-each $\theta _ { 2 } ^ { \prime }$ is the image of two points $\theta _ { 2 }$ This property disqualifies (1.58) as a model for the Poincare map of a dynamical system. For a two-dimensional torus the situation is more favourable. The map

$$
{ \begin{array} { r l } { { \left[ \theta _ { 1 } ^ { \prime } \right] } = { \left[ \begin{array} { l l } { m _ { 1 1 } } & { m _ { 1 2 } } \\ { m _ { 2 1 } } & { m _ { 2 2 } } \end{array} \right] } { \left[ \begin{array} { l } { \theta _ { 1 } } \\ { \theta _ { 2 } } \end{array} \right] } } & { \quad ( { \mathrm { m o d } } 2 \pi ) } \end{array} }
$$

will be periodic if all the elements $m _ { i j }$ of the matrix $\mathcal { M }$ are integers. The condition that the mapping be one-to-one is just that det $\mathcal { M } = 1$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/013e7dbbed6173de76377652efa8707e4fc8a264005304ebad27cfe8b8f515c4.jpg)  
FigC1.8.JThe invariant curves for the linear map on the torus specified by (1.59) and (1.60)are circles in the $\pmb \theta$ coordinates.

Example

$$
{ \mathcal { M } } = { \left[ \begin{array} { l l } { 0 } & { - 1 } \\ { 1 } & { \ 0 } \end{array} \right] } .
$$

The eigenvalues of $\mathcal { M }$ are $\mathrm { e x p } ( \pm i \pi / 2 )$ The origin is a fixed point about which the plane rotates $9 0 ^ { \circ }$ for each iteration.The invariant curves for this map arecircles (fig.1.8)even when these cross theboundary of theunit cell centred on the origin.

Example. The matrix

$$
\mathcal { M } = \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right]
$$

generates the Anosov automorphism,collquially knownas Arnold'scatmap (fig.1.9).The origin is an unstable fixed point with real eigenvalues $\gamma _ { 1 } > 1$ $> \gamma _ { 2 }$ equal to $( 3 \pm { \sqrt { 5 } } ) / 2 .$ The eigenvectors $\boldsymbol { \xi } _ { 1 }$ and $\boldsymbol { \xi } _ { 2 }$ shown in fig1.10have irrationally related components since $\mathcal { M }$ is an integer matrix.The invariant helicoidal lines $t \xi _ { j }$ are therefore dense on the torus. The points of intersection of these twolines (fig.1.11)hrecalled homoclinic points.Images of intersections are also intersections of the invariant lines, so there are an infinite rumber of homoclinic points.The homoclinic orbits are the only ones with the property that they accumulate on the origin for both forward (positive) and backward (negative) iterations of the map.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/f63f3109748ba82b96db4ad38c3e1233d8a02452e240b65cc0c26db964dc259d.jpg)

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/492cf77657c196ba3573f380063d5bdbe490a60f5ba8d42e5f1e7c2f0a37d12e.jpg)  
Fig1.9.JArnold's catmapstretchestheunit squareand folds it back ontoitself in such a way that points initially close together become separated and vice versa.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/5c4cac28f576c6e6e57ab8ff1f1f3057cc5c6095196e5ef66d4e534b80887fbe.jpg)  
Fig1.1o.,The real eigenvectors have components that are irrationally related, so the respective orbits wind densely around the torus.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/d77ac55d0b664ed148807ee2e76618e963f6d8a0156a58b25d21c03bba819a76.jpg)  
Fig..11) The intersections of the incoming and outgoing separatrices are called homoclinic points. These are dense on the torus.

The map is linear, so any region $F$ of the torus is stretched in the $\xi _ { 1 }$ direction and contracted along $\boldsymbol { \xi } _ { 2 }$ . After a large number n of iterations, $F$ is deformed into a very long and thin helicoidal strip winding around the torus. For n sufficiently large, ${ \mathcal { M } } ^ { n } F$ will intersect many times any other region $G$ of the torus.In fact,we shall show in section 3.4 that the catmap has the property of mixing; that is,the ratio of the area of the intersection $G \cap { \mathcal { M } } ^ { n } F$ to $G$ is the same as the ratio of the area of $F$ to the torus itself.

The existence of isolated homoclinic points and the property of mixing are typical of the dynamics of chaotic systems. Paradoxically perhaps,they are associated with the presence of periodic orbits,the most regular form of motion! In the present example they can be trivially constructed from the observation that any point with coordinates $\pmb { \theta } _ { 0 } = 2 \pi ( r _ { 1 } / s _ { 1 } , r _ { 2 } / s _ { 2 } )$ where $r _ { j }$ and $s _ { j }$ are mutually prime, will return to itself after a number of iterations $n$ equal to the minimum common multiple of $s _ { 1 }$ and $s _ { 2 }$ .Periodic orbits are the fixed points of the mapping with matrix ${ \mathcal { M } } ^ { n }$ for some $n$ ,so each point, specified by coordinates of the above form, will have an unstable periodic orbit with eigenvalues $( \gamma _ { 1 } ^ { n } , \gamma _ { 2 } ^ { n } )$ .The rational numbers are dense among the reals; therefore, these periodic orbits are dense on the torus.

# 2

# Nonlinear systems

Little can be said that applies generally to nonlinear systems. We have access mainly to local results, such as the basic existence and uniqueness theorem, which establishes the possibility of rectifying vector fields. The conditions for the theorem exclude the neighbourhoods of equilibria, exactly the regions approximated by linear fields in chapter 1. This omission is filled in by the Hartman-Grobman theorem, which guarantees the existence of a coordinate transformation that linearizes a neighbourhood of generic points of equilibrium.

There follows a discussion of Poincaré sections. In principle they reduce the study of motion near a periodic orbit to the iterations of a map in the neighbourhood of a fixed point. The linear approximation near a fixed point was shown in chapter 1 to be equivalent to a linear flow. The nontrivial extension of the Hartman-Grobman theorem to maps thus provides information on the motion surrounding an important class of periodic orbits.

Poincare sections reduce Hamiltonian systems to a map in a phase space with two fewer dimensions.That the map preserves symplectic area just the area, in the case of the plane) is a consequence of the Poincare-Cartan theorem, here derived from the variational principle. We willdiscuss the reduction of two dimensions for a Hamiltonian system, by making it periodic in time.In particular we will see how specific choices of coordinates may preserve some of the symmetry properties of the full system.

In conclusion we will discuss two global theorems on the structural stability for motion in two dimensions. Peixoto's theorem classifies all generic dynamical systems inthe plane, whereas Anosov's theorem guarantees the structural stability of the cat map.

# 2.1 Rectification of vector fields

It is useful to refine our mathematical terminology before discussing the general theorems presented in the following sections.We start bydefininga diffeomorphism as a one-to-one map $\mathbf { y } = \mathbf { G } ( \mathbf { x } ) ,$ where both the functions G and $\mathbf { G } ^ { - 1 }$ are differentiable.

A nonlinear change of coordinates can be linearized locally. There results a linear map between the vectors that act at a given point and those that act onits image.Insimplepsical situationsoconfusionarisesifwecosder the points,which suer the nonlinear transformation,and the vectors to inhabit the same Euclidean space. The discussion becomes clearer nonetheless, if we atribute to each point $\mathbf { X }$ a complete $N$ -dimensional vector space,containing all the vectors that may possibly act on $\mathbf { X }$ This is called the tangent space. Thus, a differentiable map G from an $N$ dimensional domain $U$ to an $M$ -dimensional range $V$ generates a linear map from the tangent space at $\mathbf { X }$ to the tangent space at $\mathbf { y } = \mathbf { G } ( \mathbf { x } )$ This tangent map DG is defined by the condition that, given any curve ${ \bf x } ( t )$

$$
D \mathbf { G } \left( \left. \frac { d \mathbf { x } } { d t } \right| _ { t = 0 } \right) = \frac { d } { d t } \bigg | _ { t = 0 } \left( \mathbf { G } ( \mathbf { x } ( t ) ) \right) ,
$$

where $( d \mathbf { x } / d t ) _ { t = 0 }$ is a vector acting on the point $\mathbf { x } ( 0 ) ,$ while the vector on the right side acts on y(O).This definition makes no use ofany particular choice of coordinates for $\mathbf { x }$ .However,givena set of basis vectors $\displaystyle \{ \mathbf { e } _ { 1 } , \ldots , \mathbf { e } _ { N } \}$ such that $\mathbf { x }$ has coordinates $\{ \mathbf { x } _ { 1 } , . . . , \mathbf { x } _ { N } \} ,$ the chain rule

$$
{ \dot { y } } _ { j } = \sum _ { i = 1 } ^ { N } { \frac { \partial y _ { j } } { \partial x _ { i } } } { \dot { x } } _ { i }
$$

identifies the matrix representation of $D \mathbf G$ with the Jacobian matrix of the nonlinear map G.

We can now state the basic theorems, discussed and proved in Arnold (1973). There exists a diffeomorphism $\mathbf { G } \colon ( \mathbf { x } , t ) \to ( \mathbf { y } , t ) .$ ，defined in some neighbourhood $V$ of a point $( \mathbf { x } _ { 0 } , t )$ of the Euclidean $( N + 1 )$ -dimensional space, that takes the sytem

$$
\dot { { \mathbf x } } = { \mathbf f } ( { \mathbf x } , t )
$$

into the system

$$
\dot { \mathbf { y } } = 0
$$

in the image $W = \mathbf { G } ( V )$ The theorem is represented figuratively in fig.2.1. Note that the diffeomorphism is defined in a space that includes $t$ ,butit does not alter the time. Thus, if ${ \bf x } ( t )$ is a solution of (2.3), $\mathbf { G } ( \mathbf { x } ( t ) )$ will be a solution of (2.4).

This rectification theorem implies the existence and uniqueness theorem, since the diffeomorphism G has a unique inverse. The advantage here is that we also obtain qualitatively the local structure of the orbits in the neighbourhood V. To derive the corollary of the rectification theorem, which applies directly to autonomous systems, we label the phase space coordinates $\mathbf { x } = ( x _ { 1 } , \mathbf { X } )$ and the vector field ${ \bf f } = ( f _ { 1 } , { \bf F } )$ .Dividing the $N - 1$ remaining equations of the system by the first equation, we obtain the (reduced, nonautonomous) sem

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/1c1d05d75efe293300f73fa47e8fd7ef0a7fd9eb33fe60b422fd5db101b379c5.jpg)  
$\widetilde { \mathrm { F i g . } } \widetilde { \mathcal { Q } } . \widetilde { 1 . } \widetilde { \Big . }$ There exists an invertible differentiable map (diffeomorphism) that transforms the trajectories in a neighbourhood $V$ into straight lines.

$$
\frac { d \mathbf { X } } { d x _ { 1 } } { = } \frac { \mathbf { F } ( \mathbf { X } ; x _ { 1 } ) } { f _ { 1 } ( \mathbf { X } ; x _ { 1 } ) }
$$

in the‘time' $x _ { 1 }$ ,if $f _ { 1 } \neq 0$ . This system can be rectified into

$$
d { \bf Y } / d y _ { 1 } = 0 ,
$$

where $y _ { 1 } = x _ { 1 }$ .A change of scale will bring $f _ { 1 } = 1$ , so we obtain the full vector

$$
{ \dot { \mathbf { y } } } = { \mathbf { e } } _ { 1 } = ( 1 , 0 , \ldots , 0 ) . \ .
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/90d6465b33f767302bf5fdc358e184268c04546275147e6d424b2ccf81726fbd.jpg)  
Fig(2.2.jThe orbits of both the harmonic oscillator and the inverted pendulum can bk rectified in a neighbourhood that excludes the origin.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/f75baa26608941f63cff9ace681a90e3026bffe13650d4cb0c5927457daa05c8.jpg)

If $f _ { 1 } = 0$ we can use another ‘time variable' $x _ { j } ,$ unless all the field compoe as $\mathbf f \neq 0$ Figure2.2displaystheeciicatiooftehmoicosand the inverted dulum(terod).

# Exercise

Sketch the level curves of the coordinates that rectify the following vector fields:

$$
\begin{array} { l } { { ( \mathrm { a } ) ~ \mathbf { f } = x _ { 1 } \mathbf { e } _ { 1 } + 2 x _ { 2 } \mathbf { e } _ { 2 } , } } \\ { { ( \mathrm { b } ) ~ \mathbf { f } = \mathbf { e } _ { 1 } + \sin x _ { 1 } \mathbf { e } _ { 2 } , } } \\ { { ( \mathrm { c } ) ~ \mathbf { f } = x _ { 1 } \mathbf { e } _ { 1 } + ( 1 - x _ { 1 } ^ { 2 } ) \mathbf { e } _ { 2 } . } } \end{array}
$$

We have noted that the point where $\mathbf { f } = 0$ defines an equilibrium of the system; it is also known as a singularity of the vector field.

# Exercises

1. Prove that vector field singularities are invariant under diffeomorphisms; that is, if $\mathbf { x } _ { e }$ is a singular point of $\mathbf { f } ( \mathbf { x } )$ ,then ${ \bf G } ( { \bf x } _ { e } )$ is a singular point of DG(f).   
2. The dynamical matrix near an equilibrium is $d \mathbf { f } / d \mathbf { x }$ .Show that its eigenvalues are invariant under diffeomorphisms.

# 2.2 The Hartman-Grobman theorem

The local structure of the orbits near singularities of the vector field is not elucidated by the rectification theorem. It is natural therefore to try to classify the types of motion around equilibria, according to the different kinds of linearized motion studied in the first chapter. The dificulty is that these depend only on whether the eigenvalue is real or complex or degenerate. On the other hand, diffeomorphisms cannot reduce related linearized motions to a standard formas a consequence of the last exrcise in section 2.1. For example, no diffeomorphism can transform the system $\dot { x } = 2 x$ into ${ \dot { x } } = x$ 、Thus, the partition of diffeomorphic vector fields is continuous rather than discrete.

So as not to distinguish between fields such as $x$ and $2 x$ ,we need a cruder notion of equivalence between vector fields. This is based on homeomorphisms, that is,continuous one-toone maps with a continuous inverse,but not necessarily differentiable.

# Exercise

Showthatthe homeomorphism y = x|x| takes the system y =2yintox=x, for $x \neq 0$ ·

Where the homeomorphism is not differentiable,no new vector field is implicitlydefined.We thusdenote twosystemsas topologicallyequivalentif there exists a homeomorphism $\mathbf { y } = \mathbf { G } ( \mathbf { x } )$ that identifies the respective flows

$$
{ \bf G } ( { \bf x } ( { \bf x } _ { 0 } , t ) ) = { \bf y } ( { \bf G } ( { \bf x } _ { 0 } ) , t )
$$

for all $\mathbf { x } _ { 0 }$

We can now enunciate the basic theorem of Hartman and Grobman: If the linear part of the field near a point of equilibrium has no zero or purely imaginary eigenvalues, then the system and its linear part are topologically equivalent within some neighbourhood of the equilibrium.

This is just as one would hope: The different kinds of linear motion studied in chapter 1 correspond to the flows near general points of equilibrium. Equilibria with no purely imaginary eigenvalues are said to be hyperbolic.The exception for centres with imaginary eigenvalues is easy to understand. The motion in the eigenplane was in this case seen to lie on closed ellipses, the boundary case between tending to the origin or away from it. Higher terms in the Taylor expansion of the vector field may still push it either way. However, purely imaginary eigenvalues are generic in the class of Hamiltonian systems, so that in their case the Hartman-Grobman theorem is only a partial result. A full understanding of the motion near a stable Hamiltonian system will become possible only after the discussion of the theorem of Kolmogorov, Arnold and Moser in chapter 6.

The Hartman-Grobman theorem guarantees that for every real eigenvector (or eigenplane) of the linearized system there corresponds a curve (or a two-dimensional surface) in the nonlinear system. Grouping together all the eigenvectors with a negative real part, the resulting invariant plane $E ^ { - }$ with dimension N- contains allthe points that tend to theequilibrium x.in the linearized system as $t  \infty$ . Similarly, the invariant plane $E ^ { + }$ with dimension N+ contains all the x →x.as t → - oo. If x. is hyperbolic, then $N ^ { - } + N ^ { + } = N$ . The Hartman-Grobman theorem identifies $E ^ { - }$ and $E ^ { + }$ respectively,with $W ^ { - }$ ,the stable manifoldnd $W ^ { + }$ ,theunstablemanifold,of the nonlinerilereeingteotyatttin $W ^ { \pm }$ tend to x when t →干 oo. Though the Hartman-Grobman theorem is only local, we can obviously extend the stable manifold to include the orbits of all of its points, defined in the neighbourhood of x for t→- oo,and likewise for $W ^ { + }$ .The stable manifold theorem establishes the plausible result that W=are tangent at x.to the invariant planes E+ and also that W+ are differentiable as many times as the field f itself.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/acd57ab85b48f4faf85b84f6e71e86e0b99f0f9612623b6bbb6870902176068f.jpg)  
$\mathrm { F i g } \textcircled { 2 . 3 . }$ (a) Linearized motion for the system $\dot { x } = x , \dot { y } = y + x ^ { 2 } .$ (b) Stable and unstable manifolds $W ^ { \pm }$ for the full nonlinear system.

The foregoing abstract discussion becomes more tangible with a simple example and some exercises taken from Guckenheimer and Holmes (1983). Consider the system

$$
\dot { x } = x , \qquad \dot { y } = - y + x ^ { 2 } .
$$

In this case $E ^ { + }$ corresponds to the $x$ axis and $E ^ { - }$ to the $y$ axis. Eliminating the time from the system, we obtain the diferential equation

$$
\frac { d y } { d x } = - \frac { y } { x } + x , \qquad \mathrm { o r } \qquad \dot { x } \frac { d y } { d x } + y = x ^ { 2 } .
$$

This can be immediately integrated, whereby

$$
y = { \frac { x ^ { 2 } } { 3 } } + { \frac { c } { x } }
$$

is the equation of the orbits. From the stable manifold theorem we know that $W ^ { + }$ is the orbit tangent to the $x$ axis at the origin; it has $c = 0$ .The stable manifold $W ^ { - }$ is still the $y$ axis. The graphs for the linear and the nonlinear systems are shown in figs(2.3a andb,jrespectively.

# Exercises

Find the points of equilibrium of the following systems and classify the respective linear parts. Start by rewriting the second-order equations as first-order systems:

$$
\begin{array} { r l } & { \mathrm { ( a ) ~ } \ddot { x } + \varepsilon \dot { x } - x + x ^ { 3 } = 0 , } \\ & { \mathrm { ( b ) ~ } \ddot { x } + \sin x = 0 , } \\ & { \mathrm { ( c ) ~ } \ddot { x } + \varepsilon \dot { x } ^ { 2 } + \sin x = 0 , } \\ & { \mathrm { ( d ) ~ } \dot { x } = - x + x ^ { 2 } , ~ \dot { y } = x + y , } \\ & { \mathrm { ( e ) ~ } \ddot { x } + \varepsilon ( x ^ { 2 } - 1 ) \dot { x } + x = 0 . } \end{array}
$$

(Where ε appears let ε<0,ε=O and ε >O.) Try to surmise the global structure of the stable and unstable manifolds in all these cases.

# 2.3 General Poincare sections: maps

A special kind of Poincare section has already been presented in section 1.3. In general we cut the N-dimensional phase space by an(N - 1)-dimensional plane $\Sigma$ [or more generally by an $( N - 1 )$ dimensional manifold].The first returnofthe orbit ofeach point in $\Sigma$ ,with the sameorientation with which it started off,efinesa ifeomorphism T:→∑,nownas the Poncare map. If $\tau$ is the time that an orbit starting at $\mathbf { x } _ { 0 }$ takes to return to $\scriptstyle \sum$ ,we have

$$
\begin{array} { r } { { \bf T } ( { \bf x } _ { 0 } ) = { \bf x } ( { \bf x } _ { 0 } , \tau ) . } \end{array}
$$

If $\Sigma$ is a coordinate plane, (2.9) reduces to a set of $N - 1$ equations.

A periodic orbit of a dynamical system generates periodic points of the Poincarempthatisaltho $\mathbf { X } _ { j }$ of the orbit with $\Sigma$ ,there is a number $n$ such that

$$
\mathbf { T } ^ { n } ( \mathbf { x } _ { j } ) = \mathbf { x } _ { j } .
$$

In other words,a periodic pointis afixed point of some power of the map. The diffeomorphism $\mathbf { T } ^ { n }$ can always be approximated by its linear part $D ^ { \prime } \mathbf { T } ^ { n }$ The stability matrix $\mathcal { M }$ associated with this map can then be identified with the flow matrix $\exp ( \mathcal { A } t )$ for $t = 1$ of the linear system, whose dyamical matrix is $\mathcal { A } = \ln \mathcal { M }$ Each eigenvalue $\gamma$ of $\mathcal { M }$ corresponds to an eigenvalue $\lambda = \ln \gamma$ of $\mathcal { A }$ and both matrices have the same eigenvectors. We can thus define stable and unstable invariant planes $E ^ { \pm }$ for the map $\mathbf { T } ^ { n }$ in exactly the same way as for a continuous flow. The point $\mathbf { X } _ { j }$ will be hyperbolic if the dimensions $N ^ { \pm }$ of $E ^ { \pm }$ add up to $N$ ,that is,if $D ^ { \prime } \mathbf { T } ^ { n }$ has no eigenvalues with unit modulus.

The Hartman-Grobman theorem can be extended to maps. First we define topological equivalence between two maps (difeomorphisms F and $\mathbf { G }$ ) to mean that there exists a homeomorphism $\mathbf { y } = \mathbf { H } ( \mathbf { x } )$ such that $\mathbf { H } ( \mathbf { F } ( \mathbf { x } ) ) = \mathbf { G } ( \mathbf { y } )$ .The theorem is then as follows: Let $\mathbf { G }$ be a diffeomorphism with a hyperbolic fixed point $\mathbf { X } _ { e } ,$ Then there exists a neighbourhood of $\mathbf { X } _ { \mathrm { e } }$ where $\mathbf { G }$ is topologically equivalent to $D \mathbf G$ ,the linear part of G.

The fundamental importance of this extension of the Hartman-Grobman theorem lies in the fact that periodic orbits are much more common than equilibria in dynamical systems. In fact, we have shown that they are dense in the case of the cat map.

The discrete form of the Hartman-Grobman theorem is proved in Arnold (1982),and the theorem for flows is an immediate consequence. The stable manifold theorem can also be extended to diffeomorphisms; that is, the stable and unstable manifolds $W ^ { \pm }$ ,corresponding to $E ^ { \pm }$ ,are tangent to the planes $E ^ { \pm }$ at $\mathbf { x } _ { \mathrm { e } }$ ;the $W ^ { \pm }$ surfaces are differentiable as many times as the map G. It should be noted that the orbits of a map will be a sequence of discrete points, even if they lie on an invariant curve. The local structure of the orbits for a map on the plane with real eigenvalues is shown in fig2.4.

Returning now to the case of a periodic point, we note that the linearized transformation is simply given by the chain rule as

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/c01da06d76d7b0262cbb23edfc9bc3a798eb132728197f3b2787da801ed373ea.jpg)  
Fig2.4JNonlinearmapscanhavestableandunstablemanifoldsjustascontinuous systems doeventhough the orbitsaredscrete its

$$
D \mathbf { T } ^ { n } ( \mathbf { x } _ { 0 } ) = D \mathbf { T } ( \mathbf { T } ^ { n - 1 } ( \mathbf { x } _ { 0 } ) ) D \mathbf { T } ( \mathbf { T } ^ { n - 2 } ( \mathbf { x } _ { 0 } ) ) \cdots D \mathbf { T } ( \mathbf { x } _ { 0 } ) .
$$

In the case of the Poincare map,however, we are stil bound by the need to follow the flow,soas to work out the map.Poincare sections are a good way to present computations of the orbits of higher-dimensional systems, but only very rarely can we directly deduce the map from the flow, as in the example at the end of this section.

The great value of Poincaré sections manifests itself in the study of generic properties of dynamical systems. For instance, we see that in the neighbourhood of a hyperbolic periodic orbit $\gamma _ { - }$ ，corresponding to a hyperbolic periodic point of a Poincare section, there will be stable and unstable manifolds $W ( \gamma )$ , such that all the orbits on $W ^ { - } ( \gamma )$ approach $\gamma$ as $t  \infty$ ， whereas all orbits in $W ^ { + } ( \gamma )$ approach $\gamma$ as $t \to - \infty$ .The relation between the full stable and unstable manifolds and those on the Poincare section is sketched in fig2.5.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/9d0d2c0ac895b65a2a87df158fa2f982ed0a35b4689d5e657b12a63ae91c4bb7.jpg)  
Fig[2.5J The stable and unstable manifolds of a Poincare map are the sections of two-dimensional surfaces in phase space that intersect along the periodic orbit.

We conclude this section by identifyingstroboscopic maps,derived from the observation of the flow at regular intervals, with the Poincare map. We have already worked with stroboscopic maps in the case of autonomous linear systems, in which case they are isomorphic to their parent flows. Forced oscillationswere the field is riodic inime,t is, $\mathbf f ( t + \tau ) = \mathbf f ( t )$ for all t,lead to a much richer relationship between map and flow. We can always consider the iterations of the map resulting from the flow for each period $\tau$ as the result of successive sections at the planes $\theta _ { 0 } + 2 m \pi$ for the autonomous system

$$
\dot { { \bf x } } = { \bf f } ( { \bf x } , \theta \tau / 2 \pi ) , \qquad \dot { \theta } = 2 \pi / \tau .
$$

The following example of a forced linear oscillator

$$
\ddot { x } + 2 \beta \dot { x } + x = \gamma \cos \omega t
$$

at resonance,ω =|1-β²1/2,is borrowed fromGuckenheimerand Holmes (1983). It can be treated as the system

$$
\scriptstyle { \left[ \begin{array} { l } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { - 1 } & { - 2 \beta } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } + { \left[ \begin{array} { l } { 0 } \\ { \gamma \cos \theta } \end{array} \right] } ,
$$

The general solution of the second-order equation is known to have the

$$
x ( t ) = \exp { ( - \beta t ) } ( C _ { 1 } \cos { \omega t } + C _ { 2 } \sin { \omega t } ) + A \cos { \omega t } + B \sin { \omega t } ,
$$

where the constants $C _ { 1 }$ and $C _ { 2 }$ are determined by the initial conditions as

$$
C _ { 1 } = x _ { 0 } - A , \qquad C _ { 2 } = - B + [ \dot { x } _ { 0 } + \beta ( x _ { 0 } - A ) ] / \omega .
$$

Identifying $x _ { 1 } ( t ) = x ( t )$ and $x _ { 2 } ( t ) = \dot { x } ( t ) ,$ ，we obtain the Poincare map $\mathbf { x } ( \mathbf { x } _ { 0 } , t = 2 \pi / \omega )$ as

$$
\begin{array} { r l } & { x _ { 1 } = A + ( x _ { 1 0 } - A ) \exp { ( - 2 \pi \beta / \omega ) } , } \\ & { } \\ & { x _ { 2 } = \omega B + ( x _ { 2 0 } - \omega B ) \exp { ( - 2 \pi \beta / \omega ) } . } \end{array}
$$

This is a linear map with degenerate eigenvalues $\exp ( - 2 \pi \beta / \omega )$ Therefore, the map orbits approach the fixed point $( A , \omega B )$ radially (fig.2.6).JTheflow

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/87f98a46c362589f02e22edab4c0dfec953778cad135bd7999ec17c385642e09.jpg)  
Fig 2.6./The fixed point of the Poincare map for the system obtained from the equation x + 2βx + x = ycos wt is not at the origin. The map orbits approach this point radially.

tends asymptotically to a periodic orbit. Note that even in this simple case the map depends on the initial time or phase $\theta _ { 0 }$ , taken here to be zero.

# 2.4 Poincare sections of Hamiltonian systems

The conservation of energy in a Hamiltonian system enables us to reduce the phase space of a Poincare section by two dimensions rather than one. This followsfromtherestrictionof thePoincaresection(2.9totheenergy surface or energy shell,

$$
H ( \mathbf { p } , \mathbf { q } ) = E .
$$

Thus, if $\Sigma$ is the plane $q _ { 1 } = 0$ ,we can use $( p _ { 2 } , \ldots , p _ { L } , q _ { 2 } , \ldots , q _ { L } ) = ( \mathbf { P } , \mathbf { Q } )$ as coordinates for the intersection of $\Sigma$ with the energy surface,and determine $p _ { 1 }$ from (2.13).

A fundamental property of Hamiltonian Poincare maps is that they are canonical transformations,in the same way as are the stroboscopic maps generated by Hamiltonian flows. Invariance of the symplectic area for differential parallelograms implies the conservation of the symplectic area S for any closed loop in the phase space

$$
S = \sum _ { l = 1 } ^ { L } S _ { l } , \qquad .
$$

where each $S _ { l }$ is the area of the projection of the loop onto the lth

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/c779d787d9d9ffb6252645dee5e86ef9d0d87bc04e4582295a87e6aa9da1cff8.jpg)  
Fig2.7.jThe symplectic area fora closed circuit is the algebraic sum of the areas of its projestions onto all the canonical conjugate planes. It is invariant with respect to Hamiltonian flows.

conjugated plane,

$$
S _ { l } = \oint p _ { l } d q _ { l } ,
$$

as shown in fig.(2.7, (Plane Poincare maps are area preserving.) The symplectic area S is also known as the reduced action. Its invariance is a consequence of the Poincare-Cartan integral theorem: Given a tube of trajectories in extended phase $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } , t )$ generated by a closed curve $\Gamma _ { 1 }$ ,then any other irreducible curve $\Gamma _ { 2 }$ around the same tube will have the same full action:

$$
\oint _ { \Gamma _ { 1 } } [ \mathbf { p } \cdot d \mathbf { q } - H  = \oint _ { \Gamma _ { 2 } } [ \mathbf { p } \cdot d \mathbf { q } - H  -  H  - 
$$

Figure(2.8 shows a tube of trajectories for a system with a single freedom. It is important to note that the theorem in no way restricts each curve $\Gamma _ { j }$ to have a definite time or a given energy $E$ .The imposition of either of these conditions leads immediately to the conservation of the reduced action

$$
\oint _ { \Gamma _ { 1 } } \mathbf { p } \cdot d \mathbf { q } = \oint _ { \Gamma _ { 2 } } \mathbf { p } \cdot d \mathbf { q } .
$$

Any closed circuit $\Gamma _ { 1 }$ in a Poincaré section $\Sigma$ defines a tube of trajectories that intersects $\Sigma$ again in a new circuit $\Gamma _ { 2 }$ .Since all these orbits have the same energy by construction, (2.17) holds.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/132c6dfa43b11d7d9cdea519f62f0daa357981ecdc983e6ebd29cc1bb3b291bd.jpg)  
Fig.2.8.jThe trajectories that start out from a closed curve T define a tube of trajectories; F2 is any other curve obtained by cutting this tube.

The Poincaré-Cartan integral theorem is one of the cornerstones of classical mechanics.Arnold (1978) uses it to derive Hamilton's variational principle.Yetthelateris themorefamiliarstarting point inphysics courses, so it is worthwhile outlining the deduction in the opposite direction. The variational principlestates that,givenany one-parameter familyofcurves $\gamma _ { \lambda }$ joining the lines $( q _ { 1 } , t _ { 1 } )$ to $( q _ { 2 } , t _ { 2 } )$ in extended phase space such that $\gamma _ { 0 }$ is a trajectory of the system,then

$$
\int _ { \gamma _ { \lambda } } \left[ { \bf p } \cdot d { \bf q } - H d t \right] - \int _ { \gamma _ { 0 } } \left[ { \bf p } \cdot d { \bf q } - H d t \right] = O ( \lambda ^ { 2 } ) .
$$

Here we introduce the standard notation, that a function $f ( x ) = O ( x )$ if

$$
\operatorname* { l i m } _ { x \to 0 } \left| { \frac { f ( x ) } { x } } \right| < \infty .
$$

Let us now define a one-parameter family of trajectories $\gamma ^ { \prime } ( \lambda )$ so that $\gamma ^ { \prime } ( 0 ) = \gamma _ { 0 }$ ,and let $\Gamma$ be an arbitrary curve joining $( \mathbf { q } _ { 1 } , t )$ and $( \mathbf { q } _ { 2 } , t )$ embedded in the resulting two-dimensional surface. This construction is shown in fig2.9jin the case of one freedom. If $\Lambda$ is the largest value taken by $\lambda$ along $\Gamma$ ,we can calculate the closed integral

$$
{ \boldsymbol { \sigma } } \equiv \int _ { \gamma _ { 0 } } \left[ \mathbf { p } \cdot d \mathbf { q } - H d t \right] - \int _ { \Gamma } \left[ \mathbf { p } \cdot d \mathbf { q } - H d t \right]
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/1d3358c4fcb4fcfb3cc63631acd752b43a3cda377c0735072f90c14b1969ba99.jpg)  
Fig(2.9.)In this construction $\gamma _ { 0 }$ is a trajectory and $\Gamma$ is some curve contained in the surtace $\gamma ^ { \prime } ( \lambda ) ,$ with the same end points as $\gamma _ { 0 }$ ·

by subdividing it into the $n$ closed integrals

$$
\sigma = \sum _ { j = 1 } ^ { n } \oint _ { j } [ \mathbf { p } \cdot d \mathbf { q } - H d t ] ,
$$

obtained by starting out from $\Gamma$ along $\gamma ^ { \prime } ( j \Lambda / n )$ until meeting $\Lambda$ again and then returning along $\gamma ^ { \prime } ( ( j + 1 ) \Lambda / n )$ .Each integral in(2.21) can be interpreted as the difference in total action between a trajectory and a nearby path. Thus, the variational principle (2.18) implies that

$$
\sigma = \operatorname* { l i m } _ { n  \infty } \sum _ { j = 1 } ^ { n } O \biggl ( ( { \frac { \Lambda } { n } } ) ^ { 2 } \biggr ) = 0 .
$$

Consider now an arbitrary reducible curve inscribed in a one-parameter family of trajectories, which means that the curve can be continuously shrunk to a point, without leaving the two-dimensional surface. The total action for such a curve will be zero as a consequence of(2.22). This is not the case of the two curves $\Gamma _ { 1 }$ and $\Gamma _ { 2 }$ specified in the Poincare-Cartan theorem but we can construct a reducible curve by cutting the tube of trajectories in fig2.8and joining $\Gamma _ { \mathrm { ~ 1 ~ } }$ and $\Gamma _ { 2 }$ by the two paths along the cut. The integrals of the action along both paths on either side of the cut cancel out, leaving

$$
\sigma = \sigma _ { \Gamma _ { 1 } } - \sigma _ { \Gamma _ { 2 } } = 0 .
$$

We conclude this section with a discussion of the local motion in the neighbourhood of periodic orbits of Hamiltonian systems. A Poincare section reduces the flow to a canonical map with two fewer dimensions. If the map is linearized,it can be identified with the linear flow derived from a quadratic Hamiltonian belonging to one of the categories classified in section 1.2.If the original system has two freedoms,the reduced system has only one; then the generic possibilities are real or purely imaginary eigenvalues (classes 1 and 2 in section 1.2). The Hartman-Grobman theorem guarantees that in the former case the nonlinear map can be transformed to its linear part by a homeomorphism. For three or more freedoms,itissopossible tohaveareduced quadratic Hamiltonaninone of the classes 3and 5vovingrspectivelympe gevluel degenerate eigenvalues. In these cases the corresponding nonlinear maps are topologically equivalent to their linear part.

# 2.5 Reduction to time-periodic systems

Wefound in section 2.3 that the stroboscopic map ofa time-periodic system can be identified with the Poincare map of an autonomous system augmented by one dimension. We shallnow investigate the converse procedure, namely, the reduction of autonomous systems to timedependent systems of fewer dimensions,in the vicinity of a periodic orbit.

For general systems this task is trivial in principle.All we have to do is change the coordinate system $\mathbf { x } \to ( \theta , \mathbf { X } )$ with vector field $( f _ { \boldsymbol { \theta } } , \mathbf { F } )$ in such a way that the closed orbit (of period $\tau$ )becomes the $\theta$ coordinate line $( \theta , \mathbf { 0 } )$ with velocity

$$
\dot { \theta } = \omega = 2 \pi / \tau .
$$

Neighbouring orbits will not generally coincide with the closed lines $( \boldsymbol { \theta } , \mathbf { X } _ { 0 } )$ The construction for a two-dimensional system showing the periodic orbit andone ofitsneighbours isdrawn infig2.1Becauseofcontinuityhre will be a region surrounding the periodic orbit where

$$
\dot { \theta } = f _ { \theta } ( \theta , { \bf X } ) \neq 0 . \qquad \ .
$$

In this neighbourhood we can define the reduced system

$$
\frac { d \mathbf { X } } { d \theta } { = } \frac { \mathbf { F } ( \mathbf { X } ; \theta ) } { f _ { \theta } ( \mathbf { X } ; \theta ) } ,
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/5d3c4df67194783ee7c02b40e48948aa1cee2c9162a6461675b465a0424f7962.jpg)  
Fig2.10.Qrbits near a periodic orbit are not generally closed lines, but in this region the angular coordinate satisfies $\dot { \theta } \neq 0$

$( 2 \pi )$ -peri6dic in the time' 0.The strosboscopic map $\theta = 2 m \pi$ of the reduced system coincides with the Poincare map of the full system (fig.2.10).)

AHamiltonian system requires more careful treatment if we are to ensure that the reduced system is also Hamiltonian. Let us for the moment Suppose that canonical coordinates (J,P,0,Q) can be found, where 0 has the same properties as in the preceding paragraph. Then condition (2.25), that is,

$$
\dot { \theta } = \partial H / \partial J \neq 0
$$

near the orbit, implies that we can invert the relation $H ( \mathbf { p } , \mathbf { q } ) = E$ to obtain the well-behaved function

$$
J = K ( { \bf P } , { \bf Q } ; \theta ; E ) .
$$

Consider now the variational system.It identifies trajectories as the paths that minimize the complete action among all possible paths. In particular, these include all the paths with the same energy as both end-points of the trajectory. But for these paths the full action equals the reduced action:

$$
\int [ { \bf p } \cdot d { \bf q } - H d t ] = \int { \bf p } \cdot d { \bf q } = \int [ { \bf P } \cdot d { \bf Q } - K d ( - \theta ) ] .
$$

The isomorphism between the first and the last term in (2.29) then guarantees that the orbits in the energy shell satisfy Hamilton’s equations

$$
{ \frac { d \mathbf { P } } { d t } } = - { \frac { \partial K } { \partial \mathbf { Q } } } , \qquad { \frac { d \mathbf { Q } } { d t } } = { \frac { \partial K } { \partial \mathbf { P } } } ,
$$

with $t = - \theta$ Thus,an autonomous Hamiltonian system can be reduced by a whole freedom near a periodic orbit. The stroboscopic map for the reduced system can be identified with the Poincare map for the full system.

Reduction of the Hamiltonian was achieved under the assumption that suitable canonical coordinates could be found, which must now be verified. The first point to note is that periodic orbits generally appear in Hamiltonian systems within one-parameter families. This is easily shown by considering the one-parameter family of Poincare sections, obtained by varying the energy. The intersection of a given periodic orbit of energy E with its Poincare section is a fixed point of the map:

$$
\mathbf { T } ^ { n } ( \mathbf { X } , E ) = \mathbf { X } .
$$

Differentiating (2.31) with respect to $E$ ,we obtain

$$
\frac { d \mathbf { X } } { d E } = ( \mathbf { 1 } - \mathcal { M } ^ { n } ) ^ { - 1 } \frac { d \mathbf { T } ^ { n } } { d E } ,
$$

where $\mathcal { M } ^ { n } = D \mathbf { T } ^ { n }$ .So we can use the implicit function theorem to define the family of fixed points $\mathbf { X } ( E ) .$ except at the resonant energies where

$$
\operatorname* { d e t } ( \mathcal { M } ^ { n } - 1 ) = 0 .
$$

We shallse in chapter 4 that at these energies the periodic orbit family bifurcates; that is,there is a coalescence of orbit families.In some cases (integrable systems) the periodic orbits come in families with $L$ or more parameters, but in the following discussion we shall consider only the twodimensional annulus- $\because$ obtained by varying a single energy-dependent parameter.

The ideal coordinate system, to study the neighbourhood of periodic orbits,embeds the nlu $\gamma$ in a coordinate surface. To find what kind of surface this is,we check the skew product of two independent vectors tangent to $\gamma$ .Choosing $\eta = ( - \hat { c } H / \hat { o } \mathbf { q } , \hat { c } H / \hat { o } \mathbf { p } )$ ,the velocity vector tangent to the periodic orbit, and ${ \boldsymbol { \xi } } = ( d { \boldsymbol { \mathbf { p } } } , d { \boldsymbol { \mathbf { q } } } )$ we have

$$
\pmb { \eta } \wedge \pmb { \xi } = \frac { \hat { c } H } { \hat { c } \mathbf { p } } \cdot d \mathbf { p } + \frac { \hat { c } H } { \hat { \sigma } \mathbf { q } } \cdot d \mathbf { q } = d H ( \pmb { \xi } ) \neq 0
$$

by construction. According to conditions (1.46) we can then choose $\xi$ and $\eta$ to be in the new $( p _ { 1 } , q _ { 1 } )$ plane.

By contrast, any vector $\xi ^ { \prime }$ chosen in the tangent plane of the energy surface along the periodic orbit has $d H ( \xi ^ { \prime } ) = 0$ ; therefore,its skew product with $\pmb { \eta }$ is zero. The result of the exercise on page 13 is that any vector $\xi$ defines a unique $( 2 L - 1 )$ -dimensional plane with the property that all the vectors in it have a null skew product with $\xi$ (its skew-orthogonal plane). Hence, for any choice of $\xi$ in $\gamma ,$ as in (2.34), the intersection of its skeworthogonal plane with the tangent plane to the energy surface is I, a $( 2 L - 2 )$ -dimensional plane that can be taken as the basis for the remaining $( \mathbf { P } , \mathbf { Q } )$ coordinates. Figure 2.11strows-a-three-dimensional reduction of the resulting geometry,in which γ is fully two-dimensional, the energy surface appears as two-dimensional and $\Gamma$ is reduced to a single dimension.

Taking radial and angular coordinates in the $( p _ { 1 } , q _ { 1 } )$ plane, so that the periodic orbits are coordinate lines, we achieve the required canonical transformation. As a bonus we also obtain

$$
\frac { \partial H } { \partial \mathbf { P } } \Bigg | _ { \gamma } = \frac { \partial H } { \partial \mathbf { Q } } \Bigg | _ { \gamma } = 0 ,
$$

that is, local invariance of the Hamiltonian with respect to the transverse coordinates $( \mathbf { P } , \mathbf { Q } )$ . However, it is not generally possible to find a transformation that makes the Hamiltonian completely independent of the transverse coordinates, for then all orbits would lie in two-dimensional $( \mathbf { P } , \mathbf { Q } ) =$ const planes; that is,al orbits would be periodic. At best we can choose the Hamiltonian to be independent of $( \mathbf { P } , \mathbf { Q } )$ for $| \theta | < \alpha < \pi$ so that the $( \theta = 0 , J = \mathrm { c o n s t } )$ plane coincides with the Poincare section.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/d3bdb99cffc0b889a2a26e5fe5c0f8f6eaf9120a117e1c329367f69efb489b97.jpg)  
Fig2.11Jy is the twodimensional annulus formed by the one-parameter family of periodic orbits. The skew-orthogonal plane $\Gamma$ to the flow vector $\eta$ of a periodic orbit is tangent to the energy surface $H ( \mathfrak { p } , \mathfrak { q } ) = E$

The generality of the above reduction can distort symmetries of the original system, which may be worth preserving. There is_a simpler alternative, when the projection of the closed orbit onto one of the coordinate planes does not intersect itself (fig.2.12).We can then choose this to be the $( p _ { 1 } , q _ { 1 } )$ plane and transform to $( J , \theta )$ coordinates in it, so tht $2 \pi J$ is the area ofeach projected closed orbit and $\dot { \theta } =$ const along each orbit. Then $( \mathbf { P } , \mathbf { Q } )$ will be the remaining coordinates of the untransformed system.

Suppose now that the system has a special symmetry. As an example we will examine the important case in which it has time-reversal symmetry; namely,the motion projected onto the q coordinate plane has the property that changing the velocity ${ \dot { \mathbf { q } } } \to - { \dot { \mathbf { q } } }$ amounts to running the system backward in time. In particular this is obtained for $p$ -symmetric Hamiltonians:

$$
H ( { \bf p } , { \bf q } ) = H ( - { \bf p } , { \bf q } ) .
$$

Consider now running a symmetric periodic orbit forward and back ward in time from the point where $p _ { 1 } = 0$ Because of the symmetry of the

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/983fd4971bfbd096a1dab5bbd84ca08347f6dd50609e3ef682379a47fbc31cdc.jpg)  
Fig2.12Tefmilyofperodicbitscanbeprojetedtothe $( p _ { 1 } , q _ { 1 } )$ plane, and the variable $J$ can be defined so that $2 \pi J$ is thearea of a periodic orbit.

Hamiltonian and the fact that $\dot { \theta }$ is constant,we shall have $- \theta ( t ) = \theta ( - t )$ so $p _ { 1 } ( - \theta , J , - \mathbf { P } , \mathbf { Q } ) = - p _ { 1 } ( \theta , J , \mathbf { P } , \mathbf { Q } )$ and $q _ { 1 } ( - \theta , J , - \mathbf { P } , \mathbf { Q } ) = q _ { 1 } ( \theta , J , \mathbf { P } , \mathbf { Q } )$ Thus,the new coordinates preserve symmetry for the full Hamiltonian,

$$
H ( J , \theta , { \bf P } , { \bf Q } ) = H ( J , - \theta , - { \bf P } , { \bf Q } ) ,
$$

and for the reduced Hamiltonian,

$$
K ( \mathbf { P } , \mathbf { Q } ; \theta ; E ) = K ( - \mathbf { P } , \mathbf { Q } ; - \theta ; E ) .
$$

Since the Poincaré map T is the stroboscopic map for the reduced flow, in which $\theta$ is taken from $0 \to - 2 \pi$ ,the inverse $\mathbf { T } ^ { - 1 }$ is the map for which $\theta$ is taken from $0 \to + 2 \pi$ .Therefore, the inverse Poincare map is obtained by reflecting the coordinate P, propagating the point forward in time and reflecting $\mathbf { P }$ back again. Defining the reflection

$$
\mathbb { R } { : ( \mathbb { P } , \mathbb { Q } ) \to ( - \mathbb { P } , \mathbb { Q } ) } ,
$$

we find that

$$
\mathbf { T } ^ { - 1 } = \mathbf { R } \cdot \mathbf { T } \cdot \mathbf { R }
$$

as shown in fig.2.13.This property of $\mathbf { T }$ with respect toan inversion Rfor

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/c54ea1bb8673889302a5d905e907bd823a360d247e686570cccd8a010834f963.jpg)

Fig2.13) The inverse of a reversible map can be obtained as a product of the map T and the symmetry $\mathbf { R }$

which

$$
\mathbf { R } \cdot \mathbf { R } = 1
$$

where 1is the identity map,defines a reversible map according to Greene, Mackay， Vivaldi and Feigenbaum (1981).

# Exercises

1. Show that reversible maps can always be decomposed as the product of two inversions R and TR.   
2. Show that the property of reversibility is invariant with respect to coordinate transformations.

# 2.6 Structural stability

The Hartman-Grobman theorem presented in section 2.2 establishes the topological equivalence of some neighbourhood of an equilibrium of a nonlinear system with its linear part. Nondegenerate hyperbolic linear systems with equivalent eigenvalue structures -that is,the same number of positive,negative orcomplex eigenvalues -can be taken into eachother by homeomorphisms. It follows that all nondegenerate hyperbolic nonlinear systems with the same eigenvalue structure form a class of topologically equivalent systems. A suficiently small perturbation of such a system will turn it into a new system with the same eigenvalue structure as it had before and hence the same equivalence class. The system is then said to be structurally stable in a neighbourhood of the equilibrium.

The notion of topological equivalence is too restrictive to be taken as a basis for the generalization of the definition of structural stability to the neighbourhood of periodic orbits. We have seen in the preceding section that a one-parameter family of systems wil generally support oneparameter families of periodic orbits. However, there is no restriction placed on the period of these closed orbits, which must be equal in order to be topologically equivalent. Following Arnold (1982), we thus define two systems to be topologically (orbitally) equivalent (in some region of phase space) if there exists a homeomorphism that associates the orbits of both systems. This definition does not imply equal time intervals for the equivalent sections of each pair of orbits. Finally we define a system to be structurally stable if it is contained in a neighbourhood of systems topologically (orbitally) equivalent to it. This definition is inclusive of the neighbourhoods of nondegenerate hyperbolic points already treated.

The conjecture that the concept of structural stability permits a global classification of ‘typical’ dynamical systems is borne out for twodimensional autonomous systems. This is the content of Peixoto's theorem (Peixoto and Peixoto, 1959): A plane dynamical system with an $r$ -times differentiable vector field,which points in (out) of every point along a compact boundary,is structurally stable in the bounded region ifand only if

1. the number of points of equilibrium and periodic orbits are finite and all are hyperbolic; and 2. there are no orbits joining a saddle point to another or to itself.

The structurally stable systems form a dense open subset in the set of systems with $r$ -times differentiable fields and the same boundary condition.

This statement means that arbitrarily small perturbations exist which make any system structurally stable. This extremely strong result, for systems restricted only by the two conditions of Peixoto's theorem, is a consequence of the small dimensionality of the phase space. In fact, the theorem can be generalized to systems defined on compact surfaces such as spheres or tori (Peixoto, 1962). The orbits alteady have one dimension; since they never cross,there remains only one dimension in which they can get tangled up.Figure2.14 shows examples of(a)structurally stable and(b) unstable systems in the plane.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/1da2b8fd7c3197c857572671553542251093ba3d31051743378e7d5e2a08ac27.jpg)  
Fig(2.14.Phase diagrams for (a) structurally stablel systems in the plane and (b) structurally unstable systems, according to Peixotos theorem.

For flows in three or more dimensions, or equivalently for maps of two or more dimensions, the situation becomes more complicated. In particular Smale constructed in 1965 an example, discussed in Arnold (1982),of a three-dimensional diffeomorphism whose neighbourhood contains no structurally stable systems.

It is worth emphasizing that we are dealing here with typical systems not generated by a Hamiltonian. For instance, we found in section 1.2 that elliptic points (centres) are structurally stable with respect to linear perturbations of the Hamiltonian, but they are unstable with respect toa general linear perturbation, or even a nonlinear Hamiltonian perturbation, as we shall see in chapter 6. The reader willfind preparatory material and a sketched partial proof of Peixoto's theorem in Guckenheimer and Holmes (1983), a book dealing mainly with dissipative systems.

# Exercise

Show that a Hamiltonian system in the plane never satisfies the conditions of Peixoto’s theorem.

An important exception to the difficulty of achieving global understanding of the structure of two-dimensional maps is furnished by Anosov's theorem,demonstrated in Arnold(1982): The cat map is structurally stable. In other words,any diffeomorphism on the torus sufficiently close to the cat map can be taken into it by a homeomorphism.

These systems bear no resemblance to those established by Peixoto's theorem to be structurally stable -they are the prototype of chaotic conservative systems. Typically， conservative diffeomorphisms exhibit chaotic regions mixed up with regular regions, as we shall see. It is not surprising, therefore, that no statement can be made about making arbitrary maps on the torus structurally stable, in contrast to Peixoto's theorem. For example, the elliptic linear map presented in section 1.4 is neither structurally stable nor close to a linear hyperbolic map.

# Chaotic motion

The flow in an autonomous Hamiltonian system with one freedom is even more restricted than the generic motion categorized by Peixoto's theorem. The constancy of the Hamiltonian holds all the orbits to its level curves. For a bound system most of these will be closed loops, the exception being the levels of sddle points, that is,unstable equilibria of the Hamiltonian. he corresponding orbits either start out at an unstable point as $t \to - \infty$ and return to the same point $2 5 t  + \infty$ , or go on to another unstable point. These two cases,knoyn respectively as homoclinic and heteroclinic orits are shown in figs.3.1aandbfunder the potential curves $V ( q )$ that generate them,if the Hamiltonian has the form $p ^ { 2 } + V ( q ) ]$ .The homoclinic orbit of the pendulum (fig.3.1b)jis known as the separatrix between the small librations of the system and the full rotatons-arising at higher energies.

Consider making a small perturbation to this system, that is,eoupling to another degree of freedom or,equivalentlyadding an oscillatory forcing term to the Hamiltonian. Far from the unstable equilibrium,anorbit close to the separatrix will feel mainly the unperturbed Hamiltonian. But this gives a zero force near the saddle, so the perturbation becomes dominant near the unstable point: It can switch librations into rotations and back again. Successive switches will be uncorrelated, because the periods of rotations and librations lying close to the separatrix vary infinitely. The resulting motion can be classified as chaotic,albeit constrained to a narow strip of phase space. It is bounded by closed curves, which survive in the Poincare map of the system, according to the theorem of Kolmogorov, Arnold and Moser to be discussed in chapter 6. Of course, the chaotic region widens as the perturbation parameter is increased.

The separatrices correspond to the stable and unstable manifolds of the equilibrium, which continue to exist in the Poincare map. Far from the equilibrium their extensions usually cross transversely at discrete homoclinic (heteroclinic) points. We begin this chapter with the study of Melnikov's analytic criterion for such crossings to occur. Then we analyse the motion near homoclinic points, introducing the method of symbolic dynamics.TheresultistheSmaleirkhoff theorem,whichestablishes the existence of dense(chaotic) orbits and an infinite number of periodic orbits, such as were found in the cat map.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/db8a688d5fb28f465e618608eb0792ec50203279339160847e5559f05e37e836.jpg)  
$\mathrm { F i g } \widehat { ( 3 . 1 , }$ (a) The homoclinic $W _ { 0 }$ orbit isdoublyasymptotic,for $t \to \pm \infty$ to the same unstable equilibrium.(b) A heteroclinic orbit tends asymptotically to one unstable equilibrium for $t \to - \infty$ and to another for $t  \infty$

In the remainder of this chapter we discuss rudiments of ergodic theory. The definition of invariant measure on the phase space leads to a precise theory of what happens to ‘almost all orbits’. After a preliminary study of informationtoryetric tropy is trouced d oected te local Lyapunov exponent. The last section joins many strands of the chapter in the (heuristic) uniformity principle for periodic orbits.

# 3.1 Melnikov's method

Consider a one-freedom system with the Hamiltonian

$$
H ( { \bf x } , t ) = H _ { 0 } ( { \bf x } ) + \varepsilon H _ { 1 } ( { \bf x } , t ) ,
$$

where $H _ { 1 }$ is time periodic with period $\tau$ We take $H _ { 0 }$ to have an unstable point at the origin, whose stable and unstable separatrices $W _ { 0 } ^ { \pm }$ form a smooth curve, as in fig3.1a.jWe can define a continuous set of Poincare sections $\Sigma _ { t _ { 0 } }$ ; all the corresponding maps

$$
\mathbf { x } \to \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { \prime } = \mathbf { x } _ { \varepsilon } ^ { \prime } ( \mathbf { x } ( t _ { 0 } ) , t _ { 0 } + \tau )
$$

will have an unstable fixed point close to the origin, as was shown in section 2.5.

Thecbjectiveis tounderstandthewaythattheseparatrices $W _ { \varepsilon , t _ { 0 } } ^ { \pm }$ extend and in particular whether they cross transversely.The method is perturbative; that is we use the fact that $W _ { \varepsilon , t _ { 0 } } ^ { \pm }$ will remain close to $W _ { 0 } ^ { \pm }$ within appropriate time intervals, $[ t _ { 0 } , \infty )$ for the stable manifold and $( - \infty , t _ { 0 } ]$ for the unstable manifold. For instance, it is proved in Guckenheimer and Holmes (1983) that the distance between the orbits on the perturbed stable separatrix $\mathbf { x } _ { \varepsilon } ^ { - } \left( \mathbf { x } _ { \varepsilon } ^ { - } \left( t _ { 0 } \right) , t \right)$ and the unperturbed separatrix $\mathbf { x } _ { 0 } ( \mathbf { x } _ { 0 } , t - t _ { 0 } )$ is uniformly of order ε in $( t _ { 0 } , \infty )$

Let us consider now a point $\mathbf { x } _ { 0 } ( 0 )$ on the unperturbed separatrix and the straight line $\pi$ ,defined by the gradient $\partial { \cal H } _ { 0 } / \partial { \bf x }$ at this point. The line willintersect theperturbedstableandunstable manioldsat the two points $\mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { \pm } ( t _ { 0 } ) ,$ as shown in Tig3.2.We define the Melnikov functionas

$$
M ( t _ { 0 } ) = \varepsilon ^ { - 1 } [ H _ { 0 } ( \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { + } ( t _ { 0 } ) ) - H _ { 0 } ( \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { - } ( t _ { 0 } ) ) ] .
$$

Suppose how that the separatrices of the perturbed Poincare map, correspohding to Σ,.,do interesect transversely at some point h, above xo in fig3.2jIts image by the map will be another point of intersection below thelineπ,ahomoclinicpoint ht+ofthe sectionΣ+(fig.3.3).Considering all the continuum of sections between $\Sigma _ { t _ { 0 } }$ and $\textstyle \sum _ { t _ { 0 } + \tau }$ ,we obtain a continuous locus of points $\mathbf { h } _ { t }$ (the homoclinic orbit of the full system) joining $\mathbf { h } _ { t _ { 0 } }$ and hto+.Hence,there willbe a time for which h,lies on thelineπ,that isfor which $M ( t ) = 0$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/36bdbaea3103e52632a902075ca5bdff7139c1ad0cc7d324bd4a09b98f1b642a.jpg)  
Fig3.2The perturbed systemalsohasstable andunstablemanfolds $W _ { \varepsilon } ^ { \pm } _ { 0 }$ lying close t the unperturbed separatrix (the dashed line). A straight line normal to the separatrix at $\mathbf { x } _ { 0 } ( 0 )$ intersects both the stable and the unstable manifolds.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/d2a183a3a53b5860829a2ed5e983dbcb6ef31c38631de5243d0dd5337255bdea.jpg)  
Fig3.3./If there exists a homoclinic point to one side of the line $\pi _ { \mathfrak { s } }$ its image lies on the other side. The Poincare sections depend on the time,and there will be a t for which the homoclinic point lies exactly on $\pi$

The existence of a zero of the Melnikov function amounts to the existence of a homoclinic point. Transverse intersections of the separatrices give rise to simple zeros (with dM/dt ≠O). If the system is ‘integrable', so that $W ^ { \pm }$ join smoothly, the Melnikov function is identically zero. In this case the homoclinic points are nonisolated. Usually we refer to transverse intersections of separatrices simply as homoclinic points. They are the only points along the separatrices that tend to the equilibrium both as $t  \infty$ and as $t \to - \infty$

We can calculate directly the $\varepsilon \to 0$ limit of the Melnikov function from $H _ { 0 } , H _ { 1 }$ and the knowledge of the unperturbed flow. All that is required is to rewrite the Melnikov function in the form

$$
\varepsilon M ( t _ { 0 } ) = \int _ { - \infty } ^ { t } \dot { H } _ { 0 } ( \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { + } ( t ) ) d t + \int _ { t _ { 0 } } ^ { \infty } \dot { H } _ { 0 } ( \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { - } ( t ) ) d t ,
$$

which follows from the observation that $\mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { + } ( - \infty ) = \mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { - } ( \infty )$ ,the fixed point itself. Defining the Poisson bracket

$$
\{ F , G \} = \frac { \partial F } { \hat { c } q } \frac { \partial G } { \hat { c } p } - \frac { \partial G } { \hat { c } q } \frac { \partial F } { \partial p }
$$

of the functions $F$ and $\mathbf { G }$ and using the equation

$$
\dot { H } _ { 0 } = \{ H _ { 0 } , H \} = \varepsilon \{ H _ { 0 } , H _ { 1 } \}
$$

(see Goldstein,980),w

$$
M ( t _ { 0 } ) = \int _ { - \infty } ^ { \infty } \left\{ H _ { 0 } ( \mathbf { x } _ { 0 } ( t - t _ { 0 } ) ) , H _ { 1 } ( \mathbf { x } _ { 0 } ( t - t _ { 0 } , t ) \right\} d t + O ( \varepsilon ) ,
$$

since the difference between $\mathbf { x } _ { \varepsilon , t _ { 0 } } ^ { \pm } ( t - t _ { 0 } )$ and $\mathbf { x } _ { 0 } ( t - t _ { 0 } )$ is of $O ( \varepsilon )$ within each integral in (3.4).

Thus, the calculation of the integral (3.7), for xo along the unperturbed separatrix and for all $t _ { 0 }$ in the period, willreveal whether the system has a homoclinic point. The symmetry in the integral may even be sufficient to answer the question. For example, consider $H _ { 0 } = p ^ { 2 } / 2 + q ^ { 3 } / 3 - q ^ { 2 } / 2$ (fig.3.1a) perturbed by H1 =(p²/2)cos(2πt/t). The Poisson bracket $\{ H _ { 0 } , H _ { 1 } \} = ( q ^ { 2 } - q ) p \cos ( 2 \pi t / \tau ) .$ and the Melnikov function becomes

$$
M ( t _ { 0 } ) = \int _ { - \infty } ^ { \infty } ( q _ { 0 } ^ { 2 } ( t ) - q _ { 0 } ( t ) ) p _ { 0 } ( t ) \cos \biggl ( \frac { 2 \pi ( t + t _ { 0 } ) } { \tau } \biggr ) d t .
$$

If we choose po(O)=0,qo(O)=≥,the integrand wil be antisymmetric in t for to=0 (fig3.4).Thus,M(O)=Oand it is easy to verify that M(t) is not identically zero. The perturbed system therefore has isolated homoclinic points.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/5dda7937fdae04b2840356d89abf6d439f1b1b2fed8f8d6b5deceec481394158.jpg)  
Fig3.4)Thechoiceoft=Omakestheintegandof the Melinkovfunction in the example (3.8) antisymmetric, so $M ( 0 ) = 0$

The Melnikov method can be extended to deal with non-Hamiltonian perturbations,though the analysis becomes somewhat intricate. Guckenheimer and Holmes (1983) present this more general theory. It is clear that homoclinic crossings are structurally stable. A small perturbation of a Melnikov function with a nondegenerate zero produces another function with a zero.

# 3.2 The homoclinic tangle

Having established the fact that separatrices can intersect, let us deduce some of its consequences, and so build up the pattern of homoclinic motion. First we note that separatrices cannot cross themselves. This is because the image of an intersection is also an intersection. In the case of the stable manifold, there would be an infinity of self-intersections accumulating on the fixed point, in contradiction with the stable manifold theorem presented in section 2.2.

The images of the intersections of the stable manifold with the unstable manifold are again homoclinic points. Here there is no contradiction with the approximately linear structure near the fixed point (fig.3.5).It should be noted that, in the absence of reflection about the fixed point (as in the weak perturbation of an equilibrium), the map orbits do not cross the separatrix.It follows that fig3.5 ghows a pair of distinct homoclinic orbits arriving at the fixed point.

Another important property of a conservative map is that the successive loops formed between separatrix intersections must have the same area. But the distance between successive homoclinic points decreases exponentially as the fixed point is approached, so the ‘length' of the loops must grow exponentially, while avoiding self-intersections. The only way out is for the outgoing separatrix to accumulate back onto itself,as fig. 3.5 begins to show. This behaviour is in fact common to general (nonconservative) homoclinic motion, but the proof must then rely on the Palis lambda lemma (see Guckenheimer and Holmes,1983).

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/163d8f5f35a1882c17264e5ea96e8f37cab36bd2b8ee4b397a31ef7d161ebd07.jpg)  
Fig3.5.Locally the orbits do not cross the separatrix. By continuity it follows that this figure shows a pair of alternate homoclinic orbits.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/445d0f8593c43c687bacad113e11d98bbfc4db8172585fd4c022eefab4b7a2cf.jpg)  
Fig6eib

Secondary intersections among the separatrices (fig 3.6) gre not avoided. There results an infinite number of distinct homochnic orbits. In this context it is hard to resist the magic of Poincare's own description (Poincare99),re ghlyr

To even try to represent the figure formed by these two curves and their infinite intersections, each of which corresponds to a doubly asymptotic solution. The intersections form a ind of trellis,a tissue,an infinitely tight attice; each of the curves must never self-intersect, but it must fold itself ina very complex wayso as to return and cut the lattice an infinite number of times.

The complexity of this figure is so astonishing that I cannot even attempt to draw it. Nothing is more appropriate to give us an idea of the complexity of the three-body problem and in general of all the problems in Dynamics where there is/no uniform integral.

Let us consider the successive images of the small parallelogram in fig3.6Afterfiveiterations of the mapit willevolve intoaongstrip hugging theunstable manifold,soas tointersect theparalelogram (fig In general there will always be a kth iteration of the map, with the effect of stretching a neighbouring region of a homoclinic point and superpgsing it on the initial region. In the following section we will study the simplest ekample of such a process.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/3886aa20a79004b9d68014b3ec035421349e4f83726b8305c413b63bd50fb097.jpg)  
Fig.3.7.The parallelogram shown in fig. 3.6 will become an elongated strip (with the same area) that eventually intersects its pre-image.

# 3.3 Symbolic orbits

Following the presentation of Lanford (1983), we seek a transformation T of the unit square R that stretches it and folds it over itself (fig.3.8a)The mapping is not one-to-one: The set of points in R, which are brought back into R by T, consists of two vertical rectangles $\Delta _ { 0 }$ and $\Delta _ { 1 }$ ,and their images aretwo horizontal rectangles (fig.8b).The simplest choice is todefine the linear map

$$
\mathbf { T } { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } = { \left[ \begin{array} { l } { \beta p + \gamma _ { 0 , p } } \\ { \alpha q + \gamma _ { 0 , q } } \end{array} \right] } \quad { \mathrm { i n ~ } } \Delta _ { 0 } , \qquad \mathbf { T } { \left[ \begin{array} { l } { p } \\ { q } \end{array} \right] } = { \left[ \begin{array} { l } { - \beta p + \gamma _ { 1 , p } } \\ { - \alpha q + \gamma _ { 1 , q } } \end{array} \right] } \quad { \mathrm { i n ~ } } \Delta _ { 1 }
$$

with $\alpha > 1$ and $0 < \beta < 1$ .Thus, $\mathbf { T }$ expands the square uniformly in the horizontal direction and contracts it along the vertical.

The problem is now to unravel the structure of the set of orbits that remain in $R$ for all positive and negative iterations of T. Let $\mathbf { x } = ( p , q )$ and $( \mathbf { x } _ { n } , - \infty < n < \infty )$ ）be such an orbit. For ${ \bf x } _ { n + 1 } = { \bf T } { \bf x } _ { n }$ to be in $R$ ,it is necessary that each $\mathbf { X } _ { n }$ falls either in $\Delta _ { 0 }$ or in $\Delta _ { 1 }$ .Since $\Delta _ { 0 }$ and $\Delta _ { 1 }$ have no points in common, ${ \bf { X } } _ { n }$ cannot be in both. Hence, there exists a unique index $i _ { n }$ (one or zero) such that $\mathbf { x } _ { n } \in \Delta _ { i _ { n } }$ .Proceeding in the same way for each n, we can associate a sequence $\left\{ i _ { n } \right\}$ of zeros and ones to each orbit, which remains in $R$ for all $n$ The sequence $\left\{ i _ { n } \right\}$ is called the symbolic description of the orbit. We consider the sequence $\left\{ i _ { n } \right\}$ as a function of $\mathbf { x } _ { 0 } , \{ i _ { n } ( \mathbf { x } _ { 0 } ) \}$ ,also denoted by the (infinite) vector $\mathbf { i } ( \mathbf { x } _ { 0 } )$ ,the symbolic orbit. Evidently the orbit and its symbolic description are related by the shift

$$
i _ { n } ( \mathbf { T x } _ { 0 } ) = i _ { n + 1 } ( \mathbf { x } _ { 0 } ) .
$$

Can we invert the process; that is, is an orbit uniquely defined by its

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0001_pages_0001-0070/auto/images/124a99f4bddade26e86256697cb3431ea791d724d701a23a512700a84db3e769.jpg)  
Fig(3.8) (a) Smale's horseshoe map (3.9) linearly stretches the unit square and folds It back onto itself in imitation of homoclinic motion. (b) The images of the vertical strips $\Delta _ { 0 }$ and $\Delta _ { 1 }$ are horizontal strips.


<!-- chunk 0002: pages 71-140 -->
symbol sequence? Can we associate an orbit to any arbitrary symbolic orbit? To settle these questions,we start by studying finite symbol sequences. Given the sequence $i _ { 0 } , \ldots , i _ { n - 1 }$ of zeros and ones, we define $\Delta _ { i _ { 0 } \dots , i _ { n - 1 } }$ to be the set of all points that start out in $\Delta _ { i _ { 0 } }$ , then proceed to $\Delta _ { i _ { 1 } }$ and so on to $\Delta _ { i _ { n - 1 } } .$ Using the fact that T expands horizontal separations by a factor $\alpha$ ,we deduce that $\Delta _ { i _ { 0 } \dots , i _ { n - 1 } }$ is a rectangle with unit height and width $\alpha ^ { - n }$ . Analogouslythe set of pointssuchthat $T ^ { J } \mathbf { X } _ { 0 } \in \Delta _ { i _ { j } }$ for $- n \leq j \leq - 1$ is $T ^ { n } \Delta _ { i _ { - n } \dots i _ { - 1 } } .$ Thisisanotersetofectanglesofunitlengthandheight $\beta ^ { n }$ Each horizontal and vertical rectangle intersects in a litle rectangle of height $\beta ^ { n }$ and width $\alpha ^ { - n }$ ,containing all the points for which $T ^ { j } \mathbf { x } _ { 0 } \in \Delta _ { i _ { j } }$ for $- n \leq j \leq { \underline { { n } } } - 1 .$

Figurd3.9jdisplays $\Delta _ { i _ { 0 } , i _ { 1 } }$ and $\Delta _ { i _ { - 2 } , i _ { - 1 } } .$ In the limit $n  \infty$ there results a sequence of inscribed rectangles,the sides of which tend to zero for any sequence i. Let the unique limiting point be $\mathbf { x } _ { 0 }$ ; it has the property that $T _ { j } \mathbf { X } _ { 0 } \in \Delta _ { i _ { j } }$ for allj,and no other point has this property.In short,we obtaina one-to-one correspondence between orbits and symbolic orbits.

The set of points contained in al te strips $\Delta _ { i _ { 0 } , \dots , i _ { n } }$ as $n \to \infty$ is an example of a Cantor set,also the case of the set $\Delta _ { i _ { - n } , \dots , i _ { - 1 } }$ Cantor sets are discussed within the general category of fractals in Mandelbrot (1982). Let

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/d1638b5bdeaf026588804bb11d1b4ea7a8f4058229b4cd8a896b02c660dcdd3f.jpg)  
Fig3.9.)The intersections of $\Delta _ { i _ { 0 } , i _ { 1 } }$ and $\Delta _ { i - 2 , i - 1 }$ are the sixteen black rectangles.

A be the set of all the points that never leave R; then the present and the future(io,i,..)ofthe orbit of xeAdetermine itsqoordinate,whereas its past is given by the coordinate $p _ { \cdot }$

The unique correspondence between orbits and sequences of symbols permits us to infer the existence of orbits with definite types of recurrence, from the existence of sequences with the same property. For instance,a periodic orbit will be characterized by a periodic sequence of symbols. Therefore, $\Lambda$ contains an infinite number of periodic orbits, corresponding to all the periodic symbolic orbits. In fact, it is easy to see that periodic orbits are dense in $\Lambda$ :Take $\mathbf { x } _ { 0 } \in \Lambda$ and let i be its symbolic orbit. We then definei as the periodic sequence that coincides with i between the iterations $- \boldsymbol { n }$ and $n + 1$ .This sequence corresponds to the periodic point $\mathbf { x } _ { 0 } ^ { \prime }$ ,which lies in the same rectangle of sides $\alpha ^ { - n }$ and $\beta ^ { n }$ as $\mathbf { x } _ { 0 }$ ,since they have the same symbolic sequence between $- \boldsymbol { n }$ and $n + 1$ .Choosing n arbitrarily large, we bring $\mathbf { x } _ { 0 } ^ { \prime }$ arbitrarily close to $\mathbf { x _ { 0 } }$ ·

There are ‘well-behaved’ orbits in $\Lambda$ ,but we also find chaotic motion. In particular, an orbit whose symbolic sequence contains all the finite sequences of zeros and ones comes arbitrarily close to all the points in A. In other words, there exist dense orbits in $\Lambda$

The motivation for the study of Smale's horseshoe was its resemblance to high powers of the Poincare map in the neighbourhood of homoclinic points.This analogy is made rigorous by the Smale-Birkhoff homoclinic theorem (proved in Guckenheimer and Holmes, 1983): Let T be a diffeomorpism,sch tht $\mathbf { x } _ { e }$ is a hyperbolic fixed point and there exists a point $\mathbf { x } \neq \mathbf { x } _ { \mathrm { e } }$ of transverse intersection of the separatrices $W ^ { + } ( { \bf x } _ { \mathrm { e } } )$ with $W ^ { - } ( \mathbf { x } _ { e } )$ .Then $\mathbf { T }$ has a ‘hyperbolic invariant set’ $\Lambda$ ,on which $\mathbf { T }$ is topologically equivalent to a general shift on a symbolic orbit.

Two points should be explained about this theorem. The first is that it establishes the existence of a unique correspondence between the orbit in the invariant set $\Lambda$ and a sequence of symbols., but this sequence can be more complex than the binary sequence in Smale's horsehoe; that is, there may be more ‘rectangles' $\Delta _ { j }$ than in this simple example. However, there must be points in each rectangle $\Delta _ { j }$ that map intoevery oneofthe rectangles $\Delta _ { j } ^ { \prime }$ The general shift equation is still given by (3.10).

It is also necessary to define what is meant bya‘hyperbolic' invariant set. We have already encountered hyperbolic motion in the case of the cat map (section 1.4). For a nonlinear map we define this property in terms of DT, the derivative map introduced in section 2.1. Thus, a set A is called hyperbolic if we can decompose the tangent space of each point x in A into subspaces $E _ { x }$ such that

where $C > 0$ and $0 < \gamma < 1 .$ In other words,for each point $\mathbf { x }$ in $\Lambda$ there exists a plane $E _ { \mathrm { x } } ^ { - }$ along which points infinitesimally close to $\mathbf { x }$ approach the orbit of $\mathbf { x }$ exponentially as $n  \infty$ , and another plane $E _ { \mathrm { x } } ^ { + }$ where the points approach the orbit of $\mathbf { x }$ as $n  - \infty$

It should be noted that,in the definition of hyperbolic set,thedecomposition of $E ^ { \pm }$ is not presumed for the ‘ambient space’ surrounding $\Lambda$ ， though in the simple case of the cat map, $\Lambda$ is the entire torus. The stable manifold theorem (section 2.2) can be generalized to hyperbolic sets;that is, there exist invariant manifolds $W _ { \mathbf { x } } ^ { \pm }$ ,tangent to $E _ { \mathrm { x } } ^ { \pm }$ ,whose points tend to the image $\mathbf { T } ^ { n } \mathbf { X } \in { \Lambda }$ as $n  \mp \infty$ .Ofcourse,any periodic point in $\Lambda$ is necessarily hyperbolic.

The immediate consequence of the Smale-Birkhoff theorem is that transverse homoclinic points lead to dense orbits and an infinite number of unstable periodic orbits, just as in the case of Smale's horseshoe. Horseshoe-type constructions have in fact been one of the main methods of establishing the existence of chaotic motion in dynamical systems. In particular,Devaney (1979) uses them to establish generic spiralling chaos in the neighbourhood of Hamiltonian equilibria with complex eigenvalues. The demonstration of Sitnikov's theorem for the three-body problem can also rely on the same method, as in Moser (1973). It must be pointed out, however, that horseshoes provide nonconstructive information. The calculation of the periodic orbits in $\Lambda$ must rely on other methods,such as the one presented in chapter 4.

As we noted in section 3.1, homoclinic bifurcations also occur in dissipative systems. In their case the orbits converge on an attractor with smaller dimensionality than the phase space. This attractor is an invariant set; its coincidence with the hyperbolic set $\Lambda$ is known as a strange attractor, discussed in Guckenheimer and Holmes (1983).

# 3.4 Measure and ergodicity

The goal of providing a complete qualitative description of generic dynamical systems is far from being achieved. It is therefore important to try to determine the main properties of ‘almost all orbits' of a system. We adopt, then, a probabilistic point of view, which neglects ‘exceptional trajectories' in favour of the ‘typical’ ones. To give a precise meaning to these vague concepts,we must fall back on the concept of measure.Abstract mathematical definitions of measure veil our familiarity with this term in the context of probability densities: If the (positive) probability density in a Euclidean space $\textstyle { \mathbb { R } } ^ { n }$ is $f ( \mathbf { x } )$ ,then the probability measure in a region $_ D$ is

$$
\mu ( D ) = \int _ { D } d \mu = \int _ { D } d \mathbf { x } f ( \mathbf { x } ) .
$$

General measures are also defined by a positive density function, which does not have to be normalized to unity. Where a measure is defined on a set of discrete points,it is the sum of the measures for each point,in the same way as a probability.

An invariant measure for a map $\mathbf { T }$ is a measure with the property

$$
\mu ( \mathbf { T } ( A ) ) = \mu ( A )
$$

for any set A. In sections 1.3 and 1.4 we used the same notation for the area of a region of the torus. This was justified, since the area itself was an invariant of the maps studied there. We also know that phase space volume is preserved by Hamiltonian flows; hence, the invariant measure for these systems will be the volume. The $N$ -dimensional volume in $\mathbb { R } ^ { N }$ is known as the Lebesgue measure. If we focus on a single energy shell $H ( \mathbf { x } )$ $= E$ ,however,the preservation of volume on the whole phase space entails that the invariant measure corresponding to an element of area $d \sigma$ is the Liouville measure

$$
d \mu = d \sigma / ( \nabla \mathbf { H } \cdot \nabla \mathbf { H } ) ^ { 1 / 2 } = \delta ( E - H ( \mathbf { x } ) ) d \mathbf { x } .
$$

Integrating over the shell of energy $E$ and volume $V$ we obtain the total measure $\mu ( E ) = d V / d E$ Other examples of invariant measure are() $\begin{array} { r } { \mathbb { 1 } ) \mu ( \mathbf { x } _ { j } ) = } \end{array}$ $1 / n$ , in the case where the $\mathbf { x } _ { j }$ form an $n$ -fold periodic orbit; (2) $T ( x ) = 2 x$ (mod 1) in the interval $( 0 , 1 )$ ,which preserves the Lebesgue measure,though it is not a one-to-one mapping.

A fundamental result of the theory of invariant measures is the Poincareé recurrence theorem: Given a map T with an invariant probability measure μ and a measurable set A,if we define the set A。 = {xEA: Tx eventually leave $A$ permanently}, then $\mu ( A _ { 0 } ) = 0$

Following Lanford (1983), we demonstrate this theorem by defining the set $D _ { n }$ of points whose image $I ^ { \prime \prime } \mathbf { x } \in A$ ,while $T ^ { j } \mathbf { x } \notin A$ for $j > n$ .Note that no requirement is made that x itself belong to A in this definition. Evidently the intersections D Dm=(the empty set) ifn ≠m.We also find that x is in $D _ { n }$ if and only if $1 ^ { n } \mathbf { x }$ is in $D _ { 0 }$ ,that is, $D _ { n } = T ^ { - n } D _ { 0 }$ ,which implies that

$$
\mu ( D _ { n } ) = \mu ( D _ { 0 } )
$$

for all $n$ . Therefore, the measure of the union of sets

$$
\mu ( D _ { 0 } \cup \cdots \cup D _ { n - 1 } ) = n \mu ( D _ { 0 } ) \leq 1 ,
$$

so that $\mu ( D _ { 0 } ) = 0$ ,since $n$ can be made arbitrarily large, and

$$
\mu { \binom { \infty } { n = 0 } } D _ { n } ) = 0 .
$$

The set $A _ { 0 }$ in the theorem is a subset of this union set

$$
A _ { 0 } = A \cap { \binom { \infty } { n = 0 } } D _ { n } \quad \quad
$$

Therefore, $\mu ( A _ { 0 } ) = 0$ .This theorem is also valid for a continuous flow.

A point $\mathbf { x }$ is a wandering point of the map T if there is a neighbourhood $U$ of $\mathbf { x }$ and a number $N$ for which $( \mathbf { T } ^ { n } U ) \cap U = \emptyset$ for all $n > N$ otherwise, $\mathbf { x }$ is called a nonwandering point.IfTis defined ina limited region of phase space or a compact manifold,the orbit of a wandering point must accumulate on the set of nonwandering points.Otherwise, the neighbourhoods of every point of the orbit, to which it cannot return, would eventually fill all the available phase space. It follows that the wandering points form an open set. Consider the union of these neighbourhoods $U$ for all the wandering points.By the recurrence theorem, the measure of this set is zero,and hence the measure of the set of wandering points is also zero. In the case of a Hamiltonian system in which $H ( \mathbf { x } ) < \mathbf { E }$ is a region with finite volume, the invariant measure is the volume itself. The set of wandering points is open and has zero volume; it is therefore empty. We conclude that in a Hamiltonian system with bounded motion all points are nonwandering.

We can consider now a function $f ( \mathbf { x } )$ defined on a region of phase space with an invariant measure $\mu$ Foralmost all points,thatis,with the exceion of points forming a set of zero measure,the orbit will return again and again to the neighbourhoods already visited. If the intervals between these visits are not too erratic, we expect to be able to define the time average,

$$
{ \overline { { f } } } ( \mathbf { x } ) = N ^ { - 1 } \operatorname* { l i m } _ { N  \infty } \sum _ { n = 0 } ^ { N - 1 } f ( \mathbf { T } ^ { n } \mathbf { x } ) .
$$

This is the main content of Birkhoff's local ergodic theorem,that is,the limit in (3.18) exists if $f ( \mathbf { x } )$ is measurable:

$$
\int | f | d \mu < \infty .
$$

This theorem also guarantees that $\overline { { f } } ( \mathbf { T x } ) = \overline { { f } } ( \mathbf { x } )$ and that

$$
\int { \overline { { f } } } ( \mathbf { x } ) d \mu = \int f ( \mathbf { x } ) d \mu \equiv \langle f ( \mathbf { x } ) \rangle .
$$

Note that no guarantee is given that a given time average equals the ensemble average on the right side of (3.2O). This willcertainly not be the case for most periodic orbits, the time average of which is just the average over a single period. The fact that the set of points for which $\bar { f } ( \mathbf { x } )$ may not exist has zero measure is a strong restriction on bounded Hamiltonian systems.For dissipative systems,μ>Oonly on atractors,outside of which no time average can be defined. Birkhoff's local ergodic theorem also holds for systems with continuous time. A proof is given in Billingsley (1965).

We have seen that in chaotic systems there are dense orbits. It is plausible that for one of these the coincidence of averages,

$$
{ \overline { { f } } } ( \mathbf { x } ) = \langle f ( \mathbf { x } ) \rangle ,
$$

will be verified.This is the motivation for the definition of ergodic system as one for which (3.21) holds for almost all orbits, for any measurable function $f$

# Exercise

Show that periodic orbits have zero measure in ergodic systems.

An important consequence of this definition is that it excludes any possibility of there existing two or more disjoint sets with positive measure in an ergodic system. For if two such sets $\mathbf { T } M _ { 1 } = M _ { 1 }$ and $\mathbf { T } M _ { 2 } = M _ { 2 }$ ， existed, we od eine thefuio

$$
f ( \mathbf { x } ) = \left\{ { \begin{array} { l l } { 1 \qquad ( \mathbf { x } \in M _ { 1 } ) } \\ { 0 \qquad ( \mathbf { x } \in M _ { 2 } ) } \end{array} } \right.
$$

witha time average that evidently depends on x.Conversely,the system can always be decomposed if it is not ergodic. This follows from the fact that f(x) will not then be a constant for almost allx. So we can find a suitable value a for which both the sets M1 ={x:f(x)<a} and M2= {x:f(x)>a} have finite measure. According to Birkhoff's theorem the time average is invariant with respect to $\mathbf { T }$ so $M _ { 1 }$ and $M _ { 2 }$ are disjoint invariant sets with finite measure. Thus, a system is ergodic if and only if it cannot be decomposed; that is,any invariant set must have zero or unit (normalized) measure. Furthermore, an invariant measurable function (f(Tx)=f(x)) must be a constant for almost all $\mathbf { x }$

# Exercise

Show that a Hamiltonian system is never globally ergodic.What is refered to as anergodic system inthiscaseis theflow on theenergy shell with the Liouville measure (3.13).

Another fundamental concept for the study of chaotic motion is that of ‘mixing'. As motivation we take the classic example in Arnold and Avez (1968)-a glass containing 20 percent rum and 80 percent Coca Cola (fig.3.10))If theyare separated so that theregion $A$ is the region originally oceupied by the rum and $B$ is any region in the glass,after mixing n times the percentage of rum in $B$ should be roughly

$$
1 0 0 \mu ( \mathbf { T } ^ { n } A \cap B ) / \mu ( B ) \simeq 1 0 0 \mu ( A )
$$

if $\mu$ is normalized. In other words, we expect that each part of the glass will contain 20 percent of rum as $n  \infty$ .We therefore define a system to be mixing if

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \mathbf { T } ^ { n } A \cap B ) = \mu ( A ) \mu ( B )
$$

for any pair of measurable sets $A$ and $B$

The property of mixing implies ergodicity. To show this we choose an invariant measurable set $A$ ：

$$
\mathbf { T } ^ { n } A \cap A = A
$$

and the set $B = A$ Then (3.24) reduces to

$$
\mu ( A ) = ( \mu ( A ) ) ^ { 2 } ,
$$

wherefore $\mu ( A ) = 0$ or 1.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/682805fc0ca48a7a0b2f57c4faa7b8e54ee3147246ec30977281f9965f8c0332.jpg)  
Fig.(3.10.)Mixing $20 \%$ of rum into $80 \%$ of Coca Cola, there should be an equal proportion of rum in any region $B$ of the glass.

Any region A will be distorted into a very long thin strip, winding helicoidally around the torus, by successive iterations of Arnold's cat map. This system is mixing and therefore it is also ergodic.As for the translations of the torus studied in section 1.3, they do not deform a region A. The intersections of $\mathbf { T } ^ { n } A$ with a region $B$ will alternate for all $n$ between being empty,or having positive measure. This is an example of an ergodic system that is not mixing.

# 3.5 Entropy

A fundamental characteristic of chaotic motion is that any initial uncertainty about the system's position in phase space increases rapidly with time. Another way to put it is that successive approximate measurements of the system's position supply more information in a chaotic system than in a more ‘predictable' system. The concept of metric entropy introduced by Kolmogorov turns this into a rigorous idea.

Let us make a partition $\alpha$ of phase space into $N$ disjoint regions $A _ { i }$ ,so that the probability of finding the system in any one of them is $\mu ( A _ { i } ) = \mu _ { i }$ .We then define the entropy of the partition $\alpha$ to be

$$
h ( \alpha ) = - \sum _ { i = 1 } ^ { N } \mu _ { i } \log \mu _ { i } .
$$

The partitions into $N$ regions with the maximum entropy are the ones for which $\mu _ { i } = 1 / N$ for all i: $h = \log N .$ This follows from the fact that the function $\phi ( x ) = - x \log x$ (fig.3.11)is_convex in the interval [0,1]. Therefore,

$$
\phi \biggl ( N ^ { - 1 } \sum _ { j = 1 } ^ { N } x _ { j } \biggr ) \geq N ^ { - 1 } \sum _ { j = 1 } ^ { N } \phi ( x _ { j } )
$$

and hence

$$
h ( \alpha ) = \textstyle \sum \phi ( \mu _ { i } ) \le N \phi ( N ^ { - 1 } \textstyle \sum \mu _ { i } ) = N \phi ( N ^ { - 1 } ) = \log N .
$$

Thetrivialpartition,whereoneoftheegonshasunitmeasue,istheoly one with zero entropy.

The probability of finding the system in a region $A _ { i }$ of the partition $\alpha$ may or may not be independent of the probability of finding it in the region Bj of the partition β. For example,a mixing system that was in B, to start with willcertainly be in T"B,- scattered throughout phase space after a large number n of iterations.In this case the probabilities of the partitions β and α = lim T"β,for n → o,are independent. The combined partition into the regions $A _ { i } \cap B _ { j }$ with probabilities $\mu _ { i j } = \mu ( A _ { i } \cap B _ { j } )$ is denoted $\alpha \lor \beta$ If $\propto$ and $\beta$ are independent, $\mu _ { i j } = \mu _ { i } \mu _ { j } .$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/a0956d75a1b486e5973b8e88126bc03f7f33ea8f82ef02bb2eac98e35d732555.jpg)  
Fig. $\textcircled{3 . 1 1 }$ The convexity of $\phi ( x ) = - x \log x$ is fundamental for the proof of important properties of the metric entropy.

# Exercise

Show that,if $\alpha$ and $\beta$ are independent, the entropy of the combined partition is

$$
h ( \alpha \vee \beta ) = h ( \alpha ) + h ( \beta ) .
$$

When $\alpha$ and $\beta$ are not independent, we define the conditional probability of finding the system in $A _ { i } ,$ given that it is in $B _ { j }$ ,as

$$
\mu _ { i / j } = \mu _ { i j } / \mu _ { j } .
$$

The combined entropy then becomes

$$
\begin{array} { l } { { \displaystyle h ( \alpha \vee \beta ) = - \sum _ { i j } \mu _ { j } \mu _ { i / j } ( \log \mu _ { j } + \log \mu _ { i / j } ) } } \\ { { \displaystyle \qquad = - \sum _ { j } \mu _ { j } \log \mu _ { j } \sum _ { i } \mu _ { i / j } - \sum _ { j } \mu _ { j } \sum _ { i } \mu _ { i / j } \log \mu _ { i / j } } } \end{array}
$$

Defining the conditional entropy of $\alpha$ relative to $B _ { j }$ as

$$
h ( \alpha / B _ { j } ) = - \sum _ { i } \mu _ { i / j } \log \mu _ { i / j } \qquad .
$$

and the conditional entropy of a relative to the partition $\beta$ as the mean value

for $h ( \alpha / B _ { j } )$

$$
h ( \alpha / \beta ) = \sum _ { j } \mu _ { j } h ( \alpha / B _ { j } ) ,
$$

we obtain

$$
h ( \alpha \vee \beta ) = h ( \beta ) + h ( \alpha / \beta ) .
$$

# Exercise

Use the convexity of the function in fig. 3.11 to prove that

$$
h ( \alpha / \beta ) \leq h ( \alpha ) .
$$

We can now return to the question of incomplete information about the system and its evolution.If a measurement localizes the system in one of the regions $A _ { j }$ , we reduce the uncertainty concerning its localization. The information produced by the measurement consists of the removal of uncertainty that preceded this event. The larger the uncertainty, the greater will be the amount of information obtained by its removal. The entropy of a partition $\alpha$ has been shown to have properties that permit us to consider it as a measure of the uncertainty of $\alpha$ We can therefore define the quantity of information obtained by localizing the system in one of the regions $A _ { j }$ as $h ( \alpha )$

If we make a measurement on $\alpha$ ,having already ascertained the $B _ { j }$ into which the system belongs in the partition $\beta$ ，the average increase of information will be $h ( \alpha / \beta )$ This additional information is a maximum if $\alpha$ and $\beta$ are independent -in this case a measurement of $\beta$ in no way reduces the uncertainty of $\alpha$ Though we have found that the present definition of entropy has desirable properties,it may stillappear somewhat arbitrary. However,it is shown in Khinchin(1957) that this is the onlydefinition that satisfies conditions (3.29) and (3.35).

We focus on the sequence of partitions $\mathbf { T } ^ { n } \alpha$ It is demonstrated in Arnold and Avez (1968) that the limit

$$
h ( \alpha , \mathbf { T } ) \equiv \operatorname* { l i m } _ { n  \infty } { \frac { h ( \alpha \vee \mathbf { T } \alpha \vee \cdots \vee \mathbf { T } ^ { n - 1 } \alpha ) } { n } }
$$

exists.We call $h ( \alpha , \mathbf { T } )$ the entropy of $\alpha$ relative to $\mathbf { T }$ .Finally we define the metric entropy of the map $\mathbf { T }$ as

$$
h ( \mathbf { T } ) \equiv \operatorname* { s u p } h ( \alpha , \mathbf { T } ) ,
$$

where the supremum extends over al measurable partions. Evidently we always have $h ( \mathbf { T } ) \geq 0$

# Exercise

Prove that the metric entropy is invariant with respect to acoordinate transformation $\mathbf { x } ^ { \prime } = \mathbf { F } ( \mathbf { x } )$ ,that is, $h ( \mathbf { T } ) = h ( \mathbf { F } { \boldsymbol { \cdot } } \mathbf { T } { \boldsymbol { \cdot } } \mathbf { F } ^ { - 1 } )$ ：

It is not usuall feasible to compute the metric entropy of a dynamical system directly from its definition.Yet it is worthwhile to try to gain a feeling for the process involved. Each iteration leads to a new combined partition, which results from the addition of the boundaries of the regions $\mathbf { T } ^ { n } A _ { j }$ to the boundaries of all the previous partitions. For example, if the original partition divided phase space into $2 N$ regions of equal measure and each iteration of the map led to a new partition that cut each region in half, then $h ( \alpha \vee \cdots \vee \mathbf { T } ^ { n - 1 } \alpha ) = n \log 2 + \log N ,$ so $h ( \alpha , T ) = \log 2$ This example shows that positive entropy requires exponential growth, with $n$ ,of the number of regions in $\alpha \lor \cdots \lor \mathbf { T } ^ { n - 1 } \alpha$ But it must be remembered that the number of regions in $\mathbf { T } ^ { n } \alpha$ is the same as that in $\alpha$ , so an exponential growth of the combined partition demands an exponential growth of the boundary of the regions $\mathbf { T } ^ { n } A _ { j } .$ Only thus can the boundaries of $\mathbf { T } ^ { n } \alpha$ cut a constant proportion of the ever diminishing regions $\alpha \lor \cdots \lor \mathbf { T } ^ { n - 1 } \alpha .$ This does not occur for the translations of the torus studied in section 1.3. The length of the boundary of any region $\mathbf { T } ^ { n } A _ { j }$ is constant; hence,the etropy $h ( \alpha , \mathbf { T } )$ is zero for any partition $\alpha$ ,even though this system is ergodic.

For the cat map we do have exponential stretching of the boundaries of each region along the direction of the eigenvector $\xi _ { 1 }$ corresponding to the eigenvalue $\lambda _ { 1 }$ .If each region were collapsed back on itself as was the case with the horseshoe (but fitting exactly,as the full cat map itself), each region would be divided into $\lambda _ { 1 }$ equal regions. The result would be that

$$
h ( \mathbf { T } ) = \log \lambda _ { 1 } .
$$

This is the correct result,proved by inai (1959),which implies that the existence of many extra regions (due to the boundaries not fiting properly) is counterbalanced by the fact that the entropy is actually smaller than the maximum $\log N$ .This result can be generalized to $r$ dimensional tori: if a linear map T of the torus has $r$ real and distinct eigenvalues, then

$$
h ( \mathbf { T } ) = \sum _ { | \lambda _ { i } | > 1 } 1 0 \mathbf { g } | \lambda _ { i } | .
$$

It is usually very difficult to verify whether the properties of ergodicity, mixing and positive entropy hold for a given Hamiltonian system.The first systems for which this has been achieved are billiards, that is，the free motion of a particle in the plane within a given boundary. Usually one considers that the particle undergoes specular reflectioh at the boundary, but in Sinai's billiard shown in fig 3.12a ghis is true only for encounters with the circular barrier. The boundary conditions along the square are taken to be periodic, so that the billiard in fact has the topology of a torus. The periodic representation of the torus is shown in fig3.12b.This system was proved by Sinai (197o) to have all the chaotic properties, including positive entropy. Another system proved to be chaotic by Buminovitch (1974) is the stadium: the interior ofa pair of semicircles joined by two straight segments.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/e47b5cc403b311993c014cfd56100c283f6fd131737bef3610c8951a80b0b726.jpg)  
Fig3.12.InSinai'sbiliardtheparticeundergoesspecularreflectionatthecircular barrier,while the boundary conditions on the square are periodic. Thus, the square in (a) is in fact a torus with the perhodic representation depicted in (b).

The concept of entropy permits us to quantify the decay of information brought about by the entire flow of the system. Yet the loss of memory about approximate initial conditions is a local property of chaotic motion. Let us consider a small ball of radius $\varepsilon ( 0 )$ centred on the initial position of some orbit in phase space. The successive images of the ball will be distorted under the map T. In the limit $\varepsilon ( 0 ) \to 0$ , we can use the linearized map DT, so that the ball develops into a small ellipsoid. Naming the principal axes of the ellipsoid as $\varepsilon _ { i } ( n )$ ,we define the Lyapunou exponents as

$$
\gamma _ { i } = \operatorname* { l i m } _ { \varepsilon ( 0 ) \to 0 } \operatorname* { l i m } _ { n \to \infty } \frac { 1 } { n } \log \frac { \varepsilon _ { i } ( n ) } { \varepsilon ( 0 ) } .
$$

# Exercise

Define the Lyapunov exponents in terms of the tangent space vectors introduced in chapter 2.

For a periodic orbit of period $r$ ,theabovelimitevidentlyexistsandthe $\gamma _ { i }$ are just the eigenvalues of $\mathcal { M } ^ { r } = D \mathbf { T } ^ { r }$ .Where periodic orbitsare dense,we therefore expect that most orbits will have Lyapunov exponents. This is indeed the content of a theorem of Oseledec (1968), which holds under very general conditions. Furthermore, for a hyperbolic set with dense orbits, almost all orbits will share the same Lyapunov exponents. The largest positive exponent measures the rate of divergence between neighbouring orbits,whereas negative exponents measure convergence rates along stable manifolds. For a Hamiltonian system $\textstyle \sum \gamma _ { i } = 1$ ，whereas $\sum \gamma _ { i } < 1$ for dissipative systems.

It was shown in the preceding section that the metric entropy wil be positive only if the frontiers of a typical region grow exponentially with time. The possibility of choosing such a region as the small ball used to define the Lyapunov exponent suggests that positive entropy is connected to positive Lyapunov exponents. In the case of linear maps of the torus we simply have $\gamma _ { i } = \ln | \lambda _ { i } |$ ,so equation (3.40) becomes

$$
h ( \mathbf { T } ) = \sum _ { \gamma _ { i } > 1 } \gamma _ { i } .
$$

Pesin(1977) has indeed shown that (3.42) can be generalized for a single region of connected chaotic motion. If there is more than one region (separated by invariant curves or manifolds), the generalization is

$$
h ( { \bf T } ) = \int d \mu \sum _ { \gamma _ { i } > 1 } \gamma _ { i } ( { \bf x } ) .
$$

This connection between the Lyapunov exponents and the metric entropy is of great practical importance, since the latter are much easier to compute. Lichtenberg and Lieberman (1983, chap. 5) present a detailed discussion of this subject and provide many references.

# 3.6 The principle of uniformity

Hyperbolic sets are characterized by dense orbits and by a dense population of periodic orbits. The ergodic theory,briefly outlined in the two preceding sections, relies on the former and neglects the latter. Yet a dense orbit mimics every periodic orbit of the system arbitrarily closely for many periods, so it should be possible to replace the time average over a ‘typical orbit' by an average over all the periodic orbits. Clearly the chaotic orbit will remain close to very unstable periodic orbits for a shorter time than the relatively stable ones. It follows that the mean over periodic orbits must be a weighted average.

The principle of uniform density of periodic orbits is most easily presented in the case of an area-preserving map in a region of area A,as in the appendix of Hannay and Ozorio de Almeida (1984). Let us consider a peaked function δ(x),centred on the origin but normalized to unity for all ε, so that for ε→O it becomes a two-dimensional Dirac δ function. Then δ(xn- xo) is a function of xo defined throughout the area A, which has peaks in al the regions where orbits return very close to their starting positions after precisely $n$ iterations. Another function of $\mathbf { x } _ { 0 }$ that we can construct is

$$
\Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) ,
$$

peaked in all the regions with orbits that return to a small neighbourhood of $\mathbf { x } _ { 0 }$ for some iteration $n \geq N$

One of the consequences of the Poincaré recurrence theorem discussed in section 3.4 is that all points of an area-preserving map are nonwandering; that is, the image of any neighbourhood $U$ of $x _ { 0 }$ will eventually intersect $U$ 。 If we take this neighbourhood to be the area ε around $\mathbf { x } _ { 0 }$ ,we see that there will be a peak of $\Delta _ { \varepsilon , N }$ in the neighbourhood of any point $\mathbf { x } _ { 0 }$ in the limit $N  \infty$ . This uniform distribution of peaks will make $\Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } )$ a smooth function over $A$ . In fact,we can estimate when this will happen: Defining $\nu ( N )$ to be the number of periodic points with period equal to or smaller than $N$ ,the number of peaks in $\Delta _ { \varepsilon , N }$ will be equal to or greater than $\nu ( N )$ (equality being obtained in the limit $\varepsilon \to 0$ ). The smoothing of $\Delta _ { \scriptscriptstyle \varepsilon , N }$ will then occur when

$$
\varepsilon \nu ( N ) \gg A .
$$

For an ergodic system we can readily calculate this smooth limit,since

$$
\operatorname* { l i m } _ { N \to \infty } \Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \operatorname* { l i m } _ { N \to \infty } \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) = \overline { { \delta } } _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } ) _ { \mathbf { x } _ { 0 } = \mathbf { x } } .
$$

It is importanttonotethatthetimeaverageontherightsideisnowtaken over a function of $\mathbf { x } _ { 0 }$ ,centred on the immobile point $\mathbf { x }$ .The limit exists for almost all xo and in particular for Xo = x. The ergodic property then becomes

$$
\operatorname* { l i m } _ { N  \infty } \Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \langle \delta _ { \varepsilon } ( \mathbf { x } _ { 0 } - \mathbf { x } ) \rangle = A ^ { - 1 } .
$$

The principle of uniformity can now be stated as the conjecture that we can take the limit ε→0 on the left side of (3.47) before the N→oo limit. In practice this means that we can make the & neighbourhoods sufficiently

small so as to be able to neglect the contribution of nonperiodic orbits to $\Delta _ { \scriptscriptstyle \varepsilon , N }$ , while making $\nu ( N )$ large enough for(3.45)to be valid.Inconclusion

$$
\operatorname* { l i m } _ { N  \infty } \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) = \frac { 1 } { A }
$$

is a sum over periodic orbits,though the equation makes sense only for arbitrarilysmall smoothing of the $\delta$ functions.Integrating both sides of (3.48) over $\mathbf { x } _ { 0 }$ ,we obtain the sum rule over periodic points,

$$
\operatorname* { l i m } _ { N \to \infty } N ^ { - 1 } \sum _ { n = 1 } ^ { N } \sum _ { j = 1 } ^ { \nu ( n ) - \nu ( n - 1 ) } | \operatorname* { d e t } ( \mathcal { M } _ { j } ^ { n } - 1 ) | ^ { - 1 } \to 1 .
$$

The weight ofa periodic point is given by a factor that appeared in(2.23). It depends on the stability matrix $\mathcal { M }$ introduced in section 2.3 and is unbounded as the linearized map $D \mathbf { T } ^ { n }$ approaches the unit map.

For a fully chaotic system with positive entropy $h ( \mathbf { T } )$ the weight of an orbit of very high period wil have the limit

$$
| \mathrm { d e t } ( \mathcal { M } _ { j } ^ { n } - 1 ) | ^ { - 1 } \xrightarrow [ n \to \infty ] { } | ( e ^ { n \gamma } - 1 ) ( e ^ { - n \gamma } - 1 ) | ^ { - 1 } \xrightarrow [ n \to \infty ] { } e ^ { - n \gamma } = \mathrm { e x p } [ - n h (  { \mathbb { T } } ) ] ,
$$

where $\gamma$ is the positive Lyapunov exponent. The contribution of any finite number of orbits to the sum in (3.49) can be neglected, so we can use (3.50) for all the orbits. Since the contribution of each orbit is $n \exp ( - n h )$ we obtain the average number of periodic orbits with period $n$ as

$$
\nu ( n ) - \nu ( n - 1 ) { \longrightarrow } \exp ( n h ) / n .
$$

The above argument is strictly valid only if $n$ is a prime number. Otherwise, we have neglected the repeated contribution of orbits for which $n / m$ is an integer for some integer m. However, taking (3.51) as a first approximation we verify that the number of orbits with period $n / m$ is indeed exponentially smaller than the number with period n. Rigourous results concerning uniformity and exponential proliferation of periodic orbits are presented by Parry and Pollicot (1983) and Parry (1984).

# Exercise

Though the uniformity principle is restricted to ergodic systems, show that Birkhoff's local ergodic theorem can be used to extend the validity of the sum rule (3.49) to systems that are merely recurrent.

The uniformity principle and the sum rule may be applied to the Poincare map ofa Hamiltonian system.It is worthwhile,however,to extend them to the continuous periodic orbits in the flow itself.The first dificulty is that ergodic flow on the energy shell does not preserve area, though it does conserve the Liouville measure (3.13).For this reason we define the shell 8 function $\delta _ { \mu } ( \mathbf { x } )$ by its properties

$$
\delta _ { \mu } ( { \bf x } ) = 0 , \qquad { \bf x } \ne 0
$$

(choosing the origin to lie on the shell) and

$$
\int d \mu \delta _ { \mu } ( { \bf x } ) = 1 .
$$

Just as with the usual Dirac $\delta$ functions,we must understand this to be the limit of peaked functions, but I will leave out explicit reference to the smearing parameter so as not to encumber the notation.

The time average can be written in the form

$$
\bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ) = \operatorname * { l i m } _ { T  \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ) ,
$$

where the sash in the integral sign excludes an arbitrarily small neighbourhood of the origin. Its equivalence to the configurational average

$$
\begin{array} { r } { \langle \delta _ { \mu } ( \mathbf { x } ( 0 ) - \mathbf { x } ) \rangle = \mu ^ { - 1 } = ( d V / d E ) ^ { - 1 } , } \end{array}
$$

for the choice of $\mathbf { x } ( 0 ) = \mathbf { x }$ ,leads to the uniformity in $\mathbf { x } ( 0 )$ of

$$
\operatorname * { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ( 0 ) ) = \mu ^ { - 1 } .
$$

This formula for the uniform distribution of periodic orbits is exactly analogous to the one for maps. The need to exclude a neighbourhood of the origin from the average over time here becomes evident.

The sum rule over periodic orbits is obtained by integrating over the measure $\mu$ of the whole shell:

$$
\operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \int d \mu \delta _ { \mu } ( { \bf x } ( t ) - { \bf x } ( 0 ) ) = 1 .
$$

The configurational integral can be subdivided into integrals in the neighbourhood ofeach periodic orbit.For each of these we can introduce the local coordinate system presented in section 2.5.The shell δ function δμ then takes on the simple form

$$
\delta _ { \mu } ( \theta , P , Q ) = ( d H / d J ) \delta ( \theta , P , Q ) .
$$

Consequently,

$$
\begin{array} { l } { \displaystyle \oint _ { j \mathrm { t h o r b i t } } d t d \mu \delta _ { \mu } ( { \bf x } ( t ) - { \bf x } ( 0 ) ) = \int d t d \theta _ { 0 } d P _ { 0 } d Q _ { 0 } \delta ( \theta _ { 0 } + \omega _ { j } t - ( \theta _ { 0 } + 2 \pi m ) ) } \\ { \displaystyle \qquad \times \delta ( ( P , Q ) _ { t } - ( P , Q ) _ { 0 } ) } \\ { = | \tau _ { j } | | \operatorname* { d e t } \{ \mathcal { M } _ { j } ^ { m } - { \bf 1 } \} | ^ { - 1 } , \qquad ( 3 . 5 } \end{array}
$$

so that the sum rule becomes

$$
\operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \sum _ { | m \tau _ { j } | < T } | \tau _ { j } | | \operatorname* { d e t } \big \{ \mathcal { M } _ { j } ^ { m } - \mathbf { 1 } \big \} | ^ { - 1 } = 1 .
$$

As in the discrete case,it is not necessary to presuppose ergodicity to arriveat this sum rule,though it is essential to theunformity principle(3.56). For a system with positive entropy we can neglect the contribution of multiple repetitions of periodic orbits,just as in the discrete case.For large periods the number of periodic orbits increases exponentially,permitting us to define the weighted density of periodic orbits,

$$
f ( \tau ) = \sum _ { j } | \tau _ { j } | | \operatorname* { d e t } \{ \mathcal { M } _ { j } - \mathbf { 1 } \} | ^ { - 1 } \delta ( \tau - \tau _ { j } ) \underset { \tau  \infty } { \longrightarrow } 1 ,
$$

as can be verified by integrating over t.

In chapter 9, which presents the theory of the quantum energy spectrum in terms of the classical periodic orbits, the factor $| \mathrm { d e t } ( \mathcal { M } ^ { m } - \mathbf { 1 } ) | ^ { - 1 }$ will reappear and (3.61) becomes the basis for an important result concerning correlations of the spectrum.

# Normal forms

Having established the ubiquity of periodic orbits in dynamical systems, we now return to the study of the motion near a given periodic orbit, fixed point or point of equilibrium. The Hartman-Grobman theorem of section 2.2 guarantees the existence of a continuous coordinate transformation that linearizes the vector field near a hyperbolic fixed point, but no indication is given as to how to construct this transformation. The method of normal forms, invented by Poincaré, consists of eliminating nonlinear terms of the vector field by successive polynomial transformations. If this process can be carried out to all orders, the resulting compound transformation can be shown to be convergent in some cases, and an analytic reduction of the nonlinear vector field to a linear one is thus achieved. This transformation can be approximated to arbitrary accuracy.

One of the cases in which this process can never be carried out is that of Hamiltonian systems. The Hamiltonian cannot generally be made quadratic by a canonical transformation, though Birkhoff showed that it can be simplified into a form that shares some of the important features of quadratic Hamiltonians. For hyperbolic points this transformation is analytic in a narrow neighbourhood of the separatrices, allowing us to calculate precisely some homoclinic orbits and the periodic orbit families that accumulate on them.

The elimination of nonlinear terms of low order near stable points in Hamiltonian systems allows a qualitative understanding of the motion in their neighbourhood,even though the transformation cannot be etended to infinite orders.This is important in the case of the bifurcation of stable orbits discussed at the end of this chapter. The nonconvergence of the Birkhoff transformation is due to the intricate nature of the motion in these regions, which is studied in chapters 5 and 6.

# 4.1 General systems

A linear coordinate transformation can take a dynamical system into the form

$$
\dot { \mathbf { x } } = \mathcal { L } \mathbf { x } + \mathbf { g } _ { k } ( \mathbf { x } ) + \mathbf { g } _ { k + 1 } ( \mathbf { x } ) + \cdots
$$

in the neighbourhood of the origin,an equilibrium with $N$ distinct eigenvalues. Here $\mathcal { L }$ is a diagonal matrix with elements $\lambda _ { j } .$ and the components of the vector fields $\mathbf { \boldsymbol { \mathsf { g } } } _ { j }$ are homogeneous polynomials of order $j .$ We seek a nonlinear coordinate transformation

$$
\mathbf { x } = \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ,
$$

the components of $\mathbf { h }$ being homogeneous polynomials of order $\mathbf { k }$ ,that eliminates ${ \bf g } _ { k }$ fromthedyamicalstem.Itroucing(4.2)t(4.)e obtain

$$
\begin{array} { r l } & { \dot { \mathbf { y } } = ( \mathbf { 1 } + \hat { \alpha } \mathbf { h } / \hat { \sigma } \mathbf { y } ) ^ { - 1 } \{ \mathcal { L } ( \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ) + \mathbf { g } _ { k } ( \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ) + \cdots \} } \\ & { \quad = \mathcal { L } \mathbf { y } + \{ \mathcal { L } \mathbf { h } ( \mathbf { y } ) - ( \hat { \sigma } \mathbf { h } / \hat { \sigma } \mathbf { y } ) \mathcal { L } \mathbf { y } + \mathbf { g } _ { k } ( \mathbf { y } ) \} + \cdots , } \end{array}
$$

neglecting all termsof order $\geq k + 1$ . The required polynomials $h _ { j } ( \mathbf { y } )$ thus satisfy the equations

$$
\lambda _ { j } h _ { j } - \sum _ { i } { \frac { \partial h _ { j } } { \partial y _ { i } } } \lambda _ { i } y _ { i } = g _ { k j } ,
$$

The substitution of $h _ { j }$ by any of its monomials $\left( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } \right)$ on the left side of (4.4) gives

$$
\lambda _ { j } ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) - \sum _ { i } \lambda _ { i } y _ { i } \frac { \hat { \mathcal { O } } } { \partial y _ { i } } ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) = \Bigg ( \lambda _ { j } - \sum _ { i } \lambda _ { i } m _ { i } \Bigg ) ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) ;
$$

so we can solve (4.4) by choosing the coefficients of the monomials in $h _ { j }$ to be equal to the coefficients in $g _ { k j }$ divided by $\begin{array} { r } { ( \sum _ { i } \lambda _ { i } m _ { i } - \lambda _ { j } ) } \end{array}$

The transformation eliminating the terms ${ \bf g } _ { k } ( { \bf x } )$ from the vector field modifies the higher-order terms, but the form of the dynamical system will be the same as (4.1), with $k$ replaced by $k + 1 .$ The process of elimination can be carried through indefinitely unless there exists a vector $\mathbf { m }$ with positive integer components, or which

$$
\lambda _ { j } = \sum _ { i = 1 } ^ { N } m _ { i } \lambda _ { i } = \mathbf { m } \cdot \boldsymbol { \mathcal { L } }
$$

for one of the eigenvalues. The equality (4.6) is known as the resonance condition,nd the llet $k = \textstyle \sum _ { i } m _ { i }$ for which it holds is the order of the resonance. We can obviously eliminate all the terms $\mathbf { g } _ { 2 } \cdots \mathbf { g } _ { k - 1 }$ of a resonant system of order $k _ { i }$ ，and if the system is nonresonant, we can formally eliminate all the nonlinear terms. Examples of resonant systems are those with 𝜆 =22 (second order) and 𝜆1 +2=O (third order,since $\lambda _ { 1 } = 2 \lambda _ { 1 } + \lambda _ { 2 } )$ .The relation $2 \lambda _ { 1 } = 3 \lambda _ { 2 }$ does not imply a resonance.

It is easy to correlate some resonances to the configuration of the motion. This is the case of a conjugate pair of imaginary eigenvalues. As we have seen in section 1.2, the linear motion then has a centre, so that the nonlinear terms may push the orbits either towards the origin or away from it. The case of two degenerate real (negative) eigenvalues can likewise be understood. The linear motion is then radial towards the origin. This is the borderline between two nodes, having either eigenvector as the ‘fast or the ‘slow' axis. A perturbation may also make the dynamical matrix undiagonalizable.

Example. Consider the system ${ \dot { \mathbf { x } } } = { \mathbf { f } } ( { \boldsymbol { x } } )$

$$
\dot { x } _ { 1 } = \lambda _ { 1 } x _ { 1 } , \qquad \dot { x } _ { 2 } = \lambda _ { 2 } x _ { 2 } + a x _ { 1 } ^ { 3 } .
$$

The transformation $\mathbf x \to \mathbf y$

$$
y _ { 1 } = x _ { 1 } ^ { 3 } , \qquad y _ { 2 } = x _ { 2 } ,
$$

linearizes this system in the form

$$
\dot { y } _ { 1 } = 3 \lambda _ { 1 } y _ { 1 } , \qquad \dot { y } _ { 2 } = \lambda _ { 2 } y _ { 2 } + a y _ { 1 } .
$$

This system can be diagonalized by the transformation $\mathbf { y } \to \mathbf { Y }$ ：

$$
Y _ { 1 } = y _ { 1 } , \qquad Y _ { 2 } = y _ { 2 } - { \frac { a } { 3 \lambda _ { 1 } - \lambda _ { 2 } } } y _ { 2 } .
$$

Finallytetrasrtio $\mathbf { Y }  \pmb { \chi }$

$$
Y _ { 1 } = { \mathfrak { x } } _ { 1 } ^ { 3 } , \qquad Y _ { 2 } = { \mathfrak { x } } _ { 2 } ,
$$

brings thedynamical system to the form $\dot { \pmb { x } } = D { \bf f } ( { \pmb { x } } ) .$ The full transformation ${ \pmb x }  { \pmb x }$ is simply

$$
x _ { 1 } = x _ { 1 } , \qquad x _ { 2 } = x _ { 2 } + { \frac { a } { 3 \lambda _ { 1 } - \lambda _ { 2 } } } x _ { 1 } ^ { 3 } .
$$

It is analytic everywhere unless there is a resonance: 2 =3𝜆. In this case there is nothing special about the resonant system itself. However, it becomes impossible to diagonalize the degenerate linear system (4.10).

# Exercise

It is posible to reduce systems with degenerate eigenvalues to a normal form if the eigenvalues are degenerate, though the solution no longer decouples interms ofmonomials (Arnold,1982).Find the linear equations for the coefficients in h for $k = 2$ if the diagonal matrix can be reduced only to a two-dimensional Jordan block.

The absence of an exact resonance does not guarantee the convergence of the normal-form transformation to the resulting linear system. The problem is that the resonance condition may be approached closely many times with arbitrary precision, as $| { \bf m } |  \infty$ . This is known as the small-denominator problem: Some of the coefficients of the successive normal-form transformations become arbitrarily large. The necessary and sufficient condition for this not to occur is that $\mathcal { L }$ lie in the Poincare domain: Allthe eigenvalues lie on one side of a straight line on the complex $\lambda$ plane, whereas the origin lies on the other side. To see that this is suficient, we project all the eigenvalues onto the normal to the sraight line,as in figC4.1All of these will be greater than or equal to the distance between the straight line and the origin. Hence, the linear combination of eigenvalnes $\mathbf { m } \cdot \mathcal { L }$ has an arbitrarily large normal projection as $| { \bf m } | \to \infty$ It must therefore become greater than the projection of any individual eigenvalue.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/b7bfc47a31da1586a86ffca187c87edbc868c09ab47644ca9454c777f9342d0c.jpg)  
FigC4.1.The eigenvalues lie in the Poincare domain if they are all on the opposite side of a straight line with respect to the origin. Convergence of the normal form in some neighbourhood of the origin is guaranteed in this case.

Poincaré demonstrated the convergence of the normal-form transformationinaneighbourhood of theequilibrium for eigenvalues in the Poincare domain. In the Siegel domain, complementary to the Poincare omain, convergence is still possible according to Siegel's theorem (demonstrated in Arnold, 1982, sec. 28). The sufficient condition is that there exist positive numbers $C$ and $\nu$ such that

$$
| \lambda _ { j } - \mathbf { m } \cdot \mathcal { L } | \geq C / | \mathbf { m } | ^ { \nu }
$$

for each eigenvalue $\lambda _ { j }$ and for all positive-integer vectors m. This strange condition resembles the one for the convergence of the circle map,to be discussed in detail in the next chapter.

There are two alternatives by which we can extend the normal-form analysis to periodic orbits. One is to consider the Poincare section near a periodic orbit and to derive the normal form in the neighbourhood of the fixed point. This procedure, presented in Arnold (1982), is simple for general systems, but its adaptation to Hamiltonian systems is not easy. Otherwise, we can use periodic coordinates based on the periodic orbit, as in section 2.5,and work with the reduced time-dependent system.

Consider,then,the linear part of this time periodic sytem:

$$
\dot { \mathbf { x } } = \mathcal { A } ( t ) \mathbf { x } .
$$

We now define the matrix $\mathcal { L }$ so that the map after the period $2 \pi$ takes the form

$$
\mathbf { x } = \exp ( 2 \pi { \mathcal { L } } ) \mathbf { x } _ { 0 } = \left( \exp \int _ { 0 } ^ { 2 \pi } { \mathcal { A } } ( t ) d t \right) \mathbf { x } _ { 0 } .
$$

The coordinate transformation

$$
\mathbf { x } = \left( \exp \int _ { 0 } ^ { t } \mathcal { A } ( t ) d t \right) \exp ( - t \mathcal { L } ) \mathbf { y }
$$

can then be verified to reduce (4.14) to the time-dependent linear system

$$
\dot { \mathbf { y } } = \mathcal { L } \mathbf { y } .
$$

If 4 has distinct eigenvalues,it can be diagonalized, so we will suppose $\mathcal { L }$ to be diagonal as in the time-independent theory

We seek again a nonlinear coordinate transformation that eliminates the term $\mathbf { g } _ { k }$ (of order $\geq 2$ ) from the expansion

$$
{ \dot { \mathbf { x } } } = { \mathcal { L } } { \mathbf { x } } + { \mathbf { g } } _ { k } ( { \mathbf { x } } , t ) + { \mathbf { g } } _ { k + 1 } ( { \mathbf { x } } , t ) + \cdots .
$$

Thus substitution

$$
\mathbf { x } = \mathbf { y } + \mathbf { h } ( \mathbf { y } , t ) ,
$$

where h is a vector with polynomial components $h _ { j }$ in y that has periodic coefficients in $t ,$ leads to the set of equations

$$
\lambda _ { j } h _ { j } - \sum _ { i } \frac { \partial h _ { j } } { \partial y _ { i } } \lambda _ { i } y _ { i } - \frac { \partial h _ { j } } { \partial t } = - g _ { k j } ( \mathbf { y } , t ) .
$$

Expanding the components in Fourier series,

$$
h _ { j } ( { \bf y } , t ) = \sum _ { l = - \infty } ^ { \infty } \sum _ { m _ { 1 } + \cdots + m _ { N } = k } h _ { j , m , l } y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } e ^ { i l t } ,
$$

and proceeding likewise with the field components $g _ { k j }$ ,we obtain the formal solution

$$
h _ { j , \mathbf { m } , l } = \frac { g _ { k j , \mathbf { m } , l } } { i l + \mathbf { m } \cdot \mathcal { L } - \lambda _ { j } } ,
$$

unless the resonance condition

$$
\lambda _ { j } = \mathbf { m } \cdot \boldsymbol { \mathcal { L } } + i \boldsymbol { l }
$$

is satisfied.

The question of convergence of the normal-form series is dealt with in much the same way as in the time-dependent problem. The difference lies in the imaginary number il,which limits the Poincare domain to be the set of matrices $\mathcal { L }$ ,the eigenvalues of which have all positive real parts or all negative real parts. Convergence is guaranteed in the Poincaré domain, whereas small denominators again appear in the complementary Siegel domain.

# 4.2 The Birkhoff normal form

It was shown in section 1.2 that the eigenvalues of Hamiltonian systems always arise in pairs: $\lambda , - \lambda$ . In the context of normal forms they therefore have a third-order resonance. Hence, it is impossible to linearize Hamiltonian systems by an analytic canonical transformation. The best that one can aim for is to simplify their Taylor expansion at an equilibrium or periodic orbit,as with non-Hamiltonian resonances treated by Arnold (1982) and Guckenheimer and Holmes (1983).

The special feature of the Birkhoff normal form is that it is a reduction of the Hamiltonian rather than the fulldynamical system.The generating function $S ( \pmb { \mathscr { p } } , \pmb { \ q } , t )$ defines implicitlya canonical transformation $( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } )  ( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } )$ by the equations

$$
{ \bf p } = \hat { \sigma } S / \hat { \partial } { \bf q } , \qquad { \bf q } = \hat { \sigma } S / \hat { \partial } { \bf p } .
$$

The Hamiltonian is concomitantly transformed by

$$
H ( \mathfrak { p } , \mathfrak { q } ) = H ( \mathfrak { p } , \mathfrak { q } ) + \partial S / \partial t .
$$

The idea is thus to study the effect of polynomial generating functions on the Taylor expansion of the Hamiltonian. The treatment here will be limited to a single degree of freedom, to avoid encumbering the notation, for the generalization is obvious. Since the system is time periodic, the foregoing also applies to the neighbourhood of a periodic orbit of an autonomous system with two freedoms, as discussed in section 2.5.

The simplest case is the unstable equilibrium. The Taylor-Fourier expansion of the Hamiltonian then has the form

$$
H ( p , q , t ) = \lambda p q + \sum _ { \alpha + \beta = k } ^ { \infty } \ \sum _ { l = - \infty } ^ { \infty } H _ { \alpha \beta l } p ^ { \alpha } q ^ { \beta } \exp ( i l t ) ,
$$

where $k > 2$ .This is transformed by the generating function

$$
S ( \mathfrak { p } , q , t ) = \mathfrak { p } q + \sum _ { \alpha + \beta = k } \ \sum _ { l = - \infty } ^ { \infty } S _ { \alpha \beta l } \mathfrak { p } ^ { \alpha } q ^ { \beta } \exp ( i l t ) .
$$

According to(4.24) the first term of $s$ generates the identity transformation. The second term will be small,ofoder $k$ , near the origin. The series for the first two partial derivatives,

$$
\begin{array} { c } { { p = \displaystyle \hat { \sigma } S / \hat { \sigma } q = \mathfrak { p } \Bigg [ 1 + \displaystyle \sum _ { \iota , \alpha + \beta = k } \beta S _ { \alpha \beta \iota } \mathfrak { p } ^ { \boldsymbol { x } - 1 } q ^ { \beta - 1 } \exp ( i l t ) \Bigg ] , } } \\ { { \mathrm { q } = \hat { \sigma } S / \hat { \sigma } \mathfrak { p } = q \Bigg [ 1 + \displaystyle \sum _ { \iota , \alpha + \beta = k } \alpha S _ { \alpha \beta \iota } \mathfrak { p } ^ { \boldsymbol { x } - 1 } q ^ { \beta - 1 } \exp ( i l t ) \Bigg ] , } } \\ { { \partial S / \hat { \sigma } t = \displaystyle \sum _ { \iota , \alpha + \beta = k } i l S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha } q ^ { \beta } \exp ( i l t ) , } } \end{array}
$$

can be inverted up to order $k$ to yield the explicit transformation,

$$
\begin{array} { l } { { \displaystyle p = \mathfrak { p } \Bigg [ 1 + \sum _ { l , \alpha + \beta = k } \beta S _ { \alpha \beta l } \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \Bigg ] , } } \\ { { \displaystyle q = \mathfrak { q } \Bigg [ 1 - \sum _ { l , \alpha + \beta = k } \alpha S _ { \alpha \beta l } \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \Bigg ] , } } \\ { { \displaystyle \frac { \partial S } { \partial t } = \sum _ { l , \alpha + \beta = k } i l S _ { \alpha \beta l } \mathfrak { p } ^ { \alpha } \mathfrak { q } ^ { \beta } \exp ( i l t ) + \cdots , } } \end{array}
$$

The quadratic part of the Hamiltonian becomes

$$
\lambda p q = \lambda \mathfrak { p q } \left[ 1 + \sum _ { l , \mathfrak { x } + \beta = k } ( \beta - \alpha ) \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \right] ,
$$

so the full Hamiltonian takes the form

$$
H ( \mathfrak { p } , \mathfrak { q } , t ) = \lambda \mathfrak { p q } + \sum _ { l , \alpha + \beta = k } \left\{ H _ { x \beta l } + [ \lambda ( \beta - \alpha ) - i l ] S _ { \alpha \beta l } \mathfrak { p } ^ { \alpha } \mathfrak { q } ^ { \beta } \in \mathrm { x p } ( i l t ) + \cdots \right\} .
$$

We can therefore eliminate all the terms of order $k$ with the choice

$$
S _ { \alpha \beta l } = \frac { - H _ { \alpha \beta l } } { \lambda ( \beta - \alpha ) - i l } ,
$$

except for the term $\begin{array} { r } { \alpha = \beta , l = 0 } \end{array}$ that is,the term $H _ { \alpha \alpha 0 } ( \mathfrak { p } \mathfrak { q } ) ^ { \alpha }$ .Note that the inclusion of such a term in (4.26), with 2α <k, would not alter in any way the form of the k-order terms in (4.31). Hence,we can iterate the process of eliminating higher and higher order terms of the Hamiltonian,so as to obtain the kth-order Birkhoff normal form

$$
H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = \lambda { \mathfrak { p } } { \mathfrak { q } } + H _ { 2 } ( { \mathfrak { p } } { \mathfrak { q } } ) ^ { 2 } + \cdots + H _ { k } ( { \mathfrak { p } } { \mathfrak { q } } ) ^ { k / 2 } + \sum _ { l , \alpha + \beta = k + 1 } H _ { \alpha \beta l } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } \exp ( i l t )
$$

for any even k.

Differentiating the Hamiltonian in the normal form results in a polynomial dynamical system with odd-order terms, which correspond to the resonant terms of the Poincare normal form discussed in the previous section. Within that context the Hamiltonian system is in the Siegel domain; that is,in addition to the exact resonances, it is also subject to small denominators. The nontrivial content of Birkhoff's construction is seen from the fact that there are no small denominators in the successive transformations whose generating functions have coefficients given by (4.32). The expectation that the normal-form transformation is convergent for $k \to \infty$ is indeed borne out by Moser (1956) for a disc around the origin. We shall discuss the motion near an unstable orbit in the next section.

The Hamiltonian near a stable equilibrium has the Taylor-Fourier expansion

$$
H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = { \frac { \omega } { 2 } } \left( { \mathfrak { p } } ^ { 2 } + { \mathfrak { q } } ^ { 2 } \right) + \sum _ { \alpha + \beta = 3 } ^ { \alpha + \beta = \infty } \sum _ { l } H _ { \alpha \beta l } ^ { \prime } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } \exp ( i l t ) ,
$$

where $k > 2$ .This form is not convenient for the deduction of the normal-form transformation, so we complexify the Hamiltonian; that is, considering $p$ and $q$ to be complex variables, we make the linear transformation

$$
z = p + i q , \qquad z ^ { * } = p - i q .
$$

The variables z and z\* are considered to be independent. However,if the initial conditions for pand q are real z(t) and z\*(t) will remain complex conjugate solutions for all t, as discussed in section 1.1.

# Exercise

Verify that the trajectories z(t)and z\*(t) satisfy Hamilton's equations with the Hamiltonian

$$
- 2 i H ( p ( z , z ^ { * } ) , q ( z , z ^ { * } ) , t ) = - i \omega z z ^ { * } + \sum _ { \alpha + \beta = 3 } ^ { \alpha + \beta = \infty } \sum _ { l } H _ { \alpha \beta l } z ^ { \alpha } z ^ { * \beta } \exp ( i l t ) .
$$

Following exactly the same method as for the unstable case, we can now reduce the Hamiltonian to the kth-order normal form:

$$
- 2 i H = - i \omega _ { 3 3 } { ^ * } + H _ { 2 } ( _ { 3 3 } { ^ * } ) ^ { 2 } + \cdots + H _ { k } ( _ { 3 3 } { ^ * } ) ^ { k / 2 }
$$

That is, we eliminate the ‘nondiagonal’ coefficients of the Hamiltonian through the choice

$$
S _ { \alpha \beta l } = \frac { i H _ { \alpha \beta l } } { \omega ( \alpha - \beta ) - l }
$$

for the coefficients of the generating function

$$
S ( { 3 } , z ^ { * } , t ) = { 3 } { { z ^ { * } } } + \sum _ { \substack { l , \alpha + \beta = k } } S _ { \alpha \beta l 3 } { ^ { \alpha } } { z ^ { * \beta } } \exp ( i l t )
$$

of the transformation $( z , z ^ { * } ) \to ( 3 , 3 ^ { * } ) .$

This process can be carried through indefinitely only if the frequency $\omega$ is not a rational number. Otherwise,the maximum order for the normal form will be the highest $\alpha + \beta = k$ for which the resonance condition

$$
\omega ( \alpha - \beta ) - l = 0
$$

is not met. Even for irrational frequencies we are beset by small denominators,arising for all $\propto$ ， $\beta$ and l, such tht $l ( \alpha - \beta )$ is a good rational approximation to $\omega$ .These near resonances lead usually to the divergence of the normal form for stable periodic orbits,as will be shown in section 4.4. Only the time-independent Hamiltonian with a single freedom is exempt from resonances or small denominators.

The procedure for deducing the normal form for autonomous systems with two freedoms (or more) is essentially the same as above. If the linearized Hamiltonian is λPiq1 +2Pzq2,we can use the real coordinates, obtaining a normal form with small denominators (and resonances if $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are rationally related). For $\lambda _ { 1 } p _ { 1 } q _ { 1 } + ( \omega _ { 2 } / 2 ) ( p _ { 2 } ^ { 2 } + q _ { 2 } ^ { 2 } )$ we proceed by complexifying the $( p _ { 2 } , q _ { 2 } )$ coordinates. The resultant normal form has no small denominators.Finally, we complexify both pairs of coordinates to obtain the normal form for a stable equilibrium. This is the case that is studied most extensively in spite of the presence of smalldenominators. Most presentations follow a more abstract algebraic approach, which leads to useful computational methods.Theseare reviewed by Lichtenberg and Lieberman (1983).

# Exercise

Show that the complexification

$$
\begin{array} { r l } { p _ { 1 } ^ { \prime } = p _ { 1 } - i p _ { 2 } , \quad } & { { } q _ { 1 } ^ { \prime } = q _ { 1 } + i q _ { 2 } } \\ { p _ { 2 } ^ { \prime } = p _ { 1 } + i p _ { 2 } , \quad } & { { } q _ { 2 } ^ { \prime } = q _ { 1 } - i q _ { 2 } } \end{array}
$$

takes the linear Hamiltonian system $H = \lambda ( p _ { 1 } q _ { 1 } + p _ { 2 } q _ { 2 } ) + \omega ( p _ { 1 } q _ { 2 } - q _ { 1 } p _ { 2 } ) .$ witha compexartetofgenvluesintoeo $H ^ { \prime } = ( \lambda - i \omega ) p _ { 1 } ^ { \prime } q _ { 1 } ^ { \prime } +$ $( \lambda + i \omega ) p _ { 2 } ^ { \prime } q _ { 2 } ^ { \prime }$ . Show that the normal form for $H ^ { \prime }$ has no small denominators.

# 4.3 Homoclinic motion revisited

The Birkhoff-Moser theorem,which establishes the existence of an analytic transformation reducing an unstable time-periodic system to its Birkhoff normal form,also applies to maps.This is obvious for the Poincare map of the system, and Moser (1956) proves that one can always interpolate a time-periodic Hamiltonian system, given an area-preserving map. The normal form of the map will simply be the Poincaré map of the normal form for the interpolated time-periodic system. Since the normalized Hamiltonian is independent of time and depends only on the product pq: $H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = f ( \xi )$ where $\xi = { \mathfrak { p } } { \mathfrak { q } }$ ,Hamilton's equations have the form

$$
\dot { \mathfrak { p } } = - ( d f / d \xi ) \mathfrak { p } , \qquad \dot { \mathfrak { q } } = ( d f / d \xi ) \mathfrak { q } .
$$

Verifying that $\xi$ and hence $d f / d \xi$ are constants of the motion, we can immediately integrate (4.42) and so obtain the Poincare map for a period of $2 \pi , { \pmb x } ^ { \prime } = { \bf T } _ { N } ( { \pmb x } ) ,$ as

$$
{ \bf p } ^ { \prime } = U ( { \mathfrak { p q } } ) { \mathfrak { p } } , \qquad { \mathfrak { q } } ^ { \prime } = U ^ { - 1 } ( { \mathfrak { p q } } ) { \mathfrak { q } } ,
$$

where

$$
U ( \xi ) = \exp ( - i 2 \pi d f / d \xi ) .
$$

For a time-periodic system we get a different normal-form transformation for each Poincare map by fixing $t$ in (4.26) and (4.27). Of course, it is not necessary to go through the business of interpolating systems once the existence of the normal form for maps has been proved. All that must be done is to evaluate the coefficients of

$$
U ( \mathfrak { p q } ) = \lambda \Biggl [ 1 + \sum _ { \alpha = 1 } ^ { \infty } U _ { 2 \alpha } ( \mathfrak { p q } ) ^ { \alpha } \Biggr ]
$$

and the normal-form transformation $\mathbf { x } = \mathbf { N } ( \pmb { x } )$

$$
\begin{array} { l } { { \displaystyle p = { \mathfrak { p } } + \sum _ { \alpha + \beta = 2 } ^ { \infty } p _ { \alpha \beta } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } } , } \\ { { \displaystyle q = { \mathfrak { q } } + \sum _ { \alpha + \beta = 2 } ^ { \infty } q _ { \alpha \beta } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } } , } \end{array}
$$

by direct substitution into the map $\mathbf { x } ^ { \prime } = \mathbf { T } ( \mathbf { x } ) \colon$

$$
\begin{array} { l } { { p ^ { \prime } = \lambda p + \displaystyle \sum _ { \alpha + \beta = 2 } ^ { \infty } p _ { \alpha \beta } ^ { \prime } p ^ { x } q ^ { \beta } , } } \\ { { q ^ { \prime } = \lambda ^ { - 1 } q + \displaystyle \sum _ { x + \beta = 2 } ^ { \infty } q _ { x \beta } ^ { \prime } p ^ { \alpha } q ^ { \beta } . } } \end{array}
$$

Moser(1956) proves the convergence of the normal-form transformation in a small disc surrounding the origin. This is not of immediate use, because the disc is an unstable region,only briefly visited by most points. It is therefore important to show that the region of convergence can be extended,as inda Silva Ritter,Ozorio de Almeida and Douady (1987), for an analytic map whose inverse ${ \bf T } ^ { - 1 }$ is also analytic.This is possible because the normal map (4.43) is defined in terms of the function $U ( { \mathfrak { p } } { \mathfrak { q } } )$ which is itself invariant under the mapping. If the series for the normal map converges for $( \mathfrak { p } _ { 0 } , \mathfrak { q } _ { 0 } )$ in $D _ { 0 }$ , it converges for all $( { \mathfrak { p } } , { \mathfrak { q } } )$ such that ${ \mathfrak { p q } } \leq { \mathfrak { p } } _ { 0 } { \mathfrak { q } } _ { 0 }$ . The relation between the invariant curves and the region of convergence $D _ { 0 }$ and $\mathbf { N } ( D _ { 0 } )$ for the original and the normalized system.is shown in fig.C4.2.)

Let us now define the transformations

$$
{ \bf N } _ { m } = { \bf T } ^ { - m } { \cdot } { \bf N } { \cdot } { \bf T } _ { N } ^ { m } , \qquad { \bf N } _ { 0 } = { \bf N }
$$

for all positive or negative $m$ Since $\mathbf { N }$ is analytic in $D _ { 0 }$ ， $\mathbf { N } _ { - m }$ is analytic in the region

$$
\begin{array} { r } { D _ { m } = \mathbf { T } _ { N } ^ { m } ( D _ { 0 } ) . } \end{array}
$$

All the regions $D _ { n }$ have points inommon, namely,some neighbourod

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/3b291c3b31a6d928efb90fcda5c742a19244735f844d621ba298331442f08b30.jpg)  
FigC 4.2. The circle of convergence D and the invariant hyperbolas that touch it aredistorted by the normal-form transformation N.

of the origin (fig.4.3) Moreover, ${ \bf N } _ { 0 }$ and $\mathbf { N } _ { m }$ coincide in the region where they both converge:

$$
\mathbf { N } _ { m } = \mathbf { T } ^ { - m } { \boldsymbol { \cdot } } \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } _ { N } ^ { m } = \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } _ { N } ^ { m } { \boldsymbol { \cdot } } \mathbf { N } ^ { - 1 } { \boldsymbol { \cdot } } \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } ^ { m } = \mathbf { N } .
$$

The same is true for any pair of regions $D _ { m }$ and $D _ { m ^ { \prime } }$ , so we can define the extended normal-form transformation to be

$$
\mathbb { N } = \operatorname* { l i m } _ { K  \infty } \bigcup _ { m = - K } ^ { K } \mathbf { N } _ { m } ,
$$

Which will be analytic in the region

$$
\mathbb { D } = \operatorname* { l i m } _ { K  \infty } \bigcup _ { m = - K } ^ { K } D _ { m } .
$$

Because of (4.5O), the Taylor series for each $\mathbf { N } _ { m }$ will be identical with the series for ${ \bf N } _ { 0 }$ , but we must show that the region of convergence for the Taylor series of $\mathbf { N } _ { m }$ indeed extends far out of $D _ { 0 }$ . This is done in da Silva Ritter,Ozorio de Almeida and Douady (1987) by complexifying, that is, by using the fact that the convergence of the series for $\mathbf { N } _ { 0 } ( \pmb { x } _ { 0 } )$ implies the convergence of the Taylor series for $\mathbf { N } _ { 0 } ( \mathfrak { z } )$ for $\lvert 3 _ { 1 } \rvert \leq \lvert x _ { 1 0 } \rvert$ and $| 3 _ { 2 } | \leq | x _ { 2 0 } |$ .Therefore, inside this region there are no poles, nor are there any in the complex regions $D _ { \mathfrak { n } \mathfrak { c } }$ obtained from it by the transformations (4.48).Thisfaciuresuestheonveenceoftheyiein $D _ { \mathrm { n c } }$

The separatrices of the map $\mathbf { T }$ are the images of the $\mathfrak { x } _ { 1 } = 0$ and $\mathfrak { X } _ { 2 } = 0$ axes under the transformation $\mathbb { N } ( { \pmb x } ) .$ The extension of the Birkhoff-Moser theorem guarantees that the normal form converges, indefinitely far out along the separatrices. As a consequence we can calculate homoclinic (and heteroclinic) points from the images of both axes under N.(Heteroclinic points are calculated from the normal forms for two unstable points.) Though it is not difficult to compute some homoclinic points directly by following orbits along the stable and unstable manifolds, it is only the above method that provides the entire homoclinic orbit with uniform precision.All that has to be done is to follow the linear orbit of the ngrmal coordinates for the homoclinic point, before transforming back to x This last step is not even necessary close to the origin,since there $\mathbb { N }$ is asymptotic to the identity.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/5dfad7d6eecd7aea184a8f300250891f8cbe3397a74a6e64b2492fac9f191a4a.jpg)  
Fig：4.3All the images $D _ { n }$ of $D _ { 0 }$ have a common intersection,whichiluds the origin.

The normal-form transformation also converges along invariant square hyperbolas very close to the $\mathfrak { x } _ { 1 } = 0$ and $\mathfrak { x } _ { 2 } = 0$ axes. The images of these curves self-intersect near the homoclinic points. These self-intersections are not generally periodic points,but a simple argument due tp Birkhoff (1927) shows that they give rise to an infinite sequence of periodic points. Consider the orbit of a point of self-intersection; generally there will be $n - 1$ images along the invariant curve,say the inner one in figC4.4a,while the nth image lies yod theelf-interseion.owevertheage spacing between the points on the orbit diminishes continuously as the /invariant curves come closer| to the separatrices,that is,for self-intersections that approach the homoclinic point. Thele will thus be an invariant curve where the nthl image of the self-intersection comes back to itself exactly -the nth-order periodic orbit. By thesame token we find an $( n + 1 )$ order periodic orbit and so on.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/3edb5489785d563cef96657c27a7af7ecbca155e35084920ef2c25a6ed0cd7c5.jpg)  
Fig4.4)(a) The three self-intersectipg curves within the stable and the unstable manitolds are the images of invariant hyperbolas. There are fiye images of the point of intersection on the inner curve and six on the outer curve. The boundary curve supports a periodic orbit of period 6. (b) Here the pair pf curves supports a single periodic orbit of period 15. (c) A periodic orbit of perjod 24 is supported on three open invariant curves.

There are many other famjlies of periodic points that accumulate on the homoclinic point in the/limit of infinite periods.For instance, there are the families based on the mutual intersections/of a pair of invariant curves shown in figC4.4bjThese are obtained by reduiring that two families of curves satisfy two conditions: The orbit of each one of the intersections must land exactly on the other intersection. This is also the situation for the simplest heteroclinic points.Figure4.4c sketches a periodic orbit based on three invariant curves. In general we can find periodic orbits bound to any number $k$ of invariant curves. In the limit where $k \to \infty$ ,we obtain recurrent chaotic orbits.

The larger the period of the orbit, the closer will be the hyperbolas on which they travel to the $\pmb { \mathscr { X } }$ axes. In this limit the map $\mathbf { T } _ { N }$ becomes linear. Since the periodic points accumulate on the homoclinic point, their position is accurately given by a linearization of the normal-form transformation around the homoclinic point. Combining both linearizations,we arrive at explicit linear equations for the periodic points, which are asymptotically exact in the limit of high periods.To achieve this,let us consider both images (x\*,O) and (O,x\*) of the homoclinic point x\* under the transformation N-1 (fig.4.5).We define N and N2 to be the restrictions of N to neighbourhoeds of these two points. A periodic point of order m, with normal eoordinates xm, propagates from near (0,r\*) by Tn into the neighbourhood of (x\*,O). It satisfies the equation

$$
\begin{array} { r } { \pmb { x } _ { m } = \mathbb { N } _ { 2 } ^ { - 1 } \cdot \mathbb { N } _ { 1 } \cdot \mathbf { T } _ { N } ^ { m } ( \pmb { x } _ { m } ) . } \end{array}
$$

Linearizing N,around the images of the homoclinic point and the normal map $\mathbf { T } _ { N } ^ { m }$

$$
{ \left[ \begin{array} { l } { { \pmb x } _ { 1 } ^ { \prime } } \\ { { \pmb x } _ { 2 } ^ { \prime } } \end{array} \right] } = { \mathcal { L } } ^ { m } { \pmb x } = { \left[ \begin{array} { l l } { \lambda } & { 0 } \\ { 0 } & { \lambda ^ { - 1 } } \end{array} \right] } ^ { m } { \pmb x } ,
$$

we can approximate (4.53) by the linear equation

$$
\begin{array} { r } { \mathcal { R } ^ { m } \pmb { \chi } \equiv D [ \mathbb { N } _ { 2 } ^ { - 1 } \cdot \mathbb { N } _ { 1 } \cdot \mathbf { T } _ { N } ^ { m } ] \pmb { x } = ( 0 , \pmb { x } _ { 2 } ^ { * } ) + ( D \mathbb { N } _ { 2 } ) ^ { - 1 } ( D \mathbb { N } _ { 1 } ) [ \mathcal { L } ^ { m } \pmb { x } - ( \pmb { x } _ { 1 } ^ { * } , 0 ) ] . } \end{array}
$$

A periodic orbit ${ \pmb x } _ { m _ { J } } . . . , m _ { 1 }$ with $m _ { 1 }$ points on one hyperbola, $m _ { 2 }$ on another and so on up to $m _ { J }$ on the $J$ th hyperbola is obtained from the solution of the equation

$$
\biggl ( \prod _ { j = 1 } ^ { J } \mathcal { R } _ { m _ { J } } - 1 \biggr ) \tt t _ { m _ { J } \cdots m _ { 1 } } = 0 .
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/90ab9cbca6fb6a505ea9b7ec8173e07a85906db8080c9d91737adbbdc3a51ff7.jpg)  
$\mathrm { F i g } ( 4 . 5 . )  { \mathbb { N } } _ { 1 } (  { \mathbf { x } } )$ and $\mathbb { N } _ { 2 } ( \mathbf { x } )$ are,respectively，therestrictionsof $\mathbb { N } ( \mathbf { x } )$ to the neighbourhoods of the pre-images of the homoclinic point (x\*,O) and (0,r\*).

Contrary to appearances, (4.56) is not a homogeneous equation, the inhomogeneous terms arising from the normal coordinates for the homoclinic point in (4.55). Thus,we obtain a unique solution forany set of indices m1.·my. The resulting approximation for xm..m1 becomes asymptotically exact in the limit where all the $m _ { J }  \infty$ ·

It is interesting that the presence of denumerable periodic orbits is a consequence of the Smale-Birkhoff theorem and ultimately derives from the nonlinearity of the map T.It may seen strange to calculate these orbits from a linear map, but it must be borne in mind that the linearization is performed around the homoclinic point and not the origin. We are familiar with chaotic maps where the orbits are ‘folded back in’. This is the case of Arnold’s cat map,which also has denumerable periodic orbits,and even for Smale's horseshoe,developed as a simplified model of homoclinic motion.

The computational feasibility of calculating homoclinic orbits from the Birkhoff normal form was verified by Ozorio de Almeida, Coutinho and da Silva Ritter (1985) for the family of quadratic maps

$$
\begin{array} { r } { x _ { 1 } ^ { \prime } = x _ { 1 } \cosh \alpha + ( x _ { 2 } - x _ { 1 } ^ { 2 } ) \sinh \alpha , } \\ { x _ { 2 } ^ { \prime } = x _ { 2 } \sinh \alpha + ( x _ { 2 } - x _ { 1 } ^ { 2 } ) \cosh \alpha . } \end{array}
$$

This can be proved to be equivalent to all quadratic maps with a hyperbolic fixed point at the origin, just as the similar map used by Henon (1969) is equivalent to all quadratic maps containing an eliptic fixed point. Figures 4.6a and b show,respectively，the separatrices calculated by iterating points on the separatrices close to the origin and by the normal form. Da Silva Ritter et al. (1987) achieved the calculation of unstable orbits that returned to themselves after ten iterations within an accuracy of twenty-one significant figures, by calculating the self-intersection of invariant curves! Good agreement was found with the periodic points calculated from the explicit linear equation (4.56) with $J = 1$ ), and the accuracy of the points calculated in this way was seen to improve with $n$

This technique can evidently be extended to the calculation of heteroclinic points and their satellite periodic orbits and to the calculation of homoclinic(heteroclinic) points of time-periodic Hamiltonian systems with one freedom. Though the numerical convergence of the normal form is very fast, the very large x coordinates needed to calculate ‘higher homoclinic points’ arising from the mutual intersections of long loops of the separatrices may not be accessible. It seems likely that the present formalism can be used to compute homoclinic and periodic orbits near unstable equilibria for which the normal form has no small denominators.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/68e7d89d2a64bfbe8c13b15fde3eb094c30e6b94c152cda02c21c568d1794128.jpg)  
Fig(4.6.J(a)Points on the stable and unstable manifolds obtained by positive and negative iterations on the linear approximation of the manifolds very near the origin,for $\alpha = 1 . 4$ (b) The two separatrices calculated from the Birkhoff normal form up to twentieth order.

# 4.4 Bifurcations of stable periodic orbits

In the absence of an exact resonance, the cancelling of all the off-diagonal' terms in the normal form for a stable periodic orbit leads to the formal series

$$
- 2 i H = - i \omega z z ^ { * } + H _ { 2 } ( z z ^ { * } ) ^ { 2 } + \cdots ,
$$

We can cast this into real variables by merely reversing the transformation (4.35), so

$$
H = \omega \bigg ( \frac { p ^ { 2 } + q ^ { 2 } } { 2 } \bigg ) + H _ { 2 } \bigg ( \frac { p ^ { 2 } + q ^ { 2 } } { 2 } \bigg ) ^ { 2 } + \cdots ,
$$

or we can use the canonical polar coordinates (1.48), that is,action-angle variables,

$$
p = ( 2 I ) ^ { 1 / 2 } \sin \phi , \qquad q = ( 2 I ) ^ { 1 / 2 } \cos \phi ,
$$

to obtain

$$
H = \omega I + H _ { 2 } I ^ { 2 } + \cdots .
$$

The Hamiltonian not only is integrable, because of the loss of its time dependence,but also is independent of $\theta$ .The circles centred on the origin are invariant circles, just as with the quadratic Hamiltonian ωl = $\omega ( p ^ { 2 } + q ^ { 2 } ) / 2$ The difference is that the motion along each circle no longer has the universal angular velocity $\omega$ . Indeed, from Hamilton's equations

$$
\dot { \phi } ( I ) = \omega + 2 H _ { 2 } I + \cdots .
$$

Even though the normal form does not usually converge, we can bring any nonresonant Hamiltonian to coincide with it in its lowest terms, The normal form therefore provides an accurate approximation.of the motion close to the origin,that is,the periodic orbit ofanautonomous two-freedom system.In this expanded picture (fig4.7),Ihe invariant circle of the normal form corresponds to a thin torus surrounding the periodic orbit. Neighbouring orbits wind around such tori. The frequency Qf rotation (I) varies continuously,so that arbitrarily close to the origin there are Birkhoff tori for which \$= l/k is a rational number. The orbits on these tori are periodic, for the orbits of the Poincare map t→t +2π close after k iterations.

Let us focus on one of these periodic tori, while altering the energy. It was shown in section 2.5 that typical periodic orbits are members of one-parameter families, where the energy can be chosen as the parameter. Generally the linear frequency will be a monotonic function ω(E) over a small energy range. So if the periodic orbit torus lies close to the periodic orbit at the orign, we may choose instead

$$
\varepsilon = \omega ( E ) - l / k
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/014d2feeed84afb0cea354c1e8a9e61f2799db7fa5e02bfcb32ca2d09ac0fb62.jpg)  
Fig(4.7The invariant circle of the normal form corresponds to a thin torus surrounding the periodic orbit.

as the parameter for the family. Substituting $l / k$ on the left side of (4.62) and taking $\omega$ from (4.63), the action variable for the periodic torus is seen to be

$$
I _ { l / k } = - \varepsilon / ( 2 H _ { 2 } ) + O ( \varepsilon ^ { 2 } ) .
$$

Thus, the periodic torus collapses onto the origin as $\varepsilon \to 0$ ,which is exactly the resonance condition. This event resembles the generic Hopf bifurcations of dissipative systems described by Arnold (1982) and Guckenheimer and Holmes (1983). The orbits on the periodic torus are fixed points of the kth iteration of the Poincare map. According to the Birkhoff picture', this entire family of fixed points collapses onto the central fixed point when a resonance occurs. This is a complete alteration of the ‘linear picture',where at resonance all points become fixed points.The resonance condition for the Poincare map is the same as (2.33).

As the resonance condition is approached, one of the denominators in the normal-form transformation becomes arbitrarily large. The Birkhoff normal form does not hold through the resonance, so we must work instead witha resonant normal form,including allthe terms that blow up the transformation exactly at the resonance. This has the form

$$
- 2 i { \cal H } = - i \omega z z ^ { * } + { \cal H } _ { 2 } ( z z ^ { * } ) ^ { 2 } + \cdots + { \cal H } _ { k 0 l } z ^ { k } e ^ { i l t } + { \cal H } _ { 0 k , - l } z ^ { * k } e ^ { - i l t } + \cdots ,
$$

showing explicitly the resonant term of lowest order,since this will have the strongest effect near the origin, where the bifurcation takes place. Though the resonant terms cannot be cancelled when $\varepsilon = 0$ ,we can still eliminate the time dependence by means of the canonical time-dependent

transformation

$$
\zeta = z \exp ( i l t / k ) , \qquad \zeta ^ { * } = z ^ { * } \exp ( - i l t / k ) ,
$$

generated implicitly by

$$
\sigma ( z , \zeta ^ { * } , t ) = z \zeta ^ { * } \exp ( i l t / k ) .
$$

Applying (4.25), we obtain

$$
- 2 i H = - i \varepsilon \zeta \zeta ^ { * } + H _ { 2 } ( \zeta \zeta ^ { * } ) ^ { 2 } + \cdots + 2 i \operatorname { I m } ( H _ { k 0 l } \zeta ^ { k } ) + \cdots ,
$$

using the fact that $H _ { 0 k , - m } = - \ H _ { k 0 m } ^ { * }$ for $H$ to be real. In the real polar coordinates

$$
\zeta = ( 2 I ) ^ { 1 / 2 } \exp ( i \phi ) ,
$$

the Hamiltonian takes the form

$$
H ( I , \phi ) = \varepsilon I + H _ { 2 } I ^ { 2 } + \cdots + a I ^ { k / 2 } \sin ( k \phi ) .
$$

So the coordinate transformation (4.66) takes the system to rotating coordinates in which the periodic torus (4.64) becomes a circle of fixed points.For $k > 4$ the last term,as well as the higher $\phi$ independent terms, are smaller than the first two as $I \to 0$ .We can then consider the effect of the $\phi$ dependent term as a perturbation. Because of it, in general $( d H / d \phi ) _ { I _ { l / k } } \neq 0$ ,so that the only fixed points on the periodic torus have $\phi = ( \pi / 2 + n \pi ) / k$ . As a first approximation around the unperturbed torus $I _ { l / k } ,$ we have

$$
H ( I , \phi ) = H _ { 2 } ( I - I _ { l / k } ) ^ { 2 } + a I _ { l / k } ^ { k / 2 } \sin k \phi ,
$$

which can be recognized as the Hamiltonian for the pendulum; its level curves are shown in fig 4.8.jSo one half.of the periodic points are stable and one-half unstable. The stable points are surrounded by closed invariant curves known as islands or island tori in the extended two-freedom system. These correspond to librations of the pendulum. The pendulum rotations are distortions of the unperturbed Birkhoff invariant curves [horizontal lines, in the $( I , \phi )$ coordinates]. Between rotations and librations lie the separatrices.Since the system is time independent, we obtain their equation from the level curve with the energy of the unstable fixed point:

$$
I - I _ { \iota / k } = [ a I _ { \iota / k } ^ { k / 2 } ( 1 - \sin k \phi ) / H _ { 2 } ] ^ { 1 / 2 } .
$$

Therefore,the maximum area of the islands is of order $\varepsilon ^ { k / 4 }$ .For $k > 4$ the islands shrink faster than the periodic tori as $\varepsilon \to 0$ 、Thus, the ‘Birkhoff picture’， though qualitatively incorrect right down to $\varepsilon \to 0$ ，becomes quantitatively accurate: Itis impossible todistinguisha very thinresonance from a torus in a computation.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/81aa645094b0a2750dcc046d8fe70af330f982a979709a314d9479d9892517cc.jpg)  
$\mathrm { F i g } \widehat { ( 4 . 8 . ) }$ The Hamiltonian for the resonant normal form is approximately the same as for a pendulum with angular momentum $I - I _ { t / k }$

The foregoing analysis focused on a single periodic Birkhoff torus followed through the exact resonance by means of a survey of the family of periodic orbits placed at the origin. For a single energy $E$ there is an infinite number of periodic Birkhoff tori,the frequency of which approximates the irrational frequency $\omega ( E )$ arbitrarily well. The above theory can be applied to every one of them. In each case the periodic Birkhoff torus breaks up into $2 k$ periodic points, corresponding to a single pair of stable and unstable periodic orbits in the extended system. These resonances are dense near the origin, so the Birkhoff normal form cannot converge onto the wrong picture of the motion.

We note that even the resonant normal form does not converge. To start withit displays only a single resonance,so it is wrong in the region of rotations of the pendulum Hamiltonian(4.62). To the truncated resonant normal form, we must add the time-dependent remainder. We therfore expect that the separatrices will split into the transverse homoclinic intersections studied in chapter 3. Yet the closer the periodic Birkhoff torus is to the origin,the smaller willthis remainder be, so this region of chaotic motion becomes very narrow as the resonant region collapses on the origin.

There remains the all-important question of whether any tori subsist between this dense set of resonances,and indeed whether the islands themselves are not actually swept away by the homoclinic windings of the separatrices.Note that this whole analysis now can be applied to the stable periodic satellite orbit. We then obtain dense resonances among the islands,containing in turn stable periodic orbitsand so on.It turns out that typical stable motion is actually harder toanalyse than the chaotic unstable motion, our principal subject until now. The preeminent result in this area is the theorem of Koimogorov, Arnold and Moser, to be discussed in chapter 6,after the preliminary consideration of maps of the circle in chapter 5.

# Exercises

1. Verifythatthe transformation(4.66)alsoeliminates thetimedependence of all the higher-order resonant terms. Therefore the resonant normal form is integrable up to any order.   
2. Deduce the normal form for the neighbourhood of a stable equilibrium of an autonomous system with two freedoms.   
3. Show that,in the case of an exact resonance inexercise 2,acoordinate transformation willeliminate the dependence of the Hamiltonian on one of the angles. The corresponding action is an independent constant of the motion.

The resonances of order $k \leq 4$ have different structures. The case where $k = 3$ is analysedby Arnold (1978,app.7). Only a single unstable satelite orbit appears, corresponding to three fixed points. However, satellite fixed points exist on both sides of the resonance (fig. 4.9). The fourth-order resonance can happen generically in two forms. One follows the higherorder resonances, whereas the other is analogous to the third-order resonance.

The resonances of order 1 and 2 are the hardest to analyse. The problem is that it becomes impossible to separate clearly the quadratic part of the Hamiltonian as in (4.34) before starting the analysis. These cases were sorted out by Meyer (197O) in his complete analysis of generic bifurcations of area-preserving maps. Just as with the unstable points studied in section 4.3, there is a unique relation between the normal form for a periodic Hamiltonian and its Poincare section. The normal forms for all the generic bifurcations of fixed points of area-preserving maps are shown in fig 4.9.Y

According to the figure we have second-order resonances for both stable and unstable fixed points.These are known as period-doubling bifurcations, since the satellite periodic orbits have twice the period of the central orbit.

<table><tr><td rowspan=1 colspan=1>Repetitionnumberm</td><td rowspan=1 colspan=1>Linearizedmap M atresonance</td><td rowspan=1 colspan=1>Linearizedmap Mm atresonance</td><td rowspan=1 colspan=1>Fixed pts oftrue Mm offresonance,E&gt;0</td><td rowspan=1 colspan=1>Fixed pts oftrue Mm offresonance,E&lt;0</td><td rowspan=1 colspan=1>Normalform</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>三</td><td rowspan=1 colspan=1>三</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Eq²+q3+p²</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>三</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>Eq²+q4+p²</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Eq²+q³-qp²</td></tr><tr><td rowspan=1 colspan=1>4a</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>村</td><td rowspan=1 colspan=1>EI+Cl²+al² sin(4Φ)IC| &gt;|alcase</td></tr><tr><td rowspan=1 colspan=1>4b</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EI+CI²+al²sin(4Φ)IC|&lt;|a|case</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EI+CI²al5/12 sin(5Φ)</td></tr><tr><td rowspan=1 colspan=1>&gt;5</td><td rowspan=1 colspan=5>Natural extension of case 5</td></tr></table>

In the same way, we can refer to the nth-order resonance as a period n-ling bifurcation.It is common for the period doubling of a stable periodic orbit to be followed by a cascade of successive period doublings of the stable periodicorbitsesultingfromeachbifurcation.Thiseventhasbeen analysed byountis (1981),reeneetal.(981)andCollt,ckd Koch (1981) for area-preserving maps, though its scaling properties were first studied in dissipative maps by Feigenbaum (1978,1979). In a finite parameter range (energy in Poincare sections), there occurs an infinite number of bifurcations,resulting inan infinitenumber ofunstable periodic orbits of arbitrarily high period. The previously stable region thus turns into a domain of hyperbolic chaotic motion,as studied in chapter 3.For disipative maps this is often refered toas the‘universal route to chaos' We have seen that it is not the only route for conservative maps, where chaotic motion may appear through the homoclinic bifurcation.

The situation for the quadratic map (4.57) is illustrative. For low values of the parameter $\alpha .$ there is anellipticfixed point,as wellasthehyrbolic fixed pointattheorigin(fig4.1o)Tisstarts toundergoperiod-doubling bifurcations for $\alpha > \alpha _ { 0 } \simeq 1 . 6 7$ Howeveromereolinc windings of the separatrices have already swept away practically allthe invariant curves surrounding the stable point. Thus, in this case perioddoubling bifurcations appearonlyasafinal step in the path tocompletely chaotic motion.

Meyer classified all the generic bifurcations of periodic orbits in area-preserving maps,that is,for all periodic orbits with ‘nothing special about them.Does the classification apply to the reversible maps introduced in section 2.5,or to maps with other symmetries? We found there that an inversion Ric $\mathbf { R } \mathbf { R } = \mathbf { 1 }$ , is invariant with respect to a coordinate transformation. So if a map has,saya reflection symmetryits al form will also have an inversion symmetry.Furthermore, this symmetry is asymptotic to a reflection for points close to the origin,because the normal-form transformation reduces there to the identity. Therefore,only symmetric terms of the normal form will have nonzero coefficients. Symmetries may therefore cancel the generic resonant term of the normal form. We must then look for the lowest resonant terms that are not cancelled,obtaining in this way a resonant normal form for the symmetric orbit,as in Aguiar,Malta, Baranger and Davies (1987).

# Exercises

1. Show that a single reflection symmetry does not alter the normal form for resonances of order $n \geq 3$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/3f6793d71ac32712264bb626547b6601a91fda4768b7f38ce990693ea74eb9c2.jpg)  
Fig/4.10Orbits of the quadratic map (4.57) for $\alpha = 0 . 2$ (a) and $\alpha = 0 . 9$ (b).

2. Show that a pair of reflection symmetries cancels the coefficient of the lowest resonant term for $n = 3$ .The symmetric resonant normal-form Hamiltonian haslevelcurves resembling the sixth-orderresonance,but there are two pairs of satellite orbits of period three.

Whatever the symmetry properties of the map, the possibilities for a bifurcation are limited by a geometric constraint: The Poincaré index of a closed curve $C$ that passes no fixed points is defined by Greene et al. (1981)as the number of times that the vector $\mathbf { T } ( \mathbf { x } ) - \mathbf { x }$ encircles the origin as $\mathbf { x }$ traverses $C$ ,taken to be positive or negative,respectively，as the encirclement and traversal are in the same or in opposite directions. For example, the index of a small curve around a single ordinary hyperbolic, eliptic or inversion hyperbolicpoint isespectively1,or1.rided that $C$ crosses no fixed points,the index is a continuous function of $C$ Being integer-valued,it must be constant. Thus,we speak of the inex of a fixed point, meaning the index of any closed curve surrounding it and no other fixed points. The index is summable-that is, the index of a curve,formed by traversing first one and then another curve, is the sum of the separate indices,so the index of any curve is the sum of the indices of the fixed points that it contains. Continuity of the map in its parameter then implies that the sum of the indices of the fixed points ina given region is constant as the parameter is varied, so long as none of them crosses the boundary of the chosen region. This limits the ways in which bifurcations can take place.

# Exercise

Show that in a period $n$ ling bifurcation, ith $n > 2 ,$ elliptic and ordinary hyperbolic orbits must be created in pairs, whatever the symmetry constraints.

# Maps on the circle

The motion along thin tori surrounding stable periodic orbits in the Birkhoff approximation was studied in section 1.3. The Poincare maps on such tori are translations of the circle (rotations). According to the analysis in section 4.4, the periodic Birkhoff tori and their neighbours are broken up by the nearly resonant terms of the Hamiltonian, which generate small denominators in the normal-form transformation. Even so, the survival of nonperiodic tori is not excluded, as will be confirmed by the theorem of Kolmogorov,Arnold and Moser in chapter 6. Understanding the motion near stable periodic orbits thus requires a preliminary study of general motion on tori, or their Poincare sections-maps on the circle.

There is a didactic incentive that perhaps even outweighs the abovementioned physical motivation for the study of circle maps. In the context of these maps,many of the mathematical difficulties that beset the analysis of stable motion manifest themselves in their clearest, simplest form. We will analyse the effect of the near commensurability of frequencies, that is,rational rotation numbers. The attempt to reduce general maps to rotations leads once again to small denominators. Convergence in their presence is possible,but this result is so surprising that considerable effort will be spent in sketching proof.

# 5.1 The rotation number

Consider the general dynamical system

$$
\begin{array} { r } { \Dot { \theta } = \omega ( \theta ) , } \end{array}
$$

defined on the two-dimensional torus O≤0,≤2π. The orbils are given by

$$
\cfrac { d \theta _ { 2 } } { d \theta _ { 1 } } = \cfrac { \omega _ { 2 } ( \pmb { \theta } ) } { \omega _ { 1 } ( \pmb { \theta } ) }
$$

if ω(0)≠0. The Poincaré map T:02→02 associates to each point 02 (and 01=0) the solution of (5.2)for01 =2π (fig5.1).This diffeomorpism

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/da41fa00ca982adefb532d0399ab203439dfcad13c9e3f9c54483c0f8c04c0f1.jpg)  
Fig 5.1.The Poincare map associates to each point $\theta _ { 2 0 }$ the intersection of its orbifwith the line $\theta _ { 1 } = 2 \pi$

can always be written in the form

$$
T \theta = \theta + F ( \theta ) ,
$$

dropping the index of $\theta _ { 2 }$ . The angular function $f ( \theta )$ satisfies

$$
F ( \theta + 2 \pi ) = F ( \theta ) \qquad \mathrm { a n d } \qquad d F / d \theta > - 1 .
$$

The rotation number for the map $T$ is defined as

$$
\mu = { \frac { 1 } { 2 \pi } } \operatorname* { l i m } _ { k \to \infty } { \frac { F ( \theta ) + F ( T \theta ) + \cdots + F ( T ^ { k - 1 } \theta ) } { k } } .
$$

In the case where $T$ is a rotation, $2 \pi \mu$ will therefore be just the rotation angle. It is important to show that the above limit exists and that it is independent of $\theta$ .The following proof is borrowed from Arnold (1982).

Let us consider the angle by which the point $\theta$ is rotated under the kth power of the map $T$ ：

$$
F _ { k } ( \theta ) = F ( \theta ) , + F ( T \theta ) + \cdots + F ( T ^ { k - 1 } \theta ) .
$$

Since T(0+2π)= T(0)+2π and hence T(0+2π)= T(0)+2π,it follows that,if $| \theta _ { 1 } - \theta _ { 2 } | < 2 \pi$ then

$$
| F _ { k } ( \theta _ { 1 } ) - F _ { k } ( \theta _ { 2 } ) | < 2 \pi .
$$

Furthermore,because Fk is 2π-periodic,we can add any multiple of 2π to either0or02,sothatinfact(5.7)holds forany0and02.Takingnow m to be the integer for which

$$
2 \pi m _ { k } \leq F _ { k } ( 0 ) \leq 2 \pi ( m _ { k } + 1 ) ,
$$

we obtain from (5.7)

$$
| F _ { k } ( \theta ) - 2 \pi m _ { k } | < 4 \pi
$$

and hence

$$
\left| \frac { F _ { k } ( \theta ) } { 2 \pi k } - \frac { m _ { k } } { k } \right| < \frac { 2 } { k } .
$$

So far we have shown only that $F _ { k } / 2 \pi k$ is contained in an interval $\sigma _ { k } = ( ( m _ { k } - 2 ) / k , ~ ( m _ { k } + 2 ) / k ) ,$ ，which vanishes with $k ^ { - 1 }$ . This does not necessarily imply that $m _ { k } / k$ has a constant limit. However,we now note t

$$
\frac { F _ { k l } ( \theta ) } { 2 \pi k l } { = } \frac { 1 } { l } \sum _ { i = 0 } ^ { l - 1 } \frac { F _ { k } ( T ^ { i } \theta ) } { 2 \pi k } .
$$

Each of the terms $F _ { k } ( T ^ { i } \theta ) / 2 \pi k$ is contained in the interval $\sigma _ { k }$ ,so that

$$
\left| \frac { F _ { k l } ( \theta ) } { 2 \pi k l } - \frac { m _ { k } } { k } \right| < \frac { 2 } { k } .
$$

Now $F _ { \kappa l } ( \theta ) / 2 \pi k l$ also belongs to the interval $\sigma _ { i } ,$ which tends to zero with $l ^ { - 1 }$ It follows that all pairs of intervals $\sigma _ { k }$ and $\sigma _ { t }$ intersect one another. Since they both tend to zero,the unique common point of intersection is the rotation number itself.

An immediate corollary is that a map with a periodic orbit must have a rational rotation number.Afterall,if $\theta _ { 0 }$ returns after $r$ iterations,itsimage on a periodic straight line under $T ^ { r }$ will be $\theta _ { 0 } + 2 \pi s ,$ where $s$ is an integer. Therefore, $F _ { l r } ( \theta _ { 0 } ) = 2 \pi s l$ for all $l ,$ so the rotation number is just $s / r$ Conversely, if $F _ { r } ( \theta ) > 2 \pi s$ for all $\theta$ ，we cannot have $s / r$ as the rotation number, the same being the case if $F _ { r } ( \theta )$ is always smaller than $2 \pi s .$ Therefore, $\mu = s / r$ implies that $F _ { r } ( \theta ) = 2 \pi s$ for some 0. Thus, a rational rotation number always implies the existence of at least one periodic orbit.

If the rotation number is irrational, the map has no periodic orbit. This means that, for all0, F,(0)>2πs, if μ>s/r, no matter how good an approximation $s / r$ may be to $\mu$ For each $\theta$ the order of the points (0,T0,...,T\*0) on the circle is the same as for the irrational rotation 2πμ. Otherwise, the switching of the order of 0 and T0 in an interval (01,02) would imply the existence of a periodic orbit in this interval.

# 5.2 Reduction of circle maps to rotations

We have seen how an irrational rotation number imposes a strong restrictionona diferentiable mapping.It is therefore plausible that there exists a coordinate transformation that reduces the map to a mere rotation. This is indeed the content of Denjoy's theorem (see Arnold,1982,or Guckenheimer and Holmes1983fora proof): Ifa twice-differentiable diffeomorphism of the circle has an irrational rotation number $\mu$ it is topologically equivalent to a rotation of the circle by the angle $2 \pi \mu$

There exists then a continuous transformation capable of reducing the map to a rotation,but this transformation is not necessarily differentiable. Denjoy's theorem is somewhat analogous to the Hartman-Grobman theorem. The latter guarantees a local topological equivalence between a map in the neighbourhood of a hyperbolic point and its linearization, whereas the former guarantees a global equivalence for circle maps. In both cases,a problem arises only if we insist that the transformations be differentiable.

Surprisingly, perhaps, there is another theorem (Arnold, 1982) which asserts that only diffeomorphisms of the circle with rational rotation numbers are structurally stable. A sufficient condition for this is that all the periodic orbits be nondegenerate, that is, that the derivative of the rth powers of the map be nonzero. In other words, if we consider a one-parameter family of maps, a map with nondegenerate periodic orbits is topologically equivalent to all the maps in a given neighbourhood. All of these must have the same rotation number. Conversely the neighbourhood of a map with an irrational rotation number will contain maps that do not coincide with it under any coordinate transformation. Let $\alpha$ be the parameter; then μ(α) is a function that is constant for some interval of $\alpha$ at every rational value of $\mu$ Since the rational numbers are dense among the real numbers, it is appropriate to wonder whether there are any points α for which μ(α) is irrational. If the answer is negative, then $\mu ( \alpha )$ will have a graph that is a staircase with finite irregular steps. Otherwise, the values of $\alpha$ for which $\mu ( \alpha )$ are irrational form a Cantor set. The graph of $\mu ( \alpha )$ will then be a devil's staircase with infinitely small steps, as described by Mandelbrot (1982).

In this confusing situation it is best to analyse a concrete example (Arnold, 1965):

$$
T _ { \alpha } ( \theta ) = \theta + \alpha + \varepsilon \sin \theta
$$

in the limit where $\varepsilon \to 0$ .We proceed by determining the region in the $( \alpha , \varepsilon )$ plane, for which there exists a periodic orbit of period μ = s/r. For ε = 0,

there is just the single point α =2πs/r.Thus, we seek the small parameters εand $\alpha ^ { \prime } = \alpha - 2 \pi s / r _ { \mathrm { ~ ~ } }$ for which the equation

$$
\theta = T ^ { r } ( \theta ) = \theta + 2 \pi s + r \alpha ^ { \prime } + \varepsilon \sum _ { j = 0 } ^ { r - 1 } \sin ( T ^ { j } \theta )
$$

has a solution.

For $\mu = 1$ , (5.14) reduces to

$$
0 = \alpha ^ { \prime } + \varepsilon \sin \theta ,
$$

wherefore the straight segments

$$
| { \boldsymbol { \alpha } } ^ { \prime } | = \varepsilon
$$

bound the region with $\mu = 1$ (or 0). For $\mu = \textstyle { \frac { 1 } { 2 } }$ ,(5.14) becomes

$$
0 = 2 \alpha ^ { \prime } + \varepsilon \sin \theta + \varepsilon \sin ( \theta + \pi + \alpha ^ { \prime } + \varepsilon \sin \theta ) .
$$

Expanding the last term around $\theta + \pi$ ,we obtain

$$
( 2 - \varepsilon \cos \theta ) \alpha ^ { \prime } = ( \varepsilon ^ { 2 } / 2 ) \sin 2 \theta .
$$

Thus,as $\varepsilon \to 0 .$ we have the condition

$$
\vert x ^ { \prime } \vert \leq \varepsilon ^ { 2 } / 4 .
$$

# Exercise

Show that the equation for an orbit of period 3 reduces to

$$
3 \alpha ^ { \prime } - \sin ( 2 \pi / 3 ) \varepsilon ^ { 2 } = - \varepsilon ^ { 3 } \cos ( \theta + 4 \pi / 3 ) \cos ( \theta + 2 \pi / 3 ) \sin \theta
$$

and hence the condition for a periodic orbit is just

$$
| \alpha ^ { \prime } - \dot { \varepsilon } ^ { 2 } / 2 \sqrt { 3 } | \leq \varepsilon ^ { 3 } / 4 .
$$

The regions of the $( x , \varepsilon )$ plane where the rotation number is 1, ${ \frac { 1 } { 2 } } , \ { \frac { 1 } { 3 } }$ and $\textstyle { \frac { 2 } { 3 } }$ are indicated in figS.2For $r > 1$ they touch the $x$ axis in a cusp, which becomes narrower as r increases. For larger $r$ we still find that the interval of $\alpha$ for which the map has rotation number $s / r$ is $O ( \varepsilon ^ { r } )$ Since $1 \leq s < r$ ,there are $r - 1$ such intervals; the total length of the regions where $\mu$ is rational is of order $\varepsilon + \varepsilon ^ { 2 } + 2 \varepsilon ^ { 3 } + \cdots$ ,a convergent series the sum of which vanishes as $\varepsilon \to 0$ . Thus, in this case the parameters $\alpha .$ for which the map has an irrational rotation number,form a Cantor set with finite Lebesgue measure. The function $\mu ( \alpha )$ is a devil's staircase. Even so, any interval of $\alpha$ will be crossed by the ‘tongues' in fig. 5.2,where $\mu$ is rational, sono map withanirrational rotation number is structuraly stable.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/8747596d593134235da85a09bcbe53794544fc20f5860839db5cf04948439091.jpg)  
Fig.5.2. The ‘tongues', which reach down to the rational numbers on the $x$ axis, are thg parameter ranges with the given rational rotation numbers. The ‘tongues’ become thinner as the rational denominators increase.

/We have seen that the parameter $x / 2 \pi$ need not coincide with the fotation number, even though the function $f ( \theta ) = \varepsilon \sin \theta$ satisfies

$$
\int _ { 0 } ^ { 2 \pi } f ( \theta ) d \theta = 0 .
$$

However, for maps with irrational rotation numbers, $\alpha / 2 \pi$ is indeed the rotation number. In these cases Denjoy's theorem guarantees that the map can be transformed into a rotation for which time averages and configurational averages coincide, so $\bar { f } ( \theta ) = 0$ .The definition (5.5) of the rotation number is just the average of $| x + f ( \theta ) | / 2 \pi$ ,so the rotation number is exactly $\alpha / 2 \pi$ Conversely, if $x / 2 \pi$ is an irrational rotation number, then $\int f ( \theta )$ has zero average in a map with the form of (5.13). The picture is then that, for each irrational number times $2 \pi$ along the line $\varepsilon = 0$ in fig. 5.2, there is a vertical segment along which the map has the same irrational rotation number. The height of this segment will be limited by some spreading ‘rational tongue'.

The possibility that $T _ { \alpha }$ has an irrational rotation number depends on $\alpha$ being ‘suficiently irrational’ in some sense. Denjoy's theorem then guarantees that a homeomorphism will turn $T _ { \alpha }$ into a mere rotation. In section 5.4 we will find that for sufficiently small ε there may even be analytic reductions of $T _ { \alpha }$ into a rotation. However, we must first examine more closely this concept of being ‘sufficiently irrational'.

# 5.3 Approximating irrational numbers by rational numbers

Irrational numbers can be approximated by rational numbers to arbitrarily high accuracy. For example $\pi$ is approximated by the sequence

$$
{ \frac { s } { r } } = { \frac { 3 } { 1 } } , { \frac { 3 1 } { 1 0 } } , { \frac { 3 1 4 } { 1 0 0 } } , { \frac { 3 1 4 2 } { 1 0 0 0 } } , { \frac { 3 1 4 1 6 } { 1 0 0 0 0 } } , . . . ,
$$

which provides better approximations as $r$ increases. Thus, for decimal approximations we obtain

$$
\left| \mu - { \frac { s } { r } } \right| < { \frac { 1 } { r } } ,
$$

with $r _ { n } = 1 0 ^ { n }$ ,and a similar inequality holds for any other basis.

For a finite sequence of $n$ terms, some bases will lead to better approximations than others, but extending the sequence to higher terms we find that this advantage will be reversed in favour of another basis. Thus, it is worthwhile to look for a basis-independent sequence, such as the sequence of continued fractions:

$$
\mu _ { n } = a _ { 0 } + \frac { 1 } { a _ { 1 } } +
$$

$$
+ { \frac { 1 } { a _ { n } } } .
$$

These approximants

$$
\mu _ { n } = s _ { n } / r _ { n }
$$

obey the following recursion relation,

$$
\begin{array} { r l } { { } } & { { S _ { n } = a _ { n } S _ { n - 1 } + s _ { n - 2 } , } } \\ { { } } & { { } } \\ { { } } & { { r _ { n } = a _ { n } r _ { n - 1 } + r _ { n - 2 } , } } \end{array}
$$

for $n \geq 2$

This result is demonstrated in Khinchin (1963), a source of many other important results on continued fractions. We proceed by induction, supposing that (5.27) holds up to order $n - 1$ Defining

$$
{ \frac { S _ { n - 1 } ^ { ' } } { r _ { n - 1 } ^ { ' } } } = a _ { 1 } + { \frac { 1 } { a _ { 2 } } } \nonumber _ { + }
$$

$$
+ \frac { 1 } { a _ { n } } ,
$$

we have

$$
\begin{array} { l } { { S _ { n } = a _ { 0 } S _ { n - 1 } ^ { ' } + r _ { n - 1 } ^ { ' } , } } \\ { { \qquad r _ { n } = s _ { n - 1 } ^ { \prime } } } \end{array}
$$

and by hypothesis

$$
\begin{array} { l } { { S _ { n - 1 } ^ { \prime } = a _ { n } s _ { n - 2 } ^ { \prime } + s _ { n - 3 } ^ { \prime } , } } \\ { { \qquad r _ { n - 1 } ^ { \prime } = a _ { n } r _ { n - 2 } ^ { \prime } + r _ { n - 3 } ^ { \prime } . } } \end{array}
$$

Introducing (530)into(5.29)andrearrnging theterms,weimmdiately retrieve (5.27),which evidently odsor $n = 2$

The sequence of integers $a _ { n }$ determines the sequence of approximants $( r _ { n } , s _ { n } )$ Consider the graphical construction,presented in Arnold (1982) and showninfig.3wiche $( r _ { n } , s _ { n } )$ are pictured as the integer coordinates of points on the plane. The real numbers are associated with the slope of straight lines passing through the origin. Thus,an irrational number corresppnds to a straight line that avoids al the points on the integer lattice in fig.5.3.A good sequence of approximants to the irrational number $\mu$ is the sequence of vectors $\mathbf { v } _ { n } = ( r _ { n } , S _ { n } )$ ,which starts with $\mathbf { v } _ { 0 } = ( 1 , 0 )$ and $\mathbf { v } _ { 1 } = ( 0 , 1 )$ .Vectors ${ \bf v } _ { n }$ are obtained by adding to $\mathbf { v } _ { n - 2 }$ the vector $\mathbf { v } _ { n - 1 }$ multiplied by the largest integer $a _ { n }$ for which $\begin{array} { r } { \mathbf { v } _ { n } = a _ { n } \mathbf { v } _ { n - 1 } - \mathbf { v } _ { n } } \end{array}$ still remains on the same side of the straight line as $\mathbf { v } _ { n - 2 }$ . The resulting approximant $( r _ { n } , s _ { n } )$ satisfies the recursion relation (5.27); hence, the sequence $a _ { 0 } , a _ { 1 } , \ldots$ determines its unique continued-fraction representation. In the limit where $n  \infty$ we obtain the irrational number as an infinite continued fraction.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/df3dbeda84ccbf357238a19a003ace95a81d4eb8b294d79596eaf8c8e8a733fa.jpg)  
Fig.5.3.JThe sequence of vectors $\mathbf { v } _ { n }$ supplies ideal approximations to the irrational slope of the straight line.

How do the continued-fraction approximations compare with those depending on a basis? The difference between two approximants $\mu _ { n }$ and $\mu _ { n + 1 }$ is

$$
\left| { \frac { s _ { n } } { r _ { n } } } - { \frac { s _ { n + 1 } } { r _ { n + 1 } } } \right| = \left| { \frac { s _ { n } r _ { n + 1 } - s _ { n + 1 } r _ { n } } { r _ { n } r _ { n + 1 } } } \right| = { \frac { 1 } { r _ { n } r _ { n + 1 } } } ,
$$

since the numerator of the second term is the area of the parallelogram formed by the vectors ${ \bf v } _ { n }$ and $\mathbf { v } _ { n + 1 } .$ This area is 1 for the pair $\left( \mathbf { v } _ { 0 } , \mathbf { v } _ { 1 } \right)$ and successive parallelograms have a common side and the same height. The approximants are alternately greater and smaller than $\mu$ and $r _ { n + 1 } \geq r _ { n }$ so they all satisfy the inequality

$$
\left| \mu - { \frac { s } { r } } \right| < { \frac { 1 } { r ^ { 2 } } } .
$$

Thus,the continued-fraction sequence converges much more rapidly onto an irrational number than any basis-dependent sequence. The larger the numbers $a _ { n }$ ,the beter e vrgence;terlle $a _ { n } = \infty$ if $\mu$ is a rational number. In contrast,the hardest number to approximate by rationals is the golden mean,

$$
\mu = { \cfrac { 1 } { 1 + { \cfrac { 1 } { 1 + } } } } = { \cfrac { \sqrt { 5 } - 1 } { 2 } } .
$$

Can we find a sequence of approximants satisfying even more favourable Diophantine conditions than (5.32)? The answer is that (5.32) is the best that can be guaranteed uniformly for all the real numbers.This follows from the result that, for most numbers μ in the interval [O,1] and for all o >0, there exists a number $K ( \mu , \sigma )$ such that

$$
\left| \mu - { \frac { s } { r } } \right| \geq { \frac { K } { r ^ { 2 + \sigma } } }
$$

for all pairs of integers (r,s). Any infinite sequence of approximants for μ must have $r _ { n } \to \infty$ ,so that beyond acertain element $K / r _ { n } ^ { 2 + \sigma } > 1 / r _ { n } ^ { 2 + \sigma ^ { \prime } }$ ， whatever the number $K$ .Therefore, since $0 < \sigma ^ { \prime } \leq \sigma$ and $o$ can be made as small as we like, the numbers satisfying the Diophantine conditions (5.34) cannot be approximated to better accuracy than (5.32).

To demonstrate (5.34) we first fix $s$ and $r$ .Consider now the set of numbers $\mu$ for which these inequalities are violated. They form an interval of length $2 K / r ^ { 2 + \sigma }$ The union of all these intervals with the same $r$ hasa total length equal to or smaller than $2 K / r ^ { 1 + \sigma }$ since $s \leq r$ Summing over all the $r$ s we obtain a set, the Lebesgue measure of which is $C K$ where

$$
C = 2 \sum _ { r = 1 } ^ { \infty } r ^ { - ( 1 + \sigma ) } < \infty .
$$

By choosing $K$ arbitrarily small, we make the measure of the set of points that violates (5.34) as small as we like. Thus,the set of numbers that infringes these Diophantine conditions for any $K$ has zero measure.

The numbers that satisfy the conditions (5.34) for a given pair of $\sigma > 0$ and $K > 0$ are known as numbers of type $( K , \sigma )$ This is the basis for the vague concept of ‘suficiently irrational’ used inthe previous sections; that is,the numbers of type $( K , \sigma )$ with larger maximal $K$ or smaller minimal $\sigma$ may be thought of as the more irrational'.

# 5.4 Kolmogorov's method

According to Denjoy's theorem, a map with an irrational rotation number is always conjugate to a rotation by a homeomorphism. Just as with the Hartman-Grobman theorem, the proof is nonconstructive, so we now seek the required transformation in a manner analogous to the method of normal forms, that is, by iterated simplifications.

Consider a map of the form

$$
\theta  T \theta = \theta + 2 \pi \mu + f ( \theta ) .
$$

As we saw in section 5.2, the only requirement on $f ( \theta )$ for the irrational parameter $\mu$ to be the rotation number is that this function have zero

average. We will also suppose that $f ( \theta )$ is an analytic periodic function in the strip $| \operatorname { I m } \theta | < \rho$ of the complex plane, where

$$
\operatorname* { s u p } \lvert f ( \theta ) \rvert \equiv \lVert f \rVert _ { \rho } < \varepsilon .
$$

# Exercise

Determine the bound on the function $f ( \theta )$ in (5.13) for the strip $| \operatorname { I m } \theta | < \rho$

We now seek a diffeomorphism

$$
\phi  G \phi = \phi + g ( \phi ) = \theta ,
$$

which brings the map $T$ to the rotation $\upsilon$ (by the angle $2 \pi \mu )$ . Thus,G satisfies

$$
T \cdot G \phi = G \cdot U \phi ,
$$

leading to the functional equation

$$
g ( \phi + 2 \pi \mu ) - g ( \phi ) = f ( \phi + g ( \phi ) ) .
$$

The problem is to establish for what rotation numbers (5.40) has a solution.

If $f$ is of order ε,it isplausible tat $g$ is too. So expanding $f ,$ we obtain as a first approximation to $\textbf { G }$ the transformation

$$
\phi  G _ { 0 } \phi = \phi + g ^ { 0 } ( \phi ) = \theta ,
$$

where the function $g ^ { 0 } ( \phi )$ satisfies the equation

$$
g ^ { 0 } ( \phi + 2 \pi \mu ) - g ^ { 0 } ( \phi ) = f ( \phi ) .
$$

If we expand $f ( \phi )$ and $g ^ { 0 } ( \phi )$ in Fourier series,

and

$$
\begin{array} { l } { { f ( \phi ) = \displaystyle \sum _ { l } f _ { l } \exp ( i l \phi ) } } \\ { { \displaystyle g ^ { 0 } ( \phi ) = \sum _ { l } g _ { l } ^ { 0 } \exp ( i l \phi ) , } } \end{array}
$$

equation (5.42) reduces to

$$
\sum _ { l } g _ { l } ^ { 0 } \left[ \exp ( i 2 \pi l \mu ) - 1 \right] \exp ( i l \phi ) = \sum _ { l } f _ { l } \exp ( i l \phi ) ,
$$

with the formal solution

$$
g _ { l } ^ { 0 } = { \frac { f _ { l } } { \exp ( \mathrm { i } 2 \pi l \mu ) - 1 } } .
$$

There is no exact resonance among the coeficients,because the tion number was assumed irrational. However, there will be arbitrarily small denominators on the right side,just as with the normal forms of chapter 4. We have now developed the tools with which to tackle such a tricky convergence problem. If $\mu$ is of type $( K , \sigma )$ ,that is,itsatisfies the Diophantine conditions (5.34), the distance of lμ to the nearest integer is greater than K//1 +o. The numbers 1 and exp(i2πlμ) are separated by the arc $2 \pi l \mu$ along the unit circle. We seek a lower bound for the length of the chord that joins them.Since the minimum ratio between chord and arc is $2 / \pi$ ,the former satisfies the inequality

$$
| \exp ( i 2 \pi l \mu ) - 1 | \geq \frac { 2 } { \pi } ( 2 \pi l \mu ) \geq \frac { 4 K } { | l | ^ { 1 + \sigma } } .
$$

The convergence of the Fourier series for $g ^ { \mathrm { o } } ( \phi )$ depends on the exponential decay of thecoeficients $f _ { l }$ being capable of dominating the powerlawdecayofthedenominatorsallowedby(5.46).Thiscanbeshown directly from the definition

$$
\begin{array} { r } { f _ { l } = ( 2 \pi ) ^ { - 1 } \displaystyle \int _ { 0 } ^ { 2 \pi } f ( \phi ) \exp ( - i l \phi ) d \phi . } \end{array}
$$

We can move the path of integration to $\operatorname { I m } \phi = - \rho$ for $l > 0$ ,since $f$ is analytic in a strip of this width and the vertical integrals along $\mathbf { R e } \phi = 0$ and $2 \pi$ cancel each other. Thus,

$$
f _ { l } = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 1 2 \pi } f ( \phi - i \rho ) \exp ( - i l \phi - l \rho ) d \phi \leq \varepsilon \exp ( - | l | \rho ) ,
$$

using (5.37).Converselyfor a given sequence of coecents $f _ { l }$ satisfying (5.48),we can guarantee that the corresponding Fourier series converges to an analytic function $f ( \phi )$ in a strip of width $2 \rho$ .We can even determine a bound on $g ^ { 0 } ( \phi )$ in the narrower strip of width $2 ( \rho - \delta )$

$$
\begin{array} { r l } {  { \| g ^ { 0 } \| _ { \rho - \delta } \le \sum _ { l } ( \varepsilon / 4 K ) | l | ^ { 1 + \sigma } \exp ( - | l | \rho ) | \exp ( i l \phi ) | } } \\ & { \le ( \varepsilon / 4 K ) \sum _ { l } | l | ^ { 2 } \exp ( - | l | \rho ) \exp [ | l | ( \rho - \delta ) ] } \\ & { = \frac { \varepsilon } { 4 K } \frac { d ^ { 2 } } { d \delta ^ { 2 } } \sum _ { l } \exp ( - | l | \delta ) } \\ & { \le \frac { 2 \varepsilon } { 4 K } \frac { d ^ { 2 } } { d \delta ^ { 2 } } \frac { 1 } { 1 - \exp ( - \delta ) } \le \varepsilon D \delta ^ { - 3 } , } \end{array}
$$

assuming that $\sigma < 1$ and $\delta < 1$ .Using more delicate majorations Arnold

(1982) obtains the norm

$$
\| g ^ { 0 } \| _ { \rho - \delta } \leq \varepsilon C \delta ^ { - 2 - \sigma } ,
$$

in which the number $C$ [like $D$ in (5.49)] depends only on $K$ and $\sigma$

The transformation $G _ { 0 }$ reduces $T$ to a rotation up to order $\varepsilon ^ { 2 }$ In analogy to the theory of normal forms, we can attempt to eliminate the difference between $T$ and a rotation up to order $\varepsilon ^ { 3 }$ and so on. The problem is the difficulty of demonstrating the convergence of this procedure.

A fruitful alternative method was proposed by Kolmogorov (1954): Instead of eliminating terms of higher and higher order, we apply the same procedure as described above to $T _ { 1 }$ ,the result of the transformation $G _ { 0 }$ on $T _ { \parallel }$ This produces a new transformation $G _ { 1 }$ and so on. The convergence is improved, in exact analogy to Newton's method, for determining the roots of a function. This consists of linearizing the function $f ( x )$ about the point $x _ { 0 }$ ,yielding a first approximation $x _ { 1 }$ to the root of $f ( x )$ (fig.5.4). Instead of seeking to improve this approximation by taking the quadratic expansion of $f ( x )$ about $x _ { 0 }$ , we now take a new linear approximation about $x _ { 1 }$ ， and this process is iterated indefinitely. It is readily verified that the nth approximation $f ( x _ { n } ) = O ( \varepsilon ^ { 2 n } ) ,$ instead of $O ( \varepsilon ^ { n } )$ obtained for approximations by a power series.

We therefore construct the transformation

$$
T _ { 1 } = G _ { 0 } ^ { - 1 } \cdot T \cdot G _ { 0 } ;
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/7db81ba5df594f23e5bfa517ba00c5f9da118b1b4bd619a41d94f02d995ce4e3.jpg)  
Fig.5.4.jNewton's method for finding the root of a function relies on iterating linear approximations and so converges much better than making polynomial approximations at a fixed initial point.

that is,T is the transformation Tviewed withthe coordinates  defined by (5.41). If we substituted G for G, in (5.51), T would be the rotation $U$ The problem is now to quantify the statement that ， $T _ { 1 }$

$$
\phi  T _ { 1 } \phi \equiv \phi + 2 \pi \mu + f _ { 1 } ( \phi ) ,
$$

is closer to a rotation than T.The residue f1(Φ) between T and U must have zero average just as f(Φ). We estimate fr(Φ) from the relation $G _ { 0 } \cdot T _ { 1 } \phi \equiv T \cdot G _ { 0 } \phi$ ：

$$
\phi + 2 \pi \mu + f _ { 1 } ( \phi ) + g ^ { 0 } ( \phi + 2 \pi \mu + g _ { 1 } ( \phi ) ) \equiv \phi + g ^ { 0 } ( \phi ) + 2 \pi \mu + f ( \phi + g ^ { 0 } ( \phi ) ) .
$$

Hence,

$$
{ \cal f } _ { 1 } ( \phi ) = [ f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) ] - [ g ^ { 0 } ( \phi + 2 \pi \mu + f _ { 1 } ( \phi ) ) - g ^ { 0 } ( \phi + 2 \pi \mu ) ] ,
$$

using (5.42) to rearrange the terms. The mean value theorem provides a norm for the first bracket:

$$
\parallel f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) \parallel _ { \rho - \delta } \leq \parallel d f / d \phi \parallel _ { \rho - \delta } \parallel g ^ { 0 } \parallel _ { \rho - \delta } .
$$

The norm for $d f / d \phi$ is easily shown to be $O ( \varepsilon \delta ^ { - 2 } )$ by proceeding as in (5.49). Together with (5.50), we thus oin

$$
\| f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) \| _ { \rho - \delta } \leq C ^ { \prime } \varepsilon ^ { 2 } \delta ^ { - 5 } .
$$

Careful consideration of the second square bracket in(5.54) yields a similar result; that is, we have

$$
\| f _ { 1 } \| _ { \rho - \delta } \leq C ^ { \prime \prime } \varepsilon ^ { 2 } \delta ^ { - 5 } .
$$

The norm $\parallel f _ { 1 } \parallel$ estimates the ‘error’ in the approximation of $T _ { 1 }$ by $U$ ， a rotation. The order of the “error' doubles at each successive approximation, just as in Newton's method. Still, it is not yet clear that we can iterate indefinitely these approximations, since a finite choice for $\delta$ will ‘eat away’ the convergence strip $\rho$ after a finite number of iterations, whereas any attempt to reduce $\delta$ leads to a small denominator in (5.57). The only way out is to take a diminishing sequence of $\delta _ { n }$ s,suchas

$$
\delta _ { 0 } = \delta < { \textstyle \frac { 1 } { 2 } } , \qquad \delta _ { n } = \delta _ { n - 1 } ^ { 3 / 2 } , \qquad \rho _ { n } = \rho _ { n - 1 } - \delta _ { n - 1 } ,
$$

Then

$$
\sum _ { n } \delta _ { n } < \delta _ { 0 } \sum _ { n } ( \delta _ { 0 } ^ { 1 / 2 } ) ^ { n } < \frac { \rho } { 2 }
$$

if $\delta _ { 0 }$ is sufficiently small.

The final step is to connect the norms $\parallel f _ { n } \parallel$ to the sequence of $\delta _ { n } :$ s.Fora sufficiently large integer $m$ ,we can replace (5.57) by

$$
\begin{array} { r } { \| f _ { 1 } \| _ { \rho - \delta } \leq \varepsilon ^ { 2 } \delta _ { 0 } ^ { - m } . } \end{array}
$$

But $\delta _ { n } \leq \delta _ { 0 }$ , so the residue of successive approximations satisfies

$$
\| f _ { n } \| _ { \rho _ { n } } \leq \| f _ { n - 1 } \| ^ { 2 } \delta _ { n - 1 } ^ { - m } .
$$

The number $^ m$ ,common toalltheinequalities (5.61),depends olyon $\kappa$ and $\sigma$ We now specify

$$
\begin{array} { r } { \varepsilon = \delta _ { 0 } ^ { N } , } \end{array}
$$

where $N$ is chosen large enough for

$$
2 N - m \ge 3 N / 2 .
$$

Thus, using (5.60) and (5.58),

$$
\begin{array} { r } { \| f _ { 1 } \| _ { \rho _ { 1 } } \leq \delta _ { 0 } ^ { 3 N / 2 } = \delta _ { 1 } ^ { N } , } \end{array}
$$

whereas repeated use of (5.61) yields

$$
\begin{array} { r } { \| f _ { n } \| _ { \rho _ { n } } \leq \delta _ { n } ^ { N } . } \end{array}
$$

We have shown that Kolmogorov’s method converges for $\sigma < 1$ and for small enough ε(K). Of course, we could have done the same for $\sigma < 2$ obtaining a smaller estimate for ε. The more delicate majorations in the proof of Arnold (1982)， on which this exposition is based, provide convergence for a much wider range of $\varepsilon ( K , \sigma )$ .The range of convergence is actually much wider still, since Herman (1979) proved that even difeomorphisms not close to rotations can be conjugate to them by a diffeomorphism.

So far it has not been possible to apply Herman's methods to the problems of Hamiltonian dynamics to be studied in thefollowing chapter. The proof of Siegel's theorem also tackles the small-denominator problem, without having to rely on Kolmogorov's method. The later retains its paramount importance as the basis of the theorem of Kolmogorov,Arnold and Moser. For this reason it has been worthwhile to give a full account of it for the simplest relevant application.

Integrable and quasi-integrable systems

In the previous chapter we atained global understanding of a very simple kind of system.We now return to full Hamiltonian systems,but these will be restricted in such a way as to allow a global knowledge of their main characteristics. This class of integrable systems contains all the solved problems in classical mechanics,as well as the truncations of the Birkhoff normal forms studied in chapter 4. We willfind that no limitation need be made on the number of freedoms of an integrable system. In fact, their definition can beextended up to an infinite number offreedoms,leading to the solution of important partial differential equations,but this subectlies beyond the scope of this book.

We start by defining integrable systems and by studying the geometry of their invariant surfaces.This leads tothedefinitionof generalactionangle variables. The consideration of a few simple examples elicits the concept of caustics,that is,singularities of the projections ofinvariant surfaces.We wil discuss briefly Thom and Arnold's classification of some of the simpler generic caustics.

In conclusion we will study perturbations of integrable systems. In section 6.5 we willdiscuss the averaging principle,which is then related toa stationary perturbation theory, reminiscent of the resonant normal forms encountered in section 4.4. This evokes the question of survival of the invariant surfaces of an integrable system after a perturbation, to be answered by the Kolmogorov, Arnold and Moser (KAM theorem). The sketch of its proof relies on that of the analytical reduction of circle maps to rotations presented in section 5.4.

# 6.1 Invariant tori

A necessary condition for a system with $L$ freedoms to be integrable is that it have $L$ independent constants of the motion. The Hamiltonian of an autonomous system $H ( \mathbf { x } )$ is a constant function; therefore, there must be

$L - 1$ other functions with the property that

$$
\frac { d } { d t } F ( \mathbf { x } ( t ) ) = \sum _ { l = 1 } ^ { L } \left( \frac { \partial F } { \partial q _ { l } } \frac { \partial H } { \partial p _ { l } } - \frac { \partial F } { \partial p _ { l } } \frac { \partial H } { \partial q _ { l } } \right) = \left\{ F , H \right\} = 0 ,
$$

where the penultimate term defines the Poisson bracket of the functions F and H.The antisymmetry of the Poisson bracket implies that H will also be a constant of the motion for the Hamiltonian $F$ . A fundamental property (demonstrated in Arnold,1978, sec. 39) is that the flows ${ \bf x } _ { H } ( t )$ and ${ \bf x } _ { F } ( t ^ { \prime } )$ generated by two Hamiltonians that satisfy (6.1) commute: Whichever the order in which we ‘switch on' the Hamiltonian $F$ for the time $t ^ { \prime }$ and $H$ for the time t, the system arrives at the same point $\mathbf { x }$ ,if it started out from the same point $\underline { { \mathbf { x } _ { 0 } } } . 5$

The $L$ constants of the motion must be independent; that is,at each point X the vector fields $\dot { \bf x } _ { i } = \mathcal { \bar { F } } \partial F _ { i } / \partial { \bf x }$ and $\dot { \bf x } _ { j } = \mathcal { F } \boldsymbol { \partial } F _ { j } / \partial { \bf x }$ [with $\mathcal { J }$ given by (1.37)] must be linearly independent. The last condition defining an integrable system is that each pair of functions $F _ { i }$ and $F _ { j }$ be in involution:

$$
\bigl \{ { \cal F } _ { i } , { \cal F } _ { j } \bigr \} = 0 .
$$

This condition encompasss (6.1)if we identify $H ( \mathbf { x } ) = F _ { L } ( \mathbf { x } )$

Each orbit of an integrable system is contained in an $L$ dimensional surface $T _ { s }$ resulting from the multiple intersection of the $L$ surfaces $F _ { j } ( \mathbf { x } ) =$ const, each with $( 2 L - 1 )$ dimensions. The condition of involution guarantees that we would obtain the same invariant surface by choosing any one of the functions $F _ { j } ( \mathbf { x } )$ as the Hamiltonian,or even by choosing any arbitrary function of the $\boldsymbol { F } _ { j }$ s. The $L$ Hamiltonians define $L$ vector fields tangent to $T _ { i }$ because each vector is tangent to an orbit contained in this surface.

Let us consider again equation (6.1). Comparison with (1.38) establishes that the Poisson bracket of two functions $F$ and $H$ is merely the skew product $\dot { \mathbf { X } } _ { F } \wedge \dot { \mathbf { X } } _ { H }$ ,that is, the symplectic area or (reduced) action of the parallelogram formed by these two vectors. The $L$ vectors $\dot { \bf x } _ { t } .$ ,corresponding to the $L$ functions $F _ { t }$ , can be taken as a basis for the tangent plane to the invariant surface $T .$ Hence, the condition of involution implies that the symplectic area is null for any pair of vectors tangent to $T .$ This differential result can evidently be extended to any reducible circuit on T,a property that defines a nul or Lagrangian surface.

Consider now the orbits defined by the L independent vector fields x, starting from an arbitrary point $\mathbf { x } _ { 0 }$ on the surface $T .$ The positions along each orbit result from the action of the one-parameter groups of canonical transformations

$$
G _ { l } ^ { t _ { l } } \mathbf { x } _ { 0 } = \mathbf { x } ( t _ { l } , \mathbf { x } _ { 0 } )
$$

with the properties

$$
G _ { l } ^ { t _ { l } } G _ { l } ^ { s _ { l } } = G _ { l } ^ { t _ { l } + s _ { l } } \qquad \mathrm { a n d } \qquad ( G ^ { t _ { l } } ) ^ { - 1 } = G ^ { - t _ { l } } .
$$

Since these $\mathcal { L }$ groups commute,

$$
G _ { k } ^ { \ell k } G _ { l } ^ { \ell _ { l } } = G _ { l } ^ { t _ { l } } G _ { k } ^ { t _ { k } } ,
$$

we can define the action of the commutative group

$$
\mathbf { G } ^ { t } = G _ { 1 } ^ { t _ { 1 } } \cdots G _ { L } ^ { t _ { L } } ,
$$

with $\mathbf { t } = ( t _ { 1 } , \dots , t _ { L } )$

It is easy to define an invariant measure on $T$ for the motion generated by any of the Hamiltonians $F$ .Each of these preserves the Liouville measure $\delta ( F _ { l } ( \mathbf { x } ) - E _ { l } ) d \mathbf { x } ;$ therefore,

$$
d \mu = \prod _ { l = 1 } ^ { L } \delta ( F _ { l } ( \mathbf { x } ) - E _ { l } ) d \mathbf { x } ,
$$

will be invariant on $T .$ We can thus apply the Poincaré recurrence theorem (section 3.4) to the case of bounded motion, that is, when $T$ is a compact surface. The implication is that,in any neighbourhood of a point $\mathbf { x } _ { 0 } .$ some point $\mathbf { x } _ { 0 } ^ { ' }$ will return to this neighbourhood after some time $t _ { l }$ .For a group of flows that commute, this result can be strengthened: We can bring $\mathbf { x } _ { 0 }$ to $\mathbf { x } _ { 0 } ^ { \prime }$ by means of the action of the element $\mathbf { G } ^ { \alpha \mathfrak { t } }$ of the group $\mathbf { G } ^ { \mathfrak { t } }$ Thus,

$$
G _ { l } ^ { t _ { l } } \mathbf { x } _ { 0 } = \mathbf { G } ^ { - \delta t } G _ { l } ^ { t _ { l } } \mathbf { G } ^ { \delta t } \mathbf { x } _ { 0 }
$$

is a point that has returned close to $\mathbf { x } _ { 0 }$ after the time $t _ { l } ,$ under the flow generated by $F _ { l } .$

We can take the $t _ { l } ^ { \phantom { \dagger } }$ s as coordinates on $T$ by fixing an initial point $\mathbf { x } _ { 0 } ,$ because $\mathbf { G } ^ { t }$ is a commutative group. This arrangement is sketched in fig.6.1 for $L = 2$ within a three-dimensional subspace. Consider the orbit $\gamma _ { 1 }$ of $\mathbf { x } _ { 0 }$ under the action of $F _ { 1 }$ .It returns to $\mathbf { x } _ { 0 } ^ { \prime }$ in a neighbourhood of $\mathbf { x } _ { 0 }$ after a time t. In fact,y1 must intersect the t =Ocoordinate plane in a time t\*.To see this,note that γ returns close to xo,where its velocity xis transverseto this plane. The configuration is sketched in fig6.2afor L=2. If we now switch offFand switch on any one of the other Hamiltonians F,the system will move on a t surface which is a new image of $t _ { 1 } = 0$ But this motion, without any participation of $F _ { \mathrm { ~ 1 ~ } }$ ,determines a plane in the t coordinates, which reduces to a vertical straight line for $L = 2$ (fig.6.2b The plane $t _ { 1 } = t _ { 1 } ^ { * }$ contains a new image of the t origin, $\mathbf { x } _ { 0 }$ .The vector joining the origin to this point generates an irreducible circuit on $T ,$ since reducible curves are. represented by closed loops in the t coordinates.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/226066ab1befa59b2a836ad6d0f617b214497d06d1e6da10cdc85b81f29eee91.jpg)  
Fig6.1. The velocity vectors $D \mathbf { G } ^ { \imath } \mathbf { x } _ { 0 }$ are tangent to the torus and the lines $G _ { l } ^ { t _ { l } } { \bf x } _ { 0 }$ can be used as coordinates on the torus.

By repeating the same procedure for $\gamma _ { 2 }$ ,the curve $G _ { 2 } ^ { t _ { 2 } } \mathbf { X } _ { 0 }$ ,we obtain the image of the coordinate plane $t _ { 2 } = 0$ as a parallel plane with the constant coordinate $t _ { 2 } ^ { * }$ and so on for all the other coordinates. The set of all these planes with $t _ { j } = \pm t _ { j } ^ { * }$ forms an $L$ cube centred on the origin. On each of the $L$ pairs of faces there will be a different image of the origin (Figl6.2b)such that the vector joining it to the origin corresponds to an irreducible circuit on $T ,$ The vectors with tips on $t = \pm t _ { j } ^ { * }$ correspond to the same circuit traversed inoppositesenses,andallthelinearcombinationsofthese vectors supply multiple windings of the irreducible circuits.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/cbc2ed92b1d7fa97dc5427d8b64da6a22d904ecf9bafc7dd57f40fc869eb85a0.jpg)

If the neighbourhood surrounding the origin is chosen to be small, then each image of the origin willbe close to the centre of the cube face,as shown in fig(6.2b.However, $\gamma _ { j }$ may intersect the $t _ { j } = 0$ plane many times just outside this neighbourhood for $t _ { j } < t _ { j } ^ { * }$ . By increasing the size of the neighbourhood we incorporate these intersections, so that the time $t _ { j } ^ { * }$ for the first crossing in the neighbourhood is reduced. The structure is still the same, with the $2 L$ images of the origin lying in the faces of a cube (farther from their centre). If the neighbourhood is sufficiently large (for instance, if it covers uniquely the entire surface $T$ ), we obtain minimum times $t _ { j } ^ { * }$ corresponding to the first traversal of the planes $t _ { j } = 0$

The advantage is that we now obtain the discrete group of all the irreducible circuits on $T _ { \ast }$ If we label the images of the origin on the faces of the cube by $\mathbf { e } _ { t }$ ,then the members of the group are specified by

$$
\mathbf { t } = n _ { 1 } \mathbf { e } _ { 1 } + \cdots + n _ { L } \mathbf { e } _ { L } ,
$$

where $n _ { l }$ is an integer. There can be no other points in this group,because there are none inside the cube by construction and we can bring any point outside to the inside by adding to it one of the vectors tin (6.9). Finally we note that this group is independent of the point $\mathbf { x } _ { 0 }$ , since for any point $\mathbf { x } = \mathbf { G } ^ { \mathrm { r } } \mathbf { x } _ { 0 }$

$$
{ \bf G } ^ { \mathrm { t } } { \bf x } = { \bf G } ^ { \mathrm { t } + \tau } { \bf x } _ { 0 } = { \bf G } ^ { \tau } { \bf x } _ { 0 } = { \bf x } , \quad
$$

for the t's satisfying (6.9). We have thus shown that there are exactly $L$ independent circuits passing through any point of the invariant surface. It follows that $T$ isan $L$ torus, that is,a common torus in the case where $L = 2$

We can now make a linear transformation from the t coordinates to the $\phi$ coordinates,the axes of which are the vectors ${ \bf e } _ { l }$ ,so that $\phi _ { t }$ varies in the interval $( 0 , 2 \pi )$ from the origin to the tip of the vector.In these coordinates $T$ is the Cartesian product of L circles and the movement generated by the Hamiltonian $H ( \mathbf { x } )$ is rectilinear and uniform:

$$
\phi ( t ) = \phi ( 0 ) + \omega t .
$$

We conclude that the motion of an integrable system can be reduced to a translation on a torus, the properties of which were studied in section 1.3. This result constitutes the main content of the Liouville-Arnold theorem. We will conclude its discussion by showing that a canonical transformation can always be found such that the motion on the torus is given by (6.11).

The obvious choice would be to take the L variables Fand L angles Φ as coordinates for an integrable system. The problem is that the transformation $\left( \mathbf { p } , \mathbf { q } \right) \to \left( \mathbf { F } , \phi \right)$ would not be canonical in general,entailing the os of the Hamiltonian form of the system. So we must find new constants of the motion I(F) that are canonically conjugate to the angles $\phi$

The condition for the transformation $( { \bf p } , { \bf q } ) \to ( { \bf I } , \phi )$ to be canonical is that it preserve the symplectic area for any closed loop in phase space:

$$
\oint \mathbf { p } \cdot d \mathbf { q } = \oint \mathbf { I } \cdot d { \boldsymbol { \phi } } .
$$

Since the angles $\phi$ have no dimension, it follows that the new variables I must have the dimension of an action. Each $L$ dimensional torus is characterized by $L$ irreducible circuits. We can therefore associate the $L$ variables Ito the symplectic area of these circuits,as long as all the possible deformations of a given irreducible loop have the same action. This condition is indeed satisfied by the invariant tori of an integrable system, because all the deformations of an irreducible circuit are obtained by adding to it a reducible loop of zero action. We thus define the action variables

$$
I _ { j } = ( 2 \pi ) ^ { - 1 } \oint _ { \gamma _ { j } } { \bf p } \cdot d { \bf q } ,
$$

where $\gamma _ { j }$ is the jth irreducible circuit on the torus. Provided that the Jacobian determinant $\partial \mathbf { I } / \partial \mathbf { F }$ is nonzero, we can sstitute $H ( \mathbf { F } ) = H ( \mathbf { I } )$

It remains to show that the variables conjugate to I are the required angles $\phi$ .To this end we note that the Lagrangian property of the torus implies the existence of the function

$$
S ( \mathbf { q } , \mathbf { I } ) = \int _ { \mathbf { q } _ { 0 } } ^ { \mathbf { q } } \mathbf { p } _ { \mathrm { I } } ( \mathbf { q } ) \cdot d \mathbf { q } .
$$

In a two-dimensional phase space the torus specified by a given I is a closed curve, so that $p _ { I } ( q )$ is an even number of points. Generally the $L$ -dimensional torus also intersects transversely the $L$ dimensional plane q =const in discrete points within the 2L-dimensional phase space. The function S is therefore multivalued. If we choose $S ( \mathbf { q } , \mathbf { I } )$ as the generating function for a canonical transformation $( { \bf p } , { \bf q } )  ( { \bf I } , \phi ^ { \prime } )$ ,the transformation is implicitly given by

$$
\partial S / \partial { \bf q } = { \bf p } , \qquad \partial S / \partial { \bf I } = \phi ^ { \prime } .
$$

For an irreducible circuit of the torus, $\gamma _ { i }$ , the change of the angles $\phi _ { j } ^ { \prime }$ is

simply

$$
( \Delta \phi _ { j } ^ { \prime } ) _ { \gamma _ { i } } = \Delta _ { \gamma _ { i } } \frac { \partial S } { \partial I _ { j } } = \frac { \partial } { \partial I _ { j } } \Delta _ { \gamma _ { i } } S = \frac { \partial } { \partial I _ { j } } 2 \pi I _ { j } = 2 \pi \delta _ { i j } .
$$

So theconjugate angles Φ' =Φj,the privileged angular coordinates on the torus.

The solution of an integrable system can thus be found in principle by determining the canonical transformation $( \mathbf { p } , \mathbf { q } ) \to ( \mathbf { I } , \phi ) .$ ,which is guaranteed to exist. There is no general method for achieving this end, but once the transformation has been found, we obtain Hamilton's equations in the form

$$
{ \dot { \bf I } } = - \frac { \partial H } { \partial \phi } ( { \bf I } ) = 0 , \quad \mathrm { ~ } \mathrm { ~  ~ \bar { \phi } ~ } = \frac { \partial H } { \partial { \bf I } } = { \pmb { \omega } } .
$$

So the motion is given by (6.11), with the frequencies $\omega$ specified by (6.17). Generally the motion will be multiply periodic, admitting the Fourier expansion

$$
\begin{array} { r } { \mathbf { q } ( t ) = \displaystyle \sum _ { \mathbf { m } } \mathbf { q } _ { \mathrm { _ m } } ( \mathbf { I } ) \exp { [ i \mathbf { m } \cdot ( \boldsymbol { \omega } t + \phi _ { 0 } ) ] } , } \\ { \mathbf { p } ( t ) = \displaystyle \sum _ { \mathbf { m } } \mathbf { p } _ { \mathrm { _ m } } ( \mathbf { I } ) \exp { [ i \mathbf { m } \cdot ( \boldsymbol { \omega } t + \phi _ { 0 } ) ] } . } \end{array}
$$

# 6.2 Examples of integrable systems

The simplest case is that of a system with a single freedom and a Hamiltonian)of the form

$$
\textcircled{ H = p ^ { 2 } / 2 m + V ( q ) }
$$

for energies $E < V ( \infty )$ and $E < V ( - \infty )$ The tori are then $p$ -symmetric level curves of the Hamiltonian. The corresponding action variable is just

$$
I = ( 2 \pi ) ^ { - 1 } \oint p d q = \pi ^ { - 1 } \int _ { q _ { 1 } } ^ { q _ { 2 } } d q \big \{ 2 m [ E - V ( q ) ] \big \} ^ { 1 / 2 } ,
$$

where the $q _ { j }$ are the turning points,for which $p = 0$

Example.Thesquare well)a ball rolling freely with speedC between two walls separated by a distanceCdJIt is assumed that the ball has elastic) CcollisionswithtewallTssaeellismorefmlarinquantum mechanics. The action is obtained from fig6.3as

$$
I = ( 2 \pi ) ^ { - 1 } ( \mathrm { a r e a ~ o f ~ r e c t a n g l e } ) = m v d / \pi .
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/157a6e58954cadd24b3fe17b726a905beca2bf558862025e0fd9cf3434b92b9c.jpg)  
Fig6.3Teactiovarbleforesareeisaiedomtheareaf the rectangle in phase space.

Since the corresponding energy is $E = m v ^ { 2 } / 2$ the HamiltonianJis just

$$
\textcircled { H ( I ) = ( \pi I ) ^ { 2 } / ( 2 m d ^ { 2 } ) . }
$$

In this case the angle variable depends linearly on $q$ ,which already has a (piecewise) uniform motion.

# Exercise

Show that the dependence of the Hamiltonian $p ^ { 2 } / 2 m + C \tan ^ { 2 } ( \pi / q )$ on the action variable tends to that of (6.22) in the limit of high energies.

Example. The harmonic oscillator. The Hamiltonian has the form

$$
H ( p , q ) = p ^ { 2 } / 2 + \omega ^ { 2 } q ^ { 2 } / 2 = E .
$$

The level curve is an ellipse with semiaxes $( 2 E ) ^ { 1 / 2 }$ and $( 2 E ) ^ { 1 / 2 } / \omega$ ,so that

$$
I = ( 2 \pi ) ^ { - 1 } ( \mathrm { a r e a ~ o f ~ a n ~ e l l i p s e } ) = E / \omega ,
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/a516672dd362ba02831676f0b122b960b45837dc050ef3390c6f91fc737074df.jpg)  
Fig 6.4. The ratio $\partial \phi / \partial q$ is proportional to the $\delta p$ separating level curves whose actions differ by $\delta I$

that is,

$$
H ( I ) = \omega I .
$$

The angular frequency $\phi = \omega$ is therefore the same for all ellipses.

Of course, this is just the case of linear motion around a stable equilibrium already analysed in chapter 1.Through the canonical rescaling $( p , q ) {  } ( p ^ { \prime } , q ^ { \prime } ) { = } ( \omega ^ { - 1 / 2 } p , \omega ^ { 1 / 2 } q )$ ,the Hamiltonian reduces to the standard form $\omega ( p ^ { \prime 2 } + q ^ { \prime 2 } ) / 2$ .We hence recognize the action-angle variables as the canonical polar coordinates in the $( p ^ { \prime } , q ^ { \prime } )$ plane, defined by (1.49).

The angular variable for a one-freedom system is

$$
\phi ( q ) = \frac { \hat { o } } { \hat { o } I } \int _ { q _ { 0 } } ^ { q } d q p ( q , I )
$$

within an additive constant. We can therefore visualize $\partial \phi / \partial q$ to be proportional to the $\delta p$ separating level curves that haveactions differing by $\delta I \left( \mathrm { { f i g } } { \sqrt { 6 . 4 \right) } }$ Evidently, $\partial \phi / \partial q \to \infty$ when $q \to q _ { j }$ ,a turning point. The angular distribution along the invariant curve can also be understood directly from Liouvilles theorem. The conservation of area by the flow implies that the linearly moving angle becomes stretched where invariant curves approach each other and compressed where they separate.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0002_pages_0071-0140/auto/images/cd2f713d81870408bb14173c8474501b544454523a769df89610378193b1ee2b.jpg)  
Fig.6.5. The effect of a canonical shear transformation on the level curves is that the turning poifts no longer have $\pmb { \mathrm { p } } = 0$

# Exercise

Show that, if $s$ is the length along the elliptic level curve of the harmonic oscillator (6.23),then the ratio between dΦ/ds at the tips of the major and minor axes is $\omega ^ { 2 }$ 。

Other examples and properties of one-freedom systems are discussed in Percival and Richards (1982). Note that general coordinate transformations will destroy the simple form of Hamiltonians (6.19). The turning points will then no longer coincide with the zeros of $p$ along the level curve. One such class of transformations consists of the symplectic (linear) transformations studied in section 1.2. Another one includes the shears

$$
p ^ { \prime } = p - A ( q ) , \qquad q ^ { \prime } = q .
$$

The effect of a linear shear on the leveleurves is shown in fig.6.5/Evidently, the composition of two canonical transformations is again canonical. In the case of polynomial transformations, Engel (1958) proved that they can always be reduced to the composition of a symplectic transformation with a shear.

Example.Motion under a central force. The energy has the form

$$
H ( p _ { r } , p _ { \theta } , r , \theta ) = \frac { 1 } { 2 m } p _ { r } ^ { 2 } + \frac { 1 } { 2 m r ^ { 2 } } p _ { \theta } ^ { 2 } + V ( r ) \nonumber
$$

for the geometry indicated in fig.6.6a.fThe angular momentum $p _ { \theta }$ is a constant of the motionbecause the Hamiltonian is indepedent of $\theta .$ It is readily verified that $H$ and $p _ { \theta }$ are in involution,so this twofreedom stem is integrable.

Two irreducible circuits for the torus, labeled by a given energy and angular momentum, are the rotation in $\theta$ with constant $r$ and the libration in $r$ with constant $\theta$ .The corresponding action variables are

$$
I _ { 2 } = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } p _ { \theta } d \theta = p _ { \theta }
$$

and

$$
I _ { 1 } = \frac { 1 } { 2 \pi } \oint p _ { r } d r = \frac { 1 } { \pi } \int _ { r _ { 1 } } ^ { r _ { 2 } } \left\{ 2 m \left[ E - \frac { 1 } { 2 m r ^ { 2 } } I _ { 2 } ^ { 2 } - V ( r ) \right] \right\} ^ { 1 / 2 } d r ,
$$

where $r _ { 1 }$ and $r _ { 2 }$ are theturningpointsforthelibrationshown infig6.6t. The action I2 may be positive or negative and H(I1,I2),obtained from the inversion of (6.29),is symmetric in this variable (fig6.7).)


<!-- chunk 0003: pages 141-210 -->
![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/183100986d17a538471a08e70af2c87dcda6273093da84ed8f80b209a72e2540.jpg)  
Fig. 6.6. (a) The central force always points in the direction of the origin,and its magnitude depends only on the coordinate r. (b) The turning points for the librations are the same as for the one-dimensional motion with the effective potential $V ( r ) + p _ { \theta } ^ { 2 } / 2 m r ^ { 2 }$ (c) The invariant torus projects/as an annulus in configuration space; its boundaries are the caustics.

The invariant toras projects into configuration space $( r , \theta )$ or $( q _ { 1 } , q _ { 2 } )$ as an annulus $( \overbrace { \mathrm { I } \mathrm { g } } \{ 6 . 6 \mathrm { c } \} . ) _ { \cdot } ^ { \star }$ Each point within it is the image of two points of the torus,ite $\pm \ : p _ { r }$ allowed by (6.27) for fixed $H = E$ and $p _ { \theta }$ .The boundary of the torus projection is known as the caustic.It is composed of the two circles $\boldsymbol { r } = \boldsymbol { r } _ { 1 }$ and $r = r _ { 2 }$ ,where the two pre-images on the torus coalesce. The torus defined by the same energy, but angular momentum $- \pmb { p _ { \theta } }$ ,has the same caustics.

The Hamiltonian depends nonlinearly on $I _ { \mathrm { ~ 1 ~ } }$ and $I _ { 2 }$ ,entailing the continuous variation of the frequencies

$$
{ \pmb \omega } = \frac { \partial H } { \partial { \bf I } } ( { \bf I } )
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/a54794b4081f798572e9bb27bc36b5112b5c59da89c3246408083aa99852d3f8.jpg)  
Fig 6.7J The level curves of $H ( I _ { 1 } , I _ { 2 } )$ are symmetric in $I _ { 2 }$

among the invariant tori. In any neighbourhood $( \delta I _ { 1 } , \delta I _ { 2 } )$ of the action variables we find tori with rationally related frequencies, that is, tori where all the orbits are periodic.The case of the Kepler problem,in which all tori have periodic orbits,is singular - there are other constants of the motion beyond angular momentum and energy. Another instance, in which all the orbits are periodic, is that of the isotropic harmonic oscillator with $V ( r ) = \omega ^ { 2 } r ^ { 2 } .$ The extra constants of the motion in this case willbe discussed in the following example.

Example.Separable systems.These are characterized by Hamiltonians of the form

$$
H ( \mathbf { p } , \mathbf { q } ) = \sum _ { l = 1 } ^ { L } H _ { l } ( p _ { l } , q _ { l } ) .
$$

All the partial Hamiltonians $H _ { l }$ are in involution with one another and with the full Hamiltonian $H$ .Choosing the corresponding partial energies $E _ { l }$ as constants of the motion, we obain the action vriables $I _ { l }$ independently from equations like (6.20). The most powerful general method for integrating the equations ofmotion,thatof HamiltonandJacobi,relison transformations to coordinates that separate the Hamiltonian. This is discussed by Arnold (1978) and Goldstein (1980). It follows that the Hamilton-Jacobi method can be applied only to integrable systems.

In the case of a two-dimensional harmonic oscillator or of a pair of uncoupled oscillators, the Hamiltonian will be

$$
H ( \mathbf { I } ) = \omega _ { 1 } I _ { 1 } + \omega _ { 2 } I _ { 2 } .
$$

Itslevelcurvesretraight-inegment fig.8)heequencete same foralltori,sothatall orbitsareperiodic if tHe $\omega _ { j }$ are rationally related. Otherwise,the orbits are al open.In the case where $\omega _ { 1 } = \omega _ { 2 }$ ,the oscillator is isotropic. The fact that all orbits are then periodic may be attributed to the existence of a further constant of the motion $p _ { \theta }$ ,independent of $H _ { 1 }$ and $H _ { 2 }$ .The intersection of the level curves of these three functions is a closed curve, which defines the orbit.

The caustics for the torus of aseparable system of two freedoms areeasily found from the construction shown in figl6.9. Thre-independence of the motion in the conjugate planes $( p _ { 1 } , q _ { 1 } )$ and $\left( p _ { 2 } , q _ { 2 } \right)$ implies that the caustics are straight-line segments corresponding to the turning points. Therefore, the torus projects onto the configuration plane as a rectangle. Any point q inside it corresponds to four points on the torus with coordinates $( p _ { 1 } ^ { \pm } , q _ { 1 } ^ { \pm } )$ Two pairs coalesce on the (double) caustic. This projection of a smooth torus would be impossible were it embedded in three-dimensional space rather than in four dimensions. We can still‘visualize’ this projection by considering a vertical tyre tube (i.e., the position in which it rolls on the ground). When emptied of airit collapses into a rectangle on the floorjust as our separable torus, but it is no longer smooth. In a four-dimensional space we can now fillit out along the fourth dimension' without altering the projection.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/219309f058a7f3fbfeddb04683afdb7fdb45c09adf384ffd7d7c2bf78f2b3ee7.jpg)  
Fig(6.8. JThe Hamiltonian for a two-dimensional oscillator is a linear function of the actions.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/9cabdda44795bd6fa3ca8ccaa929ff3af558b56b7a1c71810950a585a7ab1293.jpg)  
Fig6.9. From the phase graphs of the two independent motions of a separable system, we obtain the projection of the torus onto the configuration space. Each point inside the rectangle is the image of four points inside the torus.

A final important example of integrable systems is provided by the normal-form Hamiltonians, which approximately describe the motion surrounding a stable periodic orbit, studied in section 4.4. Truncating the Birkhoff normal form, we obtain an integrable system,the action-angle variables of which are $I$ and $J$ .Even the resonant normal forms are integrable systems andalmost allpoints lieon tori,though this is not true for the points lying along separatrices in the $( I , \theta )$ plane. The reason is that these are level curves of the reduced Hamiltonian H(I,0) (a constant of the motion) with the same partial energy as one of its equilibria.At such a point the vector field (i,0)=O,contrary to the assumptions in the Arnold-Liouville theorem. The phase space of a system with separatrices cannot be globally transformed to action-angle variables. This is possible only for each separate family of tori.

# 6.3 Caustics

The previous examples have made familiar the fact that p(q) for an invariant torus and hence the action S(q),defined by(6.14),are multivalued functions. The caustics limiting the motion in configuration space are the boundaries of the branches of S(q). They correspond to the set of points in phase space where

$$
\operatorname* { d e t } d { \bf p } / d { \bf q } = \infty .
$$

The way that different branches of $S ( \mathbf { q } )$ join together at a caustic can be analysed by means of its Legendre transform

$$
S ( { \bf { p } } ) = { \bf { p } } \cdot { \bf { q } } - S ( { \bf { q } } ) ,
$$

where ${ \mathfrak { q } } ( { \mathfrak { p } } )$ is given by (6.15).Inthecaseofonefreedom,wecanmakethe graphicalcotuctiowing6.1egangioioe

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/1cb3feddb6da266393696908a592c0e9cf4197e97a9ce8cdc48c01de7cc540e8.jpg)  
Fig6.10.Grapicalconstructionoftheaction $S ( \mathfrak { p } )$ given S(q); together they make up the area of a rectangle.

invariant torus implies that

$$
\oint \mathbf { q } \cdot d \mathbf { p } = - \oint \mathbf { p } \cdot d \mathbf { q } = 0 .
$$

Therefore, the function

$$
S ( { \mathfrak { p } } ) = \int _ { \mathfrak { p } _ { 0 } } ^ { \mathfrak { p } } \ \mathfrak { q } \cdot d { \mathfrak { p } }
$$

is the same function defined by (6.34) within an additive constant. This function is also multivalued, and its branches join at caustics of the projection of the torus onto the p space (fig.6.11) However, $S ( \mathbf { \mathfrak { p } } )$ is a one-toonefunction in the neighbourhood of the caustics of $S ( \mathbf { q } )$ Differentiating (6.36),

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/6db914b2b7bea57e816457b2cf39c8fb145b4e4de98c29fa77822f63b5a3056e.jpg)  
Fig.6.11/ The function S(p) is multivalued like S(q). The branches meet at the caustics $p ^ { + }$ and $p ^ { - }$

and inverting (6.33), we obtain the caustic condition in the form

$$
\operatorname* { d e t } \left| { \frac { \partial \mathbf { q } } { \partial \mathbf { p } } } \right| = \operatorname* { d e t } \left| { \frac { \partial ^ { 2 } S } { \partial \mathbf { p } \partial \mathbf { p } } } \right| = 0 .
$$

The map p→q is given by the gradient of the function S(p) according to (6.37). The classification of the locally generic forms of the simplest singularities (638)ofgradient maps isthecontentof Thom's theoremthe cornerstoele Stewart (1978). Generic singularities are those whose form remains invariant with respect to small alterations of the function S(p). The clasification depends only on the dimension of configuration space. The simplest case is that of one freedom,for which the only structurally stable causticis the fold,that is,theturning point alreadymet inseveral eamples. Folds also appear in higher-dimensional configuration spaces; this is the caseofthefoldlinesinfig6.6chedimensionofthelocusoffoldpont is always one less than that of the configuration space; for example, folds will form two-dimensional surfaces in the case of a three-freedom system. For this reason folds are said to have codimension 1.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/36c0beb626f9241e1997f0fe402f168239024efc0c412ef52797170ee6fae602.jpg)  
Fig6.12Cusppoitsaretegeericprojetionofthemeetingofsothfolds in the phase space.

Caustic lines can join at a cusp point (fig.6.12) Cusps are the only other generic caustic in the plane. Since their dimension is two less than the configuration space, they are of codimension 2. Hence, they appear along lines in a three-dimensional space. So far we have not met any cusp point, but these caneasily be obtained by rotating the torus of fig.C6.6cby a group of symplectic transformations. The result is the same as the projection of a rotated tyre tube depicted in $\widetilde { \mathrm { I } 1 } \mathtt { g } \langle \overline { { 6 . 1 3 } } .$ The numbers in the figure specify the multiplicity of $S ( \mathbf { q } )$ in each region.

Thom's theorem also furnishes the normal form to which we can reduce the action function S(p) by a canonical transformation near the generic caustic. The most elegant presentation in the context of Hamiltonian dynamics is that of Arnold (1978,app.12), who has considerably extended the classification of caustics. The idea is to use the mixed action function $S ( p _ { i } , \ldots , p _ { l } , q _ { l + 1 } , \ldots , q _ { L } ) .$ ，which can be considered to be the Legendre transform of $S ( \mathbf { q } )$ with respect to $l$ variables, or the transform of $S ( \mathbf { q } )$ with respect to $L - l$ variables. The transformation $\mathbf p \to \mathbf q$ is given implicitly by

$$
q _ { i } = { \partial S } / { \partial p _ { i } } , \qquad p _ { j } = { \partial S } / { \partial q _ { j } }
$$

with $1 \leq i \leq l$ and $l < j \leq L$ ·

A nonsingular region has the normal form

$$
A _ { 1 } : S = \sum _ { i } p _ { i } ^ { 2 } ;
$$

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/72c7acd1590adc40ab68d1ba879dc1e361de4101206df45c4470006664530bdc.jpg)  
Fig6.13y Cusps appear in the shadows of a semitransparent tyre tube as it is rotated from a horizontal to a vertical position.The numbers in the figure indicate the multiplicity of the projection in each region.

that is,the Lagrangian manifold can be linearized in the absence of a caustic.For $L = 1$ ,the only generic singularity is the fold with the normal form

$$
A _ { 2 } \colon S = \pm p _ { 1 } ^ { 3 } .
$$

For $L > 1$ we obtain the normal form for the fold line $( L = 2 )$ , the fold surface $\left( L = 3 \right)$ and so onsimply by ading $L - 1$ terms of the normal form $A _ { 1 }$ to $A _ { 2 }$ .This procedure for constructing the normal form for singularities in higher-dimensional spaces by adding $A _ { 1 }$ is also validfor the singularities that follow. For $L = 2$ the other genericcaustic is thecuspthenormalform of which is

$$
A _ { 3 } { : } S = \pm p _ { 1 } ^ { 4 } + q _ { 2 } p _ { 1 } ^ { 2 } .
$$

For $L = 3$ we have two new generic codimension-3 caustics:

$$
\begin{array} { c } { { A _ { 4 } { : } S = \pm p _ { 1 } ^ { 5 } + q _ { 3 } p _ { 1 } ^ { 3 } + q _ { 2 } p _ { 1 } ^ { 2 } , } } \\ { { { } } } \\ { { D _ { 4 } ^ { \pm } { : } S = \pm p _ { 1 } ^ { 2 } p _ { 2 } \pm p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } . } } \end{array}
$$

For $L = 4$ there is also

$$
\begin{array} { c } { { A _ { 5 } { : } S = \pm p _ { 1 } ^ { 6 } + q _ { 4 } p _ { 1 } ^ { 4 } + q _ { 3 } p _ { 1 } ^ { 3 } + q _ { 2 } p _ { 1 } ^ { 2 } , } } \\ { { } } \\ { { D _ { 5 } { : } S = \pm p _ { 1 } ^ { 2 } q _ { 2 } \pm p _ { 2 } ^ { 4 } + q _ { 4 } p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } , } } \end{array}
$$

and finallyor $L = 5$ ，

$$
\begin{array} { r l } & { A _ { 6 } { : } S = \pm p _ { 1 } ^ { 7 } + q _ { 5 } p _ { 1 } ^ { 5 } + \cdots + q _ { 2 } p _ { 1 } ^ { 2 } , } \\ & { D _ { 6 } { : } S = \pm p _ { 1 } ^ { 2 } p _ { 2 } \pm p _ { 2 } ^ { 5 } + q _ { 5 } p _ { 2 } ^ { 4 } + q _ { 4 } p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } , } \\ & { E _ { 6 } { : } S = \pm p _ { 1 } ^ { 3 } \pm p _ { 2 } ^ { 4 } + q _ { 5 } p _ { 1 } q _ { 2 } ^ { 2 } + q _ { 4 } p _ { 1 } p _ { 2 } + q _ { 3 } p _ { 2 } ^ { 2 } . } \end{array}
$$

Arnold(1975)also studied the generic caustics for $L > 5$ ,but they cannot all be reduced to a discrete set.

The catastrophes $D _ { 4 } ^ { \pm }$ (6.44) are known as the umbilics. If both the first terms have the same sign, we have the hyperbolic umbilic $D _ { 4 } ^ { + }$ ;otherwise,the normal form represents the elliptic umbilic.

# Exercises

1. Show that the transformation

$$
p _ { 1 } = 2 ^ { - 2 / 3 } 3 ^ { 1 / 2 } ( \mathfrak { p } _ { 1 } - \mathfrak { p } _ { 2 } ) , \qquad p _ { 2 } = 2 ^ { - 2 / 3 } ( \mathfrak { p } _ { 1 } + \mathfrak { p } _ { 2 } )
$$

reduces the normal form for $D _ { 4 } ^ { + }$ to

$$
\pm { \mathfrak { p } } _ { 1 } ^ { 3 } \pm { \mathfrak { p } } _ { 2 } ^ { 3 } + 2 ^ { - 4 / 3 } q _ { 3 } ( { \mathfrak { p } } _ { 1 } + { \mathfrak { p } } _ { 2 } ) ^ { 2 } .
$$

Find the transformation ${ \mathfrak { q } } \to { \mathfrak { q } }$ that makes $( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } )  ( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } )$ a canonical transformation.

2. Show that the folds of a separable system meet each other along the $\mathfrak { q } _ { 3 } = 0$ (i.e., $q _ { 3 } = 0$ ) section of the hyperbolic umbilic.

The double fold lines of a separable system do not meet at a cusp point, the only other generic singularity for a two-dimensional system. According to exercise 2 above, this meeting takes place in a section of a higher singularity. Thom's theorem thus leads us to expect that a small deformation of the torus will‘almost always'unfold this singularity into generic caustics. These are obtained by taking sections of ${ D } _ { 4 } ^ { + }$ with $q _ { 3 }$ small but finite;thtise o $q _ { 3 }$ not to be a coordinate in a higher-dimensional phase space but a parameter measuring the ‘departure from separability'. The result of the unfolding is shown in $\mathrm { f i g } ( 6 . 1 4 ^ { }$ The deformation of a separable torus in two dimensions may therefore have caustics resembling that of the torus with cireular symmetry in fig.6.13cj This is not the only possibilityhowever,since ctastrophe theory provides only local lts. Ozorio de Almeida and Hannay (1982) present transformationsthat bring separable tori into each of the configurations in figl6.15

How sure can we be that a perturbation of the torus is generic - that is, capable of unfolding the projection of the torus? There wil obviously be no unfolding if the perturbed Hamiltonian is still separable. What about an invariant torus of a general $\mathbf { p } ^ { 2 } / 2 m + V ( \mathbf { q } )$ type of Hamiltonian? Even in this case,it was shown by Ozorio de Almeida and Hannay (1982) that there is no unfolding of the $D _ { 4 } ^ { + }$ corners because of the symmetry in the momenta.The unfoldings in figC6.15 areall realized by breaking this symmetry. The central problem in utilizing Thom's theorem or other arguments based on genericity or structural stability is to know whether the perturbation is really generic or special, owing to a possibly hidden symmetry.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/c1fc4868ceb6e0a56e9f451d2985d97795a5db123a97138c615d49d9b42f48b4.jpg)  
Fig.6.14. The double fold lines of the hyperbolic umbilic are unfolded so that there are regions with zero, two or four pre-images on the torus.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/f48e8dcd2814b1a3c83514ae96c490bb562c25d995658e580d5f7fbc5b74bf78.jpg)  
Fig6.15.Possible global unfoldings for a separable torus.

The original concept of caustic is that of an envelope of a family of trajectories. In our case the family is the projection onto configuration space of the orbits that wind around an invariant torus. When the orbits pass smoothly from one torus branch to another, their projections touch a caustic. The simplest example of a caustic is that of a hose sprinkling parallel jets of water (fig.6.16), The caustic is the horizontal line of maximum height attained by the water.It corresponds to a singularity in the density of orbits.If the orbits dre identified with the light rays of optics, the resulting high intensity of light leads to ‘burning’ - hence the name. Berry and Upstill (198O) provide a clear presentation of caustics and catastrophe theory in an intuitive optcal context.

In an integrable system where the frequencies do not have a constant ratio,almost all tori have open orbits that are dense. It follows that we can take a single orbit as/'the family’ and obtain the caustic as the envelope 9f successive windings of this orbit. Furthermore, the integrability of the system can be asgertained if almost all orbits have caustic envelopes. As an example we first consider the circular biliard in fig.6.17a.JWe know this to be an integrable system,because the force is central. Any orbit has a point of closest appfoach to the centre,at which it is tangent to an inscribed circle - the caustic. It is much harder to show directly that the elliptic billiard is an integrable system. However,in this case it is also true that any orbit has as envelope an inscribed curve,in this case a confocal elipse (fig. 6.17b).

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/2c196685657c60630319f4c24fbda2f3043f25d2fe2eaa73fb6e6e5434fedbfa.jpg)  
Fig616Olteealoft is an envelope of orbits, i.e., a caustic.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/2e68068184ee542695afdd89f3362b9cec2fa4b291d601078cd9f9b28de3b10d.jpg)  
${ \mathrm { F i g } } { \widehat { 6 . 1 7 } } .$ (a) An orbit in a circular billiard has an inscribed circular envelope. The equatity of the angles of incidence and reflection with respect to the radius leads to the conservation of angular momentum. (b) An orbit in an elliptic bilhard also has an envelope -a confocal ellipse. The equality of the angles of incidehce and reflection with respect to the lines to the foci at O and $0 ^ { \prime }$ leads to the conservation of the product of angular momenta about O and $\mathbf { 0 } ^ { \circ }$

# Exercise

Show that the product $\boldsymbol { J } _ { 0 } \boldsymbol { J } _ { 0 }$ of the angular momenta about the foci O and $0 ^ { \prime }$ is conserved for thecircular biliard.(Hint:The angles between the tangent to an ellipse, at a given point,and the two lines joining it to the foci are equal.y

# 6.4 Perturbations and averaging

The'introduction to the theory of integrable systems presented in the preceding sections will serve as the basis for the traditional treatment of the semiclassical limit of quantum mechanics in chapter 7.The very particular restrictions on integrable systems prevent them from being structurally stable. Thus,in spite of the great number of solved integrable problems in classical mechanics,one should not expect that a general perturbation will lead to a new integrable system. Yet it is stillvery worthwhile to base the understanding of nearly integrable systems on the unperturbed system. In

This result was communicated to me by J.H. Hannay.

section 6.5 we shall discuss the fundamental question of the survival of invariant tori subject to perturbations,the subject of the KAM theorem. We start with the discussion of approximate methods -that is,low-order perturbation theory and the averaging principle\~which provide good quantitative results for limited time intervals.

It is convenient to study the flow of a perturbed system with the actionangle variables of the integrable system.The equations of motion fora quasi-integrable system have the form

$$
\begin{array} { l } { { \dot { \boldsymbol { \phi } } = \omega _ { 0 } ( \mathbf { I } ) + \varepsilon \mathbf { f } ( \mathbf { I } , \boldsymbol { \phi } ) , } } \\ { { \qquad } } \\ { { \dot { \mathbf { I } } = \varepsilon \mathbf { g } ( \mathbf { I } , \boldsymbol { \phi } ) . } } \end{array}
$$

If the Hamiltonian has the form

$$
H ( \mathbf { I } ) = H _ { 0 } ( \mathbf { I } ) + \varepsilon H _ { 1 } ( \mathbf { I } , \phi ) , \qquad 
$$

then

$$
{ \bf f } = \partial { \cal H } _ { 1 } / \partial { \bf I } \quad \quad \mathrm { a n d } \quad \quad { \bf g } = - \partial { \cal H } _ { 1 } / \partial \phi .
$$

Consider ‘disconnecting the perturbation’ so that all the orbits are restricted to the invariant tori of $H _ { 0 }$ .Wecan thenevaluate the time average of $\mathbf { g } ( \mathbf { I } , \phi ( t ) )$ .Almost alltori will have rationally independent frequencies,so the equivalence of time and configuration averages is valid:

$$
{ \bar { \bf g } } ( \mathrm { \bf I } ) \equiv { \frac { 1 } { T } } \operatorname* { l i m } _ { T \to \infty } \int _ { 0 } ^ { T } { \bf g } ( \mathrm { \bf I } , \phi ( t ) ) d t = ( 2 \pi ) ^ { - L } \int _ { 0 } ^ { 2 \pi } \cdots \int _ { 0 } ^ { 2 \pi } { \bf g } ( \mathrm { \bf I } , \phi ) d \phi .
$$

In other words, the residue of the periodic force,

$$
\tilde { \mathbf { g } } ( \mathbf { I } , \boldsymbol { \phi } ) \equiv \mathbf { g } ( \mathbf { I } , \boldsymbol { \phi } ) - \bar { \mathbf { g } } ( \mathbf { I } ) ,
$$

has zero time average for periods $T$ much larger than the characteristic periods $2 \pi \omega _ { 0 } ^ { - 1 }$ of the integrable system. This suggests that, if we now reconnect the perturbation so that the system moves according to(6.50), the effect of the force $\tilde { \bf g }$ will be small, provided that the ‘inertia' $\varepsilon ^ { - 1 }$ of the system is large and the unperturbed periods are small. The system is already receiving a contrary force before it has had time to respond to the original force. This argument leads to the approximation of (6.50) by the averaged system

$$
\dot { \mathbf { I } } ^ { \prime } = \varepsilon \bar { \mathbf { g } } ( \mathbf { I } ^ { \prime } ) .
$$

This conjecture is confirmed for the following simple example presented by Arnold (1978, sec. 52):

$$
\dot { \phi } = \omega \neq 0 , \qquad \dot { I } = \varepsilon g ( \phi ) .
$$

The solution is

$$
\begin{array} { l } { { I ( t ) - I ( 0 ) = \displaystyle \int _ { 0 } ^ { t } \varepsilon g ( \phi _ { 0 } + \omega t ) d t = \displaystyle \int _ { 0 } ^ { t } \varepsilon \bar { g } d t + \frac { \varepsilon } { \omega } \int _ { \phi _ { 0 } } ^ { \phi _ { 0 } + t / \omega } \tilde { g } ( \phi ) d \phi } } \\ { { \quad \quad = \varepsilon \bar { g } t + \frac { \varepsilon } { \omega } h \bigg ( \displaystyle \frac { t } { \omega } \bigg ) , } } \end{array}
$$

where h() isa periodic functionand therefore bounded.Thus,ifI(t) is the motion of the averaged system, we have

$$
| I ( t ) - I ^ { \prime } ( t ) | < C \varepsilon ,
$$

where $C = \| h \| \omega ^ { - 1 } .$ The validity of the averaging principle for $L$ -freedom systems, subject to a perturbation depending on a single angle under quite general conditions, is also proved by Arnold (1978, sec. 52); that is,

$$
| I ( t ) - I ^ { \prime } ( t ) | < C \varepsilon \qquad \mathrm { f o r } \qquad 0 \leq t \leq \varepsilon ^ { - 1 } .
$$

The averaging principle must be applied with care if the system has more than one freedom and the perturbation also depends on more than one angle. The problem resides in the tori with rationally dependent frequencies: An unperturbed periodic orbit will not average out a perturbation that depends on more than a single angle. If the frequency ratio $\omega _ { 1 } / \omega _ { 2 }$ isa low-order rational, the unperturbed periodic orbit will sample only an atypical part of ${ \bf g } ( \phi _ { 1 } , \phi _ { 2 } )$ and even the open orbits of neighboring tori will take a long time to sweep through all the angles. We cannot apply the full averaging principle in such a region. Stillit is possible to make a partial average along the direction of the unperturbed periodic orbit, the fast variable, while keeping the slow variables transverse to the motion generated by $H _ { 0 }$ ·

A superior alternative to averaging away oscillatory terms of a Hamiltonian perturbation is to eliminate them by means of canonical transformations. We have already met a particular form of this procedure in chapter 4. There the unperturbed integrable Hamiltonian was quadratic, so that in the neighbourhood of the origin we could treat the higher-order angle-dependent terms in the Taylor expansion as the perturbation.We will now study the general perturbed Hamiltonian (6.51)， following the presentation of Lichtenberg and Lieberman (1983).

The function $H _ { 1 }$ is multiply periodic in the angles $\phi$ so it can be developed in the Fourier series

$$
H _ { 1 } ( \mathbf { I } , \phi ) = \sum _ { \mathbf { m } } H _ { 1 \mathbf { m } } ( \mathbf { I } ) \exp ( i \mathbf { m } \cdot \phi ) .
$$

The Hamiltonian is then subject to a transformation $( { \bf I } , \phi )  ( { \bf I ^ { \prime } } , \phi ^ { \prime } )$ ， generated implicitly by

$$
S ( \mathbf { f } ^ { \prime } , \phi ) = \mathbf { f } ^ { \prime } { \boldsymbol { \cdot } } \phi + \varepsilon S _ { 1 } ( \mathbf { f } ^ { \prime } , \phi ) ,
$$

where

$$
S _ { 1 } ( \mathbf { I } ^ { \prime } , \phi ) = \sum _ { \mathbf { m } } S _ { 1 \mathbf { m } } ( \mathbf { I } ^ { \prime } ) \exp ( i \mathbf { m } \cdot \phi ) .
$$

Differentiating,

$$
\begin{array} { r } { \mathbf { I } = \mathbf { I ^ { \prime } } + \varepsilon \partial S _ { 1 } ( \mathbf { I ^ { \prime } } , \phi ) / \partial \phi , } \\ { \mathbf { \phi } } \\ { \phi ^ { \prime } = \phi + \varepsilon \hat { c } \partial S _ { 1 } ( \mathbf { I ^ { \prime } } , \phi ) / \partial \mathbf { I ^ { \prime } } , } \end{array}
$$

we obtain the explicit transformation in the form

$$
\begin{array} { c } { { { \bf I } = { \bf I ^ { \prime } } + \varepsilon \hat { \sigma } S _ { 1 } ( { \bf I ^ { \prime } } , \phi ^ { \prime } ) / \hat { \sigma } \phi + O ( \varepsilon ^ { 2 } ) , } } \\ { { \phi = \phi ^ { \prime } - \varepsilon \hat { \sigma } S _ { 1 } ( { \bf I ^ { \prime } } , \phi ^ { \prime } ) / \hat { \sigma } { \bf I ^ { \prime } } + O ( \varepsilon ^ { 2 } ) . } } \end{array}
$$

The Hamiltonian is invariant with respect to this transformation, so

$$
H ^ { \prime } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } ) = H _ { 0 } ( \mathbf { I } ^ { \prime } ) + \varepsilon H _ { 1 } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } ) + \varepsilon \frac { \partial H _ { 0 } } { \partial \mathbf { I } ^ { \prime } } \bullet \frac { \partial S _ { 1 } } { \partial \phi ^ { \prime } } + O ( \varepsilon ^ { 2 } ) .
$$

We can now specify the function $S _ { 1 }$ so as to cancel the angular dependence of the linear part of $H ^ { \prime }$ .In this way the new Hamiltonian becomes integrable up to ${ \cal O } ( \varepsilon ^ { 2 } ) .$ The required condition is

$$
{ \pmb \omega } \cdot \frac { \partial S _ { 1 } } { \partial { \pmb \phi } ^ { \prime } } = - \sum _ { { \bf m } \neq 0 } H _ { \mathrm { 1 m } } ( { \bf I } ^ { \prime } ) \exp ( i { \bf m } \cdot { \pmb \phi } ^ { \prime } ) ,
$$

which yields

$$
S _ { 1 } ( { \bf { I } } ^ { \prime } , \phi ) = i \sum _ { m \neq 0 } \frac { H _ { \mathrm { 1 m } } ( { \bf { I } } ^ { \prime } ) } { { \bf { m } } \cdot \omega } \exp ( i { \bf { m } } \cdot \phi ) .
$$

Once again we have to face the problem of small denominators. Generally the frequencies vary continuously among the tori, so the resonant tori, for ich

$$
\mathbf { m } \cdot \boldsymbol { \omega } ( \mathbf { I } ) = 0 ,
$$

are dense in phase space. We can study the first-order effct of the perturbation in the neighbourhood of a given resonant torus by adopting its periodic orbits as coordinates.Inthecaseof two freedoms,theresonant torus will have frequencies

$$
\omega _ { 1 } / \omega _ { 2 } = s / r .
$$

If we choose one of the angular coordinates to be

$$
\phi = \phi _ { 1 } - s \phi _ { 2 } / r ,
$$

then $\dot { \phi } = 0$ on the unperturbed torus. We need a full canonical transformation $( I _ { 1 } , I _ { 2 } , \phi _ { 1 } , \phi _ { 2 } )  ( J , I , \theta , \phi )$ incorporating (6.67). This is implicitly defined by the generating function

$$
F = ( \phi _ { 1 } - s \phi _ { 2 } / r ) I + ( \phi _ { 2 } / r ) J ,
$$

so that the rest of the transformation becomes

$$
\theta = \phi _ { 2 } / r , \qquad I = I _ { 1 } , \qquad J = r I _ { 2 } + s I _ { 1 } .
$$

# Exercise

Find the irreducible circuits $\theta = 0$ and $\phi = 0$ on the torus and show that the respective symplectic areas are $2 \pi J$ and $2 \pi I$

This exercise identifies the variables $( J , \theta )$ with the periodic orbit variables introduced in section 2.5.In the present integrable case, each orbit belongs to a family with two parameters - the energy and the angle $\phi$

$$
H = H _ { 0 } ( J , I ) + \varepsilon H _ { 1 } ( J , I , \theta , \phi ) ,
$$

where

$$
H _ { 1 } = \sum _ { k , m } H _ { k , m } ( J , I ) \exp { \{ i [ k \phi + ( k s + m r ) \theta ] \} } .
$$

Though we cannot average over both angles, this is a reasonable approximation for the fast variable $\theta$ .The result is

$$
\begin{array} { r } { \overline { { H } } = H _ { 0 } ( J , I ) + \varepsilon \overline { { H } } _ { 1 } ( J , I , \phi ) , } \end{array}
$$

where

$$
\stackrel { \_ } { H } _ { 1 } = \sum _ { n = 0 } ^ { \infty } H _ { - n r , n s } ( J , I ) \exp ( - i n r \phi ) ,
$$

By abandoning the attempt to eliminate all the angular dependence of the Hamiltonian, we thus obtain an improved approximation. The Hamiltonian $H$ is integrable, since $J$ is an independent constant of the motion.

# Exercise

Derive the approximation (6.72) of the Hamiltonian (6.70) through perturbation theory and show that the generating function for the corresponding canonical transformation has no small denominators. Note that the identity of the two approximate Hamiltonians does not imply that the motion is the same.

If $\boldsymbol { \overline { { H } } } _ { 1 }$ is an analytic function (in a complex strip $| \operatorname { I m } \phi | < \rho )$ ,then the coefficients in the Fourier series (6.73) decay exponentially. The simplest case is the one in which the only nonzero terms have $| n | \leq 1 .$ For smalle we can then make an approximate Taylor expansion about the unperturbed periodic torus with actions $( I _ { 0 } , J _ { 0 } )$ to obtain

$$
\begin{array} { r } { \widetilde { H } = H _ { 0 } ( I _ { 0 } , J _ { 0 } ) + \varepsilon H _ { 0 , 0 } ( I _ { 0 } , J _ { 0 } ) + a ( \Delta I ) ^ { 2 } + \varepsilon b \cos ( r \phi ) . } \end{array}
$$

This approximation is known as a Chirikov resonance (see Chirikov,1979). We immediately recognize the pendulum Hamiltonian in the variables $( \Delta I , \phi )$ studied in section 4.4.There are $r$ families of isands,corresponding toa single family of island tori.These are centred bya single stable periodic orbit,and they are separated from the enveloping tori by the separatrices that emanate from the unique unstable periodic orbit. The inclusion of further terms in the series (6.73)merely distorts the pendulum tori if all the higher-order terms are small. In contrast, the inclusion of $\theta$ dependent terms will generally lead to homoclinic intersections of the separatrices and hence to the existence of chaotic orbits. The appearance of pairs of stable and unstable periodic orbits at a resonance of a perturbed integrable system can be proved by topological arguments. This is the content of the Poincare-Birkhoff theorem,the proof of which is sketched by Berry (1978).

Ofcourse, we can apply the above theory again to the resonant island tori as in Lichtenbergand Lieberman (1983). These tori willbreak up into new islands and so on in an infinite hierarchy. The complexity of this picture leads to doubts that there is any truth in it. Do any tori survive the perturbation? This is the subject of the following section.

# 6.5 Discussion of the KAM theorem

A first approximation to the perturbed Hamiltonian (6.51) in the neighbourhood of a perturbed torus is given by (6.72) and(6.73). The appearance of unstable fixed points leads to motion that is radically different from that generated by the original Hamiltonian. Further perturbation from this resonant approximation still alters important features of the motion,but it generally cannot bring back even distortions of the unperturbed tori usually destroyed in the resonant region. This is because the unstable periodic orbits willshow up as hyperbolic fixed points in a Poincare section. These points with their separatrices are incompatible with the unperturbed torus family. Nonetheless, unstable fixed points are structurally stable within a one-parameter family of maps, as was shown in section 2.5.

Taking into account all the resonances up to a given order [defined as the biggest integer $\left| \boldsymbol { r } \right|$ or $| s |$ in (6.66)], we obtain a picture such as fig.6.18.The exponential decay of the coefficients $H _ { k , m }$ in(6.71) implies that the size of the resonance - that is the area between the separatrices - proportional to εb in (6.74) decreases exponentially with the order of the resonance. We can thus obtain a first approximation to the flow as a whole by extending fig. 6.18 to all orders of resonance, while omitting those higher-order resonances that overlap and hence are ‘swallowed up’ by lower-order resonances. The resonant tori are densely distributed in the unperturbed system. Can tori survive the perturbation in the midst of all the resonances?

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/2572e0c8533be28c4a3e7f2e4825a8d964313646530e10ed7f80ba52383e6623.jpg)  
Fi& 6.18. Generally each region surrounding an unperturbed periodic torus will devetop a resonance, but the resonant region becomes very narrow for those tori with very long periodic orbitsy

In the case of two freedoms,the Poincare map for an unperturbed torus can be reduced to a translation on a circle. In chapter 5 we found that perturbations of this simple motion can stillbe reduced to it, provided that the rotation number is ‘suficiently irrational'. In the present context the rotation number can be identified with the frequency ratio, which varies continuously among the tori. Resonant tori correspond to circle maps whose rotation numbers are rational. Therefore, the basic theorem in section 5.4 proves directly that, if a torus ‘sufficiently far’ from resonance survives a perturbation,its Poincare mapcan be reduced to a translation; that is,its flow willbe quasi-periodic,just as in the integrable system.

The demonstration that tori do actually survive is much more intricate than the theory of the circle map.I will sketch only briefly the proof of Arnold(1963).The first step is toshow theconvergenceof the Fourierseries for the generating function (6.58) of the canonical transformation $( I , \phi )$ $ ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } )$ corresponding to first-order perturbation theory.To this end we assume that $H _ { 1 } ( \mathbf { I } , \phi )$ is analytic,with $\| H _ { 1 } \| < \varepsilon$ in astrip $| \operatorname { I m } \phi | < \rho$ (as with the circle map)and in a domain $G$ of $\textit { \textbf { l } }$ Convergence is proved in a reduced strip $| \operatorname { I m } \phi ^ { \prime } | < \rho - \delta$ and in a subdomain of $\mathrm { \bf G }$ .This includesall thetori with actions $\mathbf { I ^ { \prime } }$ and frequencies

$$
\pmb { \omega } ^ { \prime } = \partial \pmb { H } ^ { \prime } / \partial \pmb { \mathrm { I } } ^ { \prime }
$$

satisfying the Diophantine condition

$$
| \omega ^ { \prime } \cdot \mathbf { k } | \geq c | \mathbf { k } | ^ { - v } .
$$

The constants $c$ and $\nu$ depend only on ε and not on the integer vector $\mathbf { k }$

The result of this transformation is that the original Hamiltonian is reduced to the form

$$
H ^ { \prime } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } ) = H _ { 0 } ^ { \prime } ( \mathbf { I } ^ { \prime } ) + \varepsilon ^ { 2 } H _ { 2 } ^ { \prime } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } )
$$

along the tori satisfying (6.76). By applying Kolmogorov's method, as presented in section 5.4, it can now be shown that successive canonical transformations cancel the $\phi$ -dependent term while preserving a residual analyticity strip for the Hamiltonian.In this way the KAM theorem proves that the majority of the volume of phase space is occupied by invariant tori as $\varepsilon \to 0$ .Moser's demonstration of the survival of invariant curves in areapreserving maps relaxes the condition of analyticity on $H$ (Moser, 1962). On the other hand, Arnold's proof applies to perturbations of integrable systems with any number of freedoms.

The tori in the KAM theorem are specified by their frequencies (6.75) and (6.76). Therefore,the validity of the theorem depends on the nondegeneracy of the map $\mathbf { I } \to \omega$ ; that is, we must add the condition that

$$
\mathrm { d e t } | \partial ^ { 2 } H / \partial \mathbf { I } ^ { 2 } | \neq 0 .
$$

The KAM theorem can be adapted to integrable systems that are perturbed by a time-periodic Hamiltonian, since this can always be transformed into an autonomous system in an expanded phase space (see section 2.5). An important corollary for a forced system with one fredom is that linearly stable equilibria are truly stable,even after the perturbation. The reason is that near the equilibrium the Hamiltonian can be approximated by the truncated Birkhoff normal form, as in section 4.4. The remainder can be considered to be a perturbation that vanishes as the equilibrium is approached. The KAM theorem thus guarantees the existence of invariant curves surrounding the equilibrium. The orbits within are continuous and cannot intersect the curves. Since invariant tori exist arbitrarily close to the equilibrium,the motion in its neighbourhood is stable.

The motion for an autonomous system with two freedoms is restricted to three-dimensional energy surfaces. The KAM theorem guarantees the survival of small two-dimensional Birkhoff tori with the same energy as that of a point of linearly stable equilibrium. The equilibrium is inside any one of these tori on the energy shell. Thus, other orbits will remain within, even if they are not actually on a torus. The motion near a linearly stable periodic orbit of an autonomous two-freedom system is also stable, by a similar argument.

# Exercise

Explain why we must invoke the Birkhoff normal form,rather than apply the KAM theorem directly to the integrable linearized system， by considering the whole nonlinear part as a perturbation.

The stability willbe lost only when the last enveloping torus is destroyed. Presumably this torus is characterized by the frequency ratio most difficult to approximate by rationals. This conjecture has been computationally verified by Greene (1979) for the ‘standard map'. This large perturbation regime is not accessible to the KAM techniques -hence, the great interest in the adaptation by Escande (1985) of‘renormalization group' techniques to the study of the survival of tori subject to large perturbations.

A relatively recent discovery of great importance by Aubry (1978) and Percival (1979) is that of nonchaotic,nonperiodic orbits resulting from the destruction of nonresonant tori by large perturbations. General existence proofs are given by Katok (1982), Mather (1982) and Aubrey and Le Daeron (1983). This orbit maintains the same rotation number as on the torus before destruction, but it does not fill a torus densely. There are gaps,creating a structure described as a product ofa torus with a Cantor set.These so-called cantori hinder thediffusion of chaotic orbits,as studied byMackayeissdcal984).matelyodthesttio of a torus, holes of the cantorus are exponentially small, entailing exponentially slow diffusion through the gaps.

The situation for systems with three freedoms resembles that of the motion near cantori, even for arbitrarily small perturbations. The reason is that a three-dimensional torus does not separate the five-dimensional energy surface.It can be circumvented, just as a line in three-dimensional space. The Poincare map for an integrable system will consist of linear translations along two-dimensional tori by angles (2πμ1,2πμ2). All the tori with rotation numbers satisfying

$$
m _ { 1 } \mu _ { 1 } + m _ { 2 } \mu _ { 2 } = k
$$

are resonant.The KAM theorem guarantees the survival of only sufficiently nonresonant tori. These are.the ones that are not caught in Arnold's net, partiallyskecedinfig19Eachbandinthenetorrespondstooeof the resonance conditions (6.79). They become exponentially narrow as the order of the resonance becomes large. Instead of an infinite number of separated chaotic regions,as with two freedoms, we have a single chaotic region that penetrates everywhere. Since the bands communicate, an orbit started inside the chaotic region of one particular band will be able to wander around and explore all the other bands. The net is dense on the square, so the orbit will be able to go everywhere. This is known as Arnold diffusion. The diffusion will be exponentially slow as ε→O, because of the exponential narrowness of the higher-order bands. This subject is extensively reviewed by Lichtenberg and Lieberman (1983).

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/842abc55cde0be60cffa28e04d9bddb8f8f266af1395025dd2b42323850e160b.jpg)  
FigC6.19.|The resonance condition establishes straight lines in the plane of rotation numbers $( \mu _ { 1 } , \mu _ { 2 } )$ for the unperturbed system. The resonant region for each of these is thus a band. These are multiply connected in Arnold's net.

The proof in section 6.1 that the invariant tori of an integrable system are Lagrangian cannot be generalized to the survivors of a KAM perturbation. Nonetheless, this important property also holds for any invariant surface contained in an energy shell. This is a consequence of the same argument that led to the Poincare-Cartan theorem in section 2.4. The full action

$$
\oint [ { \bf p } \cdot d { \bf q } - H d t ] = 0
$$

for any reducible closed circuit on the surface formed by a one-parameter family of trajectories in extended phase space. If all the orbits have the same energy, the loop can be projected into phase space, yielding

$$
\oint \mathbf { p } \cdot d \mathbf { q } = 0 .
$$

Thus,the invariant tori ofa KAM system have caustics,just as do those of an integrable system. Moreover, their local features should have the generic properties allowed by catastrophe theory,unless there are special symmetries involved. Since all the invariant KAM tori have dense orbits, we can in principle determine whether an orbit belongs to a torus by simply graphing_it_in configuration space and watching out for envelopes. FigureC6.20 shows orbits computed by Ramaswamy and Marcus (1981) for a one-parameter family of quasi-integrable two-freedom Hamiltonians of the p² + V(q) type.The first six graphs indicate the existence of a torus. Note the nongeneric meeting of the folds at the umbilic corners, due to the symmetry in p. The penultimate orbit is compatible with a thin island torus, since each thin ribbon shows a fold. The last graph indicates chaotic motion constrained by surviving tori: There are bounds to the motion, but clearly some orbits turn before reaching this ‘outermost.envelope'. The corresponding Poincare sections are shown in fig.6.21.

In a quasi-integrable system, we can be sure trat an envelope for the successive windings of a trajectory is the signature of a torus.However,a more general system may have invariant surfaces with diferent topology. An example is provided by the ‘pseudointegrable’ systems studied by Richens and Berry (1981), which appear among polygon biliards. Among these,a two-dimensional invariant surface may be a $g$ -handled sphere with $g > 1$ $\scriptstyle { \mathcal { G } }$ is called the genus of the surface). Ozorio de Almeida and Hannay (1982) present a rule for identifying $g$ from thecaustics ofa two-dimensional invariant surface: The tangent to a smooth closed line swings through a multiple of $2 \pi$ (it may self-ntersect).If theclosed line hscusps,howerit may swing through half-turns; that is, we consider the direction of the tangent line as that of a car travelling along a fold line, which backs away when it meets a cusp point. Then, if all the caustic lines are traversed the "same”way - that is, with the double layer of the fold always on the right (or always on the left)-the total number of rotations of the tangent line is $g - 1$ .For a torus with umbilic corners, because of symmetry， the rule must be applied to the unfolded projection, as in fig6.15.

We have now completed the outline of classical dynamics. Many subjects omitted or merely touched upon are thoroughly discussed by Lichtenberg and Lieberman (1983), who also provide extensive references.My emphasis has been mainly on periodic orbits. In contrast to a dissipative system, where periodic orbits may be attractors, there is zero probability of the system being on a periodic orbit. However, we have seen many systems where periodic orbits are at least approximately dense. This is the case of integrable systems, simply because commensurable frequency ratios are dense among the real numbers. Perturbing these systems we generally destroy all the periodic tori. Yet isolated periodic orbits remain, half of which are stable. Around these we find nonresonant island tori, the periodic tori giving way to isolated periodic orbits and so on,in an ever finer selfsimilar structure. The complement of this figure is organized around the unstable periodic orbits, also present in the resonant region. Their separatrices generally have homoclinic or heteroclinic intersections -points of accumulation for infinite families of periodic orbits. Increasing the perturbation may bring about the destruction of most island tori and the period-doubling bifurcation cascades of the stable fixed points. The result is the population of most of phase space by a multitude of unstable periodic orbits,as in the cat map,where they are proved to be dense.

The hypothesis that periodic orbits are dense means that all orbits can be well approximated by periodic orbits for arbitrarily long times. One of the guiding principles for research in this field since Poincaré has thus been the parallel studies of the local motion near periodic orbits and of their organization in phase space. The latter program is certainly at a much more incipient stage.Allthe same,it willbe shown inchapter9 that the same principle is also a valuable guide to the study of the semiclassical limit of quantum mechanics, our concern from here on.

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/0b48321ac12ce975c78c9dc94658248b4ac02af61ec654815f042f837ca54bc1.jpg)

![](../chunks/Hamiltonian Systems Chaos and Quantization (Cambridge Monographs on Mathematical Physics)_part_0003_pages_0141-0210/auto/images/9003d7910853b6e957d5ade82e5595d0dc8057428c66549e96ca602398fc6d2d.jpg)
