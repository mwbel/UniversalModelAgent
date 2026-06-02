CHAPTER 10

AFFINE GEOMETRY: GEODESICS，PARALLEL TRANSPORT, AND COVARIANT DERIVATIVE

Galilei's Principle of Inertia is sufficient in itself to prove conclusively that the world is affine in character.

This chapter is entirely Track 2 Chapter 9 is necessary   
preparation for it. It will be needed as   
preparation for (1) Chapters 11-13 (differential geometry: Newtonian gravity), (2) the second half of Chapter 14 (calculation of curvature), and (3) the details, but not the message, of Chapter 15 (Bianchi identities).

Freely falling particies and their clocks

Free fall is the“natural state of motion,” so natural, in fact, that the path through spacetime of a freely falling, neutral test body is independent of its structure and composition (the “weak equivalence principle” of Einstein, Eotvos, Dicke; see Box 1.2 and $\ S 3 8 . 3 \AA$ .

Picture spacetime as filled with free-fali trajectories. Pick an event. Pick a velocity there. They determine a unique trajectory.

Be more precise. Ask for the maximum amount of information tied up in each trajectory. Is it merely the sequence of points along which the test body falls? No; there is more. Each test body can carry a clock with itself (same kind of clock-"good” clock in sense of Figure 1.9—regardless of structure or composition of test body). The clock ticks as the body moves,labeling each event on its trajectory with a number: the time $\lambda$ the body was there. Result: the free-fall trajectory is not just a sequence of points; it is a parametrized sequence, a “curve" $\mathcal { P } ( \lambda )$

But is the parametrization unique? Not entirely. Quite arbitrary are (l) the choice of time origin, ${ \mathcal { P } } ( 0 )$ ；and (2) the units (centimeters,seconds,furlongs,...) in which clock time $\lambda$ is measured. Hence, $\lambda$ is unique only up to linear transformations

$$
\lambda _ { \mathrm { n e w } } = a \lambda _ { \mathrm { o l d } } + b ;
$$

![](images/5c6f3ebbe4072fbfa1e87cdd73e2bd4259d8a444c821e3e2852f5949161aaaaa.jpg)  
Figure 10.1. A geodesic viewed as a rule for“straight-on parallel transport.”Pick an event $\mathcal { P } _ { 0 } ^ { \mathrm { ~ ~ } }$ and a tangent vector $\pmb { \nu } = \pmb { d } / d \lambda$ there. Construct the unique geodesic $\mathcal { P } ( \lambda )$ that（l） passes through $\scriptstyle { \mathcal { P } } _ { 0 }$ ${ \bf \dot { \varphi } _ { 0 } } \colon \mathcal { P } ( 0 ) = \mathcal { P } _ { 0 }$ and (2) has $\pmb { u }$ as its tangent vector there: $( d \mathcal { P } / d \lambda ) _ { \lambda = 0 } = \pmb { u } .$ This geodesic can be viewed as a rule for picking up $\pmb { u }$ from ${ \mathcal { P } } ( 0 )$ and laying it down again at its tip, ${ \mathcal { P } } ( 1 ) .$ ,in as straight a manner as possibie,

$$
{ \pmb u } _ { \lambda = 1 } = ( d ^ { \varrho } / d \lambda ) _ { \lambda = 1 } ;
$$

and for then picking it up and laying it down as straight as possible again at $\mathcal { P } ( 2 )$ ，

$$
{ \pmb u } _ { \lambda = 2 } = ( d \mathcal { P } / d \lambda ) _ { \lambda = 2 } ;
$$

etc. This sequence of“straight as possible,”“taii-on-tip” transports gives meaning to the idea that $( d \mathcal { P } / d \lambda ) _ { \lambda = 1 7 }$ and $\pmb { \upsilon } = ( d \hat { \mathcal { P } } / d \lambda ) _ { \lambda = 0 }$ are “the same vector”at different points along the geodesic; or, equivalently. that one has been obtained from the other by“straight-on parallel transport.”

$^ b$ ("new origin of clock time") is a number independent of location on this specific free-fall trajectory,and $^ { a }$ ("ratio of new units to old") is also.

In the curved spacetime of Einstein (and in that of Cartan-Newton, Chapter 12), these parametrized free-fall trajectories are the straightest of all possible curves. Consequently, one gives these trajectories the same name,“geodesics,”that mathematicians use for the straight lines of a.curved manifold; and like the mathematicians, one uses the name “affine parameter" for the parameter $\lambda$ along a free-fall geodesic. Equation (lO.1) then says “the affine parameter of a geodesic is unique up to linear transformations."

Geodesic defined as a free-fall trajectory

The affine parameter ("clock time") along a geodesic has nothing to do,a priori, with any metric.It exists even in the absence of metric (e.g.,in Cartan-Newtonian spacetime). It gives one a method for comparing the separation between events on a geodesic ( $\mathcal { B }$ and $\boldsymbol { \mathcal { Q } }$ are“twice as far apart" as $\mathcal { R }$ and $\mathcal { L }$ if $[ \lambda _ { \mathfrak { s } } - \lambda _ { \mathfrak { c } } ] = 2 [ \lambda _ { \mathfrak { s } } - \lambda _ { \mathfrak { c } } ] )$ But the affine parameter measures relative separations only along its own geodesic. It has no means of reaching off the geodesic.

The above features of geodesics,and others,are summarized in Figure l0.l and Box 10.1.

# $\$ 10.2$ .PARALLEL TRANSPORT AND COVARIANT DERIVATIVE: PICTORIAL APPROACH

Affine parameter defined as clock time along free-fall trajectory

Two test bodies,initially falling through spacetime on parallel,neighboring geodesics, get pushed toward each other or apart by tidal gravitational forces (spacetime curvature). To quantify this statement, one must quantify the concepts of “parallel" and “rate of acceleration away from each other.” Begin with paralelism.

# Box 10.1 GEODESICS

Geodesic in brief

Give point, give tangent vector; get unique, affine-parametrized curve ("geodesic").

Geodesic: in context of gravitation physics

World line of a neutral test particle ("Einstein's geometric theory of gravity"; also “Cartan's translation into geometric terms of Newton's theory of gravity"):

(1）“given point": some event on this world line;   
(2)“given vector": vector("displacement per unit increase of parameter") tangent to world line at instant defined by that event;   
(3)“unique curve": every neutral test particle with a specified initial position and a specified initial velocity follows the same world line, regardless of its composition and regardless of its mass (small; test mass!;“weak equivalence principle of Einstein-Eotvos-Dicke");   
(4)“affine parameter": in Cartan-Newton theory, Newton's “universal time”(which is measured by“good’clocks)；in the real physical world,"proper time"(as measured by a “good”clock) along a timelike geodesic;   
(5)“parametrized curve": (a) affine parameter unique up to a transformation of the form $\lambda \longrightarrow a \lambda + \bar { b }$ ,where $^ { a }$ and $^ { b }$ are constants (no arbitrariness along a given geodesic other than zero of parameter and unit of parameter); or equivalently (b) given any three events ${ \mathcal { Q } } , { \mathcal { B } }$ ， $\mathcal { C }$ on the geodesic,one can find by well-determined physical construction ("clocking") a unique fourth event $\boldsymbol { \phi }$ on the geodesic such that $( \lambda _ { \mathcal { G } } - \lambda _ { \mathcal { C } } )$ is equal to $( \lambda _ { \checkmark } - \lambda _ { \checkmark } )$ ; or equivalently (c) [differential version] given a tangent vector with components $( d x ^ { \alpha } / d \lambda ) _ { \alpha }$ at point $\boldsymbol { \mathcal { Q } }$ ，one can find by physical construction (again “clocking") “the same tangent vector” at point $\mathcal { C }$ with uniquely determined components $( d x ^ { \alpha } / d \lambda ) _ { \mathcal { C } }$ (vector “equal"；components ordinarily not equal because of twisting and turning of arbitrary base vectors between $\boldsymbol { \mathcal { Q } }$ and $\mathcal { E }$ ).

Comparison of vectors at different events by parallel transport

Consider two neighboring events $\boldsymbol { \mathcal { Q } }$ and $\mathcal { B }$ connected by a curve $\mathcal { P } ( \lambda )$ .A vector $\pmb { v } _ { q }$ lies in the tangent space at $\boldsymbol { \mathcal { q } }$ ,and a vector $\pmb { v } _ { \ast }$ lies in the tangent space at $\mathcal { B }$ How can one say whether $\pmb { v } _ { \alpha }$ and $\pmb { v } _ { \ast \ast }$ are parallel, and how can one compare their lengths? The equivalence principle gives an answer: an observer travels (using rocket power as necessary） through spacetime along the world line $\mathcal { P } ( \lambda )$ . He carries the vector $\pmb { v } _ { q }$ with himself as he moves,and he uses flat-space Newtonian or Minkowskian standards to keep it always unchanging (flat-space physics is valid locally according to the equivalence principle!). On reaching event $\boldsymbol { \mathcal { B } }$ the observer compares his “parallel-transported vector” $v _ { q }$ with the vector ${ \pmb v } _ { ; \hbar }$ . If they are identical, then the original vector $\pmb { v } _ { \pmb { \tilde { q } } }$ was (by definition) parallel to $\pmb { v } _ { \mathfrak { N } }$ , and they had the same length. (No metric means no way to quantify length; nevertheless, parallel transport gives a way to compare length!)

The equivalence principle entered this discussion in a perhaps unfamiliar way, applied to an observer who may be accelerated,rather than to one who is freely falling. But one cannot evade a basic principle by merely confronting it with an intricate application. (Ingenious perpetual-motion machines are as impossible as simpleminded ones!) The equivalence principle states that no local measurement that is insensitive to gravitational tidal forces can detect any difference whatsoever between flat and curved spacetime. The spaceship navigator has an inertial guidance system (accelerometers,gyroscopes,computers） capable of preserving an inertial reference frame in flat spacetime; and in flat spacetime it can compute the attitude and velocity of any object in the spaceship relative to a given inertial frame. The purchaser may specify whether he wants a guidance computer programmed with the laws of zero-gravity Newtonian mechanics,or with those of special-relativity physics. Use this same guidance system-including the same computer program-in curved spacetime.A vector is being parallel transported if the guidance system's computer says it is not changing.

Parallel transport defined using inertial guidance systems and equivalence principle

Will the result of transport in this way be independent of the curve used to link $\boldsymbol { \mathcal { I } }$ and $\mathcal { B } \smash { ? }$ Clearly yes,in gravity-free spacetime, since this is a principal performance criterion that the purchaser of an inertial guidance system can demand of the manufacturer. But in a curved spacetime,the answer is “NO!” If $\pmb { v } _ { \alpha }$ agrees with $\pmb { v } _ { ; \ast }$ after paralel transport along one curve, it need not agree with $\pmb { v } _ { \ast \beta }$ after parallel transport along another. Spacetime curvature produces discrepancies. But one is not ready to study and quantify those discrepancies (Chapter 1l),until one has developed the mathematical formalism of parallel transport, which, in turn, cannot be done until one has made precise the “flat-space standards for keping the vector $\pmb { v } _ { \alpha }$ always unchanging” as it is transported along a curve.

Result of parallel transport depends on route.

The flat-space standards are made precise in Box 1O.2.They lead to (l)a“Schild's ladder” construction for performing parallel transport; (2） the concept “covariant derivative,” $\yen 1$ ,of a vector field $\pmb { \nu }$ along a curve with tangent u; (3) the “equation of motion” $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ for a geodesic, which states that “a geodesic parallel transports its own tangent vector along itself;” and (4) a link between the tangent spaces at adjacent events (Figure 10.2).

# Schild's ladder for performing parallel transport: its consequences

# $\$ 10.3$ .PARALLEL TRANSPORT AND COVARIANT DERIVATIVE: ABSTRACT APPROACH

From the“Schild's ladder” construction of Box l0.2,one learns the following properties of spacetime's covariant derivative:

(continued on page 252)

# BoX 10.2 FROM GEODESICS TO PARALLEL TRANSPORT TO COVARIANT DIFFERENTIATION TO GEODESICS TO...

"Parallel transport" as defined by geodesics

A.Transport any sufficiently short stretch of a curve $\mathcal { Q } \mathfrak { X }$ (i.e., any tangent vector) parallel to itself along curve $\mathcal { Q } \mathfrak { s } \mathfrak { \beta }$ to point $\beta$ as follows:

![](images/0296b48132aef8b15343b8775053c04b814bde246d3f7013bd969384c4e123f1.jpg)

1. Take some point $\mathfrak { R }$ along $\boldsymbol { \mathcal { Q } } \boldsymbol { \mathcal { B } }$ close to $\boldsymbol { \mathcal { q } }$ Take geodesic $\mathfrak { X P }$ through $\mathfrak { X }$ and $\mathcal { D } \pi$ .Take any affine parametrization $\lambda$ of $\mathcal { X P }$ and define a unique point $\mathfrak { X }$ by the condition $\lambda _ { \cdot \cdot \pi } = { \textstyle \frac { 1 } { 2 } } ( \lambda _ { \cdot } x + \lambda _ { \cdot \cdot \pi } )$ ("equal stretches of time in x and $\Re \mathfrak { P } \bar { \pi } ^ { \mathfrak { n } }$

![](images/1ae2a3c3928742a9a852fd2715c3091036e520f850c09ce8fb3056ac10a21358.jpg)

2. Take geodesic that starts at $\boldsymbol { \mathcal { Q } }$ and passes through $\mathcal { D }$ ,and extend it by an equal parameter increment to point $\mathcal { P }$

![](images/e08d4697d378e1a4000ee741ec274a669d82543aa06762da84e0ce237b86cf8d.jpg)

![](images/dd822f08eb20e258f7888b6547bde24ee895f6b1d14653bd6e856d386c528f75.jpg)

3. Curve ${ \mathcal { D } } \mathscr { R } { \mathcal { P } }$ gives vector $\mathcal { Q X }$ as propagated parallel to itself from $\boldsymbol { \mathcal { Q } }$ to $\mathfrak { R }$ (for sufficiently short $\mathcal { Q } \mathfrak { X }$ and $\mathcal { Q } \mathfrak { R } \mathrm { ~ }$ ). This construction certainly yields parallel transport in flat spacetime (Newtonian or Einsteinian). Moreover,it is local (vectors $\mathcal { Q } \mathcal { X } , \mathcal { Q } \mathcal { R }$ etc., very short). Therefore,it must work even in curved spacetime. (It embodies the equivalence principle.)

4. Repeat process over and over,and eventually end up with $\mathcal { Q X }$ propagated parallel to itself from $\boldsymbol { \mathcal { Q } }$ to $\mathcal { B }$ . Call this construction “Schild's Ladder,” from Schild's (1970) similar construction. [See also Ehlers, Pirani, and Schild (1972).] Note that curve $\mathcal { Q B }$ need not be a geodesic. There is no requirement that $\mathcal { D } \mathcal { Q }$ be the straight-on continuation of $\mathcal { Q P }$ similar to the geodesic requirement in the“cross-brace” that $\mathcal { R P }$ be the straight-on continuation of $\mathcal { Q } \mathcal { U }$

![](images/c6bdf1091cfb53edb189962a58caf49725b3831c2b202b6e3f842fdc52defe59.jpg)  
"Schild's Ladder"

5. Result of propagating $\mathcal { Q X }$ parallel to itself from $\boldsymbol { \mathcal { q } }$ to $\mathcal { B }$ depends on choice of world line $\mathcal { Q B }$ ("evidence of curvature of spacetime").

B. Ask how rapidly a vector ffeld $\pmb { \nu }$ is changing along a curve with tangent vector ${ \pmb u } = d / d \lambda$ The answer, $d { \pmb v } / d \lambda \equiv \breve { \pmb v } _ { \pmb u } { \pmb v } \equiv$ "rate of change of $\pmb { \nu }$ with respect to $\lambda ^ { \prime \prime } \equiv ^ { \bullet }$ covariant derivative of $\pmb { \nu }$ along u,” is constructed by the following obvious procedure:(l） Take $\pmb { \nu }$ at $\lambda = \lambda _ { 0 } + \varepsilon$ (2）Parallel transport it back to $\lambda = \lambda _ { 0 }$ .(3) Calculate how much it differs from $\pmb { \nu }$ there. (4) Divide byε (and take limit as $\varepsilon \longrightarrow 0$ ）：

"Covariant differentiation" as defined by paraliel transport

$$
\pmb { \nabla _ { \pmb { u } } } \pmb { v } = \underset { \varepsilon  0 } { \mathrm { L i m } } \{ \frac { [ \pmb { v } ( \lambda _ { 0 } ^ { - } + \varepsilon ) ] _ { \mathrm { p a r a l l e l t r a n s p o r t e d t o } \lambda _ { 0 } } - \pmb { v } ( \lambda _ { 0 } ) } { \varepsilon } \} .
$$

I $\mathbf { \hat { \mu } } ( \mathbf { \bar { \mu } } ( \mathbf { \sigma } ) = d / d \lambda$ is short compared to scale of inhomogeneities in the vector field $\pmb { \nu } _ { : }$ then $\yen 1$ can be read directly off drawing I,or, equally well, off drawing I1.

![](images/f5411ae7560c1b3546ec7a6db6e790eaed58125d77deecc201f357003b521a6f.jpg)

![](images/79b40b4c83d9afdafdb3a7838e2fd59d8faef622669737653a2dd9f107667a45.jpg)

"Symmetry" of covariant differentiation

![](images/b129d4a9afd2b3d47a523f84b06c37667cd42fd2327f12de6bbf76dc649130e0.jpg)  
Box 10.2 (continued)

Chain rule for covariant differentiation

![](images/1a0c6d9987adae5fa4bc7621956969e786a0360e04204041a684ec6f55ce7e29.jpg)  
Additivity for covariant differentiation

C. Take two vector felds. Combine into one the two diagrams for $\yen 1$ and $\yen 4$ Thereby discover that $\pmb { \nabla } _ { \pmb { u } } \pmb { v } - \pmb { \nabla } _ { \pmb { v } } \pmb { u }$ is the vector by which the v-u-v-u quadrilateral fails to close-i.e. (see Box 9.2)，it is the commutator $[ \pmb { u } , \pmb { v } ]$ ： $\begin{array} { r } { \check { \Psi } _ { u } v - \check { \Psi } _ { v } u = [ u , v ] } \end{array}$

Terminology: $\blacktriangledown$ is said to be a “symmetric”or "torsion-free” covariant derivative when $\yen 1$ $- \nabla _ { v } \pmb { u } = [ \pmb { u } , \pmb { v } ]$ Other types of covariant derivatives,as studied by mathematicians,have no relevance for any gravitation theory based on the equivalence principle.

D. The “take-the-difference”and “take-the-limit” process used to define $\check { \check { \mathbf { \psi } } } _ { \pmb { \psi } } \hat { \pmb { \ v } }$ guarantees that it obeys the usual rule for differentiating products:

u(fv)= fuv + （uLflDv 个个   
scalar vector “derivative of f along   
field field u,” denoted $\widehat { v } _ { u } f$ in first part of book；actually equal to $d f / d \lambda$ if ${ \pmb u } = d / d \lambda$ ； also sometimes denoted $\pmb { \nabla } _ { \pmb { u } } f _ { \pmb { \cdot } } ,$

(for proof, see exercise 10.2.)

E.In the real physical world,be it Newtonian or relativistic, parallel transport of a triangle cannot break its legs apart: (l) A,B, C initially such that $\pmb { A } + \pmb { B } = \pmb { C }$ (2)A,B, $\pmb { c }$ each parallel transported with himself by freely falling (inertial） observer;(3）then $\pmb { A } + \pmb { B } = \pmb { C }$ always. Any other result would violate the equivalence principle!

1. Consequence of this (as seen by following through definition of covariant derivative, and by noting that any vector $\pmb { u }$ can be regarded as the tangent vector to a freely falling world line):

$$
\nabla _ { u } ( v + w ) = \nabla _ { u } v + \nabla _ { u } w
$$

for any vector ${ \pmb u }$ and vector fields $\pmb { \nu }$ and w.

2.Consequence of this,combined with symmetry of covariant derivative, and with additivity of the “closer of quadrilaterals” $[ { \pmb u } , { \pmb v } ]$

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } + \pmb { n } } \pmb { v } = \pmb { \nabla } _ { \pmb { u } } \pmb { v } + \pmb { \nabla } _ { \pmb { n } } \pmb { v } . } \end{array}
$$

(See exercise.l0.1.） This can be inferred, alternatively, from the equivalence principle: in a local inertial frame,as in special relativity or Newtonian theory, the change in $\pmb { \nu }$ along ${ \pmb u } + { \pmb n }$ should equal the sum of the changes along $\pmb { u }$ and along $\pmb { n }$

3.Consequence of above: choose $\pmb { n }$ to be a multiple of $\pmb { u }$ ；thereby conclude

$$
\begin{array} { r } { \mathbf { \check { v } } _ { a u } \pmb { v } = a \pmb { \nabla } _ { \pmb { u } } \pmb { v } . } \end{array}
$$

F. The“Schild's ladder” construction process for parallel transport (beginning of this box), applied to the tangent vector of a geodesic (exercise l0.6) guarantees: a geodesic parallel transports its own tangent vector along itself. Translated into covariant-derivative language:

$$
\begin{array} { r }  \pmb { \mu = d / d \lambda \mathrm { ~ i s ~ a ~ t a n g e n t } } \\ { \pmb { \mathrm { v e c t o r ~ t o ~ a ~ c u r v e , ~ a n d } } } \\ { \pmb { \nabla _ { u } u = 0 } } \end{array}
$$

Thus closes the circle: geodesic to parallel transport to covariant derivative to geodesic.

Geodesics as defined by parallel transport or covariant differentiation

Symmetry: $\pmb { \nabla } _ { \pmb { u } } \pmb { v } - \pmb { \nabla } _ { \pmb { v } } \pmb { u } = [ \pmb { u } , \pmb { v } ]$ for any vector felds $\pmb { u }$ and ${ \pmb v } ^ { * }$

Chain rule:

![](images/a005bb66538399a49909fed82189f27de1298e2f98a4a2c6e8d18cce38d48aec.jpg)

![](images/8d5f76d71abdc6f909aebebea788b5518af849984cfd594fac8dcafcacd5af18.jpg)  
Figure 10.2. The link between the tangent spaces at neighboring points，made possible by a parallel-transport law. Choose basis vectors $\pmb { e _ { 1 } }$ and $\pmb { e } _ { 2 }$ at the event $\pmb { \mathcal { Q } }$ .Parallel transport them to a neighboring eventB.(Schild's ladder for transport of $e _ { 1 }$ is shown in the figure.) Then any other vector $\pmb { v }$ that is parallel transported from $\pmb { \mathcal { a } }$ to $\it { : } \overrightarrow { \beta }$ will have the same components at the two events (parallel transport cannot break the legs of a triangle; see $\mathfrak { B o x } \ 1 0 . 2 ;$ ：

Thus,parallel transport provides a unique and complete link between the tangent space at $\boldsymbol { \mathcal { Q } }$ and the tangent space at $\pmb { \mathcal { B } }$ It identifies a unique vector at $\boldsymbol { \mathcal { B } }$ with each vector at $\pmb { \mathcal { a } }$ in a way that preserves all algebraic relations.Similarly （see $\ S 1 0 . 3 )$ ,it identifies a unique l-form at $\pmb { \mathcal { B } }$ with each l-form at $\pmb { \mathcal { a } }$ ， and a unique tensor at $\pmb { \mathcal { B } }$ with each tensor at $\pmb { \mathcal { a } }$ ，preserving all algebraic relations such as $\langle { \pmb \sigma } , { \pmb v } \rangle = 1 9 . 9$ and $\pmb { \mathscr { s } } ( \pmb { \sigma } , \pmb { v } , \pmb { w } ) = 3 7 ~ 1$

Actually,all this is true only in the limit when $\pmb { \mathcal { a } }$ and $\boldsymbol { \mathcal { B } }$ are arbitrarily close to each other.When $\pmb { \mathcal { a } }$ and $\boldsymbol { \mathcal { B } }$ are close but not arbitrarily close,the result of parallel transport is slightly different for different paths;so the link between the tangent spaces is slightly nonunique. But the differences decrease by a factor of 4 each time the affine-parameter distance between $\pmb q$ and $\pmb { \mathcal { B } }$ is cut in half; see Chapter 11.

Any “rule” $\blacktriangledown$ ，for producing new vector felds from old, that satisfes these four conditions, is called by differential geometers a “symmetric covariant derivative.” Such a rule is not inherent in the more primitive concepts (Chapter 9) of curves, vectors, tensors, etc. In the arena of a spacetime laboratory, there are as many ways of defining a covariant derivative rule $\blacktriangledown$ as there are of rearranging sources of the gravitational field. Different free-fall trajectories (geodesics） result from different distributions of masses.

Given the geodesics of spacetime,or of any other manifold, one can construct a unique corresponding covariant derivative by the Schild's ladder procedure of Box 10.2.Given any covariant derivative,one can discuss parallel transport via the equation

and one can test whether any curve is a geodesic via

Equation for parallel transport

Thus a knowledge of all geodesics is completely equivalent to a knowledge of the covariant derivative.

The covariant derivative $\blacktriangledown$ generalizes to curved spacetime the flat-space gradient $\blacktriangledown$ . Like its flat-space cousin,it can be viewed as a machine for producing a number $\langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle$ out of a 1-form $\pmb { \sigma }$ ,a vector $\pmb { u }$ ,and a vector field v. This machine viewpoint is explored in Box 10.3. Note there an important fact: despite its machine nature, $\blacktriangledown$ is not a tensor; it is a nontensorial geometric object.

Knowledge of ali geodesics is equivalent to knowledge of covariant derivative

In curved as in flat spacetime, $\blacktriangledown$ can be applied not only to vector fields,but also to functions,1-form fields,and tensor fields.Its action on functions is defined in the obvious manner:

Covariant derivative generalizes flat-space gradient

Action of covariant derivative on functions,1-forms,and tensors

$$
\forall f \equiv d f ; \qquad \forall _ { u } f \equiv \partial _ { u } f \equiv u [ f ] \equiv \langle d f , u \rangle .
$$

Its action on 1-form felds and tensor felds is defined by the curved-space generalization of equation (3.39): VS is a linear machine for calculating the change in output of $\pmb { s }$ ，from point to point,when “constant” (i.e., parallel transported) vectors are inserted into its slots.Example: the gradient of a $\ l ( _ { 1 } ^ { 0 } )$ tensor,i.e.,of a l-form feld $\pmb { \sigma }$ . Pick an event $\mathcal { P } _ { 0 }$ ；pick two vectors ${ \pmb u }$ and $\pmb { \nu }$ in the tangent space at $\mathcal { P } _ { 0 }$ ； construct from $\pmb { \nu }$ a“constant” vector field ${ \pmb v } ( \mathcal { P } )$ by parallel transport along the direction of $\pmb { u } , \pmb { \bigtriangledown _ { u } } \pmb { v } = 0$ . Then $\yen 0$ is a $( _ { 2 } ^ { 0 } )$ tensor, and $\yen 1$ is a $( _ { 1 } ^ { 0 } )$ tensor defined at $\scriptstyle { \mathcal { P } } _ { 0 }$ by

$$
\begin{array} { r } { \Psi \sigma ( { \pmb v } , { \pmb u } ) \equiv \langle \pmb { \nabla _ { \pmb { u } } } \sigma , { \pmb v } \rangle \equiv \pmb { \nabla _ { \pmb { u } } } ( \langle \sigma , { \pmb v } \rangle ) \equiv \frac { d } { d \lambda } \langle \pmb { \sigma } , { \pmb v } \rangle , } \end{array}
$$

where $\pmb { \mu } = \pmb { d } / d \lambda$ . This defines $\yen 0$ and $\yen 1$ ,because it states their output for any (continued on page 257)


<!-- chunk 0005: pages 281-350 -->
# Box 10.3 COVARIANT DERIVATIVE VIEWED AS A MACHINE: CONNECTION COEFFICIENTS AS ITS COMPONENTS

# A.The Machine View

1. The covariant derivative operator $\blacktriangledown$ ,like most other geometric objects,can be regarded as a machine with slots. There is one such machine at each event ${ \boldsymbol { \mathscr { s p } } } _ { 0 }$ in spacetime. In brief, the machine interpretation of $\blacktriangledown$ at ${ \mathcal { P } } _ { 0 }$ says

(g.、v(）,u)=<σ.v>.   
First slot: insert Second slot; insert Third slot:insert A new vector:   
a l-form $\pmb { \sigma }$ that a vector field ${ \pmb v } ( \emptyset ^ { \mathnormal { \mathnormal } } )$ a vector $\pmb { u }$ that “the covariant de  
resides in the tan- defined on a neigh- resides in the rivative of the vec  
gent space at ${ \mathfrak { P } } _ { 0 }$ borhood of $\scriptstyle { \mathcal { P } } _ { 0 }$ tangent space at $\mathcal { P } _ { 9 }$ tor field $\pmb { \nu }$ with J ,respect to u." 1

[Note: this slot notation for $\blacktriangledown$ serves no useful purpose except to emphasize the "machine"-nature of $\blacktriangledown$ . This box is the only place it will be used.]

2.Geometrically, the output of the machine, $\langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle$ ,is obtained as follows: (a) Calculate the rate of change of ${ \pmb v } .$ $\yen 1$ ，along the vector $\pmb { u }$ ；when $\pmb { u }$ and $\pmb { \nu }$ are infinitesimally small, the calculation can be represented pictorially:

![](images/3190889cb58244799ef3f8d29de2e80c9dcc1ace240e150b24bef6b04bcb96f3.jpg)  
$\yen 1$ a vector that resides in the tangent space at $\scriptstyle { \mathcal { P } } _ { 0 }$

(b) Count how many surfaces of the l-form $\pmb { \sigma }$ are pierced by the vector $\yen 1$ (piercing occurs in tangent space at $\scriptstyle { \boldsymbol { \mathscr { s } } } _ { 0 } .$ ）

![](images/5a096cc3c6ddc96de52bdeebc5d542340be3ee2bad97f92fde1ea5e016d2a2cd.jpg)

$$
\langle \pmb { \sigma } , \pmb { \nabla _ { u } } \pmb { v } \rangle = - 2 . 8 .
$$

This number is the output of the machine $\blacktriangledown$ ,when $\pmb { \sigma }$ ${ \pmb v } ( \mathcal { P } )$ and $\pmb { u }$ are inserted into its slots.

3.Another, equivalent, statement of covariant derivative as a machine.Leave first slot empty (no mention of any 1-form $\pmb { \sigma }$ ); get a new vector field from original vector field $\pmb { \nu }$ ：

empty

=“covariant derivative of vector field $\pmb { \nu }$ along vector u."

4.A third machine operation. Leave first and third slots empty (no mention of any 1-form $\pmb { \sigma }$ ； no mention of any vector ${ \pmb u }$ along which to differentiate); get a (l) tensor field from original vector field $\pmb { \nu }$ ：

$$
\pmb { \bigtriangledown } ( \underbrace { \mathbf { \Pi } } _ { : : : } , \pmb { v } ( \pmb { \mathcal { P } } ) , \underbrace { \mathbf { \Pi } } _ { : : : } ) \equiv \pmb { \nabla } \pmb { v }
$$

This tensor field, $\forall v ,$ ,is the curved-space generalization of the flat-space $\forall v$ studied in $\ S 3 . 5$ . It has two slots (the two left empty in its definition). Its output for given input is

$$
\pmb { \nabla } \pmb { v } ( \underbrace { \vphantom { \ d u ( \pmb { v } } , \pmb { u } ) } _ { : : : : } , \pmb { u } ) = \pmb { \nabla } _ { \pmb { u } } \pmb { v }
$$

$$
\begin{array} { r } { \pmb { \nabla } \pmb { v } ( \pmb { \sigma } , \pmb { u } ) = \langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle . } \end{array}
$$

5. Summary of the quantities defined above:

(a) $\blacktriangledown$ is a covariant derivative operator; to get a number from it, insert ${ \pmb \sigma } , { \pmb v } ( \mathcal { P } )$ and $\pmb { u }$ ； the result is $\langle \pmb { \sigma } , \pmb { \ v } _ { \pmb { \ u } } \pmb { v } \rangle$   
(b) $\forall v$ is the gradient of $\pmb { \nu }$ ；to get a number from it,insert $\pmb { \sigma }$ and $\pmb { u }$ ；the result is $\langle \pmb { \sigma } , \pmb { \check { \bigtriangledown } } _ { \pmb { u } } \pmb { v } \rangle$ [same as in (a)}.   
(c） $\yen 1$ is the covariant derivative of $\pmb { \nu }$ along $\pmb { u }$ ; to get a number from it,insert $\pmb { \sigma }$ ； the result is $\langle \pmb { \sigma } , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle$ [same as in (a) and (b)).

# B. How $\blacktriangledown$ Differs from a Tensor

The machine $\blacktriangledown$ differs from a tensor in two ways. (l) The middle slot of $\blacktriangledown$ will not accept a vector; it demands a vector feld-the vector field that is to be differentiated. (2) V is not a linear machine (whereas a tensor must be linear!):

$$
\begin{array} { r l } & { \Psi ( a \sigma . f ( \mathcal { S } ^ { \rho } ) \pmb { v } ( \mathcal { S } ^ { \rho } ) , b \pmb { u } ) \equiv \langle a \sigma , \pmb { \nabla } _ { b \pmb { u } } f \pmb { v } \rangle } \\ & { \qquad = a b f \langle \sigma , \pmb { \nabla } _ { \pmb { u } } \pmb { v } \rangle + \underbrace { a b \langle \sigma , \pmb { v } \rangle \ \pmb { \nabla } _ { \pmb { u } } f } _ { \pmb { \downarrow } } } \\ & { \qquad \quad \mathrm { [ t h i s ~ w o u l d ~ b e ~ a b s e n t ~ i f ~ \pmb { v } ~ w e r e ~ a ] } \} } \\ & { \qquad \quad \mathrm { l i n e a r ~ m a c h i n e } . } \end{array}
$$

# C. The "Connection Coefficients" as Components of $\blacktriangledown$

Given a tensor $\pmb { s }$ of rank $\textstyle { \binom { 1 } { 2 } }$ ,a basis of tangent vectors $\{ \pmb { e } _ { \alpha } \}$ at the event $\mathcal { P } _ { 0 }$ where $\pmb { s }$ resides,and the dual basis of 1-forms $\{ \pmb { \omega } ^ { \alpha } \}$ ,one defines the components of $\pmb { s }$ by

$$
S ^ { \alpha } { } _ { \beta \gamma } \equiv \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } , \pmb { e } _ { \gamma } ) .
$$

One defines the components of $\blacktriangledown$ similarly, except that for $\blacktriangledown$ one needs not only a basis $\{ \pmb { e } _ { \alpha } \}$ at the event ${ \mathcal { P } } _ { 0 } ,$ but also a basis $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ at each event $\mathcal { P }$ in its neighborhood:

$$
\begin{array} { r l } & { \Gamma ^ { \alpha } { } _ { \beta \gamma } \equiv \mathrm { c o m p o n e n t s ~ o f ~ } \Psi = \Psi ( \boldsymbol { \omega } ^ { \alpha } , \boldsymbol { \mathbf { e } } _ { \beta } ( \mathcal { P } ) , \boldsymbol { \mathbf { e } } _ { \gamma } ) } \\ & { \qquad \equiv \langle \boldsymbol { \omega } ^ { \alpha } , \nabla _ { \pmb { e } _ { \gamma } } \mathbf { e } _ { \beta } \rangle } \\ &  \qquad \simeq \bigg ( \begin{array} { l } { \mathrm { \cdots } \mathrm { { \alpha } c o m p o n e n t ~ o f ~ c h a n g e ~ i n ~ b a s i s ~ v e c t o r ~ } \pmb { e } _ { \beta } , \mathrm { ~ w h e n } } \\ { \mathrm { i n ~ e v a l u a t i n g ~ } \pmb { e } _ { \beta } \mathrm { ~ o n e ~ m o v e s ~ f r o m ~ t a i l ~ t o ~ t i p ~ o f ~ } \pmb { e } _ { \gamma } \bigg ) . } \end{array} \end{array}
$$

These components of $\blacktriangledown$ are called the “connection coeffcients” of the basis $\big \{ \pmb { e } _ { \alpha } \big \}$ They are the “coordinate representation’of the covariant derivative operator $\blacktriangledown$

Thecovariant derivativeoperator $\blacktriangledown$ and the connection coeficients $\Gamma ^ { \alpha } { } _ { \mu \nu }$ provide different mathematical representations of the same geometric animal? Preposterous! The one animal runs from place to place and barks, or at least bites (takes difference, for example,between vector fields at one place and at a nearby place).The other animal, endowed with forty faces (see exercise 10.9) sits quietly at one spot. It would be difficult for two animals to look more different. Yet they do the same jobs in any world compatible with the equivalence principle: (1） they summarize the properties of all geodesics that go through the point in question; and,so doing, (2) they provide a physical means (parallel transport) to compare the values of vector fields and tensor fields at two neighboring events.

given input vectors $\pmb { \nu }$ and $\pmb { u }$ if ${ \pmb v } ( \mathcal { P } )$ is not constrained to be “constant” along $\pmb { \upsilon } = \pmb { d } / d \lambda$ ,then $( d / d \lambda ) \langle \pmb { \sigma } , \pmb { v } \rangle$ has contributions from both the change in $\pmb { \nu }$ and the change in $\pmb { \sigma }$ ：

$$
\frac { d } { d \lambda } \langle \sigma , v \rangle \equiv \pmb { \nabla } _ { u } \langle \sigma , v \rangle = \langle \pmb { \nabla } _ { u } \sigma , v \rangle + \langle \sigma , \pmb { \nabla } _ { u } v \rangle
$$

(see exercise 10.3).

Similarly, if $\pmb { s }$ is a $\mathbf { \Sigma } ( _ { 2 } ^ { 1 } )$ tensor field, then its gradient VS is a $\textstyle { \binom { 1 } { 3 } }$ tensor field defined as follows. Pick an event $\mathcal { P } _ { \mathbf { 0 } }$ pick three vectors ${ \pmb u } , { \pmb v } , { \pmb w } ,$ and a 1-form $\pmb { \sigma }$ in the tangent space at $\mathcal { P } _ { 0 } \mathrm { : \Omega }$ turn $\nu , w ,$ and $\pmb { \sigma }$ into “constant” vector fields and a “constant” 1-form field near $\mathcal { P } _ { \mathbf { 0 } }$ by means of parallel transport ( $\mathbf { \nabla } \cdot \mathbf { \vec { v } } _ { u } \mathbf { \vec { v } } = \mathbf { \nabla } \cdot \mathbf { \vec { w } } = \mathbf { \nabla } \cdot \mathbf { \vec { v } } _ { u } \mathbf { \vec { \sigma } } = 0$ at ${ \mathcal { P } } _ { 0 } ,$ ； then define

$$
\begin{array} { c } { { \nabla S ( \sigma , v , w , { \boldsymbol u } ) \equiv ( \nabla _ { \boldsymbol u } S ) ( \sigma , v , { \boldsymbol w } ) \equiv \nabla _ { \boldsymbol u } [ S ( \sigma , v , { \boldsymbol w } ) ] } } \\ { { { } } } \\ { { { } = \partial _ { \boldsymbol u } [ S ( \sigma , v , { \boldsymbol w } ) ] . } } \end{array}
$$

# Exercise 1O.1. ADDITIVITY OF COVARIANT DIFFERENTIATION

Show that the commutator ("closer of quadrilaterals") is additive:

$$
[ u , v + w ] = [ u , v ] + [ u , w ] ; \qquad [ u + n , v ] = [ u , v ] + [ n , v ] .
$$

Use this result,the additivity condition $\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } ( \pmb { v } + \pmb { w } ) = \pmb { \nabla } _ { \pmb { u } } \pmb { v } + \pmb { \nabla } _ { \pmb { u } } \pmb { w } , } \end{array}$ and symmetry of the covariant derivative, $\begin{array} { r } { \nabla _ { u } v - \nabla _ { v } u = [ u , v ] , } \end{array}$ to prove that

$$
\pmb { \nabla } _ { \pmb { u } + \pmb { m } } \pmb { v } = \pmb { \nabla } _ { \pmb { u } } \pmb { v } + \pmb { \nabla } _ { \pmb { n } } \pmb { v } .
$$

# Exercise 1O.2. CHAIN RULE FOR COVARIANT DIFFERENTIATION

Use pictures,and the “take-the-diference-and-take-the-limit” definition of $\yen 1$ (Box 10.2) to show that

$$
\pmb { \nabla _ { \pmb { u } } } ( f \pmb { v } ) = f \pmb { \nabla _ { \pmb { u } } } \pmb { v } + \pmb { v } \partial _ { \pmb { u } } [ f ] .
$$

# Exercise 1O.3. ANOTHER CHAIN RULE

Derive equation (l0.7)，using the “take-the-difference-and-take-the-limit” definitions of derivatives. Hint:Before taking the differences,parallel transport $\pmb { \sigma } [ \mathcal { P } ( \lambda ) ]$ and ${ \pmb v } \widetilde { \mathscr { P } } ( \lambda ) ]$ back from $\mathcal { P } ( \lambda )$ to ${ \mathcal { P } } ( 0 )$

# Exercise 1O.4. STILL ANOTHER CHAIN RULE

Show that, as in flat spacetime,so also in curved spacetime,

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } ( \pmb { v } \otimes \pmb { w } ) = ( \pmb { \nabla } _ { \pmb { u } } \pmb { v } ) \otimes \pmb { w } + \pmb { v } \otimes ( \pmb { \nabla } _ { \pmb { u } } \pmb { w } ) . } \end{array}
$$

Write down the more familiar component version of this equation in flat spacetime.

Solution to first part of exercise: Choose l-forms $\pmb { \sigma }$ and $\pmb { \rho }$ at the event $\scriptstyle { \mathcal { P } } _ { 0 }$ in question, and extend them along the vector $\pmb { u } = d / d \lambda$ by parallel transport, $\yen 123,456$ .Then

(def of $\pmb { \check { \check { \mathbf { \alpha } } } } _ { \pmb { \alpha } }$ on a tensor)

def of tensor product “ $\cdot \otimes ^ { \dag }$ ）

$$
{ \begin{array} { l } { \displaystyle [ \nabla _ { \boldsymbol { u } } ( { \boldsymbol { v } } \otimes { \boldsymbol { w } } ) ] ( \rho . \sigma ) = { \frac { d } { d \lambda } } [ ( { \boldsymbol { v } } \otimes { \boldsymbol { w } } ) ( \rho , \sigma ) ] } \\ { \displaystyle \qquad = { \frac { d } { d \lambda } } [ \langle \rho , { \boldsymbol { v } } \rangle \langle \sigma . { \boldsymbol { w } } \rangle ] } \\ { \displaystyle \qquad = { \frac { d \langle \rho , { \boldsymbol { v } } \rangle } { d \lambda } } \langle \sigma , { \boldsymbol { w } } \rangle + \langle \rho , { \boldsymbol { v } } \rangle { \frac { d \langle \sigma , { \boldsymbol { w } } \rangle } { d \lambda } } } \\ { \displaystyle \qquad = \langle \rho , \nabla _ { \boldsymbol { u } } { \boldsymbol { v } } \rangle \langle \sigma , { \boldsymbol { w } } \rangle + \langle \rho , { \boldsymbol { v } } \rangle \langle \sigma , \nabla _ { \boldsymbol { u } } { \boldsymbol { w } } \rangle } \\ { \displaystyle \qquad = [ ( \nabla _ { \boldsymbol { u } } { \boldsymbol { v } } ) \otimes { \boldsymbol { w } } ] ( \rho , \sigma ) + [ \mathbf { v } \otimes ( \nabla _ { \boldsymbol { u } } { \boldsymbol { w } } ) ] ( \rho , \sigma ) } \end{array} }
$$

(def of tensor product $\ " \otimes \ " )$

# Exercise 10.5. ONE MORE CHAIN RULE

Show,using techniques similar to those in exercise l0.4, that

$$
\begin{array} { r } { \Psi _ { u } ( \sigma \otimes \rho \otimes v ) = ( \pmb { \nabla } _ { u } \sigma ) \otimes \rho \otimes \pmb { v } + \sigma \otimes ( \pmb { \nabla } _ { u } \rho ) \otimes \pmb { v } + \sigma \otimes \rho \otimes ( \pmb { \nabla } _ { u } \pmb { v } ) . } \end{array}
$$

# Exercise 10.6. GEODESIC EQUATION

Use the “Schild's ladder" construction process for parallel transport (beginning of Box l10.2) to show that a geodesic paralel transports its own tangent vector along itself (end of Box 10.2).

# S10.4. PARALLEL TRANSPORT AND COVARIANTDERIVATIVE: COMPONENT APPROACH

The pictorial approach motivates the mathematics; the abstract approach makes the pictorial ideas precise; but usually one must use the component approach in order to actually do complex calculations.

To work with components, one needs a set of basis vectors $\{ \pmb { e } _ { \alpha } \}$ and the dual set of basis 1-forms $\{ \pmb { \omega } ^ { \alpha } \}$ . In flat spacetime a single such basis suffices; all events can use the same Lorentz basis. Not so in curved spacetime! There each event has its own tangent space, and each tangent space requires a basis of its own. As one travels from event to event, comparing their bases via parallel transport, one sees the bases twist and turn. They must do so. In no other way can they accommodate themselves to the curvature of spacetime. Bases at points $\mathcal { P } _ { 0 }$ and $\mathcal { P } _ { 1 } .$ ，which are the same when compared by parallel transport along one curve, must differ when compared along another curve (see “Curvature"; Chapter 11).

To quantify the twisting and turning of a “field” of basis vectors $\{ \pmb { e } _ { \alpha } ( { \mathcal { P } } ) \}$ and forms $\{ \pmb { \omega } ^ { \alpha } ( \mathcal { P } ) \}$ , use the covariant derivative. Examine the changes in vector fields along a basis vector ${ \pmb { e } } _ { \beta }$ ,abbreviating

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { \theta } _ { \beta } } } \equiv \pmb { \nabla _ { \beta } } \qquad ( \operatorname* { d e f } \ \mathrm { o f } \ \pmb { \nabla _ { \beta } } ) ; } \end{array}
$$

and especially examine the rate of change of some basis vector: $\pmb { \nabla } _ { \beta } \pmb { e } _ { \alpha } ,$ Thisrate of change is itself a vector, so it can be expanded in terms of the basis:

$$
\begin{array} { r } { \pmb { \nabla } _ { \beta } \pmb { e } _ { \alpha } = \pmb { e } _ { \mu } { \cal T } _ { \alpha \beta } ^ { \mu } \qquad ( \operatorname* { d e f } \operatorname { o f } { \varGamma ^ { \mu } } _ { \alpha \beta } ) ; } \end{array}
$$

note reversal of order of $\pmb { \alpha }$ and $\beta$ ！

and the resultant“connection coeffcients" $T ^ { \mu } { } _ { \alpha \beta }$ can be calculated by projection on the basis 1-forms:

$$
\langle { \pmb { \omega } } ^ { \mu } , { \pmb { \nabla } } _ { \beta } { \pmb e } _ { \alpha } \rangle = { \cal T } ^ { \mu } { } _ { \alpha \beta } .
$$

(See exercise l0.7;also Box l0.3.） Because the basis 1-forms are “locked into” the basis vectors $( \langle { \pmb { \omega } } ^ { \nu } , { \pmb e } _ { \alpha } \rangle = \delta _ { \alpha } ^ { \nu } )$ , these same connection coefficients $T ^ { \nu } { } _ { \alpha \dot { \beta } }$ tell how the 1-form basis changes from point to point:

$$
\begin{array} { c } { { \pmb { \nabla } _ { \beta } \pmb { \omega } ^ { \nu } = - \pmb { \Gamma } ^ { \nu } { } _ { \alpha \beta } \pmb { \omega } ^ { \alpha } , } } \\ { { \langle \pmb { \nabla } _ { \beta } \pmb { \omega } ^ { \nu } , \pmb { e } _ { \alpha } \rangle = - \pmb { \Gamma } ^ { \nu } { } _ { \alpha \beta } . } } \end{array}
$$

(See exercise 10.8.)

The connection coefficients do even more. They allow one to calculate the components of the gradient of an arbitrary tensor $\pmb { s }$ . In a Lorentz frame of flat spacetime, the components of $\yen 5$ are obtained by letting the basis vectors ${ \pmb e } _ { \alpha } = \partial \mathcal { P } / \partial x ^ { \alpha } =$ $\partial / \partial x ^ { \alpha }$ act on the components of $\pmb { s }$ Thus for a $\mathbf { \Sigma } ( _ { 2 } ^ { 1 } )$ tensor field $\pmb { s }$ one finds that

$$
{ \pmb \nabla } { \pmb S } ~ \mathrm { h a s ~ c o m p o n e n t s } ~ S _ { ~ \beta \gamma , \delta } ^ { \alpha } = \frac { \partial } { \partial \pmb x ^ { \delta } } [ S _ { ~ \beta \gamma } ^ { \alpha } ] .
$$

Not so in curved spacetime, or even in a non-Lorentz basis in flat spacetime. There the basis vectors turn, twist, expand, and contract, so even if $\pmb { s }$ were constant $( \pmb { \nabla } \pmb { s } = 0 )$ , its components on the twisting basis vectors would vary. The connection coefficients, properly applied, wil compensate for this twisting and turning. As one learns in exercise l0.10,the components of $\yen 5$ ,called $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ so that

Components of the gradient ofa tensor field

$$
\pmb { \nabla } \pmb { S } = S ^ { \alpha } { } _ { \beta \gamma ; \pmb { \delta } } \pmb { \sigma } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } \otimes \pmb { \omega } ^ { \delta } ,
$$

can be calculated from those of $\pmb { s }$ by the usual flat-space method, plus a correction applied to each index (i.e., to each basis vector):

$$
 \begin{array} { r l } { { \boldsymbol { \mathfrak { n } } } : \mathbf { w h e n ~ c o r r e c t i n g ~ } ^ { * } \mathbf { u p } ^ { * } { \mathrm { ~ i n d i c e s } } \mathbf { \Psi } } & { { \left[ \begin{array} { l } { \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \\ { \mathrm { o n ~ i n d e x ~ b e i n g ~ c o r r e c t e d } } \\ { \displaystyle } \end{array} \right] } } \\ &  \qquad { \left[ \begin{array} { l } { \qquad \qquad \displaystyle { \begin{array} { l } { \qquad \qquad \displaystyle { \Biggl \downarrow } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } } \\ { \qquad \displaystyle { \vphantom { \qquad \displaystyle { \Biggl { \downarrow } } } } \left[ { \mathrm { i n d e x ~ b e i n g ~ i n d e x } } \right] } \end{array}  } } \qquad { \mathrm { i n d e x } } \mathbf { \Psi } } \\ { \right]\qquad { \boldsymbol { S } } ^ { \alpha } _ { \beta \gamma ; \delta } = { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \gamma , \delta } + { \boldsymbol { S } } ^ { \mu } { \boldsymbol { \beta } } _ { \gamma } { \boldsymbol { T } } ^ { \alpha } { \mathrm { ~ \dagger } } \mathbf { \Psi } ^ { \beta } _ { \beta \delta } - { \boldsymbol { \frac { \uparrow } { \alpha } } } { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \gamma } { \boldsymbol { T } } ^ { \mu } { \boldsymbol { \beta } } _ { \beta \delta } - { \boldsymbol { S } } ^ { \alpha } { \boldsymbol { \beta } } _ { \beta \mu } { \boldsymbol { T } } ^ { \mu } { \boldsymbol { \gamma } } _ { \gamma \delta } , } \\ { \qquad \displaystyle { \left[ \begin{array} { l } { { \qquad \mathrm { i n t e n ~ c o r r e c t i n g ~ i n d i c e s } } \\ { \qquad \quad \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \\ { \qquad \displaystyle { \Biggl [ \mathrm { i n t e r c h a n g e ~ a n d ~ s u m } } \end{array}  } } \qquad { \mathrm { V o r ~ } } \mathbf { \Psi } } \end{\right]array} } \end{array} \end{array}
$$

Here

$$
S ^ { \alpha } { } _ { \beta \gamma , \delta } \equiv e _ { \delta } [ S ^ { \alpha } { } _ { \beta \gamma } ] \equiv \partial _ { \pmb { \rho } _ { \delta } } S ^ { \alpha } { } _ { \beta \gamma } .
$$

Components of the covariant derivative of a tensor field

Equation (l0.18) looks complicated;but it is really very simple,once the pattern has been grasped.

Just as one uses special notation, $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ ，for the components of $\yen 5$ so one introduces special notation, $D S ^ { \alpha } { } _ { \beta \gamma } / d \lambda$ ,for components of the covariant derivative $\pmb { \nabla _ { \pmb { u } } } \pmb { S }$ along ${ \pmb u } = d / d \lambda$ ：

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { S } = ( D S ^ { \alpha } { } _ { \beta \gamma } / d \lambda ) \pmb { e _ { \alpha } } \otimes \pmb { \omega ^ { \beta } } \otimes \pmb { \omega ^ { \gamma } } ; } \end{array}
$$

$$
{ \frac { D S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } = S ^ { \alpha } { } _ { \beta \gamma ; \delta } u ^ { \delta } = ( S ^ { \alpha } { } _ { \beta \gamma , \delta } + \mathrm { c o r r e c t i o n ~ t e r m s } ) u ^ { \delta } .
$$

Since for any $f$

$$
f _ { , \delta } u ^ { \delta } = \partial _ { \pmb { u } } f = d f / d \lambda
$$

this reduces to

$$
{ \frac { D S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } = { \frac { d S ^ { \alpha } { } _ { \beta \gamma } } { d \lambda } } + S ^ { \mu } { } _ { \beta \gamma } { } T ^ { \alpha } { } _ { \mu \delta } u ^ { \delta } - S ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta \delta } u ^ { \delta } - S ^ { \alpha } { } _ { \beta \mu } { } T ^ { \mu } { } _ { \gamma \delta } u ^ { \delta } .
$$

Chain rule for gradient

The power of the component approach shows up clearly when one discusses chain rules for covariant derivatives. The multitude of abstract-approach chain rules (equations l0.2b, l0.7,10.10,10.11) all boil down into a single rule for components: The gradient operation “;” obeys the standard partial-differentiation chain rule of ordinary calculus.Example:

$$
\begin{array}{c} ( f v ^ { \alpha } ) _ { ; \mu } = f _ { ; \mu } v ^ { \alpha } + f v _ { ; \mu } ^ { \alpha }  \\ { \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \mathrm { ~ } } \end{array}
$$

(contract this with $u ^ { \mu }$ to get chain rule l0.2b). Another example:

$$
\begin{array} { l } { { ( \sigma _ { \alpha } v ^ { \alpha } ) _ { ; \mu } = \sigma _ { \alpha ; \mu } v ^ { \alpha } + \sigma _ { \alpha } v ^ { \alpha } { } _ { ; \mu } } } \\ { { \mathrm { ~ } \qquad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } } \\ { { \mathrm { ~ } \qquad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } } \end{array}
$$

(contract this with $u ^ { \mu }$ to get chain rule 10.7). Another example:

$$
( \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } ) _ { ; \mu } = \sigma _ { \alpha ; \mu } \rho _ { \beta } v ^ { \gamma } + \sigma _ { \alpha } \rho _ { \beta ; \mu } v ^ { \gamma } + \sigma _ { \alpha } \rho _ { \beta } v ^ { \gamma } { } _ { ; \mu }
$$

EXERCISES

(contract this with $u ^ { \mu }$ to get chain rule 10.11). Another example: see Exercise (10.12) below.

# Exercise 10.7. COMPUTATION OF CONNECTION COEFFICIENTS Derive equation (l0.l4) for $T ^ { \mu } { } _ { \alpha \beta }$ from equation (10.13).

Exercise 10.8. CONNECTION FOR 1-FORM BASIS   
Derive equations (l0.15) and (10.16), which relate ${ \pmb v } _ { \beta } { \pmb \omega } ^ { \nu }$ 10 ${ { T ^ { \nu } } _ { \alpha \beta } }$ ，from equation (10.14). Hint: use equation (10.7).

# Exercise 10.9. SYMMETRY OF CONNECTION COEFFICIENTS

Show that the symmetry of spacetime's covariant derivative (equation l0.2a) is equivalent to the following symmetry condition on the connection coefficients:

$$
\begin{array} { l }  { \equiv { \cal { T } } ^ { \mu } { } _ { [ \alpha \beta ] } = - \frac { 1 } { 2 } \langle { \pmb { \omega } } ^ { \mu } , \underbrace { [ { \pmb { e } } _ { \alpha } , { \pmb { e } } _ { \beta } ] } _ { \displaystyle \mathrm { ~ \pmb { \ / { \ / { \ / } } } ~ } } \rangle \equiv - \frac { 1 } { 2 } c _ { \alpha \beta } \mathrm { \tiny { / } } \mathrm { ~ \pmb { \ / { \ / { \ / } } } ~ } } \\ { \mathrm { m u t a t o r ~ o f ~ b a s i s ~ v e c t o r s } { \ ! } } \end{array}
$$

As a special case, $T ^ { \mu } { } _ { \alpha \beta }$ is symmetric in α and $\beta$ when a coordinate basis $( \pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha } )$ is used. Show that in a coordinate basis this symmetry reduces the number of independent connection coeffcients at each event from $4 \times 4 \times 4 = 6 4$ to $4 \times 1 0 = 4 0$

# Exercise 10.10. COMPONENTS OF GRADIENT

Derive equation (10.18)for the components of the gradient, $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$ . Hint: Expand $\pmb { s }$ in terms of the given basis,and then evaluate the righthand side of

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { S } = \pmb { \nabla } _ { \pmb { u } } ( S ^ { \alpha } { } _ { \beta \gamma } \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ) , } \end{array}
$$

for an arbitrary vector $\pmb { u }$ Use the chain rules (l0.2b) and (l0.l1). By comparing the result with

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { S } = S ^ { \alpha } { } _ { \beta \gamma ; \delta } u ^ { \delta } \pmb { e } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ,
$$

read of te components $S ^ { \alpha } { } _ { \beta \gamma ; \delta }$

# Exercise 10.11. DIVERGENCE

Let $\pmb { \tau }$ be a $\textstyle { { \binom { 2 } { 0 } } }$ tensor field,and define the divergence on its second slot by the same process as in flat spacetime: $\pmb { \bigtriangledown } \cdot \pmb { \tau } =$ contraction of $\forall \pmb { \tau } _ { }$ i.e.,

$$
( \pmb { \nabla } \cdot \pmb { \tau } ) ^ { \alpha } = T ^ { \alpha \beta } { } _ { ; \beta } .
$$

Write the components $T ^ { \alpha \beta } { } _ { ; \beta }$ in terms of $T ^ { \alpha \beta } { } _ { , \beta }$ plus correction terms for each of the two indices of ${ \pmb \tau } .$

[Answer:

$$
T ^ { \alpha \beta } { } _ { ; \beta } = T ^ { \alpha \beta } { } _ { , \beta } + { } T ^ { \alpha } { } _ { \mu \beta } T ^ { \mu \beta } + T ^ { \beta } { } _ { \mu \beta } T ^ { \alpha \mu } { } . ]
$$

# Exercise 10.12. VERIFICATION OF CHAIN RULE

Let $S ^ { \alpha \beta } { } _ { \gamma }$ be components of a $\mathbf { \Sigma } ( _ { 1 } ^ { 2 } )$ tensor field, and $M _ { \beta } { } ^ { \gamma }$ be components of a $\textstyle { { \binom { 1 } { 1 } } }$ tensor field. By contracting these tensor fields,one obtains a vector field $S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma }$ 、The chain rule for the divergence of this vector field reads

$$
( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { ; \alpha } = S ^ { \alpha \beta } { } _ { \gamma ; \alpha } M _ { \beta } { } ^ { \gamma } + S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } { } _ { ; \alpha } ,
$$

Verify the validity of this chain rule by expressing both sides of the equation in terms of directional derivatives $\{ \cdot _ { e _ { \alpha } } )$ plus connection-coefficient corrections. Hint: the left side becomes

$$
( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { ; \alpha } = \underbrace { ( S ^ { \alpha \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) _ { , \alpha } } _ { \Big \uparrow } + \Gamma ^ { \alpha } { } _ { \mu \alpha } ( S ^ { \mu \beta } { } _ { \gamma } M _ { \beta } { } ^ { \gamma } ) .
$$

The right side has many more correction terms (three on $S ^ { \alpha \beta } { } _ { \gamma : \alpha }$ ： two on $M _ { \beta } { } ^ { \gamma } { } _ { ; \alpha } )$ , but they must cancel against each other, leaving only one.

Exercise 1O.13. TRANSFORMATION LAW FOR CONNECTION COEFFICIENTS

Let $\{ \pmb { e } _ { \alpha } \}$ and $\{ \pmb { e } _ { \mu ^ { \prime } } \}$ be two different fields of basis vectors related by the transformation law

$$
\pmb { e } _ { \mu ^ { \prime } } ( \vartheta ^ { \bar { p } } ) = L ^ { \alpha } { } _ { \mu ^ { \prime } } ( \vartheta ^ { \bar { p } } ) \pmb { e } _ { \alpha } ( \vartheta ^ { \bar { p } } ) .
$$

Show that the corresponding connection coefficients are related by

$$
\begin{array} { r } { { \int ^ { \alpha ^ { \prime } } } { } _ { \beta ^ { \prime } \gamma ^ { \prime } } = \underbrace { L ^ { \alpha ^ { \prime } } { } _ { \rho } L ^ { \mu } { } _ { \beta ^ { \prime } } L ^ { \nu } { } _ { \gamma ^ { \prime } } } _ { \beta ^ { \prime } \gamma ^ { \prime } } \Gamma ^ { \rho } { } _ { \mu \nu } + L ^ { \alpha ^ { \prime } } { } _ { \mu } L ^ { \mu } { } _ { \beta ^ { \prime } , \gamma ^ { \prime } } } \end{array}
$$

standard transformation law for components of a tensor

# Exercise 10.14. POLAR COORDINATES IN FLAT 2-DIMENSIONAL SPACE

On a sheet of paper draw an $( r , \phi )$ polar coordinate system. At neighboring points, draw the basis vectors $\pmb { e } _ { \hat { \tau } } = \hat { \partial } / \hat { c } r$ and $\pmb { e } _ { \hat { \phi } } \equiv r ^ { - 1 } \partial / \partial \phi$ .(a)Use this picture,and Euclid's version of parallel transport, to justify the relations

$$
\forall _ { \hat { \tau } } \pmb { e } _ { \hat { \tau } } = 0 , \qquad \pmb { \nabla } _ { \hat { \tau } } \pmb { e } _ { \hat { \phi } } = 0 , \qquad \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \tau } } = r ^ { - 1 } \pmb { e } _ { \hat { \phi } } , \qquad \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \phi } } = - r ^ { - 1 } \pmb { e } _ { \hat { \tau } } ,
$$

