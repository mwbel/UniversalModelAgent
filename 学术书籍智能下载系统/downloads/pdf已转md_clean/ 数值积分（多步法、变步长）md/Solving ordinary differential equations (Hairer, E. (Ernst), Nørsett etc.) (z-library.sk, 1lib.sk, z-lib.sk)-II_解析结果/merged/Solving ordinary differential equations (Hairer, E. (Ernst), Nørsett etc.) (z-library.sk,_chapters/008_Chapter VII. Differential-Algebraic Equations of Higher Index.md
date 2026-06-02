# Chapter VII. Differential-Algebraic Equations of Higher Index

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/62063237685b84940fee033d61d0f261f48b19af3c0b3af89fdfccdffd92aea2.jpg)  
(Drawing by K.Wanner)

In the preceding chapter we considered the simplest special case of differentialalgebraic equations - the so-called index 1 problem. Many problems of practical interest are, however, of higher index, which makes them more and more difficult for their numerical treatment.

We start by classfying differential-algebraic equations (DAE) by the index (index of nilpotency for linear problems with constant coefficients; differentiation and perturbation index for general nonlinear problems) and present some examples arising in applications (Sect. VII.1). Several different approaches for solving numerically higher index problems are discussed in Sect. VI1.2: index reduction by differentiation combined with suitable projections,state space form methods, and treatment as overdetermined or unstructured systems. Sections VI1.3 and VII.4 study the convergence properties of multistep methods and Runge-Kutta methods when they are applied directly to index 2 systems. It may happen that the order of convergence is lower than for ordinary differential equations ("order reduction"). The study of conditions which guarantee a certain order is the subject of Sect. VII.5. Half-explicit methods for index 2 problems are especially suited for constrained mechanical systems (Sect. VI.6). A multibody mechanism and its numerical treatment are detailed in Sect. VI1.7. Finally, we discuss symplectic methods for constrained Hamiltonian systems (Sect. VII.8), and explain their long-term behaviour by a backward error analysis for differential equations on manifolds.

# VII.1 The Index and Various Examples

The most general form of a differential-algebraic system is that of an implicit differential equation

$$
F ( u ^ { \prime } , u ) = 0
$$

where $F$ and $u$ have the same dimension. We always assume $\boldsymbol { F }$ to be sufficiently differentiable. A non-autonomous system is brought to the form(1.1) by appending $\mathscr { x }$ to the vector $u$ , and by adding the equation $x ^ { \prime } = 1$

If $\partial F / \partial u ^ { \prime }$ is invertible we can formally solve (1.1) for $u ^ { \prime }$ to obtain an ordinary differential equation. In this chapter we are interested in problems (1.1） where $\partial F / \partial u ^ { \prime }$ is singular.

# Linear Equations with Constant Coefficients

Uebrigens kann ich die Meinung des Hrn. Jordan nicht theilen, dass es ziemlich schwer sei, der Weierstrass-schen Analyse zu folgen； sie scheint mir im Gegentheil vollkommen durchsichtig zu sein, ... (L. Kronecker 1874)

The simplest and best understood problems of the form(1.1) are linear differential equations with constant coefficients

$$
B u ^ { \prime } + A u = d ( x ) .
$$

In looking for solutions of the form $e ^ { \lambda x } u _ { 0 }$ (if $d ( x ) \equiv 0 { \mathrm { . } }$ ） we are led to consider the “matrix pencil” $A + \lambda B$ . When $A + \lambda B$ is singular for all values of $\lambda$ , then (1.2)has either no solution or infinitely many solutions for a given initial value (Exercise 1). We shall therefore deal only with regular matrix pencils, i.e., with problems where the polynomial $\operatorname* { d e t } ( A + \lambda B )$ does not vanish identically. The key to the solution of (1.2) is the following simultaneous transformation of $A$ and $B$ to canonical form.

Theorem 1.1(Weierstrass 1868, Kronecker 1890). Let $A + \lambda B$ be a regular matrix pencil. Then there exist nonsingular matrices $P$ and $Q$ such that

$$
P A Q = \left( { \begin{array} { c c } { C } & { 0 } \\ { 0 } & { I } \end{array} } \right) , \qquad P B Q = \left( { \begin{array} { c c } { I } & { 0 } \\ { 0 } & { N } \end{array} } \right)
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $I I _ { \perp }$ Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_31, $©$ Springer-Verlag Berlin Heidelberg 2010

where N = blockdiag $( N _ { 1 } , \ldots , N _ { k } )$ ,each $N _ { \imath }$ is of the form

$$
N _ { \imath } = \left( \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { } } & { { 0 } } \\ { { } } & { { \cdot \cdot } } & { { \cdot \cdot } } & { { } } \\ { { } } & { { } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { } } & { { } } & { { 0 } } \end{array} \right) ,
$$

and $C$ can be assumed to be in Jordan canonical form.

Proof (Gantmacher 1954 (Chapter XII),see also Exercises 2 and 3). We fix some $c$ such that $A + c B$ is invertible. If we multiply

$$
A + \lambda B = A + c B + ( \lambda - c ) B
$$

by the inverse of $A + c B$ and then transform $( A + c B ) ^ { - 1 } B$ to Jordan canonical form (Theorem I.12.2) we obtain

$$
\left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { I } } \end{array} \right) + \left( \lambda - c \right) \left( \begin{array} { c c } { { J _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { J _ { 2 } } } \end{array} \right) .
$$

Here, $J _ { 1 }$ contains the Jordan blocks with non-zero eigenvalues, $J _ { 2 }$ those with zero eigenvalues (the dimension of $J _ { 1 }$ is just the degree of the polynomial $\operatorname* { d e t } ( A +$ $\lambda B )$ ). Consequently, ${ { J } _ { 1 } }$ and $I - c J _ { 2 }$ are both invertible and multiplying (1.5) from the left by blockdiag $\left( J _ { 1 } ^ { - 1 } , ( I - \bar { c } J _ { 2 } ) ^ { - 1 } \right)$ gives

$$
\left( { \begin{array} { c c } { J _ { 1 } ^ { - 1 } ( I - c J _ { 1 } ) } & { 0 } \\ { 0 } & { I } \end{array} } \right) + \lambda \left( { \begin{array} { c c } { I } & { 0 } \\ { 0 } & { ( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 } } \end{array} } \right) .
$$

The matrices $J _ { 1 } ^ { - 1 } ( I - c J _ { 1 } )$ and $( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 }$ can then be brought to Jordan canonical form. Since all eigenvalues of $( I - c J _ { 2 } ) ^ { - 1 } J _ { 2 }$ are zero,we obtain the desired decomposition (1.3). □

Theorem 1.1 allows us to solve (1.2) as follows: we premultiply(1.2) by $P$ and use the transformation

$$
u = Q \left( \begin{array} { c } { { y } } \\ { { z } } \end{array} \right) , \qquad P d ( x ) = \left( \begin{array} { c } { { \eta ( x ) } } \\ { { \delta ( x ) } } \end{array} \right) .
$$

This decouples the differential-algebraic system (1.2) into

$$
y ^ { \prime } + C y = \eta ( x ) , \qquad N z ^ { \prime } + z = \delta ( x ) .
$$

The equation for $y$ is just an ordinary differential equation. The relation for $z$ decouples again into $k$ subsystems, each of the form (with $m = m _ { \imath }$ ）

$$
z _ { 2 } ^ { \prime } + z _ { 1 } = \delta _ { 1 } ( x )
$$

$$
\begin{array} { c } { { z _ { m } ^ { \prime } + z _ { m - 1 } = \delta _ { m - 1 } ( x ) } } \\ { { z _ { m } = \delta _ { m } ( x ) . } } \end{array}
$$

Here $z _ { m }$ is determined by the last equation,and the other components are obtained recursively by repeated differentiation. Thus $z _ { 1 }$ depends on the $( m - 1 )$ -th derivative of $\delta _ { m } ( x )$ . Since numerical differentiation is an unstable procedure, the largest $m _ { \imath }$ appearing in (1.4） is a measure of numerical difficulty for solving problem (1.2). This integer $\left( \operatorname* { m a x } { m _ { \ i } } \right)$ ） is called the index of nilpotency of the matrix pencil $A + \lambda B$ . It does not depend on the particular transformation used to get (1.3) (see Exercise 4).

Linear Equations with Variable Coefficients. In the case, where the matrices $A$ and $B$ in (1.2) depend on $\boldsymbol { x }$ , the study of the solutions is much more complicated. Multiplying the equation by $P ( x )$ and substituting $u = Q ( x ) v$ , yields the system

$$
P B Q v ^ { \prime } + ( P A Q + P B Q ^ { \prime } ) v = 0 ,
$$

which shows that the transformation (1.3) is no longer relevant. With the use of transformations of the form (1.8), Kunkel & Mehrmann (1995) derive a canonical form for linear systems with variable coefficients.

# Differentiation Index

A lot of English cars have steering wheels. (Fawlty Towers,Cleese and Booth 1979)

Let us start with the following example:

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = 0 . 7 \cdot y _ { 2 } + \sin ( 2 . 5 \cdot z ) = f _ { 1 } ( y , z ) } \\ & { y _ { 2 } ^ { \prime } = 1 . 4 \cdot y _ { 1 } + \cos ( 2 . 5 \cdot z ) = f _ { 2 } ( y , z ) } \\ & { 0 = y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } - 1 = g ( y ) . } \end{array}
$$

The“control variable” $z$ in (1.9a) can be interpreted as the position of a “steering wheel” keeping the vector field $( y _ { 1 } ^ { \prime } , y _ { 2 } ^ { \prime } )$ tangent to the circle $y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } = 1$ ,so that condition (1.9b) remains continually satisfied (see Fig.1.1a). By differentiating (1.9b) and substituting(1.9a) we therefore must have

