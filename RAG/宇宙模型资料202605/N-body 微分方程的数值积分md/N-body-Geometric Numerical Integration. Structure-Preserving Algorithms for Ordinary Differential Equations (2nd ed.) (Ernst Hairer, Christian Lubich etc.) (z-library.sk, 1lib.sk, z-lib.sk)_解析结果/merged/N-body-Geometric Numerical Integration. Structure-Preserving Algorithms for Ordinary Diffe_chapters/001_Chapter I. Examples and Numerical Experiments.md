# Chapter I. Examples and Numerical Experiments

Thischapter introduces some interesting examples of differential equations and illustrates different types of qualitative behaviour of numerical methods.Wedeliberatelyconsider only very simple numerical methods of orders1and 2toemphasize thequalitative aspects of the experiments.The same effects(on adifferent scale) occurwith more sophisticated higher-order integration schemes.The experiments presented here should serveasamotivation for the theoretical and practical investigations of later chapters.Thereader is encouraged to repeat the experiments or to invent similar ones.

# I.1 First Problems and Methods

Numerical applications of the case of two dependent variables are not easily obtained. (A.J.Lotka 1925,p.79)

Ourfirst problems,theLotka-Volterra model and thependulum equation,are differential equations in two dimensions and showalready many interesting geometric properties.Our first methodsare various variants of the Euler method,themidpoint rule,and the Stormer-Verletscheme.

# I.1.1 TheLotka-Volterra Model

Westart with anequation from mathematical biologywhich models the growth of animal species.Ifareal variable $u ( t )$ istorepresent the number of individuals ofa certain species at time $t$ ,the simplest assumption about its evolution is $d u / d t = u \cdot \alpha .$ , where $\alpha$ isthereproduction rate.Aconstant $\alpha$ leads to exponential growth.Inthe case of more species living together,the reproduction rates will also depend on thepopulation numbers of the other species.For example,for two specieswith $u ( t )$ denoting the number of predators and $v ( t )$ thenumber of prey,aplausible assumptionismadebytheLotka-Volterramodel

$$
\begin{array} { r } { \dot { u } = u ( v - 2 ) } \\ { \dot { v } = v ( 1 - u ) , } \end{array}
$$

where the dots on $u$ and $\upsilon$ stand for differentiationwith respect to time.(We have chosen the constants2and $^ { 1 }$ in（1.1）arbitrarily.)A.J.Lotka（1925,Chap.VIII)used

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/f979493c656c6fb111c9b2491b3051c3e1258a6222ce62640458d483a0d27456.jpg)  
Fig.1.1.Vector field,exact flow,and numerical flow for theLotka-Volterra model(1.1)

thismodel tostudy parasiticinvasion of insect species,and,withits help,V.Volterra （1927)explained curious fishingdata from theupper Adriatic Sea followingWorld WarI.

Equations（1.1）constitute an autonomous system of differential equations.In general,we write such a system inthe form

$$
\dot { y } = f ( y ) ~ .
$$

Every $y$ representsa point in the phase space,inequation(1.1） above $y = ( u , v )$ is in the phase plane $\mathbb { R } ^ { 2 }$ .Thevector-valued function $f ( y )$ represents avectorfield which,at any point of the phase space,prescribes the velocity(directionand speed) of the solution $y ( t )$ that passes through that point (see the first picture of Fig.1.1).

FortheLotka-Volterra model,we observe that the systemcycles through three stages:（1） the prey population increases;(2) the predator population increases by feeding on theprey;(3) the predator population diminishes due to lack of food.

Flowofthe System.A fundamental concept isthe flow over time $t$ Thisisthe mappingwhich,toanypoint $y _ { 0 }$ inthe phase space,associates the value $y ( t )$ ofthe solution with initial value $y ( 0 ) = y _ { 0 } .$ Thismap,denoted by $\varphi _ { t }$ ,isthusdefined by

$$
\varphi _ { t } ( y _ { 0 } ) = y ( t ) \quad { \mathrm { ~ i f ~ } } \quad y ( 0 ) = y _ { 0 } .
$$

The second picture of Fig.1.1 shows the results of three iterations of $\varphi _ { t }$ （with $t =$ 1.3)for theLotka-Volterraproblem,forasetof initial values $y _ { 0 } = ( u _ { 0 } , v _ { 0 } )$ forming ananimal-shaped set $A$ .1

Invariants.Ifwe divide the two equations of(1.1) by each other,we obtainasingle equation between the variables $u$ and $\boldsymbol { v }$ Afterseparation ofvariableswe get

$$
0 = { \frac { 1 - u } { u } } { \dot { u } } - { \frac { v - 2 } { v } } { \dot { v } } = { \frac { d } { d t } } I ( u , v )
$$

where

$$
I ( u , v ) = \ln u - u + 2 \ln v - v ,
$$

so that $I ( u ( t ) , v ( t ) ) = C o n s t$ forall $t$ We call the function $I$ an invariant of the system(1.1).Everysolutionof(1.1）thuslies ona level curve of(1.4).Someof these curvesare drawn in thepictures of Fig.1.1.Since the level curves are closed, all solutions of(1.1) are periodic.

# I.1.2First Numerical Methods

Explicit Euler Method.The simplest of all numerical methods for the system(1.2) is the method formulated by Euler(1768),

$$
y _ { n + 1 } = y _ { n } + h f ( y _ { n } ) .
$$

It uses aconstant step size $h$ to compute,one after the other,approximations $y _ { 1 }$ , $y _ { 2 }$ , $y _ { 3 } , . . .$ to the values $y ( h )$ ， $y ( 2 h )$ , $y ( 3 h )$ ， $\cdot \cdot \cdot$ of the solution starting from a given initialvalue $y ( 0 ) = y _ { 0 }$ Themethod iscalled theexplicit Eulermethod,because the approximation $y _ { n + 1 }$ is computed using an explicit evaluation of $f$ at thealready known value $y _ { n }$ Suchaformula representsamapping

$$
\varPhi _ { h } : y _ { n } \mapsto y _ { n - 1 } ,
$$

which wecallthe discrete or numerical flow.Some iterations of the discrete flow for theLotka-Volterra problem（1.1）（with $h = 0 . 5$ )arerepresented in the third picture ofFig.1.1.

Implicit EulerMethod.Theimplicit Eulermethod

$$
y _ { n + 1 } = y _ { n } + h f ( y _ { n + 1 } ) ,
$$

isknown for itsall-dampingstability properties.In contrast to (1.5),the approximation $y _ { n + 1 }$ isdefined implicitlyby(1.6),and the implementationrequires the numerical solution of a nonlinear system of equations.

Implicit Midpoint Rule. Taking the mean of $y _ { n }$ and $y _ { n + 1 }$ in theargument of $f$ ,we get the implicit midpointrule

$$
y _ { n + 1 } = y _ { n } + h f { \biggl ( } { \frac { y _ { n } + y _ { n + 1 } } { 2 } } { \biggr ) } .
$$

Itisasymmetricmethod,which means thatthe formula is left unaltered after exchanging $y _ { n }  y _ { n + 1 }$ and $h  - h$ (more on symmetric methods in Chap.V).

Symplectic EulerMethods.For partitioned systems

