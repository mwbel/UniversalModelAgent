# CHAPTER 11

# GEODESIC DEVIATION AND SPACETIME CURVATURE

Spacetime curvature manifests itself as gravitation, by means of the deviation of one geodesic from a nearby geodesic (relative acceleration of test particles).

Let the geodesics of spacetime be known. Then the covariant derivative $\blacktriangledown$ and its connection coeffcients ${ T ^ { \alpha } } _ { \beta \gamma }$ arealsoknonHowromtisoatiodoes one define, calculate, and understand geodesic deviation and spacetime curvature? The answer unfolds in this chapter, and is summarized in Box 11.1. To disclose the answer one must (l) define the “relative acceleration vector" $\yen 123,456$ which measures the deviation of one geodesic from another $( \ S 1 1 . 2 )$ ； (2) derive an expression in terms of $\blacktriangledown$ or $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ for the“Riemann curvature tensor,”which produces the geodesic deviation $( \ S 1 1 . 3 )$ ; (3) see Riemann curvature at work, producing changes in vectors that are parallel transported around closed circuits (S11.4);(4)see Riemann curvature test whether spacetime is flat (S11.5); and (5) construct a special coordinate system,“Riemann normal coordinates,"which is tied in a special way to the Riemann curvature tensor (S11.6).

This chapter is entirely   
Track 2.Chapters 9 and 10 are   
necessary preparation for it. It will be needed as   
preparation for (1) Chapters 12 and 13 (Newtonian gravity: Riemannian geometry), (2) the second half of Chapter 14 (calculation of curvature), and (3) the details,but not the message,of Chapter 15 (Bianchi identities).

# $\$ 12$ . THE RELATIVE ACCELERATION OF NEIGHBORING GEODESICS

Focus attention on a family of geodesics (Figure l1.1). Let one geodesic be distinguished from another by the value of a“selector parameter" $\pmb { n }$ .The family includes not only geodesics $n = 0 , 1 , 2 , \ldots$ but also geodesics for all intervening values of

Geometry of a family of geodesics:

Selector parameter

# BoX 11.1 GEODESIC DEVIATION AND RIEMANN CURVATURE IN BRIEF

"Geodesic separation" $\pmb { n }$ is displacement (tangent vector) from point on fiducial geodesic to point on nearby geodesic characterized by same value of affine parameter $\lambda$

Geodesic separation changes with respect to $\lambda$ (i.e., changes along the tangent vector $\pmb { \upsilon } = d / d \lambda$ ） at a rate given by the equation of geodesic deviation

$$
\nabla _ { u } \ \nabla _ { u } n + R i e m a m n \left( \ldots , { u } , n , { u } \right) = 0
$$

(second-order equation; see $\ S \ S 1 . 6$ and 1.7; Figures 1.10, 1.11, 1.12).

In terms of components of the Riemann tensor the driving force("tidal graviational force") is

$$
( . . . , { \pmb u } , { \pmb n } , { \pmb u } ) = { \pmb e } _ { \alpha } R ^ { \alpha } { } _ { \beta \gamma \delta } u ^ { \beta } n ^ { \gamma } u ^ { \delta } .
$$

The components of the Riemann curvature tensor in a coordinate frame are given in terms of the connection coefficients by the formula

$$
\begin{array} { l } { { R ^ { \alpha } { } _ { \beta \gamma \delta } = \displaystyle \frac { \partial T ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } - \frac { \partial T ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } } } \\ { { + T ^ { \alpha } { } _ { \mu \gamma } T ^ { \mu } { } _ { \beta \delta } - T ^ { \alpha } { } _ { \mu \delta } { \cal T ^ { \mu } } _ { \beta \gamma } . } } \end{array}
$$

This curvature tensor not only quantifies the concept of “tidal gravitational force,” but also enters into Einstein's law, by which “matter tells spacetime how to curve.” That law, to be studied in later chapters, takes the following operationalcomputational form in a given coordinate system:

(a)Write down trial formula for dynamic evolution of metric coefficients $g _ { \mu \nu }$ with time.

(b) Calculate the connection coefficients from

$$
\begin{array} { r } { { T ^ { \alpha } } _ { \mu \nu } = g ^ { \alpha \beta } { \cal T } _ { \beta \mu \nu } ; } \end{array}
$$

$$
{ \cal T } _ { \beta \mu \nu } = { \frac { 1 } { 2 } } \bigg ( { \frac { \partial g _ { \beta \nu } } { \partial x ^ { \mu } } } + { \frac { \partial g _ { \beta \mu } } { \partial x ^ { \nu } } } - { \frac { \partial g _ { \mu \nu } } { \partial x ^ { \beta } } } \bigg )
$$

(derived in Chapter 13).

(c) Calculate Riemann curvature tensor from equation (3).

(d) Calculate Einstein curvature tensor from

$$
G _ { \mu \nu } = { R ^ { \alpha } } _ { \mu \alpha \nu } - { \frac { 1 } { 2 } } g _ { \mu \nu } g ^ { \sigma \tau } { R ^ { \alpha } } _ { \sigma \alpha \tau }
$$

(geometric significance in Chapter 15).

(e) Insert into Einstein's equations (Chapter 17):

$$
\begin{array} { r l r l } & { G _ { \mu \nu } = 0 } & & { ( \mathrm { e m p t y ~ s p a c e } ) , } \\ & { G _ { \mu \nu } = 8 \pi T _ { \mu \nu } } & & { ( \mathrm { w h e n ~ m a s s  – e n e r g y ~ i s } } \end{array}
$$

(f） Test whether the trial formula for the dynamic evolution of the geometry was correct, and, if not, change it so it is.

Affine parameter

$\pmb { n } .$ The typical point $\mathcal { P }$ on the typical geodesic will be a continuous, doubly differentiable function of the selector parameter $\pmb { n }$ and the affine parameter $\lambda$ ； thus

$$
{ \mathcal { P } } = { \mathcal { P } } ( \lambda , n ) .
$$

Tangent vector

The tangent vector

$$
\pmb { u } = \frac { \partial \mathcal { P } } { \partial \lambda } \qquad ( \mathbf { C a r t a n \ n o t a t i o n } )
$$

or

$$
\pmb { u } = \frac { \partial } { \partial \lambda } \qquad \mathrm { ( n o t a t i o n ~ o f ~ t h i s ~ b o o k ) }
$$

is constant along any given geodesic in this sense: the vector $\pmb { u }$ at any point, trans-

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/fa9b741e11443dbcb279ceae37216f23809c4d79345b6934d4ed3c8eb1894407.jpg)  
Figure 11.1. One-parameter family of geodesics.The“selector parameter" $\pmb { n }$ tells which geodesic. The affine parameter $\lambda$ tells where on a given geodesic. The two tangent vectors indicated in the diagram are ${ \pmb u } =$ $\partial / \partial \lambda$ (Cartan: $\partial \mathscr { P } / \partial \lambda$ and ${ \pmb n } = \partial / \partial { \pmb n }$ (Cartan: $\hat { c } \hat { \mathscr { P } } / \hat { \mathscr { o } } n$ .

ported parallel to itself along the geodesic, arrives at a second point coincident in direction and length with the $\pmb { u }$ already existing at that point.

The“separation vector”

$$
\pmb { \eta } = \frac { \partial \pmb { \mathcal { P } } } { \partial \pmb { n } } \qquad ( \mathbf { C a r t a n \ n o t a t i o n } )
$$

or

$$
{ \pmb { \eta } } = { \frac { \partial } { \partial { \pmb { n } } } } \qquad { \mathrm { ( n o t a t i o n ~ o f ~ t h i s ~ b o o k ) } }
$$

measures the separation between the geodesic $\pmb { n }$ ,regarded as the fiducial geodesic, and the typical nearby geodesic, $n + 4 n$ (for small $\varDelta n$ ), in the sense that

$$
( \varDelta n ) \pmb { \mathstrut } = \left\{ \begin{array} { c } { { \Delta n \frac { \hat { c } ^ { \acute { \sigma } } } { \partial n } \nonumber } } \\ { { \mathrm { ~ { \ m e a s u r e s ~ t h e } ~ \left\{ \begin{array} { l } { { \mathrm { P 0 s i t i o n } } } \\ { { \mathrm { a n y } } } \\ { { \mathrm { f u n c t i o n } } } \end{array} \right\} } } } \end{array} \right.
$$

brought about by transfer of attention from the one geodesic to the other at a fixed value of the affine parameter $\lambda$ . This vector is represented by the arrow $\because \mathcal { D } \mathcal { L } \mathcal { L }$ in the first diagram in Box 11.2.

(continued on page 270)

“Fiducial geodesic”n. Separation vector n $\varDelta n =$ $\mathfrak { M } \mathcal { Q }$ leads from point $\because \pi$ on it, to point $\underset { ^ { \prime } } { \underbrace { \mathcal { O } } }$ with same value of affine parameter $\lambda$ (timelike quantity） on neighboring “test geodesic” $n + 4 n$

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/a28ed6ee49bb9cfc9d6a84fcb9345dd05bc652da0c53211cab81c74fb0c3fa90.jpg)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/9af3beffe23496169fabf1bbbcc215f0d4e2491dae4cf8d8ff59ba6a7917b13d.jpg)

Parallel transport of $\mathcal { D } \mathcal { Q }$ by “Schild's ladder construction”(Box 10.2） to $\mathcal { D B }$ and $\mathcal { L } \mathcal { Q }$ If the test geodesic $n + 4 n$ had kept a constant separation from the fiducial geodesic $\pmb { n } ,$ its tracer point would have arrived at $\boldsymbol { \mathcal { I } }$ at the value $( \lambda - \varDelta \lambda )$ of the affine parameter, and at $\mathcal { B }$ at $( \lambda + \varDelta \lambda )$

Actual location of tracer point of test geodesic at values of the timelike affine parameter $( \lambda - 4 \lambda )$ ， $\lambda ,$ and $( \lambda + \varDelta \lambda )$

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/42a96cdbf832790bdf36a4230cefc65f30c08e70095e7fa3569ddc8ec0825006.jpg)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/1b77acd4d3120c6a8a9f2d65f24650c0eb5b2da8914fc7433347c0f5aceba57c.jpg)

Confrontation between actual course of tracer point on test geodesic and “canonical course": course it would have had to take to keep constant separation from the tracer point moving along the fiducial geodesic.

Test geodesic same as before, except for uniform stretchout in scale of affine parameter. Any measure of departure of the actual course of geodesic from the canonical course $( \mathcal { Q Q B } )$ , to be useful, should be independent of this stretchout. Hence, take as measure of geodesic deviation,not the vector $\mathcal { B R }$ alone,nor the vector ${ \mathcal { Q } } { \mathcal { P } } _ { : }$ ，but the stretch-independent combination $\pmb { \delta } _ { 2 } = ( \mathcal { B } \mathcal { R } ) +$ $( \mathcal { Q P } )$ . Here the sign of addition implies that the two vectors have been transported parallel to themselves, before addition, to a common point $\mathfrak { L }$ in the diagram; $\mathfrak { R }$ in the differential calculus limit $\varDelta n \longrightarrow 0$ ， $\varDelta \lambda \longrightarrow 0$ .

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/2e8e9f25c65d29e622945e8778694ce8a1bbc778116fdf106bee7d4932dfde2d.jpg)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/2754f609928705fc30861d7f4da689834b8420ac2dc53f8738e100cfcb4e86a1.jpg)

