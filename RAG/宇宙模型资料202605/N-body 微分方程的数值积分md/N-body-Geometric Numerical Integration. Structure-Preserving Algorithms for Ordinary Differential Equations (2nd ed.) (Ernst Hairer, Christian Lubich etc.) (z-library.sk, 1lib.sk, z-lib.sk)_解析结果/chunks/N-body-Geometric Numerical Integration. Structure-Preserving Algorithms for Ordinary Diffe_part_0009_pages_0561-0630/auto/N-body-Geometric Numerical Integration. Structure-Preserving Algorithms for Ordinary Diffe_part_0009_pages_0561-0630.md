Rescaling Positions and Momenta.We transform

$$
q _ { 0 } = \check { q } _ { 0 } , \quad q _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } \check { q } _ { 1 } , \quad t = \check { t }
$$

with the conjugate momenta

$$
\check { p } _ { 0 } = p _ { 0 } , \quad \check { p } _ { 1 } = \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } p _ { 1 } , \quad \check { E } = - \frac { 1 } { 2 } \check { q } _ { 1 } ^ { T } \varepsilon ^ { 1 / 2 } \Omega ^ { - 3 / 2 } \dot { \Omega } p _ { 1 } + E .
$$

In the new variables,the Hamiltonian becomes (we omit the haceks on all variables)

$$
\begin{array} { l l l } { H } & { = } & { \displaystyle \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \\ & {  } & {  + q ^ { T } \check { K } ( t ) p + U ( T ( t ) q , t ) + E } \end{array}
$$

with

$$
\begin{array} { r c l } { { \check { K } } } & { { = } } & { { \left( \begin{array} { c c } { { K _ { 0 0 } } } & { { \varepsilon ^ { - 1 / 2 } K _ { 0 1 } \varOmega ^ { 1 / 2 } } } \\ { { \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } K _ { 1 0 } } } & { { \varOmega ^ { - 1 / 2 } K _ { 1 1 } \varOmega ^ { 1 / 2 } + \frac { 1 } { 2 } \varOmega ^ { - 1 } \dot { \varOmega } } } \end{array} \right) } } \\ { { \cal T } } & { { = } } & { { \left( T _ { 0 } \mid \varepsilon ^ { 1 / 2 } T _ { 1 } \right) = \left( \begin{array} { c c } { { T _ { 0 0 } } } & { { \varepsilon ^ { 1 / 2 } T _ { 0 1 } } } \\ { { T _ { 1 0 } } } & { { \varepsilon ^ { 1 / 2 } T _ { 1 1 } } } \end{array} \right) = C Q \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { \varepsilon ^ { 1 / 2 } \varOmega ^ { - 1 / 2 } } } \end{array} \right) . } } \end{array}
$$

Eliminating theSingular Block.Wenextremove the $\mathcal { O } ( \varepsilon ^ { - 1 / 2 } )$ off-diagonal block in $\dot { K }$ bythecanonical transformation

$$
- p _ { 1 } = - \overline { { p } } _ { 1 } + \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } K _ { 0 1 } ^ { T } q _ { 0 } , \quad q _ { 0 } = \overline { { q } } _ { 0 } , \quad t = \bar { t }
$$

with the conjugate variables

$$
\tilde { \tau } _ { 1 } = q _ { 1 } , \quad \overline { { { p } } } _ { 0 } = p _ { 0 } + \varepsilon ^ { 1 / 2 } K _ { 0 1 } \Omega ^ { - 1 / 2 } q _ { 1 } , \quad \overline { { { E } } } = E + \varepsilon ^ { 1 / 2 } q _ { 0 } ^ { T } \frac { d } { d t } \big ( K _ { 0 1 } \Omega ^ { - 1 / 2 } \big ) q _ { 1 }
$$

Inthese coordinates,theHamiltonian takes the form (we omit all bars)

$$
\begin{array} { r c l } { H } & { = } & { \displaystyle \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \\ & & { \displaystyle + q ^ { T } L ( t ) p + \frac { 1 } { 2 } q ^ { T } S ( t ) q + U ( T ( t ) q , t ) + E } \end{array}
$$

with the lower block-triangular matrix

$$
\begin{array} { l c l } { { { \cal L } } } & { { = } } & { { \left( \begin{array} { c c } { { L _ { 0 0 } } } & { { 0 } } \\ { { \varepsilon ^ { 1 / 2 } L _ { 1 0 } } } & { { L _ { 1 1 } } } \end{array} \right) } } \\ { { } } & { { = } } & { { \left( \begin{array} { c c } { { K _ { 0 0 } } } & { { 0 } } \\ { { \varepsilon ^ { 1 / 2 } \Omega ^ { - 1 / 2 } ( K _ { 1 0 } + K _ { 0 1 } ^ { T } ) } } & { { \varOmega ^ { - 1 / 2 } K _ { 1 1 } \varOmega ^ { 1 / 2 } + \frac { 1 } { 2 } \varOmega ^ { - 1 } \ddot { \varOmega } } } \end{array} \right) } } \end{array}
$$

and the symmetric matrix

$$
S = \left( \begin{array} { c c } { { \ S _ { 0 0 } } } & { { \varepsilon ^ { 1 / 2 } S _ { 0 1 } } } \\ { { \varepsilon ^ { 1 / 2 } S _ { 1 0 } } } & { { \varepsilon S _ { 1 1 } } } \end{array} \right) ,
$$

where

$$
\begin{array} { l } { { S _ { 0 0 } = - K _ { 0 1 } K _ { 0 1 } ^ { T } , } } \\ { { S _ { 0 1 } = S _ { 1 0 } ^ { T } = - K _ { 0 0 } K _ { 0 1 } \Omega ^ { - 1 / 2 } } } \\ { { \phantom { S _ { 0 0 } = - K _ { 0 1 } \Omega ^ { - 1 / 2 } ( \Omega ^ { 1 / 2 } K _ { 1 1 } ^ { T } \Omega ^ { - 1 / 2 } + \frac { 1 } { 2 } \Omega ^ { - 1 } \dot { \Omega } ) - \frac { d } { d t } \big ( K _ { 0 1 } \Omega ^ { - 1 / 2 } \big ) , } } } \\ { { S _ { 1 1 } = \Omega ^ { - 1 / 2 } ( - K _ { 1 0 } K _ { 0 1 } = K _ { 0 1 } ^ { T } K _ { 1 0 } ^ { T } + K _ { 0 1 } ^ { T } K _ { 0 1 } ) \Omega ^ { - 1 / 2 } , } } \end{array}
$$

Wenote that with the energy bound(2.2）we now have

$$
p _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) , \quad q _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) .
$$

Equations of Motion.Thedifferential equationsnow take the form

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { f _ { 0 } ( p , q , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + g _ { 0 } ( q , t ) } \\ { \left( \frac { \dot { p } _ { 1 } } { \dot { q } _ { 1 } } \right) } & { = } & { \frac { 1 } { \varepsilon } \left( \begin{array} { c c } { 0 } & { - \varOmega ( t ) } \\ { \varOmega ( t ) } & { 0 } \end{array} \right) \left( \frac { p _ { 1 } } { q _ { 1 } } \right) + \left( \begin{array} { c c } { \dot { f } _ { 1 } ( p , q , t ) } \\ { g _ { 1 } ( q , t ) } \end{array} \right) } \end{array}
$$

with the functions bounded uniformly in $\succ$ ，

$$
\binom { f _ { 0 } } { f _ { 1 } } = - L ( t ) p - \bar { S } ( t ) q - T ( t ) ^ { T } \nabla U ( T ( t ) q , t ) , \quad \binom { g _ { 0 } } { g _ { 1 } } = L ( t ) ^ { T } q .
$$

Thematrix in thesystem is diagonalized byaconstant unitary matrix:with

$$
{ \it \Delta } { \it \Gamma } = \frac { 1 } { \sqrt { 2 } } \left( \begin{array} { c c } { { I } } & { { I } } \\ { { - i I } } & { { i I } } \end{array} \right)
$$

wehave

$$
\left( \begin{array} { c c } { { 0 } } & { { - \Omega ( t ) } } \\ { { \Omega ( t ) } } & { { 0 } } \end{array} \right) = { \cal T } \left( \begin{array} { c c } { { i \Omega ( t ) } } & { { \cdot \quad 0 } } \\ { { 0 } } & { { - i \Omega ( t ) } } \end{array} \right) { \cal T } ^ { * } .
$$

Remark.Action-angle variables $p _ { 1 , j } = \sqrt { a _ { j } } \cos \theta _ { j }$ ${ q _ { 1 , j } = \sqrt { a _ { j } } \sin \theta _ { j } }$ for the harmonic oscillators would now put the Hamiltonianinto theform $H = \textstyle { \frac { 1 } { \varepsilon } } \omega ( t ) \cdot a +$ $G ( a , \theta , p _ { 0 } , q _ { 0 } , t )$ ,which could be studied further using averaging techniques,that is, using coordinate transforms that reduce the dependence on the angles in the Hamiltonian;see Neishtadt (1984) for averaging out up to an exponentially small remainderinthe case ofa single high frequency.The first-order averaging transformmight bedone numerically (cf.the formulasin Sect.XII.2),but the higher-order transformsinvolve increasingly higherderivatives of the functions involved and thereforebecome impractical from the numerical viewpoint.For systemswith several frequencies the averaging transforms require multi-dimensional integrals which are expensive to compute.For our numerical purposes we therefore continue diferently, adaptingthe adiabatic transformation of Sect.XIV.1.1.

TheSystemin Adiabatic Variables.Let thediagonal phase matrix be givenas

$$
\varPhi ( t ) = \int _ { t _ { 0 } } ^ { t } A ( s ) d s \quad \mathrm { ~ w i t h ~ } A ( t ) = \left( \begin{array} { c c } { \varOmega ( t ) } & { 0 } \\ { 0 } & { - \varOmega ( t ) } \end{array} \right) .
$$

Ourfinal transformation follows (1.4) and sets

$$
\eta = \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) \varGamma ^ { \ast } \left( \begin{array} { c } { p _ { 1 } } \\ { q _ { 1 } } \end{array} \right) .
$$

The factor $\varepsilon ^ { - 1 / 2 }$ is chosen forconvenience sothat (2.12)implies

$$
\eta = \mathcal { O } ( 1 ) .
$$

Weremark thatup to nowalltransformationswere invariant underrescaling $\varepsilon \longrightarrow \sigma \varepsilon$ and $A ( t ) \longrightarrow \sigma ^ { 2 } A ( t )$ ,buthere we havechosen to giveup this invariance in favourof (2.17).Note that $\eta$ is of the form

$$
\eta = \varepsilon ^ { - 1 / 2 } { \cal T } ^ { * } \left( { \pi \atop \rho } \right) = { \frac { \varepsilon ^ { - 1 / 2 } } { \sqrt { 2 } } } \left( { \pi + i \rho \atop \pi - i \rho } \right)
$$

with real vectors $\pi , \rho$ satisfying

$$
\pi + i \rho = \exp \Bigl ( - \frac { i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \varOmega ( s ) d s \Bigr ) ( p _ { 1 } + i q _ { 1 } ) .
$$

Wedenote the inverse transformas

$$
\left( { \begin{array} { c } { p _ { 1 } } \\ { q _ { 1 } } \end{array} } \right) = \varepsilon ^ { 1 / 2 } \left( { \begin{array} { c } { P _ { 1 } ( t ) } \\ { Q _ { 1 } ( t ) } \end{array} } \right) \eta \quad { \mathrm { ~ w i t h ~ } } \quad \left( { \begin{array} { c } { P _ { 1 } ( t ) } \\ { Q _ { 1 } ( t ) } \end{array} } \right) = T \exp \left( { \frac { i } { \varepsilon } } \varPhi ( t ) \right) .
$$

Together with $\begin{array} { r } { e = E + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( t ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( t ) q _ { 1 } } \end{array}$ and unaltered $p _ { 0 } , q _ { 0 } , t$ thisyields a canonical transformation $( p _ { 0 } , \pi , e , q _ { 0 } , \rho , t ) \mapsto ( p _ { 0 } , p _ { 1 } , E , q _ { 0 } , q _ { 1 } , t )$ TheHamiltonianreads in these variables

$$
\begin{array} { r } { H = \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + q ^ { T } L ( t ) p + \frac { 1 } { 2 } q ^ { T } S ( t ) q + U ( T ( t ) q , t ) + e , } \end{array}
$$

where on the right-hand side the components $p _ { 1 } , q _ { 1 }$ are expressed in terms of $\eta$ and $\pi , \rho$ by(2.20) and(2.18).The equations of motion now become

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { f _ { 0 } ( p , q , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + g _ { 0 } ( q , t ) } \\ { \dot { \eta } } & { = } & { \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) T ^ { * } \left( \begin{array} { c } { f _ { 1 } ( p , q , t ) } \\ { g _ { 1 } ( q , t ) } \end{array} \right) } \end{array}
$$

with $p _ { 1 } , q _ { 1 }$ expressed in terms of $\eta$ by(2.20).Written out,the differential equations for $p _ { 0 } , q _ { 0 }$ read

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - L _ { 0 0 } p _ { 0 } - S _ { 0 0 } q _ { 0 } - T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } , t ) - \varepsilon S _ { 0 1 } Q _ { 1 } \eta } \\ & & { - T _ { 0 } ^ { T } \Big ( \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) - \nabla U ( T _ { 0 } q _ { 0 } , t ) \Big ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + L _ { 0 0 } ^ { T } q _ { 0 } + \varepsilon L _ { 1 0 } ^ { T } Q _ { 1 } \eta . } \end{array}
$$

Thematrix multiplying $\eta$ aftersubstituting the expressions $f _ { 1 }$ and $g _ { 1 }$ in the differential equation for $\eta$ becomes,apart from the oscillatory exponentials,

$$
\begin{array} { r c l } { W } & { = } & { { \cal { T } } ^ { * } \left( \begin{array} { c c } { - { \cal { L } } _ { 1 1 } } & { - \varepsilon { \cal { S } } _ { 1 1 } } \\ { 0 } & { { \cal { L } } _ { 1 1 } ^ { T } } \end{array} \right) { \cal { T } } ^ { } \quad - } \\ & { = } & { - { \frac { 1 } { 2 } } \left( \begin{array} { c c } { { \cal { L } } _ { 1 1 } - { \cal { L } } _ { 1 1 } ^ { T } } & { { \cal { L } } _ { 1 1 } + { \cal { L } } _ { 1 1 } ^ { T } } \\ { { \cal { L } } _ { 1 1 } + { \cal { L } } _ { 1 1 } ^ { T } } & { { \cal { L } } _ { 1 1 } - { \cal { L } } _ { 1 1 } ^ { T } } \end{array} \right) - { \frac { i \varepsilon } { 2 } } \left( \begin{array} { c c } { - { \cal { S } } _ { 1 1 } } & { { \cal { S } } _ { 1 1 } } \\ { - { \cal { S } } _ { 1 1 } } & { { \cal { S } } _ { 1 1 } } \end{array} \right) , } \end{array}
$$

which has adiagonal of size ${ \mathcal { O } } ( \varepsilon ) .$ The equation for $\eta$ then reads

$$
\begin{array} { r l } & { \dot { \eta } ~ = ~ \mathrm { e x p } \left( - \frac { i } { \varepsilon } \Phi ( t ) \right) W ( t ) \mathrm { e x p } \left( \frac { i } { \varepsilon } \Phi ( t ) \right) \eta } \\ & { \qquad = P _ { 1 } ^ { \ast } \left( L _ { 1 0 } p _ { 0 } + S _ { 1 0 } \bar { q } _ { 0 } + T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) \right) . } \end{array}
$$

Thematrix multiplying $\eta$ isbounded independentlyof $\varepsilon$ ,but highly oscillatory.Note that thecoordinate transforms leadingto(2.21),(2.23)are linearand can becarried outby standard numerical linearalgebra routines.

Adiabatic Invariants.We suppose that the eigenfrequencies $\omega _ { j } ( t )$ remain separated andbounded away from O:there are $\delta > 0$ and $c > 0$ such that for any pair $\omega _ { j } ( t )$ and $\omega _ { k } ( t )$ with $j \neq k ( j , k = 1 , \ldots , m )$ ,the lower bounds

$$
| \omega _ { j } ( t ) - \omega _ { k } ( t ) | \geq \delta , \quad \ \omega _ { j } ( t ) \geq c
$$

hold for all $t$ underconsideration.Under condition (2.24） the right-hand side $r ( t )$ inthedifferential equation for $\eta$ consists only of oscillatory terms,up to $\mathcal { O } ( \varepsilon )$ (No smooth terms larger than $\mathcal { O } ( \varepsilon )$ arise because the matrix $W$ hasa diagonal of size $\mathcal { O } ( \varepsilon )$ ）Itthen followsbypartial integration that

$$
\int _ { 0 } ^ { t } r ( s ) d s = \mathcal { O } ( \bar { \varepsilon } ) ~ \mathrm { f o r } ~ t \leq \mathrm { C o n s t . } ,
$$

andasin（1.6）we then obtain

$$
\eta ( t ) = \eta ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

The functions defined by

$$
I _ { j } = | \eta _ { j } | ^ { 2 } \qquad ( j = 1 , \ldots , m )
$$

are thusadiabatic invariants:

$$
I _ { j } ( t ) = I _ { j } ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

Starting fromaHamiltonian system (2.1),where the mass matrix equals the identity andthestifnessmatrixislreadyagonalwefindtat $I _ { j }$ is the action (energy divided by frequency)

$$
I _ { j } ( t ) = \frac { 1 } { \omega _ { j } ( t ) } \left( \frac { 1 } { 2 } p _ { j } ( t ) ^ { 2 } + \frac { \omega _ { j } ( t ) ^ { 2 } } { 2 \varepsilon ^ { 2 } } q _ { j } ( t ) ^ { 2 } \right) ,
$$

which fora constant frequency $\omega _ { j }$ becomes aconstant multiple of the oscillatory energyconsidered in Sect.XIII.9.

The Slow Limit System.As $\varepsilon  0$ ,the evolution of the slow variables $p _ { 0 } , q _ { 0 }$ is governed by the equations

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - L _ { 0 0 } ( t ) p _ { 0 } - S _ { 0 0 } ( t ) q _ { 0 } - T _ { 0 } ( t ) ^ { T } \nabla U ( T _ { 0 } ( t ) q _ { 0 } , t ) } \\ { \dot { q } _ { 0 } } & { = } & { p _ { 0 } + L _ { 0 0 } ( t ) ^ { T } q _ { 0 } } \end{array}
$$

which is the system with the time-dependent Hamiltonian

$$
H _ { 0 } ( p _ { 0 } , q _ { 0 } , t ) = \frac { 1 } { 2 } p _ { 0 } ^ { T } p _ { 0 } + q _ { 0 } ^ { T } L _ { 0 0 } ( t ) p _ { 0 } + \frac { 1 } { 2 } q _ { 0 } ^ { T } S _ { 0 0 } ( t ) q _ { 0 } + U ( T _ { 0 } ( t ) q _ { 0 } , t ) .
$$

Weconclude this subsection with a simple illustration of the above procedure.

Example2.1 (Harmonic oscillator with slowly varying frequency).For the scalar second-orderdifferential equation

$$
\ddot { q } + \frac { \omega ( t ) ^ { 2 } } { \varepsilon ^ { 2 } } q = 0 ,
$$

where $\omega ( t )$ isboundedaway fromOand hasaderivative bounded independently of $\boldsymbol { \mathsf { E } }$ ,theabove transformations simplify considerably.TheHamiltonian in the original variables isalready of the form

$$
H = \frac { 1 } { 2 } p ^ { 2 } + \frac { 1 } { 2 } \frac { \omega ( t ) ^ { 2 } } { \varepsilon ^ { 2 } } q ^ { 2 } ,
$$

and hencethe first two transformations are not needed at all,and there are no slow variables $p _ { 0 } , q _ { 0 }$ .Therescaling transformation yieldstheHamiltonian(2.1O)in the form

$$
H = \frac { \omega ( t ) } { 2 \varepsilon } \check { p } ^ { 2 } + \frac { \omega ( t ) } { 2 \varepsilon } \check { q } ^ { 2 } + \frac { 1 } { 2 } \frac { \ddot { \omega } ( t ) } { \omega ( t ) } \check { p } \check { q } .
$$

With the adiabatic transformation (2.19）we thus represent the solution as

$$
\sqrt { \frac { \varepsilon } { \omega ( t ) } } \dot { q } ( t ) + i \sqrt { \frac { \omega ( t ) } { \varepsilon } } q ( t ) = \exp \Bigl ( \frac { i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \omega ( s ) d s \Bigr ) \zeta ( t ) ,
$$

where $\zeta = \pi + i \rho$ solves the differential equation

$$
\dot { \zeta } ( t ) = - \frac { 1 } { 2 } \frac { \dot { \omega } ( t ) } { \omega ( t ) } \exp \Bigl ( - \frac { 2 i } { \varepsilon } \int _ { t _ { 0 } } ^ { t } \omega ( s ) d s \Bigr ) \zeta ( t )
$$

and satisfies $\zeta ( t ) = \zeta ( t _ { 0 } ) { \bigl ( } 1 + { \mathcal { O } } ( \varepsilon ) { \bigr ) }$ for $t = \mathcal { O } ( 1 ) .$ (In theabove notation,we have n=e-1/（））Thectin

$$
I ( t ) = \frac { 1 } { \omega ( t ) } \left( \frac { 1 } { 2 } { \dot { q } } ( t ) ^ { 2 } + \frac { \omega ( t ) ^ { 2 } } { 2 \varepsilon ^ { 2 } } q ( t ) ^ { 2 } \right)
$$

isanadiabatic invariant.

# XIV.2.2Adiabatic Integrators

Asimple long-time-step integrator for the oscillatory mechanical system with timedependent Hamiltonian(2.1） nowreadsas follows:

-Solve the slow limit system(2.29) for $p _ { 0 } , q _ { 0 }$ ,e.g.,bytheStormer-Verlet method.   
-Keep the adiabatic variable $\eta$ constant at its initial value.

Underthecondition of bounded energy (2.1) and the frequency separation condition (2.24）,the error in $\eta$ isthen $\mathcal { O } ( \varepsilon )$ overintervals $t \leq$ Const.by(2.26).The difference between the solutions of(2.21）and the limit equation (2.29)is bounded by $O ( \varepsilon ^ { 2 } )$ for $t \leq \mathrm { C o n s t . }$ ,ascan be shown by forming the difference of the equations,integrating,estimating the integral of the extra terms by $\mathcal { O } ( \varepsilon ^ { 2 } )$ using（2.26）and partial integration,and applying the Gronwall inequality.In the original variables $p , q$ of (2.1) this yieldsan error $\mathcal { O } ( \varepsilon ^ { 2 } )$ in the positions and $\mathcal { O } ( \varepsilon )$ in the momenta.

Morerefined integratorsare needed for two independent reasons:

1. to keep control of $\eta$ on subintervals where the frequencies are not well separated andwhere $\eta$ may thusdeviate from its near-constant value; 2.to obtain higher order of approximation on intervals with separated frequencies.

Wesimplify the following presentation by assuming that the potential $U$ is quadratic:

$$
U ( q , t ) = \frac { 1 } { 2 } q ^ { T } G ( t ) q ,
$$

withasymmetric matrix $G ( t )$ depending smoothly on $t$ .We leave the required modifications for general $U$ to theinterested reader.Alternatively,themethodwith $U = 0$ canbe used in the splittingapproach of Sect.XIV.2.3below.

Anadiabatic integratoras described in Sect.XIV.1.2 can be extended to(2.23) and combined with a symmetric splittng between the weakly coupled systems (2.21)and(2.23):we beginwith a symplectic Euler half-step for $p _ { 0 } , q _ { 0 }$ (denoting the time levels by superscripts),

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 / 2 } } } & { { = } } & { { p _ { 0 } ^ { 0 } - { \displaystyle \frac { h } { 2 } } \Bigl ( { \cal L } _ { 0 0 } p _ { 0 } ^ { 1 / 2 } + ( S _ { 0 0 } + T _ { 0 } ^ { T } G T _ { 0 } ) q _ { 0 } ^ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \qquad + \varepsilon \bigl ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } \bigr ) Q _ { 1 } ^ { - } \eta ^ { 0 } \Bigr ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 0 } ^ { 1 / 2 } } } & { { = } } & { { q _ { 0 } ^ { 0 } + { \displaystyle \frac { h } { 2 } } \Bigl ( p _ { 0 } ^ { 1 / 2 } + { \cal L } _ { 0 0 } ^ { T } q _ { 0 } ^ { 0 } + \varepsilon { \cal L } _ { 1 0 } ^ { T } { \mathcal Q } _ { 1 } ^ { - } \eta ^ { 0 } \Bigr ) . } } \end{array}
$$

Here the matrix functions $L _ { 0 0 }$ , $L _ { 1 0 }$ ， $S _ { 0 0 }$ ， $S _ { 0 1 }$ ， $T _ { 0 }$ , $T _ { 1 }$ are evaluated at $t _ { 1 / 2 } = t _ { 0 } +$ $h / 2$ ,and $\mathcal { Q } _ { 1 } ^ { - }$ is theaverage of the oscillatory function $Q _ { 1 }$ of (2.20)over the halfstep,

$$
\mathcal { Q } _ { 1 } ^ { - } \approx \frac { 2 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } / 2 } Q _ { 1 } ( t ) d t ,
$$

obtained witha linear approximation of the phase $\varPhi ( t )$ and analytic computation of theintegral.We thenmakea fullstep for $\eta$ with Eq.(2.23) like in(1.12)，

$$
\begin{array} { r c l } { \eta ^ { 1 } } & { = } & { \eta ^ { 0 } + \hbar \Big ( E ( \phi ) \bullet \mathcal { Z } \bullet W \Big ) \frac { 1 } { 2 } ( \eta ^ { 1 } + \eta ^ { 0 } ) } \\ & & { \qquad - \hbar \mathcal { P } _ { 1 } ^ { * } \Big ( L _ { 1 0 } p _ { 0 } ^ { 1 / 2 } + ( S _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) q _ { 0 } ^ { 1 / 2 } \Big ) , } \end{array}
$$

where again all matrix functionsare evaluated at $t _ { 1 / 2 }$ ,and $\mathcal { P } _ { 1 }$ is the linear-phase approximation to the average

$$
\mathcal { P } _ { 1 } \approx \frac { 1 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } } P _ { 1 } ( t ) d t .
$$

Thematrix $W$ is as in (2.22),but with $S _ { 1 1 }$ replaced by $S _ { 1 1 } + T _ { 1 } ^ { T } G T _ { 1 } .$ The stepis completedbyahalf-step for $p _ { 0 } , q _ { 0 }$ with the adjoint symplectic Euler method:

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 } } } & { { = } } & { { p _ { 0 } ^ { 1 / 2 } - \displaystyle \frac { h } { 2 } \Big ( { \cal L } _ { 0 0 } p _ { 0 } ^ { 1 / 2 } + ( { \cal S } _ { 0 0 } + T _ { 0 } ^ { T } { \cal G } T _ { 0 } ) q _ { 0 } ^ { 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + \varepsilon \big ( { \cal S } _ { 0 1 } + T _ { 0 } ^ { T } { \cal G } T _ { 1 } \big ) { \cal Q } _ { 1 } ^ { + } \eta ^ { 1 } \Big ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 0 } ^ { 1 } } } & { { = } } & { { q _ { 0 } ^ { 1 / 2 } + \displaystyle \frac { h } { 2 } \Big ( p _ { 0 } ^ { 1 / 2 } + { \cal L } _ { 0 0 } ^ { T } q _ { 0 } ^ { 1 } + \varepsilon { \cal L } _ { 1 0 } ^ { T } { \cal Q } _ { 1 } ^ { + } \eta ^ { 1 } \Big ) , } } \end{array}
$$

where thematrix functions are still evaluated at $t _ { 1 / 2 }$ ,and $\mathcal { Q } _ { 1 } ^ { + }$ approximates the averageof $Q _ { 1 }$ over the second half-step.

We now give local error bounds for this integrator,under conditions that include thecase of an avoided crossing of frequencies.

Theorem2.2.Suppose that the functionsin(2.1） are smooth and the frequencies satisfy(2.24)withminimal distance $\delta > 0$ for $t _ { 0 } \le t \le t _ { 0 } + h$ andthe orthogonalmatrix $Q _ { * } ( t )$ of(2.7),which diagonalizesthe nonsingular part ofthe stiffness matrix,hasderivativesbounded by $\dot { Q } _ { * } ( t ) = \mathcal { O } ( \delta ^ { - 1 } )$ , $\ddot { Q } _ { * } ( t ) = \mathcal { O } ( \delta ^ { - 2 } )$ Assume furthertheenergybound(2.2)fortheinitialvalues.Then,the localerrorofmethod (2.30)-(2.32)is bounded by

$$
\begin{array} { r c l } { { p _ { 0 } ^ { 1 } - p _ { 0 } ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 3 } / \delta ^ { 2 } ) + \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } } \\ { { q _ { 0 } ^ { 1 } - q _ { 0 } ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 3 } / \delta ) + \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } } \\ { { \eta ^ { 1 } - \eta ( t _ { 0 } + h ) } } & { { = } } & { { \mathcal { O } ( h ^ { 2 } / \delta ^ { 2 } ) . } } \end{array}
$$

Theconstantssymbolizedby $\mathcal { O }$ do not depend on $\varepsilon$ ， $h ,$ and $\delta$

Proof.(a) Under the given conditions we have

$$
\begin{array} { r l } & { K _ { 0 0 } = \mathcal { O } ( 1 ) , K _ { 0 1 } = \mathcal { O } ( 1 ) , K _ { 1 0 } = \mathcal { O } ( 1 ) , K _ { 1 1 } = \mathcal { O } ( \delta ^ { - 1 } ) , \mathrm { a n d } } \\ & { } \\ & { \dot { K } _ { 0 0 } = \mathcal { O } ( 1 ) , \dot { K } _ { 0 1 } = \mathcal { O } ( \delta ^ { - 1 } ) , \dot { K } _ { 1 0 } = \mathcal { O } ( \delta ^ { - 1 } ) , \dot { K } _ { 1 1 } = \mathcal { O } ( \delta ^ { - 2 } ) } \end{array}
$$

This yields the bounds

$$
L _ { 0 0 } , L _ { 1 0 } , S _ { 0 0 } , S _ { 1 1 } = O ( 1 )
$$

and similarly for theirderivatives,and

$$
\begin{array} { r } { L _ { 1 1 } , S _ { 0 1 } , S _ { 1 0 } = \mathcal { O } ( \delta ^ { - 1 } ) , \quad \dot { L } _ { 1 1 } , \dot { S } _ { 0 1 } , \dot { S } _ { 1 0 } = \mathcal { O } ( \delta ^ { - 2 } ) , } \end{array}
$$

and hence also

$$
W = { \mathcal O } ( \delta ^ { - 1 } ) , \quad \dot { W } = { \mathcal O } ( \delta ^ { - 2 } ) .
$$

So we have from theenergy boundandthediferentialequation(2.23)for $\eta$

$$
\eta = \mathcal { O } ( 1 ) , \quad \dot { \eta } = \mathcal { O } ( \delta ^ { - 1 } ) .
$$

From thedifferential equations(2.21） for $p _ { 0 } , q _ { 0 }$ we conclude

$$
\ddot { p } _ { 0 } = \mathcal { O } ( \delta ^ { - 1 } ) + \mathcal { O } ( \varepsilon \delta ^ { - 2 } ) , \ddot { q } _ { 0 } = \mathcal { O } ( \varepsilon \delta ^ { - 1 } ) .
$$

(b)To study the local error in $\eta$ ,weintegrate（2.23）from $t _ { 0 }$ to $t _ { 0 } { + } h$ and compare with the corresponding term in(2.31）:

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + h } P _ { 1 } ^ { * } ( t ) \Big ( \bar { L } _ { 1 0 } p _ { 0 } + ( \bar { S } _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) q _ { 0 } \Big ) ( t ) d t } \\ & { \displaystyle - h \mathcal { P } _ { 1 } ^ { * } \Big ( \bar { L } _ { 1 0 } ( t _ { 1 / 2 } ) p _ { 0 } ^ { 1 / 2 } \neq ( S _ { 1 0 } + T _ { 1 } ^ { T } G T _ { 0 } ) ( t _ { 1 / 2 } ) q _ { 0 } ^ { 1 / 2 } \Big ) } \\ & { \displaystyle = \mathcal { O } ( h ^ { 2 } / \delta ^ { 2 } ) , } \end{array}
$$

where we have used the above bounds and the error estimate for the linear phase approximationin the average of $P _ { 1 } ( t )$ ,cf.Sect. XIV.1.2,

$$
\mathcal { P } _ { 1 } - \frac { 1 } { h } \int _ { t _ { 0 } } ^ { t _ { 1 } } P _ { 1 } ( t ) d t = \mathcal { O } ( h / \delta ) .
$$