$$
\begin{array} { r } { \dot { u } = a ( u , v ) } \\ { \dot { v } = b ( u , v ) , } \end{array}
$$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/a14bfb7be88540d822b1f4aad06152eac37123520dd1e6b6e8540231c2e04e8a.jpg)  
Fig.1.2.Solutions of the Lotka-Volterra equations(1.1） (step sizes $h = 0 . 1 2$ initialvalues $( 2 , 2 )$ for the explicit Euler method, $( 4 , 8 )$ forthe implicit Euler method, $( 4 , 2 )$ and $( 6 , 2 )$ for the symplectic Euler method)

suchas the problem(1.1),we consider also partitioned Euler methods

$$
\begin{array} { r l } & { u _ { n + 1 } = u _ { n } + h a ( u _ { n } , v _ { n + 1 } ) \quad \mathrm { ~ o r ~ } \quad u _ { n + 1 } = u _ { n } + h a ( u _ { n + 1 } , v _ { n } ) } \\ & { v _ { n + 1 } = v _ { n } + h b ( u _ { n } , v _ { n + 1 } ) , \quad \mathrm { ~ o r ~ } \quad v _ { n + 1 } = v _ { n } + h b ( u _ { n + 1 } , v _ { n } ) , } \end{array}
$$

whichtreat one variablebythe implicitand the other variableby the explicitEuler method.In viewofan important propertyof thismethod,discovered byde Vogelaere (1956)and to be discussed in Chap.VI,we call them symplectic Euler methods.

Numerical Example for theLotka-Volterra Problem.Our first numerical experimentshows thebehaviour of thevariousnumerical methods applied to theLotka-Volterra problem.Inparticular,weare interested inthe preservationof theinvariant $I$ over long times.Fig.1.2 plotsthe numerical approximations of the first 125 steps with the above numerical methods applied to（1.I）,all with constant step sizes.We observe that the explicit and implicit Euler methods show wrong qualitative behaviour.The numerical solution either spirals outwards or inwards.The symplectic. Eulermethod (implicit in $u$ and explicit in $v$ however,givesa numerical solution that lies apparently onaclosed curveas does the exact solution.Note that thecurves of the numerical and exact solutions do not coincide.

# I.1.3The Pendulum asa Hamiltonian System

Agreat deal of attention in this book will be addressed to Hamiltonian problems, and our next exampleswill be of this type.These problemsare of the form

$$
\dot { p } = - H _ { q } ( p , q ) , \qquad \dot { q } = H _ { p } ( p , q ) ,
$$

where the Hamiltonian $H ( p _ { 1 } , \dots , p _ { d } , q _ { 1 } , \dots q _ { d } )$ represents the total energy; $q _ { i }$ are the position coordinates and $p _ { i }$ themomenta for $i = 1 , \ldots , d$ ,with $d$ thenumberof

degrees of freedom; $H _ { p }$ and $H _ { q }$ are the vectors of partial derivatives.One verifies easily by differentiation (see Sect.IV.1) that,along the solution curves of(1.10),

$$
H ( p ( t ) , q ( t ) ) = ( \gamma _ { O n S t } ,
$$

i.e.,theHamiltonianisan invariant ora first integral.Moredetailsabout Hamiltonian systems and their derivation from Lagrangian mechanicswill be given in Sect.VI.1.

Pendulum. The mathematical pendulum (mass $m = 1$ , massless rod of length $\ell \ = \ 1$ ，gravitational acceleration $g = 1$ ）isasystem with one degree of freedom having the Hamiltonian

$$
H ( p , q ) = { \frac { 1 } { 2 } } p ^ { 2 } - \cos q ,
$$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/a00bf95b299246332366b864f1d1e5e930fe3444b8e51c8fa76cc37d48b89413.jpg)

so that the equations of motion(1.10) become

$$
\dot { p } = - \sin q , \qquad \dot { q } = p .
$$

Since thevector feld(1.13)is $2 \pi$ -periodicin $q$ itis natural to consider $q$ asavariable on the circle $S ^ { 1 } .$ Hence,the phase space of points $( p , q )$ becomes thecylinder $\mathbb { R } \times S ^ { 1 } .$ Fig.1.3 shows some level curves of $H ( p , q ) .$ By(1.11),the solution curves of the problem(1.13) lie on such level curves.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/3c3bcfff00cd9d373ec258de63fc2a7f1ba532a62238ba6439f306fe68f8776e.jpg)  
Fig.1.3.Exact and numerical flow for the pendulum problem(1.13);step sizes $h = t = 1$

AreaPreservation.Figure 1.3（first picture）illustrates that the exact flow ofa Hamiltonian system(1.1O)is area preserving.This can be explained as follows:the derivative of the flow $\varphi _ { t }$ withrespect to initial values $( p , q )$ ,

$$
\varphi _ { t } ^ { \prime } ( p , q ) = \frac { \partial \big ( p ( t ) , q ( t ) \big ) } { \partial ( p , q ) } ,
$$

satisfies the variational equation ²

$$
\phi _ { t } ^ { \prime } ( p , q ) = \left( \begin{array} { c c } { { - H _ { p q } } } & { { - H _ { q q } } } \\ { { H _ { p p } } } & { { H _ { q p } } } \end{array} \right) \varphi _ { t } ^ { \prime } ( p , q ) ,
$$

where the second partial derivatives of $H$ areevaluatedat $\varphi _ { t } ( p , q )$ Inthe case of onedegree of freedom（ $d = 1$ ),asimple computation shows that

$$
\frac { d } { d t } \operatorname* { d e t } \varphi _ { t } ^ { \prime } ( p , q ) = \frac { d } { d t } \Big ( \frac { \partial p ( t ) } { \partial p } \frac { \partial q ( t ) } { \partial q } - \frac { \partial p ( t ) } { \partial q } \frac { \partial q ( t ) } { \partial p } \Big ) = . . . . = 0 .
$$

Since $\varphi _ { 0 }$ is the identity,this implies $\operatorname* { d e t } \varphi _ { t } ^ { \prime } ( p , q ) = 1$ forall $t$ ,which means that the flow $\varphi _ { t } ( p , q )$ isan area-preservingmapping.

Thelast two pictures of Fig.1.3 show numerical flows.The explicit Euler method is clearly seen nottopreservearea but the symplectic Eulermethod is(this will be proved in Sect.VI.3).One of the aims of'geometric integration'is the study of numerical integrators that preserve such types of qualitative behaviour of the exact flow.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/6ba452de74af458f19ed71163d1d7d4c784ea315e166c9aa76fd886e8b9d5ba1.jpg)  
Fig.1.4.Solutions of thependulum problem（1.13)；explicit Euler with step size $h = 0 . 2$ ， initialvalue $( p _ { 0 } , q _ { 0 } ) = ( 0 , 0 . 5 )$ symplectic Eulerwith $h = 0 . 3$ and initialvalues $q _ { 0 } = 0$ , $p _ { 0 } = 0 . 7 , 1 . 4 , 2 . 1$ ;Stormer-Verletwith $h = 0 . 6$

Numerical Experiment.We applythe above numerical methods to the pendulum equations(see Fig.1.4）.Similar to the computations for theLotka-Volterra equations,we observe that the numerical solutions of the explicit Euler and of the implicitEulermethod (not drawn in Fig.1.4） spiral either outwards or inwards.The symplectic Euler method shows the correct qualitative behaviour,but destroys the left-right symmetry of theproblem.The Stormer-Verlet scheme,whichwediscuss next,works perfectly even with doubled step size.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/7d3786d6f5ce024154491d9d2c95408d9bc4dba3e742f1155c6edb97a80f268e.jpg)  
Fig.1.5.Carl Stormer(left picture),born:3September 1874in Skien(Norway),died:13August 1957. Loup Verlet(right picture),born:24May1931in Paris

# I.1.4The Stormer-Verlet Scheme

Theabove equations(1.13) for the pendulumare of the form

$$
{ \begin{array} { r l r l r l } & { { \dot { p } } = f ( q ) } & & { \quad { \mathrm { ~ o r ~ } } \quad { \ddot { q } } = f ( q ) } \\ & { { \dot { q } } = p } \end{array} }
$$

which is the important special case of a second order differential equation.The most natural discretization of（1.14）is

$$
q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = h ^ { 2 } f ( q _ { n } ) ,
$$

whichis just obtained byreplacing the second derivativein(1.14)by the central second-orderdifference quotient.This basic method,or its equivalent formulation givenbelow,iscalledtheStormermethodinastronomy,theVerletmethod³inmoleculardynamics,the leap-frogmethodinthecontext of partial differential equations, andit has further names inotherareas (see Hairer,Lubich&Wanner(2Oo3),p.402). C.Stormer (19o7)used higher-order variants for numerical computations concerningtheaurora borealis.L.Verlet（1967）proposed thismethod for computations in moleculardynamics,where it has becomeby farthemostwidelyused integration scheme.

Geometrically,the Stormer-Verlet methodcan beseenasproduced by parabolas,which in the points $t _ { n }$ possess the right second derivative $f ( q _ { n } )$ (seeFig.1.6 to the left).But we can also think of polygons,which possess the right slope in the midpoints(Fig.1.6to the right).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/163ba1c0a33202cd06df1bfdeae6a3f8063f068050293fb244671c84c9544c75.jpg)  
Fig.1.6.Illustration for the Stormer-Verlet method

Approximations to thederivative $p = \dot { q }$ are simply obtained by

$$
p _ { n } = { \frac { q _ { n + 1 } - q _ { n - 1 } } { 2 h } } \quad \quad { \mathrm { a n d } } \quad \quad p _ { n + 1 / 2 } = { \frac { q _ { n + 1 } - q _ { n } } { h } } ,
$$

One-Step Formulation.The Stormer-Verlet method admitsaone-step formulation which is useful for actual computations.The value $q _ { n }$ together with the slope $p _ { n }$ and the second derivative $f ( q _ { n } )$ ,allat $t _ { n }$ ,uniquelydetermine theparabolaand hence also the approximation $\left( p _ { n + 1 } , q _ { n + 1 } \right)$ at $t _ { n + 1 } .$ Writing(1.15)as $p _ { n + 1 / 2 } - p _ { n - 1 / 2 } =$ $h f ( q _ { n } )$ and using $p _ { n + 1 / 2 } + p _ { n - 1 / 2 } = 2 p _ { n } ,$ wegetby elimination of either $p _ { n + 1 / 2 }$ orpn-1/2 the formulae

