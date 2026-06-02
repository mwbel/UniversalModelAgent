# Chapter IV. Stiff Problems - One-Step Methods

This chapter introduces stiff (styv (Swedish first!), steif (German), stif (Islandic), stijf (Dutch), raide (French), rigido (Spanish), rigido (Portuguese),stiff (Italian), kankea (Finnish)， δóokαμπTo (Greek)，merev (Hungarian), rigid (Rumanian), tog (Slovenian),vrst (Serbo-Croatian), tuhy (Czecho-Slovakian), sztywny (Polish), jaik (Estonian),stiegrs (Latvian), standus (Lithuanian),stign (Breton), zurrun (Basque)， sert(Turkish)， xkecTky (Russian)，TBbpⅡ(Bulgarian), $\cos \theta \sin \theta$ (Vietnamese), ngumu (Swaheli) ...) differential equations. While the intuitive meaning of stiff is clear to all specialists, much controversy is going on about it's correct mathematical definition (see e.g. p.360-363 of Aiken (1985)). The most pragmatical opinion is also historically the first one (Curtiss & Hirschfelder 1952): stiff equations are equations where certain implicit methods, in particular BDF, perform better, usually tremendously better, than explicit ones. The eigenvalues of the Jacobian $\partial f / \partial y$ play certainly a role in this decision, but quantities such as the dimension of the system, the smoothness of the solution or the integration interval are also important (Sections IV.1 and IV.2).

Stiff equations need new concepts of stability (A-stability, Sect.IV.3) and lead to mathematical theories on order restrictions (order stars, Sect.IV.4). Stiff equa-tions require implicit methods; we therefore focus in Sections IV.5 and IV.6 on implicit Runge-Kutta methods, in IV.7 on (semi-implicit) Rosenbrock methods and in IV.9 on semi-implicit extrapolation methods. The actual efcient implementation of implicit Runge-Kutta methods poses a number of problems which are discussed in Sect. IV.8. Section IV.10 then reports on some numerical experience for all these methods.

With Sections IV.11,IV.12 and IV.13 we begin with the discussion of contractivity ( $B$ -stability) for linear and nonlinear differential equations. The chapter ends with questions of existence and numerical stability of the implicit Runge-Kutta solutions (Sect.IV.14) and a convergence theory which is independent of the stiffness （ $B$ -convergence, Sect.IV.15).

# IV.1 Examples of Stiff Equations

... Around 1960, things became completely different and everyone became aware that the world was fullof stiff problems.

(G.Dahlquist in Aiken 1985)

Stiff equations are problems for which explicit methods don't work. Curtiss & Hirschfelder (1952) explain stiffness on one-dimensional examples such as

$$
y ^ { \prime } = - 5 0 ( y - \cos x ) .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/44294b653f8fe56307ca6a1026d21239ebc909df8a4d72ebc62f24fdf8a08795.jpg)  
Fig. 1.1. Solution curves of (1.1) with implicit Euler solution

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b205967b69c4ec14316e380cdeb5f3881d567844de8882a7c1dd82e5365dad35.jpg)  
Fig.1.2.Explicit Euler for $y ( 0 ) = 0$ ， $h = 1 . 9 7 4 / 5 0$ and 1.875/50

Solution curves of Equation (1.1) are shown in Fig.1.1. There is apparently a smooth solution in the vicinity of $y \approx \cos x$ and all other solutions reach this one after a rapid “transient phase". Such transients are typical of stiff equations, but are neither suficient nor necessary. For example, the solution with initial value $y ( 0 ) =$ 1 (more precisely 2500/2501） has no transient. Fig.1.2 shows Euler polygons for the initial value $y ( 0 ) = 0$ and step sizes $h = 1 . 9 7 4 / 5 0$ (38 steps） and $h =$ 1.875/50 (40 steps)． We observe that whenever the step size is a litle too large (larger than 2/5O),the numerical solution goes too far beyond the equilibrium and violent oscillations occur.

Looking for better methods for differential equations such as (1.1),Curtiss and Hirschfelder discovered the BDF method (see Sect.III.1): the approximation $y \approx \cos x$ (i.e., $f ( x , y ) = 0 { \mathrm { . } }$ ） is only a crude approximation to the smooth solution, since the derivative of cos $\boldsymbol { x }$ is not zero. It is much better, for a given solution value $y _ { n }$ , to search for a point $y _ { n + 1 }$ where the slope of the vector field is directed towards $y _ { n }$ , hence

$$
{ \frac { y _ { n + 1 } - y _ { n } } { h } } = f ( x _ { n + 1 } , y _ { n + 1 } ) .
$$

This is the implicit Euler method. The dotted line in Fig.1.1 consists of three implicit Euler steps and demonstrates impressively the good stability property of this method. Equation (1.1) is thus apparently “stiff” in the sense of Curtiss and Hirschfelder.

Extending the above idea“by taking higher order polynomials to fit $y$ at a large number of points" then leads to the BDF methods.

# Chemical Reaction Systems

When the equations represent the behaviour of a system containing a number of fast and slow reactions,a forward integration of these equations becomes difficult. (H.H. Robertson 1966)

The following example of Robertson's (1966) has become very popular in numerical studies (Willoughby 1974):

$$
\begin{array} { c c c } { { A } } & { { \xrightarrow { 0 . 0 4 } } } & { { B } } \\ { { B + B } } & { { \xrightarrow { 3 \cdot 1 0 ^ { 7 } } } } & { { C + B } } \\ { { B + C } } & { { \xrightarrow { 1 0 ^ { 4 } } } } & { { A + C } } \end{array}
$$

which leads to the equations

$$
\begin{array} { r l r l } & { y _ { 1 } ^ { \prime } = - 0 . 0 4 y _ { 1 } + 1 0 ^ { 4 } y _ { 2 } y _ { 3 } \qquad } & & { y _ { 1 } ( 0 ) = 1 } \\ & { y _ { 2 } ^ { \prime } = } & { 0 . 0 4 y _ { 1 } - 1 0 ^ { 4 } y _ { 2 } y _ { 3 } - 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & & { y _ { 2 } ( 0 ) = 0 } \\ & { y _ { 3 } ^ { \prime } = } & & { 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & & { y _ { 3 } ( 0 ) = 0 . } \end{array}
$$

After a bad experience with explicit Euler just before,let's try a higher order method and a more elaborate code for this example: DOPRI5 (cf. Volume 1). The numerical solutions obtained for $y _ { 2 }$ with $R t o l = 1 0 ^ { - 2 }$ (209 steps) as well as with $R t o l = 1 0 ^ { - 3 }$ (205 steps） and $A t o l = 1 0 ^ { - 6 }$ : Rtol are displayed in Fig.1.3. Fig.1.4 presents the step sizes used by the code and also the local error estimates. There, all rejected steps are crossed out.

We observe that the solution $y _ { 2 }$ rapidly reaches a quasi-stationary position in the vicinity of $y _ { 2 } ^ { \prime } = 0$ ，which in the beginning $( y _ { 1 } = 1 , y _ { 3 } = 0 )$ is at $0 . 0 4 \approx$ $3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 }$ ,hence $y _ { 2 } \approx 3 . 6 5 \cdot 1 0 ^ { - 5 }$ ， and then very slowly goes back to zero again. The numerical method, however, integrates this smooth solution by thousands of apparently unnecessary steps. Moreover, the chosen step sizes are more or less independent of the chosen tolerance. Hence, they seem to be governed by stability rather than by precision requirements. It can also be seen that an implicit Runge-Kutta code (such as RADAU5 described in Sections IV.5 and IV.8) integrates this equation without any problem.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/179eb916c6e4268de22d8a7a879d70ad54b8e2b574c84d3c8a4f3e14996478d8.jpg)  
Fig.1.3.Numerical solution for problem (1.4) with DOPRI5 and RADAU5

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/3c84e187f75a74b3933c539df18becbc972ea161ea81ddd140fc3390a41cb41d.jpg)  
Fig.1.4. Step sizes and local error estimates of DOPRI5, $T o l = 1 0 ^ { - 2 }$

# Electrical Circuits

This behavior is known, at least in part, to any experienced worker in the field. (G. Hall 1985)

One of the simplest nonlinear equations describing a circuit is van der Pol's equation (see Sect.I.16)

$$
\begin{array} { l l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } & { { ~ y _ { 1 } ( 0 ) = 2 } } \\ { { \qquad y _ { 2 } ^ { \prime } = \mu ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \qquad y _ { 2 } ( 0 ) = 0 . } } \end{array}
$$

We have seen in Chapter $\mathbf { I I }$ that this equation is easily integrated for moderate values of $\mu$ . But we now choose $\mu = 5 0 0$ and suspect that the problem might become diffcult. It turns out that the period of the solution increases with $\mu$ We therefore rescale the solutions and introduce $t = x / \mu , z _ { 1 } ( t ) = y _ { 1 } ( x ) , z _ { 2 } ( t ) =$ $\mu y _ { 2 } ( x )$ . In the resulting equation the factor $\mu ^ { 2 }$ multiplies the entire second line of $f$ . Substituting again $y$ for $z , x$ for $t$ and $\mu ^ { 2 } = 1 / \varepsilon$ we obtain

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/779c1627d13137a0cdbd99853768482f5b9d20673573bd9b3d50786610e2a115.jpg)  
Fig.1.5. Numerical solution for DEABM at equation (1.5'), $R t o l = 1 0 ^ { - 2 }$ ， $A t o l = 1 0 ^ { - 7 }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/3fa6edff3026dd77967a4201f0ca269022ca5f52e4ea26de42e9fae1e74a75bb.jpg)  
Fig.1.6. Step sizes and orders for DEABM, $R t o l = 1 0 ^ { - 2 }$ ， $1 0 ^ { - 6 }$ ， $A t o l = 5 \cdot 1 0 ^ { - 8 }$

$$
\begin{array} { l l l } { { y _ { 1 } ^ { \prime } = y _ { 2 } } } & { { \mathrm { ~ o r ~ } } } & { { y _ { 1 } ^ { \prime } = y _ { 2 } } } \\ { { y _ { 2 } ^ { \prime } = \mu ^ { 2 } \big ( ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \big ) } } & { { } } & { { \varepsilon y _ { 2 } ^ { \prime } = ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } . } } \end{array}
$$

The steady-state approximation (see Vol. I, Formula (I.16.5)) then becomes independent of $\mu$

Why not try a multistep code this time? For example the predictor-corrector Adams code DEABM of Shampine & Watts. Figures 1.5 and 1.6 show the numerical solution, the step sizes and the orders for the first 45O steps. Eventually the code stops with the message $I d i d = - 4$ ("the problem appears to be stiff"). The implicit Runge-Kutta code RADAU5 integrates over the same interval in 11 steps.

# Diffusion

Stalling numerical processes must be wrong. (A“golden rule”of Achi Brandt)

Another source of stiffness is the translation of diffusion terms by divided differences (method of lines, see Sect.I.1) into a large system of ODE's. We choose the Brusselator (see (16.12) of Sect.I.16) in one spatial variable $\boldsymbol { \mathscr { x } }$

$$
\begin{array} { l } { \displaystyle \frac { \partial u } { \partial t } = A + { u ^ { 2 } v } - ( B + 1 ) u + \alpha \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial v } { \partial t } = B u - { u ^ { 2 } v } + \alpha \frac { \partial ^ { 2 } v } { \partial x ^ { 2 } } } \end{array}
$$

with $0 \leq x \leq 1 , A = 1 , B = 3 , \alpha = 1 / 5 0$ and boundary conditions

$$
\begin{array} { l l } { { u ( 0 , t ) = u ( 1 , t ) = 1 , } } & { { v ( 0 , t ) = v ( 1 , t ) = 3 , } } \\ { { u ( x , 0 ) = 1 + \sin ( 2 \pi x ) , } } & { { v ( x , 0 ) = 3 . } } \end{array}
$$

We replace the second spatial derivatives by finite differences on a grid of $N$ points $x _ { i } = i / ( N + 1 ) \ ( 1 \leq i \leq N ) , \Delta x = 1 / ( N + 1 )$ and obtain from (1.6)

$$
\begin{array} { r l } & { u _ { \iota } ^ { \prime } = 1 + u _ { \iota } ^ { 2 } v _ { i } - 4 u _ { i } + \displaystyle \frac { \alpha } { ( \Delta x ) ^ { 2 } } ( u _ { i - 1 } - 2 u _ { i } + u _ { \iota + 1 } ) , } \\ & { ~ v _ { i } ^ { \prime } = 3 u _ { \iota } - u _ { i } ^ { 2 } v _ { \iota } + \displaystyle \frac { \alpha } { ( \Delta x ) ^ { 2 } } ( v _ { \iota - 1 } - 2 v _ { i } + v _ { i + 1 } ) , } \\ & { u _ { 0 } ( t ) = u _ { N + 1 } ( t ) = 1 , \quad v _ { 0 } ( t ) = v _ { N + 1 } ( t ) = 3 , } \\ & { u _ { i } ( 0 ) = 1 + \sin ( 2 \pi x _ { \iota } ) , \quad v _ { \iota } ( 0 ) = 3 , \quad i = 1 , \ldots , N . } \end{array}
$$

Table 1.1. Results for (1.6'） with ODEX for $0 \leq t \leq 1 0$   

<table><tr><td>N</td><td>Tol</td><td>accepted steps</td><td>rejected steps</td><td>function calls</td></tr><tr><td>10</td><td>10-4</td><td>21</td><td>3</td><td>365</td></tr><tr><td>20</td><td>10-4</td><td>81</td><td>25</td><td>1138</td></tr><tr><td>30</td><td>10-4</td><td>167</td><td>45</td><td>2459</td></tr><tr><td>40</td><td>10-4</td><td>275</td><td>62</td><td>4316</td></tr><tr><td>40</td><td>10-2</td><td>266</td><td>59</td><td>3810</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/00d6478b51e868a690dfabc6e4b42bbe183fd281cf5759b2c882f7195b7771ee.jpg)  
Fig. 1.7. Solution $u ( x , t )$ of (1.6） with $N = 4 0$ using ODEX

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/eda88a7f7de679c61ece0dd4311e6d83af47d847a99ab0c99e0a9e40ef7e5553.jpg)  
Fig.1.8. Step size and order of ODEX at (1.6') with $N \approx 4 0$

This time we try the extrapolation code ODEX (see Volume I) and integrate over $0 \leq t \leq 1 0$ with $A t o l = R t o l = T o l$ . The number of necessary steps increases curiously with $N$ , as is shown in Table 1.1. Again, for $N$ large, the computing time is nearly independent of the desired tolerance, the computed solutions, however, differ considerably (see Fig.1.7). Even the smooth $1 0 ^ { - 4 }$ -solution shows curious stripes which are evidently unconnected with the behaviour of the solution. Fig.1.8 shows the extremely ragged step size and order changes which take place in this example.

We again have all the characteristics of a “stiff” problem,and the use of an implicit method promises better results. However, when applying such a method, one must carefully take advantage of the banded or sparse structure of the Jacobian matrix. Otherwise the numerical work involved in the linear algebra would increase with $N ^ { 3 }$ , precisely as the work for the explicit method ( $N ^ { 2 }$ for the number of steps and $N$ for the work per step).

# A "Stiff' Beam

Although it is common to talk about “stiff differential equations,” an equation per se is not stiff,a particular initial value problem for that equation may be stiff,in some regions,but the sizes of these regions depend on the initial values and the error tolerance. (C.W. Gear 1982)

Let us conclude our series of examples by a problem from mechanics: the motion of an elastic beam. We suppose the beam inextensible of length 1 and thin. So we neglect shearing forces and rotatory inertia. We further want to allow it arbitrarily large movements. Thus, the most natural coordinate system to use is the angle $\theta$ as a function of arc length $s$ and time $t$ .We further suppose the beam clamped at s=0 andaforce F=(F,F）acting at the free end $s \approx 1$ . The beam is then described by the equations

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/2a7e8fb87e8223bd42a8465e1a0fe247d1a2563abce150deb20a289da21ede81.jpg)

(Drawing by K. Wanner)

$$
x ( s , t ) = \int _ { 0 } ^ { s } \cos \theta ( \sigma , t ) d \sigma ,
$$

$$
y ( s , t ) = \int _ { 0 } ^ { s } \sin \theta ( \sigma , t ) d \sigma .
$$

In order to obtain the equations of motion for this problem, we apply Lagrange theory (Lagrange 1788). This requires that we form $L = T - U$ where $T$ is the kinetic and $U$ the potential energy. For the first of these we have simply

$$
T = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } \Big ( ( \dot { x } ( s , t ) ) ^ { 2 } + ( \dot { y } ( s , t ) ) ^ { 2 } \Big ) d s .
$$

The potential energy is made up of energy from bending (depending on the curvature) and from exterior forces as follows:

$$
U = \frac { 1 } { 2 } \int _ { 0 } ^ { 1 } ( \theta ^ { \prime } ( s , t ) ) ^ { 2 } d s - F _ { x } ( t ) x ( 1 , t ) - F _ { y } ( t ) y ( 1 , t ) .
$$

Here dots and primes denote derivatives with respect to $t$ and $s$ respectively. The equations of motion are now obtained by a “trivial” calculation (we are grateful to our colleague J. Descloux for having shown us how this must be done!） using the Hamilton principle which leads to (see Exercise 2)

$$
\begin{array} { r l r } {  { \int _ { 0 } ^ { 1 } G ( s , \sigma ) \cos \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) \ddot { \theta } ( \sigma , t ) d \sigma } } \\ & { } & { = \theta ^ { \prime \prime } ( s , t ) + \cos \theta ( s , t ) F _ { y } ( t ) - \sin \theta ( s , t ) F _ { x } ( t ) \qquad \quad ( 1 , } \\ & { } & { \quad - \displaystyle \int _ { 0 } ^ { 1 } G ( s , \sigma ) \sin \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) ( \Dot { \theta } ( \sigma , t ) ) ^ { 2 } d \sigma , \quad 0 \le s \le 1 } \end{array}
$$

$$
\theta ( 0 , t ) = 0 , \qquad \theta ^ { \prime } ( 1 , t ) = 0
$$

where

$$
G ( s , \sigma ) = 1 - \operatorname* { m a x } ( s , \sigma )
$$

is Green's function for the problem $- w ^ { \prime \prime } ( s ) = g ( s )$ ， $w ^ { \prime } ( 0 ) = w ( 1 ) = 0$ . If we discretize the integrals with the help of the midpoint rule

$$
\int _ { 0 } ^ { 1 } { f ( \theta ( \sigma , t ) ) d \sigma } = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } f ( \theta _ { k } ) , \qquad \theta _ { k } = \theta \Big ( \big ( k - \frac { 1 } { 2 } \big ) \frac { 1 } { n } , t \Big ) , \qquad k = 1 , \ldots , n - 1 .
$$

Equations (1.10) become

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 1 } ^ { n } a _ { l k } \ddot { \theta } _ { k } = n ^ { 4 } \Big ( \theta _ { l - 1 } - 2 \theta _ { l } + \theta _ { l + 1 } \Big ) + n ^ { 2 } \Big ( \cos \theta _ { l } F _ { y } - \sin \theta _ { l } F _ { x } \Big ) } } \\ { { - \displaystyle \sum _ { k = 1 } ^ { n } g _ { l k } \sin ( \theta _ { l } - \theta _ { k } ) \dot { \theta } _ { k } ^ { 2 } , \qquad l = 1 , \dots , n } } \end{array}
$$

$$
\theta _ { 0 } = - \theta _ { 1 } , \qquad \theta _ { n + 1 } = \theta _ { n }
$$

where

$$
a _ { l k } = g _ { l k } \cos ( \theta _ { l } - \theta _ { k } ) , \qquad g _ { l k } = n + { \frac { 1 } { 2 } } - \operatorname * { m a x } ( l , k ) .
$$

Integration without preparation is frustration.

(Reverend Leon Sullivan)

Numerical integration of (1.10'） seems quite tedious, since the acceleration $\ddot { \theta }$ is only given implicitly. The computation of $\ddot { \theta } _ { k }$ requires the solution of a linear

system $A { \ddot { \theta } } = v$ . Due to the special structure of $A$ , this can be done efficiently, since with $B = \left( b _ { l k } \right) , b _ { l k } = g _ { l k } \sin ( \theta _ { l } - \theta _ { k } )$ , we have

$$
A + i B = \mathrm { d i a g } \Bigl ( e ^ { \imath \theta _ { 1 } } , \ldots , e ^ { \imath \theta _ { n } } \Bigr ) G \mathrm { d i a g } \Bigl ( e ^ { - \imath \theta _ { 1 } } , \ldots , e ^ { - \imath \theta _ { n } } \Bigr ) .
$$

The matrix $G = \left( g _ { l k } \right)$ has the beautiful inverse

$$
G ^ { - 1 } = \left( \begin{array} { c c c c c c } { { 1 } } & { { - 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 2 } } & { { - 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 2 } } & { { - 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } & { { 3 } } \end{array} \right) ,
$$

a positive definite tridiagonal matrix (a natural coincidence: $G ^ { - 1 }$ represents the second order difference operator, and $G$ comes from the Green function for a second order integration problem). Now

$$
( A + i B ) ^ { - 1 } = C + i D = \mathrm { d i a g } \Big ( e ^ { i \theta _ { 1 } } , \ldots , e ^ { \imath \theta _ { n } } \Big ) G ^ { - 1 } \mathrm { d i a g } \Big ( e ^ { - i \theta _ { 1 } } , \ldots , e ^ { - \imath \theta _ { n } } \Big )
$$

and

$$
A C - B D = I , \quad A D + B C = 0
$$

lead to $A ^ { - 1 } = C + D C ^ { - 1 } D$ . We can also simplify the term $- \sum g _ { l k } \sin ( \theta _ { l } -$ $\theta _ { k } ) \dot { \theta } _ { k } ^ { 2 }$ ，which in vector notation is $- B \dot { \theta } ^ { 2 }$ ，with the formula $A ^ { - 1 } B = - D C ^ { - 1 }$ (from (1.17)). The accelerations $\ddot { \theta } _ { k }$ are now obtained from (1.10') as follows.

a)Let $v _ { l } = n ^ { 4 } \big ( \theta _ { l - 1 } - 2 \theta _ { l } + \theta _ { l + 1 } \big ) + n ^ { 2 } \big ( \cos \theta _ { l } F _ { y } - \sin \theta _ { l } F _ { x } \big ) ,$ b) Compute $w = D v + { \dot { \theta } } ^ { 2 }$ （ $D$ is bidiagonal);   
c) Solve the tridiagonal system $C u = w$ ，   
d) Compute $\ddot { \theta } = C v + D u$ .

Thus the evaluation of (1.10') reduces to ${ \mathcal { O } } ( n )$ operations (instead of $\mathcal { O } ( n ^ { 3 } ) )$ .We choose the initial conditions

$$
\theta ( s , 0 ) = 0 , \qquad \dot { \theta } ( s , 0 ) = 0
$$

and apply the exterior forces

$$
F _ { x } = - \varphi ( t ) , \quad F _ { y } = \varphi ( t ) , \qquad \varphi ( t ) = \left\{ { 1 . 5 \cdot \sin ^ { 2 } t } \quad 0 \leq t \leq \pi \right.
$$

The resulting system of ODE's is then integrated for $0 \leq t \leq 5$ by the code DOP853 of Volume I, although strictly speaking, the code is of too high an order for such a problem. The results are summarized in Table 1.2.

We observe the same phenomenon as before, the number of necessary steps increases like $\mathcal { O } ( n ^ { 2 } )$ (the numerical work like $\mathcal { O } ( n ^ { 3 } ) )$ , and is more or less independent of the chosen tolerance. The numerical solution for $n = 4 0$ is displayed in Fig. 1.9. Only each 20th of the nearly 90o0 steps is drawn (otherwise the picture would just be completely black). The computed solution looks perfectly smooth and there is no apparent reason for the need of so many steps. In fact due to lack of stability, the numerical method produces small vibrations which are invisible for $T o l = 1 0 ^ { - 7 }$ ,and which force the integrator to such small step sizes. If we relax the high precision requirement, these oscillations become visible (Fig.1.10).

Table 1.2.Results for the beam (1.10） with DOP853   

<table><tr><td>m</td><td>Tol</td><td>accepted steps</td><td>rejected steps</td><td>function calls</td></tr><tr><td>.5 10 20</td><td>10-7 10-7 10-7</td><td>142 383 1397</td><td>35 26 273</td><td>2091 4884 19769</td></tr><tr><td>40 20 20 20</td><td>10-7 10-3 10-5 10-7</td><td>6913 1486 1967 1397</td><td>1347 450 266 273</td><td>97775 22784 26532 19769</td></tr></table>

# High Oscillations

Let us now choose slightly perturbed initial values in the beam equation (1.10). Instead of (1.18) we put

$$
\theta _ { 1 } = \ldots = \theta _ { n - 1 } = 0 , \theta _ { n } = 0 . 4 , \quad \dot { \theta } _ { 1 } = \ldots = \dot { \theta } _ { n } = 0 .
$$

This time, the correct solution for $n = 1 0$ of（1.10'） computed with $T o l = 1 0 ^ { - 6 }$ and more than 200O steps is displayed in Fig.1.11.

The solution is highly oscillatory, no damping wipes out the fast vibrations since the system is conservative. Hence also an implicit method, if required to follow all these oscillations, would need the same number of steps and there would of course be no advantage in using it. So we see that the decision whether a problem should be regarded as stiff or nonstiff ("... that is the question), may also depend on the chosen initial conditions. On the other hand, we shall see in Sect.IV.2 that whenever these high oscillations are not desired,implicit methods are a marvellous instrument for wiping them out.

# Exercises

1.(Curtiss & Hirschfelder 1952). “It is interesting to notice that this method of integration (the implicit Euler) may be used in either direction”. Integrate equation (1.1) backward with step size $- 0 . 5$ and initial value $y ( 1 . 5 ) = 0$ in three steps. Observe that the numerical solution remains stable and follows the smooth solution.

2. Derive the equations of motion(1.10) for the elastic beam from(1.8) and (1.9).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/6416a5d7910f267093a40a63144e81780c4955fdfb9c151dafab49c1675b8da4.jpg)  
Fig.1.10. DOP853 on the beamwith $T o l = 0 . 0 0 7 5$ ，$n = 2 0$ ， every 5th step drawn.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/7f0b85ca644c9ae00561fdd87e3bcb117896bfba4ae2a329cf452b8c933bc0c3.jpg)  
Fig.1.11. DOP853 on highly oscillatorybeam with $T o l = 0 . 0 0 0 0 0 1$ ，$n = 1 0$ ， every 4th step drawn.

Hint. If you want to avoid differentiation in function spaces, then discretize the beam as, say,

$$
x _ { j } = \Delta s \sum _ { k = 1 } ^ { j } \cos \theta _ { k } , \quad y _ { j } = \Delta s \sum _ { k = 1 } ^ { j } \sin \theta _ { k } , \quad j = 1 , \ldots , n , \Delta s = { \frac { 1 } { n } }
$$

$$
T = \frac { \Delta s } { 2 } \sum _ { \jmath = 1 } ^ { n } \left( \dot { x } _ { \jmath } ^ { 2 } + \dot { y } _ { \jmath } ^ { 2 } \right) = \frac { \Delta s } { 2 } \sum _ { \jmath = 1 } ^ { n } \dot { z } _ { \jmath } \dot { \bar { z } } _ { \jmath } , \qquad z _ { \jmath } = \Delta s \sum _ { k = 1 } ^ { \jmath } e ^ { \imath \theta _ { k } }
$$

$$
U = \frac { \Delta s } { 2 } \sum _ { j = 1 } ^ { n } \Bigl ( \frac { \theta _ { j } - \theta _ { j - 1 } } { \Delta s } \Bigr ) ^ { 2 } - F _ { x } \Delta s \sum _ { k = 1 } ^ { n } \cos \theta _ { k } - F _ { y } \Delta s \sum _ { k = 1 } ^ { n } \sin \theta _ { k } ,
$$

form the Lagrange function $L = T - U$ and apply $n$ -dimensional Lagrange theory (Lagrange (1788)，, Vol. II, Sect. VII and VIII, a very clear derivation can be found in Sommerfeld (1942), Vol. I, $\ S 3 6 )$

$$
{ \frac { d } { d t } } { \Bigl ( } { \frac { \partial L } { \partial { \dot { \theta } } _ { k } } } { \Bigr ) } - { \frac { \partial L } { \partial \theta _ { k } } } = 0
$$

or

$$
\sum _ { l = 1 } ^ { n } L _ { \dot { \theta } _ { k } \dot { \theta } _ { l } } \ddot { \theta } _ { l } = L _ { \theta _ { k } } - L _ { \dot { \theta } _ { k } t } - \sum _ { l = 1 } ^ { n } L _ { \dot { \theta } _ { k } \theta _ { l } } \dot { \theta } _ { l } .
$$

3.Apply an explicit code tothe Oregonator (Chapter I, Equation (16.15))

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = 7 7 . 2 7 \Big ( y _ { 2 } + y _ { 1 } \big ( 1 - 8 . 3 7 5 \times 1 0 ^ { - 6 } y _ { 1 } - y _ { 2 } \big ) \Big ) } \\ { y _ { 2 } ^ { \prime } = \frac { 1 } { 7 7 . 2 7 } ( y _ { 3 } - ( 1 + y _ { 1 } ) y _ { 2 } ) } \\ { y _ { 3 } ^ { \prime } = 0 . 1 6 1 ( y _ { 1 } - y _ { 3 } ) } \end{array}
$$

and study its performance.

4. a) Compute the equations of motion of the hanging rope (Fig.1.12) of length 1 by using the results of Exercise 2. The potential energy has to be replaced by

$$
U = - \int _ { 0 } ^ { 1 } x ( s , t ) d s .
$$

Result.

$$
\begin{array} { l l } { \displaystyle \int _ { 0 } ^ { 1 } G ( s , \sigma ) \cos \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) \ddot { \theta } ( \sigma , t ) d \sigma } & { ( 1 \cdot \frac 1 2 ) } \\ { \displaystyle } & { = - \int _ { 0 } ^ { 1 } G ( s , \sigma ) \sin \big ( \theta ( s , t ) - \theta ( \sigma , t ) \big ) ( \dot { \theta } ( \sigma , t ) ) ^ { 2 } d \sigma - ( 1 - s ) \sin \theta ( s , t ) } \end{array}
$$

for $0 \leq s \leq 1$ , or, when discretized

$$
\sum _ { k = 1 } ^ { n } a _ { l k } \ddot { \theta } _ { k } = - \sum _ { k = 1 } ^ { n } b _ { l k } \dot { \theta } _ { k } ^ { 2 } - n \left( n + \frac { 1 } { 2 } - l \right) \sin \theta _ { l } .
$$

b) Do numerical computations with DOPRI5 or DOP853. Choose as initial po-sition a hanging rope in equilibrium which is then released at one end.

Hint. The hanging rope in equilibrium satisfies, in the usual coordinates,

$$
\int _ { x _ { 0 } } ^ { x _ { 1 } } { y \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } } d x = \mathrm { m i n } \qquad \mathrm { w i t h } \qquad \int _ { x _ { 0 } } ^ { x _ { 1 } } { \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } } d x = 1 ,
$$

which, using a Lagrange multiplier, becomes

$$
\int _ { x _ { 0 } } ^ { x _ { 1 } } ( y - \lambda ) \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } } d x = \mathrm { s t a t } .
$$

Applying (2.6) of Sect.I.2 yields $y - \lambda = K \sqrt { 1 + ( y ^ { \prime } ) ^ { 2 } }$ with solution

$$
y = \lambda + K { \mathrm { c o s h } } \Bigl ( { \frac { x + \alpha } { K } } \Bigr ) .
$$

Suitable choices of the parameters and change of coordinates $\ . \ K = 1 / 2 , \ \lambda =$ $- K \mathrm { c o s h } ( \alpha / K ) , x  y , y  - x )$ then lead to

$$
\theta ( s , 0 ) = \pi / 2 - \arctan ( \sinh ( 2 \alpha ) - 2 s ) .
$$

Result. DOP853 has computed the solution for $0 \leq t \leq 5$ ， $n = 6 0$ and $T o l =$ $1 0 ^ { - 5 }$ ， $\alpha = 0 . 6$ , in 203 steps (Fig.1.12). The number of steps increases here like $\mathcal { O } ( n )$ , so the rope is - evidently -- less stiff than the beam.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/dfff1393fd4453400d84609edde6c638c97cbcc5c2fc6dec9a4bce70e60b2a7f.jpg)  
Fig.1.12. Movement of hanging rope, every step drawn

# IV.2Stability Analysis for Explicit RK Methods

... werden wir bei dem Anfangswertproblem hyperbolischer Gleichungen erkennen, dass die Konvergenz allgemein nur dann vorhanden ist, wenn die Verhältnisse der Gittermaschen in verschiedenen Richtungen gewissen Ungleichungen genuigen.

(Courant, Friedrichs & Lewy 1928)

The first analysis of instability phenomena and step size restrictions for hyperbolic equations was made in the famous paper of Courant, Friedrichs & Lewy (1928). Later,many authors undertook a stability analysis,very often independently,in order to explain the phenomena encountered in the foregoing section. An early and beautiful paper on this subject is Guillou & Lago (1961).

# Stability Analysis for Euler's Method

Let $\varphi ( x )$ be a smooth solution of $y ^ { \prime } = f ( x , y )$ . We linearize $f$ in its neighbourhood as follows

$$
y ^ { \prime } ( x ) = f { \bigl ( } x , \varphi ( x ) { \bigr ) } + { \frac { \partial f } { \partial y } } { \bigl ( } x , \varphi ( x ) { \bigr ) } { \bigl ( } y ( x ) - \varphi ( x ) { \bigr ) } + \ldots
$$

and introduce $y ( x ) - \varphi ( x ) = { \overline { { y } } } ( x )$ to obtain

$$
{ \overline { { y } } } ^ { \prime } ( x ) = { \frac { \partial f } { \partial y } } { \big ( } x , \varphi ( x ) { \big ) } \cdot { \overline { { y } } } ( x ) + \ldots = J ( x ) { \overline { { y } } } ( x ) + \ldots .
$$

As a first approximation we consider the Jacobian $J ( x )$ as constant and neglect the error terms. Omitting the bars we arrive at

$$
y ^ { \prime } = J y .
$$

If we now apply, say, Euler's method to (2.2'), we obtain

$$
y _ { m + 1 } = R ( h J ) y _ { m }
$$

with

$$
R ( z ) = 1 + z .
$$

The behaviour of (2.3) is studied by transforming $J$ to Jordan canonical form (see Sect.I.12). We suppose that $J$ is diagonalizable with eigenvectors $v _ { 1 } , \ldots , v _ { n }$ and write $y _ { 0 }$ in this basis as

$$
y _ { 0 } = \sum _ { i = 1 } ^ { n } \alpha _ { i } v _ { i } .
$$

Inserting this into (2.3) we obtain

$$
y _ { m } = \sum _ { i = 1 } ^ { n } \bigl ( R ( h \lambda _ { i } ) \bigr ) ^ { m } \alpha _ { \iota } \cdot v _ { i } ,
$$

where the $\lambda _ { i }$ are the corresponding eigenvalues (see also Exercises 1 and 2). Clearly $y _ { m }$ remains bounded for $m  \infty$ , if for all eigenvalues the complex number $z = h \lambda _ { i }$ lies in the set

$$
S = \left\{ z \in \mathbb { C } ; | R ( z ) | \leq 1 \right\} = \left\{ z \in \mathbb { C } ; | z - ( - 1 ) | \leq 1 \right\}
$$

which is the circle of radius 1 and centre $- 1$ . This leads to the explanation of the results encountered in Example (1.1). There we have $\lambda = - 5 0$ ,and $h \lambda \in S$ means that $0 \leq h \leq 2 / 5 0$ , in perfect accordance with the numerical observations.

# Explicit Runge-Kutta Methods

An explicit Runge-Kutta method (Sect.II.2, Formula (2.3)) applied to (2.2'） gives

$$
\begin{array} { r } { g _ { \imath } = y _ { m } + h J \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { \imath j } g _ { j } } \\ { y _ { m + 1 } = y _ { m } + h J \displaystyle \sum _ { j = 1 } ^ { s } b _ { \jmath } g _ { \jmath } \ : . } \end{array}
$$

Inserting ${ \mathit { g } } _ { \mathit { j } }$ repeatedly from the first line,this becomes

$$
y _ { m + 1 } = R ( h J ) y _ { m }
$$

where

$$
R ( z ) = 1 + z \sum _ { j } b _ { j } + z ^ { 2 } \sum _ { j , k } b _ { j } a _ { j k } + z ^ { 3 } \sum _ { j , k , l } b _ { j } a _ { j k } a _ { k l } + . . .
$$

is a polynomial of degree $\leq s$ ·

Definition 2.1. The function $R ( z )$ is called the stability function of the method. It can be interpreted as the numerical solution after one step for

$$
y ^ { \prime } = \lambda y , \qquad y _ { 0 } = 1 , \qquad z = h \lambda ,
$$

the famous Dahlquist test equation. The set

$$
S = \left\{ z \in \mathbb { C } \mathrm { ~ } ; \left| R ( z ) \right| \leq 1 \right\}
$$

is called the stability domain of the method.

Theorem 2.2. If the Runge-Kutta method is of order $p$ ,then

$$
R ( z ) = 1 + z + \frac { z ^ { 2 } } { 2 ! } + \ldots + \frac { z ^ { p } } { p ! } + \mathcal { O } ( z ^ { p + 1 } ) .
$$

Proof. The exact solution of (2.9) is $e ^ { z }$ and therefore the numerical solution $y _ { 1 } =$ $R ( z )$ must satisfy

$$
e ^ { z } - R ( z ) = \mathcal { O } ( h ^ { p + 1 } ) = \mathcal { O } ( z ^ { p + 1 } ) .
$$

Another argument is that the expressions in (2.8) appear in the order conditions for the“tall” tres $\tau , t _ { 2 1 } , t _ { 3 2 } , t _ { 4 4 } , t _ { 5 9 } , \ldots .$ (see Table 2.2 of Sect.I1.2,p.148). They are therefore equal to $1 / q !$ for $q \leq p$ □

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/68f82621a7c9622f9e31b2de6b8d05e5fc971de840db8f41c4e50071fb1b4505.jpg)  
Fig.2.1. Stability domains for explicit Runge-Kutta methods of order ${ \mathfrak { p } } = s$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/773a2a6d253c9f21f9d2c990945ffc8a31d122f556604c422c7782f266d46c56.jpg)  
Fig.2.2. Stability domains for DOPRI methods

As a consequence, all explicit Runge-Kutta methods with $p = s$ possess the stability function

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 ! } } + . . . + { \frac { z ^ { s } } { s ! } } .
$$

The corresponding stability domains are represented in Fig.2.1.

The method of Dormand & Prince DOPRI5 (Sect.II.5, Table 5.2) is of order 5 with $s = 6$ (the 7th stage is for error estimation only). Here $R ( z )$ is obtained by direct computation. The result is

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 2 0 } } + { \frac { z ^ { 6 } } { 6 0 0 } } .
$$

For DOP853 (Sect.II.5,Fig.5.3), $R ( z )$ becomes

$$
\begin{array} { c } { { R ( z ) = \displaystyle { \sum _ { j = 0 } ^ { 8 } \frac { z ^ { \prime } } { j ! } } + 2 . 6 9 1 6 9 2 2 0 0 1 6 9 1 \cdot 1 0 ^ { - 6 } z ^ { 9 } + 2 . 3 4 1 3 4 5 1 0 8 2 0 9 8 \cdot 1 0 ^ { - 7 } z ^ { 1 0 } } } \\ { { + 1 . 4 9 4 7 3 6 4 8 5 4 5 9 2 \cdot 1 0 ^ { - 8 } z ^ { 1 1 } + 3 . 6 1 3 3 2 4 5 7 8 1 2 8 2 \cdot 1 0 ^ { - 1 0 } z ^ { 1 2 } } } \end{array}
$$

The stability domains for these two methods are given in Fig. 2.2.

# Extrapolation Methods

The GBS-algorithm (see Sect.I1.9, Formulas (9.10), (9.13)) applied to $y ^ { \prime } = \lambda y$ ， $y ( 0 ) = 1$ leads with $z = H \lambda$ to

$$
\begin{array} { r l } & { \quad y _ { 0 } = 1 , \quad \quad y _ { 1 } = 1 + \frac { z } { n _ { _ { J } } } } \\ & { } \\ & { \quad y _ { i + 1 } = y _ { i - 1 } + 2 \frac { z } { n _ { _ { J } } } y _ { \imath } \qquad i = 1 , 2 , \ldots , n _ { j } } \\ & { } \\ & { \quad { \cal T } _ { \jmath ^ { \mathrm { I } } } = \frac { 1 } { 4 } ( y _ { n _ { \jmath } - 1 } + 2 y _ { n _ { \jmath } } + y _ { n _ { \jmath } + 1 } ) } \\ & { } \\ & { { \cal T } _ { j , k + 1 } = { \cal T } _ { \jmath , k } + \frac { { \cal T } _ { j , k } - { \cal T } _ { \jmath - 1 , k } } { ( n _ { j } / n _ { j - k } ) ^ { 2 } - 1 } . } \end{array}
$$

The stability domains for the diagonal terms $T _ { 2 2 } , T _ { 3 3 } , T _ { 4 4 }$ , and $T _ { 5 5 }$ for the harmonic sequence

$$
\{ n _ { \jmath } \} = \{ 2 , 4 , 6 , 8 , 1 0 , . . . \}
$$

(the one which is used in ODEX) are displayed in Fig.2.3. We have also added those for the methods without the smoothing step (II.9.13c),which shows some difference for negative real eigenvalues.

# Analysis of the Examples of IV.1

The Jacobian for the Robertson reaction (1.3) is given by

$$
\left( \begin{array} { c c c } { { - 0 . 0 4 } } & { { 1 0 ^ { 4 } y _ { 3 } } } & { { 1 0 ^ { 4 } y _ { 2 } } } \\ { { 0 . 0 4 } } & { { - 1 0 ^ { 4 } y _ { 3 } - 6 \cdot 1 0 ^ { 7 } y _ { 2 } } } & { { - 1 0 ^ { 4 } y _ { 2 } } } \\ { { 0 } } & { { 6 \cdot 1 0 ^ { 7 } y _ { 2 } } } & { { 0 } } \end{array} \right)
$$

which in the neighbourhood of the equilibrium $y _ { 1 } = 1$ ， $y _ { 2 } = 0 . 0 0 0 0 3 6 5$ ， $y _ { 3 } = 0$ is

$$
\left( \begin{array} { c c c } { { - 0 . 0 4 } } & { { 0 } } & { { 0 . 3 6 5 } } \\ { { 0 . 0 4 } } & { { - 2 1 9 0 } } & { { - 0 . 3 6 5 } } \\ { { 0 } } & { { 2 1 9 0 } } & { { 0 } } \end{array} \right)
$$

with eigenvalues

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/ce2aa538e99391fe27daadcf4fbc118953c29ddbd0e3b130e69e4c36d754dbc6.jpg)  
Fig. 2.3. Stability domains for GBS extrapolation methods

$$
\lambda _ { 1 } = 0 , \quad \lambda _ { 2 } = - 0 . 4 0 5 , \quad \lambda _ { 3 } = - 2 1 8 9 . 6 .
$$

The third one produces stiffness. For stability we need (see the stability domain of DOPRI5 in Fig. 2.2) $- 2 1 9 0 h \ge - 3 . 3$ , hence $h \leq 0 . 0 0 1 5$ . This again confirms the numerical observations.

The Jacobian of example (1.6') (Brusselator reaction with diffusion) is a large $2 N \times 2 N$ matrix. It is composed of reaction terms and diffusion terms:

$$
J = \left( \begin{array} { c c } { \mathrm { d i a g } ( 2 u _ { i } v _ { \ i } - 4 ) } & { \mathrm { ~ } \mathrm { d i a g } ( u _ { i } ^ { 2 } ) } \\ { \mathrm { d i a g } ( 3 - 2 u _ { i } v _ { i } ) } & { \mathrm { ~ } \mathrm { d i a g } ( - u _ { i } ^ { 2 } ) } \end{array} \right) + \frac { \alpha } { ( \Delta x ) ^ { 2 } } \left( \begin{array} { c c } { K } & { 0 } \\ { 0 } & { K } \end{array} \right)
$$

where

$$
K = \left( \begin{array} { c c c c c c } { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { - 2 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - 2 } } \end{array} \right) \ .
$$

The eigenvalues of $\kappa$ are known (see Sect.I.6,Formula (6.7b)), namely

$$
\mu _ { k } = - 4 { \left( \sin { \frac { \pi k } { 2 N + 2 } } \right) } ^ { 2 } ,
$$

and therefore the double eigenvalues of the right hand matrix in (2.16) are

$$
- \frac { 4 \alpha } { ( \Delta x ) ^ { 2 } } \Big ( \sin \frac { \pi k } { 2 N + 2 } \Big ) ^ { 2 } = - 4 \alpha \big ( N + 1 \big ) ^ { 2 } \Big ( \sin \frac { \pi k } { 2 N + 2 } \Big ) ^ { 2 } ,
$$

and are located between $- 4 \alpha ( N + 1 ) ^ { 2 }$ and O. Since this matrix is symmetric, its eigenvalues are wel conditioned and the first matrix on the right side of (2.16) with much smaller coefficients can be regarded as a small perturbation. Therefore the eigenvalues of $J$ in (2.16) will remain close to those of the unperturbed matrix and lie in a stripe neighbouring the interval $[ - 4 \alpha ( N + 1 ) ^ { 2 } , 0 ]$ . Numerical computations for $N = 4 0$ show for example that the largest negative eigenvalue of $J$ varies between $- 1 3 3 . 3$ and -134.9,while the unperturbed value is $- 4 \cdot 4 1 ^ { 2 } \cdot \sin ^ { 2 } ( 4 0 \pi / 8 2 ) / 5 0 = - 1 3 4 . 2 8$ ． Since most stability domains for ODEX end close to $- 5 . 5$ on the real axis (Fig.2.3), this leads for $N = 4 0$ to $h \leq 0 . 0 4$ and the number of steps must be $\geq 2 5 0$ (compare with Table 1.1).

In order to explain the behaviour of the beam equation, we linearize it in the neighbourhood of the solution ${ \theta } _ { k } = \dot { \theta } _ { k } = 0 , F _ { x } = \dot { F _ { y } } = 0$ . There (1.10') becomes

$$
G \ddot { \theta } = n ^ { 4 } \left( \begin{array} { c c c c c c } { { - 3 } } & { { 1 } } & { { } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { - 2 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { - 2 } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - 1 } } \end{array} \right) \theta ,
$$

since for $\theta = 0$ we have $A = G$ and $B = 0$ . We now insert $G ^ { - 1 }$ from (1.16) and observe that the matrices involved are, with the exception of two elements, equal to $\pm K$ of (2.17). We therefore approximate (2.20) by

$$
\ddot { \theta } = - n ^ { 4 } K ^ { 2 } \theta .
$$

This second order equation was integrated in IV.1 as a first order system

$$
\left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) ^ { \cdot } = \left( \begin{array} { c c } { 0 } & { I } \\ { - n ^ { 4 } K ^ { 2 } } & { 0 } \end{array} \right) \left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) = E \left( \begin{array} { c } { \theta } \\ { \dot { \theta } } \end{array} \right) .
$$

By solving

$$
\left( \begin{array} { c c } { { 0 } } & { { I } } \\ { { - n ^ { 4 } K ^ { 2 } } } & { { 0 } } \end{array} \right) \left( \begin{array} { l } { { y } } \\ { { z } } \end{array} \right) = \lambda \left( \begin{array} { l } { { y } } \\ { { z } } \end{array} \right) ,
$$

we find that $\lambda$ is an eigenvalue of $E$ iff $\lambda ^ { 2 }$ is an eigenvalue of $- n ^ { 4 } K ^ { \tilde { 2 } 2 }$ .Thus Formula (2.18) shows that the eigenvalues of $E$ are situated on the imaginary axis between $- 4 n ^ { 2 } i$ and $+ 4 n ^ { 2 } i$ . We see from Fig.2.2 that the stability domain of DOP853 covers the imaginary axis between approximately $- 6 i$ and $+ 6 i$ . Hence for stability we need $h \leq 1 . 5 / n ^ { 2 }$ and the number of steps for the interval $0 \leq$ $t \leq 5$ must be larger than $\approx 1 0 n ^ { 2 } / 3$ . This,again,was observed in the numerical calculations (Table 1.2).

# Automatic Stiffness Detection

Neither is perfect, but even an imperfect test can be quite useful, as we can show from experience ... (L.F. Shampine 1977)

Explicit codes applied to stiff problems are apparently not very efficient and the remaining part of the book will be devoted to the construction of more stable algorithms. In order to avoid that an explicit code waste too much effort when encountering stiffness (and to enable a switch to a more suitable method), it is important that the code be equipped with a cheap means of detecting stiffness. The analysis of the preceding subsection demonstrates that, whenever a nonstiff code encounters stiffness, the product of the step size with the dominant eigenvalue of the Jacobian lies near the border of the stability domain. We shall show two manners of exploiting this observation to detect stiffness.

Firstly,we adapt the ideas of Shampine & Hiebert (1977) to the Dormand & Prince method of order 5(4), given in Table I.5.2. The method possesses an error estimator $e r r _ { 1 } = y _ { 1 } - \widehat { y } _ { 1 }$ which, in the nonstiff situation, is $\mathcal { O } ( h ^ { 5 } )$ . However in the stiff case,when the method is working near the border of the stability domain $S$ , the distance $d _ { 1 } = y _ { 1 } - y ( x _ { 0 } + h )$ to the smooth solution is approximately $d _ { \mathbf { \scriptscriptstyle 1 } } \approx R ( h J ) d _ { 0 }$ ,where $J$ denotes the Jacobian of the system, $R ( z )$ is the stability function of the method, and $d _ { 0 } = y _ { 0 } - y ( x _ { 0 } )$ . Here we have neglected the local error for an initial value on the smooth solution $y ( x )$ ．A similar formula, with $R$ replaced by $\widehat { R }$ , holds for the embedded method. The error estimator satisfies $e r r _ { 1 } \approx E ( h J ) d _ { 0 }$ with $E ( z ) = R ( z ) - \widehat { R } ( z )$ . The idea is now to search for a second error estimator $\widetilde { e r r } _ { 1 }$ (with $\widetilde { e r r } _ { 1 } \approx \widetilde { E } ( h J ) d _ { 0 } )$ such that

i) $| \widetilde { E } ( z ) | \leq \theta | E ( z ) |$ on $\partial S \cap \mathbb { C } ^ { - }$ with a small $\theta < 1$ ； ii) $\widetilde { e r r } _ { 1 } = \mathcal { O } ( h ^ { 2 } )$ for $h  0$ ·

Condition (i) implies that $\| \widetilde { e r r } _ { 1 } \| < \| e r r _ { 1 } \|$ when $h \lambda$ is near $\partial S$ (the problem is possibly stiff),and condition (ii) will lead to $\| \widetilde { e r r } _ { 1 } \| \gg \| e r r _ { 1 } \|$ for step sizes which are determined by accuracy requirements (when the problem is not stiff). If $\| \widetilde { e r r } _ { 1 } \| < \| e r r _ { 1 } \|$ occurs several times in succession (say 15 times) then a stiff code might be more efficient.

For the construction of $\widetilde { e r r } _ { 1 }$ we put $\widetilde { e r r } _ { 1 } = h ( d _ { 1 } k _ { 1 } + d _ { 2 } k _ { 2 } + . . . + d _ { s } k _ { s } )$ , where the $k _ { i } = f ( x _ { 0 } + c _ { \ i } h , g _ { i } )$ are the available function values of the method. The coefficients $d _ { \imath }$ are determined in such a way that

$$
\sum _ { i = 1 } ^ { s } d _ { i } = 0 , \qquad \sum _ { i = 1 } ^ { s } d _ { i } c _ { i } = 0 . 0 2
$$

(so that (ii) holds) and that $\theta$ in (i) is minimized.A computer search gave values which have been rounded to

$$
\begin{array} { r l } & { d _ { 1 } = - 0 . 0 8 5 3 6 , \quad d _ { 2 } = 0 . 0 8 8 , \quad d _ { 3 } = - 0 . 0 0 9 6 , } \\ & { d _ { 4 } = 0 . 0 0 5 2 , \quad d _ { 5 } = 0 . 0 0 5 7 6 , \quad d _ { 6 } = - 0 . 0 0 4 . } \end{array}
$$

The factor O.02 in (2.24) has been chosen such that $\theta$ in (i) is close to 0.3 on large parts of the border of $S$ ,but $\vert \widetilde { E } ( z ) / E ( z ) \vert$ soon becomes larger than 1 if $z$ approaches the origin.

In Fig. 2.4 we present the contour lines $| \widetilde { E } ( z ) / E ( z ) | = C o n s t \ : ( C o n s t = 4 , 2 , 1$ ， 0.5,0.3, 0.2,0.14,0.1) together with the stability domain of the method. A numerical experiment is illustrated in Fig.2.5. We applied the code DOPRI5 (see the Appendix to Volume I) to the van der Pol equation (1.5') with $\varepsilon = 0 . 0 0 3$ . The upper picture shows the first component of the solution, the second picture displays the quotient $\| \widetilde { e r r } _ { 1 } \| / \| e r r _ { 1 } \|$ for the three tolerances $T o l = 1 0 ^ { - 3 }$ ， $1 0 ^ { - 5 } , 1 0 ^ { - 7 }$ . The last picture is a plot of $h | \lambda | / 3 . 3$ where $h$ is the current step size and $\lambda$ the dominant eigenvalue of the Jacobian and 3.3 is the approximate distance of $\partial S$ to the origin.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/6bbb4dc1df9d7cae18242618340b484e83ab40712d0fca1e30780abf1e8fecce.jpg)

A second possibility for detecting stiffness is to estimate directly the dominant eigenvalue of the Jacobian of the problem. If $v$ denotes an approximation to the corresponding eigenvector with $\{ \{ v \} \}$ sufficiently small then, by the mean value theorem,

$$
| \lambda | \approx { \frac { \| f ( x , y + v ) - f ( x , y ) \| } { \| v \| } }
$$

will be a good approximation to the leading eigenvalue. For the Dormand & Prince method (Table II.5.2) we have $c _ { 6 } = c _ { 7 } = 1$ . Therefore, a natural choice is

$$
\varrho = \frac { \| k _ { 7 } - k _ { 6 } \| } { \| g _ { 7 } - g _ { 6 } \| }
$$

where $k _ { i } = f ( x _ { 0 } + c _ { i } h , g _ { i } )$ are the function values of the current step. Both values, $g _ { 7 } = y _ { 1 }$ and $g _ { 6 }$ , approximate the exact solution $y ( x _ { 0 } + h )$ and it can be shown by Taylor expansion that $g _ { 7 } - g _ { 6 } = \mathcal { O } ( h ^ { 3 } )$ . This difference is thus sufficiently small, in general. The same argument also shows that $g _ { 7 } - g _ { 6 } = \widetilde { E } ( h J ) d _ { 0 }$ ，where $J$ is the Jacobian of the linearized differential equation and $\tilde { E } ( z )$ is a polynomial with subdegree 4. Hence, $g _ { 7 } - g _ { 6 }$ is essentially the vector obtained by 4 iterations of the power method applied to the matrix $h J$ . It will be a good approximation to the eigenvector corresponding to the leading eigenvalue. As in the above numerical experiment we applied the code DOPRI5 to the van der Pol equation (1.5'） with $\varepsilon = 0 . 0 0 3$ . Fig. 2.6 presents a plot of $h \varrho / 3 . 3$ where $h$ is the current step size and $\varrho$ the estimate (2.26). This is in perfect agreement with the exact values $h | \lambda | / 3 . 3$ (see third picture of Fig. 2.5).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/e145daf6d476499eb7d7f6b75169547b6dbac0d2e82aeffdce2d14a137297be9.jpg)  
Fig. 2.5. Stiffness detection with DOPRI5

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/74a3ef128c2ada547c01b14f908378f4bffe46f4570da001b2b60052d43c566a.jpg)  
Fig. 2.6. Estimation of Lipschitz constant with DOPRI5

Further numerical examples have shown that the estimate (2.26) also gives satisfactory approximations of $| \lambda |$ when the dominant eigenvalue $\lambda$ is complex. However, if the argument of $\lambda$ is needed too, one can extend the power method as proposed by Wilkinson (1965, page 579). This has been elaborated by Sottas (1984) and Robertson (1987).

The two techniques above allow us to detect the regions where the step size is restricted by stability. In order to decide whether a stiff integrator will be more efficient,one has to compare the expense of both methods. Studies on this question have been undertaken in Petzold (1983), Sottas (1984) and Butcher (1990).

# Step-Control Stability

We now come to the explanation of another phenomenon encountered in Sect. IV.1, that of the ragged behaviour of the step size (e.g. Fig.1.4 or 1.8),a research initiated by G.Hall (1985/86) and continued by G. Hall & D.J. Higham (1988). Do there exist methods or stiff equations for which the step sizes $h _ { n }$ behave smoothly and no frequent step rejections appear?

We make a numerical study on the equation

$$
\begin{array} { r l r } & { \boldsymbol { y } _ { 1 } ^ { \prime } = - 2 0 0 0 \left( \quad \cos x \cdot \boldsymbol { y } _ { 1 } + \sin x \cdot \boldsymbol { y } _ { 2 } + 1 \right) \quad } & { \boldsymbol { y } _ { 1 } ( 0 ) = 1 } \\ & { \boldsymbol { y } _ { 2 } ^ { \prime } = - 2 0 0 0 \left( - \sin x \cdot \boldsymbol { y } _ { 1 } + \cos x \cdot \boldsymbol { y } _ { 2 } + 1 \right) \quad } & { \boldsymbol { y } _ { 2 } ( 0 ) = 0 } \end{array}
$$

for $0 \leq x \leq 1 . 5 7$ ，whose eigenvalues move slowly on a large circle from $- 2 0 0 0$ to $\pm 2 0 0 0 i$ . If we apply Fehlberg's method RKF5(4) (Table II.5.1) in local extrapolation mode (i.e.，we continue the integration with the higher order result） and DOPRI5 to this equation (with Euclidean error norm without scaling),we obtain the step size behaviour presented in Fig.2.7. There all rejected steps are crossed out (3 rejected steps for RKF5(4) and 104 for DOPRI5.

In order to explain this behaviour,we consider for $y ^ { \prime } = \lambda y$ (of course!） the numerical process

$$
\begin{array} { l } { { \displaystyle y _ { n + 1 } = R ( h _ { n } \lambda ) y _ { n } } } \\ { { \displaystyle e r r _ { n } = E ( h _ { n } \lambda ) y _ { n } } } \\ { { \displaystyle h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { \alpha } } } \end{array}
$$

(where $e r r _ { n }$ is the estimated error, $E ( z ) = \widehat { R } ( z ) - R ( z )$ ， $\alpha = 1 / ( \widehat { p } + 1 )$ and $\widehat { p }$ is the order of $\widehat { R }$ ) as a dynamical system whose fixed points and stability we have to study. A possible safety factor ("fac” of formula (4.13) of Sect.II.4) can easily be incorporated into $T o l$ and does not affect the theory. The analysis simplifies if we introduce logarithms

$$
\eta _ { n } = \log | y _ { n } | , \qquad \chi _ { n } = \log h _ { n }
$$

so that (2.28) becomes

$$
\begin{array} { r l } & { \eta _ { n + 1 } = \log | R ( e ^ { \chi _ { n } } \lambda ) | + \eta _ { n } , } \\ & { \chi _ { n + 1 } = \alpha \Big ( \gamma - \log | E ( e ^ { \chi _ { n } } \lambda ) | - \eta _ { n } \Big ) + \chi _ { n } , } \end{array}
$$

where $\gamma$ is a constant. This is now a map $\mathbb { R } ^ { 2 } \to \mathbb { R } ^ { 2 }$ . Its fixed point $( \eta , \chi )$ satisfies

$$
| R ( e ^ { \chi } \lambda ) | = 1 ,
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/204cb60bb5e9a21b0c6cc9691323b02416b8cf43902e34ed977f442f07518f4d.jpg)  
Fig. 2.7. Step sizes of RKF5(4) and DOPRI5 for (2.27)

which determines the step size $e ^ { x }$ so that the point $z = e ^ { x } \lambda$ must be on the border of the stability domain. Further

$$
\eta = \gamma - \log | E ( z ) |
$$

determines $\eta$ . Now the Jacobian of the map (2.30) at this fixed point becomes

$$
C = \frac { \partial ( \eta _ { n + 1 } , \chi _ { n + 1 } ) } { \partial ( \eta _ { n } , \chi _ { n } ) } = \left( \begin{array} { c c } { { 1 } } & { { u = \mathrm { R e } \left( \displaystyle \frac { R ^ { \prime } ( z ) } { R ( z ) } \cdot z \right) } } \\ { { - \alpha } } & { { 1 - \alpha v } } \end{array} \right) \qquad \begin{array} { l } { { u = \mathrm { R e } \left( \displaystyle \frac { R ^ { \prime } ( z ) } { R ( z ) } \cdot z \right) } } \\ { { v = \mathrm { R e } \left( \displaystyle \frac { E ^ { \prime } ( z ) } { E ( z ) } \cdot z \right) . } } \end{array}
$$

Proposition 2.3. The step-control mechanism is stable for $h \lambda = z$ on the boundary of the stability domain if and only if the spectral radius of $C$ in (2.32) satisfies

$$
\varrho ( C ) < 1 .
$$

We then call the method $S C$ -stable at $z$

The matrix $C$ is independent of the given differential equation and of the given tolerance. It is therefore a characteristic of the numerical method and the boundary of its stability domain. Let us study some methods of Sect.II.5. a) RKF4(5) (Table 5.1), $\alpha = 1 / 5$ ：

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 0 4 } } , \quad E ( z ) = { \frac { z ^ { 5 } } { 7 8 0 } } - { \frac { z ^ { 6 } } { 2 0 8 0 } } .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/54553e8f38e90df7af204125a4f4ebcc0ab204b5435c8a8dd7774f87ed6cbee6.jpg)  
Fig. 2.8. Regions of step-control stability

b) DOPRI5 (Table 5.2), $\alpha = 1 / 5$ ：

$$
R ( z ) = \sec ( 2 . 1 3 ) , ~ E ( z ) = { \frac { 9 7 } { 1 2 0 0 0 0 } } z ^ { 5 } - { \frac { 1 3 } { 4 0 0 0 0 } } z ^ { 6 } + { \frac { 1 } { 2 4 0 0 0 } } z ^ { 7 }
$$

c) RKF5(4) (Table 5.1, with local extrapolation), $\alpha = 1 / 5$ ：

$$
R ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + { \frac { z ^ { 3 } } { 6 } } + { \frac { z ^ { 4 } } { 2 4 } } + { \frac { z ^ { 5 } } { 1 2 0 } } + { \frac { z ^ { 6 } } { 2 0 8 0 } }
$$

d) HIHA5 (Method of Higham & Hall,see Table 2.1 below), $\alpha = 1 / 5$ ：

$$
\begin{array} { l } { { \displaystyle R ( z ) = 1 + z + \frac { z ^ { 2 } } { 2 } + \frac { z ^ { 3 } } { 6 } + \frac { z ^ { 4 } } { 2 4 } + \frac { z ^ { 5 } } { 1 2 0 } + \frac { z ^ { 6 } } { 1 4 4 0 } \ : , } } \\ { { \displaystyle E ( z ) = - \frac { 1 } { 1 2 0 0 } z ^ { 5 } + \frac { 1 } { 2 4 0 0 } z ^ { 6 } + \frac { 1 } { 1 4 4 0 0 } z ^ { 7 } } } \end{array}
$$

The corresponding stability domains are represented in Fig.2.8. There, the regions of the boundary, for which $\varrho ( C ) < 1$ is satisfied,are represented as thick lines. It can be observed that the phenomena of Fig.2.7,as well as those of Sect. IV.1, are nicely verified.

DOP853. The step size control of the code DOP853 (Volume I) is slightly more complicated. It is based on a “stretched” error estimator (see Sect.II.1O) and, for the test equation $y ^ { \prime } = \lambda y$ , it is equivalent to replacing $| E ( z ) |$ of (2.30) by

$$
| E ( z ) | = \frac { | E _ { 5 } ( z ) | ^ { 2 } } { \sqrt { | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 \cdot | E _ { 3 } ( z ) | ^ { 2 } } } ,
$$

where $E _ { 3 } ( z ) = \widehat { R } _ { 3 } ( z ) - R ( z ) , E _ { 5 } ( z ) = \widehat { R } _ { 5 } ( z ) - R ( z )$ ,and $\widehat { R } _ { 3 } ( z ) , \widehat { R } _ { 5 } ( z )$ are the stability functions of third and fifth order embedded methods, respectively. The above analysis is still valid if the expression $v$ of (2.32) is replaced by the derivative

<table><tr><td>0</td><td colspan="6"></td></tr><tr><td>2-91-3１-23-5</td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1-8</td><td>0</td><td>38</td><td></td><td></td><td></td></tr><tr><td></td><td>91</td><td>27</td><td>78</td><td>8</td><td></td><td></td></tr><tr><td></td><td>500</td><td>100</td><td>125</td><td>125</td><td></td><td></td></tr><tr><td>1</td><td>11 1</td><td>27</td><td>1</td><td>36</td><td>5</td><td></td></tr><tr><td></td><td>20</td><td>20</td><td></td><td></td><td>125</td><td></td></tr><tr><td>1</td><td>12</td><td>0</td><td>2</td><td>4</td><td>96</td><td>48</td></tr><tr><td></td><td></td><td></td><td>27</td><td></td><td>125</td><td></td><td></td></tr><tr><td>y1</td><td>R</td><td>0</td><td>32</td><td>43</td><td>96</td><td>5-481-24</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td>1</td></tr><tr><td>?</td><td></td><td>0</td><td>2</td><td>15</td><td>2</td><td></td><td>10</td></tr></table>

of $\log | E ( e \boldsymbol { x } \lambda ) |$ with respect to $\chi$ , which is

$$
v = 2 v _ { 5 } - \frac { v _ { 5 } | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 v _ { 3 } | E _ { 3 } ( z ) | ^ { 2 } } { | E _ { 5 } ( z ) | ^ { 2 } + 0 . 0 1 | E _ { 3 } ( z ) | ^ { 2 } } ,
$$

where $v _ { 5 } = \mathrm { R e } \left( z E _ { 5 } ^ { \prime } ( z ) / E _ { 5 } ( z ) \right)$ and $v _ { 3 } = \mathrm { R e } \left( z E _ { 3 } ^ { \prime } ( z ) / E _ { 3 } ( z ) \right)$ . Since $| { \cal E } ( z ) | =$ ${ \mathcal { O } } ( | z | ^ { 8 } )$ for $| z | \to 0$ , we have to use the value $\alpha = 1 / 8$ in (2.32). The regions of $S C$ -stability are shown in Fig.2.8.

SC-Stable Dormand and Prince Pairs of Order 5. We see from Fig.2.8 that the method DOPRI5 is not $S C$ -stable at the intersection of the real axis with the boundary of the stability region. We are therefore interested in finding 5(4)-th order explicit Runge-Kutta pairs from the family of Dormand & Prince (198O) with larger regions of $S C$ -stability.

Requiring the simplifying assumption (I.5.15),Algorithm 5.2 of Sect.II.5 yields a class of Runge-Kutta methods with $c _ { 3 } , c _ { 4 } , c _ { 5 }$ as free parameters. Higham & Hall (199o) have made an extensive computer search for good choices of these parameters in order to have a reasonable size of the stability domain,large parts of $S C$ -stability and a small 6th order error constant. It turned out that the larger one wants the region of $S C$ -stability, the larger the error constant becomes. A compromise choice between Scylla and Charybdis,which in addition yields nice rational coefficients, is given by $c _ { 3 } = 1 / 3$ ， $c _ { 4 } = 1 / 2$ and $c _ { 5 } = 3 / 5$ . This then leads to the method of Table 2.1 which has satisfactory stability properties as can be seen from Fig. 2.8.

# A PI Step Size Control

We saw that it was an I-controler ... and a control-man knows that PI is always better than I ..

(K. Gustafsson, June 1990)

In 1986/87 two students of control theory attended a course of numerical analysis at the University of Lund. The outcome of this contact was the idea to resolve the above instability phenomena in stiff computations by using the concept of “PID control'(Gustafsson,Lundh & Soderlind 1988). The motivation for PID control, a classic in control theory (Callender,Hartree & Porter 1936) is as follows:

Suppose we have a continuous-time control problem where $\theta ( t )$ is the departure, at time $t$ , of a quantity to be controlled from its normal value. Then one might suppose that

$$
{ \dot { \theta } } ( t ) = C ( t ) - m \theta ( t )
$$

where $C ( t )$ denotes the effect of the control and the term $- m \theta ( t )$ represents a self-regulating effect such as $\mathbf { \sp { 6 6 } _ { 2 } }$ vessel in a constant temperature bath". The most simple assumption for the control would be

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t )
$$

which represents, say, a valve opened or closed in dependence of $\theta$ . The equations (2.39) and (2.40) together lead to

$$
{ \ddot { \theta } } + m { \dot { \theta } } + n _ { 1 } \theta = 0
$$

which, for $n _ { 1 } > 0$ ， $m > 0$ , is always stable. If, however, we assume (more realis-tically) that our system has some time-lag, we must replace (2.40) by

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t - T )
$$

and the stability of the process may be destroyed. This is precisely the same effect as the instability of Equation (17.6) of Sect.II.17 and is discussed similarly. In order to preserve stability, one might replace (2.40') by

$$
- { \dot { C } } ( t ) = n _ { 1 } \theta ( t - T ) + n _ { 2 } { \dot { \theta } } ( t - T )
$$

or even by

$$
\begin{array} { r } { - \dot { C } ( t ) = n _ { 1 } \theta ( t - T ) + n _ { 2 } \dot { \theta } ( t - T ) + n _ { 3 } \ddot { \theta } ( t - T ) . } \end{array}
$$

Here, the first term on the right hand side represents the “Integral feedback” $( I )$ ， the second term“Proportional feedback” $( P )$ and the last term is the “Derivative feedback” $( D )$ .The $P$ -term especially increases the constant $m$ in (2.41), thus adds extra friction to the equation. It is thus natural to expect that the system becomes more stable. The precise tuning of the parameters $n _ { 1 } , n _ { 2 } , n _ { 3 }$ is, however, a long task of analytic study and practical experience.

In order to adapt the continuous-time model (2.40") to our situation, we replace

$$
\begin{array} { r l } & { C ( t ) \longleftrightarrow \log h _ { n } \quad \mathrm { ( t h e ~ ^ { * } c o n t r o l ~ v a r i a b l e ^ { * } ) } } \\ & { \theta ( t ) \longleftrightarrow \log | e r r _ { n } | - \log T o l \quad \mathrm { ( t h e ~ ^ { * } d e v i a t i o n " ) } } \end{array}
$$

and replace derivatives in $t$ by differences. Then the formula (see (2.28))

$$
h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { n _ { 1 } } ,
$$

which is

$$
- \bigl ( \log h _ { n + 1 } - \log h _ { n } \bigr ) = n _ { 1 } \bigl ( \log | e r r _ { n } | - \log T o l \bigr ) ,
$$

corresponds to (2.40). The $P I$ -control (2.40") would read

$$
\begin{array} { r l } & { - ( \log h _ { n + 1 } - \log h _ { n } ) = n _ { 1 } ( \log | e r r _ { n } | - \log T o l ) } \\ & { \qquad + n _ { 2 } \big ( ( \log | e r r _ { n } | - \log T o l ) - ( \log | e r r _ { n - 1 } | - \log T o l ) \big ) , } \end{array}
$$

or when resolved,

$$
h _ { n + 1 } = h _ { n } \cdot \bigg ( \frac { T o l } { | e r r _ { n } | } \bigg ) ^ { n _ { 1 } } \bigg ( \frac { | e r r _ { n - 1 } | } { | e r r _ { n } | } \bigg ) ^ { n _ { 2 } } .
$$

In order to perform a theoretical analysis of this new algorithm we again choose the problem $y ^ { \prime } = \lambda y$ and have as in (2.28)

$$
\begin{array} { r l } & { y _ { n + 1 } = R ( h _ { n } \lambda ) y _ { n } } \\ & { e r r _ { n } = E ( h _ { n } \lambda ) y _ { n } } \\ & { h _ { n + 1 } = h _ { n } \cdot \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { n _ { 1 } } \left( \frac { \left| e r r _ { n - 1 } \right| } { | e r r _ { n } | } \right) ^ { n _ { 2 } } } \\ & { = h _ { n } \left( \frac { T o l } { | e r r _ { n } | } \right) ^ { \alpha } \left( \frac { | e r r _ { n - 1 } | } { T o l } \right) ^ { \beta } } \end{array}
$$

where $\alpha = n _ { 1 } + n _ { 2 } , \beta = n _ { 2 }$ . With the notation (2.29) this process becomes

$$
\begin{array} { r l } & { \eta _ { n + 1 } = \log | R ( e ^ { \chi _ { n } } \lambda ) | + \eta _ { n } } \\ & { \chi _ { n + 1 } = \chi _ { n } - \alpha \log | E ( e ^ { \chi _ { n } } \lambda ) | - \alpha \eta _ { n } + \beta \log | E ( e ^ { \chi _ { n - 1 } } \lambda ) | + \beta \eta _ { n - 1 } + \gamma } \end{array}
$$

with some constant $\gamma$ .This can be considered as a map $\left( \eta _ { n } , \chi _ { n } , \eta _ { n - 1 } , \chi _ { n - 1 } \right)$ $ ( \eta _ { n + 1 } , \chi _ { n + 1 } , \eta _ { n } , \chi _ { n } )$ . At a fixed point $( \eta , \chi )$ , which again satisfies (2.31), the Jacobian is given by

$$
\widetilde C = \frac { \partial ( \eta _ { n + 1 } , \chi _ { n + 1 } , \eta _ { n } , \chi _ { n } ) } { \partial ( \eta _ { n } , \chi _ { n } , \eta _ { n - 1 } , \chi _ { n - 1 } ) } = \left( \begin{array} { c c c c } { { 1 } } & { { u } } & { { 0 } } & { { 0 } } \\ { { - \alpha } } & { { 1 - \alpha v } } & { { \beta } } & { { \beta v } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \end{array} \right)
$$

with $u$ and $v$ as in (2.32). A numerical study of the spectral radius $\varrho ( \widetilde { C } )$ with $\alpha =$ $1 / p$ (where $p$ is the exponent of $h$ of the leading term in the error estimator), $\beta =$ 0.08 along the boundary of the stability domains of the above RK-methods shows an impressive improvement (see Fig.2.9) as compared to the standard algorithm of Fig.2.8. The only exception is DOP853,which becomes unstable close to the real axis, whereas it was $S C$ -stable for $\beta = 0$ . For this method,the value $\beta = 0 . 0 4$ is more suitable.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/0d68f8297eaa9ddddd1c7766cc3385bd3467feafeeac0f5d92ecf5f1190be4a5.jpg)  
Fig.2.9.Regions of step-control stability with stabilization factor $\beta = 0 . 0 8$

The step size behaviour of DOPRI5 with the new strategy ( $\beta = 0 . 1 3 )$ applied to the problem (1.6'） is compared in Fig.2.10 to the undamped step size control （ ${ \bf \nabla } \cdot \beta = 0 )$ . The improvement needs no comment. In order to make the difference clearly visible,we have chosen an extra-large tolerance $A t o l = R t o l = 8 \cdot 1 0 ^ { - 2 }$ ： With $\beta = 0 . 1 3$ the numerical solution becomes smooth in the time-direction. The zig-zag error in the $\boldsymbol { x }$ -direction represents the eigenvector corresponding to the largest eigenvalue of the Jacobian and its magnitude is below Atol.

Man sieht dass selbst der frommste Mann nicht allen Leuten gefallen kann. (W. Busch, Kritik des Herzens 1874)

Study for small $h$ . For the non-stiff case the new step size strategy may be slightly less efficient. In order to understand this,we assume that $| e r r _ { n } | \approx C h _ { n } ^ { p }$ so that (2.43c) becomes

$$
h _ { n + 1 } = h _ { n } \bigg ( \frac { T o l } { C h _ { n } ^ { p } } \bigg ) ^ { \alpha } \bigg ( \frac { C h _ { n - 1 } ^ { p } } { T o l } \bigg ) ^ { \beta }
$$

or, by taking logarithms,

$$
\log h _ { n + 1 } + ( p \alpha - 1 ) \log h _ { n } - p \beta \log h _ { n - 1 } = ( \alpha - \beta ) \log \Big ( \frac { T \alpha l } { C } \Big ) .
$$

This is a linear diference equation with characteristic equation

$$
\lambda ^ { 2 } + ( p \alpha - 1 ) \lambda - p \beta = 0 ,
$$

the roots of which govern the response of the system to variations in $C$ . Obviously, the choice $\alpha = 1 / p$ and $\beta = 0$ would be most perfect by making both roots equal to zero; but this is just the classical step size control. We therefore have to compromise by choosing $\alpha$ and $\beta$ such that (2.45) remains stable for large parts of the stability boundary and at the same time keeping the roots of (2.47) significantly smaller than one. A fairly good choice, found by Gustafsson (1991) after some numerical computations,is

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/c0d0ae93f6408ac119ea904985ea89fdbbdb3a9654a2300a9f26b105237309e7.jpg)  
Fig.2.10. Numerical solution of (1.6'） with $T o l = 8 \cdot 1 0 ^ { - 2 }$

$$
\alpha \approx 0 . 7 / p , \qquad \beta \approx 0 . 4 / p .
$$

# Stabilized Explicit Runge-Kutta Methods

For many problems, usually not very stiff,of large dimension, and with eigenvalues known to lie in a certain region, explicit methods with large stability domains can be very eficient. We consider here methods with extended stability domains along the negative real axis,which are, therefore, especially suited for the time integration of systems of parabolic PDEs. An excellent survey article with additional details and references is Verwer (1996).

Our problem is to find, for a given $s$ , a polynomial of the form $R ( z ) = 1 + z +$ $a _ { 2 } z ^ { 2 } + \ldots + a _ { s } z ^ { s }$ such that the corresponding stability domain is, in the direction of the negative axis,as large as possible. The main ingredient for these methods are the Chebyshev polynomials (Chebyshev 1854)

$$
T _ { s } ( x ) = \cos ( s \operatorname { a r c c o s } x )
$$

$$
T _ { s } ( x ) = 2 x T _ { s - 1 } ( x ) - T _ { s - 2 } ( x ) , \qquad T _ { 0 } ( x ) = 1 , \quad T _ { 1 } ( x ) = x
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/726ed458e22466eaaff95e505359eeb6686084376d1e14b8b4e9a917207c5ffe.jpg)  
Fig.2.11. Shifted Chebyshev polynomial $T _ { 9 } ( 1 + z / 8 1 )$ and its zeros

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/0aac40a98abe2196c466757db4eeb23ff4de1daddbdf6324cd3e786ffbfc8e31.jpg)  
Fig.2.12. Stability domains for shifted Chebyshev polynomials (s = 2,3,4,5) (dots represent limiting case $s \to \infty$ , see Exercise 8 below)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/64ba04b03ce6c92845c4a26a2014f94645dd6bd04ed7d609e8eb5e970857ae48.jpg)  
Fig.2.13.Stability domains for damped Chebyshev stability functions, $\varepsilon = 0 . 0 5$

which remain for $- 1 \leq x \leq 1$ between $- 1$ and $+ 1$ and among these polynomials have the largest possible derivative $T _ { s } ( 1 ) = s ^ { 2 }$ (A.A. Markov 1890). Therefore, one must set (Saul'ev 1960, Saul'ev's postgraduate student Yuan Chzao Din 1958, Franklin 1959,Guillou & Lago 1961)

$$
\begin{array} { r } { \hat { R } _ { s } ( z ) = T _ { s } ( 1 + z / s ^ { 2 } ) } \end{array}
$$

so that $R _ { s } ( 0 ) = 1$ ， $R _ { s } ^ { \prime } ( 0 ) = 1$ , and $| R _ { s } ( z ) | \leq 1$ for $- 2 s ^ { 2 } \leq z \leq 0$ (see Fig. 2.11). In particular we have

$$
\begin{array} { r l } & { R _ { 1 } ( z ) = 1 + z } \\ & { R _ { 2 } ( z ) = 1 + z + \frac { 1 } { 8 } z ^ { 2 } } \\ & { R _ { 3 } ( z ) = 1 + z + \frac { 4 } { 2 7 } z ^ { 2 } + \frac { 4 } { 7 2 9 } z ^ { 3 } } \\ & { R _ { 4 } ( z ) = 1 + z + \frac { 5 } { 3 2 } z ^ { 2 } + \frac { 1 } { 1 2 8 } z ^ { 3 } + \frac { 1 } { 8 1 9 2 } z ^ { 4 } } \\ & { R _ { 5 } ( z ) = 1 + z + \frac { 4 } { 2 5 } z ^ { 2 } + \frac { 2 8 } { 3 1 2 5 } z ^ { 3 } + \frac { 1 6 } { 7 8 1 2 5 } z ^ { 4 } + \frac { 1 6 } { 9 7 6 5 6 2 5 } z ^ { 5 } \ . } \end{array}
$$

whose stability domains are represented in Fig. 2.12.

Damping. In the points where $T _ { s } ( 1 + z / s ^ { 2 } ) = \pm 1$ , there is no damping at all of the higher frequencies and the stability domain has zero width. We therefore choose a small $\varepsilon > 0$ ,say $\varepsilon = 0 . 0 5$ , and put (already suggested by Guillou & Lago 1961)

$$
R _ { s } ( z ) = \frac { 1 } { T _ { s } ( w _ { 0 } ) } T _ { s } ( w _ { 0 } + w _ { 1 } z ) , \quad w _ { 0 } = 1 + \frac { \varepsilon } { s ^ { 2 } } , \quad w _ { 1 } = \frac { T _ { s } ( w _ { 0 } ) } { T _ { s } ^ { \prime } ( w _ { 0 } ) } .
$$

These polynomials oscillate between approximately $1 - \varepsilon$ and $- 1 + \varepsilon$ and again satisfy $R _ { s } ( z ) = 1 + z + \mathcal { O } ( z ^ { 2 } )$ . The stability domains become a bit shorter (by $( 4 \varepsilon / 3 ) s ^ { 2 } )$ , but the boundary is in a safe distance from the real axis (see Fig. 2.13).

Lebedev's Realization. Our next problem is to find Runge-Kutta methods which realize these stability polynomials. A first idea, mentioned by Saul'ev (1960) and Guillou & Lago (1961), is to write

$$
R _ { s } ( z ) = \prod _ { \ i = 1 } ^ { s } ( 1 + \delta _ { \ i } z ) \qquad \mathrm { w h e r e } \quad \delta _ { i } = - \frac { 1 } { z _ { i } } , \quad z _ { \ i } \mathrm { ~ r o o t s ~ o f ~ } R ( z )
$$

and to represent the RK method as the composition of explicit Euler steps

$$
g _ { 0 } : = y _ { 0 } , \qquad g _ { \iota } : = g _ { \iota - 1 } + h \delta _ { \iota } f ( g _ { \iota - 1 } ) , \quad ( i = 1 , 2 , \ldots , s ) , \qquad y _ { 1 } : = g _ { s } .
$$

A disadvantage here is the fact that for the first of these roots,which in absolute value is much smaller than the others, we shall have a very large Euler step, which is surely not good. Lebedev's idea (Lebedev 1989,1994) is therefore to group the roots symmetrically two-by-two together and to represent the corresponding quadratic factor

$$
( 1 + \delta _ { i } z ) ( 1 + \delta _ { i } ^ { \prime } z ) = ( 1 + 2 \alpha _ { \iota } z + \beta _ { \iota } z ^ { 2 } )
$$

by a two-stage scheme

$$
\begin{array} { r l } & { \qquad g _ { \iota } : = g _ { i - 1 } + h \alpha _ { \iota } f ( g _ { \iota - 1 } ) } \\ & { \qquad g _ { i + 1 } ^ { \star } : = g _ { i } + h \alpha _ { i } f ( g _ { \iota } ) } \\ & { \qquad g _ { \iota + 1 } : = g _ { i + 1 } ^ { \star } - h \alpha _ { i } \gamma _ { i } \big ( f ( g _ { i } ) - f ( g _ { \iota - 1 } ) \big ) } \\ & { \qquad = g _ { i + 1 } ^ { \star } - \gamma _ { \iota } \big ( ( g _ { i + 1 } ^ { \star } - g _ { i } ) - ( g _ { i } - g _ { i - 1 } ) \big ) } \end{array}
$$

which produces (2.54) if $\beta _ { i } = \alpha _ { \iota } ^ { 2 } ( 1 - \gamma _ { \iota } )$ . This halves nearly the largest Euler step size and allows also complex conjugate pairs of roots. The expression $( g _ { i + 1 } ^ { \star } - g _ { i } ) -$ $\left( g _ { \ i } - g _ { \ i - 1 } \right) \approx h ^ { 2 } \alpha _ { \ i } ^ { 2 } y ^ { \prime \prime }$ can be used for error estimations and step size selections. For odd $s$ , there remains one single root which gives rise to an Euler step (2.53).

Best Ordering. Some attention is now necessary for the decision in which order the roots shall be used (Lebedev & Finogenov 1976). This is done by two requirements: firstly, the quantities

$$
S _ { \jmath } = \operatorname* { m a x } _ { z } | 1 + \delta _ { 1 } z | \prod _ { \imath = 1 } ^ { \jmath } | 1 + 2 \alpha _ { \imath } z + \beta _ { \imath } z ^ { 2 } | ,
$$

which express the stability of the internal stages,must be $\leq 1$ (here, the max is taken over real $z$ in the stability interval of the method). Secondly, the quantities

$$
Q _ { j } = \operatorname * { m a x } _ { z } \prod _ { i = \jmath + 1 } ^ { s } | 1 + 2 \alpha _ { \iota } z + \beta _ { i } z ^ { 2 } | ,
$$

which describe the propagation of rounding errors,must be as small as possible. These conditions, evaluated numerically for the case $s = 9$ , lead to the ordering indicated in Fig.2.11.

Second Order Methods. If the stability polynomial is a second order approximation to $e ^ { z }$ ,i.e., if

$$
R _ { s } ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 } } + a _ { 3 } z ^ { 3 } + \ldots + a _ { s } z ^ { s }
$$

then it can be seen from (2.8) that any corresponding Runge-Kutta scheme is also of second order for nonlinear problems. Analytic expressions, in terms of an elliptic integral, for such optimal polynomials have been obtained by Lebedev & Medovikov (1994). Their stability region reaches to $- 0 . 8 2 1 8 4 2 \cdot s ^ { 2 }$ for $s \gg 1$ Their practical computation is usually done numerically (Remez 1957, Lebedev 1995).For example,in the case $s = 9$ and for a damping factor $\varepsilon = 0 . 0 1 5$ ，we obtain the roots

$$
\begin{array} { r l } & { z _ { 9 } = - 6 4 . 6 4 2 3 8 3 8 9 , \quad z _ { 8 } = - 6 0 . 6 7 4 7 9 3 4 7 , \quad z _ { 7 } = - 5 3 . 2 1 6 9 5 4 8 8 , } \\ & { z _ { 6 } = - 4 3 . 1 6 5 2 7 0 1 0 , \quad z _ { 5 } = - 3 1 . 7 2 4 7 1 6 9 9 , \quad z _ { 4 } = - 2 0 . 2 5 4 7 4 1 6 3 , } \\ & { z _ { 3 } = - 1 0 . 0 5 5 4 5 9 3 8 , \quad z _ { 2 , 1 } = - 1 . 3 0 5 9 6 1 6 6 \pm i \cdot 1 . 3 4 0 4 7 5 1 7 } \end{array}
$$

The corresponding stability polynomials,which are stable for $- 6 5 . 1 5 \leq z \leq 0$ ,the stability domain, and the best ordering are shown in Fig. 2.14. We see that we now have a pair of complex roots.

Lebedev's computer code,called DUMKA, incorporates the formulas of the above type with automatic selection of $h$ and $s$ in a wide range.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/918c85c618d7fb17239ad04801b79447436e84e70e9d2134284e1f92f62bea73.jpg)  
Fig. 2.14. Second order Zolotarev approximation with stability domain

Numerical Example. As an illustration, the method corresponding to (2.55) and (2.57) has been applied to problem (1.6'). Theory predicts stability for approximately $h \leq 6 5 . 1 5 / 1 3 5 = 0 . 4 8 2 6$ . The leftmost picture of Fig.2.15 is computed with $h = 0 . 4 8 8 6 5$ ,which is a little too large and produces instability. The middle picture is produced by the code DUMKA with $T o l = 3 \cdot 1 0 ^ { - 3 }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/d6e5d95076891699c553cafb1bd4f467228c69da7692e41cc54cbf2659208e94.jpg)  
Fig.2.15. Problem (1.6): Lebedev9, $h = 0 . 4 8 8 6 5$ (left), DUMKA (middle),RKC (right) (all internal stages drawn)

The Approach of van der Houwen & Sommeijer. An elegant idea for a second realization has been found by van der Houwen & Sommeijer (198O): apply scaled and shifted Chebyshev polynomials and use the three-term recusion formula (2.49') for defining the internal stages. We therefore, following Bakker (1973), set

$$
R _ { s } ( z ) = a _ { s } + b _ { s } T _ { s } ( w _ { 0 } + w _ { 1 } z ) \qquad w _ { 0 } = 1 + \varepsilon / s ^ { 2 } , \varepsilon \approx 0 . 1 5 .
$$

The conditions for second order

$$
R _ { s } ( 0 ) = 1 , \quad R _ { s } ^ { \prime } ( 0 ) = 1 , \quad R _ { s } ^ { \prime \prime } ( 0 ) = 1
$$

lead to

$$
w _ { 1 } = \frac { T _ { s } ^ { \prime } ( w _ { 0 } ) } { T _ { s } ^ { \prime \prime } ( w _ { 0 } ) } , \qquad b _ { s } = \frac { T _ { s } ^ { \prime \prime } ( w _ { 0 } ) } { ( T _ { s } ^ { \prime } ( w _ { 0 } ) ) ^ { 2 } } , \qquad a _ { s } = 1 - b _ { s } T _ { s } ( w _ { 0 } ) ,
$$

with damping $a _ { s } + b _ { s } \approx 1 - \varepsilon / 3$ (see Ex.9). We now put for the internal stages

$$
R _ { j } ( z ) = a _ { \jmath } + b _ { \jmath } T _ { j } ( w _ { 0 } + w _ { 1 } z ) \qquad j = 0 , 1 , \ldots , s - 1 .
$$

It has been discovered by Sommeijer (see Sommeijer & Verwer 198O), that these $R _ { j } ( z )$ can, for $j \geq 2$ , be approximations of second order at certain points $\boldsymbol { x } _ { 0 } + \boldsymbol { c } _ { j } \boldsymbol { h }$ if

$$
R _ { \ j } ( 0 ) = 1 , \quad R _ { \ j } ^ { \prime } ( 0 ) = c _ { \ j } , \quad R _ { \ j } ^ { \prime \prime } ( 0 ) = c _ { \ j } ^ { 2 }
$$

which gives

$$
R _ { j } ( z ) - 1 = b _ { j } \big ( T _ { j } ( w _ { 0 } + w _ { 1 } z ) - T _ { j } ( w _ { 0 } ) \big ) , \qquad b _ { j } = \frac { T _ { j } ^ { \prime \prime } ( w _ { 0 } ) } { ( T _ { j } ^ { \prime } ( w _ { 0 } ) ) ^ { 2 } } .
$$

The three-term recurrence relation (2.49') now leads to

$$
R _ { j } ( z ) - 1 = \mu _ { j } ( R _ { j - 1 } ( z ) - 1 ) + \nu _ { j } ( R _ { j - 2 } ( z ) - 1 ) + \kappa _ { j } \cdot z \cdot ( R _ { j - 1 } ( z ) - a _ { j - 1 } )
$$

where

$$
\mu _ { j } = \frac { 2 b _ { j } w _ { 0 } } { b _ { j - 1 } } , \quad \nu _ { j } = \frac { - b _ { j } } { b _ { j - 2 } } , \quad \kappa _ { j } = \frac { 2 b _ { j } w _ { 1 } } { b _ { j - 1 } } , \qquad j = 2 , 3 , \ldots , s .
$$

This formula allows, in the case of a nonlinear differential system, to define the scheme

$$
\begin{array} { l r } { { g _ { 0 } - y _ { 0 } = 0 , } } \\ { { g _ { 1 } - y _ { 0 } = \kappa _ { 1 } h f ( g _ { 0 } ) , } } \\ { { g _ { j } - y _ { 0 } = \mu _ { j } ( g _ { j - 1 } - y _ { 0 } ) + \nu _ { j } ( g _ { j - 2 } - y _ { 0 } ) + \kappa _ { j } h f ( g _ { j - 1 } ) - a _ { j - 1 } \kappa _ { j } h f ( g _ { 0 } ) , } } \end{array}
$$

which, being of second order for $y ^ { \prime } { = } \lambda y$ , is of second order for nonlinear equations too (again because of (2.8)). For $j = 1$ only first order is possible and $\kappa _ { 1 }$ can be chosen freely. Sommeijer & Verwer (1980) suggest to put

$$
b _ { 0 } = b _ { 2 } , b _ { 1 } = b _ { 2 } \mathrm { w h i c h g i v e s } \kappa _ { 1 } = c _ { 1 } = \frac { c _ { 2 } } { T _ { 2 } ^ { \prime } ( w _ { 0 } ) } \approx \frac { c _ { 2 } } { 4 } .
$$

Fig. 2.16 shows, for $s \approx 9$ as usual, the functions $R _ { s } ( z )$ and $R _ { j } ( z ) , j = 2 , . . . , s -$ 1 together with the stability domain of $R _ { s } ( z )$ (the“Venus of Willendorf"） in exactly the same frame as Lebedev's Zolotarev polynomial of Fig. 2.14. We see that the stability domain becomes a little shorter, but we have closed analytic expres-sions and a smoother behaviour of the $c _ { i } \mathrm { ^ { \circ } } \mathbf { s }$ (see Fig.2.15,right). Allinternal stages satisfy $| R _ { j } ( z ) | \leq 1$ , and the method can be seen to possess a satisfactory numerical stability (see Verwer,Hundsdorfer & Sommeijer 199O). The above formulas have been implemented in a research code RKC ("Runge-Kutta-Chebyshev") by Sommeijer (1991). As can be seen from Fig.2.15, it performs well for equation (1.6'). More numerical results shall be reported in Sect. IV.10.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/7dacc8adaf2e93e845220c003f9c80f79042aa6c0490df962ac8bac5c8895963.jpg)  
Fig. 2.16. Stability function and domain for RKC method, $s = 9$ ， $\varepsilon = 0 . 1 5$

Combined Approach of Abdulle & Medovikov. Recent research and a code ROCK4 are presented in: A. Abdulle, Fourth order Chebyshev methods with recurrence relation, to appear in SIAM J. Sci. Comput. 2002.

# Exercises

1. Prove that Runge-Kutta methods are invariant under linear transformations $y =$ $T z$ (i.e., if one applies the method to $y \prime = f ( x , y )$ and to $z ^ { \prime } = T ^ { - 1 } f ( x , T z )$ with initial values satisfying $y _ { 0 } = T z _ { 0 }$ , then we have $y _ { 1 } = T z _ { 1 }$ )

2. Consider the differential equation $y ^ { \prime } = A y$ and a numerical solution given by $y _ { n + 1 } = R ( h A ) y _ { n }$ . Suppose that $R ( z )$ is $A$ -stable,i.e., it satisfies

$$
| R ( z ) | \leq 1 \qquad { \mathrm { f o r } } \qquad { \mathrm { R e ~ } } z \leq 0 ,
$$

and show, by transforming $A$ to Jordan canonical form, that

a) if $y ^ { \prime } = A y$ is stable, then $\{ y _ { n } \}$ is bounded; b）if $y ^ { \prime } = A y$ is asymptotically stable, then $y _ { n } \to 0$ for $n \to \infty$ ·

3. (Optimal stability for hyperbolic problems,van der Houwen (1968),(1977), p.99): Given $m$ ，find a polynomial $\begin{array} { r } { R _ { m } ( z ) = 1 + z + . . } \end{array}$ . of degree $m + 1$ such that $| R ( i y ) | \leq 1$ for $- \beta \leq y \leq \beta$ with $\beta$ as large as possible.

Result. The solution (Sonneveld & van Leer 1985) is given by

$$
R _ { m } ( z ) = \frac { 1 } { 2 } V _ { m - 1 } ( \zeta ) + V _ { m } ( \zeta ) + \frac { 1 } { 2 } V _ { m + 1 } ( \zeta ) , \quad \zeta = \frac { z } { m }
$$

where $V _ { m } ( \zeta ) = i ^ { m } T _ { m } ( \zeta / i )$ are the Chebyshev polynomials with positive coefficients. $R _ { m } ( i y )$ is stable for $- m \leq y \leq m$ . The first $R _ { m }$ are (see Abramowitz & Stegun, p. 795)

$$
\begin{array} { l r } { { R _ { 1 } ( z ) = 1 + \zeta + \zeta ^ { 2 } } } & { { \zeta = \frac { z } { m } } } \\ { { \ } } & { { R _ { 2 } ( z ) = 1 + 2 \zeta + 2 \zeta ^ { 2 } + 2 \zeta ^ { 3 } } } \\ { { \ } } & { { R _ { 3 } ( z ) = 1 + 3 \zeta + 5 \zeta ^ { 2 } + 4 \zeta ^ { 3 } + 4 \zeta ^ { 4 } } } \\ { { \ } } & { { R _ { 4 } ( z ) = 1 + 4 \zeta + 8 \zeta ^ { 2 } + 1 2 \zeta ^ { 3 } + 8 \zeta ^ { 4 } + 8 \zeta ^ { 5 } } } \end{array}
$$

Similar as for Chebyshev polynomials, they satisfy the recurrence relation $R _ { m + 1 } = 2 \zeta R _ { m } + R _ { m - 1 } ( m \geq 2 )$ . Their stability domains are given in Fig. 2.17.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/520f94074a509b1989999f2507b664b9fdb51e1831fa882d8e89e6a149ded4fa.jpg)  
Fig.2.17. Stability domains for hyperbolic approximations

4． Linearize the rope equation (1.24) in the neighbourhood of $\theta = \dot { \theta } = 0$ and make a stability analysis. Re-obtain Lagrange's equation (I.6.2) from the linearized equation with the coordinate transformation

$$
\begin{array} { r } { \boldsymbol { y } = \left( \begin{array} { l l l l l } { 1 } & & & & \\ { 1 } & { 1 } & & & \\ { 1 } & { 1 } & { 1 } & & \\ { : } & { \vdots } & { \vdots } & { \ddots } \end{array} \right) \boldsymbol \theta , \qquad \boldsymbol \theta = \left( \begin{array} { l l l l l } { 1 } & & & & \\ { - 1 } & { 1 } & & & \\ & { - 1 } & { 1 } & & \\ & & { \ddots } & { \ddots } \end{array} \right) \boldsymbol y . } \end{array}
$$

5.Fig.2.18 shows the numerical results of the classical 4th order Runge-Kutta method with equidistant steps over $0 \leq t \leq 5$ for the beam problem(1.7)-(1.20) with $n \approx 8$ . Explain the result with the help of Fig.2.1.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/6cedcfcc18332dfd240b797084a53f939767e1197597b52671f654b2ac055dda.jpg)  
Fig. 2.18. Classical Runge-Kutta method (constant step sizes) on the beam problem

6.For theexample of Exercise 5,the explicit Euler method,although converging for $h \to 0$ , is never stable (see Fig. 2.19). Why?

7. Let $\lambda$ be an eigenvalue of the two-dimensional left upper submatrix of $\widetilde { C }$ in (2.45) (matrix $C$ of (2.32)) and denote its analytic continuation as eigenvalue of $\widetilde { C }$ by $\lambda ( \beta )$ . Prove that

a)If $\operatorname { R e } \lambda \neq 0$ , then for some $y \in \mathbb { R }$

$$
\lambda ( \beta ) = \lambda \cdot \left( 1 - \frac { \beta } { \alpha } \left( 1 - \mathrm { R e } \lambda \right) + i \beta y + \mathcal { O } ( \beta ^ { 2 } ) \right) .
$$

This shows that $| \lambda ( \beta ) | < | \lambda |$ for small $\beta > 0$ if $\mathrm { R e } \lambda < 1$

b)If $\lambda$ and $\mu$ are two distinct real eigenvalues of the above mentioned submatrix,then

$$
\lambda ( \beta ) = \lambda \cdot \Big ( 1 - \frac { \beta } { \alpha } \left( 1 - \frac { 1 } { \lambda } \right) ^ { 2 } \frac { 1 } { \lambda - \mu } + \mathcal { O } ( \beta ^ { 2 } ) \Big ) .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/eb9de4faf6c1d46465baefc721fd0f662b23e2b694beaf5dcced1f77c2f0b83a.jpg)  
Fig. 2.19.Explicit Euler on the beam problem (every 5Oth step dran)

Hint. Write the characteristic polynomial of $\widetilde { C }$ in the form

$$
\operatorname* { d e t } ( \lambda I - \widetilde { C } ) = \lambda \big ( \lambda p ( \lambda ) + \beta q ( \lambda ) \big ) ,
$$

where $p ( \lambda ) = \operatorname* { d e t } ( \lambda I - C )$ is the characteristic polynomial of $C$ , and differentiate with respect to $\beta$ ·

8. Show that for the Chebyshev stability functions (2.5O) we have

$$
\operatorname* { l i m } _ { s  \infty } R _ { s } ( z ) = \cos ( \sqrt { - 2 z } ) .
$$

Hint. Insert $\operatorname { a r c c o s } ( 1 - x ^ { 2 } / 2 ) \approx x$ into (2.49) and (2.50). The corresponding stability domain is indicated by dotted lines in the last picture of Fig.2.12.

9. Show (for example with the help of(2.49') that for the Chebyshev polynomials

$$
T _ { s } ^ { \prime } ( 1 ) = s ^ { 2 } , \qquad T _ { s } ^ { \prime \prime } ( 1 ) = \frac { s ^ { 2 } ( s ^ { 2 } - 1 ) } { 3 }
$$

and obtain asymptotic values (for $\varepsilon \to 0$ )for $w _ { 1 } , b _ { s } , a _ { s }$ , the damping factor and the stability interval of the Bakker polynomials (.58).

10.(Cross-shaped stability domains). For $- 1 \leq \varphi \leq 1$ we put $z = - b \pm \sqrt { a ( \varphi - 1 ) + b ^ { 2 } }$ ,so that $z$ moves on a cross $- 2 b \leq$ $z \le 0$ and $z = - b \pm i y$ . Thus (an idea of Lebedev)

$$
R _ { 2 s } ( z ) = T _ { s } ( \varphi ( z ) )
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/3292bde8540e7a77b9d13a6e25915b65271f9b427c4eeac63a55865a6d2bd91f.jpg)

is a stability function for eigenvalues on crosses (as, e.g., for the PLATE problem). Determine $a$ in dependence of $b$ from the condition $R ^ { \prime } ( 0 ) = 1$ and find the maximal value for $y$

Result. $R _ { 2 s } ( z ) = T _ { s } ( 1 + z / s ^ { 2 } + z ^ { 2 } / ( 2 b s ^ { 2 } ) )$ ； $y _ { \mathrm { { m a x } } } = { \sqrt { 4 b s ^ { 2 } - b ^ { 2 } } } .$

# IV.3Stability Function of Implicit RK-Methods

I didn't like all these“strong”，“perfect",“absolute”，“general-ized",“super”,“hyper”,“complete” and so on in mathematical definitions,I wanted something neutral; and having been impres-sed by David Young's “property $A ^ { \ast }$ ,I chose the term“A-stable”.

(G. Dahlquist, in 1979)

There are at least two ways to combat stiffness. One is to design a better computer, the other, to design a better algorithm.

(H.Lomax in Aiken 1985)

Methods are called $A$ -stable if there are no stability restrictions for $y ^ { \prime } { = } \lambda y$ ， $\mathrm { R e } \lambda <$ O and $h > 0$ . This concept was introduced by Dahlquist (1963) for linear multistep methods,but also applied to Runge-Kutta processes. Ehle (1968) and Axelsson (1969) then independently investigated the $A$ -stability of implicit Runge-Kutta methods and proposed new classes of $A$ -stable methods. A nice paper of Wright (1970) studied collocation methods.

# The Stability Function

We start with the implicit Euler method. This method, $y _ { 1 } = y _ { 0 } + h f ( x _ { 1 } , y _ { 1 } )$ ,applied to Dahlquist's equation $y ^ { \prime } = \lambda y$ becomes $y _ { 1 } = y _ { 0 } + h \lambda y _ { 1 }$ which, after solving for $y _ { 1 }$ ， gives

$$
y _ { 1 } = R ( h \lambda ) y _ { 0 } \quad { \mathrm { w i t h } } \quad R ( z ) = { \frac { 1 } { 1 - z } } .
$$

This time, the stability domain is the exterior of the circle with radius 1 and centre $+ 1$ . The stability domain thus covers the entire negative half-plane and a large part of the positive half-plane as well. The implicit Euler method is very stable.

Proposition 3.1. The s-stage implicit Runge-Kutta method

$$
\begin{array} { l l } { { g _ { \imath } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) \quad } } & { { i = 1 , \ldots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) \quad } } & { { } } \end{array}
$$

applied to $y ^ { \prime } = \lambda y$ yields $y _ { 1 } = R ( h \lambda ) y _ { 0 }$ with

$$
\begin{array} { c } { R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 } , } \\ { b ^ { T } = ( b _ { 1 } , \dots , b _ { s } ) , \quad A = ( a _ { \iota _ { \mathcal { I } } } ) _ { i , \jmath = 1 } ^ { s } , \quad \mathbb { 1 } = ( 1 , \dots , 1 ) ^ { T } . } \end{array}
$$

Remark. As in Definition 2.1, $R ( z )$ is called the stability function of Method (3.1).

Proof. Equation (3.1a) with $f ( x , y ) = \lambda y$ ， $z = h \lambda$ becomes a linear system for the computation of $g _ { 1 } , \ldots , g _ { s }$ . Solving this and inserting into (3.1b) leads to (3.2).

Another useful formula for $R ( z )$ is the following (Stetter 1973,Scherer 1979):

Proposition 3.2. The stability function of(3.1) satisfies

$$
R ( z ) = { \frac { \operatorname* { d e t } \left( I - z A + z \Im b ^ { T } \right) } { \operatorname* { d e t } \left( I - z A \right) } } .
$$

Proof. Applying (3.1) to (2.9) yields the linear system

$$
\left( \begin{array} { l l } { I - z A } & { 0 } \\ { - z b ^ { T } } & { 1 } \end{array} \right) \left( \begin{array} { l } { g } \\ { y _ { 1 } } \end{array} \right) = y _ { 0 } \left( \begin{array} { l } { \Im } \\ { 1 } \end{array} \right) .
$$

Cramer's rule (Cramer 1750) implies that the denominator of $R ( z )$ is $\operatorname* { d e t } ( I -$ $z A )$ ，and its numerator

$$
\operatorname* { d e t } { \binom { I - z A \quad \mathbb { 1 } } { - z b ^ { T } \quad 1 } } = \operatorname* { d e t } { \binom { I - z A + z \mathbb { 1 } b ^ { T } \quad 0 } { - z b ^ { T } \quad 1 } } = \operatorname* { d e t } { \big ( } I - z A + z \mathbb { 1 } b ^ { T } { \big ) } .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/26bb08d9c2088e57c909eb667fc8d27767ec2f098dfc756e9d5c1b08141a0ee5.jpg)  
Fig.3.1. Stability domains for implicit Runge-Kutta methods

The stability functions for the methods of Sect.II.7 are presented in Table 3.1. The corresponding stability domains are displayed in Fig.3.1.

We see that for implicit methods $R ( z )$ becomes a rational function with numerator and denominator of degree $\leq s$ . We write

$$
R ( z ) = \frac { P ( z ) } { Q ( z ) } , \qquad \deg P = k , \quad \deg Q = j .
$$

Table 3.1. Stability functions for implicit Runge-Kutta methods of Sect. I1.7   

<table><tr><td></td><td>Method</td><td>R(z)</td></tr><tr><td>a)</td><td>0-method (I1.7.2)</td><td>1+z(1-0) 1-z0</td></tr><tr><td>b)</td><td>implicit Euler (II.7.3)</td><td>1 1-z</td></tr><tr><td>c）</td><td>implicit midpoint (I1.7.4) } trapezoidal rule (I1.7.5)</td><td>1+z/2 1-x/2</td></tr><tr><td>d）</td><td>Hammer-Hollingsworth (II.7.6)</td><td>1+4z/6+x²/6 1-x/3</td></tr><tr><td>e)</td><td>SDIRK order 3 (Table II.7.2)</td><td>1+z(1-2γ)+x²(1/2-2γ+γ²) （1-Y2）</td></tr><tr><td>f</td><td>Hammer-Hollingsw. 4 (Table II.7.3)} Lobatto IIIA, order 4 (Table II.7.7)</td><td>1+z/2+z²/12 1-x/2+z²/12</td></tr><tr><td>g）</td><td>Kuntzm.-Butcher 6 (Table I1.7.4)</td><td>1+z/2+z²/10+x³/120 1-z/2+z²/10-z³/120</td></tr><tr><td>h)</td><td>Butcher&#x27;s Lobatto 4 (Table I1.7.6)</td><td>1+3z/4+z²/4+ z³/24 1-z/4</td></tr><tr><td>i)</td><td>Butcher&#x27;s Lobatto 6 (Table II.7.6)</td><td>1+2z/3+z²/5+x³/30+z4/360 1-z/3+z²/30</td></tr><tr><td>j）</td><td>Radau IIA, order 5 (Table II.7.7)</td><td>1+2z/5+z²/20 1-3x/5+3z²/20-z/60</td></tr></table>

If the method is of order $p$ ,then

$$
e ^ { z } - R ( z ) = C z ^ { p + 1 } + { \mathcal O } ( z ^ { p + 2 } ) \qquad { \mathrm { f o r ~ } } z \to 0
$$

(see Theorem 2.2). The constant $C$ is usually $\neq 0$ . If not, we increase $p$ in (3.5) until $C$ becomes $\neq 0$ . We then call $R ( z )$ a rational approximation to $e ^ { z }$ of order $p$ and $C$ its error constant.

# A-Stability

We observe that some methods are stable on the entire left half-plane $\mathbb { C } ^ { - }$ .This is precisely the set of eigenvalues,where the exact solution of (2.9) is stable too (Sect.I.13, Theorem 13.1). A desirable property for a numerical method is that it preserves this stability property.

Definition 3.3 (Dahlquist 1963). A method, whose stability domain satisfies

$$
S \supset \mathbb { C } ^ { - } = \{ z ; \quad \mathrm { R e } z \leq 0 \} ,
$$

is called A-stable.

A Runge-Kutta method with (3.4) as stability function is $A$ -stable if and only if

$$
| R ( i y ) | \leq 1 \qquad { \mathrm { f o r ~ a l l ~ r e a l ~ } } y
$$

and

$$
R ( z ) \mathrm { i s ~ a n a l y t i c ~ f o r ~ } \mathrm { R e } z < 0 .
$$

This follows from the maximum principle applied to $\mathbb { C } ^ { - }$ .By a slight abuse of language, we also call $R ( z )$ $A$ -stable in this case (or, as many authors say, $\ " A \ –$ acceptable", Ehle 1968).

Condition (3.6) alone means stability on the imaginary axis and may be called $I$ -stability. It is equivalent to the fact that the polynomial

$$
E ( y ) = | Q ( i y ) | ^ { 2 } - | P ( i y ) | ^ { 2 } = Q ( i y ) Q ( - i y ) - P ( i y ) P ( - i y )
$$

satisfies

$$
E ( y ) \geq 0 \qquad { \mathrm { f o r ~ a l l ~ } } y \in \mathbb { R } .
$$

Proposition 3.4. $E ( y )$ ， defined by (3.8), is an even polynomial of degree ≤ $2 \operatorname* { m a x } ( \deg P , \deg Q )$ .1f $R ( z )$ is an approximation of order $p$ ，then

$$
E ( y ) = \mathcal { O } ( y ^ { p + 1 } ) \qquad f o r \ y \to 0 .
$$

Proof. Taking absolute values in (3.5) gives

$$
| e ^ { z } \vert - \frac { | P ( z ) \vert } { | Q ( z ) | } = \mathcal { O } ( z ^ { p + 1 } ) .
$$

Putting $z = i y$ and using $\left\{ e ^ { \imath y } \right\} = 1$ leads to

$$
| Q ( i y ) | - | P ( i y ) | = \mathcal { O } ( y ^ { p + 1 } ) .
$$

The result now follows from

$$
E ( y ) = ( | Q ( i y ) | + | P ( i y ) | ) ( | Q ( i y ) | - | P ( i y ) | ) .
$$

Examples 3.5.For the implicit midpoint rule, the trapezoidal rule, the Hammer & Hollingsworth, the Kuntzmann & Butcher and Lobatto IIIA methods (c,f, g of Table 3.1） we have $\textstyle E ( y ) \equiv 0$ since $Q ( z ) = P ( - z )$ ．This also follows from Proposition 3.4 because $p = 2 j$ . A straightforward computation shows that (3.7) is satisfied, hence these methods are $A$ -stable.

For methods d, h, i of Table 3.1 we have $\deg P > \deg Q$ and the leading coefficient of $E$ is negative. Therefore (3.9) cannot be true for $y  \infty$ and these methods are not $A$ -stable.

For the Radau IIA method of order 5 (case j) we obtain $E ( y ) = y ^ { 6 } / 3 6 0 0$ and by inspection of the zeros of $Q ( z )$ the method is seen to be $A$ -stable.

For the two-stage SDIRK method (case e) $E ( y )$ becomes

$$
E ( y ) = ( \gamma - 1 / 2 ) ^ { 2 } ( 4 \gamma - 1 ) y ^ { 4 } .
$$

Thus the method is $A$ -stable for $\gamma \geq 1 / 4$ ． The 3rd order method is $A$ -stable for $\gamma = ( 3 + \sqrt { 3 } ) / 6$ , but not for $\gamma = ( 3 - \sqrt { 3 } ) / 6$ (see Fig.3.1).

The following general result explains the $I .$ stability properties of the foregoing examples.

Proposition 3.6. $A$ rational function (3.4) of order $p \geq 2 j - 2$ is $I$ -stable if and only if $| R ( \infty ) | \leq 1$ ，

Proof. $| R ( \infty ) | \leq 1$ implies $k \leq j$ . By Proposition 3.4, $E ( y )$ must be of the form $K \cdot y ^ { 2 \mathcal { I } }$ . By letting $y  \infty$ in (3.6) and (3.9), we see that $| R ( \infty ) | \leq 1$ is equivalent to $K \geq 0$ ： □

# $\pmb { L }$ -Stability and $A ( \alpha )$ -Stability

The trapezoidal rule for the numerical integration of first-order ordinary differential equations is shown to possess, for a certain type of problem,an undesirable property. (A.R.Gourlay 1970)

$A$ -stability is not the whole answer to the problem of stiff equations. (R.Alexander 1977)

Some of the above methods seem to be optimal in the sense that the stability region coincides exactly with the negative half-plane. This property is not as desirable as it may appear, since for a rational function

$$
\operatorname* { l i m } _ { z \to - \infty } R ( z ) = \operatorname* { l i m } _ { z \to \infty } R ( z ) = \operatorname* { l i m } _ { z = i y , y \to \infty } R ( z ) .
$$

The latter must then be 1 in modulus,since $| R ( i y ) | = 1$ for all real $y$ . This means that for $z$ close to the real axis with a very large negative real part, $| R ( z ) |$ is, although $< 1$ ,very close to one. As a consequence, stiff components in (2.6) are damped out only very slowly. We demonstrate this with the example

$$
y ^ { \prime } = - 2 0 0 0 ( y - \cos x ) , \qquad y ( 0 ) = 0 , \qquad 0 \leq x \leq 1 . 5 ,
$$

which is the same as (1.1),but with increased stiffness. The numerical results for the trapezoidal rule are compared to those of implicit Euler in Fig.3.2. The implicit Euler damps out the transient phase much faster than the trapezoidal rule. It thus appears to be a desirable property of a method that $| R ( z ) |$ be much smaller than 1 for $z  - \infty$

Definition 3.7 (Ehle 1969). A method is called $L$ -stable if it is $A$ -stable and if in addition

$$
\operatorname* { l i m } _ { z \to \infty } R ( z ) = 0 .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/ed181cd056c8c6963a8ca3fea569aed72d3586cc76de3a39c88e5d5fa3533a19.jpg)  
Fig.3.2. Trapezoidal rule versus implicit Euler on (3.11)

Among the methods of Table 3.1,the implicit Euler, the SDIRK method (e) with $\gamma = ( \bar { 2 } \pm \sqrt { 2 } ) / 2$ , as well as the Radau IIA formula (j) are $I$ -stable.

Proposition 3.8. If an implicit Runge-Kutta method with nonsingular $A$ satisfies one of the following conditions:

$$
\begin{array} { r } { a _ { s , } = b _ { _ { \jmath } } \quad j = 1 , \ldots , s , } \\ { a _ { \imath 1 } = b _ { 1 } \quad i = 1 , \ldots , s , } \end{array}
$$

then $R ( \infty ) = 0$ . This makes $A$ -stable methods $I$ -stable.

Proof. By (3.2)

$$
R ( \infty ) = 1 - b ^ { T } A ^ { - 1 } \mathbb { 1 }
$$

and (3.13) means that $A ^ { T } e _ { s } = b$ where $e _ { s } = ( 0 , \ldots , 0 , 1 ) ^ { T }$ . Therefore $R ( \infty ) =$ $1 - e _ { s } ^ { T } \mathbb { 1 } = 1 - 1 = 0$ . In the case of (3.14) use $A e _ { \mathbf { 1 } } = \mathbb { 1 } b _ { \mathbf { 1 } }$ □

Methods satisfying (3.13） are called stiffly accurate (Prothero & Robinson 1974).They are important for the solution of singularly perturbed problems and for differential-algebraic equations (see Chapters VI and VII).

The definition of $A$ -stability is on the one hand too weak,as we have just seen, and on the other hand too strong in the sense that many methods which are not so bad at all are not $A$ -stable. The following definition is a little weaker and will be specially useful in the chapter on multistep methods.

Definition 3.9 (Widlund 1967). A method is said to be $A ( \alpha )$ -stable if the sector

$$
S _ { \alpha } = \{ z ; | \arg ( - z ) | < \alpha , \ z \neq 0 \}
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/c2ed8a7632c0180941d178ec772ef86dfe09fcc626e026e134727cf692177ec3.jpg)

is contained in the stability region.

Forexaplethedaoimati $R _ { 0 3 } ( z ) = \left( 1 - z + { \frac { z ^ { 2 } } { 2 ! } } - { \frac { z ^ { 3 } } { 3 ! } } \right) ^ { - }$ 1 (see (3.29) below) is $A ( \alpha )$ -stable for $\alpha \leq 8 8 . 2 3 ^ { \circ }$

# Numerical Results

To show the effects of good stability properties on the stiff examples of Sect.IV.1, we choose the 3-stage Radau IIA formula (Table 5.6 of Sect.IV.5) which, as we have seen, is A-stable, $L$ -stable and of reasonably high order. It has been coded (Subroutine RADAU5 of the Appendix) and the details of this program will be discussed later (Sect.IV.8). This program integrates all the examples of Sect.IV.1 in a couple of steps and the plots of Fig.1.3 and Fig.1.5 show a clear difference.

The beam equation(1.10'） with $n = 4 0$ is integrated, with $R t o l = A t o l = 1 0 ^ { - 3 }$ (absolute) and smooth initial values,in 28 steps (Fig.3.3).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/a65f68a655c68040adca3ac6a897419a1865fa0664a13ed2b025f4b1e8840c86.jpg)  
Fig. 3.3. RADAU5 on the beam (1.10'), every step drawn

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/20234a7e89dd745d4b68204318dd52f3ffb9a6e046c04fdecbec2bbef10cf479.jpg)  
Fig.3.4. RADAU5 on oscillatory beam with large Tol (107 steps,all drawn)

Since the Radau5 formula is $I$ -stable, the stability domain also covers the imaginary axis and large parts of the right half-plane $\mathbb { C } ^ { + }$ . This means that high oscillations of the true solution may be damped by the numerical method. This effect, sometimes judged undesirable (B. Lindberg (1974): “dangerous property ..."),may also be welcome to suppress uninteresting oscillations. This is demonstrated by applying RADAU5 with very large tolerance ( $\mathbf { \nabla } \cdot R t o l = A t o l = 1$ ）to the beam equation (1.10'） with $n = 1 0$ and the perturbed initial value $\theta _ { n } ( 0 ) = 0 . 4$ Here, the high oscillations soon disappear and the numerical solution becomes perfectly smooth (Fig.3.4). If, however, the tolerance requirement is increased, the program is forced to follow all the oscillations and the picture remains the same as in Fig. 1.11.

# Stability Functions of Order $\geq s$

Consider rational functions $R ( z ) = P ( z ) / Q ( z )$ ，where $Q ( 0 ) = 1$ , and both $P ( z )$ and $Q ( z )$ are polynomials of degree at most $s$ . If $R ( z )$ is an approximation of $e ^ { z }$ of order $\geq s$ , then is follows from (3.5) that

$$
e ^ { z } Q ( z ) = P ( z ) + C _ { 1 } z ^ { s + 1 } + C _ { 2 } z ^ { s + 2 } + \dots .
$$

Consequently, the polynomial $P ( z )$ and also the error constants $C _ { 1 } , C _ { 2 } , \ldots$ are uniquely determined in terms of the coefficients of $Q ( z )$ . For

$$
Q ( z ) = q _ { 0 } + q _ { 1 } z + q _ { 2 } z ^ { 2 } + . . . + q _ { s } z ^ { s } , \qquad q _ { 0 } = 1
$$

an expansion of $e ^ { z } Q ( z )$ into powers of $z$ yields

$$
\begin{array} { c } { { P ( z ) = q _ { 0 } + z \displaystyle \left( \frac { q _ { 0 } } { 1 ! } + \frac { q _ { 1 } } { 0 ! } \right) + z ^ { 2 } \displaystyle \left( \frac { q _ { 0 } } { 2 ! } + \frac { q _ { 1 } } { 1 ! } + \frac { q _ { 2 } } { 0 ! } \right) } } \\ { { + \ldots + z ^ { s } \displaystyle \left( \frac { q _ { 0 } } { s ! } + \frac { q _ { 1 } } { ( s - 1 ) ! } + \ldots + \frac { q _ { s } } { 0 ! } \right) , } } \end{array}
$$

and for the error constants

$$
\begin{array} { l } { { C _ { 1 } = \displaystyle \frac { q _ { 0 } } { ( s + 1 ) ! } + \frac { q _ { 1 } } { s ! } + \ldots + \frac { q _ { s - 1 } } { 2 ! } + \frac { q _ { s } } { 1 ! } } } \\ { { C _ { 2 } = \displaystyle \frac { q _ { 0 } } { ( s + 2 ) ! } + \frac { q _ { 1 } } { ( s + 1 ) ! } + \ldots + \displaystyle \frac { q _ { s - 1 } } { 3 ! } + \frac { q _ { s } } { 2 ! } . } } \end{array}
$$

The Polynomial $M ( { \pmb x } )$ . With help of the polynomial

$$
M ( x ) = q _ { s } + q _ { s - 1 } { \frac { x } { 1 ! } } + q _ { s - 2 } { \frac { x ^ { 2 } } { 2 ! } } + \ldots + q _ { 0 } { \frac { x ^ { s } } { s ! } }
$$

the formulas for $Q ( z )$ and $P ( z )$ become more symmetric. We have

$$
\begin{array} { l } { { Q ( z ) = M ^ { ( s ) } ( 0 ) + M ^ { ( s - 1 ) } ( 0 ) z + . . . + M ( 0 ) z ^ { s } } } \\ { { P ( z ) = M ^ { ( s ) } ( 1 ) + M ^ { ( s - 1 ) } ( 1 ) z + . . . + M ( 1 ) z ^ { s } , } } \end{array}
$$

and the error constants are given by

$$
C _ { 1 } = \int _ { 0 } ^ { 1 } M ( x ) d x , \qquad \quad C _ { 2 } = \int _ { 0 } ^ { 1 } ( 1 - x ) M ( x ) d x .
$$

For the stability function of collocation methods we have the following nice result.

Theorem 3.10 (K. Wright 1970, S.P. Norsett 1975). The stability function of the collocation method based on the points $c _ { 1 } , c _ { 2 } , \ldots , c _ { s }$ is given by $R ( z ) =$ $P ( z ) / Q ( z )$ ， where $Q ( z )$ and $P ( z )$ are the polynomials of (3.22) and (3.23), respectively, with $M ( x ) ~ g i \nu e n ~ b y$

$$
M ( x ) = { \frac { 1 } { s ! } } \prod _ { \ i = 1 } ^ { s } ( x - c _ { \ i } ) .
$$

Proof (Ngrsett & Wanner 1979). We assume $x _ { 0 } = 0 , h = 1 , \lambda = z , y _ { 0 } = 1$ and let $u ( x )$ be the collocation polynomial. Since $u ^ { \prime } ( x ) - z u ( x )$ is a polynomial of degree $s$ which vanishes at the collocation points, there are constants $K _ { 0 }$ and $\kappa$ such that

$$
u ^ { \prime } ( x ) - z u ( x ) = K _ { 0 } M ( x ) \qquad { \mathrm { o r } } \qquad \bigl ( 1 - { \frac { D } { z } } \bigr ) u ( x ) = K M ( x )
$$

with the polynomial $M ( x )$ of (3.25) ( $D$ denotes the differentiation operator). Expanding $( 1 - D / z ) ^ { - 1 }$ into a geometric series yields

$$
u ( x ) = K \Big ( 1 + \frac { D } { z } + \frac { D ^ { 2 } } { z ^ { 2 } } + \ldots + \frac { D ^ { s } } { z ^ { s } } \Big ) M ( x ) ,
$$

because $M ^ { ( j ) } ( x ) \equiv 0$ for $j > s$ .From $u ( 1 ) = R ( z ) u ( 0 )$ we have the relation $R ( z ) = u ( 1 ) / u ( 0 )$ ,which leads to (3.22) and (3.23). □

# Padé Approximations to the Exponential Function

Comme cela est souvent le cas en ce qui concerne les découvertes scientifiques, leur inventeur n'est pas H. Padé.

(C. Brezinski 1984, Euvres de H. Padé, p. 5)

Padé approximations (Padé 1892) are rational functions which, for a given degree of the numerator and the denominator, have highest order of approximation. Their origin lies in the theory of continued fractions and they played a fundamental role in Hermite's (1873) proof of the transcendency of $e$

These optimal approximations can be obtained for the exponential function $e ^ { z }$ from (3.22) and (3.23) by the following idea (Padé 1899): choose $M ( x )$ such that in (3.22) and (3.23) as many terms as possible involving high powers of $z$ become zero, i.e.,

$$
M ( x ) = \frac { x ^ { k } ( x - 1 ) ^ { \jmath } } { ( k + j ) ! } ;
$$

then $M ^ { ( i ) } ( 0 ) = 0$ for $i = 0 , \ldots , k - 1$ and $M ^ { ( \imath ) } ( 1 ) = 0$ for $i = 0 , \ldots , j - 1$

Theorem 3.11. The $( k , j )$ -Padé approximation to $e ^ { z }$ is given by

$$
R _ { k j } ( z ) = { \frac { P _ { k j } ( z ) } { Q _ { k j } ( z ) } }
$$

where

$$
\begin{array} { l } { { P _ { k j } ( z ) = 1 + \displaystyle \frac { k } { j + k } z + \displaystyle \frac { k ( k - 1 ) } { ( j + k ) ( j + k - 1 ) } \cdot \displaystyle \frac { z ^ { 2 } } { 2 ! } + . . . + \displaystyle \frac { k ( k - 1 ) . . . 1 } { ( j + k ) . . . ( j + 1 ) } \cdot \displaystyle \frac { z ^ { k } } { k ! } } } \\ { { Q _ { k j } ( z ) = 1 - \displaystyle \frac { j } { k + j } z + \displaystyle \frac { j ( j - 1 ) } { ( k + j ) ( k + j - 1 ) } \cdot \displaystyle \frac { z ^ { 2 } } { 2 ! } - . . . + ( - 1 ) ^ { j } \displaystyle \frac { j ( j - 1 ) . . . 1 } { ( k + j ) . . . ( k + 1 ) } \cdot \displaystyle \frac { z ^ { j } } { j ! } } } \\ { { = P _ { j k } ( - z ) , } } \end{array}
$$

with error

$$
e ^ { z } - R _ { k j } ( z ) = ( - 1 ) ^ { \jmath } \frac { j ! k ! } { ( j + k ) ! ( j + k + 1 ) ! } z ^ { \jmath + k + 1 } + { \mathcal O } ( z ^ { \jmath + k + 2 } ) .
$$

It is the unique rational approximation to $e ^ { z }$ of order $j + k$ ， such that the degrees of numerator and denominator are $k$ and $j$ , respectively.

Table 3.2. Padé approximations for $e ^ { z }$   

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1+1</td><td rowspan=1 colspan=1>1+2+321</td></tr><tr><td rowspan=1 colspan=1>11-z</td><td rowspan=1 colspan=1>1+21-</td><td rowspan=1 colspan=1>1+2+1221-</td></tr><tr><td rowspan=1 colspan=1>11-2+2</td><td rowspan=1 colspan=1>1+22+2112</td><td rowspan=1 colspan=1>122！12+1心1-2</td></tr><tr><td rowspan=2 colspan=1>15   美1-z+</td><td rowspan=1 colspan=1>1+2</td><td rowspan=2 colspan=1>1+2+1江1021-2+ 32      1 3-</td></tr><tr><td rowspan=1 colspan=1>12    132！云3</td></tr></table>

Proof. Inserting (3.28) into (3.22)and (3.23) gives the formulas for $P _ { k _ { \mathcal { I } } } ( z ) , Q _ { k _ { \mathcal { I } } } ( z )$ and (3.3O). The uniqueness is a consequence of the fact that the $( j ^ { - } + k )$ -degree polynomial $M ( x )$ of (3.21) must have a zero of multiplicity $k$ at $x = 0$ ,and one of multiplicity $j$ at $x \approx 1$ □

Table 3.2 shows the first Padé approximations to $e ^ { z }$ . We observe that the stabil-ity function of many methods of Table 3.1 are Padé approximations. The diagonal Padé approximations are those with $k = j$

# Exercises

1. Let $R ( z )$ be the stability function of (3.1) and $R ^ { * } ( z )$ the stability function of its adjoint method (see Sect. I.8). Prove that

$$
R ^ { * } ( z ) = \left( R ( - z ) \right) ^ { - 1 } .
$$

2. Consider an implicit Runge-Kutta method of order $p \geq s$ with nonsingular $A$ ， distinct $c _ { i }$ and non-zero $b _ { i }$ . Show

a)If $C ( s )$ and $c _ { s } = 1$ then (3.13);   
b) If $D ( s )$ and $c _ { 1 } = 0$ then (3.14).

In both cases the stability function satisfies $R ( \infty ) = 0$ ·

(For the definition of the assumptions $C ( s )$ and $D ( s )$ see Sect. IV.5).

3． Show that collocation methods can only be $L$ -stable if $\mathcal { M } ( 1 ) = 0$ ,i.e., if one of the $c ^ { * } s$ ,usually $c _ { s }$ , equals 1.

4. (Padé (1899), see also Lagrange (1776)). Show that the continued fraction

$$
e ^ { x } = 1 + { \cfrac { x } { 1 - { \cfrac { x } { 2 } } + { \cfrac { { \frac { 1 } { 1 \cdot 3 } } { 4 } } { 1 + { \cfrac { { \frac { 1 } { 3 \cdot 5 } } { 1 + { \cfrac { { \frac { 1 } { 5 \cdot 7 } } { 1 + { \cfrac { x ^ { 2 } } { 4 } } } } } } { 1 + { \cfrac { { \frac { 1 } { 7 \cdot 9 } } { 1 + \ddots } } } } } } } } } } 
$$

leads to the diagonal Padé approximations for $e ^ { x }$

Hint. Compute the first partial fractions. If you don't succeed in finding a general proof, read Sect. IV.5.

5．The trapezoidal rule

$$
\frac { 0 } { 1 } \textcircled { 1 / 2 } \frac { 0 } { 1 / 2 }
$$

satisfies $a _ { s i } = b _ { i }$ ，but not $R ( \infty ) = 0$ . Why doesn't this contradict Proposition 3.8?

6. Show that

$$
\begin{array} { l } { y _ { 1 } = y _ { 0 } + h f ( y _ { 0 } + \theta ( y _ { 1 } - y _ { 0 } ) ) } \\ { y _ { 1 } = y _ { 0 } + h ( 1 - \theta ) f ( y _ { 0 } ) + h \theta f ( y _ { 1 } ) } \end{array}
$$

are both nonlinear extensions of the $\theta$ -method. Find others.

7. The composition of a step of the $\theta$ -method with step-size $\alpha h$ , followed by a $\theta ^ { \prime }$ -method with step-size $( 1 - 2 \alpha ) h$ and again a $\theta$ -method with step-size $\alpha h$ leads to

$$
R ( z ) = \Big ( \frac { 1 + \alpha z ( 1 - \theta ) } { 1 - \alpha z \theta } \Big ) ^ { 2 } \Big ( \frac { 1 + ( 1 - 2 \alpha ) z ( 1 - \theta ^ { \prime } ) } { 1 - ( 1 - 2 \alpha ) z \theta ^ { \prime } } \Big )
$$

Show that this method, for $\theta ^ { \prime } = 1 - \theta$ , is of order 2 if $\alpha = 1 - \sqrt { 2 } / 2$ and strongly $A$ -stable (i.e., $A$ -stable and $| R ( \infty ) | < 1 )$ for $\theta > 1 / 2$ . The authors Muller, Prohl, Rannacher & Turek(1994) call this method “fractional $\theta$ method" and use it successfully for computations of the incompressible Navier-Stokes equations.

Mein hochgeehrter Lehrer, der vor wenigen Jahren verstorbene Geheime Hofrath Gauss in Gottingen,pflegte in vertraulichem Gespräche häufig zu äussern, die Mathematik sei weit mehr eine Wissenschaft fur das Auge als eine fir das Ohr. Was das Auge mit einem Blicke sogleich übersieht...

(J.F Encke 1861, publ. in Kronecker's Werke, Vol. 5, page 391)

Order stars, discovered by searching for a better understanding of the stability properties of the Padé approximations to $e ^ { z }$ (Wanner, Hairer & Ngrsett 1978), offered nice and unexpected access to many other results: the “second barrier’ of Dahlquist, the Daniel & Moore conjecture, highest possible order with real poles, comparison of stability domains (Jeltsch & Nevanlinna 1981,1982),order bounds for hyperbolic or parabolic difference schemes (e.g., Iserles & Strang 1983, Iserles & Williamson 1983, Jeltsch 1988).

# Introduction

When I wrote my book in 1971 I wanted to draw “relative stability domains",but curious stars came out from the ploter. I thought of an error in the program and I threw them away ...

(C.W. Gear, in 1979)

We present in Fig.4.1 the stabilitydomains forthePadéapproximations $R _ { 3 3 } , R _ { 2 4 }$ ， $R _ { 1 5 } , R _ { 0 6 }$ of Theorem 3.12,which are all 6th order approximations to $\exp ( z )$ .It can be observed that $R _ { 3 3 }$ and $R _ { 2 4 }$ are nicely $A$ -stable. The other two are not, $R _ { 1 5 }$ violates (3.6) and $R _ { 0 6 }$ violates (3.7). After some meditation on these and similar figures, trying to obtain a better understanding of these phenomena, one is finally led to

Definition 4.1. The set

$$
A = \left\{ z \in \mathbb { C } \ ; \ | R ( z ) | > | e ^ { z } | \right\} = \left\{ z \in \mathbb { C } \ ; \ | q ( z ) | > 1 \right\}
$$

where $q ( z ) = R ( z ) / e ^ { z }$ ,is called the order star of $R$

The order star does not compare $| R ( z ) |$ to 1,as does the stability domain, but to the exact solution $| e ^ { z } | = e ^ { x }$ and it is hoped that this might give more information. As we always assume that the coefficients of $R ( z )$ are real, the order star is symmetric with respect to the real axis. Furthermore, since $\left| e ^ { \imath y } \right| = 1$ ， $A$ is the complementary set of the stability domain $S$ on the imaginary axis. Therefore we have from (3.6) and (3.7):

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/40ff5c4015188dd835575b4e35d32b5e2ce273d02192c108b432b7c1060decd6.jpg)  
Fig. 4.1. Stability domains for Padé approximations

Lemma 4.2. $R ( z )$ is $I$ -stable if and only if (i） $A \cap i \mathbb { R } = \emptyset$ ·   
Further, $R ( z )$ is $A$ -stable if and only if (i) and (ii) all poles of $R ( z )$ $\risingdotseq$ poles of $q ( z ) )$ lie in the positive half plane $\mathbb { C } ^ { + }$

Fig.4.2 shows the order stars corresponding to the functions of Fig.4.1. These order stars show a nice and regular behaviour: there are $j$ black “fingers” to the right, each containing a pole of $R _ { k j }$ , and $k$ white“fingers"to the left, each containing a zero. Exactly two boundary curves of $A$ tend to infinity near to the imaginary axis. These properties are a consequence of the following three Lemmas.

Lemma 4.3. If $R ( z )$ is an approximation to $e ^ { z }$ of order $\mathfrak { p }$ ,i.e.,if

$$
e ^ { z } - R ( z ) = C z ^ { p + 1 } + \mathcal { O } ( z ^ { p + 2 } )
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b993829742e18f9360cb2e06941dfce6015da60c919b9b2cd24f5fc9cbf21a7f.jpg)  
Fig.4.2. Order stars for Padé approximations

with $C \neq 0$ , then, for $z  0$ ， $A$ behaves like $a$ “star”with $p + 1$ sectors of equal width $\pi / ( p + 1 )$ ， separated by $p + 1$ similar “white" sectors ofthe complementary set. The positive real axis is inside a black sector iff $C < 0$ and inside a white sector ff $C > 0$

Proof. Dividing the error formula (4.2) by $e ^ { z }$ gives

$$
\frac { R ( z ) } { e ^ { z } } = 1 - C z ^ { p + 1 } + \mathcal { O } ( z ^ { p + 2 } ) .
$$

Thus the value $R ( z ) / e ^ { z }$ surrounds the point 1 as often as $z ^ { p + 1 }$ surrounds the origin, namely $p + 1$ times. So, $R ( z ) / e ^ { z }$ is $p + 1$ times alternatively inside or outside the unit circle. It lies inside for small positive real $z$ whenever $C > 0$ □


<!-- chunk 0002: pages 71-140 -->
Lemma 4.4. If $z = r e ^ { \imath \theta }$ and $r  \infty$ ,then $z \in A$ for $\pi / 2 < \theta < 3 \pi / 2$ and $z \not \in A$ $f o r \ : - \pi / 2 < \theta < \pi / 2$ . The border $\partial A$ possesses only two branches which $g o$ to infinity. If

$$
R ( z ) = K z ^ { \ell } + \mathcal O ( z ^ { \ell - 1 } ) \qquad \mathrm { f o r } \quad z \to \infty ,
$$

these branches asymptotically approach

$$
x = \log | K | + \ell \log | y |
$$

Proof. The first assertion is the well-known fact that the exponential function, for $\mathrm { R e } z  \pm \infty$ is much stronger than any polynomial or rational function. In order to show the uniqueness of the border lines, we consider for $r  \infty$ the two functions

$$
\begin{array} { l } { { \varphi _ { 1 } ( \theta ) = | e ^ { z } | ^ { 2 } = e ^ { 2 r \cos \theta } } } \\ { { \varphi _ { 2 } ( \theta ) = | R ( z ) | ^ { 2 } = R ( r e ^ { \imath \theta } ) R ( r e ^ { - \imath \theta } ) . } } \end{array}
$$

Differentiation gives

$$
\frac { \varphi _ { 1 } ^ { \prime } } { \varphi _ { 1 } } = - 2 r \sin \theta , \qquad \frac { \varphi _ { 2 } ^ { \prime } } { \varphi _ { 2 } } = 2 r \mathrm { R e } \left( i e ^ { \imath \theta } \cdot \frac { R ^ { \prime } ( r e ^ { i \theta } ) } { R ( r e ^ { i \theta } ) } \right) .
$$

Since $| R ^ { \prime } / R |  0$ for $r  \infty$ , we have

$$
\frac { d } { d \theta } \log \varphi _ { 1 } ( \theta ) < \frac { d } { d \theta } \log \varphi _ { 2 } ( \theta ) \qquad \mathrm { f o r } \quad \theta \in [ \varepsilon , \pi - \varepsilon ] .
$$

Hence in this interval there can only be one value of $\theta$ with $\varphi _ { 1 } ( \theta ) = \varphi _ { 2 } ( \theta )$ .Formula (4.4) is obtained from (4.3) by

$$
| K | ( x ^ { 2 } + y ^ { 2 } ) ^ { \ell / 2 } \approx e ^ { x } , \qquad \log | K | + { \frac { \ell } { 2 } } \log ( x ^ { 2 } + y ^ { 2 } ) \approx x
$$

and by neglecting $x ^ { 2 }$ ，which is justified because $x / y  0$ whenever $x + i y$ tends to infinity on the border of $A$ . □

It is clear from the maximum principle that each bounded “finger” of $A$ in Fig. 4.2 must contain a pole of $q ( z )$ . A still stronger result is the following:

Lemma 4.5. Each bounded subset $F \subset A$ with common boundary $\partial F \subset \partial A$ collecting m sectors at the origin must contain at least m poles of $q ( z )$ (each counted according to its multiplicity). Analogously, each bounded “white" subset $F \subset \mathbb { C } \backslash A$ with m sectors at the origin must contain at least m zeros of $q ( z )$

Proof.Suppose first that $\partial F$ is represented by a parametrized positively oriented loop $c ( t )$ ， $t _ { 0 } \leq t \leq t _ { 1 }$ .Let $\vec { a } = \left( c _ { 1 } ^ { \prime } ( t ) , c _ { 2 } ^ { \prime } ( t ) \right)$ be the tangent vector and $\vec { n } = \left( c _ { 2 } ^ { \prime } ( t ) , - c _ { 1 } ^ { \prime } ( t ) \right)$ an exterior normal vector. We write

$$
q ( z ) = r ( x , y ) \cdot e ^ { \imath \varphi ( x , y ) } , \qquad z = x + i y
$$

so that $\log q ( z ) = \log r ( x , y ) + i \varphi ( x , y )$ . Since the modulus increases inside $F$ ， we have

$$
\frac { \partial ( \log r ) } { \partial \vec { n } } \leq 0 .
$$

Now the Cauchy-Riemann diferential equations for $\log q$ are

$$
{ \frac { \partial ( \log r ) } { \partial x } } = { \frac { \partial \varphi } { \partial y } } ; \qquad { \frac { \partial ( \log r ) } { \partial y } } = - { \frac { \partial \varphi } { \partial x } } ,
$$

so that (4.6) becomes

$$
\frac { \partial \varphi } { \partial \vec { a } } \leq 0 .
$$

This inequality is strict except at a finite number of points,because $q ^ { \prime } ( c ( t ) ) \cdot c ^ { \prime } ( t ) =$ $i \cdot q ( c ( t ) ) \cdot \partial \varphi / \partial \vec { a }$ and the number of zeros of $q ^ { \prime } ( z )$ is finite. Thus the argument of $q$ decreases along $c$ . If the contour curve $c ( t )$ returns $m$ times to the origin, where the argument is a multiple of $2 \pi$ , the vector $q ( z )$ must perform at least $m$ complete revolutions in the negative sense (Fig.4.3). Thus the argument principle (an idea which we have already encountered in Sect.I.13; see Volume I, pages 81 and 382), ensures the presence of at least $m$ poles inside $\boldsymbol { F }$ (there are no zeros, because these are not in $A$ ).

If the boundary curve is represented by several curves, all rotation numbers are added up. For“white” subsets the proof is similar, just that $\partial ( \log r ) / \partial { \vec { n } } > 0$ and the argument rotates in the other sense. □

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/c58e7fd32341071483be7bde2645eab71254b925606273d323a3faa2f4111650.jpg)  
Fig. 4.3. SDIRK methods, order 3; arrows indicate direction of $q ( z )$

Fig. 4.3 gives an illustration of two order stars for the SDIRK methods of order 3 (Table 3.1, case e). Here, $q ( z )$ possesses a double pole at $z = 1 / \gamma$ . However, for $\gamma = ( 3 - \sqrt { 3 } ) / 6$ , the bounded component $F$ of $A$ collects only one sector at the origin. Since the vector $q ( z )$ performs two rotations, there is in addition to the origin a second point on $\partial { \cal F }$ for which $\arg ( q ) = 0$ ,i.e., $\arg ( R ( z ) ) = \arg ( e ^ { z } )$ Thus, because $| R ( z ) | = | e ^ { z } |$ on $\partial A$ , we have $R ( z ) = e ^ { z }$ . These points are called exponential fitting points. Another version of Lemma 4.5 is thus (Iserles 1981):

Lemma $4 . 5 ^ { \circ }$ . Each bounded subset $F \subset A$ with $\partial F \subset \partial A$ contains exactly as many poles as there are exponential fitting points on its boundary. □

# Order and Stability for Rational Approximations

In the sequel we suppose $R ( z )$ to be an arbitrary rational approximation of order $p$ with $k$ zeros and $j$ poles.

Theorem 4.6. If $R ( z )$ is $A$ -stable, then $p \leq 2 k _ { 1 } + 2$ ，where $k _ { 1 }$ is the number of different zeros of $R ( z )$ in $\mathbb { C } ^ { - }$

Proof. At least $\left[ ( p + 1 ) / 2 \right]$ sectors of $A$ start in $\mathbb { C } ^ { - }$ (Lemma 4.3). By $A$ -stability these have to be infinite and enclose at least $[ ( p + 1 ) / 2 ] - 1$ bounded white fingers, each containing at least one zero by Lemma 4.5. Therefore $[ ( p + 1 ) / 2 ] - 1 \le k _ { 1 }$ □

Theorem 4.7. If $R ( z )$ is $I$ -stable, then $p \leq 2 j _ { 1 }$ ，where $j _ { 1 } ^ { \mathrm { ~ ~ } }$ is the number of poles of $R ( z )$ in $\mathbb { C } ^ { + }$ .

Proof. At least $\{ ( p + 1 ) / 2 \}$ sectors of $A$ start in $\mathbb { C } ^ { + }$ ．They cannot cross $i \mathbb { R }$ and must therefore be bounded (Lemma 4.4). Again by Lemma 4.5 we have $[ ( p +$ $1 ) / 2 ] \leq j _ { 1 }$ · □

Theorem 4.8. Suppose that $p \geq 2 j - 1$ and $| R ( \infty ) | \leq 1$ . Then, $R ( z )$ is $A$ -stable.

Proof. By Proposition 3.6 the function $R ( z )$ is $I$ -stable. Applying Theorem 4.7 we get $j _ { 1 } \geq j$ so that $I$ -stability implies $A$ -stability. □

Theorem 4.9 (Crouzeix & Ruamps 1977). Suppose $p \geq 2 j - 2$ ， $| R ( \infty ) | \leq 1$ ,and the coefficients of the denominator $Q ( z )$ have alternating signs. Then, $R ( z )$ is A-stable.

Proof. A similar argument as in the foregoing proof allows at most one pole in $\mathbb { C } ^ { - }$ ： It would then be real and its existence would contradict the hypothesis on signs of $Q ( z )$ □

Theorem 4.10. Suppose $p \ge 2 j - 3 , R ( z$ $R ( z )$ is $I$ -stable,and thecoefficientsof $Q ( z )$ have alternating signs. Then, $R ( z )$ is $A$ -stable.

Proof.For $p \geq 2 j - 3$ the argument of the foregoing proof is still valid. However Proposition 3.6 is no longer applicable and we need the hypothesis on $I$ -stability.

We see from Fig.4.2 that all poles and all zeros for Padé approximations must be simple. Whenever two poles coalesce, the corresponding sectors create a bounded white finger between them with the need for an additional zero. Thus the presence of multiple zeros or poles will require an order reduction.

Theorem 4.11. Let $R ( z )$ possess $k _ { 0 }$ distinct zeros and $j _ { 0 }$ distinct poles. Then, $p \leq k _ { 0 } + j _ { 0 }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/2561eecb3c37c7a2b26e1830ecffb96105ace9e7a920274531a4aeb38f4be604.jpg)  
Fig.4.4. Order star on Gaussian sphere

Proof. We identify the complex plane with the Gaussian sphere and the order star with a CW-complex decomposition of this sphere (Fig. 4.4). Let $s _ { 2 }$ be the number of 2-cells $f _ { i } , s _ { 1 }$ the number of 1-cells $l _ { i }$ (paths),and $s _ { 0 }$ the number of vertices. Then Euler's polyhedral formula ( ${ } ^ { 6 6 } \mathrm { S i }$ enim numerus angulorum solidorum fuerit $= S$ , numerus acierum $= A$ et numerus hedrarum $= H$ , semper habetur $S + H =$ $A + 2$ , hincque vel $S = A + 2 - H$ vel $H = A + 2 - S$ vel $A = S + H - 2$ ,quae relationis simplicitas ob demonstrationis difficultatem ...",Euler(1752)),implies

$$
s _ { 0 } - s _ { 1 } + s _ { 2 } = 2 .
$$

Modern versions are in any book on algebraic topology,for particularly easy read-ing see e.g. Massey (1980, p.87, Corollary 4.4). Formula (4.9) is only true if all $f _ { i }$ are homeomorphic to disks. Otherwise, they have to be cut into disks by additional paths (dotted in Fig. 4.4). So, in general, we have

$$
s _ { 0 } - s _ { 1 } + s _ { 2 } \geq 2 .
$$

Since each vertex is reached by at least 2 paths, the origin by hypothesis by $2 p + 2$ ， and since every path has two extremities, we have

$$
s _ { 1 } - s _ { 0 } \geq p .
$$

By Lemma 4.5 each 2-cell, with the exception of two (the two “infinite"ones) must contain at least a pole or a zero, so we have

$$
s _ { 2 } \leq k _ { 0 } + j _ { 0 } + 2 .
$$

These three inequalities give $p \leq k _ { 0 } + j _ { 0 }$

# Stability of Padé Approximations

... evidence is given to suggest that these are the only L-acceptable Padé approximations to the exponential.

(B.L.Ehle 1973)

Theorem 4.12. A Padé approximation $R _ { k j } ( z )$ ， given in (3.30), is A-stable if and only if $k \leq j \leq k + 2$ . All zeros and all poles are simple.

Proof. The “if-part is a consequence of Theorem 4.9. The “only if"-part follows from Theorem 4.6 since $p = k + j$ . For the same reason Theorem 4.11 shows that all poles and zeros are simple. □

# Comparing Stability Domains

Da ist der allerärmste Mann dem ander'n viel zu reich, das Schicksal setzt den Hobel an und hobelt beide gleich.

(F.Raimund,das Hobellied)

Jeltsch & Nevanlinna (1978) proved the following“disk theorem": If $S$ is the stability domain of an s -stage explicit Runge-Kutta method and $D$ the disk with centre -s and radius s (i.e the stability domain of $s$ explicit Euler steps with step size $h / s )$ ,then

$$
S \nsim D
$$

unless $S = D$ and the method in question is Euler's method. This curious result expresses the fact that Euler's method is “the most stable” of all methods with equal numerical work. After the discovery of order stars it became clear that the result is much more general and that any method has the same property (Jeltsch & Nevanlinna 1981). We shall also see in Chapter V that this result generalizes to many multistep methods. The main tool of this theory is

Definition 4.13. Let $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ be rational approximations to $e ^ { z }$ ,then their relative order star is defined as

$$
B = \left. z \in \mathbb { C } \textrm { ; } \left| \frac { R _ { 1 } ( z ) } { R _ { 2 } ( z ) } \right| > 1 \right. .
$$

Here, the stability function for method 1 is compared to the stability function for method 2 instead of to the exact solution $e ^ { z }$ . The following order relations

lead, by subtraction, to

$$
\begin{array} { r } { e ^ { z } - R _ { 1 } ( z ) = C _ { 1 } z ^ { p _ { 1 } + 1 } + \dots } \\ { e ^ { z } - R _ { 2 } ( z ) = C _ { 2 } z ^ { p _ { 2 } + 1 } + \dots . } \end{array}
$$

$$
\frac { R _ { 1 } ( z ) } { R _ { 2 } ( z ) } = 1 - C z ^ { p + 1 } + . . .
$$

where $p = \operatorname* { m i n } ( p _ { 1 } , p _ { 2 } )$ and

$$
C = \left\{ \begin{array} { l l } { C _ { 1 } - C _ { 2 } } & { \mathrm { i f } \ p _ { 1 } = p _ { 2 } } \\ { C _ { 1 } } & { \mathrm { i f } \ p _ { 1 } < p _ { 2 } } \\ { - C _ { 2 } } & { \mathrm { i f } \ p _ { 1 } > p _ { 2 } . } \end{array} \right.
$$

Remark 4.14. The statement of Lemma 4.3 remains unchanged for $B$ ，whenever $C \neq 0$ . Since the fraction $R _ { 1 } ( z ) / R _ { 2 } ( z )$ has no essential singularity at infinity, there is no analogue of Lemma 4.4. Further, the boundedness assumption on $\boldsymbol { F }$ can be omitted in Lemmas 4.5 and $4 . 5 '$ (if $\infty$ is a pole of $R _ { 1 } ( z ) / R _ { 2 } ( z )$ , it has to be counted also). With the correspondences displayed in Table 4.1, the statements of Theorems 4.6 and 4.7 remain true for $B$ .

Table 4.1. Correspondences between $A$ and $B$   

<table><tr><td>order star A (4.1)</td><td>←</td><td>relative order star B (4.13)</td></tr><tr><td>imaginary axis</td><td>←</td><td>aS2</td></tr><tr><td>Ci</td><td>←→</td><td>interior of S2</td></tr><tr><td>C+</td><td>←→</td><td>exterior of S2</td></tr><tr><td>method A-stable</td><td>←</td><td>S1U S2</td></tr><tr><td>p</td><td>←</td><td>min(p1,P2)</td></tr></table>

Theorem 4.15. If $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ are polynomial stability functions of degree s and orders $\geq 1$ ,then the corresponding stability domains satisfy

$$
S _ { 1 } \not \supset S _ { 2 } \qquad a n d \qquad S _ { 1 } \not \subset S _ { 2 } .
$$

Proof. Suppose that $S _ { 1 } \supset S _ { 2 }$ (i.e., by Table 4.1, suppose “ $A$ -stability"). Then the analogue of Theorem 4.7 requires that $R _ { 1 } ( z ) / R _ { 2 } ( z )$ have a pole outside $S _ { 2 }$ . Since

$R _ { 1 } ( z )$ and $R _ { 2 } \{ z \}$ have the same degree, $R _ { 1 } ( z ) / R _ { 2 } ( z )$ has no pole at infinity. Therefore the only poles of $R _ { 1 } ( z ) / R _ { 2 } ( z )$ are the zeros of $R _ { 2 } \{ z \}$ and these are inside $S _ { 2 }$ . This is a contradiction and proves the first part of (4.16). The second part is obtained by exchanging $R _ { 1 } ( z )$ and $R _ { 2 } ( z )$ □

In order to compare numerical methods with different numerical work, we consider scaled stability domains.

Definition 4.16. Let $R \{ z \}$ be the stability function of degree $s$ of an explicit Runge-Kutta method (usually with $s$ stages), then

$$
S ^ { s c a l } = \left\{ z \ ; \ | R ( s z ) | \leq 1 \right\} = \left\{ z \ ; \ s \cdot z \in S \right\} = \frac { 1 } { s } S
$$

will be called the scaled stability domain of the method.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/2febbcb81146ca03c14f1f7778f884448dd145e45a8e0f48f63cd767166733d6.jpg)  
Fig. 4.5. Scaled stability domains for Taylor methods (2.12)

Theorem 4.17 (Jeltsch & Nevanlinna 1981). If $R _ { 1 } ( z )$ and $R _ { 2 } \{ z \}$ are the stability functions of degrees $s _ { 1 }$ resp. $s _ { 2 }$ of two explicit Runge-Kutta methods of orders $\geq 1$ , then

$$
S _ { 1 } ^ { s c a l } \not \supset S _ { 2 } ^ { s c a l } \qquad a n d \qquad S _ { 1 } ^ { s c a l } \not \subset S _ { 2 } ^ { s c a l } ,
$$

i.e., a scaled stability domain can never completely contain another.

The interesting interpretation of this result is that for any two methods, there exists a differential equation $y \prime = \lambda y$ such that one of them performs better than the other.No “miracle” method is possible.

Proof. We compare $s _ { 2 }$ steps of method 1 with step size $h / s _ { 2 }$ to $s _ { 1 }$ steps of method 2 with step size $h / s _ { 1 }$ . Both procedures then have comparable numerical work for the same advance in step size. Applied to $y ^ { \prime } = \lambda y$ , this compares

$$
\left( R _ { 1 } \big ( \frac { z } { s _ { 2 } } \big ) \right) ^ { s _ { 2 } } \qquad 1 0 \qquad \left( R _ { 2 } \big ( \frac { z } { s _ { 1 } } \big ) \right) ^ { s _ { 1 } }
$$

of the same degree. Theorem 4.15 now gives

$$
s _ { 2 } \cdot S _ { 1 } \ \not \supset \ s _ { 1 } \cdot S _ { 2 } \qquad \mathrm { o r } \qquad S _ { 1 } ^ { s c a l } \not \supset S _ { 2 } ^ { s c a l } .
$$

As an illustration to this theorem,we present in Fig.4.5 the scaled stability domains for the Taylor methods of orders 1,2,3,4 (compare with Fig.2.1). It can clearly be observed that none of them contains another.

# Rational Approximations with Real Poles

The surprising result is that the maximum reachable order is $m + 1$ ， (Ngrsett & Wolfbrandt 1977)

The stability functions of diagonally implicit Runge-Kutta methods (DIRK methods), i.e., methods with $a _ { i j } = 0$ for $i < j$ ,are

$$
R ( z ) = \frac { P ( z ) } { ( 1 - \gamma _ { 1 } z ) ( 1 - \gamma _ { 2 } z ) \ldots ( 1 - \gamma _ { s } z ) } ,
$$

where $\gamma _ { i } = a _ { i \ i } \ ( i = 1 , \dots , s )$ and degree $P \leq s$ . This follows at once from Formula (3.3) of Proposition 3.2, since the determinant of a triangular matrix is the product of its diagonal elements. Thus $R ( z )$ possesses real poles $1 / \gamma _ { 1 } , 1 / \gamma _ { 2 } , \ldots , 1 / \gamma _ { s } .$ Such approximations to $e ^ { z }$ will also appear in the next sections as stability func-tions of Rosenbrock methods and so-called singly-implicit Runge-Kutta methods. They thus merit a more thorough study. Research on these real-pole approximations was started by Ngrsett (1974) and Wolfbrandt (1977). Many results are collected in their joint paper Norsett & Wolfbrandt (1977).

If the method is of order at least $s$ ， $P ( z )$ is given by (3.18). We shall here, and in the sequel, very often write the formulas for $s = 3$ without always mentioning how trivial their extension to arbitrary $s$ is. Hence for $s = 3$

$$
R ( z ) = \frac { 1 + z \Big ( \displaystyle \frac { S _ { 0 } } { 1 ! } - \displaystyle \frac { S _ { 1 } } { 0 ! } \Big ) + z ^ { 2 } \Big ( \displaystyle \frac { S _ { 0 } } { 2 ! } - \displaystyle \frac { S _ { 1 } } { 1 ! } + \displaystyle \frac { S _ { 2 } } { 0 ! } \Big ) + z ^ { 3 } \Big ( \displaystyle \frac { S _ { 0 } } { 3 ! } - \displaystyle \frac { S _ { 1 } } { 2 ! } + \displaystyle \frac { S _ { 2 } } { 1 ! } - \displaystyle \frac { S _ { 3 } } { 0 ! } \Big ) } { 1 - z S _ { 1 } + z ^ { 2 } S _ { 2 } - z ^ { 3 } S _ { 3 } }
$$

where

$$
S _ { 0 } = 1 , \qquad S _ { 1 } = \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } , \qquad S _ { 2 } = \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } , \qquad S _ { 3 } = \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } .
$$

The error constant is for ${ p } = s$

$$
C = { \frac { S _ { 0 } } { 4 ! } } - { \frac { S _ { 1 } } { 3 ! } } + { \frac { S _ { 2 } } { 2 ! } } - { \frac { S _ { 3 } } { 1 ! } } .
$$

Theorem 4.18. Let $R ( z )$ be an approximation to $e ^ { z }$ of order $p$ with real poles only and let $k$ be the degree of its numerator. Then,

$$
p \leq k + 1 .
$$

Proof. If a sector of the order star $A$ ends up with a pole on the real axis, then by symmetry the complex conjugate sector must join the first one. All white sectors enclosed by these two must therefore be finite (Fig.4.6.). The same is true for sectors joining the infinite part of $A$ . There is thus on each side of the real axis at most one white sector which can be infinite. Thus the remaining $p - 1$ white sectors require together at least $p - 1$ zeros by Lemma 4.5, i.e., we have $p - 1 \leq k$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/d435798c465addee2a3eaedcbc1b6ceb92f6983f32220a511f6bf08375d32eae.jpg)  
Fig.4.6. An approximation with real poles, 3 zeros, order 4

Remark 4.19. If $p { \ge } k$ , then at least one white sector must be unbounded. This is then either the first sector on the positive real axis, or, by symmetry, there is a pair of two sectors. By the proof of Theorem 4.18 the pair is unique and we shall call it Cary Grant's part.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/17f7d7a12b47252512fe3123ad49db2af64f8062e9c55d1472c16e70edb30148.jpg)

Remark 4.20. If $p = k + 1$ , the optimal case, there are $k + 2$ white sectors, two of them are infinite. Hence each of the remaining $k$ sectors must then contain exactly one root of $P ( z )$ . As a consequence, $C < 0$ iff $P ( z )$ has no positive real root between the origin and the first pole.

# The Real-Pole Sandwich

We now analyze the approximations (4.19) with order $p \geq s$ in more detail (Ngrsett & Wanner 1979). We are interested in two sets:

Definition 4.21. Let $L$ be the set of $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ for which $\deg P ( z )$ in (4.20) is $\leq s - 1$ ,i.e., $R ( \infty ) = 0$ for $\gamma _ { i } \neq 0 ~ ( i = 1 , \ldots , s )$

Definition 4.22. Denote by $H$ the set of $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ for which the error constant (4.21) is zero, i.e., for which the approximation has highest possible order $p =$ $s + 1$ ，

A consequence of Theorem 4.18 is

$$
L \cap H = \emptyset .
$$

Written for the case $s = 3$ (generalizations to arbitrary $s$ are straightforward) and using (4.20) and (4.21) the sets $L$ and $H$ become

$$
\begin{array} { r } { L = \Big \{ ( \gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } ) ; \frac { 1 } { 3 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } } { 2 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } } { 1 ! } - \frac { \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } } { 0 ! } = 0 \Big \} } \\ { H = \Big \{ ( \gamma _ { 1 } , \gamma _ { 2 } , \gamma _ { 3 } ) ; \frac { 1 } { 4 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } + \gamma _ { 3 } } { 3 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } + \gamma _ { 1 } \gamma _ { 3 } + \gamma _ { 2 } \gamma _ { 3 } } { 2 ! } - \frac { \gamma _ { 1 } \gamma _ { 2 } \gamma _ { 3 } } { 1 ! } = 0 \Big \} . } \end{array}
$$

Theorem 4.23 (Ngrsett & Wanner 1979). The surfaces $H$ and $I$ are each composed of $s$ disjoint connected sheets

$$
L = L _ { 1 } \cup L _ { 2 } \cup . . . \cup L _ { s } , \qquad H = H _ { 1 } \cup H _ { 2 } \cup . . . \cup H _ { s } .
$$

Ifa direction $\boldsymbol { \delta } = ( \delta _ { 1 } , \dots , \delta _ { s } )$ is chosen with all $\delta _ { \imath } \neq 0$ and if $k$ ofthem are positive, then the ray

$$
X = \left\{ ( \gamma _ { 1 } , \dots , \gamma _ { s } ) ; \quad \gamma _ { \imath } = t \delta _ { \imath } , 0 \leq t < \infty \right\}
$$

intersects the sheets $H _ { 1 } , L _ { 1 } , H _ { 2 } , L _ { 2 } , . . . , H _ { k } , L _ { k }$ in this order and no others.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/56ad069f5acd9ed65bcae742761df25c8d91c1d1042b9d8ee40888de374a53b4.jpg)  
Fig.4.7. Formation of the sandwich

Proof. When the $\delta _ { \iota }$ have been chosen,inserting $\gamma _ { \imath } = t \delta _ { \imath }$ into (4.23) gives

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 3 ! } - t \frac { \delta _ { 1 } + \delta _ { 2 } + \delta _ { 3 } } { 2 ! } + t ^ { 2 } \frac { \delta _ { 1 } \delta _ { 2 } + \delta _ { 1 } \delta _ { 3 } + \delta _ { 2 } \delta _ { 3 } } { 1 ! } - t ^ { 3 } \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 0 ! } = 0 } \\ { \displaystyle \frac { 1 } { 4 ! } - t \frac { \delta _ { 1 } + \delta _ { 2 } + \delta _ { 3 } } { 3 ! } + t ^ { 2 } \frac { \delta _ { 1 } \delta _ { 2 } + \delta _ { 1 } \delta _ { 3 } + \delta _ { 2 } \delta _ { 3 } } { 2 ! } - t ^ { 3 } \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 1 ! } = 0 } \end{array}
$$

for $L$ and $H$ , respectively. These are third (in general $s$ th) degree polynomials whose positive roots we have to study. We vary the $\delta \mathbf { \dot { s } } _ { \mathrm { \scriptsize { : } } }$ ，and hence the ray $X$ ， starting with all $\delta \mathbf { \hat { s } }$ negative. The polynomials (4.26) then have all coeficients positive and obviously no positive real roots. When now one delta, say $\delta _ { 3 }$ , changes sign, the leading coefficients of (4.26) become zero and one root becomes infinite for each equation and satisfies asymptotically

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/32389165b20953684959f68edd5da660d2b3b1bcb106b701ba7d3c279945a907.jpg)  
Fig.4.8. The sandwich for $s = 3 \ldots$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/7b1ad9665a126d38e562c0045379ff23f070bd34e0c6e881b4dbf9142b8c934f.jpg)  
and for $s = 5$

$$
\begin{array} { r l r } { \frac { \delta _ { 1 } \delta _ { 2 } } { 1 ! } - t \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 0 ! } \approx 0 } & { { } } & { \Longrightarrow } & { { } \quad t \approx \frac { 1 } { \delta _ { 3 } } } \\ { \frac { \delta _ { 1 } \delta _ { 2 } } { 2 ! } - t \frac { \delta _ { 1 } \delta _ { 2 } \delta _ { 3 } } { 1 ! } \approx 0 } & { { } } & { \Longrightarrow } & { { } \quad t \approx \frac { 1 } { 2 \delta _ { 3 } } } \end{array}
$$

for $L$ and $H$ , respectively. Thus $H$ comes below and $L$ comes above. Because of $L \cap H = \emptyset$ (4.22) these two roots can never cross and must therefore remain in this configuration (see Fig. 4.7).

When then successively $\delta _ { 2 }$ and $\delta _ { \mathbf { 1 } }$ change sign, the same scene repeats itself again and again, always two sheets of $H$ and $I$ descend from above in that order and are layed on the lower sheets like slices of bread and ham of a giant sandwich. Because $L \cap H = \emptyset$ , these sheets can never cross, two roots for $I$ or $H$ can never come together and become complex. So all roots must remain real and the theorem must be true.

A three-dimensional view of these surfaces is given in Fig.4.8.

The following theorem describes the form of the corresponding order star in all these sheets.

Theorem 4.24. Let $G _ { 1 } , \ldots , G _ { s }$ be the open connected components of $\mathbb { R } ^ { s } \backslash H$ such that $L _ { \imath }$ lies in $G _ { \imath }$ , and let $G _ { 0 }$ be the component containing the origin. Then the order star of $R ( z )$ given by (4.20) possesses exactly $k$ bounded fingers to the right of Cary Grant's part if and only if

$$
( \gamma _ { 1 } , \dots , \gamma _ { s } ) \in G _ { k } \cup H _ { k } .
$$

Proof. We prove this by a continuity argument letting the point $( \gamma _ { 1 } , \dots , \gamma _ { s } )$ travel through the sandwich. Since Cary Grant's part is always present (Remark 4.19), the number of bounded sectors can change only where the error constant $C$ (4.21) changes sign,i.e., on the surfaces $H _ { 1 } , H _ { 2 } , \dots , H _ { s }$ . Fig. 4.9 gives some snap-shots from this voyage for $s = 3$ and $\gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma$ . In this case the equations (4.23) become

$$
\begin{array} { c } { { \displaystyle { \frac { 1 } { 3 ! } } - { \frac { 3 \gamma } { 2 ! } } + { \frac { 3 \gamma ^ { 2 } } { 1 ! } } - { \frac { \gamma ^ { 3 } } { 0 ! } } = 0 } } \\ { { \displaystyle { \frac { 1 } { 4 ! } } - { \frac { 3 \gamma } { 3 ! } } + { \frac { 3 \gamma ^ { 2 } } { 2 ! } } - { \frac { \gamma ^ { 3 } } { 1 ! } } = 0 } } \end{array}
$$

whose roots

$$
\begin{array} { r l r l r l } & { \lambda _ { 1 } = 0 . 1 5 8 9 8 4 , \quad } & { \lambda _ { 2 } = 0 . 4 3 5 8 6 7 , \quad } & { \lambda _ { 3 } = 2 . 4 0 5 1 5 } \\ & { \chi _ { 1 } = 0 . 1 2 8 8 8 6 , \quad } & { \chi _ { 2 } = 0 . 3 0 2 5 3 5 , \quad } & { \chi _ { 3 } = 1 . 0 6 8 5 8 } \end{array}
$$

do interlace nicely as required by Theorem 4.23. The afrmation of Theorem 4.24 for $s = 3$ can be clearly observed in Fig.4.9.

For the proof of the general statement we also put $\gamma _ { 1 } = . . . = \gamma _ { s } = \gamma$ and investigate the two extreme cases:

1. $\gamma = 0 \colon \mathrm { H e r e } \ R ( z )$ is the Taylor polynomial $1 + z + \dots + z ^ { s } / s !$ whose order star has no bounded sector at all.

2. $\gamma \to \infty$ : The numerator of $R ( z )$ in (4.20) becomes for $s = 3$

$$
P ( z ) = 1 + z \Big ( \frac { 1 } { 1 ! } - \frac { 3 \gamma } { 0 ! } \Big ) + z ^ { 2 } \Big ( \frac { 1 } { 2 ! } - \frac { 3 \gamma } { 1 ! } + \frac { 3 \gamma ^ { 2 } } { 0 ! } \Big ) + z ^ { 3 } \Big ( \frac { 1 } { 3 ! } - \frac { 3 \gamma } { 2 ! } + \frac { 3 \gamma ^ { 2 } } { 1 ! } - \frac { \gamma ^ { 3 } } { 0 ! } \Big ) .
$$

If we let $\gamma \to \infty$ , this becomes with $z \gamma = w$

$$
1 - w \Big ( 3 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) + w ^ { 2 } \Big ( 3 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) - w ^ { 3 } \Big ( 1 + \mathcal { O } \big ( \frac { 1 } { \gamma } \big ) \Big ) .
$$

Therefore all roots $w _ { i } \to 1$ ,hence $z _ { \imath }  1 / \gamma$ (see the last picture of Fig.4.9). Therefore no zero of $R ( z )$ can remain left of Cary Grant's part and we have $s$ bounded fingers.

Since between these extreme cases, there are at most $s$ crossings of the surface $H$ , Theorem 4.24 must be true. □

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/33de41f42dc6bea76acfd837a96054640f1391ae85c2f0073f26e41a586dc049.jpg)  
Fig. 4.9. Order stars for $\gamma$ travelling through the sandwich

Theorem 4.25. The function $R ( z )$ defined by (4.20) can be $I$ -stable only if

$$
( \gamma _ { 1 } , \dots , \gamma _ { s } ) \in H _ { q } \cup G _ { q } \cup H _ { q + 1 } \qquad i f \ s = 2 q - 1
$$

and

$$
\begin{array} { r } { ( \gamma _ { 1 } , \ldots , \gamma _ { s } ) \in G _ { q } \cup H _ { q + 1 } \cup G _ { q + 1 } \quad i f \ s = 2 q . } \end{array}
$$

Proof. The reason for this result is similar to Theorem 4.12. For $\boldsymbol { I }$ -stability the imaginary axis cannot intersect the order star and must therefore reach the origin through Cary Grant's part. Thus $I$ -stability (and hence $A$ -stability) is only possible (roughly) in the middle of the sandwich. Since at most $\{ ( p + 2 ) / 2 \}$ and at least $\{ ( p + 1 ) / 2 \}$ of the $p + 1$ sectors of $A$ start in $\mathbb { C } ^ { + }$ , the number $k$ of bounded fingers satisfies

$$
\left[ { \frac { p + 2 } { 2 } } \right] \geq k \qquad { \mathrm { a n d } } \qquad \left[ { \frac { p + 1 } { 2 } } \right] \leq k .
$$

Inserting $p = s + 1$ on $H$ and $p = s$ on $G$ we get the above results.

# Multiple Real-Pole Approximations

... the next main result is obtained, saying that the least value of $C$ is obtained when all the zeros of the denominator are equal (Ngrsett & Wolfbrandt 1977)

Approximations for whichall poles are equal,i.e.,for which $\gamma _ { 1 } = \gamma _ { 2 } = . ~ . ~ = \gamma _ { s } = \gamma$ are called “multiple" real-pole approximations (Ngrsett 1974). We again consider only approximations for which the order is $\geq s$ . These satisfy, for $s = 3$ ，

$$
R ( z ) = \frac { P ( z ) } { ( 1 - \gamma z ) ^ { 3 } }
$$

where $P ( z )$ is given by (4.3O),and their error constant is

$$
C = \frac { 1 } { 4 ! } - \frac { 3 \gamma } { 3 ! } + \frac { 3 \gamma ^ { 2 } } { 2 ! } - \frac { \gamma ^ { 3 } } { 1 ! } .
$$

Approximations with multiple poles have many computational advantages (the linear systems to be solved in Rosenbrock or DIRK methods have all the same matrix (see Sections IV.6 and IV.7)). We are now pleased to see that they also have the smallest error constants (Ngrsett & Wolfbrandt 1977).

Theorem 4.26. On each ofthe surfaces $L _ { \imath }$ and $H _ { \imath }$ $\mathcal { I } _ { \iota } \left( i = 1 , \dots , s \right)$ the error constant $C$ of(4.20) is minimized (in absolute value) when $\gamma _ { 1 } = \gamma _ { 2 } = . \cdot . = \gamma _ { s }$

Proof. Our proof uses relative order stars (similar to (4.13))

$$
B = \Big \{ z \in \mathbb { C } \ ; \ | q ( z ) | > 1 \Big \} , \qquad q ( z ) = \frac { R _ { n e w } ( z ) } { R _ { o l d } ( z ) } ,
$$

where $R _ { o l d } ( z )$ is a real-pole approximation of order $p = s + 1$ corresponding to $\gamma _ { 1 } , \ldots , \gamma _ { s }$ and $R _ { n e w } ( z )$ is obtained by an infinitely small change of the $\gamma \mathbf { \bar { s } }$ We assume that not all $\gamma _ { \imath }$ are identical and shall show that then the error constant can be decreased. After a permutation of the indices, we assume $\gamma _ { 1 } = \operatorname* { m a x } ( \gamma _ { \imath } )$ (by Theorem $4 . 2 3 \ \gamma _ { 1 } > 0$ ,so that $1 / \gamma _ { 1 }$ represents the pole on the positive real axis which is closest to the origin) and $\gamma _ { s } < \gamma _ { 1 }$ . We don't allow arbitrary changes of the $\gamma \mathbf { \bar { s } }$ but we decrease $\gamma _ { 1 }$ ,keep $\gamma _ { 2 } , \ldots , \gamma _ { s - 1 }$ fixed and determine $\gamma _ { s }$ by the defining equations for $H$ (see (4.23)). For example, for $s = 3$ we have

$$
\gamma _ { 3 } = \frac { \displaystyle \frac { 1 } { 4 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } } { 3 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } } { 2 ! } } { \displaystyle \frac { 1 } { 3 ! } - \frac { \gamma _ { 1 } + \gamma _ { 2 } } { 2 ! } + \frac { \gamma _ { 1 } \gamma _ { 2 } } { 1 ! } } .
$$

Since the poles and zeros of $R _ { o l d } ( z )$ depend continuously on the $\gamma _ { \imath }$ ， poles and zeros of $q ( z )$ appear always in pairs (we call them dipoles). By the maximum principle or by Remark 4.14,each boundary curve of $B$ leaving the origin must lead to at least one dipole before it rejoins the origin. Since there are $s + 2 = p + 1$ dipoles of $q ( z )$ (identical poles for $R _ { o l d } ( z )$ and $R _ { n e w } ( z )$ don't give rise to a dipole of $q ( z ) )$ and $p + 1$ pairs of boundary curves of $B$ leaving the origin (Remark 4.14), each such boundary curve passes through exactly one dipole before rejoining the origin. As a consequence no boundary curve of $B$ can cross the real axis except at dipoles.

If the error constant of $R _ { o l d } ( z )$ satisfies $C _ { o l d } < 0$ ，then,by Remark 4.20, $R _ { o l d } ( z )$ has no zero between $1 / \gamma _ { 1 }$ and the origin. Therefore also $q ( z )$ possesses no dipole in this region. Since the pole of $R _ { n e w } ( z )$ is slightly larger than $1 / \gamma _ { 1 }$ (that of $R _ { o l d } ( z ) )$ , the real axis between $1 / \gamma _ { 1 }$ and the origin must belong to the complement of $B$ . Thus we have $C _ { n e w } - C _ { o l d } > 0$ by (4.14) and (4.15).

If $C _ { o l d } > 0$ there is one additional dipole of $q ( z )$ between $1 / \gamma _ { 1 }$ and the origin (see Remark 4.2O). As above weconclude this time that $C _ { n e w } - C _ { o l d } < 0$

In both cases $| C _ { n e w } | < | C _ { o l d } |$ , since by continuity $C _ { n e w }$ is near to $C _ { o l d }$ As a consequence no $( \gamma _ { 1 } , \dotsc , \gamma _ { s } ) \in H$ with at least two different $\gamma _ { \imath }$ can minimize the error constant. As it becomes large in modulus when at least one $\gamma _ { \imath }$ tends to $\infty$ (this follows from Theorem 4.18 and from the fact that in this case $R ( z )$ tends to an approximation with $s$ replaced by $s - 1 )$ the minimal value of $C$ must be attained when all poles are identical.

The proof for $L$ is the same, there are only $s - 1$ zeros of $R ( z )$ and the order is $p = s$ □

An illustration of the order star $B$ compared to $A$ is given in Fig.4.10. Another advantage of multiple real-pole approximations is exhibited by the following theorem:

Theorem 4.27 (Keeling 1989). On each surface $H _ { \imath } \cap \{ ( \gamma _ { 1 } , \ldots , \gamma _ { s } ) ; \gamma _ { \jmath } > 0 \}$ the value $\mid R ( \infty ) \mid$ of (4.20) is minimized when $\gamma _ { 1 } = \gamma _ { 2 } = . ~ . . = \gamma _ { s }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/0ef5519a7c6a93a73057d011a8c3cbed782710be02efba660c928040fb004c9a.jpg)  
Fig. 4.10. Order star $A$ compared to $B$

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>left pictures: Cold &lt; 0</td><td rowspan=1 colspan=1>right pictures: Cold &gt; 0</td></tr><tr><td rowspan=1 colspan=1>Rold</td><td rowspan=1 colspan=1>Y1 =1.272 = 1.1Y3 = 0.9455446</td><td rowspan=1 colspan=1>Y1 = 0.3572 =0.33Y3 =0.2406340</td></tr><tr><td rowspan=1 colspan=1>Rnew</td><td rowspan=1 colspan=1>Y1 = 1.1772 = 1.1Y3 =0.9628661</td><td rowspan=1 colspan=1>Y1 = 0.34572 = 0.33Y3 = 0.2440772</td></tr></table>

Proof. The beginning of the proof is identical to that of Theorem 4.26. Besides $1 / \gamma _ { 1 }$ and $1 / \gamma _ { s }$ there is at best an even number of dipoles on the positive real axis to the right of $1 / \gamma _ { 1 }$ . As in the proof above we conclude that a right-neighbourhood of $1 / \gamma _ { 1 }$ belongs to $B$ so that $\infty$ must lie in its complement (cf. Fig.4.10). This implies

$$
\mid R _ { n e w } ( \infty ) \mid < \mid R _ { o l d } ( \infty ) \mid
$$

As a consequence no element of $H \cap \{ ( \gamma _ { 1 } , \cdot \cdot \cdot , \gamma _ { s } ) ; \ \gamma _ { j } > 0 \}$ with at least two $\gamma _ { j }$ different can minimize $\mid R ( \infty ) \mid$ .Also $| R ( \infty ) \ |$ increases if $\gamma _ { 1 }  \infty$ . The statement now follows from the fact that $| R ( \infty ) \mid$ tends to infinity when at least one $\gamma _ { j }$ approaches zero. □

# Exercises

1. (Ehle 1968)． Compute the polynomial $E ( y )$ for the third and fourth Padé subdiagonal $R _ { k , k + 3 } ( z )$ and $R _ { k , k + 4 } ( z )$ (which, by Proposition 3.4 consists of two terms only). Show that these approximations violate (3.6) and cannot be $A$ -stable.

2.Prove the general formula

$$
E ( y ) = \Big ( \frac { k ! } { ( k + j ) ! } \Big ) ^ { 2 } \sum _ { r = \big [ ( k + j + 2 ) / 2 \big ] } ^ { j } \frac { ( - 1 ) ^ { j - r } } { ( j - r ) ! } \Bigg ( \prod _ { q = 1 } ^ { j - r } ( j - q + 1 ) ( k + q ) ( r - k - q ) \Bigg ) y ^ { 2 r }
$$

for the Padé approximations $R _ { k j } \ ( j \geq k )$

3. (For the fans of mathematical precision). Derive the following formulas for the roots $\lambda _ { i }$ and $\chi _ { \imath }$ of(4.28)

$$
\begin{array} { l l l } { { \chi _ { 1 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { 1 3 \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 1 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta + 2 \pi } { 3 } \Big ) , } } \\ { { \chi _ { 2 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { 2 5 \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 2 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta + 4 \pi } { 3 } \Big ) , } } \\ { { \chi _ { 3 } = \displaystyle \frac { 1 } { 2 } + \frac { 1 } { \sqrt { 3 } } \cos \displaystyle \frac { \pi } { 1 8 } , } } & { { } } & { { \lambda _ { 3 } = 1 + \sqrt { 2 } \cos \Big ( \displaystyle \frac { \theta } { 3 } \Big ) , } } \end{array}
$$

where $\theta = \arctan ( \sqrt { 2 } / 4 )$

Hint. Use the Cardano-Viete formula (e.g., Hairer & Wanner (1995), page 66).

4．Prove that all zeros of

$$
\frac { x ^ { s } } { s ! } - S _ { 1 } \frac { x ^ { s - 1 } } { ( s - 1 ) ! } + S _ { 2 } \frac { x ^ { s - 2 } } { ( s - 2 ) ! } - \ldots \pm S _ { s }
$$

are real and distinct whenever all zeros of

$$
Q ( z ) = 1 - z S _ { 1 } + z ^ { 2 } S _ { 2 } - \ldots \pm z ^ { s } S _ { s } , \qquad S _ { s } \neq 0
$$

are real. Also,both polynomials have the same number of positive (and negative) zeros (Ngrset & Wanner 1979,Bales,Karakashian & Serbin 1988).

Hint. Apply Theorem 4.23. This furnishes a geometric proof of a classical result (see e.g., Pólya & Szegoö (1925), Volume II, Part V, No.65) and allows us to interpret $R ( z )$ as the stability function of a (real) collocation method.

5. Prove that $( \gamma , \dots , \gamma ) \in L$ (Definition 4.21) if and only if $L _ { s } ( 1 / \gamma ) = 0$ ,where $L _ { s } ( x )$ denotes the Laguerre polynomial of degree $s$ (see Abramowitz & Stegun (1964),Formula 22.3.9 or Formula (6.11) below).

# IV.5 Construction of Implicit Runge-Kutta Methods

Although most of these methods appear at the moment to be largely of theoretical interest ... (B.L. Ehle 1968)

In Sect. II.7 the first implicit Runge-Kutta methods were introduced. As we saw in Sect.IV.3, not all of them are suitable for the solution of stiff differential equations. This section is devoted to the collection of several classes of fully implicit Runge-Kutta methods possessing good stability properties.

The construction of such methods relies heavily on the simplifying assumptions

$$
\begin{array} { l l l l } { { } } & { { \displaystyle B ( p ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } = \frac { 1 } { q } } } & { { q = 1 , \ldots , p ; } } \\ { { } } & { { } } & { { } } \\ { { C ( \eta ) : } } & { { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { q - 1 } = \frac { c _ { i } ^ { q } } { q } } } & { { i = 1 , \ldots , s , \quad q = 1 , \ldots , \eta ; } } \\ { { } } & { { } } & { { } } \\ { { D ( \zeta ) : } } & { { \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } c _ { i } ^ { q - 1 } a _ { i j } = \frac { b _ { \eta } } { q } ( 1 - c _ { j } ^ { q } ) } } & { { j = 1 , \ldots , s , \quad q = 1 , \ldots , \zeta . } } \end{array}
$$

Condition $B ( p )$ simply means that the quadrature formula $( b _ { \imath } , c _ { i } )$ is of order $p$ The importance of the other two conditions is seen from the following fundamental theorem, which was derived in Sect. II.7.

Theorem 5.1(Butcher 1964). If the coefficients $b _ { i } , c _ { i } , a _ { i j }$ of a Runge-Kutta method satisfy $B ( p ) , C ( \eta ) , D ( \zeta )$ with $p \leq \eta + \zeta + 1$ and $p \leq 2 \eta + 2$ , then the method is of order $p$ □

# Gauss Methods

These processes, named “Kuntzmann-Butcher methods” in Sect.II.7, are colloca-tion methods based on the Gaussian quadrature formulas, i.e., $c _ { 1 } , \ldots , c _ { s }$ are the zeros of the shifted Legendre polynomial of degree $s$ ，

$$
{ \frac { d ^ { s } } { d x ^ { s } } } \left( x ^ { s } ( x - 1 ) ^ { s } \right) .
$$

For the sake of completeness we present the first of these in Tables 5.1 and 5.2.

Table 5.1. Gauss methods of order 2 and 4   
Table 5.2. Gauss method of order 6   

<table><tr><td></td><td>-65-6 1</td><td>4</td><td>V3 4 6</td></tr><tr><td>1</td><td>1-2 1-2 +</td><td>4 V3 +</td><td>4</td></tr><tr><td></td><td></td><td>6 1</td><td>1</td></tr></table>

<table><tr><td>1 √15 10 1 1 √15 + 10</td><td>5 36 3 V15 + 24 5 √15 + 30</td><td>2-9 √15 15 2 2-9 √15 + 15</td><td>5 √15 36 30 5 √15 36 24 5</td></tr><tr><td></td><td>5 18</td><td>4-9</td><td>36 5 18</td></tr></table>

Theorem 5.2 (Butcher 1964, Ehle 1968). The s -stage Gauss method is of order $2 s$ . Its stability function is the $\left( s , s \right)$ -Padé approximation and the method is Astable.

Proof. The order result has already been proved in Sect.II.7. Since the degrees of the numerator and the denominator are not larger than $s$ for any $s$ -stage Runge-Kutta method, the stability function of this $2 s$ -order method is the $\left( \mathscr { s } , \mathscr { s } \right)$ -Padé approximation by Theorem 3.11. $A$ -stability thus follows from Theorem 4.12.□

# Radau IA and Radau IIA Methods

Butcher (1964) introduced Runge-Kutta methods based on the Radau and Lobatto quadrature formulas. He called them processes of type I, II or III according to whether $c _ { 1 } , \ldots , c _ { s }$ are the zeros of

$$
\begin{array} { r l } & { \mathrm { I : } \quad \frac { d ^ { s - 1 } } { d x ^ { s - 1 } } \bigg ( x ^ { s } ( x - 1 ) ^ { s - 1 } \bigg ) , \quad \quad \mathrm { ( R a d a u l e f t ) } } \\ & { \mathrm { I I : } \quad \frac { d ^ { s - 1 } } { d x ^ { s - 1 } } \bigg ( x ^ { s - 1 } ( x - 1 ) ^ { s } \bigg ) , \quad \quad \mathrm { ( R a d a u r i g h t ) } } \\ & { \mathrm { I I I : } \quad \frac { d ^ { s - 2 } } { d x ^ { s - 2 } } \bigg ( x ^ { s - 1 } ( x - 1 ) ^ { s - 1 } \bigg ) . \quad \mathrm { ( L o b a t t o ) } } \end{array}
$$

The weights $b _ { 1 } , \dots , b _ { s }$ are chosen such that the quadrature formula satisfies $B ( s )$ ， which implies $B ( 2 s - 1 )$ in the Radau case and $B ( 2 s - 2 )$ in the Lobatto case (see Lemma 5.15 below). Unfortunately, none of these methods of Butcher turned out to be $A$ -stable (see e.g. Table 3.1). Ehle (1969) took up the ideas of Butcher and constructed methods of type I, II and II with excellent stability properties. Independently, Axelsson (1969) found the Radau IIA methods together with an elegant proof of their $A$ -stability.

The $s$ -stage Radau IA method is of type I, where the coefficients $a _ { i j }$ ， $( i , j =$ $1 , \ldots , s )$ are defined by condition $D ( s )$ . This is uniquely possible since the $c _ { \iota }$ are distinct and the $b _ { \imath }$ not zero. Tables 5.3 and 5.4 present the first of these methods.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/504807479b58471ad51af4181dc72bb8ecba0deacf6c466585059758ae2b410c.jpg)

Table 5.3. Radau IA methods of orders 1 and 3   
Table 5.4. Radau IA method of order 5   

<table><tr><td rowspan="6">0 6-√6 10 6+√6</td><td rowspan="5">1 9 1 1</td><td>-1-√6</td><td>-1+√6</td></tr><tr><td>18</td><td>18</td></tr><tr><td>88+7√6</td><td>88-43√6</td></tr><tr><td>360</td><td>360</td></tr><tr><td>88+43√6</td><td>88-7√6</td></tr><tr><td>10</td><td>9 360</td><td>360</td></tr><tr><td rowspan="2"></td><td>1</td><td>16+√6</td><td>16-√6</td></tr><tr><td>9</td><td>36</td><td>36</td></tr></table>

Ehle's type II processes are obtained by imposing condition $C ( s )$ . By Theorem II.7.7 this results in the collocation methods based on the zeros of (5.2). They are called Radau IIA methods. Examples are given in Tables 5.5 and 5.6. For $s = 1$ we obtain the implicit Euler method.

Theorem 5.3. The s -stage Radau IA method and the $s$ -stage Radau IIA method are of order $2 s - 1$ . Their stability function is the $( s - 1 , s )$ subdiagonal Padé approximation. Both methods are $A$ -stable.

Proof. The stated orders follow from Theorem 5.1 and Lemma 5.4 below. Since $c _ { 1 } = 0$ for the Radau IA method, $D ( s )$ with $j = 1$ and $B ( 2 s - 1 )$ imply (3.14). Similarly, for the Radau IA method, $c _ { s } = 1$ and $C ( s )$ imply (3.13).Therefore,in both cases, the numerator of the stability function is of degree $\leq s - 1$ by Proposition 3.8. The statement now follows from Theorem 3.11 and Theorem 4.12. □

Table 5.5. Radau IIA methods of orders 1 and 3   

<table><tr><td>1-3 1</td><td>52 1 12 4 1 4</td></tr><tr><td></td><td>4 4</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/af81b6851ceabdf5e1d35411a3d109df0418fbb258a09dc917aea82ec0e5bfa4.jpg)

Table 5.6. Radau IIA method of order 5   

<table><tr><td>4-√6</td><td>88-76</td><td>296-169√6</td><td>-2+3√6</td></tr><tr><td>10</td><td>360</td><td>1800</td><td>225</td></tr><tr><td>4+√6</td><td>296+169√6</td><td>88+7√6</td><td>-2-3√6</td></tr><tr><td>10</td><td>1800</td><td>360</td><td>225</td></tr><tr><td>1</td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td>9</td></tr><tr><td></td><td>16-√6</td><td>16+√6</td><td>1</td></tr><tr><td></td><td>36</td><td>36</td><td>9</td></tr></table>

Lemma 5.4. Let an $s$ -stage Runge-Kutta method have distinct $c _ { 1 } , \ldots , c _ { s }$ and nonzero weights $b _ { 1 } , \dots , b _ { s }$ . Then we have

$a$ ） $C ( s )$ and $B ( s + \nu )$ imply $D ( \nu )$ ; b) $D ( s )$ and $B ( s + \nu )$ imply $C ( \nu )$ ·

Proof. Put

$$
d _ { \jmath } ^ { ( q ) } : = \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } a _ { \imath \jmath } - \frac { b _ { \jmath } } { q } ( 1 - c _ { \jmath } ^ { q } ) .
$$

Conditions $C ( s )$ and $B ( s + \nu )$ imply

$$
\sum _ { \jmath = 1 } ^ { s } d _ { \jmath } ^ { ( q ) } c _ { \jmath } ^ { k - 1 } = 0 \qquad \mathrm { f o r } \quad k = 1 , \dots , s \mathrm { a n d } q = 1 , \dots , \nu .
$$

The vector $( d _ { 1 } ^ { ( q ) } , \dots , d _ { s } ^ { ( q ) } )$ must vanish, because it is the solution of a homoge-neous linear system with a non singular matrix of Vandermonde type. This proves $D ( \nu )$

For part (b) one defines

$$
e _ { \ i } ^ { ( \boldsymbol { q } ) } : = \sum _ { \jmath = 1 } ^ { s } a _ { \iota \jmath } c _ { \jmath } ^ { \boldsymbol { q } - 1 } - \frac { c _ { \imath } ^ { \boldsymbol { q } } } { \boldsymbol { q } }
$$

and applies a similar argument to

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } c _ { \ i } ^ { k - 1 } e _ { \ i } ^ { ( q ) } = 0 , \qquad k = 1 , \dots , s , \quad q = 1 , \dots , \nu .
$$

# Lobatto IIIA, IIIB and IIC Methods

For all type III processes the $c _ { \iota }$ are the zeros of the polynomial (5.3） and the weights $b _ { \imath }$ are such that $B ( 2 s - 2 )$ is satisfied.

The coefficients $a _ { \scriptscriptstyle { \imath \jmath } }$ are defined by $C ( s )$ for the Lobatto IIA methods. It is therefore a collocation method. For the Lobato IIIB methods we impose $D ( s )$ and, finally, for the Lobatto IIIC methods we put

$$
a _ { \imath 1 } = b _ { 1 } \quad \mathrm { f o r } \quad i = 1 , \ldots , s
$$

and determine the remaining $a _ { \imath \jmath }$ by $C ( s - 1 )$ . Ehle (1969) introduced the first two classes,and presented the IIIC methods for $s \leq 3$ . The general definition of the IIIC methods is due to Chipman (1971); see also Axelsson (1972). Examples are given in Tables 5.7-5.12.

Table 5.7. Lobatto IIA methods of orders 2 and 4   

<table><tr><td></td><td>0</td><td rowspan="8">0 0 54</td><td>0</td></tr><tr><td>0 0</td><td>0</td><td>1</td></tr><tr><td>1</td><td>1</td><td>24</td></tr><tr><td>1 1</td><td>1 1</td><td>GA 1 6</td></tr><tr><td>1-2 1 2</td><td></td><td>1 2 1 6 6</td></tr></table>

Table 5.8.Lobatto IIIA method of order 6   

<table><tr><td>0 5-√5</td><td>0 11+√5</td><td>0 25-√5</td><td>0 25-13√5</td><td>0 -1+√5</td></tr><tr><td>10</td><td>120 11-√5</td><td>120</td><td>120</td><td>120</td></tr><tr><td>5+√5 10</td><td>120</td><td>25+13√5 120</td><td>25+√5</td><td>-1-√5</td></tr><tr><td></td><td>1</td><td>5</td><td>120</td><td>120</td></tr><tr><td>1</td><td>12</td><td>12</td><td>5 12</td><td>1 12</td></tr><tr><td></td><td></td><td>5</td><td>5</td><td></td></tr><tr><td></td><td>12</td><td>12</td><td>12</td><td>1 12</td></tr></table>

Theorem 5.5. The s -stage Lobatto IIIA, IIIB and IIIC methods are of order $2 s - 2$ The stability function for the Lobatto IlIA and IIIB methods is the diagonal $( s -$ $1 , s - 1 )$ -Padé approximation. For the Lobatto IIIC method it is the $\left( s - 2 , s \right)$ -Pade approximation. All these methods are A-stable.

Proof. We first prove that the IIIC methods satisfy $D ( s - 1 )$ Condition (5.5) implies $d _ { 1 } ^ { ( q ) } = 0 ~ ( q = 1 , \dots , s - 1 )$ for $d _ { 1 } ^ { ( q ) }$ given by (5.4). Conditions $C ( s - 1 )$

Table 5.9. Lobatto IIIB methods of orders 2 and 4   

<table><tr><td colspan="3"></td><td>0</td><td></td><td>1-6 0</td></tr><tr><td>0</td><td>0</td><td></td><td>1</td><td>GR</td><td>0</td></tr><tr><td>1</td><td>1-21-2 0</td><td></td><td>1</td><td></td><td>0</td></tr><tr><td></td><td>1 1</td><td></td><td></td><td>1 2-3</td><td>1</td></tr></table>

Table 5.10.Lobatto IIIB method of order 6   

<table><tr><td>0</td><td>1 12</td><td>-1-√5 24</td><td>-1+√5 24</td><td>0</td></tr><tr><td>5-√5 10</td><td>1 12</td><td>25+√5 120</td><td>25-13√5 120</td><td>0</td></tr><tr><td>5+√5 10</td><td>1 12</td><td>25 +13√5 120</td><td>25-√5 120</td><td>0</td></tr><tr><td></td><td>1</td><td>11-√5</td><td>11+√5</td><td>0</td></tr><tr><td>1</td><td>12</td><td>24</td><td>24</td><td></td></tr><tr><td rowspan="2"></td><td>1</td><td>5</td><td>5</td><td>1</td></tr><tr><td>12</td><td>12</td><td>12</td><td>12</td></tr></table>

Table 5.11. Lobatto IIC methods of orders 2 and 4   

<table><tr><td></td><td></td><td>0</td><td>1</td><td>1-3</td><td>1-6</td></tr><tr><td rowspan="2">0</td><td>1</td><td>1</td><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td><td></td><td>12</td></tr><tr><td>1</td><td>N 1-2</td><td>1</td><td>G</td><td>1</td><td>1 6</td></tr><tr><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1 1</td><td></td><td>1-6</td><td>2-3</td><td>1</td></tr></table>

Table 5.12. Lobatto IIIC method of order 6   

<table><tr><td>0 5-√5</td><td>1 12 1</td><td>-√5 12 1</td><td>V5 12 10-7√5</td><td>1 √5</td></tr><tr><td>10</td><td>12</td><td>4</td><td>60</td><td>60</td></tr><tr><td>5+√5 10</td><td>1</td><td>10+7√5</td><td>1 4</td><td>-√5</td></tr><tr><td></td><td>12</td><td>60 5</td><td>5</td><td>60 1</td></tr><tr><td>1</td><td>1 12</td><td>12</td><td>12</td><td>12</td></tr><tr><td></td><td></td><td>5</td><td>5</td><td>1</td></tr><tr><td></td><td>1 12</td><td>12</td><td>12</td><td>12</td></tr></table>

and $B ( 2 s - 2 )$ then yield

$$
\sum _ { \ i = 2 } ^ { s } d _ { \ j } ^ { ( q ) } c _ { \ j } ^ { k - 1 } = 0 \qquad \mathrm { f o r } \quad k = 1 , \dots , s - 1 \mathrm { a n d } q = 1 , \dots , s - 1 .
$$

As in the proof of Lemma 5.4 we deduce $D ( s - 1 )$ ．All order statements now follow from Lemma 5.4 and Theorem 5.1.

By definition, the first row of the Runge-Kutta matrix $A$ vanishes for the IIIA methods,and its last column vanishes for the IIB methods. The denominator of the stability function is therefore of degree $\le s - 1$ . Similarly, the last row of $A - \mathbb { 1 } b ^ { T }$ vanishes for IIIA,and the first column of $A - \mathbb { 1 } b ^ { T }$ for IIIB.Therefore, the numerator of the stability function is also of degree $\leq s - 1$ by Formula (3.3). It now follows from Theorem 3.11 that both methods have the $( s - 1 , s - 1 )$ -Padé approximation as stability function.

For the IIC process the first column as well as the last row of $A - \mathbb { 1 } b ^ { T }$ van-ish. Thus the degree of the numerator of the stability function is at most $s - 2$ by Formula (3.3). Again,Theorem 3.11 and Theorem 4.12 imply the statement.□

For a summary of these statements see Table 5.13.

Table 5.13. Fully implicit Runge-Kutta methods   

<table><tr><td>method</td><td>simplifying assumptions</td><td>order</td><td>stability function</td></tr><tr><td>Gauss Radau IA Radau IIA Lobatto IIIA Lobatto IIIB Lobatto IIIC</td><td>B(2s) C(s) D(s) B(2s-1) C(s-1) D(s） B(2s-1) C(s) D(s-1) B(2s-2) C(s) D(s-2) B(2s-2) C(s-2) D(s) B(2s-2) C(s-1) D(s-1)</td><td>2s 2s-1 2s-1 2s-2 2s-2 2s-2</td><td>(s,s)-Padé (s-1,s)-Padé (s-1,s)-Padé (s-1,s-1)-Padé (s-1,s-1)-Padé (s-2,s)-Padé</td></tr></table>

# The W -Transformation

We now attack the explicit construction of all Runge-Kutta methods covered by Theorem 5.1. The first observation is (Chipman 1971, Burrage 1978) that $C ( \eta )$ can be written as

$$
\left( \begin{array} { l l l l l } { a _ { 1 1 } } & { \dots } & { a _ { 1 s } } \\ { \vdots } & & { \vdots } \\ { \vdots } & & { \vdots } \\ { a _ { s 1 } } & { \dots } & { a _ { s s } } \end{array} \right) \left( \begin{array} { l l l l l } { 1 } & { c _ { 1 } } & { \dots } & { c _ { 1 } ^ { \eta - 1 } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta - 1 } } \end{array} \right) = \left( \begin{array} { l l l l l } { 1 } & { c _ { 1 } } & { \dots } & { c _ { 1 } ^ { \eta } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta } } \end{array} \right) \left( \begin{array} { l l l l l } { 0 } & { 0 } & { \dots } & { 0 } \\ { 1 } & { 0 } & { \dots } & { 0 } \\ { 0 } & { \frac { 1 } { 2 } } & { \dots } & { 0 } \\ { \vdots } & { \vdots } & & { \ddots } & { \vdots } \\ { 1 } & { c _ { s } } & { \dots } & { c _ { s } ^ { \eta } } \end{array} \right) .
$$

Hence, if $V$ is the Vandermonde matrix

$$
V = \left( \begin{array} { c c c c } { { 1 } } & { { c _ { 1 } } } & { { \dots } } & { { c _ { 1 } ^ { s - 1 } } } \\ { { } } & { { \vdots } } & { { } } & { { \vdots } } \\ { { 1 } } & { { c _ { s } } } & { { \dots } } & { { c _ { s } ^ { s - 1 } } } \end{array} \right) ,
$$

then the first $\eta$ (for $\eta \leq s - 1$ ) columns of $V ^ { - 1 } A V$ must have the special structure (with many zeros) of the rightmost matrix in (5.6). This $^ { 6 6 } V$ -transformation" already considerably simplifies the discussion of order and stability of methods governed by $C ( \eta )$ with $\eta$ close to $s$ (Burrage 1978). Thus, collocation methods $( \eta = s )$ are characterized by

$$
V ^ { - 1 } A V = \left( \begin{array} { c c c c c } { { 0 } } & { { } } & { { } } & { { } } & { { - \varrho _ { 0 } / s } } \\ { { 1 } } & { { 0 } } & { { } } & { { } } & { { - \varrho _ { 1 } / s } } \\ { { } } & { { 1 / 2 } } & { { 0 } } & { { } } & { { - \varrho _ { 2 } / s } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ddots } } & { { 0 } } & { { - \varrho _ { s - 2 } / s } } \\ { { } } & { { } } & { { } } & { { 1 / ( s - 1 ) } } & { { - \varrho _ { s - 1 } / s } } \end{array} \right)
$$

where the $\varrho$ 's are the coeficients of $\begin{array} { r } { M ( t ) = \prod _ { \ i = 1 } ^ { s } ( t - c _ { \ i } ) } \end{array}$ and appear when the $c _ { \iota } ^ { s }$ in (5.6) are replaced by lower powers. Whenever some of the columns of $V ^ { - 1 } A V$ are not as in (5.7), a nice idea of Ngrsett allows one to interpret the method as a perturbed collocation method (see Ngrsett & Wanner (1981) for more details).

However, the $V$ -transformation has some drawbacks: it does not allow a similar characterization of $D ( \zeta )$ ，and the discussions of $A -$ and $B$ -stability remain fairly complicated (see e.g. the above cited papers). It was then discovered (Hairer & Wanner 1981, 1982) that nicer results are obtained,if the Vandermonde matrix $V$ is replaced by a matrix $W$ whose elements are orthogonal polynomials evaluated at $c _ { \imath }$ . We therefore use the (non standard) notation

$$
P _ { k } ( x ) = { \frac { { \sqrt { 2 k + 1 } } } { k ! } } { \frac { d ^ { k } } { d x ^ { k } } } { \Big ( } x ^ { k } ( x - 1 ) ^ { k } { \Big ) } = { \sqrt { 2 k + 1 } } \sum _ { \jmath = 0 } ^ { k } ( - 1 ) ^ { \jmath + k } { \binom { k } { \jmath } } { \binom { j + k } { j } } x ^ { \jmath }
$$

for the shifted Legendre polynomials normalized so that

$$
\int _ { 0 } ^ { 1 } P _ { k } ^ { 2 } ( x ) d x = 1 .
$$

These polynomials satisfy the integration formulas

$$
\begin{array} { l l } { \displaystyle \int _ { 0 } ^ { x } P _ { 0 } ( t ) d t = \xi _ { 1 } P _ { 1 } ( x ) + \frac { 1 } { 2 } P _ { 0 } ( x ) } \\ { \displaystyle \int _ { 0 } ^ { x } P _ { k } ( t ) d t = \xi _ { k + 1 } P _ { k + 1 } ( x ) - \xi _ { k } P _ { k - 1 } ( x ) } & { \ k = 1 , 2 , . . . } \end{array}
$$

with

$$
\xi _ { k } = { \frac { 1 } { 2 \sqrt { 4 k ^ { 2 } - 1 } } }
$$

(Exercise 1). Instead of (5.7) we now have the following result.

Theorem 5.6. Let W be defined by

$$
w _ { \iota \jmath } = P _ { \jmath - 1 } ( c _ { \imath } ) , \qquad i = 1 , \ldots , s , \quad \jmath = 1 , \ldots , s ,
$$

and let $A$ be the coefficient matrix for the Gauss method of order $2 s$ . Then,

$$
W ^ { - 1 } A W = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { - \xi _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { \xi _ { 2 } } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { 0 } } & { { - \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { 0 } } \end{array} \right) = : X _ { G } .
$$

Proof. We first write $C ( \eta )$ in the form

$$
\sum _ { \ i = 1 } ^ { s } a _ { \ i \ i } p ( c _ { \ i } ) = \int _ { 0 } ^ { c _ { \ i } } p ( x ) d x \qquad { \mathrm { i f } } \quad \deg ( p ) \leq \eta - 1 ,
$$

which,by (5.10),is equivalent to

$$
\begin{array} { l } { \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } P _ { 0 } ( c _ { \jmath } ) = \xi _ { 1 } P _ { 1 } ( c _ { \imath } ) + \frac { 1 } { 2 } P _ { 0 } ( c _ { \imath } ) } \\ { \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } P _ { k } ( c _ { \jmath } ) = \xi _ { k + 1 } P _ { k + 1 } ( c _ { \imath } ) - \xi _ { k } P _ { k - 1 } ( c _ { \imath } ) \qquad k = 1 , \dots , \eta - 1 . } \end{array}
$$

For $\eta = s$ , inserting (5.12), and using matrix notation, this becomes

$$
\begin{array} { r l r } { \left( \begin{array} { c c c } { a _ { 1 1 } } & { \ldots } & { a _ { 1 s } } \\ { \vdots } & { \vdots } \\ { \vdots } & { \vdots } \\ { a _ { s 1 } } & { \ldots } & { a _ { s s } } \end{array} \right) \left( \begin{array} { c c c } { w _ { 1 1 } } & { \ldots } & { w _ { 1 s } } \\ { \vdots } & { \vdots } \\ { \vdots } & { \vdots } \\ { w _ { s 1 } } & { \ldots } & { w _ { s s } } \end{array} \right) = } & { { } } \\ { \left( \begin{array} { c c c } { w _ { 1 1 } } & { \ldots } & { w _ { 1 s } } & { P _ { s } ( c _ { 1 } ) } \\ { \vdots } & { \vdots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } \\ { w _ { s 1 } } & { \ldots } & { w _ { s s } } & { P _ { s } ( c _ { s } ) } \end{array} \right) \left( \begin{array} { c c c } { 1 / 2 } & { - \xi _ { 1 } } & { \ldots } & { } \\ { \xi _ { 1 } } & { 0 } & { - \xi _ { 2 } } \\ { \vdots } & { \xi _ { 2 } } & { \ddots } & { \vdots } \\ { \xi _ { s 1 } } & { \ddots } & { \xi _ { s - 1 } } & { 0 } \\ { w _ { s 1 } } & { \ldots } & { \xi _ { s } } \end{array} \right) . } \end{array}
$$

Since for the Gauss processes we have $P _ { s } ( c _ { 1 } ) = \ldots = P _ { s } ( c _ { s } ) = 0$ , the last column respectively row of the right hand matrices can be dropped and we obtain (5.13).

In what follows we shall study similar results for other implicit Runge-Kutta methods. We first formulate the following lemma, which is an immediate consequence of (5.15) and (5.16).

Lemma 5.7. Let A be the coefficient matrix of an implicit Runge-Kutta method and let W be a nonsingular matrix with

$$
w _ { \iota _ { 2 } } = P _ { \jmath - 1 } ( c _ { \iota } ) \qquad f o r \quad i = 1 , \ldots , s , \quad j = 1 , \ldots , \eta + 1 .
$$

Then $C ( \eta )$ (with $\eta \leq s - 1 )$ is equivalent to the fact that the first $\eta$ columns of $W ^ { - 1 } A W$ are equal to those of $X _ { G }$ in (5.13). □

The second type of simplifying assumption, $D ( \zeta )$ , is now written in the form

$$
\sum _ { \ i = 1 } ^ { s } b _ { i } p ( c _ { \ i } ) a _ { i \ i } = b _ { j } \int _ { c _ { \ j } } ^ { 1 } p ( x ) d x \qquad { \mathrm { i f } } \quad \deg ( p ) \leq \zeta - 1 .
$$

The integration formulas (5.10) together with orthogonality relations

$$
\int _ { 0 } ^ { 1 } P _ { 0 } ( x ) d x = 1 , \quad \int _ { 0 } ^ { 1 } P _ { k } ( x ) d x = \int _ { 0 } ^ { 1 } P _ { 0 } ( x ) P _ { k } ( x ) d x = 0 \quad { \mathrm { f o r } } \quad k = 1 , 2 , \dots .
$$

show that $D ( \zeta )$ (i.e.,(5.17)) is equivalent to

$$
\begin{array} { r l r } {  { \sum _ { i = 1 } ^ { s } P _ { 0 } ( c _ { _ 2 } ) b _ { \imath } a _ { \imath j } = \Big ( \frac { 1 } { 2 } P _ { 0 } ( c _ { j } ) - \xi _ { 1 } P _ { 1 } ( c _ { _ 2 } ) \Big ) b _ { j } } } \\ & { \overset { s } { \underset { i = 1 } { \sum } } P _ { k } ( c _ { _ 1 } ) b _ { \imath } a _ { \imath j } = \Big ( \xi _ { k } P _ { k - 1 } ( c _ { _ 2 } ) - \xi _ { k + 1 } P _ { k + 1 } ( c _ { j } ) \Big ) b _ { j } } & { \quad k = 1 , \ldots , \zeta - 1 . } \end{array}
$$

This can be stated as

Lemma 5.8. As in the preceding lemma, let W be a nonsingular matrix with

$$
w _ { \ i \ i } = P _ { \jmath - 1 } ( c _ { \ i } ) \qquad f o r ~ i = 1 , \dots , s , ~ j = 1 , \dots , \zeta + 1 ,
$$

and let $B = \mathrm { d i a g } ( b _ { 1 } , \dots , b _ { s } )$ with $b _ { i } \neq 0$ . Then $D ( \zeta )$ (with $\zeta \leq s - 1 )$ is equivalent to the condition that the first $\zeta$ rows of the matrix $( W ^ { T } B ) A ( W ^ { T } B ) ^ { - 1 }$ are equal to those of $X _ { G }$ in (5.13) $( i f B$ is singular, we still have (5.19) below).

Proof. Formulas (5.18), writen in matrix form, give

$$
\begin{array} { r } { W ^ { T } B A = \left( \begin{array} { c c c c c c c } { 1 / 2 } & { - \xi _ { 1 } } & & & & \\ { \xi _ { 1 } } & { 0 } & { . . } & & & \\ & { . . } & { . . } & { - \xi _ { \zeta - 1 } } & & \\ & & { \xi _ { \zeta - 1 } } & { 0 } & { - \xi _ { \zeta } } & \\ { * } & { * } & { . . } & { . . } & { . . } & { * } \\ { * } & { * } & { . . } & { . . } & { . . } & { * } \end{array} \right) W ^ { T } B . } \end{array}
$$

It is now a natural and interesting question, whether both transformation matrices of the foregoing lemmas can be made equal, i.e., whether

$$
\begin{array} { r } { W ^ { T } B = W ^ { - 1 } \qquad \mathrm { o r } \qquad W ^ { T } B W = I . } \end{array}
$$

A first result is:

Lemma 5.9. For any quadrature formula of order $\geq 2 s - 1$ the matrix

$$
\boldsymbol { W } = \left( P _ { \jmath - 1 } ( c _ { \imath } ) \right) _ { \imath , \jmath = 1 , \ . \ , s }
$$

satisfies (5.20).

Proof.If the quadrature formula is of sufficiently high order, the polynomials $P _ { k } ( x ) P _ { l } ( x )$ $( k + l \le 2 s - 2 )$ are integrated exactly,i.e.,

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } P _ { k } ( c _ { \ i } ) P _ { l } ( c _ { \ i } ) = \int _ { 0 } ^ { 1 } P _ { k } ( x ) P _ { l } ( x ) d x = \delta _ { k l } ;
$$

this, however, is simply $W ^ { T } B W = I .$

Unfortunately, Condition (5.20) is too restrictive for many methods. We therefore relax our requirements as follows:

Definition 5.10. Let $\eta$ ， $\zeta$ be given integers between O and $s - 1$ . We say that an $s \times s$ -matrix $W$ satisfies $T ( \eta , \zeta )$ for the quadrature formula $( b _ { \imath } , c _ { \imath } ) _ { i = 1 } ^ { s }$ if

$$
\left. \begin{array} { l l } { W \mathrm { i s ~ n o n s i n g u l a r } } \\ { w _ { \iota \jmath } = P _ { \jmath - 1 } ( c _ { \iota } ) } & { i = 1 , \ldots , s , \quad \displaystyle \ j = 1 , \ldots , \mathrm { m a x } ( \eta , \zeta ) + 1 } \\ { W ^ { T } B W = \binom { I } { 0 } } & { 0 } \\ { 0 } & { R } \end{array} \right\}
$$

where $I$ is the $\left( \zeta + 1 \right) \times \left( \zeta + 1 \right)$ identity matrix; $R$ is an arbitrary $\left( s - \zeta - 1 \right) \times$ $\left( s - \zeta - 1 \right)$ matrix.

The main result is given in the following theorem. Together with Theorem 5.1 it is very helpful for the construction of high order methods (see Examples 5.16 and 5.24, and Theorem 13.15).

Theorem 5.11. Let W satisfy $T ( \eta , \zeta )$ for the quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right) _ { \imath = 1 } ^ { s } .$ Then for a Runge-Kutta method based on $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right)$ we have, for the matrix $X =$ $W ^ { - 1 } A W$ ，

a) the first n columns of $X$ are those of $X _ { G } \quad \Longleftrightarrow \quad C ( \eta )$ ， b)the first $\zeta$ rows of $X$ are those of $X _ { G } \quad \Longleftrightarrow \quad D ( \zeta )$

Proof. The equivalence of (a) with $C ( \eta )$ follows from Lemma 5.7. For the proof of (b) we multiply (5.19) from the right by $W$ and obtain

$$
\boldsymbol { W } ^ { T } \boldsymbol { B } \boldsymbol { W } \cdot \boldsymbol { X } = \boldsymbol { \widetilde { X } } \cdot \boldsymbol { W } ^ { T } \boldsymbol { B } \boldsymbol { W }
$$

where $\widetilde { X }$ is the large matrix of (5.19). Because of Condition (c) of $T ( \eta , \zeta )$ the first $\zeta$ rows of $\widetilde { X }$ and $X$ must be the same (write them as block matrices). The statement now follows from Lemma 5.8. □

We have stilleft open the question of the existence of $W$ satisfying $T ( \eta , \zeta )$ · The following two lemmas and Theorem 5.14 give an answer.

Lemma 5.12. If the quadrature formula has distinct nodes $c _ { i }$ and all weights positive $\left( \boldsymbol { b } _ { \imath } > \boldsymbol { 0 } \right)$ and if it is of order $p$ with $p \geq 2 \eta + 1$ and $p \geq 2 \zeta + 1$ ， then the matrix

$$
W = \Big ( p _ { \jmath - 1 } ( c _ { \imath } ) \Big ) _ { \imath , \jmath = 1 , \ldots , s }
$$

possesses property $T ( \eta , \zeta )$ and satisfies (5.20). Here $p _ { j } ( x )$ is the polynomial of degree $j$ orthonormalized for the scalar product

$$
\langle p , r \rangle = \sum _ { \imath = 1 } ^ { s } b _ { \imath } p ( c _ { \imath } ) r ( c _ { \imath } ) .
$$

Proof. The positivity of the $b ^ { \prime } s$ makes (5.24) a scalar product on the space of polynomials of degree $\leq s - 1$ .Because of the order property (compare with (5.22))， the orthonormalized $p _ { \jmath } ( x )$ must coincide for $j \le \operatorname* { m a x } ( \eta , \zeta )$ with the Legendre polynomials $P _ { \jmath } ( x )$ . Orthonormality with respect to (5.24) means that $W ^ { T } B W = I$ . □

Lemma 5.13. If the quadrature formula has distinct nodes $c _ { \imath }$ and is of order $p \ge s + \zeta$ ,then $W$ defined by (5.21) has property $T ( \eta , \zeta )$ ·

Proof. Because of $p \ge s + \zeta$ , (5.22) holds for $k = 0 , \ldots , s - 1$ and $l = 0 , \ldots , \zeta$ This ensures (c) of Definition 5.10. □

Theorem 5.14. Let the quadrature formula be of order $p$ . Then there exists a transformation with property $T ( \eta , \zeta )$ if and only if

$$
p \geq \eta + \zeta + 1 \qquad a n d \qquad p \geq 2 \zeta + 1 ,
$$

and at least $\mathrm { m a x } ( \eta , \zeta ) + 1$ numbers among $c _ { 1 } , \ldots , c _ { s }$ are distinct.

Proof. Set $\nu = \operatorname* { m a x } ( \eta , \zeta )$ and denote the columns of the transformation $W$ by $w _ { 1 } , \dots , w _ { s }$ . In virtue of (b) of $T ( \eta , \zeta )$ we have

$$
\boldsymbol { w } _ { j } = \left( P _ { \jmath - 1 } ( c _ { 1 } ) , \ldots , P _ { j - 1 } ( c _ { s } ) \right) ^ { T } \qquad \mathrm { f o r } \quad j = 1 , \ldots , \nu + 1 .
$$

These $\nu + 1$ columns are linearlyindependentonlyifat least $\nu + 1$ among $c _ { 1 } , . . . ,$ $c _ { s }$ are distinct. Now condition (c) of $T ( \eta , \zeta )$ means that $w _ { 1 } , \dotsc , w _ { \zeta + 1 }$ are orthonormal to $w _ { 1 } , \ldots , w _ { s }$ for the bilinear form $u ^ { T } B v$ . In particular, the orthonormality of $w _ { 1 } , \ldots , w _ { \zeta + 1 }$ t0 $w _ { 1 } , \ldots , w _ { \nu + 1 }$ (compare with (5.22)) means that the quadrature formula is exact for all polynomials of degree $\nu + \zeta$ . Therefore, $p \geq$ $\nu + \zeta + 1$ (which is the same as (5.25)) is a necessary condition for $T ( \eta , \zeta )$

To show its sufficiency, we complete $w _ { 1 } , \dots , w _ { \nu + 1 }$ to a basis of $\mathbb { R } ^ { s }$ . The new basis vectors $\widehat { w } _ { \nu + 2 } , \ldots , \widehat { w } _ { s }$ are then projected into the orthogonal complement of $\operatorname { s p a n } \langle w _ { 1 } , \dotsc , w _ { \zeta + 1 } \rangle$ with respect to $u ^ { T } B v$ by a Gram-Schmidt type orthogonalization. This yields

$$
\boldsymbol { w } _ { \boldsymbol { \jmath } } = \widehat { \boldsymbol { w } } _ { \boldsymbol { \jmath } } - \sum _ { k = 1 } ^ { \zeta + 1 } ( \boldsymbol { w } _ { k } ^ { T } \boldsymbol { B } \widehat { \boldsymbol { w } } _ { \boldsymbol { \jmath } } ) \boldsymbol { w } _ { k } \qquad \mathrm { f o r } \ j = \nu + 2 , \dots , s .
$$

# Construction of Implicit Runge-Kutta Methods

For the construction of implicit Runge-Kutta methods satisfying $B ( p ) , C ( \eta )$ and $D ( \zeta )$ with the help of Theorem 5.11, we first have to choose a quadrature formula of order $p$ . The following lemma is the basic result for Gaussian integration.

Lemma 5.15. Let $c _ { 1 } , \ldots , c _ { s }$ be real and distinct and let $b _ { 1 } , \dots , b _ { s }$ be determined by condition $B ( s )$ (i.e.,the formula is “interpolatory"). Then this quadrature formula is of order $2 s - k$ if and only if the polynomial $M ( x ) = ( x - c _ { 1 } ) ( x -$ $c _ { 2 } ) \ldots ( x - c _ { s } )$ is orthogonal to all polynomials of degree $\leq s - k - 1$ , i.e., if and only if

$$
M ( x ) = C \Bigl ( P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \ldots + \alpha _ { k } P _ { s - k } ( x ) \Bigr ) .
$$

For a proof see Exercise 2.

We see from (5.26) that all quadrature formulas of order $2 s - k$ can be specified in terms of $k$ parameters $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { k }$

Next, if the integers $\eta$ and $\zeta$ satisfy $\eta + \zeta + 1 \leq 2 s - k$ and $2 \zeta + 1 \leq 2 s - k$ (cf. (5.25)), we can compute a matrix $W$ satisfying $T ( \eta , \zeta )$ from Theorem 5.14 (or one of Lemmas 5.12 and 5.13). Finally a matrix $X$ is chosen which satisfies (a) and (b) of Theorem 5.11. Then the Runge-Kutta method with coefficients $A = W X W ^ { - 1 }$ is of order at least $\operatorname* { m i n } ( \eta + \zeta + 1 , 2 \eta + 2 )$ by Theorem 5.1.

Example 5.16. We search for all implicit Runge-Kutta methods satisfying $B ( 2 s -$ 2), $C ( s - 1 )$ and $D ( s - 2 )$ , i.e.， methods which are of order at least $2 s - 2$ by Theorem 5.1. As in (5.26), we put

$$
M ( x ) = C \left( P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x ) \right) .
$$

If $\alpha _ { 2 }$ satisfies

$$
\alpha _ { 2 } < \frac { s - 1 } { s } \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } } ,
$$

then the roots of $M$ are real and distinct (see Exercise 7). The matrix $W$ given in (5.21) has Property $T ( s - 1 , s - 2 )$ by Lemma 5.13. Finally we put

$$
X = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { \cdot } } & { { } } & { { } } & { { } } \\ { { } } & { { \cdot } } & { { \cdot } } & { { \cdot } } & { { - \xi _ { s - 2 } } } & { { } } \\ { { } } & { { } } & { { \xi _ { s - 2 } } } & { { 0 } } & { { \beta _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \xi _ { s - 1 } } } & { { \beta _ { s } } } \end{array} \right)
$$

(see Theorem 5.11), and obtain with $A = W X W ^ { - 1 }$ a family of implicit Runge-Kutta methods of order 2s - 2 with the four parameters α1,α2,βg, βg-1\*

All methods of Table 5.13 (with the exception of Lobatto IIIB) must be special cases. The corresponding parameter values are indicated in Table 5.14 (for their computation see Exercise 3). If we put $\alpha _ { \mathbf { 1 } } = 0$ and $\alpha _ { 2 } = - \sqrt { 2 s + 1 } / \sqrt { 2 s - 3 }$ (Lobato quadrature), we obtain the two-parameter family of Chipman (1976).

Table 5.14. Special cases of method (5.27,5.28)   

<table><tr><td rowspan=1 colspan=1>Method</td><td rowspan=1 colspan=1>α1</td><td rowspan=1 colspan=1>α2</td><td rowspan=1 colspan=1>β</td><td rowspan=1 colspan=1>β-1</td></tr><tr><td rowspan=1 colspan=1>GaussRadau IARadau IIALobatto IIIALobatto IIIC</td><td rowspan=1 colspan=1>0√2s+1/√2s-1√2s+1/√2s-100</td><td rowspan=1 colspan=1>000√2s+1/√2s-3</td><td rowspan=1 colspan=1>01/(4s-2)1/(4s-2)0</td><td></td></tr></table>

# Stability Function

We try to express the stability function of an implicit Runge-Kutta method in terms of the transformed Runge-Kutta matrix $X = W ^ { - 1 } A W$ . From (b) and (c) of Property $T ( \eta , \zeta )$ it follows that

$$
\boldsymbol { W } \boldsymbol { e } _ { 1 } = \mathbb { 1 } , \qquad \boldsymbol { W } ^ { T } \boldsymbol { B } \mathbb { 1 } = \boldsymbol { e } _ { 1 } , \qquad \boldsymbol { e } _ { 1 } = ( 1 , 0 , \dots , 0 ) ^ { T } .
$$

Hence Formulas (3.2) and (3.3)become

$$
R ( z ) = 1 + z e _ { 1 } ^ { T } ( I - z X ) ^ { - 1 } e _ { 1 } ,
$$

$$
R ( z ) = \frac { \operatorname* { d e t } ( I - z X + z e _ { 1 } e _ { 1 } ^ { T } ) } { \operatorname* { d e t } ( I - z X ) } .
$$

The stability function depends only on $X$ and not on the underlying quadrature formula. Hence,the stability function of the method of Example 5.16 depends on $\beta _ { s }$ and $\beta _ { s - 1 }$ only.Formula (5.31) becomes more symmetric (Hairer & Turke 1984) if we introduce the arithmetic mean of the matrices $X$ and $X - e _ { 1 } e _ { 1 } ^ { T }$ and define

$$
\boldsymbol { Y } = \boldsymbol { X } - \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ,
$$

which is just the matrix $X$ without the $1 / 2$ in the $( 1 , 1 )$ -position.

Proposition 5.17. For a Runge-Kutta method (3.1) let $W$ satisfy $T ( \eta , \zeta )$ for some $\eta$ ， $\zeta \geq 0$ , and let $Y$ be given by(5.32) where $X = W ^ { - 1 } A W$ . The stability function then satisfies

$$
R ( z ) = { \frac { 1 + { \frac { 1 } { 2 } } \Psi ( z ) } { 1 - { \frac { 1 } { 2 } } \Psi ( z ) } }
$$

with

$$
\Psi ( z ) = z e _ { 1 } ^ { T } ( I - z Y ) ^ { - 1 } e _ { 1 } .
$$

Proof. Applying the Runge-Kuta method to the test equation (2.9) yields

$$
g = \mathbb { 1 } y _ { 0 } + z A g , \qquad y _ { 1 } = y _ { 0 } + z b ^ { T } g .
$$

With $W ^ { - 1 } g = \widehat { g } = ( \widehat { g } _ { 1 } , \dots , \widehat { g } _ { s } ) ^ { T }$ this becomes

$$
( I - z Y ) \widehat { g } = e _ { 1 } \bigl ( y _ { 0 } + \frac { z } { 2 } \widehat { g } _ { 1 } \bigr ) , \qquad y _ { 1 } = y _ { 0 } + z \widehat { g } _ { 1 } ,
$$

where we have used (5.29). Computing $\widehat { g } _ { 1 }$ from the first equation of (5.35）) and inserting this into the second one gives the result. □

If the Runge-Kutta method satisfies $B ( 2 \nu + 1 ) , C ( \nu )$ and $D ( \nu )$ for some integer $\nu$ ,then $Y$ is given by (see Theorem 5.11)

$$
Y = \left( \begin{array} { c c c c c } { { 0 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { \cdot _ { \cdot } } } & { { \cdot _ { \cdot } } } & { { } } & { { } } \\ { { } } & { { \cdot _ { \cdot } } } & { { 0 } } & { { - \xi _ { \nu } } } \\ { { } } & { { } } & { { } } & { { \xi _ { \nu } } } & { { \boxed { Y _ { \nu } } } } \end{array} \right) .
$$

In this case the computation of (5.34) for the $\left( s , s \right)$ -matrix $Y$ can be reduced to that of the smaller $\bigl ( s - \nu , s - \nu \bigr )$ -matrix $Y _ { \nu }$ as follows:

Theorem 5.18. If $Y$ is given by (5.36), the function $\Psi ( z )$ of(5.34) has the continued fraction representation

$$
\Psi ( z ) = { \frac { z \Big | } { | 1 } } + { \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } \Big | } { | \ 1 \ } } + \ldots + { \frac { \xi _ { \nu - 1 } ^ { 2 } z ^ { 2 } \Big | } { | \ 1 \ } } + \xi _ { \nu } ^ { 2 } z \Psi _ { \nu } ( z )
$$

where $\Psi _ { \nu } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \nu } ) ^ { - 1 } e _ { 1 } .$

Proof. Let $Y _ { \jmath }$ (for $0 \leq j \leq \nu + 1 ,$ ）denote the $\left( s - j , s - j \right)$ principal minors of $Y$ , where the first $j$ rows and columns are suppressed. Expanding the determinant of $I - z Y _ { \jmath - 1 }$ with respect to the first row (and then the first column) gives for $j = 1 , \dots , \nu$

$$
\operatorname* { d e t } ( I - z Y _ { \jmath - 1 } ) = \operatorname* { d e t } ( I - z Y _ { \jmath } ) + \xi _ { \jmath } ^ { 2 } z ^ { 2 } \operatorname* { d e t } ( I - z Y _ { \jmath + 1 } ) .
$$

By Cramer's rule, the functions $\Psi _ { \jmath } ( z )$ can also be written as

$$
\Psi _ { j } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \jmath } ) ^ { - 1 } e _ { 1 } = z \frac { \operatorname * { d e t } ( I - z Y _ { \jmath + 1 } ) } { \operatorname * { d e t } ( I - z Y _ { \jmath } ) } .
$$

Dividing (5.38) by $\operatorname* { d e t } ( I - z Y _ { \jmath } )$ yields

$$
\Psi _ { \jmath - 1 } ( z ) = \frac { z } { 1 + \xi _ { \jmath } ^ { 2 } z \Psi _ { \jmath } ( z ) } .
$$

A repeated use of (5.40) gives (5.37) since $\Psi ( z ) = \Psi _ { 0 } ( z )$

We are thus naturally led to continued fraction expansions, a technique which was historically the earliest one.Birkhoff & Varga(1965) used it in their proof of the $A$ -stability of the diagonal Padé approximations. Later, Ehle (1969,1973) tried to extend “Varga's proof" to verify the $A$ -stability of the first and second subdiagonals of the Padé table ("This was unsuccessful because the resulting continued fraction expansions were not easily related to one another."). Therefore, Ehle (1973),Ehle & Picel (1975),proved $A$ -stability results for the first and second subdiagonal and some generalizations by a completely different method. The following study of $A$ -stability (see Butcher 1977,Hairer 1982, Hairer & Turke 1984) combines the above continued fraction expansion with properties of positive functions.

# Positive Functions

Many stability conditions for numerical methods can be expressed in the form that some associated function is positive.

(G. Dahlquist 1978)

$A$ -stability ofan implicit Runge-Kutta method is defined bythe property

$$
| R ( z ) | < 1 \qquad \mathrm { f o r } \quad \mathrm { R e } z < 0 .
$$

Since the transformation $( 1 + \zeta ) / ( 1 - \zeta )$ occurring in (5.33） maps the negative half-plane onto the open unit disc, (5.41) is equivalent to

$$
\operatorname { R e } \Psi ( z ) < 0 \qquad \operatorname { f o r } \quad \operatorname { R e } z < 0 .
$$

This condition means that $- \Psi ( - z )$ is a positive function; for rational functions the concept of positivity can be defined as follows:

Definition 5.19.A rational function $f ( z )$ is called positive if

$$
\operatorname { R e } f ( z ) > 0 \qquad { \mathrm { f o r } } \quad \operatorname { R e } z > 0 .
$$

A nice survey on the relevance of positive functions to numerical analysis is given by Dahlquist (1978). The following lemmas collect some properties of positive functions.

Lemma 5.20. Let $f ( z )$ and $g ( z )$ be positive functions. Then we have

a） $\alpha f ( z ) + \beta g ( z )$ is positive, if $\alpha > 0$ and $\beta \geq 0$ ；   
$b _ { . }$ ） $1 / f ( z )$ is positive;   
c） $f ( g ( z ) )$ is positive.

Observe that the poles of a positive function cannot lie in the positive half-plane, but poles on the imaginary axis are possible, e.g., the function $1 / z$ is positive.

Lemma 5.21. Suppose that

$$
f ( z ) = \frac { c } { z } + g ( z ) w i t h g ( z ) = { \cal O } ( 1 ) \mathrm { f o r } z  0 ,
$$

and $g ( z ) \not \equiv 0$ . Then $f ( z )$ is positive if and only if $c \geq 0$ and $g ( z )$ is positive.

Proof. The “if-part" follows from Lemma 5.20. Suppose now that $f ( z )$ is positive. The constant $c$ has to be non-negative, since for small positive values of $z$ we have R $\mathrm { ~ e ~ } f ( z ) > 0$ . On the imaginary axis we have (apart from poles) $\operatorname { R e } g ( i y ) =$ $\\\\\\\\\\\\mathrm  { t e } f ( i y ) \geq 0$ or more precisely

$$
\operatorname* { l i m } _ { z \to i y , \mathrm { \tiny ~ R e } } z _ { > 0 } \mathrm { R e } g ( z ) \geq 0 \qquad \mathrm { f o r } \quad y \in \mathbb { R } .
$$

The maximum principle for harmonic functions then implies that either $g ( z ) \equiv 0$ or $g ( z )$ is positive. □

A consequence of this lemma is the following characterization of $A$ -stability.

Theorem 5.22. Consider a Runge-Kutta method whose stability function is given by (5.33) with $Y$ as in (5.36). It is $A$ -stable if and only if

$$
\operatorname { R e } \Psi _ { \nu } ( z ) < 0 \qquad f o r \quad \operatorname { R e } z < 0
$$

where $\Psi _ { \nu } ( z ) = z e _ { 1 } ^ { T } ( I - z Y _ { \nu } ) ^ { - 1 } e _ { 1 } ~ a s ~ i n \left( 5 . 3 7 \right.$ ）.

Proof. We consider the submatrices $Y _ { j }$ of $Y$ and the functions $\Psi _ { j } ( z )$ of (5.39). As we prefer to work with positive functions we put

$$
\chi _ { \ j } ( z ) = - \Psi _ { \ j } ( - z ) = z e _ { 1 } ^ { T } ( \MakeUppercase { \romannumeral 1 } + z Y _ { \nu } ) ^ { - 1 } e _ { 1 } .
$$

By (5.42), $A$ -stability is equivalent to the positivity of $\chi _ { 0 } ( z )$ and condition (5.43) means that $\chi _ { \nu } ( z )$ is a positive function. Relation (5.40) becomes

$$
\big ( \chi _ { j - 1 } ( z ) \big ) ^ { - 1 } = \frac { 1 } { z } + \xi _ { j } ^ { 2 } \chi _ { j } ( z ) .
$$

Since all $\chi _ { \ j } ( z )$ are bounded near the origin and do not vanish identically (see (5.44)), it follows from Lemma 5.21 that $\chi _ { \jmath } ( z )$ is a positive function iff $\chi _ { \ j - 1 } ( z )$ is positive. This proves the theorem. □

Example 5.23. For the Runge-Kuta method of Example 5.16 with $X$ given by (5.28) we have

$$
\Psi _ { s - 2 } ( z ) = \frac { z ( 1 - \beta _ { s } z ) } { 1 - \beta _ { s } z - \xi _ { s - 1 } \beta _ { s - 1 } z ^ { 2 } } .
$$

Since

$$
\Big ( \Psi _ { s - 2 } ( z ) \Big ) ^ { - 1 } = \frac { 1 } { z } - \xi _ { s - 1 } \beta _ { s - 1 } \frac { z } { 1 - \beta _ { s } z }
$$

it follows from Lemma 5.21 and Theorem 5.22 that the method is $A$ -stable iff

$$
\beta _ { s - 1 } = 0 ~ \mathrm { o r } ~ ( \beta _ { s - 1 } < 0 ~ \mathrm { a n d } ~ \beta _ { s } \geq 0 ) .
$$

Comparing this result with Tables 5.14 and 5.13 leads to a second proof for the $A$ -stability of the diagonal and the first two subdiagonal Padé approximations for $e ^ { z }$ (see Theorem 4.12).

Example 5.24 (Construction of all $A$ -stable Runge-Kutta methods satisfying $B ( 2 s - 4 )$ ， $C ( s - 2 )$ and $D ( s - 3 ) .$ ). We take a quadrature formula of order $2 s - 4$ and construct, by Theorem 5.14, a matrix $W$ satisfying Property $T ( s - 2 , s - 3 )$ The Runge-Kutta matrix $A$ is then of the form

$$
A = W ( Y + \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ) W ^ { - 1 }
$$

with $Y$ given by (5.36), $\nu = s - 3$ and

$$
Y _ { s - 3 } = \left( \begin{array} { c c c } { { 0 } } & { { \gamma _ { s - 2 } } } & { { \beta _ { s - 2 } } } \\ { { \xi _ { s - 2 } } } & { { \gamma _ { s - 1 } } } & { { \beta _ { s - 1 } } } \\ { { 0 } } & { { \gamma _ { s } } } & { { \beta _ { s } } } \end{array} \right) .
$$

For the study of $A$ -stability we have to compute $\Psi _ { s - 3 } ( z )$ from (5.39). Expanding $\operatorname* { d e t } ( I - z Y _ { s - 3 } )$ with respect to its first column we obtain

$$
\displaystyle \left( \Psi _ { s - 3 } ( z ) \right) ^ { - 1 } = \frac { 1 } { z } + \frac { z \xi _ { s - 2 } ( g _ { 0 } - g _ { 1 } z ) } { 1 - f _ { 1 } z + f _ { 2 } z ^ { 2 } }
$$

where

$$
\begin{array} { r l } & { f _ { 1 } = \beta _ { s } + \gamma _ { s - 1 } , \qquad f _ { 2 } = \beta _ { s } \gamma _ { s - 1 } - \beta _ { s - 1 } \gamma _ { s } , } \\ & { g _ { 0 } = - \gamma _ { s - 2 } , \qquad g _ { 1 } = - \beta _ { s } \gamma _ { s - 2 } + \beta _ { s - 2 } \gamma _ { s } . } \end{array}
$$

By Lemma 5.21 and Theorem 5.22 we have $A$ -stability iff either $g _ { 0 } = g _ { 1 } = 0$ or

$$
\frac { z ( g _ { 0 } + g _ { 1 } z ) } { 1 + f _ { 1 } z + f _ { 2 } z ^ { 2 } }
$$

is a positive function, which is equivalent to (see Exercise 4b)

$$
g _ { 0 } > 0 , \quad g _ { 1 } \geq 0 , \quad f _ { 2 } \geq 0 , \quad g _ { 0 } f _ { 1 } - g _ { 1 } \geq 0 .
$$

A similar characterization of $A$ -stable Runge-Kutta methods of order $2 s - 4$ is given in Wanner (1980).

# Exercises

1. Verify the integration formulas (5.10) for the shifted Legendre polynomials.

Hint. By orthogonality $\int _ { 0 } ^ { x } P _ { k } ( t ) d t$ must be a linear combination of $P _ { k + 1 } , P _ { k }$ and $P _ { k - 1 }$ only. The coefficient of $P _ { k }$ vanishes by symmetry. For the rest just look at the coefficients of $x ^ { k + 1 }$ and $x ^ { k - 1 }$

2. Give a proof of Lemma 5.15.

Hint (Jacobi 1826). If $f ( x )$ is a polynomial of degree $2 s - k - 1$ ,and $r ( x )$ the interpolation polynomial of degree $s - 1$ , then $\begin{array} { r } { f ( x ) = q ( x ) M ( x ) + r ( x ) } \end{array}$ ， where deg $q ( x ) \leq s - k - 1$

3.Let $R ( z )$ be the stability function of the Runge-Kutta method of Example 5.16.

a) The degree of its denominator is $\leq s - 1$ iff $\beta _ { s } = \beta _ { s - 1 } \xi _ { s - 1 } 2 ( 2 s - 3 )$

Hint. Use Formula (5.31) and the fact that $\operatorname* { d e t } ( I - z X _ { G } )$ is the denominator of the diagonal Padé approximation.

b) The degree of the numerator of $R ( z )$ is $\leq s - 1$ iff

$$
\beta _ { s } = - \beta _ { s - 1 } \xi _ { s - 1 } 2 ( 2 s - 3 ) .
$$

c) The degree of the numerator of $R ( z )$ is $\leq s - 2$ iff in addition to (5.49) it holds $\beta _ { s } = 1 / ( 2 s - 2 )$

d) Verify the entries of Table 5.14.

4．a) The function

$$
s ( z ) = \frac { \alpha + \beta z } { \gamma + \delta z }
$$

with $\gamma > 0$ satisfies $\operatorname { R e } s ( z ) \geq 0$ for $\mathrm { R e } z > 0$ iff $\alpha \ge 0 , \beta \ge 0$ and $\delta \ge 0$ b) Use the identity (for $g _ { 0 } > 0$ ）

$$
{ \frac { 1 + f _ { 1 } z + f _ { 2 } z ^ { 2 } } { z ( g _ { 0 } + g _ { 1 } z ) } } - { \frac { 1 } { z g _ { 0 } } } = { \frac { ( f _ { 1 } - g _ { 1 } / g _ { 0 } ) + f _ { 2 } z } { g _ { 0 } + g _ { 1 } z } }
$$

to verify that the function given in (5.47) is positive iff(5.48) holds.

5. Suppose that

$$
f ( z ) = c z + g ( z ) \qquad { \mathrm { w i t h } } \qquad g ( z ) = { \mathcal { O } } ( 1 ) \qquad { \mathrm { f o r ~ } } z \to \infty
$$

and $g ( z ) \not \equiv 0$ . Using the transformation $z  1 / z$ in Lemma 5.21, show that $f ( z )$ is a positive function, if and only if $c \geq 0$ and $g ( z )$ is positive.

6. Give an alternative proof of the Routh criterion (Theorem 13.4 of Chapter I): All zeros of the real polynomial

$$
p ( z ) = a _ { 0 } z ^ { n } + a _ { 1 } z ^ { n - 1 } + \ldots + a _ { n } \quad ( a _ { 0 } > 0 )
$$

lie in the negative half-plane Re $z < 0$ if and only if

$$
c _ { \imath 0 } > 0 \qquad \mathrm { f o r } i = 0 , 1 , . . . , n .
$$

The $c _ { \imath \jmath }$ are the coefficients of the polynomials

$$
p _ { \ i } ( z ) = c _ { \ i 0 } z ^ { n - 1 } + c _ { \ i 1 } z ^ { n - \ i - 2 } + c _ { \ i 2 } z ^ { n - \ i - 4 } + . . .
$$

where

$$
\begin{array} { l l } { { p _ { 0 } ( z ) = a _ { 0 } z ^ { n } + a _ { 2 } z ^ { n - 2 } + \ldots , ~ } } & { { i . e . , ~ c _ { 0 \jmath } = a _ { 2 \jmath } } } \\ { { { } } } & { { { } p _ { 1 } ( z ) = a _ { 1 } z ^ { n - 1 } + a _ { 3 } z ^ { n - 3 } + \ldots , ~ } } & { { i . e . , ~ c _ { 1 \jmath } = a _ { 2 \jmath + 1 } . } } \end{array}
$$

and

$$
p _ { \iota + 1 } ( z ) = c _ { \iota 0 } p _ { \iota - 1 } ( z ) - c _ { \iota - 1 , 0 } z p _ { \iota } ( z ) , \qquad i = 1 , \ldots , n - 1 .
$$

Hint. By the maximum principle for harmonic functions the condition ${ } ^ { * } p ( z ) \neq$ 0 for $\mathrm { R e } z \ge 0 ^ { 3 }$ is equivalent to ‘ $^ { \prime } | p ( - z ) / p ( z ) | < 1$ for $\mathrm { R e } z > 0 ^ { , , }$ and the condition that $p _ { 0 } ( z )$ and $p _ { 1 } ( z )$ are irreducible. Using the transformation (5.33) this becomes equivalent to the positivity of $p _ { 0 } ( z ) / p _ { 1 } ( z )$ . Now divide (5.50) by $c _ { \imath - 1 , 0 } p _ { \imath } ( z )$ and use Exercise 5 recursively.

7. Show that

$$
\alpha _ { 2 } < \frac { s - 1 } { s } \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } }
$$

is a suficient condition for $M ( x ) = P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x )$ to have real and pairwise distinct roots.

Hint. (See “Lemma $1 8 ^ { \circ }$ of Ngrsett & Wanner 1981). Consider the set $D$ of all pairs $\left( \alpha _ { 1 } , \alpha _ { 2 } \right)$ for which the roots $c _ { \imath }$ of $M ( x )$ are real and distinct, and the corresponding interpolatory quadrature formula has positive $b _ { \imath }$ . Verify that $( 0 , 0 ) \in D$ ， and show that for $( \alpha _ { 1 } , \alpha _ { 2 } ) \in \partial D$ either one $b _ { i }$ becomes zero or two $c _ { \imath }$ coalesce but the quadrature formula remains of order $2 s - 2$ . Therefore it must be the Gaussian formula with $s - 1$ nodes of order $2 s - 2$ and we must have

$$
P _ { s } ( x ) + \alpha _ { 1 } P _ { s - 1 } ( x ) + \alpha _ { 2 } P _ { s - 2 } ( x ) = c ( x - \beta ) P _ { s - 1 } ( x ) .
$$

Now use the three-term recursion formula

$$
s \xi _ { s } P _ { s } ( x ) = ( x - 1 / 2 ) P _ { s - 1 } ( x ) - ( s - 1 ) \xi _ { s - 1 } P _ { s - 2 } ( x )
$$

(bramowitz&Stegnp82modfd)t $x P _ { s - 1 }$ on the rght of (5.52)Thenobaibyompingtheoeentsof $P _ { s } , P _ { s - 1 }$ and $P _ { s - 2 }$

$$
c = { \frac { 1 } { s \xi _ { s } } } \qquad \alpha _ { 1 } = { \frac { 1 } { s \xi _ { s } } } \Big ( { \frac { 1 } { 2 } } - \beta \Big ) , \qquad \alpha _ { 2 } = { \frac { s - 1 } { s } } { \frac { \sqrt { 2 s + 1 } } { \sqrt { 2 s - 3 } } } .
$$

If $\beta$ is one of the roots of $P _ { s - 1 }$ ,then (5.52) has adouble root and the estimate (5.51) for $\alpha _ { 2 }$ is optimal.

# IV.6Diagonally Implicit RK Methods

... they called their methods “diagonally implicit”,a term which is reserved here for the special case where all diagonal entries are equal ... (R.Alexander 1977)

We continue to quote from this nice paper: “To integrate a system of $\mathscr { n }$ differential equations, an implicit method with a full $s \times s$ matrix requires the solution of ns simultaneous implicit (in general nonlinear) equations in each time step(...） One way to circumvent this difficulty is to use a lower triangular matrix $( a _ { i j } )$ (i.e., a matrix with $a _ { \scriptscriptstyle \imath \jmath } = 0$ for $i < j )$ ; the equations may then be solved in $s$ successive stages with only an $\mathscr { n }$ -dimensional system to be solved at each stage". In accordance with many authors,and in disaccordance with others (see above),we call such a method diagonally implicit (DIRK).

"In solving the $n$ -dimensional systems by Newton-type iterations one solves linear systems at each stage with a coeficient matrix of the form $I - h a _ { i \imath } \partial f / \partial y$ If all $a _ { \ i i }$ are equal one may hope to use repeatedly the stored LU-factorization of a single such matrix". When we want to emphasize this additional property for a DIRK method, we shall call it a singly diagonally implicit (SDIRK) method.

It is a curious coincidence that in the early seventies at least four theses dedi-cated a large part of their research to DIRK and SDIRK methods, very often having in mind their usefulness for the treatment of partial differential equations (R. Alt 1971,M. Crouzeix 1975,A. Kurdi 1974, S.P. Ngrsett 1974). The classical paper on the subject is Alexander (1977).

# Order Conditions

The traditional problem of choosing the coefficients leads to a nonlinear algebraic jungle,to which civilization and order were brought in the pioneering work of J.C. Butcher, further refined in the Thesis of M. Crouzeix. (R.Alexander 1977)

We want to make the“jungle” still a little more civilized by the following idea: consider a SDIRK scheme

<table><tr><td rowspan="2">C1 C2</td><td colspan="4">Y</td></tr><tr><td>a21</td><td>Y</td><td></td><td></td></tr><tr><td>：</td><td></td><td></td><td></td><td></td></tr><tr><td>·</td><td>：</td><td></td><td></td><td></td></tr><tr><td>cs</td><td></td><td></td><td></td><td>Y</td></tr><tr><td></td><td>ag1</td><td>ag2</td><td></td><td></td></tr><tr><td></td><td>b</td><td>b2</td><td></td><td>8</td></tr></table>

with $s$ stages. The order conditions (see Vol. I, Sect.II.2) consist of sums such as

$$
\sum _ { \jmath , k , l } b _ { \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } .
$$

Because there are now more non-zero entries in the matrix $A$ than for explicit methods, this sum contains far more terms as it did before. The trick is to transfer all expressions containing a $\gamma$ to the right-hand side of (6.1). The resulting sum, denoted by $\sum ^ { \prime }$ , is then only built upon the subdiagonal entries as for explicit Runge-Kutta methods. The right-hand side becomes (for this example)

$$
{ \sum _ { j , k , l } } ^ { \prime } b _ { _ { j } } a _ { _ { j k } } a _ { k l } = \sum _ { j , k , l } b _ { _ { j } } ( a _ { _ { j k } } - \gamma \delta _ { _ { j k } } ) ( a _ { k l } - \gamma \delta _ { _ { k l } } )
$$

where $\delta _ { \ j \ k }$ denotes the Kronecker delta. Multiplying out we obtain

$$
\sum _ { \jmath , k , l } { ^ { \prime } b } _ { \jmath } a _ { \jmath k } a _ { k l } = \sum _ { \jmath , k , l } b _ { \jmath } a _ { \jmath k } a _ { k l } - \gamma \Big ( \sum _ { \jmath , l } b _ { j } a _ { j l } + \sum _ { \jmath , k } b _ { \jmath } a _ { \jmath k } \Big ) + \gamma ^ { 2 } \sum _ { j } b _ { \jmath } .
$$

For all sums on the right we insert order conditions (e.g. from Theorem 2.1 of Sect.II.2) and obtain

$$
\sum _ { \jmath , k , \ell } { } ^ { \prime } b _ { \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } - \gamma + \gamma ^ { 2 } .
$$

The general rule is that there appears an alternating polynomial in $\gamma$ whose coefficients are sums of $1 / \gamma ( u )$ ，where $u$ runs through all trees which are obtained by “short-circuiting” one, two, three,etc. vertices of $t$ (with exception of the root). The conditions for order 4 obtained in this way are summarized in Table 6.1. For $s \approx 2$ ， $p = 3$ and $s \simeq 3$ ， $p = 4$ these simplified conditions have only very few nonzero terms and the equations become especially simple to solve (see Exercise 1).

# Stiffly Accurate SDIRK Methods

Our main interest here lies in methods satisfying

$$
a _ { s _ { 3 } } = b _ { _ { _ { J } } } \quad \mathrm { f o r } \quad j = 1 , \ldots , s ,
$$

i.e., in methods for which the numerical solution $y _ { 1 }$ is identical to the last internal stage. A first consequence of this property is that $R ( \infty ) = 0$ (see Proposition 3.8). The order conditions for such methods can, instead of (6.1"), be simplified still further: consider again the example (6.1), which can now be written as

$$
\sum _ { \jmath , k , l } a _ { s \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } .
$$

Table 6.1. Order conditions for SDIRK methods   

<table><tr><td>t ·</td><td></td><td>e(t）|previous conditions</td><td>simplified conditions</td></tr><tr><td rowspan="5">广 m m /m k</td><td>∑bj=1 1 2 3</td><td>∑b;=1</td></tr><tr><td>∑bjak=1</td><td>∑&#x27;bajk=-γ</td></tr><tr><td>∑bajka=1</td><td>∑&#x27;bjajajl=-γ+²</td></tr><tr><td>∑bajkakl= 3</td><td>∑&#x27;byajkakl=-γ+²</td></tr><tr><td>∑bjakajlajm= ∑bajkakiam=</td><td>∑&#x27;bakalagm=1-Y+2²-3 ∑&#x27;bajkaklaym=-x+2γ²-3</td></tr></table>

This time we have, instead of (6.1')

$$
\begin{array} { r l } {  { \sum _ { j , k , l } a _ { s _ { j } } a _ { j k } a _ { k l } = \sum _ { j , k , l } ( a _ { s _ { j } } - \gamma \delta _ { s _ { j } } ) ( a _ { j k } - \gamma \delta _ { j k } ) ( a _ { k l } - \gamma \delta _ { k l } ) } } \\ & { = \sum _ { j , k , l } a _ { s j } a _ { j k } a _ { k l } - \gamma \Bigl ( \sum _ { j , k } a _ { s _ { j } } a _ { j k } + \sum _ { j , l } a _ { s j } a _ { j l } + \sum _ { k , l } a _ { s k } a _ { k l } \Bigr ) } \\ & { + \gamma ^ { 2 } \Bigl ( \sum _ { j } a _ { s j } + \sum _ { k } a _ { s k } + \sum _ { l } a _ { s l } \Bigr ) - \gamma ^ { 3 } \cdot 1 . } \end{array}
$$

Again inserting known order conditions, we now obtain

$$
{ \sum _ { \jmath , k , l } } ^ { \prime } a _ { s \jmath } a _ { \jmath k } a _ { k l } = \frac { 1 } { 6 } - \frac { 3 } { 2 } \gamma + 3 \gamma ^ { 2 } - \gamma ^ { 3 } .
$$

The general rule is similar to the one above: the difference is that $a l l$ vertices (including the root) are now available for being short-circuited. Another example, for the tree $t _ { 4 2 }$ , is sketched in Fig.6.1 and leads to the following right-hand side:

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 8 } - \gamma \Big ( \frac { 1 } { 3 } + \frac { 1 } { 3 } + 1 \cdot \frac { 1 } { 2 } + \frac { 1 } { 6 } \Big ) + \gamma ^ { 2 } \Big ( \frac { 1 } { 2 } + 1 \cdot 1 + 1 \cdot 1 + \frac { 1 } { 2 } + \frac { 1 } { 2 } + \frac { 1 } { 2 } \Big ) } \\ { \displaystyle - \gamma ^ { 3 } ( 1 + 1 + 1 + 1 ) + \gamma ^ { 4 } = \frac { 1 } { 8 } - \frac { 4 } { 3 } \gamma + 4 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } . } \end{array}
$$

The order conditions obtained in this manner are displayed in Table 6.2 for all trees of order $\leq 4$ . The expressions $\sum ^ { \prime }$ are written explicitly for the SDIRK method

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/29783c2197496d29ab17e9eab06b5cfa1d17bcfcc1a88391bfe2de1ed8bbb3db.jpg)  
Fig. 6.1. Short-circuiting tree $\displaystyle t _ { 4 2 }$

(6.3)with $s \approx 5$ satisfying condition (6.2)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/e1597db1bfe94a070ca257cf1f442e3018edb8ee51a120b4e7ed4f7f83367bba.jpg)

Observe that they become very similar to those of Formulas (1.11) in Sect. II.1.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/1f7a44ca1ab69124eaad0fc093d00c94d6f1fbd309467a00085515247276922a.jpg)

$$
\begin{array} { r l } & { \sum ^ { \prime } a _ { 3 j } - b _ { 1 } + b _ { 2 } + b _ { 3 } + b _ { 4 } = p _ { 1 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 1 } - b _ { 2 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } + b _ { 3 } c _ { g _ { 4 } ^ { \prime } } ^ { \prime } = p _ { 2 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 2 } + b _ { 2 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } + b _ { 4 } c _ { g _ { 4 } ^ { \prime } } ^ { \prime 2 } = p _ { 3 } } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } c _ { g _ { 1 } } a _ { g _ { 1 } } - b _ { 3 } a _ { g _ { 1 } } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + b _ { 4 } ( a _ { 4 } c _ { g _ { 2 } ^ { \prime } } ^ { 2 } + a _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } ) = p _ { 4 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } b _ { 1 } a _ { 1 } - b _ { 3 } a _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 2 } + b _ { 4 } ( a _ { 4 } c _ { g _ { 1 } ^ { \prime } } ^ { 2 } + a _ { 3 } c _ { g _ { 3 } ^ { \prime } } ^ { \prime } ) = p _ { 4 } , } \\ & { \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } a _ { 1 ^ { \prime } } a _ { 1 ^ { \prime } m } - b _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 3 } a _ { 1 } - b _ { 4 } c _ { g _ { 1 } ^ { \prime } } ^ { 4 } a _ { 1 ^ { \prime } } = p _ { 5 } } \\ &  \sum ^ { \prime } a _ { g _ { 1 } } a _ { g _ { 1 } } a _ { 1 ^ { \prime } } a _ { 1 m } - b _ { 3 } c _ { g _ { 1 } ^ { \prime } } ^ { 4 } a _ { 3 } c _  \end{array}
$$

$$
\begin{array} { l } { p _ { 5 } = \displaystyle \frac { 1 } { 4 } - 2 \gamma + \frac { 9 } { 2 } \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 6 } = \displaystyle \frac { 1 } { 8 } - \frac { 4 } { 3 } \gamma + 4 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 7 } = \displaystyle \frac { 1 } { 1 2 } - \gamma + \frac { 7 } { 2 } \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \\ { p _ { 8 } = \displaystyle \frac { 1 } { 2 4 } - \frac { 2 } { 3 } \gamma + 3 \gamma ^ { 2 } - 4 \gamma ^ { 3 } + \gamma ^ { 4 } } \end{array}
$$

Solution of Equations (6.4). By clever elimination from equations (6.4;4） and (6.4;6) as well as (6.4;4) and (6.4;7) we obtain

$$
\begin{array} { r l } & { b _ { 3 } a _ { 3 2 } c _ { 2 } ^ { \prime } \big ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } \big ) = c _ { 4 } ^ { \prime } p _ { 4 } - p _ { 6 } } \\ & { b _ { 4 } c _ { 3 } ^ { \prime } a _ { 4 3 } \big ( c _ { 2 } ^ { \prime } - c _ { 3 } ^ { \prime } \big ) = c _ { 2 } ^ { \prime } p _ { 4 } - p _ { 7 } . } \end{array}
$$

Multiplying these two equations and using (6.4;8) gives

$$
p _ { 8 } b _ { 3 } ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } ) ( c _ { 2 } ^ { \prime } - c _ { 3 } ^ { \prime } ) c _ { 3 } ^ { \prime } = ( c _ { 4 } ^ { \prime } p _ { 4 } - p _ { 6 } ) ( c _ { 2 } ^ { \prime } p _ { 4 } - p _ { 7 } ) .
$$

We now compute $b _ { 2 } , b _ { 3 } , b _ { 4 }$ from (6.4;2), (6.4;3), (6.4;5). This gives

$$
b _ { 3 } = \left( - p _ { 2 } c _ { 2 } ^ { \prime } c _ { 4 } ^ { \prime } + p _ { 3 } ( c _ { 4 } ^ { \prime } + c _ { 2 } ^ { \prime } ) - p _ { 5 } \right) / \left( c _ { 3 } ^ { \prime } ( c _ { 3 } ^ { \prime } - c _ { 2 } ^ { \prime } ) ( c _ { 4 } ^ { \prime } - c _ { 3 } ^ { \prime } ) \right)
$$

and $b _ { 2 }$ as well as $b _ { 4 }$ by cyclic permutation. Comparing the last two equations leads to

$$
c _ { 4 } ^ { \prime } = \frac { p _ { 8 } p _ { 3 } c _ { 2 } ^ { \prime } - p _ { 8 } p _ { 5 } - c _ { 2 } ^ { \prime } p _ { 6 } p _ { 4 } + p _ { 6 } p _ { 7 } } { p _ { 8 } p _ { 2 } c _ { 2 } ^ { \prime } - p _ { 8 } p _ { 3 } - c _ { 2 } ^ { \prime } p _ { 4 } p _ { 4 } + p _ { 4 } p _ { 7 } } .
$$

We now choose $\gamma , c _ { 2 } ^ { \prime }$ and $c _ { 3 } ^ { \prime }$ as free parameters. Then $c _ { 4 } ^ { \prime }$ is obtained from (6.7); $b _ { 2 } , b _ { 3 } , b _ { 4 }$ from (6.6), $b _ { 1 }$ from (6.4;1), $a _ { 3 2 }$ and $a _ { \scriptscriptstyle 4 3 }$ from (6.5), $a _ { 4 2 }$ from (6.4;4), and finally $a _ { 2 1 } , a _ { 3 1 } , a _ { 4 1 }$ from (6.3).

Embedded 3rd order formula: As proposed by Cash (1979),we can append to the above formula a third order expression

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \sum _ { \iota = 1 } ^ { 4 } \widehat { b } _ { i } k _ { \iota }
$$

(thus by omitting the term $b _ { 5 } = \gamma$ )for the sake of step size control. The coefficients $\widehat { b } _ { 1 } , \ldots , \widehat { b } _ { 4 }$ are simply obtained by solving the first 4 equations of Table 6.1 (linear system). Continuous embedded 3rd order formulas can be obtained in this way too (see Theorem 6.1 of Sect.II.6)

$$
y ( x _ { 0 } + \theta h ) \approx y _ { 0 } + h \sum _ { \imath = 1 } ^ { 4 } b _ { i } ( \theta ) k _ { \imath } .
$$

The coefficients $b _ { 1 } ( \theta ) , \dots , b _ { 4 } ( \theta )$ are obtained by solving the first 4 (simplified) conditions of Table 6.1, with the right-hand sides replaced by

$$
\theta , \quad \frac { \theta ^ { 2 } } { 2 } - \gamma \theta , \quad \frac { \theta ^ { 3 } } { 3 } - \gamma \theta ^ { 2 } + \gamma ^ { 2 } \theta , \quad \frac { \theta ^ { 3 } } { 6 } - \gamma \theta ^ { 2 } + \gamma ^ { 2 } \theta ,
$$

respectively. The continuous solution obtained in this way becomes $\widehat { y } _ { 1 }$ for $\theta =$ 1 instead of the $4$ -th order solution $y _ { 1 }$ . The global continuous solution would therefore be discontinuous. In order to avoid this discontinuity, we add $b _ { 5 } ( \theta )$ and include the fifth equation from Table 6.1 with right-hand side

$$
\frac { \theta ^ { 4 } } { 4 } - \gamma \theta ^ { 3 } + \frac { 3 \gamma ^ { 2 } \theta ^ { 2 } } { 2 } - \gamma ^ { 3 } \theta .
$$

# The Stability Function

By Formula (3.3), the stability function $R ( z )$ for a DIRK method is of the form

$$
R ( z ) = \frac { P ( z ) } { ( 1 - a _ { 1 1 } z ) ( 1 - a _ { 2 2 } z ) \dots ( 1 - a _ { s s } z ) } ,
$$

because the determinant of a triangular matrix is the product of its diagonal entries. The numerator $P ( z )$ is a polynomial of degree $s$ at most. If the method is of order $p \geq s$ ，this polynomial is uniquely determined by Formula (3.18). It is simply obtained from the first terms of the power series for $( 1 - a _ { 1 1 } z ) \dots ( 1 - a _ { s s } z ) \cdot e ^ { z }$

For SDIRK methods, with $a _ { 1 1 } = \dots = a _ { s s } = \gamma$ , we obtain (see also Formula (3.18) with $q _ { \jmath } = { \left( - \gamma \right) } ^ { j } { \binom { s } { j } }$ ）

$$
P ( z ) = ( - 1 ) ^ { s } \sum _ { \jmath = 0 } ^ { s } L _ { s } ^ { ( s - j ) } \Big ( { \frac { 1 } { \gamma } } \Big ) ( \gamma z ) ^ { \jmath }
$$

with error constant

$$
C = \frac { \gamma ^ { s } ( - 1 ) ^ { s + 1 } } { s + 1 } L _ { s + 1 } ^ { ( 1 ) } \biggl ( \frac { 1 } { \gamma } \biggr )
$$

where

$$
L _ { s } ( x ) = \sum _ { j = 0 } ^ { s } ( - 1 ) ^ { j } \binom { s } { j } \frac { x ^ { j } } { j ! }
$$

is the $s$ -degree Laguerre polynomial. $L _ { s } ^ { ( k ) } ( x )$ denotes its $k$ -th derivative. Since the function (6.9) is analytic in $\mathbb { C } ^ { - }$ for $\gamma > 0$ ， $A$ -stability is equivalent to

$$
E ( y ) = Q ( i y ) Q ( - i y ) - P ( i y ) P ( - i y ) \geq 0 \qquad { \mathrm { ~ f o r ~ a l l ~ } } y _ { \mathrm { i } }
$$

(see (3.8)). This is an even polynomial of degree $2 s$ (in general) and subdegree $2 j$ where $j = [ ( p + 2 ) / 2 ]$ (see Proposition 3.4). We therefore define the polynomial $F ( x )$ by

$$
F ( y ^ { 2 } ) = E ( y ) / y ^ { 2 j } \quad j = [ ( p + 2 ) / 2 ] .
$$

and check the condition $F ( x ) \geq 0$ for $x \ge 0$ using Sturm sequences. We display the results obtained (similar to Burrage 1978) in Table 6.3.

For completeness, we give the following explicit formulas for $E ( y )$

$$
{ \begin{array} { r l } { s = 1 ; p = 1 : } & { } \\ & { E = y ^ { 2 } ( 2 \gamma - 1 ) } \\ { s = 2 ; p = 2 : } \\ & { { \phantom { s p a c e } } E = y ^ { 4 } \left( - { \frac { 1 } { 4 } } + 2 \gamma - 5 \gamma ^ { 2 } + 4 \gamma ^ { 3 } \right) = y ^ { 4 } { \left( 2 \gamma - 1 \right) } ^ { 2 } \left( \gamma - { \frac { 1 } { 4 } } \right) } \\ { s = 3 ; p = 3 : } \\ & { { \phantom { s p a c e } } E = y ^ { 4 } \left( { \frac { 1 } { 1 2 } } - \gamma + 3 \gamma ^ { 2 } - 2 \gamma ^ { 3 } \right) + y ^ { 6 } \left( - { \frac { 1 } { 3 6 } } + { \frac { \gamma } { 2 } } - { \frac { 1 3 \gamma ^ { 2 } } { 4 } } + { \frac { 2 8 \gamma ^ { 3 } } { 3 } } - 1 2 \gamma ^ { 4 } + 6 \gamma ^ { 5 } \right) } \end{array} }
$$

Table 6.3. $A$ -stability of (6.9),order $p \geq s$   

<table><tr><td>S</td><td>A -stability</td><td>A -stability and p = s +1</td></tr><tr><td>1</td><td>1/2≤γ&lt;8</td><td>1/2</td></tr><tr><td>2</td><td>1/4≤γ&lt;8</td><td>(3+√3)/6</td></tr><tr><td>3</td><td>1/3≤γ ≤1.06857902</td><td>1.06857902</td></tr><tr><td>4</td><td>0.39433757 ≤ γ ≤ 1.28057976</td><td></td></tr><tr><td>5</td><td>{0.24650519≤γ≤0.36180340 0.42078251≤γ≤0.47326839</td><td>0.47326839</td></tr><tr><td>6</td><td>0.28406464 ≤ γ ≤ 0.54090688</td><td></td></tr><tr><td>7</td><td></td><td></td></tr><tr><td>8</td><td>0.21704974 ≤ γ ≤ 0.26471425</td><td></td></tr></table>

$$
\begin{array} { r l } & { 4 ; \ p = 4 : } \\ & { E = y ^ { 6 } \left( \frac { 1 } { 7 2 } - \frac { \chi } { 3 } + \frac { 1 7 \gamma ^ { 2 } } { 6 } - \frac { 3 2 \gamma ^ { 3 } } { 3 } + 1 7 \gamma ^ { 4 } - 8 \gamma ^ { 5 } \right) } \\ & { \quad + y ^ { 8 } \left( - \frac { 1 } { 5 7 6 } + \frac { \gamma } { 1 8 } - \frac { 2 5 \gamma ^ { 2 } } { 3 6 } + \frac { 1 3 \gamma ^ { 3 } } { 3 } - \frac { 1 7 3 \gamma ^ { 4 } } { 1 2 } + \frac { 7 6 \gamma ^ { 5 } } { 3 } - 2 2 \gamma ^ { 6 } + 8 \gamma ^ { 7 } \right) . } \end{array}
$$

$A$ -stability means here that all coefficients must be non-negative.A general formula is as follows.

Lemma 6.1. The $E$ -polynomial for (6.8) with $a _ { 1 1 } = \dots = a _ { s s } = \gamma$ and $p \geq s$ satisfies

$$
\begin{array} { l } { { \displaystyle { E ( y ) = \Big ( 1 - L _ { s } \Big ( \frac { 1 } { \gamma } \Big ) ^ { 2 } \Big ) ( \gamma y ) ^ { 2 s } } } } \\ { { \mathrm { - 2 } \sum _ { \jmath = \lbrack { ( p + 2 ) / 2 } \rbrack } ^ { s - 1 } ( - 1 ) ^ { s + j } ( \gamma y ) ^ { 2 j } \int _ { 0 } ^ { 1 / \gamma } L _ { s } ( x ) L _ { s } ^ { ( 2 s + 1 - 2 \jmath ) } ( x ) d x . } }  \end{array}
$$

Proof. Inserting Formula (6.9) into the definition of $E ( y )$

$$
\begin{array} { l } { { \displaystyle E ( y ) = ( 1 + \gamma ^ { 2 } y ^ { 2 } ) ^ { s } - P ( i y ) P ( - i y ) } } \\ { { \displaystyle \qquad = ( 1 + \gamma ^ { 2 } y ^ { 2 } ) ^ { s } - \sum _ { k } \sum _ { l } L _ { s } ^ { ( s - k ) } \left( \frac 1 \gamma \right) L _ { s } ^ { ( s - l ) } \left( \frac 1 \gamma \right) ( \gamma i y ) ^ { k + l } ( - 1 ) ^ { l } } } \end{array}
$$

and using integration by parts for the verification of

$$
2 \int _ { 0 } ^ { \alpha } { \cal L } _ { s } ( x ) { \cal L } _ { s } ^ { ( 2 s + 1 - 2 j ) } ( x ) d x = ( - 1 ) ^ { s } \sum _ { k + l = 2 \atop { } } ( - 1 ) ^ { l } { \cal L } _ { s } ^ { ( s - k ) } ( x ) { \cal L } _ { s } ^ { ( s - l ) } ( x ) \Big | _ { 0 } ^ { \alpha }
$$

one obtains the result, since

$$
\sum _ { k + l = 2 j } ( - 1 ) ^ { l } L _ { s } ^ { ( s - k ) } ( 0 ) L _ { s } ^ { ( s - l ) } ( 0 ) = ( - 1 ) ^ { j } { \binom { s } { j } } .
$$

# Multiple Real-Pole Approximations with $R ( \infty ) = \mathbf { 0 }$

For methods satisfying (6.2) we have $R ( \infty ) = 0$ . Therefore the highest coefficient of $P ( z )$ in (6.9) is zero. If the order of the method is known to be $p \geq s - 1$ ，the remaining coefficients of $P ( z )$ are still uniquely determined by $\gamma$ and we have

$$
P ( z ) = ( - 1 ) ^ { s } \sum _ { j = 0 } ^ { s - 1 } L _ { s } ^ { ( s - _ { j } ) } \Bigl ( \frac { 1 } { \gamma } \Bigr ) ( \gamma z ) ^ { j }
$$

with error constant

$$
C = ( - 1 ) ^ { s } L _ { s } \Bigl ( { \frac { 1 } { \gamma } } \Bigr ) \gamma ^ { s } .
$$

The first polynomials $E ( y )$ of (6.12) are now:

$$
\begin{array} { r l } & { s = 2 , \ p = 1 ; } \\ & { \qquad E = y ^ { 2 } ( - 1 + 4 \gamma - 2 \gamma ^ { 2 } ) + y ^ { 4 } \gamma ^ { 4 } } \\ & { s = 3 , \ p = 2 ; } \\ & { \qquad E = y ^ { 4 } \left( - \frac { 1 } { 4 } + 3 \gamma - 1 2 \gamma ^ { 2 } + 1 8 \gamma ^ { 3 } - 6 \gamma ^ { 4 } \right) + y ^ { 6 } \gamma ^ { 6 } } \\ & { s = 4 , \ p = 3 ; } \\ & { E = y ^ { 4 } \left( \frac { 1 } { 1 2 } - \frac { 4 \gamma } { 3 } + 6 \gamma ^ { 2 } - 8 \gamma ^ { 3 } + 2 \gamma ^ { 4 } \right) } \\ & { \qquad + y ^ { 6 } \left( - \frac { 1 } { 3 6 } + \frac { 2 \gamma } { 3 } - 6 \gamma ^ { 2 } + \frac { 7 6 \gamma ^ { 3 } } { 3 } - 5 2 \gamma ^ { 4 } + 4 8 \gamma ^ { 5 } - 1 2 \gamma ^ { 6 } \right) + y ^ { 8 } \gamma ^ { 8 } . } \end{array}
$$

The regions of $\gamma$ for $A$ -(and hence $L - )$ stability are displayed in Table 6.4.

Table 6.4. $I$ -stability of $R ( z )$ with $P$ from (6.14), order $p \geq s - 1$   

<table><tr><td>S</td><td>L -stability</td><td>L-stab. and p = s</td></tr><tr><td>2</td><td>(2-√2)/2≤γ≤(2+√2)/2</td><td>γ =(2±√2)/2</td></tr><tr><td>3</td><td>0.18042531 ≤ γ ≤ 2.18560010</td><td>Y = 0.43586652</td></tr><tr><td>4</td><td>0.22364780 ≤ γ ≤ 0.57281606</td><td>Y = 0.57281606</td></tr><tr><td>5</td><td>0.24799464 ≤ γ ≤ 0.67604239</td><td>Y= 0.27805384</td></tr><tr><td>6</td><td>0.18391465≤ γ ≤0.33414237</td><td>Y= 0.33414237</td></tr><tr><td>7</td><td>0.20408345 ≤ γ ≤ 0.37886489</td><td></td></tr><tr><td>8</td><td>0.15665860 ≤ γ ≤ 0.23437316</td><td>Y= 0.23437316</td></tr></table>

# Choice of Method

We now determine the free parameters for method (6.3） with $s \approx 5$ and order 4. For a good choice of $\gamma$ , we have displayed in Fig. 6.2 the error constant $C$ as well as the regions for $A \cdot$ and $A ( 0 )$ -stability.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/7c2fa09cf30bf2edc8c3ad36030fa0d4e13a6277a2655b66c38e9b78c911ad29.jpg)  
Fig. 6.2 Error constant and $A$ -stability domain for $s = 5 , p = 4$

This suggests that $\gamma$ between O.25 and O.29 is a good choice. The method is then $L$ -stable and the error constant is small. For various values of $\gamma$ in this range, we determined (by a nonlinear Gauss-Newton code) $c _ { 2 } ^ { \prime }$ and $c _ { 3 } ^ { \prime }$ in order to minimize the fifth-order error terms. It turned out that

$$
c _ { 2 } ^ { \prime } = 0 . 5 , \qquad c _ { 3 } ^ { \prime } = 0 . 3
$$

is close to optimal. With this we coded two different choices of $\gamma \colon \gamma = 4 / 1 5 =$ 0.2666..., which was numerically the better choice and $\gamma = 1 / 4$ , which gave, via Formulas (6.4), (6.5),(6.6) and (6.7),especially nice rational coefficients. These latter are displayed in Table 6.5. We have included a continuous solution to this method

$$
y ( x _ { 0 } + \theta h ) \approx y _ { 0 } + h \sum _ { \jmath = 1 } ^ { 5 } b _ { j } ( \theta ) k _ { \jmath } ,
$$

which is third order for $0 < \theta < 1$ and updates to the fourth order approximation $y _ { 1 }$ for $\theta \approx 1$

Table 6.5. $L$ -stable SDIRK method of order 4   

<table><tr><td></td><td></td><td>4 1 25</td><td></td><td></td></tr><tr><td></td><td>371 1360</td><td>137 2720</td><td>1 544</td><td>4</td></tr><tr><td>1</td><td></td><td>4</td><td>125</td><td>85 1-4</td></tr><tr><td></td><td></td><td></td><td>16</td><td>12</td></tr><tr><td>y1 二</td><td></td><td></td><td>125</td><td>85</td></tr><tr><td></td><td>25242524598</td><td></td><td>16</td><td>14 12</td></tr><tr><td>y 二</td><td></td><td></td><td>225</td><td>85 0</td></tr><tr><td></td><td></td><td></td><td>32 12</td><td></td></tr><tr><td>err 二</td><td>3</td><td>49148171627132</td><td>2 0</td><td>4</td></tr></table>

$$
\begin{array} { l } { { b _ { 1 } ( \theta ) = \displaystyle { \frac { 1 1 } { 3 } } \theta - \frac { 4 6 3 } { 7 2 } \theta ^ { 2 } + \frac { 2 1 7 } { 3 6 } \theta ^ { 3 } - \frac { 2 0 } { 9 } \theta ^ { 4 } } } \\ { { b _ { 2 } ( \theta ) = \displaystyle { \frac { 1 1 } { 2 } } \theta - \frac { 3 8 5 } { 1 6 } \theta ^ { 2 } + \frac { 6 6 1 } { 2 4 } \theta ^ { 3 } - 1 0 \theta ^ { 4 } } } \\ { { b _ { 3 } ( \theta ) = \displaystyle { - \frac { 1 2 5 } { 1 8 } } \theta + \frac { 2 0 1 2 5 } { 4 3 2 } \theta ^ { 2 } - \frac { 8 8 7 5 } { 2 1 6 } \theta ^ { 3 } + \frac { 2 5 0 } { 2 7 } \theta ^ { 4 } } } \\ { { b _ { 4 } ( \theta ) = \displaystyle { - \frac { 8 5 } { 4 } } \theta ^ { 2 } + \frac { 8 5 } { 6 } \theta ^ { 3 } } } \\ { { b _ { 5 } ( \theta ) = \displaystyle { - \frac { 1 1 } { 9 } } \theta + \frac { 5 5 7 } { 1 0 8 } \theta ^ { 2 } - \frac { 3 5 9 } { 5 4 } \theta ^ { 3 } + \frac { 8 0 } { 2 7 } \theta ^ { 4 } . } } \end{array}
$$

# Exercises

1.(Crouzeix & Raviart 1980). Compute the SDIRK methods (Table 6.1) for $s =$ 3, $p = 4$ . Obtain also (for $s = 2 , p = 3$ ） once again the method of Table 7.2, Sect. I1.7.

Result. The last order condition is in both cases just a polynomial in $\gamma$ . Among the different solutions, the following presents an $A$ -stable scheme:

$$
\begin{array} { l } { \gamma = \displaystyle \frac { 1 } { \sqrt { 3 } } \cos \left( \frac { \pi } { 1 8 } \right) + \frac { 1 } { 2 } } \\ { \delta = \displaystyle \frac { 1 } { 6 ( 2 \gamma - 1 ) ^ { 2 } } . } \end{array}
$$

2． Verify all details of Tables 6.1 and 6.2.

3. The four cases of $A$ -stable SDIRK methods of order $p = s + 1$ indicated in Table 6.3 (right) are the only ones existing. This fact has not yet been rigorously proved, because the “proof" given in Wanner, Hairer & Nprsett (1978) uses an asymptotic formula without error estimation. Do better.

4. Cooper & Sayfy (1979) have derived many DIRK (which they call “semiexplicit") methods of high order. Their main aim was to minimize the number of implicit stages and not to maximize stability. One of their methods is

<table><tr><td>6-√6 10</td><td colspan="4">6-√6 10</td></tr><tr><td>6+9√6</td><td>-6+5√6</td><td>6-√6</td><td></td><td></td></tr><tr><td>35</td><td>14 888+607√6</td><td>10 126-161√6</td><td>6-√6</td><td></td></tr><tr><td>1</td><td>2850</td><td>1425</td><td>10</td><td></td></tr><tr><td>4-6 10</td><td>3153-3082√6 14250</td><td>3213+1148√6 28500</td><td>-267+88√6 500</td><td>6-√6 10</td></tr><tr><td>4+√6</td><td>-32583+14638√6</td><td>-17199+364√6</td><td>1329-544√6</td><td>-96+131√6 6-√6</td></tr><tr><td>10</td><td>71250</td><td>142500</td><td>2500</td><td>625 10</td></tr><tr><td>1</td><td>： 0 市</td><td>0</td><td>小</td><td>16-√6 16+√6 0</td></tr></table>

Show that it is of order 5 and $A$ -stable, but not $L$ -stable.

5. It can be seen in Table 6.4 that for $s = 2 , 4 , 6$ ,and 8 the $L$ -stability superconvergence point coincides with the right end of the $A$ -stability interval. Explain this with the help of order star theory (Fig. 6.3.a).

Further, for $s \simeq 7$ ，a superconvergence point is given by $\gamma = 0 . 2 0 4 0 6 6 9 3$ ， which misses the $A$ -stability interval given there by less than $2 \cdot 1 0 ^ { - 5 }$ . Should the above argument also apply here and must there be a computation error somewhere? Study the corresponding order star to show that this is not the case (Fig. 6.3.b).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/35ab1256c9ed7df36e876e4266cd5919f0f773838703d57c284f8b3560021513.jpg)  
Fig. 6.3.a. Multiple pole order star $s = 8$ ，Y= 0.23437316

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/d7e02e84f33d2abbc059cc3c03d392d27627cf1268348f4a2f045ef158fb0b7b.jpg)  
Fig. 6.3.b. Multiple pole order star

When the functions $\varphi$ are non-linear, implicit equations can in general be solved only by iteration. This is a severe drawback, as it adds to the problem of stability,that of convergence of the iterative process.An alternative,which avoids this difficulty, is (H.H. Rosenbrock 1962/63)

... is discussed in this section. Among the methods which already give satisfactory results for stiff equations, Rosenbrock methods are the easiest to program. We shall describe their theory in this section, which will lead us to our first “stiff code. Rosenbrock methods belong to a large class of methods which try to avoid nonlinear systems and replace them by a sequence of linear systems. We therefore call these methods linearly implicit Runge-Kutta methods. In the literature such methods are often called “semi-implicit” (or was it “semi-explicit"?), or “generalized" or “modified” or “adaptive” or “additive" Runge-Kutta methods.

# Derivation of the Method

We start, say, with a diagonally implicit Runge-Kutta method

$$
\begin{array} { l l } { { \displaystyle k _ { \imath } = h f \biggl ( y _ { 0 } + \sum _ { j = 1 } ^ { \imath - 1 } a _ { \imath j } k _ { \jmath } + a _ { \imath \imath } k _ { \imath } \biggr ) \quad } } & { { \displaystyle i = 1 , \ldots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { s } b _ { \imath } k _ { \imath } } } & { { \displaystyle } } \end{array}
$$

applied to the autonomous differential equation

$$
y ^ { \prime } = f ( y ) .
$$

The main idea is to linearize Formula (7.1). This yields

$$
\begin{array} { l } { { \displaystyle k _ { \imath } = h f ( g _ { i } ) + h f ^ { \prime } ( g _ { \imath } ) a _ { i \imath } k _ { \imath } } } \\ { { \displaystyle g _ { i } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { i - 1 } a _ { \imath j } k _ { \jmath } , } } \end{array}
$$

and can be interpreted as the application of one Newton iteration to each stage in （7.1） with starting values $k _ { i } ^ { ( 0 ) } = 0$ . Instead of continuing the iterations until convergence, we consider (7.3) as a new class of methods and investigate anew its order and stability properties.

Important computational advantage is obtained by replacing the Jacobians $f ^ { \prime } ( g _ { \imath } )$ by $J = f ^ { \prime } ( y _ { 0 } )$ , so that the method requires its calculation only once (Calahan 1968). Many methods of this type and much numerical experience with them have been obtained by van der Houwen (1973), Cash (1976) and Ngrsett (1975).

We gain further freedom by introducing additional linear combinations of the terms $J k _ { \ j }$ into (7.3)(Ngrsett & Wolfbrandt 1979,Kaps & Rentrop 1979). We then arrive at the following class of methods:

Definition 7.1. An $s$ -stage Rosenbrock method is given by the formulas

$$
\begin{array} { r l } & { k _ { \iota } = h f \biggl ( y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { \iota - 1 } \alpha _ { \iota _ { j } } k _ { j } \biggr ) + h J \displaystyle \sum _ { \jmath = 1 } ^ { \iota } \gamma _ { \iota _ { j } } k _ { \jmath } , \qquad i = 1 , \dots , s } \\ & { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { \jmath } k _ { \jmath } } \end{array}
$$

where $\alpha _ { \iota _ { 2 } } , \gamma _ { \iota _ { 2 } } , b _ { \iota }$ are the determining coeficients and $J = f ^ { \prime } ( y _ { 0 } )$

Each stage of this method consists of a system of linear equations with unknowns $k _ { \imath }$ and with matrix $I - h \gamma _ { \imath \imath } J$ . Of special interest are methods for which $\gamma _ { 1 1 } = . . . = \gamma _ { s s } = \gamma$ , so that we need only one LU-decomposition per step.

Non-autonomous problems. The equation

$$
y ^ { \prime } = f ( x , y )
$$

can be converted to autonomous form by adding $x ^ { \prime } = 1$ . If method (7.4) is applied to the augmented system, the components corresponding to the $x$ -variable can be computed explicitly and we arrive at

$$
\begin{array} { l } { { \displaystyle k _ { \scriptscriptstyle 3 } = h f \bigg ( x _ { 0 } + \alpha _ { \scriptscriptstyle 3 } h , y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \scriptscriptstyle 3 \jmath } k _ { \jmath } \bigg ) + \gamma _ { \scriptscriptstyle 3 } h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) + h \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { \imath \jmath } k _ { \jmath } } } \\ { { \displaystyle y _ { \scriptscriptstyle 1 } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } k _ { \jmath } , ~ } } \end{array}
$$

where the additional coeficients are given by

$$
\alpha _ { \ i } = \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } , \qquad \gamma _ { \imath } = \sum _ { \jmath = 1 } ^ { \imath } \gamma _ { \imath \jmath } .
$$

Implicit differential equations. Suppose the problem is of the form

$$
M y ^ { \prime } = f ( x , y )
$$

where $M$ is a constant matrix (nonsingular for the moment). If we formally multiply (7.2b) with $M ^ { - 1 }$ , apply method (7.4a),and then multiply the resulting formula

with $M$ , we obtain

$$
\begin{array} { c } { { M k _ { \iota } = h f \displaystyle \bigg ( x _ { 0 } + \alpha _ { \iota } h , y _ { 0 } + \sum _ { j = 1 } ^ { i - 1 } \alpha _ { \iota j } k _ { \iota } \bigg ) + \gamma _ { \iota } h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) + h \displaystyle \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \sum _ { j = 1 } ^ { \iota } \gamma _ { \iota j } k _ { j } } } \\ { { y _ { 1 } = y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { s } b _ { j } k _ { j } . } } \end{array}
$$

An advantage of this formulation is that the inversion of $M$ is avoided and that possible band-structures of the matrices $M$ and $\partial f / \partial y$ are preserved.

# Order Conditions

Conditions on the free parameters which ensure that the method is of order $p$ ,i.e., the local error satisfies

$$
y ( x _ { 0 } + h ) - y _ { 1 } = \mathcal { O } \bigl ( h ^ { p + 1 } \bigr ) , \qquad 
$$

can be obtained either by straightforward differentiation or by the use of the theorems on $B$ -series (Sect. II.12). We follow here the first approach, since it requires only the knowledge of Sect. II.2. The second possibility is sketched in Exercise 2.

As in Sect.II.2, we write the system (7.2) in tensor notation and Method (7.4) as1

$$
\begin{array} { l } { { \displaystyle k _ { \jmath } ^ { J } = h f ^ { J } ( g _ { \jmath } ) + h \sum _ { K } f _ { K } ^ { J } ( y _ { 0 } ) \sum _ { k } \gamma _ { \jmath k } k _ { k } ^ { K } } } \\ { { \displaystyle g _ { \imath } ^ { J } = y _ { 0 } ^ { J } + \sum _ { \jmath } \alpha _ { \imath \jmath } k _ { \jmath } ^ { J } , } } \\ { { \displaystyle y _ { 1 } ^ { J } = y _ { 0 } ^ { J } + \sum _ { \jmath } b _ { \jmath } k _ { \jmath } ^ { J } . } } \end{array}
$$

Again,we use Leibniz's rule (cf. (I1.2.4))

$$
\left. ( k _ { \ j } ^ { J } ) ^ { ( q ) } \right| _ { h = 0 } = q \big ( f ^ { J } ( g _ { \ j } ) \big ) ^ { ( q - 1 ) } \big | _ { h = 0 } + q \sum _ { K } f _ { K } ^ { J } ( y _ { 0 } ) \sum _ { k } \gamma _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( q - 1 ) } \big | _ { h = 0 }
$$

and have from the chain rule(cf. Sect.II.2,(2.6;1),(2.6;2))

$$
\begin{array} { l } { { \displaystyle \left( f ^ { J } ( g _ { \jmath } ) \right) ^ { \prime } = \sum _ { K } f _ { K } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime } } } \\ { { \displaystyle \left( f ^ { J } ( g _ { \jmath } ) \right) ^ { \prime \prime } = \sum _ { K , L } f _ { K L } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime } \cdot ( g _ { \jmath } ^ { L } ) ^ { \prime } + \sum _ { K } f _ { K } ^ { J } ( g _ { \jmath } ) \cdot ( g _ { \jmath } ^ { K } ) ^ { \prime \prime } } } \end{array}
$$

etc.Inserting this into (7.6) we obtain recursively

$$
\begin{array} { l } { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 0 ) } | _ { i = 0 } = 0 } } \\ { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 1 ) } | _ { k = 0 } = f ^ { J } } } \\ { { \displaystyle \langle k _ { j } ^ { J } \rangle ^ { ( 2 ) } | _ { k = 0 } = 2 \sum _ { K } ^ { J } f _ { K } ^ { J } f ^ { K } \sum _ { k } \alpha _ { j k } + 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } \gamma _ { j k } } } \\ { { \displaystyle ~ = 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } ^ { K } \langle \alpha _ { k } + \gamma _ { j k } \rangle } } \\ { { \displaystyle \big ( k _ { j } ^ { J } \rangle ^ { ( 3 ) } \big ) | _ { k = 0 } = 3 \sum _ { K , L } ^ { J } f _ { K L } ^ { J } f ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { j k } \alpha _ { j l } } } \\ { { \displaystyle ~ + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } ^ { K } \big ( \alpha _ { k } + \gamma _ { j k } \big ) \big ( \alpha _ { k l } + \gamma _ { k k } \big ) } } \end{array}
$$

etc. All elementary differentials are evaluated at $y _ { 0 }$ . Comparing the derivatives of the numerical solution $( q \ge 1 )$

$$
( y _ { 1 } ^ { J } ) ^ { ( q ) } | _ { h = 0 } = \sum _ { j } b _ { \jmath } ( k _ { \jmath } ^ { J } ) ^ { ( q ) } | _ { h = 0 }
$$

with those of the true solution (Sect. I.2, Formula (2.7;1), (2.7;2), (2.7;3)), we arrive at the following conditions for order three:

$$
\begin{array} { c c c c } { { \cdot _ { \jmath } } } & { { } } & { { } } & { { \sum b _ { \jmath } = 1 } } \\ { { } } & { { } } & { { } } & { { \sum b _ { \jmath } ( \alpha _ { \jmath k } + \gamma _ { \jmath k } ) = { \frac { 1 } { 2 } } } } \\ { { } } & { { } } & { { } } & { { } } \\ { { \iota _ { \mathcal { N } _ { \jmath } ^ { l } } } } & { { } } & { { } } & { { \sum b _ { \jmath } \alpha _ { \jmath k } \alpha _ { \jmath l } = { \frac { 1 } { 3 } } } } \\ { { } } & { { } } & { { } } & { { \sum b _ { \jmath } ( \alpha _ { \jmath k } + \gamma _ { \jmath k } ) ( \alpha _ { k l } + \gamma _ { k l } ) = { \frac { 1 } { 6 } } . } } \end{array}
$$

The only difference with the order conditions for Runge-Kutta methods is that at singly-branched vertices of the corresponding trees $\alpha _ { \ j k }$ is replaced by $\alpha _ { \ j k } + \gamma _ { \ j k } .$ In order to arrive at a general result, the formulas obtained motivate the following definition:

Definition 7.2. Let $t$ be a labelled tre of order $q$ with root $j$ ; we denote by

$$
\Phi _ { j } ( t ) = \sum _ { k , l , \dots } \varphi _ { \jmath , k , l , \dots }
$$

the sum over the remaining $q - 1$ indices $k , l , \ldots$ etc. The summand $\varphi _ { \ j , k , l , \dots }$ is a product of $q - 1$ factors,which are

$\alpha _ { k l } + \gamma _ { k l }$ if $l$ is the only son of $k$ ；   
αkl if $l$ is a son of $k$ and $k$ has at least two sons.

Using the recursive representation of trees (Def.I.2.12) we have $\Phi _ { \jmath } ( \tau ) = 1$ for the only tree of order 1 and,as in (I1.2.19),

$$
\Phi _ { j } ( t ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { k _ { 1 } , \dots , k _ { m } } \alpha _ { _ { j k _ { 1 } } } \dots \alpha _ { _ { j k _ { m } } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \dots \Phi _ { k _ { m } } ( t _ { m } ) } & { \mathrm { i f } t = [ t _ { 1 } , \dots , t _ { m } ] , } \\ { \displaystyle \sum _ { k } ( \alpha _ { _ { j k } } + \gamma _ { j k } ) \Phi _ { k } ( t _ { 1 } ) } & { \mathrm { i f } t = [ t _ { 1 } ] . } \end{array} \right.
$$

Theorem 7.3. The derivatives of $k _ { \jmath } ^ { J }$ , given by (7.4), satisfy

$$
( k _ { \jmath } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = \sum _ { t \in L T _ { q } } \gamma ( t ) \Phi _ { j } ( t ) F ^ { J } ( t ) ( y _ { 0 } )
$$

and the numerical solution $y _ { 1 } ^ { J }$ satisfies

$$
( y _ { 1 } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = \sum _ { t \in L T _ { q } } \gamma ( t ) \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) F ^ { J } ( t ) ( y _ { 0 } ) ,
$$

where $F ^ { J } ( t )$ are the elementary differentials (Definition II.2.3).

Proof. Because of (7.8) we only have to prove the first formula. This is done by induction on $q$ and follows exactly the lines of the proof of Theorem I1.2.11. We use (7.6), replace the expression $f ^ { J } ( g _ { _ { J } } ) ^ { ( q - 1 ) }$ by Faa di Bruno's formula (Lemma I.2.8), use

$$
( g _ { j } ^ { K } ) ^ { ( \delta ) } = \sum _ { k } \alpha _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( \delta ) }
$$

for the derivatives of $g _ { \jmath }$ and insert the induction hypothesis $( 7 . 7 ; \delta )$ with $\delta \leq q - 1$ This gives

$$
\begin{array} { l } { { \displaystyle \left( k _ { j } ^ { J } \right) ^ { ( q ) } \Big \} _ { h = 0 } = q \displaystyle \sum _ { u \in L S _ { q } } \displaystyle \sum _ { t _ { 1 } \in L T _ { \delta _ { 1 } } } \displaystyle \sum _ { \substack { t _ { m } \in L T _ { \delta _ { m } } } } \gamma ( t _ { 1 } ) \ldots \gamma ( t _ { m } ) } } \\ { ~ \cdot \displaystyle \sum _ { k _ { 1 } } \alpha _ { \jmath k _ { 1 } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \ldots \displaystyle \sum _ { k _ { m } } \alpha _ { \jmath k _ { m } } \Phi _ { k _ { m } } ( t _ { m } ) }  \\ { ~ \cdot \displaystyle \sum _ { \substack { k _ { 1 } , \ldots , K _ { m } } } f _ { K _ { 1 } \dots K _ { m } } ^ { J } ( \jmath _ { 0 } ) F ^ { K _ { 1 } } ( t _ { 1 } ) ( \jmath _ { 0 } ) \ldots F ^ { K _ { m } } ( t _ { m } ) ( \jmath _ { 0 } ) }  \\ { ~ + q \displaystyle \sum _ { t _ { 1 } \in L T _ { \delta ^ { - 1 } } } \gamma ( t _ { 1 } ) \sum _ { k } \gamma _ { \jmath k } \Phi _ { k } ( t _ { 1 } ) \sum _ { K } f _ { K } ^ { \gamma } ( \jmath _ { 0 } ) F ^ { K } ( t _ { 1 } ) ( \jmath _ { 0 } ) . } \end{array}
$$

The one-to-one correspondence between the summation set $\{ ( u , t _ { 1 } , \dots , t _ { m } ) | u \in L S _ { q }$ ， $t _ { j } \in L T _ { \delta _ { j } } \}$ and $L T _ { q }$ together with the recursion formulas (7.9), (II.2.17), (II.2.i8) now yields the result. □

Comparing Theorems 7.3 and II.2.6 we obtain:

Table 7.1. Trees and order conditions up to order 5   

<table><tr><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>graph</td><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>t）</td><td rowspan=1 colspan=1>Pt()</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>可</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>t21</td><td rowspan=1 colspan=1>”</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>MBjk</td><td rowspan=1 colspan=1>1/2- γ</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>t31t32</td><td rowspan=1 colspan=1>兴</td><td rowspan=1 colspan=1>36</td><td rowspan=1 colspan=1>∑kQkajlMk,Bkβkl</td><td rowspan=1 colspan=1>1/31/6-γ+γ²</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>t41t42t43t44</td><td rowspan=1 colspan=1>k  m山X宝</td><td rowspan=1 colspan=1>481224</td><td rowspan=1 colspan=1>∑k,,makaj1am∑klmajkβklagm∑k,L,mBjkakakm∑k,,mBkβkiBIm</td><td rowspan=1 colspan=1>1/41/8-γ/31/12- γ/31/24-γ/2+3γ²/2-γ3</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>t51东县t52t53t54t55t5657t58t59</td><td rowspan=1 colspan=1>东县3</td><td rowspan=1 colspan=1>5东县10153020204060120</td><td rowspan=1 colspan=1>ΣajkaJlαjmα Jp∑ajkβkiα jmαJp∑αJkaklαkmαjpMaJkβkiβImαjp∑aJkβkiajmβmp∑βjkaklQkmQkp∑Bkakiβimakp∑βkβkiaimalp∑βJkβkiβimβmp</td><td rowspan=1 colspan=1>1/51/10- ~/41/151/30 - γ/4+ γ²/31/20- γ/4+ γ²/31/20- γ/41/40-5γ/24+ γ²/31/60- γ/6+γ²/31/120-γ/6+γ²-2γ³+γ4</td></tr></table>

# Theorem 7.4. A Rosenbrock method (7.4) with $J = f ^ { \prime } ( y _ { 0 } )$ is of order $p$ if

$$
\sum _ { \ j } b _ { \ j } \Phi _ { \ j } ( t ) = \frac { 1 } { \gamma ( t ) } \qquad f o r \quad \varrho ( t ) \leq p .
$$

The expressions $\Phi _ { j } ( t )$ simplify, if we introduce the abbreviation

$$
\beta _ { \imath \jmath } = \alpha _ { \imath j } + \gamma _ { \imath j } .
$$

The order conditions (7.11) for all trees up to order 5 are given in Table 7.1.

A further simplification of the order conditions (7.11) is possible if

$$
\gamma _ { i i } = \gamma \qquad { \mathrm { f o r ~ a l l } } i
$$

(It is unfortunate that in the current literature the letter $\gamma$ is used for the parameter in (7.4) as well as for $\gamma ( t )$ in (7.11) and we hope that no confusion will arise). In the same way as for DIRK methods, the summations in the expressions for $\Phi _ { j } ( t )$

in the 5th column of Table 7.1 again contain more terms than the corresponding ex-pressions for explicit Runge-Kutta methods, since the matrix $\gamma _ { \imath \jmath }$ (and hence $\beta _ { i j } )$ contains non-zero elements in the diagonal. The difference is that here these diagonal $\gamma$ appear only for singly-branched vertices (see Definition 7.2). Therefore the procedure explained in Sect.IV.6 (see Formulas (6.1') and (6.1") must be slightly modified and leads to order conditions of the form

$$
\sum _ { j } ^ { } { } ^ { b _ { j } } \Phi _ { j } ( t ) = p _ { t } ( \gamma )
$$

where the polynomials $p _ { t } ( \gamma )$ are listed in the last column of Table 7.1.

# The Stability Function

If we apply Method (7.4） to the test equation $y ^ { \prime } = \lambda y$ and if we assume $J =$ $f \prime ( y _ { 0 } ) = \lambda$ then the numerical solution becomes $y _ { 1 } = R ( h \lambda ) y _ { 0 }$ with

$$
R ( z ) = 1 + z b ^ { T } ( I - z B ) ^ { - 1 } \mathbb { 1 }
$$

where we have used the notation $b ^ { T } = \left( b _ { 1 } , \ldots , b _ { s } \right)$ and $B = ( \beta _ { i j } ) _ { \imath , j = 1 } ^ { s }$ . Since $B$ is alower triangular matrix, the stability function (7.14) is equal to that of a DIRKmethod with RK-matrix $B$ . Properties of such stability functions have already been investigated in Sect.IV.6.

# Construction of Methods of Order 4

In order to construct 4-stage Rosenbrock methods of order 4 we list, for convenience,the whole set of order conditions (c.f. Table 7.1.).

$$
\begin{array} { r l r l } & { \ddots } & & { \hat { b } _ { 1 } + \hat { b } _ { 2 } + \hat { b } _ { 3 } + \hat { b } _ { 4 } = 1 } \\ & { \Biggl . \hfill } & & { \Biggl . \int } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 2 } - \gamma = \mathcal { P } _ { 2 1 } ( \gamma ) } \\ & { \times } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 2 } - \gamma = \mathcal { P } _ { 2 1 } ( \gamma ) } \\ & { \searrow } & & { \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } ( 3 4 \partial _ { 4 } \partial _ { 2 } ^ { ( 0 ) } - \partial _ { 4 } \partial _ { 3 } ^ { ( 0 ) } ) = \frac { 1 } { 2 0 } - \gamma + \gamma ^ { 2 } = \mathcal { P } _ { 3 2 } ( \gamma ) } \\ & { \ddots } & & { \hat { b } _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } + \hat { b } _ { 4 } \partial _ { 4 } ^ { ( 0 ) } + \frac { 1 } { 4 } } \\ & { \searrow } & & { \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \alpha _ { 2 } \partial _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } \alpha _ { 4 } ( \alpha _ { 4 } \partial _ { 2 } ^ { ( 0 ) } + \alpha _ { 4 } \partial _ { 3 } ^ { ( 0 ) } ) = \frac { 1 } { 8 } - \frac { \gamma } { 3 } - \gamma = \mathcal { P } _ { 4 2 } ( \gamma ) } \\ & {  \times } & &  \hat { b } _ { 3 } \partial _ { 3 } ^ { ( 0 ) } \alpha _ { 2 } ^ { ( 0 ) } + \hat { b } _ { 4 } ( 3 \alpha _ { 4 } ^ { ( 0 ) } \alpha _ { 2 } ^ { ( 0 ) } + \beta _ { 3 } \gamma \alpha _ { 3 }  \end{array}
$$

Here we have used the abbreviations

$$
\alpha _ { i } = \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \imath \jmath } , \qquad \beta _ { i } ^ { \prime } = \sum _ { \jmath = 1 } ^ { i - 1 } \beta _ { \imath \jmath } .
$$

For the sake of step size control we also look for an embedded formula (Wolfbrandt 1977,Kaps & Rentrop 1979)

$$
\widehat { y } _ { 1 } = y _ { 0 } + \sum _ { j = 1 } ^ { s } \widehat { b } _ { \jmath } k _ { j }
$$

which uses the same $k _ { j }$ -values as (7.4), but has different weights. This method should have_order 3,i.e.,the four conditions (7.15a)-(7.15d) should be satisfied also for the $\widehat { b } _ { \iota }$ . These equations constitute the linear system

$$
\left( { \begin{array} { c c c c } { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { \beta _ { 2 } ^ { \prime } } & { \beta _ { 3 } ^ { \prime } } & { \beta _ { 4 } ^ { \prime } } \\ { 0 } & { \alpha _ { 2 } ^ { 2 } } & { \alpha _ { 3 } ^ { 2 } } & { \alpha _ { 4 } ^ { 2 } } \\ { 0 } & { 0 } & { \beta _ { 3 2 } \beta _ { 2 } ^ { \prime } } & { \sum ^ { \prime } \beta _ { 4 j } \beta _ { j } ^ { \prime } } \end{array} } \right) { \left( \begin{array} { c } { { \widehat { b } _ { 1 } } } \\ { { \widehat { b } _ { 2 } } } \\ { { \widehat { b } _ { 3 } } } \\ { { \widehat { b } _ { 4 } } } \end{array} \right) } = \left( { \begin{array} { c } { 1 } \\ { 1 / 2 - \gamma } \\ { 1 / 3 } \\ { 1 / 6 - \gamma + \gamma ^ { 2 } } \end{array} } \right) .
$$

Whenever the matrix in (7.18) is regular, uniqueness of the solutions of the linear system implies $\widehat { b } _ { \iota } = b _ { i } \ ( i = 1 , \dots , 4 )$ and the approximation $\widehat { y } _ { 1 }$ cannot be used for step size control. We therefore have to require that the matrix (7.18) be singular, i.e.,

$$
( \beta _ { 2 } ^ { \prime } \alpha _ { 4 } ^ { 2 } - \beta _ { 4 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) \beta _ { 3 2 } \beta _ { 2 } ^ { \prime } = ( \beta _ { 2 } ^ { \prime } \alpha _ { 3 } ^ { 2 } - \beta _ { 3 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) \sum _ { j = 2 } ^ { 3 } \beta _ { 4 j } \beta _ { j } ^ { \prime } .
$$

This condition guarantees the existence of a 3rd order embedded method (7.17), whenever (7.15) possesses a solution.The computation of the coefficients $\sigma _ { \imath \jmath } ,$ $\beta _ { i _ { 1 } } , \gamma , b _ { \iota }$ satisfying (7.15),(7.16) and (7.19) is now done in the following steps:

Step 1. Choose $\gamma > 0$ such that the stability function (7.14) has desirable stability properties (c.f. Table 6.3).

Step 2. Choose $\alpha _ { 2 } , \alpha _ { 3 } , \alpha _ { 4 }$ and $b _ { 1 } , b _ { 2 } , b _ { 3 } , b _ { 4 }$ in such a way that the three conditions (7.15a),(7.15c), (7.15e) are fulfilled. One obviously has four degrees of freedom in this choice. Observe that the $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { \alpha } _ { \imath } \right)$ need not be the coeficients of a standard quadrature formula, since $\sum b _ { \imath } \alpha _ { \imath } = 1 / 2$ need not be satisfied.

Step 3. Take $\beta _ { 4 3 }$ as a free parameter and compute $\beta _ { 3 2 } \beta _ { 2 } ^ { \prime }$ from (7.15h)， then $\left( \beta _ { 4 2 } \beta _ { 2 } ^ { \prime } + \beta _ { 4 3 } \beta _ { 3 } ^ { \prime } \right)$ from(7.15d). These expressions, inserted into (7.19) yield a second relation between $\beta _ { 2 } ^ { \prime } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ (the first one is (7.15b)). Eliminating $\left( b _ { 4 } \beta _ { 4 2 } + \right.$ $b _ { 3 } \beta _ { 3 2 } )$ from (7.15d) and (7.15g) gives

$$
b _ { 4 } \beta _ { 4 3 } ( \beta _ { 2 } ^ { \prime } \alpha _ { 3 } ^ { 2 } - \beta _ { 3 } ^ { \prime } \alpha _ { 2 } ^ { 2 } ) = \beta _ { 2 } ^ { \prime } p _ { 4 3 } ( \gamma ) - \alpha _ { 2 } ^ { 2 } p _ { 3 2 } ( \gamma ) ,
$$

a third linear relation for $\beta _ { 2 } ^ { \prime } , \beta _ { 3 } ^ { \prime } , \beta _ { 4 } ^ { \prime }$ . The resulting linear system is regular if $b _ { 4 } \beta _ { 4 3 } \alpha _ { 2 } \gamma ( 3 \gamma - 1 ) \neq 0$

Step 4. Once the $\beta _ { i } ^ { \prime }$ are known we can find $\beta _ { 3 2 }$ and $\beta _ { 4 2 }$ from the values of $\beta _ { 3 2 } \beta _ { 2 } ^ { \prime }$ ， $\left( \beta _ { 4 2 } \beta _ { 2 } ^ { \prime } + \beta _ { 4 3 } \beta _ { 3 } ^ { \prime } \right)$ obtained in Step 3.

Step 5. Choose $\alpha _ { 3 2 } , \alpha _ { 4 2 } , \alpha _ { 4 3 }$ according to (7.15f). One has two degrees of freedom to do this. Finally, the values $\alpha _ { \imath } , \beta _ { \imath } ^ { \prime }$ yield $\alpha _ { \imath 1 } , \beta _ { \imath 1 }$ via condition (7.16).

Table 7.2 Rosenbrock methods of order 4   

<table><tr><td rowspan=1 colspan=1>method</td><td rowspan=1 colspan=1>Y</td><td rowspan=1 colspan=1>parameter choices</td><td rowspan=1 colspan=1>A(a)-stable</td><td rowspan=1 colspan=1>|R(00）</td></tr><tr><td rowspan=1 colspan=1>GRK4A(Kaps-Rentrop 79)GRK4T(Kaps-Rentrop 79)Shampine (1982)Veldhuizen (1984)Veldhuizen (1984)L-stable method</td><td rowspan=1 colspan=1>0.3950.2310.50.2257080.50.572816</td><td rowspan=1 colspan=1>α2 = 0.438,α3 = 0.87b4 = 0.25α2=2γ，(7.22),b=0α2=2γ,(7.22),b3=0α2 =2γ，(7.22),b3=0α2 =2γ,α3=0.5,b3=0α2 =2γ,(7.22),b3 =0</td><td rowspan=1 colspan=1>π/289.3°π/289.5°π/2π/2</td><td rowspan=1 colspan=1>0.9950.4541/30.241/30</td></tr></table>

Most of the popular Rosenbrock methods are special cases of this construction (see Table 7.2). Usually the remaining free parameters are chosen as follows: if we require

$$
\alpha _ { 4 3 } = 0 , \qquad \alpha _ { 4 2 } = \alpha _ { 3 2 } \quad \mathrm { a n d } \quad \alpha _ { 4 1 } = \alpha _ { 3 1 }
$$

then the argument of $f$ in （7.4） is the same for $i = 3$ and $i = 4$ .Hence,the number of function evaluations is reduced by one. Further free parameters can be determined so that several order conditions of order five are satisfied. Multiplying the condition (7.15g) with $\alpha _ { 2 }$ and subtracting it from the order condition for the tree $t _ { 5 6 }$ yields

$$
b _ { 4 } \beta _ { 4 3 } \alpha _ { 3 } ^ { 2 } ( \alpha _ { 3 } - \alpha _ { 2 } ) = p _ { 5 6 } ( \gamma ) - \alpha _ { 2 } p _ { 4 3 } ( \gamma ) .
$$

This determines $\beta _ { 4 3 }$ ．The order condition for $t _ { 5 1 }$ can also easily be fulfilled in Step 2. If $\alpha _ { 3 } = \alpha _ { 4 }$ (see (7.20) this leads to the restriction

$$
\alpha _ { 3 } = \frac { 1 / 5 - \alpha _ { 2 } / 4 } { 1 / 4 - \alpha _ { 2 } / 3 } .
$$

In Table 7.2 we collect some well-known methods. All of them satisfy (7.20) and (7.21） (Only exception: the second method of van Veldhuizen for $\gamma = 0 . 5$ has $\beta _ { 4 3 } = 0$ instead of (7.21)). The definition of the remaining free parameters is given in the first two columns. The last columns indicate some properties of the stability function.

# Higher Order Methods

As for explicit Runge-Kutta methods the construction of higher order methods is facilitated by the use of simplifying assumptions. First, the condition

$$
\sum _ { \ i = \ i } ^ { s } b _ { \ i } \beta _ { \ i \jmath } = b _ { \jmath } ( 1 - \alpha _ { \jmath } ) , \qquad \ i = 1 , \dots , s
$$

plays a role similar to that of (II.1.12) for explicit Runge-Kutta methods. It implies that the order condition of the left-hand tree in Fig.7.1 is a consequence of the two on the right-hand side. A difference to Runge-Kutta methods is that here the vertex directly above the root has to be multiply-branched.

The second typeofsimplifing asumptionis (with $\begin{array} { r } { \beta _ { k } = \sum _ { l = 1 } ^ { k } \beta _ { k l } ) } \end{array}$

$$
\sum _ { k = 1 } ^ { \jmath - 1 } \alpha _ { \jmath k } \beta _ { k } = \frac { \alpha _ { \jmath } ^ { 2 } } { 2 } , \qquad j = 2 , \ldots , s .
$$

It has an effect similar to that of (II.5.7). As a consequence of (7.24) the order conditions of the two trees in Fig.7.2 are equivalent. Again the vertex marked by an arrow has to be multiply-branched.

The use of the above simplifying assumptions has been exploited by Kaps & Wanner (1981） for their construction of methods up to order 6. Still higher order methods would need generalizations of the above simplifying assumptions (in analogy to $C ( \eta )$ and $D ( \zeta )$ of Sect.I1.7).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/24e1ac3dd4d2f0e54838dab6227c35443a00064ba2728ee38a2f2e5f50dbad9c.jpg)  
Fig. 7.1. Reduction with (7.23)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/6f67bcddd10b07db4518f9c97ea88e439631c8f64308c5af0ef70c16e4c1d75f.jpg)  
Fig. 7.2. Reduction with (7.24)

# Implementation of Rosenbrock-Type Methods

A direct implementation of (7.4) requires,at each stage, the solution of a linear system with the matrix $I - h \gamma _ { \imath \imath } J$ and also the matrix-vector multiplication $J$ $\sum \gamma _ { \imath \jmath } k _ { \jmath }$ . The latter can be avoided by the introduction of the new variables

$$
u _ { \ i \ i } = \sum _ { \jmath = 1 } ^ { \ i } \gamma _ { \imath \jmath } k _ { \jmath } , \qquad i = 1 , \ldots , s .
$$

If $\gamma _ { \imath \imath } \neq 0$ for all $i$ , the matrix $\boldsymbol { \Gamma } = ( \gamma _ { \imath \jmath } )$ is invertible and the $k _ { \imath }$ can be recovered from the $u _ { \iota }$ ：

$$
k _ { \ i } = \frac { 1 } { \gamma _ { \ i \ i } } u _ { \ i } - \sum _ { \ j = 1 } ^ { \ i - 1 } c _ { \ i j } u _ { \ j } , \qquad C = \mathrm { d i a g } ( \gamma _ { 1 1 } ^ { - 1 } , \ldots , \gamma _ { s s } ^ { - 1 } ) - \Gamma ^ { - 1 } .
$$

Inserting this formula into (7.4) and dividing by $h$ yields

$$
\begin{array} { c } { { \displaystyle \left( \frac { 1 } { h \gamma _ { \scriptscriptstyle { \vphantom { \bigg ( } } I } } { \cal I } - { \cal J } \right) u _ { \scriptscriptstyle { \vphantom { \bigg ( } } I } \left( y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \iota _ { \jmath } } u _ { \jmath } \right) + \sum _ { \jmath = 1 } ^ { \imath - 1 } \left( \frac { c _ { \iota _ { \jmath } } } { h } \right) u _ { \jmath } , \qquad i = 1 , \dots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { s } m _ { \jmath } u _ { \jmath } , } } \end{array}
$$

where

$$
( a _ { \imath j } ) = ( \alpha _ { \imath j } ) \Gamma ^ { - 1 } , \qquad ( m _ { 1 } , \ldots , m _ { s } ) = ( b _ { 1 } , \ldots , b _ { s } ) \Gamma ^ { - 1 } .
$$

Compared to (7.4) the formulation (7.25) of a Rosenbrock method avoids not only the above mentioned matrix-vector multiplication, but also the $n ^ { 2 }$ multiplications for $\{ \gamma _ { \imath \imath } h \} J$ . Similar transformations were first proposed by Wolfbrandt (1977), Kaps & Wanner (1981) and Shampine (1982). The formulation (7.25) can be found in Kaps,Poon & Bui (1985).

For non-autonomous problems this transformation yields

$$
\begin{array} { r } { \Big ( \displaystyle \frac { 1 } { h \gamma _ { \eta _ { 2 } } } I - \displaystyle \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \Big ) u _ { \iota } = f \Big ( x _ { 0 } + \alpha _ { \iota } h , y _ { 0 } + \displaystyle \sum _ { j = 1 } ^ { i - 1 } a _ { \iota _ { j } } u _ { j } \Big ) } \\ { + \displaystyle \sum _ { j = 1 } ^ { \iota - 1 } \Big ( \displaystyle \frac { c _ { \iota j } } { h } \Big ) u _ { j } + \gamma _ { \iota } h \displaystyle \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) } \end{array}
$$

with $\alpha _ { \iota }$ and $\gamma _ { i }$ given by (7.5).

For implicit differential equations of the form (7.2b) the transformed Rosenbrock method becomes

$$
\begin{array} { l } { \displaystyle \left( \frac { 1 } { h \gamma _ { \scriptscriptstyle { \mathscr { N } _ { \tau } } } } { M } - \frac { \partial f } { \partial y } ( x _ { 0 } , y _ { 0 } ) \right) u _ { \scriptscriptstyle { \tau } } = f \Big ( x _ { 0 } + \alpha _ { i } h , y _ { 0 } + \sum _ { \tau = 1 } ^ { \tau - 1 } a _ { \scriptscriptstyle { \tau \mathscr { I } } } u _ { \tau } \Big ) } \\ { \displaystyle + { M \sum _ { \tau = 1 } ^ { i - 1 } \left( \frac { c _ { \tau _ { \mathscr { I } } } } { h } \right) u _ { \scriptscriptstyle { \tau } } } + \gamma _ { \scriptscriptstyle { \tau } } h \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } ) . } \end{array}
$$

Coding. Rosenbrock methods are nearly as simple to implement as explicit Runge-Kutta methods. The only difference is that at each step the Jacobian $\partial f / \partial y$ has to be evaluated and $s$ linear systems have to be solved. Thus, one can take an explicit RK code (say DOPRI5),add four lines which compute $\partial f / \partial y$ by finite differences (or call a user-supplied subroutine JAC which furnishes it analytically); add further a call to a Gaussian DEComposition routine, and add to each evaluation-stage a call to a linear SOLver. Since the method is of order 4(3), the step size prediction formula

$$
h _ { n e w } = h \cdot \operatorname* { m i n } \Bigl \{ 6 . , \operatorname* { m a x } \Bigl ( 0 . 2 , 0 . 9 \cdot ( T o l / e r r ) ^ { 1 / 4 } \Bigr ) \Bigr \}
$$

seems appropriate.

However, we want the code to work economically for non-autonomous problems as well as for implicit equations. Further, if the dimension of the system is large, it becomes crucial that the linear algebra be done,whenever possible, in banded form. All these possibilities,autonomous or not, implicit or explicit, $\partial f / \partial y$ banded or not, $B$ banded or not, $\partial f / \partial y$ analytic or not,("... that is the question") lead to $2 ^ { 5 }$ different cases, for each of which the code contains special parts for high efficiency. Needless to say, it works well on all stiff problems of Sect.IV.1. A more thorough comparison and testing will be given in Sect.IV.10.

# The“Hump"

On some very stiff equations, however, the code shows a curious behaviour: con-sider the van der Pol equation in singular perturbation form(1.5'） with

$$
\varepsilon = 1 0 ^ { - 6 } , \quad y _ { 1 } ( 0 ) = 2 , \quad y _ { 2 } ( 0 ) = - 0 . 6 6 .
$$

We further select method GRK4T (Table 7.2; each other method there behaves similarly)and $T o l = 7 \cdot 1 0 ^ { - 5 }$ . Fig.7.3 shows the numerical solution $y _ { 1 }$ as well as the step sizes chosen by the code. There all rejected steps are indicated by an $\times$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/ee80221625c1291378fc33ce9ed6e8c522a014bc01be786c1f4335f0a56c4d77.jpg)  
Fig. 7.3. Step sizes for GRK4T at Equation (1.5')

Curious step size drops (by a factor of about $1 0 ^ { - 3 }$ ) occur without any apparent exterior reason. Further, these drops are accompanied by a huge number of step rejections (up to 2O). In order to understand this phenomenon, we present in the left picture of Fig.7.4 the exact local error as well as the estimated local error $\| y _ { 1 } - { \widehat { y } } _ { 1 } \|$ at $x = 0 . 5 5 1 3 9$ as a function of the step size $h$ (both in logarithmic scale). The current step size is marked by large symbols. The error behaves like $C \cdot h ^ { 5 }$ only for very small $h \left( \leq 1 0 ^ { - 6 } = \varepsilon \right)$ .Between $h = 1 0 ^ { - 5 }$ and the step size actually used $\left\{ \approx 1 0 ^ { - 2 } \right\}$ the error is more or less constant. Whenever this constant is larger than $T o l$ (horizontal broken line), the code is forced to decrease the step size until $h \approx \varepsilon$ . As a first remedy, we accelerate this lengthy process, as Shampine (1982) also did,by more drastical step size reductions $\left( h _ { n e w } = h / 1 0 \right)$ after each second consecutive step rejection. It also turns out (see right picture of Fig.7.4) that the effect disappears in the neighbourhood of the actual step size for the $L$ - stable method (where $R ( \infty ) = 0 ,$ ).Methods with $R ( \infty ) = 0$ and also ${ \widehat { R } } ( \infty ) = 0$ have been derived by Kaps & Ostermann (1990).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0002_pages_0071-0140/auto/images/4fc7cdf4f5ba909f0bfec76a7cd816cf2f5473c07b9117f37c79b5cd9b5af1d6.jpg)  
Fig.7.4. Study of local error for (1.5') at $x = 0 . 5 5 1 3 9$

A more thorough understanding of these phenomena is possible by the consideration of singular perturbation problems (Chapter VI).

# Methods with Inexact Jacobian(W -Methods)

The relevant question is now, what is the cheapest type of implicitness we have to require. (Steihaug& Wolfbrandt 1979)

All the above theory is built on the assumption that $J$ is the exact Jacobian $\partial f / \partial y$ This implies that the matrix must be evaluated at every step,which can make the computations costly. The following attempt, due to Steihaug & Wolfbrandt (1979), searches for order conditions which assure classical order for all approximations $A$ of $\partial f / \partial y$ . The latter is then maintained over several steps and is just used to assure stability. The derivation of the order conditions must now be done somewhat differently: if $J$ is replaced by an arbitrary matrix $A$ ,Formula(7.6) becomes

$$
( k _ { \jmath } ^ { J } ) ^ { ( q ) } \big | _ { h = 0 } = q ( f ^ { J } ( g _ { \jmath } ) ) ^ { ( q - 1 ) } | _ { h = 0 } + q \sum _ { K } A _ { K } ^ { J } \sum _ { k } \gamma _ { \jmath k } ( k _ { k } ^ { K } ) ^ { ( q - 1 ) } | _ { h = 0 }
$$

where $A = ( A _ { K } ^ { J } ) _ { J , K = 1 } ^ { n }$ , and we obtain

$$
( k _ { \ j } ^ { J } ) ^ { ( 2 ) } \big | _ { \phantom { h = 0 } h = 0 } = 2 \sum _ { K } f _ { K } ^ { J } f ^ { K } \sum _ { k } \alpha _ { \ j k } + 2 \sum _ { K } A _ { K } ^ { J } f ^ { K } \sum _ { k } \gamma _ { \ j k } .
$$

Inserted into (7.8), the first term must equal the derivative of the exact solution and

the second must be zero. Similarly, we obtain instead of (7.7;3)

$$
\begin{array} { l } { { \displaystyle \left( k _ { _ { J } } ^ { J } \right) ^ { ( 3 ) } \big | _ { h = 0 } = 3 \sum _ { K , L } f _ { K L } ^ { J } f ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \alpha _ { _ { J l } } } } & { { ( 7 . 3 1 ; 2 ) } } \\ { { \displaystyle \qquad + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \alpha _ { _ { k l } } + 3 \cdot 2 \sum _ { K , L } f _ { K } ^ { J } A _ { L } ^ { K } f ^ { L } \sum _ { k , l } \alpha _ { _ { J k } } \gamma _ { k l } } } \\ { { \displaystyle \qquad + 3 \cdot 2 \sum _ { K , L } A _ { K } ^ { J } f _ { L } ^ { K } f ^ { L } \sum _ { k , l } \gamma _ { _ { J k } } \alpha _ { _ { k l } } + 3 \cdot 2 \sum _ { K , L } A _ { K } ^ { J } A _ { L } ^ { K } f ^ { L } \sum _ { k , l } \gamma _ { _ { J k } } \gamma _ { _ { k l } } } } & { { ( 7 . 3 1 \sqrt { \frac { J } { \alpha _ { K } } } ) ^ { 2 } } } \end{array}
$$

and the order conditions for order three become

$$
\begin{array} { r l } & { \sum _ { b _ { 2 } = 1 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } = 1 / 2 } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } = 0 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 3 } \in \mathcal { S } _ { k } \in \mathcal { R } _ { f } = 1 / 3 } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \in \mathcal { K } _ { k } = 1 / 6 } } \\ & { \sum _ { b _ { 3 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 3 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 2 } } } \\ & { \sum _ { b _ { 3 } \in \mathcal { T } _ { k } \cap \mathcal { K } _ { k } = 0 } ^ { b _ { 4 } } } \\ & { \sum _ { b _ { 2 } \in \mathcal { S } _ { k } \cap \mathcal { K } _ { k } = 0 . } } \end{array}
$$

For a graphical representation of the elementary differentials in (7.31;q) and of the order conditions (7.32) we need trees with two different kinds of vertices (one representing $f$ and the other $A$ ). As in Sect.II.15 we use “meagre” and “fat’ vertices (see Definitions I.15.1 to I.15.4). Not all trees with meagre and fat vertices ( $. P \mathrm { - }$ trees) have to be considered. From the above derivation we see that fat vertices have to be singly-branched (derivatives of the constant matrix $A$ are zero) and that they cannot be at the end of a branch. We therefore use the notation

$$
\begin{array} { r l } & { T W = \left\{ \begin{array} { l l } { P \mathrm { - t r e e s } ; \mathrm { ~ e n d \mathrm { - v e r t i c e s } ~ a r e ~ m e a g r e ~ a n d } } \\ { \mathrm { ~ f a t ~ v e r t i c e s ~ a r e ~ s i n g l y \mathrm { - } b r a n c h e d } \ } } \end{array} } \end{\right\array} \end{array}
$$

and if the vertices are labelled monotonically, we write $L T W$

Definition 7.5. The elementary differentials for trees $t \in T W$ are defined recursively by $F ^ { J } ( \tau ) ( y ) = f ^ { J } ( y )$ and

$$
F ^ { J } ( t ) ( y ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { K _ { 1 } , \ldots , K _ { m } } f _ { K _ { 1 } , \ldots , K _ { m } } ^ { J } ( y ) \cdot \left( F ^ { K _ { 1 } } ( t _ { 1 } ) ( y ) , \ldots , F ^ { K _ { m } } ( t _ { m } ) ( y ) \right) } & \\ { \quad } & { \mathrm { i f } t = \medspace _ { a } [ t _ { 1 } , \ldots , t _ { m } ] \quad \mathrm { ( m e a g r e ~ r o o t ) } } \\ { \displaystyle \sum _ { K } A _ { K } ^ { J } \cdot F ^ { K } ( t _ { 1 } ) ( y ) } & { \mathrm { i f } t = \medskip _ { b } [ t _ { 1 } ] \quad \mathrm { ( f a t ~ r o o t ) } . } \end{array} \right.
$$

Definition 7.6. For $t \in T W$ we let $\Phi _ { j } ( \tau ) = 1$ and

$$
\Phi _ { \ j } ( t ) = \left\{ \begin{array} { l l } { { \displaystyle \sum _ { k _ { 1 } , \ldots , k _ { m } } \alpha _ { \ j  k _ { 1 } } \ldots \alpha _ { \ j k _ { m } } \Phi _ { k _ { 1 } } ( t _ { 1 } ) \ldots \Phi _ { k _ { m } } ( t _ { m } ) } } & { { \mathrm { ~ i f ~ } t = \int _ { a } [ t _ { 1 } , \ldots , t _ { m } ] \ldots \Phi _ { k _ { m } } ( t _ { m } ) \mathrm { ~ d ~ } } } \\ { { \displaystyle \sum _ { k } \gamma _ { \jmath k } \Phi _ { k } ( t _ { 1 } ) } } & { { \mathrm { ~ i f ~ } t = \phantom { \left( \sum _ { k _ 1 } \right) } \mathrm { d } } } \end{array} \right.
$$

We remark that $T$ (the set of trees as considered for Runge-Kutta methods) is a subset of TW and that the above definitions coincide with Definitions II.2.3 and I1.2.9 (c.f. also Formulas (I1.2.18) and (II.2.19)). The general result is now the following

Theorem 7.7. A W -method (7.4) with $J = A$ arbitrary is of order $p$ iff

$$
\begin{array} { r l r } & { \displaystyle \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) = \frac { 1 } { \gamma ( t ) } \qquad } & { f o r t \in T \ w i t h \ \varrho ( t ) \le p , \ a n d } \\ & { \displaystyle \sum _ { \jmath } b _ { \jmath } \Phi _ { \jmath } ( t ) = 0 \qquad } & { f o r t \in T { \cal W } \setminus T \ w i t h \ \varrho ( t ) \le p . } \end{array}
$$

The proof is essentially the same as for Theorems 7.3 and 7.4.

Table 7.3. Number of order conditions for W-methods   

<table><tr><td>order p</td><td>12345 6 7 8</td></tr><tr><td>no. of conditions</td><td>3 21 58 166 498 1540</td></tr></table>

The number of order conditions for $W$ -methods is rather large (see Table 7.3), since each tree of $T$ with $\kappa$ singly-branched vertices gives rise to $2 ^ { \kappa }$ order conditions (in the case of symmetry some may be identical). Therefore, $W$ -methods of higher order are best obtained by extrapolation (see Sect. IV.9).

The stability investigation for linearly implicit methods with $A \neq f ^ { \prime } ( y _ { 0 } )$ is very complicated. If we linearize the differential equation (as in the beginning of Sect.IV.2) and assume the Jacobian to be constant,we arrive at a recursion of the form

$$
y _ { 1 } = R ( h f ^ { \prime } ( y _ { 0 } ) , h A ) y _ { 0 } .
$$

Since, in general, the matrices $f ^ { \prime } ( y _ { 0 } )$ and $A$ cannot be diagonalized simultaneously, the consideration of scalar test equations is not justified. Stability investigations for the case when $\left\| f ^ { \prime } ( y _ { 0 } ) - A \right\|$ is small will be considered in Sect.IV.11.

# Exercises

1. (Kaps 1977). There exists no Rosenbrock method (7.4) with $s \approx 4$ and $p = 5$ Prove this.

2.(Ngrsett & Wolfbrandt 1979). Generalize the derivation of order conditions for Runge-Kutta methods with the help of B-series (Sect.II.11, page 247) to Rosenbrock methods.

Hint. Prove that, foraB-series $B ( \mathbf { a } , y _ { 0 } )$ with $\mathbf { a } : T \longrightarrow \mathbb { R }$ satisfying $\mathbf { a } ( \emptyset ) = 0$

$$
h f ^ { \prime } ( y _ { 0 } ) B ( \mathbf { a } , y _ { 0 } ) = B ( \widehat { \mathbf { a } } , y _ { 0 } )
$$

is again a B-series with coefficients

$$
\widehat { \mathbf { a } } ( t ) = \left\{ \begin{array} { l l } { \varrho ( t ) \mathbf { a } ( t _ { 1 } ) } & { \mathrm { i f } t = [ t _ { 1 } ] } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right.
$$

3. Cooper & Sayfy (1983) consider additive Runge-Kut methods

$$
\begin{array} { l l } { { g _ { \scriptscriptstyle 4 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \alpha _ { \scriptscriptstyle 4 \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } ) + h J \displaystyle \sum _ { \jmath = 1 } ^ { \imath } \eta _ { \scriptscriptstyle 4 \jmath } g _ { \jmath } ~ } } & { { i = 1 , \ldots , s + 1 } } \\ { { { } } } & { { { } } } \\ { { y _ { 1 } = g _ { s + 1 } ~ } } & { { { ( 7 . 3 - 1 ) } } } \end{array}
$$

wlose cofciertsi $\begin{array} { r } { \sum _ { j = 1 } ^ { \imath - 1 } \alpha _ { i j } = c _ { i } , \sum _ { j = 1 } ^ { \imath } \eta _ { \imath j } = 0 . } \end{array}$

a) Prove that (7.34) is equivalent to (7.4) whenever $\alpha _ { s + 1 , i } = b _ { i }$ and

$$
\left( \eta _ { \iota _ { 2 } } \right) \left( \alpha _ { i j } \right) = \left( \alpha _ { i j } \right) \left( \gamma _ { i j } \right) .
$$

Here all matrices are of dimension $( s + 1 ) \times ( s + 1 )$ . The last line of $( \gamma _ { i j } )$ need not be specified since the last column of $\left( \alpha _ { \iota j } \right)$ is zero.

b) If the coefficients of (7.34) satisfy $\alpha _ { i , i - 1 } \neq 0$ for all $i$ , then we can always find an equivalent method of type (7.4).

4.(Verwer 1980,Verwer & Scholz 1983)． Derive order conditions for Rosenbrock methods “with time-lagged Jacobian”,i.e., methods of type (7.4) where $J$ is assumed to be $f ^ { \prime } ( y ( x _ { 0 } - \omega h ) )$ . If $\omega$ is the step ratio $h _ { o l d } / h$ ,this allows re-use of the Jacobian of the previous step.

5.(Kaps & Ostermann 1989). Show that some order conditions of (7.32) can be shifted to higher orders if it is assumed that

$$
f ^ { \prime } ( y _ { 0 } ) - J = { \mathcal { O } } ( h ) .
$$

This makes the conditions of Exercise 4 independent of $\omega$ ·

Result. The number of order-shifts is equal to the number of fat nodes

# IV.8 Implementation of Implicit Runge-Kutta Methods

These have not been used to any great extent ..

(S.P. Ngrsett 1976)

However, the implementation difficulties of these methods have precluded their general use; ... (J.M. Varah 1979)

Although Runge-Kutta methods present an attractive alternative, especially for stiff problems，... it is generally believed that they will never be competitive with multistep methods.

(K. Burrage, J.C. Butcher & FH. Chipman 1980)

Runge-Kutta methods for stiff problems, we are just beginning to explore them ... (L. Shampine in Aiken 1985)

If the dimension of the differential equation $y \prime = f ( x , y )$ is $n$ ， then the s-stage fully implicit Runge-Kutta method (3.1） involves a $n \cdot s$ -dimensional nonlinear system for the unknowns $g _ { 1 } , \dots , g _ { s }$ . An efficient solution of this system is the main problem in the implementation of an implicit Runge-Kutta method.

Among the methods discussed in Sect.IV.5, the processes Radau IIA of Ehle, which are $L$ -stable and of high order, seem to be particularly promising. Most of the questions arising (starting values and stopping criteria for the simplified Newton iterations, efficient solution of the linear systems,and the selection of the step sizes) are discussed here for the particular Ehle method with $s \approx 3$ and $p = 5$ . This then constitutes a description of the code RADAU5 of the appendix. An adaptation of the described techniques to other fully implicit Runge-Kutta methods is more or less straight-forward, if the Runge-Kutta matrix has at least one real eigenvalue. We also describe briefly our implementation of the diagonal implicit method SDIRK4 (Formula (6.16)).

# Reformulation of the Nonlinear System

In order to reduce the influence of round-off errors we prefer to work with the smaller quantities

$$
z _ { \imath } = g _ { \imath } - y _ { 0 } .
$$

Then (3.1a) becomes

$$
z _ { \imath } = h \sum _ { \jmath = 1 } ^ { \ast } a _ { \imath _ { \jmath } } f ( x _ { 0 } + c _ { \jmath } h , y _ { 0 } + z _ { \jmath } ) \qquad i = 1 , \dots , s .
$$

Whenever the solution $z _ { 1 } , \dots , z _ { s }$ of the system (8.2a) is known, then (3.1b) is an explicit formula for $y _ { 1 }$ .A direct application of this requires s additional function evaluations. These can be avoided, if the matrix $A = \left( a _ { \imath j } \right)$ of the Runge-Kutta

coefficients is nonsingular. Indeed,(8.2a) can be written as

$$
\binom { z _ { 1 } } { \vdots } = A \left( \begin{array} { c } { { h f ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } } \\ { { \vdots } } \\ { { h f ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } } \end{array} \right) ,
$$

so that (3.1b) is seen to be equivalent to

$$
y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { s } d _ { \imath } z _ { \imath }
$$

where

$$
( d _ { 1 } , \dotsc , d _ { s } ) = ( b _ { 1 } , \dotsc , b _ { s } ) A ^ { - 1 } .
$$

For the 3-stage Radau IIA method(Table 5.6) the vector $d$ is simply $( 0 , 0 , 1 )$ ,since $b _ { \imath } = a _ { s \imath }$ for all $i$ .

Another advantageofFormula (8.2b)is the following: thequantities $z _ { 1 } , \dots , z _ { s }$ are computed iteratively and are therefore affected by iteration errors. The evaluation of $f ( x _ { 0 } + c _ { \iota } h , y _ { 0 } + z _ { \iota } )$ in Eq.(3.1b) would then, due to the large Lipschitz constant of $f$ ,amplify these errors, which then “can be disastrously inaccurate for a stiff problem" (L.F. Shampine 1980).

# Simplified Newton Iterations

For a general nonlinear differential equation the system (8.2a) has to be solved iteratively. In the stone-age of stiff computation (i.e., before 1967) people were usually thinking of simple fixed-point iteration. But this transforms the algorithm into an explicit method and destroys the good stability properties. The paper of Liniger & Willoughby (197O) then showed the advantages of using Newton's method for this purpose. Newton's method applied to system (8.2a) needs for each iteration the solution of a linear system with matrix

$$
\left( \begin{array} { c c c } { I - h a _ { 1 1 } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } & { \dots } & { - h a _ { 1 s } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } \\ { \vdots } & { } & { \vdots } \\ { - h a _ { s 1 } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ) } & { \dots } & { I - h a _ { s s } \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ) } \end{array} \right) .
$$

$\begin{array} { r } { \frac { \partial f } { \partial y } ( x _ { 0 } + c _ { \iota } h , y _ { 0 } + z _ { \iota } ) } \end{array}$ by an

$$
J \approx { \frac { \partial f } { \partial y } } ( x _ { 0 } , y _ { 0 } ) .
$$

Then the simplified Newton iterations for (8.2a) become

$$
\begin{array} { c } { { ( I - h A \otimes J ) \Delta Z ^ { k } = - Z ^ { k } + h ( A \otimes I ) F ( Z ^ { k } ) } } \\ { { Z ^ { k + 1 } = Z ^ { k } + \Delta Z ^ { k } . } } \end{array}
$$

Here $Z ^ { k } = ( z _ { 1 } ^ { k } , \dots , z _ { s } ^ { k } ) ^ { T }$ is the $k$ -th approximation tothesolution,and $\Delta Z ^ { k } =$ $( \Delta z _ { 1 } ^ { k } , \ldots , \ \Delta z _ { s } ^ { k } ) ^ { T }$ are the increments. $F ( Z ^ { k } )$ is an abbreviation for

$$
F ( Z ^ { k } ) = \left( f ( x _ { 0 } + c _ { 1 } h , y _ { 0 } + z _ { 1 } ^ { k } ) , \dots , f ( x _ { 0 } + c _ { s } h , y _ { 0 } + z _ { s } ^ { k } ) \right) ^ { T } .
$$

Each iteration requires $s$ evaluations of $f$ and the solution of a $n \cdot s$ -dimensional linear system. The matrix $\left( I - h A \otimes J \right)$ is the same for all iterations. Its LUdecomposition is done only once and is usually very costly.

Starting Values for the Newton Iteration. A natural and simple choice for the starting values in the iteration (8.4) (or equivalently (8.13) below), since the exact solution of (8.2a) satisfies $z _ { \imath } = \mathcal { O } ( h )$ ,would be

$$
z _ { \ i } ^ { 0 } = 0 , \qquad i = 1 , \ldots , s .
$$

However, better choices are possible in general. If the implicit Runge-Kutta method satisfies the condition $C ( \eta )$ (see Sections IV.5 and II.7) for some $\eta \leq s$ ,then

$$
z _ { \imath } = y ( x _ { 0 } + c _ { \imath } h ) - y _ { 0 } + \mathcal { O } ( h ^ { \eta + 1 } ) .
$$

Suppose now that $c _ { \iota } \neq 0 \ ( i = 1 , \ldots , s )$ and consider the interpolation polynomial of degree $s$ , defined by

$$
q ( 0 ) = 0 , \qquad q ( c _ { \ i } ) = z _ { \ i } \qquad i = 1 , \ldots , s .
$$

Since the interpolation error is of size $\mathcal { O } ( h ^ { s + 1 } )$ we obtain together with (8.6)

$$
y ( x _ { 0 } + t h ) - y _ { 0 } - q ( t ) = \mathcal { O } ( h ^ { \eta + 1 } )
$$

(cf. Theorem 7.10 of Chapter $\amalg$ for collocation methods)． We use the values of $q ( t )$ also beyond the interval $[ 0 , 1 ]$ and take

$$
z _ { \imath } ^ { 0 } = q ( 1 + w c _ { \imath } ) + y _ { 0 } - y _ { 1 } , \quad i = 1 , \ldots , s , \quad w = h _ { n e w } / h _ { o l d }
$$

as starting values for the Newton iteration in the subsequent step. Numerical experiments with the 3-stage Radau IIA method have shown that (8.5') usually leads to a faster convergence than (8.5).

Stopping Criterion. This question is closely related to an estimation of the iteration error. Since convergence is linear, we have

$$
\begin{array} { r } { \| \Delta Z ^ { k + 1 } \| \leq \Theta \| \Delta Z ^ { k } \| , \quad \mathrm { \ h o p e f u l l y ~ w i t h ~ } \quad \Theta < 1 . } \end{array}
$$

Applying the triangle inequality to

$$
Z ^ { k + 1 } - Z ^ { * } = ( Z ^ { k + 1 } - Z ^ { k + 2 } ) + ( Z ^ { k + 2 } - Z ^ { k + 3 } ) + . . .
$$

(where $Z ^ { \ast }$ is the exact solution of (8.2a)) yields the estimate

$$
\| Z ^ { k + 1 } - Z ^ { * } \| \leq \frac { \Theta } { 1 - \Theta } \| \Delta Z ^ { k } \| .
$$

The convergence rate $\Theta$ can be estimated by the computed quantities

$$
\begin{array} { r } { \Theta _ { k } = \| \Delta Z ^ { k } \| / \| \Delta Z ^ { k - 1 } \| , \qquad k \geq 1 . } \end{array}
$$

It is clear that the iteration error should not be larger than the local discretization error, which is usually kept close to $T o l$ . We therefore stop the iteration when

$$
\eta _ { k } \| \Delta Z ^ { k } \| \le \kappa \cdot T o l \quad \mathrm { w i t h } \quad \eta _ { k } = \frac { \Theta _ { k } } { 1 - \Theta _ { k } }
$$

and accept $Z ^ { k + 1 }$ as approximation to $Z ^ { * }$ . This strategy can only be applied after at least two iterations. In order to be able to stop the computations after the first iteration already (which is especially advantageous for linear systems) we take for $k = 0$ the quantity

$$
\eta _ { 0 } = \left( \operatorname* { m a x } ( \eta _ { o l d } , U r o u n d ) \right) ^ { 0 . 8 }
$$

where $\eta _ { o l d }$ is the last $\eta _ { k }$ of the preceding step. It remains to make a good choice for the parameter $\kappa$ in (8.10). To this end we applied the code RADAU5 for many different values of $\kappa$ between 10 and $1 0 ^ { - 4 }$ and with some different tolerances Tol to several differential equations. The observation was that the code works most efficiently for values of $\kappa$ around $1 0 ^ { - 1 }$ or $1 0 ^ { - 2 }$

It is our experience that the code becomes more efficient when we allow a relatively high number of iterations (eg., $k _ { m a x } = 7$ or 10). During these $k _ { m a x }$ iterations, the computations are interrupted and restarted with a smaller stepsize (for example with $h : = h / 2 )$ if one of the following situations occurs a) there is a $k$ with $\Theta _ { k } \ge 1$ (the iteration “diverges"); b) for some $k$ ，

$$
\frac { \Theta _ { k } ^ { k _ { m a x } - k } } { 1 - \Theta _ { k } } \| \Delta Z ^ { k } \| > \kappa \cdot T o l .
$$

The left-hand expression in (8.11) is a rough estimate of the iteration error to be expected after $k _ { m a x } - 1$ iterations.The norm,used in all these formulas,should be the same as the one used for the local error estimator.

If only one Newton iteration was necessary to satisfy (8.1O) or if the last $\Theta _ { k }$ was very small, say $\leq 1 0 ^ { - 3 }$ ， then we don't recompute the Jacobian in the next step. As a consequence, the Jacobian is computed only once for linear problems with constant coeffcients (as long as no step rejection occurs).

# The Linear System

An essential gain of numerical work for the solution of the linear system (8.4) is obtained by the following method, introduced independently by Butcher (1976) and Bickart (1977),which exploits with much profit the special structure of the matrix $I - h A \otimes J$ in (8.4).

The idea is to premultiply (8.4) by $( h A ) ^ { - 1 } \otimes I$ (we suppose here that $A$ is invertible) and to transform $A ^ { - 1 }$ to a simple matrix (diagonal, block diagonal, triangular or Jordan canonical form)

$$
{ \cal T } ^ { - 1 } A ^ { - 1 } { \cal T } = \Lambda .
$$

With the transformed variables $W ^ { k } = ( T ^ { - 1 } \otimes I ) Z ^ { k }$ , the iteration (8.4) becomes equivalent to

$$
\begin{array} { c } { { ( h ^ { - 1 } \Lambda \otimes I - I \otimes J ) \Delta W ^ { k } = - h ^ { - 1 } ( \Lambda \otimes I ) W ^ { k } + ( T ^ { - 1 } \otimes I ) F ( ( T \otimes I ) W ^ { k } ) } } \\ { { W ^ { k + 1 } = W ^ { k } + \Delta W ^ { k } . } } \end{array}
$$

We also replace $Z ^ { k }$ and $\Delta Z ^ { k }$ by $W ^ { k }$ and $\Delta W ^ { k }$ in the formulas (8.7)-(8.11) (and thereby again save some work).

For the sequel, we suppose that the matrix $A ^ { - 1 }$ has one real eigenvalue $\widehat { \gamma }$ and one complex conjugate eigenvalue pair ${ \widehat { \alpha } } \pm i { \widehat { \beta } }$ . This is a typical situation for 3-stage implicit Runge-Kutta methods such as Radau IA. With $\gamma = h ^ { - 1 } \widehat { \gamma }$ ， $\alpha =$ $h ^ { - 1 } \widehat { \alpha } , \beta = h ^ { - 1 } \widehat { \beta }$ the matrix in (8.13) becomes

$$
\left( \begin{array} { c c c } { { \gamma I - J } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { \alpha I - J } } & { { - \beta I } } \\ { { 0 } } & { { \beta I } } & { { \alpha I - J } } \end{array} \right)
$$

so that (8.13) splits into two linear systems of dimension $n$ and $2 n$ , respectively. Several ideas are possible to exploit the special structure of the $2 n \times 2 n$ -submatrix. The easiest and numerically most stable way has turned out to be the following: transform the real subsystem of dimension $2 n$ into an $n$ -dimensional, complex system

$$
\big ( ( \alpha + i \beta ) I - J \big ) ( u + i v ) = a + i b
$$

and apply simple Gaussan elimination. For machines without complex arithmetic, one just has to modify the linear algebra routines. Then a complex multiplication consists of 4 real multiplications and the amount of work for the solution of (8.14') becomes approximately $4 n ^ { 3 } / 3$ operations. Thus the total work for system (8.14) is about $5 n ^ { 3 } / 3$ operations. Compared to $( 3 n ) ^ { 3 } / 3$ , which would be the number of operations necessary for decomposing the untransformed matrix $I - h A \otimes J$ in (8.4), we gain a factor of about 5 in arithmetical operations. Observe that the transformations, such as $Z ^ { k } = ( T \otimes I ) W ^ { k }$ ， need only $\mathcal { O } ( n )$ additions and multiplications. The gain is still more drastic for methods with more than 3 stages.

Transformation to Hessenberg Form. For large systems with a full Jacobian $J$ a further gain is possible by transforming $J$ to Hessenberg form

$$
S ^ { - 1 } J S = H = \left( \begin{array} { l l l l } { { \ast } } & { { \cdot \cdot } } & { { \ast } } & { { \ast } } \\ { { \ast } } & { { } } & { { } } & { { \ast } } \\ { { } } & { { \cdot _ { \cdot } } } & { { } } & { { \vdots } } \\ { { } } & { { } } & { { \ast } } & { { \ast } } \end{array} \right) .
$$

This procedure was originally proposed for multistep methods by Enright (1978) and extended to the Runge-Kutta case by Varah (1979). With the code ELMHES, taken from LINPACK, this is performed with $2 n ^ { 3 } / 3$ operations. Because the multiplication of $S$ with a vector needs only $n ^ { 2 } / 2$ operations (observe that $S$ is triangular) the solution of (8.13) is found in $\mathcal { O } ( n ^ { 2 } )$ operations, if the Hessenberg matrix $H$ is known. This transformation is especially advantageous, if the Jacobian $J$ is not changed during several steps.

# Step Size Selection

One possibility to select the step sizes is Richardson extrapolation (cf. Sect.II.4). We describe here the use of an embedded pair of methods which is easier to pro-gram and which makes the code more flexible. The following formulas are for the special case of the 3-stage Radau IIA methods; the same ideas are applicable to all implicit Runge-Kutta methods, whose Runge-Kutta matrix has at least one real eigenvalue.

Embedded Formula. Since our method is of optimal order, it is impossible to embed it efficiently into one of still higher order. Therefore we search for a lower order method of the form

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \left( \widehat { b } _ { 0 } f ( x _ { 0 } , y _ { 0 } ) + \sum _ { \iota = 1 } ^ { 3 } \widehat { b } _ { \iota } f ( x _ { 0 } + c _ { \iota } h , g _ { \iota } ) \right)
$$

where $g _ { 1 } , g _ { 2 } , g _ { 3 }$ are the values obtained from the Radau IIA method and $\widehat { b } _ { 0 } \not = 0$ (the choice $\widehat { b } _ { 0 } = \gamma _ { 0 } = \widehat { \gamma } ^ { - 1 }$ ，where $\widehat { \gamma }$ is the real eigenvalue of the matrix $A ^ { - 1 }$ ， again saves some multiplications). The difference

$$
{ \widehat { y } } _ { 1 } - y _ { 1 } = \gamma _ { 0 } h f ( x _ { 0 } , y _ { 0 } ) + \sum _ { i = 1 } ^ { 3 } ( { \widehat { b } } _ { \imath } - b _ { \imath } ) h f ( x _ { 0 } + c _ { \imath } h , g _ { i } ) ,
$$

which can also be written in the form

$$
\begin{array} { r } { \widehat { y } _ { 1 } - y _ { 1 } = \gamma _ { 0 } h f ( x _ { 0 } , y _ { 0 } ) + e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } , } \end{array}
$$

then serves for error estimation. In order that $\widehat { y } _ { 1 } - y _ { 1 } = \mathcal { O } ( h ^ { 4 } )$ the coefficients have to satisfy

$$
\displaystyle { \big ( e _ { 1 } , e _ { 2 } , e _ { 3 } \big ) = \frac { \gamma _ { 0 } } { 3 } ( - 1 3 - 7 \sqrt { 6 } , - 1 3 + 7 \sqrt { 6 } , - 1 ) } .
$$

Unfortunately, for $y ^ { \prime } = \lambda y$ and $h \lambda  \infty$ the difference (8.17) behaves like $\widehat { y } _ { 1 } -$ $y _ { 1 } \approx \gamma _ { 0 } h \lambda y _ { 0 }$ ，which is unbounded and therefore not suitable for stiff equations. We propose (an idea of Shampine) to use instead

$$
e r r = ( I - h \gamma _ { 0 } J ) ^ { - 1 } ( \widehat { y } _ { 1 } - y _ { 1 } ) .
$$

The LU-decomposition of $\left( ( h \gamma _ { 0 } ) ^ { - 1 } I - J \right)$ is available anyway from the previous work, so that the computation of (8.19) is cheap. For $h  0$ we still have $e r r =$ $\mathcal { O } ( h ^ { 4 } )$ ,and for $h \lambda  \infty$ (if $y ^ { \prime } = \lambda y$ and $J = \lambda$ ) we obtain $e r r  - 1$

This behaviour (for $h \lambda  \infty )$ ） is already much beter than that for $\widehat { y } _ { 1 } - y _ { 1 }$ ， but it is not good enough in order to avoid the “hump” phenomenon, described in Sect.IV.7. In the first step and after every rejected step for which $\left\| e r r \right\| > 1$ ，we therefore use instead of (8.19) the expression

$$
\widetilde { e r r } = ( I - h \gamma _ { 0 } J ) ^ { - 1 } \big ( \gamma _ { 0 } h f \big ( x _ { 0 } , y _ { 0 } + e r r \big ) + e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } \big )
$$


<!-- chunk 0003: pages 141-210 -->
for step size prediction. This requires one additional function evaluation, but satisfies $\widetilde { e r r }  0$ for $h \lambda  \infty$ ,as does the error of the numerical solution.

Standard Step Size Controller. Since the expressions (8.19) and (8.2O) behave like $\mathcal { O } ( h ^ { 4 } )$ for $h  0$ , the standard step size prediction leads to

$$
h _ { \mathrm { n e w } } = f a c \cdot h _ { \mathrm { o l d } } \cdot \lvert \lvert e r r \rvert \rvert ^ { - 1 / 4 } .
$$

where

$$
\left| \left| e r r \right| \right| = \sqrt { \frac { 1 } { n } \sum _ { \ i = 1 } ^ { n } \Bigl ( \frac { e r r _ { i } } { s c _ { \ i } } \Bigr ) ^ { 2 } } ,
$$

and $s c _ { \ i } = A t o l _ { \ i } + \operatorname* { m a x } ( | y _ { 0 \ i } | , | y _ { 1 \ i } | ) \cdot R t o l _ { \ i }$ as in (4.11) of Sect.II.4. Here, the safety factor fac is proposed to depend on $N e w t$ , the number of Newton iterations of the current step and on the maximal number of Newton iterations $k _ { \mathrm { m a x } }$ ,say, as: $f a c = 0 . 9 \times ( 2 k _ { \operatorname* { m a x } } + 1 ) / ( 2 k _ { \operatorname* { m a x } } + N e w t ) .$

In order to save LU-decompositions of the matrix (8.14),we also include the following strategy: if no Jacobian is recomputed and if the step size $h _ { \mathrm { n e w } }$ , defined by (8.21), satisfies

$$
c _ { 1 } h _ { \mathrm { o l d } } \leq h _ { \mathrm { n e w } } \leq c _ { 2 } h _ { \mathrm { o l d } }
$$

with, say $c _ { 1 } = 1 . 0$ and $c _ { 2 } = 1 . 2$ , then we retain $h _ { \mathrm { o l d } }$ for the following step.

Predictive Controller The step size prediction by formula (8.21) has the disadvan-tage that step size reductions by more than the factor fac are not possible without step rejections (observe that $h _ { \mathrm { n e w } } < f a c \cdot h _ { \mathrm { o l d } }$ implies $\left\| e r r \right\| > 1 )$ . For stiff differential equations, however, a rapid decrease of the step size is often required (see for example the situation of Fig.8.1, where the step size drops from $1 0 ^ { - 2 }$ to $1 0 ^ { - 7 }$ within a very small time interval). Denoting by $e r r _ { n + 1 }$ the error expression (8.19) (or (8.20))，, computed in the $\mathscr { n }$ th step with step size $h _ { n }$ ， step size predictions are typically derived from the asymptotic formula

$$
\| e r r _ { n + 1 } \| = C _ { n } h _ { n } ^ { 4 } .
$$

The strategy (8.21) is based on the additional assumption $C _ { n + 1 } \approx C _ { n }$ ， which, as we have seen, is not always very realistic.

A careful control-theoretic study of step size strategies has been undertaken by Gustafsson (1994). He came to the conclusion that a better model is to assume that $\log C _ { n }$ is a linear function of $\mathscr { n }$ . This means that $\log C _ { n + 1 } - \log C _ { n }$ is constant or, equivalently,

$$
C _ { n + 1 } / C _ { n } \approx C _ { n } / C _ { n - 1 } .
$$

Inserting $C _ { n }$ and $C _ { n - 1 }$ from (8.23) and $C _ { n + 1 }$ from $1 = C _ { n + 1 } h _ { \mathrm { n e w } } ^ { 4 }$ into (8.24) yields

$$
h _ { \mathrm { n e w } } = f a c \cdot h _ { n } \bigg ( \frac { 1 } { \| e r r _ { n + 1 } \| } \bigg ) ^ { 1 / 4 } \cdot \frac { h _ { n } } { h _ { n - 1 } } \bigg ( \frac { \| e r r _ { n } \| } { \| e r r _ { n + 1 } \| } \bigg ) ^ { 1 / 4 } .
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/a34acc3688c9c236807cdc429aaec0e6d70a277e063eab770d1be544ea4411b3.jpg)  
Fig.8.1. Solution, step sizes and Newton iterations for RADAU5

In our code RADAU5 we take the minimum of the two step sizes (8.21) and (8.25). For the problem considered in Fig.8.1, this new strategy reduces the number of rejected steps from 27 to 7.

Numerical Study of the Step-Control Mechanism. As a representative example we choose the van der Pol equation $( 1 . 5 )$ with $\varepsilon = 1 0 ^ { - 6 }$ , initial values $y _ { 1 } ( 0 ) = 2$ ， $y _ { 2 } ( 0 ) = - 0 . 6$ and integration interval $0 \leq x \leq 2$ . Fig.8.1 shows four pictures. The first one presents the solution $y _ { 1 } ( x )$ with all accepted integration steps for $A t o l = R t o l = 1 0 ^ { - 4 }$ . Below this, the step sizes obtained by RADAU5 are plotted as function of $_ x$ . The solid line represents the accepted steps. The rejected steps are indicated by $\times \mathit { \textbf { s } }$ . Observe the very small step sizes which are required in the rapid transients between the smooth parts of the solution. The lowest two pictures give the number of Newton iterations needed for solving the nonlinear system (8.2a), once as function of $_ x$ ，and once as function of the step-number. The last picture also indicates the steps where the Jacobian has been recomputed.

Another numerical experiment (Fig.8.2) illustrates the quality of the error es-timates. We applied the code RADAU5 with $A t o l = R t o l = 1 0 ^ { - 4 }$ and initial step size $h = 1 0 ^ { - 4 }$ to the above problem and plotted at several chosen points of the numerical solution

a） the exact local error (marked by small circles) b) the estimates (8.19) and (8.20) (marked by $\phi$ and X respectively)

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/c1288d1775b4a9653e848870d6ad471e07218049aae9f0e7cb2dc0c334c0e37d.jpg)  
Fig.8.2. Exact local error and the estimates (8.19) and (8.20)

as functions of $h$ . The large symbols indicate the position of the actually used step size. Newt is the number of required Newton iterations.

It is interesting to note that the local error behaves like $\mathcal { O } ( h ^ { 6 } )$ (straight line of slope 6) only for $h \leq \varepsilon$ and for large $h$ . Between these regions, the local error grows like $\mathcal { O } ( h ^ { - 1 } )$ with decreasing $h$ . This is the only region where the error estimate (8.20) is significantly better than (8.19). Therefore,we use the more expensive estimator (8.2O) only in the first and after each rejected step. In any way,both error estimators are always above the actual local error, so that the code usually produces very precise results.

# Implicit Differential Equations

Many applications (such as space discretizations of parabolic differential equations) often lead to systems of the form

$$
M y ^ { \prime } = f ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 }
$$

with a constant matrix $M$ . For such problems we formally replace all $f$ 's by $M ^ { - 1 } f$ and multiply the resulting equations by $M$ .Formulas (8.13) and (8.19) then have to be replaced by

$$
\left( h ^ { - 1 } \Lambda \otimes M - I \otimes J \right) \Delta W ^ { k } = - h ^ { - 1 } \left( \Lambda \otimes M \right) W ^ { k } + ( T ^ { - 1 } \otimes I ) F ( ( T \otimes I ) W ^ { k } )
$$

$$
e r r = \left( ( h \gamma _ { 0 } ) ^ { - 1 } M - J \right) ^ { - 1 } \left( f ( x _ { 0 } , y _ { 0 } ) + ( h \gamma _ { 0 } ) ^ { - 1 } M ( e _ { 1 } z _ { 1 } + e _ { 2 } z _ { 2 } + e _ { 3 } z _ { 3 } ) \right) .
$$

Here the matrix $J$ is again an approximation to $\partial f / \partial y$ . These formulas may even be applied to certain problems (8.26) with singular $M$ (for more details see Chapters VI and VII).

Solving the linear system (8.13a) is done by a decomposition of the matrix (see (8.14), (8.14'))

$$
\left( \begin{array} { c c } { { \gamma M - J } } & { { 0 } } \\ { { 0 } } & { { ( \alpha + i \beta ) M - J } } \end{array} \right) .
$$

If $M$ and $J$ are banded or sparse, the matrices $\gamma M - J$ and $( \alpha + \imath \beta ) M - J$ remain banded or sparse, respectively. The code RADAU5 of the appendix has options for banded structures.

# An SDIRK-Code

We have also coded,using many of the above ideas,the SDIRK formula (6.16) together with the global solution (6.17). For this method also, it was again very important to replace the error estimator $y _ { 1 } - { \widehat { y } } _ { 1 }$ by (8.19).

Here, in contrast to fully implicit Runge-Kutta methods, one can treat the stages one after the other. Such a serial computation has the advantage that the information of the already computed stages can be used for a good choice of the starting values for the Newton iterations in the subsequent stages. For example, suppose that

$$
\begin{array} { l } { z _ { 1 } = \gamma h f ( x _ { 0 } + \gamma h , y _ { 0 } + z _ { 1 } ) } \\ { z _ { 2 } = \gamma h f ( x _ { 0 } + c _ { 2 } h , y _ { 0 } + z _ { 2 } ) + a _ { 2 1 } h f ( x _ { 0 } + \gamma h , y _ { 0 } + z _ { 1 } ) } \end{array}
$$

are already available. Since for all $i$

$$
z _ { i } = c _ { i } h f ( x _ { 0 } , y _ { 0 } ) + ( \sum _ { \jmath } a _ { i \jmath } c _ { j } ) h ^ { 2 } ( f _ { x } + f _ { y } f ) ( x _ { 0 } , y _ { 0 } ) + \mathcal { O } ( h ^ { 3 } ) ,
$$

by solving

$$
\left( { \begin{array} { c c } { c _ { 1 } } & { c _ { 2 } } \\ { \sum _ { j } a _ { 1 j } c _ { j } } & { \sum _ { j } a _ { 2 j } c _ { j } } \end{array} } \right) { \binom { \alpha _ { 1 } } { \alpha _ { 2 } } } = \left( { \begin{array} { c c } { c _ { 3 } } \\ { \sum _ { j } a _ { 3 j } c _ { j } } \end{array} } \right)
$$

one finds $\alpha _ { 1 } , \alpha _ { 2 }$ such that

$$
\alpha _ { 1 } z _ { 1 } + \alpha _ { 2 } z _ { 2 } = z _ { 3 } + \mathcal { O } ( h ^ { 3 } ) .
$$

The expression $z _ { 3 } ^ { ( 0 ) } = \alpha _ { 1 } z _ { 1 } + \alpha _ { 2 } z _ { 2 }$ then serves as starting value for the computation of $z _ { 3 }$ . In the last stage one can take $\widehat { y } _ { 1 }$ ，which is then available, for starting the Newton iterations for $g _ { s } = y _ { 1 }$ .The computation of $z _ { 3 } , z _ { 4 } , y _ { 1 }$ ，done in this way, needs few Newton iterations and a failure of convergence is usually already detected in the first stage.

However, when parallel processors are available, the exploitation of the triangular structure of the Runge-Kutta matrix may be less desirable. Whereas in the iteration (8.13） all $s$ function evaluations and much of the linear algebra can be done in parallel, this is no longer possible for DIRK-methods, when $z _ { 1 } , \dots , z _ { k }$ is used in the computations of $z _ { k + 1 }$

# SIRK-Methods

The fact that singly-implicit methods have a coeficient matrix with a one-point spectrum is the key to reducing the operation count for these methods to the level which prevails in linear multistep methods.

(J.C.Butcher, K. Burrage & FH. Chipman 1980)

In order to avoid the difficulties (in writing a Runge-Kutta code) caused by the com-plex eigenvalues of the Runge-Kutta matrix $A$ , one may look for methods with real eigenvalues, especially with a single $s$ -fold real eigenvalue. Such methods were introduced by Ngrsett (1976). Burrage (1978) provided them with error estimators, and codes in ALGOL and FORTRAN are presented in Butcher, Burrage & Chipman (1980). The basic methods for their code STRIDE are given by the following lemma.

Lemma 8.1. For collocation methods (i.e., for Runge-Kuta methods satisfying condition $C ( s )$ of Sect. IV.5), we have

$$
\operatorname* { d e t } ( I - z A ) = ( 1 - \gamma z ) ^ { s } ,
$$

if and only if

$$
c _ { \iota } = \gamma x _ { \iota } , \qquad i = 1 , \ldots , s ,
$$

where $x _ { 1 } , \dots , x _ { s }$ are the zeros of the Laguerre polynomial $L _ { s } ( x )$ $( c . f .$ Formula (6.11)).

Proof. The polynomial $\operatorname* { d e t } ( I - z A )$ is the denominator of the stability function (Formula (3.3)), so that by Theorem 3.10

$$
M ^ { ( s ) } ( 0 ) + M ^ { ( s - 1 ) } ( 0 ) z + \ldots + M ( 0 ) z ^ { s } = ( 1 - \gamma z ) ^ { s }
$$

with $M ( x )$ given by (3.25). Computing $M ^ { ( j ) } ( 0 )$ from (8.30) we obtain

$$
\frac { 1 } { s ! } \prod _ { i = 1 } ^ { s } ( x - c _ { i } ) = M ( x ) = \sum _ { \jmath = 0 } ^ { s } { \binom { s } { \jmath } } ( - \gamma ) ^ { s - \jmath } \frac { x ^ { \jmath } } { \jmath ! } = ( - \gamma ) ^ { s } L _ { s } ( \frac { x } { \gamma } )
$$

which leads to (8.29).

The stability function of the method of Lemma 8.1 has been studied in Sections IV.4 (multiple real-pole approximations) and IV.6. We have further seen (Proposition 3.8) that $R ( \infty ) = 0$ when $x _ { 0 } + h$ is a collocation point. This means that $c _ { q } = 1$ or $\gamma = 1 / x _ { q }$ for $q \in \{ 1 , \ldots , s \}$ where $0 < x _ { 1 } < . . . < x _ { s }$ are the zeros of $L _ { s } ( x ) ^ { \dagger }$ . However, if we want $A$ -stable methods, Theorem 4.25 restricts this point to be in the middle (more precisely: $q = s / 2$ or $s / 2 + 1$ for $s$ even, $q = ( s + 1 ) / 2$ for $s$ odd).An apparently undesirable consequence of this is that many of the collocation points lie outside the integration interval (for example, for $s \approx 5$ and $q = 3$ we have $c _ { 1 } = 0 . 0 7 3$ ， $c _ { 2 } = 0 . 3 9 3$ ， $c _ { 3 } = 1$ ， $c _ { 4 } = 1 . 9 7 0$ ， $c _ { 5 } = 3 . 5 1 5 )$ .

Since these methods with $\gamma = 1 / x _ { q }$ are of order $p {  } s$ only,it is easy to embed them into a method of higher order. Burrage (1978) added a further stage

$$
g _ { s + 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s + 1 } a _ { s + 1 , \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } )
$$

where $c _ { s + 1 }$ and $a _ { s + 1 , s + 1 }$ are arbitrary and the other $a _ { \mathfrak { s } + 1 , \ j }$ are determined so that the $( s + 1 )$ -stage method satisfies $C ( s )$ too. In order to avoid a new LUdecomposition we choose $a _ { s + 1 , s + 1 } = \gamma$ . The coefficient $c _ { s + 1 }$ is fixed arbitrarily

as $c _ { s + 1 } = 0$ . We then find a unique method

$$
\widehat { y } _ { 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s + 1 } \widehat { b } _ { \jmath } f ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } )
$$

of order $s + 1$ by computing the coefficients of the interpolatory quadrature rule. An explicit formula for the matrix $T$ which transforms the Runge-Kutta matrix $A$ to Jordan canonical form and $A ^ { - 1 }$ to a very simple lower triangular matrix $\Lambda$ is given in Exercise 1. It can be used for economically solving the linear system (8.13).

# Exercises

1. (Butcher 1979).For the collocation method with $c _ { 1 } , \ldots , c _ { s }$ given by (8.29) prove that (e.g. for $s = 4$ ）

$$
T ^ { - 1 } A T = \gamma \left( \begin{array} { c c c c } { { 1 } } & { { } } & { { } } & { { } } \\ { { - 1 } } & { { 1 } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { 1 } } & { { } } \\ { { } } & { { } } & { { - 1 } } & { { 1 } } \end{array} \right) , T ^ { - 1 } A ^ { - 1 } T = \frac { 1 } { \gamma } \left( \begin{array} { c c c c } { { 1 } } & { { } } & { { } } & { { } } \\ { { 1 } } & { { 1 } } & { { } } & { { } } \\ { { 1 } } & { { 1 } } & { { 1 } } & { { } } \\ { { 1 } } & { { 1 } } & { { 1 } } & { { 1 } } \end{array} \right)
$$

where the transformation $T$ satisfies

$$
T = \left( L _ { \jmath - 1 } ( x _ { \imath } ) \right) _ { \imath , \jmath = 1 } ^ { s } , \qquad T ^ { - 1 } = \left( \frac { x _ { \jmath } L _ { \imath - 1 } ( x _ { \jmath } ) } { s ^ { 2 } L _ { s - 1 } ( x _ { \jmath } ) ^ { 2 } } \right) _ { \imath , \jmath = 1 } ^ { s }
$$

and $L _ { \jmath - 1 } ( \boldsymbol { x } )$ are the Laguerre polynomials.

Hint. Use the identities

$$
L _ { n } ^ { \prime } ( x ) = L _ { n - 1 } ^ { \prime } ( x ) - L _ { n - 1 } ( x ) , \qquad L _ { n } ( x ) = L _ { n - 1 } ( x ) + { \frac { x } { n } } L _ { n } ^ { \prime } ( x )
$$

and the Christoffel-Darboux formula

$$
\sum _ { \jmath = 0 } ^ { n } L _ { \jmath } ( x ) L _ { \jmath } ( y ) = \frac { n + 1 } { y - x } \Big ( L _ { n + 1 } ( x ) L _ { n } ( y ) - L _ { n + 1 } ( y ) L _ { n } ( x ) \Big )
$$

which, in the limit $y  x$ ,becomes

$$
\sum _ { j = 0 } ^ { n } ( L _ { j } ( x ) ) ^ { 2 } = ( n + 1 ) { \Big ( } L _ { n + 1 } ( x ) L _ { n } ^ { \prime } ( x ) - L _ { n + 1 } ^ { \prime } ( x ) L _ { n } ( x ) { \Big ) } .
$$

# IV.9Extrapolation Methods

It seems that a suitable version of an IEM (implicit extrapolation method) which takes care of these dificulties may become a very strong competitor to any of the general discretization methods for stiff systems presently known.

(the very last sentence of Stetter's book,1973)

Extrapolation of explicit methods is an interesting approach to solving nonstiff differential equations (see Sect.I.9). Here we show to what extent the idea of extrapolation can also be used for stiff problems. We shall use the results of Sect. II.8 for the existence of asymptotic expansions and apply them to the study of those implicit and linearly implicit methods, which seem to be most suitable for the computation of stiff differential equations. Our theory here is restricted to classical $h  0$ order,the study of stability domains and $A$ -stability.

A big difficulty, however, is the fact that the coefficients and remainders of the asymptotic expansion can explode with increasing stiffness and the $h$ -interval, for which the expansion is meaningful,may tend to zero. Bounds on the remainder which hold uniformly for a class of arbitrarily stiff problems,will be discussed later in Sect. VI.5.

# Extrapolation of Symmetric Methods

It is most natural to look first for symmetric one-step methods as the basic integration scheme. Promising candidates are the trapezoidal rule

$$
y _ { \iota + 1 } = y _ { \iota } + { \frac { h } { 2 } } { \Bigl ( } f ( x _ { \iota } , y _ { \iota } ) + f ( x _ { \iota + 1 } , y _ { \iota + 1 } ) { \Bigr ) }
$$

and the implicit mid-point rule

$$
y _ { \imath + 1 } = y _ { \imath } + h f \Big ( x _ { \imath } + \frac { h } { 2 } , \frac { 1 } { 2 } \left( y _ { \imath + 1 } + y _ { \imath } \right) \Big ) .
$$

We take some step-number sequence $n _ { 1 } < n _ { 2 } < n _ { 3 } < \ldots$ set $\begin{array} { r } { h _ { \jmath } = H / n _ { \jmath } } \end{array}$ and define

$$
T _ { j 1 } = y _ { h _ { j } } ( x _ { 0 } + H ) ,
$$

the numerical solution obtained by performing $n _ { \jmath }$ steps with step size $h _ { \ j }$ As described in Sect.I.9 we extrapolate these values according to

$$
T _ { \jmath , k + 1 } = T _ { \jmath , k } + \frac { T _ { \jmath , k } - T _ { \jmath - 1 , k } } { ( n _ { \jmath } / n _ { \jmath - k } ) ^ { 2 } - 1 } .
$$

E. Hairer and G. Wanner, Solving Ordinary Differential Equations $I I _ { \perp }$ ， Springer Series in Computational Mathematics 14, DOI 10.1007/978-3-642-05221-7_9, $©$ Springer-Verlag Berlin Heidelberg 2010

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/83a23622c865d41304b2423d8011573c89576ab98f4a9bb9e6277ede2a662bbd.jpg)  
Fig.9.1. Stability domains for the extrapolated trapezoidal rule

This provides an extrapolation tableau

$$
\begin{array} { c c c c c } { { T _ { 1 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { T _ { 2 1 } } } & { { T _ { 2 2 } } } & { { } } & { { } } & { { } } \\ { { T _ { 3 1 } } } & { { T _ { 3 2 } } } & { { T _ { 3 3 } } } & { { } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } \end{array}
$$

all entries of which represent diagonally implicit Runge-Kutta methods (see Ex-ercise 1). Due to the symmetry of the basic schemes (9.1) and (9.2), $T _ { \ j \boldsymbol { k } }$ is a DIRK-method of order $2 k$ . In order to study the stability properties of these methods, we apply them to the test equation $y ^ { \prime } = \lambda y$ . For both methods,(9.1) and (9.2), we obtain

$$
y _ { i + 1 } = { \frac { 1 + { \frac { h \lambda } { 2 } } } { 1 - { \frac { h \lambda } { 2 } } } } y _ { i }
$$

so that the stability function $R _ { j k } ( z )$ of the method $T _ { j k }$ is given recursively by $\left( z = H \lambda \right)$

$$
\begin{array} { c } { { R _ { j 1 } ( z ) = \displaystyle \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } } , } } \\ { { R _ { j , k + 1 } ( z ) = R _ { j , k } ( z ) + \displaystyle \frac { R _ { j , k } ( z ) - R _ { j - 1 , k } ( z ) } { ( n _ { j } / n _ { j - k } ) ^ { 2 } - 1 } . } } \end{array}
$$

Already Dahlquist (1963) noticed that for $n _ { 1 } = 1$ and $n _ { 2 } = 2$ we have

$$
R _ { 2 2 } ( z ) = \frac { 1 } { 3 } \left( 4 \left( \frac { 1 + \frac { z } { 4 } } { 1 - \frac { z } { 4 } } \right) ^ { 2 } - \left( \frac { 1 + \frac { z } { 2 } } { 1 - \frac { z } { 2 } } \right) \right) \to \frac { 5 } { 3 } > 1 \mathrm { f o r } z \to \infty ,
$$

an undesirable property when solving stiff problems. Stetter (1973) proposed taking only even or only odd numbers in the step-number sequence $\{ n _ { \jmath } \}$ .Then, all stability functions of the extrapolation tableau tend for $z  \infty$ to $1$ or $- 1$ ， respectively. But even in this situation extrapolation immediately destroys the $A$ - stability of the underlying scheme (Exercise 2). Fig.9.1 shows the stability domains $\{ z \ ; \ | R _ { k k } ( z ) | \le 1 \}$ for the sequence $\{ 1 , 3 , 5 , 7 , 9 , \ldots \}$

# Smoothing

Some numerical examples reveal the power of the smoothing combined with extrapolation. (B.Lindberg 1971)

Another possibility to overcome the difficulty encountered in (9.7) is smoothing (Lindberg 1971). The idea is to replace the definition (9.3)by Gragg's smoothing step

$$
\begin{array} { c } { { \displaystyle \widehat { T } _ { \jmath 1 } = S _ { h _ { \jmath } } ( x _ { 0 } + H ) , } } \\ { { \displaystyle S _ { h } ( x ) = \frac { 1 } { 4 } \big ( y _ { h } ( x - h ) + 2 y _ { h } ( x ) + y _ { h } ( x + h ) \big ) . } } \end{array}
$$

With $y _ { h } ( x ) , S _ { h } ( x )$ also possesses an asymptotic expansion in even powers of $h$ Therefore, extrapolation according to (9.4) is justified.For the stability function of T1 we now obtain

$$
\begin{array} { c c l } { { \widehat { R } _ { j 1 } ( z ) = \displaystyle \frac { 1 } { 4 } \left\{ \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } - 1 } + 2 \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } } + \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } + 1 } \right\} } } \\ { { = \displaystyle \frac { 1 } { \left( 1 - \frac { z } { 2 n _ { j } } \right) ^ { 2 } } \left( \frac { 1 + \frac { z } { 2 n _ { j } } } { 1 - \frac { z } { 2 n _ { j } } } \right) ^ { n _ { j } - 1 } } } & { { ( 9 } } \end{array}
$$

which is an $L$ -stable approximation to the exponential function. The stability functions $\widehat { R } _ { \jmath k } ( z )$ (obtained from (9.6b)) all satisfy $\widehat { R } _ { \jmath k } ( z ) = \mathcal { O } ( z ^ { - 2 } )$ for $z \to \infty$ .For the step-number sequence

$$
\{ n _ { \jmath } \} = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , . . . \}
$$

the stability domains of $\widehat { R } _ { k k } ( z )$ are plotted in Fig.9.2.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/ea7f078e45a8f796ab5e18d8211cbe522f30832668548dbb517ea9cac702e000.jpg)  
Fig.9.2. Stability domains of Rkk(z)

# The Linearly Implicit Mid-Point Rule

Extrapolation codes based on fully implicit methods are difficult to implement efficiently. After extensive numerical computations, G.Bader and P.Deuflhard (1983) found that a linearly implicit (Rosenbrock-type) extension of the GBS method of Sect.II.9 gave promising results for stiff equations. This method is based on a two-step algorithm, since one-step Rosenbrock methods (7.4) cannot be symmetric for nonlinear differential equations.

The motivation for the Bader & Deuflhard method is based on Lawson's transformation (Lawson 1967)

$$
y ( x ) = e ^ { J x } \cdot c ( x ) ,
$$

where it is hoped that the matrix $J \approx f ^ { \prime } ( y )$ will neutralize the stiffness.Differentiation gives

$$
c ^ { \prime } = e ^ { - J x } \cdot g ( x , e ^ { J x } c ) \quad { \mathrm { ~ w i t h ~ } } \quad g ( x , y ) = f ( x , y ) - J y .
$$

We now solve (9.13) by the Gragg algorithm (I1.9.13b)

$$
c _ { i + 1 } = c _ { i - 1 } + 2 h e ^ { - J x _ { i } } \cdot g ( x _ { i } , e ^ { J x _ { i } } c _ { i } )
$$

and obtain by back-substitution of (9.12)

$$
e ^ { - h J } y _ { i + 1 } = e ^ { h J } y _ { i - 1 } + 2 h g ( x _ { i } , y _ { i } ) .
$$

For evident reasons of computational ease we now replace $e ^ { \pm h J }$ by the approximations $I \pm h J$ and obtain, adding an appropriate starting and final smoothing step,

$$
\begin{array} { r l r } & {  { ( I - h J ) y _ { 1 } = y _ { 0 } + h g ( x _ { 0 } , y _ { 0 } ) } } \\ & { } & { \displaystyle ( I - h J ) y _ { i + 1 } = ( I + h J ) y _ { i - 1 } + 2 h g ( x _ { i } , y _ { i } ) } \\ & { } & { \displaystyle S _ { h } ( x ) = \frac { 1 } { 2 } ( y _ { 2 m - 1 } + y _ { 2 m + 1 } ) \quad \mathrm { w h e r e } x = x _ { 0 } + 2 m h . } \end{array}
$$

Substituting finally $g$ from (9.13), we arrive at (with $x = x _ { 0 } + 2 m h$ ， $x _ { \ i } = x _ { 0 } + i h )$

$$
\begin{array} { c } { { ( I - h J ) ( y _ { 1 } - y _ { 0 } ) = h f ( x _ { 0 } , y _ { 0 } ) } } \\ { { ( I - h J ) ( y _ { i + 1 } - y _ { \imath } ) = \displaystyle - ( I + h J ) ( y _ { i } - y _ { \imath - 1 } ) + 2 h f ( x _ { \imath } , y _ { i } ) } } \\ { { S _ { h } ( x ) = \displaystyle \frac { 1 } { 2 } ( y _ { 2 m - 1 } + y _ { 2 m + 1 } ) } } \end{array}
$$

where $J$ stands for some approximation to the Jacobian $\frac { \partial f } { \partial y } \big ( x _ { 0 } , y _ { 0 } \big )$ . Putting $J { = } 0$ ， Formulas (9.16a) and (9.16b) become equivalent to those of the GBS method. The scheme (9.16b) is the linearly implicit (or semi-implicit) mid-point rule, Formula (9.16a) the linearly implicit Euler method.

Theorem 9.1 (Bader & Deuflhard 1983).Let $f ( x , y )$ be sufficiently often differentiable and let $J$ be an arbitrary matrix; then the numerical solution defined by $\left( 9 . l 6 a , b , c \right)$ possesses an asymptotic expansion of the form

$$
y ( x ) - S _ { h } ( x ) = \sum _ { \jmath = 1 } ^ { l } e _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } C ( x , h )
$$

where $C ( \boldsymbol { x } , h )$ is bounded for $x _ { 0 } \leq x \leq \overline { { x } }$ and $0 \leq h \leq h _ { 0 }$ .For $J \neq 0$ we have in general $e _ { j } ( x _ { 0 } ) \neq 0$

Proof. As in Stetter's proof for the GBS algorithm we introduce the variables

$$
\begin{array} { r l } & { h ^ { * } = 2 h , \quad x _ { k } ^ { * } = x _ { 0 } + k h ^ { * } , \quad u _ { 0 } = v _ { 0 } = y _ { 0 } , \quad u _ { k } = y _ { 2 k } , } \\ & { v _ { k } = ( I - h J ) y _ { 2 k + 1 } + h J y _ { 2 k } - h f ( x _ { 2 k } , y _ { 2 k } ) } \\ & { \quad = ( I + h J ) y _ { 2 k - 1 } - h J y _ { 2 k } + h f ( x _ { 2 k } , y _ { 2 k } ) . } \end{array}
$$

Method (9.16a,b) can then be rewritten as

$$
\begin{array} { r l } & { \left( \begin{array} { c } { u _ { k + 1 } } \\ { v _ { k + 1 } } \end{array} \right) = \left( \begin{array} { c } { u _ { k } } \\ { v _ { k } } \end{array} \right) \qquad ( } \\ & { + h \ast \left( \begin{array} { c c } { f \left( x _ { k } ^ { \ast } + \frac { h ^ { \ast } } { 2 } , y _ { 2 k + 1 } \right) - J y _ { 2 k + 1 } + J \left( \frac { u _ { k + 1 } + u _ { k } } { 2 } \right) } \end{array} \right) } \\ & { + h \ast \left( \begin{array} { c } { 1 \Big ( f \left( x _ { k } ^ { \ast } + h ^ { \ast } , u _ { k + 1 } \right) + f \left( x _ { k } ^ { \ast } , u _ { k } \right) \Big ) + J y _ { 2 k + 1 } - J \big ( \frac { u _ { k + 1 } + u _ { k } } { 2 } \big ) } \end{array} \right) } \end{array}
$$

where,from (9.18), we obtain the symmetric representation

$$
y _ { 2 k + 1 } = \frac { v _ { k + 1 } + v _ { k } } { 2 } + h ^ { \ast } J \Big ( \frac { u _ { k + 1 } - u _ { k } } { 4 } \Big ) - \frac { h ^ { \ast } } { 4 } \Big ( f \big ( x _ { k + 1 } ^ { \ast } , u _ { k + 1 } \big ) - f \big ( x _ { k } ^ { \ast } , u _ { k } \big ) \Big ) .
$$

The symmetry of (9.19) is illustrated in Fig.9.3 and can be checked analytically by exchanging $u _ { k + 1 }  u _ { k } , v _ { k + 1 }  v _ { k }$ ， $h ^ { \ast }  - h ^ { \ast }$ ,and $x _ { k } ^ { * }  x _ { k } ^ { * } + h ^ { * }$ . Method (9.19) is consistent with the differential equation

$$
\begin{array} { r l r } { u ^ { \prime } = f ( x , v ) - J ( v - u ) , } & { { } } & { u ( x _ { 0 } ) = y _ { 0 } } \\ { v ^ { \prime } = f ( x , u ) + J ( v - u ) , } & { { } } & { v ( x _ { 0 } ) = y _ { 0 } } \end{array}
$$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/00ed4d016f38d7705ad45db8257986a28b5aec194fefa02ad697da8382c44f39.jpg)  
Fig.9.3. Symmetry of Method (9.19) (see (9.16b))

whose exact solution is $u ( x ) = v ( x ) = y ( x )$ ，where $y ( x )$ is the solution of the original equation $y ^ { \prime } = f ( x , y )$ . Applying Theorem II.8.10 we obtain

$$
\begin{array} { l } { { y ( x ) - u _ { h ^ { * } } ( x ) = \displaystyle \sum _ { \jmath = 1 } ^ { l } a _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } A ( x , h ) } } \\ { { \displaystyle y ( x ) - v _ { h ^ { * } } ( x ) = \sum _ { \jmath = 1 } ^ { l } b _ { \jmath } ( x ) h ^ { 2 \jmath } + h ^ { 2 l + 2 } B ( x , h ) } } \end{array}
$$

with $a _ { _ { \mathcal { I } } } ( x _ { 0 } ) = b _ { _ { \mathcal { I } } } ( x _ { 0 } ) = 0$ . With the help of Formulas (9.18) we can express the numerical solution (9.16c) in terms of $u _ { m }$ and $v _ { m }$ as follows:

$$
\frac { 1 } { 2 } ( y _ { 2 m + 1 } + y _ { 2 m - 1 } ) = ( I - h ^ { 2 } J ^ { 2 } ) ^ { - 1 } \Big ( v _ { m } + h ^ { 2 } J \big ( f ( x _ { 2 m } , u _ { m } ) - J u _ { m } \big ) \Big ) ,
$$

and we obtain for $x = x _ { 0 } + 2 m h$ ，

$$
\begin{array} { c } { { y ( x ) - S _ { h } ( x ) = ( I - h ^ { 2 } J ^ { 2 } ) ^ { - 1 } \bigg ( y ( x ) - v _ { h ^ { * } } ( x ) } } \\ { { - h ^ { 2 } J \Big ( f ( x , u _ { h ^ { * } } ( x ) ) + J \big ( y ( x ) - u _ { h ^ { * } } ( x ) \big ) \Big ) \bigg ) . } } \end{array}
$$

Inserting the expansions (9.20) we find (9.17).

As an application of this theorem we obtain an interesting theoretical result on the existence of $W$ -methods (7.4) (with inexact Jacobian). We saw in Volume I (Exercise1ofSect IL9andTheoremIL9.4)thatthe $T _ { j , k }$ of the extrapolated GBS method represent explicit Runge-Kutta methods. By analogy, it is not difficult to guess that the $T _ { \ j , k }$ for the above linearly implicit midpoint rule represent W - methods (more details in Exercise 3) and we have the following existence result fol such methods.

Theorem 9.2. For $p$ even, there exists a W -method (7.4) of order $p$ with $s =$ $p ( p + 2 ) / 4$ stages.

Proof. It follows from(9.20) that for $x = x _ { 0 } + 2 m h$ the numerical solution $y _ { h } ( x ) =$ $y _ { 2 m }$ possesses an $h ^ { 2 }$ -expansion of the form (9.17) with $e _ { j } ( x _ { 0 } ) = 0$ . Therefore, extrapolation yields W -methods of order $2 k$ (in the $k$ -th column). The result follows by taking $\{ n _ { j } \} = \{ 2 , 4 , 6 , 8 , 1 0 , 1 2 , . . . \}$ and counting the number of necessary function evaluations. □

Table 9.1. $A ( \alpha )$ -stability of extrapolated linearly implicit mid-point rule   

<table><tr><td colspan="6">90°</td></tr><tr><td>90° 90°</td><td colspan="4"></td></tr><tr><td>90°</td><td>90°</td><td>90°</td><td></td><td></td></tr><tr><td>90°</td><td>89.34°</td><td>87.550</td><td>87.34°</td><td></td></tr><tr><td>90°</td><td>88.80°</td><td>86.87°</td><td>86.10°</td><td>86.02°</td></tr><tr><td>90°</td><td>88.490</td><td>87.30°</td><td>86.61°</td><td>86.36° 86.33°</td></tr><tr><td>90°</td><td>88.430</td><td>87.42°</td><td>87.00° 86.78°</td><td>86.70° 86.69°</td></tr></table>

For a stability analysis we apply the method (9.16) with $J = \lambda$ to the test equation $y ^ { \prime } = \lambda y$ . In this case Formula (9.16b) reduces to

$$
y _ { \imath + 1 } = { \frac { 1 + h \lambda } { 1 - h \lambda } } y _ { i - 1 }
$$

and the numerical result is given by

$$
S _ { h } ( x _ { 0 } + 2 m h ) = \frac { 1 } { ( 1 - h \lambda ) ^ { 2 } } \Big ( \frac { 1 + h \lambda } { 1 - h \lambda } \Big ) ^ { m - 1 } y _ { 0 } ,
$$

exactly the same as that obtained from the trapezoidal rule with smoothing (see Formula (9.10). We next have to choose a step-number sequence $\{ n _ { \jmath } \}$ . Clearly, $n _ { j } = 2 m _ { j }$ must be even.Bader & Deuflhard (1983） proposed taking only odd numbers $m _ { j }$ ， since then $S _ { h } ( x _ { 0 } + 2 m _ { \jmath } h )$ in (9.21) has the same sign as the exact solution $e ^ { \lambda \bar { 2 } m _ { j } h } y _ { 0 }$ for all real $h \lambda \leq 0$ . Consequently they were led to

$$
\{ n _ { j } \} = \{ 2 , 6 , 1 0 , 1 4 , 2 2 , 3 4 , 5 0 , . . . \} .
$$

Putting $T _ { j 1 } = S _ { h _ { j } } ( x _ { 0 } + H )$ with ${ h _ { j } = H / n _ { j } }$ and defining $T _ { j k }$ by (9.4) we obtain a tableau of $W$ -methods (7.4) (Exercise 3). By Theorem 9.1 the $k$ -th column of this tableau represents methods of order $2 k - 1$ independent of the choice of $J$ (the methods are not of order $2 k$ ,since $e _ { l } ( x _ { 0 } ) \neq 0$ in (9.17)). The stability function of $T _ { j 1 }$ is given by

$$
R _ { j 1 } ( z ) = \frac { 1 } { ( 1 - \frac { z } { n _ { j } } ) ^ { 2 } } \left( \frac { 1 + \frac { z } { n _ { j } } } { 1 - \frac { z } { n _ { j } } } \right) ^ { n _ { j } / 2 - 1 }
$$

and those of $T _ { \ j \boldsymbol { k } }$ can be computed with the recursion (9.6b). An investigation of the $E$ -polynomial (3.8) for these rational functions shows that not only $T _ { j 1 }$ ,but

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/500f1c6133a71c149d84c345e6cf79150b9e8732c8d63d60c50390a7e0c258ee.jpg)  
Fig. 9.4. Stability domains of extrapolated linearly implicit mid-point rule

also $T _ { 2 2 } , T _ { 3 2 }$ and $T _ { 3 3 }$ are $A$ -stable (Hairer,Bader & Lubich 1982). The angle of $A ( \alpha )$ -stability for some further elements in the extrapolation tableau are listed in Table 9.1. Stability domains of $T _ { k k }$ for $k = 2 , 3 , 4 , 5 , 6$ are plotted in Fig. 9.4.

# Implicit and Linearly Implicit Euler Method

Why not consider also non-symmetric methods as basic integration schemes? Deuflhard (1985) reports on experiments with extrapolation of the implicit Euler method

$$
y _ { i + 1 } = y _ { i } + h f ( x _ { i + 1 } , y _ { \imath + 1 } )
$$

and of the linearly implicit Euler method

$$
( I - h J ) ( y _ { i + 1 } - y _ { i } ) = h f ( x _ { i } , y _ { i } ) ,
$$

where, again, $J$ is an approximation to $\frac { \partial f } { \partial y } \big ( x _ { 0 } , y _ { 0 } \big )$ .These methods are not symmetric and have only a $h$ -expansion of their global error. We therefore have to extrapolate the numerical solutions at $x _ { 0 } + H$ according to

$$
T _ { j , k + 1 } = T _ { j , k } + \frac { T _ { j , k } - T _ { j - 1 , k } } { ( n _ { j } / n _ { j - k } ) - 1 } ,
$$

so that $T _ { j k }$ represents a method of order $k$

For both basic methods,(9.24) and (9.25), the stability function of $T _ { j k }$ is the same and defined recursively by

$$
\begin{array} { c } { { R _ { j 1 } ( z ) = \displaystyle \bigg ( 1 - \frac { z } { n _ { j } } \bigg ) ^ { - n _ { j } } } } \\ { { { } } } \\ { { R _ { j , k + 1 } ( z ) = R _ { j , k } ( z ) + \displaystyle \frac { R _ { j , k } ( z ) - R _ { j - 1 , k } ( z ) } { ( n _ { j } / n _ { j - k } ) - 1 } . } }  \end{array}
$$

Taking the step-number sequence

$$
\{ n _ { j } \} = \{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , . . . \}
$$

we have plotted in Fig.9.5 the stability domains of $R _ { k k } ( z )$ (left picture） and $R _ { k , k - 1 } ( z )$ (right picture). All these methods are seen to be $A ( \alpha )$ -stable with $\alpha$ close to $9 0 °$ . The values of $\alpha$ (computed numerically) for $R _ { j k } ( z )$ with $j \le 8$ are given in Table 9.2.

We shall see in the chapter on differential algebraic systems that it is preferable to use the first subdiagonal of the extrapolation tableau resulting from (9.28). This is equivalent to the use of the step number sequence $\{ n _ { i } \} = \{ 2 , 3 , 4 , 5 , . . . \}$ . Also an effective construction of a dense output can best be motivated in the seting of differential-algebraic equations (Sect. VI.5).

Table 9.2. $A ( \alpha )$ -stabiliy of extrapolated Euler   

<table><tr><td colspan="8"></td></tr><tr><td>90° 90° 90°</td><td colspan="5"></td><td rowspan="7">89.80°</td></tr><tr><td>90°</td><td>90°</td><td>89.850</td><td></td><td></td></tr><tr><td>90°</td><td>90°</td><td>89.90°</td><td>89.77°</td><td></td></tr><tr><td>90°</td><td>90°</td><td>89.930</td><td>89.84°</td><td>89.77°</td></tr><tr><td>90°</td><td>90°</td><td>89.95°</td><td>89.88°</td><td>89.82° 89.780</td></tr><tr><td>90°</td><td>90°</td><td>89.96°</td><td>89.91° 89.860</td><td>89.820 89.83°</td></tr><tr><td>90°</td><td>90°</td><td>89.970</td><td>89.93°</td><td>89.89° 89.85°</td></tr></table>

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/4ebadf70862a50d3aa59480b18587f4c0358f000ba7e3f709f65db63c878de45.jpg)  
Fig.9.5.Stability domains of extrapolated Euler

# Implementation

Extrapolation methods based on implicit discretizations are in general less efficient than those based on linearly implicit discretizations. The reason is that the arising nonlinear systems have to be solved very accurately, so that the asymptotic expansion of the error is not destroyed. The first successful extrapolation code for stiff differential equations is METAN1 of Bader & Deuflhard (1983),which implements the linearly implicit mid-point rule (9.16). In fact, Formula (9.16b) is replaced by the equivalent formulation

$$
\Delta y _ { \imath } = \Delta y _ { i - 1 } + 2 ( I - h J ) ^ { - 1 } \Big ( h f ( x _ { \imath } , y _ { \imath } ) - \Delta y _ { \imath - 1 } \Big ) , \quad \Delta y _ { \imath } = y _ { \imath + 1 } - y _ { \imath }
$$

which avoids a matrix-vector multiplication. The step size and order selection of this code is described in Deuflhard (1983). Modifications in the control of step size and order are proposed by Shampine (1987). We have implemented the following two extrapolation codes (see Appendix):

SODEX is based on the linearly implicit mid-point rule (9.16),uses the stepnumber sequence (9.22) and is mathematically equivalent to METAN1. The step size and order selection in SODEX is with some minor changes that of the non-stiff code ODEX of Sect. II.9. We just mention that in the formula for the work per unit step (II.9.26) the number $A _ { k }$ is augmented by the dimension of the differential equation in order to take into account the Jacobian evaluation.

SEULEX is an implementation of the linearly implicit Euler method (9.25) using the step-number sequence $\{ 2 , 3 , 4 , 5 , 6 , 7 , \ldots \}$ (other sequences can be chosen as internal options). The step size and order selection is that of SODEX. The original code (EULSIM, first discussed by Deuflhard 1985) uses the same numerical method,but a different implementation.

Neither code can solve the van der Pol equation problem in a straightforward way because of overflow ...

(L.F. Shampine 1987)

A big diffculty in the implementation of extrapolation methods is the use of “large” step sizes. During the computation of $T _ { \ j 1 }$ one may easily get into trouble with exponential overflow when evaluating the right-hand side of the differential equation. As a remedy we propose the following strategies:

a） In establishing the extrapolation tableau we compare the estimated error $e r r _ { \jmath } =$ $\| T _ { j , j - 1 } - T _ { j j } \|$ with the preceding one. Whenever $e r r _ { j } \geq e r r _ { j - 1 }$ for some $j \geq 3$ we restart the computation of the step with a smaller $H$ ,say, $H = 0 . 5 \cdot H$   
b) In order to be able to interrupt the computations already after the first $f$ evaluations,we require that the step sizes $h = H / n _ { i }$ (for $i = 1$ and $i \approx 2$ be small enough so that a simplified Newton iteration applied to the implicit Euler method $y = y _ { 0 } + h f ( x , y )$ ， $x = x _ { 0 } + h$ would converge ("stability check", an idea of Deuflhard). The first two iterations read

$$
\begin{array} { r l } & { ( I - h J ) \Delta _ { 0 } = h f ( x _ { 0 } , y _ { 0 } ) , \qquad y ^ { ( 1 ) } = y _ { 0 } + \Delta _ { 0 } } \\ & { ( I - h J ) \Delta _ { 1 } = h f ( x _ { 0 } + h , y ^ { ( 1 ) } ) - \Delta _ { 0 } . } \end{array}
$$

The computations for the step are restarted with a smaller $H$ ,if $\| \Delta _ { 1 } \| \ge \| \Delta _ { 0 } \|$ (divergence of the iteration). Observe that for both methods,(9.16) and (9.25), no additional function evaluations are necessary. For the linearly implicit midpoint rule we have the simple relations $\Delta _ { 0 } = \Delta y _ { 0 }$ ， $\begin{array} { r } { \Delta _ { 1 } = \frac { 1 } { 2 } ( \Delta y _ { 1 } - \Delta y _ { 0 } ) } \end{array}$ (see (9.29)).

Non-Autonomous Differential Equations. Given a non-autonomous differential equation $y ^ { \prime } { = } f ( x , y )$ , one has several possibilities to apply the above extrapolation algorithms:

i) apply the Formula (9.16) or (9.25)directly (this is justified, since allasymptotic expansions hold for general non-autonomous problems);   
ii） transform the differential equation into an autonomous system by adding $x ^ { \prime } = 1$ and then apply the algorithm. This yields

$$
( I - h J ) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( x _ { \iota } , y _ { \iota } ) + h ^ { 2 } \frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } )
$$

for the linearly implicit Euler method (the derivative $\frac { \partial f } { \partial x } ( x _ { 0 } , y _ { 0 } )$ can also be replaced by some approximation). For the linearly implicit mid-point rule, (9.16a) has to be replaced by (9.31) with $i \simeq 0$ , the remaining two formulas (9.16b) and (9.16c) are not changed.

iii） apply one simplified Newton iteration to the implicit Euler discretization (9.24). This gives

$$
( I - h J ) ( y _ { \iota + 1 } - y _ { \iota } ) = h f ( x _ { \iota + 1 } , y _ { \iota } ) .
$$

The use of this formula avoids the computation of the derivative $\partial f / \partial x$ ,but requires one additional function evaluation for each $T _ { , \mathfrak { l } }$ . In the case of the linearly implicit mid-point rule the replacement of (9.16a) by (9.32） would destroy symmetry and the expansions in $h ^ { 2 }$

A theoretical study of the three different approaches for the linearly implicit Euler method applied to the Prothero-Robinson equation (see Exercise 4 below) indicates that the third approach is preferable. More theoretical insight into this question will be obtained from the study of singular perturbation problems (Chapter VI).

Implicit Differential Equations. Our codes in the appendix are written for problems of the form

$$
M y ^ { \prime } = f ( x , y )
$$

where $M$ is a constant square matrix. The necessary modifications in the basic formulas are obtained,as usual, by replacing all $f ^ { \prime } s$ and $J ^ { \prime } s$ by $M ^ { - 1 } f$ and $M ^ { - 1 } J$ ， and premultiplying by $M$ . The linearly implicit Euler method then reads

$$
( M - h J ) ( y _ { i + 1 } - y _ { \imath } ) = h f ( x _ { \imath } , y _ { \imath } )
$$

andthe linearlyimplicit mid-pointrule becomes,with $\Delta y _ { i } = y _ { i + 1 } - y _ { i }$

$$
\Delta y _ { \imath } = \Delta y _ { \imath - 1 } + 2 ( M - h J ) ^ { - 1 } \Big ( h f ( x _ { \imath } , y _ { i } ) - M \Delta y _ { \imath - 1 } \Big ) .
$$

# Exercises

1. Consider the implicit mid-point rule (9.2) as basic integration scheme and define $T _ { \ j \boldsymbol { k } }$ by (9.3) and (9.4).

a) Prove that $T _ { \ j \boldsymbol { k } }$ represents a DIRK-method of order $p = 2 k$ with $s = n _ { \mathrm { 1 } } +$ $n _ { 2 } + \ldots + n _ { _ { J } }$ stages.

b） $\widehat { T } _ { \jmath k }$ ,definedy(9.8)d(9.4)svalettK-etdfder $p = \bar { 2 } k - 1$ only.

2.Let $R _ { \ j k } ( z )$ be given by (9.6) and assume that the step-number sequence consists of even numbers only. Prove that $R _ { \ j 2 } ( z )$ cannot be $A$ -stable. More precisely, show that at most a finite number of points of the imaginary axis can lie in the stability domain of $R _ { j 2 } ( z )$ (interpret Fig. 9.6).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/39722dae46486d4bc0ba72671a329fd34bb3ea3bc5ee99cbf3263a4b62ca6b36.jpg)  
Fig.9.6. How extrapolation destroys $A$ -stability

3.Prove that $S _ { h } ( x )$ ,defined by (9.16),is the numerical result of the $( 2 n + 1 )$ stage $W$ -method (7.4) with the following coefficients $\left( n = 2 m \right)$ ：

$$
\begin{array} { r l } & { \alpha _ { i j } = \left\{ \begin{array} { l l } { 1 / n } & { \mathrm { i f ~ } j = 1 \mathrm { ~ a n d ~ } i \mathrm { ~ e v e n } , } \\ { 2 / n } & { \mathrm { i f ~ } 1 < j < i \mathrm { ~ a n d ~ } i - j \mathrm { ~ o d d } , } \\ { 0 } & { \mathrm { e l s e } . } \end{array} \right. } \\ & { \gamma _ { \imath j } = \left\{ \begin{array} { l l } { ( - 1 ) ^ { i - j } / n } & { \mathrm { i f ~ } j = 1 \mathrm { ~ o r ~ } j = i , } \\ { 2 ( - 1 ) ^ { i - \jmath } / n } & { \mathrm { i f ~ } 1 < j < i . } \end{array} \right. } \\ & { b _ { \imath } = \alpha _ { n + 1 , \imath } + \gamma _ { n + 1 , i } \qquad \mathrm { f o r ~ a l l ~ } i . } \end{array}
$$

4.Apply the three different versions of the linearly implicit Euler method (9.25), (9.31) and (9.32) to the problem $y ^ { \prime } = \lambda ( y - \varphi ( x ) ) + \varphi ^ { \prime } ( x )$ ．Prove that the errors $e _ { i } = y _ { i } - \varphi ( x _ { i } )$ satisfy $e _ { \imath + 1 } = ( 1 - h \lambda ) ^ { - 1 } e _ { \imath } + \delta _ { h } ( x _ { i } )$ , where for $h \to 0$ and $h \lambda  \infty$ ，

$$
\begin{array} { l } { { \delta _ { h } ( x ) = - h \varphi ^ { \prime } ( x ) + { \mathcal O } ( h ^ { 2 } ) + { \mathcal O } ( \lambda ^ { - 1 } ) , } } \\ { { \delta _ { h } ( x ) = - \displaystyle \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + ( 1 - h \lambda ) ^ { - 1 } h ^ { 2 } \lambda ( \varphi ^ { \prime } ( x ) - \varphi ^ { \prime } ( x _ { 0 } ) ) + { \mathcal O } ( h ^ { 3 } ) + { \mathcal O } ( h \lambda ^ { - 1 } ) , } } \\ { { \delta _ { h } ( x ) = ( 1 - h \lambda ) ^ { - 1 } \Big ( \displaystyle \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + { \mathcal O } ( h ^ { 3 } ) \Big ) , } } \end{array}
$$

respectively.

Theory without practice cannot survive and dies as quickly as it lives. (Leonardo da Vinci

1452-1519,cited from M. Kline,Math. Thought 1972, p. 224)

Sine experientia nihil sufficienter scrire potest (Without experience it is not possible to know anything adequately).

(Inscription overlooking Botanic Garden, Oxford; found in The Latin Citation Calendar, Oxford 1996)

After having seen so many diferent methods and ideas in the foregoing sections, it is legitimate to study how all these theoretical properties pay off in numerical efficiency.

# The Codes Used

We compared the following codes, some of which are described in the Appendix:

RADAU5 and SDIRK4 are implicit Runge-Kutta codes. The first one is based on the Radau IIA method with $s = 3$ of order 5 (Table 5.6), whereas the second one is based on the SDIRK method (6.16) of order 4. Both methods are $I$ stable. Details of their implementation are given in Sect.IV.8.

RODAS and ROS4 are Rosenbrock codes of order 4 with an embedded 3rd order error estimator. ROS4 implements the methods of Table 7.2. A switch allows one to choose between the different coefficient sets. The underlying method of RODAS satisfies additional order conditions for differential-algebraic equations (see Sect. VI.4 below), but requires a little more work per step. RODAS5 is an extension of RODAS to order 5. Its coefcients are constructed by Di Marzo (1992).

SEULEX and SODEX are extrapolation codes. They implement the (Stiff) linearly implicit EULer EXtrapolation method (9.32) and the extrapolation algorithm based on the linearly implicit mid-point rule (method (9.16) of Bader & Deuflhard 1983),respectively. Both methods are discussed in Sect.IV.9.

In the numerical experiments of this section we have also included the results of LSODE (a BDF code of Hindmarsh 1980)． It is a representative of the class of multistep methods to be described in Chapter V.

Many of the treated examples are very stiff and explicit methods would require hours to compute the solution. On some examples, however, it was also interesting to see their performance, especially for the methods with extended region of stabil-ity (e.g., the Runge-Kutta-Chebyshev code RKC of Sommeijer (1991), explained in Sect.IV.2),as well as for a standard explicit Runge-Kutta code, such as DOPRI5 of Volume I.

# Twelve Test Problems

Man huite sich,auf Grund einzelner Beispiele allgemeine Schluisse über den Wert oder Unwert einer Methode zu ziehen. Dazu gehort sehr viel Erfahrung. (L. Collatz 1950)

The first extensive numerical comparisons for stiff equations were made by Enright, Hull & Lindberg (1975). Their STIFF-DETEST set of problems has become a veritable “must” for generations of software writers (see also the critical remarks of Shampine 1981). Several additional test problems, usually from chemical kinetics,have been proposed by Enright & Hull (1976). An interesting review article containing also problems of large dimension is due to Byrne & Hindmarsh (1987).

The problems chosen here for our tests are the following:

VDPOL - the van der Pol oscillator (see (1.5") and Fig.8.1)

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = y _ { 2 } } \\ { \qquad y _ { 2 } ^ { \prime } = \big ( ( 1 - y _ { 1 } ^ { 2 } ) y _ { 2 } - y _ { 1 } \big ) / \varepsilon , \qquad \varepsilon = 1 0 ^ { - 6 } } \\ { y _ { 1 } ( 0 ) = 2 , \quad y _ { 2 } ( 0 ) = 0 ; \quad x _ { \mathrm { o u t } } = 1 , 2 , 3 , 4 , \dots , 1 1 . } \end{array}
$$

ROBER - the reaction of Robertson (1966) (see (1.3) and (1.4))

$$
\begin{array} { r l r } { y _ { 1 } ^ { \prime } = - 0 . 0 4 y _ { 1 } + 1 0 ^ { 4 } y _ { 2 } y _ { 3 } \qquad } & { } & { y _ { 1 } ( 0 ) = 1 } \\ { y _ { 2 } ^ { \prime } = } & { { } 0 . 0 4 y _ { 1 } - 1 0 ^ { 4 } y _ { 2 } y _ { 3 } - 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & { y _ { 2 } ( 0 ) = 0 } \\ { y _ { 3 } ^ { \prime } = } & { { } \ 3 \cdot 1 0 ^ { 7 } y _ { 2 } ^ { 2 } \qquad } & { y _ { 3 } ( 0 ) = 0 , } \end{array}
$$

one of the most prominent examples of the “stiff" literature. It was usually treated on the interval $0 \leq x \leq 4 0$ , until Hindmarsh discovered that many codes fail if $_ x$ becomes very large $( 1 0 ^ { 1 1 } \ \mathrm { s a y } )$ . The reason is that whenever the numerical solution of $y _ { 2 }$ accidentally becomes negative, it then tends to $- \infty$ and the run ends by overflow. We have therefore chosen $x _ { \mathrm { o u t } } = 1 , 1 0 , 1 0 ^ { 2 } , 1 0 ^ { 3 } , \dotsc , 1 0 ^ { 1 1 }$ ·

OREGO - the Oregonator, the famous model with a periodic solution describing the Belusov-Zhabotinskii reaction (Field & Noyes 1974,see also Enright & Hull 1976)

$$
\begin{array} { l } { y _ { 1 } ^ { \prime } = 7 7 . 2 7 \Big ( y _ { 2 } + y _ { 1 } \big ( 1 - 8 . 3 7 5 \cdot 1 0 ^ { - 6 } y _ { 1 } - y _ { 2 } \big ) \Big ) } \\ { y _ { 2 } ^ { \prime } = \cfrac { 1 } { 7 7 . 2 7 } \big ( y _ { 3 } - ( 1 + y _ { 1 } ) y _ { 2 } \big ) } \\ { y _ { 3 } ^ { \prime } = 0 . 1 6 1 \big ( y _ { 1 } - y _ { 3 } \big ) } \end{array}
$$

$$
y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = 2 , \quad y _ { 3 } ( 0 ) = 3 , \qquad x _ { 0 0 t } = 3 0 , 6 0 , 9 0 , \ldots , 3 6 0 .
$$

For pictures see Volume I, p. 119.

HIRES -this chemical reaction involving eight reactants was proposed by Schäfer (1975） to explain “the growth and differentiation of plant tissue independent of

photosynthesis at high levels of irradiance by light". It has been promoted as a test example by Gottwald (1977). The corresponding equations are

$$
\begin{array} { r l } & { y _ { 1 } ^ { \prime } = - 1 . 7 1 \cdot y _ { 1 } + 0 . 4 3 \cdot y _ { 2 } + 8 . 3 2 \cdot y _ { 3 } + 0 . 0 0 0 7 } \\ & { y _ { 2 } ^ { \prime } = 1 . 7 1 \cdot y _ { 1 } - 8 . 7 5 \cdot y _ { 2 } } \\ & { y _ { 3 } ^ { \prime } = - 1 0 . 0 3 \cdot y _ { 3 } + 0 . 4 3 \cdot y _ { 4 } + 0 . 0 3 5 \cdot y _ { 5 } } \\ & { y _ { 4 } ^ { \prime } = 8 . 3 2 \cdot y _ { 2 } + 1 . 7 1 \cdot y _ { 3 } - 1 . 1 2 \cdot y _ { 4 } } \\ & { y _ { 5 } ^ { \prime } \simeq - 1 . 7 4 5 \cdot y _ { 5 } + 0 . 4 3 \cdot y _ { 6 } + 0 . 4 3 \cdot y _ { 7 } } \\ & { y _ { 6 } ^ { \prime } = - 2 8 0 \cdot y _ { 6 } y _ { 8 } + 0 . 6 9 \cdot y _ { 4 } + 1 . 7 1 \cdot y _ { 5 } - 0 . 4 3 \cdot y _ { 6 } + 0 . 6 9 \cdot y _ { 7 } } \\ & { y _ { 7 } ^ { \prime } = 2 8 0 \cdot y _ { 6 } y _ { 8 } - 1 . 8 1 \cdot y _ { 7 } } \\ & { y _ { 8 } ^ { \prime } = - y _ { 7 } ^ { \prime } } \end{array}
$$

$$
y _ { 1 } ( 0 ) = 1 , \quad y _ { 2 } ( 0 ) = y _ { 3 } ( 0 ) = \ldots = y _ { 7 } ( 0 ) = 0 , \quad y _ { 8 } ( 0 ) = 0 . 0 0 5 7
$$

and chosen output values are $x _ { \mathrm { o u t } } = 3 2 1 . 8 1 2 2$ and 421.8122.

E5 — is another chemical recation problem, called $^ { 6 6 } \mathrm { E } 5 ^ { \circ }$ in the collection by Enright,Hull & Lindberg (1975). It is given by

$$
\begin{array} { r l r l } { y _ { 1 } ^ { \prime } = - A y _ { 1 } - B y _ { 1 } y _ { 3 } } & { } & & { y _ { 1 } ( 0 ) = 1 . 7 6 \cdot 1 0 ^ { - 3 } } \\ { y _ { 2 } ^ { \prime } = { } } & { { } A y _ { 1 } } & { - M C y _ { 2 } y _ { 3 } } & { } & { y _ { 2 } ( 0 ) = 0 } \\ { y _ { 3 } ^ { \prime } = { } } & { { } A y _ { 1 } - B y _ { 1 } y _ { 3 } - M C y _ { 2 } y _ { 3 } + C y _ { 4 } } & { } & { y _ { 3 } ( 0 ) = 0 } \\ { y _ { 4 } ^ { \prime } = { } } & { { } B y _ { 1 } y _ { 3 } } & { - C y _ { 4 } } & { } & { y _ { 4 } ( 0 ) = 0 , } \end{array}
$$

where $A = 7 . 8 9 \cdot 1 0 ^ { - 1 0 }$ ， $B = 1 . 1 \cdot 1 0 ^ { 7 }$ ， $C = 1 . 1 3 \cdot 1 0 ^ { 3 }$ ,and $M = 1 0 ^ { 6 }$ . As we can see from Fig.10.1 the variables are badly scaled $( y _ { 1 } \approx 1 0 ^ { - 3 }$ at the beginning,all other components do not exceed the value $1 . 4 6 \cdot 1 0 ^ { - 1 0 } )$ ,and “... a scalar absolute error tolerance is quite unsuitable” (Shampine 1981). The differential equation possesses the invariant $y _ { 2 } - y _ { 3 } - y _ { 4 } = 0$ , and it is recommended to use the relation $y _ { 3 } ^ { \prime } = y _ { 2 } ^ { \prime } - y _ { 4 } ^ { \prime }$ in the function subroutine (because of eventual cancellation of digits).

Originally the problem was posed on the interval $0 \leq x \leq 1 0 0 0$ , but Alexander (1997) discovered that the solutions possess interesting properties on a much longer interval.We folow this suggestion and consider output values at $x _ { \tt o u t } =$ $1 0 , 1 0 ^ { 3 } , 1 0 ^ { 5 } , 1 0 ^ { 7 } , \dotsc , 1 0 ^ { 1 3 }$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/c815e9e9ee59e64b3193a46d67ff29f64d551f6a5229652c5c8d1792d3a94375.jpg)  
Fig.10.1. Solution of (10.5) in double logarithmic scale

PLATE - this is a linear and non-autonomous example of medium stiffness and medium size. It describes the movement of a rectangular plate under the load of a car passing across it:

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } + \omega \frac { \partial u } { \partial t } + \sigma \Delta \Delta u = f ( x , y , t ) .
$$

The plate $\Omega = \{ ( x , y ) ; 0 \leq x \leq 2 , 0 \leq y \leq 4 / 3 \}$ is discretized on a grid of $8 \times 5$ interior points $x _ { \imath } = i h$ ， $y _ { \jmath } = j h , h = 2 / 9$ with initial and boundary conditions

$$
u | _ { \partial \Omega } = 0 , \quad \Delta u | _ { \partial \Omega } = 0 , \quad u ( x , y , 0 ) = 0 , \quad \frac { \partial u } { \partial t } ( x , y , 0 ) = 0 .
$$

The integration interval is $0 \leq t \leq 7$ . The load $f ( x , y , t )$ is idealized by the sum of two Gaussian curves which move in the $x$ -direction and which reside on “four wheels"

$$
f ( x , y , t ) = \left\{ \begin{array} { c c } { { 2 0 0 \big ( e ^ { - 5 ( t - x - 2 ) ^ { 2 } } + e ^ { - 5 ( t - x - 5 ) ^ { 2 } } \big ) } } & { { \mathrm { i f ~ } y = y _ { 2 } \mathrm { ~ o r ~ } y _ { 4 } } } \\ { { 0 } } & { { \mathrm { f o r ~ a l l ~ o t h e r ~ } y . } } \end{array} \right.
$$

The plate operator $\Delta \Delta$ is discretized via the standard “computational molecule”

$$
\begin{array} { r l } { 1 } & { { } } \\ { 2 } & { { } { - } 8 \quad 2 } \\ { 1 } & { { } { - } 8 \quad 2 0 \quad { - } 8 \quad 1 } \\ { 2 } & { { } { - } 8 \quad 2 } \\ { 1 } & { { } \qquad 1 } \end{array}
$$

and the friction and stiffness parameters are chosen as $\omega = 1 0 0 0$ and $\sigma = 1 0 0$ The resulting system is then of dimension 80 with negative real as well as complex eigenvalues ranging between $- 5 0 0 \leq \mathrm { R e } \lambda < 0$ with maximal angle $\alpha \approx 7 1 ^ { \circ }$ (see Definition 3.9).

BEAM— the elastic beam (1.10) of Sect.IV.1. We choose $n = 4 0$ in (1.10'） so that the differential system is of dimension 80, and $0 \le t \le 5$ as integration interval. The eigenvalues of the Jacobian are purely imaginary and vary between $- 6 4 0 0 i$ and $+ 6 4 0 0 i$ (see Eq.(2.23)). The initial conditions (1.18) and (1.19) are chosen such that the solution nevertheless appears to be smooth. However, a detailed numerical study shows that the exact solution possesses high oscillations with period $\approx 2 \pi / 6 4 0 0$ and amplitude $\approx 1 0 ^ { - 6 }$ (see Fig.10.2).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/3b059ee4cb0251e10b2f483d415a3d1664ed3518db57f7127a114afe064b0028.jpg)  
Fig.10.2. Third finite differences $\Delta ^ { 3 } y _ { 8 0 } / \Delta x ^ { 3 }$ of solutionsof the beam equation (1.10'） with $n = 4 0$ for $0 \leq x \leq 0 . 0 7$

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/164cb468cfd0531dc6b04f5d3db01189a5ee55dd546c64564dcf85ad9605b0e7.jpg)  
Fig.10.3. The cusp catastrophe with $N \approx 3 2$

CUSP — this is a combination of Zeeman's “cusp catastrophe”model ( $( - \varepsilon \dot { y } =$ $y ^ { 3 } + a y + b )$ for the nerve impulse mechanism (Zeeman 1972) combined with the van der Pol oscillator (see Fig.10.3)

$$
\begin{array} { l } { \displaystyle \frac { \partial y } { \partial t } = - \frac { 1 } { \varepsilon } ( y ^ { 3 } + a y + b ) + \sigma \frac { \partial ^ { 2 } y } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial a } { \partial t } = b + 0 . 0 7 v + \sigma \frac { \partial ^ { 2 } a } { \partial x ^ { 2 } } } \\ { \displaystyle \frac { \partial b } { \partial t } = ( 1 - a ^ { 2 } ) b - a - 0 . 4 y + 0 . 0 3 5 v + \sigma \frac { \partial ^ { 2 } b } { \partial x ^ { 2 } } } \end{array}
$$

where

$$
v = \frac { u } { u + 0 . 1 } , \quad u = ( y - 0 . 7 ) ( y - 1 . 3 ) .
$$

We put $\sigma = 1 / 1 4 4$ and make the problem stiff by choosing $\varepsilon = 1 0 ^ { - 4 }$ . We discretize the diffusion terms by the method of lines

$$
\begin{array} { r l } & { \dot { y } _ { \iota } = - 1 0 ^ { 4 } ( y _ { \iota } ^ { 3 } + a _ { \iota } y _ { \iota } + b _ { \iota } ) + D ( y _ { \iota - 1 } - 2 y _ { \iota } + y _ { \iota + 1 } ) } \\ & { \dot { a } _ { \iota } = b _ { \iota } + 0 . 0 7 v _ { \iota } + D ( a _ { \iota - 1 } - 2 a _ { \iota } + a _ { \iota + 1 } ) \qquad \quad \qquad i = 1 , \dots , N } \\ & { \dot { b } _ { \iota } = ( 1 - a _ { \iota } ^ { 2 } ) b _ { \iota } - a _ { \iota } - 0 . 4 y _ { \iota } + 0 . 0 3 5 v _ { \iota } + D ( b _ { \iota - 1 } - 2 b _ { \iota } + b _ { \iota + 1 } ) } \end{array}
$$

where

$$
N = 3 2 , \quad v _ { \ i } = \frac { u _ { \ i } } { u _ { \ i } + 0 . 1 } , \quad u _ { \ i } = ( y _ { \ i } - 0 . 7 ) ( y _ { \ i } - 1 . 3 ) , \quad D = \sigma N ^ { 2 } = \frac { N ^ { 2 } } { 1 4 4 } ,
$$

with periodic boundary conditions

$$
\begin{array} { r l r l r l } { y _ { 0 } : = y _ { N } , } & { \quad } & { a _ { 0 } : = a _ { N } , } & { \quad } & { b _ { 0 } : = b _ { N } , } & \\ { y _ { N + 1 } : = y _ { 1 } , } & { \quad } & { a _ { N + 1 } : = a _ { 1 } , } & { \quad } & { b _ { N + 1 } : = b _ { 1 } , } & \end{array}
$$

and obtain a system of dimension $3 \cdot N = 9 6$ . We take the initial values

$$
y _ { \tau } ( 0 ) = 0 , \quad a _ { \ i } ( 0 ) = - 2 \cos \Bigl ( { \frac { 2 i \pi } { N } } \Bigr ) , \quad b _ { \ i } ( 0 ) = 2 \sin \Bigl ( { \frac { 2 i \pi } { N } } \Bigr ) \qquad i = 1 , \ldots , N .
$$

and $t _ { \mathrm { o u t } } = 1 . 1$ ·

BRUSS — this is the equation(1.6') with $\alpha = 1 / 5 0$ ,the same initial conditions as in Sect.IV.1,and integration interval $0 \leq t \leq 1 0$ . But we now let $N = 5 0 0$ so that (1.6') becomes a system of 1ooo differential equations with largest eigenvalue close to $- 2 0 0 0 0$ . The equations therefore become considerably stiff. The Jacobian of this system is banded with upper and lower bandwidth 2 (if the solution components are ordered as $u _ { 1 } , v _ { 1 } , u _ { 2 } , v _ { 2 } , u _ { 3 } , v _ { 3 } , \quad$ etc.).

KS - is the one-dimensional Kuramoto-Sivashinsky equation

$$
{ \frac { \partial U } { \partial t } } = - { \frac { \partial ^ { 2 } U } { \partial x ^ { 2 } } } - { \frac { \partial ^ { 4 } U } { \partial x ^ { 4 } } } - { \frac { 1 } { 2 } } { \frac { \partial U ^ { 2 } } { \partial x } }
$$

with periodic boundary conditions $\boldsymbol { u } ( \boldsymbol { x } + \boldsymbol { L } , t ) = \boldsymbol { u } ( \boldsymbol { x } , t )$ , taken from Collet, Eckmann,Epstein & Stubbe (1993)．We choose $L = 2 \pi / q$ ， $q = 0 . 0 2 5$ , and take as initial condition

$$
\begin{array} { r l } & { \eta _ { 1 } = \operatorname* { m i n } ( x / L , 0 . 1 - x / L ) , } \\ & { \eta _ { 2 } = 2 0 ( x / L - 0 . 2 ) ( 0 . 3 - x / L ) , } \\ & { \eta _ { 3 } = \operatorname* { m i n } ( x / L - 0 . 6 , 0 . 7 - x / L ) , } \\ & { \eta _ { 4 } = \operatorname* { m i n } ( x / L - 0 . 9 , 1 - x / L ) , } \end{array}
$$

The inverse heat equation term $- \partial ^ { 2 } U / \partial x ^ { 2 }$ creates instability, which is stabilized for the higher oscillations by the beam equation term $- \partial ^ { 4 } U / \partial x ^ { 4 }$ . The nonlinear transport term $\partial U ^ { 2 } / \partial x$ couples the modes and ensures that the solution remains bounded. All this creates wonderful chaos (see Fig.10.4).

We solve Eq.(10.9) using the pseudo-spectral method, i.e.，we consider the Fourier coefficients

$$
\widehat { U } _ { \ j } ( t ) = \frac { 1 } { L } \int _ { 0 } ^ { L } U ( \boldsymbol { x } , t ) e ^ { - \imath q \boldsymbol { \jmath } x } d \boldsymbol { x } , \qquad U ( \boldsymbol { x } , t ) = \sum _ { \boldsymbol { \jmath } \in \mathbb { Z } } \widehat { U } _ { \ j } ( t ) e ^ { \imath q \boldsymbol { \jmath } x } ,
$$

so that (10.9) takes the form of an infinite dimensional ordinary differential equation

$$
\widehat { U } _ { \jmath } ^ { \prime } = \big ( ( q j ) ^ { 2 } - ( q j ) ^ { 4 } \big ) \widehat { U } _ { \jmath } - \frac { \imath q j } { 2 } ( \widehat { U \cdot U } ) _ { \jmath } .
$$

We truncate this system as follows: for a fixed $N$ ,say $N = 1 0 2 4$ , we consider the $N$ -periodic sequence $u ( t ) = \{ u _ { \ j } ( t ) \}$ solving the ordinary differential equation

$$
u ^ { \prime } = ( d ^ { 2 } - d ^ { 4 } ) u - \frac { i d } { 2 } \mathcal { F } _ { N } \big ( \mathcal { F } _ { N } ^ { - 1 } u \cdot \mathcal { F } _ { N } ^ { - 1 } u \big ) ,
$$

where $d$ denotes the $N$ -periodic sequence given by $d _ { j } = q j$ for $| j | < N / 2$ and $d _ { N / 2 } = 0$ ,and the product of sequences in (10.11) is componentwise. The discrete

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/d348a2fa54c6842f5b15655b14f6a30e9492d4a2ef64cafca1b8169fd3b878ce.jpg)  
Fig.10.4. Solution of Kuramoto-Sivashinsky equation

Fourier transform $\mathcal { F } _ { N }$ can be computed by FFT. From the fact that $U ( x , t )$ is real it follows that the sequence $u$ is hermitian, i.e., $u _ { - \jmath } = \overline { { u } } _ { \jmath }$ ．Hence, the routine REALFT from Press,Flannery, Teukolsky& Vetterling(1986,1989),Chapter 12,is best suited for computing the right-hand side of (10.11). Since $d _ { 0 } = d _ { N / 2 } = 0$ ,the components $u _ { 0 } ( t )$ and $u _ { N / 2 } ( t )$ are constant and need not be integrated. We thus are concerned with an ordinary differential equation of real dimension $N - 2 =$ 1022.As initial values we take the discrete Fourier transform of $\left\{ U ( j L / N , 0 ) \right\}$ with the $( N / 2 )$ th component put to zero. In our tests we solve the differential equation (10.11) on the interval $0 \leq t \leq 1 0 0$ (see Fig. 10.4).

It can be seen from Fig.10.5 that the Fourier modes tend to zero for $j  \infty$ ， behave chaotically, and, by computing their mean values over a long period, that the modes for $q j \approx \sqrt { 2 } / 2$ are dominant.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/dbbf5fa2b0fa728b16997d9098de68a3f4c0372156f04b86381ea63bfe59df31.jpg)  
Fig.10.5. Fourier modes for Kuramoto-Sivashinsky equation

BECKDO - the Becker-Döring model describes the dynamics of a system with a large number of identical particles which can coagulate to form clusters. We let $y _ { k }$ denote the expected number of $k$ -particle clusters per unit volume. Assuming that clusters can gain or loose only single particles, we are led to the system

$$
\begin{array} { l } { { y _ { 1 } ^ { \prime } = - J _ { 1 } - \displaystyle \sum _ { k = 1 } ^ { N - 1 } J _ { k } , \qquad y _ { N } ^ { \prime } = J _ { N - 1 } } } \\ { { y _ { k } ^ { \prime } = J _ { k - 1 } - J _ { k } , \qquad k = 2 , 3 , \ldots , N - 1 , } } \end{array}
$$

where $J _ { k } = y _ { 1 } y _ { k } - b _ { k + 1 } y _ { k + 1 }$ and $b _ { k + 1 } = \exp \left( k ^ { 2 / 3 } - ( k - 1 ) ^ { 2 / 3 } \right)$ . For a detailed description of this system we refer to the article by Carr, Duncan & Walshaw (1995). This equation is especially interesting because of its metastability (extremely slow variations in the solution over very long time intervals; see Fig. 10.6).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/e55d64b0a0471e1587715aacf370dfab2daa8de82579f8ab2c9c0307b1cdc642.jpg)  
Fig.10.6. Solutions of Becker-Doring equation (10.12)

As initial condition we take

$$
y _ { 1 } ( 0 ) = \varrho , \qquad y _ { k } ( 0 ) = 0 \qquad \mathrm { f o r } \quad k = 2 , \ldots , N
$$

(no clusters at the beginning). It can be seen by differentiation that the density (total number of particles per unit volume)

$$
\sum _ { k = 1 } ^ { N } k y _ { k } \quad ( = \varrho )
$$

is an invariant of the system (10.12). Most numerical schemes (in particular Runge-Kutta methods and multistep methods) preserve automatically such linear invariants in the absence of round-off errors. Whenever the relation (10.14) is not satisfactorily preserved, there is the possibility to re-establish it during the computations by projections (see “differential equations with invariants", Sect.VI1.2). This precautionary measure was not used in the subsequent numerical tests.

In order to be able to observe the metastable states of the system, the dimension $N$ has to be sufficiently large. Following the experiments of Carr, Duncan &

Walshaw (1995) we take $N = 5 0 0 0$ and $\varrho = 7 . 5$ , and consider the solution on the interval $0 \leq t \leq 1 0 ^ { 1 5 }$ . We compare the errors at $x _ { \mathrm { o u t } } = 1 , 1 0 , 1 0 ^ { 2 } , 1 0 ^ { 3 } , \dotsc , 1 0 ^ { 1 5 }$

The Jacobian of this system is tri-diagonal with an additional non-zero first row and a non-zero first column. A Gershgorin test reveals that its eigenvalues can not go,except for the initial phase,beyond $- 1 0$ . Stiffness, in this example,is therefore not created by large eigenvalues of $J$ , but by the extremely long integration interval.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/54f99ff73ba613b31db1b279569aea337182776c9c6dd7452f70621a288b9298.jpg)  
Fig.10.7. Solution of Brusselator in 2 dimensions

BRUSS-2D-the two-dimensional Brusselator reaction-diffusion problem of Sect.

$$
\begin{array} { l } { \displaystyle \frac { \partial u } { \partial t } = 1 + u ^ { 2 } v - 4 . 4 u + \alpha \Big ( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } \Big ) + f ( x , y , t ) } \\ { \displaystyle \frac { \partial v } { \partial t } = 3 . 4 u - u ^ { 2 } v + \alpha \Big ( \frac { \partial ^ { 2 } v } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } v } { \partial y ^ { 2 } } \Big ) } \end{array}
$$

in its discretized form (II.10.14), but this time we make the problem stiff by increasing the coefficient $\alpha$ (which was 0.002） to $\alpha = 0 . 1$ and by increasing the number of grid points to $N = 1 2 8$ . This gives an ordinary differential equation of dimension $2 N ^ { 2 } = 3 2 7 6 8$ . The initial conditions, chosen here as

$$
u ( x , y , 0 ) = 2 2 \cdot y ( 1 - y ) ^ { 3 / 2 } , \qquad v ( x , y , 0 ) = 2 7 \cdot x ( 1 - x ) ^ { 3 / 2 } ,
$$

are quickly wiped out by the strong diffusion (see Fig.10.7 for $t = 1$ ), we therefore suppose that the inhomogeneity $f ( x , y , t )$ defined by

$$
f ( x , y , t ) = \left\{ \begin{array} { l l } { 5 } & { \mathrm { i f ~ } ( x - 0 . 3 ) ^ { 2 } + ( y - 0 . 6 ) ^ { 2 } \leq 0 . 1 ^ { 2 } \mathrm { ~ a n d ~ } t \geq 1 . 1 } \\ { 0 } & { \mathrm { e l s e } } \end{array} \right.
$$

models an extra addition of substance $u$ in a small disc. In order to be able to solve the linear algebra comfortably by a double FFT routine we replace the Neumann conditions of Sect.I.10 by periodic boundary conditions

$$
u ( x + 1 , y , t ) = u ( x , y , t ) , \qquad u ( x , y + 1 , t ) = u ( x , y , t ) .
$$

As output points we choose $x _ { \mathrm { o u t } } = 1 . 5$ and 11.5.

# Results and Discussion

For each of these examples we have computed very carefully the exact solution at the specified output points. Then, the above codes have been applied with many different tolerances

$$
T o l = 1 0 ^ { - 2 - m / 4 } , \qquad m = 0 , 1 , 2 , \ldots , 3 2 .
$$

More precisely, we set the relative error tolerance to be $R t o l = T o l$ and the absolute error tolerance $A t o l = 1 0 ^ { - 6 } \cdot T o$ l for the problems OREGO and ROBER, $A t o l =$ $1 0 ^ { - 4 } \cdot T o l$ for HIRES, $A t o l = 1 0 ^ { - 3 } \cdot T o l$ for PLATE and BECKDO, $A t o l = 1 . 7 \cdot 1 0 ^ { - 2 4 }$ for E5, and $A t o l = T o l$ for all other problems. Several codes returned numerical re-sults which were considerably less precise than the required precision, while other methods turned out to be more reliable. As a reasonable measure of efficiency we have therefore chosen to compare

- the actual error (a norm taken over all components and all output points) - the computing time (of a SUN Sparc 20 Workstation) in seconds.

The obtained data are then displayed as a polygonal line in a “precision-work diagram’ in double logarithmic scales. The integer-exponent tolerances $1 0 ^ { - 2 }$ ， $1 0 ^ { - 3 }$ ， $1 0 ^ { - 4 }$ ,... are displayed as enlarged symbols. The symbol for $T o l = 1 0 ^ { - 5 }$ is specially distinguished by its gray colour. The more this line is to the right, the higher was the obtained precision; the higher this line is to the top, the slower was the code. The“slope” of the curve expresses the (effective) order of the formula: lower order methods are steeper than higher order methods. The results of the above codes on the 12 test examples are displayed in Figs.10.8 and 10.9.

VDPOL,ROBER, OREGO — are very stiff problems of small dimension. We see from Fig.10.8 that the Rosenbrock code RODAS is best for low tolerances ( $1 0 ^ { - 2 }$ to $1 0 ^ { - 5 }$ ),whereas the extrapolation code SEULEX is superiour for stringent tolerances.Due to the cheapness of the function evaluations the multistep code LSODE requires in general slightly more computing time than the one-step codes. We also remark that for a given tolerance (the position of the gray symbol for $T o l = 1 0 ^ { - 5 }$ ） the code RADAU5 gives the precisest result, followed by RODAS, SEULEX，and LSODE.

HIRES -- this problem is less stiff and can also be solved by explicit methods. The computing times for the explicit code DOPRI5 are initially perfectly horizontal. This is, of course, no surprise, because the step size is restricted by stability. The (explicit, but stabilized) Runge-Kutta-Chebyshev code RKC shows a considerable improvement over DOPRI5 for low tolerances. The stiff codes are still more efficient.

E5 — is a stiff and badly scaled problem, which is integrated over a very long time. Codes cannot work correctly, if the absolute tolerance Atol is too large. The codes RODAS (for low tolerances） and RADAU5 (for $T o l \le 1 0 ^ { - 4 } $ ） give the best results. LSODE works safely only for $T o l \le 1 0 ^ { - 5 }$ ，whereas SEULEX has problems with round-off errors at high precision.

PLATE and BEAM—are both problems of the type $y ^ { \prime \prime } { = } f ( x , y , y ^ { \prime } )$ ,implemented as the first order system $y \prime = v$ ， $v ^ { \prime } = f ( x , y , v )$ . For stiff codes the linear systems to be solved have a matrix of the form

$$
\left( \begin{array} { c c } { { \alpha I } } & { { I } } \\ { { B } } & { { C } } \end{array} \right)
$$

(where $I$ is the identity matrix). Using the option IWORK $( 9 ) = 1 1 / 2$ (where $N$ is the dimension of the first order system) our codes do the first $N / 2$ elimination sweeps analytically and the dimension of the linear system is halved. Without this option, the computing times for the codes RADAU5, RODAS, and SEULEX would be larger by a factor of about 3.0, 1.7,and 2.6,respectively (these numbers are for the BEAM problem at $T o l = 1 0 ^ { - 5 }$ ). We did not include here the results of LSODE, for which we did not have an easy possibility for such a reduction. For the PLATE problem we also exploited the banded structure of $\partial f / \partial y$ and $\partial f / \partial v$ by puting ML $J \mathbb { A } \mathbb { C } { = } 1 6$ and MUJ $A C = 1 6$ .

For both problems the explicit code DOPRI5 was applicable too.A curious phenomenon arose for DOPRI5 at the PLATE problem: as expected, for low tolerance requirements $( T o l \ge 1 0 ^ { - 5 } )$ ， the code appeared to be restricted by stability， gave computing times independent of $T o l$ and issued the message “the problem seems to be stiff". But for more stringent tolerances the code was restricted by precision, with computing times unexpectedly high above those of the implicit code RADAU5. The analysis of Sect. IV.15 for the Prothero & Robinson problem (15.1） gives an explanation for this fact. We see that stiffproblems not only create loss of stability, but also loss of precision for explicit integrators.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/f2d999e350d9c330cfd15705659adbb416e0b74b99f4ee984b84c8bce85e6fca.jpg)  
Fig.10.8. Work-precision diagrams for problems of dimension 2 to 80

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/e04af4214765435cd0dce3781292b98cb89d7410867f466504bcc057adc74322.jpg)  
Fig.10.9. Work-precision diagrams for problems of dimension 80 to 32768

Especially for the BEAM problem,a problem with expensive linear algebra, the efficiency of the codes can be considerably increased by tuning the parameters. If, for the integration with RADAU5, we put

$$
\begin{array} { l l } { { \sf W O R K ( 3 ) = 0 . 1 } } & { { \mathrm { ( J a c o b i a n ~ l e s s ~ o f t e n ~ r e c o m p u t e d ) } } } \\ { { \sf W O R K ( 4 ) = 0 . 3 } } & { { \mathrm { ( N e w t o n ~ i t e r a t i o n s ~ s t o p p e d ~ e a r l i e r ) } } } \\ { { \sf N U R K ( 5 ) = 0 . 9 9 } } & { { \mathrm { ( S t e p ~ s i z e ~ c h a n g e d ~ l e s s ~ o f t e n , } } } \\ { { \sf W O R K ( 6 ) = 2 . } } & { { \mathrm { d e c r e a s i n g ~ n u m b e r ~ o f ~ L U \mathrm { - } d e c o m p o s i t i o n s . } } } \end{array}
$$

then the computing time decreases by a factor between 2 and 5. Fig.10.9 shows the spectacular improvement of this “tuned" run.

CUSP — the Jacobian of this problem is of the form

$$
J = \left( \begin{array} { c c c c } { { A _ { 1 } } } & { { B _ { 1 } } } & { { } } & { { D _ { 1 } } } \\ { { C _ { 2 } } } & { { A _ { 2 } } } & { { \ddots } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { B _ { N - 1 } } } \\ { { D _ { N } } } & { { } } & { { C _ { N } } } & { { A _ { N } } } \end{array} \right)
$$

where $A _ { \ i _ { 2 } } , B _ { \ i } , C _ { \ i } , D _ { \ i }$ are $3 \times 3$ matrices,and an efficient solution of the linear system needs a special treatment (see Exercise 1). However the considered methods, with the exception of the Rosenbrock methods, do not require an exact Jacobian. Therefore,an easy possibility for a considerable reduction of computing time is simply to use the codes in the banded version by putting $M I = M U = 3$ The $D _ { 1 }$ and $D _ { N }$ are neglected and we obtain the computing times displayed in Fig.10.9. If the Jacobian were treated as a full matrix, the computing times would increase by a factor of 8.3, 6.6,and 4.8 for the codes RADAU5, SEULEX, and LSODE, respectively (these numbers are for $T o l = 1 0 ^ { - 5 }$ ). The explicit code RKC gives excellent results for low precision, whereas the results of DOPRI5 (more than 30 seconds) are outside of the picture.

BRUSS - for this one-dimensional reaction-diffusion problem the linear algebra is done in the “banded” version with “analytical Jacobian". The problem is very stiff (large diffusion constant and small $\Delta x )$ and an explicit method, such as DO-PRI5,would require close to 600o0 steps of integration. The code RKC works well, although less efficiently than the stiff integrators.

KS 一 the solution of this problem is sensitive with respect to changes in the initial values,a phenomenon already encountered in the LRNZ problem of Sect. I.10. Similarly as there, the precision increases only for $T o l$ beyond a certain threshold. The Jacobian of this problem is full. Numerical experiments revealed that the codes worked best when the Jacobian is replaced by a diagonal matrix with $( q j ) ^ { 2 } - ( q j ) ^ { 4 }$ in its $j$ th entry. Rosenbrock methods,which require an exact Jacobian,are not efficient here. The explicit codes RKC and DOPRI5 need too much computing time.

BECKDO- for this problem,the stiff codes (the only ones which work) require the solution of linear systems of the form

$$
\left( \begin{array} { c c } { { u } } & { { v ^ { T } } } \\ { { w } } & { { T } } \end{array} \right) \left( \begin{array} { l } { { x } } \\ { { y } } \end{array} \right) = \left( \begin{array} { l } { { a } } \\ { { b } } \end{array} \right) ,
$$

where $v , w , b$ are $( n - 1 )$ -dimensional vectors and $T$ is a tri-diagonal matrix. Since the linear algebra routines are completely separated from the codes RADAU5, RODAS and SEULEX, it is easy to replace these routines by a special program which solves (10.19) efficiently as follows

$$
\begin{array} { r l } & { x = \left( a - v ^ { T } T ^ { - 1 } b \right) / \left( u - v ^ { T } T ^ { - 1 } w \right) } \\ & { y = T ^ { - 1 } b - x T ^ { - 1 } w . } \end{array}
$$

It is not necessary to alter the stiff integrator itself.

Fig.10.9 shows that, as usual, RODAS is best for low tolerances and RADAU5 is preferable for high precision. Not as usual is the fact that RODAS performs very badly for stringent tolerances. We explain this by the fact that the linear system (10.19) is sensitive to round-off errors, or, as Wilkinson would turn it, delivers a solution for a wrong Jacobian. Thus, the order of the Rosenbrock method drops to 1.

BRUSS-2D — due to its large dimension ( $' n = 2 \cdot 1 2 8 ^ { 2 } = 3 2 7 6 8 \rangle$ ，this problem makes no sense in full or even banded linear algebra. We therefore solved the linear equations (in the codes with separated linear algebra, see the corresponding remarks in the BECKDO problem) by FFT methods, taking into account only the(stiff) diffusion terms and neglecting the (in this problem non-stiff) reaction terms. The FFT codes used were those of Press,Flannery, Teukolsky & Vetterling (1986,1989) in the chapter on partial differential equations. A special advantage of the Radau method is here that the complex algebra, which is anyway used in FFT, crunches the complex eigenvalues of the Runge-Kutta matrix without further harm.

For this problem, which is a typical parabolic partial differential equation with non-stiff nonlinearities, we have made a detailed comparison of the performances of the implicit code RADAU5, the “stabilized’ explicit code RKC,and the explicit code DOPRI5, in dependence of the discretization parameter $\Delta x = \Delta y = 1 / N$ and the diffusion parameter $\alpha$ (see Eqs.(10.15) and (II.10.14)). The results (number of function calls and computing times) are displayed in Table 10.1, where the best performances are displayed in boldface characters. We can see how the olympic fire goes over from DOPRI5, which is best for low stiffness $( \alpha N ^ { 2 } \le 1 )$ , by increasing the stiffness first to RKC,and then (for $\alpha N ^ { 2 } \geq 1 0 0 0 )$ to the implicit RADAU5 code. We also observe that the number of function evaluations is nearly independent of the stiffness for RADAU5, behaves like $C o n s t \cdot \sqrt { \alpha } \cdot N$ for RKC, and like Const · $\alpha \cdot N ^ { 2 }$ for DOPRI5.

Comparisons Between Codes of the Same Type. Figs.10.8 and 10.9, which are a sort of “Final Competition of Wimbledon”, contain only one code from each class of integration methods (Radau methods, Implicit Runge-Kutta, Rosenbrock, and extrapolation methods). Following are some comparisons within each of these classes.

Table 10.1. Function evaluations / computing times at $T o l = 1 0 ^ { - 5 }$   

<table><tr><td rowspan=1 colspan=1>RADAU5</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N = 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N = 128</td><td rowspan=1 colspan=1>N = 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α=10-2α = 10-1α=1</td><td rowspan=1 colspan=1>3372/19.81286/7.71150/6.81195/7.8</td><td rowspan=1 colspan=1>3233/84.91322/36.21131/30.91199/33.0</td><td rowspan=1 colspan=1>3271/413.51295/167.41227/172.31247/177.3</td><td rowspan=1 colspan=1>3290/2215.61381/868.81173/854.91242/945.9</td><td rowspan=1 colspan=1>3261/14902.11380/6459.31204/5664.91258/5961.2</td></tr><tr><td rowspan=1 colspan=1>RKC</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N= 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N= 128</td><td rowspan=1 colspan=1>N = 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α = 10-2α = 10-1α=1</td><td rowspan=1 colspan=1>2367/4.71661/3.21899/3.64013/7.2</td><td rowspan=1 colspan=1>2277/18.61674/13.82823/22.57565/58.9</td><td rowspan=1 colspan=1>2249/76.32078/70.45047/176.814631/503.4</td><td rowspan=1 colspan=1>2311/352.53379/511.59666/1446.229022/4328.8</td><td rowspan=1 colspan=1>2911/1912.06259/4086.918911/12312.2</td></tr><tr><td rowspan=1 colspan=1>DOPRI5</td><td rowspan=1 colspan=1>N=16</td><td rowspan=1 colspan=1>N= 32</td><td rowspan=1 colspan=1>N= 64</td><td rowspan=1 colspan=1>N= 128</td><td rowspan=1 colspan=1>N= 256</td></tr><tr><td rowspan=1 colspan=1>α=10-3α =10-2α =10-1α=1</td><td rowspan=1 colspan=1>976/2.0784/1.64366/9.042832/90.6</td><td rowspan=1 colspan=1>1030/8.51894/15.417176/145.5171010/1505.8</td><td rowspan=1 colspan=1>1408/48.56976/240.668446/2419.7683836/24362.7</td><td rowspan=1 colspan=1>3286/509.427478/4369.6273568/43982.2</td><td rowspan=1 colspan=1>11464/7704.2</td></tr></table>

Radau Methods. For a comparison of Radau methods of various orders (see also the results of Reymond (1989) in the first edition), we have written a code RADAUP, which allows to choose with the help of a method flag IWORK $( 1 1 ) = 3$ ,5,7 to choose between $s = 3 , 5$ ， or 7 (i.e., between orders $p = 5 , 9$ ，or 13). The code is for $s = 3$ mathematically equivalent to RADAU5, but, due to a different coding, slightly slower. We can see in Fig.10.1O how the higher order pays off for higher precision,but for lower precision arise problems due to large step sizes and bad convergence of the Newton iterations.

Implicit Runge-Kutta Methods. It has for a long time been taken for granted that only DIRK and SDIRK methods could be implemented efficiently. Our experience shows that the diagonally implicit method SDIRK4, constructed in Section IV.6, gives rather disappointing results (see Fig. 10.11). An exception is the BEAM problem with its, microscopically, highly oscillatory solutions. Since the code SDIRK4 has not the option for “second order" linear algebra, we have also applied RADAU5 without this option. The computing times for RADAU5 are therefore not the same as in Fig. 10.9.

Rosenbrock Methods. There is usually not much difference between the performance of the different Rosenbrock methods (see Fig.10.12). In spite of their larger number of stages, the codes RODAs5 (order 5）and RODAS (order 4） give often the best results. Among the 4th order “classical” Rosenbrok methods of Table 7.2 the best is in general “method $2 ^ { \mathfrak { s } }$ with its small error constant; it fails completely, however,on the Beam problem due to lack of $A$ -stability."Method $6 ^ { \circ }$ corresponds to the choice of coefficients which give an $L$ -stable method.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/00071c3ad6adbf6d7ceb2eb3e95c867f522a2d39ba25c2e7ab4b9ef3ecaa9819.jpg)  
Fig.10.10. Comparison between Radau codes

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/daea7d9e0c3af3b391e0bcc9bffc40c15ca246d94dc8c61da17be46c93f0432f.jpg)  
Fig.10.11. Comparison between implicit Runge-Kutta codes

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/15ec86b0617ac9571ee934b3d0048a3a2420e8a7b2d7d14f560bd3b8b9ddae53.jpg)  
Fig.10.12. Comparison between Rosenbrock codes

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/7ee35b4010c72ed892ebceb686a228335deb5718da721e6dd655db0e4a501aef.jpg)  
Fig.10.13. Comparison between extrapolation codes

Extrapolation Methods. The code SODEX,which is based on an $h ^ { 2 }$ -extrapolation of the semi-implicit midpoint rule, is clearly superiour to SEULEX for low precision (see Fig.10.13). The opposite situation appears for more stringent tolerances; here we observe an order reduction phenomenon, which is explained in Sect. VI.5 below. We have also included in these tests the results of the code EULSIM by Deuflhard, Novak&Poehle (poehle $@$ sc.zib-berlin.de) which is another implementation of the extrapolated semi-implicit Euler method, with a different stepsize sequence.

Chebyshev Methods. During the final realization of these experiments we have received a code DUMKA3 (written by A. Medovikov, nucrect $@$ inm.ras.ru) which implements an extension of the optimal Chebyshev methods of Lebedev (see Sect. IV.2) to third order. This code is still in a very experimental stage,but the results, presented in Fig. 10.14, are very promising.

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/6f23601cde27d38e3ee525461a4e83a22cba36ebb864dc456cef0ab8ce1dcc80.jpg)  
Fig.10.14. Comparison between Chebyshev codes and RADAU5

# Partitioning and Projection Methods

Most codes for solving stiff systems ... spend most of their time solving systems of linear equations ...

(Watkins & HansonSmith 1983)

Further spectacular reductions of the work for the linear algebra are often possible. One of the oldest ideas is to partition a stiff system into a (hopefully) small stiff system and a large nonstiff part,

$$
\begin{array} { l l } { { { y } _ { a } ^ { \prime } = f _ { a } \left( y _ { a } , y _ { b } \right) \quad \quad } } & { { ( \mathrm { s t i f f } ) } } \\ { { { y } _ { b } ^ { \prime } = f _ { b } \left( y _ { a } , y _ { b } \right) \quad \quad } } & { { ( \mathrm { n o n s t i f f } ) , } } \end{array}
$$

so that the two systems can be treated by two different methods, one implicit and the other explicit (e.g. Hofer 1976). The theory of $P$ -series in Sect.II.14 had its origin in the study of the order properties of such methods. A difficulty of this approach is,of course,to decide which equations should be the stiff ones. Further, stiffness may affect subspaces which are not parallel to the coordinate axes. We shall therefore turn our attention to procedures which do not adapt the underlying numerical method to the partitioning,but the linear algebra only. An excellent survey of the older literature on these methods is given by Soderlind (1981). The following definition describes an especially promising class of problems:

Definition10.1 (Bjorck 1983,1984). The system $y ^ { \prime } = f ( x , y )$ is called separably stiff at a position $x _ { 0 } , y _ { 0 }$ if the Jacobian $\begin{array} { r } { \dot { J _ { \mathrm { ~ } } } = \frac { \partial f } { \partial y } ( \bar { x } _ { 0 } , y _ { 0 } ) } \end{array}$ possesses $k < n$ eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ such that

$$
\operatorname* { m i n } _ { 1 \leq i \leq k } | \lambda _ { \iota } | > > \operatorname* { m a x } _ { k + 1 \leq i \leq n } | \lambda _ { i } | .
$$

The eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ are called the stiff eigenvalues and

$$
\mu = \operatorname* { m i n } _ { 1 \leq i \leq k } | \lambda _ { i } | { \bf \mu } / \operatorname* { m a x } _ { k + 1 \leq \imath \leq n } | \lambda _ { i } |
$$

the relative separation. The space $D$ spanned by the $^ { s t }$ iff eigenvectors is called the dominant invariant subspace.

For example, the Robertson problem (10.2) possesses only one stiff eigenvalue (close to -20oO),and is therefore separably stiff with $k = 1$ . The CUSP problem (10.8'）of dimension 96 has 32 large eigenvalues which range,except for transient phases,between $- 2 0 0 0 0$ and -6oooo.All other eigenvalues satisfy approximately $| \lambda | < 3 0$ ． This problem is,in fact,a singular perturbation problem (see Sect.VI.1),and such problems are all separably stiff. The other large problems of this section have eigenvalues scattered all around. A.R. Curtis' study (1983) points out that in practical problems separably stiff problems are rather seldom.

The Method of Gear and Saad. Implicit methods such as (transformed) Runge-Kutta or multistep formulas require the solution of a linear system (where we denote,as usual in linear algebra, the unknown vector by $x$ ）

$$
A x = b \qquad { \mathrm { w h e r e } } \qquad A = { \frac { 1 } { h \gamma } } I - J
$$

with residual $r = b - A x$ . We choose $k$ (usually) orthogonal vectors $q _ { 1 } , \ldots , q _ { k }$ in such a way that the span $\{ q _ { 1 } , \dots , q _ { k } \} = \widetilde { \cal D }$ is an approximation to the dominant subspace $D$ , and denote by $Q$ the $k \times n$ -matrix formed by the columns $q _ { j }$ ，

$$
Q = ( q _ { 1 } , \dots , q _ { k } ) .
$$

There are now several possibilities for replacing the solution $x$ of (10.23) by an approximate solution $\bar { \tilde { x } _ { \mathrm { \ell } } } \in \tilde { D }$ . One of the most natural is to require (Saad 1981, Gear & Saad 1983; in fact,Galerkin 1915) that the residual of $\widetilde { x }$ ，

$$
\widetilde { r } = b - A \widetilde { x } = A ( x - \widetilde { x } ) ,
$$

be orthogonal to $\widetilde { D }$ , i.e., that $Q ^ { T } ( b - A \widetilde { x } ) = 0$ . If we write $\widetilde { x }$ in the basis of (10.24) as $\widetilde { x } = Q \widetilde { y }$ , this yields

$$
\begin{array} { r } { H \widetilde { y } = Q ^ { T } b , } \end{array}
$$

where

$$
H = Q ^ { T } A Q \qquad \mathrm { o r } \qquad Q H = A Q ,
$$

which means that we have to solve a linear system of dimension $k$ with matrix $H$ . A particularly good choice for $\widetilde { D }$ is a Krylov subspace spanned by an arbitrary vector $r _ { 0 }$ (usually the residual of a well chosen initial approximation $x _ { 0 }$ ），

$$
{ \widetilde D } = \operatorname { s p a n } \{ r _ { 0 } , A r _ { 0 } , A ^ { 2 } r _ { 0 } , \ldots , A ^ { k - 1 } r _ { 0 } \} .
$$

The vectors (10.28) constitute the sequence created by the well-known power me-thod. Therefore, in the case of a separably stiff system, as analyzed by D.J. Higham (1989), the space $\widetilde { D }$ approaches the space $D$ extremely well as soon as its dimension is sufficiently high. In the Arnoldi process (Arnoldi 1951) the vectors of (10.28) are successively orthonormalized (Gram-Schmidt) as

$$
\begin{array} { r l r l } & { q _ { 1 } = r _ { 0 } / \Vert r _ { 0 } \Vert } \\ & { \widehat { q } _ { 2 } = A q _ { 1 } - h _ { 1 1 } q _ { 1 } , } & & { q _ { 2 } = \widehat { q } _ { 2 } / h _ { 2 1 } \quad \mathrm { w i t h } \quad h _ { 2 1 } = \Vert \widehat { q } _ { 2 } \Vert } \end{array}
$$

and so on,and we see that

$$
\begin{array} { l } { { A q _ { 1 } = h _ { 2 1 } q _ { 2 } + h _ { 1 1 } q _ { 1 } } } \\ { { A q _ { 2 } = h _ { 3 2 } q _ { 3 } + h _ { 2 2 } q _ { 2 } + h _ { 1 2 } q _ { 1 } } } \\ { { \ldots } } \end{array}
$$

which,compared to (10.28),shows that $H$ is Hessenberg. For $A$ symmetric, $H$ is also symmetric, hence tridiagonal, so that the method is equivalent to the conjugate gradient method.

Two features are important for this method: Firstly, the matrix $A$ need never be computed nor stored. All that is needed are the matrix-vector multiplications in (10.29),which can be obtained from the “directional derivative"

$$
J v \approx [ f ( x , y + \delta v ) - f ( x , y ) ] / \delta .
$$

Several people therefore call such methods “matrix-free". Secondly, the dimension $k$ does not have to be known: one simply computes one column of $H$ after the other and periodically estimates the residual. As soon as this estimate is small enough (or $k$ becomes too large) the algorithm stops. We also mention two variants of the method:

1. (Gear & Saad 1983, p. 595). Before starting the computation of the Krylov subspace, perform some initial iteration of the power method on the initial vector $r _ { 0 }$ ,using either the matrix $A$ or the matrix $J$ . Lopez & Trigiante （1989) report excellent numerical results for this procedure.

2. Incomplete Orthogonalization (Saad 1982). The new vector $A q _ { \jmath }$ is only orthogonalized against the previous $p$ vectors, where $p$ is some small integer. This makes $H$ a banded matrix and saves computing time and memory. For symmetric matrices, the ideal choice is of course $p = 2$ , for matrices more and more unsymmetric $p$ usually is increased to 10 or 15.

The EKBWH-Method (this tongue-twister stands for Enright, Kamel, Bjorck, Watkins and HansonSmith). Here, the matrices $A$ (and $J$ ) in (10.23)are replaced by approximations

$$
\stackrel { \sim } { A } = \frac { 1 } { h \gamma } I - \stackrel { \sim } { J }
$$

where $\widetilde { J }$ should approach $J$ suficiently well and the matrix $\widetilde { A }$ be relatively easy to invert. $\widetilde { J }$ is determined as follows: Complete (theoretically) the vectors (10.24) to an orthogonal basis $( Q , { \widehat { Q } } )$ of $\mathbb { R } ^ { n }$ . In the new basis $J$ becomes

$$
\left( { \begin{array} { l } { Q ^ { T } } \\ { { \widehat { Q } } ^ { T } } \end{array} } \right) J \left( Q , { \widehat { Q } } \right) = \left( { \begin{array} { l l } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { T _ { 2 1 } } & { T _ { 2 2 } } \end{array} } \right)
$$

and we have

$$
Q ^ { T } J Q = T _ { 1 1 } .
$$

If span $Q = \widetilde { D }$ approaches $D$ , then $T _ { 1 1 }$ will contain the stiff eigenvalues and $T _ { 2 1 }$ will tend to zero. If $\widetilde { D } = D$ exactly, then $T _ { 2 1 } = 0$ and (10.32) is a block-Schur decomposition of $J$ . For separably stiff systems $\| T _ { 2 2 } \|$ will become small compared to $( h \gamma ) ^ { - 1 }$ and we define

$$
\widetilde { J } = ( Q , \widehat { Q } ) \left( \begin{array} { c c } { { T _ { 1 1 } } } & { { T _ { 1 2 } } } \\ { { 0 } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { Q ^ { T } } } \\ { { \widehat { Q } ^ { T } } } \end{array} \right) = Q ( T _ { 1 1 } Q ^ { T } + T _ { 1 2 } \widehat { Q } ^ { T } ) \stackrel { ( 1 0 . 3 2 ) } { = } Q Q ^ { T } J .
$$

This shows $\widetilde { J }$ to be the orthogonal projection of $J$ onto $\widetilde { D }$ . The inverse of $\widetilde { A }$ is computed by developing $( I - B ) ^ { - 1 } = I + B + B ^ { 2 } + \dots .$ as a geometric series

$$
\begin{array} { r l } & { \widetilde { A } ^ { - 1 } = h \gamma \big ( I - h \gamma Q Q ^ { T } J \big ) ^ { - 1 } } \\ & { \quad \quad = h \gamma \big ( I + h \gamma Q Q ^ { T } J + h ^ { 2 } \gamma ^ { 2 } Q \underbrace { Q ^ { T } J Q } _ { T _ { 1 1 } } Q ^ { T } J + \dots \big ) } \\ & { \quad \quad = h \gamma \big ( I + Q ( h \gamma I + h ^ { 2 } \gamma ^ { 2 } T _ { 1 1 } + h ^ { 3 } \gamma ^ { 3 } T _ { 1 1 } ^ { 2 } + \dots ) Q ^ { T } J \big ) } \\ & { \quad \quad = h \gamma \big ( I + Q \big ( \frac { 1 } { h \gamma } I - T _ { 1 1 } \big ) ^ { - 1 } Q ^ { T } J \big ) } \end{array}
$$

which only requires the solution of the “small” system with matrix $\left( I / h \gamma - T _ { 1 1 } \right)$ (the last expression is called the Sherman-Morrison-Woodbury formula).

Choice of $Q$ ：

-Björck(1983) computes the precise span of $D$ , by Householder transforms followed by block- $Q R$ iterations. For separably stiff systems the block $T _ { 2 1 }$ converges to zero linearly with ratio $\mu ^ { - 1 }$ so that usually 2 or 3 iterations are sufficient. A disadvantage of the method is that an estimate for the dimension $k$ of $D$ must be known in advance.

-Enright & Kamel（1979) transform $J$ to Hessenberg form and stop the transformations when $\| T _ { 2 1 } \| + \| T _ { 2 2 } \|$ become suficiently smal (remark that $T _ { 2 1 }$ is non zero in its last column only). Thus the dimension $k$ can be discovered dynamically. Enright & Kamel combine the Householder reflexions with a pivoting strategy and repeated row & column permutations in order to make $T _ { 2 2 }$ small as fast as possible. It was first observed numerically (by Carlsson) and then shown theoretically (Soderlind 1981) that this pivoting strategy “needs some comments": if we start from (10.32),by knowing that

$$
\left( \begin{array} { c c } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { T _ { 2 1 } } & { T _ { 2 2 } } \end{array} \right)
$$

is Hessenberg in its frst $k$ columns, (with $h _ { 2 1 } \neq 0 , h _ { 3 2 } \neq 0 , \ldots )$ and do the analysis of formulas (10.29) backwards,we see that the space $\widetilde { D }$ for the Enright & Kamel method is a Krylov subspace created by $q _ { 1 }$ (D.J. Higham 1989). Thus only the first permutation influences the result.

- Watkins & HansonSmith (1983) start from an arbitrary $Q ^ { ( 0 ) }$ followed by several steps of the block power method

$$
J Q ^ { ( \imath ) } = Q ^ { ( \imath + 1 ) } R ^ { ( \imath + 1 ) }
$$

where $R ^ { ( i + 1 ) }$ re-orthogonalizes the vectors of the product $J Q ^ { ( \imath ) }$ . A great advantage of this procedure is that no large matrix needs to be computed nor stored. The formulas (10.35) as well as (10.34) only contain matrix-vector products which are computed by (10.30). The disadvantage is that the dimension of the space must be known.

Stopping Criteria. The above methods need a criterion on the goodness of the approximation $\widetilde { J }$ to decide whether the dimension $k$ is sufficient. Suppose that we solve the linear equation (10.23) by a modified Newton correction which uses $\tilde { A }$ as “approximate Jacobian"

$$
\widetilde { x } = x _ { 0 } + \widetilde { A } ^ { - 1 } \big ( b - A x _ { 0 } \big ) ,
$$

then the convergence of this iteration is governed by the condition

$$
\varrho \big ( I - \widetilde { A } ^ { - 1 } A \big ) = \varrho \big ( \widetilde { A } ^ { - 1 } \big ( \widetilde { A } - A \big ) \big ) = \varrho \big ( \widetilde { A } ^ { - 1 } \big ( J - \widetilde { J } \big ) \big ) < 1 .
$$

A reasonable condition is therefore that the spectral radius $\varrho$ of $\widetilde { A } ^ { - 1 } ( J - \widetilde { J } )$ is plainly smaller than 1. Let us compute this value for the Bjork method ( $( T _ { 2 1 } = 0$ ： since the eigenvalues of a matrix $C$ are invariant under the similarity transforma-

tion $T ^ { - 1 } C T$ , we have

$$
\begin{array} { r l } & { \varrho \left( \widetilde { A } ^ { - 1 } ( J - \widetilde { J } ) \right) = \varrho \left( \left( \frac { 1 } { h \gamma } I - \left( \begin{array} { c c } { T _ { 1 1 } } & { T _ { 1 2 } } \\ { 0 } & { 0 } \end{array} \right) \right) ^ { - 1 } \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { T _ { 2 2 } } \end{array} \right) \right) } \\ & { \qquad = \varrho \left( \left( \begin{array} { c c } { \left( \frac { 1 } { h \gamma } I - T _ { 1 1 } \right) ^ { - 1 } } & { \times \times \times } \\ { 0 } & { h \gamma I } \end{array} \right) \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { T _ { 2 2 } } \end{array} \right) \right) } \\ & { \qquad = \varrho \left( \left( \begin{array} { c c } { 0 } & { \times \times } \\ { 0 } & { h \gamma T _ { 2 2 } } \end{array} \right) \right) = \varrho ( h \gamma T _ { 2 2 } ) . } \end{array}
$$

In practice, a condition of the form

$$
\| h \gamma T _ { 2 2 } \| < 1 ,
$$

where $\| \cdot \|$ is usually the Frobenius norm $\sqrt { \sum _ { i , j } a _ { \iota j } ^ { 2 } }$ , ensures a reasoable rte f convergence. For an analogous condition in the Enright-Kamel case see Exercise 3 below.

# Exercises

1. (The red-black reduction). The Jacobian matrix of the (periodic) cusp catastrophe model (10.8’) is of the form

$$
\left( \begin{array} { c c c c c } { { A _ { 1 } } } & { { B _ { 1 } } } & { { } } & { { } } & { { C _ { 1 } } } \\ { { C _ { 2 } } } & { { A _ { 2 } } } & { { B _ { 2 } } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { C _ { 2 m - 1 } } } & { { A _ { 2 m - 1 } } } & { { B _ { 2 m - 1 } } } \\ { { B _ { 2 m } } } & { { } } & { { C _ { 2 m } } } & { { A _ { 2 m } } } \end{array} \right)
$$

where $A _ { \imath } , B _ { \imath } , C _ { \imath }$ are $( 3 \times 3 )$ -matrices. Write a solver which solves linear equations with matrix (10.38） using the “red-black ordering reduction". This means that $A _ { 1 } , A _ { 3 } , A _ { 5 } , \dotsc .$ are used as (matricial） pivots to eliminate $C _ { 2 } , C _ { 4 } , \ldots , B _ { 2 } , B _ { 4 } , \ldots$ aboveand belowbyGaussanblock-elimination.Then the resulting system is again of the same structure as (10.38) with halved dimension. If the original system's dimension contains $2 ^ { k }$ as prime factor, this process can be iterated $k$ times. Study the increase of performance which this algorithm allows for the RADAU5 and Rosenbrock codes on model (10.8'). The algorithm is also highly parallelizable.

2. Show by numerical experiments that the circular nerve (10.8') loses its limit cycle when the diffusion coefficient $D$ becomes either too smal (the message does not go across the water fall) or too large (the limit cycle then melts down across the origin).

3.(Stopping criterion for Enright & Kamel method; D.J. Higham 1989). Suppose that the matrix $J$ has been transformed to partial Hessenberg form (see

$$
\left( { \big { \underset { Q ^ { T } } { Q ^ { T } } } } \right) J ( Q , { \widehat { Q } } ) = { \overset { k } { _ { n - k } } } \left( { \begin{array} { l l } { k } & { n - k } \\ { H } & { T _ { 1 2 } } \\ { ( 0 ~ b ) } & { T _ { 2 2 } } \end{array} } \right)
$$

where $H$ is upper Hessenberg and $b$ a column vector. Show that the criterion (10.36) then becomes

$$
\varrho ( h \gamma B ) < 1
$$

where

$$
B = \begin{array} { l r } { { k } } & { { k - 1 } } & { { 1 + n - k } } \\ { { n - k } } & { { \left( \begin{array} { l r } { { 0 } } & { { - h \gamma \overline { { { H } } } ^ { - 1 } T _ { 1 2 } \bigl ( b T _ { 2 2 } \bigr ) } } \\ { { 0 } } & { { \left( b T _ { 2 2 } \right) } } \end{array} \right) } } \end{array}
$$

with $\overline { { H } } = \left( I - h \gamma H \right)$ . Since $\varrho ( B )$ is the same as the spectral radius of its lower $1 + n - k$ by $1 + n - k$ principal submatrix,a sufficient condition for convergence is

$$
 { | h \gamma | } \sqrt {  { | | T _ { 2 2 } | | ^ { 2 } } +  { | | b | | ^ { 2 } } +  { | | y | | ^ { 2 } } } < 1
$$

where $y ^ { T }$ is the $k$ -th row of the matrix $- h \gamma \overline { { H } } ^ { - 1 } T _ { 1 2 } ( b T _ { 2 2 } )$

# IV.11 Contractivity for Linear Problems

He who loves practice without theory is like the sailor who boards ship without a rudder and compass and never knows where he may be cast. (Leonardo da Vinci 1452-1519, cited from M. Kline,Mathematical Thought .. 1972,p. 224)

The stability analysis of the preceeding sections is based on the transformation of the Jacobian $J \approx \partial f / \partial y$ to diagonal form (see Formulas (2.5),(2.6) of Sect.IV.2). Especially for large-dimensional problems, however, the matrix which performs this transformation may be badly conditioned and destroy all the nice estimations which have been obtained.

Example 11.1. The discretization of the hyperbolic problem

$$
{ \frac { \partial u } { \partial t } } = { \frac { \partial u } { \partial x } }
$$

by the method of lines leads to

$$
y ^ { \prime } = A y , \qquad A = \lambda \left( \begin{array} { c c c c c } { { - 1 } } & { { 1 } } & { { } } & { { } } & { { } } \\ { { } } & { { - 1 } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { } } & { { 1 } } \\ { { } } & { { } } & { { } } & { { - 1 } } \end{array} \right) , \qquad \lambda = \frac { 1 } { \Delta x } > 0 .
$$

This matrix has all eigenvalues at $- \lambda$ and the above spectral stability analysis would indicate fast asymptotic convergence to zero. But neither the solution of (11.1)，which just represents a travelling wave, nor the solution of (11.2), if the dimension becomes large,have this property. So our interest in this section is to obtain rigorous bounds for the numerical solution (see (2.3))

$$
y _ { m + 1 } = R ( h A ) y _ { m }
$$

in different norms of $\mathbb { R } ^ { n }$ or $\mathbb { C } ^ { n }$ . Here $R ( z )$ represents the stability function of the method employed. We have from (11.3)

$$
\| y _ { m + 1 } \| \leq \| R ( h A ) \| \cdot \| y _ { m } \|
$$

(see Volume I, Sect.I.9,Formula (9.10)),and contractivity is assured if

$$
\| R ( h A ) \| \leq 1 .
$$

# Euclidean Norms (Theorem of von Neumann)

People in mathematics and science should be reminded that many of the things we take for granted today owe their birth to perhaps one of the most brilliant people of the twentieth century — John von Neumann.

(John Impagliazzo, quoted from SIAM News September 1988)

Let the considered norm be Euclidean with the corresponding scalar product denoted by $\langle \cdot , \cdot \rangle$ . Then, for the solution of $y ^ { \prime } = A y$ we have

$$
{ \frac { d } { d x } } \| y \| ^ { 2 } = { \frac { d } { d x } } \langle y , y \rangle = 2 \mathrm { R e } \langle y , y ^ { \prime } \rangle = 2 \mathrm { R e } \langle y , A y \rangle ,
$$

hence the solutions are decaying in this norm if

$$
\operatorname { R e } \left. y , A y \right. \leq 0 \quad { \mathrm { f o r ~ a l l } } \quad y \in \mathbb { C } ^ { n } .
$$

This result is related to Theorem 10.6 of Sect.I.10, because

$$
\mathrm { R e } \left. y , A y \right. \leq \mu _ { 2 } ( A ) \left\| y \right\| ^ { 2 } ,
$$

where $\mu _ { 2 } ( A )$ is the logarithmic norm of $A$ (Eq. (10.20) of Sect.I.10).

Theorem 11.2. Let the rational function $R ( z )$ be bounded for Re $z \le 0$ and assume that the matrix $A$ satisfies (11.6). Then, in the matrix norm corresponding to the scalar product we have

$$
\| R ( A ) \| \leq \operatorname* { s u p } _ { \operatorname { R e } z \leq 0 } | R ( z ) | .
$$

Remark. This is a finite-dimensional version of a result of J. von Neumann (1951). A short proof is given in Hairer,Bader & Lubich (1982). The idea of the following proof is due to M. Crouzeix (unpublished).

Proof. a) Normal matrices can be transformed to diagonal form by a unitary matrix $Q$ (see Exercise 3 of Section I.12). Hence, $A = Q D Q ^ { * }$ ，where $D =$ diag $\{ \lambda _ { 1 } , \ldots , \lambda _ { n } \}$ . In this case we have

$$
\| R ( A ) \| = \| Q R ( D ) Q ^ { * } \| = \| R ( D ) \| = \operatorname* { m a x } _ { \iota = 1 , \ldots , n } | R ( \lambda _ { \iota } ) | ,
$$

ind (11.8) follows from (11.6), because the eigenvalues of $A$ satisfy $\mathrm { R e } \lambda _ { \imath } \leq 0$

b) For a general $A$ we consider the matrix function

$$
A ( \omega ) = \frac { \omega } { 2 } ( A + A ^ { * } ) + \frac { 1 } { 2 } ( A - A ^ { * } ) .
$$

We see from the identity

$$
\langle v , A ( \omega ) v \rangle = \omega \mathrm { R e } \langle v , A v \rangle + i \operatorname { I m } \langle v , A v \rangle
$$

that $A ( \omega )$ satisfies (11.6) for all $\omega$ with $\mathrm { R e } \omega \geq 0$ , so that also the eigenvalues of $A ( \omega )$ satisfy $\operatorname { R e } \lambda ( \omega ) \leq 0$ for $\mathrm { R e } \omega \geq 0$ . Therefore, the rational function

$$
\varphi ( \omega ) = \langle u , R ( A ( \omega ) ) v \rangle
$$

$( u , v$ fixed) has no poles in $\operatorname { R e } \omega \geq 0$ . Using $A ( 1 ) = A$ we obtain from the maximum principle that

$$
\begin{array} { r l } { \langle u , R ( A ) v \rangle = \displaystyle \varphi ( 1 ) \le \operatorname* { s u p } _ { y \in \mathbb R } \varphi ( i y ) \le \operatorname* { s u p } _ { y \in \mathbb R } \| R ( A ( i y ) ) \| \| u \| \| v \| } & { } \\ { \le \displaystyle \operatorname* { s u p } _ { \tiny \mathrm { R e } ~ z \le 0 } | R ( z ) | \| u \| \| v \| . } & { } \end{array}
$$

The last inequality of (11.9) follows from part (a), because $A ( i y )$ is a normal matrix (i.e., $A ( i y ) A ( i y ) ^ { * } = A ( i y ) ^ { * } A ( i y ) )$ . Formula (11.8) is now an immediate consequence of (11.9) and of the fact that $\begin{array} { r } { \| C \| = \operatorname* { s u p } _ { \| u \| \leq 1 , \| v \| \leq 1 } \left. u , C v \right. } \end{array}$ □

Corollary 11.3. If the rational function $R ( z )$ is $A$ -stable, then the numerical solution $y _ { n + 1 } = R ( h A ) y _ { n }$ is contractive in the Euclidean norm $\left( i . e . , \ \left. y _ { n + 1 } \right. \leq \right.$ $| | y _ { n }  | $ ,whenever (1l.6) is satisfied.

Proof. $A$ -stability implies that $\operatorname* { m a x } _ { \mathrm { R e } z \leq 0 } | R ( z ) | \leq 1$

Corollary 11.4. If $a$ matrix $A$ satisfies $\operatorname { R e } \langle v , A v \rangle \leq \nu \| v \| ^ { 2 }$ for all $v \in \mathbb { C } ^ { n }$ ,then

$$
\| R ( A ) \| \leq \operatorname* { s u p } _ { \operatorname { R e } z \leq \nu } | R ( z ) | .
$$

Proof. Apply Theorem 11.2 to $\widetilde { R } ( z ) = R ( z + \nu )$ and $\widetilde { A } = A - \nu I$

# Error Growth Function for Linear Problems

Guided by the above estimate, we define

$$
\varphi _ { R } ( x ) : = \operatorname* { s u p } _ { \operatorname { R e } z \leq x } | R ( z ) | .
$$

This function is called error growth function (for linear problems). It is continuous and monotonically increasing. If $R ( z )$ is analytic in the half-plane $\operatorname { R e } z < x$ ,the maximum principle implies that

$$
\varphi _ { R } ( x ) = \operatorname* { s u p } _ { y \in \mathbb { R } } | R ( x + \imath y ) | .
$$

# Examples.

1. Implicit Euler method:

$$
R ( z ) = { \frac { 1 } { 1 - z } } \qquad \varphi _ { R } ( x ) = \left\{ { R ( x ) } \begin{array} { l l } { { \displaystyle R ( x ) } } & { { \mathrm { ~ i f ~ } } - \infty < x < 1 } \\ { { \displaystyle \infty } } & { { \mathrm { ~ i f ~ } } 1 \leq x . } \end{array} \right.
$$

2. The stability function of the $\theta$ -method (or of a one-stage Rosenbrock method):

$$
R ( z ) = \frac { 1 + ( 1 - \theta ) z } { 1 - \theta z } \qquad \varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { | R ( \infty ) | } & { \mathrm { ~ i f ~ } x \leq \xi _ { 0 } } \\ { R ( x ) } & { \mathrm { ~ i f ~ } \xi _ { 0 } \leq x < 1 / \theta } \\ { \infty } & { \mathrm { ~ i f ~ } 1 / \theta \leq x , } \end{array} \right.
$$

where $\xi _ { 0 } = ( 1 - 2 \theta ) / ( 2 \theta ( 1 - \theta ) )$ for $0 < \theta < 1$ and $\xi _ { 0 } = - \infty$ for $\theta \geq 1$

3. The (0,2)-Padé approximation:

$$
R ( z ) = { \frac { 1 } { 1 - z + z ^ { 2 } / 2 } } \varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { R ( x ) } & { \mathrm { ~ i f ~ } - \infty < x \leq 0 } \\ { \displaystyle { \frac { 1 } { 1 - x } } } & { \mathrm { ~ i f ~ } 0 \leq x < 1 } \\ { \infty } & { \mathrm { ~ i f ~ } 1 \leq x . } \end{array} \right.
$$

4. The (1,2)-PdoimaiRz)

$$
\varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { | R ( x ) | } & { \mathrm { i f ~ } - \infty < x \leq \xi } \\ { \frac { \sqrt { 3 \sqrt { 1 2 x ^ { 2 } + 1 2 x + 9 } + 1 0 x + 7 } } { 2 ( 2 - x ) } } & { \mathrm { i f ~ } \xi _ { 0 } \leq x < 2 } \\ { \infty } & { \mathrm { i f ~ } 2 \leq x , } \end{array} \right.
$$

where $\xi _ { 0 } = - 6 - 3 \sqrt { 1 0 }$

5. he (2,2)-Pad pfroxia $R ( z ) = \frac { 1 + z / 2 + z ^ { 2 } / 1 2 } { 1 - z / 2 + z ^ { 2 } / 1 2 }$

$$
\varphi _ { R } ( x ) = \left\{ \begin{array} { l l } { 1 \quad } & { \mathrm { i f ~ } - \infty < x \leq 0 } \\ { \displaystyle \frac { 2 x + \sqrt { 9 + 3 x ^ { 2 } } } { 3 - x } \quad } & { \mathrm { i f ~ } 0 \leq x < 3 } \\ { \infty \quad } & { \mathrm { i f ~ } 3 \leq x . } \end{array} \right.
$$

The next two theorems give some general results on the shape of $\varphi _ { R } ( x )$

Theorem 11.5. Let $R ( z )$ be an $A$ -stable approximation to $e ^ { z }$ of exact order $p$ ， i.e.， $R ( z ) = e ^ { z } - C z ^ { p + 1 } + \mathcal { O } \left( z ^ { p + 2 } \right)$ with $C \neq 0$ . If additionally $| R ( i y ) | < 1$ for $y \neq 0$ and $| R ( \infty ) | < 1$ ， then we have

$a )$ f $p$ is odd

$$
\varphi _ { R } ( x ) = e ^ { x } + \mathcal { O } ( x ^ { p + 1 } ) \quad f o r \quad x \to 0 .
$$

$b _ { . }$ if $p$ is even we have (11.17) only for $( - 1 ) ^ { p / 2 } C x > 0$ , otherwise

$$
\varphi _ { R } ( x ) = e ^ { x } + \mathcal { O } ( x ^ { r + 1 } ) \ - \ fint { f o r \quad x \to 0 }
$$

for some positive rational number $r \leq p / 2$

Proof. The assumptions imply that for $x \to 0$ the maximum of $\{ | R ( x + i y ) | ; y \in \mathbb { R } \}$ must be located near the origin. We further observe that it must lie within the order star $A = \left\{ z \in \mathbb { C } ; | R ( z ) | > | e ^ { z } | \right\}$ .If $p$ is odd, the order star consists of $p + 1$ sectors near the origin (Lemma 4.3) and, asymptotically for $z  \infty$ ， all elements of $A$ satisfy $| z | \leq D | x |$ ， $D < \infty$ . Therefore

$$
| R ( z ) | = e ^ { x } + \mathcal { O } ( | z | ^ { p + 1 } ) = e ^ { x } + \mathcal { O } ( x ^ { p + 1 } ) \quad \mathrm { f o r } \quad x \to 0 .
$$

The same argument applies if $p$ is even and $( - 1 ) ^ { p / 2 } C x > 0$ . In the remaining case $p$ even and $( - 1 ) ^ { p / 2 } C x < 0 )$ the maximum of $\{ | R ( x + i y ) | ; y \in \mathbb { R } \}$ is attained near the imaginary axis and a more detailed analysis is necessary (Hairer, Bader & Lubich 1982). □

Theorem 11.6 (Hairer & Zennaro 1996). For an $A$ -stable approximation to $e ^ { z }$ the function $\varphi _ { R } ( x )$ is superexponential, i.e., it satisfies $\varphi _ { R } ( 0 ) = 1$ and

$$
\varphi _ { R } ( x _ { 1 } ) \varphi _ { R } ( x _ { 2 } ) \leq \varphi _ { R } ( x _ { 1 } + x _ { 2 } )
$$

for all $x _ { 1 } , x _ { 2 }$ having the same sign.

Proof. $A$ -stability is equivalent to $\varphi _ { R } ( 0 ) = 1$ ．It therefore remains to verify (11.19). Let $x _ { 1 }$ and $x _ { 2 }$ be fixed (both $\leq 0$ or both $\geq 0$ ) and assume $\varphi _ { R } ( x _ { 1 } + x _ { 2 } ) <$ $\infty$ . The idea is to consider the rational function

$$
S ( z ) = R ( a - z ) R ( z )
$$

where $a \in \mathbb { C }$ is a parameter satisfying $\mathrm { R e } a \leq x _ { 1 } + x _ { 2 }$ . Due to $A$ -stability and $\varphi _ { R } ( x _ { 1 } + x _ { 2 } ) < \infty , S ( z )$ is analytic on the stripe $0 \leq \mathrm { R e } z \leq x _ { 1 } + x _ { 2 }$ （ $\mathrm { ~ r ~ } x _ { 1 } + x _ { 2 } \leq$ $\mathrm { R e } z \le 0 ) ,$ ，and its modulus is bounded by $\varphi _ { R } ( x _ { 1 } + x _ { 2 } )$ on the border. By the maximum principle we therefore have for all $z$ in the considered stripe

$$
| R ( a - z ) R ( z ) | \leq \varphi _ { R } ( x _ { 1 } + x _ { 2 } ) .
$$

We now choose $z$ on the line $\mathrm { R e } z = x _ { 2 }$ in such a way that $| R ( z ) |$ becomes maximal; then, we choose $a$ on the line $\mathrm { R e } a = x _ { 1 } + x _ { 2 }$ (i.e., $\operatorname { R e } { \big ( } a - z { \big ) } = x _ { 1 } { \big . }$ ）such that $| R ( a - z ) |$ becomes maximal (eventually one has to consider limits). This proves (11.19). □

Property (11.19) has an interesting practical interpretation. Consider a numerical solution $y _ { n }$ obtained with variable step sizes.Repeated application of (11.4) and Corollary 11.4 implies

$$
\| y _ { m } \| \leq \Big ( \prod _ { k = 0 } ^ { m - 1 } \varphi _ { R } ( h _ { k } \mu ) \Big ) \cdot \| y _ { 0 } \| ,
$$

if the problem $y ^ { \prime } = A y$ satisfies (11.7) with $\mu = \mu _ { 2 } ( A )$ . For $\mu < 0$ and for an $A -$ stable method all factors $\varphi _ { R } ( h _ { k } \mu )$ are smaller than one. If in addition $| R ( \infty ) | < 1$ ，

these factors are close to one only for $h _ { k } \to 0$ . The inequality (11.19), written as

$$
\begin{array} { r } { \varphi _ { R } ( h _ { k } \mu ) \varphi _ { R } ( h _ { k + 1 } \mu ) \leq \varphi \big ( ( h _ { k } + h _ { k + 1 } ) \mu \big ) , } \end{array}
$$

means that replacing two consecutive steps by one large step of size $h _ { k } + h _ { k + 1 }$ increases the upper bound (11.2O). Therefore,after combining several consecutive steps (if necessary), we may assume $h _ { k } \geq h > 0$ for all $k$ . This implies that $\| y _ { m } \| \leq$ $\varrho ^ { m } \| y _ { 0 } \|$ with $\varrho = \varphi _ { R } ( h \mu ) < 1$ . Hence, for any mesh $x _ { 0 } , x _ { 1 } , \ldots$ with $x _ { m } \to \infty$ ，we have asymptotic stability,i.e., $\| y _ { m } \| \to 0$ for $m \to \infty$ . Under additional restrictions on the step size, sharper bounds on $\| y _ { m } \|$ can be obtained (Exercise 3).

# Small Nonlinear Perturbations

The above estimates,valid only for linear autonomous equations $y ^ { \prime } = J y$ ，can be extended to problems with small nonlinear perturbations, so-called semi-linear problems

$$
y ^ { \prime } = J y + g ( x , y )
$$

where

$$
\begin{array} { c } { { \langle y , J y \rangle \leq \mu \| y \| ^ { 2 } } } \\ { { } } \\ { { \| g ( x , y ) - g ( x , z ) \| \leq L \| y - z \| } } \end{array}
$$

with $L$ assumed to be small.

Here,in the presence of nonlinearities, stability properties are obtained by $\mathbf { e s - }$ timating the distance of two neighbouring solutions $y ( x )$ and ${ \widehat { y } } ( x )$ . Instead of (11.5) we therefore have

$$
\frac { d } { d x } \| y ( x ) - \widehat { y } ( x ) \| ^ { 2 } = 2 \langle y ^ { \prime } - \widehat { y } ^ { \prime } , y - \widehat { y } \rangle
$$

which gives,after inserting(11.21） for $y ^ { \prime }$ and ${ \widehat { y } } ^ { \prime }$ ,using the Cauchy-Schwarz inequality and the estimates (11.22)

$$
{ \frac { d } { d x } } \| y ( x ) - { \widehat { y } } ( x ) \| ^ { 2 } \leq 2 { \big ( } \mu + L { \big ) } \ \| y ( x ) - { \widehat { y } } ( x ) \| ^ { 2 } .
$$

We thus have contractivity whenever $\mu + L \leq 0$

We now want to establish the same property for the numerical solutions. In principle, these estimates can be carried out for all methods of this chapter; however, since the subsequent sections will deal with so many nice properties of implicit Runge-Kutta methods, we shall concentrate here on Rosenbrock methods.

Example 11.7. Consider the 1-stage Rosenbrock method

$$
\begin{array} { c } { { ( I - \gamma h J ) k _ { 1 } = h f ( x _ { 0 } , y _ { 0 } ) } } \\ { { y _ { 1 } = y _ { 0 } + k _ { 1 } } } \end{array}
$$

with $\gamma > 0$ as a free parameter. Its stability function is

$$
R ( z ) = \frac { 1 + ( 1 - \gamma ) z } { 1 - \gamma z }
$$

and we have $A$ -stability for $\gamma \geq 1 / 2$ . Application of (11.24) to (11.21) yields

$$
y _ { 1 } = R ( h J ) y _ { 0 } + ( I - \gamma h J ) ^ { - 1 } h g ( x _ { 0 } , y _ { 0 } ) .
$$

From von Neumann's theorem (Corollary 11.4) we obtain $\| ( I - \gamma h J ) ^ { - 1 } \| \leq ( 1 -$ $\gamma h \mu ) ^ { - 1 }$ and $\| R ( h J ) \| \leq \varphi _ { R } ( h \mu )$ with $\varphi _ { R }$ given in (11.13). If we take a second numerical solution $\widehat { y } _ { 1 }$ ,also defined by (11.25),its difference to $y _ { 1 }$ can be estimated by

$$
\| y _ { 1 } - \widehat { y } _ { 1 } \| \leq \Big ( R ( h \mu ) + \frac { h L } { 1 - \gamma h \mu } \Big ) \| y _ { 0 } - \widehat { y } _ { 0 } \| = \Big ( 1 + \frac { h ( \mu + L ) } { 1 - \gamma h \mu } \Big ) \| y _ { 0 } - \widehat { y } _ { 0 } \|
$$

whenever $\xi _ { 0 } < h \mu < 1 / \gamma$ with $\xi _ { 0 }$ given in (11.13). Therefore contractivity occurs for $\mu + L \leq 0$ , as desired.

For the general Rosenbrock method (7.4) applied to problem (11.21)

$$
\begin{array} { l } { { \displaystyle { k _ { \imath } = h g \big ( x _ { 0 } + c _ { \imath } h , u _ { \imath } \big ) + h J y _ { 0 } + h J \sum _ { \jmath = 1 } ^ { \imath } \big ( a _ { \imath \jmath } + \gamma _ { \imath \jmath } \big ) k _ { \jmath } } } } \\ { { \displaystyle { u _ { \imath } = y _ { 0 } + \sum _ { \jmath = 1 } ^ { \imath - 1 } a _ { \imath \jmath } k _ { \jmath } } , \quad { y _ { 1 } = y _ { 0 } + \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } k _ { \imath } } } } \end{array}
$$

we easily find the following analogue of the variation of constants formula.

Theorem 11.8. The numerical solution of a Rosenbrock method applied to (11.21) can be written as

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = R ( h J ) y _ { 0 } + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } ( h J ) g ( x _ { 0 } + c _ { \imath } h , u _ { \imath } ) } } \\ { \displaystyle { u _ { \imath } = R _ { \imath } ( h J ) y _ { 0 } + h \sum _ { j = 1 } ^ { \imath - 1 } a _ { \imath _ { \jmath } } ( h J ) g ( x _ { 0 } + c _ { \jmath } h , u _ { \jmath } ) , \quad i = 1 , \ldots , s . } } \end{array}
$$

Here $R ( z )$ is the stability function, $R _ { \ i } ( z )$ are the so-called internal stability functions and $b _ { i } ( z ) , \ a _ { \ i j } ( z )$ are rational functions whose only pole is $1 / \gamma$ and which satisfy $b _ { \imath } ( \infty ) = 0$ ， $\dot { a } _ { \iota \jmath } ( \infty ) = 0$ □

Remark. For many classes of linearly implicit methods (e.g., the methods of van der Houwen (1977),Friedli (1978), Strehmel & Weiner (1982),etc.), the numerical solution can be expressed by (11.26) with certain rational functions. Thus the following analysis can be applied to these methods as well.

We now take a second numerical solution $\widehat { y } _ { 0 } , \widehat { u } _ { \iota } , \widehat { y } _ { 1 }$ (again defined by (11.26)), take the difference to $y _ { 1 }$ and apply the triangle inequality. Using von Neumann's theorem (Corollary 11.4) the assumptions (11.22) then imply

$$
\begin{array} { r l } & { \| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \varphi _ { R } ( h \mu ) \| \widehat { y } _ { 0 } - y _ { 0 } \| + h L \displaystyle \sum _ { \imath = 1 } ^ { s } \varphi _ { b _ { \imath } } ( h \mu ) \| \widehat { u } _ { \imath } - u _ { \imath } \| } \\ & { \| \widehat { u } _ { \imath } - u _ { \imath } \| \leq \varphi _ { R _ { \imath } } ( h \mu ) \| \widehat { y } _ { 0 } - y _ { 0 } \| + h L \displaystyle \sum _ { \jmath = 1 } ^ { \imath - 1 } \varphi _ { a _ { \imath , \jmath } } ( h \mu ) \| e \widehat { u } _ { \jmath } - u _ { \jmath } \| . } \end{array}
$$

Inserting the second inequality of(11.27) repeatedly into the first one yields

Theorem 11.9. Under the assumption (11.22) the difference of two numerical solutions of (7.4) can be estimated by

$$
\| { \widehat { y } } _ { 1 } - y _ { 1 } \| \leq { \big ( } \varphi _ { R } ( h \mu ) + c h L { \big ) } \| { \widehat { y } } _ { 0 } - y _ { 0 } \|
$$

where $\varphi _ { R } ( x )$ is given by (11.11) ( $R ( z )$ is the stability function of (7.4)) and c is a constant depending smoothly on $h L$ and $h \mu$ but not on $\| J \|$ (which represents the stiffness of the problem). □

This estimate shows numerical contractivity whenever $\varphi _ { R } ( h \mu ) + h L ^ { * } \leq 0$ .In Theorem 11.5 we have shown under certain assumptions that $\varphi _ { R } ( x ) = 1 + x +$ $o ( x )$ ，so contractivity holds essentially for $\mu + L ^ { * } \leq 0$ . In any case we have that $A$ -stability implies

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \left( 1 + h C ^ { * } \right) \| \widehat { y } _ { 0 } - y _ { 0 } \|
$$

for $h \mu \leq C o n s t$ . Here, $C ^ { * }$ is a constant independent of the stiffess of (11.21).

Remark. Since the rational functions $b _ { \imath }$ and $a _ { \scriptscriptstyle { \imath \jmath } }$ in (11.26) vanish at infinity,also $( 1 - \gamma h J ) b _ { \iota } ( h J )$ and $( 1 - \gamma h J ) a _ { \iota \boldsymbol { \jmath } } ( h J )$ are uniformly bounded for $J$ satisfying (11.22) and for $h \mu \leq C < \gamma ^ { - 1 }$ . Instead of the second condition of (11.22) we may therefore require that

$$
\begin{array} { r } { \| ( I - \gamma h J ) ^ { - 1 } h ( g ( x , y ) - g ( x , z ) ) \| \leq \ell \| y - z \| , } \end{array}
$$

and the statement of Theorem 11.9 holds with $h L$ replaced by $\ell$ . Observe that the assumption（11.22) implies （11.29） with $\ell = h L / ( 1 - \gamma h \mu )$ . However, in some special situations the number $\ell$ may be significantly smaller than $h L$ . Related techniques are used by Hundsdorfer(1985) and Strehmel & Weiner (1987) to prove contractivity and convergence for linearly implicit methods. Ostermann (1988) ap-plies these ideas to nonlinear singular perturbation problems, where $h L = \mathcal { O } ( h \varepsilon ^ { - 1 } )$ with some very small $\varepsilon$ $\left( \varepsilon \ll h \right)$ ,but $\ell$ can be bounded independently of $\varepsilon ^ { - 1 }$ ·

# Contractivity in $\| \cdot \| _ { \infty }$ and $\| \cdot \| _ { 1 }$

The study of contractivity in general norms has been carried out mainly by Spijker (1983,1985) and his collaborators. Similar techniques of proof can be found in Bolley & Crouzeix (1978),where a related problem (monotonicity) is treated.

The following theorem gives a condition which is necessary for contractivity just for the special equation (11.2) and for one of the two norms $\| \cdot \| _ { \infty } \ \mathrm { o r } \ \| \cdot \| _ { 1 } .$ Later,the same condition will also turn out to be sufficient for general problems and all norms.

Theorem 11.10. Let $A$ be the $\textit { n }$ -dimensional matrix of(11.2) with fixed $\lambda \geq 0$ For a rational function $R ( z )$ satisfying $R ( 0 ) = 1$ we have

$$
\| R ( h A ) \| _ { \infty } \leq 1 \quad i n a l l d i m e n s i o n s \quad n = 1 , 2 , \ldots .
$$

only if

$$
R ^ { ( j ) } ( x ) \geq 0 f o r x \in [ - \lambda h , 0 ] a n d j = 0 , 1 , 2 , . . .
$$

(The same statement is true,if Il:ll in (11.30) is replaced by $\| \cdot \| _ { 1 } )$

Proof. We put $h = 1$ and write $A = - \lambda I + \lambda N$ ,where $N$ is a nilpotent matrix. In a suitable norm, $\| N \|$ is arbitrarily small and therefore we have by Taylor expansion and $N ^ { n } = 0$

$$
R ( A ) = \sum _ { j = 0 } ^ { n - 1 } R ^ { ( j ) } ( - \lambda ) { \frac { ( \lambda N ) ^ { j } } { j ! } } .
$$

This means (e.g. for $n = 4$ ）

$$
R ( A ) = \left( \begin{array} { r r r r } { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 2 } } { 2 ! } R ^ { \prime \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 3 } } { 3 ! } R ^ { \prime \prime \prime } ( - \lambda ) } } \\ { { } } & { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } & { { \frac { \lambda ^ { 2 } } { 2 ! } R ^ { \prime \prime } ( - \lambda ) } } \\ { { } } & { { } } & { { R ( - \lambda ) } } & { { \lambda R ^ { \prime } ( - \lambda ) } } \\ { { } } & { { } } & { { R ( - \lambda ) } } & { { R ( - \lambda ) } } \end{array} \right) .
$$

Application of Formula (I.9.11'） shows that $\| R ( A ) \| _ { \infty } \leq 1 \ ( \mathrm { o r } \ \| R ( A ) \| _ { 1 } \leq 1 )$ isequivalent to

$$
\sum _ { j = 0 } ^ { n - 1 } \big | R ^ { ( j ) } ( - \lambda ) \big | \frac { \lambda ^ { j } } { j ! } \ \le 1 .
$$

If (11.32) is valid for all $n \geq 1$ , the series

$$
\sum _ { \jmath \geq 0 } R ^ { ( \jmath ) } ( - \lambda ) \frac { \lambda ^ { j } } { j ! }
$$

is absolutely convergent, and therefore we have

$$
1 = R ( 0 ) = \sum _ { j \geq 0 } R ^ { ( j ) } ( - \lambda ) { \frac { \lambda ^ { j } } { j ! } } \leq \sum _ { j \geq 0 } | R ^ { ( j ) } ( - \lambda ) | { \frac { \lambda ^ { j } } { j ! } } \leq 1
$$

implying $R ^ { ( j ) } ( - \lambda ) \geq 0$ for all $j \geq 0$ . Since the Taylor expansion

$$
R ^ { ( j ) } ( x ) = \sum _ { k \geq \jmath } R ^ { ( k ) } ( - \lambda ) \frac { ( x + \lambda ) ^ { k - j } } { ( k - j ) ! }
$$

consists for $x \geq - \lambda$ only of non-negative terms, we have (11.31).

The next theorem shows that condition (11.31） is sufficient for contractivity in arbitrary norms. It can readily be applied to the system (11.2),since its matrix satisfies $\| A + \lambda I \| _ { \infty } = \lambda$

Theorem 11.11. Consider an arbitrary norm and let $A$ be such that for some $\lambda \geq 0$ ，

$$
\| A + \lambda I \| \leq \lambda .
$$

If the stability function of $a$ method satisfies $R ( 0 ) = 1$ and

$$
R ^ { ( \jmath ) } ( x ) \geq 0 \quad f o r \quad x \in [ - \varrho , 0 ] \quad a n d \quad j = 0 , 1 , 2 , \ldots .
$$

then we have numerical contractivity $\| R ( h A ) \| \leq 1$ , whenever $h \lambda \leq \varrho$

Proof. We again put $h = 1$ . Since for $0 \leq \lambda \leq \varrho$ we have $R ^ { ( j ) } ( - \lambda ) \ge 0$ for all $j$ the function

$$
R ( z ) = \sum _ { j \geq 0 } R ^ { ( j ) } ( - \lambda ) { \frac { ( z + \lambda ) ^ { j } } { j ! } }
$$

satisfies $| R ( z ) | \leq R ( - \lambda + r )$ for all complex $z$ in the disk $| z + \lambda | \leq r$ . This property and (11.35) imply that no pole of $R ( z )$ can lie in $| z + \lambda | \leq \lambda$ ， so that the radius of convergence of (11.36) is strictly larger than $\lambda$ . Consequently we have from (11.34)

$$
R ( A ) = \sum _ { j \geq 0 } R ^ { ( \jmath ) } ( - \lambda ) { \frac { ( A + \lambda I ) ^ { \jmath } } { j ! } } .
$$

The triangle inequality applied to (11.37) yields the conclusion.

# Study of the Threshold Factor

Definition 11.12. The largest $\varrho$ satisfying (11.35) is called the threshold-factor of $R ( z )$

Example 11.13. The implicit Euler method, for which

$$
R ^ { ( j ) } ( x ) = { \frac { j ! } { ( 1 - x ) ^ { j + 1 } } } , \quad j = 0 , 1 , 2 , \ldots ,
$$

satisfies (11.35) for all $\varrho > 0$ . It possesses a threshold-factor $\varrho = \infty$

Example 11.14 (Threshold-factor for Padé-approximations). The derivatives of the polynomials

$$
R _ { k 0 } ( z ) = 1 + z + { \frac { z ^ { 2 } } { 2 ! } } + \ldots + { \frac { z ^ { k } } { k ! } }
$$

are easily calculated; the most dangerous one is $1 + z$ ,therefore $\varrho = 1$ for all $k$

The Padé approximations $R _ { k 1 } ( z )$ possess one simple pole only,so they can be written in the form

$$
R _ { k 1 } ( z ) = \frac { a } { 1 - b z } + \mathrm { p o l y n o m i a l i n } z ,
$$

which has only a finite number of derivatives which can change sign (see Example 11.13). The numerical values obtained are shown in Table 11.1.

The functions $R _ { k 2 } ( z )$ possess no real pole (see Sect.IV.4). But the property $| R ( z ) | \leq R ( - \varrho + r )$ for $| z + \varrho | \leq r$ (see proof of Theorem 11.10) means that the maximum of $| R ( z ) |$ on the circle with center $- \varrho$ and radius $\mathscr { r }$ is assumed to the right on the real axis. For increasing $\boldsymbol { \mathscr { r } }$ , the first pole met by this circle must therefore be real and to the right of $- \varrho$ ． This is not possible here and therefore the approximations $R _ { k 2 } ( z )$ never satisfy property (11.35). This is indicated by an asterisk $( * )$ in Table 11.1.

All further values of Table 11.1 were computed using the decomposition of $R ( z )$ into partial fractions and are cited from Kraaijevanger (1986) and van de Griend & Kraaijevanger (1986).

Table 11.1. Threshold-factors of Padé approximations   

<table><tr><td>k</td><td>0 1 2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>J=0</td><td>1 1</td><td>1</td><td>1</td><td>1 1</td><td>1</td></tr><tr><td>J=1</td><td>8 2</td><td>2.196</td><td>2.350 2.477</td><td>2.586</td><td>2.682</td></tr><tr><td>j=2</td><td>* *</td><td>*</td><td>* *</td><td>*</td><td>*</td></tr><tr><td>j=3</td><td>0.584 1.195</td><td>1.703</td><td>2.208</td><td>2.710 3.212</td><td>3.713</td></tr><tr><td>j=4</td><td>* *</td><td>*</td><td>* *</td><td>*</td><td>*</td></tr><tr><td>j=5</td><td>0.353 0.770</td><td>1.081</td><td>1.424</td><td>1.794 2.185</td><td>2.590</td></tr></table>

It is curious to observe that in this table the methods with the largest thresholdfactors are precisely those which are not $A$ -stable. An exception is the implicit Euler method $\left( k = 0 , j = 1 \right)$ for which $\varrho = \infty$ .

# Absolutely Monotonic Functions

... on peut definir la fonction $e ^ { x }$ comme la seule fonction absolument monotone sur tout le demi-axe négatif qui prend al'origine, ainsi que sa dérivee premiere [sic] la valeur un.

(S. Bernstein 1928)

A thorough study of real functions satisfying (11.35) was begun by S.Bernstein (1914) and continued by F. Hausdorff(1921). Such functions are called absolutely monotonic in $[ - \varrho , 0 ]$ . Later, S. Bernstein (1928) gave the following characterization of functions which are absolutely monotonic in $( - \infty , 0 ]$ (see also D.V. Widder 1946).

Theorem 11.15 (Bernstein 1928). A necessary and sufficient condition that $R ( x )$ be absolutely monotonic in $( - \infty , 0 ]$ is that

$$
R ( x ) = \int _ { 0 } ^ { \infty } e ^ { x t } d \alpha ( t ) ,
$$

where $\alpha ( t )$ is bounded and non-decreasing and the integral converges for $- \infty <$ $x \le 0$

This is a hard result and the main key for the next two theorems. It does not seem to permit an elementary and easy proof. We therefore refer to the original literature, S. Bernstein (1928). For a more recent description see e.g. Widder (1946),p.160. From this result we immediately get the “limit case $\lambda  \infty ^ { \prime \prime }$ of Theorem 11.11, which also holds for an arbitrary norm.

Theorem 11.16. Let $R ( x )$ be absolutely monotonic in $( - \infty , 0 ] , R ( 0 ) = 1$ and A a matrix with non-positive logarithmic norm $\mu ( A ) \leq 0$ ， then

$$
\| R ( A ) \| \leq 1 .
$$

Proof. By Theorem I.10.6 we have for the solution $y ( x ) = e ^ { A x } y _ { 0 }$ of $y ^ { \prime } = A y$ that $\| y ( x ) \| \leq \| y _ { 0 } \|$ , hence also $\| e ^ { \ b { A } \ b { x } } \| \leq 1$ for $x \ge 0$ . The statement now follows from

$$
\| R ( A ) \| = \| \int _ { 0 } ^ { \infty } e ^ { A t } d \alpha ( t ) \| \le \int _ { 0 } ^ { \infty } \| e ^ { A t } \| d \alpha ( t ) \le \int _ { 0 } ^ { \infty } d \alpha ( t ) = R ( 0 ) = 1
$$

since $\alpha ( t )$ is non-decreasing.

The following result proves that no Runge-Kutta method of order $p > 1$ can have a stability function which is absolutely monotonic in $( - \infty , 0 ]$

Theorem 11.17. If $R ( x )$ is absolutely monotonic in $( - \infty , 0 ]$ and

$$
R ( x ) = 1 + x + x ^ { 2 } / 2 + \mathcal { O } ( x ^ { 3 } ) \qquad f o r \quad x \to 0 ,
$$

then $R ( x ) = e ^ { x }$

Proof (Bolley & Crouzeix 1978). It follows from (11.38) that

$$
R ^ { ( j ) } ( 0 ) = \int _ { 0 } ^ { \infty } t ^ { j } d \alpha ( t ) .
$$

Since $R ( 0 ) = R ^ { \prime } ( 0 ) = R ^ { \prime \prime } ( 0 ) = 1$ , this yields

$$
\int _ { 0 } ^ { \infty } ( 1 - t ) ^ { 2 } d \alpha ( t ) = 0 .
$$

Consequently, $\alpha ( t )$ must be the Heaviside function $( \alpha ( t ) = 0$ for $t \leq 1$ and $\alpha ( t ) =$ 1 for $t > 1$ ). Inserted into (11.38) this gives $R ( x ) = e ^ { x }$ □

# Exercises

1. Prove Formula (11.14). For given $\boldsymbol { x }$ ，study the set of $y$ -values for which $| R ( x + i y ) |$ attains its maximum.

2. Show that the error growth function (11.11） for an $A$ -stable $R ( z )$ of order $p \geq 1$ satisfies

$$
\varphi _ { R } ( x ) > e ^ { x } \quad { \mathrm { f o r ~ a l l } } \quad x \neq 0 .
$$

Hint. You can study the order star on parallel lines $\{ x + i y , y \in \mathbb { R } \}$ (Hairer, Bader & Lubich 1982),or you can use the fact that $\varphi _ { R } ( x )$ is superexponential.

3. (Hairer & Zennaro 1996). Let $| R ( \infty ) | < 1$ and consider a mesh $x _ { 0 } , x _ { 1 } , \ldots$ with step sizes $h _ { k } = x _ { k + 1 } - x _ { k }$ satisfying $h _ { k + 1 } \leq c h _ { k }$ $( c > 1 )$ .Prove the existence of constants $C > 0$ and $\alpha > 0$ such that

$$
\begin{array} { r } { \| y _ { m } \| \leq C ( x _ { m } - x _ { 0 } ) ^ { - \alpha } \| y _ { 0 } \| \qquad \mathrm { ~ f o r ~ } \quad m = 1 , 2 , \ldots . } \end{array}
$$

4. (Kraaijevanger 1986). Let $R ( z )$ be a polynomial of degree $s$ satisfying $R ( z ) =$ $e ^ { z } + \mathcal { O } \big ( z ^ { p + 1 } \big )$ . Then the threshold factor $\varrho$ (Definition 11.11) is restricted by

$$
\varrho \leq s - p + 1 .
$$

Hint. Justify the formula

$$
R ^ { ( p - 1 ) } ( z ) = \sum _ { \jmath = 0 } ^ { s - p + 1 } \alpha _ { \jmath } \Big ( 1 + \frac { z } { \varrho } \Big ) ^ { \jmath } , \quad \alpha _ { \jmath } \geq 0
$$

and deduce the result from $R ^ { ( p - 1 ) } ( 0 ) = R ^ { ( p ) } ( 0 ) = 1$

5. Let $\varrho$ be the threshold factor of the rational function $R ( z )$ . Show that its stability domain contains the disc $| z + \varrho | \le \varrho$

# IV.12 B-Stability and Contractivity

Next we need a generalization of the notion of $A$ -stability. The most natural generalization would be to consider the case that ${ \boldsymbol x } ( t )$ is a uniform-asymptotically stable solution ... in the sense of Liapunov theory ... but this case seems to be a little too wide.

(G. Dahlquist 1963)

The theoretical analysis of the application of numerical methods on stiff nonlinear problems is still fairly incomplete.

(G. Dahlquist 1975)

Here we enter a new era, the study of stability and convergence for general nonlinear systems. All the“crimes” and diverse omissions of which we have been guilty in earlier sections, especially in Sect. IV.2, shall now be repaired.

Large parts of Dahlquist's(1963) paper deal with a generalization of $A$ -stability to nonlinear problems. His search for a sufciently general class of nonlinear systems was finally successful 12 years later. In his talk at the Dundee conference of July 1975 he proposed to consider differential equations satisfying a one-sided Lipschitz condition,and he presented some first results for multistep methods. J.C.Butcher(1975） then extended (on the flight back from the conference） the ideas to implicit Runge-Kutta methods and the concept of $B$ -stability was born.

# One-Sided Lipschitz Condition

We consider the nonlinear differential equation

$$
y ^ { \prime } = f ( x , y )
$$

such that for the Euclidean norm the one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 }
$$

holds.The number $\nu$ is the one-sided Lipschitz constant of $f$ . This definition is motivated by the following result.

Lemma 12.1. Let $f ( x , y )$ be continuous and satisfy (12.2). Then, for any two solutions $y ( x )$ and $z ( x )$ of(12.1) we have

$$
\| y ( x ) - z ( x ) \| \leq \| y ( x _ { 0 } ) - z ( x _ { 0 } ) \| \cdot e ^ { \nu ( x - x _ { 0 } ) } \qquad f o r ~ x \geq x _ { 0 } .
$$

Proof. Differentiation of $m ( x ) = \| y ( x ) - z ( x ) \| ^ { 2 }$ yields

$$
m ^ { \prime } ( x ) = 2 { \bigl \langle } f ( x , y ( x ) ) - f ( x , z ( x ) ) , \ y ( x ) - z ( x ) { \bigr \rangle } \leq 2 \nu m ( x ) .
$$

This differential inequality can be solved to give (see Theorem I.10.3)

$$
m ( x ) \leq m ( x _ { 0 } ) e ^ { 2 \nu ( x - x _ { 0 } ) } \qquad { \mathrm { f o r } } \ x \geq x _ { 0 } ,
$$

which is equivalent to the statement.

EHairer and G Wanner, Solving Ordinary Differential Equations II, Springer Series in Computat1onal Mathematics 14, DOI 10 1007/978-3-642-05221-7_12, $©$ Springer-Verlag Berlin Heidelberg 2010

Remarksesoistt $\mu ( \frac { \partial f } { \partial y } ) \leq \nu$ (see Sect.I.10, Exercise 6), if $f$ is continuously differentiable. Lemma 12.1 then becomes a special case of Theorem I.10.6.

b) For complex-valued $y$ and $f$ condition (12.2) has to be replaced by

$$
\mathrm { R e } \left. f ( x , y ) - f ( x , z ) , y - z \right. \leq \nu \left. y - z \right. ^ { 2 } , \qquad y , z \in \mathbb { C } ^ { n } ,
$$

and Lemma 12.1 remains valid.

# $B$ -Stability and Algebraic Stability

Whenever $\nu \leq 0$ in (12.2） the distance between any two solutions of (12.1） is a non-increasing function of $x$ . The same property is then also desirable for the numerical solutions. We consider here implicit Runge-Kutta methods

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = y _ { 0 } + h \sum _ { i = 1 } ^ { s } b _ { i } f \big ( x _ { 0 } + c _ { i } h , g _ { i } \big ) , } } \\ { \displaystyle { g _ { \imath } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { \imath j } f \big ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } \big ) , \qquad i = 1 , \dots , s . } } \end{array}
$$

Definition 12.2 (Butcher 1975). A Runge-Kutta method is called $B$ -stable, if the contractivity condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq 0
$$

implies for all $h \geq 0$

$$
\lVert y _ { 1 } - { \widehat { y } } _ { 1 } \rVert \leq \lVert y _ { 0 } - { \widehat { y } } _ { 0 } \rVert .
$$

Here, $y _ { 1 }$ and $\widehat { y } _ { 1 }$ are the numerical approximations after one step starting with initial values $y _ { 0 }$ and $\widehat { y } _ { 0 }$ ,respectively.

Clearly, $B$ -stability implies $A$ -stability. This is seen by applying the above definition to $y ^ { \prime } = \lambda y , \lambda \in \mathbb { C }$ or, more precisely, to

$$
\left( \begin{array} { c } { { y _ { 1 } ^ { \prime } } } \\ { { y _ { 2 } ^ { \prime } } } \end{array} \right) = \left( \begin{array} { c c } { { \alpha } } & { { - \beta } } \\ { { \beta } } & { { \alpha } } \end{array} \right) \left( \begin{array} { c } { { y _ { 1 } } } \\ { { y _ { 2 } } } \end{array} \right) .
$$

Example 12.3. For the collocation methods based on Gaussian quadrature a simple proof of $B$ -stability is possible (Wanner 1976). We denote by $u ( x )$ and ${ \widehat { u } } ( x )$ the collocation polynomials (see Definition II.7.6) for the initial values $y _ { 0 }$ and $\widehat { y } _ { 0 }$ and differentiate the function $m ( x ) = \| u ( x ) - { \widehat { u } } ( x ) \| ^ { 2 }$ ． At the collocation points $\xi _ { \ i } = x _ { 0 } + c _ { \ i } h$ we obtain

$$
\begin{array} { r } { m ^ { \prime } ( \xi _ { \iota } ) = 2 \big \langle f ( \xi _ { \iota } , u ( \xi _ { \iota } ) ) - f ( \xi _ { \iota } , \widehat { u } ( \xi _ { \iota } ) ) , u ( \xi _ { \iota } ) - \widehat { u } ( \xi _ { \iota } ) \big \rangle \leq 0 . } \end{array}
$$

The result then follows from the fact that Gaussian quadrature integrates the polynomial $m ^ { \prime } ( x )$ (which is of degree $2 s - 1 )$ ） exactly and that the weights $b _ { \imath }$ are positive:

$$
\begin{array} { l } { \displaystyle \| y _ { 1 } - \widehat { y } _ { 1 } \| ^ { 2 } = m ( x _ { 0 } + h ) = m ( x _ { 0 } ) + \int _ { x _ { 0 } } ^ { x _ { 0 } + h } m ^ { \prime } ( x ) d x } \\ { \displaystyle = m ( x _ { 0 } ) + h \sum _ { \imath = 1 } ^ { s } b _ { \imath } m ^ { \prime } ( x _ { 0 } + c _ { \imath } h ) \leq m ( x _ { 0 } ) = \| y _ { 0 } - \widehat { y } _ { 0 } \| ^ { 2 } . } \end{array}
$$

An algebraic criterion for $B$ -stability was found independently by Burrage & Butcher(1979) and Crouzeix (1979). The result is

Theorem 12.4. If the coeffcients of a Runge-Kutta method (12.3) satisfy

i） $b _ { \imath } \geq 0$ for $i = 1 , \dots , s ,$   
ii $M = ( m _ { i j } ) = ( b _ { \ i } a _ { \ i j } + b _ { \jmath } a _ { \jmath \imath } - b _ { i } b _ { \jmath } ) _ { i , j = 1 } ^ { \it s }$ is non-negative definite, then the method is $B$ -stable.

Definition 12.5.A Runge-Kutta method, satisfying (i) and (ii) of Theorem 12.4, is called algebraically stable.

Proof of Theorem 12.4. We introduce the differences

$$
\begin{array} { r l } & { \Delta y _ { 0 } = y _ { 0 } - \widehat { y } _ { 0 } , \qquad \Delta y _ { 1 } = y _ { 1 } - \widehat { y } _ { 1 } , \qquad \Delta g _ { \iota } = g _ { \iota } - \widehat { g } _ { \iota } , } \\ & { \Delta f _ { \iota } = h \big ( f ( x _ { 0 } + c _ { \iota } h , g _ { i } ) - f ( x _ { 0 } + c _ { i } h , \widehat { g } _ { \iota } ) \big ) , } \end{array}
$$

and subtract the Runge-Kutta formulas (12.3) for $y$ and $\widehat { y }$

$$
\begin{array} { l } { \displaystyle \Delta y _ { 1 } = \Delta y _ { 0 } + \sum _ { i = 1 } ^ { s } b _ { i } \Delta f _ { \imath } , } \\ { \displaystyle \Delta g _ { \imath } = \Delta y _ { 0 } + \sum _ { j = 1 } ^ { s } a _ { \imath j } \Delta f _ { \jmath } . } \end{array}
$$

Next we take the square of Formula (12.5a)

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { i = 1 } ^ { s } b _ { \imath } \langle \Delta f _ { \imath } , \Delta y _ { 0 } \rangle + \sum _ { \imath = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } b _ { \imath } b _ { \jmath } \langle \Delta f _ { \imath } , \Delta f _ { \jmath } \rangle .
$$

The main idea of the proof is now to compute $\Delta y _ { 0 }$ from (12.5b) and insert this into (12.6). This gives

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { \iota = 1 } ^ { s } b _ { \iota } \langle \Delta f _ { \iota } , \Delta g _ { i } \rangle - \sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { \iota \jmath } \langle \Delta f _ { \iota } , \Delta f _ { \jmath } \rangle .
$$

$\langle \Delta f _ { \imath } , \Delta g _ { i } \rangle \leq 0$ by $( 1 2 . 2 ^ { \circ } )$ and ta $\begin{array} { r } { \sum _ { \iota , \jmath = 1 } ^ { s } m _ { \iota \jmath } \langle \Delta f _ { i } , \Delta f _ { \jmath } \rangle \geq 0 } \end{array}$

Example 12.6. For the SDIRK method of Table 7.2 (Chapter II) the weights $b _ { i }$ are seen to be positive and the matrix $M$ becomes

$$
M = ( \gamma - 1 / 4 ) \cdot \left( \begin{array} { r r } { { 1 } } & { { - 1 } } \\ { { - 1 } } & { { 1 } } \end{array} \right) .
$$

For $\gamma \ge 1 / 4$ this matrix is non-negative definite and we have $B$ -stability. Exactly the same condition was obtained by studying its $A$ -stability (c.f. (3.10)).

# Some Algebraically Stable IRK Methods

La premiere de ces proprietes consiste en ce que tous les $A _ { k }$ sont positifs. (T.-J. Stieltjes 1884)

The general study of algebraic stability falls naturally into two steps: the positivity of the quadrature weights and the nonnegative-definitness of the matrix $M$

Theorem 12.7. Consider a quadrature formula $( c _ { \imath } , b _ { \imath } ) _ { \imath = 1 } ^ { s }$ of order $p$

$a _ { . }$ ）If $p \geq 2 s - 1$ then $b _ { \imath } > 0$ for all $i$ $b _ { \mathcal { S } }$ If $c _ { \imath }$ are the zeros of (5.3) (Lobatto quadrature) then $b _ { i } > 0$ for all $i$

Proof (Stieltjes 1884). The first statement follows from the fact that for $p \geq 2 s - 1$ polynomials of degree $2 s - 2$ are integrated exactly, hence

$$
b _ { \imath } = \int _ { 0 } ^ { 1 } \prod _ { \jmath \neq \imath } \Bigl ( { \frac { x - c _ { \jmath } } { c _ { \imath } - c _ { \jmath } } } \Bigr ) ^ { 2 } d x > 0 .
$$

In the case of the Lobatto quadrature $( c _ { 1 } = 0 , \ c _ { s } = 1$ and $p = 2 s - 2 )$ the factors for the indices $j = 1$ and $j = s$ are taken without squaring and the same argument applies. □

In order to verify condition (ii) of Theorem 12.4 we find it convenient to use the $W$ -transformation of Sect.IV.5 and to consider $W ^ { T } M W$ instead of $M$ In vector notation $( b = ( b _ { 1 } , \dots , b _ { s } ) ^ { T }$ ， $B = \mathrm { d i a g } ( b _ { 1 } , \dots , b _ { s } )$ ， $A = \left( a _ { \imath \jmath } \right) )$ we have

$$
M = B A + A ^ { T } B - b b ^ { T } .
$$

If we choose $W$ according to Lemma 5.12, then $W ^ { T } B W = I$ and, since $W ^ { T } b =$ $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T }$ ,condition (ii) becomes equivalent to

$$
W ^ { T } M W = X + X ^ { T } - e _ { 1 } e _ { 1 } ^ { T } { \mathrm { i s ~ n o n } } { \mathrm { - n e g a t i v e ~ d e f i n i t e } }
$$

where $X = W ^ { - 1 } A W = W ^ { T } B A W$ as in Theorem 5.11.

Theorem 12.8. Suppose that a Runge-Kutta method with distinct $c _ { \imath }$ and positive $b _ { i }$ satisfies the simplifying assumptions $B ( 2 s - 2 ) , C ( s - 1 ) , D ( s - 1 )$ (see beginning of Sect.IV.5). Then the method is algebraically stable if and only if $| R ( \infty ) | \leq 1$ (where $R ( z )$ denotes the stability function).

Proof. Since the order of the quadrature formula is $p \geq 2 s - 2$ , the matrix $W$ of Lemma 5.12 is

$$
W = W _ { G } D , \quad D = { \mathrm { d i a g } } ( 1 , \dots , 1 , \alpha ^ { - 1 } ) ,
$$

where $\boldsymbol { W } _ { G } = ( P _ { \jmath - 1 } ( c _ { \imath } ) ) _ { \imath , \jmath = 1 } ^ { s }$ is as in (5.21), and $\begin{array} { r } { \alpha ^ { 2 } = \sum _ { \iota = 1 } ^ { s } \bar { b } _ { i } P _ { s - 1 } ^ { 2 } ( c _ { \iota } ) \ne 0 } \end{array}$ .Us-ing the relation (observe that $W ^ { T } B W = I$ ）

$$
X = W ^ { - 1 } A W = D ^ { - 1 } W _ { G } ^ { - 1 } A W _ { G } D = D W _ { G } ^ { T } B A ( W _ { G } ^ { T } B ) ^ { - 1 } D ^ { - 1 }
$$

and applying Lemma 5.7 with $\eta = s - 1$ and Lemma 5.8 with $\xi = s - 1$ , we obtain

$$
X = \left( \begin{array} { c c c c c c } { { 1 / 2 } } & { { - \xi _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { 0 } } & { { \cdot \cdot } } & { { } } & { { } } & { { } } \\ { { } } & { { \cdot \cdot } } & { { \cdot \cdot } } & { { - \xi _ { s - 2 } } } & { { } } & { { } } \\ { { } } & { { } } & { { \xi _ { s - 2 } } } & { { 0 } } & { { - \alpha \xi _ { s - 1 } } } \\ { { } } & { { } } & { { } } & { { \alpha \xi _ { s - 1 } } } & { { \beta } } \end{array} \right) .
$$

If this matrix is inserted into (12.10) then, marvellous surprise, everything cancels with the exception of $\beta$ . Therefore, condition (ii) of Theorem 12.4 is equivalent to $\beta \geq 0$

Using the representation (5.31)of the stability function we obtain by develop-ing the determinants

$$
| R ( \infty ) | = \left| { \frac { \operatorname* { d e t } ( X - e _ { 1 } e _ { 1 } ^ { T } ) } { \operatorname* { d e t } X } } \right| = \left| { \frac { \beta d _ { s - 1 } - \alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } } { \beta d _ { s - 1 } + \alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } } } \right| ,
$$

where $d _ { k } = k ! / ( 2 k ) !$ is the determinant of the $k$ -dimensional matrix $X _ { G }$ of (5.13). Since $\alpha ^ { 2 } \xi _ { s - 1 } ^ { 2 } d _ { s - 2 } > 0$ ,the expression(12.12)isbounded by1iff $\beta \geq 0$ This proves the statement. □

Comparing these theorems with Table 5.13 yields

Theorem 12.9. The methods Gauss, Radau IA, Radau IIA and Lobatto IIIC are algebraically stable and therefore also $B$ -stable. □

# A N -Stability

$A$ -stability theory is based on the autonomous linear equation $y ^ { \prime } = \lambda y$ ，whereas $B$ -stability is based on general nonlinear systems $y ^ { \prime } { = } f ( x , y )$ . The question arises whether there is a reasonable stability theory between these two extremes. A natural approach would be to study the scalar, linear, nonautonomous equation

$$
y ^ { \prime } = \lambda ( x ) y , \qquad \operatorname { R e } \lambda ( x ) \leq 0 ,
$$

where $\lambda ( x )$ is an arbitrarily varying complex-valued function (Burrage & Butcher 1979,Scherer 1979). The somewhat surprising result of this subsection will be that stability for(12.13) will, for most RK-methods, be equivalent to $B$ -stability.

For the problem (12.13) the Runge-Kutta method (12.3) becomes (in vector notation $g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T }$ ， $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T } )$

$$
g = 1 1 y _ { 0 } + A Z g , \quad Z = \mathrm { d i a g } ( z _ { 1 } , \dots , z _ { s } ) , \quad z _ { \jmath } = h \lambda ( x _ { 0 } + c _ { \jmath } h ) .
$$

Computing $g$ from(12.14) and inserting into (12.3a) gives

$$
\begin{array} { r } { y _ { 1 } = K ( Z ) y _ { 0 } , \quad K ( Z ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 } . } \end{array}
$$

Definition 12.10. A Runge-Kutta method is called AN -stable, if

$$
| K ( Z ) | \leq 1 \quad \left\{ { \begin{array} { l } { { \mathrm { f o r ~ a l l ~ } } Z = \mathrm { d i a g } ( z _ { 1 } , \ldots , z _ { s } ) { \mathrm { ~ s a t i s f y i n g ~ R e ~ } } z _ { j } \leq 0 } \\ { { \mathrm { a n d ~ } } z _ { \jmath } = z _ { k } { \mathrm { ~ w h e n e v e r ~ } } c _ { \jmath } = c _ { k } \ ( j , k = 1 , \ldots , s ) . } \end{array} } \right.
$$

Comparing (12.15) with (3.2) we find that

$$
K \big ( \mathrm { d i a g } ( z , z , \ldots , z ) \big ) = R ( z ) ,
$$

the usual stability function. Further, arguing as with (12.4), $B$ -stability implies $A N$ -stability. Therefore we have:

Theorem 12.11. For Runge-Kutta methods it holds

$$
B \cdot s t a b l e \quad \Rightarrow \quad A N \cdot s t a b l e \quad \Rightarrow \quad A \cdot s t a b l e .
$$

For the trapezoidal rule $y _ { 1 } = y _ { 0 } + { \textstyle \frac { h } { 2 } } \big ( f ( x _ { 0 } , y _ { 0 } ) + f ( x _ { 1 } , y _ { 1 } ) \big )$ the function $\bar { \kappa } ( Z )$ of (12.15) is given by

$$
K ( Z ) = \frac { 1 + z _ { 1 } / 2 } { 1 - z _ { 2 } / 2 } .
$$

Putting $z _ { 2 } = 0$ and $z _ { 1 }  - \infty$ we see that this method is not $A N$ -stable. More generally we have the following result.

Theorem 12.12 (Scherer 1979). The Lobatto IIIA and Lobatto IIIB methods are not $A N$ -stable and therefore not $B$ -stable.

Proof. As in Proposition 3.2 we find that

$$
K ^ { ^ { \prime } } ( Z ) = { \frac { \operatorname * { d e t } ( I - ( A - 1 1 b ^ { T } ) Z ) } { \operatorname * { d e t } ( I - A Z ) } } .
$$

By definition, the first row of $A$ and the last row of $A - \mathbb { 1 } b ^ { T }$ vanish for the Lobatto IIIA methods (compare also the proof of Theorem 5.5). Therefore the denominator of $K ( Z )$ does not depend on $z _ { 1 }$ and the numerator not on $z _ { s }$ . If we put for example $z _ { 2 } = . . . = z _ { s } = 0$ , the function $K ( Z )$ is unbounded for $z _ { 1 }  - \infty$ · This contradicts $A N$ -stability.

For the Lobatto IIB methods, one uses in a similar way that the last column of $A$ and the first column of $A - \mathbb { 1 } b ^ { T }$ vanish. □

The following result shows,as mentioned above, that $A N$ -stability is much closer to $B$ -stability than to $A$ -stability.

Theorem 12.13 (Burrage & Butcher 1979). Suppose that

$$
| K ( Z ) | \leq 1 \left\{ \begin{array} { l l } { f o r a l l Z = \mathrm { d i a g } ( z _ { 1 } , \ldots , z _ { s } ) w i t h \mathrm { R e } z _ { \jmath } \leq 0 } \\ { a n d | z _ { \jmath } | \leq \varepsilon f o r s o m e \varepsilon > 0 , } \end{array} \right.
$$

then the method is algebraically stable (and hence also $B$ -stable).

Proof. For $\Delta f _ { \imath } : = z _ { \imath } \Delta g _ { \imath }$ and $\Delta y _ { 0 } = 1$ the result of (12.5) is $\Delta { y } _ { 1 } = K ( Z )$ . Taking care of the fact that $z _ { \imath }$ need not be real, the computation of the proof of Theorem 12.4 shows that

$$
| K ( Z ) | ^ { 2 } - 1 = 2 \sum _ { \imath = 1 } ^ { \imath } b _ { \imath } \mathrm { R e } z _ { \imath } | g _ { \imath } | ^ { 2 } - \sum _ { \imath , \jmath = 1 } ^ { s } m _ { \imath \jmath } \bar { z } _ { \imath } \bar { g } _ { \imath } z _ { \jmath } g _ { \jmath } .
$$

Here $g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T }$ is a solution of (12.14) with $y _ { 0 } = 1$ ·

To prove that $b _ { \imath } \geq 0$ ,choose $z _ { \imath } = - \varepsilon < 0$ and $z _ { \jmath } = 0$ for $j \neq \imath$ . Assumption (12.19) together with (12.20) implies

$$
- 2 \varepsilon b _ { \iota } | g _ { \iota } | ^ { 2 } - m _ { \iota \iota } \varepsilon ^ { 2 } | g _ { \iota } | ^ { 2 } \leq 0 .
$$

For sufficiently small $\varepsilon , g _ { \imath }$ is close to 1 and the second term in(12.21) is negligible for $\boldsymbol { b } _ { \imath } \neq 0$ . Therefore, $b _ { \imath }$ must be non-negative.

To verify the second condition of algebraic stability we choose the purely imaginary numbers $z _ { \jmath } = i \varepsilon \xi _ { \jmath } \left( \xi _ { \jmath } \in \mathbb { R } \right)$ . Since again $g _ { \imath } = 1 + \mathcal { O } ( \varepsilon )$ for $\varepsilon \to 0$ , we have from (12.20) that

$$
- \varepsilon ^ { 2 } \sum _ { \ i , \jmath = 1 } ^ { s } m _ { \imath \jmath } \xi _ { \imath } \xi _ { \jmath } + \mathcal { O } ( \varepsilon ^ { 3 } ) \leq 0 .
$$

Therefore, $M = ( m _ { \imath \jmath } )$ has to be non-negative definite.

Combining this result with those of Theorems 12.4 and 12.11 we obtain

Corollary 12.14. For non-confluent Runge-Kutta methods (i.e., methods with all $c _ { \ j }$ distinct) the concepts of $A N$ -stability, $B$ -stability and algebraic stability are equivalent. □

An equivalence result (between $B$ - and algebraic stability) for confuent Runge-Kutta methods is much more difficult to prove (see Theorem 12.18 below) and will be our next goal. To this end we first have to discuss reducible methods.

# Reducible Runge-Kutta Methods

For an RK-method (12.3) it may happen that for alldiferential equations (12.1)

i） some stages don't influence the numerical solution;   
ii） several $g _ { \imath }$ are identical.

In both situations the Runge-Kuta method can be simplified to an “equivalent" one with fewer stages.

For an illustration of situation (i) consider the method of Table 12.1. Its numerical solution is independent of $g _ { 2 }$ and equivalent to the implicit Euler solution. For the method of Table 12.2 one easily verifies that $g _ { 1 } = g _ { 2 }$ , whenever the system (12.3b) possesses a unique solution. The method is thus equivalent to the implicit mid-point rule.

Table 12.2. $S$ -reducible method   

<table><tr><td>1/2 1/2</td><td>1/2 0 1/4 1/4</td></tr><tr><td></td><td>1/2 1/2</td></tr></table>

Table 12.1. $D J$ -reducible method   
Table 12.3. $D J$ -reducibility   

<table><tr><td>1 1/2</td><td>1 0 1/4 1/4</td></tr><tr><td></td><td>1 0</td></tr></table>

The situation (i) above can be made more precise as follows:

Definition 12.15 (Dahlquist & Jeltsch 1979). A Runge-Kutta method is called $D J$ -reducible, if for some non-empty index set $T \subset \{ 1 , \ldots , s \}$ ，

$$
b _ { _ { J } } = 0 \quad { \mathrm { f o r } } \quad { _ { \mathcal { J } } } \in T \qquad { \mathrm { a n d } } \qquad a _ { _ { \iota _ { \mathcal { J } } } } = 0 \quad { \mathrm { f o r } } \quad i \notin T , { \ i \in T } .
$$

Otherwise it is called $D J$ -irreducible.

Condition (12.22) implies that the stages $\jmath \in T$ don't influence the numerical solution. This is best seen by permuting the stages so that the elements of $T$ are the last ones (Cooper 1985). Then the Runge-Kutta tableau becomes that of Table 12.3.

$$
{ \frac { c _ { 1 } } { c _ { 2 } } } \quad \left| { \begin{array} { c c } { A _ { 1 1 } } & { 0 } \\ { A _ { 2 1 } } & { A _ { 2 2 } } \\ { b _ { 1 } ^ { T } } & { 0 } \end{array} } \right| \qquad \Rightarrow \qquad { \frac { c _ { 1 } } { b _ { 1 } ^ { T } } } \quad \left| { \begin{array} { l } { A _ { 1 1 } } \\ { b _ { 1 } ^ { T } } \end{array} } \right|
$$

An interesting property of $D J$ -irreducible and algebraically stable Runge-Kuta methods was discovered by Dahlquist & Jeltsch (1979).

Theorem 12.16. A $D J$ -irreducible, algebraically stable Runge-Kutta method satisfies

$$
b _ { \ i } > 0 f o r i = 1 , \ldots , s .
$$

Proof. Suppose $b _ { \jmath } = 0$ for some index $j$ . Then $m _ { j j } = 0$ by definition of $M$ . Since $M$ is non-negative definite,all elements in the $j$ th column of $M$ must vanish (Exercise 11） so that $b _ { \imath } a _ { \imath \jmath } = 0$ for all $i$ ．This implies (12.22) for the set $T =$ $\{ j | b _ { j } = 0 \}$ , a contradiction to $D J$ -irreducibility. □

An algebraic criterion for the situation (ii) was given for the first time (but incompletely) by Stetter(1973,p.127) and finally by Hundsdorfer & Spijker(1981), see also Butcher(1987),p.319,and Dekker & Verwer (1984), p.108.

Definition 12.17. A Runge-Kutta method is $S$ -reducible,if for some partition $( S _ { 1 } , \ldots , S _ { r } )$ of $\{ 1 , \ldots , s \}$ with $r < s$ we have for all $l$ and $m$

$$
\sum _ { k \in S _ { m } } a _ { \iota k } = \sum _ { k \in S _ { m } } a _ { \jmath k } \quad \mathrm { i f } \quad \iota , \dot { \jmath } \in S _ { l } .
$$

Otherwise it is called $S$ -irreducible. Methods which are neither $D J$ -reducible nor $S$ -reducible are called irreducible.

In order to understand condition (12.23) we assume that, after a certain permutation of the stages, $l \in S _ { l }$ for $l = 1 , \ldots , r$ . We then consider the $\pmb { \gamma }$ -stage method with coefficients

$$
c _ { \iota } ^ { \ast } = c _ { \iota } , \qquad a _ { \iota \ j } ^ { \ast } = \sum _ { k \in S _ { \jmath } } a _ { \iota k } , \qquad b _ { \jmath } ^ { \ast } = \sum _ { k \in S _ { \jmath } } b _ { k } .
$$

Application of this new method to (12.1) yields $g _ { 1 } ^ { * } , \ldots , g _ { r } ^ { * } , y _ { 1 } ^ { * }$ and one easily verifies that $g _ { \imath }$ and $y _ { 1 }$ defined by

$$
g _ { \ i } = g _ { l } ^ { \ast } \quad \mathrm { i f } \quad i \in S _ { l } , \qquad y _ { 1 } = y _ { 1 } ^ { \ast } ,
$$

are a solution of the original method (12.3). For the method of Table 12.2 we have $S _ { 1 } = \{ 1 , 2 \}$ . A further example of an $S$ -reducible method is given in Table 12.4 of Sect.II.12 ( $\mathbfcal { S } _ { 1 } = \{ 1 , 2 , 3 \}$ and $S _ { 2 } = \{ 4 \}$ ）.

# The Equivalence Theorem for $S$ -Irreducible Methods

Theorem 12.18 (Hundsdorfer & Spijker 1981). For $S$ -irreducible Runge-Kuta methods,

Proof. Because of Corollary 12.14,which covers nearly all cases of practical importance - and which was much easier to prove - this theorem seems to be of little practical interest. However, it is an interesting result which had been con-jectured by many people for many years, so we reproduce its proof, which also includes the three Lemmas 12.19-12.21. The counter example of Exercise 6 below shows that $S$ -irreducibility is a necessary hypethesis.

By Theorem 12.4 it is sufficient to prove that $B$ -stability and $S$ -irreducibility imply algebraic stability. For this we take s complex numbers $z _ { 1 } , \dots , z _ { s }$ which satisfy $\mathrm { R e } z _ { _ { \jmath } } < 0$ and $| z _ { \jmath } | \leq \varepsilon$ for some sufficiently small $\varepsilon > 0$ . We show that there exists a continuous function $f : \mathbb { C } \to \mathbb { C }$ satisfying

$$
\operatorname { R e } { \big \langle } f ( u ) - f ( v ) , u - v { \big \rangle } \leq 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } u , v \in \mathbb { C } ~ ,
$$

such that the Runge-Kutta solutions $y _ { 1 } , g _ { \imath }$ and $\widehat { y } _ { 1 } , \widehat { g } _ { \iota }$ corresponding to $y _ { 0 } = 0$ ， $\widehat { y } _ { 0 } = 1$ ， $h \approx 1$ satisfy

$$
f ( { \widehat { g } } _ { \imath } ) - f ( g _ { \imath } ) = z _ { \imath } ( { \widehat { g } } _ { \imath } - g _ { \imath } ) .
$$

This yields $\widehat { y } _ { 1 } - y _ { 1 } = K ( Z )$ with $K ( Z )$ given by (12.15). $B$ -stability then implies $| K ( Z ) | \le 1$ . By continuity of $K ( Z )$ near the origin we then have $| \mathit { K } ( Z ) | \le 1$ for all $z _ { \jmath }$ which satisfy $\mathrm { R e } z _ { \jmath } \leq 0$ and $| z _ { \jmath } | \leq \varepsilon$ ， so that Theorem 12.13 proves the statement.

Construction of the function $f$ : we denote by $\Delta g _ { i }$ the solution of

$$
\Delta g _ { \imath } = 1 + \sum _ { \jmath = 1 } ^ { s } a _ { i j } z _ { \jmath } \Delta g _ { \jmath }
$$

(the solution exists uniquely if $| z _ { \jmath } | \leq \varepsilon$ and $\varepsilon$ is sufficiently small). With $\xi , \eta$ given by Lemma 12.19 (below) we define

$$
\begin{array} { l l } { { g _ { \iota } = t \eta _ { \iota } , } } & { { f ( g _ { \iota } ) = t \xi _ { \iota } } } \\ { { \widehat { g } _ { \iota } = g _ { \iota } + \Delta g _ { \iota } , } } & { { f ( \widehat { g } _ { i } ) = f ( g _ { \iota } ) + z _ { \iota } \Delta g _ { \iota } . } } \end{array}
$$

This is well-defined for sufficiently large $t$ (to be fixed later), because the $\eta _ { \imath }$ are distinct. Clearly, $g _ { \imath }$ and $\widehat { \boldsymbol { g } } _ { \imath }$ represent a Runge-Kutta solution for $y _ { 0 } = 0$ and $\widehat { y } _ { 0 } = 1$ ， and (12.26) is satisfied by definition.

We next show that

$$
\operatorname { R e } { \big \langle } f ( u ) - f ( v ) , u - v { \big \rangle } < 0 \qquad { \mathrm { i f } } \qquad u \neq v
$$

is satisfied for $u , v \in D = \{ g _ { 1 } , \dotsc , g _ { s } , \widehat { g } _ { 1 } , \dotsc , \widehat { g } _ { s } \}$ . This follows from the construction of $\xi , \eta$ ,if $u , v \in \{ g _ { 1 } , \dotsc , g _ { s } \}$ . If $u \simeq g _ { \tau }$ and $\boldsymbol { v } = \widehat { \boldsymbol { g } } _ { \iota }$ this is a consequence of (12.26). For the remaining case $u = \widehat { g } _ { \iota } , v \in D \setminus \{ g _ { \iota } , \widehat { g } _ { \iota } \}$ we have

$$
\langle f ( u ) - f ( v ) , u - v \rangle = t ^ { 2 } ( \xi _ { \imath } - \xi _ { \jmath } ) ( \eta _ { \imath } - \eta _ { \jmath } ) + \mathcal { O } ( t ) \quad \mathrm { f o r } \quad t \to \infty ,
$$

so that (12.28) is satisfied, if $t$ is sufficiently large. Applying Lemma 12.20 below we find a continuous function $f : \mathbb { C } \to \mathbb { C }$ that extends (12.27) and satisfies (12.25).

To complete the above proof we still need the following three lemmas:

Lemma 12.19. Let $A$ be the coeffcient matrix of an $S$ -irreducible Runge-Kutta method. Then there exist vectors $\xi \in \mathbb { R } ^ { s }$ and $\eta = A \xi$ such that

$$
( \xi _ { \iota } - \xi _ { \jmath } ) ( \eta _ { \iota } - \eta _ { \jmath } ) < 0 f o r i \neq j .
$$

Proof (see Butcher 1982). The first idea is to put

$$
\boldsymbol { \xi } = \mathbb { 1 } - \varepsilon A \mathbb { 1 } \quad \mathrm { w i t h } \quad \mathbb { 1 } \mathbb { = } ( 1 , 1 , \dots , 1 ) ^ { T } ,
$$

so that $\eta$ becomes

$$
\eta = A \xi = A \mathbb { 1 } - \varepsilon A ^ { 2 } \mathbb { 1 } .
$$

f $c _ { \imath } \neq c _ { \jmath }$ for all $i , j$ ,then $\xi _ { i } - \xi _ { { \scriptscriptstyle 3 } } \neq 0$ and for $\varepsilon$ sufficientlysmall we have $\eta _ { i } - \eta _ { j }$ of opposite sign, thus (12.29) is true.

For a proof of the remaining cases,we shall construct recursively vectors $v _ { 0 } , v _ { 1 } , v _ { 2 } , \ldots$ and denote by $P _ { k }$ the partition of $\{ 1 , \ldots , s \}$ defined by the equivalence relation

$$
i \sim j \quad \iff \quad ( \boldsymbol { v } _ { q } ) _ { \iota } = ( \boldsymbol { v } _ { q } ) _ { \jmath } \quad \mathrm { f o r } \quad q = 0 , 1 , \ldots , k .
$$

For a given partition $P$ of $\{ 1 , 2 , \ldots , s \}$ we introduce the space

$$
X ( P ) = \{ v \in \mathbb { R } ^ { s } ; ( v ) _ { \imath } = ( v ) _ { j } \quad { \mathrm { i f } } \quad i \sim j \quad { \mathrm { w i t h r e s p e c t t o ~ } } P \} .
$$

With this notation,the method is $S$ -irreducible if and only if

$$
A X ( P ) \not \subset X ( P )
$$

for every partition other than $\{ \{ 1 \} , \{ 2 \} , \dots , \{ s \} \}$

We start with $v _ { 0 } = \mathbb { 1 }$ and $P _ { 0 } = \{ \{ 1 , . . . , s \} \}$ and define

$$
v _ { k + 1 } = \left\{ \begin{array} { l l } { A v _ { k } \quad } & { \mathrm { i f } A v _ { k } \notin X ( P _ { k } ) } \\ { \omega } & { \mathrm { i f } A v _ { k } \in X ( P _ { k } ) } \end{array} \right.
$$

where $\omega$ is an arbitrary vector of $X ( P _ { k } )$ satisfying $A \omega \notin X ( P _ { k } )$ . Such a choice is possible by (12.31). After a finite number of steps, say $m$ ，we arrive at $P _ { m } =$ $\{ \{ 1 \} , \{ 2 \} , \dots , \{ s \} \}$ , because the number of components of $P _ { k }$ is increasing, and strictly increasing after every second step. Therefore all elements of the vector

$$
\xi = v _ { 0 } - \varepsilon v _ { 1 } + \varepsilon ^ { 2 } v _ { 2 } - . . . + ( - \varepsilon ) ^ { m } v _ { m }
$$

are distinct (for sufficiently small $\varepsilon > 0$ ) and (12.29) is satisfied.

Lemma 12.20 (Minty 1962). Let $\mathcal { U } _ { 1 } , \dots , \mathcal { U } _ { k }$ and $f ( u _ { 1 } ) , \ldots , f ( u _ { k } )$ be elements of $\mathbb { R } ^ { n }$ with

$$
\langle f ( u _ { \ i } ) - f ( u _ { \ j } ) , u _ { \ i } - u _ { \ j } \rangle < 0 \qquad f o r \quad i \neq \jmath .
$$

Then there exists a continuous extension $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ satisfying

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 \qquad f o r a l l \quad u , v \in \mathbb { R } ^ { n } .
$$

Proof (Wakker 1985).Define

$$
\gamma = \operatorname* { m a x } _ { \iota \neq j } \frac { \langle f ( u _ { \iota } ) - f ( u _ { \iota } ) , u _ { \iota } - u _ { \jmath } \rangle } { | | f ( u _ { \iota } ) - f ( u _ { \jmath } ) | | ^ { 2 } } < 0
$$

and put $g ( u _ { \iota } ) = 2 \gamma f ( u _ { \iota } ) - u _ { \iota }$ ,so that $\| g ( u _ { \ i } ) - g ( u _ { \ j } ) \| \leq \| u _ { \ i } - u _ { \ j } \|$ . An applica-tion of Lemma 12.21 shows that there exists a continuous extension $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ satisfying $\| g ( u ) - g ( v ) \| \leq \| u - v \|$ (i.e., $g$ is non-expansive). The function

$$
f ( u ) = \frac { 1 } { 2 \gamma } \big ( g ( u ) + u \big )
$$

then satisfies the requirements.

Lemma 12.21 (Kirszbraun 1934). Let $u _ { 1 } , \ldots , u _ { k }$ and $g ( u _ { 1 } ) , \dots , g ( u _ { k } ) \in \mathbb { R } ^ { n } b e$ such that

$$
| | g ( u _ { \ i } ) - g ( u _ { \ j } ) | | \leq | | u _ { \ i } - u _ { \ j } | | \qquad f o r \ i , j = 1 , \ldots , k .
$$

Then there exists a continuous extension $g : \mathbb { R } ^ { n }  \mathbb { R } ^ { n }$ such that

$$
\left\| g ( u ) - g ( v ) \right\| \leq \left\| u - v \right\| \qquad f o r a l l \quad u , v \in \mathbb { R } ^ { n } .
$$

Proof. This was once a difficult result in set-theory. A particularly nice proof, of which we give here a “dynamic" version, has been found by I.J. Schoenberg(1953).

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0003_pages_0141-0210/auto/images/a4c3448ac40215ca50a7afd5804ce8597378870d6cfb00a3890e7237bfcef4f4.jpg)  
Fig.12.1. Construction of $g ( p )$

a) The main problem is to construct for one given point $p$ the extension $g ( p )$ such that (12.33) remains satisfied. We move the points $u _ { \imath }$ into their images $g ( u _ { \ i } )$ by an affine map

$$
u _ { \ i } ( \lambda ) = u _ { \ i } + \lambda ( g ( u _ { \ i } ) - u _ { \ i } ) , \qquad 0 \le \lambda \le 1 , \ i = 1 , \dots , k .
$$

We define $\boldsymbol { r } _ { \imath } = \| u _ { \imath } - p \|$ and shrink, for each $\lambda$ , the balls with center $u _ { \imath } ( \lambda )$ and radius $r _ { \ i } \mu$ until their intersection consists of one point only

$$
\mu ( \lambda ) : = \operatorname* { m i n } \Bigl \{ \mu ; \bigcap _ { i = 1 } ^ { k } \bigl \{ u ; \| u _ { \iota } ( \lambda ) - u \| \le r _ { \iota } \mu \bigr \} \neq \emptyset \Bigr \} .
$$

This intersection point, denoted by $p ( \lambda )$ (see Fig.12.1),depends continuously (except for a possible sudden decrease of $\mu$ if $\lambda = 0$ ） and piecewise differentiably on $\lambda$ . We shall show that $\mu ( \lambda )$ is non-increasing, which means that $g ( p ) : = p ( 1 )$ is a point satisfying (12.33).

We denote the vectors

$$
R _ { \iota } : = u _ { \iota } ( \lambda ) - p ( \lambda ) ,
$$

and have from the hypothesis (12.32) that $\| R _ { \imath } - R _ { \jmath } \| ^ { 2 }$ is non-increasing, hence that $\langle R _ { \iota } - R _ { j } , d R _ { \iota } - d R _ { j } \rangle \leq 0$ or

$$
\langle R _ { \imath } , d R _ { \jmath } \rangle + \langle R _ { \jmath } , d R _ { \imath } \rangle \geq \langle R _ { \imath } , d R _ { \imath } \rangle + \langle R _ { \jmath } , d R _ { \jmath } \rangle .
$$

As can be seen in Fig.12.1, not all points $u _ { \ i } ( \lambda )$ are always “active” in (12.35), i.e., $p ( \lambda )$ lies on the boundary of the shrinked ball centered in $u _ { \ i } ( \lambda )$ . While for $\lambda \simeq 0$ (for which $\| R _ { \imath } \| = r _ { \imath } \mu )$ all four are active,at $\lambda = 1 / 2$ the active points are $u _ { 1 } ( \lambda ) , u _ { 2 } ( \lambda ) , u _ { 3 } ( \lambda )$ ， and finally for $\lambda \simeq 1$ we only have $u _ { 1 } ( \lambda )$ and $u _ { 2 } ( \lambda )$ active. We suppose, for a given $\lambda$ ， that $u _ { 1 } ( \lambda ) , \ldots , u _ { m } ( \lambda ) \ ( m \leq \bar { k } )$ are the active points,which may sometimes require a proper renumbering. The crucial idea of Schoenberg is the fact that $p ( \lambda )$ lies in the convex hull of $u _ { 1 } ( \lambda ) , \dots , u _ { m } ( \lambda )$ ,i.e., there are positive values $c _ { 1 } ( \lambda ) , \ldots , c _ { m } ( \lambda )$ with $\scriptstyle \sum _ { \imath = 1 } ^ { m } c _ { \imath } R _ { \imath } = 0$ . This means that

$$
\begin{array} { r } { \langle \sum _ { \iota } c _ { \iota } R _ { \iota } , \sum _ { \jmath } c _ { \jmath } d R _ { \jmath } \rangle = 0 . } \end{array}
$$

We here apply (12.37) pairwise to $i , j$ and $j , i$ , and obtain

$$
\begin{array} { r } { 0 = \langle \sum _ { \iota } c _ { \iota } R _ { \iota } , \sum _ { \jmath } c _ { \jmath } d R _ { \jmath } \rangle \geq \sum _ { \iota } \langle R _ { \imath } , d R _ { \imath } \rangle \big ( c _ { \iota } \sum _ { \jmath } c _ { \jmath } \big ) . } \end{array}
$$

Since by construction (see (12.36)) all $\Vert R _ { \imath } \Vert$ decrease or increase simultaneously with $\mu$ , and since all $c _ { \scriptscriptstyle \imath } > 0$ , we see that $d \mu \leq 0$ ,i.e., $\mu$ is non-increasing.

b) The rest is now standard (Kirszbraun): we choose a countable dense sequence of points $p _ { 1 } , p _ { 2 } , p _ { 3 } , . . .$ in $\mathbb { R } ^ { n }$ and extend $g$ gradually to these points, so that (12.33) is always satisfied. By continuity (see (12.33)),our function is then defined everywhere. This completes the proof of Lemma 12.21 and with it the proof of Theorem 12.18. □

Nous ne connaissons pas d'exemples de méthodes qui soient $B$ - stables au sens de Butcher et qui ne soient pas $B$ -stables suivant notre definition. (M. Crouzeix 1979)

Remark. Burrage & Butcher (1979) distinguish between $B N$ -stability (based on non-autonomous systems) and $B$ -stability (based on autonomous systems). Since the differential equation constructed in the above proof (see (12.25)) is autonomous, both concepts are equivalent for irreducible methods.

# Error Growth Function

All the above theory deals only with contractivity when the one-sided Lipschitz constant $\nu$ in (12.2) is zero (see Definition 12.2). The question arises whether we can sharpen the estimate when it is known that $\nu < 0$ , and whether we can obtain estimates also in the case when (12.2) holds only for some $\nu > 0$

Definition 12.22 (Burrage & Butcher 1979). Let $\nu$ be given and set $x = h \nu$ ,where $h$ is the step size. We then denote by $\varphi _ { B } ( x )$ the smallest number for which the estimate

$$
\| y _ { 1 } - { \widehat { y } } _ { 1 } \| \leq \varphi _ { B } ( x ) \| y _ { 0 } - { \widehat { y } } _ { 0 } \|
$$

holds for all problems satisfying

$$
\operatorname { R e } { \big \langle } f ( x , y ) - f ( x , z ) , y - z { \big \rangle } \leq \nu \| y - z \| ^ { 2 } .
$$

We call $\varphi _ { B } ( x )$ the error growth function of the method.

We consider here complex-valued functions $f : \mathbb { R } \times \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$ ．This is not more general (any such system can be written in real form by considering real and imaginary parts, see Eq.(12.4)), but it is more convenient when working with problems $y ^ { \prime } = \lambda ( x ) y$ ，where $\lambda ( x )$ is complex-valued.

In the case of a linear nonautonomous problem $y ^ { \prime } = A ( x ) y$ ,condition (12.39) becomes $\mu ( A ( x ) ) \leq \nu$ (where $\mu ( \cdot )$ denotes the logarithmic norm; see Sect.I.10). Putting $Z _ { \iota } : = h A ( x _ { 0 } + c _ { \iota } h )$ , the difference of two numerical solutions becomes

$$
y _ { 1 } - { \widehat { y } } _ { 1 } = K ( Z _ { 1 } , \ldots , Z _ { s } ) ( y _ { 0 } - { \widehat { y } } _ { 0 } ) ,
$$

where

$$
K ( Z _ { 1 } , \ldots , Z _ { s } ) = I + ( b ^ { T } \otimes I ) Z \bigl ( I \otimes I - ( A \otimes I ) Z \bigr ) ^ { - 1 } ( \mathbb { 1 } \otimes I ) ,
$$

and $Z$ is the block diagonal matrix with $Z _ { 1 } , \dots , Z _ { s }$ as entries in the diagonal.

Theorem 12.23. The error growth function of an implicit Runge-Kutta method satisfies

$$
\varphi _ { B } ( x ) = \operatorname* { s u p } _ { \mu ( Z _ { 1 } ) \leq x , \ldots , \mu ( Z _ { s } ) \leq x } | | K ( Z _ { 1 } , \ldots , Z _ { s } ) | | .
$$

Proof. Upper Bound. The difference $\Delta { y } _ { 1 } = { y } _ { 1 } - \widehat { y } _ { 1 }$ of two Runge-Kutta solutions satisfies (12.5). The assumption (12.39) implies that $\mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { i } \right. \leq x \| \Delta g _ { i } \| ^ { 2 }$ We shall prove that there exist matrices $Z _ { i }$ $( i = 1 , \ldots , s )$ with $\mu ( Z _ { \imath } ) \leq x$ such that $\Delta f _ { \imath } = Z _ { \imath } \Delta g _ { \imath }$ . This implies $\Delta y _ { 1 } = K ( Z _ { 1 } , \dots , Z _ { s } ) \Delta y _ { 0 }$ and,as a consequence, that the right-hand expression of Eq.(12.41) is an upper bound of $\varphi _ { B } ( x )$

f $\Delta g _ { \imath } = 0$ then $\Delta f _ { \imath } = 0$ and we can take an arbitrary matrix satisfying $\mu ( Z _ { \imath } ) \leq$ $x$ . Therefore,let us consider vectors $f , g$ (with $g \neq 0$ in $\mathbb { C } ^ { n }$ satisfying $\operatorname { R e } \left. f , g \right. \leq$ $x \| g \| ^ { 2 }$ . We put $u _ { 1 } : = g / \| g \|$ ,and complete it to an orthonormal basis $\boldsymbol { u } _ { 1 } , \ldots , \boldsymbol { u } _ { n }$


<!-- chunk 0004: pages 211-280 -->
of $\mathbb { C } ^ { n }$ . Then we define the matrix $Z$ by

$$
Z u _ { 1 } : = f / \| g \| , \qquad \quad Z u _ { \mathit { \iota } } : = x u _ { \iota } - \langle u _ { \iota } , f \rangle u _ { 1 } / \| g \| , \quad \quad i = 2 , \ldots , n .
$$

We have $Z g = f$ , and one readily verifies that $\operatorname { R e } \langle Z v , v \rangle \leq x \| v \| ^ { 2 }$ for all $v =$ $\textstyle \sum _ { \imath = 1 } ^ { n } \alpha _ { \imath } u _ { \imath }$

Lower Bound. We first consider nonconfluent Runge-Kutta methods. For given $Z _ { 1 } , \dots , Z _ { s }$ with $\mu ( Z _ { \imath } ) \leq x$ let $A ( x )$ be a continuous function satisfying $h A ( x _ { 0 } +$ $c _ { \ i } h ) = Z _ { i }$ and $\mu ( A ( x ) ) \leq x$ for all $_ x$ （ $\vert A ( x )$ is,for example, obtained by linear interpolation). Then we have $\Delta y _ { 1 } = K ( Z _ { 1 } , \dots , Z _ { s } ) \Delta y _ { 0 }$ and, consequently, also $\varphi _ { B } ( x ) \geq \| K ( Z _ { 1 } , \ldots , Z _ { s } ) \|$ for all $Z _ { 1 } , \dots , Z _ { s }$ with $\mu ( Z _ { i } ) \leq x$

For confluent methods the proof is more complicated. Without loss of general-  
ity we can assume that the method is irreducible, because neither the value $\varphi _ { B } ( x )$   
nor the right-hand expression of Eq.(12.41) change, when the method is replaced   
by an equivalent one. The main observation is now that the Lemmata 12.20 and $Z _ { 1 } , \dots , Z _ { s }$ $\mu ( Z _ { \imath } ) \leq x$ $\begin{array} { r } { \Delta g _ { \ i } = \Delta y _ { 0 } + \sum _ { \ j = 1 } ^ { s } a _ { i \ j } Z _ { \ j } \Delta \bar { g } _ { \it j } } \end{array}$ $f : \mathbb { C } ^ { n } \to \mathbb { C } ^ { n }$   
which satisfies (12.39) with $\nu \simeq x$ (we put $h = 1$ )and $f ( g _ { \imath } ) - f ( \widehat { g } _ { \imath } ) = Z _ { \imath } ( g _ { \imath } - \widehat { g } _ { \imath } )$   
This completes the proof of the theorem. □

For 1 -stage methods ( $( s = 1 )$ ）the Theorem of von Neumann (Corollary 11.4) implies that it is sufficient to consider scalar, complex-valued $z _ { 1 }$ in Eq. (12.41). Since $\begin{array} { r } { K ( z ) = R ( z ) } \end{array}$ in this case, we have

$$
\varphi _ { B } ( x ) = \varphi _ { R } ( x ) \qquad { \mathrm { f o r ~ a l l ~ 1 \mathrm { - } s t a g e ~ m e t h o d s . } }
$$

For the moment it is not clear, whether one can restrict the supremum in Eq.(12.41) to scalar, complex-valued $z _ { \imath }$ also for $s \geq 2$ . This would require a generalization of the Theorem of von Neumann to functions of more than one variables (Hairer & Wanner 1996). We shall come back to this question later in this section.

Theorem 12.24 (Hairer & Zennaro 1996). For $B$ -stable Runge-Kutta methods the error growth function is superexponential, i.e., $\varphi _ { B } ( 0 ) = 1$ and

$$
\varphi _ { B } ( x _ { 1 } ) \varphi _ { B } ( x _ { 2 } ) \leq \varphi _ { B } ( x _ { 1 } + x _ { 2 } ) \qquad f o r ~ x _ { 1 } , x _ { 2 } ~ h a \nu i n g ~ t h e ~ s a m e ~ s i g n .
$$

Proof. The property $\varphi _ { B } ( 0 ) = 1$ follows from Definition 12.5. For the proof of the inequality we consider the rational function

$$
S ( z ) = u _ { A } ^ { * } K ( A _ { 1 } - z I , \ldots , A _ { s } - z I ) v _ { A } u _ { B } ^ { * } K ( B _ { 1 } + z I , \ldots , B _ { s } + z I ) v _ { B } ,
$$

where the matrices $A _ { \ j } , B _ { \ j }$ satisfy $\mu ( A _ { \ j } ) \leq x _ { 1 } + x _ { 2 }$ and $\mu ( B _ { \jmath } ) \leq 0$ ,and $u _ { A } , v _ { A } ,$ $u _ { B } , v _ { B }$ are arbitrary vectors of $\mathbb { C } ^ { n }$ .Using the property $\mu ( { \dot { A } } _ { \ j } - z I ) = \mu ( A _ { \ j } ) -$ $\mathrm { R e } z$ and the fact that $\begin{array} { r } { \| C \| = \operatorname* { s u p } _ { \| u \| = 1 , \| v \| = 1 } \left| u ^ { * } C v \right| } \end{array}$ , the inequality is obtained exactly as in the proof of Theorem 11.6. □

The fact that $\varphi _ { B } ( x )$ is superexponential together with $\varphi _ { B } ( - \infty ) = | R ( \infty ) |$ (see Exercise 8) allows us to draw the same conclusions on asymptotic stability of numerical solutions as in Sect.IV.11.

# Computation of $\varphi _ { B } ( { \pmb x } )$

The idea is to search for the maximum of $\| \Delta y _ { 1 } \|$ under the restriction (12.39). More precisely, we consider the following inequality constrained optimization problem:

$$
\begin{array} { r l } & { \| \Delta y _ { 1 } \| ^ { 2 } \to \operatorname* { m a x } , } \\ & { \operatorname { R e } \left. \Delta f _ { i } , \Delta g _ { \ i } \right. \le x \| \Delta g _ { \ i } \| ^ { 2 } , \quad i = 1 , \ldots , s . } \end{array}
$$

Here $\Delta f _ { 1 } , \ldots , \Delta f _ { s }$ are regarded as independent variables in $\mathbb { C } ^ { n } , \Delta y _ { 1 }$ and $\Delta g _ { \imath }$ are defined by (12.5), and $\Delta y _ { 0 }$ is considered as a parameter. A classical approach for solving the optimization problem (12.43) is to introduce Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ , and to consider the Lagrangian

$$
\begin{array} { r l r } & { } & { \mathcal { L } ( \Delta f , D ) = \displaystyle \frac { 1 } { 2 } \| \Delta y _ { 1 } \| ^ { 2 } - \sum _ { \imath = 1 } ^ { s } d _ { \imath } \left( \mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { \imath } \right. - x \| \Delta g _ { \imath } \| ^ { 2 } \right) } \\ & { } & { = - \displaystyle \frac { 1 } { 2 } \left( \Delta y _ { 0 } ^ { * } , \Delta f ^ { * } \right) \left( \left( \begin{array} { c c } { \alpha } & { u ^ { T } } \\ { u } & { W } \end{array} \right) \otimes I \right) \left( \begin{array} { c } { \Delta y _ { 0 } } \\ { \Delta f } \end{array} \right) , } \end{array}
$$

where $\Delta f = ( \Delta f _ { 1 } , \dots , \Delta f _ { s } ) ^ { T }$ ， $D = \operatorname { d i a g } \left( d _ { 1 } , \dots , d _ { s } \right)$ , and

$$
\begin{array} { r l } & { \alpha = - 1 - 2 x \mathbb { 1 } ^ { T } D \mathbb { 1 } , } \\ & { \quad u = D \mathbb { 1 } - b - 2 x A ^ { T } D \mathbb { 1 } , } \\ & { \quad W = D A + A ^ { T } D - b b ^ { T } - 2 x A ^ { T } D A . } \end{array}
$$

Theorem 12.25 (Burrage & Butcher 1980). If the matrix

$$
\left( \begin{array} { c c } { { \alpha + \varphi ^ { 2 } } } & { { u ^ { T } } } \\ { { u } } & { { W } } \end{array} \right) \qquad i s p o s i t i v e s e m i - d e f t n i t e
$$

for some $d _ { 1 } \geq 0 , \ldots , d _ { s } \geq 0$ ， then it holds $\| \Delta y _ { 1 } \| \le \varphi \| \Delta y _ { 0 } \|$ for all problems satisfying (12.39) with $h \nu \leq x$ . Consequently, we have $\varphi _ { B } ( x ) \leq \varphi$

Proof. Substracting $\varphi ^ { 2 } \| \Delta y _ { 0 } \| ^ { 2 } / 2$ from both sides of (12.44) yields

$$
\frac { 1 } { 2 } \Big ( \| \Delta y _ { 1 } \| ^ { 2 } - \varphi ^ { 2 } \| \Delta y _ { 0 } \| ^ { 2 } \Big ) - \sum _ { \iota = 1 } ^ { s } d _ { \iota } \Big ( \mathrm { R e } \left. \Delta f _ { \iota } , \Delta g _ { \iota } \right. - x \| \Delta g _ { \iota } \| ^ { 2 } \Big ) \leq 0 .
$$

The statement then follows from $d _ { \imath } \geq 0$ and $\mathrm { R e } \left. \Delta f _ { \imath } , \Delta g _ { \imath } \right. \leq x \| \Delta g _ { \imath } \| ^ { 2 }$

With the help of this theorem, Burrage & Butcher (1980) computed an upper bound of $\varphi _ { B } ( x )$ for many 2-stage methods. It turned out that for al these 2 -stage methods $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ ,where

$$
\varphi _ { K } ( x ) = \operatorname* { s u p } _ { \substack { \mathrm { R e } z _ { 1 } \leq x , \dots , \mathrm { R e } z _ { s } \leq x } } | K ( z _ { 1 } , \dots , z _ { s } ) | .
$$

There naturally arises the question: is it true that $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ for all Runge-Kutta methods? If we want to check the validity of $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ for a given Runge-Kutta method, we have to find non-negative Lagrange multipliers $d _ { \imath }$ ,such that (12.46) is satisfied. The following lemmas will be useful for this purpose.

We denote by $z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 }$ the values, for which the supremum in Eq.(1.47) is attained. By the maximum principle we have $z _ { \jmath } ^ { 0 } = x + i y _ { \jmath } ^ { 0 }$ $( y _ { \jmath } ^ { 0 } = \infty$ is admitted). We further put $z ^ { 0 } = ( z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 } )$ and let $\partial _ { j } K ( z ^ { 0 } )$ be the derivative of $K ( z _ { 1 } , \ldots , z _ { s } )$ with respect to the $j$ th argument, evaluated at $z ^ { 0 }$ ·

Lemma 12.26. Let x be fxed with $\varphi _ { K } ( x ) < \infty$ . The condition (12.46) with $\varphi = \varphi _ { K } ( x )$ then uniquely determines the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ (see $E q . \left( l 2 . 5 3 \right) b e l o w \rangle$ . They are real and positive.

Proof. Consider the identity (12.44) for the special case,where $\Delta f _ { \jmath }$ is scalar, $\Delta f _ { _ { \jmath } } = z _ { _ { \jmath } } \Delta g _ { _ { \jmath } }$ ,and hence $\Delta y _ { 1 } = K ( z _ { 1 } , \dots , z _ { s } )$ . For $\operatorname { R e } z _ { \jmath } = x$ this identity becomes

$$
| K ( z _ { 1 } , \dots , z _ { s } ) | ^ { 2 } - \varphi ^ { 2 } = - ( 1 , \Delta f ^ { * } ) \binom { \alpha + \varphi ^ { 2 } } { u } \binom { u ^ { T } } { \Delta f } \cdot
$$

Putting $\varphi : = \varphi _ { K } ( x )$ and $z _ { \jmath } : = z _ { \jmath } ^ { 0 }$ (eventually one has to consider limits) the lefthand expression of Eq.(12.48) vanishes. This together with assumption (12.46) implies that $u + W \Delta f = 0$ ,i.e.,

$$
D \mathbb { 1 } - \boldsymbol { b } - 2 x \boldsymbol { A } ^ { T } \boldsymbol { D } \mathbb { 1 } + \left( \boldsymbol { D } \boldsymbol { A } + \boldsymbol { A } ^ { T } \boldsymbol { D } - \boldsymbol { b } \boldsymbol { b } ^ { T } - 2 x \boldsymbol { A } ^ { T } \boldsymbol { D } \boldsymbol { A } \right) \Delta f = 0 .
$$

Collecting suitable terms, and using $\Delta f = Z _ { 0 } \Delta g$ and $\Delta g = \mathbb { 1 } + A \Delta f$ , where $Z _ { 0 } =$ diag $\big ( z _ { 1 } ^ { 0 } , \dots , z _ { s } ^ { 0 } \big )$ ,this relation becomes

$$
D \Delta g = ( I - A ^ { T } Z _ { 0 } ^ { * } ) ^ { - 1 } \boldsymbol { b } \cdot \boldsymbol { K } ( z ^ { 0 } ) .
$$

We shall show that all components of $\Delta g = ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 }$ are different from zero, so that (12.49) uniquely determines the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ ·

Expanding $K ( z _ { 1 } , \ldots , z _ { s } )$ into a Taylor series with respect to $z _ { \jmath }$ , we obtain

$$
K ( z _ { 1 } ^ { 0 } , \ldots , z _ { j } , \ldots , z _ { s } ^ { 0 } ) = K ( z ^ { 0 } ) \Bigl ( 1 + c ( z _ { j } - z _ { j } ^ { 0 } ) + \mathcal { O } \bigl ( ( z _ { j } - z _ { j } ^ { 0 } ) ^ { 2 } \bigr ) \Bigr ) ,
$$

where $c = \partial _ { j } K ( z ^ { 0 } ) / K ^ { \prime } ( z ^ { 0 } )$ . Since $| K ( z _ { 1 } ^ { 0 } , \dots , z _ { \jmath } , \dots , z _ { s } ^ { 0 } ) | \le | K ^ { \prime } ( z ^ { 0 } ) |$ for $\mathrm { R e } z _ { j } \le$ $\mathrm { R e } z _ { \jmath } ^ { 0 }$ ，we have $c > 0$ , and consequently also

$$
\partial _ { j } K ( z ^ { 0 } ) \neq 0 , \qquad 0 < \partial _ { \ j } K ( z ^ { 0 } ) / K ( z ^ { 0 } ) < \infty .
$$

Differentiating $K ( z _ { 1 } , \dots , z _ { s } ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 }$ 1 with respect to $z _ { \jmath }$ yields

$$
\partial _ { \ j } K ( z ^ { 0 } ) = b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } \boldsymbol { e } _ { \jmath } \boldsymbol { e } _ { \jmath } ^ { T } ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 } ,
$$

and we obtain from (12.50) that

$$
b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } e _ { \jmath } \neq 0 , \qquad \quad \Delta g _ { \jmath } = e _ { \jmath } ^ { T } ( I - A Z _ { 0 } ) ^ { - 1 } \mathbb { 1 } \neq 0 ,
$$

so that $d _ { 1 } , \ldots , d _ { s }$ are uniquely determined by(12.49). Dividing the $j$ th component of (12.49) by $\Delta g _ { \jmath }$ , it follows from (12.51) that

$$
d _ { \jmath } = | b ^ { T } ( I - Z _ { 0 } A ) ^ { - 1 } e _ { \jmath } | ^ { 2 } \cdot \frac { K ( z ^ { 0 } ) } { \partial _ { \jmath } K ( z ^ { 0 } ) } ,
$$

which is a strictly positive real number by (12.50) and (12.52).

In this proof we have implicitly assumed that all $z _ { \jmath } ^ { 0 }$ are finite. If $z _ { \jmath } ^ { 0 } = x + i \infty$ for some $j$ ， one has to apply the standard transformation $\omega _ { \ j } = x + \mathrm { 1 } / ( z _ { \ j } - x )$ ， which maps the half-plane $\mathrm { R e } z _ { \jmath } \leq x$ onto $\mathrm { R e } \omega _ { \ j } \leq x$ ,and $\infty$ into $0$ □

Lemma 12.27. If the matrix W of Eq. $( l 2 . 4 5 c )$ with $d _ { 1 } , \ldots , d _ { s }$ given by Lemma 12.26, is positive semi-definite, then we have $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$

Proof. It follows from

$$
\left( \begin{array} { c c } { { \alpha + \varphi _ { k } ^ { 2 } ( x ) } } & { { u ^ { T } } } \\ { { u } } & { { W } } \end{array} \right) \left( \begin{array} { c } { { 1 } } \\ { { \Delta f } } \end{array} \right) = 0
$$

(see Eq.(12.48)) and from $v ^ { T } W v \geq 0$ for all $v \in \mathbb { R } ^ { s }$ that the matrix in (12.54) is positive semi-definite. The statement then follows from Theorem 12.25. □

With the above results it is possible to check for a given Runge-Kutta method, whether $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ is satisfied. This can be done by the following algorithm:

compute $\varphi = \varphi _ { K } ( x )$ of Eq. (12.47) either numerically or with help of a formula manipulation program;   
， compute the Lagrange multipliers $d _ { 1 } , \ldots , d _ { s }$ from Lemma 12.26;   
· check, whether the matrix $W$ of Eq.(12.45c) is positive semi-definite. If this is the case, it holds $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$ by Lemma 12.27.

Example 12.28. For the two-stage Radau IIA method (see Table 5.5) the function $K ( z _ { 1 } , z _ { 2 } )$ is given by

$$
K ( z _ { 1 } , z _ { 2 } ) = \frac { 1 + z _ { 1 } / 3 } { 1 - 5 z _ { 1 } / 1 2 - z _ { 2 } / 4 + z _ { 1 } z _ { 2 } / 6 } .
$$

The maximum of $\left| { \cal K } ( z _ { 1 } , z _ { 2 } ) \right|$ on the set $\mathrm { R e } z _ { \imath } \leq x$ is attained at

$$
\begin{array} { r l } & { z _ { 1 } ^ { 0 } = \left\{ \begin{array} { l l } { x + i \infty } & { \mathrm { f o r } x \leq \xi } \\ { x + \imath x \sqrt { \displaystyle \frac { 4 5 - 4 2 x + 8 x ^ { 2 } } { 9 + 1 8 x - 8 x ^ { 2 } } } } & { \mathrm { f o r } \xi \leq x < 3 / 2 } \end{array} \right. } \\ & { z _ { 2 } ^ { 0 } = \left\{ \begin{array} { l l } { x } & { \mathrm { f o r } x \leq \xi } \\ { x + i \displaystyle \frac { x \sqrt { \displaystyle ( 4 5 - 4 2 x + 8 x ^ { 2 } ) ( 9 + 1 8 x - 8 x ^ { 2 } ) } } { 8 x ^ { 2 } - 6 x - 9 } } & { \mathrm { f o r } \xi \leq x < 3 / 2 } \end{array} \right. } \end{array}
$$

(the value $\xi = ( 9 - 3 \sqrt { 1 7 } ) / 8$ is a root of $9 + 1 8 x - 8 x ^ { 2 } = 0 { \mathrm { : } }$ and it is given by

$$
\varphi _ { k } ( x ) = \left\{ \begin{array} { l l l } { \displaystyle \frac { 4 } { 5 - 2 x } } & { \mathrm { i f } } & { x \leq \xi } \\ { \displaystyle \frac { 3 + 4 x } { \sqrt { ( 3 - 2 x ) ( 3 + 4 x - 2 x ^ { 2 } ) } } } & { \mathrm { i f } } & { \xi \leq x < 3 / 2 . } \end{array} \right.
$$

The function $K ( z _ { 1 } , z _ { 2 } )$ is not bounded on $\mathrm { R e } z _ { \imath } \leq x$ for $x \ge 3 / 2$ . From the proof of Lemma 12.26 we compute $d _ { \mathrm { { i } } }$ and $d _ { 2 }$ ,and obtain

$$
d _ { 1 } = \left\{ \begin{array} { l l } { \displaystyle \frac { 9 } { ( 3 - x ) ( 5 - 2 x ) } } & { \mathrm { f o r } x \le \xi } \\ { \displaystyle \frac { ( 3 + 4 x ) ^ { 2 } } { 4 ( 3 + 4 x - 2 x ^ { 2 } ) } } & { \mathrm { f o r } \xi \le x } \end{array} \right. \qquad d _ { 2 } = \left\{ \begin{array} { l l } { \displaystyle \frac { 2 } { 5 - 2 x } } & { \mathrm { f o r } x \le \xi } \\ { \displaystyle \frac { 3 + 4 x } { 4 ( 3 + 4 x - 2 x ^ { 2 } ) } } & { \mathrm { f o r } \xi \le x . } \end{array} \right.
$$

With these values one checks straight-forwardly that the matrix $W$ of Eq.(12.45c) is semi-definite positive,so that $\varphi _ { B } ( x ) = \varphi _ { \bar { \Lambda } ^ { \prime } } ( x )$ ； see also Burrage & Butcher (1980). Actually, the matrix $W$ is non-singular for $x < \xi$ ,and of rank one for $\xi \le x < 3 / 2$

A comparison with Eq.(11.15) shows that we do not obtain the same estimate as for linear autonomous problems.

The above algorithm can easily be applied to other two-stage methods. We thus obtain for the two-stage Gauss method

$$
\mathrm { i f } \ - \infty < x \leq 0
$$

$$
\varphi _ { B } ( x ) = \left\{ \begin{array} { l l } { 1 } \\ { \displaystyle \frac { 2 x + \sqrt { 9 + 3 x ^ { 2 } } } { 3 - x } } \end{array} \right.
$$

and for the two-stage Lobatto IIIC method

$$
\varphi _ { B } ( x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { 1 } { 1 - x + x ^ { 2 } } \quad } & { \mathrm { i f } \ - \infty < x \leq 0 } \\ { \displaystyle \frac { 1 } { 1 - x } \quad } & { \mathrm { i f } \ 0 \leq x < 1 . } \end{array} \right.
$$

For methods with more than two stages, explicit formulas are dificult to obtain, and one has to apply numerical methods for the computation of $z _ { \jmath } ^ { 0 }$ (supremum in Eq.(12.47)).

# Exercises

1. Prove, directly from Def.12.2, that the implicit Euler method is $B$ -stable.

2. Let $M$ be a symmetric $s \times s$ -matrix and $\langle \cdot , \cdot \rangle$ the scalar product of $\mathbb { R } ^ { n }$ . Then $M$ is non-negative definite, if and only if

$$
\sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { \iota _ { \jmath } } \langle u _ { \iota } , u _ { \jmath } \rangle \geq 0 \quad \mathrm { f o r ~ a l l } \quad u _ { \iota } \in \mathbb { R } ^ { n } .
$$

Hint. Use $M = Q ^ { T } D Q$ where $D$ is diagonal.

3. Give a simple proof for the $B$ -stability of the Radau IIA methods by extending the ideas of Example 12.3.

Hint. For the quadrature,based on the zeros of (5.2),we have

$$
\int _ { 0 } ^ { 1 } \varphi ( x ) d x = \sum _ { \iota = 1 } ^ { s } b _ { \iota } \varphi ( c _ { \iota } ) + C \varphi ^ { ( 2 s - 1 ) } ( \xi ) , \quad 0 < \xi < 1 .
$$

with $C < 0$ (see e.g. Abramowitz & Stegun (1964,Formula 25.4.31).

4.(Dahlquist & Jeltsch 1987). Prove that Method Iof Table 12.4 is $S$ -reducible with respect to the partition $( \{ 1 \} , \{ 2 , 3 \} )$ . The reduced method II itself is $D J$ - reducible and reduces to Method III.

For the initial value problem $y ^ { \prime } = f ( y )$ ， $y ( 0 ) = 1$ ,where $f ( y ) = y ^ { 2 }$ for $y \geq 0$ and $f ( y ) = 0$ for $y < 0$ ,and for $h \approx 2$ , Methods I and III have unique solutions which are different. Explain this apparent contradiction.

0 0 0 0   
1/2 0 1 -1/2 0 0 0   
1/2 0 1/2 0 1/2 0 1/2 0 0 1 6 -b 1 0 1 Method I Method II Method III

5. Give a counterexample of an irreducible $A N$ -stable but not algebraically stable,and hence not $B$ -stable method.

Hint. Start with any algebraically stable method with，say, two stages and modify it as indicated in Table 12.5. Find conditions on the free parameters $d , e , \alpha$ such that the two methods are identical for equations $y ^ { \prime } = \lambda ( x ) y$ . This ensures $A N$ -stability of the second method. Then play with the parameters to destroy algebraic stability.

6. Show that the method of Table 12.1 is $D J$ -reducible, but not $S$ -reducible; show that it is algebraically stable together with the reduced method.

Table 12.5. Construction of $A N$ -stable but not $B$ -stable method

$$
\begin{array} { r } { \underbrace { c _ { 1 } } _ { \begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c } { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & & & & { \Rightarrow } & & & { c _ { 1 } } & {  } & { a _ { 1 1 } } & { a _ { 1 2 } \alpha } & & { a _ { 1 2 } ( 1 - \alpha ) } & & \\ { c _ { 2 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & & & & { c _ { 2 } } & & & { c _ { 2 } } & & { d \alpha } & & { d ( 1 - \alpha ) } & \\ { b _ { 1 } } & { b _ { 2 } } & & & & { \Rightarrow } & & & { c _ { 2 } } & & & { b _ { 2 } \alpha } & & { e ( 1 - \alpha ) } & & \end{array} } } \end{array}
$$

Show that the method of Table 12.2 is $S$ -reducible, but not $D J$ -reducible;   
show that it is not algebraically stable,but that the reduced method is.

7. (Sandberg & Shichman 1968,Vanselow 1979,Hundsdorfer 1985). Prove that Rosenbrock methods are not $B$ -stable in the sense of Definition 11.2.

Hint. Apply the method to the scalar problem $y ^ { \prime } = f ( y )$ ， $y _ { 0 } = 1$ where $f ( y )$ is a non-increasing function satisfying (for a small $\varepsilon$ ）

$$
f ( y ) = { \left\{ \begin{array} { l l } { - y } & { { \mathrm { ~ i f ~ } } \ \left| y - 1 \right| \geq 2 \varepsilon } \\ { - 1 } & { { \mathrm { ~ i f ~ } } \ \left| y - 1 \right| \leq \varepsilon . } \end{array} \right. }
$$

8.(Hairer & Zennaro 1996). For irreducible,algebraically stable Runge-Kutta methods the error growth function satisfies

$$
\varphi _ { B } ( x ) \leq { \frac { { \sqrt { 1 - 2 x \gamma ( 1 - \varrho ^ { 2 } ) } } - 2 x \gamma \varrho } { 1 - 2 x \gamma } }
$$

where $\varrho = \vert R ( \infty ) \vert \ ( R ( z )$ is the stability fuction), $\begin{array} { r } { \gamma = \left( \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } ^ { - 1 } v _ { \jmath } ^ { 2 } \right) ^ { - 1 } } \end{array}$ and $\begin{array} { r } { ( v _ { 1 } , \ldots , v _ { s } ) ^ { T } = \operatorname* { l i m } _ { \varepsilon \to 0 } b ^ { T } ( A + \varepsilon I ) ^ { - 1 } } \end{array}$

Hint. From(12.7) we have $\begin{array} { r } { \| \Delta y _ { 1 } \| ^ { 2 } \leq \| \Delta y _ { 0 } \| ^ { 2 } + 2 x \sum _ { \imath } b _ { \imath } \| \Delta g _ { \imath } \| ^ { 2 } } \end{array}$ . Then, compute $\Delta f _ { \imath }$ from (12.5b) (if $A$ is invertible), insert it into (12.5a) and conclude $\begin{array} { r } { \Delta y _ { 1 } = R ( \infty ) \Delta y _ { 0 } + \sum _ { \jmath } ( \sum _ { \imath } b _ { \imath } \omega _ { \imath \jmath } ) \Delta g _ { \jmath } } \end{array}$ ，where $( \omega _ { \imath \jmath } ) = A ^ { - 1 }$ . The Cauchy-Schwarz inequality yields $\begin{array} { r } { \sum _ { \ i } b _ { \ i } \| \Delta g _ { \ i } \| ^ { 2 } \geq \gamma \big ( \| \Delta y _ { 1 } \| - \varrho \| \Delta y _ { 0 } \| \big ) ^ { 2 } } \end{array}$ which, in-serted into the first estimate, gives a second degree inequality for $\Delta y _ { 1 }$

9.Prove that for the 3-stage Gauss method we have for $x \ge 0$

$$
\varphi _ { B } ( x ) \geq ( 1 + x / 2 ) / ( 1 - x / 2 ) .
$$

Hint. Using (12.18), compute $\bar { K } ( Z )$ for $z _ { 1 }  - \infty , z _ { 2 } = x , z _ { 3 }  - \infty$

10. If the matrix $W$ of Eq.(12.45c),with $d _ { 1 } , \ldots , d _ { s }$ given by Lemma 12.26,is either non-singular or of rank $\leq 1$ , then it holds $\varphi _ { B } ( x ) = \varphi _ { K } ( x )$

Hint. Exploit the fact that the expression in Eq.(12.48) with $\varphi = \varphi _ { K } ( x )$ is non-positive for all $z _ { \jmath }$ with $\mathrm { R e } z _ { \jmath } \leq x$ ·

11. Show that for a non-negative definite symmetric matrix $M = ( m _ { \imath \jmath } )$ one has

$$
| m _ { \imath \jmath } | \leq \sqrt { m _ { \imath \imath } m _ { \jmath \jmath } } .
$$

# IV.13 Positive Quadrature Formulas and B-Stable RK-Methods

Bien que le probleme (des quadratures) ait une durée de deux cents ans ä peu pres,bien qu'il était l'objet de nombreuses recherches de plusieurs géometres: Newton, Cotes, Gauss, Jacobi, Hermite,Tchebychef, Christoffel, Heine,Radeau [sic],A.Markov, T. Stitjes [sic], C. Possé, C. Andréev, N. Sonin et d'autres, il ne peut étre considéré, cependant, comme suffisamment épuisé.

(V. Steklov 1917)

We shall give a constructive characterization of all irreducible $B$ -stable Runge-Kutta methods (Theorem 13.15). Because of Theorem 12.16 we first have to study quadrature formulas with positive weights.

# Quadrature Formulas and Related Continued Fractions

Steklov (1916) proved that a family of interpolatory quadrature formulas converges for all Riemann integrable functions,if all weights of the formulas are positive ("Il faut remarquer cependant que de tels théoremes généraux ne peuvent avoir aucune valeur pratique ..."). This theorem, rediscovered around 1922 by Fejér, initiated an extensive search for quadrature formulas with positive weights. Fejer (1933, “weiter habe ich noch auf sehr kurzem Wege das folgende Resultat erhalten ...") found the result:

“if $P _ { s } ( z )$ are the Legendre polynomials normalized as in(13.4) and $c _ { 1 } , \ldots , c _ { s }$ are the zeros of $M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z )$ with $\alpha _ { 2 } \leq 0$ , then the weights $b _ { i }$ are all positive".

The theory of $B$ -stable methods renewed the interest in positive quadrature formulas and Burrage (1978) obtained the sharp bound

$$
\alpha _ { 2 } < \frac { ( s - 1 ) ^ { 2 } } { 4 ( 2 s - 1 ) ( 2 s - 3 ) }
$$

for the positivity of the $b _ { \imath }$ in the above case. This is the same as condition (5.51) in a different normalization. A short proof of this result (see “Lemma $1 8 ^ { \circ }$ of Norsett & Wanner 1981） then led to a complete characterization of positive quadrature formulas by Sottas & Wanner (1982). An independent proof of an equivalent result was found by Peherstorfer (1981). In what follows,we give a new approach using continued fractions.

Consider a quadrature formula

$$
\sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f ( c _ { \jmath } ) \approx \int _ { 0 } ^ { 1 } f ( x ) d x
$$

with distinct nodes $c _ { \imath }$ and non-zero weights $b _ { \imath }$ . The main idea is to consider the rational function

$$
Q ( z ) = \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \frac { 1 } { z - c _ { \jmath } } = \frac { N ( z ) } { M ( z ) }
$$

where, as usual, $M ( z ) = ( z - c _ { 1 } ) \cdot . . . \cdot ( z - c _ { s } )$ . We first express the order of the quadrature formula in terms of the function $Q ( z )$

Lemma 13.1. A quadrature formula is of order $p$ if and only if $Q ( z )$ ， defined by (13.2), satisfies

$$
Q ( z ) = - \log \left( 1 - \frac { 1 } { z } \right) + \mathcal { O } \left( \frac { 1 } { z ^ { p + 1 } } \right) \qquad f o r \quad z \to \infty .
$$

Proof. Inserting the geometric series for $( 1 - c _ { \jmath } / z ) ^ { - 1 }$ into (13.2) we obtain

$$
Q ( z ) = \sum _ { k \geq 1 } \Big ( \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { k - 1 } \Big ) \frac { 1 } { z ^ { k } } .
$$

Therefore (13.3) is equivalent to

$$
\sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { k - 1 } = \frac 1 k \qquad \mathrm { f o r } \quad k = 1 , \dots , p .
$$

We now study the case of the Gaussian quadrature formulas, where the function (13.2) will be denoted by $Q _ { s } ^ { G } ( z ) = N _ { s } ^ { G } ( z ) / M _ { s } ^ { G } ( z )$ ; here the $c _ { \imath }$ are the zeros of the $s$ -degree shifted Legendre polynomial

$$
P _ { s } ( z ) = \frac { s ! } { ( 2 s ) ! } \frac { d ^ { s } } { d z ^ { s } } \big ( z ^ { s } ( z - 1 ) ^ { s } \big ) ,
$$

which is normalized so that the coefficient of $z ^ { s }$ is 1．The polynomials (13.4) satisfy the recurrence relation (see Eq.(5.53) or Abramowitz & Stegun, p. 782)

$$
P _ { s + 1 } ( z ) = \Big ( z - \frac { 1 } { 2 } \Big ) P _ { s } ( z ) - \tau _ { s } P _ { s - 1 } ( z ) , \qquad \tau _ { s } = \frac { s ^ { 2 } } { 4 ( 4 s ^ { 2 } - 1 ) }
$$

and $P _ { 0 } ( z ) = 1 , P _ { - 1 } ( z ) = 0$ . Since this quadrature formula is of optimal order $2 s$ ， it follows from (13.3) that

$$
N _ { s } ^ { G } ( z ) = - M _ { s } ^ { G } ( z ) \log \left( 1 - \frac { 1 } { z } \right) + \mathcal { O } \left( \frac { 1 } { z ^ { s + 1 } } \right) .
$$

We now insert $M _ { s } ^ { G } ( z ) = P _ { s } ( z )$ (see (13.2)) into (13.5) and multiply by $\log ( 1 -$ $1 / z )$ (which is $\mathcal { O } ( 1 / z )$ for $z \to \infty$ ). A comparison with (13.6) shows that the polynomials $N _ { s } ^ { G } ( z )$ must also satisfy the recurrence formula (13.5) (with $N _ { 0 } ^ { G } ( z ) = 0$ ， $N _ { 1 } ^ { G } ( z ) = 1 )$ .It thus follows from elementary properties of continued fractions (Exercise 1 or Perron (1913), page 4) that

$$
Q _ { s } ^ { G } ( z ) = \frac { 1 } { | z - \frac { 1 } { 2 } } - \frac { \tau _ { 1 } } { | z - \frac { 1 } { 2 }  } - \ldots - \frac { \tau _ { s - 1 } } { | { z - \frac { 1 } { 2 } }  } .
$$

For an arbitrary quadrature formula we have

Lemma 13.2. An irreducible rational function $Q ( z ) = N ( z ) / M ( z )$ (with deg M = $s$ ，deg $N = s - 1$ ) satisfies (13.3) with $p \geq 2 ( s - k )$ ， if and only if

$$
Q ( z ) = { \frac { 1 } { | z - { \frac { 1 } { 2 } } - { \frac { \tau _ { 1 } } { | z - { \frac { 1 } { 2 } }  } } - \ldots - { \frac { \tau _ { s - k - 1 } } { | z - { \frac { 1 } { 2 } } - { \frac { g ( z ) } { | f ( z )  } }  } } } } - { \frac { g ( z ) } { | f ( z )  } }
$$

with deg $f = k$ and deg $g \le k - 1$

Proof. From Lemma 13.1 we know that $Q ( z ) = Q _ { s } ^ { G } ( z ) + \mathcal { O } \bigl ( 1 / z ^ { 2 ( s - k ) + 1 } \bigr )$ . Therefore the first $2 ( s - k )$ coefficients in the continued fraction expansions for $Q ( z )$ and $Q _ { s } ^ { G } ( z )$ must be the same. □

Endlich sei noch die folgende Formel wegen ihrer häufigen Anwendungen ausdricklich hervorgehoben:

(O. Perron 1913, page 5)

Lemma 13.3. The functions $M ( z )$ and $N ( z )$ of Lemma 13.2 are related to $f ( z )$ and $g ( z )$ of(13.7') as follows:

$$
\begin{array} { r } { M ( z ) = P _ { s - k } ( z ) f ( z ) - P _ { s - k - 1 } ( z ) g ( z ) , } \\ { N ( z ) = N _ { s - k } ^ { G } ( z ) f ( z ) - N _ { s - k - 1 } ^ { G } ( z ) g ( z ) . } \end{array}
$$

Proof. This follows from the recursion (13.30)and Exercise 1 below,if we put there $b _ { 0 } = 0$ ， $b _ { 1 } = \ldots = b _ { s - k } = z - 1 / 2 , b _ { s - k + 1 } = f ( z )$ and $a _ { 1 } = 1$ ， $a _ { _ { 2 } } = - \tau _ { _ { 2 ^ { - 1 } } } ( j =$ $2 , \ldots , s - k )$ ， $a _ { s - k + 1 } = - g ( z )$ □

Solving the linear system (13.8) for $f ( z )$ and $g ( z )$ gives, with the use of Exercise 2,

$$
\begin{array} { r l } & { f ( z ) \cdot \tau _ { 1 } \cdot \cdot \cdot \tau _ { s - k - 1 } = N ( z ) P _ { s - k - 1 } ( z ) - M ( z ) N _ { s - k - 1 } ^ { G } ( z ) } \\ & { g ( z ) \cdot \tau _ { 1 } \cdot \cdot \cdot \tau _ { s - k - 1 } = N ( z ) P _ { s - k } ( z ) - M ( z ) N _ { s - k } ^ { G } ( z ) . } \end{array}
$$

# Number of Positive Weights

For a given rational function (13.2), the weights are determined by

$$
b _ { \imath } = \frac { N ( c _ { \imath } ) } { M ^ { \prime } ( c _ { \imath } ) } .
$$

But we want our theory to work also for confluent nodes for which $M ^ { \prime } ( c _ { \imath } ) = 0$ ·

Therefore we suppose that $c _ { 1 } , \ldots , c _ { m } \ ( m \leq s )$ are the real and distinct zeros of $M ( z )$ of multiplicities $l _ { 1 } , \ldots , l _ { m }$ . Then we let

$$
b _ { \imath } = \frac { N ( c _ { \imath } ) } { M ^ { ( l _ { \imath } ) } ( c _ { \imath } ) } \qquad i = 1 , \ldots , m .
$$

For $l _ { \ i } = 1$ this is just (13.1O); otherwise we are considering the weights for the highest derivative of a Hermitian quadrature formula (see Exercise 3).

The main idea (following Sottas & Wanner 1982) is now to consider the path $\gamma ( t ) = ( f ( t ) , g ( t ) )$ in the plane $\mathbb { R } ^ { 2 }$ ,where $f$ and $g$ are the polynomials of (13.7'). For $t \to \pm \infty$ this path tends to infinity with horizontal limiting directions,since the degree of $f$ is higher than that of $g$ . Equation (13.8) tells us that for an irreducible $Q ( z )$ this path does not pass through the origin.

Definition 13.4. The rotation number $r$ of $\gamma$ is the integer for which $r \pi$ is the total angle of rotation around the origin for the path $\gamma ( t ) \left( - \infty < t < \infty \right)$ measured in the negative (clockwise) sense. Counter-clockwise rotations are negative.

An algebraic definition of $r$ is possible as

$$
r = \sum _ { \iota } \mathrm { s i g n } \left( f ^ { ( { \iota } _ { \iota } ) } ( t _ { \iota } ) g ( t _ { \iota } ) \right) ,
$$

where the summation is over allreal zeros of $f ( t )$ with odd multiplicity $l _ { \ i }$

Theorem 13.5 (Sottas & Wanner 1982). Let $Q ( z ) = N ( z ) / M ( z )$ be an irreducible rational function as in Lemma 13.2. Suppose that $c _ { 1 } , \ldots , c _ { m }$ are the (distinct) real zeros of $M ( z )$ with odd multiplicity and denote by $n _ { + }$ (respectively $n _ { - }$ ）the number of positive (respectively negative) $b _ { \imath }$ . Further, let $r$ be the rotation number of $\gamma = ( f , g )$ (Definition 13.4). Then

$$
n _ { + } - n _ { - } = s - k + r .
$$

Proof. The proof is by counting the number of crossings of the vectors $\gamma ( t ) =$ $( f ( t ) , g ( t ) )$ and $\beta ( t ) = ( P _ { s - k - 1 } ( t ) , P _ { s - k } ( t ) )$ , like the crossings of hands on a Swiss cuckoo clock.

From(13.9) we see that when $t$ equals a zero $c _ { \imath }$ of $M$ ， these two vectors are parallel in the same sense $( N ( c _ { \imath } ) > 0 )$ or in the opposite sense $( N ( c _ { \imath } ) < 0 )$ · From (13.8) we observe that $M ( t )$ is just the exterior product $\gamma ( t ) \times \beta ( t )$ .By elementary geometry,and taking into account Formula (13.10')，we see that at every zero $c _ { \imath }$ with odd multiplicity we have

i） $b _ { \imath } > 0$ , if the crossing of $\gamma ( t )$ with $\beta ( t )$ is clockwise;   
ii) $b _ { \imath } < 0$ , if this crossing is counter-clockwise.   
Zeros of $M ( t )$ with even multiplicity don't give rise to crossings.

Since the zeros of $P _ { s - k }$ and $P _ { s - k - 1 }$ interlace (see.g. Theorem 3.3.2 of Szego 1939),the vector $\beta ( t )$ turns counter-clockwise with a total angle of $- ( s -$ $k \pi$ (see Fig.13.1). The vector $\gamma ( t )$ turns with a total angle rπr measured clockwise (Definition 13.4). Since the limiting directions of $\gamma ( t )$ and $\beta ( t )$ are different (horizontal for $\gamma ( t )$ and vertical for $\boldsymbol { \beta } ( t )$ ）， $\gamma ( t )$ must cross $\beta ( t )$ ，as $t$ increases from $- \infty$ to $+ \infty$ ，exactly $s - k + r$ times more often clockwise than counterclockwise. This gives Formula (13.11). □

![](../chunks/Solving ordinary differential equations (Hairer, E. (Ernst), Nørsett etc.) (z-library.sk,_part_0004_pages_0211-0280/auto/images/edfa93f029e03908a8c081103eafcbce4d78afd88eed38ad2539f4fbf3c9ffc9.jpg)  
Fig. 13.1. The path $( P _ { s - k - 1 } ( t ) , P _ { s - k } ( t ) )$ for $s - k = 7$

Corollary 13.6. Under the assumptions of Theorem 13.5, all zeros of $M ( z )$ are real and simple, and the $b _ { \imath }$ are positive if and only if

$$
r = k .
$$

Proof. $r = k$ means by (13.11) that $n _ { + } - n _ { -- } = s$ . Because of $n \geq 0$ and $\eta _ { i } \leq s ,$ this is equivalent to $n _ { + } = s$ and $n _ { \dots } = 0$ ， □

# Characterization of Positive Quadrature Formulas

The following theorem gives a constructive characterization of all quadrature formulas with positive weights.

# Theorem 13.7. Let

$$
\sigma _ { 1 } < \varrho _ { 1 } < \sigma _ { 2 } < \varrho _ { 2 } < . . . < \varrho _ { k - 1 } < \sigma _ { k }
$$

be arbitrary real numbers and $C$ a positive constant. Then, putting

$$
f ( z ) = ( z - \sigma _ { 1 } ) \ldots ( z - \sigma _ { k } ) , \quad g ( z ) = C ( z - \varrho _ { 1 } ) \ldots ( z - \varrho _ { k - 1 } ) ,
$$

computing $M ( z ) , \ N ( z )$ from (13.8), taking $c _ { 1 } , \ldots , c _ { s }$ as the zeros of $M ( z )$ and $b _ { i } f r o m ( I 3 . I O ) ,$ one obtains all quadrature formulas with positive weights of order $p \geq 2 ( s - k )$ .If $C = \tau _ { s - k }$ the order is $p \ge 2 ( s - k ) + 1$

Proof. The functions $f ( z )$ and $g ( z )$ are irreducible, so that also the fraction $N ( z ) / M ( z )$ is irreducible by (13.9). The statement now follows from Corollary 13.6,since the polynomials (13.12）are all possible polynomials for which $r \approx k$ . The stated order properties follow from Lemma 13.2. □

Example 13.8. Let $c _ { 1 } , \ldots , c _ { s }$ be the zeros of

$$
M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z ) .
$$

In order to study when the corresponding quadrature formula has positive weights, we use (13.5) to write (13.13) as

$$
M ( z ) = P _ { s - 1 } ( z ) \Big ( z - \frac { 1 } { 2 } + \alpha _ { 1 } \Big ) - P _ { s - 2 } ( z ) \big ( \tau _ { s - 1 } - \alpha _ { 2 } \big ) .
$$

Consequently $f ( z ) = z - 1 / 2 + \alpha _ { 1 } , g ( z ) = \tau _ { s - 1 } - \alpha _ { 2 }$ and Theorem 13.7 implies that the zeros of $M ( z )$ arerealandthe weightspositive,ifandoyif $\alpha _ { 2 } < \tau _ { s - 1 }$ ， hence (13.1) is proved.

For $k > 1$ the rotation number $r$ of $( f ( t ) , g ( t ) )$ can be computed with Sturm's algorithm (Lemma 13.3 of Sect. I.13). Consider, for example,

$$
\begin{array} { r l r } {  { M ( z ) = P _ { s } ( z ) + \alpha _ { 1 } P _ { s - 1 } ( z ) + \alpha _ { 2 } P _ { s - 2 } ( z ) + \alpha _ { 3 } P _ { s - 3 } ( z ) } } \\ & { } & { = P _ { s - 2 } ( z ) \big [ ( z - \frac { 1 } { 2 } ) ( z - \frac { 1 } { 2 } + \alpha _ { 1 } ) + \alpha _ { 2 } - \tau _ { s - 1 } \big ] \qquad } \\ & { } & { \qquad - P _ { s - 3 } ( z ) \big [ \tau _ { s - 2 } ( z - \frac { 1 } { 2 } + \alpha _ { 1 } ) - \alpha _ { 3 } \big ] . } \end{array}
$$

Application of Lemma I.13.3 to the polynomials $f ( z ) = ( z - { \textstyle \frac { 1 } { 2 } } ) ( z - { \textstyle \frac { 1 } { 2 } } + \alpha _ { 1 } ) +$ $\alpha _ { 2 } - \tau _ { s - 1 }$ and $g ( z ) = \tau _ { s - 2 } ( z - \textstyle { \frac { 1 } { 2 } } + \alpha _ { 1 } ) - \alpha _ { 3 }$ shows that the corresponding quadrature formula has positive weights iff

$$
\frac { \alpha _ { 3 } } { \tau _ { s - 2 } } \Big ( \alpha _ { 1 } - \frac { \alpha _ { 3 } } { \tau _ { s - 2 } } \Big ) - \alpha _ { 2 } + \tau _ { s - 1 } > 0 ,
$$

a result first found by Burrage (1978).

# Necessary Conditions for Algebraic Stability

We now turn our attention to algebraic stability. We again use the notation $B ( p )$ ， $C ( \eta ) , D ( \xi )$ of Sect. IV.5.

Lemma 13.9 (Burrage 1982). Consider Runge-Kutta methods, which satisfy $B ( 2 )$ and the second condition for algebraic stability (i.e. M non-negative). Then,

$a$ ） $C ( k )$ implies $B ( 2 k - 1 )$ ； b） $D ( k )$ implies $B ( 2 k - 1 )$

Proof. Instead of considering $M$ ， we work with the transformed matrix $\widehat { M } =$ $V ^ { T } M V$ where $V = ( c _ { \imath } ^ { \jmath - 1 } ) _ { \imath , \jmath = 1 } ^ { s }$ 1),J=1 is the Vandermonde matrix. The elements of M are given by

$$
\widehat { m } _ { q r } = \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { r - 1 } + \sum _ { j = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } \sum _ { \imath = 1 } ^ { s } a _ { \jmath \imath } c _ { \imath } ^ { q - 1 } - \sum _ { \imath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q - 1 } \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } .
$$

We further introduce

$$
g _ { r } = r \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { r - 1 } - 1
$$

so that $B ( \nu )$ is equivalent to $g _ { r } = 0 \ ( r = 1 , \ldots , \nu )$ . Then $C ( k )$ simplifies (13.15) to

$$
\widehat { m } _ { q r } = \frac { 1 } { q \cdot r } \left( g _ { q + r } + 1 - ( g _ { q } + 1 ) ( g _ { r } + 1 ) \right) \qquad q \leq k , r \leq k .
$$

Similarly, $D ( k )$ implies

$$
\widehat { m } _ { q r } = - \frac { 1 } { q \cdot r } \left( g _ { q + r } + g _ { q } \cdot g _ { r } \right) \qquad q \leq k , r \leq k .
$$

We now start with the hypothesis $B ( 2 )$ ,i.e., $B ( 2 l )$ for ${ \mathit { l } } = 1$ .This means that $g _ { 1 } = . . . = g _ { 2 l } = 0$ , so that, in both cases, $\widehat { m } _ { l l } = 0$ . But if for a non-negative definite matrix a diagonal element is zero, the whole corresponding column must also be zero (see Exercise 11 of Sect.IV.12). This leads to $g _ { l + q } = 0$ for $q = 1 , \ldots , k ;$ so we have $B ( k + l )$ . We then repeat the argument inductively until we arrive at $B ( 2 k - 1 )$ □

Since $s$ -stage collocation methods satisfy $B ( s )$ and $C ( s )$ (see Theorem 7.8 of Chapter II) we have

Corollary 13.10 (Burrage 1978). An $s$ -stage algebraically stable collocation method must be of order at least $2 s - 1$ . □

Because symmetric methods have even order this gives:

Corollary 13.11 (Ascher & Bader 1986). $A$ symmetric algebraically stable collocation scheme has to be at Gaussian points. □

The next result states the necessity of the simplifying assumption $C ( k )$ . Ob-serve that by Theorem 12.16 the weights $b _ { \imath }$ of $D J$ -irreducible,algebraically stable methods have to be positive.

Lemma 13.12. If a Runge-Kutta method of order $p \geq 2 k + 1$ satisfies $b _ { i } > 0$ for $i = 1 , \dots , s$ , then the condition $C ( k )$ holds.

Proof (Dahlquist & Jeltsch (1979) atribute this idea to Butcher). The order conditions (see Sect. II.2)

$$
\sum _ { \ i = 1 } ^ { s } b _ { i } c _ { \ i } ^ { 2 q } = \frac { 1 } { 2 q + 1 }
$$

$$
\begin{array} { l } { { \displaystyle \sum _ { i , \jmath = 1 } ^ { s } b _ { \imath } c _ { \imath } ^ { q } a _ { \imath \jmath } c _ { \jmath } ^ { q - 1 } = \frac { 1 } { ( 2 q + 1 ) q } } } \\ { { \displaystyle \sum _ { \imath , j , m = 1 } ^ { s } b _ { \imath } a _ { i \jmath } c _ { \jmath } ^ { q - 1 } a _ { \imath m } c _ { m } ^ { q - 1 } = \frac { 1 } { ( 2 q + 1 ) q ^ { 2 } } } } \end{array}
$$

imply that

$$
\sum _ { \ i = 1 } ^ { s } b _ { \ i } \bigg ( \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { q - 1 } - \frac { c _ { \imath } ^ { q } } { q } \bigg ) ^ { 2 } = 0
$$

for $2 q + 1 \leq p$ . Since the $b _ { \imath }$ are positive,the individual terms of this sum must be zero for $q \leq k$ . □

A simple consequence of this lemma are the following order barriers for diagonally implicit DIRK $\mathbf { \rho } ( a _ { \imath \jmath } = 0$ for $i < j \}$ ）and singly diagonally implicit SDIRK $( a _ { \iota _ { \mathcal { I } } } = 0$ for $i < j$ and $a _ { \scriptscriptstyle 2 2 } = \gamma$ for all $i$ ） methods.

# Theorem 13.13 (Hairer 1980).

$a$ ）A DIRK method with all $b _ { \imath }$ positive has order at most $\boldsymbol { \delta }$ $b$ ）An SDIRK method with all $b _ { \imath }$ positive has order at most 4; $c$ ） An algebraically stable DIRK method has order at most 4.

Proof. a) Suppose the order is greater than 6 and let $i$ be the smallest index such that $c _ { \imath } \neq 0$ . Then by Lemma 13.12

$$
a _ { { } _ { 1 2 } } c _ { { } _ { 2 } } = { \frac { c _ { \imath } ^ { 2 } } { 2 } } , \qquad a _ { { } _ { 1 2 } } c _ { { } _ { \imath } } ^ { 2 } = { \frac { c _ { \imath } ^ { 3 } } { 3 } } ,
$$

contradicting $c _ { \imath } \neq 0$ ·

b) As above,we arrive for order greater than 4 at

$$
a _ { \scriptscriptstyle { \imath \imath } } c _ { \scriptscriptstyle { \imath } } = \frac { c _ { \scriptscriptstyle { \imath } } ^ { 2 } } { 2 } \quad \mathrm { o r } \quad a _ { \scriptscriptstyle { \imath \imath } } = \frac { c _ { \scriptscriptstyle { \imath } } } { 2 } ( \ne 0 ) .
$$

Since for SDIRK methods we have $a _ { \scriptscriptstyle { \imath 2 } } = a _ { \scriptscriptstyle { 1 1 } }$ , this leads to $c _ { 1 } = a _ { 1 1 } \neq 0$ , hence i= 1. Now a11 = c1/2 contradicts α = C1:

c) It is sufficient to consider $D J$ -ireducible methods, since the reduction process (see Table 12.3) leaves the class of DIRK methods invariant. From Theorem 12.16 and Lemma 13.12 we obtain that algebraic stability and order greater than 4 imply

$$
a _ { 1 1 } = c _ { 1 } , \qquad a _ { 1 1 } c _ { 1 } = \frac { c _ { 1 } ^ { 2 } } { 2 } ,
$$

and hence $a _ { 1 1 } = 0$ . Inserted into $m _ { 1 1 }$ this yields $m _ { 1 1 } = - b _ { 1 } ^ { 2 } < 0$ , contradicting the non-negativity of the matrix $M$ . □

Similarly to Lemma 13.12 we have the following result for the second type of simplifying assumptions.

Lemma 13.14. Ifa Runge-Kutta method of order $p \ge 2 k + 1$ is algebraically stable and satisfies $b _ { \imath } > 0$ for all $i$ ， then the condition $D ( k )$ holds.

Proof. The main idea is to use the $W$ -transformation of Sect.IV.5 and to consider $W ^ { T } M W$ instead of $M$ (see also the proof of Theorem 12.8). By Theorem 5.14 there exists a matrix $W$ satisfying $T ( k , k )$ (see Definition 5.10).With the help of Lemma 13.12 and Theorem 5.11a we obtain that the first $k$ diagonal elements of

$$
\begin{array} { r } { W ^ { T } M W = ( W ^ { T } B W ) X + X ^ { T } ( W ^ { T } B W ) ^ { T } - e _ { \mathbf { l } } e _ { \mathbf { l } } ^ { T } } \end{array}
$$

are zero. Since $M$ and hence also $W ^ { T } M W$ is non-negative definite, the first $k$ columns and rows of $W ^ { T } M W$ have to vanish. Thus the matrix $( W ^ { T } B W ) X$ must be skew-symmetric in these regions (with exception of the first element). Because of $C ( k )$ the first $k$ columns and rows of $( W ^ { T } B W ) X$ and $X$ are identical. Thus the result follows from Theorem 5.11. □

# Characterization of Algebraically Stable Methods

Theorem 12.16, Lemma 13.12 and Lemma 13.14 imply that $D J$ -irreducible and algebraically stable RK-methods of order $p \geq 2 k + 1$ satisfy $b _ { \imath } > 0$ for all $i$ , and the simplifying assumptions $C ( k )$ and $D ( k )$ . These properties allow the following constructive characterization of all irreducible $B$ -stable RK-methods.

Theorem 13.15 (Hairer & Wanner 1981). Consider a pth order quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right) _ { \imath = 1 } ^ { s }$ with positive weights and let W satisfy Property $T ( k , k )$ of Definition $5 . 1 0$ with $k = [ ( p - 1 ) / 2 ]$ . Then all $p$ th order algebraically stable Runge-Kuta methods corresponding to this quadrature formula are given by

$$
A = W X W ^ { - 1 }
$$

where

$$
( W ^ { T } B W ) X = \frac { 1 } { 2 } e _ { 1 } e _ { 1 } ^ { T } ~ + ~ \left( \begin{array} { l l l l } { { 0 } } & { { - \xi _ { 1 } } } & { { } } & { { } } \\ { { \xi _ { 1 } } } & { { \ddots } } & { { \ddots } } & { { } } \\ { { } } & { { \ddots } } & { { 0 } } & { { - \xi _ { k } } } \\ { { } } & { { } } & { { \xi _ { k } \left| ~ \overline { { { Q } } } ~ \right.}  } \end{array} \right)
$$

and $Q$ is an arbitrary matrix of dimension $s - k$ for which $Q + Q ^ { T }$ is non-negative definite. For $p$ even we have to require that $q _ { 1 1 } = 0$ .

Proof. Algebraic stability and the positivity of the weights $b _ { \imath }$ imply $C ( k )$ and $D ( k )$ with $k = [ ( p - 1 ) / 2 ]$ . The matrix $A$ of such a method can be written as (13.17) with $X$ given by (13.18). This follows from Theorem 5.11 and the fact that multiplication with $W ^ { T } B W$ does not change the first $k$ columns and rows of $X$ .This method is algebraically stable iff $M$ (or $W ^ { T } M W )$ is non-negative definite.By (13.16) this means that $Q + Q ^ { T }$ is non-negative definite.

Conversely,any Runge-Kutta method given by (13.17), (13.18) with $Q + Q ^ { T }$ non-negative definite is algebraically stable and satisfies $C ( k )$ and $D ( k )$ . There-fore it follows from Theorem 5.1 in the case of odd $p { = } 2 k + 1$ that the Runge-Kutta method is of order $p$

If $p$ is even, say $p { = } 2 k { + } 2$ , the situation is slightly more complicated. Because of

$$
q _ { 1 1 } = \sum _ { i , j = 1 } ^ { s } b _ { \imath } P _ { k } ( c _ { \imath } ) a _ { i j } P _ { k } ( c _ { j } )
$$

it follows from $B ( 2 k + 2 ) , C ( k ) , D ( k )$ that the order condition (13.19) below (with $\xi = \eta = k \AA$ ） is equivalent to $q _ { 1 1 } = 0$ . The stated order $p$ of the RK-method now follows from Lemma 13.16. □

In the above proof we used the following modification of Theorem 5.1.

Lemma 13.16. If the coefficients $b _ { \imath } , c _ { \imath } , a _ { i j }$ of an RK-method satisfy

$$
\sum _ { \ i , \ i = 1 } ^ { s } b _ { \ i } c _ { \ i } ^ { \xi } a _ { i \ i } c _ { \ j } ^ { \eta } = \frac { 1 } { ( \eta + \xi + 2 ) ( \eta + 1 ) }
$$

and $B ( p )$ ，C(n）， $D ( \xi )$ with $p \leq \eta + \xi + 2$ and $p \leq 2 \eta + 2$ ,then the method is oforder $p$

Proof. The reduction process with the help of $C ( \eta )$ and $D ( \xi )$ as described in Sect.II.7 (Volume I) reduces all trees to the bushy trees covered by $B ( p )$ .The only exception is the tree corresponding to order condition (13.19). □

Example 13.17 (Three-stage $B$ -stable SIRK methods). Choose a third order quadrature formula with positive weights and let $W$ satisfy $W ^ { T } B W = I$ .Then (13.18) becomes

$$
X = \left( \begin{array} { c c c } { { \frac { 1 } { 2 } } } & { { - \xi _ { 1 } } } & { { 0 } } \\ { { \xi _ { 1 } } } & { { a } } & { { b } } \\ { { 0 } } & { { c } } & { { d } } \end{array} \right) , \qquad \xi _ { 1 } = \frac { 1 } { 2 \sqrt { 3 } } .
$$

The method is $B$ -stable if $X ^ { T } + X - e _ { 1 } e _ { 1 } ^ { T }$ is non-negative, i.e. if

$$
a \geq 0 , \quad d \geq 0 , \quad 4 a d \geq ( c + b ) ^ { 2 } .
$$

If we want this method to be singly-implicit, we must have for the characteristic polynomial of $A$

$$
\chi _ { A } ( z ) = ( 1 - \gamma z ) ^ { 3 } = 1 - 3 \gamma z + 3 \gamma ^ { 2 } z ^ { 2 } - \gamma ^ { 3 } z ^ { 3 } .
$$

This means that (see (13.17))

$$
\begin{array} { r } { \displaystyle \frac { 1 } { 2 } + a + d = 3 \gamma } \\ { \displaystyle \frac { a } { 2 } + \frac { 1 } { 1 2 } + \frac { d } { 2 } + a d - c b = 3 \gamma ^ { 2 } } \\ { \displaystyle \frac { a d - c b } { 2 } + \frac { 1 } { 1 2 } d = \gamma ^ { 3 } . } \end{array}
$$

Some elementary algebra shows that these equations can be solved and the inequalities (13.20) satisfied if $1 / 3 \le \gamma \le 1 . 0 6 8 5 7 9 0 2$ , i.e., exactly if the corresponding rational approximation is $A$ -stable(cf. Table 6.3; see also Hairer & Wanner(1981), where the analogous case with $s = p = 5$ is treated).

# The “Equivalence" of $\pmb { A }$ - and $B$ -Stability

Many $A$ -stable RK-methods are not $B$ -stable (e.g., the trapezoidal rule, the Lobatto IIIA and Lobatto IIIB methods; see Theorem 12.12). On the other hand there is the famous result of Dahlquist (1978),saying that every $A$ -stable one-legmethod is $B$ -stable, which we shall prove in Sect.V.6. We have further seen in Example 13.17 that for a certain class of $A$ -stable methods there is always a $B$ - stable method with the same stability function. The general truth of this result was conjectured for many years and is as follows:

Theorem 13.18 (Hairer & Turke 1984, Hairer 1986).Let $R ( z ) = P ( z ) / Q ( z )$ $( P ( 0 ) = Q ( 0 ) = 1$ ， $\deg P \leq s$ ， $\deg Q = s$ ) be an irreducible, $A$ -stable function satisfying $R ( z ) - e ^ { z } = \mathcal { O } ( z ^ { p + 1 } )$ for some $p \geq 1$ . Then there exists an s-stage $B$ -stable Runge-Kutta method of order $p$ with $R ( z )$ as stability function.

Proof. Since $R ( z )$ is an approximation to $e ^ { z }$ of order $p$ , it can be written in the form

$$
R ( z ) = \frac { 1 + \frac { 1 } { 2 } \Psi ( z ) } { 1 - \frac { 1 } { 2 } \Psi ( z ) } , \qquad \Psi ( z ) = \frac { z \Big | } { | 1 } + \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } | } { 1 } + . . . + \frac { \xi _ { k - 1 } ^ { 2 } z ^ { 2 } | } { 1 } + \xi _ { k } ^ { 2 } z \Psi _ { k } ( z )
$$

where $k = [ ( p - 1 ) / 2 ]$ ， $\xi _ { \ j } ^ { 2 } = 1 / ( 4 ( 4 j ^ { 2 } - 1 ) )$ and $\Psi _ { k } ( z ) = z g ( z ) / f ( z )$ with $g ( 0 ) =$ $f ( 0 ) = 1$ ，d $\operatorname { s g } f \leq s - k$ ,deg $\cdot g \leq s - k - 1$ (for $p$ even we have in addition $g ^ { \prime } ( 0 ) =$ $f ^ { \prime } ( 0 ) )$ . For the diagonal Padé-approximation $R ^ { G } ( z )$ of order $2 s$ this follows from Theorem 5.18 with $\nu = s - 1$ and $\Psi _ { \nu } = z$ ：

$$
R ^ { G } ( z ) = \frac { 1 + \frac { 1 } { 2 } \Psi ^ { G } ( z ) } { 1 - \frac { 1 } { 2 } \Psi ^ { G } ( z ) } , \qquad \Psi ^ { G } ( z ) = \frac { z \Big | } { | 1 } + \frac { \xi _ { 1 } ^ { 2 } z ^ { 2 } | } { 1 } + \ldots + \frac { \xi _ { s - 1 } ^ { 2 } z ^ { 2 } | } { 1 } .
$$

For an arbitrary $R ( z )$ (satisfying the assumptions of the theorem) this is then a con-sequence of $R ( z ) = R ^ { G } ( z ) + \mathcal { O } ( z ^ { p + 1 } )$ , or equivalently $\Psi ( z ) = \Psi ^ { G } ( z ) + \mathcal { O } ( z ^ { p + 1 } )$

The function $R ( z )$ of (13.21) is $A$ -stable iff(Theorem 5.22)

$$
\operatorname { R e } \Psi _ { k } ( z ) < 0 \quad { \mathrm { f o r } } \quad \operatorname { R e } z < 0 .
$$

Therefore,the function $\chi ( z ) = - \Psi _ { k } ( - 1 / z )$ is positive (c.f. Definition 5.19) and by Lemma 13.19 below there exists an $\left( s - k \right)$ -dimensional matrix $Q$ such that

$$
\chi ( z ) = e _ { 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { 1 } \quad \mathrm { a n d } \quad Q + Q ^ { T }
$$

We now fix an arbitrary quadrature formula of order $p$ with positive weights $b _ { i }$ and (for the sake of simplicity) distinct nodes $c _ { i }$ . We let $W$ be a matrix satisfying $W ^ { T } B W = I$ and Property $T ( k , k )$ with $k = [ ( p - 1 ) / 2 ]$ (c.f. Lemma 5.12),and define the Runge-Kutta coefficients $\left( { a _ { \iota j } } \right)$ by (13.17) and (13.18). This Runge-Kutta method is algebraically stable, because $Q + Q ^ { T }$ is non-negative definite and of order $p$ (observe that $g ^ { \prime } ( 0 ) = f ^ { \prime } ( 0 )$ implies that the upper left element of $Q$ vanishes). Finally, it follows from Theorem 5.18 and $\Psi _ { k } ( z ) = - \chi ( - 1 / z ) =$ $z e _ { 1 } ^ { T } ( I - z Q ) ^ { - 1 } e _ { 1 }$ that its stability function is $R ( z )$ □

It remains to prove the following lemma.

Lemma 13.19. Let $\chi ( z ) = \alpha ( z ) / \beta ( z )$ be an irreducible rational function with real polynomials

$$
\alpha ( z ) = z ^ { n - 1 } + \alpha _ { 1 } z ^ { n - 2 } + \ldots , \quad \beta ( z ) = z ^ { n } + \beta _ { 1 } z ^ { n - 1 } + \ldots .
$$

Then $\chi ( z )$ is a positive function iff there exists an $\mathscr { n }$ -dimensional real matrix $Q$ ， such that

$$
\chi ( z ) = e _ { 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { 1 } \quad a n d \quad Q + Q ^ { T } \quad n o n { \cdot } n e g a t i v e d e f i n i t e .
$$

Proof. a) The sufficiency follows from

$$
\mathrm { R e } \chi ( z ) = q ( z ) ^ { \ast } \{ \mathrm { R e } z \cdot I + { \textstyle { \frac { 1 } { 2 } } } ( Q + Q ^ { T } ) \} q ( z )
$$

with $q ( z ) = ( Q + z I ) ^ { - 1 } e _ { 1 }$ ， since $Q + Q ^ { T }$ is non-negative definite.

b) For the proof of necessity, the hard part, we use Lemma 6.8 of Sect. V.6 below. This lemma is the essential ingredient for Dahlquist's equivalence result and willbe proved in the chapter on multistep methods. It states that the positivity of $\chi ( z )$ is equivalent to the existence of real, symmetric and non-negative definite matrices $A$ and $B$ , such that for arbitrary $z , w \in \mathbb { C }$ $\boldsymbol { \Xi } \mathbb { C } ( \vec { z } = ( z ^ { n - 1 } , \dots , z , 1 ) ^ { T }$ ， $\vec { w } =$ $( w ^ { n - 1 } , \ldots , w , 1 ) ^ { T } )$ ，

$$
\alpha ( z ) \beta ( w ) + \alpha ( w ) \beta ( z ) = ( z + w ) \vec { z } ^ { T } A \vec { w } + \vec { z } ^ { T } B \vec { w } .
$$

The matrix $A$ is positive definite, if $\alpha ( z )$ and $\beta ( z )$ are relatively prime.

Comparing the coeficients of $w ^ { n }$ in (13.25) we get

$$
\alpha ( z ) = \vec { z } ^ { T } A e _ { 1 }
$$

and observe that the first column of $A$ consists of the coefficients of $\alpha ( z )$ . For the Cholesky decomposition of $A$ ， $A = U ^ { T } U$ （ $U$ is an upper triangular matrix） we

thus have $U e _ { \mathbf { 1 } } = e _ { \mathbf { 1 } }$ .We next consider the possible computation of the matrix $Q$ from the relation

$$
( Q + z I ) U \vec { z } = \beta ( z ) \cdot e _ { 1 }
$$

or equivalently

$$
Q U \overrightarrow { z } = \beta ( z ) \cdot e _ { 1 } - z U \overrightarrow { z } .
$$

The right-hand side of(13.28) is a known polynomial of degree $n - 1$ ,since $U e _ { \mathbf { 1 } } =$ $e _ { 1 }$ . Therefore,a comparison of the coefficients in(13.28) yields the matrix $Q U$ and hence also $Q$ . It remains to prove that this matrix $Q$ satisfies (13.24).

Using (13.27), the formula $A e _ { 1 } = U ^ { T } U e _ { 1 } = U ^ { T } e _ { 1 }$ and (13.26) we obtain

$$
e _ { \bf 1 } ^ { T } ( Q + z I ) ^ { - 1 } e _ { \bf 1 } \cdot \beta ( z ) = e _ { \bf 1 } ^ { T } U \vec { z } = e _ { \bf 1 } ^ { T } A ^ { T } \vec { z } = \alpha ( z ) ,
$$

which verifies the first relation of (13.24). Further,from (13.27) and $\alpha ( z ) = e _ { 1 } ^ { T } U \vec { z }$ we get

$$
\vec { z } ^ { T } U ^ { T } ( Q + w I ) U \vec { w } = \alpha ( z ) \beta ( w ) .
$$

Inserting this formula and the analogous one (with $z$ and $w$ exchanged） into (13.25) yields $0 = \vec { z } ^ { T } \big ( B - U ^ { T } \big ( Q + Q ^ { T } \big ) U \big ) \vec { w }$ , so that $B = U ^ { T } ( Q + Q ^ { T } ) U$ .This verifies the second relation of (13.24), since $B$ is symmetric and non-negative definite. □

# Exercises

1. (Perron (1913) attributes this result to Wallis,Arithmetica infinitorum 1655 and Euler 1737). Let the sequences $\{ A _ { k } \}$ and $\{ B _ { k } \}$ be given by

$$
\begin{array} { l l } { { A _ { k } = b _ { k } A _ { k - 1 } + a _ { k } A _ { k - 2 } , \quad } } & { { A _ { - 1 } = 1 , \quad A _ { 0 } = b _ { 0 } } } \\ { { B _ { k } = b _ { k } B _ { k - 1 } + a _ { k } B _ { k - 2 } , \quad } } & { { B _ { - 1 } = 0 , \quad B _ { 0 } = 1 } } \end{array}
$$

then

$$
{ \frac { A _ { n } } { B _ { n } } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| b _ { 1 } \right. } } + \ldots + { \frac { a _ { n } } { \left| b _ { n } \right. } } .
$$

Hint. Let $x = ( x _ { 0 } , x _ { 1 } , \ldots , x _ { n + 1 } ) ^ { T }$ be the solution of $M x = ( 0 , \ldots , 0 , 1 ) ^ { T }$ ， where

$$
M = \left( \begin{array} { c c c c c c c } { { 1 } } & { { - b _ { 0 } } } & { { - a _ { 1 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { 1 } } & { { - b _ { 1 } } } & { { - a _ { 2 } } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \ddots } } & { { \ddots } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { 1 } } & { { - b _ { n - 1 } } } & { { - a _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { 1 } } & { { - b _ { n } } } \\ { { } } & { { } } & { { } } & { { } } & { { } } & { { 1 } } & { { } } \end{array} \right) \ .
$$

One easily finds

$$
{ \frac { x _ { 0 } } { x _ { 1 } } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| x _ { 1 } / x _ { 2 } \right. } } = b _ { 0 } + { \frac { a _ { 1 } } { \left| { b _ { 1 } } \right. } } + { \frac { a _ { 2 } } { \left| x _ { 2 } / x _ { 3 } \right. } } = \dots
$$

so that ${ x _ { 0 } } / { x _ { 1 } }$ is equal to the right hand side of (13.31). The statement now follows from the fact that

$$
\begin{array} { l } { { ( A _ { - 1 } , A _ { 0 } , \ldots , A _ { n } ) M = ( 1 , 0 , \ldots , 0 ) } } \\ { { ( B _ { - 1 } , B _ { 0 } , \ldots , B _ { n } ) M = ( 0 , 1 , 0 , \ldots , 0 ) . } } \end{array}
$$

implying $x _ { 0 } = A _ { n }$ and $x _ { 1 } = B _ { n }$

2. Let $P _ { s } ( z )$ be the Legendre polynomial (13.4) and $N _ { s } ^ { G } ( z )$ defined by the recursion (13.5) with $N _ { 0 } ^ { G } ( z ) = 0$ ， $N _ { 1 } ^ { G } ( z ) = 1$ . Prove that

$$
N _ { s - k } ^ { G } ( z ) P _ { s - k - 1 } ( z ) - N _ { s - k - 1 } ^ { G } ( z ) P _ { s - k } ( z ) = \tau _ { 1 } \cdot \tau _ { 2 } \cdot . . . \cdot \tau _ { s - k - 1 } .
$$

Hint. Use the relation

$$
\left( { \begin{array} { c c } { N _ { m } ^ { G } ( z ) } & { P _ { m } ( z ) } \\ { N _ { m - 1 } ^ { G } ( z ) } & { P _ { m - 1 } ( z ) } \end{array} } \right) = \left( { \begin{array} { c c } { z - \frac { 1 } { 2 } } & { - \tau _ { m - 1 } } \\ { 1 } & { 0 } \end{array} } \right) \left( { \begin{array} { c c } { N _ { m - 1 } ^ { G } ( z ) } & { P _ { m - 1 } ( z ) } \\ { N _ { m - 2 } ^ { G } ( z ) } & { P _ { m - 2 } ( z ) } \end{array} } \right) .
$$

3. Consider the Hermitian quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = b _ { 1 } f ( c _ { 1 } ) + \alpha f ( c _ { 2 } ) + \beta \frac { f ^ { \prime } ( c _ { 2 } ) } { 1 ! } + \gamma \frac { f ^ { \prime \prime } ( c _ { 2 } ) } { 2 ! } .
$$

Replace $f ^ { \prime } ( c _ { 2 } )$ and $f ^ { \prime \prime } ( c _ { 2 } )$ by finite divided differences based on $f ( c _ { 2 } - \varepsilon )$ ， $f ( c _ { 2 } ) , f ( c _ { 2 } + \varepsilon )$ to obtain a quadrature formula

$$
\int _ { 0 } ^ { 1 } f ( x ) d x = \overline { { { b } } } _ { 1 } f ( c _ { 1 } ) + \overline { { { b } } } _ { 2 } f ( c _ { 2 } - \varepsilon ) + \overline { { { b } } } _ { 3 } f ( c _ { 2 } ) + \overline { { { b } } } _ { 4 } f ( c _ { 2 } + \varepsilon ) .
$$

a) Compute $Q ( z )$ for Formula(13.33) and obtain,by letting $\varepsilon \to 0$ , an expres-sion which generalizes (13.2) to Hermitian quadrature formulas.

b) Compute the values of $b _ { 1 }$ and $b _ { 2 }$ $( l _ { 1 } = 1 , l _ { 2 } = 3 )$ of (13.10').

c) Show that $n _ { + } - n _ { - }$ (see Theorem 13.5) is the same for (13.32) and (13.33) with $\varepsilon$ sufficiently small.

Results.

$$
\begin{array} { l l l } { \displaystyle Q ( z ) = \frac { b _ { 1 } } { z - c _ { 1 } } + \frac { \alpha } { z - c _ { 2 } } + \frac { \beta } { ( z - c _ { 2 } ) ^ { 2 } } + \frac { \gamma } { ( z - c _ { 2 } ) ^ { 3 } } } \\ { \displaystyle b _ { 1 } = b _ { 1 } \quad \mathrm { ( s i c ! ) } , \quad b _ { 2 } = \gamma / 3 ! . } \end{array}
$$

4.The rational function $\chi ( z ) = \alpha ( z ) / \beta ( z )$ with $\alpha ( z ) = z + \alpha _ { 1 }$ ， $\beta ( z ) = z ^ { 2 } +$ $\beta _ { 1 } z + \beta _ { 2 }$ is positive, iff $\alpha _ { 1 } \geq 0 , \quad \beta _ { 2 } \geq 0$ $\beta _ { 1 } - \alpha _ { 1 } \ge 0$ (compare (5.48))

a) Find real, symmetric and non-negative definite matrices $A$ and $B$ such that (13.25) holds.   
b） Show that these matrices are,in general, not unique.   
c） As in the proof of Lemma 13.19,compute the matrix $Q$ such that (13.24) holds. Hint. Begin with the construction of $B$ by putting $w = - z$ in (13.25).

# IV.14 Existence and Uniqueness of IRK Solutions

Jusqu'ä présent, nous avons supposé que le schéma admettait une solution. Pour en démontrer l'existence ... (Crouzeix & Raviart 1980)

Since contractivity without feasibility makes little sense .. (M.N. Spijker 1985)

Since the Runge-Kutta methods studied in the foregoing sections are all implicit, we have to ensure that the numerical solutions, for which we have derived so many nice results, also really exist. The existence theory for implicit Runge-Kutta methods, presented in Volume I(Theorem II.7.2), is for the non-stiff case only, where $h L$ is small( $I$ the Lipschitz constant). This is not a reasonable assumption for the stiff case.

We shallstudy the existence of a Runge-Kutta solution,defined implicitly by

$$
\begin{array} { l } { { g _ { i } = y _ { 0 } + \displaystyle h \sum _ { j = 1 } ^ { s } a _ { \iota _ { j } } f \big ( x _ { 0 } + c _ { j } h , g _ { \jmath } \big ) , \quad i = 1 , \dots , s } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } f \big ( x _ { 0 } + c _ { \jmath } h , g _ { \jmath } \big ) , } } \end{array}
$$

for differential equations which satisfy the one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 } .
$$

# Existence

It was first pointed out by Crouzeix & Raviart (198O) that the coercivity of the Runge-Kutta matrix $A$ (or of its inverse) plays an important role for the proof of existence.

Definition 14.1. We consider the inner product $\langle u , v \rangle _ { D } = u ^ { T } D v$ ，where $D =$ diag $( d _ { 1 } , \ldots , d _ { s } )$ with $d _ { \imath } > 0$ . We then denote by $\alpha _ { D } ( A ^ { - 1 } )$ the largest number $\alpha$ such that

$$
\begin{array} { r } { \langle u , A ^ { - 1 } u \rangle _ { D } \geq \alpha \langle u , u \rangle _ { D } \qquad \mathrm { f o r ~ a l l } \quad u \in \mathbb { R } ^ { s } . } \end{array}
$$

We also set

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { s u p } _ { D > 0 } \alpha _ { D } ( A ^ { - 1 } ) .
$$

The first existence results for the above problem were given by Crouzeix & Raviart (1980),Dekker (1982)and Crouzeix,Hundsdorfer & Spijker (1983). Their results can be summarized as follows:

Theorem 14.2. Let $f$ be continuously differentiable and satisfy (l4.2). If the Runge-Kutta matrix $A$ is invertible and

$$
h \nu < \alpha _ { 0 } ( A ^ { - 1 } )
$$

then the nonlinear system $( l 4 . l a )$ possesses a solution $( g _ { 1 } , \ldots , g _ { s } )$

Proof. The original proofs are based on the “uniform monotonicity theorem”or on similar results. We present here a more elementary version which, however, has the disadvantage of requiring the differentiability hypothesis for $f$ . The idea is to consider the homotopy

$$
g _ { \imath } = y _ { 0 } + h \sum _ { \jmath = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , g _ { \jmath } ) + ( \tau - 1 ) h \sum _ { \jmath = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , y _ { 0 } ) ,
$$

which is constructed in such a way that for $\tau = 0$ the system (14.6) has the solution $g _ { i } \simeq y _ { 0 }$ ,and for $\tau \simeq 1$ it is equivalent to (14.1a). We consider $g _ { \imath }$ as functions of $\tau$ and differentiate (14.6) with respect to this parameter. This gives

$$
{ \dot { g } } _ { i } = h \sum _ { j = 1 } ^ { s } a _ { i j } { \frac { \partial f } { \partial y } } ( x _ { 0 } + c _ { j } h , g _ { j } ) \cdot { \dot { g } } _ { j } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( x _ { 0 } + c _ { j } h , y _ { 0 } )
$$

or equivalently

$$
\left( I - h ( A \otimes I ) \{ f _ { y } \} \right) \dot { g } = h ( A \otimes I ) f _ { 0 }
$$

where we have used the notations

$$
\dot { \boldsymbol g } = ( \dot { g } _ { 1 } , \dots , \dot { g } _ { s } ) ^ { T } , \qquad \boldsymbol f _ { 0 } = \big ( f ( \boldsymbol x _ { 0 } + c _ { 1 } h , y _ { 0 } ) , \dots , f ( \boldsymbol x _ { 0 } + c _ { s } h , y _ { 0 } ) \big ) ^ { T }
$$

(more precisely, $\dot { g }$ should be written as $( \dot { g } _ { 1 } ^ { T } , \dots , \dot { g } _ { s } ^ { T } ) ^ { T } )$ and

$$
\{ f _ { y } \} = \mathrm { b l o c k d i a g } \Big ( \frac { \partial f } { \partial y } \big ( x _ { 0 } + c _ { 1 } h , g _ { 1 } \big ) , \ . . . , \frac { \partial f } { \partial y } \big ( x _ { 0 } + c _ { s } h , g _ { s } \big ) \Big ) .
$$

In order to show that $\dot { g }$ can be expressed as ${ \dot { g } } = G ( g )$ with a globally bounded $G ( g )$ , we take a $D$ satisfying $h \nu < \alpha _ { D } ( A ^ { - 1 } )$ , multiply (14.7) by $\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I )$ and so obtain

$$
\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I ) \dot { g } - h \dot { g } ^ { T } ( D \otimes I ) \{ f _ { y } \} \dot { g } = h \dot { g } ^ { T } ( D \otimes I ) f _ { 0 } .
$$

We now estimate the three individual terms of this equation.

The estimate

$$
\dot { g } ^ { T } ( D A ^ { - 1 } \otimes I ) \dot { g } \geq \alpha _ { D } ( A ^ { - 1 } ) \| \dot { g } \| _ { D } ^ { 2 } ,
$$

where we have introduced the notation $\| \dot { \boldsymbol { g } } \| _ { D } ^ { 2 } = \dot { g } ^ { T } ( D \otimes I ) \dot { \boldsymbol { g } }$ ,is (14.3) in the case of scalar differential equations (absence of $^ { 6 6 } \otimes I ^ { 5 7 } )$ . In the general case we must apply the ideas of Exercise 1 of Sect.IV.12 to the matrix ${ \scriptstyle { \frac { 1 } { 2 } } } ( D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } ) -$ $\alpha _ { D } ( A ^ { - 1 } ) D$ ，which is non-negative definite by Definition 14.1. It follows from (14.2) with $y = z + \varepsilon u$ that

$$
\left. \varepsilon \frac { \partial f } { \partial y } \left( x , z \right) u + o ( \varepsilon ) , \varepsilon u \right. \leq \nu \varepsilon ^ { 2 } \| u \| ^ { 2 } .
$$

Dividing by $\varepsilon ^ { 2 }$ and taking the limit $\varepsilon \to 0$ we obtain $\begin{array} { r } { \langle u , \frac { \partial f } { \partial y } ( x , z ) u \rangle \leq \nu \| u \| ^ { 2 } } \end{array}$ for all $( x , z )$ and all $u$ . Consequently we also have

$$
\dot { g } ^ { T } ( D \otimes I ) \{ f _ { y } \} \dot { g } \leq \nu \| \dot { g } \| _ { D } ^ { 2 } .
$$

The right-hand term of (14.8) is bounded by $h \| \dot { g } \| _ { D } \cdot \| f _ { 0 } \| _ { D }$ by the Cauchy-Schwarz-Bunjakowski inequality.

Inserting these three estimates into (14.8) yields

$$
\left( \alpha _ { D } ( A ^ { - 1 } ) - h \nu \right) \| | { \dot { g } } \| | _ { D } ^ { 2 } \leq h \| { \dot { g } } \| _ { D } \cdot \| | f _ { 0 } \| _ { D } .
$$

This proves that $\dot { g }$ can be written as ${ \dot { g } } = G ( g )$ with

$$
\| G ( g ) \| _ { D } \leq { \frac { h \| f _ { 0 } \| _ { D } } { \alpha _ { D } ( A ^ { - 1 } ) - h \nu } } .
$$

It now follows from Theorem 7.4 (Sect.I.7) that this differential equation with initial values $g _ { i } ( 0 ) = y _ { 0 }$ possesses a solution for all $\tau$ , in particular also for $\tau \simeq 1$ This proves the existence of a solution of (14.1a). □

Remark. It has recently been shown by Kraaijevanger & Schneid (1991, Theorem 2.12) that Condition (14.5) is “essentially optimal".

# A Counterexample

After our discussion that Monday afternoon (October 1980) I went for a walk and I got the idea for the counterexample.

(M.N. Spijker)

The inequality in (14.5) is strict, therefore Theorem 14.2 (together with Exercise 1 below) does not yet answer the simple question: “does a $B$ -stable method on a contractive problem $( \nu = 0 )$ always admit a solution". A first counterexample to this statement has been given by Crouzeix,Hundsdorfer & Spijker (1983). An easy idea for constructing another counterexample is to use the $W$ -transformation (see Sections IV.5 and IV.13) as follows:

We put $s \approx 4$ and take a quadrature formula with positive weights, say,

$$
( c _ { \imath } ) = ( 0 , 1 / 3 , 2 / 3 , 1 ) , ~ ( b _ { \imath } ) = ( 1 / 8 , 3 / 8 , 3 / 8 , 1 / 8 ) .
$$

We then construct a matrix $W$ satisfying property $T ( 1 , 1 )$ according to Lem-ma 5.12. This yields for the above quadrature formula

$$
W = \left( \begin{array} { c c c c } { { 1 } } & { { - \sqrt { 3 } } } & { { \sqrt { 3 } } } & { { - 1 } } \\ { { 1 } } & { { - \sqrt { 3 } / 3 } } & { { - \sqrt { 3 } / 3 } } & { { 1 } } \\ { { 1 } } & { { \sqrt { 3 } / 3 } } & { { - \sqrt { 3 } / 3 } } & { { - 1 } } \\ { { 1 } } & { { \sqrt { 3 } } } & { { \sqrt { 3 } } } & { { 1 } } \end{array} \right) .
$$

Finally, we put (with $\xi _ { 1 } = 1 / ( 2 \sqrt { 3 } ) )$

$$
\begin{array} { r } { A = W X W ^ { - 1 } \quad \mathrm { w i t h } \quad X = \left( \begin{array} { c c c c } { 1 / 2 } & { - \xi _ { 1 } } & { 0 } & { 0 } \\ { \xi _ { 1 } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { - \beta } \\ { 0 } & { 0 } & { \beta } & { 0 } \end{array} \right) . } \end{array}
$$

For $\beta = 1 / ( 4 \sqrt { 3 } )$ this gives nice rational coefficients for the RK-matrix,namely

$$
A = \frac { 1 } { 4 8 } \left( \begin{array} { c c c c } { { 3 } } & { { 0 } } & { { 3 } } & { { - 6 } } \\ { { 6 } } & { { 9 } } & { { 0 } } & { { 1 } } \\ { { 5 } } & { { 1 8 } } & { { 9 } } & { { 0 } } \\ { { 1 2 } } & { { 1 5 } } & { { 1 8 } } & { { 3 } } \end{array} \right) .
$$

It follows from Theorem 13.15 that this method is algebraically stable and of order 4. However,± $i \beta$ is an eigenvalue pair of $X$ and hence also of $A$ .

We thus choose the differential equation

$$
y ^ { \prime } = J y + f ( x ) \quad \mathrm { w i t h } \quad J = \left( { \begin{array} { c c } { 0 } & { - 1 / \beta } \\ { 1 / \beta } & { 0 } \end{array} } \right) ,
$$

which satisfies (14.2) with $\nu = 0$ independent of the choice of $f ( x )$ . If we apply the above method with $h \approx 1$ to this problem and initial values $x _ { 0 } = 0$ ， $y _ { 0 } = ( 0 , 0 ) ^ { T }$ ， Eq.(14.1a) becomes equivalent to the linear system

$$
( I - A \otimes J ) g = ( A \otimes I ) f _ { 0 } ,
$$

where $g = ( g _ { 1 } , \ldots , g _ { 4 } ) ^ { T }$ and $f _ { 0 } = ( f ( c _ { 1 } ) , \ldots , f ( c _ { 4 } ) ) ^ { T }$ . The matrix $\left( I - A \otimes J \right)$ is singular because the eigenvalues of $I - A \otimes J$ are just $1 - \lambda \mu$ where $\lambda$ and $\mu$ are the eigenvalues of $A$ and $J$ ,respectively. However, $A$ is regular, therefore it is possible to choose $f ( x )$ in such a way that this equation does not have a solution.

# Influence of Perturbations and Uniqueness

Our next problem is the question, how perturbations in the Runge-Kutta equations influence the numerical solution. Research into this problem was initiated independently by Frank, Schneid & Ueberhuber (preprint 1981, published 1985) and Dekker (1982).

As above, we use the notations

$$
\begin{array} { r l r } & { \| u \| _ { D } = \sqrt { u ^ { T } D u } = \sqrt { \langle u , u \rangle _ { D } } \quad } & { u \in \mathbb { R } ^ { s } } \\ & { \| g \| _ { D } = \sqrt { g ^ { T } ( D \otimes I ) g } \quad } & { g \in \mathbb { R } ^ { s n } } \end{array}
$$

and $\| A \| _ { D }$ for the corresponding matrix norm.

Theorem 14.3 (Dekker 1984). Let $g _ { i }$ and $y _ { 1 }$ be given by (14.1) and consider perturbed values $\widehat { g } _ { i }$ and $\widehat { y } _ { 1 }$ satisfying

$$
\begin{array} { l } { { \displaystyle { \widehat { g } } _ { i } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } a _ { i j } f \big ( x _ { 0 } + c _ { j } h , \widehat { g } _ { j } \big ) + \delta _ { i } } } \\ { { \displaystyle { \widehat { y } } _ { 1 } = y _ { 0 } + h \sum _ { j = 1 } ^ { s } b _ { j } f \big ( x _ { 0 } + c _ { j } h , \widehat { g } _ { j } \big ) } . } \end{array}
$$

If the Runge-Kutta matrix $A$ is invertible,if the one-sided Lipschitz condition(14.2) is satisfied, and $h \nu < \alpha _ { D } ( A ^ { - 1 } )$ for some positive diagonal matrix $D$ , then we have the estimates

$$
\begin{array} { r l } & { \left\| \left. \widehat { g } - g \right. \right\| _ { D } \leq \frac { \left\| A ^ { - 1 } \right\| _ { D } } { \alpha _ { D } \left( A ^ { - 1 } \right) - h \nu } \left\| \delta \right\| _ { D } } \\ & { \left\| \widehat { y } _ { 1 } - y _ { 1 } \right\| \leq \| b ^ { T } A ^ { - 1 } \| _ { D } \Bigg ( 1 + \frac { \left\| A ^ { - 1 } \right\| _ { D } } { \alpha _ { D } \left( A ^ { - 1 } \right) - h \nu } \Bigg ) \left\| \left. \delta \right. \right\| _ { D } , } \end{array}
$$

$$
g = ( g _ { 1 } , \ldots , g _ { s } ) ^ { T } , { \widehat { g } } = ( { \widehat { g } } _ { 1 } , \ldots , { \widehat { g } } _ { s } ) ^ { T } , a n d \delta = ( \delta _ { 1 } , \ldots , \delta _ { s } ) ^ { T } .
$$

Proof. With the notation $\Delta g = \widehat { g } - g$ and

$$
\Delta f = \left( f ( x _ { 0 } + c _ { 1 } h , \widehat g _ { 1 } ) - f ( x _ { 0 } + c _ { 1 } h , g _ { 1 } ) , \ldots , f ( x _ { 0 } + c _ { s } h , \widehat g _ { s } ) - f ( x _ { 0 } + c _ { s } h , g _ { s } ) \right) ^ { T }
$$

the difference of (14.11a) and (14.1a) can be written as

$$
\Delta g = h ( A \otimes I ) \Delta f + \delta .
$$

As in the proof of Theorem 14.2 we multiply this equation by $\Delta g ^ { T } ( D A ^ { - 1 } \otimes I )$ and obtain

$$
\Delta g ^ { T } ( D A ^ { - 1 } \otimes I ) \Delta g - h \Delta g ^ { T } ( D \otimes I ) \Delta f = \Delta g ^ { T } ( D A ^ { - 1 } \otimes I ) \delta .
$$

This equation is very similar to Eq.(14.8) and we estimate it in the same way: since $D$ is a diagonal matrix with positive entries,it follows from (14.2) that

$$
\Delta g ^ { T } ( D \otimes I ) \Delta f \leq \nu \| \Delta g \| _ { D } ^ { 2 } .
$$

Inserting (14.15) and (14.9) (with $\dot { g }$ replaced by $\Delta g$ ） into (14.14) we get

$$
\left( \alpha _ { D } ( A ^ { - 1 } ) - h \nu \right) \| | \Delta g \| | _ { D } ^ { 2 } \leq \| \Delta g \| _ { D } \| | ( A ^ { - 1 } \otimes I ) \delta \| _ { D }
$$

which implies (14.12). The estimate (14.13) then follows immediately from

$$
\begin{array} { r } { \widehat { y } _ { 1 } - y _ { 1 } = h ( \boldsymbol { b } ^ { T } \otimes I ) \Delta f = ( \boldsymbol { b } ^ { T } A ^ { - 1 } \otimes I ) ( \Delta g - \delta ) . } \end{array}
$$

Putting $\delta \simeq 0$ in Theorem 14.3 we get the following uniqueness result.

Theorem 14.4. Consider a differential equation satisfying (14.2). If the Runge-Kutta matrix $A$ is invertible and $h \nu < \alpha _ { 0 } ( A ^ { - 1 } )$ , then the system $( l 4 . l a )$ possesses at most one solution. □

# Computation of $\alpha _ { 0 } ( A ^ { - 1 } )$

... the determination of a suitable matrix $D$ ... This task does not seem easy at first glance ... (K.Dekker 1984)

The value $\alpha _ { D } ( A ^ { - 1 } )$ of Definition 14.1 is the smallest eigenvalue of the symmetric matrix $\left( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } + ( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } ) ^ { T } \right) / 2$ .The computation of $\alpha _ { 0 } ( A ^ { - 1 } )$ is more difficult, because the optimal $D$ is not known in general.

An upper bound for $\alpha _ { 0 } \big ( A ^ { - 1 } \big )$ is

$$
\alpha _ { 0 } ( A ^ { - 1 } ) \leq \operatorname* { m i n } _ { i = 1 , \ldots , s } \omega _ { \ i i }
$$

where $\omega _ { \imath j }$ are the entries of $A ^ { - 1 }$ . This follows from (14.3) by putting $u \approx e _ { i }$ ,the $i$ th unit vector.

Lower bounds for $\alpha _ { 0 } ( A ^ { - 1 } )$ were first given by Frank, Schneid & Ueberhuber in 1981. Following are the exact values due to Dekker (1984), Dekker & Verwer (1984, p.55-164),and Dekker & Hairer (1985) (see also Liu & Kraaijevanger 1988 and Kraaijevanger & Schneid 1991).

Theorem 14.5. For the methods of Sect. IV.5 we have:

<table><tr><td>Gauss</td><td>α(A-1)=.min</td><td>i=m,， 2c(1-c）</td><td>1</td></tr><tr><td>Radau IA</td><td>α0(A-1)=</td><td>1 1 2（1-c2）</td><td>if s=1, if s&gt;1,</td></tr><tr><td>Radau IA</td><td>α0(A-1) =</td><td>（1 1 2cg-1</td><td>if s=1, if s&gt;1,</td></tr><tr><td>Lobatto IIIC</td><td></td><td></td><td>if s= 2, if s &gt;2.</td></tr></table>

Proof. a) Gauss methods: written out in “symmetricized form”,estimate (14.3) reads

$$
\frac { 1 } { 2 } u ^ { T } \big ( D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } \big ) u \geq \alpha u ^ { T } D u .
$$

Evidently the sharpest estimates come out if $D$ is such that the left-hand matrix is as “close to diagonal as possble". After many numerical computations, Dekker had the nice surprise that with the choice $D = B ( C ^ { - 1 } - I )$ ，where $B =$ diag $\left( b _ { 1 } , \ldots , b _ { s } \right)$ and $C = \operatorname { d i a g } \left( c _ { 1 } , \ldots , c _ { s } \right)$ , the matrix

$$
D A ^ { - 1 } + \left( D A ^ { - 1 } \right) ^ { T } = B C ^ { - 2 }
$$

becomes completely diagonal. Then the optimal $\alpha$ is simply obtained by testing the unit vectors $u \simeq e _ { k }$ ,which gives

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { m i n } _ { i } { \frac { b _ { i } } { 2 c _ { i } ^ { 2 } d _ { i } } } = \operatorname* { m i n } _ { i } { \frac { b _ { i } } { 2 c _ { i } ^ { 2 } b _ { i } ( 1 / c _ { i } - 1 ) } } = \operatorname* { m i n } _ { i } { \frac { 1 } { 2 c _ { i } ( 1 - c _ { i } ) } } .
$$

It remains to prove (14.17): we verify the equivalent formula

$$
V ^ { T } ( A ^ { T } D + D A - A ^ { T } B C ^ { - 2 } A ) V = 0
$$

where $V = ( c _ { \imath } ^ { \jmath - 1 } )$ is the Vandermonde matrix. The $( l , m )$ -element of the matrix (14.18) is

$$
\begin{array} { r } { \displaystyle \sum _ { \imath , \jmath } b _ { \jmath } \Big ( \frac { 1 } { c _ { j } } - 1 \Big ) a _ { \jmath i } c _ { \imath } ^ { l - 1 } c _ { \jmath } ^ { m - 1 } + \displaystyle \sum _ { \imath , j } b _ { \imath } \Big ( \frac { 1 } { c _ { \imath } } - 1 \Big ) a _ { \imath j } c _ { i } ^ { l - 1 } c _ { \jmath } ^ { m - 1 } } \\ { - \displaystyle \sum _ { \imath , \jmath , k } b _ { \imath } \frac { 1 } { c _ { \imath } ^ { 2 } } a _ { \imath k } c _ { k } ^ { l - 1 } a _ { \imath j } c _ { \jmath } ^ { m - 1 } . } \end{array}
$$

With the help of the simplifying assumptions $C ( s )$ and $B ( 2 s )$ the expression (14.19) can be seen to be zero.

b) For the Radau IA methods we take $D = B ( I - C )$ and show that

$$
D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } = B + e _ { 1 } e _ { 1 } ^ { T } .
$$

The stated formula for $\alpha _ { 0 } ( A ^ { - 1 } )$ then follows from $0 = c _ { 1 } < c _ { 2 } < . . . < c _ { s }$ and from

$$
{ \frac { b _ { 1 } + 1 } { b _ { 1 } } } \geq { \frac { 1 } { 1 - c _ { 2 } } } ,
$$

which is a simple consequence of $b _ { 1 } = 1 / s ^ { 2 }$ (see Abramowitz & Stegun (1964), Formula 25.4.31). For the verification of (14.20) one shows that $V ^ { T } ( D A ^ { - 1 } +$ $( D A ^ { - 1 } ) ^ { T } - B - e _ { 1 } e _ { 1 } ^ { T } ) V = 0$ . Helpful formulas for this verification are $A ^ { - 1 } V e _ { 1 } =$ $b _ { 1 } ^ { - 1 } e _ { 1 }$ ， $V ^ { T } e _ { 1 } = e _ { 1 }$ and $A ^ { - 1 } V e _ { \jmath } = ( j - 1 ) V e _ { \jmath - 1 }$ for $j \geq 2$

c) Similarly, the statement for the Radau IIA methods follows with $D = B C ^ { - 1 }$ from the identity

$$
D A ^ { - 1 } + ( D A ^ { - 1 } ) ^ { T } = B C ^ { - 2 } + e _ { s } e _ { s } ^ { T } .
$$

d) As in part (b) one proves for the Lobatto IIIC methods that

$$
\boldsymbol { B A } ^ { - 1 } + ( \boldsymbol { B A } ^ { - 1 } ) ^ { T } = \boldsymbol { e } _ { 1 } \boldsymbol { e } _ { 1 } ^ { T } + \boldsymbol { e } _ { s } \boldsymbol { e } _ { s } ^ { T } .
$$

Since this matrix is diagonal, we obtain $\alpha _ { 0 } ( A ^ { - 1 } ) = 1$ for $s \approx 2$ and $\alpha _ { 0 } { \left( A ^ { - 1 } \right) } = 0$ for $s > 2$ . □

For diagonally implicit Runge-Kuta methods we have the following result.

Theorem 14.6 (Montijano 1983). For a DIRK-method with positive $a _ { \ i i } \ m e$ have

$$
\alpha _ { 0 } ( A ^ { - 1 } ) = \operatorname* { m i n } _ { \imath = 1 , \imath \to \imath } \frac { 1 } { a _ { \imath i } } .
$$

Proof. With $D = \operatorname { d i a g } \left( 1 , \varepsilon ^ { 2 } , \varepsilon ^ { 4 } , \dots , \varepsilon ^ { 2 s - 2 } \right)$ we obtain

$$
D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } + ( D ^ { 1 / 2 } A ^ { - 1 } D ^ { - 1 / 2 } ) ^ { T } = \mathrm { d i a g } ( a _ { 1 1 } ^ { - 1 } , \ldots , a _ { s s } ^ { - 1 } ) + { \mathcal O } ( { \varepsilon } ) ,
$$

so that $\alpha _ { 0 } ( A ^ { - 1 } ) \geq \operatorname* { m i n } _ { \ i } a _ { i \ i } ^ { - 1 } + { \mathcal { O } } ( \varepsilon )$ . This inequality for $\varepsilon \to 0$ and (14.16) prove the statement. □

# Methods with Singular $\mathbf { A }$

For the Lobatto IIIA methods the first stage is explicit (the first row of $A$ vanishes) and for the Lobatto IIB methods the last stage is explicit (the last column of $A$ vanishes). For these methods the Runge-Kutta matrix is of the form

$$
A = \left( \begin{array} { l l } { { 0 } } & { { 0 } } \\ { { a } } & { { \widetilde { A } } } \end{array} \right) \qquad \mathrm { o r } \qquad A = \left( \begin{array} { l l } { { \widetilde { A } } } & { { 0 } } \\ { { a ^ { T } } } & { { 0 } } \end{array} \right)
$$

and we have the following variant of Theorem 14.2.

Theorem 14.7． Let $f$ be continuously differentiable and satisfy (14.2). If the Runge-Kutta matrix is given by one of the matrices in (14.23) with invertible $\widetilde { A }$ ， then the assumption

$$
h \nu < \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } )
$$

implies that the nonlinear system $( l 4 . l a )$ has a solution.

Proof. The explicit stage poses no problem for the existence of a solution. To obtain the result we repeat the proof of Theorem 14.2 for the $s - 1$ implicit stages (i.e., $A$ is replaced by $\widetilde { A }$ and the inhomogenity in (14.6) may be different). □

An explicit formula for $\alpha _ { 0 } { \big ( } { \overset { \sim } { A } } ^ { - 1 } { \big ) }$ for the Lobatto IIIB methods has been given by Dekker & Verwer (1984),and for the Lobatto IIIA methods by Liu,Dekker & Spijker (1987). The result is

Theorem 14.8. We have for

$$
\begin{array} { r l } & { \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } ) = \left\{ \begin{array} { l l } { 2 \quad \quad \quad } & { i f s = 2 , } \\ { c _ { s - 1 } ^ { - 1 } \quad \quad } & { i f s > 2 , } \end{array} \right. } \\ & { \alpha _ { 0 } ( \widetilde { A } ^ { - 1 } ) = \left\{ \begin{array} { l l } { 2 \quad \quad } & { i f s = 2 , } \\ { ( 1 - c _ { 2 } ) ^ { - 1 } \quad \quad } & { i f s > 2 . } \end{array} \right. } \end{array}
$$

Proof. For the Lobatto IIA methods we put $D = \widetilde { B } \widetilde { C } ^ { - 2 }$ with the diagonal matrices $\widetilde { \boldsymbol B } = \mathrm { d i a g } \left( \boldsymbol b _ { 2 } , \dots , \boldsymbol b _ { s } \right)$ and $\widetilde { C } = \mathrm { d i a g } \left( \bar { c _ { 2 } } , \dots , c _ { s } \right)$ . As in part (a) of the proof of Theorem 14.5 we get

$$
D \widetilde { A } ^ { - 1 } + ( D \widetilde { A } ^ { - 1 } ) ^ { T } = e _ { s - 1 } e _ { s - 1 } ^ { T } + 2 \widetilde { B } \widetilde { C } ^ { - 3 }
$$

which implies the formula for $\alpha _ { 0 } ( \stackrel { \sim } { A } ^ { - 1 } )$ ， because $b _ { \pmb { s } } = ( \pmb { s } ( \pmb { s } - 1 ) ) ^ { - 1 }$ and $( 1 +$ $2 b _ { s } ) \geq b _ { s } / c _ { s - 1 }$ for $s > 2$

For the Lobatto IB methods the choice $D = \widetilde { B } ( I - \widetilde { C } ) ^ { 2 }$ (with the matrices $\widetilde { B } = \mathrm { d i a g } \left( b _ { 1 } , \ldots , b _ { s - 1 } \right)$ ， $\widetilde { C } = \mathrm { d i a g } \left( c _ { 1 } , \dots , c _ { s - 1 } \right) )$ leads to

$$
D \widetilde { A } ^ { - 1 } + ( D \widetilde { A } ^ { - 1 } ) ^ { T } = e _ { 1 } e _ { 1 } ^ { T } + 2 \widetilde { B } ( I - \widetilde { C } ) .
$$

This proves the second statement.

Methods with explicit stages (such as Lobatto IIIA and IIB) don't allow estimates of the numerical solution in the presence of arbitrary perturbations. They are usually not $A N$ -stable and $K ( Z )$ is not bounded (see Theorem 12.12). Nevertheless we have the following uniqueness result.

Theorem 14.9. Consider a differential equation satisfying (14.2). If the Runge-Kutta matrix is of the form (14.23) with invertible $\widetilde { A }$ and if $h \nu < \alpha _ { 0 } \big ( \widetilde { A } ^ { - 1 } \big )$ ，then the nonlinear system $( l 4 . l a )$ has at most one solution.

Proof. Suppose, there exists a second solution ${ \widehat { g } } _ { \imath }$ satisfying (14.11a) with $\delta _ { \imath } = 0$ . a) If the first stage is explicit we have $\widehat { g } _ { 1 } = g _ { 1 }$ . The difference of the two Runge-Kutta formulas then yields

$$
\Delta g = h ( \widetilde { A } \otimes I ) \Delta f
$$

with $\Delta g = ( \widehat { g } _ { \imath } - g _ { \imath } ) _ { \imath = 2 } ^ { s }$ and $\Delta f = ( f ( x _ { 0 } + c _ { \imath } h , \widehat { g } _ { \imath } ) - f ( x _ { 0 } + c _ { \imath } h , g _ { \imath } ) ) _ { \imath = 2 } ^ { s }$ . As in the proof of Theorem 14.3 we then conclude that $\Delta g = 0$

b) In the second case we can apply Theorem 14.3 to the first $s - 1$ stages, which yields uniqueness of $g _ { 1 } , \ldots , g _ { s - 1 }$ . Clearly, $g _ { s }$ also is unique, because the last stage is explicit. □

# Lobatto IIC Methods

For the Lobatto IIIC methods with $s \geq 3$ we have $\alpha _ { 0 } \big ( A ^ { - 1 } \big ) = 0$ (see Theorem 14.5). Since these methods are algebraically stable it is natural to ask whether the non-linear system (14.1a) also has a solution for differential equations satisfying (14.2) with $\nu = 0$ ． A positive answer to this question has been given by Hundsdorfer & Spijker (1987) for the case $s = 3$ , and by Liu & Kraaijevanger (1988) for the general case $s \geq 3$ (see Exercise 6 below; see also Kraaijevanger & Schneid 1991).

# Exercises

1. Prove that $\alpha _ { 0 } ( A ) \geq 0$ for algebraically stable Runge-Kutta methods. Also, $\alpha _ { 0 } ( A ^ { - 1 } ) \geq 0$ if in addition the matrix $A$ is invertible.

2.Let $A$ be a real matrix. Show that $\alpha _ { 0 } ( A ) \leq \operatorname { R e } \lambda$ ,where $\lambda$ is an eigenvalue of $A$

3. (Hundsdorfer 1985,Cooper 1986). Prove that Theorem 14.2 remains valid for singular $A$ ,if $h \nu < \alpha$ with $\alpha$ satisfying

$$
\langle u , A u \rangle _ { D } \geq \alpha \langle A u , A u \rangle _ { D } \qquad { \mathrm { f o r ~ a l l } } \quad u \in \mathbb { R } ^ { s } .
$$

Hint. Use the transformation $g = \mathbb { 1 } \otimes y _ { 0 } + ( A \otimes I ) k$ and apply the ideas of the proof of Theorem 14.2 to the homotopy

$$
k _ { i } = f ( x _ { 0 } + c _ { i } h , y _ { 0 } + h \sum _ { \jmath = 1 } ^ { \ s } a _ { \imath j } k _ { j } ) + ( \tau - 1 ) f ( x _ { 0 } + c _ { i } h , y _ { 0 } ) .
$$

4. (Barker, Berman & Plemmons 1978, Montijano 1983). Prove that for any twostage method the condition

$$
a _ { 1 1 } > 0 , \qquad a _ { 2 2 } > 0 , \qquad \operatorname* { d e t } ( A ) > 0
$$

is equivalent to $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$

Remark. For a generalization of this result to three-stage methods see Kraaijevanger (1991).

5.For the two-stage Radau IIA method we have $\alpha _ { 0 } ( A ^ { - 1 } ) = 3 / 2$ . Construct a differential equation $y ^ { \prime } = \lambda ( x ) y$ with $\operatorname { R e } \lambda ( x ) = 3 / 2 + \varepsilon$ $\vert \varepsilon > 0$ arbitrarily small) such that the Runge-Kutta equations do not admit a unique solution for all $h > 0$

6. Prove that for the Lobatto IIIC methods (with $s \geq 3$ ） the matrix

$$
I - ( A \otimes I ) J \quad { \mathrm { w i t h } } \quad J = { \mathrm { b l o c k d i a g } } \left( J _ { 1 } , \dots , J _ { s } \right)
$$

is non-singular, if $\mu _ { 2 } ( J _ { k } ) \leq 0$ . This implies that the Runge-Kutta equations (14.1a) have a unique solution for all problems $y ^ { \prime } = A ( x ) y + f ( x )$ with $\mu _ { 2 } ( A ( x ) ) \leq 0$

Hint (Liu & Kraaijevanger 1988,Liu,Dekker & Spijker 1987).Let $v =$ $( v _ { 1 } , \ldots , v _ { s } ) ^ { T }$ be a solution of $( I - ( A \otimes I ) J ) v = 0$ . With the help of (14.21) show first that $v _ { 1 } = v _ { s } = 0$ . Then consider the $\left( s - 2 \right)$ -dimensional submatrix $\widetilde { A } = ( a _ { i j } ) _ { i , \jmath = 2 } ^ { s - 1 }$ and prove $\alpha _ { 0 } \big ( \widetilde { A } ^ { - 1 } \big ) > 0$ byconsideringthediagoalmatrix $\widetilde { D } =$ diag $\ ( b _ { \ i } ( c _ { i } ^ { - 1 } - 1 ) ^ { 2 } ) _ { i = 2 } ^ { s - 1 }$

7. Consider an algebraically stable Runge-Kutta method with invertible $A$ and apply it to the differential equation $y ^ { \prime } { = } ( J ( x ) { - } \varepsilon I ) y + f ( x )$ where $\mu ( J ( x ) ) \leq$ $0$ and $\varepsilon > 0$ . Prove that the numerical solution $y _ { 1 } \left( \varepsilon \right)$ converges to a limit for $\varepsilon \to 0$ , whereas the internal stages $g _ { \imath } ( \varepsilon )$ need not converge.

Hint. Expand the $g _ { \imath } ( \varepsilon )$ in a series $g _ { i } ( \varepsilon ) = \varepsilon ^ { - 1 } g _ { i } ^ { ( - 1 ) } + g _ { i } ^ { ( 0 ) } + \varepsilon g _ { \imath } ^ { ( 1 ) } + \ldots .$ and prove the implication

$$
\begin{array} { c } { { g = \left( A \otimes I \right) J g \quad \Longrightarrow \quad ( b ^ { T } \otimes I ) J g = 0 } } \\ { { \mid = \mathrm { b l o c k d i a g } \left( J ( x _ { 0 } + c _ { 1 } h ) , \ldots , J ( x _ { 0 } + c _ { s } h ) \right) . } } \end{array}
$$

In using $A$ -stable one-step methods to solve large systems of stiff nonlinear differential equations, we have found that - (a) some $A$ -stable methods give highly unstable solutions,and 一 (b) the accuracy of the solutions obtained when the equations are stiff often appears to be unrelated to the order of the method used.

This has caused us to re-examine the form of stability required when stiff systems of equations are solved,and to question the relevance of the concept of (nonstiff) order of accuracy for stiff problems. (A.Prothero & A.Robinson 1974)

Prothero & Robinson (1974) were the first to discover the order reduction of implicit Runge-Kutta methods when applied to stiff differential equations. Frank, Schneid & Ueberhuber(1981) then introduced the “concept of $B$ -convergence", which furnishes global error estimates independent of the stiffness.

# The Order Reduction Phenomenon

For the study of the accuracy of Runge-Kutta methods applied to stiff differential equations, Prothero & Robinson (1974) proposed considering the problem

$$
y ^ { \prime } = \lambda { \bigl ( } y - \varphi ( x ) { \bigr ) } + \varphi ^ { \prime } ( x ) , \qquad y ( x _ { 0 } ) = \varphi ( x _ { 0 } ) , \qquad { \mathrm { R e ~ } } \lambda \leq 0 .
$$

This allows explicit formulas for the local and global errors and provides much new insight.

Applying a Runge-Kutta method to (15.1) yields

$$
\begin{array} { l } { { g _ { i } = y _ { 0 } + h \displaystyle \sum _ { j = 1 } ^ { s } a _ { i _ { j } } \left( \lambda \big ( g _ { \jmath } - \varphi ( x _ { 0 } + c _ { j } h ) \big ) + \varphi ^ { \prime } \big ( x _ { 0 } + c _ { j } h \big ) \right) } } \\ { { \displaystyle y _ { 1 } = y _ { 0 } + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } \left( \lambda \big ( g _ { \jmath } - \varphi ( x _ { 0 } + c _ { j } h ) \big ) + \varphi ^ { \prime } \big ( x _ { 0 } + c _ { j } h \big ) \right) } . } \end{array}
$$

If we replace here the $g _ { \imath } , y _ { 0 }$ and $y _ { 1 }$ by the exact solution values $\varphi ( x _ { 0 } + c _ { \iota } h )$ ， $\varphi ( x _ { 0 } )$ and $\varphi ( x _ { 0 } + h )$ , respectively, we obtain a defect which is given by

$$
\begin{array} { r } { \varphi ( x _ { 0 } + c _ { \iota } h ) = \varphi ( x _ { 0 } ) + h \displaystyle \sum _ { \jmath = 1 } ^ { s } a _ { i j } \varphi ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) + \Delta _ { i , h } ( x _ { 0 } ) } \\ { \varphi ( x _ { 0 } + h ) = \varphi ( x _ { 0 } ) + h \displaystyle \sum _ { \jmath = 1 } ^ { s } b _ { j } \varphi ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) + \Delta _ { 0 , h } ( x _ { 0 } ) . } \end{array}
$$

Taylor series expansion of the functions in (15.3) shows that

$$
\Delta _ { 0 , h } ( x _ { 0 } ) = \mathcal { O } ( h ^ { p + 1 } ) , \qquad \Delta _ { \iota , h } ( x _ { 0 } ) = \mathcal { O } ( h ^ { q + 1 } ) ,
$$

where $p$ is the order of the quadrature formula $\left( \boldsymbol { b } _ { \imath } , \boldsymbol { c } _ { \imath } \right)$ and $q$ is the largest number such that the condition $C ( q )$ (see Sect. IV.5), i.e.,

$$
\sum _ { \jmath = 1 } ^ { s } a _ { \imath j } c _ { \jmath } ^ { k - 1 } = \frac { c _ { \imath } ^ { k } } { k } \qquad \mathrm { f o r } \quad k = 1 , \dots , q \quad \mathrm { a n d ~ a l l } \quad \imath ,
$$

holds. The minimum of $q$ and $p$ is often called the stage order of the Runge-Kutta method. Subtracting (15.3) from (15.2) and eliminating the internal stages we get

$$
y _ { 1 } - \varphi ( x _ { 0 } + h ) = R ( z ) ( y _ { 0 } - \varphi ( x _ { 0 } ) ) - z b ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x _ { 0 } ) - \Delta _ { 0 , h } ( x _ { 0 } )
$$

where we have used the notation $z \approx \lambda h$ ， $R ( z ) = 1 + z b ^ { T } ( I - z A ) ^ { - 1 } \mathbb { 1 }$ for the stability function and $\Delta _ { h } ( x ) = ( \Delta _ { 1 , h } ( x ) , \dots , \Delta _ { s , h } ( x ) ) ^ { T }$ . We also denote the local error, which we get from(15.6) on putting $y _ { 0 } = \varphi ( x _ { 0 } )$ ,by

$$
\delta _ { h } ( x ) = - z b ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x ) - \Delta _ { 0 , h } ( x ) .
$$

If we repeat the above calculation with $x _ { n }$ instead of $x _ { 0 }$ we obtain the recursion

$$
y _ { n + 1 } - \varphi ( x _ { n + 1 } ) = R ( z ) ( y _ { n } - \varphi ( x _ { n } ) ) + \delta _ { h } ( x _ { n } )
$$

which leads to the following formula for the global error

$$
y _ { n + 1 } - \varphi ( x _ { n + 1 } ) = R ( z ) ^ { n + 1 } { \bigl ( } y _ { 0 } - \varphi ( x _ { 0 } ) { \bigr ) } + \sum _ { \jmath = 0 } ^ { n } R ( z ) ^ { n - \jmath } \delta _ { h } ( x _ { \jmath } ) .
$$

The classical (non-stiff) theory treats the case where $z = \mathcal { O } ( h )$ and in this situation the global error behaves like $\mathcal { O } ( h ^ { p } )$ .When solving stiff differential equations one is interested in step sizes $h$ which are much larger than $| \lambda | ^ { - 1 }$ . We therefore study the global error (15.9) under the assumption that simultaneously $h  0$ and $z = \lambda h  \infty$ . In Table 15.1 we collect the results for the Runge-Kutta methods of Sect.IV.5. There in the last column (variable $h$ ) the symbols $h$ and $z$ have to be interpreted as max $h _ { \iota }$ and $z = \lambda \operatorname* { m i n } h _ { \iota }$ . We remark that Formulas (15.7) and (15.8) (but not (15.9)) remain valid for variable $h$ ,if $z$ is replaced by $z _ { n } = h _ { n } \lambda$

Table 15.1. Error for (15.1） when $h  0$ and $z = h \lambda \to \infty$   

<table><tr><td colspan="2">Method</td><td>local error</td><td colspan="2">global error</td></tr><tr><td colspan="2">odd</td><td></td><td>constant h {h8+1</td><td>variable h</td></tr><tr><td colspan="2">s Gauss even s</td><td>h8+1</td><td>h</td><td>h</td></tr><tr><td colspan="2">Radau IA</td><td>h</td><td>h</td><td>h</td></tr><tr><td colspan="2">Radau IA odd</td><td>x-1h8+1</td><td>z-1h8+1 {x-1h8</td><td>z-1h8+1</td></tr><tr><td colspan="2">Lobatto IIIA s s even</td><td>x-1h8+1</td><td>z-1h8+1</td><td>x-1h8</td></tr><tr><td rowspan="3">LobattoIIIB s</td><td>odd S</td><td>zh8-2 zh8-1</td><td></td><td>zh8-2</td></tr><tr><td>even</td><td>zh-1</td><td></td><td></td></tr><tr><td>x-1h</td><td>x-1h8</td><td></td><td>x-1hg</td></tr></table>

# Verification of Table 15.1.

Gauss. Since the Runge-Kutta matrix $A$ is invertible, we have $- z b ^ { T } ( I - z A ) ^ { - 1 } =$ $b ^ { T } A ^ { - 1 } + { \mathcal { O } } ( z ^ { - 1 } )$ and (15.4) inserted into (15.7) gives $\begin{array} { r } { \boldsymbol { \mathcal { S } } _ { h } \left( \boldsymbol { x } \right) = \boldsymbol { \mathcal { O } } ( h ^ { s + 1 } ) } \end{array}$ (observe that $q = s$ ). It then follows from (15.8) (for constant and variable $h$ ) that the global error behaves like $\mathcal { O } ( h ^ { s } )$ because $| R ( z ) | \le 1$ . For odd $s$ we have $R ( \infty ) = - 1$ and the global error estimate can be improved in the case of constant step sizes. This follows from partial summation

$$
\sum _ { p = 0 } ^ { n } \varrho ^ { n - \jmath } \delta ( x _ { \jmath } ) = { \frac { 1 - \varrho ^ { n + 1 } } { 1 - \varrho } } \delta ( x _ { 0 } ) + \sum _ { \jmath = 1 } ^ { n } { \frac { 1 - \varrho ^ { n + 1 - \jmath } } { 1 - \varrho } } \big ( \delta ( x _ { \jmath } ) - \delta ( x _ { \jmath - 1 } ) \big )
$$

of the sum in (15.9) and from the fact that $\delta _ { h } ( x _ { \jmath } ) - \delta _ { h } ( x _ { \jmath - 1 } ) = { \mathcal O } ( h ^ { q + 2 } ) .$

Radau IA. The local error estimate follows in the same way as for the Gauss methods. Since $R ( z ) = \mathcal { O } ( z ^ { - 1 } )$ the error propagation in (15.8) is negligible and the local and global errors have the same asymptotic behaviour.

Radau IIA and Lobatto IIIC. These methods have $a _ { s _ { 2 } } = b _ { \iota }$ for all $i$ . Therefore the last internal stage is identical to the numerical solution and the local error can be written as

$$
\delta _ { h } ( x ) = - e _ { s } ^ { T } ( I - z A ) ^ { - 1 } \Delta _ { h } ( x ) .
$$

Since $A$ is invertible this formula shows the presence of $z ^ { - 1 }$ in the local error. Again we have $R ( \infty ) = 0$ , so that the global error is essentially cqual to the local error.

Lobatto IIIA. The first stage is explicit, $g _ { 1 } = y _ { 0 }$ ,and is done without introducing an error. Therefore $\Delta _ { 1 , h } ( x ) = 0$ and (because of $a _ { s _ { 1 } } = b _ { _ { 2 } }$ ） the local error has the form

$$
\delta _ { h } ( x ) = - e _ { s - 1 } ^ { T } ( I - z \widetilde { A } ) ^ { - 1 } \widetilde { \Delta } _ { h } ( x )
$$

where $\stackrel { \sim } { A } = ( a _ { \iota \jmath } ) _ { \iota , \jmath = 2 } ^ { \mathfrak { s } }$ and $\widetilde { \Delta } _ { h } = ( \Delta _ { 2 , h } , \ldots , \Delta _ { s , h } ) ^ { T }$ . The statements of Table 15.1 now follow as for the Gauss methods.

Lobatto IB. The matrix $A$ is singular (its last column vanishes), therefore the two" $z ^ { \dprime }$ in (15.7) do not simply cancel for $z  \infty$ . A more detailed analysis (see Exercise 5 below） shows that the local error is not bounded if $z  \infty$ .Although $A$ -stable, these methods are not suited for the solution of stiff problems. □

We observe from Table 15.l that the order of convergence for problem (15.1) with large $\lambda$ is considerably smaller than the classical order. Further we see that methods satisfying $a _ { s _ { 2 } } = b _ { \ i }$ (Radau IIA, Lobatto IIIA and Lobatto IIIC) give an asymptotically exact result for $z  \infty$ ．Prothero & Robinson（1974） call such methods stiffly accurate. The importance of this condition will appear again when we treat singularly perturbed and differential-algebraic problems (Chapter VI).

# The Local Error

Das besondere Schmerzenskind sind die Fehlerabschatzungen.

(L. Collatz 1950)

Our next aim is to extend the above results to general nonlinear differential equations $y \prime = f ( x , y )$ satisfying a one-sided Lipschitz condition

$$
\langle f ( x , y ) - f ( x , z ) , y - z \rangle \leq \nu \| y - z \| ^ { 2 } .
$$

The following analysis,begun by Frank, Schneid & Ueberhuber (1981), was elaborated by Frank, Schneid & Ueberhuber (1985) and Dekker & Verwer (1984). We again denote the local error by

$$
\delta _ { h } ( x ) = y _ { 1 } - y ( x + h ) ,
$$

where $y _ { 1 }$ is the numerical solution with initial value $y _ { 0 } = y ( x )$ on the exact solution.

Proposition 15.1. Consider a differential equation which satisfies (15.11). Assume that the Runge-Kutta matrix $A$ is invertible, $\alpha _ { 0 } ( A ^ { - 1 } ) \geq 0$ (see Definition $I 4 . I )$ ， and that the stage order is $q$

$a \mathrm { , }$ 1f $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ then

$$
\| \delta _ { h } ( x ) \| \leq C h ^ { q + 1 } \operatorname* { m a x } _ { \xi \in [ x , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| \quad f o r \quad h \nu \leq \alpha < \alpha _ { 0 } ( A ^ { - 1 } ) .
$$

$b _ { . }$ ）If $\alpha _ { D } ( A ^ { - 1 } ) = 0$ for some positive diagonal matrix $D$ and $\nu < 0$ then

$$
\| \delta _ { h } ( x ) \| \leq C \Big ( h + \frac { 1 } { | \nu | } \Big ) h ^ { q } \operatorname* { m a x } _ { \xi \in [ x , x + h ] } \| y ^ { ( q + 1 ) } ( \xi ) \| .
$$

In both cases the constant $C$ depends only on the coefficients of the Runge-Kuta matrix and on $\alpha$ (for case $\left( a \right) .$ ）.

Remarks. a) The crucial fact in these estimates is that the right-hand side depends only on derivatives of the exact solution and not on the stiffness of the problem. These estimates are useful when a “smooth” solution of a stiff problem has to be approximated.

b) The hypothesis $\alpha _ { D } ( A ^ { - 1 } ) = 0$ (see case (b))is stronger than $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ (see Exercise 4 below). For the Lobatto IIIC methods,for which $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ $\mathit { \Pi } _ { s } ^ { ' } >$ 2), we have $\alpha _ { D } ( A ^ { - 1 } ) = 0$ with $D \approx B$ (see (14.21)). For stiffly accurate methods the estimate of part (b) can be improved by using (14.12) instead of (14.13).

c) In the estimates of the above proposition the maximum is taken over $\xi \in \mathbf { \Xi }$ $[ x , x + h ]$ . In the case where $0 \leq c _ { i } \leq 1$ is not satisfied, this interval must of course be correspondingly enlarged.

Proof. We put $\widehat { g } _ { \iota } = y \big ( x _ { 0 } + c _ { i } h \big )$ , so that the relation (14.11a) is satisfied with

$$
\delta _ { \imath } = y ( x _ { 0 } + c _ { \imath } h ) - y ( x _ { 0 } ) - h \sum _ { \jmath = 1 } ^ { s } a _ { \imath j } y ^ { \prime } ( x _ { 0 } + c _ { \jmath } h ) .
$$

Taylor expansion shows that

$$
\| \delta _ { i } \| \leq C _ { \iota } h ^ { q + 1 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { 1 } ] } \| y ^ { ( q + 1 ) } ( x ) \|
$$

where $\begin{array} { r } { C _ { \imath } = ( \vert c _ { \imath } \vert ^ { q + 1 } + ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } \vert a _ { \imath \jmath } \vert \cdot \vert c _ { \jmath } \vert ^ { q } ) / ( q + 1 ) ! } \end{array}$ is a method-dependent constant. Similarly, the value $\widehat { y } _ { 1 }$ of (14.11b) satisfies

$$
y ( x _ { 0 } + h ) - \widehat { y } _ { 1 } = y ( x _ { 0 } + h ) - y ( x _ { 0 } ) - h \sum _ { j = 1 } ^ { s } b _ { j } y ^ { j } ( x _ { 0 } + c _ { j } h ) = { \cal O } ( h ^ { q + 1 } ) ,
$$

because the order of the quadrature formula $\left( b _ { \imath } , c _ { i } \right) \mathrm { i } \mathrm { s } \geq q$ . Since

$$
\| \delta _ { h } ( x ) \| \leq \| y _ { 1 } - { \widehat { y } } _ { 1 } \| + \| { \widehat { y } } _ { 1 } - y ( x _ { 0 } + h ) \|
$$

the desired estimates follow from (14.13) of Theorem 14.3.

# Error Propagation

At the end of Sect.IV.12 we derived for some particular Runge-Kutta methods sharp estimates of the form

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \varphi _ { B } \big ( h \nu \big ) \| \widehat { y } _ { 0 } - y _ { 0 } \| ,
$$

where ${ \widehat { y } } _ { 1 } , y _ { 1 }$ are the numerical solutions corresponding to ${ \widehat { y } } _ { 0 } , y _ { 0 }$ ,respectively, and where the differential equation satisfies (15.11). We give here a simple proof of a crude estimate of $\varphi _ { B } ( h \nu )$ which, however, will be suficient to derive interesting convergence results.

Proposition 15.2 (Dekker & Verwer 1984). Suppose that the differential equation satisfies (15.11) and apply an algebraically stable Runge-Kutta method with invertible $A$ and $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ . Then for any $\alpha$ with $0 < \alpha < \alpha _ { 0 } \bigl ( A ^ { - 1 } \bigr )$ there exists $a$ constant $C > 0$ such that

$$
\| \widehat { y } _ { 1 } - y _ { 1 } \| \leq \big ( 1 + C h \nu \big ) \| \widehat { y } _ { 0 } - y _ { 0 } \| \qquad f o r \quad 0 \leq h \nu \leq \alpha .
$$

Proof. From (12.7) we have (using the notation of the proof of Theorem 12.4)

$$
\| \Delta y _ { 1 } \| ^ { 2 } = \| \Delta y _ { 0 } \| ^ { 2 } + 2 \sum _ { \iota = 1 } ^ { s } b _ { \iota } \langle \Delta f _ { \iota } , \Delta g _ { \iota } \rangle - \sum _ { \iota = 1 } ^ { s } \sum _ { \jmath = 1 } ^ { s } m _ { i \jmath } \langle \Delta f _ { \iota } , \Delta f _ { \jmath } \rangle .
$$

By algebraic stability the last term in (15.14) is non-positive and can be neglected. Using (15.11) and the estimate (14.12) with $\delta _ { i } = \widehat { y } _ { 0 } - y _ { 0 }$ we obtain

$$
\begin{array} { r l r } {  { 2 \sum _ { \imath = 1 } ^ { s } b _ { \imath } \langle \Delta f _ { \imath } , \Delta g _ { \imath } \rangle \le 2 h \nu \sum _ { \imath = 1 } ^ { s } b _ { \imath } \| \Delta g _ { \imath } \| ^ { 2 } } } \\ & { } & { \leq 2 h \nu C _ { 1 } \| \Delta g \| _ { D } ^ { 2 } \le \frac { 2 h \nu C _ { 2 } } { ( \alpha _ { D } ( A ^ { - 1 } ) - h \nu ) ^ { 2 } } \| \Delta y _ { 0 } \| ^ { 2 } . } \end{array}
$$

Inserting this into (15.14) yields

$$
\| \Delta y _ { 1 } \| \leq \left( 1 + \frac { h \nu C _ { 2 } } { ( \alpha _ { D } ( A ^ { - 1 } ) - h \nu ) ^ { 2 } } \right) \| \Delta y _ { 0 } \|
$$

which proves the desired estimate.

# $B$ -Convergence for Variable Step Sizes

We are now in a position to present the main result of this section.

Theorem 15.3. Consider an algebraically stable Runge-Kutta method with invertible $A$ and stage order $q \leq p$ and suppose that (15.11) holds. $a _ { \scriptscriptstyle \perp }$ If $0 < \alpha < \alpha _ { 0 } \bigl ( A ^ { - 1 } \bigr )$ and $\nu > 0$ then the global error satisfies

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q } \frac { \left( e ^ { C _ { 1 } \nu ( x _ { n } - x _ { 0 } ) } - 1 \right) } { C _ { 1 } \nu } C _ { 2 } \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| \quad f o r \quad h \nu \leq \alpha .
$$

$^ { b ) }$ 1f $\alpha _ { 0 } ( A ^ { - 1 } ) > 0$ and $\nu \leq 0$ then

$$
\Vert y _ { n } - y ( x _ { n } ) \Vert \leq h ^ { q } ( x _ { n } - x _ { 0 } ) C _ { 2 } \ \operatorname* { m a x } _ { x \in \{ x _ { 0 } , x _ { n } \} } \Vert y ^ { ( q + 1 ) } ( x ) \Vert \quad f o r a l l \quad h > 0 .
$$

$c ) I f \alpha _ { D } ( A ^ { - 1 } ) = 0$ for some positive diagonal matrix $D$ and $\nu < 0$ then

$$
\| y _ { n } - y ( x _ { n } ) \| \leq h ^ { q - 1 } C \Big ( h + \frac { 1 } { | \nu | } \Big ) ( x _ { n } - x _ { 0 } ) \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( q + 1 ) } ( x ) \| .
$$

The constants $C _ { 1 } , C _ { 2 } , C$ depend only on the coefficients of the Runge-Kutta matrix. In the case of variable step sizes, $h$ has to be interpreted as $h = \operatorname* { m a x } h _ { \ i }$

Proof. This convergence result is obtained in exactly the same way as that for nonstiff problems (Theorem I1.3.6). For the transported errors $E _ { \jmath }$ (see Fig. II.3.2) we have the estimate (for $\nu \geq 0$ ）

$$
\| E _ { \jmath } \| \leq e ^ { C \nu \left( x _ { n } - x _ { \jmath } \right) } \| \delta _ { h _ { \jmath - 1 } } ( x _ { \jmath - 1 } ) \|
$$

by Proposition 15.2, because $1 + C h \nu \leq e ^ { C \nu h }$ . We next insert the local error estimate of Proposition 15.1 into (15.15) and sum up the transported errors $E _ { \jmath }$ . This

yields the desired estimate for $\nu \geq 0$ because

$$
\begin{array} { r l } { \displaystyle \sum _ { \jmath = 1 } ^ { n } h _ { \jmath - 1 } e ^ { C \nu ( x _ { n } - x _ { \jmath } ) } \leq \int _ { x _ { 0 } } ^ { x _ { n } } e ^ { C \nu ( x _ { n } - x ) } d x } \\ { \displaystyle } & { \qquad = \left\{ \left( e ^ { C \nu ( x _ { n } - x _ { 0 } ) } - 1 ) / ( C \nu ) \right. \right. \left. \mathrm { f o r } \nu > 0 \right. } \\ { \displaystyle } & { \qquad \mathrm { f o r } \nu = 0 . } \end{array}
$$

f $\nu < 0$ we have $\| E _ { \jmath } \| \leq \| \delta _ { h _ { \jmath - 1 } } ( x _ { \jmath - 1 } ) \|$ by algebraic stability and the same arguments apply. □

Motivated by this result we define the order of $B$ -convergence as follows:

Definition 15.4 (Frank, Schneid & Ueberhuber 1981). A Runge-Kutta method is called $B$ -convergent of order $r$ for problems $y ^ { \prime } = f ( x , y )$ satisfying (15.11),if the global error admits an estimate

$$
\| y _ { n } - y ( x _ { n } ) \| \| \leq h ^ { r } \gamma ( x _ { n } - x _ { 0 } , \nu ) \operatorname* { m a x } _ { \substack { \jmath = 1 , \dots , l } } \operatorname* { m a x } _ { \substack { x \in [ x _ { 0 } , x _ { n } ] } } \| y ^ { ( \jmath ) } ( x ) \| \quad \mathrm { f o r } \quad h \nu \leq \alpha ,
$$

where $h = \operatorname* { m a x } h _ { \ i }$ .Here $\gamma$ is a method-dependent function and $\alpha$ also depends only on the coefficients of the method.

As an application of the above theorem we have

Theorem 15.5. The Gauss and Radau IIA methods are $B$ -convergent of order $s$ (number of stages). The Radau IA methods are $B$ -convergent of order $s - 1$ . The 2-stage Lobatto IIIC method is $B$ -convergent of order $l$ □

For the Lobatto IIC methods with $s \geq 3$ stages $\left( \alpha _ { 0 } ( A ^ { - 1 } ) = 0 \right.$ and $q = s - 1 \AA .$ ） Theorem 15.3 shows $B$ -convergence of order $s - 2$ if $\nu < 0$ . This is not an optimal result. Spijker (1986) proved $B$ -convergence of order $s - 3 / 2$ for $\nu < 0$ and constant step sizes. Schneid (1987) improved this result to $s - 1$ . Recently, Dekker, Kraaijevanger & Schneid (1991) showed that these methods are $B$ -convergent of order $s - 1$ for general step size sequences, if one allows the function $\gamma$ in Definition 15.4 to depend also on the ratio max $h _ { \imath } / \operatorname* { m i n } h _ { \imath }$

The Lobatto IIIA and IIB methods cannot be $B$ -convergent since they are not algebraically stable. This will be the content of the next subsection.

# $B$ -Convergence Implies Algebraic Stability

In order to find necessry conditions for $B$ -convergence we consider the problem

$$
y ^ { \prime } = \lambda ( x ) { \bigl ( } y - \varphi ( x ) { \bigr ) } + \varphi ^ { \prime } ( x ) , \qquad \operatorname { R e } \lambda ( x ) \leq \nu
$$

with exact solution $\varphi ( x ) = x ^ { q + 1 }$ . We apply a Runge-Kutta method with stage order $q$ and obtain for the global error $\varepsilon _ { n } = y _ { n } - \varphi ( x _ { n } )$ the simple recursion

$$
\varepsilon _ { n + 1 } = { \cal K } ( Z _ { n } ) \varepsilon _ { n } - { \cal L } ( Z _ { n } ) h ^ { q + 1 }
$$

(cf.Eq.(15.8) of the beginning of this section,where the case $\lambda ( x ) = \lambda$ was treated). Here $Z _ { n } = \mathrm { d i a g } \left( h \lambda ( x _ { n } + c _ { 1 } h ) , \ldots , h \lambda ( x _ { n } + c _ { s } h ) \right)$ and

$$
K ( Z ) = 1 + b ^ { T } Z ( I - A Z ) ^ { - 1 } \mathbb { 1 } , \quad L ( Z ) = d _ { 0 } + b ^ { T } Z ( I - A Z ) ^ { - 1 } d .
$$

The function $\bar { \cal K } ( Z )$ was already encountered in Definition 12.10, when treating $A N$ -stability. The vector $d = ( d _ { 1 } , \ldots , d _ { s } ) ^ { T }$ and $d _ { 0 }$ in $L ( Z )$ characterize the local error and are given by

$$
d _ { 0 } = 1 - ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } b _ { \jmath } c _ { \jmath } ^ { q } , \qquad d _ { \imath } = c _ { \imath } ^ { q + 1 } - ( q + 1 ) \sum _ { \jmath = 1 } ^ { s } a _ { \imath \jmath } c _ { \jmath } ^ { q } .
$$

Observe that by definition of the stage order we have either $d _ { 0 } \neq 0$ or $d \neq 0$ (or both). We are now in the position to prove

Theorem 15.6 (Dekker, Kraaijevanger & Schneid 1991). Consider a $D J$ -irreducible Runge-Kutta method which satisfies $0 \leq c _ { 1 } < c _ { 2 } < . . . < c _ { s } \leq 1 $ If,for some $r$ ， $l$ and $\nu < 0$ , the global error satisfies the $B$ -convergence estimate $( l 5 . l 6 )$ ,then the method is algebraically stable.

Proof. Suppose that the method is not algebraically stable. Then,by Theorem 12.13 and Lemma 15.17 below, there exists $Z = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right)$ with $\mathrm { R e } z _ { \jmath } < 0$ such that $( I - A Z ) ^ { - 1 }$ exists and

$$
| K ( Z ) | > 1 , \qquad L ( Z ) \ne 0 .
$$

We consider the interval $[ 0 , ( 1 + \theta ) / 2 ]$ and for even $N$ the step size sequence $( h _ { n } ) _ { n = 0 } ^ { N - 1 }$ given by

$$
h _ { n } = 1 / N \quad ( \mathrm { f o r } n \mathrm { e v e n } ) , \quad h _ { n } = \theta / N \quad ( \mathrm { f o r } n \mathrm { o d d } ) .
$$

If $N$ is sufficiently large it is possible to define a function $\lambda ( x )$ which satisfies $\operatorname { R e } \lambda ( x ) \leq \nu$ and

$$
\lambda ( x _ { n } + c _ { \iota } h _ { n } ) = { \left\{ \begin{array} { l l } { N z _ { \iota } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ e v e n } } } \\ { N z _ { s + 1 - \iota } } & { { \mathrm { f o r ~ } } n { \mathrm { ~ o d d } } . } \end{array} \right. }
$$

Because of (15.18) the global error $\varepsilon _ { n } = y _ { n } - \varphi ( x _ { n } )$ for the problem (15.17) sat-

isfies (with $h = 1 / N _ { \cdot }$ ）

$$
\begin{array} { l } { { \varepsilon _ { n + 1 } = K ( Z ) \varepsilon _ { n } - h ^ { q + 1 } L ( Z ) \quad \mathrm { f o r } n \mathrm { e v e n } } } \\ { { \varepsilon _ { n + 1 } = K ( \widetilde { Z } ) \varepsilon _ { n } - h ^ { q + 1 } L ( \widetilde { Z } ) \quad \mathrm { f o r } n \mathrm { o d d } } } \end{array}
$$

where $\widetilde { Z } = \operatorname { d i a g } \left( \theta z _ { s } , \dots , \theta z _ { 1 } \right)$ . Consequently we have

$$
\varepsilon _ { 2 m + 2 } = K ( \widetilde { Z } ) K ( Z ) \varepsilon _ { 2 m } - h ^ { q + 1 } ( K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) )
$$

and the error at $X = ( 1 + \theta ) / 2$ is given by

$$
\varepsilon _ { N } = - \frac { 1 } { N ^ { q + 1 } } \left( K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) \right) \frac { ( K ( \widetilde { Z } ) K ( Z ) ) ^ { N / 2 } - 1 } { K ( \widetilde { Z } ) K ( Z ) - 1 } .
$$

If $\theta$ is suficiently small, $K ( \widetilde { Z } ) \to 1$ and $L ( \widetilde { Z } ) \to d _ { 0 }$ , so that by (15.21)

$$
| K ( \widetilde { Z } ) K ( Z ) | > 1 \quad \mathrm { a n d } \quad K ( \widetilde { Z } ) L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) \ne 0 .
$$

Therefore $| \varepsilon _ { N } | \to \infty$ as $N \to \infty$ $N$ even), which contradicts the estimate (15.16) of $B$ -convergence.

To complete the above proof we give the following lemma:

Lemma 15.7 (Dekker, Kraaijevanger & Schneid 1990). Consider a $D J$ -irreducible Runge-Kutta method and suppose

$$
b ^ { T } Z ( I - A Z ) ^ { - 1 } d = 0
$$

for all $\boldsymbol { Z } = \operatorname { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right)$ with $I - A Z$ invertible; then $d = 0$

Proof. We define

$$
T = \big \{ j \big | b _ { i _ { 1 } } a _ { \iota _ { 1 } i _ { 2 } } a _ { i _ { 2 } i _ { 3 } } \cdot \cdot \cdot a _ { i _ { k - 1 } i _ { k } } = 0 \quad \mathrm { ~ f o r ~ a l l ~ } k \mathrm { ~ a n d ~ } i _ { l } \mathrm { ~ w i t h ~ } i _ { k } = j \big \} .
$$

Putting $k = 1$ we obtain $b _ { j } = 0$ for $j \in T$ . Further,if $i \not \in T$ and $j \in T$ there exists $( i _ { 1 } , \dots , i _ { k } )$ with $i _ { k } = i$ such that

$$
b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } \neq 0 , \quad b _ { \iota _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } a _ { i j } = 0
$$

implying $a _ { \scriptscriptstyle { \imath \jmath } } = 0$ . Therefore the method is $D J$ -reducible if $T \neq \emptyset$ . For the proof of the statement it thus suffices to show that $d \neq 0$ implies $T \neq \emptyset$ ·

Replacing $( I - A Z ) ^ { - 1 }$ by its geometric series, assumption (15.23) becomes equivalent to

$$
b ^ { T } Z ( A Z ) ^ { k - 1 } d = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } k { \mathrm { ~ a n d ~ } } Z = \operatorname { d i a g } { \big ( } z _ { 1 } , \ldots , z _ { s } { \big ) } .
$$

Comparing the coefficient of $z _ { i _ { 1 } } \cdots z _ { i _ { k } }$ gives

$$
\sum b _ { j _ { 1 } } a _ { j _ { 1 } j _ { 2 } } \cdot \cdot \cdot a _ { j _ { k - 1 } j _ { k } } d _ { j _ { k } } = 0 ,
$$

where the summation is over all permutations $( j _ { 1 } , \dots , j _ { k } )$ of $( i _ { 1 } , \dots , i _ { k } )$ Sup-pose now that $d _ { j } \neq 0$ for some index $j$ . We shall prove by induction on $k$ that

$$
b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k - 1 } i _ { k } } = 0 \quad { \mathrm { ~ f o r ~ a l l ~ } } \quad i _ { \ell } ( \ell = 1 , \dots , k ) \quad { \mathrm { w i t h } } \quad i _ { k } = j ,
$$

so that $j \in T$ and consequently $T \neq \emptyset$

For $k \simeq 1$ this follows immediately from (15.25)． In order to prove (15.26) for $k + 1$ we suppose, by contradiction, that $( i _ { 1 } , \dots , i _ { k + 1 } )$ with $i _ { k + 1 } = j$ exists such that $b _ { i _ { 1 } } a _ { i _ { 1 } i _ { 2 } } \dots a _ { i _ { k } i _ { k + 1 } } \ne 0$ .The relation (15.25)then implies the existence of apermutation(k+1)of (ik1)suchthatb ， too. We now denote by $q$ the smallest index for which $i _ { q } \neq j _ { q }$ .Then $i _ { q } = j _ { r }$ for some $r > q$ and

$$
b _ { i _ { 1 } } a _ { i _ { 1 } \ i _ { 2 } } \cdot \cdot \cdot a _ { i _ { q - 1 } i _ { q } } a _ { j _ { r } j _ { r + 1 } } \cdot \cdot \cdot a _ { j _ { k } j _ { k + 1 } } \neq 0
$$

contradicts the induction hypothesis, because the expression in (15.27) contains at most $k$ factors. □

# The Trapezoidal Rule

The trapezoidal rule

$$
y _ { k + 1 } = y _ { k } + { \frac { h _ { k } } { 2 } } { \Big ( } f { \big ( } x _ { k } , y _ { k } { \big ) } + f { \big ( } x _ { k + 1 } , y _ { k + 1 } { \big ) } { \Big ) }
$$

is not algebraically stable. Therefore (Theorem 15.6) it cannot be $B$ -convergent in the sense of Definition 15.4. Nevertheless it is possible to derive estimates (15.16), if we restrict ourselves to special step size sequences (constant, monotonic,...). This was first proved by Stetter (unpublished) and investigated in detail by Kraai-jevanger (1985). The result is

Theorem 15.8 (Kraaijevanger 1985). If the differential equation satisfies (15.11), then the global error of the trapezoidal rule permits for $h _ { j } \nu \leq \alpha < 2$ the estimate

$$
\Vert y _ { n } - y ( x _ { n } ) \Vert \leq C \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \Vert y ^ { ( 3 ) } ( x ) \Vert \sum _ { k = 0 } ^ { n - 1 } \Big ( \prod _ { \substack { j = k + 1 } } ^ { n - 1 } \operatorname* { m a x } \left( 1 , h _ { j } / h _ { j - 1 } \right) \Big ) h _ { k } ^ { 3 } .
$$

Proof. We denote by ${ \widehat { y } } _ { k } = y ( x _ { k } )$ the exact solution at the grid points. From the Taylor expansion we then get

$$
\widehat { y } _ { k + 1 } = \widehat { y } _ { k } + \frac { h _ { k } } { 2 } \Big ( f \big ( x _ { k } , \widehat { y } _ { k } \big ) + f \big ( x _ { k + 1 } , \widehat { y } _ { k + 1 } \big ) \Big ) + \delta _ { k }
$$

where

$$
\| \delta _ { k } \| \leq \frac { 1 } { 1 2 } h _ { k } ^ { 3 } \operatorname* { m a x } _ { x \in [ x _ { k } , x _ { k + 1 } ] } \| y ^ { ( 3 ) } ( x ) \| .
$$

The main idea is now to introduce the intermediate values

$$
\begin{array} { l } { { y _ { k + 1 / 2 } = y _ { k } + \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k } , y _ { k } ) = y _ { k + 1 } - \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k + 1 } , y _ { k + 1 } ) } } \\ { { \widehat { y } _ { k + 1 / 2 } = \widehat { y } _ { k } + \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k } , \widehat { y } _ { k } ) + \delta _ { k } = \widehat { y } _ { k + 1 } - \displaystyle \frac { h _ { k } } { 2 } f ( x _ { k + 1 } , \widehat { y } _ { k + 1 } ) . } } \end{array}
$$

The transition yk-1/2 → Yk+1/2

$$
y _ { k + 1 / 2 } = y _ { k - 1 / 2 } + { \frac { 1 } { 2 } } { ( h _ { k - 1 } + h _ { k } ) f ( x _ { k } , y _ { k } ) }
$$

can then be interpreted as one step of the $\theta$ -method

$$
y _ { m + 1 } = y _ { m } + h f \bigl ( x _ { m } + \theta h , y _ { m } + \theta ( y _ { m + 1 } - y _ { m } ) \bigr )
$$

with $\theta = h _ { \boldsymbol k - 1 } / ( h _ { \boldsymbol k - 1 } + h _ { \boldsymbol k } )$ and step size $h = ( h _ { k - 1 } + h _ { k } ) / 2$ . A similar calculation shows that the same $\theta$ -method maps $\widehat { y } _ { k - 1 / 2 }$ t0 $\widehat { y } _ { k + 1 / 2 } - \delta _ { k }$ . Therefore we have

$$
\begin{array} { r } { \| \widehat { y } _ { k + 1 / 2 } - y _ { k + 1 / 2 } - \delta _ { k } \| \leq \varphi _ { B } ( h \nu ) \ \| \widehat { y } _ { k - 1 / 2 } - y _ { k - 1 / 2 } \| , } \end{array}
$$

where the growth function $\varphi _ { B } ( h \nu )$ is given by (see Eqs.(12.42) and (11.13))

$$
\begin{array} { l } { \displaystyle \varphi _ { B } \big ( h \nu \big ) = \operatorname* { m a x } \bigl \{ \big ( 1 - \theta \big ) / \theta , \big ( 1 + ( 1 - \theta ) h \nu \big ) / \big ( 1 - \theta h \nu \big ) \bigr \} } \\ { \displaystyle = \operatorname* { m a x } \bigl \{ h _ { k } / h _ { k - 1 } , \big ( 1 + \frac 1 2 h _ { k } \nu \big ) / \big ( 1 - \frac 1 2 h _ { k - 1 } \nu \big ) \bigr \} = : \varphi _ { k } . } \end{array}
$$

By the triangle inequality we also get

$$
\begin{array} { r } { \| \widehat { y } _ { k + 1 / 2 } - y _ { k + 1 / 2 } \| \leq \varphi _ { k } \| \widehat { y } _ { k - 1 / 2 } - y _ { k - 1 / 2 } \| + \| \delta _ { k } \| . } \end{array}
$$

Further it follows from(15.31) with $k = 0$ and from $\widehat { y } _ { 0 } = y _ { 0 }$ that

$$
\| \widehat { y } _ { 1 / 2 } - y _ { 1 / 2 } \| = \| \delta _ { 0 } \| ,
$$

whereas the backward Euler steps $y _ { n - 1 / 2 } \to y _ { n }$ and $\widehat { y } _ { n - 1 / 2 } \to \widehat { y } _ { n }$ (see ( imply

$$
\Vert \widehat { y } _ { n } - y _ { n } \Vert \leq \frac { 1 } { \left( 1 - \frac { 1 } { 2 } h _ { n - 1 } \nu \right) } \Vert \widehat { y } _ { n - 1 / 2 } - y _ { n - 1 / 2 } \Vert
$$

again by Example 12.24 with $\theta = 1$ . A combination of (15.33), (15.34) and (15.35) yields

$$
\left\| \widehat { y } _ { n } - y _ { n } \right\| \leq \frac { 1 } { \left( 1 - \frac { 1 } { 2 } h _ { n - 1 } \nu \right) } \sum _ { k = 0 } ^ { n - 1 } \Big ( \prod _ { \substack { \jmath = k + 1 } } ^ { n - 1 } \varphi _ { \jmath } \Big ) \| \delta _ { k } \| .
$$

For $\nu \leq 0$ we have $\varphi _ { k } \leq \operatorname* { m a x } ( 1 , h _ { k } / h _ { k - 1 } )$ and the statement follows if we insert (15.30) into (15.36). For $\nu \geq 0$ we use the estimate $\left( h _ { k - 1 } \nu \leq 1 \right)$

$$
\frac { 1 + \frac 1 2 h _ { k } \nu } { 1 - \frac 1 2 h _ { k - 1 } \nu } = \frac { 1 + \frac 1 2 h _ { k - 1 } \nu } { 1 - \frac 1 2 h _ { k - 1 } \nu } \cdot \frac { 1 + \frac 1 2 h _ { k } \nu } { 1 + \frac 1 2 h _ { k - 1 } \nu } \le e ^ { 2 h _ { k - 1 } \nu } \cdot \operatorname* { m a x } \Bigl ( 1 , \frac { h _ { k } } { h _ { k - 1 } } \Bigr )
$$

so that the statement holds with $C = e ^ { 2 \nu ( x _ { n } - x _ { 0 } ) } / 1 2$

Crla $\left( h _ { k } \right) _ { k = 0 } ^ { N - 1 }$ is constant or monotonic,then for $h = \operatorname* { m a x } h _ { i }$

$$
\| y _ { n } - y ( x _ { n } ) \| \leq C \operatorname* { m a x } _ { x \in [ x _ { 0 } , x _ { n } ] } \| y ^ { ( 3 ) } ( x ) \| \cdot h ^ { 2 } .
$$

# Order Reduction for Rosenbrock Methods

Obviously, Rosenbrock methods (Definition 7.1） cannot be $B$ -convergent in the sense of Definition 15.4 (see also Exercise 7 of Sect.IV.12). Nevertheless it is interesting to study their behaviour on stiff problems such as the Prothero & Robinson model (15.1). Since this equation is non-autonomous we have to use the formulation (7.4a). A straightforward calculation shows that the global error $\varepsilon _ { n } =$ $y _ { n } - \varphi ( x _ { n } )$ satisfies the recursion

$$
\varepsilon _ { n + 1 } = R ( z ) \varepsilon _ { n } + \delta _ { h } ( x _ { n } )
$$

where $R ( z )$ is the stability function (7.14)and the local error is given by

$$
\delta _ { h } ( x ) = \varphi ( x ) - \varphi ( x + h ) + b ^ { T } ( I - z B ) ^ { - 1 } \Delta
$$

with $B = ( \alpha _ { i j } + \gamma _ { \imath \jmath } ) , b = ( b _ { 1 } , \ldots , b _ { s } ) ^ { T } , \Delta = ( \Delta _ { 1 } , \ldots , \Delta _ { s } ) ^ { T }$ and

$$
\Delta _ { i } = z ( \varphi ( x ) - \varphi ( x + \alpha _ { \iota } h ) - \gamma _ { i } h \varphi ^ { \prime } ( x ) ) + h \varphi ^ { \prime } ( x + \alpha _ { i } h ) + \gamma _ { \iota } h ^ { 2 } \varphi ^ { \prime \prime } ( x ) .
$$

Taylor expansion gives the following result.

Lemma 15.10. The local error $\delta _ { h } ( x )$ of a Rosenbrock method applied to (15.1) satisfies for $h  0$ and $z = \lambda h  \infty$

$$
\delta _ { h } ( x ) = \Bigl ( \sum _ { i , j } b _ { i } \omega _ { i j } \alpha _ { j } ^ { 2 } - 1 \Bigr ) \frac { h ^ { 2 } } { 2 } \varphi ^ { \prime \prime } ( x ) + \mathcal { O } \bigl ( h ^ { 3 } \bigr ) + \mathcal { O } \Bigl ( \frac { h ^ { 2 } } { z } \Bigr ) ,
$$

where $\omega _ { \imath \jmath }$ are the entries of $B ^ { - 1 }$ ·

Remarks. a) Unless the Rosenbrock method satisfies the new order condition

$$
\sum _ { i , j = 1 } ^ { s } b _ { i } \omega _ { i j } \alpha _ { j } ^ { 2 } = 1 ,
$$

the local error and the global error (if $| R ( \infty ) | < 1 )$ are of size $\mathcal { O } ( h ^ { 2 } )$ . Since none of the classical Rosenbrock methods of Sect.IV.7 satisfies (15.39), their order of convergence is only 2 for the problem (15.1) if $\lambda$ is very large.

b) A convenient way to satisfy (15.39) is to require

$$
\alpha _ { s i } + \gamma _ { s i } = b _ { i } ( i = 1 , \ldots , s ) \quad \mathrm { a n d } \quad \alpha _ { s } = 1 .
$$

This is the analogue of the condition $a _ { s _ { 1 } } = b _ { \ i }$ for Runge-Kutta methods. It implies not only (15.39) but even

$$
\begin{array} { r } { \delta _ { h } ( x ) = \mathcal { O } \Big ( \frac { h ^ { 2 } } { z } \Big ) , } \end{array}
$$

so that such methods yield asymptotically exact results for $z  \infty$

c) A deeper understanding of Eq.(15.39) will be possible when studying the error of Rosenbrock methods for singular perturbation and differential-algebraic problems (Chapter VI). We shall construct there methods satisfying (15.40).

d) Scholz (1989) writes the local error $\delta _ { h } \{ x \}$ in the form

$$
\delta _ { \hbar } ( x ) = \sum _ { j \geq 2 } C _ { j } ( z ) \hbar ^ { j } \varphi ^ { ( j ) } ( x )
$$

and investigates the possibility of having $C _ { \ j } ( \ j z ) \equiv 0$ for $j = 2$ (and also $j > 2$ ). Hundsdorfer (1986) and Strehmel & Weiner(1987) extend the above analysis to semi-linear problems (11.21) which satisfy (11.22). Their results are rather technical but allow the construction of “ $B$ -convergent" methods of order $p > 1$ ·

# Exercises

1. Prove that the stage order of an SDIRK method is at most 1, that of a DIRK method at most 2.

2. Consider a Runge-Kuta method with $0 \leq c _ { 1 } < . . . < c _ { s } \leq 1$ which has stage order $q$ ． Prove that the method cannot be $B$ -convergent (for variable step sizes) of order $q + 1$

Hint. Use Formula (15.22) and prove that

$$
\frac { I \tilde { \mathcal { ( Z ) } } L ( Z ) + \theta ^ { q + 1 } L ( \widetilde { Z } ) } { I \tilde { \mathcal { ( Z ) } } I \tilde { \mathcal { ( Z ) } } - 1 }
$$

cannot be uniformly bounded for

$$
Z = \mathrm { d i a g } \left( z _ { 1 } , \dots , z _ { s } \right) , \qquad { \widetilde { Z } } = \mathrm { d i a g } \left( { \widetilde { z } } _ { 1 } , \dots , { \widetilde { z } } _ { s } \right)
$$

with $\mathrm { R e } z _ { \imath } \leq 0 , \mathrm { R e } \tilde { z } _ { \imath } \leq 0$ (in the case ${ { c } _ { 1 } } = 0$ and $c _ { s } = 1$ one has to prove this under the restriction $\hat { z } _ { 1 } = \theta z _ { s }$ ， $\tilde { z } _ { s } \simeq \theta z _ { 1 }$ ). For this consider valucs $\tilde { \mathbf { \Xi } } _ { \tilde { \mathbf { \Lambda } } _ { 1 } } , \ \widetilde { \boldsymbol { z } } _ { 1 }$ close to the origin.

3.(Burrage & Hundsdorfer 1987).Assume $c _ { i } \sim c _ { j }$ is not an integer for $1 \leq i <$ $\jmath \leq s$ ,and the order of $B$ -convergence (for constant step sizes) of a Runge-Kutta method is $q + 1$ （ $q$ denotes the stage order). Then $d _ { 0 } = 0$ and all components of $\boldsymbol { d } = ( d _ { 1 } , \ldots , d _ { s } ) ^ { T }$ are equal (see (15.20) for the definition of $d _ { j }$ ).

Hint. Study the uniform boundedness of the function $L ( Z ) / ( K ( Z ) - 1 )$

4. (Kraaijevanger). Show that for

$$
A ^ { - 1 } = { \left( \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } \end{array} \right) }
$$

we have $\alpha _ { 0 } ( A ^ { - 1 } ) = 0$ , but there exists no positive diagonal matrix $D$ such that $\alpha _ { D } ( A ^ { - 1 } ) = 0$ . For more insight see “Corollary $2 . 1 5 ^ { \circ }$ of Kraaijevanger & Schneid (1991).

5. Prove that for the Lobatto IIIB methods, with

$$
A = \left( \begin{array} { l l } { \widetilde { A } } & { 0 } \\ { a ^ { T } } & { 0 } \end{array} \right)
$$

the dominant term of the local error (15.7) is (for $h \to 0$ and $z = h \lambda \to \infty$ ）

$$
z b _ { s } ( a ^ { T } \widetilde { A } ^ { - 1 } c ^ { q + 1 } - 1 ) \frac { h ^ { q + 1 } } { ( q + 1 ) ! } \varphi ^ { ( q + 1 ) } ( x ) .
$$

Here $q = s - 2$ is the stage order and $\boldsymbol { c } = ( c _ { 1 } , \dots , c _ { s - 1 } ) ^ { T }$ . Show further that

$$
\begin{array} { r l r l } & { { } a ^ { T } \widetilde { A } ^ { - 1 } c ^ { k } = 1 } & { } & { { } \mathrm { f o r } \quad k = 1 , 2 , \ldots , q } \\ & { { } a ^ { T } \widetilde { A } ^ { - 1 } c ^ { k } \neq 1 } & { } & { { } \mathrm { f o r } \quad k = q + 1 . } \end{array}
$$

Hint. Equation (15.44) follows from $C ( q )$ . Show (15.45) by supposing that $a ^ { T } \tilde { A } ^ { - 1 } c ^ { q + 1 } = 1$ which together with (15.44) implies that

$$
\sum _ { \ i = 1 } ^ { s - 1 } d _ { \ i } p ( c _ { \ i } ) = p ( 1 ) \qquad \mathrm { w h e r e } \quad d ^ { T } = a ^ { T } \widetilde { A } ^ { - 1 }
$$

for every polynomial of $\deg p \leq q + 1 = s - 1$ satisfying $p ( 0 ) = 0$ . Arrive at a contradiction with

$$
p ( x ) = ( x - c _ { 1 } ) ( x - c _ { 2 } ) \cdot \ldots \cdot ( x - c _ { s - 1 } ) .
$$
