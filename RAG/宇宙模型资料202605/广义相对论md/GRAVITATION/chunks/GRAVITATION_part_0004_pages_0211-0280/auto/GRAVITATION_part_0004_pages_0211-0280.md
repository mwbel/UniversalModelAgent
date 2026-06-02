Box 7.1 (continued)

From the absence of explicit $t \cdot , \phi \cdot ,$ and $\pmb { \tau }$ -dependence in $L$ ,infer three constants of motion: the canonical momenta

$$
P _ { t } \equiv - m \gamma = \partial L / \partial i
$$

(this defines Y） and

$$
P _ { \phi } \equiv m \alpha = \partial L / \partial \dot { \phi }
$$

(this defines $\pmb { \alpha }$ )；and the Hamiltonian

$$
H = \dot { x } ^ { \mu } ( \partial L / \partial \dot { x } ^ { \mu } ) - L ,
$$

which can be set equal to $- { \frac { 1 } { 2 } } m$ by appropriate normalization of the path parameter $\tau .$ .From these constants of the motion, derive an orbit equation as follows: (l) calculate $H = - \frac { 1 } { 2 } m$ in terms of $r , \dot { r } , \dot { \phi } .$ and $i _ { \downarrow }$ (2)eliminate $i$ and $\dot { \phi }$ in favor of the constants $\boldsymbol { \mathsf { \tt T } }$ and $\pmb { \alpha }$ ；(3)as in Newtonian orbit problems, define $u = M / r$ and write

$$
\frac { d u } { d \phi } = \frac { \dot { u } } { \dot { \phi } } = - \frac { M \dot { r } } { r ^ { 2 } \dot { \phi } } = - \frac { M } { \alpha } ( 1 + 2 u ) \dot { r } ;
$$

(4)in $H _ { : }$ eliminate $\dot { r }$ in favor of $d u / d \phi$ via the above equation,and eliminate $r$ in favor of $\pmb { u }$ ；(5) solve for $d u / d \phi$ . The result is

$$
\left( { \frac { d u } { d \phi } } \right) ^ { 2 } + u ^ { 2 } = ( \gamma ^ { 2 } - 1 + 2 u ) { \frac { M ^ { 2 } } { \alpha ^ { 2 } } } \biggl [ { \frac { 1 + 2 u } { 1 - 2 u } } \biggr ] .
$$

Neglecting cubic and higher powers of $u = G M / c ^ { 2 } r \sim ( 1 - \gamma ^ { 2 } )$ in this equation, derive the perihelion shift. (For details of method, see exercise 40.4,with the $\boldsymbol { \gamma }$ and $\pmb { \alpha }$ of this box renamed $\widetilde { E }$ and $\widetilde { L }$ and with the $\boldsymbol { \gamma }$ and $\beta$ of that exercise set equal to l and O.) The resulting shift per orbit is

$$
\begin{array} { r } { \Delta \phi = 8 \pi M / r _ { 0 } + O ( [ M / r _ { 0 } ] ^ { 2 } ) . } \end{array}
$$

This is $\textstyle { \frac { 4 } { 3 } }$ the prediction of general relativity; and it disagrees with the observations On Mercury (see Box 40.3).

# E.Bending of Light (exercise 7.3E)

The deflection angle for light passing the sun is, on dimensional grounds,a smal quantity, $\begin{array} { r } { \varDelta \phi \sim M _ { \odot } / R _ { \odot } \sim 1 0 ^ { - 6 } . } \end{array}$ ； from the outset, one makes approximations based On this smallness. A diagram of the photon trajectory, set in the $x , z \cdot$ plane, shows that, for initial motion parallel to the $z \cdot$ -axis, the deflection angle can be expressed in terms of the final momentum as $\varDelta \phi = p _ { z } / p _ { z }$ .Compute the final $\pmb { p _ { x } }$ by an integral along the trajectory,

$$
p _ { x } = \int _ { - \infty } ^ { + \infty } ( d p _ { x } / d z ) d z ,
$$

![](images/8b0e11cdfccab66a5aec2dc79d9ccda3cd8d2c46eae6df5c39f298f20b75282a.jpg)

treating $\pmb { p _ { z } }$ as essentially constant. This computation requires generalization of the equation of motion (2) to the case of zero rest mass.To handle the limit $m \longrightarrow 0$ ， introduce a new parameter $\lambda = \tau / m$ ；then $p ^ { \mu } = m ( d z ^ { \mu } / d \tau ) = d z ^ { \mu } / d \lambda$ Also define $p _ { \mu } = ( \eta _ { \mu \nu } + h _ { \mu \nu } ) p ^ { \nu }$ , since this quantity appears simply in equation (2) and agrees with $p _ { \mu }$ in the limit $r \longrightarrow \infty$ , where one will need to evaluate it. Then equation (2) reads, for any $m$ ,including $m = 0$ ，

$$
\frac { d P _ { \mu } } { d \lambda } = \frac { 1 } { 2 } h _ { \alpha \beta , \mu } p ^ { \alpha } p ^ { \beta } .
$$

On the righthand side here, since $h _ { \alpha \beta , \mu }$ is small, a crude approximation to $p ^ { \mu }$ suffices; $p ^ { 1 } = p ^ { 2 } = 0 , p ^ { 0 } = p ^ { 3 } = d z / d \lambda = \stackrel { \cdot } { \omega } =$ constant. Thus,

$$
\frac { d P _ { 1 } } { d \lambda } = \frac { 1 } { 2 } ( h _ { 0 0 } + 2 h _ { 0 3 } + h _ { 3 3 } ) _ { , 1 } \omega ^ { 2 }
$$

and

$$
\quad \frac { 1 } { p _ { 3 } } \frac { d P _ { 1 } } { d z } = \frac { 1 } { 2 } ( h _ { 0 0 } + 2 h _ { 0 3 } + h _ { 3 3 } ) _ { , 1 } .
$$

For the sun, $h _ { 0 0 } = h _ { 3 3 } = 2 M / r$ ,and $h _ { 0 3 } = 0$ (equation 8), so

$$
A \phi = - \left( { \frac { p _ { 1 } } { p _ { 3 } } } \right) _ { \mathrm { f i n a l } } = - \left( { \frac { P _ { 1 } } { p _ { 3 } } } \right) _ { \mathrm { f i n a l } } = \int _ { - \infty } ^ { \infty } { \frac { 2 M t d z } { ( \lambda ^ { 2 } + z ^ { 2 } ) ^ { 3 / 2 } } } { \stackrel { . . . } { = } } { \frac { 2 M } { \lambda } } \int _ { - \infty } ^ { \infty } { \frac { d \xi } { ( 1 + \xi ^ { 2 } ) ^ { 3 / 2 } } } = { \frac { 4 M } { t } } .
$$

For light grazing the sun, $\ell = R _ { \odot } ,$ this gives $\pmb { \mathcal { \Delta } } \phi = 4 M _ { \odot } / R _ { \odot }$ radians $= 1 ^ { \prime \prime } . 7 5$ ,which is also the prediction of general relativity,and is consistent with the observations (see Box 40.1).

# F. Gravitational Waves (exercise 7.3F)

The field equations (4) and gauge properties (5) of the present flat-spacetime theory are identical to those of Einstein's “linearized theory.”Thus,the treatment of gravitational waves using linearized theory,which is presented in $\ S \ S 1 8 . 2 , 3 5 . 3$ ,and 35.4, applies here.

# G. Positive Energy of the Waves (exercise 7.3G)

Computing a general formula for $\mathcal { H }$ from equation (7.17)is tedious, but it is sufficient to consider only the special case of a plane wave (equation 7.l3)-or better still,

a plane wave with only $h _ { 1 2 } = h _ { 2 1 } = f ( z - t )$ . Any gravitational wave can be constructed as a superposition of such plane waves. First compute the Langrangian for this case. According to equation (7.8), it reads

$$
\mathcal { L } _ { f } = ( 3 2 \pi ) ^ { - 1 } [ ( h _ { 1 2 , 0 } ) ^ { 2 } - ( h _ { 1 2 , 3 } ) ^ { 2 } ] .
$$

Now the full content of the formula (7.l7) defining $\mathcal { H }$ is precisely the following: start from the Lagrangian; keep all terms that are quadratic in time derivatives; omit all terms that are linear in time derivatives; and reverse the sign of terms that contain no time derivatives.The result is

$$
\mathcal { K } = ( 3 2 \pi ) ^ { - 1 } [ ( h _ { 1 2 , 0 } ) ^ { 2 } + ( h _ { 1 2 , 3 } ) ^ { 2 } ] ,
$$

which is positive.

# H. Self-Inconsistency of the Theory (exercise 7.3H)

From equation (7.10), find

$$
T ^ { \mu \nu } { } _ { , \nu } = m \int { \frac { d z ^ { \mu } } { d \tau } } { \frac { d z ^ { \nu } } { d \tau } } { \frac { \hat { \nabla } } { \hat { \partial } x ^ { \nu } } } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] d \tau .
$$

But $\delta ^ { 4 } ( { \pmb x } - { \pmb z } )$ depends only on the difference $x ^ { \mu } - z ^ { \mu }$ ， ${ \bf s } 0 - \partial / \partial z ^ { \nu }$ can replace $\hat { \boldsymbol { d } } / \hat { \boldsymbol { d } } \boldsymbol { x } ^ { \nu }$ when acting on the $\delta$ -function. Noting that

$$
\frac { d z ^ { \nu } } { d \tau } \frac { \partial } { \partial z ^ { \nu } } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] = \frac { d } { d \tau } \delta ^ { 4 } [ { \pmb x } - { \pmb z } ( \tau ) ] ,
$$

rewrite $T ^ { \mu \nu } { } _ { , \nu }$ as

$$
\dot { T } ^ { \mu \nu } { } _ { , \nu } = - m \int \dot { z } ^ { \mu } ( d / d \tau ) \delta ^ { 4 } [ x - z ( \tau ) ] d \tau = + m \int \ddot { z } ^ { \mu } \delta ^ { 4 } [ x - z ( \tau ) ] d \tau .
$$

(The last step is obtained by an integration by parts.) Thus $T ^ { \mu \nu } { } _ { , \nu } = 0$ holds if and only if $\tilde { z } ^ { \mu } = 0$ . But $\tilde { z } ^ { \mu } = 0$ means that the gravitational fields have no effect on the motion of the particle. But this contradicts the equation of motion (2), which follows from the theory's variational principle. Thus, this tensor theory of gravity is inconsistent. [Stated briefly,equation (4) requires $T ^ { \mu \nu } { } _ { , \nu } = 0$ ,while equation (2) excludes it.]

The fact that, in this theory,gravitating bodies cannot be affected by gravity,also holds for bodies made of arbitrary stress-energy (e.g., rubber balls or the Earth). Since all bodies gravitate, since the field equations imply $T ^ { \mu \nu } { } _ { , \nu } = 0$ , and since this “equation of motion for stress-energy” implies conservation of a body's total 4-momentum $P ^ { \mu } = \mathcal { J } T ^ { \mu 0 } d ^ { 3 } x$ ，no body can be accelerated by gravity. The Earth cannot be attracted by the sun; it must fly off into interstellar space!