$$
\begin{array} { r c l } { { } } & { { } } & { { p _ { n + 1 / 2 } ~ = ~ p _ { n } + \displaystyle \frac { h } { 2 } ~ f ( q _ { n } ) } } \\ { { } } & { { } } & { { q _ { n + 1 } ~ = ~ q _ { n } + h p _ { n + 1 / 2 } } } \\ { { } } & { { } } & { { p _ { n + 1 } ~ = ~ p _ { n + 1 / 2 } + \displaystyle \frac { h } { 2 } ~ f ( q _ { n + 1 } ) } } \end{array}
$$

which is an explicit one-step method $\phi _ { h } : ( q _ { n } , p _ { n } ) \longmapsto ( q _ { n + 1 } , p _ { n + 1 } )$ for the corresponding first order system of(1.14). If one isnot interested in the values $p _ { n }$ ofthe derivative,the firstand third equationsin (1.17) can be replaced by

$$
\begin{array} { r } { p _ { n + 1 / 2 } = p _ { n - 1 / 2 } + h f ( q _ { n } ) . } \end{array}
$$

# I.2 TheKepler Problemand the Outer Solar System

Iawoke as if from sleep,anew light broke on me. (J.Kepler;quoted fromJ.L.E.Dreyer,Ahistoryofastronomy,1906,Dover1953,p.391)

Oneof the great achievementsin the history of science was the discovery of the lawsof J.Kepler(16o9),based on manyprecisemeasurements of the positions-of Marsby Tycho Braheand himself.Theplanetsmoveinelliptic orbitswith the sun at one of the foci(Kepler's first law)

$$
r = { \frac { d } { 1 + e \cos \varphi } } = a - a e \cos E ,
$$

(where $a \quad =$ greataxis, $e \quad =$ eccentricity, $\begin{array} { r l } { b } & { { } = } \end{array}$ $a { \sqrt { 1 - e ^ { 2 } } }$ ， $d = b { \sqrt { 1 - e ^ { 2 } } } = a ( 1 - e ^ { 2 } )$ , $E = \operatorname { e c } .$ centricanomaly, $\varphi =$ trueanomaly).

Newton (Principia 1687)then explained this motion by his general law of gravitational attraction （proportional to $1 / r ^ { 2 }$ )andtherelation between forcesand acceleration(the“Lex II'of the Principia).This then opened the way for treating arbitrarycelestial motions by solvingdifferential equations.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/b26a557064e211c584098e905881f733983cbd1550f270fc3924de2a84da83a0.jpg)

Two-Body Problem.For computing the motion of two bodies which attract each other,we choose one of the bodies as the centre of our coordinate system;the motion will then stay ina plane (Exercise 3)and we can use two-dimensional coordinates $q \ = \ ( q _ { 1 } , q _ { 2 } )$ forthe position of the second body.Newton's laws,with asuitable normalization,then yield the followingdifferential equations

$$
\ddot { q } _ { 1 } = - \frac { q _ { 1 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } ; \qquad \ddot { q } _ { 2 } = - \frac { q _ { 2 } } { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 / 2 } } .
$$

This is equivalent toa Hamiltonian system with the Hamiltonian

$$
H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = \frac { 1 } { 2 } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } , \qquad p _ { i } = \ddot { q } _ { i } .
$$

# 1.2.1 Angular Momentumand Kepler's Second Law

The system hasnot only the total energy $H ( p , q )$ asafirstintegralbutalsothe angularmomentum

$$
L ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 } .
$$

Thiscan bechecked by differentiationand isnothing other than Kepler's second law,which says that the ray $F M$ sweeps equal areas in equal times (see the litle picture at the beginning of Sect.I.2).