Alternative courses that the test geodesic of $\mathbf { o }$ could have taken through $\mathcal { L }$ (families of geodesics characterized by different degrees of divergence from the left or convergence towards the right). Tilt changes values of $\mathcal { Q } \mathcal { P }$ (to $\vec { q } \bar { \mathcal { P } } )$ and BR (to $\mathbf { \widehat { \mathbf { \mathcal { A } } } } _ { 1 } \mathbf { \overline { { \mathbf { \mathcal { R } } } } }$ ） individually,but not value of the sum $\pmb { \delta } _ { 2 . } = ( \mathcal { B } \mathcal { R } )$ $+ \left( \mathcal { Q } \mathcal { P } \right)$ ("lever principle").

Note that arrow $\mathcal { B R }$ is of first order in $\pmb { \varDelta \lambda }$ and of first order in $\varDelta n$ ；similarly for $\mathcal { Q } \mathcal { P }$ ; hence the combination $\pmb { \delta } _ { 2 }$ is of second order in $\pmb { \varDelta } \lambda$ and first order in $\pmb { \varDelta n }$ .Conclude that the arrow $\pmb { \delta } _ { 2 } / ( \pmb { \varDelta } \lambda ) ^ { 2 } ( \pmb { \varDelta } n )$ is the desired measure of geodesic deviation in the sense that:

size of mesh (ultimately to go to zero) cancels out; parameterization of test geodesic cancels out; slope of test geodesic cancels out.

Give this arrow the name “relative-acceleration vector”; and by examining it more closely (Box 11.3), discover the formula

$$
\pmb { \delta } _ { 2 } / ( \varDelta \lambda ) ^ { 2 } ( \varDelta n ) = \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n }
$$

for it.

Box ll.2 illustrates what it means to speak of geodesic deviation. One transports the separation n $\Delta n = \mathfrak { P } \mathfrak { Q } \mathfrak { Q }$ parallel to itself along the fiducial geodesic. The tip of this vector traces out the canonical course that the nearby tracer point would have to pursue if it were to maintain constant separation from the fiducial tracer point. The actual course of the test geodesic deviates from this “canonical’ course. The deviation,a vector ( $\mathcal { Q } \mathcal { P }$ of Box 1l.2), changes with the affine parameter ( ${ \mathcal { Q } } { \mathcal { P } }$ at $\boldsymbol { \mathcal { q } }$ ， 0at $\mathcal { L }$ Bat $\mathcal { B }$ ). The first derivative of this vector with respect to the affine parameter is sensitive to the scale of parameterization along the test geodesic, and to its slope (Box 11.2,F). Not so the second derivative. lt depends only on the tangent vector $\pmb { u }$ of the fiducial geodesic,and on the separation vector $\pmb { n } \pmb { \varDelta n }$ Divide this second derivative of the deviation by $\varDelta n$ and give it a name: the “relative-acceleration vector" Discover (Box 11.3) a simple formula for it

$$
( \mathrm { r e l a t i v e - a c c e l e r a t i o n ~ v e c t o r } ) = \nabla _ { \boldsymbol { u } } \ \nabla _ { \boldsymbol { u } } n .
$$

# $\$ 123$ TIDAL GRAVITATIONAL FORCES AND RIEMANN CURVATURE TENSOR

With“relative acceleration” now defined, turn to the“tidal gravitational force”(i.e., “spacetime curvature") that produces it. Use a Newtonian analysis of tidal forces

# Box 11.3 GEODESIC DEVIATION:ARROW CORRELATED WITH SECOND COVARIANT DERIVATIVE

The arrow $\pmb { \delta } _ { 2 }$ in Box 11.2 measures, not the rate of change of the separation of the test geodesic $n + \Delta n$ from the “canonical course"d2bB as baseline,but the second derivative:

$$
\begin{array} { r l } & { \bigg ( \mathrm { f i r s t ~ d e r i v a t i v e ~ a t ~ } \lambda + \frac { 1 } { 2 } { \varDelta \lambda } \bigg ) = \nabla _ { u } n = \frac { \mathcal { X } \mathcal { Q } - \mathcal { X } \mathcal { Q } } { \varDelta \lambda \varDelta n } = \frac { \mathcal { B } \mathcal { R } } { \varDelta \lambda \varDelta n } ; } \\ & { \bigg ( \mathrm { f i r s t ~ d e r i v a t i v e ~ a t ~ } \lambda - \frac { 1 } { 2 } { \varDelta \lambda } \bigg ) = \nabla _ { u } n = \frac { \mathcal { L } \mathcal { Q } - \mathcal { L } \mathcal { P } } { \varDelta \lambda \varDelta n } = \frac { - \mathcal { Q } \mathcal { P } } { \varDelta \lambda \varDelta n } . } \end{array}
$$

Transpose to common location $\lambda$ ,take difference,and divide it by $\Delta \lambda$ to obtain the second covariant derivative with respect to the vector $\pmb { u }$ ；thus

$$
\begin{array} { l } { \displaystyle \nabla _ { u }  \nabla _ { u } \boldsymbol { n } = \frac { ( \nabla _ { u } \boldsymbol { n } ) _ { \lambda + \frac { 1 } { 2 } } \boldsymbol { \varDelta \lambda } - ( \nabla _ { u } \boldsymbol { n } ) _ { \lambda - \frac { 1 } { 2 } } \boldsymbol { \varDelta \lambda } } { \boldsymbol { \varDelta \lambda } } } \\ { \displaystyle = \frac { ( \mathcal { B R } + \mathcal { A P } ) _ { \mathrm { v e c t o r s t r a n s p o r t e d t o } } } { ( \boldsymbol { \varDelta \lambda } ) ^ { 2 } \boldsymbol { \varDelta n } } = \frac { \delta _ { 2 } } { ( \boldsymbol { \varDelta \lambda } ) ^ { 2 } \boldsymbol { \varDelta n } } } \\ { \displaystyle = \overbrace { \boldsymbol { \cdots } \mathrm { r e l a t i v e \ a c c e l e r a t i o n \ v e c t o r ^ { \prime } } \mathrm { f o r \ n e i g h b o } } ^ { ( \mathcal { A } ) } } \end{array}
$$

(left half of Box 11.4) to motivate the geometric analysis (right half of same box). Thereby arrive at the remarkable equation

$$
\begin{array} { r l r } { \nabla _ { u } \nabla _ { u } \boldsymbol { n } } & { { } + } & { [ \nabla _ { \boldsymbol { n } } , \nabla _ { u } ] \boldsymbol { u } = 0 . } \\ { \mathrm { ~  ~ { \frac ~ { \phi ~ } { \varepsilon ~ } } ~ } } & { { } \Gamma ^ { \prime } \quad \mathrm { e l a t i v e } \quad } & { \Gamma ^ { \prime } \quad \mathrm { e " ~ t i d e \mathrm { - } p r o d u c i n g } } \\ { \mathrm { ~  ~ { \frac ~ { \phi ~ } { \varepsilon ~ } } ~ } } & { { } \mathrm { g r a v i t a t i o n a l ~ f o r c e s " ~ } , } \end{array}
$$

Tide-producing gravitational forces expressed in terms of a commutator

This equation is remarkable, because at first sight it seems crazy. The term $[ \pmb { \bigtriangledown _ { n } } , \pmb { \bigtriangledown _ { u } } ] \pmb { u }$ involves second derivatives of $\pmb { u }$ ,and a first derivative of $\forall _ { \pmb { n } }$ ：

$$
[ \pmb { \nabla } _ { n } , \pmb { \nabla } _ { u } ] \pmb { u } \equiv \pmb { \nabla } _ { n } \pmb { \nabla } _ { u } \pmb { u } - \pmb { \nabla } _ { u } \ \pmb { \nabla } _ { n } \pmb { u } .
$$

It thus must depend on how $\pmb { u }$ and $\pmb { n }$ vary from point to point. But the relative acceleration it produces, $\yen 1$ is known to depend only on the values of $\pmb { u }$ and $\pmb { n }$ at the fiducial point,not on how $\pmb { u }$ and $\pmb { n }$ vary (see Box 11.2, F). How is this possible?

Somehow all derivatives must drop out of the tidal-force quantity $[ \pmb { \nabla } _ { \pmb { n } } , \pmb { \nabla } _ { \pmb { u } } ] \pmb { u } .$ One must be able to regard $[ \pmb { \nabla } _ { \dots } , \pmb { \nabla } _ { \dots } ] \ldots \pmb { \mathrm { a s } }$ a purely local, algebraic machine with three slots,whose output is a vector. If it is purely local and not differential, then it is even linear (as one sees from the additivity properties of $\blacktriangledown$ ), so it must be a tensor. Give this tensor the name Riemann,and give it a fourth slot for inputing a 1-form:

$$
R i e m a n n \ ( . . . , c , A , B ) \equiv [ \Psi _ { A } , \Psi _ { B } ] C ;
$$

This is only a tentative definition of Riemann.Before accepting it, one should verify that it is, indeed,a tensor. Does it really depend on only the values of $\pmb { A }$ ， B, C at the point of evaluation,and not on how they are changing there? The answer (derived in Box l1.5) is “almost.”It fails the test, but with a slight modification it will pass.The modification is to replace the commutator $[ \pmb { \bigtriangledown _ { A } } , \pmb { \bigtriangledown _ { B } } ]$ by the"curvature operator"

Curvature operator defined

$$
\begin{array} { r } { \mathcal { R } ( A , B ) \equiv [ \nabla _ { A } , \nabla _ { B } ] - \nabla _ { [ A , B ] } , } \end{array}
$$

where $\yen 123$ is the derivative along the vector $[ A , B ]$ (commutator of $\pmb { A }$ and $\pmb { B }$ ) $( \mathcal { R } ( A , B ) \equiv [ \nabla _ { A } , \nabla _ { B } ]$ for the fields ${ \pmb A } = { \pmb n }$ and $\pmb { \cal B } = \pmb { \mu }$ of the geodesic-deviation problem, because $[ { \pmb n } , { \pmb u } ] = 0 .$ ） Then the modified and acceptable definition of the Riemann curvature tensor is

Riemann curvature tensor defined

$$
\begin{array} { r l } & { R i e m a n n \left( \ldots , \pmb { C } , \pmb { A } , \pmb { B } \right) \equiv \langle \pmb { \mathcal { A } } ( \pmb { A } , \pmb { B } ) \pmb { C } ; } \\ & { R i e m a n n \left( \sigma , \pmb { C } , \pmb { A } , \pmb { B } \right) \equiv \langle \pmb { \sigma } , \acute { \mathcal { A } } ( \pmb { A } , \pmb { B } ) \pmb { C } , } \end{array}
$$

To define Riemann thus,and to verify its tensorial character (exercise l1.2), does not by any means teach one what curvature is all about. To understand curvature, one must scrutinize Riemann from all viewpoints. That is the task of the rest of this chapter.

# Box 11.4 RELATIVE ACCELERATION OF_TEST PARTICLES一 GEOMETRIC ANALYSIS PATTERNED ON NEWTONIAN ANALYSIS

# Newtonian Analysis

# Geometric Analysis

1. Consider a family of test-particle trajectories $x ^ { j } ( t , n )$ in ordinary,three-dimensional space: $" t "$ is time measured by particle's clock, or any clock; $" n '$ is “selector parameter.”

1. Consider a family of test-particle trajectories (geodesics), ${ \mathcal { P } } ( \lambda , n )$ ,in spacetime: $^ { \mathfrak { s } } \lambda ^ { \mathfrak { s } }$ is affineparameter, i.e.， time measured by particle's clock; $" n "$ is “selector parameter.”

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/0f3187734a3f75b90bdf2e341aeb2b0a52d5f8cc59e0fed3c9ce7989da177eab.jpg)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/4dd6460014c2577948e3a84f7b942be8b7d6e9601be5d16176b0de2c0255935f.jpg)

