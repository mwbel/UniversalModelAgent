<!-- source: FOURTH ORDER SYMPLECTIC INTEGRATION.pdf -->

<!-- pdf_type: normal; pages: 23; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-23 -->
# FOURTH-ORDER SYMPLECTIC INTEGRATION\*

ETIENNE FOREST

Lawrence Berkeley Laboratory

Berkeley， California 94720

and

RONALD D.RUTH

Stanford Linear Accelerator Center

Stanford University, Stanford, California 94309

# ABSTRACT

In this paper we present an explicit fourth-order method for the integration of Hamilton's Equations. This method preserves the property that the time evolution of such a system yields a canonical transformation from the initial conditions to the final state. That is, the integration step is an explicit symplectic map. Although the result is first derived for a specific type of Hamiltonian,it is shown to be quite general. In particular, the results can be applied to any Lie group.

# Submitted to Physica D

# 1. Introduction

There are many diferent ways to integrate differential equations numerically. These various methods are usually characterized by the accuracy of a single step in time (the independent variable). Thus if in a smal time step $h$ the integration is performed so that it is accurate through order $h ^ { k }$ , then the method is referred to as an $k ^ { t h }$ order integration method.

The class of differential equations of interest here is that in which the equations are derivable from a Hamiltonian. The exact solution of such a system of differential equations leads to a symplectic map from the initial conditions to the present state of the system. However,a characteristic feature of most high order $\left( k > 2 \right)$ integration methods is that they are not exactly symplectic. One manifestation of this is that the determinant of the Jacobian of the transformation for one time step differs slightly from unity,and thus the system will be damped or excited artificially. In many applications the salient features of the solutions appear only after long times or large numbers of iterations; in these applications spurious damping or excitation may lead to misleading results.

The purpose of this paper is to develop an explicit fourth order symplectic map (a fourth order integration step which preserves exactly the canonical character of the equations of motion). For a typical numerical integration this method can be used to eliminate noncanonical effects while providing the accuracy of a fourth order integration step. In addition there is another way of viewing this approach. If we iterate any explicit integration step whether canonical or not, eventually the absolute error in the coordinates and the momenta gets large. In cases where the integration step is not symplectic,and in which spurious damping occurs, X and p settle onto some fixed point. If the map is symplectic,this does not happen. A symplectic integration step generates phase space behavior which is close to that of the original system with errors in phase’ which add up after many iterations to yield large absolute errors in $x$ and $p$ when compared with the exact solution of the differential equation.

Therefore in the symplectic case it is possible and sometimes attractive to replace the differential equation by a symplectic map. This map then becomes the object of study and so can be iterated as much as we like. When viewed in this way a fourth order integration step becomes a method to replace a differential equation with a map. This symplectic map is the solution of some physical problem which is close in a well defined sense to the original problem. For nonsymplectic integration methods the iterations must be stopped before the solution deviates very far from the exact solution of the differential equations.

- Before proceeding we would like to mention that the method described here was circulated privately by us several years ago and is now used routinely in several computer programs which trace the trajectories of particles in particle accelerators.

# 2.The Problem

Consider a system of differential equations governed by the Hamiltonian,

$$
H = A ( { \bf p } ) + V ( { \bf x } ) \quad .
$$

Thus the equations of motion are given by

$$
\begin{array} { r l } { \displaystyle \frac { d { \bf x } } { d t } = \frac { \partial H } { \partial { \bf p } } } & { , } \\ { \displaystyle \frac { d { \bf p } } { d t } = - \frac { \partial H } { \partial { \bf x } } } & { . } \end{array}
$$

In the equations above the bold face X and $\mathbf { p }$ are $n$ dimensional vectors of the coordinates and momenta respectively and $t$ is the independent variable. Although the above Hamiltonian is explicitly independent of the time,it is general enough to take care of the case of a time dependent potential. In the time dependent case if we have a Hamiltonian given by

$$
H _ { 1 } = A ^ { \prime } ( { \bf p } ) + V ^ { \prime } ( { \bf x } , t ) \quad ,
$$

then we can use another independent variable $\tau$ and replace the time dependent problem with the following $\tau$ independent problem:

$$
H = A ^ { \prime } ( { \bf p } ) + p _ { n + 1 } + V ^ { \prime } ( { \bf x } , x _ { n + 1 } ) \quad .
$$

which is of the same form as Eq. (2.1). In this case the solution of Hamilton's equations for $x _ { n + 1 }$ yields $x _ { n + 1 } ~ = ~ \tau$ .Thus $x _ { n + 1 }$ is just constrained to be the independent variable.

The solution of the equations of motion in (2.2) is given by the functions

$$
\begin{array} { r l } { \mathbf { x } ( \mathbf { x } _ { 0 } , \mathbf { p } _ { 0 } , t ) } & { { } , } \\ { } \\ { \mathbf { p } ( \mathbf { x } _ { 0 } , \mathbf { p } _ { 0 } , t ) } & { { } , } \end{array}
$$

where $\mathbf { x } _ { 0 }$ and ${ \bf p } _ { 0 }$ are the initial conditions at time $t = 0$ . Due to the canonical character of the equations of motion, Eq. (2.5) is a canonical transformation (or a symplectic map) from the initial conditions to the state at time $t$ . Let us denote this map by $M ( t )$ such that

$$
( { \bf x } , { \bf p } ) = M ( t ) ( { \bf x } _ { 0 } , { \bf p } _ { 0 } ) \quad .
$$

We would like to find a symplectic map $M _ { k } ( t )$ which approximates $M ( t )$ through order $t ^ { k }$ . Thus the difference between the two maps will be of order $t ^ { k + 1 }$

