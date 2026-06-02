solution (without projection) shows the correct qualitative behaviour (this can be explained by a backward error analysis, see Sect.II.16),whereas the projection onto ${ \cal H } = C o n s t$ destroys this property. A remedy could be the following: apply a symplectic method to the problem, project the numerical solution to ${ \cal H } = C o n s t$ ， but continue the integration with the unprojected values.

# Methods Based on Local State Space Forms

This method is also called differential-geometric approach by Potra & Rheinboldt (1990). The idea is to regard the differential-algebraic system as a differential equation on a manifold (see Sect. VII.1) and to solve the equation in this manifold by introducing suitable local coordinates.

Let us illustrate this approach at the pendulum example. The equations, formulated in cartesian coordinates,are given in the beginning of this section. The solution manifold is (compare with Eq.(1.22))

$$
\mathcal { M } = \big \{ ( x , y , u , v ) \mid x ^ { 2 } + y ^ { 2 } = 1 , x u + y v = 0 \big \} .
$$

This is a 2-dimensional manifold in $\mathbb { R } ^ { 4 }$ and can be parametrized by $( \varphi , \eta )$ as follows:

$$
\begin{array} { r l r l } { x = \cos \varphi , } & { { } } & { } & { { } u = - \eta \sin \varphi , } \\ { y = \sin \varphi , } & { { } } & { { } v = \eta \cos \varphi . } \end{array}
$$

A short calculation shows that the system (2.1a,b),(2.3),written in the new coordinates, leads to the well-known equation

$$
\varphi ^ { \prime } = \eta , \qquad \eta ^ { \prime } = - \cos \varphi .
$$

This differential equation can be solved numerically without any difficulties. The numerical approximation in the original coordinates is then obtained via (2.16). Obviously, the position and velocity constraints are satisfied exactly.

Although this example nicely illustrates the main ideas, it may be misleading. First of all, in typical applications it is not possible to use one and the same parametrization throughout the whole integration. Secondly, the choice of coordinates is usually not obvious and the transformed differential equation can be much more complicated than the original one (see for example Alishenas (1992)).

Local State Space Form. Suppose that the differential-algebraic system, which we want to solve, can be written as a differential equation

$$
y ^ { \prime } = v ( y ) , \qquad y \in { \mathcal { M } }
$$

on a smooth $d$ -dimensional manifold $M \subset \mathbb { R } ^ { n }$ .Consider a coordinate function $\omega : U \to V$ (sufficiently differentiable,bijective,and $\omega ^ { \prime } ( \eta )$ of full rank) between the open set $U \subset \mathbb { R } ^ { d }$ and $V \subset M$ ， and denote the coordinates in $U$ by $\eta \in \mathbb { R } ^ { d }$ Under the transformation $y = \omega ( \eta )$ the equation (2.18) becomes

$$
\omega ^ { \prime } ( \eta ) \eta ^ { \prime } = v \left( \omega ( \eta ) \right) .
$$

Since $v ( y ) \in T _ { y } \mathcal { M }$ for all $y \in M$ (see Eq.(1.19)), there exists $\eta ^ { \prime }$ such that (2.19) holds. Moreover $\eta ^ { \prime }$ is unique, because $\omega ^ { \prime } ( \eta )$ is of full rank. Using the notation $\omega ^ { \prime } ( \eta ) ^ { + } = { \left( \omega ^ { \prime } ( \eta ) ^ { T } \omega ^ { \prime } ( \eta ) \right) } ^ { - 1 } \omega ^ { \prime } ( \eta ) ^ { T }$ for the pseudo-inverse of $\omega ^ { \prime } ( \eta )$ we therefore obtain

$$
\eta ^ { \prime } = \omega ^ { \prime } ( \eta ) ^ { + } v ( \omega ( \eta ) ) ,
$$

which is an ordinary differential equation in $\mathbb { R } ^ { d }$ and is called local state space form of (2.18). Observe that different coordinate functions lead to different state space forms.

The numerical procedure for solving (2.18) is the following: suppose that an approximation $y _ { k } \in M$ of $y ( t _ { k } )$ is given. We then choose a coordinate function and apply a standard method (e.g. Runge-Kutta) with initial value $\eta _ { k } = \omega ^ { - 1 } ( y _ { k } )$ to the state space form (2.20). This yields an approximation $\eta _ { k + 1 }$ at time $t _ { k + 1 } .$ Finally, we put $y _ { k + 1 } = \omega \big ( \eta _ { k + 1 } \big )$ . By definition of this procedure, the numerical approximation $y _ { k + 1 }$ again lies in $M$

If one uses one and the same local state space form for the whole integration (as it is the case for the pendulum example, Eq.(2.17)), the convergence properties for (2.20) carry immediately over to (2.18) via the coordinate function $y = \omega ( \eta )$ In more complex situations it may be necessary to change the coordinates several times, and from a computational point of view it may even be more advantageous to change them in every integration step.

Theorem 2.2. Consider the above procedure for the numerical solution of (2.18), and denote by $y = \omega _ { k } ( \eta )$ the coordinate transformation of the k th step. If， in a neighbourhood of $\omega _ { k } ^ { - 1 } ( y _ { k } )$ ， the matrices $\omega _ { \boldsymbol { k } } ^ { \prime } ( \eta )$ and $\omega _ { k } ^ { \prime } ( \eta ) ^ { + }$ are uniformly bounded in $k$ ， then the convergence properties for standard ordinary differential equations carry over to the problem (2.18) on a manifold $\ M$

Proof. In the case of one-step methods we have

$$
y _ { k + 1 } = \omega _ { k } \Big ( \omega _ { k } ^ { - 1 } ( y _ { k } ) + h \Phi _ { k } \big ( \omega _ { k } ^ { - 1 } ( y _ { k } ) , h \big ) \Big ) ,
$$

where $\Phi _ { k } ( \eta , h )$ is the increment function of the method when applied to (2.20) with $\omega$ replaced by $\omega _ { k }$ . Due to the regularity assumptions on $\omega _ { k } ( \eta )$ ,this formula can be written as

$$
y _ { k + 1 } = y _ { k } + h \Psi _ { k } ( y _ { k } , h )
$$

and takes the form of a standard one-step method. The assumptions guarantee that the functions $\Psi _ { k }$ have a uniform Lipschitz constant with respect to the first argument. Therefore the convergence proofs of Sect.II.3 apply. For multistep methods the situation is analogous. □

Choice of Local Coordinates. Let us explain two choices for the constrained mechanical system (2.4), whose solution manifold is given by

$$
{ \mathcal { M } } = \{ ( q , u ) \mid g ( q ) = 0 , G ( q ) u = 0 \} .
$$

Here $q , u \in \mathbb { R } ^ { n }$ are generalized coordinates, $g ( q ) \in \mathbb { R } ^ { m }$ and $G ( q ) = g _ { q } ( q )$ .The adaptation to other differential-algebraic systems with known solution manifold is more or less straightforward.

Generalized Coordinate Partitioning (Wehage & Haug 1982). Assuming that the Jacobian $G ( q )$ has full row rank, there exists a partitioning $q = ( \eta , \widehat { \eta } )$ such that $g _ { \hat { \eta } } ( \eta , \widehat { \eta } )$ is invertible $( \eta \in \mathbb { R } ^ { n - m }$ ， $\widehat { \eta } \in \mathbb { R } ^ { m } )$ . By the Implicit Function Theorem the constraint $g ( q ) = 0$ can be solved for $\widehat { \eta }$ in a neighbourhood of a consistent value $q _ { 0 } = ( \eta _ { 0 } , \widehat { \eta } _ { 0 } )$ . Hence, there exists a function $\widehat { \eta } = h ( \eta )$ (defined for $\eta$ close to $\eta _ { 0 }$ ）such that $g ( \eta , h ( \eta ) ) = 0$ . With a corresponding partitioning $u = ( \nu , \widehat { \nu } )$ the velocity constraint becomes $g _ { \eta } ( \eta , \widehat { \eta } ) \nu + g _ { \widehat { \eta } } ( \eta , \widehat { \eta } ) \widehat { \nu } = 0$ and allows us to express $\widehat { \nu }$ in terms of $\eta , \nu$ as $\widehat { \nu } = k ( \eta , \nu )$ . A coordinate function is thus given by $\omega ( \eta , \nu ) =$ $\big ( ( \eta , h ( \eta ) ) , ( \nu , k ( \eta , \nu ) ) \big )$ ,and the differential equation in these local coordinates is

$$
\eta ^ { \prime } = \nu , \qquad \nu ^ { \prime } = \nu ^ { \prime } \bigl ( \omega ( \eta , \nu ) \bigr ) ,
$$

where $\nu ^ { \prime } ( q , u )$ collects the $\nu$ -components of the solution $u ^ { \prime } ( q , u )$ of the linear system (1.38e). We emphasize that for a numerical implementation the differential equation (2.22) need not be known analytically. However, a nonlinear system has to be solved each time when the right-hand side of (2.22) has to be evaluated.

Tangent Space Parametrization (Potra & Rheinboldt 1991, Yen 1993). Instead of partitioning the components of $q$ and $u$ we split the vectors $q - q _ { 0 }$ and $u - u _ { 0 }$ according to

$$
q - q _ { 0 } = Q _ { 0 } \eta + Q _ { 1 } \widehat { \eta } , \qquad u - u _ { 0 } = Q _ { 0 } \nu + Q _ { 1 } \widehat { \nu } ,
$$

where the columns of $Q _ { 0 }$ form a basis of the tangent space $\{ v \mid G ( q _ { 0 } ) v = 0 \}$ to the manifold $q ( q ) = 0$ , which is completed by the columns of $Q _ { 1 }$ to a basis of the whole space. The condition $g ( q ) = 0$ together with the first relation of (2.23) define (locally) $q$ and $\widehat { \eta }$ as functions of $\eta$ . Similarly, $G ( q ) u = 0$ and the second relation of (2.23) define $u$ and $\widehat { \nu }$ as functions of $\nu$ and $q$ . Denoting these relationships by $\widehat { \eta } = h ( \eta )$ ， $\widehat { \nu } = k ( \eta , \nu )$ ，we get formally the same coordinate function as in the previous example, and the state space form is given by

$$
\eta ^ { \prime } = \nu , \qquad \nu ^ { \prime } = Q _ { 0 } ^ { + } u ^ { \prime } \bigl ( \omega ( \eta , \nu ) \bigr ) ,
$$

where $Q _ { 0 } ^ { + } = ( Q _ { 0 } ^ { T } Q _ { 0 } ) ^ { - 1 } Q _ { 0 } ^ { T }$ is the pseudo-inverse of $Q _ { 0 }$ ,and $u ^ { \prime } ( q , u )$ denotes the solution of the linear system (2.5).

The evaluation of $h ( \eta )$ requires the solution of a nonlinear system,whose Jacobian is

$$
\left( \begin{array} { c c } { { I } } & { { - Q _ { 1 } } } \\ { { G ( q _ { 0 } ) } } & { { 0 } } \end{array} \right) .
$$

This suggests to take $- Q _ { 1 } = G ^ { T } ( q _ { 0 } )$ or better $- Q _ { 1 } = M ^ { - 1 } ( q _ { 0 } ) G ^ { \mathcal { T } } ( q _ { 0 } )$ ， so that simplified Newton iterations lead to linear systems with a matrix that already appears in (2.5). The linear system for the computation of $k ( \eta , \nu )$ has the same structure.

Due to the fact that the evaluation of the right-hand side of (2.24) requires the solution of a nonlinear system, the authors of this approach prefer the use of multistep methods which, in general, use less function evaluations than one-step methods. In connection with Runge-Kutta methods, Potra (1995) suggests the use of certain predicted values instead of the exact solutions of these nonlinear systems, and requires that only the approximation at the end of every step lies on the manifold $\mathcal { M }$ . The resulting algorithm is then equivalent to solving the index 1 problem combined with projections onto $\ M$ at the end of each step.

# Overdetermined Differential-Algebraic Equations

In contrast to the approach at the beginning of this section, where the constraint is replaced by one of its derivatives,we consider the original system and one or more derivatives of the constraints as a unity. For example, the equations of motion of a constrained mechanical system become

$$
\begin{array} { c } { { q ^ { \prime } = u } } \\ { { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) } } \\ { { 0 = G ( q ) u } } \\ { { 0 = g _ { q q } ( q ) ( u , u ) + G ( q ) M ( q ) ^ { - 1 } \left( f ( q , u ) - G ^ { T } ( q ) \lambda \right) . } } \end{array}
$$

This system is overdetermined,because we are concerned with more equations than unknowns. Nevertheless, it possesses a unique solution, if (1.47) is satisfied and consistent initial values are prescribed.

We illustrate the numerical solution of (2.25) with the BDF method.A formal application (see Sect. VI.2) gives

$$
\begin{array} { r l } & { q _ { k } - \widehat { q } - h \gamma u _ { k } = 0 } \\ & { M ( q _ { k } ) ( u _ { k } - \widehat { u } ) - h \gamma \big ( f ( q _ { k } , u _ { k } ) - G ^ { T } ( q _ { k } ) \lambda _ { k } \big ) = 0 } \\ & { g ( q _ { k } ) = 0 } \\ & { G ( q _ { k } ) u _ { k } = 0 } \\ & { g _ { q q } ( q _ { k } ) ( u _ { k } , u _ { k } ) + G ( q _ { k } ) M ( q _ { k } ) ^ { - 1 } \big ( f ( q _ { k } , u _ { k } ) - G ^ { T } ( q _ { k } ) \lambda _ { k } \big ) = 0 , } \end{array}
$$

were $\gamma = \beta _ { k } / \alpha _ { k }$ $\begin{array} { r } { \widehat { q } = \big ( \sum _ { \imath = 0 } ^ { k - 1 } \alpha _ { i } q _ { i } \big ) / \alpha _ { k } } \end{array}$ and $\begin{array} { r } { \widehat { u } = \big ( \sum _ { \imath = 0 } ^ { k - 1 } \alpha _ { i } u _ { i } \big ) / \alpha _ { k } } \end{array}$ general. A natural idea (Fuhrer 1988) is to search for a least square solution of (2.26). There are several ways to do this. One can consider different norms,or one can require some of the equations to be exactly satisfied and the remaining ones in a least square sense. Fuhrer & Leimkuhler (1991) impose all constraints $( 2 . 2 6 \mathrm { c } , \mathrm { d } , \mathrm { e } )$ ， and treat the remaining equations by the use of a special pseudoinverse. This can be achieved by introducing Lagrange multipliers $\mu _ { k } , \eta _ { k }$ in the first two equations

of (2.26) as follows:

$$
\begin{array} { r l } & { M ( { q } _ { k } ) ( { q } _ { k } - \widehat { q } - h \gamma { u } _ { k } ) + h \gamma \big ( { G } ^ { T } ( { q } _ { k } ) { \mu } _ { k } + ( { G } _ { q } ( { q } _ { k } ) { u } _ { k } ) ^ { T } { \eta } _ { k } \big ) = 0 } \\ & { M ( { q } _ { k } ) ( { u } _ { k } - \widehat { u } ) - h \gamma \big ( f ( { q } _ { k } , { u } _ { k } ) - { G } ^ { T } ( { q } _ { k } ) \lambda _ { k } \big ) + h \gamma { G } ^ { T } ( { q } _ { k } ) { \eta } _ { k } = 0 . } \end{array}
$$

For sufficiently small $h$ , the system (2.27a,b), $( 2 . 2 6 \mathrm { c } , \mathrm { d } , \mathrm { e } )$ has a locally unique solution, if (1.47) is satisfied.

Connection with GGL-Formulation. If we omit the acceleration constraint (2.26e), there is no need for two Lagrange multipliers, and we can put $\eta _ { k } = 0$ . The resulting system $( 2 . 2 7 \mathbf { a } , \mathbf { b } )$ ， $( 2 . 2 6 \mathrm { c } , \dot { \mathrm { d } } )$ is then nothing else than the standard BDF discretization of the system (1.48).

# Unstructured Higher Index Problems

We consider a general differential-algebraic system

$$
F ( u ^ { \prime } , u ) = 0 .
$$

For its numerical solution we shall construct an ‘underlying ODE’ (see Defini-tion 1.2) and solve it by any integration method. This approach has been developed in several papers by Campbell (1989,1993). We shall explain the main ideas following the presentation of Campbell & Moore (1995).

Inspired by the definition of the differentiation index we consider the derivative array equations

$$
F ( u ^ { \prime } , u ) = 0 , \ \frac { d F ( u ^ { \prime } , u ) } { d x } = 0 , \ \ldots , \ \frac { d ^ { m } F ( u ^ { \prime } , u ) } { d x ^ { m } } = 0
$$

which we write in compact form as

$$
{ \cal G } ( u ^ { \prime } , w , u ) = 0 ,
$$

where $\boldsymbol { w } = \left( u ^ { \prime \prime } , u ^ { \prime \prime \prime } , \ldots , u ^ { ( m + 1 ) } \right)$ collects the higher derivatives of $u$ .In Eq. (2.29) we consider $w , u$ , and also $u ^ { \prime }$ as independent variables. Besides the usual differentiability assumptions we assume that

(A1） the matrix $\left( \boldsymbol { G } _ { u ^ { \prime } } , \boldsymbol { G } _ { w } \right)$ is 1-full with respect to $u ^ { \prime }$ ; this means that the relation $G _ { u ^ { \prime } } \Delta u ^ { \prime } + G _ { w } \Delta w = 0$ implies $\Delta u ^ { \prime } = 0$ ；

(A2） the matrix $\left( \boldsymbol { G } _ { u ^ { \prime } } , \boldsymbol { G } _ { w } \right)$ has constant rank;  
(A3） the matrix $( G _ { u ^ { \prime } } , G _ { w } , G _ { u } )$ has full row rank.

These assumptions are required to hold in a neighbourhood of a particular solution of (2.28). The construction of the underlying ODE is based on the following lemma and on its proof.

Lemma 2.3 (Campbell & Moore 1995). Consider a sufficiently smooth problem (2.28) and assume that (A1), (A2), and (A3) hold. Then there exist coordinate partitions $\boldsymbol { w } = ( w _ { a } , w _ { b } )$ ， $\boldsymbol { u } = \left( \boldsymbol { u } _ { a } , \boldsymbol { u } _ { b } \right)$ (and also $u ^ { \prime } = \left( u _ { a } ^ { \prime } , u _ { b } ^ { \prime } \right)$ with the same partition

as for $u$ ), such that the derivative array equations (2.29) are equivalent to

$$
\begin{array} { r l r l } & { u _ { a } ^ { \prime } = f _ { a } ( u _ { b } ) , } & & { w _ { a } = \varphi _ { 2 } ( w _ { b } , u _ { b } ) } \\ & { u _ { b } ^ { \prime } = f _ { b } ( u _ { b } ) , } & & { u _ { a } = \varphi _ { 3 } ( u _ { b } ) } \end{array}
$$

in a neighbourhood of the consistent initial value $\left( { { u } _ { 0 } ^ { \prime } , { w } _ { 0 } , { u } _ { 0 } } \right)$ ·

Proof. We consider the matrix $( G _ { u ^ { \prime } } , G _ { w } , G _ { u } )$ evaluated at $\left( { { u } _ { 0 } ^ { \prime } , { w } _ { 0 } , { u } _ { 0 } } \right)$ and perform a QR factorization, where column permutations are restricted to components within the vectors $u ^ { \prime } , w$ ,and $u$ . This yields

$$
\begin{array} { r } { Q ^ { T } ( G _ { u ^ { \prime } } , G _ { w } , G _ { u } ) P = ( \begin{array} { c } { B _ { 1 } } \\ { 0 } \\ { 0 } \end{array} | \begin{array} { c c } { C _ { 1 } } & { C _ { 2 } } \\ { C _ { 3 } } & { C _ { 4 } } \\ { 0 } & { 0 } \end{array} | \begin{array} { c c } { D _ { 1 } } & { D _ { 2 } } \\ { D _ { 3 } } & { D _ { 4 } } \\ { D _ { 5 } } & { D _ { 6 } } \end{array} ) , } \end{array}
$$

where $B _ { 1 } , C _ { 3 } , D _ { 5 }$ are nonsingular by Assumption (A3), $Q$ is an orthogonal matrix，and $P = \mathrm { d i a g } \left( P _ { 1 } , P _ { 2 } , P _ { 3 } \right)$ withsuitable permutationmatrices $P _ { 1 } , P _ { 2 } , P _ { 3 }$ Fixing the permutation $P$ , We apply theabovefactorzationalsoto $\left( \boldsymbol { G } _ { u ^ { \prime } } , \boldsymbol { G } _ { w } , \boldsymbol { G } _ { u } \right)$ evaluated at an arbitrary point $( u ^ { \prime } , w , u )$ close to $\left( { { u } _ { 0 } ^ { \prime } , { w } _ { 0 } , { u } _ { 0 } } \right)$ .Because of Assumption (A2) this gives (2.31） with smooth matrices $Q , B _ { i } , C _ { i }$ ，and $D _ { i }$ .The decomposition (2.31) defines the partitions $\boldsymbol { w } = \left( \boldsymbol { w } _ { a } , \boldsymbol { w } _ { b } \right)$ and $\boldsymbol { u } = \left( \boldsymbol { u } _ { a } , \boldsymbol { u } _ { b } \right)$ . The first, second and fourth block-columns in (2.31) form an invertible matrix. The Implicit Function Theorem thus implies that (2.29) can be solved for $u ^ { \prime } , w _ { a } , u _ { a }$ ,and we obtain the equivalent system

$$
u ^ { \prime } = \varphi _ { 1 } ( w _ { b } , u _ { b } ) , \qquad w _ { a } = \varphi _ { 2 } ( w _ { b } , u _ { b } ) , \qquad u _ { a } = \varphi _ { 3 } ( w _ { b } , u _ { b } ) .
$$

We still have to show that the functions $\varphi _ { 1 }$ and $\varphi _ { 3 }$ are independent of $w _ { b }$ .By definition of the $\varphi _ { i }$ we have

$$
G \Big ( \varphi _ { 1 } ( w _ { b } , u _ { b } ) , \big ( \varphi _ { 2 } ( w _ { b } , u _ { b } ) , w _ { b } \big ) , \big ( \varphi _ { 3 } ( w _ { b } , u _ { b } ) , u _ { b } \big ) \Big ) = 0 .
$$

Differentiating with respect to $w _ { b }$ yields

$$
G _ { u ^ { \prime } } \cdot \frac { \partial \varphi _ { 1 } } { \partial w _ { b } } + G _ { w _ { a } } \cdot \frac { \partial \varphi _ { 2 } } { \partial w _ { b } } + G _ { w _ { b } } + G _ { u _ { a } } \cdot \frac { \partial \varphi _ { 3 } } { \partial w _ { b } } = 0 .
$$

Multiplying this relation by $Q ^ { T }$ ,we see from Eq.(2.31) that $D _ { 5 } { \left( \partial \varphi _ { 3 } / \partial w _ { b } \right) } = 0$ Since $D _ { 5 }$ is nonsingular, this implies $( \partial \varphi _ { 3 } / \partial w _ { b } ) = 0$ ，so that $\varphi _ { 3 }$ is independent of $w _ { b }$ . Assumption (A1) now implies from (2.32) that also $( \partial \varphi _ { 1 } / \partial w _ { b } )$ vanishes. This completes the proof of the lemma. □

Suppose that we know how to compute $f _ { a } ( u _ { b } ) , f _ { b } ( u _ { b } )$ and $\varphi _ { 3 } ( u _ { b } )$ for a given value $u _ { b }$ . From (2.30) we then have an ordinary differential equation for $u _ { b }$ ,which can be solved by any integration method (Runge-Kutta or multistep, explicit or implicit，...)，and the remaining components are given by $u _ { a } = \varphi _ { 3 } ( u _ { b } )$ .The numerical solution of this method thus preserves all constraints (also the hidden ones).

Computation of the Values $f _ { a } ( u _ { b } ) , \ f _ { b } ( u _ { b } )$ and $\varphi _ { 3 } ( u _ { b } )$ . It follows from Assump-tion (A3) that $( G _ { u ^ { \prime } } , G _ { w } , G _ { u } ) ^ { T } G = 0$ is equivalent to $G \simeq 0$ . Thus, for given $u _ { b }$ ， any method of finding the minimum $( u ^ { \prime } , w , u _ { a } )$ of the function $G T G$ may be used. Campbell & Moore (1995) propose the use of Gauss-Newton iterations.

Remark. A closely related algorithm has been proposed by Kunkel & Mehrmann (1996). Instead of extracting from the derivative array equations an ordinary differential equation for all variables, they extract an equivalent index 1 problem and solve it by standard integration methods. This modification usually requires one differentiation less of the original system (2.28).

# Exercises

1. Repeat the experiment of Fig.2.1 with other numerical methods (explicit Euler method,multistep methods,constant and variable step sizes,...). You will observe that in some situations the error in $g ( q _ { n } )$ grows only linearly, and the error in $G ( q _ { n } ) u _ { n }$ remains bounded. Try to explain this observation.   
2.a) Prove that the matrix in (2.5) is 1-full with respect to $u ^ { \prime }$ if and only if the restriction of $M$ to the kernel of $G$ is injective (this is exactly the condition that is needed in order to be able to apply the methods of this section). b) Show by examples that neither $M$ needs to be nonsingular nor $G$ has to be of full rank in order that the condition of part (a) is satisfied.

# VII.3 Multistep Methods for Index 2 DAE

BDF is so beautiful that it is hard to imagine something else could be better. (L. Petzold 1988,heard by P. Deuflhard)

Convergence results of multistep methods for problems of index at least 2 are harder to obtain than for semi-explicit index 1 problems (see Section VI.2). A first convergence result for BDF schemes, valid for linear constant coeficient DAE's of arbitrary index，was given by Sincovec,Erisman， Yip & Epton (1981). Convergence of BDF for nonlinear DAE systems was then studied by Gear, Gupta & Leimkuhler (1985),Lotstedt & Petzold (1986) and Brenan & Engquist (1988).An independent convergence analysis was given by Griepentrog & März (1986), März (1990). They considered general linear multistep methods and problems, where the differential and algebraic equations (and/or variables) are not explicitly separated.

There are several implementations of the BDF schemes for differential-algebraic systems. The most widely used code is DASSL of Petzold (1982). It is described in detail in the book of Brenan, Campbell & Petzold (1989). Further implementations are LSODI of Hindmarsh (1980) and SPRINT of Berzins & Furzeland (1985).

In this section we consider semi-explicit problems

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { 0 = g ( y ) . } } \end{array}
$$

We assume that $f$ and $g$ are sufficiently differentiable and that

$$
g _ { y } ( y ) f _ { z } ( y , z ) \mathrm { i s  i n v e r t i b l e }
$$

in a neighbourhood of the solution，so that the problem has index 2. A linear multistep method for(3.1) reads

$$
\begin{array} { c } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { i } y _ { n + \imath } = h \sum _ { \imath = 0 } ^ { k } \beta _ { i } f ( y _ { n + i } , z _ { n + i } ) } } \\ { { 0 = g ( y _ { n + k } ) . } } \end{array}
$$

This is not the only meaningful definition of a multistep method for (3.1). One could as well replace (3.3b) by

$$
0 = \sum _ { \imath = 0 } ^ { k } \beta _ { i } g ( y _ { n + i } ) ,
$$

E. Hairer and G. Wanner, Solving Ordinary Diferential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_33, $©$ Springer-Verlag Berlin Heidelberg 2010

which is obtained by putting $\varepsilon \approx 0$ in (VI.2.1). The following results can be extended without any difficulty to the second approach. For BDF schemes (where $\beta _ { 0 } = . ~ . ~ . = \beta _ { k - 1 } = 0 ^ { \setminus }$ ）both definitions are equivalent.

The convergence results of this section are also valid for index 2 systems of the form $y \prime = f ( y , z )$ ， $0 = g ( y , z )$ ,if they can be transformed to (3.1) without any differentiation (see the discussion after Eq.(1.14)). This is because the multistep method (3.3) is invariant with respect to these transformations. The same is true for problems of the form $M ( u ) u ^ { \prime } = \varphi ( u )$ , if the multistep method is defined by

$$
\sum _ { i = 0 } ^ { k } \alpha _ { i } u _ { n + i } = h \sum _ { i = 0 } ^ { k } \beta _ { i } v _ { n + i } , \qquad M ( u _ { n + k } ) v _ { n + k } = \varphi ( u _ { n + k } ) .
$$

# Existence and Uniqueness of Numerical Solution

Equations (3.3) constitute a nonlinear system for $y _ { n + k } , z _ { n + k }$ . We have the follow-ing result about the existence of its solution.

Theorem 3.1. Suppose that for a solution $y ( x ) , z ( x )$ of(3.1) the starting values satisfy for $j = 0 , \ldots , k - 1$ and $x _ { j } = x _ { 0 } + j h$

$$
y _ { \ j } - y ( x _ { j } ) = \mathcal O ( h ) , \qquad z _ { j } - z ( x _ { \ j } ) = \mathcal O ( h ) , \qquad g ( y _ { \ j } ) = \mathcal O ( h ^ { 2 } ) .
$$

If(3.2) holds in $a$ neighbourhood of this solution and if $\beta _ { k } \neq 0$ , then the nonlinear system

$$
\sum _ { \imath = 0 } ^ { k } \alpha _ { i } y _ { i } = h \sum _ { i = 0 } ^ { k } \beta _ { \imath } f ( y _ { \imath } , z _ { i } )
$$

has a solution for $h \leq h _ { 0 }$ . This solution is locally unique and satisfes

$$
y _ { k } - y ( x _ { k } ) = \mathcal { O } ( h ) , \qquad z _ { k } - z ( x _ { k } ) = \mathcal { O } ( h ) .
$$

Proof. We put

$$
\eta = - \sum _ { \iota = 0 } ^ { k - 1 } \frac { \alpha _ { \iota } } { \alpha _ { k } } y _ { \iota } + h \sum _ { \iota = 0 } ^ { k - 1 } \frac { \beta _ { \iota } } { \alpha _ { k } } f ( y _ { \iota } , z _ { \iota } )
$$

and define $\zeta$ close to $z ( x _ { k } )$ such that $g _ { y } ( \eta ) f ( \eta , \zeta ) = 0$ .We further replace $h ( \beta _ { k } / \alpha _ { k } )$ by a new step size which we again denote by $h$ . Then the system (3.7) is equivalent to

$$
\begin{array} { c } { { y _ { k } = \eta + h f ( y _ { k } , z _ { k } ) } } \\ { { 0 = g ( y _ { k } ) } } \end{array}
$$

which is simply the implicit Euler method.

We next show that

$$
\eta - y ( x _ { k } ) = { \cal O } ( h ) , \qquad \zeta - z ( x _ { k } ) = { \cal O } ( h ) , \qquad g ( \eta ) = { \cal O } ( h ^ { 2 } ) .
$$

$y _ { \jmath } - y ( x _ { \jmath } ) = \mathcal { O } ( h )$ ard from $\textstyle \sum _ { i = 0 } ^ { k } \alpha _ { i } = 0$ $\zeta$ (3.11) can be seen as follows: we replace all $f ( y _ { \imath } , z _ { i } )$ in (3.9) by $f ( y ( x _ { k } ) , z ( x _ { k } ) )$ ， introducing an error of size $\mathcal { O } ( h ^ { 2 } )$ in $\eta$ . Hence

$$
\eta - y ( x _ { k } ) = - \sum _ { i = 0 } ^ { k - 1 } \frac { \alpha _ { i } } { \alpha _ { k } } \left( y _ { i } - y ( x _ { k } ) \right) + h \left( \sum _ { i = 0 } ^ { k - 1 } \frac { \beta _ { i } } { \alpha _ { k } } \right) f \bigl ( y ( x _ { k } ) , z ( x _ { k } ) \bigr ) + { \cal O } ( h ^ { 2 } ) .
$$

Because of (1.14b,c) this implies

$$
g ( \eta ) = - \sum _ { i = 0 } ^ { k - 1 } \frac { \alpha _ { i } } { \alpha _ { k } } g _ { y } \big ( y ( x _ { k } ) \big ) \big ( y _ { i } - y ( x _ { k } ) \big ) + \mathcal { O } ( h ^ { 2 } ) .
$$

The last statement of (3.11) now followsfrom the fact that $g _ { y } ( y ( x _ { k } ) ) ( y _ { i } - y ( x _ { k } ) ) =$ $g ( y _ { i } ) + \mathcal { O } ( h ^ { 2 } )$ and from (3.6).

To show the existence of a locally unique solution of (3.1O), it is possible to adapt the proof of “Theorem $4 . 1 ^ { \dag }$ of HLR89 to the implicit Euler method. We shall, however, reformulate (3.1O) in such a way that the implicit function theorem is applicable. We write (3.10b) as

$$
\begin{array} { c } { { 0 = g ( y _ { k } ) = g ( y _ { k } ) - g \big ( \eta ( h ) \big ) + g \big ( \eta ( h ) \big ) } } \\ { { \displaystyle = \int _ { 0 } ^ { 1 } g _ { y } \Big ( \eta ( h ) + \tau \big ( y _ { k } - \eta ( h ) \big ) \Big ) d \tau \cdot \big ( y _ { k } - \eta ( h ) \big ) + g \big ( \eta ( h ) \big ) } } \end{array}
$$

where we have explicitly indicated the dependence of $\eta$ on $h$ . Replacing the factor $y _ { k } - \eta ( h )$ by $h f ( y _ { k } , z _ { k } )$ from (3.10a) and dividing by $h$ we get the system

$$
\begin{array} { l } { { \displaystyle y _ { k } - \eta \big ( h \big ) - h f \big ( y _ { k } , z _ { k } \big ) = 0 } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } g _ { y } \Big ( \eta \big ( h \big ) + \tau \big ( y _ { k } - \eta ( h ) \big ) \Big ) d \tau \cdot f \big ( y _ { k } , z _ { k } \big ) + \frac { 1 } { h } g \big ( \eta ( h ) \big ) = 0 } } \end{array}
$$

