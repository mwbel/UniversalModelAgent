# FOURTH-ORDER SYMPLECTIC INTEGRATION\*

Etienne FOREST Lawrence Berkeley Laboratory,Berkeley,CA 94720,USA

and

Ronald D.RUTH Stanford Linear Accelerator Center,Stanford University,Stanford, CA 94309,USA

Received 24 August 1989 Revised manuscript received 20 November 1989 Communicated by J. Guckenheimer

Inthis paper we presentanexplicit fourth-order method for the integrationof Hamilton's equations.This method preserves thepropertythat thetimeevolutionofsuchasystemyieldsacanonical ransformationfromthe initialconditions to thefinal state.Thatis,theintegrationstepisan explicitsymplectic map.Although theresultisfirstderivedforaspecific type of Hamiltonian,it is shown to be quite general.In particular,the resultscan be applied to any Lie group.

# 1. Introduction

There are many different ways to integrate differential equations numerically. These various methods are usually characterized by the accuracyof a single step in time (the independent variable).Thus if in a small time step $\pmb { h }$ the integration is performed so that it is accurate through order $h ^ { k }$ ,then the method is referred to as a $\pmb { k }$ th-order integration method.

The class of differential equations of interest here is that in which the equations are derivable from a Hamiltonian. The exact solution of such a system of diffrential equations leads to a symplectic map from the initial conditions to the present state of the system. However,a characteristic feature of most high-order $( k > 2 )$ integration methods is that they are not exactly symplectic. One manifestation of this is that the determinant of the Jacobian of the transformation for one time step difers slightly from unity, and thus the system will be damped or excited artificially.In many applications the salient features of the solutions appear only after long times or large numbers of iterations; in these applications spurious damping or excitation may lead to misleading results.

The purpose of this paper is to develop an explicit fourth-order symplectic map (a fourth-order integration step which preserves exactly the canonical character of the equations of motion).For a typical numerical integration this method can be used to eliminate noncanonical effects while providing the accuracy of a fourth-order integration step.In addition there is another way of viewing this approach. If we iterate any explicit integration step whether canonical or not, eventually the absolute error in the coordinates and the momenta gets large. In cases where the integration step is not symplectic,and in which spurious damping or antidamping occurs, $\pmb { x }$ and $\pmb { p }$ either settle onto some fixed point or diverge roughly exponentially. If the map is symplectic, this does not happen.We have observed that a symplectic integration step with a suffciently small step size generates a phase space portrait which is close to that of the original system, however, with errors in“phase” which add up after many iterations to yield large absolute errors in $x$ and $\pmb { p }$ when compared with the exact solution of the differential equation.

Therefore in the symplectic case it is possible and sometimes attractive to replace the diffrential equation by a symplectic map.This map then becomes a model for the system in question and so can be iterated as much as we like. When viewed in this way,a fourth-order integration step becomes a method for modeling a differential equation with a map.The closeness of the model to the differential equation can be controlled with the step size. Nonsymplectic integration methods cannot be used as models for symplectic problems,and the iterations must be stopped before the solution deviates very far from the exact solution of the differential equations.

Before proceeding we would like to mention that the method described here was circulated privately by us several years ago and is now used routinely in several computer programs which trace the trajectories of particles in particle accelerators.

# 2. The problem

Consider a system of differential equations governed by the Hamiltonian

$$
H = A { \bigl ( } p { \bigr ) } + V { \bigl ( } x { \bigr ) } .
$$

Thus the equations of motion are given by

$$
\mathrm { d } x / \mathrm { d } t = \partial H / \partial p , \qquad \mathrm { d } p / \mathrm { d } t = - \partial H / \partial x .
$$

In the equations above the bold face $\pmb { x }$ and $\pmb { p }$ are $\pmb { n }$ -dimensional vectors of the coordinates and momenta,respectively,and $t$ is the independent variable. Although the above Hamiltonian is explicitly indepedent of time, it is general enough to take care of the case of a time-dependent potential. In the time-dependent case,if we have a Hamiltonian given by

$$
H _ { 1 } = A ^ { \prime } { \left( \begin{array} { l } { p } \end{array} \right) } + V ^ { \prime } { \left( \begin{array} { l } { x , t } \end{array} \right) } ,
$$

then we can use another independent variable $\pmb { \tau }$ and replace the time-dependent problem with the following $\pmb { \tau }$ independent problem:

$$
H = A ^ { \prime } ( \textbf { \em p } ) + p _ { n + 1 } + V ^ { \prime } \big ( \textbf { \em x } , x _ { n + 1 } \big ) ,
$$

which is of the same form as eq. (2.1). In this case the solution of Hamilton's equations for $x _ { n + 1 }$ yields $x _ { n + 1 } = \tau$ Thus $x _ { n + 1 }$ is just constrained to be the independent variable.

The solution of the equations of motion in (2.2) is given by the functions

$$
x \big ( x _ { 0 } , p _ { 0 } , t \big ) , \qquad p \big ( x _ { 0 } , p _ { 0 } , t \big ) ,
$$

where $\pmb { x _ { 0 } }$ and ${ \pmb p _ { 0 } }$ are the initial conditions at time $\pmb { t = 0 }$ . Due to the canonical character of the equations of motion,eq.(2.5) is a canonical transformation (or a symplectic map) from the initial conditions to the

state at time t. Let us denote this map by $M ( t )$ such that

$$
\begin{array} { r } { \big ( \boldsymbol { x } , \boldsymbol { p } \big ) = M \big ( t \big ) \big ( \boldsymbol { x } _ { 0 } , \boldsymbol { p } _ { 0 } \big ) . } \end{array}
$$

We would like to find a symplectic map $M _ { k } ( t )$ which approximates $M ( t )$ through order $t ^ { k }$ Thus the difference between the two maps will be of order $t ^ { k + 1 }$ ；

$$
\lVert M ( t ) - M _ { k } ( t ) \rVert = \mathcal { O } \big ( t ^ { k + 1 } \big ) .
$$

