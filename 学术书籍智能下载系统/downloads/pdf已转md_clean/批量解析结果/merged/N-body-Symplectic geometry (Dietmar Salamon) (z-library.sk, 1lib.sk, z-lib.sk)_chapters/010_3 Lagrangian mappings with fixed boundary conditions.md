# 3 Lagrangian mappings with fixed boundary conditions

Proposition 4 leads us to the following auxiliary problem of the classification of Lagrangian mappings with fixed boundary conditions. Consider a diagram:

$$
\begin{array} { l c l } { { L ^ { \prime } \hookrightarrow } } & { { T _ { \Gamma } ^ { * } M } } & { { \to } } & { { \Gamma } } \\ { { \ \cap } } & { { \ \cap } } & { { \ \cap } } \\ { { \ L \hookrightarrow } } & { { T ^ { * } M } } & { { \to } } & { { M , } } \end{array}
$$

where $\Gamma , M , L ^ { \prime }$ are fixed smooth manifolds, $\mathbf { r }$ being given by the equation $q _ { 1 } = 0 , L ^ { \prime }$ being taken from Proposition 4 and $\pmb { L }$ being a Lagrangian submanifold containing $\pmb { L ^ { \prime } }$ as a submanifold.

Theorem ${ \pmb 6 }$ A generic Lagrangian submanifold $\pmb { L }$ in the class of Lagrangian submanifolds containing $L ^ { \prime }$ may be reduced by means of a Lagrangian equivalence of $\pmb { T } ^ { * } \pmb { M }$ preserving $\mathbf { r }$ to a form with one of the following generating families (the equation for $\mathbf { r }$ is $\pmb q _ { 1 } = 0$ ：

$a A : B _ { k } : F ( x , q ) = x ^ { k + 1 } + q _ { k } x ^ { k } + . . . + q _ { 2 } x ^ { 2 } + q _ { 1 } x ;$ ${ \pmb a } { \pmb B } : { \bf A }$ generic such germ can be reduced to the form

$$
F ( x , y , q ) = x ^ { 3 } + y ^ { 2 } + q _ { 2 } x + q _ { 1 } y ;
$$

A set of such germs of codimension 1 can be reduced to the form

$$
F ( x , y , q ) = x ^ { 3 } + x y ^ { 2 } + q _ { 3 } y ^ { 2 } + q _ { 2 } x + q _ { 1 } y .
$$

All the other germs have higher codimension;

$$
b A : D _ { k } : F ( x , q ) = x ^ { 2 } y + y ^ { k - 1 } + q _ { k - 1 } y ^ { k - 2 } + . . . + q _ { 2 } y + q _ { 1 } x .
$$

# Proof.aA Because

$$
T _ { 0 } L \subset ( T _ { 0 } L ^ { \prime } ) ^ { \bot } = \operatorname { S p a n } \langle \partial / \partial p _ { 1 } , \partial / \partial q _ { 1 } , \ldots , \partial / \partial q _ { n } \rangle ,
$$

we can choose either $( q _ { 1 } , \ldots , q _ { n } )$ or $\left( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } \right)$ as coordinates on $\pmb { L }$ In the first case there is no singularity of the projection of $\pmb { L }$ onto $\pmb { M }$ ,and $\pmb { L }$ can be brought to the normal form $p _ { 1 } = . . . = p _ { n } = 0$ 、In the second case there exists a generating function $S ( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } )$ such that $\pmb { L }$ is given by the equations

$$
q _ { 1 } = - \frac { \partial S } { \partial p _ { 1 } } , \quad p _ { 2 } = \frac { \partial S } { \partial q _ { 2 } } , \quad \ldots , \quad p _ { n } = \frac { \partial S } { \partial q _ { n } } .
$$

The condition $L ^ { \prime } \subset L$ gives rise to the following: all the partial derivatives of $s$ are known at the hypersurface ${ \mathfrak { p } } _ { 1 } = 0$ of the space of parameters (namely, they are equal to zero). This implies that $s$ is of the form

$$
S = p _ { 1 } ^ { 2 } \cdot \varphi ( p _ { 1 } , q _ { 2 } , \ldots , q _ { n } ) ,
$$