2. Equation of motion for each trajectory:

$$
\left( \frac { \partial ^ { 2 } x ^ { j } } { \partial t ^ { 2 } } \right) _ { n } + \frac { \partial \bar { \phi } } { \partial x ^ { j } } = 0 ,
$$

where $\pmb { \phi }$ is Newtonian potential.

2. Geodesic equation for each trajectory:

$$
\pmb { \nabla } _ { \pmb { u } } \pmb { u } = 0 .
$$

[Looks like first-order equation； is actually second-order because the $\bullet \bullet \bullet$ being differentiated is itself a derivative, $\pmb { u } = ( \hat { \partial } \pmb { \mathcal { P } } _ { \mathrm { \prime } } / \hat { \partial } \lambda ) _ { n } . ]$

3. Take difference between equations of motion for neighboring trajectories, $\pmb { n }$ and $n + 4 n$ and take limit as $\varDelta n \longrightarrow 0$ -i.e.,take derivative

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } \left[ \left( \frac { \partial ^ { 2 } x ^ { j } } { \partial t ^ { 2 } } \right) _ { n } + \frac { \partial \phi } { \partial x ^ { j } } \right] = 0 . } \end{array}
$$

3.Take difference between geodesic equations for neighboring geodesics $\pmb { n }$ and $n + 4 n ,$ and take limit as $\varDelta n \longrightarrow 0$ -ie.,take covariant derivative

$$
\pmb { \nabla } _ { \pmb { n } } \left[ \pmb { \nabla } _ { \pmb { u } } \pmb { u } \right] = 0 .
$$

4. When $\hat { \partial } / \hat { \partial } n$ acts on second term, rewrite it as

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } = \left( \frac { \partial x ^ { k } } { \partial n } \right) _ { t } \frac { \partial } { \partial x ^ { k } } = n ^ { k } \frac { \partial } { \partial x ^ { k } } ; } \end{array}
$$

Thereby obtain

$$
\begin{array} { r } { \left( \frac { \partial } { \partial n } \right) _ { t } \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial x ^ { j } } { \partial t } \right) _ { n } + \frac { \partial ^ { 2 } \varPhi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0 . } \end{array}
$$

4. There is no second term, so leave equation in form

$$
\begin{array} { r } { \pmb { \nabla } _ { \pmb { n } } \left[ \pmb { \nabla } _ { \pmb { u } } \pmb { u } \right] = 0 . } \end{array}
$$

5. To obtain equation for relative acceleration, move $( \partial / \partial n ) _ { t }$ through both of the $\left( \partial / \partial t \right) _ { n }$ terms (permissible because partial derivatives commute!):

$$
\begin{array} { r } { \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial } { \partial t } \right) _ { n } \left( \frac { \partial x ^ { j } } { \partial n } \right) _ { t } + \frac { \partial ^ { 2 } \varPhi } { \partial x ^ { j } \partial x ^ { k } } n ^ { k } = 0 . } \end{array}
$$

This is equivalent to

（2n） 22 +xxn =0.   
[relative ttide-producing   
acceleration"] gravitational forces"]

5. To obtain equation for relative acceleration, $\yen 1$ move $\forall _ { \pmb { n } }$ through $\pmb { \tau } _ { \pmb { u } }$ and through the $\partial / \partial \lambda$ of $\pmb { \upsilon } = \partial \mathcal { P } / \partial \lambda$ ：

a. First step: In $\begin{array} { r } { \pmb { \nabla _ { n } } \pmb { \nabla _ { u } } \pmb { u } = 0 } \end{array}$ ,move $\forall _ { \pmb { n } }$ through $\pmb { \check { \nu } _ { \pmb { \ u } } }$ . The result:

$( \nabla _ { u } \ : \nabla _ { \boldsymbol { n } } + \underbrace { [ \ : \nabla _ { \boldsymbol { n } } , \ : \nabla _ { \boldsymbol { u } } ] } _ { \displaystyle \dot { \uparrow } } ) \boldsymbol { u } = 0 .$ commutator;must be included as protection against possibility that $\pmb { \nabla _ { u } } \pmb { \nabla _ { n } } \neq \pmb { \nabla _ { n } } \pmb { \nabla _ { u } }$

b. Second step: Move $\forall _ { \pmb { n } }$ through $\partial / \partial \lambda$ of $\pmb { \upsilon } = \partial \mathcal { P } / \partial \lambda$ ; i.e., write

$$
\begin{array} { r } { = \left[ \frac { \partial } { \partial n } , \frac { \partial } { \partial \lambda } \right] = \frac { \partial ^ { 2 } } { \partial n \partial \lambda } - \frac { \partial ^ { 2 } } { \partial \lambda \partial n } = 0 . } \end{array}
$$

c. Result:

uVun +[mu]u = 0   
"relative "tide-producing   
acceleration" gravitational forces"; i.e..“spacetime curvature”

Box 11.5 RIEMANN CURVATURE TENSOR

# A. Definition of Riemann Motivated by Tidal Gravitational Forces:

1. Tidal forces (spacetime curvature) produce relative acceleration of test particles (geodesics） given by

$$
\begin{array} { r } { \nabla _ { u } \nabla _ { u } \pmb { n } + [ \pmb { \nabla } _ { n } , \pmb { \nabla } _ { u } ] \pmb { u } = 0 . } \end{array}
$$

# Box 11.5 (continued)

2. This motivates the definition

$$
\begin{array} { r } { R i e m a n n \left( . \vphantom { \frac { b } { b } } \mathrm { ~ \frac ~ { \ p ~ { \frac { b } { b } } ~ { \frac { b } { b } } ~ { \frac { c } { d } } } ~ } , \pmb { c } , \pmb { A } , \pmb { B } \right) = [ \pmb { \nabla } _ { A } , \pmb { \nabla } _ { B } ] \pmb { C } . } \\ { \mathrm { \frac { 1 } { \ l e m p t y ~ s l o t ~ f o r ~ i n s e r t i n g } } } \end{array}
$$

# B. Failure of this Definition

1. Definition acceptable only if Riemann $( \ldots , \pmb { C } , \pmb { A } , \pmb { B } )$ is a linear machine, independent of how A, B, $\pmb { c }$ vary from point to point.

2. Check, in part: change variations of $\pmb { c }$ but not $\pmb { c }$ itself, at event $\mathcal { P } _ { \mathbf { 0 } }$

$$
\begin{array} { r } { \pmb { C } _ { \mathrm { N E W } } ( \mathcal { P } ) = f ( \mathcal { P } ) \pmb { C } _ { \mathrm { o L D } } ( \mathcal { P } ) . } \\ { \qquad \quad \vdots _ { [ \mathrm { a r b i t r a r y f u } } } \end{array}
$$

3. Does this change $[ \pmb { \nabla } _ { \pmb { A } } , \pmb { \nabla } _ { \pmb { B } } ] \pmb { C } ?$ Yes！ Exercise 11.1 shows

$$
\{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { N E W } } \} _ { \mathrm { a t } \mathcal { P } _ { 0 } } - \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { O L D } } \} _ { \mathcal { P } _ { 0 } } = C _ { \mathrm { O L D } } \nabla _ { [ A , B ] } f .
$$

# C. Modified Definition of Riemann:

1. The term causing trouble, $\pmb { c } _ { \mathrm { o L D } } \pmb { \bigtriangledown } _ { [ \pmb { A } , \pmb { B } ] } f ,$ can be disposed of by subtracting a “correction term” resembling it from Riemann-i.e.,by redefining

$$
\begin{array} { r } { R i e m a n n \left( \ldots , \ldots , { \pmb { C } } , { \pmb { A } } , { \pmb { B } } \right) \equiv \mathcal { R } ( { \pmb { A } } , { \pmb { B } } ) { \pmb { C } } , \qquad } \\ { \mathcal { R } ( { \pmb { A } } , { \pmb { B } } ) \equiv [ \pmb { \nabla } _ { \pmb { A } } , \pmb { \nabla } _ { \pmb { B } } ] - \pmb { \nabla } } \end{array}
$$

2. The above calculation then gives a result independent of the“modifying function” $f$

$$
\{ { \mathcal { R } } ( A , B ) C _ { \mathrm { N E W } } \} _ { \mathrm { a t } { \boldsymbol { \varphi } } _ { 0 } } = \{ { \mathcal { R } } ( A , B ) C _ { \mathrm { 0 L D } } \} _ { \mathrm { a t } { \boldsymbol { \varphi } } _ { 0 } } .
$$

# D. Is Modified Definition Compatible with Equation for Tidal Gravitational Forces?

2. This works just as well for modified definition of Riemann as for original definition, because

$$
\begin{array} { r } { \begin{array} { r } { \boldsymbol { \mathcal { R } } ( n , { \boldsymbol { u } } ) = [ \boldsymbol { \nabla } _ { n } , \boldsymbol { \nabla } _ { \boldsymbol { u } } ] - \boldsymbol { \nabla } _ { [ n , { \boldsymbol { u } } ] } = [ \boldsymbol { \nabla } _ { n } , \boldsymbol { \nabla } _ { \boldsymbol { u } } ] . } \\ { \qquad \quad \vdots \qquad \displaystyle { \mathrm { ~ L } } \int _ { \boldsymbol { u } } = 0 \mathrm { ~ b e c a u s e ~ } n = ( \partial / \partial n ) _ { \boldsymbol { \lambda } } \mathrm { ~ a n d } \Bigg ] } \end{array} } \\ { \boldsymbol { \nabla } _ { \boldsymbol { u } } = ( \partial / \partial \lambda ) _ { n } \mathrm { ~ c o m m u t e } \qquad } \end{array}
$$

Geodesic deviation and tidal forces cannot tell the difference between $\mathcal { R } ( \pmb { n } , \pmb { u } )$ and $[ \pmb { \nabla } _ { \pmb { n } } , \pmb { \nabla } _ { \pmb { u } } ] _ { : }$ ，nor consequently between old and new definitions of Riemann.

# E. Is Modified Definition Acceptable?

I.e., is Riemann $( \ldots , \pmb { c } , \pmb { A } , \pmb { B } ) \equiv \Re ( \pmb { A } , \pmb { B } ) \pmb { C }$ a linear machine with output independent of how $\pmb { A }$ ,B, $\pmb { c }$ vary near point of evaluation? YES! (See exercise l1.2.)