Abeautiful geometric justification of this law is due to I.Newton4(Principia （1687),BookI,figure forTheoremI).Theidea istoapplythe Stormer-Verlet scheme(1.15） to the equations(2.2）(see Fig.2.1).Byhypothesis,the diagonal of the parallelogram $q _ { n - 1 } q _ { n } q _ { n + 1 }$ ,whichis $\left( q _ { n + 1 } - q _ { n } \right) - \left( q _ { n } - q _ { n - 1 } \right) \ =$ $q _ { n + 1 } - 2 q _ { n } + q _ { n - 1 } = C o n s t \cdot f ( q _ { n } )$ ,points towards the sun $S$ Therefore,the altitudes of the triangles $q _ { n - 1 } q _ { n } S$ and $q _ { n + 1 } q _ { n } S$ are equal.Since they have the common base $q _ { n } S$ ,they also haveequal areas.Hence

$$
\operatorname* { d e t } ( q _ { n - 1 } , q _ { n } - q _ { n - 1 } ) = \operatorname* { d e t } ( q _ { n } , q _ { n + 1 } - q _ { n } )
$$

and by passing to the limit $h  0$ we see that $\operatorname* { d e t } ( q , p ) = C o n s t .$ This is (2.4).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/b971014a5d1d803acefe0d11b3f9997ed4870ddbaaa8be94d867bd66eb0d4ad3.jpg)  
Fig.2.1.ProofofKepler'sSecondLaw(left);facsimilefromNewton’sPrincipia (right)

Wehave not only an elegant proof for this invariant,but wealso see that the Stormer-Verlet schemepreserves thisinvariant forevery $h > 0$ .

# 1.2.2Exact Integration of the Kepler Problem

Pour voir présentement que cette courbe $A B C$ ...est toujours une SectionConique,ainsique Mr.Newton I'a suppose,pag.55.Coroll.I.sans le demontrer;ily faut bienplusd'adresse: （Joh.Bernoulli1710,p.475）

Itis now interesting,inversely to the procedureof Newton,toprove that any solution of(2.2)follows either an elliptic,parabolic or hyperbolic arc and to describe the solutionsanalytically.Thiswas first done by Joh.Bernoulli(171o,full of sarcasm against Newton),and byNewton(1713,second edition of the Principia,without mentioningaword about Bernoulli).

By(2.3)and(2.4),every solution of(2.2) satisfies the two relations

$$
\frac { 1 } { 2 } \left( \dot { q } _ { 1 } ^ { 2 } + \dot { q } _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } = H _ { 0 \ast } ~ q _ { 1 } \dot { q } _ { 2 } - q _ { 2 } \dot { q } _ { 1 } = L _ { 0 } ,
$$

where the constants $H _ { 0 }$ and $L _ { 0 }$ aredetermined by the initial values.Usingpolar coordinates $q _ { 1 } = r \cos \varphi$ , $q _ { 2 } = r \sin \varphi$ ,thissystem becomes

$$
{ \frac { 1 } { 2 } } \left( { \dot { r } } ^ { 2 } + r ^ { 2 } { \dot { \varphi } } ^ { 2 } \right) - { \frac { 1 } { r } } = H _ { 0 } , \qquad r ^ { 2 } \dot { \varphi } = L _ { 0 } .
$$

Forits solution weconsider $r$ as a function of $\varphi$ and write $\begin{array} { r } { \dot { r } = \frac { d r } { d \varphi } \cdot \dot { \varphi } . } \end{array}$ The elimination of $\dot { \varphi }$ in(2.6）then yields

$$
{ \frac { 1 } { 2 } } \left( \left( { \frac { d r } { d \varphi } } \right) ^ { 2 } + r ^ { 2 } \right) { \frac { L _ { 0 } ^ { 2 } } { r ^ { 4 } } } - { \frac { 1 } { r } } = H _ { 0 } .
$$

In this equation we use the substitution $r = 1 / u$ ， $d r = - d u / u ^ { 2 }$ which gives (with $\prime = d / d \varphi$ ）

$$
\frac { 1 } { 2 } ( u ^ { \prime 2 } + u ^ { 2 } ) - \frac { u } { L _ { 0 } ^ { 2 } } - \frac { H _ { 0 } } { L _ { 0 } ^ { 2 } } = 0 .
$$

This isa“Hamiltonian”for the system

$$
u ^ { \prime \prime } + u = { \frac { 1 } { d } } \quad \mathrm { i . e . , } \quad u = { \frac { 1 } { d } } + c _ { 1 } \cos \varphi + c _ { 2 } \sin \varphi = { \frac { 1 + e \cos ( \varphi - \varphi ^ { * } ) } { d } }
$$

where $d = L _ { 0 } ^ { 2 }$ and the constant $e$ becomes,from (2.7),

$$
e ^ { 2 } = 1 + 2 H _ { 0 } L _ { 0 } ^ { 2 }
$$

(byExercise7,the expression $1 + 2 H _ { 0 } L _ { 0 } ^ { 2 }$ is non-negative).This is precisely formula (2.1).The angle $\varphi ^ { * }$ isdetermined by the initial values $r _ { 0 }$ and $\varphi _ { 0 }$ .Equation (2.1) represents an elliptic orbit with eccentricity $e$ for $H _ { 0 } < 0$ (seeFig.2.2,dotted line), aparabola for $H _ { 0 } = 0$ ,andahyperbolafor $H _ { 0 } > 0$ .

Finally,we must determine the variables $\boldsymbol { r }$ and $\varphi$ as functions of $t$ With the relation (2.8)and $r = 1 / u$ ,the second equation of(2.6) gives

$$
\frac { d ^ { 2 } } { \left( 1 + e \cos ( \varphi - \varphi ^ { \ast } ) \right) ^ { 2 } } d \varphi = L _ { 0 } d t
$$

which,afteranelementary,butnoteasy,integration,representsanimplicitequation for $\varphi ( t )$

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/ce60f4ec881a29b5dbeb510e7aaa4b303d9c35f40519c1b76d0c89202511d4cf.jpg)  
Fig.2.2.Numerical solutions of the Kepler problem (eccentricity $e ~ = ~ 0 . 6$ indots:exact solution)

# 1.2.3Numerical Integration of the Kepler Problem

Forthe problem(2.2）we choose,with $0 \leq e < 1$ ,theinitial values

$$
q _ { 1 } ( 0 ) = 1 - e , \quad q _ { 2 } ( 0 ) = 0 , \quad \dot { q } _ { 1 } ( 0 ) = 0 , \quad \dot { q } _ { 2 } ( 0 ) = \sqrt { \frac { 1 + e } { 1 - e } } .
$$

This implies that $H _ { 0 } = - 1 / 2$ , $L _ { 0 } = \sqrt { 1 - e ^ { 2 } }$ , $d = 1 - e ^ { 2 }$ and $\varphi ^ { * } = 0$ Theperiod of the solution is $2 \pi$ (Exercise5).Fig.2.2 shows some numerical solutions for the eccentricity $e = 0 . 6$ compared to the exact solution.After our previous experience, it isno longera surprise that the explicit Euler method spirals outwards and gives a completelywronganswer.Forthe other methods we takeastep size1OO times larger in order to“see something".We see that the nonsymmetric symplectic Euler method distorts the ellipse,and that all methods exhibita precession effect,clockwise for Stormer-Verlet and symplectic Euler,anti-clockwise for the implicit midpoint rule. Thesame behaviour occurs for the exact solution of perturbed Keplerproblems (Exercise 12)and has occupied astronomers for centuries.

Ournext experiment(Fig.2.3） studies the conservation of invariantsand the global error.Themain observationis that the errorinthe energy grows linearly for the explicit Euler method,and itremains boundedand small(no secular terms) for thesymplectic Euler method.The global error,measured in the Euclideannorm, showsaquadratic growth for the explicit Euler compared toa linear growth for thesymplectic Euler.As indicated in Table2.1 theimplicit midpointruleand the Stormer-Verletscheme behave similarto the symplectic Euler,but havea smaller error dueto their higher order.We remark that the angularmomentum $L ( p , q )$ isexactlyconserved by thesymplectic Euler,theStormer-Verlet,and theimplicit midpoint rule.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/ca33a2bf16b816d57ab4dbaa71566faea7e78bb694fdba1479a48875591a8ce7.jpg)  
Fig.2.3.Energy conservation and global error for the Kepler problem

Table2.1.Qualitative long-time behaviour for theKepler problem; $t$ is time, $h$ the step size   

<table><tr><td>method</td><td>errorin H</td><td>error inL</td><td>global error</td></tr><tr><td>explicit Euler</td><td>O（th）</td><td>(th）</td><td>O(t²h)</td></tr><tr><td>symplectic Euler</td><td>O(h）</td><td>0</td><td>（th）</td></tr><tr><td>implicitmidpoint</td><td>O(h²）</td><td>0</td><td>O(th²)</td></tr><tr><td>Stormer-Verlet</td><td>O（h²）</td><td>0</td><td>O(th²)</td></tr></table>

# I.2.4 The Outer Solar System

Theevolution of the entire planetary system has been numericallyintegrated foratime spanofnearly 1oomillionyears.Thiscalculation confirms that the evolution of the solar system as a wholeis chaotic,...

(G.J.Sussman&J.Wisdom1992)

Wenext apply our methods to the system which describes the motion of the five outerplanetsrelative to the sun.This system has been studied extensively byastronomers.The problem isa Hamiltonian system (1.10)（ $N$ -bodyproblem)with

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 0 } ^ { 5 } \frac { 1 } { m _ { i } } p _ { i } ^ { T } p _ { i } - G \sum _ { i = 1 } ^ { 5 } \sum _ { j = 0 } ^ { i - 1 } \frac { m _ { i } m _ { j } } { \| q _ { i } - q _ { j } \| } .
$$

Here $p$ and $q$ are the supervectors composed by the vectors $p _ { i } , q _ { i } \in \mathbb { R } ^ { 3 }$ (momenta and positions),respectively.Thechosen units are:masses relativeto the sun,so that thesun hasmass1.We have taken

$$
m _ { 0 } = 1 . 0 0 0 0 0 5 9 7 6 8 2
$$

to takeaccount of the inner planets.Distances are in astronomical units $( 1 \left[ \mathrm { A . U . } \right] = $ 14959787O[km]),timesin earth days,and the gravitational constant is

$$
G = 2 . 9 5 9 1 2 2 0 8 2 8 6 \cdot 1 0 ^ { - 4 } .
$$

The initial values for the sun are taken as $q _ { 0 } ( 0 ) = ( 0 , 0 , 0 ) ^ { 1 }$ and $\dot { \boldsymbol { q } } _ { 0 } ( 0 ) = ( 0 , 0 , 0 ) ^ { T } .$ All other data (masses of the planetsand the initial positionsand initial velocities)aregivenin Table2.2.The initial datais taken from“AhnertsKalender fur Sternfreunde 1994",Johann AmbrosiusBarth Verlag1993,and they correspond to September5,1994at0h00.6

Table2.2.Data for the outersolar system   

<table><tr><td rowspan=1 colspan=1>planet</td><td rowspan=1 colspan=1>mass</td><td rowspan=1 colspan=1>initial position</td><td rowspan=1 colspan=1>initial velocity</td></tr><tr><td rowspan=1 colspan=1>Jupiter</td><td rowspan=1 colspan=1>m1=0.000954786104043</td><td rowspan=1 colspan=1>-3.5023653-3.8169847-1.5507963</td><td rowspan=1 colspan=1>0.00565429-0.00412490-0.00190589</td></tr><tr><td rowspan=1 colspan=1>Saturn</td><td rowspan=1 colspan=1>m2=0.000285583733151</td><td rowspan=1 colspan=1>9.0755314-3.0458353-1.6483708</td><td rowspan=1 colspan=1>0.001683180.004835250.00192462</td></tr><tr><td rowspan=1 colspan=1>Uranus</td><td rowspan=1 colspan=1>m3=0.0000437273164546</td><td rowspan=1 colspan=1>8.3101420-16.2901086-7.2521278</td><td rowspan=1 colspan=1>0.003541780.001371020.00055029</td></tr><tr><td rowspan=1 colspan=1>Neptune</td><td rowspan=1 colspan=1>m4=0.0000517759138449</td><td rowspan=1 colspan=1>11.4707666-25.7294829-10.8169456</td><td rowspan=1 colspan=1>0.002889300.001145270.00039677</td></tr><tr><td rowspan=1 colspan=1>Pluto</td><td rowspan=1 colspan=1>m5=1/(1.3.108）</td><td rowspan=1 colspan=1>-15.5387357-25.2225594-3.1902382</td><td rowspan=1 colspan=1>0.00276725-0.00170702-0.00136504</td></tr></table>

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/808b3dfbd3a8560f988602d39677b2698c4d2b51240ae013679c144be7e87fa6.jpg)  
Fig.2.4.Solutions of the outer solar system

To this system we apply the explicit and implicit Euler methods with step size $h = 1 0$ thesymplectic Euler and the Stormer-Verlet method with much larger step sizes $h = 1 0 0$ and $h = 2 0 0$ ,repectively,all overa timeperiodof 200000 days.The numerical solution (see Fig.2.4）behaves similarly to that forthe Kepler problem.With the explicit Euler method theplanets have increasing energy,they spiral outwards, Jupiter approaches Saturn which leaves theplane of the two-body motion.With the implicit Euler method the planets (first Jupiter and then Saturn)

fall into the sunand are thrown far away.Both the symplectic Euler method and the Stormer-Verlet scheme show the correct behaviour.Anintegration overa much longer time of say several million years does not deteriorate this behaviour.Letus remark thatSussman&Wisdom(1992) have integratedtheouter solar systemwith special geometric integrators.

# I.3The Henon-HeilesModel

..because:(1）itis analytically simple;this makes the computation of thetrajectorieseasy;(2)at the same time,itis sufficiently complicated to give trajectorieswhich are far from trivial. (Henon&Heiles1964）

TheHenon-Heiles model was created for describing stellar motion,followed for a verylong time,inside the gravitational potential $U _ { 0 } ( r , z )$ ofagalaxywithcylindrical symmetry(Henon&Heiles 1964).Exterisivenumerical experimentations should helpto answer the question,if thereexists,besides theknown invariants $H$ and $L$ , athird invariant.Despite endless tentatives of analytical calculations during many decades,sucha formula had not been found.

Afterareduction of the dimension,a Hamiltonian in twodegrees of freedom of theform

$$
H ( p , q ) = { \frac { 1 } { 2 } } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) + U ( q )
$$

isobtained and the questionis,if such an equation hasa second invariant.Here, Henon and Heiles put aside the astronomical origin of the problem and choose

$$
U ( q ) = \frac { 1 } { 2 } ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) + q _ { 1 } ^ { 2 } q _ { 2 } - \frac { 1 } { 3 } q _ { 2 } ^ { 3 }
$$

(see citation).The potential $U$ isrepresented inFig.3.1.When $U$ approaches $\textstyle { \frac { 1 } { 6 } }$ ,the level curves of $U$ tend toan equilateral triangle,whose vertices are saddle points of $U .$ The corresponding system

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/eb0e63819e8a0c402825778deef29348eae82c1479c19bd5dd8223bf0a59c728.jpg)  
Fig.3.1.Potentialof theHenon-HeilesModelandasolution

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/3543500487d3610984a5128a428bd5c4b33a85c6f77af27fafb989aac380a055.jpg)  
Fig.3.2.Poincare cuts for $q _ { 1 } = 0 , p _ { 1 } > 0$ of the Henon-HeilesModel for $\begin{array} { r } { H = \frac { 1 } { 1 2 } } \end{array}$ (6 orbits,left)and $\begin{array} { r } { H = \frac { 1 } { 8 } } \end{array}$ (1orbit,right）

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/8774bd47cd62afd1030e0900d91a363b045095246206dbe12323ec307215708a.jpg)  
Fig.3.3.Poincaré cuts for numerical methods,one orbit each;explicit Euler (left),implicit Euler(right).Same initial data as in Fig.3.2

$$
\ddot { q } _ { 1 } = - q _ { 1 } - 2 q _ { 1 } q _ { 2 } , \qquad \ddot { q } _ { 2 } = - q _ { 2 } - q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 }
$$

has solutions with nontrivial properties.For given initial values with $H ( p _ { 0 } , q _ { 0 } ) < \frac { 1 } { 6 }$ and $q _ { 0 }$ inside the triangle $U \leq \frac { 1 } { 6 }$ ,the solution stays there and moves somehowlike amass point gliding on this surface (see Fig.3.1,right).

PoincaréCuts.Wefix first theenergy $H _ { 0 }$ and put $q _ { 1 0 } = 0$ Then for any point $P _ { 0 } = ( q _ { 2 0 } , p _ { 2 0 } )$ ,we obtain $p _ { 1 0 }$ from (3.1)as $p _ { 1 0 } = \sqrt { 2 H _ { 0 } - 2 U _ { 0 } - p _ { 2 0 } ^ { 2 } }$ ,wherewe choose thepositiveroot.We then follow the solution until it hits again the surface $q _ { 1 } = 0$ in the positive direction $p _ { 1 } > 0$ and obtainapoint $P _ { 1 } = ( q _ { 2 1 } , p _ { 2 1 } )$ ;inthe same way we compute $P _ { 2 } = ( q _ { 2 2 } , p _ { 2 2 } )$ ,etc.For the same initial values as in Fig.3.1 and with $\begin{array} { r } { H _ { 0 } = \frac { 1 } { 1 2 } } \end{array}$ ,the solution for $0 \leq t \leq 3 0 0 0 0 0$ gives $4 6 8 6 5$ Poincarecuts whichareall displayedinFig.3.2(left).They seem to lie exactly onacurve,as do theorbits for5other choices of initial values.This picture thus shows“convincing evidence"for the existence ofa second invariant,for which Gustavson(1966) has deriveda formal expansion,whose first termsrepresent perfectly these curves.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/14d0fcca30639e49ac8b342a015b6716b82ec46cc968e86f7e4794d80c75aa59.jpg)  
Fig.3.4.Global error of numerical methods for nearly quasiperiodicand for chaotic solutions; same initial data asin Fig.3.2

“Butherecomes the surprise”(Henon-Heiles,p.76):Fig.3.2 shows to the right the same picture in the $\left( q _ { 2 } , p _ { 2 } \right)$ plane forasomewhat higher Energy $\begin{array} { r } { H = \frac { 1 } { 8 } } \end{array}$ The motion turnscompletely to chaosand all hope forasecond invariant disappears. Actually,Gustavson's series does not converge.

Numerical Experiments.We nowapply numerical methods,the explicit Euler method to the low energy initial values $\begin{array} { r } { H = \frac { 1 } { 1 2 } } \end{array}$ (Fig.3.3,left),and the implicit Eulermethod to the high energyinitial values(Fig.3.3,right),both methodswitha very small step size $h = 1 0 ^ { - 5 }$ Aswe already expect from ourprevious experiences, theexplicit Euler method tends to increase the energy and turns order intochaos, while the implicit Euler method tendstodecrease itand turns chaos into order.The Stormer-Verlet method(not shown) behaves as the exact solution even for step sizes as large as $h = 1 0 ^ { - 1 }$ ,

In ournext experimentwe study the global error(see Fig.3.4),once for thecase of thenearly quasiperiodic orbit（ $H = \textstyle { \frac { 1 } { 1 2 } }$ ）and once for the chaotic one( $H = \textstyle { \frac { 1 } { 8 } }$ ), both for the explicit Euler,the symplectic Euler,and the Stormer-Verlet scheme. Itmay come asa surprise,that only in the first case we have the same behaviour (linear orquadratic growth) as in Fig.2.3 for the Kepler problem.In the second case ( $H = \textstyle { \frac { 1 } { 8 } }$ )theglobal error growsexponentially forall methods,and the explicit Euler method isworst.

Studyof aMapping.Thepassage fromapoint $P _ { i }$ to the next one $P _ { i + 1 }$ (asexplained forthe left picture of Fig.3.2)can beconsidered asa mapping $\varPhi : P _ { i } \mapsto$ $P _ { i + 1 }$ and the sequence of points $P _ { 0 } , P _ { 1 } , P _ { 2 } , \ldots$ are just the iterates of this mapping. Thismappingisrepresentedforthetwoenergy levels $H = \textstyle { \frac { 1 } { 1 2 } }$ and $H \ = \ { \textstyle \frac { 1 } { 8 } }$ in Fig.3.5and its study allowsto better understand thebehaviour of the orbits.We see no significant difference between the two cases,simply for larger $H$ thedeformationsare more violent and correspond to larger eigenvalues of the Jacobian of $\phi .$ In both cases we have seven fixed points,which correspond to periodic solutions of the system(3.3).Four of themare stableand lieinsidethewhite islands ofFig.3.2.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/247b477cafac3f341fb38df08f0621bb87a0a10611d0b2d621fe659702b06c03.jpg)  
Fig.3.5.The Poincaremap $\varPhi : P _ { 0 }  P _ { 1 }$ fortheHenon-Heiles Model

# I.4 Molecular Dynamics

Wedonot need exact classical trajectories todo this,but must laygreat emphasis on energyconservationas being of primary importance for this reason. (M.P.Allen&D.J.Tildesley1987)

Molecular dynamics requires the solution of Hamiltonian systems(1.1O),where the otalenergy is given by

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { N } \frac { 1 } { m _ { i } } p _ { i } ^ { T } p _ { i } + \sum _ { i = 2 } ^ { N } \sum _ { j = 1 } ^ { i - 1 } V _ { i j } \Bigl ( \lVert q _ { i } - q _ { j } \rVert \Bigr ) ,
$$

and $V _ { i j } ( r )$ are given potential functions.Here. $q _ { i }$ and $p _ { i }$ denote the positions and momenta of atoms and $m _ { i }$ istheatomicmassof theithatom.Weremark that the outer solar system (2.12)is such an $N$ -bodysystemwith $V _ { i j } ( r ) = - G m _ { i } m _ { j } / r .$ In moleculardynamics the Lennard-Jones potential

$$
V _ { i j } ( r ) = 4 \varepsilon _ { i j } \bigg ( \Big ( \frac { \sigma _ { i j } } { r } \Big ) ^ { 1 2 } - \Big ( \frac { \sigma _ { i j } } { r } \Big ) ^ { 6 } \bigg )
$$

isverypopular（ $\varepsilon _ { i j }$ and $\sigma _ { i j }$ are suitable constants depending on the atoms). This potential has an absolute minimum atdistance $r = \sigma _ { i j } \sqrt { 2 }$ The forcedue to thispotential strongly repels theatoms when they are closer than this value, and they atract each other when they are farther away.

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/981ba1e67a3420f8a6126b5bc217aa8dc5adaffdb763fe60b9c2791d46da2d7e.jpg)