where $\varphi$ is a germ of some function. Hence $\pmb { L }$ is given by the generating family

$$
F ( x , q ) = S ( x , q _ { 2 } , \ldots , q _ { n } ) + x q _ { 1 } = x ^ { 2 } \varphi ( x , q _ { 2 } , \ldots , q _ { n } ) + x q _ { 1 } .
$$

Consequently for a generic $\varphi$ the function $f ( x ) = F ( x , 0 )$ is of the type $\pmb { A } _ { k }$ for some $\pmb { k }$ ，and $\pmb { F }$ is a versal deformation of $\pmb { f }$ ，which is $\mathbf { R } _ { + }$ -equivalent to the family

$$
F ( x , q ) = x ^ { k + 1 } + q _ { k - 1 } x ^ { k - 1 } + \ldots + q _ { 2 } x ^ { 2 } + q _ { 1 } x .
$$

Because we can only make transformations of the $\pmb q$ variables preserving $q _ { 1 } = 0$ , indeed we may only reduce the family to the form

$$
F ( x , q ) = x ^ { k + 1 } + q _ { k } x ^ { k } + \dots + q _ { 2 } x ^ { 2 } + q _ { 1 } x .
$$

Analogous calculations in the cases $\pmb { a } \pmb { B }$ and $\pmb { b } \pmb { A }$ show that the generating family may be chosen in the form

$$
\begin{array} { r } { a B : F ( x , y , q ) = x ^ { 3 } + x q _ { 2 } + y q _ { 1 } + y ^ { 2 } \varphi ( x , y , q _ { 3 } , \dots , q _ { n } ) ; } \\ { b A : F ( x , y , q ) = x ^ { 2 } y + x q _ { 2 } + y q _ { 1 } + y ^ { 2 } \varphi ( x , y , q _ { 3 } , \dots , q _ { n } ) . } \end{array}
$$

Standard classification theorems of critical point theory show that these families are versal deformations of the corresponding functions and $\pmb { \mathrm { R } } _ { + }$ equivalent to the families given in the theorem. Moreover,a reduction to the normal form may be made by means of changes of the variables $\pmb q$ preserving $q _ { 1 } = 0$ .□

The case $b B$ which is not considered in Theorem 6 is much more complicated. In this case (and in the more general cases) the generating family is not a versal deformation. Calculations show that the generating family in this case is of the form

$$
\begin{array} { r } { F ( x , q ) = \frac { 1 } { 6 } x ^ { 6 } + \frac { 1 } { 4 } x ^ { 4 } q _ { 3 } + \frac { 1 } { 2 } x ^ { 2 } q _ { 2 } + ( x ^ { 4 } + q _ { 3 } x ^ { 2 } + q _ { 2 } ) ^ { 2 } \varphi ( x , q _ { 2 } , \dots , q _ { n } ) + x q _ { 1 } . } \end{array}
$$

We are interested in the problem,to which form this family may be brought by means of $\mathbf { R } _ { + }$ -transformations. Even if we are not interested in the Lagrangian sub-manifold itself but only in its caustic,the problem is to which simplest form a germ of the family

$$
\frac { \partial F } { \partial x } = ( x ^ { 4 } + x ^ { 2 } q _ { 3 } + q _ { 2 } ) [ x + ( 8 x ^ { 3 } + 4 q _ { 3 } x ) \varphi + ( x ^ { 4 } + q _ { 3 } x ^ { 2 } + q _ { 2 } ) \varphi ^ { \prime } ] + q _ { 1 }
$$

may be brought by means of a $V$ -equivalence.

If we could bring this family to the same form with $\varphi = 0$ , we would have obtained a “symmetric butterfly” (fg.5,see [4]) but we cannot guarantee this.