$$
\| M ( t ) - M _ { k } ( t ) \| = O ( t ^ { k + 1 } ) \quad .
$$

The method for calculating $M _ { k } ( t )$ is presented in the next section.

# 3. The Method of Successive Canonical Transformations

In this section the basic approach to find $M _ { k } ( t )$ will be successive canonical transformations. If we perform the transformations in Eq. (2.6) so that $\mathrm { H }$ is expressed in terms of the initial conditions, then the equations of motion are

$$
\begin{array} { r } { \frac { d { \bf x } _ { 0 } } { d t } = 0 \quad , } \\ { \frac { d { \bf p } _ { 0 } } { d t } = 0 \quad , } \end{array}
$$

or the new Hamiltonian $H ^ { ' }$ is identically zero or at least independent of $\mathbf { x } _ { 0 }$ and $\mathbf { p } _ { 0 }$

This suggests that we perform canonical transformations in such a way as to make $H$ vanish through some order in $t$ . Let us assume that we succeed through

order $t ^ { k - 1 }$ ; that is, we performthe canonical transformation

$$
\begin{array} { r } { ( \begin{array} { l } { \mathbf { x } } \\ { \mathbf { p } } \\ { H } \end{array} )  ( \begin{array} { l } { \mathbf { x } ^ { \prime } } \\ { \mathbf { p } ^ { \prime } } \\ { H ^ { \prime } } \end{array} ) } \end{array}
$$

such that

$$
H ^ { \prime } ( \mathbf { x } ^ { \prime } , \mathbf { p } ^ { \prime } , t ) = O ( t ^ { k } ) .
$$

Then the solutions for the equations of motion are

$$
\begin{array} { c c } { { { \bf x } ^ { \prime } = { \bf x } _ { 0 } + O ( t ^ { k + 1 } ) } } & { { , } } \\ { { } } & { { } } \\ { { { \bf p } ^ { \prime } = { \bf p } _ { 0 } + O ( t ^ { k + 1 } ) } } & { { , } } \end{array}
$$

where $\mathbf { x } _ { 0 }$ and ${ \bf p } _ { 0 }$ are constants. This means that the new coordinates and momenta differ from the initial conditions at order $t ^ { k + 1 }$ . Thus if $\mathbf { x } ^ { \prime }$ and $ { \mathbf { p } } ^ { \prime }$ are used as initial conditions and if we calculate $\mathbf { x }$ and $\mathbf { p }$ by inverting the transformation in Eq. (3.2), the error introduced is of order tk+1. Therefore, X and p are accurate through order tk. So in order to calculate Mk(t),we must perform a canonical transformation (or a sequence of them) so that the new Hamiltonian is of order $t ^ { k }$ .

A canonical transformation is performed with the aid of a generating function. There are different types of these, but for this section it is useful to use a generating function which is a function of the new coordinates and the old momenta. Let us consider the map $( \mathbf { x } , \mathbf { p } ) \mapsto ( \mathbf { x } ^ { \prime } , \mathbf { p } ^ { \prime } )$ . The generating function is given by1

$$
F _ { 3 } ( { \bf x } ^ { \prime } , { \bf p } , t ) = - { \bf x } ^ { \prime } \cdot { \bf p } + G ( { \bf x } ^ { \prime } , { \bf p } , t ) \quad ,
$$

while the transformation equations are

$$
\mathbf { x } = - \frac { \partial F _ { 3 } } { \partial \mathbf { p } } = \mathbf { x } ^ { \prime } - G _ { \mathbf { p } } ( \mathbf { x } ^ { \prime } , \mathbf { p } , t ) \quad ,
$$

$$
\begin{array} { l } { { { \displaystyle { \bf p } ^ { \prime } = - \frac { \partial F _ { 3 } } { \partial { \bf x } } = { \bf p } - G _ { { \bf x } } ( { \bf x } ^ { \prime } , { \bf p } , t ) \quad , } } } \\ { { { \displaystyle H ^ { \prime } = H + \frac { \partial F _ { 3 } } { \partial t } = H + G _ { t } \quad , } } } \end{array}
$$

where boldface subscripts have been used to denote the gradient operation and scalar subscripts denote partial derivatives. Thus, the generating function differs from the identity by the function $G ( \mathbf { x } ^ { \prime } , \mathbf { p } , t )$ . In order to construct an explicit fourth-order symplectic integration step,it will be necessary to use several such transformations in sequence as in Ref. 2. To illustrate the technique,it is useful to consider first a low-order symplectic integration step. By examining Eq. (3.8), a good first choice for a generating function is

$$
\begin{array} { l } { { G = - H ( { \bf p } , { \bf x } ^ { \prime } ) t } } \\ { { { \bf \Gamma } } } \\ { { { \bf \Gamma } = - \left[ { \cal A } ( { \bf p } ) + V ( { \bf x } ^ { \prime } ) \right] t \quad , } } \end{array}
$$

which yields the transformation equations

$$
\begin{array} { r l } { \mathbf { p } ^ { \prime } = \mathbf { p } + V _ { \mathbf { x } } ( \mathbf { x } ^ { \prime } ) t } & { { } , } \\ { \mathbf { x } = \mathbf { x } ^ { \prime } + A _ { \mathbf { p } } ( \mathbf { p } ) t } & { { } . } \end{array}
$$

Substituting into the Hamiltonian we find

$$
\begin{array} { l } { { H ^ { \prime } = V \left[ { \bf x } ^ { \prime } + t A _ { \mathrm { p } } ( { \bf p } ^ { \prime } - V _ { \bf x } ( { \bf x } ^ { \prime } ) t ) \right] - V ( { \bf x } ^ { \prime } ) } } \\ { { \mathrm { } } } \\ { { \mathrm { } \simeq t V _ { \bf x } ( { \bf x } ^ { \prime } ) \cdot A _ { \mathrm { p } } ( { \bf p } ^ { \prime } ) + O ( t ^ { 2 } ) \quad , } } \end{array}
$$

where we have expanded for small $t$ . Since $H ^ { \prime }$ is of order $t$ , the right hand sides of Hamilton's equations are also of order $t$ . Therefore, the solution is

$$
\begin{array} { l } { { { \bf x } ^ { \prime } = \mathrm { c o n s t } + O ( t ^ { 2 } ) , } } \\ { { { \bf \phi } } } \\ { { { \bf p } ^ { \prime } = \mathrm { c o n s t } + O ( t ^ { 2 } ) . } } \end{array}
$$

Therefore, if $( \mathbf { x } ^ { \prime } , \mathbf { p } ^ { \prime } )$ are interpreted as initial conditions and Eq. (3.10) is used to calculate $\left( \mathbf { x } , \mathbf { p } \right)$ at some small time $t$ , the error introduced is of order $t ^ { 2 }$ . Thus,this approach has yielded a first-order symplectic map, $M _ { 1 } ( t )$

Note that in Eq. (3.10) we must invert the momentum equation,that is, we must express $\mathbf { p }$ as a function of $\mathbf { x } ^ { \prime }$ and $\mathbf { p ^ { \prime } }$ . With the particular Hamiltonian shown, this inversion is trivial; however,for more general Hamiltonians one must solve the resulting implicit quation numericall4 The requirement of the special formof $H$ shown in Eq. (2.1) will be partly removed in Section 5 where a more general approach is shown.

# 4.Fourth Order Symplectic Integration

To proceed to higher order one can take several approaches. The most obvious choice is to proceed in a way analagous to a Runge and Kutta integration step; that is,to construct a sequence of maps with coefficients which are adjusted to satisfy Hamilton's equations. This is the approach taken in Ref. 2 to derive general 2nd and 3rd order symplectic integration steps. The general form is taken from Eq. (3.10)

$$
{ \bf p } _ { i + 1 } = { \bf p } _ { i } - c _ { i } t V _ { \bf x } ( { \bf x } _ { i } ) \quad , \quad { \bf x } _ { i + 1 } = { \bf x } _ { i } + d _ { i } t A _ { \bf p } ( { \bf p } _ { i + 1 } ) \quad ,
$$

for $\textit { i } = \textit { 0 }$ to $N$ and where $\left( \mathbf { x } _ { o } , \mathbf { p } _ { o } \right)$ are the initial conditions,and $\left( \mathbf { x } _ { N } , \mathbf { p } _ { N } \right) =$ $\left( \mathbf { x } , \mathbf { p } \right)$ are the values of the coordinates and momenta after time step $t$ .Note that the momenta after any given sub-step must be evaluated first followed by the coordinates after that sub-step. The full integration step is the complete sequence of maps; intermediate values of $\left( \mathbf { x } , \mathbf { p } \right)$ at the sub-steps are merely for convenience and should not be interpreted as physical values.

The procedure for finding the coeffcients consists of substituting the sequence of canonical transformations to evaluate the new Hamiltonian. Because the new Hamiltonian is in terms of the initial conditions, the transformations are applied in the reverse of the order shown in Eq. (4.1). That is, $( \mathbf { x } , \mathbf { p } ) \mapsto \left( \mathbf { x } _ { N - 1 } , \mathbf { p } _ { N - 1 } \right) \mapsto$ $( \mathbf { x } _ { N - 2 } , \mathbf { p } _ { N - 2 } ) \dots ( \mathbf { x } _ { o } , \mathbf { p } _ { o } )$ . The final Hamiltonian is then a function of $\left( \mathbf { x } _ { o } , \mathbf { p } _ { o } \right)$ and the undetermined coefficients. We determine the coefficients by requiring that the Hamiltonian be zero through some order in $t$ . For example for $N = 2$ we can find M2(t)with the folowing coeffients:

$$
\begin{array} { l } { { c _ { 1 } = 0 \ , \ d _ { 1 } = 1 / 2 \quad , } } \\ { { } } \\ { { c _ { 2 } = 1 \ , \ d _ { 2 } = 1 / 2 \quad . } } \end{array}
$$

For $N = 3$ we can find $M _ { 3 } ( t )$ provided the six coeffcients satisfy the following five equations.

$$
\begin{array} { r c l } { { } } & { { } } & { { c _ { 1 } + c _ { 2 } + c _ { 3 } = 1 ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { d _ { 1 } + d _ { 2 } + d _ { 3 } = 1 ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { c _ { 2 } d _ { 1 } + c _ { 3 } ( d _ { 1 } + d _ { 2 } ) = 1 / 2 ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { c _ { 2 } d _ { 1 } ^ { 2 } + c _ { 3 } ( d _ { 1 } + d _ { 2 } ) ^ { 2 } = 1 / 3 ~ , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { d _ { 3 } + d _ { 2 } ( c _ { 1 } + c _ { 2 } ) ^ { 2 } + d _ { 1 } c _ { 1 } ^ { 2 } = 1 / 3 ~ . } } \end{array}
$$

A possible solution is given by²

$$
\begin{array} { l } { { c _ { 1 } = 7 / 2 4 , c _ { 2 } = 3 / 4 , c _ { 3 } = - 1 / 2 4 , } } \\ { { } } \\ { { d _ { 1 } = 2 / 3 , d _ { 2 } = - 2 / 3 , d _ { 3 } = 1 . } } \end{array}
$$

For the case of $N = 4$ ,it is possible to find $M _ { 4 } ( t )$ . In this case there are 8 equations with 8 unknowns. These are rather tedious to write out in full detail. As an example we give a few of the relations:

$$
c _ { 1 } + c _ { 2 } + c _ { 3 } + c _ { 4 } = 1 \quad ,
$$

$$
d _ { 1 } + d _ { 2 } + d _ { 3 } + d _ { 4 } = 1 \quad ,
$$

(dic1C2+d²c1c3 +d²c1c4-d²c1 -2d1c1d2c2 + 2d1c1d2c3 +2d1c1d2C4- 2d1c1d2 - 2dic1C2d3 -2d1c1c2d4 + 2dic1C2 -2dic1d3c3 + 2d1c1d3C4 -2d1c1d3- $\begin{array} { r l } & { \mathcal { H } _ { 1 } ( \omega , \omega ; t , \omega + \omega ; t , \omega - \omega ; t , \omega + \omega , 2 \omega ; t , \omega + \omega , 2 \omega ; t , \omega - \omega , - \omega , - \omega , \omega ; \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 2 } ( \omega , \omega ; \omega , - \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 3 } ( \omega , \omega ; \omega , - \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 3 } ( \omega , \omega ; \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { + \mathcal { H } _ { 3 } ( \omega , \omega ; \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 4 } ( \omega , \omega ; \omega , - \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 5 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 6 } ( \omega , \omega ; \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 7 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 8 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ & { \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega , \omega ) } \\ &  \mathcal { H } _ { 9 } ( \omega , \omega , \omega , \omega , \omega , \omega , \omega  \end{array}$ 十

The other 5 equations are somewhat shorter than Eq. (4.7) above but are of comparable complexity. This set of 8 equations and 8 unknowns (which is easily reduced to 6 equations and 6 unknowns) does not have an obvious analytical solution.However,it is possible to find an analytical solution. Consider the following substitution for the coefficients:

$$
\begin{array} { l l } { { c _ { 1 } = 0 ~ , ~ } } & { { d _ { 1 } = x + 1 / 2 ~ , } } \\ { { \ } } & { { \ } } \\ { { c _ { 2 } = 2 x + 1 ~ , ~ } } & { { d _ { 2 } = - x ~ , } } \\ { { \ } } & { { \ } } \\ { { c _ { 3 } = - 4 x - 1 ~ , ~ } } & { { d _ { 3 } = - x ~ , } } \\ { { \ } } & { { \ } } \\ { { c _ { 4 } = 2 x + 1 ~ , ~ } } & { { d _ { 4 } = x + 1 / 2 ~ , } } \end{array}
$$

or alternatively

$$
\begin{array} { l l } { { c _ { 1 } = x + 1 / 2 , } } & { { d _ { 1 } = 2 x + 1 , } } \\ { { } } & { { } } \\ { { c _ { 2 } = - x , } } & { { d _ { 2 } = - 4 x - 1 , } } \\ { { } } & { { } } \\ { { c _ { 3 } = - x , } } & { { d _ { 3 } = 2 x + 1 , } } \\ { { } } & { { } } \\ { { c _ { 4 } = x + 1 / 2 , } } & { { d _ { 4 } = 0 . } } \end{array}
$$

After substitution in the 8equations obtained, we find that each of the6 expressions remaining (2 are trivially satisfied) are simply proportional to the follwing cubic polynominal

$$
4 8 x ^ { 3 } + 2 4 x ^ { 2 } - 1 \quad .
$$

Therefore,they have a common solution given by the roots of the cubic equation

$$
4 8 x ^ { 3 } + 2 4 x ^ { 2 } - 1 = 0 \quad .
$$

The real root is given by

$$
\begin{array} { l } { { x = \frac { ( 2 ^ { 1 / 3 } + 2 ^ { - 1 / 3 } - 1 ) } { 6 } } } \\ { { = . 1 7 5 6 \ldots } } \end{array} .
$$

These solutions were first found numerically using the improved Newton-Raphson Method of Bassti et al: This was not completely trivial as the method only works in the neighborhood of a solution. It was combined with a Monte Carlo search to locate the solution. After examining the 2 solutions found,it was straightforward to postulate the exact form shown in Eqs. (4.8) and (4.9). The substitution was made using the program REDUCE.6

The previous procedure is straightforward but complex enough to necessitate the use of algebraic computation to evaluate expressions. In the next section we reformulate the problem using somewhat different techniques and show how the results obtained are actually more general than presented in this section.

# 5. The General Approach Using Lie Groups

5.1.SYMPLECTIC MAPS ACTING ON FUNCTIONS OF PHASE-SPACE

The results we have derived in this paper apply to any Lie group. The Lie group of symplectic maps generated by Hamilton's equations is not the simplest example of a Lie group. In fact,it is an infinite dimensional Lie group since any function used for the Hamiltonian will generate a symplectic map. Nevertheless, we will see how to rephrase in group language the problem of canonical integration by looking at Hamiltonian dynamics.

We start with Hamilton's equations,

$$
\frac { d { \bf z } } { d t } = \left[ { \bf z } , H \right] ,
$$

where $[ f , g ]$ denotes the Poisson bracket,and $\mathbf { z }$ is a vector composed of the coordinates and momenta. Equation (5.1) can be rewritten as

$$
\frac { d { \bf z } } { d t } = : - { \cal H } : { \bf z } \quad ,
$$

where

$$
: - H ( \mathbf { z } ) : g ( \mathbf { z } ) = [ - H ( \mathbf { z } ) , g ( \mathbf { z } ) ] \ .
$$

In equations (5.1)-(5.3) the Poisson brackets are taken with respect to $\mathbf { z }$ To turn equation (5.1) into an equation involving symplectic maps,we must use a succession of tricks? First,we will look for a map $M ( t )$ which acts on functions of $\mathbf { z } _ { o }$ and propagates them in time according to (5.1):

$$
g ( { \bf z } ( t ) ) = M ( t ) g ( { \bf z } _ { o } ) \quad .
$$

Since $g$ has no explicit time dependence, it is also propagated in time with the Poisson bracket,

$$
\frac { d g } { d t } = [ g , H ] ~ .
$$

If we substitute (5.4) into (5.5),we find

$$
\begin{array} { c } { \displaystyle \frac { d M } { d t } g ( { \bf z } _ { o } ) = \left[ M g ( { \bf z } _ { o } ) , H ( M { \bf z } _ { o } ; t ) \right] } \\ { \displaystyle = \left[ M g ( { \bf z } _ { o } ) , M H ( { \bf z } _ { o } ; t ) \right] } \\ { \displaystyle = M \left[ g ( { \bf z } _ { o } ) , H ( { \bf z } _ { o } ; t ) \right] _ { { \bf z } _ { o } } } \\ { \displaystyle = M : - H ( { \bf z } _ { o } ; t ) : g ( { \bf z } _ { o } ) } \end{array}
$$

To go from (5.5) to (5.6),we use (5.4). Equation (5.7) is a tautology coming from the definition of $M$ . Finally (5.8) is simply the invariance of the Poisson bracket under symplectic transformations. We can proceed one step further by realizing that $g ( \mathbf { z } _ { 0 } )$ is an arbitrary function of $\mathbf { z } _ { o }$ ，

$$
\frac { d M } { d t } = M : - H ( \mathbf { z } _ { o } ; t ) : \quad .
$$

Equation (5.1O) is the starting point of a Lie algebraic treatment of classical dynamics. It is important to emphasize that $M$ acts on functions of $\mathbf { z } _ { o }$ and transforms their functional form in conformity with (5.5).

# 5.2．THE ONE-MAP INTEGRATOR

Here to simplify the notation,we will restrict ourselves to time-independent Hamiltonians. As previously shown ,it is often possible to apply the time-independent formulae by extending the phase-space.

Formally, we can solve (5.10) in the time independent case. In fact the solution is just

$$
M ( t ) \dot { = } \exp ( : - t H ( \mathbf { z } _ { o } ) : ) .
$$

The trouble with Equation (5.11） resides in the impossibility of evaluating $M ( t ) { \bf z } _ { o }$ for an arbitrary $H$ . Symplectic integration consists in replacing $M ( t )$ by a product of symplectic maps which approximates $M ( t )$ to a given order and such that each factor can be exactly and explicitly evaluated on the function ${ \bf z } _ { o }$

The frst case to consider is the one-map approximation of $M ( t )$ . Imagine that we have found a map $N ( t )$ such that

$$
M ( t ) = N ( t ) + O ( t ^ { k + 1 } ) ,
$$

and that ${ \cal N } ( t ) { \bf z } _ { o }$ is a well-known function of ${ \bf z } _ { o }$ and $t$ . Then $N ( t )$ isa $k ^ { t h }$ order

integration step,

$$
\begin{array} { r } { N ( t ) = M _ { k } ( t ) \quad . } \end{array}
$$

To illustrate this particularly simple case, consider the one-dimensional Hamiltonian given by

$$
H = { \frac { ( p - f ( q ) ) ^ { 2 } } { 2 } } + v ( q ) ~ .
$$

To construct a first order integration step, we can approximate the map produced by $H$ with a simple characteristic function,

$$
\begin{array} { c } { { F ( q , \bar { p } ) = q \bar { p } + t H ( q , \bar { p } ) \quad , } } \\ { { { } } } \\ { { { \bf z } _ { o } = ( q , p ) \quad , } } \\ { { { } } } \\ { { { \bf z } ( t ) = ( \bar { q } , \bar { p } ) \quad . } } \end{array}
$$

The map produced by $F ( q , { \bar { p } } )$ can be written down explicitly. In this case $M _ { 1 } ( t )$ is just given by

$$
\begin{array} { l } { { \bar { q } = M _ { 1 } ( t ) \dot { q } = q + \displaystyle \frac { t ( p - f - t v ^ { \prime } ) } { 1 - t f ^ { \prime } } \quad , } } \\ { { \bar { p } = M _ { 1 } ( t ) p = \displaystyle \frac { p - t ( v ^ { \prime } + f f ^ { \prime } ) } { 1 - t f ^ { \prime } } \quad . } } \end{array}
$$

In Equation (5.16), the prime indicates a derivative with respect to $q$ . From this example, we see that the techniques used to fabricate symplectic maps are central to the discovery of explicit symplectic integrators. It should be noticed that (5.15) is always a frst order approximation of the map generated by $H$ . However, for an arbitrary $H$ , it is not always possible to invert explicitly the equations obtained from the characteristic function $F$ ．Nevertheless,it is possible to use (5.15) in conjunction with a Newton search procedure. This is much slower than any explicit techniques. The higher order generalization of (5.15) of Channell and Scovel4 are based on the idea of one-map implicit integration.

# 5.3. THE TWO-MAPS INTEGRATOR

Let us suppose that we can not find a symplectic approximation of $H$ Nevertheless, let us assume that we can split $H$ into two pieces which can be solved exactly when considered as independent Hamiltonians,

$$
H = H _ { 1 } + H _ { 2 } \quad ,
$$

$$
\exp ( - t : H _ { i } : ) = N _ { i } ( t ) .
$$

Can we make an approximation to $M ( t )$ using both $N _ { 1 }$ and $N _ { 2 }$ ? Furthermore, can we in a consistent manner work out an approximation of first,second, third or even fourth order in $t \left( k = 1 , \ldots , 4 \right)$ ？

The answer to these questions is yes and depends only on the Lie group structure of the symplectic group,which is the ability to write maps in the neighborhood of the identity as the exponent of some Poisson bracket operator. First,let us introduce the Campbell-Baker-Hausdorff formula (CBH). The CBH formula allows us to combine the exponent of two Lie group elements of the form $\exp ( A )$ ,where $A$ is some operator. In fact let us consider two group elements $\exp ( \epsilon A )$ and $\exp ( \epsilon B )$ ， then the product $\exp ( C )$ , is approximated by a formula involving only commutators,

$$
\exp ( C ) = \exp ( \epsilon A ) \exp ( \epsilon B ) \quad ,
$$

$$
\begin{array} { c } { { C = \epsilon A + \epsilon B + \displaystyle \frac { \epsilon ^ { 2 } } { 2 } \{ A , B \} + \displaystyle \frac { \epsilon ^ { 3 } } { 1 2 } \Biggl \{ \{ B , A \} , A \Biggr \} + \displaystyle \frac { \epsilon ^ { 3 } } { 1 2 } \Biggl \{ B , \{ B , A \} \Biggr \} } } \\ { { - \displaystyle \frac { \epsilon ^ { 4 } } { 2 4 } \Biggl \{ B , \{ B , A \} , A \Biggr \} \Biggr \} + \ldots { \cal O } ( \epsilon ^ { 5 } ) , } } \end{array}
$$

$$
\{ A , B \} = A B - B A \quad .
$$

The formulas given in (5.19)-(5.21) will allow us to derivecanonical integration techniques valid for any Lie group because they do not depend on the symplectic structure.

To do this we need one more property of the Poisson bracket,

$$
\{ : f : , : g : \} = : [ f , g ] : \quad .
$$

Now, consider the following approximation of $M$ ：

$$
\begin{array} { l } { { N ( t ) = N _ { 1 } ( t ) N _ { 2 } ( t ) } } \\ { { { } ~ } } \\ { { { } ~ = \exp ( - t : H _ { 1 } : ) \exp ( : - t H _ { 2 } : ) } } \\ { { { } ~ = \exp ( - { } _ { : } t H + { \frac { t ^ { 2 } } { 2 } } ^ { 2 } [ H _ { 1 } , H _ { 2 } ] + . . . : ) } } \\ { { { } ~ { } ~ } } \\ { { { } ~ = M ( t ) + O ( t ^ { 2 } ) = M _ { 1 } ( t ) ~ . } } \end{array}
$$

Clearly, Equation (5.23) leads to a frst order integrator.Now,let us symmetrize $N ( t )$

$$
\begin{array} { r l } & { N ( t ) = N _ { 1 } ( \frac { t } { 2 } ) N _ { 2 } ( t ) N _ { 1 } ( \frac { t } { 2 } ) } \\ & { \qquad = \exp \biggl ( \cdot - \frac { t } { 2 } H _ { 1 } : \biggr ) \exp ( \cdot - t H _ { 2 } : ) \exp \biggl ( \cdot - \frac { t } { 2 } H _ { 1 } : \biggr ) + O ( t ^ { k + 1 } ) } \\ & { \qquad = \exp \biggl ( \cdot - t \biggl ( \frac { H _ { 1 } } { 2 } + H _ { 2 } \biggr ) + \frac { t ^ { 2 } } { 4 } [ H _ { 1 } , H _ { 2 } ] + O ( t ^ { 3 } ) : \biggr ) \exp \biggl ( \cdot - \frac { t } { 2 } H _ { 1 } : \biggr ) } \\ & { \qquad = \exp \biggl ( \cdot - t H + \frac { t ^ { 2 } } { 4 } [ H _ { 1 } , H _ { 2 } ] + \frac { t ^ { 2 } } { 4 } [ H _ { 2 } , H _ { 1 } ] + O ( t ^ { 3 } ) : \biggr ) } \\ & { \qquad = \exp ( \colon - t H + O ( t ^ { 3 } ) : ) = M _ { 2 } ( t ) ~ . } \end{array}
$$

This new approximation which we can properly call the generalized leap-frog is quadratic. In fact, it is straightforward to show that any symmetrized product cannot have even powers of $t$ in the Lie operator.

It is clear that all the results of the previous sections which were derived with the help of a generating function and seemed to apply in a very restrictive manner to the special Hamiltonian used,are in fact very general. Not only do they extend to the entire symplectic group but also to other Lie groups as well.

While the group approach cleans up the conceptual side of the problem, it is also true that it provides a simple derivation of the 4th order integrator. We start with the following symmetrized ansatz:

$$
N ( t ) = \exp ( A ) \exp ( B ) \exp ( \alpha A ) \exp ( \beta B ) \exp ( \alpha A ) \exp ( B ) \exp ( A ) \quad ,
$$

$$
2 ( 1 + \alpha ) A = - t : H _ { 1 } : ,
$$

$$
( 2 + \beta ) B = - t : H _ { 2 } : \ .
$$

From the CBH formula, we deduce that to order $t ^ { 3 }$ there can be only four terms in the exponent of $N ( t )$ . Consequently, in addition to (5.26) and (5.27) which take care of order $t$ terms, we can find two additional equations using the $t ^ { 3 }$ terms. These equations are determined by setting the triple commutations of (5.26) and (5.27) to zero and are given by

$$
- \frac { \beta \alpha ^ { 2 } } { 6 } + \frac { 2 \alpha ^ { 2 } } { 3 } - \frac { \alpha \beta } { 3 } - \frac { 2 \alpha } { 3 } - \frac { \beta } { 6 } - \frac { 1 } { 3 } = 0 \quad ,
$$

$$
{ \frac { \beta ^ { 2 } \alpha } { 6 } } + { \frac { \beta ^ { 2 } } { 6 } } - { \frac { \alpha \beta } { 3 } } - { \frac { \alpha } { 3 } } + { \frac { 2 \beta } { 3 } } + { \frac { 2 } { 3 } } = 0 ~ .
$$

Solving for $\beta$ using (5.28) and substituting into (5.29) gives the following results:

$$
\beta = { \frac { 4 \alpha ^ { 2 } - 4 \alpha - 2 } { ( \alpha + 1 ) ^ { 2 } } } \quad ,
$$

$$
{ \frac { \alpha ( \alpha ^ { 3 } - 3 \alpha ^ { 2 } + 3 \alpha + 1 ) } { ( \alpha + 1 ) ^ { 3 } } } = 0 .
$$

Equations (5.30) and (5.31) admit one useful real solution which is given by $\alpha = 1 - 2 ^ { 1 / 3 }$ . For that value $N ( t )$ is just

$$
\begin{array} { l } { { { \cal N } ( t ) = { \cal N } _ { 1 } \displaystyle \left( \frac { t } { 2 ( 1 + \alpha ) } \right) { \cal N } _ { 2 } \left( \displaystyle \frac { t } { 1 + \alpha } \right) { \cal N } _ { 1 } \left( \displaystyle \frac { \alpha t } { 2 ( 1 + \alpha ) } \right) { \cal N } _ { 2 } \left( \displaystyle \frac { ( \alpha - 1 ) t } { ( 1 + \alpha ) } \right) } } \\ { { ~ \times { \cal N } _ { 1 } \left( \displaystyle \frac { \alpha t } { 2 ( 1 + \alpha ) } \right) { \cal N } _ { 2 } \left( \displaystyle \frac { t } { 1 + \alpha } \right) { \cal N } _ { 1 } \left( \displaystyle \frac { t } { 2 ( 1 + \alpha ) } \right) } } \\ { { ~ = { \cal M } ( t ) + { \cal O } ( t ^ { 5 } ) = { \cal M } _ { 4 } ( t ) ~ . } } \end{array}
$$

Equation (5.32) is precisely the solution found in Section 4.

# 5.4. THE N-MAPS INTEGRATOR

We have seen how to generate a 4th order two-maps integrator using only the Lie group structure. For three-maps integrators, the best one can do is to symmetrize the expression of a single step,

$$
H = H _ { 1 } + H _ { 2 } + H _ { 3 } \quad ,
$$

$$
N _ { i } ( t ) = \exp ( - t : H _ { i } : ) \quad ,
$$

$$
M ( t ) = N _ { 1 } ( \frac { t } { 2 } ) N _ { 2 } ( \frac { t } { 2 } ) N _ { 3 } ( t ) N _ { 2 } ( \frac { t } { 2 } ) N _ { 1 } ( \frac { t } { 2 } ) + O ( t ^ { 3 } ) .
$$

In general, the $N$ -maps symmetrized integrator is always quadratic.

As a final remark: recall that we said that the maps $N _ { i }$ must equal $e ^ { : - t H _ { \uparrow } : }$ ； in general they need to be only an approximation of $e ^ { : - t H _ { i } : }$ belonging to the Lie group and of an order greater than the order of the method of integration.

# 5.5．EXAMPLES OF SOME IMPORTANT HAMILTONIANS

Our task is reduced to finding ways to decompose standard Hamiltonians in pieces which can be computed either exactly or approximated by some other symplectic maps.

Let us start with a very important case in the theory of circular particle accelerators: the Hamiltonian for a sector bending magnet which might also have other fields present (quadrupole,sextupole ...). In this case

$$
\begin{array} { c } { { H = H _ { 1 } + H _ { 2 } \quad , } } \\ { { H _ { 1 } = - \displaystyle \left( 1 + \frac { x } { \rho } \right) \sqrt { ( 1 + \delta ) ^ { 2 } - p _ { x } ^ { 2 } - p _ { y } ^ { 2 } } - \frac { p _ { \tau } } { \beta _ { o } } \quad , } } \\ { { H _ { 2 } = \displaystyle \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } + \frac { x } { \rho } - V ( x , y ) \quad , } } \\ { { ( 1 + \delta ) ^ { 2 } = 1 - \displaystyle \frac { 2 p _ { \tau } } { \beta _ { o } } + p _ { \tau } ^ { 2 } \quad , \quad \beta _ { o } = \displaystyle \frac { v _ { o } } { c } . } } \end{array}
$$

This Hamiltonian generates the motion of the variables $\left( x , p _ { x } , y , p _ { y } , \tau , p _ { \tau } \right)$ .The time-like variable is the path length variable s measuring the distance along the design orbit. The dynamics of $H _ { 1 }$ or $H _ { 2 }$ is exactly solvable. In fact, $H _ { 1 }$ is just a rotation in polar coordinates.

It is customary and sometimes convenient to replace $H$ by an expanded Hamiltonian which exact in $1 + \delta$ but only quadratic in the transverse momenta,

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \mathcal { H } = \mathcal { H } _ { 1 } + \mathcal { H } _ { 2 } } } \\ { { } } & { { } } & { { \displaystyle \mathcal { H } _ { 1 } = \frac { p _ { x } ^ { 2 } + p _ { y } ^ { 2 } } { 2 ( 1 + \delta ) } - \frac { p _ { \tau } } { \beta _ { o } } - \delta \quad , } } \\ { { } } & { { } } & { { \displaystyle \mathcal { H } _ { 2 } = - \frac { \delta x } { \rho } + \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } - V ( x , y ) \quad . } } \end{array}
$$

Again,both $\mathcal { H } _ { 1 }$ and $\mathcal { H } _ { 2 }$ are exactly solvable. Interestingly,another division of $\mathcal { H }$ is possible,

$$
\begin{array} { l } { { \displaystyle \mathcal { H } _ { 1 } = \frac { p _ { x } ^ { 2 } + p _ { y } ^ { 2 } } { 2 ( 1 + \delta ) } - \frac { p _ { \tau } } { \beta _ { o } } - \delta - \frac { \delta x } { \rho } - \frac { x ^ { 2 } } { 2 \rho ^ { 2 } } - V _ { 2 } ( x , y ) \quad , } } \\ { { \displaystyle \mathcal { H } _ { 2 } = - V _ { \ge 3 } ( x , y ) \quad . } } \end{array}
$$

In the division of equations (5.43) and (5.44), the map $N _ { 1 }$ is exactly solvable, giving rise to a $\delta$ -dependent matrix and a time of flight which is quadratic in the betatron variables $\left( x , p _ { x } , y , p _ { y } \right)$

The quantity $V _ { \geq 3 } ( x , y )$ is just the non-linear part of the multipole content and produces a kick. Traditionally, $\mathcal { H } _ { 1 }$ and $\mathcal { H } _ { 2 }$ have been used in the standard “kick codes” for particle tracking in accelerators using a quadratic algorithm. (One thin lens $\left( \mathcal { H } _ { 2 } \right)$ in the middle of each linear element $\left( \mathcal { H } _ { 1 } \right)$ ).

- From the few useful examples which have been studied here,it is quite clear that no general recipe is available for explicit symplectic integrators.

# 6. Concluding Remarks and Acknowledgements

Finally, we conclude with a remark on the time-dependent case. Going back to the general problem, consider Hamilton's equations given by (5.1). We can write the following equivalence:

$$
\frac { d \vec { z } } { d t } = [ \vec { z } , H ( \vec { z } ; t ) ] \quad ,
$$

$$
\begin{array} { r } { \implies \left\{ \begin{array} { c c } { \frac { d { \mathbf { z } } } { d \tau } } & { = \left[ { \mathbf { z } } , H ( { \mathbf { z } } ; t ) + p _ { t } \right] } \\ { \frac { d t } { d \tau } } & { = \left[ t , H + p _ { t } \right] = 1 } \\ { \frac { d p _ { t } } { d \tau } } & { = \left[ p _ { t } , H + p _ { t } \right] = - \frac { \partial H } { \partial t } } \end{array} \right. . } \end{array}
$$

The phase space has been extended to $\mathbf { w } = ( \mathbf { z } , t , p _ { t } )$ ，and the new time-like variable is just 7. The two-maps integration formulae can be used if the motion of either $H _ { 1 } + p _ { t }$ or $H _ { 2 } + p _ { t }$ can be solved exactly. Results of the previous sections were based on an $H _ { 1 }$ depending only on the momenta, hence $H _ { 1 } + p _ { t }$ is solvable and we do regain the time-dependent formulae of the previous sections (See equation 2.4).

As we mentioned,only the Lie structure of the group entered in the integration formulae. Consequently it is possible to use them in other contexts. In particular, it could be applied to the problem of spin motion in a storage ring. In the usual approximation,one neglects the efect of the spin on the orbital motion,but includes the effect of the orbit on the spin. Our method can allow us to write an integrator which not only preserves the symplectic character of the orbital motion, but also forces the spin transfer matrix into SU(2) in the spinor representation or $O ( 3 )$ if the spin is treated as a 3-dimensional vector.

- To conclude, we would like to thank M. Bassetti for his help with the numerical solution of the equations in Section 4, F. Neri for useful discussions and finally R. Warnock for reading the manuscript and for several useful suggestions.

As a final note we would like to add that just prior to submisson of this paper, we learned of results obtained independently which overlap some of the results obtained here.

# REFERENCES

1. H. Goldstein, Classical Mechanics, Addison-Wesley Publishing Co.， New York,1965.   
2. R. D. Ruth, IEEE Trans. on Nucl. Sci.,NS-30, No.4 (1983) 2669.   
3. R. DeVogelaere, Methods of Inlegration Which Preserve the Contact Transformation Property of the IIamilton Equations, N7-ONR-43906.   
4. P. J. Channell and C. Scovel, Los Alamos National Laboratory note LA-UR-88-1828 (1988).   
5.M.Bassetti, R. M. Buonanni and M. Placidi, Nucl. Inst. and Meth. 45 (1966) 93.   
6. A. C. Hearn, REDUCE vers. 3.1, the RAND Corporation, Santa Monica,   
-CA.   
7. A. J. Dragt and E. Forest, J. Math. Phys. 24 (1983) 2734.   
8. J. Candy, University of Alberta, private communication.