Combining this estimatewith the error bound of the adiabatic midpoint rule for the homogeneous equation as given in Theorem1.2 yields thestated error bound for $\eta _ { \mathrm { 1 } }$

(c）The error bound for the components $p _ { 0 } , q _ { 0 }$ comes about by combining error bounds for the Stormer-Verlet method(which require the bounds for ${ \ddot { p } } _ { 0 } , { \ddot { q } } _ { 0 } )$ and the estimates

$$
\begin{array} { l } { \displaystyle \int _ { t _ { 0 } } ^ { t _ { 0 } + h / 2 } \varepsilon ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } ) Q _ { 1 } \eta ( t ) d t - \frac { h } { 2 } \varepsilon \big ( S _ { 0 1 } + T _ { 0 } ^ { T } G T _ { 1 } \big ) ( t _ { 1 / 2 } ) Q _ { 1 } ^ { - } \eta ^ { 0 } } \\ { = \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ^ { 2 } ) } \end{array}
$$

and

$$
\int _ { t _ { 0 } } ^ { t _ { 0 } + h / 2 } \varepsilon L _ { 1 0 } ^ { T } Q _ { 1 } \eta ( t ) d t - \frac { h } { 2 } \varepsilon L _ { 1 0 } ( t _ { 1 / 2 } ) \mathcal { Q } _ { 1 } ^ { - } \eta ^ { 0 } = \mathcal { O } ( \varepsilon h ^ { 2 } / \delta ) ,
$$

and the same estimates for the second half-step.See also Exercise7 fora similar situation.

In the case of well-separated eigenvalues,the global error on bounded time intervals is thus bounded by $\mathcal { O } ( h ^ { 2 } ) + \mathcal { O } ( h \varepsilon )$ in $\psi _ { 0 } , q _ { 0 }$ for $t \leq$ Const.and by $\mathcal { O } ( h )$ in $\eta$ Inthe original variables $p , q$ of(2.1）,this thenyieldsan error

$$
q _ { n } - q ( t _ { n } ) = { \mathcal O } ( h ^ { 2 } ) + { \mathcal O } ( h \varepsilon ) , \quad p _ { n } - p ( t _ { n } ) = { \mathcal O } ( h ) \quad \mathrm { ~ f o r ~ } t _ { n } \le \mathrm { C o n s t . }
$$

Withanadaptive step size strategyasin Sect.XIV.1.2,itisagain possible to follow $\eta$ through non-adiabatic transitions nearavoided crossings of eigenvalues.

Ahigher-order scheme with a global errorof $\mathcal { O } ( h ^ { 2 } )$ in $\eta -$ in the situation ofseparated eigenvalues-isobtained byreplacingtheupper line in(2.31）bya second-orderadiabatic integratoras discussed in Sect.XIV.1.2,leaving the last term in(2.31） unaltered.In the original variables $p , q$ of(2.1）,theerror is then $\mathcal { O } ( h ^ { 2 } )$ bothin positionsand(fast and slow)momenta.The error is even $\mathcal { O } ( \varepsilon h ^ { 2 } )$ in thefast positions $q _ { \perp }$ of(2.8）,which oscillate with an amplitude $\mathcal { O } ( \varepsilon )$ Werefer to Lorenz, Jahnke&Lubich (2oo5) for theparticular case of second-order differential equations $\ddot { q } + \varepsilon ^ { - 2 } A ( t ) q = 0$ withapositive definite matrix $\boldsymbol A ( t )$ ,

# XIV.2.3 Error Analysis of the Impulse Method

Thetransformation to adiabatic variables of Sect.XIV.2.1 also gives new insight into the error behaviour of multiple time stepping methods such as the impulse or mollified impulse method discussed in SectionsVIII.4 and XIII.1,which do not usecoordinate transforms inthemethod formulation.These methodsare of interest when the eigendecompositions needed inadiabatic integrators are computationally more expensive than doing many small stepswith the fast subsystem,and when evaluations of thepotential force are so costly that the computational work for the fast subsystem becomes irrelevant.We consider the splitting

$$
H = H ^ { \mathrm { f a s t } } + H ^ { \mathrm { s l o w } }
$$

of the Hamiltonian (2.3)with

$$
\begin{array} { r c l } { { H ^ { \mathrm { f a s t } } ( p , E , q , t ) } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } p ^ { T } M ( t ) ^ { - 1 } p + \frac { 1 } { 2 \varepsilon ^ { 2 } } q ^ { T } A ( t ) q + { \bar { E } } } } \\ { { } } & { { } } & { { } } \\ { { H ^ { \mathrm { s l o w } } ( p , E , q , t ) } } & { { = } } & { { \displaystyle U ( q , t ) . } } \end{array}
$$

The impulse method is given as the composition of the exact flows of the subsystems (see SectionsVIII.4 and XIII.1.3):

$$
\varPhi _ { h } = \varphi _ { h / 2 } ^ { \mathrm { s l o w } } \circ \varphi _ { h } ^ { \mathrm { f a s t } } \circ \varphi _ { h / 2 } ^ { \mathrm { s l o w } } ,
$$

whereweare interested intaking long time steps $h \geq c \varepsilon$ (with a positive constant c). The equations of motion of the slow subsystem,

$$
\dot { p } = - \nabla U ( q , t ) , \quad \dot { q } = 0 , \quad \dot { t } = 0 ,
$$

are solved trivially by

$$
\widehat { \boldsymbol { p } } = \boldsymbol { p } - \frac { h } { 2 } \nabla U ( \boldsymbol { q } , t ) , \quad \widehat { \boldsymbol { q } } = \boldsymbol { q } , \quad \widehat { t } = t .
$$

Incontrast,the fastsubsystem needsto be integrated approximately,e.g.,bymany small substepswith the Stormer-Verlet methodin the originalvariables $( p , q )$ orby one step of themethod(2.30)-(2.32)with $G = 0$ inadiabatic variables $( p _ { 0 } , q _ { 0 } , \eta )$ Inthe following we ignore the error resulting from this additional approximation and study the splitting method with exact flows.

Theerror behaviour of this method can be understood with the help of the transformation toadiabatic variablesof Sect.XIV.2.1.The impulsemethod in theadiabaticvariables $p 0 , q _ { 0 } , \eta$ is obtained by splitting the differential equations(2.21)and (2.23).The fast subsystemisobtained by simply putting $U = 0$ in these equations, and the slow subsystemreads

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { - T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) , \quad \dot { q } _ { 0 } = 0 } \\ { \dot { \eta } } & { = } & { - P _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t ) } \end{array}
$$

alongwith $\dot { t } = 0$ ,sothat theargument inall thematrices is frozenat the initial time. Here $P _ { 1 } ( t )$ and $Q _ { 1 } ( t )$ areagain the highly oscillatory matrix functions of(2.20). Since $Q _ { 1 } P _ { 1 } ^ { * } = 0$ wehave $Q _ { 1 } \eta = \mathrm { C o n s t }$ ,and therefore,inthesevariablestheflow $\varphi _ { h / 2 } ^ { \mathrm { s l o w } }$ is he mapping given by

$$
\begin{array} { r c l } { { \widehat { p } _ { 0 } } } & { { = } } & { { p _ { 0 } - \displaystyle \frac { h } { 2 } T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t _ { 0 } ) , \widehat { q } _ { 0 } = q _ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { \widehat { \eta } } } & { { = } } & { { \eta - \displaystyle \frac { h } { 2 } P _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } Q _ { 1 } \eta , t _ { 0 } ) , } } \end{array}
$$

where the matrices ， , , areevaluated at .In the impulse method, the anotherapplicatiho abovvalueeufoeit $\varphi _ { h / 2 } ^ { \mathrm { s l o w } }$ $\varphi _ { h } ^ { \mathrm { t a s t } }$ which isfllowed by

Adisturbing feature in(2.33) is the appearance of theparticular value $P _ { 1 } ( t _ { 0 } )$ of thehighly oscillatory function instead of theaverage $\mathcal { P } _ { 1 }$ as in (2.31).

Wenow consider the error propagation for $\eta$ in the case of well-separated frequencies.Recall that the exact solution then satisfies $\eta ( t ) ~ = ~ \eta ( 0 ) + \mathcal { O } ( \varepsilon )$ for $t \leq$ Const.For ease of presentation we consider a constant step size $h$ ,

Lemma2.3.Assumetheenergybound(2.2)fortheinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remainseparated fromeach other,then the result after $^ { u }$ steps satisfies,for $n h \leq T \leq C o n s t .$ ，

$$
\eta _ { n } = \eta _ { 0 } + \sigma _ { n } + \mathcal { O } ( \varepsilon ) ,
$$

where

$$
\| \sigma _ { n } \| \leq C \kappa \quad w i t h \quad \kappa = \operatorname* { m a x } _ { 0 \leq n h \leq T } \operatorname* { m a x } _ { k } \Big \| h \sum _ { j = 0 } ^ { n } \mathrm { e x p } \Big ( \frac { i } { \varepsilon } \phi _ { k } ( t _ { j } ) \Big ) \Big \| .
$$

Proof.We have $\eta _ { n } ~ = ~ \eta _ { h } ( t _ { n } )$ ,where $\eta _ { h } ( t )$ solves the differential equation with impulses,

$$
\dot { \eta } _ { h } = \exp \left( - \frac { i } { \varepsilon } \varPhi \right) W \exp \left( \frac { i } { \varepsilon } \varPhi \right) \eta _ { h } + r + \sum _ { j } \varDelta \eta _ { j } \delta _ { j } .
$$

Here $W ( t )$ is the matrix (2.22)appearing in (2.23),and

$$
\begin{array} { r } { r ( t ) = - P _ { 1 } ^ { * } ( t ) \big ( L _ { 1 0 } ( t ) p _ { 0 , h } ( t ) + S _ { 0 1 } ( t ) q _ { 0 , h } ( t ) \big ) } \end{array}
$$

with $p _ { 0 , h } ( t )$ , $q _ { 0 , h } ( t )$ denoting the piecewise constant functions that take the values ofthe numerical solution.Furtherwe have

$$
\varDelta \eta _ { j } = - h P _ { 1 } ( t _ { j } ) ^ { \ast } T _ { 1 } ( t _ { j } ) ^ { T } \nabla U \big ( T _ { 0 } ( t _ { j } ) q _ { 0 , j } + \varepsilon T _ { 1 } ( t _ { j } ) Q _ { 1 } ( t _ { j } ) \eta _ { j } , t _ { j } \big ) ,
$$

the expression on the right-hand side of (2.33).and $\delta _ { j }$ isaDirac impulse located at $t _ { j } .$ It follows that,for $t = n h$ ,

$$
\begin{array} { r l l } { \mathrm { \Pi } _ { \mathfrak { i } } - \eta _ { 0 } } & { = } & { \eta _ { h } ( t _ { n } ) - \eta _ { h } ( 0 ) } \\ & { = } & { \displaystyle \int _ { 0 } ^ { t } \exp \left( - \frac { \dot { \iota } } { \varepsilon } \varPhi ( s ) \right) W ( s ) ^ { - } \exp \left( \frac { \dot { \iota } } { \varepsilon } \varPhi ( s ) \right) \eta _ { h } ( s ) d s + \int _ { 0 } ^ { t } r ( s ) d s + \sigma } \end{array}
$$

where $\sigma _ { n }$ is the trapezoidal sum of the terms on the right-hand side of (2.33):

$$
\sigma _ { n } = - h \sum _ { j = 0 } ^ { n } { { ^ { \prime } P _ { 1 } } ( t _ { j } ) ^ { * } T _ { 1 } } ( t _ { j } ) ^ { T } \nabla U \big ( T _ { 0 } ( t _ { j } ) q _ { 0 , j } + \varepsilon T _ { 1 } ( t _ { j } ) Q _ { 1 } ( t _ { j } ) \eta _ { j } , t _ { j } \big ) .
$$

Theprimeonthesumindicatesthatthefirstandlasttermare takenwiththefactor $\textstyle { \frac { 1 } { 2 } }$ . Usingpartial integrationas in（1.6）,we obtain

$$
\int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) W ( s ) \exp \Bigl ( \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) \eta _ { h } ( s ) d s = \mathcal { O } ( \varepsilon ) ,
$$

and by partial integration as in (2.25),

$$
\int _ { 0 } ^ { t } r ( s ) d s = { \mathcal { O } } ( \varepsilon ) .
$$

This shows (2.34).A partial summation in (2.36),summingup the oscillatory terms $P _ { 1 } ( t _ { j } )$ and differencing the smoother other terms,then yields(2.35). □

The size of $\boldsymbol { \kappa }$ of(2.35)depends on possible resonances between the step size and thefrequencies,yielding $\boldsymbol { \kappa }$ between $\mathcal { O } ( h )$ and ${ \mathcal { O } } ( 1 ) .$ For the error of the method we have the following.

Theorem2.4.Assume theenergy bound(2.2)fortheinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remainseparatedfromeachother,thentheerroroftheimpulsemethod aftern steps with step size $h \geq c \varepsilon$ satisfies

$$
\begin{array} { r c l } { { p _ { n } - p ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( \kappa ) } } \\ { { q _ { n } - q ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ^ { 2 } ) + { \mathcal { O } } ( \varepsilon \kappa ) . } } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ do not depend on $\boldsymbol { \varepsilon }$ , $h$ andnwith $n h \le \mathrm { C o n s t }$

Proof The error of size $\mathcal { O } ( \kappa )$ in $\eta$ immediately implies an error of size $\mathcal O ( \kappa )$ in the actions $\begin{array} { r } { I _ { j } = \frac { 1 } { 2 } | \eta _ { j } | ^ { 2 } } \end{array}$ ,andan error of ${ \mathcal { O } } ( \kappa )$ in the fast momenta $p _ { 1 }$ andof $\mathcal { O } ( \varepsilon \kappa )$ in the fast positions $q _ { 1 }$ of(2.9);recall the transformation (2.16)and the rescaling.In the slow components $p _ { 0 } , q _ { 0 }$ themethod isaperturbed variantof the Stormer-Verlet method.The contribution of the perturbations $\varepsilon T _ { 1 } Q _ { 1 } \eta$ to the error is of size $\mathcal { O } ( \varepsilon \kappa )$ Thisis seen byapplying the simple lemma belowwith $y = ( p _ { 0 } , q _ { 0 } )$ and

$$
d _ { n } = \left( { - h T _ { 0 } ( t _ { n } ) ^ { T } \nabla ^ { 2 } U ( T _ { 0 } ( t _ { n } ) q _ { 0 , n } , t _ { n } ) \varepsilon T _ { 1 } ( t _ { n } ) Q _ { 1 } ( t _ { n } ) \eta _ { n } } \right) + \mathcal { O } ( h ^ { 2 } \varepsilon )
$$

and using partial summation of the $d _ { n }$ ,summing up the oscillatory terms $Q _ { 1 } ( t _ { n } )$ and differencingthe other terms. □

Lemma 2.5.Let $\bar { \varPhi } _ { h } ( y ) = y + h F _ { h } ( y )$ bea one-step method where $F _ { h }$ hasLipschitz constant $L$ .Considerthemethodandaperturbation,

$$
y _ { n + 1 } = \varPhi _ { h } ( y _ { n } ) \qquad a n d \qquad \widetilde { y } _ { n + 1 } = \varPhi _ { h } ( \widetilde { y } _ { n } ) + d _ { n } ,
$$

withthesame starting values $y _ { 0 } = y _ { 0 }$ .Then,thedifferenceisboundedby

$$
\left\| \widetilde { y } _ { n } - y _ { n } \right\| \leq e ^ { n h L } , \operatorname* { m a x } _ { 0 \leq k \leq n - 1 } \left\| \sum _ { j = 0 } ^ { k } d _ { j } \right\| .
$$

ProofThe result follows from

$$
\widetilde { y } _ { n } - y _ { n } = h \sum _ { j = 0 } ^ { n - 1 } \bigl ( F _ { h } ( \widetilde { y } _ { n } ) - F _ { h } ( y _ { n } ) \bigr ) + \sum _ { j = 0 } ^ { n - 1 } d _ { j }
$$

with the discrete Gronwall inequality.

# XIV.2.4 ErrorAnalysis of the Mollified ImpulseMethod

The problem with possible step-size resonances can be greatly alleviated by the mollified impulse method (see Sect.XII.1.4) where the potential $U ( q , t )$ isreplaced bya modified potential ${ \overline { { U } } } ( q , t ) .$ A good choice is

$$
\overline { { U } } ( \boldsymbol { q } , t ) = U ( \boldsymbol { A } ( t ) \boldsymbol { q } , t ) \quad \mathrm { ~ w i t h ~ } \ \boldsymbol { A } ( t ) = C ( t ) Q ( t ) \left( \begin{array} { c c } { I } & { 0 } \\ { 0 } & { S ( t ) } \end{array} \right) Q ( t ) ^ { T } C ( t ) ^ { - 1 }
$$

with $C$ and $Q$ of(2.4) and (2.6），and

$$
{ \mathcal { S } } ( t ) = \mathrm { s i n c } \left( { \frac { h } { \varepsilon } } { \mathcal { \Omega } } ( t ) \right) = { \frac { 1 } { 2 h } } \int _ { - h } ^ { h } \mathrm { e x p } \left( \pm { \frac { i s } { \varepsilon } } { \mathcal { \Omega } } ( t ) \right) d s .
$$

Acalculation shows that itreplaces (2.33)by

$$
\begin{array} { r c l } { { \widehat { p } _ { 0 } } } & { { = } } & { { p _ { 0 } - \displaystyle \frac { h } { 2 } T _ { 0 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } \mathcal { Q } _ { 1 } \eta , t _ { 0 } ) , \quad \widehat { q } _ { 0 } = q _ { 0 } } } \\ { { } } & { { } } & { { } } \\ { { \widehat { \eta } } } & { { = } } & { { \eta - \displaystyle \frac { h } { 2 } \mathcal { P } _ { 1 } ^ { * } T _ { 1 } ^ { T } \nabla U ( T _ { 0 } q _ { 0 } + \varepsilon T _ { 1 } \mathcal { Q } _ { 1 } \eta , t _ { 0 } ) , } } \end{array}
$$

withmatrix functions evaluated at $t _ { 0 }$ ,where $\mathcal { P } _ { 1 } ( t )$ and $\mathcal { Q } _ { 1 } ( t )$ are the linear-phase approximationsto theaverage over the interval $\lfloor t - h , t + h \rfloor$ of $P _ { 1 }$ and $Q _ { 1 }$ ,respectively,

$$
\begin{array} { l } { \displaystyle \mathcal { P } _ { 1 } ( t ) = \mathcal { S } ( t ) P _ { 1 } ( t ) = \frac { 1 } { 2 h } \int _ { t - h } ^ { t + h } P _ { 1 } ( s ) d s + \mathcal { O } ( h ) } \\ { \displaystyle \mathcal { Q } _ { 1 } ( t ) = \mathcal { S } ( t ) Q _ { 1 } ( t ) = \frac { 1 } { 2 h } \int _ { t - h } ^ { t + h } Q _ { 1 } ( s ) d s + \mathcal { O } ( h ) . } \end{array}
$$

Therefore,(2.34) and(2.36) hold with the highly oscillatory $P _ { 1 } ( t _ { j } )$ replaced by the averages $\mathcal { P } _ { 1 } ( t _ { j } )$ Usingapartial summation in(2.36)and noting that,for $t = n h \leq$ Const.,

$$
\left\| h \sum _ { j = 1 } ^ { n } \mathcal { P } _ { 1 } ( t _ { j } ) \right\| = \left\| \int _ { 0 } ^ { t } P _ { 1 } ( s ) d s \right\| + \mathcal { O } ( h ) = \mathcal { O } ( \varepsilon ) + \mathcal { O } ( h ) ,
$$

we obtain an estimate

$$
\eta _ { n } = \eta _ { 0 } + O ( h )
$$

instead of the corresponding bound(2.34）with(2.35).This eliminates the bad effect of step size resonances (large $\boldsymbol { \kappa }$ ）onthe propagationin the fastvariables over bounded time intervals $t \leq$ Const.(though not on longer intervals,as we know from Chap.XIII).The more harmless effect of step size resonances on the slow variables, as visible in the term $\mathcal { O } ( \varepsilon \kappa )$ in Theorem 2.4,is likewise reduced to $\mathcal { O } ( \varepsilon h )$ Wethus obtain the following improvement over the error bounds in Theorem 2.4.

Theorem2.6.Assumetheenergybound(2.2)for theinitialvalues.Ifthefrequencies $\omega _ { j } ( t )$ remain separatedfromeachother,thentheerror of theabovemollified impulsemethodafter $n$ stepswith step size $h \geq c \varepsilon$ satisfies

$$
\begin{array} { r c l } { { p _ { n } - p ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ) } } \\ { { q _ { n } - q ( t _ { n } ) } } & { { = } } & { { { \mathcal { O } } ( h ^ { 2 } ) . } } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ do notdepend on $\boldsymbol { \varepsilon }$ ， $h$ andnwith $n h \leq \mathrm { C o n s t }$

Adirect implementation of thismethod requires just the same matrix decompositions that are needed for the integrators inadiabatic variables.Itis thenreasonable touseone step of the adiabatic integrator of Sect.XIV.2.2 for solvingthe fast subsystem overa timestep.

Analternative is tocompute the average $\boldsymbol { A } ( t )$ by smalltime steps from thelinear differential equation with the Hamiltonian $H ^ { \mathrm { f a s t } }$ ,asformulated in Sect.XIII.1.4. The method described here thencorresponds to (XIII.1.18)with $c = 1$

# XIV.3Mechanical Systems with Solution-Dependent Frequencies

We²consider the Hamiltonian

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q ) + { \frac { 1 } { \varepsilon ^ { 2 } } } V ( q )
$$

with a strong potential ${ \mathcal { E } } ^ { - 2 } V ( q )$ that penalizes some directions of motion.Analytical studiesof thisproblemweredonebyRubin&Ungar（1957),Takens(1980),and Bornemann(1998).Inanalternative approach to theseworks,we here describea transformation of the problem toadiabatic variables.This gives new insight into the solution behaviour and can be used as the starting point for the construction of longtime-step integrators.Italso enables us to analyse the error of multiple time-stepping methods.

# XIV.3.1 Constraining Potentials

Weconsider the Hamiltonian(3.1）,where $M ( q )$ isasymmetric positive definite mass matrix depending smoothly on the positions $q \in \mathbb { R } ^ { n }$ , $U$ isasmooth potential, and theconstraining potential is assumed to satisfy the following:

The smooth function $V : D \subset \mathbb { R } ^ { n } \longrightarrow \mathbb { R }$ attainsits minimumvalueOona $d$ -dimensional manifold $\nu \subset \mathbb { R } ^ { n }$ ,

$$
\mathcal V = \{ q \in D \mid V ( q ) = \operatorname* { m i n } V = 0 \} .
$$

Ina neighourhood of $\nu$ ,thepotential $V$ isstrongly convex along directions nontangential to $\nu$ ,that is,there exists $\alpha > 0$ such that for $q \in \mathcal V$ ,theHessian $\nabla ^ { 2 } V ( q )$ satisfies

$$
v ^ { T } \nabla ^ { 2 } V ( q ) v \geq \alpha \cdot v ^ { T } M ( q ) v
$$

![](images/543b6ef1f7c18d3b28cfd6fcc86fab3bba0c8ae7c615bd41dfc3ef84ff2cb5e3.jpg)

for all vectors $\boldsymbol { v }$ in the $M ( q )$ -orthogonalcomplementof thetangent space $T _ { q } \nu$

Welet $m = n - d$ be the number of independent constraints that locally describe themanifold $\nu$ .

Example 3.1 (Chain of Stiff Springs).The position of $m + 1$ mass points in a plane,arranged in a chain connected by stiff springs with spring constants $\alpha _ { i } ^ { 2 } / \varepsilon ^ { 2 }$ ,is determined by the Cartesiancoordinates of the first mass point and by m anglesi and the elongations $d _ { i }$ ofthe $\boldsymbol { n }$ springs.The constraining potential is

$$
V = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } \alpha _ { i } ^ { 2 } d _ { i } ^ { 2 } ,
$$

and the constraint manifold is described by $d _ { 1 } = \dots = d _ { m } = 0$ corresponding to non-elongated springs.The frequencies of the vibrationsin such achain depend on theangles.

In the above example we have,in the coordinates givenby the anglesand elongations,apotential $V$ of theform

$$
V ( q ) = \frac { 1 } { 2 } q _ { 1 } ^ { T } A ( q _ { 0 } ) q _ { 1 }
$$

for $q = ( q _ { 0 } , q _ { 1 } ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,with a positive definite matrix $A ( q _ { 0 } )$ .The manifold of constraints is here simply $\mathcal { V } = \mathbb { R } ^ { d } \times 0$ Asthe following lemma shows,thisis already the general situation in suitable local coordinates.

Lemma3.2.Underconditions(3.2)-(3.3),thereexistsasmoothlocal changeof coordinates $q = \chi ( y )$ suchthat

$$
V ( q ) = \frac { 1 } { 2 } y _ { 1 } ^ { T } A ( y _ { 0 } ) y _ { 1 } ~ j o r ~ q = \chi ( y )
$$

with $\boldsymbol { y } = \left( y _ { 0 } , y _ { 1 } \right)$ near $_ 0$ in $\mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,where $A ( y _ { 0 } )$ is $a$ symmetricpositivedefinite $m \times m$ matrix.

Proof.Ina first step,we choose local coordinates $q = \psi ( x )$ with $\boldsymbol { x } = \left( \boldsymbol { x } _ { 0 } , \boldsymbol { x } _ { 1 } \right)$ near $_ 0$ in $\mathbb { R } ^ { d } \times \mathbb { R } ^ { m }$ ,such that $q = \psi ( x ) \in \mathcal { V }$ ifand only if $x _ { 1 } = 0 .$ In these coordinates, denoting ${ \hat { V } } ( x ) = V ( q )$ for $q = \psi ( x )$ ,we then have

$$
\widehat { V } ( x _ { 0 } , 0 ) = 0 , \quad \nabla \widehat { V } ( x _ { 0 } , 0 ) = 0
$$

by(3.2）,and

$$
A ( x _ { 0 } ) : = \nabla _ { x _ { 1 } } ^ { 2 } \widehat { V } ( x _ { 0 } , 0 ) \quad \mathrm { i s ~ p o s i t i v e ~ d e f n i t e }
$$

by(3.3).We now change coordinates by the near-identity transformation

$$
y _ { 0 } = x _ { 0 } , \quad y _ { 1 } = \mu ( x ) x _ { 1 }
$$

where thereal factor $\mu ( x )$ (near1for $x _ { 1 }$ near $0$ is to be chosen such that

$$
\frac 1 2 y _ { 1 } ^ { T } A ( y _ { 0 } ) y _ { 1 } = \widehat { V } ( x _ { 0 } , x _ { 1 } ) .
$$

Since the right-hand side equals

$$
\widehat { V } ( x _ { 0 } , x _ { 1 } ) - \widehat { V } ( x _ { 0 } , 0 ) - x _ { 1 } ^ { T } \nabla \widehat { V } ( x _ { 0 } , 0 ) = \frac { 1 } { 2 } x _ { 1 } ^ { T } A ( x _ { 0 } ) x _ { 1 } + r ( x )
$$

with $r ( x ) = \mathcal { O } ( \| x _ { 1 } \| ^ { 3 } )$ ,the choice

$$
\mu ( x ) = \sqrt { 1 + \frac { 2 r ( x ) } { x _ { 1 } ^ { T } A ( x _ { 0 } ) x _ { 1 } } }
$$

does the trick.

Weremark thatLemma3.2couldbeobtainedasacorollary to theMorse lemma, forwhichwerefer to Abraham&Marsden（1978)and Crouzeix&Rappaz(1989).

The change to the local coordinates $\boldsymbol { x } = \left( \boldsymbol { x } _ { 0 } , \boldsymbol { x } _ { 1 } \right)$ such that $V ( q ) = 0$ if and only if $x _ { 1 } = 0$ for $q = \psi ( x )$ isnot numerically constructive from the mere knowledge ofanexpression for the potential $V _ { \ast }$ However,in many situations the manifold $\nu$ can be described by constraints $g ( q ) = 0$ ,and $x _ { \mathrm { 1 } } = g$ can then be extended toa full setofcoordinates.The above transformation from $x$ to $y$ canbe done numerically. In theusual way,the transformation $q = \chi ( y )$ of the position coordinates extends to acanonical transformation by setting $p _ { y } = \chi ^ { \prime } ( y ) ^ { T } p$ for the conjugate momenta; seeExample VI.5.2.

Solutions of(3.1） arein general oscillatorywith frequencies of siz $c \sim \varepsilon ^ { - 1 }$ Thereexist,however,special solutions having arbitrarily many time derivatives bounded independently of $\succeq$ ,which forarbitrary $N \geq 1$ stay $\mathcal { O } ( \varepsilon ^ { N } )$ close toa manifold $\mathcal { V } ^ { \varepsilon , N }$ that has a distance $\mathcal { O } ( \varepsilon )$ to $V$ SeeLubich(1993),where also implicit Runge-Kutta methods for the approximation of the smooth solutions are studied.In thissectionwe are,however,interested in approximating general oscillatory solutions of bounded energy.

# XIV.3.2 Transformationto Adiabatic Variables

We start froma Hamiltonian (3.1) incoordinates $( p , q )$ where the constraining potential isalreadyof theform(3.4)for $q = ( q _ { 0 } , q _ { 1 } )$ Wenote that forasystem of bounded energy,we then have $q _ { 1 } = { \mathcal { O } } ( \varepsilon )$

Wenowperformaseries of canonical transformations that take the Hamiltonian intoaform that is better suited fora direct numerical treatmentand for theerroranalysis of multiple time-stepping methods.The transformations are similar to those for the time-dependent case treated in Sect.XIV.2.1,but here theyappear ina permuted order.

Transforming the Stiffness Matrix into the Identity.We write the Cholesky decomposition of the stiffness matrix as

$$
A ( q _ { 0 } ) = C ( q _ { 0 } ) ^ { - T } C ( q _ { 0 } ) ^ { - 1 }
$$

and change to variables

$$
q _ { 0 } = \widetilde { q } _ { 0 } , q _ { 1 } = C ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 }
$$

along with the conjugate momenta

$$
\widetilde { p } _ { 0 } = p _ { 0 } + \Big ( \frac { \partial } { \partial \widetilde { q } _ { 0 } } C ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 } \Big ) ^ { T } p _ { 1 } , \quad \widetilde { p } _ { 1 } = C ( \widetilde { q } _ { 0 } ) ^ { T } p _ { 1 } .
$$

With the transformed mass matrix $\boldsymbol { \bar { M } } ( \boldsymbol { \tilde { q } } ) = \boldsymbol { B } ( \boldsymbol { \tilde { q } } ) \boldsymbol { M } ( \boldsymbol { \tilde { q } _ { 0 } } , \boldsymbol { C } ( \boldsymbol { \tilde { q } _ { 0 } } ) \boldsymbol { \tilde { q } _ { 1 } } ) \boldsymbol { B } ( \boldsymbol { \tilde { q } } ) ^ { T }$ (for the matrix $B ( { \widehat { q } } )$ that transforms $\widetilde { p } = B ( \widetilde { q } ) p )$ and the potential $\begin{array} { r } { \boldsymbol { U } ( \widetilde { \boldsymbol { q } } ) = \boldsymbol { U } ( \widetilde { q } _ { 0 } , \boldsymbol { C } ( \widetilde { q } _ { 0 } ) \widetilde { q } _ { 1 } ) } \end{array}$ , theHamiltonian takes the simplified form (we omit alltildes)

$$
H = \frac { 1 } { 2 } { p } ^ { T } M ( q ) ^ { - 1 } p + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } q _ { 1 } ^ { T } q _ { 1 } + U ( q ) .
$$

Eliminating Off-Diagonal Blocks in the Mass Matrix. We write the mass matrix $M ( q )$ as

$$
M = \left( \begin{array} { c c } { { M _ { 0 0 } } } & { { M _ { 0 1 } } } \\ { { M _ { 1 0 } } } & { { M _ { 1 1 } } } \end{array} \right) .
$$

With $G ( \overline { { { q } } } _ { 0 } ) = - M _ { 0 0 } ( \overline { { { q } } } _ { 0 } , 0 ) ^ { - 1 } M _ { 0 1 } ( \overline { { { q } } } _ { 0 } , 0 )$ ,we transform

$$
q _ { 0 } = \overline { { { q } } } _ { 0 } + G ( \overline { { { q } } } _ { 0 } ) \overline { { { q } } } _ { 1 } , \quad q _ { 1 } = \overline { { { q } } } _ { 1 } ,
$$

with the conjugate momenta

$$
\overline { { p } } _ { 0 } = p _ { 0 } + \bigg ( \frac { \partial } { \partial \overline { { q } } _ { 0 } } G ( \overline { { q } } _ { 0 } ) \overline { { q } } _ { 1 } \bigg ) ^ { T } p _ { 0 } , \quad \overline { { p } } _ { 1 } = p _ { 1 } + G ( \overline { { q } } _ { 0 } ) ^ { T } p _ { 0 } .
$$