Take stock, first, of what one knows already about the Riemann curvature tensor. (l) Riemann is a tensor; despite the appearance of $\blacktriangledown$ in its definition (11.9), no derivatives actually act on the input vectors $\mathbf { A } , \mathbf { B } ,$ ,and C.(2) Riemann is a $\textstyle { { \binom { 1 } { 3 } } }$ tensor; its first slot accepts a l-form; the others, vectors. (3) Riemann is determined entirely by $\blacktriangledown$ ,or equivalently by the geodesics of spacetime,or equivalently by spacetime's parallel transport law; nothing but $\blacktriangledown$ and the input vectors and l-form are required to fix Riemann's output. (4) Riemann produces the tidal gravitational forces that pry geodesics (test-particle trajectories) apart or push them together; i.e., it characterizes the “curvature of spacetime":

Tide-producing gravitational forces expressed in terms of Riemann

$$
\nabla _ { u } \ : \nabla _ { u } n + R i e m a n n \ : ( . . . , u , n , u ) = 0 .
$$

(This “equation of geodesic deviation” follows from equations 11.6, 11.8, and l1.9, and the relation $[ { \pmb n } , { \pmb u } ] = 0$ ）

All tese facets of Riemann are pictorial (e.g., geodesic deviation; see Boxes 11.2 and ll.3) or abstract (e.g.,equations l1.8 and l1.9 for Riemann in terms of $\blacktriangledown$ ) Riemann's component facet,

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } \equiv R i e m a n n ~ ( \omega ^ { \alpha } , e _ { \beta } , e _ { \gamma } , e _ { \delta } ) \equiv \langle \omega ^ { \alpha } , \mathcal { R } ( e _ { \gamma } , e _ { \delta } ) e _ { \beta } \rangle , ~ .
$$

Components of Riemann expressed in terms of connection coefficients

is related to the component facet of $\blacktriangledown$ by the following equation, valid in any coordinate basis $\{ { \pmb e } _ { \alpha } \} = \left\{ \hat { \sigma } / \hat { \sigma } x ^ { \alpha } \right\}$ ：

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } = { \frac { \partial { \cal { T } } ^ { \alpha } { } _ { \beta \delta } } { \partial x ^ { \gamma } } } - { \frac { \partial { \cal { T } } ^ { \alpha } { } _ { \beta \gamma } } { \partial x ^ { \delta } } } + { \cal { T } } ^ { \alpha } { } _ { \mu \gamma } { \cal { T } } ^ { \mu } { } _ { \beta \delta } - { \cal { T } } ^ { \alpha } { } _ { \mu \delta } { \cal { T } } ^ { \mu } { } _ { \beta \gamma } .
$$

(See exercise l1.3 for derivation,and exercise l1.4 for the extension to noncoordinate bases.） These components of Riemann,with no sign of any derivative operator anywhere, may leave one with a better feeling in one's stomach than the definition (l1.8)with its nondifferentiating derivatives!

Exercise 11.1. $[ \nabla _ { A } , \nabla _ { B } ] c$ DEPENDS ON DERIVATIVES OF $\pmb { c }$ (Based on Box 11.5.） Let $\pmb { c } _ { \mathrm { x E W } }$ and $\pmb { c } _ { \mathrm { o } \mathbf { L } \mathbf { D } }$ be vector fields related by

$$
\begin{array} { r } { \pmb { c } _ { \mathrm { N E W } } ( \mathcal { G } ) = f ( \mathcal { G } ) \pmb { c } _ { \mathrm { o L D } } ( \mathcal { G } ) . } \\ { \qquad \quad \mathrm { L } _ { \mathrm { l a r b i t r a r y } } } \end{array}
$$

Show that

$$
\begin{array} { r } { \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { N E W } } \} _ { \mathrm { a t } } \varphi _ { \mathrm { _ 0 } } - \{ [ \nabla _ { A } , \nabla _ { B } ] C _ { \mathrm { O L D } } \} _ { \mathrm { a t } } \varphi _ { \mathrm { _ 0 } } = C _ { \mathrm { O L D } } \Psi _ { [ A , B ] } f . } \end{array}
$$

Exercise 11.2. PROOF THAT Riemann IS A TENSOR

Show from its definition (l1.8,11.9) that Riemann is a tensor. Hint: Use the following procedure.

(a)If $f ( \mathcal { P } )$ is an arbitrary function, show that

$$
{ \mathcal { R } } ( A , B ) f C = f { \mathcal { R } } ( A , B ) c .
$$

(b） Similarly show that

$$
{ \mathfrak { A } } \left( f { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } = f { \ o { \forall } { \hbar } } \left( { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } \qquad { \mathrm { a n d } } \qquad { \ o { \forall } { \hbar } } \left( { \pmb { A } } , f { \pmb { B } } \right) { \pmb { C } } = f { \ o { \forall } { \hbar } } \left( { \pmb { A } } , { \pmb { B } } \right) { \pmb { C } } ,
$$

(c) Show that ${ \mathcal { R } } ( \pmb { A } , \pmb { B } ) \pmb { c }$ is linear; i.e.,

$$
\begin{array} { r l } & { \Re ( \pmb { A } + \pmb { a } , \pmb { B } ) \pmb { C } = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { A } ( \pmb { a } , \pmb { B } ) \pmb { C } ; } \\ & { } \\ & { \mathcal { R } ( \pmb { A } , \pmb { B } + \pmb { b } ) \pmb { C } = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { A } ( \pmb { A } , \pmb { b } ) \pmb { C } ; } \\ & { \mathcal { R } ( \pmb { A } , \pmb { B } ) ( \pmb { C } + \pmb { c } ) = \mathcal { A } ( \pmb { A } , \pmb { B } ) \pmb { C } + \mathcal { R } ( \pmb { A } , \pmb { B } ) \pmb { c } , } \end{array}
$$

(d) Now use the above properties to prove the most crucial feature of ${ \mathcal { R } } ( { \pmb A } , { \pmb B } ) { \pmb c }$ Modify the variations (gradients) of A. $\pmb { B }$ ,and $\pmb { c }$ in an arbitrary manner, but leave $\pmb { A } , \pmb { B } , \pmb { C }$ unchanged at ${ \mathcal { P } } _ { 0 }$

$$
\left. \begin{array} { l } { { { \pmb { A } } \longrightarrow { \pmb { A } } + a ^ { \alpha } { \pmb { e } } _ { \alpha } } } \\ { { { \pmb { B } } \longrightarrow { \pmb { B } } + b ^ { \alpha } { \pmb { e } } _ { \alpha } } } \\ { { { \pmb { C } } \longrightarrow { \pmb { C } } + c ^ { \alpha } { \pmb { e } } _ { \alpha } } } \end{array} \right. \qquad \} \begin{array} { l } { { a ^ { \alpha } ( { \mathcal { P } } ) , b ^ { \alpha } ( { \mathcal { P } } ) , c ^ { \alpha } ( { \mathcal { P } } ) \mathrm { a r b i t r a r y \ e x c e p t } } } \\ { { \mathrm { t h e y \ a l l \ v a n i s h \ a t \mathcal { S } } = { \mathcal { P } } _ { 0 } , } } \end{array}
$$

Show that this modification leaves ${ \mathcal { R } } ( \pmb { A } , \pmb { B } ) \pmb { c }$ unchanged at $\mathcal { P } _ { 0 } .$

(e)From these facts,conclude that Riemann is a tensor.

# Exercise 11.3. COMPONENTS OF Riemann IN COORDINATE BASIS

Derive equation (l1.12) for the components of the Riemann tensor in a coordinate basis. [Solution:

$$
\begin{array} { r l r l } & { R ^ { \alpha } { } _ { \beta \gamma \delta } = R i e m a n n ~ ( \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \beta } , \boldsymbol { e } _ { \gamma } , \boldsymbol { e } _ { \delta } ) } & & { \Big [ \mathrm { s t a n d a r d ~ w a y ~ t o } } \\ & { } & & { \Big [ \mathrm { c a l c u l a t e ~ c o m p o n e n t s } \Big ] } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { \mathcal { R } } ( \boldsymbol { e } _ { \gamma } , \boldsymbol { e } _ { \delta } ) \boldsymbol { e } _ { \beta } \rangle } & & { [ \mathrm { b y ~ d e f i n i t i o n ~ ( 1 1 . 9 ) } ] } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , ( \boldsymbol { \Psi } _ { \gamma } \boldsymbol { \Psi } _ { \delta } - \boldsymbol { \Psi } _ { \delta } \boldsymbol { \Psi } _ { \gamma } ) \boldsymbol { e } _ { \beta } \rangle } & & { \Big [ \mathrm { b y ~ d e f i n i t i o n ~ ( 1 1 . 8 ) ~ p l u s } } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \mu } \boldsymbol { T } ^ { \mu } { } _ { \beta \delta , \gamma } + ( \boldsymbol { e } _ { \nu } \boldsymbol { T } ^ { \nu } { } _ { \mu \gamma } ) \boldsymbol { T } ^ { \mu } { } _ { \beta \delta } - \boldsymbol { e } _ { \mu } \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma , \delta } - ( \boldsymbol { e } _ { \nu } \boldsymbol { T } ^ { \nu } { } _ { \mu \delta } ) \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma } \rangle } \\ & { } & & { \qquad = \langle \boldsymbol { w } ^ { \alpha } , { } \boldsymbol { \theta } _ { \beta } \gamma - \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma , \delta } \rangle \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \mu } \rangle + ( \boldsymbol { T } ^ { \nu } { } _ { \mu \gamma } { \cal T } ^ { \mu } { } _ { \beta \delta } - \boldsymbol { T } ^ { \nu } { } _ { \mu \delta } \boldsymbol { T } ^ { \mu } { } _ { \beta \gamma } ) \langle \boldsymbol { w } ^ { \alpha } , \boldsymbol { e } _ { \nu } \rangle , } \end{array}
$$

# Exercise 11.4. COMPONENTS OF RIEMANN IN NONCOORDINATE BASIS

In a noncoordinate basis with commutation coeffcients $c _ { \alpha \beta } { } ^ { \gamma }$ defined by equation (9.22),derive the following equation for the components of Riemann:

$$
{ R ^ { \alpha } } _ { \beta \gamma \delta } = { \Gamma ^ { \alpha } } _ { \beta \delta , \gamma } - { \Gamma ^ { \alpha } } _ { \beta \gamma , \delta } + { \Gamma ^ { \alpha } } _ { \mu \gamma } { { r ^ { \mu } } _ { \beta \delta } } - { \Gamma ^ { \alpha } } _ { \mu \delta } { { r ^ { \mu } } _ { \beta \gamma } } - { \Gamma ^ { \alpha } } _ { \beta \mu } { { c } _ { \gamma \delta } } ^ { \mu } .
$$

# $\$ 123$ ．PARALLEL TRANSPORT AROUND A CLOSED CURVE