$$
g _ { y } ( y ) f ( y , z ) = 0 .
$$

This defines a “hidden” submanifold of the cylinder,on which all solutions of $( 1 . 9 \mathrm { a } , \mathbf { b } )$ must lie (see Fig.1.1b). We stilldo not know how, with increasing $x$ ， the variable $z$ changes. This is obtained by differentiating(1.9c) with respect to $_ x$ ： $g _ { y y } ( f , f ) + g _ { y } f _ { y } f + g _ { y } f _ { z } z ^ { \prime } = 0$ . From this relation we can extract

$$
z ^ { \prime } = - ( g _ { y } f _ { z } ) ^ { - 1 } \left( g _ { y y } ( f , f ) + g _ { y } f _ { y } f \right)
$$

if

$$
g _ { y } ( y ) f _ { z } ( y , z ) \qquad { \mathrm { i s ~ i n v e r t i b l e . } }
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/d8b1c8fd022bf17e511c5a0378a7f3ed9530fd69deaf0cd4bae25b921352fb2b.jpg)  
Fig.1.la. The vector field (1.9a,d)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/4971b822e2c9e2e5cdd0bd6afb0fd938d17b898a7b2dd4d99c60e73cde5c6d8e.jpg)  
Fig.1.1b. The hidden submanifold

We have been able to transform the above differential-algebraic equation (1.9a,b) into an ordinary differential system (1.9a,d) by two analytic differentiations of the constraint (1.9c). This fact is used for the following definition, which has been developed in several papers (Gear & Petzold 1983,1984; Gear, Gupta & Leimkuhler 1985,Gear 1990, Campbell & Gear 1995).

Definition 1.2. Equation (1.1) has differentiation index $d i = m$ if $m$ is the minimal number of analytical differentiations

$$
F ( u ^ { \prime } , u ) = 0 , \ \frac { d F ( u ^ { \prime } , u ) } { d x } = 0 \ , \ \ldots \ , \ \frac { d ^ { m } F ( u ^ { \prime } , u ) } { d x ^ { m } } = 0
$$

such that equations (1.11) allow us to extract by algebraic manipulations an explicit ordinary differential system $u ^ { \prime } = \varphi ( u )$ (which is called the “underlying $O D E ^ { , } )$ .

Examples. Linear Equations with Constant Coefficients. The following problem

$$
\begin{array} { r l r l } { z _ { 2 } ^ { \prime } + z _ { 1 } = \delta _ { 1 } } & { { } \quad } & { z _ { 2 } ^ { \prime \prime } + z _ { 1 } ^ { \prime } = \delta _ { 1 } ^ { \prime } } \\ { z _ { 3 } ^ { \prime } + z _ { 2 } = \delta _ { 2 } } & { { } \Rightarrow } & { z _ { 3 } ^ { \prime \prime \prime } + z _ { 2 } ^ { \prime \prime } = \delta _ { 2 } ^ { \prime \prime } \quad } & { \Rightarrow } & { z _ { 1 } ^ { \prime } = \delta _ { 1 } ^ { \prime } - \delta _ { 2 } ^ { \prime \prime } + \delta _ { 3 } ^ { \prime \prime \prime } } \\ { z _ { 3 } = \delta _ { 3 } } & { { } \quad } & { z _ { 3 } ^ { \prime \prime \prime } = \delta _ { 3 } ^ { \prime \prime \prime } } \end{array}
$$

can be seen to have differentiation index 3. For linear equations with constant coefficients the differentiation index and the index of nilpotency are therefore the same.

Systems of Index $l$ . The differential-algebraic systems already seen in Chapter VI

$$
\begin{array} { r } { y ^ { \prime } = f ( y , z ) } \\ { 0 = g ( y , z ) } \end{array}
$$

have no $z ^ { \prime }$ . We therefore differentiate (1.13b) to obtain

$$
z ^ { \prime } = - g _ { z } ^ { - 1 } ( y , z ) g _ { y } ( y , z ) f ( y , z )
$$

which is possible if $g _ { z }$ is invertible in a neighbourhood of the solution. The problem (1.13a,b), for invertible $g _ { z }$ , is thus of differentiation index 1.

Systems of Index 2. In the system (see example (1.9))

$$
\begin{array} { c } { { y ^ { \prime } = f \bigl ( y , z \bigr ) } } \\ { { 0 = g \bigl ( y \bigr ) , } } \end{array}
$$

where the variable $z$ is absent in the algebraic constraint, we obtain by differentiation of(1.14b) the “hidden constraint"

$$
0 = g _ { y } ( y ) f ( y , z ) .
$$

If (1.10) is satisfied in a neighbourhood of the solution, then (1.14a) and (1.14c) constitute an index 1 problem. Differentiation of (1.14c) yields the missing differential equation for $z$ ,so that the problem(1.14a,b) is of differentiation index 2. If the initial values satisfy $0 = g ( y _ { 0 } )$ and $0 = g _ { y } ( y _ { 0 } ) f ( y _ { 0 } , z _ { 0 } )$ , we call them consistent. In this case,and only in this case,the system (1.14a,b) possesses a (locally) unique solution.

System (1.14a,b) is a representative of the larger class of problems of type (1.13a,b) with singular $g _ { z }$ . If we assume that $g _ { z }$ has constant rank in a neighbourhood of the solution, we can eliminate certain algebraic variables from $0 = g ( y , z )$ until the system is of the form (1.14). This can be done as follows: from the con-stant rank assumption it follows that either there exists a component of $g$ such that $\partial g _ { i } / \partial z _ { 1 } \neq 0$ locally, or $\partial g / \partial z _ { 1 }$ vanishes identically so that $g$ is already independent of $z _ { 1 }$ . In the first case we can express $z _ { 1 }$ as a function of $y$ and the remaining components of $z$ ，and then we can eliminate $z _ { 1 }$ from the system. Repeating this procedure with $z _ { 2 } , z _ { 3 }$ , etc.,will lead to a system of the form (1.14). This transformation does not change the index. Moreover, most numerical methods are invariant under this transformation. Therefore, theoretical work done for systems of the form (1.14) will also be valid for more general problems.

Systems of Index 3.Problems of the form

$$
\begin{array} { c } { { y ^ { \prime } = f ( y , z ) } } \\ { { z ^ { \prime } = k ( y , z , u ) } } \\ { { 0 = g ( y ) } } \end{array}
$$

are of differentiation index 3, if

$$
g _ { y } f _ { z } k _ { u } \mathrm { i s \ i n v e r t i b l e }
$$

in a neighbourhood of the solution. Differentiating (1.15c) twice gives

$$
\begin{array} { l } { 0 = g _ { y } f } \\ { 0 = g _ { y y } ( f , f ) + g _ { y } f _ { y } f + g _ { y } f _ { z } k . } \end{array}
$$

Equations (1.15a,b),(1.15e) together with Condition (1.16) are of the index 1 form (1.13a,b). Consistent inital values must satisfy the three conditions (1.15c,d,e).

An extensive study of the solution space of general differential-algebraic systems is done by Griepentrog & März (1986),März (1989,1990). These authors try to avoid assumptions on the smoothness on the problem as far as possible and re-place the above differentiations by a careful study of suitable projections depending only on the first derivatives of $F$ .

# Differential Equations on Manifolds

In the language of differentiable manifolds,whose use in DAE theory was urged by Rheinboldt (1984),a constraint (such as $g ( y ) = 0$ )represents a manifold, which we denote by

$$
\mathcal { M } = \{ y \in \mathbb { R } ^ { n } \mid g ( y ) = 0 \} .
$$

We assume that $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ (with $m < n \mathrm { ~ . ~ }$ )is a sufficiently differentiable function whose Jacobian $g _ { y } ( y )$ has full rank for $y \in M$ . For a fixed $y \in \mathcal { M }$ we denote by

$$
T _ { y } { \mathcal { M } } = \{ v \in \mathbb { R } ^ { n } \mid g _ { y } ( y ) v = 0 \} ,
$$

the tangent space of $\mathcal { M }$ at $y$ . This is a linear space and has the same dimension $n - m$ as the manifold $\mathcal { M }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/a05449e58134f1bab72e7577852de2caf7a02d4360e8f679e754fa5c26b2628c.jpg)  
Fig.1.2. A manifold with a tangent vector field, a chart, and a solution curve

A vector field on $\mathcal { M }$ is a mapping $v : \mathcal { M } \to \mathbb { R } ^ { n }$ , which satisfies $v ( y ) \in T _ { y } \mathcal { M }$ for all $y \in M$ . For such a vector field we call

$$
y ^ { \prime } = v ( y ) , \qquad y \in { \mathcal { M } }
$$

