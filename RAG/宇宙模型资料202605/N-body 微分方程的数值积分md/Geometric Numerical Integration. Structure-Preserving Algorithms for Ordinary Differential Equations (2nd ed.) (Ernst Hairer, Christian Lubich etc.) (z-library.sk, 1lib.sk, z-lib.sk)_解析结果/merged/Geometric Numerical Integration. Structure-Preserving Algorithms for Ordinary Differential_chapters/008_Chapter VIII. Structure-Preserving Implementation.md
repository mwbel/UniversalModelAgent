# Chapter VIII. Structure-Preserving Implementation

Thischapter is devoted to practical aspects of an implementation of geometric integrators.We explain strategies for changing the step size whichdo not deteriorate the correct qualitative behaviour of the solution.We study multiple time stepping strategies,the effect of round-off in long-time integrations,and the efficient solution of nonlinear systems arising in implicit integration schemes.

# VIII.1 Dangers of Using Standard Step Size Control

Another possible shortcoming of the method concerns its behavior when usedwitha variable stepsize...The integratorcompletely loses its desirable qualities...This can be understood at least qualitatively by realizing thatby changing the time step one is in essence continually changingthe nearby Hamiltonian... (B.Gladman,M.Duncan&J.Candy1991)

In the previouschapterswe have studied symmetricand symplectic integrators,and wehave seen an enormous progress in long-time integrations of various problems. Decadesago,a similar enormous progresswas the introduction of algorithms with automatic step size control.Naively,one would expect that the blind combination ofboth techniques leads to even betterperformances.We shall see bya numerical experiment that thisis not the case,a phenomenon observed by Gladman,Duncan &Candy(1991)and Calvo& Sanz-Serna(1992).

We study the long-time behaviour of symplectic methods combined with the following standard step size selection strategy(see e.g.,Hairer,Nprsett&Wanner (1993),Sect.II.4).We assume that an expression $e r r _ { n }$ related to the local error is available for the current step computed with step size $h _ { n }$ (usually obtained with an embedded method).Based on an asymptotic formula $e r r _ { n } \approx C h _ { n } ^ { r }$ (for $h _ { n } \to 0$ and ontherequirement to get an errorclose toa user supplied tolerance Tol,we predict a new step size by

$$
h _ { n e w } = 0 . 8 5 \cdot h _ { n } \Big ( \frac { T o l } { e r r _ { n } } \Big ) ^ { 1 / r } ,
$$

wherea safety factor O.85 is included.We thenapplythe methodwithstep size $h _ { n + 1 } \ = \ h _ { n e w } .$ If for the new step $e r r _ { n + 1 } \ \leq \ T o l$ ,thestep isaccepted and the integration is continued.If $e r r _ { n + 1 } > T o l$ ,it isrejected and recomputed with the step size $h _ { n e w }$ obtained from（1.1）with $n + 1$ instead of $\boldsymbol { n }$ Similar step size strategies areimplemented inmost codes for solving ordinary differential equations.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/89c4b9a7b805c613f09b5494523bcb8db9b5a2028cb879af0a3423484ffb932b.jpg)  
Fig.1.1.Stormer-Verlet scheme applied with fixed step size(middle)orwith the standard step size strategy(below) compared to the exact solution(above);solutions are for the interval $0 \leq t \leq 1 2 0$ (left),for $2 0 0 0 \leq t \leq 2 1 2 0$ (middle),and for $4 0 0 0 \leq t \leq 4 1 2 0$ (right)

Numerical Experiment. We consider the perturbed Kepler problem

$$
\begin{array} { c c c } { { \dot { q } _ { 1 } = p _ { 1 } , } } & { { ~ \dot { p } _ { 1 } = - \displaystyle \frac { q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - \displaystyle \frac { \delta q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 5 / 2 } } } } \\ { { \dot { q } _ { 2 } = p _ { 2 } , } } & { { ~ \dot { p } _ { 2 } = - \displaystyle \frac { q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } - \displaystyle \frac { \delta q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 5 / 2 } } } } \end{array}
$$

$\delta = 0 . 0 1 5 )$ with initialvalues

$$
q _ { 1 } ( 0 ) = 1 - e , \quad q _ { 2 } ( 0 ) = 0 , \quad p _ { 1 } ( 0 ) = 0 , \quad p _ { 2 } ( 0 ) = \sqrt { ( 1 + e ) / ( 1 - e ) }
$$

(eccentricity $e = 0 . 6$ ).AsanumericalmethodwetaketheStormer-Verlet scheme (I.1.17)which is symmetric,symplectic,and of order2.The fixed step size implementation isstraightforward.For thevariable step size strategywe take for $e r r _ { n }$ the Euclidean normof thedifference between the Stormer-Verlet solutionand the symplectic Euler solution(which is availablewithout any further functionevaluation). Since $e r r _ { n } = { \cal O } ( h _ { n } ^ { 2 } )$ wetake $r = 2$ in (1.1).

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/96dd645b19f619b34a145b7524602d28b49626376587fd7631de76adc029c9f1.jpg)  
Fig.1.2.Study of the error intheHamiltonianand of the global error for theStormer-Verlet scheme.Fixed step size implementation with $h = 1 0 ^ { - 3 }$ variablestep size with $T o l = 1 0 ^ { - 4 }$