The method for calculating $M _ { k } ( t )$ is presented in section 3.

# 3. The method of successive canonical transformations

In this section the basic approach to find $M _ { k } ( t )$ will be successive canonical transformations. If we perform the transformations in eq. (2.6) so that $\pmb { H }$ is expressed in terms of the initial conditions,then the equations of motion are

$$
\mathrm { d } x _ { 0 } / \mathrm { d } t = 0 , \qquad \mathrm { d } p _ { 0 } / \mathrm { d } t = 0 ,
$$

or the new Hamiltonian $H ^ { \prime }$ is identically zero or at least independent of $\pmb { x } _ { 0 }$ and ${ \pmb p _ { 0 } }$

This suggests that we perform canonical transformations in such a way as to make $\pmb { H }$ vanish through some order in $t .$ Let us assume that we succeed through order $t ^ { k - 1 }$ ； that is,we perform the canonical transformation

$$
( \begin{array} { c } { { { \pmb x } } } \\ { { { \pmb p } } } \\ { { { \pmb H } } } \end{array} )  ( \begin{array} { c } { { { \pmb x } ^ { \prime } } } \\ { { { \pmb p } ^ { \prime } } } \\ { { { \pmb H } ^ { \prime } } } \end{array} )
$$

such that

$$
H ^ { \prime } \left( x ^ { \prime } , p ^ { \prime } , t \right) = \mathcal { O } \left( t ^ { k } \right) .
$$

Then the solutions for the equations of motion are

$$
\begin{array} { r } { x ^ { \prime } = x _ { 0 } + \mathcal { O } \big ( t ^ { k + 1 } \big ) , \qquad p ^ { \prime } = p _ { 0 } + \mathcal { O } \big ( t ^ { k + 1 } \big ) , } \end{array}
$$

where $\pmb { x _ { 0 } }$ and ${ \pmb { p } } _ { \pmb { 0 } }$ are constants. This means that the new coordinates and momenta differ from the initial conditions at order $t ^ { k + 1 }$ . Thus if $\mathbf { \Delta } \mathbf { x } ^ { \prime }$ and $\pmb { p } ^ { \prime }$ are used as initial conditions and if we calculate $\pmb { x }$ and $\pmb { p }$ by inverting thetransformationineq.(3.2),theeror introduced isofder $t ^ { k + 1 }$ . Therefore, $\pmb { x }$ and $\pmb { p }$ are accurate through order $t ^ { k }$ . So in order to calculate $M _ { k } ( t )$ , we must perform a canonical transformation (or a sequence of them) so that the new Hamiltonian is of order $t ^ { k }$

A canonical transformation is performed with the aid of a generating function. There are diferent types of these, but for this section it is useful to use a generating function which is a function of the new coordinates and the old momenta. Let us consider the map $( { \pmb x } , { \pmb p } ) \mapsto ( { \pmb x } ^ { \prime } , { \pmb p } ^ { \prime } )$ . The generating function is given by [1]

$$
F _ { 3 } ( x ^ { \prime } , p , t ) = - x ^ { \prime } \cdot p + G \big ( x ^ { \prime } , p , t \big ) ,
$$

while the transformation equations are

$$
\begin{array} { r l } & { \mathbf { \boldsymbol { x } } = - \partial F _ { 3 } / \partial p = \mathbf { \boldsymbol { x } } ^ { \prime } - G _ { p } \big ( \mathbf { \boldsymbol { x } } ^ { \prime } , \mathbf { \boldsymbol { p } } , t \big ) , } \\ & { \mathbf { \boldsymbol { \mathsf { I } } } } \\ & { \mathbf { \boldsymbol { p } } ^ { \prime } = - \partial F _ { 3 } / \partial \mathbf { \boldsymbol { x } } = p - G _ { x } \big ( \mathbf { \boldsymbol { x } } ^ { \prime } , \mathbf { \boldsymbol { p } } , t \big ) , } \\ & { \mathbf { \boldsymbol { H } } ^ { \prime } = H + \partial F _ { 3 } / \partial t = H + G _ { t } , } \end{array}
$$

where boldface subscripts have been used to denote the gradient operation and lightface subscripts denote partial derivatives. Thus, the generating function difers from the identity by the function $G ( x ^ { \prime } , p , t )$ .In order to construct an explicit fourth-order symplectic integration step,it will be necessary to use several such transformations in sequence as in ref.[2].To illustrate the technique,it is useful to consider first a low-order symplectic integration step.By examining eq. (3.8), a good first choice for a generating function is

$$
G = - H ( \boldsymbol { p } , \boldsymbol { x } ^ { \prime } ) t = - \left[ \boldsymbol { A } ( \boldsymbol { p } ) + V ( \boldsymbol { x } ^ { \prime } ) \right] t ,
$$

which yields the transformation equations

$$
\pmb { p } ^ { \prime } = \pmb { p } + V _ { x } \big ( \pmb { x } ^ { \prime } \big ) \pmb { t } , \qquad \pmb { x } = \pmb { x } ^ { \prime } + A _ { p } \big ( \pmb { p } \big ) \pmb { t } .
$$

Substituting into the Hamiltonian we find

$$
\begin{array} { r l } & { H ^ { \prime } = V \big ( { x } ^ { \prime } + t A _ { p } \big ( p ^ { \prime } - V _ { x } \big ( { x } ^ { \prime } \big ) t \big ) \big ) - V \big ( { x } ^ { \prime } \big ) } \\ & { } \\ & { \qquad \simeq t V _ { x } \big ( { x } ^ { \prime } \big ) \cdot A _ { p } \big ( p ^ { \prime } \big ) + \mathcal { O } \big ( t ^ { 2 } \big ) , } \end{array}
$$

where we have expanded for small $t$ Since $H ^ { \prime }$ is of order $t$ ,the right-hand sides of Hamilton's equations are also of order t. Therefore, the solution is