Thiscanonical change ofvariables eliminates $M _ { 0 1 }$ and $M _ { 1 0 }$ in the transformed mass matrix $\boldsymbol { M } ( \boldsymbol { q } _ { 0 } , 0 )$ and keeps the Schur complement on the block diagonal:with the symmetric positive definite matrices

$$
\overline { { { M } } } _ { 0 } ( \overline { { { q } } } _ { 0 } ) = M _ { 0 0 } ( \overline { { { q } } } _ { 0 } , 0 ) , \quad \overline { { { M } } } _ { 1 } ( \overline { { { q } } } _ { 0 } ) = \left( M _ { 1 1 } - M _ { 1 0 } M _ { 0 0 } ^ { - 1 } M _ { 0 1 } \right) ( \overline { { { q } } } _ { 0 } , 0 ) ,
$$

thetransformation puts the Hamiltonian into theform(we omit all bars)

$$
\begin{array} { r c l } { { \cal H } } & { { \equiv } } & { { \displaystyle { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + \frac { 1 } { 2 } p _ { 1 } ^ { T } M _ { 1 } ( q _ { 0 } ) ^ { - 1 } p _ { 1 } + \frac { 1 } { 2 \varepsilon ^ { 2 } } q _ { 1 } ^ { T } q _ { 1 } } } \\ { { } } & { { } } & { { \displaystyle { + \frac { 1 } { 2 } p ^ { T } R ( q ) p + U ( q _ { 0 } + G ( q _ { 0 } ) q _ { 1 } , q _ { 1 } ) } } } \end{array}
$$

where $R$ is asmooth matrix-valued function satisfying

$$
R ( q _ { 0 } , 0 ) = 0 .
$$

Diagonalizing theMassMatrix oftheFast Variables.Wediagonalize

$$
M _ { 1 } ( q _ { 0 } ) = Q ( q _ { 0 } ) \Omega ( q _ { 0 } ) ^ { - 2 } Q ( q _ { 0 } ) ^ { T }
$$

with the diagonal matrix $\varOmega ( q _ { 0 } ) = \mathrm { d i a g } ( \omega _ { j } ( q _ { 0 } ) )$ of frequencies and an orthogonal matrix $Q ( q _ { 0 } )$ ,which depends smoothly on $q _ { 0 }$ if the frequenciesare separated.We transform

$$
q _ { 0 } = \widehat { q } _ { 0 } , q _ { 1 } = Q ( \widehat { q } _ { 0 } ) \widehat { q } _ { 1 }
$$

with the conjugate momenta

$$
\widehat { p } _ { 0 } = p _ { 0 } + \bigg ( \frac { \partial } { \partial \widehat { q } _ { 0 } } Q ( \widehat { q } _ { 0 } ) \widehat { q } _ { 1 } \bigg ) ^ { T } p _ { 1 } , \quad \widehat { p } _ { 1 } = Q ( \widehat { q } _ { 0 } ) ^ { T } p _ { 1 } .
$$

Thematrix

$$
\boldsymbol { Y } ( \boldsymbol { \widehat { q } } ) = \Big ( \frac { \partial } { \partial \widehat { q _ { 0 } } } \boldsymbol { Q } ( \widehat { q _ { 0 } } ) \boldsymbol { \widehat { q } } _ { 1 } \Big ) ^ { T } \boldsymbol { Q } ( \widehat { q _ { 0 } } )
$$

is of size $\mathcal { O } ( \widehat { q } _ { 1 } )$ butitis this expression which may become large near avoided crossings of eigenvalues.We consider the associated matrix

$$
\begin{array} { r } { X ( \widehat { q } ) = \left( \begin{array} { c c } { 0 } & { X _ { 0 1 } } \\ { X _ { 1 0 } } & { X _ { 1 1 } } \end{array} \right) = \left( \begin{array} { c c } { 0 } & { - M _ { 0 } ^ { - 1 } Y } \\ { - Y ^ { T } M _ { 0 } ^ { - 1 } } & { Y ^ { T } M _ { 0 } ^ { - 1 } Y } \end{array} \right) . } \end{array}
$$

With amatrix $\widehat { R } ( \widehat { q } )$ satisfying(3.7),which isasumof the appropriately transformed previous matrix $R$ and the above matrix $X$ ,theHamiltonianin the newvariables $( \widehat { p } , \widehat { q } )$ becomes (we omit all hats）

$$
\begin{array} { r l r } { H } & { = } & { \frac { 1 } { 2 } { p } _ { 0 } ^ { T } M _ { 0 } ( { q } _ { 0 } ) ^ { - 1 } { p } _ { 0 } + \frac { 1 } { 2 } { p } _ { 1 } ^ { T } \Omega ( { q } _ { 0 } ) ^ { 2 } { p } _ { 1 } + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } { q } _ { 1 } ^ { T } { q } _ { 1 } } \\ & { } & { \mathrm + \frac { 1 } { 2 } { p } ^ { T } R ( { q } ) { p } + U ( { q } _ { 0 } + G Q ( { q } _ { 0 } ) { q } _ { 1 } , Q ( { q } _ { 0 } ) { q } _ { 1 } ) . } \end{array}
$$

RescalingPositionsandMomenta.Wechangeto rescaled fast variables

$$
q _ { 0 } = \check { q } _ { 0 } , ~ q _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } \check { q } _ { 1 }
$$

(note that $q _ { 1 } = \mathcal { O } ( \varepsilon )$ implies $\check { q } _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } ) )$ with the conjugate momenta

$$
\check { p } _ { 0 } \equiv p _ { 0 } + \varepsilon ^ { 1 / 2 } \Big ( { \frac { \partial } { \partial \check { q } _ { 0 } } } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } \check { q } _ { 1 } \Big ) ^ { T } p _ { 1 } , \quad \check { p } _ { 1 } = \varepsilon ^ { 1 / 2 } \varOmega ( \check { q } _ { 0 } ) ^ { 1 / 2 } p _ { 1 } .
$$

In thenew variables,the Hamiltonian becomes(we omit the haceks onall variables)

$$
\begin{array} { r c l } { { H } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } { \varOmega } ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } { \varOmega } ( q _ { 0 } ) q _ { 1 } } } \\ { { } } & { { } } & { { \displaystyle { + \frac { 1 } { 2 } } p ^ { T } R ( q ) p + U ( T ( q _ { 0 } ) q ) , } } \end{array}
$$

where

$$
T = \Big ( T _ { 0 } \ \big \vert \ \varepsilon ^ { 1 / 2 } T _ { 1 } \Big ) = \left( \begin{array} { c c } { I } & { \varepsilon ^ { 1 / 2 } G Q \varOmega ^ { 1 / 2 } } \\ { 0 } & { \varepsilon ^ { 1 / 2 } Q \varOmega ^ { 1 / 2 } } \end{array} \right)
$$

and $R ( q )$ isa symmetric matrix of the form