Straightforward steps to repair this inconsistency in the theory lead inexorably to general relativity (see Box l7.2 part 5). Having adopted general relativity as the theory of gravity, one can then use the present flat-spacetime theory as an approximation to it (“Linearized general relativity"; treated in Chapters 18,l9,and 35; see especially discussion at end of $\ S 1 8 . 3 \AA$ 0.

# $\ S 7 . 2$ . GRAVITATIONAL RED SHIFT DERIVED FROM ENERGY CONSERVATION

Einstein argued against the existence of any ideal,straight-line reference system such as is assumed in Newtonian theory.He emphasized that nothing in a natural state of motion, not even a photon, could ever give evidence for the existence or location of such ideal straight lines.

That a photon must be affected by a gravitational field Einstein (l9ll) showed from the law of conservation of energy,applied in the context of Newtonian gravitation theory. Let a particle of rest mass m start from rest in a gravitational field $g$ at point $\mathcal { Q }$ and fall freely for a distance $h$ to point $\mathcal { B }$ . It gains kinetic energy mgh. Its total energy,including rest mass, becomes

Gravitational redshift derived from energy considerations

$$
m + m g h .
$$

Now let the particle undergo an annihilation at $\mathcal { B }$ ，converting its total rest mass plus kinetic energy into a photon of the same total energy. Let this photon travel upward in the gravitational field to $\mathcal { Q }$ . If it does not interact with gravity, it will have its original energy on arrival at $\boldsymbol { \mathcal { Q } }$ .At this point it could be converted by a suitable apparatus into another particle of rest mass m (which could then repeat the whole process) plus an excess energy mgh that costs nothing to produce.To avoid this contradiction of the principal of conservation of energy,which can also be stated in purely classical terms,Einstein saw that the photon must suffer a red shift. The energy of the photon must decrease just as that of a particle does when it climbs out of the gravitational field. The photon energy at the top and the bottom of its path through the gravitational feld must therefore be related by

$$
E _ { \mathrm { b o t t o m } } = E _ { \mathrm { t o p } } ( 1 ~ + ~ g h ) = E _ { \mathrm { t o p } } ( 1 ~ + ~ g _ { \mathrm { c o n v } } h / c ^ { 2 } ) .
$$

The drop in energy because of work done against gravitation implies a drop in frequency and an increase in wavelength (red shift; traditionally stated in terms of a red shift parameter, $z = \varDelta \lambda / \lambda$ )； thus,

$$
1 + z = \frac { \lambda _ { \mathrm { t o p } } } { \lambda _ { \mathrm { b o t t o m } } } = \frac { h \nu _ { \mathrm { b o t t o m } } } { h \nu _ { \mathrm { t o p } } } = \frac { E _ { \mathrm { b o t t o m } } } { E _ { \mathrm { t o p } } } = 1 + g h .
$$

The redshift predicted by this formula has been verified to l percent by Pound and Snider (l964,l965),refining an experiment by Pound and Rebka (1960).

# $\$ 7.3$ .GRAVITATIONAL REDSHIFT IMPLIES SPACETIME IS CURVED

An argument by Schild (1960,1962,1967） yields an important conclusion: the existence of the gravitational redshift shows that a consistent theory ofgravity cannot be constructed within the framework of special relativity.

![](images/6f2ac1ad29d7ec4d267dd7540ae4c921cf9e1f37085b92426e37e2001d6a56b9.jpg)  
Figure 7.1. Successive pulses of light rising from height $z _ { 1 }$ to height $z _ { 2 } = z _ { 1 } + h$ against the gravitational feld of the earth.The paths $\gamma _ { 1 }$ ,and $\gamma _ { 2 }$ must be exactly congruent, whether sloped at $4 5 ^ { \circ }$ (left)or having variable slope (right).

Assume gravity is described by an (unspecified) field in flat spacetime..

Whereas Einstein's argument (last section) was formulated in Newtonian theory, Schild's is formulated in special relativity.It analyzes gravitational redshift experiments in the field of the Earth,using a global Lorentz frame tied to the Earth's center.It makes no demand that free particles initially at rest remain at rest in this global Lorentz frame (except far from the Earth,where gravity is negligible). On the contrary,it demands that free particles be accelerated relative to the Lorentz frame by the Earth's gravitational field.It is indifferent to the mathematical nature of that field (scalar, vector,tensor,...),but it does insist that the gravitational accelerations agree with experiment. And, of course, it demands that proper lengths and times be governed by the metric of special relativity.

Schild's argument proceeds as follows.Consider one observer at rest on the Earth's surface at height $z _ { 1 } ,$ ,and a second above the Earth's surface at height $z _ { 2 } = z _ { 1 } + h$ (Figure 7.1). The observers may verify that they are at rest relative to each other and relative to the Earth's Lorentz frame by,for instance,radar ranging to free particles that are at rest in the Earth's frame far outside its gravitational field.The bottom experimenter then emits an electromagnetic signal of a fixed standard frequency $\omega _ { b }$ which is received by the observer on top.For definiteness,let the signal be a pulse exactly $N$ cycles long. Then the interval of time\* $\delta \tau _ { \mathsf { b o t } }$ required for the emission of the pulse is given by $2 \pi N = \omega _ { b } \delta \tau _ { \mathrm { b o t } } .$ The observer at the top is then to receive these same $N$ cycles of the electromagnetic wave pulse and measure the time interval\* $\delta \tau _ { \mathsf { t o p } }$ required. By the definition of “frequency,” it satisfies $2 \pi N =$ $\omega _ { t } \delta \tau _ { \mathsf { t o p } }$ .The redshift effect, established by experiment (for us) or by energy conservation (for Einstein), shows $\omega _ { t } < \omega _ { b }$ ； consequently the time intervals are different, $\delta \tau _ { \mathrm { t o p } } > \delta \tau _ { \mathrm { b o t } } .$ Transfer this information to the special-relativity spacetime diagram of the experiment (Figure 7.l). The waves are light rays; so one might show them as traveling along $4 5 ^ { \circ }$ null lines in the spacetime diagram (Figure 7.1,A). In this simplified but slightly inadequate form of the argument,one reaches a contradiction by noticing that here one has drawn a parallelogram in Minkowski spacetime in which two of the sides are unequal, $\tau _ { \mathrm { { t o p } } } > \tau _ { \mathrm { { b o t } } }$ ，whereas a parallelogram in flat Minkowski spacetime cannot have opposite sides unequal. One concludes that special relativity cannot be valid over any sufficiently extended region. Globally,spacetime, as probed by the tracks of light rays and test particles, departs from flatness("curvature"; Parts III and IV of this book),despite the fine fit that Lorentz-Minkowski flatness gives to physics locally.

Figure 7.1,B, repairs an oversimplification in this argument by recognizing that the propagation of light will be influenced by the gravitational field. Therefore photons might not follow straight lines in the diagram. Consequently,the world lines $\gamma _ { 1 }$ and $\gamma _ { 2 }$ of successive pulses are curves.However, the gravitational field is static and the experimenters do not move. Therefore nothing in the experimental setup changes with time. Whatever the path $\gamma _ { 1 }$ ，the path $\gamma _ { 2 }$ must be a congruent path of exactly the same shape,merely translated in time.On the basis of this congruence and the fact that the observers are moving on parallel world lines, one would again conclude,if flat Minkowski geometry were valid, that $\tau _ { \mathrm { b o t } } = \tau _ { \mathrm { t o p } } ,$ ， thus contradicting the observed redshift experiment. The experimenters do not need to understand the propagation of light in a gravitational field.They need only use their radar apparatus to verify the fact that they are at rest relative to each other and relative to the source of the gravitational field. They know that, whatever influence the gravitational feld has on their radar apparatus,it will not be a time-dependent influence. Moreover, they do not have to know how to compute their separation in order to verify that the separation remains constant. They only need to verify that the round-trip time required for radar pulses to go out to each other and back is the same every time they measure it.

Schild's redshift argument does not reveal what kind of curvature must exist, or whether the curvature exists in the neighborhood of the observational equipment or Some distance away from it. It does say, however, quite unambigously, that the flat spacetime of special relativity is inadequate to describe the_situation,and it should therefore motivate one to undertake the mathematical analysis of curvature in Part III.

This assumption is incompatible with gravitational redshift

Conclusion:spacetime is curved

# $\ S 7 . 4$ .GRAVITATIONAL REDSHIFT AS EVIDENCE FOR THE PRINCIPLE OF EQUIVALENCE

Einstein (l9o8,1911) elevated the idea of the universality of gravitational interactions to the status of a fundamental principle of equivalence, that all effects of a uniform gravitational field are identical to the effects of a uniform acceleration of the coordinate system.This principle generalized a result of Newtonian gravitation theory,in which a uniform acceleration of the coordinate system in equation (7.l） gives rises to a

Principle of equivalence:a uniform gravitational field is indistinguishable from a uniform acceleration of a reference frame

supplementary uniform gravitational field. However, the Newtonian theory only gives this result for particle mechanics.Einstein's principle of equivalence asserts that a similar correspondence willhold for all the laws of physics, including Maxwell's equations for the electromagnetic feld.

The rules of the game--the“scientific method"-require that experimental support be sought for any new theory or principle,and Einstein could treat the gravitational redshift as the equivalent of experimental confirmation of his principle of equivalence.There are two steps in such a confirmation: first, the theory or principle must predict an effect (the next paragraph describes how the equivalence principle implies the redshift); second, the predicted effect must be observed.With the Pound-Rebka-Snider experiments,one is in much better shape today than Einstein was for this second step. Einstein himself had to rely on the experiments supporting the general Concept of energy conservation, plus the necesity of aredshift to preserve energy conservation,as a substitute for direct experimental confirmation.

Gravitational redshift derived from equivalence principle

The existence of the gravitational redshift can be deduced from the equivalence principle by considering two experimenters in a rocket ship that maintains a constant acceleration $g$ .Let the distance between the two observers be $h$ in the direction of the acceleration. Suppose for definiteness that the rocket ship was at rest in some inertial coordinate system when the bottom observer sent off a photon. It will require time $t = h$ for the photon to reach the upper observer.In that time the top observer acquires a velocity $v = g t = g h$ .He will therefore detect the photon and observe a Doppler redshift $z = v = g h$ . The results here are therefore identical to equation (7.20).The principle of equivalence of course requires that,if this redshift is observed in an experiment performed under conditions of uniform acceleration in the absence of gravitational fields, then the same redshift must be observed by an experiment performed under conditions where there is a uniform gravitational field, but no acceleration. Consequently,by the principle of equivalence, one can derive equation (7.20)as applied to the gravitational situation.

# $\$ 7.5$ ． LOCAL FLATNESS，GLOBAL CURVATURE

The equivalence principle helps one to discern the nature of the spacetime curvature, whose existence was inferred from Schild's argument.Physics is the same in an accelerated frame as it is in a laboratory tied to the Earth's surface. Thus,an Earth-bound lab can be regarded as accelerating upward, with acceleration $g$ relative to the Lorentz frames in its neighborhood.\* Equivalently,relative to the lab and the Earth's surface, all Lorentz frames must accelerate downward.But the downward (radial) direction is different at different latitudes and longitudes.Hence,local Lorentz frames,initially at rest with respect to each other but on opposite sides of the Earth, subsequently fall toward the center and go flying through each other. Clearly they cannot be meshed to form the single global Lorentz frame, tied to the

Earth, that was assumed in Schild's argument. This nonmeshing of local Lorentz frames, like the nonmeshing of local Cartesian coordinates on a curved 2-surface, is a clear manifestation of spacetime curvature.

Geographers have similar problems when mapping the surface of the earth. Over small areas,a township or a county,it is easy to use a standard rectangular coordinate system. However, when two fairly large regions are mapped,each with one coordinate axis pointing north, then one finds that the edges of the maps overlap each other best if placed at a slight angle (spacetime analog: relative velocity of two local Lorentz frames meeting at center of Earth). It is much easier to start from a picture of a spherical globe,and then talk about how small flat maps might be used as good approximations to parts of it, than to start with a huge collection of small maps and try to piece them together to build up a picture of the globe. The exposition of the geometry of spacetime in this book will therefore take the first approach. Now that one recognizes that the problem is to fit together local, flat spacetime descriptions of physics into an over-all view of the universe,one should be happy to jump,in the next chapter, into a broadscale study of geometry.From this more advantageous viewpoint,one can then face the problem of discussng the relationship between the local inertial coordinate systems appropriate to two nearby regions that have slightly different gravitational fields.

# Nonmeshing of local Lorentz frames motivates study of geometry

Two types of geometry relevant to spacetime:

There are actually two distinguishable ways in which geometry enters the theory of general relativity. One is the geometry of lengths and angles in four-dimensional spacetime,which is inherited from the metric structure $d s ^ { 2 }$ of special relativity. Schild's argument already shows (without a direct appeal to the equivalence principle) that the special-relativistic ideas of length and angle must be modified. The modified ideas of metric structure lead to Riemannian geometry,which will be treated in Chapters 8 and l3. However, geometry also enters general relativity because of the equivalence principle.An equivalence principle can already be stated within Newtonian gravitational theory,in which no concepts of a spacetime metric enter,but only the Euclidean metric structure of three-dimensional space. The equivalence-principle view of Newtonian theory again insists that the local standard of reference be the freely falling particles. This requirement leads to the study of a spacetime geometry in which the curved world lines of freely falling particles are defined to be locally straight. They play the role in a curved spacetime geometry that straight lines play in flat spacetime. This “affine geometry” will be studied in Chapters lO--12. It leads to a quantitative formulation of the ideas of“covariant derivative” and “curvature” and even “curvature of Newtonian spacetime"!

Riemannian geometry (lengths and angles)

Affine geometry （"'straight lines"and curvature)

# PART 三

# THE MATHEMATICS OF CURVED SPACETIME

Wherein the reader is exposed to the charms of a new temptress-Modern Differential Geometry-and makes a decision: to embrace her for eight full chapters:or, having drunk his fill, to escape after one.

# CHAPTER 8

# DIFFERENTIAL GEOMETRY: AN OVERVIEW

lam coming more and more to the conviction that the necessity   
of our geometry cannot be demonstrated,at least neither by.nor for,the human intellect....geometry should be ranked,not with arithmetic,which is purelyaprioristic,butwith mechanics. (1817)

We must confess in all humility that,while number is a product ofour mind alone,space has a reality beyond the mind whose rules we cannot completely prescribe.(1830)

CARL FRIEDRICH GAUSS

# S8.1. AN OVERVIEW OF PART III

Gravitation is a manifestation of spacetime curvature, and that curvature shows up in the deviation of one geodesic from a nearby geodesic ("relative acceleration of test particles").The central issue of this part of the book is clear: How can one quantify the“separation,"and the“rate ofchange”of"separation,”oftwo“geodesics” in “curved” spacetime? A clear, precise answer requires new concepts.

Concepts to be developed in Part III:

"Separation” between geodesics will mean “vector.” But the concept of vector as employed in flat Lorentz spacetime (a bilocal object: point for head and point for tail) must be sharpened up into the local concept of tangent vector, when one passes to curved spacetime. Chapter 9 does the sharpening. It also reveals how the passage to curved spacetime affects l-forms and' tensors.

It takes one tool (vectors in curved geometry, Chapter 9) to define “separation" clearly as a vector; it takes another tool (parallel transport in curved spacetime, Chapter lO) to compare separation vectors at neighboring points and to define the “rate of change of separation.” No transport, no comparison; no comparison, no meaning to the term “rate of change"! The notion of parallel transport founds itself

Tangent vector

# Geodesic

Covariant derivative

on the idea of“geodesic,” the world line of a freely falling particle. The special mathematical properties of a geodesic are explored in Chapter l0. That chapter uses geodesics to define parallel transport, uses parallel transport to define covariant derivative, and-completing the circle-uses covariant derivative to describe geodesics.

Geodesic deviation

Chapter ll faces up to the central issue: geodesic deviation ("rate of change of separation vector between two geodesics"),and its use in defining the curvature of spacetime.

Spacetime curvature

But to define curvature is not enough. The man who would understand gravity deeply must also see curvature at work, producing relative accelerations of particles in_ Newtonian spacetime (Chapter l2); he must learn how,in Einstein spacetime, distances (metric) determine completely the curvature and the law of parallel trans-port (Chapter l3); he must be the master of powerful tools for computing curvature (Chapter l4); and he must grasp the geometric significance of the algebraic and differential symmetries of curvature (Chapter 15).

# This chapter:a Track-1 overview of differential geometry

Unfortunately, such deep understanding requires time-far more time than one can afford in a ten-week or fteen-week course,far more than a lone reader may wish to spend on first passage through the book. For the man who must rush on rapidly,this chapter contains a “Track-1” overview of the essential mathematical tools $( \ S \ S 8 . 4 \ – 8 . 7 )$ . From it one can gain an adequate,but not deep,understanding of spacetime curvature, of tidal gravitational forces,and of the mathematics of curved spacetime.This overview is also intended for the Track-2 reader; it will give him a taste of what is to come.The ambitious reader may also wish to consult other introductions to differential geometry (see Box 8.1).

# Box 8.1 BOOKS ON DIFFERENTIAL GEOMETRY

There are several mathematics texts that may be consulted for a more detailed and extensive discussion of modern differential geometry along the line taken here. Bishop and Goldberg (l968) is the no.l reference.Hicks (l965) could be chosen as a current standard graduate-level text, with O'Neill (1966） at the undergraduate level introducing many of the same topics without presuming that the reader finds easy and obvious the current style in which pure mathematicians think and write.Auslander and MacKenzie (l963）at a somewhat more advanced level also allow for the reader to whom differential equations are more familiar than homomorphisms.Willmore (l959) is easy to read but presents no challenge,and leads to little progress in adapting to the style of current mathematics.Trautman (l965) and Misner (1964a, 1969a) are introductions somewhat similar to ours, except for deemphasis of pictures; like ours, they are aimed at the student of relativity. Flanders (1963） is easy and useful as an introduction to exterior differential forms;it also gives examples of their application to a wide variety of topics in physics and engineering.

# $\$ 8.2$ .TRACK 1 VERSUS TRACK 2: DIFFERENCE IN OUTLOOK AND POWER

Nothing is more wonderful about the relation between Einstein's theory of gravity and Newton's theory than this,as discovered by Elie Cartan (l923,1924): that both theories lend themselves to description in terms of curvature; that in both this curvature is governed by the density of mass-energy; and that this curvature allows itself to be defined and measured without any use of or reference to any concept of metric. The difference between the two theories shows itself up in this: Einstein's theory in the end (or in the beginning,depending upon how one presents it!) does define an interval between every event and every nearby event; Newton's theory not only does not, but even says that any attempt to talk of spacetime intervals violates Newton's laws. This being the case, Track 2 will forego for a time (Chapters 9-12) any use of a spacetime metric ("Einstein interval"). It will extract everything possible from a metric-free description of spacetime curvature (all of Newton's theory; important parts of Einstein's theory).

Geodesic deviation is a measurer and definer of curvature,but the onlooker is forbidden to reduce a vector description of separation to a numerical measure of distance (no metric at this stage of the analysis): what an impossible situation! Nevertheless,that is exactly the situation with which Chapters 9-12 will concern themselves: how to do geometry without a metric. Speaking physically, one will overlook at this stage the fact that the geometry of the physical world is always and everywhere locally Lorentz, and endowed with a light cone, but one will exploit to the fullest the Galileo-Einstein principle of equivalence: in any given locality one can find a frame of reference in which every neutral test particle, whatever its velocity, is free of acceleration. The tracks of these neutral test particles define the geodesics of the geometry. These geodesics provide tools with which one can do much: define parallel transport (Chapter lO),define covariant derivative (Chapter 10),quantify geodesic deviation (Chapter ll), define spacetime curvature (Chapter 11),and explore Newtonian gravity (Chapter l2). Only after this full exploitation of metric-free geodesics will Track 2 admit the Einstein metric back into the scene (Chapters 13-15).

But to forego use of the metric is a luxury which Track 1 can ill afford; too little time would be left for relativistic stars, cosmology, black holes, gravitational waves, experimental tests,and the dynamics of geometry. Therefore,the Track-1l overview in this chapter keeps the Einstein metric throughout. But in doing so,it pays a heavy price: (l) no possibility of seeing curvature at work in Newtonian spacetime (Chapter 12); (2) no possibility of comparing and contrasting the geometric structures of Newtonian spacetime (Chapter l2) and Einstein spacetime (Chapter l3),and hence no possibility of grasping fully the Newtonian-based motivation for the Einstein field equations (Chapter 17); (3) no possibility of understanding fully the mathematical interrelationships of “geodesic,”“parallel transport,” "covariant derivative,”“curvature,”and “metric”(Chapters 9,10,11,13); (4) no possibility of introducing the mathematical subjects “differential topology"(geometry without metric or covariant

Preview of Track-2 differential geometry

What the Track-1 reader will miss

derivative, Chapter 9) and “affne geometry”(geometry with covariant derivative but no metric, Chapters l0 and 11),subjects which find major application in modern analytical mechanics [see, e.g., Arnold and Avez (l968)； also exercise 4.ll of this book],in Lie group theory with its deep implications for elementary particle physics [see,e.g., Hermann (1966); also exercises 9.12, 9.13,10.16,and 11.12 of this book], in the theory and solution of partial differential equations [see,e.g., Sternberg(l969)], and,of course, in gravitation theory.

# $\$ 8.3$ . THREE ASPECTS OF GEOMETRY: PICTORIAL，ABSTRACT，COMPONENT

Gain the power in $\ S 8 . 4$ and Chapter 9 to discuss tangent vectors,l-forms, tensors in curved spacetime; gain the power in $\ S 8 . 5$ and Chapter l0 to parallel-transport vectors,to differentiate them,to discuss geodesics; use this power in $\ S 8 . 7$ and Chapter 1l to discuss geodesic deviation, to define curvature; .... But full power this will be only if it can be exercised in three ways:in pictures,in abstract notation,and in component notation (Box 8.3). Elie Cartan $( \mathbf { B o x 8 . 2 } ) ,$ gave new insight into both

![](images/5590f1d72c1e39219c35c50382256f6dabe7fe26dca7ec31952a9a2842c7064d.jpg)  
Box 8.2 ELIE CARTAN,1869-1951

Elie Cartan is a most remarkable figure in recent mathematical history. One learns from his obituary [Chern and Chevalley (l952)] that he was born a blacksmith's son in southern France,and proved the value of government scholarship aid by rising through the system to a professorship at the Sorbonne in l912 when he was 43. At the age of 32 he invented the exterior derivative [Cartan (1901), which he used then mostly in differential equations and the theory of Lie groups,where he had already made significant contributions. He was about fifty when he began applying it to geometry, and sixty before Riemannian geometry specifically was the object of this research,including his text [Cartan (l928)], which is still reprinted and worth studying. Although universally recognized,his work did not find responsive readers until he neared retiremcnt around 1940,when the “Bourbaki” generation of French mathematicians began to provide a conceptual framework for (among other things) Cartan's insights and methods.This made Cartan communicable and teachable as his own writings never were,so that by the time of his death at 82 in 1951 his infuence was obviously dominating the revolutions then in full swing in all the fields (Lie groups, differential equations, and differential geometry) in which he had primarily worked.

The modern,abstract,coordinate-free approach to geometry,which is used extensively in this book, is due largely to Elie Cartan.He also discovered the geometric approach to Newtonian gravity that is developed and exploited in Chapter 12.

# Box 8.3 THREE LEVELS OF DIFFERENTIAL GEOMETRY

(l） Purely pictorial treatment of geometry: tangent vector is conceived in terms of the separation of two points in the limit in which the points are indefinitely close; vectors are added and subtracted locally as in flat space; vectors at distinct points are compared by parallel transport from one point to another; this_parallel transport is accomplished by_a “Schild's ladder construction”of geodesics (Box 10.2); diagrams,yes;algebra, no; it is tied conceptually as closely as possible to the world of test particles and measurements.   
(2) Abstract differential geometry: treats a tangent vector as existing in its own right,without necessity to give its breakdown into components, $\pmb { A } = A ^ { 0 } \pmb { e } _ { 0 } + A ^ { 1 } \pmb { e } _ { 1 } + A ^ { 2 } \pmb { e } _ { 2 } + A ^ { 3 } \pmb { e } _ { 3 } ,$

just as one is accustomed nowadays in electromagnetism to treat the electric vector $\pmb { { \cal E } } ,$ ， without having to write out its components; uses a similar approach to differentiation (compare gradient operator $\mathbf { v }$ of elementary vector analysis,as distinguished from coordinate-dependent pieces of such an operator, such as $\partial / \partial x , \partial / \partial y$ ，etc.)； is the quickest, simplest mathematical scheme One knows to derive general results in differential geometry. (3) Differential geometry as expressed in the language of components: is indispensible in programming large parts of general relativity for a computer; is convenient or necessary or both when one is dealing even at the level of elementary algebra with the most simple applications of relativity, from the expansion of the Friedmann universe to the curvature around a static center of attraction.

Newtonian gravity (Chapter l2) and the central geometric simplicity of Einstein's field equations (Chapter l5), because he had full command of all three methods of doing differential geometry. Today, no one has full power to communicate with others about the subject who cannot express himself in all three languages. Hence the interplay between the three forms of expression in what follows.

It is not new to go back and forth between the three languages,as witnesses the textbook treatment of the velocity and acceleration of a planet in Kepler motion around the sun. The velocity is written

Planetary orbit as example of three viewpoints

$$
\mathbf { \nu } = v ^ { \hat { r } } e _ { \hat { r } } + v ^ { \hat { \phi } } e _ { \hat { \phi } } .
$$

(The hats $\dots$ on $\boldsymbol { e } _ { \hat { \boldsymbol { r } } }$ and $\pmb { e } _ { \hat { \phi } }$ signify that these are unit vectors.）The acceleration is

$$
a = \frac { d \mathfrak { v } } { d t } = \frac { d \mathfrak { v } ^ { \hat { r } } } { d t } \mathfrak { e } _ { \hat { r } } + \frac { d \mathfrak { v } ^ { \hat { \phi } } } { d t } \mathfrak { e } _ { \hat { \phi } } + \mathfrak { v } ^ { \hat { r } } \frac { d \mathfrak { e } _ { \hat { r } } } { d t } + \mathfrak { v } ^ { \hat { \phi } } \frac { d \mathfrak { e } _ { \hat { \phi } } } { d t } .
$$

![](images/568de275318e2c00970bf21b67b4aa8467ab69a36f0143b9d4c2e39ba67c2728.jpg)  
Figure 8.1. A Keplerian orbit in the sun’s gravitational feld,as treated using the standard Euclidean-space version of Newtonian gravity.The basis vectors themselves change from point to point along the orbit [equations (8.3).This fgure illustrates the pictorialaspectof differential geometry.Later(exercise8.5)it wililustrate the concepts of“covariant derivative”and “connection coefficients.”

The unit vectors are turning (Figure 8.1) with the angular velocity $\omega = d \phi / d t$ ; so

$$
\begin{array} { l } { \displaystyle \frac { d e _ { \hat { r } } } { d t } = \omega e _ { \hat { \phi } } = \frac { d \hat { \phi } } { d t } e _ { \hat { \phi } } , } \\ { \displaystyle \frac { d e _ { \hat { \phi } } } { d t } = - \omega e _ { \hat { r } } = - \frac { d \phi } { d t } e _ { \hat { r } } . } \end{array}
$$

Thus the components of the acceleration have the values

$$
a ^ { \hat { r } } = { \frac { d v ^ { \hat { r } } } { d t } } - v ^ { \hat { \phi } } { \frac { d \phi } { d t } } = { \frac { d ^ { 2 } r } { d t ^ { 2 } } } - r \left( { \frac { d \phi } { d t } } \right) ^ { 2 }
$$

and

$$
a ^ { \hat { \phi } } = { \frac { d v ^ { \hat { \phi } } } { d t } } + v ^ { \hat { r } } { \frac { d \phi } { d t } } = { \frac { d } { d t } } \left( r { \frac { d \phi } { d t } } \right) + { \frac { d r } { d t } } { \frac { d \phi } { d t } } .
$$

Here is the acceleration in the language of components; $\pmb { a }$ was the acceleration in abstract language; and Figure 8.l shows the acceleration as an arrow. Each of these three languages will receive its natural generalization in the coming sections and chapters from two-dimensional flat space (with curvilinear coordinates） to four-dimensional curved spacetime, and from spacetime to more general manifolds (see $\ S 9 . 7$ on manifolds).

Turn now to the Track-1 overview of diferential geometry.

# $\$ 8.4$ . TENSOR ALGEBRA IN CURVED SPACETIME

Tensor algebra:

To see spacetime curvature at work,examine tidal gravitational forces (geodesic deviation); and to probe these forces, make measurements in a finite-sized laboratory. Squeeze the laboratory to infinitesimal size; alleffects of spacetime curvature become infinitesimal; the physicist cannot tell whether he is in fat spacetime or curved spacetime.Neither can the mathematician,in the limit as his domain of attention squeezes down to a single event, $\mathcal { P } _ { o }$

(1）occurs in infinitesimal neighborhood of an event

At the event $\mathcal { P } _ { o }$ (in the infinitesimal laboratory) both physicist and mathematician can talk of vectors, of 1-forms, of tensors; and no amount of spacetime curvature can force the discussion to change from its flat-space form.A particle at $\mathcal { P } _ { o }$ has a 4-momentum $\pmb { p }$ ,with squared length

(2) is same in curved spacetime as in flat

$$
p ^ { 2 } = p \cdot p = g ( p , p ) = - m ^ { 2 } .
$$

The squared length,as always, is calculated by inserting $\pmb { p }$ into both slots of a linear machine, the metric $\pmb { \mathscr { g } }$ at $\mathcal { P } _ { o }$ . The particle also has a 4-acceleration $\pmb { a }$ at $\mathcal { P } _ { o }$ ； and, if the particle is charged and freely moving, then $\pmb { a }$ is produced by the electromagnetic feld tensor $\pmb { F }$ ：

$$
m \pmb { a } = e \pmb { F } ( . \dots , \pmb { u } ) .
$$

In no way can curvature affect such local, coordinate-free, geometric relations.And in no way can it prevent one from introducing a local Lorentz frame at $\mathcal { P } _ { o } ,$ and from performing standard, flat-space index manipulations in it:

$$
p = p ^ { \alpha } e _ { \alpha } , \quad p ^ { 2 } = p ^ { \alpha } p _ { . } ^ { \beta } \eta _ { \alpha \beta } = p ^ { \alpha } p _ { \alpha } , \quad \quad m a ^ { \alpha } = e F ^ { \alpha \beta } u _ { \beta } .
$$

But local Lorentz frames are not enough for the man who would calculate in curved spacetime. Non-Lorentz frames (nonorthonormal basis vectors $\{ \pmb { e } _ { \alpha } \} )$ often simplify calculations.Fortunately,no effort at all is required to master the rules of "index mechanics”in an arbitrary basis at a fixed event $\mathcal { P } _ { o }$ . The rules are identical to those in flat spacetime, except that (l) the covariant Lorentz components $\eta _ { \alpha \beta }$ of the metric are replaced by

(3)rules for component manipulation change slightly when using nonorthonormai basis

$$
\begin{array} { r } { g _ { \alpha \beta } \equiv \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } \equiv \pmb { g } ( \pmb { e } _ { \alpha } , \pmb { e } _ { \beta } ) ; } \end{array}
$$

Components of metric

(2) the contravariant components $\eta ^ { \alpha \beta }$ are replaced by $g ^ { \alpha \beta }$ ， where

$$
| | g ^ { \alpha \beta } | | \equiv | | g _ { \alpha \beta } | | ^ { - 1 } ( \mathrm { m a t r i x \ i n v e r s e } ) ;
$$

i.e.,

$$
g _ { \alpha \beta } g ^ { \beta \gamma } = \delta _ { \alpha } \gamma ;
$$

(3)the Lorentz transformation matrix $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and its inverse $1 1 A ^ { \beta } { } _ { \alpha ^ { \prime } } | |$ are replaced by an arbitrary but nonsingular transformation matrix $| | L ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ and its inverse $1 1 L ^ { \beta } { _ { \alpha } } ! !$ ：

$$
\begin{array} { r } { \pmb { \mathscr { e } } _ { \beta } = \pmb { \mathscr { e } } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } , \qquad p ^ { \beta } = L ^ { \beta } { } _ { \alpha } p ^ { \alpha ^ { \prime } } , } \\ { | ! L ^ { \beta } { } _ { \alpha ^ { \prime } } | | = | ! L ^ { \alpha ^ { \prime } } { } _ { \beta } | | ^ { - 1 } ; } \end{array}
$$

(4) in the special case of “coordinate bases,” ${ \pmb e } _ { \alpha } = \partial \mathcal { P } / \partial x ^ { \alpha }$ ， $\begin{array} { r } { \pmb { e } _ { \beta ^ { \prime } } = \partial \mathcal { P } / \partial \boldsymbol { x } ^ { \beta ^ { \prime } } , } \end{array}$

$$
L ^ { \alpha ^ { \prime } } { } _ { \beta } = \partial x ^ { \alpha ^ { \prime } } / \partial x ^ { \beta } , \qquad L ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } } ;
$$

and (5) the Levi-Civita tensor $\pmb { \varepsilon }$ ,like the metric tensor, has components that depend--- on how nonorthonormal the basis vectors are (see exercise 8.3): if ${ \pmb \theta } _ { 0 }$ points toward the future and $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ are righthanded, then

$$
\begin{array} { l } { { \varepsilon _ { \alpha \beta \gamma \delta } = ( - g ) ^ { 1 / 2 } [ \alpha \beta \gamma \delta ] , } } \\ { { \varepsilon ^ { \alpha \beta \gamma \delta } = g ^ { - 1 } \varepsilon _ { \alpha \beta \gamma \delta } = - ( - g ) ^ { - 1 / 2 } [ \alpha \beta \gamma \delta ] , } } \end{array}
$$

where $[ \alpha \beta \gamma \delta ]$ is the completely antisymmetric symbol

$$
[ \alpha \beta \gamma \delta ] \equiv \left\{ { \begin{array} { l } { + 1 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ i s ~ a n ~ e v e n ~ p e r m u t a t i o n ~ o f ~ } } 0 1 2 3 , } \\ { - 1 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ i s ~ a n ~ o d d ~ p e r m u t a t i o n ~ o f ~ } } 0 1 2 3 , } \\ { 0 { \mathrm { ~ i f ~ } } \alpha \beta \gamma \delta { \mathrm { ~ a r e ~ n o t ~ a l l ~ d i f f e r e n t } } , } \end{array} } \right.
$$

and where $g$ is the determinant of the matrix $1 | g _ { \alpha \beta } | |$

$$
g \equiv { \sf d e t l l } g _ { \alpha \beta } | | = { \sf d e t l } | \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } | | .
$$

Read Box 8.4 for full discussion and proofs; work exercise 8.1 below for fuller understanding and mastery.

Several dangers are glossed over in this discussion.In flat spacetime one often does not bother to say where a vector,l-form, or tensor is located. One freely moves geometric objects from event to event without even thinking. Ofcourse,the unwritten rule of transport is: hold all lengths and directions fixed while moving;i.e.,hold all Lorentz-frame components fixed; i.e.，“parallel-transport” the object. But in

# Box 8.4 TENSOR ALGEBRA AT A FIXED EVENT IN AN ARB/TRARY BASIS

A.Bases

Tangent-vector basis: Pick $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ at $\scriptstyle { \mathcal { P } } _ { 0 }$ arbitrarily-but insist they belinearly independent.

“Dual basis” for l-forms: The basis $\{ \pmb { e } _ { \alpha } \}$ determines a l-form basis $\{ { \pmb { \omega } } ^ { \alpha } \}$ (its “dual basis") by

$$
\langle { \pmb w } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }
$$

[see equation (2.19)].

Geometric interpretation (Figure 9.2): ${ \pmb e } _ { 2 } , { \pmb e } _ { 3 } , { \pmb e } _ { 0 }$ lie parallel to surfaces of $\pmb { \omega } ^ { 1 }$ ； $\pmb { \varrho } _ { 1 }$ pierces precisely one surface of $\pmb { \omega } ^ { 1 }$

Function interpretation: $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ determines the value of $\pmb { \omega } ^ { \pmb { \alpha } }$ on any vector $\pmb { \mu } = \pmb { u } ^ { \beta } \pmb { \mathcal { e } } _ { \beta }$ (number of “bongs of bel" as $\pmb { u }$ pierces $\pmb { \omega } ^ { \alpha }$ ：

$$
\langle { \pmb w } ^ { \alpha } , { \pmb u } \rangle = \langle { \pmb w } ^ { \alpha } , u ^ { \beta } { \pmb e } _ { \beta } \rangle = u ^ { \beta } \langle { \pmb w } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = u ^ { \beta } \delta _ { \beta } ^ { \alpha } = u ^ { \alpha } .
$$

Special case: coordinate bases. Choose an arbitrary coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ At $\mathcal { P } _ { 0 }$ choose ${ \pmb { e } } _ { \alpha } = \partial \pmb { \mathcal { P } } / \partial x ^ { \alpha }$ as basis vectors.Then the dual basis is $\pmb { \omega } ^ { \alpha } = \pmb { d x } ^ { \alpha }$ Proof: the general coordinate-free relation $\langle \pmb { d } f , \pmb { v } \rangle = \hat { \partial } _ { \pmb { v } } f$ [equation (2.17)], with $f = x ^ { \alpha }$ and $\pmb { v } = \partial \pmb { \mathcal { P } } / \partial x ^ { \beta }$ ，reads

$$
\begin{array} { r } { \langle \pmb { d } x ^ { \alpha } , \partial \pmb { \mathcal { P } } / \partial x ^ { \beta } \rangle = ( \partial / \partial x ^ { \beta } ) x ^ { \alpha } = \delta _ { \beta } ^ { \alpha } . } \end{array}
$$

# B. Algebra of Tangent Vectors and 1-Forms

The Lorentz-frame discussion of equations (2.19) to(2.22) is completely unchanged when one switches to an arbitrary basis. Its conclusions:

expansion, $\pmb { u } = \pmb { e } _ { \alpha } \pmb { u } ^ { \alpha }$ ， $\sigma = \sigma _ { \alpha } \omega ^ { \alpha }$ ； calculation of components, uα = <ωα,u>, O& = (σ,eα>; value of form on vector, $\langle \pmb { \sigma } , \pmb { u } \rangle = \sigma _ { \alpha } u ^ { \alpha }$

Application to gradients of functions:

expansion, ${ \pmb d } f = f _ { , \alpha } { \pmb \omega } ^ { \alpha }$ [defines $f _ { , \alpha } ]$ ；   
calculation of components, $f _ { , \alpha } = \langle d f , e _ { \alpha } \rangle = \partial _ { \pmb { \theta } _ { \alpha } } f$ [see equation (2.17)].

Raising and lowering of indices is accomplished with gaβ and gαβ equations (8.5） and (8.6)). Proof:

$\widetilde { \pmb { u } }$ ，the l-form corresponding to $\pmb { u }$ , is defined by $\langle \widetilde { \pmb { u } } , \pmb { v } \rangle = \pmb { u } \cdot \pmb { v }$ for all $\mathbf { \Delta } v ;$   
thus, $u _ { \alpha } \equiv \langle \tilde { \pmb { u } } , \pmb { e } _ { \alpha } \rangle = \pmb { u } \cdot \pmb { e } _ { \alpha } = u ^ { \beta } \pmb { e } _ { \beta } \cdot \pmb { e } _ { \alpha } = u ^ { \beta } g _ { \beta \alpha } .$ ：   
inverting this equation yields $u ^ { \beta } = g ^ { \beta \alpha } u _ { \alpha }$

# C. Change of Basis

The discussion of Lorentz transformations in equations (2.39) to (2.43) is applicable to general changes of basis if one replaces $| | A ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ by an arbitrary but nonsingular matrix $1 | L ^ { \alpha ^ { \prime } } { } _ { \beta } | |$ [equations (8.7), (8.8)]. Conclusions:

$$
\begin{array} { r l r l } & { \pmb { e } _ { \alpha ^ { \prime } } = \pmb { e } _ { \beta } L ^ { \beta } _ { \alpha ^ { \prime } } , } & & { \pmb { e } _ { \beta } = \pmb { e } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } ; } \\ & { \pmb { \omega } ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \pmb { \omega } ^ { \beta } , } & & { \pmb { \omega } ^ { \beta } = L ^ { \beta } _ { \alpha ^ { \prime } } \pmb { \omega } ^ { \alpha ^ { \prime } } ; } \\ & { \pmb { v } ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \pmb { v } ^ { \beta } , } & & { \pmb { v } ^ { \beta } = L ^ { \beta } _ { \alpha ^ { \prime } } \pmb { v } ^ { \alpha ^ { \prime } } ; } \\ & { \sigma _ { \alpha ^ { \prime } } = \sigma _ { \beta } L ^ { \beta } _ { \alpha ^ { \prime } } , } & & { \sigma _ { \beta } = \sigma _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } . } \end{array}
$$

When both bases are coordinate bases, then $L ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } } , L ^ { \alpha ^ { \prime } } { } _ { \beta } = \partial x ^ { \alpha ^ { \prime } } / \partial x ^ { \beta }$ Proof:

$$
{ \pmb e } _ { \alpha ^ { \prime } } = { \frac { \hat { \alpha } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } = { \frac { \hat { \alpha } x ^ { \beta } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } { \frac { \hat { \alpha } } { \hat { \alpha } x ^ { \beta } } } = { \frac { \hat { \alpha } x ^ { \beta } } { \hat { \alpha } x ^ { \alpha ^ { \prime } } } } { \pmb e } _ { \beta } ; \qquad \mathrm { s i m i l a r l y } ~ { \pmb e } _ { \beta } = { \frac { \hat { \alpha } x ^ { \alpha ^ { \prime } } } { \hat { \alpha } x ^ { \beta } } } { \pmb e } _ { \alpha ^ { \prime } } .
$$

# D． Algebra of Tensors

The discussions of tensor algebra given in $\ S 3 . 2$ [equations (3.8) to (3.22)] and in $\ S 3 . 5$ (excluding gradient and divergence) are unchanged, except that

$$
\eta _ { \alpha \beta } \longrightarrow g _ { \alpha \beta } \qquad \eta ^ { \alpha \beta } \longrightarrow g ^ { \alpha \beta } , \qquad A _ { \beta } ^ { \alpha ^ { \prime } } \longrightarrow L _ { \beta } ^ { \alpha ^ { \prime } } , \qquad A _ { \alpha ^ { \prime } } ^ { \beta } \longrightarrow L _ { \alpha ^ { \prime } } ^ { \beta } ;
$$

and the components of the Levi-Civita tensor are changed from (3.50) to (8.10) [see exercise 8.3[.

Chief conclusions :

expansion, $\pmb { S } = S ^ { \alpha } { } _ { \beta \gamma } \pmb { \theta } _ { \alpha } \otimes \pmb { \omega } ^ { \beta } \otimes \pmb { \omega } ^ { \gamma } ;$   
components, $S ^ { \alpha } { } _ { \beta \gamma } = \pmb { S } ( \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } , \pmb { e } _ { \gamma } ) ;$   
raising and lowering indices, $S _ { \mu \beta } { } ^ { \nu } = g _ { \mu \alpha } g ^ { \nu \gamma } S ^ { \alpha } { } _ { \beta \gamma } ;$   
change of basis, $S ^ { \lambda ^ { \prime } } { } _ { \mu ^ { \prime } \nu ^ { \prime } } = L ^ { \lambda ^ { \prime } } { } _ { \alpha } L ^ { \dot { \beta } } { } _ { \mu ^ { \prime } } L ^ { \gamma } { } _ { \nu ^ { \prime } } S ^ { \alpha } { } _ { \beta \gamma }$ ；   
machine operation, $\pmb { S } ( \pmb { \sigma } , \pmb { u } , \pmb { v } ) = { S ^ { \alpha } } _ { \beta \gamma } \sigma _ { \alpha } u ^ { \beta } v ^ { \gamma }$ ；   
tensor product, ${ \pmb { \tau } } = { \pmb { \mu } } \otimes { \pmb { v } } \Longleftrightarrow { \pmb { T } } ^ { \alpha \beta } = { \pmb { u } } ^ { \alpha } { \pmb { v } } ^ { \beta }$ ；   
contraction, ${ \bf \ddot { \theta } } ^ { \bullet } { \bf \bar { M } } =$ contraction of $\pmb R$ on slots 1 and $3 ^ { \mathfrak { w } } \Longleftrightarrow M _ { \mu \nu } = R ^ { \alpha } { } _ { \mu \alpha \nu }$ wedge product, $\alpha \wedge \beta$ has components $\alpha ^ { \mu } \beta ^ { \nu } - \beta ^ { \mu } \alpha ^ { \nu }$ ；   
Dual, ${ } ^ { * } J _ { \alpha \beta \gamma } = J ^ { \mu } \varepsilon _ { \mu \alpha \beta \gamma } , { } ^ { * } F _ { \alpha \beta } = { \scriptstyle { \frac { 1 } { 2 } } } F ^ { \mu \nu } \varepsilon _ { \mu \nu \alpha \beta } , { } ^ { * } B _ { \alpha } = { \scriptstyle { \frac { 1 } { 6 } } } B ^ { \lambda \mu \nu } \varepsilon _ { \lambda \mu \nu \alpha } .$

# E. Commutators (exercise 8.2; \$9.6; Box 9.2)

f ${ \pmb u }$ and $\pmb { \nu }$ are tangent vector felds,one takes the view that $\pmb { u } = \hat { d } _ { \pmb { u } }$ and $\pmb { v } = \hat { d } _ { \pmb { v } }$ and one defines

$$
\mathbf { \Delta } [ u , v ] \equiv [ \hat { \sigma } _ { u } , \hat { \sigma } _ { v } ] \equiv \hat { \sigma } _ { u } \hat { \sigma } _ { v } - \hat { \sigma } _ { v } \hat { \sigma } _ { u } .
$$

This commutator is itself a tangent vector field.

Components in a coordinate basis:

$$
\begin{array} { r } { [ { \pmb u } , { \pmb v } ] = ( u ^ { \beta } v ^ { \alpha } , _ { \beta } - v ^ { \beta } u ^ { \alpha } , _ { \beta } ) ( \partial / \partial x ^ { \alpha } ) . \qquad } \\ { \qquad \quad \pmb { \mathrm { t } } = { \pmb e } _ { \alpha } ] } \end{array}
$$

Commutation coefficients of a basis:

$$
[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] \equiv c _ { \alpha \beta } { } ^ { \gamma } { \pmb e } _ { \gamma } , \qquad c _ { \alpha \beta \mu } \equiv c _ { \alpha \beta } { } ^ { \gamma } g _ { \gamma \mu } .
$$

Coordinate basis ("holonomic") ${ c _ { \alpha \beta } } ^ { \gamma } = 0$

Noncoordinate basis ("anholonomic") some ${ c _ { \alpha \beta } } ^ { \gamma } \neq 0$ (see exercise 9.9).

curved spacetime there is no global Lorentz coordinate system in which to hold components fixed; and objects initially parallel, after “parallel transport” along different curves cease to be parallel("geodesic deviation”; Earth's meridians,parallel at equator, cross at north and south poles). Thus,in curved spacetime one must not blithely move a geometric object from point to point, without carefully specifying how it is to be moved and by what route. Each local geometric object has its own official place of residence (event $\mathcal { P } _ { o } )$ ; it can interact with other objects residing there (tensor algebra); but it cannot interact with any object at another event $\mathcal { L }$ until it has been carefully transported from $\mathcal { P } _ { o }$ to $\mathfrak { L }$

Vectors and tensors must not be moved blithely from point to point

This line of reasoning, pursued further,leads one to speak of the“tangent space” at each event, in which that event's vectors (arrows)and 1-forms (families of surfaces) lie,and in which its tensors (linear machines） operate. One even draws heuristic pictures of the tangent space,as in Figure 9.1 (p. 231).

Tangent space defined

Another danger in curved spacetime is the temptation to regard vectors as arrows linking two events ("point for head and point for tail")-i.e.,to regard the tangent space of Figure 9.l as lying in spacetime itself.This practice can be useful for heuristic purposes, but it is incompatible with complete mathematical precision. (How is the tangent space to be molded into a warped surface?) Four definitions of a vector were given in Figure 2.l (page 49): three definitions relying on “point for head and point for tail"； one, $" d \varphi / d \lambda "$ ，purely local. Only the local definition is wholly viable in curved spacetime, and even it can be improved upon, in the eyes of mathematicians,as follows.

Definitions of vector in curved spacetime:

(1)as $d \mathcal { P } / d \lambda$

There is a one-to-one correspondence (complete “isomorphism") between vectors ${ \pmb u }$ and directional derivative operators $\partial _ { \pmb { u } }$ . The concept of vector is a bit fuzzy, but “directional derivative” is perfectly well-defined.To get rid of all fuzziness, exploit the isomorphism to the full: define the tangent vector $\pmb { u }$ to be equal to the corresponding directional derivative

$$
\pmb { u } \equiv \partial _ { \pmb { u } } .
$$

(2) as directional derivative

(This practice, unfamiliar as it may be to a physicist at first, has mathematical power; so this book will use it frequently. For a fuller discussion, see $\ S 9 . 2 . )$

# Exercise 8.1. PRACTICE WITH TENSOR ALGEBRA

Let $t , x , y , z$ be Lorentz coordinates in flat spacetime, and let

$$
r = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } , \qquad \theta = \cos ^ { - 1 } ( z / r ) , \qquad \phi = \tan ^ { - 1 } ( y / x )
$$

be the corresponding spherical coordinates. Then

$$
{ \pmb e } _ { 0 } = \hat { \sigma } \mathcal { S } / \hat { \sigma } t , \qquad { \pmb e } _ { r } = \hat { \sigma } \mathcal { S } ^ { \beta } / \hat { \sigma } r , \qquad { \pmb e } _ { \theta } = \hat { \sigma } \mathcal { S } / \hat { \sigma } \theta , \qquad { \pmb e } _ { \phi } = \hat { \sigma } \mathcal { P } / \hat { \sigma } \phi
$$

is a coordinate basis,and

$$
{ \pmb { e } } _ { \hat { \imath } } = \frac { \partial \mathcal { P } } { \partial t } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { \partial \mathcal { P } } { \partial r } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { 1 } { r } \frac { \hat { c } \mathcal { P } } { \hat { c } \theta } , \qquad { \pmb { e } } _ { \hat { \imath } } = \frac { 1 } { r \sin \theta } \frac { \hat { \partial } \mathcal { P } } { \hat { c } \phi }
$$

is a noncoordinate basis.

(a) Draw a picture of $\mathbf { \mathcal { e } } _ { \theta } , \mathbf { \mathcal { e } } _ { \phi } , \mathbf { \mathcal { e } } _ { \hat { \theta } }$ ,and $\pmb { e } _ { \hat { \phi } }$ at several different points on a sphere of constant t,r. [Answer for $\pmb { \theta } , \pmb { \theta } _ { \phi }$ should resemble Figure 9.1.]

(b) What are the l-form bases $\scriptstyle \left\{ \pmb { \omega } ^ { \alpha } \right\}$ and $\{ \pmb { \omega } ^ { \hat { \alpha } } \}$ dual to these tangent-vector bases? [Answer: $\omega ^ { 0 } = \mathbf { \nabla } \mathbf { \mathbf { \mathbf { \mathit { d } } } } t$ $\pmb { \omega } ^ { \tau } = \pmb { d r }$ $\omega ^ { \theta } = d \theta$ $\omega ^ { \phi } = d \phi$ ； $\pmb { \omega } ^ { \hat { 0 } } = \pmb { d } t$ $\pmb { \omega } ^ { \dagger } = \pmb { d r }$ $\omega ^ { \bar { \dot { \theta } } } = r d \theta$ ， $\begin{array} { r } { { \pmb { \omega } } ^ { \hat { \diamond } } = r \sin \theta \mathbf { d } \phi . } \end{array}$ 1

(c) What is the transformation matrix linking the original Lorentz frame to the spherical. coordinate frame $\{ \pmb { e _ { a } } \} \ ?$ [Answer: nonzero components are

$$
\begin{array} { r l r l } & { L ^ { t } _ { 0 } = 1 , \quad } & { L ^ { z } _ { r } = \frac { \hat { c } \hat { z } } { \hat { \sigma } r } = \cos \theta . } & & { L ^ { z } _ { \theta } = \frac { \hat { \sigma } z } { \hat { \sigma } \theta } = - r \sin \theta , } \\ & { L ^ { z } _ { r } = \sin \theta \cos \phi , \quad } & { L ^ { x } _ { \theta } = r \cos \theta \cos \phi , \quad } & { L ^ { x } _ { \phi } = - r \sin \theta \sin \phi , } \\ & { L ^ { \nu } _ { r } = \sin \theta \sin \phi , \quad } & { L ^ { \nu } _ { \theta } = r \cos \theta \sin \phi , \quad } & { L ^ { \nu } _ { \phi } = r \sin \theta \cos \phi . ] } \end{array}
$$

(d) Use this transformation matrix to calculate the metric components $g _ { \alpha \beta }$ in the spherical coordinate basis. and invert the resulting matrix to get $g ^ { \alpha \beta }$ .[Answer:

$$
\begin{array} { r l r l r l r l r l } & { } & { g _ { 0 0 } = - 1 , \quad } & { g _ { r r } = 1 , } & & { g _ { \theta \theta } = r ^ { 2 } , \quad } & { g _ { \phi \phi } = r ^ { 2 } \sin ^ { 2 } \theta , } & & { \mathrm { a l l ~ o t h e r ~ } g _ { \alpha \beta } = 0 . } \\ & { } & { g ^ { 0 0 } = - 1 , } & & { g ^ { r r } = 1 , } & & { g ^ { \theta \theta } = r ^ { - 2 } , } & & { g ^ { \phi \phi } = r ^ { - 2 } \sin ^ { - 2 } \theta , } & & { \mathrm { a l l ~ o t h e r ~ } g ^ { \alpha \beta } = 0 . } \end{array}
$$

(e) Showthat the noncoordinate basis $\left\{ \pmb { e } _ { \dot { \alpha } } \right\}$ is orthonoraleveryhere;ie,tat $g _ { \hat { \alpha } \hat { \beta } } =$ $\eta _ { \alpha \beta }$ ；i.e. that

$$
g = - { \omega } ^ { \hat { 0 } } \otimes { \omega } ^ { \hat { 0 } } + { \omega } ^ { \hat { \tau } } \otimes { \omega } ^ { \hat { \tau } } + { \omega } ^ { \hat { \theta } } \otimes { \omega } ^ { \hat { \theta } } + { \omega } ^ { \hat { \phi } } \otimes { \omega } ^ { \hat { \phi } } .
$$

(f） Write the gradient of a function $f$ in terms of the spherical coordinate and noncoordinate bases. [Answer:

$$
{ \begin{array} { r l } & { d f = { \frac { \partial f } { \partial t } } d t + { \frac { \partial f } { \partial r } } d r + { \frac { \partial f } { \partial \theta } } d \theta + { \frac { \partial f } { \partial \phi } } d \phi } \\ & { \qquad = { \frac { \partial f } { \partial t } } { \boldsymbol { \omega } } ^ { \hat { 0 } } + { \frac { \partial f } { \partial r } } { \boldsymbol { \omega } } ^ { \hat { r } } + { \frac { 1 } { r } } { \frac { \partial f } { \partial \theta } } { \boldsymbol { \omega } } ^ { \hat { \theta } } + { \frac { 1 } { r \sin \theta } } { \frac { \partial f } { \partial \phi } } { \boldsymbol { \omega } } ^ { \hat { \phi } } . } \end{array} }
$$

(g)What are the components of the Levi-Civita tensor in the spherical coordinate and noncoordinate bases? [Answer for coordinate basis:

$$
\begin{array} { l } { { \varepsilon _ { 0 r \theta \phi } = - \varepsilon _ { r 0 \theta \phi } = + \varepsilon _ { r \theta 0 \phi } = \cdot \cdot \cdot = r ^ { 2 } \sin \theta , } } \\ { { \varepsilon ^ { 0 r \theta \phi } = - \varepsilon ^ { r 0 \theta \phi } = + \varepsilon ^ { r \theta \phi 0 } = \cdot \cdot \cdot = - r ^ { - 2 } \sin ^ { - 1 } \theta . } } \end{array}
$$

# Exercise 8.2. COMMUTATORS

Take the mathematician's viewpoint that tangent vectors and directional derivatives are the same thing, $\pmb { u } = \hat { d } _ { \pmb { u } }$ .Let ${ \pmb u }$ and $\pmb { \nu }$ be two vector fields,and define their commutator in the manner familiar from quantum mechanics

$$
[ { \pmb u } , { \pmb v } ] \equiv [ \hat { \sigma } _ { { \pmb w } } , \hat { \sigma } _ { { \pmb v } } ] \equiv \hat { \sigma } _ { { \pmb u } } \hat { \sigma } _ { { \pmb v } } - \hat { \sigma } _ { { \pmb v } } \hat { \sigma } _ { { \pmb u } }
$$

(a) Derive the following expression for $[ { \pmb u } , { \pmb v } ] ,$ ,valid in any coordinate basis,

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } ^ { \beta } { \pmb v } ^ { \alpha } , \beta - v ^ { \beta } { \pmb u } ^ { \alpha } , \beta ) { \pmb e } _ { \alpha } .
$$

Thus, despite the fact that it looks like a second-order differential operator, $[ { \pmb u } , { \pmb v } ]$ is actually of first order-i.e., it is a tangent vector.

(b) For any basis $\{ \pmb { \mathscr { e } } _ { \pmb { \alpha } } \}$ ,one defines the“commutation coefficients” ${ c _ { \beta } } { _ { \gamma } } ^ { \alpha }$ and ${ c _ { \beta \gamma \alpha } }$ by

$$
[ e _ { \beta } , e _ { \gamma } ] \equiv c _ { \beta \gamma } { } ^ { \alpha } e _ { \alpha } ; c _ { \beta \gamma \alpha } \equiv g _ { \alpha \mu } c _ { \beta \gamma } { } ^ { \mu } .
$$

Show that ${ c _ { \beta \gamma } } ^ { \alpha } = { c _ { \beta \gamma \alpha } } = 0$ for any coordinate basis.

(c） Calculate $c _ { \hat { \beta } \hat { \gamma } } { } ^ { \hat { \alpha } }$ for the spherical noncoordinate basis of exercise 8.1.[Answer: All vanish except

$$
\begin{array} { r l } & { c _ { \hat { r } \hat { \theta } } ^ { \enspace \enspace \hat { \theta } } = - c _ { \hat { \theta } \hat { r } } ^ { \enspace \enspace \hat { \theta } } = - 1 / r , } \\ & { c _ { \hat { r } \hat { \phi } } ^ { \enspace \enspace \hat { \phi } } = - c _ { \hat { \phi } \hat { r } } ^ { \enspace \enspace \hat { \phi } } = - 1 / r , } \\ & { c _ { \hat { \theta } \hat { \phi } } ^ { \enspace \enspace \hat { \phi } } = - c _ { \hat { \phi } \hat { \theta } } ^ { \enspace \enspace \hat { \phi } } = - \cot \theta / r . ] } \end{array}
$$

# Exercise 8.3. COMPONENTS OF LEVI-CIVITA TENSOR IN NONORTHONORMAL FRAME

(a) Show that expressions (8.10) are the components of $\pmb \varepsilon$ in an arbitrary basis, with ${ \pmb \theta } _ { 0 }$ pointing toward the future and $\pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ right-handed.[Hints: (l） Review the discussion of $\pmb \varepsilon$ in Lorentz frames, given in exercise 3.13. (2) Calculate $\pmb { \varepsilon } _ { \alpha \beta \gamma \delta }$ and $\varepsilon ^ { \alpha \beta \gamma \delta }$ by transforming from a local Lorentz frame $\left\{ \pmb { e } _ { \hat { \mu } } \right\}$ ,e.g.,

$$
\varepsilon _ { \alpha \beta \gamma \delta } = L _ { \alpha } ^ { \hat { \mu } } L _ { \beta } ^ { \hat { \nu } } L _ { \gamma } ^ { \hat { \lambda } } L _ { \delta } ^ { \hat { \rho } } \varepsilon _ { \hat { \mu } \hat { \nu } \hat { \lambda } \hat { \rho } } .
$$

(3) Show that these expressions reduce to

$$
\varepsilon _ { \alpha \beta \gamma \delta } = \mathsf { d e t l } | L ^ { \hat { \mu } } { } _ { \nu } | | \varepsilon _ { \alpha \beta \hat { \gamma } \hat { \delta } } , \qquad \varepsilon ^ { \alpha \beta \gamma \delta } = \mathsf { d e t l } | L ^ { \nu } { } _ { \hat { \mu } } | | \varepsilon ^ { \hat { \alpha } \hat { \beta } \hat { \gamma } \hat { \delta } } .
$$

(4) Show, from the transformation law for the metric components, that

$$
( \mathop { \bf d e t } | | L ^ { \nu } { } _ { \hat { \mu } } | | ) ^ { 2 } \mathop { \bf d e t } | | g _ { \alpha \beta } | | = - 1 .
$$

(5)Combine these results to obtain expressions (8.10).]

(b) Show that the components of the permutation tensors [defined by equations (3.50h)- (3.50j)] have the same values [equations (3.50k)- $( 3 . 5 0 \mathbf { m } ) ]$ in arbitrary frames as in Lorentz frames.

Additional exercises on tensor algebra: exercises 9.3 and 9.4 (page 234).

# \$8.5. PARALLEL TRANSPORT, COVARIANT DERIVATIVE, CONNECTION COEFFICIENTS，GEODESICS

The vehicle that carries one from classical mechanics to quantum mechanics is the correspondence principle. Similarly, the vehicle between flat spacetime and curved spacetime is the equivalence principle: “The laws of physics are the same in any local Lorentz frame of curved spacetime as in a global Lorentz frame of flat spacetime.”But to apply the equivalence principle,one must first have a mathematical representation of a local Lorentz frame. The obvious choice is this: $\pmb { A }$ local Lorentz frame at a given event ${ \mathcal { P } } _ { o }$ is the closest thing there is to a global Lorentz frame at that event; i.e., it is a coordinate system in which

Equivalence principle as vehicle between flat spacetime and curved

Local Lorentz frame: mathematical representation

$$
g _ { \mu \nu } ( \mathcal { P } _ { o } ) = \eta _ { \mu \nu } ,
$$

and in which $g _ { \mu \nu }$ holds as tightlyas possible to $\eta _ { \mu \nu }$ in the neighborhood of ${ \mathcal { P } } _ { o }$ ：

$$
g _ { \mu \nu , \alpha } ( \mathcal { P } _ { o } ) = 0 .
$$

More tightly than this it cannot hold in general $[ g _ { \mu \nu , \alpha \beta } ( \mathcal { P } _ { o } )$ cannot be set to zero]; spacetime curvature forces it to change. [Combine $\ S 1 1 . 5$ with equations (8.24) and (8.44).]

An observer in a local Lorentz frame in curved spacetime can compare vectors and tensors at neighboring events, just as he would in fat spacetime. But to make the comparison, he must parallel-transport them to a common event. For him the act of parallel transport is simple:he keeps all Lorentz-frame components fixed, just as if he were in flat spacetime. But for a man without a local Lorentz frameperhaps with no coordinate system or basis vectors at all-parallel transport is less trivial.He must either ask his Lorentz-based friend the result,or he must use a more sophisticated technique.One technique he can use-a“Schild's ladder”construction that requires no coordinates or basis vectors whatsoever-is described in $\ S 1 0 . 2$ and Box l0.2. But the Track-l reader need not master Schild's ladder. He can always ask a local Lorentz observer what the result of any given parallel transport is,.or he can use general formulas worked out below.

Comparison by paralel transport is the foundation on which rests the gradient of a tensor field, VT. No mention of parallel transport was made in $\ S 3 . 5$ ，where the gradient was first defined, but parallel transport occurred implicitly: one defined $\yen 7$ in such a way that its components were $T ^ { \alpha } { } _ { \beta , \gamma } = \partial T ^ { \alpha } { } _ { \beta } / \partial x ^ { \gamma }$ [for $\pmb { \tau }$ a $\mathbf { \Sigma } ( _ { 1 } ^ { 1 } )$ tensor]; i.e., one asked $\yen 7$ to measure how much the Lorentz-frame components of $\pmb { \tau }$ change from point to point. But“no change in Lorentz components”would have meant “parallel transport,” so one was implicitly asking for the change in $\pmb { \tau }$ relative to what $\pmb { \tau }$ would have been after pure parallel transport.

To codify in abstract notation this concept pf differentiation,proceed as follows. First define the “covariant derivative” $\yen 1$ of $\pmb { \tau }$ along a curve $\mathcal { P } ( \lambda )$ , whose tangent vector is $\pmb { \mu } = d \mathcal { P } / d \lambda$ ：

$$
( \nabla _ { u } T ) _ { \mathrm { a t } \mathcal { P } ( 0 ) } = \operatorname* { l i m } _ { \varepsilon \to 0 } \left\{ \frac { T [ \mathcal { P } ( \varepsilon ) ] _ { \mathrm { p a r a l l e l - t r a n s p o r t e d t o } \mathcal { P } ( 0 ) } - T [ \mathcal { P } ( 0 ) ] } { \varepsilon } \right\} .
$$

Gradient defined

(See Figure 8.2 for the special case where $\pmb { \tau }$ is a vector field ${ \pmb v } .$ ）Then define $\yen 7$ to be the linear machine,that gives $\yen 1$ when $\pmb { u }$ is inserted into its last slot:

$$
\pmb { \nabla } \pmb { \tau } ( . \dots , . \dots , \pmb { u } ) \equiv \pmb { \nabla } _ { \pmb { u } } \pmb { \tau } .
$$

The result is the same animal ("gradient") as was defined in $\ S 3 . 5$ (for proof see exercise 8.8). But this alternative definition makes clear the relationship to parallel transport, including the fact that

In a local Lorentz frame,the components of $\yen 7$ are directional derivatives of the components of T: $T ^ { \beta } { } _ { \alpha , \gamma } ,$ Not so in a general basis. If $\{ \pmb { e } _ { \beta } ( \mathcal { P } ) \}$ is a basis that varies arbitrarily but smoothly from point to point, and $\{ \pmb { \omega } ^ { \pmb { \alpha } } ( \mathcal { P } ) \}$ is its dual basis, then $\pmb { \nabla } \pmb { T } = \pmb { \nabla } ( T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } )$ will contain contributions from $\bigtriangledown e _ { \beta }$ and $\yen 40$ , as well as from $\nabla { T ^ { \beta } } _ { \alpha } \equiv { \bf { d } } T ^ { \beta } { } _ { \alpha } = T ^ { \beta } { } _ { \alpha , \gamma } \pmb { \omega } ^ { \gamma } { } $

To quantify the contributions from $\triangledown _ { \pmb { \theta } _ { \beta } }$ and $\yen 40$ ,i.e.,to quantify the twisting, turning,expansion,and contraction of the basis vectors and 1-forms,one defines "connection coefficients":

![](images/949aa0130233846b2081f9a8add92c5ebf85326e2a3800c460dc7f48d6e15430.jpg)  
Figure 8.2. Definition of the covariant derivative $\cdots$ of a vector field ${ \pmb v }$ along a curve ${ \mathcal { P } } ( \lambda )$ ， with tangent vector $\pmb { \upsilon } \equiv d \vartheta / d \lambda$ ：（l） choose a point ${ \mathcal { P } } ( 0 )$ on the curve,at which to evaluate $\yen 1$ (2)Choose a nearby point $\mathcal { P } ( \varepsilon )$ on the curve.(3） Parallel-transport ${ \pmb v } [ \mathcal { P } ( \varepsilon ) ]$ along the curve back to ${ \mathcal { P } } ( 0 )$ ，getting the vector ${ \pmb v } _ { \mathrm { i i } } [ \pmb { \mathcal { P } } ( \pmb { \varepsilon } ) ] .$ (4）Take the difference $\delta \pmb { v } \equiv \pmb { v } _ { \nparallel } [ \mathcal { P } ( \varepsilon ) ] - \pmb { v } [ \mathcal { P } ( 0 ) ] .$ (5）Then $\yen 1$ is defined by

$$
\begin{array} { r } { \pmb { \nabla _ { \pmb { u } } } \pmb { v } \equiv \mathrm { \small ~ L i m ~ } \frac { \delta \pmb { v } } { \varepsilon } = \mathrm { \small ~ L i m ~ } \bigg \{ \frac { \pmb { v } _ { \mathrm { i i } } [ \pmb { \mathcal { S } } ( \varepsilon ) ] - \pmb { v } [ \pmb { \mathcal { S } } ( 0 ) ] } { \varepsilon } \bigg \} . } \end{array}
$$

$$
\begin{array} { r l } & { \Gamma ^ { \alpha } { } _ { \beta \gamma } \equiv \langle \boldsymbol { \omega } ^ { \alpha } , \boldsymbol { \nabla } _ { \gamma } \pmb { e } _ { \beta } \rangle \qquad \left[ \begin{array} { l } { \mathrm { N o t e ~ r e v e r s a l ~ o f ~ } \beta \mathrm { ~ a n d ~ } \gamma \mathrm { ~ t o ~ m a k e ~ t h e } } \\ { \mathrm { d i f f e r e n t i a t i n g ~ i n d e x ~ c o m e ~ l a s t ~ o n ~ } T } \end{array} \right] } \\ &  \qquad \quad \begin{array} { r l } & { \qquad \quad \begin{array} { r l } & { } \\ & { \qquad \mathrm { ~ \left[ i m e ^ \alpha \mathbf { v } _ { \it \alpha \gamma } \right] ~ } } \end{array} } \\ & { \qquad = \left( \begin{array} { l } { \alpha \mathrm { ~ c o m p o n e n t ~ o f ~ c h a n g e ~ i n ~ } \pmb { e } _ { \beta } , \mathrm { ~ r e l a t i v e } } \\ { \mathrm { t o ~ p a r a l l e l ~ t r a n s p o r t , ~ a l o n g ~ } \pmb { e } _ { \gamma } } \end{array} \right) , } \end{array} \end{array}
$$

and one proves (exercise 8.l2) that

$$
\langle \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = - { \Gamma ^ { \alpha } } _ { \beta \gamma } .
$$

In terms of these coefficients and

$$
{ T ^ { \beta } } _ { \alpha , \gamma } \equiv \nabla _ { \gamma } { T ^ { \beta } } _ { \alpha } \equiv \partial _ { \pmb { \theta } _ { \gamma } } { T ^ { \beta } } _ { \alpha } \equiv \partial _ { \gamma } { T ^ { \beta } } _ { \alpha } ,
$$

thecomponentsofthegradienteoted $T ^ { \beta } { } _ { \alpha ; \gamma } ,$

Components of gradient in arbitrary frame

$$
T ^ { \beta } { } _ { \alpha ; \gamma } = T ^ { \beta } { } _ { \alpha , \gamma } + T ^ { \beta } { } _ { \mu \gamma } T ^ { \mu } { } _ { \alpha } - T ^ { \mu } { } _ { \alpha \gamma } T ^ { \beta } { } _ { \mu }
$$

(see exercise 8.13). If the basis at the event where $\yen 7$ is calculated were a local Lorentz frame,the components of Twould just be T.Because it is not,one must correct this “Lorentz-frame”value for the twisting,turning,expansion, and contraction of the basis vectors and l-forms. The $^ { \mathfrak { s } } T T ^ { \mathfrak { s } }$ terms in equation (8.21) are the necessary corrections-one for each index of $\pmb { \tau } .$ The pattern of these correction terms is easy to remember: (l) $" + "$ sign if index being corrected is up, $^ { 6 6 } - { } ^ { 5 9 }$ sign if it is down; (2) differentiation index ( $\langle \gamma$ in above case) always at end of $\boldsymbol { r }$ ； (3) index being corrected ( $\beta$ in first term, $\pmb { \alpha }$ in second） shifts from $T$ onto $\boldsymbol { r }$ and gets replaced on $T$ by a dummy summation index $( \mu )$

Knowing the components (8.21) of the gradient, one can calculate the components of the covariant derivative $\yen 1$ by a simple contraction into $u ^ { \gamma }$ [see equation (8.17):

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { T } = ( T ^ { \beta } { } _ { \alpha ; \gamma } u ^ { \gamma } ) \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } . } \end{array}
$$

Components of covariant derivative

When $\pmb { u }$ is the tangent vector to a curve $\mathcal { P } ( \lambda ) , \pmb { \upsilon } = d \mathcal { P } / d \lambda$ ,one uses the notation $D T ^ { \beta } { } _ { \alpha } / d \lambda$ for the components of $\yen 1$

$$
\begin{array} { r l } & { \frac { D T ^ { \beta } _ { \alpha } } { d \lambda } \equiv T ^ { \beta } _ { \alpha ; \gamma } u ^ { \gamma } \overset { \_ } { = } T ^ { \beta } _ { \alpha ; \gamma } \frac { d x ^ { \gamma } } { d \lambda } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

The“”in $T ^ { \beta } { } _ { \alpha ; \gamma }$ reminds one to correct $T ^ { \beta } { } _ { \alpha , \gamma }$ with $^ { 6 6 } T T ^ { \prime \prime }$ terms; similarly, the “D” in $D T ^ { \beta } { } _ { \alpha } / d \lambda$ reminds one to correct $d T ^ { \beta } { } _ { \alpha } / d \lambda$ with $^ { 6 6 } T ^ { 7 }$ terms.

Calculation of connection coefficients from metric and commutators

This is all well and good, but how does one find out the connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ foragivenbasisThe answer isderivedinexercise8.15.Itsays: (1)taketh metric coeficients in the given basis; (2)calculate their directional derivatives along the basis directions

$$
\begin{array} { l l } { { g _ { \beta \gamma , \mu } \equiv \partial _ { \mu } g _ { \beta \gamma } \ } } & { { = \partial g _ { \beta \gamma } / \partial x ^ { \mu } ; } } \\ { { \uparrow \ } } & { { \uparrow \ \mathrm { [ i f ~ a ~ c o o r d } } } \end{array}
$$

(3) calculate the commutation coefficients of the basis [equations (8.14) in general; $c _ { \mu \beta \gamma } = 0$ in special case of coordinate basis]; (4) calculate the “covariant connection coefficients"

$$
\begin{array} { c } { { { \cal T } _ { \mu \beta \gamma } = \displaystyle \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } + \underbrace { c _ { \mu \beta \gamma } + c _ { \mu \gamma \beta } - c _ { \beta \gamma \mu } } _ { \displaystyle \mathrm { \large \large \displaystyle \frac { 1 } { 2 } } } ; } } \\ { { \mathrm { \smallskip \displaystyle \ z e o r d i n a t e \ b a s i s } } } \end{array}
$$

(5）raise an index to get the connection coefficients:

$$
\begin{array} { r } { T ^ { \alpha } { } _ { \beta \gamma } = g ^ { \alpha \mu } { \cal T } _ { \mu \beta \gamma } . } \end{array}
$$

[Note on terminology: a coordinate basis always has $c _ { \alpha \beta \gamma } = 0$ , and is sometimes called holonomic; a noncoordinate basis always has some of its $c _ { \alpha \beta \gamma }$ nonzero, and is sometimes called anholonomic. In the holonomic case, the connection coefficients are sometimes called Christoffel symbols.]

The component notation, with its semicolons, commas, $D$ 's, connection coefficients, etc. looks rather formidable at first. But it bears great computational power,one discovers as one proceeds deep into gravitation theory; and its rules of manipulation are simple enough to be learned easily. By contrast, the abstract notation $( \boldsymbol { \nabla } \pmb { \tau } , \pmb { \nabla } _ { \pmb { u } } \pmb { T } ,$ etc.)is poorly suited to complex calculations; but it possesses great conceptual power.

This contrast shows clearly in the way the two notations handle the concept of geodesic.A geodesic of spacetime is a curve that is straight and uniformly parametrized,as measured in each local Lorentz frame along its way. If the geodesic is timelike,then it is a possible world line for a freely falling particle,and its uniformly ticking parameter $\lambda$ (called“affine parameter") is a multiple of the particle's proper time, $\lambda = a \tau + b$ .(Principle of equivalence: test particles move on straight lines in local Lorentz frames,and each particle's clock ticks at a uniform rate as measured by any Lorentz observer.） This definition of geodesic is readily translated into abstract, coordinate-free language: a geodesic is a curve $\mathcal { P } ( \lambda )$ that parallel-transports its tangent vector $\pmb { \upsilon } = d \mathcal { P } / d \lambda$ along itself--

Geodesic and affine parameter defined

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 .
$$

(See Figure 10.1.) What could be simpler conceptually? But to compute the geodesic, given an initial event $\scriptstyle { \mathcal { P } } _ { o }$ and initial tangent vector $\pmb { u } ( \pmb { \mathcal { P } } _ { 0 } )$ there,one must use the component formalism. Introduce a coordinate system $x ^ { \alpha } ( { \mathcal { P } } )$ , in which $u ^ { \alpha } = d x ^ { \alpha } / d \lambda$ ， and write the component version of equation (8.25) as

$$
0 = { \frac { D ( d x ^ { \alpha } / d \lambda ) } { d \lambda } } = { \frac { d ( d x ^ { \alpha } / d \lambda ) } { d \lambda } } + \left( { T ^ { \alpha } } _ { \mu \gamma } { \frac { d x ^ { \mu } } { d \lambda } } \right) { \frac { d x ^ { \gamma } } { d \lambda } }
$$

[see equation (8.23), with one less index on $T ]$ ;i.e.,

$$
{ \frac { d ^ { 2 } x ^ { \alpha } } { d \lambda ^ { 2 } } } + { \Gamma ^ { \alpha } } _ { \mu \gamma } { \frac { d x ^ { \mu } } { d \lambda } } { \frac { d x ^ { \gamma } } { d \lambda } } = 0 .
$$

Geodesic equation

This geodesic equation can be solved (in principle) for the coordinates of the geodesic, $x ^ { \alpha } ( \lambda )$ ，when initial data $[ x ^ { \alpha }$ and $d x ^ { \alpha } / d \lambda$ at $\lambda = \lambda _ { 0 } ]$ have been specified.

The geodesics of the Earth's surface (great circles) are a foil against which one can visualize connection coefficients; see Figure 8.3.

The material of this section is presented more deeply and from a different view-point in Chapters l0 and 13. The Track-2 reader who plans to study those chapters is advised to ignore the following exercises. The Track-l reader who intends to skip Chapters 9-15 will gain necessary experience with the component formalism by working exercises 8.4-8.7. Less important to him, but valuable nonetheless,are exercises 8.8-8.15,which develop the formalism of covariant derivatives and connection coefficients in a systematic manner. The most important results of these exercises will be summarized in Box 8.6 (pages 223 and 224).

# ExerCiSe 8.4. PRACTICE IN WRITING COMPONENTS OF GRADIENT

Rewrite the following quantities in terms of ordinary derivatives $( f _ { . \gamma } \equiv \partial _ { e } f \equiv { \mathbf { v } } _ { \gamma } f )$ and $" T 7 "$ correction terms: (a) $T _ { \ ; \check { \check { Y } } }$ where $T$ is a function. (b) $T ^ { \alpha } { } _ { ; Y }$ where $\pmb { \tau }$ is a vector. (c) $T _ { \alpha ; \gamma }$ where $\pmb { \tau }$ is a 1-frm. (d) $T ^ { \alpha } { _ { \beta 8 } } ^ { \varepsilon } { _ { ; \gamma } } { \cdot }$ [Answer:

(a) $T _ { ; \gamma } = T _ { , \gamma } . \qquad ( { \mathsf { b } } ) \ T ^ { \alpha } { } _ { ; \gamma } = T ^ { \alpha } { } _ { , \gamma } + \Gamma ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } .$ (c） Ta;γ= Ta,y- Γ²aγTu.(d) $T ^ { \alpha } { } _ { \beta 8 } { } ^ { \varepsilon } { } _ { ; 7 } = T ^ { \alpha } { } _ { \beta 8 } { } ^ { \varepsilon } { } _ { ; 7 } + T ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta 8 } { } ^ { \varepsilon } - T ^ { \mu } { } _ { \beta \gamma } T ^ { \alpha } { } _ { \mu 8 } { } ^ { \varepsilon } - T ^ { \mu } { } _ { \delta \gamma } T ^ { \alpha } { } _ { \beta \mu } { } ^ { \varepsilon } + T ^ { \varepsilon } { } _ { \mu \gamma } T ^ { \alpha } { } _ { \beta 8 } { } ^ { \mu } { } .$

# EXERCISES

![](images/c4e807d7faad5206609287168bc7e886ddd3e2eae692ddd2275f4ebf9b39e611.jpg)  
Figure 8.3. The why of connection coeffcients,schematically portrayed. The aviator pursuing his great circle route from Peking to Vancouver finds himself early going north,butlater going south,although heis navigating the straightest route that is at all open to him (geodesic). The apparent change in direction indicates a turning,not in his route,but in the system of coordinates with respect to which his route is described. The vector $\pmb { v }$ of his velocity (a vector defined not on spacetime butrather on the Earth's two-dimensional surface),carried forward by parallel transport from an earlier moment to a later moment,finds itself in agreement with the velocity that he is then pursuing; or,in the abstract language of coordinate-free differential geometry,the covariant derivative $\yen 1$ vanishes along the route ("equation of a geodesic"). Though $\pmb { \nu }$ is in this sense constant,the individual pieces of which the navigator considers this vector to be built, $\pmb { \nu } = v ^ { \theta } \pmb { e } _ { \theta } + v ^ { \phi } \pmb { e } _ { \phi } ,$ are not constant.

In the language of components,the quantities $v ^ { \pmb { \theta } }$ and $v ^ { \phi }$ are changing along the route at a rate that annuls the covariant derivative of ${ \pmb v }$ thus

$$
\pmb { \nabla } _ { \pmb { v } } \pmb { v } = \pmb { a } = a ^ { \phi } \pmb { e } _ { \phi } + a ^ { \theta } \pmb { e } _ { \theta } = 0 ,
$$

or

$$
\begin{array} { c } { { 0 = a ^ { \theta } = \displaystyle \frac { d v ^ { \theta } } { d t } + \Gamma ^ { \theta } { } _ { m n } v ^ { m } v ^ { n } \mathrm { , } } } \\ { { 0 = a ^ { \phi } = \displaystyle \frac { d v ^ { \phi } } { d t } + \Gamma ^ { \phi } { } _ { m n } v ^ { m } v ^ { n } \mathrm { . } } } \end{array}
$$

In this sense the connection coefficients $T _ { ~ m n } ^ { j }$ serve as“turning coeficients” to tell how fast to“turn” the components of a vector in order to keep that vector constant (against the turning infuence of the base vectors).

Alternatively,the navigator can use an “automatic pilot system” which parallel-transports its own base vectors along the plane's route:

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \theta ^ { \prime } } = \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \phi ^ { \prime } } = 0 ; } \end{array}
$$

solid vectors at $\pmb { \mathcal { a } }$ become dotted vectors at $\clubsuit$ .Then the components of $\pmb { \nu }$ must be kept fixed to achieve a great-circle route,

$$
\frac { d v ^ { \theta ^ { \prime } } } { d t } = \frac { d v ^ { \phi ^ { \prime } } } { d t } = 0 ;
$$

and the turning coeficients are used to describe the turning of the lines of latitude and longitude relative to this parallel-transported basis:

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \theta } = \pmb { e } _ { m } \varGamma ^ { m } { } _ { \theta n } \upsilon ^ { n } , } \\ { \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \phi } = \pmb { e } _ { m } \varGamma ^ { m } { } _ { \phi n } \upsilon ^ { n } . } \end{array}
$$

Thesame turning coefficients enter into both viewpoints.The only difference is in how these coeffcients are used.

# Exercise 8.5. A SHEET OF PAPER IN POLAR COORDINATES

The two-dimensional metric for a flat sheet of paper in polar coordinates $( r , \theta )$ is $d s ^ { 2 } = d r ^ { 2 }$ $+ \ r ^ { 2 } d \phi ^ { 2 }$ -or,in modern notation, $g = d r \otimes d r + r ^ { 2 } d \phi \otimes d \phi$

(a)Calculate the connection coeffcients using equations (8.24).[Answer: $\begin{array} { r } { \hat { I } _ { \phi \phi } ^ { r } = - r ; } \end{array}$ $\begin{array} { r } { T _ { \tau \phi } ^ { \phi } = \bar { T } _ { \phi r } ^ { \phi } = 1 / r ; } \end{array}$ all othersvanish.]

(b) Write down the geodesic equation in $( r , \phi )$ .coordinates. [Answer: $d ^ { 2 } r / d \lambda ^ { 2 } -$ $r ( d \phi / d \lambda ) ^ { 2 } = 0$ ； $d ^ { 2 } \phi / d \lambda ^ { 2 } + ( 2 / r ) ( d r / d \lambda ) ( d \phi / d \lambda ) = 0 . ]$

(c） Solve this geodesic equation for $r ( \lambda )$ and $\phi ( \lambda )$ ,and show that the solution is a uniformly parametrized straight line $( x \equiv r \cos \phi = a \lambda + b$ for some $a$ and $b ; y \equiv r \sin \phi = j \lambda + k$ for some $j$ and $k$

(d) Verify that the noncoordinate basis $\pmb { e } _ { \hat { r } } \equiv \pmb { e } _ { r } = \partial \pmb { \mathcal { P } } / \partial r$ $\begin{array} { r } { \pmb { \mathscr { e } } _ { \hat { \phi } } \equiv r ^ { - 1 } \pmb { \mathscr { e } } _ { \phi } \quad r ^ { - 1 } \partial \pmb { \mathscr { P } } / \partial \phi , } \end{array}$ $\pmb { \omega } ^ { r } = \pmb { d r } , \pmb { \bar { \omega } } ^ { \hat { \phi } } = r \pmb { d \phi }$ is orthonormal,and that $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb { \sigma } } _ { \beta } \rangle = \delta ^ { \hat { \alpha } } { } _ { \beta }$ .Then calculate the connection coefficients of this basis from a knowledge [part (a)] of the connection of the coordinate basis. [Answer:

$$
\begin{array} { r l } & { \Gamma ^ { \hat { \phi } } { } _ { \hat { \phi } \hat { \mathbf { r } } } = \langle \boldsymbol { \omega } ^ { \hat { \phi } } , \boldsymbol { \Psi } _ { \hat { r } } \pmb { e } _ { \hat { \phi } } \rangle = \langle r d \phi , \boldsymbol { \Psi } _ { r } ( r ^ { - 1 } \pmb { e } _ { \phi } ) } \\ & { \quad \quad \quad = r \langle d \phi , ( \pmb { \Psi } _ { r } r ^ { - 1 } ) \pmb { e } _ { \phi } + r ^ { - 1 } ( \pmb { \Psi } _ { r } \pmb { e } _ { \phi } ) \rangle = r \langle d \phi , - r ^ { - 2 } \pmb { e } _ { \phi } \rangle + \langle d \phi , \pmb { \Psi } _ { r } \pmb { e } _ { \phi } \rangle } \\ & { \quad \quad \quad = \begin{array} { r } { - r ^ { - 1 } + \displaystyle \int ^ { \phi } { } _ { \phi r } = - r ^ { - 1 } + r ^ { - 1 } = 0 ; } \end{array} } \end{array}
$$

similarly, $\Gamma _ { . } ^ { \hat { \phi } } { } _ { \hat { \tau } \hat { \phi } } = + 1 / r , \Gamma _ { . } ^ { \hat { \tau } } { } _ { \hat { \phi } \hat { \phi } } = - 1 / r ;$ all others vanish.]

(e) Consider the Keplerian orbit of Figure 8.l and $\ S 8 . 3$ as a nongeodesic curve in the sun's two-dimensional,Euclidean, equatorial plane.In place of the old notation $d \nu / d t , d e _ { \hat { r } } / d t$ ， etc.,use the new notation $\pmb { \nabla } _ { \pmb { v } } \pmb { v } , \pmb { \nabla } _ { \pmb { v } } \pmb { e } _ { \hat { \tau } }$ ,etc.Then $\pmb { v } = d \mathcal { P } / d t$ is the tangent to the orbit,and $\ b { a } = \ b { \nabla } _ { \ b { v } } \ b { v }$ is the acceleration. Derive equations (8.4) for $a ^ { \dagger }$ and $a ^ { \hat { \phi } }$ using component manipulations and connection coefficients in the orthonormal basis.

# Exercise 8.6. SPHERICAL COORDINATES IN FLAT SPACETIME

The spherical noncoordinate basis $\left\{ \pmb { e } _ { \hat { \alpha } } \right\}$ of Exercise 8.1 was orthonormal, $g _ { \hat { \alpha } \hat { \beta } } = \eta _ { \hat { \alpha } \hat { \beta } }$ ，bu1 had nonvanishing commutation coefficients [part (c) of Exercise 8.2].

(a) Calculate the connection coefficients for this basis,using equations (8.24). [Answer:

$$
\begin{array} { r l } & { \Gamma ^ { \hat { \theta } } { } _ { \hat { r } \hat { \theta } } = \Gamma ^ { \hat { \phi } } { } _ { \hat { r } \hat { \phi } } = - \Gamma ^ { \hat { r } } { } _ { \hat { \theta } \hat { \theta } } = - \Gamma ^ { \hat { r } } { } _ { \hat { \phi } \hat { \phi } } = 1 / r ; } \\ & { \Gamma ^ { \hat { \phi } } { } _ { \hat { \theta } \hat { \phi } } = - \Gamma ^ { \hat { \theta } } { } _ { \hat { \phi } \hat { \phi } } = \cot \theta / r ; } \end{array}
$$

all others vanish.]

(b) Write down expressions for $\pmb { \nabla } _ { \hat { \pmb { \alpha } } } \pmb { e } _ { \hat { \pmb { \beta } } }$ in terms of $\pmb { e } _ { \hat { \gamma } } ,$ and verify the correctness of these expressions by drawing sketches of the basis vectors on a sphere of constant $t$ and $r .$ [Answer:

$$
\begin{array} { l l } { { \pmb { \nabla } _ { \hat { \theta } } \pmb { e } _ { \hat { r } } = r ^ { - 1 } \pmb { e } _ { \hat { \theta } } , } } & { { \pmb { \nabla } _ { \hat { \theta } } \pmb { e } _ { \hat { \theta } } = - r ^ { - 1 } \pmb { e } _ { \hat { r } } , \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { r } } = r ^ { - 1 } \pmb { e } _ { \hat { \phi } } , } } \\ { { \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \theta } } = ( \cot \theta / r ) \pmb { e } _ { \hat { \phi } } , } } & { { \pmb { \nabla } _ { \hat { \phi } } \pmb { e } _ { \hat { \phi } } = - r ^ { - 1 } \pmb { e } _ { \hat { r } } - ( \cot \theta / r ) \pmb { e } _ { \hat { \theta } } . } } \end{array}
$$

All others vanish.]

(c) Calculate the divergence of a vector, $\pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { \alpha } } { } _ { ; \hat { \pmb { \alpha } } } .$ in this basis.[Answer:

$$
\begin{array} { r l } & { \pmb { \nabla } \cdot \pmb { A } = A ^ { \hat { t } } , \hat { \pmb { \imath } } + r ^ { - 2 } ( r ^ { 2 } A ^ { \hat { \pmb { r } } } ) , \hat { \pmb { \imath } } + ( \sin \theta ) ^ { - 1 } ( \sin \theta A ^ { \hat { \theta } } ) , \hat { \pmb { \theta } } + A ^ { \hat { \phi } } , \hat { \pmb { \phi } } } \\ & { \quad \quad = \frac { \partial A ^ { \hat { t } } } { \partial t } + \frac { 1 } { r ^ { 2 } } \frac { \partial ( r ^ { 2 } A ^ { \hat { \tau } } ) } { \partial r } + \frac { 1 } { r \sin \theta } \frac { \partial ( \sin \theta A ^ { \hat { \theta } } ) } { \partial \theta } + \frac { 1 } { r \sin \theta } \frac { \hat { c } A ^ { \hat { \phi } } } { \hat { c } \phi } . } \end{array}
$$

This answer should be familiar from flat-space vector analysis.]

# Exercise 8.7. SYMMETRIES OF CONNECTION COEFFICIENTS

Fromequation (8.24b),thesymmetryof temetrcandtheantisymetry $( c _ { \beta \gamma \mu } = - c _ { \gamma \beta \mu } )$

of the commutation_coeffcients. show that: $T _ { \alpha 1 \beta \gamma 1 } = 0$ (last two indices are symmetric) in a coordinate basis: $I _ { ( \hat { \alpha } \hat { \beta } ) \hat { \gamma } } = 0$ (first two indices are antisymmetric) in a globally orthonormal basis,gaβ = naβ

# SYSTEMATIC DERIVATION OF RESULTS IN S8.5

# ExerciSe 8.8. NEW DEFINITION OF VT COMPARED WITH OLD DEFINITION

The new definition of $\yen 7$ is given by equations (8.16) and (8.17). Use the fact that parallel transport keeps local-Lorentz components fixed to derive,from (8.16),the Lorentz-frame equation $\pmb { \nabla _ { \pmb { u } } } \pmb { \bar { T } } = T ^ { \beta } { } _ { \alpha , \gamma } u ^ { \gamma } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha }$ :From this and equation (8.17), infer that the Lorentzframe components of $\yen 7$ are $T ^ { \beta } { } _ { \alpha , \gamma }$ --which accords with the old definition of $\forall \pmb { \tau } .$

# Exercise 8.9. CHAIN RULE FOR $\pmb { \nabla _ { \pmb { u } } } \pmb { \tau }$

(a)Use calculations in'a local Lorentz frame to show that $\because \check { \pmb { \triangledown } } _ { \pmb { \Uparrow } } ^ { \pmb { \Uparrow } }$ obeys the standard chain rule for derivatives:

$$
\nabla _ { u } ( f A \otimes B ) = ( \nabla _ { u } f ) A \otimes B + f ( \nabla _ { u } A ) \otimes B + f A \otimes ( \nabla _ { u } B ) .
$$

Here $\pmb { A }$ and $\pmb { B }$ are arbitrary vectors,1-forms,or tensors;and $f$ is an arbitrary function.[Hint: assume for concreteness that $\pmb { A }$ is a (） tensor and $\pmb { B }$ is a vector. Then this equation reads, in Lorentz-frame component notation,

$$
( f A ^ { \alpha } { } _ { \beta } B ^ { \gamma } ) _ { , \delta } u ^ { \delta } = ( f _ { , \delta } u ^ { \delta } ) A ^ { \alpha } { } _ { \beta } B ^ { \gamma } + f ( A ^ { \alpha } { } _ { \beta , \delta } u ^ { \delta } ) B ^ { \gamma } + f A ^ { \alpha } { } _ { \beta } ( B ^ { \gamma } { } _ { , \delta } u ^ { \delta } ) .
$$

(b) Rewrite equation (8.27) in component notation in an arbitrary basis. [Answer: same as (8.27'), except “,” is replaced everywhere by ";". But note that $f _ { \bar { s } } \bar { u } ^ { \bar { s } } = f _ { , \bar { s } } u ^ { \bar { s } }$ , because the function $f$ "has no components to correct".]

# Exercise 8.10. COVARIANT DERIVATIVE COMMUTES WITH CONTRACTION

(a) Let $\pmb { S }$ be a $\left( { } _ { 2 } ^ { 1 } \right)$ tensor, Using components in a local Lorentz frame show that

$\pmb { \nabla } _ { \pmb { u } }$ (contraction on slots l and 2 of $\pmb { S } ) =$ (contraction on slots l and 2 of $\yen 5$

[Hint: in a local Lorentz frame this equation makes the trivial statement

$$
\biggl ( \sum _ { \alpha } S _ { \alpha \beta } ^ { \alpha } \biggr ) _ { , \gamma } u ^ { \gamma } = \sum _ { \alpha } ( S _ { \alpha \beta , \gamma } ^ { \alpha } u ^ { \gamma } ) . ]
$$

Exercise 8.11. ALGEBRAIC PROPERTIES OF $\blacktriangledown$

Use calculations in a local Lorentz frame to show that

$$
\pmb { \nabla } _ { a \pmb { u } + b \pmb { v } } \pmb { S } = a \pmb { \nabla } _ { \pmb { u } } \pmb { S } + b \pmb { \nabla } _ { \pmb { v } } \pmb { S }
$$

for all tangent vectors ${ \pmb u } , { \pmb v }$ and numbers $a , b$ ; also that

$$
\pmb { \nabla _ { \pmb { u } } } ( \pmb { S } + \pmb { M } ) = \pmb { \nabla _ { \pmb { u } } } \pmb { S } + \pmb { \nabla _ { \pmb { u } } } \pmb { M }
$$

for any two tensor fields $\pmb { s }$ and $\pmb { M }$ of the same rank;also that

![](images/667e2aea5a26c6d23f1f6eabfc377ddb022b39e6851de4a83a8448e33a187f40.jpg)

for any two vector fields $\pmb { u }$ and ${ \pmb w } .$

# Exercise 8.12. CONNECTION COEFFICIENTS FOR 1-FORM BASIS

Show that the same connection coefficients $\Gamma ^ { \alpha } { } _ { \beta \ Y }$ that describe the changes in $\{ \pmb { e } _ { \beta } \}$ from point to point [definition (8.19a)] also describe the changes in $\{ \pmb { \omega } ^ { \alpha } \}$ , except for a change in sign [equation (8.19b)]. {Answer: (1) $\langle { \pmb { \omega } } ^ { \alpha } , { \pmb e } _ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta }$ is a constant function (O or l, depending on whether $\alpha = \beta \mathrm { \hbar }$ .(2)Thus, $\pmb { \nabla } _ { \gamma } \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = \partial _ { \pmb { e } _ { \gamma } } \langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle = 0 .$ (3)But $\langle \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle$ is the contraction of $\pmb { \omega } ^ { \alpha } \otimes \pmb { e } _ { \beta } ,$ so equation (8.28) implies $0 = \check { \Psi } _ { \boldsymbol { \ Y } }$ (contraction of $\pmb { \omega } ^ { \alpha } \otimes \pmb { \mathscr { e } } _ { \beta } )$ $=$ contraction of $[ \pmb { \nabla } _ { \gamma } ( \pmb { \omega } ^ { \alpha } \otimes \pmb { e } _ { \beta } ) ]$ (4)Apply the chain rule (8.27) to conclude ${ \boldsymbol { 0 } } =$ contraction of $[ ( \nabla _ { \gamma } \omega ^ { \alpha } ) \otimes \pmb { e } _ { \beta } + \pmb { \omega } ^ { \alpha } \otimes ( \dot { \nabla } _ { \gamma } \pmb { e } _ { \beta } ) ] = \langle \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } , \pmb { e } _ { \beta } \rangle + \langle \pmb { \omega } ^ { \alpha } , \pmb { \nabla } _ { \gamma } \pmb { e } _ { \beta } \rangle$ (5）Finally，use definition (8.l9a) to arrive at the desired result,(8.19b).)

# Exercise 8.13.‘ $. r { \boldsymbol { \tau } } ^ { \prime \prime }$ CORRECTION TERMS FOR $\pmb { T } ^ { \beta } { } _ { \alpha : \gamma }$

Derive equation (8.21) for $T ^ { \beta } { } _ { \alpha ; \gamma }$ in an arbitrary basis by first calculating the components of $\yen 1$ for arbitrary $\pmb { u }$ ,and by then using equation (8.17) to infer the components of $\yen 1$ [Answer: (l) Use the chain rule (8.27) to get

$$
\begin{array} { r l } & { \pmb { \nabla _ { u } T } = \pmb { \nabla _ { u } } ( T ^ { \beta } \pmb { \alpha _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } ) } \\ & { \quad \quad = ( \pmb { \nabla _ { u } T ^ { \beta } } \pmb { \alpha _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } + T ^ { \beta } \llcorner ( \pmb { \nabla _ { u } } \pmb { e _ { \beta } } ) \otimes \pmb { \omega ^ { \alpha } } + T ^ { \beta } \llcorner \pmb { e _ { \beta } } \otimes ( \pmb { \nabla _ { u } } \pmb { \omega ^ { \alpha } } ) . } \end{array}
$$

(2） Write $\pmb { u }$ in terms of its components, $\pmb { \mu } = \pmb { u } ^ { \gamma } \pmb { e } _ { \gamma }$ ；use linearity of $\pmb { \sigma } _ { \pmb { u } }$ in ${ \pmb u }$ from equation (8.29), to get $\begin{array} { r } { \pmb { \nabla _ { u } } = u ^ { \gamma } \pmb { \nabla _ { \gamma } } } \end{array}$ and use this in $\yen 1$

$$
\pmb { \nabla _ { u } T } = u ^ { \gamma } \{ T _ { \alpha , \gamma } ^ { \beta } \pmb { e _ { \beta } } \otimes \pmb { \omega ^ { \alpha } } + T _ { \alpha } ^ { \beta } ( \pmb { \nabla _ { \gamma } } \pmb { e _ { \beta } } ) \otimes \pmb { \omega ^ { \alpha } } + T _ { \alpha } ^ { \beta } \pmb { e _ { \beta } } \otimes ( \pmb { \nabla _ { \gamma } } \pmb { \omega ^ { \alpha } } ) \} .
$$

(3）Use equations $_ { ( 8 . 1 9 a , \mathbf { b } ) }$ ,rewritten as

$$
\begin{array} { r } { \pmb { \nabla } _ { \gamma } \pmb { e } _ { \beta } = { \Gamma ^ { \mu } } _ { \beta \gamma } \pmb { \theta } _ { \mu } , \qquad \pmb { \nabla } _ { \gamma } \pmb { \omega } ^ { \alpha } = - { \Gamma ^ { \alpha } } _ { \mu \gamma } \pmb { \omega } ^ { \mu } , } \end{array}
$$

to put $\yen 1$ in the form

$$
\pmb { \nabla _ { \pmb { \mu } } } \pmb { T } = u ^ { \gamma } \{ T ^ { \beta } { } _ { \alpha , \gamma } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } + T ^ { \mu } { } _ { \beta \gamma } T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \mu } \otimes \pmb { \omega } ^ { \alpha } - T ^ { \alpha } { } _ { \mu \gamma } T ^ { \beta } { } _ { \alpha } \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \mu } \} .
$$

(4)Rename dummy indices so that the basis tensor ${ \pmb e } _ { \beta } \otimes { \pmb \omega } ^ { \alpha }$ can be factored out:

$$
\pmb { \nabla _ { u } } \pmb { T } = u ^ { \gamma } \{ T ^ { \beta } { } _ { \alpha , \gamma } + \bar { T ^ { \beta } } { } _ { \mu \gamma } T ^ { \mu } { } _ { \alpha } - \bar { T ^ { \mu } } { } _ { \alpha \gamma } T ^ { \beta } { } _ { \mu } \} \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } .
$$

(5）By comparison with

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { T } = \pmb { \nabla } \pmb { T } ( \dots , \dots , \dots , \pmb { u } ) = ( T ^ { \beta } { } _ { \alpha ; \gamma } u ^ { \gamma } ) \pmb { e } _ { \beta } \otimes \pmb { \omega } ^ { \alpha } , } \end{array}
$$

read of the value of $T ^ { \beta } { } _ { \alpha ; \gamma \cdot 1 }$

# Exercise 8.14. METRIC IS COVARIANTLY CONSTANT

Show on physical grounds (using properties of local Lorentz frames) that

$$
{ \pmb { \bigtriangledown } } \pmb { \bigtriangledown } = 0
$$

or,equivalently, that $\pmb { \bigtriangledown _ { u } } \pmb { g } = 0$ for any vector $\pmb { u }$ .Then deduce as a mathematical consequence the obviously desirable product rule

$$
\nabla _ { \boldsymbol { u } } ( A \cdot B ) = ( \nabla _ { \boldsymbol { u } } A ) \cdot B + A \cdot ( \nabla _ { \boldsymbol { u } } B ) .
$$

[Answer:(l) As discussed following equation (8.18), the components of $\yen 9$ in a local Lorentz frame are $g _ { \mu \nu , \alpha }$ Just use $\pmb { \mathscr { g } }$ for $\pmb { \tau }$ in that discusion. But these components allvanish by equation (8.15b). Therefore equation (8.33) holds in this frame,and-as a tensor equation-in all frames.(2） The product rule is also a tensor equation, true immediately via components in a local Lorentz frame.(3) Prove the product rule also the hard way,to see where equation (8.33) enters.Use the chain rule of exercise 8.9 to write

$$
\begin{array} { c } { { \pmb { \nabla _ { u } } ( g \otimes A \otimes B ) = ( \pmb { \nabla _ { u } } g ) \otimes A \otimes B + g \otimes ( \pmb { \nabla _ { u } } A ) \otimes B } } \\ { { + \pmb { g } \otimes A \otimes ( \pmb { \nabla _ { u } } B ) . } } \end{array}
$$

Use equation (8.33） to drop one term,then contract, forming

$$
\pmb { A } \cdot \pmb { B } = \mathrm { c o n t r a c t i o n } \left( \pmb { g } \otimes \pmb { A } \otimes \pmb { B } \right)
$$

and the other inner products. Exercise 8.1O is used to justify commuting the contraction with $\pmb { \sigma } _ { \pmb { u } }$ on the lefthand side.l

# Exercise 8.15. CONNECTION COEFFICIENTS IN TERMS OF METRIC

Use the fact that the metric is covariantly constant [equation (8.33)] to derive equation (8.24b) for the connection coeffcients. Treat equation (8.24c) as a definition of $\Gamma _ { \mu \beta \gamma }$ in terms of $\boldsymbol { T } ^ { \alpha } { } _ { \beta \boldsymbol { Y } } .$ [Answer: (l) Calculate the components of $\yen 9$ in an arbitrary frame:

$$
\begin{array} { r } { g _ { \alpha \beta ; \gamma } = 0 = g _ { \alpha \beta , \gamma } - { \Gamma ^ { \mu } } _ { \alpha \gamma } g _ { \mu \beta } - { \Gamma ^ { \mu } } _ { \beta \gamma } g _ { \mu \dot { \alpha } } } \\ { \equiv g _ { \alpha \beta , \gamma } - { \Gamma } _ { \beta \alpha \gamma } - { \Gamma } _ { \alpha \beta \gamma } ; \qquad } \end{array}
$$

thereby conclude that $g _ { \alpha \beta , \gamma } = 2 { \Gamma } _ { ( \alpha \beta ) \gamma } .$ (Round brackets denote symmetric part.) (2) Construct the metric terms in theclaimed answer for Pμpy:

$$
\begin{array} { r l } & { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - g _ { \beta \gamma , \mu } ) = { \cal T } _ { ( \mu \beta ) \gamma } + { \cal T } _ { ( \mu \gamma ) \beta } - { \cal T } _ { ( \beta \gamma ) \mu } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } - { \cal T } _ { \beta \mu } ) } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta , \gamma } + g _ { \mu \gamma , \beta } + { \cal T } _ { \mu \beta \gamma } + { \cal T } _ { \mu \gamma \beta } + { \cal T } _ { \gamma \mu \beta } - { \cal T } _ { \beta \gamma \mu } - { \cal T } _ { \gamma \beta \mu } ) } } \\ & { \phantom { \frac { 1 } { 2 } ( g _ { \mu \beta \gamma } + g _ { \mu \beta \gamma } + { \cal T } _ { \mu \beta \gamma } + { \cal T } _ { \beta [ \mu \gamma ] } + { \cal T } _ { \gamma [ \mu \beta ] } ) } } \end{array}
$$

(3）Infer fromequation (8.3l), with ${ \pmb u }$ and $\pmb { \nu }$ chosen as two basis vectors $\mathbf { \Omega } ( \pmb { u } = \pmb { e } _ { \mu } , \pmb { w } = \pmb { e } _ { \nu } ,$ 9 that

$$
c _ { \mu \nu } ^ { \rho } \pmb { e } _ { \rho } \equiv [ \pmb { e } _ { \mu } , \pmb { e } _ { \nu } ] = \pmb { \nabla } _ { \mu } \pmb { e } _ { \nu } - \pmb { \nabla } _ { \nu } \pmb { e } _ { \mu } = ( { T ^ { \rho } } _ { \nu \mu } - { T ^ { \rho } } _ { \mu \nu } ) \pmb { e } _ { \rho } = 2 { T ^ { \rho } } _ { [ \nu \mu ] } \pmb { e } _ { \rho } ;
$$

i.e.,

$$
{ \cal { T } ^ { \rho } } _ { [ \mu \nu ] } = - \mathrm { \frac { ~ 1 } { 2 ~ } } c _ { \mu \nu } { } ^ { \rho } ; \qquad \varGamma _ { \rho [ \mu \nu ] } = - \mathrm { \frac { ~ 1 } { 2 ~ } } c _ { \mu \nu \rho } .
$$

(4)This,combined with step (2) yields the desired formula for $\hat { I _ { \mu \beta \gamma ^ { \cdot } } } ]$

# $\$ 8.6$ :LOCAL LORENTZ FRAMES: MATHEMATICAL DISCUSSION

An observer falling freely in curved spacetime makes measurements in his local Lorentz frame.What he discovers has been discussed extensively in Parts Iand I of this book.Try now to derive his basic discoveries from the formalism of the last section.

Pick an event $\mathcal { P } _ { o }$ on the observer's world line.His local Lorentz frame there is a coordinate system $x ^ { \alpha } ( { \mathcal { P } } )$ in which

Local Lorentz frame:

$$
g _ { \alpha \beta } \equiv \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } \equiv \frac { \partial \mathcal { P } } { \partial x ^ { \alpha } } \cdot \frac { \partial \mathcal { P } } { \partial x ^ { \beta } } = \eta _ { \alpha \beta } \ \mathrm { a t } \ \mathcal { P } _ { o }
$$

(Lorentz metric at $\mathcal { P } _ { \pmb { \mathscr { o } } } )$ ,and in which

$$
\partial g _ { \alpha \beta } / \partial x ^ { \mu } = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { o }
$$

(metric as Lorentz as possible near $\mathcal { P } _ { \pmb { \mathscr { o } } }$ ). [See equation (8.15).] In addition,by virtue of equations (8.24),

$$
{ \varGamma ^ { \alpha } } _ { \beta \gamma } = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { o }
$$

(no “correction terms”in covariant derivatives). Of course, the observer must be at rest in his local Lorentz frame; i.e.,his world line must be

$$
x ^ { j } = x ^ { j } ( \mathcal { P } _ { o } ) = \mathrm { c o n s t a n t } ; \qquad x ^ { 0 } \mathrm { v a r y i n g } .
$$

Query:Equations (8.35) to (8.37) guarantee that the observer is at rest in a local Lorentz frame.Do they imply that he is freely falling?(They should!） Answer: Calculate the observer's 4-acceleration $\pmb { a } = d \pmb { u } / d \tau$ (notation of chapter $6 ) = \nabla _ { \mathbf { u } } \mathbf { u }$ (notation of this chapter). His 4-velocity, calculated from equation (8.37) is

Origin falls freely along a geodesic

$$
\begin{array} { r } { \pmb { \mu } = ( d x ^ { \alpha } / d \tau ) \pmb { e } _ { \alpha } = ( d x ^ { 0 } / d \tau ) \pmb { e } _ { 0 } = \pmb { e } _ { 0 } ; } \\ { \left[ \begin{array} { c } { \mathrm { b e c a u s e } \pmb { u } \mathrm { \ a n d \ } \pmb { e } _ { 0 } \mathrm { \ b o t h } } \\ { \mathrm { h a v e \ u n i t \ l e n g t h } } \end{array} \right] ^ { \dag } } \end{array}
$$

so his 4-acceleration is

$$
\begin{array} { r } { \pmb { a } = \pmb { \nabla } _ { \pmb { u } } \pmb { u } = \pmb { \nabla } _ { 0 } \pmb { e } _ { 0 } = { \Gamma } ^ { \alpha } _ { 0 0 } \pmb { e } _ { \alpha } } \\ { = 0 \mathrm { ~ a t ~ } \mathcal { P } _ { \hat { 0 } } . } \end{array}
$$

Thus, he is indeed freely falling $( \pmb { \mathscr { a } } = 0 )$ ; and he moves along a geodesice $( \nabla _ { \mathbf { \pmb { u } } } \pmb { \mu } = 0 )$ 1

Query: Do freely falling particles move along straight lines $( d ^ { 2 } x ^ { \alpha } / d \tau ^ { 2 } = 0 )$ inthe observer's local Lorentz frame at $\mathcal { P } _ { \pmb { \mathscr { o } } } \mathscr { ? }$ (They should!) Answer: A freely falling particle experiences zero 4-acceleration

Freely falling particles move on straight lines

$$
\begin{array} { r } { \pmb { a } _ { \mathrm { p a r t i c l e } } = \pmb { \nabla } _ { \pmb { u } _ { \mathrm { p a r t i c l e } } } \pmb { u } _ { \mathrm { p a r t i c l e } } = 0 ; } \end{array}
$$

i.e., it parallel-transports its 4-velocity; i.e., it moves along a geodesic of spacetime

with affine parameter equal to its proper time. The geodesic equation for its world line,in local Lorentz coordinates, says

$$
{ \begin{array} { r l } { { \frac { d ^ { 2 } x ^ { \alpha } } { d \tau ^ { 2 } } } = - { r ^ { \alpha } } _ { \mu \nu } { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } } \\ { \ } & { \ } \\ & { \qquad = 0 \ \mathrm { a t } \ { \mathcal { P } } _ { o } . } \end{array} }
$$

The particle's world line is, indeed, straight at $\mathcal { P } _ { o }$

Query:Does the freely falling observer Fermi-Walker-transport his spatial basis vectors $\bullet _ { j } .$ ：i.e.,can he attach them to gyroscopes that he carries? (He should be able to!) Answer: Fermi-Walker transport (Box 6.2) would say

$$
\begin{array} { r l r } { \frac { d \pmb { e } _ { j } } { d \tau } } & { { } \equiv } & { \pmb { \nabla } _ { \pmb { u } } \pmb { e } _ { j } = \pmb { u } ( \pmb { a } \cdot \pmb { e } _ { j } ) - \pmb { a } ( \pmb { u } \cdot \pmb { e } _ { j } ) . } \end{array}
$$

But $\pmb { u } = \pmb { e } _ { 0 } , \pmb { e } _ { 0 } \cdot \pmb { e } _ { j } = 0$ ,and ${ \pmb a } = 0$ for the observer; so Fermi-Walker transport in this case reduces to parallel transport along ${ \pmb { \theta } } _ { \mathbf { 0 } }$ : thus $\pmb { \bigtriangledown } _ { 0 } \pmb { \varrho } _ { j } = 0$ .This is,indeed, how $\pmb { e } _ { j }$ is transported through $\mathcal { P } _ { o }$ ,because

$$
\begin{array} { r } { \pmb { \nabla } _ { 0 } \pmb { e } _ { j } = { \cal T } ^ { \alpha } { } _ { j 0 } \pmb { e } _ { \alpha } = 0 \mathrm { a t } \mathcal { P } _ { o } . } \end{array}
$$

# \$8.7. GEODESIC DEVIATION AND THE RIEMANN CURVATURE TENSOR

“Gravitation is a manifestation of spacetime curvature, and that curvature shows up in the deviation of one geodesic from a nearby geodesic (relative acceleration of test particles).”To make this statement precise, first quantify the “deviation”or “relative acceleration” of neighboring geodesics.

Focus attention on a family of geodesics ${ \mathcal { P } } ( \lambda , n )$ ； see Figure 8.4. The smoothly varying parameter $\pmb { n }$ ("selector parameter") distinguishes one geodesic from the next. For fixed $_ n$ ， $\mathcal { P } ( \lambda , n )$ is a geodesic with affine parameter $\lambda$ and with tangent vector

$$
\pmb { \mu } = \hat { \sigma } \mathcal { P } / \hat { \partial } \lambda ;
$$

thus $\pmb { \bigtriangledown _ { \pmb { u } } } \pmb { u } = 0$ (geodesic equation). The vector

$$
\pmb { n } \equiv \partial \mathcal { P } / \partial n
$$

measures the separation between points with the same value of $\lambda$ on neighboring geodesics.

An observer falling freely along the“fiducial geodesic” $n = 0$ watches a test particle fall along the“test geodesic"” $n = 1$ . The velocity of the test particle relative to him he quantifies by $\yen 1$ ，This relative velocity, like the separation vector ${ \pmb n } ,$ ， is an arbitrary “initial condition.”Not arbitrary,however,is the “relative acceleration,” $\yen 1$ of the test particle relative to the observer (see Boxes I1.2 and 11.3). It would be zero in flat spacetime. In curved spacetime,it is given by

![](images/eec624dcfe9caf76ee09de7f33491625cecde122804216239382d9ad4064c903.jpg)  
Figure 8.4. A family of geodesics ${ \mathcal { P } } ( \lambda , n )$ 、The selector parameter $n$ tells“which”geodesic;the affine parameter $\lambda$ tells“where”on a given geodesic. The separation vector $\pmb { \eta } \equiv \hat { \sigma } ^ { \mathrm { s p } } / \partial n$ at a point $\mathcal { P } ( \lambda , 0 )$ along the fiducial geodesic, $n = 0$ ,reaches (approximately） to the point $^ { g p } ( \lambda , 1 )$ with the same value of $\lambda$ on the test geodesic, $n = 1$ 、

$$
\begin{array} { r } { \forall _ { u } \forall _ { u } n + R i e m a n n \left( . . . , u , n , u \right) = 0 , } \end{array}
$$

Riemann curvature tensor defined by relative acceleration of geodesics

or, in component notation,

$$
\frac { D ^ { 2 } n ^ { \alpha } } { d \lambda ^ { 2 } } + R ^ { \alpha } { } _ { \beta \gamma \delta } u ^ { \beta } n ^ { \gamma } u ^ { \delta } = 0 .
$$

This equation serves as a definition of the“Riemann curvature tensor;"and it can also be used to derive the following expressions for the components of Riemann ina coordinate basis:

Components of Riemann

$$
\begin{array} { r l } & { R ^ { \alpha } { } _ { \beta \gamma \delta } = \langle d x ^ { \alpha } , [ \Psi _ { \gamma } , \Psi _ { \delta } ] \pmb { e } _ { \beta } \rangle } \\ & { \quad \quad \quad = \frac { \partial { \cal T } ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } - \frac { \partial { \cal T } ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } + { \cal T } ^ { \alpha } { } _ { \mu \gamma } { \cal T } ^ { \mu } { } _ { \beta \delta } - { \cal T } ^ { \alpha } { } _ { \mu \delta } { \cal T } ^ { \mu } { } _ { \beta \gamma } . } \end{array}
$$

(For proof,read Box I1.4, Box l1.5.and exercise 11.3,in that order.) For a glimpse of the man who first analyzed the curvature of spaces with three and more dimensions, see Box 8.5.

Spacetime curvature causes not only geodesic deviation, but also route dependence in parallel transport (parallel transport around a closed curve changes a vector or tensor-Box l1.7)； it causes covariant derivatives to fail to commute equation (8.44)}; and it prevents the existence of a global Lorentz coordinate system (S11.5).

At first sight one might think Riemann has $4 \times 4 \times 4 \times 4 = 2 5 6$ independent components. But closer examination $( \ S 1 3 . 5 )$ reveals a variety of symmetries

$$
R _ { \alpha \beta \gamma \delta } = R _ { [ \alpha \beta ] [ \gamma \delta ] } = R _ { [ \gamma \delta ] [ \alpha \beta ] } , \qquad R _ { [ \alpha \beta \gamma \delta ] } = 0 , \qquad R _ { \alpha [ \beta \gamma \delta ] } = 0
$$

# Box 8.5 GEORG FRIEDRICH BERNHARD RIEMANN

September 17, 1826, Breselenz, Hanover-July 20, 1866, Selasca, Lake Maggiore

![](images/7d49a684eea05616c150f4d548a5b252b192295a8d0ce4b1f1e863bf77e6cc76.jpg)

With his famous doctoral thesis of l85l,“Foundations for a general theory of functions of a single complex variable,”Riemann founded one branch of modern mathematics (the theory of Riemann surfaces)；and with his famous lecture of three years later founded another (Riemannian geometry).These and other writings will be found in his collected works,edited by H. Weber (1953).

"The properties which distinguish space from other conceivable triply-extended magnitudes are only to be deduced from experience.... At every point the three-directional measure of curvature can have an arbitrary value if only the effective curvature of every measurable region of space does not differ noticeably from zero.”[G. F. B. Riemann,“On the hypotheses that lie at the foundations of geometry,”Habilitationsvorlesung of June 10,1854,on entry into the philosophical faculty of the University of Gotingen.]

Dying of tuberculosis twelve years later, occu-(antisymmetry on first two indices; antisymmetry on last two; -symmetry under exchange of first pair with last pair; vanishing of completely antisymmetric parts). These reduce Riemann (in four dimensions) from 256 to 20 independent components.

Besides these algebraic symmetries, Riemann possesses differential symmetries called “Bianchi identities,”

$$
R ^ { \alpha } { } _ { \beta [ \lambda \mu ; \nu ] } = 0 ,
$$

which have deep geometric significance (Chapter 15).

From Riemann one can form several other curvature tensors by contraction. The easiest to form are the “Ricci curvature tensor,”

pied with an attempt at a unified explanation of gravity and electromagnetism, Riemann communicated to Betti his system of characterization of multiply-connected topologies (which opened the door to the view of electric charge as “lines of force trapped in the topology of space"),making use of numbers that today are named after Betti but that are identified with a symbol, $R _ { n }$ ,that honors Riemann.

“A more detailed scrutiny of a surface might disclose that what we had considered an elementary piece in reality has tiny handles attached to it which change the connectivity character of the piece,and that a microscope of ever greater magnification would reveal ever new topological complications of this type,ad infinitum.The Riemann point of view allows, also for real space,topological conditions entirely different from those realized by Euclidean space.Ibelieve that only on the basis of the freer and more general conception of geometry which had been brought out by the development of mathematics during the last century,and with an open mind for the imaginative possibilities which it has revealed,can a philosophically fruitful attack upon the space problem be undertaken." H. Weyl (1949, p. 91).

“But...physicists were still far removed from such a way of thinking; space was still, for them, a rigid, homogeneous something,susceptible of no change or conditions. Only the genius of Riemann, solitary and uncomprehended,had already won its way by the middle of the last century to a new conception of space,in which space was deprived of its rigidity,and in which its power to take part in physical events was recognized as possible.” A.Einstein (1934,p. 68).

Riemann formulated the first known model for superspace (for which see Chapter 43),a superspace built,however, not of the totality of all 3- geometries with positive definite Riemannian metric (the dynamic arena of Einstein's general relativity), but-of all conformally equivalent closed Riemannian 2-geometries of the same topology, a type of superspace known today as Teichmüller space,for more on Riemann's contributions to which and the subsequent development of which, see the chapters by L. Bers and J. A. Wheeler in Gilbert and Newton (1970).

Ricci curvature tensor

$$
R _ { \mu \nu } \equiv R _ { ~ \mu \alpha \nu } ^ { \alpha } \stackrel { _ = } { _ \mathrm { \tiny ~ \left\{ ~ \right\} ~ } } r _ { ~ \mu \nu , \alpha } ^ { \alpha } - { \cal T } _ { ~ \mu \alpha , \cdot } ^ { \alpha } + { \cal T } _ { ~ \beta \alpha } ^ { \alpha } { \cal T } _ { ~ \mu \cdot } ^ { \beta } - { \cal T } _ { ~ \beta \nu } ^ { \alpha } { \cal T } _ { ~ \mu \alpha } ^ { \beta } ,
$$

and the“scalar curvature,"

Scalar curvature

$$
R \equiv R ^ { \mu } { } _ { \mu } .
$$

But of much greater geometric significance is the“Einstein curvature tensor”

Einstein curvature tensor

$$
{ G ^ { \mu } } _ { \nu } \equiv \frac { 1 } { 2 } \varepsilon ^ { \mu \alpha \beta \gamma } R _ { \beta \gamma } ^ { \rho \sigma } \frac { 1 } { 2 } \varepsilon _ { \nu \alpha \rho \sigma } = R ^ { \mu } _ { \nu } - \frac { 1 } { 2 } \delta ^ { \mu } _ { \nu } R .
$$

Of all second-rank curvature tensors one can form by contracting Riemann, only Einstein $= \pmb { G }$ retains part of the Bianchi identities (8.46): it satisfies

Contracted Bianchi identities

$$
{ \cal G } _ { ; \nu } ^ { \mu \nu } = 0 .
$$

For the beautiful geometric meaning of these “contracted Bianchi identities”("the boundary of a boundary is zero"), see Chapter 15.

Box 8.6 summarizes the above equations describing curvature,as well as the fundamental equations for covariant derivatives.

[The following exercises from Track 2 are appropriate for the Track-l reader who wishes to solidfy his understanding of curvature: 11.6,11.9,11.10,13.7-11,and 14.3.]

# Exercise 8.16. SOME USEFUL FORMULAS IN COORDINATE FRAMES

In any coordinate frame,define $g$ to be the determinant of the matrix $g _ { \alpha \beta }$ [equation 8.11] Derive the following relations,valid in any coordinate frame.

(a) Contraction of connection coefficients:

$$
{ \Gamma ^ { \alpha } } _ { \beta \alpha } = ( \ln \sqrt { - \cdot } g ) _ { , \beta } .
$$

[Hint: Use the results of exercise 5.5.]

(b） Components of Ricci tensor:

$$
R _ { \alpha \beta } = \frac { 1 } { \sqrt { - g } } ( \sqrt { - g } { \cal { \Gamma } } ^ { \mu } { } _ { \alpha \beta } ) _ { , \mu } - ( \ln \sqrt { - g } ) _ { , \alpha \beta } - { \cal { \Gamma } } ^ { \mu } { } _ { \nu \alpha } { \cal { T } } ^ { \nu } { } _ { \beta \mu } .
$$

(c) Divergence of a vector $A ^ { \alpha }$ or antisymmetric tensor $F ^ { \alpha \beta }$ ：

$$
{ A ^ { \alpha } } _ { ; \alpha } = { \frac { 1 } { \sqrt { - g } } } ( { \sqrt { - g } } A ^ { \alpha } ) _ { , \alpha } , { F ^ { \alpha \beta } } _ { ; \beta } = { \frac { 1 } { \sqrt { - g } } } ( { \sqrt { - g } } F ^ { \alpha \beta } ) _ { , \beta } .
$$

(d) Integral of a scalar field $\Psi$ Over the proper volume of a 4-dimensional region $\mathcal { V }$ ：

$$
\int _ { \mathcal { V } } \Psi d ( { \mathrm { p r o p e r ~ v o l u m e } } ) = \int _ { \mathcal { V } } \Psi { \sqrt { - g } } d t d x d y d z .
$$

[Hint: In a localLorentz frame, $d ( \mathrm { p r o p e r v o l u m e } ) = d t d \hat { x } d \hat { y } d \hat { z } ,$ Usea Jacobian to transform this volume element to the given coordinate frame,and prove from the transformation law

$$
g _ { \alpha \beta } = \frac { \partial x ^ { \hat { \mu } } } { \partial x ^ { \alpha } } \frac { \partial x ^ { \hat { \nu } } } { \partial x ^ { \beta } } \eta _ { \mu \nu }
$$

that the Jacobian is equal to ${ \sqrt { - g } } . ]$

Box 8.6 COVARIANT DERIVATIVE AND CURVATURE: FUNDAMENTAL EQUATIONS   

<table><tr><td>Entity</td><td>Abstract notation</td><td>Component notation</td></tr><tr><td>Covariant Derivative</td><td>Vut = vT(....... u)</td><td>Ta;yuY = DTB/dX (u=dp/d) dT +(TB,T-r'aT）uu d</td></tr><tr><td>algebraic properties (Exercise 8.11)</td><td>uf=auf= &lt;df,u) Vau+bvT =aT+ bT (S+M)=S+M</td><td>faua=fua TB(auY+bu）=TY +bTUY (s+M=S+M</td></tr><tr><td>chain rule</td><td>uw ~ ∀wu = [u,w] for u, w both vector fields (AB)=(A)B+A(B) fA)=(uSA+A</td><td>rP{μp]=- p[equation (8.34)] （AB)u²=AB;Buu+ABY:uu</td></tr><tr><td>Vu and contraction commute</td><td>(contraction of S) =(contraction of S)</td><td>（fAaB）uu=fABu+fAaB;uu (∑soay)u=∑(Sayixu) T ;μ α</td></tr><tr><td>*metric covariantly constant</td><td>Vug = 0</td><td>gaβ;yuY =0</td></tr><tr><td>Gradient</td><td>4T</td><td>TPa;y=TBay+reyTa- rαyTB</td></tr><tr><td>Connection Coefficients</td><td>raBy=&lt;w,eB） =-&lt;,ua,e&gt;</td><td>raBy=garμBy* FBy= 2(gupy+8uy.B-8u</td></tr><tr><td></td><td></td><td>+ Cμβγ +CμγB -CBγμ）* Cβyu= 8u = gμa&lt;wα,[eβ,eγl&gt;*</td></tr><tr><td>Local Lorentz frame at 90 Parallel trans- port</td><td>Vs = 0</td><td>Coordinate system with gμ(9）=nμ raBy(9）=0 SaB;uY =0</td></tr><tr><td>Entity</td><td colspan="2">Abstract notation Component noiation</td></tr><tr><td>Geodesic Equation</td><td>4uu = 0 Riemann (σ.C.A.B)三(σ.(A.B)C)</td><td>d²x/dx²+ r. (dxu/d)(dx/d)=0 in a coordinate basis</td></tr><tr><td>Riemann Curvature Tensor</td><td>(A.B)三[A:B-A.B) (not track-one formulas: see Chapter I1)</td><td>arags arBy RBy6 = 2xY ax + roμyrB-raur"BY in coordinate frame</td></tr><tr><td>Ricci Curvature Tensor</td><td>Ricci = contraction on slots land3ofRiemann</td><td>[see equation (l1.13) for formula in non- coordinate frame] Rμ=Rαμav=Ta-raa+raβrβup -rr in coordinate frame</td></tr><tr><td>*Curvature Scalar</td><td>R=(contraction of Ricci)</td><td>R= R</td></tr><tr><td>*Einstein Curvature Tensor</td><td>G = Ricci - gR</td><td>Gaβ= RaB-8aR Useful formulas for computing Gα&amp; (derived in §14.2): Go=-(R1212 + R223+ R3131）,</td></tr><tr><td></td><td></td><td>G1=-(RO²02 + R03+ R²323),</td></tr><tr><td>*Symmetries of Curvature Tensors</td><td></td><td>G1= R1020 + R1323, etc. Raβγ&amp;=R[aβ}ys]=R[γs]laβ},R[aβγs1=O,Ra[βγs=0 Rβ=R(aβ).Gaβ= G(aB)</td></tr><tr><td>Bianchi Identities</td><td></td><td>Rβ{x:x = 0</td></tr><tr><td>*Contracted Bianchi Identities</td><td></td><td>Ga=0</td></tr><tr><td>Geodesic Deviation</td><td>un+ Riemann(...,u.n,u) = 0</td><td>D²na +RaBy8uβnYu=0 d</td></tr><tr><td>Parallel Transport around closed</td><td>δA + Riemann (...A.u,v) = 0 if u,v are edges of curve</td><td>SAα+RαBy8AβuYu=0</td></tr></table>

\*If metric is absent,these starred formulas cannot be formulated.Allother formulas are valid in absence of metric.

# CHAPTER 9

# DIFFERENTIAL TOPOLOGY

In analytic geometry,many relations which are independent of any frame must be expressed with respect to some particular frame.It is therefore preferable to devise new methods  
methods which lead directly to intrinsic properties without any mention of coordinates. The development of the topology of   
general spaces and of the objects which occur in them,as well as the development of the geometry of general metric spaces, are steps in this direction.

KARL MENGER，in Schilpp (1949)，p. 467.

# $\$ 9.1$ .GEOMETRIC OBJECTS IN METRIC-FREE, GEODESIC-FREE SPACETIME

Curved spacetime without metric or geodesics or parallel transport, i.e.,“differential topology,” is the subject of this easy chapter. It is easy because all the necessary geometric objects (event, curve,vector, l-form, tensor) are already familiar from flat spacetime. Yet it is also necessary, because one's viewpoint must be refined when one abandons the Lorentz metric of flat spacetime.

# Events

The primitive concept of an event $\mathscr { P }$ (Figure 1.2) needs no refinement. The essential property here is identifiability,which is not dependent on the Lorentz metric structure of spacetime.

This chapter is entirely Track 2. It depends on no preceding   
Track-2 material. It is needed as preparation   
for (1） Chapters 10-13 (differential geometry; Newtonian gravity). and (2) Box 30.1 (mixmaster cosmology). It will be helpful in (1）Chapter 14 (calculation of curvature) and in (2)Chapter 15(Bianchi identities).

Metric is abandoned

Geometric concepts must be refined

# Curves

Again no refinement.A“curve” $\mathcal { S } ( \lambda )$ is also too primitive to care whether spacetime has a metric-except that, with metric gone, there is no concept of “proper length" along the curve. This is in accord with Newton's theory of gravity,where one talks of the lengths of curves in “space,” but never in “spacetime."

# Vectors

Here refinement is needed.In special relativity one could dress primitive ("identifiable")events in enough algebraic plumage to talk of vectors as differences $\mathcal { P } - \mathcal { Q }$ between“algebraic” events. Now the plumage is gone,and the old bilocal("point for head and point for tail") version of a vector must be replaced by a purely local version $( \ S 9 . 2 )$ . Also vectors cannot be moved around; each vector must be attached to a specific event $\mathfrak { S 8 9 . 2 }$ and 9.3).

# 1-Forms

Almost no refinement needed, except that, with metric gone,there is no way to tell which l-form corresponds to a given vector (no way to raise and lower indices), and each 1-form must be atached to a specific event (89.4).

# Tensors

Again almost no refinement, except that each slot of a tensor is specific: if it accepts vectors, then it cannot accommodate l-forms,and conversely (no raising and lowering of indices); also, each tensor must be attached to a specific event (89.5).

# $\$ 9.2$ ."VECTOR" AND "DIRECTIONAL DERIVATIVE" REFINED INTO TANGENT VECTOR

Flat spacetime can accommodate several equivalent definitions of a vector (S2.3): a vector is an arrow reaching from an event $\mathcal { P } _ { 0 }$ to an event $\mathcal { Q } _ { 0 } ;$ it is the parameterized straight line, $\mathcal { P } ( \lambda ) = \mathcal { P } _ { 0 } + \lambda ( \mathcal { Z } _ { 0 } - \mathcal { P } _ { 0 } )$ extending from $\mathcal { P } _ { 0 }$ at $\lambda = 0$ to $\mathcal { Q } _ { 0 }$ at $\lambda = 1$ ； it is the rate of change of the point $\mathcal { P } ( \lambda )$ with increasing $\lambda .$ $d \mathcal { P } / d \lambda$

Old definitions of vector break down when metric is abandoned

With Lorentz metric gone, the“arrow” definition and the“parametrized-straight line”definition must break down.By what route is the arrow or line to be laid out between $\mathcal { P } _ { 0 }$ and $\boldsymbol { \mathcal { Q } } _ { 0 } \boldsymbol { ? }$ There is no concept of straightness; all routes are equally straight or bent.

Such fuzziness forces one to focus on the “rate-of-change-of-point-along-curve”

![](images/0e7c4b061b20f8a3b6dd3843bc64d9bfbec44d54539f0b136d47403bc099deb6.jpg)  
Box 9.1 TANGENT VECTORS AND TANGENT SPACE

A tangent vector $d \mathcal { P } / d \lambda$ is defined to be “the limit, when $N \longrightarrow \infty$ ，of $N$ times the displacement of $\mathcal { S }$ as $\lambda$ ranges from O to $1 / N$ ”One cannot think of this final displacement $d \mathcal { P } / d \lambda$ as lying in spacetime; fuzziness forbids (no concept of straightness). Instead,one visualizes $d \mathcal { P } / d \lambda$ as lying in a“tangent plane”or “tangent space,”which makes contact with spacetime only at ${ \mathcal { P } } ( 0 )$ ,the event where $d \mathcal { P } / d \lambda$ is evaluated. All other tangent vectors at ${ \mathcal { P } } ( 0 ) { - } \mathrm { e . g . } , d { \mathcal { P } } / d \rho , d { \mathcal { P } } / d \eta , d { \mathcal { P } } / d \xi .$ -lie in this same tangent space.

To make precise these concepts of tangent space and tangent vector,-one may regard spacetime as embedded in a flat space of more than four dimensions. One can then perform the limiting process that leads to $d \mathcal { P } / d \lambda ,$ ,using straight arrows in the flat embedding space.The result is a higherdimensional analog of the figure shown above.

But such a treatment is dangerous. It suggests, falsely，that the tangent vector $d \mathcal { P } / d \lambda$ and the tangent space at $\mathcal { P } _ { 0 }$ depend on how the embedding is done,or depend for their existence on the embedding process. They do not. And to make clear that they do not is one motivation for defining the directional derivative operator $" d / d \lambda "$ to be the tangent vector, rather than using Cartan's more pictorial concept $" d \mathcal { P } / d \lambda "$ 、

definition, $d \mathcal { P } / d \lambda$ . It, under the new name“tangent vector,”is explored briefly in $\ B \circ \mathbf { x } \ 9 . 1$ ,and in greater depth in the following paragraphs.

Even $" d \varphi / d \lambda "$ is a fuzzy definition of tangent vector, most mathematicians would argue.More acceptable,they suggest, is this definition: the tangent vector u to $\pmb { a }$ curve $\mathcal { P } ( \lambda )$ is the directional derivative operator along that curve

$$
\pmb { \upsilon } = \partial _ { \pmb { u } } = ( d / d \lambda ) _ { \mathrm { a l o n g c u r v e } } ,
$$

Best new definition:"'tangent vector equals directional derivative operator" $\pmb { u } = \pmb { d } / d \lambda$

Tangent vector equals directional derivative operator? Preposterous! A vector started out as a happy, irresponsible trip from $\mathcal { P } _ { 0 }$ to ${ \mathcal { Q } } _ { 0 }$ It ended up loaded with the social responsibility to tell how something else changes at $\mathcal { P } _ { 0 }$ At what point did the vector get saddled with this unexpected load? And did it really change its character all that much,as it seems to have done? For an answer, go back and try

Alternative definition, $\pmb { \upsilon } = d \hat { \mathscr { P } } / d \lambda$ ，requires embedding in flat space of higher dimensionality

to redo the “rate-of-change-of-point” definition, $d \mathcal { P } / d \lambda$ ,in the form of a limiting process:

0.Choose a curve $\mathcal { P } ( \lambda )$ whose tangent vector $d \mathscr { s p } / d \lambda$ at $\lambda = 0$ is desired. 1. Take the displacement of $\mathcal { P }$ as $\lambda$ ranges from O to l; that is not $d \mathscr { o } ^ { \flat } / d \lambda$ 、 2.Take twice the displacement of $\mathcal { S }$ as $\lambda$ ranges from 0 to $\scriptstyle { \frac { 1 } { 2 } } ;$ that is not $d ^ { \boldsymbol { o } \vec { p } } / d \lambda$ $N _ { \ast }$ Take $N$ times the displacement of $\mathscr { P }$ as $\lambda$ ranges from O to $1 / N ;$ that is not $d { \mathcal { P } } / d \lambda .$ $\infty$ . Take the limit of such displacements as $N \longrightarrow \infty$ ; that is $d ^ { \omega } / d \lambda$ 、

This definition has the virtue that $d \mathcal { P } / d \lambda$ describes the properties of the curve $\mathcal { P } ( \lambda )$ ， not over the huge range from $\lambda = 0$ to $\lambda = 1$ ,where the curve might be doing wild things,but only in an infinitesimal neighborhood of the point $\mathcal { P } _ { 0 } = \mathcal { P } ( 0 )$

The deficiency in this definition is that no meaning is assigned to steps $1 , 2 , \ldots$ $N , \ldots$ ， so there is nothing, yet, to take the limit of.To make each “displacement of ${ \mathcal { P } } ^ { * }$ a definite mathematical object in a space where “limit” has a meaning, one can imagine the original manifold to be a low-dimensional surface in some much higher-dimensional flat space.Then $\mathcal { P } ( 1 / N ) - \mathcal { P } ( 0 )$ is just a straight arrow connecting two points, i.e. a segment of a straight line,which,in general,will not lie in the surface itself-see Box 9.1.The resulting mental picture of a tangent vector makes its essential properties beautifully clear,but at the cost of some artifacts. The picture relies on a specific but arbitrary way of embedding the manifold of interest (metricfree spacetime) in an extraneous flat space.In using this picture,one must ignore everything that depends on the peculiarities of the embedding. One must think like the chemist, who uses tinkertoy molecular models to visualize many essential properties of a molecule clearly,but easily ignores artifacts of the model (colors of the atoms,diameters of the pegs, its tendency to collapse) that do not mimic quantummechanical reality.

Elie Cartan's approach to diferential geometry, including the $d \mathcal { P } / d \lambda$ idea of a tangent vector, suggests that he always thought of manifolds as embedded in flat spaces this way,and relied on insights that he did not always formalize to separate the essential geometry of these pictures from their embedding-dependent details. Acceptance of his methods of calculation came late.Mathematicians, who mistrusted their own ability to distinguish fact from artifact, exacted this price for acceptance: stop talking about the movement of the point itself,and start dealing only with concrete measurable changes that take place within the manifold, changes in any or all scalar functions $f$ as the point moves. The limiting process then reads:

0. Choose a curve $\mathcal { P } ( \lambda )$ whose tangent vector at $\lambda = 0$ is desired.   
1. Compute the number $f [ \mathcal { P } ( 1 ) ] - f [ \mathcal { P } ( 0 ) ] ,$ . which measures the change in $f$ as the point $\mathcal { P } ( \lambda )$ moves from $\mathcal { P } _ { 0 } = \mathcal { P } ( 0 )$ to $\mathcal { Q } _ { 0 } = \mathcal { P } ( 1 )$   
2. Compute $2 \{ f [ \mathcal { P } ( \vec { \mathfrak { g } } ) ] - f [ \mathcal { P } ( 0 ) ] \}$ , which is twice the change in $f$ as the point goes from ${ \mathcal { P } } ( 0 )$ to $\mathcal { P } ( \scriptstyle { \frac { 1 } { 2 } } )$   
N. Compute $N \{ f [ \mathcal { P } ( 1 / N ) ] - f [ \mathcal { P } ( 0 ) ] \}$ ，which is $N$ times the change in $f$ as the point goes from $\mathcal { P } ( 0 )$ to $\mathcal { P } ( 1 / N )$

$\infty$ 、 Same in the limit as $N \longrightarrow \infty$ : (change in $f ) = d f / d \lambda$

O. The vector is not itself the change in $f .$ It is instead the operation $d / d \lambda$ ,which, when applied to $f ,$ gives the change $d f / d \lambda$ Thus

$$
\mathsf { t a n g e n t \ v e c t o r = } d / d \lambda
$$

[cf. definition (9.1)].

The operation $d / d \lambda$ clearly involves nothing but the last steps $N \longrightarrow \infty$ in this limiting process, and only those aspects of these steps that are independent of $f .$ But this means it involves the infinitesimal displacements of the point $\mathcal { P }$ and nothing more.

One who wishes both to stay in touch with the present and to not abandon Cartan's deep geometric insight $( \mathbf { B o x } \ 9 . 1 )$ can seek to keep alive a distinction between:

(A） the tangent vector itself in the sense of Cartan, the displacement $d \mathcal { P } / d \lambda$ of a point;and   
(B) the “tangent vector operator,” or “directional derivative operator,” telling what happens to a function in this displacement: (tangent vector operator) $= d / d \lambda$

However,present practice drops (or, if one will,“slurs") the word“operator” in (B), and uses the phrase “tangent vector” itself for the operator,as will be the practice here from now on. The ideas (A) and (B) should also slur or coalesce in one's mind, so that when one visualizes an embedding diagram with arrows drawn tangent to the surface, one always realizes that the arrow characterizes an infinitesimal motion of a point $d \mathcal { P } / d \lambda$ that takes place purely within the surface,and when one thinks of a derivative operator $d / d \lambda$ , one always visualizes this same infinitesimal motion of a point in the manifold,a motion that must occur in constructing any derivative $d f ( \mathcal { P } ) / d \lambda$ 、 In this sense,one should regard a vector $d \mathcal { P } / d \lambda \equiv d / d \lambda$ as both“a displacement that carries attention from one point to another” and“a purely geometric object built on points and nothing but points.”

The hard-nosed physicist may still be inclined to say “Tangent vector equals directional derivative operator? Preposterous!” Perhaps he will be put at ease by another argument. He is asked to pick an event ${ \mathcal { P } } _ { 0 }$ 、At that event he chooses any set of four noncoplanar vectors (vectors defined in whatever way seems reasonable to him)；he names them $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ ；and he uses them as a basis on which to expand all other vectors at $\mathcal { P } _ { 0 }$ ：

$$
u = u ^ { \alpha } e _ { \alpha } , \qquad v = v ^ { \alpha } e _ { \alpha } .
$$

He is asked to construct the four directional derivative operators $\partial _ { \alpha } \equiv \partial _ { \pmb { \alpha } _ { r } }$ along his four basis vectors.As in flat spacetime, so also here; the same expansion coeffcients that appear in $\pmb { u } = \pmb { u } ^ { \alpha } \pmb { \mathcal { e } } _ { \alpha }$ also appear in the expansion for the directional derivative:

lsomorphism between directional derivatives and vectors

$$
\partial _ { \pmb { \omega } } = u ^ { \pmb { \alpha } } \partial _ { \alpha } , \partial _ { \pmb { \nu } } = v ^ { \pmb { \alpha } } \partial _ { \alpha } ,
$$

Hence,every relation between specific vectors at ${ \mathcal { P } } _ { 0 }$ induces an identical relation between their differential operators:

$$
\begin{array} { c } { { \pmb u = a \pmb w + b \pmb v \Longleftrightarrow u ^ { \alpha } = a w ^ { \alpha } + b v ^ { \alpha } } } \\ { { \Longleftrightarrow \partial _ { \pmb u } = a \partial _ { \pmb w } + b \partial _ { \pmb v } . } } \end{array}
$$

Tangent space defined

There is a complete “isomorphism” between the vectors and the corresponding directional derivatives. So how can the hard-nosed physicist deny the hard-nosed mathematician the right to identify completely each tangent vector with its directional derivative? No harm is done; no answer to any computation can be affected.

This isomorphism extends to the concept “tangent space."Because linear relations (such as $\hat { \partial } _ { \pmb { u } } = a \hat { \partial } _ { \pmb { w } } + b \hat { \partial } _ { \pmb { v } } )$ among directional derivatives evaluated at one and the same point ${ \mathcal { P } } _ { 0 }$ are meaningful and obey the usual addition and multiplication rules, these derivative operators form an abstract (but finite-dimensional) vector space called the tangent space at $\mathcal { P } _ { 0 }$ 、In an embedding picture (Box 9.1).one uses these derivatives (as operators in the flat embedding space) to construct tangent vectors $\pmb { u } = \hat { o } _ { \pmb { u } ^ { \pmb { \imath } } } s ^ { \ p }$ ， $\pmb { v } = \hat { \partial } _ { \pmb { v } } \mathcal { s } ^ { \dagger }$ ,in the form of straight arrows. Thereby one identifies the abstract tangent space with the geometrically visualized tangent space.

Coordinate-induced basis defined

# $\$ 9.3$ .BASES,COMPONENTS,AND TRANSFORMATION LAWS FOR VECTORS

An especially useful basis in the tangent space at an event $\mathcal { P } _ { 0 }$ is induced by any coordinate system [four functions, $x ^ { 0 } ( { \mathcal { P } } ) , x ^ { 1 } ( { \mathcal { P } } ) , x ^ { 2 } ( { \mathcal { P } } ) , x ^ { 3 } ( { \mathcal { P } } ) ]$ ：

$$
\begin{array} { r } { \pmb { e _ { 0 } } \equiv \left( \frac { \partial } { \partial x ^ { 0 } } \right) _ { x ^ { 1 } , x ^ { 2 } , x ^ { 3 } } = \left( \overset { \mathrm { d i r e c t i o n a l ~ d e r i v a t i v e ~ a l o n g ~ t h e } } { \mathrm { c u r v e ~ w i t h ~ c o n s t a n t ~ } } ( x ^ { 1 } , x ^ { 2 } , x ^ { 3 } ) \right) _ { \mathrm { a t } \mathcal { P } _ { 0 } } , } \end{array}
$$

$$
{ \pmb e } _ { 1 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 1 } } , \qquad e _ { 2 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 2 } } , \qquad e _ { 3 } = \frac { \hat { \partial } } { \hat { \partial } x ^ { 3 } } .
$$

Changes of basis: transformation matrices defined

(See Figure 9.1.)

A transformation from one basis to another in the tangent space at $\mathcal { P } _ { 0 } ,$ , like any change of basis in any vector space, is produced by a nonsingular matrix,

$$
{ \pmb e } _ { \alpha ^ { \prime } } = { \pmb e } _ { \beta } L ^ { \beta } { } _ { \alpha ^ { \prime } } \mathrm { ; }
$$

and,as always (including the Lorentz frames of flat spacetime), the components of a vector must transform by the inverse matrix

$$
u ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } u ^ { \beta } ;
$$

$$
\begin{array} { r } { \vert \vert L ^ { \alpha ^ { \prime } } { } _ { \beta } \vert \vert = \vert \vert L ^ { \beta } \gamma ^ { \vert \vert - 1 } , \mathrm { i . e . , } \left\{ \begin{array} { l l } { L ^ { \alpha ^ { \prime } } { } _ { \beta } L ^ { \beta } { } _ { \gamma } = \delta ^ { \alpha ^ { \prime } } { } _ { \gamma } , } \\ { L ^ { \delta } { } _ { \alpha ^ { \prime } } L ^ { \alpha ^ { \prime } } { } _ { \beta } = \delta ^ { \delta } { } _ { \beta } . } \end{array} \right. } \end{array}
$$

![](images/739f58fe0047b8197dcc869bd9801b1c076d1082ced40a0cb6fb7a6cd37e4a6d.jpg)  
Figure 9.1. The basis vectors induced,by a coordinate system,into the tangent space at each event.Here a truncated, two-dimensional spacetime is shown (two other dimensions suppressed),with coordinates $x ( \mathcal { P } )$ and ${ \dot { \psi } } ( { \mathcal { P } } )$ ，and with corresponding basis vectors $\partial / \partial x$ and $\partial / \partial \psi$

This “inverse” transformation law guarantees Compatibility between the expansions $\pmb { u } = \pmb { e } _ { \alpha ^ { \prime } } \pmb { u } ^ { \alpha ^ { \prime } }$ and $\pmb { \mu } = \pmb { \varrho } _ { \beta } \pmb { u } ^ { \beta }$ ：

$$
\begin{array} { r } { \pmb { u } = \pmb { e } _ { \alpha ^ { \prime } } u ^ { \alpha ^ { \prime } } = ( \pmb { e } _ { \gamma } L ^ { \gamma } { } _ { \alpha ^ { \prime } } ) ( L ^ { \alpha ^ { \prime } } { } _ { \beta } u ^ { \beta } ) = \pmb { e } _ { \gamma } \delta ^ { \gamma } { } _ { \beta } u ^ { \beta } } \\ { = \pmb { e } _ { \beta } u ^ { \beta } . \qquad } \end{array}
$$

In the special case of transformations between coordinate-induced bases, the transformation matrix has a simple form:

so

$$
{ \begin{array} { r } { { \frac { \partial } { \partial x ^ { \alpha ^ { \prime } } } } = { \frac { \partial x ^ { \beta } } { \partial x ^ { \alpha ^ { \prime } } } } { \frac { \partial } { \partial x ^ { \beta } } } ( { \mathrm { b y ~ u s u a l ~ r u l e s ~ o f ~ c a l c u l u s } } ) , } \\ { L ^ { \beta } _ { \alpha ^ { \prime } } = ( { \partial x ^ { \beta } } / { \partial x ^ { \alpha ^ { \prime } } } ) _ { \mathrm { a t e v e n t } { \mathcal { P } } _ { \mathrm { 0 } } { \mathrm { w h e r e } } \mathrm { t a n g e n t s p a c e l i e s } } . } \end{array} }
$$

(Note: this generalizes the Lorentz-transformation law $x ^ { \beta } = A ^ { \beta } { } _ { \alpha ^ { \prime } } x ^ { \alpha ^ { \prime } }$ ,which has the differential form $A ^ { \beta } { } _ { \alpha ^ { \prime } } = \partial x ^ { \beta } / \partial x ^ { \alpha ^ { \prime } }$ ; also,it provides a good way to remember the signs in the $\boldsymbol { A }$ matrices.)

# $\$ 9.4$ .1-FORMS

When the Lorentz metric is removed from spacetime, one must sharpen up the concept of a l-form $\pmb { \sigma }$ by insisting that it, like any tangent vector ${ \pmb u } .$ ，be attached to a specific event $\mathcal { P } _ { 0 }$ in spacetime. The family of surfaces representing $\pmb { \sigma }$ resides in the tangent space at $\mathcal { P } _ { 0 }$ ，not in spacetime itself. The piercing of surfaces of $\pmb { \sigma }$ by an arrow $\pmb { u }$ to produce the number $\langle \pmb { \sigma } , \pmb { u } \rangle$ ("bongs of bell"） occurs entirely in the tangent space.

![](images/06ff8084a06ccbc909e94440587c1fa25805a1acbfa28f6aef05f4fd79cfb873.jpg)  
Figure 9.2. The basis vectors ${ \pmb \theta } _ { \alpha }$ and dual basis l-forms $\pmb { \omega } ^ { \beta }$ in the tangent space of an event $\mathcal { G } _ { \mathfrak { o } } .$ The condition

$$
\langle { \pmb { \omega } } ^ { \beta } , { \pmb { \sigma } } _ { \alpha } \rangle = \delta _ { \alpha } ^ { \beta }
$$

dictates that the vectors $\pmb { e } _ { 2 }$ and ${ \pmb { \theta } } _ { 3 }$ lie parallel to the surfaces of $\pmb { \omega } ^ { 1 }$ ,and that $\pmb { \theta _ { 1 } }$ extend from one surface of $\pmb { \omega } ^ { 1 }$ to the next (precisely 1.0o surfaces pierced).

Notice that this picture could fit perfectly well into a book on $\mathbf { x }$ -raysand crystallography.There the vectors $\pmb { \theta _ { 1 } }$ ， $\pmb { e } _ { 2 }$ ， ${ \pmb \theta } _ { 3 }$ wouid be the edges of a unit cell of the crystal; and the surfaces of $\omega ^ { 1 } , \omega ^ { 2 }$ ， $\pmb { \omega } ^ { 3 }$ wouid be the surfaces of unit cells.Aiso,for an $\mathbf { x }$ -ray diffraction experiment,with waveiength of radiation and orientation of crystal appropriateiy adjusted, the successve surfaces of $\pmb { \omega } ^ { 1 }$ wouid produce Bragg reflection.For other choices of waveiength and orientation,the surfaces of $\scriptstyle { \pmb { \mu } } ^ { 2 }$ 0r $\pmb { \omega } ^ { 3 }$ wouid produce Bragg reflection.

Given any set of basis vectors $\{ \pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 } \}$ at an event ${ \mathcal { P } } _ { 0 } ,$ one constructs the "dual basis"of 1-forms $\{ { \pmb { \omega } } ^ { 0 } , { \pmb { \omega } } ^ { 1 } , { \pmb { \omega } } ^ { 2 } , { \pmb { \omega } } ^ { 3 } \}$ by choosing the surfaces of $\pmb { \omega } ^ { \beta }$ such that that

$$
\langle { \pmb { \omega } } ^ { \beta } , { \pmb e } _ { \alpha } \rangle = \delta ^ { \beta } { } _ { \alpha } .
$$

See Figure 9.2. A marvelously simple formalism for calculating and manipulating components of tangent vectors and 1-forms then results:

Component-manipulation formulas

$$
\begin{array} { c } { { u = e _ { \alpha } u ^ { \alpha } } } \\ { { \ } } \\ { { \sigma = \sigma _ { \beta } \omega ^ { \beta } } } \\ { { \ } } \\ { { u ^ { \alpha } = \langle { \omega ^ { \alpha } , u } \rangle } } \\ { { \ } } \\ { { \sigma _ { \beta } = \langle { \sigma , e _ { \beta } } \rangle } } \\ { { \ } } \\ { { \mathrm { : } \ u \rangle = \sigma _ { \alpha } u ^ { \alpha } } } \end{array}
$$

$$
\omega ^ { \alpha ^ { \prime } } = L ^ { \alpha ^ { \prime } } { } _ { \beta } \omega ^ { \beta }
$$

$$
\sigma _ { \alpha ^ { \prime } } = \sigma _ { \beta } L ^ { \beta } { } _ { \alpha ^ { \prime } }
$$

(Exercise 9.1 below justifies these equations.)

In the absence of a metric, there is no way to pick a specific 1-form $\widetilde { \pmb { u } }$ at an event $\mathcal { P } _ { 0 }$ and say that it corresponds to a specific tangent vector $\pmb { u }$ at $\mathcal { P } _ { 0 }$ . The correspondence set up in flat spacetime,

Correspondence between vectors and 1-forms rubbed out

$$
\langle \widetilde { \pmb { u } } , \pmb { v } \rangle = \pmb { u } \cdot \pmb { v } \qquad \mathrm { f o r ~ a l l ~ } \pmb { v } ,
$$

was rubbed out when “.” was rubbed out. Restated in component language: the raising of an index, $u ^ { \alpha } = \eta ^ { \alpha \beta } u _ { \beta }$ ,is impossible because the $\eta ^ { \alpha \beta }$ do not exist; similarly, lowering of an index, $u _ { \beta } = \eta _ { \beta \alpha } u ^ { \alpha }$ ,is impossible.

The l-form gradient df was introduced in $\ S 2 . 6$ with absolutely no reference to metric.Consequently,it and its mathematical formalism are the same here,without metric,as there with metric,except that, like all other l-forms, ${ \pmb d } { \pmb f }$ now resides in the tangent space rather than in spacetime itself. For example, there is no change in the fundamental equation relating the projection of the gradient to the directional derivative:

$$
\begin{array} { r } { \langle d f , \pmb { u } \rangle = \partial _ { \pmb { u } } f = \pmb { u } [ f ] . \qquad } \\  \bigg [ \mathrm { o l d ~ n o t a t i o n ~ f o r } \bigg ] \mathscr { \bigg { T } } \begin{array} { r } { \underline { { \operatorname { i } } } _ { \mathrm { r e w ~ n o t a t i o n } ; } } \\ { \underline { { \operatorname { i r e c t i o n } a 1 \mathrm { ~ d e r i v a t i v e } } } \end{array} } \end{array}
$$

Gradient of a function

Similarly,there are no changes in the component equations,

$$
\begin{array} { l l } { d f = f _ { , \alpha } \boldsymbol { \omega } ^ { \alpha } } & { ( \mathrm { e x p a n s i o n ~ o f ~ } d f \mathrm { i n ~ a r b i t r a r y } } \\ & { \mathrm { b a s i s } ) , } \\ { f _ { , \alpha } = \partial _ { \alpha } f = e _ { \alpha } [ f ] } & { ( \mathrm { w a y ~ t o ~ c a l c u l a t e ~ c o m p o n e n t s } } \\ & { \mathrm { o f ~ } d f ) , } \\ { f _ { , \alpha } = \partial f / \partial x ^ { \alpha } } & { \mathrm { i f ~ } \{ e _ { \alpha } \} \mathrm { ~ i s ~ a ~ c o r d i n a t e ~ b a s i s } , } \end{array}
$$

except that they work in arbitrary bases, not just in Lorentz bases.And,as in Lorentz frames,so also in general: the one-form basis $\{ d x ^ { \alpha } \}$ and the tangent-vector basis $\{ \hat { \boldsymbol { d } } / \hat { \boldsymbol { o } } \boldsymbol { x } ^ { \alpha } \}$ ， which are induced into a tangent space by the same coordinate system, are the duals of each other,

$$
\langle d x ^ { \alpha } , \partial / \partial x ^ { \beta } \rangle = \delta ^ { \alpha } { } _ { \beta } .
$$

(See exercise 9.2 for proofs.) Also,most aspects of Cartan's “Exterior Calculus"(parts A,B, C of Box 4.1) are left unaffected by the removal of metric.

# $\$ 9.5$ .TENSORS

A tensor S,in the absence of Lorentz metric,differs from the tensors of flat, Lorentz spacetime in two ways.(l) $\pmb { s }$ must reside at a specific event $\mathcal { P } _ { 0 }$ ,just as any vector or l-form must.(2) Each slot of $\pmb { s }$ is specific; it will accept either vectors or l-forms, but not both, because it has no way to convert a 1-form $\widetilde { \pmb { u } }$ into a“corresponding

Specificity of tensor slots

vector” $\pmb { u }$ as it sends $\widetilde { \pmb { u } }$ through its linear machinery. Thus,if $\pmb { s }$ is a $\textstyle { { \binom { 1 } { 2 } } }$ tensor

s(... ...）, insert 1-form here insert vector here insert vector here

then it cannot be converted alternatively to a $\textstyle { { \binom { 2 } { 1 } } }$ tensor, or a $( _ { 0 } ^ { 3 } )$ tensor, or a $( \mathbf { _ { 3 } ^ { 0 } } )$ tensor by the procedure of $\ S 3 . 2$ . In component language, the indices of $\pmb { S }$ cannot be raised and lowered.

Except for these two restrictions (attachment to a specific event; specificity of slots), a tensor $\pmb { s }$ is the same linear machine as ever.And the algebra of component manipulations is the same:

$$
\begin{array} { c } { { { \stackrel {  } { \pmb S } } = S ^ { \alpha } { } _ { \beta \gamma } { \pmb e } _ { \alpha } \stackrel {  } { \otimes } \tilde { \pmb { \omega } ^ { \beta } } \otimes { } \tilde { \pmb { \omega } ^ { \gamma } } , } } \\ { { { \pmb S } ( \pmb \sigma , u , v ) = S ^ { \alpha } { } _ { \beta \gamma } \sigma _ { \alpha } u ^ { \beta } v ^ { \gamma } . } } \end{array}
$$

# Exercise 9.1. COMPONENT MANIPULATIONS

Derive equations (9.1lc) through (9.1lg) from (9.10), (9.1la,b),(9.6), (9.7),and (9.8).

# Exercise 9.2. COMPONENTS OF GRADIENT, AND DUALITY OF COORDINATE BASES

In an arbitrary basis, define $f _ { , \alpha }$ by the expansion (9.13a). Then combine equations (9.1ld) and (9.12) to obtain the method (9.13b) of computing $f _ { , \alpha }$ Finally,combine equations (9.12) and (9.13b) to show that the bases $\{ d x ^ { \alpha } \}$ and $\left\{ \partial / \partial x ^ { \beta } \right\}$ are the duals of each other.

# ExerCise 9.3. PRACTICE MANIPULATING TANGENT VECTORS

Let $\mathscr { s } _ { \mathbf { 0 } }$ be the point with coordinates $( x = 0 , y = 1 , z = 0 )$ in a three-dimensional space; and define three curves through $\mathscr { P } _ { \mathbf { 0 } }$ by

$$
\begin{array} { r l } & { \mathcal { P } ( \lambda ) = ( \lambda , 1 , \lambda ) , } \\ & { \mathcal { S } ( \xi ) = ( \sin \xi , \cos \xi , \xi ) , } \\ & { \mathcal { S } ( \rho ) = ( \sinh \rho , \cosh \rho , \rho + \rho ^ { 3 } ) . } \end{array}
$$

(a） Compute $( d / d \lambda ) f , ( d / d \xi ) f ,$ and $( d / d \rho ) f$ for the function $f = x ^ { 2 } - y ^ { 2 } + z ^ { 2 }$ at the point $\mathscr { P } _ { \mathbf { 0 } } .$ (b) Calculate the components of the tangent vectors $d / d \lambda , d / d \boldsymbol { \xi }$ and $d / d \rho$ at $\mathcal { P } _ { \mathbf { 0 } } .$ using the basis $\{ { \partial } / { \partial x } ,  \partial / { \partial y } , \partial / { \partial z }  \}$ ·

# ExerCise 9.4. MORE PRACTICE WITH TANGENT VECTORS

In a three-dimensional space with coordinates $( x , y , z )$ ,introduce the vector field $v = y ^ { 2 }$ $\partial / \partial x - x \partial / \partial z$ ， and the functions $f = x y , g = z ^ { 3 }$ . Compute

$$
\begin{array} { c c }   ( a )  \begin{array} { c c } { { { \pmb v } [ { f } ] \quad } } & { { ( c ) { \pmb v } [ { f g } ] \quad } } \\ { { ( b ) { \pmb v } [ { g } ] \quad } } & { { ( d ) { \begin{array} { c c } { { f { \pmb v } [ { g } ] \quad } } & { { ( e ) { \pmb v } [ { f } ^ { 2 } + g ^ { 2 } ] } } \\ { { f { \pmb v } [ { g } ] - g { \pmb v } [ { f } ] \quad } } & { { ( f ) { \pmb v } \{ { \pmb v } [ { f } ] \} } } \end{array} } } } \end{array} \end{array}
$$

ExerCise 9.5. PICTURE OF BASIS 1-FORMS INDUCED BY COORDINATES In the tangent space of Figure 9.l, draw the basis l-forms $\pmb { d } \pmb { \psi }$ and $\pmb { d } \chi$ induced by the $\psi$ ， $x ^ { \cdot }$ coordinate system.

# Exercise 9.6. PRACTICE WITH DUAL BASES

In a three-dimensional space with spherical coordinates $r , \theta , \phi ,$ ,one often likes to use,instead of the basis $\partial / \partial r , \partial / \partial \theta , \partial / \partial \phi .$ the basis

$$
\pmb { e } _ { \hat { r } } = \frac { \hat { \partial } } { \partial r } , \qquad \pmb { e } _ { \hat { \theta } } = \frac { 1 } { r } \frac { \hat { \partial } } { \partial \theta } , \qquad \pmb { e } _ { \hat { \phi } } = \frac { 1 } { r \sin \theta } \frac { \hat { \partial } } { \partial \phi } .
$$

(a)What is the l-form basis $\{ \pmb { \omega } ^ { \hat { \tau } } , \pmb { \omega } ^ { \hat { \theta } } , \pmb { \omega } ^ { \hat { \phi } } \}$ dual to this tangent-vector basis? (b) On the sphere $r = 1$ ，draw pictures of the bases $\left\{ { \partial } / { \partial r } , \right. \partial / { \partial \theta } , \left. { \partial } / { \partial \phi } \right\}$ ， $\{ \pmb { e } _ { \hat { r } } , \pmb { e } _ { \hat { \theta } } , \pmb { e } _ { \hat { \phi } } \}$ ， $\{ d r , d \theta , d \phi \}$ ， and $\{ \pmb { \omega } ^ { \hat { r } } , \pmb { \omega } ^ { \hat { \theta } } , \pmb { \omega } ^ { \hat { \phi } } \}$

# S9.6. COMMUTATORS AND PICTORIAL TECHNIQUES

A vector ${ \pmb u } _ { 0 }$ given only at one point $\mathcal { P } _ { 0 }$ suffices to compute the derivative $\pmb { u } _ { 0 } [ f ] \equiv$ $\partial _ { { \pmb u } _ { 0 } } f ,$ which is simply a number associated with the point $\scriptstyle { \mathfrak { s p } } _ { 0 }$ . In contrast, a vector field $\pmb { u }$ provides a vector ${ \pmb u } ( { \mathcal { P } } )$ -which is a differential operator $\widehat { \partial } _ { \pmb { \omega } ( \mathfrak { s p } ) }$ -at each point $\mathcal { P }$ in some region of spacetime. This vector field operates on a function $f$ to produce not just a number, but another function $\pmb { u } [ f ] \equiv \partial _ { \pmb { u } } f .$ A second vector field $\pmb { \nu }$ can perfectly well operate on this new function, to produce yet another function

$$
{ \pmb v } \{ { \pmb u } [ f ] \} = \hat { \partial } _ { \pmb v } ( \hat { \partial } _ { \pmb u } f ) .
$$

Does this function agree with the result of applying ${ \pmb v }$ first and then ${ \pmb u } \mathrm { ? }$ Equivalently, does the“commutator”

$$
[ { \pmb u } , { \pmb v } ] [ f ] \equiv { \pmb u } \{ { \pmb v } [ f ] \} - { \pmb v } \{ { \pmb u } [ f ] \}
$$

vanish?

The simplest special case is when $\pmb { u }$ and $\pmb { \nu }$ are basis vectors of a coordinate system, $\pmb { \mu } = \hat { \partial } / \hat { \partial } x ^ { \alpha }$ ， $\pmb { v } = \partial / \partial x ^ { \beta }$ . Then the commutator does vanish, because partial derivatives always commute:

$$
[ \partial / \partial x ^ { \alpha } , \partial / \partial x ^ { \beta } ] [ f ] = \partial ^ { 2 } f / \partial x ^ { \beta } \partial x ^ { \alpha } - \partial ^ { 2 } f / \partial x ^ { \alpha } \partial x ^ { \beta } = 0 .
$$

But in general the commutator is nonzero,as one sees from a coordinate-based calculation:

$$
\begin{array} { c } { { \displaystyle { [ { \pmb u } , { \pmb v } ] } f = u ^ { \alpha } \frac { \hat { \partial } } { \partial x ^ { \alpha } } \left( v ^ { \beta } \frac { \hat { \partial } f } { \partial x ^ { \beta } } \right) - v ^ { \alpha } \frac \hat { \partial } { \hat { \sigma } x ^ { \alpha } } \left( u ^ { \beta } \frac { \hat { \partial } f } { \partial x ^ { \beta } } \right) } } \\ { { = \left[ ( u ^ { \alpha } v ^ { \beta } { } _ { , \alpha } - v ^ { \alpha } { u ^ { \beta } } _ { , \alpha } ) \frac \hat { \partial } { \partial x ^ { \beta } } \right] f . } } \end{array}
$$

Commutator of two vector fields isa vector field

Notice however, that the commutator $[ { \pmb u } , { \pmb v } ]$ like ${ \pmb u }$ and $\pmb { \nu }$ themselves,isa vector field,i.e., a linear differential operator at each event:

Commutator asa “closer of curves"

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } [ { \pmb v } ^ { \beta } ] - { \pmb v } [ { \pmb u } ^ { \beta } ] ) \frac { \hat { \partial } } { \partial { \pmb x } ^ { \beta } } = ( { \pmb u } ^ { \alpha } { \pmb v } ^ { \beta } , _ { \alpha } - v ^ { \alpha } { \pmb u } ^ { \beta } , _ { \alpha } ) \frac { \hat { \partial } } { \partial { \pmb x } ^ { \beta } } .
$$

Such results should be familiar from quantum theory's formalism for angular momentum operators (exercise 9.8).

The three levels of geometry-pictorial, abstract, and component-yield three different insights into the commutator.(l） The abstract expresion $[ { \pmb u } , { \pmb v } ]$ suggests the close connection to quantum theory,and brings to mind the many tools developed there for handling operators. But recall that the operators of quantum theory need not be first-order differential operators. The kinetic energy is second order and the potential is zeroth order in the familiar Schrodinger equation. Only first-order operators are vectors.(2)The component expression $u ^ { \alpha } v ^ { \beta } { } _ { , \alpha } - v ^ { \alpha } u ^ { \beta } { } _ { , \alpha } ,$ valid in any coordinate basis,brings the commutator into the reaches of the powerful tools of index mechanics. (3） The pictorial representation of $[ \pmb { u } , \pmb { v } ]$ $( { \tt B o x } \ 9 . 2 )$ reveals its fundamental role as a “closer of curves”-a role that willbe important in Chapter 1l's analysis of curvature.

Commutators find application in the distinction between a coordinate-induced basis, $\{ \pmb { e } _ { \alpha } \} = \{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \}$ ,and a noncoordinate basis. Because partial derivatives always commute,

# A. Pictorial Representation in Flat Spacetime

1. For ease of visualization, consider flat spacetime,so the two vector fields ${ \pmb u } ( { \mathcal { P } } )$ and ${ \pmb v } ( { \mathcal { P } } )$ can be laid out in spacetime itself.   
2. Choose an event ${ \mathfrak { s o } } _ { 0 }$ where the commutator $[ { \pmb u } , { \pmb v } ]$ is to be calculated.   
3. Give the names $\mathcal { P } _ { 1 } , \mathcal { P } _ { 2 } , \mathcal { P } _ { 3 } , \mathcal { P } _ { 4 }$ to the events pictured in the diagram.   
4. Then the vector $\mathcal { P } _ { 4 } - \mathcal { P } _ { 3 } ,$ which measures how much the four-legged curve fails to close, can be expressed in a coordinate basis as

![](images/8bf2c15d493349ec4b5a37ac9f8779bb55ba220e0c8bdb21f907097bd5797d4a.jpg)  
Box 9.2 THE COMMUTATOR AS A CLOSER OF QUADRILATERALS

$$
\begin{array} { r l } { \mathcal { S } _ { 4 } - \mathcal { S } _ { 3 } = [ \pmb { u } ( \mathcal { P } _ { 0 } ) + \pmb { v } ( \mathcal { P } _ { 1 } ) ] - [ \pmb { u } ( \mathcal { P } _ { 2 } ) + \pmb { v } ( \mathcal { P } _ { 0 } ) ] } & { } \\ { = [ \pmb { v } ( \mathcal { P } _ { 1 } ) - \pmb { v } ( \mathcal { P } _ { 0 } ) ] - [ \pmb { u } ( \mathcal { P } _ { 2 } ) - \pmb { u } ( \mathcal { P } _ { 0 } ) ] } & { } \\ { = ( v ^ { \beta } , \alpha ^ { u ^ { \alpha } } \pmb { e } _ { \beta } ) _ { \mathcal { S } _ { 0 } } - ( u ^ { \beta } , \alpha ^ { v ^ { \alpha } } \pmb { e } _ { \beta } ) _ { \mathcal { S } _ { 0 } } + \mathrm { ~ e r r o r s } } & { } \\ { = [ \pmb { u } , \pmb { v } ] _ { \mathcal { S } _ { 0 } } + \mathrm { ~ e r r o r s . } } & { } \\ { \qquad \quad \pmb { \mathrm { ~ \mathscr { L } _ { [ t e r m s ~ s u c h ~ a s ~ } } v ^ { \beta } } , _ { \mu ^ { \nu } } u ^ { \mu } u ^ { \nu } \pmb { e } _ { \beta } ] } \end{array}
$$

5. Notice that if u and v are halved everywhere, then [u,v] is cut down by a factor of 4, while the error terms in the above go down by a factor of 8. Thus, $[ \pmb { u } , \pmb { v } ]$ represents accurately the gap in the four-legged curve (“quadrilateral") in the limit where $\pmb { u }$ and $\pmb { \nu }$ are sufficiently short; i.e., $[ { \pmb u } , { \pmb v } ]$ "closes the quadrilateral”whose edges aie the vectors felds $\pmb { u }$ and $v .$

B. Pictorial Representation in Absence of Metric, or in Curved Spacetime with a Metric

![](images/489a97286ff6e8a1e68e5c7025d32b9260d64d497a702426ad238fe946ac211d.jpg)

1. The same picture must work, but now one dares not (at least initially)lay out the vector fields in spacetime itself. Instead one lays out two families of curves: the curves for which ${ \pmb u } ( { \mathcal { P } } )$ is the tangent vector; and the curves for which ${ \pmb v } ( \mathcal { P } )$ is the tangent vector.

2. The gap ${ } ^ { 6 6 } { \mathcal { P } } _ { 4 } - { \mathcal { P } } _ { 3 } { } ^ { \prime \prime }$ in the four-legged curve can be characterized by the difference $f ( \mathcal { P } _ { 4 } ) - f ( \mathcal { P } _ { 3 } )$ in the values of an arbitrary function at ${ \mathcal { P } } _ { 4 }$ and $\mathcal { P } _ { 3 }$ .That difference is,in a coordinate basis,

$$
\begin{array} { r c l } { { f ( \dot { \mathcal { S } } _ { 4 } ) - f ( \mathcal { S } _ { 3 } ) = \displaystyle \{ f ( \mathfrak { s } ^ { \rho } _ { 4 } ) - f ( \mathfrak { s } ^ { \rho } _ { 1 } ) \} } } & { { + } } & { { \displaystyle \{ f ( \mathfrak { s } ^ { \rho } _ { 1 } ) - f ( \mathfrak { s } ^ { \rho } _ { 0 } ) \} } } \\ { { \displaystyle \ } } & { { \displaystyle \left( f _ { , \alpha } \mathfrak { v } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { v } ^ { \alpha } \mathfrak { v } ^ { \beta } \right) _ { \varphi _ { 1 } } } } & { { \displaystyle \ \left( f _ { , \alpha } \mathfrak { u } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { u } ^ { \alpha } \mathfrak { u } ^ { \beta } \right) _ { \varphi _ { 0 } } } } \\ { { - \underbrace { [ f ( \mathfrak { s } ^ { \rho } _ { 2 } ) - f ( \mathfrak { s } ^ { \rho } _ { 0 } ) ] } _ { \displaystyle \left( f _ { , \alpha } \mathfrak { v } ^ { \alpha } + \frac { 1 } { 2 } f _ { , \alpha \beta } \mathfrak { v } ^ { \alpha } \mathfrak { v } ^ { \beta } \right) _ { \varphi _ { 0 } } } } } & { { - } } & { { \displaystyle \frac { [ f ( \mathfrak { s } ^ { \rho } _ { 3 } ) - f ( \mathfrak { s } ^ { \rho } _ { 2 } ) ] } { 2 } } } \end{array}
$$

$$
\begin{array} { r l } & { = [ ( u ^ { \beta } v ^ { \alpha } , _ { \beta } - v ^ { \beta } u ^ { \alpha } , _ { \beta } ) \partial f / \partial x ^ { \alpha } ] _ { \mathcal { S } _ { 0 } } + } \\ & { = \{ [ u , v \} [ f ] \} _ { \mathcal { S } _ { 0 } } + \cdots \mathrm { c u b i c ~ e r r o r s . } ^ { , , } } \end{array}
$$

Here “cubic errors” are cut down by a factor of 8,while $[ { \pmb u } , { \pmb v } ] f$ is cut down by one of 4,whenever ${ \pmb u }$ and $\pmb { \nu }$ are cut in half.

3.The result

$$
f ( \mathcal { P } _ { 4 } ) - f ( \mathcal { S } _ { 3 } ) = \{ { \boldsymbol { [ } \pmb { u } , \pmb { v } ] } [ f ] \} _ { \mathcal { S } _ { 0 } } + \mathrm { { ^ { * } c u b i c \ e r r o r s ^ { \prime } } }
$$

says that $[ { \pmb u } , { \pmb v } ]$ is a tangent vector at $\mathcal { P } _ { 0 }$ that describes the separation between the points $\mathcal { P } _ { 3 }$ and ${ \mathcal { P } } _ { 4 }$ .Its description gets arbitrarily accurate when $\pmb { u }$ and $\pmb { \nu }$ get arbitrarily short. Thus, $[ { \pmb u } , { \pmb v } ]$ closes the quadrilateral whose edges are the projections of $\pmb { u }$ and $\pmb { v }$ into spacetime.

# C． Philosophy of Pictures

1. Pictures are no substitute for computation. Rather, they are useful for (a) suggesting geometric relationships that were previously unsuspected and that one verifies subsequently by computation; (b) interpreting newly learned geometric results.

2.This usual noncomputational role of pictures permits one to be sloppy in drawing them. No essential new insight was gained in part B over part A, when one carefully moved the tangent vectors into their respective tangent spaces, and permitted only curves to lie in spacetime. Moreover, the original picture (part A) was clearer because of its greater simplicity.

3.This motivates one to draw “sloppy” pictures,with tangent vectors lying in spacetime itself-so long as one keeps those tangent vectors short and occasionally checks the scaling of errors when the lengths of the vectors are halved.

Conversely,if one is given a feld of basis vectors ("frame field") $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ ,but one does not know whether a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ exists in which $\{ \pmb { e } _ { \alpha } \} = \{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \}$ ， one can find out by a simple test: calculate all $( 4 \times 3 ) / 2 = 6$ commutators $[ e _ { \alpha } , e _ { \beta } ] ;$ if they al vanish,then there exists such a coordinate system. If not, there doesn't. Stated more briefly, $\{ \pmb { e } _ { \alpha } ( \mathcal { P } ) \}$ is a coordinate-induced basis if and only if $[ { \pmb e } _ { \alpha } , { \pmb e } _ { \beta } ] = 0$ for all ${ \pmb { e } } _ { \pmb { \alpha } }$ and $\pmb { e } _ { \beta }$ .(See exercise 9.9 for proof; see $\ S 1 1 . 5$ for an important application.) Coordinate-induced bases are sometimes called “holonomic.”In an “anholonomic basis” (noncoordinate basis), one defines the commutation coefficients ${ c _ { \mu \nu } } ^ { \alpha }$ by

Vanishing commutator:a test for coordinate bases

Commutation coefficients defined

$$
[ \pmb { e } _ { \mu } , \pmb { e } _ { \nu } ] = c _ { \mu \nu } ^ { \alpha } \pmb { e } _ { \alpha } .
$$

They enter into the component formula for the commutator of arbitrary vector felds ${ \pmb u }$ and $\pmb { \nu }$

$$
[ { \pmb u } , { \pmb v } ] = ( { \pmb u } [ { \pmb v } ^ { \beta } ] - { \pmb v } [ { \pmb u } ^ { \beta } ] + { \pmb u } ^ { \mu } { \pmb v } ^ { \nu } c _ { \mu \nu } ^ { \beta } ) { \pmb e } _ { \beta }
$$

(see exercise 9.10).

[Warning! In notation for functions and fields,mathematicians and physicists often use the same symbols to mean contradictory things. The physicist may write $\ell$ when considering the length of some critical component in an instrument he is designing, then switch to $\ell ( T )$ when he begins to analyze its response to temperature changes. Thus $\ell$ is a number, whereas $\ell ( T )$ is a function. The mathematician,in contrast, will write $f$ for a function that he may be considering as an element in some infinite-dimensional function space. Once the function is supplied with an argument, he then contemplates $f ( x )$ ,which is merely a number: the value of $f$ at the point $_ x$ .Caught between these antithetical rituals of the physics and mathematics sects, the authors have adopted a clear policy: vacilation. Usually physics-sect statements, like “On a curve $\mathcal { P } ( \lambda ) \ldots , \neg \ ,$ are used; and the reader can translate them himself into mathematically precise language: “Consider a curve $\mathcal { C }$ on which a typical point is ${ \mathcal { P } } = { \mathcal { C } } ( \lambda )$ ; on this curve ....” But on occasion the reader will encounter a pedantic-sounding paragraph written in mathematics-sect jargon (Example: Box 23.3). Such paragraphs deal with concepts and relationships so complex that standard physics usage would lead to extreme confusion. They also should prevent the reader from becoming so conditioned to physics usage that he is allergic to the mathematical literature,where great advantages of clarity and economy of thought are achieved by consistent reliance on wholly unambiguous notation.]

Physicists'notation vs. mathematicians'notation

# Exercise 9.7. PRACTICE WITH COMMUTATORS

Compute the commutator $[ e _ { \hat { \theta } } . e _ { \hat { \phi } } ]$ of the vector fields

$$
{ \pmb e } _ { \hat { \theta } } = \frac { 1 } { r } \frac { \partial } { \hat { c } \pmb \theta } , \qquad { \pmb e } _ { \hat { \phi } } = \frac { 1 } { r \sin \theta } \frac { \hat { c } } { \hat { c } \phi } .
$$

Express your result as a linear combination of $\pmb { \theta } _ { \pmb { \theta } }$ and $\pmb { e } _ { \hat { \phi } }$

# Exercise 9.8. ANGULAR MOMENTUM OPERATORS

In Cartesian coordinates of three-dimensional Euclidean space,one defines three “angularmomenium operalors"(vector fields) $\pmb { L _ { j } }$ by

$$
\pmb { L } _ { j } \equiv \epsilon _ { j k l } x ^ { k } ( \hat { c } / \hat { c } x ^ { l } ) .
$$

Draw a picture of these three vector fields. Calculate their commutators both pictorially and analytically.

# Exercise 9.9. COMMUTATORS AND COORDINATE-INDUCED BASES

Let $\pmb { u }$ and $\pmb { \nu }$ be vector fields in spacetime. Show that in some neighborhood of any given point there exists a coordinate system for which

$$
\pmb { \upsilon } = \hat { \varrho } / \hat { \varrho } x ^ { 1 } , \qquad \pmb { v } = \hat { \varrho } / \partial x ^ { 2 } ,
$$

if and only if $\pmb { u }$ and $\pmb { v }$ are linearly independent and commute:

$$
[ { \pmb u } , { \pmb v } ] = 0 .
$$

First make this result plausible from the second figure in $\tt B o x 9 . 2$ ； then prove it mathematically. Note: this result can be generalized to four arbitrary vector fields $e _ { 0 } , e _ { 1 } , e _ { 2 } ,$ $\pmb { e _ { 3 } }$ There exists a coordinate system in which $\pmb { e } _ { \alpha } = \hat { \partial } / \hat { \partial } x ^ { \alpha }$ if and only if $\pmb { e } _ { 0 } , \pmb { e } _ { 1 } , \pmb { e } _ { 2 } , \pmb { e } _ { 3 }$ are linearly independent and $[ { \pmb e } _ { \mu } , { \pmb e } _ { \nu } ] = 0$ for all pairs ${ \pmb \mathscr { e } } _ { \mu } , \pmb { \mathscr { e } } _ { \mathfrak { r } }$

# Exercise 9.1O. COMPONENTS OF COMMUTATOR IN NON-COORDINATE BASIS Derive equation (9.23).

# Exercise 9.11. LIE DERIVATIVE

The“Lie derivative” of a vector field ${ \pmb v } ( { \pmb \mathcal { P } } )$ along a vector field ${ \pmb u } ( { \pmb \mathcal { P } } )$ is defined by

$$
\pmb { \mathscr { L } } _ { \pmb { \mu } } \pmb { v } \equiv [ \pmb { u } , \pmb { v } ] .
$$

Draw a space-filling family of curves (a “congruence") on a sheet of paper. Draw an arbitrary vector $\pmb { v }$ at an arbitrary point $\mathcal { P } _ { \mathbf { 0 } }$ on the sheet. Transport that vector along the curve through $\scriptstyle { \mathcal { P } } _ { 0 }$ by means of the “Lie iransport law” $\pmb { \mathscr { L } _ { u } } \pmb { v } = 0$ ,where $\pmb { \mu } = d / d t$ is the tangent to the curve. Draw the resulting vector $\pmb { \nu }$ at various points $\mathcal { P } ( t )$ along the curve.

Exercise 9.12. A CHIP OFF THE OLD BLOCK (a) Prove the Jacobi identity

$$
[ { \pmb u } , [ { \pmb v } , { \pmb w } ] ] + [ { \pmb v } , [ { \pmb w } , { \pmb u } ] ] + [ { \pmb w } , [ { \pmb u } , { \pmb v } ] ] = 0
$$

by picking out all terms of the form $\hat { \partial } _ { \pmb { \mu } } \hat { \partial } _ { \pmb { \nu } } \hat { c } _ { \mathbf { w } } ,$ showing that they add to zero,and arguing from symmetry that all other terms, e.g., $\hat { c } _ { { \pmb w } } \hat { d } _ { \pmb { \mu } } \hat { d } _ { \pmb { v } }$ terms,must similarly cancel.

(b) State this identity in index form.   
(c) Draw a picture corresponding to this identity (see Box 9.2).

# $\$ 9.7$ .MANIFOLDS AND DIFFERENTIAL TOPOLOGY

Spacetime is not the only arena in which the ideas of this chapter can be applied. Points,curves,vectors, 1-forms,and tensors exist in any“differentiable manifold.”

Their use to study differentiable manifolds constitutes a branch of mathematics called "differential topology"-hence the title of this chapter.

The mathematician usually begins his development of differential topology by introducing some very primitive concepts, such as sets and topologies of sets, by building a fairly elaborate framework out of them,and by then using that framework to define the concept of a differentiable manifold. But most physicists are satisfied with a more fuzzy, intuitive definition of manifold: roughly speaking,an $\pmb { n }$ -dimensional differentiable manifold is a set of“points” tied together continuously and differentiably,so that the points in any sufficiently small region can be put into a one-to-one correspondence with an open set of points of $R ^ { n }$ · $[ R ^ { n }$ is the number space of $_ n$ dimensions,i.e., the space of ordered $\pmb { n }$ -tuples $( x ^ { 1 } , x ^ { 2 } , \ldots , x ^ { n } ) .$ ] That correspondence furnishes a coordinate system for the neighborhood.

Differentiable manifold "defined"

Examples of differentiable manifolds

A few examples will convey the concept better than this definition. Elementary examples (Euclidean 3-spaces,the surface of a sphere) bring to mind too many geometric ideas from richer levels of geometry; so one is forced to contemplate something more complicated.Let $R ^ { 3 }$ be a three-dimensional number space with the usual advanced-calculus ideas of continuity and differentiability. Points $\pmb { \xi }$ of $R ^ { 3 }$ are triples, $\pmb { \xi } = ( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } )$ ,of real numbers.Let a ray $\mathcal { P }$ in $R ^ { 3 }$ be any half-line from the origin consisting of all $\pmb { \xi }$ of the form $\pmb { \xi } = \lambda \pmb { \eta }$ for some fixed $\pmb { \eta } \neq 0$ and for all positive real numbers $\lambda > 0$ . (See Figure 9.3.) A good example of a differentiable manifold then is the set $S ^ { 2 }$ of all distinct rays. If $f$ is a real-valued function with a specific value $f ( { \mathcal { P } } )$ for any ray $\mathcal { P }$ [so one writes $f \colon S ^ { 2 } \longrightarrow R \colon \mathcal { P } \longrightarrow f ( \mathcal { P } ) ] ,$ it should be intuitively (or even demonstrably) clear that we can define what we mean by saying $f$ is continuous or differentiable. In this sense $S ^ { 2 }$ itself is continuous and differentiable. Thus $S ^ { 2 }$ is a manifold,and the rays $\mathcal { P }$ are the points of $S ^ { 2 }$ . There are many other manifolds that diferential topology finds indistinguishable from $S ^ { 2 }$ The simplest is the two-dimensional spherical surface (2-sphere),which is the standard representation of $S ^ { 2 }$ ; it is the set of points $\pmb { \xi }$ of $R ^ { 3 }$ satisfying $( \xi _ { 1 } ) ^ { 2 } + ( \xi _ { 2 } ) ^ { 2 } + ( \xi _ { 3 } ) ^ { 2 } = 1$ Clearly a different point $\mathcal { P }$ of $S ^ { 2 }$ (one ray in $R ^ { 3 }$ )intersects each point of this standard 2-sphere surface,and the correspondence is continuous and differentiable in either direction (ray to point; point to ray). The same is true for any ellipsoidal surface in $R ^ { 3 }$ enclosing the origin,and for any other surface enclosing the origin that has

The manifold ${ \mathcal { S } } ^ { 2 }$

![](images/7989b22536dcf6f6cbc73db0c21e899b5f28e13ecccf284bf62bdfb6e03c3156.jpg)  
Figure 9.3. Three different representations of the differentiabie manifoid $S ^ { 2 }$ .The first is the set of ail rays emanating from the origin; the second is the sphere they intersect;the third is an oddshaped,closed surface that each ray intersects precisely once.

a different ray through each point of itself. They each embody the same global continuity and differentiability concepts. and represent the same abstract differentiable manifold $S ^ { 2 }$ ，the 2-sphere. They,and the bundle of rays we started with, all have the same geometric properties at this rudimentary level of geometry. A two-dimensional manifold that has a different geometric structure at this level (a different “differentiable structure") is the torus $T ^ { 2 }$ , the surface of a donut. There is no way to imbed this surface smoothly in $R ^ { 3 }$ so that a distinct ray $\mathcal { P } \in S ^ { 2 }$ intersects each of its points; there is no invertible and differentiable correspondence between $T ^ { 2 }$ and $S ^ { 2 }$

The manifold $\tau ^ { 2 }$

The manifold SO(3) (rotation group)

Another example of a manifold is the rotation group $S O ( 3 )$ , whose points $\mathcal { S }$ are all the $3 \times 3$ orthogonal matrices of unit determinant, s $0 \mathcal { P } = | | P _ { i j } | |$ with $\mathcal { P } ^ { \pmb { T } \ o \mathcal { O } } = 1$ and det $\langle { \boldsymbol { \mathsf { y } } } ^ { \flat } = { \boldsymbol { \mathsf { l } } }$ . This is a three-dimensional space (one often uses the three Eulerangle parameters in computations), where differential ideas (e.g., angular velocity) are employed; hence, it is a manifold. So is the Lorentz group.

The differentiability of a manifold (i.e., the possibility of defining differentiable functions on it) permits one to introduce coordinate systems locally, if not globally, and also curves, tangent spaces,tangent vectors,1-forms,and tensors, just as is done for spacetime.But the mere fact that a manifold is differentiable does not mean that such concepts as geodesics, parallel transport, curvature,metric, or length exist in it. These are additional layers of structure possessed by some manifolds, but not by all Roughly speaking, every manifold has smoothness properties and topology, but without additional structure it is shapeless and sizeless.

Affine geometry and Riemannian geometry defined

That branch of mathematics which adds geodesics, parallel transport, and curvature (shape) to a manifold is called affne geometry; that branch which adds a metric is called Riemannian geometry. They will be studied in- the next few chapters.

# EXERCISES

# EXERCISES ON THE ROTATION GROUP

As the exposition of differential geometry becomes more and more sophisticated in the following chapters,the exercises will return time and again to the rotation group as an example of a manifold.Then,in $\mathbf { B o x } ~ 3 0 . 1 $ ，the results developed in these exercises will beused to analyze the“Mixmaster universe,”which is a particularly important cosmological solution to Einstein's field equation.

Before working these exercises,the reader may wish to review the Euler-angle parametrization for rotation matrices,as treated, e.g., on pp.l07-lO9 of Goldstein (1959).

# Exercise 9.13. ROTATION GROUP:GENERATORS

Let $\mathcal { K } _ { \mathrm { ~ f ~ } }$ be three $3 \times 3$ matrices whose components are $( K _ { t } ) _ { m n } = \epsilon _ { t _ { m n } }$ (a）Display the matrices $\mathcal { F } _ { 1 } , ( \hat { \mathscr { h } _ { 1 } } ) ^ { 2 } , ( \hat { \mathscr { h } _ { 1 } } ) ^ { 3 } ,$ and $( \hat { \mathcal { R } } _ { 1 } ^ { \star } ) ^ { 4 }$ (b) Sum the series

$$
\mathcal { R } _ { z } ( \theta ) \equiv \exp ( \mathcal { K } _ { 1 } \theta ) = \sum _ { n = 0 } ^ { \infty } \frac { \theta ^ { n } } { n ! } ( \mathcal { K } _ { 1 } ) ^ { n } .
$$

Show that ${ \mathcal R } _ { \varepsilon } ( \theta )$ is a rotation matrix and that it produces a rotation through an angle $\pmb \theta$ about the $x \cdot$ -axis.

(c) Show similarly that $\mathcal { R } _ { z } ( \phi ) = \exp ( \mathcal { K } _ { 3 } \phi )$ and $\mathcal { R } _ { u } ( x ) = \exp ( \mathcal { K } _ { 2 } { \chi \smash [ t ] { \mathstrut } } )$ are rotation matrices, and that they produce rotations through angles $\phi$ and $x$ about the $z \cdot$ and y-axes, respectively.

(d) Explain why $\mathcal { P } = \mathcal { R } _ { z } ( \psi ) \mathcal { R } _ { z } ( \theta ) \mathcal { R } _ { z } ( \phi )$ defines the Euler-angle coordinates, $\psi , \theta , \phi$ for the generic element $\mathcal { P } \in S O ( 3 )$ of the rotation group.

(e) Let $\mathcal { C }$ be the curve $\mathscr { P } = \mathscr { R } _ { z } ( t )$ through the identity matrix, $\mathcal { C } ( 0 ) = \mathfrak { g } \in S O ( 3 )$ . Show that its tangent, $( d \mathcal { C } / d t ) ( 0 ) \equiv \dot { \mathcal { C } } ( 0 )$ does not vanish by computing $\dot { \mathcal { C } } ( 0 ) f _ { 1 2 }$ where $f _ { 1 2 }$ is the function $f _ { 1 2 } ( \mathcal { P } ) = P _ { 1 2 } ,$ whose value is the l2 matrix element of $\mathcal { P }$

(f) Define a vector field ${ \pmb { e } } _ { 3 }$ on $S O ( 3 )$ by letting $\pmb { \mathscr { e } } _ { 3 } ( \mathcal { P } )$ be the tangent (at $\scriptstyle { t = 0 }$ to the curve $\mathcal { C } ( t ) = \mathcal { R } _ { z } ( t ) \mathcal { P }$ through $\mathcal { P }$ . Show that $\pmb { \mathscr { e } } _ { 3 } ( \mathcal { P } )$ is nowhere zero. Note: $\pmb { e _ { 3 } } ( \mathcal { P } )$ is called the“generator of rotations about the $z \cdot$ -axis,"because it points from $\mathcal { P }$ toward neighboring rotations, $\mathcal { R } _ { z } ( t ) \mathcal { P }$ ,which differ from $\mathcal { P }$ by a rotation about the $z \cdot$ -axis.

(g） Show that $\pmb { e } _ { 3 } = ( \hat { \partial } / \hat { \partial } \psi ) _ { \pmb { \theta } \phi }$ (h) Derive the following formulas,valid for $t \ll 1$ ：

$$
\begin{array} { r l } & { \mathscr { R } _ { \boldsymbol { x } } ( t ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } ) = \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } - \boldsymbol { t } \sin \boldsymbol { \psi } \cot \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } + \boldsymbol { t } \cos \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } + \boldsymbol { t } \sin \boldsymbol { \psi } / \sin \boldsymbol { \theta } ) ; } \\ & { \mathscr { R } _ { \boldsymbol { y } } ( t ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } ) = \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \psi } + \boldsymbol { t } \cos \boldsymbol { \psi } \cot \boldsymbol { \theta } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \theta } + \boldsymbol { t } \sin \boldsymbol { \psi } ) \mathscr { R } _ { \boldsymbol { z } } ( \boldsymbol { \phi } - \boldsymbol { t } \cos \boldsymbol { \psi } / \sin \boldsymbol { \theta } ) . } \end{array}
$$

(i） Define $\pmb { e } _ { 1 } ( \pmb { \mathcal { P } } )$ and $\pmb { e } _ { 2 } ( \mathcal { P } )$ to be the tangent vectors (at $t = 0$ ）to the curves $\mathcal { C } ( t ) = \mathcal { R } _ { z } ( t ) \mathcal { P }$ and $\mathcal { C } ( t ) = \mathcal { R } _ { y } ( t ) \mathcal { P }$ ,respectively. Show that

$$
\begin{array} { r } { \pmb { e } _ { 1 } = \cos \psi \frac { \hat { \partial } } { \partial \theta } - \sin \psi \left( \cot \theta \frac { \hat { \partial } } { \partial \psi } - \frac { 1 } { \sin \theta } \frac { \hat { \partial } } { \partial \phi } \right) , } \\ { \pmb { e } _ { 2 } = \sin \psi \frac { \hat { \partial } } { \partial \theta } + \cos \psi \left( \cot \theta \frac { \hat { \partial } } { \partial \psi } - \frac { 1 } { \sin \theta } \frac { \hat { \partial } } { \partial \phi } \right) . } \end{array}
$$

$\pmb { e _ { 1 } }$ and $\pmb { e _ { 2 } }$ are the “generators of rotations about the $x \cdot$ and $y$ -axes.”

# ExerciSe 9.14. ROTATION GF:OUP: STRUCTURE CONSTANTS

Jse the three vector fields constructed in the last exercise,

$$
{ \begin{array} { r l } & { e _ { 1 } = \cos \psi { \frac { \partial } { \partial \theta } } - \sin \psi { \biggl ( } \cot \theta { \frac { \partial } { \partial \psi } } - { \frac { 1 } { \sin \theta } } { \frac { \partial } { \partial \phi } } { \biggr ) } , } \\ & { e _ { 2 } = \sin \psi { \frac { \partial } { \partial \theta } } + \cos \psi { \biggl ( } \cot \theta { \frac { \partial } { \partial \psi } } - { \frac { 1 } { \sin \theta } } { \frac { \partial } { \partial \phi } } { \biggr ) } , } \\ & { e _ { 3 } = { \frac { \partial } { \partial \psi } } , } \end{array} }
$$

as basis vectors for the manifold of the rotation group.The above equations express this “basis of generators”in terms of the Euler-angle basis.Show that the commutation coeffcients for this basis are

$$
{ c _ { \alpha \beta } } ^ { \gamma } = - \epsilon _ { \alpha \beta \gamma } ,
$$

independently of location $\mathcal { S }$ in the rotation group.These coefficients are also called the structure constants of the rotation group.

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