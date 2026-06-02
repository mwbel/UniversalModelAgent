The flow map of (10.10) is symplectic and hence area preserving. It can be shown using normal form theory [7, 8] that this implies that the ratio $A ( t ) / A ( 0 )$ remains equal to one along the flow of (10.10) up to order $\mathcal { O } ( \varepsilon )$ terms. These small perturbation terms are due to the fact that the rapidly rotating solutions do not exactly form closed loops.

The scaled quantity

$$
J : = \frac { A } { 2 \pi }
$$

is equivalent to the action variable in the standard transformation from $( x , p _ { x } )$ to action-angle variables $( J , \phi )$ . Hence the action $J$ is a “near-invariant” of (10.10) for $\varepsilon$ sufficiently small and is called an adiabatic invariant [7, 8]. See also Section 5.2.3 in Chapter 5.

Let us discuss the precise form of $J$ for (10.7) and (10.8). Assuming a fixed length $L$ , the Hamiltonian (10.7) describes harmonic oscillations of frequency $\omega = \varepsilon ^ { - 1 }$ and the solutions are given by

$$
x ( t ) = R \sin ( \phi ( t ) ) + L , \qquad p _ { x } ( t ) = R \cos ( \phi ( t ) ) ,
$$

where $\phi ^ { \prime } ( t ) = \varepsilon ^ { - 1 }$ and $R$ is a constant of integration determined by the initial conditions. The area of the circle described by $( x ( t ) , p _ { x } ( t ) )$ is given by $A = \pi R ^ { 2 }$ . On the other hand, we have $H _ { \mathsf { f } } = R ^ { 2 } / ( 2 \varepsilon )$ and, hence, the associated adiabatic invariant is given by

$$
J = \varepsilon H _ { \mathrm { f } } = \frac { 1 } { 2 } \left[ p _ { x } ^ { 2 } + ( x - L ( \pmb q ) ^ { 2 } ) \right] .
$$

In a similar manner, we obtain

$$
J = \frac { \varepsilon } { \sqrt { K ( \pmb q ) } } H _ { \mathrm { f } } = \frac { 1 } { 2 \sqrt { K ( \pmb q ) } } \left[ p _ { x } ^ { 2 } + K ( \pmb q ) x ^ { 2 } \right]
$$

as the adiabatic invariant for the Hamiltonian (10.8). Indeed, for fixed $K = K ( \pmb q )$ , solutions of (10.8) are of the form

$$
x ( t ) = \frac { R } { K ^ { 1 / 4 } } \sin ( \phi ( t ) ) , \qquad p _ { x } ( t ) = R K ^ { 1 / 4 } \cos ( \phi ( t ) ) ,
$$

where $\phi ^ { \prime } ( t ) = \omega = \varepsilon ^ { - 1 } \sqrt { K }$ and $R$ is again arbitrary. The area of the ellipse followed by $( x ( t ) , p _ { x } ( t ) )$ is given by $A = \pi R ^ { 2 }$ and the energy by $H _ { \mathrm { f } } = K ^ { 1 / 2 } R ^ { 2 } / ( 2 \varepsilon )$ . Hence, we obtain $\mathcal { I }$ as given above. In both cases, the equality

$$
H _ { \mathrm { f } } = \omega J
$$

holds, where $\omega$ is the frequency of the rapidly rotating motion.

# 10.1.4 The effect of numerical resonances

Let us now return to the LTS methods. Composition methods have been considered before in this book. However, the method (10.5) is different from those composition methods since the map $\psi _ { \Delta t }$ is not close to the identity. Hence, although (10.5) generates a symplectic map, long time energy conservation cannot be concluded from backward error analysis. Sharp increases in energy are indeed observed for particular values of $\Delta t$ and these are associated with numerically induced resonances as briefly discussed in Section 10.1.1 for single frequency systems. To explore this issue in more detail in the context of slow–fast systems, we discuss two simple model problems.

# A linear model problem

Consider a linear system with Hamiltonian

$$
H = \frac { 1 } { 2 } \left[ p ^ { 2 } + q ^ { 2 } \right] + \frac { 1 } { 2 \varepsilon } \left[ p _ { x } ^ { 2 } + ( x - q ) ^ { 2 } \right] .
$$

The associated equations of motion are

$$
\begin{array} { r } { \left[ \begin{array} { c } { \dot { q } } \\ { \dot { p } } \\ { \dot { x } } \\ { \dot { p } _ { x } } \end{array} \right] = \left[ \begin{array} { c c c c } { 0 } & { 1 } & { 0 } & { 0 } \\ { - 1 - \varepsilon ^ { - 1 } } & { 0 } & { \varepsilon ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \varepsilon ^ { - 1 } } \\ { \varepsilon ^ { - 1 } } & { 0 } & { - \varepsilon ^ { - 1 } } & { 0 } \end{array} \right] \left[ \begin{array} { c } { q } \\ { p } \\ { x } \\ { p _ { x } } \end{array} \right] . } \end{array}
$$

These equations can, of course, be solved analytically. This is also true for the fast and slow subsystems and we can implement an LTS method in the form

$$
\boldsymbol { M } _ { \Delta t } = e ^ { \Delta t / 2 B } \cdot e ^ { \Delta t \boldsymbol { A } } \cdot e ^ { \Delta t / 2 B } ,
$$

where

$$
\pmb { A } = \left[ \begin{array} { c c c c } { 0 } & { 0 } & { 0 } & { 0 } \\ { - \varepsilon ^ { - 1 } } & { 0 } & { \varepsilon ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \varepsilon ^ { - 1 } } \\ { \varepsilon ^ { - 1 } } & { 0 } & { - \varepsilon ^ { - 1 } } & { 0 } \end{array} \right] , \qquad \pmb { B } = \left[ \begin{array} { c c c c } { 0 } & { 1 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] .
$$

The eigenvalues of the exact solution operator

$$
W _ { \Delta t } = e ^ { \Delta t ( A + B ) }
$$

are all on the unit circle. For the numerical approximation ${ M } _ { \Delta t }$ to be stable, we have to require that all its eigenvalues be on the unit circle as well. To check this property, we define

$$
\Lambda ( \Delta t ) = \operatorname* { m a x } _ { i = 1 , \ldots , 4 } | \lambda _ { i } ( \Delta t ) | ,
$$

![](images/4381771235529c906aacde64cf0b95fd1444cef029fef7e4a0a487cdcae18343.jpg)  
Figure 10.2 Stability of LTS method as a function of $\Delta t / \varepsilon$ .

where $\lambda _ { j } ( \Delta t )$ , $i = 1 , \dots , 4$ , are the eigenvalues of ${ M } _ { \Delta t }$ . The linear stability boundary for the St¨ormer–Verlet method is $\omega \Delta t \leq 2$ , where $\omega$ is the highest frequency in the system. Here we have $\omega \approx \varepsilon ^ { - 1 }$ and it can be seen from Fig. 10.2 that the LTS method becomes unstable for the first time at about $\Delta t { } \omega _ { } \approx { } \pi$ . Of course, if one excludes the domains of instability by a proper choice of $\Delta t$ , then a much larger timestep could be used in principle. One can also see from Fig. 10.2 that the domains of instability shrink for smaller values of $\varepsilon$ . The precise motion of all four eigenvalues $\lambda _ { j }$ as a function of $\Delta t / \varepsilon$ , $\varepsilon = 1 / 4 0$ , can be found in Fig. 10.3. Note that the eigenvalues leave the unit circle near fast–fast or fast– slow eigenvalue crossings (resonances) which implies an exponential instability of the method.

# A nonlinear model problem

We take a Hamiltonian of type (10.8) with $K ( q ) = 1 + \alpha q ^ { 2 }$ , $\alpha = 0 . 1$ ; i.e.

$$
H = \frac { 1 } { 2 } \left[ p ^ { 2 } + q ^ { 2 } \right] + \frac { 1 } { 2 \varepsilon } \left[ p _ { x } ^ { 2 } + ( 1 + \alpha q ^ { 2 } ) x ^ { 2 } \right] .
$$

![](images/d23e05afdd3f428b016bf8e024cf2494658c6205b691c78a58cd1982cfd66ebe.jpg)  
Figure 10.3 Eigenvalues of LTS propagator as a function of $\Delta t / \varepsilon$ , $\varepsilon = 1 / 4 0$ .

The equations of motion for the fast subsystem

$$
\dot { x } = \varepsilon ^ { - 1 } p _ { x } , \quad \dot { p } _ { x } = - \varepsilon ^ { - 1 } ( 1 + \alpha q ^ { 2 } ) x , \quad \dot { q } = 0 , \quad \dot { p } = - \frac { \alpha } { \varepsilon } x ^ { 2 } q
$$

can be solved analytically. The frequency of the fast motion is

$$
\omega = \varepsilon ^ { - 1 } \sqrt { 1 + \alpha q ^ { 2 } } ,
$$

and the solution in $( x , p _ { x } )$ (for frozen $q$ ) is given by

$$
\begin{array} { l } { { \displaystyle x ( t ) = x ( 0 ) \cos ( \omega t ) + \frac { p _ { x } ( 0 ) } { \sqrt { 1 + \alpha q ^ { 2 } } } \sin ( \omega t ) } , } \\ { { \displaystyle p _ { x } ( t ) = p _ { x } ( 0 ) \cos ( \omega t ) - x ( 0 ) \sqrt { 1 + \alpha q ^ { 2 } } \sin ( \omega t ) } . } \end{array}
$$

The update for the momentum $p$ becomes

$$
\begin{array} { l } { { \displaystyle p ( t ) = p ( 0 ) - \frac { \alpha q ( 0 ) } { \sqrt { 1 + \alpha q ( 0 ) ^ { 2 } } } \left[ \frac { x ( 0 ) ^ { 2 } } { 2 } \left( \omega t + \cos ( \omega t ) \sin ( \omega t ) \right) + \right. } } \\ { { \displaystyle \left. + \frac { p _ { x } ( 0 ) ^ { 2 } } { 2 ( 1 + \alpha q ( 0 ) ^ { 2 } ) } \left( \omega t - \cos ( \omega t ) \sin ( \omega t ) \right) + \frac { x ( 0 ) p _ { x } ( 0 ) } { \sqrt { 1 + \alpha q ( 0 ) ^ { 2 } } } \sin ^ { 2 } ( \omega t ) \right] } } \end{array}
$$

We denote the associated flow map by $\pmb { \phi } _ { \Delta t , H _ { f } }$ . The timestepping method is given by

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t / 2 , H _ { \mathrm { s } } } \circ \pmb { \phi } _ { \Delta t , H _ { \mathrm { f } } } \circ \pmb { \phi } _ { \Delta t / 2 , H _ { \mathrm { s } } } ,
$$

where $\pmb { \phi } _ { t , H _ { \mathrm { s } } }$ is the solution operator for the (slow) harmonic oscillator

$$
\dot { q } = p , \qquad \dot { p } = - q .
$$

We set $\varepsilon = 0 . 0 2 5$ , $q ( 0 ) = x ( 0 ) = 0$ , $p ( 0 ) = 1$ , $p _ { x } ( 0 ) = 2 \varepsilon ^ { 1 / 2 }$ , and integrated the equations of motion over a time interval of $t \in [ 0 , 2 0 0 ]$ for stepsizes $\Delta t$ in the range of $\varepsilon ^ { - 1 } \Delta t \in [ 1 , 1 0 ]$ . In Fig. 10.4, we plot

$$
\Delta E _ { \mathrm { m a x } } = \operatorname* { m a x } _ { t \in [ 0 , 2 0 0 ] } \frac { | H ( t ) - H ( 0 ) | } { H ( 0 ) } , \quad \Delta J _ { \mathrm { m a x } } = \operatorname* { m a x } _ { t \in [ 0 , 2 0 0 ] } \frac { | J ( t ) - J ( 0 ) | } { J ( 0 ) }
$$

as a function of the scaled stepsize $\Delta t / \varepsilon$ . Significantly increased errors in energy and adiabatic invariant are clearly visible in the vicinity of $\Delta t / \varepsilon = k \pi$ , $k = 1 , 2 , 3$ . However, since we observe exactly the same energy behavior for a simulation over the longer time interval $t \in [ 0 , 8 0 0 ]$ , the increased errors are not linked to an instability of the method. This is in contrast to the linear test problem (10.12), where exponential instabilities occurred near $\Delta t / \varepsilon = k \pi$ , $k = 1 , 2 , \ldots .$ . The somewhat favorable behavior of nonlinear over linear problems is observed quite often in practice and can be traced back to the fact that the frequency (10.15) of the fast system is not constant but varies in time as a function of $q ( t )$ .

![](images/f2611859cdb02cab1e5ff5a097f1185d5183a35a6ef4e8b8a5f6de82de3f0468.jpg)  
Figure 10.4 Maximum relative errors in total energy and adiabatic invariant as a function of $\Delta t / \varepsilon$ , $\varepsilon = 1 / 4 0$ , for LTS method.

# 10.2 Averaging and reduced equations

We have seen in Section 10.1.3 that the highly oscillatory motion in a single fast degree of freedom gives rise to the existence of an adiabatic invariant $\mathcal { I }$ . We will now use this adiabatic invariant to discuss the effect of the fast motion in $\left( x , p _ { x } \right)$ on the slow degrees of freedom $( \pmb q , \pmb p )$ . The relevant equations of motion in the variable $( \pmb q , \pmb p )$ are

$$
\dot { \boldsymbol { q } } = \boldsymbol { M } ^ { - 1 } \boldsymbol { p } , \qquad \dot { \boldsymbol { p } } = - \nabla _ { \boldsymbol { q } } \boldsymbol { V } ( \boldsymbol { q } ) - \varepsilon ^ { - 1 } \nabla _ { \boldsymbol { q } } \boldsymbol { V } _ { \mathrm { f } } ( \boldsymbol { x } ( t ) , \boldsymbol { q } ) ,
$$

where $x ( t )$ is now assumed to be a given function of time. In fact, we can deduce from the previous discussions that $x ( t )$ has to be of the form

$$
x ( t ) \approx \sqrt { \frac { 2 J } { \varepsilon \omega } } \sin ( \phi ( t ) ) + b ( \pmb { q } ) ,
$$

with $\phi ^ { \prime } ( t ) = \omega$ and $\omega = \omega ( q ( t ) )$ is the instantaneous frequency of the fast oscillations. For example, consider the Hamiltonian (10.7), then $\omega = \varepsilon ^ { - 1 }$ and $b ( \pmb q ) = L ( \pmb q )$ . On the other hand, we obtain $\omega = \varepsilon ^ { - 1 } \sqrt { K ( \pmb q ) }$ and $b ( \pmb q ) = 0$ for the system (10.8). Recall that the action $J$ is an adiabatic invariant. In accordance with this, we may set $J = { \mathsf { c o n s t } }$ .

Let us now sketch the basic idea of averaging. See [197, 7, 8] for more details. Assume we are given a second-order time-dependent differential equation

$$
\ddot { y } = f ( y , \phi ( t ) ) ,
$$

where $\phi ( t )$ is a given function such that $\phi ^ { \prime } ( t ) = \omega ( t ) \gg 1$ and $f ( y , \tau )$ is $2 \pi -$ periodic in $\tau$ . One can think of these equations as a mechanical system driven by a highly oscillatory time-dependent excitation of instantaneous frequency $\omega$ . Let us assume that $\omega ( t ) \geq \varepsilon ^ { - 1 }$ and $\omega ( t )$ is slowly varying in time, then the motion in the variable $y$ is characterized by the averaged equations

$$
\ddot { y } = \bar { f } ( y ) , \qquad \bar { f } ( y ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } f ( y , \tau ) d \tau ,
$$

over time intervals of order one up to an approximation error of $\mathcal { O } ( \varepsilon )$ [197, 7, 8]. Let us apply this result to the system (10.16). We assume that $\omega ( q ) \geq \varepsilon ^ { - 1 }$ and obtain the averaged equations

$$
\dot { \pmb q } = { \pmb M } ^ { - 1 } { \pmb p } , \qquad \dot { \pmb p } = - \nabla _ { \pmb q } V ( \pmb q ) + \bar { \cal F } _ { \mathrm { f } } ( \pmb q ) ,
$$

where

$$
\bar { F } _ { \mathrm { f } } = - \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \varepsilon ^ { - 1 } \nabla _ { q } V _ { \mathrm { f } } \left( \sqrt { \frac { 2 J } { \omega } } \sin ( \tau ) + b ( q ) , q \right) d \tau .
$$

Once the averaged force $\bar { F } _ { \mathrm { f } }$ is known, the equations (10.17) form a set of reduced equations in the slow variable $( \pmb q , \pmb p )$ .

Let us explicitly compute $\bar { F } _ { \mathrm { f } }$ for our two examples. We find that

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } ( x ( \tau ) - L ) d \tau = 0 ,
$$

and

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } { x ( \tau ) ^ { 2 } d \tau } = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } { \frac { 2 J } { K ^ { 1 / 2 } } \sin ^ { 2 } ( \tau ) d \tau } = \frac { J } { K ^ { 1 / 2 } } ,
$$

respectively. Hence we obtain $\bar { \pmb { F } } _ { \mathrm { f } } = { \bf 0 }$ for (10.7) and

$$
\bar { F } _ { \mathrm { f } } = - \frac { J } { 2 \varepsilon \sqrt { K ( \pmb q ) } } \nabla _ { \pmb q } K ( \pmb q ) = - \varepsilon ^ { - 1 } J \nabla _ { \pmb q } \sqrt { K ( \pmb q ) } ,
$$

for (10.8), respectively. Furthermore, the averaged equations (10.17) can be written in canonical form with Hamiltonian

$$
\bar { H } ( \pmb { q } , \pmb { p } ) = H _ { s } ( \pmb { q } , \pmb { p } ) + \omega ( \pmb { q } ) \mathcal { I } ,
$$

and $\omega = \varepsilon ^ { - 1 }$ or $\omega = \varepsilon ^ { - 1 } \sqrt { K ( \pmb q ) }$ , respectively. The value of the adiabatic invariant $J$ is taken to be constant and is determined from the initial values of $\left( q , x , p _ { x } \right)$ . We mention that $\bar { H }$ can, formally, be obtained from $H = H _ { \mathsf { s } } + H _ { \mathsf { f } }$ , the identity (10.11) and the adiabatic invariance of $J$ .

With this we complete the short discussion on the concept of averaging and the idea of reduced equations. See, for example, [165, 18, 28, 163] for further results on mechanical systems with a single fast degree of freedom.

Let us compare the full dynamics to the reduced dynamics for the Hamiltonian (10.14). The reduced Hamiltonian is given by

$$
\bar { H } = \frac { 1 } { 2 } ( p ^ { 2 } + q ^ { 2 } ) + \sqrt { 1 + \alpha q ^ { 2 } } J .
$$

We take the same initial conditions and parameter values as used in Section 10.1.4. In Fig. 10.5, we plot the solution curves in the slow $( q , p )$ variable for the unreduced and reduced equations. Note that the equations obtained by simply dropping the high-frequency part altogether, i.e. $\dot { q } = p$ , $\dot { p } = - q$ , would have completely circular solutions.

The averaging approach and the complete elimination of the highly oscillatory degree of freedom, as just outlined, is difficult to generalize to systems with more than one fast degree of freedom. This is because of possible resonant interactions between the fast modes which lead to non-constant action variables [190, 27, 160]. However, the idea to average the fast forces can still be utilized in numerical methods and we will devote the rest of the chapter to two such numerical averaging approaches.

![](images/3d21573f0ab02c9960bd5983f1e9c10cf4ab51948d601870f6894464a83f80bc.jpg)  
Figure 10.5 Comparison of slow $q \mathrm { . }$ -component of the solutions to the unreduced and averaged equations.

# 10.3 The reversible averaging (RA) method

Let us now develop a numerical method that uses the idea of averaging to allow for larger timesteps. The main motivation is to avoid the loss of accuracy or, even worse, the instabilities near resonances that we observed for standard LTS methods. We wish to emphasize that the idea of averaging in the context of LTS methods and symplectic integration was first proposed by GARC´ıA-ARCHILLA, SANZ-SERNA, AND SKEEL [67]. The associated method MOLLY will be discussed in detail in the following section. In this section, we will focus on the reversible averaging (RA) method of LEIMKUHLER AND REICH [112].

Let us assume that a numerical approximation $z ^ { n } = ( \pmb { q } ^ { n } , \pmb { p } ^ { n } , x ^ { n } , p _ { x } ^ { n } )$ is given at time level $t _ { n }$ . We first describe a procedure to numerically compute a timeaveraged force $\bar { F } _ { \mathrm { f } }$ at $t ~ = ~ t _ { n }$ . The idea is to freeze the value of $\pmb q ( t )$ at $\pmb q ^ { n }$ and to compute the solution $( x ( t ) , p _ { x } ( t ) )$ to the associated fast equations of motion

$$
\dot { x } = \varepsilon ^ { - 1 } p _ { x } , \qquad \dot { p } _ { x } = \varepsilon ^ { - 1 } \nabla _ { x } V _ { \mathsf { f } } ( x , \pmb { q } ^ { n } ) ,
$$

over the time interval $t \in \left[ t _ { n - 1 } , t _ { n + 1 } \right]$ with initial (“middle”) conditions $x ( t _ { n } ) =$ $x ^ { n }$ and $p _ { x } ( t _ { n } ) = p _ { x } ^ { n }$ . We determine a time-averaged force along this solution

$$
\bar { F } _ { \mathrm { f } } ^ { n } = - \frac { 1 } { 2 \Delta t } \int _ { - \Delta t } ^ { \Delta t } { \varepsilon } ^ { - 1 } \nabla _ { q } V _ { \mathrm { f } } ( x ( t _ { n } + \tau ) , { \pmb q } ^ { n } ) d \tau .
$$

The reversible averaging (RA) method is now defined by the following sequence of steps

THE REVERSIBLE AVERAGING (RA) METHOD

1. Compute the time-averaged force $\bar { F } _ { \mathrm { f } } ^ { n }$ using (10.18) and apply the f St¨ormer–Verlet method to compute the new position $\pmb q ^ { n + 1 }$ at $t _ { n + 1 }$

$$
\begin{array} { c } { { { \pmb p } ^ { n + 1 / 2 } = { \pmb p } ^ { n } + \displaystyle \frac { \Delta t } { 2 } \left[ \bar { \pmb F } _ { \mathrm { f } } ^ { n } - \nabla _ { \mathbfit q } V ( \pmb q ^ { n } ) \right] , } } \\ { { { \pmb q } ^ { n + 1 } = { \pmb q } ^ { n } + \Delta t { \pmb M } ^ { - 1 } { \pmb p } ^ { n + 1 / 2 } . } } \end{array}
$$

2. Compute the solution $( x ( t ) , p _ { x } ( t ) )$ to the fast equations of motion

$$
\dot { x } = \varepsilon ^ { - 1 } p _ { x } , \qquad \dot { p } _ { x } = \varepsilon ^ { - 1 } \nabla _ { x } V _ { \dagger } ( x , \bar { \pmb q } ( t ) ) ,
$$

over $t \in \left[ t _ { n } , t _ { n + 1 } \right]$ with $\pmb { \bar { q } } ( t )$ varying along the linear path

$$
\bar { q } ( t ) = \frac { { { q } ^ { n + 1 } } + { { q } ^ { n } } } { 2 } + ( t - { { t } _ { n + 1 / 2 } } ) { { M } ^ { - 1 } } { { p } ^ { n + 1 / 2 } } ,
$$