Numerical Experiments with a Frozen Argon Crystal.AsinBiesiadecki& Skeel（1993）weconsider the interaction of seven argon atoms in aplane,where six of themare arranged symmetricallyaroundacentreatom. Asamathematical model we take theHamiltonian（4.1） with $N = 7$ ， $m _ { i } = m = 6 6 . 3 4 \cdot 1 0 ^ { - 2 7 }$ [kg],

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/293b615784e06d861fa13e39cf5fe4a9d56bedb44ee9a35f2baec9b1c3cdab86.jpg)

$$
\varepsilon _ { i j } = \varepsilon = 1 1 9 . 8 k _ { B } [ { \bf J } ] , \qquad \sigma _ { i j } = \sigma = 0 . 3 4 1 [ { \mathrm { n m } } ] ,
$$

where $k _ { B } = 1 . 3 8 0 6 5 8 \cdot 1 0 ^ { - 2 3 } \ : [ \mathrm { J / K } ]$ isBoltzmann'sconstant (see Allen& Tildesley (1987),page 21).Asunits for our calculations we take masses in $\left[ \mathrm { k g } \right]$ ,distances in nanometers $\left( 1 [ \mathrm { n m } ] \right) = 1 0 ^ { - 9 } [ \mathrm { m } ] ,$ ,and times in nanoseconds(1 [nsec] $= 1 0 ^ { - 9 }$ [sec]). Initialpositions (in [nm])and initial velocities (in[nm/nsec]) are given in Table4.1. They are chosen such that neighbouring atoms have a distance that is close to the onewith lowest potential energy,and such that the total momentum is zero and therefore the centre of gravitydoes not move.Theenergy at the initial position is $H ( p _ { 0 } , q _ { 0 } ) \approx - 1 2 6 0 . 2 k _ { B }$ [J].