$$
x ^ { \prime } = \mathrm { c o n s t . } + { \mathcal O } \left( t ^ { 2 } \right) , \qquad p ^ { \prime } = \mathrm { c o n s t . } + { \mathcal O } \left( t ^ { 2 } \right) .
$$

Therefore, if $( \pmb { x } ^ { \prime } , \pmb { p } ^ { \prime } )$ are interpreted as initial conditions and eq. (3.10) is used to calculate $( { \pmb x } , { \pmb p } )$ at some small time $t$ ,the error introduced is of order $t ^ { 2 }$ .Thus,this approach has yielded a first-order symplectic map, $M _ { 1 } ( t )$

Note that in eq. (3.10) we must invert the momentum equation, that is,we must express $\pmb { p }$ as a function of $\mathbf { \Delta } \mathbf { x } ^ { \prime }$ and $\pmb { p } ^ { \prime }$ .With the particular Hamiltonian shown, this inversion is trivial; however,for more general Hamiltonians one must solve the resulting implicit equation numerically [3,4]. The requirement of the special form of $\pmb { H }$ shown in eq. (2.1) will be partly removed in section 5, where a more general approach is shown.

# 4. Fourth-order symplectic integration

To proceed to higher order one can take several approaches. The most obvious choice is to proceed in a way analogous to a Runge and Kutta integration step; that is, to construct a sequence of maps with coeffcients which are adjusted to satisfy Hamilton's equations. This is the approach taken in ref. [2] to derive general second- and third-order symplectic integration steps. The general form is taken from eq. (3.10),

$$
\begin{array} { l } { { p _ { i + 1 } = p _ { i } - c _ { i } t V _ { x } ( x _ { i } ) , } } \\ { { \ } } \\ { { x _ { i + 1 } = x _ { i } + d _ { i } t A _ { p } ( p _ { i + 1 } ) , } } \end{array}
$$

for $\pmb { i } = \mathbf { 0 }$ to $\pmb { N }$ and where $( x _ { 0 } , p _ { 0 } )$ are the initial conditions,and $( { \pmb x } _ { N } , { \pmb p } _ { N } ) = ( { \pmb x } , { \pmb p } )$ are the values of the coordinates and momenta after time step t. Note that the momenta after any given sub-step must be evaluated first followed by the coordinates after that sub-step.The fullintegration step is the complete sequence of maps; intermediate values of $( x , p )$ at the sub-steps are merely for convenience and should not be interpreted as physical values.

The procedure for finding the coeficients consists of substituting the sequence of canonical transformations to evaluate the new Hamiltonian. Because the new Hamiltonian is in terms of the initial conditions, the transformations are applied in the reverse of the order shown in eq. (4.1). That is, $( \pmb { x } , \pmb { p } ) \mapsto$ $( { \pmb x } _ { N - 1 } , { \pmb p } _ { N - 1 } ) \mapsto ( { \pmb x } _ { N - 2 } , { \pmb p } _ { N - 2 } ) \mapsto . . . \mapsto ( { \pmb x } _ { 0 } , { \pmb p } _ { 0 } )$ .The final Hamiltonian is then a function of $( \pmb { x _ { 0 } } , \pmb { p _ { 0 } } )$ and the undetermined coeffcients. We determine the coefficients by requiring that the Hamiltonian be zero through some order in t. For example for $N \Leftarrow 2$ we can find $M _ { 2 } ( t )$ with the following coefficients [2]:

$$
\begin{array} { r } { c _ { 1 } = 0 , \qquad d _ { 1 } = \frac { 1 } { 2 } , \qquad c _ { 2 } = 1 , \qquad d _ { 2 } = \frac { 1 } { 2 } . } \end{array}
$$

For $N = 3$ we can find $M _ { 3 } ( t )$ provided the six coeffcients satisfy the following five equations:

$$
\begin{array} { r l } & { c _ { 1 } + c _ { 2 } + c _ { 3 } = 1 , } \\ & { d _ { 1 } + d _ { 2 } + d _ { 3 } = 1 , } \\ & { c _ { 2 } d _ { 1 } + c _ { 3 } \big ( d _ { 1 } + d _ { 2 } \big ) = \frac 1 2 , } \\ & { c _ { 2 } d _ { 1 } ^ { 2 } + c _ { 3 } \big ( d _ { 1 } + d _ { 2 } \big ) ^ { 2 } = \frac 1 3 , } \\ & { d _ { 3 } + d _ { 2 } \big ( c _ { 1 } + c _ { 2 } \big ) ^ { 2 } + d _ { 1 } c _ { 1 } ^ { 2 } = \frac 1 3 . } \end{array}
$$

A possible solution is given by [2]

$$
\begin{array} { l l } { { c _ { 1 } = \frac { 7 } { 2 4 } , } } & { { \quad c _ { 2 } = \frac { 3 } { 4 } , } } & { { \quad c _ { 3 } = - \frac { 1 } { 2 4 } , } } \\ { { { } } } & { { { } } } \\ { { d _ { 1 } = \frac { 2 } { 3 } , } } & { { \quad d _ { 2 } = - \frac { 2 } { 3 } , } } & { { \quad d _ { 3 } = 1 . } } \end{array}
$$

For the case of $N = 4$ , it is possible to find $M _ { 4 } ( t )$ . In this case there are 8 equations with 8 unknowns. These are rather tedious to write out in full detail. As an example we give a few of the relations:

$$
\begin{array} { r l } &  \begin{array} { r l } & { \eta _ { 1 } + \theta _ { 2 } - \theta _ { 3 } + \theta _ { 4 } } \\ & { \frac { 1 } { 2 } ( \sin \theta _ { 2 } + \theta _ { 3 } + \theta _ { 4 } ) } \\ & { \frac { 1 } { 2 } ( \sin \theta _ { 3 } + \theta _ { 4 } ) ^ { 2 } + \theta _ { 4 } + \theta _ { 5 } + 2 \theta _ { 6 } + 2 \theta _ { 6 } + \theta _ { 7 } - 2 \theta _ { 4 } + \theta _ { 4 } + \theta _ { 5 } + 2 \theta _ { 4 } + \theta _ { 6 } } \\ & { + \frac { 1 } { 2 } ( \sin \theta _ { 3 } + \theta _ { 4 } ) ^ { 2 } + \theta _ { 6 } + \theta _ { 7 } + 2 \theta _ { 6 } + \theta _ { 7 } + 2 \theta _ { 6 } + \theta _ { 7 } + 2 \theta _ { 6 } + \theta _ { 7 } + 2 \theta _ { 6 } + \theta _ { 7 } } \\ & { - 2 4 \theta _ { 4 } + \theta _ { 7 } + 2 \theta _ { 6 } + 2 \theta _ { 7 } - 2 \theta _ { 4 } + \theta _ { 8 } + 2 \theta _ { 4 } + \theta _ { 1 } + \theta _ { 1 } + 2 \theta _ { 6 } + 2 \theta _ { 6 } + 2 \theta _ { 7 } + 2 \theta _ { 1 } + 2 \theta _ { 7 } } \\ & { + 2 \theta _ { 1 } + \theta _ { 7 } + 2 \theta _ { 8 } + 2 \theta _ { 7 } + 2 \theta _ { 7 } + 2 \theta _ { 8 } + \theta _ { 1 } + 2 \theta _ { 7 } + 2 \theta _ { 6 } + 2 \theta _ { 7 } + 2 \theta _ { 6 } + 2 \theta _ { 7 } + 2 \theta _ { 7 } } \\ & { - 2 4 \theta _ { 1 } + \theta _ { 7 } + 2 \theta _ { 7 } + 2 \theta _ { 7 } + 2 \theta _ { 7 } + 2 \theta _ { 1 } + \theta _ { 1 0 } + 2 \theta _ { 7 } + 2 \theta _ { 6 } + 2 \theta _ { 7 } + 3 \theta _ { 8 } + 2 \theta _ { 7 } } \\ & { - 2 4 \theta _ { 8 } + \theta _ { 1 0 } + 2 \theta _ { 1 0 } + 2 \theta _ { 1 0 } + 2 \theta _ { 1 0 } + 2 \theta _ { 1 0 } - 2 \theta _ { 1 0 } - 2 \theta _ { 1 0 } + 3 \theta _ { 1 0 } } \\ &  - 2 \theta _ { 1 0 } + \theta _   \end{array} \end{array}
$$

The other 5 equations are somewhat shorter than eq.(4.7) above but are of comparable complexity. This set of 8equations and 8 unknowns (which is easily reduced to 6 equations and 6 unknowns) does not have an obvious analytical solution.However,it is possible to find an analytical solution. Consider the following substitution for the coeffcients:

$$
\begin{array} { l l } { { c _ { 1 } = 0 , } } & { { d _ { 1 } = x + \frac { 1 } { 2 } , } } \\ { { c _ { 2 } = 2 x + 1 , } } & { { d _ { 2 } = - x , } } \\ { { c _ { 3 } = - 4 x - 1 , } } & { { d _ { 3 } = - x , } } \\ { { c _ { 4 } = 2 x + 1 , } } & { { d _ { 4 } = x + \frac { 1 } { 2 } , } } \end{array}
$$

# or alternatively

$$
\begin{array} { l l } { { c _ { 1 } = x + \frac 1 2 , ~ } } & { { d _ { 1 } = 2 x + 1 , } } \\ { { } } & { { } } \\ { { c _ { 2 } = - x , ~ } } & { { d _ { 2 } = - 4 x - 1 , } } \\ { { } } & { { } } \\ { { c _ { 3 } = - x , ~ } } & { { d _ { 3 } = 2 x + 1 , } } \\ { { } } & { { } } \\ { { c _ { 4 } = x + \frac 1 2 , ~ } } & { { d _ { 4 } = 0 . } } \end{array}
$$

After substitution in the 8 equations obtained, we find that each of the 6 expressions remaining (2 are trivially satisfied) are simply proportional to the following cubic polynominal

$$
4 8 x ^ { 3 } + 2 4 x ^ { 2 } - 1 .
$$

Therefore, they have a common solution given by the roots of the cubic equation

$$
4 8 x ^ { 3 } + 2 4 x ^ { 2 } - 1 = 0 .
$$

The real root is given by

$$
\begin{array} { r } { x = \frac { 1 } { 6 } \big ( 2 ^ { 1 / 3 } + 2 ^ { - 1 / 3 } - 1 \big ) = 0 . 1 7 5 6 \dots . } \end{array}
$$

These solutions were first found numerically using the improved Newton-Raphson method of Bassetti et al.[5]. This was not completely trivial as the method only works in the neighborhood of a solution.It was combined with a Monte Carlo search to locate the solution.After examining the 2 solutions found,it was straightforward to postulate the exact form shown in eqs. (4.8)and (4.9). The substitution was made using the program REDUCE [6].

The previous procedure is straightforward but complex enough to necessitate the use of algebraic computation to evaluate expressions. In section 5 we reformulate the problem using somewhat different techniques and show how the results obtained are actually more general than presented in this section.

# 5. The general approach using Lie groups

# 5.1.Symplectic maps acting on functions of phase space

The results we have derived in this paper apply to any Lie group. The Lie group of symplectic maps generated by Hamilton's equations is not the simplest example of a Lie group. In fact, it is an infinite-dimensional Lie group since any function used for the Hamiltonian wil generate a symplectic map. Nevertheless, we will see how to rephrase in group language the problem of canonical integration by looking at Hamiltonian dynamics.

We start with Hamilton's equations,

$$
\mathrm { d } z / \mathrm { d } t = [ z , H ] ,
$$

where $[ f , \pmb { g } ]$ denotes the Poisson bracket, and $z$ is a vector composed of the coordinates and momenta. Eq.

(5.1) can be rewritten as

$$
{ \bf d } \pmb { \ z } / { \bf d } t = : - \pmb { H } ; \pmb { \ z } ,
$$

where