What are the effects of spacetime curvature,and how can one quantify them? One effect is geodesic deviation (relative acceleration of test bodies), quantified by equation (ll.lO). Another effect, almost as important, is the change in a vector caused by parallel transport around a closed curve. This effect shows up most clearly in the same problem,geodesic deviation, that motivated curvature in the first place. The relative acceleration vector $\blacktriangledown _ { \pmb { u } } \ \pmb { \nabla } _ { \pmb { u } } \pmb { n }$ is also the change $\delta \pmb { u }$ in the vector u caused by parallel transport around the curve whose legs are the vectors $\pmb { n }$ and $\pmb { u }$ ：

Change in a vector due to parallel transport around a closed curve:

Related to geodesic deviation

$$
\begin{array} { r } { \pmb { \nabla _ { u } } \pmb { \nabla _ { u } } \pmb { n } = \delta \pmb { u } . } \end{array}
$$

(See Box l1.6 for proof.) Hence, in this special case one can write

$$
\delta \pmb { u } + R i e m a n n \left( . . . , \pmb { u } , \pmb { n } , \pmb { u } \right) = 0 .
$$

The expected generalization is obvious: pick a closed quadrilateral with legs u Aa and $\pmb { v } \pmb { \varDelta } b$ (Figure 11.2; $\pmb { \varDelta } a$ and $_ { \pmb { \varDelta b } }$ are small parameters,to go to zero at end of discussion). Parallel transport the vector $\pmb { A }$ around this quadrilateral. The resultant change in $\pmb { A }$ should satisfy the equation

$$
\delta { \pmb A } + R i e m a n { \pmb n } \left( . . . , { \pmb A } , { \pmb u } \Delta a , { \pmb v } \Delta b \right) = 0 ;
$$

Equation for change

or, equivalently,

$$
\delta { \pmb A } + 4 a \Delta b \mathcal { R } ( { \pmb u } , { \pmb v } ) { \pmb A } = 0 ;
$$

or, more precisely,

$$
\operatorname * { L i m } _ { 4 a  0 } ( { \frac { \delta A } { \varDelta a \ \varDelta b } } ) + R i e m a n n ( . . . , A , u , v ) = 0 .
$$

The proof is enlightening, for it reveals the geometric origin of the correction term $\yen 1$ in the curvature operator.

The circuit of transport (Figure l1.2) is to be made from two arbitrary vector fields u Aa and ${ \pmb v } \pmb { \varDelta b }$ .However,a circuit made only of these felds has a gap in it, for a simple reason. The magnitude of $\pmb { u }$ varies the wrong way from place to place. The displacement u $\pmb { \varDelta } \boldsymbol { a }$ that reaches.across at the bottom of the quadrilateral from

Derivation of equation for change

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/c8a24f87b098810e6c765271133a96ea4ae43879b31af243bd2c211e782a1f60.jpg)  
Figure 11.2. The change $\delta \pmb { A }$ in a vector $\pmb { A }$ as a result of parallel transport around a closed curve. The edges of the curve are the vector fields u $\pmb { \varDelta } a$ and $\pmb { v } \pmb { \mathcal { A } b }$ plus the“closer of the quadrilateral" $\{ v \ \varDelta b , \pmb { u } \ \varDelta a \} = \{ \pmb { v } ,$ u $\pmb { \varDelta a }$ $^ { \varDelta b }$ (see Box 9.2),

one line of v's to another cannot make the connection at the top of the quadrilateral. Similarly the v's vary the wrong way from place to place to connect the u's. To close the gap and complete the circuit, insert the “closer of quadrilaterals” $[ v \varDelta b$ ， $\pmb { \mathscr { u } } \Delta a ] = [ \pmb { v } , \pmb { u } ] \Delta a \Delta b$ (See Box 9.2 for why this vector closes the gap.)

With the route now specified, the vector $\pmb { A }$ is to be transported around it. One way to do this,“geometrical construction”by the method of Schild's ladder applied Over and over, is the foundation for planning a possible experiment. For planning an abstract and coordinate-free calculation (the present line of action), introduce a “fiducial field,” only to take it away at the end of the calculation. Plan: Conceive of $\pmb { A }$ , not as a localized vector defined solely at the start of the trip,but as a vector field (defined throughout the trip). Purpose: To provide a standard of reference (comparison of A transported from the origin with A at the place in question). Principle: The standard of reference will cancel out in the end. Procedure:

/Net change made in taking the vector A, originally localized at the start of the circuit,and transporting it parallel to itself ("mobile A") -8A= 1 around the closed circuit. This quantity cannot be evaluated until completion of circuit because there is no preexisting standard of (reference along the way. /A quantity subject to analysis for each leg of circuit individually. This new quantity is defined by introducing throughout the whole region a vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ ， smoothly varying, and in agreement at starting =+ point with the original localized A, but otherwise arbitrary. This new quantity is then given by $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ at starting point (same as Alocalized) at starting point) minus $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ at finish point (after transit). /Change in Afid relative to $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ in the course of transport along