$$
R ( q ) = \left( \begin{array} { c c } { { R _ { 0 0 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } & { { \varepsilon ^ { - 1 / 2 } R _ { 0 1 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } \\ { { \varepsilon ^ { - 1 / 2 } R _ { 1 0 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } & { { \varepsilon ^ { - 1 } R _ { 1 1 } ( q _ { 0 } , \varepsilon ^ { 1 / 2 } q _ { 1 } ) } } \end{array} \right)
$$

with smooth functions $R _ { i j }$ satisfying $R _ { i j } ( q _ { 0 } , 0 ) = 0$ Therefore,the expression ${ \scriptstyle { \frac { 1 } { 2 } } } p ^ { T } R ( q ) p$ can berewritten in the form

$$
\begin{array} { r c l } { \frac { 1 } { 2 } \boldsymbol { p } ^ { T } \boldsymbol { R } ( \boldsymbol { q } ) \boldsymbol { p } } & { = } & { \boldsymbol { \varepsilon } ^ { 1 / 2 } \boldsymbol { c } ( \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) ^ { T } \boldsymbol { q } _ { 1 } + \boldsymbol { p } _ { 1 } ^ { T } \boldsymbol { L } ( \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) ^ { T } \boldsymbol { q } _ { 1 } } \\ & & { + } & { \boldsymbol { \varepsilon } ^ { - 1 / 2 } \boldsymbol { \tau } ( \boldsymbol { p } _ { 1 } , \boldsymbol { p } _ { 1 } , \boldsymbol { q } _ { 1 } ; \boldsymbol { p } _ { 0 } , \boldsymbol { q } _ { 0 } ) + \rho ( \boldsymbol { p } , \boldsymbol { q } ) , } \end{array}
$$

withavector $c$ ,amatrix $L$ ,afunction $\tau$ that is trilinear in $p _ { 1 } , p _ { 1 } , q _ { 1 }$ ,andaremainder ofsize $\rho ( p , q ) = { \mathcal O } ( \varepsilon ^ { 2 } )$ for $p _ { 1 } , q _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ whosepartial derivatives with respect to $p _ { 1 } , q _ { 1 }$ are ofsize $\mathcal { O } ( \varepsilon ^ { 3 / 2 } )$ ,and with respect to $p _ { 0 } , q _ { 0 }$ ofsize $\mathcal { O } ( \varepsilon ^ { 2 } )$ ,

Equations of Motion.The differential equations now take the form

$$
\begin{array} { r c l } { { \dot { p } _ { 0 } } } & { { = } } & { { \displaystyle - \nabla _ { q _ { 0 } } \left( \frac { 1 } { 2 } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + U ( q _ { 0 } , 0 ) \right) } } \\ { { } } & { { } } & { { \displaystyle - \nabla _ { q _ { 0 } } \left( \frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \mathcal { Q } ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \mathcal { Q } ( q _ { 0 } ) q _ { 1 } \right) + f _ { 0 } ( p , q ) } } \\ { { \dot { q } _ { 0 } } } & { { = } } & { { \displaystyle M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + g _ { 0 } ( p , q ) } } \\ { { \left( \begin{array} { c } { { \dot { p } _ { 1 } } } \\ { { \dot { q } _ { 1 } } } \end{array} \right) } } & { { = } } & { { \displaystyle \frac { 1 } { \varepsilon } \left( \begin{array} { c c } { { 0 } } & { { - \mathcal { Q } ( q _ { 0 } ) } } \\ { { \mathcal { Q } ( q _ { 0 } ) } } & { { 0 } } \end{array} \right) \left( \begin{array} { c } { { p _ { 1 } } } \\ { { q _ { 1 } } } \end{array} \right) + \left( \begin{array} { c } { { f _ { 1 } ( p , q ) } } \\ { { g _ { 1 } ( p , q ) } } \end{array} \right) } } \end{array}
$$

with the functions

$$
\begin{array} { r c l } { { \left( \begin{array} { c } { { f _ { 0 } } } \\ { { f _ { 1 } } } \end{array} \right) } } & { { = } } & { { - \nabla _ { q } \left( \frac 1 2 p ^ { T } R ( q ) p + U ( T ( q _ { 0 } ) q ) - U ( q _ { 0 } , 0 ) \right) } } \\ { { } } & { { } } & { { } } \\ { { \left( \begin{array} { c } { { g _ { 0 } } } \\ { { g _ { 1 } } } \end{array} \right) } } & { { = } } & { { R ( q ) p . } } \end{array}
$$

We note the magnitudes $f _ { 0 } = \mathcal { O } ( \varepsilon )$ , $g _ { 0 } = \mathcal { O } ( \varepsilon )$ and $f _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ , $g _ { 1 } = \mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ inthecase of separated eigenfrequencies,where the diagonalizationis smooth with bounded derivatives.By(3.11）we have(omittingthearguments $p _ { 0 } , q _ { 0 }$ in $c , L , I ^ { \prime }$ ）

$$
\begin{array} { r l r } { f _ { 1 } } & { = } & { - \varepsilon ^ { 1 / 2 } c - L p _ { 1 } + \varepsilon ^ { - 1 / 2 } a ( p _ { 1 } , p _ { 1 } ; p _ { 0 } , q _ { 0 } ) - \varepsilon ^ { 1 / 2 } T _ { 1 } ^ { T } \nabla U ( q _ { 0 } , 0 ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) } \\ { g _ { 1 } } & { = } & { L ^ { T } q _ { 1 } + \varepsilon ^ { - 1 / 2 } b ( p _ { 1 } , q _ { 1 } ; p _ { 0 } , q _ { 0 } ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) \qquad ( \partial _ { \tau } \partial _ { q _ { 0 } } q _ { 0 } ) + { \mathcal O } ( \varepsilon ^ { 3 / 2 } ) , } \end{array}
$$

where the functions $a$ and $b$ are bilinear in their first twoarguments.

TheSystemin Adiabatic Variables.We finally leave the canonical framework and transformtoadiabaticvariables as in(2.16).Alongasolution $( p ( t ) , q ( t ) )$ ofthe system (3.12)we consider the diagonal phase matrix $\varPhi ( t )$ defined by

$$
\dot { \Phi } = \Lambda ( q _ { 0 } ) \mathrm { w i t h } \Lambda ( q _ { 0 } ) = \left( \begin{array} { c c } { { \Omega ( q _ { 0 } ) } } & { { 0 } } \\ { { 0 } } & { { - \Omega ( q _ { 0 } ) } } \end{array} \right) .
$$

With the constant unitary matrix $\varGamma$ of(2.14），which diagonalizes the matrix in (3.12),we introduce theadiabatic variables

$$
\eta = \varepsilon ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi \right) \bar { \varGamma } ^ { \ast } \left( \begin{array} { c } { { p _ { 1 } } } \\ { { q _ { 1 } } } \end{array} \right)
$$

and denote the inverse transform as

$$
\binom { p _ { 1 } } { q _ { 1 } } = \varepsilon ^ { 1 / 2 } \binom { p _ { 1 } } { Q _ { 1 } } \eta = \varepsilon ^ { 1 / 2 } { \cal { T } } \exp \Big ( \frac { i } { \varepsilon } \Phi \Big ) \eta .
$$

The differential equations (3.12) for $p _ { 1 } , q _ { 1 }$ then turn into

$$
\dot { \eta } = \dot { \varepsilon } ^ { - 1 / 2 } \exp \left( - \frac { i } { \varepsilon } \varPhi \right) \varGamma ^ { * } \left( { \begin{array} { c } { f _ { 1 } } \\ { g _ { 1 } } \end{array} } \right) = \varepsilon ^ { - 1 / 2 } P _ { 1 } ^ { * } f _ { 1 } + \varepsilon ^ { - 1 / 2 } Q _ { 1 } ^ { * } g _ { 1 }
$$

with the arguments $( p _ { 0 } , \varepsilon ^ { 1 / 2 } P _ { 1 } \eta , q _ { 0 } , \varepsilon ^ { 1 / 2 } Q _ { 1 } \eta )$ in the functions $f _ { 1 } , g _ { 1 } .$ Inserting the expressions for $f _ { 1 }$ and $g _ { \mathrm { 1 } }$ from(3.13),we obtain as in(2.22) and(2.23),with

$$
W = - \frac { 1 } { 2 } \left( \begin{array} { c c } { { L - L ^ { T } } } & { { L + L ^ { T } } } \\ { { L + L ^ { T } } } & { { L - L ^ { T } } } \end{array} \right) ,
$$

thedifferential equation

$$
\begin{array} { r c l } { \dot { \eta } } & { = } & { \displaystyle \exp ( - \frac { i } { \varepsilon } \varPhi ) W ( p _ { 0 } , q _ { 0 } ) \exp ( \frac { i } { \varepsilon } \varPhi ) \eta } \\ & & { +  \exp ( - \frac { i } { \varepsilon } \varPhi ) L ^ { * } ( ^ { a ( P _ { 1 } \eta , P _ { 1 } \eta ; p _ { 0 } , q _ { 0 } ) } _ { b ( P _ { 1 } \eta , Q _ { 1 } \eta ; p _ { 0 } , q _ { 0 } ) } ) } \\ & & { -  P _ { 1 } ^ { * } ( c ( p _ { 0 } , q _ { 0 } ) + T _ { 1 } ( q _ { 0 } ) ^ { T } \nabla U ( q _ { 0 } , 0 ) ) + r } \end{array}
$$

with the remainder $r ( p _ { 0 } , q _ { 0 } , P _ { 1 } \eta , Q _ { 1 } \eta ) = \mathcal { O } ( \varepsilon ) .$

Adiabatic Invariants.Fora solutionwith bounded energy,both $p _ { 1 } ( t )$ and $q _ { 1 } ( t )$ in (3.12)are of size $\mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ and hence

$$
\eta ( t ) = \mathcal { O } ( 1 ) .
$$

Wenow integrate both sides of the above differential equation from Oto $t$ The integral of the terms in (3.19)is $\mathcal { O } ( \varepsilon )$ ,asisseen bypartial integration since $P _ { 1 } ^ { * } ( t )$ is oscillatory with an $\mathcal { O } ( \varepsilon )$ integral and $p _ { 0 } , q _ { 0 }$ havebounded derivatives.

Wenow suppose that the eigenfrequencies $\omega _ { j } ( t ) : = \omega _ { j } ( q _ { 0 } ( t ) )$ remain separated and bounded away from $_ 0$ thereisaconstant $\delta > 0$ such that for any pair $\omega _ { j } ( t )$ and $\omega _ { k } ( t )$ with $j \neq k$ ,thelower bounds

$$
| \omega _ { j } ( t ) - \omega _ { k } ( t ) | \geq \delta , \quad \ \omega _ { j } ( t ) \geq \frac { \delta } { 2 }
$$

hold for all $t$ underconsideration.In this situation,asin Sect.XIV.2.1,the integral from0to $t$ of the term(3.17） is bounded by $\mathcal { O } ( \varepsilon )$ ,since the matrix $W$ has zero diagonal.

Itremains to study the term(3.18）with the bilinear functions $^ a$ and $b$ This termhas only oscillatory components if the following non-resonance condition is satisfied:for all $j , k , l$ andall combinations of signs,

$$
| \omega _ { j } ( t ) \pm \omega _ { k } ( t ) \pm \omega _ { l } ( t ) | \geq \delta
$$

with a positive $\delta$ independent of $\boldsymbol { \varepsilon } .$ In this case,also the integral over the term(3.18) is of size $\mathcal { O } ( \varepsilon )$ ,andwe obtain

$$
\eta ( t ) = \eta ( 0 ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

If condition (3.21) is weakened torequiring thatfor all $j , k , l = 1 , \ldots , m$

$$
\omega _ { j } ( t ) \pm \omega _ { k } ( t ) \pm \omega _ { l } ( t ) \ \mathrm { h a s ~ a ~ f i n i t e ~ n u m b e r ~ o f ~ a t ~ m o s t ~ s i m p l e ~ z e r o s }
$$

inthe considered time interval,then the estimate deteriorates to (see Exercise1)

$$
\eta ( t ) = \eta ( 0 ) + { \cal O } ( \varepsilon ^ { 1 / 2 } ) \mathrm { f o r } t \leq \mathrm { C o n s t } .
$$

Theactions

$$
I _ { j } = | \eta _ { j } | ^ { 2 } \qquad ( j = 1 , \ldots , m )
$$

are thus adiabatic invariants:

$$
I _ { j } ( t ) = I _ { j } ( 0 ) + \mathcal { O } ( \varepsilon ) \mathrm { f o r } t \leq \mathrm { C o n s t } .
$$

in case of (3.22),andupto $\mathcal { O } ( \varepsilon ^ { 1 / 2 } )$ in case of (3.24).

The Slow System.Since the oscillatory energy equals

$$
\frac { 1 } { 2 \varepsilon } p _ { 1 } ^ { T } \varOmega ( q _ { 0 } ) p _ { 1 } + \frac { 1 } { 2 \varepsilon } q _ { 1 } ^ { T } \varOmega ( q _ { 0 } ) q _ { 1 } = \sum _ { j = 1 } ^ { m } I _ { j } \omega _ { j } ( q _ { 0 } ) ,
$$

thedifferential equations (3.12)fortheslow variables $p _ { 0 } , q _ { 0 }$ become,up to $\mathcal { O } ( \varepsilon )$

$$
\begin{array} { r c l } { \dot { p } _ { 0 } } & { = } & { \displaystyle - \nabla _ { g _ { 0 } } \Big ( \frac { 1 } { 2 } p _ { 0 } ^ { T } M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } + U ( q _ { 0 } , 0 ) \Big ) - \sum _ { j = 1 } ^ { m } I _ { j } \nabla _ { q _ { 0 } } \omega _ { j } ( q _ { 0 } ) } \\ { \dot { q } _ { 0 } } & { = } & { \displaystyle M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 } . } \end{array}
$$

Compared with the constrained system with Hamiltonian ${ \scriptstyle { \frac { 1 } { 2 } } } p ^ { T } M ( q ) ^ { - 1 } p + U ( q )$ on the configuration manifold $\nu$ ,the slow motion is thus driven by the additional potential $\textstyle \sum _ { j = 1 } ^ { m } I _ { j } \omega _ { j } ( q _ { 0 } )$ depending on the actions $I _ { j }$ See alsoRubin&Ungar (1957), Takens(198O),and Bornemann (1998) for different derivationsand discussions ofthe correction potential.

Avoided Crossing of Frequencies and Takens Chaos.If the distance $\delta$ of frequenciesin(3.2o) becomes so small at apoint $q _ { 0 } ( t )$ that $\delta ^ { 2 } \ \leq \varepsilon$ ,thentherecan again occur $\mathcal { O } ( 1 )$ changesin adiabatic invariants $I _ { j }$ ,asinthe Zener example of Sect.XIV.1.1.In the present situation of solution-dependent frequencies,however, the level to which $I _ { j }$ jumpsafter the avoided crossing,depends very sensitively on the slow solution variables $q _ { 0 } ( t )$ through the terms $\exp ( \pm \frac { i } { \varepsilon } \Phi )$ in (3.17).In turn,the slow motion of $\mathit { p } _ { 0 } , q _ { 0 }$ afterthe avoided crossing depends on the new values of $I _ { j }$ through(3.27).The effect is that the slow motion depends very sensitively on perturbations of the initial values in the case of an avoided crossing;see Takens(1980). The indeterminacy of the slow motion in the limit $\varepsilon \to 0$ istermed Takens chaos by Bornemann（1998）.

# XIV.3.3 Integratorsin Adiabatic Variables

Along-time-step integrator for the oscillatory mechanical system with Hamiltonian (3.1)can now be obtained as follows:

Solve the slow system(3.27)intandem with applyinganadiabatic integrator (see Sect.XIV.1.2) toasimplified equation for theadiabatic variables,

$$
\dot { \eta } = \exp \Bigl ( - \frac { i } { \varepsilon } \Phi \Bigr ) W \exp \Bigl ( \frac { i } { \varepsilon } \Phi \Bigr ) \eta ,
$$

where $W$ is given by(3.16)withasimplified matrix $L :$ with $v _ { 0 } = M _ { 0 } ( q _ { 0 } ) ^ { - 1 } p _ { 0 }$ ,let

$$
L ( p _ { 0 } , q _ { 0 } ) = - \Omega ( q _ { 0 } ) ^ { 1 / 2 } \left. \frac { d } { d \tau } \right| _ { \tau = 0 } Q ( q _ { 0 } + \tau v _ { 0 } ) ^ { T } Q ( q _ { 0 } ) \Omega ( q _ { 0 } ) ^ { - 1 / 2 } .
$$

Thismatrix $L$ captures the principal terms,coming from the matrix $X _ { 0 1 }$ in (3.8）, whichare responsible fora change of theadiabatic invariants dueto anavoided crossing as long as the frequency separation condition (3.2O) holdswith apossibly $\boldsymbol { \mathsf { E } }$ -dependent $\delta \gg \varepsilon$ ,e.g.,with $\delta \sim \varepsilon ^ { 1 / 2 }$ where $O ( 1 )$ changes occur in the adiabatic invariants.Because of the Takens chaos,itcannot beexpected that such an integrator yieldsagood approximation to“the”solution,butthe method can approximate analmost-solution (havinga small defectin the differential equations）that passes through the avoided crossing zone,and itdetects the change of adiabatic invariants. The properties of integrators of this type are currently under investigation (Lorenz &Lubich 2006).

Further we refer to Jahnke(2O03,2Oo4b) for theconstruction and analysis of adiabatic integrators for mixed quantum-classical molecular dynamics,where similarlyanonlinearcoupling of slow and fast,oscillatory motions occurs.

# XIV.3.4 Analysis of Multiple Time-SteppingMethods

The errorbehaviour of the impulseandmolified impulsemethod applied toan oscillatory Hamiltonian system(3.1）withwell-separated frequenciescan beanalysed intheadiabaticvariables in the samewayaswedidin Sections XIV.2.3and XIV.2.4 for the case of time-dependent frequencies.Analogous formulas and the same conclusions hold;essentially we need to replace the argument $t$ by $q _ { 0 }$ in the appearing functions.However,their behaviour in the situation ofan avoided crossingwith Takenschaos is presently not understood.

# XIV.4 Exercises

1.Show that

$$
\int _ { 0 } ^ { t } \exp \Big ( \frac { i } { \varepsilon } \phi ( s ) \Big ) d s = \mathcal { O } ( \varepsilon ^ { 1 / ( m + 1 ) } )
$$

if $\lambda : = \dot { \phi }$ has finitely many zeros of orderatmost $m$ in the interval $[ 0 , t ]$

Hint:Use the methodof stationary phase;see,e.g.,Olver(1974) or van der Corput (1934).

2.Show that the adiabatic variables $\eta ( t )$ of（1.4）remain approximately constant also in the following cases of non-separated eigenvalues:

（a）amultiple eigenvalue $\lambda _ { j } ( t )$ of constant multiplicity $m$ forall $t$ and the orthogonal basis $v _ { j , 1 } ( t ) , \ldots , v _ { j , m } ( t )$ ofthe corresponding eigenspace chosen such that the derivatives $\dot { v } _ { j , l } ( t )$ areorthogonal to the eigenspace forall $t$ ;

(b)acrossing of eigenvalues, $\lambda _ { j } ( t _ { * } ) = \lambda _ { k } ( t _ { * } )$ with $\dot { \lambda } _ { j } ( t _ { * } ) \neq \dot { \lambda } _ { k } ( t _ { * } )$ ,forwhich theeigenvectors are smooth functions of $t$ inaneighbourhood of $t _ { * }$ ;seealso Born&Fock（1928） for crossingswhere $\lambda _ { j } ~ - ~ \lambda _ { k }$ can have zeros of higher multiplicity.

3.Let the differential equation（1.1） with smooth skew-hermitian $Z ( t )$ be transformed locally over $[ t _ { 0 } , t _ { 0 } + h ]$ to $\begin{array} { r } { z ( t ) = \exp ( - \frac { t } { \varepsilon } Z _ { * } ) y ( t ) } \end{array}$ ,sothat

$$
\dot { z } = \frac { 1 } { \varepsilon } \exp ( - \frac { t } { \varepsilon } Z _ { * } ) \left( Z ( t ) - Z _ { * } \right) \exp ( \frac { t } { \varepsilon } Z _ { * } ) z
$$

with $Z _ { * } = Z ( t _ { 0 } + h / 2 ) $ Consider the averaged midpoint rule

$$
z _ { 1 } = z _ { 0 } + \frac { 1 } { \varepsilon } \int _ { 0 } ^ { h } \exp ( - \frac { s } { \varepsilon } Z _ { \star } ) \left( \widetilde { Z } ( s ) - Z _ { \star } \right) \exp ( \frac { s } { \varepsilon } Z _ { \star } ) d s \ \frac { 1 } { 2 } ( z _ { 0 } + z _ { 1 } ) ,
$$

where $Z ( t )$ is thequadratic interpolation polynomial through $Z ( t _ { 0 } )$ , $Z _ { * }$ , $Z ( t _ { 1 } )$ . Show that the local error $z _ { 1 } - z ( t _ { 1 } )$ is of size $\mathcal { O } ( h ^ { 4 } / \varepsilon ^ { 2 } )$ ,whichis $\mathcal { O } ( h ^ { 2 } )$ only for $h = { \mathcal { O } } ( \varepsilon )$ .Explainwhy the error bound cannot be improved to $\mathcal { O } ( h ^ { 2 } )$ for $h = \mathcal { O } ( \varepsilon ^ { \alpha } )$ with $\alpha < 1$ .

Hint:See the proofs of Theorems2.1(i）and 3.1 in Hochbruck& Lubich (1999b),cf.alsoIserles(2004).

4.In the situation of the previous exercise,let $U$ beaunitary matrix of eigenvectorsof $Z _ { * }$ ,andlet $\tilde { D } ( t )$ be the diagonal matrix containing the diagonal entries of ${ \cal U } ^ { * } \big ( \tilde { Z } ( t ) - Z _ { * } \big ) { \cal U } .$ Findamodification of the above averaged midpoint rule by terms that use only $\bar { D } ( t )$ ,such that the local error is $\mathcal { O } ( h ^ { 2 } )$ for $h \leq \varepsilon ^ { 3 / 4 }$ if the eigenvalues of $Z _ { * }$ areallseparatedbyadistance $\delta$ independent of $\varepsilon$ .

5.Compare the error behaviour of the averaged midpoint rules (1.12) and (4.1) nearthe avoided crossing of the eigenvalues in the Zener matrix(1.9).

6.Formulate symmetric modifications of the adiabatic integrators(1.12）and (1.13)that use function evaluations at the grid points $t _ { n }$ and $t _ { n + 1 }$ instead of $t _ { n + 1 / 2 }$

7.Consider the differential equation $\dot { y } = f ( y ) + g ( t )$ with a smooth function $f ( y )$ anda function $g ( t ) = \mathcal { O } ( 1 )$ with $\dot { g } ( t ) = \mathcal { O } ( \delta ^ { - 1 } )$ with respect toa small parameter $\delta .$ Forthe modified midpoint rule

$$
y _ { 1 } = y _ { 0 } + h f \Big ( \frac { y _ { 0 } + y _ { 1 } } { 2 } \Big ) + \int _ { t _ { 0 } } ^ { t _ { 1 } } g ( t ) d t ,
$$

showthat the localerror satisfies $y _ { 1 } - y ( t _ { 1 } ) = \mathcal { O } ( h ^ { 3 } / \delta )$

8.Write theHamiltonian system(XIII.9.2)in adiabatic variables and relate this tc thefirst terms of the modulated Fourier expansion.

9.Compare the impulse method of Sect.XIV.2.3 with the method based on the splitting

$$
H = { \Big ( } { \frac { 1 } { 2 } } p ^ { T } M ( t ) ^ { - 1 } p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q ^ { T } A ( t ) q { \Big ) } + { \Big ( } U ( q , t ) + E { \Big ) } .
$$

10.Show that Theorem2.6 remainsvalid for thechoice ${ \mathbfcal { S } } ( t ) = 0$ in(2.37）.This correspondsto the projection to the constraint manifold in the mollified impulse methodasproposed by Izaguirre,Reich&Skeel(1999).

# Chapter XV. Dynamics of Multistep Methods

Multistep methodsare the basis of importantcodes for nonstiff differential equations(Adamsmethods)and for stiff problems(BDF methods).We study here their applicability to long-time integrations of Hamiltonian or reversible systems.

This chapter starts with numerical experiments which illustrate that the longtimebehaviour of classical multistep methods isin general disappointing.They eitherbehave as non-symplectic and non-symmetric one-step methods,or theyexhibitundesired instabilities(parasitic solutions).Certain multistep methods forsecondorder equations orpartitioned multistepmethods,however,haveamuch better long-time behaviour.They are promisingmethods,because ina constant step size mode they can be easily implemented,and high order can be obtained with one function evaluation per step.We characterize such methods by studying their underlyingone-step method,their symplecticity,their conservation properties,as wellas their long-term stability.

# XV.1 Numerical Methods and Experiments

Wepresent the numerical methods treated in this chapter,and in numerical experimentswe look at their behaviour on Hamiltonian systems.

# XV.1.1LinearMultistep Methods

For first order systems of differential equations $\dot { y } = f ( y )$ ,linear multistep methods aredefinedbytheformula

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } f ( y _ { n + j } ) ,
$$

where $\alpha _ { j } , \beta _ { j }$ arereal parameters, $\alpha _ { k } \neq 0$ ,and $| \alpha _ { 0 } | + | \beta _ { 0 } | > 0$ Foran application ofthis formula we needa starting procedurewhich,inaddition to an initial value $y ( t _ { 0 } ) = y _ { 0 }$ ,provides approximations $y _ { 1 } , \ldots , y _ { k - 1 }$ to $y ( t _ { 0 } + h ) , \dotsc , y ( t _ { 0 } + ( k - 1 ) h ) .$ Theapproximations $y _ { n }$ to $y ( t _ { 0 } + n h )$ for $n \geq k$ can then be computed recursively from(1.1).In the case $\beta _ { k } = 0$ we have an explicit method,otherwise itis implicit and the numerical solution $y _ { n + k }$ has to be computed iteratively.

![](images/b3058f513b89779dc7d506de631664dfb3e9e2312711f79c222ee0917c1c898d.jpg)  
Germund Dahlquist1

Since thefundamental work of Dahlquist （1956)itiscommon todenotethe generating polynomials of the coefficients by

$$
\rho ( \zeta ) \equiv \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta ^ { j } , \qquad \sigma ( \zeta ) = \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta ^ { j } .
$$

For the classical theory of multistep methods we refer the reader to Chap.IIIof Hairer, Norsett&Wanner(1993).We just recall some important definitions.

Order.A multistep method has order $r$ if, when applied with exact starting values to the problem $\dot { y } = t ^ { q }$ ( $0 \leq q \leq r$ ),it integrates the problem without error.This is equivalent tothe requirement that

$$
\rho ( e ^ { h } ) - h \sigma ( e ^ { h } ) = \mathcal { O } ( h ^ { r + 1 } ) \qquad \mathrm { f o r } \quad h \to 0 .
$$

Stability.Method(1.1）is stable if,whenapplied to $y ~ = ~ 0$ ,ityields for all $y _ { 0 } , \ldots , y _ { k - 1 }$ abounded numerical solution.Thisis equivalent to the requirement thatthe polynomial $\rho ( \zeta )$ satisfies the root condition,i.e.,all roots of $\rho ( \zeta ) = 0$ satisfy $| \zeta | \le 1$ ,andthoseon theunit circle are simpleroots.The methodis called strictly stable,ifall rootsareinside the unit circle with theexception of $\zeta = 1$

Convergence.If a multistep method is stable and of order $r \geq 1$ ,itis convergent of order $r$ forall sufficiently smooth problems.This means that,assuming starting approximationswith an error bounded by $\mathcal { O } ( h ^ { r } )$ ,theglobal error satisfies $y _ { n } -$ $y ( t _ { 0 } + n h ) = \mathcal { O } ( h ^ { r } )$ oncompact intervals $n h \le { \cal T }$ ..

Symmetry.If the coefficients ofamultistep formula(1.1） satisfy

$$
\alpha _ { k - j } = - \alpha _ { j } , \qquad \beta _ { k - j } = \beta _ { j } \qquad \mathrm { f o r ~ a l l } ~ j ,
$$

thenthe method iscalled symmetric.Condition (1.3) implies that for every zero $\zeta$ of $\rho ( \zeta )$ also its inverse $\zeta ^ { - 1 }$ isazero.Hence,forstable symmetric methods all zeros of $\bar { \rho } ( \zeta )$ are simple and lie on the unit circle.

Example1.1.Weconsider the pendulum equation (I.1.13),and weapply the followingmultistepmethods:the2-step explicit Adams method

$$
y _ { n + 2 } = y _ { n + 1 } + h \Big ( \frac 3 2 f _ { n + 1 } - \frac 1 2 f _ { n } \Big ) ,
$$

the2-step backward diferentiation formula (BDF)

$$
{ \frac { 3 } { 2 } } y _ { n + 2 } - 2 y _ { n + 1 } + { \frac { 1 } { 2 } } y _ { n } = h f _ { n + 2 } ,
$$

and the (2-step) symmetric explicit midpoint rule

![](images/deb21da6077deedfdc82cee4fe06206e5bb8da7d7a806798a117737a2778e9f3.jpg)  
Fig.1.1.Solutions of thependulum problem(I.1.13);explicit Adams with step size $h =$ 0.5,initial value $( p _ { 0 } , q _ { 0 } ) = ( 0 , 0 . 7 )$ BDFwith step size $h = 0 . 5$ ,initialvalue $( p _ { 0 } , q _ { 0 } ) =$ $( 0 , 0 . 9 5 )$ ;explicit midpoint rulewith $h = 0 . 4$ and initialvalue $( p _ { 0 } , q _ { 0 } ) = ( 1 . 1 , 0 )$

$$
y _ { n + 2 } = y _ { n } + 2 h f _ { n + 1 } .
$$

Forall methodswe take $y _ { 1 } = y _ { 0 } + h f _ { 0 }$ as the approximation for $y ( t _ { 0 } + h )$ The resultsof the first 108 stepsare shown in Fig.1.1.We observe that the first two methods,as expected,behave similarly as the explicit and implicit Euler method (thenumerical solutionspiralseitheroutwardsorinwards).Thiswill be rigorously explainedinSect.XV.2.1below.However,asmight notbeexpected,thesymmetric method(1.6)does notbehave like the implicit midpoint rule(cf.Fig.I.1.4),it shows undesired increasing oscillations (parasitic solutions).

After this negative experience with classical multistep methods,the obvious question is:are there multistep methods which havea long-time behaviour that is comparable to symplectic and/or symmetric one-step methods?

# XV.1.2 Multistep Methods for Second Order Equations

Many important Hamiltonian systems are second order differential equations

$$
{ \ddot { y } } = f ( y ) ,
$$

where the force $f$ isindependent of the velocity $\dot { y }$ Introducing the new variable alitepewiet ,weobtain the system , $\dot { v } = f ( y )$ offirst order equations.Ifwe apply $\begin{array} { r } { \rho ^ { * } ( \zeta ) = \sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } \zeta ^ { j } } \end{array}$ and （=∑isteget

$$
\sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } y _ { n + j } = h \sum _ { j = 0 } ^ { k ^ { * } } \beta _ { j } ^ { * } v _ { n + j ; } \qquad \sum _ { j = 0 } ^ { k ^ { * } } \alpha _ { j } ^ { * } v _ { n + j } = h \sum _ { j = 0 } ^ { k ^ { * } } \beta _ { j } ^ { * } f ( y _ { n + j } ) .
$$

An elimination of the $\boldsymbol { v }$ variables thenyields

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } f ( y _ { n + j } ) ,
$$

where $k = 2 k ^ { * }$ ， $\rho ( \zeta ) = \rho ^ { * } ( \zeta ) ^ { 2 }$ and $\sigma ( \zeta ) = \sigma ^ { * } ( \zeta ) ^ { 2 }$ We consider here methods （1.8）whichdo not necessarily originate from amultistepmethod for first order equations,and we denote the generating polynomials of the coefficients $\alpha _ { j }$ and $\beta _ { j }$ againby $\rho ( \zeta )$ and $\sigma ( \zeta )$ Fromtheclassical theory(see Sect.III.1Oof Hairer,Norsett &Wanner 1993)we recall the followingdefinitions and results.

Order.A method(1.8)has order $r$ if its generating polynomials satisfy

$$
\rho ( e ^ { h } ) - h ^ { 2 } \sigma ( e ^ { h } ) = \mathcal { O } ( h ^ { r + 2 } ) \qquad \mathrm { f o r } \quad h \to 0 .
$$

Stability.Method(1.8) is stable if all zeros of thepolynomial $\rho ( \zeta )$ satisfy $| \zeta | \le 1$ ， andthose on the unit circle are at most double zeros.Observe that for methods originatingfrom(1.1）all zerosaredouble.Themethod iscalled strictly stable,if all zeros are inside the unit circle with the exception of $\zeta = 1$

Convergence.If amultistep method(1.8) is stable,of order $r \geq 1$ and if the starting valuesare accurate enough,the global error satisfies $y _ { n } - y ( t _ { 0 } + n h ) = \mathcal { O } ( h ^ { r } )$ on compact intervals $n h \le T$ .

SymmetryIfthecoefficientsof(1.8)satisfy

$$
\alpha _ { k - j } = \alpha _ { j } , \qquad \beta _ { k - j } = \beta _ { j } \qquad \mathrm { f o r ~ a l l } ~ j ,
$$

then themethod issymmetric.Again,for every zero $\zeta$ of $\rho ( \zeta )$ thevalue $\zeta ^ { - 1 }$ isalso a zero.Hence,stable symmetric methods have all zeros of $\rho ( \zeta )$ on the unit circle and they are at most of multiplicity two.

Dahlquist(1956) noticed that double zeros of $\rho ( \zeta )$ on the unit circle can lead to anexponential error growth.Lambert&Watson（1976)analyzedindetail the application of(1.8)to the linear test equation $\ddot { y } = - \omega ^ { 2 } y .$ They found thatwith symmetricmethods forwhich $\rho ( \zeta )$ does not have double roots on the unit circle other than $\zeta = 1$ ,thenumerical solution remainsclose toaperiodic orbit(forsufficiently small stepsizes).For example,theStormer-Verlet method $y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } f _ { n }$ satisfies this property for $0 < h \omega < 2$ (see Sect.I.5.2).The study of thelong-time behaviour of symmetric methods(1.8)was then put forward by the article of Quinlan&Tremaine(199o),wherean excellent performance for simulations of the outer solar system is reported.

Example1.2.We consider the Keplerproblem (I.2.2）with initial values(I.2.11) and eccentricity $e = 0 . 2$ .Weapply the following three methods with constant step size $h = 0 . 0 1$ on the interval of length $2 \pi \cdot 1 0 ^ { 5 }$ (i.e., $1 0 ^ { 5 }$ periods):

$$
\begin{array} { r l } & { y _ { n + 4 } - 2 y _ { n + 3 } + y _ { n + 2 } = h ^ { 2 } \Big ( \cfrac { 7 } { 6 } f _ { n + 3 } - \cfrac { 5 } { 1 2 } f _ { n + 2 } + \cfrac { 1 } { 3 } f _ { n + 1 } - \cfrac { 1 } { 1 2 } f _ { n } \Big ) } \\ & { y _ { n + 4 } - 2 y _ { n + 2 } + y _ { n } = h ^ { 2 } \Big ( \cfrac { 4 } { 3 } f _ { n + 3 } + \cfrac { 4 } { 3 } f _ { n + 2 } + \cfrac { 4 } { 3 } f _ { n + 1 } \Big ) } \\ & { y _ { n + 4 } - 2 y _ { n + 3 } + 2 y _ { n + 2 } - 2 y _ { n + 1 } + y _ { n } = h ^ { 2 } \Big ( \cfrac { 7 } { 6 } f _ { n + 3 } - \cfrac { 1 } { 3 } f _ { n + 2 } + \cfrac { 7 } { 6 } f _ { n + 1 } \Big ) . } \end{array}
$$

![](images/e8240c0dc1fce402b89c6029b359aed0926c99b94742947980e780371df65363.jpg)  
Fig.1.2.Error in the total energy for the three linear multistep methods of Example1.2 appliedtothe Keplerproblemwith $e = 0 . 2$

All three methodsare of order $r = 4$ method(A)isstrictlystable,whereasmethods (B）and(C)are symmetric.For method(B） the $\rho$ -polynomial hasadoublerootat $\zeta = - 1$ ,formethod (C) it doesnot havedoubleroots other than1.Startingvalues $y _ { 1 } , y _ { 2 }$ ,and $y _ { 3 }$ arecomputedveryaccuratelywithahigh-orderRunge-Kuttamethod.

Theerror in the total energy isplotted forall three methodsin Fig.1.2.On thefirst1O periods,all methodsbehave similarlyand noerror growth isobserved. Beyond this interval,method（A）showsa linearerror growth（as itis thecase for non-symplecticand non-symmetric one-stepmethods),method(B) has an exponential error growth,and formethod(C) the errorremains bounded ofsize $\mathcal { O } ( h ^ { 4 } )$ on thewhole interval of integration.One of the aims of this chapter is to explain the excellent long-time behaviour of method(C).

Stabilized Version of(1.8).Due to the double zeros (of modulus one) of the characteristic polynomial of thedifferenceequation $\sum _ { j } \alpha _ { j } y _ { n + j } = 0$ ,we have an undesired propagation of rounding errors (especially for long-time integrations）.To overcome this difficulty,wesplit the characteristic polynomial $\rho ( \zeta )$ into

$$
\rho ( \zeta ) = \rho _ { A } ( \zeta ) \cdot \rho _ { B } ( \zeta ) ,
$$

such that each polynomial

$$
\rho _ { A } ( \zeta ) = \sum _ { j = 0 } ^ { k _ { A } } \alpha _ { j } ^ { ( A ) } \zeta ^ { j } , \qquad \rho _ { B } ( \zeta ) = \sum _ { j = 0 } ^ { k _ { B } } \alpha _ { j } ^ { ( B ) } \zeta ^ { j }
$$

hasonly simple roots of modulus one. Introducing the new variable $h v _ { n } : =$ $\sum _ { j } \alpha _ { j } ^ { ( A ) } y _ { n + j }$ ,therecurrencerelation（1.8) becomes equivalent to

$$
\sum _ { j = 0 } ^ { k _ { A } } \alpha _ { j } ^ { ( A ) } y _ { n + j } = h v _ { n ; } \qquad \sum _ { j = 0 } ^ { k _ { B } } \alpha _ { j } ^ { ( B ) } v _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } f _ { n + j } .
$$

Thisformula,which for the Stormer-Verlet scheme correspondsto the one-step formulation(I.1.17),ismuch better suited for an implementation.If the splitting issuch that $\rho _ { A } ^ { \prime } ( 1 ) = 1$ ,thediscretization(1.12）isconsistent with the first order partitioned system $\dot { y } = v , \dot { v } = f ( y )$

# XV.1.3PartitionedMultistep Methods

Motivated by the stabilized version(1.12）of multistep methods for second order equations,letus consider general partitioned systems ofdifferential equations

$$
\dot { y } = f ( y , v ) , \qquad \dot { v } = g ( y , v ) ,
$$

where,needless tosay, $y$ and $v$ maybe vectors.Theideaistoapply differentmultistepmethodsto different components.We thus get

$$
\sum _ { j = 0 } ^ { k } { \alpha } _ { j } ^ { ( A ) } y _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } ^ { ( A ) } f _ { n + j ; } \qquad \sum _ { j = 0 } ^ { k } { \alpha } _ { j } ^ { ( B ) } v _ { n + j } = h \sum _ { j = 0 } ^ { k } \beta _ { j } ^ { ( B ) } g _ { n + j } ,
$$

where $f _ { n } = f ( y _ { n } , v _ { n } )$ and $g _ { n } = g ( y _ { n } , v _ { n } ) .$ We can take the same $k$ for both methods without loss of generality,if we abandon theassumption $| \alpha _ { 0 } | + | \beta _ { 0 } | > 0$

Such a method is of order $T$ ,ifboth methodsare of order $\boldsymbol { r } _ { * }$ It is stable (strictly stable,symmetric, $\cdot \cdot \cdot$ ),if both methodsare stable (strictly stable,symmetric,...).

Example 1.3. For our next experiment we use the symmetric methods

$$
\begin{array} { r l } { : } & { { } \quad y _ { n + 3 } - y _ { n + 2 } + y _ { n + 1 } - y _ { n } = h ( f _ { n + 2 } + f _ { n + 1 } ) } \\ { : } & { { } \quad v _ { n + 3 } - v _ { n + 1 } = 2 h g _ { n + 2 } . } \end{array}
$$

Both methods are of order 2,and their $\rho$ -polynomials $\rho _ { A } ( \zeta ) = ( \zeta - 1 ) ( \zeta ^ { 2 } + 1 )$ and $\rho _ { B } ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 )$ do not have common zeros with the exception of $\zeta = 1$ .

0

![](images/2fcd10fb90909a6ddbdee32d6546c7b4239ecb6bad0892979f99aca0187c6ee0.jpg)  
Fig.1.3.Three versions of the methods(1.15）applied with step size $h = 5 0$ （days）to the outersolarsystem.For method(B)only the numerical orbits of Jupiterand Saturn are plotted. Thetime intervals are given in units of $1 0 0 0 0$ days

Wechoose the outer solar systemwith thedataas described in Sect.I.2.4,and weapply the methods in three versions:（i)as partitioned method(AB),where the positions are treated bymethod (A） and thevelocities by method(B);(ii) method (A）isapplied to all components;(iii） method(B） isapplied to all components. Thenumerical resultsare shown in Fig.1.3.Whereas theindividual methods show instabilitieson rather short time intervals,the partitioned method givesa correct picture evenwith a large step size $h = 5 0$

# XV.2 The UnderlyingOne-Step Method

Much insight into the long-time behaviour of multistep methods can be gained by relating their numerical solution toone-step methods.This thenallows foran application of the considerations of the preceding sections.

# XV.2.1 Strictly Stable Multistep methods

Itwasa surprising result when Kirchgraber(1986)proved that strictly stable multistepmethodsare essentially equivalent to one-step methods.Although this one-step methodis“quiteexotic”(Eirola&Nevanlinna1988),itisthekeyforabetterunderstanding of thedynamics of strictly stable methods.

Theorem2.1 (Kirchgraber 1986). Considera strictly stable linear multistep method(1.1)appliedwithasufficiently small stepsize $h$ .Then,thereexistsa onestepmethod $\phi _ { h }$ such that for starting approximations computed by $y _ { j } = \varPhi _ { h } ^ { \jmath } ( y _ { 0 } )$ ， $j = 1 , \ldots , k - 1 ,$ thenumericalsolutionof(1.1) isidenticaltothat obtainedby the one-step method,i.e., $y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )$ forall $n \geq 0$

Proof.The ideais toreformulate themultistepmethod(1.1）in suchaway that the InvariantManifoldTheorem of Sect.XII.3canbeapplied.Tokeepthenotationas simple aspossible,let us consider the case $k = 3$ .

We writethe method in the form

$$
\left( { \begin{array} { c } { y _ { n + 3 } } \\ { y _ { n + 2 } } \\ { y _ { n + 1 } } \end{array} } \right) = \left( { \begin{array} { c c c } { - a _ { 2 } } & { - a _ { 1 } } & { - a _ { 0 } } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} } \right) \left( { \begin{array} { c } { y _ { n + 2 } } \\ { y _ { n + 1 } } \\ { y _ { n } } \end{array} } \right) + h \left( { \begin{array} { c } { F _ { h } ( y _ { n } , y _ { n + 1 } , y _ { n + 2 } ) } \\ { 0 } \\ { 0 } \end{array} } \right)
$$

with $a _ { i } = \alpha _ { i } / \alpha _ { k }$ ,andwe transform the appearing matrix $A$ to Jordan canonical form $J = T ^ { - 1 } A T .$ We thus get

$$
Z _ { n + 1 } \equiv \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { d _ { \mathrm { { 1 1 } } } } } & { { d _ { \mathrm { { 1 2 } } } } } \\ { { 0 } } & { { d _ { { 2 1 } } } } & { { d _ { { 2 2 } } } } \end{array} \right) Z _ { n } + h G ( Z _ { n } ) , \qquad \bar { Z } _ { n } = { \cal T } ^ { - 1 } \left( \begin{array} { c } { { y _ { n + 2 } } } \\ { { y _ { n + 1 } } } \\ { { y _ { n } } } \end{array} \right) .
$$

Since themethodis strictly stable,1 isa simple eigenvalue of $A$ ,andallother eigenvalues are less than 1in modulus.Consequently,the matrix $D = \left( d _ { i j } \right)$ satisfies

$\| D \| < 1$ inasuitable norm.Partitioning $Z _ { n } = ( \xi _ { n } , \eta _ { n } ) ^ { { \scriptscriptstyle T } }$ into its first component $\xi _ { n }$ and the rest (collected in $\eta _ { n }$ ),wesee that(2.2）is of the form(XI.3.1）with $L _ { x x } , L _ { x y } , L _ { y x }$ ofsize $\mathcal { O } ( h )$ ,and $L _ { y y } = \| D \| < 1 .$ TheoremXII.3.1thusyields the existence ofa function $\eta = s ( \xi )$ such that the manifolds

$$
\mathcal { N } _ { h } = \Big \{ \left( \begin{array} { c } { \xi } \\ { s ( \xi ) } \end{array} \right) ; \xi \in \mathbb { R } ^ { d } \Big \} \qquad \mathrm { a n d } \qquad \mathcal { M } _ { h } = \Big \{ T \left( \begin{array} { c } { \xi } \\ { s ( \xi ) } \end{array} \right) ; \xi \in \mathbb { R } ^ { d } \Big \}
$$

areinvariant under the mappings(2.2） and(2.1),respectively.The function $s ( \xi )$ is Lipschitz continuous with constant $\lambda = { \mathcal { O } } ( h )$ .

Since the first column of $T$ ,whichis the eigenvector corresponding to the eigenvalue $1$ of $A$ ,is given by $( 1 , 1 , 1 ) ^ { T }$ ,the last component of $T \left( { \xi } \atop { s ( \xi ) } \right)$ satisfies $y = \xi + g ( \xi )$ where $g ( \xi )$ isLipschitz continuous with constant ${ \mathcal { O } } ( h )$ BytheBanach fixed-point theorem this equation has a unique solution $\xi = r ( y ) .$ Consequently,the manifold $\mathcal { M } _ { h }$ can be parametrized in terms of $y$ as

$$
\mathcal { M } _ { h } = \big \{ ( \varPsi _ { h } ( y ) , \varPhi _ { h } ( y ) , y ) ^ { T } ; y \in \mathbb { R } ^ { d } \big \} .
$$

Its invarianceunder(2.1) implies that

$$
\begin{array} { r } { \mathrm {  { ~ \mathcal { F } ~ } } _ { h } ( \widehat { y } ) \mathrm {  { ~ \cal { F } ~ } } _ { h } ( \widehat { y } ) = \left( \begin{array} { c c c } { - a _ { 2 } } & { - a _ { 1 } } & { - a _ { 0 } } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} \right) \left( \begin{array} { l } { \varPsi _ { h } ( y ) } \\ { \varPhi _ { h } ( y ) } \\ { y } \end{array} \right) + h \left( \begin{array} { c } { F _ { h } ( y , \varPhi _ { h } ( y ) , \varPsi _ { h } ( y ) ) } \\ { 0 } \\ { 0 } \end{array} \right) } \end{array}
$$

and consequently $\widehat { y } = \varPhi _ { h } ( y )$ and $\varPhi _ { h } ( \widehat { y } ) = \varPsi _ { h } ( y )$ ,sothat $\varPsi _ { h } ( y ) = \varPhi _ { h } ^ { 2 } ( y )$ This holdsforall $y$ ,and thusproves the statement of the theorem. □

Example2.2.Fora scalarlinearproblem $\dot { y } = \lambda y$ ,theapplication ofamultistep method yieldsadifference equation withcharacteristicpolynomial $\rho ( \zeta ) - h \lambda \sigma ( \zeta )$ Denoting its zeros by $\zeta _ { 1 } ( h \lambda ) , \ldots , \zeta _ { k } ( h \lambda )$ ,where $\zeta _ { 1 } ( 0 ) = 1$ and $| \zeta _ { j } ( 0 ) | < 1$ for $j \geq 2$ ,the numerical solution can be written as (assuming distinct $\zeta _ { j } ( h \lambda )$ ）

$$
y _ { n } = c _ { 1 } \zeta _ { 1 } ^ { n } ( h \lambda ) + c _ { 2 } \zeta _ { 2 } ^ { n } ( h \lambda ) + . . . + c _ { k } \zeta _ { k } ^ { n } ( h \lambda ) .
$$

The coefficients $c _ { 1 } , \ldots , c _ { k }$ depend on $h \lambda$ andaredetermined by the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 } .$ Inthis situation theunderlying one-step method is the mapping $y _ { 0 } \mapsto \zeta _ { 1 } ( h \lambda ) y _ { 0 } .$ Observethat $\zeta _ { 1 } ( z )$ isin general not a rational function as weare used to with Runge-Kutta methods.

Remark2.3 (Asymptotic Phase).For arbitrary $y _ { 0 } , y _ { 1 } , \dotsc , y _ { k - 1 }$ close to the exact solution,there exists $y _ { 0 } ^ { * }$ such that the multistep solution $\left\{ y _ { n } \right\}$ and the one-step solution $\left\{ y _ { n } ^ { * } \right\}$ ,givenby ${ \boldsymbol y } _ { n + 1 } ^ { * } = \Phi _ { h } ( { \boldsymbol y } _ { n } ^ { * } )$ ,approach exponentially fast,i.e.,

$$
\| y _ { n } - y _ { n } ^ { * } \| \leq C o n s t \cdot \rho ^ { n } \qquad { \mathrm { f o r ~ a l l ~ } } n \geq 0
$$

with some $\rho$ satisfying $0 < \rho < 1$ (seeExercise XII.3).This is due to the attractivity of the invariant manifold $\mathcal { M } _ { h }$ Aproof isgiveninStoffer(1993),and itisbasedon techniques of Nipp $\&$ Stoffer(1992).Thisresult explainswhy strictly stable linear multistep methods have the same long-time behaviour as one-step methods.

Inthecontext of“geometric numerical integration”weare mainly interested in symplectic and/or symmetric methodswhich,for linear problems,are characterized by the condition $\zeta _ { 1 } ( - z ) \zeta _ { 1 } ( z ) \equiv 1$ (seeSect.VI.4.2).This,however,is only possible forsymmetric multistep methods(Exercise1）which cannot be strictly stable.

# XV.2.2Formal Analysis forWeaklyStableMethods

Theproof and the statement of Theorem2.1 break down as soon asat least one root of $\rho ( \zeta )$ ,different from1,hasmodulus one.Moreover,Example2.2 shows that we cannot expectaproperty like（2.3）with $\rho < 1$ Allwecan hopeforisto find an underlyingone-stepmethod asa formal series in $h$ Surprisingly,this providesalot ofinsight into the long-timedynamics ofweakly stable multistep methods.

Theorem2.4.Considera linearmultistepmethod(1.1),andassume that $\zeta = 1$ is asinglerootof $\rho ( \zeta ) = 0$ .Thenthereexistsauniqueformal expansion

$$
\bar { \phi } _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + \ldots .
$$

suchthat

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } \varPhi _ { h } ^ { j } ( y ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f \bigl ( \varPhi _ { h } ^ { j } ( y ) \bigr ) ,
$$

whereidentity isunderstood inthe sense offormal powerseries in $h$

If themultistepmethod is oforder $T$ ,thenalsotheunderlyingone-stepmethod isoforder $r$ ,i.e., $\varPhi _ { h } ( y ) - \varphi _ { h } ( y ) = \mathcal { O } ( h ^ { r + 1 } ) ,$

The formal series for $\varPhi _ { h } ( y )$ is called“step-transition operator”in the Chinese literature(seee.g.,Feng(1995),page274).Wecall it“underlying one-stepmethod". Notice that this theoremdoes not requireany stability assumption.

Proof.Expanding $ { \varPhi } _ { h } ^ { \ j } ( y )$ and $f \left( \varPhi _ { h } ^ { \jmath } ( y ) \right)$ into powers of $h$ ,a comparison of thecoefficientsyields

$$
\begin{array} { r l } & { \rho ^ { \prime } ( 1 ) d _ { 1 } ( y ) \ = \ \sigma ( 1 ) f ( y ) } \\ & { \rho ^ { \prime } ( 1 ) d _ { 2 } ( y ) \ = \ - \frac { \rho ^ { \prime \prime } ( 1 ) } { 2 } d _ { 1 } ^ { \prime } ( y ) d _ { 1 } ( y ) + \sigma ^ { \prime } ( 1 ) f ^ { \prime } ( y ) d _ { 1 } ( y ) } \\ & { \rho ^ { \prime } ( 1 ) d _ { j } ( y ) \ = \ \dots , } \end{array}
$$

where the three dots represent known functions depending on derivatives of $f ( y )$ and on $d _ { i } ( y )$ with $i < j$ Since $\rho ^ { \prime } ( 1 ) \neq 0$ byassumption,unique coefficient functionsd;（y）are obtained recursively.The statement on the order follows fromthe fact that the exact flow $\varphi _ { h } ( y )$ hasadefect $\mathcal { O } ( h ^ { r + 1 } )$ in the multistep formula. □

Thecomputation of the previous proof shows that the series (2.4) isa B-series. This follows rigorously from the results of Sect.II.1.4.Whereas the B-series representation of Runge-Kutta methods converges for sufficiently small $h$ ,thisisin general not the case for(2.4);see the next example.

Example2.5.Considera consistent two-step method

$$
\alpha _ { 2 } y _ { n + 2 } + \alpha _ { 1 } y _ { n + 1 } + \alpha _ { 0 } y _ { n } = h \big ( \beta _ { 2 } f _ { n + 2 } + \beta _ { 1 } f _ { n + 1 } + \beta _ { 0 } f _ { n } \big ) ,
$$

andapply itto thesimple system $\dot { y } = f ( t ) , \dot { t } = 1 .$ The $y$ -component of the underlying one-step method then takesthe form

$$
\varPhi _ { h } ( t _ { 0 } , y _ { 0 } ) = y _ { 0 } + \sum _ { j \geq 1 } h ^ { j } a _ { j } f ^ { ( j - 1 ) } ( t _ { 0 } ) .
$$

Putting $f ( t ) = e ^ { t }$ yields

$$
A ( \zeta ) = \sum _ { j \geq 1 } a _ { j } \zeta ^ { j - 1 } = \frac { \beta _ { 2 } e ^ { 2 \zeta } + \beta _ { 1 } e ^ { \zeta } + \beta _ { 0 } } { \alpha _ { 2 } ( 1 + e ^ { \zeta } ) + \alpha _ { 1 } } .
$$

for the generating function of the coefficients $a _ { j }$ Sincethis function has finite poles, theradius of convergence of $A ( \zeta )$ isfinite.Therefore,the radius of convergence ofthe series (2.6) has to be zero as soon as $f ^ { ( j ) } ( t _ { 0 } )$ behaves like $j ! \mu \kappa ^ { \mathcal { I } }$ （thisis typically thecase foranalytic functions).Independent of the fact whether themethod is strictly stable or not,the series (2.6) usually does not converge.

Both,Theorem 2.1 and Theorem 2.4,extend ina straightforward manner to partitioned multistep methods(1.14).To get analogous results for multistep methods (1.8)for second order differential equations,one has to introduce an approximation forthe velocity $v = { \dot { y } } .$ Thiswillbeexplained inmoredetail in Sect.XV.3below.

# XV.3Backward Error Analysis

Thebackward error analysis for multistep methods (Hairer 1999) is presented in two steps:

·for“smooth”numerical solutions (obtained by the underlying one-step method);   
·for the general case.

Theidealized situation of no parasitic terms gives already much insight into conservationproperties of the method (see Sect.XV.4).The study of the general case is, however,necessary for getting estimates for the parasitic solutions(Sect.XV.5）,so thatrigorous statements on the long-time behaviour are possible.

# XV.3.1 Modified Equation for Smooth Numerical Solutions

Theformal backward erroranalysis ofChap.IX couldbe directlyapplied to the underlying one-stepmethod ofSect.XV.2.2.However,due to thenon-convergenceof the series for $\varPhi _ { h } ( y )$ ,difficulties may ariseas soon as rigorous estimates are desired. Weprefer to derive the modified differential equationdirectly from the multistep formula and thus avoid the use of the underlying one-step method.

Theorem 3.1.Considera linear multistepmethod(1.1),andassumethat $\rho ( 1 ) = 0$ and $\rho ^ { \prime } ( 1 ) = \sigma ( 1 ) \neq 0$ Then there exist unique $h$ -independentfunctions $f _ { j } ( y )$ such that,forevery truncationindex $N$ ,every solution of

$$
\dot { y } = f ( y ) + h f _ { 2 } ( y ) + h ^ { 2 } f _ { 3 } ( y ) + \ldots + h ^ { N - 1 } f _ { N } ( y )
$$

satisfies

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y ( t + j h ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f { \big ( } y ( t + j h ) { \big ) } + { \mathcal O } ( h ^ { N + 1 } ) .
$$

If themultistepmethodisoforder $r$ ,then $f _ { j } ( y ) = 0 f o r 2 \leq j \leq r .$ If themethod is symmetric,then $f _ { j } ( y ) = 0$ forall even $j$ ,sothat themodifiedequation(3.1) hasan expansion in even powers of $h$

Proof.Using theLiederivative $( D _ { i } g ) ( y ) = g ^ { \prime } ( y ) f _ { i } ( y )$ (with $f _ { 1 } ( y ) = f ( y ) )$ and $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + . . . ,$ thesolutionof(3.1）withinitial value $y ( t ) = y$ satisfies $y ( t + j h ) = e ^ { j h D } y + \mathcal O ( h ^ { N + 1 } )$ and $f ( y ( t + j h ) ) = e ^ { j h D } f ( y ) + { \mathcal { O } } ( h ^ { N + 1 } )$ (by Taylor expansion).We thus have

$$
\rho ( e ^ { h D } ) y = h \sigma ( e ^ { h D } ) f ( y ) + \mathcal { O } ( h ^ { N + 1 } ) .
$$

With the expansion $x \sigma ( e ^ { x } ) / \rho ( e ^ { x } ) = 1 + \mu _ { 1 } x + \mu _ { 2 } x ^ { 2 } + . . .$ this becomes

$$
\dot { y } = ( 1 + \mu _ { 1 } h D + \mu _ { 2 } h ^ { 2 } D ^ { 2 } + . . . ) f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

A comparison with (3.1) yields $f _ { 1 } ( y ) = f ( y )$ ,and

$$
f _ { j } ( y ) = \sum _ { l \geq 1 } \mu _ { l } \sum _ { j _ { 1 } + \ldots + j _ { l } = j - 1 } \left( D _ { j _ { 1 } } \ldots D _ { j _ { l } } f \right) ( y )
$$

for $j \geq 2$ ,whichuniquelydefines the functions $f _ { j } ( y )$ in a recursive manner.

Lemma 3.2. If $f ( y )$ is analyticandbounded by $M$ in $B _ { R } ( y _ { 0 } )$ ,thenwe have

$$
\left\| f _ { j } ( y ) \right\| \leq \mu M \bigg ( \frac { \eta M j } { R } \bigg ) ^ { j - 1 } \qquad f o r \qquad \| y - y _ { 0 } \| \leq R / 2 ,
$$

where $\mu$ and $\eta$ depend only onthecoefficients $\alpha _ { j } , \beta _ { j }$ ofthemultistep method.

Proof.The estimate(3.6)isobtained asintheproofof TheoremIX.7.5.We just sketch the main idea in the notation used there.With $\delta = R / ( 2 ( J - 1 ) )$ wehave $\| f _ { j } \| _ { j } \le \delta b _ { j }$ ,where the generating function $\begin{array} { r } { b ( \zeta ) = \sum _ { j \geq 1 } b _ { j } \zeta ^ { j } } \end{array}$ of the $b _ { j }$ satisfies

$$
b ( \zeta ) = \frac { M \zeta } { \delta } \Big ( 1 + \sum _ { l \geq 1 } | \mu _ { l } | \ : b ( \zeta ) ^ { l } \Big ) .
$$

By the implicit function theorem, $b ( \zeta )$ isanalyticand boundedinadiscof radius $c \delta / M$ centred at the origin（ $c$ isapositive constant depending only on the coefficients of themultistepmethod).The estimate (3.6) then follows from Cauchy's inequalitiesasin theproof of Theorem IX.7.5. □

Itisremarkable that,although the Taylor series of the underlying one-step method generally diverges,the coefficient functions of themodifieddifferential equation satisfy the same estimate asfor Runge-Kutta methods.This enablesus toproveananalogue of Theorem IX.7.6which,for one-stepmethods,isthe main ingredient for exponentially small error estimates.One can prove that for suitably chosen $N = N ( h )$ and for $h \leq h _ { 0 } / 4$ with $h _ { 0 } = R / ( e \eta M )$ ,the solution of (3.1) satisfies

$$
\Big | \Big | \sum _ { j = 0 } ^ { k } \alpha _ { j } y ( t + j h ) - h \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( y ( t + j h ) \big ) \Big | \Big | \leq h \gamma M e ^ { - h _ { 0 } / h } ,
$$

where $\gamma$ depends only on the multistep formula.Theproof of thisstatement is similartothat ofTheoremIX.7.6.Weskipdetailsand referto Hairer(1999).

Forstrictly stable multistepmethods,Theorem 2.1 together with the Invariant Manifold Theorem XII.3.2 thusimply that theunderlyingone-stepmethod is exponentially close to the exact solution of the truncated modified equation.The parasitic solution terms are rapidly damped out by the property(2.3) of asymptoticphase.The sameconclusions as for one-step methods can therefore be drawn.

Forsymmetric methods the situation is not so simple.One has to study the parasitic solution components to get information on the long-time behaviour of the numerical solution of(1.1). The basic techniqueswill be prepared in Sect.XV.3.2.

Partitioned MultistepMethods.The extension of the modified differential equation tomethods(1.14) is straightforward.There exist functions $f _ { j } ( y , v )$ and $g _ { j } ( y , v )$ such that the exact solution of

$$
\begin{array} { l } { { \dot { y } = f ( y , v ) + h f _ { 2 } ( y , v ) + . . . + h ^ { N - 1 } f _ { N } ( y , v ) } } \\ { { \dot { v } = g ( y , v ) + h g _ { 2 } ( y , v ) + . . . + h ^ { N - 1 } g _ { N } ( y , v ) } } \end{array}
$$

satisfies the multistep formula(1.14)uptoadefect of size ${ \mathcal { O } } ( h ^ { N + 1 } ) .$ The coefficient functions can be computed by comparing（3.7）to

$$
\begin{array} { l } { { \dot { y } = ( 1 + \mu _ { 1 } ^ { ( A ) } h D + \mu _ { 2 } ^ { ( A ) } h ^ { 2 } D ^ { 2 } + . . . . ) f ( y , v ) + \mathcal { O } ( h ^ { N } ) } } \\ { { \dot { v } = ( 1 + \mu _ { 1 } ^ { ( B ) } h D + \mu _ { 2 } ^ { ( B ) } h ^ { 2 } D ^ { 2 } + . . . ) g ( y , v ) + \mathcal { O } ( h ^ { N } ) , } } \end{array}
$$

where the real numbers $\mu _ { j } ^ { ( A ) }$ and $\mu _ { j } ^ { ( B ) }$ are given by $x \sigma ^ { ( A ) } ( e ^ { x } ) / \rho ^ { ( A ) } ( e ^ { x } ) = 1 +$ $\mu _ { 1 } ^ { ( A ) } x + \mu _ { 2 } ^ { ( A ) } x ^ { 2 } + \ldots$ and by $x \sigma ^ { ( B ) } ( e ^ { x } ) / \rho ^ { ( B ) } ( e ^ { x } ) = 1 + \mu _ { 1 } ^ { ( B ) } x + \mu _ { 2 } ^ { ( B ) } x ^ { 2 } + . . . ,$ , respectively.The Lie operator is defined by $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + . . . ,$ where $( D _ { j } \psi ) ( y , v ) = \varPsi _ { y } ( y , v ) f _ { j } ( y , v ) + \varPsi _ { z } ( y , v ) g _ { j } ( y , v )$ ,and itcorresponds tothe time derivative of solutions of(3.7).

Multistep Methods for Second Order Differential Equations.The method(1.8) for differential equations $\ddot { y } = f ( y )$ canbe treatedina similarway.In the absence ofderivative approximations we get a modified differential equation of the second order

$$
\ddot { y } = f ( y ) + h f _ { 2 } ( y , \dot { y } ) + \ldots + h ^ { N - 1 } f _ { N } ( y , \dot { y } ) ,
$$

where the perturbation terms also depend on $\dot { y } .$ Its exact solution satisfies the multisteprelation（1.8）up toa defect of size $\mathcal { O } ( h ^ { N + 2 } )$ ,if（3.9)is equivalent to

$$
\ddot { y } = ( 1 + \mu _ { 1 } h D + \mu _ { 2 } h ^ { 2 } D ^ { 2 } + \ldots ) f ( y ) + \mathcal { O } ( h ^ { N } ) ,
$$

where $x ^ { 2 } \sigma ( e ^ { x } ) / \rho ( e ^ { x } ) ~ = ~ 1 + \mu _ { 1 } x + \mu _ { 2 } x ^ { 2 } + . . . .$ ,andthe timederivativeis given by the Lie operator $D = D _ { 1 } + h D _ { 2 } + h ^ { 2 } D _ { 3 } + \ldots$ with $( D _ { 1 } \varPsi ) ( y , \dot { y } ) =$ $\varPsi _ { y } ( y , \dot { y } ) \dot { y } + \varPsi _ { \dot { y } } ( y , \dot { y } ) f ( y )$ and $( D _ { j } \varPsi ) ( y , \dot { y } ) = \varPsi _ { \dot { y } } ( y , \dot { y } ) f _ { j } ( y , \dot { y } )$ for $j \geq 2 .$ Acomparison of equal powers of $h$ in(3.9）and(3.1O) uniquelydefines the coefficient functions $f _ { j } ( y , \dot { y } )$ .

Ifthemultistep method(1.8) is complemented witha difference formula for approximations of the derivative $v = \dot { y }$ at grid points,

$$
v _ { n } = \frac { 1 } { h } \sum _ { j = - l } ^ { l } \delta _ { j } y _ { n + j } ,
$$

we get an additional modified differential equation

$$
v = ( 1 + \nu _ { 1 } h D + \nu _ { 2 } h ^ { 2 } D ^ { 2 } + \ldots ) \dot { y } .
$$

The coefficients $\nu _ { j }$ are given by $x ^ { - 1 } \delta ( e ^ { x } ) = 1 + \nu _ { 1 } x + \nu _ { 2 } x ^ { 2 } + . . . .$ where $\begin{array} { r } { \delta ( \zeta ) = \sum _ { j = - l } ^ { l } \delta _ { j } \zeta ^ { j } . } \end{array}$ For given $y$ ,thisrelationgivesaformalonetoonecorrespon dence between $\upsilon$ and $\dot { y }$ Consequently,thedifferential equation(3.1O）combined with(3.12)can beconsidered asafirst order differential system for thevariables $y$ and $\boldsymbol { U }$ .

# XV.3.2 Parasitic Modified Equations

In practice,due to the necessity of starting approximations $y _ { 1 } , \ldots , y _ { k - 1 }$ ,the numerical solution of amultistep method does not lie onasolution of(3.1).Formethods, where initial perturbations are not damped out sufciently fast (cf.property (2.3) ofasymptotic phase),an additional investigation is therefore needed for the study of the propagation of perturbations in the starting approximations.Letus start with twoillustrating numerical experiments.

Example 3.3.Consider the explicit,linear 3-step method

$$
y _ { n + 3 } - y _ { n + 2 } + y _ { n + 1 } - y _ { n } = h ( f _ { n + 2 } + f _ { n + 1 } ) ,
$$

with characteristic polynomial $\rho ( \zeta ) = ( \zeta - 1 ) ( \zeta ^ { 2 } + 1 )$ ,and apply it to thependulum equation (I.1.13).Fora better illustration of the propagation of errorswe consider starting approximations $y _ { 1 } , y _ { 2 }$ that arerather far from the exact solution passing through $y _ { 0 }$ Theresult is shown in Fig.3.1.Weobserve that the numerical solution doesnot lie on one smooth curve,but on four curves,and every fourth solution approximation is on the same curve.

![](images/c3e74e9b790d2621f1b38448375957f316fc511fc776443357ff628cc4151c64.jpg)  
Fig.3.1.Numerical solution of(3.13)applied to thependulumequation.The initial approximations $y _ { 0 } = ( 1 . 9 , 0 . 4 )$ , $y _ { 1 } = ( 1 . 7 , 0 . 2 )$ , $y _ { 2 } = ( 2 . 1 , 0 )$ areindicated by black bullets;the solution points $y _ { 3 } , y _ { 7 } , y _ { 1 1 } , \dots$ ingrey

![](images/457ad2b00ca1d668ecce1a0fca42847b94f00ae1a5a8774408a2113de94e6f51.jpg)  
Fig.3.2.Numerical solution of the explicit midpoint rule(3.14） applied to thependulum equation.The initial approximations $y _ { 0 } = ( 1 . 9 , 0 . 4 )$ , $y _ { 1 } = ( 1 . 7 , 0 . 2 )$ areindicated by black bullets;the solution points $y _ { 2 } , y _ { 4 } , y _ { 6 } , \ldots$ in grey

Thisexample shows an unexpected good long-time behaviour.Although the startingapproximationsare farfromasmooth solution,the distanceof the numerical approximations toa smooth solution curve does not increase.This is,however, not the typical situation as can be seen from our next experiment.

Example 3.4.We consider the explicit midpoint rule

$$
y _ { n + 2 } - y _ { n } = 2 h f _ { n + 1 } ,
$$

which has $\rho ( \zeta ) = ( \zeta - 1 ) ( \zeta + 1 )$ ascharacteristic polynomial.This time,the numerical solution(see Fig.3.2)lies ontwosmooth curves.Incontrast to theprevious example,anunacceptable linear growth ofthe perturbationscan be observed.

Tobeable to explain this behaviour of the multistep solutions,we complement theanalysis of the modified equation for smooth numerical solutionswith so-called parasiticmodified equations.This theory has been developedbyHairer(1999) for first order differential equations,and extended to second order systems byHairer& Lubich(2004).

Consider a stable,symmetric multistepmethod(1.1） and denote the zeros of its characteristic polynomial $\rho ( \zeta )$ by $\zeta _ { 1 } = 1$ （principal root） and $\zeta _ { 2 } , \ldots , \zeta _ { k }$ (parasitic roots).We then enumerate the set of all finite products,

$$
\left\{ \zeta _ { \ell } \right\} _ { \ell \in \mathcal { T } } = \Big \{ \zeta = \zeta _ { 1 } ^ { m _ { 1 } } \cdot . . . . \cdot \zeta _ { k } ^ { m _ { k } } ; m _ { j } \geq 0 \Big \} = \big \{ \zeta _ { 1 } , . . . , \zeta _ { k } , \zeta _ { k + 1 } , . . . , \big \} ,
$$

Itis $\{ 1 , i , - i , - 1 \}$ formethod(3.13）and $\{ 1 , - 1 \}$ for the explicit midpoint rule (3.14).The set of subscripts $\mathcal { L }$ can be finite or infinite.We let $\mathcal { Z } ^ { \ast } = \mathcal { I } \backslash \{ 1 \}$ ,and we denote by $\mathcal { T } _ { N } ^ { * }$ and $\mathcal { I } _ { N }$ thefinite subsets of elements which,in the representation (3.15),have $\sum _ { j } m _ { j } < N$ .

Motivated by the previous examplesand by representations of the asymptotic expansion of the global error ofweakly stable multistep methods (see for example Sect.III.9ofHairer,Nprsett&Wanner,1993),we aimatwriting the general solution $y _ { n }$ of themultistep method(1.1）in the form

$$
y _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h ) ,
$$

where $y ( t )$ and $z _ { \ell } ( t )$ aresmooth functions (with derivatives bounded independently of $h$ ).The followingresult extends Theorem 3.1.

Theorem3.5.Considera stable,consistent,and symmetric multistepmethod(1.1). Forevery truncation index $ { N _ { \mathrm { ~ \scriptsize ~ \geq ~ 2 ~ } } }$ ，therethenexist $h$ -independentfunctions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ with $\mathbf { z } ^ { \ast } = ( z _ { \ell } ) _ { \ell = 2 } ^ { k }$ such that for every solution of

$$
\begin{array} { r l r } & { \dot { y } = f _ { 1 , 1 } ( y , \mathbf { z } ^ { * } ) + h f _ { 1 , 2 } ( y , \mathbf { z } ^ { * } ) + . . . . + h ^ { N - 1 } f _ { 1 , N } ( y , \mathbf { z } ^ { * } ) } \\ & { \dot { z } _ { \ell } = f _ { \ell , 1 } ( y , \mathbf { z } ^ { * } ) + h f _ { \ell , 2 } ( y , \mathbf { z } ^ { * } ) + . . . . + h ^ { N - 1 } f _ { \ell , N } ( y , \mathbf { z } ^ { * } ) } & { f o r ~ 2 \le \ell \le k } \\ & { z _ { \ell } = h f _ { \ell , 2 } ( y , \mathbf { z } ^ { * } ) + . . . + h ^ { N } f _ { \ell , N + 1 } ( y , \mathbf { z } ^ { * } ) } & { f o r ~ \bar { \ell } > k } \\ & { z _ { \ell } = 0 ~ f o r ~ \ell \notin \mathcal { T } _ { N } } \end{array}
$$

with initial values $z _ { \ell } ( 0 ) = \mathcal { O } ( h ) f o r 2 \leq \ell \leq k ,$ thefunction

$$
x ( t ) = y ( t ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { t / h } z _ { \ell } ( t )
$$

satisfies

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) = h \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) + { \cal O } ( h ^ { N + 1 } ) .
$$

For $\mathbf { z } ^ { * } = 0$ thedifferential equationfor $y$ isthesameasthatofTheorem3.1.The solutions of(3.17) satisfy $z _ { \ell } ( t ) = \overline { { z _ { j } } } ( t )$ whenever $\zeta _ { \ell } = \overline { { \zeta _ { j } } }$ andthis relation holds fortheinitial values.Moreover $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 1 } )$ onboundedtimeintervalsif $\zeta _ { \ell }$ isaproduct ofno fewer than $m \geq 2$ rootsof $\rho ( \zeta )$

Proof.We let $z _ { 1 } ( t ) : = y ( t )$ and insert the finite sum(3.18)into(3.19).This yields

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) ~ = ~ \sum _ { j = 0 } ^ { k } \alpha _ { j } \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { ( t + j h ) / h } e ^ { j h D } z _ { \ell } ( t ) } } \\ { { ~ = ~ \displaystyle \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \sum _ { j = 0 } ^ { k } \alpha _ { j } \zeta _ { \ell } ^ { j } e ^ { j h D } z _ { \ell } ( t ) ~ = ~ \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } ( t ) , } } \end{array}
$$

where,asusual, $\mathcal { D }$ represents differentiation with respect to time.We then expand $f \left( \boldsymbol { x } ( t ) \right)$ intoa Taylor series around $y ( t )$ ,

$$
\begin{array} { r c l } { f ( \boldsymbol { x } ( t ) ) } & { = } & { \displaystyle \sum _ { m \ge 0 } \frac { 1 } { m ! } f ^ { ( m ) } ( \boldsymbol { y } ( t ) ) \Big ( \sum _ { \ell _ { 1 } \in \mathcal { Z } ^ { * } } \zeta _ { \ell _ { 1 } } ^ { t / h } z _ { \ell _ { 1 } } ( t ) , \ldots , \sum _ { \ell _ { m } \in \mathcal { Z } ^ { * } } \zeta _ { \ell _ { m } } ^ { t / h } z _ { \ell _ { m } } ( t ) \Big ) } \\ & { = } & { \displaystyle \sum _ { \ell \in \mathcal { T } } \zeta _ { \ell } ^ { t / h } \sum _ { m \ge 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( \boldsymbol { y } ( t ) ) \big ( z _ { \ell _ { 1 } } ( t ) , \ldots , z _ { \ell _ { m } } ( t ) \big ) . } \end{array}
$$

This gives,as above,

$$
\begin{array} { l l } { { } } & { { \displaystyle \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) } } \\ { { } } & { { = \displaystyle \sum _ { \ell \in \mathbb { Z } } \zeta _ { \ell } ^ { t / h } \sigma ( \zeta \ell e ^ { h D } ) \displaystyle \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta , \ell } f ^ { ( m ) } \big ( y ( t ) \big ) \big ( z _ { \ell _ { 1 } } ( t ) , . . . , z _ { \ell _ { m } } ( t ) \big ) . } } \end{array}
$$

Comparing coefficients of $\boldsymbol { \zeta } _ { \ell } ^ { t / h }$ for $\ell \in \mathcal { L } _ { N }$ in (3.19) thus yields

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = h \sigma ( \zeta _ { \ell } e ^ { h D } ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { { \bar { \zeta } } _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , \ldots , z _ { \ell _ { m } } )
$$

(for $\ell = 1$ and $m = 0$ the sum isunderstood to include the term $f ( y )$ ).With the expansion $x \sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } ) = \mu _ { \ell , 0 } + \mu _ { \ell , 1 } x + \mu _ { \ell , 2 } x ^ { 2 } + . . . .$ for $1 \le \ell \le k$ ,where $\zeta _ { \ell }$ isasimple root of $\rho ( \zeta )$ ,this equation becomes

$$
\dot { z } _ { \ell } = \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \tilde { \zeta } _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

and with $\sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } ) = \mu _ { \ell , 0 } + \mu _ { \ell , 1 } x + \mu _ { \ell , 2 } x ^ { 2 } + \dots .$ for $\ell > k$ ,where $\rho ( \zeta _ { \ell } ) \neq 0$ ,

$$
z _ { \ell } = h \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } , . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

Intheusual way(elimination of the first and higher derivativesby the differential equationsand by the differentiated thirdrelation of(3.17)) thisallowsus to define recursively the functions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ ,

From this construction processit follows that on bounded time intervalswe have $z _ { \ell } ( t ) = \mathcal { O } ( h )$ forall $\ell \geq 2$ ,and $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 1 } )$ if $\zeta _ { \ell }$ isa product of no fewer than $m \geq 2$ rootsof $\rho ( \zeta )$ In(3.2O)and in the above construction of the coefficient functions $f _ { \ell , j } ( y , \mathbf z ^ { * } )$ we have neglected terms that contain at least $N$ factors $z _ { j } .$ This gives rise to the $\mathcal { O } ( h ^ { N + 1 } )$ term in (3.19). □

Initial values $y ( 0 )$ ， $z _ { \ell } ( 0 ) , \ell = 2 , \ldots , k$ ,for the system(3.17)are obtained from thestarting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ via therelation

$$
y _ { j } = y ( j h ) + \sum _ { \ell \in \mathcal { T } ^ { * } } \zeta _ { \ell } ^ { j } z _ { \ell } ( j h ) , \quad j = 0 , 1 , \dots , k - \backslash 1 .
$$

For $h = 0$ thisrepresentsa linear Vandermonde system for $y ( 0 )$ , $z _ { \ell } ( 0 )$ TheImplicitFunction Theorem thus proves the local existence ofa solution of(3.24) for sufficiently small step sizes $h$ .If $y _ { j } , j = 2 , \ldots , k$ approximatea solution $y _ { e x } ( t )$ of $\dot { y } = f ( y )$ withanerror $\mathcal { O } ( h ^ { s } )$ (with $s \leq r + 1$ ,where $T$ is the order of the method), then $y ( 0 ) - y _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } )$ and $z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } )$ for $\ell = 2 , \ldots , k$ .

Therepresentation (3.16) of the numerical solution and the (principal and parasitic)modified equations (3.17)will be themain ingredients for the study of longterm stability of multistepmethods in Sect.XV.5.An extension of the previous theoremtopartitioned multistepmethodsis more or less straightforward.We leave the details asan exercise for thereader.

Multistep Methods for Second Order Differential Equations.A completely analogousresult can be proved for stable,symmetric multistepmethods(1.8)appliedto $\ddot { y } = f ( y )$ .Weagain denote the zeros of $\rho ( \zeta )$ by $\zeta _ { 1 } = 1$ and $\zeta _ { \ell } , \ell = 2 , \ldots , q$ Notice,however,that $\zeta _ { 1 } = 1$ isalwaysa double zero,and the others can be simple ordouble zeros of $\rho ( \zeta )$ ,andthat $q \leq k$ Weconsider the index sets $\mathcal { L }$ , $\boldsymbol { \mathcal { L } ^ { * } }$ , $\mathcal { I } _ { N }$ ,and $\mathcal { T } _ { N } ^ { * }$ asin (3.15).

Theorem 3.6.Consider a stable,consistent,and symmetric multistepmethod(1.8). Forevery truncation index $N \geq 2$ ，there then exist $h$ -independent functions $f _ { \ell , j } ( y , \dot { y } , \mathbf z ^ { * } )$ (where ${ \mathbf z } ^ { \ast }$ denotes the vectorcollectingas elements $z _ { \ell } , \dot { z } _ { \ell }$ if $\zeta _ { \ell }$ is $a$ doubleroot,and $z _ { \ell }$ if $\zeta _ { \ell }$ is $\alpha$ simpleroot of $\rho ( \zeta )$ )suchthat foreverysolutionof

$$
\begin{array} { l l } { \ddot { y } } & { = \ f _ { 1 , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + h f _ { 1 , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N - 1 } f _ { 1 , N } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad ( 3 . } \\ { \ddot { z } _ { \ell } } & { = \ f _ { \ell , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N - 1 } f _ { \ell , N } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad i f \ \rho ( \zeta _ { \ell } ) = \rho ^ { \prime } ( \zeta _ { \ell } ) = 0 } \\ { \dot { z } _ { \ell } } & { = \ h f _ { \ell , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N } f _ { \ell , N + 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad \ i f \ \rho ( \zeta _ { \ell } ) = 0 , \rho ^ { \prime } ( \zeta _ { \ell } ) \neq } \\ { z _ { \ell } } & { = \ h ^ { 2 } f _ { \ell , 3 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + \ldots + h ^ { N + 1 } f _ { \ell , N + 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \qquad \ i f \ \rho ( \zeta _ { \ell } ) \neq 0 } \\ { z _ { \ell } } & { = \ 0 \qquad f o r \ \ell \notin \mathcal { X } _ { N } } \end{array}
$$

with initial values $z _ { \ell } ( 0 ) = \mathcal O ( h ) f o r 2 \le \ell \le q$ thefunction

satisfies

$$
x ( t ) = y ( t ) + \sum _ { \ell \in \mathbb { Z } ^ { \star } } \zeta _ { \ell } ^ { t / h } z _ { \ell } ( t )
$$

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } x ( t + j h ) \stackrel { } { = } h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } f \big ( x ( t + j h ) \big ) + { \mathcal O } ( h ^ { N + 2 } ) .
$$

For $\mathbf { z } ^ { * } = 0$ thedifferential equation for $y$ is the same as in(3.9).The solutions of (3.25）satisfy $z _ { \ell } ( t ) = \overline { { z _ { j } } } ( t )$ whenever $\zeta _ { \ell } = \zeta _ { j }$ andthisrelationholdsfortheinitial values.Moreover, $z _ { \ell } ( t ) = \mathcal { O } ( h ^ { m + 2 } )$ on boundedtime intervalsif $\zeta _ { \ell }$ is aproduct of no fewerthan $m \geq 2$ rootsof $\rho ( \zeta )$ .

Proof.Incompleteanalogytotheproof ofTheorem3.5we obtain

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = h ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { h D } ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { { \zeta _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , . . . . , z _ { \ell _ { m } } )
$$

which differs from (3.21） only in the factor $h ^ { 2 }$ .Depending on whether $\zeta _ { \ell }$ is adouble,a simple,or nota zero of $\rho ( \zeta )$ ,weexpand $x ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } )$ or $x \sigma ( \zeta e e ^ { x } ) / \rho ( \zeta e e ^ { x } )$ or $\sigma ( \zeta _ { \ell } e ^ { x } ) / \rho ( \zeta _ { \ell } e ^ { x } )$ intoa series of powers of $x$ ,andwedenote its coefficients by $\mu _ { \ell , j } .$ This then yields

$$
\ddot { z } _ { \ell } = \Bigl ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + \ldots \Bigr ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \bigl ( z _ { \ell _ { 1 } } , \ldots , z _ { \ell _ { m } } \bigr ) ,
$$

if $\rho ( \zeta _ { \ell } ) = \rho ^ { \prime } ( \zeta _ { \ell } ) = 0$ ,but $\rho ^ { \prime \prime } ( \zeta _ { \ell } ) \neq 0$ (in particular for $\ell = 1$ and $\zeta _ { 1 } = 1$ ）,

$$
\dot { z } _ { \ell } = h \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } , . . . \zeta _ { r _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) \big ( z _ { \ell _ { 1 } } , . . . , z _ { \ell _ { m } } \big ) ,
$$

if $\rho ( \zeta _ { \ell } ) = 0$ ,but $\rho ^ { \prime } ( \zeta _ { \ell } ) \neq 0$ ,and

$$
z _ { \ell } = \bar { h } ^ { 2 } \Big ( \mu _ { \ell , 0 } + \mu _ { \ell , 1 } h D + . . . \Big ) \sum _ { m \geq 0 } \frac { 1 } { m ! } \sum _ { \zeta _ { \ell _ { 1 } } . . . \zeta _ { \ell _ { m } } = \zeta _ { \ell } } f ^ { ( m ) } ( y ) ( z _ { \ell _ { 1 } } , . . . . , z _ { \ell _ { m } } \Big ) ,
$$

if $\rho ( \zeta _ { \ell } ) \neq 0 ,$ Therest of the proof is identical to that of Theorem 3.5.

For the system of modified equations(3.25）we need initial values $y ( 0 ) , \dot { y } ( 0 )$ , $z _ { \ell } ( 0 ) , \dot { z } _ { \ell } ( 0 )$ if $\zeta _ { \ell }$ isa double root of $\rho ( \zeta )$ ,and $z _ { \ell } ( 0 )$ if $\zeta _ { \ell }$ isa simpleroot.These initial values can be obtained from the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ via the relation (3.24）.

Lemma 3.7.Considera stable,symmetricmultistepmethod(1.8) oforder $r$ and let the starting approximations $y _ { 0 } , \ldots , y _ { k - 1 }$ satisfy $y _ { j } - y _ { e x } ( j h ) = \mathcal { O } ( h ^ { s } )$ with $2 \leq s \leq r + 2$ .Thenthereexist(locally)unique initial values for thesystem(3.25) such that its solution exactly satisfies(3.24).

These initial values satisfy $z _ { \ell } ( 0 ) = { \overline { { z _ { j } } } } ( 0 )$ if $\zeta _ { \ell } = \zeta _ { j }$ and

$$
\begin{array} { r l } & { y ( 0 ) - y _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \quad h \dot { y } ( 0 ) - h \dot { y } _ { e x } ( 0 ) = \mathcal { O } ( h ^ { s } ) , } \\ & { z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \quad h \dot { z } _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) \qquad i f \zeta _ { \ell } i s a d o u b l e r o o t , } \\ & { z _ { \ell } ( 0 ) = \mathcal { O } ( h ^ { s } ) , \qquad i f \zeta _ { \ell } i s a s i m p l e r o o t . } \end{array}
$$

ProofWe scale the derivatives by $h$ ,andconsider $y ( 0 )$ , $h \dot { y } ( 0 )$ , $z _ { \ell } ( 0 )$ and $h z _ { \ell } ( 0 )$ as unknowns in the system (3.24),where $y ( t )$ and $z _ { \ell } ( t )$ areasolution of(3.25）.For $h = 0$ alinear,confluent Vandermondesystemis obtained.Sincethisisaninvertible matrix,the Implicit Function Theorem provesthe statement. □

# XV.4 CanMultistep Methods be Symplectic?

Readers might beastonished to find aquestion mark in the title.Thereason is that we shall present two definitions of symplecticity ofmultistep methods applied toa Hamiltonian system

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q ) .
$$

Oneworks in thephase space of the exact flow,the other ina higher dimensional space.But which one is suitable?We further show that certain multistep methods canpreserve energy overlong times,even if they are not symplectic.

# XV.4.1 Non-Symplecticity of the Underlying One-Step Method

A conjecture due to FengKang.

(Y.-F.Tang 1993)

Anatural definition of symplecticity consists of the requirement that the underlying one-step method(Theorem2.4)be symplectic.Thismeans that the (truncated) modified equation(3.1） isHamiltonian.Unfortunately,we havethe followingnegative result.

Theorem4.1 (Tang1993).Theunderlyingone-stepmethodofa consistent linear multistepmethod(1.1) cannotbesymplectic.

Proof.We show that the firstperturbation term in the modified equation (3.1) is in general not Hamiltonian.From(3.4）weknow that $f _ { r + 1 } ( y ) = \mu _ { r } ( D _ { 1 } ^ { r } f ) ( y )$ which (omitting the non-zero error constant $\mu _ { r }$ ）isgiven by

$$
\sum _ { \tau \in T , | \tau | = r + 1 } \alpha ( \tau ) F ( \tau ) ( y ) = | \tau | ! \sum _ { \tau \in T , | \tau | = r + 1 } \frac { 1 } { \sigma ( \tau ) } b ( \tau ) F ( \tau ) ( y )
$$

with $b ( \tau ) = 1 / \gamma ( \tau )$ for $| \tau | = r + 1$ (Theorem III.1.3 and(III.1.27)).Suppose nowthat(4.2) is Hamiltonian forall separable Hamiltonian vector fields $f ( y ) =$ $J ^ { - 1 } \nabla H ( y )$ TheoremIX.10.4 then implies

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \qquad { \mathrm { f o r ~ a l l ~ } } u , v \in T { \mathrm { ~ w i t h ~ } } | u | + | v | = r + 1 .
$$

This,however,isin contradiction with

$$
\frac { 1 } { \gamma ( u \circ v ) } + \frac { 1 } { \gamma ( v \circ u ) } = \frac { 1 } { \gamma ( u ) } \cdot \frac { 1 } { \gamma ( v ) } ,
$$

which isa consequence of TheoremVI.7.6(because the exact solution isa symplectictransformationand,asaB-series,hascoefficients $a ( \tau ) = 1 / \gamma ( \tau ) )$ . □

Asimilarnegativeresult holdsfora much largerclass of integrationmethods. Forexample,itisproved by Hairer&Leone（1998)that,amongtheclassofonelegmethods(see(4.7) below）,only the implicit mid-point rule issymplectic(in the sense that the underlying one-step method is symplectic).

PartitionedLinearMultistepMethods.Weknowat least onesymplectic method ofthe form(1.14).It is thesymplectic Euler method(VI.3.1),which combines the implicit and the explicit Euler methods.However,we do not have betterwithin the class of partitioned multistep methods as is shownin the next theorem.

Theorem4.2.If theunderlying one-stepmethodofaconsistent,partitionedlinear multistepmethod(1.14) issymplecticforall separable Hamiltoniansystems,then its order satisfies $r \leq 1$

Proof.Suppose that the order of themethodis $r \geq 2$ By(3.8）,the dominant perturbation terminthemodified differential equationis $\mu _ { r } ^ { ( A ) } h ^ { r } ( D _ { 1 } ^ { r } f ) ( y , z )$ forthe $y$ -component and $\mu _ { r } ^ { ( B ) } h ^ { r } ( D _ { 1 } ^ { r } g ) ( y , z )$ for the $z$ component (atleastoneoftheco efficients $\mu _ { r } ^ { ( A ) } / \gamma ( \tau )$ $\mu _ { r } ^ { ( A ) }$ $\tau \in T P _ { p } , | \tau | = r + 1$ and $\mu _ { r } ^ { ( B ) }$ is non-zero).ThisisaP-serieswithcoeficients and $b ( \tau ) = \mu _ { r } ^ { ( B ) } / \gamma ( \tau )$ if $\tau \in T P _ { q } , | \tau | = r + 1$ $b ( \tau ) =$ If theunderlying one-stepmethod is symplectic(i.e.,the modified differential equationislocallyHamiltonian),TheoremIX.1O.4 impliesthat

$$
b ( u \circ v ) + b ( v \circ u ) = 0 \quad \mathrm { f o r } \quad u \in T P _ { p } , v \in T P _ { q } , | u | + | v | = r + 1 .
$$

Taking for $u \in \mathcal { I } ^ { \prime } P _ { p }$ the tree with one vertex,and for $v \in \mathop { \cal { I } } { \cal { I } } { \cal { I } } _ { q } ^ { \prime }$ anarbitrary treewith $| \boldsymbol { v } | = \boldsymbol { r }$ condition(4.3)gives the first relation of

$$
\frac { \mu _ { r } ^ { ( A ) } } { ( r + 1 ) \gamma ( v ) } + \frac { \mu _ { r } ^ { ( B ) } r } { ( r + 1 ) \gamma ( v ) } = 0 , \qquad \frac { \mu _ { r } ^ { ( B ) } } { ( r + 1 ) \gamma ( v ) } + \frac { \mu _ { r } ^ { ( A ) } r } { ( r + 1 ) \gamma ( v ) } = 0 .
$$

Exchanging the colour of the vertices gives the second relation.This contradicts our assumption $r \geq 2$ . □

If we restrict our considerations to Hamiltonian systems with

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } C p + c ^ { T } p + U ( q ) ,
$$

where the kinetic energy isat most quadraticin $p$ ,wecan find symplectic,partitionedmultistepmethods oforder two.Indeed,thecombination of the trapezoidal rulewith the explicitmidpoint rule

$$
p _ { n + 1 } - p _ { n } = - \frac { h } { 2 } \Big ( \nabla U ( q _ { n + 1 } ) + \nabla U ( q _ { n } ) \Big ) , \quad q _ { n + 1 } - q _ { n - 1 } = 2 h \big ( C p _ { n } + c \big )
$$

hasthe Stormer-Verlet method asunderlying one-step method.Thisis seen as follows:since theHamiltonianis separable,formula(VI.3.4）yields thefirst formula of(4.5).The second relation is a consequence of $q _ { n + 1 } - q _ { n } + h ( C p _ { n + 1 / 2 } + c )$ and $p _ { n + 1 / 2 } + p _ { n - 1 / 2 } = 2 p _ { n }$ ,and uses the linearity of $H _ { p } ( p , q )$ .

Also for this special class of Hamiltonian systemswecannot achieve high order and symplecticity at the same time.

Theorem4.3.If the underlyingone-stepmethodofaconsistent,partitioned linear multistepmethod(1.14)issymplecticforall Hamiltoniansystemswith Hamiltonian oftheform(4.4),thenitsordersatisfies $r \leq 2$ .

Proof.Thebeginningis thesameasthat for Theorem 4.2.Welet $r \geq 2$ be the order of themethod (A)so that $\mu _ { r } ^ { ( A ) } \neq 0$ Insteadof(4.3)wenowhavetouse

$$
b ( u \circ \circ v ) - b ( v \circ \circ u ) = 0 \qquad { \mathrm { f o r } } \quad u , v \in T N _ { p } , | u | + | v | = r ,
$$

whichalso follows from Theorem IX.10.4.Takingfor $u \in T N _ { p }$ the tree with one vertex,and for $v \in \mathop { I N _ { p } }$ anarbitrary treewith $| \boldsymbol { v } | = r - 1$ ,condition （4.6） gives the relation

$$
\frac { \mu _ { r } ^ { ( A ) } ( r - 1 ) } { 2 ( r + 1 ) \gamma ( v ) } - \frac { \mu _ { r } ^ { ( A ) } } { r ( r + 1 ) \gamma ( v ) } = 0 ,
$$

which is contradictory for $r > 2$ ,because $\mu _ { r } ^ { ( A ) } \neq 0$

Remark4.4.We believethatthestatement ofTheorem4.3remainstrue,ifwe restrict our considerationto Hamiltonian functions（4.4）with $c = 0$ and invertible matrix $C$ .Sincemultistepmethods(1.8) for second orderdifferential equations can beconverted intopartitioned multistep methods,this then implies that methods（1.8) cannot be symplectic unless the order satisfies $r \leq 2$ ,

# XV.4.2 Symplecticity intheHigher-Dimensional PhaseSpace

Wepresent herea second approach for thedefinition of symplecticity of multistep methods (more precisely,of one-legmethods).It ismuch inspired by the $G$ -stability theoryofDahlquist(1975)for thestudy of stiffdifferential equations.

Tosimplify the nonlinear stability theory of linear multistep methods(1.1), Dahlquist(1975) introduced the so-called one-legmethods,which aredefined by therelation

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } y _ { n + j } \stackrel { } { = } h f \Big ( \sum _ { j = 0 } ^ { k } \beta _ { j } y _ { n + j } \Big ) ,
$$

where the normalization $\begin{array} { r } { \sigma ( 1 ) = \sum _ { j } \beta _ { j } = 1 } \end{array}$ isassumed.In fact,thereisa close relationship between thenumerical solution of（4.7）and（1.1）,and their long-time behaviour is the same(see Sect.V.6of Hairer $\&$ Wanner,1996).In the following we consider the super-vectors $Y _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ collecting $k$ consecutive approximations of the solution.

Definition 4.5.Let $G$ beaninvertible symmetric matrix of dimension $k$ A $k$ -step multistep or one-leg method is called $G$ -symplecticif

$$
Y _ { n + 1 } ^ { T } \left( G \otimes S \right) Y _ { n + 1 } = Y _ { n } ^ { T } \left( G \otimes S \right) Y _ { n } ,
$$

whenever thedifferential equation $\dot { y } = f ( y )$ has $y ^ { T } S y$ as invariant (with symmetric $S$ ),i.e.,the vectorfield satisfies $y ^ { T } S f ( y ) = 0$ forall $y$ .

Itisof course also possible to express this definition in terms ofdifferential forms.As a consequence ofLemma VI.4.1 the conservation of quadratic first integralsis equivalent to symplecticity(Bochev& Scovel 1994).

Incontrast to the negative results of Sect.XV.4.1,there exist a lot of $G$ - symplecticmethods.We have the followingresult.

Theorem4.6(Eirola&Sanz-Serna 1992).Every irreduciblesymmetric one-leg method(4.7）is $G$ -symplecticforsomematrix $G$ ,

Proof.Werecall that aone-legmethod is irreducible if thegeneratingpolynomials $\rho ( \zeta )$ and $\sigma ( \zeta )$ have no common zeros.

Construction of $G$ .Thesymmetry relation (1.3) implies $\rho ( 1 / \zeta ) = - \zeta ^ { - k } \rho ( \zeta )$ and $\sigma ( 1 / \zeta ) = \zeta ^ { - k } \sigma ( \zeta )$ Consequently,thepolynomial $\rho ( \zeta ) \sigma ( \omega ) + \rho ( \omega ) \sigma ( \zeta )$ vanishes for $\omega = 1 / \zeta$ ,and contains the factor $\zeta \omega - 1$ We thendefine $G$ by

$$
\frac { 1 } { 2 } \big ( \rho ( \zeta ) \sigma ( \omega ) + \rho ( \omega ) \sigma ( \zeta ) \big ) = ( \zeta \omega - 1 ) \sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { i - 1 } \omega ^ { j - 1 } .
$$

The matrix $G$ obtained in this way is symmetric.

Regularity of $G$ .Applying the geometric seriesweget

$$
\sum _ { i , j = 1 } ^ { k } g _ { i j } \zeta ^ { i - 1 } \omega ^ { j - 1 } = - \frac { 1 } { 2 } \big ( \rho ( \zeta ) \sigma ( \omega ) \mp \rho ( \omega ) \sigma ( \zeta ) \big ) \big ( 1 + \zeta \omega + \zeta ^ { 2 } \omega ^ { 2 } + . . . . \big ) ,
$$

wherethe identity holds as formal power series.Suppose that thematrix $G$ isnot invertible.Then there existsa vector $u = ( u _ { 0 } , u _ { 1 } , \ldots , u _ { k - 1 } ) ^ { T }$ suchthat $G u =$ 0.Weformallyreplace the appearances of $\omega ^ { \mathcal { I } - 1 }$ with $u _ { j - 1 }$ for $j \ \leq \ k$ andwith zerofor $j > k .$ This gives an identity of the form $0 = \rho ( \zeta ) a ( \zeta ) + \sigma ( \zeta ) b ( \zeta )$ with polynomials $a ( \zeta )$ and $b ( \zeta )$ of degree at most $k - 1$ ,and we get a contradiction with the irreducibility of the method.

$G$ -Symplecticity.Wenextreplacein(4.9) $S ^ { i _ { \omega } , j }$ with $y _ { n + i } ^ { T } S y _ { n + j } .$ Together with （4.7） thisyields

$$
h \Bigl ( \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } \Bigr ) ^ { T } S f \Bigl ( \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n + i } \Bigr ) = Y _ { n + 1 } ^ { T } ( G \otimes S ) Y _ { n + 1 } - Y _ { n } ^ { T } ( G \otimes S ) Y _ { n } ,
$$

where $Y _ { n } = ( y _ { n } , \dots , y _ { n + k - 1 } ) ^ { T } .$ This proves (4.8)for all functions $f ( y )$ satisfying $y ^ { T } S f ( y ) = 0$ □

Example 4.7.We consider the explicit midpoint rule(1.6),which is alsoa one-leg method,andthe3-stepmethod(3.13).By Theorem 4.6the one-legversionsare $G$ -symplectic.Following the constructive proof of this theorem we find

$$
G = { \left( \begin{array} { l l } { 0 } & { 1 } \\ { 1 } & { 0 } \end{array} \right) } \qquad { \mathrm { a n d } } \qquad G = { \left( \begin{array} { l l l } { 0 } & { 1 } & { 1 } \\ { 1 } & { - 2 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right) } \ ,
$$

respectively.We apply both methodsto twoclosely related Hamiltoniansystems, namely the pendulum equation with $H ( p , q ) = p ^ { 2 } / 2 - \cos q$ and aperturbed problemwith $H ( p , q ) = p ^ { 2 } / 2 - \cos q ( 1 - p / 6 )$ ,and we study the preservation of the

![](images/e90f4b15b808b690bf78b42692d6084f3cc2664e4541a37a36de064d268d2c7d.jpg)  
Fig.4.1.Numerical Hamiltonian $H ( p _ { n } , q _ { n } ) - H ( p _ { 0 } , q _ { 0 } )$ of the explicit mid-pointruleand the 3-stepmethod(3.13),applied withstepsize $h = 0 . 0 1$ tothe pendulum problem $\quad ( H ( p , q ) =$ $p ^ { 2 } / 2 - \cos q )$ and toaperturbed problem $( H ( p , q ) = p ^ { 2 } / 2 - \cos q ( 1 - \stackrel { \triangledown } { p } / 6 ) )$ ontheinterval $[ 0 , 1 1 0 0 ]$ (only every 131st stepis drawn)

Hamiltonian (see Fig.4.1).The result is somewhat surprising.The midpoint rule behaveswellfor theperturbed problem,but showsa linearerror growth in the Hamiltonian for thependulumproblem.Onthe other side,theweakly stable 3-stepmethod behaveswell for thependulum equation (which is in agreement with the stable behaviour ofFig.3.1),but hasan exponential error growth for the perturbed problem. Notice that different scalesare used in the four pictures.

Theabove example illustrates that $G$ -symplecticity ofanumerical methodis notsufficient fora good long-time behaviour.Itis necessary to getunder control the parasitic solution components.

# XV.4.3Modified Hamiltonian of Multistep Methods

After the negative results of Sect.XV.4.1,we are fortunately also able toprove positiveresults concerning the near conservation of the Hamiltonian.

Theorem4.8.Fora symmetric,consistent linearmultistep method(1.1) oforder $r$ appliedto $\begin{array} { r } { \dot { y } = J ^ { - 1 } \nabla H ( y ) } \end{array}$ ,thereexistsa seriesoftheform

$$
\widetilde H ( y ) = H ( y ) + h ^ { r } H _ { r + 1 } ( y ) + h ^ { r + 2 } H _ { r + 3 } ( y ) + \dots ,
$$

whichisaformalfirst integral of themodifiedequation(3.1)without truncation.

Proof.With $\rho ( e ^ { x } ) / ( x \sigma ( e ^ { x } ) ) = 1 + \gamma _ { r } x ^ { r } + \gamma _ { r + 2 } x ^ { r + 2 } + . . . .$ it follows from (3.3) that the solution of the modified differential equation satisfies

$$
( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \dot { y } = J ^ { - 1 } \nabla H ( y ) + \mathcal { O } ( h ^ { N } ) ,
$$

where,due to the symmetry of themethod,only odd derivatives of $y ( t )$ appear.We multiply both sideswith $\dot { y } ^ { T } J$ sothat theright-hand side becomes the total derivative $\begin{array} { r } { \frac { d } { d t } H ( y ) } \end{array}$ Ontheleft-hand sidewenote ${ \dot { y } } ^ { T } J { \dot { y } } \ = \ 0$ ， $\begin{array} { r } { \dot { y } ^ { T } J y ^ { ( 3 ) } = \frac { d } { d t } \big ( \dot { y } ^ { T } J \ddot { y } \big ) } \end{array}$ and similarly for higherderivatives

$$
\dot { y } ^ { T } J y ^ { ( 2 m + 1 ) } = \frac { d } { d t } \Bigl ( \dot { y } ^ { T } J y ^ { ( 2 m ) } - \dot { y } ^ { T } J y ^ { ( 2 m - 1 ) } + \ldots \pm y ^ { ( m ) T } J y ^ { ( m + 1 ) } \Bigr ) .
$$

Wethus obtaina time derivative of an expression inwhich the appearing derivatives can be substituted as functions of $y$ via the modified differential equation (3.1). Altogether this yields

$$
- \frac { d } { d t } \Bigl ( h ^ { r } H _ { r + 1 } ( y ) + h ^ { r + 2 } H _ { r + 3 } ( y ) + \ldots \Bigr ) = \frac { d } { d t } H ( y ) + { \cal O } ( h ^ { N } ) .
$$

which proves the statement.

The statement of the previous theorem is somewhat surprising.The underlying one-step method,although not symplectic,nearly conserves theHamiltonian for general $H ( y )$ (notevenreversibility isrequired).Thisindicatesthat thecondition (IX.9.2O)can be satisfied for all trees also by non-symplectic methods.

Forpartitioned multistep methodswe do not know of a similar resultunless if werestrict our consideration to Hamiltonians of the form (4.4).In this case we are concerned with multistep methods for second order differential equations.

Theorem4.9.Forasymmetric,consistentlinear multistepmethod(1.8)oforder $r$ appliedto $\ddot { y } = - \nabla U ( y )$ ,thereexistsa seriesoftheform

$$
\widetilde { H } ( y , \dot { y } ) = \frac { 1 } { 2 } \dot { y } ^ { T } \dot { y } + U ( y ) + h ^ { r } H _ { r + 1 } ( y , \dot { y } ) + h ^ { r + 2 } H _ { r + 3 } ( y , \dot { y } ) + \dots ,
$$

whichisaformalfirst integralofthemodifiedequation(3.9)without truncation.

Proof.Theproofisvery similarto thatoftheprevioustheorem.Weexpand $\rho ( e ^ { x } ) / ( x ^ { 2 } \sigma ( e ^ { x } ) ) = 1 + \gamma _ { r } x ^ { r } + \gamma _ { r + 2 } x ^ { r + 2 } + . . . ,$ and similar to(3.10) we obtain

$$
( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \ddot { y } = - \nabla U ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

This time we multiply both sides with ${ \dot { y } } ^ { T } .$ Theright-hand side becomes the total derivative $\begin{array} { r l } { \frac { d } { d t } { U } ( y ) } \end{array}$ and for the left-hand side we use $\begin{array} { r } { \dot { y } ^ { T } \ddot { y } = \frac { d } { d t } ( \dot { y } ^ { T } \dot { y } ) } \end{array}$ and for higher even-orderderivatives

$$
{ \dot { y } } ^ { T } y ^ { ( 2 m ) } = { \frac { d } { d t } } \Bigl ( { \dot { y } } ^ { T } y ^ { ( 2 m - 1 ) } - { \ddot { y } } ^ { T } y ^ { ( 2 m - 2 ) } + \ldots \pm { \frac { 1 } { 2 } } y ^ { ( m ) T } y ^ { ( m ) } \Bigr ) .
$$

Integrating and substituting second and higher derivatives of $_ y$ via the modified differential equation(3.9) yields the desired formal first integral close to the Hamiltonian of the system. □

The formal first integral (4.13） does not depend on how approximationsto the derivative $v = \dot { y }$ are obtained.If the derivativeat grid points is numerically computed with the formula (3.11),then one can use the one-to-one correspondence (3.12)to express the coeffcient functions of the modified differential equation in termsof $y$ and $\boldsymbol { v }$ .

# XV.4.4Modified Quadratic First Integrals

Symplectic one-step methods exactly preservequadratic first integrals(Sect.IV.2).   
Thisis not true for the underlying one-step method of symmetric multistep methods.   
However,aswe shall proveinthis section,it nearly preserves such first integrals.

Theorem4.10.Let $Q ( y ) = y ^ { T } C y$ (with $a$ symmetricmatrix $C$ )beafirst integral of $\dot { y } = f ( y )$ Forasymmetric,consistent linearmultistepmethod $( I , I )$ oforderr, therethenexistsaseriesoftheform

$$
\widetilde Q ( y ) = y ^ { T } C y + h ^ { r } Q _ { r + 1 } ( y ) + h ^ { r + 2 } Q _ { r + 3 } ( y ) + \dots ,
$$

whichisaformalfirst integralofthemodifiedequation(3.1)without truncation.

Proof.We multiply(4.11)with $y ^ { T } C$ und thus obtain

$$
y ^ { T } C ( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \dot { y } = y ^ { T } C f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

Since $y ^ { \scriptscriptstyle T } C y$ isafirst integral,the termon theright-hand side vanishes.For the terms ontheleft-handside we notice that $\begin{array} { r } { y ^ { T } C \dot { y } = \frac { 1 } { 2 } \frac { d } { d t } ( y ^ { T } C y ) } \end{array}$ and that

$$
y ^ { T } C y ^ { ( 2 m + 1 ) } = { \frac { d } { d t } } { \Big ( } y ^ { T } C y ^ { ( 2 m ) } - { \dot { y } } ^ { T } C y ^ { ( 2 m - 1 ) } + \ldots \pm { \frac { 1 } { 2 } } y ^ { ( m ) T } C y ^ { ( m ) } { \Big ) } .
$$

Asin the proofs of Sect.XV.4.3 we now deduce the statement.

Asimilarresult holds for second orderdifferential equationsand methods(1.8). Thisconcerns for example the total angular momentum in $N$ -bodysystems.

Theorem4.11.Supposethat $\ddot { y } = f ( y )$ has $L ( y , \dot { y } ) = y ^ { T } E \dot { y }$ as first integral,i.e., $E$ isskew-symmetric and $y ^ { T } E f ( y ) = 0$ Forasymmetric,consistent linearmultistep method(1.8)of order $r$ ,therethenexistsa seriesof theform

$$
\tilde { L } ( y , \dot { y } ) = y ^ { T } E \dot { y } + h ^ { r } L _ { r + 1 } ( y , \dot { y } ) + h ^ { r + 2 } L _ { r + 3 } ( y , \dot { y } ) + \dots ,
$$

whichisa formal first integralofthemodifiedequation(3.9)without truncation.

Proof.Multiplying(4.14)with $y ^ { T } E$ gives

$$
y ^ { T } E ( 1 + \gamma _ { r } h ^ { r } D ^ { r } + \gamma _ { r + 2 } h ^ { r + 2 } D ^ { r + 2 } + . . . ) \ddot { y } = y ^ { T } E f ( y ) + \mathcal { O } ( h ^ { N } ) .
$$

The term at theright vanishes.Since $\mathcal { L }$ isaskew-symmetricmatrix,we have for the terms tothe leftthat $\begin{array} { r } { y ^ { T } E \ddot { y } = \frac { d } { d t } y ^ { T } E \dot { y } } \end{array}$ and that

$$
y ^ { T } E y ^ { ( 2 m + 2 ) } = { \frac { d } { d t } } { \Big ( } y ^ { T } E y ^ { ( 2 m + 1 ) } - { \dot { y } } ^ { T } D y ^ { ( 2 m ) } + \ldots \pm y ^ { ( m ) T } E y ^ { ( m + 1 ) } { \Big ) } .
$$

Thisyields the statement as in the previous proofs.

Remark 4.12.Noticing that the underlying one-step method of a symmetric multistepmethod can beexpressed asa formal B-series(cf.Sect.XV.2.2),it follows from(4.17)that the modified first integral of Theorem 4.10is of the form(VI.8.6). ByTheorem VI.8.5 theunderlying one-stepmethod is thereforeconjugate toasymplectic integrator.

Asimilarresult holds for symmetric methods(1.8) complemented witha symmetric derivative approximation(3.11).The variables $\upsilon$ and $\dot { y }$ are related via(3.12) having an expansion in even powers of $h$ Substituting $\dot { y } = \dot { y } ( y , v )$ of thisrelation intothe modified first integral(4.18),we obtainan expression of the form(VI.8.11). Here,the elementary differentials correspond to the system $y = v$ , $\dot { v } = f ( y )$ ( $v$ has tobe identified with $z$ ).TheoremVI.8.8combinedwith Theorem4.11provesthat the underlying one-step method is conjugate to a symplectic integrator.

# XV.5Long-TermStability

Theresults of Sects.XV.4.3 and XV.4.4 imply the nearconservation of the total energy and oftheangular momentum in $N$ -bodyproblems for numerical solutions oftheunderlying one-step method of multistep methods.This,however,isof no valueas longas theparasitic solutions of themultistep method are not under control. Thepresent section is devoted to the study of the stability of numerical solutions overlong time intervals.

# XV.5.1 RoleofGrowth Parameters

Theanalysis of this section isbased on the representation

$$
y _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h )
$$

of the numerical solution of a multistep method (cf.formula (3.16)).

LinearMultistepMethodsforFirstOrderEquations.By Theorem3.5 theparasitic components $z _ { \ell }$ (for $2 \leq \ell \leq k$ ）arethe solution ofadifferential equation which,by(3.22),isof theform

$$
\dot { z } _ { \ell } = \mu _ { \ell } f ^ { \prime } ( y ) z _ { \ell } + \ldots .
$$

This is just the variational equation of $\dot { y } = f ( y )$ scaled by

$$
\mu _ { \ell } = \frac { \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } \rho ^ { \prime } ( \zeta _ { \ell } ) } ,
$$

whichis the so-called growth parameter as introduced by Dahlquist (1959)and motivated there bya linear stability analysis (see Exercise5).

Weshallillustrate at the examples of Sect.XV.3.2 that the study of the truncated equation(5.2)gives alreadyalot of insight into the long-time behaviour ofmultistep methods.

![](images/3d393701d05b794dbbbcd0cfd81767020909e9b9dd7ba66813e6ebecf1f8d239.jpg)  
Fig.5.1.First component of the solution of the pendulum equation(grey） together with the Euclidean norm of the solution $v ( t )$ of the scaled variational equation (5.4)

Example 5.1.For the pendulum equation,the truncated equation (5.2) is

$$
\left( { \begin{array} { c } { { \dot { y } } _ { 1 } } \\ { { \dot { y } } _ { 2 } } \end{array} } \right) = \left( { \begin{array} { c } { { y _ { 2 } } } \\ { { - \sin y _ { 1 } } } \end{array} } \right) , \qquad \left( { \begin{array} { c } { { \dot { v } } _ { 1 } } \\ { { \dot { v } } _ { 2 } } \end{array} } \right) = \mu \left( { \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \cos y _ { 1 } } } & { { 0 } } \end{array} } \right) \left( { \begin{array} { c } { { v _ { 1 } } } \\ { { v _ { 2 } } } \end{array} } \right) .
$$

Wefix initial valuesas $y ( 0 ) = ( 1 . 9 , 0 . 4 ) ^ { T }$ and $v ( 0 ) = ( 0 . 1 , 0 . 1 ) ^ { I } .$ Figure5.1 shows the solution component $y _ { 1 } ( t )$ in grey,and the Euclidean norm of $v ( t )$ as solidblack line,once for $\mu = - 1$ and once for $\mu = 0 . 5$ Wenotice that the function $v ( t )$ remains small and bounded for $\mu = - 0 . 5$ ,andthat it increases linearly for $\mu = - 1$

Thisagreesperfectlywith the observations ofFigs.3.1 and 3.2,because the method (3.13) has growth parameter $\mu _ { \ell } = - 0 . 5$ for the roots $\zeta _ { \ell } = \pm i$ ,whereas the explicit midpoint rule(3.14）has $\mu _ { \ell } = - 1$ for $\zeta _ { \ell } = - 1$

Thesame analysis for partitioned multistep methods allows one to better understand thebehaviourof thedifferentmethodsinFig.1.3.The leadingtermof the parasitic modified equations depends on whether $\boldsymbol { \mathscr { Q } }$ isaroot of bothpolynomials $\rho _ { A } ( \zeta )$ and $\rho _ { B } ( \zeta )$ ,oronly ofone of them.Thisisvery similar to the situation encountered with multistepmethods for second orderdifferential equations which we treat next.

LinearMultistep Methods for Second Order Equations.Theorem 3.6 tellsus that the modified equation for the parasitic components $\boldsymbol { \mathcal { Z } } \boldsymbol { \ell }$ depends on the multiplicity of the root $\zeta _ { \ell }$ Considera stable,symmetric method(1.8)for $\ddot { y } = f ( y ) .$ If $\zeta _ { \ell }$ isa double rootof $\rho ( \zeta )$ ,formula(3.29)yields

$$
\ddot { z } _ { \ell } = \mu _ { \ell } f ^ { \prime } ( y ) \dot { z } _ { \ell } + . . . . , \mu _ { \ell } = \frac { 2 \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } ^ { 2 } \rho ^ { \prime \prime } ( \zeta _ { \ell } ) } ,
$$

where we have not written terms containingat least two factors $z _ { j } .$ If $\zeta _ { \ell }$ isasingle root of $\rho ( \zeta )$ ,weget from(3.30） that

$$
\dot { z } _ { \ell } = h \mu _ { \ell } f ^ { \prime } ( y ) z _ { \ell } + \ldots , \qquad \mu _ { \ell } = \frac { \sigma ( \zeta _ { \ell } ) } { \zeta _ { \ell } \rho ^ { \prime } ( \zeta _ { \ell } ) } .
$$

Thereisan enormous difference between the parasitic modified equations corresponding todouble or single rootsof $\rho ( \zeta ) .$ Equation (5.5) is the complete analogue of(5.2)and,as before,the long-time behaviouris hardlypredictableand strongly depends on the growth parameter.For single roots,however,we are concernedwith afirstorder differential equation(5.6) havinganadditional factor $\hbar$ asbonus.For theanalysis of Sects.XV.5.2 and XV.5.3itis important to have only singleroots.

Definition 5.2.A symmetric multistep method (1.8） for second order differential equationsiscalleds-stableif,apart fromthedoublerootat $1$ ,all zeros of $\rho ( \zeta )$ are simple and ofmodulus one.

The linearized parasitic modified equations give much insight into the long-time behaviour of multistep methods.To get rigorous estimes over long times,however, furtherconsiderationsare necessary.A partial result is given byCano&Sanz-Serna （1998)for multistep methods(1.8）applied to equations $\ddot { y } = f ( y )$ with periodic exact solution.There,the first terms of the asymptotic error expansion for the global errorarecomputed,and their growthasa function of time is studied.We shall follow theapproachof Hairer&Lubich（2Oo4）who exploit theHamiltonian structureof second order differential equations.

# XV.5.2Hamiltonian of theFullModified System

Intheremainder of this section we restrict our consideration to s-stable,irreducible linearmultistepmethods

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } q _ { n + j } = - h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } \nabla U ( q _ { n + j } ) ,
$$

applied to Hamiltonian systemswritten as

$$
\ddot { q } = - \nabla U ( q ) ,
$$

where $U ( q )$ is assumed to be real-analytic in the considered region.

Thekey toprovinglong-time error estimates is the observation that much of the Hamiltonian structureis conserved in themodified equations(3.25).Theresults and techniques of this subsectionare closely related to those of Sect.XIII.6.3developed fornumerical methods for oscillatory differential equations.

We let ${ \bf z } = ( z _ { \ell } ) _ { \ell \in \mathcal { T } _ { N } }$ and define $\mathcal { U } ( \mathbf { z } )$ as

$$
\mathcal { U } ( \mathbf { z } ) = U ( z _ { 0 } ) + \sum _ { m \geq 1 } \frac { 1 } { m ! } \sum _ { \zeta _ { \boldsymbol { \kappa } _ { 1 } } , \ldots , \zeta _ { \boldsymbol { \epsilon } _ { m } } = 1 } U ^ { ( m ) } ( z _ { 0 } ) ( z _ { \boldsymbol { \ell } _ { 1 } } , \ldots , z _ { \boldsymbol { \ell } _ { m } } ) ,
$$

where the secondsumisoverallindices $\ell _ { 1 } \in \mathcal { L } _ { N } ^ { * } , \ldots , \ell _ { m } \in \mathcal { L } _ { N } ^ { * }$ with $\zeta _ { \ell _ { 1 } } \ldots \zeta _ { \ell _ { m } } = 1$ (using the notation of Sect.XV.3.2).Since theroots of $\rho ( \zeta )$ ,differentfrom $\zeta _ { 1 } = 1$ arecomplex and appear in pairs(Exercise 3),also the functions $z _ { \ell }$ appearinpairs. It is convenient touse the notation $z _ { - \ell } = z _ { j }$ if $\zeta _ { \ell } = \zeta _ { j }$ .

It follows from (3.28)with $f ( q ) = - \nabla U ( q )$ that every solution of the truncated modified equation(3.25) satisfies

$$
\rho ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = - h ^ { 2 } \sigma ( \zeta _ { \ell } e ^ { h D } ) \nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } ) + \mathcal { O } ( h ^ { N + 2 } )
$$

(for all $\ell \in \mathcal { L }$ aslongas

$$
y \in K , \quad \| { \dot { y } } \| \leq M , \quad \| z _ { \ell } \| \leq \delta { \mathrm { ~ f o r ~ } } 1 < \ell < k ,
$$

where $K$ isacompact subset of the domain of analyticity of $U ( q )$ ， $M > 0$ some bound on the derivative,and $0 < \delta = { \mathcal { O } } ( h )$ isasufficiently small constant (note that this implies $\| z _ { \ell } \| \le \delta$ forall $\ell \in \mathcal { T } ^ { * }$ if $h$ issufficiently small, cf.thealgebraic relations of (3.25)).

Forease of presentation,we assume for the moment that $\sigma ( \zeta _ { \ell } ) \neq 0$ forall $\ell \in \mathcal { I } _ { N }$ (we know that this holds for $1 \le \ell < k$ ,because the method is irreducible). Weapply the operator $\sigma ^ { - 1 } ( \zeta _ { \ell } e ^ { h D } )$ to both sides of(5.10)and divide by $h ^ { 2 }$

$$
h ^ { - 2 } \Big ( { \frac { \rho } { \sigma } } \Big ) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = - \nabla _ { z \_ \ell } \mathcal { U } ( \mathbf { z } ) + \mathcal { O } ( h ^ { N } ) .
$$

We then multiply with $\dot { z } _ { - \ell } ^ { T }$ , sum over all $ { \ell } \in  { \mathcal { L } } _ { N }$ ,and thus obtain

$$
h ^ { - 2 } \sum _ { \ell \in \mathcal { T } _ { N } } \dot { z } _ { - \ell } ^ { T } \Big ( \frac { \rho } { \sigma } \Big ) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } + \frac { d } { d t } \mathcal { U } ( \mathbf { z } ) = \mathcal { O } ( h ^ { N } ) .
$$

Wenow show that also the first expression on the left-hand side isa total derivative ofa function depending on $\mathbf { z }$ and its time derivatives.Forthiswe note that

$$
\left( { \frac { \rho } { \sigma } } \right) ( \zeta \ell e ^ { i x } ) = \sum _ { j \geq 0 } c _ { \ell , j } x ^ { j } \qquad { \mathrm { w i t h ~ } } r e a l { \mathrm { ~ c o e f f i c i e n t s } } \quad c _ { \ell , j } = ( - 1 ) ^ { j } c _ { - \ell , j } .
$$

This holds because the symmetry of the multistep method yields $( \rho / \sigma ) ( 1 / \zeta ) =$ $( \rho / \sigma ) ( \zeta )$ and hence,for real $x$ ， $( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) = ( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) = { \overline { { ( \rho / \sigma ) ( \zeta _ { \ell } e ^ { i x } ) } } }$ . Withtheexpansion（5.14）we obtain

$$
\left( \frac { \rho } { \sigma } \right) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } = \sum _ { j = 0 } ^ { N + 1 } c _ { \ell , j } ( - i h ) ^ { j } z _ { \ell } ^ { ( j ) } + \mathcal { O } ( h ^ { N + 2 } ) .
$$

Tostudy(5.13）weapplytherelation (4.12) for thereal function $y = z _ { 1 }$ and for $z _ { \ell }$ corresponding to $\zeta _ { \ell } = - 1$ ,while for thecomplex-valued functions $z = z _ { \ell }$ ,with complex conjugate $z = z _ { - \ell }$ ,weuse

$$
\begin{array} { l } { { \displaystyle \mathrm { R e } ^ { \frac { \cdot } { z } T } z ^ { ( 2 m ) } = \mathrm { R e } \frac { d } { d t } \Big ( \dot { \bar { z } } ^ { T } z ^ { ( 2 m - 1 ) } - \ddot { \bar { z } } ^ { T } z ^ { ( 2 m - 2 ) } + . . . \pm \frac { 1 } { 2 } ( \bar { z } ^ { ( m ) } ) ^ { T } z ^ { ( m ) } \Big ) } \ ~ } \\ { { \displaystyle \mathrm { I m } \ddot { \bar { z } } ^ { T } z ^ { ( 2 m + 1 ) } = \mathrm { I m } \frac { d } { d t } \Big ( \dot { \bar { z } } ^ { T } z ^ { ( 2 m ) } = \ddot { \bar { z } } ^ { T } z ^ { ( 2 m - 1 ) } + . . . \mp ( \bar { z } ^ { ( m ) } ) ^ { T } z ^ { ( m + 1 ) } \Big ) } . } \end{array}
$$

Together with(5.15) theserelations show that the terms

$$
{ \dot { z } } _ { - \ell } ^ { T } \Bigl ( { \frac { \rho } { \sigma } } \Bigr ) ( { \zeta } _ { \ell } e ^ { h D } ) z _ { \ell } + { \dot { z } } _ { \ell } ^ { T } \Bigl ( { \frac { \rho } { \sigma } } \Bigr ) ( { \zeta } _ { - \ell } e ^ { h D } ) z _ { - \ell }
$$

$$
= \sum _ { j = 0 } ^ { N + 1 } c _ { \ell , j } 2 \operatorname { R e } \left( ( - i h ) ^ { j } \vec { z } _ { \ell } ^ { \ : T } z _ { \ell } ^ { ( j ) } \right) + \mathcal { O } ( h ^ { N + 2 } )
$$

giveatotal derivative(upto theremainder term).Hence the left-hand sideof(5.13) can be written asthe time derivative ofa function whichdepends on $z _ { \ell }$ , $\ell \in \mathcal { L } _ { N }$ ,and ontheir derivatives.Usingthe modified equation(3.25）we eliminate all $z _ { \ell }$ correspondingto $\zeta _ { \ell }$ with $\rho ( \zeta _ { \ell } ) \neq 0$ andtheirderivatives,the firstand higherderivatives of $z _ { \ell }$ (for $1 < \ell < k$ ),and the second and higher derivatives of $y = z _ { 1 }$ Wethus get afunction

$$
\mathcal { H } ( y , \dot { y } , \mathbf { z ^ { * } } ) = H _ { 0 } ( y , \dot { y } , \mathbf { z ^ { * } } ) + . . . . + h ^ { N - 1 } H _ { N - 1 } ( y , \dot { y } , \mathbf { z ^ { * } } )
$$

$\mathbf { z } ^ { * } = ( z _ { \ell } ) _ { \ell = 2 } ^ { k - 1 }$ ,such that

$$
\frac { d } { d t } \mathcal { H } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) \big ) = \mathcal { O } ( h ^ { N } ) ,
$$

alongsolutions of.(3.25） that stayina set defined by(5.11).The function $\mathcal { H }$ is therefore an almost-invariant of the system (3.25).

If,however, $\sigma ( \zeta )$ does havea zero $\zeta _ { \ell }$ ,then we omit the corresponding term from the sum in (5.13).Hence the term $\dot { z } _ { - \ell } ^ { \varDelta } \nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } )$ ismissing from $( d / d t ) \mathcal { U } ( \mathbf { z } )$ and musttherefore be compensated in theremainder term.Since $\zeta _ { \ell }$ isa product of no fewer than two zeros of $\rho ( \zeta )$ ,it follows from(3.31）and from $\mu _ { \ell , 0 } = 0$ that $z _ { \ell } =$ $\mathcal { O } ( h ^ { 3 } \delta ^ { 2 } )$ ,aslong as $\| z _ { j } \| \leq \delta$ for $1 < j < k$ Wefurtherhave $\nabla _ { z _ { - } } \mathcal { U } ( \mathbf { z } ) = \mathcal { O } ( \delta ^ { 2 } )$ ， so that theremainder termin（5.17）isaugmented by $\mathcal { O } ( h ^ { 3 } \delta ^ { 4 } )$ .

Wesummarize theabove considerations(Hairer&Lubich 2oo4)as follows.

Theorem5.3.Every solution of the truncatedmodifiedequation(3.25) satisfies, withH from(5.16),

$$
\begin{array} { r } { \mathcal { H } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) \big ) = \mathcal { H } \big ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf z } ^ { * } ( 0 ) \big ) + \mathcal { O } ( t h ^ { N } ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) } \end{array}
$$

aslongas the solution stays in the set definedby(5.11).Moreover,

$$
\begin{array} { r } { \mathcal { H } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = H ( y , \dot { y } ) + \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( h \delta ^ { 2 } ) . } \end{array}
$$

The closeness to the Hamiltonian $H ( y , \dot { y } ) = \textstyle { \frac { 1 } { 2 } } \| \dot { y } \| ^ { 2 } + U ( y )$ follows also directly from the above construction.For $\mathbf { z } ^ { \ast } = \mathbf { 0 }$ wehave $\mathcal { H } ( y , \dot { y } , 0 ) = \bar { H } ( y , \dot { y } )$ , where $\bar { H }$ is themodified energy from Theorem 4.9.

We willuse Theorem5.3in SectionXV.6.1to infer the long-timenear-conservation of the Hamiltonian along numerical solutions.Before that we need to bound the parasitic components.

# XV.5.3Long-Time Bounds for Parasitic Solution Components

Themodified equations have further almost-invariantswhich are close to the squares ofthe norms of the parasitic components that correspond to the roots of $\rho ( \zeta )$ We derive them here and use them to show that allparasitic solution components remain small oververy long times.The techniquesused in this subsectionare similar to thosein Sects.XIII.6 and XIII.7.

We consider $\ell$ with $1 < \ell < k$ forwhich $\zeta _ { \ell }$ is a simple root of $\rho ( \zeta )$ and $\sigma ( \zeta _ { \ell } ) \neq$ O.The dominant term on the left-hand side of(5.12)is $- c _ { \ell , 1 } i h ^ { - 1 } \dot { z } _ { \ell } .$ Since

$$
\frac { d } { d t } \| \boldsymbol { z } _ { \ell } \| ^ { 2 } = \boldsymbol { z } _ { - \ell } ^ { T } \dot { \boldsymbol { z } } _ { \ell } + \boldsymbol { z } _ { \ell } ^ { T } \dot { \boldsymbol { z } } _ { - \ell } ,
$$

we multiply (5.12) with $z _ { - \ell } ^ { T }$ and the corresponding equation for $\zeta _ { - \ell }$ with $z _ { \ell } ^ { T }$ ,and weform the difference,so that the dominant term on the left-hand side becomes $\begin{array} { r } { - c _ { \ell , 1 } i h ^ { - 1 } \frac { d } { d t } \| z _ { \ell } \| ^ { 2 } } \end{array}$ (note $c _ { - \ell , 1 } = - c _ { \ell , 1 } ,$ .Dividing by $- c _ { \ell , 1 } i h ^ { - 1 }$ gives

$$
\begin{array} { r l } & { \frac { i } { c _ { \ell , 1 } h } \Big ( z _ { - \ell } ^ { T } \frac { \rho } { \sigma } ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } - z _ { \ell } ^ { T } \frac { \rho } { \sigma } ( \zeta _ { - \ell } e ^ { h D } ) z _ { - \ell } \Big ) } \\ & { \qquad = \frac { i h } { c _ { \ell , 1 } } \Big ( - z _ { - \ell } ^ { T } \nabla _ { z _ { - \ell } } \mathcal { U } ( { \bf z } ) + z _ { \ell } ^ { T } \nabla _ { z _ { \ell } } \mathcal { U } ( { \bf z } ) \Big ) . } \end{array}
$$

Wefirst estimate theright-hand expression.Since

$$
\nabla _ { z _ { - \ell } } \mathcal { U } ( \mathbf { z } ) = \nabla ^ { 2 } U ( z _ { 0 } ) z _ { \ell } + \mathcal { O } ( \delta ^ { 2 } ) ,
$$

aslong as (5.11）is satisfied,we obtain from the symmetry of the Hessian that the right-hand side of(5.21)isof size $\mathcal { O } ( h \delta ^ { 3 } )$ Thedominant $\mathcal { O } ( h \delta ^ { 3 } )$ termis present onlyif $\zeta _ { - \ell }$ can be written as the product of two roots of $\rho ( \zeta )$ other than 1.If this is not the case,the expression (5.21) is of size $\mathcal { O } ( h \delta ^ { 4 } )$

Usingthe expansion (5.15)on the left-hand side of(5.21)and therelations (for $z = z _ { \ell }$ ）

$$
\begin{array} { l } { { \mathrm { R e } \overline { { { z } } } ^ { T } z ^ { ( 2 m + 1 ) } = \mathrm { R e } \displaystyle \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } z ^ { ( 2 m ) } - \frac { \div ^ { T } } { \overline { { { z } } } } z ^ { ( 2 m - 1 ) } \cdots \mp \frac { 1 } { 2 } ( \overline { { { z } } } ^ { ( m ) } ) ^ { T } z ^ { ( m ) } \Big ) } } \\ { { \mathrm { I m } \overline { { { z } } } ^ { T } z ^ { ( 2 m + 2 ) } = \mathrm { I m } \displaystyle \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } z ^ { ( 2 m + 1 ) } - \overline { { { z } } } ^ { T } z ^ { ( 2 m ) } + \ldots \pm ( \overline { { { z } } } ^ { ( m ) } ) ^ { T } z ^ { ( m + 1 ) } \Big ) } } \end{array}
$$

weobtain that(5.21) is,up to $\mathcal { O } ( h ^ { N } )$ ,thetotalderivativeofafunctiondepending on $\mathbf { z }$ and itsderivatives.

By construction the dominant termis $\frac { d } { d t } \left| \right| z _ { \ell } \left| \right| ^ { 2 } ,$ The following terms have at least one more power of $h$ andat least one derivativewhich by(3.25）gives rise to an additional factor $h$ .Eliminating higher derivativeswith the help of(3.25),we arrive ata function of the form

$$
\displaystyle { \mathcal { K } _ { \ell } ( y , \dot { y } , \mathbf { z } ^ { * } ) = \| z _ { \ell } \| ^ { 2 } + h ^ { 2 } K _ { \ell , 2 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + . . . + h ^ { N - 1 } K _ { \ell , N - 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) } .
$$

Aswe haveseen,its total derivativeis of size $\mathcal { O } ( h \delta ^ { 3 } )$ orsmaller.We summarize these considerations in the following theorem.

Theorem5.4.Alongevery solution of thetruncated modifedequation(3.25) the function $\boldsymbol { \mathcal { K } } _ { \ell } ( y , \dot { y } , \mathbf { z } ^ { * } )$ satisfiesfor $1 < \ell < k$

$$
\begin{array} { r } { K _ { \ell } \big ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) \big ) = K _ { \ell } \big ( y ( 0 ) , \dot { y } ( 0 ) , \mathbf { z } ^ { * } ( 0 ) \big ) + \mathcal { O } ( t h ^ { N } ) + \mathcal { O } ( t h \delta ^ { 3 } ) } \end{array}
$$

aslongasthe solutionstaysinthe set defined by(5.11).Theseconderror termis replacedby $\mathcal { O } ( t h \delta ^ { 4 } )$ ifno rootof $\rho ( \zeta )$ otherthan $^ { 1 }$ is theproduct oftwo other roots. Moreover,

$$
\begin{array} { r } { \mathcal { K } _ { \ell } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = \| z _ { \ell } \| ^ { 2 } + \mathcal { O } ( h ^ { 2 } \delta ^ { 2 } ) . } \end{array}
$$

Thisresult allows us to write the numerical solution ina form that is suitable for deriving long-time error estimates.Let us first collect the necessary assumptions:

（A1）the multistep method(5.7) is symmetric, $s$ -stable,andof order $T$ ;   
（A2）the potential function $U ( q )$ of(5.8)is defined and analytic in an open neighbourhood of acompact set $K$ ;   
（A3）the starting approximations $q _ { 0 } , \ldots , q _ { k - 1 }$ are such that the initial values for (3.25）obtained from Lemma 3.7 satisfy $y ( 0 ) \in K$ , $\| \dot { \boldsymbol { y } } ( 0 ) \| ~ \le ~ M$ ,and $\| z _ { \ell } ( 0 ) \| \le \delta / 2$ for $1 < \ell < k$ ;   
（A4）the numerical solution $\left\{ q _ { n } \right\}$ stays for $0 \leq n h \leq T$ in a compact set $K _ { 0 }$ which hasapositive distance to the boundary of $K$

Theorem5.5 (Hairer&Lubich2004).Assume(A1)-(A4).Forsufficiently small $h$ and $\delta$ and forafixedtruncation index $N$ (large enough such that $h ^ { N } = { \mathcal O } ( \delta ^ { 4 } ) ,$ , thereexist functions $y ( t )$ and $z _ { \ell } ( t )$ onan intervaloflength

$$
T = { \cal O } ( ( h \delta ) ^ { - 1 } )
$$

such that

· $q _ { n } = y ( n h ) + \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h )$ for0≤nh≤T;   
·onevery subinterval $| j h , ( j + 1 ) h )$ thefunctions $y ( t ) , z _ { \ell } ( t )$ area solution of the system（3.25）；   
the functions $y ( t ) , z _ { \ell } ( t )$ have jump discontinuities of size $\mathcal { O } ( h ^ { N + 2 } )$ at thegrid points $j h$   
$\| z _ { \ell } ( t ) \| \leq \delta$ for $0 \leq t \leq T .$

Ifno root of $\rho ( \zeta )$ other than $^ { 1 }$ isthe product of two other roots,all theseestimates arevalidonanintervalof length $T = { \cal O } ( ( h \delta ^ { 2 } ) ^ { - 1 } )$

Proof. To define the functions $y ( t )$ , $z _ { \ell } ( t )$ on the interval $[ j h , ( j + 1 ) h )$ we consider the $k$ consecutive numerical solution values $q _ { \lambda } , q _ { \lambda + 1 } , . . . , q _ { \lambda + k - 1 } .$ Wecompute initialvalues for(3.25)accordingtoLemma3.7,andwe let $y ( t ) , z _ { \ell } ( t )$ be a solution of (3.25)on $[ j h , ( j + 1 ) h ) .$ Because their defect is $\mathcal { O } ( h ^ { N } )$ and $\mathcal { O } ( h ^ { N + 1 } )$ ,respectively, such a construction yields jump discontinuities of size $\mathcal { O } ( h ^ { N + 2 } )$ at the grid points.

Itfollows from Theorem5.4 that $\mathcal { K } _ { \ell } ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) )$ remains constant up to an error of size $\mathcal { O } ( h ^ { 2 } \delta ^ { 3 } )$ on the interval $\left| j h , ( j + 1 ) h \right.$ Taking into account the jump discontinuities,we find that

$$
\begin{array} { r } { K _ { \ell } ( y ( t ) , \dot { y } ( t ) , { \mathbf z } ^ { * } ( t ) ) \le K _ { \ell } ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf z } ^ { * } ( 0 ) ) + C _ { 1 } t h \delta ^ { 3 } + C _ { 2 } t h ^ { N + 1 } } \end{array}
$$

