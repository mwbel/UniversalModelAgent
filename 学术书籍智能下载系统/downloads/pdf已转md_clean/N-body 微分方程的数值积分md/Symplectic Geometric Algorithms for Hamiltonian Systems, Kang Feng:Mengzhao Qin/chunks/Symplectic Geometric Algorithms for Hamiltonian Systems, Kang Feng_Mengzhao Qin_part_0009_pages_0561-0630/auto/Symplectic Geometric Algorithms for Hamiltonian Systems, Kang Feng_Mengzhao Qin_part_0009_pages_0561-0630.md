$$
2 H = \sum _ { i = 1 } ^ { 3 } a _ { i } x _ { i } ^ { 2 } + \sum _ { i , j = 1 } ^ { 3 } b _ { i j } ( p _ { i } x _ { j } + x _ { i } p _ { j } ) + \sum _ { i , j = 1 } ^ { 3 } c _ { i j } p _ { i } p _ { j } .
$$

For heavy top, the energy is often expressed as the sum of kinetic energy and potential energy, i.e.,

$$
H ( x , p ) = \frac { x _ { 1 } ^ { 2 } } { 2 I _ { 1 } } + \frac { x _ { 2 } ^ { 2 } } { 2 I _ { 2 } } + \frac { x _ { 3 } ^ { 2 } } { 2 I _ { 3 } } + \gamma _ { 1 } p _ { 1 } + \gamma _ { 2 } p _ { 2 } + \gamma _ { 3 } p _ { 3 } ,
$$

where $I _ { i }$ is the main movement inertia of the rigid body, $\gamma _ { i }$ $( i = 1 , 2 , 3$ ) are three coordinates of the center of mass. It is easy to see that this is a separable system.

The structure matrix of the Lie–Poisson system is

$$
\left[ \begin{array} { c c } { { J ( x ) } } & { { J ( p ) } } \\ { { } } & { { } } \\ { { J ( p ) } } & { { O } } \end{array} \right] ,
$$

where $J ( x )$ is defined in Subsection 12.4.4.

It is difficult to construct Lie–Poisson algorithm on heavy top than on the free rigid body because the generating function methods are no longer suitable. However, it may become easier by the composition method and the Lemma 4.3.

We will first split the Hamiltonian function $H$ of heavy top system into six part $H = \sum _ { i = 1 } ^ { 6 } H _ { i }$ , where

$$
H _ { i } = \frac { x _ { i } ^ { 2 } } { 2 I _ { i } } , H _ { i + 3 } = \gamma _ { i } p _ { i } , i = 1 , 2 , 3 .
$$

We will take $H _ { 1 } , H _ { 4 }$ as examples to construct Lie–Poisson scheme.

First, we will take $H _ { 1 }$ as the Hamilton function, then

$$
\left[ \begin{array} { c } { \dot { x } } \\ { \dot { p } } \end{array} \right] = \left[ \begin{array} { c c } { J ( x ) } & { J ( p ) } \\ { J ( p ) } & { 0 } \end{array} \right] \left[ \begin{array} { c } { \frac { \partial H _ { 1 } } { \partial x } } \\ { 0 } \end{array} \right] ,
$$

after manipulating, we get

$$
\left\{ \begin{array} { l } { x _ { 1 } = 0 , } \\ { x _ { 2 } = \frac { x _ { 3 } x _ { 1 } } { I _ { 1 } } , } \\ { x _ { 3 } = - \frac { x _ { 2 } x _ { 1 } } { I _ { 1 } } , } \\ { p _ { 1 } = 0 , } \\ { p _ { 2 } = \frac { x _ { 1 } p _ { 3 } } { I _ { 1 } } , } \\ { p _ { 3 } = - \frac { x _ { 1 } p _ { 2 } } { I _ { 1 } } . } \end{array} \right.
$$

Theorem 4.4. The Midpoint scheme of (4.22) is Poisson scheme for heavy top.

Proof. By Theorem 1.2, the midpoint scheme is the Poisson scheme iff mapping

$$
( x , p ) \longrightarrow ( { \widehat { x } } , { \widehat { p } } )
$$

satisfies

$$
\left[ \begin{array} { l l } { \frac { \partial \widehat { x } } { \partial x } } & { \frac { \partial \widehat { x } } { \partial p } } \\ { \frac { \partial \widehat { p } } { \partial x } } & { \frac { \partial \widehat { p } } { \partial p } } \end{array} \right] \left[ \begin{array} { l l } { J ( x ) } & { J ( p ) } \\ { J ( p ) } & { O } \end{array} \right] \left[ \begin{array} { l l } { \frac { \partial \widehat { x } } { \partial x } } & { \frac { \partial \widehat { p } } { \partial x } } \\ { \frac { \partial \widehat { x } } { \partial p } } & { \frac { \partial \widehat { p } } { \partial p } } \end{array} \right] = \left[ \begin{array} { l l } { J ( \widehat { x } ) } & { J ( \widehat { p } ) } \\ { J ( \widehat { p } ) } & { O } \end{array} \right] .
$$

Denote $\left( \frac { \partial \widehat { y } } { \partial z } \right) = \widehat { y } _ { z }$ , then the expand Equation (4.23),

$$
\left\{ \begin{array} { l l } { \widehat { x } _ { x } J ( x ) \widehat { x } _ { x } ^ { \mathrm { T } } = J ( \widehat { x } ) , } \\ { \widehat { x } _ { x } J ( x ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { x } _ { x } J ( p ) \widehat { p } _ { p } ^ { \mathrm { T } } = J ( \widehat { p } ) , } \\ { \widehat { p } _ { x } J ( x ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { p } _ { p } J ( p ) \widehat { p } _ { x } ^ { \mathrm { T } } + \widehat { p } _ { x } J ( p ) \widehat { p } _ { p } ^ { \mathrm { T } } = 0 . } \end{array} \right.
$$

From the results of Subsection12.4.4, the first equation of system (4.24) is obviously hold. Note also

$$
\widehat { p } _ { x } = \left[ \begin{array} { c c c } { 0 } & { p _ { 2 1 } } & { p _ { 3 1 } } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] , \quad \widehat { p } _ { p } = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { p _ { 2 2 } } & { p _ { 2 3 } } \\ { 0 } & { p _ { 3 2 } } & { p _ { 3 3 } } \end{array} \right] ,
$$

where p21 = $p _ { 2 1 } = \frac { \partial \widehat { p } _ { 2 } } { \partial x _ { 1 } }$ , $p _ { 3 1 } = \frac { \partial \widehat { p } _ { 3 } } { \partial x _ { 1 } }$ $p _ { i j } = \frac { \partial \widehat { p } _ { i } } { \partial p _ { j } } \left( i , j = 2 , 3 \right)$ . Through the computation, we have

$$
\begin{array} { l l } { { p _ { 2 2 } = x _ { 2 2 } , \quad p _ { 2 3 } = x _ { 2 3 } , \quad p _ { 3 2 } = x _ { 3 2 } , \quad p _ { 3 3 } = x _ { 3 3 } , \quad } } \\ { { \mathrm { } } } \\ { { p _ { 2 1 } = { \displaystyle \frac { \tau \widehat { p _ { 3 } } } { I _ { 1 } } } , \quad p _ { 3 1 } = { \displaystyle \frac { - \tau \widehat { p _ { 2 } } } { I _ { 1 } } } , \quad } } \end{array}
$$

where $a$ is defined by the Euler scheme (4.16).

Substituting (4.25) into Equation (4.24), the 2nd and 3rd equations of (4.24) are also hold. -

If $H _ { 4 }$ is taken as Hamiltonian function of a system, the equation degenerates into a constant equation. Then constructing Lie–Poisson scheme is trivial.

For a Hamiltonian function of general form, we need to perform a transformation, so that the equation is easier for constructing the Lie–Poisson scheme. Take the free rigid body as the example.

For a quadratic form, we have

$$
H = H _ { i } + H _ { i j } = \frac { 1 } { 2 } a _ { i } x _ { i } ^ { 2 } + \frac { 1 } { 2 } a _ { i j } ( x _ { i } + x _ { j } ) ^ { 2 } ,
$$

i.e., we can eliminate the mixed items and transform it into a sum of squares. Next, we can construct Lie–Poisson scheme for system with $H _ { i j }$ as Hamiltonian function. Take $H _ { 1 2 }$ as an example

$$
\dot { x } = J ( x ) \frac { \partial H _ { 1 2 } } { \partial x } .
$$

It is easy to see that $x _ { 1 } + x _ { 2 }$ is a Casimir function of system. Expanding Equation (4.26) yields

$$
\left[ \begin{array} { c } { \dot { x } _ { 1 } } \\ { \dot { x } _ { 2 } } \\ { \dot { x } _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { - a _ { 1 2 } x _ { 3 } ( x _ { 1 } + x _ { 2 } ) } \\ { a _ { 1 2 } x _ { 3 } ( x _ { 1 } + x _ { 2 } ) } \\ { a _ { 1 2 } ( x _ { 1 } ^ { 2 } - x _ { 2 } ^ { 2 } ) } \end{array} \right] .
$$

Since $x _ { 1 } + x _ { 2 }$ is a constant, denote $c = x _ { 1 } + x _ { 2 }$ , the Equation (4.27) becomes

$$
\left\{ \begin{array} { l l } { \dot { x } _ { 1 } = - c a _ { 1 2 } x _ { 3 } , } \\ { } \\ { \dot { x } _ { 2 } = c a _ { 1 2 } x _ { 3 } , } \\ { } \\ { \dot { x } _ { 3 } = c a _ { 1 2 } ( c - 2 x _ { 2 } ) . } \end{array} \right.
$$

The midpoint scheme to the above equations is no longer Lie–Poisson scheme. However, we can solve system of the Equations (4.28) analytically without difficulty.

# 12.4.6 Other Lie–Poisson Algorithm

Apart from the Lie–Poisson algorithm described above, we have other Lie–Poisson algorithms, which include but not limited to Scovel and MacLaclan[MS95] constrained Hamiltonian algorithm, and Veselov[Ves91b,Ves88] discrete Lagrangian system approach, as well as the reduction method mentioned before. Below, we will give a brief introduction to these method.

# 1. Constrained Hamiltonian algorithm

The detailed description about the constrained Hamiltonian algorithm can be found in literature[MS95] and its references. Here we apply it to rigid motion only.

The structure space for a rigid motion is $S O ( n ) = N$ . Take a larger linear space $M = g l ( n )$ . Then the constraint function of $N$ on $M$ is

$$
\phi ( \boldsymbol { q } ) = \boldsymbol { q } ^ { \mathrm { T } } \boldsymbol { q } - 1 , \quad \forall \ \boldsymbol { q } \in M .
$$

Note that $\phi ( q ) = 0$ on $N$ , and $\mathbf { d } \phi ( q ) = T _ { q } ( M ) \to \mathbf { R }$ is a differential mapping. Assume on $T ^ { * } M$ , there exists a non-constraint system of Hamiltonian equations

$$
\left\{ \begin{array} { l } { \dot { p } = - \partial _ { q } H , } \\ { ~ } \\ { \dot { q } = \partial _ { p } H . } \end{array} \right.
$$

Then on $T ^ { * } N$ , if the local coordinates $( p , q )$ on $T ^ { * } M$ is still used, we should have

$$
\phi ( q ) = 0 \Longrightarrow \mathrm { d } \phi \cdot \dot { q } = \mathrm { d } \phi \cdot \partial _ { p } H = \{ H , \phi \} .
$$

Therefore, on $T ^ { * } M$ , there exists an embedded submanifold

$$
C M = \{ ( p , q ) \in T ^ { * } M : \phi ( q ) = 0 , \{ H , \phi \} = 0 \} ,
$$

which can induce a mapping

$$
\psi : \quad C M \longrightarrow T ^ { * } M , \quad ( p , q ) \longrightarrow ( p _ { - } , q ) ,
$$

where $p _ { - } = \psi ( p , q )$ . It is easy to verify that this is an isomorphic mapping and preserving the symplectic structure.

There exist constrained equations of dynamic system on $C M$ ,

$$
\left\{ \begin{array} { l l } { \dot { q } = \partial _ { p } H , } \\ { ~ } \\ { \dot { p } = - \partial _ { q } H + \mathrm { d } \phi \cdot \mu . } \end{array} \right.
$$

If it is easy to construct structure-preserving scheme for the Equation (4.29) (e.g. when (4.29) is a separable system), then we can use map $\psi$ to induce the algorithm on $T N$ .

Take $S O ( n )$ as an example.

On $^ { T M }$ we have a Lagrangian function $L ( q , \dot { q } ) = \frac { 1 } { 2 } \operatorname { t r } \left( \dot { q } J \dot { q } ^ { \mathrm { T } } \right)$ . Using the Legendre transformation, we can obtain Hamiltonian function $H ( p , q ) = { \frac { 1 } { 2 } } \operatorname { t r } \left( p J ^ { - 1 } p ^ { \mathrm { T } } \right)$ on $T ^ { * } M$ . Therefore, using (4.29), we can obtain the constrained Hamiltonian equation of the dynamic system:

$$
\left\{ { \begin{array} { l } { { \dot { q } } = { \frac { 1 } { 2 } } p J ^ { - 1 } , } \\ { { \dot { p } } = \mathbf { d } \psi \cdot \mu = 2 q \mu , } \end{array} } \right.
$$

which is a separable Hamilton system obviously. It is easy to construct the explicit symplectic difference scheme. But on $T N$ , the Hamiltonian function becomes $H ( p , q ) = \frac { 1 } { 4 } \mathrm { t r } ( I ^ { - 1 } ( q ^ { \mathrm { T } } p ) ( q ^ { \mathrm { T } } p ) ^ { \mathrm { T } } )$ , and its Hamiltonian equations are

$$
\left\{ \begin{array} { l l } { \dot { q } = q I ^ { - 1 } ( q ^ { \mathrm { T } } p ) = \frac { \partial H } { \partial p } , } \\ { \dot { p } = p I ^ { - 1 } ( q ^ { \mathrm { T } } p ) = - \frac { \partial H } { \partial q } , } \end{array} \right.
$$

where $q \in S O ( n )$ , $q ^ { \mathrm { T } } p \in s o ( n )$ . This is not a separable Hamilton system. Therefore, constructing its symplectic difference method will be difficult and computationally complicated. However using (4.30) and maps $\psi$ , we can construct the algorithm for $S O ( n )$ easily. Note that ${ \psi } ( p ) = \frac { 1 } { 2 } ( p - q p ^ { \mathrm { T } } q )$ in this case.

Scovel and McLachlan[MS95] proved this algorithm preserves the momentum mapping. We remark that the constraint Hamiltonian system has advantage only when the expansion system is separable. Otherwise this algorithm is impractical. Take the rigid body as an example. On $T ^ { * } S O ( 3 )$ , if Euler equation is to be solved, there are only 6 unknowns. If we expand it to $T ^ { * } G L ( n )$ , the number of unknown becomes 18. If system is not separable, then the computation cost will definitely increase.

# 2. Veselov–Moser algorithm

Veselov–Moser algorithm $[ \mathrm { M V } 9 1 ]$ is to discretize Lagrange function first and then apply Legendre transformation to the discrete Lagrange function. The constructed algorithm preserves discreted symplectic structure, thus also preserves system’s Lie– Poisson structure. The concrete procedure is as follows:

$1 ^ { \circ }$ First discretize the Lagrange function. $2 ^ { \circ }$ Add constraint and find the solution for $\delta S = 0$ $3 ^ { \circ }$ Obtain the discrete equation. $4 ^ { \circ }$ Solve this equation.

For $S O ( n )$ , $S = \sum _ { k = 1 } ^ { n } \operatorname { t r } \left( X _ { k } J X _ { k + 1 } ^ { \mathrm { T } } \right)$ . The constrained Lagrange function is

$$
L = S + \sum _ { k = 1 } ^ { n } ( X _ { k } X _ { k } ^ { \mathrm { T } } - 1 ) ,
$$

then

$$
\delta L = 0 \Longrightarrow X _ { k + 1 } J + X _ { k - 1 } J = \Lambda _ { k } X _ { k } , \quad \forall \ k \in { \bf Z } ,
$$

from this, we can have a system of equations

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { M _ { k + 1 } = w _ { k } M _ { k } w _ { k } ^ { - 1 } , } \\ { M _ { k } = w _ { k } ^ { \mathrm { T } } J - J w _ { k } , } \end{array} \right. \quad w _ { k } \in O ( n ) , } \end{array}
$$

where $w _ { k } = X _ { k + 1 } ^ { - 1 } X _ { k }$ . It is easy to prove that this discrete system of equations converges to continuous system of Euler-Arnold equations:

$$
\left\{ \begin{array} { l l } { \dot { M } = [ M , \Omega ] , } \\ { M = J \Omega + \Omega J , } \end{array} \right. \quad \Omega \in o ( n ) .
$$

To solve Equation (4.32), the key lies in solving for $w _ { k }$ . In order to make iteration $( X _ { k } , Y _ { k } )  ( X _ { k + 1 } , Y _ { k + 1 } )$ symplectic, $Y _ { k } = X _ { k + 1 }$ , we need

$$
Y _ { k + 1 } J + X _ { k } J = \Lambda _ { k } X _ { k + 1 } , \quad \Lambda _ { k } \in S m ( n ) .
$$

This is because

$$
\begin{array} { l l l } { { Y _ { k + 1 } J + X _ { k } J } } & { { = } } & { { X _ { k + 1 } w _ { k + 1 } ^ { \mathrm { T } } J + X _ { k } J } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + X _ { k + 1 } ^ { \mathrm { T } } X _ { k } J ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ) . } } \end{array}
$$

See also

$$
J w _ { k } ^ { \mathrm { T } } - w _ { k } J = M _ { k + 1 } = w _ { k + 1 } ^ { \mathrm { T } } J - J w _ { k + 1 } ,
$$

then

$$
J w _ { k } ^ { \mathrm { T } } + J w _ { k + 1 } = w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ,
$$

i.e., $w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J$ is symmetric. Thus ∃ Λk, $\Lambda _ { k } = \Lambda _ { k } ^ { \mathrm { T } }$ , so that

$$
X _ { k + 1 } ( w _ { k + 1 } ^ { \mathrm { T } } J + w _ { k } J ) = \Lambda _ { k } X _ { k + 1 } .
$$

Therefore,

$$
Y _ { k + 1 } J + X _ { k } J = \Lambda _ { k } X _ { k + 1 }
$$

satisfies symplectic condition.

The next question is how to solve $w _ { k } ^ { \mathrm { T } } J - J w _ { k } = M _ { k } = t m _ { k }$ for $w _ { k } ?$ The numerical experiments show that not all solutions $w _ { k }$ that satisfy Equations (4.32) are the solutions we want. To solve $\omega _ { k }$ quickly, we propose to use the Quaternion method. $w \in S O ( 3 )$ corresponds to an element $q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } )$ in $S H _ { 1 }$ . Their relations will be given in Section 12.5. Then the second equation in Equation (4.32) becomes

$$
\left\{ \begin{array} { l l } { 2 ( \alpha _ { 2 } - \alpha _ { 1 } ) q _ { 2 } q _ { 1 } + 2 ( \alpha _ { 1 } + \alpha _ { 2 } ) q _ { 3 } q _ { 0 } = - \delta t m _ { 3 } , } \\ { 2 ( \alpha _ { 3 } - \alpha _ { 1 } ) q _ { 3 } q _ { 1 } - 2 ( \alpha _ { 3 } + \alpha _ { 1 } ) q _ { 2 } q _ { 0 } = \delta t m _ { 2 } , } \\ { 2 ( \alpha _ { 3 } - \alpha _ { 2 } ) q _ { 3 } q _ { 2 } + 2 ( \alpha _ { 3 } + \alpha _ { 2 } ) q _ { 1 } q _ { 0 } = - \delta t m _ { 1 } , } \end{array} \right.
$$

in addition,

$$
q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } = 1 .
$$

Solving the above nonlinear equations for $\left( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } \right)$ is not an easy task. We found that when iteration step size is small, $q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 }$ behaves reasonable. However, when the step size is large, the solution behaves erratically. Numerical experiments show that solving these nonlinear equations is quite time-consuming, and hence this method is not recommended in practice.

# 3. Reduction method

Reduction method bases on the momentum mapping discussed in previous sections. We have mentioned that the solution of a Lie–Poisson system lies in a coadjoint orbit in Section 12.2, and this orbit has non-degenerated symplectic structure. If we can construct the symplectic algorithm on this reduced orbit, then this algorithm is naturally Lie–Poisson. Moreover it preserves the Casimir function and also preserves the orbit. Below, we will take $S O ( 3 )$ as an example to illustrate this method.

The coadjoint orbit of $S O ( 3 )$ is a two dimensional spherical surface $S _ { 2 } ^ { r }$ . On $S _ { 2 } ^ { r }$ , we have a symplectic structure

$$
\omega _ { \mu } ( \xi _ { \mathbf { g } ^ { * } } ( \mu ) , \eta _ { \mathbf { g } ^ { * } } ( \mu ) ) = - \mu [ \xi , \eta ] ,
$$

and Hamiltonian function

$$
H _ { \mu } ( A d _ { g ^ { - 1 } } ^ { * } \mu ) = \frac { 1 } { 2 } I ^ { - 1 } ( A d _ { g ^ { - 1 } } ^ { * } \mu ) ^ { 2 } ,
$$

where $A d _ { g ^ { - 1 } } ^ { * } \mu$ denotes an element on $S _ { 2 } ^ { r }$ .

How to choose the chart and local coordinate on $S _ { 2 } ^ { r }$ , so that the symplectic structure becomes simple, is very important. We once selected the spherical coordinate to be the local coordinate and the corresponding symplectic structure and Hamiltonian function become very complicated. However, if the Euler angle coordinate is used, the equations become very simple.

Let

$$
S _ { 2 } ^ { r } = \{ ( x , y , z ) ~ | ~ x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = r ^ { 2 } \} ,
$$

where $x , y , z$ are three angular momentums in the body description. Using Euler angle coordinate $\theta , \psi$ to do the following coordinate transformation:

$$
\left\{ \begin{array} { l l } { x = r \sin \theta \cos \varphi , } \\ { y = r \sin \theta \sin \varphi , } \\ { z = r \cos \theta . } \end{array} \right.
$$

Lie–Poisson (Euler) equation may become the following Hamiltonian equations:

$$
\left\{ \begin{array} { l } { \displaystyle \dot { \theta } = - \frac { 1 } { r \sin \theta } \frac { \partial H } { \partial \varphi } , } \\ { \displaystyle \dot { \varphi } = \frac { 1 } { r \sin \theta } \frac { \partial H } { \partial \theta } , } \end{array} \right.
$$

where

$$
H = { \frac { 1 } { 2 } } \left( { \frac { r ^ { 2 } \sin ^ { 2 } \theta \cos ^ { 2 } \varphi } { I _ { 1 } } } + { \frac { r ^ { 2 } \sin ^ { 2 } \theta \sin ^ { 2 } \varphi } { I _ { 2 } } } + { \frac { r ^ { 2 } \cos ^ { 2 } \theta } { I _ { 3 } } } \right) .
$$

We can construct a non-standard symplectic algorithm for Equations (4.34) or we can simplify the problem further by transformation

$$
( \theta , \varphi )  ( \cos \theta , \varphi ) = ( x _ { 1 } , x _ { 2 } ) ,
$$

then

$$
\left\{ \begin{array} { l l } { \frac { \mathrm { d } x _ { 1 } } { \mathrm { d } t } = \frac { 1 } { r } \frac { \partial H } { \partial x _ { 2 } } , } \\ { \frac { \mathrm { d } x _ { 2 } } { \mathrm { d } t } = - \frac { 1 } { r } \frac { \partial H } { \partial x _ { 1 } } . } \end{array} \right.
$$

This is a Hamiltonian system with standard symplectic structure, and its symplectic algorithm is easy to construct.

To sum up, constructing Lie–Poisson scheme for a Lie–Poisson system has three methods. The first method is to lift it to $T ^ { * } G$ and construct the symplectic algorithm (includes constraint Hamiltonian method) on it. The second is the direct construction based on $\mathbf { g } ^ { * }$ (generating function method and composition method). The third is to construct symplectic algorithm on the reduced coadjoint orbit.

# 12.5 Relation Among Some Special Group and Its Lie Algebra

In this section, we present relation among special group and its Lie algebra.

# 12.5.1 Relation Among $S O ( 3 ) , s o ( 3 )$ and $S H _ { 1 } , S U ( 2 )$

Let

$$
\begin{array} { l } { { \Lambda \in S O ( 3 ) , \quad \Lambda \Lambda = 1 , \quad | \Lambda | = 1 , } } \\ { { \nonumber } } \\ { { \widehat { \xi } \in s o ( 3 ) \Longrightarrow \widehat { \xi } + \widehat { \xi } ^ { \mathrm { T } } = 0 , } } \end{array}
$$

$q \in S H _ { 1 }$ is a normal Quaternion $q = ( q _ { 0 } , \overline { { { q } } } ) = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } ) , \overline { { { q } } } = ( q _ { 1 } , q _ { 2 } , q _ { 3 } ) ,$

$$
q _ { 0 } ^ { 2 } + \lVert \overline { { q } } \rVert ^ { 2 } = 1 = q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + q _ { 3 } ^ { 2 } .
$$

We assume

$$
\forall \xi \in \mathbf { R } ^ { 3 } , \quad \xi = ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } ) \Longrightarrow \widehat { \xi } = \left[ \begin{array} { c c c } { 0 } & { - \xi _ { 3 } } & { \xi _ { 2 } } \\ { \xi _ { 3 } } & { 0 } & { - \xi _ { 1 } } \\ { - \xi _ { 2 } } & { \xi _ { 1 } } & { 0 } \end{array} \right] \in s o ( 3 ) ,
$$

$\xi$ is called the axial quantity of ${ \widehat { \xi } } .$ When $\widehat { A } \in s o ( 3 )$ , $A$ expresses its axial quantity.

# 1. Transformation between $S O ( 3 )$ and $S H _ { 1 }$

$\forall ~ q \in S H _ { 1 }$ , $x \in \mathrm { ~ } q _ { 0 } \simeq \mathbf { R } ^ { 3 }$ , $q x q ^ { - 1 }$ represents a rotation of $x$ . Using isomorphic mapping:

$$
{ \cal A } ( q ) = \left[ \begin{array} { c c } { { q _ { 0 } + q _ { 1 } \mathrm { i } } } & { { q _ { 2 } + q _ { 3 } \mathrm { i } } } \\ { { - q _ { 2 } + q _ { 3 } \mathrm { i } } } & { { q _ { 0 } - q _ { 1 } \mathrm { i } } } \end{array} \right] , \quad H \simeq { \bf C } ^ { 2 } ,
$$

we can obtain $\forall ~ q \in H , \exists \Lambda \in S O ( 3 ) , \forall ~ x \in$ , we have

$$
A ( q x q ^ { - 1 } ) = A ( 0 , \Lambda x ) .
$$

From this we can get $\Lambda$ .

Given $q = ( q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 } )$ , then

$$
\Lambda = 2 \left[ \begin{array} { c c c c } { { q _ { 0 } ^ { 2 } + q _ { 1 } ^ { 2 } - \frac { 1 } { 2 } } } & { { q _ { 1 } q _ { 2 } - q _ { 0 } q _ { 3 } } } & { { q _ { 0 } q _ { 2 } + q _ { 1 } q _ { 3 } } } \\ { { } } & { { } } & { { } } \\ { { q _ { 1 } q _ { 2 } + q _ { 0 } q _ { 3 } } } & { { q _ { 0 } ^ { 2 } + q _ { 2 } ^ { 2 } - \frac { 1 } { 2 } } } & { { q _ { 2 } q _ { 3 } - q _ { 0 } q _ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { q _ { 1 } q _ { 3 } - q _ { 0 } q _ { 2 } } } & { { q _ { 0 } q _ { 1 } + q _ { 2 } q _ { 3 } } } & { { q _ { 0 } ^ { 2 } + q _ { 3 } ^ { 2 } - \frac { 1 } { 2 } } } \end{array} \right] ,
$$

or simplify as

$$
\Lambda = ( 2 q _ { 0 } ^ { 2 } - 1 ) 1 + 2 q _ { 0 } \widehat { q } + 2 q \otimes q .
$$

It is easy to see that, if $\Lambda = ( \Lambda _ { i j } )$ is known, then

$$
\left. \begin{array} { l } { q _ { 0 } = \frac { 1 } { 2 } \sqrt { 1 + \operatorname { t r } \Lambda } , } \\ { q _ { 1 } = \frac { \left( Q _ { 3 2 } - Q _ { 2 3 } \right) } { 4 q _ { 0 } } } \\ { q _ { 2 } = \frac { \left( Q _ { 1 3 } - Q _ { 3 1 } \right) } { 4 q _ { 0 } } } \\ { q _ { 3 } = \frac { \left( Q _ { 2 1 } - Q _ { 1 2 } \right) } { 4 q _ { 0 } } } \end{array} \right\} \Longrightarrow q = \frac { 1 } { 4 q _ { 0 } } ( \Lambda - \Lambda ^ { \operatorname { T } } ) .
$$

# 2. Relation between $s o ( 3 )$ and $S O ( 3 )$

The relation between $s o ( 3 )$ and $S O ( 3 )$ is the relation between Lie algebra and Lie group. Let $\widehat { \xi }$ be an antisymmetry matrix for the axial quantity $\bar { \xi }$ , then $\exp \left( \widehat { \varepsilon } \right)$ denotes a rotation in $S O ( 3 )$ . We have the expansion

$$
\exp \left( { \widehat { \xi } } \right) = \sum _ { n = 0 } ^ { \infty } { \frac { 1 } { n ! } } { \widehat { \xi } } ^ { n } \in S O ( 3 ) .
$$

According to the properties of $S O ( 3 )$ , this expansion has a closed form, i.e., the Rodrigue formula

$$
\Lambda = \exp \left( \widehat { \xi } \right) = 1 + \frac { \sin \| \xi \| } { \| \xi \| } \widehat { \xi } + \frac { 1 } { 2 } \frac { \sin ^ { 2 } \left( \frac { 1 } { 2 } \| \xi \| \right) } { \left( \frac { 1 } { 2 } \| \xi \| \right) ^ { 2 } } \widehat { \xi } ^ { 2 } .
$$

We have two proofs of the above formula: one is from the geometry point of view and the other is from algebra point of view. Below, we will give details on the algebraic proof.

$\forall \widehat { \xi } \in s o ( 3 )$ , the following results hold after simple calculations:

$$
\widehat { \xi } ^ { 3 } = - \widehat { \xi } , \widehat { \xi } ^ { 4 } = - \widehat { \xi } ^ { 2 } , | \xi | = 1 .
$$

Substitute them into the above series expansion,

$$
\begin{array} { l } { { \exp \left( \widehat { \xi } \right) = \exp \left( \left\| \xi \right\| \cdot \widehat { n } \right) \left( n = \displaystyle \frac { \xi } { \| \xi \| } \right) } } \\ { { = 1 + \sin \left\| \xi \right\| \widehat { n } + \left( 1 - \cos \left\| \xi \right\| \right) \widehat { n } ^ { 2 } } } \\ { { = 1 + \displaystyle \frac { \sin \left\| \xi \right\| } { \left\| \xi \right\| } \widehat { \xi } + \displaystyle \frac { 1 } { 2 } \frac { \sin ^ { 2 } \displaystyle \frac { 1 } { 2 } \| \xi \| } { \left( \displaystyle \frac { 1 } { 2 } \| \xi \| \right) ^ { 2 } } \widehat { \xi } ^ { 2 } . } } \end{array}
$$

We can prove that $\| \xi \|$ is the angle of rotation $\exp \left( \widehat { \xi } \right)$ .

# 3. Transformation between $S O ( 3 )$ and $S H _ { 1 }$

The relation between $S O ( 3 )$ and $S H _ { 1 }$ is manifested by the relation between $s o ( 3 )$ and $S H _ { 1 }$ . A rotation in $S O ( 3 )$ , $( \theta , n )  ( \| \xi \| , \xi )$ ,

$$
\begin{array} { r c l } { { \forall \left( \| \xi \| , \xi \right) \in S O ( 3 ) \implies \widehat { \xi } \in s o ( 3 ) } } & { { } } & { { } } \\ { { } } & { { } } & { { } } \\ { { \implies q _ { 0 } = \cos \frac { 1 } { 2 } \| \xi \| , } } & { { } } \\ { { } } & { { } } & { { } } \\ { { q } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \left( \frac { \sin \displaystyle \frac { 1 } { 2 } \| \xi \| } { \displaystyle \frac { 1 } { 2 } \| \xi \| } \right) \xi . } } \end{array}
$$

When $\| \xi \| \ll 1$ , we use

$$
{ \frac { \sin x } { x } } = 1 - { \frac { x ^ { 2 } } { 6 } } + { \frac { x ^ { 4 } } { 1 2 0 } } - { \frac { x ^ { 6 } } { 5 0 4 0 } }
$$

to deal with the singularity situation.

If $q _ { 0 } ^ { 2 } + \| q \| ^ { 2 } \neq 1$ , normalization is needed, which is just divided by $\sqrt { q _ { 0 } ^ { 2 } + \| q \| ^ { 2 } }$

Given $( q _ { 0 } , q ) \in S H _ { 1 }$ , we need to solve for $\widehat { \xi }$ . Since $\xi$ has the same direction as $q$ , we have

$$
\xi = \| \xi \| { \frac { q } { \| q \| } } ,
$$