a differential equation on the manifold $\mathcal { M }$ . Differentiation on an $\left( n { - } m \right)$ -dimensional manifold is described by so-called charts $\varphi _ { i } : U _ { i } \to E _ { i }$ ,where the $U _ { i }$ cover the manifold $\mathcal { M }$ and the $E _ { \imath }$ are open subsets of $\mathbb { R } ^ { n - m }$ (Fig.1.2; see also Lang (1962), Chap.II and Abraham, Marsden & Ratiu (1983), Chap.III). The local theory of ordinary differential equations can be extended to vector fields on manifolds in a straightforward manner:

Project the vectors $v ( y )$ onto $E _ { i }$ via a chart $\varphi _ { i }$ by multiplying $v ( y )$ with the Jacobian of $\varphi _ { \imath }$ at $y$ . Then apply standard results to the pro-jected vector field in $\mathbb { R } ^ { n - m }$ ,and pull the solution back to $\mathcal { M }$

(see Fig.1.2). The local existence of solutions of (1.19) can be shown in this way. The obtained solution is independent of the chosen chart. Where the solution leaves the domain of a chart, the integration must be continued via another one.

Index 2 Problems. Consider the system $_ { ( 1 . 1 4 a , b ) }$ and suppose that (1.10) is satisfied. This condition implies that $g _ { y } ( y )$ is of full rank,so that (1.17) is a smooth manifold. Moreover, the Implicit Function Theorem implies that the differentiated constraint (1.14c） can be solved for $z$ (in a neighbourhood of the solution), i.e., there exists a smooth function $h ( y )$ such that

$$
g _ { y } ( y ) f ( y , z ) = 0 \qquad \Longleftrightarrow \qquad z = h ( y ) .
$$

Inserting this relation into (1.10a) yields

$$
y ^ { \prime } = f { \big ( } y , h ( y ) { \big ) } , \qquad y \in { \mathcal { M } }
$$

which is a differential equation on the manifold(1.17), because $f ( y , h ( y ) ) \in T _ { y } \mathcal { M }$ by (1.20). The differential equation (1.21) is equivalent to (1.14a,b).

Example. The manifold $M$ for problem (1.9） is onedimensional (circle). In points,where $y _ { 1 } \neq \pm 1$ ，we can solve (1.9b) to obtain locally $y _ { 2 } = \pm { \sqrt { 1 - y _ { 1 } ^ { 2 } } }$ . The map $( y _ { 1 } , y _ { 2 } ) \mapsto y _ { 1 }$ consitutes a chart $\varphi$ , which is bijective in a neighbourhood of the considered point. Inserting $z$ from $( 1 . 9 \mathrm { c } )$ and the above $y _ { 2 }$ into (1.9a), yields an equation $y _ { 1 } ^ { \prime } = G ( y _ { 1 } )$ ， which is the projected vector field in $\mathbb { R } ^ { 1 }$ .

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/921403f36c4fc4059542cbc9c2c69b3aea22d84744aaf445db8d4d07c067765c.jpg)

Index 3 Problems.For the system $( 1 . 1 5 \mathrm { a } , \mathsf { b } , \mathsf { c } )$ the solutions lie on the manifold

$$
\mathcal { M } = \{ ( y , z ) ~ \vert ~ g ( y ) = 0 , ~ g _ { y } ( y ) f ( y , z ) = 0 \} .
$$

The assumption (1.16) implies that $g _ { y } ( y )$ and $g _ { y } ( y ) f _ { z } ( y , z )$ have full rank, so that $\mathcal { M }$ is a manifold. Its tangent space at $( y , z )$ is

$$
\begin{array} { r } { T _ { ( y , z ) } \mathcal { M } = \{ ( v , w ) | g _ { y } ( y ) v = 0 , g _ { y y } ( y ) \big ( f ( y , z ) , v \big ) \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } } \\ { + g _ { y } ( y ) \big ( f _ { y } ( y , z ) v + f _ { z } ( y , z ) w \big ) = 0 \} . } \end{array}
$$

Solving Eq.(1.15e) for $u$ and inserting the result into (1.15b) yields a differential equation on the manifold $\mathcal { M }$ . Because of (1.15d,e), the obtained vector field lies in the tangent space $T _ { ( y , z ) } { \mathcal { M } }$ for all $( y , z ) \in M$

# The Perturbation Index

Now fills thy sleep with perturbations. (The Ghost of Anne in Shakespeare's Richard III,act $\mathbb { V } _ { \mathfrak { s } }$ sc.I)

A second concept of index,due to HLR89 1, interprets the index as a measure of sensitivity of the solutions with respect to perturbations of the given problem.

Definition 1.3. Equation (1.1） has perturbation index $p i = n$ along a solution $u ( x )$ on $[ 0 , { \overline { { x } } } ]$ ,if $m$ is the smallest integer such that, for all functions $\widehat { \mathcal { U } } \big ( \mathcal { X } \big )$ having a defect

$$
F ( \widehat { u } ^ { \prime } , \widehat { u } ) = \delta ( x ) ,
$$

there exists on $\left[ 0 , { \overline { { x } } } \right]$ an estimate

$$
\| \widehat { u } ( x ) - u ( x ) \| \leq C \Big ( \| \widehat { u } ( 0 ) - u ( 0 ) \| + \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ( \xi ) \| + . . . + \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ^ { ( m - 1 ) } ( \xi ) \| \Big )
$$

whenever the expression on the right-hand side is sufficiently small.

Remark. We deliberately do not write “Let ${ \widehat { u } } ( x )$ be the solution of $F ( \widehat { \mathcal { U } } ^ { \prime } , \widehat { \mathcal { U } } ) =$ $\delta ( x ) \ldots ^ { \mathfrak { n } }$ in this definition, because the existence of such a solulion ${ \widehat { u } } ( x )$ for an arbitrarily given $\displaystyle \delta ( x )$ is not assured. We start with $\widehat { u }$ and then compute $\delta$ as defect of (1.1).

Systems of Index 1. For the computation of the perturbation index of (1.13a,b) we consider the perturbed system

$$
\begin{array} { r } { \widehat { \mathcal { Y } } ^ { \prime } = f ( \widehat { \mathcal { Y } } , \widehat { z } ) + \delta _ { 1 } ( x ) } \\ { 0 = g ( \widehat { \mathcal { Y } } , \widehat { z } ) + \delta _ { 2 } ( x ) . } \end{array}
$$

The essential observation is that the difference $\widehat { z } \sim z$ can be estimated with the help of the Implicit Function Theorem, without any differentiation of the equation. Since $g _ { z }$ is invertible by hypothesis, this theorem gives from (1.26b) compared to (1.13b)

$$
\| \widehat { \widetilde { \widetilde { \mathbf { \Gamma } } } } ( x ) - z ( x ) \| \leq C _ { 1 } \big ( \| \widehat { \widetilde { \boldsymbol { y } } } ( x ) - \boldsymbol { y } ( x ) \| + \| \delta _ { 2 } ( x ) \| \big )
$$

as long as the right-hand side of (1.27) is sufficiently small. We now subtract (1.26a) from (1.13a), integrate from 0 to $\boldsymbol { x }$ ,use a Lipschitz condition for $f$ and the above estimate for ${ \widehat { z } } ( x ) - z ( x )$ . This gives for $e ( x ) = \| { \widehat { y } } ( x ) - y ( x ) \|$

$$
e ( x ) \leq e ( 0 ) + C _ { 2 } \int _ { 0 } ^ { r } e ( t ) d t + C _ { 3 } \int _ { 0 } ^ { x } \| \delta _ { 2 } ( t ) \| d t + \Big \| \int _ { 0 } ^ { \varepsilon } \delta _ { 1 } ( t ) d t \Big \| .
$$

In this estimate the norm is inside the integral for $\delta _ { 2 }$ , but outside the integral for $\delta _ { 1 }$ This is due to the fact that perturbations of the algebraic equation(1.13b) are more

serious than perturbations of the differential equation (1.13a). We finally apply Gronwall's Lemma (Exercise I.10.2) to obtain on a bounded interval $[ 0 , { \overline { { x } } } ]$

$$
\begin{array} { l l l } { \displaystyle \| \widehat { y } ( x ) - y ( x ) \| \leq C _ { 4 } \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \int _ { 0 } ^ { x } \| \delta _ { 2 } ( t ) \| d t + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \Big \| \int _ { 0 } ^ { \xi } \delta _ { 1 } ( t ) d t \Big \| \Big ) } \\ { \displaystyle \leq C _ { 5 } \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta _ { 2 } ( \xi ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta _ { 1 } ( \xi ) \| \Big ) . } \end{array}
$$

This inequality,together with (1.27),shows that the perturbation index of the problem is 1.

Systems of Index 2. We consider the following perturbation of system (1.14a,b)

$$
\begin{array} { c } { { \widetilde { y } ^ { \prime } = f ( \widehat { y } , \widehat { z } ) + \delta ( x ) } } \\ { { 0 = g ( \widehat { y } ) + \theta ( x ) . } } \end{array}
$$

Differentiation of (1.28b) gives

$$
0 = g _ { y } ( \widehat { y } ) f ( \widehat { y } , \widehat { z } ) + g _ { y } ( \widehat { y } ) \delta ( x ) + \theta ^ { \prime } ( x ) .
$$

Under the assumption (1.1O) we can use the estimates of the index 1 case (with $\delta _ { 2 } ( x )$ replaced by $g _ { y } \big ( \widehat { y } ( x ) \big ) \delta ( x ) + \theta ^ { \prime } ( x ) )$ to obtain

$$
\begin{array} { r l } & { \| \widehat { y } ( x ) - y ( x ) \| \leq C \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \int _ { 0 } ^ { x } \big ( \| \delta ( \xi ) \| + \| \theta ^ { \prime } ( \xi ) \| \big ) d \xi \Big ) } \\ & { \| \widehat { z } ( x ) - z ( x ) \| \leq C \Big ( \| \widehat { y } ( 0 ) - y ( 0 ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \delta ( \xi ) \| + \displaystyle \operatorname* { m a x } _ { 0 \leq \xi \leq x } \| \theta ^ { \prime } ( \xi ) \| \Big ) . } \end{array}
$$

Since these estimates depend on the first derivative of $\theta$ , the perturbation index of this problem is 2. A sharper estimate for the $y$ -component is given in Exercise 6.

Example. Fig.1.3 presents an illustration for the index 2 problem (1.9a,b). Small perturbations of $g ( y )$ ，once discontinuous in the first derivative (left),the other of oscillatory type (right),results in discontinuities or violent oscillations of $z$ ， respectively.

The above examples might give the impression that the differentiation index and the perturbation index are always equal. The following counter-examples show that this is not true.

Counterexamples. The first counterexample of type $M ( y ) y ^ { \prime } = f ( y )$ is given by Lubich (1989):

$$
\begin{array} { r l r } { y _ { 1 } ^ { \prime } - y _ { 3 } y _ { 2 } ^ { \prime } + y _ { 2 } y _ { 3 } ^ { \prime } = 0 } & { } & { \widehat { y } _ { 1 } ^ { \prime } - \widehat { y } _ { 3 } \widehat { y } _ { 2 } ^ { \prime } + \widehat { y } _ { 2 } \widehat { y } _ { 3 } ^ { \prime } = 0 \quad \quad } \\ { y _ { 2 } = 0 } & { } & { \widehat { y } _ { 2 } = \varepsilon \sin \omega x } \\ { y _ { 3 } = 0 } & { } & { \widehat { y } _ { 3 } = \varepsilon \cos \omega x } \end{array}
$$

with $y _ { \ i } ( 0 ) = 0 \ ( i = 1 , 2 , 3 )$ . Inserting $\widehat { y } _ { 2 } = \varepsilon \sin \omega x$ and $\widehat { y } _ { 3 } = \varepsilon \cos \omega x$ into the first equation gives $\widehat { y } _ { 1 } ^ { \prime } = \varepsilon ^ { 2 } \omega$ which makes, for $\varepsilon$ fixed and $\omega  \infty$ ,an estimate

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/2c58003ff96d5ed7c11d372fb556371c627ee360c7628512f5d6257c0bcc1cdc.jpg)  
Fig.1.3.Perturbations of an index 2 problem