as longas $\| z _ { \ell } ( t ) \| \leq \delta .$ By（5.24）this then implies

$$
\| z _ { \ell } ( t ) \| ^ { 2 } \leq \| z _ { \ell } ( 0 ) \| ^ { 2 } + C _ { 1 } t h \delta ^ { 3 } + C _ { 2 } t h ^ { N + 1 } + C _ { 3 } h ^ { 2 } \delta ^ { 2 } .
$$

The assumption $\| z _ { \ell } ( t ) \| ~ \le ~ \delta$ iscertainly satisfied as long as $C _ { 1 } t h \delta \ \leq \ 1 / 4$ , $C _ { 2 } t h ^ { N + 1 } \leq \delta ^ { 2 } / 4$ ,and $C _ { 3 } h ^ { 2 } \leq 1 / 4$ sothat theright-hand sideof（5.26)is bounded by $\delta ^ { 2 }$ This proves not only the estimate for $| | z _ { \ell } ( t ) | |$ ,but at the same time it guaranteesrecursively that the above construction of the functions $y ( t ) , z _ { \ell } ( t )$ is feasible. $\boxed { \begin{array} { r l } \end{array} }$

Notice that forinitial values computed bya sufficiently accurate one-step method the constant $\delta$ can be chosen as small as $\mathcal { O } ( h ^ { r + 2 } )$ where $r$ is the order ofthemultistepmethod (cf.Lemma 3.7).The above estimatesare thereforevalid onvery long time intervals.