Forcomputations in molecular dynamics one is usually not interested in the trajectories of the atoms,but one aimsat macroscopic quantities such as temperature, pressure,internal energy,etc.Here we consider the total energy,givenby the Hamiltonian,and the temperaturewhich can be calculated from the formula(see Allen&

Table 4.1.Initial values for the simulation ofa frozen argon crystal   

<table><tr><td rowspan=1 colspan=1>atom</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>position</td><td rowspan=1 colspan=1>0.000.00</td><td rowspan=1 colspan=1>0.020.39</td><td rowspan=1 colspan=1>0.340.17</td><td rowspan=1 colspan=1>0.36-0.21</td><td rowspan=1 colspan=1>-0.02-0.40</td><td rowspan=1 colspan=1>-0.35-0.16</td><td rowspan=1 colspan=1>-0.310.21</td></tr><tr><td rowspan=1 colspan=1>velocity</td><td rowspan=1 colspan=1>-30-20</td><td rowspan=1 colspan=1>50-90</td><td rowspan=1 colspan=1>-70-60</td><td rowspan=1 colspan=1>9040</td><td rowspan=1 colspan=1>8090</td><td rowspan=1 colspan=1>-40100</td><td rowspan=1 colspan=1>-80-60</td></tr></table>

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/fc9cddb7eada1e699af05f44f63559c5c70f50a0af375d859f2140c5ffed92d1.jpg)  
Fig.4.1.Computed total energyand temperature of the argon crystal

Tildesley (1987),page 46)

$$
T = \frac { 1 } { 2 N k _ { B } } \sum _ { i = 1 } ^ { N } m _ { i } \| \dot { q } _ { i } \| ^ { 2 } .
$$

Weapplytheexplicit and symplectic Euler methodsand alsothe Verlet method tothisproblem.Observe that foraHamiltonian such as（4.1）allthreemethods areexplicit,and all of them need only one force evaluation per integration step.In Fig.4.1 we present the numerical results of our experiments.The integrations are done over an interval of length O.2[nsec].The stepsizes are indicated in femtoseconds $( 1 \ : [ \mathrm { f s e c } ] = 1 0 ^ { - 6 }$ [nsec]).

The two upper pictures show the values $\left( H ( p _ { n } , q _ { n } ) - H ( p _ { 0 } , q _ { 0 } ) \right) / k _ { B }$ asa function oftime $t _ { n } = n h .$ Forthe exact solution,this value isprecisely zero forall times. Similarto earlierexperimentswe see that the symplectic Eulermethodis qualitativelycorrect,whereas the numerical solution of the explicit Euler method,although computed witha much smaller step size,is completely useless (see the citation at thebeginning of this section).TheVerlet method is qualitatively correctand gives much more accurate results than the symplectic Euler method (we shall see later thattheVerletmethod isof order2).The two computationswith theVerletmethod showthat the energy errordecreasesbya factor of4if the step sizeisreduced by a factor of 2 (second order convergence).

Thetwo lower pictures ofFig.4.1 show the numerical values of the temperature difference $T - T _ { 0 }$ with $T$ given by（4.3）and $T _ { 0 } \approx 2 2 . 7 2 [ ]$ K](initialtemperature). Incontrast to thetotal energy,thisisnot anexact invariant,but for ourproblemit fuctuates around aconstant value.The explicit Euler method gives wrongresults, butthe symplectic Eulerand the Verlet methods show thedesired behaviour.This timeareduction of the step size does not reduce the amplitude of the oscillations, which indicates that the fluctuation of the exact temperature is of the same size.

# I.5Highly Oscillatory Problems

Inthis section we discuss a system with almost-harmonic high-frequency oscillations.We show numerical phenomena of methods applied with step sizes that are not small compared to the period of the fastest oscillations.

# I.5.1A Fermi-Pasta-Ulam Problem

...dealing with the behavior of certain nonlinearphysical systems where thenon-linearityis introducedasaperturbation toaprimarily linearproblem.The behaviorof thesystems istobestudied fortimes whicharelong compared to the characteristic periods of the corresponding linear problems. (E.Fermi,J.Pasta,S.Ulam1955)

Inthe early1950sMANIAC-I had justbeencompleted and satpoised foran attack on significant problems....Fermi suggested that itwould behighly instructive to integrate the equations ofmotion numerically for ajudiciously chosen,one-dimensional, harmonic chain of mass points weaklyperturbed by nonlinear forces. (J.Ford 1992)

Theproblem ofFermi,Pasta&Ulam（1955）isa simplemodel for simulations in statistical mechanicswhich revealed highly unexpected dynamical behaviour.We considera modification consisting of a chain of $_ { 2 m }$ mass points,connected with alternating soft nonlinearand stiff linear springs,and fixed at theend points (see Galgani,Giorgill,Martinoli&Vanzini(1992)andFig.5.1).Thevariables $q _ { 1 } , \ldots , q _ { 2 m }$ $q _ { 0 } = q _ { 2 m + 1 } = 0$ ）stand for the displacements of the mass points,and $p _ { i } = { \dot { q } } _ { i }$ for their velocities.The motion is described byaHamiltoniansystem with total energy

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/cdaa40818d54c7a4c906b91cf955f57946df0be896d56d8dfed3128fa9de0395.jpg)  
Fig.5.1.Chain with alternating soft nonlinear and stiff linear springs

$$
H ( p , q ) = \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } ( p _ { 2 i - 1 } ^ { 2 } + p _ { 2 i } ^ { 2 } ) + \frac { \omega ^ { 2 } } { 4 } \sum _ { i = 1 } ^ { m } ( q _ { 2 i } - q _ { 2 i - 1 } ) ^ { 2 } + \sum _ { i = 0 } ^ { m } ( q _ { 2 i + 1 } - q _ { 2 i } ) ^ { 4 } ,
$$

where $\omega$ isassumed to be large.It is quite natural to introduce the new variables

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/ad55b58c16440a5884248bdd653567d251004a95154fbf1b11ff2f16f1068e21.jpg)  
Fig.5.2.Exchange of energyin the exact solution of the Fermi-Pasta-Ulam model.The picture to theright is an enlargement of the narrow rectangle in the left-hand picture