$$
: - H ( z ) : g ( z ) = \big [ - H ( z ) , g ( z ) \big ] .
$$

In eqs. (5.1)-(5.3) the Poisson brackets are taken with respect to z. To turn eq. (5.1) into an equation involving symplectic maps, we must use a succession of tricks [7]. First, we will look for a map $M ( t )$ which acts on functions of $z _ { 0 }$ and propagates them in time according to (5.1):

$$
g \big ( z \big ( t \big ) \big ) = M \big ( t \big ) g \big ( z _ { 0 } \big ) .
$$

Since $\pmb { g }$ has no explicit time dependence, it is also propagated in time with the Poisson bracket,

$$
\begin{array} { r } { \mathbf { d } g / \mathbf { d } t = \big [ g , H \big ] . } \end{array}
$$

If we substitute (5.4) into (5.5), we find

$$
\begin{array} { r } { \mathrm { d } M / \mathrm { d } t g \big ( z _ { 0 } \big ) = \big [ M g \big ( z _ { 0 } \big ) , H \big ( M z _ { 0 } ; t \big ) \big ] } \\ { = \big [ M g \big ( z _ { 0 } \big ) , M H ( z _ { 0 } ; t ) \big ] } \\ { = M \big [ g \big ( z _ { 0 } \big ) , H \big ( z _ { 0 } ; t \big ) \big ] _ { z _ { 0 } } } \\ { = M : - H \big ( z _ { 0 } ; t \big ) : g \big ( z _ { 0 } \big ) . } \end{array}
$$

To go from (5.5) to (5.6), we use (5.4). Eq. (5.7) is a tautology coming from the definition of $M$ Finally (5.8) is simply the invariance of the Poisson bracket under symplectic transformations.We can proceed one step further by realizing that $g ( z _ { 0 } )$ is an arbitrary function of $\pmb { z _ { 0 } }$ ，

$$
{ \bf d } M / { \bf d } t = M : - { \cal H } ( z _ { 0 } ; t ) : .
$$

Eq.(5.10) is the starting point of a Lie algebraic treatment of classical dynamics.It is important to emphasize that $\pmb { M }$ acts on functions of $\pmb { z _ { 0 } }$ and transforms their functional form in conformity with (5.5).

# 5.2. The one-map integrator

Here to simplify the notation, we will restrict ourselves to time-independent Hamiltonians.As previously shown, it is often possible to apply the time-independent formulae by extending the phase space.

Formally, we can solve (5.1O) in the time-independent case. In fact the solution is just

$$
\begin{array} { r } { \pmb { M } \big ( \tau \big ) = \exp \big ( : - t H \big ( z _ { 0 } \big ) : \big ) . } \end{array}
$$