which is the discrete analogue of system $_ { ( 1 . 1 4 a , \mathbf { c } ) }$ For $h = 0$ the values $y _ { k } =$ $\eta ( 0 )$ and $z _ { k } = \zeta ( 0 )$ satisfy (3.14) because $g ( \eta ( h ) ) = \mathcal { O } ( h ^ { 2 } )$ and $g _ { y } ( \eta ) f ( \eta , \zeta ) = 0$ Further, the derivative of (3.14) with repect to $\left( { y } _ { k } , \boldsymbol { z } _ { k } \right)$ is of the form

$$
\left( \begin{array} { c c } { I + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( 1 ) } & { ( g _ { y } f _ { z } ) ( \eta , \zeta ) + \mathcal { O } ( h ) } \end{array} \right) ,
$$

which has a bounded inverse for $h \leq h _ { 0 }$ . Therefore the implicit function theorem (Ortega & Rheinboldt 1970,p.128) yields the existence of a locally unique solution of (3.14) and hence also of (3.1O) and (3.7). □

# Influence of Perturbations

The influence of perturbations in the multistep formula (3.3) on the numerical solution will be studied in the next theorem.

Theorem 3.2. Let $y _ { k } , z _ { k }$ be given by (3.7) and consider perturbed values $\widehat { y } _ { k } , \widehat { z } _ { k }$ satisfying

$$
\begin{array} { c } { { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { i } \widehat { y } _ { i } = h \sum _ { i = 0 } ^ { k } \beta _ { i } f ( \widehat { y } _ { i } , \widehat { z } _ { i } ) + h \delta } } \\ { { 0 = g ( \widehat { y } _ { k } ) + \theta . } } \end{array}
$$

In addition to the assumptions of Theorem 3.1 suppose that for $j = 0 , \ldots , k - 1$

$$
\widehat y _ { j } - y _ { j } = { \cal O } ( h ^ { 2 } ) , \qquad \widehat z _ { j } - z _ { j } = { \cal O } ( h ) , \qquad \delta = { \cal O } ( h ) , \qquad \theta = { \cal O } ( h ^ { 2 } ) .
$$

Then, for $h \leq h _ { 0 }$ we have the estimates

$$
\begin{array} { l } { \displaystyle \| \widehat { y } _ { k } - y _ { k } \| \leq C \Big ( \| \widehat { Y } _ { 0 } - Y _ { 0 } \| + h \| \widehat { Z } _ { 0 } - Z _ { 0 } \| + h \| \delta \| + \| \theta \| \Big ) } \\ { \displaystyle \| \widehat { z } _ { k } - z _ { k } \| \leq \frac { C } { h } \Big ( \displaystyle \sum _ { j = 0 } ^ { k - 1 } \| g _ { y } ( \widehat { y } _ { k } ) ( \widehat { y } _ { j } - y _ { j } ) \| + h \| \widehat { Y } _ { 0 } - Y _ { 0 } \| } \\ { \displaystyle \qquad + h \| \widehat { Z } _ { 0 } - Z _ { 0 } \| + h \| \delta \| + \| \theta \| \Big ) } \end{array}
$$

wer $\widehat { Y } _ { 0 } - Y _ { 0 } = ( \widehat { y } _ { k - 1 } - y _ { k - 1 } , \ldots , \widehat { y } _ { 0 } - y _ { 0 } ) ^ { T } , \ \lVert \widehat { Y } _ { 0 } - Y _ { 0 } \rVert = \operatorname* { m a x } _ { 0 \leq \jmath \leq k - 1 } \lVert \widehat { y } _ { j } - y _ { j } \rVert ,$ $z$

Proof. In analogy to the proof of Theorem 3.1 we put

$$
\widehat { \eta } = - \sum _ { \iota = 0 } ^ { k - 1 } \frac { \alpha _ { i } } { \alpha _ { k } } \widehat { y } _ { i } + h \sum _ { i = 0 } ^ { k - 1 } \frac { \beta _ { i } } { \alpha _ { k } } f ( \widehat { y } _ { i } , \widehat { z } _ { i } )
$$

and rescale $h$ and $\delta$ , so that (3.16) becomes

$$
\begin{array} { c } { { \widehat { y } _ { k } = \widehat { \eta } + h f ( \widehat { y } _ { k } , \widehat { z } _ { k } ) + h \delta } } \\ { { 0 = g ( \widehat { y } _ { k } ) + \theta . } } \end{array}
$$

As in the proof of Theorem 3.1 we conclude from (3.17) that $\widehat { y } _ { k } - \widehat { \eta } = \mathcal { O } ( h )$ and $\widehat { z } _ { k } - \widehat { \zeta } = { \mathcal { O } } ( h )$ , where $\widehat { \zeta }$ is such that $g _ { y } ( \widehat { \eta } ) f ( \widehat { \eta } , \widehat { \zeta } ) = 0$ . Inspired by Eq.(3.14) we rewrite (3.19b) as

$$
0 = \int _ { 0 } ^ { 1 } g _ { y } \Big ( \widehat { \eta } + \tau \big ( \widehat { y } _ { k } - \widehat { \eta } \big ) \Big ) d \tau \cdot \big ( f ( \widehat { y } _ { k } , \widehat { z } _ { k } ) + \delta \big ) + \frac { 1 } { h } g ( \widehat { \eta } ) + \frac { 1 } { h } \theta ,
$$

which is now a discrete analogue of Eq.(1.29). Subtracting (3.20) from (3.14b) and

exploiting the fact that the matrix $g _ { y } f _ { z }$ is invertible, we deduce the estimate

$$
\| \widehat { z } _ { k } - z _ { k } \| \leq C \left( \| \widehat { y } _ { k } - y _ { k } \| + \| \widehat { \eta } - \eta \| + \| \delta \| + \frac { 1 } { h } \| g ( \widehat { \eta } ) - g ( \eta ) \| + \frac { 1 } { h } \| \theta \| \right) .
$$

A Lipschitz condition for $f$ applied to the diference of (3.19a) and (3.14a) yields

$$
\begin{array} { r } { \| \widehat { y } _ { k } - y _ { k } \| \leq \| \widehat { \eta } - \eta \| + h L \big ( \| \widehat { y } _ { k } - y _ { k } \| + \| \widehat { z } _ { k } - z _ { k } \| \big ) + h \| \delta \| . } \end{array}
$$

Combining the last two estimates we get

$$
\begin{array} { l } { \displaystyle | | \widehat { y } _ { k } - y _ { k } | | \leq C \big ( | | \widehat { \eta } - \eta | | + h | | \delta | | + | | \theta | | \big ) } \\ { \displaystyle | | \widehat { z } _ { k } - z _ { k } | | \leq \frac { C } { h } \big ( | | g _ { y } ( \widehat { \eta } ) ( \widehat { \eta } - \eta ) | | + h | | \widehat { \eta } - \eta | | + h | | \delta | | + | | \theta | | \big ) . } \end{array}
$$

The conclusion now follows from the definitions of $\eta$ and $\zeta$ and from $\widehat { y } _ { k } - \widehat { \eta } =$ ${ \mathcal { O } } ( h )$ □

Remark 3.3. a) The above proof shows that the constant $C$ in (3.18) depends on bounds for certain derivatives of $f$ and $g$ , but not on the constants implied by the $\mathcal { O } ( \dots )$ terms in (3.17) (if $h$ is sufficiently small). This observation will be used in the convergence proof below.

b) For one-step methods (e.g., implicit Euler method,trapezoidal rule) the term $\begin{array} { r } { \| \sum _ { J = 0 } ^ { k - 1 } g _ { y } \big ( \widehat { y } _ { k } \big ) \big ( \widehat { y } _ { j } - y _ { \jmath } \big ) \| } \end{array}$ at $g ( y _ { 0 } ) = g ( \widehat { y } _ { 0 } ) = 0$ Indeed, it follows from $\widehat { y } _ { \mathrm { 1 } } = \widehat { y } _ { \mathrm { 0 } } + \mathcal { O } ( h )$ that $g _ { y } ( \widehat { y } _ { 1 } ) ( \widehat { y } _ { 0 } - y _ { 0 } ) = g _ { y } ( \widehat { y } _ { 0 } ) ( \widehat { y } _ { 0 } - y _ { 0 } ) +$ $\mathcal { O } ( h \vert \vert \widehat { y } _ { 0 } - y _ { 0 } \vert \vert )$ . Further we have

$$
g _ { y } ( \widehat { y } _ { 0 } ) ( \widehat { y } _ { 0 } - y _ { 0 } ) = g ( \widehat { y } _ { 0 } ) - g ( y _ { 0 } ) + { \mathcal O } ( \| \widehat { y } _ { 0 } - y _ { 0 } \| ^ { 2 } ) ,
$$

so that the term in question is estimated by $\mathcal { O } ( h \| \widehat { y } _ { 0 } - y _ { 0 } \| )$ if $l _ { l }$ is sufficiently small.

# The Local Error

Consider initial values $y _ { j } = y ( x _ { j } )$ ， $z _ { \jmath } = z ( x _ { \jmath } ) ( j = 0 , \ldots , k - 1 )$ on the exact solution of (3.1) and apply the multistep formula (3.7) once. The differences $y _ { k } -$ $y ( x _ { k } )$ and $z _ { k } - z ( x _ { k } )$ are then called the local errors of the method.

Lemma 3.4. Suppose that the DAE (3.1) satisfies (3.2) and that the mulistep method (3.7) has order $p$ (in the sense of Sect.IlI.2). Then its local error satisfies

$$
y _ { k } - y ( x _ { k } ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad z _ { k } - z ( x _ { k } ) = \mathcal { O } ( h ^ { p } ) .
$$

Proof. We put $\widehat { y } _ { \prime } = y ( \boldsymbol { x } _ { \prime } ) , \widehat { z } _ { j } = z ( \boldsymbol { x } _ { \prime } )$ for $j = 0 , \ldots , k ^ { \circ }$ . These values satisfy (3.16) with $\ S = \mathcal { O } ( h ^ { \ i } ) \big \}$ and $\theta \simeq 0$ . Since ${ \widehat { y } } _ { j } = y _ { j }$ and $\widehat { z } _ { \jmath } = z _ { \jmath }$ for $j < k$ , thc statement follows immediately from Theorem 3.2. □

# Convergence for BDF

The study of convergence is simpler for BDF schemes than for general multi-step methods, because $y _ { n + k }$ depends only on $y _ { n } , \ldots , y _ { n + k - 1 }$ ,but not on $z _ { n } , \ldots ,$ $z _ { n + k - 1 }$ (due to $\beta _ { 0 } = . . . = \beta _ { k - 1 } = 0 .$ ). Therefore the $y$ - and $z$ -components can be treated separately. The following convergence result was obtained by Gear, Gupta &Leimkuhler (1985),Lotstedt & Petzold (1986) and Brenan & Engquist (1988).

Theorem 3.5. Consider an index 2 problem (3.1) which satisfes (3.2). Then the $k$ -step BDF scheme (II.1.22') is convergent of order $p = k$ ,if $k \leq 6 ; i . e .$ ，

$$
y _ { n } - y ( x _ { n } ) = O ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = O ( h ^ { p } ) \quad f o r \quad x _ { n } = n h \leq C o n s t ,
$$

whenever the initial values satisfy

$$
y _ { \jmath } - y ( x _ { \jmath } ) = \mathcal { O } ( h ^ { p + 1 } ) \qquad f o r \quad \jmath = 0 , \ldots , k - 1 .
$$

Remark. The assumption (3.25) can be relaxed to $y _ { j } - y ( x _ { j } ) = \mathcal { O } ( h ^ { p } )$ for $k \geq 3$ ， but not for $k = 1$ (see Exercise 1).

Proof. We combine the convergence proof for Runge-Kutta methods (HLR89, Theorem 4.4) with the techniques of Sect.III.4. Inspired by Lady Windermere's Fan (Fig.II.4.1） we first study the propagation of the local errors and their accumulation over the whole interval for the $y$ -component (part a). The $z$ -component is treated in part (b) and technical details are given in part (c).

a) In addition to the numerical solution $\{ y _ { n } , z _ { n } \}$ ，which we now also denote by $\{ y _ { n } ^ { 0 } , z _ { n } ^ { 0 } \}$ ， we consider for $\ell = 1 , 2 , \ldots$ the multistep solutions $\{ y _ { n } ^ { \ell } , z _ { n } ^ { \ell } \}$ with starting values $y _ { \jmath } ^ { \ell } = y ( x _ { j } )$ ， $z _ { \jmath } ^ { \ell } = z ( x _ { j } )$ for $j = \ell - 1 , \ldots , \ell + k - 2$ on the exact solutionOurfirstaimis to etiate $y _ { n } ^ { \ell } - y _ { n } ^ { \ell + 1 }$ in terms of the local errors $y _ { \ell + k - 1 } ^ { \ell } - y _ { \ell + k - 1 } ^ { \ell + 1 }$ (or starting errors if $\ell = 0$ ). For simplicity we omit the upper index and consider two neighbouring multistep solutions $\{ \widehat { y } _ { n } , \widehat { z } _ { n } \}$ and $\{ \widetilde { y } _ { n } , \widetilde { z } _ { n } \}$ · In order to be able to apply Theorem 3.2 we fix three sufficiently large constants $C _ { 0 } , C _ { 1 } , C _ { 2 }$ and suppose that for $n h \le C o n s t$

$$
\begin{array} { r } { \| \widehat { \boldsymbol { y } } _ { n } - \boldsymbol { y } ( \boldsymbol { x } _ { n } ) \| \leq C _ { 0 } h , \qquad \| \widetilde { \boldsymbol { y } } _ { n } - \widehat { \boldsymbol { y } } _ { n } \| \leq C _ { 1 } h ^ { 2 } , \qquad \| \widehat { \boldsymbol { z } } _ { n } - \boldsymbol { z } ( \boldsymbol { x } _ { n } ) \| \leq C _ { 2 } h . } \end{array}
$$

This willbe justified in part (c) below. We introduce the notation $\Delta y _ { n } = \widetilde { y } _ { n } -$ $\widehat { y } _ { n } , \Delta z _ { n } = \widetilde { z } _ { n } - \widehat { z } _ { n }$ and $\Delta Y _ { n } = ( \Delta y _ { n + k - 1 } , . . . , \Delta y _ { n } ) ^ { T }$ Observing that $y _ { n + k } ,$ $z _ { n + k }$ do not depend on $z _ { n } , \ldots , z _ { n + k - 1 }$ for the BDF schemes, it follows from Theorem 3.2 with $\delta \approx 0$ and $\theta = 0$ that

$$
\begin{array} { l } { \| \Delta y _ { n + k } \| \leq C \| \Delta Y _ { n } \| } \\ { \| \Delta z _ { n + k } \| \leq \displaystyle \frac { C } { h } \left( \displaystyle \sum _ { j = 0 } ^ { k - 1 } \| g _ { y } ( \widehat { y } _ { n + k } ) \Delta y _ { n + j } \| + h \| \Delta Y _ { n } \| \right) . } \end{array}
$$

Here $C$ does not depend on the choice of $C _ { 0 } , C _ { 1 } , C _ { 2 }$ ,if $h$ is sufficiently small (see Remark 3.3a). Our assumption (3.26) together with (3.27) implies $\Delta y _ { n + k } = \mathcal { O } ( h ^ { 2 } )$

and $\Delta z _ { n + k } = \mathcal { O } ( h )$ . We therefore obtain by linearization of the multistep formula

$$
\begin{array} { c } { \displaystyle \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } \Delta y _ { n + \imath } = h \beta _ { k } f _ { z } ( \widehat { y } _ { n + k } , \widehat { \widetilde { \mathbf { \zeta } } } _ { n + k } ) \Delta z _ { n + k } + \mathcal O ( h \| \Delta \mathrm { Y } _ { n } \| ) } \\ { 0 = g _ { y } ( \widehat { y } _ { n + k } ) \Delta y _ { n + k } + \mathcal O ( h \| \Delta Y _ { n } \| ) . } \end{array}
$$

We next use the projections (see also Definition 4.3 below)

$$
\begin{array} { r } { Q _ { n } = \big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \big ) ( \widehat { y } _ { n + k } , \widehat { z } _ { n + k } ) . \qquad P _ { n } = I - Q _ { n } } \end{array}
$$

for which

$$
P _ { n } ^ { 2 } = P _ { n } , \quad Q _ { n } ^ { 2 } = Q _ { n } , \quad P _ { n } Q _ { n } = Q _ { n } P _ { n } = 0 , \quad Q _ { n + 1 } = Q _ { n } + \mathcal { O } ( h ) .
$$

The last relation of (3.30) follows from (3.26) and the smoothness of the solution $y ( x ) , z ( x )$ We then multiply (3.28a) by $P _ { n + k }$ (which eliminates $\Delta z _ { n + k } )$ and (3.28b) by $f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 }$ . This yields with (3.30)

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } P _ { n + i } \Delta y _ { n + \ i } = \mathcal { O } ( h \| \Delta Y _ { n } \| ) , \qquad Q _ { n + k } \Delta y _ { n + k } = \mathcal { O } ( h \| \Delta Y _ { n } \| ) .
$$

Introducing the vectors

$$
\begin{array} { r } { U _ { n } = ( P _ { n + k - 1 } \Delta y _ { n + k - 1 } , \dots , P _ { n } \Delta y _ { n } ) ^ { T } , } \\ { V _ { n } = ( Q _ { n + k - 1 } \Delta y _ { n + k - 1 } , \dots , Q _ { n } \Delta y _ { n } ) ^ { T } , } \end{array}
$$

we have $\Delta Y _ { n } = U _ { n } + V _ { n }$ and the relations (3.31) become

$$
\begin{array} { r } { U _ { n + 1 } = ( A \otimes I ) U _ { n } + \mathcal { O } ( h \| U _ { n } \| + h \| V _ { n } \| ) } \\ { V _ { n + 1 } = ( N \otimes I ) V _ { n } + \mathcal { O } ( h \| U _ { n } \| + h \| V _ { n } \| ) } \end{array}
$$

where (with $\alpha _ { \ j } ^ { \prime } = \alpha _ { \ j } / \alpha _ { k } )$

$$
A = \left( \begin{array} { c c c c } { - \alpha _ { k - 1 } ^ { \prime } } & { \ldots } & { - \alpha _ { 1 } ^ { \prime } } & { - \alpha _ { 0 } ^ { \prime } } \\ { 1 } & { } & { 0 } & { 0 } \\ { } & { \ddots } & { \vdots } & { \vdots } \\ { } & { } & { 1 } & { 0 } \end{array} \right) , \quad N = \left( \begin{array} { c c c c } { 0 } & { \ldots } & { 0 } & { 0 } \\ { 1 } & { } & { 0 } & { 0 } \\ { } & { \ddots } & { \vdots } & { \vdots } \\ { } & { } & { 1 } & { 0 } \end{array} \right) .
$$

According to Lemma II1.4.4 we now choose a norm $\{ \{ U \} \}$ such that $\| A \otimes I \| \leq 1$ ， We then choose a (possibly different） norm $\{ \{ V \} \}$ ， for which $\| N \otimes I \| \leq \varrho < 1$ Consequently it follows from (3.32) that

$$
\begin{array} { r } { \left( \begin{array} { l } { \| U _ { n + 1 } \| } \\ { \| V _ { n + 1 } \| } \end{array} \right) \leq \left( \begin{array} { l l } { 1 + \mathcal { O } ( h ) } & { \quad \mathcal { O } ( h ) } \\ { \quad \mathcal { O } ( h ) } & { \varrho + \mathcal { O } ( h ) } \end{array} \right) \left( \begin{array} { l } { \| U _ { n } \| } \\ { \| V _ { n } \| } \end{array} \right) . } \end{array}
$$

As in the proof of Lemma VI.3.9 we diagonalize the matrix in (3.34) and so obtain

$$
\begin{array} { r l r } {  { \| \Delta Y _ { n } \| \leq C o n s t _ { 1 } \big ( \| U _ { n } \| + \| V _ { n } \| \big ) } } \\ & { } & { \leq C o n s t _ { 2 } \big ( \| U _ { 0 } \| + ( \varrho ^ { n } + h ) \| V _ { 0 } \| \big ) , } \\ & { } & { \| V _ { n } \| \leq C o n s t _ { 3 } \big ( h \| U _ { 0 } \| + ( \varrho ^ { n } + h ) \| V _ { 0 } \| \big ) . } \end{array}
$$

The vectors $U _ { 0 }$ and $V _ { 0 }$ are composed of local errors (of the $y$ -component） or of errors in the starting values, which are of size $\mathcal { O } ( h ^ { p + 1 } )$ by (3.23) and (3.25). Hence, it follows from (3.35) that the propagated errors satisfy

$$
\begin{array} { c } { \left\| \Delta y _ { n } \right\| \leq C _ { 3 } h ^ { p + 1 } , } \\ { \left\| g _ { y } ( \widehat { y } _ { n + k } ) \Delta y _ { n + j } \right\| \leq C _ { 4 } ( \varrho ^ { n } + h ) h ^ { p + 1 } \quad \mathrm { f o r } j = 0 , \ldots , k - 1 . } \end{array}
$$

Summing up we obtain

$$
\| y _ { n } - y ( x _ { n } ) \| \leq \sum _ { \ell = 0 } ^ { n - k + 1 } \| y _ { n } ^ { \ell } - y _ { n } ^ { \ell + 1 } \| \leq C _ { 5 } h ^ { p } ,
$$

the desired estimate for the $y$ -component.

b) Since $z _ { n }$ depends only on $y _ { n - k } , \ldots , y _ { n - 1 }$ but not on the previous $z$ -values, we can apply Theorem 3.2 with $\widehat { y } _ { \ i } = y ( x _ { i } ) , \widehat { z } _ { i } = z ( x _ { i } ) , \delta = \mathcal { O } ( h ^ { p } )$ and $\theta = 0$ . This yields

$$
\| z _ { n } - z ( x _ { n } ) \| \leq { \frac { C } { h } } \sum _ { j = 1 } ^ { k } \| g _ { y } \big ( y ( x _ { n } ) \big ) \big ( y _ { n - j } - y ( x _ { n - j } ) \big ) \| + { \mathcal O } ( h ^ { p } ) .
$$

Using (3.36) and $y _ { n } ^ { \ell } = y ( x _ { n } ) + \mathcal { O } ( h ^ { p } )$ , which follows as in (3.37), we obtain

$$
| | g _ { y } \big ( y ( x _ { n } ) \big ) \big ( y _ { n - \jmath } - y ( x _ { n - \jmath } ) \big ) | | = \bigg | \bigg | \sum _ { \ell = 0 } ^ { n - k + 1 } g _ { y } \big ( y ( x _ { n } ) \big ) \big ( y _ { n - \jmath } ^ { \ell } - y _ { n - \jmath } ^ { \ell + 1 } \big ) \bigg | |
$$

$$
\leq \ \sum _ { \ell = 0 } ^ { n - k + 1 } \Big ( \big \| g _ { y } ( y _ { n } ^ { \ell } ) \big ( y _ { n - \jmath } ^ { \ell } - y _ { n - j } ^ { \ell + 1 } \big ) \big \| + \mathcal { O } ( h ^ { 2 p + 1 } ) \Big ) = \mathcal { O } ( h ^ { p + 1 } )
$$

and hence also

$$
\lVert z _ { n } - z ( x _ { n } ) \rVert \leq C _ { 6 } h ^ { p } .
$$

c) In general, the constants $C _ { 3 } , C _ { 5 }$ and $C _ { 6 }$ will depend on $C _ { 0 } , C _ { 1 } , C _ { 2 }$ of our assumption (3.26). For $p \geq 2$ we can restrict the step size $h$ so that

$$
C _ { 5 } h ^ { p - 1 } \leq C _ { 0 } , \qquad C _ { 3 } h ^ { p - 1 } \leq C _ { 1 } , \qquad C _ { 6 } h ^ { p - 1 } \leq C _ { 2 }
$$

and the numerical solutions will never violate the conditions (3.26) on the considered interval.

For $p = 1$ (the implicit Euler method) we know from Remark 3.3b that the estimate (3.27b) can be replaced by

$$
\| \Delta z _ { n + k } \| \leq C \| \Delta Y _ { n } \| .
$$

Instead of (3.28a) we thus immediately get

$$
\Delta y _ { n + 1 } - \Delta y _ { n } = \mathcal { O } ( h | | \Delta y _ { n } | | )
$$

where the constant implied by the $\mathcal { O } ( \dots )$ term is independent of $C _ { 0 } , C _ { 1 } , C _ { 2 }$ ,if $h$ is sufficiently small. Standard techniques (without considering the projections (3.29)) then yield the convergence result. □

With the ideas of Sect.III.5 the above proof can be extended to cover variable step sizes as well. Originally, such a convergence result was given by Gear, Gupta &Leimkuhler (1985).

# General Multistep Methods

For a general multistep method (3.3) with generating polynomials

$$
\varrho ( \zeta ) = \sum _ { \iota = 0 } ^ { k } \alpha _ { \iota } \zeta ^ { \iota } , \qquad \sigma ( \zeta ) = \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } \zeta ^ { \iota }
$$

we have the following convergence result.

Theorem 3.6. Consider an index2 problem(3.1) which satisfies (3.2). Assume that the multistep method is stable (Definition II1.3.2) and strictly stable at infinity (the zeros of $\sigma ( \zeta )$ lie inside the unit disc $| \zeta | < 1 )$ . If its order is $\smash {  { p _ { \perp } } \geq 2 }$ , then the global error satisfies

$$
y _ { n } - y ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) \quad f o r \quad x _ { n } = n h \leq C o n s t
$$

whenever the initial values satisfy $( f o r \ j = 0 , \ldots , k - 1 )$

$$
y _ { \jmath } - y ( x _ { \jmath } ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad z _ { \jmath } - z ( x _ { \jmath } ) = \mathcal { O } ( h ^ { p } ) .
$$

Proof. The proof is essentially the same as for the BDF schemes. Due to the dependence of $y _ { n + k } , z _ { n + k }$ on $y _ { n } , \ldots , y _ { n + k - 1 }$ and on $z _ { n } , \ldots , z _ { n + k - 1 }$ the following modifications are necessary.

In addition to (3.26) we assume $\| { \widetilde { z } } _ { n } - { \widehat { z } } _ { n } \| \leq C _ { 3 } h ,$ . Instead of (3.27) we have (from Theorem 3.2)

$$
\begin{array} { r l } & { \displaystyle \| \Delta y _ { n + k } \| \leq C \big ( \| \Delta Y _ { n } \| + h \| \Delta Z _ { n } \| \big ) } \\ & { \displaystyle \| \Delta z _ { n + k } \| \leq \frac { C } { h } \bigg ( \displaystyle \sum _ { j = 0 } ^ { k - 1 } \| g _ { y } \big ( \widehat { y } _ { n + k } \big ) \Delta y _ { n + j } \| + h \| \Delta Y _ { n } \| + h \| \Delta Z _ { n } \| \bigg ) } \end{array}
$$

and (3.28) becomes

$$
\begin{array} { r l r } {  { \sum _ { \imath = 0 } ^ { k } \alpha _ { \imath } \Delta y _ { n + i } = h \sum _ { \imath = 0 } ^ { k } \beta _ { \imath } f _ { z } ( \widehat { y } _ { n + k } , \widehat { z } _ { n + k } ) \Delta z _ { n + \imath } + { \mathcal O } ( h \| \Delta Y _ { n } \| + h ^ { 2 } \| \Delta Z _ { n } \| ) } } \\ & { } & { \quad \quad \quad 0 = g _ { y } ( \widehat { y } _ { n + k } ) \Delta y _ { n + k } + { \mathcal O } ( h \| \Delta Y _ { n } \| + h ^ { 2 } \| \Delta Z _ { n } \| ) . \quad \quad ( 3 . } \end{array}
$$

A recursion for $\Delta z _ { n }$ is obtained as follows: we multiply the upper linc of (3.43) by $\left( ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \right) \left( { \widehat { y } } _ { n + k } , { \widehat { z } } _ { n + k } \right)$ and so get

$$
\begin{array} { r l } {  { h \sum _ { \iota = 0 } ^ { k } \beta _ { \iota } \Delta z _ { n + \iota } = \sum _ { \iota = 0 } ^ { k } \alpha _ { \iota } ( ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } ) ( \widehat { y } _ { n + k } , \widehat { z } _ { n + k } ) \Delta y _ { n + \iota } } } \\ & { \quad + \ O \big ( h \| \Delta Y _ { n } \| + h ^ { 2 } \| \Delta Z _ { n } \| \big ) . } \end{array}
$$

With the projections $P _ { n } , Q _ { n }$ of(3.29) and the vectors $U _ { n } , V _ { n }$ we thus obtain (3.32) with an additional $\mathcal { O } ( h ^ { 2 } \Vert \Delta Z _ { n } \Vert )$ ）term. From (3.44) we get

$$
\begin{array} { r } { h \Delta Z _ { n + 1 } = ( B \otimes I ) h \Delta Z _ { n } + \mathcal { O } \Big ( h \| U _ { n } \| + \| V _ { n } \| + h ^ { 2 } \| \Delta Z _ { n } \| \Big ) , } \end{array}
$$

where

$$
B = \left( \begin{array} { c c c c } { - \beta _ { k - 1 } ^ { \prime } } & { \hdots } & { - \beta _ { 1 } ^ { \prime } } & { - \beta _ { 0 } ^ { \prime } } \\ { 1 } & { } & { 0 } & { 0 } \\ { } & { \ddots } & { \vdots } & { \vdots } \\ { } & { } & { \vdots } & { \vdots } \end{array} \right)
$$

with $\beta _ { \jmath } ^ { \prime } = \beta _ { j } / \beta _ { k }$ . For this equation we use a norm for which $\| B \otimes I \| \leq \kappa < 1$ This is possible, because the method is strictly stable at infinity. Summarizing, we get the inequality

$$
\begin{array} { r } { \left( \begin{array} { c } { \| U _ { n + 1 } \| } \\ { \| V _ { n + 1 } \| } \\ { h \| \Delta Z _ { n + 1 } \| } \end{array} \right) \le \left( \begin{array} { c c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( h ) } & { \varrho + \mathcal { O } ( h ) } & { \mathcal { O } ( h ) } \\ { \mathcal { O } ( h ) } & { \mathcal { O } ( 1 ) } & { \kappa + \mathcal { O } ( h ) } \end{array} \right) \left( \begin{array} { c } { \| U _ { n } \| } \\ { \| V _ { n } \| } \\ { h \| \Delta Z _ { n } \| } \end{array} \right) } \end{array}
$$

which can be solved as before and yields

$$
\begin{array} { r l } & { \| \Delta y _ { n } \| \leq C _ { 3 } h ^ { p + 1 } , \qquad \| \Delta z _ { n } \| \leq C _ { 7 } ( \varrho ^ { n } + \kappa ^ { n } + h ) h ^ { p } , } \\ & { \| g _ { y } ( \widehat { y } _ { n + k } ) \Delta y _ { n + j } \| \leq C _ { 4 } ( \varrho ^ { n } + \kappa ^ { n } + h ) h ^ { p + 1 } \qquad \mathrm { f o r ~ } j = 0 , \dots , k - 1 . } \end{array}
$$

Summing up the propagated errors as in (3.37) we obtain the desired estimates for the $y$ -and $z$ -component. □

# Solution of the Nonlinear System by Simplified Newton

The nonlinear system (3.3) is usually solved by a simplified Newton iteration and it is interesting to study its convergence. As in the proof of Theorem 3.1 we introduce $\eta$ by (3.9) and rescale $h$ so that the nonlinear system becomes (omitting the indices)

$$
\begin{array} { r } { y - \eta - h f ( y , z ) = 0 } \\ { g ( y ) = 0 . } \end{array}
$$

This is just the implicit Euler method and we can apply the discussion of HLR89, Chapter 7. The Jacobian of the nonlinear system (3.47) is

$$
J = \left( \begin{array} { c c } { { I - h f _ { y } } } & { { - h f _ { z } } } \\ { { g _ { y } } } & { { 0 } } \end{array} \right)
$$

and its inverse has the form

$$
J ^ { - 1 } = \left( \begin{array} { c c } { { P + \mathcal { O } ( h ) } } & { { f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } + \mathcal { O } ( h ) } } \\ { { - h ^ { - 1 } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } + \mathcal { O } ( 1 ) } } & { { h ^ { - 1 } ( g _ { y } f _ { z } ) ^ { - 1 } + \mathcal { O } ( 1 ) } } \end{array} \right)
$$