(b) From these relations write down the connection coeffcients. (c) Let $\pmb { A } = A ^ { \hat { \tau } } \pmb { e } _ { \hat { \tau } } + A ^ { \hat { \phi } } \pmb { e } _ { \hat { \phi } }$ bea vectorfield. Show thatits divergence, $\pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { \alpha } } { } _ { ; \hat { \alpha } } = A ^ { \hat { \alpha } } { } _ { , \hat { \alpha } } + \Gamma ^ { \hat { \alpha } } { } _ { \hat { \mu } \hat { \alpha } } A ^ { \hat { \mu } }$ , can be calculated using the formula

$$
\pmb { \nabla } \cdot \pmb { A } = \frac { 1 } { r } \frac { \partial A \hat { \phi } } { \partial \phi } + \frac { 1 } { r } \frac { \partial ( r A ^ { \hat { \tau } } ) } { \partial r }
$$

(which should be familiar to most readers).

# \$10.5. GEODESIC EQUATION

Geodesic equation: abstract version

Geodesics--the parametrized paths of freely falling particles-were the starting point of this chapter. From them parallel transport was constructed (Schild's ladder; Box 10.2);and parallel transport in turn produced the covariant derivative and its connection coefficients. Given the covariant derivative, one recovered the geodesics: they were the curves whose tangent vectors, $\pmb { \upsilon } = d \mathcal { P } / d \lambda$ ，satisfy $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ $\mathbf { \widetilde { \mu } } _ { \pmb { { u } } }$ is parallel transported along itself).

Let a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ be given.Let it induce basis vectors $\pmb { e } _ { \alpha } = \partial / \partial x ^ { \alpha }$ into the tangent space at each event. Let the connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ for this “coordinate basis” be given. Then the component version of the “geodesic equation” $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ becomes a differential equation for the geodesic $x ^ { \alpha } ( \lambda )$ ：

$$
\begin{array} { r } { \pmb { \mathscr { u } } = \frac { d } { d \lambda } = \frac { d x ^ { \alpha } } { d \lambda } \frac { \partial } { \partial x ^ { \alpha } } \quad \Longrightarrow } \end{array}
$$

(2） then components of $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ are

$$
\begin{array} { r l } & { 0 = u ^ { \alpha } { } _ { ; \beta } u ^ { \beta } = ( u ^ { \alpha } { } _ { , \beta } + \Gamma ^ { \alpha } { } _ { \gamma \beta } u ^ { \gamma } ) u ^ { \beta } } \\ & { \quad = \frac { \partial } { \partial x ^ { \beta } } \bigg ( \frac { d x ^ { \alpha } } { d \lambda } \bigg ) \frac { d x ^ { \beta } } { d \lambda } + \Gamma ^ { \alpha } { } _ { \gamma \beta } \frac { d x ^ { \gamma } } { d \lambda } \frac { d x ^ { \beta } } { d \lambda } , } \end{array}
$$

which reduces to the differential equation

$$
\frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \alpha } { } _ { \gamma \beta } \frac { d x ^ { \gamma } } { d \lambda } \frac { d x ^ { \beta } } { d \lambda } = 0 .
$$

Component version

This component version of the geodesic equation gives an analytic method ("translation”of Schild's ladder） for constructing the parallel transport law from a knowledge of the geodesics. Pick an event $\mathcal { P } _ { \mathbf { 0 } }$ and set up a coordinate system in its neighborhood. Watch many clock-carrying particles pass through (or arbitrarily close to) $\mathcal { P } _ { \mathbf { 0 } }$ .For each particle read off the values of $d ^ { 2 } x ^ { \alpha } / d \lambda ^ { 2 }$ and $d x ^ { \alpha } / d \lambda$ at $\mathcal { P } _ { \mathbf { 0 } } .$ Insert all the data for many particles into equation (lo.27),and solve for the connectioncoecientsostubdatlyet $T ^ { \alpha } { } _ { \gamma \beta }$ is obtained thereby; the antisymmetric part $T ^ { \alpha } { } _ { [ \gamma \beta ] }$ , vanishes identicallyin any coordinate frame! (See exercise 10.9.) Knowing $T ^ { \alpha } { } _ { \gamma \beta }$ ,use them to paralel transport any desired vector along any desired curve through $\mathcal { P } _ { \mathbf { 0 } }$ ：

How to construct parallel transport law from knowledge of geodesics

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { v } = 0 \quad \iff \quad \frac { d \pmb { v } ^ { \alpha } } { d \lambda } + \pmb { I } ^ { \alpha } \mathstrut _ { \gamma \beta } \pmb { v } ^ { \gamma } \frac { d \pmb { x } ^ { \beta } } { d \lambda } = 0 . } \end{array}
$$

# ExerCise 10.15. COMPONENTS OF PARALLEL-TRANSPORT LAW

EXERCISES

Show that equation (l0.28) is the component version of the law for parallel transporting a vector $\pmb { v }$ along the curve $\mathcal { P } ( \lambda )$ with tangent vector $\pmb { \upsilon } = d \mathcal { P } / d \lambda$

# Exercise 10.16. GEODESICS IN POLAR COORDINATES

In rectangular coordinates on a flat sheet of paper, Euclid's straight lines (geodesics) satisfy $d ^ { 2 } x / d \lambda ^ { 2 } = d ^ { 2 } y / d \lambda ^ { 2 } = 0$ 、Transform this geodesic equation into polar coordinates $( x =$ $r \ \cos \ \phi , \ y = r$ sin $\phi$ )；and read off the resulting connection coefficients by comparison with equation (lO.27). These are the connection coeficients for the coordinate basis $( \hat { \boldsymbol { o } } / \hat { \boldsymbol { o } } \boldsymbol { r } ,$ $\hat { \partial } / \hat { \partial } \phi )$ .From them calculate the connection coefficients for the basis

$$
\pmb { e } _ { \hat { \tau } } = \frac { \hat { \partial } } { \hat { o } r } , \qquad \pmb { e } _ { \hat { \phi } } = \frac { 1 } { r } \frac { \hat { c } } { \hat { \partial } \phi } .
$$

The answer should agree with the answer to part (b) of Exercise l0.l4. Hint: Use such relations as

$$
\Psi _ { e _ { \odot } } e _ { \hat { r } } = \Psi _ { ( 1 / \tau ) ( \hat { \partial } / \hat { \partial } \phi ) } ( \hat { c } / \partial r ) = \frac { 1 } { r } \Psi _ { ( \hat { \partial } / \hat { \partial } \phi ) } ( \hat { o } / \partial r ) .
$$

# Exercise 10.17. ROTATION GROUP:GEODESICS AND CONNECTION COEFFICIENTS

[Continuation of exercises 9.l3 and 9.l4.] In discussing the rotation group,one must make a clear distinction between the Euclidean space (coordinates $x , y , z$ ；basis vectors $\partial / \partial x , \partial / \partial y$ ， $\hat { \sigma } / \hat { \sigma } z )$ in which the rotation matrices act. and the group manifold $S O ( 3 )$ (coordinates $\downarrow , \theta .$ ， $\phi$ ; coordinate basis $\hat { \sigma } / \hat { c } \downarrow , \hat { \sigma } / \hat { \sigma } \theta , \hat { c } / \hat { \sigma } \phi$ ；basis of"generators” $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 } )$ ,whose points $\mathcal { P }$ are rotation matrices.

(a) Pick a vector

$$
\pmb { n } = \pmb { n } ^ { x } \hat { \sigma } / \hat { \sigma } x + \pmb { n } ^ { y } \hat { \sigma } / \hat { \sigma } y + \pmb { n } ^ { z } \hat { \sigma } / \hat { \sigma } z
$$

in Euclidean space. Show that

$$
\begin{array} { r } { \ddot { \mathcal { R } } _ { n } ( t ) \equiv \exp [ ( n ^ { x } ; \ddot { \lambda _ { 1 } } + n ^ { y } ; \ddot { \lambda _ { 2 } } + n ^ { z } ; \ddot { \lambda _ { 3 } } ) t ] } \end{array}
$$

is a rotation matrix that rotates the axes of Euclidean space by an angle

$$
t | n | = t [ ( n ^ { z } ) ^ { 2 } + ( n ^ { y } ) ^ { 2 } + ( n ^ { z } ) ^ { 2 } ] ^ { 1 / 2 }
$$

about the direction $\pmb { n }$ $( \bar { \mathcal { A } } _ { \ j } ^ { - }$ are matrices defined in exercise 9.13.)

(b) In the group manifold $S O ( 3 )$ ，pick a point (rotation matrix) $\mathcal { P }$ ,and pick a tangent vector $\pmb { u } = u ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ at $\mathcal { P }$ Let $\pmb { u }$ be a vector in Euclidean space with the same components as $\pmb { u }$ has in $S O ( 3 )$ ：

$$
{ \pmb u } = u ^ { 1 } { \pmb e } _ { 1 } + u ^ { 2 } { \pmb e } _ { 2 } + u ^ { 3 } { \pmb e } _ { 3 } ; \qquad { \pmb u } = u ^ { 1 } \hat { v } / \hat { v } x + u ^ { 2 } \hat { v } / \hat { v } y + u ^ { 3 } \hat { v } / \hat { v } z .
$$

Show that $\pmb { u }$ is the tangent vector (at $t = 0$ ）to the curve

$$
\mathcal { C } ( t ) = \mathcal { R } _ { \boldsymbol { u } } ( t ) \mathcal { P } .
$$

The curve $\mathcal { C } ( t )$ through the arbitrary point $\mathcal { P }$ with arbitrary tangent vector $\pmb { u } = ( d \mathcal { C } / d t ) _ { t = 0 }$ is a very special curve:every point on it differs from $\mathcal { P }$ by a rotation $\boldsymbol { \mathcal { R } } _ { \boldsymbol { \mu } } ( t )$ about one and the same direction $\pmb { u }$ No other curve in $S O ( 3 )$ with “starting conditions” $\{ \mathcal { P } , \pmb { u } \}$ has such beautiful simplicity.Hence it is natural to decree that each such $\mathcal { C } ( t )$ is a geodesic of the group manifold $S O ( 3 )$ 、This decree adds new geometric structure to $S O ( 3 )$ ; it converts $S O ( 3 )$ from a differentiable manifold into something more special: an affine manifold.

One has no guarantee that an arbitrarily chosen family of curves in an arbitrary manifold can be decreed to be geodesics.Most families of curves simply do not possess the right geometric properties to function as geodesics. Most will lead to covariant derivatives that violate one or more of the fundamental conditions (l0.2). To learn whether a given choice of geodesics is possible, one can try to derive connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ (for some given basis)corresponding to the chosen geodesics.If the derivation is successful, the choice of geodesics was a possble one. If the derivation produces inconsistencies,the chosen family of curves have the wrong geometric properties to function as geodesics.

(c) For the basis of generators $\{ \pmb { e } _ { \alpha } \}$ derive connection coefficients corresponding to the chosen geodesics, $\mathcal { C } ( t ) = \mathcal { R } _ { u } ( t ) \mathfrak { s } \bar { \mathcal { P } } ,$ of $S O ( 3 )$ . Hint: show that the components $u ^ { \alpha } = \langle { \pmb { \omega } } ^ { a } , { \pmb { \omega } } \rangle$ of the tangent $\pmb { \mu } = d \mathcal { E } / d t$ to a given geodesic are independent of position $\mathcal { C } ( t )$ along the geodesic. Then use the geodesic equation $\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0$ ,expanded in the basis $\{ e _ { \alpha } \}$ , to calculate the symmetric part of the connection $T ^ { \alpha } { } _ { ( \beta \gamma ) }$ Finally use equation(10.23)tocalculate $\Gamma ^ { \alpha } { } _ { [ \beta \gamma ] }$ [Answer:

$$
T ^ { \alpha } { } _ { \beta \gamma } = \frac { 1 } { 2 } \epsilon _ { \alpha \beta \gamma } ,
$$

where $\epsilon _ { \alpha \beta \gamma }$ is the completely antisymmetric symbol with $\epsilon _ { 1 2 3 } = + 1$ This answer is independent of location $\mathcal { P }$ in $S O ( 3 ) ! ]$