and initial conditions equal to $x ( t _ { n } ) = x ^ { n }$ , $p _ { x } ( t _ { n } ) = p _ { x } ^ { n }$ . Next set

$$
x ^ { n + 1 } = x ( t _ { n + 1 } ) , \qquad p _ { x } ^ { n + 1 } = p _ { x } ( t _ { n + 1 } ) .
$$

3. Compute the time-averaged force $\bar { F } ^ { n + 1 }$ and update the momentum

$$
\pmb { p } ^ { n + 1 } = \pmb { p } ^ { n + 1 / 2 } + \frac { \Delta t } { 2 } \left[ \bar { F } _ { \mathrm { f } } ^ { n + 1 } - \nabla _ { \pmb { q } } V ( \pmb { q } ^ { n + 1 } ) \right] .
$$

If the force acting on the slow particles is linear in $x$ , then the average to be computed for the slow momentum update simplifies to

$$
\bar { F } _ { \mathrm { f } } ^ { n } = - \varepsilon \nabla _ { \ b { q } } V _ { \mathrm { f } } ( \bar { x } ^ { n } , \pmb { q } ^ { n } ) ,
$$

where

$$
\bar { x } ^ { n } = \frac 1 { 2 \Delta t } \int _ { - \Delta t } ^ { \Delta t } x ( t _ { n } + \tau ) d \tau .
$$

The same simplification may be used whenever $\left| x ^ { n } - \bar { x } ^ { n } \right|$ is sufficiently small.

The RA method is a symmetric one-step method. This implies that the method respects the time-reversal symmetry: $S : ( q , p , x , p _ { x } ) \to ( q , - p , x , - p _ { x } )$ , since it is easy to verify that

$$
\begin{array} { r } { { \pmb { S } } \pmb { \phi } _ { \Delta t } ( z ) = \pmb { \phi } _ { - \Delta t } ( { \pmb { S } } z ) . } \end{array}
$$

However, the RA method is, in general, not symplectic.

# 10.3.1 Numerical experiments

Let us explore the properties of the RA method by numerical investigation of three model problems.

# A linear test problem

Let us apply the RA method to the Hamiltonian (10.12). Since the system is linear, one can explicitly construct the associated linear timestep map ${ M } _ { \Delta t }$ .

We first consider the motion of the fast system

$$
\dot { x } = \varepsilon ^ { - 1 } p _ { x } , \qquad \dot { p } _ { x } = - \varepsilon ^ { - 1 } ( x - q ) ,
$$

for $q = q ^ { n }$ fixed. We introduce the new variable $\xi = x - q$ and obtain the solution

$$
\xi ( t ) = \xi ( 0 ) \cos ( \omega t ) + p _ { x } ( 0 ) \sin ( \omega t ) ,
$$

$\omega = \varepsilon ^ { - 1 }$ . The averaged $\bar { \xi } ^ { n }$ is given by

$$
\bar { \xi } ^ { n } = \frac { 1 } { 2 \Delta t } \int _ { - \Delta t } ^ { \Delta t } \xi ( t ) d t = \xi ^ { n } \frac { 1 } { \omega \Delta t } \sin ( \omega \Delta t ) ,
$$

where $\xi ^ { n } = x ^ { n } - q ^ { n }$ . Hence the update of the slow variables becomes

$$
\begin{array} { l } { { p ^ { n + 1 / 2 } = p ^ { n } - \displaystyle \frac { \Delta t } { 2 } \left[ q ^ { n } + C \displaystyle \frac { q ^ { n } - x ^ { n } } { \varepsilon } \right] , } } \\ { { q ^ { n + 1 } = q ^ { n } + \Delta t p ^ { n + 1 / 2 } , } } \end{array}
$$

where

$$
C = \frac { \sin ( \omega \Delta t ) } { \omega \Delta t } .
$$

Next we have to find the propagator for the linear system (10.19) along $q ( t ) = q ^ { n } + t p ^ { n + 1 / 2 }$ . We again use the variable $\xi = x - q$ and obtain the linear system

$$
\dot { \xi } = \omega ( p _ { x } - \varepsilon p ^ { n + 1 / 2 } ) , \qquad \dot { p } _ { x } = - \omega \xi .
$$

The solutions of this system are given by

$$
\begin{array} { r l } & { \xi ( t ) = \xi ( 0 ) \cos ( \omega t ) + ( p _ { x } ( 0 ) - \varepsilon p ^ { n + 1 / 2 } ) \sin ( \omega t ) , } \\ & { p _ { x } ( t ) = \varepsilon p ^ { n + 1 / 2 } + ( p _ { x } ( 0 ) - \varepsilon p ^ { n + 1 / 2 } ) \cos ( \omega t ) - \xi ( 0 ) \sin ( \omega t ) , } \end{array}
$$

and we obtain the propagator

$$
\begin{array} { r l } & { x ^ { n + 1 } = q ^ { n + 1 } + ( x ^ { n } - q ^ { n } ) \cos ( \omega \Delta t ) + ( p _ { x } ^ { n } - \varepsilon p ^ { n + 1 / 2 } ) \sin ( \omega \Delta t ) \quad , } \\ & { p _ { x } ^ { n + 1 } = \varepsilon p ^ { n + 1 / 2 } + ( p _ { x } ^ { n } - \varepsilon p ^ { n + 1 / 2 } ) \cos ( \omega \Delta t ) - ( x ^ { n } - q ^ { n } ) \sin ( \omega \Delta t ) . } \end{array}
$$

We finally update the momentum by

$$
p ^ { n + 1 } = p ^ { n + 1 / 2 } - \frac { \Delta t } { 2 } \left[ q ^ { n + 1 } + C \frac { q ^ { n + 1 } - x ^ { n + 1 } } { \varepsilon } \right] .
$$

It is found that the associated propagator is stable for all values of $\Delta t$ . The precise motion of all four eigenvalues can be found in Fig. 10.6. Note that the eigenvalues stay on the unit circle.

We wish to point out that the proper choice of the average in (10.20) is crucial. For example, replacing (10.20) by

$$
\bar { \xi } ^ { n } = \frac { 1 } { \Delta t } \int _ { - \Delta t / 2 } ^ { \Delta t / 2 } \xi ( t ) d t = \xi ^ { n } \frac { 2 } { \omega \Delta t } \sin ( \omega \Delta t / 2 ) ,
$$

leads to resonance instabilities similar to those observed in Fig. 10.2.

The linear system (10.19) could also be integrated along a constant $q =$ $q ^ { n + 1 / 2 } = q ^ { n } + \Delta t / 2 p ^ { n }$ . In this case, the linear propagator (10.21)–(10.22) simplifies to

$$
\begin{array} { r l } & { x ^ { n + 1 } = q ^ { n + 1 / 2 } + ( x ^ { n } - q ^ { n + 1 / 2 } ) \cos ( \omega \Delta t ) + p _ { x } ^ { n } \sin ( \omega \Delta t ) , } \\ & { p _ { x } ^ { n + 1 } = p _ { x } ^ { n } \cos ( \omega \Delta t ) - ( x ^ { n } - q ^ { n + 1 / 2 } ) \sin ( \omega \Delta t ) . } \end{array}
$$

However, this modification degrades the performances of the RA method. See the numerical experiments in the following subsection.

# A nonlinear model problem

Let us come back to the nonlinear model problem (10.14) of Section 10.1.4. The momentum update for the RA method becomes

$$
\begin{array} { c } { { p ^ { n + 1 / 2 } = p ^ { n - 1 / 2 } - \Delta t q ^ { n } - { \displaystyle \frac { \alpha q ^ { n } } { 2 \sqrt { 1 + \alpha ( q ^ { n } ) ^ { 2 } } } \left[ \left( ( x ^ { n } ) ^ { 2 } + { \displaystyle \frac { ( p _ { x } ^ { n } ) ^ { 2 } } { 1 + \alpha ( q ^ { n } ) ^ { 2 } } } \right) \omega \Delta t \right. } } } \\ { { \left. + \left( ( x ^ { n } ) ^ { 2 } - { \displaystyle \frac { ( p _ { x } ^ { n } ) ^ { 2 } } { 1 + \alpha ( q ^ { n } ) ^ { 2 } } } \right) \cos ( \omega \Delta t ) \sin ( \omega \Delta t ) \right] , } } \end{array}
$$

![](images/2e44594645e229460cc625b3ef235131e8806ef280adaf6e55a5815205e08552.jpg)  
Figure 10.6 Eigenvalues of RA propagator as a function of $\Delta t / \varepsilon$ , $\varepsilon = 1 / 4 0$ .

where $\omega = \varepsilon ^ { - 1 } \sqrt { 1 + \alpha q ^ { 2 } }$ . The fast system is propagated by integrating

$$
\dot { q } = p ^ { n + 1 / 2 } , \quad \dot { p } = 0 , \quad \dot { x } = \varepsilon ^ { - 1 } p _ { x } \quad \dot { p } _ { x } = - \varepsilon ^ { - 1 } ( 1 + \alpha q ^ { 2 } ) x ,
$$

using St¨ormer–Verlet with a small stepsize $\delta t \approx 0 . 1 \varepsilon$ subject to the constraint that $\Delta t / \delta t$ is an integer. We call this the RA-1 method. For comparison, we also implemented the following version of the RA method. The momentum update in $p$ is kept the same as for RA-1. But the fast system is propagated via

$$
q ^ { n + 1 / 2 } = q ^ { n } + \frac { \Delta t } { 2 } p ^ { n + 1 / 2 } ,
$$

followed by the exact solution of

$$
\dot { x } = \varepsilon ^ { - 1 } p _ { x } \quad \dot { p } _ { x } = - \varepsilon ^ { - 1 } ( 1 + \alpha ( q ^ { n + 1 / 2 } ) ^ { 2 } ) x ,
$$

and

$$
q ^ { n + 1 } = q ^ { n + 1 / 2 } + \frac { \Delta t } { 2 } p ^ { n + 1 / 2 } .
$$

We call this method RA-0. We performed the same numerical experiment as described in Section 10.1.2 for the MTS method. The results can be found in Fig. 10.7. While RA-0 is cheaper to implement than RA-1, its performance does not match that of RA-1. The largest relative error in energy over the whole range of stepsizes $\Delta t / \varepsilon \in [ 1 , 1 0 ]$ is $\Delta E _ { \mathrm { m a x } } \approx 0 . 0 2 7 1$ for RA-1 and $\Delta E _ { \mathrm { m a x } } \approx 1 . 2 1 2 4$ for RA-0. RA-1 also clearly outperforms the MTS method of Section 10.2. Again, we emphasize that the increased errors in energy are not linked to instabilities but are to be attributed to a reduced accuracy of the method. The nearly level error in the adiabatic invariant for the RA-1 method is due to a constant resolution of the fast oscillations by choosing $\delta t \approx 0 . 1 \varepsilon$ independently of $\Delta t$ .

![](images/efff6c36ff2e087b1fd72a0dd87e1cfe80fb9ba69934962707fe401619839098.jpg)  
Figure 10.7 Maximum relative errors in total energy and adiabatic invariant as a function of $\Delta t / \varepsilon$ , $\varepsilon = 1 / 4 0$ , for RA methods.

# 10.4 The mollified impulse (MOLLY) method

The mollified impulse method (MOLLY) [67] has been designed for a slightly different class of Hamiltonian systems than those considered so far. Let us therefore

assume that we are given a Hamiltonian

$$
H = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } + V _ { \dagger } ( \pmb { q } ) + V _ { 5 } ( \pmb { q } ) ,
$$

such that the reduced Hamiltonian

$$
H _ { \mathsf { f } } = { \frac { 1 } { 2 } } { \pmb { p } } ^ { T } { \pmb { M } } ^ { - 1 } { \pmb { p } } + V _ { \mathsf { f } } ( { \pmb { q } } )
$$

well captures the motion of the overall system over short time intervals. Note that we do not have an associated splitting into slow and fast variables as assumed so far.

An MTS method can be implemented in the following way. We integrate $H _ { \mathrm { f } }$ by the St¨ormer–Verlet method using a small timestep $\delta t$ . Denote the associated timestepping map by $\pmb { \psi } _ { \delta t , H _ { f } }$ . Now consider the symplectic composition method

$$
\pmb { \psi } _ { \Delta t } : = \pmb { \phi } _ { \Delta t / 2 , V _ { \mathrm { s } } } \circ \left[ \pmb { \psi } _ { \delta t , H _ { \mathrm { f } } } \right] ^ { N } \circ \pmb { \phi } _ { \Delta t / 2 , V _ { \mathrm { s } } } ,
$$

$\Delta t = \delta t \cdot N$ . If we apply this MTS method to a linear test problem, then resonance instabilities are, in general, observed (see BIESIADECKI AND SKEEL [20] and GARC´ıA-ARCHILLA, SANZ-SERNA, AND SKEEL [67]).

The basic idea to eliminate or weaken some of these resonances is to replace the “slow” potential energy $V _ { s }$ by an averaged potential energy. In the mollified MTS (MOLLY) method, as suggested by GARC´ıA-ARCHILLA, SANZ-SERNA, AND SKEEL [67], this is achieved in the following way. Let $\pmb q ( t )$ denote the solution of $H _ { \mathrm { f } }$ with initial conditions $\pmb q ( 0 ) = \pmb q$ and $\pmb { p } ( 0 ) = \pmb { 0 }$ . Then one can compute an averaged $\bar { \pmb q }$ , for example the long average [67]

$$
\bar { \pmb q } = \frac { 1 } { 2 \Delta t } \int _ { - \Delta t } ^ { \Delta t } \pmb q ( t ) d t .
$$

The relation between the initial $\pmb q$ and the averaged $\bar { \pmb q }$ can be viewed as a map

$$
\bar { \pmb q } = \mathcal { A } ( \pmb q ) .
$$

This map is applied to the potential energy function $V _ { s }$ to yield a new (filtered) potential energy

$$
\bar { V } _ { 5 } ( \pmb q ) = V ( \mathcal { A } ( \pmb q ) ) .
$$

MOLLY is now characterized by the modified MTS method

$$
\pmb { \psi } _ { \Delta t } : = \pmb { \phi } _ { \Delta t / 2 , \bar { V } _ { \mathrm { s } } } \circ [ \pmb { \psi } _ { \delta t , H _ { \mathrm { r } } } ] ^ { N } \circ \pmb { \phi } _ { \Delta t / 2 , \bar { V } _ { \mathrm { s } } } .
$$

Note that $\pmb { \phi } _ { \Delta t / 2 , \bar { V } _ { \mathrm { s } } }$ denotes the $\mathsf { e x a c t }$ time- $\Delta t / 2$ -flow map associated to the smoothed potential energy function $\bar { V _ { \mathsf { s } } }$ . Hence the overall timestepping generates a symplectic map.

An important limitation of MOLLY should be pointed out. Since averaging and differentiation do not, in general, commute, the smoothed potential energy can only be used when the difference between $\pmb q$ and $\boldsymbol { \mathcal { A } } ( \boldsymbol { q } )$ is small or the system is (nearly) linear.

Let us come back to the linear test example (10.12). We split the Hamiltonian into

$$
H _ { \mathrm { f } } = \frac { 1 } { 2 } \left[ p ^ { 2 } + \varepsilon ^ { - 1 } ( p _ { x } ^ { 2 } + ( x - q ) ^ { 2 } ) \right]
$$

and

$$
V _ { s } ( x , q ) = \frac { 1 } { 2 } q ^ { 2 } .
$$

The propagator for the fast $H _ { \mathsf { f } }$ -system is $e ^ { \Delta t A }$ with

$$
\pmb { A } = \left[ \begin{array} { c c c c } { 0 } & { 1 } & { 0 } & { 0 } \\ { - \pmb { \varepsilon } ^ { - 1 } } & { 0 } & { \pmb { \varepsilon } ^ { - 1 } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \pmb { \varepsilon } ^ { - 1 } } \\ { \pmb { \varepsilon } ^ { - 1 } } & { 0 } & { - \pmb { \varepsilon } ^ { - 1 } } & { 0 } \end{array} \right] ,
$$

and $z = ( q , p , x , p _ { x } ) ^ { T }$ . The next step is to construct a mollifier $\mathcal { A }$ . To do so, it is convenient to introduce transformed coordinates $q _ { 1 } = q$ and $q _ { 2 } = x - q$ . The corresponding canonical momenta are given by $p = p _ { 1 } - p _ { 2 }$ and $p _ { x } = p _ { 2 }$ . Thus the transformed Hamiltonian $\tilde { H } _ { \mathrm { f } }$ is

$$
\tilde { { \cal H } } _ { \mathrm { f } } = \frac 1 2 \left[ ( p _ { 1 } - p _ { 2 } ) ^ { 2 } + \varepsilon ^ { - 1 } ( p _ { 2 } ^ { 2 } + q _ { 2 } ^ { 2 } ) \right] ,
$$

with associated equations of motion

$$
\dot { p } _ { 1 } = 0 , \quad \dot { q } _ { 1 } = p _ { 1 } - p _ { 2 } , \quad \dot { p } _ { 2 } = - \varepsilon ^ { - 1 } q _ { 2 } , \quad \dot { q } _ { 2 } = p _ { 2 } - p _ { 1 } + \varepsilon ^ { - 1 } p _ { 2 } .
$$

We solve these equations subject to zero initial conditions in $p _ { 1 }$ and $p _ { 2 }$ , i.e. $p _ { 1 } ( 0 ) = p _ { 2 } ( 0 ) = 0$ . We immediately conclude that $p _ { 1 } ( t ) = 0$ and the equations of motion simplify to

$$
\dot { q } _ { 1 } = - p _ { 2 } , \quad \dot { p } _ { 2 } = - \varepsilon ^ { - 1 } q _ { 2 } , \quad \dot { q } _ { 2 } = ( 1 + \varepsilon ^ { - 1 } ) p _ { 2 } .
$$

The frequency of the fast oscillations in $\left( q _ { 2 } , p _ { 2 } \right)$ is

$$
\omega = \sqrt { \varepsilon ^ { - 1 } ( 1 + \varepsilon ^ { - 1 } ) } ,
$$

and solutions are given explicitly by

$$
q _ { 2 } ( t ) = q _ { 2 } ( 0 ) \cos ( \omega t ) , \qquad p _ { 2 } ( t ) = - \frac { q _ { 2 } ( 0 ) } { \varepsilon \omega } \sin ( \omega t ) .
$$

Hence, we obtain

$$
q _ { 1 } ( t ) = q _ { 1 } ( 0 ) - \frac { q _ { 2 } ( 0 ) } { 1 + \varepsilon ^ { - 1 } } \left( \cos ( \omega t ) - 1 \right)
$$

and the averaged value

$$
\bar { q } _ { 1 } = \frac { 1 } { 2 \Delta t } \int _ { - \Delta t } ^ { \Delta t } q _ { 1 } ( t ) d t = q _ { 1 } ( 0 ) - \frac { q _ { 2 } ( 0 ) } { 1 + \varepsilon ^ { - 1 } } \left( \frac { \sin ( \omega \Delta t ) } { \Delta t \omega } - 1 \right) .
$$

If we translate this result back to the original variables, then the mollifier $\mathcal { A }$ is given by

$$
\bar { q } = \mathcal { A } ( x , q ) = q - \frac { x - q } { 1 + \varepsilon ^ { - 1 } } \left( \frac { \sin ( \omega \Delta t ) } { \omega \Delta t } - 1 \right)
$$

and the mollified potential energy $V _ { s }$ by

$$
\bar { V } _ { \mathrm { s } } = \frac { 1 } { 2 } \bar { q } ^ { 2 } = \frac { 1 } { 2 } q ^ { 2 } + \frac { C ^ { 2 } } { 2 } ( x - q ) ^ { 2 } + C ( q - x ) q ,
$$

where

$$
C = \frac { 1 } { 1 + \varepsilon ^ { - 1 } } \left( \frac { \sin ( \omega \Delta t ) } { \omega \Delta t } - 1 \right) .
$$

The propagator for the mollified slow system is $e ^ { \Delta t \bar { B } }$ with

$$
\bar { B } = \left[ \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - ( 1 + C ) ^ { 2 } } } & { { 0 } } & { { C + C ^ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { C + C ^ { 2 } } } & { { 0 } } & { { - C ^ { 2 } } } & { { 0 } } \end{array} \right] .
$$

Fig. 10.8 reveals that the mollified LTS method is vastly more stable than the original LTS method (10.13). However, tiny resonance instabilities are still present near multiples of $2 \pi$ .

See problem 4 in the Exercises for another example of a mollified MTS method.

# 10.5 Multiple frequency systems

So far we have exclusively dealt with systems that possess a single fast degree of freedom. This is, of course, not the situation typically encountered in applications such as molecular dynamics or numerical weather prediction [47]. The LTS methods described in Sections 10.3 and 10.4 can still be applied to such more general highly oscillatory systems but they encounter additional difficulties. Take the case of two fast degrees of freedom with frequencies $\omega _ { 1 }$ and $\omega _ { 2 }$ . Following the discussion in Section 10.1.1, a standard LTS methods leads to the investigation of the two associated frequencies $\Omega _ { 1 , \Delta t }$ and $\Omega _ { 2 , \Delta t }$ which are both in the range ${ \mathcal { T } } = [ - \pi , \pi )$ . While $\omega _ { 1 }$ and $\omega _ { 2 }$ will in general be different and non-resonant, we can now always find a stepsize $\Delta t$ such that $\Omega _ { 1 , \Delta t } = \Omega _ { 2 , \Delta t }$ . Hence, for that particular $\Delta t$ , the two modes are in one-to-one resonance which, typically, manifests itself with a numerical instability of the associated integration scheme. Furthermore, these instabilities are not easily mollified because they can occur for any value of $\Omega _ { 1 , \Delta t } = \Omega _ { 2 , \Delta t }$ in the interval $\mathcal { T }$ . See also [67].

![](images/245a95efd22a78460d6080f6739284d09d21fb208668e3fc540049eaece3abe7.jpg)  
Figure 10.8 Stability of MOLLY as a function of $\Delta t / \varepsilon$ .

The only known stable MTS method for general Hamiltonian systems of type

$$
H = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } + V ( \pmb { q } ) + \frac { 1 } { 2 \varepsilon ^ { 2 } } \pmb { g } ( \pmb { q } ) ^ { T } \pmb { g } ( \pmb { q } )
$$

has been proposed by IZAGUIRRE, REICH AND SKEEL [93] and makes use of the holonomic constraint $g ( \pmb q ) = \pmb 0$ in the definition of the mollifier $\mathcal { A }$ . See the Exercises.

# 10.6 Exercises

1. Non-autonomous backward error analysis. Following a result by KUKSIN AND POSCHEL ¨ [100] (see also MOAN [135]), we can imbed a symplectic method

into the time-one-flow map of a non-autonomous Hamiltonian system with Hamiltonian of the form

$$
\tilde { H } _ { \Delta t } = 2 \pi e + \Delta t H ( q , p ) + \Delta t g _ { \Delta t } ( q , p , \tau ) ,
$$

where $g _ { \Delta t }$ is an appropriate function which is $2 \pi$ -periodic in $\tau$ . The symplectic structure of the extended equations in $( q , p , \tau , e )$ is