where $P = I - f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y }$ is the projection of (3.29). We now consider the

simplified Newton method as a fixed point iteration with the function

$$
\Phi ( y , z ) = \left( { \begin{array} { c } { y } \\ { z } \end{array} } \right) - J _ { 0 } ^ { - 1 } \left( { \begin{array} { c } { y - \eta - h f ( y , z ) } \\ { g ( y ) } \end{array} } \right) .
$$

The subscript $0$ in $J _ { 0 }$ indicates that the argumcnts of the derivatives in (3.48) are evaluated at some fixed approximation $( \widehat { \eta } , \widehat { \zeta } )$ to the solution of (3.47). We shall use the notation $\{ f _ { y } \} _ { 0 }$ for $f _ { y } ( \widehat { \eta } , \widehat { \zeta } )$ , etc. Direct calculation of $\Phi ^ { \prime } ( y , z )$ gives

$$
\begin{array} { r } { \left( \begin{array} { l l } { \{ f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \} _ { 0 } ( \{ g _ { y } \} _ { 0 } - g _ { y } ) + \mathcal { O } ( h ) } & { h \{ P \} _ { 0 } f _ { z } + \mathcal { O } ( h ^ { 2 } ) } \\ { h ^ { - 1 } \{ ( g _ { y } f _ { z } ) ^ { - 1 } \} _ { 0 } ( \{ g _ { y } \} _ { 0 } - g _ { y } ) + \mathcal { O } ( 1 ) } & { \{ ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \} _ { 0 } ( \{ f _ { z } \} _ { 0 } - f _ { z } ) + \mathcal { O } ( h ) } \end{array} \right) . } \end{array}
$$

If we assume that $( \widehat { \eta } , \widehat { \zeta } )$ approximates the fixed point of (3.5O) with an error of $\mathcal { O } ( h )$ , then we have at this fixed point

$$
\Phi ^ { \prime } ( y , z ) = { \binom { { \mathcal { O } } ( h ) } { { \mathcal { O } } ( 1 ) } } \quad { \mathcal { O } } ( h ^ { 2 } ) \bigg ) .
$$

With the scaling matrix $D = \mathrm { d i a g } \left( I , h I \right)$ (this corresponds to a multiplication of the $z$ -variables by $h$ ) we havc $\| D \Phi ^ { \prime } ( y , z ) D ^ { - 1 } \| = { \mathcal { O } } ( h )$ . In the norm $\| y \| + h \| z \|$ we therefore gain a factor $h$ in each simplified Newton iteration.

Remark. The above analysis remains valid if $f _ { y }$ or parts of it are replaced by zero in $J _ { 0 }$ . For mechanical problems such an algorithm was proposed by Gear, Gupta &Leimkuhler (1985).

# Exercises

1. Show that the assumption $g ( y _ { \ i } ) = \mathcal { O } ( h ^ { 2 } )$ for $j = 0 , \ldots , k - 1$ cannot be omitted in Theorem 3.1.

Counterexample. Consider the system $x ^ { \prime } = 1 , y ^ { \prime } = k ( z ) , 0 = y - x$ ，where $k ( z ) = ( e ^ { z - 1 } + 1 ) / 2$ ．Apply the implicit Euler method with initial values $x _ { 0 } = 0 , y _ { 0 } = h , z _ { 0 } = 1$

2. (Gear,Hsu & Petzold 1981, Gear & Petzold 1984). Consider the problem

$$
\left( { \begin{array} { c c } { 0 } & { 0 } \\ { 1 } & { \eta x } \end{array} } \right) \left( { \begin{array} { c } { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} } \right) + \left( { \begin{array} { c c } { 1 } & { \eta x } \\ { 0 } & { 1 + \eta } \end{array} } \right) \left( { \begin{array} { c } { y } \\ { z } \end{array} } \right) = \left( { \begin{array} { c } { f ( x ) } \\ { g ( x ) } \end{array} } \right) .
$$

a) Prove that the system (3.52) has index 2 for all values of $1 7$

b) The $z$ -component of the exact solution is $z ( x ) = g ( x ) - f ^ { \prime } ( x )$

c) The implicit Euler method,applied to (3.52) in an obvious manner,yields the recursion

$$
z _ { n + 1 } = { \frac { \eta } { 1 + \eta } } z _ { n } + { \frac { 1 } { 1 + \eta } } \left( g ( x _ { n + 1 } ) - { \frac { f ( x _ { n + 1 } ) - f ( x _ { n } ) } { h } } \right) .
$$

Hence,the method is convergent for $\eta > - 1 / 2$ ,but unstable for $r _ { \beta } < - 1 / 2$ For $\eta = - 1$ the numerical solution does not exist.

# VII.4 Runge-Kutta Methods for Index 2 DAE

RK methods prove popular at IMA conference on numerical ODEs. (Byrne & Hindmarsh, SIAM News,March 1990)

This section is devoted to the convergence of implicit Runge-Kutta methods for semi-explicit index 2 systems (3.1) which satisfy (3.2). The $\varepsilon$ -embedding method of Sect. VI.1 defines the numerical solution by

$$
y _ { n + 1 } = y _ { n } + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } k _ { n \iota } , \qquad z _ { n + 1 } = z _ { n } + h \sum _ { \iota = 1 } ^ { s } b _ { \iota } \ell _ { n \iota }
$$

where

$$
k _ { n \ i } = f ( Y _ { n \ i } , Z _ { n \ i } ) , \qquad 0 = g ( Y _ { n \ i } )
$$

and the internal stages are given by

$$
Y _ { n \imath } = y _ { n } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } k _ { n \jmath } , \qquad Z _ { n \imath } = z _ { n } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \ell _ { n \jmath }
$$

(the state space form method (VI.1.12) does not make sense here, because the al-gebraic conditions do not depend on $z$ ).

The first convergence results for this situation are due to Petzold (1986). They are formulated for general problems $F ( y ^ { \prime } , y ) = 0$ under the assumption of "uniform index one". Since the system(3.1) becomes “uniform index one" if we replace $z$ by $u ^ { \prime }$ (Gear 1988,see also Exercise 1), the results of Petzold can be applied to (3.1). A further study for the semi-explicit system (3.1) is given by Brenan & Petzold (1989). Their main result is that for (4.1) the global error of the $y$ -component is $\mathcal { O } ( h ^ { q + 1 } )$ , and that of the $z$ -component is $\mathcal { O } ( h ^ { q } )$ (where $q$ denotes the stage order of the method). This result was improved by HLR89,using a different approach (local and global error are studied separately).

# The Nonlinear System

We first investigate existence, uniqueness and the influence of perturbations to the solution of the nonlinear system (4.1). In order to simplify the notation we write $( \eta , \zeta )$ for $\left( y _ { n } , z _ { n } \right)$ ，which we assume $h$ -dependent, and we suppress the index $_ n$ in $Y _ { n \imath }$ , etc. The nonlinear system then reads

$$
\left. \begin{array} { l } { { Y _ { \it \ / { \tau } } = \eta + h { \displaystyle \sum _ { \jmath = 1 } ^ { \it \ / { \ s } } } a _ { i \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) } } \\ { { 0 = g ( Y _ { \imath } ) } } \end{array} \right\} \qquad i = 1 , \ldots , s
$$

Once a solution to(4.2)is known, wecancompute $\ell _ { n \imath }$ from (4.1c) (whenever $\left( { a _ { \iota _ { \mathcal { I } } } } \right)$ is an invertible matrix) and then $y _ { n + 1 } , z _ { n + 1 }$ from (4.1a).

Theorem 4.1 (HLR89, p. 31). Suppose that $( \eta , \zeta )$ satisfy

$$
g ( \eta ) = \mathcal { O } ( h ^ { 2 } ) , \qquad g _ { y } ( \eta ) f ( \eta , \zeta ) = \mathcal { O } ( h )
$$

and that (3.2) holds in a neighbourhood of $( \eta , \zeta )$ . If the Runge-Kutta matrix $\left( { { a _ { \iota } } _ { \ j } } \right)$ is invertible, then the nonlinear system (4.2) possesses for $h \leq h _ { 0 }$ $a$ locally unique solution which satisfies

$$
Y _ { \imath } - \eta = \mathcal { O } ( h ) , \qquad Z _ { \imath } - \zeta = \mathcal { O } ( h ) .
$$

Remark. Condition (4.3) expresses the fact that $( \eta , \zeta )$ is close to consistent initial values. We also see from (4.2) that the solution $( Y _ { \imath } , Z _ { \imath } )$ does not depend on $\zeta$ The value of $\zeta$ in (4.3) only specifies the solution branch of $g _ { y } ( y ) f ( y , z ) = 0$ to which the numerical solution is close.

The proof of Theorem 4.1 for the implicit Euler method was given in Sect. VII.3 (proof of Theorem 3.1). If we replace (3.14) by

$$
\begin{array} { l } { { \displaystyle Y _ { \imath } - \eta ( h ) - h \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) = 0 } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } g _ { y } \Big ( \eta ( h ) + \tau \big ( Y _ { \imath } - \eta ( h ) \big ) \Big ) d \tau \cdot \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) + \frac { 1 } { h } g \big ( \eta ( h ) \big ) = 0 } } \end{array}
$$

it extends in a straightforward manner to general Runge-Kuta methods.

Influence of Perturbations. Besides (4.2) we also consider the perturbed system

$$
\left. \begin{array} { l } { { \displaystyle \widehat { Y } _ { i } = \widehat { \eta } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } f ( \widehat { Y } _ { j } , \widehat { Z } _ { j } ) + h \delta _ { \imath } } } \\ { { 0 = g ( \widehat { Y } _ { \imath } ) + \theta _ { i } } } \end{array} \right\} \qquad i = 1 , \ldots , s
$$

and we investigate the influence of the perturbations $\delta _ { \imath }$ and $\theta _ { i }$ on the numerical solution.

Theorem 4.2 (HLR89, p. 33). Let $Y _ { i } , Z _ { \imath }$ be a solution of (4.2) and consider perturbed values ${ \widehat { Y } } _ { \imath } , { \widehat { Z } } _ { \imath }$ satisfying (4.6). In addition to the assumptions of Theorem 4.1 suppose that

$$
\widehat { \eta } - \eta = \mathcal { O } ( h ^ { 2 } ) , \qquad \widehat { Z } _ { \scriptscriptstyle { \imath } } - \zeta = \mathcal { O } ( h ) , \qquad \delta _ { \scriptscriptstyle { \imath } } = \mathcal { O } ( h ) , \qquad \theta _ { \scriptscriptstyle { \imath } } = \mathcal { O } ( h ^ { 2 } ) .
$$

Then we have for $h \leq h _ { 0 }$ the estimates

$$
\begin{array} { l } { \displaystyle | | \widehat { Y } _ { \imath } - Y _ { \imath } | | \leq C \left( | | \widehat { \eta } - \eta | | + h | | \delta | | + | | \theta | | \right) } \\ { \displaystyle | | \widehat { Z } _ { \imath } - Z _ { \imath } | | \leq \frac { C } { h } \left( | | g _ { y } ( \eta ) ( \widehat { \eta } - \eta ) | | + h | | \widehat { \eta } - \eta | | + h | | \delta | | + | | \theta | | \right) } \end{array}
$$

where $\| \delta \| = \operatorname* { m a x } _ { \ i } \big \| \delta _ { \ i } \big \|$ and $\| \theta \| = \operatorname* { m a x } _ { \ i } \| \theta _ { \ i } \|$ . If the initial values satisfy $g ( \eta ) = 0$ and $g ( \widehat { \eta } ) = 0$ , then we have the stronger estimate

$$
\| \widehat { Z } _ { \iota } - Z _ { \iota } \| \leq \frac { C } { h } \left( h \| \widehat { \eta } - \eta \| + h \| \delta \| + \| \theta \| \right) .
$$

The constant $C$ in (4.8) and (4.9) depends only on bounds for certain derivatives of $f$ and $g$ , but not on the constants implied by the $\mathcal { O } ( \dots )$ terms in(4.3) and (4.7).

Proof. The estimates (4.8) are obtained by extending the proof of Theorem 3.2. When both initial values, $\eta$ and $\widehat { \eta }$ , lie on the manifold $g ( y ) = 0$ ，we have by Taylor expansion $0 = g ( \widehat { \eta } ) - g ( \eta ) = g _ { y } ( \eta ) ( \widehat { \eta } - \eta ) + { \mathcal O } ( \| \widehat { \eta } - \eta \| ^ { 2 } )$ . In this situation the term $g _ { y } ( \eta ) ( \widehat { \eta } - \eta )$ in (4.8b) is of size $\mathcal { O } ( h ^ { 2 } \vert \vert \widehat { \eta } - \eta \vert \vert )$ and may be neglected.□

# Estimation of the Local Error

We begin by defining two projections which will be important for the study of local errors for index 2 problems (3.1).

Definition 4.3.For given $y _ { 0 } , z _ { 0 }$ for which $( g _ { y } f _ { z } ) ( y _ { 0 } , z _ { 0 } )$ is invertible we define the projections

$$
\begin{array} { r } { Q = \big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \big ) ( y _ { 0 } , z _ { 0 } ) , \qquad P = I - Q . } \end{array}
$$

Geometric interpretation. Let $\mathcal { U }$ be the manifold defined by $\mathcal { U } = \{ y ; g ( y ) = 0 \}$ and let $T _ { y _ { 0 } } \mathcal { U } = \ker ( g _ { y } ( y _ { 0 } ) )$ be the tangent space at a point $y _ { 0 } \in \mathcal { U }$ . Further let $\mathcal { V } = \{ f ( y _ { 0 } , z ) \ ; \ z$ arbitrary $\}$ and let $T _ { f _ { 0 } } \mathcal { V } = \mathrm { I m } \left( f _ { z } ( y _ { 0 } , z _ { 0 } ) \right)$ be its tangent space at $f _ { 0 } = f ( y _ { 0 } , z _ { 0 } )$ . Here, $z _ { 0 }$ is the value for which $f ( y _ { 0 } , z _ { 0 } )$ lies in $T _ { y \mathrm { o } } \mathcal { U }$ (i.e., for which the condition $g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } ) = 0$ is satisfied (see 1.14c)). By considering the arrows $f ( y _ { 0 } , z )$ with varying $z$ (see Fig.4.1), the space $T _ { f _ { 0 } } \nu$ can be interpreted as the directions in which the control variables $z$ bring the solution to the manifold $\mathcal { U }$ . By (3.2) these two spaces are transversal and their direct sum generates the $y$ -space. It follows from (4.10) that $P$ projects onto $T _ { y _ { 0 } } \mathcal { U }$ parallel to $T _ { f _ { 0 } } \nu$ and $Q$ projects onto $T _ { f _ { 0 } } \nu$ parallel to $T _ { y _ { 0 } } \mathcal { U }$

Consider now initial values $y _ { 0 } = y ( x )$ ， $z _ { 0 } = z ( x )$ on the exact solution and denote by $y _ { 1 } , z _ { 1 }$ the numerical solution of the Runge-Kutta method (4.1). The local error

$$
\delta y _ { h } ( x ) = y _ { 1 } - y ( x + h ) , \qquad \delta z _ { h } ( x ) = z _ { 1 } - z ( x + h )
$$

![](images/6b025fd7372a6dd16bb5dfccd21469987d11cef90f6f677210b182ec096a843c.jpg)  
Fig. 4.1. Projections $P$ and $Q$

can be estimated as follows:

Lemma 4.4 (HLR89, p.34). Suppose that a Runge-Kutta method with invertible coefficient matrix $\left( { a _ { \iota } } _ { \jmath } \right)$ satisfies the assumptions $B ( p )$ and $C ( q )$ of Sect. IV.5 with $p \geq q$ . Then we have

$$
\begin{array} { r l } & { \delta y _ { h } ( x ) = \mathcal { O } ( h ^ { q + 1 } ) , \qquad P ( x ) \delta y _ { h } ( x ) = \mathcal { O } \bigl ( h ^ { \mathrm { m u n } ( p + 1 , q + 2 ) } \bigr ) } \\ & { \delta z _ { h } ( x ) = \mathcal { O } ( h ^ { q } ) , } \end{array}
$$

where $P ( x )$ is the projection (4.10) evaluated at $( y ( x ) , z ( x ) )$ . If, in addition, the Runge-Kutta method is stiffly accurate (i.e., satisfies $a _ { s 2 } = b _ { \imath }$ for all $i$ ), then

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { \operatorname* { m i n } ( p + 1 , q + 2 ) } ) .
$$

Proof. The exact solution values $\widehat { \eta } = y ( x ) , \widehat { Y } _ { \imath } = y ( x + c _ { \imath } h ) , \widehat { Z } _ { \imath } = z ( x + c _ { \imath } h )$ satisfy (4.6) with $\theta _ { \imath } = 0$ and

$$
\delta _ { \ i } = \frac { h ^ { q } } { q ! } y ^ { ( q + 1 ) } ( x ) \Big ( \frac { c _ { \ i } ^ { q + 1 } } { q + 1 } - \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { q } \Big ) + \mathcal { O } ( h ^ { q + 1 } ) .
$$

The difference to the numerical solution (4.2) with $\eta = y ( x ) ,$ ）can thus be estimated with Theorem 4.2, yielding

$$
Y _ { \imath } - y ( x + c _ { \imath } h ) = { \cal O } ( h ^ { q + 1 } ) , \qquad Z _ { \imath } - z ( x + c _ { \imath } h ) = { \cal O } ( h ^ { q } ) .
$$

Since the quadrature formula $\{ b _ { \imath } , c _ { \imath } \}$ is of order $p$ , we have

$$
y ( x + h ) - y ( x ) - h \sum _ { \iota = 1 } ^ { s } b _ { \iota } f \big ( y ( x + c _ { \iota } h ) , z ( x + c _ { \iota } h ) \big ) = \mathcal { O } ( h ^ { p + 1 } ) .
$$

Subtracting this formula from (4.1a) we get

$$
y _ { 1 } - y ( x + h ) = h f _ { z } ( y ( x ) , z ( x ) ) \sum _ { \iota = 1 } ^ { s } b _ { \iota } \big ( Z _ { \iota } - z ( x + c _ { \iota } h ) \big ) + { \cal O } ( h ^ { p + 1 } ) + { \cal O } ( h ^ { q + 2 } ) .
$$

Because of $P ( x ) f _ { z } ( y ( x ) , z ( x ) ) \equiv 0$ , this proves (4.12) for the $y$ -component. The

estimate for the $z$ -component follows from (see (1.28))

$$
z _ { 1 } - z ( x + h ) = \sum _ { \ i , \ j = 1 } ^ { s } b _ { \ i } \omega _ { \ i _ { 2 } } \big ( Z _ { \ j } - z ( x + c _ { \ j } h ) \big ) + \mathcal { O } \big ( h ^ { q + 1 } \big )
$$

and (4.14).

Under the assumption $a _ { s 2 } = b _ { \imath }$ (for all $i$ ) we have $g ( y _ { 1 } ) = 0$ so that by Taylor expansion

$$
0 = g ( y _ { 1 } ) - g { \big ( } y ( x + h ) { \big ) } = g _ { y } { \big ( } y ( x ) { \big ) } \delta y _ { h } ( x ) + { \mathcal O } ( h \| \delta y _ { h } ( x ) \| ) .
$$

This implies that $Q ( x ) \delta y _ { h } ( x ) = \mathcal { O } ( h \| \delta y _ { h } ( x ) \| )$ ， and (4.13) is a consequence of (4.12) and (4.10). □

For some important Runge-Kutta methods (such as Radau IA and Lobatto IIIC) the estimates of Lemma 4.4 are not optimal. Sharp estimates will be given in Theorem 4.9 for collocation methods and in Sect. VII.5 for general Runge-Kutta methods.

# Convergence for the $y$ -Component

The numerical solution $\{ y _ { n } \}$ ， defined by (4.1), does not depend on $\left\{ z _ { n } \right\}$ . Con-sequently, the convergence for the $y$ -component can be treated independently of estimates for the $z$ -component.

Theorem 4.5 (HLR89,p. 36). Suppose that (3.2) holds in a neighbourhood of the solution $( y ( x ) , z ( x ) )$ of(3.1) and that the initial values are consistent. Suppose further that the Runge-Kutta matrix $\left( { a _ { \iota } } _ { \jmath } \right)$ is invertible, that $| R ( \infty ) | < 1$ (see $( V I . I . I I e ) ,$ and that the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { r } ) , \qquad P ( x ) \delta y _ { h } ( x ) = \mathcal { O } ( h ^ { r + 1 } )
$$

with $P ( x )$ as in Lemma 4.4. Then the method (4.1) is convergent of order $r , i . e .$

$$
y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { r } ) \qquad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t .
$$

If in addition $\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { r + 1 } )$ ,then $g ( y _ { n } ) = \mathcal { O } ( h ^ { r + 1 } )$

Proof. A complete proof of this result is given in (HLR89,pp. 36-39). We re-strict our presentation to stiffly accurate Runge-Kutta methods (i.e., $a _ { \scriptscriptstyle { s _ { 1 } } } = b _ { \scriptscriptstyle { \imath } { \imath } }$ for all $i )$ . This considerably simplifies several parts of the proof, and nevertheless covers many important Runge-Kutta methods (such as Radau IA, Lobatto IIIC and the SDIRK method (IV.6.16)). The assumption $a _ { s _ { 1 } } = b _ { \ i }$ (for all $i$ ） implies that $g ( y _ { n } ) = 0$ for all $n$ and, as a consequence of (4.15) and (4.16), that

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { r + 1 } ) .
$$

The following proof is similar to that of Theorem 3.5 and uses, once again, Lady Windermere's Fan of Fig.II.3.2.

In addition to the numerical solution $\{ y _ { n } , z _ { n } \}$ ,also denoted by $\{ y _ { n } ^ { 0 } , z _ { n } ^ { 0 } \}$ ,we consider the Runge-Kutta solutions $\{ y _ { n } ^ { \ell } , z _ { n } ^ { \ell } \}$ with initial values $y _ { \ell } ^ { \ell } = y ( x _ { \ell } )$ ， $z _ { \ell } ^ { \ell } =$ the 1ocaleror on the exact solution. Wefrst estimate $\delta y _ { h } ( x _ { \ell } ) = y _ { \ell + 1 } ^ { \ell } - y _ { \ell + 1 } ^ { \ell + 1 }$ d $\mathcal { Y } _ { n } ^ { \ell } - \mathcal { Y } _ { n } ^ { \ell + 1 }$ for in terms of two neighbouring Runge-Kutta solutions by $\{ \widetilde { y } _ { n } \} , \ \{ \widehat { y } _ { n } \}$ and their difference by $\Delta y _ { n } = \widetilde { y } _ { n } - \widehat { y } _ { n }$ . We suppose for the moment that

$$
\| \widehat { y } _ { n } - y ( x _ { n } ) \| \leq C _ { 0 } h , \qquad \| \Delta y _ { n } \| \leq C _ { 1 } h ^ { 2 }
$$

(this will be justified below). Theorem 4.2 with $\delta _ { \tau } = 0$ and $\theta _ { \imath } = 0$ then yields

$$
\begin{array} { r } { \| \widetilde { Y } _ { n \iota } - \widehat { Y } _ { n \iota } \| \leq C \| \Delta y _ { n } \| , \qquad \| \widetilde { Z } _ { n \iota } - \widehat { Z } _ { n \iota } \| \leq C \| \Delta y _ { n } \| } \end{array}
$$

where $C$ is some constant independent of $C _ { 0 }$ and $C _ { 1 }$ . A Lipschitz condition for $f ( y , z )$ implies that

$$
\| \Delta y _ { n + 1 } \| \leq \| \Delta y _ { n } \| + h \sum _ { \iota = 1 } ^ { \textit { s } } | b _ { \iota } | \Big ( L _ { 1 } \| \widetilde { Y } _ { n \iota } - \widehat { Y } _ { n \iota } \| + L _ { 2 } \| \widetilde { Z } _ { n \iota } - \widehat { Z } _ { n \iota } \| \Big ) .
$$

Inserting (4.19) we get $\| \Delta y _ { n + 1 } \| \leq ( 1 + h L ) \| \Delta y _ { \eta } \|$ and hence also

$$
\begin{array} { r } { \| \Delta y _ { n } \| \leq C _ { 2 } \| \Delta y _ { 0 } \| \qquad \mathrm { ~ f o r ~ } \quad n h \leq C o n s t . } \end{array}
$$

For our situation in Lady Windermere's Fan the use of (4.17) yields

$$
\begin{array} { r } { \| y _ { n } ^ { \ell } - y _ { n } ^ { \ell + 1 } \| \leq C _ { 2 } \| \delta y _ { h } ( x _ { \ell } ) \| \leq C _ { 3 } h ^ { \tau + 1 } \qquad \mathrm { f o r ~ } n \geq \ell + 1 \mathrm { ~ a n d ~ } n h \leq C o n s t . } \end{array}
$$

Summing up we obtain the desired estimate

$$
\| y _ { n } - y ( x _ { n } ) \| \leq \sum _ { \ell = 0 } ^ { n - 1 } \| y _ { n } ^ { \ell } - y _ { n } ^ { \ell + 1 } \| \leq C _ { 4 } h ^ { \prime } \qquad { \mathrm { f o r ~ } } n h \leq C o n s t .
$$

Since $C _ { 3 }$ and $C _ { 4 }$ do not depend on $C _ { 0 }$ 0r $C _ { 1 }$ (if $h$ is sufficiently small), the assumption (4.18) is justified by induction on $\gamma _ { \ell }$ provided the constants $C _ { 0 } , C _ { 1 }$ are chosen sufficiently large. □

# Convergence for the $z$ -Component

Theorem 4.6 (HLR89, p.40). Consider the index 2 problem (3.1)-(3.2) with con-sistent initial values and assume that the Runge-Kutta matrix $\left( { a } _ { \iota _ { \mathcal { I } } } \right)$ is invertible and $| R ( \infty ) | < 1$ . If the global error of the $y$ -component is $\mathcal { O } ( h ^ { \prime } )$ ， $g ( y _ { n } ) = \mathcal { O } ( h ^ { \ast + 1 } )$ and the local error of the $z$ -component is $\mathcal { O } ( h ^ { r } )$ , then we have for the global error

$$
z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { r } ) \qquad f o r \quad x _ { n } - x _ { 0 } = n h \leq C o n s t .
$$

Remark. If,in addition to the invertibility of $\left( { { q } _ { \iota _ { \mathcal { I } } } } \right)$ and $| R ( \infty ) | < 1$ , the conditions $B ( q )$ and $C ( q )$ are satisfied then we have $\tilde { { \tilde { \alpha } _ { n } } } - \dot { z } ( \boldsymbol { x _ { n } } ) = \mathcal { O } ( \hbar ^ { q } )$ (see Lemma 4.4).

Proof. We write the global error as

$$
z _ { n + 1 } - z ( x _ { n + 1 } ) = z _ { n + 1 } - \widehat { z } _ { n + 1 } + \delta z _ { h } ( x _ { n } )
$$

where $( \widehat { y } _ { n + 1 } , \widehat { z } _ { n + 1 } )$ denotes the numerical solution obtained from the starting values $\left( y ( x _ { n } ) , z ( x _ { n } ) \right)$ and $\delta z _ { h } ( x _ { n } )$ is the local error. From(VI.1.11d) we have

$$
z _ { n + 1 } - \widehat { z } _ { n + 1 } = R ( \infty ) \left( z _ { n } - z ( x _ { n } ) \right) + \sum _ { \iota , \jmath = 1 } ^ { s } b _ { \iota } \omega _ { \iota \jmath } \big ( Z _ { n \jmath } - \widehat { Z } _ { n \jmath } \big ) .
$$

The assumption $g ( y _ { n } ) = \mathcal { O } ( h ^ { r + 1 } )$ implies that $g _ { y } ( y _ { n } ) ( y _ { n } - y ( x _ { n } ) ) = { \mathcal { O } } ( h ^ { r + 1 } )$ and,together with $y _ { n } - y ( x _ { n } ) = \mathcal { O } ( h ^ { r } )$ ,itfollowsfrom4.2that $Z _ { n _ { 2 } } -$ ${ \widehat { Z } } _ { n jmath } = { \mathcal { O } } ( h ^ { r } )$ .Iserig(4)

$$
z _ { n + 1 } - z ( x _ { n + 1 } ) = R ( \infty ) \left( z _ { n } - z ( x _ { n } ) \right) + \mathcal { O } ( h ^ { r } ) ,
$$

which proves the statement.

# Collocation Methods

An important subclass of implicit Runge-Kutta methods are the collocation methods as introduced in Sect.II.7. For the index 2 problem (3.1) they can be defined as follows.

Definition 4.7. Let $c _ { 1 } , \ldots , c _ { s }$ be $s$ distinct real numbers and denote by $u ( x ) , v ( x )$ the polynomials of degree $s$ (collocation polynomials) which satisfy

$$
u ( x _ { 0 } ) = y _ { 0 } , \qquad v ( x _ { 0 } ) = z _ { 0 }
$$

$$
\left. \begin{array} { c l c } { { u ^ { \prime } ( x _ { 0 } + c _ { \iota } h ) = f \big ( u ( x _ { 0 } + c _ { \iota } h ) , v ( x _ { 0 } + c _ { \iota } h ) \big ) } } \\ { { \qquad 0 = g \big ( u ( x _ { 0 } + c _ { \iota } h ) \big ) } } \end{array} \right\} \qquad i = 1 , \ldots , s .
$$

Then, the numerical solution is given by

$$
y _ { 1 } = u ( x _ { 0 } + h ) , \qquad z _ { 1 } = v ( x _ { 0 } + h ) .
$$

A straightforward extension of Theorems II.7.7 and I1.7.8 to index 2 problems shows that (4.23) is equivalent to the s -stage Runge-Kutta method (4.1) whose coefficients are defined by $B ( s )$ and $C ( s )$ (see Sect.IV.5 for their definition). This equivalence allows us to deduce from Theorem 4.1 the existence and local uniqueness of the collocation polynomials provided that the corresponding Runge-Kutta matrix is invertible.Hence we assume in the sequel that $c _ { \imath } \neq 0$ for all $i$ . The case of a singular Runge-Kutta matrix is considered in Exercises 2 and 3.

The quality of $u ( x ) , v ( x )$ as approximations to $y ( x ) , z ( x )$ is described by the next theorem, which extends Theorem II.7.10.