(1.25)with $m \simeq 1$ impossible. However, for $m \simeq 2$ the estimate (1.25) is clearly satisfied. This problem,which is obviously of differentiation index 1,is thus of perturbation index 2.

It was believed for some time (see the first edition, p.479),that the differenti-ation and perturbation indices can difer at most by 1. The following example, due to Campbell & Gear (1995), was therefore a big surprise:

$$
y _ { m } N y ^ { \prime } + y = 0 ,
$$

where $N$ is a $m \times m$ upper triangular nilpotent Jordan block. Since the last row of $N$ is zero, we have $y _ { m } = 0$ ,and the differentiation index is 1. On the other hand, adding a perturbation makes $y _ { m }$ different from zero. This is the reason why the perturbation index of(1.32) is $m$

# Control Problems

Many problems of control theory lead to ordinary differential equations of the form $y \prime = f ( y , u )$ ，where $u$ represents a set of controls. Similar as in example (1.9) above, these controls must be applied so that the solution satisfies some constraints $0 = g ( y , u )$ . For numerical examples of such control problems we refer to Brenan (1983)(space shutle simulation) and Brenan, Campbell & Petzold (1989).

Optimal Control Problems are differential equations $y \prime = f ( y , u )$ formulated in such a way that the control $u ( x )$ has to minimize some cost functional. The Euler-- Lagrange equation then often becomes a differential-algebraic system (Pontryagin, Boltyanskij,Gamkrelidze & Mishchenko 1961,Athans & Falb 1966,Campbell 1982).We demonstrate this on the problem

$$
y ^ { \prime } = f ( y , u ) , \qquad y ( 0 ) = y _ { 0 }
$$

with cost functional

$$
J ( u ) = \int _ { 0 } ^ { 1 } \varphi \big ( y ( x ) , u ( x ) \big ) d x .
$$

For a given function $u ( x )$ the solution $y ( x )$ is determined by (1.33a). In order to find conditions for $u ( x )$ which minimize $\boldsymbol { J } ( u )$ of (1.33b), we consider the perturbed control $u ( x ) + \varepsilon \delta u ( x )$ where $\delta u ( x )$ is an arbitrary function and $\varepsilon$ a small number. To this control there corresponds a solution $y ( x ) + \varepsilon \delta y ( x ) + { \mathcal { O } } ( \varepsilon ^ { 2 } )$ of (1.33a); hence (by comparing powers of $\varepsilon$ ）

$$
\delta y ^ { \prime } ( x ) = f _ { y } ( x ) \delta y ( x ) + f _ { u } ( x ) \delta u ( x ) , \qquad \delta y ( 0 ) = 0 ,
$$

where, as usual, $f _ { y } ( x ) = f _ { y } ( y ( x ) , u ( x ) )$ , etc. Linearization of (1.33b) shows that

$$
J ( u + \varepsilon \delta u ) - J ( u ) = \varepsilon \int _ { 0 } ^ { 1 } \left( \varphi _ { y } ( x ) \delta y ( x ) + \varphi _ { u } ( x ) \delta u ( x ) \right) d x + \mathcal O ( \varepsilon ^ { 2 } )
$$

so that

$$
\int _ { 0 } ^ { 1 } \left( \varphi _ { y } ( x ) \delta y ( x ) + \varphi _ { u } ( x ) \delta u ( x ) \right) d x = 0
$$

is a necessary condition for $u ( x )$ to be an optimal solution of our problem. In order to express $\delta y$ in terms of $\delta u$ in (1.35),we introduce the adjoint differential equation

$$
\boldsymbol { v } ^ { \prime } = - f _ { y } ( \boldsymbol { x } ) ^ { \mathcal { T } } \boldsymbol { v } - \varphi _ { y } ( \boldsymbol { x } ) ^ { \mathcal { T } } , \qquad \boldsymbol { v } ( 1 ) = 0
$$

with inhomogeneity $\varphi _ { y } ( x ) ^ { T }$ . Hence we have (see Exercise 7)

$$
\int _ { 0 } ^ { 1 } \varphi _ { y } ( x ) \delta y ( x ) d x = \int _ { 0 } ^ { 1 } v ^ { T } ( x ) f _ { u } ( x ) \delta u ( x ) d x .
$$

Inserted into (1.35) this gives the necessary condition

$$
\int _ { 0 } ^ { 1 } \Big ( \boldsymbol { v } ^ { T } ( \boldsymbol { x } ) f _ { u } ( \boldsymbol { x } ) + \varphi _ { u } ( \boldsymbol { x } ) \Big ) \delta \boldsymbol { u } ( \boldsymbol { x } ) d \boldsymbol { x } = 0 .
$$

Since this relation has to be satisfied for all $\delta u$ we obtain the necessary relation $v ^ { T } ( x ) f _ { u } ( x ) + \varphi _ { u } ( x ) = 0$ by the so-called “fundamental lemma of variational calculus".

In summary, we have proved that a solution of the above optimal control problem has to satisfy the system

$$
\begin{array} { r l r l } & { \boldsymbol { y } ^ { \prime } = f ( \boldsymbol { y } , \boldsymbol { u } ) , } & & { \boldsymbol { y } ( 0 ) = \boldsymbol { y } _ { 0 } } \\ & { \boldsymbol { v } ^ { \prime } = - f _ { y } ( \boldsymbol { y } , \boldsymbol { u } ) ^ { T } \boldsymbol { v } - \varphi _ { y } ( \boldsymbol { y } , \boldsymbol { u } ) ^ { T } , } & & { \boldsymbol { v } ( 1 ) = 0 } \\ & { 0 = \boldsymbol { v } ^ { T } f _ { u } ( \boldsymbol { y } , \boldsymbol { u } ) + \varphi _ { u } ( \boldsymbol { y } , \boldsymbol { u } ) . } \end{array}
$$

This is a boundary value differential-algebraic problem. It can also be obtained directly from the Pontryagin minimum principle (see Pontryagin et al. 1961, Athans & Falb 1966).

Differentiation of the algebraic relation in (1.39) shows that the system (1.39) has index 1 if the matrix

$$
\sum _ { i = 1 } ^ { n } v _ { i } \frac { \partial ^ { 2 } f _ { \imath } } { \partial u ^ { 2 } } \left( y , u \right) + \frac { \partial ^ { 2 } \varphi } { \partial u ^ { 2 } } \left( y , u \right)
$$

is invertible along the solution.A situation where the system (1.39) has index 3 is presented in Exercise 8. An index 5 problem of this type is given in “Example $3 . 1 ^ { \mathfrak { s } }$ of Clark (1988). Other control problems with a large index are discussed in Campbell (1995).

# Mechanical Systems

... berechnen wir $T , V , L$ . Mehr brauchen wir von der Geometrie und Mechanik unseres Systems nicht zu wissen. Alles üibrige besorgt ohne unser Zutun der Formalismus von LAGRANGE.

(Sommerfeld 1942, $\ S 3 5 \mathrm { \Omega }$

An interesting class of differential-algebraic systems appears in mechanical modeling of constrained systems. A choice method for deriving the equations of mo-tion of mechanical systems is the Lagrange-Hamilton principle, whose long history goes back to merely theological ideas of Leibniz and Maupertuis. Let $q _ { 1 } , \ldots , q _ { n }$ be position coordinates of a system and $u _ { i } = \dot { q } _ { i }$ the velocities. Suppose a function $L ( q , \dot { q } )$ is given; then the Euler equations of the variational problem

$$
\int _ { t _ { 1 } } ^ { t _ { 2 } } L ( q , \dot { q } ) d t = \operatorname* { m i n } !
$$

are given by

$$
{ \frac { d } { d t } } \left( { \frac { \partial L } { \partial { \dot { q } } _ { k } } } \right) - { \frac { \partial L } { \partial q _ { k } } } = 0 , \qquad k = 1 , \ldots , n
$$

or

$$
\sum _ { \ell = 1 } ^ { n } L _ { \dot { q } _ { k } \dot { q } _ { \ell } } \ddot { q } _ { \ell } = L _ { q _ { k } } - \sum _ { \ell = 1 } ^ { n } L _ { \dot { q } _ { k } q _ { \ell } } \dot { q } _ { \ell } .
$$

The great discovery of Lagrange (1788) is that for $L = T - U$ ，where $T$ is the kinetic energy and $U$ the potential energy, the differential equations (1.43) describe the movement of the corresponding “conservative system". For a proof and various generalizations, consult any book on mechanics e.g., Sommerfeld (1942)，vol.I, $\ S \ S 3 3 - 3 7$ , or Arnol'd (1979), part II.

Example 1. For the mathematical pendulum of length $\ell$ we choose as position coordinate the angle $\theta = q _ { 1 }$ such that $T = m \ell ^ { 2 } { \dot { \theta } } ^ { 2 } / 2$ and $U = - \ell m g \cos { \theta }$ . Then (1.43) becomes $\ell { \ddot { \theta } } = - g \sin \theta$ , the well-known pendulum equation.

Movement with Constraints. Suppose now that we have some constraints $g _ { 1 } ( q ) =$ $0 ; \ldots , g _ { m } ( q ) = 0$ on our movement. Another great idea of Lagrange is to vary the “Lagrange function” as follows in this case

$$
L = T - U - \lambda _ { 1 } g _ { 1 } ( q ) - . . . - \lambda _ { m } g _ { m } ( q )
$$

where the “Lagrange multipliers” $\lambda _ { i }$ are appended to the coordinates. The important fact is that, since $L$ is independent of $\bar { \dot { \lambda } } _ { i }$ , the equation (1.43), for the derivatives with respect to $\lambda _ { k }$ , just becomes $0 = g _ { k } ( q )$ , the desired side conditions.

Example 2. We now describe the pendulum in Cartesian coordinates $x , y$ with constraint $x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } = 0$ . This gives for (1.44)

$$
L = { \frac { m } { 2 } } { \bigl ( } { \dot { x } } ^ { 2 } + { \dot { y } } ^ { 2 } { \bigr ) } - m g y - \lambda ( x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } )
$$

