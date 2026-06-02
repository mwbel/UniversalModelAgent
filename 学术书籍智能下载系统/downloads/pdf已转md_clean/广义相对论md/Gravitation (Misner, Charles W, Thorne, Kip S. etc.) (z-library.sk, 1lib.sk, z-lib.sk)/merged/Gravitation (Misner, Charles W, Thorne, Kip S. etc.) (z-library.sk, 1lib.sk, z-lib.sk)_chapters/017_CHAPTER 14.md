CHAPTER 14

CALCULATION OF CURVATURE

# $\$ 14.1$ . CURVATURE AS A TOOL FOR UNDERSTANDING PHYSICS

Elementary physics sometimes allows one to shortcircuit any systematized calculation of curvature (frequency of oscillation of test particle; tide-producing acceleration near a center of attraction; curvature of a closed 3-sphere model universe; effect of parallel transport on gyroscope or vector; see Figures 1.1, 1.10,and 1.12,and Boxes 1.6 and 1.7); but on other occasions a calculation of curvature is the quickest way into the physics.This chapter is designed for such occasions. It describes three ways to calculate curvature and gives the components of the Einstein curvature tensor for a plane gravitational wave (Box 14.4, equation 5), for the Friedmann geometry of the universe (Box 14.5),and for Schwarzschild geometry, both static (exercise 14.13) and dynamic (exercise 14.16). These and other calculations of curvature elsewhere are indexed under “curvature tensors.”

It is enough to look at an expression for a 4-geometry as complicated as

This chapter is entirely Track 2. Chapter 4 (differential forms)   
and Chapter 10,11,and 13   
(ditferential geometry) are   
necessary preparation for   
\$514.5-14.6. This chapter is needed as   
preparation for Chapter 15   
(Bianchi identities). It will be helpful in many   
applications of gravitation   
theory (Chapters 23-40).

$$
\begin{array} { c } { { d s ^ { 2 } = - ( x / 3 ^ { 1 / 2 } L + y ^ { 2 } / 1 2 L ^ { 2 } ) ^ { - 3 / 2 } \Big ( \int \frac { v d z } { z } \Big ) ^ { - 1 } ( - z / L ) ^ { 3 ^ { - 1 / 2 } } d t ^ { 2 } } } \\ { { + ( x / 3 ^ { 1 / 2 } L + y ^ { 2 } / 1 2 L ^ { 2 } ) ^ { 1 + 3 ^ { 1 / 2 } } \Big ( \int \frac { v d z } { z } \Big ) ^ { 1 + 2 / 3 ^ { 1 / 2 } } ( - z / L ) _ { - \frac { 1 } { - 4 } > ^ { 3 - 1 / 2 } } ^ { - 1 + 3 ^ { - 1 / 2 } } d x ^ { 2 } } } \\ { { - \ - \overbrace { { ( x / 3 ^ { 1 / 2 } L + y ^ { 2 } / 1 2 L ^ { 2 } ) ^ { - 4 / 3 ^ { 1 / 2 } } } \Big ( \int \frac { v d z } { z } \Big ) ^ { 1 + 2 / 3 ^ { 1 / 2 } } ( - z / L ) ^ { - 3 ^ { 1 / 2 } } d y ^ { 2 } } ^ { + ( x / 3 ^ { 1 / 2 } ) ^ { - 3 ^ { 1 / 2 } } } ( - z / L ) ^ { - 3 ^ { 1 / 2 } } d y ^ { 2 } } } \\ { { + ( x / 3 ^ { 1 / 2 } L + y ^ { 2 } / 1 2 L ^ { 2 } ) ^ { 3 + 3 ^ { 1 / 2 } } \Big ( \int \frac { v d z } { z } \Big ) ^ { 1 + 2 / 3 ^ { 1 / 2 } } ( - z / L ) ^ { - 2 - 3 ^ { - 1 / 2 } } \times } } \\ { { \times \Big ( \frac { v ^ { 2 } - 1 } { - 1 - z / L } \Big ) d z ^ { 2 } } } \end{array}
$$

# Situations in which one must compute curvature

[Harrison (1959)] to realize that one might understand the physical situation better if one knew what the curvature is; similarly with any other complicated expressions for metrics that arise from solving Einstein's equations or that appear undigested in the literature. In any such case, the appropriate method often is: curvature first, understanding second.

Curvature is the simplest local measure of geometric properties (see Box 14.1). Curvature is therefore a good first step toward a more comprehensive picture of the spacetime in question.

One sometimes has an expression for a spacetime metric first, and then makes calculations of curvature to understand it. But more often one makes calculations of curvature, subject to specified conditions of symmetry in space and time,as an aid in arriving at an expression for a physically interesting metric (stars,Chapters 23 to 26;model cosmologies, Chapters 27 to 30; collapse and black holes,Chapters 31 to 34; and gravitational waves, Chapters 35 to 37).

"Standard procedure" for computing curvature

The basic “standard procedure for computing curvature" is illustrated in Box 14.2. Two formulas in Box 14.2, derived previously,are used in succession. The first (equations 1 and 2) has the form $\boldsymbol { r } \sim g \odot \boldsymbol { g }$ and provides the $T ^ { \mu } { } _ { \alpha \beta }$ . The other (equation 3) has the form $R \sim \partial { \cal r } + { \cal r } ^ { 2 }$ and gives the curvature components $R ^ { \mu } { } _ { \nu \alpha \beta }$

Methods of displaying curvature formulas

After the curvature components have been computed, there are helpful ways to present the results. (l) Form the Rici tensor $R _ { \mu \nu } = { R ^ { \alpha } } _ { \mu \alpha \nu }$ and the scalar curvature $R = { R ^ { \mu } } _ { \mu }$ (2)Fomotherivariansuhas $R ^ { \mu \nu } { } _ { \alpha \beta } R ^ { \alpha \beta } { } _ { \mu \nu } .$ (3)Form components $R ^ { \hat { \mu } \hat { \nu } } { } _ { \hat { \alpha } \hat { \beta } }$ in a judiciously chosen orthonormal frame $\pmb { \omega } ^ { \hat { \alpha } } = L _ { \beta } ^ { \hat { \alpha } } d x ^ { \beta }$ ,and (4) display $R ^ { \{ \hat { \mu } \hat { \nu } \} } { } _ { \{ \hat { \alpha } \hat { \beta } \} }$ as a $6 \times 6$ matrix (in four dimensions; a $3 \times 3$ matrix in three dimensions) where $[ \hat { \mu } \hat { \nu } ] = [ \hat { 0 } \hat { 1 } ] ,$ [02],[03],[23],[31],[12] labels the rows and $[ \hat { \alpha } \hat { \beta } ]$ labels the columns (exercises 14.14 and 14.15). (5) Last, but by far the most important for general relativity,form the Einstein tensor $G ^ { \hat { \mu } } { } _ { \hat { \nu } }$ as described in $\ S 1 4 . 2$

The method of computation outlined above and described in more detail in Box 14.2 is used wherever it is quicker to employ a standard method than to learn or invent a better method. The standard method is always preferable for the student in a short course where physical insight has higher priority than technical facility. It is,however,a dull method, better suited to computers than to people. Fven.the algebra can be handled by a computer (see Box 14.3).

Computation of curvature using a computer

# EXERCISES

# Exercise 14.1. CURVATURE OF A TWO-DIMENSIONAL HYPERBOLOID

Compute the curvature of the hyperboloid $t ^ { 2 } - x ^ { 2 } - y ^ { 2 } = T ^ { 2 } = \mathsf { c o n s t }$ in $2 + 1$ Minkowski spacetime with $d s _ { 3 } \sp 2 = - d t \sp 2 + d x \sp 2 + d y \sp 2$ .First show that intervals within this two-dimensional surface can be expressed in_the form $d s ^ { 2 } = T ^ { 2 } ( d \alpha ^ { 2 } + \sinh ^ { 2 } \alpha \ d \phi ^ { 2 } )$ bya suitable choice of coordinates $\pmb { \alpha }$ ， $\phi ,$ on the hyperboloid.

# Exercise 14.2. RIEMANNIAN CURVATURE EXPRESSIBLE IN TERMS OF RICCI CURVATURE IN TWO AND THREE DIMENSIONS

In two dimensions,there is only one independent curvature component, $\pmb { R _ { 1 2 1 2 } }$ Evidently the single scalar quantity $\pmb R$ must carry the same information. The two-dimensional identity $R _ { \mu \nu \alpha \beta } = { \scriptstyle { \frac { 1 } { 2 } } } R ( g _ { \mu \alpha } { \dot { g _ { \nu \beta } } } - { \dot { g _ { \mu \beta } } } g _ { \nu \alpha } )$ is established by noting that it is the only tensor formula giving

(continued on page 343)

# Box 14.1 PERSPECTIVES ON CURVATURE

1. Historical point of departure: a curved line on a plane. There is no way to define the curvature of a line by measurements confined to ("intrinsic to"） the line itself. One needs,for example, the azimuthal bearing $\pmb \theta$ of the tangent vector relative to a fixed direction in the plane,as a function of proper distance s measured along the curve; thus, $\theta = \theta ( s )$ Then curvature $\kappa$ and its reciprocal, the radius of curvature $\pmb { \rho }$ ，are given by $\kappa ( s ) =$ $1 / \rho ( s ) = d \theta ( s ) / d s$ .Alternatively,one can examine departure, $y$ ,measured normally off from the tangent line as a function of distance $_ x$ measured along that tangent line; then $\kappa = 1 / \rho = d ^ { 2 } y / d x ^ { 2 }$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/f1173f8cea472ed8e750a7aced1048a91abfccb5d03be6530a830110b43e27ab.jpg)

2. This concept was later extended to a curved surface embedded in flat (Euclidean) 3-space. Departure, $z$ ,of the smooth curved surface from the flat surface tangent to it at a given point is described in the neighborhood of that point by the quadratic expression

$$
z = { \frac { 1 } { 2 } } a x ^ { 2 } + b x y + { \frac { 1 } { 2 } } c y ^ { 2 } .
$$

Rotation of the axes by an appropriate angle $\pmb { \alpha }$ ，

$$
\begin{array} { l } { { x = \xi \cos \alpha + \eta \sin \alpha , } } \\ { { \ \gamma = - \xi \sin \alpha + \eta \cos \alpha , } } \end{array}
$$

reduces this expression to

$$
z = \frac { 1 } { 2 } \kappa _ { 1 } \xi ^ { 2 } + \frac { 1 } { 2 } \kappa _ { 2 } \eta ^ { 2 } ,
$$

with

and

$$
\begin{array} { r } { \kappa _ { 1 } = 1 / \rho _ { 1 } } \\ { \kappa _ { 2 } = 1 / \rho _ { 2 } } \end{array}
$$

representing the two “principal curvatures” of the surface.

3.Gauss (l827) conceived the idea of defining curvature by measurements confined entirely to the surface ("society of ants"). From a given point $\mathcal { P }$ on the surface, proceed on a geodesic on the surface for a proper distance e measured entirely within the surface. Repeat, starting at the original point but proceeding in other directions.

# Box 14.1 (continued)

Obtain an infinity of points. They define a “circle". Determine its proper circumference, again by measurements confined entirely to the surface. Using the metric corresponding to the embedding viewpoint

$$
\begin{array} { r c l } { { } } & { { } } & { { d s ^ { 2 } = d z ^ { 2 } + d \xi ^ { 2 } + d \eta ^ { 2 } ~ \mathrm { ( E u c l i d e a n ~ 3 \cdot s p a c e ) } } } \\ { { } } & { { } } & { { ~ \mathrm { / m e t r i c ~ i n t r i n s i c } } } \\ { { } } & { { } } & { { = [ ( \kappa _ { 1 } \xi ~ d \xi + \kappa _ { 2 } \eta ~ d \eta ) ^ { 2 } + ( d \xi ^ { 2 } + d \eta ^ { 2 } ) ] ~ \mathrm { ( \Phi _ { t o \ t h e \ c u r v e d } ~ ) } , } } \\ { { } } & { { } } & { { ~ \mathrm { / 2 - g e o m e t r y } } } \end{array}
$$

one can calculate the result of such an “intrinsic measurement.” One calculates that the circumference differs from the Euclidean value, $2 \pi \epsilon$ ,by a fractional correction that is proportional to the square of e; specifically,

$$
\operatorname* { L i m } _ { \epsilon \to 0 } \frac { 6 } { \epsilon ^ { 2 } } \Big ( 1 - \frac { \mathrm { c i r c u m f e r e n c e } } { 2 \pi \epsilon } \Big ) = \kappa _ { 1 } \kappa _ { 2 } = \frac { 1 } { \rho _ { 1 } \rho _ { 2 } } = \mathsf { d e t } \binom { a } { b } \ _ { c } ^ { b } \Big ) .
$$

Note especially the first equality sign. Gauss did not conceal the elation he felt on discovering that something defined by measurements entirely within the surface agrees with the product of two quantities, $\kappa _ { 1 }$ and $\mathbf { \delta \kappa _ { 2 } } ,$ that individually demand for their definition measurements extrinsic to the surface.

4.The contrast between “extrinsic”and “intrinsic" curvature is summarized in the terms,

$$
\begin{array} { r l } & { ( \mathrm { e x t r i n s i c ~ c u r v a t u r e } ) = \kappa = ( \kappa _ { 1 } + \kappa _ { 2 } ) ( \mathrm { c m } ^ { - 1 } ) , } \\ & { \qquad \left( \mathrm { i n t r i n s i c ~ o r ~ G a u s s i a n } \right) = \kappa _ { 1 } \kappa _ { 2 } ( \mathrm { c m } ^ { - 2 } ) } \\ & { \qquad \mathrm { c u r v a t u r e } } \end{array}
$$

□

(the latter being identical with half the scalar curvature invariant, $R ,$ of the 2-geometry). Draw a 3:4:5 triangle on a flat piece of paper; then curl up the paper. The Euclidean 2-geometry intrinsic to the piece of paper is preserved by this bending. The Gaussian curvature intrinsic to the surface remains unaltered; it keeps the Euclidean value of zero $( \pmb { \kappa _ { 2 } }$ non-zero; $\kappa _ { 1 }$ ,zero; product, $\kappa _ { 1 } \kappa _ { 2 } =$ zero). However, the extrinsic curvature is changed from $\boldsymbol { \kappa } _ { 1 } + \boldsymbol { \kappa } _ { 2 } = 0$ to a non-zero value, $\kappa _ { 1 } +$ $\kappa _ { 2 } \neq 0$

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/03535e3bb5ff63ec3544c5b66f06647ea56e2a8c14f3dc10424a053b5a488ba7.jpg)

5. The curvature dealt with in this chapter is curvature intrinsic to spacetime; that is,curvature defined without any use of, and repelling every thought of, any embedding in any hypothetical higher-dimensional fat manifold (concept of Riemann,

Clifford, and Einstein that geometry is a dynamic participant in physics, not some God-given perfection above the battles of matter and energy).

6. The curvature of the geometry of spacetime imposes curvature on any spacelike slice(3-geometry; "initial-value hypersurface") through that spacetime (see “relations of Gauss and Codazzi’ in Chapter 21, on the initial-value problem of geometrodynamics).