Theorem 4.8. Consider a collocation method (4.23) with all $c _ { \imath } \neq 0$ . Then we have for $k = 0 , 1 , \ldots , s$ and $x \in [ x _ { 0 } , x _ { 0 } + h ]$

$$
\begin{array} { r l } & { \| u ^ { ( k ) } ( x ) - y ^ { ( k ) } ( x ) \| \leq C h ^ { s + 1 - k } , } \\ & { \| v ^ { ( k ) } ( x ) - z ^ { ( k ) } ( x ) \| \leq C h ^ { s - k } . } \end{array}
$$

Proof. We exploit the fact that $u ( x _ { 0 } + c _ { \ i } h ) = Y _ { \ i }$ ， $v ( x _ { 0 } + c _ { \imath } h ) = Z _ { \imath }$ are the internal stages of the Runge-Kutta method (4.1). Consequently the collocation polynomials can be written as

$$
\begin{array} { l } { { \displaystyle u ( x _ { 0 } + t h ) = y _ { 0 } \ell _ { 0 } ( t ) + \sum _ { \imath = 1 } ^ { s } Y _ { \imath } \ell _ { \imath } ( t ) } } \\ { { \displaystyle v ( x _ { 0 } + t h ) = z _ { 0 } \ell _ { 0 } ( t ) + \sum _ { \imath = 1 } ^ { s } Z _ { \imath } \ell _ { \imath } ( t ) } } \end{array}
$$

where the $\ell _ { \ i } ( t )$ are the Lagrange polynomials defined by

$$
\ell _ { 0 } ( t ) = \prod _ { \jmath = 1 } ^ { s } { \frac { ( t - c _ { \jmath } ) } { ( - c _ { \jmath } ) } } , \qquad \ell _ { \imath } ( t ) = { \frac { t } { c _ { \imath } } } \prod _ { \jmath = 1 \atop \jmath \neq \imath } ^ { s } { \frac { ( t - c _ { \jmath } ) } { ( c _ { \imath } - c _ { \jmath } ) } } .
$$

Familiar estimates of the interpolation error imply that the exact solution $y ( x )$ satisfies

$$
y ( x _ { 0 } + t h ) = y _ { 0 } \ell _ { 0 } ( t ) + \sum _ { \iota = 1 } ^ { s } y ( x _ { 0 } + c _ { \iota } h ) \ell _ { \iota } ( t ) + \mathcal { O } ( h ^ { s + 1 } ) .
$$

The factor $h ^ { s + 1 }$ in the interpolation error comes from the $( s + 1 )$ -th derivative of $y ( x _ { 0 } + t h )$ with respect to $t$ . Obviously, the interpolation error is differentiable as often as the function $y ( x )$ . If we differentiate (4.25) $k$ times,then by Rolle's theorem, the difference

$$
h ^ { k } y ^ { ( k ) } ( x _ { 0 } + t h ) - \Big ( y _ { 0 } \ell _ { 0 } ^ { ( k ) } ( t ) + \sum _ { \ i = 1 } ^ { s } y ( x _ { 0 } + c _ { \ i } h ) \ell _ { \ i } ^ { ( k ) } ( t ) \Big )
$$

vanishes at least at $s + 1 - k$ points.Hence, the polynomial enclosed in brackets in $( 4 . 2 5 ^ { \circ } )$ can be interpreted as an interpolation polynomial of degree $s - k$ for the function $h ^ { k } y ^ { ( k ) } ( x _ { 0 } + t h )$ Its error is thus again of size $\mathcal { O } ( h ^ { s + 1 } )$ . Subtracting (4.25) from (4.24a) and differentiating $k$ times thus yields

$$
h ^ { k } \big ( u ^ { ( k ) } ( x _ { 0 } + t h ) - y ^ { ( k ) } ( x _ { 0 } + t h ) \big ) = \sum _ { \iota = 1 } ^ { s } \big ( Y _ { \iota } - y ( x _ { 0 } + c _ { \iota } h ) \big ) \ell _ { \iota } ^ { ( k ) } ( t ) + { \mathcal O } ( h ^ { s + 1 } )
$$

and a similar formula for the $z$ -component. The conclusion now follows from (4.14) with $q = s$ □

# Superconvergence of Collocation Methods

It is now natural to ask whether superconvergence takes place at $x _ { 0 } + h$ (as for ordinary differential equations; see Theorem II.7.9). The answer is affirmative, if the method is stiffly accurate,i.e., if $c _ { s } = 1$

Theorem 4.9. If $c _ { \scriptscriptstyle 2 } \neq 0$ for all $i$ and $c _ { s } = 1$ , then the $y$ -component of the local error of the collocation method (4.23) satisfies

$$
y _ { 1 } - y ( x _ { 0 } + h ) = \mathcal { O } \bigl ( h ^ { p + 1 } \bigr ) ,
$$

where $p$ is the order of the underlying quadrature formula.

Proof. We insert the collocation polynomials into the differential-algebraic problem and define the defect by

$$
\begin{array} { c } { { u ^ { \prime } ( x ) = f \bigl ( u ( x ) , v ( x ) \bigr ) + \delta ( x ) } } \\ { { 0 = g \bigl ( u ( x ) \bigr ) + \theta ( x ) . } } \end{array}
$$

By Definition 4.7 we have

$$
\delta ( x _ { 0 } + c _ { \ i } h ) = 0 , \qquad \theta ( x _ { 0 } ) = 0 , \qquad \theta ( x _ { 0 } + c _ { \ i } h ) = 0 .
$$

We next differentiate (4.26b) with respect to $x$ and use (4.26a):

$$
0 = g _ { y } ( u ( x ) ) { \big ( } f ( u ( x ) , v ( x ) ) + \delta ( x ) { \big ) } + \theta ^ { \prime } ( x ) .
$$

This motivates the use of the equation

$$
0 = g _ { y } ( u ) \big ( f ( u , v ) + \delta ( x ) \big ) + \theta ^ { \prime } ( x )
$$

for arbitrary $( u , v )$ in a neighbourhood of the solution of (3.1). Because of (3.2) we can extract $v$ from (4.29) so that (4.29) can be written as

$$
v = G \bigl ( u , \delta ( x ) , \theta ^ { \prime } ( x ) \bigr ) .
$$

Inserting into (4.26a) and into (3.1) this yields

$$
\begin{array} { l } { { u ^ { \prime } ( x ) = f \Big ( u ( x ) , G \big ( u ( x ) , \delta ( x ) , \theta ^ { \prime } ( x ) \big ) \Big ) + \delta ( x ) } } \\ { { y ^ { \prime } ( x ) = f \Big ( y ( x ) , G \big ( y ( x ) , 0 , 0 \big ) \Big ) . } } \end{array}
$$

In order to compute $u ( x ) - y ( x )$ we now apply the nonlinear variation-of-constants formula (Theorem I.14.5). This requires the computation of the defect of $u ( x )$ inserted into (4.31b)

$$
{ \begin{array} { r l } & { u ^ { \prime } ( x ) - f { \Big ( } u ( x ) , G { \big ( } u ( x ) , 0 , 0 { \big ) } { \Big ) } } \\ & { = f { \Big ( } u ( x ) , G { \big ( } u ( x ) , \delta ( x ) , \theta ^ { \prime } ( x ) { \big ) } { \Big ) } + \delta ( x ) - f { \Big ( } u ( x ) , G { \big ( } u ( x ) , 0 , 0 { \big ) } { \Big ) } } \\ & { = \Phi ( x , 1 ) - \Phi ( x , 0 ) + \delta ( x ) } \end{array} }
$$

where

$$
\Phi ( x , \tau ) = f { \Big ( } u ( x ) , G { \big ( } u ( x ) , \tau \cdot \delta ( x ) , \tau \cdot \theta ^ { \prime } ( x ) { \big ) } { \Big ) } .
$$

Then the formula $\begin{array} { r } { \Phi ( x , 1 ) - \Phi ( x , 0 ) = \int _ { 0 } ^ { 1 } \partial \Phi / \partial \tau \left( x , \tau \right) d \tau } \end{array}$ shows that the defect (4.32) can be written as

$$
Q _ { 1 } ( x ) \delta ( x ) + Q _ { 2 } ( x ) \theta ^ { \prime } ( x ) .
$$

We now insert this into Eq.(I.14.18) and obtain

$$
\begin{array} { l l l } { \displaystyle u ( x ) - y ( x ) = \int _ { x _ { 0 } } ^ { x } \mathrm { r e s o l v e n t } ( x , t ) \cdot \mathrm { d e f e c t } ( t ) d t } \\ { \displaystyle \qquad = \int _ { x _ { 0 } } ^ { x } \Bigl ( S _ { 1 } ( x , t ) \delta ( t ) + S _ { 2 } ( x , t ) \theta ^ { \prime } ( t ) \Bigr ) d t . } \end{array}
$$

Integrating the second term by parts we get (since $\theta ( x _ { 0 } ) = 0$ ）

$$
y _ { 1 } - y ( x _ { 0 } + h ) = \int _ { x _ { 0 } } ^ { x _ { 0 } + h } \Bigl ( S _ { 1 } ( x _ { 0 } + h , t ) \delta ( t ) - \frac { \partial S _ { 2 } } { \partial t } ( x _ { 0 } + h , t ) \theta ( t ) \Bigr ) d t
$$

The assumption $c _ { s } = 1$ implies that $\theta ( x _ { 0 } + h ) = 0 $ so that the last expression in (4.33) vanishes. The main idea is now to integrate the expression in (4.33） with the quadrature formula $\{ b _ { \imath } , c _ { \imath } \}$ (see also the proof of Theorem II.7.9). With the abbreviation

$$
\sigma ( t ) = S _ { 1 } ( x _ { 0 } + h , t ) \delta ( t ) - \frac { \partial S _ { 2 } } { \partial t } ( x _ { 0 } + h , t ) \theta ( t )
$$

this gives

$$
y _ { 1 } - y ( x _ { 0 } + h ) = \int _ { x _ { 0 } } ^ { x _ { 0 } + h } \sigma ( t ) d t = h \sum _ { \iota = 1 } ^ { \ s } b _ { \iota } \sigma ( x _ { 0 } + c _ { \iota } h ) + e r r ( \sigma ) .
$$

Because of (4.27) we have $\sigma ( x _ { 0 } + c _ { \iota } h ) = 0$ for all $i$ and the quadrature error is estimated by

$$
\| e r r ( { \boldsymbol { \sigma } } ) \| \leq C \hbar ^ { p + 1 } \operatorname* { m a x } _ { t \in [ x _ { 0 } , x _ { 0 } + h ] } \| { \boldsymbol { \sigma } } ^ { ( p ) } ( t ) \| .
$$

The $p$ -th derivative of $\sigma ( t )$ contains derivatives of $f , g$ and of $\delta ( x ) , \theta ( x )$ By Theorem 4.8 they are uniformly bounded for $h \leq h _ { 0 }$ . Hence $y _ { 1 } - y ( x _ { 0 } + h ) =$ $e r r ( \sigma ) = \mathcal { O } ( h ^ { p + 1 } )$ , proving the theorem. □

# Projected Runge-Kutta Methods

For collocation methods which are not stifly accurate it is possible to prove superconvergence (as in Theorem 4.9) if the method is combined with a certain projec-tion. We start with a more careful study of the local error of the $y$ -component in (4.33).

Lemma 4.10. If $c _ { \imath } \neq 0$ for all $i$ ， then the $y$ -component of the local error of the collocation method (4.23) satisfies

$$
y _ { 1 } - y ( x _ { 0 } + h ) = - \Big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \Big ) \big ( y ( x _ { 0 } + h ) , z ( x _ { 0 } + h ) \big ) \theta ( x _ { 0 } + h ) + \mathcal { O } ( h ^ { p + 1 } )
$$

where $\theta$ is the defect given by (4.26b) and $p$ is the order of the underlying quadrature formula.

Proof. The above proof of Theorem 4.9 (see Eq.(4.33)) shows that the local error satisfies

$$
y _ { 1 } - y ( x _ { 0 } + h ) = S _ { 2 } ( x _ { 0 } + h , x _ { 0 } + h ) \theta ( x _ { 0 } + h ) + \mathcal { O } ( h ^ { p + 1 } ) . \qquad 
$$

Hence, we only have to compute $S _ { 2 } ( x , x )$ . Since any resolvent equals the identity matrix if both of its arguments are equal, it follows from the definition of $S _ { 2 } ( x , t )$ and from (4.32') that

$$
S _ { 2 } ( x , x ) = \int _ { 0 } ^ { 1 } f _ { z } \Big ( u ( x ) , G \big ( u ( x ) , \tau \delta ( x ) , \tau \theta ^ { \prime } ( x ) \big ) \Big ) \frac { \partial G } { \partial \theta ^ { \prime } } \Big ( u ( x ) , \tau \delta ( x ) , \tau \theta ^ { \prime } ( x ) \Big ) d \tau .
$$

Differentiating (4.29) with respect to $\theta ^ { \prime }$ gives

$$
\frac { \partial G } { \partial \theta ^ { \prime } } = \frac { \partial v } { \partial \theta ^ { \prime } } = - ( g _ { y } f _ { z } ) ^ { - 1 } ( u , v ) .
$$

Furthermore,it follows from (4.27） that $\delta ( x ) = \mathcal { O } ( h ^ { s } )$ and $\theta ^ { \prime } ( x ) = \mathcal { O } ( h ^ { s } )$ for $x = x _ { 0 } + h$ . Using $u ( x ) - y ( x ) = \mathcal { O } ( h ^ { s + 1 } )$ (from Theorem 4.8) we thus obtain for $x = x _ { 0 } + h$

$$
S _ { 2 } ( x , x ) = \left( f _ { z } \big ( g _ { y } f _ { z } \big ) ^ { - 1 } \right) \big ( y ( x ) , z ( x ) \big ) + \mathcal { O } ( h ^ { s } ) .
$$

The statement now follows from $p \leq 2 s$ and from $\theta ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { s + 1 } )$

The geometric interpretation of Lemma 4.10 is as follows: if we split the local error $\delta y _ { h } ( x _ { 0 } )$ according to the projections of Fig.4.1 then the component $Q ( x _ { 0 } + h ) \delta y _ { h } ( x _ { 0 } )$ is of size $\mathcal { O } ( h ^ { s + 1 } )$ , whereas the component $P ( x _ { 0 } + h ) \delta y _ { h } ( x _ { 0 } )$ is $\mathcal { O } \{ h ^ { p + 1 } )$ . This suggests to project after every step the numerical solution of a Runge-Kutta method onto the manifold $g ( y ) = 0$ with the help of the projection operator $P ( x _ { 0 } + h )$ as follows:

Definition 4.11 (Ascher & Petzold 1991).Let $y _ { 1 } , z _ { 1 }$ be the numerical solution of an implicit Runge-Kutta method (4.1) and define ${ \widehat { y } } _ { 1 } , \lambda$ as the solution of the system

$$
\begin{array} { l } { { \widehat { y } _ { 1 } = y _ { 1 } + f _ { z } ( \widehat { y } _ { 1 } , z _ { 1 } ) \lambda } } \\ { { 0 = g ( \widehat { y } _ { 1 } ) . } } \end{array}
$$

If the value $\widehat { y } _ { 1 }$ (and $z _ { 1 } )$ is used for the step by step integration of (3.1), then we call this procedure projected Runge-Kutta method.

Remarks. 1) If $g ( y _ { 1 } )$ is sufficiently small, then the nonlinear system (4.38） pos-sesses a locally unique solution. A Newton-type iteration with starting values $\widehat { y } _ { 1 } ^ { ( 0 ) } = y _ { 1 }$ ， $\lambda ^ { ( 0 ) } = 0$ will converge to this solution. This follows at once from the theorem of Newton-Kantorovich(Ortega & Rheinboldt 1970) because the Jacobian of (4.38) evaluated at the starting values

$$
\left( { \begin{array} { c c } { I } & { - f _ { z } ( y _ { 1 } , z _ { 1 } ) } \\ { g _ { y } ( y _ { 1 } ) } & { 0 } \end{array} } \right)
$$

has a bounded inverse by (3.2).

2)For stiffly accurate Runge-Kutta methods (i.e.， if $a _ { s _ { 2 } } = b _ { \ i }$ for all $i$ ）the projected and unprojected Runge-Kutta methods coincide.

3) The proof of the next theorem shows that the argument in $f _ { z } ( \widehat { y } _ { 1 } , z _ { 1 } )$ may be replaced by some other approximation to $y ( x _ { 0 } + h )$ ， $z ( x _ { 0 } + h )$ whose error is at most $\mathcal { O } ( h ^ { s } )$ ·

The following theorem proves superconvergence for projected collocation methods (also if the corresponding Runge-Kutta method is not stiffly accurate). Su-perconvergence results for general Runge-Kutta methods are given in Sect. VI.8.

Theorem 4.12 (Ascher & Petzold 1991). If $c _ { \imath } \neq 0$ for all $i$ , then the $y$ -component of the local error of the projected collocation method (4.23), (4.38) satisfies

$$
{ \widehat { y } } _ { 1 } - y ( x _ { 0 } + h ) = { \mathcal { O } } ( h ^ { p + 1 } )
$$

where $p$ is the order of the underlying quadrature formula.

Proof. We write $\widehat { e } _ { 1 } = \widehat { y } _ { 1 } - y ( x _ { 0 } + h )$ ， $e _ { 1 } = y _ { 1 } - y \big ( x _ { 0 } + h \big )$ for the local errors and denote the projections of Definition 4.3 by

$$
\begin{array} { r l r } { Q = \big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \big ) ( \widehat { y } _ { 1 } , z _ { 1 } ) , } & { { } } & { P = I - Q . } \end{array}
$$

The idea is to split $\widehat { e } _ { 1 }$ according to

$$
\widehat { e } _ { 1 } = P \widehat { e } _ { 1 } + Q \widehat { e } _ { 1 }
$$

and to estimate both components separately. The first formula of (4.38) together with (4.37) and $\theta ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { s + 1 } )$ imply that

$$
\begin{array} { r } { P \widehat { e } _ { 1 } = P e _ { 1 } = \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { s + 1 } \vert \vert \widehat { e } _ { 1 } \vert \vert ) . } \end{array}
$$

Further we have $0 = g ( \widehat { y } _ { 1 } ) - g \big ( y ( x _ { 0 } + h ) \big ) = g _ { y } \big ( \widehat { y } _ { 1 } \big ) \widehat { e } _ { 1 } + { \cal O } \big ( \| \widehat { e } _ { 1 } \| ^ { 2 } \big ) ,$ ,implying

$$
Q { \widehat { e } } _ { 1 } = { \mathcal { O } } ( \| { \widehat { e } } _ { 1 } \| ^ { 2 } ) .
$$

Formulas (4.40) and (4.41) inserted into (4.39) give

$$
\widehat { e } _ { 1 } = \mathcal { O } ( h ^ { p + 1 } ) + \mathcal { O } ( h ^ { s + 1 } \| \widehat { e } _ { 1 } \| ) + \mathcal { O } ( \| \widehat { e } _ { 1 } \| ^ { 2 } )
$$

and the statement ofthe theorem is an immediate consequence.

Global convergence of order $\mathcal { O } ( h ^ { p } )$ of the projected collocation methods is obtained exactly as in the proof of Theorem 4.5. We observe that the numerical solution always remains on the manifold $g ( y ) = 0$ so that the estimate (4.9) applies.

# Summary of Convergence Results

Table 4.1 collects the optimal error estimates for some important Runge-Kutta methods when applied to the index 2 problem (3.1)-(3.2). The local error estimates can be verified as follows: Gauss,Radau IA and SDIRK by Lemma 4.4, Radau IIA by Theorem 4.9, Lobatto IC by Theorem 5.10 below and Lobatto IIIA with the help of Exercise 4. For the projected methods the estimates follow from Theorem 4.12 and the considerations of Sect. VI.5. Because there are several ways of defining the $z$ -component of the numerical solution, we do not present their convergence behaviour. The global convergence result follows from Theorems 4.5 and 4.6 for the Radau IA, Radau IIA, Lobatto IIIC and SDIRK methods. The remaining methods (Gauss and Lobatto IIIA) require some more effort because their stability function only satisfies $| R ( \infty ) | = 1$ . For a detailed discussion of these methods we refer to HLR89 and Jay (1993).

Table 4.1. Error estimates for the index 2 problem (3.1)-(3.2)   

<table><tr><td>Method</td><td colspan="2">stages</td><td colspan="2">local error y Z</td></tr><tr><td>Gauss</td><td>了 S odd</td><td>h0+1 h</td><td>y {ho+1</td><td>Z h8-1 一</td></tr><tr><td>projected Gauss</td><td>s even</td><td>h28+1</td><td>h h28</td><td>h9-2</td></tr><tr><td>Radau IA</td><td>S</td><td>h h9-1</td><td>h</td><td>h-1</td></tr><tr><td>projected Radau IA</td><td>S</td><td>h2g-1</td><td>h28-2</td><td></td></tr><tr><td>Radau IIA</td><td>s</td><td>h2g</td><td>h2g-1</td><td>h</td></tr><tr><td></td><td>S odd</td><td>h</td><td></td><td>{h0-1</td></tr><tr><td>Lobatto IIIA</td><td>{s S even</td><td>h29-1 h</td><td>h29-2</td><td>h</td></tr><tr><td>Lobatto IIIC</td><td>S</td><td>h28-1 h-1</td><td>h28-2</td><td>h9-1</td></tr><tr><td>SDIRK (IV.6.16)</td><td>5</td><td>h h</td><td>h²</td><td>h1</td></tr><tr><td>SDIRK (IV.6.18)</td><td>3</td><td>h2</td><td>h1 h²</td><td>h1</td></tr></table>

# Exercises

1. Consider the index 2 problem $y ^ { \prime } = f ( y , z )$ ， $0 = g ( y )$ . Put $z = u ^ { \prime }$ ， $v = ( y , u ) ^ { T }$ so that the problem becomes

$$
F ( v ^ { \prime } , v ) = \left( { { y } ^ { \prime } } - f ( y , u ^ { \prime } ) \right) = 0 .
$$

Prove that the matrix pencil $F _ { v } + \lambda F _ { v ^ { \prime } }$ is of index 1 whenever $( g _ { y } f _ { z } ) ^ { - 1 }$ exists. Hint. Consider the transformation

$$
\left( \begin{array} { c c } { { I } } & { { a } } \\ { { 0 } } & { { I } } \end{array} \right) \left( F _ { v } + \lambda F _ { v ^ { \prime } } \right) \left( \begin{array} { c c } { { I } } & { { b } } \\ { { 0 } } & { { I } } \end{array} \right)
$$

where $a = f _ { y } f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 }$ and $b = f _ { z }$ are chosen such that the upper right block in (4.42) vanishes.

2. Consider Runge-Kutta methods whose coefficients satisfy:

${ a _ { 1 } } _ { \imath } = 0$ for all $i$ and $\left( a _ { \iota _ { 2 } } \right) _ { \iota , \jmath \geq 2 }$ is invertible.

(Examples are collocation methods with $c _ { 1 } = 0$ , such as Lobatto IIIA).

If $g ( \eta ) = 0$ then the nonlinear system (4.2) has a locally unique solution which satisfies $Y _ { 1 } = \eta$ ， $Z _ { 1 } = \zeta$

3. Let $c _ { 1 } = 0$ ， $c _ { 2 } , \ldots , c _ { s }$ be $s$ distinct real numbers. Show that there exist unique polynomials $u ( x )$ and $v ( x )$ $\deg u = s$ ， $\deg v = s - 1 \colon$ ）such that (4.23a,b) holds.

Hint. Apply the ideas of the proof of Theorem II.7.7 and Exercise 2.

4. Investigate the validity of the conclusions of Theorems 4.8 and 4.9 for the situation where $c _ { 1 } = 0$

5.(Computation of the algebraic variable $z$ by piecewise discontinuous interpolation, see Ascher (1989). Modify the definition of $z _ { n + 1 }$ in the Runge-Kutta method (4.1) as follows: let $v ( x )$ be the polynomial of degree $s - 1$ satisfying $v ( x _ { n } + c _ { \imath } h ) = Z _ { n \imath }$ for all $i$ , then define $z _ { n + 1 } = v ( x _ { n } + h )$ . In the case of collocation methods (4.23) this definition removes the condition $v ( x _ { 0 } ) = z _ { 0 }$ while lowering the degree of $v ( x )$ by 1.

a) Verify: $z _ { n + 1 }$ does not depend on $z _ { n }$ ,also if the stability function of the method does not vanish at infinity.

b) Prove that for projected collocation methods with $c _ { \imath } \neq 0$ for all $i$ we have $z _ { n } - z ( x _ { n } ) = \mathcal { O } ( h ^ { s } )$

c) For the projected Gauss methods compare this result with that of the standard approach.

6. The statement of Theorem 4.8 still holds,if one omits the condition $v ( x _ { 0 } ) = z _ { 0 }$ in Definition 4.7 and if one lets $v ( x )$ be a polynomial of degree $s - 1$ ·

# VII.5 Order Conditions for Index 2 DAE

For an application of the convergence result of the preceding section (Theorem 4.5) it is desirable to know the optimal values of $\mathscr { r }$ in (4.16). Comparing the Taylor expansions of the exact and numerical solutions we derive conditions for $c _ { i } , a _ { \iota _ { j } } , b _ { \jmath }$ which are equivalent to (4.16). For collocation methods we recover the result of Theorem 4.9. For other methods (such as Lobatto IIIC) the estimates of Lemma 4.4 are substantially improved.

The theory of this section is given in HLR89 (Sect.5). Our presentation is slightly different and is in complete analogy to the derivation of the index 1 order conditions of Sect. VI.4. The results of this section are here applied to Runge-Kutta methods only; analogous formulas for Rosenbrock methods can be found in Roche (1988). An independent investigation, conducted for the index 2 problem $f ( y , z ^ { \prime } ) = 0$ ， $z = g ( y )$ by A. Kvarng (1990),leads to the same order conditions for Runge-Kutta methods.

# Derivatives of the Exact Solution

We consider the index 2 problem

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { 0 = g ( y ) } } \end{array}
$$

and assume consistent initial values $y _ { 0 } , z _ { 0 }$ . The first derivative of the solution $y ( x )$ is given by (5.1a). Differentiating this equation we get

$$
y ^ { \prime \prime } = f _ { y } ( y , z ) y ^ { \prime } + f _ { z } ( y , z ) z ^ { \prime } .
$$

In order to compute $z ^ { \prime }$ we differentiate (5.1b) twice

$$
\begin{array} { l } { { 0 = g _ { y } ( y ) y ^ { \prime } } } \\ { { 0 = g _ { y y } ( y ) ( y ^ { \prime } , y ^ { \prime } ) + g _ { y } ( y ) y ^ { \prime \prime } } } \end{array}
$$

and insert (5.2) and (5.1a). This yields (omiting the obvious function arguments)

$$
0 = g _ { y y } ( f , f ) + g _ { y } f _ { y } f + g _ { y } f _ { z } z ^ { \prime }
$$

or equivalently

$$
z ^ { \prime } = ( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y y } ( f , f ) + ( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y } f _ { y } f .
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations II, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_35, $©$ Springer-Verlag Berlin Heidelberg 2010

Here we have used the index 2 assumption (3.2), that $g _ { y } f _ { z }$ is invertible in a neighbourhood of the solution. We now differentiate (5.1a) and (5.5) with respect to $x$ ， and replace the appearing $y ^ { \prime }$ and $z ^ { \prime }$ by (5.1a) and (5.5). We use (for a constant vector $u$ ）

$$
\begin{array} { r l } {  { \frac { d } { d x } ( - g _ { y } f _ { z } ) ^ { - 1 } u } } \\ & { = ( - g _ { y } f _ { z } ) ^ { - 1 } \Big ( g _ { y y } \big ( f _ { z } ( - g _ { y } f _ { z } ) ^ { - 1 } u , f \big ) + g _ { y } f _ { z y } \big ( ( - g _ { y } f _ { z } ) ^ { - 1 } u , f \big ) } \\ & { \quad + g _ { y } f _ { z z } \Big ( ( - g _ { y } f _ { z } ) ^ { - 1 } u , ( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y y } ( f , f ) + ( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y } f _ { y } f \Big ) \Big ) } \end{array}
$$

(cf.Formula (VI.4.7)) and thus obtain

$$
\begin{array} { r l } { g ^ { \prime \prime } = \int _ { S } f _ { + } ^ { \prime } + f _ { + } - g _ { g _ { g } } f _ { - } ^ { \prime \prime } ) ^ { - 1 } g _ { g _ { g } } \gamma _ { g _ { g } } \gamma _ { f } f _ { f } ^ { \prime } + f _ { + } ^ { \prime \prime } + f _ { g _ { g } } f _ { f } ^ { \prime } \gamma ^ { - 1 } g _ { g _ { g } } \gamma ^ { - 1 } g _ { g _ { g } } f _ { f } ^ { \prime } } \\ { g ^ { \prime \prime } = \big ( - g _ { g } f _ { + } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { + } f _ { f } \big ) + 3 \big ( - g _ { g } f _ { + } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } f _ { g } ^ { \prime } \big ) } \\ & { + 3 \big ( - g _ { g } f _ { + } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { + } \big ( - g _ { g } f _ { - } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } ^ { \prime } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } ^ { \prime } \big ) \big ) } \\ & { + 3 \big ( - g _ { g } g _ { f } \big ) ^ { - 1 } ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } ^ { \prime } f _ { g _ { g } } \big ) - ^ { 1 } g _ { g _ { g } } \big ( f _ { - } ^ { \prime } f _ { g } \big ) + \big ( - g _ { g } f _ { f } ^ { \prime } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } f _ { g } ^ { \prime } \big ) } \\ & { + 3 \big ( - g _ { g } f _ { - } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { - } ^ { \prime } \big ( f _ { g } - g _ { g _ { g } } f _ { - } ^ { \prime } \big ) ^ { - 1 } g _ { g _ { g } } f _ { f } ^ { \prime } \big ) + \big ( - g _ { g } f _ { - } \big ) ^ { - 1 } g _ { g _ { g } } \big ( f _ { + } f \big ) } \\ &  + 2 \big ( - g _ { g } f _ { - } \big ) ^ { - 1 } g _ { g } \big ( f _ { - } ^  \end{array}
$$

Obviously,a graphical representation of these expressions will be of great help.

# Trees and Elementary Differentials

As in Sect. VI.4 we identify each occuring $f$ with a meagre vertex,each of its derivatives with an upwards leaving branch, the expression $( - g _ { y } f _ { z } ) _ { . } ^ { - 1 } g$ with a fat vertex and the derivatives of $g$ therein again with upwards leaving branches. The corresponding graphs for $y ^ { \prime } , z ^ { \prime } , y ^ { \prime \prime } , z ^ { \prime \prime }$ (see Formulas (5.1a), (5.5), (5.7), (5.8)) are given in Fig. 5.1.

The derivatives of $y$ are characterized by trees with a meagre root (the lowest vertex). These trees will be denoted by $t$ or $t _ { \imath }$ , the tree consisting of the root only (for $y ^ { \prime }$ ) being $\tau$ . Derivatives of $z$ have trees with a fat root. They will be denoted by $u$ or $u _ { \iota }$

Definition 5.1. Let $D A T 2 = D A T 2 _ { y } \cup D A T 2 _ { z }$ denote the set of (differential algebraic index 2) trees defined recursively by

![](images/346d66a008600ce0750ded0f00dfd0d1e07af370f88a90173282f2f655e1cee8.jpg)  
Fig. 5.1. Graphical representation of the first derivatives

a) $\tau \in D A T 2 _ { y }$ ，  
b) $[ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots u _ { n } ] _ { y } \in D A T 2 _ { y }$ if $t _ { 1 } , \ldots , t _ { m } \in D A T 2 _ { y }$ and $u _ { 1 } , . . . u _ { n } \in D A T 2 _ { z } \colon$   
c） $[ t _ { 1 } , \dots , t _ { m } ] _ { z } \in D A T 2 _ { z }$ if $t _ { 1 } , \dots , t _ { m } \in D A T 2 _ { y }$ and either $m > 1$ or$m = 1$ and $t _ { 1 } \neq [ u ] _ { y }$ with $u \in D A T 2 _ { z }$