$$
\omega = d p \wedge d q + d e \wedge d \tau .
$$

a. Perform a canonical change of variables from $( e , \tau )$ to $E = - 2 e$ and $s = - \tau / 2$ . Verify that the new equations of motion can be written in the form

$$
\begin{array} { r l } & { \dot { q } = + \Delta t \nabla _ { p } [ H ( q , p ) + h _ { \Delta t } ( q , p , s ) ] , } \\ & { \dot { p } = - \Delta t \nabla _ { q } [ H ( q , p ) + h _ { \Delta t } ( q , p , s ) ] , } \\ & { \dot { s } = - \pi , } \\ & { \dot { E } = - \Delta t \nabla _ { s } h _ { \Delta t } ( q , p , s ) , } \end{array}
$$

and find $h _ { \Delta t }$ in terms of $g _ { \Delta t }$ .

b. Use the result from (a) to ”justify” the modified Hamiltonian (10.6).

2. Resonance instabilities for single-degree-of-freedom systems. Consider a one degree of freedom linear system

$$
\dot { q } = \omega p , \qquad \dot { p } = - \omega q - q ,
$$

which we write as

$$
\dot { z } = \omega J z + B z ,
$$

with $z = ( q , p ) ^ { T }$ . An LTS method can be defined by

$$
M _ { \Delta t } = W _ { 2 } ( \Delta t / 2 ) W _ { 1 } ( \omega \Delta t ) W _ { 2 } ( \Delta t / 2 ) ,
$$

where

$$
W _ { 1 } ( \omega \Delta t ) = \mathbf { e } ^ { \omega \Delta t J } , \qquad W _ { 2 } ( \Delta t / 2 ) = \mathbf { e } ^ { \Delta t / 2 B } .
$$

a. According to standard stability results for symplectic matrices (see [7]), we know that ${ M } _ { \Delta t }$ is stable provided

(i) $\Delta t$ is sufficiently small, (ii) the eigenvalues of $W _ { 1 } ( \omega \Delta t )$ are on the unit circle and simple.

What values of $\tau = \omega \Delta t$ give rise to double eigenvalues of $W _ { 1 } ( \tau ) ?$

b. Assume that $\Delta t$ has been chosen such that

$$
| \omega \Delta t - 2 \pi | \ll \Delta t .
$$

Show that ${ M } _ { \Delta t }$ is equivalent to

$$
M _ { \Delta t } = W _ { 2 } ( \Delta t / 2 ) W _ { 1 } ( \omega \Delta t - 2 \pi ) W _ { 2 } ( \Delta t / 2 ) .
$$

Determine the parameter $\hat { \omega }$ , $| \hat { \omega } | \leq \pi / \Delta t$ , in the equation

$$
\dot { z } = \hat { \omega } J z + B z ,
$$

such that the associated matrix exponential,

$$
\begin{array} { r } { \tilde { W } ( \Delta t ) = { \bf e } ^ { \Delta t ( \hat { \omega } J + B ) } , } \end{array}
$$

satisfies

$$
\begin{array} { r } { \pmb { M } _ { \Delta t } = \tilde { \pmb { W } } ( \Delta t ) + \mathcal { O } ( \Delta t ^ { 2 } ) , } \end{array}
$$

as $\Delta t \to 0$ and $\omega  \infty$ subject to (10.26).

Show that $\hat { \omega }$ can become negative for certain values of $\Delta t$ . What implications can we deduce for the solution behavior of the modified equation (10.27)? Compare your findings with the results from Fig. 10.1.

3. Resonance instabilities for single-degree-of-freedom systems. If one applies the LTS method (10.5) to the nonlinear oscillator

$$
\dot { q } = \omega p , \qquad \dot { p } = - \omega q - g ^ { \prime } ( q ) ,
$$

$g ^ { \prime } ( q )$ an odd function in $q$ , numerical instabilities can be observed for $\omega \Delta t \approx$ $k \pi$ , $k$ a positive integer. We have seen in Section 10.1.1 that the LTS method (10.5) leads to a modified Hamiltonian $\tilde { H }$ with an effective frequency $\hat { \omega } \approx 0$ for stepsizes $\Delta t$ such that $\omega \Delta t \approx 2 k \pi$ . A similar statement can, in fact, be derived for the case $\omega \Delta t \approx k \pi$ . We write the LTS method (10.5) applied to (10.28) in the abstract form

$$
z ^ { n + 1 } = \pmb { \psi } _ { \Delta t } ( z ^ { n } ) , \qquad z ^ { n } = ( q ^ { n } , p ^ { n } ) ^ { T } .
$$

Next we perform a change of variables

$$
\hat { z } ^ { n } = ( - 1 ) ^ { n } z ^ { n }
$$

and formally obtain a numerical method

$$
\hat { z } ^ { n + 1 } = \hat { \pmb { { \psi } } } _ { \Delta t } ( \hat { z } ^ { n } ) ,
$$

in terms of the new sequence of variables $\left\{ \hat { z } ^ { n } \right\}$ .

a. Derive an explicit expression for $\hat { \pmb { { \psi } } } _ { \Delta t }$ assuming that $g ^ { \prime } ( - q ) = - g ^ { \prime } ( q )$ .   
b. Show that $\hat { \pmb { { \psi } } } _ { \Delta t }$ is equivalent to the LTS method (10.5) applied to the nonlinear oscillator $\dot { q } = \left( \omega + \frac { \pi } { \Delta t } \right) p , \qquad \dot { p } = - \left( \omega + \frac { \pi } { \Delta t } \right) q - g ^ { \prime } ( q ) .$   
c. Following the arguments of Section 10.1.1, discuss the numerical behavior of $\hat { \pmb { { \psi } } } _ { \Delta t }$ for $\omega \Delta t \approx k \pi$ , $k$ an odd integer. See also the previous problem.

4. Mollified LTS methods. We develop a mollified version of the LTS method (10.5) applicable to the nonlinear oscillator (10.28). The basic idea is to find a mollified slow Hamiltonian $\bar { H } _ { s }$ such that

$$
\pmb { \phi } _ { \Delta t / 2 , \bar { H } _ { s } } = \mathbf { i d } ,
$$

for $\omega \Delta t = k \pi$ , $k$ a positive integer. This implies that the numerical method reduces to

$$
\pmb { \psi } _ { \Delta t } = \pmb { \phi } _ { \Delta t , H _ { f } } = \mathbf { e } ^ { \omega \Delta t J } ,
$$

for resonant stepsizes $\Delta t$ .

a. Consider the matrix

$$
C ( \tau ) = \frac { 1 } { 2 \tau } J ^ { - 1 } \left( { \bf e } ^ { 2 \tau J } - I _ { 2 } \right) .
$$

Show that (i) $C ( \tau ) \to I _ { 2 }$ as $\tau  0$ and (ii) $c ( \tau ) = 0$ for $\tau = k \pi$ . Remark: Condition (i) is necessary for convergence of the method as $\tau  0$ .

b. Given an arbitrary Hamiltonian $H _ { s } ( z )$ , we define the associated mollified Hamiltonian

$$
\bar { H } _ { s } ( z ; \tau ) = H _ { s } ( C ( \tau ) z ) .
$$

Find $\bar { H } _ { s } = \bar { V } _ { s }$ for $H _ { s } = V _ { s } = q ^ { 2 } / 2$ .

c. Using the result from (b), implement the mollified LTS method

$$
\pmb { { \psi } } _ { \Delta t } = \pmb { { \phi } } _ { \Delta t / 2 , \bar { H } _ { s } } \circ \pmb { { \phi } } _ { \Delta t , H _ { f } } \circ \pmb { { \phi } } _ { \Delta t / 2 , \bar { H } _ { s } } ,
$$

for $H _ { s } = q ^ { 2 } / 2$ . How does the method behave near $\omega \Delta t = k \pi$ as compared with the non-mollified method?

5. Many-degrees-of-freedom systems. Additional difficulties arise when considering systems with two fast degrees of freedom, for example

$$
H = \frac { \omega _ { 1 } } { 2 } \left( p _ { 1 } ^ { 2 } + q _ { 1 } ^ { 2 } \right) + \frac { \omega _ { 2 } } { 2 } \left( p _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } \right) + V _ { s } ( q _ { 1 } , q _ { 2 } ) .
$$

For simplicity, we set $\omega _ { 1 } = \omega$ and $\omega _ { 2 } = 4 \omega$ and concentrate again on linear systems.

An LTS method of type (10.5) will produce a symplectic matrix ${ M } _ { \Delta t }$ which can be thought of as a small perturbation of the symplectic matrix

$$
W ( \omega \Delta t ) = { \bf e } ^ { \omega \Delta t A } , \qquad A = \left[ \begin{array} { c c c c } { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 2 } } \\ { { 0 } } & { { 0 } } & { { - 2 } } & { { 0 } } \end{array} \right] .
$$

Hence we have to make use of the perturbation theory of symplectic matrices. A good introduction to this topic and the associated theory due to KREJN (1950) can be found in [7]. Below we give a brief discussion on the implications for LTS methods.

a. For which values of $\tau = \omega \Delta t \neq 0$ does $W ( \tau )$ have non-simple (repeated) eigenvalues on the unit circle? (Hint: sufficient condition is $\Delta t ( \omega _ { 1 } + \omega _ { 2 } ) =$ $\pi k$ . Is this condition also necessary?) For future reference, let $\lambda$ denote the double eigenvalue with $| \mathsf { m } \lambda > 0$ . (Recall that the complex conjugate of $\lambda$ is also an eigenvalue.)   
b. Take one particular value of $\tau$ found under (a) and call it $\tau ^ { * }$ . Determine the two-dimensional plane spanned by the complex-valued eigenvectors $\pmb { v }$ of $W ( \tau ^ { * } )$ corresponding to the double eigenvalue $\lambda$ . Denote this plane by $\Pi _ { \lambda } \subset \mathbb { C } ^ { 2 }$ .   
c. The matrix $W ( \tau )$ introduces a quadratic form