$$
\begin{array} { r l } & { \int \mathrm { ( R a n g e ~ i n ~ \mathbb { A } ^ { ( t e i d e ) } ~ r e l a t i v e ~ t o ~ t h e ~ p a r a l e l ) d i - t r a n s p o r t e d ~ \mathbb { A } ^ { ( m o b i n g ) } } , } \\ &  = \left( \begin{array} { l l } { \mathrm { o f ~ r e f i r e r n c e } , } & { \mathrm { ~ o f ~ e ~ o n ~ \mathbb { A } \in ~ \mathbb { B } ^ { \nu } ~ o f ~ t o ~ m a t i o n s ~ a l o n g ~ f o l l o w i n g ~ l e g } , } \\ { 1 \cdot 2 : } & { \mathrm { ~ i s ~ p o r s i n g ~ \mathbb { P } _ { \times } ^ { \nu } \mathbb { A } ^ { ( t i e n d ) } ~ \mathbb { A } ^ { \nu } ( \mathrm { o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / \mathrm { a v e l } } \mathrm { a d ~ \mathbb { A } ^ { \nu } ~ f r o r } } \\ { \quad \nu \ \mathbb { A } , } & { \mathrm { g i v i n i n g ~ \mathbb { P } _ { \times } \mathbb { A } ^ { ( t i e n d ) } } \ \Delta b \ \mathrm { ( ~ o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / a e d ~ \mathbb { A } ^ { \nu } ~ f r o r } } \\ { - \mu \ \lambda \mu _ { \nu } \mathrm { g i v i n g } - } & { \nabla _ { \times } A ^ { ( t i e n d ) } \ \mathcal { A } b \ \mathrm { ( o n ~ 1 i n e ~ t i r o u g h ~ s t a r t i n g ~ p o l ) } } \\ { - \mu \ \lambda \mu _ { \nu } \mathrm { i n i n g } - } & { \nabla _ { \times } A ^ { ( t i e n d ) } \ \mathcal { A } a \ \mathrm { ( o n ~ 1 i n e ~ \mathbb { A } ^ { \nu } ) / a c d } \nu \mathrm { ~ f o r ~ a } b } \end{array} \right. } \\ & { \quad \quad + u \ L _ { 0 } \mathrm { i d } \ \mathrm { B i n g ~ \mathbb { P } } _ { \times } } \\ & { \quad \quad + \left\{ \nu , u \right\} \Delta a \ L _ { 0 } \mathrm { i v i n g ~ \mathbb { P } } _ { \times } \ \mathrm { f i r e a l ~ \Delta a l ~ \delta a \ L e ~ ( o n ~ i n e ~ \mathbb { A } ^ { \nu } ~ s t a r t i n g ~ p o l ~ \pi ~ } ) } \\ & { = \left\{ \nabla _ { \nu } \nabla _ { \nu } - \nabla _ { \nu } \nabla _ { \nu } + \nabla _ { \nu \times 1 } \right\} \ \mathrm { A } ^ { ( t i e n d ) } \ \mathcal { A } a \mathcal { A } b } \\ &  = R i f \mathrm { n } \mu _ { \nu }  \end{array}
$$

Profit: The curvature operator

$$
\ R i e m a n n \left( \ldots , \ldots , \ldots , \pmb { u } , \pmb { v } \right) = \mathcal { R } ( \pmb { u } , \pmb { v } ) = [ \pmb { \nabla } _ { \pmb { u } } , \pmb { \nabla } _ { \pmb { v } } ] - \pmb { \nabla } _ { [ \pmb { u } , \pmb { v } ] } ,
$$

# Box 11.6 GEODESIC DEVIATION AND PARALLEL TRANSPORT AROUNDCLOSED CURVE: TWO ASPECTS OF SAME CONSTRUCTION

Geodesic Deviation

$$
\nabla _ { u } \nabla _ { u } n = \operatorname { L i m } _ { \stackrel { \scriptstyle \ A \lambda  0 } { \scriptstyle \ A n  0 } } \{ \frac { \displaystyle \mathcal { Q } \mathcal { P } + \mathit { \mathcal Q B } \mathcal { Q } } { \displaystyle ( \Delta \lambda ) ^ { 2 } \Delta n } \} .
$$

(See Boxes 11.2 and 11.3)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/55554b111b50372aae71fb3b2eea2510fbfc48aae05ab533c41c490aaf440e02.jpg)

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/3ada0a3aac7462f95c3b58da9a508a9d46d9fdcfc4902c2f572be0da00a74739.jpg)

# Geodesic Deviation

Same result; different construction. To simplify the connection with closed-curve transport, change the tilt and dilate the parametrization of geodesic $\mathcal { S } \mathcal { Q } \mathcal { R }$ in A. The result: B,where $\overrightarrow { \mathcal { S } }$ and $\mathcal { Q }$ coincide. From F of Box l1.2 one knows $\tilde { a } \tilde { \cdot } \tilde { \mathcal { P } } +$ $\begin{array} { r } { { \mathfrak { A } } _ { \mathfrak { L } } ^ { \gamma } { \mathfrak { R } } = { \mathfrak { a } } ^ { \overline { { \mathcal { P } } } } + { \mathfrak { B } } { \overline { { \mathcal { R } } } } . } \end{array}$ -i.e. $\yen 123,456$ isthe same for this family of geodesics as for the original family

$$
\nabla _ { \boldsymbol { u } } \nabla _ { \boldsymbol { u } } \boldsymbol { n } = \operatorname * { L i m } _ { \stackrel { \mathrm { 4 \lambda  0 } } { \mathrm { 4 \lambda  0 } } } \{ \frac { \langle \boldsymbol { \mathcal { B } } \boldsymbol { \overbar { \mathcal { B } } } } { ( \Delta \lambda ) ^ { 2 } } \} .
$$

Also,to simplify discussion set $\varDelta n = \varDelta \lambda = 1$ ,and assume $\pmb { n }$ and $\pmb { u }$ are small enough that one can evaluate $\yen 1$ without taking the limit:

$$
\begin{array} { r } { \nabla _ { u } \ : \nabla _ { u } { n } = \langle \mathcal { B } \overline { { \mathcal { R } } } . } \end{array}
$$

# Parallel Transport Around Closed Curve, Performed by Same Construction

Plan: Parallel transport the vector u $\begin{array} { r } { \mathbf { \nabla } \cdot \mathbf { \delta } \varDelta \lambda = \mathcal { Q } \overline { { \mathcal { R } } } } \end{array}$ counterclockwise around the curve $2 \longrightarrow \bar { \varphi } \longrightarrow \mathcal { E } \stackrel { \cdot } { \longrightarrow } \mathcal { R } \longrightarrow \mathcal { Q } .$ Execution: (1) Call transported vector ${ \pmb u } ^ { ( \mathbf { m } ) } \ ( ^ { * } { \mathbf { m } ^ { \prime } }$ for “mobile"). (2) At $\mathcal { L }$ ， $\pmb { \upsilon } ^ { ( \mathbf { m } ) } = \mathcal { Q } \overline { { \mathcal { R } } }$ . (3)At $\bar { \mathcal P }$ ， $\pmb { \mu } ^ { ( \mathbf { m } ) } = \mathcal { \bar { P } } \mathcal { Q }$ because $\boldsymbol { \overline { { \mathcal { P } } } } \boldsymbol { \mathcal { Q } } \boldsymbol { \overline { { \mathcal { R } } } }$ is a geodesic and $\pmb { \mu } ^ { ( \mathbf { m } ) }$ is its tangent vector. (4) At $\mathcal { L }$ ， $\pmb { \mathscr { u } } ^ { ( \mathbf { m } ) } = \mathscr { L } \mathcal { D } \mathscr { R }$ according to Schild's ladder of the picture. (5) At $\mathfrak { R }$ ， $\pmb { u } ^ { ( \mathbf { m } ) } = \mathcal { R } \mathcal { R }$ because $\mathcal { L } \mathcal { D } \mathcal { R } \mathcal { R }$ is a geodesic and $\pmb { \mu } ^ { ( \mathbf { m } ) }$ is now its tangent vector. (6) At $\mathcal { L }$ ， $\pmb { \nu } ^ { ( \mathbf { m } ) } = \mathcal { Q } \mathcal { G } \beta$ according to Schild's ladder. Result: The change in ${ \pmb u } ^ { ( \mathbf { m } ) }$ is $- \mathcal { B } \overline { { \mathcal { R } } }$ .Had the curve been circuited in opposite direction $\mathcal { L } \longrightarrow \overline { { \mathcal { P } } } \stackrel { } { \longrightarrow }$ ${ \mathcal { Q } } \longrightarrow { \mathcal { R } } \longrightarrow { \mathcal { L } } )$ ， the change would have been $+ \sqrt [ 6 ] { 3 } \sqrt { 2 }$ ：

applied to the vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ ， gives the negative of the change in the localized vector A localized (called $\pmb { A } ^ { ( \mathrm { m o b i l e } ) }$ during the phase of travel) on paralel transport around the closed circuit. It does not give the change in $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ on traversal of that circuit, for $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ has the same value at the end of the journey as at the beginning. Equation (l1.14'） expresses that change in terms of the conveniently calculated differential operator, $\boldsymbol { \mathcal { R } } ( \boldsymbol { u } , \boldsymbol { v } ) = [ \nabla _ { \boldsymbol { u } } , \nabla _ { \boldsymbol { v } } ] - \nabla _ { [ \boldsymbol { u } , \boldsymbol { v } ] }$ Paradox: Neither wanted nor evaluated is the change in the quantity $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ acted on by this operator. Payoff: Ostensibly differential in the character of its action on $\pmb { A }$ ,the operator Riemann $( \ldots , \ldots , \pmb { u } , \pmb { v } ) = \mathcal { R } ( \pmb { u } , \pmb { v } )$ is actually local. Thus,replace the proposed smoothly varying vector field $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ by a quite different but also smoothly varying vector field Afild,new).Then the two fields need agree only at the one point in question for them to give the same output Riemann $( . . . , A , u , v ) = \mathcal { R } ( u , v ) A$ at that point. This one knows from the fact that δA, the quantity calculated, has an existence and value independent of the choice of $\pmb { A } ^ { \mathrm { ( f i e l d ) } }$ .This one can also verify by detailed calculation (exercise l1.2). Power: Although they cancel out in their response to any change of A with location, the several differentiations in the curvature operator respond directly to the “rate of change of geometry with location”("geodesic deviation"). Prolongation: The closed curve need not be a quadrilateral. The curvature operator tells how a vector changes on parallel transport about smallcurves of arbitrary shape (Box 11.7).

# Exercise 11.5. COPLANARITY OF CLOSED CURVES

EXERCISE

Let $\pmb { f } _ { 1 }$ and $\pmb { f _ { 2 } }$ be the bivectors (see Box 11.7) for two small closed curves at the same event.   
Show that the curves are coplanar if and only if ${ \pmb f } _ { 1 } = a { \pmb f } _ { 2 }$ for some number a.

# Box 11.7 THE LAW FOR PARALLEL TRANSPORT ABOUT A CLOSED CURVE

# A. Special Case

Curve is closed quadrilateral formed by vector fields $\pmb { u }$ and ${ \pmb v } .$

1. Law says (in component form)

$$
\delta A ^ { \alpha } + R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } u ^ { \gamma } v ^ { \delta } = 0 .
$$

2. On what characteristics of the closed curve does this depend?

a. Notice that $R ^ { \alpha } { } _ { \beta \gamma \delta } = - R ^ { \alpha } { } _ { \beta \delta \gamma }$ (antisymmetry in last two indices; obvious in equation 11.12 for components; also obvious because reversing the direction the curve is traversed-i.e., interchanging $\pmb { u }$ and $\pmb { \nu }$ -should reverse sign of $\delta \pmb { A }$ ). b.Equation （l） contracts $\pmb { \mu } \otimes \pmb { \nu }$ into these antisymmetric,last two indices. The symmetric part of $\pmb { u } \otimes \pmb { v }$ must give zero. Only the antisymmetric part, $\pmb { \upsilon } \wedge \pmb { v } = \pmb { \upsilon } \otimes \pmb { v } - \pmb { v } \otimes \pmb { u }$ can contribute:

$$
\delta A ^ { \alpha } + { \frac { 1 } { 2 } } R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } ( u \wedge v ) ^ { \gamma \delta } = 0 .
$$

3. This antisymmetric part is a “bivector."It is independent of the curve's shape; it depends only on (a) the plane the curve lies in, and (b) the area enclosed by the curve. [Although without metric “area” is meaningless,“relative areas at an event in a given plane” have just as much meaning as “relative lengths at an

# Box 11.7 (continued)

event along a given direction.” Two vectors at the same event lie on the same line if they are multiples of each other; their relative length in that case is their. ratio. Similarly, two small closed curves at the same event lie in the same plane if their bivectors are multiples of each other (exercise l1.5); their relative area in that case is the ratio of their bivectors.]

# B. General Case

Arbitrary but small closed curve.

1. Break the curve down into a number of quadrilaterals, all lying in the same plane as the curve.

![](../chunks/GRAVITATION_part_0005_pages_0281-0350/auto/images/63e0e55c3fcc65249aeb04f88de4ebf0cefc76c2ab4ba2fc5d102e2fb21dafe6.jpg)