Example5.6.To illustrate the long-time behaviour of the parasitic terms $z _ { \ell }$ we consider the pendulum equation $q = - \sin q$ ,andwe apply the symmetricmultistep methods(B)and(C) of Example1.2.For method (C),the starting values are chosen farfrom a smooth solution,so that the propagation of the parasitic termsin the numerical solution can be better observed.We compute the velocity approximation by

$$
v _ { n } = { \frac { h } { 1 2 } } \Big ( 8 ( q _ { n + 1 } - q _ { n - 1 } ) - ( q _ { n + 2 } - q _ { n - 2 } ) \Big ) .
$$

![](images/eacb69580dbd7f43a8ba97d06ad7261ca22218e30b6a03238035d2ca9c57662e.jpg)  
Fig.5.2.Stable propagation of perturbations in the starting values for method(C)of Example 1.2;initial values are $q _ { 0 } = 1 . 1 4 1$ $q _ { 1 } = 1 . 1 5 8$ , $q _ { 2 } = 1 . 1 7 8$ and $q _ { 3 } = 1 . 2 0 6$

![](images/59ad34f059343e1d5853b59b4b92c65fdcc5a13205a1afa2a328a36120342f22.jpg)  
Fig.5.3.Unstable propagation of perturbations in thestartingvalues,for method(B)of Example1.2;initial valuesare $q _ { 0 } = 1 . 1 4 7$ $q _ { 1 } = 1 . 1 8 3$ , $q _ { 2 } = 1 . 2 5 5$ ,and $q _ { 3 } = 1 . 2 8 6$