where $\| \xi \|$ can be given by $\left\| \xi \right\| = 2 \sin ^ { - 1 } ( \left\| q \right\| )$ .

# 12.5.2 Representations of Some Functions in $S O ( 3 )$

By definition, we have

$$
\begin{array} { l } { { \displaystyle i e x ( \xi ) = \sum _ { n = 0 } ^ { \infty } \frac { \xi ^ { n } } { ( n + 1 ) ! } , } } \\ { { \displaystyle \chi ( \xi ) i e x ( - \xi ) = I d _ { \xi } . } } \end{array}
$$

For ${ \widehat { \xi } } \in s o ( 3 )$ , from $\left( \frac { \widehat { \xi } } { | | \xi | | } \right) ^ { 3 } = - \frac { \widehat { \xi } } { | | \xi | | }$ , we have

$$
{ \begin{array} { r l } { i e x ( - { \widehat { \xi } } ) } & { = \displaystyle \sum _ { n = 0 } ^ { \infty } { \frac { ( - { \widehat { \xi } } ) ^ { n } } { ( n + 1 ) ! } } = \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( { \widehat { \xi } } ) ^ { 2 k } } { ( 2 k + 1 ) ! } } + \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( - { \widehat { \xi } } ) ^ { 2 k + 1 } } { ( 2 k + 2 ) ! } } } \\ & { = \displaystyle \ 1 + \displaystyle \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k + 1 } \| \xi \| ^ { 2 k } } { ( 2 k + 1 ) ! } } \left( { \frac { { \widehat { \xi } } } { \| \xi \| } } \right) ^ { 2 } + \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { k + 1 } \| \xi \| ^ { 2 k + 1 } } { ( 2 k + 2 ) ! } } \cdot { \frac { { \widehat { \xi } } } { \| \xi \| } } } \\ & { = \displaystyle \ 1 + { \frac { | \xi | - \sin | \xi | } { | \xi | ^ { 3 } } } { \widehat { \xi } } ^ { 2 } + \displaystyle { \frac { \cos | \xi | - 1 } { | \xi | ^ { 2 } } } { \widehat { \xi } } } \\ & { = \displaystyle \ 1 + c _ { 1 } { \widehat { \xi } } + c _ { 2 } { \widehat { \xi } } ^ { 2 } , } \end{array} }
$$

where c1 = cos |ξ| − 1 , $c _ { 1 } ~ = ~ \frac { \cos ~ | \xi | - 1 } { | \xi | ^ { 2 } } , c _ { 2 } ~ = ~ \frac { | \xi | - \sin ~ | \xi | } { | \xi | ^ { 3 } }$ |ξ| − sin |ξ|3 . χ(ξ) can be obtained by formula $\chi ( \widehat { \xi } ) i e x ( - \widehat { \xi } ) = I d _ { \xi }$ .

Let $\chi ( \widehat { \xi } ) = 1 + a _ { 1 } \widehat { \xi } + a _ { 2 } \widehat { \xi } ^ { 2 }$ , then