2. Traverse each quadrilateral once in the same sense as the curve is to be traversed. Result: all interior edges get traversed twice in opposite directions (no net traversal); the outer edge (the curve itself） gets traversed once.

3. Thus,SA due to traversing curve is the sum of the $\delta \pmb { A }$ s from traversal of each quadrilateral:

$$
\delta A ^ { \alpha } = - \frac { 1 } { 2 } \sum _ { \mathrm { q u a d r i l a t e r a l s } } R ^ { \alpha } { } _ { \beta \gamma \delta } A ^ { \beta } ( u \wedge v _ { \mathrm { f o r ~ g i v e n ~ q u a d r i l a t e r a l } } ) ^ { \gamma \delta } .
$$

Define the bivector $\pmb { \mathscr { f } }$ for the curve as the sum of the bivectors for its component quadrilaterals:

$$
\pmb { \mathscr { t } } \equiv \mathrm { ~ \mathcal ~ { ~ \sum ~ } ~ } \left( \mathbf { u } \wedge \pmb { \mathscr { v } } \right) _ { \mathrm { q u a d r i l a t e r a l } }
$$

(add “areas"; keep plane the same).

4.Then

$$
\delta A ^ { \alpha } + \frac { 1 } { 2 } R _ { ~ \beta \gamma \delta } ^ { \alpha } A ^ { \beta } f ^ { \gamma \delta } \equiv \delta A ^ { \alpha } + R _ { ~ \beta \downarrow \gamma \delta \mid } ^ { \alpha } A ^ { \beta } f ^ { \gamma \delta } = 0 .
$$

# C. Warning

This is valid only for closed curves of small compass: δA doubles when the area doubles; but the error increases by a factor ${ \sim } 2 ^ { 3 / 2 }$ $\mathbf { \delta } \mathbf { \delta } \mathbf { A } \propto \Delta a \Delta b$ in calculation of $\ S 1 1 . 4$ ； but error $\propto ( A a ) ^ { 2 } \varDelta b$ or $\Delta a ( \Delta b ) ^ { 2 } ]$

# $\$ 123$ .FLATNESS IS EQUIVALENT TO ZERO RIEMANN CURVATURE

To say that space or spacetime or any other manifold is flat is to say that there exists a coordinate system $\{ x ^ { \alpha } ( { \mathcal { P } } ) \}$ in which all geodesics appear straight:

Flatness ofamanifold defined

$$
x ^ { \alpha } ( \lambda ) = a ^ { \alpha } + b ^ { \alpha } \lambda .
$$

(Example: Lorentz spacetime of special relativity,where test bodies move on such straight lines.） They can appear so if and only if the connection coeffcients in the geodesic equation

$$
\frac { d ^ { 2 } x ^ { \beta } } { d \lambda ^ { 2 } } + { \cal { T } } ^ { \beta } { } _ { \mu \nu } \frac { d x ^ { \mu } } { d \lambda } \frac { d x ^ { \nu } } { d \lambda } = 0 ,
$$

expressed in the same coordinate system, all vanish:

$$
T ^ { \beta } { } _ { \mu \nu } = 0 .
$$

From the vanishing of these connection coeffcients,it follows immediately (equation 11.12) that all the components of the curvature tensor are zero:

Flatness implies Riemann $= 0$

$$
R ^ { \beta } { } _ { \gamma \mu \nu } = 0 .
$$

[Geometric restatement of $( 1 1 . 1 6 ) \longrightarrow ( 1 1 . 1 8 ) \longrightarrow ( 1 1 . 1 9 )$ : For all geodesics to be straight in a given coordinate system means that initially parallel geodesics preserve their separation; the geodesic deviation is zero; and therefore the curvature vanishes.]

Is the converse true? Does zero Riemann curvature imply the existence of a coordinate system in which all geodesics appear straight? Yes,as one sees by the following construction.

Transport a vector parallel to itself from $\mathcal { P } _ { 0 }$ to $\mathcal { L }$ ,and then back from $\mathcal { L }$ t0 ${ \mathcal { P } } _ { 0 }$ along a slightly different route. It returns to its starting point with no alteration in magnitude or direction, because Riemann everywhere vanishes. Therefore parallel transport of a base vector $\pmb { e } _ { \mu }$ from ${ \mathcal { P } } _ { 0 }$ to $\mathcal { L }$ yields at $\mathcal { L }$ a base vector $\pmb { \varrho } _ { \mu }$ that is independent,both in magnitude and in direction,of the route of transportation (for routes obtainable one from the other by any continuous sequence of deformations). As for $\mathcal { L }$ ，so for all points of the manifold; and as for the one base vector $\pmb { e } _ { \mu } ,$ so for a complete set of base vectors $( \mu = 0 , 1 , 2 , 3$ : Parallel transport of a basis $\{ \pmb { e } _ { \alpha } ( \mathcal { P } _ { 0 } ) \}$ yields everywhere a field of frames ("frame field"),each base vector of which suffers zero change (relative to the frame field) on parallel transport from any point to any nearby point: thus,

Proof that Riemann $= 0$ implies flatness

$$
\begin{array} { r } { \pmb { \nabla } \pmb { e } _ { \mu } = 0 ; } \end{array}
$$

or

$$
\pmb { \nabla } _ { \nu } \pmb { e } _ { \mu } \left( \equiv \pmb { \nabla } _ { \pmb { e } _ { \nu } } \pmb { e } _ { \mu } \right) = 0 .
$$

With the vanishing of these individual derivatives,there also vanishes the commutator of any two basis-vector fields:

$$
[ { \pmb e } _ { \mu } , { \pmb e } _ { \nu } ] = \pmb { \nabla } _ { \mu } { \pmb e } _ { \nu } - \pmb { \nabla } _ { \nu } { \pmb e } _ { \mu } = 0 - 0 = 0 .
$$

Lorentz coordinates exist if andonlyif Riemann $= 0$

Flatness does not imply Euclidean topology

The gap in the quadrilateral of Figure 11.2 (there read $" \tilde { \varrho } _ { \mu } ^ { \mathrm { ~ ~ } } , "$ for $" \pmb { u } _ { \pmb { \imath } } ^ { \ \ast } \cdots + \pmb { \imath } \pmb { \imath } _ { \pmb { \imath } } ^ { \ \ast } \pmb { \imath } _ { \pmb { \imath } } ^ { \ \ \ast } | \pmb { u } _ { \pmb { \imath } } ^ { \ \ \ast } | ^ { 2 }$ for $\cdots$ ） closes up completely. Thereupon one can introduce coordinates $x ^ { \mu }$ ,each of which increases with a motion in the direction of the corresponding vector field; and with appropriate scaling of these coordinates,one can write

$$
{ \pmb \mathscr { e } } _ { \mu } = \frac { \partial } { \partial x ^ { \mu } }
$$

(see exercise 9.9). With this coordinate basis in hand, one can employ the formula

$$
\pmb { \nabla } _ { \alpha } \pmb { e } _ { \beta } = \pmb { e } _ { \mu } { \varGamma } ^ { \mu } { } _ { \beta \alpha }
$$

to calculate the connection coefficients. From the vanishing of the quantities on the left,one concludes that all the connection coefficients on the right ("bending of geodesics") must be zero; so spacetime is indeed flat.

SurySpees $T ^ { \mu } { } _ { \alpha \beta } = 0$ everywhere and geodesics are straight lines, $x ^ { \alpha } ( \lambda ) = a ^ { \alpha } + b ^ { \alpha } \lambda$ -if and only $i f$ Riemann $= 0$

Note:In the spacetime of Einstein, which has a metric,one can choose $\{ \pmb { e } _ { \pmb { \mu } } ( \mathcal { P } _ { 0 } ) \}$ in the above argument to be orthonormal, $\underline { { \pmb { e } } } _ { \mu } \cdot \pmb { e } _ { \nu } = \eta _ { \mu \nu }$ at $\mathcal { P } _ { 0 }$ .The resulting field of frames willthen be orthonormal everywhere,and the resulting coordinate system will be Lorentz. Thus, in Einsteinian gravity the above summary can be rewritten: spacetime is flat (there exists a Lorentz coordinate system) if and only if Riemann $= 0$

Warning: Flatness does not necessarily imply Euclidean topology. Take a sheet of paper. It is flat.Roll it up into a cylinder.It is still flat,intrinsically. The tracks of geodesics over it have not changed. Distances between neighboring points have not changed. Only the topology has changed, so far as an observer confined forever to the sheet is concerned.(The“extrinsic geometry"-the way the sheet is embedded in the surrounding three-dimensional space-has also changed;but an observer on the sheet knows nothing of this, and it is not the subject of the present chapter. See, instead $\ S 2 1 . 5 . )$

Take this cylinder. Bend it around and glueits two ends together, without changing its flat intrinsic geometry. Doing so is impossible if the cylinder remains embedded in flat, three-dimensional Euclidean space； perfectly possible if it is embedded in a Euclidean space of4 dimensions. However,embedding is unimportant to observers confined to the cylinder, since all they ever measure is intrinsic geometry； so all that matters to them is the topological identification of the two ends of the cylinder with each other. The result is topologically a torus; but the tracks of geodesics are still unchanged; the intrinsic geometry is flat; Riemann vanishes.

By analogy, take flat Minkowskii spacetime.Pick some'Lorentz frame, and in it pick a cube $1 0 ^ { 1 0 }$ light years on each side $( 0 < x < 1 0 ^ { 1 0 }$ light years； similarly for $y$ and $z ^ { - }$ ). Identify opposite faces of the cube so that a geodesic exiting across one face enters across the other. The result is topologically a three-torus: a “closed universe”with finite volume,with flat, Minkowskii geometry,and with a form that changes not at all as Lorentz time $t$ passes (no expansion, no contraction).

# $\$ 123$ .RIEMANN NORMAL COORDINATES

In curved spacetime one can never find a coordinate system with ${ T ^ { \alpha } } _ { \beta \gamma } = 0$ everywhere. But one can always construct local inertial frames at a given event $\mathcal { P } _ { 0 }$ ; and as viewed in such frames,free particles must move along straight lines,at least locally-which means $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ must vanish,at least locally.

A very special and useful realization of such a local inertial frame is a Riemannnormal coordinate system. Pick an event $\mathcal { P } _ { 0 }$ and a set of basis vectors $\{ \pmb { e } _ { \alpha } ( \mathcal { P } _ { 0 } ) \}$ to be used there by an inertial observer. Fill spacetime, near ${ \mathcal { P } } _ { 0 }$ ,with geodesics radiating out from $\mathcal { P } _ { 0 }$ like the quills of a hedgehog or porcupine. Each geodesic is determined by its tangent vector $\pmb { v }$ at $\mathcal { P } _ { 0 }$ ; and the general point on it can be denoted

Riemann normal coordinates: arealization of local inertial frames

Geometric construction of Riemann normal coordinates

$$
\begin{array} { r }  \begin{array} { r l } & { \mathcal { P } = \mathcal { G } ( \lambda ; \pmb { v } ) . } \\ & { \Big [ \mathrm { a f f i n e ~ p a r a m e t e r } ; } \\ & { \Big [ \mathrm { t e l l s ~ ^ { \ast \ast } w h e r e ^ { \circ , ~ } o n ~ g e o d e s i c } \Big ] } \end{array} \begin{array} { r l } & { \Big [ \mathrm { ~ t a n g e n t ~ v e c t o r ~ a t ~ \mathcal { P } _ { 0 } ; ~ } } \\ & { \Big [ \mathrm { t e l l s ~ ^ { \ast \ast } w h i c h ~ g e o d e s i c } ^ { \prime } \end{array} \Big ) } \end{array}
$$

Actually, this gives more geodesics than are needed. One reaches the same point after parameter length $^ { \frac { 1 } { 2 } \lambda }$ if the initial tangent vector is $2 v$ ,as one reaches after $\lambda$ if the tangent vector is $\pmb { \nu }$

$$
\mathcal { G } ( \lambda ; \pmb { v } ) = \mathcal { G } \left( \frac { 1 } { 2 } \lambda ; 2 \pmb { v } \right) = \mathcal { G } ( 1 ; \lambda \pmb { v } ) .
$$

Thus,by fixing $\lambda = 1$ and varying $\pmb { \nu }$ in all possible ways,one can reach every point in some neighborhood of $\mathcal { P } _ { 0 }$ .This is the foundation for constructing Riemann normal coordinates. Choose an event $\mathcal { P }$ .Find that tangent vector $\pmb { \nu }$ at $\mathcal { P } _ { 0 }$ for which $\mathcal { P } =$ $\mathcal { G } ( 1 ; \pmb { v } )$ Expand that $\pmb { \nu }$ in terms of the chosen basis and give its components the names $x ^ { \alpha }$ ：

$$
{ \mathcal { P } } = { \mathcal { G } } ( 1 ; x ^ { \alpha } \pmb { e } _ { \alpha } ) .
$$

The point $\mathcal { P }$ determines $x ^ { \alpha }$ uniquely (if $\mathcal { P }$ is near enough to $\mathcal { P } _ { 0 }$ that spacetime curvature has not caused geodesics to cross each other). Similarly, $x ^ { \alpha }$ determines $\mathcal { P }$ uniquely.Hence, $x ^ { \alpha }$ can be chosen as the coordinates of $\mathcal { P }$ -its“Riemann-normal coordinates,based on the event $\mathcal { P } _ { 0 }$ and basis $\{ \pmb { e } _ { \alpha } ( \mathcal { S } _ { 0 } ) \}$ ”

Equation (l1.26） summarizes Riemann-normal coordinates concisely. Other equations,derived in exercise l1.9, summarize their powerful properties:

$$
\begin{array} { c } { { { \pmb e } _ { \alpha } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = ( \partial / \partial x ^ { \alpha } ) _ { \mathcal { S } { \bf \rho } _ { 0 } } ; } } \\ { { { \cal T } ^ { \alpha } { } _ { \beta \gamma } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = 0 ; } } \\ { { { \cal T } ^ { \alpha } { } _ { \beta \gamma , \mu } ( { \mathcal { S } } { \bf \rho } _ { 0 } ) = - \displaystyle \frac { 1 } { 3 } ( R ^ { \alpha } { } _ { \beta \gamma \mu } + R ^ { \alpha } { } _ { \gamma \beta \mu } ) . } } \end{array}
$$

Mathematical properties of Riemann normal coordinates

If spacetime has a metric (as it does in actuality),and if the observer's frame at $\mathcal { P } _ { 0 }$ has been chosen orthonormal $( \pmb { e } _ { \alpha } \cdot \pmb { e } _ { \beta } = \eta _ { \alpha \beta } )$ ，then

$$
\begin{array} { c } { { g _ { \alpha \beta } ( \mathcal { S } _ { 0 } ) = \eta _ { \alpha \beta } , } } \\ { { g _ { \alpha \beta , \mu } ( \mathcal { S } _ { 0 } ) = 0 , } } \\ { { g _ { \alpha \beta , \mu \nu } ( \mathcal { S } _ { 0 } ) = \displaystyle - \frac { 1 } { 3 } ( R _ { \alpha \mu \beta \nu } + R _ { \alpha \nu \beta \mu } ) } } \\ { { \displaystyle = - \frac { 2 } { 3 } J _ { \alpha \beta \mu \nu } , } } \end{array}
$$

$$
R _ { \alpha \beta \gamma \delta } ( \mathring { \mathcal { S } } _ { 0 } ) = g _ { \alpha \mathfrak { s } , \beta \gamma } ( \mathring { \mathcal { S } } _ { 0 } ) - g _ { \alpha \gamma , \beta \mathfrak { s } } ( \mathring { \mathcal { S } } _ { 0 } ) .
$$

Othermathematical realizations of a local inertial frame

Here $J _ { \alpha \beta \mu \nu }$ are components of the Jacobi curvature tensor (see exercise l1.7).

Is this the onlycoordinatesystem that is locallyinertial at ${ \mathcal { P } } _ { 0 }$ (i.e., has ${ T ^ { \alpha } } _ { \beta \gamma } = 0$ there)and is tied to the basis vectors ${ \pmb { e } } _ { \alpha }$ there (i.e., has $\partial / \partial x ^ { \alpha } = \pmb { e } _ { \alpha }$ there)? No. But all such coordinate systems (called “normal coordinates") will be the same to second order:

$$
\begin{array} { r } { x _ { \mathrm { N E W } } ^ { \alpha } ( \mathcal P ) = x _ { \mathrm { O L D } } ^ { \alpha } ( \mathcal P ) + \mathrm { c o r r e c t i o n s ~ o f ~ o r d e r } ~ ( x _ { 0 \mathrm { L D } } ^ { \alpha } ) ^ { 3 } . } \end{array}
$$

Moreover, only those the same to third order,

$$
\begin{array} { r } { x _ { \mathrm { N E W } } ^ { \alpha } ( \mathcal P ) = x _ { \mathrm { O L D } } ^ { \alpha } ( \mathcal P ) + \mathrm { c o r r e c t i o n s ~ o f ~ o r d e r ~ } ( x _ { 0 \mathrm { L D } } ^ { \alpha } ) ^ { 4 } , } \end{array}
$$

will preserve the beautiful ties (l1.29) and (l1.32) to the Riemann curvature tensor.

EXERCISES

# Exercise 11.6. SYMMETRIES OF Riemann

(To be discussd in Chapter l3). Show that Riemann has the following symmetries:

$$
\begin{array} { r l } { R ^ { \alpha } { } _ { \beta \gamma \delta } = R ^ { \alpha } { } _ { \beta [ \gamma \delta ] } \quad } & { ( \mathrm { a n t i s y m m e t r i c ~ o n ~ l a s t ~ 2 ~ i n d i c e s } ) } \\ { R ^ { \alpha } { } _ { \{ \beta \gamma \delta \} } = 0 \quad } & { ( \mathrm { v a n i s h i n g ~ o f ~ c o m p l e t e l y ~ a n t i s y m m e t r i c ~ p a r t } ) } \end{array}
$$

# Exercise 11.7. GEODESIC DEVIATION MEASURES ALL CURVATURE COMPONENTS

The equation of geodesic deviation, written up to now in the form

or

$$
\begin{array} { c } { { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \pmb { R i } e m a n n \left( . . . , \pmb { u } , \pmb { n } , \pmb { u } \right) = 0 } } \\ { { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \pmb { \mathcal { A } } ( \pmb { n } , \pmb { u } ) \pmb { u } = 0 , } } \end{array}
$$

also lets itself be written in the Jacobi form $\begin{array} { r } { \pmb { \nabla } _ { \pmb { u } } \pmb { \nabla } _ { \pmb { u } } \pmb { n } + \mathcal { J } ( \pmb { u } , \pmb { u } ) \pmb { n } = 0 . } \end{array}$ Here $\mathcal { J } ( \pmb { u } , \pmb { v } )$ ,the“Jacobi curvature operator,”is defined by

$$
\mathcal { J } ( \pmb { u } , \pmb { v } ) \pmb { n } \equiv \frac { 1 } { 2 } \left[ \mathcal { R } ( \pmb { n } , \pmb { u } ) \pmb { v } + \mathcal { R } ( \pmb { n } , \pmb { v } ) \pmb { u } \right] ,
$$

and is related to the“Jacobi curvature tensor” by

$$
\begin{array} { r } { J a c o b i \left( . . . , n , u , v \right) \equiv \mathcal { J } ( u , v ) n , } \end{array}
$$

which implies

$$
{ J ^ { \mu } } _ { \nu \alpha \beta } = { J ^ { \mu } } _ { \nu \beta \alpha } = { \frac { 1 } { 2 } } ( R ^ { \mu } { } _ { \alpha \nu \beta } + R ^ { \mu } { } _ { \beta \nu \alpha } ) .
$$

(a) Show that $J ^ { \mu } { } _ { ( \alpha \beta \gamma ) } = 0$ follows from $R ^ { \mu } { } _ { \alpha \beta \gamma } = R ^ { \mu } { } _ { \alpha [ \beta \gamma ] } .$

(b) Show that by studying geodesic deviation (allowing arbitrary $\pmb { u }$ and $\pmb { n }$ in $\yen 1$ $\mathcal { J } ( u , u ) n = 0 )$ one can measure all components of Jacobi.

(c) Show that Jacobi contains precisely the same information as Riemann.[Hint: show that

$$
{ R ^ { \mu } } _ { \alpha \nu \beta } = { \frac { 2 } { 3 } } ( J ^ { \mu } { } _ { \nu \alpha \beta } - J ^ { \mu } { } _ { \beta \alpha \nu } ) ;
$$

this plus equation(11.36) for $J ^ { \mu } { } _ { \nu \alpha \beta }$ proves "same information content".] Hene, by studying geodesic deviation one can also measure all the components of Riemann.

(d) Show that the symmetry of $R ^ { \mu } { } _ { [ \nu \alpha \beta ] } = 0$ is essentialin theequivalence between Jacobi and Riemann by exhibiting proposed values for $R ^ { \mu } { } _ { \nu \alpha \beta } = - R ^ { \bar { \mu } } { } _ { \nu \beta \alpha }$ for which $R ^ { \mu } { } _ { [ \nu \alpha \beta ] } \neq 0$ ， and from which one would find $J ^ { \mu } { } _ { \nu \alpha \beta } = 0$

# Exercise 11.8. GEODESIC DEVIATION IN GORY DETAIL

Write out the equation of geodesic deviation in component form in a coordinate system. Expand all covariant derivatives (semicolon notation) in terms of ordinary (comma) derivatives and in terms of I's to show all $\boldsymbol { r }$ and a terms explicitly.

# Exercise 11.9. RIEMANN NORMAL COORDINATES IN GENERAL

Derive properties (11.27),(11.28),(11.29),(11.31),(11.32),and (11.32') of Riemann normal coordinates. Hint: Proceed as follows.

(a)From definition (11.26),derive $( \partial \mathcal { P } / \partial x ^ { \alpha } ) _ { \varphi _ { 0 } } = \pmb { \varrho } _ { \alpha } .$ (b) Similarly,from definition (I1.26),show that each of the curves $x ^ { \alpha } = v ^ { \alpha } \lambda$ (where the $v ^ { \alpha }$ are constants) is a geodesic through ${ \mathcal P _ { 0 } } .$ with affine parameter $\lambda$ (c） Show that $T ^ { \alpha } { } _ { \beta \gamma } ( \mathcal { P } _ { 0 } ) = 0$ by substituting $x ^ { \alpha } = v ^ { \alpha } \lambda$ into the geodesic equation. (d） Since the curves $x ^ { \alpha } = v ^ { \alpha } \lambda$ are geodesics for every choice of the parameters $v ^ { \alpha }$ ,they provide not only a geodesic tangent $\pmb { \upsilon } \equiv ( \partial / \partial \lambda ) _ { v ^ { \alpha } }$ ，but also several deviation vectors ${ \pmb N } _ { ( \alpha ) } \equiv ( \partial / \partial v ^ { \alpha } ) _ { \lambda }$ . Compute the components of these vectors in the Riemann normal coordinate system,and substitute into the geodesic deviation equation as written in exercise 11.8. (e) Equate to zero the coefficients of the zeroth and first powers of $\lambda$ in the geodesic deviation equation of part (d),using

$$
\left. T ^ { \alpha } { } _ { \beta \gamma } \right| _ { x ^ { \mu } = v ^ { \mu } \lambda } = \lambda v ^ { \mu } \bar {Gamma ^ { \alpha } } { } _ { \beta \gamma , \mu } ( \mathcal { S } \vec { \rho } _ { 0 } ) + O ( \lambda ^ { 2 } ) ,
$$

which is a Taylor series for $\boldsymbol { r }$ Inthis wayarrveatequatin (1.29)for $T ^ { \alpha } { } _ { \beta \gamma , \mu }$ in terms of the Riemann tensor.

(f） From equations (11.28),(l1.29),and (8.24) for the connection coeffcients in terms of the metric, derive equations (11.31), (11.32),and (11.32').

# Exercise 11.10. BIANCHI IDENTITIES

Show that the Riemann curvature tensor satisfies the following“Bianchi identities”

$$
R ^ { \alpha } { } _ { \beta [ \gamma \delta ; \epsilon ] } = 0 .
$$

The geometric meaning of these identities will be discussed in Chapter 15.[Hint: Perform the calculation at the origin of a Riemann normal coordinate system.]

# Exercise 11.11. CURVATURE OPERATOR ACTS ON 1-FORMS

Let $\mathcal { R } ( \pmb { u } , \pmb { v } )$ be the operator $\begin{array} { r } { \langle \hat { \mathcal { R } } ( \pmb { \mu } , \pmb { v } ) = [ \pmb { \nabla } _ { \pmb { u } } , \pmb { \nabla } _ { \pmb { v } } ] - \pmb { \nabla } [ \pmb { u } , \pmb { v } ] } \end{array}$ when acting on l-forms $\pmb { \sigma }$ (or other tensors) as well as on tangent vectors. Show that

$$
\langle \Re ( { \pmb u } , { \pmb v } ) { \pmb \sigma } , { \pmb w } \rangle = - \langle { \pmb \sigma } , \Re ( { \pmb u } , { \pmb v } ) { \pmb w } \rangle .
$$

Exercise 11.12. ROTATION GROUP:RIEMANN CURVATURE

[Continuation of exercises 9.13,9.14,and I0.17.] Calculate the components of the Riemann curvature tensor for the rotation group's manifold $S O ( 3 )$ ； use the basis of generators $\{ e _ { \alpha } \}$ · [Answer:

$$
R ^ { \alpha } { } _ { \beta \gamma \delta } = \frac { 1 } { 2 } \delta _ { \gamma \delta } ^ { \alpha \beta } ,
$$

where $\delta _ { \gamma \delta } ^ { \alpha \beta }$ is the permutation symbol defined in equation (3.50l):

$$
\delta _ { \gamma \delta } ^ { \alpha \beta } \equiv ( \delta ^ { \alpha } { } _ { \gamma } \delta ^ { \beta } { } _ { \delta } - \delta ^ { \alpha } { } _ { \delta } \delta ^ { \beta } { } _ { \gamma } ) .
$$

Note that this answer is independent of location $\mathcal { P }$ in the group manifold.]