and (1.43) becomes

$$
\begin{array} { c } { { m \ddot { x } = - 2 x \lambda } } \\ { { m \ddot { y } = - m g - 2 y \lambda } } \\ { { 0 = x ^ { 2 } + y ^ { 2 } - \ell ^ { 2 } . } } \end{array}
$$

In this example the physical meaning of $\lambda$ is the tension in the rod which maintains the mass point on the desired orbit.

The general form of a constrained mechanical system (1.43) is in vector notation (after replacing dots by primes)

$$
\begin{array} { c } { q ^ { \prime } = u } \\ { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } \\ { 0 = g ( q ) } \end{array}
$$

where $M ( q ) = T _ { \dot { q } \dot { q } } = T _ { u u }$ is a positive definite matrix, $G ( q ) = \partial g / \partial q$ and $q =$ $( q _ { 1 } , \ldots , q _ { n } ) ^ { T }$ ， $\boldsymbol { u } \equiv ( \dot { q } _ { 1 } , \dots , \dot { q } _ { n } ) ^ { T }$ ， $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { m } ) ^ { T }$ . Various formulations are possible for such a problem, each of which leads to a different numerical approach.

Index 3 Formulation (position level, descriptor form). If we formally multiply (1.46b) by $M ^ { - 1 }$ ,the system (1.46) becomes of the form (1.15) with $( q , u , \lambda )$ in the roles of $( y , z , u )$ . The condition (1.16), written out for (1.46), is

$$
G M ^ { - 1 } G ^ { T } \qquad \mathrm { i s ~ i n v e r t i b l e } .
$$

This is satisfied, if the constraints (1.46c) are independent, i.e., if the rows of the matrix $G$ are linearly independent. Under this assumption, the system (1.46a,b,c) is thus an index 3 problem.

Index 2 Formulation (velocity level). Differentiation of (1.46c) gives

$$
0 = G ( q ) u .
$$

If we replace (1.46c) by (1.46d) we obtain a system of the form (1.14a,b) with $( q , u )$ in the role of $y$ and $\lambda$ that of $z$ ．One verifies that Condition (1.10） is equivalent to (1.47), so that $( 1 . 4 6 \mathsf { a } , \mathsf { b } , \mathsf { d } )$ represents a problem of index 2.

Index 1 Formulation (acceleration level). If we differentiate twice the constraint (1.46c), the resulting equation together with (1.46b) yield

$$
\left( \begin{array} { c c } { { M ( q ) } } & { { G ^ { T } ( q ) } } \\ { { G ( q ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { u ^ { \prime } } } \\ { { \lambda } } \end{array} \right) = \left( \begin{array} { c } { { f ( q , u ) } } \\ { { - g _ { q q } ( q ) ( u , u ) } } \end{array} \right) .
$$

This allows us to express $u ^ { \prime }$ and $\lambda$ as functions of $q , u$ , provided that the matrix in (1.46e) is invertible. Hence,(1.46a,e) consitute an index 1 problem. The assumption on the matrix in Eq.(1.46e) is weaker than (1.47),because $M ( q )$ need not be regular.

All these formulations are mathematically equivalent,if the initial values are consistent, i.e., if (1.46c,d,e) are satisfied. However, if for example the index 2 system (1.46a,b,d) is integrated numerically, the constraints of the original problem will no longer be exactly satisfied. For this reason Gear, Gupta & Leimkuhler (1985)introduced another index 2 formulation("... an interesting way of reducing the problem to index two and adding variables so that the constraint continues to be satisfied".).

GGL Formulation. The idea is to add the constraint (1.46d) to the original system and to introduce an additional Lagrange multiplier $\mu$ in (1.46a). For the sake of symmetry we also multiply (1.46a) by $M ( q )$ , so that the whole system becomes

$$
\begin{array} { c } { { M ( q ) q ^ { \prime } = M ( q ) u - G ^ { T } ( q ) \mu } } \\ { { M ( q ) u ^ { \prime } = f ( q , u ) - G ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) } } \\ { { 0 = G ( q ) u . } } \end{array}
$$

Here the differential variables are $( q , u )$ and the algebraic variables are $( \mu , \lambda )$ . System (1.48) is of the form (1.14a,b) and the index 2 assumption is satisfied if (1.47) holds.

A concrete mechanical system is described in detail, together with numerical results for all the above formulations, in Sect. VI.7.

# Exercises

1. Prove that the initial value problem

$$
B u ^ { \prime } + A u = 0 , \qquad u ( 0 ) = u _ { 0 }
$$

has a unique solution if and only if the matrix pencil $A + \lambda B$ is regular.

Hint for the "only if" part. If $\mathscr { n }$ is the dimension of $u$ , choose arbitrarily $n + 1$ distinct $\lambda _ { i }$ and vectors $\textstyle v _ { \imath } \neq 0$ satisfying $( A + \lambda _ { \iota } B ) v _ { \iota } = 0$ . Then take a linear combination, such that $\sum { \alpha _ { \ i } v _ { \ i } } = 0$ ,but $\sum \alpha _ { \ i } e ^ { \lambda _ { \ i } x } v _ { i } \not \equiv 0$

2. (Stewart 1972). Let $A + \lambda B$ be a regular matrix pencil. Show that there exist unitary matrices $Q$ and $Z$ such that

$$
\begin{array} { r } { Q A Z = \left( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} \right) , \qquad Q B Z = \left( \begin{array} { c c } { B _ { 1 1 } } & { B _ { 1 2 } } \\ { 0 } & { B _ { 2 2 } } \end{array} \right) } \end{array}
$$

are both triangular. Further, the diagonal elements of $A _ { 2 2 }$ and $B _ { 1 1 }$ are all 1, those of $B _ { 2 2 }$ are all 0.

Hint (Compare with the Schur decomposition of Theorem I.12.1). Let $\lambda _ { 1 }$ be a zero of $\operatorname* { d e t } ( A + \lambda B )$ and $v _ { 1 } \neq 0$ be such that $( A + \lambda _ { 1 } B ) v _ { 1 } = 0$ . Verify that $B v _ { 1 } \neq 0$ and that

$$
A Z _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { - \lambda _ { 1 } } } & { { \ast } } \\ { { 0 } } & { { \widetilde { A } } } \end{array} \right) , \qquad B Z _ { 1 } = Q _ { 1 } \left( \begin{array} { c c } { { 1 } } & { { \ast } } \\ { { 0 } } & { { \widetilde { B } } } \end{array} \right)
$$