Figure 5.2 shows the numerical solution $( q _ { n } , v _ { n } )$ for $n \geq 2$ Thevalues for $n =$ $2 , 3 , 4 , 5$ areindicated by larger black bullets.The parasitic roots of method (C)are $\pm i$ andboth are simple.The numerical solution is therefore of the form

$$
q _ { n } = y ( n h ) + i ^ { n } z _ { 1 } ( n h ) + ( - i ) ^ { n } { \overline { { z _ { 1 } ( n h ) } } } + ( - 1 ) ^ { n } z _ { 2 } ( n h ) .
$$

One observesin Fig.5.2 that the functions $z _ { j } ( t )$ not only remain boundedand small, butthey stay essentiallyconstant over theconsidered interval.This shouldbecompared to Fig.3.1,where the parasitic functions $z _ { j } ( t )$ are bounded,but not constant.

Method(B) hasa double parasitic root at $^ { - 1 }$ and,therefore,is not $s$ -stable. Its numerical solution behaves like $q _ { n } = y ( n h ) + ( - 1 ) ^ { n } z ( n h )$ InFig.5.3every second approximation is drawnin grey.One sees that the numerical solution stays on two smooth curves $y ( t ) + z ( t )$ and $y ( t ) - z ( t )$ which,however,do not remain close to each other.

# XV.6 Explanation of the Long-Time Behaviour

The bounds on the parasitic solution components of Sect.XV.5.3 allow us to get rigorousstatements on the long-time behaviour of multistep methods(5.7)for second orderdifferential equations.Thefollowingresultsaretaken fromHairer&Lubich (2004).We do not know of similar results for multistep methods (1.1).

# XV.6.1 Conservation of Energy and Angular Momentum

Theenergyconservationis now a directconsequence ofTheorems 5.3and 5.5.We shall use the representation of $q _ { n }$ in terms of functions $y ( t ) , z _ { \ell } ( t )$ as in Theorem 5.5. Taking intoaccount the jumpdiscontinuities of these functions,Theorem5.3 yields

$$
\begin{array} { r } { \mathcal { H } ( y ( t ) , \dot { y } ( t ) , \mathbf { z } ^ { * } ( t ) ) = \mathcal { H } ( y ( 0 ) , \dot { y } ( 0 ) , \mathbf { z } ^ { * } ( 0 ) ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) + \mathcal { O } ( t h ^ { N + 1 } ) . } \end{array}
$$

Wehave $\delta = \mathcal { O } ( h ^ { r + 1 } )$ if the starting approximations are computed by a $r$ th.order one-step method.If $N$ ischosen sufficiently large,this together with(5.19) implies

$$
\begin{array} { r } { H ( y ( t ) , \dot { y } ( t ) ) = H ( y ( 0 ) , \dot { y } ( 0 ) ) + { \mathcal O } ( h ^ { p } ) \qquad \mathrm { f o r } \quad 0 \le t \le T = { \mathcal O } ( h ^ { - p - 2 } ) . } \end{array}
$$

If the velocity approximation $\begin{array} { r } { p _ { n } \ = \ v _ { n } } \end{array}$ is given bya $r$ thorderfinitedifference formula(3.11),it follows from Theorem5.5 that $p _ { n } = { \dot { y } } ( n h ) + { \mathcal { O } } ( h ^ { r } )$ provided the truncation index $N$ issufficiently large.Thisproves the following result,and explains the excellent long-time behaviour of method(C)in Fig.1.2.

Theorem6.1(Total Energy).Foraproblem $\ddot { q } ~ = ~ - \nabla U ( q )$ with total energy $H ( p , q ) = { \textstyle \frac { 1 } { 2 } } p ^ { 1 } p + U ( q )$ ,thenumerical solutionofan s-stable symmetric multistepmethod(5.7)oforder $r$ satisfies

$$
H ( q _ { n } , p _ { n } ) = H ( q _ { 0 } , p _ { 0 } ) + { \mathcal O } ( h ^ { r } ) \qquad f o r \quad n h \leq h ^ { - r - 2 } .
$$

Ifnorootof $\rho ( \zeta )$ other than $1$ isaproduct of two other roots,the statement holds onintervalsoflength $O ( h ^ { - 2 r - 3 } )$ □

Weassume next that thedifferential equation $\ddot { q } = - \nabla U ( q )$ hasa quadratic first integral of the form $L ( q , \dot { q } ) = \dot { q } ^ { T } A q$ (e.g.,the angular momentumin $N$ -body problems).Thismeans that $A$ is skew-symmetric and $\nabla U ( q ) ^ { T } A q = 0$ Thelast equation can also be interpreted as the invariance relation $U ( e ^ { \tau A } q ) = U ( q ) .$ This property implies for $\mathcal { U } ( \mathbf { z } )$ givenby（5.9），that $\mathcal { U } ( e ^ { \tau A } \mathbf { z } ) = \mathcal { U } ( \mathbf { z } )$ (here $e ^ { \tau { \cal A } } \mathbf { z } =$ $( e ^ { \tau A } z _ { \ell } ) _ { \ell \in \mathcal { T } } )$ Along solutions ${ \bf z } ( t )$ of themodified equations (5.10)we therefore haveup to terms of size $\mathcal { O } ( h ^ { N } )$

$$
= \frac { d } { d \tau } \Big | _ { \tau = 0 } \mathcal { U } ( e ^ { \tau A } \mathbf { z } ) = \sum _ { \ell \in \cal Z } z _ { - \ell } ^ { T } A \nabla _ { z = \ell } \mathcal { U } ( \mathbf { z } ) = \sum _ { \ell \in \cal Z } h ^ { - 2 } z _ { - \ell } ^ { T } A \left( \frac { \rho } { \sigma } \right) ( \zeta _ { \ell } e ^ { h D } ) z _ { \ell } ( \mathbf { z } ) .
$$

If $\sigma ( \zeta )$ hasaroot $\zeta _ { \ell }$ ,then the correspondingtermis omitted from the last sum,leadingtoa remainder term which in the worst case is $\mathcal { O } ( h ^ { 3 } \delta ^ { 4 } )$ ,asinTheorem5.3.Like intheprevious proofs,the last sumis,for skew-symmetric $A$ ,the total derivative of afunction