The trouble with eq. (5.11） resides in the impossibility of evaluating $M ( t ) z _ { 0 }$ for an arbitrary $\pmb { H }$ Symplectic integration consists in replacing $M ( t )$ by a product of symplectic maps which approximates $M ( t )$ to a given order and such that each factor can be exactly and explicitly evaluated on the function $\pmb { z _ { 0 } }$

The first case to consider is the one-map approximation of $M ( t )$ . Imagine that we have found a map $N ( t )$ such that

$$
\begin{array} { r } { M ( t ) = N ( t ) + \mathcal { O } \big ( t ^ { k + 1 } \big ) , } \end{array}
$$

and that ${ \pmb N } ( t ) z _ { \pmb 0 }$ is a well-known function of $\pmb { z _ { 0 } }$ and $t$ . Then $N ( t )$ is a $\pmb { k }$ th-order integration step,

$$
N ( t ) = M _ { k } ( t ) .
$$

To illustrate this particularly simple case, consider the one-dimensional Hamiltonian given by

$$
H = { \textstyle \frac { 1 } { 2 } } \big [  p - f ( q ) \big ] ^ { 2 } + v \big (  q \big ) .
$$

To construct a first-order integration step, we can approximate the map produced by $\pmb { H }$ with a simple characteristic function,

$$
\begin{array} { l } { { F \big ( q , \bar { p } \big ) = q \bar { p } + t H \big ( q , \bar { p } \big ) , } } \\ { { \mathsf { z } } _ { 0 } = \big ( q , p \big ) , } \\ { { \mathsf { z } } \big ( t \big ) = \big ( \bar { q } , \bar { p } \big ) . } \end{array}
$$

The map produced by $F ( q , { \bar { p } } )$ can be writen down explicitly. In this case $M _ { 1 } ( t )$ is just given by

$$
\begin{array} { l } { \displaystyle \bar { q } = M _ { 1 } ( t ) q = q + \frac { t \bigl ( p - f - t v ^ { \prime } \bigr ) } { 1 - t f ^ { \prime } } , } \\ { \displaystyle \bar { p } = M _ { 1 } ( t ) p = \frac { p - t \bigl ( v ^ { \prime } + f f ^ { \prime } \bigr ) } { 1 - t f ^ { \prime } } . } \end{array}
$$

In eq. (5.16),the prime indicates a derivative with respect to q. From this example,we see that the techniques used to fabricate symplectic maps are central to the discovery of explicit symplectic integrators. It should be noticed that (5.15)is always a first-order approximation of the map generated by H. However, for an arbitrary $\pmb { H } _ { : }$ ，it is not always possible to invert explicitly the equations obtained from the characteristic function ${ \pmb F } .$ Nevertheless,it is possible to use (5.15) in conjunction with a Newton search procedure. This is much slower than any explicit techniques. The higher-order generalization of (5.15)of Channell and Scovel [4] is based on the idea of one-map implicit integration.

# 5.3. The two-map integrator

Let us suppose that we cannot find a symplectic approximation of $H .$ .Nevertheless,let us assume that we can split $\pmb { H }$ into two pieces which can be solved exactly when considered as independent Hamiltonians,

$$
\begin{array} { l } { H = H _ { 1 } + H _ { 2 } , } \\ { \quad } \\ { \exp ( - t : H _ { i } ; ) = N _ { i } ( t ) . } \end{array}
$$

Can we make an approximation to $M ( t )$ using both $N _ { 1 }$ and $ { N _ { 2 } } ?$ Furthermore, can we in a consistent manner work out an approximation of first, second, third or even fourth order in $\pmb { t }$ $( k = 1 , \ldots , 4 ) ^ { \bullet }$

The answer to these questions is yes and depends only on the Lie group structure of the symplectic group,which is the ability to write maps in the neighborhood of the identity as the exponent of some Poisson bracket operator. First, let us introduce the Campbell-Baker-Hausdorf formula (CBH). The CBH formula allows us to combine the exponent of two Lie group elements of the form $\mathtt { e } ^ { A }$ where $\pmb { A }$ is some operator. In fact let us consider two group elements $\tt e ^ { \epsilon { } A }$ and $\mathsf { e } ^ { \mathsf { e } B }$ ，then the product $\mathtt { e } ^ { c }$ is approximated by a formula involving only commutators,

$$
\begin{array} { l } { { { \mathrm { e } } ^ { C } = { \mathrm { e } } ^ { \epsilon A } { \mathrm { e } } ^ { \epsilon B } , } } \\ { { { } } } \\ { { { \cal C } = \epsilon A + \epsilon B + { \textstyle \frac { 1 } { 2 } } \epsilon ^ { 2 } \bigl \{ \ A , B \bigr \} + { \textstyle \frac { 1 } { 1 2 } } \epsilon ^ { 3 } \bigl \{ \bigl \{ \ B , A \bigr \} , A \bigr \} + { \textstyle \frac { 1 } { 1 2 } } \epsilon ^ { 3 } \bigl \{ \ B , \bigl \{ \ B , A \bigr \} \bigr \} } } \\ { { { } } } \\ { { { } ~ - { \textstyle \frac { 1 } { 2 4 } } \epsilon ^ { 4 } \bigl \{ \ B , \bigl \{ \bigl \{ \ B , A \bigr \} , A \bigr \} \bigr \} + \cdots + \mathcal O \bigl ( \epsilon ^ { 5 } \bigr ) , } } \\ { { { \bigl \{ } A , B \bigr \} = A B - B A . } } \end{array}
$$

The formulas given in (5.19)-(5.21) willalow us to derive canonical integration techniques valid for any Lie group because they do not depend on the symplectic structure.

To do this we need one more property of the Poisson bracket,

$$
\{ : f : , : g : \} = : [ f , g ] : .
$$

Now, consider the following approximation of $\pmb { M }$ ：

$$
\begin{array} { r l } & { N \big ( t \big ) = N _ { 1 } \big ( t \big ) N _ { 2 } \big ( t \big ) } \\ & { \qquad = \exp \big ( - t : H _ { 1 } : \big ) \exp \big ( : - t H _ { 2 } : \big ) } \\ & { \qquad = \exp \big ( - : t H + \frac { 1 } { 2 } t ^ { 2 } \big [ H _ { 1 } , H _ { 2 } \big ] + \ldots \big : \big ) } \\ & { \qquad = M \big ( t \big ) + \mathcal { O } \big ( t ^ { 2 } \big ) = M _ { 1 } \big ( t \big ) . } \end{array}
$$

Clearly, eq. (5.23) leads to a first-rder integrator. Now, let us symmetrize $N ( t )$ ：

$$
\begin{array} { r l } & { N \big ( t \big ) = N _ { 1 } \big ( \frac { 1 } { 2 } t \big ) N _ { 2 } \big ( t \big ) N _ { 1 } \big ( \frac { 1 } { 2 } t \big ) } \\ & { \qquad = \exp \big ( \cdot - \frac { 1 } { 2 } t H _ { 1 } \cdot \big ) \exp \big ( \cdot - t H _ { 2 } \colon \big ) \exp \big ( \cdot - \frac { 1 } { 2 } t H _ { 1 } \colon \big ) } \\ & { \qquad = \exp \big ( \cdot - t \big ( \frac { 1 } { 2 } H _ { 1 } + H _ { 2 } \big ) + \frac { 1 } { 4 } t ^ { 2 } \big [ H _ { 1 } , H _ { 2 } \big ] + \mathcal { O } \big ( t ^ { 3 } \big ) \colon \big ) \exp \big ( \cdot - \frac { 1 } { 2 } t H _ { 1 } \colon \big ) } \\ & { \qquad = \exp \big ( \cdot - t H + \frac { 1 } { 4 } t ^ { 2 } \big [ H _ { 1 } , H _ { 2 } \big ] + \frac { 1 } { 4 } t ^ { 2 } \big [ H _ { 2 } , H _ { 1 } \big ] + \mathcal { O } \big ( t ^ { 3 } \big ) \colon \big ) } \\ & { \qquad = \exp \big ( \cdot - t H + \mathcal { O } \big ( t ^ { 3 } \big ) \colon \big ) = M _ { 2 } \big ( t \big ) . } \end{array}
$$

This new approximation which we can properly call the generalized leap-frog is quadratic. In fact, it is straightforward to show that any symmetrized product cannot have even powers of $t$ in the Lie operator.

It is clear that allthe results of the previous sections which were derived with the help of a generating function and seemed to apply in a very restrictive manner to the special Hamiltonian used,are in fact very general. Not only do they extend to the entire symplectic group but also to other Lie groups as well.

While the group approach cleans up the conceptual side of the problem,it is also true that it provides a simple derivation of the fourth-order integrator.We start with the following symmetrized ansatz:

$$
\begin{array} { r l } & { N \left( t \right) = { \mathrm { e } } ^ { A } { \mathrm { e } } ^ { B } { \mathrm { e } } ^ { \alpha A } { \mathrm { e } } ^ { \beta B } { \mathrm { e } } ^ { \alpha A } { \mathrm { e } } ^ { B } { \mathrm { e } } ^ { A } , } \\ & { 2 \left( 1 + \alpha \right) A = - t { : } H _ { 1 } { : } , } \\ & { \left( 2 + \beta \right) B = - t { : } H _ { 2 } { : } . } \end{array}
$$

From the CBH formula, we deduce that to order $t ^ { 3 }$ there can be only four terms in the exponent of $N ( t )$ Consequently,in addition to (5.26) and (5.27),which take care of order $t$ terms, we can find two additional equations using the $t ^ { 3 }$ terms. These equations are determined by setting the triple commutations of (5.26) and (5.27) to zero and are given by

$$
\begin{array} { r l } & { - \frac { 1 } { 6 } \beta \alpha ^ { 2 } + \frac { 2 } { 3 } \alpha ^ { 2 } - \frac { 1 } { 3 } \alpha \beta - \frac { 2 } { 3 } \alpha - \frac { 1 } { 6 } \beta - \frac { 1 } { 3 } = 0 , } \\ & { \frac { 1 } { 6 } \beta ^ { 2 } \alpha + \frac { 1 } { 6 } \beta ^ { 2 } - \frac { 1 } { 3 } \alpha \beta - \frac { 1 } { 3 } \alpha + \frac { 2 } { 3 } \beta + \frac { 2 } { 3 } = 0 . } \end{array}
$$

Solving for $\pmb { \beta }$ using (5.28) and substituting into (5.29) gives the following results:

$$
\begin{array} { l } { \displaystyle \beta = \frac { 4 \alpha ^ { 2 } - 4 \alpha - 2 } { \big ( \alpha + 1 \big ) ^ { 2 } } , } \\ { \displaystyle \frac { \alpha \big ( \alpha ^ { 3 } - 3 \alpha ^ { 2 } + 3 \alpha + 1 \big ) } { \big ( \alpha + 1 \big ) ^ { 3 } } = 0 . } \end{array}
$$

Eqs. (5.30)and (5.31)admit one useful real solution which is given by $\alpha = 1 - 2 ^ { 1 / 3 }$ . For that value $N ( t )$ is just

$$
\begin{array} { l } { { N ( t ) = N _ { 1 } \bigg ( \displaystyle \frac { t } { 2 \big ( 1 + \alpha \big ) } \bigg ) N _ { 2 } \bigg ( \displaystyle \frac { t } { 1 + \alpha } \bigg ) N _ { 1 } \bigg ( \displaystyle \frac { \alpha t } { 2 \big ( 1 + \alpha \big ) } \bigg ) N _ { 2 } \bigg ( \displaystyle \frac { \big ( \alpha - 1 \big ) t } { \big ( 1 + \alpha \big ) } \bigg ) } } \\ { { \times N _ { 1 } \bigg ( \displaystyle \frac { \alpha t } { 2 \big ( 1 + \alpha \big ) } \bigg ) N _ { 2 } \bigg ( \displaystyle \frac { t } { 1 + \alpha } \bigg ) N _ { 1 } \bigg ( \displaystyle \frac { t } { 2 \big ( 1 + \alpha \big ) } \bigg ) } } \\ { { = M \big ( t \big ) + \mathcal { O } \big ( t ^ { 5 } \big ) = M _ { 4 } \big ( t \big ) . } } \end{array}
$$

Eq. (5.32) is precisely the solution found in section 4.

# 5.4. The $\pmb { N }$ map integrator

We have seen how to generate a fourth-order two-map integrator using only the Lie group structure. For three-map integrators, the best one can do is to symmetrize the expression of a single step,

$$
\begin{array} { r l } & { H = H _ { 1 } + H _ { 2 } + H _ { 3 } , } \\ & { N _ { i } \big ( t \big ) = \exp \big ( - t : H _ { i } \big : \big ) , } \\ & { M \big ( t \big ) = N _ { 1 } \big ( \frac { 1 } { 2 } t \big ) N _ { 2 } \big ( \frac { 1 } { 2 } t \big ) N _ { 3 } \big ( t \big ) N _ { 2 } \big ( \frac { 1 } { 2 } t \big ) N _ { 1 } \big ( \frac { 1 } { 2 } t \big ) + \mathcal { O } \big ( t ^ { 3 } \big ) . } \end{array}
$$

In general, the $\pmb { N }$ map symmetrized integrator is always quadratic.

As a final remark: recall that we said that the maps $N _ { i }$ must equal $\mathbf { e x p } ( : - \mathbf { \mathfrak { t } } H _ { i } \mathbf { : } )$ ; in general they need to be only an approximation of $\mathrm { e x p } ( : - t H _ { i } ; $ ） belonging to the Lie group and of an order greater than the order of the method of integration.

# 5.5.Examples of some important Hamiltonians

Our task is reduced to finding ways to decompose standard Hamiltonians in pieces which can be computed either exactly or approximated by some other symplectic maps.

Let us start with a very important case in the theory of circular particle accelerators: the Hamiltonian for a sector bending magnet which might also have other fields present (quadrupole, sextupole..). In this case

$$
\begin{array} { l } { { H = H _ { 1 } + H _ { 2 } , } } \\ { { \ } } \\ { { H _ { 1 } = \displaystyle - \left( 1 + \frac { x } { \rho } \right) \sqrt { \left( 1 + \delta \right) ^ { 2 } - p _ { x } ^ { 2 } - p _ { y } ^ { 2 } } - \frac { p _ { \tau } } { \beta _ { 0 } } , } } \\ { { \ } } \\ { { H _ { 2 } = \displaystyle \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } + \frac { x } { \rho } - V ( x , y ) , } } \\ { { \ } } \\ { { \displaystyle \left( 1 + \delta \right) ^ { 2 } = 1 - \frac { 2 p _ { \tau } } { \beta _ { 0 } } + p _ { \tau } ^ { 2 } , \qquad \beta _ { 0 } = \frac { v _ { 0 } } { c } . } } \end{array}
$$

This Hamiltonian generates the motion of the variables $( x , p _ { x } , y , p _ { y } , \tau , p _ { \tau } )$ . The time-like variable is the path length variable $\pmb { s }$ measuring the distance along the design orbit. The dynamics of $H _ { 1 }$ or $H _ { 2 }$ is exactly soluble. In fact, $H _ { 1 }$ is just a rotation in polar coordinates.

It is customary and sometimes convenient to replace $\pmb { H }$ by an expanded Hamiltonian which exact in $\hphantom { 0 } 1 + \delta$ but only quadratic in the transverse momenta,

$$
\begin{array} { r l } & { \mathcal { H } { = } \mathcal { H } _ { 1 } + \mathcal { H } _ { 2 } , } \\ & { \mathcal { H } _ { 1 } { = } \displaystyle \frac { p _ { x } ^ { 2 } + p _ { y } ^ { 2 } } { 2 \left( 1 + \delta \right) } - \frac { p _ { \tau } } { \beta _ { 0 } } - \delta , } \\ & { \mathcal { H } _ { 2 } { = } \displaystyle - \frac { \delta x } { \rho } + \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } - V \big ( x , y \big ) . } \end{array}
$$