Definition 5.2. The order of a tree $t \in D A T 2 _ { y }$ or $u \in D A T 2 _ { z }$ , denoted by $\varrho ( t )$ or $\varrho \big ( u \big )$ , is the number of meagre vertices minus the number of fat vertices.

Definition 5.3. The elementary differentials $F ( t )$ （or $F ( u )$ ) corresponding to trees in DAT2 are defined as follows:

$$
{ \begin{array} { r l } & { F ( t ) = { \cfrac { \partial ^ { m + n } f } { \partial y ^ { m } \partial z ^ { n } } } \left( F ( t _ { 1 } ) , \dots , F ( t _ { m } ) , F ( u _ { 1 } ) , \dots , F ( u _ { n } ) \right) } \\ & { { \mathrm { ~ i f ~ } } t = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { y } \in D A T 2 _ { y } , } \\ & { F ( u ) = ( - g _ { y } f _ { z } ) ^ { - 1 } { \cfrac { \partial ^ { m } g } { \partial y ^ { m } } } \left( F ( t _ { 1 } ) , \dots , F ( t _ { m } ) \right) } \\ & { { \mathrm { ~ i f ~ } } u = [ t _ { 1 } , \dots , t _ { m } ] _ { z } \in D A T 2 _ { z } . } \end{array} }
$$

# Taylor Expansion of the Exact Solution

In order to continue the process which led to (5.7) and (5.8) we need the differentiation of elementary differentials $F ( t )$ and $F ( u )$ . This is described by the following rules:

i) attach to each vertex a branch with $\tau$ (derivative of $f$ or $g$ with respect to $y$ and addition of the factor $y ^ { \prime } = f )$ ；

ii） attach to each meagre vertex a branch with $[ \tau , \tau ] _ { z }$ ; attach to each meagre vertex a branch with ${ \bigl [ } \{ \tau \} _ { y }  \bigr \} _ { z }$ (this yields two trees and corresponds to the derivative of $f$ with respect to $z$ and to the addition of the factors $( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y y } ( f , f )$ and $( - g _ { y } f _ { z } ) ^ { - 1 } g _ { y } f _ { y } f$ of (5.5));

iii） split each fat vertex into two new fat vertices (one above the other) and link them via a new meagre vertex. Then four new trees are obtained as follows: attach a branch with $\tau$ to the lower of these fat vertices; attach a branch with $\tau , [ \tau , \tau ] _ { z }$ or $[ [ \tau ] _ { y } \big ] _ { z }$ to the new meagre vertex (this corresponds to the derivation of $( - g _ { y } f _ { z } ) ^ { - 1 }$ and follows at once from Eq.(5.6)).

Some of the elementary differentials in (5.8) appear more than once. In order to understand how often such an expression (or the corresponding tree) appears in the derivatives of $y$ or $z$ ， we indicate the order of generation of the vertices as follows (see Fig.5.2): for the trees of order 1, namely $\boldsymbol { \tau } , [ \boldsymbol { \tau } , \boldsymbol { \tau } ] _ { z }$ and $[ [ \tau ] _ { y } \big ] _ { z }$ ，we add the label 1 to a meagre vertex such that

each fat vertex is followed by at least one unlabelled meagre vertex.

Each time a tree is “differentiated” according to the above rules we provide the newly attached tree (of order 1) with a new label such that (5.9) still holds. The labelling so obtained is obviously increasing along each branch.

![](images/375f6d4584a4f080378c04a63f99e30dc88df46a561a44434f13982aab39aeab.jpg)  
Fig.5.2. Examples of monotonically labelled trees

Definition 5.4. A tree $t \in D A T 2 _ { y }$ (or $u \in D A T 2 _ { z } ,$ ），together with a monotonic labelling of $\varrho ( t )$ （or $\varrho ( u ) )$ among its meagre vertices such that (5.9) holds,is called a monotonically labelled tree. The sets of such monotonically labelled trees are denoted by $L D A T 2 _ { y }$ ， $L D A T 2 _ { z }$ , and LDAT2.

Since the differentiation process of trees described above generates all elements of LDAT2,and each of them exactly once,and since each differentiation increases the order of the trees by one, we have the following result.

Theorem 5.5 (HLR89, p.58). For the exact solution of(5.1) we have:

$$
y ^ { ( q ) } ( x _ { 0 } ) = \sum _ { \substack { t \in L D A T 2 _ { y } , \varrho ( t ) = q } } F ( t ) ( y _ { 0 } , z _ { 0 } ) = \sum _ { \substack { t \in D A T 2 _ { y } , \varrho ( t ) = q } } \alpha ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } )
$$

$$
z ^ { ( q ) } ( x _ { 0 } ) = \sum _ { \substack { u \in L D A T 2 _ { z } , \varrho ( u ) = q } } F ( u ) ( y _ { 0 } , z _ { 0 } ) = \sum _ { \substack { u \in D A T 2 _ { z } , \varrho ( u ) = q } } \alpha ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) .
$$

The integer coefficients $\alpha ( t )$ and $\alpha ( u )$ indicate the number of possible monotonic labellings of $a$ tree. □

# Derivatives of the Numerical Solution

For the problem (5.1） with consistent inital values $( y _ { 0 } , z _ { 0 } )$ we write one step of a Runge-Kutta method in the form

$$
y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { s } b _ { \imath } k _ { \imath } , \qquad z _ { 1 } = z _ { 0 } + \sum _ { \imath = 1 } ^ { s } b _ { \imath } \ell _ { \imath }
$$

where

$$
k _ { \ i } = h f ( Y _ { \ i } , Z _ { \ i } ) , \qquad 0 = g ( Y _ { \ i } )
$$

and

$$
Y _ { \imath } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } k _ { \jmath } , \qquad Z _ { \imath } = z _ { 0 } + \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } \ell _ { \jmath } .
$$

We have replaced $h k _ { n \imath } , h \ell _ { n \imath }$ of Formula (4.1) by $k _ { \imath } , \ell _ { \imath }$ . This is not essential, but adjusts the derivation of the order conditions to the presentation of Sect. VI.4. Since the following derivation is very similar to the one given in Sect.VI.4,we restrict ourselves to the main ideas.

We consider $y _ { 1 } , z _ { 1 } , k _ { \iota } , \ell _ { i } , Y _ { \iota } , Z _ { \iota }$ as functions of $h$ and compute their derivatives at $h \approx 0$ . From (5.10a) we get

$$
y _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { i = 1 } ^ { s } b _ { \imath } k _ { \imath } ^ { ( q ) } ( 0 ) ,
$$

and (5.10b) yields

$$
k _ { \iota } ^ { ( q ) } ( 0 ) = q { \Big ( } f ( Y _ { \iota } , Z _ { \iota } ) { \Big ) } ^ { ( q - 1 ) } { \Big | } _ { h = 0 } , \qquad 0 = { \Big ( } g ( Y _ { \iota } ) { \Big ) } ^ { ( q ) } { \Big | } _ { h = 0 } .
$$

The total derivatives of $f ( Y _ { i } , Z _ { \imath } )$ and $g ( Y _ { \imath } )$ can be computed by Faa di Bruno's formula (see (VI.4.14) and (VI.4.15)). This gives

$$
\left( f ( Y _ { \imath } , Z _ { \imath } ) \right) ^ { ( q - 1 ) } = \sum \frac { \partial ^ { m + n } f ( Y _ { \imath } , Z _ { \imath } ) } { \partial y ^ { m } \partial z ^ { n } } \left( Y _ { \imath } ^ { ( \mu _ { 1 } ) } , \ldots , Y _ { \imath } ^ { ( \mu _ { m } ) } , Z _ { \imath } ^ { ( \nu _ { 1 } ) } , \ldots , Z _ { \imath } ^ { ( \nu _ { n } ) } \right)
$$

with $\mu _ { 1 } + . . . + \mu _ { m } + \nu _ { 1 } + . . . + \nu _ { n } = q - 1$ ,and

$$
\left( g ( Y _ { i } ) \right) ^ { ( q ) } = \sum { \frac { \partial ^ { m } g ( Y _ { \imath } ) } { \partial y ^ { m } } } \left( Y _ { i } ^ { ( \mu _ { 1 } ) } , \ldots , Y _ { \imath } ^ { ( \mu _ { m } ) } \right)
$$

with $\mu _ { 1 } + \ldots + \mu _ { m } = q$ . The summations in (5.13) and (5.14) are over sets of suitable “special labelled trees". We next insert

$$
Y _ { \imath } ^ { ( \mu ) } = \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } k _ { \jmath } ^ { ( \mu ) }
$$

into (5.13) and (5.14) and so obtain from (5.12)

$$
k _ { \ i } ^ { ( q ) } ( 0 ) = q \sum \frac { \partial ^ { m + n } f ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { \jmath = 1 } ^ { s } a _ { i \jmath } k _ { \jmath } ^ { ( \mu _ { 1 } ) } ( 0 ) , \dots , Z _ { \imath } ^ { ( \nu _ { 1 } ) } ( 0 ) , \dots \right)
$$

and

$$
0 = g _ { y } ( y _ { 0 } ) \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } k _ { \jmath } ^ { ( q ) } ( 0 ) + \sum _ { m \geq 2 } \frac { \partial ^ { m } g ( y _ { 0 } ) } { \partial y ^ { m } } \biggl ( \sum _ { j = 1 } ^ { s } a _ { \imath j } k _ { \jmath } ^ { ( \mu _ { 1 } ) } ( 0 ) , \dots \biggr ) .
$$

Iserting( $Z _ { \jmath } ^ { ( q - 1 ) } ( 0 )$ we get

$$
\begin{array} { l } { { ( - g _ { y } f _ { z } ) ( y _ { 0 } , z _ { 0 } ) \displaystyle \sum _ { j = 1 } ^ { s } a _ { \imath g } Z _ { \jmath } ^ { ( q - 1 ) } ( 0 ) \ ~ } } \\ { { \displaystyle ~ = \sum _ { \jmath = 1 } ^ { s } a _ { \imath g } \displaystyle \sum _ { ( m , n ) \neq ( 0 , 1 ) } g _ { \jmath } ( y _ { 0 } ) \displaystyle \frac { \partial ^ { m + n } f ( y _ { 0 } , z _ { 0 } ) } { \partial y ^ { m } \partial z ^ { n } } \left( \sum _ { l = 1 } ^ { s } a _ { \jmath l } k _ { l } ^ { ( \mu _ { 1 } ) } ( 0 ) , \dots , Z _ { \jmath } ^ { ( \nu _ { 1 } ) } ( 0 ) , \dots \right) } } \\ { { \displaystyle ~ + \frac { 1 } { q } \sum _ { m \geq 2 } \frac { \partial ^ { m } g ( y _ { 0 } ) } { \partial y ^ { m } } \left( \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } k _ { \jmath } ^ { ( \mu _ { 1 } ) } ( 0 ) , \dots \right) . } } \end{array}
$$

Thisformulallows ustocompute $Z _ { \imath } ^ { ( q - 1 ) }$ , whenever $( g _ { y } f _ { z } )$ and $\left( { a _ { \iota } } _ { \jmath } \right)$ are invertible. We denote the coeficients of the inverse of $\left( { { a _ { \iota } } _ { \ j } } \right)$ by $\omega _ { \imath \jmath }$ ,i.e.,

$$
( \omega _ { \imath \jmath } ) = ( a _ { \imath \jmath } ) ^ { - 1 } .
$$

The following result then follows by induction on $q$ from (5.16) and (5.18).

Theorem 5.6 (HLR89). The derivatives of $k _ { i }$ and $Z _ { i }$ satisfy

$$
\begin{array} { r l } & { k _ { i } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle t \in L D A T 2 _ { y , \varrho } ( t ) = q } \gamma ( t ) \Phi _ { \iota } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } \\ & { Z _ { \iota } ^ { ( q ) } ( 0 ) = \displaystyle \sum _ { \scriptstyle u \in L D A T 2 _ { z } , \varrho ( u ) = q } \gamma ( u ) \Phi _ { \iota } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) , } \end{array}
$$

where the coefficients $\Phi _ { \imath } ( t )$ and $\Phi _ { i } ( u )$ are given by $\Phi _ { \imath } ( \tau ) = 1$ and

$$
\Phi _ { \imath } ( t ) = \sum _ { \mu _ { 1 } , \dots , \mu _ { m } } a _ { \imath \mu _ { 1 } } \cdot \cdot \cdot a _ { i \mu _ { m } } \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } ) \Phi _ { i } ( u _ { 1 } ) \cdot \cdot \cdot \Phi _ { \imath } ( u _ { n } )
$$

$$
i f \ t = [ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }
$$

$$
\Phi _ { \imath } ( u ) = \sum _ { \jmath , \mu _ { 1 } , . . , \mu _ { m } } \omega _ { i j } a _ { \jmath \mu _ { 1 } } \cdot \cdot \cdot a _ { \jmath \mu _ { m } } \cdot \Phi _ { \mu _ { 1 } } ( t _ { 1 } ) \cdot \cdot \cdot \Phi _ { \mu _ { m } } ( t _ { m } )
$$

$$
i f \ u = [ t _ { 1 } , \dots , t _ { m } ] _ { z }
$$

and the rational coefficients $\gamma ( t )$ and $\gamma ( u )$ are defined by $\gamma ( \tau ) = 1$ and

$$
\begin{array} { l l } { { \gamma ( t ) = \varrho ( t ) \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) \gamma ( u _ { 1 } ) \dots \gamma ( u _ { n } ) } } & { { i f ~ t = [ t _ { 1 } , \dots , t _ { m } , u _ { 1 } , \dots , u _ { n } ] _ { y } ~ , } } \\ { { \gamma ( u ) = { \frac { 1 } { \varrho ( u ) + 1 } } ~ \gamma ( t _ { 1 } ) \dots \gamma ( t _ { m } ) } } & { { i f ~ u = [ t _ { 1 } , \dots , t _ { m } ] _ { z } . } } \end{array}
$$

The derivatives of the numerical solution $y _ { 1 }$ are now obtained from (5.11). In order to get those of $z _ { 1 }$ , we compute $\ell _ { i }$ from (5.10c) and insert it into (5.10a). This yields

$$
z _ { 1 } = z _ { 0 } + \sum _ { \imath , \jmath = 1 } ^ { s } b _ { i } \omega _ { \imath \jmath } ( Z _ { j } - z _ { 0 } )
$$

and its derivatives are given by

$$
z _ { 1 } ^ { ( q ) } ( 0 ) = \sum _ { i , \jmath = 1 } ^ { s } b _ { i } \omega _ { \imath j } Z _ { j } ^ { ( q ) } ( 0 ) .
$$

We thus obtain the following result.

Theorem 5.7. The numerical solution of (5.10) satisfies

$$
\begin{array} { l } { { \displaystyle y _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { t \in L D A T 2 _ { y } , \varrho ( t ) = q } \gamma ( t ) \sum _ { i = 1 } ^ { s } b _ { i } \Phi _ { \imath } ( t ) F ( t ) ( y _ { 0 } , z _ { 0 } ) } , } \\ { { \displaystyle z _ { 1 } ^ { ( q ) } | _ { h = 0 } = \sum _ { u \in L D A T 2 _ { z } , \varrho ( u ) = q } \gamma ( u ) \sum _ { i , j = 1 } ^ { s } b _ { \imath } \omega _ { i j } \Phi _ { \jmath } ( u ) F ( u ) ( y _ { 0 } , z _ { 0 } ) } , } \end{array}
$$

where the coefficients $\gamma$ and $\Phi _ { i }$ are given in Theorem 5.6.

# Order Conditions

A comparison of Theorem 5.7 with Theorem 5.5 gives

Theorem 5.8 (HLR89). For the Runge-Kutta method (5.10) we have

$$
\begin{array} { r l } & { y ( x _ { 0 } + h ) - y _ { 1 } = \mathcal { O } ( h ^ { p + 1 } ) \quad \quad i f } \\ & { \qquad \displaystyle \sum _ { \iota = 1 } ^ { s } b _ { \iota } \Phi _ { \iota } ( t ) = \frac { 1 } { \gamma ( t ) } \quad f o r \quad t \in D A T 2 _ { y } , \varrho ( t ) \le p , } \\ & { z ( x _ { 0 } + h ) - z _ { 1 } = \mathcal { O } ( h ^ { q + 1 } ) \quad \quad i f f } \\ & { \qquad \displaystyle \sum _ { \iota , j = 1 } ^ { s } b _ { \iota } \omega _ { \iota _ { y } } \Phi _ { \jmath } ( u ) = \frac { 1 } { \gamma ( u ) } \quad f o r u \in D A T 2 _ { z } , \varrho ( u ) \le q , } \end{array}
$$

where the coefficients $\gamma$ and $\Phi _ { i }$ are those of Theorem 5.6 and $\omega _ { \imath \jmath }$ is given by (5.19). □

Remark 5.9. Let $P ( x _ { 0 } ) = I - ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } ) ( y _ { 0 } , z _ { 0 } )$ be the projection introduced in Definition 4.3. Since $P ( x _ { 0 } ) f _ { z } ( y _ { 0 } , z _ { 0 } ) \dot { = } 0$ we have

$$
P ( x _ { 0 } ) F ( t ) ( y _ { 0 } , z _ { 0 } ) = 0
$$

for all trees $t \in D A T 2 _ { y }$ of the form $t = [ u ] _ { y }$ with $u \in D A T 2 _ { z }$ . Consequently, such trees of order $p$ need not be considered for the construction of Runge-Kutta methods of order $p$ (see Theorem 4.5).

Applying repeatedly the definition of $\Phi _ { i }$ in Theorem 5.6 we get the following algorithm:

Forming the Order Condition for a Given Tree. Attach to each vertex one summation index; if the root is fat,attach three indices to this root. Then the left hand side of the order condition is a sum over all indices of a product with factors

$\begin{array} { r l } & { b _ { i } } \\ & { b _ { \iota } \omega _ { i j } \omega _ { j k } } \\ & { a _ { \iota j } } \\ & { \omega _ { \iota j } } \end{array}$ if $^ { \mathfrak { s } \mathfrak { e } } _ { i } \mathfrak { p }$ is the index of a meagre root; if $^ { \ast \epsilon } i , j , k ^ { \prime \prime }$ are the three indices of a fat root; if $^ { \bullet \bullet } \ j ^ { \bullet }$ lies directly above $^ { 6 6 } i ^ { 2 9 }$ and $^ { 6 6 } j ^ { 3 9 }$ is meagre; if $^ { 6 6 } j ^ { 3 9 }$ lies directly above $^ { \mathfrak { s } _ { i } \mathfrak { s } }$ and $^ { 6 6 } j ^ { 3 9 }$ is fat.

In Table 5.1 we collect the order conditions for some trees of DAT2． We have not included the trees which have only meagre vertices, because their order condition is exactly the same as that of Sect.I.2 (Table 2.2). Several trees of DAT2 lead to the same order condition (Exercise 2). We also observe that some of the order conditions for the trees $[ u ] _ { y }$ with $u \in D A T 2 _ { z }$ are identical to those for index 1 problems (see Exercise 1 of Sect. VI.4).

Table 5.1. Trees and order conditions   

<table><tr><td>g（t）</td><td>graph</td><td>order condition</td></tr><tr><td>2</td><td>Y</td><td>∑bwc²=1</td></tr><tr><td>3</td><td>Y</td><td>∑bwo²=1</td></tr><tr><td>3</td><td>Y</td><td>∑bwGakCk=</td></tr><tr><td>3</td><td>Y</td><td>∑bciwijo²=</td></tr><tr><td>3</td><td></td><td>∑bwC²wkc²= 4</td></tr><tr><td>@(u）</td><td>graph</td><td>order condition</td></tr><tr><td>1</td><td>Y</td><td>∑bwjwkc²=2 ∑bw2wjko=3</td></tr><tr><td>2</td><td rowspan="2"></td><td>∑biwijwkkakee=</td></tr><tr><td>2</td><td></td></tr><tr><td>2</td><td></td><td>∑biwiGwjc²=2</td></tr></table>

# Simplifying Assumptions

For the construction of implicit Runge-Kutta methods the simplifying conditions $B ( p ) , C ( \eta ) , D ( \xi )$ of Sect.IV.5 play an important role. The following result extends Theorem IV.5.1 to index 2 problems.

Theorem 5.10 (HLR89, p.67). Suppose that the Runge-Kutta matrix $\left( a _ { \imath j } \right)$ is invertible and that $b _ { \imath } = a _ { s \imath }$ for $i = 1 , \dots , s$ . Then the conditions $B ( p ) , C ( \eta ) , D ( \xi )$ with $p \leq 2 \eta$ and $p \leq \eta + \xi + 1$ imply that the $y$ -component of the local error of (5.1) satisfies

$$
y _ { 1 } - y ( x _ { 0 } + h ) = \mathcal { O } ( h ^ { p + 1 } ) .
$$

Proof. We just outline the main ideas; details are given in (HLR89, pp.64-67). As in Sect.II.7 (Fig.II.7.1) we first simplify the order conditions with the help of $C ( \eta )$ . This implies that trees with a branch ending with $[ \tau , \ldots , \tau ] _ { y }$ (the number of $\tau$ 's is $k - 1 \AA$ ）where $k \leq \eta$ need no longer be considered. If we write $C ( \eta )$ in the form

$$
\sum _ { \jmath = 1 } ^ { s } \omega _ { \imath \jmath } c _ { \jmath } ^ { k } = k c _ { \imath } ^ { k - 1 } \qquad \mathrm { f o r } \quad k = 1 , \ldots , \eta ,
$$

we observe that trees ending with $[ \tau , \dots , \tau ] _ { z }$ can also be reduced if the number of $\boldsymbol { \tau } ^ { \prime } \boldsymbol { \mathsf { s } }$ is between 1 and $\eta$

The simplifying condition $D ( \xi )$ allows us to remove trees $[ \tau , \ldots , \tau , t ] _ { y }$ with $t \in D A T _ { y }$ , where the number of $\tau$ 's is $\leq \xi$ . Writing $D ( \xi )$ as

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } c _ { i } ^ { k } \omega _ { i j } = \sum _ { \ i = 1 } ^ { s } b _ { \ i } \omega _ { \ i j } - k b _ { \ j } c _ { \ j } ^ { k - 1 } \quad \mathrm { ~ f o r ~ } \quad k = 1 , \dots , \xi
$$

it follows that the trees $\left\{ \tau , \ldots , \tau , u \right\} _ { y }$ with $u \in D A T _ { z }$ (number of $\tau$ 's is $k$ ) can also be eliminated for $1 \leq k \leq \xi$ . Since $p \leq 2 \eta$ and $p \leq \eta + \xi + 1$ all that remains after these reductions are the bushy trees $[ \tau , \dots , \tau ] _ { y }$ whose order conditions are satisfied by $B ( p )$ ,and trees of the form $[ u ] _ { y }$ with $u \in D A T _ { z }$ . Because of the assumption $b _ { \imath } = a _ { s \imath }$ we have

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } \omega _ { \ i \jmath } = \left\{ \begin{array} { l l } { { 0 } } & { { \mathrm { i f } \quad j = 1 , \ldots , s - 1 } } \\ { { 1 } } & { { \mathrm { i f } \quad j = s , } } \end{array} \right.
$$

and these trees can also be reduced to the bushy trees.

Remark. If the function $f$ of (5.1a) is linear in $z$ ,i.e.,

$$
f ( y , z ) = f _ { 0 } ( y ) + f _ { z } ( y ) z ,
$$

then the elementary diferentials for trees $[ t _ { 1 } , \ldots , t _ { m } , u _ { 1 } , \ldots , u _ { n } ] _ { y }$ with $n \geq 2$ vanish identically and the corresponding order conditions need not be considered.

In this situation the assumption $p \leq 2 \eta$ can be relaxed to $p \leq 2 \eta + 1$ . An important class of problems satisfying (5.26) are constrained mechanical systems in the index 2 formulation (1.46a,b,d).

As an illustration of Theorem 5.10 we consider the Lobatto IIC methods. They satisfy $B ( p ) , C ( \eta ) , D ( \xi )$ with $p = 2 s - 2$ ， $\eta = s - 1$ and $\xi = s - 1$ (see Table IV.5.13) and also $a _ { s _ { 1 } } = b _ { \ i }$ . It therefore follows from Theorem 5.10 that the local error satisfies $\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { 2 s - 1 } )$

The following result shows that for methods which do not satisfy $a _ { s 2 } = b _ { \imath }$ it is unlikely that the estimates of Lemma 4.4 can be improved.

Lemma 5.11. Let $p$ be the largest integer such that the $y$ -component of the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { p + 1 } ) .
$$

If the Runge-Kutta matrix is invertible and $c _ { \imath } \neq 1$ for all $i$ , then

$$
\boldsymbol { p } \le \boldsymbol { s } ^ { * }
$$

where s\* is the number ofdistinct non-zero values among C1,.. Cg.

Proof. The order conditions for the trees $[ [ \tau , \dots , \tau ] _ { z } ] _ { y }$ imply that

$$
\sum _ { \ i , \ i = 1 } ^ { s } b _ { \ i } \omega _ { \ i j } \int _ { 0 } ^ { c _ { \jmath } } q ( t ) d t = \int _ { 0 } ^ { 1 } q ( t ) d t
$$

for all polynomials $q ( t )$ of degree $\le p - 1$ .Put $q ( t ) = d ^ { \prime } ( t )$ ，where $d ( t )$ isa polynomial of minimal degree such that $d ( c _ { \imath } ) = 0$ for all $i$ ， $d ( 0 ) = 0$ and $d ( 1 ) \neq 0$ Condition (5.27) is violated by this polynomial. The inequality $\boldsymbol { p } \le \boldsymbol { s } ^ { * }$ now follows because the degree of this polynomial $q ( t )$ is $s ^ { * }$ □

# Projected Runge-Kutta Methods