$$
\kappa ( x , y ; \tau ) = x ^ { T } J W ( \tau ) y , \qquad J = \left[ \begin{array} { c c c c } { 0 } & { 1 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { - 1 } & { 0 } \end{array} \right] .
$$

Find an explicit expression of $\kappa ( x , x ; \tau ^ { * } )$ for your choice of $\tau = \tau ^ { * }$ .

d. A standard result in symplectic perturbation theory [7] implies that the symplectic matrix $W ( \tau )$ is stable under small (symplectic) perturbations, if its eigenvalues are simple or, in case there is a non-simple eigenvalue $\lambda$ , if the quadratic form $\kappa ( x , x ; \tau )$ has the same sign for all real vectors $x$ in $\Pi _ { \lambda }$ . Is $W ( \tau ^ { * } )$ stable for your choice of $\tau = \tau ^ { * } ?$ (Hint: The matrix is unstable under perturbations for all resonances satisfying $\Delta t ( \omega _ { 1 } + \omega _ { 2 } ) = 2 \pi k$ , $k$ a positive integer [67].)

6. Averaged equations and adiabatic invariant. Consider a particle of unit mass with coordinate $\pmb q = ( q _ { 1 } , q _ { 2 } ) ^ { T } \in \mathbb { R } ^ { 2 }$ subject to the potential

$$
V ( \pmb q ) = \frac { 1 } { 2 } q _ { 1 } ^ { 2 } + \frac { 1 } { 2 \varepsilon ^ { 2 } } ( \| \pmb q \| - L ( \phi ) ) ^ { 2 } ,
$$

where the equilibrium length $L$ is given by $L ( \phi ) = 1 + 0 . 2 \sin ^ { 2 } \phi$ and $- \pi <$ $\phi \leq \pi$ is the angle of $\pmb { q } = ( q _ { 1 } , q _ { 2 } ) ^ { T }$ with the $q _ { 1 }$ -coordinate axis. We set $\varepsilon = 0 . 0 1$ .

a. Reformulate the problem in polar coordinates $( r , \phi )$ . Clearly, for $\varepsilon \to 0$ , the motion in the radius $r ( t )$ is highly oscillatory about its equilibrium value $L \left( \phi \right)$ . Find the associated adiabatic invariant $J$ , the fast frequency $\omega$ , and the reduced/averaged Hamiltonian.   
b. Implement a symplectic method for the unreduced Hamiltonian system and compare the results with a simulation of the constrained formulation

$$
{ \cal H } _ { \mathrm { c o n s t r } } ( \pmb q , { \pmb p } ) = \frac { 1 } { 2 } \| { \pmb p } \| ^ { 2 } + \frac { 1 } { 2 } q _ { 1 } ^ { 2 } + \lambda ( \| \pmb q \| ^ { 2 } - L ( \phi ) ^ { 2 } ) ,
$$

subject to $\| \pmb q \| ^ { 2 } = L ( \phi ) ^ { 2 }$ . Choose your initial conditions such that either $J = 0$ or $J = \varepsilon$ .

Explain your numerical findings.

7. The MTS method equilibrium. We derive the LTS method Equilibrium [93] for a Hamiltonian of the form (10.25). Given a set of coordinates $\pmb q$ , we first define the “projection” map $\bar { \pmb q } = \mathcal { A } ( \pmb q )$ as the solution to the nonlinear system

$$
\begin{array} { l } { { \bar { \pmb q } = \pmb q + \pmb G ( \pmb q ) ^ { T } \pmb \lambda , } } \\ { { \pmb 0 = \pmb g ( \bar { \pmb q } ) . } } \end{array}
$$

The map $\boldsymbol { \mathcal { A } } ( \boldsymbol { q } )$ gives rise to the mollified Hamiltonian

$$
H _ { \mathrm { m o l l y } } = \frac { 1 } { 2 } \pmb { p } ^ { T } \pmb { M } ^ { - 1 } \pmb { p } + V ( \pmb { A } ( \pmb { q } ) ) + \frac { 1 } { 2 \varepsilon ^ { 2 } } \pmb { g } ( \pmb { q } ) ^ { T } \pmb { g } ( \pmb { q } ) .
$$

a. Find the equations of motion corresponding to the mollified Hamiltonian (10.29). b. Describe an implementation of the associated MTS method (10.24).

# Molecular dynamics

Over the past several decades, molecular simulation has become increasingly important for chemists, physicists, bio-scientists, and engineers, and plays a role in applications such as rational drug design and the development of new types of materials. While many levels of detail can be incorporated if desired, in most cases work is performed with a simplified atomic model, consisting of a large number of mass points interacting in various types of forces, i.e. an N-body problem.

There are essentially two principal types of simulation methodology in common use. In Monte-Carlo (MC) methods, random steps are taken in order to achieve a rapid sampling of the most likely states of the molecule. In molecular dynamics (MD), the idea is to construct approximate trajectories for the N-body problem and to use these to gain an understanding of how the molecule evolves in time, for example in response to a stimulus, during a transition between states, or as a means for calculating averages. It should be stressed that only MD and not MC methods allow the theoretical possibility of obtaining time-dependent quantities from simulation, while both schemes can in principle be used for the same statistical-mechanical calculations. Increasingly, one finds that MD and MC schemes are combined in various ways to seek improved efficiency. In this chapter we will focus only on (pure) MD methods, and in particular on the geometric integration issues associated to computing MD trajectories. For a more complete perspective on molecular simulation, the reader is referred to a text on the subject such as that of SCHLICK [174], ALLEN AND TILDESLEY [4], RAPPAPORT [152], or FRENKEL AND SMIT [66].

Because of the very rapid oscillatory motions that are characteristic of molecular systems, very small timesteps of about a femtosecond $( 1 0 ^ { - 1 5 } 5 \mathsf { e c } )$ are typically used in molecular dynamics. This means that in order to get estimates for parameters of interest from simulation, it is necessary to perform runs involving enormous numbers of timesteps. Even a nanosecond is a very short time relative to physical phenomena, and that already represents around one million timesteps in a typical simulation. At the same time there are severe size limitations due to the complexity of the force evaluations that must be performed at each timestep.

The type of forces involved in the model can make a huge difference. If the atoms have charge, then a very long-ranged Coulombic potential will be needed. Important advances have been made in the design of efficient algorithms for these types of non-bonded interactions, but the costs are still prohibitive: at the time of this writing, systems of this type of dimension up to only several hundred thousand particles can be simulated, typically for times of at the most a few nanoseconds. The physical dimensions of such systems are only a few tens of angstroms at most. This is the typical situation for biomolecular models, which invariably include charge. Other types of molecular systems arising in materials science and condensed matter physics may not have any long-ranged forces; in such cases, the complexity of the force calculation is greatly reduced and systems of up to even a billion atoms can be simulated.

The first systems to be studied using direct simulation were purely collisional “hard sphere” systems [3]. Work on hard body models continues to the present [200, 181, 183, 88]. We will restrict ourselves to models involving a smooth potential energy function, especially those used most commonly for molecular liquids, as introduced by RAHMAN AND STILLINGER [151] and VERLET [198].

A simple gas such as argon can be described easily using a Lennard–Jones potential

$$
\varphi ( r ) = 4 \epsilon \left( \left( \frac { \sigma } { r } \right) ^ { 1 2 } - 2 \left( \frac { \sigma } { r } \right) ^ { 6 } \right) ,
$$

where $r$ is atomic separation, $\epsilon$ the well depth, and $\sigma$ is the equilibrium atomic separation.

To define a molecular system, we arrange $N$ particles in a cubic box with edges of length $L$ , with “periodic boundary conditions” imposed so that at any instant a particle with coordinates $( x , y , z )$ inside the computational domain interacts with an infinite number of periodic images obtained by adding or subtracting multiples of $L$ from each coordinate of each atom. When only short-range forces are involved, the potentials may be cut off so that particles in the computational domain do not interact with their own image. Ultimately, we are left with a system of Newton’s equations

$$
\pmb { M } \ddot { \pmb q } = \pmb { F } ( \pmb q ) : = - \nabla _ { \pmb { q } } V ( \pmb q ) ,
$$

where $M$ is the mass matrix. We typically simulate the system from some given positions and velocities $\pmb q ( t _ { 0 } ) = \pmb q _ { 0 }$ , $\dot { { \pmb q } } ( t _ { 0 } ) = \dot { { \pmb q } } _ { 0 }$ .

Positions and velocities in a molecular system represent sample points from a certain ensemble of states. Because arbitrary initial data usually correspond to an unrepresentative state for the ensemble of interest, a crucial stage in molecular simulation is the so-called “equilibration” or “thermalization” of the system, usually performed by evolving the system for some time from provided data (typically a few thousand timesteps suffice). At the end of this initial phase, the positions and velocities are taken as the starting points for a sampling trajectory.

For simple homogeneous liquids, one sometimes begins by placing the atoms on a regular “crystal lattice” and introducing random velocities of appropriate magnitude. In the case of more complicated systems such as biomolecules, the approximate structure of the system must be encoded in the position data, for example based on a computation using nuclear magnetic resonance (NMR) imaging. Again, randomized initial velocities will likely be used at the start of the equilibration phase. It is sometimes necessary for the simulator to correct certain very nonphysical initial positions and/or velocities in order to be able to get a successful initial run.

There are several key computational challenges to be addressed when computing trajectories of a Lennard–Jones fluid. First, the greater part of the computational effort involves the calculation of the $\scriptstyle { \frac { 1 } { 2 } } N ( N - 1 )$ interaction forces and potentials between pairs of atoms, even though the force acting between distant pairs is very weak. Verlet resolved this difficulty by imposing cutoffs based on distance according to which the potential is replaced by zero for atomic separations greater than a certain cutoff value $r _ { c }$ (typically $2 . 5 \sigma { - 3 . 3 \sigma } )$ . A system for keeping track of close pairs, now referred to as the Verlet table, was introduced. All distances are computed from time to time, and those pairs within distance $r _ { M }$ , $r _ { M } > r _ { c }$ , are recorded in the table. Force evaluations are limited to entries in the table. The “skin” $r _ { M } - r _ { c }$ must be chosen carefully in accordance with the temperature of simulation, typical particle speed, and frequency of updating of the Verlet table so that no particle pairs can move into the cutoff range between table updates. Other techniques are available for tracking local interactions, such as retaining linked lists of neighbor atoms for each given atom, and adjusting these lists during simulation.

In case long-ranged potentials (especially the $r ^ { - 1 }$ Coulomb potential) are involved, we must include even very distant images in the force summation. If the interaction between particles is uniform, in a box of side $L$ , then the potential energy of the system is

$$
V ( \pmb { q } ) = \sum _ { \pmb { k } } \sum _ { i < j } ^ { N } \varphi ( | | \pmb { q } _ { i } - \pmb { q } _ { j } - L \pmb { k } | | ) ,
$$

where the sum is taken over pairs of atoms $( i , j )$ and the repeating images defined by the multi-index $k$ with three integer components. Various techniques are used to simplify the computation of this infinite sum. In particular the method of fast Ewald summation computes the Coulomb potential at a point due to a periodic lattice of point charges by dividing the computation into sums over near and far terms through introduction of a smooth “screening potential” of a particular type. The sum of the screened terms converges rapidly. The complementary summation converges very rapidly if calculated instead in the Fourier domain. A scaling parameter in the screening potential allows for balancing the work done in each part of the calculation for maximal efficiency. An alternative approach, the so-called fast multipole method, is in some ways more flexible than Ewald summation since it does not depend on having an infinite periodic sum, although there are complex efficiency trade-offs between the two schemes, particularly in the context of parallel computing. Both methods are employed in MD simulations. Other methods of treating long-ranged solvent forces include implicit solvent models based on a simplified continuum description. While the development and assessment of force calculation techniques is an important area of research, it does not directly influence the time integration issues (as long as a sufficiently accurate approximation is used).

The next issue is the choice of integrator. In Chapter 4, we introduced the St¨ormer–Verlet method, a popular explicit second-order symplectic scheme and applied it to a “planar molecular system”; in fact this was one of the first used for continuous potential molecular dynamics simulation. Verlet observed in his 1967 paper, “small irregularities in the total energy” but commented that “the error is of no consequence.” What Verlet and those who followed him observed was the lack of any systematic or secular drift when the St¨ormer–Verlet method was properly implemented. We have seen similar behavior in our simulation of the planar system in Chapter 4. Given the symplecticness of the method, and our understanding of the properties of symplectic discretizations (see especially Chapter 5), it is perhaps not surprising that the St¨ormer–Verlet method achieves good conservation of energy.1 The reason that backward error analysis seems to be accurate for molecular models is probably related to the presence of the Lennard–Jones potential (or other short-ranged repulsive component of the energy); through repulsion, very close approaches of atoms are ruled out. As we shall see below, the presence of a perturbed energy function is also of dramatic importance for validating computed statistical mechanics from MD trajectories.

# 11.1 From liquids to biopolymers

During the 1970s and 1980s, work continued on MD simulations of water [151] and other molecular liquids with internal degrees of freedom. Today molecular dynamics methods are being applied routinely to simulate large flexible biomolecules.

The simple model of an MD pair potential requires a number of changes for more complicated systems. For example, the interaction between atoms of polyatomic molecules typically requires both Lennard–Jones and Coulombic terms between all atoms, not just simplified potentials between molecular centres. The potential energy function then must maintain internal geometries by including bonds (lengths, angles, and dihedral angles). This results in a more complicated molecular energy function of the form

$$
V = V _ { \mathrm { l . j . } } + V _ { \mathrm { C } } + V _ { \mathrm { l . b . } } + V _ { \mathrm { a . b . } } + V _ { \mathrm { d . b . } } + V _ { \mathrm { i . d . } } ,
$$

where $V _ { \mathrm { L . J . } }$ and $V _ { C }$ represent Lennard–Jones and Coulombic nonbonded potentials, $V _ { \left| . \mathrm { b } . \right. } , V _ { \mathrm { a } . \mathrm { b } . } , V _ { \mathrm { d } . \mathrm { b } . }$ correspond to length bonds, angle bonds, and dihedral angle bending, respectively. The latter terms consist of sums over various pairs, triples and quadruples of spatially localized groups of atoms. Table 11.1 describes the typical functional form of each term. All coefficients $\kappa _ { b } , \kappa _ { \theta } , \kappa _ { \phi }$ , and the equilibrium values $\bar { r } _ { i j }$ , $\bar { \theta } _ { i j k }$ , $\bar { \phi } _ { i j k I }$ are derived from empirical values; these coefficients may be different for each pair, triple, quadruple of atoms admitting the corresponding type of bond. (Another type of term, a so-called improper dihedral term, may also be present.)

Some of the most popular parameterizations for potentials are those provided by the software packages CHARMM, AMBER, NAMD and GROMACS.2

Because molecular simulation is concerned with very small regions of space and small time intervals, it is useful and numerically sensible to use an appropriate system of units. In practice, typical MD codes perform an internal conversion to a standard system such as the AKMA convention detailed in the following table:

AKMA Units   

<table><tr><td>length</td><td>angstrom</td></tr><tr><td>energy</td><td>kilocalorie/mole</td></tr><tr><td>mass</td><td>atomic mass unit (amu)</td></tr><tr><td>charge</td><td>electron charge e</td></tr><tr><td>time</td><td>20.455 ps</td></tr><tr><td>kB</td><td>1.987191 × 10-3</td></tr><tr><td>coulomb constant 1/(4π∈o)</td><td>3.320716 × 10²</td></tr></table>

In typical MD codes, unit conversions are performed internally.

2Because of the great volume of parameters involved in a model for even a modest molecule, it is essential to have access to a suitable software package. GROMACS and NAMD are freely distributed. Both CHARMM and AMBER are available for purchase; for academic users, the cost is relatively very modest. For CHARMM pricing and availability see the website at http://yuri.harvard.edu/. For AMBER pricing and availability, see the website at http://www.amber.ucsf.edu/amber/amber.html. For GROMACS, see http://www. gromacs.org/. For NAMD see http://www.ks.uiuc.edu/Research/namd/.

Table 11.1 Typical components of the molecular dynamics energy function.   

<table><tr><td>Nonbonded terms VL.J.</td><td>-2(</td><td></td></tr><tr><td>Vc</td><td>QiQj</td><td></td></tr><tr><td>Bonds</td><td></td><td></td></tr><tr><td>V.b. qk</td><td>(rm- 2</td><td></td></tr><tr><td>Va.b.</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>a</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>Vd.b.</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>K[1+cos(np(φijkl-φijk1)]</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

The terms in the potential energy include interactions on a broad range of spatial scales (including bonds with equilibrium length $1 \ \mathrm { \AA } { = } 1 0 ^ { - 1 0 } \ \mathrm { m }$ , as well as very long-ranged Coulombic terms). Likewise the variation of timescales is vast, ranging from rapid oscillations of the CH bond (around $1 0 ^ { - 1 4 } s $ ) to conformational changes such as the rotation or folding process of a large molecular component that may take milliseconds or even seconds. We have already learned in Chapter 2 that the numerical stability of an integrator will be limited by the fastest harmonic components (i.e., the bond stretch), which means that in molecular dynamics stepsize is limited to around a femtosecond. Much work is therefore concentrated on developing advanced multi-scale timestepping schemes (such as those we have encountered in Chapter 10), and on rapid evaluation of non-bonded forces.

The MD potential is highly nonlinear. When many terms are present, the potential surface will be very rough. If we think of dynamics in terms of the analogy of a ball rolling on a potential energy surface, then it is easy to see how the dynamics may be trapped for long intervals in highly localized regions. We have mentioned that MD is often used as a sampling device. We typically assume that MD models are ergodic, implying that all but a few special trajectories will visit the entire allowable phase space. The critical practical question for MD simulation is how long does it take for this to happen; on a highly corrugated landscape sampling may be achieved very slowly, and algorithmic devices are needed to accelerate the process. Another related problem sometimes treated using dynamics is minimization of the potential energy; this problem is also very challenging, since there are likely to be many local minima.

![](images/7519e3b87df5501e293e8edae34d7d2ff7a6346edda1c9cd924d14e0928e0a33.jpg)  
Example1 One of the most popular small models used in biomolecular simulation is the alanine dipeptide (N-Acetylalanyl-N’-Methylamide), which serves as a common test example for demonstrating enhancements in simulation methodology. The allatom model contains 22 atoms (carbon, hydrogen, nitrogen and oxygen) as described by Figure 11.1. The labels in 11.1 are those used in describing the molecule and its interactions for input to a molecular dynamics code. These labels are defined in a “PDB” (protein databank) file which gives representative atomic positions, atomic types, and linking topology of the molecule. The force field parameters are then provided automatically by the MD software. There may be slight or even substantial differences in force parameters depending on which software package is used, so care is needed in comparing numerical simulation results.   
Figure 11.1 Diagram showing atom numbers and labels for the alanine dipeptide used in a PDB file and for CHARMM simulation.

The Alanine Dipeptide exhibits many of the features characteristic of biological molecules. While the dynamics is complicated, it turns out that the study of the energy surface can be simplified by reference to two central dihedral angles ( $\dot { \psi }$ and $\phi$ corresponding to the successive atom quadruples 5-7-9-15 and 7-9-15-17 in Fig. 11.1, respectively). For each pair of dihedral values, a global constrained minimization is performed over all degrees of freedom. The resulting “reduced energies” are plotted in the lower diagram in Fig. 11.2, with three states marked by the molecular conformations corresponding to the three stable local minima.

![](images/64dbffc7e0e3d956cc6b225d683030ed026a841887cc1c3e577ea9fc796f64ad.jpg)  
Figure 11.2 Reduced energy surface for the alanine dipeptide, see text for description.

Together with the dipeptide molecule (the “solute”), one has to introduce as part of the modeling process a collection of surrounding water molecules (the “solvent”). Typically for the alanine dipeptide, this might require 500 additional water molecules. The whole system is then typically treated using periodic boundary conditions and Ewald summation for the long-ranged forces. The result is a model Hamiltonian of considerable detail with which simulations can be performed.

As an illustration, we simulate the all-atom model using CHARMM. We first “equilibrated the system” to a temperature of $3 0 0 \mathsf { K }$ by solving with a thermostat (see later in this chapter for a discussion of thermostatting). The thermostat was then turned off and constant energy simulation was performed. On the left in Fig. 1, we illustrate a short-term (2500 timestep) simulation with 1 femtosecond timesteps by plotting the trajectory of the central dihedral angles. At the energy level used, the constant energy trajectory will visit both of the two local minima near the initial point (the two left-most conformations shown in Fig. 11.2). This is illustrated by plotting snapshots every 100 timesteps of a longer (1M timestep) simulation (Fig. 1, right).

![](images/9b9491d6abb00621971487926ad57c7617b168ca4bd146756f336bc2e3cf95b2.jpg)  
Figure 11.3 Short (left) and medium-length (right) trajectories for the alanine dipeptide. See text.

The relative smoothness and simplicity of the reduced energy surface for the alanine dipeptide suggests that, if the “right” variables in a molecular system can be identified (the so-called essential degrees of freedom), then the study of molecular conformations might be made much more tractable. However, one should keep in mind that identifying essential degrees of freedom is not always so easy a task and that most biomolecules will have many more atoms than the alanine dipeptide and many more conformational states, and even the reduced energy landscape will be highly complicated. Even when, as here, the system reduces elegantly in the essential degrees of freedom, one must be cautious about the interpretations that are made regarding the “dynamics” on this surface, since no simple formula relates the slow timescale to the rapid timescales of the original system. ✷

# 11.1.1 Constraints

We have already discussed in Chapter 7 the use of constraints to remove the fastest oscillatory terms due to the presence of stiff springs with rest length. Since a bond stretch is nothing other than a stiff spring with rest length, this device is commonly used in molecular simulations. In this way, the energy function will be slightly smoothed, but it has often been argued in the molecular dynamics literature that the resulting simplification typically does not alter the dynamics appreciably on the timescales used in current simulation practice. However some caution must be exercised with regard to the thermodynamic equilibrium behavior as has been first pointed out by FIXMAN [61].

See the Exercises for an example of using SHAKE in the molecular modeling context.

# 11.2 Statistical mechanics from MD trajectories

Given the small size of any atom, it is not obvious that simulating an atomic system consisting of several thousands or millions of particles can provide useful information about even the smallest realistic system. Only when the principles of statistical mechanics are brought into play can we extrapolate from the tiny simulated system to that of a much larger aggregate. Statistical mechanics begins with the identification of an appropriate density or ensemble of states with respect to which all averages are computed. The key premise is that any given state is representative of a continuum of similar states, and that the probability of finding the system in any given region $R$ of phase space at any arbitrary instant can be viewed as proportional to an integral of the provided density over $R$ .

We will assume that any individual motion in the system is governed by a Hamiltonian $H$ . In general, we expect the density to be invariant under the evolution of the system, so that $\rho$ is a steady state of the Liouville equation, i.e.

$$
\frac { d \rho } { d t } = \{ \rho , H \} = \nabla _ { q } \rho \cdot \nabla _ { p } H - \nabla _ { p } \rho \cdot \nabla _ { q } H .
$$

One way, and in the generic case the only way, to guarantee this is to demand that $\rho$ be a function of $H$ .

In general several parameters must be chosen to define the characteristics of the system. One approach is to fix the number $N$ of atoms and assume that these atoms comprise an isolated system which evolves in a fixed volume in space. While evidently unrealistic from a physical point of view, this finite model provides the simplest framework for simulation on a computer. (The restriction to a finite volume is achieved most readily by the use of periodic boundary conditions as mentioned previously, which introduces a modification of the potential energy function.) Because the system is isolated, its evolution is completely defined by the system Hamiltonian and the energy is a constant of motion. We still must define a suitable density. Since the density is to be a function of energy and the energy is a constant of motion, it seems that a natural choice for the density in these circumstances is

$$
\rho _ { \mathrm { m i c r o c a n o n i c a l } } = \delta [ H - E ] ,
$$

which, when normalized, implies that the relative likelihood of finding the system in a given bounded measurable subset of the energy surface $H \ = \ E$ is proportional to the corresponding surface area. Because this approach relies on the assumptions of constant particle number $N$ , volume $V$ , and energy $E$ we typically refer to it as the NVE ensemble. It is also commonly termed the microcanonical ensemble.

A more realistic assumption than constant energy is that our finite system is continually exchanging energy with a larger bath of atoms at a fixed temperature.

The instantaneous temperature of a molecular system with $N$ atoms is defined by

$$
T _ { \mathrm { i n s t } } : = \frac { 1 } { 3 k _ { B } N } \sum _ { i = 1 } ^ { N } m _ { i } \| \mathbf { v } _ { i } \| ^ { 2 } .
$$

The canonical ensemble assumes the density

$$
\rho _ { \mathsf { c a n o n i c a l } } = \exp ( - { \frac { 1 } { k _ { B } T } } H ) = : \exp ( - \beta H ) .
$$

Here $k _ { B }$ is Boltzmann’s constant, $\tau$ represents the fixed temperature of the bath, and $\beta = 1 / k _ { B } T$ . Again, the number of particles $N$ and the volume of the system $V$ are fixed, but the energy is now allowed to fluctuate. (The precise justification for the exponential function is due to Gibbs and is based on a simplified kinetic theory.) Whereas simulating the dynamics of a system in the microcanonical ensemble requires nothing more than numerical integration of the Hamiltonian system, the NVT ensemble demands some sort of stochastic or dynamic mechanism to model the effect of the bath. We will return to this issue momentarily. Note that just because the temperature of the environment is assumed to be fixed, it does not imply that $T _ { \mathrm { i n s t } }$ is constant. Rather, this quantity, which is a function of the $N$ variables of the system, will fluctuate along trajectories, although its long-term average will tend to $\tau$ .

Some other examples of useful ensembles include the NPT (constant pressure, temperature and particle number) ensemble and the grand canonical ensemble (in which both energy and particle number are allowed to fluctuate). It is also possible to work with a more general density. In some cases, generalized ensembles are introduced based on physical arguments; in other instances they may be used as modeling devices to increase the sampling rate in phase space.

In defining statistical mechanics as we have done here, we make several assumptions about the Hamiltonians involved, in particular that the energy is bounded below and that the total integral of the density function is bounded. An important assumption we commonly make about a physical model is that averages taken along trajectories reproduce the appropriate ensemble average. This is what is meant by ergodicity: that a typical trajectory will eventually visit all states with $\rho > 0$ . If we treat a system in the NVE ensemble, then we can infer that the energy is constant, but we cannot necessarily infer that all possible states on the constant energy surface will be reachable from any particular state. For small systems, it is common to find periodic orbits or quasi-periodic tori motion that restrict a typical trajectory to a small portion of phase space; more generally, the presence of strong potentials such as those due to harmonic bonds may introduce barriers which similarly confine trajectories. If ergodicity is assumed, however, then we can use trajectories as sampling devices, simply averaging a given quantity along the computed dynamics to obtain ensemble averages.

# 11.2.1 Ensemble computations

As we have stated, the typical use made of molecular simulation is to compute averages with respect to the underlying density. Examples of such computations include finding the internal energy, spatial extent, or the time constants associated with local relaxation of a perturbation. We will denote the average of some function $A ( \pmb q , \pmb p )$ with respect to the NVE ensemble for a given Hamiltonian $H$ by $\langle A \rangle _ { \mathsf { N V E } } ^ { H }$ , and use similar notation for other averages. Under the ergodicity assumption, a macroscopic quantity, which for real systems could be observed or measured, can be thought of as a long-time average $\bar { A } ( \tau )$ , $\tau \gg 1$ , of some (instantaneous) function $A ( t ) = A ( \pmb q ( t ) , \pmb p ( t ) )$ which depends on the collective position and velocity at time $t$ . The temporal average is defined as

$$
\langle A \rangle : = \operatorname* { l i m } _ { \tau \to \infty } \bar { A } ( \tau ) = \operatorname* { l i m } _ { \tau \to \infty } \frac { 1 } { \tau } \int _ { 0 } ^ { \tau } A ( \pmb { q } ( t ) , \pmb { p } ( t ) ) \ d t .
$$

Ergodicity in the NVE ensemble now becomes equivalent to the statement that $\langle A \rangle = \langle A \rangle _ { \mathsf { N V E } } ^ { H }$ .

In practice, trajectories are computed at a large finite number of discrete times $\tau _ { 1 } , \dots , \tau _ { N }$ , in which case the integral is replaced by a (finite) discrete sum.

Some macroscopic quantities of interest are collected in Table 11.2. In this table, the Boltzman constant is denoted $k _ { B }$ , and instantaneous temperature $\tau$ is proportional to kinetic energy and is defined as in (11.3). Specific heat at constant volume measures the rate of change of temperature due to a change in energy. The velocity autocorrelation function measures how the velocities at time $t$ are related to velocities at a later time $t + \tau$ . The pair correlation function, or radial distribution function for a system of particles with volume $V$ , gives the number of particles $n ( r )$ situated at a distance between $r$ and $r + \Delta r$ from another particle. The mean square displacement $R ( \tau )$ measures average atomic fluctuations over time windows of length $\tau$ . With $t = 0$ , the value of $\tau$ at which $R$ ceases to change significantly can be understood as the time required for a simulated system to achieve equilibrium. The diffusion coefficient $D$ is proportional to the slope of $R ( \tau )$ over long times via the Einstein relation given in Table 11.2. More details for computing these quantities can be found in ALLEN AND TILDESLEY [4], RAPPAPORT [152], and FRENKEL AND SMIT [66].

Specific heat at constant volume

$$
C _ { V } = \left[ \frac { 2 } { 3 N } - \frac { 4 } { 9 } \frac { \langle ( T - \langle T \rangle ) ^ { 2 } \rangle } { \langle T \rangle ^ { 2 } } \right] ^ { - 1 } k _ { B }
$$

Velocity autocorrelation function

$$
Z ( \tau ) = \left. \frac { 1 } { N } \mathbf { \boldsymbol { v } } ( . ) \cdot \mathbf { \boldsymbol { v } } ( . + \tau ) \right.
$$

Pair correlation function (radial distribution function)

$$
g ( r , \Delta r ) = \left. \frac { V } { N } \frac { n ( r ) } { ( 4 \pi r ^ { 2 } \Delta r ) } \right.
$$

Mean square displacement after time $\tau$

$$
R ( \tau ) = \left. \frac { 1 } { N } \sum _ { i = 1 } ^ { N } ( r _ { i } ( . + \tau ) - r _ { i } ( . ) ) ^ { 2 } \right.
$$

Diffusion coefficient, $D$ ,

$$
2 \tau D = \frac { 1 } { 3 } R ( \tau )
$$

# 11.3 Dynamical formulations for the NVT, NPT and other ensembles

Some modification of the dynamical system (or the introduction of a stochastic perturbation) is necessary to make the dynamics sample the other ensembles, for example the canonical one. There are many ways to do this, but the most popular techniques are Nos´e dynamics and Langevin dynamics. In Langevin dynamics, the combination of a damping force and a stochastic term maintains the system at a given temperature. (The stochastic component models the interactions with a temperature bath; the damping simulates the transfer of energy to the bath.)

The dynamics take the form

$$
{ \pmb M } \ddot { \pmb q } = - \nabla _ { \pmb q } V ( \pmb q ) + { \pmb R } ( t ) - \gamma \dot { \pmb q } ,
$$

where the dissipation rate $\gamma$ and the vector $R ( t )$ of white noise processes are linked via the fluctuation–dissipation relation. Because of the presence of damping and the introduction of a random forcing, the dynamics are not any longer Hamiltonian. As the geometric integration of stochastic differential equations is beyond the scope of the current text (and indeed still at a preliminary stage of development compared with the deterministic theory), we consider rather alternatives which compute trajectories in the canonical ensemble from a modified continuous dynamics.

NOSE [146] proposed to augment the phase space by an additional variable $S$ and its canonical momentum $\pi _ { s }$ , and to work with the extended Hamiltonian

$$
{ \mathcal H } _ { \sf N o s e } = H ( { \bf q } , \tilde { p } / s ) + \frac { \pi _ { s } ^ { 2 } } { 2 Q } + g \beta ^ { - 1 } | { \sf n } s .
$$

Here $\beta = 1 / k _ { B } T$ and $g = N _ { f } + 1$ , where $N _ { f }$ is the number of degrees of freedom of the real system (typically $N _ { f } = 3 N$ , where $N$ is the number of atoms, but this may be reduced if constraints are present). The constant $Q$ represents an artificial “mass” associated with $S$ . One should note that $\tilde { p }$ is the canonical momenta associated with the position variable, $\pmb q$ . The tilde is used to distinguish it from the from the real momenta given by $p = \tilde { p } / s$ .

To understand how Nos´e’s extended Hamiltonian yields canonical averages, we consider the following sequence of calculations.

1. From elementary calculus, we know that for any $^ { a }$ , the following holds

$$
e ^ { - a } = \int _ { 0 } ^ { \infty } \delta [ a + \mathsf { I n } s ] d s .
$$

Since here and below, all integration is over the entire real line, we will suppress the limits and simply write

$$
e ^ { - a } = \int \delta [ a + \mathsf { I n } s ] d s .
$$

2. A very slight generalization results in

$$
e ^ { - \beta H ( q , p ) } = \beta \int \delta [ H ( q , p ) + \beta ^ { - 1 } \ln s ] d s .
$$

3. We can also include a power of $s$ outside the $\delta$ -function, as in

$$
e ^ { - \beta H ( q , p ) } = \frac { \beta } { g } \int \delta [ H ( q , p ) + g \beta ^ { - 1 } \ln s ] s ^ { g - 1 } d s .
$$

4. Note that for a scalar function $h ( x )$ of an $N _ { f }$ -vector $x$ , we have, via change of variables,

$$
\iint \ldots \int h ( \tilde { x } / s ) d \tilde { x } _ { 1 } d \tilde { x } _ { 2 } \ldots d \tilde { x } _ { N _ { f } } = \iint \ldots \int s ^ { N _ { f } } h ( x ) d x _ { 1 } d x _ { 2 } \ldots d x _ { N _ { f } } .
$$

Again, the integration is over all real space. We introduce another shorthand at this point, writing, simply,

$$
\int h ( \tilde { x } / s ) d ^ { N _ { f } } \tilde { x } = \int s ^ { N _ { f } } h ( x ) d ^ { N _ { f } } x .
$$

As a consequence, we may write:

$$
\int A ( q , p ) \ e ^ { - \beta H ( q , p ) } \ d ^ { N _ { f } } p = { \frac { \beta } { g } } \int \int A ( q , \tilde { p } / s ) \delta [ H ( q , \tilde { p } / s ) + g \beta ^ { - 1 } \ln s ] \ d ^ { N _ { f } } \tilde { p } \ d \tilde { q } \ .
$$

where, as before, $g = N _ { f } + 1$ .

5. Finally, we note that

$$
\begin{array} { r } { \displaystyle \int \int A ( \boldsymbol { q } , \tilde { p } / s ) \delta [ H ( \boldsymbol { q } , \tilde { p } / s ) + g \beta ^ { - 1 } \ln s ] d ^ { N _ { f } } \tilde { p } d s = } \\ { \displaystyle C \int \int A ( \boldsymbol { q } , \tilde { p } / s ) \delta [ \mathcal { H } _ { \sf N o s e } - E ] d ^ { N _ { f } } \tilde { p } d \pi _ { s } d s , } \end{array}
$$

where $C$ is a constant, and $E$ is the pseudo-energy level. It follows that the NVE ensemble average for the Hamiltonian (11.4) is equivalent to the canonical NVT ensemble for the original system with Hamiltonian $H$ in the following sense:

$$
\langle A ( \pmb q , \tilde { \pmb p } / s ) \rangle _ { \sf N V E } ^ { \mathcal { H } _ { \sf N o s e } } = \langle A ( \pmb q , \pmb p ) \rangle _ { \sf N V T } ^ { H } .
$$

The conclusion is that trajectories of the Nos´e extended Hamiltonian generate canonically distributed averages, given assumptions of equal a priori probabilities and ergodicity, hence Nos´e dynamics can be used for canonical sampling. The Nos´e formulation is the starting point for numerical schemes for realizing the canonical ensemble from trajectories, but it is not yet clear precisely how the extended Hamiltonian dynamics are related to the those of the original system. We take up this issue in the next subsections.

# 11.3.1 Coordinate transformations: the separated form

Consider first a canonical Hamiltonian of the form

$$
H = a ( \pmb q ) \frac { \pmb p ^ { T } \pmb M ^ { - 1 } \pmb p } { 2 } + V ( \pmb q ) ,
$$

where a is a positive scalar-valued function of position $q , \ V$ is a potential and $M$ is a mass matrix. Introducing a Poincar´e type time transformation, we can reduce (11.5) to mechanical form

$$
\hat { H } = \frac { H - E } { a ( \pmb q ) } = \frac { { \pmb p } ^ { T } { \pmb M } ^ { - 1 } { \pmb p } } { 2 } + \frac { V ( \pmb q ) - E } { a ( \pmb q ) } ,
$$

where $E$ is a constant representing the value of the energy integral along a given trajectory. The problem of separating the variables in the Hamiltonian therefore means finding a change of variables to the form (11.5).

While we cannot flatten out just any metric using such simple coordinate and time transformations, it is possible to do this neatly for Nos´e dynamics. First replace $s$ by its logarithm, also modifying the momentum to make the transformation canonical:

$$
\begin{array} { r } { \theta = \mathsf { I n } s , \qquad \pi _ { s } = \mathsf { e x p } ( - \theta ) \pi _ { \theta } . } \end{array}
$$

We then follow with a rescaling of time by $e ^ { 2 \theta }$ , so that the Hamiltonian becomes

$$
\hat { H } = \frac { p ^ { T } M ^ { - 1 } p } { 2 } + \frac { \pi _ { \theta } ^ { 2 } } { 2 Q } + e ^ { 2 \theta } ( V ( \pmb q ) + g \beta ^ { - 1 } \theta - E ) .
$$

Because the transformation is canonical, it is also area preserving, and it can be shown that the averages of functions of $\pmb q$ and $p / s$ are not disturbed.

The elementary form of the separated Hamiltonian can simplify the interpretation of Nos´e dynamics. With $g / \beta$ replaced by an arbitrary positive parameter $\gamma$ , we can define an “isothermal potential” by

$$
\tilde { V } ( \pmb { q } , \theta ) = e ^ { 2 \theta } ( \gamma \theta + V ( \pmb { q } ) - E ) .
$$

This has stationary points $( { \bar { q } } , { \bar { \theta } } )$ , where $\bar { \pmb q }$ is a stationary point of $V$ and $\bar { \theta } =$ $( E - V ( \bar { q } ) ) / \gamma - 1 / 2$ . The stability is determined from the original system. A stable center in the original mechanical system is thus mapped to a corresponding stable center in the constant temperature dynamics.

Due to the shift of energy in the Poincar´e transformation, all motion takes place on the zero-energy surface of the Nos´e Hamiltonian. Since the kinetic energy is everywhere non-negative, the entire range of negative isothermal potential energy will be explored. For a fixed value of $\theta$ , the new potential is a shift and scaling of the original potential. For positive $\theta$ , the motion in a bounded potential is uniformly bounded, while in principle the dynamics may make very long excursions in the negative $\theta$ direction. With $\theta = 0$ we have $\tilde { V } ( \pmb { q } , 0 ) = V ( \pmb { q } ) - E$ , and

![](images/a2e3ec7b2c7a8c33ffbfaf218e171a46f927cc5514c4a23e65377721322b7b36.jpg)  
Figure 11.4 “Isothermal” potential surface corresponding to the double well potential at small (left) and large (right) values of $r$ .

$$
\operatorname* { l i m } _ { \theta \to + \infty } \tilde { V } ( \pmb q , \theta ) = + \infty , \qquad \operatorname* { l i m } _ { \theta \to - \infty } \tilde { V } ( \pmb q , \theta ) = 0 .
$$

The modified potential has a unique global minimum in $\theta$ , so the modified potential can be viewed as a “valley” with sides rising in $\theta$ .

Let us illustrate this with the example of a double well potential

$$
V ( q ) = q ^ { 2 } ( q - 1 ) ^ { 2 } .
$$

In the constant energy dynamics, low energy orbits are automatically confined to one or the other of the two energy wells. The isothermal system does not exhibit such a separation, but the transition between wells becomes rare at low temperature. See Fig. 11.4.

# 11.3.2 Time-reparameterization and the Nos´e–Hoover method

The Nos´e Hamiltonian generates configurations from the canonical distribution, but it also introduces an unnatural scaling of the intrinsic time. This introduces some practical computational difficulties, since the configurations are not available at equally spaced points in real time. A similar problem is encountered when the separated formulation is used as the basis for computation, as described above. An alternative real-variable reformulation of the equations of motion was proposed by NOSE [146] which incorporates a time transformation. Simplifications to the real-variable system were suggested by HOOVER [87] resulting in the traditional treatment of the Nos´e Hamiltonian called the Nos´e–Hoover method. Let us briefly review the properties of the Nos´e–Hoover system of equations, and discuss some of the common numerical methods.

The Nos´e Hamiltonian generates the equations of motion

$$
\begin{array} { r l } & { \frac { d q _ { i } } { d \tau } = \frac { \tilde { p } _ { i } } { m _ { i } s ^ { 2 } } , } \\ & { \frac { d s } { d \tau } = \frac { \pi _ { s } } { Q } , } \\ & { \frac { d \tilde { p } _ { i } } { d \tau } = - \nabla _ { q _ { i } } V ( q ) , } \\ & { \frac { d \pi _ { s } } { d \tau } = \sum _ { i } \frac { \| \tilde { p } _ { i } \| ^ { 2 } } { m _ { i } s ^ { 3 } } - \frac { \beta ^ { - 1 } g } { s } . } \end{array}
$$

The following change of variables can be applied

$$
p _ { i } = \frac { \tilde { p } _ { i } } { s } \qquad \pi = \pi _ { s } / s .
$$

This is followed by a time-transformation, $\begin{array} { r } { \frac { d \tau } { d t } = s } \end{array}$ yielding the non-Hamiltonian system in terms of the “real” variables

$$
\begin{array} { l } { { \displaystyle { \dot { q } _ { i } = \frac { p _ { i } } { m _ { i } } } , } } \\ { { \displaystyle { \dot { p } _ { i } = - \nabla _ { q _ { i } } V ( q ) - p _ { i } \frac { s \pi } { Q } } , } } \\ { { \displaystyle { \dot { s } = \frac { s ^ { 2 } \pi } { Q } } , } } \\ { { \displaystyle { \dot { \pi } = \frac { 1 } { s } \left( \sum _ { i } \frac { \| p \| _ { i } ^ { 2 } } { m _ { i } } - \beta ^ { - 1 } g \right) - \frac { s \pi ^ { 2 } } { Q } } . } } \end{array}
$$

Introducing $\xi = s \pi / Q$ and replacing ln $S$ by $\eta$ , one not only eliminates the variable $\pi$ , but also decouples the variable $S$ from the system; this yields the Nos´e–Hoover formulation:

$$
\begin{array} { l } { \displaystyle \dot { q } _ { i } = \frac { p _ { i } } { m _ { i } } , } \\ { \displaystyle \dot { p } _ { i } = - \nabla _ { q _ { i } } V ( q ) - p _ { i } \xi , } \\ { \displaystyle \dot { \eta } = \xi , } \\ { \displaystyle \dot { \xi } = \frac { 1 } { Q } \left( \sum _ { i } \frac { p _ { i } ^ { 2 } } { m _ { i } } - \beta ^ { - 1 } g \right) . } \end{array}
$$

Canonical sampling in Nos´e–Hoover can be shown to require $g = N _ { f }$ (the number of degrees of freedom of the real system). This reduction in the degrees of freedom is needed to recover configurations at the correct temperature. Although

this system is not Hamiltonian, it does have a conserved quantity, the total extended energy

$$
E _ { e x t } = \sum _ { i } \frac { \| \pmb { p } \| _ { i } ^ { 2 } } { 2 m _ { i } } + V ( \pmb { q } ) + \frac { Q \xi ^ { 2 } } { 2 } + g \beta ^ { - 1 } \eta .
$$

This system is time reversible, and it is advisable to solve the equations of motion with a reversible integrator. A number of schemes are available, for example: [66, 126, 94].

# 11.4 A symplectic approach: the Nos´e–Poincar´e method

We introduce two different kinds of error when calculating an ensemble average using a molecular dynamics sampling technique. First, every timestepping scheme introduces some error at each timestep, and these accumulate in a complicated way. Second, the calculation of stochastic quantities from simulation is generally a slow-converging process, so very large numbers of timesteps will often be needed to deliver good estimates. Indeed, in systems with a large number of local minima, we may need to greatly restrict the space over which our trajectories sample in order to achieve any sort of useful estimates at all.

In the most general setting, there is also not much we can say about the effect of the numerical error on the ensemble calculation, other than that if we use an off-the-shelf integrator, we expect the error to grow fairly rapidly with time. Methods which do not stay near the energy surface very soon lead to unrealistic averages. On the other hand, is it enough for the integrator to preserve energy approximately in order for us to trust the averages? The answer is of course, no: in the simplest case, we could think of using any arbitrary method projected on to the energy surface. We could apply this scheme in conjunction with any arbitrary method to obtain perfect energy conservation, but it would not generally be effective. For example if the method introduced dissipation, causing trajectories to spiral towards equilibria, we would expect to see similar artifacts in the projected method’s dynamics.

If we use a symplectic method, we usually expect good energy conservation, but something else comes into play. There is also an associated perturbed statistical mechanics – a consequence of the Hamiltonian structure of the modified equations! Thus a symplectic scheme not only stays near the modified energy surface $\tilde { H } _ { \Delta t }$ , it allows us the possibility of computing averages in a modified microcanonical ensemble, for example $\dot { \delta } \left[ \tilde { H } _ { \Delta t } - \dot { E } \right]$ . Does this idea carry over to Nos´e dynamics? If we solve the Nos´e system at constant energy using a symplectic method, then what we are actually able to compute (assuming ergodicity) is a sampling with respect to a modified microcanonical ensemble of the form

$$
\rho _ { \mathsf { N V E } } ^ { \tilde { \mathcal { H } } _ { \Delta t } } = \delta \left[ \mathcal { H } _ { \mathsf { N } o s \epsilon } + \Delta t ^ { 2 } \Delta \mathcal { H } _ { 2 } + \ldots - E \right] .
$$

In order to move things forward we must show how to complete each of the steps described in the proof of Nos´e dynamics of integrating out the variables $S$ and $\pi _ { s }$ on which the above density depends, resulting in a modified canonical distribution. This introduces some new challenges, since all transformations involved must be global, and it is difficult to say anything about the perturbative expansion far from the trajectory of interest. However if we are willing to assume that trajectories of our system stay uniformly bounded for all time, then it is possible to invoke the implicit function theorem, which allows us to compute the integral over s as in the proof of Nos´e’s theorem, and using this we can show that the effective combination of Nos´e dynamics and symplectic discretization is real variable sampling of a modified canonical ensemble of the form $\exp ( - \beta \tilde { H } _ { \Delta t } )$ . This viewpoint is addressed in [25]. This perspective offers concrete motivation for using a symplectic method, since for bounded systems, at least, the symplectic property is crucial for establishing effective sampling.

Note that the separated formulation makes possible a very simple symplectic discretization of Nos´e dynamics based on St¨ormer–Verlet, see [110]. However, although the method of implementation is trivial, the computation of autocorrelation functions typically requires data equally spaced in time, and since the separated form works in an artificial timescale, this requires some interpolation. It simplifies things to work with a scheme that is formulated in real time.

In this section we will outline a procedure for scaling time while preserving the Hamiltonian structure. The method used here was first given in [26]. We have already seen in the separable formulation (and earlier in the context of variable stepsize) that a time transformation can be implemented as a rescaling of the Hamiltonian of the system, shifted to zero

$$
{ \tilde { \mathcal { H } } } = f ( q , p ) ( H - E ) ,
$$

where $f > 0$ is a “time scaling” function, and the constant $E$ is the initial value of $H$ along a trajectory of interest. With $H = E$ , the dynamics of the transformed system will be equivalent to those of the original system, up to a transformation of time $d t / d t ^ { \prime } = f$ .

In order to correct the Nos´e timescale, the appropriate Poincar´e transformation is $d t / d t ^ { \prime } = s$ , applied to a slightly modified version of the Nos´e extended Hamiltonian in (11.4)

$$
\tilde { \mathcal { H } } = \left( \sum _ { j } \frac { \| \tilde { { \pmb { p } } } _ { i } \| ^ { 2 } } { 2 m _ { i } s ^ { 2 } } + V ( { \pmb q } ) + \frac { \pi _ { s } ^ { 2 } } { 2 Q } + g \beta ^ { - 1 } \ln s - E \right) s .
$$

The modification comes in that we must take the constant $g = N _ { f }$ (as opposed to $\tilde { g } = N _ { f } + 1 ,$ ), as in Nos´e–Hoover. The constant $E$ is chosen to be the initial value of the Nos´e Hamiltonian, $\mathcal { H } _ { \mathsf { N o s e } }$ . It is not difficult to show that this transformed Hamiltonian (11.13), which we call Nos´e–Poincar´e, generates configurations from the canonical distribution in the variables $\pmb q$ and $\tilde { p } / s$ , see [26] for details.

The disadvantage of the general Poincar´e transformation in (11.12) is that it mixes the variables so that a straightforward explicit symplectic treatment of the extended Hamiltonian is not, in general, possible. However, the fact that the scaling function $f$ depends only on $s$ means that the discrete equations can often be decoupled, and we can easily formulate semi-explicit symplectic methods.

Returning to the Nos´e–Poincar´e Hamiltonian, $\tilde { \mathcal { H } }$ , we write the equations of motion

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } q _ { i } = \frac { \tilde { p } _ { i } } { m _ { i } s } , } \\ { \displaystyle \frac { d } { d t } \tilde { p } _ { i } = - s \nabla _ { q _ { i } } V ( q ) , } \\ { \displaystyle \frac { d s } { d t } = s \frac { \pi _ { s } } { Q } , } \\ { \displaystyle \frac { d \pi _ { s } } { d t } = \sum _ { j } \frac { \| \tilde { p } _ { i } \| ^ { 2 } } { m _ { i } s ^ { 2 } } - g \beta ^ { - 1 } - \Delta \mathcal { H } \left( q , \tilde { p } , s , \pi _ { s } \right) , } \end{array}
$$

where

$$
\Delta \mathcal { H } \left( \pmb { q } , \widetilde { \pmb { p } } , s , \pi _ { s } \right) = \sum _ { i } \frac { \| \widetilde { \pmb { p } } _ { i } \| ^ { 2 } } { 2 m _ { i } s ^ { 2 } } + V ( \pmb { q } ) + \frac { \pi _ { s } ^ { 2 } } { 2 Q } + g \beta ^ { - 1 } \ln { s } - E .
$$

The value of $E$ is chosen such that $\Delta \mathcal { H } \left( \pmb q ( 0 ) , \tilde { \pmb p } ( 0 ) , s ( 0 ) , \pi _ { s } ( 0 ) \right) = 0$ . We apply to this the generalized leapfrog algorithm (see Chapter 4). Since we are treating a time-reversible Hamiltonian system, the resulting method is symplectic and time reversible

$$
\begin{array} { l } { { \displaystyle { \bar { p } } _ { i } ^ { n + 1 / 2 } = { \bar { p } } _ { i } ^ { n } - \frac { \Delta t } { 2 } s ^ { n } \nabla _ { q } V ( q ^ { n } ) } , } \\ { { \displaystyle \pi _ { s } ^ { n + 1 / 2 } = \pi _ { s } ^ { n } + \frac { \Delta t } { 2 } \left( \sum _ { i } \frac { 1 } { m _ { i } } \left( \frac { \| { \bar { p } } _ { i } ^ { n + 1 / 2 } \| } { s ^ { n } } \right) ^ { 2 } - g \beta ^ { - 1 } \right) } } \\ { ~ - \frac { \Delta t } { 2 } \Delta \mathcal { H } \left( q ^ { n } , \bar { p } ^ { n + 1 / 2 } , s ^ { n } , \pi _ { s } ^ { n + 1 / 2 } \right) , }  \\ { { \displaystyle s ^ { n + 1 } = s ^ { n } + \frac { \Delta t } { 2 } \left( s ^ { n + 1 } + s ^ { n } \right) \frac { \pi _ { s } ^ { n + 1 / 2 } } { Q } } , } \\ { { \displaystyle q _ { i } ^ { n + 1 } = q _ { i } ^ { n } + \frac { \Delta t } { 2 } \left( \frac { 1 } { s ^ { n + 1 } } + \frac { 1 } { s ^ { n } } \right) \frac { \bar { p } _ { i } ^ { n + 1 / 2 } } { m _ { i } } } , } \end{array}
$$

$$
\begin{array} { l } { \displaystyle \pi _ { s } ^ { n + 1 } = \pi _ { s } ^ { n + 1 / 2 } + \frac { \Delta t } { 2 } \left( \sum _ { i } \frac { 1 } { m _ { i } } \left( \frac { \lVert \tilde { p } _ { i } ^ { n + 1 / 2 } \rVert } { s ^ { n + 1 } } \right) ^ { 2 } - g \beta ^ { - 1 } \right) } \\ { \displaystyle - \frac { \Delta t } { 2 } \Delta \mathcal { H } \left( q ^ { n + 1 } , \tilde { p } ^ { n + 1 / 2 } , s ^ { n + 1 } , \pi _ { s } ^ { n + 1 / 2 } \right) , } \\ { \displaystyle \tilde { p } _ { i } ^ { n + 1 } = \tilde { p } _ { i } ^ { n + 1 / 2 } - \frac { \Delta t } { 2 } s ^ { n + 1 } \nabla _ { q _ { i } } V ( q ^ { n + 1 } ) . } \end{array}
$$

Solving (11.16) requires us to find the roots of a quadratic equation for $\pi _ { s } ^ { n + 1 / 2 }$

$$
\frac { \Delta t } { 4 Q } \left( \pi _ { s } ^ { n + 1 / 2 } \right) ^ { 2 } + \pi _ { s } ^ { n + 1 / 2 } + \delta = 0 ,
$$

where

$$
\delta = \frac { \Delta t } { 2 } \left( g \beta ^ { - 1 } \left( 1 + \ln s ^ { n } \right) - \sum _ { i } \frac { \left( \tilde { p } _ { i } ^ { n + 1 / 2 } \right) ^ { 2 } } { 2 m _ { i } \left( s ^ { n } \right) ^ { 2 } } + V ( \pmb { q } ^ { n } ) - E \right) - \pi _ { s } ^ { n } .
$$

To avoid subtractive cancellation, we use the following quadratic formula to solve (11.21)

$$
\pi _ { s } ^ { n + 1 / 2 } = \frac { - 2 \delta } { 1 + \sqrt { 1 - \delta \Delta t / Q } } .
$$

The remaining steps of the method are explicit.

# 11.4.1 Generalized baths

In [102], an alternative to Nos´e dynamics is proposed based on a more powerful family of extended Hamiltonians. By examination of the proof that Nos´e dynamics recovers the canonical ensemble, we can observe that also the following Hamiltonian would have this property

$$
{ \mathcal H } _ { G N } = H ( \pmb q , \tilde { \pmb p } / s ) + g \beta ^ { - 1 } \ln s + G ( \pi _ { s } , \sigma _ { 1 } , \sigma _ { 2 } , \dots , \sigma _ { k } , \pi _ { 1 } , \pi _ { 2 } , \dots , \pi _ { k } ) ,
$$

Here new configuration variables $\sigma _ { 1 } , \sigma _ { 2 } , \ldots , \sigma _ { k }$ and the corresponding momenta $\pi _ { 1 }$ $1 , \pi _ { 2 } , \ldots , \pi _ { k }$ represent augmenting variables designed to (i) increase the rate of convergence to the canonical ensemble, or (ii) enable the bath to resonate with several components of the Hamiltonian system. It is possible to show that, under certain assumptions, the constant energy trajectories of the generalized bath Hamiltonian sample the canonical ensemble. The precise form of the term $G$ will be important both for the dynamical behavior and for the issues of numerical integrator design. However, there are some limitations on the choice of $G$ , as illustrated in the following examples.

Example 2 Nosé-Hoover chains are often used to enhance ergodicity. The idea is to introduce additional thermostatting variables which successively “thermostat the thermostats.” It is natural to look for a Hamiltonian formulation of Nos´e–Hoover chains, such as

$$
\begin{array} { l } { \displaystyle { \mathcal { H } } _ { \mathrm { c h a i n } } = H ( \pmb { q } , \widetilde { \pmb { p } } / s ) + \frac { \pi _ { s } ^ { 2 } } { 2 s _ { 1 } ^ { 2 } Q } + \frac { \pi _ { 1 } ^ { 2 } } { 2 s _ { 2 } ^ { 2 } Q _ { 1 } } + . . . + \frac { \pi _ { r - 1 } ^ { 2 } } { 2 s _ { r } ^ { 2 } Q _ { r - 1 } } + \frac { \pi _ { r } ^ { 2 } } { 2 Q _ { r } } } \\ { \displaystyle + g \beta ^ { - 1 } \ln s + g _ { 1 } \beta ^ { - 1 } \ln s _ { 1 } + . . . g _ { r } \beta ^ { - 1 } \ln s _ { r } , } \end{array}
$$

which is clearly in the form (11.23).

Take the case $r = 1$ , in which case the microcanonical partition function is

$$
\begin{array} { l } { { \displaystyle { \mathcal P } = \int \delta [ \mathcal { H } _ { \mathrm { c h a i n } } - E ] d \tilde { V } d s d s _ { 1 } d \pi _ { s } d \pi _ { 1 } } } \\ { { \displaystyle \quad = \int \delta [ H ( \boldsymbol { q } , \tilde { \boldsymbol { p } } / s ) + \frac { \pi _ { s } ^ { 2 } } { 2 S _ { 1 } ^ { 2 } Q } + \frac { \pi _ { 1 } ^ { 2 } } { 2 Q _ { 1 } } + g \beta ^ { - 1 } | { \mathrm n } s + g _ { 1 } \beta ^ { - 1 } | { \mathrm n } s _ { 1 } - E | d \tilde { V } d s d s _ { 1 } d \pi _ { s } d \pi _ { 1 }  } } \end{array}
$$

where $d { \tilde { V } } = d ^ { N _ { f } } q d ^ { N _ { f } } { \tilde { p } }$ is the volume form in phase space. We attempt now to integrate out with respect to $S _ { 1 }$ . Set $\pi _ { s } / s _ { 1 } = \bar { \pi }$ , so $d \pi = s _ { 1 } d \bar { \pi }$ and

$$
\begin{array} { l } { \displaystyle { \mathrm {  ~ \beta ~ } = \int \delta [ H ( \boldsymbol { q } , \tilde { p } / s ) + \frac { \bar { \pi } ^ { 2 } } { 2 Q _ { 0 } } + \frac { \pi _ { 1 } ^ { 2 } } { 2 Q _ { 1 } } + g \beta ^ { - 1 } | { \mathrm {  ~ n ~ } } s + g _ { 1 } \beta ^ { - 1 } | { \mathrm {  ~ n ~ } } s _ { 1 } - E | s _ { 1 } d \tilde { V } d s d s _ { 1 } d \bar { \pi } d \pi _ { 1 } + g \beta ^ { - 1 } | { \mathrm {  ~ n ~ } } s _ { 0 } | ] d s } } \end{array}
$$

This yields, for $g _ { 1 } = 2$

$$
\mathcal { P } = \int \exp \left( - \beta \left[ H ( \pmb { q } , \tilde { p } / s ) + \frac { \bar { \pi } ^ { 2 } } { 2 Q } + \frac { \pi _ { 1 } ^ { 2 } } { 2 Q _ { 1 } } + g \beta ^ { - 1 } \left| \mathfrak { n } s - \bar { \cal E } \right| \right) d \tilde { V } d s d \bar { \pi } d \pi _ { 1 } , \right.
$$

but now following this by ${ \tilde { p } } / s = p$ , we obtain

$$
{ \mathcal P } = \int \exp \left( - \beta \left[ H ( { \pmb q } , { \pmb p } ) + \frac { \bar { \pi } ^ { 2 } } { 2 Q } + \frac { \pi _ { 1 } ^ { 2 } } { 2 Q _ { 1 } } + g \beta ^ { - 1 } \ln s - E \right] \right) s ^ { N _ { f } } d V d s d \bar { \pi } d \pi _ { 1 } ,
$$

$d V = d ^ { N _ { f } } \pmb { q } d ^ { N _ { f } } \pmb { p }$ , if we then choose $g \ = \ N _ { f }$ , it appears in the exponential that $\mathrm { e x p } ( - g \ln s ) = s ^ { - N _ { f } }$ , but we must still perform the integration with respect to $s$ which is unbounded! ✷

In order to correct this problem there are several approaches one can take, including modification of the chain Hamiltonian in order to bound the s-integral. On the other hand we can also try completely different kinds of couplings, such as the following from [102]:

# Example 3

$$
\mathcal { H } _ { \mathrm { v e r t e x } } = \frac { \tilde { p } ^ { T } M ^ { - 1 } \tilde { p } } { 2 s ^ { 2 } } + V ( q ) + g \beta ^ { - 1 } \ln { s } + \frac { ( 1 + \sum \sigma _ { i } ^ { 2 } ) \pi _ { s } ^ { 2 } } { 2 Q _ { s } } + \sum _ { i } \frac { \sigma _ { i } ^ { 2 } } { 2 } + \sum _ { i = 1 , m } \frac { \pi _ { i } ^ { 2 } } { 2 Q _ { i } } .
$$

The $\sigma _ { i }$ are coupled to the original variables through $\pi _ { s }$ (a common vertex). To this generalized Hamiltonian we add a time transformation of Poincar´e type in the same manner as for Nos´e dynamics, resulting in

$$
\dot { \iota } _ { \mathrm { v e r t e x } } = s \left[ \frac { \tilde { p } ^ { T } M ^ { - 1 } \tilde { p } } { 2 s ^ { 2 } } + V ( q ) + g \beta ^ { - 1 } \ln s + \frac { ( 1 + \sum \sigma _ { i } ^ { 2 } ) \pi _ { s } ^ { 2 } } { 2 Q _ { s } } + \sum _ { i } \frac { \sigma _ { i } ^ { 2 } } { 2 } + \sum _ { i = 1 , m } \frac { \pi _ { i } ^ { 2 } } { 2 Q _ { i } } - E \right] ,
$$

$E = \mathcal { H } _ { \mathsf { v o r t e x } } ( 0 )$ . In this case a splitting method can be generated from the composition of the flows on

$$
\begin{array} { l } { { \displaystyle { H _ { 1 } = - s \left[ \frac { \left( 1 + \sum \sigma _ { i } ^ { 2 } \right) \pi _ { s } ^ { 2 } } { 2 Q _ { s } } + \frac { 1 } { 2 } \sum _ { i } \sigma _ { i } ^ { 2 } + g \beta ^ { - 1 } \ln s \right] } \ : , } } \\ { { \displaystyle { H _ { 2 } = s \left[ \frac { \tilde { p } ^ { T } M ^ { - 1 } \tilde { p } } { 2 s ^ { 2 } } + \sum \frac { \pi _ { i } ^ { 2 } } { 2 Q _ { i } } \right] } \ : , } } \\ { { \displaystyle { H _ { 3 } = s [ V ( \pmb q ) - E ] } . } } \end{array}
$$

This splitting is very similar to one proposed by Nos´e for the original Nos´e–Poincar´e method [147]. The flows for $H _ { 2 }$ and $H _ { 3 }$ are easily computed. For $H _ { 1 }$ we propose the use of a symplectic method such as the generalized Leapfrog scheme. ✷

Example 4A well-known system with reasonably good ergodicity properties is the three-ball billiard system with three hard-sphere particles in a square box. While we could use a hard-sphere bath [88], this would introduce some complications. Instead, we suggest to use a simplified bath consisting of three “soft” spheres (with pair potentials of the form $r ^ { - p }$ ) constrained to a small region via a harmonic tether to the origin. We can use this system as a generalized bath. Define

$$
\mathcal { H } _ { \mathrm { b i l i a r d } } = \mathcal { H } _ { \mathrm { N o s } \in } \big ( \tilde { p } , q , s , \pi _ { s } \big ) + \mathcal { H } _ { \mathrm { b a t h } } \big ( \{ \pmb { \sigma } _ { i } , \pmb { \pi } _ { i } \} \big ) + \mathcal { H } _ { \mathrm { i n t } } \big ( \pi _ { s } , \{ \pmb { \sigma } _ { i } , \pmb { \pi } _ { i } \} \big ) ,
$$

where

$$
\mathcal { H } _ { \mathrm { b a t h } } = \sum _ { i = 1 } ^ { 3 } \frac { \Vert \pmb { \pi } _ { i } \Vert ^ { 2 } } { 2 Q _ { i } } + \sum _ { i = 1 } ^ { 3 } \frac { \Vert \pmb { \sigma } _ { i } \Vert ^ { 2 } } { 2 } + \sum _ { i } \sum _ { j > i } \Vert \pmb { \sigma } _ { i } - \pmb { \sigma } _ { j } \Vert ^ { - 1 2 } ,
$$

and

$$
\mathcal { H } _ { \mathrm { i n t } } = \left( \sum _ { i = 1 } ^ { 3 } \| \pmb { \sigma } _ { i } \| ^ { 2 } \right) \frac { \pi _ { s } ^ { 2 } } { 2 Q _ { s } } .
$$

The bath positions and momenta $\pmb { \sigma } _ { i }$ and $\pmb { \pi } _ { i }$ are vectors in $\mathbb { R } ^ { 3 }$ . The Nos´e–Poincar´e equations for this system can be integrated using a Hamiltonian splitting like that used in the vertex coupling. This is left as an exercise.

Experiments with both of these generalized baths are discussed in [102] and, at the time of this writing, research is on-going into design of optimal baths. ✷

![](images/a2d437f84d7f98752766b440f0fdc413687e946ca81fad9b06832e547bbc0ea8.jpg)  
Figure 11.5 A simple energy rescaling function (left) and effect on energy of a double well model (right).

The development of flexible ´e-like schemes with good ergodicity properties is a topic of current. The interested reader is referred to the articles by LEIMKUHLER and SWEET [113a, b].

# 11.4.2 Simulation in other ensembles

It is interesting to consider alternatives to computation in the microcanonical or canonical ensembles. One example is the constant temperature and pressure (NPT) ensemble. Schemes for NPT calculations can be derived which are very similar to the methods discussed above for NVT simulation. For example, a variant of Nos´e–Poincar´e has been adapted for NPT simulation [182].

The development of non-standard distributions is often seen as a way to accelerate the configurational sampling of complex molecular systems having highly corrugated potential landscapes, for which the time scale of standard moleculardynamics simulations is insufficient for convergence of statistical averages. This is especially true of macromolecules, biomolecules, and amorphous materials. Over past decades, numerous schemes have been proposed for enhancing sampling efficiency, usually based on the systematic deformation of the potential (or total) energy surface to accelerate barrier crossings, either by lowering the barriers or raising the potential valleys. From a statistical mechanical perspective, such energetic modifications induce a corresponding alteration of the phase-space distribution by enhancing the statistical weight of configurations which otherwise would be rarely visited. If we have detailed knowledge of the modified sampling distribution, it is possible to “reweight” the computed trajectories to obtain averages in the original ensemble.

One of the simplest smoothing consists of introducing an energy scaling at high energy. We consider a function $\eta ( E )$ , as depicted in Fig. 11.5, and define

the “smoothed energy” by

$$
\begin{array} { r } { H ^ { \prime } = \eta ( H ) H . } \end{array}
$$

Canonical sampling with respect to this energy implies an ensemble density of the form

$$
\rho _ { \mathsf { c a n o n i c a l } } ( H ^ { \prime } ) = \mathsf { e x p } ( - \beta H ^ { \prime } ) = \mathsf { e x p } ( - \beta \eta ( H ) H ) = \rho ^ { \prime } ( H ) ,
$$

which can be viewed as a noncanonical sampling with respect to the original energy. Now suppose that we have computed a sampling trajectory for this ensemble using Nos´e dynamics, then

$$
\operatorname* { l i m } \frac { 1 } { T } \int _ { 0 } ^ { T } f ( \pmb { q } ( t ) , \tilde { \pmb { p } } ( t ) / s ( t ) ) d t \propto \int f ( \pmb { q } , \pmb { p } ) \ d \rho ^ { \prime } ( H ) d V .
$$

Of course this is not what we want! What we would like is to be able to recover the correct sampling with respect to the canonical ensemble. However, if we define

$$
\Delta H = H - H ^ { \prime } ,
$$

then

$$
\begin{array} { r l r } {  { \operatorname* { l i m } \frac { 1 } { T } \int _ { 0 } ^ { T } \exp [ - \beta \Delta H ( \pmb { q } ( t ) , \tilde { \pmb { p } } ( t ) / s ( t ) ) ] f ( \pmb { q } ( t ) , } } \\ & { } & { \tilde { \pmb { p } } ( t ) / s ( t ) ) d t \propto \int f ( \pmb { q } , \pmb { p } ) \rho _ { \mathrm { c a n } } ( H ) d V . } \end{array}
$$

This is what we mean by ensemble “reweighting.”

Alternatively, if the density is given, expressed as a function of the phase variables, one can typically derive both extended Hamiltonians and numerical methods from a reformulation of the problem to one couched in the canonical ensemble. If $\rho ( \pmb q , \pmb p )$ is the given (positive) ensemble density, we solve

$$
\rho = \exp ( - \beta \tilde { H } )
$$

for $\tilde { H }$ , where $\beta$ is essentially a free parameter. Averages with respect to Hamiltonian $H$ in the $\rho$ ensemble are now recovered directly by computing canonical averages of the system with Hamiltonian $\tilde { H }$ . However, in this work, care is needed to develop sensible geometric integrators. The Nos´e Hamiltonian for Generalized Density Dynamics (GDD) is

$$
H _ { \ N o s \bar { e } } ^ { \rho } = - \frac { 1 } { \beta } \ln \rho \big ( \pmb { q } , \tilde { \pmb { p } } / s \big ) + \frac { \pi ^ { 2 } } { 2 Q } + g \beta ^ { - 1 } \ln s .
$$

After Poincar´e transformation, this results in the equations of motion

$$
\begin{array} { l } { \displaystyle \dot { q } = - \frac { \beta ^ { - 1 } } { \rho ( q , \tilde { p } / s ) } \nabla _ { \tilde { p } / s } \rho ( \tilde { p } / s , q ) , } \\ { \displaystyle \dot { \tilde { p } } = \frac { \beta ^ { - 1 } } { \rho ( q , \tilde { p } / s ) } \nabla _ { \tilde { q } } \rho ( q , \tilde { p } / s ) , } \\ { \displaystyle \dot { s } = \frac { s \pi _ { s } } { Q } , } \\ { \displaystyle \dot { \pi } _ { s } = \frac { \beta ^ { - 1 } \tilde { p } } { s \rho ( q , \tilde { p } / s ) } \nabla _ { \tilde { p } } \rho ( q , \tilde { p } / s ) - g \beta ^ { - 1 } - \Delta H _ { \mathrm { N o s e } } ^ { \rho } . } \end{array}
$$

A separable Hamiltonian $H$ will not result in a separable $\tilde { H }$ , and the result is that a straightforward treatment based on applying Nos´ep–Poincar´e to simulate $\tilde { H }$ would have to be fully implicit. In [14] this difficulty was analyzed in some special cases, for example where $\rho = \rho _ { A } ( { \pmb q } ) \rho _ { B } ( { \pmb p } )$ and for $\rho = \rho ( H )$ . In both of these cases, it turns out to be possible to derive semi-explicit second-order symplectic schemes which require only a single force evaluation per timestep.

# 11.5 Exercises

1. Smooth potential cutoff. Often, one replaces the Lennard–Jones potential by a cut-off version whose derivative has compact support. This should be done so that the potential remains at least smooth (continuously differentiable), for example

$$
\begin{array} { r } { \phi _ { \downarrow \downarrow } ( r ) \approx \hat { \phi } _ { \downarrow \downarrow } ( r ) = \left\{ \begin{array} { l c r } { \phi _ { \downarrow \downarrow } ( r ) , } & { r < R _ { 1 } } \\ { P ( r ) , } & { R _ { 1 } \leq r < R _ { 2 } , } \\ { 0 , } & { r \geq R _ { 2 } } \end{array} \right. } \end{array}
$$

where $P ( r )$ is an interpolating polynomial (Fig. 11.6). A $C ^ { m }$ -approximation (meaning that the approximation can be differentiated $m$ times) can be obtained by introducing a higher-order Hermite interpolant $P ( r ) = A _ { 0 } + A _ { 1 } r +$ $\ldots + A _ { 2 m - 1 } r ^ { 2 m - 1 }$ , and determining the $2 m$ coefficients to satisfy the $2 m$ conditions $P ^ { ( k ) } ( R _ { 1 } ) = \phi ^ { ( k ) } ( R _ { 1 } )$ , $P ^ { ( k ) } ( R _ { 2 } ) = 0$ , $k = 0 , 1 , 2 , \ldots , m - 1$ . Find a $C ^ { 2 }$ -cutoff of the Lennard–Jones potential.

2. SHAKE discretization of Methane. Each molecule of Methane has five atoms (a carbon and four hydrogens) (see Fig. 11.7), arranged at the vertices and center of a regular tetrahedron. Let us order the atoms as follows: the central carbon of the first methane molecule, first hydrogen of first methane, second hydrogen of first methane, . . . , fourth hydrogen of first methane, central carbon of second methane, first hydrogen of second methane, etc., indexing them from 1. Just considering the equations for the first methane we have constrained equations of the form

![](images/6e2546e09fb6fdfb3c1445ecdcdc852fb0354f5d855ca4cf76ac69c7ce64cb99.jpg)

![](images/4c0e8f00749fe49593d51c4af1126ad30178d204c92db2f252ae294383d1de6d.jpg)  
Figure 11.6 Smooth potential cutoff by Hermite interpolation.   
Figure 11.7 Methane.

$$
\begin{array} { c } { { \dot { q } _ { 1 } = m _ { \mathrm { C } } ^ { - 1 } p _ { 1 } , } } \\ { { \dot { q } _ { k } = m _ { \mathrm { H } } ^ { - 1 } p _ { k } , } } \\ { { \dot { p } _ { 1 } = F _ { \mathrm { C } } - \displaystyle \sum _ { k = 1 } ^ { 4 } \lambda _ { k } ( q _ { 1 } - q _ { k + 1 } ) , } } \\ { { \dot { p } _ { k } = F _ { \mathrm { H } [ k - 1 ] } - \lambda _ { k - 1 } ( q _ { k } - q _ { 1 } ) , } } \\ { { \frac 1 2 \lVert q _ { k } - q _ { 1 } \rVert ^ { 2 } = \frac 1 2 L _ { \mathrm { C } \mathrm { H } } ^ { 2 } . } } \end{array}
$$

Here $m _ { C }$ , $m _ { H }$ represent the masses of the carbon and hydrogen atoms, respectively, $F _ { \mathrm { C } }$ and $F _ { \mathsf { H } [ k ] }$ , $k = 1 , 2 , 3 , 4$ are the forces acting on the carbon and each hydrogen atom due both to interactions with the other atoms of the first methane as well as to intermolecular interactions, and $L _ { \mathrm { C H } }$ is the natural length of this bond. The shape of the molecule is maintained by angle potentials between the hydrogens and the central carbon atom. After application of SHAKE and simplification, we find that we are left with a relatively simple system of four quadratic equations in $\lambda _ { 1 } , . . . , \lambda _ { 4 }$ . Since the equations look the same for each Methane, the SHAKE equations will only involve the Lagrange multipliers of the local group, so in a system of s methanes, we will face only s decoupled four-dimensional nonlinear subsystems, each of which can be solved by an iterative method.

Determine the coupled quadratic equations that must be solved at each step of SHAKE discretization.

3. Generalized Nos´e dynamics. State and prove conditions under which canonical sampling can be recovered from (11.23).

4. Generalized Nos´e dynamics. Write a discretization scheme for the soft-particle (“billiard”) bath model in Example 4.

# 12

# Hamiltonian PDEs

Many physical processes of interest not only evolve continuously in time but also possess a continuous spatial structure and, hence, can be described by partial differential equations (PDEs). Furthermore, many fundamental laws of physics, such as quantum mechanics, electrodynamics, ideal continuum mechanics, can be formulated within an extension of the Hamiltonian framework discussed so far to PDEs. In this chapter we focus on two particular examples of such Hamiltonian PDEs and discuss a number of numerical discretization techniques. The reader should, however, keep in mind that the solution behavior of PDEs is much more complex than that of ODEs and that the choice of an appropriate discretization will depend very much on the anticipated type of solutions. The techniques described in this chapter are very much restricted to smooth solutions such as solitons [53, 201] and balanced geophysical flows [169]. This excludes, in particular, the consideration of shocks [201]. A general introduction to numerical methods for PDEs can be found, for example, in [140].

# 12.1 Examples of Hamiltonian PDEs

# 12.1.1 The nonlinear wave equation

Let us consider the nonlinear wave equation

$$
u _ { t t } = \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) - f ^ { \prime } ( u ) , \quad u = u ( x , t ) ,
$$

where $\sigma$ and $f$ are smooth functions. If $\sigma ( u _ { x } ) = u _ { x } ^ { 2 } / 2$ , then the semi-linear wave equation

$$
{ { u } _ { t t } } = { { u } _ { x x } } - { { f } ^ { \prime } } ( u )
$$

is obtained. Other choices for $\sigma ( u _ { x } )$ lead to idealized one-dimensional models for fluids and materials.

Throughout this chapter, solutions $\boldsymbol { u } = \boldsymbol { u } ( \boldsymbol { x } , t )$ of (12.1) are assumed to be smooth in the independent variables $x$ and $t$ and we impose periodic boundary conditions $\boldsymbol { { u } } ( \boldsymbol { x } , t ) = \boldsymbol { { u } } ( \boldsymbol { x } + \boldsymbol { L } , t ) , \boldsymbol { L } \ge$ $L > 0$ .

We introduce the total energy ${ \mathcal { E } } [ u ]$ by

$$
\mathcal { E } [ u ] = \int _ { 0 } ^ { L } \left[ \frac { 1 } { 2 } u _ { t } ^ { 2 } + \sigma ( u _ { x } ) + f ( u ) \right] \ : d x ,
$$

and observe that, using integration by parts,

$$
\begin{array} { r } { \frac { d } { d t } \mathcal { E } [ u ] = \int _ { 0 } ^ { L } \left[ u _ { t } u _ { t t } + \sigma ^ { \prime } ( u _ { x } ) u _ { x t } + f ^ { \prime } ( u ) u _ { t } \right] d x } \\ { = \int _ { 0 } ^ { L } u _ { t } \left[ u _ { t t } - \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) + f ^ { \prime } ( u ) \right] d x . } \end{array}
$$

However, the term in brackets is equal to zero along solutions of (12.1) and, hence, the total energy ${ \mathcal { E } } [ u ]$ is conserved.

Let us denote the space of smooth and $L$ -periodic functions in $x$ by ${ \boldsymbol { S } } =$ $C ^ { \infty } [ 0 , L ]$ . Our assumption then is that $u ( . , t ) \in S$ for $t \geq 0$ or in short hand $u ( t ) \in S$ . This smoothness assumption explicitly excludes the consideration of shock-type solutions [201].

Furthermore, upon rewriting (12.1) as

$$
\begin{array} { l l } { u _ { t } = v , } \\ { v _ { t } = \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) - f ^ { \prime } ( u ) , } \end{array}
$$

the wave equation can, formally, be viewed as a Hamiltonian system with phase space $( u , v ) ^ { T } \in S \times S$ , symplectic form,

$$
\bar { \omega } = \int _ { 0 } ^ { L } d u \wedge d v d x ,
$$

and Hamiltonian functional

$$
\mathcal { H } [ u , v ] = \int _ { 0 } ^ { L } \left[ \frac { 1 } { 2 } v ^ { 2 } + \sigma ( u _ { x } ) + f ( u ) \right] d x .
$$

The Hamiltonian equations of motion are derived in the following way. First, the gradient $\nabla _ { z }$ of classical mechanics is replaced by the “variational” gradient $\pmb { \delta _ { z } } = ( \delta _ { u } , \delta _ { v } ) ^ { T }$ , $\boldsymbol { z } = ( u , v ) ^ { T } \in S { \times } S$ . The variational derivative $\delta _ { u } \mathcal { G }$ of a functional $\mathcal { G } [ \boldsymbol { u } ]$ is defined by

$$
\int _ { 0 } ^ { L } ( \delta _ { u } \mathcal { G } [ u ] \delta u ) d x = \operatorname* { l i m } _ { \varepsilon \to 0 } \frac { \mathcal { G } [ u + \varepsilon \delta u ] - \mathcal { G } [ u ] } { \varepsilon } ,
$$

for any $\delta u \in S$ . Let us demonstrate this for $\delta _ { u } \mathcal { H } [ u , v ]$ which is equivalent to the

variational derivative of $\begin{array} { r } { \mathcal { G } [ u ] = \int _ { 0 } ^ { L } \left[ \sigma ( u _ { x } ) + f ( u ) \right] d x } \end{array}$

$$
\begin{array} { r l } { \displaystyle \int _ { 0 } ^ { L } \left( \delta _ { u } \mathcal { G } [ u ] \delta u \right) d x = } & { \underset { \varepsilon \to 0 } { \operatorname* { l i m } } \frac { 1 } { \varepsilon } \Bigg \lbrace \int _ { 0 } ^ { L } \left[ \sigma ( [ u + \varepsilon \delta u ] _ { x } ) + f ( u + \varepsilon \delta u ) \right] d x - } \\ & { } \\ { \displaystyle \int _ { 0 } ^ { L } \left[ \sigma ( \upsilon _ { x } ) + f ( u ) \right] d x \Bigg \rbrace } \\ & { = \displaystyle \int _ { 0 } ^ { L } \left[ \sigma ^ { \prime } ( u _ { x } ) ( \delta u ) _ { x } + f ^ { \prime } ( u ) \delta u \right] d x } \\ & { = \displaystyle \int _ { 0 } ^ { L } \left[ - \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) \delta u + f ^ { \prime } ( u ) \delta u \right] d x } \\ & { = \displaystyle \int _ { 0 } ^ { L } \left[ - \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) + f ^ { \prime } ( u ) \right] \delta u d x . } \end{array}
$$

