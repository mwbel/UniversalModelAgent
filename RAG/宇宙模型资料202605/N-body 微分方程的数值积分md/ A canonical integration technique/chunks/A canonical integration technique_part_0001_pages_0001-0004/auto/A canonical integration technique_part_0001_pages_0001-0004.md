# A CANONICAL INTEGRATION TECHNIQUE

by R.Ruth

The class of differential equations studied here is that in which the equationsare derivable from a Hamiltonian usinga Hamiltonian'sEquations. The exact solution of such a system ofequations leads toa symplectic map from the initial conditions to the present state of.the system. However,a characteristic feature of all explicit high order integration methods is that they are not exactly symplectic. One manifestation of this is that the Jacobian of the transformation for one time step differs from unity; thus，the system will be damped (or excited）artificially. This can lead to incorrect phase space behaviour.The purpose of this paper is to develop explicit third-order symplectic maps (i.e.third-orderintegration steps that preserve exactly the canonical character of the equations ofmotion). Thesecan replace thetypical methodsfor integration with the benefit that they canbe iteratedindefinitelysince theyare symplectic maps. Thus theyare especiallyvaluableforstudying thelong-time behaviour of complicated nonlinear differential equations.

Presented at the 1983 Particle Accelerator Conference, 21-23 March 1983,Santa Fe,New Mexico

RonaldD.Ruth\* Lawrence Berkeley Lab,Berkeley C.A.94720

There are many different ways to integrate differentialequationsnumerically.1 Thesevarious methods are usually characterized by the accuracy ofa single stepin time.Thusif in a small time step,h, theintegration is performed so that it is accurate throughorder $\mathsf { h } ^ { \mathsf { n } }$ ，then the method is referred to as an $n ^ { \tt t R }$ orderintegration method.

The class of differential equations of interest hereis that in which the equations are derivable from a Hamiltonian using Hamilton's equations.The exact solution of such a system of differential equations leads to a symplectic map from the initial conditions to the present state of the system. A characteristic feature of all explicit high order （n>2）integration methods,however，is that they are not exactly symplectic.One manifestation of this is that the Jacobian of thetransformation for one time step differs slightly fromunity,and so the system will be damped(or excited）artificially. Inmanyapplicationsthe salient features of the solutions appear only after ongetimseorearge numeers of iterations;onin these applications spurious damping or excitation may lead to misleading results.