7. Rotation of a vector transported parallel to itself around a closed loop provides a definition of curvature as useful in four and three as in two dimensions. (In a curved two-dimensional geometry,at a point there is only one plane. Consequently only one number is required to describe the Gaussian curvature there. In three and four dimensions, there are more independent planes through a point and therefore more numbers are required to describe the curvature.） In the diagram, start with a vector at position l (North Pole). Transport it parallel to itself (position 2,3,...) around a $9 0 ^ { \circ } - 9 0 ^ { \circ } - 9 0 ^ { \circ }$ spherical triangle. It arrives back at the starting point (position 4） turned through $9 0 ^ { \circ }$ ：

$$
{ \binom { \mathrm { G a u s s i a n } } { \mathrm { c u r v a t u r e } } } = { \frac { { \binom { \mathrm { a n g l e ~ t u r n e d } } { \mathrm { t h r o u g h } } } } { { \binom { \mathrm { a r e a ~ c i r c u m . } } { \mathrm { n a v i g a t e d } } } } } = { \frac { ( \pi / 2 ) } { ( 1 / 8 ) ( 4 \pi a ^ { 2 } ) } } = { \frac { 1 } { a ^ { 2 } } }
$$

(positive; sense of rotation same as sense of circumnavigation).

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/bf90df1a75aa724eb7fe4254d537d0401e7aa9a3dceb6d2e27e8689ae01c9173.jpg)

8. Still staying for simplicity with a curved twodimensional manifold, describe the curvature of the 2-surface as a 2-form ("box-like structure") defined over the entire surface. The number of boxes enclosed by any given route gives immediately the angle in radians (or tenths or hundredths of a radian, etc., depending on chosen fineness of subdivision) turned through by a vector carried parallel to itself around that route. The contribution of a given box is counted as positive Or negative depending on whether the sense of the arrow marked on it (see magnified view) agrees or disagrees with the sense of circumnavigation of the route.

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/656dfca2da3c646e152f08364eb5d3ebc2b9089e1aa103ea0f012c4a8b306ca0.jpg)

![](../chunks/Gravitation (Misner, Charles W, Thorne, Kip S. etc.) (z-library.sk, 1lib.sk, z-lib.sk)_part_0006_pages_0351-0420/auto/images/b30745fc4159937974f2480fd8935b85046e416a157775f09a32eae8bc89cd58.jpg)  
Box 14.1 (continued)