Comparison of the left- and right-hand side yields

$$
\delta _ { u } \mathcal { H } [ u , v ] = \delta _ { u } \mathcal { G } [ u ] = - \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) + f ^ { \prime } ( u ) .
$$

One also obtains $\delta _ { v } \mathcal { H } [ u , v ] = v$

Next we rewrite the symplectic form (12.2) as

$$
\bar { \omega } = \frac { 1 } { 2 } \int _ { 0 } ^ { L } ( J _ { 2 } ^ { - 1 } d z ) \wedge d z d x ,
$$

with the (local) structure matrix

$$
J _ { 2 } = \left[ { \begin{array} { c c } { 0 } & { + 1 } \\ { - 1 } & { 0 } \end{array} } \right] ,
$$

and $d z = ( d u , d v ) ^ { T }$ . Then the wave equation (12.1) becomes equivalent to an abstract Hamiltonian system

$$
\begin{array} { r } { z _ { t } = J _ { 2 } \delta _ { z } \mathcal { H } [ z ] . } \end{array}
$$

We finally note that the nonappearance of the independent variable $x$ in the functions $f$ and $\sigma$ implies another conserved functional for the PDE (12.1), namely the total momentum

$$
\mathcal { M } [ u , v ] = \int _ { 0 } ^ { L } v u _ { x } d x .
$$