It is, of course, interesting to study the convergence order of projected Runge-Kutta methods (Definition 4.11） which are not yet covered by Theorem 4.12. The main tool for the subsequent study is the following interpretation of projected Runge-Kutta methods.

![](images/310b74d6baaee9773caa2cfee6bbf9b3dfba542279d390d182c6c758543e75a9.jpg)  
Table 5.2. Original and extended Runge-Kutta methods

Lemma 5.12 (Lubich 1991). Consider an $s$ -stage Runge-Kutta method with invertible coefficient matrix A and the extended $( s + 1 )$ -stage method defined in Table 5.2. For an initial value $y _ { 0 }$ satisfying $g ( y _ { 0 } ) = 0$ denote their numerical solutions after one step by $y _ { 1 }$ and $y _ { 1 } ^ { \varepsilon }$ ， respectively. If the function $f$ in $\left( 5 . l a \right)$ is linear in $z \ ( i . e . ,$ (5.26) is satisfied), then the numerical solution $\widehat { y } _ { 1 }$ of the projected Runge-Kutta method (4.1), (4.38) satisfies

$$
\widehat { y } _ { 1 } - y _ { 1 } ^ { \varepsilon } = { \mathcal { O } } ( h \varepsilon )
$$

for $h$ sufficiently small and $\varepsilon \to 0$

Proof. The last stage of the extended $( s + 1 )$ -stage Runge-Kutta method reads

$$
\begin{array} { c } { Y _ { s + 1 } = y _ { 1 } + h \varepsilon f ( Y _ { s + 1 } , Z _ { s + 1 } ) } \\ { 0 = g ( Y _ { s + 1 } ) } \end{array}
$$

and we have $y _ { 1 } ^ { \varepsilon } = Y _ { s + 1 }$ (note that this is the result of an implicit Euler step with step size $h \varepsilon$ starting from $y _ { 1 }$ ). Using the linearity of $f$ with respect to $z$ and putting $\lambda = h \varepsilon Z _ { s + 1 }$ we obtain

$$
\begin{array} { l } { { y _ { 1 } ^ { \varepsilon } = y _ { 1 } + h \varepsilon f _ { 0 } ( y _ { 1 } ^ { \varepsilon } ) + f _ { z } ( y _ { 1 } ^ { \varepsilon } ) \lambda } } \\ { { \quad 0 = g ( y _ { 1 } ^ { \varepsilon } ) . } } \end{array}
$$

Comparing (5.30) with (4.38) the implicit function theorem implies that (5.28) is satisfied for sufficiently small $h$ and $\varepsilon$ . □

The implicit function theorem, applied to (5.30),also shows that $y _ { 1 } ^ { \varepsilon }$ is as often differentiable with respect to $h$ and $\varepsilon$ as the right-hand side of the problem(5.1) is. Hence,the Taylor series expansion of $y _ { 1 } ^ { \varepsilon }$ with respect to $h$ has coefficients which converge to a finite limit as $\varepsilon  0$ .

The order conditions for a projected Runge-Kutta method (applied to (5.1), (5.26)） can thus be obtained by considering the limit $\varepsilon  0$ in the order condi-tions for the extended Runge-Kutta method (Exercise 5). Let us illustrate this by extending the statement of Theorem 5.10 to projected Runge-Kutta methods.

Theorem 5.13 (Lubich 1991). Suppose that the Runge-Kutta matrix $A$ is invertible and that the index 2 problem satisfies (5.26). Then the conditions $B ( p ) , \ C ( \eta ) _ { ! }$ $D ( \xi )$ with $p \leq 2 \eta + 1$ and $p \leq \eta + \xi + 1$ imply that the local error of the projected Runge-Kutta method satisfies

$$
\widehat { y } _ { 1 } - y \big ( x _ { 0 } + h \big ) = \mathcal { O } \big ( h ^ { p + 1 } \big ) .
$$

If in addition $p \leq 2 \eta$ then (5.31) holds also when $f$ is nonlinear in $z$

Proof. One verifies that the conditions $B ( p ) , ~ C ( \eta ) , ~ D ( \xi )$ ， (5.23), (5.24) and (5.25）are,in the limit $\varepsilon  0$ ，also satisfied for the extended method of Table 5.2.Let us demonstrate this for the Condition (5.23). The inverse of the extended

Runge-Kutta matrix is given by

$$
\left( \begin{array} { c c } { { A } } & { { 0 } } \\ { { b ^ { T } } } & { { \varepsilon } } \end{array} \right) ^ { - 1 } = \left( \begin{array} { c c } { { A ^ { - 1 } } } & { { 0 } } \\ { { - \varepsilon ^ { - 1 } b ^ { T } A ^ { - 1 } } } & { { \varepsilon ^ { - 1 } } } \end{array} \right) .
$$

Therefore (5.23) is seen to be satisfied for $i = 1 , \dots , s$ .For $i = s + 1$ one gets

$$
\sum _ { j = 1 } ^ { s + 1 } \omega _ { s + 1 , j } c _ { j } ^ { k } = - \varepsilon ^ { - 1 } \sum _ { \iota , \jmath = 1 } ^ { s } b _ { \iota } \omega _ { \iota \jmath } c _ { \jmath } ^ { k } + \varepsilon ^ { - 1 } ( 1 + \varepsilon ) ^ { k } .
$$

Using(5.23） for $i \leq s$ and $B ( p )$ the right-hand expression of (5.33） becomes $- \varepsilon ^ { - 1 } + \varepsilon ^ { - 1 } ( 1 + \varepsilon ) ^ { k }$ and tends to $k$ for $\varepsilon \to 0$ ． Hence,Condition (5.23） is, in the limit $\varepsilon  0$ , also satisfied for $i = s + 1$ . As in the proof of Theorem 5.10 (see also the remark after that proof) we deduce the statement for the case where $f ( y , z )$ is linear in $z$

The generalization to nonlinear problems can be proved by a perturbation argument. We let $z ( x )$ be the exact solution of (5.1) and consider the problem (Lubich 1991)

$$
\begin{array} { c } { { u ^ { \prime } = f ( u , z ( x ) ) + f _ { z } ( u , z ( x ) ) \lambda } } \\ { { 0 = g ( u ) } } \end{array}
$$

in the variables $u$ and $\lambda$ . This new problem is of index 2 again and has obviously the solution $u ( x ) = y ( x )$ and $\lambda ( x ) = 0$ ． Since (5.34） is linear in the algebraic variable $\lambda$ , the theorem can be applied and we get for the projected Runge-Kuta solution

$$
\widehat { u } _ { 1 } - y ( x _ { 0 } + h ) = \mathcal { O } \big ( h ^ { p + 1 } \big ) .
$$

We still have to estimate $\widehat { y } _ { 1 } - \widehat { u } _ { 1 }$ . This is possible with the help of Theorem 4.2. In addition to the nonlinear system (4.2) (with $\eta = y _ { 0 }$ ） we consider the method applied to (5.34):

$$
\begin{array} { l } { { U _ { \scriptscriptstyle 2 } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { \scriptscriptstyle 1 j } \Big ( f \big ( U _ { j } , z \big ( x _ { 0 } + c _ { \scriptscriptstyle j } h \big ) \big ) + f _ { z } \big ( U _ { \scriptscriptstyle 2 } , z \big ( x _ { 0 } + c _ { \scriptscriptstyle j } h \big ) \big ) \Lambda _ { \scriptscriptstyle j } \Big ) } } \\ { { 0 = g ( U _ { i } ) . } } \end{array}
$$

Its first line can be written as

$$
U _ { \imath } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } f \big ( U _ { j } , z ( x _ { 0 } + c _ { j } h ) + \Lambda _ { \jmath } \big ) + { \mathcal O } ( h \| \Lambda \| ^ { 2 } )
$$

where $\| \boldsymbol { \Lambda } \| = \operatorname* { m a x } _ { j } \| \boldsymbol { \Lambda } _ { \ j } \|$ . Theorem 4.2 thus yields

$$
\begin{array} { r } { \| U _ { \iota } - Y _ { \iota } \| \leq C h \| \Lambda \| ^ { 2 } } \\ { \| \Lambda _ { i } + z ( x _ { 0 } + c _ { \iota } h ) - Z _ { \iota } \| \leq C \| \Lambda \| ^ { 2 } . } \end{array}
$$

Since $C ( \eta )$ holds,the estimate (4.14) together with (5.37b) proves $\Lambda _ { i } = \mathcal { O } ( h ^ { \eta } )$ We therefore obtain $y _ { 1 } - u _ { 1 } = \mathcal { O } \big ( h ^ { 2 \eta + 1 } \big )$ with the help of (5.37), and $\widehat { y } _ { 1 } - \widehat { u } _ { 1 } =$ $\mathcal { O } ( h ^ { 2 \eta + 1 } )$ as a consequence of $z _ { 1 } - z ( x _ { 0 } + h ) = \mathcal { O } \left( h ^ { \eta } \right)$ □

Examples. 1) Collocation methods satisfy $B ( p ) , C ( s )$ and $D ( p - s )$ where $s$ is the number of stages and $p$ the order of the underlying quadrature formula (consult Lemma IV.5.4). Hence, the above presentation provides an alternative proof of Theorem 4.12.

2) The projected $s$ -stage Radau IA method (see Table IV.5.13) has order $2 s - 1$ for problems which are linear in $z$ , and order $2 s - 2$ for general nonlinear index 2 problems.

# Exercises

1. Denote by $r$ the largest number such that the local error of the $z$ -component satisfies $\delta z _ { h } ( x ) = \mathcal { O } ( h ^ { r } )$ . For implicit Runge-Kutta methods with invertible coefficient matrix, $R ( \infty ) = 0$ and $c _ { j } \leq 1$ (all $j )$ prove that

$$
r \leq s ^ { * }
$$

where $s ^ { * }$ is the number of distinct non-zero values among $c _ { 1 } , \ldots , c _ { s }$ Hint. The order conditions for the bushy trees $\{ \tau , \ldots , \tau \} _ { z }$ imply that

$$
\sum _ { i , j , k } b _ { i } \omega _ { \iota j } \omega _ { \jmath k } \int _ { 0 } ^ { c _ { k } } q ( t ) d t = q ( 1 )
$$

for all polynomials $q ( t )$ of degree $\leq r - 1$ ·

2. If a tree of $D A T 2$ satisfies one of the following two conditions a) a fat vertex (different from the root) is singly branched b)a singly branched meagre vertex $( \neq \mathrm { { \bf ~ r o o t } } )$ is followed by a fat vertex then the corresponding order condition is equivalent to that of a tree of the same order but with fewer fat vertices. Consequently, trees satisfying either (a) or (b) need not be considered for the construction of Runge-Kutta methods.

3．Suppose that the function $f ( y , z )$ in (5.1) is linear in $z$ . Characterize the trees of DAT2 for which the elementary diferentials vanish identically.

4. With the help of Theorem 5.10 and Lemma IV.5.4 give a new (algebraic) proof of Theorem 4.9.

5. (Lubich 1991). Consider a projected Runge-Kutta method for index 2 problems which are linear in $z$ . Prove that $\widehat { y } _ { 1 } - y ( x _ { 0 } + h ) = \mathcal { O } \left( h ^ { 4 } \right)$ iff the condition

$$
\sum _ { \ i , \ j = 1 } ^ { s } b _ { \ i } ( 1 - c _ { \ i } ) \omega _ { \ i \ j } c _ { \ j } ^ { 2 } = \frac { 1 } { 3 }
$$

is satisfied in addition to the four order conditions already needed for ordinary differential equations.

# VII.6Half-Explicit Methods for Index 2 Systems

The methods of Sects. VI.3 and VII.4 do not use the semi-explicit structurc of the differential-algebraic equation

$$
y ^ { \prime } = f ( y , z ) , \qquad 0 = g ( y )
$$

$( y \in \mathbb { R } ^ { n } , z \in \mathbb { R } ^ { m } )$ and can as well be applied to more general situations. Here we shall show how this structure can be exploited for the derivation of new, efficient integration methods. The main idea is to discretize the differential variables $y$ in an explicit manner, and the algebraic variables $z$ in an implicit manner.

The most simple method of this type is the half-explicit Euler method

$$
\begin{array} { c } { { y _ { 1 } = y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) } } \\ { { 0 = g ( y _ { 1 } ) . } } \end{array}
$$

Inserting (6.2a) into (6.2b) yields the nonlinear system $0 = g \big ( y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) \big )$ for $z _ { 0 }$ . It possesses a locally unique solution, if

$$
g _ { y } ( y ) f _ { z } ( y , z ) \mathrm { i s ~ i n v e r t i b l e }
$$

at $( y _ { 0 } , z _ { 0 } )$ . Once $z _ { 0 }$ is computed, the value $y _ { 1 }$ is determined explicitly by (6.2a).

This example shows some interesting features of half-explicit methods. Com-pared to the implicit Euler discretization, it can be implemented more efficiently. because the nonlinear system is of reduced dimension ( $m$ instead of $\hbar + m ,$ ). Compared to the explicit Euler method in the mode “index reduction and projection” (sec Sect.VI.2), it avoids an accurate computation of the derivative $g _ { y } \{ y \}$ .The numerical approximation $y _ { 1 }$ only depends on an initial value of the $y$ -component, as does the exact solution of (6.1).

In this section we shall develop half-explicit Runge-Kutta methods, extrapolation methods,and multistep methods. They are in particular very efficient for constrained mechanical systems in their index 2 formulation, because nonlinear systems are completely avoided in this situation (see below).

# Half-Explicit Runge-Kutta Methods

In HLR89,the following extension of (6.2) to explicit Runge-Kutta methods is proposed:

$$
\begin{array} { r l } { \displaystyle Y _ { \boldsymbol \tau } = y _ { 0 } + \hbar \sum _ { \boldsymbol \jmath = 1 } ^ { \boldsymbol \tau - 1 } a _ { \boldsymbol \imath \boldsymbol \jmath } f ( \boldsymbol Y _ { \boldsymbol \jmath } , \boldsymbol Z _ { \boldsymbol \jmath } ) , } & { \quad i = 1 , \dots , s } \\ { \displaystyle \boldsymbol 0 = g ( Y _ { \boldsymbol \imath } ) } \\ { \displaystyle y _ { \boldsymbol \imath } = y _ { 0 } + \hbar \sum _ { \boldsymbol \imath = 1 } ^ { s } b _ { \boldsymbol \imath } f ( Y _ { \boldsymbol \imath } , \boldsymbol Z _ { \boldsymbol \imath } ) , } \\ { \displaystyle \boldsymbol 0 = g ( y _ { \boldsymbol \imath } ) . } \end{array}
$$

We have $Y _ { 1 } = y _ { 0 }$ ,and Eq. (6.4b) is automatically satisfied for $i = 1$ , because the initial value is assumed to be consistent. We next insert $Y _ { 2 }$ from (6.4a) into (6.4b) and obtain a nonlinear equation for $Z _ { 1 }$ ，which has a (locally) unique solution, if $a _ { 2 1 } \neq 0$ and the usual index 2 assumption (6.3) is satisfied.We thus obtain $Z _ { 1 }$ and $Y _ { 2 }$ . The next step allows us to compute $Z _ { 2 }$ and $Y _ { 3 }$ ,etc.

The local error and convergence properties of (6.4) are studied in HLR89 and Brasey & Hairer (1993). It turns out that the coeficients $a _ { \scriptscriptstyle \imath \jmath } , b _ { \scriptscriptstyle \imath }$ have to satisfy additional order conditions. As a consequence, 8 stages are needed for a 5th order method (Brasey 1992), compared to only 6 stages for classical Runge-Kutta methods (see Sect. II.5). Arnold (1995) and Murua (1995) have independently proposed a modification, which simplifies the order conditions and makes the approach more efcient. Their main idea is to introduce an explicit stage $Y _ { 1 } = y _ { 0 } , Z _ { 1 } = z _ { 0 }$ ， $Y _ { 2 } = y _ { 0 } + h a _ { 2 1 } f ( y _ { 0 } , z _ { 0 } )$ , and to suppress the condition $g ( Y _ { 2 } ) = 0$ in the second stage. We follow here the approach of Murua (1995), because it is slightly more general. For consistent initial values $( y _ { 0 } , z _ { 0 } )$ we define

$$
\begin{array} { l } { { Y _ { 1 } = y _ { 0 } , ~ } } \\ { { \displaystyle } } \\ { { Y _ { \imath } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \imath \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) , ~ i = 2 , \ldots , s } } \\ { { \displaystyle } } \\ { { \widehat { Y _ { \imath } } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { \imath } \widehat { a } _ { \imath \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) , ~ } } \\ { { \displaystyle } } \\ { { y _ { 1 } = \widehat { Y } _ { \imath } . } } \end{array}
$$

The value $z _ { 1 }$ can either be computed from the hidden constraint $g _ { y } ( y _ { 1 } ) f ( y _ { 1 } , z _ { 1 } ) =$ $0$ , or from the additional stage

$$
\widehat { Y } _ { s + 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s + 1 } \widehat { a } _ { s + 1 , \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) , \qquad 0 = g ( \widehat { Y } _ { s + 1 } )
$$

as $z _ { 1 } = Z _ { s + 1 }$ . Here we have put $Y _ { s + 1 } = y _ { 1 }$ ， so that the value $f ( Y _ { s + 1 } , Z _ { s + 1 } )$

can be reused as $f ( y _ { 0 } , z _ { 0 } )$ for the next step. A significant difference comparcd to the original approach (6.4) is that the numerical solution $( y _ { 1 } , z _ { 1 } )$ depends on both initial values ( $y _ { 0 }$ and $z _ { 0 }$ ).

Existence of the Numerical Solution. Suppose that the initial values satisfy $g ( y _ { 0 } ) = 0$ and $g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } ) = \mathcal { O } ( \delta )$ with some sufficiently small $\delta > 0$ (we have to admit small perturbations in the hidden constraint, because in general the approximation $z _ { 1 }$ of (6.5e) does not satisfy $g _ { y } ( y _ { 1 } ) f ( y _ { 1 } , z _ { 1 } ) = 0 )$ . By an induction argument we assume that the values $\{ \Sigma _ { \mathfrak { j } } ^ { \prime } , \bar { Z _ { j } } )$ are already known for $j = 1 , \dots , i - 1$ ， and satisfy $Y _ { \jmath } = y _ { 0 } + \mathcal { O } ( h ) , Z _ { \jmath } = z _ { 0 } + \mathcal { O } ( h + \delta )$ .Then, $Y _ { \imath }$ is explicitly given by (6.5b), and we have $Y _ { \imath } = y _ { 0 } { \dot { + } } \mathcal { O } ( h )$ . As in (3.13) we now write the condition $0 = g ( \widehat { Y } _ { \mathfrak { a } } )$ as

$$
0 = \int _ { 0 } ^ { 1 } g _ { y } \big ( y _ { 0 } + \tau ( \widehat { Y } _ { \iota } - y _ { 0 } ) \big ) \mathop { } { d \tau } \cdot \sum _ { \jmath = 1 } ^ { \iota } \widehat { a } _ { \iota \jmath } f ( Y _ { \jmath } , Z _ { \jmath } ) ,
$$

where ${ \widehat { Y } } _ { i }$ has to be replaced by (6.5c). This is a nonlinear equation of the form $F ( Z _ { \iota } , \lambda ) = 0$ . Since $F ( z _ { 0 } , 0 ) = \mathcal { O } ( \delta )$ and

$$
\frac { \partial F } { \partial z } ( z _ { 0 } , 0 ) = \widehat { a } _ { \boldsymbol { \imath } \boldsymbol { \imath } } \cdot g _ { \boldsymbol { y } } ( y _ { 0 } ) f _ { z } ( y _ { 0 } , z _ { 0 } ) ,
$$

it follows from the Implicit Function Theorem that (6.6) has a locally unique solution, if (6.3) and the condition

$$
\widehat { \boldsymbol { a } } _ { \iota \iota } \neq 0 \qquad \mathrm { f o r a l l } \enspace \iota
$$

hold. Moreover we have $Z _ { i } = z _ { 0 } + \mathcal { O } ( \mathit { l } _ { l } + \delta )$ ，

Error Propagation and Convergence. For inconsistent initial values we replace the nonlinear equation in (6.5c） by $g ( \widehat { Y } _ { \imath } ) = g ( y _ { 0 } )$ ，so that the method is welldefined in a whole neighbourhood of the solution manifold (observe that the above existence result is still valid). Such an extension has the advantage that differentiation with respect to initial values is possible. The method (6.5) with $z _ { 1 }$ from (6.5e), can thus be written as

$$
\begin{array} { l } { { y _ { n + 1 } = y _ { n } + h \Phi ( y _ { n } , z _ { n } , h ) } } \\ { { z _ { n + 1 } = \Psi ( y _ { n } , z _ { n } , h ) } } \end{array}
$$

with smooth functions $\Phi$ and $\Psi$ . For the study of convergence and, in particular, of the order conditions the triangular matrix

$$
W = \left( w _ { \imath \jmath } \right) _ { i , \jmath = 1 } ^ { s + 1 } = \left( \begin{array} { c c c c } { { 1 } } & { { } } & { { } } & { { } } \\ { { \widehat { a } _ { 2 1 } } } & { { \widehat { a } _ { 2 2 } } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \ddots } } & { { } } \\ { { \widehat { a } _ { s + 1 , 1 } } } & { { \widehat { a } _ { s + 1 , 2 } } } & { { \cdots } } & { { \widehat { a } _ { s + 1 , * + 1 } } } \end{array} \right)
$$

will play an important role.

Lemma 6.1. Suppose that the method (6.5), satisfying (6.7), is written in the form (6.8). If $g ( y _ { 0 } ) = 0$ and $g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } ) = \mathcal { O } ( h )$ ,it holds

$$
\frac { \partial \Phi } { \partial z } ( y _ { 0 } , z _ { 0 } , h ) = O ( h ) , \qquad \frac { \partial \Psi } { \partial z } ( y _ { 0 } , z _ { 0 } , h ) = w _ { s + 1 , 1 } \cdot I + O ( h ) ,
$$

where $w _ { s + 1 , 1 } \ i s \ g i \nu e n \ b y \ ( 6 . 9 )$

Proof. From (6.5b) it follows that $\partial Y _ { \scriptscriptstyle \imath } / \partial z _ { 0 } = \mathcal { O } ( h )$ . Differentiation of (6.5c) with respect to $z _ { 0 }$ thus yields

$$
\begin{array} { c } { \displaystyle \frac { \partial \widehat { Y } _ { \imath } } { \partial z _ { 0 } } = h \displaystyle \sum _ { \jmath = 1 } ^ { \imath } \widehat { a } _ { \imath g } f _ { \imath } ( \boldsymbol { y } _ { 0 } , \boldsymbol { z } _ { 0 } ) \displaystyle \frac { \partial Z _ { \jmath } } { \partial \boldsymbol { z } _ { 0 } } + \mathcal { O } ( h ^ { 2 } ) , } \\ { \displaystyle 0 = g _ { y } ( \boldsymbol { y } _ { 0 } ) \displaystyle \frac { \partial \widehat { Y } _ { \imath } } { \partial \boldsymbol { z } _ { 0 } } + \mathcal { O } ( h ^ { 2 } ) . } \end{array}
$$

Inserting (6.10a) into (6.10b) and multiplying with the inverse of the matrix $g _ { y } ( y _ { 0 } ) f _ { z } ( y _ { 0 } , z _ { 0 } )$ ， gives the relation

$$
\sum _ { \jmath = 1 } ^ { \imath } \widehat { a } _ { \imath \jmath } { \frac { \partial Z _ { \jmath } } { \partial z _ { 0 } } } = { \mathcal { O } } ( h ) \qquad { \mathrm { f o r } } i = 2 , \dots , s + 1 .
$$

The statement now follows from $Z _ { 1 } = z _ { 0 }$ ,i.e., ${ \partial Z _ { \scriptscriptstyle 1 } } / { \partial z _ { \scriptscriptstyle 0 } } = I$

Consider two pairs of initial values $( y _ { 0 } , z _ { 0 } ) , ( \widetilde { y } _ { 0 } , \widetilde { z } _ { 0 } )$ ，satisfying $g ( y _ { 0 } ) = 0$ ， $g ( \widetilde { y } _ { 0 } ) = 0$ ， $g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } ) = \mathcal { O } ( h )$ ， $g _ { y } ( \widetilde { y } _ { 0 } ) f ( \widetilde { y } _ { 0 } , \widetilde { z } _ { 0 } ) = \mathcal { O } ( h )$ ． It follows from Lemma 6.1 that the differences $\Delta y _ { 0 } = \dot { y _ { 0 } } - \widetilde { y _ { 0 } }$ ，... satisfy the recursion

$$
\begin{array} { r } { \left( \begin{array} { c } { \| \Delta y _ { 1 } \| } \\ { \| \Delta z _ { 1 } \| } \end{array} \right) \leq \left( \begin{array} { c c } { 1 + \mathcal { O } ( h ) } & { \mathcal { O } ( h ^ { 2 } ) } \\ { \mathcal { O } ( 1 ) } & { | w _ { s + 1 , 1 } | + \mathcal { O } ( h ) } \end{array} \right) \left( \begin{array} { c } { \| \Delta y _ { 0 } \| } \\ { \| \Delta z _ { 0 } \| } \end{array} \right) . } \end{array}
$$

The local error of the method (6.5) is defined as usual． We let $( y _ { 1 } , z _ { 1 } )$ be the numerical approximation for initial values $\bigl ( y ( x ) , z ( x ) \bigr )$ on the exact solution of (6.1),and denote it by $\delta y _ { h } ( x ) = y _ { 1 } - y ( x + \dot { h } )$ ， $\delta z _ { h } ( x ) = z _ { 1 } - z ( x + h )$

Theorem 6.2 (Murua 1995). Consider the problem (6.1) with consistent initial values. Suppose that (6.7) holds and that

$$
| w _ { s + 1 , 1 } | < 1 ,
$$

where $\boldsymbol { w } _ { \mathfrak { s } + 1 , 1 }$ is given in (6.9). If the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { r + 1 } ) , \qquad \delta z _ { h } ( x ) = \mathcal { O } ( h ^ { m } ) ,
$$

then we have for $x _ { n } - x _ { 0 } \leq C o n s t$

$$
y _ { n } - y ( x _ { n } ) = { \mathcal O } ( h ^ { \mathrm { m n } ( r , m + 1 ) } ) , \qquad z _ { n } - z ( x _ { n } ) = { \mathcal O } ( h ^ { \mathrm { m i n } ( r , m ) } ) .
$$

Proof. The recursion (6.11) allows us to apply Lemma VI.3.9 with $\varepsilon = h ^ { 2 }$ and $\alpha = | w _ { s + 1 , 1 } | + \mathcal { O } ( h )$ . This shows that the contribution of the local error at $x _ { \imath }$ t0 the global error at $x _ { n }$ is bounded by

$$
C \left( \| \delta y _ { h } ( x _ { \lambda } ) \| + h ^ { 2 } \| \delta z _ { h } ( x _ { \lambda } ) \| \right) , \qquad C \left( \| \delta y _ { h } ( x _ { \lambda } ) \| + ( h ^ { 2 } + \alpha ^ { n - 1 - \upsilon } ) \| \delta z _ { h } ( x _ { \lambda } ) \| \right)
$$

for the $y -$ and $z$ -component, respectively. Summing up these contributions proves the statement. □

Order Conditions. The order conditions for method (6.5） can be derived in the same way as for Runge-Kutta methods (previous section). The only difference is that at some places the coeficients $a _ { \scriptscriptstyle { \imath \jmath } }$ have to be replaced by $\widehat { a } _ { \iota \jmath }$ . Since $z _ { 1 } =$ $Z _ { s + 1 }$ ，the order conditions for the $z$ -component can be directly obtained from Theorem 5.6. The result is the following:

Forming the Order Condition for a Given Tree. Attach to each vertex one summa-tion index. Then the left-hand side of the order condition is a sum over all indices of a product with factors

$\begin{array} { r l } & { \widehat { a } _ { s \imath } } \\ & { w _ { s + 1 , \imath } } \\ & { a _ { \imath \jmath } } \\ & { \widehat { a } _ { \imath \jmath } } \\ & { w _ { \imath \jmath } } \end{array}$ if $^ { \mathfrak { s } _ { i } , \mathfrak { p } }$ is the index of a meagre root; if $^ { \mathfrak { s } } { } _ { i } \mathbf { \vec { \mu } } ^ { \mathfrak { s } }$ is the index of a fat root; if the meagre vertex $^ { 6 6 } \mathcal { I } ^ { \dag }$ lies directly above the meagre vertex $^ { \mathfrak { s } \mathfrak { e } } _ { i } \mathfrak { s }$ ； if the meagre vertex $^ { 6 6 } j ^ { 3 }$ lies directly above the fat vertex $^ { 6 6 } i ^ { , 3 }$ ； if the fat vertex $^ { 6 6 } j ^ { 3 }$ lies directly above the meagre vertex $^ { \mathfrak { s } \mathfrak { e } } _ { 2 } \mathfrak { s }$ ；

The right-hand side of the order condition is the inverse of the rational number $\gamma$ ， defined in Theorem 5.6.

In order to satisfy the assumption (6.13) of the convergence theorem,the order conditions have to be satisfied for trees $t \in D A T 2 _ { y }$ with $\varrho ( t ) \leq r$ ， and for trees $u \in D A T 2 _ { z }$ with $\varrho ( u ) \leq m - 1$

Construction of Methods. The trees of Sect.II.2 form a subset of the “index 2 trees” to be considered here. From the above construction principle it is clear that the coefficients $a _ { \scriptscriptstyle { \imath \jmath } } , b _ { \scriptscriptstyle { \imath } } : = \widehat { a } _ { \scriptscriptstyle { s \imath } }$ have to satisfy the classical order conditions of Sect. II.2. It is therefore natural to take a known, explicit Runge-Kutta method of a certain order and to determine $\widehat { a } _ { \iota \jmath }$ in such a way that the remaining order conditions are satisfied. Arnold (1995) and Murua (1995) have shown how half-explicit methods, based on the Dormand & Prince pair of Table II.5.2,can be constructed. Let us outline the main idea.

A significant simplification of the order conditions is obtained by requiring

$$
\sum _ { \jmath = 1 } ^ { \imath } \widehat { a } _ { \imath \jmath } c _ { \jmath } ^ { q - 1 } = \frac { \widehat { c } _ { \imath } ^ { q } } { q } \qquad \mathrm { f o r } i = 1 , \ldots , s + 1 ,
$$

where $c _ { \imath } = \textstyle \sum _ { \jmath } a _ { \imath \jmath }$ and $\begin{array} { r } { \widehat { c } _ { \iota } = \sum _ { \jmath } \widehat { a } _ { \iota \jmath } } \end{array}$ .For $\imath \approx 1$ ,the relation (6.14) is automatically fulfilled because of $\widehat { a } _ { 1 \jmath } = 0$ For $i > 1$ , it can be satisfied for $q = 1$ (definition

of $\widehat { c } _ { \imath }$ ）， $q = 2$ ,and $q = 3$ . The simplification in the order conditions is similar to that illustrated in Fig.II.5.2. By the definition of the matrix $W$ , the relations of Eq.(6.14) are equivalent to

$$
\sum _ { \jmath = 1 } ^ { \imath } w _ { \imath \jmath } \widehat c _ { \jmath } ^ { q } = q c _ { \imath } ^ { q - 1 } \qquad \mathrm { f o r } i = 1 , \ldots , s + 1 .
$$

This implies further reductions in the set of order conditions. The few remaining ones can be treated in a straight-forward manner. For further details and for the coefficients of the resulting method we refer to the original article of Murua (1995). They have been incorporated in the code PHEM56 (see Sect. VI.7).

Application to Constrained Mechanical Systems. Consider the system

$$
\begin{array} { c } { q ^ { \prime } = u } \\ { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } \\ { 0 = g ( q ) , } \end{array}
$$

where $G ( q ) = g _ { q } ( q )$ . Differentiating the constraint (6.16c) yields

$$
0 = G ( q ) u .
$$

f $M ( q )$ is invertible, the system (6.16a,b,d) is of the form (6.1) with $\boldsymbol { y } = \left( \boldsymbol { q } , \boldsymbol { u } \right)$ and $z = \lambda$ . The assumption (6.3) is equivalent to (1.47).

For this particular system the method (6.5) can be applied as follows: assume that $Q _ { j } , U _ { j } , \Lambda _ { j }$ , and $\tilde { U _ { j } ^ { \prime } } = M ( Q _ { , } ) ^ { - 1 } \big ( f ( Q _ { , } , U _ { , } ) - G ^ { T } ( \bar { Q } _ { , } ) \Lambda _ { , } \big )$ are already given for $j = 1 , \ldots , i - 1$ . We then put

$$
Q _ { \imath } = q _ { 0 } + h \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \imath \jmath } U _ { \jmath } , \qquad U _ { \imath } = u _ { 0 } + h \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \imath \jmath } U _ { \jmath } ^ { \prime } ,
$$

and compute $\Lambda _ { \imath } , U _ { \imath } ^ { \prime }$ from the system

$$
\left( \begin{array} { c c } { M ( Q _ { \imath } ) } & { G ^ { T } ( Q _ { i } ) } \\ { G ( \widehat { Q } _ { i } ) } & { 0 } \end{array} \right) \left( \begin{array} { c } { U _ { \imath } ^ { \prime } } \\ { \Lambda _ { i } } \end{array} \right) = \left( \begin{array} { c } { f ( Q _ { \imath } , U _ { \imath } ) } \\ { R _ { \imath } } \end{array} \right) ,
$$

where $\begin{array} { r } { \widehat { Q } _ { i } = q _ { 0 } + h \sum _ { \jmath = 1 } ^ { \imath } \widehat { a } _ { \imath \jmath } U _ { \jmath } } \end{array}$ and $\begin{array} { r } { R _ { \iota } = - G ( \widehat { Q } _ { \iota } ) \big ( u _ { 0 } + h \sum _ { \jmath = 1 } ^ { i - 1 } \widehat { a } _ { i \jmath } U _ { \jmath } ^ { \prime } \big ) \big / ( h \widehat { a } _ { \iota i } ) } \end{array}$ are known quantities. Hence, only linear systems of type (6.17)'have to be solved. This makes half-explicit methods very attractive for the numerical solution of con-strained mechanical systems. If necessary, this method can be combined with pro-jections as explained in Sect. VI.2, so that also the position constraint is satisfied by the numerical approximation.

We remark that the methods proposed by Arnold (1995) satisfy $\widehat { Q } _ { \imath } = Q _ { \imath + 1 }$ for $i \geq 2$ , so that some $G$ evaluations can be saved in the computation of (6.17).

# Extrapolation Methods

For nonstiff ordinary differential equations,the most eficient extrapolation algorithm is the GBS method (see Sect.II.9). Lubich (1989) extends this method to differential-algebraic equations of index 2.

Consider an initial value $y _ { 0 }$ satisfying $g ( y _ { 0 } ) = 0$ ． Then,an approximation $S _ { h } ( x )$ t0 $y ( x )$ (with $x = x _ { 0 } + 2 m h )$ is defined by

$$
\begin{array} { r l } & { y _ { 1 } = y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) , \qquad g ( y _ { 1 } ) = 0 } \\ & { y _ { i + 1 } = y _ { i - 1 } + 2 h f ( y _ { i } , z _ { i } ) , \qquad g ( y _ { i + 1 } ) = 0 , \qquad i = 1 , \dots , 2 m } \\ & { S _ { h } ( x ) = ( y _ { 2 m - 1 } + 2 y _ { 2 m } + y _ { 2 m + 1 } ) / 4 . } \end{array}
$$

The starting step is identical to the half-explicit Euler method, considered at the beginning of this section. It is implicit in $z _ { 0 }$ and explicit in $y _ { 1 }$ .For the case that Eq.(6.1) in linear in $z$ ,i.e.,

$$
f ( y , z ) = f _ { 0 } ( y ) + f _ { z } ( y ) z ,
$$

we shall show below that the numerical approximations $S _ { h } ( x _ { 0 } + 2 m h )$ and $z _ { 2 m }$ possess an $h ^ { 2 }$ -expansion. Hence,these values can be used as the basis of an extrapolation method. The implementation is completely analogue to that for the GBS method (choice of the step number sequence, order and step size control, dense output, ...). Since the extrapolated values do not satisfy the constraint $g ( y ) = 0$ ， it is recommended to project them onto this manifold (as explained in Sect. VII.2) after every accepted step.

The assumption (6.19) is satisfied for many interesting problems, e.g., for the constrained mechanical system (6.16a,b,d),where $z \approx \lambda$ plays the role of a La-grange multiplier.

Theorem 6.3 (Lubich 1989). Under the assumptions (6.3) and (6.19) the numerical solution of method (6.18) possesses an asymptotic $h ^ { 2 }$ -expansion

$$
\begin{array} { l } { { y _ { 2 m } - y \big ( x _ { 2 m } \big ) = a _ { 2 } \big ( x _ { 2 m } \big ) h ^ { 2 } + a _ { 4 } \big ( x _ { 2 m } \big ) h ^ { 4 } + \cdot \cdot \cdot + a _ { 2 N } \big ( x _ { 2 m } \big ) h ^ { 2 N } + \mathcal { O } \big ( h ^ { 2 N + 2 } \big ) } } \\ { { z _ { 2 m } - z \big ( x _ { 2 m } \big ) = b _ { 2 } \big ( x _ { 2 m } \big ) h ^ { 2 } + b _ { 4 } \big ( x _ { 2 m } \big ) h ^ { 4 } + \cdot \cdot \cdot + b _ { 2 N } \big ( x _ { 2 m } \big ) h ^ { 2 N } + \mathcal { O } \big ( h ^ { 2 N + 2 } \big ) } } \end{array}
$$

and another $h ^ { 2 }$ -expansion for the error of $S _ { h } ( x _ { 2 m } )$

The numerical solution $\{ y _ { \imath } \}$ of method (6.18) lies on the manifold defined by $g ( y ) = 0$ . In order to be able to apply the results and ideas of Sects.II.8 and I.9, we extend the method (6.18) to arbitrary initial values as follows:

$$
\begin{array} { r l } { y _ { 1 } = y _ { 0 } + h f ( y _ { 0 } , z _ { 0 } ) , \quad } & { { } g ( y _ { 1 } ) = g ( y _ { 0 } ) \qquad } \\ { y _ { \ast + 1 } = y _ { \iota - 1 } + 2 h f ( y _ { \iota } , z _ { \iota } ) , \quad } & { { } g ( y _ { \iota + 1 } ) = g ( y _ { \iota - 1 } ) , \qquad i = 1 , \dots , 2 m } \end{array}
$$

We further eliminiate the $z$ -variables: using the identity

