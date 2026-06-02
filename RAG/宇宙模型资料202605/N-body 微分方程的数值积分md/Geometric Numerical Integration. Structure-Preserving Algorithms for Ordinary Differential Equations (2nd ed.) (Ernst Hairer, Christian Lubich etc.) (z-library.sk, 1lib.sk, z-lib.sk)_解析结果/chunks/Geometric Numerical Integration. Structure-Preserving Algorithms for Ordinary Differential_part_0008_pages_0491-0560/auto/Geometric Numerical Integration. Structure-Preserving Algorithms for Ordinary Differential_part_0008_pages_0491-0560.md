underlying the construction of the methods and leave numerical comparisons to Sect.XII.2 and the analysis of the methods to SectionsXII.3-XII.6.We consider onlymethods that are symmetric or symplectic.The presentation in this section follows roughly the chronological order.

# XIII.1.1 TheStormer-Verlet Method vs.Multiple Time Scales

Perhaps the most widely used method of integrating the equations of motionis that initiallyadoptedbyVerlet（1967）andattributed to Stormer. (M.P.Allen&D.J.Tildesley1987,p.78)

The Newtonian equations of motion of particle systems (in molecular dynamics, astrophysics and elsewhere)are second-order differential equations

$$
\ddot { q } = - \nabla V ( q ) .
$$

Tosimplify the presentation,we omit the positive definite mass matrix $M$ which wouldusuallymultiply $\ddot { q }$ .Thisentails no loss of generality,since a transformation $q \to M ^ { 1 / 2 } q$ and $V ( q ) \to V ( M ^ { - 1 / 2 } q )$ gives the very form(1.1).

Thestandard numerical integrator of moleculardynamics is the Stormer-Verlet scheme;see Chap.I.We recallthat this method computes the new positions $q _ { n + 1 }$ at time $t _ { n + 1 }$ from

$$
q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = h ^ { 2 } f _ { n }
$$

with the force $f _ { n } = - \nabla V ( q _ { n } ) .$ Velocityapproximationsare given by

$$
\dot { q } _ { n } = \frac { q _ { n + 1 } - q _ { n - 1 } } { 2 h } .
$$

Inits one-step formulation(see(I.1.17))the method reads1

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 / 2 } ~ = ~ p _ { n } + \frac { 1 } { 2 } h f _ { n } } } \\ { { } } & { { } } & { { q _ { n + 1 } ~ = ~ q _ { n } + h p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } ~ = ~ p _ { n + 1 / 2 } + \frac { 1 } { 2 } h f _ { n + 1 } ~ . } } \end{array}
$$

Werecall that thisisa symmetricand symplectic method of order2.Forlinear stability,i.e.,for bounded error propagationin linearized equations,the step size must be restricted to

$$
h \omega < 2
$$

where $\boldsymbol { \omega }$ isthe largest eigenfrequency (i.e.,square root of an eigenvalue) of the Hessian matrix $\nabla ^ { 2 } V ( q )$ along the numerical solution;see Sect.I.5.1.Good energy conservationrequires aneven strongerrestriction onthe step size.Valuesof $h \omega \approx \frac { 1 } { 2 }$ arefrequentlyused inmoleculardynamics simulations.

The potential $V ( q )$ is oftena sum of potentials that act on different time scales,

$$
V ( q ) = W ( q ) + U ( q ) \qquad \mathrm { w i t h } \qquad \nabla ^ { 2 } W ( q ) \mathrm { p o s i t i v e s e m i - d e f }
$$

Inthis situation,solutions arein general highly oscillatory on the slow time scale $\tau \sim 1 / \lVert \nabla ^ { 2 } U ( q ) \rVert ^ { 1 / 2 } ,$

In particular when the fast forces $- \nabla W ( q )$ are cheaper to evaluate than the slow forces $- \nabla U ( q )$ ,itis of interest to devise methodswhere the required number ofslow-force evaluations is not (or not severely）affected by the presence of the fastforces which are responsible for the oscillatory behaviour and which restrict thestep size of standard integrators like the Stormer-Verlet scheme.This situation occurs in molecular dynamics,where $W ( q )$ corresponds to short-range molecular bonds,whereas $U ( q )$ includes inter alia long-range electrostaticpotentials.

Insome approaches to this computational problem,the differential model is modified: highly oscillatory components are replaced by constraints (Ryckaert, Ciccotti&Berendsen 1977),or stochastic and dissipative termsareadded to the model (see Schlick 1999).Such modifications may prove highly successful in some applications.In the following,however,we restrict our attention to methodswhich aim atlong time stepsdirectly for theproblem(1.1）with(1.4).

Spatial semi-discretizations of nonlinear wave equations,such as the sine-Gordon equation

$$
u _ { t t } = u _ { x x } - \sin u ,
$$

form another important class of equations (1.1) with (1.4).Here $\begin{array} { r } { W ( q ) = \frac { 1 } { 2 } q ^ { T } A q } \end{array}$ where $A$ is the discretizationmatrix ofthe differential operator $- \partial ^ { 2 } / \partial x ^ { 2 }$ ..

# XIII.1.2 Gautschi’sand Deuflhard's TrigonometricMethods

Itisanticipated that trigonometric methods can be applied,with similarsuccess,also to nonlineardifferential equations describing oscillation phenomena. (W.Gautschi 1961)

The oldest methodsallowing the use of long time steps in oscillatory problems concern the particular case of aquadratic potential $\begin{array} { r } { W ( q ) = \frac 1 2 \omega ^ { 2 } q ^ { T } q } \end{array}$ with $\omega \gg 1$ ,for which the equations take the form

$$
\ddot { q } = - \omega ^ { 2 } q + g ( q ) .
$$

For such equations,Gautschi (1961） proposed a number of methods of multistep typewhich are constructed to be exact if the solution isa trigonometric polynomial in $\omega t$ ofaprescribed degree.The simplest of these methods(and the only symmetric one)reads

$$
q _ { n + 1 } = 2 q _ { n } + q _ { n - 1 } = h ^ { 2 } \operatorname { s i n c } ^ { 2 } ( { \textstyle { \frac { 1 } { 2 } } } h \omega ) \ddot { q } _ { n } ,
$$

where sinc $\xi = \sin \xi / \xi$ and $\ddot { q } _ { n } = - \omega ^ { 2 } q _ { n } + g _ { n }$ with $g _ { n } = g ( q _ { n } )$ ,or equivalently

$$
q _ { n + 1 } - 2 \cos ( h \omega ) q _ { n } + q _ { n - 1 } = h ^ { 2 } \sin \mathrm { c } ^ { 2 } ( { \frac { 1 } { 2 } } h \omega ) g _ { n } .
$$

The method gives the exact solution for equations (1.5）with $g = C o n s t$ and arbitrary $\omega$ (see also Hersch (1958) for such a construction principle).This property is readily verified with thevariation-of-constants formula

$$
\begin{array} { r c l } { { \left( \begin{array} { c } { { q ( t ) } } \\ { { \dot { q } ( t ) } } \end{array} \right) } } & { { = } } & { { \displaystyle \left( \begin{array} { c c } { { \cos t \omega } } & { { \omega ^ { - 1 } \sin t \omega } } \\ { { - \omega \sin t \omega } } & { { \cos t \omega } } \end{array} \right) \left( \begin{array} { c } { { q _ { 0 } } } \\ { { \dot { q } _ { 0 } } } \end{array} \right) } } \\ { { } } & { { } } & { { + \displaystyle \int _ { 0 } ^ { t } \left( \begin{array} { c } { { \omega ^ { - 1 } \sin ( t - s ) \omega } } \\ { { \cos ( t - s ) \omega } } \end{array} \right) g \big ( q ( s ) \big ) d s . } } \end{array}
$$

Thisformula also shows that the following scheme foravelocity approximation becomes exact for $g = C o n s t$ :

$$
\dot { q } _ { n + 1 } - \dot { q } _ { n - 1 } = 2 h \operatorname { s i n c } ( h \omega ) \ddot { q } _ { n } .
$$

Starting values $q _ { 1 }$ and $\dot { q } _ { 1 }$ are also obtained from(1.8)with $g ( q _ { 0 } )$ in place of $g ( q ( s ) )$

Deuflhard（1979)considered $h ^ { 2 }$ -extrapolation based on the explicit symmetric method that is obtained byreplacingthe integral termin（1.8)by its trapezoidal rule approximation:

$$
h \dot { q } _ { n + 1 } \bigg ) = \binom { \cos h \omega } { - h \dot { \omega } \sin h \omega } \quad \stackrel { \mathrm { s i n c } \ : h \omega } { \cos h \omega } \bigg ) \binom { q _ { n } } { h \dot { q } _ { n } } + \frac { h ^ { 2 } } { 2 } \left( \operatorname* { s i n c } _ { g _ { n + 1 } + \cos ( h \omega ) } g _ { n } \right)
$$

Eliminatingthevelocitiesyieldsthe two-step formulation

$$
q _ { n + 1 } - 2 \cos ( h \omega ) q _ { n } + q _ { n - 1 } = h ^ { 2 } \operatorname { s i n c } ( h \omega ) g _ { n } .
$$

Thevelocity approximation is obtained back from

$$
2 h \operatorname { s i n c } ( h \omega ) \dot { q } _ { n } = q _ { n + 1 } - q _ { n - 1 }
$$

oralternatively from

$$
\dot { q } _ { n + 1 } - 2 \cos ( h \omega ) \dot { q } _ { n } + \dot { q } _ { n - 1 } = h ^ { 2 } \frac { g _ { n + 1 } - g _ { n - 1 } } { 2 h } .
$$

Both Gautschi'sand Deuflhard's method reduce tothe Stormer-Verlet scheme for $\omega = 0$ Bothmethods extend ina straightforward way to systems

$$
\ddot { q } = - A q + g ( q )
$$

withasymmetric positive semi-definite matrix $A$ ,byformallyreplacing $\boldsymbol { \omega }$ by $\varOmega = A ^ { 1 / 2 }$ intheabove formulas.The methods then require the computation of products of entire functions of the matrix $h ^ { 2 } A$ with vectors.This can be done by diagonalizing $A$ ,which is efficient for problemsof small dimension orin spectral methods for nonlinear wave equations.In high-dimensional problems where adiagonalization is not feasible,these matrix function times vector products can beefficiently computed by superlinearly convergent Krylov subspace methods,see Druskin&Knizhnerman（1995)and Hochbruck& Lubich（1997).

The above methods permit extensions to more general problems(1.1) with(1.4), but this requires areinterpretation to which we turn next.

# XIII.1.3 The Impulse Method

Integrators based onr-RESPA[.] have led to considerable speed-up in theCPU time for large scale simulations ofbiomacromolecular solutions. Sincer-RESPA is symplectic such integratorsare very stable.

(B.J.Berne 1999)

TheStormerVerletmethod(1.3)canbeinterpretedasapproximatingthefow $\varphi _ { h } ^ { H }$ of the system with Hamiltonian $H ( p , q ) = T ( p ) + V ( q )$ with $T ( p ) = { \textstyle \frac { 1 } { 2 } } p ^ { I } p$ bythe symmetric splitting

$$
\varphi _ { h / 2 } ^ { V } \circ \varphi _ { h } ^ { T } \circ \varphi _ { h / 2 } ^ { V } \ : ,
$$

which involvesonly theflows of thesystemswith Hamiltonians $T ( p )$ and $V ( q )$ , which are trivial to compute;see Sect.II.5.

In the situation(1.4) ofa potential $V = W + U$ ,wemay insteaduseadifferent splitting of $H = ( T + W ) + U$ and approximate the flow $\varphi _ { h } ^ { H }$ of the system by

$$
\varphi _ { h / 2 } ^ { U } \circ \varphi _ { h } ^ { T + W } \circ \varphi _ { h / 2 } ^ { U } \ .
$$

Thisgives a method that was proposed in the context of moleculardynamics by Grubmuller,Heller,Windemuth $\&$ Schulten(1991) (their Verlet-I scheme)and by Tuckerman,Berne&Martyna(1992)(theirr-RESPA scheme).Following the terminology ofGarcia-Archilla,Sanz-Serna&Skeel(1999)we here referto thismethod astheimpulsemethod:

1.kick: set $\begin{array} { r } { p _ { n } ^ { + } = p _ { n } - \frac { 1 } { 2 } h \nabla U ( q _ { n } ) } \end{array}$ 1   
2. oscillate solve $\ddot { q } = - \nabla W ( q )$ with initial values $( q _ { n } , p _ { n } ^ { + } )$ over a time step $h$ to obtain $( q _ { n + 1 } , p _ { n + 1 } ^ { - } )$   
3.kick:set $\begin{array} { r } { p _ { n + 1 } = p _ { n + 1 } ^ { - } - \frac { 1 } { 2 } h \nabla U ( q _ { n + 1 } ) } \end{array}$

Step2must ingeneral becomputedapproximatelybya numerical integratorwith asmaller time step,which resultsin the multiple time stepping method thatwe encountered in Sect.VII.4.If the inner integratorissymplecticand symmetric,asit wouldbe for the natural choice of the Stormer-Verletmethod,then also the overall method is symplectic-as a composition of symplectic transformations,and it is symmetric-as a symmetric composition of symmetric steps.

It is interesting to note that the impulse method (with exact solution of step 2) reduces to Deuflhard's method in the case of aquadratic potential $\begin{array} { r } { W ( q ) = \frac { 1 } { 2 } q ^ { T } A q } \end{array}$ (Exercise1).

Though the method does allow larger step sizes than the Stormer-Verlet method inmolecular dynamics simulations,it isnot free from numerical diffculties.Biesadecki& Skeel（1993)andGarcia-Archilla etal.（1999）reportand in linearmodel problems analyze instabilities and numerical resonance phenomena when the product of the step size $h$ withaneigenfrequency $\omega$ of $\nabla ^ { 2 } W$ is nearan integral multiple of $\pi$

# XIII.1.4 The MollifiedImpulse Method

Wealso propose a nontrivial improvement of the impulse method that wecall the mollifed impulse method,forwhichsuperior stabilityand accuracyisdemonstrated. (B.Garcia-Archilla,J.M.Sanz-Serna&R.D.Skeel1999)

Difficulties with the impulse method can be intuitively seento come from two sources:the slow force $- \nabla U ( q )$ hasan effect only at the ends ofa timestep,but it does not enter into the oscillations in between;the slow force is evaluated,somewhat arbitrarily,at isolated points of the oscillatory solution.

Garcia-Archillaet al.(1999)propose to evaluate the slow forceat an averaged value $\overline { { { q } } } _ { n } = a ( q _ { n } )$ Theyreplace the potential $C ( q )$ by $U ( q ) = U ( a ( q ) )$ and hence the slow force $- \nabla U ( q )$ intheimpulsemethodbythemollified force

$$
- \nabla \overline { { { U } } } ( q ) = - a ^ { \prime } ( q ) ^ { T } \nabla U ( a ( q ) ) .
$$

Sincethismolified impulsemethodisthe impulsemethod foramodified potential, it isagainsymplectic and symmetric.

There are numerous possibilities to choose the average $a ( q _ { n } )$ ,but care should be taken that it is onlya function of theposition $q _ { n }$ and thus independent of $p _ { n }$ ,inorder toobtaina symplectic and symmetric method.This precludes takingaverages of the solution of the problemin the oscillation step(Step2) of the algorithm.Instead,one solves the auxiliary initial value problem

$$
\ddot { x } = - \nabla W ( x ) \quad \mathrm { ~ w i t h ~ } \quad x ( 0 ) = q , \ \dot { x } ( 0 ) = 0
$$

together with the variational equation (using the same method and the same step size)

$$
\ddot { X } = - \nabla ^ { 2 } W ( x ( t ) ) X \quad \mathrm { ~ w i t h ~ } \quad X ( 0 ) = I , \dot { X } ( 0 ) = 0
$$

andcomputes the timeaverage over an interval of length $c h$ forsome $c > 0$ :

$$
a ( q ) = \frac { 1 } { c h } \int _ { 0 } ^ { c h } x ( t ) d t , \quad a ^ { \prime } ( q ) = \frac { 1 } { c h } \int _ { 0 } ^ { c h } X ( t ) d t .
$$

Garcia-Archilla et al.(1999） found that the choice $c = 1$ gives the best results.   
Weighted averages instead of the simple average used above give no improvement.

Izaguirre,Reich&Skeel（1999）proposeto take $a ( q )$ asa projection of $q$ tothe manifold $\nabla W ( q ) = 0$ ofrest positions of the fast forces,for situationswhere all non-zero eigenfrequencies of $\nabla ^ { 2 } W ( q )$ aremuch larger than thoseof $\nabla ^ { 2 } U ( q )$ .This choice ismotivated by the fact that solutions oscillateabout this manifold.

We now turn to the interesting special case of a quadratic $\begin{array} { r } { W ( q ) = \frac { 1 } { 2 } q ^ { T } A q } \end{array}$ with asymmetric positive semi-definite matrix $A$ Inthis case,the above average can be computedanalytically.It becomes

$$
a ( q ) = \phi ( h \varOmega ) q
$$

with $\varOmega = A ^ { 1 / 2 }$ and the function $\phi ( \xi ) = \mathrm { s i n c } ( c \xi ) .$ For $a ( q )$ defined by the orthogonal projection to $A q = 0$ wehave $\phi ( 0 ) = 1$ and $\phi ( \xi ) = 0$ for $\xi$ away fromO.With $g _ { n } = - \phi ( h \varOmega ) \nabla U ( \phi ( h \varOmega ) q _ { n } ) .$ ,the mollified impulse method reduces to

$$
{ \begin{array} { r c l } { p _ { n } ^ { + } } & { = } & { p _ { n } + { \frac { 1 } { 2 } } h g _ { n } } \\ { \left( { g _ { n + 1 } } \right) } & { = } & { \left( { \begin{array} { c c } { \cosh / \mathscr { Q } } & { h \operatorname { s i n c } h \mathscr { Q } } \\ { - \mathscr { Q } \sin h \mathscr { Q } } & { \cos h \mathscr { Q } } \end{array} } \right) \left( { q _ { n } } \right) } \\ { p _ { n + 1 } } & { = } & { p _ { n + 1 } ^ { - } + { \frac { 1 } { 2 } } h g _ { n + 1 } . } \end{array} }
$$

This can equivalently be writtenas(1.1O) with the same $g _ { n }$ (and $\mathcal { N }$ in place of $\omega$ ）， orin the two-step form(1.11）with(1.12).

# XIII.1.5 Gautschi's Method Revisited

Werecallthat Gautschi's method(1.7）（with $\varOmega = A ^ { 1 / 2 }$ in place of $\boldsymbol { \omega }$ )integrates equations $\ddot { q } = - A q + g ( q )$ exactly in the case ofa constant inhomogeneity $g ( q ) =$ Const.This property is obviously kept iftheargument of $g$ in the algorithm is modified to

$$
g _ { n } = g ( \phi ( h \Omega ) q _ { n } )
$$

similar to the previous subsection.Such Gautschi-type methods were analyzed by Hochbruck&Lubich（1999a).Functions $\phi$ with $\phi ( 0 ) = 1$ thatvanish at integral multiplesof $\mathcal { R }$ giveasubstantial improvement over the original Gautschi method. Thechoice

$$
\begin{array} { r } { \phi ( \xi ) = \operatorname { s i n c } \xi { \big ( } 1 + { \frac { 1 } { 3 } } \sin ^ { 2 } { \frac { 1 } { 2 } } \xi { \big ) } } \end{array}
$$

was found to give particularly good accuracy.The methods are symmetric but not symplectic.

The following symmetric method for general problems (1.1) with (1.4)was proposed by Hochbruck&Lubich(1999a).Themethod reduces to Gautschi-type methods for quadratic $\begin{array} { r } { W ( q ) = \frac { 1 } { 2 } q ^ { T } A q } \end{array}$ Given $q _ { n }$ and ${ \dot { q } } _ { n }$ ,onecomputes an averaged value $\overline { { { q } } } _ { n } = a ( q _ { n } )$ and the solution of

$$
\begin{array} { r } { \ddot { u } = - \nabla W ( u ) - \nabla U ( \overline { { q } } _ { n } ) \qquad \mathrm { w i t h } \quad u ( 0 ) = q _ { n } , \ \dot { u } ( 0 ) = \dot { q } _ { n } } \end{array}
$$

backwardsand forwards on the intervals fromOto $- h$ and $0$ to $h$ Note that this requires only one evaluation of the slow force $- \nabla U .$ Then, $q _ { n + 1 }$ and $\dot { q } _ { n + 1 }$ are computed from

$$
\begin{array} { r c l } { { q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } ~ = ~ u ( h ) - 2 u ( 0 ) + u ( - h ) } } \\ { { \qquad \dot { q } _ { n + 1 } - \ddot { q } _ { n - 1 } ~ = ~ \dot { u } ( h ) - \dot { u } ( - h ) . } } \end{array}
$$

When the differential equation for $u$ issolved approximately bya symmetric numerical method with smaller time steps,then this becomesasymmetricmultiple time-steppingmethod.Forthe interpretation asanaveraged-force method and for thecorresponding one-step version,where the initial value for the velocity in(1.21） isreplaced by $\dot { u } ( 0 ) = 0$ wereferbackto Sect.VIII.4(where $q _ { n }$ instead of the average $\overline { { { q } } } _ { n } = a ( q _ { n } )$ was taken as the argument of the slow force $- \nabla U$ ).

# XIII.1.6 Two-Force Methods

Hairer& Lubich (2ooOa) compare the analytical solution and the numerical solutionsgiven by the above methods in the Fermi-Pasta-Ulam model of Sect.I.5.1, using the tool of modulated Fourier expansions (see Sections XIII.3and XIII.5 below).Their analysis of the slow energy exchange between stiff springs leads them topropose the following method for equations $\ddot { q } = - A q + g ( q )$ ,which requires two evaluations of the slow force per time step:with $\varOmega = A ^ { 1 / 2 }$ ,set

$$
q _ { n + 1 } - 2 \cos ( h \Omega ) q _ { n } + q _ { n - 1 } = h ^ { 2 } \operatorname { s i n c } ( h \Omega ) g ( q _ { n } ) + h ^ { 2 } d _ { n }
$$

with

$$
d _ { n } = \operatorname { s i n c } ^ { 2 } ( h \Omega ) g ( q _ { n } ) - \operatorname { s i n c } ( h \Omega ) g \big ( \operatorname { s i n c } ( h \Omega ) q _ { n } \big ) .
$$

Thismethod gives the correct slow energy exchange between stiff components in themodel problem and has better energy conservation than the Deuflhard/impulse method.With thevelocityapproximation(1.12） themethod can equivalentlybe writenin the one-step forms(1.19)or(1.1O).The method extends again toa symmetric method for general problems(1.1） with (1.4),givinga correction to the impulse method:let $g ( q ) = - \nabla U ( q )$ and let $a ( q )$ bedefined by(1.18）with $c = 1$ Set $\overline { { { q } } } _ { n } = a ( q _ { n } )$ and

$$
\overline { { { g } } } ( q _ { n } ) = \frac { 2 } { h ^ { 2 } } \Big ( a \big ( q _ { n } + \textstyle \frac { 1 } { 2 } h ^ { 2 } g ( q _ { n } ) \big ) - a ( q _ { n } ) \Big ) .
$$

The method then consists of taking

$$
g _ { n } = g ( q _ { n } ) + \overline { { { g } } } ( q _ { n } ) - g ( \overline { { { q } } } _ { n } )
$$

instead of $g ( q _ { n } ) = - \nabla U ( q _ { n } )$ in the impulse method (1.14).

Atwo-force method with interesting properties,for situations where all non-zero eigenfrequencies of $A$ are much larger than those of $\nabla ^ { 2 } U ( q )$ ,is givenby(1.23）with

$$
\begin{array} { r } { d _ { n } = \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \Omega ) g ( \chi ( h \Omega ) q _ { n } ) = \mathrm { s i n c } ( h \Omega ) g ( \chi ( h \Omega ) q _ { n } ) , } \end{array}
$$

where $\chi ( 0 ) = 1$ and $\chi ( \xi ) = 0$ for $\xi$ away from 0.

# XIII.2 A NonlinearModel Problem and Numerical Phenomena

Togain insight into the properties of the various numerical methods described in theprevious section,it is helpful to study the methodswhen they are applied to suitably chosen,rather simple model problemswhich showcharacteristic features butare still accessible to ananalysis.Such anapproach has traditionally been very successful forstiffdifferential equations(see,e.g.,Hairer&Wanner 1996).For the present stiff-oscillatory case we investigate the behaviour of the numerical methods onnonlinear systems

$$
\ddot { x } + \Omega ^ { 2 } x = g ( x )
$$

withasmooth gradient nonlinearity $g ( x ) = - \nabla U ( x )$ and with the square matrix

$$
\varOmega = \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { \omega I } } \end{array} \right) , \quad \omega \gg 1 ,
$$

with blocks of arbitrary dimension.We consider only solutions whose energy is bounded independentlyof $\boldsymbol { \omega }$ ,sothat in particular the initial values satisfy

$$
\begin{array} { r } { \frac 1 2 \| \dot { { \boldsymbol x } } ( 0 ) \| ^ { 2 } + \frac 1 2 \| \nabla { \boldsymbol x } ( 0 ) \| ^ { 2 } \leq E } \end{array}
$$

with $E$ independent of $\omega$ .

TheFermi-Pasta-Ulam (FPU) problem of Sect.I.5.1 belongs precisely to this class,and we will present numerical experiments with this example.In themodel problem(2.1） with(2.2) we clearly impose strong restrictionsin that the high frequencies are confined to the linear part and that there isa single,constant high frequency.The extension to several high frequencieswill be given in Sect.XIII.9,and constant-frequency systemswith aposition-dependent kinetic energy term areconsideredin Sect.XiII.10.Oscillatory systemswith time-orsolution-dependent high frequencieswill be studied,with different techniquesand fordifferent numerical methods,in Chap.XIV.

Inanycase,satisfactory behaviour of amethod on the model problem(2.1)can beanticipated to be necessary for a successful treatment of more general situations.

# XIII.2.1 Time Scalesin the Fermi-Pasta-Ulam Problem

TheFPU model showsdifferent behaviour ondifferent time scales:almost-harmonic motion of the stiff springs on the time scale $\omega ^ { - 1 }$ ,motion of the soft springs on the scale $\omega ^ { 0 }$ ,energy exchange between stiff springs on the time scale $\omega$ ,andalmostpreservation of the oscillatory energy over intervals that are exponentially longin $\boldsymbol { \omega }$ Thisisillustrated in the following.

We consider the FPU problem with three stiff springswith the data of Sect.I.5.1. The fourpictures of Fig.2.1 show the evolution of the following quantities: the total energy

$$
\begin{array} { r } { H ( x , \dot { x } ) = \frac { 1 } { 2 } \dot { x } ^ { T } \dot { x } + \frac { 1 } { 2 } x ^ { T } \Omega ^ { 2 } x + U ( x ) , } \end{array}
$$

(orrather $H - 0 . 8$ forgraphical reasons),which isaconserved quantity;the oscillatory energy

$$
\begin{array} { r } { I = I _ { 1 } + I _ { 2 } + I _ { 3 } \quad \mathrm { ~ w i t h } \quad I _ { j } = \frac { 1 } { 2 } \dot { x } _ { 1 , j } ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } x _ { 1 , j } ^ { 2 } \mathrm { ~ , ~ } } \end{array}
$$

where $x _ { 1 , j }$ is the $\mathcal { I }$ th component of the lower half $x _ { 1 } \in \mathbb { R } ^ { 3 }$ of $x = ( x _ { 0 } , x _ { 1 } ) ^ { T } \in \mathbb { R } ^ { 6 }$ , decomposed according to the blocksof $\varOmega$ in(2.2).We recall that $x _ { 1 , j }$ represents the

![](images/c4fae433ef226acee82cce564ad5c96724909dc9e4816695362b6de8f02b4a13.jpg)  
Fig.2.1.Different time scalesinthe Fermi-Pasta-Ulammodel $\omega = 5 0$

elongation of the $j$ th stiff spring.Further quantities shown are thekinetic energy of themass centre motion and of the relativemotion of masses joined byastifspring,

$$
\begin{array} { r } { T _ { 0 } = \frac 1 2 \| \dot { x } _ { 0 } \| ^ { 2 } , \quad T _ { 1 } = \frac 1 2 \| \dot { x } _ { 1 } \| ^ { 2 } . } \end{array}
$$

Time Scale $\omega ^ { - 1 }$ .Thevibration of the stiff linear springs is nearly harmonicwith almost-period $\pi / \omega$ .This is illustrated by theplot of $T _ { 1 }$ in the first picture.

TimeScale $\omega ^ { 0 }$ .This is the time scale of the motion of the soft nonlinear springs,as is exemplified by theplotof $\boldsymbol { \bot } _ { 0 }$ in the second picture of Fig.2.1.

Time Scale $\omega$ Aslow energy exchange among the stiff springs takes place on the scale $\omega$ Inthe third picture,theinitially excited first stiff spring passes energy to thesecond one,and thenalso the third stiff spring begins to vibrate.The picture alsoillustrates that the problem is very sensitive to perturbations of the initial data: the grey curves of each of $I _ { 1 } , I _ { 2 } , I _ { 3 }$ correspond to initial data where $1 0 ^ { - 5 }$ hasbeen addedto $x _ { 0 , 1 } ( 0 )$ ， $\dot { x } _ { 0 , 1 } ( 0 )$ and $\dot { x } _ { 1 , 1 } ( 0 )$ .The displayed solutions of the first three pictures have beencomputed veryaccuratelybyan adaptive integrator.

TimeScale $\omega ^ { N }$ , $N \geq 2$ .The oscillatory energy $\boldsymbol { \mathit { 1 } }$ has only $\mathcal { O } ( \omega ^ { - 1 } )$ deviations from theinitial value over very long time intervals.The fourth picture of Fig.2.1 shows the total energy $H$ and the oscillatory energy $I$ as computed by method(1.10)-(1.11) of Sect.XIII.1.2 with the step size $h = 2 / \omega$ ,which isnearlyaslargeasthe length of the time interval of the first picture.Nodriftis seen for $H$ or $I$ .

# XIII.2.2 Numerical Methods

Themethods described in Sect.XII.1 all have in common that they reduce tothe Stormer-Verletmethod when theyare applied to(2.1）with $\varOmega = 0$ ,and they become exact solvers for the linear homogeneous problemwith $g ( x ) \equiv 0$ They can be formulated as one-step or two-step schemes.

Two-Step Formulation.All the methodsof SectionsXII.1.2-XII.1.5,whenapplied to the system (2.1),can be written in the two-step form

$$
x _ { n + 1 } - 2 \cos ( h \varOmega ) x _ { n } + x _ { n - 1 } = h ^ { 2 } \varPsi g ( \varPhi x _ { n } ) .
$$

Here $\psi = \psi ( h \varOmega )$ and $\varPhi = \phi ( h \varOmega )$ ,wheretheflterfunctions $\psi$ and $\phi$ areeven, real-valued functions with $\psi ( 0 ) = \phi ( 0 ) = 1 .$ In our numerical experimentswe will consider the following choices of $\psi$ and $\phi$ ,whereagain $\mathrm { s i n c } ( \xi ) = \sin \xi / \xi$

$$
\begin{array} { r l r l } & { \psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } \xi ) } & { \phi ( \xi ) = 1 } & & { \mathrm { G a u t s c h i } \left( 1 9 6 1 \right) } \\ & { \psi ( \xi ) = \mathrm { s i n c } ( \xi ) } & { \phi ( \xi ) = 1 } & & { \mathrm { D e u f l h a r d } \left( 1 9 7 9 \right) } \\ & { \psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) } & { \phi ( \xi ) = \mathrm { s i n c } ( \xi ) } & { \mathrm { G a r c i a . A r c h i l l a ~ \& \ a l . \ ( 1 9 9 9 ) } } \\ & { \psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } \xi ) } & { \phi ( \xi ) \ \mathrm { o f } \left( 1 . 2 0 \right) } & { \mathrm { H o c h b r u c k ~ \& \ L u b i c h ~ ( 1 9 9 9 a ) } } \\ & { \psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \xi ) } & { \phi ( \xi ) = 1 } & & { \mathrm { H a i r e r ~ } \& \mathrm { L u b i c h } \left( 2 0 0 0 a \right) } \end{array}
$$

One-Step Formulation.The method (2.6) can be written asa symmetric one-step methodofa form that ismotivated by the variation-of-constants formula(1.8).This nowalso includes avelocity approximation $\dot { x } _ { n }$

$$
\begin{array} { r l } & { x _ { n + 1 } = \cos h \Omega x _ { n } + \varOmega ^ { - 1 } \sin h \Omega \dot { x } _ { n } + \frac { 1 } { 2 } h ^ { 2 } \varPsi g _ { n } } \\ & { \dot { x } _ { n + 1 } = - \varOmega \sin h \Omega x _ { n } + \cos h \Omega \dot { x } _ { n } + \frac { 1 } { 2 } h \bigl ( \varPsi _ { 0 } g _ { n } + \varPsi _ { 1 } g _ { n + 1 } \bigr ) } \end{array}
$$

where $g _ { n } = g ( \varPhi { x } _ { n } )$ and $\psi _ { 0 } = \psi _ { 0 } ( h \varOmega )$ ， $\psi _ { 1 } = \psi _ { 1 } ( h \Omega )$ with even functions $\psi _ { 0 }$ , $\psi _ { 1 }$ satisfying $\psi _ { 0 } ( 0 ) = 1$ ， $\psi _ { 1 } ( 0 ) = 1$ Exchanging $n  n + 1$ and $h  - h$ inthe method,itisseen that themethod issymmetricif and only if

$$
\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \psi _ { 1 } ( \xi ) , \quad \psi _ { 0 } ( \xi ) = \cos ( \xi ) \psi _ { 1 } ( \xi ) ,
$$

The method is then symplectic if and only if(Exercise2)

$$
\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \ d \varphi ( \xi ) \ d .
$$

Two-Step Velocity Schemes.For asymmetric method(2.7)-(2.8) thevelocity approximation can be equivalently obtained from

$$
2 h \operatorname { s i n c } ( h \omega ) \dot { x } _ { n } = x _ { n + 1 } - x _ { n - 1 }
$$