Indeed

$$
\begin{array} { c } { \displaystyle \frac { d } { d t } \mathcal { M } = \int _ { 0 } ^ { L } ( v _ { t } u _ { x } + v u _ { x t } ) d x } \\ { = \displaystyle \int _ { 0 } ^ { L } ( u _ { x } [ \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) - f ^ { \prime } ( u ) ] + v v _ { x } ) d x } \end{array}
$$

$$
\begin{array} { l } { = \displaystyle \int _ { 0 } ^ { L } [ - \sigma ( u _ { x } ) - f ( u ) + v ^ { 2 } / 2 ] _ { x } d x } \\ { = \displaystyle \left[ - \sigma ( u _ { x } ) - f ( u ) + v ^ { 2 } / 2 \right] _ { x = 0 } ^ { x = L } } \\ { = 0 . } \end{array}
$$

# 12.1.2 Soliton solutions

Waves are one of the most important features of fluid dynamics [201]. Particular types of waves are those that travel at a constant speed $c \neq 0$ without changing their shape. These waves are called traveling waves or solitons [201, 53]. Mathematically a soliton is described by a (smooth) function $\phi$ such that

$$
u ( x , t ) = \phi ( x - c t ) .
$$

Let us introduce the new variable $\xi = x - c t$ , then $u _ { x } = \phi _ { \xi }$ , $u _ { t } = - c \phi _ { \xi }$ , etc. Hence, assuming a solitary solution, the wave equation (12.1) gives rise to a second-order ODE,