$$
\begin{array} { r c l } { { \chi ( \widehat \xi ) i e x ( - \widehat \xi ) } } & { { = } } & { { ( 1 + a _ { 1 } \widehat \xi + a _ { 2 } \widehat \xi ^ { 2 } ) ( 1 + c _ { 1 } \widehat \xi + c _ { 2 } \widehat \xi ^ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 1 + ( a _ { 1 } + c _ { 1 } ) \widehat \xi + ( a _ { 1 } c _ { 1 } + c _ { 2 } + a _ { 2 } ) { \widehat \xi ^ { 2 } } + ( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } ) { \widehat \xi ^ { 3 } } + a _ { 2 } c _ { 2 } { \widehat \xi ^ { 4 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 1 + ( a _ { 1 } + c _ { 1 } - ( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } ) | \xi | ^ { 2 } ) \widehat \xi + ( c _ { 2 } + a _ { 2 } + a _ { 1 } c _ { 1 } - a _ { 2 } c _ { 2 } | \xi | ^ { 2 } ) \widehat \xi } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { I d , } } \end{array}
$$

therefore

$$
\left\{ \begin{array} { l l } { a _ { 1 } + c _ { 1 } - \left( a _ { 1 } c _ { 2 } + a _ { 2 } c _ { 1 } \right) | \xi | ^ { 2 } = 0 , } \\ { a _ { 1 } c _ { 1 } + c _ { 2 } + a _ { 2 } - a _ { 2 } c _ { 2 } | \xi | ^ { 2 } = 0 . } \end{array} \right.
$$

Solving the above equations, we have

$$
\begin{array} { l } { { a _ { 1 } = \displaystyle \frac { - c _ { 1 } } { ( 1 - c _ { 2 } | \xi | ^ { 2 } ) ^ { 2 } + c _ { 1 } ^ { 2 } | \xi | ^ { 2 } } = \displaystyle \frac { 1 - \cos | \xi | } { ( \sin | \xi | ) ^ { 2 } + ( 1 - \cos | \xi | ) ^ { 2 } } , \smallskip } } \\ { { a _ { 2 } = \displaystyle \frac { - c _ { 2 } + c _ { 2 } | \xi | ^ { 2 } + c _ { 1 } ^ { 2 } } { ( 1 - c _ { 2 } | \xi | ^ { 2 } ) ^ { 2 } + c _ { 1 } ^ { 2 } | \xi | ^ { 2 } } = \displaystyle \frac { \displaystyle \frac { ( \cos | \xi | - 1 ) ^ { 2 } } { | \xi | ^ { 2 } } + \displaystyle \frac { \sin | \xi | - | \xi | } { | \xi | } + ( \sin | \xi | - | \xi | ) | \xi | } { ( \sin | \xi | ) ^ { 2 } + ( 1 - \cos | \xi | ) ^ { 2 } } . } } \end{array}
$$

# Bibliography

[AKW93] M. Austin, P. S. Krishnaprasad, and L.-S. Wang: Almost Poisson integration of rigid body systems. J. of Comp. Phys., 107:105–117, (1993).   
[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Addison-Wesley, Reading, MA, Second edition, (1978).   
[AN90] A. I. Arnold and S.P. Novikov: Dynomical System IV. Springer Verlag, Berlin Heidelberg, (1990).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[CFSZ08] E. Celledoni, F. Fasso, N. S \` afstr ¨ om, and A. Zanna: The exact computation of the ¨ free rigid body motion and its use in splitting methods. SIAM J. Sci. Comput., 30(4):2084– 2112, (2008).   
[CG93] P. E. Crouch and R. Grossman: Numerical integration of ordinary differential equations on manifolds. J. Nonlinear. Sci., 3:1–33, (1993).   
[CS90] P. J. Channell and C. Scovel: Symplectic integration of Hamiltonian systems. Nonlinearity, 3:231–259, (1990).   
[CS91] P. J. Channel and J. S. Scovel: Integrators for Lie–Poisson dynamical systems. Physica D, 50:80–88, (1991).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen86] K. Feng: Symplectic geometry and numerical methods in fluid dynamics. In F. G. Zhuang and Y. L. Zhu, editors, Tenth International Conference on Numerical Methods in Fluid Dynamics, Lecture Notes in Physics, pages 1–7. Springer, Berlin, (1986).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FWQ90] K. Feng, H.M. Wu, and M.Z. Qin: Symplectic difference schemes for linear Hamiltonian canonical systems. J. Comput. Math., 8(4):371–380, (1990).   
[FWQW89] K. Feng, H. M. Wu, M.Z. Qin, and D.L. Wang: Construction of canonical difference schemes for Hamiltonian formalism via generating functions. J. Comput. Math., 7:71–96, (1989).   
[Ge91] Z. Ge: Equivariant symplectic difference schemes and generating functions. Physica D, 49:376–386, (1991).   
[GM88] Z. Ge and J. E. Marsden: Lie–Poisson–Hamilton–Jacobi theory and Lie–Poisson integrators. Physics Letters A, pages 134–139, (1988).   
[HV06] E. Hairer and G. Vilmart: Preprocessed discrete Moser–Veselov algorithm for the full dynamics of the rigid body. J. Phys. A, 39:13225–13235, (2006).   
[Kar04] B. Karasozen: Poisson integrator. ¨ Math. Comput. Modelling, 40:1225–1244, (2004).   
[Lie88] S. Lie: Zur theorie der transformationsgruppen. Christiania, Gesammelte Abh., Christ. Forh. Aar., 13, (1988).   
[LQ95a] S. T. Li and M. Qin: Lie–Poisson integration for rigid body dynamics. Computers Math. Applic., 30:105–118, (1995).   
[LQ95b] S. T. Li and M. Qin: A note for Lie–Poisson– Hamilton–Jacobi equation and Lie– Poisson integrator. Computers Math. Applic., 30:67–74, (1995).   
[McL93] R.I. McLachlan: Explicit Lie–Poisson integration and the Euler equations. Physical Review Letters, 71:3043–3046, (1993).   
[MR99] J. E. Marsden and T. S. Ratiu: Introduction to Mechanics and Symmetry. Number 17 in Texts in Applied Mathematics. Springer-Verlag, Berlin, Second edition, (1999).   
[MRW90] J.E. Marsden, T. Radiu, and A. Weistein: Reduction and hamiltonian structure on dual of semidirect product Lie algebra. Contemporary Mathematics, 28:55–100, (1990).   
[MS95] R. I. McLachlan and C. Scovel: Equivariant constrained symplectic integration. J. Nonlinear. Sci., 5:233–256, (1995).   
[MS96] R. I. McLachlan and C. Scovel: A Survey of Open Problems in Symplectic Integration. In J. E. Mardsen, G. W. Patrick, and W. F. Shadwick, editors, Integration Algorithms and Classical Mechanics, pages 151–180. American Mathematical Society, New York, (1996).   
[MV91] J. Moser and A. P. Veselov: Discrete versions of some classical integrable systems and factorization of matrix polynomials. Communications in Mathematical Physics, 139:217– 243, (1991).   
[MW83] J.E. Marsden and A. Weinstein: Coadjoint orbits, vortices and Clebsch variables for incompressible fluids. Phys D, 7: (1983).   
[MZ05] R.I. McLachlan and A. Zanna: The discrete Moser–Veselov algorithm for the free rigid body. Foundations of Computational Mathematics, 5(1):87–123, (2005).   
[Olv93] P. J. Olver: Applications of Lie Groups to Differential Equations. GTM 107. Springer-Verlag, Berlin, Second edition, (1993).   
[Qin89] M. Z. Qin: Cononical difference scheme for the Hamiltonian equation. Mathematical Methodsand in the Applied Sciences, 11:543–557, (1989).   
[TF85] H. Tal-Fzer: Spectral method in time for hyperbolic equations. SIAM J. Numer. Anal., 23(1):11–26, (1985).   
[Ves88] A.P. Veselov: Integrable discrete-time systems and difference operators. Funkts. Anal. Prilozhen, 22:1–33, (1988).   
[Ves91] A.P. Veselov: Integrable maps. Russian Math. Surveys,, 46:1–51, (1991).   
[Wan91] D. L. Wang: Symplectic difference schemes for Hamiltonian systems on Poisson manifolds. J. Comput. Math., 9(2):115–124, (1991).   
[ZQ94] W. Zhu and M. Qin: Poisson schemes for Hamiltonian systems on Poisson manifolds. Computers Math. Applic., 27:7–16, (1994).   
[ZS07a] R.van Zon and J. Schofield: Numerical implementation of the exact dynamics of free rigid bodies. J. of Comp. Phys., 221(1):145–164, (2007).   
[ZS07b] R.van Zon and J. Schofield: Symplectic algorithms for simulations of rigid body systems using the exact solution of free motion. Physical Review E, 50:5607, (2007).

# Chapter 13. KAM Theorem of Symplectic Algorithms

Numerical results have shown the overwhelming superiority of symplectic algorithms over the conventional non-symplectic systems, especially in simulating the global and structural dynamic behavior of the Hamiltonian systems. In the class of Hamiltonian systems, the most important and better-understood systems are completely integrable ones. Completely integrable systems exhibit regular dynamic behavior which corresponds to periodic and quasi-periodic motions in the phase spaces. In this chapter, we study problems as to whether and to what extent symplectic algorithms can simulate qualitatively and approximate quantitatively the periodic and quasi-periodic phase curves of integrable Hamiltonian systems.

# 13.1 Brief Introduction to Stability of Geometric Numerical Algorithms

Among the various kinds of equations of mathematical physics, only a few can be integrated exactly by quadrature and the rest are unsolvable. However, even an approximate solution is also valuable in many scientific and engineering problems. In a wide range of applications, the most powerful and perhaps the only practically feasible approximation is the numerical method — this is the case, especially in the computer era. A question arises accordingly: Whether a numerical method can reflect the real information of exact solutions of original problems properly or simulate accurately?

To a problem described by time evolutionary equations, the solutions can often be represented by a flow (or semi-flow), which is locally defined on a phase space. Curves on the phase space which are invariant under the action of the flow (or semi-flow) are called invariant curves (or positively invariant curves) of the flow (or semi-flow). There is a natural correspondence between the solutions of the equations and the invariant curves (or positively invariant curves) of the flow (or semi-flow). The invariant curves, or positively invariant curves, are called solution curves of the equations. The qualitative analysis concerns with problems about understanding topological structures of the solution curves and their limit sets, which are often sub-manifolds of the phase space. The aim of the numerical method, in principle, not only pursues an optimal quantitative approximation to the real solution of the considered problem locally but also preserves as well as possible the topological and even geometrical properties of the solution curves and their limit sets globally. The latter constitutes the main content of qualitative analysis of the numerical method.

Qualitative analysis becomes important in the study of numerical methods because instability phenomena take place very often even in the numerical simulations of very stable systems. Numerical treatments of stiff problems show that explicit methods have a severe time-step restriction, which lead to Dahlquist’s pioneering work about A-stability[Dah63] . Various notions of stability for numerical methods have been established since then, classifying different types of stable methods for different problems. The celebrated linear stability theory (A-stability, $\mathbf { A } ( \alpha )$ -stability, and L-stability)[Wid76,Ehl69] is based on the scalar linear equation1

$$
\dot { y } = \lambda y
$$

and turns out to be powerful for the numerical study of all linear-dissipation-dominated problems. G-stability, which was also developed by Dahlquist[Dah75] , is characterized by retaining the contractivity property of any two solutions of nonlinear “contractive” systems

$$
\dot { y } = f ( y ) .
$$

Here, the “contractivity” of the system (1.2) is defined by the condition

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

which implies that ${ \frac { \mathrm { d } } { \mathrm { d } t } } \| u ( t ) - v ( t ) \| \leq 0$ for any two solutions $u ( t )$ and $v ( t )$ of (1.2). It is remarkable that for linear multistep one-leg methods, G-stability is equivalent to A-stability[Dah78] . Butcher extended Dahlquist’s idea and developed B-stability theory for Runge–Kutta methods[But75] . An elegant algebraic criterion of B-stability for Runge–Kutta methods was given by Burrage and Butcher, who further suggested the notion of algebraic stability of Runge–Kutta methods by only using the algebraic conditions of the criterion[BB79] . The algebraically stable Runge–Kutta methods can inherit very important dynamic properties of dissipative systems[HS94] . In many cases, algebraic stability is equivalent to B-stability[HS81] . Many notions and results about stability were also generalized to the general linear methods[HLW02,HNW93] . In almost the whole latter half of the last century, one of the central tasks of numerical analysis was the construction and analysis of numerical methods, satisfying these various stability conditions.

Stable methods have no stringent step-size restriction in their own applicable ranges. They can preserve the dynamic stability properties (fixed points, periodic curves, and attractors) of most of dissipative systems[SH96] . Even explicit methods can also properly reflect the key dynamics of dissipative systems if sufficiently small step sizes are used[Bey87,SH96] . It was also proved that Runge–Kutta methods (including Euler methods), with small step sizes, can preserve the topological structures of dynamic trajectories of many structure-stable systems[Li99,Gar96] .

The application of a numerical method to a generic system definitely changes the structure of the system. On the other hand, conventional methods do not change the topological structures of most dynamic trajectories of typical stable systems (e.g., dissipative systems having motion stability and Morse–Smale systems and Axiom A systems having structure-stability)[SH96,Li99] . However, this remarkable advantage of the conventional methods does not carry over to conservative systems. Most of the stable methods introduce artificial dissipation into conservative systems. They produce illusive attractors and therefore destroy the qualitative character of the conservative systems even if sufficiently small step sizes of the numerical method are used. The approximate solutions of conservative systems ask for new numerical methods which require more stringent stability.

Geometric numerical integration theory for conservative systems has been developed rapidly in recent twenty years. The monographs[SSC94,HLW02,FQ03,LR05] summarize the main developments and important results of this theory. Qualitative behavior of geometric integrators has been investigated by many authors[Sha99,Sha00b,HL97,Sto98a,HLW02] . For symplectic integrators applied to Hamiltonian systems, some stability results, either in the spirits of the KAM theory or based on the backward analysis, have been well established[Sha99,Sha00b,HL97,CFM06,DF07] . The typical stable dynamics of Hamiltonian systems, e.g., quasi-periodic motions and their limit sets — minimal invariant tori, can be topologically preserved and quantitatively approximated by symplectic discretizations. In this chapter, we give a review about these results. For more details, readers refer to the relevant references[Sha99,Sha00b,HLW02,CFM06,DF07] .

# 13.2 Mapping Version of the KAM Theorem

In this section, we introduce the mapping version of the celebrated KAM theorem. The main results of the theorem stem from answering a question about the stability of motions of planets in the solar system. This question attracted many great scientists in history and the culminated breakthrough was given by Kolmogorov (1954), Arnold (1963) and Moser (1962). The monograph[HLW02] gives a nice introduction to the KAM theorem based on the Hamiltonian perturbation theory. We present some results about differentiable Cantorian foliation structures of invariant tori in phase space of an integrable symplectic mapping under perturbations. We give relevant estimates explicitly in terms of the diophantine constant and nondegeneracy parameters of the frequency map of the integrable system. As a direct application of these estimates, we state a generalization of Moser’s small twist theorem to higher dimensions, which can be applied to prove a numerical version of the KAM theorem for symplectic algorithms.

# 13.2.1 Formulation of the Theorem

Consider an exact symplectic mapping $S : ( p , q ) \to ( { \widehat { p } } , { \widehat { q } } )$ to be defined in the phase space I  Tn

$$
\widehat { p } = p - \partial _ { 2 } H ( \widehat { p } , q ) , \quad \widehat { q } = q + \partial _ { 1 } H ( \widehat { p } , q ) ,
$$

where $H : I \times \mathbf { T } ^ { n } \to \mathbf { R }$ is the generating function, $I$ is an open and usually bounded set of $\mathbf { R } ^ { n }$ and $\mathbf { T } ^ { n }$ is the standard $n$ -torus. In (2.1), $\partial _ { 1 }$ and $\partial _ { 2 }$ denote the gradient operators with respect to the first $n$ and the last $n$ variables respectively. When $H ( p , q ) = H _ { 0 } ( p )$ does not depend on $q$ , then (2.1) represents an integrable mapping $S = S _ { 0 } : ( p , q ) \to ( \widehat { p } , \widehat { q } ) = ( p , q + \omega ( p ) )$ with the frequency map

$$
\omega ( p ) = \partial H _ { 0 } ( p ) , \quad p \in I ,
$$

where $\partial$ denotes the gradient operator with respect to $p$ . Under the mapping $S _ { 0 }$ , the phase space $I \times \mathbf { T } ^ { n }$ is completely foliated into invariant $n$ -tori $\{ p \} \times \mathbf { T } ^ { n }$ , $p \in I$ . On each torus, the iterations of $S _ { 0 }$ are linear with frequencies $\omega = \omega ( p )$ . This is a typical integrable case. When a perturbation $h ( p , q )$ is added to $H _ { 0 }$ , i.e., $H ( p , q ) = H _ { 0 } ( p ) + h ( p , q )$ , (2.1) does not define an integrable mapping generally. However, KAM theorem shows that the perturbed mapping $S$ still exhibits to a large extent the integrable behavior in the phase space if the frequency map $\omega$ is nondegenerate in some sense $( \mathrm { s e e } ^ { [ \mathrm { A r n } 6 3 , \mathrm { A A } 8 9 , \mathrm { A r n } 8 9 , \mathrm { K o l } 5 4 \mathrm { \bar { b } } , \mathrm { M o s } 6 2 ] }$ for Kolmogorov’s nondegeneracy and $| [ \mathrm { C S 9 4 } , \mathrm { R i i s 9 0 } ]$ for weak nondegeneracy) and the perturbation $h$ is sufficiently small in some function space. In this chapter, we consider the following nondegeneracy condition for $\omega : I  \Omega$ :

$$
\theta \left| p _ { 1 } - p _ { 2 } \right| \leq \left| \omega ( p _ { 1 } ) - \omega ( p _ { 2 } ) \right| \leq \theta \left| p _ { 1 } - p _ { 2 } \right|
$$

for some $0 < \theta \leq \theta$ . Here $I$ and $\Omega$ are the domains of action variables and the corresponding frequency values respectively. We always assume that $I$ and $\Omega$ are open in $\mathbf { R } ^ { n }$ and $\omega$ is analytic and can be analytically extended to some complex domain, say $I + r$ , of the real domain $I$ , where $r$ is the extension radius. We assume (2.3) is satisfied for $p _ { 1 } , p _ { 2 } \in I + r$ with $| p _ { 1 } - p _ { 2 } | \leq r$ . Note that this nondegeneracy condition implies that the frequency map $\omega$ is invertible in any ball of radius $r$ and centered in $I$ , which is stronger than the standard Kolmogorov’s nondegeneracy assumption of the following (this was already noticed by Poschel in ¨ [Pos82 ¨ ] ,

$$
\theta | \mathrm { d } p | \leq | \mathrm { d } \omega ( p ) | \leq \theta | \mathrm { d } p | \quad \mathrm { f o r } \quad p \in I + r .
$$

An invariant torus of the integrable system is naturally specified by its frequency vector. Those tori are rationally dependent and even Liouville frequency vectors are generally destroyed by perturbations (Poincare and Mather \` [Mat88] ). The invariant tori of KAM type are specified by the so-called diophantine frequency vectors $\omega = ( \omega _ { 1 } , \cdots , \omega _ { n } )$ ,

$$
\begin{array} { r l } { \left| e ^ { i \langle k , \omega \rangle } - 1 \right| \geq \frac { \gamma } { | k | ^ { \tau } } } & { { } \mathrm { f o r } \ 0 \neq k = ( k _ { 1 } , \cdots , k _ { n } ) \in { \bf Z } ^ { n } } \end{array}
$$

with some constants $\gamma > 0 , \tau > 0$ , where $\langle k , \omega \rangle = \sum _ { j = 1 } ^ { n } k _ { j } \omega _ { j }$ and $| k | = \sum _ { j = 1 } ^ { n } | k _ { j } |$ for integers $k \in \mathbf { Z } ^ { n }$ .

We introduce some notations. For an open or closed set $I \subset \mathbf { R } ^ { n }$ and for $a \geq 0$ , denote by $C ^ { a } ( I \times \mathbf { T } ^ { n } )$ , the class of isotropic differentiable functions of order $a$ defined on ${ \cal I } \times { \bf T } ^ { n }$ in the sense of Whitney. The norm of a function $u \in C ^ { a } ( I \times \mathbf { T } ^ { n } )$ is denoted by $\| u \| _ { a , I \times \mathbf { T } ^ { n } }$ . Since we also get the anisotropic differentiability of the foliations of Tinvariant tori, we need the class $C ^ { \nu _ { 1 } , \nu _ { 2 } } ( I \times { \bf T } ^ { n } )$ , of anisotropic differentiable functions of order $( \nu _ { 1 } , \nu _ { 2 } )$ , with the norm denoted by $\| u \| _ { \nu _ { 1 } , \nu _ { 2 } ; I \times \mathbf { T } ^ { n } }$ for a function $u$ in the class. TThese two classes, endowed with the corresponding norms, are both Banach spaces. We also use another norm $\| \cdot \| _ { \nu _ { 1 } , \nu _ { 2 } ; I \times \mathbf { T } ^ { n } , \rho }$ for $\rho > 0$ defined by

$$
\begin{array} { r } { \| u \| _ { \nu _ { 1 } , \nu _ { 2 } ; I \times { \mathbf T } ^ { n } , \rho } = \| u \circ \sigma _ { \rho } \| _ { \nu _ { 1 } , \nu _ { 2 } ; \sigma _ { \rho } ^ { - 1 } ( I \times { \mathbf T } ^ { n } ) } } \end{array}
$$

for $u \in C ^ { \nu _ { 1 } , \nu _ { 2 } } ( I \times \mathbf { T } ^ { n } )$ , where $\sigma _ { \rho }$ denotes the partial stretching $( x , y ) \to ( \rho x , y )$ for $( x , y ) \in I \times \mathbf { T } ^ { n }$ . Note that the following relation between these two norms is valid for $0 < \rho \leq 1$ :

$$
\begin{array} { r } { \| u \| _ { \nu _ { 1 } , \nu _ { 2 } ; \rho } \leq \| u \| _ { \nu _ { 1 } , \nu _ { 2 } } \leq \rho ^ { - \nu _ { 1 } } \| u \| _ { \nu _ { 1 } , \nu _ { 2 } ; \rho } , } \end{array}
$$

where we dropped the domains to simplify the notations.

Take $\Omega = \omega ( I )$ and denote by $\Omega _ { \gamma }$ the set of those frequencies, in $\Omega$ , which satisfy the diophantine condition (2.5) for given $\gamma > 0$ and whose distance to the boundary of $\Omega$ is at least equal to $2 \gamma$ . The set $\Omega _ { \gamma }$ is a Cantor set2 and the difference $\Omega \setminus \bigcup _ { \gamma > 0 } \Omega _ { \gamma }$ is a zero set if $\tau > n + 1$ . Therefore $\Omega _ { \gamma }$ is large for small $\gamma$ .

The main results of this section are stated as follows:

Theorem 2.1. Given positive integer n and real number $\tau > n { + } 1$ , consider mapping $S$ defined in phase space ${ \cal I } \times { \bf T } ^ { n }$ by (2.1) with $H ( \widehat { p } , q ) = H _ { 0 } ( \widehat { p } ) + h ( \widehat { p } , q )$ , where $H _ { 0 }$ is analytic in $I + r$ with $r > 0$ and $h ( \widehat { p } , q )$   belongs to the Whitney’s class $C ^ { \alpha \lambda + \lambda + \tau } ( I \times$ $\mathbf { T } ^ { n }$ ) for some $\lambda > \tau + 1$ and $\alpha > 1$ ,

$$
\alpha \not \in \Lambda = \left\{ \frac { i } { \lambda } + j : i , j \geq 0 \ i n t e g e r \right\} .
$$

Suppose the frequency map $\omega = \partial H _ { 0 } : I  \Omega$ satisfies the nondegeneracy condition (2.3) for $p _ { 1 }$ , $p _ { 2 } \ \in \ I + r$ with $| p _ { 1 } - p _ { 2 } | \le r$ where the constants $\theta$ and $\Theta$ satisfy $0 < \theta \leq \Theta$ , then there exists a positive constant $\delta _ { 0 }$ , depending only on n, $\tau$ , $\lambda$ and $\alpha$ , such that for any $0 < \gamma \leq \operatorname* { m i n } { \bf \Sigma } \biggl ( 1 , \frac { 1 } { 2 } r \theta \biggr ) ,$ , if

$$
\begin{array} { r } { \| h \| _ { \alpha \lambda + \lambda + \tau , I \times \mathbf { T } ^ { n } ; \gamma \Theta ^ { - 1 } } \le \delta _ { 0 } \gamma ^ { 2 } \theta \Theta ^ { - 2 } , } \end{array}
$$

then there exists a Cantor set $I _ { \gamma } \subset I$ , a surjective map $\omega _ { \gamma } : I _ { \gamma }  \Omega _ { \gamma }$ of $C ^ { \alpha + 1 }$ class and a symplectic injection $\Phi : I _ { \gamma } \times \mathbf { T } ^ { n }  \mathbf { R } ^ { n } \times \mathbf { T } ^ { n }$ of $C ^ { \alpha , \alpha \lambda }$ class, in the Whitney’s sense, such that

$1 ^ { \circ }$ $\Phi$ is a conjugation from $S$ to $R$ . That is, the following equation holds:

$$
S \circ \Phi = \Phi \circ R ,
$$

where $R$ is the integrable rotation on ${ \cal I } _ { \gamma } \times { \bf T } ^ { n }$ with frequency map $\omega _ { \gamma }$ , i.e., $R ( P , Q ) =$ $( P , Q + \omega _ { \gamma } ( P ) ) f o r \left( P , Q \right) \in I _ { \gamma } \times { \bf T } ^ { n }$ . Moreover, Equation (2.9) may be differentiated as often as $\Phi$ allows.

$2 ^ { \circ }$ If $\Omega$ is a bounded open set of type $D$ in the Arnold’s sense3, then we have the following measure estimate

$$
m \mathcal { E } _ { \gamma } \geq \Big ( 1 - c _ { 4 } \Big ( \theta \Theta ^ { - 1 } \Big ) ^ { - n } \gamma \Big ) m \mathcal { E } ,
$$

where $\mathscr { E } _ { \gamma } = \Phi ( I _ { \gamma } \times \mathbf { T } ^ { n } )$ is the union of invariant tori $\Phi ( \{ P \} \times \mathbf { T } ^ { n } )$ , $P \in I _ { \gamma }$ , of $S$ and m denotes the invariant Liouville measure on the phase space $\mathcal { E } = I \times \mathbf { T } ^ { n }$ ; $c _ { 4 }$ is a positive constant depending on $n , \tau ,$ , a and the geometric property of the domain $\Omega$ .

$3 ^ { \circ }$ If h is of $C ^ { \beta \lambda + \lambda + \tau }$ class with $\alpha \leq \beta$ not in $\Lambda$ , then we have further that $\omega _ { \gamma } \in C ^ { \beta + 1 } ( I _ { \gamma } )$ and $\Phi \in C ^ { \beta , \beta \lambda } ( I _ { \gamma } \times \mathbf { T } ^ { n } )$ . Moreover,

$$
\left\| \sigma _ { \gamma \Theta ^ { - 1 } } ^ { - 1 } \circ \left( \Phi - I \right) \right\| _ { \substack { \beta , \beta \lambda ; \gamma \Theta ^ { - 1 } } } , \gamma ^ { - 1 } \left\| \omega _ { \gamma } - \omega \right\| _ { \beta + 1 ; \gamma \Theta ^ { - 1 } } \leq c _ { 5 } \gamma ^ { - 2 } \theta \left\| h \right\| _ { \beta \lambda + \lambda + \tau ; \gamma \Theta ^ { - 1 } }
$$

with constant $c _ { 5 }$ depending on $n , \tau , \lambda$ and $\beta$ , here we have dropped the domains in the notation of norms.

$4 ^ { \circ }$ For each $\omega ^ { \ast } \in \Omega _ { \gamma } ,$ , there exists $p ^ { * } \in I$ and $P ^ { \ast } \in I _ { \gamma }$ such that $\omega ( p ^ { * } ) =$ $\omega _ { \gamma } ( P ^ { * } ) = \omega ^ { * }$ and

$$
\begin{array} { r } { | P ^ { * } - p ^ { * } | \leq c _ { 6 } \Big ( \gamma \theta \theta ^ { - 1 } \Big ) ^ { - 1 } \| h \| _ { \alpha \lambda + \lambda + \tau , I \times \mathbf { T } ^ { n } ; \gamma \theta ^ { - 1 } } , } \end{array}
$$

where $c _ { 6 }$ is a positive constant depending on n, $\tau$ , $\lambda$ and $\alpha$

Theorem 2.2. If the frequency map $\omega$ satisfies the nondegeneracy condition (2.4), then the conclusions of Theorem 2.1 are still true with the same estimates (2.10) – (2.12) under the following smallness condition for $h$ ,

$$
\begin{array} { r } { \| h \| _ { \alpha \lambda + \lambda + \tau , I \times \mathbf { T } ^ { n } ; \gamma \Theta ^ { - 1 } } \le \delta _ { 0 } \gamma ^ { 2 } \theta ^ { 2 } \Theta ^ { - 3 } , } \end{array}
$$

where $\delta _ { 0 } > 0$ is depending only on $n$ , τ , $\lambda$ and $\alpha$ and is sufficiently small.

Remark 2.3. The above two theorems are stated for the case when $h$ is finitely many times differentiable. If $h$ is infinitely many times differentiable or analytic, we have the following conclusions, which are easily derived by similar remarks to those of[Pos82 ¨ ] .

$1 ^ { \circ }$ If $h \in C ^ { \infty } ( I \times \mathbf { T } ^ { n } )$ , then $\omega _ { \gamma } \in C ^ { \infty } ( I _ { \gamma } )$ and $\Phi \in C ^ { \infty } ( I _ { \gamma } \times \mathbf { T } ^ { n } )$ and the estimates (2.8) hold for any $\beta \geq \alpha$ .

$2 ^ { \circ }$ If $h \in C ^ { \omega } ( I \times \mathbf { T } ^ { n } )$ , then we have further $\Phi \in C ^ { \infty , \omega } ( I _ { \gamma } , \mathbf { T } ^ { n } )$ under an additional smallness condition for $\delta _ { 0 }$ which also depends on the radius of analyticity of $h$ with respect to angle variables. Here $C ^ { \omega }$ denotes the class of real analytic functions.

# 13.2.2 Outline of the Proof of the Theorems

In this section, we give an outline of the proof of Theorem 2.1. For detailed arguments refer to [Sha00a] .

a. We transform the mapping $S$ , by a partial coordinates stretching $\sigma _ { \rho } : ( x , y ) \to$ $( p , q ) = ( \rho x , y )$ , to $T = \sigma _ { \rho } ^ { - 1 } \circ S \circ \sigma _ { \rho } : ( x , y )  ( { \widehat { x } } , { \widehat { y } } ) .$ The mapping $T$ is determined by

$$
\widehat { \boldsymbol { x } } = \boldsymbol { x } - \partial _ { 2 } \boldsymbol { F } ( \widehat { \boldsymbol { x } } , \boldsymbol { y } ) , \quad \widehat { \boldsymbol { y } } = \boldsymbol { y } + \partial _ { 1 } \boldsymbol { F } ( \widehat { \boldsymbol { x } } , \boldsymbol { y } ) ,
$$

where

$$
F ( x , y ) = F _ { 0 } ( x ) + f ( x , y )
$$

is well defined on $I _ { \rho } \times \mathbf { T } ^ { n }$ with

$$
F _ { 0 } ( x ) = \rho ^ { - 1 } H _ { 0 } ( \rho x ) , \quad f ( x , y ) = \rho ^ { - 1 } h ( \rho x , y )
$$

and

$$
I _ { \rho } = \rho ^ { - 1 } I = \{ x \in \mathbf { R } ^ { n } | \rho x \in I \} .
$$

For the time being, $\rho$ is regarded as a free parameter. $F _ { 0 } ( x )$ is real analytic in $I _ { \rho } + r _ { \rho }$ and $f$ belongs to the class $C ^ { a } ( I _ { \rho } \times \mathbf { T } ^ { n } )$ where $r _ { \rho } = \rho ^ { - 1 } r$ , $a = \alpha \lambda + \lambda + \tau$ . So the new mapping $T$ satisfies the assumptions of Theorem 2.1 in which only $I$ , $r , H , H _ { 0 }$ , and $h$ are replaced by $I _ { \rho } , r _ { \rho } , F , F _ { 0 }$ , and $f$ respectively. Accordingly, the frequency map of the integrable mapping associated to the generating function $F _ { 0 }$ turns into

$$
\widetilde { \omega } ( x ) = \partial { \cal F } _ { 0 } ( x ) , \quad x \in { \cal I } _ { \rho } ,
$$

and the nondegeneracy condition for the mapping turns out to be

$$
\rho \theta \left| x _ { 1 } - x _ { 2 } \right| \leq \left| \widetilde { \omega } ( x _ { 1 } ) - \widetilde { \omega } ( x _ { 2 } ) \right| \leq \rho \theta \left| x _ { 1 } - x _ { 2 } \right|
$$

for $x _ { 1 }$ , $x _ { 2 } \in I _ { \rho } + r _ { \rho }$ with $| x _ { 1 } - x _ { 2 } | \leq r _ { \rho }$ . In addition, from (2.16), we have

$$
\| f \| _ { a , I _ { \rho } \times { \bf T } ^ { n } } = \rho ^ { - 1 } \| h \| _ { a , I \times { \bf T } ^ { n } ; \rho } .
$$

From now on, we fix $\rho = \gamma \Theta ^ { - 1 }$ . Then the assumption $0 < \gamma \leq { \frac { 1 } { 2 } } r \theta$ in Theorem 2.1 implies that $0 < \rho \leq { \frac { 1 } { 2 } } r$ . Hence, $r _ { \rho } \geq 2$ . Let $I _ { \rho } ^ { * }$ be the set of points in $I _ { \rho }$ with the distance to its boundary at least one and let

$$
I _ { \rho ; \gamma } = \widetilde { \omega } ^ { - 1 } ( \Omega _ { \gamma } ) \cap I _ { \rho } .
$$

Then, from (2.18) and the definition of $\Omega _ { \gamma }$ it follows that

$$
( I _ { \rho ; \gamma } + 1 ) \cap { \bf R } ^ { n } \subset I _ { \rho } ^ { * } \subset ( I _ { \rho } ^ { * } + 1 ) \cap { \bf R } ^ { n } \subset I _ { \rho } ,
$$

and

$$
\gamma \mu \left| x _ { 1 } - x _ { 2 } \right| \leq \left| \widetilde { \omega } ( x _ { 1 } ) - \widetilde { \omega } ( x _ { 2 } ) \right| \leq \gamma \left| x _ { 1 } - x _ { 2 } \right| , \quad \mu = \theta \Theta ^ { - 1 }
$$

for $x _ { 1 }$ , $x _ { 2 } \in I _ { \rho } + 2$ with $| x _ { 1 } - x _ { 2 } | \le 2$

b. We approximate $f$ by real analytic functions. Let

$$
s _ { j } = s _ { 0 } 4 ^ { - j } , \quad r _ { j } = s _ { j } ^ { \lambda } , \quad j = 0 , 1 , 2 , \cdot \cdot \cdot
$$

with fixed $\lambda > \tau + 1$ and $s _ { 0 } > 0$ . Let

$$
\mathcal { U } _ { j } = I _ { \rho } \times \mathbf { T } ^ { n } + ( 4 s _ { j } , 4 s _ { j } )
$$

be the complex extended domain of $I _ { \rho } \times \mathbf { T } ^ { n }$ with extended widths $4 s _ { j }$ of $I _ { \rho }$ and $\mathbf { T } ^ { n }$ respectively $[ \mathrm { P } \mathrm { i } \mathrm { s } 8 2 ]$ . By an approximation lemma [Pos82 ¨ ] , there exists real analytic functions $f _ { j }$ defined on $\mathcal { U } _ { \mathrm { 0 } }$ with $f _ { 0 } = 0$ such that, in case $f \in C ^ { b } ( I \times \mathbf { T } ^ { n } )$ with $b \geq a$ ,

$$
\begin{array} { r l } & { \lvert f _ { j } - f _ { j - 1 } \rvert _ { \mathcal { U } _ { j } } \le s _ { j } ^ { b } c _ { b } \left. f \right. _ { b ; I _ { \rho } \times \mathbf { T } ^ { n } } \quad j = 1 , 2 , \cdots , } \\ & { \left. f - f _ { j } \right. _ { b ^ { \prime } , I _ { \rho } ^ { * } \times \mathbf { T } ^ { n } } \longrightarrow 0 \quad ( j \longrightarrow \infty ) \quad \mathrm { f o r ~ } 0 < b ^ { \prime } < b , } \end{array}
$$

where $c _ { b }$ is a positive constant only depending on $b$ , $n$ and $s _ { 0 }$ but not depending on the domain $I _ { \rho }$ and hence not depending on the parameter $\rho$ . Moreover, we may require $f _ { j }$ to be $2 \pi$ -periodic in the last $n$ variables. In (2.23), $| \cdot | u _ { j }$ denotes the maximum norm of analytic functions on the complex domain $\mathcal { U } _ { j }$ .

c. We give the KAM iteration process which essentially follows Poschel ¨ $[ \mathrm { P } \mathrm { i } \mathrm { s } 8 2 ]$ in the Hamiltonian system case. For each $f _ { j }$ , we define a mapping $T _ { j } : ( x , y )  ( \widehat { x } , \widehat { y } )$ by

$$
\widehat { x } = x - \partial _ { 2 } F _ { j } ( \widehat { x } , y ) , \quad \widehat { y } = y + \partial _ { 1 } F _ { j } ( \widehat { x } , y )
$$

with $F _ { j } ( { \widehat { x } } , y ) = F _ { 0 } ( { \widehat { x } } ) + f _ { j } ( { \widehat { x } } , y )$ . For each $j$ , the function $F _ { j } ( \widehat { x } , y )$ is well-defined and real analytic on $\mathcal { U } _ { j }$ if $4 s _ { j } \leq r _ { \rho } = \rho ^ { - 1 } r$ — this inequality is satisfied for $j = 0 , 1 , \cdots$ if we choose $0 < s _ { 0 } \le 4 ^ { - 1 }$ noting that $0 < \gamma < \frac { 1 } { 2 } r \Theta \Big )$ . We can show that each $T _ { j }$ for $j \geq 0$ is a well-defined analytic mapping on a domain of complex extension of the phase space $I _ { \rho } \times \mathbf { T } ^ { n }$ , which is appropriate for the KAM iterations if $h$ is bounded by (2.8) with a sufficiently small $\delta _ { 0 } > 0$ . It follows from (2.23) that $T _ { j }$ converges to $T$ in $C ^ { b - 1 - \kappa }$ -norm for any $\kappa > 0$ on some subdomain $I _ { \rho } ^ { * } \times \mathbf { T } ^ { n }$ of the phase space $I _ { \rho } \times \mathbf { T } ^ { n }$ , where $T$ is well-defined. The central problem is to find transformations $\Phi _ { j }$ and integrable rotations $R _ { j }$ , defined on a sequence of nested complex domains that intersect a nonempty Cantor set, say $\widetilde { I } _ { \rho ; \gamma } \times \mathbf { T } ^ { n }$ , such that the following holds as $j \to \infty$ on $\widetilde { I } _ { \rho ; \gamma } \times \mathbf { T } ^ { n }$ in some Whitney’s classes,

$$
C _ { j } = R _ { j } ^ { - 1 } \circ \Phi _ { j } ^ { - 1 } \circ T _ { j } \circ \Phi _ { j } \longrightarrow \mathrm { i d e n t i t y } , \Phi _ { j } \longrightarrow \widetilde \Phi , R _ { j } \longrightarrow \widetilde R ,
$$

where $\widetilde { \Phi }$ and $\widetilde { R }$ are well-defined on $\widetilde { I } _ { \rho ; \gamma } \times \mathbf { T } ^ { n }$ . In this case, we have

$$
T \circ \widetilde { \Phi } = \widetilde { \Phi } \circ \widetilde { R } \quad \mathrm { o n } \quad \widetilde { I } _ { \rho ; \gamma } \times \mathbf { T } ^ { n } .
$$

Transforming the mapping $T$ back to $S$ by the partial coordinates stretching $\sigma _ { \rho }$ , and meanwhile transforming $\widetilde { \Phi }$ and $\widetilde { R }$ to $\Phi$ and $R$ respectively, we have

$$
S \circ \Phi = \Phi \circ R \quad \mathrm { o n ~ } I _ { \gamma } \times \mathbf { T } ^ { n } ,
$$

where

$$
I _ { \gamma } = \rho \widetilde { I } _ { \rho ; \gamma } = \{ p \in { \bf R } ^ { n } \ | \ \rho ^ { - 1 } p \in \widetilde { I } _ { \rho ; \gamma } \}
$$

is a Cantor set of $I$ . In fact, due to the nondegeneracy of the frequency map $\omega$ in the sense of (2.3), we may keep the frequencies prescribed by (2.5) fixed in the above approximation process. As a result, we have $\omega _ { \gamma } ( I _ { \gamma } ) = \Omega _ { \gamma }$ , where $\omega _ { \gamma }$ is the frequency map of the integrable rotation $R$ on $I _ { \gamma } \times \mathbf { T } ^ { n }$ . This is just the conclusion (1) of Theorem 2.1.

The construction of $\Phi _ { j }$ and $R _ { j }$ uses the KAM iteration, which is described as follows.

Assume

$$
| f _ { j } - f _ { j - 1 } | \sim \varepsilon _ { j } , \quad j = 1 , 2 , \cdots ,
$$

where $\varepsilon _ { j }$ is a decreasing sequence of positive numbers . Suppose we have already found a transformation $\Phi _ { j }$ and a rotation $R _ { j }$ with frequency map $\boldsymbol { \omega } ^ { ( j ) }$ such that

$$
C _ { j } = R _ { j } ^ { - 1 } \circ \Phi _ { j } ^ { - 1 } \circ T _ { j } \circ \Phi _ { j }
$$

satisfies

$$
| C _ { j } - I | \sim \varepsilon _ { j + 1 } .
$$

Then, we construct a transformation $\Psi _ { j }$ and a new rotation $R _ { j + 1 }$ with frequency map $\boldsymbol { \omega } ^ { ( j + 1 ) }$ such that

$$
\Phi _ { j + 1 } = \Phi _ { j } \circ \Psi _ { j }
$$

and (2.29) is also true for the next index $j + 1$ with $C _ { j + 1 }$ defined by (2.28) in which $j$ is replaced by $j + 1$ . As was remarked by Poschel¨ $\mathrm { i n } ^ { [ \mathrm { P \ddot { o s } 8 2 } ] }$ , “for this procedure to be successful it is essential to have precise control over the various domains of definition”.

We define transformation $\Psi _ { j } : ( \xi , \eta )  ( x , y )$ implicitly with the help of a generating function $\psi _ { j }$ by

$$
x = \xi + \partial _ { 2 } \psi _ { j } ( \xi , y ) , \quad y = \eta - \partial _ { 1 } \psi _ { j } ( \xi , y ) .
$$

To define $\psi _ { j }$ , we consider mapping

$$
B _ { j } = R _ { j } ^ { - 1 } \circ \Phi _ { j } ^ { - 1 } \circ T _ { j + 1 } \circ \Phi _ { j } .
$$

$B _ { j }$ is near identity and is assumed to be given implicitly from its generating function $b _ { j }$ by

$$
\widehat { x } = x - \partial _ { 2 } b _ { j } ( \widehat { x } , y ) , \quad \widehat { y } = y + \partial _ { 1 } b _ { j } ( \widehat { x } , y ) .
$$

The function $\psi _ { j }$ is then determined from $b _ { j }$ by the following homological equation

$$
\psi _ { j } ( x , y + \omega ^ { ( j ) } ( x ) ) - \psi _ { j } ( x , y ) + \widetilde { b } _ { j } ( x , y ) = 0 ,
$$

where $\widetilde { b } _ { j } ( x , y ) = b _ { j } ( x , y ) - [ b _ { j } ] ( x )$ with $[ b _ { j } ]$ being the mean value of $b _ { j }$ with respect to the angle variables over $\mathbf { T } ^ { n }$ . Define

$$
\omega ^ { ( j + 1 ) } ( x ) = \omega ^ { ( j ) } ( x ) + \partial [ b _ { j } ] ( x ) .
$$

Then $R _ { j + 1 } : ( x , y )  ( { \widehat { x } } , { \widehat { y } } )$ is just given by

$$
\widehat x = x , \quad \widehat y = y + \omega ^ { ( j + 1 ) } ( x ) .
$$

With the so defined $\Psi _ { j }$ and $R _ { j + 1 }$ , we easily show that, formally,

$$
\Psi _ { j } ^ { - 1 } \circ R _ { j } \circ B _ { j } \circ \Psi _ { j } = R _ { j + 1 } \circ C _ { j + 1 } .
$$

Formal calculations similar to those $\mathrm { i n } ^ { [ \mathrm { P \ i s 8 2 } ] }$ show that (2.29) is valid if we replace $j$ by $j + 1$ .

We do not solve the Equation (2.34) exactly. Instead, we will solve an approximate equation by truncating the fourier expansion of $\widetilde { b } _ { j }$ with respect to angle variables to some finite order so that “only finitely many resonances remain, and we obtain a real analytic solution $\psi _ { j }$ defined on an open set” $[ \mathrm { P i o s } 8 2 ]$ . This idea was first successfully used by Arnold[Arn63,AA89] .

For an earnest proof, we need more precise arguments by carefully controlling the domains of definition of functions and mappings in the iterative process. Readers can refer to $\mathrm { \Delta [ S h a 0 0 a ] }$ for details.

# 13.2.3 Application to Small Twist Mappings

In this section, we state a theorem of KAM type for small twist mappings. Such a theorem first appeared in Moser’s celebrated paper[Mos62] for 2-dimensional areapreserving mappings. Its generalization to higher dimensions was given in[Sha00a] , as a direct application of the theorems of the last section. The result may be formulated as follows:

Theorem 2.4. Consider one parameter family of mappings $S _ { t } : ( p , q ) \to ( { \widehat { p } } , { \widehat { q } } )$ with $S _ { 0 } = I$ and $S _ { 1 } = S$ , defined in phase space $I \times \mathbf { T } ^ { n }$ by

$$
\left\{ \begin{array} { l l } { \widehat { p } = p - t \partial _ { 2 } H ( \widehat { p } , q ) = p - t \partial _ { 2 } h ( \widehat { p } , q ) , } \\ { \widehat { q } = q + t \partial _ { 1 } H ( \widehat { p } , q ) = q + t \omega ( \widehat { p } ) + t \partial _ { 1 } h ( \widehat { p } , q ) , } \end{array} \right.
$$

where ${ \cal H } ( \widehat { p } , q ) = { \cal H } _ { 0 } ( \widehat { p } ) + h ( \widehat { p } , q )$ and $\omega ( \widehat { p } ) = \partial H _ { 0 } ( \widehat { p } )$ . Under the assumptions of   Theorem 2.1 (Theorem 2.2) for $H$ , if $h$  satisfies the smallness condition of Theorems 2.1 (Theorem 2.2), then the corresponding conclusions of the theorem are still valid for $S _ { t }$ $0 < t \leq 1$ ), only with the following remarks:

$1 ^ { \circ } \quad \Omega _ { \gamma }$ is replaced by

$$
\Omega _ { t , \gamma } = \Big \{ \omega \in \Omega _ { * } : \big | e ^ { i \langle k , t \omega \rangle } - 1 \big | \geq \frac { t \gamma } { | k | ^ { \tau } } f o r k \in \mathbf { Z } ^ { n } \setminus \{ 0 \} \Big \Big \} ,
$$

where $\Omega _ { * }$ denotes the set of points in $\Omega$ with distance to its boundary at least equal to $2 \gamma$ . Accordingly, $I _ { \gamma } , \omega _ { \gamma } , \Phi$ , and $R$ are replaced by $I _ { t , \gamma } , \omega _ { t , \gamma } ,$ , $\Phi _ { t }$ and $R _ { t }$ ,respectively.

$2 ^ { \circ }$ If $\Omega$ is a bounded open set of type $D$ in the Arnold’s sense $\left[ A r n \delta \right]$ , then we have the following Lebesgue measure estimate

$$
m ( \Omega \setminus \Omega _ { t , \gamma } ) \leq D \gamma m \Omega
$$

for $t \in ( 0 , 1 ]$ , with constant $D$ only depending on $n$ , $\tau$ and the geometry of $\Omega$ . So in this case, $\Omega _ { t , \gamma }$ is still a large Cantor set in $\Omega$ when $\gamma$ is small enough.

$3 ^ { \circ }$ If $h \in C ^ { \infty } ( B \times \mathbf { T } ^ { n } )$ , then $\omega _ { \gamma , t } \in C ^ { \infty } ( B _ { \gamma , t } )$ and $\Phi _ { t } \in C ^ { \infty } ( B _ { \gamma , t } \times \mathbf { T } ^ { n } )$ which satisfy the estimates (2.11) for any $\beta \ge \alpha$ .

$4 ^ { \circ }$ If $h$ is analytic with the domain of analyticity containing

$$
S ( \boldsymbol { r } , \rho ) = \left. ( p , q ) \in \mathbf { C } ^ { 2 n } : | p - p ^ { \prime } | < r , | \mathrm { I m } ~ q | < \rho ~ w i t h ~ p ^ { \prime } \in B ~ a n d \mathrm { R e } q \in \mathbf { T } ^ { n } \right.
$$

for some $r > 0$ and $\rho > 0$ (Re $q$ and $\operatorname { I m } q$ denote the real and imaginary parts of $q$ respectively) and if $h$ satisfies

$$
\| h \| _ { r , \rho } = \operatorname* { s u p } _ { ( p , q ) \in S ( r , \rho ) } | h ( p , q ) | \leq \delta _ { 0 } \gamma ^ { 2 } \theta ^ { 2 } \theta ^ { - 3 }
$$

for some sufficiently small $\delta _ { 0 } ~ > ~ 0$ depending on n, τ , r and $\rho _ { ; }$ , then all the conclusions of Theorem 2.1 (Theorem 2.2) are still true with $\omega _ { \gamma , t } \in C ^ { \infty } ( B _ { \gamma , t } )$ , $\Phi _ { t } \ \in$ $C ^ { \infty , \omega } ( B _ { \gamma , t } \times \mathbf { T } ^ { n } )$ and the estimate (2.11) holds for any $\beta \geq 0$ .

We have presented the results about the existence of differentiable foliation structures in the sense of Whitney of invariant tori for nearly integrable symplectic mappings and for mappings with small twists. Such a result was proved first by Lazutkin in $\bar { 1 } 9 7 4 ^ { [ \mathrm { L a z } 7 4 ] }$ for planar twist maps and was generalized to higher dimensions by Svanidze in $1 9 8 0 ^ { [ \mathrm { S v a 8 1 ] } }$ . For the case of Hamiltonian flows of arbitrary dimensions, the generalizations were given by J. Poschel in¨ $1 9 8 2 ^ { [ \mathrm { P \ddot { 0 } s 8 2 } ] }$ , Chierchia and Gallavotti in $1 \bar { 9 } 8 2 ^ { [ \mathrm { C G 8 2 } ] }$ . The perturbation and measure estimates in terms of $\gamma$ were studied by Russmann in 1981 ¨ [Rus81 ¨ ] , Svadnidze in $1 9 8 1 ^ { [ \mathrm { S v a 8 1 ] } }$ , Neishtadt in $1 9 8 2 ^ { [ \mathrm { N e i } 8 2 ] }$ and Poschel in¨ $1 9 8 2 ^ { [ \mathrm { P \ddot { 0 } s 8 2 } ] }$ . The estimates in terms of $\theta$ and $\Theta$ were given by Shang in $2 0 0 0 ^ { [ \mathrm { { S h a 0 0 a } ] } }$ , which are also crucial in the small twist mapping case.

# 13.3 KAM Theorem of Symplectic Algorithms for Hamiltonian Systems

In this section, we study stability of symplectic algorithms when applied to typical nonlinear Hamiltonian systems. We introduce a numerical version of the KAM theorem. Such a theorem was already suggested by Channel and Scovel in $1 9 9 0 ^ { [ \mathrm { C S 9 0 } ] }$ , Kang Feng 1991[Fen91] , and Sanz-Serna and Calvo in $1 9 9 4 ^ { \left[ { \mathrm { S S C 9 4 } } \right] }$ . Its rigorous formulation and proof were given by Shang in 1999 and $2 0 0 0 ^ { [ \mathrm { { S h a 9 9 } , \mathrm { { S h a 0 0 b } ] } } }$ based on the thesis[Sha91] . The main results consist of the existence of invariant tori, with a smooth foliation structure, of a symplectic numerical algorithm when it applies to a generic integrable Hamiltonian system with arbitrarily many degrees of freedom if the time-step size of the algorithm is sufficiently small and falls in a Cantor set of large measure. This existence result also implies that the algorithm, when it is applied to a generic integrable system of $n$ degrees of freedom, possesses $n$ independent smooth invariant functions which are in involution and well-defined on the set filled by the invariant tori in the sense of Whitney. The invariant tori are just the level sets of these functions. Quantitative analysis shows that the numerical invariant tori of a symplectic algorithm can approximate the corresponding exact invariant tori of the systems.

# 13.3.1 Symplectic Algorithms as Small Twist Mappings

We consider a Hamiltonian system with $n$ degrees of freedom in canonical form

$$
\dot { x } = - \frac { \partial K } { \partial y } ( x , y ) , \quad \dot { y } = \frac { \partial K } { \partial x } ( x , y ) , \quad ( x , y ) \in D ,
$$

where $D$ is a connected bounded, open subset of $\mathbf { R } ^ { 2 n }$ ; $x$ and $y$ are both $n$ -dimensional Euclidean coordinates with $\dot { x }$ and $\dot { y }$ the derivatives of $x$ and $y$ with respect to the time “t” respectively; $K : D \to \mathbf { R } ^ { 1 }$ is the Hamiltonian.

A symplectic algorithm that is compatible with the system (3.1) is a discretization scheme such that, when applied to the system (3.1), it uniquely determines one parameter family of symplectic step-transition maps $G _ { K } ^ { t }$ that approximates the phase flow $g _ { K } ^ { t }$ in the sense that

$$
\operatorname * { l i m } _ { t \to 0 } { \frac { 1 } { t ^ { s } } } { \Big ( } G _ { K } ^ { t } ( z ) - g _ { K } ^ { t } ( z ) { \Big ) } = 0 \quad { \mathrm { ~ f o r ~ a n y ~ } } z = ( x , y ) \in D
$$

for some $s \geq 1$ , here $t > 0$ is the time-step size of the algorithm and $s$ , the largest integer such that (3.2) holds, is the order of accuracy of the algorithm approximating the continuous systems. Note that the domain in which $G _ { K } ^ { t }$ is well-defined, say $\smash { \widetilde { D } } _ { t } ^ { - }$ , depends on $t$ generally and converges to $D$ as $t  0$ — this means that any $z \in D$ may be contained in $\tilde { \boldsymbol D } _ { t }$ when $t$ is sufficiently close to zero.

From (3.2), we may assume

$$
G _ { K } ^ { t } ( z ) = g _ { K } ^ { t } ( z ) + t ^ { s } R _ { K } ^ { t } ( z ) ,
$$

where

$$
R _ { K } ^ { t } ( z ) = \frac { 1 } { t ^ { s } } \Big ( G _ { K } ^ { t } ( z ) - g _ { K } ^ { t } ( z ) \Big )
$$

is well-defined for $z \in \widetilde { D } _ { t } \subset D$ and has the limit zero as $t  0$ for $z \in D$ . Below, we prove the main results of this chapter by simply regarding the approximation $G _ { K } ^ { t }$ to the phase flow $g _ { K } ^ { t }$ of the above form as a symplectic discretization scheme of order $s$ .

We assume that the system (3.1) is integrable. That is, there exists a system of action-angle coordinates $( p , q )$ in which the domain $D$ can be expressed as the form $B \times \mathbf { T } ^ { n }$ and the Hamiltonian depends only on the action variables, where $B$ is a connected bounded, open subset of $\mathbf { R } ^ { n }$ and $\mathbf { T } ^ { n }$ the standard $n$ -dimensional torus. Let us denote by $\Psi : B \times \mathbf { T } ^ { n }  D$ the coordinate transformation from $( p , q )$ to $( x , y )$ , then $\Psi$ is a symplectic diffeomorphism from $B \times \mathbf { T } ^ { n }$ onto $D$ . The new Hamiltonian

$$
K \circ \Psi ( p , q ) = H ( p ) , \quad ( p , q ) \in B \times \mathbf { T } ^ { n }
$$

only depends on $p$ . Therefore, in the action-angle coordinates $( p , q )$ , (3.1) takes the simple form

$$
\dot { p } = 0 , \quad \dot { q } = \omega ( p ) = \frac { \partial H } { \partial p } ( p )
$$

and the phase flow $g _ { H } ^ { t }$ is just the one parameter group of rotations $( p , q ) \to ( p , q +$ $t \omega ( p ) )$ which leaves every torus $\{ p \} \times \mathbf { T } ^ { n }$ invariant.

Assume $K$ is analytic and, without loss of generality, assume the domain of analyticity of $K$ contains the following open subset of $\mathbf { C } ^ { 2 n }$

$$
{ \mathcal D } _ { \alpha _ { 0 } } = \left\{ z = ( x , y ) \in { \bf C } ^ { 2 n } : d ( z , D ) < \alpha _ { 0 } \right\} ,
$$

with some $\alpha _ { 0 } > 0$ , where

$$
d ( z , D ) = \operatorname* { i n f } _ { z ^ { \prime } \in D } | z - z ^ { \prime } |
$$

denotes the distance from the point $z \in \mathbf { C } ^ { 2 n }$ to the set $D \subset \mathbf { C } ^ { 2 n }$ in which $| z | =$ $\operatorname* { m a x } _ { 1 \leq j \leq 2 n } | z _ { j } |$ for $z = ( z _ { 1 } , \cdots , z _ { 2 n } )$ . Also, we assume that $\Psi$ extends analytically to the following complex domain

$$
S ( r _ { 0 } , \rho _ { 0 } ) = \left\{ ( p , q ) \in { \bf C } ^ { 2 n } : d ( p , B ) < r _ { 0 } , { \mathrm R e } q \in { \bf T } ^ { n } , | { \mathrm I m } q | < \rho _ { 0 } \right\}
$$

with $r _ { 0 } > 0 , \rho _ { 0 } > 0$ and has period $2 \pi$ in each component of $q$ . In (3.7), $B$ is considered as a subset of $\mathbf { C } ^ { 2 n }$ . Without loss of generality, we suppose $\widetilde { \mathcal { D } } ( r _ { 0 } , \rho _ { 0 } ) =$ $\Psi \Big ( S ( r _ { 0 } , \rho _ { 0 } ) \Big ) \subset \mathscr { D } _ { \alpha _ { 0 } }$ and further that $\Psi$ is a diffeomorphism from $S ( r _ { 0 } , \rho _ { 0 } )$ onto $\widetilde { \mathcal { D } } ( r _ { 0 } , \rho _ { 0 } )$ . So the Equation (3.4) is valid for $( p , q ) \in S ( r _ { 0 } , \rho _ { 0 } )$ and

$$
\Psi ^ { - 1 } \circ g _ { K } ^ { t } \circ \Psi = g _ { H } ^ { t }
$$

on this complex domain of coordinates $( p , q )$ .

Checking the existing available symplectic algorithms, we find that $G _ { K } ^ { t }$ is always analytic if the Hamiltonian $K$ is analytic. Note that the domain in which $G _ { K } ^ { t }$ is welldefined converges to the domain of definition of $g _ { K } ^ { t }$ as $t$ approaches zero. We may assume, without loss of generality, $G _ { K } ^ { t }$ is well-defined and analytic in the complex domain ${ \mathcal D } _ { \alpha _ { 0 } }$ for $t$ sufficiently close to zero. Moreover, in the analytic case, we have

$$
\begin{array} { r } { \Big | G _ { K } ^ { t } ( z ) - g _ { K } ^ { t } ( z ) \Big | \le t ^ { s + 1 } M ( z , t ) } \end{array}
$$

with an everywhere positive continuous function ${ \cal M } : { \mathcal { D } } _ { \alpha _ { 0 } } \times [ 0 , \delta _ { 1 } ] \to \mathbf { R }$ for some sufficiently small $\delta _ { 1 } > 0$ .

Lemma 3.1. There exists $\delta _ { 2 } > 0$ such that for $t \in [ 0 , \delta _ { 2 } ]$ , $\widetilde { G } _ { K } ^ { t } = \Psi ^ { - 1 } \circ G _ { K } ^ { t } \circ \Psi$ is "well-defined and real analytic on the closed complex domain $\overline { { S ( \frac { r _ { 0 } } { 2 } , \frac { \rho _ { 0 } } { 2 } ) } }$ and

$$
\left| \widetilde { G } _ { K } ^ { t } ( p , q ) - g _ { H } ^ { t } ( p , q ) \right| \leq M t ^ { s + 1 } , \quad ( p , q ) \in \overline { { S \Big ( \frac { r _ { 0 } } { 2 } , \frac { \rho _ { 0 } } { 2 } \Big ) } } , \quad t \in [ 0 , \delta _ { 2 } ] ,
$$

where $M$ is a positive constant depending on $r _ { 0 } , \rho _ { 0 } , \alpha _ { 0 } , \delta _ { 1 } , \Psi$ and $K$ , not on $t$ .

Proof. Let $\mathcal { U } _ { 1 } = \overline { { S \Big ( \frac { r _ { 0 } } { 2 } , \frac { \rho _ { 0 } } { 2 } \Big ) } }$ and $\mathcal { V } _ { 1 } = \Psi \Big ( \overline { { S \Big ( \frac { r _ { 0 } } { 2 } , \frac { \rho _ { 0 } } { 2 } \Big ) } } \Big )$ . Since $\mathcal { U } _ { 1 }$ is a closed subset of $S ( r _ { 0 } , \rho _ { 0 } )$ and $\Psi$ is a diffeomorphism from $S ( r _ { 0 } , \rho _ { 0 } )$ onto ${ \mathcal D } _ { \alpha _ { 0 } }$ , $\mathcal { V } _ { 1 }$ is closed in ${ \mathcal D } _ { \alpha _ { 0 } }$ . Let $\xi$ be the distance from $\nu _ { 1 }$ to the boundary of ${ \mathcal D } _ { \alpha _ { 0 } }$ , then $\xi > 0$ . The compactness of $\nu _ { 1 }$ implies that there exists $0 < \delta _ { 1 } ^ { ' } < \delta _ { 1 }$ such that $g _ { K } ^ { t }$ maps $\nu _ { 1 }$ into $\mathcal { V } _ { 1 } + \frac { \xi } { 2 }$ for $t \in [ 0 , \delta _ { 1 } ^ { ' } ]$ , where $\mathcal { V } _ { 1 } + \frac { \xi } { 2 }$ denotes the union of all complex open balls centered in $\nu _ { 1 }$ with radius $\frac { \xi } { 2 }$ . Since $M ( z , t )$ is continuous and positive for $( z , t ) \in \mathcal { V } _ { 1 } \times [ 0 , \delta _ { 1 } ^ { ' } ]$ , there exists a constant $M _ { 0 } > 0$ which is an upper bound of $M ( z , t )$ on $\nu _ { 1 } \times [ 0 , \delta _ { 1 } ^ { ' } ]$ . Let $\delta _ { 2 } = \operatorname * { m i n } \left\{ 1 , \delta _ { 1 } ^ { ' } , \sqrt { \frac { \xi } { 4 M _ { 0 } } } \right\}$ . Then for $t \in [ 0 , \delta _ { 2 } ]$ , $G _ { K } ^ { t }$ maps $\nu _ { 1 }$ into ${ \mathcal D } _ { \alpha _ { 0 } }$ and hence $\widetilde { G } _ { K } ^ { t } = \Psi ^ { - 1 } \circ G _ { K } ^ { t } \circ \Psi$ is well-defined on $\mathcal { U } _ { 1 }$ . The real analyticity of the map follows from the real analyticity of $\Psi$ and $K$ . To verify Equation (3.9) , we first note that the analyticity of $\Psi ^ { - 1 }$ on $\overline { { \mathcal { V } _ { 1 } + \frac { 3 \xi } { 4 } } } \subset \mathcal { D } _ { \alpha _ { 0 } }$ implies that

$$
\left. \frac { \partial \Psi ^ { - 1 } } { \partial z } ( z ) \right. \le M _ { 1 }
$$

for all $z \in { \overline { { \mathcal { V } } } } _ { 1 } + { \frac { 3 \xi } { 4 } }$ with some constant $M _ { 1 } ~ > ~ 0$ ,and then Taylor formula gives $\Psi ( p , q ) \in \mathcal { V } _ { 1 }$ and

$$
\bigl | R _ { K } ^ { t } ( \Psi ( p , q ) ) \bigr | = \bigl | G _ { K } ^ { t } ( \Psi ( p , q ) ) - g _ { K } ^ { t } ( \Psi ( p , q ) ) \bigr | \le M _ { 0 } t ^ { s + 1 } \le \frac { \xi } { 4 }
$$

for $( p , q ) \in \mathcal { U } _ { 1 }$ and $t \in [ 0 , \delta _ { 2 } ]$ . Therefore,

$$
\begin{array} { r l } & { | \widetilde { G } _ { K } ^ { t } ( p , q ) - g _ { H } ^ { t } ( p , q ) | = | \Psi ^ { - 1 } ( g _ { K } ^ { t } ( \Psi ( p , q ) ) + R _ { K } ^ { t } ( \Psi ( p , q ) ) ) - \Psi ^ { - 1 } ( g _ { K } ^ { t } ( \Psi ( p , q ) ) ) } \\ & { \qquad \leq 2 n M _ { 1 } M _ { 0 } t ^ { s + 1 } . } \end{array}
$$

Let $M = 2 n M _ { 1 } M _ { 0 }$ , then (3.9) is verified.

The above lemma shows that $\smash { \widetilde { G } _ { K } ^ { t } }$ is an approximant to the one parameter group of integrable rotations $g _ { H } ^ { t }$ up to order $t ^ { s + 1 }$ as $t$ approaches zero. To apply Theorem 2.4, we need to verify the exact symplecticity of $\smash { \widetilde { G } _ { K } ^ { t } }$ so that it can be expressed by globally defined generating function. Because is not necessarily exact symplectic, the exact symplecticity of $\widetilde { G } _ { K } ^ { t } = \Psi ^ { - 1 } \circ G _ { K } ^ { t } \circ \Psi$ is not trivially observed.

Lemma 3.2. Let $G$ be an exact symplectic mapping of class $C ^ { 1 }$ from $D$ into $\mathbf { R } ^ { 2 n }$ where $D$ is an open subset of $\mathbf { R } ^ { 2 n }$ and let $\Psi$ be a symplectic diffeomorphism from $B \times \mathbf { T } ^ { n }$ onto $D$ . Then $\Psi ^ { - 1 } \circ G \circ \Psi$ is an exact symplectic mapping in the domain in which it is well-defined.

Proof. Let $( \widehat { p } , \widehat { q } ) = \Psi ^ { - 1 } \circ G \circ \Psi ( p , q )$ and let $\gamma$ be any given closed curve in the  domain of definition of $\widetilde { G } = : \Psi ^ { - 1 } \circ G \circ \Psi$ , which is an open subset of $B \times \mathbf { T } ^ { n }$ . The exact symplecticity of G will be implied by[Arn89]

$$
I ( \gamma ) = \int _ { \gamma } \widehat { p } \mathrm { d } \widehat { q } - \int _ { \gamma } p \mathrm { d } q = 0 .
$$

Now we verify (3.10). Let $\left( x , y \right) = \Psi \left( p , q \right)$ and $( { \widehat x } , { \widehat y } ) = \Psi ( { \widehat p } , { \widehat q } )$ . Then $( { \widehat { x } } , { \widehat { y } } ) =$ $G ( x , y )$ . Since $G$ is an exact symplectic, we have $\begin{array} { r } { \int _ { \gamma } \widehat { x } \mathrm { d } \widehat { y } - \int _ { \gamma } x \mathrm { d } y = 0 } \end{array}$  , where $x$

$y .$ , $\widehat { x }$ , $\widehat { y }$ are considered as functions of $( p , q )$ , which vary over $\gamma$ . Therefore, with these  conventions and with $\gamma ^ { \prime } = \Psi ^ { - 1 } \circ G \circ \Psi ( \gamma )$ ,

$$
\begin{array} { r l } { I ( \gamma ) ~ = } & { \displaystyle \int _ { \gamma } \widehat { p } \mathrm { d } \widehat { q } - \int _ { \gamma } \widehat { x } \mathrm { d } \widehat { y } + \int _ { \gamma } x \mathrm { d } y - \int _ { \gamma } p \mathrm { d } q } \\ { ~ = } & { \displaystyle \int _ { \gamma ^ { \prime } } p \mathrm { d } q - \int _ { \Psi ( \gamma ^ { \prime } ) } x \mathrm { d } y + \int _ { \Psi ( \gamma ) } x \mathrm { d } y - \int _ { \gamma } p \mathrm { d } q } \\ { ~ = } & { \displaystyle \int _ { \gamma ^ { \prime } - \gamma } p \mathrm { d } q - \int _ { \Psi ( \gamma ^ { \prime } ) - \Psi ( \gamma ) } x \mathrm { d } y . } \end{array}
$$

Note that $G$ is exact and hence it is homotopic to the identity. This implies that $\Psi ^ { - 1 } \circ$ $G \circ \Psi$ is homotopic to the identity too. So $\gamma ^ { \prime }$ and $\gamma$ belong to the same homological class in the fundamental group of the manifold $B \times \mathbf { T } ^ { n }$ . Therefore, one may find a 2-dimensional surface, say $\sigma$ , in the phase space $B \times \mathbf { T } ^ { n }$ , which is bounded by $\gamma ^ { \prime }$ and $\gamma . \Psi ( \sigma )$ is then a 2-dimensional surface in $D$ bounded by $\Psi ( \gamma ^ { \prime } )$ and $\Psi ( \gamma )$ . By stokes formula and from (3.11), we get

$$
I ( \gamma ) = \int _ { \sigma } \mathrm { d } p \wedge \mathrm { d } q - \int _ { \Psi ( \sigma ) } \mathrm { d } x \wedge \mathrm { d } y ,
$$

which is equal to zero because $\Psi$ preserves the two form $\mathrm { d } p \wedge \mathrm { d } q$

Checking the existing available symplectic algorithms, we observe that they are generally constructed by discretizing Hamiltonian systems, therefore, they generate exact symplectic step transition maps. In our case, this means that $G _ { K } ^ { t }$ is a oneparameter family of exact symplectic mappings. By Lemma 3.2, so is $\smash { \widetilde { G } _ { K } ^ { t } }$ . As a result, $\smash { \widetilde { G } _ { K } ^ { t } }$ can be re-expressed by generating function. On the other hand, by Lemma 3.1, we see that $\smash { \widetilde { G } _ { K } ^ { t } }$ is near the identity and approximates $g _ { H } ^ { t }$ up to order $t ^ { s + 1 }$ on $S \left( { \frac { r _ { 0 } } { 2 } } , { \frac { \rho _ { 0 } } { 2 } } \right)$ for $t \in [ 0 , \delta _ { 2 } ]$ . A simple argument of implicit function theorem, with the notice of the exact symplecticity of $\smash { \widetilde { G } _ { K } ^ { t } }$ , will show the following:

Lemma 3.3. There exists a function $h ^ { t }$ which depends on the time step $t$ such that it is well-defined and real analytic on the domain $S \Big ( \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } \Big )$ for $t \in [ 0 , \delta _ { 3 } ]$ with $\delta _ { 3 }$ being a sufficiently small positive number so that $\widetilde { G } _ { K } ^ { t } : ( p , q ) \to ( \widehat { p } , \widehat { q } )$ can be expressed by $h ^ { t }$ as follows:

$$
\widehat { p } = p - t ^ { s + 1 } \frac { \partial h ^ { t } } { \partial q } ( \widehat { p } , q ) , \quad \widehat { q } = q + t \omega ( \widehat { p } ) + t ^ { s + 1 } \frac { \partial h ^ { t } } { \partial \widehat { p } } ( \widehat { p } , q ) .
$$

Proof. It follows immediately from Lemmas 3.1 and 3.3 that

$$
\left\| \frac { \partial h ^ { t } } { \partial \widehat { \boldsymbol { p } } } \right\| _ { \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } } \leq M , \quad \left\| \frac { \partial h ^ { t } } { \partial q } \right\| _ { \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } } \leq M .
$$

Fix $( \widehat { p } _ { 0 } , q _ { 0 } ) \in D$ and let $h ^ { t } ( \widehat { p } _ { 0 } , q _ { 0 } ) = 0$ . For any $( \widehat { p } , q ) \in S \Big ( \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } \Big )$ , integrating the exact differential one form $\frac { \partial h ^ { t } } { \partial \widehat { p } } \mathrm { d } \widehat { p } + \frac { \partial h ^ { t } } { \partial q } \mathrm { d } q$ along one of the shortest curves from

$( \widehat { p } _ { 0 } , q _ { 0 } )$ to $( \widehat { p } , q )$ in $S \left( \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } \right)$ and then taking the maximal norm of the integration for $( \widehat { p } , q )$ over $S \left( \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } \right)$ , we obtain the estimate

$$
\| h ^ { t } \| _ { \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } } \leq 2 n M L , \quad \mathrm { f o r } \ t \in [ 0 , \delta _ { 3 } ] ,
$$

where $M$ is the constant in Lemma 3.1 and $L$ is an upper bound of the length of the shortest curves from (p0, q0) to points of S  r0 , ρ0  , which is clearly a finite positive number. Note that $B$ is a connected bounded, open subset of $\mathbf { R } ^ { n }$ and therefore, $S \left( \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } \right)$ is bounded too. -

# 13.3.2 Numerical Version of KAM Theorem

We formulate the main result of this chapter as follows.

Theorem 3.4. Let Hamiltonian system (3.1) be integrable in a connected bounded, open domain $D$ of $\mathbf { R } ^ { 2 n }$ , and let $K$ be real analytic and nondegenerate in the sense of Kolmogorov after expressed as action-angle variables. For an analytic symplectic algorithm4 compatible with the system, as long as the time-step t of the algorithm is small enough, most nonresonant invariant tori of the integrable system do not vanish, but are only slightly deformed, so that in the phase space $D$ , the symplectic algorithm also has invariant tori densely filled with phase orbits winding around them quasiperiodically, with a number of independent frequencies equal to the number of degrees of freedom. These invariant tori are all analytic manifolds and form a Cantor set, say $D _ { t }$ . The Lebesgue measure $m D _ { t }$ of the Cantor set $D _ { t }$ tends to $m D$ as $t$ tends to zero. Moreover, on $D _ { t }$ , the algorithm is conjugate to a one parameter family of rotations of the form $( p , q ) \to ( p , q + t \omega _ { t } ( p ) )$ by a $C ^ { \infty }$ -symplectic conjugation $\Psi _ { t } : B _ { t } \times \mathbf { T } ^ { n } $ $D _ { t }$ , where $( p , q )$ are action-angle coordinates and $\omega _ { t }$ is the frequency map defined on a Cantor set $B _ { t } \subset \mathbf { R } ^ { n }$ of actions.

More quantitative results hold. For any given and sufficiently small $\gamma > 0$ , if the time step $t$ is sufficiently small, then there exists closed subsets $B _ { \gamma , t }$ of $B _ { t }$ and $D _ { \gamma , t }$ of $D _ { t }$ such that $D _ { \gamma , t } = \Psi _ { t } ( B _ { \gamma , t } \times \mathbf { T } ^ { n } )$ and the following hold:

$1 ^ { \circ }$ $m D _ { \gamma , t } \geq ( 1 - c _ { 1 } ^ { \prime } \gamma ) m D$ , where $c _ { 1 } ^ { \prime }$ is a positive constant not depending on $t$ and $\gamma$ ;

$2 ^ { \circ }$ $\| \Psi _ { t } - \Psi \| _ { \beta , \beta \lambda ; B _ { \gamma , t } \times \mathbf { T } ^ { n } }$ , $\| \omega _ { t } - \omega \| _ { \beta + 1 ; B _ { \gamma , t } } \leq c _ { 2 } ^ { \prime } \gamma ^ { - ( 2 + \beta ) } \cdot t ^ { s }$ for any $\beta \geq 0$ , where $s$ γ,t Tis the accuracy order of the algorithm, $\lambda > n + 2$ , $c _ { 2 } ^ { \prime }$ is a positive constant not depending on $\gamma$ and $t .$ . The norms here are understood in the sense of Whitney;

$3 ^ { \circ }$ Every numerical invariant torus in $D _ { \gamma , t }$ is $t ^ { s }$ -close to the invariant torus of the same frequencies of the original integrable system (3.1) in the sense of Hausdorff 5.

Proof. Now the analytic version of Theorem 2.4 can be applied to $S _ { t } = \widetilde { G } _ { K } ^ { t }$ . The conditions required by Theorem 2.4 are satisfied clearly according to the assumptions of Theorem 2.1. For example, the nondegeneracy of the integrable system in the sense of Kolmogorov means that the frequency map $\omega : B \to \mathbf { R } ^ { n }$ is nondegenerate and therefore, there exists positive constants $\theta \leq \Theta$ such that $\omega$ satisfies (2.4) with some positive numbers $r ~ \leq ~ r _ { 0 }$ . We assume $r ~ = ~ r _ { 0 }$ here without loss of generality. In Theorem 2.4, the function $h$ is replaced by $t ^ { s } h ^ { t }$ which satisfies the estimate (2.40) with $r = \frac { r _ { 0 } } { 4 }$ and $\rho = \frac { \rho _ { 0 } } { 4 }$ if we choose

$$
\gamma = \gamma _ { t } = : T t ^ { d } , \quad \mathrm { w i t h ~ } 0 < d \leq \frac { s } { 2 } \mathrm { a n d } T = \sqrt { \frac { 2 n M L } { \delta _ { 0 } } } \theta ^ { - 1 } \theta ^ { \frac { 3 } { 2 } }
$$

and if $t$ is sufficiently small, where $\delta _ { 0 }$ is the bound given by (2.40) of Theorem 2.4. It is clear that the so chosen $\gamma$ satisfies the condition $\gamma \leq \operatorname* { m i n } \left( 1 , \frac { 1 } { 2 } r \theta \right)$ required by Theorem 2.4 for $t$ sufficiently close to zero. By Theorem 2.4, we then have the Cantor sets $B _ { t } = B _ { \gamma , t } \subset B$ and $\Omega _ { t } = \Omega _ { \gamma , t } \subset \omega ( B )$ , a surjective map $\omega _ { t } = \omega _ { \gamma , t } : B _ { t } \to \Omega _ { t }$ of class $C ^ { \infty }$ and a symplectic mapping $\Phi _ { t } : B _ { t } \times \mathbf { T } ^ { n }  \mathbf { R } ^ { n } \times \mathbf { T } ^ { n }$ of class $C ^ { \infty , \omega }$ , in the sense of Whitney, such that the conclusions (1) – (4) of Theorem 2.4 hold with $\gamma = T t ^ { d }$ . From (2.10), invariant tori of $\smash { \widetilde { G } _ { K } ^ { t } }$ fill out a set $\mathscr { E } _ { t } = \mathscr { E } _ { \gamma , t } = \Phi _ { t } \bigl ( B _ { t } \times \mathbf { T } ^ { n } \bigr )$ in phase space $\mathcal { E } = B \times \mathbf { T } ^ { n }$ with measure estimate

$$
m { \mathcal E } _ { t } \geq \big ( 1 - c _ { 4 } { \varGamma } \big ( \theta \theta ^ { - 1 } \big ) ^ { - n } t ^ { d } \big ) m { \mathcal E } .
$$

From (2.11), with the notice of (2.7) and the fact that

$$
\| h ^ { t } \| _ { \beta \lambda + \lambda + \tau } \leq c _ { 7 } \| h ^ { t } \| _ { \frac { r _ { 0 } } { 4 } , \frac { \rho _ { 0 } } { 4 } }
$$

by Cauchy’s estimate for derivatives of an analytic function, we have

$$
\begin{array} { r l } { \| \Phi _ { t } - I \| _ { \beta , \beta \lambda ; B _ { t } \times \mathbf { T } ^ { n } } } & { \le \ \left( \gamma \theta ^ { - 1 } \right) ^ { - \beta } \| \sigma _ { \gamma \theta ^ { - 1 } } ^ { - 1 } \circ ( \Phi _ { t } - I ) \| _ { \beta , \beta \lambda ; \gamma \theta ^ { - 1 } } } \\ & { \le \ c _ { 5 } c _ { 7 } \gamma ^ { - ( 2 + \beta ) } \theta ^ { 1 + \beta } \| t ^ { s } h ^ { t } \| _ { \frac { r _ { 0 } } 4 , \frac { \rho _ { 0 } } 4 } } \\ & { \le \ c _ { 8 } \theta ^ { 2 + \beta } \theta ^ { - ( 2 + \beta / 2 ) } \cdot t ^ { s - ( 2 + \beta ) d } } \end{array}
$$

for $t$ sufficiently close to zero, where

$$
c _ { 8 } = c _ { 5 } c _ { 7 } ( 2 n M L ) ^ { - \frac { \beta } { 2 } } \delta _ { 0 } ^ { 1 + \frac { \beta } { 2 } } .
$$

In the last inequality of (3.16), we have used the estimate (3.13) for $h ^ { t }$ . From (2.11), we also get

$$
\begin{array} { r l r } { \| \omega _ { t } - \omega \| _ { \beta + 1 ; B _ { t } } } & { \leq } & { ( \gamma \theta ^ { - 1 } ) ^ { - ( \beta + 1 ) } \| \omega _ { t } - \omega \| _ { \beta + 1 ; \gamma \Theta ^ { - 1 } } } \\ & { \leq } & { c _ { 8 } \theta ^ { 2 + \beta } \Theta ^ { - ( 1 + \beta / 2 ) } \cdot t ^ { s - ( 2 + \beta ) d } . } \end{array}
$$

Let $\Psi _ { t } = \Psi \circ \Phi _ { t }$ and $D _ { t } = \Psi ( \mathcal { E } _ { t } )$ , then $G _ { K } ^ { t } \circ \Psi _ { t } = \Psi _ { t } \circ R _ { t }$ , which means that $\Psi _ { t }$ realizes the conjugation from $G _ { K } ^ { t }$ to $R _ { t } : ( p , q ) \to ( p , q + t \omega _ { t } ( p ) )$ and for any fixed $P \in B _ { t }$ , $\Psi _ { t } ( P , { \bf T } ^ { n } )$ is an invariant torus of $G _ { K } ^ { t }$ , which is an analytic Lagrangian manifold since $\Psi _ { t }$ is a symplectic diffeomorphism and analytic with respect to the angle variables. On the torus, the iterations of $G _ { K } ^ { t }$ starting from any fixed point are quasi-periodic with frequencies $t \omega _ { t } ( p )$ which are rationally independent and satisfy the diophantine condition (4.3) with $\omega = \omega _ { t } ( p )$ and $\gamma = T t ^ { d }$ . These invariant tori distribute $C ^ { \infty }$ -smoothly in the phase space due to the $C ^ { \infty }$ -smoothness of the conjugation $\Psi _ { t }$ . Moreover, we have the same estimates for the measure of $D _ { t }$ and for the closeness of $\Psi _ { t }$ to $\Psi$ as (3.15) and (3.16), with larger constants $c _ { 4 }$ and $c _ { 8 }$ , in which $\mathcal { E } _ { t }$ , $\mathcal { E }$ , $\Phi _ { t }$ and $I$ are replaced by $D _ { t } , D , \Psi _ { t }$ and $\Psi$ respectively. For $\beta \geq 0$ , if we choose $d$ satisfying

$$
0 < d < \frac { s } { 2 + \beta } ,
$$

then, from the above estimates, we see that $\Psi _ { t }$ , with the domain of definition $B _ { t } \times \mathbf { T } ^ { n }$ , converges to the $\Psi$ in $C ^ { \beta , \beta \lambda }$ -norm and $\omega _ { t }$ , with the domain of definition $B _ { t }$ , converges to $\omega$ with respect to the $C ^ { \beta + 1 }$ -norm as $t$ tends to zero; the measure of $D _ { t }$ , the union of invariant tori of $G _ { K } ^ { t }$ , tends to the measure of the phase space $D$ . These arguments just complete the proof of the first part of Theorem 3.4.

Now, we prove the remainder of Theorem 3.4. From the estimates (3.15) – (3.17) and the uniform boundedness of the diffeomorphism $\Psi$ and its inverse as well as their derivatives, we see that if we choose $\gamma$ being fixed in advance and not depending on the time-step size $t$ of the algorithm, then we have

$$
m D _ { \gamma , t } \geq \big ( 1 - \widetilde { c } _ { 4 } ( \theta \Theta ^ { - 1 } ) ^ { - n } \gamma \big ) m D ,
$$

with constant $\widetilde { c } _ { 4 } > 0$ not depending on $\gamma$ and $t$ , where $D _ { \gamma , t } = \Psi ( \mathcal { E } _ { \gamma , t } )$ with $\mathcal { E } _ { \gamma , t } =$ $\Phi _ { t } ( B _ { \gamma , t } \times \mathbf { T } ^ { n } )$ and with $B _ { \gamma , t }$ being the subset of $B$ as indicated above. Note that $B _ { \gamma , t }$ is a closed subset of $B _ { t }$ and $D _ { \gamma , t }$ a closed subset of $D _ { t }$ if $t$ is sufficiently small. Moreover, the estimate

$$
\| \Psi _ { t } - \Psi \| _ { \beta , \beta \lambda ; B _ { \gamma , t } \times \mathbf { T } ^ { n } } \le \widetilde { c } _ { 8 } \gamma ^ { - ( 2 + \beta ) } \theta ^ { 1 + \beta } \cdot t ^ { s }
$$

and

$$
\| \omega _ { t } - \omega \| _ { \beta + 1 ; B _ { \gamma , t } } \leq \widetilde c _ { 8 } \gamma ^ { - ( 2 + \beta ) } \theta ^ { 2 + \beta } \cdot t ^ { s }
$$

hold for any $\beta \geq 0$ with $\widetilde { c } _ { 8 } \ > \ 0$ not depending on $\gamma$ and $t$ . The conclusions (1) "and (2) of the last part of Theorem 3.4 are proved if we set $c _ { 1 } ^ { \prime } = \widetilde { c } _ { 4 } \big ( \theta \Theta ^ { - 1 } \big ) ^ { - n }$ and $c _ { 2 } ^ { \prime } = \widetilde { c } _ { 8 } { \cdot } \operatorname* { m a x } ( \Theta ^ { 1 + \beta } , \Theta ^ { 2 + \beta } )$ ". From (3.19), it follows that for a sufficiently small $\gamma > 0$ , $D _ { \gamma , t }$ "has a positive Lebesque measure. From (2.12), it follows that for any $\omega ^ { \ast } \in \Omega _ { \gamma , t }$ , there exists $p ^ { * } \in B$ and $P ^ { * } \in B _ { \gamma , t }$ such that $\omega ( p ^ { * } ) = \omega _ { t } ( P ^ { * } ) = \omega ^ { * }$ and

$$
\begin{array} { r } { | P ^ { * } - p ^ { * } | \leq 2 n M L c _ { 6 } c _ { 7 } \big ( \gamma \theta \Theta ^ { - 1 } \big ) ^ { - 1 } \cdot t ^ { s } , } \end{array}
$$

which implies that

$$
\begin{array} { r } { | \Psi ( P ^ { * } , q ) - \Psi ( p ^ { * } , q ) | \leq 4 n ^ { 2 } M L \widetilde { M } _ { 1 } c _ { 6 } c _ { 7 } \big ( \gamma \theta \Theta ^ { - 1 } \big ) ^ { - 1 } \cdot t ^ { s } , } \end{array}
$$

uniformly for $q \in \mathbf { T } ^ { n }$ , where $\widetilde { M } _ { 1 }$ is an upper bound of the norm of $\frac { \partial \Psi } { \partial z } ( p , q )$ for $( p , q ) \in \overline { { { S \Big ( \frac { r _ { 0 } } { 2 } , \frac { \rho _ { 0 } } { 2 } \Big ) } } }$ . This estimate, together with (3.20), proves the third conclusion of the second part of Theorem 3.4. Theorem 3.4 is completely proved. -

A natural corollary of the above theorem is:

Corollary 3.5. Under the assumptions of the above theorem, there exists $n$ functions $F _ { 1 } ^ { t } , \cdots , F _ { n } ^ { t }$ which are defined on the Cantor set $D _ { t }$ and of class $C ^ { \infty }$ in the sense of Whitney such that:

$1 ^ { \circ }$ $F _ { 1 } ^ { t } , \cdots , F _ { n } ^ { t }$ are functionally independent and in involution (i.e., the Poisson bracket of any two functions vanishes on $D _ { t }$ );

$2 ^ { \circ }$ Every $F _ { j } ^ { t } \left( j = 1 , \cdots , n \right)$ , is invariant under the difference scheme and the invariant tori are just the intersection of the level sets of these functions;

$\ 3 ^ { \circ } \quad \ F _ { j } ^ { t } \ ( j = 1 , \cdot \cdot \cdot , n )$ approximate $n$ independent integrals in involution of the integrable system, with a suitable order of accuracy with respect to the time-step $t$ which will be explained in the proof.

Proof. By Theorem 3.4, we have

$$
G _ { K } ^ { t } \circ \Psi _ { t } ( p , q ) = \Psi _ { t } \circ R _ { t } ( p , q ) , \quad \mathrm { f o r } ( p , q ) \in B _ { t } \times { \bf T } ^ { n } ,
$$

where $R _ { t }$ is the integrable rotation $( p , q ) \to ( p , q + t \omega _ { t } ( p ) )$ and admits $n$ invariant functions, say, $p _ { 1 } , \cdots , p _ { n }$ , analytically defined on $B _ { t } \times \mathbf { T } ^ { n }$ . Let

$$
F _ { i } ^ { t } = p _ { i } \circ \Psi _ { t } ^ { - 1 } , \quad i = 1 , \cdots , n ,
$$

then they are well-defined on the Cantor set $D _ { t }$ and of class $C ^ { \infty }$ in the sense of Whitney due to the $C ^ { \infty }$ -smoothness of $\Psi _ { t } ^ { - 1 }$ on $D _ { t }$ . Moreover, we easily verify by (3.22) that

$$
F _ { i } ^ { t } \circ G _ { K } ^ { t } = F _ { i } ^ { t } , \quad i = 1 , \cdots , n ,
$$

and this means that $F _ { i } ^ { t } ( i = 1 , \cdots , n )$ are $n$ invariant functions of $G _ { K } ^ { t }$ . These $n$ invariant functions are functionally independent because $p _ { i }$ $( i = 1 , \cdots , n )$ are functionally independent and $\Psi _ { t }$ is a diffeomorphism. The claim that $F _ { i } ^ { t }$ and $F _ { j } ^ { t }$ are in involution for $1 \leq i$ , $j \leq n$ simply follows from the fact that $p _ { i }$ and $p _ { j }$ are in involution and $\Psi _ { t }$ is symplectic. Note that the Poisson bracket is invariant under symplectic coordinate transformations. Finally, it is observed from the proof of Theorem 3.4 that for each of $j = 1 , \cdots , n , F _ { j } ^ { t }$ approximates

$$
F _ { j } = p _ { j } \circ \Psi ^ { - 1 }
$$

as $t  0$ , with the order of accuracy equal to $t ^ { s - ( 2 + \beta ) d } \left( 0 < d < \frac { s } { 2 + \beta } \right.$ is given on the set $D _ { t }$ (note that this set depends also on $d$ by definition) and equal to $t ^ { s }$ on $D _ { \gamma , t }$ , a subset of $D _ { t }$ , in the norm of the class $C ^ { \beta }$ for any given $\beta \geq 0$ . It is clear that the functions $F _ { j }$ $( j = 1 , \cdots , n )$ are integrals of the integrable system and that any two of them are in involution by the symplecticity of $\Psi ^ { - 1 }$ . Corollary 3.5 is then proved. $\blacktriangle$

# 13.4 Resonant and Diophantine Step Sizes

It is observed from the proof of Theorem 3.4 that the preserved invariant tori have frequencies of the form $\omega _ { t } ~ = ~ t \omega$ , where $t$ is the step size of the algorithm and $\omega$ belongs to the frequency domain of the system, which the algorithm applies to. The frequency $\scriptstyle t \omega$ is required to satisfy the diophantine condition

$$
| \exp \left( i \langle k , t \omega \rangle \right) - 1 | \geq \frac { t \gamma } { | k | ^ { \tau } } , \quad 0 \neq k \in { \bf Z } ^ { n }
$$

with some $\gamma > 0$ and $\tau > 0$ , where $\langle u , v \rangle$ denotes the inner product of vectors $u$ and $v$ in $\mathbf { R } ^ { n }$ . Note that $t > 0$ may be arbitrarily small.

For any fixed $\boldsymbol \omega \in { \mathbf { R } } ^ { n }$ , even if it is a diophantine vector, there exists some $t$ in any small neighborhood of the origin such that (4.1) does not hold for any $\gamma > 0$ and any $\tau > 0$ . In fact, one can choose $t$ to satisfy the resonance relation

$$
\exp { ( i \langle k , t \omega \rangle ) } = 1
$$

for some $0 \neq k \in \mathbf { Z } ^ { n }$ . In the next section, we will show that such $t$ forms a dense set in $\mathbf { R }$ .

We note that a one-step algorithm, when applied to system of differential equations, can be regarded as a perturbation of the phase flow of the system. On the other hand, according to Poincare, arbitrarily small perturbations in the generic case may ´ destroy those resonant invariant tori of an integrable system. Therefore, to simulate the invariant torus with a given frequency of some Hamiltonian system by symplectic algorithms, one is forced to be very careful to select step sizes, say, to keep them away from some dense set.

Some questions arise: is it possible to simulate an invariant torus of an integrable system by symplectic algorithms? If possible, how does one select the step sizes and what structure does the set of those admitted step sizes have? In this paper, we try to answer these questions.

# 13.4.1 Step Size Resonance

For any frequency vector, step size resonance may take place very often.

Lemma 4.1. For any $\boldsymbol { \omega } \in \mathbf { R } ^ { n }$ , there exists a dense subset, say $D ( \omega )$ , of $\mathbf { R }$ such that for any $t \in D ( \omega )$ , the resonance relation (4.2) holds for some $0 \neq k \in \mathbf { Z } ^ { n }$ .

Proof. If $\langle k , \omega \rangle = 0$ for some $0 \neq k \in \mathbf { Z } ^ { n }$ , then $D ( \omega ) = \mathbf { R }$ . If $\langle k , \omega \rangle \neq 0$ for any $0 \neq k \in \mathbf { Z } ^ { n }$ , then

$$
D ( \omega ) = \Bigl \{ t = \frac { 2 \pi l } { \langle k , \omega \rangle } : 0 \neq k \in \mathbf { Z } ^ { n } , l \in \mathbf { Z } \Bigr \} ,
$$

which is clearly dense in $\mathbf { R }$ and the resonance relation (4.2) holds for any $t \in D ( \omega )$ .   
The proof of the lemma is completed.

Definition 4.2. $D ( \omega )$ is called the resonant set of step sizes with respect to the frequency $\boldsymbol \omega \in { \mathbf { R } } ^ { n }$ . Any $t \in D ( \omega )$ is called a resonant step size with respect to $\omega$ .

From Lemma 3.1, If $\omega \in \mathbf { R } ^ { n }$ is a resonant frequency, i.e., $\langle k , \omega \rangle = 0$ for some $0 \neq k \in \mathbf { Z } ^ { n }$ , then $D ( \omega ) = \mathbf { R }$ . In other words, each step size is resonant with respect to a resonant frequency. If $\boldsymbol { \omega } \in \mathbf { R } ^ { n }$ is a nonresonant frequency, i.e., $\langle k , \omega \rangle \neq 0$ for any $0 \neq k \in \mathbf { Z } ^ { n }$ , then $D ( \omega )$ is a countable and dense set of $\mathbf { R }$ . Because a resonant torus may be destroyed by arbitrarily small Hamiltonian perturbations (Poincare), any ´ invariant torus with frequency $\omega$ of a generic integrable system may not be preserved by symplectic algorithms with step sizes in $D ( \omega )$ . To simulate an invariant torus of the frequency $\omega$ , it is natural to consider those step sizes which are far away from the resonant set $D ( \omega )$ . Note that if $\omega$ is of at least 2 dimensions, the resonant set $D ( \omega )$ is “denser” than the rational numbers in $\mathbf { R }$ because the set $D ( \omega )$ consists of all real numbers in the case when $\omega$ is resonant and consists of all numbers of the form $\alpha _ { k } r$ in the case when $\omega$ is nonresonant, where $r$ takes any rational number and, for k ∈ Zn \ {0}, αk = $\alpha _ { k } = \frac { 2 \pi } { \langle k , \omega \rangle }$ which may be arbitrarily small and large, and moreover, there are arbitrarily many pairs of rationally independent numbers in $\alpha _ { k }$ . Anyway, for nonresonant $\omega$ , $D ( \omega )$ is countable.

# 13.4.2 Diophantine Step Sizes

Even though the step size may encounter resonance densely, we can still have a big possibility to select step sizes to keep away from resonance. We discuss this as follows.

Definition 4.3. A number $t \in \mathbf { R }$ is said to be of diophantine type with respect to the nonresonant frequency $\boldsymbol \omega \in { \mathbf { R } } ^ { n }$ , if

$$
\left| t - \frac { 2 \pi l } { \langle k , \omega \rangle } \right| \geq \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } , \quad 0 \neq k \in \mathbf { Z } ^ { n } , \ 0 < l \in \mathbf { Z }
$$

for some constants $\lambda > 0$ , $\mu$ and $\tau > 0$ .

We denote by $I _ { \lambda , \mu , \tau } ( \omega )$ , the set of numbers $\tau$ satisfying (4.4) for given constants $\lambda > 0$ , $\mu$ and $\tau > 0$ . Then, $I _ { \lambda , \mu , \tau } ( \omega )$ is a subset of $\mathbf { R }$ which is far away from resonance with respect to $\omega$ . For this set, we have:

Lemma 4.4. For any nonresonant frequency $\boldsymbol \omega \in { \mathbf { R } } ^ { n }$ , and for any $\lambda > 0$ , any $\mu$ and any $\tau > 0$ , the set $I _ { \lambda , \mu , \tau } ( \omega )$ is nowhere dense and closed in R. Moreover, if $\mu > 1$ and $\tau > n$ , then we have

$$
\begin{array} { r } { \mathrm { m e a s } \left( \mathbf { R } \setminus I _ { \lambda , \mu , \tau } ( \omega ) \right) \leq c \lambda , } \end{array}
$$

where c is a positive number depending only on $n , \mu$ and $\tau$

Proof. The nowhere denseness and the closedness of $I _ { \lambda , \mu , \tau } ( \omega )$ follow from the fact that the complement of the set is both open and dense in $\mathbf { R }$ for any $\lambda > 0$ , $\mu$ and $\tau > 0$ . It remains to prove (4.5). Since

$$
\mathbf { R } \setminus I _ { \lambda , \mu , \tau } ( \omega ) = \bigcup _ { 0 \leqslant \iota \in \mathbf { Z } ^ { n } \atop 0 \neq k \in \mathbf { Z } ^ { n } } \left\{ t \in \mathbf { R } : \Big | t - \frac { 2 \pi l } { \langle k , \omega \rangle } \Big | < \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } \right\} ,
$$

we have

$$
\begin{array} { r } { \mathrm { m e a s } \left( \mathbf { R } \setminus I _ { \lambda , \mu , \tau } ( \omega ) \right) \leq \displaystyle \sum _ { 0 \leq l \in \mathbf { Z } ^ { n } \atop 0 \neq k \in \mathbf { Z } ^ { n } } \frac { 2 \lambda } { l ^ { \mu } | k | ^ { \tau } } \leq 2 \lambda \displaystyle \sum _ { l = 1 } ^ { \infty } \frac { 1 } { l ^ { \mu } } \cdot \displaystyle \sum _ { 0 \neq k \in \mathbf { Z } ^ { n } } \frac { 1 } { | k | ^ { \tau } } . } \end{array}
$$

Define

$$
c _ { \mu } = \sum _ { l = 1 } ^ { \infty } { \frac { 1 } { l ^ { \mu } } } .
$$

Then $c _ { \mu } < \infty$ when $\mu > 1$ and

$$
\begin{array} { r l r } {  { \sum _ { 0 \neq k \in { \bf Z } ^ { n } } | k | ^ { - \tau } = \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ^ { \tau } } \cdot \# \{ k \in { \bf Z } ^ { n } : | k | = m \} \le 2 ^ { n } \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ^ { \tau } } \mathrm { C } _ { m } ^ { n + m - 1 } } } \\ & { } & \\ & { } & { \le 2 ^ { 2 n - 1 } \sum _ { m = 1 } ^ { \infty } \frac { 1 } { m ^ { \tau - n + 1 } } = 2 ^ { 2 n - 1 } c _ { \tau - n + 1 } < \infty \qquad } \end{array}
$$

when $\tau > n$ , here $\# S$ denotes the number of the elements of the set $S$ and $\mathrm { C _ { k } ^ { s } }$ are binomial coefficients. (4.5) is verified with

$$
c = 4 ^ { n } c _ { \mu } c _ { \tau - n + 1 } .
$$

Therefore, the lemma is completed.

Remark 4.5. We may define $I _ { \lambda , \mu , \tau } ( \omega )$ to be empty for any resonant frequency $\omega$ and any $\lambda > 0$ , any $\mu$ and any $\tau > 0$ because no number $t$ satisfies (4.4) in this case. It is possible that the set $I _ { \lambda , \mu , \tau } ( \omega )$ may still be empty even for nonresonant frequencies $\omega$ if here the numbers $\mu$ and $\tau$ are not properly chosen. Anyway, the above lemma shows that if $\mu > 1$ and $\tau > n$ , then the set $I _ { \lambda , \mu , \tau } ( \omega )$ has positive Lebesgue measure and hence is nonempty for any $\lambda > 0$ .

Remark 4.6. If $\lambda _ { 1 } > \lambda _ { 2 } > 0$ , then ${ I _ { \lambda _ { 1 } , \mu , \tau } ( \omega ) \subset I _ { \lambda _ { 2 } , \mu , \tau } ( \omega ) }$ . Therefore, if $\omega$ is a nonresonant frequency and $\mu > 1$ and $\tau > n$ , then the set of all real numbers $t$ satisfying (4.4) for some $\lambda > 0$ has full Lebesgue measure in any measurable set of $\mathbf { R }$ . It should be an interesting number theoretic problem to study the cases when $\mu \leq 1$ or $\tau \leq n$ . In numerical analysis, the step sizes are usually considered only in a bounded interval. We take the interval $[ - 1 , 1 ]$ as illustration without loss of generality.

Lemma 4.7. For a nonresonant frequency $\omega = ( \omega _ { 1 } , \omega _ { 2 } , \cdot \cdot \cdot , \omega _ { n } )$ , assume $0 < \lambda <$ $\frac { 2 \pi } { | \omega | }$ with $| \omega | = \operatorname* { m a x } _ { 1 \leq j \leq n } | \omega _ { j } |$ . If $- 1 \leq \mu \leq 1$ and $\mu + \tau > n + 1$ , then we have

$$
\operatorname { m e a s } \left( [ - 1 , 1 ] \setminus I _ { \lambda , \mu , \tau } ( \omega ) \right) \leq \widetilde c \lambda ,
$$

where $\widetilde { c }$ is a positive number depending not only on $n , \mu$ and $\tau$ but also on $| \omega |$ .

Proof. The set $[ - 1 , 1 ] \setminus I _ { \lambda , \mu , \tau } ( \omega )$ is contained in the union of all subintervals

$$
\left( \frac { 2 \pi l } { \langle k , \omega \rangle } - \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } , \frac { 2 \pi l } { \langle k , \omega \rangle } + \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } \right)
$$

for those $l \in \mathbf { Z } , l > 0$ and $k \in \mathbf { Z } ^ { n } \setminus \{ 0 \}$ such that

$$
\frac { 2 \pi l } { | \langle k , \omega \rangle | } < 1 + \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } .
$$

Since $- 1 \leq \mu \leq 1$ , we have that $\tau > n + 1 - \mu \geq n$ and (3.30) implies that $| k | > \bigg ( \frac { 2 \pi } { | \omega | } - \lambda \bigg ) l .$ . Therefore,

$$
\bigl ( [ - 1 , 1 ] \setminus I _ { \lambda , \mu , \tau } ( \omega ) \bigr ) \leq \sum _ { l = 1 } ^ { \infty } \sum _ { | k | > N _ { l , \lambda } } \frac { 2 \lambda } { l ^ { \mu } | k | ^ { \tau } } \leq 4 ^ { n } \lambda \sum _ { l = 1 } ^ { \infty } \frac { 1 } { l ^ { \mu } } \sum _ { m > N _ { l , \lambda } } \frac { 1 } { m ^ { \tau - n + 1 } } ,
$$

where $N _ { l , \lambda } = \left( \frac { 2 \pi } { | \omega | } - \lambda \right) l$ which is positive for positive $l$ . We will use the following estimate which is easy to prove:

$$
\sum _ { m > N } \frac { 1 } { m ^ { \tau - n + 1 } } \leq \left\{ \begin{array} { l l } { c _ { \tau - n + 1 } , } & { 0 < N \leq 1 , } \\ { \displaystyle \frac { 1 } { ( \tau - n ) ( N - 1 ) ^ { \tau - n } } , } & { N > 1 . } \end{array} \right.
$$

Assume $l _ { \lambda }$ is the integer such that $N _ { l _ { \lambda } , \lambda } \leq 1$ and $N _ { l _ { \lambda } + 1 , \lambda } > 1$ . Then (4.7) is verified with

$$
\widetilde { c } = 4 ^ { n } \left( c _ { \tau - n + 1 } \sum _ { l = 1 } ^ { l _ { \lambda } } \frac { 1 } { l ^ { \mu } } + \frac { 1 } { \tau - n } \sum _ { l = l _ { \lambda } + 1 } ^ { \infty } \frac { 1 } { l ^ { \mu } \left( \left( \displaystyle \frac { 2 \pi } { | \omega | } - \lambda \right) l - 1 \right) ^ { \tau - n } } \right)
$$

which is finite because the conditions $\mu + \tau > n + 1$ and $0 < \lambda < \frac { 2 \pi } { | \omega | }$ guarantee the convergence of the infinite summation in (4.1). If $l _ { \lambda } = 0$ , then we take $\sum _ { l = 1 } ^ { l _ { \lambda } } \frac { 1 } { l _ { \mu } } = 0$ and hence the first term in the bracket of Equation (4.10) disappears in this case. Note that here the number $\widetilde { c }$ depends also on $\lambda$ , but this dependence is not fatal essentially because the only harmful case is when $\lambda$ is close to $\frac { \hat { 2 } \pi } { | \omega | }$ However, this case is not of interest and may always be avoided. For example, we simply assume $0 < \lambda \leq \frac { \pi } { | \omega | }$ in the lemma. The proof of Lemma 4.7 is completed. -

Therefore, to guarantee the positiveness of the Lebesgue measure of the set $I _ { \lambda , \mu , \tau } ( \omega )$ , it is not necessary to assume $\mu > 1$ . One may require $\mu$ to only satisfy $\mu \geq - 1$ . In the case $- 1 \leq \mu \leq 1$ , however, one has to additionally require $\mu + \tau > n + 1$ , which automatically implies that $\tau > n$ . One may also consider how big the set $I _ { \lambda , \mu , \tau } ( \omega )$ is in other unit intervals with integer endpoints, but we do not go further in this direction.

Remark 4.8. It remains to study the set $I _ { \lambda , \mu , \tau } ( \omega )$ in other cases: $\mu < - 1$ or $\tau \leq n$ or $\mu + \tau \leq n + 1$ . I believe the Lebesgue measure of the set is zero in each of these cases. It is also an interesting problem to calculate the Hausdorff dimensions of the set $I _ { \lambda , \mu , \tau } ( \omega )$ in all of these cases. The cases when $- 1 \leq \mu \leq 1$ and $\nu = n - \mu + 1$ and when $\mu > 1$ and $\tau = n$ should be particularly interesting. In all other cases, I intend to believe the set is empty. Note that a special case when $n = 1 , \mu = 0$ and $\tau = n - \mu + 1 = 2$ with $\omega = 2 \pi$ just corresponds to the classical diophantine problem on approximating an irrational number by rational ones.

To any nonresonant frequency $\omega$ in $\mathbf { R } ^ { n }$ , we have associated a 3-parameter family of sets $I _ { \lambda , \mu , \tau } ( \omega )$ on the real line. The set $I _ { \lambda , \mu , \tau } ( \omega )$ has positive Lebesgue measure and hence is nonempty if $\mu \geq - 1$ , $\tau > n$ , $\mu + \tau > n + 1$ and $\lambda > 0$ suitably small (in the case when $\mu > 1$ and $\tau > n$ , $I _ { \lambda , \mu , \tau } ( \omega )$ has positive Lebesgue measure for any $\lambda > 0$ ). But to guarantee an invariant torus of the frequency $\scriptstyle t \omega$ for symplectic algorithms with the step size $t$ , it seems that the only way is to require $\scriptstyle t \omega$ satisfy a diophantine condition of the type (1.1) (J. Mather showed in $[ \mathrm { M a t 8 8 } ] \cdot$ ) that for any exact area-preserving twist mapping, an invariant circle with any Liouville frequency can be destroyed by arbitrarily small perturbations in $C ^ { \infty }$ -topology). This is the case when one requires both $\omega$ be a diophantine frequency and $t$ be a diophantine step size with respect to the $\omega$ , as the following lemma shows.

Lemma 4.9. Let $\gamma > 0$ and $0 < \lambda \leq 1$ . Then for any $\omega \in \Omega _ { \gamma } ( \tau _ { 1 } ) ^ { 6 }$ and any $t \in$ $[ - 1 , 1 ] \cap I _ { \lambda , \mu , \tau _ { 2 } } ( \omega )$ , we have

$$
\begin{array} { r } { \left| e ^ { i \left. k , t \omega \right. } - 1 \right| \geq \frac { | t | \widetilde { \gamma } } { | k | ^ { \mu + \tau _ { 1 } + \tau _ { 2 } } } , \quad 0 \neq k \in \mathbf { Z } ^ { n } , } \end{array}
$$

where

$$
\widetilde { \gamma } = \frac { 2 \lambda \gamma } { \pi \Big ( 1 + \frac { 1 } { 2 \pi } | \omega | \Big ) ^ { \mu } } .
$$

Proof. It is easy to prove that for $k \in \mathbf { Z } ^ { n }$ , $k \neq 0$ , there exists $l \in \mathbf { Z }$ such that

$$
\bigl | e ^ { i \langle k , t \omega \rangle } - 1 \bigr | \geq \frac { 2 } { \pi } \bigl | \langle k , t \omega \rangle + 2 \pi l \bigr | .
$$

We have two cases:

$1 ^ { \circ }$ $l = 0$ . Since $\omega \in \Omega _ { \gamma } ( \tau _ { 1 } )$ ,

$$
\displaystyle \lvert e ^ { i \langle k , t \omega \rangle } - 1 \rvert \geq \frac { 2 } { \pi } \bigl \lvert \langle k , t \omega \rangle \bigr \rvert \geq \frac { 2 \lvert t \rvert \gamma } { \pi \lvert k \rvert ^ { \tau _ { 1 } } } ;
$$

$$
| \langle k , \omega \rangle | \geq \frac { \gamma } { | k | ^ { \tau } } , \quad 0 \neq k \in \mathbf { Z } ^ { n } .
$$

$2 ^ { \circ }$ $l \neq 0$ . Since $t \in I _ { \lambda , \mu , \tau _ { 2 } } ( \omega )$ and $\omega \in \Omega _ { \gamma } ( \tau _ { 1 } )$ ,

$$
\begin{array} { r l } & { \left| e ^ { i \langle k , t \omega \rangle } - 1 \right| \geq \displaystyle \frac { 2 } { \pi } \left| \left. k , \Big ( t + \frac { 2 \pi l } { \langle k , \omega \rangle } \Big ) \omega \right. \right| = \displaystyle \frac { 2 } { \pi } \Big | t + \frac { 2 \pi l } { \langle k , \omega \rangle } \Big | \big | \langle k , \omega \rangle \Big | } \\ & { \quad \quad \geq \displaystyle \frac { 2 } { \pi } \cdot \frac { \lambda \gamma } { l ^ { \mu } | k | ^ { \tau _ { 1 } + \tau _ { 2 } } } . } \end{array}
$$

But

$$
\begin{array} { r l r } {  { | 2 \pi l | \le | \langle k , t \omega \rangle + 2 \pi l | + | \langle k , t \omega \rangle | \le \frac { \pi } { 2 } \big | e ^ { i \langle k , t \omega \rangle } - 1 \big | + | t | | \langle k , \omega \rangle | } } \\ & { } & { \le \pi + | t | | \omega | | k | , } \end{array}
$$

therefore,

$$
\big | e ^ { i \langle k , t \omega \rangle } - 1 \big | \geq \frac { 2 \lambda \gamma } { \pi \Big ( \frac { 1 } { 2 } + \frac { | t | } { 2 \pi } | \omega | \Big ) ^ { \mu } | k | ^ { \mu + \tau _ { 1 } + \tau _ { 2 } } } .
$$

Combining the two cases, (4.11) is verified and hence Lemma 2.4 is proved.

From the above lemmas and the fact that meas $\left( { \bf R } ^ { n } \backslash \bigcup _ { \gamma > 0 } \Omega _ { \gamma } ( \tau ) \right) = 0$ for $\tau >$ $n - 1$ , we conclude that for almost all $\boldsymbol \omega \in { \mathbf { R } } ^ { n }$ and almost all $t \in [ - 1 , 1 ] ,$ $\scriptstyle t \omega$ satisfies a diophantine condition of the mapping type (2.5). As the step size of a difference scheme, however, $t$ may fall into an arbitrarily small neighbourhood of the origin. The next lemma shows that for a nonresonant frequency $\boldsymbol { \omega } \in \mathbf { R } ^ { n }$ and for $\mu \geq - 1$ , $\tau > n + 1$ , $\mu + \tau > n + 1$ and $0 < \lambda < \frac { 2 \pi } { | \omega | }$ , the set $I _ { \lambda , \mu , \tau } ( \omega )$ has large measure near the origin of the real line.

Lemma 4.10. Let $\omega$ be a nonresonant frequency of $\mathbf { R } ^ { n }$ . Let $\lambda > 0 , \mu \geq - 1 , \tau > n$ and $\mu + \tau > n + 1$ . For any $\delta > 0$ , let

$$
J _ { \lambda , \mu , \tau } ^ { \delta } ( \omega ) = ( - \delta , \delta ) \setminus I _ { \lambda , \mu , \tau } ( \omega ) .
$$

If $\lambda + \delta < \frac { 2 \pi } { | \omega | }$ , then，

$$
\begin{array} { r } { \operatorname* { m e a s } J _ { \lambda , \mu , \tau } ^ { \delta } ( \omega ) \leq d \delta ^ { \tau - n } , } \end{array}
$$

where

$$
d = \frac { 4 ^ { n } \lambda } { \tau - n } \sum _ { l = 1 } ^ { \infty } \frac { 1 } { l ^ { \mu } \left( \left( \frac { 2 \pi } { | \omega | } - \lambda \right) l - \delta \right) ^ { \tau - n } } < \infty .
$$

Consequently, if in addition $\tau > n + 1$ , then

$$
\operatorname* { l i m } _ { \delta  0 ^ { + } } \frac { \operatorname* { m e a s } \big ( \mathrm { I } _ { \lambda , \mu , \tau } ( \omega ) \cap ( - \delta , \delta ) \big ) } { \operatorname* { m e a s } ( - \delta , \delta ) } = 1 .
$$

Proof. Let $t \in J _ { \lambda , \mu , \tau } ^ { \delta }$ . By definition, we have

$$
- \delta - \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } \leq \frac { 2 \pi l } { \langle k , \omega \rangle } \leq \delta + \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } }
$$

for some $k \in \mathbf { Z } ^ { n }$ and $0 < l \in \mathbf { Z }$ . Fix $l \in \mathbf { Z } , l \neq 0$ , denoted by $\mathcal { K } _ { l } ^ { \delta }$ the set of $k \in \mathbf { Z } ^ { n }$ satisfying (4.16). If $k \in \mathcal { K } _ { l } ^ { \delta }$ , then

$$
\frac { 2 \pi l } { \delta + \frac { \lambda } { l ^ { \mu } | k | } } \leq \frac { 2 \pi l } { \delta + \frac { \lambda } { l ^ { \mu } | k | ^ { \tau } } } \leq | \langle k , \omega \rangle | \leq | k | | \omega | ,
$$

which implies that

$$
| k | > \left( \frac { \displaystyle \frac { 2 \pi } { | \omega | } - \lambda } { \delta } \right) l \doteq N _ { l } ^ { \delta }
$$

since $\mu \geq - 1$ . This shows that ${ \cal K } _ { l } ^ { \delta } \subset \left\{ k \in { \bf Z } ^ { n } : | k | > N _ { l } ^ { \delta } \right\}$ and therefore,

$$
\mathrm { m e a s } J _ { \lambda , \mu , \tau } ^ { \delta } ( \omega ) \leq \sum _ { l = 1 } ^ { \infty } \sum _ { \stackrel { k \in \mathbb { Z } ^ { n } } { | k | > N _ { l } ^ { \delta } } } \frac { 2 \lambda } { l ^ { \mu } | k | ^ { \tau } } \leq 4 ^ { n } \lambda \sum _ { l = 1 } ^ { \infty } \frac { 1 } { l ^ { \mu } } \sum _ { m > N _ { l } ^ { \delta } } \frac { 1 } { m ^ { \tau - n + 1 } } .
$$

Because $0 < \delta + \lambda < \frac { 2 \pi } { | \omega | }$ we have $N _ { l } ^ { \delta } > 1$ . (4.13) follows from (4.9) with the constant $d$ defined by (4.14), which is finite because $\tau > n$ and $\mu + \tau - n > 1$ . (4.15) is true if, in addition, $\tau > n + 1$ .

# 13.4.3 Invariant Tori and Further Remarks

Now, we summarize the main result of this section as follows.

Theorem 4.11. Given an analytic, nondegenerate and integrable Hamiltonian system of n degrees of freedom, and given a frequency $\omega$ , in the domain of the frequencies of the system, which satisfies the diophantine condition of the form

$$
| \langle k , \omega \rangle | \geq { \frac { \gamma } { | k | ^ { \tau } } } , \quad 0 \neq k = ( k _ { 1 } , \cdot \cdot \cdot , k _ { n } ) \in \mathbf { Z } ^ { n }
$$

for some $\gamma > 0$ and $\tau > 0$ , there exists a Cantor set $I ( \omega )$ of $\mathbf { R }$ , for any symplectic algorithm applied to the system, there exists a positive number $\delta _ { 0 }$ such that if the step size t of the algorithm falls into the set $\left( - \delta _ { 0 } , \delta _ { 0 } \right) \cap I ( \omega )$ , then the algorithm, if applied to the integrable system, has an invariant torus of frequency $\boldsymbol { t \omega }$ . The invariant torus of the algorithm approximates the invariant torus of the system in the sense of Hausdorff with the order equals to the order of accuracy of the algorithm. The Cantor set $I ( \omega )$ has density one at the origin in the sense that

$$
\operatorname* { l i m } _ { \delta  0 ^ { + } } \frac { m \Big ( ( - \delta , \delta ) \cap I ( \omega ) \Big ) } { m ( - \delta , \delta ) } = 1 .
$$

Proof. For the given $\omega$ , we define $I ( \omega ) = I _ { \lambda , \mu , \tilde { \tau } } ( \omega )$ for some $\lambda > 0 , \mu > 1$ and $\widetilde { \tau } > n + 1$ . By Lemma 3.7, we have for any $t \in [ - 1 , 1 ] \cap I ( \omega )$ ,

$$
\left| e ^ { i \left. k , t \omega \right. } - 1 \right| \geq \frac { | t | \widetilde { \gamma } } { | k | ^ { \mu + \tau + \widetilde { \tau } } } , \quad 0 \neq k \in \mathbf { Z } ^ { n }
$$

with $\widetilde { \gamma }$ given by (4.12). The analytic version of Theorem 2.4 may be applied and there-"fore, for a symplectic algorithm applied to the given system7, we can find a positive number $\delta _ { 0 }$ , which depends on the numbers $n , \gamma , \tau , \lambda , \mu , \tilde { \tau }$ and $| \omega |$ and on the non-"degeneracy and the analyticity of the system and, of course, also on the algorithm, such that the algorithm has an invariant torus of the frequency $\boldsymbol { t \omega }$ with the required approximating property to the corresponding invariant torus of the system if the step size $t$ falls into the set $[ - \delta _ { 0 } , \delta _ { 0 } ] \cap I ( \omega )$ . It follows from Lemma 3.8 that the set $I ( \omega )$ has density one at the origin because we have chosen $\mu > 1$ and $\widetilde { \tau } > n + 1$ . $\blacktriangle$

Remark 4.12. In practical computations, one would like to choose big step sizes. It is interesting to look at how the $\delta _ { 0 }$ in Theorem 4.11 depends on the nonresonance property of the frequency $\omega$ and how the $\delta _ { 0 }$ relates to the size of the diophantine set $I ( \omega )$ of step sizes. It is known that the parameters $\gamma$ and $\nu$ describe the nonresonance property of the frequency $\omega$ and the parameters $\lambda , \mu$ and $\widetilde \nu$ determine the size of the set $I ( \omega )$ . Among them, the most interesting are $\gamma$ and $\lambda$ because we may fix all others in advance without loss of generality. For a given $\omega$ , we define $\gamma$ to be the biggest one such that (4.17) holds for a fixed $\tau > n - 1$ . It is easy to see, from Lemma 4.9 and Theorem 2.4, that $\delta _ { 0 }$ may be chosen to be proportional to $( \gamma \lambda ) ^ { \frac { 2 } { s } }$ , where $s$ is the order of accuracy of the algorithm considered in Theorem 4.11. Note that the more nonresonant the $\omega$ is, the bigger $\gamma$ will be and therefore the bigger $\delta _ { 0 }$ is admitted. On the other hand, for a given $\omega$ , the bigger step size is taken, the bigger $\lambda$ has to be chosen and in this case, the set $I ( \omega )$ turns out to be smaller. But anyway, the set $I ( \omega )$ is of density one at the origin. Consequently, to simulate an invariant torus, one has much more possibilities to select available small step sizes than to select available big ones.

Remark 4.13. It is interesting to make some comparisons between Theorem 3.4 and Theorem 4.11. Theorem 3.4 shows that a symplectic algorithm applied to an analytic nondegenerate integrable Hamiltonian system has so many invariant tori that the tori form a set of positive Lebesgue measures in the phase space if the step size of the algorithm is sufficiently small and fixed in an arbitrary way. No additional nonresonance or diophantine condition is imposed on the step size. But the set of frequencies of the invariant tori depends on the step size and, therefore, changes in general as the step size changes. It is a fact that the measure of the set of frequencies of the invariant tori becomes larger and larger as the step size gets smaller and smaller. These sets, however, may not intersect at all for step sizes taken over any interval near the origin. Therefore, the invariant tori of any frequencies may not be guaranteed for any symplectic algorithm with step size randomly taken in any neighbourhood of the origin. Theorem

4.11 shows that an invariant torus with any fixed diophantine frequency of an analytic nondegenerate integrable Hamiltonian system can always be simulated very well by symplectic algorithms for any step size in a Cantor set of positive Lebesgue measure near the origin. The following theorem shows that one can simulate simultaneously any finitely many invariant tori of given diophantine frequencies by symplectic algorithms with a sufficiently big probability to select available step sizes. The step sizes, of course, also have to be restricted to a Cantor set.

Theorem 4.14. Given an analytic, nondegenerate and integrable Hamiltonian system of n degrees of freedom. Given $N$ diophantine frequencies $\omega ^ { j }$ $( j = 1 , 2 , \cdots , N )$ , in the domain of the frequencies of the system, there exists a Cantor set $I$ of $\mathbf { R }$ , depending on the $N$ frequencies, such that for any symplectic algorithm applied to the system, there exists a positive number $\delta _ { 0 }$ such that if the step size $t$ of the algorithm falls into the set $\left( - \delta _ { 0 } , \delta _ { 0 } \right) \cap I$ , then the algorithm has $N$ invariant tori of the frequencies $\tau \omega ^ { j }$ $\mathbf { \Phi } _ { j } = 1 , 2 , \cdots , N )$ when it applies to the integrable system. These invariant tori approximate the corresponding ones of the system in the sense of Hausdorff with the order equal to the order of accuracy of the algorithm. The Cantor set $I$ has density one at the origin.

Proof. The proof of Theorem 4.14 follows from Theorem 4.11 and

Lemma 4.15. For any integer $N \geq 1$ , any $\omega ^ { j } \in \Omega _ { \gamma } ( \tau ) ( j = 1 , 2 , \cdots , N )$ and any $\delta > 0$ , put $\mathbf { A } ^ { N } = ( \omega ^ { 1 } , \omega ^ { 2 } , \cdot \cdot \cdot , \omega ^ { N } )$ and

$$
I _ { \lambda , \mu , \tilde { \tau } } ^ { N } ( \mathbf { A } ^ { N } ) = \bigcap _ { j = 1 } ^ { N } I _ { \lambda , \mu , \tilde { \tau } } ( \omega ^ { j } ) , \quad J _ { \lambda , \mu , \tilde { \tau } } ^ { \delta } ( \mathbf { A } ^ { N } ) = ( - \delta , \delta ) \setminus I _ { \lambda , \mu , \tilde { \tau } } ^ { N } ( \mathbf { A } ^ { N } )
$$

with given $\lambda > 0$ $\operatorname { ) } , \mu \geq - 1 , \widetilde { \tau } > n + 1$ and $\mu + \widetilde { \tau } > n + 1 .$ . Then we have

$$
\mathrm { m e a s } J _ { \lambda , \mu , \tilde { \tau } } ^ { \delta } ( { \mathbf { A } } ^ { N } ) \leq N d \delta ^ { \tilde { \tau } - n }
$$

if $\lambda + \delta < \frac { 2 \pi } { | \mathbf { A } ^ { N } | }$ , where $\vert { \bf A } ^ { N } \vert = \operatorname* { m a x } _ { 1 \leq j \leq N } \vert \omega ^ { j } \vert$ and $d$ is defined by (4.14) where $\tau$ is replaced by $\widetilde { \tau }$ and $| \omega |$ replaced by $| \mathbf { A } ^ { N } |$ . Consequently, the set $I _ { \lambda , \mu , \widetilde { \tau } } ^ { N } ( { \bf A } ^ { N } )$ has density one at the origin. Moreover, for any $t \in [ - 1 , 1 ] \cap I _ { \lambda , \mu , \tilde { \tau } } ^ { N } ( \mathbf { A } ^ { N } ) ;$ ", we have

$$
\left| e ^ { i \langle k , t \omega ^ { j } \rangle } - 1 \right| \geq \frac { | t | \widetilde { \gamma } } { | k | ^ { \mu + \tau + \widetilde { \tau } } } , \quad 0 \neq k \in \mathbf { Z } ^ { n } , \quad j = 1 , 2 , \cdots , N
$$

with $\widetilde { \gamma }$ given by (4.12) where $| \omega |$ replaced by $| \mathbf { A } ^ { N } |$ .

Proof. Lemma 4.15 is a natural corollary of Lemmas 4.9 and 4.10.

Remark 4.16. There have been some works about exponential stability of symplectic algorithms in simulating invariant tori with given diophantine frequencies of integrable or nearly integrable systems (Benettin and Giorgilli (1994)[BG94] , Hairer and Lubich in $1 9 9 7 ^ { [ \mathrm { { H L 9 7 } ] } }$ and Stoffer in $1 9 9 8 ^ { [ \mathrm { { S t o 9 8 b } ] } }$ ). The result, for example, of Hairer and

Lubich[HL97] shows that during a very long interval of iteration steps (exponentially long in $1 / t$ ), the numerical orbits of a symplectic algorithm approximate the exact orbits of some perturbed Hamiltonian system8 with a very small error (exponentially small in $- 1 / t$ ) if the starting values of the numerical orbits and the exact ones are the same and are taken on the invariant torus of the perturbed system (the invariant torus is guaranteed by the KAM theorem)[HL97] (Corollary 7) or taken in a neighbourhood of the invariant torus with the radius of order $t ^ { 2 n + 2 }$ (this is easily derived from Hairer and Lubich (1997, Corollary 8)), here $n$ is the degrees of freedom of the Hamiltonian system and $t$ is the step size of the algorithm which is assumed to be sufficiently small. Theorems 4.11 and 4.14 show that one may generate quasi-periodic (therefore, perpetually stable) numerical orbits using a symplectic algorithm which approximate exact quasi-periodic orbit of an analytic nondegenerate integrable Hamiltonian system if the step sizes of the algorithm fall into a Cantor set of large density near the origin. As the step size in this Cantor set gets smaller and smaller, more and more stable numerical orbits appear. For such a stability consideration, Theorem 3.4 shows much more: the perpetually stable numerical orbits take up a large set of the phase space so that the Lebesgue measure of the set approaches the Lebesgure measure of the phase space as the step size approaches zero. Due to the well-known topological confinement of the phase plane between invariant closed curves, this implies the perpetual stability of symplectic algorithms applied to one degree of freedom systems for any initial values if the step size is small.

Remark 4.17. Generally speaking, it is difficult to check the diophantine condition for a step size with respect to a nonresonant frequency vector. An obvious fact is fortunately, however, that step sizes $N ^ { - 1 }$ , with $N$ being integers, satisfy the diophantine condition (4.4) with respect to frequency vectors satisfying diophantine condition (2.8). This fact was checked by Dujardin and Faou in $2 0 0 7 ^ { \mathrm { [ D F 0 7 ] } }$ for the $1 + 1$ dimensional linear Schrodinger equation with a periodic potential, where a spatially ¨ periodic solution can be stably simulated using nonresonant step size $t = \frac { 1 } { 5 } = 0 . { \dot { 2 } }$ , but is quickly violated using resonant step size $t = \frac { 2 \pi } { 6 ^ { 2 } - 2 ^ { 2 } } \sim 0 . 1 9 6$ .

# Bibliography

[AA89] V. I. Arnold and A. Avez: Ergodic Problems of Classical Mechanics. Addison-Wesley and Benjamin Cummings, New York, (1989).   
[Arn63] V.I. Arnold: Proof of A. N. kolmogorov’s theorem on the preservation of quasiperiodic motions under small perturbations of the Hamiltonian,. Russian Math. Surveys, 18(5):9–36, (1963).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin, Heidelberg, Second edition, (1989).   
[BB79] K. Burrage and J.C. Butcher: Stability criteria for implicit Runge–Kutta methods. SIAM J. Numer. Anal., 16:46–57, (1979).   
[Bey87] W. J. Beyn: On invariant closed curves for one-step methods. Numer. Math., 51:103– 122, (1987).   
[BG94] G. Benettin and A. Giorgilli: On the Hamiltonian interpolation of near to the identity symplectic mappings with application to symplectic integration algorithms. J. Stat. Phys., 74:1117–1143, (1994).   
[But75] J. C. Buther: A stability property of implicity Runge–Kutta methods. BIT, 15(3):358– 361, (1975).   
[CD09] F. Castella and G. Dujardin: Propagation of gevrey regularity over long times for the fully discrete Lie-Trotter splitting scheme applied to the linear Schrodinger equation. ¨ ESIAM: Mathmatical Modelling and Numericalo Analysis, 43(4):651–676, (2009).   
[CFM06] P. Chartier, E. Faou, and A. Murua: An algebraic approach to invariant preserving integrators; the case of quadratic and Hamiltonian invariants. Numer. Math., 103(4):575– 590, (2006).   
[CG82] L. Chierchia and G. Gallavotti: Smooth prime integralsfor quasi-integrable Hamiltonian systems. IL Nuovo Cimento, 67, 277– 295, (19820.   
[CS90] P.J. Channell and C. Scovel: Symplectic integration of Hamiltonian systems. Nonlinearity, 3:231–259, (1990).   
[CS94] C. G. Cheng and Y. S. Sun: Existence of KAM tori in degenerate Hamiltonian systems. J. Differential Equations, 114(1):288–335, (1994).   
[Dah63] G. Dahlquist: A special stability problem for linear multistep methods. BIT, 3(1):27– 43, (1963).   
[Dah75] G. Dahlquist: Error analysis for a class of methods for stiff nonlinear initial value problems. In G.A. Watson, editor, Lecture notes in Mathematics, Vol. 506, Numerical Analysis, Dundee, pages 60–74. Springer, Berlin, (1975).   
[Dah78] G. Dahlquist: G-stability is equivalent to A-stability. BIT, 18:384–401, (1978).   
[DF07] G. Dujardin and E. Faou: Normal form and long time analysis of splitting schemes for the linear Schro¨dinger equation with small potential. Numer. Math., 108(2):223–262, (2007).   
[Ehl69] B. L. Ehle: On Pade approximations to the exponential function and A-stable methods ´ for the numerical solution of initial value problems. Technical Report, Research Rep. No. CSRR 2010, University of Waterloo Dept. of Applied Analysis and Computer Science, (1969). editor, Applied and industrial Mathmatics, pages 17–35. Kluwer, The Netherlands, (1991).   
[FQ03] K. Feng and M. Q. Qin: Symplectic Algorithms for Hamiltonian Systems. Zhejiang Science and Technology Publishing House,Hangzhou, in Chinese, First edition, (2003).   
[Gar96] B. M. Garay: On structural stability of ordinary differential equations with respect to discretization methods. Numer. Math., 72:449–479, (1996).   
[Hai94] E. Hairer: Backward analysis of numerical integrators and symplectic methods. Annals of Numer. Math., 1:107–132, (1994).   
[HL97] E. Hairer and Ch. Lubich: The life-span of backward error analysis for numerical integrators. Numer. Math., 76:441–462, (1997).   
[HLW02] E. Hairer, Ch. Lubich, and G. Wanner: Geometric Numerical Integration. Number 31 in Springer Series in Computational Mathematics. Springer-Verlag, Berlin, (2002).   
[HNW93] E. Hairer, S. P. Nørsett, and G. Wanner: Solving Ordinary Differential Equations I, Nonstiff Problems. Springer-Verlag, Berlin, Second revised edition, (1993).   
[HS81] W. H. Hundsdorfer and M. N. Spijker: A note on B-stability of Runge–Kutta methods. Numer. Math., 36:319–331, (1981).   
[HS94] A. R. Humphries and A. M. Stuart: Runge–Kutta methods for dissipative and gradient dynamical systems. SIAM J. Numer. Anal., 31(5):1452–1485, (1994).   
[Kol54b] A. N. Kolmogorov: On conservation of conditionally periodic motions under small perturbations of the Hamiltonian. Dokl. Akad. Nauk SSSR,, 98:527–530, (1954).   
[Laz74] V. F. Lazutkin: On Moser’s theorem on invariant curves. In Voprsoy raspr. seism. voln. vyp. Nauka Leningrad, 14:105–120, (1974).   
[Li99] M. C. Li: Structural stability for Euler method. SIAM J. Math. Anal., 30(4):747–755, (1999).   
[LR05] B. Leimkuhler and S. Reich: Simulating Hamiltonian Dynamics. Cambridge University Press, Cambridge, First edition, (2005).   
[Mat88] J. Mather: Destruction of invariant circles. Ergod. Theory & Dynam. Sys, 8:199–214, (1988).   
[Mos62] J. Moser: On invariant curves of area-preserving mappings of an annulus. Nachr. Akad. Wiss. Gottingen, II. Math.-Phys., pages 1–20, (1962).   
[Nei82] A. I. Neishtadt: Estimates in the Kolmogorov theorem on conservation of conditionally periodic motions. J. Appl. Math. Mech., 45(6):766–772, (1982).   
[Pos82] J. P ¨ oschel: Integrability of Hamiltonian systems on Cantor sets. ¨ Comm. Pure and Appl. Math., 35:653–695, (1982).   
[Rus81] H. R ¨ ussmann: On the existence of invariant curves of twist mappings of an anulus. ¨ In J. Palis, editor, Geometric Dynamics, Lecture Notes in Math. 1007, pages 677–718. Springer-Verlag, Berlin, (1981).   
[Rus90] H. R ¨ ussmann: On twist Hamiltonian. In ¨ in Colloque Internationa: Mecanique c ´ eleste ´ et systemes hamiltoniens \` . Marseille, (1990).   
[SH96] A.M. Stuart and A.R. Humphries: Dynamical Systems and Numerical Analysis. Cambridge University Press, Cambridge, Second edition, (1996).   
[Sha91] Z. J. Shang: On the KAM theorem of symplectic algorithms for Hamiltonian systems,. Ph.D. thesis (in Chinese), Computing Center, Academia Sinica, (1991).   
[Sha99] Z. Shang: KAM theorem of symplectic algorithms for Hamiltonian systems. Numer. Math., 83:477–496, (1999).   
[Sha00a] Z. J. Shang: A note on the KAM theorem for symplectic mappings. J. Dynam. Differential eqns., 12(2):357–383, (2000).   
[Sha00b] Z. J. Shang: Resonant and diophantine step sizes in computing invariant tori of Hamiltonian systems. Nonlinearity, 13:299–308, (2000).   
[SSC94] J. M. Sanz-Serna and M. P. Calvo: Numerical Hamiltonian Problems. AMMC 7. Chapman & Hall, London, (1994).   
[Sto98a] D. Stoffer: On the qualitative behavior of symplectic integrator. II: Integrable systems. J. of Math. Anal. and Applic., 217:501–520, (1998).   
[Sto98b] D. Stoffer: On the qualitative behaviour of symplectic integrators. III: Perturbed integrable systems. J. of Math. Anal. and Appl., 217:521–545, (1998).   
[Sva81] N. V. Svanidze: Small perturbations of an integrable dynamical system with an integral invariant. In Proceedings of the Steklov Institute of Mathematics, Issue 2, pages 127–151, (1981).   
[Wid76] O. B. Widlund: A note on unconditionally stable linear multistep methods. BIT, 7(1):65–70, (1976).

# Chapter 14. Lee-Variational Integrator

In the 1980s, Lee proposed an energy-preserving discrete mechanics with variable time steps by taking time (discrete) as a dynamical variable [Lee82,Lee87] . On the other hand, motivated by the symplectic property of Lagrangian mechanics, a version of discrete Lagrangian mechanics has been developed and variational integrators that preserve discrete symplectic 2-form have been obtained [MPS98,MV91,Ves88,Ves91a,WM97] , but variational integrators obtained in this way fix the time steps and consequently, they are not energy-preserving in general.

Obviously, energy-preserving discrete mechanics and variational integrators are more preferable, since solutions of the Euler–Lagrange equations of conservative continuous systems are not only symplectic but also energy-preserving. To attain this goal, we should study some discrete mechanics with discrete energy conservation and symplectic variational integrators. Recently, Kane, Marsden, and Ortiz have employed appropriate time steps to conserve a defined energy and developed what they called symplectic energy-momentum-preserving variational integrators in [KMO99] . Although their approach is more or less related to Lee’s discrete mechanics, the discrete energypreserving condition is not derived by the variational principle.

# 14.1 Total Variation in Lagrangian Formalism

The purpose of this section is to generalize or improve the above mentioned approaches as well as to explore the relations among discrete total variation, Lee’s discrete mechanics, and Kane–Marsden–Ortiz integrators. We will present a discrete total variation calculus with variable time steps and a discrete mechanics that is discretely symplectic, energy-preserving and has the correct continuous limit. In fact, this discrete variation calculus and mechanics is a generalization of Lee’s discrete mechanics in symplectic-preserving sense and can derive directly the variational symplecticenergy-momentum integrators of Kane, Marsden, and Ortiz.

# 14.1.1 Variational Principle in Lagrangian Mechanics

Before beginning this section, we will recall very briefly the ordinary variational principle in Lagrangian mechanics for later use. Suppose $Q$ denotes the extended configuration space with coordinates $( t , q ^ { i } )$ and $Q ^ { ( 1 ) }$ the first prolongation of $Q$ with

coordinates $( t , q ^ { i } , \dot { q } ^ { i } ) ^ { [ \mathrm { O l v } 9 3 ] }$ . Here $t$ denotes time and $q ^ { i } ( i = 1 , 2 , \cdot \cdot \cdot , n )$ denote the positions. Consider a Lagrangian $L \colon Q ^ { ( 1 ) } \to \mathbb { R }$ . The corresponding action functional is defined by

$$
S ( q ^ { i } ( t ) ) = \int _ { a } ^ { b } L ( t , q ^ { i } ( t ) , \dot { q } ^ { i } ) \mathrm { d } t ,
$$

where $q ^ { i } ( t )$ is a $C ^ { 2 }$ curve in $Q$ .

Hamilton’s principle seeks a curve $q ^ { i } ( t )$ denoted by $C _ { a } ^ { b }$ with endpoints $a$ and $b$ , for which the action functional $S$ is stationary under variations of $q ^ { i } ( t )$ with fixed endpoints. Let

$$
V = \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } }
$$

be a vertical vector field on $Q$ , here $q = ( q ^ { 1 } , \cdots , q ^ { n } )$ . By a vertical vector field we mean a vector field on $Q$ which does not involve terms of form $\xi ( t , q ) \frac { \partial } { \partial t }$ , for example, time $t$ does not undergo variation.

Let $F ^ { \varepsilon }$ be the flow of $V$ , i.e., a one-parameter group of transformations on $Q :$ $F ^ { \varepsilon } ( t , q ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } )$ .

$$
\begin{array} { c } { { \tilde { t } ~ = ~ t , } } \\ { { \tilde { q } ^ { i } ~ = ~ g ^ { i } ( \varepsilon , t , q ) , } } \end{array}
$$

where

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , q ) = \phi ^ { i } ( t , q ) : = \delta q ^ { i } ( t ) .
$$

In other words, the deformation (1.3) – (1.4) transforms the curve $q ^ { i } ( t )$ into a family of curves $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ in $Q$ denoted by $C _ { \varepsilon _ { a } } ^ { b }$ which are determined by

$$
\begin{array} { r c l } { { \displaystyle \tilde { t } ~ = ~ t , } } \\ { { \tilde { q } ^ { i } ~ = ~ g ^ { i } ( \varepsilon , t , q ( t ) ) . } } \end{array}
$$

Thus, we obtain a (sufficiently small) set of curves $\mathcal { C } _ { \varepsilon _ { a } } ^ { b }$ around $ { \mathcal { C } } _ { a } ^ { b }$ . Corresponding to athis set of curves there is a set of Lagrangian and action functionals

$$
S ( q ^ { i } ( t ) ) \longrightarrow S ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) = \int _ { a } ^ { b } L ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) \mathrm { d } \tilde { t } .
$$

Now, we can calculate the variation of $S$ at $q ( t )$ as follows:

$$
\begin{array} { l } { \delta S = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) ) } \\ { = \left. \int _ { a } ^ { b } \left[ \left( \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right) \phi ^ { i } \right] \mathrm { d } t + \frac { \partial L } { \partial \dot { q } ^ { i } } \phi ^ { i } \right| _ { a } ^ { b } . } \end{array}
$$

For the fixed endpoints, $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , the requirement of Hamilton’s principle, $\delta S = 0$ , yields the Euler–Lagrange equation for $q ( t )$

$$
{ \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } = 0 .
$$

If we drop the requirement of $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , we can naturally obtain the Lagrangian 1-form on $Q ^ { ( 1 ) }$ from the second term in (1.9):

$$
\theta _ { L } = \frac { \partial L } { \partial \dot { q } ^ { I } } { \bf d } q ^ { i } ,
$$

where $\mathrm { d } q ^ { i }$ are dual to $\frac { \partial } { \partial q ^ { j } } , { \bf d } q ^ { i } \biggl ( \frac { \partial } { \partial q ^ { j } } \biggr ) = \delta _ { j } ^ { i }$ . Furthermore, it can be proved that the solution of (1.10) preserves the Lagrangian 2-form

$$
\omega _ { L } : = \mathrm { d } \theta _ { L } .
$$

On the other hand, introducing the Euler–Lagrange 1-form

$$
E ( q ^ { i } , \dot { q } ^ { i } ) = \left\{ \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right\} \mathrm { d } q ^ { i } ,
$$

the nilpotency of ${ \mathrm { d } }$ leads to

$$
\mathrm { d } E ( q ^ { i } , \dot { q } ^ { i } ) + \frac { \mathrm { d } } { \mathrm { d } t } \omega _ { L } = 0 ,
$$

namely, the necessary and sufficient condition for symplectic structure preserving is that the Euler–Lagrange 1-form is closed[GLW01a,GLWW01,GW03] .

# 14.1.2 Total Variation for Lagrangian Mechanics

Consider a general vector field on $Q$

$$
V = \xi ( t , q ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } } ,
$$

here $q = ( q ^ { 1 } , \cdots , q ^ { n } )$ . Let $F ^ { \varepsilon }$ be the flow of $V$ . The variations of $( t , q ^ { i } ) \in Q$ are described in such a way

$$
( t , q ^ { i } ) \longrightarrow F ^ { \varepsilon } ( t , q ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } ) ,
$$

where

$$
\tilde { t } = f ( \varepsilon , t , q ) , \quad \tilde { q } ^ { i } = g ^ { i } ( \varepsilon , t , q )
$$

with

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } f ( \varepsilon , t , q ) = \xi ( t , q ) : = \delta t , \quad \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , q ) = \phi ^ { i } ( t , q ) : = \delta q ^ { i } .
$$

The dcurves (1.17) transfdenoted by a curve , determi $q ^ { i } ( t )$ $Q$ denoted by $ { \mathcal { C } } _ { a } ^ { b }$ into a set of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ $Q$ $\mathcal { C } _ { \varepsilon _ { \tilde { a } } } ^ { \tilde { b } }$

$$
\tilde { t } = f ( \varepsilon , t , q ( t ) ) , \quad \tilde { q } ^ { i } = g ^ { i } ( \varepsilon , t , q ( t ) ) .
$$

Before calculating the total variation of $S$ , we will introduce the first-order prolongation of $V$ denoted as $\mathrm { p r } ^ { 1 } V$

$$
\mathrm { p r } ^ { 1 } V = \xi ( t , q ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , q ) \frac { \partial } { \partial q ^ { i } } + \alpha ^ { i } ( t , q , \dot { q } ) \frac { \partial } { \partial \dot { q } ^ { i } } ,
$$

here

$$
\alpha ^ { i } ( t , q , \dot { q } ) = D _ { t } \phi ^ { i } ( t , q ) - \dot { q } ^ { i } D _ { t } \xi ( t , q ) ,
$$

where $D _ { t }$ denotes the total derivative with respect to $t$ , for example,

$$
D _ { t } \phi ^ { k } ( t , q ^ { i } ) = \phi _ { t } ^ { k } + \phi _ { q ^ { i } } ^ { k } \dot { q } ^ { i } , \quad \phi _ { t } ^ { k } = \frac { \partial \phi ^ { k } } { \partial t } .
$$

For prolongations of the vector field and the related formulae, refer to $[ \mathrm { O l v 9 3 } ]$

Now, we let us calculate the total variation of $S$ straightforwardly:

$$
\begin{array} { r l } { \delta S = } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } S ( \bar { \theta } ^ { + } ( \varepsilon , \tilde { t } ) ) - \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { \partial _ { \varepsilon } } ^ { \tilde { t } } \Big [ \bar { \epsilon } \big ( \bar { t } , \bar { \varphi } ^ { + } , \tilde { t } \big ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \mathrm { d } \tilde { t } } \\ { = } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { a } ^ { \tilde { t } } L \Big ( \bar { t } , \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \frac { \mathrm { d } \tilde { t } } { \mathrm { d } \tilde { t } } \mathrm { d } t \ \qquad \ \bar { \hat { \varepsilon } } \bar { t } = f ( \varepsilon , t , q ( t ) ) \big ) } \\ { = } & { \int _ { a } ^ { \tilde { y } } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } L \Big ( \bar { t } , \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) , \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \bar { \varphi } ^ { i } ( \varepsilon , \tilde { t } ) \Big ) \mathrm { d } t + \int _ { a } ^ { b } L ( t , q ^ { i } ( t ) , i ^ { * } ( t ) ) D _ { i } \xi \mathrm { d } t } \\ { = } & { \int _ { a } ^ { \tilde { y } } \Big [ \frac { \partial L } { \partial \varepsilon } \varepsilon + \frac { \partial L } { \partial \tilde { t } } \bar { \varphi } ^ { i } + \frac { \partial L } { \partial \tilde { t } ^ { i } } ( D _ { i } \phi ^ { i } - \bar { q } ^ { i } D _ { i } \xi ) \Big ] \mathrm { d } t + \int _ { a } ^ { b } L D _ { i } \xi \mathrm { d } t } \\ { = } &  \int _ { a } ^ { \tilde { y } } \Big [ \Big ( \frac { \partial L } { \partial \tilde { t } } + \frac { \partial L } { \mathrm { d } \varepsilon } \Big ( \frac  \partial L  \end{array}
$$

Here we have made use of (1.18), (1.20), (1.21) and

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } = \frac { \mathrm { d } } { \mathrm { d } t } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \tilde { t } = D _ { t } \xi .
$$

If $\xi ( a , q ( a ) ) = \xi ( b , q ( b ) ) = 0$ and $\phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0$ , the requirement of $\delta S = 0$ yields the equation from $\xi$ , the variation along the base manifold, i.e., the time.

$$
{ \frac { \partial L } { \partial t } } + { \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } - L \right) = 0 ,
$$

and the Euler–Lagrange equation from $\phi ^ { i }$ , the variation along the fiber, i.e., the configuration space,

$$
{ \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } = 0 .
$$

Here $\xi$ and $\phi ^ { i }$ are regarded as independent components of total variation. However, there is another decomposition for the independent components, i.e., the vertical and horizontal variations; see Remark1.2 below.

If $L$ does not depend on $t$ explicitly, i.e., $L$ is conservative, $\frac { \partial L } { \partial t } = 0$ , then (1.23) becomes the energy conservation law

$$
\frac { \mathrm { d } } { \mathrm { d } t } H = 0 , H : = \Bigl ( \frac { \partial L } { \partial \dot { q } ^ { i } } \dot { q } ^ { i } - L \Bigr ) .
$$

By expanding the left-hand side of (1.25), we obtain

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } - L \right) = - \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) { \dot { q } } ^ { i } .
$$

Thus, for a conservative $L$ , energy conservation is a consequence of Euler–Lagrange equation. This agrees with Noether theorem which states that the characteristic of an infinitesimal symmetry of the action functional $S$ is that of a conservation law for the Euler–Lagrange equation. For a conservative $L$ , $\frac { \partial } { \partial t }$ is an infinitesimal symmetry of the action functional $S$ , and its characteristic is $- \dot { q } ^ { i }$ . From Noether theorem, there exits a corresponding conservation law in the characteristic form

$$
- \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) { \dot { q } } ^ { i } = 0 .
$$

If we drop the requirement

$$
\xi ( a , q ( a ) ) = \xi ( b , q ( b ) ) = 0 , \phi ^ { i } ( a , q ( a ) ) = \phi ^ { i } ( b , q ( b ) ) = 0 ,
$$

we can define the extended Lagrangian 1-form on $Q ^ { ( 1 ) }$ from the second term in (1.22)

$$
\vartheta _ { L } : = \left( L - { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \dot { q } } ^ { i } \right) { \mathsf { d } } t + { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } { \mathsf { d } } q ^ { i } .
$$

Suppose $g ^ { i } ( t , v _ { q ^ { i } } )$ is a solution of (1.24) depending on the initial condition $v _ { q ^ { i } } \in Q ^ { ( 1 ) }$ . Restricting $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ to the solution space of (1.24) and using the same method $\mathrm { i n } ^ { \mathrm { [ M P S 9 8 ] } }$ , it can be proved that the extended symplectic 2-form is preserved:

$$
( \mathrm { p r } ^ { 1 } g ^ { i } ) ^ { * } \Omega _ { L } = \Omega _ { L } , \quad \Omega _ { L } : = \mathrm { d } \vartheta _ { L } ,
$$

where $\operatorname { p r } ^ { 1 } g ^ { i } ( s , v _ { q ^ { i } } ) = { \Big ( } s , g ^ { i } ( s , v _ { q ^ { i } } ) , { \frac { \mathrm { d } } { \mathrm { d } s } } g ^ { i } ( s , v _ { q ^ { i } } ) { \Big ) }$ denotes the first-order prolonga-$g ^ { i } ( s , v _ { q ^ { i } } ) ^ { [ \mathrm { O l v } 9 3 ] }$

Remark 1.1. If $\xi$ in (1.15) is independent of $q$ , the deformations in (1.17) are called fiber-preserving. In this case, the domain of definition of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ only depends on the deformations in (1.17). While in the general case, the domain of definition of $\tilde { q } ^ { i } ( \varepsilon , \tilde { t } )$ depends on not only the deformations in (1.17) but also on $q ^ { i } ( t )$ .

Remark 1.2. Using the identity

$$
\frac { \partial L } { \partial t } + \frac { \mathrm { d } } { \mathrm { d } t } \left( \frac { \partial L } { \partial \dot { q } ^ { i } } \dot { q } ^ { i } - L \right) = - \left( \frac { \partial L } { \partial q ^ { i } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } ^ { i } } \right) \dot { q } ^ { i } ,
$$

the Equation (1.22) becomes

$$
\delta S = \int _ { a } ^ { b } \left( { \frac { \partial L } { \partial q ^ { i } } } - { \frac { \mathrm { d } } { \mathrm { d } t } } { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } \right) ( \phi ^ { i } - \xi { \dot { q } } ^ { i } ) \mathrm { d } t + \left[ { \frac { \partial L } { \partial { \dot { q } } ^ { i } } } ( \phi ^ { i } - \xi { \dot { q } } ^ { i } ) \right] { \Big | } _ { a } ^ { b } + ( L \xi ) { \Big | } _ { a } ^ { b } .
$$

According to (1.18), $\phi ^ { i } = \delta q ^ { i }$ should be regarded as the total variation of $q ^ { i } , \delta q ^ { i } =$ $\delta _ { V } q ^ { i } + \delta _ { H } q ^ { i }$ , since the variation of $t$ also induces the variation of $q ^ { i }$ , denoted as $\delta _ { H } q ^ { i }$ , the horizontal variation of $q ^ { i }$ . Substituting $\xi = \delta t$ in (1.18), the horizontal variation of $q ^ { i }$ should be $\delta _ { H } q ^ { i } = \xi \dot { q } ^ { i }$ , and consequently $\phi ^ { i } - \xi \dot { q } ^ { i }$ is interpreted as vertical variation $\delta _ { V } q ^ { i }$ , i.e., the variation of $q ^ { i } ( t )$ at the moment $t$ (for e.g., $\mathrm { s e e } ^ { \left[ \mathrm { C H } 5 3 \right] } ,$ . Therefore, the first two terms in (1.32) come from vertical variation $\delta _ { V } q ^ { i }$ and the last term comes from horizontal variation $\delta t$ . The horizontal variation of $S$ with respect to the horizontal variation $\delta _ { H } q ^ { i } = \xi \dot { q } ^ { i }$ gives rise to the identity (1.31).

# 14.1.3 Discrete Mechanics and Variational Integrators

In this subsection, by calculus of discrete total variations, we will develop a discrete Lagrangian mechanics, which includes the boundary terms in Lee’s discrete mechanics that give rise to the discrete version of symplectic preserving. The discrete variation calculus is mainly analog to Lee’s idea that time (discrete) is regarded as a dynamical variable, i.e., the time steps are variable[Lee82,Lee87] . The vertical part of this discrete variation calculus is similar to the one $\mathrm { i n } ^ { [ \mathrm { K M O 9 9 , M V 9 1 , V e s 8 8 , V e s 9 1 a , W \bar { M } 9 7 } ] }$ . Using this calculus for discrete total variations we naturally derive the Kane–Marsden–Ortiz integrators.

We use $Q \times Q$ to denote the discrete version of the first prolongation for the extended configuration space $Q$ . A point $( t _ { 0 } , q _ { 0 } ; t _ { 1 } , q _ { 1 } ) \in Q \times Q ^ { \ 1 }$ , corresponds to a tangent vector $\frac { q _ { 1 } - q _ { 0 } } { t _ { 1 } - t _ { 0 } }$ . A discrete Lagrangian is defined to be $\mathbb { L } : Q \times Q \to \mathbb { R }$ and the corresponding action as

$$
\mathbb { S } = \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) .
$$

The discrete variational principle in total variation is to extremize $\mathbb { S }$ for variations of both $q _ { k }$ and $t _ { k }$ with fixed end points $( t _ { 0 } , q _ { 0 } )$ and $( t _ { N } , q _ { N } )$ . This discrete variational principle determines a discrete flow $\Phi : Q \times Q \to Q \times Q$ by

$$
\Phi ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) .
$$

Here $( t _ { k + 1 } , q _ { k + 1 } )$ are calculated from the following discrete Euler–Lagrange equation, i.e., the variational integrator, and the discrete energy conservation law (for conservative L)

$$
( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = 0 ,
$$

and

$$
\begin{array} { r l } & { ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + D _ { 3 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) ( t _ { k } - t _ { k - 1 } ) } \\ & { - \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) + \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , t _ { k } , q _ { k } ) = 0 , } \end{array}
$$

for all $k \in \{ 1 , 2 , \cdots , N - 1 \}$ . Here $D _ { i }$ denotes the partial derivative of $\mathbb { L }$ with respect to the $i$ -th argument. The Equation (1.35) is the discrete Euler–Lagrange equation. The Equation (1.36) is the discrete energy conservation law for a conservative $\mathbb { L }$ . The integrator $( 1 . 3 5 ) - ( 1 . 3 6 )$ is the Kane–Marsden–Ortiz integrator.

Using the discrete flow $\Phi$ , the Equations (1.35) and (1.36) become

$$
\begin{array} { r } { ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } \circ \Phi + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } = 0 , } \\ { ( ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L } ) \circ \Phi + D _ { 3 } \mathbb { L } + \mathbb { L } = 0 , } \end{array}
$$

respectively. If $( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L }$ and $( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L }$ are invertible, the Equations (1.37) and (1.38) determine the discrete flow $\Phi$ under the consistency condition

$$
( ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } - \mathbb { L } ) ^ { - 1 } \circ ( D _ { 3 } \mathbb { L } + \mathbb { L } ) = ( ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ) ^ { - 1 } \circ ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } .
$$

Now, we will prove that the discrete flow $\Phi$ preserves a discrete version of the extended Lagrange 2-form $\Omega _ { L }$ . As in continuous case, we will calculate $\mathrm { d } \mathbb { S }$ for variations with variable end points.

$$
\begin{array} { r l } &  \begin{array} { r l } &  \mathrm { d } \mathcal { E } ( \xi , \theta , \eta ^ { * } , \theta , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ { * } , \theta ^ \end{array} \end{array}
$$

$$
\begin{array} { r l } {  { \sum _ { i = 1 } ^ { N - 1 } L ( \{ k _ { i } , q _ { i } , q _ { i } , \} , \phi _ { i \neq 1 } ) ( - \delta \{ k _ { i } \} ) \Big ( \delta + \sum _ { i = 1 } ^ { N } \mathcal { L } \{ ( k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } ) \} \delta \{ k _ { i } \} } } \\ &  + \sum _ { i = 1 } ^ { N - 1 } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i } ) \mathbb { \} ) } \\ & { = \sum _ { i = 1 } ^ { N } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i } ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) ) \delta _ { \emptyset \mathcal { K } } } \\ & { + \sum _ { i = 1 } ^ { N } ( D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i + 1 } \} ) ( \delta + k _ { i + 1 } - \{ k _ { i } \} ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) ) } \\ & { + D _ { i } L ( \{ k _ { i - 1 } , q _ { i - 1 } , t _ { i } , q _ { i } \} ) ( \delta - k _ { i } - \{ k _ { i } \} ) \delta ( k _ { i } - \delta ) ) ( \delta \{ k _ { i } \} } \\ & { + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i - 1 } , q _ { i } \} ) ( \delta - k _ { i } ) \delta _ { \emptyset \mathcal { K } } } \\ & { + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i } \} ) ( \delta - k _ { i } ) \delta _ { \emptyset \mathcal { K } } + D _ { i } \{ ( k _ { i } , q _ { i - 1 } , q _ { i } ) \} \delta _ { \mathcal { K } } } \\ &  + D _ { i } L ( \{ k _ { i } , q _ { i } , t _ { i } \} ) ( \delta - k _ \end{array}
$$

We can see that the last four terms in (1.40) come from the boundary variations. Based on the boundary variations, we can define two 1-forms on $Q \times Q$

$$
\begin{array} { r l } & { \theta _ { \mathbb { L } } ^ { - } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) } \\ & { = ( D _ { 1 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ) \mathrm { d } t _ { k } } \\ & { \quad + D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \theta _ { \mathbb { L } } ^ { + } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) } \\ & { = ( D _ { 3 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) + \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ) \mathrm { d } t _ { k + 1 } } \\ & { \quad + D _ { 4 } \mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } q _ { k + 1 } , } \end{array}
$$

having employed the notations in $\left[ \mathrm { M P S 9 8 } \right]$ . We regard the pair $( \theta _ { \mathbb { L } } ^ { - } , \theta _ { \mathbb { L } } ^ { + } )$ as the discrete version of the extended Lagrange 1-form $\vartheta _ { \mathbb { L } }$ defined in (1.29).

Now, we parameterize the solutions of the discrete variational principle by the initial condition $( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } )$ and restrict $\mathbb { S }$ to that solution space. Then Equation (1.40) becomes

$$
\begin{array} { r l } & { \mathrm { d } \mathbb { S } \big ( t _ { 0 } , q _ { 0 } , \cdot \cdot \cdot , t _ { N } , q _ { N } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \cdot \cdot \cdot , \delta t _ { N } , \delta q _ { N } \big ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \cdot \delta t _ { 1 } , \delta q _ { 1 } \big ) } \\ & { \quad + \theta _ { \mathbb { L } } ^ { + } \big ( t _ { N - 1 } , q _ { N - 1 } , t _ { N } , q _ { N } \big ) \cdot \big ( \delta t _ { N - 1 } , \delta q _ { N - 1 } , \delta t _ { N } , \delta q _ { N } \big ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \cdot \big ( \delta t _ { 0 } , \delta q _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } \big ) } \\ & { \quad + \big ( \Phi ^ { N - 1 } \big ) ^ { * } \theta _ { \mathbb { L } } ^ { + } \big ( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } \big ) \big ( \delta t _ { 0 } , \delta q _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } \big ) . } \end{array}
$$

From (1.43), we obtain

$$
\begin{array} { r } { \mathtt { d } \mathbb { S } = \theta _ { \mathbb { L } } ^ { - } + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

The Equation (1.44) holds for arbitrary $N > 1$ . By taking $N = 2$ , we get

$$
\begin{array} { r } { \mathrm { d } \mathbb { S } = \theta _ { \mathbb { L } } ^ { - } + \Phi ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

By exterior differentiation of (1.45), we obtain

$$
\Phi ^ { * } ( { \bf d } \theta _ { \mathbb { L } } ^ { + } ) = - { \bf d } \theta _ { \mathbb { L } } ^ { + } .
$$

From the definition of $\theta _ { \mathbb { L } } ^ { - }$ and $\theta _ { \mathbb { L } } ^ { + }$ , we know that

$$
\theta _ { \mathbb { L } } ^ { - } + \theta _ { \mathbb { L } } ^ { + } = { \bf d } \left( \mathbb { L } ( t _ { k + 1 } - t _ { k } ) \right) .
$$

By exterior differentiation of (1.47), we obtain $1 \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - }$ . Define

$$
\Omega _ { \mathbb { L } } \equiv { \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

Finally, we have shown that the discrete flow $\Phi$ preserves the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$

$$
\Phi ^ { * } ( \Omega _ { \mathbb { L } } ) = \Omega _ { \mathbb { L } } .
$$

Now, the variational integrator (1.35), the discrete energy conservation law (1.36), and the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$ converge to their continuous counterparts as $t _ { k + 1 } \to t _ { k } , t _ { k - 1 } \to t _ { k }$ .

Consider a conservative Lagrangian $L ( q , \dot { q } )$ . For simplicity, we choose the discrete Lagrangian as

$$
\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) = L \left( q _ { k } , \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) .
$$

The variational integrator (1.35) becomes

$$
\frac { \partial L } { \partial q _ { k } } ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { 1 } { t _ { k + 1 } - t _ { k } } \left( \frac { \partial L } { \partial \Delta _ { t } q _ { k } } ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { \partial L } { \partial \Delta _ { t } q _ { k - 1 } } ( q _ { k - 1 } , \Delta _ { t } q _ { k - 1 } ) \right) = 0 ,
$$

where $\Delta _ { t } q _ { k } = \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } }$ qk+1 − qk , Δtqk 1 = $\Delta _ { t } q _ { k - 1 } = \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } }$

It is easy to see that, as $t _ { k + 1 } \to t _ { k }$ , $t _ { k - 1 } \to t _ { k }$ , the Equation (1.51) converges to

$$
\frac { \partial L } { \partial q _ { k } } - \frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } _ { k } } = 0 .
$$

The discrete energy conservation law (1.36) becomes

$$
{ \frac { E _ { k + 1 } - E _ { k } } { t _ { k + 1 } - t _ { k } } } = 0 ,
$$

where

$$
\begin{array} { l } { { \displaystyle E _ { k + 1 } = \frac { \partial L } { \partial \Delta _ { t } q _ { k } } \Delta _ { t } q _ { k } - L \left( q _ { k } , \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) , } } \\ { { \displaystyle E _ { k } = \frac { \partial L } { \partial \Delta _ { t } q _ { k - 1 } } \Delta _ { t } q _ { k - 1 } - L \left( q _ { k - 1 } , \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) . } } \end{array}
$$

The Equation (1.53) converges to

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } \left( { \frac { \partial L } { \partial { \dot { q } } _ { k } } } { \dot { q } } _ { k } - L \right) = 0
$$

as $t _ { k + 1 } \to t _ { k }$ , $t _ { k - 1 } \to t _ { k }$ .

Now, we will consider the discrete extended Lagrange 2-form $\Omega _ { \mathbb { L } }$ defined by (1.48). By discretization of (1.50), the discrete extended Lagrange 1-form $\theta _ { \mathbb { L } } ^ { + }$ defined in (1.42) becomes

$$
\theta _ { \mathbb { L } } ^ { + } = \left( L ( q _ { k } , \Delta _ { t } q _ { k } ) - \frac { \partial L } { \partial \Delta _ { t } q _ { k } } \Delta _ { t } q _ { k } \right) { \mathrm { d } } t _ { k + 1 } + \frac { \partial L } { \partial \Delta _ { t } q _ { k } } { \mathrm { d } } q _ { k + 1 } .
$$

From (1.55), we can deduce that $\theta _ { \mathbb { L } } ^ { + }$ converges to the continuous Lagrangian 1-form $\vartheta _ { L }$ defined by (1.29) as $t _ { k + 1 } \to t _ { k } , t _ { k - 1 } \to t _ { k }$ . Thus, we obtain

$$
\Omega _ { \mathbb { L } } = \mathbf { d } \theta _ { \mathbb { L } } ^ { + } \longrightarrow \mathrm { d } \vartheta _ { L } = \Omega _ { L } , \quad t _ { k + 1 } \longrightarrow t _ { k } , \quad t _ { k - 1 } \longrightarrow t _ { k } .
$$

In general, the variational integrator (1.35) with fixed time steps does not exactly conserve the discrete energy, and the computed energy will not have secular variation $\left[ \mathrm { G M 8 8 } , \mathrm { S S C 9 4 } \right]$ . In some cases, such as in discrete mechanics proposed by Lee in $\mathrm { [ L e e 8 2 , L e e 8 7 ] }$ , the integrator (1.35) is required to conserve the discrete energy (1.36) by varying the time steps. In other words, the steps can be chosen according to (1.36) so that the integrator (1.35) conserves the discrete energy (1.36). The resulting integrator also conserves the discrete extended Lagrange 2-form $\mathrm { d } \theta _ { \mathbb { L } } ^ { + }$ . This fact had not been discussed in Lee’s discrete mechanics.

Example 1.3. Let us consider an example. For the classical Lagrangian

$$
L ( t , q , \dot { q } ) = \frac { 1 } { 2 } \dot { q } ^ { 2 } - V ( q ) ,
$$

we choose the discrete Lagrangian $\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } )$ as

$$
\mathbb { L } ( t _ { k } , q _ { k } , t _ { k + 1 } , q _ { k + 1 } ) = \frac { 1 } { 2 } \left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } \right) ^ { 2 } - V \left( \frac { q _ { k + 1 } - q _ { k } } { 2 } \right) .
$$

The discrete Euler–Lagrange equation (1.35) becomes

$$
\left( \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { q _ { k } - q _ { k - 1 } } { t _ { k } - t _ { k - 1 } } \right) + \frac { V ^ { \prime } ( \bar { q } _ { k } ) ( t _ { k + 1 } - t _ { k } ) + V ^ { \prime } ( \bar { q } _ { k - 1 } ) ( t _ { k } - t _ { k - 1 } ) } { 2 } = 0 ,
$$

which preserves the Lagrange 2-form

$$
\begin{array} { r } { \left( \frac { 1 } { t _ { k + 1 } - t _ { k } } + \frac { t _ { k + 1 } - t _ { k } } { 4 } V ^ { \prime \prime } ( \bar { q } _ { k } ) \right) { \mathrm { d } { q } _ { k + 1 } } \wedge { \mathrm { d } { q } _ { k } } , } \end{array}
$$

where $\bar { q } _ { k } = \frac { q _ { k } + q _ { k + 1 } } { 2 }$ , $\bar { q } _ { k - 1 } = \frac { q _ { k - 1 } + q _ { k } } { 2 }$ .

If we take fixed variables $t _ { k + 1 } - t _ { k } = t _ { k } - t _ { k - 1 } = h$ , then (1.59) becomes

$$
{ \frac { q _ { k + 1 } - 2 q _ { k } + q _ { k - 1 } } { h ^ { 2 } } } + { \frac { V ^ { \prime } ( { \bar { q } } _ { k } ) + V ^ { \prime } ( { \bar { q } } _ { k - 1 } ) } { 2 } } = 0 ,
$$

which preserves the Lagrange 2-form

$$
\left( { \frac { 1 } { h } } + { \frac { h } { 4 } } V ^ { \prime \prime } ( { \bar { q } } _ { k } ) \right) { \mathrm { d } } q _ { k + 1 } \wedge { \mathrm { d } } q _ { k } .
$$

# 14.1.4 Concluding Remarks

We have presented the calculus of total variation problem for discrete mechanics with variable time steps referring to continuous mechanics in this section. Using the calculus for discrete total variations, we have proved that Lee’s discrete mechanics is symplectic and derived Kane–Marsden–Ortiz integrators. It is well known that an energy-preserving variational integrator is a more preferable and natural candidate of approximations for conservative Euler–Lagrange equation, since the solution of conservative Euler–Lagrange equation is not only symplectic but also energy-preserving.

As is mentioned, Kane–Marsden–Ortiz integrators are related closely to the discrete mechanics proposed by Lee[Lee82,Lee87] . In Lee’s discrete mechanics, the difference equations are the same as Kane–Marsden–Ortiz integrators. However, Lee’s difference equations are solved as boundary value problems, while Kane–Marsden–Ortiz integrators are solved as initial value problems.

Finally, it should be mentioned that in very recent works[GLW01a,GLWW01,GW03] , two of the authors (HYG and KW) and their collaborators have presented a difference discrete variational calculus and the discrete version of Euler–Lagrange cohomology for vertical variation problems in both Lagrangian and Hamiltonian formalism for discrete mechanics and field theory. In their approach, the difference operator with fixed step-length is regarded as an entire geometric object. The advantages of this approach have already been seen in the last subsection in the course of taking continuous limits although the difference operator $\Delta _ { t }$ in (1.50) is of variable step-length. This approach may be generalized to the discrete total variation problems.

# 14.2 Total Variation in Hamiltonian Formalism

We present a discrete total variation calculus in Hamiltonian formalism in this section. Using this discrete variation calculus and generating function for flows of Hamiltonian systems, we derive symplectic-energy integrators of any finite order for Hamiltonian systems from a variational perspective. The relationship between the symplectic integrators derived directly from the Hamiltonian systems and the variationally derived symplectic-energy integrators is explored.

# 14.2.1 Variational Principle in Hamiltonian Mechanics

Let us begin by recalling the ordinary variational principle in Hamiltonian formalism. Suppose $Q$ denotes the configuration space with coordinates $q ^ { i }$ , and $T ^ { * } Q$ the phase space with coordinates $( q ^ { i } , p ^ { i } ) ( i = 1 , 2 , \cdots , n )$ . Consider a Hamiltonian $H : T ^ { * } Q $ $\mathbb { R }$ . The corresponding action functional is defined by

$$
S ( ( q ^ { i } ( t ) , p ^ { i } ( t ) ) ) = \int _ { a } ^ { b } ( p ^ { i } \cdot q ^ { i } - H ( q ^ { i } , p ^ { i } ) ) \operatorname { d } t ,
$$

where $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ is a $C ^ { 2 }$ curve in phase space $T ^ { * } Q$ .

The variational principle in Hamiltonian formalism seeks the curves $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ for which the action functional $S$ is stationary under variations of $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ with fixed end points. We will first define the variation of $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ .

Let

$$
V = \sum _ { i = 1 } ^ { n } \phi ^ { i } ( { \bf q } , { \bf p } ) \frac { \partial } { \partial q ^ { i } } + \sum _ { i = 1 } ^ { n } \psi ^ { i } ( { \bf q } , { \bf p } ) \frac { \partial } { \partial p ^ { i } } ,
$$

be a vector field on $T ^ { * } Q$ , here $\pmb q = ( q ^ { 1 } , \cdot \cdot \cdot , q ^ { n } ) , \pmb { p } = ( p ^ { 1 } , \cdot \cdot \cdot , p ^ { n } )$ . For simplicity, we will use Einstein convention and omit the summation notation $\displaystyle \sum$ in the following.

Let us denote the flow of $V$ by $F ^ { \varepsilon } : F ^ { \varepsilon } ( \pmb { q } , \pmb { p } ) = ( \tilde { \pmb { q } } , \tilde { \pmb { p } } )$ , which is written in components as

$$
\begin{array} { r } { \tilde { q } ^ { i } = f ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) , } \\ { \tilde { p } ^ { i } = g ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) , } \end{array}
$$

where $( { \pmb q } , { \pmb p } ) \in T ^ { * } Q$ and

$$
\begin{array} { r l } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } f ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) = \phi ^ { i } ( \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , \pmb { q } , \pmb { p } ) = \psi ^ { i } ( \pmb { q } , \pmb { p } ) . } \end{array}
$$

Let $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ be a curve in $T ^ { * } Q$ . The transformation (2.3) and (2.4) transforms $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ into a family of curves

$$
\left( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \right) = \left( f ^ { i } ( \varepsilon , \pmb { q } ( t ) , \pmb { p } ( t ) ) , g ^ { i } ( \varepsilon , \pmb { q } ( t ) , \pmb { p } ( t ) ) \right) .
$$

Next, we will define the variation of $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ :

$$
\delta \bigl ( q ^ { i } ( t ) , p ^ { i } ( t ) \bigr ) = : \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big | _ { \varepsilon = 0 } \bigl ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \bigr ) = \bigl ( \phi ^ { i } ( q , p ) , \psi ^ { i } ( q , p ) \bigr ) .
$$

Next, we will calculate the variation of $S$ at $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ as follows:

$$
\begin{array} { r l } { \delta S } & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S \Big ( \big ( \bar { q } ^ { i } ( t ) , \bar { p } ^ { i } ( t ) \big ) \Big ) } \\ & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } S \Big ( \big ( f ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) , g ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) \big ) \Big ) } \\ & { = \left. \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \right| _ { \varepsilon = 0 } \int _ { a } ^ { b } \bigg ( g ^ { i } \Big ( \varepsilon , q ( t ) , p ( t ) \Big ) \frac { \mathrm { d } } { \mathrm { d } t } f ^ { i } \Big ( \varepsilon , q ( t ) , p ( t ) \Big ) } \\ & { \quad - H \Big ( f ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) , g ^ { i } ( \varepsilon , q ( t ) , p ( t ) ) \Big ) \bigg ) \mathrm { d } t } \\ & { = \int _ { a } ^ { b } \bigg [ \Big ( \bar { q } ^ { i } - \frac { \partial H } { \partial p ^ { i } } \Big ) \psi ^ { i } + \Big ( - \bar { p } ^ { i } - \frac { \partial H } { \partial q ^ { i } } \Big ) \phi ^ { i } \bigg ] \mathrm { d } t + p ^ { i } \phi ^ { i } \bigg | _ { a } ^ { b } . } \end{array}
$$

If $\phi ^ { i } \bigl ( \pmb { q } ( a ) , \pmb { p } ( a ) \bigr ) \phi ^ { i } \bigl ( \pmb { q } ( b ) , \pmb { p } ( b ) \bigr ) = 0$ , the requirement of $\delta S = 0$ yields the Hamilton equation for $\left( q ^ { i } ( t ) , p ^ { i } ( t ) \right)$ :

$$
\dot { q } ^ { i } = \frac { \partial H } { \partial p ^ { i } } , ~ \dot { p } ^ { i } = - \frac { \partial H } { \partial q ^ { i } } .
$$

If we drop the requirement of $\phi ^ { i } \big ( { \pmb q } ( a ) , { \pmb p } ( a ) \big ) \phi ^ { i } \big ( { \pmb q } ( b ) , { \pmb p } ( b ) \big ) \ = \ 0$ , we can naturally obtain the canonical 1-form on $T ^ { * } Q$ from the second term in (2.6): $\theta = p ^ { i } \mathrm { d } q ^ { i }$ . Furthermore, restricting $\left( ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) ) \right)$ to the solution space of (2.7), we can prove that the solution of (2.7) preserves the canonical 2-form $\omega = \mathbf { d } \theta _ { L } = \mathbf { d } p ^ { i } \wedge \mathbf { d } q ^ { i }$ .

On the other hand, it is not necessary to restrict $\left( ( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) ) \right)$ to the solution space of (2.7). Introducing the Euler–Lagrange 1-form

$$
E ( q ^ { i } , p ^ { i } ) = \Big ( \dot { q } ^ { i } - \frac { \partial H } { \partial p ^ { i } } \Big ) { \bf d } p ^ { i } + \Big ( - \dot { p } ^ { i } - \frac { \partial H } { \partial q ^ { i } } \Big ) { \bf d } q ^ { i } ,
$$

the nilpotency of $d$ leads to

$$
\mathrm { d } E ( q ^ { i } , p ^ { i } ) + \frac { \mathrm { d } } { \mathrm { d } t } \omega = 0 ,
$$

namely, the necessary and sufficient condition for symplectic structure preserving is that the Euler–Lagrange 1-form (2.8) is closed[GLW01a,GLWW01,GLW01b,GW03] .

Based on the above-given variational principle in Hamiltonian formalism and using the ideas of discrete Lagrange mechanics[Ves88,Ves91b,MPS98,WM97] , we can develop a natural version of discrete Hamilton mechanics with fixed time steps and derive symplectic integrators for Hamilton canonical equations from a variational perspective[GLWW01] .

However, the symplectic integrators obtained in this way are not energy-preserving, in general, because of its fixed time steps[GM88] . An energy-preserving symplectic integrator is a more preferable and natural candidate of approximations for conservative Hamilton equations since the solution of conservative Hamilton equations is not only symplectic but also energy-preserving. To attain this goal, we use variable time steps and a discrete total variation calculus developed in [Lee82,Lee87,KMO99,CGW03] . The basic idea is to construct a discrete action functional with variable time steps and then apply a discrete total variation calculus. In this way, we can derive symplectic integrators and their associated energy conservation laws. These variationally derived symplectic integrators are two-step integrators. If we take fixed time steps, the resulting integrators are equivalent to the symplectic integrators derived directly from the Hamiltonian systems in some special cases.

# 14.2.2 Total Variation in Hamiltonian Mechanics

In order to discuss total variation in Hamiltonian formalism, we will work with extended phase space $\mathbb { R } \times T ^ { * } Q$ with coordinates $( t , q ^ { i } , p ^ { i } )$ . Here $t$ denotes time. For details, see $\left[ { \mathrm { A r n } } 8 9 , { \mathrm { G P S } } 0 2 \right]$ . By total variation, we refer to variations of both $( q ^ { i } , p ^ { i } )$ and $t$ . Consider a vector field on $\mathbb { R } \times T ^ { * } Q$ ,

$$
V = \xi ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial q ^ { i } } + \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial p ^ { i } } .
$$

Let $F ^ { \varepsilon }$ be the flow of $V$ . For $( t , q ^ { i } , p ^ { i } ) \in \mathbb { R } \times T ^ { * } Q$ , we have $F ^ { \varepsilon } ( t , q ^ { i } , p ^ { i } ) = ( \tilde { t } , \tilde { q } ^ { i } , \tilde { p } ^ { i } )$ :

$$
\begin{array} { l } { { \tilde { t } _ { \mathbf { \lambda } } = h ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \\ { { \tilde { q } ^ { i } = f ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \\ { { \tilde { p } ^ { i } = g ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) , } } \end{array}
$$

where

$$
\begin{array} { r l } & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } h ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \xi ( t , \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } f ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \phi ^ { i } ( t , \pmb { q } , \pmb { p } ) , } \\ & { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } g ^ { i } ( \varepsilon , t , \pmb { q } , \pmb { p } ) = \psi ^ { i } ( t , \pmb { q } , \pmb { p } ) . } \end{array}
$$

The transformation $( 2 . 1 1 ) - ( 2 . 1 3 )$ transforms a curve $( q ^ { i } ( t ) , p ^ { i } ( t ) )$ into a family of curves $( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) )$ determined by

$$
\begin{array} { l } { { \tilde { t } = h \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) , } } \\ { { \tilde { q } ^ { i } = f ^ { i } \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) , } } \\ { { \tilde { p } ^ { i } = g ^ { i } \big ( \varepsilon , t , \pmb { q } ( t ) , \pmb { p } ( t ) \big ) . } } \end{array}
$$

Suppose we can solve (2.17) for $t : t = h ^ { - 1 } ( \varepsilon , \tilde { t } )$ . Then,

$$
\begin{array} { l } { { \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) = f ^ { i } ( \varepsilon , h ^ { - 1 } ( \varepsilon , \tilde { t } ) , \pmb { q } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) , \pmb { p } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) ) , } } \\ { { \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) = f ^ { i } ( \varepsilon , h ^ { - 1 } ( \varepsilon , \tilde { t } ) , \pmb { q } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) , \pmb { p } ( h ^ { - 1 } ( \varepsilon , \tilde { t } ) ) ) . } } \end{array}
$$

Before calculating the variation of $S$ directly, we will first consider the first-order prolongation of $V$ ,

$$
\mathrm { p r } ^ { 1 } V = \xi ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial t } + \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial { \pmb q } ^ { i } } + \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial p ^ { i } } + \alpha ^ { i } ( t , { \pmb q } , { \pmb p } , { \pmb q } , { \pmb p } ) \frac { \partial } { \partial { \pmb q } ^ { i } } + \beta ^ { i } ( t , { \pmb q } , { \pmb p } , { \pmb { \dot { q } } } , { \pmb { \dot { p } } } ) \frac { \partial } { \partial \vec { p } ^ { i } } ,
$$

where $\mathrm { p r } ^ { 1 } V$ denotes the first-order prolongation of $V$ and

$$
\begin{array} { l } { { \alpha ^ { i } ( t , { \pmb q } , { \pmb p } , { \dot { \pmb q } } , { \dot { \pmb p } } ) = D _ { t } \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) - { \dot { q } ^ { i } } D _ { t } \xi \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) , } } \\ { { \beta ^ { i } ( t , { \pmb q } , { \pmb p } , { \dot { \pmb q } } , { \dot { \pmb p } } ) = D _ { t } \psi ^ { i } ( t , { \pmb q } , { \pmb p } ) - { \dot { p } ^ { i } } D _ { t } \xi \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) , } } \end{array}
$$

where $D _ { t }$ denotes the total derivative. For example,

$$
D _ { t } \phi ^ { i } ( t , { \pmb q } , { \pmb p } ) = \phi _ { t } ^ { i } + \phi _ { q } \dot { \pmb q } + \phi _ { \pmb p } \dot { \pmb p } .
$$

For prolongation of vector field and formulae (2.23) and (2.24), refer to $[ \mathrm { O l v 9 3 } ]$ .

Now, let us calculate the variation of $S$ directly as follows:

$$
\begin{array} { l } { { \delta S ~ = ~ \left. { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } } \right| _ { \varepsilon = 0 } S \big ( ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) ) \big ) } } \\ { { { } ~ = ~ \left. { \frac { \mathrm { d } } { \mathrm { d } \varepsilon } } \right| _ { \varepsilon = 0 } \int _ { \tilde { a } } ^ { \tilde { b } } \Big ( \big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) { \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \Big ) \mathrm { d } \tilde { t } } } \end{array}
$$

$$
\begin{array} { r l } { \ } & { = \ \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \int _ { a } ^ { b } \Big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } + t } \\ & { \qquad \big ( \tilde { t } = h ( \varepsilon , i , q ( t ) , p ( t ) ) \big ) } \\ { \ } & { = \ \int _ { a } ^ { b } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \Big \vert _ { \varepsilon = 0 } \Big ( \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \frac { \mathrm { d } } { \mathrm { d } \tilde { t } } \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) - H \big ( \tilde { q } ^ { i } ( \varepsilon , \tilde { t } ) , \tilde { p } ^ { i } ( \varepsilon , \tilde { t } ) \big ) \Big ) \mathrm { d } t } \\ & { \ + \ \int _ { a } ^ { b } \big ( p ^ { i } ( t ) \dot { q } ^ { i } ( t ) - H \big ( q ^ { i } ( t ) , p ^ { j } ( t ) \big ) \big ) D _ { \varepsilon } \xi \mathrm { d } t } \\ { \ } & { = \ \int _ { a } ^ { b } \Big [ \Big ( \frac { \mathrm { d } } { \mathrm { d } t } H \big ( q ^ { i } ( t ) , p ^ { i } ( t ) \big ) \Big ) \xi + \Big ( - \tilde { p } ^ { i } - \frac { \partial { H } } { \partial q ^ { i } } \Big ) \dot { \varphi } ^ { i } + \Big ( \dot { q } ^ { i } - \frac { \partial { H } } { \partial p ^ { i } } \Big ) \psi ^ { i } \Big ] \mathrm { d } t } \\ & { \ + [ p ^ { i } \dot { q } ^ { i } - H ( { q } ^ { i } , p ^ { i } ) \xi ] _ { * } ^ { b } . } \end{array}
$$

In (2.25), we have used (2.14)and the fact

$$
\frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \frac { \mathrm { d } \tilde { t } } { \mathrm { d } t } = \frac { \mathrm { d } } { \mathrm { d } t } \frac { \mathrm { d } } { \mathrm { d } \varepsilon } \bigg \vert _ { \varepsilon = 0 } \tilde { t } = D _ { t } \xi .
$$

In (2.26), we have used the prolongation formula (2.23).

If $\xi { \big ( } a , \pmb { q } ( a ) , \pmb { p } ( a ) { \big ) } = \xi { \big ( } b , \pmb { q } ( b ) , \pmb { p } ( b ) { \big ) } = 0$ and $\phi ^ { i } \bigl ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \bigr ) = \phi ^ { i } \bigl ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \bigr )$ $= 0$ , the requirement of $\delta S = 0$ yields the Hamilton canonical equation

$$
\dot { q } ^ { i } = \frac { \partial H } { \partial p ^ { i } } , \quad \dot { p } ^ { i } = - \frac { \partial H } { \partial q ^ { i } }
$$

from the variation $\phi ^ { i } , \psi ^ { i }$ and the energy conservation law

$$
\frac { \mathrm { d } } { \mathrm { d } t } H ( q ^ { i } , p ^ { i } ) = 0
$$

from the variation $\xi$ . Since

$$
{ \frac { \mathrm { d } } { \mathrm { d } t } } H ( q ^ { i } , p ^ { i } ) = { \frac { \partial H } { \partial q ^ { i } } } \cdot q ^ { i } + { \frac { \partial H } { \partial p ^ { i } } } \cdot p ^ { i } ,
$$

we can very well see that the energy conservation law (2.28) is a natural consequence of the Hamilton canonical Equation (2.27).

If we drop the requirement

$$
\begin{array} { l } { { \displaystyle \xi \big ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \big ) = \xi \big ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \big ) = 0 , } } \\ { { \displaystyle \phi ^ { i } \big ( a , \pmb { q } ( a ) , \pmb { p } ( a ) \big ) = \phi ^ { i } \big ( b , \pmb { q } ( b ) , \pmb { p } ( b ) \big ) = 0 , } } \end{array}
$$

we can define the extended canonical 1-form on $\mathbb { R } \times T ^ { * } Q$ from the second term in (2.26)

$$
\theta = p ^ { i } \mathrm { d } q ^ { i } - H ( q ^ { i } , p ^ { i } ) \mathrm { d } t .
$$

Furthermore, restricting $\left( \tilde { q } ^ { i } ( t ) , \tilde { p } ^ { i } ( t ) \right)$ to the solution space of (2.27), we can prove that the solution of (2.27) preserves the extended canonical 2-form

$$
\omega = \mathbf { d } \theta = \mathbf { d } p ^ { i } \wedge \mathbf { d } q ^ { i } - \mathbf { d } H ( q ^ { i } , p ^ { i } ) \wedge \mathbf { d } t
$$

by using the same method i $\mathrm { | ^ { [ M P S 9 8 ] } }$ .

# 14.2.3 Symplectic-Energy Integrators

In this section, we will develop a discrete version of total variation in Hamiltonian formalism. Using this discrete total variation calculus, we will derive symplectic-energy integrators.

Let

$$
L ( q ^ { i } , p ^ { i } , \dot { q } ^ { i } , \dot { p } ^ { i } ) = p ^ { i } \dot { q } ^ { i } - H ( q ^ { i } , p ^ { i } )
$$

be a function from $\mathbb { R } \times T ( T ^ { * } Q )$ to $\mathbb { R }$ . Here $L$ does not depend on $t$ explicitly.

We use $P \times P$ for the discrete version $\mathbb { R } \times T ( T ^ { * } Q )$ . Here $P$ is the discrete version of $\mathbb { R } \times T ^ { * } Q$ . A point $\left( t _ { 0 } , \pmb { q } _ { 0 } , \pmb { p } _ { 0 } ; t _ { 1 } , \pmb { q } _ { 1 } , \pmb { p } _ { 1 } \right) \in P \times P$ corresponds to a tangent vector

$$
\biggl ( { \frac { q _ { 1 } - q _ { 0 } } { t _ { 1 } - t _ { 0 } } } , { \frac { p _ { 1 } - p _ { 0 } } { t _ { 0 } - t _ { 0 } } } \biggr ) .
$$

For simplicity, the vector symbols $\pmb q = ( q ^ { 1 } , \cdots , q ^ { n } )$ and $\pmb { p } = ( p ^ { 1 } , \cdots , p ^ { n } )$ are used throughout this section. A discrete $L$ is defined to be $\mathbb { L } : P \times P \to \mathbb { R }$ and the corresponding discrete action as

$$
S = \sum _ { k = 0 } ^ { N - 1 } \mathbb { L } ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) ( t _ { k + 1 } - t _ { k } ) ,
$$

where $t _ { 0 } ~ = ~ a , t _ { N } ~ = ~ b$ . The discrete variational principle in total variation is to extremize $S$ for variations of both ${ \pmb q } _ { k } , { \pmb p } _ { k }$ and $t _ { k }$ holding the end points $\left( t _ { 0 } , \pmb q _ { 0 } , \pmb p _ { 0 } \right)$ and $\left( t _ { N } , \pmb q _ { N } , \pmb p _ { N } \right)$ fixed. This discrete variational principle determines a discrete flow $\Phi : P \times P \to P \times P$ by

$$
\Phi ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } ) = ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) .
$$

Here, $( t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } )$ for all $k \in ( 1 , 2 , \cdots , N - 1 )$ are found from the following discrete Hamilton canonical equation

$$
\begin{array} { r l } & { ( t _ { k + 1 } - t _ { k } ) D _ { 2 } \mathbb { L } ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 5 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } , t _ { k } , q _ { k } , p _ { k } ) = 0 , } \\ & { ( t _ { k + 1 } - t _ { k } ) D _ { 3 } \mathbb { L } ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } ) + ( t _ { k } - t _ { k - 1 } ) D _ { 6 } \mathbb { L } ( t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } , t _ { k } , q _ { k } , p _ { k } ) = 0 } \end{array}
$$

and the discrete energy conservation law

$$
\begin{array} { r } { ( t _ { k + 1 } - t _ { k } ) D _ { 1 } \mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) + ( t _ { k } - t _ { k - 1 } ) D _ { 4 } \mathbb { L } \big ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , \pmb { q } _ { k - 1 } \big ) } \\ { - \mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) + \mathbb { L } \big ( t _ { k - 1 } , \pmb { q } _ { k - 1 } , \pmb { p } _ { k - 1 } , t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } \big ) = 0 . } \end{array}
$$

$D _ { i }$ denotes the partial derivative of $\mathbb { L }$ with respect to the $i$ th argument. Equation (2.33) is the discrete Hamilton canonical equation (variational integrator). Equation (2.34) is the discrete energy conservation law associated with (2.33). Unlike the continuous case, the variational integrator (2.33) does not satisfy (2.34) for arbitrarily given $t _ { k + 1 }$ in general. Therefore, we need to solve (2.33) and (2.34) simultaneously with $q _ { k + 1 } , p _ { k + 1 }$ and $t _ { k + 1 }$ taken as unknowns.

Now, we will prove that the discrete flow determined by (2.33) and (2.34) preserves a discrete version of the extended Lagrange 2-form $\omega$ defined in (2.30) so that we call (2.33) and (2.34) a symplectic-energy integrator. We will do this directly from the variational point of view, consistent with the continuous case[MPS98] .

As in the continuous case, we will calculate $\mathrm { d } S$ for variations with varied end points.

$$
\begin{array} { r l } &  \begin{array} { r l } & { \mathrm { S i g } \{ q _ { 1 } , q _ { 2 } , p _ { 2 } , \cdots , t _ { N } , q _ { N - 1 } , ( p _ { N - 1 } , q _ { N - 1 } , q _ { N - 1 } , q _ { N - 1 } , \cdots , q _ { N } , p _ { N - 1 } , q _ { N } , q _ { N - 1 } , \cdots , q _ { N } , q _ { N - 1 } , q _ { N } , \cdots ) } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k } - \int _ { 0 } ^ { T } [ \Phi ( q _ { k } ) \Phi _ { k - 1 } ] \Phi _ { k } ) \Big ) \Big \} \Phi _ { k } } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } \Big ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k } ) + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k + 1 } + \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k - 1 } ) \Phi _ { k } \Big ) \Big ) \Phi _ { k } } \\ & { + \displaystyle \sum _ { k = 1 } ^ { N } ( \partial _ { k } [ q _ { k } ] \Phi _ { k } \Big ) \Big ) \Big \{ \Phi _ { k } + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k - 1 } - \Phi _ { k } \Big \} + \sum _ { k = 1 } ^ { N } \frac { 1 } { | q _ { k } | } \Phi _ { k } \Big ) \Big ( \Phi _ { k + 1 } - \partial _ { k } [ q _ { k } ] \Phi _ { k - 1 } \Big ) } \\ & { - \displaystyle \sum _ { k = 1 } ^ { N } ( \int _ { 0 } ^ { T } ( \Phi ( q _ { k } ) \Phi _ { k - 1 } - q _ { k } ) + \mathcal { P } ( \cdot \Phi ) _ { k } [ q _ { k } ] \Phi _ { k - 1 } \Big ) \Phi _ { k } - \cdots ) \Phi _ { k } } \\ &  - \displaystyle \sum _ { k = 1 } ^ { N } ( \mathcal { P } _ { k } [ \Phi ( q _ { k } ) ] \Big ( \Phi ( q _ { k - 1 } , \cdots , q _ { N } ) \ \end{array} \end{array}
$$

where $\pmb { v } _ { k } = \left( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \right) ( k = 0 , 1 , \cdots , N - 1 )$ . We can see that the last six terms in (2.35) come from the boundary variations. Based on the boundary variations, we can define two 1-forms on $P \times P$ ,

$$
\begin{array} { r c l } { \theta _ { \mathbb { L } } ^ { - } ( \pmb { v } _ { k } ) } & { = } & { D _ { 2 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } \pmb { q } _ { k } + D _ { 3 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } \pmb { p } _ { k } } \\ & & { + D _ { 1 } \mathbb { L } ( \pmb { v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( \pmb { v } _ { k } ) \mathrm { d } t _ { k } } \end{array}
$$

and

$$
\begin{array} { r c l } { \theta _ { \mathbb { L } } ^ { + } ( { \pmb v } _ { k } ) } & { = } & { D _ { 5 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } { \pmb q } _ { k + 1 } + D _ { 6 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) \mathrm { d } { \pmb p } _ { k + 1 } } \\ & & { + D _ { 4 } \mathbb { L } ( { \pmb v } _ { k } ) ( t _ { k + 1 } - t _ { k } ) - \mathbb { L } ( { \pmb v } _ { k } ) \mathrm { d } t _ { k + 1 } . } \end{array}
$$

Here, we have used the notation in [MPS98] . We regard the pair $( \theta _ { \mathbb { L } } ^ { - } , \theta _ { \mathbb { L } } ^ { + } )$ as being the discrete version of the extended canonical 1-form $\theta$ defined in (2.29).

Now, we will parametrize the solutions of the discrete variational principle by $( t _ { 0 } , q _ { 0 } , t _ { 1 } , q _ { 1 } )$ , and restrict $S$ to that solution space. Then, Equation (2.35) becomes

$$
\begin{array} { r l } & { \mathrm { d } S ( t _ { 0 } , q _ { 0 } , p _ { 0 } , \cdots , t _ { N } , q _ { N } , p _ { N } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \cdots , \delta t _ { N } , \delta q _ { N } , \delta p _ { N } ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) } \\ & { \quad + \theta _ { \mathbb { L } } ^ { + } ( t _ { N - 1 } , q _ { N - 1 } , p _ { N - 1 } , t _ { N } , q _ { N } , p _ { N } ) \cdot ( \delta t _ { N - 1 } , \delta q _ { N - 1 } , \delta p _ { N - 1 } , \delta t _ { N } , \delta q _ { N } , \delta p _ { N } ) } \\ & { = \theta _ { \mathbb { L } } ^ { - } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) } \\ & { \quad + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } ( t _ { 0 } , q _ { 0 } , p _ { 0 } , t _ { 1 } , q _ { 1 } , p _ { 1 } ) \cdot ( \delta t _ { 0 } , \delta q _ { 0 } , \delta p _ { 0 } , \delta t _ { 1 } , \delta q _ { 1 } , \delta p _ { 1 } ) . } \end{array}
$$

From (2.38), we can obtain

$$
\begin{array} { r } { \mathtt { d } S = \theta _ { \mathbb { L } } ^ { - } + ( \Phi ^ { N - 1 } ) ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

The Equation (2.39) holds for arbitrary $N > 1$ . Taking $N = 2$ , we obtain

$$
\begin{array} { r } { \mathtt { d } S = \theta _ { \mathbb { L } } ^ { - } + \Phi ^ { * } \theta _ { \mathbb { L } } ^ { + } . } \end{array}
$$

By exterior differentiation of (2.40), we obtain

$$
\Phi ^ { * } ( { \bf d } \theta _ { \mathbb { L } } ^ { + } ) = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

From the definition of $\theta _ { \mathbb { L } } ^ { - }$ and $\theta _ { \mathbb { L } } ^ { + }$ , we know that

$$
\begin{array} { r } { \theta _ { \mathbb { L } } ^ { - } + \theta _ { \mathbb { L } } ^ { + } = \mathrm { d } \mathbb { L } . } \end{array}
$$

By exterior differentiation of (2.42), we obtain ${ \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - }$ . Define

$$
\omega _ { \mathbb { L } } \equiv { \bf d } \theta _ { \mathbb { L } } ^ { + } = - { \bf d } \theta _ { \mathbb { L } } ^ { - } .
$$

Finally, we have shown that the discrete flow $\Phi$ preserves the discrete extended canonical 2-form $\omega _ { \mathbb { L } }$ :

$$
\begin{array} { r } { \Phi ^ { * } ( \omega _ { \mathbb { L } } ) = \omega _ { \mathbb { L } } . } \end{array}
$$

We can now call the coupled difference system (2.33) and (2.34) a symplecticenergy integrator in the sense that it satisfies the discrete energy conservation law (2.34) and preserves the discrete extended canonical 2-form $\omega _ { \mathbb { L } }$ .

To illustrate the above-mentioned discrete total variation calculus, we present an example. We choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } ( t _ { k } , q _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } ) = \pmb { p } _ { k + 1 / 2 } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - H ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) ,
$$

where

$$
{ \pmb p } _ { k + 1 / 2 } = \frac { { \pmb p } _ { k } + { \pmb p } _ { k + 1 } } { 2 } , \qquad { \pmb q } _ { k + 1 / 2 } = \frac { { \pmb q } _ { k } + { \pmb q } _ { k + 1 } } { 2 } .
$$

Using (2.33), we can obtain the corresponding discrete Hamilton equation

$$
\begin{array} { l } { \displaystyle \frac { { \bf q } _ { k + 1 } - { \bf q } _ { k - 1 } } { 2 } - \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial H } { \partial { \bf p } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial H } { \partial { \bf p } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) = 0 , } \\ { \displaystyle \frac { { \bf p } _ { k + 1 } - { \bf p } _ { k - 1 } } { 2 } + \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial H } { \partial { \bf q } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial H } { \partial { \bf q } } ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } ) \bigg ) = 0 . } \end{array}
$$

where $\begin{array} { r } { { \pmb p } _ { k - 1 / 2 } = \frac { { \pmb p } _ { k } + { \pmb p } _ { k - 1 } } { 2 } , \quad { \pmb q } _ { k - 1 / 2 } = \frac { { \pmb q } _ { k } + { \pmb q } _ { k - 1 } } { 2 } } \end{array}$ .

Using (2.34), we can obtain the corresponding discrete energy conservation law

$$
H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) = H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) .
$$

The symplectic-energy integrator (2.46) and (2.47) preserves the discrete 2-form:

$$
\frac { 1 } { 2 } \big ( \mathrm { d } \pmb { p } _ { k } \wedge \mathrm { d } \pmb { q } _ { k + 1 } + \mathrm { d } \pmb { p } _ { k + 1 } \wedge \mathrm { d } \pmb { q } _ { k } \big ) - H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) \wedge \Big ( \frac { \mathrm { d } t _ { k } + \mathrm { d } t _ { k + 1 } } { 2 } \Big ) .
$$

If we take fixed time steps $t _ { k + 1 } - t _ { k } = h \left( h \right.$ is a constant), then (2.46) becomes

$$
\begin{array} { l } { \displaystyle \frac { { \pmb q } _ { k + 1 } - { \pmb q } _ { k - 1 } } { 2 h } = \frac { 1 } { 2 } \bigg ( \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) \bigg ) , } \\ { \displaystyle \frac { { \pmb p } _ { k + 1 } - { \pmb p } _ { k - 1 } } { 2 h } = - \frac { 1 } { 2 } \bigg ( \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) \bigg ) . } \end{array}
$$

Now, we will explore the relationship between (2.49) and the midpoint integrator for the Hamiltonian system

$$
\begin{array} { l } { { \displaystyle { \dot { \pmb q } } ~ = ~ { \frac { \partial { \cal H } } { \partial { \pmb p } } } , } } \\ { { \displaystyle { \dot { \pmb p } } ~ = ~ - { \frac { \partial { \cal H } } { \partial { \pmb q } } } . } } \end{array}
$$

The midpoint symplectic integrator for (2.50) is

$$
\begin{array} { r c l } { \displaystyle \frac { { \pmb q } _ { k + 1 } - { \pmb q } _ { k } } { h } } & { = } & { \displaystyle \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) , } \\ { \displaystyle \frac { { \pmb p } _ { k + 1 } - { \pmb p } _ { k } } { h } } & { = } & { \displaystyle - \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } \big ) . } \end{array}
$$

Replacing $k$ by $k - 1$ in (2.51), we obtain

$$
\begin{array} { r c l } { \displaystyle \frac { { \pmb q } _ { k } - { \pmb q } _ { k - 1 } } { h } ~ = ~ \frac { \partial H } { \partial { \pmb p } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) , } \\ { \displaystyle \frac { { \pmb p } _ { k } - { \pmb p } _ { k - 1 } } { h } ~ = ~ - \frac { \partial H } { \partial { \pmb q } } \big ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } \big ) . } \end{array}
$$

Adding (2.52) to (2.51) results in (2.49). Therefore, if we use (2.51) to obtain $\pmb { p } _ { k } , \pmb { q } _ { k }$ , the two-step integrator (2.49) is equivalent to the midpoint integrator (2.51). However, the equivalence does not hold in general. For example, choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) = \pmb { p } _ { k } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - H \big ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } \big ) ,
$$

and take fixed time steps $t _ { k + 1 } - t _ { k } = h$ . Then (2.33) becomes

$$
\begin{array} { l } { \displaystyle \frac { { \bf q } _ { k + 1 } - { \bf q } _ { k } } { h } ~ = ~ \frac { 1 } { 2 } \Big ( \frac { \partial H } { \partial p } \big ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial p } \big ( { \bf q } _ { k - 1 / 2 } , { \bf p } _ { k - 1 / 2 } \big ) \Big ) , } \\ { \displaystyle \frac { { \bf p } _ { k } - { \bf p } _ { k - 1 } } { h } ~ = ~ - \frac { 1 } { 2 } \Big ( \frac { \partial H } { \partial { \bf q } } \big ( { \bf q } _ { k + 1 / 2 } , { \bf p } _ { k + 1 / 2 } \big ) + \frac { \partial H } { \partial { \bf q } } \big ( { \bf q } _ { k - 1 / 2 } , { \bf p } _ { k - 1 / 2 } \big ) \Big ) . } \end{array}
$$

The integrator (2.54) is a two-step integrator which preserves $\mathrm { d } p _ { k } \wedge \mathrm { d } q _ { k + 1 } .$ . In this case, we cannot find an one-step integrator which is equivalent to (2.54). In conclusion, using discrete total variation calculus, we have derived two-step symplectic-energy integrators. When taking fixed time steps, some of them are equivalent to one-step integrators derived directly from the Hamiltonian system while the others do not have this equivalence.

# 14.2.4 High Order Symplectic-Energy Integrator

In this subsection, we will develop high order symplectic-energy integrators by using the generating function of the flow of the Hamiltonian system

$$
\dot { { \pmb z } } = J \nabla H ( { \pmb z } ) ,
$$

where

$$
\begin{array} { r } { \boldsymbol { z } = ( \pmb { p } , \pmb { q } ) ^ { \mathrm { T } } , \qquad \boldsymbol { J } = \biggl ( \begin{array} { c c } { O } & { - I } \\ { I } & { O } \end{array} \biggr ) . } \end{array}
$$

Let us first recall the generating function with normal Darboux matrix of a symplectic transformation. For details, see Chapters 5 and 6, or [Fen86,FWQW89] .

Suppose $\alpha$ is a $4 n \times 4 n$ nonsingular matrix with the form

$$
\alpha = \left( \begin{array} { c c } { { A } } & { { B } } \\ { { C } } & { { D } } \end{array} \right) ,
$$

where $A , B , C$ and $D$ are both $2 n \times 2 n$ matrices.

We denote the inverse of $\alpha$ by

$$
\alpha ^ { - 1 } = \left( \begin{array} { c c } { { A _ { 1 } } } & { { B _ { 1 } } } \\ { { C _ { 1 } } } & { { D _ { 1 } } } \end{array} \right) ,
$$

where $A _ { 1 } , B _ { 1 } , C _ { 1 }$ and $D _ { 1 }$ are both $2 n \times 2 n$ matrices. We know that a $4 n \times 4 n$ matrix $\alpha$ is a Darboux matrix if

$$
\alpha ^ { \mathrm { T } } J _ { 4 n } \alpha = \widetilde { J } _ { 4 n } ,
$$

where

$$
\begin{array} { r } { J _ { 4 n } = \left( \begin{array} { c c } { O } & { - I _ { 2 n } } \\ { I _ { 2 n } } & { O } \end{array} \right) , \quad \tilde { J } _ { 4 n } = \left( \begin{array} { c c } { J _ { 2 n } } & { O } \\ { O } & { - J _ { 2 n } } \end{array} \right) , \quad J _ { 2 n } = \left( \begin{array} { c c } { O } & { - I _ { n } } \\ { I _ { n } } & { O } \end{array} \right) , } \end{array}
$$

where $I _ { n }$ is an $n \times n$ identity matrix and $I _ { 2 n }$ is a $2 n \times 2 n$ identity matrix.

Every Darboux matrix induces a fractional transform between symplectic and symmetric matrices

$$
{ \begin{array} { r l } & { \sigma _ { \alpha } : S p ( 2 n ) \longrightarrow S m ( 2 n ) , } \\ & { \sigma _ { \alpha } = ( A S + B ) ( C S + D ) ^ { - 1 } = M , \quad { \mathrm { f o r } } \quad S \in S p ( 2 n ) , { \mathrm { ~ d e t } } ( C S + D ) \neq 0 } \end{array} }
$$

with the inverse transform $\sigma _ { \alpha } ^ { - 1 } = \sigma _ { \alpha _ { - 1 } }$

$$
\begin{array} { l } { { \sigma _ { \alpha } ^ { - 1 } : \ S m ( 2 n ) \longrightarrow S p ( 2 n ) , } } \\ { { \sigma _ { \alpha } = ( A _ { 1 } M + B _ { 1 } ) ( C _ { 1 } M + D _ { 1 } ) ^ { - 1 } = S , } } \end{array}
$$

where $S p ( 2 n )$ is the group of symplectic matrices and $S m ( 2 n )$ the set of symmetric matrices.

We can generalize the above discussions to nonlinear transformations on $\mathbb { R } ^ { 2 n }$ . Let us denote the set of symplectic transformations on $\mathbb { R } ^ { 2 n }$ by $S p D _ { 2 n }$ and the set of symmetric transformations (i.e., transformations with symmetric Jacobian) on $\mathbb { R } ^ { 2 n }$ by $S y m m ( 2 n )$ . Every $f \in S y m m ( 2 n )$ corresponds, at least locally, to a real function $\phi$ (unique to a constant) such that $f$ is the gradient of $\phi$ ,

$$
f ( { \pmb w } ) = \nabla \phi ( { \pmb w } ) ,
$$

where $\nabla \phi ( { \pmb w } ) = \left( \phi _ { w _ { 1 } } ( { \pmb w } ) , \cdots , \phi _ { w _ { 2 n } } ( { \pmb w } ) \right)$ and ${ \pmb w } = ( w _ { 1 } , w _ { 2 } , \cdot \cdot \cdot , w _ { 2 n } )$

Then, we have

$$
\begin{array} { r l } & { \sigma _ { \alpha } : S p D _ { 2 n } \longrightarrow S y m m ( 2 n ) , } \\ & { \sigma _ { \alpha } = ( A \circ g + B ) \circ ( C \circ g + D ) ^ { - 1 } = \nabla \phi , \mathrm { f o r } g \in S p D _ { 2 n } , \mathrm { d e t } ( C g _ { z } + D ) \neq 0 } \end{array}
$$

or alternatively

$$
A g ( \pmb { z } ) + B \pmb { z } = ( \nabla \phi ) ( C g ( \pmb { z } ) + D \pmb { z } ) ,
$$

where $\circ$ denotes the composition of transformation and the $2 n \times 2 n$ constant matrices $A , B , C$ and $D$ are regarded as linear transformations. $g _ { z }$ denotes the Jacobian of symplectic transformation $g$ .

Let $\phi$ be the generating function of Darboux type $\alpha$ for symplectic transformation $g$ .

Conversely, we have

$$
\begin{array} { r l } & { \frac { - 1 } { \alpha } : S y m m \left( 2 n \right) \longrightarrow S p D _ { 2 n } , } \\ & { \frac { - 1 } { \alpha } ( \nabla \phi ) = \left( A _ { 1 } \circ \nabla \phi + B _ { 1 } \right) \circ ( C _ { 1 } \circ \nabla \phi + D _ { 1 } ) ^ { - 1 } = g , \mathrm { f o r } \mathrm { d e t } ( C _ { 1 } \phi _ { w w } + D _ { 1 } ) \ne 0 , } \end{array}
$$

or alternatively

$$
A _ { 1 } \nabla \phi ( \pmb { w } ) + B _ { 1 } \pmb { w } = g \big ( C _ { 1 } \nabla \phi ( \pmb { w } ) + D _ { 1 } \pmb { w } \big ) ,
$$

where $g$ is called the symplectic transformation of Darboux type $\alpha$ for the generating function $\phi$ .

For the study of integrators, we will restrict ourselves to normal Darboux matrices, i.e., those satisfying $A + B = 0 , C + D = I _ { 2 n }$ . The normal Darboux matrices can be characterized as

$$
\alpha = \left( \begin{array} { c c } { { J _ { 2 n } } } & { { - J _ { 2 n } } } \\ { { E } } & { { I _ { 2 n } - E } } \end{array} \right) , \quad E = \frac { 1 } { 2 } ( I _ { 2 n } + J _ { 2 n } F ) , \quad F ^ { \mathrm { T } } = F ,
$$

and

$$
\alpha ^ { - 1 } = \left( \begin{array} { c c } { { ( E - I _ { 2 n } ) J _ { 2 n } } } & { { I _ { 2 n } } } \\ { { E J _ { 2 n } } } & { { I _ { 2 n } } } \end{array} \right) .
$$

The fractional transform induced by a normal Darboux matrix establishes a oneone correspondence between symplectic transformations near identity and symmetric transformations near nullity.

For simplicity, we will take $F = 0$ , then $E = \frac { 1 } { 2 } I _ { 2 n }$ and

$$
\begin{array} { r } { \alpha = \left( \begin{array} { c c } { J _ { 2 n } } & { - J _ { 2 n } } \\ { \frac { 1 } { 2 } I _ { 2 n } } & { \frac { 1 } { 2 } I _ { 2 n } } \end{array} \right) . } \end{array}
$$

Now, we will consider the generating function of the flow of (2.55) and denote it by $e _ { H } ^ { t }$ . The generating function $\phi ( { \pmb w } , t )$ for the flow $e _ { H } ^ { t }$ of Darboux type (2.60) is given by

$$
\nabla \phi = { \bigl ( } J _ { 2 n } \circ e _ { H } ^ { t } - J _ { 2 n } { \bigr ) } \circ { \Bigl ( } { \frac { 1 } { 2 } } e _ { H } ^ { t } + { \frac { 1 } { 2 } } I _ { 2 n } { \Bigr ) } ^ { - 1 } , \quad { \mathrm { ~ f o r ~ s m a l l ~ } } \quad | t | ,
$$

where $\phi ( { \pmb w } , t )$ satisfies the Hamilton–Jacobi equation

$$
\frac { \partial } { \partial t } \phi ( { \pmb w } , t ) = - H \Big ( { \pmb w } + \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ( { \pmb w } , t ) \Big )
$$

and can be expressed by Taylor series in $t$ ,

$$
\phi ( { \pmb w } , t ) = \sum _ { k = 1 } ^ { \infty } \phi ^ { k } ( { \pmb w } ) t ^ { k } , \quad \mathrm { f o r ~ s m a l l } \quad | t | .
$$

The coefficients $\phi ^ { k } ( w )$ can be determined recursively as

$$
\begin{array} { l l l } { \phi ^ { 1 } ( { \pmb w } ) } & { = } & { \displaystyle - H ( { \pmb w } ) , } \\ { \phi ^ { k + 1 } ( { \pmb w } ) } & { = } & { \displaystyle \frac { - 1 } { k + 1 } \sum _ { m = 1 } ^ { k } \frac { 1 } { m ! } \sum _ { \stackrel { { . . . } } { j _ { 1 } } + . . . + j _ { m } = k } D ^ { m } H \bigg ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } , \cdots , \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } \bigg ) , } \\ & & { \quad \quad \quad \quad \quad \quad j _ { l } \geq 1 } \end{array}
$$

where $k \geq 1$ , and we use the notation of the $m$ -linear form

$$
\begin{array} { l } { { \displaystyle D ^ { m } H \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } , \cdot \cdot \cdot , \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } \Big ) } \ ~ } \\ { { \displaystyle ~ : = \sum _ { i _ { 1 } , \cdot \cdot \cdot , i _ { m } = 1 } ^ { 2 n } H _ { z _ { i _ { 1 } } \cdot \cdot \cdot \cdot z _ { i _ { m } } } ( z ) \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { 1 } } ( { \pmb w } ) \Big ) _ { i _ { 1 } } \cdot \cdot \cdot \Big ( \frac { 1 } { 2 } J _ { 2 n } \nabla \phi ^ { j _ { m } } ( { \pmb w } ) \Big ) _ { i _ { m } } } . } \end{array}
$$

From (2.61), we can see that the phase flow $\widehat { \pmb z } : = e _ { H } ^ { t } \pmb { z }$ satisfies

$$
J _ { 2 n } ( { \widehat { z } } - z ) = \nabla \phi \Bigl ( \frac { { \widehat { z } } - z } { 2 } \Bigr ) = \sum _ { j = 1 } ^ { \infty } t ^ { j } \nabla \phi ^ { j } \Bigl ( \frac { { \widehat { z } } + z } { 2 } \Bigr ) .
$$

Now, we will choose $\mathbb { L }$ in (2.31) as

$$
\mathbb { L } \big ( t _ { k } , \pmb { q } _ { k } , \pmb { p } _ { k } , t _ { k + 1 } , \pmb { q } _ { k + 1 } , \pmb { p } _ { k + 1 } \big ) = \pmb { p } _ { k + 1 / 2 } \frac { \pmb { q } _ { k + 1 } - \pmb { q } _ { k } } { t _ { k + 1 } - t _ { k } } - \psi ^ { m } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) ,
$$

where

$$
\psi ^ { m } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) = \sum _ { j = 1 } ^ { m } t ^ { j } \phi ^ { j } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) .
$$

The corresponding symplectic-energy integrator (2.33) and (2.34) is

$$
\frac {  { \mathbf { \ell } } _ { k + 1 } -  { \mathbf { q } } _ { k - 1 } } { 2 } - \frac { 1 } { 2 }  { \left( ( t _ { k + 1 } - t _ { k } ) \frac { \partial \psi ^ { m } } { \partial p } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial \psi ^ { m } } { \partial p } ( \pmb { q } _ { k - 1 / 2 } , \pmb { p } _ { k - 1 / 2 } ) \right) } = 0
$$

$$
\begin{array} { r l } & { \displaystyle \longrightarrow - \frac { 1 } { 2 } \Big [ \big ( t _ { k + 1 } - t _ { k } \big ) \frac { 1 } { \partial { \pmb p } } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { 1 } { \partial { \pmb p } } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) \Big ] = 0 } \\ & { \displaystyle \qquad \overset { , . . . } { \longrightarrow } + \frac { 1 } { 2 } \bigg ( ( t _ { k + 1 } - t _ { k } ) \frac { \partial \psi ^ { m } } { \partial { \pmb q } } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) \frac { \partial \psi ^ { m } } { \partial { \pmb q } } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) \bigg ) = 0 } \\ & { \displaystyle \qquad \psi ^ { m } ( { \pmb q } _ { k + 1 / 2 } , { \pmb p } _ { k + 1 / 2 } ) = \psi ^ { m } ( { \pmb q } _ { k - 1 / 2 } , { \pmb p } _ { k - 1 / 2 } ) , } \end{array}
$$

which satisfies the discrete extended canonical 2-form

$$
\frac { 1 } { 2 } ( \mathrm { d } p _ { k } \wedge \mathrm { d } q _ { k + 1 } + \mathrm { d } p _ { k + 1 } \wedge \mathrm { d } q _ { k } ) - \psi ^ { m } ( \pmb { q } _ { k + 1 / 2 } , \pmb { p } _ { k + 1 / 2 } ) \wedge \Big ( \frac { \mathrm { d } t _ { k } + \mathrm { d } t _ { k + 1 } } { 2 } \Big ) .
$$

The integrator (2.68) is a two-step symplectic-energy integrator with $2 m$ -th order of accuracy.

# 14.2.5 An Example and an Optimization Method

In this subsection, we will see an example. We will take the Hamiltonian as

$$
H ( q , p ) = { \frac { 1 } { 2 } } p ^ { 2 } + { \frac { 1 } { 2 } } ( q ^ { 4 } - q ^ { 2 } ) ,
$$

where $q$ and $p$ are scalars.

Corresponding to (2.70) the discrete Lagrangian (2.31) is chosen as

$$
\mathbb { L } \big ( t _ { k } , q _ { k } , p _ { k } , t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 } \big ) = p _ { k + 1 / 2 } \frac { q _ { k + 1 } - q _ { k } } { t _ { k + 1 } - t _ { k } } - \frac { 1 } { 2 } \big ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } \big ) .
$$

The corresponding symplectic-energy integrator (2.33) and (2.34) become

$$
\begin{array} { r l r } & { \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 } - \frac { 1 } { 2 } ( ( t _ { k + 1 } - t _ { k } ) p _ { k + 1 / 2 } + ( t _ { k } - t _ { k - 1 } ) p _ { k - 1 / 2 } ) = 0 , } & { ( 2 . 7 \times \frac { 1 } { 2 } ) } \\ & { \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 } + \frac { 1 } { 2 } ( ( t _ { k + 1 } - t _ { k } ) ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) ) = 0 , } & \\ & { \frac { 1 } { 2 } p _ { k + 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } ) = \frac { 1 } { 2 } p _ { k - 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k - 1 / 2 } ^ { 4 } - q _ { k - 1 / 2 } ^ { 2 } ) , } & \end{array}
$$

where ${ t _ { k - 1 } , q _ { k - 1 } , p _ { k - 1 } }$ and $t _ { k } , q _ { k } , p _ { k }$ are given and $t _ { k + 1 } , q _ { k + 1 } , p _ { k + 1 }$ are unknowns.

In the following numerical experiment, we will use a robust optimization method suggested in $\left[ { \mathrm { K M O 9 } } { \bar { 9 } } \right]$ to solve (2.72). Concretely, let

$$
\begin{array} { r l } & { \quad A = \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 } - \frac { 1 } { 2 } \Big ( ( t _ { k + 1 } - t _ { k } ) p _ { k + 1 / 2 } + ( \stackrel {  } { t _ { k } } - t _ { k - 1 } ) p _ { k - 1 / 2 } \Big ) , } \\ & { \quad B = \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 } + \frac { 1 } { 2 } \Big ( ( t _ { k + 1 } - t _ { k } ) ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( t _ { k } - t _ { k - 1 } ) ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) \Big ) , } \\ & { \quad C = \frac { 1 } { 2 } p _ { k + 1 / 2 } ^ { 2 } + \frac { 1 } { 2 } ( q _ { k + 1 / 2 } ^ { 4 } - q _ { k + 1 / 2 } ^ { 2 } ) - \frac { 1 } { 2 } p _ { k - 1 / 2 } ^ { 2 } - \frac { 1 } { 2 } ( q _ { k - 1 / 2 } ^ { 4 } - q _ { k - 1 / 2 } ^ { 2 } ) . } \end{array}
$$

Then, we will minimize the quantity

$$
F = A ^ { 2 } + B ^ { 2 } + C ^ { 2 }
$$

![](images/e2b288f67fcabe806081dbef8ba6dab35afa65f0dcebbccecd54263c28c377ab.jpg)  
Fig. 2.1. The orbits calculated by (2.72), (2.74) left plot $q _ { 0 } = 0 . 7 7$ , $p _ { 0 } = 0$ and right plot $q _ { 0 } = 0 . 9 9$ , $p _ { 0 } = 0$

![](images/729025c504697de64300c080d6625bcc95c2d0e31f7113488a33eab46924e6c7.jpg)  
Fig. 2.2. The energy evaluation by (2.72), (2.74) left plot $q _ { 0 } = 0 . 7 7$ , $p _ { 0 } = 0$ and right plot $q _ { 0 } = 0 . 9 9$ , $p _ { 0 } = 0$

over $q _ { k + 1 } , p _ { k + 1 }$ and $t _ { k + 1 }$ under the constraint $t _ { k + 1 } > t _ { k }$ . This constraint guarantees that no singularities occur in choosing time steps.

We will compare (2.72) with the following integrator with fixed time steps:

$$
\begin{array} { r l } & { \frac { q _ { k + 1 } - q _ { k - 1 } } { 2 h } - \frac { 1 } { 2 } ( p _ { k + 1 / 2 } + p _ { k - 1 / 2 } ) = 0 , } \\ & { \frac { p _ { k + 1 } - p _ { k - 1 } } { 2 h } + \frac { 1 } { 2 } \big ( ( 2 q _ { k + 1 / 2 } ^ { 3 } - q _ { k + 1 / 2 } ) + ( 2 q _ { k - 1 / 2 } ^ { 3 } - q _ { k - 1 / 2 } ) \big ) = 0 . } \end{array}
$$

In our numerical experiment, we use two initial conditions $q _ { 0 } = 0 . 7 7 , p _ { 0 } = 0 , t =$ 0 and $q _ { 0 } = 0 . 9 9 , p _ { 0 } = 0 , t = 0 .$ . To obtain $q _ { 1 }$ and $p _ { 1 }$ , we apply the midpoint integrator with $t _ { 1 } = 0 . 1$ . In Fig. 2.1, the orbits calculated by (2.72) and (2.74) are shown for the two initial conditions. The two orbits in each initial condition are almost indistinguishable. In Fig.2.2, we plot the evolution of the energy $H ( q _ { k + 1 / 2 } , p _ { k + 1 / 2 } )$ for both (2.72) and (2.74). The oscillating curve is for (2.74) and the lower line for (2.72). For more numerical examples, see $\left[ \mathrm { K M O 9 9 } \right]$ in the Lagrangian setting. In principle, the results $\mathrm { i n } ^ { \mathrm { [ K M O 9 9 ] } }$ apply to the Hamiltonian setting in the present method as well taking ${ \frac { q _ { k + 1 } - q _ { k } } { h } } = p _ { k + 1 / 2 } .$ . The purpose is to develop a discrete total variation calculus in the Hamiltonian setting and obtain the symplectic-energy integrators. The comprehensive implementation of the obtained integrators is not the subject of present and will be a topic for future research.

# 14.2.6 Concluding Remarks

We will develop a discrete total variation calculus in Hamiltonian formalism in this subsection. This calculus provides a new method for constructing structure-preserving integrators for Hamiltonian system from a variational point of view. Using this calculus, we will derive the energy conservation laws associated with integrators. The coupled integrators are two-step integrators and preserve a discrete version of the extended canonical 2-form. If we take fixed time steps, the resulting integrators are equivalent to the symplectic integrators derived directly from the Hamiltonian systems only in special cases. Thus, new two-step symplectic integrators are variationally obtained. Using generating function method, we will also obtain higher order symplectic-energy integrators.

In principle, our discussions can be generalized to multisymplectic Hamiltonian system

$$
M z _ { t } + K z _ { x } = \nabla _ { x } H ( z ) , \quad z \in \mathbb { R } ^ { n } ,
$$

where $M$ and $K$ are skew-symmetric matrices on $\mathbb { R } ^ { n } ( n \geq 3 )$ and $S : R ^ { n } \to R$ is a smooth function $[ \mathrm { B r i 9 7 } , \mathrm { B D 0 1 } ]$ . We call the above-mentioned system a multisymplectic Hamiltonian system, since it possesses a multisymplectic conservation law

$$
\frac { \partial } { \partial t } \omega + \frac { \partial } { \partial x } \kappa = 0 ,
$$

where $\omega$ and $\kappa$ are the presymplectic forms

$$
\omega = \frac { 1 } { 2 } \mathsf { d } z \wedge M \mathsf { d } z , \quad \kappa = \frac { 1 } { 2 } \mathsf { d } z \wedge K \mathsf { d } z .
$$

The constructed action functional is

$$
S = \int { \Bigl ( } { \frac { 1 } { 2 } } z ^ { \operatorname { T } } ( M z _ { t } + K z _ { x } ) - H ( z ) { \Bigr ) } \mathrm { d } x \wedge \mathrm { d } t .
$$

Performing total variation on (2.77), we can obtain the multisymplectic Hamiltonian system (2.75), the corresponding local energy conservation law

$$
\frac { \partial } { \partial t } \Bigl ( S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { x } \Bigr ) + \frac { \partial } { \partial x } \Bigl ( \frac { 1 } { 2 } z ^ { \mathrm { T } } K z _ { t } \Bigr ) = 0 ,
$$

and the local momentum conservation law

$$
\frac { \partial } { \partial t } \Big ( \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { x } \Big ) + \frac { \partial } { \partial x } \Big ( S ( z ) - \frac { 1 } { 2 } z ^ { \mathrm { T } } M z _ { t } \Big ) = 0 .
$$

In the same way, we can develop a discrete total variation in the multisymplectic form and obtain multisymplectic-energy-momentum integrators. This will be discussed in detail in Chapter 16.