(for $\sin ( h \omega ) \neq 0$ orfrom

$$
\begin{array} { r } { \dot { x } _ { n + 1 } - 2 \cos ( h \Omega ) \dot { x } _ { n } + \dot { x } _ { n - 1 } = \frac 1 2 h \varPsi _ { 1 } ( g _ { n + 1 } - g _ { n - 1 } ) . } \end{array}
$$

Thelatter formula givesasymmetric two-step method for arbitrary even functions $\psi _ { 1 }$ with $\psi _ { 1 } ( 0 ) = 1$ ,which do not necessarily satisfy(2.9).

Multi-ForceMethods.Themethods of Sect.XIII.1.6 belong to theclass of multiforce methods,which generalize the right-hand side of(2.6)toa linearcombination of such terms:

$$
x _ { n + 1 } - 2 \cos ( h \Omega ) x _ { n } + x _ { n - 1 } = h ^ { 2 } \sum _ { j = 1 } ^ { k } \varPsi _ { j } g ( \varPhi _ { j } x _ { n } )
$$

with $\varPsi _ { j } = \psi _ { j } ( h \varOmega )$ ， $\Phi _ { j } = \phi _ { j } ( h \Omega )$ ,where $\psi _ { j }$ ， $\phi _ { j }$ are even functions with

$$
\sum _ { j = 1 } ^ { k } \psi _ { j } ( 0 ) = 1 _ { \rangle } \qquad \phi _ { j } ( 0 ) = 1 \qquad \mathrm { f o r } j = 1 _ { \rangle } . . . , k .
$$

In our numerical experimentswe include the method

# XIII.2.3 Accuracy Comparisons

Theaccuracy of the methods(A) $\mathrm { ( E ) }$ and the Stormer-Verlet method ona short time interval isshowninFig.2.2,where the errors at $t = 1$ of the different solution components in the FPU problem（with $\omega = 5 0$ areplottedasa function of the stepsize $h$ Hereand inall the following numerical experiments,the methodswere implemented in the one-step formulation(2.7)-(2.8）with(2.9).The errorsin the $x _ { 0 }$ -componentsarenearlyidentical forall themethodsinthe stabilityrangeofthe Stormer-Verletmethod $h \omega < 2$ ).Differencesbetweenthemethodsarehowever visible for larger step sizes.For the other solution components $x _ { 1 }$ ， $\dot { x } _ { 0 }$ , ${ \dot { x } } _ { 1 }$ there arepronounced differences in the error behaviour of the methods.All five methods （A)-(E)areconsiderably more accurate than the Stormer-Verletmethod.Figure2.3 showsthe errors of methods(A)-(C) for step sizes beyond the stability range of theStormer-Verlet method.Methods(A）and(B） loseaccuracywhen $h \omega$ isnear integral multiples of $\pi$ ,aphenomenon that does not occur with method (C).

![](images/4f80777d5f36af0eaa8c22fd6c514216c4940d0b6449e5c11043442437f7dba8.jpg)  
Fig.2.2.Global error at $t = 1$ forthe different components and for the five methods (A)-(E) and the Stormer-Verlet method as a function of the step size $h$

![](images/d30f21ff1fc3256d3cfb808496db13768dff16c3eab8b5b44528a27308e0a7cf.jpg)  
Fig.2.3.Global error at the first grid point after $t = 1$ for thedifferent components asa function of the step size $h$ Theerror formethod(A）isdrawnin black,formethod(B）in darkgrey,and formethod(C)in light grey.Thevertical linesindicate step sizes forwhich $h \omega$ equals $\pi$ , $2 \pi$ ,or $3 \pi$

# XIII.2.4 Energy Exchange between Stiff Components

Figure 2.4 shows the energy exchange of the six methods(A)-(F)applied to the Fermi-Pasta-Ulamproblemwiththe samedataasin Fig.2.1.The figures show again the oscillatory energies $I _ { 1 } , I _ { 2 } , I _ { 3 }$ ofthe stiff springs,their sum $I = I _ { 1 } + I _ { 2 } + I _ { 3 }$ and the total energy $H - 0 . 8$ asfunctions of time on the interval $0 \leq t \leq 2 0 0 .$ Only themethods(B),(D）and(F） givea good approximation of the energy exchange between the stiff springs.Itwill turn out in Sect.XIII.4.2 thatanecessary condition foracorrect approximation of the energy exchange is $\psi ( h \omega ) \phi ( h \omega ) = \operatorname { s i n c } ( h \omega )$ , which is satisfied formethod(B).The two-force method (F)satisfiesananalogous condition for multi-forcemethods.The good behaviour of method(D) comes from the fact that here $\psi ( h \omega ) \phi ( h \omega ) \approx 0 . 9 5 \operatorname { s i n c } ( h \omega )$ for $h \omega = 1 . 5$ .

![](images/d0c586caa78e4749ac49970a0c12869c3e4f4eb84890c9674e549cd42b49083a.jpg)  
Fig.2.4.Energy exchange between stiff springs for methods(A)-(F) $h = 0 . 0 3$ , $\omega = 5 0$ )

![](images/5e4f9b8855edcf4725d6571fa7d8592c6f23cbf1610cc55ab91116ceb0790fd1.jpg)  
Fig.2.5.Maximumerror of thetotal energy on the interval $\left[ 0 , 1 0 0 0 \right]$ formethods(A)-(F)as a function of $h \omega$ (step size $h = 0 . 0 2$

# XIII.2.5 Near-Conservation of Total and Oscillatory Energy

Figure2.5shows the maximum error of the total energy $H$ asa function of the scaled frequency $h \omega$ (step size $h = 0 . 0 2$ ).Weconsiderthelong time interval[O,1ooo].The pictures for thedifferent methods show that in general the total energy iswell conserved.Exceptionsare near integral multiplesof $\boldsymbol { \mathcal { U } }$ Certain methodsshowa bad energy conservationcloseto odd multiplesof $\pi$ ,othermethods closeto even multiplesof $\pi$ Onlymethod(E)showsauniformly good behaviour forall frequencies.In Fig.2.6we show in more detail what happens close to such integral multiples of $\pi$ .

![](images/f6794408780679bc58ceebe613f82ce50b86404b0a576288e9e07bfa5a48c030.jpg)  
Fig.2.6.Zoom (close to $\pi$ or $2 \pi$ ofthemaximum errorof the total energyonthe interval [0,1000] for three methodsasa function of $h \omega$ (step size $h = 0 . 0 2$

![](images/e57e8d1a4222231b84e02dc06f61e40683415390fa70a80122ca658206b5b641.jpg)  
Fig.2.7.Maximumdeviation of the oscillatory energy on theinterval $\left[ 0 , 1 0 0 0 \right]$ for methods（A)-(F）asa function of $h \omega$ (step size $h = 0 . 0 2$ ）

If there is adifficulty close to $\pi$ ,itis typicallyinan entire neighbourhood.Close to $2 \pi$ ,the picture is different.Method (C) has good energy conservation for values of $h \omega$ thatarevery close to $2 \pi$ ,but there are small intervalsto theleft andto theright, where the error in the total energy is large.Unlike the othermethods shown,method (B)has poor energy conservation in rather large intervalsaround even multiples of $\pi$ Methods (A）and(D）conserve thetotal energyparticularlywell,for $h \omega$ away from integral multiplesof $\pi$ .

Figure 2.7 shows similar pictureswhere the total energy $H$ isreplaced by the oscillatory energy $\boldsymbol { \mathit { 1 } }$ (cf.Sect.XIII.2.1).For the exact solution we have $I ( t ) \ =$ $C o n s t + O ( \omega ^ { - 1 } ) .$ Itis therefore not surprising that this quantity is not well conserved for smallvaluesof $\omega$ Forlargervalues of $\omega$ ,weobserve that the methods havedifficulties in conserving the oscillatory energywhen $h \omega$ is near integral multiplesof $\pi$ .Noneof the considered methodsconserves both quantities $H$ and $I$ uniformlyforallvaluesof $h \omega$ .

# XII.3 Principal Terms of the Modulated Fourier Expansion

Theanalytical tool for understanding the above numerical phenomena is provided bymodulated Fourier expansions,whichdecompose both the exactand the numerical solution into a slowly varying part and into oscillatory components built up oftrigonometric functions multiplied with slowly varying coefficient functions.A comparison of these expansionswill serve asapartial substitute for the backward erroranalysis ofChap.IX,which yields resultsonly for $h \omega  0$ and is not applicable to the situation of $h \omega \geq c > 0$ that is of interest here.In this sectionwe derive thefirst terms of the modulated Fourier expansion.

# XIII.3.1 Decomposition of the Exact Solution

Every solution of the linear equation $\ddot { x } + \Omega ^ { 2 } x = g ( t )$ with $\mathcal { Q }$ of(2.2）can be written as $y ( t ) + \cos ( \omega t ) u ( t ) + \sin ( \omega t ) v ( t ) + \mathcal { O } ( \omega ^ { - N } )$ (for $\omega  \infty$ ,where $y ( t ) , u ( t )$ , $v ( t )$ aretruncated asymptotic expansions inpowers of $\omega ^ { - 1 }$ (seeExercise4）.These functions have theproperty that all theirderivatives are bounded independentlyof theparameter $\omega \gg 1$ Hereandinthefollowing,a smooth functionisunderstood tobea function with thisproperty.Wemay hope to find a similar decomposition for solutions of the nonlinear problem (2.1).So we look for a smooth real-valued function $y ( t )$ anda smooth complex-valued function $z ( t ) = u ( t ) + i v ( t )$ such that the function

$$
x _ { * } ( t ) = y ( t ) + e ^ { i \omega t } z ( t ) + e ^ { - i \omega t } \overline { { z } } ( t )
$$

givesasmall defect when it isinserted into the differential equation (2.1) and has the given initial values

$$
x _ { * } ( 0 ) = x ( 0 ) , \quad \dot { x } _ { * } ( 0 ) = \dot { x } ( 0 ) .
$$

Underthe condition (2.3） the exact solution $x ( t )$ hasbounded energy，and we mayexpect the same of the approximation $x _ { * } ( t )$ ,whichwould then imply $z ( t ) =$ $\mathcal { O } ( \omega ^ { - 1 } )$ Wetherefore insert the ansatz(3.1） into the differential equation (2.1） andexpand the nonlinearity around the smooth part $y ( t )$ Withthevariables $y =$ $( y _ { 0 } , y _ { 1 } )$ ， $\boldsymbol { z } = \left( z _ { 0 } , z _ { 1 } \right)$ partitioned according to the blocks of $\mathcal { S }$ ,this gives the expressions

$$
\begin{array} { r } { \ddot { x } _ { * } + { \Omega } ^ { 2 } x _ { * } = \left( \begin{array} { c } { \ddot { y } _ { 0 } } \\ { \ddot { y } _ { 1 } + \omega ^ { 2 } y _ { 1 } } \end{array} \right) \ + \ e ^ { i \omega t } \left( \begin{array} { c } { - \omega ^ { 2 } z _ { 0 } + 2 i \omega \dot { z } _ { 0 } + \ddot { z } _ { 0 } } \\ { 2 i \omega \dot { z } _ { 1 } + \ddot { z } _ { 1 } } \end{array} \right) } \\ { \ + \ e ^ { - i \omega t } \left( \begin{array} { c } { - \omega ^ { 2 } \overline { { z } } _ { 0 } - 2 i \omega \dot { \bar { z } } _ { 0 } + \ddot { \bar { z } } _ { 0 } } \\ { - 2 i \omega \dot { \bar { z } } _ { 1 } + \ddot { \bar { z } } _ { 1 } } \end{array} \right) } \end{array}
$$

and,as long as $z ( t ) = O ( \omega ^ { - 1 } )$ ,

$$
\begin{array} { l } { { g ( x _ { * } ) ~ = ~ g ( y ) + g ^ { \prime \prime } ( y ) ( z , \overline { { { z } } } ) + e ^ { i \omega t } g ^ { \prime } ( y ) z + e ^ { - i \omega t } g ^ { \prime } ( y ) \overline { { { z } } } } } \\ { { ~ + ~ e ^ { 2 i \omega t } { \textstyle { \frac { 1 } { 2 } } } g ^ { \prime \prime } ( y ) ( z , z ) + e ^ { - 2 i \omega t } { \textstyle { \frac { 1 } { 2 } } } g ^ { \prime \prime } ( y ) ( \overline { { { z } } } , \overline { { { z } } } ) + { \cal O } ( \omega ^ { - 3 } ) . } } \end{array}
$$

Equations for the Coefficient Functions.We now compare the coefficients of $1 , e ^ { i \omega t } , e ^ { - i \omega t }$ and require that the dominant terms in these expressions be equal:

$$
\begin{array} { r c l } { { \ddot { y } _ { 0 } } } & { { = } } & { { g _ { 0 } ( y ) + g _ { 0 } ^ { \prime \prime } ( y ) ( z , \overline { { { z } } } ) } } \\ { { \omega ^ { 2 } y _ { 1 } } } & { { = } } & { { g _ { 1 } ( y ) } } \\ { { - \omega ^ { 2 } z _ { 0 } } } & { { = } } & { { g _ { 0 } ^ { \prime } ( y ) z } } \\ { { 2 i \omega \dot { z } _ { 1 } } } & { { = } } & { { g _ { 1 } ^ { \prime } ( y ) z , } } \end{array}
$$

Thisgivesa system of differential equations for $y _ { 0 } , z _ { 1 }$ and expresses $y _ { 1 } , z _ { 0 }$ as functions of $y _ { 0 } , z _ { 1 }$ Wenote that $y _ { 0 }$ evolves on the time scale 1,whereas $z _ { 1 }$ changes on the slow time scale $\omega$ Aslongas $y _ { 0 } ( t )$ staysina bounded domain and $z _ { 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } )$ ,(3.3)implies the bounds

$$
y _ { 1 } ( t ) = \mathcal { O } ( \omega ^ { - 2 } ) , \quad z _ { 0 } ( t ) = \mathcal { O } ( \omega ^ { - 3 } ) , \quad \dot { z } _ { 1 } ( t ) = \mathcal { O } ( \omega ^ { - 2 } ) .
$$

InitialValues.The initial values $y _ { 0 } ( 0 )$ , $\dot { y } _ { 0 } ( 0 )$ and $z _ { 1 } ( 0 )$ are obtained from condition (3.2),which givesasystem that can be solved by fixed point iterationto yield

$$
\begin{array} { r l } { y _ { 0 } ( 0 ) = x _ { 0 , 0 } + O ( \omega ^ { - 3 } ) , } & { \quad \dot { y } _ { 0 } ( 0 ) = \dot { x } _ { 0 , 0 } + \mathcal { O } ( \omega ^ { - 2 } ) } \\ { 2 \operatorname { R e } z _ { 1 } ( 0 ) = x _ { 0 , 1 } + \mathcal { O } ( \omega ^ { - 2 } ) , } & { - \omega 2 \operatorname { I m } z _ { 1 } ( 0 ) = \dot { x } _ { 0 , 1 } + O ( \omega ^ { - 2 } ) . } \end{array}
$$

Defect.As long as $z _ { 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } ) ,$ theaboveequations show thatthe defect

$$
d ( t ) = \ddot { x } _ { * } ( t ) + \varOmega ^ { 2 } x _ { * } ( t ) = g \bigl ( x _ { * } ( t ) \bigr )
$$

is ofthe form

$$
\begin{array} { r } { d ( t ) = \mathrm { R e } \left( \begin{array} { c } { \omega ^ { - 2 } e ^ { i \omega t } a ( t ) + \omega ^ { - 2 } e ^ { 2 i \omega t } b ( t ) + \mathcal { O } ( \omega ^ { - 3 } ) } \\ { \mathcal { O } ( \omega ^ { - 2 } ) } \end{array} \right) } \end{array}
$$

with smooth functions $a , b$ .Togetherwith(3.3） this also shows that the smooth $\mathcal { O } ( \omega ^ { - 2 } )$ -term $g ^ { \prime \prime } ( y ) ( z , \overline { { z } } )$ isthe principal term describing the influence of oscillatorysolution components on the evolution of smooth components.

Example.To illustrate the approximation of the solution $x ( t )$ by $x _ { * } ( t )$ of(3.1),we have solved numerically,with high accuracy,the system(3.3) for the FPU problem with thedataof Sect.I.5.1.InFigure 3.1weplot the oscillatory energy $I = I _ { 1 } +$ $I _ { 2 } + I _ { 3 }$ with $x$ replaced by the approximation $x _ { * }$ in thedefinition(2.5）of these quantities.The figure agrees rather well with FigureI.5.2.

![](images/712d1fb91f7dab64d505c9032187ec7cb854131bc12757ea895e09e50a153711.jpg)  
Fig.3.1.Sameexperiment as in Fig.I.5.2 for the solution (3.1) of (3.3)

# XIII.3.2 Decomposition of the Numerical Solution

For the numerical method (2.6),which solves linear equations $\ddot { x } = - \varOmega ^ { 2 } x$ exactly, welook similarlytotheabove fora function ofthe form

$$
x _ { h } ( t ) = y _ { h } ( t ) + e ^ { i \omega t } z _ { h } ( t ) + e ^ { - i \omega t } \overline { { z } } _ { h } ( t )
$$

with coefficient functions $y _ { h } ( t )$ , $z _ { h } ( t )$ which are smooth in the sense that all their derivativesare bounded independentlyof $h$ and $\omega$ ,such that $x _ { h } ( t )$ gives asmall defect when inserted into the difference scheme (2.6) and has the correct starting values:

$$
x _ { h } ( 0 ) = x _ { 0 } \ , x _ { h } ( h ) = x _ { 1 } .
$$

Taylor expansion of $z _ { h } ( t \pm h )$ at the point $t$ shows,after some calculation,

$$
\frac { 1 } { h ^ { 2 } } \Big ( x _ { h } ( t + h ) - 2 \cos ( h \Omega ) x _ { h } ( t ) + x _ { h } ( t - h ) \Big ) = \left( \begin{array} { c } { \delta _ { h } ^ { 2 } y _ { h , 0 } ( t ) } \\ { \sigma _ { 1 } ^ { 2 } \omega ^ { 2 } y _ { h , 1 } ( t ) + \delta _ { h } ^ { 2 } y _ { h , 1 } ( t ) } \end{array} \right)
$$

$$
\begin{array} { r l r } & { } & { + e ^ { i \omega t } \left( - \sigma _ { 1 } ^ { 2 } \omega ^ { 2 } z _ { h , 0 } ( t ) + \sigma _ { 2 } 2 i \omega \dot { z } _ { h , 0 } ( t ) + \cos ( h \omega ) \ddot { z } _ { h , 0 } ( t ) + \dots \right) } \\ & { } & { \sigma _ { 2 } 2 i \omega \dot { z } _ { h , 1 } ( t ) + \cos ( h \omega ) \ddot { z } _ { h , 1 } ( t ) + \dots \Big ) } \end{array}
$$

+thecomplexconjugate of the expression in the previous line,

where $y _ { h } ( t ) = ( y _ { h , 0 } ( t ) , y _ { h , 1 } ( t ) )$ and $z _ { h } ( t ) = ( z _ { h , 0 } ( t ) , z _ { h , 1 } ( t ) )$ according to the partitioning in (2.2),

$$
\delta _ { h } ^ { 2 } y _ { h } ( t ) = \frac { 1 } { h ^ { 2 } } \Big ( y _ { h } ( t + h ) - 2 y _ { h } ( t ) + y _ { h } ( t - h ) \Big )
$$

isthe symmetric second-order difference quotient, $\sigma _ { k } = \mathrm { s i n c } ( \textstyle { \frac { 1 } { 2 } } k h \omega )$ ,and the dots stand for higher powers of $h$ multipliedbyderivativesof $z _ { h , 0 }$ or $z _ { h , 1 } .$ Taylorexpansion of the nonlinearity now gives

$$
\begin{array} { r } { \begin{array} { r l } { \varPsi g ( \phi x _ { h } ) \ = \ \varPsi g ( \varPhi y _ { h } ) + \varPsi g ^ { \prime \prime } ( \varPhi y _ { h } ) ( \varPhi z _ { h } , \varPhi \overline { { z } } _ { h } ) } & { } \\ { \quad + \ e ^ { i \omega t } \varPsi g ^ { \prime } ( \varPhi y _ { h } ) \varPhi z _ { h } + e ^ { - i \omega t } \varPsi g ^ { \prime } ( \varPhi y _ { h } ) \varPhi \overline { { z } } _ { h } + . . . } \end{array} } \end{array}
$$

Modified Equations for the Numerical Coefficient Functions.For the moment we consider the case where the absolute values of $\boldsymbol { O } _ { 1 }$ and $o _ { 2 }$ are bounded from below bya positive constant,so that $h \omega$ isassumed bounded and boundedaway froma non-zero integral multiple of $\pi$ Wealso assume $h \omega$ to be bounded away fromzero，which is the computational situation of interest.In this case,the first termin each line of each bracket in(3.9)can be consideredasthedominant one.We therefore require that the functions $y _ { h } , z _ { h }$ satisfy

$$
\begin{array} { r c l } { { \delta _ { h } ^ { 2 } y _ { h , 0 } ~ = ~ g _ { 0 } ( \phi y _ { h } ) + g _ { 0 } ^ { \prime \prime } ( \phi y _ { h } ) ( \phi z _ { h } , \phi \overline { { { z } } } _ { h } ) } } \\ { { } } \\ { { \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) \omega ^ { 2 } y _ { h , 1 } ~ = ~ \psi ( h \omega ) g _ { 1 } ( \phi y _ { h } ) } } \\ { { } } & { { } } \\ { { - \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) \omega ^ { 2 } z _ { h , 0 } ~ = ~ \displaystyle { \frac { \partial g _ { 0 } } { \partial x _ { 0 } } ( \phi y _ { h } ) z _ { h , 0 } + \frac { \partial g _ { 0 } } { \partial x _ { 1 } } ( \phi y _ { h } ) \phi ( h \omega ) z _ { h , 1 } } } } \\ { { } } & { { } } \\ { { \mathrm { s i n c } ( h \omega ) 2 i \omega \dot { z } _ { h , 1 } ~ = ~ \psi ( h \omega ) \displaystyle { \frac { \partial g _ { 1 } } { \partial x _ { 0 } } ( \phi y _ { h } ) } z _ { h , 0 } ~ + \psi ( h \omega ) \displaystyle { \frac { \partial g _ { 1 } } { \partial x _ { 1 } } ( \bar { \phi } y _ { h } ) \phi ( h \omega ) z _ { h } } } } \end{array}
$$

The first equation should be stated more preciselyas $y _ { h , 0 }$ being a solution of a modified equation for the Stormer-Verletmethod(see ExerciseIX.3)applied to the corresponding differential equation:

$$
\ddot { y } _ { h , 0 } = \left( 1 - \frac { h ^ { 2 } } { 1 2 } \frac { d ^ { 2 } } { d t ^ { 2 } } \right) \left( g _ { 0 } ( \varPhi { y } _ { h } ) + g _ { 0 } ^ { \prime \prime } ( \varPhi { y } _ { h } ) ( \varPhi { z } _ { h } , \varPhi { \overline { { z } } } _ { h } ) \right) ,
$$

where the time derivatives of $y _ { h , 1 } , z _ { h }$ thatresult from applying the chain ruleare replaced by using the expressions in(3.11).As longas $y _ { h , 0 } ( t )$ remainsinabounded domainand $z _ { h , 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } )$ ,we have again bounds of the same type as for the coefficients of the exact solution:

$$
y _ { h , 1 } ( t ) = \mathcal { O } ( \omega ^ { - 2 } ) , \quad z _ { h , 0 } ( t ) = \mathcal { O } ( \omega ^ { - 3 } ) , \quad \dot { z } _ { h , 1 } ( t ) = \mathcal { O } ( \omega ^ { - 2 } ) .
$$

Initial Values.Wenext determine the initial values $y _ { h , 0 } ( 0 )$ , $\dot { y } _ { h , 0 } ( 0 )$ and $z _ { h , 1 } ( 0 )$ such that $x _ { h } ( 0 )$ and $x _ { h } ( h )$ coincide with the starting values $x _ { 0 } = x ( 0 )$ and $x _ { 1 }$ of thenumerical method.We let $x _ { 1 }$ becomputed from $\scriptstyle { \mathcal { X } } 0$ and $x _ { 0 }$ via the formula（2.7） with $n = 0$ ,andwe still assume that $\sigma _ { 1 }$ and $\sigma _ { 2 }$ are bounded away from zero. Using (3.11）,the condition $x _ { h } ( 0 ) = x _ { 0 } = ( x _ { 0 , 0 } , x _ { 0 , 1 } )$ then becomes

$$
\begin{array} { r c l } { { x _ { 0 , 0 } } } & { { = } } & { { y _ { h , 0 } ( 0 ) + \mathcal { O } \big ( \omega ^ { - 2 } z _ { h , 1 } ( 0 ) \big ) } } \\ { { } } & { { } } & { { } } \\ { { x _ { 0 , 1 } } } & { { = } } & { { z _ { h , 1 } ( 0 ) + \overline { { { z } } } _ { h , 1 } ( 0 ) + \mathcal { O } ( \omega ^ { - 2 } ) . } } \end{array}
$$

Theformula for the first component of (2.7), $\begin{array} { r } { x _ { 1 , 0 } - x _ { 0 , 0 } = h \dot { x } _ { 0 , 0 } + \frac { 1 } { 2 } h ^ { 2 } g _ { 0 } ( \varPhi x _ { 0 } ) } \end{array}$ ,together with $\begin{array} { r } { x _ { h , 0 } ( h ) - x _ { h , 0 } ( 0 ) = h \dot { y } _ { h , 0 } ( 0 ) + \frac { 1 } { 2 } h ^ { 2 } g _ { 0 } ( \varPhi \ d x _ { 0 } ) + \mathcal O ( h ^ { 3 } ) + \mathcal O ( \omega ^ { - 2 } z _ { h , 1 } ( 0 ) ) } \end{array}$ impliesthat

$$
\dot { x } _ { 0 , 0 } = \dot { y } _ { h , 0 } ( 0 ) + \mathcal { O } ( h ^ { 2 } ) + \mathcal { O } \big ( \omega ^ { - 1 } z _ { h , 1 } ( 0 ) \big ) .
$$

For the second component we have from (2.7)

$$
\begin{array} { r } { x _ { 1 , 1 } - \cos ( h \omega ) x _ { 0 , 1 } = h \operatorname { s i n c } ( h \omega ) \dot { x } _ { 0 , 1 } + \frac { 1 } { 2 } h ^ { 2 } \psi ( h \omega ) g _ { 1 } ( \varPhi { x } _ { 0 } ) , } \end{array}
$$

and by Taylor expansion and(3.11),

$$
\begin{array} { r c l } { \boldsymbol { \nu } , \boldsymbol { \mathrm { 1 } } ( h ) - \cos ( h \omega ) \boldsymbol { x } _ { h , 1 } ( 0 ) } & { = } & { \left( \boldsymbol { \mathrm { 1 } } - \cos ( h \omega ) \right) \boldsymbol { y } _ { h , 1 } ( 0 ) + \mathcal { O } ( h \omega ^ { - 2 } ) } \\ & & { + i \sin ( h \omega ) \big ( \boldsymbol { z } _ { h , 1 } ( 0 ) - \boldsymbol { \overline { { z } } } _ { h , 1 } ( 0 ) \big ) + \mathcal { O } ( h \omega ^ { - 1 } \boldsymbol { z } _ { h , 1 } ( 0 ) ) , } \end{array}
$$

where we note the relation $( 1 - \cos ( h \omega ) ) y _ { h , 1 } ( 0 ) \ = \ \frac { _ 1 } { ^ 2 } h ^ { 2 } \psi ( h \omega ) g _ { 1 } ( \underline { { \phi } } y _ { h } ( 0 ) )$ by (3.11）and a trigonometric identity.After division by $h \operatorname { s i n c } h \omega = \omega ^ { - 1 } \sin h \omega$ the above formulasyield

$$
\dot { x } _ { 0 , 1 } = i \omega \big ( z _ { h , 1 } ( 0 ) - \overline { { z } } _ { h , 1 } ( 0 ) \big ) + \mathcal { O } ( \omega ^ { - 2 } ) + \mathcal { O } \big ( \omega ^ { - 1 } z _ { h , 1 } ( 0 ) \big ) .
$$

Thefour equations(3.13),(3.14),(3.15）constituteanonlinear system for the four quantities $y _ { 0 } ( 0 )$ , $\dot { y } _ { 0 } ( 0 )$ , $\omega \big ( z _ { h , 1 } ( 0 ) + \overline { { z } } _ { h , 1 } ( 0 ) \big )$ ,and $\omega ( z _ { h , 1 } ( 0 ) - \overline { { z } } _ { h , 1 } ( 0 ) ) ,$ Byfixedpoint iterationand using the bounded-energyassumption(2.3),we get a locally unique solution for sufficiently small $h$ ,with $z _ { h . 1 } ( 0 ) = \mathcal { O } ( \omega ^ { - 1 } )$ and hence

$$
\begin{array} { r l } { y _ { h , 0 } ( 0 ) = x _ { 0 , 0 } + \mathcal { O } ( \omega ^ { - 3 } ) ~ , } & { { } \dot { y } _ { h , 0 } ( 0 ) = \dot { x } _ { 0 , 0 } + \mathcal { O } ( h ^ { 2 } ) } \\ { 2 \operatorname { R e } z _ { h , 1 } ( 0 ) = x _ { 0 , 1 } + \mathcal { O } ( \omega ^ { - 2 } ) ~ , } & { { } - \omega 2 \operatorname { I m } z _ { h , 1 } ( 0 ) = \dot { x } _ { 0 , 1 } + \mathcal { O } ( h \omega ^ { - 1 } ) ~ . } \end{array}
$$

Defect.As long as $z _ { h , 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } )$ ,thedefect

$$
d _ { h } ( t ) = \frac { 1 } { h ^ { 2 } } \Big ( \boldsymbol { x } _ { h } ( t + h ) - 2 \cos ( h \varOmega ) \boldsymbol { x } _ { h } ( t ) + \boldsymbol { x } _ { h } ( t - h ) \Big ) - \varPsi g \big ( \varPhi \boldsymbol { x } _ { h } ( t ) \big )
$$

is of size $\mathcal { O } ( h ^ { 2 } )$ by(3.9)-(3.1O)and the very construction(3.11） of the coefficient functions.This estimate refers again to the non-resonant case where $\sigma _ { 1 } , \sigma _ { 2 }$ arebounded away from zero and hence $h \omega$ isbounded away from non-zero integral multiples of $\mathcal { R }$ Thecase of $h \omega$ nearamultiple of $\pi$ requiresa special treatment and will be considered in the next subsection.

# XIII.4 Accuracy and Slow Exchange

Acomparison of the principal terms of the modulated Fourier expansions of the numerical and the exact solution gives much insight into the behaviour of the numerical method and therole of the flter functions $\psi$ and $\phi$ From this comparison we obtain error bounds over finite time intervals,and wediscuss the slow energy exchange between oscillatory components and the slow energy transfer from oscillatoryto smooth componentswhich take place on the time scale $\omega$ .

# XIII.4.1 Convergence Properties on Bounded Time Intervals

Asafirst application of the modulated Fourier expansion we consider error bounds onbounded time intervals.Second-order convergence estimates for more general equations $\ddot { x } = - A x + g ( x )$ with symmetric positive semi-definite matrix $A$ ,uniformly in the(arbitrarily large)eigenfrequenciesof $A$ ,are given by Garcia-Archilla, Sanz-Serna& Skeel（1999）forthemollified impulsemethod,byHochbruck&Lubich（1999a) forGautschi-typemethods,and byGrimm&Hochbruck（2005)for general methods of theclass（2.7)-(2.8）with appropriate filter functions.Those resultswere proved with different techniques.The following bounds on the filter functions $\psi$ and $\phi$ areneeded for second-order error bounds of method(2.6):

$$
\begin{array} { r } { \left| \psi ( h \omega ) \right| \leq C _ { 1 } \operatorname { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) , \ } \\ { \left| \phi ( h \omega ) \right| \leq C _ { 2 } \left| \operatorname { s i n c } ( \frac { 1 } { 2 } h \omega ) \right| , \ } \\ { \left| \psi ( h \omega ) \phi ( h \omega ) \right| \leq C _ { 3 } \left| \operatorname { s i n c } ( h \omega ) \right| . } \end{array}
$$

Theorem4.1.Consider thenumerical solution ofthe system $( 2 . I ) - ( 2 . 3 )$ bymethod (2.6)with a step size $h \leq h _ { 0 }$ (witha sufficiently small $h _ { 0 }$ independent of $\omega$ )for which $h \omega \geq c _ { 0 } > 0 .$ Let the starting value $x _ { 1 }$ begivenby（2.7）with $n = 0$ Ifthe conditions(4.1）aresatisfied,then theerrorisboundedby

$$
\| x _ { n } - x ( n h ) \| \leq C h ^ { 2 } ~ f o r ~ n h \leq T .
$$

Ifonly $| \psi ( h \omega ) | \leq C _ { 0 } \big | \mathrm { s i n c } ( \frac { 1 } { 2 } h \omega ) \big |$ holdsinsteadof(4.1),thentheorder ofconvergence reduces toone: $\| x _ { n } - x ( n h ) \| \leq C$ hfor $n h \leq 1$ Inbothcases, $C$ is independentof $\omega$ hand $\textit { n }$ with $n h \le T$ and of bounds of solution derivatives,but dependson $T$ ,on $E$ of(2.3),on bounds ofderivatives of thenonlinearity $g$ andon $C _ { 1 } , C _ { 2 } , C _ { 3 }$ or $C _ { 0 }$ .

Toobtain second-order error boundsuniformly in $h \omega$ ,condition(4.1） requires a double zeroof $\psi$ anda zero of $\phi$ at even multiplesof $\pi$ ,andazeroof $\psi$ orat odd multiples of $\pi$ Thisis satisfied forthe mollified impulse method with $\phi ( \xi ) ~ = ~ \mathrm { s i n c } ( \xi )$ ,forwhich $\psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \xi )$ Gautschi-type methods have $\psi ( \xi ) = \operatorname { s i n c } ^ { 2 } ( \textstyle { \frac { 1 } { 2 } } \xi )$ ,sothat the first condition on $\psi$ in（4.1）istrivially satisfied.The conditions on $\phi$ hold,for example,for $\phi = \mathrm { s i n c }$ orfor $\phi$ of（1.20）.The original Gautschi method has $\phi = 1$ ,which does not satisfy the second condition of(4.1), andtheDeuflhard/impulsemethod $\psi = \mathrm { s i n c } , \phi = 1$ satisfies only thethird conditionof(4.1).These latter methodsare not of second orderuniformly in $h \omega$

ProofofTheorem4.1.(a)Firstwe consider thecasewhere $h \omega$ is bounded away from integral multiples of $\pi$ ,sothat condition (4.1）is not needed.Comparing the equations(3.3)and(3.11）,whichdetermine themodulated Fourier expansioncoefficients,shows

$$
y _ { h } ( t ) = y ( t ) = \mathcal { O } ( h ^ { 2 } ) ~ , ~ z _ { h } ( t ) - z ( t ) = \mathcal { O } ( h ^ { 2 } )
$$

on bounded intervals,and hence

$$
x _ { h } ( t ) - x _ { * } ( t ) = \mathcal { O } ( h ^ { 2 } ) .
$$

Thevariation-of-constants formula(1.8) and a Gronwall-type inequality show that, onbounded intervals,the error $x _ { * } ( t ) - x ( t )$ is of the same magnitudeas the defect: by (3.6),

$$
x _ { * } ( t ) - x ( t ) = 0 ( \omega ^ { - 2 } ) .
$$

The errors $e _ { n } = x _ { n } - x _ { h } ( t _ { n } )$ satisfy

$$
e _ { n + 1 } - 2 \cos ( h \Omega ) e _ { n } + e _ { n - 1 } = b _ { n }
$$

with $b _ { n } = h ^ { 2 } \big ( \boldsymbol { \varPsi } g ( \boldsymbol { \varPhi } x _ { n } ) - \boldsymbol { \varPsi } g ( \boldsymbol { \varPhi } x _ { h } ( t _ { n } ) ) - d _ { h } ( t _ { n } ) \big ) .$ This recurrence relation can be solved toyield(Exercise5）

$$
e _ { n + 1 } = - W _ { n - 1 } e _ { 0 } + W _ { n } e _ { 1 } + \sum _ { j = 1 } ^ { n } W _ { n - j } b _ { j }
$$

with

$$
W _ { n } \equiv \left( \begin{array} { c c c } { { ( n + 1 ) I } } & { { 0 } } \\ { { 0 } } & { { { \displaystyle \frac { \sin ( n + 1 ) h \omega } { \sin h \omega } } I } } \end{array} \right) \ .
$$

Adiscrete Gronwall inequality nowyields that on bounded intervals, $e _ { n }$ isof the samemagnitudeas the defect $d _ { h } ( t )$ of（3.17）,which is $\mathcal { O } ( h ^ { 2 } )$ by the construction of(3.11)and by $z _ { h , 1 } = \mathcal { O } ( \omega ^ { - 1 } ) .$ Hence,

$$
x _ { n } - x _ { h } ( t _ { n } ) = \mathcal { O } ( h ^ { 2 } ) .
$$

Combining these estimates yields the desired second-order error bound.

(b)We now consider the case where $\omega | \mathrm { s i n c } ( \scriptstyle { \frac { 1 } { 2 } } h \omega ) | \geq c$ with a sufficiently large constant $c$ ,which depends only on bounds of derivatives of $g .$ This condition means that $h \omega$ is outside of an $\mathcal { O } ( h )$ neighbourhood of integral multiples of $2 \pi$ Under conditions (4.1),the equations(3.11) still give

$$
y _ { h , 1 } ( t ) = O ( \omega ^ { - 2 } ) \ , \quad z _ { h , 0 } ( t ) = O ( \omega ^ { - 2 } ) \ , \quad \dot { z } _ { h , 1 } ( t ) = O ( \omega ^ { - 2 } )
$$

as longas $z _ { h , 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } )$ Here the first condition of（4.1） gives the bound of $y _ { h , 1 }$ ,the second one the bound of $z _ { h , 0 }$ ,and the third one the bound of $\dot { z } _ { h , 1 }$ As in Sect.XIII.3.2,wedetermine the initial values $y _ { h , 0 } ( 0 )$ , $\dot { y } _ { h , 0 } ( 0 )$ and $z _ { h , 1 } ( 0 )$ such that $x _ { h } ( 0 )$ and $x _ { h } ( h )$ coincide with the starting values $x _ { 0 }$ and $x _ { 1 }$ of the numerical method.Usingoncemore(4.1）,we obtainasystem for theinitial values similar to (3.13)-(3.15）：

$$
\begin{array} { r l } { \boldsymbol { x } _ { 0 , 0 } } & { = \begin{array} { l } { y _ { h , 0 } ( 0 ) + \mathcal { O } \big ( \omega ^ { - 1 } z _ { h , 1 } ( 0 ) \big ) } \end{array} } \\ { \boldsymbol { x } _ { 0 , 1 } } & { = \begin{array} { l } { z _ { h , 1 } ( 0 ) + \overline { { z } } _ { h , 1 } ( 0 ) + \mathcal { O } ( \omega ^ { - 2 } ) } \end{array} } \\ { \dot { \boldsymbol { x } } _ { 0 , 0 } } & { = \begin{array} { l } { \dot { y } _ { h , 0 } ( 0 ) + \mathcal { O } ( h ) + \mathcal { O } \big ( \omega ^ { - 1 } z _ { h , 1 } ( 0 ) \big ) } \end{array} } \\ { \dot { \boldsymbol { x } } _ { 0 , 1 } } & { = \begin{array} { l } { i \omega \big ( z _ { h , 1 } ( 0 ) - \overline { { z } } _ { h , 1 } ( 0 ) \big ) + \mathcal { O } ( \omega ^ { - 1 } ) + \mathcal { O } \big ( z _ { h , 1 } ( 0 ) \big ) . } \end{array} } \end{array}
$$

With theweaker estimates for $z _ { h , 0 } ( t )$ and in (4.6）we still obtain estimates for the initial values of the type(3.16)with at most one factor $\omega ^ { - 1 }$ or $h$ less in theremainder terms.Condition (2.3） impliesagain $z _ { 1 } ( 0 ) = \mathcal { O } ( \omega ^ { - 1 } )$ ,which ensures that（4.5） holds for $0 \leq t \leq T .$ The defect is then $d _ { h } ( t ) = \mathcal { O } ( h ^ { 2 } )$ ,and as in part (a）we get the second-order error bound.

(c）Now let $\omega | \mathrm { s i n c } ( \scriptstyle { \frac { 1 } { 2 } } h \omega ) | \leq c$ ,sothat $h \omega$ is ${ \mathcal { O } } ( h )$ close to a multiple of $2 \pi$ In this case we replace the thirdequation in(3.11) simply by

$$
z _ { h , 0 } = 0 .
$$

Undercondition(4.1）we still obtain thebounds(4.5).The initial valuesare now chosen to satisfy

$$
\begin{array} { l } { { x _ { 0 , 0 } } } \\ { { { \dot { x } } _ { 0 , 1 } } \ = \ { z _ { h , 1 } } ( 0 ) + { \overline { { z } } _ { h , 1 } } ( 0 ) + { \omega ^ { - 2 } } \frac { \psi ( h \omega ) } { \mathrm { s i n c } ^ { 2 } \left( \frac { 1 } { 2 } h \omega \right) } { g _ { 1 } } ( \varPhi { x _ { 0 } } ) } \\ { { { \dot { x } } _ { 0 , 0 } } \ = \ { \dot { y } _ { h , 0 } } ( 0 ) } \\ { { { \dot { x } } _ { 0 , 1 } } \ = \ i \omega \big ( { z _ { h , 1 } } ( 0 ) - { \overline { { z } } _ { h , 1 } } ( 0 ) \big ) . } \end{array}
$$

Theyare thenbounded asin (b)and,by the argumentsused inthe determination of the initial values of Sect.XIII.3.2,yield the estimates $x _ { h } ( 0 ) \ = \ x _ { 0 } + \mathcal { O } ( h ^ { 3 } )$

and $x _ { h } ( h ) \ = \ x _ { 1 } + \mathcal { O } ( h ^ { 3 } )$ ,andagain $z _ { h , 1 } ( t ) ~ = ~ \mathcal { O } ( \omega ^ { - 1 } )$ Since（4.1） implies $\phi ( h \omega ) z _ { h , 1 } = \mathcal { O } ( \omega ^ { - 2 } )$ in the present situation of $| \mathrm { s i n c } ( \scriptstyle { \frac { 1 } { 2 } } h \omega ) | \leq c \omega ^ { - 1 }$ ,thedefect is still $d _ { h } ( t ) = \mathcal { O } ( h ^ { 2 } )$ Thebound(4.2） isalsoseen to hold.Therefore the second-order error bound remains valid in thiscase.

(d)If only $| \psi ( h \omega ) | \leq | \mathrm { s i n c } ( \frac { 1 } { 2 } h \omega ) |$ holds,then we replace the third equation in (3.11)by $z _ { h , 0 } = 0 ,$ If $\omega | \mathrm { s i n c } ( \scriptstyle { \frac { 1 } { 2 } } h \omega ) | \leq 1$ ,we also set $y _ { h , 1 } = 0$ Thedefect isthen only $d _ { h } ( t ) = \mathscr { O } ( h )$ ,which yields the first-order error bound. □

Forthe velocity approximation,we obtain the following for the method (2.12) oritsequivalent formulations.

Theorem4.2.Under theconditionsofTheorem4.1,considerthevelocityapproximationscheme(2.12)withafunction $\psi _ { 1 }$ satisfying $\psi _ { 1 } ( 0 ) = 1$ and

$$
\begin{array} { r } { | \psi _ { 1 } ( h \omega ) | \leq C _ { 1 } ^ { \prime } \left| \mathrm { s i n c } ( \frac { 1 } { 2 } h \omega ) \right| , } \end{array}
$$

Letthe starting values satisfy ${ \dot { x } } _ { 0 } = { \dot { x } } ( 0 )$ and ${ \dot { x } } _ { 1 } = { \dot { x } } ( h ) + h \sin ( h \Omega ) a _ { 1 } + { \mathcal { O } } ( h ^ { 2 } )$ with $a _ { 1 } = \mathcal { O } ( 1 )$ Then,theerrorinthevelocitiesisbounded by

$$
\| \dot { x } _ { n } - \dot { x } ( n h ) \| \leq C h f o r n h \leq T ,
$$

where $C$ isindependentof $\boldsymbol { \omega }$ ,hand $_ { f l }$ with $n h \le T$ andofbounds of solutionderivatives,butdepends on $x _ { i }$ on $E$ of(2.3),on boundsofderivatives ofthenonlinearity g, andon $C _ { 1 } , C _ { 2 } , C _ { 3 }$ and $C _ { 1 } ^ { \prime }$

Proof.(a)By the variation-of-constants formula(1.8),the exact solution satisfies

$$
\begin{array} { l } { \displaystyle \dot { x } ( t + h ) - 2 \cos ( h \Omega ) \dot { x } ( t ) + \dot { x } ( t - h ) } \\ { \displaystyle \qquad = \int _ { 0 } ^ { h } \cos \bigl ( ( h - s ) \Omega \bigr ) \Bigl ( g \bigl ( x ( t + s ) \bigr ) - g \bigl ( x ( t - s ) \bigr ) \Bigr ) d s . } \end{array}
$$

With the modulated Fourier expansion,wewrite the exact solution as

$$
x ( t ) = y ( t ) + e ^ { i \omega t } z ( t ) + e ^ { - i \omega t } \overline { { z } } ( t ) + \mathcal { O } ( \omega ^ { - 2 } )
$$

to obtain

$$
\begin{array} { r l } & { g \big ( x ( t + s ) \big ) - g \big ( x ( t - s ) \big ) } \\ & { \qquad = g ^ { \prime } \big ( y ( t ) \big ) \Big ( 2 s \dot { y } ( t ) - 4 \sin ( \omega s ) \operatorname { I m } \big ( e ^ { i \omega t } z ( t ) \big ) + \mathcal { O } ( s ^ { 2 } ) + \mathcal { O } ( \omega ^ { - 2 } ) \Big ) . } \end{array}
$$

Using the bounds(3.4),abbreviating $g _ { i , j } = \partial g _ { i } / \partial x _ { j }$ and omitting the arguments $t$ and $y ( t )$ ontheright-hand side,we therefore have

$$
\begin{array} { r l r } {  { \dot { x } ( t + h ) - 2 \cos ( h \itOmega ) \dot { x } ( t ) + \dot { x } ( t - h ) } } \\ & { } & { = ( \begin{array} { c c } { h ^ { 2 } g _ { 0 , 0 } \dot { y } _ { 0 } - 2 h ^ { 2 } \operatorname { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) \omega g _ { 0 , 1 } \operatorname { I m } { ( e ^ { i \omega t } z _ { 1 } ) } + \mathcal { O } ( h ^ { 3 } ) } \\ { h ^ { 2 } \operatorname { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) g _ { 1 , 0 } \dot { y } _ { 0 } - 2 h ^ { 2 } \operatorname { s i n c } ( h \omega ) \omega g _ { 1 , 1 } \operatorname { I m } { ( e ^ { i \omega t } z _ { 1 } ) } + \mathcal { O } ( h ^ { 3 } ) } \end{array} ) . } \end{array}
$$

Wenow use thediscrete variation-of-constants formula(4.4)and partial summation. For example,the expression

$$
\sum _ { j = 1 } ^ { n } \frac { \sin ( n + 1 - j ) h \omega } { \sin h \omega } \frac { 1 } { 2 } h ^ { 2 } \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) g _ { 1 , 0 } \big ( y ( j h ) \big ) \dot { y } _ { 0 } ( j h )
$$

is seen to be $\mathcal { O } ( h )$ uniformly in $h \omega$ and for $n h \leq T$ by partial summation,using that the function $g _ { 1 , 0 } ( y ( t ) ) \dot { y } _ { 0 } ( t )$ hasa bounded derivativeand that

$$
\frac { \sin ( \frac { 1 } { 2 } h \omega ) } { \sin ( h \omega ) } \sum _ { j = 1 } ^ { k } \sin ( j h \omega ) = \mathcal { O } ( k ) .
$$

In this way we obtain

$$
\begin{array} { l } { \dot { x } ( n h ) ~ = ~ - W _ { n - 1 } \dot { x } ( 0 ) + W _ { n } \dot { x } ( h ) } \\ { ~ + \left( { h \sum _ { j = 1 } ^ { n } ( n + 1 - j } ) h g _ { 0 , 0 } ( y ( j h ) ) \dot { y } _ { 0 } ( j h ) \right) + \mathcal { O } ( h ) . } \end{array}
$$

(b)For the numerical approximation weproceed similarly.Inserting themodulated Fourier expansion of the numerical solution,

$$
x _ { n } = y _ { h } ( t ) + e ^ { i \omega t } z _ { h } ( t ) + e ^ { - i \omega t } \overline { { z } } _ { h } ( t ) + \mathcal { O } ( h ^ { 2 } ) \mathrm { ~ f o r ~ } t = n h \leq T ,
$$

into the numerical scheme,we have with (3.12) or(4.5)

$$
\begin{array} { r l } & { \dot { \mathbf { \Omega } } _ { n + 1 } - 2 \cos ( h \omega ) \dot { x } _ { n } + \dot { x } _ { n - 1 } } \\ & { = h ^ { 2 } \left( \begin{array} { c } { g _ { 0 , 0 } \dot { y } _ { h , 0 } - 2 \phi ( h \omega ) \operatorname { s i n c } ( h \omega ) \omega g _ { 0 , 1 } \mathrm { I m } \left( e ^ { i \omega t } z _ { h , 1 } \right) + \mathcal { O } ( h ) } \\ { \psi _ { 1 } ( h \omega ) g _ { 1 , 0 } \dot { y } _ { h , 0 } - 2 \left( \psi _ { 1 } \phi \right) ( h \omega ) \operatorname { s i n c } ( h \omega ) \omega g _ { 1 , 1 } \mathrm { I m } \left( e ^ { i \omega t } z _ { h , 1 } \right) + \mathcal { O } ( h ) } \end{array} \right) } \end{array}
$$

where the functions $y _ { i , j }$ are evaluated at $\Phi y _ { h } ( t )$ and theargument $t = n h$ istobe inserted in $y _ { h , 0 }$ and $z _ { h , 1 }$ Under the condition（4.8）on $\psi _ { 1 }$ ,we obtain as in (4.9)

$$
\begin{array} { r l } { \dot { x } _ { n } ~ = ~ - W _ { n - 1 } \dot { x } _ { 0 } + W _ { n } \dot { x } _ { 1 } } & { } \\ & { ~ + \left( { h } \sum _ { j = 1 } ^ { n } ( { n } + 1 - j ) { h } { g } _ { 0 , 0 } ( \phi { y } _ { h } ( j h ) ) \dot { y } _ { h , 0 } ( j h ) \right) + \mathcal { O } ( h ) . } \end{array}
$$

Sinceweknow from theestimates(3.12) and fromtheproof of Theorem 4.1 that $\varPhi y _ { h } ( t ) = y ( t ) + \mathcal { O } ( h ^ { 2 } )$ and $\dot { y } _ { h } ( t ) = \dot { y } ( t ) + \mathcal { O } ( h ^ { 2 } )$ ,acomparison of(4.9)and(4.10) gives the result. □

# XIII.4.2 Intra-Oscillatory and Oscillatory-Smooth Exchanges

In this subsection we turn to the approximation of slow effects that take place on the time scale $\omega$ Since solutions may depart from each other exponentially,we cannot expect to obtain small point-wise error bounds on such a time scale.Instead, wetakerecourse toa kind of formal backward erroranalysiswherewe require thatthe equations determining the modulated Fourier expansion coefficients for the numerical method be small perturbations of those for the exact solution.It may be expected that methodswith this property-ceteribusparis-showabetter long-time behaviour,and thisis indeed confirmed by the numerical experiments.

In theFermi-Pasta-Ulam model,the oscillatory energy of the $j$ th stiff spring is

$$
\begin{array} { r } { I _ { j } = \frac { 1 } { 2 } \dot { x } _ { 1 , j } ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } x _ { 1 , j } ^ { 2 } , } \end{array}
$$

where x1,is the $\mathcal { I }$ th component of the lower block $x _ { 1 }$ of $x$ .Interms of the modulatedFourier expansion,this is approximately,up to $\mathcal { O } ( \omega ^ { - 1 } )$ ,

$$
\begin{array} { r } { \tilde { \mathbf { \Phi } } _ { j } \approx \frac { 1 } { 2 } \big | i \omega \bar { z } _ { 1 , j } e ^ { i \omega t } - i \omega \overline { { z } } _ { 1 , j } e ^ { - i \omega t } \big | ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } \big | z _ { 1 , j } e ^ { i \omega t } + \overline { { z } } _ { 1 , j } e ^ { - i \omega t } \big | ^ { 2 } = 2 \omega ^ { 2 } | z _ { 1 , j } | ^ { 2 } } \end{array}
$$

Theenergy exchange between stiff springs as shownin Fig.2.1is thus caused by the slow evolution of $z _ { 1 }$ determinedby(3.3).Thisshould bemodeled correctly by thenumerical method.

Theterm $g _ { 0 } ^ { \prime \prime } ( y ) ( z , \overline { { z } } )$ in the differential equation for $y _ { 0 }$ in（3.3)is the dominant termbywhich the oscillations of the stiff springs exert aninfluence on the smooth motion.A correct incorporation of this term in the numerical method is desirable.

Upon eliminating $y _ { 1 }$ and $z _ { 0 }$ in (3.3),the differential equations for $y _ { 0 }$ and $z _ { \mathrm { 1 } }$ become,up to $\textcircled { \scriptsize { 2 } } ( \omega ^ { - 3 } )$ perturbations on the right-hand sides,

$$
\begin{array} { r c l } { { \displaystyle \ddot { y } _ { 0 } ~ = ~ g _ { 0 } ( y _ { 0 } , \omega ^ { - 2 } g _ { 1 } ( y _ { 0 } , 0 ) ) \dot { + \frac { \partial ^ { 2 } g _ { 0 } } { \partial x _ { 1 } ^ { 2 } } ( y _ { 0 } , 0 ) ( z _ { 1 } , \overline { { { z } } } _ { 1 } ) } } } \\ { { \displaystyle 2 i \omega \dot { z } _ { 1 } ~ = ~ \frac { \partial g _ { 1 } } { \partial x _ { 1 } ^ { - } } ( y _ { 0 } , 0 ) z _ { 1 } . . } } \end{array}
$$

Thisis to be compared withthe analogous equations forthe modulated Fourier expansion of the numerical method,which follow from(3.11):

$$
\begin{array} { l } { { \displaystyle \delta _ { h } ^ { 2 } y _ { h , 0 } ~ = ~ g _ { 0 } ( y _ { h , 0 } , \gamma \omega ^ { - 2 } g _ { 1 } ( y _ { h , 0 } , 0 ) ) + \beta \frac { \partial ^ { 2 } g _ { 0 } } { \partial x _ { 1 } ^ { 2 } } ( y _ { h , 0 } , 0 ) ( z _ { h , 1 } , \overline { { { z } } } _ { h , 1 } ) } } \\ { { \displaystyle 2 i \omega \ddot { z } _ { h , 1 } ~ = ~ \alpha \frac { \partial g _ { 1 } } { \partial x _ { 1 } } ( y _ { h , 0 } , 0 ) z _ { h , 1 } } } \end{array}
$$

with

$$
\alpha = \frac { ( \psi \phi ) ( h \omega ) } { \operatorname { s i n c } ( h \omega ) } , \quad \beta = \phi ( h \omega ) ^ { 2 } , \quad \gamma = \frac { ( \psi \phi ) ( h \omega ) } { \operatorname { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) } .
$$

The differential equation for $z _ { h , 1 }$ is consistent with that for $z _ { \mathrm { 1 } }$ only if $\alpha = 1$ ,i.e.,

$$
\psi ( h \omega ) \phi ( h \omega ) = \mathrm { s i n c } ( h \omega ) .
$$

Amongall the methods(2.6) considered,only the Deuflhard/impulse method（ $\psi =$ sinc, $\phi = 1$ ）satisfies this condition.For thismethod we indeed observea qualitatively correct approximation of the energyexchange between stiff springsin

Fig.2.4,but we havealso seen that the energy conservation of this method is very sensitive to near-resonances.

Acorrect modeling of the slow oscillatory-smooth transfer would in addition require $\beta = 1$ and possibly $\gamma = 1$ Forgeneral $h \omega$ the condition $\gamma = 1$ is,however, incompatiblewith (4.14).

Multi-forcemethods(2.13) offeraway out of these difficulties.Forsuch methods,the coefficients of themodulated Fourier expansion satisfy(4.12)with (4.13) replaced by

$$
\begin{array} { l } { { \displaystyle \alpha = \frac { \sum _ { j } \psi _ { j } ( h \omega ) \phi _ { j } ( h \omega ) } { \sin \cos ( h \omega ) } _ { \ast } ~ \beta = \sum _ { j } \psi _ { j } ( 0 ) \phi _ { j } ( h \omega ) ^ { 2 } , } } \\ { { \displaystyle \gamma = \sum _ { j } \psi _ { j } ( 0 ) \phi _ { j } ( h \omega ) \frac { \sum _ { k } \psi _ { k } ( h \omega ) } { \sin \cos ^ { 2 } ( \frac { 1 } { 2 } h \omega ) } . } } \end{array}
$$

Thetwo-force method(1.23)with(1.25) has $\alpha = \beta = \gamma = 1$ asdesired.

# XIII.5Modulated Fourier Expansions

The decomposition of the exact and the numerical solution into modulated exponentialsandaremainder,as derived in Sect.XIII.3,was founduseful for understanding several important aspects of the numerical behaviour.Those few termsare,however,not sufficient for explaining the long-time near-conservation of the total and theoscillatory energy.The expansioncan be mademore accurate by adding further terms $e ^ { \pm 2 \imath \omega t }$ , $e ^ { \pm 3 i \omega t }$ etc.multiplied by slowlyvarying functions.This leads toan asymptotic expansion which wecall the modulated Fourier expansion.This expansionis constructed in the present section,following Hairer&Lubich(2ooOa).(In that paper the modulated Fourier expansion was called the frequency expansion.)

# XIII.5.1 Expansion of the Exact Solution

Thefollowingtheorem extends the construction of Sect.XII.3.1to arbitrary order in $\omega ^ { - 1 }$

Theorem5.1. Considera solution $x ( t )$ of(2.1)which satisfies the bounded-energy condition(2.3) and staysina compact set $K$ for $0 \leq t \leq I ^ { \prime }$ Then,thesolution admitsan expansion

$$
x ( t ) = y ( t ) + \sum _ { 0 < | k | < N } e ^ { i k \omega t } z ^ { k } ( t ) + R _ { N } ( t )
$$

forarbitrary $N \geq 2$ ,wheretheremainder termand its derivativeare boundedby

$$
R _ { N } ( t ) = \mathcal { O } ( \omega ^ { - N - 2 } ) \quad a n d \quad \dot { R } _ { N } ( t ) = \mathcal { O } ( \omega _ { - } ^ { - N - 1 } ) \quad f o r \quad 0 \le t \le T .
$$

The real-valued functions $\boldsymbol { y } ~ = ~ ( y _ { 0 } , y _ { 1 } )$ andthe complex-valued functions $z ^ { k } =$ $( z _ { 0 } ^ { k } , z _ { 1 } ^ { k } )$ togetherwithalltheirderivatives(uptoarbitrary order $M$ arebounded by

$$
\begin{array} { l l l } { { y _ { 0 } = \mathcal { O } ( 1 ) , } } & { { z _ { 0 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 3 } ) , } } & { { z ^ { k } = \mathcal { O } ( \omega ^ { - k - 2 } ) } } \\ { { y _ { 1 } = \mathcal { O } ( \omega ^ { - 2 } ) , } } & { { z _ { 1 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 1 } ) , } } & { { } } \end{array}
$$

for $k = 2 , \ldots , N - 1$ Moreover, $z ^ { - k } = z ^ { k }$ for all $k$ .These functions areunique up to terms of size $O ( \omega ^ { - N - 2 } )$ Theconstants symbolized by the $\mathcal { O }$ -notationare independentof $\boldsymbol { \omega }$ andtwith $0 \leq t \leq T$ (but they depend on $\mathcal { N }$ , $T$ on $E$ of（2.3）,on boundsof thederivativesofthenonlinearity $g ( x )$ on $K$ ,andon themaximumorder $M$ ofconsideredderivatives).

ProofWe set

$$
x _ { * } ( t ) = y ( t ) + \sum _ { 0 < | k | < \mathbb { V } } e ^ { i k \omega t } z ^ { k } ( t )
$$

and determine the smooth functions $y ( t )$ $z ( t ) = z ^ { 1 } ( t )$ ,and $z ^ { 2 } ( t ) , \ldots , z ^ { N - 1 } ( t )$ such that $x _ { * } ( t )$ inserted into thedifferential equation (2.1）hasasmall defect,of size ${ \mathcal { O } } ( \omega ^ { - N } ) .$ To this end we expand $g ( x _ { * } ( t ) )$ around $y ( t )$ and compare the coefficients of $e ^ { \imath k \omega t }$ With the notation $g ^ { ( m ) } ( y ) z ^ { \alpha } = g ^ { ( m ) } ( y ) ( z ^ { \alpha _ { 1 } } , . . . , z ^ { \alpha _ { m } } )$ foramulti-index $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ ,thereresultsthe followingsystem ofdifferential equations:

$$
\begin{array} { c } { { \displaystyle \left( \begin{array} { c } { { \bar { y } _ { 0 } } } \\ { { \omega ^ { 2 } y _ { 1 } } } \end{array} \right) + \left( \begin{array} { c } { { 0 } } \\ { { \bar { y } _ { 1 } } } \end{array} \right) = g ( y ) + \displaystyle \sum _ { s ( \alpha ) = 0 } \frac 1 { m ! } g ^ { ( m ) } ( y ) z ^ { \alpha } } } \\ { { \displaystyle \left( \begin{array} { c } { { - \omega ^ { 2 } z _ { 0 } } } \\ { { 2 i \omega \dot { z } _ { 1 } } } \end{array} \right) + \left( \begin{array} { c } { { 2 i \omega \dot { z } _ { 0 } + \ddot { z } _ { 0 } } } \\ { { \bar { z } _ { 1 } } } \end{array} \right) = \sum _ { s ( \alpha ) = 1 } \frac 1 { m ! } g ^ { ( m ) } ( y ) z ^ { \alpha } } } \\ { { \displaystyle \left( \begin{array} { c } { { - k ^ { 2 } \omega ^ { 2 } z _ { 0 } ^ { k } } } \\ { { ( 1 - k ^ { 2 } ) \omega ^ { 2 } z _ { 1 } ^ { k } } } \end{array} \right) + \left( \begin{array} { c } { { 2 k i \omega \dot { z } _ { 0 } ^ { k } + \ddot { z } _ { 0 } ^ { k } } } \\ { { 2 k i \omega \dot { z } _ { 1 } ^ { k } + \ddot { z } _ { 1 } ^ { k } } } \end{array} \right) = \sum _ { s ( \alpha ) = k } \frac 1 { m ! } g ^ { ( m ) } ( y ) z ^ { \alpha } . } } \end{array}
$$

Here the Imsi $m \geq 1$ $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ vih $\alpha _ { j }$ $0 < | \alpha _ { j } | < N _ { ☉ }$ $\begin{array} { r } { s ( \alpha ) = \sum _ { j = 1 } ^ { m } \alpha _ { j } } \end{array}$

Forlarge $\omega$ ,the dominating terms in these differential equations are given by the left-most expressions.However,since the central terms involve higher derivatives, weare confrontedwith singular perturbation problems.We are interested in smooth functions $y , z , z ^ { k }$ that satisfy the system up toa defect of size ${ \mathcal { O } } ( \omega ^ { - N } ) .$ In the spirit ofEuler'sderivation of the Euler-Maclaurin summation formula(see e.g.Hairer& Wanner 1997）weremove thedisturbing higherderivatives byusing iteratively the differentiated equations(5.5)-(5.7).This leads toasystem

$$
\begin{array} { r l } & { \ddot { y } _ { 0 } = \mathcal { F } _ { 0 } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) , \qquad \dot { z } _ { 1 } = \omega ^ { - 1 } \mathcal { F } _ { 1 } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) , } \\ & { z _ { 0 } = \omega ^ { - 2 } \mathcal { G } _ { 0 } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) , \ \dot { y } _ { 1 } = \omega ^ { - 2 } \mathcal { G } _ { 1 } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) , } \\ & { z _ { 0 } ^ { k } = \omega ^ { - 2 } \mathcal { G } _ { 0 } ^ { k } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) , \ z _ { 1 } ^ { k } = \omega ^ { - 2 } \mathcal { G } _ { 1 } ^ { k } ( \dot { y } _ { 0 } , y , z ^ { 1 } , \dots , z ^ { N - 1 } , \omega ^ { - 1 } ) . } \end{array}
$$

where $\mathcal { F } _ { j } , \mathcal { G } _ { j } , \mathcal { G } _ { j } ^ { k }$ are formal series in powers of $\omega ^ { - 1 }$ Sinceweget formal algebraic relations for $y _ { 1 } , z _ { 0 } , z ^ { k }$ ,wecan further eliminate thesevariablesin the functions $\mathcal { F } _ { j } , \mathcal { G } _ { j } , \mathcal { G } _ { j } ^ { k } .$ We finally obtain for $y _ { 1 } , z _ { 1 } , z ^ { k }$ thealgebraicrelations

$$
\begin{array} { r l } & { z _ { 0 } = \omega ^ { - 2 } \big ( G _ { 0 0 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } G _ { 0 1 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . \big ) } \\ & { y _ { 1 } = \omega ^ { - 2 } \big ( G _ { 1 0 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } G _ { 1 1 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . \big ) } \\ & { z _ { 0 } ^ { k } = \omega ^ { - 2 } \big ( G _ { 0 0 } ^ { k } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } G _ { 0 1 } ^ { k } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . \big ) } \\ & { z _ { 1 } ^ { k } = \omega ^ { - 2 } \big ( G _ { 1 0 } ^ { k } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } G _ { 1 1 } ^ { k } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . \big ) } \end{array}
$$

andasystem of real second-order differential equations for $y _ { 0 }$ and complex firstorder differential equations for $z _ { 1 }$ :

$$
\begin{array} { l } { { \ddot { y } _ { 0 } ~ = ~ F _ { 0 0 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } F _ { 0 1 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . . } } \\ { { \dot { z } _ { 1 } ~ = ~ \omega ^ { - 1 } \big ( F _ { 1 0 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + \omega ^ { - 1 } F _ { 1 1 } ( y _ { 0 } , \dot { y } _ { 0 } , z _ { 1 } ) + . . . \big ) . } } \end{array}
$$

Atthis pointwe can forget the above derivationand take itasa motivation for the ansatz(5.8)-(5.9),which is truncated after the $\mathcal { O } ( \omega ^ { - N } )$ terms.We insert this ansatz and its first and secondderivatives into(5.5)-(5.7）and comparepowers of $\omega ^ { - 1 } .$ This yieldsecurceaifoucos $F _ { j l } ^ { k } , G _ { j l } ^ { k }$ whichinadditionhowthat these functions together with their derivatives are all bounded on compact sets.

Wedetermine initial values for(5.9) such that the function $x _ { * } ( t )$ of(5.4）satisfies $x _ { * } ( 0 ) = x _ { 0 }$ and $\dot { x } _ { * } ( 0 ) = \dot { x } _ { 0 }$ .Because of the special ansatz(5.8)-(5.9),this givesa systemwhich,by fixed-point iteration,yields(locally）unique initial values $y _ { 0 } ( 0 )$ , $\dot { y } _ { 0 } ( 0 )$ , $z _ { 1 } ( 0 )$ satisfying(3.5).The assumption(2.3)impliesthat $z _ { 1 } ( 0 ) = { \cal O } ( \omega ^ { - 1 } ) .$ It further follows from the boundednessof $F _ { 1 l }$ that $z _ { 1 } ( t ) = O ( \omega ^ { - 1 } )$ for $0 \leq t \leq T$ . Goingbackto5 $G _ { j l } ^ { k }$ contain at least $k$ times the factor $z _ { 1 }$ .Thisimplies the stated bounds forall other functions.

Itremains to estimate the error $R _ { N } ( t ) = x ( t ) - x _ { * } ( t )$ For this we consider the solution of(5.8)-(5.9）with the above initial values.By construction,these functions satisfy the system（5.5)-(5.7)uptoadefect of $\mathcal { O } ( \omega ^ { - N } ) .$ This gives a defect of size $\mathcal { O } ( \omega ^ { - N } )$ when the function $x _ { * } ( t )$ of(5.4）isinsertedinto(2.1）.Ona finite time interval $0 \leq t \leq T$ ,thisimplies $R _ { N } ( t ) = \mathcal { O } ( \omega ^ { - N } )$ and $\dot { R } _ { N } ( t ) = \mathcal { O } ( \omega ^ { - N } ) .$ To obtain the slightly sharper bounds (5.2),we apply the above proof with $N$ replaced by $N + 2$ anduse the bounds(5.3）for $z ^ { N }$ and $z ^ { N + 1 }$ , □

# XIII.5.2 Expansion of the Numerical Solution

Does the numerical solution of (2.1） have a modulated Fourier expansion similar totheanalytical solution?This may of course be expected,but in Sect.XII1.3.2 weencountered difficulties in constructing the first terms of the expansion in the situation ofanumerical resonance where $h \omega$ isclose to an integral multipleof $\pi$ . Wetherefore confine the discussion to the non-resonant case.We assume that $h$ and $\omega ^ { - 1 }$ lie ina subregion of the $( h , \omega ^ { - 1 } )$ -planeof small parameters forwhich there existsa positive constant $c$ such that

$$
| \sin ( { \frac { 1 } { 2 } } k h \omega ) | \geq c { \sqrt { h } } \qquad \mathrm { f o r } \ k = 1 , . . . , N _ { \mathrm { s } } \ \mathrm { w i t h } \ N \geq 2 .
$$

This condition implies that $h \omega$ is outsidean $\mathcal { O } ( \sqrt { h } )$ neighbourhood of integral multiples of $\pi$ Forgiven $h$ and $\omega$ ,thecondition imposes a restriction on $N$ Inthe following, $N$ isafixed integer such that(5.1O) holds.There is the following numerical analogue of Theorem5.1.

Theorem 5.2. Consider the numerical solutionofthe system $( 2 . I ) - ( 2 . 3 )$ bymethod (2.6)with step size h.Let the startingvalue $x _ { 1 }$ begivenby（2.7）with $n = 0$ .Assume $h \omega \geq c _ { 0 } > 0$ ,thenon-resonancecondition(5.1O),andthebounds(4.1) for $\psi ( h \omega )$ and $\phi ( h \omega )$ Then,thenumerical solutionadmitsanexpansion

$$
x _ { n } = y _ { h } ( t ) + \sum _ { 0 < | k | < N } e ^ { i k \omega t } z _ { h } ^ { k } ( t ) + R _ { h , N } ( t )
$$

uniformly for $0 \leq t = n h \leq T .$ Theremaindertermisoftheform

$$
R _ { h , N } ( t ) = t ^ { 2 } h ^ { N } \varPsi r ( t ) \quad w i t h \quad r ( t ) = \mathcal { O } \big ( \phi ( h \omega ) ^ { N } + h ^ { m } \big ) ,
$$

where $m \geq 0$ canbechosenarbitrarily.Thecoefficient functionstogetherwithall theirderivatives(uptosomearbitrarilyfixedorder)arebounded by

$$
\begin{array} { l l l } { y _ { h , 0 } = \mathcal { O } ( 1 ) _ { \mathfrak { s } } } & { z _ { h , 0 } ^ { 1 } \equiv \mathcal { O } ( \omega ^ { - 2 } ) , } & { z _ { h , 0 } ^ { k } \equiv \mathcal { O } ( \omega ^ { - k } ) , } \\ { y _ { h , \bar { 1 } } = \mathcal { O } ( \omega ^ { - 2 } ) , } & { z _ { h , 1 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 1 } ) , } & { z _ { h , 1 } ^ { k } = \mathcal { O } ( \omega ^ { - k } ) } \end{array}
$$

for $k = 2 , \ldots , N - 1$ Moreover, $z _ { h } ^ { - k } = z _ { h } ^ { k }$ for all $k$ Theconstants symbolized by the $\mathcal { O }$ -notationareindependentof $\omega$ and $h$ with(5.1O),buttheydependon $E$ ， $N$ , $m$ ， $c ,$ and $T$ .

The proof covers the remainder of this subsection.It constructs a function

$$
x _ { h } ( t ) = y _ { h } ( t ) + \sum _ { 0 < | k | < N } e ^ { i k \omega t } z _ { h } ^ { k } ( t )
$$

with smooth coefficient functions $y _ { h } ( t )$ and $z _ { h } ^ { k } ( t )$ ,which hasasmall defectwhen itisinserted into the numerical scheme(2.6).The following functional calculus is convenient for determining the coefficient functions.

Functional Calculus.Let $f$ bean entire complex function bounded by $| f ( \zeta ) | \leq$ $C e ^ { \gamma \vert \zeta \vert } .$ Then,

$$
f ( h D ) x ( t ) = \sum _ { k = 0 } ^ { \infty } { \frac { f ^ { ( k ) } ( 0 ) } { k ! } } h ^ { k } x ^ { ( k ) } ( t )
$$

converges forevery function $x$ whichisanalytic inadisk of radius $r > \gamma h$ around $t$ If $f _ { 1 }$ and $f _ { 2 }$ are two such entire functions, then

$$
f _ { 1 } ( h D ) f _ { 2 } ( h D ) x ( t ) = ( f _ { 1 } f _ { 2 } ) ( h D ) x ( t )
$$

whenever both sides exist.We note $( h D ) ^ { k } x ( t ) = h ^ { k } x ^ { ( k ) } ( t )$ for $k = 0 , 1 , 2 , \ldots$ and $\exp ( h D ) x ( t ) = x ( t + h )$

Wenext consider the application of such an operator to functions of the form $e ^ { i \omega t } z ( t )$ ByLeibniz’rule of calculuswe have $( h D ) ^ { k } e ^ { i \omega t } z ( t ) ~ = ~ e ^ { i \omega t } ( h D +$ $i h \omega ) ^ { k } z ( t )$ Afterashort calculation this yields

$$
f ( h D ) e ^ { i \omega t } z ( t ) = e ^ { i \omega t } f ( h D + i h \omega ) z ( t )
$$

$\begin{array} { r } { f ( h D + i h \omega ) z ( t ) = \sum _ { k = 0 } ^ { \infty } f ^ { ( k ) } ( i h \omega ) / k ! \cdot h ^ { k } z ^ { ( k ) } ( t ) . } \end{array}$

An $N$ -timescontinuouslydifferentiablefunction $_ { x }$ isreplaced by its Taylor polynomial of degree $N - 1$ at $t$ ,and $f ( h D ) x ( t )$ is then considered up to $\mathcal { O } ( h ^ { N } )$ .

Modified Equations for the Coeffcient Functions.The difference operator of the numerical method becomes in this notation

$$
x ( t + h ) - 2 \cos h \Omega x ( t ) + x ( t - h ) = ( e ^ { h D } - 2 \cos h \Omega + e ^ { - h D } ) x ( t ) .
$$

Wefactorize this operatoras

$$
\begin{array} { r c l } { { { \mathcal L } ( h D ) } } & { { : = } } & { { e ^ { h D } - 2 \cos h \Omega + e ^ { - h D } = 2 \big ( \cos ( i h D ) - \cos h \Omega \big ) } } \\ { { } } & { { = } } & { { 4 \sin \big ( \frac { 1 } { 2 } h \Omega + \frac { 1 } { 2 } i h D \big ) \sin \big ( \frac { 1 } { 2 } h { \mathcal Q } = \frac { 1 } { 2 } i h D \big ) , } } \end{array}
$$

The function $x _ { h } ( t )$ of(5.14)should formally (up to $\mathcal { O } ( h ^ { N + 2 } )$ satisfythedifference scheme

$$
\begin{array} { r } { \mathcal { L } ( h D ) x _ { h } ( t ) = h ^ { 2 } \varPsi g \big ( \varPhi x _ { h } ( t ) \big ) . } \end{array}
$$

Weinsert theansatz(5.14),expand the right-hand sideintoa Taylor series around $\varPhi y _ { h } ( t )$ ,and compare the coefficients of $e ^ { 2 k \omega t }$ Thisyields the following formal equations for thefunctions $y _ { h } ( t )$ and $z _ { h } ^ { k } ( t )$ :

$$
\begin{array} { c } { { \mathcal { L } ( h D ) y _ { h } ~ = ~ h ^ { 2 } \bar { \varPsi } \Bigl ( g ( \varPhi y _ { h } ) + \displaystyle \sum _ { s ( \alpha ) = 0 } \frac { 1 } { m ! } g ^ { ( m ) } ( \varPhi y _ { h } ) ( \varPhi z _ { h } ) ^ { \alpha } \Bigr ) } } \\ { { \mathcal { L } ( h D + i k h \omega ) z _ { h } ^ { k } ~ = ~ h ^ { 2 } \bar { \varPsi } \displaystyle \sum _ { s ( \alpha ) = k } \frac { 1 } { m ! } g ^ { ( m ) } ( \varPhi y _ { h } ) ( \varPhi z _ { h } ) ^ { \alpha } . } } \end{array}
$$

Here, $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ isamulti-index as in the proof of Theorem5.1, $s ( \alpha ) =$ $\sum j = 1  { \alpha } _ { j }$ ,and $( \varPhi z ) ^ { \alpha }$ is anabbreviation for the $f / l$ -tupel $( \phi z ^ { \alpha _ { 1 } } , \ldots , \phi z ^ { \alpha _ { m } } ) ,$ Toget smooth functions $y _ { h } ( t )$ and $z _ { h } ^ { k } ( t )$ which solve(5.18)up toa small defect,we look at thedominating terms in the Taylor expansions of $\mathcal { L } ( h D )$ and $C ( h D + i k h \omega ) .$ With theabbreviations $s _ { k } = \sin ( \frac { 1 } { 2 } k h \omega )$ and $c _ { k } = \cos ( \frac { 1 } { 2 } k h \omega )$ we obtain

$$
\begin{array} { r l r } & { } & { { \mathcal L } ( h D ) = { \tiny \begin{array} { c c } { ( 0  } & { 0 } \\ { 0 } & { 4 s _ { 1 } ^ { 2 } } \end{array} } ) - { \tiny \begin{array} { c c } { ( 1 } & { 0 } \\ { 0 } & { 1 } \end{array} ) } ( i h D ) ^ { 2 } + \tiny { \cdot } \ d s . } \\ & { } & { { \mathcal L } ( h D + i h \omega ) = { \tiny \begin{array} { c c } { ( - 4 s _ { 1 } ^ { 2 } } & { 0 ) } \\ { 0 } & { 0 } \end{array} } + 2 s _ { 2 } { \tiny \begin{array} { c c } { ( \frac { 1 } { 2 } } & { 0 } \\ { 0 } & { 1 } \end{array} ) } ( i h D ) } \end{array}
$$

$$
\begin{array}{c} { \begin{array} { r l } & { - c _ { 2 } \left( { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right) ( i h D ) ^ { 2 } + \dots , \qquad ( 5 . 1 9 ) } \\ & { { \begin{array} { r c r } { { \angle } ( h D + i k h \omega ) } & { = : { \left( { \begin{array} { c c } { - 4 s _ { k } ^ { 2 } } & { 0 } \\ { 0 } & { - 4 s _ { k - 1 } s _ { k \neq 1 } } \end{array} } \right) } + 2 s _ { 2 k } \left( { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right) ( i h D ) } \end{array} } } \\ & { \qquad - { \bar { c } } _ { 2 k } \left( { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right) ( i h D ) ^ { 2 } + \dots . } \end{array} }  \end{array} 
$$

Construction of the Coefficient Functions.Under the non-resonance condition (5.10),the first non-vanishing coefficients in(5.19)are the dominant ones,and the derivation of thedefining relations for $y _ { h }$ and $z _ { h } ^ { k }$ is the same as for theanalytical solutionin Theorem5.1;seealsopart（b）of theproof of Theorem4.1.We insert (5.19)into(5.18)and weeliminaterecursivelythe higherderivatives.This motivates thfol $y _ { h }$ and $z _ { h } ^ { k }$

$$
\begin{array} { r l } & { \hat { \psi } _ { b , 0 } = f _ { 0 0 } ( \pmb { \hat { \psi } } ) + \sqrt { h } f _ { 0 0 } ( \pmb { \hat { \psi } } ) + h f _ { 0 2 } ( \pmb { \hat { \psi } } ) + \dots , } \\ & { \hat { \psi } _ { b , 1 } ^ { ( \pmb { \hat { \psi } } ) } , } \\ & { \hat { z } _ { b , 1 } ^ { \pm } = \frac { \psi ( h \omega ) h ^ { 2 } } { \delta _ { 0 } ^ { 2 } } \bigg ( f _ { 1 0 } ( \pmb { \hat { \psi } } ) + \sqrt { h } f _ { 1 1 } ( \pmb { \hat { \psi } } ) + \dots \bigg ) } \\ & { z _ { b , 0 } ^ { \pm } = \frac { h ^ { 2 } } { s _ { 0 } ^ { 2 } } \bigg ( g _ { 0 0 } ^ { \pm } ( \pmb { \hat { \psi } } ) + \sqrt { h } g _ { 0 1 } ^ { \pm } ( \pmb { \hat { \psi } } ) + \dots \bigg ) } \\ & { y _ { b , 1 } = \frac { \psi ( h \omega ) h ^ { 2 } } { \delta _ { 0 } ^ { 2 } } \bigg ( g _ { 1 0 } ( \pmb { \hat { \psi } } ) + \sqrt { h } g _ { 1 1 } ( \pmb { \hat { \psi } } ) + \dots \bigg ) } \\ & { z _ { b , 0 } ^ { \pm } = \frac { h ^ { 2 } } { s _ { 0 } ^ { 2 } } \bigg ( g _ { 0 0 } ^ { \pm } ( \pmb { \hat { z } } ) + \sqrt { h } g _ { 0 1 } ^ { \pm } ( \pmb { \hat { \psi } } ) + \dots \bigg ) } \\ & { z _ { b , 1 } ^ { \pm } = \frac { \psi ( h \omega ) h ^ { 2 } } { \delta _ { 0 } ^ { 2 } \kappa _ { b - 1 } ^ { 2 } } \bigg ( g _ { 1 0 } ^ { \pm } ( \pmb { \hat { z } } ) + \sqrt { h } g _ { 1 1 } ^ { \pm } ( \pmb { \hat { z } } ) + \dots \bigg ) . } \end{array}
$$

for $k = 2 , \ldots , N - 1$ ,where the functions depend smoothly on thevariables $y _ { h , 0 }$ , $\Dot { y } _ { h , 0 }$ , $\phi ( h \omega ) z _ { h , 1 } ^ { 1 }$ and on the bounded parameters $\sqrt { h } / s _ { k }$ ， $s _ { k }$ ， $c _ { k }$ ， $\psi ( h \omega )$ and $( h \omega ) _ { - } ^ { - 1 }$ .Inserting thisansatz and its derivatives into(5.18)andcomparing powers of $\sqrt { h }$ yieldsecurrenerelatisforthefutios $f _ { j l } ^ { k }$ , $g _ { j l } ^ { k }$ The functions $g _ { j l } ^ { k }$ (for $k \geq 1$ ）contain atleast $k$ times the factor $\phi ( h \omega ) { z } _ { h , 1 } ^ { 1 }$ ,and $f _ { 1 i }$ contains this factor at least once.Since the series in（5.2O） need not converge,we truncate them after the $h ^ { N + m + 2 }$ terms.

Initial Values.The conditions $x _ { h } ( 0 ) = x _ { 0 }$ and $x _ { h } ( h ) = x _ { 1 }$ determine the initial values $y _ { h , 0 } ( 0 )$ , $\dot { y } _ { h , 0 } ( 0 )$ and $z _ { h , 1 } ( 0 )$ inthesame way asin Sect.XIII.3.2.Condition (4.1)yields again(4.6),and(2.3)then implies $z _ { h , 1 } ( 0 ) = \mathcal { O } ( \omega ^ { - 1 } )$

Defect.It follows from(4.1）that $h \psi ( h \omega ) \phi ( h \omega ) / s _ { 2 } = \mathcal { O } ( \omega ^ { - 1 } )$ ,sothat $\dot { z } _ { h , 1 } ^ { 1 } =$ $O ( \omega ^ { - 1 } z _ { h , 1 } ^ { 1 } )$ by (5.20).This implies $z _ { h , 1 } ^ { 1 } ( t ) = \mathcal { O } ( \omega ^ { - 1 } )$ for $t \leq { \mathcal { I } } .$ The other estimates(5.i3）aredirectly obtained from(5.2O),which indeed yieldsthe following morerefined bounds for the coefficient functions togetherwith theirderivatives:

$$
\begin{array} { r l } & { y _ { h , 0 } = \mathcal { O } ( 1 ) , \quad y _ { h , 1 } = \mathcal { O } ( \omega ^ { - 2 } ) } \\ & { z _ { h , 0 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 3 } / \sqrt { h } ) , \quad z _ { h , 1 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 1 } ) , \quad \dot { z } _ { h , 1 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 2 } ) } \\ & { z _ { h , 0 } ^ { k } = \mathcal { O } ( h \phi ( h \omega ) ^ { k } \omega ^ { - k } ) , \quad z _ { h , 1 } ^ { k } = \mathcal { O } ( h \psi ( h \omega ) \phi ( h \omega ) ^ { k } \omega ^ { - k } ) . } \end{array}
$$

Consequentlythevalues $x _ { h } ( n h )$ inserted into thenumerical scheme (2.6) yield a defect of size $\mathcal { O } ( h ^ { N + 2 } )$ :

$$
\begin{array} { r l } & { x _ { h } ( t + h ) - 2 \cos ( h \Omega ) x _ { h } ( t ) + x _ { h } ( t - h ) = } \\ & { \qquad = h ^ { 2 } \varPsi \Bigl ( g ( \varPhi x _ { h } ( t ) ) + \varTheta \bigl ( \phi ( h \omega ) ^ { N } \omega ^ { - N } + h ^ { N + m } \bigr ) \Bigr ) . } \end{array}
$$

Standard convergence estimates then show that,onboundedtime intervals, $x _ { n } \mathrm { ~ - ~ }$ $x _ { h } ( n h )$ is of size $\mathcal { O } ( t ^ { 2 } h ^ { N } )$ and actually satisfies the finerestimate(5.12).This completes the proof of Theorem5.2. □

# XII1.5.3Expansion of the Velocity Approximation

Asimilar expansion holds also for the velocities.We show this for the scheme(2.11 or its equivalent one-step formulation (2.8)with (2.9).

Theorem5.3.Under theassumptionsof Theorem5.2,thevelocityapproximation ${ \dot { x } } _ { n }$ givenby(2.11） hasanexpansion

$$
\dot { x } _ { n } = v _ { h } ( t ) + \sum _ { 0 < | k | < N } e ^ { i k \omega t } w _ { h } ^ { k } ( t ) + \mathcal { O } ( t ^ { 2 } h ^ { N - 1 } )
$$

uniformly for $0 \leq t = n h \leq T$ wherethereal-valuedfunctions $v _ { h } = ( v _ { h , 0 } , v _ { h , 1 } )$ andthecomplex-valuedfunctions $w _ { h } ^ { k } = ( w _ { h , 0 } ^ { k } , w _ { h , 1 } ^ { k } )$ togetherwiththeirderivatives up toarbitrary order satisfy

$$
\begin{array} { r l r } & { v _ { h , 0 } = \dot { y } _ { h , 0 } + \mathcal { O } ( h ^ { 2 } ) , } & { w _ { h , 0 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 1 } ) , } & { w _ { h , 0 } ^ { k } = \mathcal { O } ( \omega ^ { - k } ) } \\ & { w _ { h , 1 } ^ { 1 } = i \omega z _ { h , 1 } ^ { 1 } + \mathcal { O } ( \omega ^ { - 1 } ) , } & { v _ { h , 1 } = \mathcal { O } ( \omega ^ { - 1 } ) , } & { w _ { h , 1 } ^ { k } = \mathcal { O } ( \omega ^ { - k } ) } \end{array}
$$

for $k = 2 , \ldots , N - 1$ Moreover, $w _ { h } ^ { - k } = w _ { h } ^ { k } .$ The constants symbolized by the $\mathcal { O }$ -notationareindependentof $\boldsymbol { \omega }$ and $h$ with $( 5 . I O )$ butdepend on $E$ , $N$ c,and $T .$

Proof.Let $u _ { h } ( t )$ be defined by the continuous analogue of(2.11),

$$
2 h \operatorname { s i n c } ( h \Omega ) u _ { h } ( t ) = x _ { h } ( t + h ) - x _ { h } ( t - h ) .
$$

Theorem5.2 thenyields that

$$
\dot { x } _ { n } = u _ { h } ( t ) + \mathcal { O } ( t ^ { 2 } h ^ { N - 1 } )
$$

for $t = n h$ onbounded time intervals.Here we used that the remainder term in the lowercomponent of(5.12） isof the form $\mathcal { O } ( \psi ( h \omega ) ( \phi ( h \omega ) + h ) t ^ { 2 } h ^ { N } )$ ,so that its

quotient with $2 h \operatorname { s i n c } ( h \omega )$ becomes $\mathcal { O } ( t ^ { 2 } h ^ { N - 1 } )$ by the thirdof theconditions (4.1) andby(5.10).The function $u _ { h } ( t )$ can be written as

$$
u _ { h } ( t ) = v _ { h } ( t ) + \sum _ { 0 < | k | < N } e ^ { i k \omega t } w _ { h } ^ { k } ( t ) .
$$

We insert the relation (5.14） into $- i \sin ( i h D ) ; x _ { h } ( t ) = h \operatorname { s i n c } ( h \Omega ) u _ { h } ( t )$ whichis equivalent to(5.24),and compare thecoefficients of $e ^ { \imath k \omega t }$ to obtain

$$
\begin{array} { r l } & { \mathrm { s i n c } ( i h D ) \dot { y } _ { h , 0 } = v _ { h , 0 } } \\ & { \mathrm { s i n c } ( i h D ) \dot { y } _ { h , 1 } = \mathrm { s i n c } ( h \omega ) v _ { h , 1 } } \\ & { ( i h ) ^ { - 1 } \mathrm { s i n } ( i h D - k h \omega ) z _ { h , 0 } ^ { k } = w _ { h , 0 } ^ { k } } \\ & { ( i h ) ^ { - 1 } \mathrm { s i n } ( i h D - k h \omega ) z _ { h , 1 } ^ { k } = \mathrm { s i n c } ( h \omega ) w _ { h , 1 } ^ { k } } \end{array}
$$

for $k = 1 , \ldots , N - 1 .$ In particular,for $w _ { h , 1 } ^ { 1 }$ we get

$$
w _ { h , 1 } ^ { 1 } = i \omega \cos ( i h D ) z _ { h , 1 } ^ { 1 } - i \omega \frac { \cos ( h \omega ) } { \sin ( h \omega ) } \sin ( i h D ) z _ { h , 1 } ^ { 1 } .
$$

With the above equations,the estimates now follow with the bounds (5.21） of the coefficient functions and their derivatives,using again (4.1). □

# XIII.6 Almost-Invariants of the Modulated Fourier Expansions

Thesystem for the coefcients of the modulated Fourier expansion of the exact solution isshownto have two formal invariants,which are related tothe total and the oscillatory energy.Inparticular,this explains the near-conservation of the oscillatory energy oververylong times.Analogous almost-invariantsare shown toexist also for themodulated Fourier expansion of the numerical solution.This forms thebasis for results on the long-time energyconservation of numerical methods,which will be given in Sections XIII.7 and XII1.8.

# XIII.6.1 The Hamiltonianof the Modulated Fourier Expansion

Theequation(2.1） isa Hamiltoniansystemwith theHamiltonian

$$
\begin{array} { r } { H ( x , \dot { x } ) = \frac { 1 } { 2 } \dot { x } ^ { T } \dot { x } + \frac { 1 } { 2 } x ^ { T } \Omega ^ { 2 } x + U ( x ) . } \end{array}
$$

In the modulated Fourier expansion of the solution $x ( t )$ of(2.1）,denote $y ^ { 0 } ( t ) =$ $y ( t )$ and $y ^ { k } ( t ) = e ^ { i k \omega t } z ^ { k } ( t )$ $0 < | \boldsymbol k | < N$ ,andlet

$$
\begin{array} { r } { \mathbf { y } = ( y ^ { - N + 1 } , \ldots , y ^ { - 1 } , y ^ { 0 } , y ^ { 1 } , \ldots , y ^ { N - 1 } ) . } \end{array}
$$

By(5.5)-(5.7) these functions satisfy

$$
{ \ddot { y } } ^ { k } + \Omega ^ { 2 } y ^ { k } = - \sum _ { s ( \alpha ) = k } { \frac { 1 } { m ! } } U ^ { ( m + 1 ) } ( y ^ { 0 } ) { \bf y } ^ { \alpha } + O ( \omega ^ { - N } ) .
$$

Here,the sum is over all $m \geq 0$ and all multi-indices $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ with integers $\alpha _ { j }$ $0 < | \alpha _ { j } | < N )$ whichhavea givensum $\begin{array} { r } { s ( \alpha ) = \sum _ { j = 1 } ^ { m } \alpha _ { j } } \end{array}$ ∑j=1Qj,and we write $\mathbf { y } ^ { \alpha } = ( y ^ { \alpha _ { 1 } } , \ldots , y ^ { \alpha _ { m } } ) .$ Wedefine

$$
\mathcal { U } ( { \bf y } ) = U ( y ^ { 0 } ) + \sum _ { s ( \alpha ) = 0 } \frac { 1 } { m ! } U ^ { ( m ) } ( y ^ { 0 } ) { \bf y } ^ { \alpha } .
$$

From the above it follows that $\mathbf { y } ( t )$ satisfies the system

$$
\ddot { y } ^ { k } + \varOmega ^ { 2 } y ^ { k } = - \nabla _ { y ^ { - k } } \mathcal { U } ( \mathbf { y } ) + \mathcal { O } ( \omega ^ { - N } )
$$

which, neglectingthe $\mathcal { O } ( \omega ^ { - N } )$ term,is theHamiltoniansystem (cf.Exercise 6)

$$
{ \dot { y } } ^ { k } = { \frac { \partial { \mathcal { H } } } { \partial { \dot { y } } ^ { - k } } } ( \mathbf { y } , { \dot { \mathbf { y } } } ) , \qquad { \ddot { y } } ^ { k } \equiv - { \frac { \partial { \mathcal { H } } } { \partial y ^ { - k } } } ( \mathbf { y } , { \dot { \mathbf { y } } } )
$$

with

$$
\mathcal { H } ( \mathbf { y } , \dot { \mathbf { y } } ) = \frac { 1 } { 2 } \sum _ { | k | < N } \left( ( \dot { y } ^ { - k } ) ^ { T } \dot { y } ^ { k } + ( y ^ { - k } ) ^ { T } \Omega ^ { 2 } y ^ { k } \right) + \mathcal { U } ( \mathbf { y } ) ,
$$

Theorem6.1.Under theassumptions ofTheorem5.1,theHamiltonian ofthemodulatedFourierexpansionsatisfies

$$
\begin{array} { r l } & { \mathcal { H } ( { \mathbf { y } } ( t ) , \dot { \mathbf { y } } ( t ) ) ~ = ~ \mathcal { H } ( { \mathbf { y } } ( 0 ) , \dot { \mathbf { y } } ( 0 ) ) + \mathcal { O } ( \omega ^ { - N } ) } \\ & { \mathcal { H } ( { \mathbf { y } } ( t ) , \dot { \mathbf { y } } ( t ) ) ~ = ~ H ( x ( t ) , \dot { x } ( t ) ) + \mathcal { O } ( \omega ^ { - 1 } ) . } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ areindependent of $\omega$ and $t$ with $0 \leq t \leq T$ but dependon $E$ ， $N$ and $T$ .

Proof.Multiplying(6.4)with $( \dot { y } ^ { - k } ) ^ { T }$ and summing up gives

$$
\sum _ { | k | < N } ( \dot { y } ^ { - k } ) ^ { T } ( \ddot { y } ^ { k } + \varOmega ^ { 2 } y ^ { k } ) = - \frac { d } { d t } \mathcal { U } ( { \bf y } ) + \mathcal { O } ( \omega ^ { - N } ) .
$$

Integrating from 0 to $t$ and using $y ^ { - k } = { \overline { { y ^ { k } } } }$ then yields (6.7).

Bythebounds of Theorem5.1,we have for $0 \leq t \leq I$

$$
\begin{array} { r } { \mathcal { H } ( \mathbf { y } , \dot { \mathbf { y } } ) = \frac { 1 } { 2 } \| \dot { y } _ { 0 } ^ { 0 } \| ^ { 2 } + \| \dot { y } _ { 1 } ^ { 1 } \| ^ { 2 } + \omega ^ { 2 } \| y _ { 1 } ^ { 1 } \| ^ { 2 } + U ( y ^ { 0 } ) + \mathcal { O } ( \omega ^ { - 1 } ) . } \end{array}
$$

Onthe other hand,we have from(6.1)and (5.1)

$$
\begin{array} { r } { H ( x , \dot { x } ) = \frac { 1 } { 2 } \| \dot { y } _ { 0 } ^ { 0 } \| ^ { 2 } + \frac { 1 } { 2 } \| \dot { y } _ { 1 } ^ { 1 } + \dot { y } _ { 1 } ^ { - 1 } \| ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } \| y _ { 1 } ^ { 1 } + y _ { 1 } ^ { - 1 } \| ^ { 2 } + U ( y ^ { 0 } ) + \mathcal { O } ( \omega ^ { - 1 } ) . } \end{array}
$$

Using $y _ { 1 } ^ { 1 } = e ^ { i \omega t } z _ { 1 } ^ { 1 }$ and $\dot { y } _ { 1 } ^ { 1 } = e ^ { \ i \omega t } ( \dot { z } _ { 1 } ^ { 1 } + i \omega z _ { 1 } ^ { 1 } )$ togetherwith $y _ { 1 } ^ { - 1 } = y _ { 1 } ^ { 1 }$ ,it follows from $\dot { z } _ { 1 } ^ { 1 } = \mathcal { O } ( \omega ^ { - 1 } )$ that $\dot { y } _ { 1 } ^ { 1 } + \dot { y } _ { 1 } ^ { - 1 } = i \omega ( y _ { 1 } ^ { 1 } - y _ { 1 } ^ { - 1 } ) + \mathcal { O } ( \omega ^ { - 1 } )$ and $\lVert \dot { y } _ { 1 } ^ { \perp } \rVert = \omega \lVert y _ { 1 } ^ { 1 } \rVert +$ $\mathcal { O } ( \omega ^ { - 1 } )$ Insertedinto(6.10)and(6.11),this yields (6.8). $\sqcup$

# XIII.6.2 A Formal Invariant Close to theOscillatory Energy

Inaddition to the Hamiltonian ${ \mathcal { H } } ( { \bf y } , { \dot { \bf y } } )$ ,the system for the coefficients of the modulated Fourier expansion has another formally conserved quantity.This almostinvariant depends only on the oscillatingpart and is given by

$$
{ \mathcal { T } } ( \mathbf { y } , { \dot { \mathbf { y } } } ) = - i \omega \sum _ { 0 < | k | < N } k ( y ^ { - k } ) ^ { T } { \dot { y } } ^ { k } .
$$

This turns out to be close to the energy of the harmonic oscillator,

$$
\begin{array} { r } { I ( x , \dot { x } ) = \frac { 1 } { 2 } \| \dot { x } _ { 1 } \| ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } \| x _ { 1 } \| ^ { 2 } . } \end{array}
$$

Theorem6.2.Under the assumptions ofTheorem5.1,

$$
\begin{array} { r l } { \displaystyle \mathcal { T } ( \mathbf { y } ( t ) , \dot { \mathbf { y } } ( t ) ) ~ = ~ \mathcal { T } ( \mathbf { y } ( 0 ) , \dot { \mathbf { y } } ( 0 ) ) + \mathcal { O } ( \omega ^ { - N } ) } & { } \\ { \displaystyle \mathcal { T } ( \mathbf { y } ( t ) , \dot { \mathbf { y } } ( t ) ) ~ = ~ \mathcal { I } ( x ( t ) , \dot { x } ( t ) ) + \mathcal { O } ( \omega ^ { - 1 } ) . } & { } \end{array}
$$

Theconstants symbolized by $\mathcal { O }$ areindependent of $\boldsymbol { \omega }$ and $t$ with $0 \leq t \leq T$ but dependon $E$ , $N$ and $\boldsymbol { \mathcal { T } }$

Proof.For thevector

$$
\mathbf { y } ( \lambda ) = \left( e ^ { i ( - N + 1 ) \lambda } y ^ { - N + 1 } , \ldots , e ^ { - i \lambda } y ^ { - 1 } , y ^ { 0 } , e ^ { i \lambda } y ^ { 1 } , \ldots , e ^ { i ( N - 1 ) \lambda } y ^ { N - 1 } \right)
$$

thedefinition (6.3）of $\boldsymbol { u }$ shows that $\mathcal { U } ( \mathbf { y } ( \boldsymbol { \lambda } ) )$ does not depend on $\lambda$ Itsderivative with respect to $\lambda$ thusyields

$$
0 = \frac { d } { d \lambda } \mathcal { U } ( { \bf y } ( \lambda ) ) = \sum _ { 0 < | k | < N } i k e ^ { i k \lambda } ( y ^ { k } ) ^ { T } \nabla _ { k } \mathcal { U } ( { \bf y } ( \lambda ) ) ,
$$

and putting $\lambda = 0$ we obtain

$$
\sum _ { 0 < | k | < N } i k ( y ^ { k } ) ^ { T } \nabla _ { k } \mathcal { U } ( \mathbf { y } ) = 0
$$

forall vectors $\begin{array} { r } { \mathbf { y } = ( y ^ { - N + 1 } , \ldots , y ^ { - 1 } , y ^ { 0 } , y ^ { 1 } , \ldots , y ^ { N - 1 } ) . } \end{array}$

Theproof ofTheorem6.2isnowvery similar tothatof Theorem6.1.Wemultiply therelation (6.4）with $- i \omega k ( y ^ { - k } ) ^ { T }$ instead of $( \dot { y } ^ { - k } ) ^ { T }$ Summing up yields, with the use of (6.16),

$$
- i \omega \sum _ { 0 < | k | < N } k ( y ^ { - k } ) ^ { T } \bigl ( \ddot { y } ^ { k } + \varOmega ^ { 2 } y ^ { k } \bigr ) = \mathcal { O } ( \omega ^ { - N } ) .
$$

The time derivative of $\mathcal { T } ( \mathbf { y } , \dot { \mathbf { y } } )$ of (6.12) equals

$$
\frac { d } { d t } \mathcal { Z } ( \mathbf { y } , \dot { \mathbf { y } } ) = - i \omega \sum _ { 0 < | k | < N } k \Big ( ( y ^ { - k } ) ^ { T } \ddot { y } ^ { k } + ( \dot { y } ^ { - k } ) ^ { T } \dot { y } ^ { k } \Big ) .
$$

In the sums $\begin{array} { r } { \sum _ { k } k ( y ^ { - k } ) ^ { T } \Omega ^ { 2 } y ^ { k } } \end{array}$ and $\begin{array} { r } { \sum _ { k } k ( \dot { y } ^ { - k } ) ^ { T } \dot { y } ^ { k } } \end{array}$ ,the terms with $k$ and $- k$ cancel.Hence,(6.17)and(6.18) togetheryield

$$
\frac { d } { d t } \bar { \cal T } ( { \bf y } , \dot { \bf y } ) = { \cal O } ( \omega ^ { - N } ) ,
$$

which implies (6.14).

With $\begin{array} { r } { \dot { y } ^ { k } = e ^ { i k \omega t } ( \dot { z } ^ { k } + i k \omega z ^ { k } ) = i k \omega y ^ { k } + \mathcal { O } ( \omega ^ { - 1 } ) , } \end{array}$ it follows fromthebounds of Theorem 5.1 that

$$
{ \mathcal { T } } ( \mathbf { y } , { \dot { \mathbf { y } } } ) = 2 \omega ^ { 2 } \| y _ { 1 } ^ { 1 } \| ^ { 2 } + { \mathcal { O } } ( \omega ^ { - 1 } ) .
$$

Onthe other hand,using the arguments of the proof of Theorem6.1,we have

$$
\begin{array} { r } { \dot { x } ) = \frac { 1 } { 2 } \| \dot { y } _ { 1 } ^ { 1 } + \dot { y } _ { 1 } ^ { - 1 } \| ^ { 2 } + \frac { 1 } { 2 } \omega ^ { 2 } \| y _ { 1 } ^ { 1 } + y _ { 1 } ^ { - 1 } \| ^ { 2 } + \mathcal { O } ( \omega ^ { - 1 } ) = 2 \omega ^ { 2 } \| y _ { 1 } ^ { 1 } \| ^ { 2 } + \mathcal { O } ( \omega ^ { - 1 } ) . } \end{array}
$$

This proves the second statement of the theorem.

Theorem6.2 implies that theoscilltory energyisnearlyconserved over long times:

Theorem6.3.If the solution $x ( t )$ of(2.1）stays in a compact set for $0 \le t \le \omega ^ { N }$ ， then

$$
I ( x ( t ) , \dot { x } ( t ) ) = I ( x ( 0 ) , \dot { x } ( 0 ) ) + \mathcal { O } ( \omega ^ { - 1 } ) + \mathcal { O } ( t \omega ^ { - N } ) .
$$

The constants symbolized by $\mathcal { O }$ areindependent of $\omega$ and $t$ with $0 \le t \le \omega ^ { N }$ but dependon $E$ and $N$

ProofWithafixed $T > 0$ ,let $\mathbf { y } _ { j }$ denote the vector of themodulated Fourier expansion terms that correspond to starting values $( x ( j T ) , \dot { x } ( j T ) )$ .For $t = ( n + \theta ) T$ with $0 \leq \theta < 1$ ,we have by(6.15）

$$
\begin{array} { r l } {  { I ( x ( t ) , \dot { x } ( t ) ) - I ( x ( 0 ) , \dot { x } ( 0 ) ) } } \\ & { = \mathcal { T } ( \mathbf { y } _ { n } ( \theta T ) , \dot { \mathbf { y } } _ { n } ( \theta T ) ) \neq \mathcal { O } ( \omega ^ { - 1 } ) - \mathcal { Z } ( \mathbf { y } _ { 0 } ( 0 ) , \dot { \mathbf { y } } _ { 0 } ( 0 ) ) + \mathcal { O } ( \omega ^ { - 1 } ) } \\ & { = \mathcal { Z } ( \mathbf { y } _ { n } ( \theta T ) , \dot { \mathbf { y } } _ { n } ( \theta T ) ) = \mathbb { Z } ( \mathbf { y } _ { n } ( 0 ) , \dot { \mathbf { y } } _ { n } ( 0 ) ) + } \\ & { \quad \displaystyle \sum _ { j = 0 } ^ { n - 1 } \Big ( \mathcal { Z } ( \mathbf { y } _ { j + 1 } ( 0 ) , \dot { \mathbf { y } } _ { j + 1 } ( 0 ) ) - \mathcal { Z } ( \mathbf { y } _ { j } ( 0 ) , \dot { \mathbf { y } } _ { j } ( 0 ) ) \Big ) + \mathcal { O } ( \omega ^ { - 1 } ) . } \end{array}
$$

Wenote

$$
\begin{array} { r } { \mathbb { Z } ( \mathbf { y } _ { j + 1 } ( 0 ) , \dot { \mathbf { y } } _ { j + 1 } ( 0 ) ) = \mathbb { Z } ( \mathbf { y } _ { j } ( 0 ) , \dot { \mathbf { y } } _ { j } ( 0 ) ) = \mathbb { O } ( \omega ^ { - N } ) , } \end{array}
$$

because,by the quasi-uniqueness of the coefficient functions as stated by Theorem5.1,we have ${ \bf y } _ { j + 1 } ( 0 ) = { \bf y } _ { j } ( T ) + \mathcal { O } ( \omega ^ { - N } )$ and $\dot { \bf y } _ { j + 1 } ( 0 ) = \dot { \bf y } _ { j } ( T ) + \mathcal { O } ( \omega ^ { - N } )$ , andwe have the bound (6.14）of Theorem 6.2.The sameargumentapplies to $\begin{array} { r } { \mathcal { T } ( \mathbf { y } _ { n } ( \boldsymbol { \theta T } ) , \dot { \mathbf { y } } _ { n } ( \boldsymbol { \theta T } ) ) - \mathcal { T } ( \mathbf { y } _ { n } ( 0 ) , \dot { \mathbf { y } } _ { n } ( 0 ) ) . } \end{array}$ This yields the result. □

Inadifferent approach,Benettin,Galgani&Giorgilli（1987）usea sequence ofcoordinate transformations from Hamiltonian perturbation theory to show that $I$ hasonly small deviations over time intervalswhich grow exponentiallywith $\omega$ ,in thecase of an analytic potential $U$ Bycarefully tracing the dependence on $N$ of the constants in the $\mathcal { O } ( \omega ^ { - N } )$ -terms,near-conservationof $I$ over exponentially long timeintervalscan be shown alsowithin the present framework ofmodulated Fourier expansions;see Cohen,Hairer&Lubich(2003).

# XIII.6.3 Almost-Invariants of the Numerical Method

Weshow that the coeficients of the modulated Fourier expansion of the numerical solution have almost-invariants thatareobtained similarly to theabove.We denote

$$
\begin{array} { r } { \mathbf { y } _ { h } = ( y _ { h } ^ { - N + 1 } , \dots , y _ { h } ^ { - 1 } , y _ { h } ^ { 0 } , y _ { h } ^ { 1 } , \dots , y _ { h } ^ { N - 1 } ) } \\ { \mathbf { z } _ { h } = ( z _ { h } ^ { - N + 1 } , \dots , z _ { h } ^ { - 1 } , z _ { h } ^ { 0 } , z _ { h } ^ { 1 } , \dots , z _ { h } ^ { N - 1 } ) } \end{array}
$$

with $y _ { h } ^ { \mathrm { v } } ( t ) = z _ { h } ^ { \mathrm { v } } ( t ) = y _ { h } ( t )$ and $y _ { h } ^ { k } ( t ) = e ^ { \ i k \omega t } z _ { h } ^ { k } ( t )$ ,where $y _ { h }$ and $z _ { h } ^ { k }$ are the coefficients of the modulated Fourier expansion of Theorem 5.2.Similar to(6.3)we consider the function

$$
\mathcal { U } _ { h } ( \mathbf { y } _ { h } ) = U ( \varPhi y _ { h } ^ { 0 } ) + \sum _ { s ( \alpha ) = 0 } \frac { 1 } { m ! } U ^ { ( m ) } ( \varPhi y _ { h } ^ { 0 } ) ( \varPhi \mathbf { y } _ { h } ) ^ { \alpha } ,
$$

where thesumisagaintakenoverall $m \geq 1$ and allmulti-indices ${ \alpha = ( \alpha _ { 1 } , \dots , \alpha _ { m } ) }$ with $0 < | \alpha _ { j } | < N$ forwhich $\begin{array} { r } { s ( \alpha ) = \sum _ { j } \alpha _ { j } = 0 . } \end{array}$ It then follows from (5.22）， multiplied with $h ^ { - 2 } \varPsi ^ { - 1 } \varPhi$ ,that the functions $y _ { h _ { 1 } } ^ { k } ( t )$ satisfy

$$
\varPsi ^ { - 1 } \varPhi h ^ { - 2 } \varDelta ( h D ) y _ { h } ^ { k } = - \nabla _ { - k } \mathcal { U } _ { h } ( \mathbf { y } _ { h } ) + \mathcal { O } ( h ^ { N } ) ,
$$

where $\mathcal { L } ( h D )$ of(5.16） denotes again the difference operator of the numerical method.The similarityof theserelations to(6.4）allowsusto obtain almostconserved quantities that are analogues of $\mathcal { H }$ and $\mathcal { L }$ above.

TheFirst Almost-Invariant.We multiply(6.20) by $( { \dot { y } } _ { h } ^ { - k } ) ^ { T }$ and asin (6.9）we obtain

$$
\sum _ { | k | < N } ( \dot { y } _ { h } ^ { - k } ) ^ { T } \bar { \psi } ^ { - 1 } \varPhi h ^ { - 2 } \varSigma ( h D ) y _ { h } ^ { k } + \frac { d } { d t } \mathcal { U } _ { h } ( \mathbf { y } _ { h } ) = \mathcal { O } ( h ^ { N } ) ,
$$

Since we know bounds of the coefficient functions $z _ { h } ^ { k }$ andof their derivatives from Theorem5.2ewihtohiies $z _ { h } ^ { k }$ andwegettheequivalentrlation

$$
\sum _ { | k | < N } \big ( \dot { z } _ { h } ^ { - k } - i k \omega z _ { h } ^ { - k } \big ) ^ { T } \bar { \psi } ^ { - 1 } \bar { \phi } h ^ { - 2 } \mathcal { L } ( h \bar { D } + i k \omega \bar { h } ) z _ { h } ^ { k } + \frac { d } { d t } \mathcal { U } _ { h } ( \mathbf { z } _ { h } ) = \mathcal { O } ( h ^ { N } ) .
$$

Weshall show that the left-hand sideisthe total derivative of an expression that depends onlyon $z _ { h } ^ { k }$ and derivatives thereof.Consider first the term for $k = 0 .$ The symmetry of thenumerical method entersat thisvery pointin the way that the expression ${ \cal L } ( h D ) y = h ^ { 2 } \ddot { y } + c _ { 4 } h ^ { 4 } y ^ { ( 4 ) } + c _ { 6 } h ^ { 6 } y ^ { ( 6 ) } + \dots$ contains only terms with derivatives ofan even order.Multiplied with $\dot { y } ^ { \mathcal { I } }$ ,even-orderderivatives of $y$ givea total derivative:

$$
\dot { y } ^ { T } y ^ { ( 2 l ) } = \frac { d } { d t } \Bigl ( \dot { y } ^ { T } y ^ { ( 2 l - 1 ) } - \ddot { y } ^ { T } y ^ { ( 2 l - 2 ) } + \ldots \mp ( y ^ { ( l - 1 ) } ) ^ { T } y ^ { ( l + 1 ) } \pm \frac { 1 } { 2 } ( y ^ { ( l ) } ) ^ { T } y ^ { ( l + 1 ) } \Bigr ) ,
$$

Thanks tothe symmetry of thedifference operator $\mathcal { L } ( h D )$ only expressions of this typeappear in the term for $k = 0$ in(6.21），with $z _ { h } ^ { 0 }$ in the role of $_ y$ Similarly,we getfor $z = z _ { h } ^ { k }$ and $\overline { { z } } = z _ { h } ^ { - k }$ with $0 < | \boldsymbol { k } | < N$

$$
\begin{array} { l } { { \displaystyle \mathrm { R e } ^ { \frac { \dot { z } } { { \tilde { z } } } ^ { T } } z ^ { ( 2 l ) } = \mathrm { R e } \frac { d } { d t } \Big ( \dot { \tilde { z } } ^ { T } z ^ { ( 2 l - 1 ) } - \dots \mp ( \tilde { z } ^ { ( l - 1 ) } ) ^ { T } z ^ { ( l + 1 ) } \pm \frac { 1 } { 2 } ( \tilde { z } ^ { ( l ) } ) ^ { T } z ^ { ( l ) } \Big ) } } \\ { { \displaystyle \mathrm { R e } \overline { { { z } } } ^ { T } z ^ { ( 2 l + 1 ) } = \mathrm { R e } \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } z ^ { ( 2 l ) } - \dots \pm ( \overline { { { z } } } ^ { ( l - 1 ) } ) ^ { T } z ^ { ( l + 1 ) } \mp \frac { 1 } { 2 } ( \overline { { { z } } } ^ { ( l ) } ) ^ { T } z ^ { ( l ) } \Big ) } } \\ { { \displaystyle \mathrm { I m } \dot { \tilde { z } } ^ { T } z ^ { ( 2 l + 1 ) } = \mathrm { I m } \frac { d } { d t } \Big ( \dot { \tilde { z } } ^ { T } z ^ { ( 2 l ) } - \frac { \ddot { z } ^ { T } } { z } z ^ { ( 2 l - 1 ) } + \ j \cdot \mp ( \overline { { { z } } } ^ { ( l ) } ) ^ { T } z ^ { ( l + 1 ) } \Big ) } } \\ { { \displaystyle \mathrm { I m } \overline { { { z } } } ^ { T } z ^ { ( 2 l + 2 ) } = \mathrm { I m } \frac { d } { d t } \Big ( \overline { { { z } } } ^ { T } \dot { z } ^ { ( 2 l + 1 ) } - \dot { \tilde { z } } ^ { T } z ^ { ( 2 l ) } + \dots \pm ( \overline { { { z } } } ^ { ( l ) } ) ^ { T } z ^ { ( l + 1 ) } \Big ) \ . } } \end{array}
$$

Using the formulas(5.19)for $C ( h D + i k h \omega )$ ,it is seen that the term for $k$ in (6.21) has an asymptotic $h$ -expansion with expressions of the above type as coefficients. The left-hand side of (6.21） can therefore be written as the time derivative of a function ${ \mathcal { H } } _ { h } [ { \pmb { x } } _ { h } ] ( t )$ which depends on the values at $t$ of the coefficient function vector $\mathbb { z } _ { h }$ and its first $N$ timederivatives.The relation(6.21） thus becomes

$$
\frac { d } { d t } \widehat { \mathcal { H } } _ { h } [ \mathbf { z } _ { h } ] ( t ) = { \mathcal { O } } ( h ^ { N } ) .
$$

Together with the estimates of Theorem 5.2,this construction of $\widehat { \mathcal { H } } _ { h }$ yields the following result.

（2N+1， $( z _ { h } ^ { - N + 1 } , \ldots , z _ { h } ^ { - 1 } , y _ { h } , z _ { h } ^ { 1 } , \ldots , z _ { h } ^ { N - 1 } )$ ${ \mathbf z } _ { h } =$ merical solution satisfy

$$
\widehat { \mathcal { H } } _ { h } [ \mathbf { z } _ { h } ] ( t ) = \widehat { \mathcal { H } } _ { h } [ \mathbf { z } _ { h } ] ( 0 ) + \mathcal { O } ( t h ^ { N } )
$$

for $0 \leq t \leq T .$ Moreover,

$$
\begin{array} { r } { \widehat { \mathcal { H } } _ { h } [ \mathbf { z } _ { h } ] ( t ) = \frac { 1 } { 2 } \| \dot { y } _ { h , 0 } ( t ) \| ^ { 2 } + \sigma ( h \omega ) 2 \omega ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } + U ( \varPhi y _ { h } ( t ) ) + \mathcal { O } ( h ^ { 2 } ) , } \end{array}
$$

where $\sigma ( h \omega ) = \operatorname { s i n c } ( h \omega ) \phi ( h \omega ) / \psi ( h \omega )$

The Second Almost-Invariant.By the same calculation as in the proof of Theo-$\mathrm { r e m } 6 . 2$ we obtain for ${ { U } _ { h } } ( \mathbf { y } _ { h } ( t ) )$ of(6.19)

$$
0 = \sum _ { 0 < | \boldsymbol { k } | < N } i \boldsymbol { k } \omega ( y _ { h } ^ { \boldsymbol { k } } ) ^ { T } \nabla _ { \boldsymbol { k } } \mathcal { U } _ { h } ( \mathbf { y } _ { h } ) .
$$

It then follows from(6.20）that

$$
- i \omega \sum _ { 0 < | k | < N } k ( y _ { h } ^ { - k } ) ^ { T } \varPsi ^ { - 1 } \varPhi h ^ { - 2 } \var L ( h D ) y _ { h } ^ { k } = \mathcal { O } ( h ^ { N } ) .
$$

Written in the $z$ variables,this becomes

$$
- i \omega \sum _ { 0 < | k | < N } k ( z _ { h } ^ { - k } ) ^ { T } \varPsi ^ { - 1 } \varPhi h ^ { - 2 } \varSigma ( h D + i k \omega h ) z _ { h } ^ { k } = { \cal O } ( h ^ { N } ) .
$$

Asin(6.21),the left-hand expression can be written as the time derivative of a function ${ \hat { \cal T } } _ { h } [ { \bf z } _ { h } ] ( t )$ which depends on the values at $t$ ofthe function ${ \pmb x } _ { h }$ and its first $N$ derivatives:

$$
\frac { d } { d t } \widehat { T } _ { h } [ { \bf z } _ { h } ] ( t ) = { \cal O } ( h ^ { N } ) .
$$

Together with the estimates of Theorem 5.2 thisyields the following result.

Lemma6.5.Under theassumptionsofTheorem5.2,thecoeffcient functions $\mathbf { z } _ { h }$ of themodulated Fourier expansion of the numerical solution satisfy

$$
\widehat { \mathcal { T } } _ { h } [ \mathbf { z } _ { h } ] ( t ) = \widehat { \mathcal { T } } _ { h } [ \mathbf { z } _ { h } ] ( 0 ) + \mathcal { O } ( t h ^ { N } )
$$

for $0 \leq t \leq T .$ Moreover,

$$
\widehat { T } _ { h } [ \mathbf { z } _ { h } ] ( t ) = \sigma ( h \omega ) 2 \omega ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } + \mathcal { O } ( h ^ { 2 } ) ,
$$

where again $\sigma ( h \omega ) = \operatorname { s i n c } ( h \omega ) \phi ( h \omega ) / \psi ( h \omega ) .$

Symplectic methods have $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi )$ and hence $\sigma ( h \omega ) = 1$ Tobe ableto also treat methodswhere $\sigma ( h \omega )$ can be small,we need to sharpen the estimates ofLemma 6.5.Close scrutiny of the equations(5.2O) that determine thecoefficient functions of the modulated Fourier expansion,shows that the $\mathcal { O } ( h ^ { 2 } )$ term in（6.26）contains a factor $\phi ( h \omega ) ^ { 2 }$ ,andthat the $\mathcal { O } ( t h ^ { N } )$ term in（6.25）can be put in theform $\mathcal { O } ( t \phi ( h \omega ) ^ { N } h ^ { N } ) + \mathcal { O } ( t h ^ { N + m } )$ withanarbitrary integer $m \geq 0$ ;cf.(5.12). Assume now that

$\phi$ isanalytic with no real zeros other than integral multiples ofπ.

This condition ensures that $| \phi ( h \omega ) | ^ { 2 } \geq c h ^ { m }$ forsome $1 / \ell$ if $h \omega$ satisfies (5.10). Underthe conditionsof Theorem5.2,inparticular,(4.1） and(5.10),theimproved bounds of theremainder terms yield the following estimates for ${ \mathcal T } _ { h } = \widehat { { \cal T } } _ { h } / \sigma ( h \omega )$

$$
\begin{array} { r l } & { \mathcal { T } _ { h } [ { \mathbf { z } } _ { h } ] ( t ) = \mathcal { T } _ { h } [ { \mathbf { z } } _ { h } ] ( 0 ) + \mathcal { O } ( t h ^ { N } ) } \\ & { \mathcal { T } _ { h } [ { \mathbf { z } } _ { h } ] ( t ) = 2 \omega ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } + \mathcal { O } ( h ^ { 2 } ) . } \end{array}
$$

Relationshipwith the Total and theOscillatory Energy.Thealmost-invariants

$$
\mathcal { T } _ { h } = \frac { 1 } { \sigma ( h \omega ) } \widehat { \mathcal { T } } _ { h } , \quad \mathcal { H } _ { h } = \widehat { \mathcal { H } } _ { h } - \Big ( 1 - \frac { 1 } { \sigma ( h \omega ) } \Big ) \widehat { \mathcal { T } } _ { h }
$$

of the coefficient functions of the modulated Fourier expansion are then close to the totalenergy $H$ and the oscillatory energy $I$ along the numerical solution $( x _ { n } , { \dot { x } } _ { n } )$ :

Theorem6.6.Under the conditionsofTheorems5.2andcondition (6.27),

$$
\begin{array} { r l } & { \mathcal { H } _ { h } [ { \bf z } _ { h } ] ( t ) = \mathcal { H } _ { h } [ { \bf z } _ { h } ] ( 0 ) + \mathcal { O } ( t h ^ { N } ) , \quad \mathcal { T } _ { h } [ { \bf z } _ { h } ] ( t ) = \mathcal { T } _ { h } [ { \bf z } _ { h } ] ( 0 ) + \mathcal { O } ( t h ^ { N } ) } \\ & { \mathcal { H } _ { h } [ { \bf z } _ { h } ] ( t ) = H ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) , \qquad \mathcal { T } _ { h } [ { \bf z } _ { h } ] ( t ) = { \cal I } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) } \end{array}
$$

holdsfor $0 \leq t = n h \leq T .$ Theconstants symbolized by $\mathcal { O }$ dependon $E$ , $N$ and $T$

Proof.The upper two relations follow directly from(6.22)and(6.28).Theorems 5.2 and5.3show

$$
\begin{array} { r l r } { \omega x _ { n , 1 } } & { = } & { \omega \big ( e ^ { i \omega t } z _ { h , 1 } ^ { 1 } ( t ) + e ^ { - i \omega t } z _ { h , 1 } ^ { - 1 } ( t ) \big ) + \mathcal { O } ( h ) } \\ { \dot { x } _ { n , 1 } } & { = } & { i \omega \big ( e ^ { i \omega t } z _ { h , 1 } ^ { 1 } ( t ) - e ^ { - i \omega t } z _ { h , 1 } ^ { - 1 } ( t ) \big ) + \mathcal { O } ( h ) . } \end{array}
$$

With the identity $\| v + \overline { { v } } \| ^ { 2 } + \| v - \overline { { v } } \| ^ { 2 } = 4 \| v \| ^ { 2 }$ ,thisimplies

$$
I ( x _ { n } , \dot { x } _ { n } ) = 2 \omega ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } + \mathcal { O } ( h ) .
$$

Acomparison with (6.29）then gives the stated relation between $I$ and $I _ { h }$ The relation between $H$ and $\mathcal { H } _ { h }$ is proved in the same way,using in addition (6.23).□

# XIII.7Long-Time Near-Conservation of Total and Oscillatory Energy

With the results of the previous section,we can now show that the numerical method nearlypreserves the total energy $H$ and the oscillatory energy $I$ over time intervals oflength $C _ { N } h ^ { - N + 1 }$ ,forany $N$ forwhich the non-resonance condition (5.10)is satisfied.Sucharesult isdueto Hairer&Lubich(2000a).

For convenience we restate the assumptions:

theenergy bound(2.3): $\begin{array} { r } { \frac 1 2 \| \dot { { \boldsymbol x } } ( 0 ) \| ^ { 2 } + \frac 1 2 \| { \boldsymbol \varOmega } { \boldsymbol x } ( 0 ) \| ^ { 2 } \leq E ; } \end{array}$ the condition on the numerical solution:the values $\phi { x _ { n } }$ stay ina compact subset of a domain on which the potential $U$ is smooth;

·theconditions on the filter functions: $\psi$ and $\phi$ areeven,real-analytic,and have noreal zeros other than integral multiples of $\pi$ ;theysatisfy $\psi ( 0 ) = \phi ( 0 ) = 1$ and (4.1）:

$$
\begin{array} { r l } & { | \psi ( h \omega ) | \leq C _ { 1 } \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) , \qquad | \phi ( h \omega ) | \leq C _ { 2 } | \mathrm { s i n c } ( \frac { 1 } { 2 } h \omega ) | , } \\ & { | \psi ( h \omega ) \phi ( h \omega ) | \leq C _ { 3 } | \mathrm { s i n c } ( h \omega ) | \% } \end{array}
$$

·the condition $h \omega \geq c _ { 0 } > 0$ ；

·the non-resonance condition (5.10):for some $N \geq 2$ ,

$$
| \sin ( \frac { 1 } { 2 } k h \omega ) | \geq c \sqrt { h } \mathrm { f o r } k = 1 , \ldots , N .
$$

Theorem7.1. Under theaboveconditions,thenumerical solutionof(2.1) obtained bythemethod(2.7)-(2.8)with(2.9) satisfies

$$
\begin{array} { r l r } { H ( x _ { n } , \dot { x } _ { n } ) \ = \ H ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } & { } & { f o r \quad 0 \leq n \dot { h } \leq { \dot { h } } ^ { - N + 1 } , } \\ { I ( x _ { n } , \dot { x } _ { n } ) \ = \ } & { } & { I ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } \end{array}
$$

The constants symbolized by $\mathcal { O }$ areindependentof $_ { n }$ ， $h$ ， $\omega$ satisfying the above conditions,but dependon $N$ andtheconstantsinthe conditions.

ProofTheestimatesof Theorem6.6 holduniformly over bounded intervals.We nowapply thoseestimatesrepeatedly on intervals oflength $h$ ,formodulated Fourier expansions corresponding to different starting values.As longas $( x _ { n } , { \dot { x } } _ { n } )$ satisfies thebounded-energy condition(2.3） (possibly witha larger constant $E$ ),Theorem5.2 givesa modulated Fourier expansion that corresponds to starting values $( x _ { n } , { \dot { x } } _ { n } )$ . Wedenote the vector of coefficient functions of this expansion by ${ \bf z } _ { n } ( t )$ :

$$
\mathbf { z } _ { n } = ( z _ { n } ^ { - N + 1 } , \ldots , z _ { n } ^ { - 1 } , y _ { n } , z _ { n } ^ { 1 } , \ldots , z _ { n } ^ { N - 1 } )
$$

(omiting the notational dependence on $h$ for simplicity).Because of the uniqueness, upto $\mathcal { O } ( h ^ { N + 1 } )$ ,of the coefficient functions of the modulated Fourier expansion constructed by(5.2O),the following diagram commutes up to terms of size $\mathcal { O } ( h ^ { N + 1 } )$ ：

$$
\begin{array} { c c c c c } { { ( x _ { n } , \dot { x } _ { n } ) } } & { { \longleftrightarrow } } & { { } } & { { } } & { { ( { \bf z } _ { n } ( 0 ) , \dot { \bf z } _ { n } ( 0 ) ) } } \\ { { } } & { { } } & { { } } & { { } } & { { } } \\ { { \Big \{ \begin{array} { l c l } { { { \mathrm { n u m e r i c a l } } } } & { { } } & { { } } & { { } } \\ { { { \mathrm { m e t h o d } } } } & { { } } & { { } } & { { } } \end{array} \Big \} \begin{array} { l } { { \mathrm { f l o w } } } \\ { { \mathrm { ~ ( { \bf z } _ { n } ( h ) , \dot { \bf z } _ { n } ( h ) ) } } } \end{array} } } \\ { { \begin{array} { l } { { } } & { { } } \\ { { } } & { { } } \\ { { ( { \bf z } _ { n + 1 } , \dot { x } _ { n + 1 } ) } } \end{array} } } & { { \longleftrightarrow } } & { { } } & { { ( { \bf z } _ { n + 1 } ( 0 ) , \dot { \bf z } _ { n + 1 } ( 0 ) ) } } \end{array}
$$

The construction of the coefficient functions via (5.2O) shows that also higher derivativesof ${ \bf z } _ { n }$ at $h$ and ${ { \mathbb { Z } } _ { n + 1 } }$ atOdiffer by only $\mathcal { O } ( h ^ { N + 1 } )$ .From the abovediagram and Theorem6.6wethusobtain

$$
\begin{array} { r l r } { \ \mathcal { H } _ { h } [ { \bf z } _ { n + 1 } ] ( 0 ) } & { = } & { \mathcal { H } _ { h } [ { \bf z } _ { n } ] ( h ) + { \cal O } ( h ^ { N + 1 } ) } \\ & { = } & { \mathcal { H } _ { h } [ { \bf z } _ { n } ] ( 0 ) + { \cal O } ( h ^ { N + 1 } ) . } \end{array}
$$

Repeated use of this relation gives

$$
\mathcal { H } _ { h } [ { \mathbf z } _ { n } ] ( 0 ) = \mathcal { H } _ { h } [ { \mathbf z } _ { 0 } ] ( 0 ) + \mathcal { O } ( n h ^ { N + 1 } ) .
$$

Moreover,by Theorem 6.6 the coefficient functions corresponding to thestarting values $( x _ { n } , { \dot { x } } _ { n } )$ and $( x _ { 0 } , \dot { x } _ { 0 } )$ satisfy

$$
\begin{array} { r c l } { { \displaystyle \mathcal { H } _ { h } [ { \bf z } _ { n } ] ( 0 ) } } & { { = } } & { { H ( x _ { n } , \dot { x } _ { n } ) + { \mathcal O } ( h ) ~ , } } \\ { { \displaystyle \mathcal { H } _ { h } [ { \bf z } _ { 0 } ] ( 0 ) } } & { { = } } & { { H ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) ~ . } } \end{array}
$$

So we obtain

$$
\begin{array} { r l } & { H ( x _ { n } , \dot { x } _ { n } ) - H ( x _ { 0 } , \dot { x } _ { 0 } ) \ = \ \mathcal { H } _ { h } [ \mathbf { z } _ { n } ] ( 0 ) - \mathcal { H } _ { h } [ \mathbf { z } _ { 0 } ] ( 0 ) + \mathcal { O } ( h ) } \\ & { \ = \ \mathcal { O } ( n h ^ { N + 1 } ) + \mathcal { O } ( \dot { h } ) \ , } \end{array}
$$

which gives the desired bound for the deviation of the total energy along the numerical solution.The same argument appliesto $I ( x _ { n } , { \dot { x } } _ { n } )$ . 门

Theimposed bounds of $\psi$ and $\phi$ become important when $h \omega$ is close to an integral multipleof $\pi$ .Arethese conditions also sufficientto guarantee favourable energy behaviouruniformlyin $h \omega$ ,arbitrarilyclosetomultiplesof $\pi { } ?$ Unfortunately theanswer is negative (seeFig.2.5to Fig.2.7).Theanalysis of method(2.7)-(2.9) for exact resonances $h \omega = m \pi$ withinteger $m$ shows that stronger conditions

$$
| \psi ( h \omega ) | \leq C \left| \operatorname { s i n c } ( h \omega ) \right| , \quad | \psi ( h \omega ) \phi ( h \omega ) | \leq C \operatorname { s i n c } ^ { 2 } ( h \omega )
$$

arerequired.Even this is not sufficient for near-conservation ofthe total and the oscillatory energy for $h \omega$ nearamultipleof $\pi$ Forlinearproblems

$$
\ddot { x } + \binom { 0 } { 0 } \stackrel { 0 } { \omega ^ { 2 } } ) x = - A x
$$

witha two-dimensional symmetric matrix $A$ with $a _ { 0 0 } > 0$ ,andwith initial values satisfying the bounded-energycondition(2.3),Hairer&Lubich(2Oooa) showthat thenumerical method conserves the total energy up to $\mathcal { O } ( h )$ uniformly forall times and forall values of $h \omega$ ,ifandonlyif

$$
\psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \xi ) \phi ( \xi ) .
$$

Thereisno method(2.7)-(2.8)which approximately preserves the oscillatory energy $\boldsymbol { \mathit { 1 } }$ uniformly forall $h \omega$ ina fixed open interval that containsa multiple of $2 \pi$

Insummary,the bad effect of step-size resonances on the energy behaviour of themethod cannot beeliminated,but itcan beconsiderablymitigated byanappropriate choice of the filter functions $\psi$ and $\phi$ ,

# XIII.8 Energy Behaviour of the Stormer-Verlet Method

Theresults of Sections XII.5-XIII.7 provide new insight into the energy behaviourof the classical Stormer-Verlet method.We present in this sectionweakened versions of results of Hairer&Lubich(2000b).

Inapplications,the Stormer-Verlet method is typically used with step sizes $h$ for which the product with the highest frequency $\omega$ isintherange oflinear stability,but isbounded away from O.For example,in spatially discretizedwave equations, $h \omega$ isknownas theCFL number,which is typicallykept near1.Values of $h \omega$ around $\textstyle { \frac { 1 } { 2 } }$ areoften used in moleculardynamics.In contrast,the backward error analysis of Chap.IXexplains the long-time energy behaviour only for $h \omega  0$ ..

Consider now applying the Stormer-Verlet method to the nonlinear model problem (2.1)-(2.3),

$$
x _ { n + 1 } - 2 x _ { n } + x _ { n - 1 } = - h ^ { 2 } \Omega ^ { 2 } x _ { n } - h ^ { 2 } \nabla U ( x _ { n } ) ,
$$

with $h \omega < 2$ forlinear stability.Themethodismadeaccessibletotheanalysis ofSections XII.3-XIII.7 by rewritingit as a trigonometric method (2.6) witha modified frequency:

$$
x _ { n + 1 } - 2 \cos ( h \widetilde { \Omega } ) x _ { n } + x _ { n - 1 } = - h ^ { 2 } \nabla U ( x _ { n } ) ,
$$

where

$$
\begin{array} { r } { \widetilde { \Omega } = \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { \widetilde { \omega } I } \end{array} \right) \quad \mathrm { w i t h } \quad \sin ( \frac { 1 } { 2 } h \widetilde { \omega } ) = \frac { 1 } { 2 } h \omega . } \end{array}
$$

The velocity approximation

$$
{ \dot { x } } _ { n } = { \frac { x _ { n + 1 } - x _ { n - 1 } } { 2 h } }
$$

doesnot correspond to the velocity approximation (2.11） of the trigonometric method,but this presents onlya minor technical difficulty.We showthat the followingmodified energiesare well conservedby the Stormer-Verletmethod:

$$
\begin{array} { l l } { { H ^ { * } ( x , \dot { x } ) = H ( x , \dot { x } ) + \frac { 1 } { 2 } \gamma \| \dot { x } _ { 1 } \| ^ { 2 } } } & { { \mathrm { w i t h } \gamma = \frac { 1 } { 1 - \frac { 1 } { 4 } ( h \omega ) ^ { 2 } } - 1 . } } \\ { { I ^ { * } ( x , \dot { x } ) = I ( x , \dot { x } ) + \frac { 1 } { 2 } \gamma \| \dot { x } _ { 1 } \| ^ { 2 } } } & { { \mathrm { w i t h } \gamma = \frac { 1 } { 1 - \frac { 1 } { 4 } ( h \omega ) ^ { 2 } } - 1 . } } \end{array}
$$

Here $H$ and $\varLambda$ areagain the totaland theoscilatory energy of thesystem (2.1） (defined with the original $\omega$ ,notwith $\omega$ ).

Theorem8.1.Let the Stormer-Verlet methodbeappliedtotheproblem(2.1)-(2.3) with a step size $h$ forwhich $0 < c _ { 0 } \leq h \omega \leq c _ { 1 } < 2$ and $| \sin ( \frac { 1 } { 2 } k h \widetilde { \omega } ) | \geq c \sqrt { h }$ for $k = 1 , \ldots , N$ forsome $N \geq 2$ and $c > 0$ Suppose furtherthat thenumerical solution values $x _ { n }$ stay ina region onwhich all derivatives of $U$ arebounded.Then, themodifedenergies along the numerical solution satisfy

$$
\begin{array} { r l } & { H ^ { * } ( x _ { n } , \dot { x } _ { n } ) = H ^ { * } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } \\ & { I ^ { * } ( x _ { n } , \dot { x } _ { n } ) = I ^ { * } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } \end{array} \quad f o r ~ 0 \leq n h \leq h ^ { - N + 1 } .
$$

The constants symbolized by $\mathcal { O }$ are independent ofn, $h$ , $\omega$ withthe above conditions.

Proof.Withthemodifiedvelocities $x _ { n } ^ { \prime }$ defined by

$$
2 h \operatorname { s i n c } ( h \widetilde { \Omega } ) x _ { n } ^ { \prime } = x _ { n + 1 } - x _ { n - 1 }
$$

method (8.2) becomesa method (2.6) with (2.11),or equivalently (2.7)-(2.8),with $\varpi$ instead of $\omega$ andwith $\psi ( \xi ) = \phi ( \xi ) = 1$ ，

The condition $0 < c _ { 0 } \leq h \omega \leq c _ { 1 } < 2$ implies $| \sin ( \frac { 1 } { 2 } k h \widetilde { \omega } ) | \geq c _ { 2 } > 0$ for $k = 1 , 2$ ,andhence conditions(7.1）aretrivially satisfiedwith $h \omega$ instead of $h \omega$ Wearethusinthe position toapply Theorem7.1,which yields

$$
\begin{array} { r l r } { \widetilde { H } ( x _ { n } , x _ { n } ^ { \prime } ) \ = \ \widetilde { H } ( x _ { 0 } , x _ { 0 } ^ { \prime } ) + { \mathcal O } ( h ) } & { } & \\ { \widetilde { I } ( x _ { n } , x _ { n } ^ { \prime } ) \ = \ \widetilde { I } ( x _ { 0 } , x _ { 0 } ^ { \prime } ) + { \mathcal O } ( h ) } & { } & \end{array} \quad \mathrm { f o r ~ } 0 \leq n h \leq h ^ { - N + 1 } ,
$$

where $\bar { H }$ and $\vec { I }$ aredefined in the same way as $H$ and $\boldsymbol { { I } }$ ,butwith $\boldsymbol { \widetilde { \omega } }$ in place of $\boldsymbol { \omega }$ . ThecomponentsoftheStormer-Verletvelocities ${ \dot { x } } _ { n }$ and themodifed velocities $x _ { n } ^ { \prime }$ arerelated by

$$
\dot { x } _ { n , 0 } = x _ { n , 0 } ^ { \prime } , \qquad \dot { x } _ { n , 1 } = \operatorname { s i n c } ( h \widetilde { \omega } ) x _ { n , 1 } ^ { \prime } = \frac { \omega } { \widetilde { \omega } } \sqrt { 1 - \frac { 1 } { 4 } h ^ { 2 } \omega ^ { 2 } } x _ { n , 1 } ^ { \prime } ,
$$

so that

$$
\begin{array} { l } { \displaystyle \widetilde { I } ( x _ { n } , x _ { n } ^ { \prime } ) ~ = ~ \frac { 1 } { 2 } \| x _ { n , 1 } ^ { \prime } \| ^ { 2 } + \frac { 1 } { 2 } \widetilde { \omega } ^ { 2 } \| x _ { n , 1 } \| ^ { 2 } } \\ { \displaystyle ~ = ~ \frac { 1 } { 2 } \frac { \widetilde { \omega } ^ { 2 } } { \omega ^ { 2 } } \frac { 1 } { 1 - \frac { 1 } { 4 } h ^ { 2 } \omega ^ { 2 } } \| \dot { x } _ { n , 1 } \| ^ { 2 } + \frac { 1 } { 2 } \frac { \widetilde { \omega } ^ { 2 } } { \omega ^ { 2 } } \omega ^ { 2 } \| x _ { n , 1 } \| ^ { 2 } } \\ { \displaystyle ~ = ~ \frac { \widetilde { \omega } ^ { 2 } } { \omega ^ { 2 } } I ^ { * } ( x _ { n } , \dot { x } _ { n } ) . } \end{array}
$$

Similarly,

$$
\begin{array} { l } { { \displaystyle H ^ { * } ( x _ { n } , \dot { x } _ { n } ) ~ = ~ \frac 1 2 \| \dot { x } _ { n , 0 } \| ^ { 2 } + U ( x _ { n } ) + { \cal I } ^ { * } ( x _ { n } , \dot { x } _ { n } ) } } \\ { ~ = ~ { \cal \widetilde H } ( x _ { n } , x _ { n } ^ { \prime } ) + \left( \frac { \omega ^ { 2 } } { { \cal \widetilde \omega } ^ { 2 } } - 1 \right) { \cal \widetilde I } ( x _ { n } , x _ { n } ^ { \prime } ) , } \end{array}
$$

and hence(8.6)yields the result.

For fixed $h \omega \geq c _ { 0 } > 0$ and $h  0$ ,themaximumdeviation in the energy does not tend toO,due to the highly oscillatory term $\scriptstyle { \frac { 1 } { 2 } } \gamma \Vert { \dot { x } } _ { 1 } \Vert ^ { 2 }$ in $H ^ { * } ( x , \dot { x } )$ and $I ^ { * } ( x , \dot { x } )$ . We show,however,that time averages of $H$ and $\boldsymbol { \mathit { I } }$ arenearly preserved over long time.Foran arbitrary fixed $T > 0$ ,considertheaverages over intervalsoflength $T$ ,

$$
\begin{array} { l } { \displaystyle \overline { { H } } _ { n } ~ = ~ \frac { 1 } { T } h \sum _ { | j h | \leq T / 2 } H ( x _ { n + j } , \dot { x } _ { n + j } ) } \\ { \displaystyle \overline { { I } } _ { n } ~ = ~ \frac { 1 } { T } h \sum _ { | j h | \leq T / 2 } I ( x _ { n + j } , \dot { x } _ { n + j } ) . } \end{array}
$$

Theorem8.2.Under theconditions ofTheorem8.1,thetimeaveragesof thetotal andthe oscillatory energyalong the numerical solution satisfy

$$
\begin{array} { r l } { \overline { { H } } _ { n } = \overline { { H } } _ { 0 } + \mathcal { O } ( h ) } & { { } \quad f o r 0 \leq n h \leq h ^ { - N + 1 } , } \\ { \overline { { I } } _ { n } = \overline { { I } } _ { 0 } + \mathcal { O } ( h ) } & { { } \quad f o r 0 \leq n h \leq h ^ { - N + 1 } . } \end{array}
$$

Theconstants symbolizedby $\mathcal { O }$ areindependent ofn,h, $\omega$ withthe aboveconditions.

ProofWe show

$$
\begin{array} { l } { { \displaystyle \overline { { { H } } } _ { n } ~ = ~ H ^ { * } ( x _ { n } , \dot { x } _ { n } ) - \frac { 1 } { 2 } \frac { \gamma } { 1 + \gamma } ~ I ^ { * } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) } } \\ { { \displaystyle \overline { { { I } } } _ { n } ~ = ~ I ^ { * } ( x _ { n } , \dot { x } _ { n } ) - \frac { 1 } { 2 } \frac { \gamma } { 1 + \gamma } ~ I ^ { * } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) , } } \end{array}
$$

whichimpliestheresultby Theorem 8.1.Consider the modulated Fourier expansions of $x _ { n }$ and $\boldsymbol { x } _ { n } ^ { \prime }$ for $t = n h$ inaboundedinterval.Theorem5.3 shows that

$$
x _ { n , 1 } ^ { \prime } = i \widetilde { \omega } \big ( e ^ { i \widetilde { \omega } t } \bar { z } _ { h , 1 } ^ { 1 } ( t ) - e ^ { - i \widetilde { \omega } t } \overline { { z _ { h , 1 } ^ { 1 } } } ( t ) \big ) + \mathcal { O } ( h ) , \qquad t = n h ,
$$

with $z _ { h , 1 } ^ { 1 } ( t )$ from the modulated Fourier expansion of Theorem 5.2 (with $\bar { \omega }$ instead of $\omega$ ).With(8.7)it follows that

$$
\begin{array} { r } { \dot { x } _ { n , 1 } = i \omega \sqrt { 1 - \frac { 1 } { 4 } h ^ { 2 } \omega ^ { 2 } } \left( e ^ { i \widetilde { \omega } t } z _ { h , 1 } ^ { 1 } ( t ) - e ^ { - i \widetilde { \omega } t } \overline { { z _ { h , 1 } ^ { 1 } } } ( t ) \right) + { \mathcal O } ( h ) , } \end{array}
$$

and therefore,recalling the definitionof $\gamma$ ，

$$
\Vert \dot { x } _ { n , 1 } \Vert ^ { 2 } = \omega ^ { 2 } \frac { 1 } { 1 + \gamma } \left( 2 \Vert z _ { h , 1 } ^ { 1 } ( t ) \Vert ^ { 2 } - 2 \mathrm { R e } e ^ { 2 i \widetilde { \omega } t } z _ { h , 1 } ^ { 1 } ( t ) ^ { 2 } \right) + \mathcal { O } ( h ) .
$$

Theorems 5.2and5.3yield

$$
2 \widetilde { \omega } ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } = \widetilde { I } \big ( x _ { n } , x _ { n } ^ { \prime } \big ) + \mathcal { O } ( h )
$$

and hence,by(8.8),

$$
2 \omega ^ { 2 } \| z _ { h , 1 } ^ { 1 } ( t ) \| ^ { 2 } = I ^ { * } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) .
$$

Apartial summation shows that the time average over thehighly oscillatory terms $e ^ { 2 w t } \omega ^ { 2 } z _ { h , 1 } ^ { 1 } ( t ) ^ { 2 }$ is ${ \mathcal { O } } ( h ) ,$ This finallygives

$$
\frac { 1 } { T } h \sum _ { | j | \leq T / 2 } \| \dot { x } _ { j , 1 } \| ^ { 2 } = \frac { 1 } { 1 + \gamma } I ^ { * } ( x _ { n } , \dot { x } _ { n } ) + O ( h ) .
$$

Taking the time averages in the expressions of the definition (8.4)of $H ^ { * }$ and $I ^ { * }$ then yields(8.12）. □

![](images/6c30361a7a0aeb261e657142a134702692c70b8e16e3aecad700cf1bd32b0dbb.jpg)  
Fig.8.1.Total energies(left）and their predicted averages(right） for the Stormer-Verlet method and fortwodifferent initial values,with $\omega = 5 0$ and $h$ suchthat $h \omega = 0 . 8$

Figure 8.1 illustrates the above result.It shows the total energy $H$ for two different initial values on the left,and theaverages as predicted by the expression on theright-hand side of(8.12)on the right picture.The initial values areas in Chap.I with the exception of $x _ { 1 , 1 } ( 0 )$ and $\dot { x } _ { 1 , 1 } ( 0 )$ Wetake $x _ { 1 , 1 } ( 0 ) = \sqrt { 2 } / \omega$ , $\dot { x } _ { 1 , 1 } ( 0 ) = 0$ forone set of initial values and $x _ { 1 , 1 } ( 0 ) = 0$ , ${ \dot { x } } _ { 1 , 1 } ( 0 ) = { \sqrt { 2 } }$ for the other.The total energiesat the initial values are 2.0o240o32and 2,respectively.

# XIII.9 Systems with Several Constant Frequencies

This section studies the conservation of invariants and almost-invariants along numerical approximationsof an extension of(2.1） to systemswith the Hamiltonian function

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ^ { - 1 } p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q ^ { T } A q + U ( q )
$$

witha positive definite constant matrix $M$ andapositive semi-definite constant matrix $A$ .With the Cholesky decomposition $M = L L ^ { T }$ and the canonical transformation $\widetilde { p } = L ^ { - 1 } p , \ \widetilde { q } = L ^ { T } q$ we obtaina Hamiltonian where the mass matrix is the identity matrix and $A$ is transformed to $\begin{array} { r } { \boldsymbol { A } = \boldsymbol { L } ^ { - 1 } \boldsymbol { A } \boldsymbol { L } ^ { - T } . } \end{array}$ Diagonalizing $\bar { A } = Q A Q ^ { T }$ and transforming to $x = Q ^ { T } { \widetilde { q } }$ thenyieldsa Hamiltonian of the form(we omit the tilde on $U ( x ) = U ( q )$ and $H ( x , \dot { x } ) = H ( p , q )$

$$
H ( x , \dot { x } ) = \frac { 1 } { 2 } \sum _ { j = 0 } ^ { \ell } \Bigl ( \| \dot { x } _ { j } \| ^ { 2 } + \frac { \lambda _ { j } ^ { 2 } } { \varepsilon ^ { 2 } } \| x _ { j } \| ^ { 2 } \Bigr ) + U ( x ) ,
$$

where ${ \boldsymbol { x } } = ( x _ { 0 } , x _ { 1 } , \ldots , x _ { \ell } )$ with $x _ { j } \in \mathbb { R } ^ { d _ { j } }$ , $\lambda _ { 0 } = 0$ ,and $\lambda _ { j } > 0$ for $j \geq 1$ are all distinct. After rescaling $\boldsymbol { \varepsilon }$ we may assume $\lambda _ { j } \geq 1$ for $j = 1 , \ldots , \ell$

Following Cohen,Hairer $\&$ Lubich (2oo4)we extend the results of the previous sections to the multi-frequency case $\ell > 1$ Modulated Fourier expansionsareagain thebasic analytical tool.A new aspect is possible resonance among the $\lambda _ { j }$ ,

# XIII.9.1 Oscillatory Energiesand Resonances

Theequations of motion for the Hamiltonian system (9.2） can be written as the system of second-order differential equations

$$
\ddot { x } = - \Omega ^ { 2 } x + g ( x ) ,
$$

where $\Omega = \mathrm { d i a g } ( \omega _ { j } I )$ with the frequencies $\omega _ { j } = \lambda _ { j } / \varepsilon$ and $g ( x ) = - \nabla U ( x )$ As suitable numerical methodswe consideragain the class of trigonometric integrators studied in Sect.XII.2,(2.6)with(2.11),with filter functions $\psi$ and $\phi$ .

Weare interested in the long-timenear-conservation of the total energy $H ( x , { \dot { x } } )$ and the oscillatory energies

$$
I _ { j } ( x , \dot { x } ) = \frac { 1 } { 2 } \Big ( \| \dot { x } _ { j } \| ^ { 2 } + \frac { \lambda _ { j } ^ { 2 } } { \varepsilon ^ { 2 } } \| x _ { j } \| ^ { 2 } \Big ) \mathrm { f o r } j \geq 1
$$

or suitable linear combinations thereof.Benettin,Galgani& Giorgilli（1989) have shown that the quantities

$$
\tilde { I } _ { \mu } ( x , \dot { x } ) = \sum _ { j = 1 } ^ { \ell } \frac { \mu _ { j } } { \lambda _ { j } } I _ { j } ( x , \dot { x } )
$$

areapproximately preserved alongevery bounded solution of theHamiltonian systemthat hasatotal energy bounded independentlyof $\boldsymbol { \varepsilon }$ ,onexponentiallylongtime intervals of size $\mathcal { O } ( e ^ { c / \varepsilon } )$ if the potential $U ( x )$ isanalyticand $\boldsymbol { \mu } = ( \mu _ { 1 } , \dots , \mu _ { \ell } )$ is orthogonal to the resonance module

$$
\mathcal { M } = \{ k \in \mathbb { Z } ^ { \ell } : k _ { 1 } \lambda _ { 1 } + . . . , + k _ { \ell } \lambda _ { \ell } = 0 \} ,
$$

if a diophantine non-resonance condition holds outside $\mathcal { M }$ (Cf.also Sect.XII.9.4 below.)

Since $\mu = \lambda$ is orthogonal to $\mathcal { M }$ ,thetotaloscilatoryenergy $\textstyle \sum _ { j = 1 } ^ { \ell } I _ { j } ( x , \dot { x } )$ of thesystem isapproximatelypreserved independentlyof theresonance module $\mathcal { M }$ Subtracting this expression from the total energy(1.7),we see that also the smooth energy

$$
K ( x , \dot { x } ) = \frac { 1 } { 2 } \| \dot { x } _ { 0 } \| ^ { 2 } + U ( x )
$$

isapproximately preserved.Withan $\boldsymbol { E }$ -independentbound of thetotal energy $H ( x , { \dot { x } } )$ we have $x _ { j } = \mathcal { O } ( \varepsilon )$ for $j = 1 , \ldots , \ell$ sothat $K ( x , { \dot { x } } )$ is close to the Hamiltonian ofthereduced system inwhichall oscillatory degrees of freedomare taken out, $\begin{array} { r } { H _ { 0 } ( x _ { 0 } , \dot { x } _ { 0 } ) = \frac { 1 } { 2 } \| \dot { x } _ { 0 } \| ^ { 2 } + U ( x _ { 0 } , 0 , \dots , 0 ) . } \end{array}$

Example9.1.To illustrate the conservation of the various energies,we considera Hamiltonian（1.7）with $\ell = 3$ , $\lambda = ( 1 , { \sqrt { 2 } } , 2 )$ and we assume that the dimensions of xareall1with the exception of that of $x _ { 1 } = ( x _ { 1 , 1 } , x _ { 1 , 2 } )$ which is2.The resonance module is then $\mathcal { M } = \left\{ \left( k _ { 1 } , 0 , k _ { 3 } \right) ; k _ { 1 } + 2 k _ { 3 } = 0 \right\}$ Wetake $\varepsilon ^ { - 1 } = \omega = 7 0$ ,the potential

![](images/4a0e06ef59229f4b470cd8828e52bf7eb9d8220fe33f3c51e8d9ecff1ccceb3c.jpg)  
Fig9.1.Oscilltoryenergiesoftheindividualcomponents(thefrequencies $\lambda _ { j } \omega = \lambda _ { j } / \varepsilon$ areindicated)and the sum $I _ { 1 } + I _ { 3 }$ of theoscillatory energies corresponding to theresonant frequencies $\omega$ and $_ { 2 \omega }$

$$
U ( x ) = ( 0 . 0 5 + x _ { 1 , 1 } + x _ { 1 , 2 } + x _ { 2 } + 2 . 5 x _ { 3 } ) ^ { 4 } + \frac { 1 } { 8 } x _ { 0 } ^ { 2 } x _ { 1 , 1 } ^ { 2 } + \frac { 1 } { 2 } x _ { 0 } ^ { 2 } ,
$$

and $x ( 0 ) = ( 1 , 0 . 3 \varepsilon , 0 . 8 \varepsilon , - 1 . 1 \varepsilon , 0 . 7 \varepsilon )$ , $\dot { x } ( 0 ) = ( - 0 . 2 , 0 . 6 , 0 . 7 , - 0 . 9 , 0 . 8 )$ asinitial values.We consider $I _ { \mu }$ for $\mu = ( 1 , 0 , 2 )$ and $\mu = ( 0 , { \sqrt { 2 } } , 0 )$ ,which are both orthogonal to $\mathcal { M } .$ InFig.9.1 we plot the oscillatory energies for the individual components of the system.The corresponding frequencies are attached to the curves. We also plot the sum $I _ { 1 } + I _ { 3 }$ of the three oscillatory energies corresponding to the resonant frequencies $1 / \varepsilon$ and $2 / \varepsilon$ We see that $I _ { 1 } + I _ { 3 }$ aswell as $I _ { 2 }$ (whichare $I _ { \mu }$ forthe above two vectors $\mu \perp \mathcal { M }$ arewell conserved over long times up to small oscillations of size ${ \mathcal { O } } ( \varepsilon ) .$ Thereisan energy exchange between the two components corresponding to the same frequency $1 / \varepsilon$ ,andonalarger scaleanenergyexchange between $I _ { 1 }$ and $I _ { 3 }$ .

Numerical Experiment.Asa first method we take(2.6)with $\phi ( \xi ) = 1$ and $\psi ( \xi ) =$ $\mathrm { s i n c } ( \xi )$ ,and we apply it with large step sizes so that $h \omega = h / \varepsilon$ takes the values1,2, 4,and8.Figure 9.2 shows the various oscillatory energieswhich can be compared to theexact values inFig.9.1.Forallstep sizes,the oscillatory energy corresponding to the frequency $\sqrt { 2 } w$ and thesum ${ { I } _ { 1 } } + { { I } _ { 3 } }$ arewell conserved on long time intervals. Oscillations in these expressions increase with $h$ The energy exchange between resonant frequencies is close to that of the exact solution.We have not plotted the totalenergy $H ( x _ { n } , { \dot { x } } _ { n } )$ nor the smooth energy $K ( x _ { n } , \dot { x } _ { n } )$ of（9.7）.Both are well conserved over long times.

Werepeat this experiment with the method where $\phi ( \xi ) ~ = ~ 1$ and $\psi ( { \boldsymbol { \xi } } ) = $ $\mathrm { s i n c } ^ { 2 } ( \xi / 2 )$ (Fig.9.3).Only the oscillatory energy corresponding to $\sqrt { 2 } \omega$ isapproximately conserved over long times.Neither the expression $I _ { 1 } + I _ { 3 }$ northe total energy(not shown） are conserved.The smooth energy $K ( x _ { n } , \dot { x } _ { n } )$ is,however,well conserved.

Figure9.4 shows the corresponding result for the method with $\phi ( \xi ) = \mathrm { s i n c } ( \xi )$ and $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) .$ Theoscillatory energy for $\sqrt { 2 } \omega$ andalso $I _ { 1 } + I _ { 3 }$ arewell conserved.However,the energy exchange between the resonant frequencies is not correctly reproduced.

![](images/811237235de621cd272851626a413b8b06208e6c7f5db080ae8ff72f564d19a2.jpg)  
Fig.9.2.Oscillatory energiesas in Fig.9.1along the numerical solution of(2.6)with $\phi ( \xi ) =$ 1and $\psi ( \xi ) = \mathrm { s i n c } ( \xi )$

![](images/45f05d7db4fb5ded611f66e840b90673910b8c849030ecc61472040ff8ccb97a.jpg)  
Fig.9.3.Oscilltory energies as in Fig.9.1 along thenumerical solution of(2.6)with $\phi ( \xi ) =$ 1and $\psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \xi / 2 )$

![](images/3879848582eefc44996afe8e096cccc64f28a15b2c9dd528dc4948d6ca510dfd.jpg)  
Fig.9.4.Oscillatory energies as in Fig.9.1along thenumerical solution of(2.6)with $\phi ( \xi ) =$ $\mathrm { s i n c } ( \xi )$ and $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi )$

# XIII.9.2Multi-Frequency Modulated Fourier Expansions

The above numerical phenomena can be understood with amulti-frequency version of the modulated Fourier expansions studied in the previous chapter.We only outline thederivation and properties,since they are in large parts similar to the singlefrequencycase.Moredetailscan be foundin Cohen,Hairer&Lubich(2Oo4).We assume conditions that extend those of the previous sections:

·The energyof theinitial values is bounded independentlyof $\boldsymbol { \varepsilon }$ ,

$$
\frac { 1 } { 2 } \| \dot { x } ( 0 ) \| ^ { 2 } + \frac { 1 } { 2 } \| \varOmega x ( 0 ) \| ^ { 2 } \leq E .
$$

The numerical solution values $\boldsymbol { \varPhi } . \boldsymbol { x } _ { n }$ stay ina compact subset ofa domain on which thepotential $U$ is smooth.   
We impose a lower bound on the step size: $h / \varepsilon \geq c _ { 0 } > 0$   
Weassume the numerical non-resonance condition

$$
\Big | \sin \Big ( \frac { h } { 2 \varepsilon } k \cdot \lambda \Big ) \Big | \geq c \sqrt { h } \quad \mathrm { f o r ~ a l l ~ } k \in { \mathbb Z } ^ { \ell } \backslash { \mathcal M } \mathrm { ~ w i t h ~ } | k | \leq N ,
$$

for some $N \geq 2$ and $c > 0$

Forthefilter functions weassumethat for $\xi _ { j } = h \lambda _ { j } / \varepsilon ~ ( j = 1 , \ldots , \ell ) ,$

$$
\begin{array} { r l } & { \left. \psi ( \xi _ { j } ) \right. \leq C _ { 1 } \operatorname { s i n c } ^ { 2 } ( \frac { 1 } { 2 } \xi _ { j } ) , } \\ & { \left. \phi ( \xi _ { j } ) \right. \leq C _ { 2 } \left. \operatorname { s i n c } ( \frac { 1 } { 2 } \xi _ { j } ) \right. , } \\ & { \left. \psi ( \xi _ { j } ) \right. \leq C _ { 3 } \left. \operatorname { s i n c } ( \xi _ { j } ) \phi ( \xi _ { j } ) \right. . } \end{array}
$$

Theconditions on the filter functions are somewhat stronger than necessary,but they facilitate the presentation in the following.

Fora given vector $\lambda = ( \lambda _ { 1 } , \ldots , \lambda _ { \ell } )$ and for the resonance module $\mathcal { M }$ defined by(9.6），we let $\kappa$ beaset of representatives of the equivalence classes in $\mathbb { Z } ^ { \ell } / \mathcal { M }$ which are chosen such that for each $k \in \mathcal { K }$ the sum $| k | = | k _ { 1 } | + \ldots + | k _ { \ell } |$ isminimal in the equivalence class $[ k ] = k + \mathcal { M }$ ,andwith $k \in \mathcal { K }$ ,also $- k \in \mathcal { K }$ Wedenote, for $\mathcal { N }$ of(6.3),

$$
{ \mathcal { N } } = \{ k \in K : | k | < N \} , \qquad { \mathcal { N } } ^ { * } = { \mathcal { N } } \setminus \{ ( 0 , . . . , 0 ) \} .
$$

The following multi-frequency version of Theorem XII.5.2 establishes amodulated Fourier expansion for the numerical solution.

Theorem9.2.Consider the numerical solution of the system(9.3) by the method (2.6)with step size h.Underconditions(9.9)-(9.11),thenumerical solutionadmits anexpansion

$$
x _ { n } = y ( t ) + \sum _ { k \in N ^ { * } } e ^ { i k \cdot \omega t } z ^ { k } ( t ) + \varPsi \cdot O ( t ^ { 2 } h ^ { N } )
$$

with $\omega = \lambda / \varepsilon$ ,uniformly for $0 \leq t = n h \leq T$ and $\boldsymbol { \mathsf { \Sigma } }$ andh satisfying $h / \varepsilon \geq c _ { 0 } > 0$ Themodulationfunctions togetherwith alltheirderivatives(uptosomearbitrarily fixed order)areboundedby

$$
\begin{array} { c c } { { y _ { 0 } } } & { { y _ { i } = \mathcal { O } ( \varepsilon ^ { 2 } ) } } \\ { { z _ { j } ^ { \pm ( j ) } } } & { { = \mathcal { O } ( \varepsilon ) , } } \\ { { z _ { j } ^ { k } = \mathcal { O } ( h \varepsilon ^ { | k | } ) } } & { { f o r \ k \not = \mathcal { O } ( \varepsilon ^ { 2 } ) } } \end{array}
$$

for $j = 1 , \ldots , \ell .$ Here, $\langle j \rangle = ( 0 , \ldots , 1 , \ldots , 0 )$ is the jthunit vector. The last estimateholdsalso for $z _ { 0 } ^ { k }$ forall $k \in \mathcal { N } ^ { * }$ Moreover,the function $y$ isreal-valued and $z ^ { - k } = { \overline { { z ^ { k } } } }$ forall $k \in \mathcal { N } ^ { * }$ .The constants symbolizedby the $\mathcal { O }$ -notation are independent ofh, $\scriptscriptstyle \stackrel { \scriptscriptstyle  } { \sim }$ and $\lambda _ { j }$ with(9.1O),but they dependon $E$ ， $N$ c,and $T$ .

Theproof extends thatof Theorem XII.5.2.In termsof the diferenceoperator of the method, $L ( h D ) = e ^ { h D } - 2 \cos h \itOmega + e ^ { - h D } ,$ thefunctions $y ( t )$ and $z ^ { k } ( t )$ are constructed such that,up to terms of size $\varPsi \cdot \mathcal { O } ( h ^ { N + 2 } )$ ，

$$
\begin{array} { r l r } & { } & { \displaystyle \bar { L } ( h D ) y = h ^ { 2 } \bar { \psi } \Big ( \bar { g } ( \varPhi y ) + \sum _ { s ( \alpha ) \sim 0 } \frac 1 { m ! } g ^ { ( m ) } ( \varPhi y ) ( \varPhi z ) ^ { \alpha } \Big ) } \\ & { } & { \displaystyle L ( h D + i h k \cdot \omega ) z ^ { k } = h ^ { 2 } \varPsi \sum _ { s ( \alpha ) \sim k } \frac 1 { m ! } g ^ { ( m ) } ( \varPhi y ) ( \varPhi z ) ^ { \alpha } , } \end{array}
$$

Here,the sums on the right-hand side are over all $m \geq 1$ and over multi-indices $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ with $\alpha _ { j } \in \mathcal N ^ { * }$ ,forwhich the sum $\begin{array} { r } { s ( \alpha ) = \sum _ { j = 1 } ^ { m } \alpha _ { j } } \end{array}$ satisfies therelation $s ( \alpha ) \sim k$ ,thatis, $s ( \alpha ) - k \in { \mathcal { M } } .$ The notation $( \Phi z ) ^ { \alpha }$ is short for the $- i m -$ -tupie $\left( \boldsymbol { \phi } \boldsymbol { z } ^ { \alpha _ { 1 } } , \ldots , \boldsymbol { \phi } \boldsymbol { z } ^ { \alpha _ { m } } \right)$ .

A similarexpansion to that for $x _ { n }$ exists also for thevelocityapproximation ${ \dot { x } } _ { n }$ , like inTheorem XIII.5.3.Asaconsequence,the oscillatory energy(9.4)along the numerical solution takes the form,at $t = n h \leq T ,$

$$
I _ { j } ( x _ { n } , \dot { x } _ { n } ) = 2 \omega _ { j } ^ { 2 } \| z _ { j } ^ { ( j ) } ( t ) \| ^ { 2 } + \mathcal { O } ( \varepsilon ) .
$$

With the first terms of themodulated Fourier expansion one proves,as in TheoremsXII.4.1and XII.4.2,error boundsoverbounded timeintervalswhichare of second order in the positions and of first orderin the velocities:

$$
\| x _ { n } - x ( t _ { n } ) \| \leq C h ^ { 2 } , \qquad \| \dot { x } _ { n } - \dot { x } ( t _ { n } ) \| \leq C h ,
$$

where $\boldsymbol { C }$ isindependent of $\succ$ ， $h$ and $\textit { n }$ with $n h \le { \cal T }$ and of bounds of solution derivatives.

# XIII.9.3Almost-Invariants of the Modulation System

With $y ^ { 0 } ( t ) = z ^ { 0 } ( t ) = y ( t )$ and $y ^ { k } ( t ) = e ^ { i k \cdot \omega t } z ^ { k } ( t )$ for $k \in \mathcal N$ ,where $_ y$ and $z ^ { k }$ are themodulation functions of Theorem 9.2,we denote

$$
\begin{array} { r } { \mathbf { y } = ( y ^ { k } ) _ { k \in N } , \quad \mathbf { z } = ( z ^ { k } ) _ { k \in N } . } \end{array}
$$

We introduce the extended potential

$$
\mathcal { U } ( \mathbf { y } ) = U ( \phi y ^ { 0 } ) + \sum _ { s ( \alpha ) \sim 0 } \frac { 1 } { m ! } U ^ { ( m ) } ( \phi y ^ { 0 } ) ( \phi \mathbf { y } ) ^ { \alpha } ,
$$

where thesum isagain taken overall $m \geq 1$ and all multi-indices $\alpha = ( \alpha _ { 1 } , \ldots , \alpha _ { m } )$ with $\alpha _ { j } \in \mathcal { N } ^ { * }$ for which $\begin{array} { r } { s ( \alpha ) = \sum _ { j } \alpha _ { j } \in \mathcal { M } . } \end{array}$ The functions $y ^ { k } ( t )$ thensatisfy

$$
\psi ^ { - 1 } \varPhi h ^ { - 2 } L ( h D ) y ^ { k } = - \nabla _ { - k } \mathcal { U } ( \mathbf { y } ) + \varPhi \cdot \mathcal { O } ( h ^ { N } ) ,
$$

where $\nabla _ { - k }$ denotes the gradient with respect to the variable $y ^ { - k }$ This system has almost-invariants that are related tothe Hamiltonian $H$ and the oscillatory energies $I _ { \mu }$ with $\mu \perp \mathcal { M }$

TheEnergy-TypeAlmost-Invariant of the Modulation System.We multiply (9.18)by $( { \dot { y } } ^ { - k } ) ^ { T }$ andsum over $k \in \mathcal N$ to obtain

$$
\sum _ { k \in \mathcal { N } } ( \dot { y } ^ { - k } ) ^ { T } \varPsi ^ { - 1 } \varPhi h ^ { - 2 } L ( h D ) y ^ { k } + \frac { d } { d t } \mathcal { U } ( \mathbf { y } ) = \mathcal { O } ( h ^ { N } ) .
$$

Since we know bounds of the modulation functions $z ^ { k }$ and of their derivatives from Theorem9.2,werewrite thisrelation interms of the quantities $z ^ { k }$ ：

$$
\sum _ { k \in \mathcal { N } } ( \dot { z } ^ { - k } - i k \cdot \omega z ^ { - k } ) ^ { T } \varPsi ^ { - 1 } \varPhi h ^ { - 2 } L ( h D + i h k \cdot \omega ) z ^ { k } + \frac { d } { d t } \mathcal { U } ( \mathbf { z } ) = \mathcal { O } ( h ^ { N } ) .
$$

Asin(6.21）we obtain that the left-hand side of(9.19)can be written as the time derivative ofa function $\mathcal { H } ^ { \ast } | \mathbf { z } | ( t )$ which depends on the values at $t$ of the modulationfunction vector $\mathbb { Z }$ and itsfirst $N$ time derivatives.The relation(9.19） thus becomes

$$
\frac { d } { d t } \mathcal { H } ^ { \ast } [ \mathbf { z } ] ( t ) = \mathcal { O } ( h ^ { N } ) .
$$

Together with the estimates of Theorem 9.2 this construction of $\mathcal { H } ^ { * }$ yieldsthe following multi-frequency extension ofLemma XIII.6.4.

Lemma9.3.Under theassumptionsof Theorem9.2,themodulationfunctions ${ \bf z } =$ $( z ^ { k } ) _ { k \in \mathcal { N } }$ ofthenumerical solution satisfy

$$
\mathcal { H } ^ { * } [ \mathbf { z } ] ( t ) = \mathcal { H } ^ { * } [ \mathbf { z } ] ( 0 ) + \mathcal { O } ( t h ^ { N } )
$$

for $0 \leq t \leq T .$ Moreover,at $t = n h$ wehave

$$
\begin{array} { r } { \mathcal { H } ^ { * } [ \mathbf { z } ] ( t ) = H ^ { * } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( h ) , } \end{array}
$$

where,with $\sigma ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) / \psi ( \xi )$ and ${ \xi } _ { j } = h \lambda _ { j } / { \varepsilon } ,$

$$
H ^ { * } ( x , \dot { x } ) = H ( x , \dot { x } ) + \sum _ { j = 1 } ^ { \ell } \bigl ( \sigma ( \xi _ { j } ) - 1 \bigr ) I _ { j } ( x , \dot { x } ) .
$$

TheMomentum-Type Almost-Invariants of theModulation System.The equations(9.18) have further almost-invariants that result from invariance properties of the extended potential $\boldsymbol { u }$ ,similarly as the conservation of angular momentum results froman invariance of the potential $U$ inamechanical system by Noether's theorem. For $\mu \in \mathbb { R } ^ { \ell }$ and $\mathbf { y } = ( y ^ { k } ) _ { k \in \mathcal { N } }$ we set

$$
S _ { \mu } ( \tau ) \mathbf { y } = ( e ^ { i \mathbf { k } \cdot \mu \tau } y ^ { k } ) _ { k \in \mathcal { N } } , \qquad \tau \in \mathbb { R }
$$

so that,bythe multi-linearityof the derivative,thedefinition(9.17) yields

$$
\mathcal { U } \big ( S _ { \mu } ( \tau ) \mathbf { y } \big ) = \bar { U } ( \varPhi y ^ { 0 } ) + \sum _ { s ( \alpha ) \sim 0 } \frac { e ^ { i s ( \alpha ) \cdot \mu \tau } } { m ! } \bar { U } ^ { ( m ) } ( \varPhi y ^ { 0 } ) ( \varPhi \mathbf { y } ) ^ { \alpha } .
$$

If $\mu \perp \mathcal { M }$ ,then the relation $s ( \alpha ) \sim 0$ implies $s ( \alpha ) \cdot \mu = 0$ ,and hence the expression （9.23）is independent of $_ { \tau }$ It therefore followsthat

$$
0 = \frac { d } { d \tau } \Big | _ { \tau = 0 } \mathcal { U } ( S _ { \mu } ( \tau ) \mathbf { y } ) = \sum _ { k \in \mathcal { N } } i ( k \cdot \mu ) \left( y ^ { k } \right) ^ { T } \nabla _ { k } \mathcal { U } ( \mathbf { y } )
$$

forall vectors $\mathbf { y } = ( y ^ { k } ) _ { k \in \mathcal { N } } .$ If $\mu$ is not orthogonal to $\mathcal { M }$ ,some terms in the sum of (9.23）depend on $\tau$ .However,forthesetermswith $s ( \alpha ) \in \mathcal { M }$ and $s ( \alpha ) \cdot \mu \neq 0$ we have $| s ( \alpha ) | \geq M = \operatorname* { m i n } \{ | k | : 0 \neq k \in \mathcal { M } \}$ andif $\mu \perp \mathcal { M } _ { N }$ ,then $| s ( \alpha ) | \geq N + 1$ Thebounds(5.13) then yield

$$
\sum _ { k \in \mathcal { N } } i ( k \cdot \mu ) \left( \boldsymbol { y } ^ { k } \right) ^ { T } \nabla _ { k } \mathcal { U } ( \mathbf { y } ) = \left\{ \begin{array} { l l } { \mathcal { O } ( \boldsymbol { \varepsilon } ^ { M } ) } & { \mathrm { f o r ~ a r b i t r a r y ~ } \mu } \\ { \mathcal { O } ( \boldsymbol { \varepsilon } ^ { N + 1 } ) } & { \mathrm { f o r ~ } \mu \perp \mathcal { M } _ { N } } \end{array} \right.
$$

for the vector $\mathbf { y } = \mathbf { y } ( t )$ as given by Theorem9.2.Multiplying the relation(9.18) by $\begin{array} { r } { \frac { i } { \varepsilon } ( - k \cdot \mu ) \left( y ^ { - k } \right) ^ { T } } \end{array}$ and summing over $k \in \mathcal N$ ,we obtain with(9.24) that

$$
- \frac { i } { \varepsilon } \sum _ { k \in \mathcal { N } } ( k \cdot \mu ) ( y ^ { - k } ) ^ { T } \varPsi ^ { - 1 } \varPhi h ^ { - 2 } \varSigma ( h \mathscr { D } ) y ^ { k } = \mathscr { O } ( h ^ { N } ) + \mathscr { O } ( \varepsilon ^ { M - 1 } ) .
$$

The $\mathcal { O } ( \varepsilon ^ { M - 1 } )$ term is not present for $\mu \perp \mathcal { M } _ { N }$ Written in the $z$ variables,this becomes

$$
- \frac { i } { \varepsilon } \sum _ { k \in \mathcal { N } } ( k \cdot \mu ) ( z ^ { - k } ) ^ { T } \bar { \psi } ^ { - 1 } \varPhi h ^ { - 2 } L ( h D + i h k \cdot \omega ) z ^ { k } = \mathcal { O } ( h ^ { N } ) + \mathcal { O } ( \varepsilon ^ { M - 1 } ) ,
$$

Asin(9.19),theleft-hand expression turns out to be the time derivative ofa function $\boldsymbol { \mathcal { T } } _ { \mu } ^ { \ast } [ \mathbf { \boldsymbol { \mathbf { z } } } ] ( t )$ which depends on the values at $t$ of the function z and its frst $N$ derivatives:

$$
\frac { d } { d t } \mathcal { T } _ { \mu } ^ { * } [ \mathbf { z } ] ( t ) = \mathcal { O } ( h ^ { N } ) + \mathcal { O } ( \varepsilon ^ { M - 1 } ) .
$$

Together with Theorem9.2thisyields the following.

Lemma9.4.Under the assumptionsof Theorem9.2,the modulationfunctionsz satisfy

$$
\mathcal { T } _ { \mu } ^ { * } [ \mathbf { z } ] ( t ) = \mathcal { T } _ { \mu } ^ { * } [ \mathbf { z } ] ( 0 ) + \mathcal { O } ( t h ^ { N } ) + \mathcal { O } ( t \varepsilon ^ { M - 1 } )
$$

for all $\mu \in \mathbb { R } ^ { \ell }$ and for $0 \leq t \leq T .$ They satisfy

$$
{ \mathscr T } _ { \mu } ^ { * } [ { \mathbf { z } } ] ( t ) = { \mathscr T } _ { \mu } ^ { * } [ { \mathbf { z } } ] ( 0 ) + { \mathscr O } ( t h ^ { N } )
$$

$f o r \mu \perp \mathcal { M } _ { N }$ and $0 \leq t \leq T .$ Moreover,at $t = n h$

$$
T _ { \mu } ^ { * } [ \mathbf { z } ] ( t ) = I _ { \mu } ^ { * } ( x _ { n } , \dot { x } _ { n } ) + \mathcal { O } ( \varepsilon ) ,
$$

where,again with $\sigma ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) / \psi ( \xi ) ,$

$$
I _ { \mu } ^ { * } ( x , \dot { x } ) = \sum _ { j = 1 } ^ { \ell } \sigma ( \xi _ { j } ) \frac { \mu _ { j } } { \lambda _ { j } } I _ { j } ( x , \dot { x } ) .
$$

# XIII.9.4 Long-TimeNear-Conservation of Total and Oscillatory Energies

With theproof of TheoremXII.7.1,theabovetwo lemmasyield the following results fromCohen,Hairer&Lubich(2004).

Theorem9.5.Underconditions(9.9)-(9.11),thenumerical solutionobtainedby method(2.6)with(2.11） satisfies,for $H ^ { * }$ and $I _ { \mu } ^ { * }$ defined by(9.22)and(9.29),

$$
\begin{array} { r l } { { H ^ { * } ( x _ { n } , \dot { x } _ { n } ) \ = \ H ^ { * } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } } & { { } } \\ { { I _ { \mu } ^ { * } ( x _ { n } , \dot { x } _ { n } ) \ = \ } { I _ { \mu } ^ { * } ( x _ { 0 } , \dot { x } _ { 0 } ) \ + { \mathcal O } ( h ) } } & { { } } \end{array} \quad f o r 0 \leq n h \leq h ^ { - N + 1 }
$$

for $\mu \in \mathbb { R } ^ { \ell }$ with $\mu \perp { \mathcal { M } } _ { N } = \{ k \in { \mathcal { M } } : | k | \leq N \} .$ The constants symbolized by $\mathcal { O }$ areindependentof $\textit { n }$ ,h,ε, $\lambda _ { j }$ satisfying the above conditions,but depend on $N$ and theconstantsinthe conditions.

Since $\mu = \lambda$ is always orthogonal to $\mathcal { M }$ andto $\mathcal { M } _ { \mathrm { ~ N ~ } }$ ,therelation

$$
K ^ { \prime } ( x , \dot { x } ) = H ^ { * } ( x , \dot { x } ) - I _ { \lambda } ^ { * } ( x , \dot { x } )
$$

for the smooth energy(9.7) implies

$$
K ( x _ { n } , \dot { x } _ { n } ) = K ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) \quad \mathrm { ~ f o r ~ } 0 \leq n h \leq h ^ { - N + 1 } .
$$

For $\sigma ( \xi ) = 1$ (orequivalently $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) )$ themodified energies $H ^ { * }$ and $I _ { \mu } ^ { * }$ areidenticaltotheoriginalenergies $H$ and $I _ { \mu }$ of (9.2)and (9.5).Thecondition $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi )$ isknown tobe equivalent to the symplecticity of theonestep method $( x _ { n } , { \dot { x } } _ { n } ) \mapsto ( x _ { n + 1 } , { \dot { x } } _ { n + 1 } )$ ,butitsappearanceintheabovetheorem iscaused byadifferent mechanismwhichisnot inany obviouswayrelated to symplecticity.Without this condition we still have the followingresult,which also considers the long-time near-conservation of the individual oscillatory energies $I _ { j }$ for $j = 1 , \ldots , \ell ,$

Theorem9.6.Underconditions(9.9)-(9.11),thenumericalsolutionobtained by method(2.6)with(2.11) satisfies

$$
\begin{array} { l } { H ( x _ { n } , \dot { x } _ { n } ) ~ = ~ H ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } \\ { I _ { j } ( x _ { n } , \dot { x } _ { n } ) ~ = ~ I _ { j } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ) } \end{array} \quad f o r ~ 0 \le n h \le h \cdot \operatorname* { m i n } ( \varepsilon ^ { - M + 1 } , h ^ { - N } )
$$

for $j = 1 , \ldots , \ell ,$ with $M = \operatorname* { m i n } \{ | k | : 0 \neq k \in \mathcal { M } \}$ .The constants symbolized by $\mathcal { O }$ areindependentof $n _ { i }$ $h$ , $\boldsymbol { \mathrm { \Sigma } }$ ， $\lambda _ { j }$ satisfying theaboveconditions,but depend on $N$ andtheconstants inthe conditions.

For the non-resonant case $M = \{ 0 \}$ we have $M = \infty$ and hence the length of theinterval with energy conservation is only restricted by(9.iO).Notice that always $M \geq 3$ ,and $M = 3$ only in the case of a 1:2 resonance among the $\lambda _ { j }$ Fora1:3 resonance we have $M = 4$ and inall othercases $M \geq 5$

Explanation of the Numerical Experiment of Sect.XIII.9.1.All numerical methodsinFigs.9.2-9.4 satisfythe conditions of Theorems 9.6and 9.5 for the step sizes considered.

InFig.9.2 we have the(symplectic）method(2.6)with $\phi ( \xi ) = 1$ and $\psi ( \xi ) = $ $\mathrm { s i n c } ( \xi )$ which has $\sigma ( \xi ) = 1$ ,sothat $H$ and $H ^ { * }$ ,and $I _ { \mu }$ and $I _ { \mu } ^ { * }$ coincide.For all stepsizes,the oscillatory energy $I _ { 2 }$ corresponding to the non-resonant frequency $\sqrt { 2 } \omega$ and the sum $I _ { 1 } + I _ { 3 }$ arewell conserved on long time intervals,in accordance with Theorem 9.5.The individual energies $I _ { 1 }$ and $\boldsymbol { { I } } _ { 3 }$ corresponding to the resonant frequencies $\omega = 1 / \varepsilon$ and $2 / \varepsilon$ arenot preserved on the time scale considered here, cf.Fig.9.1.In fact,Theorem 9.6 here yields onlya time scale $\mathcal { O } ( h \varepsilon ^ { - 2 } )$ .

In Fig.9.3we use the method with $\phi ( \xi ) = 1$ and $\psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \xi / 2 )$ ,forwhich $\sigma ( \xi )$ is not identical to 1,and hence $H$ and $H ^ { \ast }$ ,and $I _ { \mu }$ and $I _ { \mu } ^ { * }$ do not coincide. The oscilatory energy ${ \cal I } _ { 2 } = \sigma _ { 2 } ^ { - 1 } { \cal I } _ { \mu } ^ { * }$ with $\mu \equiv ( 0 , 1 , 0 ) \perp \mathcal { M }$ ,which corresponds to thenon-resonant frequency $\sqrt { 2 } \omega$ ,isapproximatelyconserved over long times. Since Theorem 9.5only states that the modified energiesare well preserved,it is not surprising that neither $I _ { 1 } + I _ { 3 }$ nor the original total energy $H$ （not shown in the figure）are conserved.The modified energies $H ^ { * }$ and $\sigma _ { 1 } I _ { 1 } + \sigma _ { 3 } I _ { 3 }$ （not shown）are indeedwell conserved,and so is the smooth energy $\boldsymbol { K }$ inagreement with(9.30).

Figure 9.4 shows theresult for the(symplectic)method with $\phi ( \xi ) = \underline { { { \mathrm { s i n c } } } } ( \xi )$ and $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi )$ Since $\sigma ( \xi ) = 1$ ,theoscillatory energy $I _ { 2 }$ for $\sqrt { 2 } \omega$ and also $I _ { 1 } + I _ { 3 }$ arewell conserved,inagreement with Theorem 9.5.However,the energy exchange between the resonant frequencies isnot correctlyreproduced.This behaviourisnot explained by Theorems9.5and 9.6,but itcorrespondstothe analysis inSect.XIII.4.2 which,for the single-frequency case,explains the incorrect energy exchange of methods that do not satisfy $\psi ( \xi ) \phi ( \xi ) = \mathrm { s i n c } ( \xi )$ (and thus,of all symplectic methods(2.7)-(2.10),with the exception of the abovemethod with $\phi ( \xi ) = 1$ and $\psi ( \xi ) = \mathrm { s i n c } ( \xi ) )$ .Thatanalysis could be extended to the multi-frequency case considered here.

Weremark thatthe techniques of Sects.XIII.9.2and XII.9.3 canalso beused to study the energy errorof the Stormer-Verlet method,as in Sect.XII.8;see Theorem5.1in Cohen,Hairer&Lubich（2Oo4）.Themodulated Fourier expansion of theexact solution yieldsresults on the near-preservation of the oscillatory energies alonga bounded exact solution:underthe energy bound(9.9)and the non-resonance condition

$$
| k \cdot \lambda | \geq c { \sqrt { \varepsilon } } \quad { \mathrm { f o r ~ } } k \in \mathbb { Z } ^ { \ell } \setminus { \mathcal { M } } { \mathrm { ~ w i t h ~ } } | k | \leq N
$$

wehave(seeTheorem6.1inCohen,Hairer&Lubich2004)

$$
I _ { \mu } \bigl ( x ( t ) , \dot { x } ( t ) \bigr ) = I _ { \mu } \bigl ( x ( 0 ) , \dot { x } ( 0 ) \bigr ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { f o r ~ } 0 \leq t \leq \varepsilon ^ { - N + 1 }
$$

for $\mu \in \mathbb { R } ^ { \ell }$ with $\mu \perp \mathcal { M } _ { N } = \{ k \in \mathcal { M } : | k | \leq N \}$ We further have

$$
I _ { j } \big ( x ( t ) , \dot { x } ( t ) \big ) = I _ { j } \big ( x ( 0 ) , \dot { x } ( 0 ) \big ) + \mathcal { O } ( \varepsilon ) \quad \mathrm { ~ f o r ~ } 0 \leq t \leq \varepsilon \cdot \operatorname* { m i n } ( \varepsilon ^ { - M + 1 } , \varepsilon ^ { - N } ( t ) ) ,
$$

for $j = 1 , \ldots , \ell$ with $M = \operatorname* { m i n } \{ | k | : 0 \neq k \in \mathcal { M } \} .$

# XIII.10 Systemswith Non-Constant Mass Matrix

The high frequencies of the linearized differential equation remain constant up to small deviations for mechanical systemswith a Hamiltonian of the form

$$
H ( p , q ) = { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q ) ^ { - 1 } p _ { 0 } + { \frac { 1 } { 2 } } p _ { 1 } ^ { T } M _ { 1 } ^ { - 1 } p _ { 1 } + { \frac { 1 } { 2 } } p ^ { T } R ( q ) p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q _ { 1 } ^ { T } A _ { 1 } q _ { 1 } + U ( p _ { 0 } - p _ { 0 } )
$$

with a symmetric positive definite matrix $M _ { 0 } ( q )$ ,constant symmetric positive definitematrices $M _ { 1 }$ and $A _ { 1 }$ ,asymmetric matrix $R ( q )$ with

$$
R ( q _ { 0 } , 0 ) = 0 ,
$$

and a potential $U ( q )$ .All the functionsare assumed to depend smoothly on $q$ . Bounded energy then requires $q _ { 1 } = \mathcal { O } ( \varepsilon )$ ,sothat $p ^ { T } R ( q ) p = \mathcal { O } ( \varepsilon )$ but thederivative of this term with respect to $q _ { 1 }$ is $\mathcal { O } ( 1 )$ ,

Asin(9.1),we may assume,afteran appropriate canonical linear transformation based ona Cholesky decomposition of the mass matrix and a diagonalization of the resulting stiffness matrix,that the Hamiltonian is of the form

$$
H ( p , q ) = \frac { 1 } { 2 } p _ { 0 } ^ { T } M _ { 0 } ( q ) ^ { - 1 } p _ { 0 } + \frac { 1 } { 2 } \sum _ { j = 1 } ^ { \ell } \biggl ( \| p _ { j } \| ^ { 2 } + \frac { \lambda _ { j } ^ { 2 } } { \varepsilon ^ { 2 } } \| q _ { j } \| ^ { 2 } \biggr ) + \frac { 1 } { 2 } p ^ { T } R ( q ) p + U ( p ) ,
$$

with distinct, constant $\lambda _ { j } \geq 1$

The necessity for such a generalization results from the fact that oscillatory mechanical systems with near-constant frequencies in2or3space dimensions typically cannot be put in theform(9.1),but in the more general form(10.1) or(10.2).

Example 10.1 (Stiff Spring Pendulum).The motion of a mass point (of mass 1) hanging on a massless stiff spring(with spring constant $1 / \varepsilon ^ { 2 }$ ）isdescribed inpolar coordinates $x _ { 1 } = r \sin \varphi$ , $x _ { 2 } = - r \cos \varphi$ by theLagrangianwith kinetic energy $T = { \textstyle \frac { 1 } { 2 } } ( \dot { x } _ { 1 } ^ { 2 } + \dot { x } _ { 2 } ^ { 2 } ) = { \textstyle \frac { 1 } { 2 } } ( \dot { r } ^ { 2 } + r ^ { 2 } \dot { \varphi } ^ { 2 } )$ and potential energy $\begin{array} { r } { U = \frac { 1 } { 2 \epsilon ^ { 2 } } \left( r - 1 \right) ^ { 2 } - r \cos \varphi } \end{array}$ With the coordinates $q _ { 0 } = \varphi$ , $q _ { 1 } = r - 1$ and theconjugate momenta $p _ { i } = \partial T / \partial q _ { i }$ this gives the Hamiltonian

$$
H ( p , q ) = { \textstyle { \frac { 1 } { 2 } } } \big ( ( 1 + q _ { 1 } ) ^ { - 2 } p _ { 0 } ^ { 2 } + p _ { 1 } ^ { 2 } \big ) + { \textstyle { \frac { 1 } { 2 \varepsilon ^ { 2 } } } } q _ { 1 } ^ { 2 } - ( 1 + q _ { 1 } ) \cos q _ { 0 } ,
$$

which is of the form (10.2).

Numerical methods for systems(10.2)are studied by Cohen (20o5).He splits the small term $\scriptstyle { \frac { 1 } { 2 } } p ^ { T } R ( q ) p$ from the principal terms of the Hamiltonianand proposes the following method,where

$$
K ( p _ { 0 } , q ) = { \frac { 1 } { 2 } } p _ { 0 } ^ { T } M _ { 0 } ( q ) ^ { - 1 } p _ { 0 } + U ( q ) .
$$

Algorithm10.2.1.A half-stepwiththe symplectic Eulermethodapplied tothe systemwith Hamiltonian ${ \scriptstyle { \frac { 1 } { 2 } } } p ^ { T } R ( q ) p$ gives

$$
\begin{array} { r c l } { { { \widehat { p } } ^ { n } } } & { { = } } & { { p ^ { n } - \displaystyle \frac { h } { 2 } \nabla _ { q } \left( \frac { 1 } { 2 } ( { \widehat { p } } ^ { n } ) ^ { T } R ( q ^ { n } ) { \widehat { p } } ^ { n } \right) } } \\ { { { \widehat { q } } ^ { n } } } & { { = } } & { { q ^ { n } + \displaystyle \frac { h } { 2 } R ( q ^ { n } ) { \widehat { p } } ^ { n } . } } \end{array}
$$

2.Treating the oscillatory components ofthe variables $p$ andqwith a trigonometricmethod(2.7)-(2.8)and the slowcomponentswiththe Stormer-Verlet scheme yields（for $j = 1 , \ldots , \ell$ andwith $\omega _ { j } = \lambda _ { j } / \varepsilon$ and $\xi _ { j } = h \omega _ { j }$ )

$$
\begin{array} { r l r } { v _ { 0 } ^ { n + 1 / 2 } } & { = } & { \widehat { p } _ { 0 } ^ { n } - \frac { h } { 2 } \nabla _ { q _ { 0 } } K ( p _ { 0 } ^ { n + 1 / 2 } , \widehat { \phi } \widehat { q } ^ { n } ) } \\ { \widehat { q } _ { 0 } ^ { n + 1 } } & { = } & { \widehat { q } _ { 0 } ^ { n } + \frac { h } { 2 } \bigg ( \nabla _ { p _ { 1 } } K ( p _ { 0 } ^ { n + 1 / 2 } , \phi \widehat { q } ^ { n } ) + \nabla _ { p _ { 0 } } K ( p _ { 0 } ^ { n + 1 / 2 } , \widehat { \phi } \widehat { q } ^ { n + 1 } ) \bigg ) } \\ { \widehat { q } _ { j } ^ { n + 1 } } & { = } & { \cos ( \xi _ { j } ) \widehat { q } _ { j } ^ { n } + \omega _ { j } ^ { - 1 } \sin ( \xi _ { j } ) \widehat { p } _ { j } ^ { n } - \frac { h ^ { 2 } } { 2 } \psi ( \xi _ { j } ) \nabla _ { q _ { j } } K ( p _ { 0 } ^ { n + 1 / 2 } , \widehat { \phi } \widehat { q } ^ { n } ) } \\ { \widehat { p } _ { j } ^ { n + 1 } } & { = } & { - \omega _ { j } \sin ( \xi _ { j } ) \widehat { q } _ { j } ^ { n } + \cos ( \xi _ { j } ) \widehat { p } _ { j } ^ { n } - \frac { h } { 2 } \bigg ( \psi _ { 0 } ( \xi _ { j } ) \nabla _ { q _ { j } } K ( p _ { 0 } ^ { n + 1 / 2 } , \widehat { \phi } \widehat { q } ^ { n } ) } \\ & { } & { + \psi _ { 1 } ( \xi _ { j } ) \nabla _ { q _ { 0 } } K ( p _ { 0 } ^ { n + 1 / 2 } , \phi \widehat { q } ^ { n + 1 } ) \bigg ) , } \\ { \widehat { p } _ { 0 } ^ { n + 1 } } & { = } & { p _ { 0 } ^ { n + 1 / 2 } - \frac { h } { 2 } \nabla _ { q _ { 0 } } K ( p _ { 0 } ^ { n + 1 / 2 } , \widehat { \phi } \widehat { q } ^ { n + 1 } ) \qquad \quad ( 1 0 . } \end{array}
$$

where $\Phi = \phi ( h \varOmega )$ with $\Omega = \mathrm { d i a g } ( \omega _ { j } I )$

3.Ahalf-stepwith theadjoint symplectic Euler methodappliedto the system with Hamiltonian $\scriptstyle { \frac { 1 } { 2 } } p ^ { 1 } R ( q ) p$ gives

$$
\begin{array} { r c l } { { p ^ { n + 1 } } } & { { = } } & { { \displaystyle \widehat { p } ^ { n + 1 } - \frac { h } { 2 } \nabla _ { q } \left( \frac { 1 } { 2 } ( \widehat { p } ^ { n + 1 } ) ^ { T } R ( q ^ { n + 1 } ) \widehat { p } ^ { n + 1 } \right) } } \\ { { } } & { { } } & { { } } \\ { { q ^ { n + 1 } } } & { { = } } & { { \displaystyle \widehat { q } ^ { n + 1 } + \frac { h } { 2 } R ( q ^ { n + 1 } ) \widehat { p } ^ { n + 1 } . } } \end{array}
$$

The filter functions $\psi , \psi _ { 0 } , \psi _ { 1 } , \phi$ areagain real-valued functions with $\psi ( 0 ) =$ $\psi ( 0 ) = \psi ( 0 ) = \phi ( 0 ) = 1$ that satisfy (2.9).The method is still symplectic if and only if(2.10) holds.Note that Step2.of thealgorithm is explicit if $M _ { 0 } ( q )$ does not depend on $q _ { 0 }$

Cohen (2004,2005) studies the modulated Fourier expansion of this method and showsthat the long-time near-conservation of total and oscillatory energies as given byTheorem9.6remainsvalidalso inthismore general situation.

Example 10.3(Triatomic Molecule).The motion of anear-rigid triatomic molecule is described bya Hamiltonian system witha Hamiltonian (1O.2).For simplicity wefix theposition of the central atom.We then have two stiff-spring pendulums strongly coupled byanother spring.With anglesand distances as shown inFig.10.1, weuse the position coordinates $\varphi _ { 1 } , q _ { 1 } = r _ { 1 } - 1 , \varphi _ { 2 } , q _ { 2 } = r _ { 2 } - 1$ with the conjugate momenta $\pi _ { 1 } , p _ { 1 } , \pi _ { 2 } , p _ { 2 }$ ,respectively.TheHamiltonianthenreads

$$
\begin{array} { r c l } { { H ( \pi , p , \varphi , q ) } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \Big ( ( 1 + q _ { 1 } ) ^ { - 2 } \pi _ { 1 } ^ { 2 } + p _ { 1 } ^ { 2 } + ( 1 + q _ { 2 } ) ^ { - 2 } \pi _ { 2 } ^ { 2 } + p _ { 2 } ^ { 2 } \Big ) } } \\ { { } } & { { } } & { { \displaystyle + \frac { 1 } { 2 \varepsilon ^ { 2 } } \Big ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + \frac { \alpha ^ { 2 } } { 2 } ( \varphi _ { 2 } - \varphi _ { 1 } ) ^ { 2 } \Big ) + U ( \varphi , q ) } } \end{array}
$$

with a spring constant $\scriptstyle { \frac { 1 } { 2 } } \alpha ^ { 2 } / \varepsilon ^ { 2 }$ for connecting the two pendulums and an external potential $U$ .With the canonical change of variables

$$
\left( { \begin{array} { l } { q _ { 3 } } \\ { q _ { 0 } } \end{array} } \right) = { \frac { 1 } { \sqrt { 2 } } } \left( { \begin{array} { l l } { - 1 } & { 1 } \\ { 1 } & { 1 } \end{array} } \right) \left( { \begin{array} { l } { \varphi _ { 1 } } \\ { \varphi _ { 2 } } \end{array} } \right) , \left( { \begin{array} { l } { \pi _ { 1 } } \\ { \pi _ { 2 } } \end{array} } \right) = { \frac { 1 } { \sqrt { 2 } } } \left( { \begin{array} { l l } { - 1 } & { 1 } \\ { 1 } & { 1 } \end{array} } \right) \left( { \begin{array} { l } { p _ { 3 } } \\ { p _ { 0 } } \end{array} } \right) ,
$$

the Hamiltonian takes the form(10.2)：

$$
\begin{array} { l c l } { { H ( p , q ) } } & { { = } } & { { \frac { 1 } { 2 } ( p _ { 0 } ^ { 2 } + p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } + p _ { 3 } ^ { 2 } ) + \frac { 1 } { 2 \varepsilon ^ { 2 } } ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } + \alpha ^ { 2 } q _ { 3 } ^ { 2 } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { + p ^ { T } R ( q ) p + \widehat U ( q ) } } \end{array}
$$

with

$$
p ^ { T } R ( q ) p = - \frac { 1 } { 4 } \frac { 2 q _ { 2 } + q _ { 2 } ^ { 2 } } { ( 1 + q _ { 2 } ) ^ { 2 } } \left( p _ { 0 } - p _ { 3 } \right) ^ { 2 } - \frac { 1 } { 4 } \frac { 2 q _ { 1 } + q _ { 1 } ^ { 2 } } { ( 1 + q _ { 1 } ) ^ { 2 } } \left( p _ { 0 } + p _ { 3 } \right) ^ { 2 }
$$

and $\hat { U } ( q ) = U ( \varphi _ { 1 } , \varphi _ { 2 } , q _ { 1 } , q _ { 2 } )$

Forthe water molecule theratio between the frequencies of the bond angle and the bond lengths is $\alpha \approx 0 . 2$ ,according to somepopular models.Inour numerical experiments,we observed good conservation of all the oscillatory energies and the totalenergy.More interesting phenomena occur ina near-resonance situation.We consider $\alpha = 0 . 4 9$ and $\varepsilon = 0 . 0 1$ ,noexteriorpotential （ $U = 0$ ),and initial values $q ( 0 ) = ( 0 , \varepsilon / 2 , \varepsilon , \alpha / \varepsilon )$ and $p ( 0 ) \ = \ ( 1 . 1 , 0 . 2 , - 0 . 8 , 1 . 3 )$ InFig.10.2weapply themethod of Algorithm 10.2with step sizes $h = 0 . 5 \varepsilon$ and $h = 2 \varepsilon$ andobtain numerical results that agree very well with asolution obtained with very smallstep sizes.For comparison we showinFig.1O.3 theresults of theStormer-Verlet method with step sizes $h = 0 . 2 \varepsilon$ and $h = 0 . 5 \varepsilon$ ,forwhich the energy exchange is not correct.For thereasonexplainedinSect.VI.3,(3.2)-(3.3),bothmethodsare fully explicit for this problem.

![](images/71a81ecfd4b2eb906b24374c07ec858b427184d0486facc1c17a0fc82b4ac5cd.jpg)  
Fig.10.1.Water moleculeand reference configurationas gray shadow

![](images/2c14fd1ec7e0b15f2b78f6cca0ecd06d7ec43bafc7321f470f33fd4663637757.jpg)  
Fig.10.2.Oscillatory energiesand total energy for the method of Algorithm 10.2

![](images/e9cf0a8929e86bb118f72067864da452f84d298769d2ba138c190d74e15245b1.jpg)  
Fig.10.3.Oscillatory energiesand total energy for the Stormer-Verlet method

# XIII.11 Exercises

1.Show that the impulse method (with exact solution of the fast system)reduces toDeuflhard'smethod in the case of a quadratic potential $\begin{array} { r } { W ( q ) = \frac { 1 } { 2 } q ^ { T } A q } \end{array}$ .

2.Show that amethod(2.7)-(2.8)satisfying (2.9)issymplectic if and onlyif

$$
\psi ( \xi ) = \mathrm { s i n c } ( \xi ) \phi ( \xi ) \qquad \mathrm { f o r } \quad \xi = h \omega .
$$

3.The change of coordinates $x _ { n } ~ = ~ \chi ( h \Omega ) z _ { n }$ transforms(2.7)-(2.8） into a method of identical formwith $\phi , \psi , \psi _ { 0 } , \psi _ { 1 }$ replaced by $\chi \phi , \chi ^ { - 1 } \psi , \chi ^ { - 1 } \psi _ { 0 }$ , $\chi ^ { - 1 } \psi _ { 1 }$ Prove that,for $h \omega$ satisfying $\mathrm { s i n c } ( h \omega ) \phi ( h \omega ) / \psi ( h \omega ) > 0$ itispossible to find $\chi ( h \omega )$ such that the transformed method is symplectic.

4.Prove that for infinitely differentiable functions $g ( t )$ the solution of ${ \ddot { x } } + \omega ^ { 2 } x =$ $g ( t )$ can be written as

$$
x ( t ) = y ( t ) + \cos ( \omega t ) u ( t ) + \sin ( \omega t ) v ( t ) ,
$$

where $y ( t )$ , $u ( t )$ , $v ( t )$ aregiven by asymptotic expansions in powers of $\omega ^ { - 1 }$ . HintUse the variation-of-constants formulaand applyrepeated partial integration.

5.Show that the recurrence relation $e _ { n + 1 } - 2 \cos ( h \Omega ) e _ { n } + e _ { n - 1 } = b _ { n }$ has the solution

$$
e _ { n + 1 } = - W _ { n - 1 } e _ { 0 } + W _ { n } e _ { 1 } + \sum _ { j = 1 } ^ { n } W _ { n - j } \ : b _ { j }
$$

with $W _ { n } \ = \ \sin ( h \Omega ) ^ { - 1 } \sin \big ( ( n + 1 ) h \Omega \big )$ (or theappropriate limit when $\sin ( h \Omega )$ isnot invertible).

6.Consider a Hamiltonian $H ( p _ { R } , p _ { I } , q _ { R } , q _ { I } )$ andlet

$$
{ \mathcal { H } } ( p , q ) = 2 H ( p _ { R } , p _ { I } , q _ { R } , q _ { I } )
$$

for $p = p _ { R } + 2 p _ { I }$ , $q = q _ { R } + \ i q _ { I }$ Prove that in the new variables $p , q$ the Hamiltonian system becomes

$$
\dot { p } = - \frac { \partial \mathcal { H } } { \partial \overline { { { q } } } } ( p , q ) , \qquad \dot { q } = \frac { \partial \mathcal { H } } { \partial \overline { { { p } } } } ( p , q ) .
$$

7.Prove the following refinement of Theorem6.3:along the solution $x ( t )$ of(2.1）, themodified oscillatory energy $J ( x , \dot { x } ) = I ( x , \dot { x } ) - x _ { 1 } ^ { T } g _ { 1 } ( x )$ satisfies

$$
J ( x ( t ) , \dot { x } ( t ) ) = J ( x ( 0 ) , \dot { x } ( 0 ) ) + \mathcal { O } ( \omega ^ { - 2 } ) + \mathcal { O } ( t \omega ^ { - N } ) .
$$

8.Define $\begin{array} { r } { \dot { H } ( x , \dot { x } ) = H ( x , \dot { x } ) - \rho x _ { 1 } ^ { T } g _ { 1 } ( x ) } \end{array}$ , $J ( x , \dot { x } ) = J ( x , \dot { x } ) - \rho x _ { 1 } ^ { T } g _ { 1 } ( x )$ with $J ( x , { \dot { x } } )$ of the previous exercise and with

$$
\rho = \frac { \psi ( h \omega ) } { \mathrm { s i n c } ^ { 2 } ( \frac { 1 } { 2 } h \omega ) } - 1 .
$$

In the situation of Theorem7.1,show that

$$
\begin{array} { r c l } { { \widehat { H } ( x _ { n } , \dot { x } _ { n } ) } } & { { = } } & { { \widehat { H } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ^ { 2 } ) } } \\ { { \widehat { J } ( x _ { n } , \dot { x } _ { n } ) } } & { { = } } & { { \widehat { J } ( x _ { 0 } , \dot { x } _ { 0 } ) + { \mathcal O } ( h ^ { 2 } ) } } \end{array} \quad \mathrm { ~ f o r ~ } 0 \leq n h \leq h ^ { - N + 1 } .
$$

Noticethat the total energy $H ( x _ { n } , { \dot { x } } _ { n } )$ and themodified oscillatory energy $J ( x _ { n } , \dot { x } _ { n } )$ are conserved up to $\mathcal { O } ( h ^ { 2 } )$ if $\rho = 0$ ,i.e.,if $\psi ( \xi ) = \mathrm { s i n c } ^ { 2 } ( \textstyle { \frac { 1 } { 2 } } \xi ) .$ This explains the excellent energy conservation ofmethods(A)and(D)in Figure 2.5 away fromresonances.

9.Generalizing theanalysis of Sect.XII.8,study the energy behaviour of the impulseoraveraged-forcemultiple time-steppingmethod of Sect.VII.4witha fixed number $N$ ofStormer-Verlet substeps per step,when the method isapplied to the model problemwith $h \omega$ bounded away from zero.

# Chapter XIV. Oscillatory Differential Equations with Varying High Frequencies

Newaspects come into play when the high frequencies in an oscillatory system and their associated eigenspaces do not remain nearly constant,as in theprevious chapter,but change with time or depend onthe solution.Webegin by studying lineardifferential equations withatime-dependent skew-hermitianmatrix and then turnto nonlinear oscillatory mechanical systems with time-or solution-dependent frequencies.Our analysis uses canonical coordinate transforms that separate slow and fast motions and relate the fast oscillations to the skew-hermitian linear case.For thenumerical treatment we consider suitably constructed long-time-stepmethods ("adiabatic integrators")and multiple time-stepping methods.

# XIV.1LinearSystems with Time-Dependent Skew-Hermitian Matrix

Weconsider first-order lineardifferential equationswith a skew-hermitian matrix thatchanges slowly compared to the rapid oscillations in the solution,aproblem thathas attracted much attention in quantummechanics.We present asuitableclass ofnumerical methods,termed adiabatic integrators,which can take time steps that aresubstantially larger than the almost-periods of the oscillations.

# XIV.1.1 Adiabatic Transformationand AdiabaticInvariants

It comes from the greek aδLαβaTlxos,"which cannot be crossed".

..wearriveby analogyto the“adiabaticprinciple”used in Quantum andthen Classical Mechanics.Itis based upon the fact that the harmonic oscillator (and other simpledynamical systemsas itwas found later) submittedto slow variations of its parametersmodifies itsenergybut keeps itsaction(energydivided by frequency) constant.

As wecan see,the path from the word“adiabatic”used in thermodynamicsto the above"adiabatic principle”is tortuous and our greek colleagues arecertainlypuzzled by sentences such as“the changes in theadiabatic invariant due to[..] crossing”whichwe shall use later.

(J.Henrard 1993)

$$
\dot { y } ( t ) = \frac { 1 } { \varepsilon } Z ( t ) y ( t ) ,
$$

where $Z ( t )$ isareal skew-symmetric(or complex skew-hermitian）matrix-valued function with time derivatives bounded independently of the small parameter $\varepsilon$ . In quantum dynamics such equations arise with $Z ( t ) = - i H ( t )$ ,where thereal symmetric（or hermitian）matrix $H ( t )$ represents the quantum Hamiltonian operatorina discrete-level Schrodinger equation.We will also encounter real equations ofthis type in thetreatment ofoscillatory classical mechanical systemswith timedependent frequencies.Solutions oscillate with almost-periods $\sim \varepsilon$ ,while the systemmatrix changes on a slower time scale $\sim 1$

Transforming the Problem.We begin by looking fora time-dependent linear transformation

$$
\eta ( t ) = T _ { \varepsilon } ( t ) y ( t ) ,
$$

taking the system to the form

$$
\Dot { \eta } ( t ) = S _ { \varepsilon } ( t ) \eta ( t ) \quad \mathrm { ~ w i t h ~ } \quad S _ { \varepsilon } = \Dot { T } _ { \varepsilon } T _ { \varepsilon } ^ { - 1 } \Lt + \frac { 1 } { \varepsilon } T _ { \varepsilon } Z T _ { \varepsilon } ^ { - 1 } ,
$$

which is chosen such that $S _ { \varepsilon } ( t )$ is of smaller norm than the matrix $\scriptstyle { \frac { 1 } { \varepsilon } } Z ( t )$ of(1.1).

Remark1.1.A first ideaisto freeze $\boldsymbol { Z } ( t ) \approx \boldsymbol { Z } _ { * }$ over a time step and to choose the transformation

$$
\Gamma _ { \varepsilon } ( t ) = \exp \left( - \frac { t } { \varepsilon } Z _ { * } \right) \mathrm { y i e l d i n g } S _ { \varepsilon } ( t ) = \frac { 1 } { \varepsilon } \exp \left( - \frac { t } { \varepsilon } Z _ { * } \right) \left( Z ( t ) - Z _ { * } \right) \exp \left( \frac { t } { \varepsilon } Z _ { * } \right) ,
$$

This matrix function $S _ { \varepsilon } ( t )$ is highly oscillatoryand bounded in norm by $\mathcal { O } ( h / \varepsilon )$ for $| t - t _ { 0 } | \leq h$ ,if $Z _ { * } = Z ( t _ { 0 } + h / 2 ) ,$ Numerical integrators based on this transformationare given byLawson（1967）and more recentlybyHochbruck&Lubich (1999b), Iserles (2002,2004),and Degani & Schiff(2003).Reasonable accuracy still requires step sizes $h = { \mathcal { O } } ( \varepsilon )$ ingeneral; see also Exercise 3.In the above papers this transfomation has,however,been put to good use in situationswhere the timederivatives of thematrix inthedifferential equation havemuch smaller norm than the matrix itself.

Adiabatic Transformation.Inorder to obtainadifferential equation(1.3）with a uniformly bounded matrix $S _ { \varepsilon } ( t )$ we diagonalize

$$
Z ( t ) = U ( t ) i \Lambda ( t ) U ( t ) ^ { * }
$$

withareal diagonal matrix $\begin{array} { r } { \Lambda ( t ) = \mathrm { d i a g } \left( \lambda _ { j } ( t ) \right) } \end{array}$ and aunitary matrix $U ( t ) =$ $( u _ { 1 } ( t ) , \ldots , u _ { n } ( t ) )$ of eigenvectors depending smoothly on $t$ (possibly except where eigenvalues cross).We define $\eta ( t )$ bytheunitaryadiabatic transformation

$$
\eta ( t ) = \exp \left( - \frac { i } { \varepsilon } \Phi ( t ) \right) U ( t ) ^ { * } y ( t ) \quad \mathrm { w i t h } \quad \varPhi ( t ) = \mathrm { d i a g } \left( \phi _ { j } ( t ) \right) = \int _ { 0 } ^ { t } { \varLambda ( s ) d s } ,
$$

which represents the solution ina rotating frame of eigenvectors.Each component of $\eta ( t )$ isa coefficient in the eigenbasis representation of $y ( t )$ rotated inthecomplexplane by the negative phase.Such transformations have been in use in quantummechanics since the work of Born&Fock（1928）onadiabatic invariantsin Schrodinger equations,asdiscussed in the next paragraph.The transformation(1.4) yieldsa differential equation where the $\circeq$ -independent skew-hermitianmatrix

$$
W ( t ) = \dot { U } ( t ) ^ { * } U ( t )
$$

isframed by oscillatory diagonal matrices:

$$
\dot { \eta } ( t ) = \exp \left( - \frac { i } { \varepsilon } \varPhi ( t ) \right) W ( t ) \exp \left( \frac { i } { \varepsilon } \varPhi ( t ) \right) \eta ( t ) .
$$

Numerical integrators for（1.1） based on the transformation to the differential equation(1.5）with bounded,though highlyoscillatoryright-hand side,are given by Jahnke&Lubich（2003)andJahnke(2004a);see Sect.XIV.1.2.

Adiabatic Invariants.Possibly afteratime-dependent rephasing of the eigenvectors, $u _ { k } ( t ) \longrightarrow e ^ { i \alpha _ { k } ( t ) } u _ { k } ( t )$ ,wecan assume that ${ \dot { u } } _ { k } ( t )$ isorthogonal to $u _ { k } ( t )$ for all $t$ (Thisisautomatically satisfiedif $U ( t )$ isareal orthogonal matrix,asis the case for $Z ( t ) = - i H ( t )$ withareal symmetric matrix $H ( t )$ ）Wethen have the matrix $W = ( w _ { \jmath k } ) = ( \dot { u } _ { \jmath } ^ { * } u _ { k } )$ with zero diagonal.

After integration of both sides of the differential equation(1.5） from O to $t$ , partial integration of the terms on theright-hand sideyields for $j \neq k$ (terms for $j = k$ do not appear since $w _ { j j } = 0$ ）

$$
\begin{array} { r l } & { \displaystyle \int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \phi _ { k } ( s ) \bigr ) \Bigr ) w _ { j k } ( s ) \eta _ { k } ( s ) d s } \\ & { \displaystyle = i \varepsilon \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \bar { \phi } _ { k } ( s ) \bigr ) \Bigr ) \frac { w _ { j k } ( s ) \eta _ { k } ( s ) } { \lambda _ { j } ( s ) - \lambda _ { k } ( s ) } \Bigr | _ { 0 } ^ { t } } \\ & { \quad \displaystyle - i \varepsilon \int _ { 0 } ^ { t } \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } ( s ) - \phi _ { k } ( s ) \bigr ) \Bigr ) \frac { d } { d s } \frac { w _ { j k } ( s ) \eta _ { k } ( s ) } { \lambda _ { j } ( s ) - \lambda _ { k } ( s ) } d s . } \end{array}
$$

At this point, suppose that the eigenvalues $\lambda _ { j } ( t )$ are,for all $t$ ,separated fromeach other byapositivedistance $\delta$ independent of $\varepsilon$

$$
| \lambda _ { j } ( t ) - \lambda _ { k } ( t ) | \geq \delta \qquad { \mathrm { f o r ~ a l l ~ } } j \neq k .
$$

Then thereciprocals of theirdifferences and the coupling matrix $W ( t )$ arebounded independentlyof $\varepsilon$ ,asaretheir derivatives.Togetherwith the boundedness of $\dot { \eta }$ as implied by(1.5),this shows

$$
\eta ( t ) = \eta ( 0 ) + O ( \varepsilon ) \quad \mathrm { ~ f o r ~ } t \leq \mathrm { C o n s t } .
$$

Thisresultisaversion of the quantum-adiabatic theorem of Born& Fock（1928) which states that the actions $| \eta _ { j } | ^ { 2 }$ (the energy in the $j$ thstate, $\langle \eta _ { j } u _ { j } , H \eta _ { j } u _ { j } \rangle =$ $\lambda _ { j } | \eta _ { j } | ^ { 2 }$ ,dividedbythe frequency $\lambda _ { j }$ ）remain approximately constant for times $t =$ $\mathcal { O } ( 1 )$ .Such functions $I ( y , t )$ that satisfy $I ( y ( t ) , t ) = I ( y ( 0 ) , 0 ) + \mathcal { O } ( \varepsilon )$ for $t =$ $\mathcal { O } ( 1 )$ along every $\mathcal { O } ( 1 )$ -bounded solution $y ( t )$ ofthe differential equation,arecalled adiabatic invariants.

Super-Adiabatic Transformations.Adiabatic invariants are obtained over longer time scales byrefining the transformation;see Lenard (1959)and Garrido (1964). Herewe show that the transformation matrix $T _ { \epsilon }$ of（1.2） can be constructed such that thematrix $S _ { \epsilon }$ inthe transformed differential equation(1.3)is of size $\mathcal { O } ( \varepsilon ^ { N } )$ . Letusmake the ansatz ofaunitary transformation matrix

$$
T _ { \varepsilon } ^ { ( N ) } = \exp \Bigl ( - \frac { i } { \varepsilon } \Phi \Bigr ) \exp ( - i \Phi _ { 1 } ) \exp ( \varepsilon X _ { 1 } ) \ldots \exp ( - i \varepsilon ^ { N - 1 } \Phi _ { N } ) \exp ( \varepsilon ^ { N } X _ { N } )
$$

withreal diagonal matrices $\varPhi _ { n } ( t )$ and complex skew-hermitian matrices $X _ { n } ( t )$ We find that $\begin{array} { r } { S _ { \varepsilon } = \frac { 1 } { \varepsilon } T _ { \varepsilon } Z T _ { \varepsilon } ^ { * } + T _ { \varepsilon } T _ { \varepsilon } ^ { * } } \end{array}$ is $\mathcal { O } ( \varepsilon )$ if and only if $X _ { 1 }$ and $\varLambda _ { 1 } : = \dot { \Phi } _ { 1 }$ satisfy

$$
{ \frac { 1 } { \varepsilon } } \Bigl ( \exp ( \varepsilon X _ { 1 } ) i \lambda \exp ( - \varepsilon X _ { 1 } ) - i \lambda \Bigr ) - i A _ { 1 } + W = \mathcal { O } ( \varepsilon ) ,
$$

orequivalently,if $X _ { 1 }$ and $\varLambda _ { 1 }$ solve the commutator equation

$$
[ i \varLambda , X _ { 1 } ] + i \varLambda _ { 1 } = W .
$$

This is solved by setting $i A _ { 1 }$ equal to the diagonal of $W$ and determining the offdiagonal entries $x _ { j k } ^ { ( 1 ) }$ of $X _ { 1 }$ from the scalar equations

$$
i ( \lambda _ { j } - \lambda _ { k } ) x _ { j k } ^ { ( 1 ) } = w _ { j k } , \qquad j \neq k ,
$$

which can be doneas longas the eigenvalues are separated.The diagonal of $X _ { 1 }$ is set to zero. Since $W$ is skew-hermitian,so is $X _ { 1 }$ Similarlyweobtainforhigher powers of $\boldsymbol { \varepsilon }$ theequations

$$
[ i \varLambda , X _ { n } ] + i \varLambda _ { n } = W _ { n - 1 } ,
$$

where thematrix $W _ { n - 1 }$ contains only previously constructed terms up to index $n { - } 1$ andderivativesup to order $\boldsymbol { n }$ andisskew-hermitian because $S _ { \varepsilon }$ isskew-hermitian. Inthiswaywe obtainaunitary transformation such that

$$
\eta ^ { ( N ) } ( t ) = T _ { \varepsilon } ^ { ( N ) } ( t ) y ( t ) \qquad \mathrm { s a t i s f i e s } \quad \dot { \eta } ^ { ( N ) } = \mathcal { O } ( \varepsilon ^ { N } ) .
$$

Weremark thattheaboveconstructionof $T _ { \varepsilon } ^ { ( N ) }$ is analogous totransformations in Hamiltonian perturbation theory;cf.Sect.X.2.

The differential equation (1.1)thus has adiabatic invariants over times $\mathcal { O } ( \varepsilon ^ { - N } )$ forarbitrary $N \geq 1$ ,andin fact even over exponentially long time intervals $t = \mathcal { O } ( e ^ { c / \varepsilon } )$ if the functions havea bounded analytic extension toacomplex strip, asisshownbyJoye&Pfister(1993)andNenciu(1993).The leadingtermin theexponentillysmalldeviationof $| \eta _ { j } ^ { ( N ) } ( t ) | ^ { 2 }$ intheoptimallytuncatedsupebtic basis hasbeenrigorouslymade explicitby Betz&Teufel(20o5a,20o5b),proving aconjecture by Berry (1990).

Avoided Crossing of Eigenvalues and Non-Adiabatic Transitions.To illustrate the effects ofaviolation of the separation condition（1.7),we consider the generic two-dimensional example studiedby Zener(1932),with thematrix

$$
{ \cal Z } ( t ) = - i \left( \begin{array} { c c } { { t } } & { { \delta } } \\ { { \delta } } & { { - t } } \end{array} \right) ,
$$

which has the eigenvalues $\pm i \sqrt { t ^ { 2 } + \delta ^ { 2 } }$ Theminimal distance of the eigenvalues is $2 \delta$ at $t = 0$ For $\delta = \mathcal { O } ( \sqrt { \varepsilon } )$ theadiabatic invariance（1.8） is no longervalid,and $\eta$ canundergo $\mathcal { O } ( 1 )$ changes in an $\mathcal { O } ( \delta )$ neighbourhoodof $t = 0$ ：anon-adiabatic transitioninphysical terminology.Thechanges in theadiabatic invariant due to the avoided crossing of eigenvalues are illustrated in Fig.1.1and can beexplained as follows.

![](images/457d2823b7a3ffb4fcca190f5b6ff63c5d9a97dd144a3a275afe80e24801ddc4.jpg)  
Fig.1.1.Non-adiabatictransition: $| \eta _ { 1 } ( t ) | ^ { 2 }$ and $| \eta _ { 2 } ( t ) | ^ { 2 }$ as function of $t$ for $\varepsilon = 0 . 0 1$ and $\delta = 2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ (increasingdarkness)

Near the avoided crossing,anew time scale $\tau = t / \delta$ isappropriate.The decomposition $Z ( t ) = U ( t ) i \varLambda ( t ) U ( t ) ^ { T }$ of the matrix yields

$$
\begin{array} { r l r } { U ( t ) = \widetilde { U } ( \tau ) } & { = } & { \left( \begin{array} { c c } { \cos \alpha ( \tau ) } & { - \sin \alpha ( \tau ) } \\ { \sin \alpha ( \tau ) } & { \cos \alpha ( \tau ) } \end{array} \right) , } \\ { A ( t ) / \delta = \widetilde { A } ( \tau ) } & { = } & { \left( \begin{array} { c c } { - \sqrt { \tau ^ { 2 } + 1 } } & { 0 } \\ { 0 } & { \sqrt { \tau ^ { 2 } + 1 } } \end{array} \right) , } \end{array}
$$

with $\begin{array} { r } { \alpha ( \tau ) = \frac { \pi } { 4 } - \frac { 1 } { 2 } } \end{array}$ arctan $( \tau )$ .We introduce therescaled matrices

$$
\begin{array} { r c l } { { \widetilde \Phi ( \tau ) } } & { { = } } & { { \displaystyle \int _ { 0 } ^ { \tau } \widetilde { \cal A } ( \sigma ) d \sigma = \displaystyle \Phi ( t ) / \delta ^ { 2 } , } } \\ { { \widetilde W ( \tau ) } } & { { = } } & { { \displaystyle \left( \frac { d } { d \tau } \widetilde { U } ( \tau ) ^ { T } \right) \widetilde { U } ( \tau ) = \displaystyle \frac { 1 } { 2 ( \tau ^ { 2 } + 1 ) } \left( \begin{array} { l l } { { 0 } } & { { - 1 } } \\ { { 1 } } & { { 0 } } \end{array} \right) = \delta \cdot W ( t ) . } } \end{array}
$$

Note that the entries of $W ( t )$ havea sharp peak of height $( 2 \delta ) ^ { - 1 }$ at $t = 0$ The rescaled function $\widetilde { \eta } ( \tau ) = \eta ( t )$ isasolution of the differential equation

$$
\frac { d } { d \tau } \widetilde { \eta } ( \tau ) = \exp \left( - \frac { i \delta ^ { 2 } } { \varepsilon } \widetilde { \Phi } ( \tau ) \right) \widetilde { W } ( \tau ) \exp \left( \frac { i \delta ^ { 2 } } { \varepsilon } \widetilde { \Phi } ( \tau ) \right) \widetilde { \eta } ( \tau ) .
$$

For $\delta ^ { 2 } \leq \varepsilon$ and $| \tau | = | t / \delta | \leq 1$ ,thematrix on the right-hand sideis bounded of norm $\sim 1$ and has bounded derivativeswithrespect to $\gamma$ Thefunction $\overline { { \eta } } ( \tau )$ therefore changes itsvalue by an amount of size $\mathcal { O } ( 1 )$ in the interval $| \tau | \leq 1$ Wealsonote thatany numerical integrator using piecewise polynomial approximations of $W ( t )$ and hence of $W ( \tau )$ must take step sizes $\Delta \tau = h / \delta \ll 1$ ,i.e., $h \ll \delta$ .Onthe otherhand,the rescaling shows that the number of time steps needed to resolve the non-adiabatic transition uptoa specifiedaccuracy is independent of $\delta$ .

# XIV.1.2Adiabatic Integrators

Wediscuss symmetric long-time-step integrators fortherotating-frame differential equation(1.5） that describes skew-hermitiansystemsin adiabatic variables.The construction follows Jahnke&Lubich(2Oo3) andJahnke(2004a);see also Lorenz, Jahnke&Lubich（2005).

First-Order Integrators.We consider thedifferential equation (1.5)and integrate both sides from $t _ { n }$ to $t _ { n + 1 } = t _ { n } + h$ :

$$
\eta ( t _ { n + 1 } ) = \eta ( t _ { n } ) + \int _ { t _ { n } } ^ { t _ { n + 1 } } \exp \left( - \frac { i } { \varepsilon } \varPhi ( s ) \right) W ^ { \prime } ( s ) \exp \left( \frac { i } { \varepsilon } \varPhi ( s ) \right) \eta ( s ) d s ,
$$

where $W ( t )$ isan $\boldsymbol { \mathsf { \Sigma } }$ -independent matrix,continuouslydifferentiablein $t$ ,andthe real diagonal matrix of phases $\varPhi ( t )$ is given as the integral of $\begin{array} { r } { \Lambda ( t ) = \mathrm { d i a g } \left( \lambda _ { j } ( t ) \right) } \end{array}$ . In the applications, $W ( t )$ and $\varPhi ( t )$ are not given explicitly,but need to be computed usingnumerical differentiationand integration,respectively.For simplicity,wehere ignore this approximation and consider $W , \phi$ , $\varLambda$ asgiven time-dependent functions.

Since $\eta$ and $W$ havebounded derivatives,the following averaged version of the implicit midpoint rule hasalocal errorof $\mathcal { O } ( h ^ { 2 } )$ uniformly in $\succeq$ :1

$$
\eta _ { n + 1 } = \eta _ { n } + \int _ { t _ { n } } ^ { t _ { n + 1 } } \exp \Bigl ( - \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) W ( t _ { n + 1 / 2 } ) \exp \Bigl ( \frac { i } { \varepsilon } \Phi ( s ) \Bigr ) d s \ \frac { 1 } { 2 } ( \eta _ { n + 1 } + \eta _ { n } )
$$

The problem then remains to compute the oscillatory integral.The integrand can be rewritten as

$$
E ( \varPhi ( s ) ) \circ W ( t _ { n + 1 / 2 } ) ,
$$

where $\circ$ denotes the entrywise product of matrices and

$$
E ( \varPhi ) = \left( e _ { j k } \right) \quad \mathrm { ~ w i t h ~ } \quad e _ { j k } = \exp \Bigl ( - \frac { i } { \varepsilon } \bigl ( \phi _ { j } - \phi _ { k } \bigr ) \Bigr ) .
$$

With a linear phase approximation (of an error $\mathcal { O } ( h ^ { 2 } )$ ）

$$
\Phi ( t _ { n + 1 / 2 } + \theta h ) \approx \varPhi ( t _ { n + 1 / 2 } ) + \theta h A ( t _ { n + 1 / 2 } ) ,
$$

theintegral is approximated by

$$
h E ( \varPhi ( t _ { n + 1 / 2 } ) ) \bullet \varPsi ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } )
$$

where $\boldsymbol { \mathcal { T } } ( t )$ isthematrix of integrated exponentialswith entries (we omit the argument $t$ ）

$$
\mathcal { T } _ { j k } = \int _ { - 1 / 2 } ^ { 1 / 2 } \exp \Bigl ( - \frac { i \theta h } { \varepsilon } ( \lambda _ { j } - \lambda _ { k } ) \Bigr ) d \theta = \mathrm { s i n c } \Bigl ( \frac { h } { 2 \varepsilon } ( \lambda _ { j } - \lambda _ { k } ) \Bigr ) .
$$

Theerror in the integral approximation comes solely from the linearphase approximationand is bounded by $\begin{array} { r } { \mathcal { O } \big ( h \cdot \frac { h ^ { 2 } } { \varepsilon } \cdot \frac { \varepsilon } { h } \big ) = \mathcal { O } ( h ^ { 2 } ) } \end{array}$ if the $\lambda _ { j }$ areseparated,because then the integral ${ \mathcal { I } } _ { j k }$ is of size $\begin{array} { r } { { \mathcal { O } } \left( \frac { \varepsilon } { h } \right) . } \end{array}$ Wethus obtain the followingaveraged implicit midpointrulewitha local errorof $\mathcal { O } ( h ^ { 2 } )$ uniformlyin $\boldsymbol { \varepsilon }$ :

$$
\begin{array} { r } { \eta _ { n + 1 } = \eta _ { n } + h \Big ( E ( \hat { \Phi } ( t _ { n + 1 / 2 } ) ) \bullet \mathcal { Z } ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } ) \Big ) \frac { 1 } { 2 } ( \eta _ { n + 1 } + \eta _ { n } ) . } \end{array}
$$

Ananalogue of the explicit midpoint rule is similarly constructed,and from the Magnus series (IV.7.5)of the solution we obtain the following averaged exponential midpoint rule,againwith an $\mathcal { O } ( h ^ { 2 } )$ local error uniformly in $\boldsymbol { \mathsf { E } }$ ：

$$
\eta _ { n + 1 } = \exp \left( { \hat { h } E ( \varPhi ( t _ { n + 1 / 2 } ) ) \bullet \varPsi ( t _ { n + 1 / 2 } ) \bullet W ( t _ { n + 1 / 2 } ) } \right) \eta _ { n } .
$$

Forskew-hermitian $W ( t )$ ,alsothematrix in(1.12）and(1.13）isskew-hermitian, and hence both of the above integrators preserve the Euclidean norm of $\eta$ exactly. Wesummarize the local error bounds for these methodsunder conditions that include the case of an avoided crossing of eigenvalues.

Theorem1.2 (Local Error).Suppose that for $t _ { 0 } \leq t \leq t _ { 0 } + h$ andall $j , k ,$

$$
| \lambda _ { j } ( t ) - \lambda _ { k } ( t ) | \geq \delta , \quad | \dot { \lambda } _ { j } ( t ) | \leq C _ { 0 } , \quad | \| W ( t ) \| \leq \frac { C _ { 1 } } { \delta } , \quad \| \dot { W } ( t ) \| \leq \frac { C _ { 2 } } { \delta ^ { 2 } }
$$

with $\delta > 0$ .Then,the localerrorofmethods(1.12)and(1.13)isboundedby

$$
\| \eta _ { 1 } - \eta ( t _ { 0 } + h ) \| \le C \frac { h ^ { 2 } } { \delta ^ { 2 } } \| \eta _ { 0 } \| .
$$

Theconstant $C$ is independent of $h , \varepsilon , \delta$ .

ProofThe result is obtained with the arguments and approximation estimates given above,taking in addition account of the dependence on $\delta$ . □

The local error contains smooth,non-oscillatory components which accumulate toaglobal error $\eta _ { n } - \eta ( t _ { n } ) = \mathcal { O } ( h )$ onbounded intervals if the eigenvaluesremain well separated.Using that in this case $\eta$ isconstant up to $\mathcal { O } ( \varepsilon )$ ,thiserrorbound can be improved to $\mathcal { O } ( \operatorname* { m i n } \{ \varepsilon , h \} )$ The integrators thus do not resolve the $\mathcal { O } ( \varepsilon )$ oscillations in $\eta$ forlarge step sizes $h \geq \varepsilon$ ,butlikeinJahnke&Lubich（2003）

theycan be combined with a(symmetric and scaling-invariant) adaptive step size strategy such that themethods followthe non-adiabatic transitions through avoided crossings of eigenvalueswith small stepsand take large steps elsewhere.

Wehereconsiderapplyingan integrating reversible step size controleras in Sect.VII.3.2 with the step size density function

$$
\sigma ( t ) = \left( \| W ( t ) \| ^ { 2 } + \alpha ^ { 2 } \right) ^ { - 1 / 2 }
$$

for a parameter $\alpha$ that can be interpreted as the ratio of theaccuracy parameter andthe maximum admissible step size.Choosing the Frobenius norm $\| W \| =$ (trace $W ^ { T } W ) ^ { 1 / 2 }$ ,wethen obtain the following version of Algorithm VIII.3.4, where $\mu$ istheaccuracyparameterand

$$
G ( t ) = - \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } = \left( \| W ( t ) \| ^ { 2 } + \alpha ^ { 2 } \right) ^ { - 1 } \operatorname { t r a c e } \left( \dot { W } ( t ) ^ { T } W ( t ) \right) .
$$

Set $z _ { 0 } = 1 / \sigma ( t _ { 0 } )$ and,for $n \geq 0$

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n } + { \displaystyle \frac { \mu } { 2 } } G ( t _ { n } ) } } \\ { { h _ { n + 1 / 2 } } } & { { = } } & { { \displaystyle \mu / z _ { n + 1 / 2 } } } \\ { { t _ { n + 1 } } } & { { = } } & { { t _ { n } + h _ { n + 1 / 2 } } } \\ { { \eta _ { n } } } & { { \mapsto } } & { { \displaystyle \eta _ { n + 1 } ~ \mathrm { ~ b y ~ } ( 1 . 1 2 ) ~ \mathrm { o r ~ } ( 1 . 1 3 ) ~ \mathrm { w i t h ~ s t e p ~ s i z e ~ } h _ { n + 1 / 2 } } } \\ { { z _ { n + 1 } } } & { { = } } & { { \displaystyle z _ { n + 1 / 2 } + { \displaystyle \frac { \mu } { 2 } } G ( t _ { n + 1 } ) . } } \end{array}
$$

Weremark that the schemes(1.12)and(1.13)can be modified such that they use evaluations at $t _ { n }$ and $t _ { n + 1 }$ instead of $t _ { n + 1 / 2 }$ (Exercise 6).

Applying the above algorithmwith accuracy parameter $\mu = 0 . 0 1$ and $\alpha = 0 . 1$ totheproblemofFig.1.1with $\varepsilon = 0 . 0 1$ and $\delta = 2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ yields the step size sequences shown in Fig.1.2.In each case the error at the end-point $t = 1$ was between $0 . 5 \cdot 1 0 ^ { - 3 }$ and $2 \cdot 1 0 ^ { - 3 }$ .

![](images/43b8f4c3a712a0c19f91a7dc78dcbe3e9172acc0c8238c5d358baea084272663.jpg)  
Fig.1.2.Non-adiabatic transition:step sizes as function of $t$ for $\varepsilon ~ = ~ 0 . 0 1$ and $\delta \ =$ $2 ^ { - 1 } , 2 ^ { - 3 } , 2 ^ { - 5 } , 2 ^ { - 7 }$ (increasingdarkness）

Second-Order Integrators.The $\mathcal { O } ( \varepsilon )$ oscillations in $\eta$ areresolved with step sizes upto $h \ = \ O ( { \sqrt { \varepsilon } } )$ for methods that give $\mathcal { O } ( h ^ { 2 } )$ accuracy uniformlyin $\varepsilon$ Such methods requirea quadraticphase approximation,and one needs further terms obtained from reinserting $\eta ( s )$ under theintegral in（1.iO）onceagainbythesame formula,thus yielding termswith iterated integrals (this procedure is known as the Neumann or Peano or Dyson expansion in different communities,cf.Iserles 2004), orbyincludingthe first commutatorin the Magnus expansion (IV.7.5).Symmetric second-order methods of both typesare constructed by Jahnke (2004a).

Caremust be taken in computing the arising oscillatory integrals.Iserles (2004) proposesand analysesFilon quadrature (after Filon,1928),whichisapplicable whenthemoments,i.e.,the integrals overproducts of oscillatory exponentials andpolynomials,areknownanalytically.Thisis not thecase,however,for all of theintegrals appearing in the second-order methods.The alternative chosen by Jahnke(2oo4a) is to use an expansion technique based on partial integration.The ideacan beillustrated on an integral suchas

$$
\int _ { 0 } ^ { 1 } \exp \Bigl ( \frac { i \alpha \theta h } { \varepsilon } \Bigr ) \cdot \exp \Bigl ( \frac { i \beta \theta ^ { 2 } h ^ { 2 } } { \varepsilon } \Bigr ) d \theta
$$

with $\alpha \neq 0$ Partial integration that integratesthe firstfactoranddifferentiates the second factoryieldsa boundary termandagainanintegral ofthe sametype,but nowwithanadditionalfactor $\begin{array} { r } { \mathcal { O } \big ( \frac { \varepsilon } { h } \cdot \frac { h ^ { 2 } } { \varepsilon } \big ) = \mathcal { O } ( h ) } \end{array}$ Usingthistechniquerepeatedly intheoscillatory integrals appearingin the second-order methods permitstoapproximate all of themup to $\mathcal { O } ( h ^ { 3 } )$ asneeded.WerefertoJahnke(20o4a) forthe precise formulation and error analysis of these second-order methods,which are complicated to formulate,but do not require substantially more computational work than the first-ordermethods described above,and just the same number of matrix evaluations.

Higher-Order Integrators.Integrators of general order $p \geq 1$ are obtained with a phaseapproximation bypolynomialsofdegree $p$ andby includingall termsof the Neumann orMagnus expansion for（1.5）withup to $p$ -foldintegrals.

# XIV.2Mechanical Systemswith Time-Dependent Frequencies

Westudy oscillatory mechanical systems with explicitly time-dependent frequencies,where the time-dependentHamiltonianis

$$
H ( p , q , t ) = { \frac { 1 } { 2 } } p ^ { T } M ( t ) ^ { - 1 } p + { \frac { 1 } { 2 \varepsilon ^ { 2 } } } q ^ { T } A ( t ) q + U ( q , t )
$$

with apositive definitemass matrix $M ( t )$ andapositive semi-definite stiffness matrixA(t）ofconstant rankwhosederivativesare bounded independentlyof $\boldsymbol { \varepsilon }$ .Such aHamiltonian describes oscillations ina mechanical system that at the same time exertsa driven motion onaslower time scale.We considermotions of bounded energy:

$$
H ( p ( t ) , q ( t ) , t ) \leq \mathrm { C o n s t } .
$$

Wetransform (2.1) toamoreamenable form bya seriesof linear time-dependent canonical coordinate transforms.The transformations turn the equations of motion intoaform that approximately separates the time scales.This makes theproblem moreaccessible to numerical discretization with large time steps and to the error analysis of multiple time-steppingmethods applieddirectlyto(2.1)in theoriginally given coordinates.

# XIV.2.1 Canonical Transformationto Adiabatic Variables

Bya series of canonical time-dependent linear transformations,which can all be donenumericallywith standard linearalgebra routines,we now take the Hamiltonian system(2.1）toa form fromwhich adiabatic invariantscan beread off and which will serve as the base camp for both the construction and error analysis of numerical methods.

Weintroduce the energy $E$ as theconjugate variableto time $t$ and extend the Hamiltonian to

$$
\widehat { H } ( p , E , q , t ) = H ( p , q , t ) + E .
$$

The canonicalequations ofmotion are then (the gradient $\nabla$ refers only to $q$ ）

$$
\begin{array} { r c l } { \dot { p } } & { = } & { - \displaystyle \frac { 1 } { \varepsilon ^ { 2 } } A ( t ) q - \nabla U ( q , t ) } \\ { \dot { q } } & { = } & { { \cal M } ( t ) ^ { - 1 } p } \end{array}
$$

along with $\dot { E } = - \partial H / \partial t$ and $t = 1$

Transforming theMassMatrix into the Identity Matrix.We change variables such that the mass matrix $M ( t )$ inthe kineticenergy part is replaced bythe identity. Witha smooth factorization

$$
\boldsymbol { M } ( t ) ^ { - 1 } = \boldsymbol { C } ( t ) \boldsymbol { C } ( t ) ^ { T } ,
$$

e.g.,froma Cholesky decomposition of $M ( t )$ ,wetransformto variables $( \widetilde { q } , t )$ by

$$
q = C ( t ) \widetilde { q } , \quad t = \widetilde { t } .
$$

Then,theconjugate momenta are given by (see Example VI.5.2)

$$
\left( \begin{array} { l } { \medskip \widetilde { p } } \\ { \widetilde { E } } \end{array} \right) = \left( \begin{array} { l l } { \medskip C } & { \dot { C } \widetilde { q } } \\ { 0 } & { 1 } \end{array} \right) ^ { T } \left( \begin{array} { l } { \medskip p } \\ { E } \end{array} \right) = \left( \begin{array} { c } { \medskip C ^ { T } p } \\ { \widetilde { q } ^ { T } \dot { C } ^ { T } p + E } \end{array} \right) .
$$

With the transformed matrix $\begin{array} { r c l } { A } & { = } & { C ^ { T } A C } \end{array}$ ,the Hamiltonian ${ \cal H } ( \widetilde { p } , E , \widetilde { q } , \widetilde { t } ) \ =$ $\hat { H } ( p , E , q , t )$ in thenew variables then takes the form(we omitalltildes)

$$
{ \cal H } ( p , E , q , t ) = \frac { 1 } { 2 } p ^ { T } p + \frac { 1 } { 2 \varepsilon ^ { 2 } } q ^ { T } { \cal A } ( t ) q - q ^ { T } \dot { C } ( t ) ^ { T } C ( t ) ^ { - T } p + U ( C ( t ) q , t ) + { \cal B } ( t ) \dot { C } ( t ) \dot { C } ( t ) ,
$$

Diagonalizing the Stiffness Matrix.We diagonalize the matrix $A ( t )$ in (2.5）,

$$
A ( t ) = Q ( t ) \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { \varOmega ( t ) ^ { 2 } } } \end{array} \right) Q ( t ) ^ { T }
$$

with the diagonal matrix $\Omega ( t ) = \mathrm { d i a g } ( \omega _ { j } ( t ) )$ of frequencies and an orthogonal matrix $Q ( t )$ ,which depends smoothlyon $t$ ifthe frequencies remain separated.The matrix $Q ( t )$ can be obtained as the product

$$
Q ( t ) = Q _ { 0 } ( t ) \left( \begin{array} { c c } { { I } } & { { 0 } } \\ { { 0 } } & { { Q _ { * } ( t ) } } \end{array} \right) ,
$$

where the transformation with $Q _ { 0 } ( t )$ takes $A ( t )$ to the block-diagonal form

$$
A ( t ) = Q _ { 0 } ( t ) \left( \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { A _ { * } ( t ) } } \end{array} \right) Q _ { 0 } ( t ) ^ { T }
$$

and $Q _ { * } ( t )$ diagonalizes $A _ { * } ( t )$ Theeffect of an avoided crossing of frequencies is localized to $Q _ { * } ( t )$ ,which then can have large derivatives,whereas those of $Q _ { 0 } ( t )$ remainmoderatelybounded.The transformation

$$
q = Q ( t ) { \widehat { q } } , \quad t = { \widehat { t } }
$$

with the conjugate momenta

$$
\widehat { \boldsymbol { p } } = \boldsymbol { Q } ( t ) ^ { T } \boldsymbol { p } , \quad \widehat { \boldsymbol { E } } = \widehat { \boldsymbol { q } } ^ { T } \dot { \boldsymbol { Q } } ( t ) ^ { T } \boldsymbol { p } + \boldsymbol { E }
$$

yields the Hamiltonian in thenew variables $( \widehat { p } , \widehat { E } , \widehat { q } , \widehat { t } )$ as (we omit all hats)

$$
H = \frac { 1 } { 2 } { p ^ { T } } p + \frac { 1 } { 2 { \varepsilon } ^ { 2 } } { q ^ { T } } \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { \varOmega ( t ) ^ { 2 } } \end{array} \right) q + { q ^ { T } } K ( t ) { p } + U ( C ( t ) Q ( t ) { q } , t ) + E
$$

with

$$
K = { \binom { K _ { 0 0 } } { K _ { 1 0 } } } K _ { 0 1 } \Big ) = Q ^ { T } \dot { Q } - Q ^ { T } \dot { C } ^ { T } C ^ { - T } Q .
$$

We decompose also

$$
\begin{array} { r } { p = \binom { p _ { 0 } } { p _ { 1 } } , \quad q = \binom { q _ { 0 } } { q _ { 1 } } } \end{array}
$$

according to the blocks in(2.6) and refer to $q _ { 0 }$ and $q _ { 1 }$ （ $p _ { 0 }$ and $p _ { 1 }$ astheslowand fast positions (slow and fast momenta),respectively.With the energy bound (2.2) wehave

$$
p _ { 1 } = \mathcal { O } ( 1 ) , \quad q _ { 1 } = \mathcal { O } ( \varepsilon ) .
$$