Again, both $\mathcal { H } _ { 1 }$ and $\pmb { \mathcal { H } } _ { 2 }$ are exactly solvable. Interestingly,another division of $\pmb { \mathcal { H } }$ is possible,

$$
\begin{array} { r l } & { \mathrel { \mathcal { H } } _ { 1 } = \displaystyle \frac { p _ { x } ^ { 2 } + p _ { y } ^ { 2 } } { 2 \left( 1 + \delta \right) } - \frac { p _ { \tau } } { \beta _ { 0 } } - \delta - \frac { \delta x } { \rho } - \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } - V _ { 2 } \mathopen { } \mathclose \bgroup \left( x , y \aftergroup \egroup \right) , } \\ & { \mathrel { \mathcal { H } } _ { 2 } = \displaystyle - V _ { \geq 3 } \mathopen { } \mathclose \bgroup \left( x , y \aftergroup \egroup \right) . } \end{array}
$$

In the division of eqs. (5.43) and (5.44), the map $N _ { 1 }$ is exactly solvable, giving rise to a $\pmb { \delta }$ -dependent matrix and a time of flight which is quadratic in the betatron variables $( x , p _ { x } , y , p _ { y } )$

.The quantity $V _ { \geq 3 } ( \pmb { x } , \pmb { y } )$ is just the nonlinear part of the multipole content and produces a kick. Traditionally, $\mathcal { H } _ { 1 }$ and $\mathcal { H } _ { 2 }$ have been used in the standard “kick codes” for particle tracking in accelerators using a quadratic algorithm. (One thin lens $( \mathcal { R } _ { 2 } )$ in the middle of each linear element $( \mathcal { H } _ { 1 } ) . )$