The purpose of this note is to develop an explicit third order symplectic map (i.e.a third order integration step that preserves exactly the canonical character of the equations of motion）and to indicate the method for higher order maps. For a typical numerical integration,this method can be used to eliminate the noncanonicaleffectswhileprovidingtheaccuracy corresponding to a third order integration step.

There is in addition another benefit of this approach.If we iterateamap ofa given order whether canonical or not,eventuallythe absolute error in and $\overrightarrow { p }$ gets large.In cases where spuriousdamping occurs,Xandp typically settle into some stable fixed point² If the map is symplectic,this is not the case. A symplectic map generates phase space behaviour which is close to that of the original system with errors in phase which eventuallymay add up after many interations to yield large absolute errors in $\overrightarrow { \sf x }$ and $\overrightarrow { \mathsf p }$ ·

Therefore，in the symplectic case,it is possible and sometimes attractive to replace the differential equation by a symplectic map.This map then becomes the object of study and so can be iterated as much as we like. This is possible since the map is the solutionof some physical Hamiltonian problem which,in some sense,is close to the original problem. For other integration methods this is not the case and iterations must be terminated at some·point.

# The Problem

Consider a system of differential equations governed by the Hamiltonian,

$$
H = \overrightarrow { p } ^ { 2 } / 2 + V ( X , t ) .
$$

This is just Newton $" { \mathfrak { s } }$ second law with the potential $\forall ( \vec { \boldsymbol { x } } , t )$ The solution of the equations of motionis given by the functions

$$
\vec { \bf \xparallel } ( \vec { \bf x } _ { 0 } , \vec { \bf p } _ { 0 } , \ t ) \quad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \vec { \bf \mathsf { p } } ( \vec { \bf x } _ { 0 } , \vec { \mathsf { p } } _ { 0 } , \ t ) ,
$$

where $\vec { \pmb { x } } _ { 0 }$ and $\vec { \mathsf { p } } _ { 0 }$ are the initial conditions at time $t ~ = ~ 0$ .Due tothe canonical character of the equations of motions,Equation (2）constitutesa canonical transformation(ora symplectic map）from the initial conditionsto the state at time t which we denote by

$$
( \mathbf { \boldsymbol { x } } , \mathsf { p } ) = \mathsf { M } ( \mathsf { t } ) ( \mathbf { \boldsymbol { x } } _ { 0 } , \mathsf { p } _ { 0 } ) .
$$

Now the questicr:is:if the_parameter t is small, can this map be found approximatelyto some given order int？If this can be done explicitly，then the process can easily be iterated and the error controlled by adjusting the step size,t.Of course,the typical integration method does just this but sacrifices the canonical character of the map This we propose to avoid.Let the approximate nth ordersymplectic map bedenoted by

$$
( \times , p ) = M _ { n } ( t ) ( \times _ { 0 } , p _ { 0 } ) ,
$$

where t is the time step(assumed small）and n is the order of the map,i.e.

$$
\vert \vert \boldsymbol { \mathsf { M } } ( \mathsf { t } ) - \boldsymbol { \mathsf { M } } _ { \mathsf { n } } ( \mathsf { t } ) \vert \vert = 0 ( \mathsf { t } ^ { \mathsf { n } + 1 } ) .
$$

Inthe next section we demonstrate a method for finding ${ \mathfrak { M } } _ { \mathfrak { n } } ( \mathfrak { t } )$ ：

To illustrate the method first start from low order.If we somehow perform the transformation in Equation (3) so that H is expressed in terms of the initial conditions,then the equations of motion are

$$
\frac { d \vec { \bf x } _ { 0 } } { d \bf t } = 0 \qquad \frac { d \vec { \bf p } _ { 0 } } { d \bf t } = 0 ,
$$

or the new Hamiltonian, $\sharp ^ { \prime }$ ,isidentically zero (or at least independent of $\mathsf { x } _ { 0 } , \mathsf { p } _ { 0 } )$ This suggests that we makecanonical transformations in such a way as to make Hvanish. Thus the program is to make these successive canonical transformations until we arrive at the intitial conditions of the problem,or at Teast to another set of coordinates which approximates $( \mathsf { x } _ { 0 } , \mathsf { p } _ { 0 } )$ through some order in t.

Let $( \mathsf { x } _ { 1 } , \mathsf { p } _ { 1 } )$ be the new coordinates. Then the convenient form forthe generating functionof the canonical transformation is that involving the new coordinatesand old momenta

$$
( \textsf { x } , \mathsf { p } ) { \ + } ( \textsf { x } _ { 1 } , \mathsf { p } _ { 1 } )
$$

$$
\begin{array} { r c l } { { x = \displaystyle \frac { - \partial \mathsf { F } _ { 3 } } { \partial \mathsf { p } } \ = \ \mathsf { x } _ { 1 } \ - \ \mathsf { G } _ { \mathsf { p } } \ , \qquad \mathsf { p } _ { 1 } } } & { { = \displaystyle \frac { - \partial \mathsf { F } _ { 3 } } { \partial \mathsf { x } _ { 1 } } \ = \ \mathsf { p } \ - \ \mathsf { G } _ { \mathsf { x } _ { 1 } } } } \\ { { \displaystyle \mathsf { H } _ { 1 } } } & { { = \ \mathsf { H } \ + \ \displaystyle \frac { \partial \mathsf { F } _ { 3 } } { \partial \mathsf { t } } \ } } & { { = \ \mathsf { H } \ + \ \mathsf { G } _ { \mathsf { t } } \ , } } \end{array}
$$

where subscripts have been used to denote partial derivatives. Equations (8）suggest that we select

$$
G = - \{ p ^ { 2 } / 2 + V ( x _ { 1 } , 0 ) \} t
$$

so that

$$
p _ { 1 } = p - f ( x _ { 1 } , 0 ) { \sf t } \qquad \mathrm { ~ x ~ \equiv ~ x _ 1 ~ + ~ p t , }
$$

where the force, $\pmb { \mathscr { f } }$ ,has been introduced,

$$
f ( x , 0 ) = - \ \partial V ( x , 0 ) / \partial x .
$$

Subsituting into the Hamiltonian yields

$$
\mathtt { H } _ { 1 } = \mathtt { V } \big ( \mathtt { x } _ { 1 } + \mathtt { \ t } \big ( \mathtt { p } _ { 1 } + \mathtt { f } \big ( \mathtt { x } _ { 1 } , 0 \big ) \mathtt { t } \big ) , \mathtt { t } \big ) - \mathtt { V } \big ( \mathtt { x } _ { 1 } , 0 \big )
$$

and expanding on the small parameter t,we have

$$
H _ { 1 } = t V _ { t } ( x _ { 1 } , 0 ) - t p _ { 1 } f ( x _ { 1 } , 0 ) + 0 ( t ^ { 2 } ) .
$$

Since $\mathsf { H } _ { 1 }$ is ${ 0 } ( t )$ ，the right hand sides of the differentialequationsfrom Hamilton $\boldsymbol { \cdot } _ { 5 }$ Equationsare also ${ 0 } ( t )$ .Therefore,the solution is

$$
x _ { 1 } = c _ { 0 } n s t + 0 ( t ^ { 2 } ) \rho _ { 1 } = c _ { 0 } n s t + 0 ( t ^ { 2 } ) .
$$

Soif $\mathsf { x } _ { 1 }$ and $\mathsf { p } _ { 1 }$ are used as initial conditions，the errorintroducedis $0 ( t ^ { 2 } )$ .Thus this approachhas yielded a first order symplectic map, ${ \sf M } _ { 1 } \left( t \right)$ ：

Since this is such a low order method，it could havebeenderivedbyinspection；however,it illustrates the method which will be used in the next and subsequent sections.Notice that if $( \mathsf { x } _ { 1 } , \mathsf { p } _ { 1 } )$ are viewed as initial conditions in Equation (lO），then the momentum p must be calculated first and then used to evaluate X. This is a characteristic feature of the method. In addition note that the transformation leads back to the initial conditions；thus，the momentum equation must be inverted (trivial in this case).

# The Second Order Map

It is possible to continue from the results of the previous section to obtain a second order map；however， there is a well known method (the leap frog method) which is exactly canonical,is second order and which requires only one evaluation of the force. In order to understand that method and to lay the groundwork for a third order map,it is useful to modify the approach in the previous section.The modification consists of performing two canonical transformations rather than one. These are given by：

$$
\begin{array} { r c l } { { \displaystyle ( \times , { \mathsf { p } } ) \to \left( \times _ { 1 } , { \mathsf { p } } _ { 1 } \right) : \qquad \times } } & { { = \mathrm {  ~ \times _ 1 ~ } + \mathrm {  ~ \ a p t } , \quad { \mathsf { p } } _ { 1 } } } & { { = \mathrm {  ~ \mathsf { p } ~ - \ t f } ( \mathrm {  ~ \times _ 1 ~ } , { \mathsf { b } } { \mathsf { t } } ) } } \\ { { \mathrm {  ~ { \texttt ~ { ~ F ~ } = ~ - \mathrm {  ~ \ x _ 1 } p ~ - ~ a ~ } } } } & { { \displaystyle ( \mathrm {  ~ \mathtt { 1 5 } ~ } \mathrm {  ~ \alpha ~ } } } \\ { { \displaystyle ( \mathrm {  ~ \times _ 1 ~ } , { \mathsf { p } } _ { 1 } ) \to \left( \mathrm {  ~ \times _ 2 { } } { \mathsf { p } } _ { 2 } \right) : \qquad \mathrm {  ~ \times _ 1 ~ } } } & { { = \mathrm {  ~ \times _ 2 ~ } + \mathrm {  ~ \left( \mathtt { 1 - a } \right) } { \mathsf { p } } _ { 1 } { \mathsf { t } } , \qquad { \mathsf { p } } _ { 2 } } } & { { = \mathrm {  ~ \mathtt { p } _ 1 ~ } } } \\ { { \displaystyle { \mathsf { F } } } } & { { = - \mathrm {  ~ \ x _ 2 ~ } { \mathsf { p } } _ { 1 } } } & { { - } } & { { \displaystyle ( \frac { \mathrm {  ~ \mathtt { 1 - a } ~ } } { 2 } ) { \mathsf { p } } _ { 1 } { \mathrm {  ~ \mathrm { \texttt ~ { ~ 2 } ~ } } } . } } \end{array}
$$

Thus,there is an intermediate step at which the force is evaluated. At this time the parameters a and bare undetermined;however, these can be used to generate a second order map. Substituting the two transformations into the Hamiltonian and expandingin thesmallparameter,t,yie.lds

$$
H _ { 2 } = t ( 1 - 2 a ) p _ { 2 } t ( x _ { 2 } , 0 ) + t ( 1 - 2 b ) V _ { t } ( x _ { 2 } , 0 ) + 0 ( t ^ { 2 } ) .
$$

The purpose of the expansion in t is to identify the coefficients of various powers in $H _ { 2 }$ The transformation equations in Equation（l5)，however,must be kept exactly in order to preserve the canonical character.

Now recall from the previous section that if H is of $0 ( t ^ { n } )$ ，andif $( p _ { 2 } , x _ { 2 } )$ are used asinitial conditions,the resulting mapis $n ^ { t h }$ order.Therefore, if we choose

$$
a = b = 1 / 2 ,
$$

then ${ \sf H } _ { 2 }$ is $0 ( t ^ { 2 } )$ ，and the total map is_ second order. Tosummarize the precedingresults shift the notation $( x _ { 2 }  x _ { 0 } , p _ { 2 }  p _ { 0 } )$ ,rewrite the transformations in thereverseorderandperformtheobvious generalisation to many dimensions.Then the second order map is given by the scheme following:

$$
M a p : ( \vec { \times } , \vec { p } ) = M _ { 2 } ( h ) ( \vec { \times } _ { 0 } , \vec { p } _ { 0 } )
$$

$$
\begin{array} { r l r } { \vec { \mathsf { p } } _ { 1 } } & { = } & { \vec { \mathsf { p } } _ { 0 } \qquad , \qquad \vec { \mathsf { x } } _ { 1 } ^ { \mathsf { \_ { \alpha } } } = \vec { \mathsf { x } } _ { 0 } + \vec { \mathsf { p } } _ { 1 } \hbar / 2 } \\ { \vec { \mathsf { p } } } & { = } & { \vec { \mathsf { p } } _ { 1 } + \mathsf { t } \vec { \mathsf { f } } \left( \vec { \mathsf { x } } _ { 1 } , \mathsf { t } _ { 0 } + \mathsf { h } / 2 \right) , \quad \vec { \mathsf { x } } ^ { \mathsf { \_ { \alpha } } } = \vec { \mathsf { x } } _ { 1 } + \vec { \mathsf { p } } \mathsf { h } / 2 } \end{array}
$$

This method is well known (the leap frog method) andused frequent1y in circumstances where anomolous damping or excitation is undesirable.Note that itis written somewhat differentlythan usual sinceitis calculated for one full step.Since it is useful to have higher order maps for savingsin computation time andforimproved accuracy of the phase space behavior, inthe next section this method is extended to third order.

# Third Order Maps

There are many possible generalisations to extend theprocedure described in the previous sections to higher order. The first approach that comes to mind is toinclude more intermediate steps or additional force evaluations.A second approach is to begin from the second order Hamiltonian and make yet another canonical transformation to eliminate another order in the t dependence of H.Both of these approaches are possible inprirciple and will work; however,thereisone difficuity.The functionaldependence in X and pof the terms which are of higher order in t can be quite complicated. Because of the nature ofcanonical transformations,one is forced to invert an equation ${ \mathsf p } _ { 1 } \left( { \mathsf p } _ { 0 } \right) { \star } { \mathsf p } _ { 0 } \left( { \mathsf p } _ { 1 } \right)$ ： This can be done explicitly only thesimplest cases. Inmore complicatedcasestie functional form isimplicit,and thus the utility of such an approach can be extemely diminished due to the 1ackof explicit formulae.

Fortunately, for the simple Hamiltonian in Equation(1）there is_amethod of avoiding this. The key toavoidingimplicitexpressionsliesin two points.The first isthat an exact expression relating newtooldvariablesisonlynecessaryin transformation equations.It is fine to substitute approximate perturbative expressionsinto the Hamiltonian (this has been done already).The second point is that onlyonehalf oftheequations fromthe generating function need to be inverted.In our case this is the momentum equation.With this in mind a combination of thetwo approaches mentioned above will be usedin order to generate a third order map.First writea somewhat more general two step transformation given by：

$$
\begin{array} { r l r } {  { ( \boldsymbol { \times } , \boldsymbol { \mathsf { p } } ) \to ( \boldsymbol { \times } _ { 1 } , \mathsf { p } _ { 1 } ) : \qquad \mathsf { F } ( \mathsf { x } _ { 1 } , \mathsf { p } , \mathsf { t } ) = - \mathsf { x } _ { 1 } \mathsf { p } - \frac { \mathrm { a } \mathsf { p } ^ { 2 } \mathsf { t } } { 2 } - \mathsf { b } \mathsf { t } \mathsf { V } ( \mathsf { x } _ { 1 } , \mathsf { c } \mathsf { t } ) } } \\ & { } & { \mathsf { x } ~ = ~ \mathsf { x } _ { 1 } ~ + ~ \mathsf { a } \mathsf { p } \mathsf { t } , } \\ & { } & { ( \mathsf { x } _ { 1 } , \mathsf { p } _ { 1 } ) \to ( \mathsf { x } _ { 2 } , \mathsf { p } _ { 2 } ) : \quad \mathsf { F } = ~ - ~ \mathsf { x } _ { 2 } \mathsf { p } _ { 1 } - \frac { ( 1 - \mathsf { a } ) } { 2 } \mathsf { p } _ { 1 } { } ^ { 2 } \mathsf { t } - ( 1 - \mathsf { b } ) \mathsf { t } \mathsf { V } ( \mathsf { x } _ { 2 } , \mathsf { d } \mathsf { t } ) } \\ & { } & { \mathsf { p } _ { 2 } ~ = ~ \mathsf { p } _ { 1 } ~ - ~ ( 1 - \mathsf { b } ) \mathsf { t } \mathsf { f } ( \mathsf { x } _ { 2 } , \mathsf { d } \mathsf { t } ) \qquad \mathsf { x } _ { 1 } ~ = ~ \mathsf { x } _ { 2 } ~ + ~ ( 1 - \mathsf { a } ) \mathsf { p } _ { 1 } \mathsf { t } ~ \bullet } \end{array}
$$

Subsituting into the Hamiltonian in Equation （1） andexpandingin the small parameter,t,we find(after somealgebra)

$$
\begin{array} { r l r } { \mathsf { H } _ { 2 } } & { = } & { \mathsf { \Lambda } _ { \mathsf { c } } ^ { \mathsf { c } } \mathsf { p } _ { 2 } \mathsf { f } \left( { x } _ { 2 } , 0 \right) \left[ \underline { { 2 } } \mathsf { b } \left( 1 - { \mathsf { a } } \right) \ - 1 \right] \_ + \ \mathsf { t } \mathsf { V } _ { \mathsf { t } } \left[ \underline { { \breve { \mathsf { I } } } } - 2 \mathsf { b } \mathsf { c } - 2 ( 1 - { \mathsf { b } } ) \frac { \mathsf { d } } { \mathsf { d } } \right] } \\ { \mathsf { + } \mathsf { t } ^ { 2 } \mathsf { p } _ { 2 } { \mathsf { \Lambda } } ^ { 2 } \mathsf { f } _ { \mathsf { x } } \left[ \underline { { \mathsf { \bar { \lambda } } } } ( 1 - { \mathsf { a } } ) ^ { 2 } \mathsf { b } / 2 - 1 / \underline { { \overline { { \mathsf { Z } } } } } \right] + \ \mathsf { t } ^ { 2 } \mathsf { V } _ { \mathsf { f } } \left[ \underline { { \breve { \lambda } } } / 2 - 3 \mathsf { b } \mathsf { c } ^ { 2 } / 2 - 3 ( 1 - { \mathsf { b } } ) \mathsf { d } ^ { 2 } / \frac { \overline { { \mathsf { Z } } } } { 2 } \right. } \\ { \mathsf { + } } & { \mathsf { t } ^ { 2 } \ \mathsf { f } _ { \mathsf { t } } \mathsf { p } _ { 2 } \left[ \underline { { \mathsf { \bar { \lambda } } } } \mathsf { c } \mathsf { b } \left( 1 - { \mathsf { a } } \right) - \underline { { \breve { \mathsf { I } } } } \right] } & { \left. \left( 2 \mathsf { f } \left( 1 - { \mathsf { a } } \right) - 1 \right) \mathsf { d } ^ { 2 } \mathsf { b } \right] } \\ { + } & { \mathsf { t } ^ { 2 } \mathsf { f } ^ { 2 } \left[ 2 \left( 1 - { \mathsf { a } } \right) \left( 1 - { \mathsf { b } } \right) \mathsf { b } + { \mathsf { b } } ^ { 2 } \left( 1 - { \mathsf { a } } \right) / 2 - { \mathsf { a } } \mathsf { b } - \left( 1 - { \mathsf { b } } \right) \frac { \mathsf { d } } { \mathsf { d } } \right] } & { + \ { \mathsf { O } } ( \mathsf { t } ^ { 3 } ) . } \end{array}
$$

The philosophy of selecting the free parameters in this case is the same as in previous sections with one exception.Since there aremore equationsthan unknowns,it is impossible to eliminate all second order termsat this step. However,another transformation can remove the remaining terms,provided that the equation for the momentum transformation is trivial to invert.Anticipating this problem,first eliminate all terms in Equation(20）with powers of $\mathsf { p } _ { 2 }$ ；This yields 3 equations for 3 unknowns with the solutions,

$$
b = 3 / 4 a = 1 / 3 , c = 2 / 3 .
$$

In addition the terms with time derivatives both vanish with the choice

$$
{ \texttt { d } } = { \texttt { 0 } } .
$$

With this choice of parameters ${ \sf H } _ { 2 }$ becomes

$$
H _ { 2 } = - t ^ { 2 } f ^ { 2 } ( x _ { 2 } , 0 ) / 1 6 + 0 ( t ^ { 3 } ) .
$$

The transformation to eliminate the last $0 ( t ^ { 2 } )$ termis

$$
\begin{array} { r c l } { { \sf F ( x _ { 3 } , p _ { 2 } ) } } & { { = } } & { { \mathrm { \bf ~ - ~ \ c _ { 3 } ~ p _ { 2 } ~ + ~ \ c ^ { 3 } ~ f ^ { 2 } ( ~ x _ { 3 } ~ , 0 ) / 4 8 ~ } } } \\ { { \mathrm { \bf ~ \ p _ { 3 } ~ = ~ \ p _ { 2 } ~ - ~ \ c ^ { 3 } \sf f f _ { \sf X } ( x _ { 3 } , 0 ) / 2 4 ~ } } } & { { \mathrm { \bf ~ x _ { 2 } ~ = ~ \ x _ { 3 } ~ } } } \end{array}
$$

However,since $\boldsymbol { \mathsf { X } }$ is changed,we can simply combine the previous transformation with the second one in Eq (19).

Therefore， if we rewrite with the change of notation $x _ { 2 } + x _ { 0 }$ ，generalise to the multidimensional case，and rewrite the transformations in the opposite order,we find a third order symplectic map given by the following scheine:

$$
\vec { \mathsf { p } } _ { 1 } = \vec { \mathsf { p } } _ { 0 } + \frac { 1 } { 4 } \mathsf { h } \vec { \mathsf { f } } ( \vec { \mathsf { x } } _ { 0 } , \mathsf { t } _ { 0 } ) + \frac { \mathsf { h } ^ { 3 } } { 4 8 } \vec { \nabla } \left[ \overline { { \mathsf { f } } } ( \vec { \mathsf { x } } _ { 0 } , \mathsf { t } _ { 0 } ) . \vec { \mathsf { f } } ( \vec { \mathsf { x } } _ { 0 } , \mathsf { t } _ { 0 } ) \right]
$$

$$
\vec { \sf x } _ { 1 } = \vec { \sf x } _ { 0 } + 2 { \sf h } \vec { \sf p } _ { 1 } / 3
$$

$$
\vec { \mathsf { p } } = \vec { \mathsf { p } } _ { 1 } + \frac { 3 } { 4 } \mathsf { n } \vec { \mathsf { f } } ( \vec { \mathsf { x } } _ { 1 } , \mathsf { t } _ { 0 } + \frac { 2 } { 3 } \mathsf { n } ) \vec { \mathsf { x } } = \vec { \mathsf { x } } _ { 1 } + \frac { \mathsf { n } } { 3 } \vec { \mathsf { p } }
$$

# A More General Hamiltonian

Theprevioussectionshaveconsideredthe Hamiltonian in Equation （1）.In this section we treat a somewhat more general case given by

$$
H = g ( \vec { \mathsf { p } } ) + v ( \vec { \mathsf { x } } , t ) .
$$

Notice that a special case of Equation (26） is the Hamiltonian for relativistic motion.In that case

$$
g ( \vec { p } ) = c \sqrt { \vec { p } \cdot \vec { p } + m ^ { 2 } c ^ { 2 } } .
$$

In addition Equation （26）can be used for the case of motion ina magnetic field which is described by only one component of the vector potential (say $\mathsf { A } _ { z }$ .n this case the independent variable is Z rather than t. FortheHamiltonianinEquation（26），the "leap-frog"algorithm yields results correct through second order provided that it is modified as follows:

In this case it is necessary to perform a three step canonical transformation in order to avoid implicit expressions. Usingthe methods developed inthe previous sections,the third order map can be written as

$$
M a p : ( \vec { x } , \vec { p } ) = M _ { 3 } ( h ) ( \vec { x } _ { 0 } , \vec { p } _ { 0 } )
$$

$$
\begin{array} { r l r l r l } & { \log _ { 1 } } & { = } & { \vec { \mathsf { p } } _ { 0 } } & { + \mathtt { c } _ { 1 } \mathsf { h } ^ { \dag } ( \vec { \mathsf { x } } _ { 0 } , \mathsf { t } _ { 0 } ) } & { \vec { \mathsf { x } } _ { 1 } } & { = } & { \vec { \mathsf { x } } _ { 0 } } & { + \mathtt { d } _ { 1 } \mathsf { h } \frac { \mathtt { d } \mathtt { g } } { \mathtt { d } \vec { \mathsf { p } } } ( \vec { \mathsf { p } } _ { 1 } ) } \\ & { \quad \quad \mathsf { \xi } _ { 2 } } & { = } & { \vec { \mathsf { p } } _ { 1 } } & { + \mathtt { c } _ { 2 } \mathsf { h } ^ { \dag } ( \vec { \mathsf { x } } _ { 1 } , \mathsf { t } _ { 0 } + \mathtt { d } _ { 1 } \mathsf { h } ) } & { \vec { \mathsf { x } } _ { 2 } } & { = } & { \vec { \mathsf { x } } _ { 1 } } & { + \mathtt { d } _ { 2 } \mathsf { h } \frac { \mathtt { d } \mathtt { g } } { \mathtt { d } \vec { \mathsf { p } } } ( \vec { \mathsf { p } } _ { 2 } ) } \\ & { \quad \mathsf { 3 } ) } & { \vec { \mathsf { p } } } & { = } & { \vec { \mathsf { p } } _ { 2 } } & { + \mathtt { c } _ { 3 } \mathsf { h } \vec { \mathsf { f } } ( \vec { \mathsf { x } } _ { 2 } , \mathsf { t } _ { 0 } + \left( \mathtt { d } _ { 1 } + \mathtt { d } _ { 2 } \right) \mathsf { h } , \vec { \mathsf { x } } } & { = } & { \vec { \mathsf { x } } _ { 2 } } & { + \mathtt { d } _ { 3 } \mathsf { h } \frac { \mathtt { d } \mathtt { g } } { \mathtt { d } \vec { \mathsf { p } } } ( \vec { \mathsf { p } } ) } \end{array}
$$

The ${ \sf c } ^ { \prime } { \sf s }$ and ${ \sf d } ^ { \prime } { \sf s }$ must satisfy the following equations,

$$
\begin{array} { r l } & { \mathsf { c } _ { 1 } + \mathsf { c } _ { 2 } + \mathsf { c } _ { 3 } = 1 \cdot , \mathsf { d } _ { 1 } + \mathsf { d } _ { 2 } + \mathsf { d } _ { 3 } = 1 , \mathsf { c } _ { 2 } \mathsf { d } _ { 1 } + \mathsf { c } _ { 3 } \left( \mathsf { d } _ { 1 } + \mathsf { d } _ { 2 } \right) = 1 / 2 } \\ & { \mathsf { c } _ { 2 } { \mathsf { d } _ { 1 } } ^ { 2 } + \mathsf { c } _ { 3 } \left( \mathsf { d } _ { 1 } + \mathsf { d } _ { 2 } \right) ^ { 2 } = 1 / 3 , \mathsf { d } _ { 3 } + \mathsf { d } _ { 2 } \left( \mathsf { c } _ { 1 } + \mathsf { c } _ { 2 } \right) ^ { 2 } + \mathsf { d } _ { 1 } \mathsf { c } _ { 1 } { } ^ { 2 } = 1 / 3 } \end{array}
$$

Notice that there are five equations for six unknowns; thus,there are many solutions.One particularly simple solution is obtained by setting $d _ { 3 } = 1 ^ { 4 }$ .

$$
\begin{array} { l l l l l l l } { { \mathsf { C } _ { \mathrm { 1 } } } } & { { = } } & { { 7 / 2 4 } } & { { } } & { { \mathsf { c } _ { 2 } } } & { { = } } & { { 3 / 4 } } & { { \mathsf { c } _ { 3 } } } & { { = } } & { { - 1 / 2 4 } } \\ { { \mathsf { d } _ { \mathrm { 1 } } } } & { { = } } & { { 2 / 3 } } & { { } } & { { \mathsf { d } _ { 2 } } } & { { = } } & { { - 2 / 3 } } & { { \mathsf { d } _ { 3 } } } & { { = } } & { { 1 } } \end{array}
$$

Notice that this three step third order map has no derivative of the force.In that sense it is the simplest （aswell as the most general）obtained here.

# Conclusions and Speculations

Thepurpose of this note has been two-fold; firstly to present results for third order symplectic maps，and secondly to illustrate,in some detail,the method in orderto point the wayto higher order maps. The third order maps obtained are not unique.

The general Hamiltonian will probably always lead to implicit equations for the final state in terms of theinitial conditions；however,there is one other interesting Hamiltonian which may have an explicit high ordermap,

$$
H = [ \vec { p } - \vec { A } ( \vec { \bf x } , t ) ] ^ { 2 } / 2
$$

where A is just the vector potential for an electromagnetic field. In this case the troublesome term is

$$
\vec { \mathsf { p } } \cdot \vec { \mathsf { A } } .
$$

This leads to matrix inversion even in the first order case and for order higher than two,it may be difficult to obtain explicit formulae.However,it is probably possible to write down a second order map and may be possible to find an explicit third order map.

Again,this method is expressed for one full time step and thus may appear somewhat different than the typical implementation in a computer code.

In addition， it is possible to obtain a third order map for the more general Hamiltonian.

I would like to thank Elon Close，Joe Bisognano, and Victor Brady for useful discussions and especially Jackson Laslett for suggesting the problem and for implementing these methods in ongoing research on nonlineardifferential equations.

# Acknowledgements

# References

1）F.B.Hildebrand,Introduction to Numerical Analysis NewYork,McGraw-HiT1（1974）   
2）L.Jackson Laslett，private communication.   
3)H.Goldstein,Classical Mechanics, Addison-Wesley（1965）p.242.   
4)Noticed by Victor Brady at Lawrence Berkeley Lab.