Proof of Theorem 1. According to condition $( * )$ the manifold $L _ { 2 }$ is known to be contained in the level surface $H _ { 2 }$ of the Hamiltonian $h _ { 2 }$ .We can obtain any small perturbation of ${ \bf { { L } } } _ { 2 }$ by means of a corresponding perturbation of $H _ { 2 }$ . So we may assume ${ \pmb L } _ { 2 }$ to be in general position and make use of Theorem 6. However, the condition of convexity of the Hamiltonian implies a prohibition of some singularities from Theorem 6. Namely, if there is no complete intersection then the characteristics of $H _ { 2 }$ are transversal to the boundary $T _ { \Gamma } ^ { * } M$ .This means that ${ \pmb L } _ { 2 }$ is transversal to $T _ { \Gamma } ^ { * M }$ as well. From the list of Theorem 6 this condition is satisfied only by the simplest singularities: $F = x ^ { 2 } + x q _ { 1 }$ (the caustic is absent） in the case $\pmb { a } \pmb { A }$ and $F = x ^ { 3 } + y ^ { 2 } + q _ { 2 } x + q _ { 1 } y$ (the caustic is smooth and transversal to the boundary） in the case $\pmb { a } \pmb { B }$ ，

At the points of complete reflection $\mathbf { { { L } _ { 2 } } }$ may not be (and indeed is not) transversal to the boundary,and of all the singularities described in Theorem 6,only the case $\pmb { B } \pmb { a }$ may occur,which completes the proof.□

# References

[1] Arnold V.I., Critical points of functions and classifcation of functics, Uspechi math. nauk, v.29,1974,2,11-49 (in Russian).   
[2] Arnold V.I, Gusein-Zade, S.M. and Varchenko,A.N., Singularities of differentiable maps,I,Birkhauses,Boston,1985.   
[3] Janeczko,S.and Kowalczyk,A., Classification of generic 3-dimentional Lagrangian singularities with $( Z _ { 2 } ) ^ { 1 }$ -symmetries, preprint (1988).

[4] Janeczko, S.and Roberts,R.M., Classification of symmetric caustics I: Symplectic equivalence,in “Singularity theory and Applications,Warwick 1989,Part II" edited by R.M. Robert and I.N. Stewart, LNM1463, Springer-Verlag,Heidelberg,Berlin,1991,pp.193-219.

[5] Nye, J.F.,The catastrophe optics of liquid drop lenses, Proc. R. Soc. London A403 (1986),27-50.

[6] Zakalyukin, V.M., On Lagrangian and Legendrean singularities, Funct. anal.i pril.,1976,10,1,26-36.

# Examples of Singular Reduction

Eugene Lerman Richard Montgomery Reyer Sjamaar

Mathematisch Instituut der Rijksuniversiteit te Utrecht \* PO Box 80.010,3508 TA Utrecht,The Netherlands

January 1991

# Introduction

The construction of the reduced space for a symplectic manifold with symmetry,as formalized by Marsden and Weinstein [13],has proved to be very useful in many areas of mathematics ranging from classical mechanics to algebraic geometry. In the ideal situation, which requires the value of the moment map to be weakly regular,the reduced space is again a symplectic manifold.A lot of work has been done in the last ten years in the hope of finding a ‘correct' reduction procedure in the case of singular values. For example, Arms, Gotay and Jennings describe several approaches to reduction in [4]. At some point it has also been observed by workers in the field that in all examples the level set of a moment map modulo the appropriate group action is a union of symplectic manifolds.Recently Otto has proved that something similar does indeed hold,namely that such a quotient is a union of symplectic orbifolds [16]. Independently two of us,R. Sjamaar and E. Lerman,have proved a stronger result [21]. We proved that in the case of proper actions the reduced space, which we simply took to be the level set modulo the action, is a stratifed symplectic space. Thereby we obtained a global description of the possible dynamics,a procedure for lifting the dynamics to the original space and a local characterization of the singularities of the reduced space. (The precise definitions will be given below.） The goal of this paper is twofold. First of all, we would like to present a number of examples that illustrate the general theory. Secondly, in computing the examples we have noticed that many familiar methods for computing reduced spaces work nicely in the singular situations. For instance,in the case of a lifted action on a cotangent bundle the reduced space at the zero level is the‘cotangent bundle' of the orbit space.And in some cases the reduced space can be identified with the closure of a coadjoint orbit.