$$
\begin{array} { r l r } { x _ { 0 , i } \ = \ \big ( q _ { 2 i } + q _ { 2 i - 1 } \big ) / \sqrt { 2 } , } & { } & { x _ { 1 , i } \ = \ \big ( q _ { 2 i } - q _ { 2 i - 1 } \big ) / \sqrt { 2 } , } \\ { y _ { 0 , i } \ = \ \big ( p _ { 2 i } + p _ { 2 i - 1 } \big ) / \sqrt { 2 } , } & { } & { y _ { 1 , i } \ = \ \big ( p _ { 2 i } - p _ { 2 i - 1 } \big ) / \sqrt { 2 } , } \end{array}
$$

where $x _ { 0 , i }$ $i = 1 , \ldots , m )$ representsa scaled displacement of the $i$ th stiff spring, $x _ { 1 , i }$ a scaled expansion (or compression） of the $i$ thstiffspring,and $y _ { 0 , i } , y _ { 1 , i }$ their velocities(or momenta).With this change of coordinates,the motion in the new variablesisagaindescribed bya Hamiltonian system,with

$$
\begin{array} { r c l } { \displaystyle H ( y , x ) ~ = ~ \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } \left( y _ { 0 , i } ^ { 2 } + y _ { 1 , i } ^ { 2 } \right) + \frac { \omega ^ { 2 } } { 2 } \sum _ { i = 1 } ^ { m } x _ { 1 , i } ^ { 2 } + \frac { 1 } { 4 } \Big ( ( x _ { 0 , 1 } - x _ { 1 , 1 } ) ^ { 4 } + } \\ { \displaystyle \quad + \sum _ { i = 1 } ^ { m - 1 } \left( x _ { 0 , i + 1 } - x _ { 1 , i + 1 } - x _ { 0 , i } - x _ { 1 , i } \right) ^ { 4 } + ( x _ { 0 , m } + x _ { 1 , m } ) ^ { 4 } \Big ) . } \end{array}
$$

Besidesthefactthat theequations ofmotionareHamiltonian,sothatthe totalenergy isexactly conserved,they havea further interesting feature.Let

$$
I _ { j } ( x _ { 1 , j } , y _ { 1 , j } ) = \frac { 1 } { 2 } \big ( y _ { 1 , j } ^ { 2 } + \omega ^ { 2 } x _ { 1 , j } ^ { 2 } \big )
$$

denote the energy of the $\mathcal { I }$ th stiff spring.It turnsout that there isan exchange of energy between the stiff springs,but the total oscillatory energy $\textit { I } = \textit { I } _ { 1 } + \ldots +$ $I _ { m }$ remains close to a constant value,in fact, $I { \big ( } ( x ( t ) , y ( t ) ) = I { \big ( } ( x ( 0 ) , y ( 0 ) { \big ) } +$ $\mathcal { O } ( \omega ^ { - 1 } )$ .Foranillustration of this property,we choose $m = 3$ (asin Fig.5.1）, $\omega = 5 0$ ,

$$
x _ { 0 , 1 } ( 0 ) = 1 , \quad y _ { 0 , 1 } ( 0 ) = 1 , \quad x _ { 1 , 1 } ( 0 ) = \omega ^ { - 1 } , \quad y _ { 1 , 1 } ( 0 ) = 1 ,
$$

and zero for the remaining initial values.Fig.5.2 displays the energies $I _ { 1 } , I _ { 2 } , I _ { 3 }$ ofthestiff springs together with the total oscillatory energy $I = I _ { 1 } + I _ { 2 } + I _ { 3 }$ asa function of time.The solution has beencomputed verycarefully with high accuracy, so that thedisplayed oscillationscan be considered as exact.

# I.5.2 Application of Classical Integrators

Which of themethods of theforegoing sections produce qualitatively correctapproximations when the product of the step size $h$ with the high frequency $\boldsymbol { \omega }$ isrelativelylarge？

Linear Stability Analysis.To get an idea of the maximum admissible step size, weneglect the quartic term in the Hamiltonian (5.2),so that thedifferential equation splitsintothe two-dimensional problems $\dot { y } _ { 0 , i } = 0$ , ${ \dot { x } } _ { 0 , i } = y _ { 0 , i }$ and

$$
\dot { y } _ { 1 , i } = - \omega ^ { 2 } x _ { 1 , i } , \quad \dot { x } _ { 1 , i } = y _ { 1 , i } .
$$

Omitting the subscripts,the solution of(5.4) is

$$
{ \binom { y ( t ) } { \omega x ( t ) } } = { \binom { \cos \omega t } { \sin \omega t } } \quad { \cos \omega t } \quad ) { \binom { y ( 0 ) } { \omega x ( 0 ) } } .
$$

Thenumerical solution ofaone-stepmethod applied to(5.4)yields

$$
\left( \begin{array} { c } { { y _ { n + 1 } } } \\ { { \omega x _ { n + 1 } } } \end{array} \right) = M ( h \omega ) \left( \begin{array} { c } { { y _ { n } } } \\ { { \omega x _ { n } } } \end{array} \right) ,
$$

and the eigenvalues $\lambda _ { i }$ of $M ( h \omega )$ determine the long-time behaviour of the numerical solution.Stability(i.e.,boundednessof the solution of(5.5))requires the eigenvalues to be less than or equal to one in modulus.For the explicit Euler method wehave $\lambda _ { 1 , 2 } = 1 \pm i h \omega$ ,so that the energy ${ \cal I } _ { n } = ( y _ { n } ^ { 2 } + \omega ^ { 2 } x _ { n } ^ { 2 } ) / 2$ increasesas $( 1 + h ^ { 2 } \omega ^ { 2 } ) ^ { n / 2 } .$ Forthe implicit Euler method we have $\lambda _ { 1 , 2 } = ( 1 \pm i h \omega ) ^ { - 1 }$ ,and theenergy decreasesas $( 1 + h ^ { 2 } \omega ^ { 2 } ) ^ { - n / 2 } $ Forthe implicit midpointrule,the matrix $M ( h \omega )$ isorthogonal and therefore $I _ { n }$ isexactlypreserved forall $h$ and forall times.Finally,for thesymplecticEulermethodand for the Stormer-Verletscheme we have

$$
\begin{array} { r } { H ( h \omega ) = \left( \begin{array} { c c } { 1 } & { - h \omega } \\ { h \omega } & { 1 - h ^ { 2 } \omega ^ { 2 } } \end{array} \right) , \quad M ( h \omega ) = \left( \begin{array} { c c } { 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 2 } & { - \frac { h \omega } 2 \left( 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 4 \right) } \\ { \frac { h \omega } 2 } & { 1 - \frac { h ^ { 2 } \omega ^ { 2 } } 2 } \end{array} \right) } \end{array}
$$

respectively.For both matrices,the characteristicpolynomial is $\lambda ^ { 2 } - ( 2 - h ^ { 2 } \omega ^ { 2 } ) \lambda + 1 ,$ so that the eigenvalues are ofmodulus one ifand onlyif $| h \omega | \leq 2$ .

Numerical Experiments.We apply several methods to the Fermi-Pasta-Ulam （FPU）problem,with $\omega = 5 0$ and initial dataasgivenin Sect.I.5.1.Theexplicit andimplicit Euler methods givecompletelywrong solutions even for very small stepsizes.Fig.5.3presents the numerical results for $H$ ， $I$ , $I _ { 1 }$ ， $I _ { 2 }$ , $I _ { 3 }$ obtained with theimplicit midpoint rule,thesymplectic Euler,and the Stormer-Verlet scheme. For the small step size $h = 0 . 0 0 1$ all methods give satisfactory results,although the energy exchangeis notreproduced accurately overlong times.The Hamiltonian $H$ andthe total oscillatory energy $I$ arewell conserved over much longer time intervals.The larger step size $h = 0 . 0 3$ has been chosen such that $h \omega = 1 . 5$ isclose to the stability limit of the symplectic Eulerand the Stormer-Verlet methods.The values of $H$ and $I$ are still bounded over very long time intervals,but the oscillations do not represent the true behaviour.Moreover, the averagevalue of $I$ isno longer close to1,as it is for the exact solution.These phenomena call foran explanation, and for numerical methods with an improved behaviour (see Chap.XIII).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/b8c4ae458658078cea557c4bf93279799995ce8e62d2c9a2b5d6fee17dc20184.jpg)  
Fig.5.3.Numerical solution for theFPU problem(5.2）with dataasin Sect.I.5.1,obtained withthe implicit midpointrule(left),symplectic Euler(middle),and Stormer-Verlet scheme (right);the upper pictures use $h = 0 . 0 0 1$ ,the lower pictures $h = 0 . 0 3$ thefirst four pictures show the Hamiltonian $H - 0 . 8$ and theoscillatory energies $I _ { 1 } , I _ { 2 } , I _ { 3 } , I ;$ the last two pictures only show $I _ { 2 }$ andI

# I.6 Exercises

1.Show that theLotka-Volterra problem(1.1)inlogarithmicscale,i.e.,byputting $p = \log u$ and $q = \log v$ ,becomesa Hamiltonian system with the function(1.4) asHamiltonian (see Fig.6.1).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/2fb25c0ca6aa77ecf7b6a8a3c936904f22c2dae41f089ac032ede0b6af3da850.jpg)  
Fig.6.1.Areapreservationin logarithmic scale of theLotka-Volterraflow

2.Apply the symplectic Euler method(or the implicit midpoint rule) to problems such as

$$
{ \binom { \dot { u } } { \dot { v } } } = { \binom { ( v - 2 ) / v } { ( 1 - u ) / u } } \psi \qquad { \binom { \dot { u } } { \dot { v } } } = { \binom { u ^ { 2 } v ( v - 2 ) } { v ^ { 2 } u ( 1 - u ) } }
$$

with various initial conditions.Both problems have the same first integral (1.4) astheLotka-Volterra problem and therefore their solutionsare also periodic. Dothe numerical solutions also show this behaviour?

3.Ageneral two-body problem (sun and planet) is givenby the Hamiltonian

$$
H ( p , p _ { S } , q , q _ { S } ) = \frac { 1 } { 2 M } p _ { S } ^ { T } p _ { S } + \frac { 1 } { 2 m } p ^ { T } p - \frac { G m M } { \| q - q _ { S } \| } ,
$$

where $q _ { S } , q \in \mathbb { R } ^ { 3 }$ are the positions of the sun (mass $M$ and the planet (mass $_ { f } / \iota$ ), $p _ { S } , p \in \mathbb { R } ^ { 3 }$ are their momenta,and $G$ is the gravitational constant.

a)Prove:in heliocentric coordinates $Q : = q - q s$ ,the equations of motion are

$$
\ddot { Q } = - G ( M + m ) { \frac { Q } { \lVert Q \rVert ^ { 3 } } } .
$$

b)Prove that ${ \begin{array} { r } { { \frac { d } { d t } } { \big ( } Q ( t ) \times Q ( t ) { \big ) } = 0 } \end{array} }$ ,sothat $Q ( t )$ stays for all times $t$ in the plane $E = \{ q ; d ^ { T } q = 0 \}$ where $d = Q ( 0 ) \times \dot { Q } ( 0 )$ .