$$
g ( y _ { \iota + 1 } ) - g ( y _ { \iota - 1 } ) = \int _ { - 1 } ^ { 1 } g _ { y } \Big ( \frac { y _ { \iota + 1 } + y _ { \iota - 1 } } { 2 } + \sigma \frac { y _ { \iota + 1 } - y _ { \iota - 1 } } { 2 } \Big ) d \sigma \cdot \Big ( \frac { y _ { \iota + 1 } - y _ { \iota - 1 } } { 2 } \Big ) ,
$$

Eq.(6.20b) becomes

$$
0 = \int _ { - 1 } ^ { 1 } g _ { y } \Big ( \frac { y _ { \iota + 1 } + y _ { \iota - 1 } } { 2 } + \sigma h f ( y _ { \iota } , z _ { \iota } ) \Big ) d \sigma \cdot f ( y _ { \iota } , z _ { \iota } ) .
$$

By assumption (6.3) and the Implicit Function Theorem,Eq.(6.21) can be solved for $z _ { \imath }$ as a smooth function of $( y _ { \imath + 1 } + y _ { \imath - 1 } ) / 2 ,$ $y _ { \imath }$ ,and $h$ . Inserted into (6.20b) we obtain a recursion of the type

$$
y _ { \iota + 1 } = y _ { \iota - 1 } + 2 h \Phi \big ( y _ { \iota } , ( y _ { \iota + 1 } + y _ { \iota - 1 } ) / 2 , h \big ) .
$$

The starting step (6.2Oa) can be rewritten in a similar way. We consider the more general system

$$
w = v + h f ( u , z ) , \qquad g ( w ) = g ( v ) ,
$$

where $u , v$ ,and $h$ are given. It can be written in the equivalent form

$$
0 = \int _ { 0 } ^ { 1 } g _ { y } \big ( v + \tau h f ( u , z ) \big ) \ d \tau \cdot f ( u , z ) ,
$$

which yields $z$ as a smooth function of $u , v$ ,and $h$ (again by the Implicit Function Theorem). Hence, the solution of (6.23) can be written as

$$
\boldsymbol { w } = \boldsymbol { v } + h \Phi _ { 0 } ( \boldsymbol { u } , \boldsymbol { v } , h ) ,
$$

and the starting step (6.20a) becomes

$$
y _ { 1 } = y _ { 0 } + h \Phi _ { 0 } ( y _ { 0 } , y _ { 0 } , h ) .
$$

The crucial point of these reformulations is that the two-step method (6.22) and the starting step (6.25) are not only defined on the manifold $g ( y ) = 0$ , but on an open neighbourhood of it. Therefore,the standard ODE theory can be applied. Results for the method(6.22),(6.25) immediately carry over to the method (6.18),because both methods are identical for initial values satisfying $g ( y _ { 0 } ) = 0$ .

Asymptotic Expansion for Symmetric Two-Step Methods. Motivated by the above reformulations we consider the method

$$
\begin{array} { c } { y _ { 1 } = y _ { 0 } + h \Phi _ { 0 } ( y _ { 0 } , y _ { 0 } , h ) } \\ { y _ { \iota + 1 } = y _ { \iota - 1 } + 2 h \Phi \big ( y _ { \iota } , ( y _ { \iota + 1 } + y _ { \iota - 1 } ) / 2 , h \big ) , } \end{array}
$$

where $\Phi _ { 0 }$ and $\Phi$ are arbitrary, smooth increment functions. We assume that $\Phi _ { 0 } ( y , y , 0 ) = \Phi ( y , y , 0 ) = f ( y )$ , so that both methods are consistent with the ordinary differential equation $y ^ { \prime } = f ( y )$ . In order to get an $h ^ { 2 }$ -expansion of the error, the starting step (6.26a) has to be compatible with (6.26b) in the following sense: for arbitrary $u _ { k } , v _ { k }$ , the three values

$$
\begin{array} { l l } { { y _ { 2 k - 1 } : = v _ { k } - h \Phi _ { 0 } ( u _ { k } , v _ { k } , - h ) , \qquad } } & { { y _ { 2 k } : = u _ { k } , } } \\ { { } } & { { } } \\ { { y _ { 2 k + 1 } : = v _ { k } + h \Phi _ { 0 } ( u _ { k } , v _ { k } , h ) } } & { { } } \end{array}
$$

satisfy the recursion (6.26b).

Theorem 6.4. If the method (6.26) satisfes the compatibility condition (6.27), the numerical approximations

$$
y _ { 2 m } , \qquad ( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) / 2
$$

have an asymptotic expansion in even powers of $h$

Proof. Inspired by Steter's proof of Theorem I.9.2 we put $u _ { k } : = y _ { 2 k }$ , and let $v _ { k }$ be the solution of

$$
y _ { 2 k + 1 } : = v _ { k } + h \Phi _ { 0 } ( u _ { k } , v _ { k } , h ) .
$$

We thus get the one-step method in doubled dimension

$$
\begin{array} { r } { \left( \begin{array} { c } { u _ { k + 1 } } \\ { v _ { k + 1 } } \end{array} \right) = \left( \begin{array} { c } { u _ { k } } \\ { v _ { k } } \end{array} \right) + h ^ { * } \left( \begin{array} { c } { \Phi \big ( y _ { 2 k + 1 } , ( u _ { k + 1 } + u _ { k } ) / 2 , h ^ { * } / 2 \big ) } \\ { \frac { 1 } { 2 } \big ( \Phi _ { 0 } ( u _ { k } , v _ { k } , h ^ { * } / 2 ) + \Phi _ { 0 } ( u _ { k + 1 } , v _ { k + 1 } , - h ^ { * } / 2 ) \big ) } \end{array} \right) , } \end{array}
$$

where $h ^ { * } = 2 h$ , and $y _ { 2 k + 1 }$ is given by (6.28). The assumption (6.27) implies that this one-step method is symmetric. Therefore, $y _ { 2 m } = u _ { m }$ and $v _ { m }$ have an asymptotic $h ^ { 2 }$ -expansion (see Theorem II.8.10). From

$$
( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) / 2 = y _ { 2 m } + h \big ( \Phi _ { 0 } ( u _ { m } , v _ { m } , h ) - \Phi _ { 0 } ( u _ { m } , v _ { m } , - h ) \big )
$$

it follows that the same is true for $( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) / 2$

Proof of Theorem 6.3. We have already seen that the method (6.20) can be written in the form (6.26)． All that remains to do is to check the compatibility condition (6.27). By definition of $\Phi _ { 0 } ( u , v , h )$ (see the equivalence of Eqs.(6.23) and (6.25)) we have

$$
\begin{array} { r l } { { y } _ { 2 k - 1 } = { v } _ { k } - h f ( { u } _ { k } , { z } ^ { - } ) , \qquad } & { { g } ( { y } _ { 2 k - 1 } ) = g ( { v } _ { k } ) } \\ { { y } _ { 2 k + 1 } = { v } _ { k } + h f ( { u } _ { k } , { z } ^ { + } ) , \qquad } & { { g } ( { y } _ { 2 k + 1 } ) = g ( { v } _ { k } ) . } \end{array}
$$

Since $f$ is linear in $z$ ,this implies (6.20b) with $z _ { 2 k } = ( z ^ { - } + z ^ { + } ) / 2$ . The asymptotic $h ^ { 2 }$ -expansion of $y _ { 2 m }$ and $S _ { h } ( x _ { 2 m } )$ thus follows from Theorem 6.4. From (6.21) we then see that also $z _ { 2 m }$ has an $h ^ { 2 }$ -expansion. □

# $\beta$ -Blocked Multistep Methods

The convergence analysis of Sect. VII.3 shows that all roots of the $\sigma$ -polynomial of a multistep method must lie inside the unit disc in order to get a convergent method of order $p$ . This is a severe restriction and excludes,for example,all explicit and implicit Adams methods. Arévalo,Fuhrer & Soderlind(1995) suggest a modification which allows the use of “nonstiff” multistep methods. The idea is to treat different parts of the problem by different discretizations.

For the index 2 problem

$$
y ^ { \prime } = f _ { 0 } ( y ) + f _ { z } ( y ) z , \qquad 0 = g ( y ) ,
$$

where $f ( y , z ) = f _ { 0 } ( y ) + f _ { z } ( y ) z$ depends linearly on $z$ , we consider the discretization

$$
\sum _ { \ i = 0 } ^ { k } \alpha _ { \ i } y _ { \boldsymbol n + i } = h \sum _ { \iota = 0 } ^ { k } \beta _ { i } f ( y _ { n + i } , z _ { n + i } ) - h f _ { z } ( y _ { n + k } ) \sum _ { i = 0 } ^ { k } \gamma _ { i } z _ { n + i } ,
$$

with $g ( y _ { n + k } ) = 0$ , and denote the generating polynomials by

$$
\varrho ( \zeta ) = \sum _ { i = 0 } ^ { k } \alpha _ { i } \zeta ^ { \circ } , \qquad \sigma ( \zeta ) = \sum _ { i = 0 } ^ { k } \beta _ { i } \zeta ^ { i } , \qquad \tau ( \zeta ) = \sum _ { i = 0 } ^ { k } \gamma _ { i } \zeta ^ { i } .
$$

Theorem 6.5 (Arévalo,Fuhrer & Soderlind 1996). Let the index 2 problem (6.29) satisfy (6.3). Assume that the multistep method $( \varrho , \sigma )$ is stable and of order $p$ ( $\mathbf { \{ }  p = k$ or $p = k + 1 ,$ ,that $\tau ( \zeta ) = \gamma _ { k } ( \zeta - 1 ) ^ { k }$ , and that all roots of $\sigma ( \zeta ) - \tau ( \zeta )$ lie inside the unit disc $| \zeta | < 1$ . Then the global error satisfies for $x _ { n } - x _ { 0 } \leq C o n s t$

$$
y _ { n } - y ( x _ { n } ) = { \mathcal { O } } ( h ^ { p } ) , \qquad z _ { n } - z ( x _ { n } ) = { \mathcal { O } } ( h ^ { k } ) .
$$

Proof. The special form of $\tau ( \zeta )$ is equivalent to

$$
\sum _ { i = 0 } ^ { k } \gamma _ { i } z ( x _ { n } + i h ) = \mathcal { O } \left( h ^ { k } \right) ,
$$

so that the newly added term in (6.30)is small. Moreover, this term is premultiplied by $f _ { z } ( y _ { n + k } )$ , so that the local error satisfies

$$
\delta y _ { h } ( x ) = \mathcal { O } ( h ^ { k + 1 } ) , \qquad P ( x ) \delta y _ { h } ( x ) = \mathcal { O } ( h ^ { p + 1 } ) ,
$$

where $P ( x )$ is the projector of Definition 4.3.

With these observations in mind, the convergence result is obtained along the lines of the proof of Theorem 3.6. The only difference is that the coefficients $\beta _ { \imath }$ have to be replaced by $\beta _ { i } - \gamma _ { i }$ in Eqs. (3.43) and (3.44). □

In principle,one can take any convergent multistep method $( \varrho , \sigma )$ of order $p = k$ or $p = k + 1$ , and try to optimize the parameter $\gamma _ { k }$ in $\tau ( \zeta )$ in such a way that the roots of $\sigma ( \zeta ) - \tau ( \zeta )$ become small. The result, for the implicit Adams methods, is rather disappointing. Only for $k \le 3$ itis possible to obtain convergent $\beta$ -blocked Adams methods (Arévalo,Fuhrer & Soderlind (1996),see also Exercise 3).

Difference Corrected BDF. Consider the $( k + 1 )$ -step BDF method, defined in Eq. (II.1.22')， and replace $\nabla ^ { k + 1 } y _ { n + 1 }$ by $\nabla ^ { k } f _ { n + 1 }$ . This leads to the so-called difference corrected BDF

$$
\sum _ { j = 1 } ^ { k } \frac { 1 } { j } \nabla ^ { j } y _ { n + 1 } = h \Big ( f _ { n + 1 } - \frac { 1 } { k + 1 } \nabla ^ { k } f _ { n + 1 } \Big ) ,
$$

introduced by Soderlind (1989). Method (6.31) is a $k$ -step method of order $p =$ $k + 1$ .Its $\varrho$ -polynomial is identical to that of the BDF method and $\sigma ( \zeta ) = \zeta ^ { k } -$ $( \zeta - 1 ) ^ { k } / ( k + 1 )$ . With $\tau ( \zeta ) = - ( \zeta - 1 ) ^ { k } / ( k + 1 )$ the difference $\sigma ( \zeta ) - \tau ( \zeta )$ has all roots equal to zero. This is therefore an ideal candidate for a method of type (6.30).

# Exercises

1. Construct allhalf-explicit methods (6.5) of order 3 ( $\cdot r = m = 3$ in Eq.(6.13)) with $s = 3$ stages. You can take $c _ { 2 } , c _ { 3 } , \alpha , \widehat { c } _ { 2 } , \widehat { c } _ { 4 }$ as free parameters. Hint. Start with a classical Runge-Kutta method of order 3 (Exercise 4 of Sect. II.1),and show that the order conditions imply (6.14) for $q = 2$

2. Show that the method (IV.9.15) of Bader & Deuflhard (1983) is of the form (6.26) with

$$
\begin{array} { r l } & { \Phi ( u , v , h ) = f ( u ) - J u + J v } \\ & { \Phi _ { 0 } ( u , v , h ) = ( I - h J ) ^ { - 1 } \big ( f ( u ) - J u + J v \big ) . } \end{array}
$$

Check the assumption (6.27).

3.Let $\left( \varrho _ { k } , \sigma _ { k } \right)$ be the generating polynomials of the $k$ -step implicit Adams methods (Sect. II.1). For $k = 1 , 2 , \ldots , 1 0$ study numerically the function

$$
R _ { k } ( \gamma ) : = \operatorname* { m a x } \left\{ | \zeta ^ { * } | \ ; \ \zeta ^ { * } \ \mathrm { i s \ r o o t \ o f } \ \sigma _ { k } ( \zeta ) - \gamma ( \zeta - 1 ) ^ { k } = 0 \right\} .
$$

For which values of $k$ is it possible to find $\gamma$ with $R _ { k } ( \gamma ) < 1 \gamma$

# VI1.7 Computation of Multibody Mechanisms

Dynamics of multibody systems is of great importance in the fields of robotics,biomechanics,spacecraft control, road and rail vehicle design, and dynamics of machinery.

(W. Schiehlen 1990)

After having seen several different approaches for the numerical solution of constrained mechanical systems,we are interested in their effciency when applied to a concrete situation. We consider two particular multibody mechanisms with constraints, one nonstiff and one stiff. General references for the computation of mechanical systems are Haug (1989) and Roberson & Schwertassek (1988).

# Description of the Model

We first consider “Andrews’ squeezer mechanism", which has become prominent through the work of Giles (1978) and Manning (1981), who promoted it as a test example for numerical codes; see also Ormrod & Andrews (1986). It consists of 7 rigid bodies connected by joints without friction in plane motion. It is represented in Fig.7.1, which we have copied (with permission) from the book of Schiehlen (1990). The numerical constants, also taken from Schiehlen (199O),are displayed in Tables 7.1 and 7.2. The arrows in the right picture of Fig.7.1 indicate the posi-tions of the centres of gravity $C _ { 1 } , \ldots , C _ { 7 }$ . In Table 7.1 the spring coefficient of the spring connecting the point $D$ with $C$ is denoted by $c _ { 0 }$ and the unstretched length is $\ell _ { 0 }$ . We suppose that the mechanism is driven by a motor, located at $O$ ,whose constant drive torque is given by $m o m = 0 . 0 3 3$ . The coordinate origin is the point $O$ in Fig.7.1 and the coordinates of the other fixed points $A , B$ and $C$ are given by

$$
\binom { x a } { y a } = \binom { - 0 . 0 6 9 3 4 } { - 0 . 0 0 2 2 7 } , \binom { x b } { y b } = \binom { - 0 . 0 3 6 3 5 } { 0 . 0 3 2 7 3 } , \binom { x c } { y c } = \binom { 0 . 0 1 4 } { 0 . 0 7 2 } .
$$

Table 7.1. Geometrical parameters  

<table><tr><td>d= 0.028 ea = 0.01421 rr = 0.007 sa = 0.01874 sd= 0.02 tb = 0.00916 ub = 0.00449</td><td>da = 0.0115 zf= 0.02 ra = 0.00092 sb = 0.01043 zt = 0.04 u = 0.04 Co = 4530</td><td>e = 0.02 fa= 0.01421 ss = 0.035 sc = 0.018 ta = 0.02308 ua = 0.01228 lo = 0.07785</td></tr></table>

E.Hairer and G. Wanner, Solving Ordinary Differential Equations I, Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_37, $©$ Springer-Verlag Berlin Heidelberg 2010

![](images/b75eb35d6acff8e322490213750065847dcbedf55c825f227ffbb616fa7da3b2.jpg)  
Fig.7.1. Seven body mechanism (Schiehlen 1990, with permission)

Table 7.2. Parameters of the 7 bodies   

<table><tr><td>No.</td><td>masses m1 to m7</td><td>inertias I1 to I7</td></tr><tr><td>1</td><td>0.04325</td><td>2.194 ·10-6</td></tr><tr><td>2</td><td>0.00365</td><td>4.410:10-7</td></tr><tr><td>3</td><td>0.02373</td><td>5.255·10-6</td></tr><tr><td>4</td><td>0.00706</td><td>5.667 ·10-7</td></tr><tr><td>5</td><td>0.07050</td><td>1.169 .10-5</td></tr><tr><td>6</td><td>0.00706</td><td>5.667 .10-7</td></tr><tr><td>7</td><td>0.05498</td><td>1.912 · 10-5</td></tr></table>

In order to derive the equations of motion we use the angles (see Fig.7.1)

$$
q _ { 1 } = \beta , \quad q _ { 2 } = \Theta , \quad q _ { 3 } = \gamma , \quad q _ { 4 } = \Phi , \quad q _ { 5 } = \delta , \quad q _ { 6 } = \Omega , \quad q _ { 7 } = \varepsilon ,
$$

as position coordinates for the mechanical system. If $( x _ { \ j } , y _ { \ j } )$ are the cartesian coordinates of the centre of gravity $C _ { \jmath }$ $( j = 1 , \ldots , 7 )$ ,the kinetic energy of the multibody system is

$$
T = \sum _ { \jmath = 1 } ^ { 7 } m _ { \jmath } \frac { \dot { x } _ { \jmath } ^ { 2 } + \dot { y } _ { \jmath } ^ { 2 } } { 2 } + \sum _ { \jmath = 1 } ^ { 7 } I _ { \jmath } \frac { \dot { \omega } _ { \jmath } ^ { 2 } } { 2 }
$$

where $\omega _ { \ j }$ is the total angle of rotation of the $j$ th body and $m _ { \jmath } , I _ { j }$ are constants given in Table 7.2. The values of $x _ { j } , y _ { j } , \dot { x } _ { j } ^ { 2 } + \dot { y } _ { j } ^ { 2 }$ and $\dot { \omega } _ { j }$ can be obtained in terms

of (7.2) by simple geometry (see Fig.7.1):

$$
\begin{array} { r l } { \Sigma _ { 1 } : } & { x _ { 1 } = r a \cdot \cos \beta } \\ & { y _ { 1 } = r a \cdot \sin \beta } \\ & { \dot { x } _ { 1 } ^ { 2 } + \dot { y } _ { 1 } ^ { 2 } = r a ^ { 2 } \cdot \dot { \beta } ^ { 2 } } \\ & { \dot { \omega } _ { 1 } = \dot { \beta } } \end{array}
$$

$$
\begin{array} { r l } & { \quad \sum _ { j = 0 } ^ { n } - \lambda _ { j } \lambda _ { j } \lambda _ { j } = \alpha \int _ { 0 } ^ { 1 } - 2 \sin ( \alpha + \beta ) } \\ & { \quad + 2 \sin ( \beta - \gamma ^ { 2 } ) - 2 \sin ( \gamma - \alpha ) \cos ( \alpha + \beta ) \sin ^ { 2 } \lambda _ { j } } \\ & { \quad \le \alpha + \frac { \alpha } { 2 } \left( \frac { \beta } { \lambda _ { j } } - \gamma ^ { 2 } \right) - \sin ( \alpha + \beta ) \cos ( \alpha + \beta ) \left( \frac { \beta } { \lambda _ { j } } - \gamma ^ { 2 } \right) } \\ & { \quad - \sin ( \alpha + \beta ) \cos ( \alpha + \gamma ) \sin ( \alpha + \gamma ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \frac { \beta } { \lambda _ { j } } - \gamma ^ { 2 } \right) } \\ & { \quad \quad - \sin ( \alpha + \beta ) \cos ( \alpha + \gamma ) \sin ( \alpha ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \frac { \beta } { \lambda _ { j } } - \gamma ^ { 2 } \right) } \\ & { \quad \le \alpha - \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) } \\ & { \quad \le \alpha - \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \alpha ) } \\ & { \quad \le \alpha - \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \beta ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \beta ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \beta ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \beta ) } \\ & { \quad \le \alpha + \frac { \alpha + \beta } { 2 } \left( \alpha + \beta \right) \cos ( \alpha + \gamma ) \sin ( \beta ) \sin ( \gamma ) \le \alpha \beta \le \alpha \beta \le \alpha \beta \le \alpha \beta \le \alpha \beta } \\ &  \quad \le \alpha + \beta \le \alpha \le \alpha \le \beta \le \alpha \le \alpha \le \alpha \beta \le \alpha \le \alpha \le \beta \le  \end{array}
$$$$
\begin{array} { r l } { \varepsilon _ { 1 } ^ { \prime \prime } } & { = \varepsilon _ { 2 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } } \\ & { \quad + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } } \\ & { \quad - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } } \\ & { \quad - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } } \\ { \varepsilon _ { 1 } ^ { \prime \prime \prime } } & { = \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } } \\ & { \quad - \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } } \\ & { \quad + \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } - \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _ { 3 } ^ { \prime \prime } } \\ &  \quad + \varepsilon _ { 3 } ^ { \prime \prime } + \varepsilon _   \end{array}
$$

The potential energy ofthe system is due to the motor at the origin and to the spring connecting the point $D$ with $C$ . By Hooke's law it is

$$
U = - m o m \cdot \beta + c _ { 0 } { \frac { ( \ell - \ell _ { 0 } ) ^ { 2 } } { 2 } } ,
$$

where $\ell$ is the distance between $D$ and $C$ , namely

$$
\begin{array} { r } { \ell = \sqrt { ( x d - x c ) ^ { 2 } + ( y d - y c ) ^ { 2 } } } \\ { x d = x b + s c \cdot \sin \gamma + s d \cdot \cos \gamma } \\ { y d = y b - s c \cdot \cos \gamma + s d \cdot \sin \gamma . } \end{array}
$$

Finally,we have to formulate the algebraic constraints. The mechanism contains three loops. The first loop connects $O$ with $B$ via $\bar { K _ { 1 } } , K _ { 2 } , \bar { K _ { 3 } }$ ; the other two loops connect $O$ with $A$ , one via $K _ { 1 } , K _ { 2 } , K _ { 4 } , K _ { 5 }$ , the other via $K _ { 1 } , K _ { 2 } , K _ { 6 } , K _ { 7 }$ .For each loop we get two algebraic conditions:

$$
\begin{array} { r l } & { r r \cdot \cos \beta - d \cdot \cos ( \beta + \Theta ) - s s \cdot \sin \gamma = x b } \\ & { r r \cdot \sin \beta - d \cdot \sin ( \beta + \Theta ) + s s \cdot \cos \gamma = y b } \\ & { r r \cdot \cos \beta - d \cdot \cos ( \beta + \Theta ) - e \cdot \sin ( \Phi + \delta ) - z t \cdot \cos \delta = x a } \\ & { r r \cdot \sin \beta - d \cdot \sin ( \beta + \Theta ) + e \cdot \cos ( \Phi + \delta ) - z t \cdot \sin \delta = y a } \\ & { r r \cdot \cos \beta - d \cdot \cos ( \beta + \Theta ) - z f \cdot \cos ( \Omega + \varepsilon ) - u \cdot \sin \varepsilon = x a } \\ & { r r \cdot \sin \beta - d \cdot \sin ( \beta + \Theta ) - z f \cdot \sin ( \Omega + \varepsilon ) + u \cdot \cos \varepsilon = y a . } \end{array}
$$

With the position coordinates $q$ from (7.2) the equations (7.5) represent the constraint $g ( q ) = 0$ where $g : \mathbb { R } ^ { 7 }  \mathbb { R } ^ { 6 }$ . Together with the kinetic energy $T$ of (7.3) the potential energy $U$ of (7.4) and $L = T - U - \lambda _ { 1 } g _ { 1 } - . . . - \lambda _ { 6 } g _ { 6 }$ the equations of motion (1.46) are fully determined.

# Fortran Subroutines

For the reader's convenience we include the essential parts of the FORTRAN subroutines describing the differential-algebraic problem. The equations of motion are of the form

$$
\begin{array} { r } { M ( q ) \ddot { q } = f ( q , \dot { q } ) - G ^ { T } ( q ) \lambda } \\ { 0 = g ( q ) \qquad } \end{array}
$$

where $q \in \mathbb { R } ^ { 7 }$ is the vector defined in (7.2) and $\lambda \in \mathbb { R } ^ { 6 }$ . In the following descrip-tion the variables $\mathbb { Q } \left( { \mathrm { 1 } } \right) , \ldots , \mathbb { Q } \left( { \mathrm { 7 } } \right)$ correspond to $\beta , \ldots , \varepsilon$ (exactly as in (7.2)) and $\mathbb { Q P } ( 1 ) , \dots , \mathbb { Q P } ( 7 )$ to their derivatives ${ \dot { \beta } } , \dots , { \dot { \varepsilon } }$ . In all subroutines we have used the abbreviations

$$
\begin{array} { r } { \begin{array} { l l l } { \mathrm { S I B E } } & { = } & { \mathrm { S I N } \left( \mathbb { Q } \left( \mathbf { 1 } \right) \right) } \\ { \mathrm { S I T H } } & { = } & { \mathrm { S I N } \left( \mathbb { Q } \left( 2 \right) \right) } \\ { \mathrm { S I G A } } & { = } & { \mathrm { S I N } \left( \mathbb { Q } \left( 3 \right) \right) } \end{array} } \end{array}
$$

$$
\begin{array} { r } { \begin{array} { l l } { \mathtt { C O B E } = \mathtt { C O S } } & { ( \mathtt { Q } ( \mathtt { 1 } ) ) } \\ { \mathtt { C O T H } = \mathtt { C O S } } & { ( \mathtt { Q } ( \mathtt { 2 } ) ) } \\ { \mathtt { C O G A } = \mathtt { C O S } } & { ( \mathtt { Q } ( \mathtt { 3 } ) ) } \end{array} } \end{array}
$$

<table><tr><td>SIPH = SIN （Q(4))</td></tr><tr><td>COPH = cos （Q(4)) SIDE = SIN (Q(5)) CODE = Cos</td></tr><tr><td>(Q(5)) SIOM = SIN (Q(6)) COOM = cos (Q(6))</td></tr><tr><td>SIEP 1 SIN (Q(7)) COEP = cos (Q(7))</td></tr><tr><td></td></tr><tr><td>SIBETH = SIN (Q(1)+Q(2)) COBETH = cos (Q(1)+Q(2)) SIPHDE Ⅱ SIN (Q(4)+Q(5)) COPHDE = Cos (Q(4)+Q(5))</td></tr><tr><td>SIOMEP = SIN (Q(6)+Q(7)) COOMEP = Cos (Q(6)+Q(7))</td></tr><tr><td></td></tr><tr><td>BEP QP(1) = THP = QP(2)</td></tr><tr><td>PHP = QP(4) DEP = QP(5)</td></tr><tr><td>OMP = QP(6) EPP Ⅱ QP(7)</td></tr></table>

The remaining parameters ${ \mathrm { X A } } , { \mathrm { Y A } } , \ldots , { \mathrm { D } } , { \mathrm { D A } } , { \mathrm { E } } , { \mathrm { E A } } , \ldots , { \mathrm { M 1 } } , { \mathrm { I 1 } } , { \mathrm { M 2 } } , \ldots .$ are those of（7.1） and Tables 7.1 and 7.2. They usually reside in a COMMON block. The elements of $M ( q )$ in (7.6) are given by

$$
{ m _ { \iota \jmath } } = \frac { { \partial ^ { 2 } } L } { { \partial { \dot { q } } _ { \imath } \partial { \dot { q } } _ { \jmath } } } = \frac { { \partial ^ { 2 } } T } { { \partial { \dot { q } } _ { i } \partial { \dot { q } } _ { \jmath } } } .
$$

This matrix is symmetric and (due to the special arrangement of the coordinates) tridiagonal. The non-zero elements (on and below the diagonal) are

$$
\begin{array} { r l } { \mathrm { \mathfrak { M } ( \pm , \pm ) } } &  = \mathrm  \mathfrak { M } 1 + \mathord { \mathfrak { R } } / \mathrm { A } + \mathrm { e } + \mathrm { \mathfrak { Z } } + \mathrm { \ b } / \mathrm { \mathfrak { A } } / \mathrm { s } + \mathrm { e } \left( \mathrm { \mathrm { R } } \mathrm { \mathtt { R } } \mathrm { \mathtt { A } } \ast \mathrm { \overline { { e } } \mathrm { \Omega } / \mathrm { H } + \mathrm { D } \mathrm { A } \ast \mathrm { c } \mathrm { \Omega } \right) \mathrm { \Omega } + \mathrm { \ I } \mathrm { \mathtt { I } } + \mathrm { \Omega } \mathrm { \Omega } } \\ { \mathrm { \mathfrak { M } ( 2 , \pm ) } } &  = \mathrm { \mathfrak { M } 2 + \mathrm { e } \left( \mathrm { D } \mathrm { A } \ast \mathrm { e } + \mathrm { \ r { Z } } - \mathrm { D } \mathrm { A } \ast \mathrm { R } \mathrm { \mathtt { A } } \ast \mathrm { C } \mathrm { \Omega } \right) \mathrm { \textnormal { \iota } } + \mathrm { \ r } \mathrm { \mathfrak { R } } \mathrm { \mathrm { A } } \ast \mathrm { c } \mathrm { \Omega } \mathrm { \mathrm { T } } \mathrm { H } + \mathrm { D } \mathrm { A } \ast \mathrm { e } + 2 \mathrm { \ r { Z } } \mathrm { \textnormal { \iota } } } \\ { \mathrm { \mathfrak { M } ( 3 , \mathtt { \mathtt { J } } ) } } &  = \mathrm { \mathfrak { M } 2 + \mathrm { e } \mathrm { \Omega } / \mathrm { B } \mathrm { \ r } \mathrm { \mathfrak { A } } \ast \mathrm { \mathrm { \Gamma } } _ { 2 } + \mathrm { \ r } \mathrm { \mathfrak { Z } } } \\ { \mathrm { \mathfrak { M } ( 4 , \mathtt { J } ) } } &  = \mathrm { \mathfrak { M } 4 \mathrm { e } \left( \mathrm { E } \mathrm { B } \ast \mathrm { e } + \mathrm { \ r { Z } } + \mathrm { S } \mathrm { B } \ast \mathrm { e } + 2 \mathrm { \iota } \mathfrak { J } \mathrm { \Phi } } \\ { \mathrm { \mathfrak { M } ( 5 , \pm ) } } &  = \mathrm { \mathfrak { M } 4 \mathrm { e } \left( \mathrm { \Gamma } \mathrm { } \mathrm { \overline { { E } } } \mathrm { A } \right) \ast \mathrm { e } \mathrm { \Omega } + \mathrm { \ r } \mathrm { \mathfrak { A } } \mathrm { \ r } \mathrm { E } \mathrm { H } \right) \mathrm { \Omega } + \mathrm { \ r } \mathrm { \mathfrak { A } } } \\ { \mathrm { \mathfrak { M } ( 5 , \pm ) } } &  = \mathrm  \mathfrak  M  \end{array}
$$

The $i$ th component of the function $f$ in (7.6) is defined by

$$
f _ { \imath } ( q , \dot { q } ) = \frac { \partial ( T - U ) } { \partial q _ { i } } - \sum _ { j = 1 } ^ { 7 } \frac { \partial ^ { 2 } ( T - U ) } { \partial \dot { q } _ { i } \partial q _ { j } } \cdot \dot { q } _ { \jmath } .
$$

Written as FORTRAN statements we have