$$
c ^ { 2 } \phi _ { \xi \xi } = \partial _ { \xi } \sigma ^ { \prime } ( \phi _ { \xi } ) - f ^ { \prime } ( \phi ) ,
$$

in the independent variable $\xi$ . Equation (12.5) is a Euler–Lagrange equation and to obtain the corresponding Hamiltonian formulation we introduce the new dependent variable (conjugate momentum) $\psi = c ^ { 2 } \phi _ { \xi } - \sigma ^ { \prime } ( \phi _ { \xi } )$ . Let us assume that this relation is invertible, i.e., there is a function $g ( \psi )$ such that $\phi _ { \xi } ~ =$ $g ^ { \prime } ( \psi )$ . Hence one can rewrite the second-order ODE (12.5) as a conservative system

$$
\psi _ { \xi } = - f ^ { \prime } ( \phi ) , \qquad \phi _ { \xi } = g ^ { \prime } ( \psi ) ,
$$

with Hamiltonian

$$
\begin{array} { r } { H = g ( \psi ) + f ( \phi ) . } \end{array}
$$

A solution $\phi ( \xi )$ gives rise to a soliton solution if the boundary conditions $\phi _ { \xi } ( \pm \infty ) =$ 0 are satisfied, i.e., $\phi ( \xi )$ approaches some constant value as $\xi  \pm \infty$ . In particular, let $( \phi _ { i } , \psi _ { i } )$ denote the equilibrium solutions of (12.6), then any homoclinic or heteroclinic solution of (12.6) gives rise to a (not necessarily stable) soliton solution of the nonlinear wave equation (12.1).1

Example 1 Let us consider the sine-Gordon equation

$$
U _ { t t } = U _ { x x } - \mathsf { S i n } ( U ) .
$$

Traveling wave solutions $u ( x , t ) = \phi ( x - c t )$ must satisfy the second-order ODE

$$
c ^ { 2 } \phi _ { \xi \xi } = \phi _ { \xi \xi } - \mathsf { s i n } ( \phi ) .
$$

We introduce the momentum $\psi = c ^ { 2 } \phi _ { \xi } - \phi _ { \xi }$ . For $c \neq \pm 1$ , this relation can be inverted and we obtain $\phi _ { \xi } = \psi / ( c ^ { 2 } - 1 )$ and $g ( \psi ) = { \textstyle \frac { 1 } { 2 } } \psi ^ { 2 } / ( c ^ { 2 } - 1 )$ . Hence the Hamiltonian equations are

$$
\psi _ { \xi } = - \sin ( \phi ) , \qquad \phi _ { \xi } = \frac { 1 } { c ^ { 2 } - 1 } \psi
$$

with Hamiltonian

$$
H = \frac { \psi ^ { 2 } } { 2 ( c ^ { 2 } - 1 ) } + ( 1 - \cos \phi ) .
$$

These are the equations of motion for a nonlinear pendulum with mass $m = c ^ { 2 } - 1$ . Hence we first consider the condition $| c | > 1$ . The nonlinear pendulum possesses heteroclinic solutions connecting pairs of hyperbolic equilibria $\displaystyle ( \phi , \psi ) = ( k \pi , 0 )$ and $( \phi , \psi ) = ( ( k + 2 ) \pi , 0 )$ for $k = 1 , \pm 3 , \pm 5 , . . . .$ These heteroclinic connections are easily found as the contour lines of constant energy $H = 0$ . Unfortunately, the associated soliton solutions are all unstable [201, 53]. For $| c | < 1$ , the equilibrium points $( k \pi , 0 )$ , $( ( k + 2 ) \pi , 0 )$ , $k = 0 , \pm 2 , \pm 4 , . . .$ , become hyperbolic and give rise to stable soliton solutions. An explicit soliton solution with wave speed $C$ , $| c | < 1$ , is given by

$$
u ( x , t ) = 4 \arctan \exp \left( { \frac { x - c t } { \sqrt { 1 - c ^ { 2 } } } } \right) .
$$

Because of their special shape, these solutions are called kink solitons.

# 12.1.3 The two-dimensional rotating shallow-water equations

Large-scale geophysical flows in the atmosphere and ocean are essentially incompressible and often stratified into nearly two-dimensional layers. Furthermore, the effect of the earth’s rotation significantly affects large-scale patterns away from the equator, for example in mid-latitude or near the poles. See ANDREWS [6] and SALMON [169] for an introduction to geophysical fluid dynamics and MORRI-SON [139] for further details on the Hamiltonian formalism of geophysical fluid dynamics.

A simple one-layer model system is provided by the two-dimensional rotating shallow-water equations (SWEs) [139, 169]

$$
u _ { t } + u u _ { x } + v u _ { y } = + f v - c _ { 0 } ^ { 2 } h _ { x } ,
$$

$$
\begin{array} { r } { v _ { t } + u v _ { x } + v v _ { y } = - f u - c _ { 0 } ^ { 2 } h _ { y } , } \\ { h _ { t } + u h _ { x } + v h _ { y } = - h ( u _ { x } + v _ { y } ) , } \end{array}
$$

where $\pmb { \mathscr { u } } = ( \mathscr { u } , \mathscr { v } ) ^ { T } \in \mathbb { R } ^ { 2 }$ is the horizontal velocity field, $c _ { 0 } = { \sqrt { g H } }$ , $g$ is the gravitational constant, $H$ is the mean layer depth of the fluid, $h > 0$ is the normalized layer depth with mean value scaled equal to one, and $f > 0$ is twice the angular velocity of the rotating fluid. For simplicity, we will consider the SWEs over a double periodic domain of size $L \times L$ and keep $f = f _ { 0 }$ constant.

We next introduce the material time derivative of a function $w ( x , y , t )$

$$
\frac { D w } { D t } = w _ { t } + u w _ { x } + v w _ { y } = w _ { t } + u \cdot \nabla _ { x } w ,
$$

and rewrite the SWEs (12.7)–(12.9) in the form

$$
\begin{array} { l } { \displaystyle \frac { D \pmb { u } } { D t } = f _ { 0 } J _ { 2 } \pmb { u } - c _ { 0 } ^ { 2 } \nabla _ { \pmb { x } } \eta , } \\ { \displaystyle \frac { D h } { D t } = - h \nabla _ { \pmb { x } } \cdot \pmb { u } , } \end{array}
$$

where $\pmb { x } = ( x , y ) ^ { T }$ , $h = 1 + \eta$ , and

$$
J _ { 2 } = \left[ { \begin{array} { c c } { 0 } & { + 1 } \\ { - 1 } & { 0 } \end{array} } \right] .
$$

Given a function $w ( x , t )$ , the material time derivative characterizes the change of w along motion of a fluid particle $\pmb { X } ( t ) = ( X ( t ) , Y ( t ) ) ^ { T } \in \mathbb { R } ^ { 2 }$ , which is passively advected under the velocity field $\pmb { u }$ , i.e.

$$
{ \frac { D X } { D t } } = \pmb { u } .
$$

As an example consider absolute vorticity

$$
\zeta = v _ { x } - u _ { y } + f _ { 0 } = \nabla _ { x } \times \pmb { u } + f _ { 0 } .
$$

Using

$$
\begin{array} { l } { \displaystyle \nabla _ { x } \times \frac { D { \boldsymbol u } } { D t } = \frac { \partial } { \partial x } \frac { D } { D t } { \boldsymbol v } - \frac { \partial } { \partial y } \frac { D } { D t } { \boldsymbol u } } \\ { \displaystyle = ( { \boldsymbol v } _ { t } + { \boldsymbol u } { \boldsymbol v } _ { x } + { \boldsymbol v } { \boldsymbol v } _ { y } ) _ { x } - ( { \boldsymbol u } _ { t } + { \boldsymbol u } { \boldsymbol u } _ { x } + { \boldsymbol v } { \boldsymbol u } _ { y } ) _ { y } } \\ { \displaystyle = ( { \boldsymbol v } _ { x } - { \boldsymbol u } _ { y } ) _ { t } + { \boldsymbol u } ( { \boldsymbol v } _ { x } - { \boldsymbol u } _ { y } ) _ { x } + { \boldsymbol v } ( { \boldsymbol v } _ { x } - { \boldsymbol u } _ { y } ) _ { y } + ( { \boldsymbol v } _ { x } - { \boldsymbol u } _ { y } ) ( { \boldsymbol u } _ { x } + { \boldsymbol v } _ { y } ) } \\ { \displaystyle = \frac { D } { D t } \zeta + ( \zeta - f _ { 0 } ) \nabla _ { x } \cdot { \boldsymbol u } , } \end{array}
$$

it is easy to conclude from (12.10) that absolute vorticity satisfies the continuity equation

$$
\frac { D \zeta } { D t } = - \zeta \nabla _ { x } \cdot \pmb { u } .
$$

The ratio of absolute vorticity $\zeta$ and layer depth $h$ is called potential vorticity (PV) $q = \zeta / h$ [169]. The PV field $q$ is materially conserved since, using (12.11) and (12.13)

$$
\frac { D q } { D t } = \frac { 1 } { h } \left\{ \frac { D \zeta } { D t } - q \frac { D h } { D t } \right\} = 0 .
$$

Let us now assume that, for the scales and motion of interest, we find that the velocity field $\pmb { u }$ satisfies

$$
\frac { 1 } { f _ { 0 } } \frac { D \pmb { u } } { D t } \approx \pmb { 0 } .
$$

Then the momentum equation (12.10) reduces to

$$
\mathbf { 0 } \approx J _ { 2 } \pmb { u } - \frac { c _ { 0 } ^ { 2 } } { f _ { 0 } } \nabla _ { \pmb { x } } \eta .
$$

The right-hand side can be solved for the velocity and one obtains the geostrophic wind approximation

$$
\pmb { u } ^ { 9 } = - \frac { c _ { 0 } ^ { 2 } } { f _ { 0 } } J _ { 2 } \nabla _ { x } \eta .
$$

We next assume that potential vorticity $q$ is materially advected along the geostrophic wind $\pmb { u } ^ { 9 }$ , i.e.

$$
\begin{array} { r } { q _ { t } + \pmb { u } ^ { 9 } \cdot \nabla _ { \pmb { x } } q = 0 . } \end{array}
$$

Potential vorticity $q$ , with $\pmb { u }$ replaced by $\pmb { u } ^ { 9 }$ , can be expressed as

$$
q = \frac { \nabla _ { \boldsymbol { x } } \times \pmb { u } ^ { 9 } + f _ { 0 } } { 1 + \eta } = f _ { 0 } \frac { L _ { R } ^ { 2 } \nabla _ { \boldsymbol { x } } ^ { 2 } \eta + 1 } { 1 + \eta } ,
$$

where we used $h = 1 + \eta$ and introduced the Rossby deformation radius $L _ { R } =$ $c _ { 0 } / f _ { 0 }$ . The final step in our approximation is provided by the assumption

$$
\frac { L _ { R } ^ { 2 } \nabla _ { x } ^ { 2 } \eta + 1 } { 1 + \eta } \approx L _ { R } ^ { 2 } \nabla _ { x } ^ { 2 } \eta + 1 - \eta ,
$$

which leads to

$$
q / f _ { 0 } - 1 \approx L _ { R } ^ { 2 } \nabla _ { x } ^ { 2 } \eta - \eta .
$$

This approximation gives rise to the (linear) $P V$ inversion relation

$$
\eta ^ { 9 } = - \left( 1 - L _ { R } ^ { 2 } \nabla _ { x } ^ { 2 } \right) ^ { - 1 } ( q / f _ { 0 } - 1 ) .
$$

Equation (12.15) with $\eta$ replaced by $\eta ^ { \mathfrak { g } }$ together with (12.16) provide a closed set of equations called the quasi-geostrophic approximation [169]. The quasigeostrophic approximation is a valid approximation to the full SWEs for a layer depth $h$ evolving on a typical horizontal length-scale $L \ge L _ { R }$ and for velocities $\pmb { u }$ with a typical scale $U$ such that the associated Rossby number satisfies $\mathsf { R o } =$ $U / ( f _ { 0 } L ) \ll 1$ .2 The ratio of $L _ { R }$ to $L$ is called the Burger number: $\mathsf { B u } = ( L _ { R } / L ) ^ { 2 }$ .

Instead of solving the reduced quasi-geostrophic equations, one is often interested in numerically approximating the full SWEs (12.10)–(12.11) subject to initial data satisfying (12.14). We will describe a numerical method in Section 12.2.2. The method is based on a Lagrangian formulation3 of fluid dynamics, which we outline next.

The Lagrangian description of fluid dynamics is a particle-based formulation with the continuum of particles being advected according to (12.12). Hence, the positions of all fluid particles $\pmb { X } = ( X , Y ) ^ { T }$ are given as a time-dependent transformation from a label space $\mathbb { A } \subset \mathbb { R } ^ { 2 }$ to position space $\mathbb { X } \subset \mathbb { R } ^ { 2 }$

$$
\pmb { X } = \pmb { X } ( \pmb { a } , t ) , \quad \pmb { a } = ( \pmb { a } , \pmb { b } ) ^ { T } \in \mathbb { A } , \quad \pmb { X } = ( \pmb { X } , \pmb { Y } ) ^ { T } \in \mathbb { X } ^ { 2 } .
$$

The labels are fixed for each particle and a natural choice is provided by the particle’s initial conditions, i.e. $\pmb { a } = \pmb { X } ( \pmb { a } , 0 )$ , which we assume from now on.

The fluid layer depth $h$ is defined as a function of the determinant of the $2 \times 2$ Jacobian matrix

$$
\pmb { X _ { a } } = \frac { \partial ( X , Y ) } { \partial ( a , b ) }
$$

through the relation

$$
h ( { \pmb X } , t ) | { \pmb X } _ { { \pmb a } } | = h _ { o } ( { \pmb a } ) ,
$$

where, for the specific labels defined above, $h _ { o } ( \pmb { a } ) = h ( \pmb { a } , 0 )$ is the initial layerdepth at $t = 0$ . Differentiation of (12.18) with respect to time and using (12.12) yields an expression that is equivalent to the continuity equation (12.11). Hence (12.18) and (12.11) are essentially equivalent statements.

Consider the integral identity

$$
h ( \boldsymbol { x } , t ) = \int h ( \boldsymbol { X } , t ) \delta ( \boldsymbol { x } - \boldsymbol { X } ) d \boldsymbol { X } d \boldsymbol { Y }
$$

2More precisely, we also have to request that $| \eta | \ll 1$ [169].

defining the layer-depth $h$ at time $t$ and Eulerian position $x$ . Here $\delta$ denotes the Dirac delta function. Using $d X d Y = \vert X _ { a } \vert d a d b$ and (12.18), we can pull this integral back to label space, arriving at the relation

$$
h ( x , t ) = \int h _ { o } ( { \pmb a } ) \delta ( { \pmb x } - { \pmb X } ( { \pmb a } , t ) ) d { \ b a } d b ,
$$

which can be taken as the definition of the layer depth in a Lagrangian description of fluid mechanics.

The SWEs (12.10)–(12.11) are now reformulated to

$$
\begin{array} { l } { \displaystyle \frac { \partial \pmb { u } } { \partial t } = f _ { 0 } J _ { 2 } \pmb { u } ^ { \bot } - c _ { 0 } ^ { 2 } \nabla \pmb { x } h , } \\ { \displaystyle \frac { \partial \pmb { X } } { \partial t } = \pmb { u } , } \end{array}
$$

where $h$ is defined by (12.18) or (12.19). Note that the material time derivative was replaced by the partial derivative with respect to time. This reflects the fact that the material time derivative becomes a partial derivative in a Lagrangian formulation of fluid dynamics, where time $t$ and labels $\pmb { a } \in \mathbb { A }$ are now the independent variables. Next we introduce the canonical momenta

$$
\mathbf { \omega } \mathbf { p } = h _ { o } \mathbf { \omega } \mathbf { u } ,
$$

and the equations (12.20)–(12.21) become canonical with Hamiltonian

$$
{ \mathcal { H } } = { \frac { 1 } { 2 } } \int { \frac { \mathbf { p } \cdot \mathbf { p } } { h _ { o } } } d a d b + { \frac { c _ { 0 } ^ { 2 } } { 2 } } \int h _ { o } h d a d b
$$

and symplectic two-form

$$
\bar { \omega } : = \int \left( \frac { h _ { o } f _ { 0 } } { 2 } d \pmb { X } \wedge J _ { 2 } d \pmb { X } + d \pmb { p } \wedge d \pmb { X } \right) d a d b .
$$

# 12.1.4 Noncanonical Hamiltonian wave equations

We have already encountered in Chapter 8 the rigid body as an example of a noncanonical Hamiltonian system of the general form

$$
\frac { d } { d t } z = J ( z ) \nabla _ { z } H ( z ) .
$$

For PDEs, this generalizes to

$$
\begin{array} { r } { u _ { t } = \mathcal { I } ( u ) \delta _ { u } \mathcal { H } . } \end{array}
$$

Here $\mathcal { I } ( u )$ is a linear (in general, differential) operator, called the Poisson operator, that has to satisfy certain properties similar to those for the matrix $J ( z )$ [139].

A well-known example is provided by the Korteweg–de Vries (KdV) equation [53]

$$
u _ { t } + u u _ { x } + u _ { x x x } = 0 .
$$

Here the operator $\mathcal { I }$ is equal to

$$
{ \mathcal { I } } = - { \frac { \partial } { \partial x } } ,
$$

and the Hamiltonian functional is given by

$$
{ \mathcal { H } } = \int \left[ { \frac { 1 } { 6 } } u ^ { 3 } - { \frac { 1 } { 2 } } u _ { x } ^ { 2 } \right] d x .
$$

We can also introduce a noncanonical Poisson bracket

$$
\{ \mathcal { F } , \mathcal { G } \} = - \int ( \delta _ { u } \mathcal { F } ) \partial _ { x } ( \delta _ { u } \mathcal { G } ) d x ,
$$

and the skew-symmetry of $\{ { \mathcal { F } } , { \mathcal { G } } \}$ follows upon integration by parts. Similar to the rigid body, the Poisson operator $\mathcal { I }$ is not invertible and this gives rise to the Casimir function

$$
C [ u ] = \int u d x .
$$

Indeed, it is easy to verify that

$$
\frac { d } { d t } C = \{ C , \mathcal { H } \} = 0 ,
$$

along solutions of the KdV equation.

Inviscid fluid dynamics leads to Eulerian equations of motion that are also noncanonical. However, compared with $\mathsf { K d V }$ , the situation is made more complicated by the fact that the Poisson operator $\mathcal { I }$ is now no longer constant and independent of the dynamical variables. In fact, one can draw an analogy between two-dimensional incompressible fluid dynamics and an infinite-dimensional version of rigid body dynamics. See the review article by MORRISON [139] for further details.

# 12.2 Symplectic discretizations

The basic idea of symplectic discretization methods for Hamiltonian PDEs consists of two steps:

(i) A spatial truncation that reduces the PDE to a system of Hamiltonian ODEs.

(ii) Timestepping of the finite-dimensional Hamiltonian ODE using an appropriate symplectic method.

The crucial new step is the construction of a finite-dimensional ODE model that retains the Hamiltonian character of the given PDE. The most popular approach is based on the introduction of a spatial grid over which the equations of motion can be truncated. Another approach, particularly well suited for Lagrangian fluid dynamics, reduces the PDE to a set of moving particles interacting through an appropriate potential energy function. Both approaches will be described below.

Finally we give a note of warning. Certain noncanonical Hamiltonian PDEs resist a spatial truncation to a finite-dimensional Hamiltonian system. This is true in particular for the Eulerian formulation of inviscid fluid dynamics. The only significant exception is provided by incompressible fluids on a plane with double periodic boundary conditions. See ZEITLIN [208] and MCLACHLAN [128] for a numerical implementation.

# 12.2.1 Grid-based methods

Consider the nonlinear wave equation (12.1). The first step towards a numerical algorithm is to introduce $N$ grid points $x _ { i } = i \Delta x , \Delta x = L / N$ , $i = 1 , \dots , N$ , and to approximate functions $u \in S$ by vectors $\pmb { \imath } = ( u _ { 1 } , u _ { 2 } , \ldots , u _ { N } ) ^ { T } \in \mathbb { R } ^ { N }$ with $u ( x _ { i } ) \approx u _ { i }$ . We define $u _ { i + N } = u _ { i }$ , reflecting the fact that periodic boundary conditions are imposed. The new state space is $z = \{ z _ { i } \} \in \mathbb { R } ^ { 2 N }$ , $z _ { i } = ( u _ { i } , v _ { i } ) ^ { T } \in$ $\mathbb { R } ^ { 2 }$ . The symplectic form (12.2) is naturally truncated to

$$
\bar { \omega } _ { N } = \sum _ { i = 1 } ^ { N } d u _ { i } \wedge d v _ { i } \Delta x = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } d z _ { i } \wedge J _ { 2 } ^ { - 1 } d z _ { i } \Delta x ,
$$

and the Hamiltonian functional (12.3) is approximated by the sum