Conclusion.The coordinates corresponding toa basis in $E$ satisfy the twodimensional equations (2.2).

4.In polar coordinates,the two-body problem (2.2) becomes

$$
\ddot { r } = - V ^ { \prime } ( r ) \qquad \mathrm { w i t h } \qquad V ( r ) = { \frac { L _ { 0 } ^ { 2 } } { 2 r ^ { 2 } } } - { \frac { 1 } { r } }
$$

which is independent of $\varphi$ Theangle $\varphi ( t )$ can beobtained by simple integration from $\dot { \varphi } ( t ) = L _ { 0 } / r ^ { 2 } ( t )$ .

5.Compute the period of the solution of the Kepler problem (2.2) and deduce fromtheresult Kepler's“third law”.

Hint.ComparingKepler's second law(2.6)with the area of the elipse gives ${ \scriptstyle \frac { 1 } { 2 } } L _ { 0 } T = a b \pi .$ Thenapply(2.7).The result is $T = 2 \pi ( 2 \vert { \cal H } _ { 0 } \vert ) ^ { - 3 / 2 } = 2 \pi a ^ { 3 / 2 }$

6.Deduce Kepler's first Ilaw from (2.2) by the elegant method ofLaplace(1799). Hint.Multiplying(2.2)with(2.5）gives

$$
L _ { 0 } \ddot { q } _ { 1 } = \frac { d } { d t } \Bigl ( \frac { q _ { 2 } } { r } \Bigr ) , \qquad L _ { 0 } \ddot { q } _ { 2 } = \frac { d } { d t } \Bigl ( - \frac { q _ { 1 } } { r } \Bigr ) ,
$$

and after integration $\begin{array} { r } { L _ { 0 } \dot { q } _ { 1 } = \frac { q _ { 2 } } { r } + B } \end{array}$ ， $\begin{array} { r } { L _ { 0 } \dot { q } _ { 2 } = - \frac { q _ { 1 } } { r } + A } \end{array}$ ,where $A$ and $B$ are integration constants.Then eliminate $\dot { q } _ { 1 }$ and $\dot { q } _ { 2 }$ bymultiplying these equations by $q _ { 2 }$ and $- q _ { 1 }$ respectivelyand by subtracting them.Theresult isaquadratic equation in $q _ { 1 }$ and $q _ { 2 }$

7.Whatever the initial values for the Kepler problem are, $1 + 2 H _ { 0 } L _ { 0 } ^ { 2 } \ge 0$ holds. Hence,the value $e$ iswell defined by(2.9).

Hint. $L _ { 0 }$ is thearea of theparallelogram spanned by the vectors $q ( 0 )$ and ${ \dot { q } } ( 0 )$

8.Implementation of the Stormer-Verlet scheme.Explain why the use of the onestepformulation(1.17）isnumericallymore stablethan that of the two-term recursion (1.15).

9.Runge-Lenz-Pauli vector. Prove that the function

$$
A ( p , q ) = \left( \begin{array} { c } { { p _ { 1 } } } \\ { { p _ { 2 } } } \\ { { 0 } } \end{array} \right) \times \left( \begin{array} { c c } { { 0 } } \\ { { 0 } } \\ { { q _ { 1 } p _ { 2 } - q _ { 2 } p _ { 1 } } } \end{array} \right) = \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } \left( \begin{array} { c } { { q _ { 1 } } } \\ { { q _ { 2 } } } \\ { { 0 } } \end{array} \right)
$$

isafirst integral of the Kepler problem,i.e., $A \big ( p ( t ) , q ( t ) \big ) \ = \ C o n s t$ along solutionsof theproblem.However,itisnota first integral of theperturbed Kepler problem of Exercise12.

10.Add acolumn to Table 2.1 which shows the long-time behaviour of theerror in the Runge-Lenz-Pauli vector (see Exercise 9) for the various numerical integrators.

11.For the Kepler problem,eliminate $( p _ { 1 } , p _ { 2 } )$ from the relations ${ \cal H } ( p , q ) = C o n s t$ , $L ( p , q ) ~ = ~ C o n s t$ and $A ( p , q ) ~ = ~ C o n s t$ Thisgivesa quadratic relation for $( q _ { 1 } , q _ { 2 } )$ and proves that the solution lies onan ellipse,a parabola,or on a hyperbola.

12.Study numerically the solution of the perturbed Kepler problem with Hamiltonian

$$
H ( p _ { 1 } , p _ { 2 } , q _ { 1 } , q _ { 2 } ) = \frac { 1 } { 2 } \left( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } \right) - \frac { 1 } { \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } } } - \frac { \mu } { 3 \sqrt { ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) ^ { 3 } } } ,
$$

where $\mu$ isa positive or negative small number.Among others,this problem describes themotion ofa planet in the Schwarzschild potential for Einstein's general relativity theory7.You will observe a precession of the perihelion,which,applied to the orbit ofMercury,represented the historically first verification of Einstein’s theory (seee.g.,Birkhoff 1923,p.261-264).

![](../chunks/N-body-Geometric Numerical Integration. Structure-Preserving Algorithms for Ordinary Diffe_part_0001_pages_0001-0070/auto/images/367faa04ca35585f142ded582c7fa3e42e6e29afe19b1697149082a985d64e6b.jpg)

The precession can also be expressed analytically:the equation for $u = 1 / r$ as a function of $\varphi$ ,correspondingto(2.8),here becomes

$$
u ^ { \prime \prime } + u = \frac { 1 } { d } + \mu u ^ { 2 } ,
$$

where $d = L _ { 0 } ^ { 2 } .$ Now compute the derivative of this solution with respect to $\mu$ ， at $\mu = 0$ and $\boldsymbol { u } = ( 1 + e \cos ( \varphi - \varphi ^ { * } ) ) / d$ after one period $t = 2 \pi$ This leadsto $\eta = \mu ( e / d ^ { 2 } ) \cdot 2 \pi \sin \varphi$ (see the small picture).Then,for small $\mu$ ,theprecession afterone period is

$$
\Delta \varphi = \frac { 2 \pi \mu } { d } .
$$