$$
\begin{array} { r l } { \mathrm { Y D } } & { = \mathrm { S D } \ast \mathrm { C O G A } \ + \mathrm { \Lambda } \leq \mathrm { C G } \ast \mathrm { S T G A } \ + \ \mathrm { Y B } } \\ { \mathrm { Y D } } & { = \ \mathrm { S D } \ast \mathrm { S I } \mathrm { C G } \ - \ \mathrm { S C } \ast \mathrm { C O G A } \ + \ \mathrm { Y B } } \\ { \mathrm { L A H G } } & { = \mathrm { S D } \mathrm { H P T } \ \left( \ \mathrm { ( 1 0 , 1 - X , C ) } \ast \neq 2 \ \ast \ \mathrm { ( 1 D D - Y C ) } \ast \ast \neq 2 \right) } \\ { \mathrm { F O R } } & { = - \ \mathrm { C O } \ \ast \ \mathrm { ( 1 . A R G } \ - \ \mathrm { L O ) } / \ \mathrm { L A H G } } \\ { \mathrm { F X } } & { = \mathrm { F 0 R C E } \ \ast \ \mathrm { ( 1 . D N - X , C ) } } \\ { \mathrm { F T } } & { = \mathrm { F 0 R C E } \ \ast \ \mathrm { ( 1 . 0 , 1 - Y . C ) } } \\ { \mathrm { F T } } & { = \mathrm { F 0 R C H } \ \ast \ \mathrm { H . \Lambda } \ } \\ { \mathrm { P ( 2 ) } } & { = \ \mathrm { H 0 H } \ast \ \mathrm { H . \Lambda } \ \mathrm { H . A } \ast \mathrm { B R } + \mathrm { H . F A } ^ { \ast } \mathrm { H F P } \ast \ \mathrm { ( 7 H P + 2 4 8 B E P ) } \ast \mathrm { S I T H } } \\ { \mathrm { P ( 2 ) } } & { = \ \mathrm { H 2 } \ast \mathrm { H . N } \ast \mathrm { H x } \mathrm { H x } \mathrm { H . W } \mathrm { P y } + 2 \mathrm { S 5 } \mathrm { T } \mathrm { T } \mathrm { H } } \\ { \mathrm { P ( 3 ) } } & { = \mathrm { Y U K } \ast \mathrm { ( 5 0 . 6 A ) } \ast \ \mathrm { S D } \ast \mathrm { C O } \mathrm { F X } } \\ { \mathrm { F ( 6 ) } } & { = \mathrm { H . U 4 } \ast \mathrm { ( 7 4 . 7 6 \times 2 8 ) } \ast \mathrm { P H } \ast \mathrm { ( 7 R P + 2 4 8 B E ) } \times \mathrm { C O P H } } \\ { \mathrm { F ( 6 ) } } & { = \ \mathrm { H . W } \ast \mathrm { H . ( 7 . 6 \times 1 0 . 7 6 \times 2 0 . 4 8 ) } } \\ { \mathrm { F ( 7 ) } } & { = \mathrm { H . W } \ast \mathrm { H . W } \mathrm { P y } + \mathrm { F P } \ast \mathrm { C O } \mathrm { H . W } } \\  \mathrm { F ( 7 ) }  \end{array}
$$

The algebraic constraints $g ( q ) = 0$ are given by the following six equations (see (7.5))

G(1) = RR\*COBE - D\*COBETH - SS\*SIGA - XB G(2) = RR\*SIBE - D\*SIBETH + SS\*COGA - YB G(3) RR\*COBE - D\*COBETH - E\*SIPHDE - ZT\*CODE - XA G(4) RR\*SIBE - D\*SIBETH + E\*COPHDE - ZT\*SIDE - YA G(5) RR\*COBE - D\*COBETH - ZF\*COOMEP - U\*SIEP - XA G(6) = RR\*SIBE - D\*SIBETH - ZF\*SIOMEP + U\*COEP - YA

And here is the Jacobian matrix $G ( q ) = g _ { q } ( q )$ . The non-zero entries of this $6 \times 7$ array are

$ \begin{array} { r l } { \mathbb { G } { \mathrm { q } } \left( 1 , 1 \right) } & { = - \mathbb { R } \mathbb { R } \mathbb { * } \mathbb { S } \mathbb { I } \mathbb { B } \mathbb { E } + { \mathrm { D } } { \mathrm { * } } { \mathrm { S I B E } } \mathbb { T } \mathbb { H } } \\ { \mathbb { G } { \mathrm { q } } \left( 1 , 2 \right) } & { = { \mathrm { D } } { \mathrm { * } } { \mathrm { S I B E T H } } } \\ { \mathbb { G } { \mathrm { q } } \left( 1 , 3 \right) } & { = - \ \mathbb { S } { \mathrm { s } } { \mathrm { c o p t a k } } } \\ { \mathbb { G } { \mathrm { q } } \left( 2 , 1 \right) } & { = { \mathrm { R } } \mathbb { R } { \mathrm { * } } \mathbb { C } { \mathrm { 0 } } \mathbb { B } \mathbb { E } - { \mathrm { D } } { \mathrm { * } } { \mathrm { C o B E T H } } } \\ { \mathbb { G } { \mathrm { q } } \left( 2 , 2 \right) } & { = - \ { \mathrm { D } } { \mathrm { * } } { \mathrm { C o B E T H } } } \\ { \mathbb { G } { \mathrm { q } } \left( 2 , 3 \right) } & { = - \ { \mathrm { S } } { \mathrm { S } } { \mathrm { * } } { \mathrm { S i G } } { \mathrm { A } } } \\ { \mathbb { G } { \mathrm { q } } \left( 3 , 1 \right) } & { = - \ { \mathrm { R } } { \mathrm { t } } { \mathrm { R } } { \mathrm { * } } { \mathrm { S i T B E } } + { \mathrm { D } } { \mathrm { * } } { \mathrm { S I B E T H } } } \\ { \mathbb { G } { \mathrm { q } } \left( 3 , 2 \right) } & { = { \mathrm { D } } { \mathrm { * } } { \mathrm { S I B E T H } } } \\ { \mathbb { G } { \mathrm { q } } \left( 3 , 4 \right) } & { = - \ { \mathrm { E } } { \mathrm { * } } { \mathrm { C o p t h } } { \mathrm { D } } \mathbb { E } } \\ { \mathbb { G } { \mathrm { q } } \left( 4 , 1 \right) } & { = { \mathrm { R } } { \mathrm { q } } { \mathrm { s } } { \mathrm { C o p t h } } { \mathrm { E } } } \\ { \mathbb { G } { \mathrm { q } } \left( 4 , 1 \right) } & { = { \mathrm { R } } { \mathrm { k } } { \mathrm { ( C o p E ~ - ~ } } { \mathrm { D } } { \mathrm { * } } { \mathrm { C o B E T H } } } \end \end{array}$ GQ(4,2) = - D\*C0BETH GQ(4,4) = - E\*SIPHDE GQ(4,5) = - E\*SIPHDE - ZT\*CODE GQ(5,1) = - RR\*SIBE + D\*SIBETH GQ(5,2) = D\*SIBETH GQ(5,6) = ZF\*SIOMEP GQ(5,7) = ZF\*SIOMEP - U\*COEP GQ(6,1） = RR\*COBE - D\*COBETH GQ(6,2) = - D\*C0BETH GQ(6,6) = - ZF\*C0OMEP GQ(6,7) = - ZF\*COOMEP - U\*SIEP

If we apply a numerical method to the index 1 formulation of the system, we also need the expression $g _ { q q } ( q ) ( \dot { q } , \dot { q } )$ . It is given by

GQQ(1) = - RR\*COBE\*V(1)\*\*2 + D\*COBETH\*(V(1)+V(2))\*\*2 + + $\mathtt { S S } * \mathtt { S I G A } * \mathtt { V } \left( 3 \right) * * 2$   
GQQ $\begin{array} { r l r } { \mathrm { ( 2 ) } } & { { } = } & { - \mathrm { \nabla { R R } } \ast \mathrm { S I B E } \ast \mathrm { V \left( 1 \right) } \ast \ast 2 \mathrm { \nabla { + } } \mathrm { \ D } \ast \mathrm { S I B E T H } \ast \left( \mathrm { V \left( 1 \right) } \ast \mathrm { V \left( 2 \right) } \right) \ast \ast 2 \mathrm { \nabla { + } } \mathrm { R e } \cdot \left( \mathrm { V \left( 1 \right) } \ast \mathrm { V \left( 1 \right) } \ast \mathrm { V \left( 2 \right) } \right) } \end{array} .$ · + $\mathtt { S S } * \mathtt { C O G A } * \mathtt { V } \left( 3 \right) * * 2$   
GQQ(3)= - $\mathrm { R R ^ { * } C O B E ^ { * } V } \left( 1 \right) * * 2 \ + \ \mathrm { D ^ { * } C O B E T H ^ { * } } \left( \mathrm { V } \left( 1 \right) + \mathrm { V } \left( 2 \right) \right) * * 2$ + + $\mathrm { E * S I P H D E * \left( V \left( 4 \right) + V \left( 5 \right) \right) * * 2 \ + \ Z T * C O D E * V \left( 5 \right) * * 2 }$ GQQ(4)= - $\mathrm { R R } { * } \mathrm { S I B E } { * } \mathrm { V } \left( \mathrm { 1 } \right) { * } { * } { 2 } \ \mathrm { ~ + ~ } \mathrm { D } { * } \mathrm { S I B E T H } { * } \left( \mathrm { V } \left( \mathrm { 1 } \right) { + } \mathrm { V } \left( \mathrm { 2 } \right) \right) { * } { * } { \mathrm { ~ + ~ } }  \mathrm { ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ } \mathrm { V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V } \mathrm { ~ - ~ V }$ 2- + $\mathrm { E * C O P H D E * \left( V \left( 4 \right) + V \left( 5 \right) \right) * * 2 \ + \ Z T * S I D E * V \left( 5 \right) }$ \*\*2 GQQ(5） = $\begin{array} { r l r } { - } & { { } \mathrm { R R } { * } \mathrm { C O B E } { * } \mathrm { V } ( 1 ) { * * } 2 } & { + } & { { } \mathrm { D } { * } \mathrm { C O B E T H } { * } ( \mathrm { V } ( 1 ) { + } \mathrm { V } ( 2 ) \mathrm { T } { - } \mathrm { E T } { * } \mathrm { A } ( \mathrm { V } ( 1 ) { + } \mathrm { V } ( 1 ) { + } \mathrm { V } ( 2 ) ) } \end{array}$ \*\*2 + + $\mathrm { { Z F ^ { * } C O M E P * \left( V \left( 6 \right) + V \left( 7 \right) \right) * * 2 \ + \ U * S I E P * V \left( 7 \right) } }$ \*\*2 GQQ(6) = $\begin{array} { r l r } { - } & { { } \mathrm { R R ^ { * } S T B E ^ { * } V } \left( 1 \right) * * 2 } & { + } & { { \mathrm { D ^ { * } S T B E T H ^ { * } } } \left( \mathrm { V } \left( 1 \right) + \mathrm { V } \left( 2 \right) \right) } \end{array}$ \*\*2+ + ZF\*SI0MEP\*(V(6)+V(7))\*\*2 - U\*C0EP\*V(7)\*\*2

# Computation of Consistent Initial Values

We first compute a solution of $g ( q ) = 0$ . Since $g$ consists of 6 equations in 7 unknowns we can fix one of them arbitrarily, say $\Theta ( 0 ) = 0$ , and compute the remaining coordinates by Newton iterations. This gives

$\beta ( 0 ) = - 0 . 0 6 1 7 1 3 8 9 0 0 1 4 2 7 6 4 4 9 6 3 5 8 9 4 8 4 5 8 0 0 1$ Q(O)= 0.455279819163070380255912382449 Φ(0) = 0.222668390165885884674473185609 8(0) = 0.487364979543842550225598953530 Ω(0) = -0.222668390165885884674473185609 $\varepsilon ( 0 ) = 1 . 2 3 0 5 4 7 4 4 4 5 4 9 8 2 1 1 9 2 4 9 7 3 5 0 1 5 5 6 8 .$

![](images/f2ccc2acc7fbaec4fde51ded20a75e8ec38d1b47ccd0acfb4a87754c5eedd9ba.jpg)  
Fig.7.2. Solution of 7 body mechanism

The condition $G ( q ) \dot { q } = 0$ is satisfied if we put

$$
\dot { \beta } ( 0 ) = \dot { \Theta } ( 0 ) = \dot { \gamma } ( 0 ) = \dot { \Phi } ( 0 ) = \dot { \delta } ( 0 ) = \dot { \Omega } ( 0 ) = \dot { \varepsilon } ( 0 ) = 0 .
$$

The values of $\lambda ( 0 )$ and ${ \ddot { q } } ( 0 )$ are then uniquely determined by (7.6a) and the twice differentiated constraint $0 = g _ { q q } ( q ) ( \dot { q } , \dot { q } ) + G ( q ) \ddot { q }$ . We just have to solve a linear system with the matrix

$$
\left( \begin{array} { c c } { { M ( q ) } } & { { G ^ { T } ( q ) } } \\ { { G ( q ) } } & { { 0 } } \end{array} \right) .
$$

Observe that $g _ { q q }$ need not be evaluated, because $\dot { q } ( 0 ) = 0$ . Due to the choice $\Theta ( 0 ) = 0$ most components of $\lambda ( 0 )$ and $\ddot { q } ( 0 )$ vanish. Only the first two of these are different from zero and given by

$$
\begin{array} { r l } & { \ddot { \beta } ( 0 ) = 1 4 2 2 2 . 4 4 3 9 1 9 9 5 4 1 1 3 8 7 0 5 9 1 1 6 2 5 8 8 7 } \\ & { \ddot { \Theta } ( 0 ) = - 1 0 6 6 6 . 8 3 2 9 3 9 9 6 5 5 8 5 4 0 2 9 4 3 3 7 1 9 4 1 5 } \\ & { \lambda _ { \mathbf { 1 } } ( 0 ) = 9 8 . 5 6 6 8 7 0 3 9 6 2 4 1 0 8 9 6 0 5 7 6 5 4 9 8 2 1 7 0 } \\ & { \lambda _ { \mathbf { 2 } } ( 0 ) = - 6 . 1 2 2 6 8 8 3 4 4 2 5 5 6 6 2 6 5 5 0 3 1 1 4 3 9 3 1 2 2 . } \end{array}
$$

The solution of this seven body mechanism is plotted (mod $2 \pi$ ) in Fig.7.2 for $0 \leq t \leq 0 . 0 3$

# Numerical Computations

We first transform (7.6) into a first order system by introducing the new variable $v = { \dot { q } }$ . Our codes apply only to problems where the derivative is multiplied by a constant matrix. We therefore also consider $w = \ddot { q }$ as a variable so that (7.6a) becomes an algebraic relation. The various formulations of the problem,as discussed in Sect. VII.1, are now as follows:

Index 3 Formulation. With $v = { \dot { q } }$ and $w = \ddot { q }$ the system (7.6) can be writen as

$$
\begin{array} { l } { \dot { q } = v } \\ { \dot { v } = w } \\ { 0 = M ( q ) w - f ( q , v ) + G ^ { T } ( q ) \lambda } \\ { 0 = g ( q ) . } \end{array}
$$

Index 2 Formulation. If we differentiate $0 = g ( q )$ once and replace (7.11d) by

$$
0 = G ( q ) v ,
$$

we get an index 2 problem which is mathematically equivalent to (7.6).

Index 1 Formulation. One more differentiation of (7.11e) yields

$$
0 = g _ { q q } ( q ) ( v , v ) + G ( q ) w ,
$$

so that $( 7 . 1 1 { \mathrm { a } } , { \mathrm { b } } , { \mathrm { c } } , { \mathrm { f } } )$ constitutes an index 1 problem.

We have applied several codes with many different tolerances between $1 0 ^ { - 2 }$ and $1 0 ^ { - 1 0 }$ to these formulations. The results are given in Fig.7.3. We have plotted the computing time (on a SUN Spark 2O workstation) against the error of the $( q , v ) \cdot$ components at $x _ { \mathrm { e n d } } = 0 . 0 3$ (in double logarithmic scale).

![](images/96ec3de1a960722e255b5798af0249cdcbd6393cc28929c19622d12e5f687de7.jpg)  
Fig.7.3.Work-precision diagram

Explicit Runge-Kutta Methods. The index 1 formulation allows us to apply explicit methods such as DOPRI5 or DOP853 of Volume I. For this we have Written a function subroutine which solves in each call the linear system (7.11c,f) for $w$ and $\lambda$ and inserts the result into (7.11a,b). Since there is no stiffness in the obtained differential equation for $( q , v )$ , it is not surprising that here the explicit codes work very efficiently (Fig. 7.3).

In order to avoid the drift-off phenomenon (see Sect. VI.2), we have also combined this method with projections onto the solution manifold. This can be implemented conveniently with help of the subroutine SOLOUT,which is called by DOPRI5 after every successful step (set IRTRN $\ r = 2$ in order to indicate that the numerical approximation has been altered). The full projection (on position and velocity level, (7.11d) and (7.11e)) is slightly more expensive than velocity stabilization alone (denoted by DOPRI5_VEL in Fig.7.3） and does not give improved results. The first picture of Fig.7.4 shows the results of the three different implementations: the ‘standard’ approach is without any projection,‘velocity’ means that we perform only velocity stabilization,and ‘position’ indicated that we do consecutive projections on the position and velocity level. We see that velocity stabilization gives the best results concerning achieved accuracy and computing time.

Half-Explicit Methods. These methods (discussed in Sect. VII.6) are especially adapted to the numerical solution of (nonstiff) constrained mechanical systems. Only linear systems with the matrix (7.9) have to be solved, otherwise the methods are explicit. Since they are applied directly to the index 2 formulation, the velocity constraint (7.11e) is automatically satisfied, and no subroutine for the computation of $g _ { q q } ( q ) ( v , v )$ is required.

The extrapolation code MEXX of Lubich (1989) (see also Lubich, Nowak, Poehle & Engstler 1992) implements the half-explicit mid-point rule (6.18). The existence of an $h ^ { 2 }$ -expansion (Theorem 6.3) justifies extrapolation and thus yields methods of arbitrarily high order. It is not surprising that this code gives excellent results for high precision computations.

The first code implementing half-explicit Runge-Kutta methods is HEM5 of Brasey (1994). It has been modified and improved by Arnold (1995, code HEX5) and Murua (1995,code PHEM56). We have also included the results of the latter code (Fig.7.3). It is slightly less effcient than DOPRI5_VEL in this particular example, because the evaluation of $g _ { q q } ( q ) ( v , v )$ is cheap. Arnold (1995） and Murua (1995) report about experiments (with expensive $g _ { q q } ( q ) ( v , v ) )$ ，where the half-explicit methods are superiour to explicit Runge-Kutta methods with velocity projection.

BDF. The famous code DASSL of Petzold (1982), see also Brenan, Campbell & Petzold (1989), is a realization of the BDF multistep formulas. It is written for problems of the general form $F ( u , u ^ { \prime } , x ) { = } 0$ , so that it is not necessary to introduce $\ddot { q }$ of (7.6) as new variable. We applied it using default values for all parameters except for the scaling of the error estimation. We put $\mathrm { I N F O } ( 2 ) { = } 1$ and

$$
\mathrm { A T O L ( I ) } = \mathrm { R T O L ( I ) } = \left\{ \begin{array} { l l } { { T o l } } & { { \mathrm { f o r I = 1 , \ldots , 1 4 , } } } \\ { { \mathrm { 1 . 0 D 0 } } } & { { \mathrm { f o r I \geq 1 5 , } } } \end{array} \right.
$$

which means that we control the accuracy for $q$ and $v$ , but not for the Lagrange multipliers $\lambda$ . In the comparisons of Fig.7.3 (index 2 formulatin) and Fig.7.4 we used the full Jacobian of the problem, obtained by numerical differentiation. This turned out to be more eficient than providing an analytic approximation, where the derivatives of $f , M$ and $G$ are neglected.

![](images/fcfde105d43e3c313b38836b53a142d32ecbd7d9902c5e9603bd06f23bd61fa7.jpg)  
Fig. 7.4. Work-precision diagram

Implicit Runge-Kutta Methods. Our code RADAU5 is written for problems of the form $B y ^ { \prime } = f ( x , y )$ with constant, possibly singular matrix $B$ . It can therefore be applied to all three of the above formulations. Convergence is guaranteed by Theorem VI.1.1 for the index 1 formulation,by Theorems 4.5 and 4.6 for the index 2 formulation,and by the results of HLR89 for the index 3 case. However, the higher the index, the more difficult is it to solve the nonlinear Runge-Kutta equa-tions. We have applied the code with the options $\mathrm { I W O R K } ( 5 ) = 1 4$ ， $\mathrm { I W O R K } ( 6 ) = 0$ and $\mathrm { I W O R K } ( 7 ) = 1 3$ $( \mathrm { I W O R K } ( 5 ) = 7$ and $\mathrm { I W O R K } ( 6 ) = 7 $ for the index 3 formulation),so that the acceleration $w$ and the Lagrange multiplier $\lambda$ are scaled by $h ^ { 2 }$ in the error estimation. This guarantees the convergence of the simplified Newton iterations (see HLR89, Chapter 7 for a justification). Furthermore,we have exploited the special structure $\dot { q } = v , \dot { v } = w$ of our system by setting IWORK(9) $= 1 4$ and $\mathrm { I W O R K } ( 1 0 ) = 7$ . This speeds up the computation of the arising linear systems. The results are given in Fig.7.3 (index 2 formulation) and in the lower left picture of Fig.7.3 for all three formulations of the problem. We have used an analytical approximation to the Jacobian (neglecting the derivatives of $f$ ， $M$ and $G$ ) and did not apply any projection onto the solution manifold.

Savings in Linear Algebra. If the problem is nonstiff, one can use a reduced Jacobian for the solution of the nonlinear Runge-Kutta equations. Neglecting the derivatives of $f , M$ and $G$ (what we have done for the above calculations), we are led to linear systems of the form (in the index 2 case)

$$
\left( \begin{array} { c c c c } { - \alpha I } & { I } & { 0 } & { 0 } \\ { 0 } & { - \alpha I } & { I } & { 0 } \\ { 0 } & { 0 } & { M } & { G ^ { T } } \\ { 0 } & { G } & { 0 } & { 0 } \end{array} \right) \left( \begin{array} { c } { \Delta q } \\ { \Delta v } \\ { \Delta w } \\ { \Delta \lambda } \end{array} \right) = \left( \begin{array} { c } { a } \\ { b } \\ { c } \\ { d } \end{array} \right)
$$

where $\alpha = ( h \gamma ) ^ { - 1 }$ ， $h$ the step size and $\gamma$ an eigenvalue of the Runge-Kutta matrix. The evaluation of the matrix in (7.12) is free, because $M ( q )$ and $G ( q )$ have to be evaluated anyway for the right-hand side of the differential-algebraic system. Eliminating the variable $\Delta v$ in the last row of (7.12) yields the smaller system

$$
\left( \begin{array} { c c } { { M } } & { { G ^ { T } } } \\ { { G } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { \Delta w } } \\ { { \Delta \lambda } } \end{array} \right) = \left( \begin{array} { c } { { c } } \\ { { \alpha d + G b } } \end{array} \right)
$$

which is of the same type as those for the explicit methods. Once a solution to (7.13) is known the values of $\Delta v$ and $\Delta q$ are easily obtained from the first two rows of (7.12). We observe that the matrix in (7.13) does not depend on $\alpha = ( h \gamma ) ^ { - 1 }$ ． Hence only one LU decomposition is necessary for a step, independently of the number of distinct eigenvalues of the Runge-Kutta matrix. An implementation of these ideas reduced considerably the work for solving the nonlinear systems (see last picture of Fig. 7.4).

A similar reduction of the linear algebra was first proposed by Gear, Gupta & Leimkuhler (1985) for the BDF schemes. The above idea is not restricted to the index 2 case,and extends straightforwardly to the index 1 and index 3 situations. We finally remark that one has the possibility of retaining the decomposed matrix of (7.13) over several steps even in the case when the step size is changed.

# A Stiff Mechanical System

We now want to introduce some “stiffness” into the above mechanical system. To this end we take into account the elasticity of one of these bodies ( $K _ { 6 }$ appears to be the simplest one) and replace it by a spring with very large spring constant $c _ { 1 }$ . Thus the length of this spring will become an additional unknown variable $q _ { 8 }$ . We let the unstretched length be zf (of Table 7.1),and assume that the centre of gravity $C _ { 6 }$ has constant distance fa from the upper joint (see Fig.7.1). We further simplify the problem by assuming that the inertia of this body remains constant. Obviously the algebraic constraints (7.5) remain unchanged; we only have to replace the constant zf in (7.5) by the new variable $q _ { 8 }$ . The derivative matrix $G ( q ) = g ^ { \prime } ( q )$ has to be changed accordingly. It is now a $6 \times 8$ matrix.

The equations of motion for this modified problem are obtained as follows: in the kinetic energy (7.3) only the contribution of the 6th body (the new spring) changes, namely

$$
\begin{array} { r l } & { x _ { 6 } = x a + u \cdot \sin \varepsilon + ( q _ { 8 } - f a ) \cdot \cos ( \Omega + \varepsilon ) } \\ & { y _ { 6 } = y a - u \cdot \cos \varepsilon + ( q _ { 8 } - f a ) \cdot \sin ( \Omega + \varepsilon ) } \\ & { \dot { x } _ { 6 } ^ { 2 } + \dot { y } _ { 6 } ^ { 2 } = ( q _ { 8 } - f a ) ^ { 2 } \cdot \dot { \Omega } ^ { 2 } + 2 \cdot \left( ( q _ { 8 } - f a ) ^ { 2 } - u \cdot ( q _ { 8 } - f a ) \cdot \sin \Omega \right) \cdot \dot { \Omega } \cdot \dot { \varepsilon } } \\ & { \qquad + \left( ( q _ { 8 } - f a ) ^ { 2 } - 2 \cdot u \cdot ( q _ { 8 } - f a ) \cdot \sin \Omega + u ^ { 2 } \right) \cdot \dot { \varepsilon } ^ { 2 } } \\ & { \qquad + 2 \cdot u \cdot \cos \Omega \cdot \dot { \varepsilon } \cdot \dot { q } _ { 8 } + \dot { q } _ { 8 } ^ { 2 } } \\ & { \dot { \omega } _ { 6 } = \dot { \Omega } + \dot { \varepsilon } } \end{array}
$$

In the potential energy we have to add a term which is due to the new spring. We thus get (compare (7.4))

$$
U = - m o m \cdot \beta + c _ { 0 } \cdot \frac { ( \ell - \ell _ { 0 } ) ^ { 2 } } { 2 } + c _ { 1 } \cdot \frac { ( q _ { 8 } - z f ) ^ { 2 } } { 2 } ,
$$

where the spring constant $c _ { 1 }$ of the new spring is large. The resulting system is again of the form (7.6), but with $q \in \mathbb { R } ^ { 8 }$ . The initial values (7.7),(7.9),(7.12) for the 7 angles (7.2) are consistent for the new problem,if we require in addition

$$
q _ { 8 } ( 0 ) = z f , \qquad \dot { q } _ { 8 } ( 0 ) = 0 .
$$

This then implies ${ \ddot { q } } _ { 8 } ( 0 ) = 0$ .For the choice $c _ { 1 } = 1 0 ^ { 1 0 }$ we applied the implicit codes RADAU5 and DASSL to the above stiff mechanical system. The behaviour of these methods was nearly identical to that for the original problem (Fig.7.4). So there was no need to draw another picture. Obviously, the explicit codes DOPRI5, PHEM56 and MEXX do not work any longer.

It should be remarked that for ${ T o l \leq 1 / c _ { 1 } }$ the efficiency of the implicit codes suddenly decreases. This is due to the fact that the exact solution of the problem (with the initial values described above) is highly oscillatory with frequency $\mathcal { O } ( \sqrt { c _ { 1 } } )$ and amplitude $\mathcal { O } ( 1 / c _ { 1 } )$ about a smooth solution. A general theory for such situations has been elaborated by Ch.Lubich (1993). For very stringent toler-ances any code is forced to follow the oscillations and the step sizes become small.

# Exercises

1. Consider the differential equation (so-called “Kreiss problem")

$$
\begin{array} { r } { y ^ { \prime } = U ^ { T } ( x ) \left( \begin{array} { c c } { - 1 } & { 0 } \\ { 0 } & { - 1 / \varepsilon } \end{array} \right) U ( x ) y , \qquad U ( x ) = \left( \begin{array} { c c } { \cos x } & { \sin x } \\ { - \sin x } & { \cos x } \end{array} \right) } \end{array}
$$

and apply the Runge-Kutta code RADAU5 to this stiff problem. You will ob-serve that, for a fixed tolerance, the number of function evaluations increases with decreasing $\varepsilon > 0$ . Then apply the method to the equivalent system

$$
y ^ { \prime } = z , \qquad 0 = \left( \begin{array} { l l } { { 1 } } & { { 0 } } \\ { { 0 } } & { { \varepsilon } } \end{array} \right) U ( x ) z + U ( x ) y
$$

and show that the number of function evaluations does not increase for $\varepsilon \to 0$

a) Explain this phenomenon by studying the convergence of the simplified Newton iterations.

b) Prove that the index of the system (7.24) with $\varepsilon = 0$ is two.

# VI1.8 Symplectic Methods for Constrained Hamiltonian Systems

In principle,all approaches discussed in Sect. VI.2 can be employed for the numerical solution of constrained Hamiltonian systems. A disadvantage of these index reduction methods is,as we shall see below, that the symplectic structure of the flow is destroyed by the discretization.

In Sect.I.6 we have seen that the equations of motion for conservative mechanical systems can be written either in terms of position and velocity coordi-nates (Lagrangian formulation) or in terms of position and momentum coordinates (Hamiltonian formulation). For constrained mechanical systems the situation is exactly the same. In the present section we consider the Hamiltonian formulation

$$
\begin{array} { c } { { q ^ { \prime } = H _ { p } ( p , q ) } } \\ { { { } } } \\ { { p ^ { \prime } = - H _ { q } ( p , q ) - G ^ { T } ( q ) \lambda } } \\ { { { } } } \\ { { 0 = g ( q ) . } } \end{array}
$$

Here, $H : \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }  \mathbb { R }$ is the Hamiltonian function, $H _ { p }$ and $H _ { q }$ denote partial derivatives, $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ (with $m < n$ ）are the constraints,and $\check { G } ( q ) = g _ { q } ( q )$ . If $\begin{array} { r } { T ( q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { T } M ( q ) \dot { q } } \end{array}$ (with invertible $M ( q ) )$ is the kinetic energy of a mechanical system and $U ( q )$ its potential energy, we have $p = M ( q ) \dot { q }$ and

$$
{ \cal H } ( p , q ) = \frac { 1 } { 2 } p ^ { T } { \cal M } ( q ) ^ { - 1 } p + { \cal U } ( q ) ,
$$

(see Eq.(I.6.26)) in contrast to the Lagrange function, which is given by ${ \mathcal { L } } ( q , { \dot { q } } ) =$ $T ( q , \dot { q } ) - U ( q )$ . If $M ( q ) = I$ (the identity), we have $p = \dot { q }$ and both formulations, (1.46) and (8.1),are identical. If $M ( q )$ depends on $q$ , the formulation (8.1) may be numerically more advantageous than (1.46) (see Exercise 1).

Differentiating the constraint in (8.1) twice, we get

$$
\begin{array} { l } { { 0 = G ( q ) H _ { p } ( p , q ) , } } \\ { { 0 = { \displaystyle \frac { d } { d q } } \Bigl ( G ( q ) H _ { p } ( p , q ) \Bigr ) H _ { p } ( p , q ) - G ( q ) H _ { p p } ( p , q ) \Bigl ( H _ { q } ( p , q ) + G ^ { T } ( q ) \lambda \Bigr ) , } } \end{array}
$$

and we see that $\lambda$ can be expressed in terms of $p$ and $q$ ,if

$$
G ( q ) H _ { p p } ( p , q ) G ^ { T } ( q )
$$

in a neighbourhood of the considered solution. Therefore,(8.1） is a differentialalgebraic system of index 3. If $H ( p , q )$ is given by (8.2), condition (8.4) is the same as (1.47).