$$
\mathcal { L } ( y , \dot { y } , \mathbf { z } ^ { * } ) = L _ { 0 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + . . . + h ^ { N - 1 } L _ { N - 1 } ( y , \ddot { y } , \mathbf { z } ^ { * } )
$$

which satisfies(under the same assumptions as in Theorem5.3)

$$
\begin{array} { r } { \mathcal { L } \big ( y ( t ) , \dot { y } ( t ) , { \mathbf { z } ^ { * } ( t ) } \big ) = \mathcal { L } \big ( y ( 0 ) , \dot { y } ( 0 ) , { \mathbf { z } ^ { * } ( 0 ) } \big ) + \mathcal { O } ( t h ^ { 3 } \delta ^ { 4 } ) + \mathcal { O } ( t h ^ { N + 1 } ) } \end{array}
$$

and

$$
\begin{array} { r } { \mathcal { L } \big ( y , \dot { y } , \mathbf { z } ^ { * } \big ) = L ( y , \dot { y } ) + \mathcal { O } ( h ^ { p } ) + \mathcal { O } ( \delta ^ { 2 } / h ) . } \end{array}
$$

Wetherefore obtain the following result.

Theorem 6.2 (Angular Momentum). Let $L ( q , \dot { q } ) = \dot { q } ^ { T } A q$ beafirst integral of $\ddot { q } = - \nabla U ( q )$ Thenumerical solution ofan $s$ -stablesymmetricmultistepmethod (5.7)of order $\tau$ thensatisfies

$$
L ( q _ { n } , p _ { n } ) = L ( q _ { 0 } , p _ { 0 } ) + \mathcal { O } ( h ^ { r } ) \qquad f o r \quad n h \leq h ^ { - r - 2 } .
$$

Ifnoroot of $\rho ( \zeta )$ other than1is $^ a$ product oftwootherroots,the statement holds onintervalsoflength $O ( h ^ { - 2 r - 3 } )$ . □

# XV.6.2Linear ErrorGrowth for Integrable Systems

The differential equation $\ddot { q } = - \nabla U ( q )$ writtenas $\dot { q } \ = \ v$ , $\dot { \boldsymbol { v } } = - \nabla U ( \boldsymbol { q } ) .$ is reversible with respect to the involution $v \mapsto - v$ Assumethat itisalsoan integrable system in the sense of Definition XI.1.1,and denote by $a \ = \ I ( q , v )$ theaction variables,and by $\omega ( a )$ the frequences of the system.

By Theorem 5.5,the numerical solution can be written as $q _ { n } ~ = ~ y ( n h ) ~ +$ $\begin{array} { r } { \sum _ { \ell \in \mathbb { Z } ^ { * } } \zeta _ { \ell } ^ { n } z _ { \ell } ( n h ) } \end{array}$ ,where (at least locally) $y ( t )$ is thesolutionofamodifeddifferential equation (first equation of (3.25))

$$
\ddot { y } = f _ { 0 , 0 } ( y , \dot { y } , \mathbf { z } ^ { * } ) + h f _ { 0 , 1 } ( y , \dot { y } , \mathbf { z } ^ { * } ) \stackrel { } { + } \dots + h ^ { N - 1 } f _ { 0 , N - 1 } ( y , \dot { y } , \mathbf { z } ^ { * } )
$$

which,for $\mathbf { z } ^ { * } = 0$ becomes the reversible modified differential equation (3.9).Since $z _ { j } ( t ) = O ( \delta )$ (see Theorem5.5)and since $\mathbf { z } ^ { \ast }$ appears at least quadratically in(6.2), this equation isa $\mathcal { O } ( \delta ^ { 2 } )$ perturbation of (3.9).We are nowin the position toapply theresultsofLemma XI.2.1and Theorem XI.3.1.Theadditional (non-reversible) perturbation of size $\mathcal { O } ( \delta ^ { 2 } )$ in the differential equation (6.2) produces an error term of size $\mathcal { O } ( t \delta ^ { 2 } )$ in the action variables and of size $\mathcal { O } ( t ^ { 2 } \delta ^ { 2 } )$ in the angle variables.If $\delta = \mathcal { O } ( h ^ { r + 1 } )$ ,these terms are negligible with respect to those already appearingin Theorem XI.3.1.The errorsdue to the jumpdiscontinuities(Theorem 5.5） are also negligible.We have thus proved the following statement.

Theorem6.3.Consider applying the $s$ -stablesymmetricmultistepmethod(5.7)of order $r$ toan integrablereversible system $\ddot { q } = - \nabla U ( q )$ with real-analytic potential $U$ Supposethat $\omega ^ { \ast } \in \mathbb { R } ^ { d }$ satisfiesthediophantinecondition(X.2.4).Then, there exist positive constants $C , c$ and $h _ { 0 }$ such that the following holdsforall stepsizes $\textit { h } \leq \ h _ { 0 }$ :everynumerical solution $( q _ { n } , v _ { n } )$ startingwith frequencies $\omega _ { 0 } = \omega ( I ( q _ { 0 } , v _ { 0 } ) )$ suchthat $\lVert \omega _ { 0 } - \omega ^ { * } \rVert \leq c \lvert \log h \rvert ^ { - \nu - 1 }$ satisfies

$$
\begin{array} { r c l } { \| ( q _ { n } , v _ { n } ) - ( q ( t ) , v ( t ) ) \| } & { \leq } & { C t h ^ { r } } \\ { \| I ( q _ { n } , v _ { n } ) - I ( q _ { 0 } , v _ { 0 } ) \| } & { \leq } & { C h ^ { r } } \end{array} \qquad f o r \quad 0 \leq t = n h \leq h ^ { - r } .
$$

Theconstants $h _ { 0 } , c , C$ depend on $d , \gamma , \nu$ and on bounds ofthepotential.

# XV.7 Practical Considerations

In computationswith multistep methods one can observe resonance phenomena,if relatively large step sizesare used.Thisand theuse of variable step sizes are the subject of this section.

# XV.7.1 Numerical Instabilities and Resonances

Soon after Quinlan and Tremaine's methods were published,however, AlarToomre discovered a disturbing feature of the methods,...

(G.D.Quinlan 1999)

It isa simple task to derive multistep methods of high order.Consider,for example, methods of the form (1.8) for second order differential equations $\ddot { y } = f ( y )$ Their orderis determined by thecondition(1.9).Wechoose arbitrarily $\rho ( \zeta )$ such that $\zeta = 1$ isa double zero and the stability condition is satisfied.Condition (1.9)then gives

$$
\sigma ( \zeta ) = \rho ( \zeta ) / \log ^ { 2 } \zeta + \mathcal { O } \bigl ( ( \zeta - 1 ) ^ { r } \bigr ) .
$$

Expanding theright-hand expressionintoa Taylor seriesat $\zeta = 1$ and truncating suitably,thisyields thecorresponding $\sigma$ polynomial. If we take

$$
\rho ( \zeta ) = ( \zeta - 1 ) ^ { 2 } ( \zeta ^ { 6 } + \zeta ^ { 4 } + \zeta ^ { 3 } + \zeta ^ { 2 } + 1 ) ,
$$

Table7.1.Symmetric multistep methods for second order problems; $k = 8$ and order $r = 8$   

<table><tr><td colspan="3"></td><td colspan="2">SY8B</td><td colspan="2">SY8C</td></tr><tr><td>i</td><td>αi</td><td>SY8 12096β</td><td>αi</td><td>120960β</td><td>ai</td><td>8640β</td></tr><tr><td rowspan="4">0 1 2</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td></td><td>17671</td><td>0</td><td>192481</td><td></td><td>13207</td></tr><tr><td>2</td><td>-23622</td><td>0</td><td>6582</td><td></td><td>-8934</td></tr><tr><td>0</td><td>61449 -50516</td><td>-1/2 -1</td><td>816783 -156812</td><td>0 0</td><td>42873 -33812</td></tr></table>

wegetin thisway Method SY8of Table 7.1,a method proposedby Quinlan& Tremaine(199o) for computationsincelestial mechanics.All methods of Table7.1 are8-stepmethods,of order8,and symmetric,i.e.,the relations $\alpha _ { i } = \alpha _ { k - i }$ and $\beta _ { i } = \beta _ { k - i }$ aresatisfied.Therefore,we present the coefficients only for $i \le k / 2$ .

These methods give approximations $y _ { n }$ tothe solution of the differential equation.Ifalsoderivative approximations are needed,weget thembyfinitedifferences, e.g.,for the 8th order methodsof Table7.1we use

$$
\begin{array} { r } { \dot { y } _ { n } = \frac { 1 } { 8 4 0 h } \Big ( 6 7 2 ( y _ { n + 1 } - y _ { n - 1 } ) - 1 6 8 ( y _ { n + 2 } - y _ { n - 2 } ) \Big . \qquad } \\ {  \qquad + 3 2 ( y _ { n + 3 } - y _ { n - 3 } ) - 3 ( y _ { n + 4 } - y _ { n - 4 } ) \Big ) . } \end{array}
$$

Weapply thismethod to the Keplerproblem(I.2.2),oncewith eccentricity $e = 0$ and oncewith $e = 0 . 2$ ,andinitialvalues(I.2.11),such thattheperiodoftheexact solution is $2 \pi$ Starting approximationsare computed accuratelywithahigh order Runge-Kutta method.We apply Method SY8with many different step sizesranging from $2 \pi / 3 0$ to $2 \pi / 9 5$ ,and we plotinFig.7.1 themaximumerror of the total energy asa function of $2 \pi / h$ (where $h$ denotes the step size).We see that in general the error decreaseswith the step size,but there isan extremely large error for $h \approx 2 \pi / 6 0$ . For $e \neq 0$ ,furtherpeakscan beobservedat integralmultiplesof5and6.Itisour aimtounderstand this behaviour.

Instabilities.We put $z = q _ { 1 } + \ i q _ { 2 }$ ,sothatthe Keplerproblem becomes

$$
\ddot { z } = \psi ( | z | ) z , \qquad \psi ( r ) = - r ^ { - 3 } ,
$$

and we choose initial values such that $z ( t ) = e ^ { \ i t }$ is a circular motion (eccentricity $e = 0$ ).Thenumerical solution of(1.8）isthereforedefinedbytherelation

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } z _ { n + j } = h ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } \psi ( | z _ { n + j } | ) z _ { n + j } .
$$

Approximating $\psi ( | z _ { n + j } | )$ with $\psi ( 1 ) = - \omega ^ { 2 }$ ,wegeta linear recurrence relation with characteristic polynomial

$$
S ( \omega h , \zeta ) = \rho ( \zeta ) + \omega ^ { 2 } h ^ { 2 } \sigma ( \zeta ) .
$$

![](images/eba4afd5087cba56b5e16feb3b9e80de01521d2288d83999672eceb749736b66.jpg)  
Fig.7.1.Maximumerrorin the total energy during the integration of 25ooorbits of the Kepler problemasa function of the number of steps per period

Theprincipal roots of $S ( \omega h , \zeta ) = 0$ satisfy $\zeta _ { 1 } ( \omega h ) \approx e ^ { i \omega h }$ and $\zeta _ { 2 } ( \omega h ) \approx e ^ { - i \omega h }$ , andwehave|S(wh）|=1forall $\mathcal { I }$ and for sufficiently small $h$ ,because the method issymmetric(Exercise2).As a consequence of $| \zeta _ { 1 } ( \omega h ) | = 1$ ,thevalues $\widehat { z } _ { n } : =$ $\zeta _ { 1 } ( \omega h ) ^ { n }$ arenot only a solution of the linear recurrence relation,but also of the nonlinearrelation(7.3).Ouraim is to study the stability of this numerical solution. Wetherefore consideraperturbed solution

$$
z _ { n } = \zeta _ { 1 } ( \omega h ) ^ { n } \big ( 1 + u _ { n } \big ) .
$$

Using $\begin{array} { r } { | z _ { n } | = 1 + \frac { 1 } { 2 } ( u _ { n } + \overline { { u } } _ { n } ) + \mathcal { O } ( | u _ { n } | ^ { 2 } ) } \end{array}$ and neglecting thequadratic and higher order terms of $\left| u _ { n } \right|$ in the relation（7.3）,we get

$$
\sum _ { j = 0 } ^ { k } ( \alpha _ { j } + \omega ^ { 2 } h ^ { 2 } \beta _ { j } ) \zeta _ { 1 } ( \omega h ) ^ { j } u _ { n + j } = \frac { h ^ { 2 } } { 2 } \psi ^ { \prime } ( 1 ) \sum _ { j = 0 } ^ { k } \beta _ { j } \zeta _ { 1 } ( \omega h ) ^ { j } \big ( u _ { n + j } + \overline { { u } } _ { n + j } \big ) .
$$

Considering alsothecomplex conjugate of thisrelation,and eliminating $u _ { n + j }$ ,we obtaina linearrecurrencerelation for $u _ { n }$ -with characteristic polynomial

$$
S ( \omega h , \zeta _ { 1 } ( \omega h ) \zeta ) \cdot S ( \omega h , \zeta _ { 1 } ( \omega h ) ^ { - 1 } \zeta ) + \mathcal { O } ( h ^ { 2 } ) .
$$

Forsmall $h$ ,its zeros are close to $\zeta _ { 1 } ( \omega h ) ^ { - 1 } \zeta _ { j }$ and $\zeta _ { 1 } ( \omega h ) \zeta _ { l } .$ If two of these zeros collapse,the $\mathcal { O } ( h ^ { 2 } )$ termsin(7.4） can producea root of modulus larger than one, sothat instability occurs.Thisis the case,if two roots $\zeta _ { j }$ , $\zeta _ { l }$ of $\rho ( \zeta ) = 0$ satisfy $\zeta _ { j } \zeta _ { l } ^ { - 1 } \approx \zeta _ { 1 } ^ { 2 } \approx e ^ { 2 i \omega h }$ ,or

$$
\theta _ { j } - \theta _ { l } = \frac { 4 \pi } { N } ,
$$

where $\zeta _ { j } = e ^ { 2 \theta _ { j } }$ and $h = 2 \pi / N$

For theMethod SY8 of Table7.1,thespurious zeros of $\rho ( \zeta )$ have arguments $\pm 4 \pi / 5 , \pm 2 \pi / 5$ ,and $\pm 2 \pi / 6$ With $\theta _ { j } = 2 \pi / 5$ and $\theta _ { l } = 2 \pi / 6$ ,the condition (7.5) gives $N = 6 0$ asacandidate for instability.This explains the experiment ofFig.7.1 for $e = 0$ Astudy of the stability of orbitswith eccentricity $e \neq 0$ (seeQuinlan

![](images/71bf1f4464c0192b6680122bb469f30fc09f60544279a6e3cc996a226e5348c8.jpg)  
Fig.7.2.Maximumerrorin the total energyduring theintegration of 25oo orbits of the Kepler problemasa function of thenumber ofstepsperperiod

1999)shows that instabilities can also occur when $4 \pi / N$ isreplaced with $2 q \pi / N$ $\mathbf { \Phi } _ { q } = 2 , 3 , \ldots )$ in therelation(7.5）.

Toavoid these instabilities as faras possible,Quinlan(1999) constructed symmetric multistep methods,where the spurious roots of $\rho ( \zeta ) = 0$ arewell spread out on the unit circle and far from $\zeta = 1$ Asaresult he proposes Method SY8B ofTable7.1.The same experimentasaboveyieldstheresultsofFig.7.2.The $\rho$ polynomial ofMethodSY8Bis

$$
\rho ( \zeta ) = ( \zeta - 1 ) ^ { 2 } \big ( \zeta ^ { 6 } + 2 \zeta ^ { 5 } + 3 \zeta ^ { 4 } + 3 . 5 \zeta ^ { 3 } + 3 \zeta ^ { 2 } + 2 \zeta + 1 \big ) ,
$$

and the $\theta _ { j }$ of the spurious roots are $\pm 2 \pi / 2 . 2 7 8$ , $\pm 2 \pi / 3 . 3 5 3$ ,and $\pm 2 \pi / 4 . 6 7 8$ The condition(7.5） is satisfied only for $N \leq 2 3 . 6 7 $ which implies that no instability occurs for $e = 0$ in the region of the experiment of Fig.7.2.

Toillustratethe importance of high order methods,we included in Fig.7.2 the results of the second order partitioned multistep method(1.15).

# XV.7.2Extension to Variable Step Sizes

Variable step size multistep methods for second order differential equations ${ \ddot { y } } =$ $f ( y )$ are of the form

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) y _ { n + j } = h _ { n + k - 1 } ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) f ( y _ { n + j } ) ,
$$

where the coefficients $\alpha _ { j }$ and $\beta _ { j }$ are allowed to depend on the step sizes $h _ { n } , \ldots$ , $h _ { n + k - 1 }$ ,moreprecisely,on theratios $h _ { n + 1 } / h _ { n } , \ldots , h _ { n + k - 1 } / h _ { n + k - 2 } ,$ Theyyield approximations $y _ { n }$ to $y ( t _ { n } )$ ona variable grid given by $t _ { n + 1 } = t _ { n } + h _ { n }$ Sucha method isoforder $r$ (cf.formula(1.9））,if

$$
\sum _ { i = 0 } ^ { k } \alpha _ { j } ( h _ { n , \cdots } , h _ { n + k - 1 } ) y ( t _ { n + j } ) = h _ { n + k - 1 } ^ { 2 } \sum _ { j = 0 } ^ { k } \beta _ { j } ( h _ { n , \cdots } , h _ { n + k - 1 } ) \ddot { y } ( t _ { n + j } )
$$

forall polynomials $y ( t )$ ofdegree $\leq r + 1 .$ It is stable,if the $\rho$ -polynomialwith coefficients $\alpha _ { j } ( h , \ldots , h )$ (constant step size） satisfies the stability condition of Sect.XV.1.2(seeTheoremII.5.7ofHairer,Ngrsett&Wanner（1993）andCano &Duran(2003a)）.

All methods of Sect.XV.7.1 can be extended to symmetric,variable step size integrators.This hasbeen discovered by Cano&Duran(2Oo3b).Forclarity of notationwe let $\widetilde { \alpha } _ { j } , \beta _ { j }$ $\mathbf { \phi } _ { j } = 0 , \ldots , k )$ be the coefficients of such a fixed step size method. Cano $\&$ Duran propose putting

$$
\beta _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } ) = \frac { h _ { n } } { h _ { n + k - 1 } } \widetilde { \beta } _ { j } ,
$$

and to determine $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that symmetry and order $k - 2$ (for arbitrary step sizes）are achieved.We also suppose(7.7),butwedetermine the coefficients $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that (7.6) holds forall polynomials $y ( t )$ of degree $\le ~ k$ .Thisuniquely determines these coeficients whenever $h _ { n } > 0 , \ldots$ $h _ { n + k - 1 } > 0$ (Vandermonde type system)and gives the following properties.

Lemma7.1.Foreven $k$ ，let $( \widetilde { \alpha } _ { j } , \widetilde { \beta } _ { j } )$ definea symmetric,stable $k$ -stepmethod (1.8）oforder $k$ ,andconsider thevariable step sizemethod givenby(7.7）and $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ such that(7.6)holds forall polynomials $_ y$ satisfying $\deg y \leq$ $k$ Thismethodextendsthefixedstep sizeformula,i.e.,

$$
\alpha _ { j } ( h , \ldots , h ) = \widetilde { \alpha } _ { j } , \qquad \beta _ { j } ( h , \ldots , h ) = \widetilde { \beta } _ { j } ,
$$

itsatisfiesthesymmetry relations

$$
\begin{array} { c } { { \alpha _ { j } ( h _ { n } , . . . , h _ { n + k - 1 } ) ~ = ~ \alpha _ { k - j } ( h _ { n \pm k = 1 } , . . . , h _ { n } ) } } \\ { { { h } _ { n + k - 1 } ^ { 2 } \beta _ { j } ( h _ { n } , . . . , h _ { n + k - 1 } ) ~ = ~ h _ { n } ^ { 2 } \beta _ { k - j } ( h _ { n + k - 1 } , . . . , h _ { n } ) , } } \end{array}
$$

and it isof order $k - 1$ forarbitrarystepsizes.Moreover,itbehaves likeamethod oforder $k$ if $h _ { n + 1 } = h _ { n } { \big ( } 1 + { \mathcal { O } } ( h _ { n } ) { \big ) }$ uniformly in $n$

Proof.Therelation (7.8) for $\beta _ { j }$ follows at once from(7.7）,and for $\alpha _ { j }$ itisaconsequenceof the uniquenessof the solution ofthe linear system for the $\alpha _ { j }$

The second condition of(7.9） follows directly from(7.7）and from the symmetryof theunderlying fixed step size method $\beta _ { k - j } = \beta _ { j }$ forall $\jmath$ ).Inserting （7.7）into （7.6）,replacing $y ( t )$ with $y ( t _ { n + k } + t _ { n } - t )$ ,and reversing the order of $h _ { n } , \ldots , h _ { n + k - 1 }$ yields

$$
\sum _ { j = 0 } ^ { k } \alpha _ { j } ( h _ { n + k - 1 } , \ldots , h _ { n } ) y ( t _ { n + k - j } ) = h _ { n } h _ { n + k - 1 } \sum _ { j = 0 } ^ { k } \widetilde { \beta } _ { j } \ddot { y } ( t _ { n + k - j } ) .
$$

Using $\beta _ { k - j } = \beta _ { j }$ this shows that $\alpha _ { k - j } ( h _ { n + k - 1 } , . . . , h _ { n } )$ satisfies exactly the same linear systemas $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ ,sothatalso the firstrelationof(7.9)is verified.

Bydefinition,thevariable step sizemethod isat least of order $k - 1$ Under the assumption $h _ { n + 1 } = h _ { n } { \big ( } 1 + { \mathcal { O } } ( h _ { n } ) { \big ) }$ the defect in(7.6)is of the form

$$
h _ { n } ^ { k + 1 } D ( h _ { n } , \ldots , h _ { n + k - 1 } ) = h _ { n } ^ { k + 1 } D ( h _ { n } , \ldots , h _ { n } ) + { \mathcal O } ( h _ { n } ^ { k + 2 } )
$$

forall sufficiently smooth $y ( t )$ Since the constant step size method is of order $k$ , theexpression $D ( h _ { n } , \ldots , h _ { n } )$ is of size $\mathcal { O } ( h _ { n } )$ ,so that we observe convergence of order $k$ . □

Thesymmetry relation(7.9） has the following interpretation:if the approximations $y _ { n } , \ldots , y _ { n + k - 1 }$ used with step sizes $h _ { n } , \ldots , h _ { n + k - 1 }$ yield $y _ { n + k }$ ,thenthe values $y _ { n + k } , \ldots , y _ { n + 1 }$ appliedwith $h _ { n + k - 1 } , \ldots , h _ { n }$ yield $y _ { n }$ asaresult （since the only on coefficients $h _ { n + k - 1 } ^ { 2 }$ $\alpha _ { j }$ and thesameresultisobtainedwith only depend on step sizeratios and the multistep formula $- h _ { n + k - 1 } , \ldots , - h _ { n } ) .$ Thisisthe analogue of the definition of symmetry for one-step methods.

Forobtaininga good long-time behaviour,the stepsizesalso have to be chosen inasymmetricand reversible way (see Sect.VII.3).One possibility isto take step sizes

$$
h _ { n + k - 1 } = \frac { \varepsilon } { 2 } \Big ( \sigma ( y _ { n + k - 1 } ) + \sigma ( y _ { n + k } ) \Big ) ,
$$

where $\varepsilon > 0$ ,and $\sigma ( y )$ is a given positive monitor function.This condition is an implicit equation for $h _ { n + k - 1 }$ ,because $y _ { n + k }$ dependson $h _ { n + k - 1 } .$ It has to be solved iteratively.Notice,however,that foran explicitmultistepformula no further force evaluations are necessaryduring this iteration.Such achoice of the step sizeguarantees that whenever $h _ { n + k - 1 }$ is chosen when stepping from $y _ { n } , \ldots , y _ { n + k - 1 }$ with $h _ { n } , \ldots , h _ { n + k - 2 }$ to $y _ { n + k }$ ,the step size $h _ { n }$ ischosen when stepping backwards from $y _ { n + k } , \ldots , y _ { n + 1 }$ with $h _ { n + k - 1 } , \ldots , h _ { n + 1 }$ to $y _ { n }$

Implementation.For given initial values $y _ { 0 } , \dot { y } _ { 0 }$ ,the starting approximations $y _ { 1 }$ ， $\cdots , y _ { k - 1 }$ should be computed accurately (forexample,bya high-orderRunge-Kutta method） with step sizes satisfying(7.1O).The solution of the scalar nonlinearequation（7.1O）has to be donecarefullyin order toreduce the overhead of the method.In our code we use $h _ { n + k - 1 } : = h _ { n + k - 2 } ^ { 2 } / h _ { n + k - 3 }$ as predictor,and we apply modified Newton iterationswith thederivativeapproximated by finitedifferences.

The coefficients $\alpha _ { j } ( h _ { n } , \ldots , h _ { n + k - 1 } )$ have to becomputed anewin every iteration.We use the basis

$$
p _ { i } ( t ) = \prod _ { j = 0 } ^ { i - 1 } ( t - t _ { n + j } ) _ { \ast } \qquad i = 0 , \dots , k
$$

for the polynomials of degree $\le \ k$ in(7.6).This leads toa linear triangular system for $\alpha _ { 0 } , \ldots , \alpha _ { k }$ Asnoticed by Cano&Duran(20o3b),thecoefficients $p _ { i } ( t _ { j } )$ and $\ddot { p } _ { i } ( t _ { j } )$ can be obtained efficiently from the recurrence relations

$$
\begin{array} { r l } { p _ { 0 } ( t ) = 1 , \quad } & { p _ { i + 1 } ( t ) = ( t - t _ { i } ) p _ { i } ( t ) } \\ { \dot { p } _ { 0 } ( t ) = 0 , \quad } & { \dot { p } _ { i + 1 } ( t ) = ( t - t _ { i } ) \dot { p } _ { i } ( t ) + p _ { i } ( t ) } \\ { \ddot { p } _ { 0 } ( t ) = 0 , \quad } & { \ddot { p } _ { i + 1 } ( t ) = ( t - t _ { i } ) \ddot { p } _ { i } ( t ) + 2 \dot { p } _ { i } ( t ) . } \end{array}
$$

![](images/8e83bddd30fc52f67ee122def73b11fdf26a0ee184d88a119335cc14599b3012.jpg)  
Fig.7.3.Maximumerrorinthe total energyduring theintegrationof 25oOorbits of the Kepler problemasa function of the number of stepsper period

During the iterations for the solution of the nonlinear equation(7.1O) only the values of $p _ { i } ( t _ { n + k } )$ have to beupdated.

Numerical Experiment.Werepeat the experiment of Fig.7.1 with the method SY8,but this time in the variable step size version and with $\sigma ( y ) = \| y \| ^ { 2 }$ asstep sizemonitor.We have computed 25oO periods of the Kepler problem with eccentricity $e = 0 . 2$ ,andwehaveplottedinFig.7.3 themaximal error in theHamiltonian asafunction of the number of steps per period (for a comparison we have also included the result of the fixed step sizeimplementation).Similar to(7.2） we use approximations $\dot { y } _ { n }$ thatare the derivative of the interpolation polynomial passing through $y _ { n } , y _ { n \pm 1 } , y _ { n \pm 2 } , . . .$ such that the correct order is obtained.The computationis stopped when the error exceeds $1 0 ^ { - 2 }$ .

Asexpected,the errorissmaller for the variablestep size version,and it is seen that the peaks due to numerical resonances are now much less although they are notcompletely removed.Forlarge step sizes,the performance deteriorates,but this isnota seriousproblem,because these methods are recommended only for high accuracy computations.

It should be remarked that the overhead,due to the computation of the coefficients $\alpha _ { j }$ and the solution of the nonlinearequation(7.1O),is rather high.Therefore, theuse of variable step sizes is recommended only when force evaluations $f ( y )$ are expensive or when constant step sizesare not appropriate.Cano&Duran（2003b) reportan excellent performance of symmetric,variable step size multistep methods forcomputations of the outer solar system.

Despite the resonances and instabilities,then,symmetric methods can stillbea better choice than Stormer methods forlong integrations of planetaryorbits provided that the user isaware of the dangers.

(G.D.Quinlan 1999)

# XV.8Multi-Value or General Linear Methods

General linear methodsisa class of integration methods that coversRunge-Kutta aswell as multistep methods.It is therefore of interest to study which of the results onthe long-time behaviour can be extended.

So-called multi-value or general linearmethodsare defined by $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ where

$$
\begin{array} { l c l } { { Y _ { n + 1 } } } & { { = } } & { { D Y _ { n } + h B f ( U _ { n + 1 } ) } } \\ { { } } & { { } } & { { } } \\ { { U _ { n + 1 } } } & { { = } } & { { C Y _ { n } + h A f ( U _ { n + 1 } ) } } \end{array}
$$

with $f ( U _ { n + 1 } ) = \left( f ( u _ { n + 1 } ^ { 1 } ) , \ldots , f ( u _ { n + 1 } ^ { s } ) \right) ^ { T }$ for $U _ { n + 1 } = \left( u _ { n + 1 } ^ { 1 } , \ldots , u _ { n + 1 } ^ { s } \right) ^ { T } ,$ and $Y _ { n } = ( y _ { n } ^ { 1 } , \dots , y _ { n } ^ { k } ) .$ Weuseasloppy notation inthe sense that the matrices $D , B , \ldots$ should be replaced with $\cal D \otimes \cal I , \cal B \otimes \cal I , . . .$ .Foracomputation,a starting procedure $S _ { h }$ anda finishing procedure $F _ { h }$ ,which extracts the numerical approximation $y _ { n }$ from $Y _ { n } ,$ haveto beadded(seeFig.8.1）.Weassume theexistence ofavector $e$ such thatwith $\mathbb { 1 } = ( 1 , \ldots , 1 ) ^ { T }$

$$
D e = e , \qquad C e = 1 1
$$

holds (preconsistency conditions). The vector $Y _ { n }$ is then an approximation to $e y ( t _ { n } )$ (more precisely to $e \otimes y ( t _ { n } )$ ).

ForRunge-Kutta methods, $D = \mathbf { \tau } ( 1 )$ isthe one-dimensional identity, $B \ =$ $( b _ { 1 } , \dots , b _ { s } )$ , $C = \mathbb { I }$ ,and $A$ is theusual Runge-Kutta matrix.For multistep methods, wehave $Y _ { n } = ( y _ { n + k - 1 } , \dots , y _ { n } ) ^ { T }$ ,and $\mathcal { D }$ isthe $k \times k$ matrix with characteristic polynomial $\rho ( \zeta )$ asin(2.1）.Foradetailed treatment of general linearmethodswe referthe reader to Chap.4of themonograph of Butcher(1987),and to Chap.III.8 ofHairer,Norsett&Wanner（1993).

![](images/a617c7f9bf9720f3b801b9269991d7ed4e179b887367c015ac3bb49485ff5d0a.jpg)  
Fig.8.1.Illustration of a multi-value method $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ with starting procedure $S _ { h }$ and finishing procedure $F _ { h }$

# XV.8.1 Underlying One-Step Method and Backward Error Analysis

Inanalogy to multistepmethods,amethod(8.1) iscalled strictly stable,if all eigenvalues of $D$ areinside the unit circle with the exception of the single eigenvalue $\zeta = 1$ .AnextensionofKirchgraber'sresult(Theorem2.1) to strictly stable general linearmethodsis given by Stoffer(1993).

Theorem8.1.Considerastrictly stable general linear method $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ anda finishing procedure $y _ { n } = F _ { h } ( Y _ { n } ) = d ^ { \cal { L } } Y _ { n } +$ $\mathcal { O } ( h )$ Assume that(8.2) and $d ^ { T } e = 1$ hold.

(i)Then there exist a unique one-step method $\varPhi _ { h } ( y )$ and a unique starting procedure $S _ { h } ( y )$ such that $G _ { h } \circ S _ { h } = S _ { h } \circ \phi _ { h }$ and $F _ { h } \circ S _ { h } = I d$ hold.

![](images/f763688748fb569b8f8c9073cc4820df3956e06dda0b6587ab9d29013384e74c.jpg)

(ii)The manifold $\mathcal { M } _ { h } \ = \ \{ S _ { h } ( y ) ; y \in \mathbb { R } ^ { d } \}$ is invariant under $G _ { h } ,$ anditis exponentiallyattractive.

Proof.Since themethod isstrictlystable,thereexistsamatrix $_ { x }$ such that

$$
\begin{array} { r } { T ^ { - 1 } D T = \left( \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { D _ { 0 } } \end{array} \right) \qquad \mathrm { w i t h } \quad \left. D _ { 0 } \right. < 1 , } \end{array}
$$

and $T e _ { 1 } = e$ (where $e _ { 1 } = ( 1 , 0 , \ldots , 0 ) ^ { T } )$ .Theproof closely followsthat of Theorem 2.1.With the transformation $( \xi _ { n } , \eta _ { n } ) ^ { I } \ = Z _ { n } = { T } ^ { - 1 } Y _ { n }$ ,thegeneral linear method（8.1） becomes

$$
\left( \begin{array} { c } { \xi _ { n + 1 } } \\ { \eta _ { n + 1 } } \end{array} \right) = \left( \begin{array} { c } { \xi _ { n } } \\ { D _ { 0 } \eta _ { n } } \end{array} \right) + h T ^ { - 1 } B f ( U _ { n + 1 } ) .
$$

with $U _ { n + 1 } = C T Z _ { n } + h A f ( U _ { n + 1 } ) .$ Asbefore,TheoremXII.3.1canbeapplied and yields the existence of an atractive manifold $\mathcal { N } _ { h } = \{ ( \xi , s ( \xi ) ) ; \xi \in \mathbb { R } ^ { d } \}$ ,whichis invariant underthemapping(8.3).We now invert the restriction of $F _ { h }$ onto the manifold ${ \mathcal { N } } _ { h } .$ Due to $d ^ { 2 } e = 1$ and $T e _ { 1 } = e$ ,wehave for $Z = Z ( \xi ) = \left( \xi , s ( \xi ) \right) ^ { T }$ that

$$
y = F _ { h } \big ( T Z ( \xi ) \big ) = d ^ { T } T Z ( \xi ) + \ldots = \xi + g ( \xi ) ,
$$

where $g ( \xi )$ isLipschitz continuous with constant $\mathcal { O } ( h )$ Bythe Banach fixed-point theorem the equation(8.4) has a unique solution $\xi = r ( y )$ Putting

$$
S _ { h } ( y ) = T Z \big ( r ( y ) \big ) = T \left( { r ( y ) } \atop { s \big ( r ( y ) \big ) } \right) ,
$$

wehave found the unique starting procedure satisfying $F _ { h } \circ S _ { h } \ : = \ : I d$ and $T ^ { - 1 } S _ { h } ( y ) \in { \mathcal { N } } _ { h } .$ Wefinally define $\phi _ { h } = F _ { h } \circ G _ { h } \circ S _ { h }$ and $\mathcal { M } _ { h } = \{ T Z \} , Z \in \mathcal { N } _ { h } \}$ , sothatall statements of the theoremareverified. □

Itis our aim to extend the concept of an underlying one-step method to nearly all(includingweakly stable) general linear methods.

Theorem8.2.Considera general linear method(8.1),and assume that $\zeta ~ = ~ 1$ isasingle eigenvalue of the propagation matrix $D$ Furthermore,let $G _ { h } ( Y )$ and $F _ { h } ( Y ) = d ^ { T } Y + \ldots$ have expansions in powers of $h$ andassume that(8.2)and $d ^ { T } e = 1$ hold.Then there exist auniqueformal one-stepmethod

$$
\Phi _ { h } ( y ) = y + h d _ { 1 } ( y ) + h ^ { 2 } d _ { 2 } ( y ) + \dots .
$$

andaunique formal startingprocedure

$$
S _ { h } ( y ) = e y + h S _ { 1 } ( y ) + h ^ { 2 } S _ { 2 } ( y ) + \dots ,
$$

such that formally $G _ { h } \circ S _ { h } = S _ { h } \circ \phi _ { h }$ and $F _ { h } \circ S _ { h } = I d$ hold.

Proof.Expanding $S _ { h } \left( \varPhi _ { h } ( y ) \right)$ and $G _ { h } ( S _ { h } ( y ) )$ into powers of $h$ ,acomparison of the coefficients yields

$$
e d _ { j } ( y ) + ( I - D ) S _ { j } ( y ) = \ldots ,
$$

wherearight-hand side depends on known functions and on $d _ { i } ( y ) , S _ { i } ( y )$ with $i < j$ . Similarly,the condition $F _ { h } \big ( S _ { y } ( y ) \big ) = y$ leadsto

$$
d ^ { T } S _ { j } ( y ) = \cdots .
$$

Due to the fact that $\zeta = 1$ isa single eigenvalue of $\mathcal { D }$ ,and that $d ^ { 1 } e \neq 0$ ,thesystem (8.5)-(8.6)uniquely determines $d _ { j } ( y )$ and $S _ { j } ( y )$ . □

Backward ErrorAnalysis forSmooth Numerical Solutions.The formal analysisof Chap.IX can bedirectly applied to theunderlying one-stepmethod of Theorem8.2.Thisyieldsa modified differential equation,but only for the smooth numerical solution (cf.Sect.XV.3.1).Notice that this modified equationdepends on the choice of the finishing procedure $F _ { h }$

# XV.8.2Symplecticity and Symmetry

Before givingaprecise meaning to thesymplecticityand symmetry of general linear methods,we establish the following lemma.

Lemma 8.3.Fora general linearmethod $Y _ { n + 1 } = G _ { h } ( Y _ { n } )$ we considertwo different finishing procedures $y _ { n } = F _ { h } ( Y _ { n } )$ and $\widehat { y } _ { n } = \widehat { F } _ { h } ( Y _ { n } )$

$$
\begin{array} { r c l } { { \widehat { y } _ { 0 } \quad \displaystyle \longrightarrow \quad \widehat { \Phi } _ { h } \quad \ } } & { { \widehat { y } _ { 1 } \quad \displaystyle \longrightarrow \quad \widehat { \Phi } _ { h } \quad } } & { { \widehat { y } _ { 2 } \quad \displaystyle \stackrel { \widehat { \Phi } _ { h } } { \longrightarrow } \quad \cdots } } \\ { { \widehat { S } _ { h } \left\downarrow \right. \widehat { F } _ { h } } } & { { \displaystyle \uparrow \widehat { F } _ { h } } } & { { \displaystyle \uparrow \widehat { F } _ { h } } } \\ { { Y _ { 0 } \quad \displaystyle \longrightarrow \quad \widehat { G } _ { h } \quad \displaystyle \longrightarrow \quad Y _ { 1 } \quad \displaystyle \xrightarrow [ { { G } _ { h } } ] { G _ { h } } \quad Y _ { 2 } \quad \displaystyle \xrightarrow [ { G } ] { G _ { h } } \quad \cdots } } \\ { { S _ { h } \left\uparrow \right. F _ { h } } } & { { \displaystyle \downarrow \ F _ { h } } } & { { \displaystyle \downarrow \ F _ { h } } } \\ { { y _ { 0 } \quad \displaystyle \longrightarrow \quad y _ { 1 } \quad \displaystyle \longrightarrow \quad y _ { 1 } \quad \displaystyle \longrightarrow \quad y _ { 2 } \quad \displaystyle \xrightarrow [ { \Phi } ] { \Phi _ { h } } \quad \displaystyle } } & { { \displaystyle \cdots } } \end{array}
$$

The two corresponding one-step methods $\varPhi _ { h } ( y )$ and $\widehat { \varPhi } _ { h } ( y )$ (given by Theorem8.2)are then conjugate to each other,i.e,

$$
\alpha _ { h } ^ { - 1 } \circ \varPhi _ { h } \circ \alpha _ { h } = \widehat { \Phi } _ { h } \qquad w i t h \qquad \alpha _ { h } = F _ { h } \circ \widehat { S } _ { h } .
$$