The numerical solution in the $\left( q _ { 1 } , q _ { 2 } \right)$ -planeispresented inFig.1.1.Tomake thelong-time behaviour of the two implementationsvisible,we show the numerical solution on threedifferentparts of the integration interval.We have included thenumbers of steps needed for the integration toreach $t = 1 2 0$ ,2120,and4120, respectively.We see that the qualitative behaviour of thevariable step size implementation is not correct,although itis more precise on short intervals.Moreover, thenear-preservation of theHamiltonianis lost (see Fig.1.2） asisthelinear error growth.Apparently,the error in the Hamiltonian behaves like $\left| a - b t \right|$ forthevariable step size implementation,and that for the solution like $\vert c t - d t ^ { 2 } \vert$ (with constants $a , b , c , d$ depending on $T o l$ ).Dueto therelatively large eccentricity of theproblem, thevariable step size implementation needs fewer function evaluations foragiven accuracy ona short timeinterval,but the opposite is true forlong-time integrations.

The aim of the next two sections is to present approaches which permit the use ofvariable step sizes for symmetric or symplectic methods without losing the qualitatively correctlong-time behaviour.

# VIII.2 Time Transformations

A variable step size implementation produces approximations $y _ { n }$ ona (non-equidistant）grid $\left\{ t _ { n } \right\}$ Thesame effectcan beachieved by performingin advance a time transformation $t  \tau$ and by applyingaconstant step size implementation tothetransformed system.If the time transformation is given as the solution ofa diferentialequation,itfollowsfromthecinrule $\begin{array} { r } { \frac { d y } { d \tau } = \frac { d y } { d t } \frac { d t } { d \tau } } \end{array}$ thatthe transformed systemis

$$
y ^ { \prime } = \sigma ( y ) f ( y ) , \qquad t ^ { \prime } = \sigma ( y ) .
$$

Here,prime indicates a derivative with respect to $\tau$ ,and we use the same letter $y$ for the solutions $y ( t )$ of $\dot { y } = f ( y )$ and $y ( \tau )$ of (2.1). If $\sigma ( y ) > 0$ ,the correspondence $t  \tau$ isbijective.

Applyinga numerical method with constant step size $\succeq$ to（2.1）yieldsapproximations $y _ { n } \approx y ( \tau _ { n } ) = y ( t _ { n } )$ ,where $\begin{array} { r } { { \mathrm { \Delta } n } = n \varepsilon } \end{array}$ and

$$
t _ { n + 1 } - t _ { n } = \int _ { n \varepsilon } ^ { ( n + 1 ) \varepsilon } \sigma { \big ( } y ( \tau ) { \big ) } d \tau \approx \varepsilon \sigma ( y _ { n } ) .
$$

Approximations to $t _ { n }$ areobtained by integrating numerically the differential equation $t ^ { \prime } = \sigma ( y )$ togetherwith $y ^ { \prime } = \sigma ( y ) f ( y )$

Inthe context of geometric numerical integration,we are interested in time transformations such that the vector field $\sigma ( y ) f ( y )$ retains geometric features of $f ( y )$

# VIII.2.1 Symplectic Integration

Fora Hamiltonian system $\dot { y } = f ( y ) = J ^ { - 1 } \nabla H ( y )$ it is natural to search for step size functions $\sigma ( y )$ such that(2.1） isagain Hamiltonian.For thiswe have tocheck whether the Jacobian of $\sigma ( y ) \nabla H ( y )$ is symmetric (cf.Integrability Lemma VI.2.7). But this is the case onlyif $\nabla H ( y ) \nabla \sigma ( y ) ^ { T }$ is symmetric,i.e., $\nabla H ( y )$ and $\nabla \sigma ( y )$ are collinear,so that $\begin{array} { r } { \frac { d } { d t } \sigma \big ( y ( t ) \big ) \ = \nabla \sigma \big ( y ( t ) \big ) ^ { T } J \nabla H \big ( y ( t ) \big ) \ = \ 0 , } \end{array}$ Consequently, $\sigma ( y ) = C o n s t$ along solutions of the Hamiltonian systemwhich is what makes this approach unattractive foravariable step size integration.This disappointing fact has beenobserved by Stoffer(1988,1995)and Skeel&Gear(1992).

Themain idea for circumventing this diffculty is the following:suppose we want to integrate the Hamiltonian system with steps of size $h \approx \varepsilon \sigma ( y )$ where $\sigma ( y ) > 0$ isastate-dependent given function and $\varepsilon > 0$ isa small parameter. Instead of multiplying the vector field $f ( y ) = J ^ { - 1 } \nabla H ( y )$ by $\sigma ( y )$ ,we consider the new Hamiltonian

$$
K ( y ) = \sigma ( y ) \Big ( H ( y ) - H _ { 0 } \Big ) ,
$$

where $H _ { 0 } ~ = ~ H ( y _ { 0 } )$ fora fixed initial value $y _ { 0 }$ .Thecorresponding Hamiltonian systemis

$$
y ^ { \prime } = \sigma ( y ) J ^ { - 1 } \nabla H ( y ) + \left( H ( y ) - H _ { 0 } \right) J ^ { - 1 } \nabla \sigma ( y ) .
$$

Compared to (2.1） we have introduced a perturbation,which vanishes along the solution of the Hamiltonian system passing through $y _ { 0 }$ ,butwhich makesthe system Hamiltonian.

Time transformations such as in (2.3)are used in classical mechanics for an analytictreatment of Hamiltonian systems (Levi-Civita(1906,192O),where(2.3）is called the“Darboux-Sundman transformation",see Sundman(1912)).Zare& Szebehely(1975) consider such time transformations for numerical purposes (without takingcareofsymplecticity).Waldvogel&Spirig（1995)applythe transformations proposed byLevi-Civita to Hill'slunar problemand solve the transformed equations bycomposition methods in order to preserve the symplectic structure.The following general procedurewas proposed independently by Hairer(1997)and Reich(1999).

Algorithm2.1.Applyanarbitrarysymplectic one-stepmethod with constant step size $\varepsilon$ totheHamiltoniansystem(2.4),augmented by $t ^ { \prime } = \sigma ( y )$ Thisyields numericalapproximations $( y _ { n } , t _ { n } )$ with $y _ { n } \approx y ( t _ { n } )$ .

Although this algorithmyields numerical approximations on anon-equidistant grid,it canbe considered asa fixed stepsize,symplectic method applied toa differentHamiltonian system.This interpretation allowsone to apply the standard techniques for the study of its long-time behaviour.

A disadvantage of thisalgorithmis that for separable Hamiltonians $H ( p , q ) =$ $T ( p ) + U ( q )$ the transformed Hamiltonian (2.3)is no longer separable.Hence,methodsthat are explicit for separable Hamiltoniansare not explicitin the implementationofAlgorithm2.1.The following examples illustrate that this disadvantage can bepartially overcome for the important caseof Hamiltonian functions

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { T } M ^ { - 1 } p + U ( q ) ,
$$

where $M$ is aconstant symmetric matrix.

Example2.2 (Symplectic Eulerwith $\mathbf { \xi } _ { p }$ -Independent Step Size Function).For step size functions $\sigma ( q )$ thesymplectic Euler method,applied with constant step size $\boldsymbol { \mathsf { E } }$ to(2.4）,reads

$$
\begin{array} { r l } & { p _ { n + 1 } = p _ { n } - \varepsilon \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \varepsilon \Big ( \frac { 1 } { 2 } p _ { n + 1 } ^ { T } M ^ { - 1 } p _ { n + 1 } + U ( q _ { n } ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) } \\ & { q _ { n + 1 } = q _ { n } + \varepsilon \sigma ( q _ { n } ) M ^ { - 1 } p _ { n + 1 } } \end{array}
$$

and yieldsan approximation at $t _ { n + 1 } = t _ { n } + \varepsilon \sigma ( q _ { n } ) .$ The first equation is non-$p _ { n + 1 }$ $\beta : = \| p _ { n + 1 } \| _ { M } ^ { 2 } : =$ $p _ { n + 1 } ^ { T } M ^ { - 1 } p _ { n + 1 }$

$$
\beta = \Big \| p _ { n } - \varepsilon \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \varepsilon \Big ( \frac { \beta } { 2 } + U ( q _ { n } ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) \Big \| _ { M } ^ { 2 }
$$

which canbe solved directly.Thenumerical solution $( p _ { n + 1 } , q _ { n + 1 } )$ is then given explicitly.

Choices of Step Size Functions. Sometimes suitable functions $\sigma ( p , q )$ areknown a priori.For example,for the two-body problem one can take $\sigma ( p , q ) = \| q \| ^ { \alpha } ,$ e.g., $\alpha = 2$ ,or $\alpha = 3 / 2$ topreserve the scaling invariance（Budd &Piggott 2Oo3）,so that smaller step sizes are taken when the two bodies are close.

Aninteresting choice,which does not require any a priori knowledge of the solution,is $\sigma ( y ) = \| f ( y ) \| ^ { - 1 } .$ The solution of (2.1) then satisfies $\| y ^ { \prime } ( \tau ) \| = 1$ (arclength parameterization）andwe get approximations $y _ { n }$ thatare nearly equidistant inthephase space.Such time transformations have been proposed by McLeod& Sanz-Serna（1982) for graphical reasonsandby Huang&Leimkuhler（1997).Fora Hamiltonian system with $H ( p , q )$ givenby(2.5),itis thusnatural to consider

$$
\sigma ( p , q ) = { \left( { \frac { 1 } { 2 } } p ^ { T } M ^ { - 1 } p + \nabla U ( q ) ^ { T } M ^ { - 1 } \nabla U ( q ) \right) } ^ { - 1 / 2 } .
$$

Wehave chosen this particular norm,because it leaves the expression (2.6) invariant with respect to linear coordinate changes $q \mapsto A q$ （implying $p \mapsto A ^ { - T } p$ .Exploiting the fact that the Hamiltonian(2.5)is constant along solutions,the step size function(2.6) can be replaced by the $\boldsymbol { p }$ -independent function

$$
\sigma ( { q } ) = \Big ( \big ( H _ { 0 } - U ( { q } ) \big ) + \nabla U ( { q } ) ^ { T } M ^ { - 1 } \nabla U ( { q } ) \Big ) ^ { - 1 / 2 } .
$$

Theuse of(2.6) and (2.7） gives nearly identical results,but (2.7)is easier to implement.Ifweare interestedin an output that isapproximatively equidistant in the $q$ -space,we cantake

$$
\sigma ( q ) = { \left( H _ { 0 } - U ( q ) \right) } ^ { - 1 / 2 } .
$$

Example2.3 (Stormer-Verlet Schemewith $\boldsymbol { p }$ -Independent Step Size Function). Fora step size function $\sigma ( q )$ theStormer-Verlet scheme gives

$$
\begin{array} { r l } & { p _ { n + 1 / 2 } = p _ { n } - \frac { \varepsilon } { 2 } \sigma ( q _ { n } ) \nabla U ( q _ { n } ) - \frac { \varepsilon } { 2 } \Big ( H \big ( p _ { n + 1 / 2 } , q _ { n } \big ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n } ) } \\ & { \quad q _ { n + 1 } = q _ { n } + \frac { \varepsilon } { 2 } \big ( \sigma ( q _ { n } ) + \sigma ( q _ { n + 1 } ) \big ) M ^ { - 1 } p _ { n + 1 / 2 } } \\ & { p _ { n + 1 } = p _ { n + 1 / 2 } - \frac { \varepsilon } { 2 } \sigma ( q _ { n + 1 } ) \nabla U ( q _ { n + 1 } ) } \\ & { \qquad \quad - \frac { \varepsilon } { 2 } \Big ( H \big ( p _ { n + 1 / 2 } , q _ { n + 1 } \big ) - H _ { 0 } \Big ) \nabla \sigma ( q _ { n + 1 } ) , } \end{array}
$$

Thefirst equation isessentially the same as that for the symplectic Eulermethod, andit can be solved for $_ { p _ { n + 1 / 2 } }$ as explained in Example 2.2.The second equation isimplicit in $q _ { n + 1 }$ ,but itis suficient to solve thescalar equation

$$
\gamma = \sigma \Big ( q _ { n } + \frac { \varepsilon } { 2 } \big ( \sigma ( q _ { n } ) + \gamma \big ) M ^ { - 1 } p _ { n + 1 / 2 } \Big )
$$

for $\gamma = \sigma ( q _ { n + 1 } ) .$ Newton iterations can be effciently applied,because $\nabla \sigma ( q )$ is available already.Thelastequation (for $p _ { n + 1 }$ )is explicit.This variable step size Stormer-Verlet scheme gives approximations at $t _ { n }$ ,where

$$
t _ { n + 1 } = t _ { n } + \frac { \varepsilon } { 2 } \bigl ( \sigma ( q _ { n } ) + \sigma ( q _ { n + 1 } ) \bigr ) .
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/cafd874ef84dfac8555f905ad8f1f11a86f25a90b5bb7de9f84e8bdccf66994b.jpg)  
Fig.2.1.Various step size strategies forthe Stormer-Verlet scheme(Example2.3)applied to theperturbedKeplerproblem(1.2）on the interval [0,10](approximately two periods)

In Fig.2.1 we illustrate how the different step size functions influence the position of the output points.Weapply the Stormer-Verlet method of Example2.3 to the perturbed Keplerproblem(1.2)with initial values,perturbation parameter,and eccentricity asin Sect.VIII.1.As step size functions we use(2.7),(2.8),and constant step size $\sigma ( q ) \equiv 1$ Forall three choices of $\sigma ( q )$ wehave adjusted theparameter $\varepsilon$ in such away that themaximal error in the Hamiltonianis close to O.O1.The step size strategy(2.7)isapparently themost efficient one.Forthisstrategy,we observe that the output points in the $q$ -plane concentrate in regionswhere thevelocity is large, while the constant step size implementation shows the opposite behaviour.

# VIII.2.2Reversible Integration

For $\rho$ -reversibledifferential equations $\dot { y } = f ( y )$ ,i.e., $f ( \rho y ) = - \rho f ( y )$ for all $_ y$ ,the time transformed problem (2.1) remains $\rho$ -reversibleif

$$
\sigma ( \rho y ) = \sigma ( y ) .
$$

Thiscondition is not very restrictiveand is satisfiedby many important time transformations.Inparticular,(2.11） holds for thearc lengthparameterization $\sigma ( y ) =$ $\| f ( y ) \| ^ { - 1 }$ if $\rho$ is orthogonal.Consequently,it makes sense to apply symmetric,reversible numerical methods with constant step size $\varepsilon$ directly to the system (2.1).

However,similar to the symplectic integration of Sect.VII.2.1,there isa serious disadvantage.For separable differential equations (i.e.,problems that can be splitas ${ \dot { p } } = f _ { 1 } ( q )$ , $\dot { q } = f _ { 2 } ( p )$ ）and for non-constant $\sigma ( p , q )$ the transformed system(2.1) isnolonger separable.Hence,methods that are explicit for separable problemsare notnecessarily explicit for(2.1）.

Example2.4(Adaptive Stormer-VerletMethod).We considera Hamiltonian systemwithseparable Hamiltonian(2.5),andweapply the Stormer-Verlet scheme to(2.1).Thisyields(Huang&Leimkuhler1997)

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 / 2 } = p _ { n } - \displaystyle \frac { \varepsilon } { 2 } s _ { n } \nabla U ( q _ { n } ) } } \\ { { } } & { { } } & { { q _ { n + 1 } = q _ { n } + \displaystyle \frac { \varepsilon } { 2 } \bigl ( s _ { n } + s _ { n + 1 } \bigr ) M ^ { - 1 } p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } = p _ { n + 1 / 2 } - \displaystyle \frac { \varepsilon } { 2 } s _ { n + 1 } \nabla U ( q _ { n + 1 } ) , } } \end{array}
$$

where $s _ { n } = \sigma ( p _ { n + 1 / 2 } , q _ { n } )$ and $s _ { n + 1 } = \sigma ( p _ { n + 1 / 2 } , q _ { n + 1 } )$ (notice that the $s _ { n + 1 }$ of thecurrent step is not the same as the $s _ { n }$ of the subsequent step,if $\sigma ( p , q )$ depends on $p$ .Thevalues $( p _ { n + 1 } , q _ { n + 1 } )$ are approximations to the solutionat $t _ { n }$ ,where

$$
t _ { n + 1 } = t _ { n } + \frac { \varepsilon } { 2 } \big ( s _ { n } + s _ { n + 1 } \big ) .
$$

Fora $p$ -independent step size function $s$ ,method (2.12) corresponds to that of Example2.3,where the terms involving $\nabla \sigma ( q )$ areremoved.The implicitness of(2.12) iscomparable to that of the method of Example2.3.Completely explicit variantsof this method will be discussed in the next section.

We conclude this section with a brief comparison of the variable step size Stormer-Verletmethods of Examples2.3 and 2.4.Method(2.12) is easier to implement and more efficient when the step size function $\sigma ( p , q )$ is expensive to evaluate.Ina few numerical comparisons we observed,however,that the errorin the Hamiltonian and in the solution isin general larger for method(2.12),and that themethod（2.9） becomes competitive when $\sigma ( p , q )$ is $p$ -independentand easyto evaluate.A similar observationin favour of method(2.9) has beenmadeby Calvo, L6pez-Marcos& Sanz-Serna(1998).

# VIII.3 Structure-Preserving Step Size Control

Thedisappointing long-time behaviour in Fig.1.1 of thevariable step sizeimplementationof theStormer-Verlet scheme isdue to lack of reversibility.Indeed,fora $\rho$ -reversible differential equationthe step size $h _ { n + 1 / 2 }$ taken for stepping from $y _ { n }$ to $y _ { n + 1 }$ should be the same as thatwhen stepping from $\rho y _ { n + 1 }$ to $\rho y _ { n }$ (cf.Fig.V.1.1). The strategy of Sect.VII.1,for which the step sizedepends on information of the preceding step,cannot guarantee such a property.

# VIII.3.1Proportional,Reversible Controllrs

Following a suggestion of Stoffer (1988）we consider step sizes depending only oninformation of the present step,i.e.,beingproportional to some function of the actual state.This leads tothealgorithm

$$
y _ { n + 1 } = \varPhi _ { h _ { n + 1 / 2 } } ( y _ { n } ) , \qquad h _ { n + 1 / 2 } = \varepsilon s ( y _ { n } , \varepsilon ) ,
$$

where $\varPhi _ { h } ( y )$ isa one-step method for $\dot { y } = f ( y )$ ,and $\boldsymbol { \varepsilon }$ isasmall parameter.For theoretical investigations itis useful to consider themapping

$$
\varPsi _ { \varepsilon } ( y ) : = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) .
$$

This isa one-stepdiscretization,consistent with $y ^ { \prime } = s ( y , 0 ) f ( y )$ ,andapplied with constant step size $\boldsymbol { \varepsilon }$ .Consequently,all results concerning the long-time integration

with constant steps (e.g.,backward error analysis of Chap.IX),and the definitions ofsymmetryandreversibilitycanbeextendedinastraightforwardway.

Symmetry.Wecall the algorithm(3.1） symmetric,if $\varPsi _ { \varepsilon } ( y )$ issymmetric,i.e., $\bar { \psi } _ { \varepsilon } = \bar { \psi } _ { - \varepsilon } ^ { - 1 } .$ In the case of a symmetric $\phi _ { h }$ this is equivalent to

$$
\begin{array} { r } { s ( \widehat { y } , - \varepsilon ) = s ( y , \varepsilon ) \qquad \mathrm { w i t h } \qquad \widehat { y } = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) . } \end{array}
$$

Reversibility.Thealgorithm(3.1）is called $\rho$ -reversibleif,whenapplied toa $\rho$ reversibledifferential equation, $\varPsi _ { \varepsilon } ( y )$ is $\rho$ -reversible,i.e., $\rho \circ \varPsi _ { \varepsilon } = \varPsi _ { \varepsilon } ^ { - 1 } \circ \rho$ (cf. Definition V.1.2).If the method $\phi _ { h }$ is $\rho$ -reversible then this is equivalent to

$$
\begin{array} { r } { s ( \rho ^ { - 1 } \widehat { y } , \varepsilon ) = s ( y , \varepsilon ) \qquad \mathrm { w i t h } \qquad \widehat { y } = \varPhi _ { \varepsilon s ( y , \varepsilon ) } ( y ) . } \end{array}
$$

Example 3.1.Aiming at step sizes $h \approx \varepsilon \sigma ( y )$ (cf.(2.2)）,Hut,Makino&McMillan (1995)propose the use of $\begin{array} { r } { s ( y , \varepsilon ) = \frac { 1 } { 2 } \big ( \sigma ( y ) + \sigma ( \widehat { y } ) \big ) } \end{array}$ where,as in Sect.VIII.2, $\sigma ( y )$ issome function that usesana priori knowledge of the solution of thedifferential equation.Notice that,becauseof $\widehat { y } = \phi _ { \varepsilon s ( y , \varepsilon ) } ( y )$ ,thevalue of $s ( y , \varepsilon )$ isdefined byanimplicit relation.Condition(3.3）is satisfied whenever $\varPhi _ { h } ( y )$ issymmetric, and(3.4）is satisfiedwhenever $\varPhi _ { h } ( y )$ is $\rho$ -reversibleand $\sigma ( \rho y ) = \sigma ( y )$ holds.Fora proof of these statements one shows that $s ( \widehat { y } , - \varepsilon )$ and $s ( y , \varepsilon )$ (resp. $s ( \rho ^ { - 1 } \widehat { y } , \varepsilon )$ and $s ( y , \varepsilon ) )$ are solution of the same nonlinear equation.

How can we find suitable step size functions $s ( y , \varepsilon )$ which satisfy all these properties,and whichdo not requireanyapriori knowledge of thesolution？Inaremarkablepublication,Stoffer（1995)gives thekeyto theanswerof thisquestion. Hesimply proposes to choose the step size $h$ in such a way that the local error estimatesatisfies $e r r = T o l$ （in contrast to $e r r \le T o l$ for the standard strategy).Let us explain this idea in some more detail forRunge-Kutta methods.

Example3.2 (Symmetric,Variable Step SizeRunge-Kutta Methods).For the numerical solution of $\dot { y } = f ( y )$ we consider Runge-Kutta methods

$$
Y _ { i } = y _ { n } + h \sum _ { j = 1 } ^ { s } a _ { i j } f ( Y _ { j } ) , \qquad y _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f ( Y _ { i } ) ,
$$

with coefficients satisfying $a _ { s + 1 - i , s + 1 - j } + a _ { i j } = b _ { j }$ for all $i , j$ Such methods are symmetric and reversible (cf.TheoremV.2.3).A common approach for step size controlistosideranembededeod $\begin{array} { r } { \widehat { y } _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } \widehat { b } _ { i } f ( Y _ { i } ) } \end{array}$ (which has the same internal stages $Y _ { i }$ ）andtotake thedifference $y _ { n + 1 } - { \hat { y } } _ { n + 1 } ,$ i.e.,

$$
D ( y _ { n } , h ) = h \sum _ { i = 1 } ^ { s } e _ { i } f ( Y _ { i } )
$$

with $e _ { i } = b _ { i } - { \widehat { b } } _ { i }$ as indicatorofthelocal error.Formethods where $Y _ { i } \approx y ( t _ { n } + c _ { i } h )$ (e.g.,collocation or discontinuous collocation） one usually computes the coefficients $e _ { i }$ fromanontrivial solution of the homogeneous linear system

$$
\sum _ { i = 1 } ^ { s } e _ { i } c _ { i } ^ { k - 1 } = \bar { 0 } \qquad \mathrm { f o r } \quad k = 1 , \ldots , s - \bar { 1 } .
$$

Thisyields $D ( y _ { n } , h ) = { \mathcal { O } } ( h ^ { r } )$ with $r$ close to $s$ .According to the suggestion of Stoffer(1995)we determine the step size $h _ { n + 1 / 2 }$ such that

$$
\| D ( y _ { n } , h _ { n + 1 / 2 } ) \| = T o l .
$$

A Taylor expansion around $h = 0$ shows that $D ( y , h ) = d _ { r } ( y ) h ^ { r } + { \mathcal O } ( h ^ { r + 1 } )$ with some $r \geq 1$ We assume $\lVert d _ { r } ( y ) \rVert \neq 0$ and we put $\varepsilon = T o l ^ { 1 / r }$ ,sothat $h _ { n + 1 / 2 }$ from (3.8)can be expressed by asmooth function $s ( y , \varepsilon )$ as (3.1).

Tosatisfythe symmetryrelation (3.3)we determine the $e _ { i }$ such that

$$
e _ { s + 1 - i } = e _ { i } \quad \mathrm { f o r ~ a l l ~ } i \qquad \mathrm { o r } \qquad e _ { s + 1 - i } = - e _ { i } \quad \mathrm { f o r ~ a l l ~ } i
$$

(Hairer& Stoffer 1997).If the Runge-Kutta method is symmetric,this then implies

$$
| | D ( y _ { n } , h ) | | = | | D ( y _ { n + 1 } , - h ) | | \qquad \mathrm { w i t h } \qquad y _ { n + 1 } = \varPhi _ { h } ( y _ { n } ) .
$$

This follows from the fact that the internal stage vectors $Y _ { i }$ of the step from $y _ { n }$ to $y _ { n + 1 }$ and the stage vectors $Y _ { i }$ of the step from $y _ { n + 1 }$ to $y _ { n }$ (negative step size $- h$ ） arerelated by $Y _ { i } = Y _ { s + 1 - i } .$ The step sizedetermined by(3.8) is thus the same for both steps and,consequently,condition(3.3)holds.

Thereversibilityrequirement(3.4)isaconsequence of

$$
| | D ( y _ { n } , h ) | | = | | D ( \rho ^ { - 1 } y _ { n + 1 } , h ) | | \qquad \mathrm { w i t h } \qquad y _ { n + 1 } = \varPhi _ { h } ( y _ { n } )
$$

which is satisfied for orthogonal mappings $\rho$ (i.e., $\rho ^ { T } \rho = I$ ).This is seenas follows: applying $\phi _ { h }$ to $\rho ^ { - 1 } y _ { n + 1 }$ gives $\rho ^ { - 1 } y _ { n }$ and theinternal stagesare $Y _ { i } = \rho ^ { - 1 } Y _ { s + 1 - i }$ Hence,we have from (3.9) that $D ( \rho ^ { - 1 } y _ { n + 1 } , h ) = \pm \rho ^ { - 1 } D ( y _ { n } , h )$ ,and (3.11） follows from the orthogonality of $\rho$

A simple special case is the trapezoidal rule

$$
y _ { n + 1 } = y _ { n } + { \frac { h _ { n \mp 1 / 2 } } { 2 } } { \Big ( } f ( y _ { n } ) + f ( y _ { n + 1 } ) { \Big ) }
$$

combined with

$$
D ( y _ { n } , h ) = { \frac { h } { 2 } } { \Big ( } f ( y _ { n + 1 } ) - f ( y _ { n } ) { \Big ) } .
$$

Thescalar nonlinear equation （3.8）for $h _ { n + 1 / 2 }$ can be solved in tandem with the nonlinear system (3.12).

Example 3.3 (Symmetric, Variable Step Size Stormer-Verlet Scheme).The strategy of Example 3.2can beextended ina straightforward waytopartitioned Runge-Kutta methods.For example,for the second order symmetric Stormer-Verlet scheme (I.1.17),applied to the problem ${ \dot { q } } = p$ , $\dot { p } = - \nabla U ( q ) .$ wecan take

$$
D ( p _ { n } , q _ { n , v } h ) = \frac { h } { 2 } \left( { { \nabla U ( q _ { n + 1 } ) - \nabla U ( q _ { n } ) } } \right)
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/adaad9b01a2871634b8381e9d0616a9ebdac66ae71c15d998aaaa4a6a396dd4b.jpg)  
Fig.3.1.Stormer-Verlet scheme appliedwith the symmetricadaptive step size strategy of Example3.3 $T o l = 0 . 0 1 $ the three pictures have the same meaningasin Fig.1.1

aserror indicator.The first component is just thedifference of the Stormer-Verlet solution and the numerical approximation obtained by the symplectic Eulermethod. The second component is a symmetrized version of it.

We apply this method with $h _ { n + 1 / 2 }$ determined by(3.8）and $T o l = 0 . 0 1$ tothe perturbed Keplerproblem（1.2) with initialvaluesas inFig.1.1.Theresult is given inFig.3.1.We identifyacorrect qualitative behaviour(compared to thewrongbehaviour for the standard step size strategyin Fig.1.1).It should bementioned that thework for solving the scalar equation (3.8) for $h _ { n + 1 / 2 }$ is not negligible,because theStormer-Verletschemeis explicit.Solving this equation iteratively,every iterationrequires one force evaluation $\nabla U ( q )$ .An efficient solver for this scalar nonlinearequation should be used.

ATwo-Step Proportional Controller.With theaim of obtaining acompletely explicitintegrator,Huang&Leimkuhler（1997）propose theuse of two-term recurrencerelations for the step size sequence,see also Holder,Leimkuhler&Reich (2001).Instead of usingarelation between $h _ { n + 1 / 2 }$ , $y _ { n }$ and $y _ { n + 1 }$ (cf.Example3.1) whichisnecessarilyimplicit,itissuggestedto usea symmetric relation.between $h _ { n - 1 / 2 }$ , $h _ { n + 1 / 2 }$ ,and $y _ { n }$ ,which then isexplicit.In particular,with thenotation $h _ { n + 1 / 2 } = \varepsilon s _ { n + 1 / 2 }$ ,it is proposed touse the two-term recurrence relation

$$
\frac { 1 } { s _ { n + 1 / 2 } } + \frac { 1 } { s _ { n - 1 / 2 } } = \frac { 2 } { \sigma ( y _ { n } ) } ,
$$

starting with $s _ { 1 / 2 } ~ = ~ \sigma ( y _ { 0 } )$ .Incombination with the Stormer-Verlet method for separableHamiltonians,thisalgorithm iscompletely explicit,and the authors report anexcellent performance for realistic problems.

Arigorous analysis ofthe long-timebehaviourof thisvariablestep size Stormer-Verletmethod ismuch moredifficult.Theresultsof Chapters IX and XI cannot be applied,because it is nota one-step mapping $y _ { n } \mapsto y _ { n + 1 }$ Theanalysis ofCirilli, Hairer&Leimkuhler（1999)shows that,similartoweaklystablemultistepmethods (Chap.XV),the numerical solution and the step size sequence contain oscillatory terms.Although these oscillations are usually very small (and hardlyvisible),it seems difcult to get rigorous estimates for them.

# VIII.3.2 Integrating,Reversible Controllers

Allvariable step size approaches of this chapter are based on some time transformation $t  \tau$ given by $\begin{array} { r } { \frac { d t } { d \tau } = \sigma ( y ) } \end{array}$ sothatthedrentialuation,xpresinte newtimevariable $\tau$ ,becomes

$$
y ^ { \prime } = { \frac { 1 } { z } } f ( y ) , \qquad z \sigma ( y ) = 1 .
$$

In Sect.VIII.2 we insert $z ^ { - 1 } = \sigma ( y )$ into the differential equation and apply anumerical method to $y ^ { \prime } = \sigma ( y ) f ( y ) .$ InSect.VIII.3.1we first discretizethe algebraic relation $z \sigma ( y ) = 1$ expressing $z _ { n + 1 / 2 }$ in terms of $y _ { n }$ and $y _ { n + 1 }$ ,and then apply a one-stepmethod to the differential equation in (3.14) assuming $z = z _ { n + 1 / 2 }$ being constant.

Inthepresent section we first differentiate the algebraic relation of (3.14)with respect to $\tau$ Thisyieldsby Leibniz'rule ${ z } ^ { \prime } { \sigma } ( y ) + { z } \nabla { \sigma } ( y ) ^ { T } y ^ { \prime } = 0$ sothat

$$
\begin{array} { r } { \boldsymbol { z } ^ { t } = G ( \boldsymbol { y } ) \qquad \mathrm { w i t h } \qquad G ( \boldsymbol { y } ) = - \displaystyle \frac { 1 } { \sigma ( \boldsymbol { y } ) } \nabla \sigma ( \boldsymbol { y } ) ^ { T } \boldsymbol { f } ( \boldsymbol { y } ) . } \end{array}
$$

Theidea of differentiating the constraint in(3.14） has been raised in Huang& Leimkuhler(1997),but soon abandoned in favourof thecontroller(3.13).The subsequent algorithm togetherwith itstheoretical justification iselaborated in Hairer &Soderlind(2oo4).The idea is to discretize first the differential equation in (3.15) andthen toapplya one-stepmethod totheproblem(3.14）with constant $z$ .The proposed algorithm is thus

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n - 1 / 2 } + \varepsilon G ( y _ { n } ) } } \\ { { y _ { n + 1 } } } & { { = } } & { { \Phi _ { \varepsilon / z _ { n + 1 / 2 } } ( y _ { n } ) } } \end{array}
$$

with $z _ { 1 / 2 } = z _ { 0 } + \varepsilon G ( y _ { 0 } ) / 2$ and $z _ { 0 } = 1 / \sigma ( y _ { 0 } ) .$ Thisalgorithm is explicit whenever the underlying one-step method $\varPhi _ { h } ( y )$ isexplicit.Itis called integrating controller, because the step size density is obtained by summingupsmall quantities.

Foratheoreticalanalysisitisconvenienttointroduce $z _ { n } = ( z _ { n + 1 / 2 } + z _ { n - 1 / 2 } ) / 2$ and towrite(3.16)asa one-step method for the augmented system

$$
y ^ { \prime } = { \frac { 1 } { z } } f ( y ) , \qquad z ^ { \prime } = G ( y ) .
$$

Notice that $I ( y , z ) = z \sigma ( y )$ isafirst integral ofthis system.

Algorithm3.4.Let $\varPhi _ { h } ( y )$ beaone-step method for $\dot { y } = f ( y )$ ， $y ( 0 ) = y _ { 0 }$ With $G ( y )$ given by(3.15）, $z _ { 0 } = 1 / \sigma ( y _ { 0 } )$ andconstant $\varepsilon$ welet

$$
\begin{array} { r c l } { { z _ { n + 1 / 2 } } } & { { = } } & { { z _ { n } + \varepsilon G ( y _ { n } ) / 2 } } \\ { { y _ { n + 1 } } } & { { = } } & { { \varPhi _ { \varepsilon / z _ { n + 1 / 2 } } ( y _ { n } ) } } \\ { { z _ { n + 1 } } } & { { = } } & { { z _ { n + 1 / 2 } + \varepsilon G ( y _ { n + 1 } ) / 2 . } } \end{array}
$$

Thevalues $y _ { n }$ approximate $y ( t _ { n } )$ where $t _ { n + 1 } = t _ { n } + \varepsilon / z _ { n + 1 / 2 }$

Thisalgorithm has an interestinginterpretation as Strang splitting for the solutionof(3.17):itapproximates the flow of $z ^ { \prime } = G ( y )$ with fixed $_ y$ overahalf-step $\varepsilon / 2$ ;thenappliesthemethod $\boldsymbol { \varPhi _ { \varepsilon } }$ to $y ^ { \prime } = f ( y ) / z$ with fixed $z$ ;finally,itcomputesa second half-step of $z ^ { \prime } = G ( y )$ with fixed $_ y$ .

With the notation

$$
{ \widehat { \boldsymbol { \phi } } } _ { \varepsilon } : { \left( \begin{array} { l } { y _ { n } } \\ { z _ { n } } \end{array} \right) } \mapsto { \left( \begin{array} { l } { y _ { n + 1 } } \\ { z _ { n + 1 } } \end{array} \right) } \qquad { \mathrm { a n d } } \qquad { \widehat { \boldsymbol { \rho } } } = { \left( \begin{array} { l l } { \rho } & { 0 } \\ { 0 } & { 1 } \end{array} \right) } .
$$

theAlgorithm 3.4 has thefollowingproperties：

$\hat { \varPhi } _ { \varepsilon }$ is symmetric whenever $\phi _ { h }$ is symmetric;   
$\hat { \varPhi } _ { \varepsilon }$ is reversible with respect to $\hat { \rho }$ whenever $\phi _ { h }$ is reversible with respect to $\rho$ and $G ( \rho y ) = - G ( y )$ (this is a consequence of $\sigma ( \rho y ) = \sigma ( y ) )$

Theseproperties imply that standard techniques for constant step size implementations can be applied to $\widehat { \varPhi } _ { \varepsilon }$ ,and thus yield insight into the variable step size algorithmof this section.Itwill be shown in Chap.XI that when applied to integrable reversible systems there isno drift in the action variablesand the global error grows onlylinearlywith time.Moreover,the firstintegral $I ( y , z ) = z \sigma ( y )$ ofthe system (3.17)isalso well preserved(without drift) for such problems.

Example3.5(Variable Step Size Stormer-Verlet method).Considera Hamiltoniansystem with separable Hamiltonian $H ( p , q ) \ = \ T ( p ) + U ( q )$ Using the Stormer-Verletmethodas basicmethod the abovealgorithm becomes(starting with $z _ { 0 } = 1 / \sigma ( y _ { 0 } )$ and $z _ { 1 / 2 } = z _ { 0 } + \varepsilon G ( p _ { 0 } , q _ { 0 } ) / 2 )$

$$
\begin{array} { r c l } { z _ { n + 1 / 2 } } & { = } & { z _ { n - 1 / 2 } + \varepsilon G ( p _ { n } , q _ { n } ) } \\ { p _ { n + 1 / 2 } } & { = } & { p _ { n } - \varepsilon \nabla U ( q _ { n } ) / ( 2 z _ { n + 1 / 2 } ) } \\ { q _ { n + 1 } } & { = } & { q _ { n } + \varepsilon \nabla T ( p _ { n + 1 / 2 } ) / z _ { n + 1 / 2 } } \\ { p _ { n + 1 } } & { = } & { p _ { n + 1 / 2 } - \varepsilon \nabla U ( q _ { n + 1 } ) / ( 2 z _ { n + 1 / 2 } ) . } \end{array}
$$

Thismethod isexplicit,symmetric and reversible as longas $G \rho ~ = ~ - G$ ,and computes approximations on a non-equidistant grid $\left\{ { { t } _ { n } } \right\}$ givenby $t _ { n + 1 } ~ = ~ t _ { n } ~ +$ $\varepsilon / z _ { n + 1 / 2 }$

Letusapply thismethod to the perturbed Kepler problem withdata and initial values as in the beginning of this chapter.Further,we select $\sigma ( q ) = ( q ^ { T } q ) ^ { \alpha / 2 }$ with $\alpha = 3 / 2$ ,sothat the control function(3.15) becomes

$$
G ( p , q ) = - \alpha p ^ { T } q / q ^ { T } q .
$$

Figure 3.2 shows the error in the Hamiltonian along the numerical solution as well asthe global error in the solution (fictive step size $\varepsilon = 0 . 0 2$ Theerror in the Hamiltonian is proportional to $\varepsilon ^ { 2 }$ without drift,and the global error grows linearly with time (in double logarithmic scale a linear growth corresponds toa line with slope one;such lines aredrawn in grey).This isqualitatively the same behaviouras observed in constant step size implementations of symplectic methods.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/b0eb4b7f2be58835ecb01a644b5c79fb06633a4c3cabd5433f899e3a322c086f.jpg)  
Fig.3.2.Numerical Hamiltonian and global errorasa function of time

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/645b19732c706e21563cf158f98e29f3dde4ce420909b2dc3b4fd74e7af7e334.jpg)  
Fig.3.3.Step sizes of the variable step size Stormer-Verlet method asa function of time,andthe control error $z _ { n } \sigma ( q _ { n } ) - z _ { 0 } \sigma ( q _ { 0 } )$ （grey curve）

Figure 3.3 shows the selected step sizes $h _ { n + 1 / 2 } = \varepsilon / z _ { n + 1 / 2 }$ asa function of time,and the control error $z _ { n } \sigma ( q _ { n } ) - z _ { 0 } \sigma ( q _ { 0 } )$ in grey.Since its deviation from the constant value $z _ { 0 } \sigma ( q _ { 0 } ) = 1$ issmall without any drift,the step density remains close to $1 / \sigma ( q )$ .Foran explanation of this excellent long-time behaviourwe refer to Sect.XI.3.

# VIII.4 Multiple Time Stepping

Acompletely different approachto variable step sizeswillbe described in this section.We are interested in situationswhere:

·many solution components of thedifferential equation vary slowly and only a few components have fast dynamics; or   
computationally expensive parts of the right-hand side do not contribute much to thedynamics of the solution.

Inthe first case itis tempting to use large step sizes for the slow components and small step sizes for the fast ones.Such integrators,called multirate methods,were first formulatedbyRice(196O)and Gear&Wells（1984).Theywere furtherdevelopedby Gunther&Rentrop(1993)inview ofapplications inelectriccircuit simulation,and by Engstler&Lubich（1997)with applicationsinastrophysics.Symmetric multirate methodsare obtained from theapproachesdescribed belowand are speciallyconstructed byLeimkuhler&Reich(2001).

The second case suggests the use of methods that evaluate the expensive part of thevector field less often than therest.Thisapproach iscalled multiple time stepping.Itwasoriginallyproposed forastronomyby Hayli（1967）and hasbecome verypopularinmoleculardynamics simulations(Streett,Tildesley& Saville 1978, Grubmuller,Heller,Windemuth&Schulten1991,Tuckerman,Berne&Martyna 1992).As noticed by Biesiadecki& Skeel (1993),one approach to such methods is within the framework of splitting and composition methods,which yields symmetricand symplectic methods.A second family of symmetric multiple time stepping methods results from the concept of using averaged force evaluations.

# VIII.4.1 Fast-Slow Splitting: the Impulse Method

Consideradifferential equation

$$
\dot { y } = f ( y ) , \qquad f ( y ) = f ^ { [ \mathrm { s l o w } ] } ( y ) + f ^ { [ \mathrm { f a s t } ] } ( y ) ,
$$

where the vector field is split into summands contributing to slow and fast dynamics,respectivelyndwhere $f ^ { \mathrm { [ s l o w ] } } ( y )$ ismoreexpensive toevaluate than $f ^ { \mathrm { { ( f a s t ) } } } ( y )$ . Multiratemethodscanoftenbecastintothisframework bycollectingin $f ^ { \mathrm { [ s l o w ] } } ( y )$ those components of $f ( y )$ which produce slow dynamics and in $f ^ { \mathrm { [ f a s t ] } } ( y )$ theremaining components.

Algorithm4.1.Foragiven $N \geq 1$ andfor thedifferentialequation(4.1) amultiple timesteppingmethodisobtainedfrom

$$
\big ( \boldsymbol { \varPhi } _ { h / 2 } ^ { [ \mathrm { s l o w } ] } \big ) ^ { * } \circ \big ( \boldsymbol { \varPhi } _ { h / N } ^ { [ \mathrm { f a s t } ] } \big ) ^ { N } \circ \boldsymbol { \varPhi } _ { h / 2 } ^ { [ \mathrm { s l o w } ] } ,
$$

whereslow] wher andfast aree $\dot { y } = f ^ { \left[ \mathrm { s l o w } \right] } ( y )$ ${ \dot { y } } = f ^ { \left[ \mathrm { f a s t } \right] } \left( y \right)$

ThemethodofAlgorithm4.1isalready stated insymmetrizedform（ $\boldsymbol { \varPhi } _ { h } ^ { * }$ denotes theadjoint of $\phi _ { h }$ ).Itisoftencalledtheimpulsemethod,because theslowpart $f ^ { \mathrm { [ s l o w ] } }$ ofthevector fieldisused-impulse-like-only at the beginningand at the end of the step,whereas the many small substepsin between are concerned solely through integrating the fastsystem $\dot { y } = f ^ { \mathrm { [ f a s t ] } } ( y )$ .

Lemma 4.2. Let $\bar { \Phi } _ { h } ^ { \lfloor s \log \rfloor }$ beanarbitrarymethodoforderl,and $\varPhi _ { h } ^ { [ \mathrm { f a s t } ] }$ asymmetric method oforder2.Then,themultipletime steppingalgorithm(4.2）issymmetric and of order2.

f $f ^ { \mathrm { [ s l o w ] } } ( y )$ and $f ^ { \mathrm { [ f a s t ] } } ( y )$ are Hamiltonian and if $\varPhi _ { h } ^ { [ \mathrm { s l o w } ] }$ and lfast] areboth symplectic,then themultiple time steppingmethodisalsosymplectic.

Proof.Due to the interpretation of multiple time stepping as composition methods the proof of these statements is obvious. □

Theorder statement ofLemma4.2isvalid for $h  0$ ,but should be taken with caution if the product of the step size $h$ witha Lipschitz constant of the problem isnotsmall (see Chap.XII fora detailedanalysis):itis not stated,and is not true in general for large $N$ ,thatif $h$ and $h / N$ are the step sizes needed to integrate the slowand fast system,respectively,withanerror bounded by $\succeq$ ,then the error of the combined scheme is $\mathcal { O } ( \varepsilon )$

Themost important application of multiple time stepping is in Hamiltonian systemswithaseparableHamiltonian

$$
H ( p , q ) = T ( p ) + U ( q ) , \qquad U ( q ) = U ^ { [ \mathrm { s l o w } ] } ( q ) + U ^ { [ \mathrm { f a s t } ] } ( q ) .
$$

Ifwe let the fast vector field correspond to $T ( p ) + U ^ { [ \mathrm { f a s t } ] } ( q )$ and the slow vector field to $U ^ { \left[ \mathrm { s l o w } \right] } \left( q \right)$ ,andifweapplytheStormer-Verletmethodandexactintegration, respectively,Algorithm4.1reads

$$
\varphi _ { h / 2 } ^ { [ \mathrm { s l o w } ] } \circ \left( \varphi _ { h / 2 N } ^ { [ \mathrm { f a s t } ] } \circ \varphi _ { h / N } ^ { T } \circ \varphi _ { h / 2 N } ^ { [ \mathrm { f a s t } ] } \right) ^ { N } \circ \varphi _ { h / 2 } ^ { [ \mathrm { s l o w } ] } ,
$$

where $\varphi _ { t } ^ { T } , \varphi _ { t } ^ { [ \mathrm { s l o w } ] } , \varphi _ { t } ^ { [ \mathrm { f a s t } ] }$   
$T ( p ) , U ^ { [ \mathrm { s l o w } ] } ( q ) , U ^ { [ \mathrm { f a s t } ] } ( q )$ $N = 1$   
(4.4)reduces to the Stormer-Verlet scheme applied to the Hamiltonian system with $H ( p , q )$ This isaconsequenceof thefactthat $\varphi _ { t } ^ { [ \mathrm { f a s t } ] } \circ \varphi _ { t } ^ { [ \mathrm { s l o w } ] } = \varphi _ { t } ^ { U }$ is the exact flow of the Hamiltonian system corresponding to $U ( q )$ of(4.3）.In the molecular dynamicsliterature,themethod(4.4)isknownastheVerlet-Imethod(Grubmuller etal.1991,who consider the method with little enthusiasm）orr-RESPA method (Tuckerman et al.1992,with much more enthusiasm).

Example 4.3.In order to illustrate the effect of multiple time steppingwe choose a ‘solarsystem'with twoplanets,i.e.,withaHamiltonian

$$
H ( p , q ) = \frac { 1 } { 2 } \Big ( \frac { p _ { 0 } ^ { T } p _ { 0 } } { m _ { 0 } } + \frac { p _ { 1 } ^ { T } p _ { 1 } } { m _ { 1 } } + \frac { p _ { 2 } ^ { T } p _ { 2 } } { m _ { 2 } } \Big ) - \frac { m _ { 0 } m _ { 1 } } { \lVert q _ { 0 } - q _ { 1 } \rVert } - \frac { m _ { 0 } m _ { 2 } } { \lVert q _ { 0 } - q _ { 2 } \rVert } - \frac { m _ { 1 } m _ { 2 } } { \lVert q _ { 1 } - q _ { 2 } \rVert }
$$

where $m _ { 0 } = 1 , m _ { 1 } = m _ { 2 } = 1 0 ^ { - 2 }$ and initial values $q _ { 0 } = ( 0 , 0 )$ ， $\dot { q } _ { 0 } = ( 0 , 0 )$ , $q _ { 1 } = ( 1 , 0 )$ ， $\dot { q } _ { 1 } = ( 0 , 1 )$ , $q _ { 2 } = ( 4 , 0 )$ , $\dot { q } _ { 2 } = ( 0 , 0 . 5 )$ With thesedata,the motion of the two planets is nearly circular with periods close to $2 \pi$ and $1 4 \pi$ ,respectively.

We split the potential as

$$
U ^ { [ \mathrm { { f a s t } } ] } ( q ) = - \frac { m _ { 0 } m _ { 1 } } { \| q _ { 0 } - q _ { 1 } \| } , \qquad U ^ { [ \mathrm { s l o w } ] } ( q ) = - \frac { m _ { 0 } m _ { 2 } } { \| q _ { 0 } - q _ { 2 } \| } - \frac { m _ { 1 } m _ { 2 } } { \| q _ { 1 } - q _ { 2 } \| } ,
$$

andweapply thealgorithm of（4.4）with $N = 1$ (Stormer-Verlet）, $N = 4$ ,and $N = 8$ Since the evaluation of $\varphi _ { t } ^ { [ \mathrm { s l o w } ] }$ isabout twice as expensive ast $\varphi _ { t } ^ { [ \mathrm { f a s t } ] }$ and thatof $\varphi _ { t } ^ { x }$ isofnegligible cost,thecomputational work of applying（4.4） onafixed interval isproportional to

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/e534411f806bdfbe8418bc5bdcfe5627350d39d3bc6cae317304494bccf4ee33.jpg)  
Fig.4.1.Maximal error in the Hamiltonianasa function of computational work

$$
{ \frac { 2 \pi } { h } } \cdot { \frac { ( 2 + N ) } { 3 } } .
$$

Ourcomputations have shown that this measure of work corresponds very well to the actual cpu time.

Wehave solved this problemwith many different step sizes $h$ Figure4.1shows themaximal error in theHamiltonian (over the interval $[ 0 , 2 0 0 \pi ]$ asafunction of thecomputational work(4.5).We notice that the value $N \ = \ 4$ yields excellent resultsforrelatively large aswell assmall step sizes.It noticeably improves the performance of the Stormer-Verlet method.If $N$ becomes too large,anirregular behaviourforlarge step sizes isobserved.Such“artificial resonances”are notorious forthismethodand havebeendiscussedbyBiesiadecki&Skeel(1993)forasimilar experiment;also see Chap.XIII.For large $N$ we also note a loss of accuracy for small step sizes.The optimal choice of $N$ (which here isclose to 4) depends on the problem and on the splitting into fastand slow parts,and has to be determined by experiment.

Themultiple time stepping technique can be iteratively extended to problems withmore than two different time scales.The idea is to split the‘fastvector field of(4.1） into $f ^ { \vert \mathrm { f a s t } \vert } ( y ) = f ^ { \vert f f \vert } ( y ) + f ^ { \vert f s \vert } ( y )$ ,and toreplace themethod $\bar { \Phi } _ { h } ^ { [ \mathrm { f a s t } ] }$ in Algorithm 4.1withamultiple time steppingmethod.Depending on theproblem,a significant gain incomputer time may be achieved in thisway.

Manymore multiple time stepping methods that extend the above Verlet-I/r-RESPA/impulse method,have been proposed in the literature,most notably the mollified impulse method of Garcia-Archilla,Sanz-Serna & Skeel (1999)；see Sect. XIII.1.

# VIII.4.2 Averaged Forces

Adifferent approach to multiple time stepping arises from the idea of advancing the stepwith averaged forceevaluations.We describesuchamethod forthe secondorder equation

$$
\ddot { y } = f ( y ) , \qquad f ( y ) = f ^ { [ \mathrm { s l o w } ] } ( y ) + f ^ { [ \mathrm { f a s t } ] } ( y ) .
$$

The exact solution satisfies

$$
y ( t + h ) - 2 y ( t ) + y ( t - h ) = h ^ { 2 } \int _ { - 1 } ^ { 1 } ( 1 - | \theta | ) f { \big ( } y ( t + \theta h ) { \big ) } d \theta ,
$$

where the integral on theright-hand side represents a weighted average of the force along the solution,which is now going to be approximated.At $t = t _ { n }$ ,wereplace

$$
f \big ( y ( t _ { n } + \theta h ) \big ) \approx f ^ { \mathrm { [ s l o w ] } } ( y _ { n } ) + f ^ { \mathrm { [ f a s t ] } } \big ( u ( \theta h ) \big )
$$

where $u ( \tau )$ isasolution of thediferential equation

$$
\ddot { u } = f ^ { \mathrm { [ s l o w ] } } ( y _ { n } ) + f ^ { \mathrm { [ f a s t ] } } ( u ) .
$$

Wethen have

$$
\begin{array} { r } { h ^ { 2 } \displaystyle \int _ { - 1 } ^ { 1 } ( 1 - | \theta | ) \Big ( f ^ { [ \mathrm { s l o w } ] } ( y _ { n } ) + f ^ { [ \mathrm { f a s t } ] } \big ( u ( \theta h ) \big ) \Big ) d \theta = u ( h ) - 2 u ( 0 ) + u ( - h ) . } \end{array}
$$

The velocitiesare treated similarly,starting from the identity

$$
{ \dot { y } } ( t + h ) - { \dot { y } } ( t - h ) = h \int _ { - 1 } ^ { 1 } f { \big ( } y ( t + \theta h ) { \big ) } d \theta ~ .
$$

ASymmetric Two-StepMethod.For the differential equation（4.7）we assume the initial values

$$
u ( 0 ) = y _ { n } , \quad \dot { u } ( 0 ) = \dot { y } _ { n } .
$$

This initial value problemissolved numerically,e.g.,bythe Stormer-Verletmethod with a smaller step size $\pm h / N$ onthe interval $[ - h , h ]$ ,yieldingnumerical approximations $u _ { N } ( \pm h )$ and $\upsilon _ { N . } ( \pm h )$ to $u ( \pm h )$ and $\dot { u } ( \pm h )$ ,respectively.Note that no further evaluations of $f ^ { \mathrm { [ s l o w ] } }$ areneeded for the computation of $u _ { N } ( \pm h )$ and $v _ { N } ( \pm h )$ . This finally givesthe symmetric two-stepmethod(Hochbruck&Lubich 1999a)

$$
\begin{array} { r c l } { { y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } } } & { { = } } & { { u _ { N } ( h ) - 2 u _ { N } ( 0 ) + u _ { N } ( - h ) } } \\ { { } } & { { } } & { { } } \\ { { \dot { y } _ { n + 1 } - \dot { y } _ { n - 1 } } } & { { = } } & { { v _ { N } ( h ) - v _ { N } ( - h ) . } } \end{array}
$$

The starting values $y _ { 1 }$ and $\dot { y } _ { 1 }$ are chosen as $u _ { N } ( h )$ and $v _ { N } ( h )$ which correspond to (4.7）and(4.8）for $n = 0$ ,.

ASymmetric One-step Method.An explicit one-step method with similar averaged forcesisobtainedwhen theinitial values for(4.7)are chosenas

$$
u ( 0 ) = y _ { n } , \quad \dot { u } ( 0 ) = 0 .
$$

Itmayappear crude to take zeroinitial values for the velocity,butweremark that for linear $f ^ { \mathrm { [ f a s t ] } }$ theaveraged force $( u ( h ) - 2 u ( 0 ) + u ( - h ) ) / h ^ { 2 }$ does not depend on the choice of ${ \dot { u } } ( 0 )$ Moreover the solution then satisfies $u ( - t ) = u ( t )$ sothat the computational cost is halved.We again denote by $u _ { N } ( h ) = u _ { N } ( - h )$ thenumerical approximation to $u ( h )$ obtained with step size $\pm h / N$ from a one-step method (e.g., fromthe Stormer-Verlet scheme).Because of(4.1O) the averaged forces

$$
F _ { n } = { \frac { 1 } { h ^ { 2 } } } \left( u _ { N } ( h ) - 2 u _ { N } ( 0 ) + u _ { N } ( - h ) \right) = { \frac { 2 } { h ^ { 2 } } } \left( u _ { N } ( h ) - u _ { N } ( 0 ) \right)
$$

now depend only on $y _ { n }$ and not on thevelocity $\dot { y } _ { n }$ .Intrustworthy Verlet manner, the scheme $y _ { n + 1 } - 2 y _ { n } + y _ { n - 1 } = h ^ { 2 } F _ { n }$ can bewritten as the one-step method

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle v _ { n + 1 / 2 } = ~ v _ { n } + \frac { h } { 2 } F _ { n } } } \\ { { } } & { { } } & { { \displaystyle y _ { n + 1 } = ~ y _ { n } + h v _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { \displaystyle v _ { n + 1 } = ~ v _ { n + 1 / 2 } + \frac { h } { 2 } F _ { n + 1 } ~ , } } \end{array}
$$

Theauxiliaryvariables $\upsilon _ { n }$ canbeinterpreted as averaged velocities:we have

$$
v _ { n } = { \frac { y _ { n + 1 } - y _ { n - 1 } } { 2 h } } \approx { \frac { y ( t _ { n + 1 } ) - y ( t _ { n - 1 } ) } { 2 h } } = { \frac { 1 } { 2 } } \int _ { - 1 } ^ { 1 } { \dot { y } } ( t _ { n } + \theta h ) d \theta ~ .
$$

Thisaverage may differ substantially from $\dot { y } ( t _ { n } )$ if the solution is highly oscillatory in $[ - h , h ]$ In the experiments of this section it turned out that the choice $v _ { 0 } = \dot { y } _ { 0 }$ and ${ \dot { y } } _ { n } = v _ { n }$ asvelocity approximations gives excellent results.

Ina multirate context,symmetric one-step schemesusing averaged forces werestudiedbyHochbruck&Lubich（1999b),Nettesheim&Reich(1999),and Leimkuhler&Reich(2oo1).Aclosely related approach forproblemswithmultiple timescalesis the heterogeneousmultiscalemethod byE(2oo3)and Engquist& Tsai (2005).

Example 4.4.We addasatellite of mass $m _ { 3 } = 1 0 ^ { - 4 }$ to the three body-problem of Example4.3.It movesrapidlyaround theplanet number one.The initial positions and velocities are $q _ { 3 } = ( 1 . 0 1 , 0 )$ and $p _ { 3 } = ( 0 , 0 )$ We split the potential as

$$
U ^ { [ \mathrm { f a s t } ] } ( q ) = - \frac { m _ { 1 } m _ { 3 } } { \lVert q _ { 1 } - q _ { 3 } \rVert } , \qquad U ^ { [ \mathrm { s l o w } ] } ( q ) = - \sum _ { \stackrel { i < j } { ( i , j ) \neq ( 1 , 3 ) } } \frac { m _ { i } m _ { j } } { \lVert q _ { i } - q _ { j } \rVert } ,
$$

andwe apply themethods (4.9),(4.11),and the impulse method (4.4).Since the sumin $U ^ { \left[ \mathrm { { s l o w } } \right] }$ contains 5 terms,the computational work is proportional to

$$
\begin{array} { l l } { { \displaystyle { \frac { 5 + N } { 6 h } } } } & { { \mathrm { f o r } \mathrm { m e t h o d s } ( 4 . 1 1 ) \mathrm { a n d } ( 4 . 4 ) } } \\ { { \displaystyle { \frac { 6 + 2 N } { 6 h } } } } & { { \mathrm { f o r } \mathrm { m e t h o d } ( 4 . 9 ) . } } \end{array}
$$

Foreach of the methodswe have optimizedthe number $N$ ofsmall steps.We obtaineda flatminimum near $N = 4 0$ for(4.9） and(4.4),and a morepronounced minimumat $N = 1 2$ for(4.11).Figure4.2shows the errorsat $t = 1 0$ in the positionsand in the Hamiltonianasa function of the computational work.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/e0328cc4aea977061c2ef2956146f18a2c27b0432e41960886e8fe0aaf7bc951.jpg)  
Fig.4.2.Errors in position and in the Hamiltonianasa function of the computational work; theclassical Stormer-Verletmethod,the impulsemethod(4.4),andtheaveraged forcemethods(4.11) and(4.9).The errors in the Hamiltonianare indicatedby grey lines(same linestyle)

Theerrorin the position islargest for the Stormer-Verlet method and significantlysmallest for theone-stepaveraged-forcemethod(4.11).The errorsinthe velocitiesareabouta factor 1oo largerforallmethods.Theyarenot included in thefigure.The error in the Hamiltonianis very similar for all methodswith the exception of the two-stepaveraged-force method (4.9),for which it is much larger.

# VIII.5 Reducing Rounding Errors

..the idea is to capture the rounding errors and feed them back into the summation. （N.J.Higham1993）

All numerical methods for solving ordinary differential equations require thecomputation of arecursion of the form

$$
y _ { n + 1 } = y _ { n } + \delta _ { n } ,
$$

where $\delta _ { n }$ ,theincrement,isusuallysmallerinmagnitude thantheapproximation $y _ { n }$ to the solution.In this situation the rounding errors caused by the computation of $\delta _ { n }$ are in general smaller than those due to theaddition in (5.1).

Afirst attempt at reducing the accumulation of rounding errors (in fixed-point arithmetic forhisRunge-Kutta code）wasdue to Gill（1951）.Kahan（1965）and Moller（1965) both extended this idea to floating point arithmetic.The resulting algorithmisnowadayscalled‘compensated summation’,and aparticularly nicepresentationandanalysisis givenbyN.Higham(1993).In the followingalgorithmwe assume that $y _ { n }$ isa scalar;vector valued recursions are treated componentwise.

Algorithm5.1 (Compensated Summation). Let $y _ { 0 }$ and $\{ \delta _ { n } \} _ { n \geq 0 }$ be given and put $e = 0$ Compute $y _ { 1 } , y _ { 2 } , \ldots$ from(5.1)asfollows:

$$
{ \begin{array} { r l } & { f o r \ n = 0 , 1 , 2 , \dots \ d o } \\ & { \ a = y _ { n } } \\ & { \ e = e + \delta _ { n } } \\ & { y _ { n + 1 } = a + e } \\ & { \ e = e + ( a - y _ { n + 1 } ) } \\ & { e n d \ d o } \end{array} }
$$

Thisalgorithm can best be understood with the help of Fig.5.1 (following the presentation of N.Higham(1993)).We present the mantissas of floating point numbers by boxes,for which the horizontal position indicates the exponent (fora large exponent the box ismore to the left).The mantissas of $y _ { n }$ and $e$ togetherrepresent theaccurate value of $y _ { n }$ （notice that in the beginning $e = 0$ .Theoperationsof Algorithm5.1yield $y _ { n + 1 }$ andanew $e$ which together represent $y _ { n + 1 } = y _ { n } + \delta _ { n }$ No digit of $\delta _ { n }$ islost in thisway.Witha standard summation the last digits of $\delta _ { n }$ (those indicated by $\delta ^ { \prime \prime }$ inFig.5.1）would have beenmissed.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/468a261368e639014b8e78498ef8492f397ecc64ecd2169672bea9f0cc2d4cf8.jpg)  
Fig.5.1.Illustration of the technique of"compensated summation"

Numerical Experiment.We study the effect of compensated summation on the Keplerproblem(I.2.2) (writtenasafirst order system)with eccentricity $e = 0 . 6$ andinitial valuesasin(I.2.11）,so that theperiod of the elliptic orbitisexactly $2 \pi$ Asthenumerical integrator we take the composition method(V.3.13） of order 8with the Stormer-Verlet scheme as basic integrator.We compute the numerical solution with step size $h = 2 \pi / 5 0 0$ oncewith standard update of the increment, oncewith compensated summation (both in double precision）and,in order to geta reference solution,we also perform the whole computation in quadruple precision. The difference between the double and quadruple precision computations gives us therounding errors.Their Euclidean normsasa function of timeare displayed in Fig.5.2.

Wesee that throughout the whole integration interval the rounding errors of the standard implementationarenearlya factor of1oo larger than those of theimplementation with compensated summation.This corresponds to the inverse of the step size or,more precisely,to the mean quotient between $y _ { n }$ and $\delta _ { n }$ in(5.1）.InFig.5.2 wehave also included the pure global error of the method(without rounding errors） atintegral multiples of the period $2 \pi$ (henceno oscillationsare visible).This is obtained as the difference of the numerical solution computed with quadruple precisionand the exact solution.We observea linear growth of thepure global error (thiswill be explained in Sect.X.3)anda growth like $\mathcal { O } ( t ^ { 3 / 2 } )$ due to the rounding errors.Thus,eventually the rounding errorswill surpass the truncation errors,but this happens for the compensated summation only after some 1ooo periods.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/947181b58bd9028ecd71dd2a1648f7fa0e27c7d3ce7958e6c9dcce83a1d6a012.jpg)  
Fig.5.2.Rounding errors and pure global error asa function of time;the parallel grey lines indicatea growth of $\mathcal { O } ( t ^ { 3 / 2 } )$

Probabilistic Explanation of the Error Growth.Our aim is to explain the growth rateof rounding errors observed in Fig.5.2.Denote by $\varepsilon _ { k }$ thevector of rounding errorsproduced during the computations in the kth step.Since the derivative of the flow $\varphi _ { t } ( y )$ describes the propagation of these errors,the accumulated rounding error attime $t = t _ { N }$ （ $t _ { k } = k h$ )is

$$
\eta _ { t } = \sum _ { k = 1 } ^ { N } \varphi _ { t - t _ { k } } ^ { \prime } ( y _ { k } ) \varepsilon _ { k } .
$$

FortheKeplerproblemand,infact,forallcompletelyintegrabledifferential equations(cf.Sect.X.1) the flow and itsderivative grow at most linearlywith time,i.e.,

$$
\left\| \varphi _ { t - t _ { k } } ^ { \prime } ( y ) \right\| \leq a + b ( t - t _ { k } ) \qquad { \mathrm { f o r } } \quad t \geq t _ { k } .
$$

Using $\varepsilon _ { k } = \mathcal { O } ( e p s )$ ,where eps denotes the roundoff unit of the computer,an applicationof the triangleinequalityto(5.2)yields $\eta _ { t } = \mathcal { O } ( t ^ { 2 } e p s ) .$ From our experiment ofFig.5.2we see that such an estimate is too pessimistic.

Fora better understanding of accumulated rounding errors over long time intervalswe makeuse of probability theory.Such an approach has been developed in theclassical book of Henrici (1962).We assume that the components $\mathbf { \xi } \in k \mathbf { \overset { . } { 2 } }$ of $\varepsilon _ { k }$ are randomvariableswithmeanand variance

$$
E ( \varepsilon _ { k i } ) = 0 , \qquad V a r ( \varepsilon _ { k i } ) = C _ { k i } \cdot e p s ^ { 2 } ,
$$

and uniformly bounded $C _ { k i } \leq C .$ For simplicity we assume that all $\varepsilon _ { k i }$ areindependentrandom variables.Replacing the matrix $\varphi _ { t - t _ { k } } ( y _ { k } )$ in (5.2)with $\varphi _ { t - t _ { k } } \bigl ( y ( t _ { k } ) \bigr )$

and denoting its entries by $w _ { i j k }$ ,the $i$ th component of the accumulated rounding error(5.2）becomes

$$
\eta _ { t i } = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { n } w _ { i j k } \varepsilon _ { k j } ,
$$

a linear combination of therandomvariables $\varepsilon _ { k j }$ .Elementaryprobability theory thus implies that

$$
E ( \eta _ { t i } ) = 0 \qquad \mathrm { a n d } \qquad V a r ( \eta _ { t i } ) = \sum _ { k = 1 } ^ { N } \sum _ { j = 1 } ^ { n } w _ { i j k } ^ { 2 } V a r ( \varepsilon _ { k j } ) .
$$

Inserting theestimate (5.3) for $w _ { i j k }$ we get

$$
V a r \left( \eta _ { t i } \right) \le \sum _ { k = 1 } ^ { N } \left( a + b ( t - t _ { k } ) \right) ^ { 2 } \operatorname* { m a x } _ { j = 1 , \ldots , n } V a r \left( \bar { \varepsilon } _ { k j } \right) = \mathcal { O } \Bigl ( \frac { C } { h } t ^ { 3 } e p s ^ { 2 } \Bigr ) .
$$

Consequently,the Euclidean norm of the expected rounding error $\eta _ { t }$ is

$$
\left( \sum _ { i = 1 } ^ { n } V a r \left( \eta _ { t i } \right) \right) ^ { 1 / 2 } = \mathcal { O } \left( \sqrt { \frac { C } { h } } t ^ { 3 / 2 } e p s \right) .
$$

This is in excellent agreement with the results displayed in Fig.5.2.

# VIII.6 Implementation of ImplicitMethods

Symplecticmethods for general Hamiltonian equationsare implicit,and so are symmetric methods for general reversible systems.Also,whenwe consider variable step sizeextensions asdescribed in SectionsVII.3and VIII.2,we are led to nonlinear equations.The efficient numerical solution of such nonlinear equations is the main difficultyinan implementation of implicit methods.Notice that in the context of geometric integration thereis no need of ad-hoc strategies for step size and order selection,so that the remaining parts of a computer code are more or less straightforward.

In the following we discuss the numerical solution of the nonlinear system defined by an implicit Runge-Kutta method.Wehave the Gauss methods ofSect.II.1.3 inmind which are symplectic and symmetric.An extension of the ideas to partitionedRunge-Kuttamethodsand to Nystrommethodsis obvious.For simplicity of notation we consider autonomous differential equations ${ \dot { y } } = f ( y ) ,$ andwewrite thenonlinear system of Definition II.1.1 inthe form

$$
Z _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } f { \big ( } y _ { n } + Z _ { j n } { \big ) } = 0 , \qquad i = 1 , . . . , s .
$$

The unknown variables are $\mathcal { L } _ { 1 n } , \ldots , \mathcal { L } _ { s n }$ ,and theequivalence ofthetwo formulations isvia therelation $k _ { i } = f \left( y _ { n } + Z _ { i n } \right) .$ Thenumerical solution after one step can be expressed as

$$
y _ { n + 1 } = y _ { n } + h \sum _ { i = 1 } ^ { s } b _ { i } f \bigl ( y _ { n } + Z _ { i n } \bigr ) .
$$

Forimplicit Runge-Kutta methods the equations (6.1） represent a nonlinear system that has to be solved iteratively.We discuss thechoice of good starting approximations for $\boldsymbol { Z } _ { i n }$ aswell as different nonlinear equation solvers (fixed-point iteration, modifiedNewton methods).

# VIII.6.1 Starting Approximations

Themost simple approximations to the solution $Z _ { i n }$ of (6.1）are $Z _ { i n } ^ { 0 } ~ = ~ 0$ or $Z _ { i n } ^ { 0 } ~ = ~ h c _ { i } f ( y _ { n } )$ where $c _ { i } = \textstyle \sum _ { j = 1 } ^ { s } a _ { i j }$ Teyeow and we will try to exploit the information of previous steps for improving them. Thereare essentially two possibilities:either use only the information of the last step $y _ { n - 1 } \mapsto y _ { n }$ （methods（A）and(B）below）,orconsidera fixed $i$ anduse the interpolation polynomial that passes through $\angle i , n - l$ for $l = 1 , 2 , \ldots$ (method(C)）. Letusseparatelydiscuss these twoapproaches.

(A)Use of Continuous Output.Consider the polynomial $w _ { n - 1 } ( t )$ ofdegree $s$ that interpolates the values $( t _ { n - 1 } , y _ { n - 1 } )$ and $( t _ { n - 1 } + c _ { i } h , Y _ { i , n - 1 } )$ for $i = 1 , \dots , s$ ,where $Y _ { i , n - 1 } = y _ { n - 1 } + Z _ { i , n - 1 }$ istheargument in (6.1) of theprevious step.For collocation methods (such as Gauss methods) $w _ { n - 1 } ( t )$ is the collocation polynomial,and we knowfrom Lemma II.1.6 that oncompact intervals

$$
w _ { n - 1 } ( t ) - y ( t ) = \mathcal { O } ( h ^ { q + 1 } )
$$

with $q = s$ ,where $y ( t )$ denotes the solution of $\dot { y } = f ( y )$ satisfying $y ( t _ { n - 1 } ) = y _ { n - 1 }$ . ForRunge-Kutta methods that are not collocation methods,(6.3)holdswith $q$ defined by the condition $C ( q )$ of(II.1.11).Since the solution of $\dot { y } = f ( y )$ passing through $y ( t _ { n } ) ~ = ~ y _ { n }$ is $\mathcal { O } ( h ^ { p + 1 } )$ closeto $y ( t )$ with $p \ \geq \ q$ ,wehave $w _ { n } ( t ) \ =$ $w _ { n - 1 } ( t ) + \mathcal { O } ( h ^ { q + 1 } )$ and the computablevalue

$$
Z _ { i n } ^ { 0 } = Y _ { i n } ^ { 0 } - y _ { n } , \qquad Y _ { i n } ^ { 0 } = w _ { n - 1 } ( t _ { n } + c _ { i } h )
$$

servesas starting approximation for(6.1）with an error of size $\mathcal { O } ( h ^ { q + 1 } )$ Thisapproachis standard in variable step size implementations of implicit Runge-Kutta methods(cf.Sect.IV.8ofHairer&Wanner(1996)).Since $w _ { n - 1 } ( t ) - y _ { n - 1 }$ isalinear combination of the $Z _ { i , n - 1 } = Y _ { i , n - 1 } - y _ { n - 1 } ,$ itfollows from(6.1）that itisalso a linear combination of $h f ( Y _ { i , n - 1 } )$ ,sothat

$$
Y _ { i n } ^ { 0 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } f ( Y _ { j , n - 1 } ) .
$$

For a constant step size implementation,the $\beta _ { i j }$ depend only onthe method coefficientsand can be computedinadvanceasthe solution of the linear Vandermonde typesystem

$$
\sum _ { j = 1 } ^ { s } \beta _ { i j } c _ { j } ^ { k - 1 } = \frac { ( 1 + c _ { i } ) ^ { k } } { k } , \qquad k = 1 , \ldots , s
$$

(see Exercise 2).For collocation methods and for methods with $q ~ \geq ~ s - 1$ the coefficients $\beta _ { i j }$ from(6.6)are optimal in the sense that they are the only ones making (6.5)an sth order approximation to the solution of(6.1).For $q \ < \ s - 1$ ,more complicated order conditions have to be considered(Sand 1992).

(B)Starting Algorithms Using Additional Function Evaluations.In particular for high order methodswhere $s$ isrelatively large,a much more accurate starting approximationcan be constructed with the aid ofa few additional function evaluations.Such startingalgorithms have been investigated by Laburta(1997),who presents coefficients for the Gauss methodsup to order8inLaburta(1998).

The idea is to use starting approximations of the form

$$
Y _ { i n } ^ { 0 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } f ( Y _ { j , n - 1 } ) + h \sum _ { j = 1 } ^ { m } \nu _ { i j } f ( Y _ { s + j , n - 1 } ) ,
$$

where $Y _ { 1 , n - 1 } , \dots , Y _ { s , n - 1 }$ arethe internal stages of the basic implicit Runge-Kutta method(with coefficients $c _ { i } , a _ { i j } , b _ { j } )$ ,and theadditionalinternal stagesare computed from

$$
Y _ { s + i , n - 1 } = y _ { n - 1 } + h \sum _ { j = 1 } ^ { s + i - 1 } \mu _ { i j } f ( Y _ { j , n - 1 } ) .
$$

Forafixed $i$ ,weinterpret $Y _ { i n } ^ { 0 }$ as the result of the explicit Runge-Kutta method with coefficients of therighttableau of

$$
\begin{array} { r } { \frac {  { c } } { \vert \vert + c \vert } \left. \begin{array} { l } { A } \\ { B } \\ { b ^ { T } } \end{array} \right.  { a } \quad \quad \quad \quad \quad \quad \frac {  { a } \vert \vert M _ { 1 } } { \beta _ { i } ^ { T } } \ k _ { i } ^ { T } } \end{array}
$$

Here, $( M _ { 1 } , M _ { 2 } ) = M = ( \mu _ { j k } )$ $\begin{array} { r } { \mu _ { j } = \sum _ { k = 1 } ^ { s + j - 1 } \mu _ { j k } } \end{array}$ and $c , \mu , \beta _ { i } , \nu _ { i }$ are the vectors composed of $c _ { j } , \mu _ { j } , \beta _ { i j } , \nu _ { i j }$ respectively.The exact stage values $Y _ { i n }$ are interpreted astheresult of the Runge-Kutta method with coefficients given in the left tableau of(6.8).The entries of the vectors $\mathbb { 1 } , b$ and $a _ { i }$ are $1 , b _ { j }$ and $a _ { i j }$ ,respectively,and $B$ is thematrix whose rows areall equal to $b ^ { T }$ .

Ifthe orderconditions(see Sect.III.1) for the two Runge-Kutta methods of(6.8) give the same result for all trees with $\leq r$ vertices,we get an approximation of order $r$ ,i.e., $Y _ { \ i n } ^ { 0 } - Y _ { i n } = \mathcal { O } ( h ^ { r + 1 } ) ,$ For the bushy tree $\tau _ { k } = [ \circ , \ldots , \bullet ]$ with $k$ vertices wehave

$$
\sum _ { j = 1 } ^ { s } \beta _ { i j } c _ { j } ^ { k - 1 } + \sum _ { j = 1 } ^ { m } \nu _ { i j } \mu _ { j } ^ { k - 1 } = \sum _ { j = 1 } ^ { s } b _ { j } c _ { j } ^ { k - 1 } + \sum _ { j = 1 } ^ { s } a _ { i j } ( 1 + c _ { j } ) ^ { k - 1 } .
$$

Notice that for collocation methods (such as the Gauss methods) the condition $C ( s )$ reduces the right-hand expression of this equation to $( 1 + c _ { i } ) ^ { k } / k$ for $k \leq s$ For $m = 0$ ,these conditions are thus equivalent to (6.6).

For the tree $[ \tau _ { k } ] = [ [ \circ , \ldots , \circ ] ]$ with $k + 1$ vertices we get thecondition

$$
\begin{array} { r l r } {  { \sum _ { j , l = 1 } ^ { s } \beta _ { i j } a _ { j l } c _ { l } ^ { k - 1 } + \sum _ { j = 1 } ^ { m } \nu _ { i j } \Big ( \sum _ { l = 1 } ^ { s } \mu _ { j l } c _ { l } ^ { k - 1 } + \sum _ { l = 1 } ^ { m } \mu _ { j , s + l } \mu _ { l } ^ { k - 1 } \Big ) } } \\ & { } & { \equiv \sum _ { j , l = 1 } ^ { s } b _ { j } a _ { j l } c _ { l } ^ { k - 1 } + \sum _ { j , l = 1 } ^ { s } a _ { i j } \Big ( b _ { l } c _ { l } ^ { k - 1 } + a _ { j l } ( 1 + c _ { l } ) ^ { k - 1 } \Big ) . } \end{array}
$$

Wenow assume that the Runge-Kutta method corresponding to the right tableau of (6.8）satisfies condition $C ( s ) .$ Thismeans that themethod $( c , A , b )$ isa collocation method,and that the coefficients $\mu _ { i j }$ have to be computed from the linear system

$$
\sum _ { j = 1 } ^ { s + i - 1 } \mu _ { i j } c _ { j } ^ { k - 1 } = \frac { \mu _ { i } ^ { k } } { k } , \qquad k = 1 , \ldots , s .
$$

Themethod corresponding to the left tableau of(6.8）then also satisfies $C ( s )$ .Consequently，the order conditions are simplified considerably,and it follows from Sect.IIL.1 that $Y _ { i n } ^ { 0 }$ is anapproximationtotheexactstagevalue $Y _ { i n }$ of order $s + 1$ or $s + 2$ if the following conditions hold:

$$
\begin{array} { r l } { \mathrm { o r d e r ~ } s + 1 } & { \mathrm { ~ i f ~ } ( 6 . 9 ) \mathrm { f o r ~ } k = 1 , . . . , s + 1 ; } \\ { \mathrm { o r d e r ~ } s + 2 } & { \mathrm { ~ i f ~ } ( 6 . 9 ) \mathrm { f o r ~ } k = 1 , . . . , s + 2 , \mathrm { a n d ~ } ( 6 . 1 0 ) \mathrm { f o r ~ } k = s + 1 } \end{array}
$$

Foran approximation of order $s + 1$ weput $m = 1$ ,wearbitrarily choose $\mu _ { 1 }$ ,wecomputeμ1jfrom(6.11）,and thecoefficients $\beta _ { i j }$ and $\nu _ { i 1 }$ from（6.9）with $k = 1 , \ldots , s + 1$ Areasonablechoice for the freeparameteris $\mu _ { 1 } \in [ 1 , 2 ]$ (inour computations we take $\mu _ { 1 } = 1 . 7 5$ for $s = 2 , 4$ ,and $\mu _ { 1 } = 1 . 8$ for $s = 6$ .1

Foranapproximation of order $s + 2$ weput $m = 3 .$ One of the three additional function evaluations can be saved if we put $\mu _ { 1 } = 0$ and $\mu _ { 2 } ~ = ~ 1$ .Thisimplies $Y _ { s + 1 , n - 1 } = y _ { n - 1 }$ and $Y _ { s + 2 , n - 1 } = y _ { n }$ so that theevaluation of $f ( Y _ { s + 1 , n - 1 } )$ is already availablefrom computations for thepreceding step(FSAL technique,“first sameas last").In our experiments we take $\mu _ { 3 } ~ = ~ 1 . 6$ for $s \ = \ 2$ , $\mu _ { 3 } = 1 . 6 5$ for $s = 4$ ,and $\mu _ { 3 } = 1 . 7 5$ for $s = 6$ Thecoefficients $\mu _ { i j } , \beta _ { i j } , \nu _ { i j }$ are then obtained as the solution of Vandermonde like linear systems.

Forpleeatiooetkiti $Z _ { i n } ^ { 0 } =$ $Y _ { i n } ^ { 0 } - y _ { n }$ andtowrite(6.7) in the form

$$
Z _ { i n } ^ { 0 } = h \sum _ { j = 1 } ^ { s } \alpha _ { i j } f ( Y _ { j , n - 1 } ) + h \sum _ { j = 1 } ^ { m } \nu _ { i j } f ( Y _ { s + j , n - 1 } )
$$

with $\alpha _ { i j } = \beta _ { i j } - b _ { j } .$

(C)Equistage Approximation.From the implicit function theorem,applied to the nonlinear system（6.1）,weknow that $Z _ { i n } = z ( y _ { n } , h )$ ,where the function $z ( y , h )$ isas smoothas $f ( y )$ Furthermore,since on compact intervals the global errorofa one-step method permits an asymptotic expansion in powers of $h$ ,wehave $y _ { n - l } =$ $y _ { N } ( t _ { n - l } , h ) + O ( h ^ { N + 1 } )$ with $y _ { N } ( t , h ) = y ( t ) + h ^ { p } e _ { p } ( t ) + \ldots , + h ^ { N } e _ { N } ( t )$ (thevalue of $N$ can bechosen arbitrarily largeif $f ( y )$ issufficiently smooth).Consequently, $Z _ { i , n - l }$ is $\mathcal { O } ( h ^ { N + 1 } )$ closeto the smooth function $z \left( y _ { N } ( t , h ) , h \right)$ at $t = t _ { n } - l h$ . Let $\zeta _ { i } ( t )$ be the polynomial of degree $k - 1$ defined by $\zeta _ { i } ( t _ { n - l } ) ~ = ~ Z _ { i , n - l }$ for $l = 1 , \ldots , k .$ Then,thevalue

$$
Z _ { i n } ^ { 0 } = \zeta _ { i } ( t _ { n } )
$$

yieldsa $\mathcal { O } ( h ^ { k + 1 } )$ approximation to the solution of (6.1).This interpolation procedure was first proposed by In't Hout(1992） for the numerical solution of delay differential equations.For the iterative solution of the nonlinearRunge-Kutta equations(6.1）,the startingapproximation (6.14) is proposed and analyzed by Calvo (2002).

The implementation of this approach is very simple.Using Newton's interpolation formulawe have

$$
Z _ { i n } ^ { 0 } = Z _ { i , n - \bar { 1 } } + \nabla Z _ { i , n - 1 } + \ldots + \nabla ^ { k - 1 } Z _ { i , n - \bar { 1 } }
$$

with backward differences given by $\nabla Z _ { i , n } = Z _ { i , n } - Z _ { i , n - 1 }$ ， $\nabla ^ { 2 } Z _ { i , n } = \nabla Z _ { i , n } -$ $\nabla Z _ { i , n - 1 }$ ,etc.

Numerical Study of Starting Approximations.We consider the Keplerproblem with eccentricity $e = 0 . 6$ and initial values such that the period is $2 \pi$ Withmany different step sizes $h = 2 \pi / N$ wecompute $N + 1$ stepswith the Gauss method oforder $p = 2 s$ $p = 4 , 8 , 1 2 )$ In the last stepwe compute thedifferent starting approximations and their error $\begin{array} { r l } {  { ( \sum _ { i = 1 } ^ { s } \| Z _ { i n } - Z _ { i n } ^ { 0 } \| ^ { 2 } ) ^ { 1 / 2 } } } \end{array}$ asa function of the step size $h$ .Theresult isplotted inFig.6.1.There,thepictures also contain the global errors after one period.Theyallow us to localize the values of $h$ ,which are of practical interest.

Weobserve that theequistage approximation(6.15)also behaves like $O ( h ^ { k + 1 } )$ when $k + 1$ islarger than the order of the integrator.However,dueto the increasingerror constants,the accuracy isimproved only for small step sizes.An optimal $k$ couldbe estimated by checking the decrease of the backward differences ${ \| \nabla ^ { \ j } Z _ { i , n - 1 } \| }$ The error of the starting approximation obtained from the continuous output behaves like $\mathcal { O } ( h ^ { s + 1 } )$ (for the Gauss methods)and,incontrast to the equistageapproximation,improveswith increasing order.The approximations (6.7）of order $s + 1$ and $s + 2$ areaclearimprovement.Asaconclusionwe find that for this example the equistage approximation (whichis free from additional function evaluations)ispreferable only for $s = 2$ (order4).For higher order,theapproximation obtained from(6.7)is significantlymore accurate and so itisworthwhile to spend these two additional function evaluations per step.

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0005_pages_0281-0350/auto/images/69beb852057ef22351766065abe6f17c16cc98bcd42403a02d5a1960f2ca7dd1.jpg)  
Fig.6.1.Errors of starting approximations for Gauss methodsas functions of the step size $h$ :thickdashed lines for the extrapolatedcontinuous output (6.4)and for theapproximations (6.7)of order $s + 1$ and $s + 2$ thinsolid linesfor theequistage approximation (6.15)with $k = 0 , 1 , \ldots , 7 ;$ thethick solid line representsthe global error of the method after one period

# VIII.6.2 Fixed-Point VersusNewton Iteration

Finallywe investigate the iterative solution of the nonlinearRunge-Kutta system (6.1).We discuss fixed-point and Newton-like iterations,and we compare their efficiency to the use of composition methods.

Fixed-Point Iteration.This isthe most simple and most natural iteration for the solutionof (6.1).Withanystartingapproximation $Z _ { i n } ^ { 0 }$ fromSect.VII.6.1 it reads

$$
Z _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } f \bigl ( y _ { n } + Z _ { j n } ^ { k } \bigr ) , \qquad i = 1 , \ldots , s .
$$

In the case where the entries of the Jacobian matrix $f ^ { \prime } ( y )$ arenot excessively large (nonstiff problems)and that the step sizeis sufficiently small,this iteration convergesfor tothe solution of(6.1).Usually,the iteration is stopped ifa cetinomofteitcees $Z _ { i n } ^ { k + 1 } - Z _ { i n } ^ { k }$ isucymal.euse $Z _ { i n } ^ { k }$ intheupdate formula(6.2） so thatno additional function evaluationisrequired.

Foranumerical study of the convergence of this iteration,we consider the Kepler problem with eccentricity $e = 0 . 6$ and initial values as in the preceding experiments(period of the solution is $2 \pi$ ).Weapply theGaussmethodsoforder 4,8,and 12 with various step sizes.For the integration over one period we show in Table 6.1 the total number of function evaluations,the mean number of required iterations per step,and the global errorat the endpoint of integration.Asa stopping criterion for thefixed-point iteration wecheck whether the norm of the difference of two successiveapproximations is smaller than $1 0 ^ { - 1 6 }$ (roundoff unit in double precision).As astarting approximation $Z _ { i n } ^ { 0 }$ we use (6.15)with $k = 8$ for the method of order 4, and the approximation(6.7)of order $s + 2$ forthe methods of orders 8and 12.The coefficients are those presented after equation (6.12).

Table6.1.Statistics of Gauss methods (total number of function evaluations,number of fixed-point iterations per step,and the global error at the endpoint)for computations of the Kepler problem over one period with $e = 0 . 6$   
Fixed-point iteration (general problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order4</td><td rowspan=1 colspan=1>80316.19.2.10-2</td><td rowspan=1 colspan=1>104310.41.7.10-2</td><td rowspan=1 colspan=1>13937.01.3.10-3</td><td rowspan=1 colspan=1>18254.68.4.10-5</td><td rowspan=1 colspan=1>23192.95.3.10-6</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>10219.71.1.10-3</td><td rowspan=1 colspan=1>14556.86.9.10-7</td><td rowspan=1 colspan=1>20914.73.6.10-9</td><td rowspan=1 colspan=1>30073.31.8.10-11</td><td rowspan=1 colspan=1>41832.16.9.10-14</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>12978.32.7.10-6</td><td rowspan=1 colspan=1>17315.48.0.10-11</td><td rowspan=1 colspan=1>23113.52.7.10-14</td><td rowspan=1 colspan=1>34412.5≤roundoff</td><td rowspan=1 colspan=1>59172.1≤roundoff</td></tr></table>

Since the starting approximations are more accurate for small $h$ thenumber ofnecessary iterationsdecreasesdrastically.Inparticular,for the4th ordermethod weneed about 16 iterations per step for $h = 2 \pi / 2 5$ ,butat most2iterationswhen $h \leq 2 \pi / 8 0 0$ Ifoneisinterestedin high accuracycomputations (e.g.,long-time simulationsin astronomy),forwhich theerror over one period is not larger than $1 0 ^ { - 1 0 }$ ,Table6.1illustratesthat highordermethods( $p \geq 1 2$ )aremost efficient.

Newton-Type Iterations.Astandard technique for solving nonlinear equations is Newton's method or some modification of it.Writing the nonlinear system (6.1）of animplicit Runge-Kutta method as $F ( Z ) = 0$ with $Z = ( Z _ { 1 n } , \ldots , Z _ { s n } ) ^ { \cal I }$ ,the Newton iteration is

$$
Z ^ { k + 1 } = Z ^ { k } - M ^ { - 1 } F ( Z ^ { k } ) ,
$$

where $M$ is some approximation to the Jacobian matrix $F ^ { \prime } ( Z ^ { k } )$ .Since the solution $\boldsymbol { \mathcal { L } }$ of the nonlinear system is $\mathcal { O } ( h )$ close to zero,it is common to use $M = F ^ { \prime } ( 0 )$ so that the matrix $M$ isindependent of the iteration index $k$ Inour special situation weget

$$
M = I \otimes I - h A \otimes J
$$

with $J = f ^ { \prime } ( y _ { n } ) .$ Here, $I$ denotes the identity matrix of suitable dimension,and $A$ is theRunge-Kutta matrix.

Werepeat the experiment of Table 6.1with modified Newton iterations instead offixed-point iterations.Theresultis shownin Table 6.2.We have suppressed the errorat the end of theperiod,because itis the sameasin Table6.1.As expected,the convergence is faster(i.e.,thenumber of iterationsper stepissmaller)so that the total numberof function evaluations isreduced.However,wedo not see in this table thatwe computed at every step the Jacobian $f ^ { \prime } ( y _ { n } )$ andan $L R$ -decompositionof thematrix $M .$ Even if we exploit the tensor product structure in(6.18)as explained


<!-- chunk 0006: pages 351-420 -->
Table6.2.Statistics of Gauss methods (total number of function evaluations,number of iterations per step) for computations of the Kepler problem over one period with $e = 0 . 6$   
Modified Newton iteration (general problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order4</td><td rowspan=1 colspan=1>3837.7</td><td rowspan=1 colspan=1>5115.1</td><td rowspan=1 colspan=1>7653.8</td><td rowspan=1 colspan=1>11252.8</td><td rowspan=1 colspan=1>16772.1</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>5975.5</td><td rowspan=1 colspan=1>8833.9</td><td rowspan=1 colspan=1>13873.0</td><td rowspan=1 colspan=1>23072.4</td><td rowspan=1 colspan=1>36671.8</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>7634.7</td><td rowspan=1 colspan=1>10953.3</td><td rowspan=1 colspan=1>17172.5</td><td rowspan=1 colspan=1>30032.2</td><td rowspan=1 colspan=1>56892.0</td></tr></table>

inHairer&Wanner (1996,Sect.IV.8),thecpu time is now considerably larger. Further improvements are possible,if the Jacobian of $f$ and hence also the $L R$ decomposition of $M$ isfrozen overa couple of steps.But all these efforts can hardly beat(in cpu time) the straightforward fixed-point iterations.In accordancewith the experience of Sanz-Serna &Calvo(1994,Sect.5.5）we recommendin general the use of fixed-point iterations.

Separable Systemsand Second Order Differential Equations.Many interesting differential equationsare of the form

$$
\dot { \eta } = f ( y ) , \qquad \dot { y } = g ( \eta ) .
$$

Forexample,the second orderdifferential equation $\ddot { y } = f ( y )$ is obtained by putting $g ( \eta ) = \eta$ .Also Hamiltonian systems with separable Hamiltonian ${ \cal H } ( p , q ) = T ( p ) +$ $U ( q )$ are of the form (6.19).

For this particular system the Runge-Kutta equations (6.1) become

$$
\zeta _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } f ( y _ { n } + Z _ { j n } ) = 0 , \qquad Z _ { i n } - h \sum _ { j = 1 } ^ { s } a _ { i j } g ( \eta _ { n } + \zeta _ { j n } ) = 0 .
$$

In this case we can still do better:instead of the standard fixed-point iteration (6.16) weapplya Gauss-Seidel like iteration

$$
\zeta _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } f ( y _ { n } + Z _ { j n } ^ { k } ) , \qquad Z _ { i n } ^ { k + 1 } = h \sum _ { j = 1 } ^ { s } a _ { i j } g ( \eta _ { n } + \zeta _ { j n } ^ { k + 1 } ) ,
$$

whichis explicit for separable systems (6.19).Notice that the starting approximations have to be computed only for $\zeta _ { i n }$ .Those for $\boldsymbol { Z } _ { i n }$ are then obtained by(6.20) with $k + 1 = 0$ .

For second order differential equations $\ddot { y } = f ( y )$ ,where $g ( \eta ) = \eta$ ,thisiteration becomes

$$
Z _ { i n } ^ { k + 1 } = \hbar c _ { i } \eta _ { n } + h ^ { 2 } \sum _ { j = 1 } ^ { s } \widehat { a } _ { i j } f ( y _ { n } + Z _ { j n } ^ { k } ) ,
$$

Table 6.3.Statistics of iterations (6.2O) for Gauss methods (total numberof function evaluations,numberof iterationsperstep)forcomputations of the Kepler problem overone period with $e = 0 . 6$   
Fixed-point iteration (separable problems)   

<table><tr><td rowspan=1 colspan=1>Gauss</td><td rowspan=1 colspan=1>h=2π/25</td><td rowspan=1 colspan=1>h=2π/50</td><td rowspan=1 colspan=1>h=2π/100</td><td rowspan=1 colspan=1>h=2π/200</td><td rowspan=1 colspan=1>h=2π/400</td></tr><tr><td rowspan=1 colspan=1>order 4</td><td rowspan=1 colspan=1>4378.7</td><td rowspan=1 colspan=1>6036.0</td><td rowspan=1 colspan=1>8574.3</td><td rowspan=1 colspan=1>12013.0</td><td rowspan=1 colspan=1>17172.1</td></tr><tr><td rowspan=1 colspan=1>order8</td><td rowspan=1 colspan=1>6135.6</td><td rowspan=1 colspan=1>9234.1</td><td rowspan=1 colspan=1>14273.1</td><td rowspan=1 colspan=1>2.3392.4</td><td rowspan=1 colspan=1>36471.8</td></tr><tr><td rowspan=1 colspan=1>order12</td><td rowspan=1 colspan=1>7814.9</td><td rowspan=1 colspan=1>11313.4</td><td rowspan=1 colspan=1>17412.6</td><td rowspan=1 colspan=1>30272.2</td><td rowspan=1 colspan=1>56772.0</td></tr></table>

where $\begin{array} { r } { c _ { i } = \sum _ { j = 1 } ^ { s } a _ { i j } } \end{array}$ and $\widehat { a } _ { i j }$ are te enres f hesquare $A ^ { 2 }$ of the Runge-Kutta matrix(any Nystrommethod could beapplied aswell).Due to the factor $h ^ { 2 }$ in(6.21) weexpect this iteration to converge about twice as fast as the standard fixed-point iteration.

TheKepler problem isasecond orderdifferential equation,so that the iteration (6.21）canbe applied.Inanalogy to theprevious tableswepresentin Table6.3the statistics of such an implementation of the Gauss methods.We observe that forrelatively large stepsizes thenumber of iterationsrequired per step in nearly halved (compared to Table6.1).For high accuracy requirements the number of necessary iterations is surprisingly small,and the question ariseswhether such an implementation can compete with high order explicit composition methods.

Comparison Between Implicit Runge-Kutta and Composition Methods.We consider second orderdifferential equations $\ddot { y } = f ( y )$ ,so that composition methods basedon the explicit Stormer-Verlet scheme can be applied.Weuse the coefficientsofmethod(V.3.14)which has turned out to beexcellentin the experiments of Sect.V.3.2.Itisamethod of order8and uses 17 functionevaluationsper integration step.

We compare it with the Gauss methods of order 8 and 12 (i.e., $s = 4$ and $s = 6$ ). Asa starting approximation for the solution of the nonlinear system (6.1） we use （6.7）with $m = 3$ , $\mu _ { 1 } = 0$ , $\mu _ { 2 } = 1$ , $\mu _ { 3 } = 1 . 7 5$ , $\mu _ { i j }$ chosen such that （6.11） holds for $k = 1 , \ldots , s + i - 1$ ,and $\beta _ { i j }$ , $\nu _ { i j }$ such that order $s + 2$ is obtained.Since we are concerned with second orderdifferential equations,we apply the iterations (6.20) until the norm of the difference of two successve approximations is below $1 0 ^ { - 1 7 }$

For both classes of methods we use compensated summation (Algorithm 5.1), which permits us to reduce rounding errors.For composition methodswe apply this technique forall updates of the basicintegrator.For Runge-Kutta methods,weuse itforaddingtheincremento $y _ { n }$ andalsoforcomputingthesum $\textstyle \sum _ { i = 1 } ^ { s } b _ { i } k _ { i }$

The work-precision diagrams of the comparison are given inFig.6.2.Theupper pictures correspond to the Kepler problem with $e = 0 . 6$ and an integration over100 periods;the lower pictures correspond to the outer solar system with data given in Sect.I.2.4and an integrationover 5OoooO earthdays.The leftpictures show the

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0006_pages_0351-0420/auto/images/8a5ca4612c51c671466bbec8c71d1b4fbdc34561f4378e08f802f3b574132666.jpg)  
Fig.6.2.Work-precision diagrams for two problems (Keplerand outer solar system） and three numerical integrators(composition method with coefficients of method(V.3.14) based ontheexplicit Stormer-Verlet scheme and the Gauss methods of orders 8and12)

Euclidean norm of theerror at the end of the integration interval asa function of total numbers of function evaluations required for the integration;the pictures to the rightpresent the same error asa function of the cpu times (with optimizing compiler ona SunBlade 1Oo workstation).We can draw the following conclusions from this experiment:

·the implementation of composition methods based on the Stormer-Verlet scheme isextremely easy;that of implicit Runge-Kuttamethods is slightly more involved because it requires a stopping criterion for the fixed-point iterations;   
·the overhead (total cpu time minus that used for the function evaluations) is much higherfor the implicit Runge-Kutta methods;this is seen from the fact that implicit Runge-Kutta methods require less function evaluations fora given accuracy,but often more cpu time;   
among thetwo Gaussmethods,the higher ordermethod ismore efficient forall precisions of practical interest;   
·forvery accurate computations (say,in quadruple precision),high order Runge-Kuttamethods are more efficient than composition methods;   
much of the computation in the Runge-Kutta codecan be done in parallel (e.g., the $s$ function evaluations of a fixed-point iteration);composition methods do not have this potential;   
implicit Runge-Kutta methods can be applied to general (non-separable） differential equations,and thecost ofthe implementation is at most twice as large;if oneis obliged to use an implicit method as the basic method for composition, many advantages of composition methods are lost.

Bothclasses of methods (composition and implicit Runge-Kutta) are of interest inthe geometric integration ofdifferential equations.Each one has itsadvantages and disadvantages.

Fortran codes of these computations are available on the Internet under the homepage<http://www.unige.ch/math/folks/hairer>.AMatlabversion ofthese codesisdescribed inE.&M.Hairer(2003).

# VIII.7 Exercises

1.Considera one-step method applied toa Hamiltonian system.Givea probabilisticproof of the property that the error of the numerical Hamiltonian due to roundoff grows like $\mathcal { O } ( \sqrt { t } e p s )$

2.Prove that the collocation polynomial can be writtenas

$$
w _ { n } ( t ) = y _ { n } + h \sum _ { i = 1 } ^ { s } \beta _ { i } ( t ) f ( Y _ { i n } ) ,
$$

where the polynomials $\beta _ { i } ( t )$ are a solution of

$$
\sum _ { j = 1 } ^ { s } \beta _ { j } ( t ) c _ { j } ^ { k - 1 } = \frac { t ^ { k } } { k } .
$$

3.Applyyour favouritecode totheKepler problemand tothe outer solarsystem withdataasinFig.6.2.Plotawork-precision diagram.

Remark.Figure7.1 shows our resultsobtained with the 8th order Runge-Kutta codeDop853（Hairer,Ngrsett&Wanner1993)comparedtoan8thordercomposition method.Rounding errors are more pronounced for Dop853,because compensated summation is not applied.Computations on shorter time intervalsand comparisons ofrequired function evaluationswould bemorein favour forDop853.Itisalso of interest toconsider high order Runge-Kutta Nystrom methods.

4.Consider starting approximations

$$
Y _ { i n } ^ { 0 } = y _ { n - 2 } + h \sum _ { j = 1 } ^ { s } \beta _ { i j } ^ { ( 2 ) } f ( Y _ { j , n - 2 } ) + h \sum _ { j = 1 } ^ { s } \beta _ { i j } ^ { ( 1 ) } f ( Y _ { j , n - 1 } )
$$

![](../chunks/Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Differential_part_0006_pages_0351-0420/auto/images/8912cc4af13149dd0f571942c8812d2dbcc2875e6ece57637504e28d0d4b88a5.jpg)  
Fig.7.1.Work-precision diagrams for the explicit,variable step size Runge-Kutta code Dop853applied to two problems(Kepler and outer solar system).For a comparison,the resultsof Fig.6.2 for the composition method are included

which use the internal stages of two consecutive steps without any additional function evaluation.What are the conditions such that(7.1) is of order $s + 1$ ,of order $s + 2 ^ { \prime }$ ？

Compare the efficiency of these formulaswith the algorithms(A) and (B）of Sect.VIII.6.1.

5.Prove that fora second order differential equation $\ddot { y } = f ( y )$ (more precisely, for $\dot { y } = z , \dot { z } = f ( y ) )$ theapplication of the $s$ -stage Gauss method gives

$$
\begin{array} { l } { { y _ { n + 1 } ~ = ~ y _ { n } + h \dot { y } _ { n } + h ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } ( 1 - c _ { i } ) f ( y _ { n } + Z _ { i n } ) } } \\ { { \dot { y } _ { n + 1 } ~ = ~ \ddot { y } _ { n } + h \displaystyle \sum _ { i = 1 } ^ { s } b _ { i } f \big ( y _ { n } + Z _ { i n } \big ) , } } \end{array}
$$

where $Z _ { i n }$ is obtained from the iteration (6.21).

Hint.The coefficients of the Gauss methods satisfy $\begin{array} { r } { \sum _ { j } b _ { j } a _ { j i } = b _ { i } ( 1 - c _ { i } ) } \end{array}$ for all $i$