where $Q _ { 1 } , Z _ { 1 }$ are unitary matrices whose first columns are $B v _ { 1 }$ and $v _ { 1 }$ ,respectively. The matrix pencil $\widetilde { A } + \lambda \widetilde { B }$ is again regular and this procedure can be continued until $\operatorname* { d e t } ( \tilde { A } + \lambda \tilde { B } ) = C o n s t$ which implies that det $\widetilde { B } = 0$ In this case we take a vector $v _ { 2 } \not = 0$ such that $\widetilde { B } v _ { 2 } = 0$ and transform $\widetilde { A } + \lambda \widetilde { B }$ with unitary matrices $Q _ { 2 } , Z _ { 2 }$ ， whose first columns are $\stackrel { \sim } { A } v _ { 2 }$ and $v _ { 2 }$ ， respectively. For a practical computation of the decomposition (1.50) see Golub & Van Loan (1989), Sect. 7.7.

3. Under the assumptions of Exercise 2 show that there exist matrices $S$ and $T$ such that

$$
\begin{array} { r l } { ( I  } & { { } S } \\ { ( 0  } & { { } I ) ( \begin{array} { c c } { A _ { 1 1 } } & { A _ { 1 2 } } \\ { 0 } & { A _ { 2 2 } } \end{array} ) ( I  } & { { } T ) = ( \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { 0 } & { A _ { 2 2 } } \end{array} ) , } \\ { ( \begin{array} { c c } { I } & { { } S } \\ { 0 } & { I } \end{array} ) ( \begin{array} { c c } { B _ { 1 1 } } & { B _ { 1 2 } } \\ { 0 } & { B _ { 2 2 } } \end{array} ) ( \begin{array} { c c } { I } & { { } T } \\ { 0 } & { I } \end{array} ) = ( \begin{array} { c c } { B _ { 1 1 } } & { 0 } \\ { 0 } & { B _ { 2 2 } } \end{array} ) . } \end{array}
$$

Hint. These matrices have to satisfy

$$
\begin{array} { r } { A _ { 1 1 } T + A _ { 1 2 } + S A _ { 2 2 } = 0 } \\ { B _ { 1 1 } T + B _ { 1 2 } + S B _ { 2 2 } = 0 } \end{array}
$$

and can be computed as follows: the first column of $T$ is obtained from(1.51b) because $\boldsymbol { B } _ { 1 1 }$ is invertible and the first column of $S B _ { 2 2 }$ vanishes; then the first column of $S$ is given by (1.51a) because $A _ { 2 2 }$ is invertible; the second column of $S B _ { 2 2 }$ is then known and we can compute the second column of $T$ from (1.51b), etc.

4.Prove that the index of nilpotency of a regular matrix pencil $A + \lambda B$ does not depend on the choice of $P$ and $Q$ in (1.3).

Hint. Consider two different decompositions of the form (1.3) and denote the matrices which appear by $C _ { 1 } , N _ { 1 }$ and $C _ { 2 } , N _ { 2 }$ , respectively. Show the existence of a regular matrix $T$ such that $N _ { 2 } = T ^ { - 1 } N _ { 1 } T$

5.Prove that the system $( \mathrm { V I } . 3 . 4 \mathrm { a } , \mathrm { b } )$ has index 2 (it is of the form (1.14a,b) and satisfies (1.10)). The full system (VI.3.4) has perturbation index $k$

6.(Arnold 1993). Consider the index 2 problem(1.14) and its perturbation(1.28). Prove that the difference $\Delta y ( x ) = \widehat { y } ( x ) - y ( x )$ satisfies

$$
\begin{array} { r l } & { \displaystyle \| \Delta y ( x ) \| \leq C \Big ( \| \Delta y ( 0 ) \| + \underset { 0 \leq \xi \leq x } { \operatorname* { m a x } } \Big ( \Big \| \int _ { 0 } ^ { \xi } P ( t ) \delta ( t ) d t \Big \| } \\ & { \qquad + \| \theta ( \xi ) \| + \big ( \| \delta ( \xi ) \| + \| \theta ^ { \prime } ( x ) \| \big ) ^ { 2 } \Big ) \Big ) } \end{array}
$$

with the projector $P ( t ) = I - \left( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } g _ { y } \right) \left( y ( t ) , z ( t ) \right)$ ， provided that the right hand side is sufficiently small.

Hint. Linearize Eq.(1.29) around $( y , z )$ ，extract $\widehat { z } - z$ ， and insert it into the difference of (1.28a) and (1.14a). The term $\left( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \right) \left( y ( x ) , z ( x ) \right) \theta ^ { \prime } ( x )$ can be replaced by $\begin{array} { r } { \frac { d } { d x } \Big ( f _ { z } ( g _ { y } f _ { z } ) ^ { - 1 } \big ( y ( x ) , z ( x ) \big ) \theta ( x ) \Big ) + \mathcal { O } ( | | \theta ( x ) | | ) } \end{array}$ before integration.

7. For the linear initial value problem

$$
y ^ { \prime } = A ( x ) y + f ( x ) , \qquad y ( 0 ) = 0
$$

consider the adjoint problem

Prove that

$$
\begin{array} { c } { { \displaystyle v ^ { \prime } = - A ( x ) ^ { T } v - g ( x ) , \qquad v ( 1 ) = 0 . } } \\ { { \displaystyle \int _ { 0 } ^ { 1 } g ( x ) ^ { T } y ( x ) d x = \int _ { 0 } ^ { 1 } v ( x ) ^ { T } f ( x ) d x . } } \end{array}
$$

8. Consider a linear optimal control problem with quadratic cost functional

$$
\begin{array} { c } { { y ^ { \prime } = A y + B u + f ( x ) , \qquad y ( 0 ) = y _ { 0 } } } \\ { { J ( u ) = \displaystyle { \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \left( y ( x ) ^ { T } C y ( x ) + u ( x ) ^ { T } D u ( x ) \right) d x } , } } \end{array}
$$

where $C$ and $D$ are assumed to be positive semi-definite.

a) Prove that $\boldsymbol { J } ( \boldsymbol { u } )$ is minimal if and only if

$$
\begin{array} { r l } & { y ^ { \prime } = A y + B u + f ( x ) , \qquad y ( 0 ) = y _ { 0 } } \\ & { v ^ { \prime } = - A ^ { T } v - C y , \qquad v ( 1 ) = 0 } \\ & { 0 = B ^ { T } v + D u . } \end{array}
$$

b) If $D$ is positive definite, then (1.52) has index 1.

c)If $D \approx 0$ and $B ^ { T } C B$ is positive definite, then (1.52) has index 3.

# VII.2 Index Reduction Methods

We have seen in Sect. VI.1 that the numerical treatment of problems of index 1, which are either in the half-explicit form(1.13) or in the form $M u ^ { \prime } = \varphi ( u )$ ,is not much more difficult than that of ordinary differential equations. For higher index problems the situation changes completely. This section is devoted to the study of several approaches that are all based on the idea of modifying the problem in such a way that the index is reduced.

# Index Reduction by Differentiation

The most apparent way of reducing the index is to differentiate repeatedly the algebraic constraints (see Definition 1.2). In general, it is recommended to differentiate until having obtained an index 1 problem. For example, the index 2 problem (1.14a,b) is replaced by (1.14a,c), or the constrained mechanical system (1.46a,b,c) by (1.46a,b,e). The resulting problem is then solved by the methods of Chapter VI.

We illustrate this approach at the “pendulum example"

$$
\begin{array} { c } { { x ^ { \prime } = u , \qquad u ^ { \prime } = - x \lambda } } \\ { { y ^ { \prime } = v , \qquad v ^ { \prime } = - 1 - y \lambda } } \\ { { 0 = x ^ { 2 } + y ^ { 2 } - 1 . } } \end{array}
$$

In this form it has index 3. Differentiating the algebraic constraint twice yields

$$
\begin{array} { l } { { 0 = x u + y v , } } \\ { { 0 = - \lambda ( x ^ { 2 } + y ^ { 2 } ) - y + u ^ { 2 } + v ^ { 2 } . } } \end{array}
$$

Equations (2.1a,b) together with(2.3) represent an index 1 problem. We can extract $\lambda$ from(2.3) and insert it into (2.1a,b)to get a differential equation for $x , y , u , v ,$ which can be solved by standard methods.