$$
H = \sum _ { i = 1 } ^ { N } \left[ \frac { 1 } { 2 } v _ { i } ^ { 2 } + \sigma \left( \frac { u _ { i } - u _ { i - 1 } } { \Delta x } \right) + f ( u _ { i } ) \right] \Delta x .
$$

Hence, we obtain the system of Hamiltonian ODEs

$$
\frac { d } { d t } z _ { i } = \frac { 1 } { \Delta x } J _ { 2 } \nabla _ { z _ { i } } H ( z ) , \qquad i = 1 , \ldots , N .
$$

Note that

$$
\operatorname* { l i m } _ { \Delta x \to 0 } \frac { 1 } { \Delta x } \nabla _ { u } H \to \delta _ { u } \mathcal H [ u , v ] \quad \mathrm { a n d } \quad \operatorname* { l i m } _ { \Delta x \to 0 } \frac { 1 } { \Delta x } \nabla _ { v } H \to \delta _ { v } \mathcal H [ u , v ] ,
$$

and the spatially discrete equations formally converge to the PDE limit (12.4).

For the specific Hamiltonian, as given above, the finite-dimensional truncation becomes

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } v _ { i } = \frac { \sigma ^ { \prime } \left( w _ { i + 1 } \right) - \sigma ^ { \prime } \left( w _ { i } \right) } { \Delta x } - f ^ { \prime } ( u _ { i } ) , } \\ { \displaystyle \frac { d } { d t } u _ { i } = v _ { i } , } \end{array}
$$

$i = 1 , \dots , N$ , with

$$
w _ { i + 1 } = \frac { u _ { i + 1 } - u _ { i } } { \Delta x } , \qquad w _ { i } = \frac { u _ { i } - u _ { i - 1 } } { \Delta x } .
$$

The equations of motion can be integrated in time using any canonical method such as a symplectic Euler method, for example,

$$
\begin{array} { r l } & { v _ { i } ^ { n + 1 } = v _ { i } ^ { n } + \Delta t \left[ \frac { \sigma ^ { \prime } \left( w _ { i + 1 } ^ { n } \right) - \sigma ^ { \prime } \left( w _ { i } ^ { n } \right) } { \Delta x } - f ^ { \prime } ( u _ { i } ^ { n } ) \right] , } \\ & { u _ { i } ^ { n + 1 } = u _ { i } ^ { n } + \Delta t v _ { i } ^ { n + 1 } , } \end{array}
$$

where

$$
w _ { i } ^ { n } = \frac { u _ { i } ^ { n } - u _ { i - 1 } ^ { n } } { \Delta x } , \qquad w _ { i + 1 } ^ { n } = \frac { u _ { i + 1 } ^ { n } - u _ { i } ^ { n } } { \Delta x } .
$$

See MCLACHLAN [129] for further details on this classical approach to the numerical solution of Hamiltonian PDEs.

This might appear to be the end of the story. However, the interpretation of the wave equation (12.1) as an infinite-dimensional Hamiltonian system has masked some of the interesting local features of the PDE. For example, let us have another look at the Hamiltonian functional $\mathcal { H } [ u , v ]$ . We can write this functional as

$$
{ \mathcal { H } } [ u , v ] = \int _ { 0 } ^ { L } E ( u , v ) d x , \qquad E ( u , v ) = { \frac { 1 } { 2 } } v ^ { 2 } + \sigma ( u _ { x } ) + f ( u ) .
$$

The function $E$ is called the energy density. Let us compute the time derivative of $E$

$$
\begin{array} { r l } & { E _ { t } = v v _ { t } + \sigma ^ { \prime } ( u _ { x } ) u _ { x t } + f ^ { \prime } ( u ) u _ { t } } \\ & { \quad = v \left[ \partial _ { x } \sigma ^ { \prime } ( u _ { x } ) - f ^ { \prime } ( u ) \right] + \sigma ^ { \prime } ( u _ { x } ) v _ { x } + f ^ { \prime } ( u ) v } \\ & { \quad = \left[ v \sigma ^ { \prime } ( u _ { x } ) \right] _ { x } . } \end{array}
$$

We have obtained what is called an energy conservation law

$$
E _ { t } + F _ { x } = 0 ,
$$

where $F = - v \sigma ^ { \prime } ( u _ { x } )$ is called the energy flux. Under periodic boundary conditions, the conservation law (12.26) immediately implies conservation of total energy since $\begin{array} { r } { \int _ { 0 } ^ { L } F _ { x } = [ F ] _ { x = 0 } ^ { x = L } \dot { = } 0 } \end{array}$ . But the energy conservation law (12.26) is valid independently of any boundary conditions. Hence it is more fundamental than conservation of total energy.

Let us repeat the above calculation for the spatially truncated system (12.24)– (12.25). We define the discrete energy density

$$
E _ { i } = \frac { 1 } { 2 } v _ { i } ^ { 2 } + \sigma ( w _ { i } ) + f ( u _ { i } ) ,
$$

and find:

$$
\begin{array} { r l } & { \frac { d } { d t } E _ { i } = v _ { i } \dot { v } _ { i } + \sigma ^ { \prime } ( w _ { i } ) \frac { \dot { u } _ { i } - \dot { u } _ { i - 1 } } { \Delta x } + { t ^ { \prime } } ( { u } _ { i } ) \dot { u } _ { i } } \\ & { \qquad = v _ { i } \frac { \sigma ^ { \prime } \left( W _ { i + 1 } \right) - \sigma ^ { \prime } \left( { w } _ { i } \right) } { \Delta x } + \sigma ^ { \prime } ( w _ { i } ) \frac { V _ { i } - V _ { i - 1 } } { \Delta x } } \\ & { \qquad = \frac { V _ { i } \sigma ^ { \prime } \left( { w } _ { i + 1 } \right) - \sigma ^ { \prime } \left( { w } _ { i } \right) V _ { i - 1 } } { \Delta x } } \\ & { \qquad = - \frac { F _ { i + 1 / 2 } - F _ { i - 1 / 2 } } { \Delta x } , } \end{array}
$$

where

$$
\begin{array} { r } { F _ { i + 1 / 2 } = - v _ { i } \sigma ^ { \prime } ( w _ { i + 1 } ) , \quad F _ { i - 1 / 2 } = - v _ { i - 1 } \sigma ^ { \prime } ( w _ { i } ) . } \end{array}
$$

Hence we have obtained a semi-discrete energy conservation law

$$
\frac { d } { d t } E _ { i } + \frac { F _ { i + 1 / 2 } - F _ { i - 1 / 2 } } { \Delta x } = 0 ,
$$

and $F _ { i \pm 1 / 2 }$ are approximations to the energy flux $F ( u ( x ) )$ at $x = i \Delta x \pm \Delta x / 2$ . Again this local energy conservation law is more fundamental than conservation of total energy $H$ . Applying a symplectic integration method in time, we can now monitor the residual,

$$
{ \mathsf { R } } _ { i } ^ { n + 1 / 2 } : = \frac { E _ { i } ^ { n + 1 } - E _ { i } ^ { n } } { \Delta t } + \frac { F _ { i + 1 / 2 } ^ { n + 1 / 2 } - F _ { i - 1 / 2 } ^ { n + 1 / 2 } } { \Delta x } ,
$$

of a fully discretized local energy conservation law with

$$
E _ { i } ^ { n } = \frac { 1 } { 2 } ( v _ { i } ^ { n } ) ^ { 2 } + \sigma ( w _ { i } ^ { n } ) + f ( u _ { i } ^ { n } ) ,
$$

and

$$
F _ { i + 1 / 2 } ^ { n + 1 / 2 } = - \frac { 1 } { 2 } \left[ v _ { i } ^ { n } \sigma ^ { \prime } ( w _ { i + 1 } ^ { n } ) + v _ { i } ^ { n + 1 } \sigma ^ { \prime } ( w _ { i + 1 } ^ { n + 1 } ) \right] ,
$$

etc. Similar to the non-conservation of total energy under symplectic time integration, we cannot, in general, expect the residual $\mathsf { R } _ { i } ^ { n + 1 / 2 }$ to be zero. But a formal backward error analysis has been developed by MOORE AND REICH [137, 138] to explain the remarkable global and local energy conservation of symplectic PDE discretizations observed, for example, in [162].

One can also derive methods that exactly conserve energy. See, for example, [96] and [115]. Such methods will, in general, not be symplectic.

Example 2Let us discuss the sine-Gordon equation

$$
U _ { t t } = U _ { x x } - \mathsf { S i n } ( U ) .
$$

The energy density is

$$
E = \frac { 1 } { 2 } ( ( u _ { t } ) ^ { 2 } + ( u _ { x } ) ^ { 2 } ) + ( 1 - \cos u ) ,
$$

and the energy flux is

$$
\boldsymbol { F } = - u _ { t } u _ { x } .
$$

The spatial discretization (12.24)–(12.25) followed by a symplectic Euler discretization in time yields

$$
\frac { V _ { i } ^ { n + 1 } - V _ { i } ^ { n } } { \Delta t } = \frac { W _ { i + 1 } ^ { n } - W _ { i } ^ { n } } { \Delta x } - \sin ( u _ { i } ^ { n } ) , \quad \frac { U _ { i } ^ { n + 1 } - u _ { i } ^ { n } } { \Delta t } = v _ { i } ^ { n + 1 } , \quad \frac { u _ { i + 1 } ^ { n + 1 } - u _ { i } ^ { n + 1 } } { \Delta x } = w _ { i + 1 } ^ { n + 1 } .
$$

The semi-discretized energy conservation law is

$$
\frac { d } { d t } \left[ \frac { 1 } { 2 } ( v _ { i } ^ { 2 } + w _ { i } ^ { 2 } ) + ( 1 - \cos ( u _ { i } ) ) \right] + \left[ \frac { - v _ { i } w _ { i + 1 } + v _ { i - 1 } w _ { i } } { \Delta x } \right] = 0 .
$$

Note that, upon eliminating $W _ { i } ^ { n }$ and $V _ { j } ^ { n }$ , the method (12.28) is equivalent to the classical centered leap-frog scheme

$$
\frac { u _ { i } ^ { n + 1 } - 2 u _ { i } ^ { n } + u _ { i } ^ { n - 1 } } { \Delta t ^ { 2 } } = \frac { u _ { i + 1 } ^ { n } - 2 u _ { i } ^ { n } + u _ { i - 1 } ^ { n } } { \Delta x ^ { 2 } } - \mathsf { s i n } ( u _ { i } ^ { n } ) .
$$

We will come back to the local aspects of Hamiltonian PDEs and their numerical counterparts in Section 12.3. Numerical results will be presented in Section 12.3.4.

Let us briefly discuss a spatial discretization for the KdV equation (12.23). The Hamiltonian is easily discretized to

$$
H = \sum _ { i = 1 } ^ { N } \left[ \frac { 1 } { 6 } u _ { i } ^ { 3 } - \frac { 1 } { 2 } \left( \frac { u _ { i } - u _ { i - 1 } } { \Delta x } \right) ^ { 2 } \right] \Delta x .
$$

The spatial truncation of the Poisson operator $\mathcal { I }$ is potentially more challenging. However, for KdV, any skew symmetric approximation of the differential operator $\mathcal { I } = \partial _ { x }$ is sufficient and will lead to a finite-dimensional Hamiltonian system. This Hamiltonian ODE can be integrated in time by a symplectic integrator. Symplectic methods based on splitting the Hamiltonian into integrable problems are available. See, for example, QUISPEL AND MCLACHLAN [132] and ASCHER AND MCLACHLAN [9].

# 12.2.2 Particle-based methods

Standard grid-based methods are, in general, not applicable to Lagrangian fluid dynamics. This is due to the ill-conditioning of the map from an initial grid (labels) $\{ X _ { i j } ( 0 ) = a _ { i j } \}$ , $\pmb { a } _ { i j } = ( i \Delta x , j \Delta y )$ to the advected particle positions $\{ X _ { i j } ( t ) \}$ . Since this map determines the layer-depth approximation in a standard meshbased Lagrangian method via a discrete approximation of (12.18), the quality of the simulation results is usually rather poor and instabilities are observed.

On the other hand, general grid-based methods are very easy to implement for an Eulerian formulation of fluid dynamics. See DURRAN [55] for an overview of such methods. However, none of these methods respects the Hamiltonian nature of the inviscid equations of motion. This is due to the already mentioned difficulty of finding a spatial truncation of the underlying noncanonical formulation of Eulerian fluid dynamics.

All these problems disappear if we give up the grid and work with the Lagrangian instead of the reduced Eulerian formulation of inviscid fluid dynamics. The resulting so-called mesh-free methods are based on an approximation of the layer-depth $h$ via the identity (12.19). The most well-known mesh-free method for Lagrangian fluid dynamics simulations is the Smoothed Particle Hydrodynamics (SPH) method of LUCY [120] and GINGOLD AND MONAGHAN [71]. Many different variants of the basic SPH method have been proposed over the years. The first application of SPH to the shallow-water equations is due to SALMON [168]. We follow here the general framework of FRANK AND REICH [64].

Any spatial discretization will lead to a finite spatial resolution. For grid-based methods that resolution is directly related to the mesh-size $\Delta x$ . For a mesh-free method, we have to instead introduce a smoothing or filter length $\alpha > 0$ . Any fluid motion below that length scale will not be properly resolved. Hence we may replace the SWEs (12.20)–(12.21) by the ‘regularized/smoothed’ formulation

$$
\begin{array} { r l } & { \frac { \partial } { \partial t } \pmb { u } = f _ { 0 } J _ { 2 } \pmb { u } - c _ { 0 } ^ { 2 } \nabla \pmb { x } ( \pmb { \mathcal { A } } * h ) , } \\ & { \frac { \partial } { \partial t } \pmb { X } = \pmb { u } , } \end{array}
$$

where the convolution $A * h$ is defined in terms of a smooth kernel function $\psi ( x , y ) \ge 0$ satisfying

• $\psi ( x , y ) = \psi ( y , x ) \ ( \mathsf { s y m m e t r y } ) ,$ $\textstyle \int { \psi ( { \boldsymbol { x } } , { \boldsymbol { y } } ) d \boldsymbol { x } d \boldsymbol { y } } = 1$ (conservation of mass), • $\psi ( x , y ) = \phi ( | | x - y | | )$ (radial symmetry).

More explicitly, we have

$$
\begin{array} { l } { \displaystyle \left( \mathcal { A } \ast h \right) ( x , t ) = \int \left( \psi ( x , \bar { x } ) \int h _ { o } ( a ) \delta ( \bar { x } - X ( a , t ) ) d a d b \right) d \bar { x } d \bar { y } } \\ { \displaystyle = \int h _ { o } ( a ) \left( \int \psi ( x , \bar { x } ) \delta ( \bar { x } - X ( a , t ) ) d \bar { x } d \bar { y } \right) d a d b } \\ { \displaystyle = \int h _ { o } ( a ) \psi ( x , X ( a , t ) ) d a d b . } \end{array}
$$

A kernel often used in the SPH method is the Gaussian

$$
\psi ( x , y ; \alpha ) = { \frac { 1 } { \pi ^ { 3 / 2 } \alpha } } \mathrm { e } ^ { - \| x - y \| ^ { 2 } / \alpha ^ { 2 } } ,
$$

where $\alpha > 0$ is the smoothing length scale.

To set up the numerical method, we introduce a mesh in label space with equally spaced grid points $\left\{ a _ { i j } \right\}$ and mesh-size $\Delta a = \Delta b$ . The grid points are enumerated by integers $k = 1 , \dots , N$ , which serve as discrete labels, so the map $s : ( i , j ) \to k$ is one-to-one. The particle positions at time $t$ are denoted by $\pmb { X } _ { k } ( t )$ and initially $\pmb { X } _ { k } ( 0 ) = \pmb { a } _ { i j }$ . Each particle has a “mass” $m _ { k } = h _ { o } ( a _ { i j } )$ and a velocity $u _ { k } ( t ) \in \mathbb { R } ^ { 2 }$ . The layer depth at $\pmb { X } _ { k } ( t )$ is then approximated by

$$
h _ { k } ( t ) = \sum _ { I } m _ { I } \psi ( { \pmb X } _ { k } ( t ) , { \pmb X } _ { I } ( t ) ) \Delta a \Delta b .
$$

Similarly, any integral of the form

$$
I = \int h _ { o } ( \pmb { a } ) w ( \pmb { X } ( \pmb { a } ) ) d \ b { a } d \ b { b }
$$

is approximated by

$$
I \approx \sum _ { k } m _ { k } w _ { k } \Delta a \Delta b , \quad \quad w _ { k } = w ( \pmb { X } _ { k } ) .
$$

From here on we can follow exactly the same approach as outlined for the symplectic discretization of grid-based methods. The Hamiltonian functional

$$
{ \mathcal { H } } = { \frac { 1 } { 2 } } \int { \frac { \mathbf { p } \cdot \mathbf { p } } { h _ { o } } } d a d b + { \frac { c _ { 0 } ^ { 2 } } { 2 } } \int h _ { o } \left( A * h \right) d a d b
$$

is approximated by the Hamiltonian

$$
{ \cal H } = \frac { 1 } { 2 } \left( \sum _ { k = 1 } ^ { N } \frac { 1 } { m _ { k } } \| p _ { k } \| ^ { 2 } + c _ { 0 } ^ { 2 } \sum _ { k , l = 1 } ^ { N } m _ { k } m _ { I } \psi ( X _ { k } , X _ { I } ) \Delta a \Delta b \right) \Delta a \Delta b ,
$$

${ \pmb p } _ { k } = m _ { k } { \pmb u } _ { k }$ , and (12.22) is replaced by the symplectic form

$$
\bar { \omega } _ { N } : = \sum _ { k = 1 } ^ { N } \left( \frac { m _ { k } f _ { 0 } } { 2 } d \pmb { X } _ { k } \wedge \pmb { J } _ { 2 } d \pmb { X } _ { k } + d \pmb { p } _ { k } \wedge d \pmb { X } _ { k } \right) \Delta a \Delta b .
$$

The resulting equations of motion are

$$
\begin{array} { r l } & { \displaystyle \frac { d } { d t } \pmb { u } _ { k } = f _ { 0 } { J } _ { 2 } \pmb { u } _ { k } - c _ { 0 } ^ { 2 } \sum _ { I = 1 } ^ { N } \bar { m } _ { I } \nabla _ { { X } _ { k } } \psi ( { { X } } _ { k } , { { X } } _ { I } ) , } \\ & { \displaystyle \frac { d } { d t } { { X } } _ { k } = \pmb { u } _ { k } , } \end{array}
$$

$k = 1 , \dots , N$ , where we have made use of the symmetry of $\psi ( x , y )$ as well as $\begin{array} { r } { { \pmb p } _ { k } / m _ { k } = { \pmb u } _ { k } = \frac { d } { d t } { \pmb X } _ { k } } \end{array}$ , and defined

$$
\bar { m } _ { k } = m _ { k } \Delta a \Delta b .
$$

Note that the mesh $\{ a _ { i j } \}$ is only needed at time $t = 0$ to give each particle $\boldsymbol { x } _ { k }$ an initial position and velocity and to allocate a mass $m _ { k }$ .

The behavior of the particle method depends crucially on a proper choice of the kernel $\psi$ . The classical SPH method uses a radially symmetric kernel of the form $\psi ( x , y ) = \phi ( | | x - y | | )$ , with $\phi ( r )$ , for example, a Gaussian or a spline function.

In [63], FRANK, GOTTWALD, AND REICH dropped the radial symmetry condition and adopted the following somewhat different strategy called the Hamiltonian Particle-Mesh (HPM) method. Following the standard particle-mesh procedure [21, 85], one defines a computational grid $\{ x _ { m n } \}$ , ${ x _ { m n } } = ( m \Delta x , n \Delta y )$ , with, for simplicity, $\Delta x \ : = \ : \Delta y$ . The choice $\Delta x = 4 \Delta a$ seems to work well in practice. This implies that, initially, there are 16 particles per computational grid cell. We introduce the interpolation function

$$
\phi ( x - X _ { k } ) : = \frac { 1 } { \Delta x \Delta y } \rho \left( \frac { | x - X _ { k } | } { \Delta x } \right) \rho \left( \frac { | y - Y _ { k } | } { \Delta y } \right) ,
$$

where $\rho ( r )$ is given by the cubic spline

$$
\rho ( r ) = \left\{ \begin{array} { l l } { \frac 2 3 - r ^ { 2 } + \frac 1 2 r ^ { 3 } , r \le 1 } \\ { \frac 1 6 ( 2 - r ) ^ { 3 } , \quad \quad 1 < r \le 1 \cdot } \\ { 0 , \quad \quad \quad r > 2 } \end{array} \right.
$$

We define the scaling factor

$$
\gamma = \int \phi ( x ) d x d y
$$

and approximate the layer-depth $h ^ { m n }$ at a grid point $x _ { m n }$ by

$$
h ^ { m n } ( t ) = \sum _ { k } \frac { m _ { k } } { \gamma } \phi _ { m n } ( { \pmb X } _ { k } ( t ) ) \Delta a \Delta b , \qquad \phi _ { m n } ( { \pmb X } ) : = \phi ( x _ { m n } - { \pmb X } ) .
$$

Let $\pmb { \mathsf { S } } = \{ S _ { p q } ^ { m n } \}$ denote the representation of a spatial averaging operator $S$ over the given grid $\{ x _ { m n } \}$ . 4 Since the cubic splines form a partition of unity on the grid, i.e.

$$
\sum _ { m n } \phi _ { m n } ( { \pmb x } ) = 1 ,
$$

we can define a continuous approximation of a smoothed/averaged layer-depth in space by means of

$$
\left( \mathcal { A } \ast h \right) ( x , t ) = \sum _ { p q , m n } \phi _ { p q } ( x ) S _ { m n } ^ { p q } h ^ { m n } ( t ) ,
$$

and the kernel function $\psi$ , as used in the HPM method, is finally given by

$$
\psi ( x , y ) = \frac { 1 } { \gamma } \sum _ { p q , m n } \phi _ { m n } ( x ) S _ { p q } ^ { m n } \phi _ { p q } ( y ) .
$$

Note that

$$
\int \psi ( x , \bar { x } ) d x d y = \sum _ { m n , p q } S _ { p q } ^ { m n } \phi _ { p q } ( \bar { x } ) = \sum _ { p q } \phi _ { p q } ( \bar { x } ) = 1 ,
$$

and the constructed basis function is symmetric and satisfies conservation of mass.

It is found that the inverse of the modified Helmholtz operator $H = 1 - \alpha ^ { 2 } \nabla _ { x } ^ { 2 }$ computed over the grid $\{ x _ { m n } \}$ using FFT provides a good choice for the matrix operator S. The smoothing length $\alpha$ is typically chosen between $\alpha = 2 \Delta x$ and $\alpha = 4 \Delta x$ . We assume that $\alpha$ is shorter than the Rossby deformation radius $L _ { R }$ . Hence the matrix operator S will filter out high-frequency waves but will leave the balanced geostrophic layer-depth (12.17) essentially unaffected.

Note that the mesh has only been introduced to efficiently compute the kernel function (12.32).

The geometric conservation properties of the particle method, including conservation of circulation and potential vorticity, have been discussed in [64] and [32].

4The approximation S should be symmetric and $\textstyle \sum _ { p q } S _ { p q } ^ { m n } = 1$