9. Curvature 2-form for the ilustrated surface of rotational symmetry ("pith helmet"） with metric $d s ^ { 2 } = d \sigma ^ { 2 } + r ^ { 2 } ( \sigma ) d \phi ^ { 2 }$ is

$$
c u r v a t u r e = - \frac { 1 } { r } \frac { d ^ { 2 } r } { d \sigma ^ { 2 } } d \sigma \wedge r d \phi
$$

(positive on crown of helmet, negative around brim,as indicated by sense of arrows in the “boxes of the 2-form”shown at left).“Meaning”of $r$ is illustrated by imbedding the surface in Euclidean 3-space, a convenience for visualization; but more important is the idea of a 2-geometry defined by measurements intrinsic to it, with no embedding.

10. How lengths ("metric") determine curvature in quantitative detail is shown nowhere more clearly than in this two-dimensional example,a model for“what is going on behind the scene” in the mathematical calculations done in this chapter with 1-forms and 2-forms in four-dimensional spacetime.

a. Net rotation in going around element of surface $\mathcal { Q B } \mathcal { Q B } \overline { { { \mathcal { Q } } } } \mathcal { Q }$ is $\delta - { \overline { { \delta } } }$ (no turn of vector to left or to right in its transport along a meridian $\pmb { \mathcal { Q } } \overline { { \pmb { \mathcal { Q } } } }$ or $\mathcal { B } \overline { { \mathcal { B } } }$ ).

b. Rotation of vector in going from d to B,relative to coordinate system (directions of meridians), is

$$
( { \mathrm { a n g l e ~ } } \delta ) = { \frac { { \mathrm { a r c } } } { { \mathrm { l e n g t h } } } } = { \frac { r ( \sigma + d \sigma ) A \phi - r ( \sigma ) A \phi } { d \sigma } } = \left( { \frac { d r } { d \sigma } } \right) _ { \sigma } A \phi .
$$

c. Rotation of vector in going from $\vec { \mathcal { a } }$ t0 $\boldsymbol { \overline { { \mathcal { B } } } }$ is similarly

$$
( \mathrm { a n g l e ~ } \overline { { { \delta } } } ) = \left( \frac { d r } { d \sigma } \right) _ { \sigma + \Delta \sigma } \Delta \phi .
$$

d. Thus net rotation is:

$$
\delta - \overline { { { \delta } } } = - \left( \frac { d ^ { 2 } r } { d \sigma ^ { 2 } } \right) _ { \sigma } \Delta \sigma \Delta \phi .
$$

e. Expressedas a form,this gives immediately equation (l).

f. Ideas and calculations are more complicated in four dimensions, primarily because one has to deal with different choices for the orientation of the surface to be studied at the point in question.

11. Translation of these geometric ideas into the language of forms is most immediate when one stays with this example of two dimensions.A sample vector $A ^ { i } = ( A ^ { 1 } , A ^ { 2 } )$ carried around the boundary of an element of surface comes back to its starting point slightly changed in direction:

$$
- \left( { \begin{array} { l } { \mathrm { c h a n g e } } \\ { \mathrm { i n } \ A ^ { i } } \end{array} } \right) = { \mathcal { R } } ^ { i } { } _ { j } A ^ { j } .
$$

a. To be more specific, it is convenient to adopt as the basis l-forms ${ \pmb { \omega } } ^ { \hat { 1 } } = { \pmb { d } } { \pmb { \sigma } }$ and $\omega ^ { \hat { 2 } } = r d \bar { \phi }$ and have $A ^ { \hat { 1 } }$ as the component of $\pmb { A }$ along the direction of increasing $\pmb { \sigma }$ ， $A ^ { \hat { 2 } }$ as the component of $\pmb { A }$ along the direction of increasing $\phi$ The matrix $\mathcal { R } _ { \ j } ^ { \ i }$ is a rotation matrix, which produces a change in direction but no change in length (zero diagonal components); thus here

$$
| | \mathcal { R } ^ { \hat { i } } { } _ { \hat { \mathfrak { j } } } | | = \bigg | \bigg | \bigg | { - } \mathcal { R } ^ { \hat { 1 } } { } _ { \hat { 2 } } \quad \begin{array} { c c } { \mathcal { R } ^ { \hat { 1 } } { } _ { \hat { 2 } } } \\ { 0 } \end{array} \bigg | \bigg | \mathrm { ~ . ~ }
$$

In this example, $\mathcal { R } ^ { \hat { 1 } } { } _ { \hat { 2 } }$ evidently represents the angle through which the vector $\pmb { A }$ turns on transport parallel to itself around the element of surface.

b. So far the rotation is “indefinite” because the size of the element of surface has not yet been specified. It is most conveniently conceived as an elementary parallelogram, defined by two vectors ("bivector"). Thus $\mathcal { R } ^ { \widehat { i } } { } _ { \widehat { j } } ,$ or, specifically, the one element that counts, $\mathcal { R } ^ { \hat { 1 } } { } _ { \hat { 2 } }$ (the “angle of rotation"), has to be envisaged as a mathematical object (“2-form") endowed with two slots, into which these two vectors are inserted to get a definite number (angle in radians). In the example of the pith helmet, one has, from equation (l)

$$
\mathcal { R } ^ { \hat { 1 } } { } _ { \hat { 2 } } = - \frac { 1 } { r } \frac { d ^ { 2 } r } { d \sigma ^ { 2 } } \pmb { \omega } ^ { \hat { 1 } } \wedge \pmb { \omega } ^ { \hat { 2 } } .
$$

Thus the ${ \mathcal R } ^ { \mu } { } _ { \nu }$ in the text are called“curvature 2-forms.”

# Box 14.1 (continued)

c. The text tells one how to read out of such expressions the.components of the Riemann curvature tensor; for example here,

$R ^ { \hat { 1 } } { } _ { \hat { 2 } \hat { 1 } \hat { 2 } } = - R ^ { \hat { 1 } } { } _ { \hat { 2 } \hat { 2 } \hat { 1 } } = ( - 1 / r ) ( d ^ { 2 } r / d \sigma ^ { 2 } )$ (coefficients of $\mathbf { \Delta } \mathbf { \omega } ^ { \hat { 1 } } \wedge \mathbf { \omega } \mathbf { \omega } ^ { \hat { 2 } }$ or ${ \pmb { \omega } } ^ { 2 } \wedge { \pmb { \omega } } ^ { \hat { 1 } } ,$ d. Generalizing to four dimensions,one understands by $R ^ { \alpha } { } _ { \beta \mu \nu }$ the factor that one has to multiply by three numbers to obtain a fourth. The number obtained is the change (with reversed sign） that takes place in the $\pmb { \alpha }$ th component of a vector when that vector is transported parallel to itself around a closed path, defined, for example, by a parallelogram built from two vectors ${ \pmb u }$ and $\pmb { \nu } .$ The factors that multiply $R ^ { \alpha } { } _ { \beta \mu \nu }$ are (l) the component of the vector $\pmb { A }$ in the $\beta$ th direction and (2,3) the $\mu \nu$ component of the extension of the parallelogram, $( u ^ { \mu } v ^ { \nu } - u ^ { \nu } v ^ { \mu } )$ . Thus

$$
\ S A ^ { \alpha } = - R ^ { \alpha } { } _ { \beta \mid \mu \nu \mid } A ^ { \beta } ( u ^ { \mu } v ^ { \nu } - u ^ { \nu } v ^ { \mu } ) .
$$

# Box 14.2 STRAIGHTFORWARD CURVATURE COMPUTATION. (Illustratod for a Globe)

The elementary and universally applicable method for computing the components $R ^ { \mu } { } _ { \nu \alpha \beta }$ of the Riemann curvature tensor starts from the metric components $g _ { \mu \nu }$ in a coordinate basis, and proceeds by the following scheme:

$$
g _ { \mu \nu } { \overset { \overset { \underset { r  \hat { \alpha } } { } } { \longrightarrow } } { \Gamma } } _ { \mu \alpha \beta } { \longrightarrow } \overset { \overset { \underset { R  \hat { \alpha } } { } } { \longrightarrow } { \Gamma ^ { \mu } } { } _ { \alpha \beta } }  \overset { \overset { R \sim \hat { \alpha } T + \overset { \underset { r  } { } } { \longrightarrow } } { \longrightarrow } { \overset { \underset { R ^ { \mu } } { } } { \longrightarrow } { } \overset { \quad } { \longrightarrow } } { \overset { } { \longrightarrow } } { \overset { } { \underset { p \alpha \beta } { } } } } .
$$

The formulas required for these three steps are

$$
\begin{array} { l l } { { \displaystyle { T _ { \mu \alpha \beta } = \frac { 1 } { 2 } \left( \frac { \partial g _ { \mu \alpha } } { \partial x ^ { \beta } } + \frac { \partial g _ { \mu \beta } } { \partial x ^ { \alpha } } - \frac { \partial g _ { \alpha \beta } } { \partial x ^ { \mu } } \right) } , } } \\ { { \displaystyle { T ^ { \mu } } _ { \alpha \beta } = g ^ { \mu \nu } { \cal T } _ { \nu \alpha \beta } , } } \end{array}
$$

and

$$
{ R ^ { \mu } } _ { \nu \alpha \beta } = { \frac { \partial { \Gamma ^ { \mu } } _ { \nu \beta } } { \partial x ^ { \alpha } } } - { \frac { \partial { \Gamma ^ { \mu } } _ { \nu \alpha } } { \partial x ^ { \beta } } } + { \Gamma ^ { \mu } } _ { \rho \alpha } { \Gamma ^ { \rho } } _ { \nu \beta } - { \Gamma ^ { \mu } } _ { \rho \beta } { \Gamma ^ { \rho } } _ { \nu \alpha } .
$$

The metric of the two-dimensional surface of a sphere of radius $^ { a }$ is

$$
d s ^ { 2 } = a ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

To compute the curvature by the standard method, use the formula for $d { \bf { \sigma } } ^ { 2 }$ as a table of ${ \pmb g } _ { { \pmb k } 1 }$ values. It shows that $g _ { \theta \theta } = a ^ { 2 }$ ， $g _ { \theta \phi } = 0$ ， $g _ { \phi \phi } = a ^ { 2 } \sin ^ { 2 } \theta$ . Compute the six possible different $T _ { j k ! } = { \cal T } _ { j ! k }$ (there will be 40 in four dimensions） from formula

(1). Thus

$$
\begin{array} { l } { { { \cal { r } } _ { \theta \phi \phi } = - a ^ { 2 } \mathrm { s i n } \theta \cos \theta = - { \cal { r } } _ { \phi \phi \theta } , } } \\ { { { \cal { r } } _ { \theta \theta \theta } = { \cal { r } } _ { \phi \phi \phi } = 0 , } } \\ { { { \cal { r } } _ { \theta \theta \phi } = { \cal { r } } _ { \phi \theta \theta } = 0 . } } \end{array}
$$

Raise the first index:

$$
\begin{array} { l } { { { \cal T } ^ { \theta } { } _ { \phi \phi } = - \sin \theta \cos \theta , } } \\ { { { \cal T } ^ { \phi } { } _ { \phi \theta } = \cot \theta , } } \\ { { { \cal T } ^ { \theta } { } _ { \theta \theta } = { \cal T } ^ { \theta } { } _ { \theta \phi } = 0 = { \cal T } ^ { \phi } { } _ { \theta \theta } = { \cal T } ^ { \phi } { } _ { \phi \phi } . } } \end{array}
$$

Choose a suitable curvature component (one that is not automatically zero by reason of the elementary symmetry $R _ { \mu \nu \alpha \beta } = R _ { [ \mu \nu ] [ \alpha \beta ] }$ , nor previously computed in another form, as by $R _ { \mu \nu \alpha \beta } = R _ { \alpha \beta \mu \nu } )$ In this two-dimensional example, there is only one choice (compared to 21 such computations in four dimensions);it is

$$
\begin{array} { l } { { R ^ { \theta } { } _ { \phi \theta \phi } = \frac { \partial { \Gamma ^ { \theta } } _ { \phi \phi } } { \partial \theta } - \frac { \partial { \Gamma ^ { \theta } } _ { \phi \theta } } { \partial \phi } + { \Gamma ^ { \theta } } _ { k \theta } { \Gamma ^ { k } } _ { \phi \phi } - { \Gamma ^ { \theta } } _ { k \phi } { \Gamma ^ { k } } _ { \phi \theta } } } \\ { ~ = \frac { \partial { \Gamma ^ { \theta } } _ { \phi \phi } } { \partial \theta } - 0 + 0 - { \Gamma ^ { \theta } } _ { \phi \phi } { \Gamma ^ { \phi } } _ { \phi \theta } } \\ { ~ = \sin ^ { 2 } \theta - \cos ^ { 2 } \theta + \sin \theta \cos \theta \cot \theta ; } \end{array}
$$

so

or

$$
\begin{array} { r } { { R ^ { \theta } { } _ { \phi \theta \phi } } = \sin ^ { 2 } \theta } \\ { \displaystyle } \\ { { R ^ { \theta \phi } { } _ { \theta \phi } } = \frac { 1 } { a ^ { 2 } } . } \end{array}
$$

Contraction gives the components of the Rici tensor,

$$
R ^ { \theta } { } _ { \theta } = R ^ { \phi } { } _ { \phi } = \frac { 1 } { a ^ { 2 } } , \qquad R ^ { \theta } { } _ { \phi } = 0 ,
$$

and further contraction gives the curvature scalar

$$
R = 2 / a ^ { 2 } .
$$

A convenient orthonormal frame in this manifold is

$$
\begin{array} { r } { \pmb { \omega } ^ { \hat { \theta } } = a \pmb { \alpha } \pmb { \theta } , \qquad \pmb { \omega } ^ { \hat { \phi } } = a \sin \theta \pmb { \alpha } \pmb { \theta } . } \end{array}
$$

More generally one writes $\omega ^ { \hat { \alpha } } = L _ { \beta } ^ { \hat { \alpha } } d x ^ { \beta }$ . To transform the curvature tensor to orthonormal components in this simple but illuminating example of a diagonal metric requires a single normalization factor for each index on a tensor. Thus = av,u= asinθ vΦ,Uθ = a-1uθ,U= (asin0)-1v.Similarly，from R= $\sin ^ { 2 } \theta$ one finds the components of the curvature tensor,

$$
R ^ { \hat { \theta } } { } _ { { \hat { \phi } } { \hat { \theta } } { \hat { \phi } } } = { \frac { 1 } { a ^ { 2 } } } = R ^ { { \hat { \theta } } { \hat { \phi } } } { } _ { { \hat { \theta } } { \hat { \phi } } } ,
$$

in the orthonormal frame.

# Box 14.3 ANALYTICAL CALCULATIONS ON A COMPUTER

Research in gravitation physics and general relativity is sometimes beset by long calculations,requiring meticulous care,of such quantities as the Einstein and Riemann curvature tensors for a given metric, or the divergence of a given stressenergy tensor, or the Newman-Penrose tetrad equations under given algebraic assumptions. Such calculations are sufficiently straightforward and deductive in logical structure that they can be handled by a computer. Since 1966,computers have been generally taking over such tasks.

There are several computer languages in which the investigator can program his analytic calculations. The computer expert may wish to work in a machine-oriented language such as LISP [see, e.g.，the work of Fletcher (l966) and of Hearn (1970)]. However,most appliers of relativity will prefer user-oriented languages such as REDUCE [created by Hearn (l97O) and available for the IBM 360 and 370,and the PDP 10 computers], ALAM [created by D'Inverno (l969) and available on Atlas computers], CAMAL [created by Barton, Bourne,and Fitch (l97O) and available on Atlas computers], and FORMAC [created by Tobey et al.(1967) and available on IBM 7090,7094,360, and 370j. For'a review of activity in this area, see Barton and Fitch (l97l). Here we describe only FORMAC. It is the most widely available and widely used of the languages; but it is probably not the most powerful [see,e.g., D'Inverno (1969)]. FORMACis to analytic work what the earliest and most primitive versions of FORTRAN were to numerical work.

FORMAC manipulates algebraic expressions involving: numerical constants,such as $1 / 3$ ; symbolic constants, such as $\pmb { x }$ or $\pmb { u }$ ; specific elementary functions, such as sin $( u )$ or exp $( x )$ ; and symbolic functions of several variables, such as $f ( x , \pmb { u } )$ or $\pmb { g } ( \pmb { u } )$ For example,it can add $a x + b x ^ { 2 }$ to $^ { 2 x + }$ $( 3 + b ) x ^ { 2 }$ and get $( a + 2 ) x + ( 3 + 2 b ) x ^ { 2 }$ it can take the partial derivative of $x ^ { 2 } u f ( x , u ) + \cos { ( x ) }$ with respect to $_ x$ and get

$$
2 x u f ( x , u ) + x ^ { 2 } u \partial f ( x , u ) / \partial x - \sin { ( x ) } .
$$

It can do any algebraic or differential-calculus computation that a human can do-but without making mistakes! Unfortunately, it cannot integrate analytically； integration requires inductive logic rather than deductive logic.

PL/l is a language that can be used simultaneously with FORMAC or independently of it. PL/l manipulates strings of characters-e.g., $^ { 6 4 } Z / 1 \times 2 9 - \overline { { + } } / .$ ” It knows symbolic logic； it can tell whether two strings are identical; it can insert new characters into a string or remove old ones; but it does not know the rules of algebra or differential calculus.Thus,its primary use is as an adjunct to FORMAC (though from the viewpoint of the computer system FORMAC is an adjunct of PL/1).

FORMAC programs for evaluating Einstein's tensor in terms of given metric components and for doing other calculations are available from many past users [see,e.g.,Fletcher,Clemens, Matzner, Thorne,and Zimmerman (l967)；Ernst (1968)；Harrison (1970)]. However, programming in FORMAC is sufficiently simple that one ordinarily does not have difficulty creating one's own program to do a given task. If a difficulty does arise,it may be because the analytic computation exhausts the core of the computer. It is easy to create an expression too large to fit in the core of any existing computer by several differentiations of an expression half a page long!

Users of FORMAC， confronted by coreexhaustion, have devised several ways to solve their problems. One is to remove unneeded parts of the program and of the FORMAC system from the core. Routines called PURGE and KILL have been developed for this purpose by Clemens and Matzner (l967). Another is to create the answer to a given calculation in manageable-sized pieces and output those pieces from the computer's core onto its disk. One must then add all the pieces together-a task that is impossible using FORMAC alone,or even FORMAC plus PL/1, but a task that James Hartle has solved [see Hartle and Thorne (l974)] by using a combination of FORMAC,PL/l,and IBM data-manipulation routines called SORT.

$R _ { \mu \nu \alpha \beta }$ as a linear function of $\pmb R$ ,constructed from $\pmb R$ and the metric alone,and with the correct contracted value $R ^ { \mu \nu } { } _ { \mu \nu } = R$ Establish acorresponding three-dimensional identity expressing $R _ { \mathrm { i } j k l }$ in terms of the Ricci tensor $R _ { j k }$ and the metric.

ExerCise 14.3. CURVATURE OF 3-SPHERE IN ORTHONORMAL FRAME Compute the curvature tensor for a 3-sphere

$$
d s ^ { 2 } = a ^ { 2 } [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta \ d \phi ^ { 2 } ) ]
$$

or for a 3-hyperboloid

$$
d s ^ { 2 } = a ^ { 2 } [ d \chi ^ { 2 } + \sinh ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ] .
$$

Convert the coordinate-based components $R ^ { \mathbf { i } } { } _ { j k l }$ to a corresponding orthonormal basis, $R ^ { \widehat { \sf 4 } } { \sf 3 } \widehat { \sf k } \sf 1 \cdot$ Display ${ R ^ { \mathrm { i } \hat { j } } } _ { \hat { k } \hat { l } } = { R ^ { \mathrm { [ i \hat { j } ] } } } _ { [ \hat { k } \hat { l } ] }$ as a $3 \times 3$ matrix with appropriately labeled rows and columns.

# $\$ 14.2$ .FORMING THE EINSTEIN TENSOR

The distribution of matter in space does not immediately tell all details of the local curvature of space,according to Einstein. The stress-energy tensor provides information only about a certain combination of components of the Riemann curvature tensor,the combination that makes up the Einstein tensor. Chapter 13 described two equivalent ways to calculate the Einstein tensor: (l) by successive contractions of the Riemann tensor

Three ways to compute the Einstein tensor from the Riemann tensor

$$
\begin{array} { c } { { R _ { \mu \nu } = R ^ { \alpha } { } _ { \mu \alpha \nu } , \qquad R = g ^ { \mu \nu } R _ { \mu \nu } , } } \\ { { \qquad \displaystyle G _ { \mu \nu } = R _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } R } } \end{array}
$$

[equations (13.48) and (l3.49)); (2) by forming the dual of the Riemann tensor and then contracting:

$$
\begin{array} { r l } & { { \sf G } _ { \alpha \beta } { { ^ { \gamma \delta } } } \equiv ( { ^ { * } R ^ { * } } ) _ { \alpha \beta } { ^ { \gamma \delta } } = \epsilon _ { \alpha \beta \mu \nu } R ^ { \left| \mu \nu \right| } { _ { \left| \rho \sigma \right| } } \epsilon ^ { \rho \sigma \gamma \delta } } \\ & { \quad \quad \quad \quad \quad = - \delta ^ { \rho \sigma \gamma \delta } { _ { \alpha \beta \mu \nu } R ^ { \left| \mu \nu \right| } } _ { \left| \rho \sigma \right| } , } \\ & { { G } _ { \beta } { ^ { \delta } } = { \sf G } _ { \alpha \beta } { ^ { \alpha \delta } } } \end{array}
$$

[equations (13.46) and (13.47)].A third method,usually superior to either of these, is discovered by combining equations (l4.5a,b):

$$
G _ { \beta } { } ^ { \delta } = G ^ { \delta } { } _ { \beta } = - \delta ^ { \delta \rho \sigma } { } _ { \beta \mu \nu } R ^ { | \mu \nu | } { } _ { | \rho \sigma | } .
$$

[Note: in any frame,orthonormal or not,the permutation tensor $\delta ^ { \delta \rho \sigma } { } _ { \beta \mu \nu }$ has components

ose thismply ealuae $\delta ^ { \delta \rho \sigma } { } _ { \beta \mu \nu }$ usineii (8.10)of $\epsilon _ { \alpha \beta \mu \nu }$ and $\epsilon ^ { \rho \sigma \gamma \ B }$ JEquation (14.6)for the Einstein tensor,writen out explic-itly, reads

$$
\begin{array} { r l } & { G _ { ~ 0 } ^ { 0 } = - ( R ^ { 1 2 } _ { ~ 1 2 } + R ^ { 2 3 } _ { ~ 2 3 } + R ^ { 3 1 } _ { 3 1 } ) , } \\ & { G _ { ~ 1 } ^ { 1 } = - ( R ^ { 0 2 } _ { ~ 0 2 } + R ^ { 0 3 } _ { ~ 0 3 } + R ^ { 2 3 } _ { ~ 2 3 } ) , } \\ & { G _ { ~ 1 } ^ { 0 } = R ^ { 0 2 } _ { ~ 1 2 } + R ^ { 0 3 } _ { ~ 1 3 } , } \\ & { G _ { ~ 2 } ^ { 1 } = R ^ { 1 0 } _ { ~ 2 0 } + R ^ { 1 3 } _ { ~ 2 3 } , } \end{array}
$$

Standard method of computing curvature is wasteful

Ways to avoid "waste":

(1） geodesic Lagrangianmethod

(2) method of curvature 2-forms

and every other component is given by a similar formula,obtainable by obvious permutations of indices.

# $\$ 14.3$ .MORE EFFICIENT COMPUTATION

If the answer to a problem or the result of a computation is not simple, then there is no simple way to obtain it. But when a long computation gives a short answer, then one looks for a beter method. Many of the best-known applications of general relativitypresentonewihmetricfsinwhichmayofthecooents $g _ { \mu \nu } , T ^ { \mu } { } _ { \alpha \beta }$ and $R ^ { \mu } { } _ { \nu \alpha \beta }$ are zero; for them the standard computation of the curvature (Box 14.2) involves much “wasted" effort. One computes many $T ^ { \mu } { } _ { \alpha \beta }$ that turn out to be zero. One checks off many terms in a sum like $- T ^ { \mu } { } _ { \rho \beta } T ^ { \rho } { } _ { \alpha \mu }$ that are zero,or cancel with others to give zero. Two alternative procedures are available to eliminate some of this “waste.” The“geodesic Lagrangian” method provides an economical way to tabulate the $\Gamma ^ { \mu } { } _ { \alpha \beta }$ .The method of “curvature 2-forms” reorganizes the description from beginning to end,and computes both the connection and the curvature.

The geodesic Lagrangian method is only.a moderate improvement over the standard method, but it also demands only a modest investment in the calculus of variations,an investment that pays off in any case in other contexts in the world of mathematics and physics. In contrast, the method of curvature 2-forms is efficient, but demands a heavier investment in the mathematics of 1-forms and 2-forms than anyone would normally find needful for any introductory survey of relativity. Anyone facing several days' work at computing curvatures, however, would do well to learn the algorithm of the curvature 2-forms.

# \$14.4. THE GEODESIC LAGRANGIAN METHOD

One normally thinks that the connection coefficients $T ^ { \mu } { } _ { \alpha \beta }$ must be known before one can write the geodesic equation

$$
\ddot { x } ^ { \mu } + { \cal T } ^ { \mu } { } _ { \alpha \beta } \dot { x } ^ { \alpha } \dot { x } ^ { \beta } = 0 .
$$

(Here and below dots denote derivative with respect to the affine parameter, X.) However, the argument can be reversed. Once the geodesic equations have been

written down, the connection coeficients can be read out of them. For instance, on the 2-sphere as treated in Box l4.2, the geodesic equations are

$$
\begin{array} { c } { { \ddot { \theta } - \sin \theta \cos \theta \dot { \phi } ^ { 2 } = 0 , } } \\ { { \ddot { \phi } + 2 \cot \theta \dot { \phi } \dot { \theta } = 0 . } } \end{array}
$$

The frst eqaion here shows that ${ \cal { T } } _ { \phi \phi } ^ { \theta } = - \sin \theta \cos \theta .$ the second equation shows thatr $T ^ { \phi } { } _ { \phi \theta } = T ^ { \phi } { } _ { \theta \phi } = \cot \theta$ ; and the absence of any further terms shows that all other $T ^ { 4 } { } _ { j k }$ are zero.

The first essential principle is thus dlear: an explicit writing out of the geodesic equationis equivalent toabulationof alltheconnectioncoents $T ^ { \mu } { } _ { \alpha \beta }$

The second principle says more: one can write out the geodesic equation without ever having computed the $\boldsymbol { T ^ { \mu } } _ { \alpha \beta }$ In order to arriveat the equations for a geodesic (see Box l3.3), one need only recall that a geodesic is a parametrized curve that extremizes-the-imegral

$$
I = { \frac { 1 } { 2 } } \int g _ { \mu \nu } { \dot { x } } ^ { \mu } { \dot { x } } ^ { \nu } d \lambda
$$

in the sense

$$
\delta I = 0 .
$$

Geodesic Lagrangian method in 4 steps:

(1)write $\prime$ in simple form

In practical applications of this variational principle,the frst step-is-to rewrite equation (14.1O) in the simplest possible form, inserting the specific values of ${ \pmb g } _ { \mu \nu }$ for the problem at hand.If one's interest-attaches to the geodesics themselves, one can recognize many constants of motion even without carrying out any variations (see Chapter-25 on geodesic motion in Schwarzschild geometry, especially $\ S 2 5 . 2$ on conservationlawsandconstantsofmotion).Forthepurposeofcomputingthe $T ^ { \mu } { } _ { \alpha \beta } ,$ one proceeds to vary each coordinate in turn, obtaining four equations. Next these equations are rearranged so that their leading terms are ${ \ddot { x } } ^ { \mu }$ In this form they must be precisely the geodesic equations (l4.8). Consequently, the $\mathcal { L } ^ { \mu } { } _ { \tilde { \alpha } \beta }$ are immediately available as the coeficients in these fourequations. For the final step in computing curvature by this method,one returns to the standard method and to formulas of the type $R \sim \partial { \cal { T } } + { \cal { T } } { \cal { T } }$ ,treated in the standard way (Box l4.2);and as the need arises for each $r$ in turn, one scans the geodesic equation to find it. The procedure is best understood by following an example: Box l4.4 provides one.

(2) vary / to get geodesic equation

(3) read off $\Gamma ^ { \alpha } { } _ { \beta \gamma }$ (4) compute $R ^ { \alpha } { } _ { \beta \gamma \delta }$ etc. by standard method

# Exercise 14.4. EINSTEIN EQUATIONS FOR THE CLOSED FRIEDMANN UNIVERSE CALCULATED BY USING THE GEODESIC LAGRANGIAN METHOD

The line element of interest here is (see Chapter 27)

$$
d s ^ { 2 } = - d t ^ { 2 } + a ^ { 2 } ( t ) [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ] .
$$

(continued on page 348)

# Box 14.4 GEODESIC LAGRANGIAN METHOD SHORTENS SOME CURVATURE COMPUTATIONS

Aim: Compute the curvature for the line element

$$
d s ^ { 2 } = L ^ { 2 } ( e ^ { 2 \beta } d x ^ { 2 } + e ^ { - 2 \beta } d y ^ { 2 } ) - 2 d u d v
$$

where $L$ and $\pmb { \beta }$ are functions of $\pmb { u }$ only. [This metric is discussed as an example of a gravitational wave in $\ S 8 3 5 . 9 _ { - 3 5 . 1 2 . ] }$

Method: Obtain the $T ^ { \mu } { } _ { \alpha \beta }$ from the geodesic equations as inferred from the variational principle (14.10),then compute $R ^ { \mu } { } _ { \nu \alpha \beta } \sim \partial { \cal T } + { \cal T } ^ { 2 }$ as in Box 14.2.

Step 1. State the variational integral. For-the mctric under-eonsideration, equation (14.10) requires $\delta { \cal I } = 0$ for

$$
I = \int \left[ { \frac { 1 } { 2 } } L ^ { 2 } ( e ^ { 2 \beta } \dot { x } ^ { 2 } + e ^ { - 2 \beta } \dot { y } ^ { 2 } ) - \dot { u } \dot { v } \right] d \lambda .
$$

A world line that extremizes this integral is a geodesic.

Step 2: Vary the coordinates of the world line, one at a time, in their dependence on $\lambda$ First vary $x ( \lambda ) ,$ keeping fixed the functions $y ( \lambda ) , u ( \lambda )$ and ${ \pmb v } ( \lambda )$ Then

$$
\delta I = \int ( L ^ { 2 } e ^ { 2 \beta } \dot { x } ) \delta \dot { x } d \lambda = - \int ( L ^ { 2 } e ^ { 2 \beta } \dot { x } ) ^ { . } \delta x d \lambda .
$$

The requirement that $\delta I = 0$ for this variation (among others） gives

$$
0 = ( L ^ { 2 } e ^ { 2 \beta } \dot { x } ) ^ { \cdot } = L ^ { 2 } e ^ { 2 \beta } \ddot { x } + \dot { x } \dot { u } \frac { \partial } { \partial u } ( L ^ { 2 } e ^ { 2 \beta } ) .
$$

Varying y,u, v, in-the same way gives

$$
\begin{array} { l } { { 0 = ( L ^ { 2 } e ^ { - 2 \beta } \dot { y } ) ^ { \cdot } = L ^ { 2 } e ^ { - 2 \beta } \ddot { y } + \dot { y } \dot { u } \frac { \widehat { \partial } } { \partial u } ( L ^ { 2 } e ^ { - 2 \beta } ) , } } \\ { { \ } } \\  { 0 = \displaystyle { \bar { v } + \frac { 1 } { 2 } \dot { x } ^ { 2 } \frac { \partial } { \partial u } ( L ^ { 2 } e ^ { 2 \beta } ) + \frac { 1 } { 2 } \dot { y } ^ { 2 } \frac { \partial } { \partial u } ( L ^ { 2 } e ^ { - 2 \beta } ) , } } \\ { { \ 0 = \ddot { u } . } } \end{array}
$$

Step 3: Rearrange to get ${ \vec { x } } ^ { \mu }$ leading terms. If this step is not straightforward, this method will not save time,and the technique of either Box l4.2 or Box l4.5 will be more suitable. In the example here, one quickly writes, using a prime for $\hat { \boldsymbol { o } } / \hat { \boldsymbol { o } } \pmb { u } .$

$$
\begin{array} { r l } & { 0 = \ddot { x } + 2 ( L ^ { - 1 } L ^ { \prime } + \beta ^ { \prime } ) \dot { x } \dot { u } , } \\ & { 0 = \ddot { y } + 2 ( L ^ { - 1 } L ^ { \prime } - \beta ^ { \prime } ) \dot { y } \dot { u } , } \\ & { 0 = \ddot { v } + ( L ^ { 2 } e ^ { 2 \beta } ) ( L ^ { - 1 } L ^ { \prime } + \beta ^ { \prime } ) \dot { x } ^ { 2 } + ( L ^ { 2 } e ^ { - 2 \beta } ) ( L ^ { - 1 } L ^ { \prime } - \beta ^ { \prime } ) \dot { y } ^ { 2 } , } \\ & { 0 = \ddot { u } . } \end{array}
$$

Step $\mathfrak { s } ^ { \prime }$ : Interpret these equations as a tabulation of $T ^ { \mu } { } _ { \alpha \beta }$ . Equations (3) are the standard equations for a geodesic,

$$
\ddot { x } ^ { \mu } + { \cal T } _ { \alpha \beta } ^ { \mu } \dot { x } ^ { \alpha } \dot { x } ^ { \beta } = 0 .
$$

Therefore it is enough to scan them to find the value of any desired $r$ For instance ${ r ^ { x } } _ { y u }$ must appear in thecoefficient $( \boldsymbol r ^ { z } _ { y u } + \boldsymbol r ^ { z } _ { u y } ) = 2 \boldsymbol r ^ { z } { } _ { y u }$ of the $\dot { y } \dot { u }$ term in the equation for $\pmb { \ddot { x } }$ But no yu term appears in equation $( 3 x )$ .Therefore $T ^ { x } { } _ { y u }$ is zero in this example. Note that equations (3) are simple,in the sense that they contain few terms; therefore most of the $T ^ { \mu } { } _ { \alpha \beta }$ must be zero. For instance,it follows from equation $( 3 u )$ that all ten $T ^ { \ * } { } _ { \alpha \beta }$ are zero. The only non-zero $\boldsymbol { r }$ 's are ${ \varGamma ^ { \varepsilon } } _ { \ast u } = { \varGamma ^ { \varepsilon } } _ { \ast x } =$ $( L ^ { - 1 } L ^ { \prime } + \beta ^ { \prime } )$ from equation $( 3 x ) , \ : T ^ { \nu } { } _ { y u } = T ^ { \nu } { } _ { u y } = ( L ^ { - 1 } L ^ { \prime } - \beta ^ { \prime } )$ from equation $( 3 y )$ ， and ${ \varGamma ^ { v } } _ { z x }$ and $\varGamma ^ { v } { } _ { y y }$ from equation $( 3 v )$

Step 4: Compute each $R ^ { \mu } { } _ { \nu \alpha \beta }$ ,etc. There is litle relief from routine in systematically applying equation (3) from Box l4.2. One must list 2l components $R ^ { \mu } { } _ { \nu \alpha \beta }$ that are not related by any of the symmetries $R _ { \mu \nu \alpha \beta } = R _ { \alpha \beta \mu \nu } = - R _ { \mu \nu \beta \alpha } ,$ and compute each. In the example here,one notesthat $T ^ { u } { } _ { \alpha \beta } = 0$ implies $R ^ { * } { } _ { \alpha \beta \gamma } = - R _ { v \alpha \beta \gamma } = 0$ . Therefore 15 of the list of 21 vanish at one swat.The list then is:

$$
\begin{array} { r l } & { R _ { \mathrm { e q p } } = - R _ { \mathrm { e q p } } ^ { * } = 0 , } \\ & { R _ { \mathrm { u e q s t } } = - R _ { \mathrm { e q p } } ^ { * } = - ( T _ { \mathrm { e q p } } ^ { * } ) ^ { * } + T _ { \mathrm { e q } } ^ { \nu } { { r ^ { * } } _ { \mathrm { s t } } } } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - ( - ( T ^ { 2 } e ^ { \beta \hbar } ) \left( \frac { { L _ { \mathrm { e p } } ^ { \prime } } } { L } + \beta ^ { \nu \prime \prime } + 2 \frac { L } { L } \beta ^ { \prime } + \beta ^ { \prime \prime } \right) , } \\ & { R _ { \mathrm { e q p } } = - R _ { \mathrm { e q p } } ^ { * } = 0 , } \\ & { R _ { \mathrm { u e p } } = - R _ { \mathrm { e p p } } ^ { * } = 0 , } \\ & { R _ { \mathrm { u e p } } = - { { \beta ^ { \mathrm { e q p } } } _ { \mathrm { s p } } } = 0 , } \\ & { R _ { \mathrm { u p } } = - { { \beta ^ { \mathrm { e q p } } } _ { \mathrm { s p } } } = - ( T _ { \mathrm { e p p } } ^ { * } ) ^ { * } + { { T ^ { \mathrm { e q p } } } _ { \mathrm { s p } } } { { r ^ { \mathrm { \nu } } } _ { \mathrm { s t } } } } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { R _ { \mathrm { u e p } } = - ( { L ^ { 2 } e ^ { - 2 \beta } } ) \left( \frac { { L _ { \mathrm { e p } } ^ { \prime \prime } } } { L } - \beta ^ { \nu \prime } - 2 \frac { L } { L } \beta ^ { \prime \prime } + \beta ^ { \prime \prime } \right) , } \\ & { R _ { \mathrm { u e p } } = - ( R _ { \mathrm { s p } } ^ { * } = 0 , } \\ & { R _ { \mathrm { e q p } } = ( { L ^ { 2 } e ^ { 2 \beta } } ) R _ { \mathrm { e p s } } ^ { * } = 0 . } \end{array}
$$

One can now calculate the Einstein tensor via equation (l4.7). In the example here, however,it is equally simple to form first the Ricci tensor by the straightforward contraction $R ^ { \mu } { } _ { \alpha \mu \beta }$ . Only $\mu = x$ and $\mu = y$ give any contribution, because no superscript index can be a $\pmb { u }$ ,and no subscript a $v .$ Thus one finds

$$
R _ { u u } = - 2 [ L ^ { - 1 } L ^ { \prime \prime } + \beta ^ { \prime 2 } ] ,
$$

all other $R _ { \alpha \beta } = 0$ ，

and

$$
R = 0 .
$$

From this last result, it follows that here the desired Einstein tensor is identical with the Ricci tensor.

(a) Set up the variational integral (l4.lO) for a geodesic in this metric,then successively vary $t , x , \theta$ and $\phi$ to obtain, after some rearrangement, four equations $0 = \ddot { t } + \cdots , 0 \stackrel { } { = }$ $\ddot { x } + \cdot \cdot \cdot$ , etc. displaying the $r$ 's in the form of equation (14.8).

(b) Use this display asatableof $r$ 's to compute $R _ { ~ \chi \mu \nu } ^ { t }$ and $R ^ { \chi } { } _ { \theta \mu p } ,$ of which only $R ^ { t } { } _ { x t x }$ and $R ^ { x } { _ { \theta x \theta } }$ are non-zero (consequence of the complete equivalence of alldirections tangent to the $x \pmb { \theta } \phi$ sphere).

(c) Convert to an orthonormal frame with $\pmb { \omega } ^ { \hat { t } } = \pmb { \mathcal { M } }$ ， $\omega { \dot { x } } = a d x$ ， $\pmb { \omega } ^ { \hat { \pmb { \theta } } } = \frac { \mathbf { \gamma } } { 2 }$ ， $\pmb { \omega } ^ { \pmb { \hat { \phi } } } = \pmb { \ ? }$ ,and list $R ^ { \hat { t } } { \hat { x } } _ { \hat { t } \hat { x } }$ and $\pmb { R } ^ { \hat { x } \hat { \theta } } { } _ { \hat { x } \hat { \theta } }$ Explain whyallothercomponentsare kownbysymmetryintersof these two.

(d) Calculate,using equations (l4.7),all independent components of the Einstein tensor $G ^ { \dot { \mu } } { } _ { \dot { \nu } }$ .[Answer: See Box 14.5.]

# \$14.5. CURVATURE 2-FORMS

In electrodynamics the abstract notation

$$
{ \pmb F } = \pmb { \mathcal { A } } { \pmb A }
$$

saves space compared to the explicit notation

$$
\begin{array} { r l } & { { \cal F } _ { 3 1 } = \displaystyle \frac { \partial { \cal A } _ { 1 } } { \partial x ^ { 3 } } - \frac { \partial { \cal A } _ { 3 } } { \partial x ^ { 1 } } , } \\ & { { \cal F } _ { 1 2 } = \displaystyle \frac { \partial { \cal A } _ { 2 } } { \partial x ^ { 1 } } - \frac { \partial { \cal A } _ { 1 } } { \partial x ^ { 2 } } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \cdot \mathrm { ~  ~ \Omega ~ } } \\ & { \quad \quad \quad \quad \cdot . . , \mathrm { e t c . ~ \mit ~ ( s i x ~ e q u a t i o n s ) } , } \end{array}
$$

Concepts needed for method of curvature 2-forms

there is no reason to shun similar economies in dealing with the dynamics of geometry. Cartan introduced the decisive ideas,seen above,of differential forms (where a simple object replaces a listing of four components; thus, $\sigma = \sigma _ { \mu } d x ^ { \mu } )$ ， and of the exterior derivative d. He went on (1928,1946) to package the 21 components $R _ { \mu \nu \alpha \beta }$ of the curvature tensor into six curvature 2-forms,

$$
{ \mathcal { R } } ^ { \mu \nu } = - { \mathcal { R } } ^ { \nu \mu } .
$$

Regarded purely as notation, these 2-forms automatically produce a profit. They cut down the weight of paper work required to list one's answer after one has it. They also provide a route into deeper insight on “curvature as a geometric object,” although that is not the objective of immediate concern in this chapter.

Cartan's exterior derivative $\pmb { d }$ automatically effects many cancelations in the calculation of curvature. It often cancels terms before they ever need to be evaluated.

Extension of Cartan's calculus from electromagnetism and other applications (Chapter 4) to the analysis of curvature (this chapter) requires two minor additions to the armament of forms and exterior derivative: (l） the idea of a vector-valued (or tensor-valued) exterior differential form; and (2) a corresponding generalization of the exterior derivative $\pmb { d } .$ This section uses both these tools in deriving the key formulas (14.18),(14.25),(l4.31),and (14.32). Once derived,however, these formulas demand no more than the standard exterior derivative for all applications and for all calculations of curvature $( 8 1 4 . 6$ and Box 14.5).

Extended exterior derivative:

The extended exterior derivative leads to nothing new in the first two contexts to which one applies it: a scalar function ( $\mathfrak { s o }$ -form") and a vector field("vector-valued O-form"). Thus, take any function $f .$ Its derivative in an unspecified direction is a l-form; or, to make a new distinction that will soon become meaningful,a “scalarvalued 1-form.” Specify the direction in which differentiation is to occur ("fill in the slot in the l-form"). Thereby obtain the ordinary derivative as it applies to a function

(1) acting on a scalar

$$
\langle d f , \pmb { u } \rangle = \hat { \partial } _ { \pmb { u } } f .
$$

Next, take any vector field $\pmb { \nu } .$ Its covariant derivative in an unspecified direction is a“vector-valued l-form.” Specify the direction $\pmb { \mu }$ in which differentiation is to occur ("fill in the slot in the l-form"). Thereby obtain the covariant derivative

(2) acting on a vector

$$
\langle d v , u \rangle \equiv \nabla _ { u } v .
$$

This object too is not new; it is the covariant derivative of the vector $\pmb { \nu }$ taken in the direction of the vector ${ \pmb u }$ .When one abstracts away from any special choice of the direction of differentiation $\pmb { \mu }$ , one finds an expression that one has encountered before, though not under its new name of“vector-valued l-form.”This expression measures the covariant derivative of the vector $\pmb { \nu }$ in an unspecified direction ("slot for direction not yet filled in"). From a look at (l4.l2a), one sees that this extended exterior derivative is applied to $\pmb { \nu } ,$ ，without reference to $\pmb { u }$ ,is

$$
\begin{array} { r } { \pmb { d v } = \pmb { \nabla } \pmb { v } . } \end{array}
$$

Similarly, for any “tensor-valued O-form” [i.e. $( \pmb { \imath } )$ tensor] s $\mathbf { \Omega } , \mathbf { \Omega } \mathbf { d } \pmb { \mathscr { s } } \equiv \pmb { \nabla } \pmb { s }$

Before proceeding further with the exterior (soon to be marked as “antisymmetric") differentiation of tensors,write down a formula (see exercise l4.5) for the exterior (antisymmetric) derivative of a product of forms:

$$
d ( \alpha \wedge \beta ) = ( d \alpha ) \wedge \beta + ( - 1 ) ^ { p } \alpha \wedge d \beta ,
$$

where $\pmb { \alpha }$ is a $\pmb { p }$ form and $\pmb { \beta }$ is a $q$ -form.

Now extend the exterior derivative from elementary forms to the exterior product of a tensor-valued $\pmb { p }$ -form $\pmb { \mathscr { s } }$ with any ordinary $q$ -form, $\pmb \beta$ ； thus,

$$
d ( S \wedge \beta ) = d S \wedge \beta + ( - 1 ) ^ { p } S \wedge d \beta .
$$

(3) defined in general

This equation can be regarded as a general definition of the extended exterior derivative. For example, if $\mathbf { \dot { s } }$ is a-tensor-valued 2-form, ${ \pmb S } = S ^ { \alpha \beta } { } _ { | \gamma \delta | } \pmb \sigma _ { \alpha } \pmb \sigma _ { \beta } d x ^ { \gamma } \wedge d x ^ { \delta }$ ， then equation (14.13b) says

$$
d \mathbb { S } = d [ ( \varphi _ { \alpha } \varphi _ { \beta } S ^ { \alpha \beta } { } _ { | \gamma \mathtt { s } | } ) ( d x ^ { \gamma } \wedge d x ^ { \mathtt { s } } ) ] = d ( \varrho _ { \alpha } \varrho _ { \beta } S ^ { \alpha \beta } { } _ { | \gamma \mathtt { s } | } ) \wedge ( d x ^ { \gamma } \wedge d x ^ { \mathtt { s } } ) .
$$

As another example,use (l4.l3b) to calculate $\pmb { d } ( \pmb { u } \pmb { \sigma } ) ,$ where $\pmb { \mu }$ is a vector-valued O-form (vector) and $\pmb { \sigma }$ is a scalar-valued 1-form (l-form):

$$
d ( u \sigma ) = ( d u ) \wedge \sigma + u d \sigma .
$$

lf one were following the practice of earlier chapters,one would have written $\pmb { \mu } \otimes \pmb { \sigma }$ where ug appears here, ${ \pmb { \mu } } \otimes$ dg instead of u do, and $\pmb { \mathscr { e } } _ { \alpha } \otimes \pmb { \mathscr { e } } _ { \beta }$ instead of ${ \pmb { e } } _ { { \pmb { \alpha } } } { \pmb { e } } _ { \beta }$ However, to avoid overcom plication in the notation,all such tensor product symbols are omitted here and hereafter.

Equations (14.12) and (14.13) do more than define the (extended) exterior derivative $\pmb { d }$ and provide a way to use it in computations. They also allow one to define and calculate the antisymmetrized second derivatives,e.g., $\pmb { d } ^ { 2 } \pmb { v } .$ The relation

$$
{ \pmb d } ^ { 2 } { \pmb v } = \Re { \pmb v }
$$

where $\pmb { \nu }$ is a vector will then introduce the “operator-valued” or $^ { 6 6 } ( _ { 1 } ^ { 1 } )$ -tensor valued" curvature 2-form $\mathcal { R }$ . The notation of the extended exterior derivative puts a new look on the old apparatus of base vectors and parallel transport, and opens a way to calculate the curvature 2-form $\mathcal { R }$

Let the vector fied $\pmb { v }$ be expanded in terms of some field of basis vectors ${ \pmb \theta } _ { \pmb { \mu } } .$ thus

$$
\pmb { v } = \pmb { e } _ { \mu } \pmb { v } ^ { \mu } .
$$

Then the exterior derivative of this vector is

$$
d v = d e _ { \mu } v ^ { \mu } + e _ { \mu } d v ^ { \mu } .
$$

Expand the typical vector-valued 1-form $\pmb { d } \pmb { e } _ { \mu }$ in the form

$$
d e _ { \mu } = e _ { \nu } { \omega ^ { \nu } } _ { \mu } .
$$

Here the “components” $\omega ^ { \nu } { } _ { \mu }$ in the expansion of $\pmb { d } \pmb { e } _ { \mu }$ are l-forms.Recall from equation (10.13) that the typical $\omega ^ { \nu } { } _ { \mu }$ is related to the connection coefficients by

$$
\omega ^ { \nu } { } _ { \mu } = { \Gamma ^ { \nu } } _ { \mu \lambda } \omega ^ { \lambda } .
$$

Therefore the expansion of the “vector” (really,“vector-valued l-form") is

$$
d v = e _ { \mu } ( d v ^ { \mu } + { \omega ^ { \mu } } _ { \nu } v ^ { \nu } ) .
$$

Now differentiate once again to find

$$
\begin{array} { l } { { d ^ { 2 } v = d e _ { \alpha } \wedge ( d v ^ { \alpha } + { \omega ^ { \alpha } } _ { \nu } v ^ { \nu } ) } } \\ { { \phantom { d } + e _ { \mu } ( d ^ { 2 } v ^ { \mu } + d { \omega ^ { \mu } } _ { \nu } v ^ { \nu } - { \omega ^ { \mu } } _ { \nu } \wedge d v ^ { \nu } ) } } \\ { { \phantom { d } = e _ { \mu } ( { \omega ^ { \mu } } _ { \alpha } \wedge d v ^ { \alpha } + { \omega ^ { \mu } } _ { \alpha } \wedge { \omega ^ { \alpha } } _ { \nu } v ^ { \nu } } } \\ { { \phantom { d } + d ^ { 2 } v ^ { \mu } + d { \omega ^ { \mu } } _ { \nu } v ^ { \nu } - { \omega ^ { \mu } } _ { \alpha } \wedge d v ^ { \alpha } ) . } } \end{array}
$$

The simplifications made here use (1) the equation (l4.l4), for a second time; and (2) the product rule (14.13a), which introduced the minus sign in the last term, ready to cancel the first term. Now consider the term ${ \pmb { d } } ^ { 2 } v ^ { \mu }$ .Recall that any given component, for example, $v ^ { 3 }$ ,is an ordinary scalar function of position (as contrasted to $\pmb { v }$ or ${ \pmb { e } } _ { 3 }$ or $\bullet _ { 3 } v ^ { 3 } .$ ). Therefore the standard exterior derivative (Chapter 4) as applied to a scalar function is all that $\pmb { d }$ can mean in ${ \pmb { d } } ^ { 2 } v ^ { \mu }$ 、But for the standard exterior derivative applied twice, one has automatically ${ \pmb { d } } ^ { 2 } v ^ { \mu } = { \bf 0 }$ (Box 4.1, B; Box 4.4). This circumstance reduces the expansion for $\mathbf { \nabla } \mathbf { d } ^ { 2 } \mathbf { v }$ to the form

Curvature 2-forms ${ \mathcal R } ^ { \mu } { } _ { \nu }$ ：

$$
d ^ { 2 } { \pmb v } = { \pmb e } _ { \mu } \mathcal { R } ^ { \mu } { } _ { \nu } v ^ { \nu } ,
$$

(1) in terms of $\mathbf { \nabla } \mathbf { \frac { 1 } { 2 } } \mathbf { \mu } _ { \mathbf { v } }$

where the $\mathcal { R } ^ { \mu } { } _ { \nu }$ are abbreviations for the curvature 2-forms

$$
\begin{array} { r } { \mathcal { R } ^ { \mu } { } _ { \nu } \equiv d \omega ^ { \mu } { } _ { \nu } + \omega ^ { \mu } { } _ { \alpha } \wedge \omega ^ { \alpha } { } _ { \nu } . } \end{array}
$$

(2) in terms of $\pmb { \omega } ^ { \pmb { \mu } }$

Ordinarily,equation (14.18) surpasses in eficiency every other known method for calculating the .curvature 2-forms.

The remarkable form of equation (l4.17) deserves comment. On the left appear two $\pmb { d } ^ { \prime } \pmb { s }$ ,reminders that one has twice differentiated the vector field ${ \pmb v } .$ But on the right, as the result of the differentiation,one has only the vector field $\pmb { \nu }$ at the point in question, undifferentiated. How $\pmb { \nu }$ varies from place to place enters not one whit in the answer. All that matters is how the geometry varies from place to place. Here is curvature coming into evidence. lt comes into evidence free of any special features of the vector field $\pmb { \nu } ,$ because the operation $\pmb { d } ^ { 2 }$ is an antisymmetrized covariant derivative [compare equation (l1.8） for this antisymmetrized covariant derivative in the previously developed abstract language,and see Boxes 11.2 and 11.6 for what is going on behind the scene expressed in the form of pictures]. In brief, the result of operating on $\pmb { \nu }$ twice with $\pmb { d }$ is an algebraic linear operation on $\pmb { v } ;$ thus,

$$
d ^ { 2 } { \pmb v } = \mathcal { R } { \pmb v } .
$$

Tensor-valued curvature 2-form $\mathcal { R }$

Here $\mathcal { R }$ is an abbreviation for the $^ { 6 6 } ( _ { 1 } ^ { 1 } )$ -tensor valued 2-form,”

$$
{ \mathcal { R } } = \pmb { \mathscr { e } } _ { \mu } \otimes \pmb { \mathscr { w } } ^ { \nu } { \mathcal { R } } ^ { \mu } { \vphantom { \bigg | } } _ { \nu } .
$$

If $\pmb { d }$ is a derivative with a“slot in it”in which to insert the vector saying in what direction the differentiation is to proceed, then the $\mathbf { \nabla } \mathbf { \overline { { d } } } ^ { 2 } \mathbf { w }$ of $d ^ { 2 } w = \mathcal { R } w$ has two slots and calls for two vectors, say, ${ \pmb u }$ and ${ \pmb v } .$ .These two vectors define the plane in which the antisymmetrized exterior derivative of (l4.19) is to be evaluated (change in $\boldsymbol { \mathsf { w } }$ upon going around the elementary route defined by ${ \pmb u }$ and $\pmb { v }$ and coming back to its starting point; Boxes 11.6 and 11.7).To spell out explicitly this insertion of vectors into slots,return first to a simpler context, and see the exterior derivative of a l-form (itself a 2-form) “evaluated" for a bivector $\mu \wedge v$ ("count of honeycomblike cells of the 2-form over the parallelogram-shaped domain defined by the two vectors ${ \pmb u }$ and $\pmb { v } ^ { \prime }$ ),and see the result of the evaluation (exercise l4.6) expressed as a commutator,

$$
\langle d \alpha , u \wedge v \rangle = \widehat { \circ } _ { u } \langle \alpha , v \rangle - \widehat { \circ } _ { v } \langle \alpha , u \rangle - \langle \alpha , [ u , v ] \rangle .
$$

This result generalizes itself to a tensor-valued l-form S of any rank in an obvious way; thus,

$$
\langle d \mathcal { S } , u \wedge v \rangle = \nabla _ { u } \langle \mathcal { S } , v \rangle - \nabla _ { v } \langle \mathcal { S } , u \rangle - \langle \mathcal { S } , [ u , v ] \rangle .
$$

Apply this result to the vector-valued 1-form ${ \pmb S } = \pmb { d } \pmb { w }$ Recall the expression for a directional derivative, $\langle d w , \pmb { u } \rangle = \pmb { \nabla } _ { \pmb { u } } w .$ Thus find the result

$$
\begin{array} { c } { { \langle d ^ { 2 } w , u \wedge v \rangle = \nabla _ { v } \ \nabla _ { v } w - \nabla _ { v } \ \nabla _ { u } w - \nabla _ { [ u , v ] } w } } \\ { { = \mathcal { A } ( u , v ) w , } } \end{array}
$$

Relation of curvature 2-form $\mathcal { R }$ to curvature operator $\mathcal { R }$

where ${ \mathcal { R } } ( \pmb { \mu } , \pmb { v } )$ is the curvature operator defined already in Chapter ll [equation (11.8)). The conclusion is simple: the $\mathbf { \Sigma } ( _ { 1 } ^ { 1 } )$ -tensor-valued 2-form $\mathcal { R }$ of(14.19),evaluated on the bivector ("parallelogram") $u \wedge v ,$ is identical with the curvature operator ${ \mathcal { R } } ( \pmb { \mu } , \pmb { \nu } )$ introduced previously; thus

$$
\langle { \mathcal R } , { \pmb u } \wedge { \pmb v } \rangle = { \mathcal R } ( { \pmb u } , { \pmb v } ) .
$$

Now go from the language of abstract operators to a language that begins to make components show up. Substitute on the left the expression (l4.20) and on the right the value of the curvature operator from (11.11); and rewrite (l4.24) in the form

$$
\begin{array} { r } { \pmb { e } _ { \mu } \otimes \pmb { \omega } ^ { \nu } \langle \mathcal { R } ^ { \mu } _ { \nu } , \pmb { u } \wedge \pmb { v } \rangle = \pmb { \varrho } _ { \mu } \otimes \pmb { \omega } ^ { \nu } \pmb { R } ^ { \mu } _ { \nu \alpha \beta } u ^ { \alpha } v ^ { \beta } . } \end{array}
$$

Relation of $\mathscr { R }$ to components of Riemann

Compare and conclude that the typical individual curvature 2-form is given by the formula

$$
{ \mathcal R } ^ { \mu } { } _ { \nu } = R ^ { \mu } { } _ { \nu \mid \alpha \beta \mid } \omega ^ { \alpha } \wedge \omega ^ { \beta }
$$

(sum over $\alpha , \beta$ restricted to $\alpha < \beta$ ; so each index pair occurs only once).

Equation (l4.25） provides the promised packaging of 2l curvature components into six curvature 2-forms; and equation (14.18) provides the quick means to calcu-late these curvature 2-forms. It is not necessary to take the key calculational equations (14.18) on faith, or to master the extended exterior derivative to prove or use them. Not one mention of any $\pmb { d }$ do they make except the standard exterior $\pmb { d }$ of Chapter 4. These key equations, moreover, can be verified in detail(exercise l4.8) by working in a coordinate frame. One adopts basis 1-forms $\pmb { \omega } ^ { \alpha } = \pmb { d } x ^ { \alpha }$ .One goes on to use $\omega ^ { \mu } { } _ { \nu } = \Gamma ^ { \mu } { } _ { \nu \lambda } d x ^ { \lambda }$ from equation (14.15). In this way one obtains the “standard formula for the curvature” [equation (11.12） and equation (3) of Box 14.2] by standard methods.

In summary, the calculus of forms and exterior derivatives reduces the

$$
T ^ { \mu } { } _ { \alpha \beta } \longrightarrow R ^ { \mu } { } _ { \nu \alpha \beta }
$$

calculation to the

$$
\omega ^ { \mu } , \longrightarrow \mathcal { R } ^ { \mu } ,
$$

computation. Now look at the other link in the chain that leads from metric to curvature. It used to be

$$
g _ { \mu \nu } \longrightarrow { \cal { T } } ^ { \mu } { } _ { \alpha \beta } .
$$

It now reduces to the calculation of “connection l-forms"; thus

$$
g _ { \mu \nu } \longrightarrow \omega ^ { \mu } { } _ { \nu } .
$$

Two principles master this first step in the curvature computation: (1) the symmetry of the covariant derivative; and (2) its compatibility with the metric. Condition (l), symmetry, appears in hidden guise in the principle

Symmetry of covariant derivative:

$$
{ \pmb d } ^ { 2 } { \pmb \mathcal { G } } = 0 .
$$

(1) expressed as ${ \pmb q } ^ { 2 } { \pmb \mathcal { P } } = { \pmb 0 }$

Here the notation $^ { * 6 } { \mathcal { S } }$ for point" comes straight out of Cartan. He thought of a vector as defined by the movement of one point to another point infinitesimally close to it. To write $\pmb { d } \pmb { \mathcal { P } }$ was therefore to take the “derivative of a point" [make a construction with a“point deleted" (tail of vector) and “point reinserted nearby" (tip of vector)]. The direction of the derivative $\pmb { d }$ in $\pmb { d } \pmb { \mathcal { P } }$ is indefinite.In other words, $\pmb { d } \pmb { \mathcal { P } }$ contains a “slot.”Only when one inserts into this slot a definite vector $\pmb { \nu }$ does $\pmb { d } \pmb { \mathcal { P } }$ give a definite answer for Cartan's vector. What is that vector that $\pmb { d } \pmb { \mathcal { P } }$ then gives? It is $\pmb { v }$ itself.“The movement that is $\pmb { \nu }$ tells the point $\mathscr { P }$ to reproduce the movement that is $\pmb { v } ^ { * }$ ; or in concrete notation,

$$
\langle \mathcal { A } \mathcal { P } , \pmb { v } \rangle = \pmb { v } .
$$

Put the content of this equation into more formalistic terms.The quantity $\pmb { d } \pmb { \mathcal { P } }$ is a ()-tensor

$$
\mathbf { \pmb { \mathcal { S } } } = \mathbf { e } _ { \mu } \mathbf { \pmb { \omega } } ^ { \mu } .
$$

It is distinguished from the generic $( _ { 1 } ^ { 1 } )$ -tensor

$$
\pmb { T } = \pmb { \sigma } _ { \pmb { \mu } } T ^ { \mu } { } _ { \nu } \pmb { \omega } ^ { \nu }
$$

by the special value of its components

$$
T ^ { \mu } { } _ { \nu } = \delta ^ { \mu } { } _ { \nu } .
$$

In this sense it deserves the name of “unit tensor.” Insert this tensor in place of $\pmb { s }$ into equation (l4.22) and obtain the result

$$
\langle d ^ { 2 \mathcal { S } } , u \wedge v \rangle = \nabla _ { u } v - \nabla _ { v } u - [ u , v ] = 0 .
$$

The zero on the right is a restatement of equation (l0.2a) or of “the closing of the vector diagram"in the picture called “symmetry of covariant differentiation"in Box 10.2.The vanishing of the righthand side for arbitrary ${ \pmb u }$ and $\pmb { \nu }$ demands the vanishing of $\pmb { d } ^ { 2 \omega }$ on the left; and conversely,the vanishing of $\pmb { d } ^ { 2 } \mathscr { P }$ demands the symmetry of the covariant derivative. The other principle basic to the forthcoming computations is “compatibility of covariant derivative with metric,”as expressed in the form

$$
d ( \pmb { \mathscr { u } } \cdot \pmb { v } ) = ( d \pmb { \mathscr { u } } ) \cdot \pmb { v } + \pmb { \mathscr { u } } \cdot ( d \pmb { v } ) .
$$

It is essential here to ascribe to the metric (the“dot") a vanishing covariant derivative; thus

$$
\pmb { d ( \cdot ) } = 0 .
$$

Capitalize on the symmetry and compatibility of the covariant derivative by using basis vectors (and where appropriate the basis l-forms dual to these basis vectors) in equations (14.26) and (l4.30). Thus from

$$
\mathbf { \nabla } \cdot \mathbf { d } \mathcal { P } = \mathcal { \mathbf { e } } _ { \mu } \pmb { \omega } ^ { \mu }
$$

(2)expressed as $d w ^ { \mu } + { w ^ { \mu } } _ { \nu } \wedge w ^ { \nu } = 0$

compute

$$
\begin{array} { c } { { 0 = d ^ { 2 } \mathcal { P } = d \pmb { \mathscr { e } } _ { \mu } \wedge \pmb { \omega } ^ { \mu } + \pmb { \mathscr { e } } _ { \mu } d \pmb { \omega } ^ { \mu } } } \\ { { = \pmb { \mathscr { e } } _ { \mu } ( \pmb { \omega } ^ { \mu } , \wedge \pmb { \omega } ^ { \nu } + \pmb { d } \pmb { \omega } ^ { \mu } ) , } } \end{array}
$$

Compatibility of $\pmb { g }$ and $\blacktriangledown$ expressed as ${ \pmb d } g _ { \mu \nu } = { \pmb w } _ { \mu \nu } + { \pmb w } _ { \nu \mu }$

Method of curvature 2-forms in 4 steps:

(1)select metric and frame (2) calculate connection 1-forms $\pmb { \omega } ^ { \pmb { \mu } }$

and conclude that the coefficient of $\pmb { e } _ { \mu }$ must vanish;or

$$
0 = d \omega ^ { \mu } + \omega ^ { \mu } { } _ { \nu } \wedge \omega ^ { \nu } \qquad ( ^ { \ast \ast } \mathfrak { s y m m e t r y ^ { \prime \prime } } ) .
$$

Next, into (14.30) in place of the general ${ \pmb u }$ and $\pmb { \nu }$ insert the specific $\pmb { e } _ { \mu }$ and $\pmb { e } _ { \nu } \mathrm { : }$ respectively,and find

$$
{ \pmb d } g _ { \mu \nu } = { \pmb \omega } _ { \mu \nu } + { \pmb \omega } _ { \nu \mu } \qquad ( { \mathrm { ' c o m p a t i b i l i t y " } } ) ,
$$

where

$$
\omega _ { \mu \nu } \equiv g _ { \mu \alpha } \omega ^ { \alpha } { } _ { \nu } = { \cal T } _ { \mu \nu \alpha } \omega ^ { \alpha } .
$$

In equations (l4.31) one has the connection between metric and connection forms expressed in the most compact way.

# $\$ 14.6$ . COMPUTATION OF CURVATURE USING EXTERIOR DIFFERENTIAL FORMS

The use of differential forms for the computation of curvature is illustrated in Box 14.5. This section outlines the method. There are three main steps: compute $\omega ^ { \mu } { } _ { \nu } ;$ compute ${ \mathcal R } ^ { \mu } { } _ { \nu }$ ; and compute $G ^ { \mu } { } _ { \nu }$ .More particularly, first select a metric and a frame. Thereby fix the basis forms $\omega ^ { \mu } = L ^ { \mu } { } _ { \alpha ^ { \prime } } d x ^ { \alpha ^ { \prime } }$ and the metric components ${ \pmb g } _ { \pmb { \mu } \pmb { \nu } }$ in $d s ^ { 2 } = g _ { \mu \nu } \omega ^ { \mu } \otimes \omega ^ { \nu }$ . Then determine the connection forms $\omega ^ { \mu } { } _ { \nu }$ ,and determine them uniquely,as solutions of the equations

$$
\begin{array} { c } { { 0 = d \pmb { \omega } ^ { \mu } + \pmb { \omega } ^ { \mu } { } _ { \nu } \wedge \pmb { \omega } ^ { \nu } , } } \\ { { { \pmb d } g _ { \mu \nu } = { } \pmb { \omega } _ { \mu \nu } + \pmb { \omega } _ { \nu \mu } . } } \end{array}
$$

The “guess and check”method of finding a solution to these equations (described and illustrated in Box 14.5) is often quick and easy.[Exercise (l4.7) shows that a solution always exists by showing that the Christoffel formula (14.36) is the unique solution in coordinate frames.] It is usually most convenient to use an orthonormal frame with $g _ { \mu \nu } = \eta _ { \mu \nu }$ (or some other simple frame where ${ \pmb g } _ { \pmb { \mu } \pmb { \nu } } =$ const, e.g., a null frame). Then ${ \pmb d } _ { { \pmb g } _ { \mu \nu } } = 0$ and equation (14.31b) shows that $\omega _ { \mu \nu } = - \omega _ { \nu \mu } .$ Therefore there are only six $\omega _ { \mu \nu }$ for which to solve in four dimensions.

(continued on page 358)

# Box 14.5 CURVATURE COMPUTED USING EXTERIOR DIFFERENTIAL FORMS(METRIC FORFRIEDMANN COSMOLOGY)

The Friedmann metric

$$
d s ^ { 2 } = - d t ^ { 2 } + a ^ { 2 } ( t ) [ \dot { d } \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ]
$$

(Box 27.1) represents a spacetime where each constant- $t$ hypersurface is a threedimensional hypersphere of proper circumference $2 \pi a ( t )$ . An orthonormal basis is easily found in this spacetime; thus,

where

$$
\begin{array} { c } { { d s ^ { 2 } = - ( \omega ^ { \hat { i } } ) ^ { 2 } + ( \omega ^ { \hat { x } } ) ^ { 2 } + ( \omega ^ { \hat { \theta } } ) ^ { 2 } + ( \omega ^ { \hat { \phi } } ) ^ { 2 } , } } \\ { { { } } } \\ { { \omega ^ { \hat { t } } = d t , } } \\ { { { } } } \\ { { \omega ^ { \hat { x } } = a d \chi , } } \\ { { { } } } \\ { { \omega ^ { \hat { \theta } } = a \sin \chi d \theta , } } \\ { { { } } } \\ { { \omega ^ { \hat { \phi } } = a \sin \chi \sin \theta d \phi . } } \end{array}
$$

# A. Connection Computation

Equation (14.31b) gives, since ${ \pmb d } g _ { \mu \nu } = { \pmb d } \eta _ { \mu \nu } = 0$ , just

$$
\begin{array} { r } { { \pmb { \omega } } _ { \mu \nu } = - { \pmb { \omega } } _ { \nu \mu } ; } \end{array}
$$

so there are only six 1-forms $\omega _ { \mu \nu }$ to be found. Turn to the second basic equation (14.3la). The game now is to guess a solution (because this is so often quicker than using systematic methods) to the equations $0 = d \omega ^ { \mu } + \omega ^ { \mu } { } _ { \nu }$ >w"in which the $\omega ^ { \nu }$ and thus also dw" are known, and $\omega ^ { \mu } { } _ { \nu }$ are unknown. The solution $\omega ^ { \mu } { } _ { \nu }$ is known to be unique; so guessing (if it leads to any answer) can only give the right answer.

Proceed from the simplest such equation. From $\omega ^ { \hat { t } } = \mathsf { d } \bar { t }$ compute

$$
\begin{array} { r } { \pmb { d \omega } ^ { \hat { t } } = 0 . } \end{array}
$$

Compare this with $d \omega ^ { t } = - \omega ^ { t } { } _ { \mu } \wedge \omega ^ { \mu }$ or(since $\omega ^ { \hat { t } } { } _ { \hat { t } } = - \omega _ { \hat { t } { \hat { t } } } = 0$ by $\omega _ { \mu \nu } = - \omega _ { \nu \mu } )$

$$
d \pmb { \omega } ^ { t } = - \pmb { \omega } ^ { t } { } _ { k } \wedge \pmb { \omega } ^ { k } = 0 .
$$

This equation could be satisfied by having $\omega ^ { i } { } _ { k } \propto \omega ^ { k }$ ,or in more complicated ways with cancelations among different terms,or more simply by $\omega ^ { \hat { t } } { } _ { \ast } = 0$ . Proceed, not

looking for trouble, until some non-zero $\omega ^ { \mu } { } _ { \nu }$ is required. From $\pmb { \omega } ^ { \hat { x } } = a \pmb { d } \chi$ find

$$
\begin{array} { l } { { { \pmb d } { \pmb \omega } ^ { \hat { x } } = \dot { a } { \pmb d } t \wedge { \pmb d } \chi } } \\ { { = ( \dot { a } / a ) { \pmb \omega } ^ { \hat { t } } \wedge { \pmb \omega } ^ { \hat { x } } \doteq - ( \dot { a } / a ) { \pmb \omega } ^ { \hat { x } } \wedge { \pmb \omega } ^ { \hat { t } } . } } \end{array}
$$

Compare this with

$$
\widehat { \ L } ^ { d \omega \widehat { x } } = - \omega \widehat { \widetilde { x } } _ { \mu } \wedge \omega ^ { \mu } _ { \widehat { \ C } } 
$$

Guess that $\dot { \omega ^ { x } } _ { \hat { t } } = ( \dot { a } / a ) \omega ^ { \hat { x } }$ from the first term; and hope the other terms vanish. (Note that this allows $\pmb { \omega } ^ { \hat { t } } { } _ { \hat { x } } \wedge \pmb { \omega } ^ { \hat { x } } = - \pmb { \omega } _ { \hat { t } \hat { x } } \wedge \pmb { \omega } ^ { \hat { x } } = \pmb { \omega } _ { \hat { x } \hat { t } } \wedge \pmb { \omega } ^ { \hat { x } } = 0$ in the $\mathbf { \Delta } \mathbf { \tilde { d } } \mathbf { \Delta } \omega ^ { \hat { t } }$ equation.) Look at $\dot { \pmb { \omega } } ^ { \hat { \pmb { \theta } } } = a \sin \chi \mathbf { \delta } d \pmb { \theta }$ ,and write

$$
\begin{array} { r } { d \omega ^ { \hat { \theta } } = ( \dot { a } / a ) \omega ^ { \hat { t } } \wedge \omega ^ { \hat { \theta } } + a ^ { - 1 } \cot x \omega ^ { \hat { x } } \wedge \omega ^ { \hat { \theta } } } \\ { = - \omega ^ { \hat { \theta } } { } _ { \hat { t } } \wedge \omega ^ { \hat { t } } - \omega ^ { \hat { \theta } } { } _ { \hat { x } } \wedge \omega ^ { \hat { x } } - \omega ^ { \hat { \theta } } { } _ { \hat { \phi } } \wedge \omega ^ { \hat { \phi } } . } \end{array}
$$

Guess, consistent with previously written equations, that

$$
\begin{array} { r l } & { \pmb { \omega } ^ { \hat { \theta } } _ { \hat { t } } = \pmb { \omega } ^ { \hat { t } } _ { \hat { \theta } } = ( \dot { a } / a ) \pmb { \omega } ^ { \hat { \theta } } , } \\ & { \pmb { \omega } ^ { \hat { \theta } } _ { \hat { x } } = - \pmb { \omega } ^ { \hat { x } } _ { \hat { \theta } } = a ^ { - 1 } \cot x \pmb { \omega } ^ { \hat { \theta } } . } \end{array}
$$

Finally from

$$
\begin{array} { r l } & { \pmb { d } \pmb { \omega } ^ { \hat { \phi } } = ( \dot { a } / a ) \pmb { \omega } ^ { \hat { t } } \wedge \pmb { \omega } ^ { \hat { \phi } } + a ^ { - 1 } \cot \chi \pmb { \omega } ^ { \hat { \chi } } \wedge \pmb { \omega } ^ { \hat { \phi } } } \\ & { \qquad + \left( a \sin \chi \right) ^ { - 1 } \cot \theta \pmb { \omega } ^ { \hat { \theta } } \wedge \pmb { \omega } ^ { \hat { \phi } } } \\ & { = - \pmb { \omega } ^ { \hat { \phi } } _ { \hat { t } } \wedge \pmb { \omega } ^ { \hat { t } } - \pmb { \omega } ^ { \hat { \phi } } _ { \hat { \chi } } \wedge \pmb { \omega } ^ { \hat { \chi } } - \pmb { \omega } ^ { \hat { \phi } } _ { \hat { \theta } } \wedge \pmb { \omega } ^ { \hat { \theta } } , } \end{array}
$$

deduce values of $\boldsymbol { \omega } ^ { \hat { \phi } } { } _ { \hat { t } } , \ \boldsymbol { \omega } ^ { \hat { \phi } } { } _ { \hat { x } } ,$ and $\omega ^ { \hat { \phi } } { \hat { \theta } }$ These are not inconsistent with previous assumptions that terms like $\omega ^ { \hat { \theta } } { } _ { \hat { \phi } } \wedge \omega ^ { \hat { \phi } }$ vanish (in the $\mathbf { \delta } \mathbf { \mathcal { I } } \mathbf { \delta } \omega ^ { \widehat { \theta } }$ equation); so one has in fact solved $d \omega ^ { \mu } = - \omega ^ { \mu } { } _ { \nu } \wedge \omega ^ { \nu }$ for a set of connection forms $\omega ^ { \mu } { } _ { \nu }$ as follows:

$$
\begin{array} { r l } & { \omega ^ { \star } _ { t } = \omega ^ { \hat { i } } _ { \star } = ( \dot { a } / a ) \omega ^ { k } , } \\ & { \omega ^ { \hat { \theta } } _ { \hat { x } } = - \omega ^ { \hat { x } } _ { \hat { \theta } } = a ^ { - 1 } \cot \chi \omega ^ { \hat { \theta } } } \\ & { \qquad = \cos \chi \omega \theta , } \\ & { \omega ^ { \hat { \phi } } _ { \hat { x } } = - \omega ^ { \hat { x } } _ { \hat { \phi } } = a ^ { - 1 } \cot \chi \omega ^ { \hat { \phi } } } \\ & { \qquad = \cos \chi \sin \theta d \phi , } \\ & { \omega ^ { \hat { \phi } } _ { \hat { \theta } } = - \omega ^ { \hat { \theta } } _ { \hat { \phi } } = ( a \sin \chi ) ^ { - 1 } \cot \theta \omega ^ { \hat { \phi } } } \\ & { \qquad = \cos \theta d \phi . } \end{array}
$$

Of course,if these hit-or-miss methods of finding $\omega ^ { \mu } { } _ { \nu }$ do not work easily in some problem, one may simply use equations (l4.32) and (14.33).

# B. Curvature Computation

The curvature computation is a straightforward substitution of $\omega ^ { \mu } { } _ { \nu }$ from equations (3) above into equation (14.34),which is

$$
{ \mathcal R } ^ { \mu } { } _ { \nu } = d \omega ^ { \mu } { } _ { \nu } + \omega ^ { \mu } { } _ { \alpha } \wedge \omega ^ { \alpha } { } _ { \nu } .
$$

This equation is short enough that one can write out the sum

$$
\mathcal { R } ^ { \hat { t } } { } _ { \hat { x } } = d \omega ^ { \hat { t } } { } _ { \hat { x } } + \omega ^ { \hat { t } } { } _ { \hat { \theta } } \wedge \omega ^ { \hat { \theta } } { } _ { \hat { x } } + \omega ^ { \hat { t } } { } _ { \hat { \phi } } \wedge \omega ^ { \hat { \phi } } { } _ { \hat { x } }
$$

in contrast to the ten terms in the corresponding R= ar + T² equation [equation. )ofBo14Frdoe $( \dot { a } / a ) ^ { \bullet } \ \pmb { \omega } ^ { \hat { t } } \wedge \pmb { \omega } ^ { \hat { x } }$ .Missing is the term $( \dot { a } / a ) \mathbf { \delta } d \omega ^ { \hat { x } }$ Instead write $\begin{array} { r l } { \pmb { \omega } _ { \hat { x } } ^ { \hat { t } } = ( \dot { a } / a ) \pmb { \omega } ^ { \hat { x } } = } & { { } ^ { \ast } } \end{array}$ $\dot { \pmb { a } } \ \pmb { d } \chi$ and then find $\mathop { d \omega \hat { ^ { t } } _ { \hat { x } } } = \ddot { a }$ dt > ${ \bf \nabla } \cdot { \bf \delta } d \chi = ( \ddot { a } / a ) \omega ^ { \hat { t } } \wedge \omega ^ { \hat { x } }$ With elementary care, then, in correctly substituting from (3) for the $\omega ^ { \mu } { } _ { \nu }$ in the formula for ${ \mathcal R } ^ { \mu } { } _ { \nu }$ ,one finds

and

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathcal { R } ^ { \hat { t } } { } _ { \hat { x } } = ( \ddot { a } / a ) \pmb { \omega } ^ { \hat { t } } \wedge \pmb { \omega } ^ { \hat { x } } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathcal { R } ^ { \hat { x } } { } _ { \hat { \theta } } = ( 1 + \dot { a } ^ { 2 } ) a ^ { - 2 } \pmb { \omega } ^ { \hat { x } } \wedge \pmb { \omega } ^ { \hat { \theta } } . } } \end{array}
$$

This completes thecomputationofthe $R ^ { \mu } { } _ { \nu \alpha \beta }$ ,since inthis isotopic modelivrse all space directions in the orthonormal frame $\pmb { \omega } ^ { \pmb { \mu } }$ are algebraically equivalent. One can therefore write

$$
\begin{array} { r l } & { \mathcal { R } _ { \ k } ^ { \ t } = ( \ddot { a } / a ) \omega ^ { \hat { t } } \wedge \omega ^ { k } , } \\ & { \mathcal { R } ^ { \ k } _ { \ t } = a ^ { - 2 } ( 1 + \dot { a } ^ { 2 } ) \omega ^ { k } \wedge \omega ^ { t } , } \end{array}
$$

for the complete list of ${ \mathcal R } ^ { \mu } { } _ { \nu }$ . Specific components, such as

or

$$
R ^ { \hat { t } } { } _ { { \hat { x } } { \hat { t } } { \hat { x } } } = \ddot { a } / a , \qquad R ^ { \hat { t } } { } _ { { \hat { x } } { \hat { t } } { \hat { \theta } } } = 0 ,
$$

$$
R ^ { \hat { t } } { } _ { { \hat { \theta } } { \hat { x } } { \hat { \phi } } } = 0 , \qquad R ^ { \hat { \theta } } { } _ { { \hat { \phi } } { \hat { \theta } } { \hat { \phi } } } = a ^ { - 2 } ( 1 + { \dot { a } } ^ { 2 } ) ,
$$

are easily read out of this display of ${ \mathcal R } ^ { \mu } { } _ { \nu }$

# C.. Contraction

From equations (14.7), find

and

$$
\begin{array} { l } { { G ^ { \hat { t } \hat { t } } = + 3 a ^ { - 2 } ( 1 + \dot { a } ^ { 2 } ) , } } \\ { { \ } } \\ { { G ^ { \hat { t } \hat { x } } = G ^ { \hat { t } \hat { \theta } } = G ^ { \hat { t } \hat { \phi } } = 0 = G ^ { \hat { x } \hat { \theta } } = G ^ { \hat { \theta } \hat { \phi } } = G ^ { \hat { \phi } \hat { x } } , } } \\ { { \ } } \\ { { G ^ { \hat { x } \hat { x } } = G ^ { \hat { \theta } \hat { \theta } } = G ^ { \hat { \phi } \hat { \phi } } = - [ 2 a ^ { - 1 } \ddot { a } + a ^ { - 2 } ( 1 + \dot { a } ^ { 2 } ) ] , } } \end{array}
$$

$$
R = - G ^ { \mu } { } _ { \mu } = 6 [ a ^ { - 1 } \ddot { a } + a ^ { - 2 } ( 1 + \dot { a } ^ { 2 } ) ] .
$$

If guessing is not easy, there is a systematic way to solve equations (l4.31） in an orthonormal frame or in any other frame in which $\mathbf { \Delta } _ { d g _ { \mu \nu } } = 0$ .Compute the $\pmb { d } \pmb { u } ^ { \mu }$ and arrange them in the format

$$
d \omega ^ { \alpha } = - c _ { | \mu \nu | } ^ { \alpha } \omega ^ { \mu } \wedge \omega ^ { \nu } .
$$

In this way display the 24 “commutation coefficients” ${ c _ { \mu \nu } } ^ { \alpha }$ . These quantities enter into the formula

$$
\omega _ { \mu \nu } = \frac { 1 } { 2 } ( c _ { \mu \nu \alpha } + c _ { \mu \alpha \nu } - c _ { \nu \alpha \mu } ) \omega ^ { \alpha }
$$

to provide the six $\omega ^ { \mu } { } _ { \nu }$ (exercise 14.12).

(3) caiculate curvature 2-forms $\mathcal { R } ^ { \mu }$

Once the $\omega _ { \mu \nu }$ are known, one computes the curvature forms ${ \mathcal R } ^ { \mu } { } _ { \nu }$ (again only six in four dimensions, since $\mathcal { R } ^ { \mu \nu } = - \mathcal { R } ^ { \nu \mu } )$ by use of the formula

$$
{ \mathcal R } ^ { \mu } { } _ { \nu } = d \omega ^ { \mu } { } _ { \nu } + \omega ^ { \mu } { } _ { \alpha } \wedge \omega ^ { \alpha } { } _ { \nu } .
$$

(4) calculate components of curvature tensors

Out of this tabulation, one reads the individual components of the curvature tensor by using the identification scheme

$$
{ \mathcal R } ^ { \mu \nu } = { R ^ { \mu \nu } } _ { | \alpha \beta | } \mu ^ { \alpha } \wedge \omega ^ { \beta } .
$$

The Einstein tensor $G ^ { \mu } { } _ { \nu }$ is computed by scanning the ${ \mathcal { R } } ^ { \mu \nu }$ display to find the appropriate $R ^ { \mu \nu } { } _ { \alpha \beta }$ components for use in formulas (14.7).

# EXERCISES

# Exercise 14.5. EXTERIOR DERIVATIVE OF A PRODUCT OF FORMS

Establish equation (14.l3a) by working up recursively from forms of lower order to forms of higher order.[Hints:Recall from equation (4.27) that for a $p$ -form

$$
\alpha = \alpha _ { | \mu _ { 1 } \dots \mu _ { p } | } d x ^ { \mu _ { 1 } } \wedge \dots \wedge d x ^ { \mu _ { p } } ,
$$

the exterior derivative is defined by

$$
d \alpha = \frac { \partial \alpha _ { \{ \mu _ { 1 } \dots \mu _ { p } \} } } { \partial x ^ { \mu _ { 0 } } } d x ^ { \mu _ { 0 } } \wedge d x ^ { \mu _ { 1 } } \wedge \cdot \cdot \cdot \wedge d x ^ { \mu _ { p } } .
$$

Applied to the product $\alpha \wedge \beta$ of two l-forms, this formula gives

$$
\begin{array} { r l } & { d ( \alpha \wedge \beta ) = d [ ( \alpha _ { \lambda } d x ^ { \lambda } ) \wedge ( \beta _ { \mu } d x ^ { \mu } ) ] } \\ & { \qquad = d [ ( \alpha _ { \lambda } \beta _ { \mu } ) ( d x ^ { \lambda } \wedge d x ^ { \mu } ) ] } \\ & { \qquad = \frac { \hat { \partial } ( \alpha _ { \lambda } \beta _ { \mu } ) } { \partial x ^ { \kappa } } d x ^ { \kappa } \wedge d x ^ { \lambda } \wedge d x ^ { \mu } } \\ & { \qquad = \Big ( \frac { \hat { \partial } \alpha _ { \lambda } } { \partial x ^ { \kappa } } d x ^ { \kappa } \wedge d x ^ { \lambda } \Big ) \wedge \beta _ { \mu } d x ^ { \mu } - ( a _ { \lambda } d x ^ { \lambda } ) \wedge \Big ( \frac { \hat { \partial } \beta _ { \mu } } { \partial x ^ { \kappa } } d x ^ { \kappa } \wedge d x ^ { \mu } \Big ) } \\ & { \qquad = ( d \alpha ) \wedge \beta - \alpha \wedge d \beta . } \end{array}
$$

Extend the reasoning to forms of higher order.]

# Exercise 14.6. RELATIONSHIP BETWEEN EXTERIOR DERIVATIVE AND COMMUTATOR

Establish formula (l4.21) by showing(a) that the righthand side is an algebraic linear function of $\pmb { u }$ and an algebraic linear function of $\pmb { \nu } ,$ and (b） that the equation holds when $\pmb { u }$ and $\pmb { \nu }$ are coordinate basis vectors $\pmb { \mu } = \widehat { \sf { d } } / \widehat { \sf { d } } x ^ { k }$ ， $\pmb { \nu } = \hat { \pmb { \sigma } } / \hat { \partial } \pmb { x } ^ { \pmb { \imath } }$

ExerciSe 14.7. CHRISTOFFEL FORMULA DERIVED FROM CONNECTION FORMS In a coordinate frame $\pmb { \omega } ^ { \mu } = \pmb { d } x ^ { \mu }$ , show that equation (14.3la) requires $T ^ { \mu } { } _ { \alpha \beta } = T ^ { \mu } { } _ { \beta \alpha }$ and that, with this symmetry established,equation (l4.31b) gives an expression for $\partial g _ { \mu \nu } / \partial x ^ { \alpha }$ which can be solved to give the Christoffel formula

$$
{ T ^ { \mu } } _ { \alpha \beta } = { \frac { 1 } { 2 } } g ^ { \mu \nu } \biggl ( { \frac { \partial g _ { \nu \alpha } } { \partial x ^ { \beta } } } + { \frac { \partial g _ { \nu \beta } } { \partial x ^ { \alpha } } } - { \frac { \partial g _ { \alpha \beta } } { \partial x ^ { \nu } } } \biggr ) .
$$

# Exercise 14.8. RIEMANN-CHRISTOFFEL CURVATURE FORMULA RELATED TO CURVATURE FORMS

Substitute $\omega ^ { \mu } { } _ { \nu } = \Gamma ^ { \mu } { } _ { \nu \lambda } d x ^ { \lambda }$ into equation (14.18),and from the result read out, according to equation (1425),the classical formua (3)of $\ B \circ \mathbf { x } \ 1 4 . 2$ for the components $R ^ { \mu } { } _ { \nu \alpha \beta }$

# Exercise 14.9. MATRIX NOTATION FOR REVIEW OF CARTAN STRUCTURE EQUATIONS

Let $e \equiv ( \pmb { \sigma } _ { 1 } , \dots , \pmb { \sigma } _ { n } )$ be a row matrix whose entries are the basis vectors,and let $\pmb { \omega }$ be a column of basis 1-forms $\pmb { \omega } ^ { \pmb { \mu } }$ Similarly let $\mathcal { Q } = | | \boldsymbol { \omega ^ { \mu } } _ { \nu } | |$ and $\mathcal { R } = | | \mathcal { R } , \mu _ { _ { p } } | |$ be square matrices with l-form and 2-form entries. This gives a compact notation in which $d \pmb { \theta } _ { \mu } = \pmb { \theta } _ { \nu } \pmb { \omega } _ { \mu } ^ { \nu }$ and $d \circ \bar { \mathcal { P } } = \bullet _ { \mu } \pmb { \omega } ^ { \mu }$ read

$$
\pmb { d e } = e \varOmega \ \mathrm { a n d } \ \pmb { d } \varphi = e \omega ,
$$

respectively.

(a)From equations (l4.37)and ${ \pmb d } ^ { 2 \varrho } = 0$ ,derive equation (14.3la) in the form

$$
0 = d \omega + \varOmega \wedge \omega .
$$

[Solution: $d ^ { 2 { \varphi } } = d e \wedge \omega + e d \omega = e ( { \varOmega } \wedge \omega + d \omega ) . ]$

(b） Compute ${ \pmb d } ^ { 2 } e$ as motivation for definition (14.18),which reads

$$
{ \mathcal { R } } = d { \mathcal { Q } } + { \mathcal { Q } } \wedge { \mathcal { Q } } .
$$

(c）From ${ \pmb d } ^ { 2 } { \pmb \omega } = 0$ ， deduce ${ \mathcal R } \wedge \omega = 0$ and then decompress the notation to get the antisymmetry relation $R ^ { \mu } { } _ { [ \alpha \beta \gamma ] } = 0$

(d) Compute $\pmb { d } \pmb { \mathcal { R } }$ from equation (14.39),and relate it to the Bianchi identity $R ^ { \mu } { } _ { \nu [ \alpha \beta ; \gamma ] } = 0$ (e) Let $v = \{ v ^ { \mu } \}$ be a column of functions; so $v = e v = \theta _ { \mu } v ^ { \mu }$ is a vector field.Compute, in compact notation, $\pmb { d } \pmb { v }$ and $\scriptstyle \pmb { d } ^ { 2 } \pmb { v }$ to show ${ \pmb d } ^ { 2 } { \pmb v } = e \Re { \pmb v }$ (which is equation 14.17).

# Exercise 14.10. TRANSFORMATION RULES FOR CONNECTION FORMS IN COMPACT NOTATION

Using the notation of the previous exercise,write $e ^ { \prime } = e A$ in place of ${ \pmb \sigma } _ { \mu ^ { \prime } } = { \pmb \sigma } _ { \nu } A ^ { \prime } { } _ { \mu ^ { \prime } }$ and similarly $\omega ^ { \prime } = A ^ { - 1 } \omega$ ,to represent a change of frame. Show that ${ \pmb d } ^ { o p } \equiv e \omega \doteq e ^ { \prime } \omega ^ { \prime }$ Substitute $e ^ { \prime } = e A$ in $\pmb { d e ^ { \prime } } = e ^ { \prime } \pmb { \varOmega ^ { \prime } }$ to deduce the transformation law

$$
\varOmega ^ { \prime } = A ^ { - 1 } \varOmega A + A ^ { - 1 } \ I A .
$$

Rewrite this in decompressed notation for coordinate frames with $A ^ { \nu } { } _ { \mu ^ { ' } } = \widehat { \sigma } x ^ { \nu } / \widehat { c } x ^ { \mu ^ { ' } }$ as a formula of the form $T ^ { \mu ^ { \prime } } { } _ { \alpha ^ { \prime } \beta ^ { \prime } } = ( ? )$

ExerciSe 14.11. SPACE IS FLAT IF THE CURVATURE VANISHES (see $\mathfrak { s } 1 1 . 5 )$ If coordinates exist in which all straight lines $( d ^ { 2 } x ^ { \mu } / d \lambda ^ { 2 } = 0 \mathrm { , }$ are geodesics,then one says the space is fat. Evidently all $T ^ { \mu } { } _ { \alpha \beta }$ and $R ^ { \mu } { } _ { \nu \alpha \beta }$ vanish in this case,by equation (14.8) and equation (3) in Box 14.2. Show conversely that,if $\langle \mathcal { H } = 0$ ,then such coordinates exist.Use the results of the previous problem to find differential equations for a transformation $\pmb { A }$ to a basis $e ^ { \prime }$ where $\varOmega ^ { \prime } = 0$ .What are the conditions for complete integrability of these equations? [Note that ${ \pmb d } f _ { K } = F _ { K } ( { \pmb x } , f )$ is completely integrable if ${ \pmb d } ^ { 2 } f _ { K } = 0$ modulo the original equations.] Why will the basis forms $\omega ^ { \mu ^ { \prime } }$ in this new frame be coordinate differentials $\pmb { \omega } ^ { \mu ^ { \prime } } = \pmb { d } x ^ { \mu ^ { \prime } } ?$

# Exercise 14.12. SYSTEMATIC COMPUTATION OF CONNECTION FORMS IN ORTHONORMAL FRAMES

Deduce equation (14.32) by applying equation (14.21) to basis vectors, using equations (8.14) to define ${ c _ { \mu \nu } } ^ { \alpha }$ .Then show that, in an orthonormal frame (or any frames with $g _ { \mu \nu } = \mathrm { c o n s t } )$ ， equation (14.33) provides a solution of equations (l4.31),which define $\omega ^ { \mu } { } _ { \nu }$ .[Compare also equation (8.24b).]

# Exercise 14.13. SCHWARZSCHILD CURVATURE FORMS

Use the obvious orthonormal frame ${ \pmb { \omega } } ^ { \hat { t } } = e ^ { \phi } { \pmb { d } } t$ ， ${ \pmb { \omega } } ^ { \hat { r } } = e ^ { { \pmb { \Lambda } } } { \pmb { d r } }$ ， $\omega ^ { \hat { \theta } } = r d \theta$ ， $\pmb { \omega } ^ { \hat { \phi } } = r \sin \theta \mathbf { \delta } \mathbf { d } \phi$ for the Schwarzschild metric

$$
d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

in which $\pmb { \phi }$ and $\pmb { A }$ are functions of $r$ only; and compute the curvature forms $\mathcal { R } \hat { \pmb { \mu } } _ { \hat { \pmb { \nu } } }$ and the Einstein tensor $G ^ { \hat { \boldsymbol { \mu } } } { } _ { \hat { \boldsymbol { \nu } } }$ by the methods of Box 14.5.[Answer: $\mathcal { R } ^ { t \hat { \tau } } = E \pmb { \omega } ^ { \hat { t } } \wedge \pmb { \omega } ^ { \hat { \tau } }$ ， $\mathcal { R } ^ { \hat { t } \hat { \theta } } = \overline { { E } } w ^ { \hat { t } } \wedge$ $\omega ^ { \hat { \theta } }$ ， $\mathcal { R } ^ { \hat { t } \hat { \phi } } = \overrightarrow { E } w ^ { \hat { t } } \wedge \overrightarrow { w ^ { \hat { \phi } } }$ ， $\mathcal { R } ^ { \hat { \theta } \hat { \phi } } = F \omega ^ { \hat { \theta } } \wedge \omega ^ { \hat { \phi } }$ ， $\mathcal { R } ^ { \hat { \phi } \hat { r } } = \widetilde { F } \pmb { \omega } ^ { \hat { \phi } } \wedge \pmb { \omega } ^ { \hat { \tau } }$ ， $\mathcal { R } ^ { \hat { \tau } \hat { \theta } } = \widetilde { F } w ^ { \hat { \tau } } \wedge \omega ^ { \hat { \theta } }$ ,with

$$
\begin{array} { l } { E = - e ^ { - 2 A } ( \phi ^ { \prime \prime } + \phi ^ { \prime 2 } - \phi ^ { \prime } A ^ { \prime } ) , } \\ { \displaystyle \bar { E } = - \frac { 1 } { r } e ^ { - 2 A } \phi ^ { \prime } , } \\ { F = \frac { 1 } { r ^ { 2 } } ( 1 - e ^ { - 2 A } ) , } \\ { \displaystyle \bar { F } = \frac { 1 } { r } e ^ { - 2 A } A ^ { \prime } ; } \end{array} -
$$

and then

$$
\begin{array} { r l } & { G _ { t } ^ { \hat { t } } = - ( F + 2 \bar { F } ) , } \\ & { G _ { \hat { \tau } } ^ { \hat { r } } = - ( F + 2 \bar { E } ) , } \\ & { G _ { \hat { \theta } } ^ { \hat { \theta } } = G _ { \hat { \phi } } ^ { \hat { \phi } } = - ( E + \bar { E } + \bar { F } ) , } \\ & { G _ { \hat { \tau } } ^ { \hat { t } } = G _ { \hat { \theta } } ^ { \hat { t } } = G _ { \hat { \phi } } ^ { \hat { t } } = 0 = G _ { \hat { \theta } } ^ { \hat { \tau } } = G _ { \hat { \phi } } ^ { \hat { \tau } } = G _ { \hat { \phi } } ^ { \hat { \theta } } . } \end{array}
$$

# ExerciSe 14.14. MATRIX DISPLAY OF THE RIEMANN-TENSOR COMPONENTS

Use the symmetries of the Riemann tensor to justify displaying its components in an orthonormal frame in the form

$$
\hat { R ^ { \hat { \mu } \hat { \nu } } } _ { \hat { \alpha } \hat { \beta } } = \sum _ { 2 3 } ^ { 0 1 } \left( \begin{array} { c } { { 1 } } \\ { { E } } \\ { { E } } \\ { { -- } } \\ { { - H ^ { T } } } \\ { { 1 2 } } \end{array} \right) , ~ \overbrace { \left( \begin{array} { c } { { 1 } } \\ { { 2 } } \\ { { 3 } } \\ { { 2 } } \end{array} \right) } ^ { \hat { 0 } 1 } = \overbrace { \left( \begin{array} { c } { { E } } \\ { { 2 } } \\ { { 3 } } \\ { { 2 } } \\ { { 3 } } \end{array} \right) } ^ { \hat { 1 } } ,
$$

where the rows are labeled by index pairs $\hat { \mu } \hat { \nu } = 0 1$ , 02,etc., as shown; and the columns ${ \hat { \alpha } } { \hat { \boldsymbol { \beta } } }$ ， similarly. Here $E , F ,$ and $\pmb { H }$ are each $3 \times 3$ matrices with (why?)

$$
E = E ^ { T } , \qquad F = F ^ { T } , \qquad \mathrm { t r a c e } \ H = 0 ,
$$

where $E ^ { T }$ means the transpose of $E .$

# Exercise 14.15. RIEMANN MATRIX WITH VANISHING EINSTEIN TENSOR

Show that the empty-space Einstein equations $G ^ { \hat { \mu } } { } _ { \hat { \nu } } = 0$ allow the matrix in equation (14.44) to be simplified to the form

$$
R ^ { \hat { \mu } \hat { \nu } } { } _ { \hat { \alpha } \hat { \beta } } = \left( { - { \frac { E } { - H } } { \stackrel { \dagger } { _ { \parallel } } } { - \frac { H } { E } } { - \nonumber } } \right) ,
$$

where now, in addition to the equality $E = F$ that this form implies,the further conditions

$$
\mathsf { r a c e \ } E = 0 , H = H ^ { T }
$$

hold.

# Exercise 14.16. COMPUTATION OF CURVATURE FOR A PULSATING OR COLLAPSING STAR

Spherically symmetric motions of self-gravitating bodies are discussed in Chapters 26 and 32.A metric form often adopted in this situation is

$$
d s ^ { 2 } = \ O - e ^ { 2 \phi } d T ^ { 2 } + e ^ { 2 A } d R ^ { 2 } + \ o r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

where now ${ \pmb { \phi } } , { \pmb { \varLambda } } .$ and $r$ are each functions of the two coordinates $R$ and $T .$ Compute the curvature 2-forms and the Einstein tensor for this metric, using the methods of Box l4.5. In the guessing of the $\omega ^ { \mu } { } _ { p }$ ,most of the terms will already be evident from the corresponding calculation in exercise l4.13.[Answer, in the obvious orthonormal frame $\pmb { \omega } ^ { \hat { T } } = e ^ { \phi } \mathbf { \vec { d } } \hat { T } , \pmb { \omega } ^ { \hat { R } } =$ $e ^ { \lambda } \partial R$ ， $\omega ^ { \hat { \theta } } = r d \theta$ ， $\omega ^ { \hat { \phi } } = r$ sin $\theta \left. d \phi \right.$ ：

$$
\begin{array} { r l } & { \mathcal { R } ^ { \hat { T } } _ { \hslash } = E \omega ^ { \hat { T } } \wedge \omega ^ { \hat { R } } , } \\ & { \mathcal { R } ^ { \hat { T } } _ { \hat { \theta } } = \bar { E } \omega ^ { \hat { T } } \wedge \omega ^ { \hat { \theta } } + H \omega ^ { \hat { R } } \wedge \omega ^ { \hat { \theta } } , } \\ & { \mathcal { R } ^ { \hat { T } } _ { \hat { \phi } } = \bar { E } \omega ^ { \hat { T } } \wedge \omega ^ { \hat { \phi } } + H \omega ^ { \hat { R } } \wedge \omega ^ { \hat { \phi } } , } \\ & { \mathcal { R } ^ { \hat { \theta } } _ { \hat { \phi } } = F \omega ^ { \hat { \theta } } \wedge \omega ^ { \hat { \phi } } , } \\ & { \mathcal { R } ^ { \hat { R } } _ { \hat { \theta } } = \bar { F } \omega ^ { \hat { R } } \wedge \omega ^ { \hat { \theta } } - H \omega ^ { \hat { T } } \wedge \omega ^ { \hat { \theta } } , } \\ & { \mathcal { S } ^ { \hat { \theta } } _ { \hat { \phi } } = \bar { F } \omega ^ { \hat { R } } \wedge \omega ^ { \hat { \phi } } - H \omega ^ { \hat { T } } \wedge \omega ^ { \hat { \phi } } , } \end{array}
$$

which,in the matrix display of exercise 14.14,gives

$$
\begin{array}{c} { R ^ { \mu \nu } } _ { \alpha \beta } = ( \begin{array} { l l l l l l } { E } & { . } & { . } & { . } & { . } & { . } \\ { . } & { \dot { E } } & { . } & { 1 } & { . } & { . } & { H } \\ { . } & { . } & { . } & { . } & { . } & { - } \end{array} ) \frac { \hat { T } \hat { R } } { \hat { \theta } }  \\ { \quad \cdot \underbrace { - \dot { \Pi } ^ { \mu \nu } } _ { . } } & { . } & { . } & { . } & { . } \\ { . } & { . } & { H } & { . } & { \dot { F } } & { . } \\ { . } & { - H } & { . } & { . } & { . } & { \dot { F } } \end{array} ) \frac { \hat { T } \hat { \phi } } { \hat { \theta } \hat { \phi } } \ .
$$

Here

$$
\begin{array} { l } { E = e ^ { - 2 \phi } ( \ddot { \lambda } + \dot { \lambda } ^ { 2 } - \dot { \lambda } \dot { \phi } ) - e ^ { - 2 A ( \phi ^ { \prime \prime } + \phi ^ { \prime 2 } - \phi ^ { \prime } \mathcal { A } ^ { \prime } ) } , } \\ { \ddot { E } = \frac { 1 } { r } e ^ { - 2 \phi } ( \ddot { r } - \dot { r } \dot { \phi } ) - \frac { 1 } { r } e ^ { - 2 A _ { r } \dot { r } \phi ^ { \prime } } , } \\ { H = \frac { 1 } { r } e ^ { - \phi - A } ( \dot { r } ^ { \prime } - \dot { r } \dot { \phi } ^ { \prime } - r ^ { \prime } \dot { \lambda } ) , } \\ { F = \frac { 1 } { r ^ { 2 } } ( 1 - r ^ { \prime 2 } e ^ { - 2 A } + \dot { r } ^ { 2 } e ^ { - 2 \phi } ) , } \\ { \ddot { F } = \frac { 1 } { r } e ^ { - 2 \phi } \dot { r } \dot { A } + \frac { 1 } { r } e ^ { - 2 A } ( r ^ { \prime } \mathcal { A } ^ { \prime } - r ^ { \prime \prime } ) . } \end{array}
$$

The Einstein tensor is

$$
\begin{array} { r l } & { G ^ { \hat { \cal T } \hat { r } } = - G ^ { \hat { r } } { _ \hat { r } } = F + 2 \bar { F } , } \\ & { G ^ { \hat { \cal T } \hat { R } } = G ^ { \hat { r } } { _ \hat { R } } = 2 H , } \\ & { G ^ { \hat { \cal T } } { _ \hat { \theta } } = G ^ { \hat { r } } { _ \hat { \phi } } = 0 , } \\ & { G ^ { \hat { \cal R } } { _ \hat { R } } = - ( 2 \bar { E } + F ) , } \\ & { G ^ { \hat { \theta } } { _ \hat { \theta } } = G ^ { \hat { \phi } } { _ \hat { \phi } } = - ( E + \bar { F } + \bar { F } ) , } \\ & { G ^ { \hat { \cal R } } { _ \hat { \theta } } = G ^ { \hat { \cal R } } { _ \hat { \phi } } = G ^ { \hat { \theta } } { _ \hat { \phi } } = 0 . 1 } \end{array}
$$

Exercise 14.17. BIANCHI IDENTITY IN ${ \pmb d } \mathcal { R } = { \pmb 0 }$ FORM Define the Riemann tensor as a bivector-valued 2-form,

$$
\mathcal { R } = \frac { 1 } { 2 } \pmb { \sigma } _ { \mu } \wedge \pmb { \varrho } _ { \nu } \mathcal { R } ^ { \mu \nu } ,
$$

and evaluate $\pmb { d } \pmb { \mathcal { H } }$ to make it manifest that $\pmb { d } \mathcal { R } = 0$ Use

$$
{ \mathcal R } ^ { \mu \nu } = d \omega ^ { \mu \nu } - \omega ^ { \mu } { } _ { \alpha } \wedge \omega ^ { \nu \alpha } ,
$$

which is derived easily in an orthonormal frame (adequate for proving ${ \pmb d } \mathscr { R } = 0 )$ ，or (as a test of skill) in a general frame where ${ \mathcal { R } } ^ { \mu \nu } = { \mathcal { R } } ^ { \mu } { } _ { \alpha } g ^ { \alpha \nu }$ and (why?) $d g ^ { \mu \nu } = - g ^ { \mu \alpha } ( d g _ { \alpha \beta } ) g ^ { \beta \nu }$ [Note: only wedge products between forms (not those between vectors) count in fixing signs in the product rule (14.13) for ${ \pmb d } .$

# Exercise 14.18. LOCAL CONSERVATION OF ENERGY AND MOMENTUM: ${ \pmb { d } } ^ { * } { \pmb { T } } = { \pmb { 0 } }$ MEANS $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \ \end{array}$

Let the duality operator \*,as defined for exterior differential forms in $\ B \circ \mathbf { x } \ 4 . 1$ act on the forms,but not on the contravariant vectors, which appear when the stress-energy tensor $\pmb { \tau }$ Or the Einstein tensor $\pmb { G }$ is written as a mixed $( \mathbf { \small \frac { 1 } { 1 } } )$ tensor:

or

$$
\begin{array} { r } { { \pmb { T } = \pmb { \varrho } _ { \mu } T ^ { \mu } { } _ { \nu } \pmb { \omega } ^ { \nu } } } \\ { { \pmb { G } = \pmb { \varrho } _ { \mu } G ^ { \mu } { } _ { \nu } \pmb { \omega } ^ { \nu } . } } \end{array}
$$

(a) Give an expression for $^ { \ast \tau }$ (or $\yen 6$ ） expanded in terms of basis vectors and forms.

(b） Show that

$$
{ } ^ { \ast } T = \sigma _ { \mu } T ^ { \mu \nu } d ^ { 3 } \Sigma _ { \nu } ,
$$

where $d ^ { 3 } \Sigma _ { \nu } = \epsilon _ { \nu \mid \alpha \beta \gamma \mid } \omega ^ { \alpha } \wedge \omega ^ { \beta } \wedge \omega ^ { \gamma }$ [see Box 5.4 and equations (8.10)].

(c） Compute $\pmb { d } ^ { \ast } \pmb { T }$ using the generalized exterior derivative $\pmb { d }$ find that

$$
d ^ { * } T = { \theta } _ { \mu } T ^ { \mu \nu } { } _ { ; \nu } \sqrt { | g | } \omega ^ { 0 } \wedge \omega ^ { 1 } \wedge \omega ^ { 2 } \wedge \omega ^ { 3 } .
$$

2