Drift-off Phenomenon. As an example we apply the code DOPRI5 to the index 1 problem(2.1a,b),(2.3) with initial values $x _ { 0 } = 1$ ， $y _ { 0 } = 0$ ， $u _ { 0 } = 0$ ， $v _ { 0 } = 0$ . We are interested, how well the constraints (2.1c) and (2.2) are preserved by the numerical solution. The result presented in Fig.2.1 shows that the error in the constraint (2.2) grows linearly, that in (2.1c) grows even quadratically. This phenomenon is explained as follows:

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/f052aa438cba3d426b8d7179d70c42a73a18079d1d1106160ed948deffa2f25f.jpg)  
Fig.2.1. Error in the constraints for DOPRI5 $\mathit { \Omega } ( A t o l = R t o l = 1 0 ^ { - 6 }$ ）

Consider a constrained mechanical system (see (1.46))

$$
\begin{array} { c } { q ^ { \prime } = u } \\ { { { \cal M } ( q ) u ^ { \prime } = f ( q , u ) - { \cal G } ^ { T } ( q ) \lambda } } \\ { { 0 = g ( q ) . } } \end{array}
$$

Differentiating (2.4c) twice we get

$$
\left( \begin{array} { c c } { { M ( q ) } } & { { G ^ { T } ( q ) } } \\ { { G ( q ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { u ^ { \prime } } } \\ { { \lambda } } \end{array} \right) = \left( \begin{array} { c } { { f ( q , u ) } } \\ { { - q _ { q q } ( q ) ( u , u ) } } \end{array} \right)
$$

which, together with (2.4a),is the corresponding index 1 problem. The important observation is now that the index 1 problem possesses a solution for arbitrary initial values $q _ { 0 }$ and $u _ { 0 }$ . Due to the fact that the second derivative of $g ( q ( t ) )$ vanishes (this is a consequence of the lower relation of (2.5)), the solution of the index 1 problem satisfies

$$
\begin{array} { r l } & { g \big ( \boldsymbol { q } ( t ) \big ) = g \big ( \boldsymbol { q } _ { 0 } \big ) + ( t - t _ { 0 } ) G ( \boldsymbol { q } _ { 0 } ) \boldsymbol { u } _ { 0 } , } \\ & { G \big ( \boldsymbol { q } ( t ) \big ) \boldsymbol { u } ( t ) = G \big ( \boldsymbol { q } _ { 0 } \big ) \boldsymbol { u } _ { 0 } . } \end{array}
$$

Theorem 2.1. If we apply a pth order numerical method to the index $l$ problem $( 2 . 4 a )$ ，(2.5) with consistent initial values at $t _ { 0 } = 0$ ， then the numerical solution $\left( q _ { n } , u _ { n } \right)$ at time $t _ { n }$ satisfies $( f o r \ t _ { n } - t _ { 0 } \leq C o n s t )$

$$
\begin{array} { r } { \| g ( q _ { n } ) \| \leq h ^ { p } ( A t _ { n } + B t _ { n } ^ { 2 } ) , \qquad \| G ( q _ { n } ) u _ { n } \| \leq h ^ { p } C t _ { n } . } \end{array}
$$

The value $h$ represents the maximal step size used.

Proof. Denote by $q ( t , t _ { 0 } , q _ { 0 } , u _ { 0 } )$ the solution of the index 1 problem with initial value $( \boldsymbol { q } _ { 0 } , \boldsymbol { u } _ { 0 } )$ at $t = t _ { 0 }$ . Since the local error $q _ { \jmath + 1 } - q ( t _ { j + 1 } , t _ { \jmath } , q _ { \jmath } , u _ { \jmath } )$ is of size $\mathcal { O } ( h _ { \jmath } ^ { p + 1 } )$ (and similarly for the $u$ -component),itfollows from (2.6a) that

$$
\left. \left. g \big ( q ( t _ { n } , t _ { j + 1 } , q _ { j + 1 } , u _ { j + 1 } ) \big ) - g \big ( q ( t _ { n } , t _ { j } , q _ { j } , u _ { j } ) \big ) \right. \right. \leq h _ { j } ^ { p + 1 } \big ( A + 2 B ( t _ { n } - t _ { j + 1 } ) \big ) .
$$

Adding up these inequalities from $j = 0$ to $j = n - 1$ gives the desired bound for $g ( q _ { n } )$ ,because the initial values are consistent, i.e., $g ( q ( t _ { n } , t _ { 0 } , q _ { 0 } , u _ { 0 } ) ) = 0$ . The second estimate of Theorem 2.1 is proved in the same way. □

Baumgarte Stabilization. The historically first remedy for this drift-off is due to Baumgarte (1972). Instead of replacing the constraint (2.4c) by its second time derivative,he proposes to replace (2.4c) by the linear combination

$$
0 = \ddot { g } + 2 \alpha \dot { g } + \beta ^ { 2 } g ,
$$

where ${ \dot { g } } , { \ddot { g } }$ are time derivatives of (2.4c),i.e.,

$$
g \simeq g ( q ) , \qquad \dot { g } = G ( q ) u , \qquad \ddot { g } = g _ { q q } ( q ) ( u , u ) + G ( q ) \big ( f ( q , u ) - G ^ { T } ( q ) \lambda \big ) .
$$

Eq.(2.7) together with (2.4b) determines $u ^ { \prime }$ and $\lambda$ as functions of $( q , u )$ ,and the resulting differential equation can be solved numerically. The idea is now to choose the free parameters $\alpha$ and $\beta$ in such a way that (2.7) is an asymptotically stable differential equation, e.g., $\beta = \alpha$ and $\alpha > 0$ . Consequently, the functions $g ( q ( t ) )$ and $G ( \boldsymbol { q } ( t ) ) \boldsymbol { u } ( t )$ are exponentially decreasing, in contrast to (2.6). The difficulty of this approach lies in a good choice of $\alpha$ . For small values of $\alpha$ the damping will not be sufficiently strong,whereas for large $\alpha$ the resulting differential equation becomes stiff and explicit methods are no longer efficient. A careful investigation on the choice of $\alpha$ can be found in Ascher, Chin & Reich (1994).

# Stabilization by Projection

We shall now analyze another possibility for avoiding the instability of the preceding example, namely the repeated projection of the numerical solution onto the solution manifold.

Index 2 Problems. Consider the system (1.14a,b). Suppose that $( y _ { n - 1 } , z _ { n - 1 } )$ is an approximation to the solution at time $t _ { n - 1 }$ which satisfies $g ( y _ { n - 1 } ) = 0$ and $g _ { y } ( y _ { n - 1 } ) f ( y _ { n - 1 } , z _ { n - 1 } ) = 0$ . Applying a numerical one-step method (state space form method of Sect. VI.1) with these values to the index 1 system(1.14a,c) yields an approximation $\widetilde { y } _ { n } , \widetilde { z } _ { n }$ that, in general, does not satisfy the constraint (1.14b). A natural way of projecting the approximation $\widetilde { y } _ { n }$ to the solution manifold $\mathcal { M }$ of Eq.(1.17) is along the image of $f _ { z }$ (see also the projected Runge-Kutta methods of Sect. VII.4). We therefore define $y _ { n }$ as the solution of

$$
y - \widetilde { y } _ { n } = f _ { z } ( \widetilde { y } _ { n } , \widetilde { z } _ { n } ) \mu , \qquad g ( y ) = 0 ,
$$

and then we adjust $z _ { n }$ by solving the equation $g _ { y } ( y _ { n } ) f ( y _ { n } , z _ { n } ) = 0$ Applying simplified Newton iterations to the nonlinear system (2.8) requires the decomposition of the matrix

$$
\left( \begin{array} { c c } { { I } } & { { f _ { z } ( \widetilde { y } _ { n } , \widetilde { z } _ { n } ) } } \\ { { g _ { y } ( \widetilde { y } _ { n } ) } } & { { 0 } } \end{array} \right) .
$$

Block elimination shows that the invertibility of (2.9) is a consequence of (1.10), and that only the matrix $g _ { y } f _ { z }$ has to be decomposed. Such a decomposition is usually already available from the application of the numerical method, so that the projection (2.8) is very cheap.

It is now natural to ask, whether this projection procedure can distroy the convergence properties of the underlying method. For a $p$ th order one-step method the local error is of size $\mathcal { O } ( h ^ { p + 1 } )$ . Since the solution of (1.14a,c) passing through $\left( y _ { n - 1 } , z _ { n - 1 } \right)$ satisfies $g ( y ( t ) ) = 0$ , it holds $g ( \widetilde { y } _ { n } ) = \mathcal { O } ( h ^ { p + 1 } )$ . Hence, the solution of (2.8) satisfies $\mu = \mathcal { O } ( h ^ { p + 1 } )$ ， $y _ { n } - \widetilde { y } _ { n } = \mathcal { O } ( h ^ { p + 1 } )$ ,and $z _ { n } - \widetilde { z } _ { n } = \mathcal { O } ( h ^ { p + 1 } )$ By the Implicit Function Theorem this solution depends smoothly on $( \widetilde { y } _ { n } , \widetilde { z } _ { n } )$ ,s0 that the mapping $( y _ { n - 1 } , z _ { n - 1 } ) \mapsto ( y _ { n } , z _ { n } )$ represents a $p$ th order one-step method for (1.14a,c). Convergence of order $p$ thus follows from the standard theory (see Sects.VI.1 and II.3). This proof also applies to multistep methods.

Constrained Mechanical Systems. For the index 3 system $_ { ( 2 . 4 a , b , c ) }$ the situation is slightly more complex. We assume consistent values $\left( q _ { n - 1 } , u _ { n - 1 } , \lambda _ { n - 1 } \right)$ at time $t _ { n - 1 }$ and apply a one-step method to the index 1 system (2.4a), (2.5) to obtain $\left( \widetilde { q } _ { n } , \widetilde { u } _ { n } \right)$ . Since the position constraint (2.4c) only depends on $q$ ， the projections for $q$ and $u$ can be done sequentially.

Projection on Position Constraint. We define $q _ { n }$ as solution of the nonlinear system

$$
\begin{array} { r } { M ( \widetilde { q } _ { n } ) ( q _ { n } - \widetilde { q } _ { n } ) + G ^ { T } ( \widetilde { q } _ { n } ) \mu = 0 } \\ { g ( q _ { n } ) = 0 . } \end{array}
$$

Projection on Velocity Constraint. With the value $q _ { n }$ obtained from the above projection we let $u _ { n }$ be the solution of

$$
\begin{array} { r } { M ( q _ { n } ) ( u _ { n } - \widetilde { u } _ { n } ) + G ^ { T } ( q _ { n } ) \mu = 0 } \\ { G ( q _ { n } ) u _ { n } \qquad = 0 . } \end{array}
$$

Lubich (1991） introduced this kind of projection, because “it is invariant under affine transformations of coordinates". We remark that the system (2.11) is linear, whereas (2.1O) is nonlinear and has to be solved by (simplified) Newton iterations. The index 3 assumption that the matrix in Eq.(2.5) is invertible,implies the existence of the projected values $q _ { n }$ and $u _ { n }$ (at least for sufficiently small step size). It is possible to alter slightly the arguments of $M$ and $G ^ { T }$ in the upper lines of (2.10) and (2.11) or to solve the system (2.11) iteratively,if this is computationally advantageous. Convergence of this method is proved in the same way as in the index 2 case.

Velocity Stabilization. It can be seen from (2.6) that errors in the velocity constraint $G ( q ) u = 0$ are more critical for the numerical solution than errors in the position constraint $g ( q ) = 0$ . It is therefore interesting to study the method, where the numerical solution is projected only to the velocity constraint. Alishenas & Olafsson (1994) come to the conclusion that “velocity projection is the most efficient projection with regard to improvement of the numerical integration".

We have applied the code DOPRI5 in four different variants to the index 1 formulation of the pendulum equation (2.1): (i) standard application without any pro-jection,(ii) only projection on the position constraint, (iii) only projection on the velocity constraint,(iv) sequential position and velocity projections. The the global error (in position and velocity) during integration is shown in Fig.2.2. We conclude that a projection on the position constraint without projection on the velocity constraint does not improve the global error (it makes it even worse in our example). On the other hand, velocity stabilization is as efficient as the complete projection (position and velocity). Nearly no difference can be observed in Fig.2.2.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/1a7a22670a2fe9dac27741d160191fe4d44bacf3d5c38b1367162ef0d4c28b26.jpg)  
Fig.2.2. Global error of DOPRI5 with various projections $\mathit { \Omega } ( A t o l = R t o l = 1 0 ^ { - 6 }$ ）

# Differential Equations with Invariants

Closely related to the above techniques is the numerical treatment of differential equations with invariants. Consider the initial value problem

$$
y ^ { \prime } = f ( y ) , \qquad y ( 0 ) = y _ { 0 } ,
$$

and suppose that the solution is known to have the invariant

$$
\varphi ( y ) = 0 .
$$

For example, the differential equation (1.46a,e) for $( q , u )$ has the invariants (1.46c) and (1.46d). Conservation laws (total energy,...） may also be written in the form (2.13). The invariant (2.13) is called a frst integral, if $\varphi _ { y } ( y ) f ( y ) \equiv 0$ in a neighbourhood of the solution.

Linear first integrals of the form $\varphi ( y ) = c + d ^ { T } y$ are preserved exactly by most integration methods (e.g., Runge-Kutta and multistep methods). Quadratic first integrals are preserved exactly by symplectic Runge-Kutta methods (see Theorem II.16.7). More complicated invariants are in general not preserved.

The above projection techniques can be adapted to the treatment of the problem (2.12-13) (see Shampine (1986),Eich (1993),Ascher, Chin & Reich (1994)).We apply a numerical method to (2.12) and project (orthogonally or somehow else) the numerical solution onto the manifold defined by (2.13). As discussed above, this precedure retains the order of convergence of the basic method.

Hamiltonian Systems. Differential equations of the form

$$
p _ { \ i } ^ { \prime } = - \frac { \partial H } { \partial q _ { \ i } } ( p , q ) , \qquad q _ { \ i } ^ { \prime } = \frac { \partial H } { \partial p _ { \ i } } ( p , q ) , \qquad i = 1 , \ldots , n ,
$$

where $\displaystyle H : \mathbb { R } ^ { 2 n }  \mathbb { R }$ is a smooth function, always have ${ \cal H } ( p , q ) = C o n s t$ as first integral. It is tempting to exploit this information and project the numerical solution

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0007_pages_0421-0490/auto/images/6ae6d227259038adb5c9f0f5153bcd6ae4a551bdc1c28b3cb349e1ddced4f7a3.jpg)  
Fig. 2.3. Study of the projection onto the manifold ${ \cal H } ( p , q ) = { \cal H } ( p _ { 0 } , q _ { 0 } )$

onto the manifold $H ( p , q ) = H ( p _ { 0 } , q _ { 0 } )$ . Consider for example the perturbed Kepler problem with Hamiltonian

$$
H ( p , q ) = { \frac { p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } } { 2 } } - { \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } } - { \frac { 0 . 0 0 5 } { \sqrt { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 } } } }
$$

and initial values $q _ { 1 } ( 0 ) = 1 - e$ ， $q _ { 2 } ( 0 ) = 0$ ， $p _ { 1 } ( 0 ) = 0$ ， $p _ { 2 } ( 0 ) = \sqrt { ( 1 + e ) / ( 1 - e ) }$ (eccentricity $e = 0 . 6 { \dot { } } ,$ ). The upper pictures of Fig. 2.3 show the numerical solution obtained by the explicit Euler method with step size $h = 0 . 0 1$ ; to the left without any projection, and to the right with projection onto ${ \cal H } = C o n s t$ . An improvement can be observed, but the numerical solution still does not reflect the geometric structure of the exact solution (invariant torus). We also have applied the symplectic Euler method (see Eq.(16.54) of Sect.II.16). Here we see that the numerical


<!-- chunk 0008: pages 491-560 -->
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/6b025fd7372a6dd16bb5dfccd21469987d11cef90f6f677210b182ec096a843c.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/346d66a008600ce0750ded0f00dfd0d1e07af370f88a90173282f2f655e1cee8.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/375f6d4584a4f080378c04a63f99e30dc88df46a561a44434f13982aab39aeab.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/310b74d6baaee9773caa2cfee6bbf9b3dfba542279d390d182c6c758543e75a9.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/b75eb35d6acff8e322490213750065847dcbedf55c825f227ffbb616fa7da3b2.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/f2ccc2acc7fbaec4fde51ded20a75e8ec38d1b47ccd0acfb4a87754c5eedd9ba.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/96ec3de1a960722e255b5798af0249cdcbd6393cc28929c19622d12e5f687de7.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0008_pages_0491-0560/auto/images/fcfde105d43e3c313b38836b53a142d32ecbd7d9902c5e9603bd06f23bd61fa7.jpg)  
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