From the few useful examples which have been studied here, it is quite clear that no general recipe is available for explicit symplectic integrators.

# 6. Concluding remarks

Finally, we conclude with a remark on the time-dependent case. Going back to the general problem, consider Hamilton's equations given by (5.1). We can write the following equivalence:

$$
\begin{array} { r l } & { \mathrm { d } \mathsf { z } / \mathrm { d } t = \left[ \mathsf { z } , H ( \mathsf { z } ; t ) \right] , } \\ & { \Rightarrow \left( \mathrm { d } \mathsf { z } / \mathrm { d } \tau = \left[ \mathsf { z } , H ( \mathsf { z } ; t ) + p _ { t } \right] , \right. } \\ & { \Rightarrow \left\{ \mathrm { d } t / \mathrm { d } \tau = \left[ t , H + p _ { t } \right] = 1 , \right. } \\ & { \left. \mathrm { d } p _ { t } / \mathrm { d } \tau = \left[ \mathsf { p } _ { t } , H + p _ { t } \right] = - \partial H / \partial t . \right. } \end{array}
$$

The phase space has been extended to $\boldsymbol { w } = ( z , t , p _ { t } )$ ， and the new time-like variable is just $\pmb { \tau }$ The two-map integration formulae can be used if the motion of either $H _ { 1 } + p _ { t }$ or $H _ { 2 } + p _ { t }$ can be solved exactly. Results of the previous sections were based on an $H _ { 1 }$ depending only on the momenta, hence $H _ { 1 } + p _ { t }$ is solvable and we do regain the time-dependent formulae of the previous sections (see eq. (2.4).

As we mentioned, only the Lie structure of the group entered in the integration formulae. Consequently it is possible to use them in other contexts.In particular,it could be applied to the problem of spin motion in a storage ring. In the usual approximation,one neglects the effct of the spin on the orbital motion, but includes the effect of the orbit on the spin. Our method can allow us to write an integrator which not only preserves the symplectic character of the orbital motion, but also forces the spin transfer matrix into SU(2) in the spinor representation or $O ( 3 )$ if the spin is treated as a 3-dimensional vector.

As a final note we would like to add that just prior to submisson of this paper, we learned of results obtained independently which overlap some of the results obtained here [8].

# Acknowledgements

We would like to thank M. Baseti for his help with the numerical solution of the equations in section 4,F. Neri for useful discussions and finally R. Warnock for reading the manuscript and for several useful suggestions.

# References

[1] H. Goldstein, Classical Mechanics (Addison-Wesley,New York,1965).   
[2] R.D. Ruth,IEEE Trans.Nucl. Sci. NS-30 (1983) 2669.   
[3]R.DeVogelaere,Methodsof integration whichpreserve thecontact transformation propertyofthe Hamiltonequations, N7-ONR-43906.   
[4] P.J. Channelland C.Scovel, Los Alamos National Laboratory note LA-UR-88-1828 (1988).   
[5] M.Bassetti,R.M. Buonanni and M. Placidi,Nucl. Instr. Meth.45 (1966) 93.   
[6] A.C. Hearn, REDUCE version 3.1, RAND Corporation, Santa Monica, CA.   
[7] A.J.Dragt and E.Forest, J. Math.Phys.24 (1983) 2734.   
[8] J. Candy, University of Alberta, private communication.