<!-- chunk 0009: pages 561-630 -->
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0009_pages_0561-0630/auto/images/4128e888c699c9dbe2616e1a8e79db12d45419090ad506f23d043a021308ce21.jpg)  
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

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0009_pages_0561-0630/auto/images/e6347f32732f8e7543a27890fffa4a0c1286d144ca48ab6e86a5c4929655aca9.jpg)

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


<!-- chunk 0010: pages 631-631 -->
of DAE solutions,411. of index 2 RK solution, 510f.   
Taylor series method, 261.   
Tchébychef,see Chebyshev.   
test problems, 144f.   
theorem of von Neumann, 168, 330.   
$\theta$ -method, 42, 50.   
threshold factor, 176, 179.   
transient phase,2.   
transistor amplifier, 376f, 379.   
trapezoidal rule,45, 131,185,234, 247, 306, 357.   
trees for ODE,92,105. for index 1 DAE,409f. for index 2 DAE, 507. for W -methods, 115. monotonically labelled, 105, 411, 509.   
underlying ODE, 455,478.   
uniqueness of multistep solutions,306f,482.

of RK solutions,219, 397. van der Houwen & Sommeijer's approach, 35. van der Pol's equation,4-5, 144,372,403, 406, 566. Vandermonde matrix, 78. VDPOL, 144,153f, 159,300f. velocity level, 464. velocity stabilization, 471. VODE,301f. Volterra-Lotka model, 556. von Neumann's theorem,168,330. $V$ -transformation, 78. W -methods, 114, 136. weak $A N$ -stability, 360. weak instability, 245. Weierstrass-Kronecker form, 452. work-precision diagram, 154f, 159f,301f,537 539. W -transformation, 77f, 183f.
