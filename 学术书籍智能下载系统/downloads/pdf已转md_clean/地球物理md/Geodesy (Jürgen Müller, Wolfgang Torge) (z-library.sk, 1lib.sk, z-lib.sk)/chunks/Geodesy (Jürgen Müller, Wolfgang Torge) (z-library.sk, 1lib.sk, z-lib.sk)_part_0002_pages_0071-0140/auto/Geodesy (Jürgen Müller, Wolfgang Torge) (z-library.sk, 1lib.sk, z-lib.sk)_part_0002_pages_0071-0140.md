![](images/0e0ddac7f1f7effa4758fe19843cfc480cb36c353c4a145ca73acdd8e0981d98.jpg)  
Fig. 3.5: Outer surface normal on the bounding surface and on the equipotential surface.

Taking the limit at the source point $P ^ { \prime }$ in (3.34), equation (3.32) reduces to Poisson’s differential equation (3.31) and to Laplace’s differential equation for the exterior space $( \rho = 0 )$ ). Based on Gauss’ formula, basic relationships can be established between observations in the gravity fi eld and parameters describing the surface $S ,$ cf. [6.5.1].

# 3.1.4 Centrifugal acceleration, centrifugal potential

The centrifugal force acts on any object of mass of the Earth. It arises as a result of the rotation of the Earth about its axis. We assume here a rotation of constant angular velocity $\omega$ about the rotation (or spin) axis, with the axis assumed fi xed with the Earth. The small effects of time variations of the rotation vector can be taken into account by reductions, cf. [2.3.4]. The centrifugal acceleration

$$
\mathbf { z } = ( \mathbf { \boldsymbol { \omega } } \times \mathbf { \boldsymbol { r } } ) \times \mathbf { \boldsymbol { \omega } } = \omega ^ { 2 } \mathbf { p }
$$

acting on a unit mass is directed outward and is perpendicular to the spin axis (Fig. 3.6). With the geocentric latitude ${ \overline { { \varphi } } } ,$ we have the distance to the rotation axis

$$
p = r { \cos } \overline { { \varphi } }
$$

and the magnitude of the centrifugal acceleration

$$
Z = \left| \mathbf { z } \right| = \omega ^ { 2 } r \mathrm { C O s } \overline { { \varphi } } .
$$

![](images/02cb268d36a4874b563c95bc954fe765489ed696c23d348e6ede3f9dd813ca4d.jpg)  
Fig. 3.6: Gravitation, centrifugal acceleration, and gravity.

The angular velocity

$$
\omega = 7 . 2 9 2 \ 1 1 5 \times 1 0 ^ { - 5 } \mathrm { r a d } s ^ { - 1 }
$$

is known with high accuracy from astronomy, cf. [2.2.2]. Consequently, the centrifugal acceleration $z = | \pmb { z } |$ can be calculated if the position of $P$ is known.

As the $Z .$ -axis of the Earth-fi xed $X ,$ Y, $Z .$ -system coincides with the axis of rotation, cf. [2.4.2], we have

$$
\mathbf { p } = { \binom { X } { Y } } , p = | \mathbf { p } | = { \sqrt { X ^ { 2 } + Y ^ { 2 } } } .
$$

With

$$
\mathbf { z } = \mathrm { g r a d } Z ,
$$

we introduce the centrifugal potential

$$
Z = Z ( p ) = { \frac { \omega ^ { 2 } } { 2 } } p ^ { 2 } , \ \operatorname * { l i m } _ { p  0 } Z = 0 .
$$

Remark: Here, the symbols $Z$ and $Z$ are used for the centrifugal acceleration and potential, respectively. They were introduced earlier for local and global coordinates and will be employed again as such in later sections.

Differentiating twice and applying the Laplacian operator yields

$$
\Delta Z = 2 ~ \omega ^ { 2 } .
$$

Therefore, the analytic function $Z ,$ as opposed to $V \left( 3 . 2 9 \right) ,$ , is not harmonic.

For points on the equator of the Earth, the centrifugal potential has a value of $1 . 1 \times$ $1 0 ^ { 5 } \mathsf { m } ^ { 2 } \mathsf { s } ^ { - 2 } ,$ and the centrifugal acceleration is $0 . 0 3 \textrm { m } s ^ { - 2 }$ $( \approx 0 . 3 \%$ of gravitation). At the poles, we have $Z = 0$ and $Z = 0$ .

# 3.1.5 Gravity acceleration, gravity potential

The gravity acceleration, or gravity g (Latin: gravitas), is the resultant of gravitation b and centrifugal acceleration $\mathbf { z }$ (Fig. 3.6):

$$
{ \bf { g } } = { \bf { b } } + { \bf { z } } .
$$

By multiplying with the mass $m$ of the attracted point, we obtain the force of gravity

$$
\mathbf { F } = m \mathbf { g } .
$$

The direction of $\mathbf { g }$ is referred to as the direction of the plumb line (vertical); the magnitude $g$ is called gravity intensity (generally just gravity). With (3.10) and (3.38), the gravity potential of the Earth becomes

$$
W = W ( \mathbf { r } ) = V + Z = G \int \limits _ { \mathrm { E a r t h } } \int \displaylimits _ { \overline { { I } } } ^ { \rho } d V + \frac { \omega ^ { 2 } } { 2 } p ^ { 2 } .
$$

It is related to the gravity acceleration by

$$
\mathbf { g } = \operatorname { g r a d } W .
$$

In the X, Y, $Z .$ -system, we have

$$
\mathbf { g } ^ { \mathsf { T } } = \left( \operatorname { g r a d } W \right) ^ { \mathsf { T } } = ( W _ { \chi } W _ { \gamma ^ { \prime } } W _ { Z } ) .
$$

Taking (2.18) into account, we obtain the components of gravity expressed by the plumb line parameters astronomical latitude and longitude $\Phi$ , Λ:

$$
\mathbf { g } = - g \mathbf { n } = - g { \left( \begin{array} { l } { \cos \Phi \cos \Lambda } \\ { \cos \Phi \sin \Lambda } \\ { \phantom { - } \sin \Phi } \end{array} \right) } .
$$

The property

$$
\mathbf { \tau } _ { \mathrm { C U r } } | \mathbf { g } = \mathbf { \mathrm { C u r l } } \mathbf { \mathrm { g r a d } } W = 0
$$

follows from the corresponding properties of gravitation and centrifugal acceleration and can also be expressed by the conditions

$$
W _ { _ { X Y } } = W _ { _ { Y X ^ { \prime } } } \ W _ { _ { X Z } } = W _ { _ { Z X ^ { \prime } } } \ W _ { _ { Y Z } } = W _ { _ { Z Y } } .
$$

$W$ and its fi rst derivatives are single-valued, fi nite, and continuous in the whole space as a consequence of the characteristics of $V$ and $Z .$ Exceptions are the uninteresting cases $r {  } { \infty }$ (then also $Z {  } { \infty } )$ ) and $g = 0$ (direction of the plumb line is not unique). Due to the behavior of $V ,$ the second derivatives of $W$ are discontinuous inside the Earth at abrupt density changes. For geodesy, the most important surface of discontinuity is the physical surface of the Earth, with a density jump from $1 . 3 \mathrm { ~ k g } \mathrm { m } ^ { - 3 }$ (density of air) to $2 7 0 \dot { 0 } \dot { \mathrm { k g } } \mathrm { m } ^ { - 3 }$ (mean density of the upper crust).

From (3.31) and (3.39), we obtain the generalized Poisson differential equation

$$
\Delta W = - 4 \pi G \rho + 2 \omega ^ { 2 } .
$$

In outer space $( \rho = 0 )$ ), it becomes the generalized Laplace differential equation

$$
\Delta W = 2 \omega ^ { 2 } .
$$

With the conditions (3.47) and (3.48) resp. (3.49), the gravity potential $W$ possesses only fi ve (out of nine) mutually independent second derivatives. They are closely related to the curvature of the level surfaces and the plumb lines, cf. [3.2.2].

Because of the fl attening at the Earth’s poles and the centrifugal acceleration, $g$ depends on the latitude. As found in [3.1.2], the gravitation for a spherical model is $9 . { \dot { 8 } } 2 ~ \mathrm { m } \mathrm { s } ^ { - 2 } ,$ , this value decreases at the equator and increases at the poles of an ellipsoidal model. The centrifugal acceleration further diminishes the equatorial value, while gravitation at the poles is not affected by centrifugal acceleration, cf. [3.1.4]. As a result, gravity varies between $9 . 7 8 ~ \mathrm { m } \ : \mathrm { s } ^ { - 2 }$ (equator) and $9 . 8 3 ~ \mathsf { m } \mathsf { s } ^ { - 2 }$ (poles), see also [4.3].

# 3.2 Geometry of the gravity fi eld

A geometrical representation of the gravity fi eld is given by the level surfaces and the plumb lines [3.2.1]. Local fi eld properties are described by the curvatures of level surfaces and plumb lines [3.2.2], and a system of “natural” coordinates can be based on these properties [3.2.3].

# 3.2.1 Level surfaces and plumb lines

The surfaces of constant gravity potential

$$
W = W ( { \bf r } ) = \mathrm { c o n s t . }
$$

are designated as equipotential or level surfaces (also geopotential surfaces) of gravity. As a result of an infi nitesimal displacement $d \mathbf { s } _ { i }$ , and in view of (3.43), the potential difference of differentially separated level surfaces (Fig. 3.7) is given by

$$
d W = \mathbf { g } \cdot d \pmb { \mathscr { s } } = g d s \cos ( \mathbf { g } , d \mathbf { s } ) .
$$

This means that the derivative of the gravity potential in a certain direction is equal to the component of gravity along this direction. Since only the projection of $d \mathbf { s }$ along the plumb line enters into (3.51), $d W$ is independent of the path. Hence, no work is necessary for a displacement along the level surface $W =$ const.: the level surfaces are equilibrium surfaces.

If ds is taken along the level surface $W = W _ { p \prime }$ then it follows from $d W = 0$ that $\cos ( \mathbf { g } , d \mathbf { s } ) = \cos 9 0 ^ { \circ } = 0$ : gravity is normal to $W = W _ { p } \mathrm { o r } ,$ in other words, the level surfaces are intersected at right angles by the plumb lines. The tangent to the plumb line is called the direction of the plumb line and has been defi ned already in [3.1.5]. If $d \mathbf { s }$ is directed along the outer surface normal n, then, because $\cos ( { \bf g } , { \bf n } ) = \cos 1 8 0 ^ { \circ } = { \bf \alpha } - 1$ , the following important differential relationship exists:

$$
d W = - g d n .
$$

It provides the link between the potential difference (a physical quantity) and the difference in height (a geometric quantity) of neighboring level surfaces. According to this relation, a combination of gravity measurements and (quasi) differential height determinations, as provided by geometric leveling, delivers gravity potential differences, cf. [5.5.4].

If $g$ varies on a level surface, then, according to (3.52), the distance dn to a neighboring level surface also changes. Therefore, the level surfaces are not parallel, and the plumb lines are space curves. As a consequence of the gravity increase of $0 . 0 5 ~ \mathsf { m } \mathsf { s } ^ { - 2 }$ from the equator to the poles, the level surfaces of the Earth converge toward the poles by $0 . 0 5 \dot { \mathsf { m s } } ^ { - 2 } / 9 . 8 \mathsf { m s } ^ { - 2 } ,$ , or $5 \times 1 0 ^ { - 3 } ,$ in a relative sense. For example, two level surfaces that are $1 0 0 . 0 \mathrm { m }$ apart at the equator are separated by only $9 9 . 5 ~ \mathrm { m }$ at the poles (Fig. 3.8).

![](images/be7e566dff828b0a93c0e3b4230f4c15fe47bb0bc911d541fcbca6226f13033d.jpg)  
Fig. 3.7: Neighboring level surfaces and plumb line.

![](images/0eb31825927af3b39f64b86172301d137f9c9f4b857dd5e28eb6018c3cc1ffd0.jpg)  
Fig. 3.8: Equipotential surfaces and plumb lines close to the Earth.

The level surfaces inside the Earth and in the exterior space are closed spheroidal surfaces. The geoid is the level surface that approximates mean sea level. Because of its importance as a reference surface for heights, it will be treated separately in [3.4]. As an outer limit in the realm of the defi nition of gravity, one may consider the level surface for which the gravitation and centrifugal acceleration in the equatorial plane cancel each other. The equatorial radius of this surface would be $4 2 \ 2 0 0 \ \mathrm { k m }$ .

The concept of the level surface was introduced by MacLaurin (1742), whereas Clairaut (1743) thoroughly discussed level surfaces and plumb lines as a whole. Bruns (1878) included the determination of the exterior level surfaces in their entirety in the fundamental problem of geodesy.

# 3.2.2 Local gravity fi eld representation

From the properties of the potential function $W = W ( \boldsymbol { \mathbf { r } } ) ,$ , it follows that the level surfaces which lie entirely in the exterior space are analytical surfaces; that is, they have no salient or singular points, cf. [3.1.5], and can be expanded in Taylor series. Level surfaces extending partially or completely inside the Earth exhibit discontinuities in the second derivatives where density jumps occur. These surfaces can thus be constructed from pieces of different analytical surfaces only. Local gravity fi eld observables are obtained with gravity meters and gravity gradiometers, they play an important role at high resolution gravity fi eld modeling (Baeschlin, 1948; Hofmann-Wellenhof and Moritz, 2005).

Using the local astronomic $x , y ,$ z-system introduced in [2.5], we develop the potential $W$ in the vicinity of the origin $P$ into a series. This local representation reads as

$$
\begin{array} { l } { { W = W _ { _ { P } } + W _ { _ { x } x } + W _ { _ { y } y } + W _ { _ { z } z } + \displaystyle \frac { 1 } { 2 } \left( W _ { _ { x x } } x ^ { 2 } + W _ { _ { y y } } y ^ { 2 } + W _ { _ { z z } } z ^ { 2 } \right) } } \\ { { \mathrm { } + W _ { _ { x y } } x y + W _ { _ { x z } } x z + W _ { _ { y z } } y z + \ldots } } \end{array}
$$

Here, $\begin{array} { r } { W _ { _ x } = { \partial W } / { \partial x } , W _ { _ x x } = { \partial ^ { 2 } W } / { \partial x ^ { 2 } } , W _ { _ x y } = { \partial ^ { 2 } W } / { \partial x \partial y } , } \end{array}$ etc. represent the fi rst and second order partial derivatives at $P$ in the local system. If the calculation point is located on the level surface through $P ,$ we have

$$
W = W _ { _ { P ^ { \prime } } } \ W _ { _ x } = W _ { _ y } = 0 , \ W _ { _ z } = - g .
$$

By solving for $Z ,$ we get the equation of the level surface in the neighborhood of $P$ :

$$
Z = \frac { 1 } { 2 g } \big ( W _ { x x } X ^ { 2 } + 2 W _ { x y } X y + W _ { y y } Y ^ { 2 } \big ) + \dots
$$

Here, we have neglected terms of third and higher order, taking into account that $Z$ is of second order compared to $x$ and $\scriptstyle \gamma ,$ due to the small curvature of the level surfaces.

The curvature of the level surface at $P$ along an azimuth $A$ is described by the curvature of the normal section (intersection of the vertical plane with the surface), which is called normal curvature. We now apply the well-known formula for the depression of a sphere (local approximation to the level surface) with respect to the horizontal $x , y .$ -plane

$$
Z = - \frac { s ^ { 2 } } { 2 R _ { A } } ,
$$

with distance $s$ from $P ,$ and radius of curvature $R _ { _ A }$ in the azimuth $A$ (Fig. 3.9). By introducing (3.55) into (3.54), and substituting $x , y$ with the local polar coordinates $s , A$

$$
x = s \cos A , \ y = s \sin A ,
$$

we obtain the normal curvature

$$
k = \frac { 1 } { R _ { _ A } } = - \frac { 1 } { g } \big ( W _ { _ { x x } } \mathrm { c o s } ^ { 2 } A + 2 W _ { _ { x y } } \mathrm { s i n } A \mathrm { c o s } A + W _ { _ { y y } } \mathrm { s i n } ^ { 2 } A \big ) .
$$

For the $x -$ and $\gamma$ -directions $A = 0 ^ { \circ }$ and $A = 9 0 ^ { \circ } .$ ), we obtain the curvatures

$$
k _ { x } = \frac { 1 } { R _ { x } } = - \frac { W _ { x x } } { g } , k _ { y } = \frac { 1 } { R _ { y } } = - \frac { W _ { y y } } { g } ,
$$

where $R _ { _ x }$ and $R _ { _ { y } }$ are the corresponding curvature radii. Analogously, the geodetic torsion in the direction of the meridian (expressing the change of direction normal to the meridian) is given by

$$
t _ { _ x } = - \frac { W _ { x y } } { g } .
$$

The normal curvature assumes its extreme values in the mutually perpendicular directions of principal curvature $A _ { \scriptscriptstyle { \mathit { 1 } } }$ and $A _ { _ 2 } = A _ { _ 1 } \pm 9 0 ^ { \circ }$ . By considering the extrema, we fi nd

$$
\tan 2 A _ { _ { 1 , 2 } } = 2 \frac { W _ { _ { x y } } } { W _ { _ { x x } } - W _ { _ { y y } } } .
$$

![](images/6ab0cebb47e4123a0c4ac6b280deb7290a8304da90e485281c0197e5e2cf2051.jpg)  
Fig. 3.9: Curvature of level surfaces and plumb lines.

Introducing (3.59) into (3.56) yields the corresponding principal curvatures

$$
\frac { 1 } { R _ { _ { A _ { _ { 1 } } } } } = \frac { 1 } { \cal { g } } ( W _ { _ { x x } } + W _ { _ { x y } } { \tan { A _ { 1 } } } ) , \frac { 1 } { R _ { _ { A _ { _ { 2 } } } } } = \frac { 1 } { \cal { g } } ( W _ { _ { y y } } + W _ { _ { x y } } { \cot { A _ { 2 } } } ) .
$$

With $\mathsf { A } _ { _ 2 } = \mathsf { A } _ { _ 1 } + 9 0 ^ { \circ }$ , the mean curvature of the level surface is given by

$$
J = \frac { 1 } { 2 } \big ( k _ { x } + k _ { y } \big ) = - \frac { 1 } { 2 g } \big ( W _ { x x } + W _ { y y } \big ) .
$$

Outside the masses of the Earth, the plumb lines can also be described analytically. In the local astronomic system, the equation of the plumb line is given by

$$
\begin{array} { r } { \boldsymbol { x } = \boldsymbol { x } ( s ) , \boldsymbol { y } = \boldsymbol { y } ( s ) , \boldsymbol { z } = \boldsymbol { z } ( s ) , } \end{array}
$$

where $s$ now is the arc length reckoned in the direction of gravity (Fig. 3.9). The line element along $s$ thus differs from gravity only by the “scale factor” g:

$$
\operatorname { g } { \left( \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right) } = { \left( \begin{array} { l } { W _ { x } } \\ { W _ { y } } \\ { W _ { z } } \end{array} \right) } ,
$$

with $x ^ { \prime } = d x / d s ,$ etc. The curvature vector of the plumb line lies in the principal normal through $P$ and thus in the horizontal plane. It reads as

$$
{ \binom { X ^ { \prime \prime } } { Y ^ { \prime \prime } } } = \kappa { \binom { \cos { A } } { 0 } } ,
$$

where $\kappa$ is the total curvature, and $A$ is the azimuth of the principal normal. Differentiating (3.63) with respect to $S _ { \prime }$ and considering that at $P \colon x ^ { \prime } = y ^ { \prime } = 0$ , $z ^ { \prime } = - 1$ , the substitution into (3.64) yields

$$
\kappa = - { \frac { W _ { _ { x z } } } { g \cos A } } = - { \frac { W _ { _ { y z } } } { g \sin A } }
$$

and

$$
A = \arctan \frac { W _ { y z } } { W _ { x z } } .
$$

The curvatures of the projections of the plumb line on the $x ,$ $Z \cdot$ -plane $( A = 0 ^ { \circ } ,$ ) and $\scriptstyle \gamma ,$ $Z$ -plane $( A = 9 0 ^ { \circ }$ ) follow from (3.65):

$$
\kappa _ { _ x } = - \frac { W _ { _ { x z } } } { g } , \kappa _ { _ y } = - \frac { W _ { _ { y z } } } { g } ,
$$

where

$$
\begin{array} { r } { \kappa = \sqrt { \kappa _ { x } ^ { 2 } + \kappa _ { y } ^ { 2 } } . } \end{array}
$$

From (3.56) to (3.67), we recognize that the curvatures of the level surfaces and the plumb lines depend on the second derivatives of the gravity potential. Consequently, they experience discontinuities at abrupt density changes, as discussed for the potential function, cf. [3.1.5].

The gravity gradient tensor (Eötvös tensor, also Marussi tensor) is comprised of the second derivatives of $W$ as follows:

$$
{ \mathrm { g r a d } } { \bf g } = { \mathrm { g r a d } } ( { \mathrm { g r a d } } W ) = { \left| \begin{array} { l l l } { W _ { x x } } & { W _ { x y } } & { W _ { x z } } \\ { W _ { y x } } & { W _ { y y } } & { W _ { y z } } \\ { W _ { z x } } & { W _ { z y } } & { W _ { z z } } \end{array} \right| } .
$$

With (3.57), (3.58), (3.67), and $W _ { z } = - g ,$ it can be transformed into the tensor

$$
- { \frac { 1 } { g } } \operatorname { g r a d } g = { \left| \begin{array} { l l l } { k _ { x } } & { t _ { x } } & { \kappa _ { x } } \\ { t _ { x } } & { k _ { y } } & { \kappa _ { y } } \\ { \kappa _ { x } } & { \kappa _ { y } } & { { \frac { 1 } { g } } { \frac { \partial g } { \partial z } } } \end{array} \right| } ,
$$

which completely describes the geometry of the gravity fi eld (Grafarend, 1986; Moritz and Hofmann-Wellenhof, 2005). As already stated in [3.1.5], (3.68) resp. (3.69) only contain fi ve independent elements.

The Eötvös tensor (3.68) includes the gravity gradient

$$
{ \mathrm { g r a d } } g = - { \left| \begin{array} { l l l } { W _ { x z } } \\ { W _ { y z } } \\ { W _ { z z } } \end{array} \right| } = { \left| \begin{array} { l l l } { \partial g / \partial x } \\ { \partial g / \partial y } \\ { \partial g / \partial z } \end{array} \right| } ,
$$

which describes the variation of gravity in the horizontal plane and in the vertical direction. The horizontal gradient is formed by the components $\partial g / \partial x$ and $\partial g / \partial \boldsymbol { y } ,$ and points in the direction of maximum gravity increase in the horizontal plane. The vertical component (often called vertical gradient) $\partial g / \partial z$ describes the gravity change with height. If we combine the generalized Poisson equation (3.48) with the mean curvature (3.61), we get

$$
\Delta W { = } W _ { x x } + W _ { y y } + W _ { z z } { = } { - } 2 g J - \frac { { \partial } g } { { \partial } z } { = } { - } 4 \pi G \rho + 2 { \omega } ^ { 2 }
$$

or

$$
\frac { \partial g } { \partial z } = - 2 g J + 4 \pi G \rho - 2 \omega ^ { 2 } .
$$

This relation was found by Bruns (1878). It connects the vertical gradient with the mean curvature of the level surface and offers a possibility to determine this curvature from gravity measurements, cf. [5.4.5].

# 3.2.3 Natural coordinates

We introduce a system of non-linear “natural” coordinates $\Phi$ , Λ, $W$ defi ned in the gravity fi eld. Astronomical latitude $\Phi$ and astronomical longitude $\Lambda$ describe the direction of the plumb line at the point $P .$ They have been introduced already in [2.5] as orientation parameters of the local gravity fi eld system with respect to the global geocentric system. The gravity potential $W$ locates $P$ in the system of level surfaces $W =$ const. (Fig. 2.12). Hence, $P$ is determined by the non-orthogonal intersection of the coordinate surfaces $\Phi = \mathrm { c o n s t } .$ , $\Lambda = \mathrm { c o n s t . }$ , and $W =$ const. The coordinate lines (spatial curves) are called astronomic meridian curve $\scriptstyle \left. { \Lambda , } \right.$ , $W =$ const.), astronomic parallel curve $( \Phi ,$ , $W =$ const.), and isozenithal line $( \Phi ,$ $\Lambda =$ const.).

The natural coordinates can be determined by measurements. Astronomic positioning provides latitude and longitude, cf. [5.3.2]. Although $W$ cannot be measured directly, potential differences can be derived from leveling and gravity measurements and then referred to a selected level surface, e.g., the geoid, cf. [5.5.4].

The relationship between the global $X , ~ Y ,$ $Z .$ -system and the $\Phi$ , Λ, $W ^ { \prime }$ system is obtained from (3.45):

$$
{ \bf g } = g r a d W = - g \left( \begin{array} { c } { { \cos \Phi \cos \Lambda } } \\ { { \cos \Phi \sin \Lambda } } \\ { { \sin \Phi } } \end{array} \right) .
$$

Solving for the natural coordinates yields the non-linear relations:

$$
\left. \begin{array} { l } { \displaystyle \Phi = \arctan \frac { - W _ { z } } { \sqrt { W _ { _ X } ^ { 2 } + W _ { _ Y } ^ { 2 } } } } \\ { \displaystyle \Lambda = \mathrm { a r c t a n } \frac { W _ { _ Y } } { W _ { _ X } } } \\ { \displaystyle W = W ( X , Y , Z ) } \end{array} \right\} .
$$

Differential relations between the local Cartesian coordinates $x , \ y , \ z$ (local astronomic system) and the global $\Phi ,$ , Λ, $W ^ { \prime }$ -system are given by

$$
d \Phi = \frac { \partial \Phi } { \partial x } d x + \frac { \partial \Phi } { \partial y } d y + \frac { \partial \Phi } { \partial z } d z , \mathrm { e t c . } ,
$$

where $d x , d y ,$ and $d z$ can be derived from local measurements, cf. [2.5].

The partial derivatives of $\Phi$ and $\Lambda$ describe the change of the plumb line direction when moving in the gravity fi eld. This corresponds to the curvature of the level surface (when moving in the horizontal plane) and of the plumb line (when moving vertically). We have the following relations:

$$
\begin{array} { r l } & { \displaystyle \frac { \partial \Phi } { \partial x } = k _ { x ^ { \prime } } \frac { \partial \Phi } { \partial y } = \frac { \cos \Phi \partial \Lambda } { \partial x } = t _ { x ^ { \prime } } \frac { \partial \Phi } { \partial Z } = \kappa _ { x } } \\ & { \displaystyle \frac { \cos \Phi \partial \Lambda } { \partial y } = k _ { y ^ { \prime } } \frac { \cos \Phi \partial \Lambda } { \partial z } = \kappa _ { y } } \\ & { \displaystyle \frac { \partial W } { \partial x } = 0 , \frac { \partial W } { \partial y } = 0 , \frac { \partial W } { \partial z } = - g , } \end{array}
$$

where the curvature and torsion parameters are given by (3.57), (3.58), and (3.67). Introducing (3.74) into the differential relations leads to the transformation

$$
{ \binom { d \Phi } { d W } } = { \binom { k _ { x } t _ { x } \kappa _ { x } } { t _ { x } \ k _ { y } \kappa _ { y } } } { \binom { d x } { d y } } ,
$$

which again contains the elements of the Eötvös tensor (3.69), see Grafarend (1975), Moritz and Hofmann-Wellenhof (1993).

As the orientation of the local systems changes from point to point, the differentials $d x ,$ dy, $d z$ are imperfect ones (i.e., they are not the differential of a function of position only), with loop closures differing from zero:

$$
\oint d x \neq 0 , \oint d y \neq 0 , \oint d z \neq 0 .
$$

$\Phi , \Lambda , W ,$ on the other hand, possess perfect differentials with

$$
\oint d \Phi = 0 , \oint d \Lambda = 0 , \oint d W = 0 .
$$

Equation (3.75) offers the possibility to transform local observable quantities (azimuths, horizontal directions and angles, zenith angles, distances, potential differences from leveling and gravity) to the global system of “natural” coordinates, where the astronomic latitude and longitude coordinates are also observables.

A theory of “intrinsic geodesy” based on the differential geometry of the gravity fi eld has been developed by Marussi (1949, 1985), see also Hotine (1969). Using only observable quantities, reductions to conventional reference systems are completely avoided. On the other hand, in order to practically evaluate (3.75), a detailed knowledge of the curvature of the gravity fi eld would be necessary. This would require a dense survey of the second derivatives of the gravity potential, as the curvature close to the Earth’s surface is rather irregular. Present gravity models already provide this information for the long- and medium-wave part of the gravity fi eld, but a high- resolution would require costly and time consuming terrestrial techniques, cf. [5.2.8], [5.4.5]. Yet even with a better knowledge of the curvature of the gravity fi eld, the transfer of coordinates would hardly be made in the system of natural coordinates, due to the complex structure of the gravity fi eld, and the success of Cartesian coordinate systems based on space geodetic methods, cf. [2.4].

# 3.3 Spherical harmonic expansion of the gravitational potential

Because the density function $\rho = \rho ( { \bf r } ^ { \prime } )$ of the Earth is not suffi ciently known, the gravitational potential $V = V ( \mathbf { r } )$ cannot be computed by Newton’s law of gravitation using (3.10). However, a convergent series expansion of $V$ is possible in the exterior space of the Earth as a special solution of Laplace’s differential equation (3.29). It can be easily derived from an expansion of the reciprocal distance appearing in Newton’s law [3.3.1], [3.3.2], e.g., Hobson (1965), Sigl (1985), Blakeley (1996). This solution corresponds to a spectral decomposition of the gravitational fi eld [3.3.3]. The coeffi cients of the series expansion provide the amplitudes of the respective spectral parts [3.3.4]. Any observable functional of $V$ can be evaluated for the determination of these coeffi cients, thus allowing a global analytical representation of the gravitational fi eld, cf. [6.6.1].

# 3.3.1 Expansion of the reciprocal distance

Applying the law of cosines to the triangle $O P ^ { \prime } P$ (Fig. 3.1), we obtain

$$
\frac { 1 } { I } = \left( r ^ { 2 } + r ^ { \prime 2 } - 2 r r ^ { \prime } \cos \psi \right) ^ { - \frac { 1 } { 2 } } = \frac { 1 } { r } \bigg ( 1 + \bigg ( \frac { r ^ { \prime } } { r } \bigg ) ^ { 2 } - 2 \frac { r ^ { \prime } } { r } \cos \psi \bigg ) ^ { - \frac { 1 } { 2 } }
$$

for the reciprocal distance $1 / I$ appearing in (3.10), between the attracted point $P$ and the attracting point $P ^ { \prime }$ . Here, $\psi$ is the central angle between the directions from $O$ to $P$ and $O$ to $P ^ { \prime } { } _ { , }$ respectively. If $1 / I$ is expanded in a series converging for $r ^ { \prime } < r ,$ and if the terms are arranged according to increasing powers of $r ^ { \prime } / r ,$ then it follows

$$
\frac { 1 } { I } = \frac { 1 } { r } \sum _ { I = 0 } ^ { \infty } \left( \frac { r ^ { \prime } } { r } \right) ^ { I } P _ { _ I } \left( \cos \psi \right) .
$$

The $P _ { \mu } ( \cos \psi )$ terms represent polynomials of $I ^ { \mathrm { t h } }$ degree in $\cos \psi .$ They are known as Legendre polynomials (zonal harmonics), and they are computed for the argument $t = \cos \psi$ by means of

$$
P _ { \ I } ( t ) = \frac { 1 } { 2 ^ { I } I ! } \frac { d ^ { I } } { d t ^ { I } } ( t ^ { 2 } - 1 ) ^ { I } .
$$

A rapid calculation is possible with the recurrence formula (Wenzel, 1985)

$$
P _ { _ { I } } ( t ) = \frac { 2 I - 1 } { I } t P _ { _ { I - 1 } } ( t ) - \frac { I - 1 } { I } P _ { _ { I - 2 } } ( t ) , I \geq 2 ,
$$

with $P _ { \mathrm { 0 } } = 1 , P _ { \mathrm { 1 } } = t .$

We now introduce the unit sphere $\sigma$ around the origin of the coordinates $O$ (Fig. 3.10). The projections of $O P$ and $O P ^ { \prime }$ on $\sigma ,$ together with the north pole projection $N ,$ form a spherical triangle. It contains the spherical coordinates $\vartheta , \lambda$

![](images/fc61f30f5f1834ca7e5bc3ca42087602850ba580db3c6dae5e0c351921566c97.jpg)  
Fig. 3.10: Spherical polar triangle on the unit sphere, spherical coordinates.

and $\vartheta , \lambda ^ { \prime } ,$ , and the central angle $\psi$ appears as a spherical distance on $\sigma ,$ see also [2.3.3]. Spherical trigonometry provides the following relationship

$$
\cos \psi = \cos \vartheta \cos \vartheta + \sin \vartheta \sin \vartheta \cos ( \lambda ^ { \prime } - \lambda ) .
$$

The corresponding decomposition of $P _ { \ / } ( \cos \psi )$ leads to

$$
\begin{array} { l } { { P _ { \mathit { I } } ( \cos \psi ) = P _ { \mathit { I } } ( \cos \vartheta ) P _ { \mathit { I } } ( \cos \vartheta ^ { \prime } ) } } \\ { { \displaystyle ~ + 2 \sum _ { m = 1 } ^ { \prime } \frac { ( I - m ) ! } { ( I + m ) ! } ( P _ { \mathit { I m } } ( \cos \vartheta ) \cos m \lambda P _ { \mathit { I m } } ( \cos \vartheta ^ { \prime } ) \cos m \lambda ^ { \prime } } } \\ { { \displaystyle ~ + P _ { \mathit { I m } } ( \cos \vartheta ) \sin m \lambda P _ { \mathit { I m } } ( \cos \vartheta ^ { \prime } ) \sin m \lambda ^ { \prime } ) . } } \end{array}
$$

Again, the $P _ { I } ( t )$ are the Legendre polynomials with the argument $t = \cos \vartheta$ or $t = \cos \vartheta$ . The associated Legendre functions of the fi rst kind, $P _ { l m } ( t )$ (degree $I$ and order $m _ { \ l }$ , are obtained by differentiating $P _ { I } ( t )$ $m$ times with respect to $t$ :

$$
P _ { _ { I m } } ( t ) = ( 1 - t ^ { 2 } ) ^ { \frac { m } { 2 } } \frac { d ^ { m } } { d t ^ { m } } P _ { _ { I } } ( t ) .
$$

Up to degree 3, the Legendre polynomials and the associated Legendre functions are given as follows:

$$
P _ { \circ } = 1 , P _ { \scriptscriptstyle 1 } = \cos \vartheta , P _ { \scriptscriptstyle 2 } = \frac { 3 } { 2 } \mathrm { c o s } ^ { 2 } \vartheta - \frac { 1 } { 2 } , P _ { \scriptscriptstyle 3 } = \frac { 5 } { 2 } \mathrm { c o s } ^ { 3 } \vartheta - \frac { 3 } { 2 } \mathrm { c o s } \vartheta
$$

and

$$
\begin{array} { r l } & { P _ { _ { 1 , 1 } } = \sin \vartheta , P _ { _ { 2 , 1 } } = 3 \sin \vartheta \cos \vartheta , P _ { _ { 2 , 2 } } = 3 \sin ^ { 2 } \vartheta } \\ & { P _ { _ { 3 , 1 } } = \sin \vartheta \Big ( \displaystyle \frac { 1 5 } { 2 } \cos ^ { 2 } \vartheta - \displaystyle \frac { 3 } { 2 } \Big ) , P _ { _ { 3 , 2 } } = 1 5 \sin ^ { 2 } \vartheta \cos \vartheta , P _ { _ { 3 , 3 } } = 1 5 \sin ^ { 3 } \vartheta \Big ) . } \end{array}
$$

A series development for the calculation of $P _ { \ I m } ( t )$ is given in Hofmann-Wellenhof and Moritz (2005, p. 17). By substituting (3.81) into (3.79), the expansion of $1 / I$ into spherical harmonics is completed.

The functions

$$
\begin{array} { r } { Y _ { _ { I m } } ^ { c } ( \vartheta , \lambda ) = P _ { _ { I m } } ( \cos { \vartheta } ) \cos { m \lambda } } \\ { Y _ { _ { I m } } ^ { s } ( \vartheta , \lambda ) = P _ { _ { I m } } ( \cos { \vartheta } ) \sin { m \lambda } \vphantom { \vartheta } \} ^ { \prime } } \end{array}
$$

contained in (3.81), are called Laplace’s surface spherical harmonics. They characterize the behavior of the developed function (here $1 / \Lambda$ on the unit sphere, cf. [3.3.3]. The orthogonality relations are valid for these functions, i.e., the integral over the unit sphere of the product of any two different functions is zero:

$$
\iint { Y _ { I m } ^ { i } Y _ { n q } ^ { k } d \sigma } = 0
$$

for $n \neq l , q \neq m ,$ or $k \neq i .$ For the product of two equal functions $Y _ { _ { I m } } ^ { c }$ or $Y _ { _ { I m ^ { \prime } } } ^ { s }$ we have

$$
\begin{array}{c} \int \int Y _ { _ { \sigma } } ^ { 2 } d \sigma = \left\{ \frac { 4 \pi } { 2 I + 1 } \mathrm { f o r } m = 0 \right.  \\ { \frac { 2 \pi ( I + m ) ! } { ( 2 I + 1 ) ( I - m ) ! } \quad \mathrm { f o r } m \neq 0 , } \end{array}
$$

see Hofmann-Wellenhof and Moritz (2005, p. 21).

# 3.3.2 Expansion of the gravitational potential

We substitute the spherical harmonic expansion of 1/l, (3.79) and (3.81), into the volume integral (3.10):

$$
\begin{array} { l } { { \displaystyle V = \frac { G } { r } \sum _ { l = 0 } ^ { \infty } \sum _ { m = 0 } ^ { l } \frac { k ( l - m ) ! } { ( l + m ) ! } } \ ~ } \\ { { \displaystyle ~ \times \ \frac { 1 } { r ^ { l } } ( P _ { l m } ( \cos \vartheta ) \cos m \frac { \chi [ \displaystyle \int ] \int _ { r ^ { \prime } P _ { l m } } ( \cos \vartheta ^ { \prime } ) \cos m \lambda ^ { \prime } d m } { \cosh \cosh \cosh \cosh \cosh \cosh \big [ \displaystyle \int _ { r ^ { \prime } P _ { l m } } ( \cos \vartheta ^ { \prime } ) \sin m \lambda ^ { \prime } d m \big ] } ) } , } \\ { { \displaystyle ~ k = \{ 1 \ \mathrm { f o r } \ m = 0 \ } \ ~ } \\ { { \displaystyle 2 \ \mathrm { f o r } \ m \neq 0 \ } } \end{array}
$$

In abbreviated form this development can be expressed as

$$
V = \sum _ { I = 0 } ^ { \infty } V _ { I } = \sum _ { I = 0 } ^ { \infty } \frac { Y _ { I } ( \vartheta , \lambda ) } { r ^ { I + 1 } } ,
$$

where the $V _ { \scriptscriptstyle I }$ are called solid spherical harmonics, they are linear combinations of the surface spherical harmonics (3.84).

For $I = 0$ , the integration yields the potential of the Earth’s mass $M$ concentrated at the center of mass (3.16). We extract this term, introduce the semi-major axis a of the Earth ellipsoid as a constant “scale factor”, and denote the mass integrals by $C _ { { \scriptscriptstyle I m } ^ { \prime } }$ $S _ { \jmath _ { m } }$ (spherical harmonic coeffi cients). The gravitational potential expanded in spherical harmonics can then be written as

$$
V = \frac { G M } { r } \left( 1 + \sum _ { l = 1 } ^ { \infty } \sum _ { m = 0 } ^ { l } \Bigl ( \frac { a } { r } \Bigr ) ^ { l } \left( C _ { l m } { \cos } m \lambda + S _ { l m } { \sin } m \lambda \right) P _ { l m } \left( { \cos } \vartheta \right) \right) .
$$

The harmonic coeffi cients (also Stokes’ coeffi cients) are given by

$$
\begin{array}{c} \begin{array} { l } { { C _ { l 0 } = C _ { l } = \displaystyle \frac { 1 } { M } \left[ \displaystyle \int \int \left( \frac { r ^ { \prime } } { a } \right) ^ { l } P _ { l } \left( \cos \vartheta \right) d m \mathrm { \ f o r \ } m = 0 \mathrm { \ a n d } \right. } } \\ { { \left. \left. C _ { l m } \right. = \displaystyle \frac { 2 } { M } \displaystyle \frac { \left( I - m \right) ! } { \left( I + m \right) ! } \displaystyle \iint \left[ \displaystyle \frac { r ^ { \prime } } { a } \right] ^ { l } P _ { l m } \left( \cos \vartheta \right) \left. \displaystyle \cos m \lambda ^ { \prime } \right. d m \mathrm { \ f o r \ } m \neq 0 \right.} } \end{array}  .   \end{array}
$$

The following denotations are also used, particularly in satellite geodesy:

$$
J _ { _ { I } } = - \ C _ { _ { I ^ { \prime } } } \ J _ { _ { I m } } = - \ C _ { _ { I m ^ { \prime } } } \ K _ { _ { I m } } = - \ S _ { _ { I m } } .
$$

Calculations in the gravitational fi eld become more convenient with the (fully) nor-__ malized spherical harmonic functions $\overline { { P } } _ { l m } \left( \cos \vartheta \right)$ . They are computed from the conventional harmonics, (3.80) and (3.82), according to

$$
\bar { P } _ { _ { I m } } ( t ) = \sqrt { k ( 2 I + 1 ) \frac { ( I - m ) ! } { ( I + m ) ! } } ~ P _ { _ { I m } } ( t ) , \ k = \left\{ \begin{array} { l l } { { 1 \mathrm { ~ f o r ~ } m = 0 } } \\ { { 2 \mathrm { ~ f o r ~ } m \ne 0 } } \end{array} \right. ,
$$

with $t = \cos \vartheta ,$ etc. Recursive formulas are also available for the calculation of the normalized harmonics and its derivatives (Paul, 1978; Tscherning et al., 1983; Wenzel, 1985):

$$
\begin{array} { l } { \displaystyle \overline { { P } } _ { I m } ( t ) = \bigg [ \frac { \left( 2 I + 1 \right) \left( 2 I - 1 \right) } { \left( I + m \right) \left( I - m \right) } \bigg ] ^ { \frac { 1 } { 2 } } t \overline { { P } } _ { I - 1 , m } ( t ) - } \\ { \displaystyle \qquad \left[ \frac { \left( 2 I + 1 \right) \left( I + m - 1 \right) \left( I - m - 1 \right) } { \left( 2 I - 3 \right) \left( I + m \right) \left( I - m \right) } \right] ^ { \frac { 1 } { 2 } } \overline { { P } } _ { I - 2 , m } ( t ) } \end{array}
$$

with

for $I > m + 1$

$$
\begin{array} { r l } & { \displaystyle \overline { { P } } _ { 0 } = 1 , \ : \overline { { P } } _ { 1 } = \sqrt { 3 } \cos \vartheta , \ : \overline { { P } } _ { 2 } = \frac { 1 } { 2 } \sqrt { 5 } \big ( 3 \cos ^ { 2 } \vartheta - 1 \big ) , } \\ & { \displaystyle \overline { { P } } _ { 1 , 1 } = \sqrt { 3 } \sin \vartheta , \ : \overline { { P } } _ { 2 , 1 } = \sqrt { 1 5 } \sin \vartheta \cos \vartheta , \ : \overline { { P } } _ { 2 , 2 } = \frac { 1 } { 2 } \sqrt { 1 5 } \sin ^ { 2 } \vartheta } \end{array}
$$

and the control formula

$$
\sum _ { m = 0 } ^ { I } \bar { P } _ { _ { I m } } ( t ) ^ { 2 } = 2 I + 1 .
$$

In addition to the orthogonality relations (3.85), (3.86) for the surface harmonics, we now also have

$$
\frac { 1 } { 4 \pi } \int \limits _ { \sigma } \left( \hat { P } _ { _ { I m } } \left\{ \cos { m \lambda } \right\} \right) ^ { 2 } d \sigma = 1
$$

over the unit sphere $\sigma .$ According to (3.92), for an expansion of the gravitational potential analogous to (3.89), the harmonic coeffi cients are now given by

$$
\left\{ \overline { { { C } } } _ { I m } \right\} = \sqrt { \frac { ( I + m ) ! } { k ( 2 I + 1 ) ( I - m ) ! } } \left\{ C _ { I m } \right\} , k = \left\{ 1 \mathrm { ~ f o r ~ } m = 0 \right. \nonumber
$$

Equation (3.89), or the corresponding equations employing fully normalized harmonics (3.92) and (3.95), represent spherical solutions of Laplace’s differential equation (3.29). These solutions can also be derived straightforwardly by the method of variable separation, after substituting the Cartesian coordinates with spherical coordinates (Hofmann-Wellenhof and Moritz, 2005, p. 9 ff.).

The expansion converges outside a sphere of radius $r = a ,$ , which just encloses the Earth (Brillouin sphere). After the theorem of Runge-Krarup, an expansion of $V$ into converging spherical harmonics can also be used in the interior of the Earth, down to a sphere completely inside the Earth and close to its surface (Bjerhammar sphere ), Krarup (1969), Moritz (1980, p. 69). Such an expansion represents an analytical continuation of the outer gravitational fi eld model into the Earth’s interior, with arbitrarily good approximation to the outer fi eld. Naturally, this extension does not satisfy the Poisson equation (3.31) which governs the actual gravitational fi eld in the Earth’s interior.

With present accuracies of the determination of the Earth’s gravity fi eld, the gravitation of the atmosphere cannot be neglected. As the density of the atmosphere primarily depends on height, corresponding models can be used to calculate the potential and the gravitation of the atmosphere as a function of height. These calculations are based on the relations derived for the potential inside an Earth constructed of homogeneous spherical shells, cf. [3.1.2]. With an atmospheric mass of about $5 . 3 2 \times 1 0 ^ { 1 8 } ~ \mathrm { k g } ,$ we get a potential value of $5 5 . 6 \ \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 2 }$ for $h = 0$ , and $5 4 . 8 ~ \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 2 }$ for $h = 1 0 0 ~ { \mathrm { k m } }$ . This effect is taken into account by corresponding reductions, cf. [4.3].

The extension of the spherical harmonic expansion for $V$ to the gravity potential $W$ is performed easily by adding the centrifugal potential $Z ( 3 . 3 8 )$ . If we express the distance $p$ to the rotational axis by spherical coordinates (2.14), the centrifugal potential reads as

$$
Z = { \frac { \omega ^ { 2 } } { 2 } } r ^ { 2 } \sin ^ { 2 } \vartheta
$$

or, after introducing the Legendre polynomial $P _ { _ 2 }$ according to (3.83a), as

$$
Z = { \frac { \omega ^ { 2 } } { 3 } } r ^ { 2 } \big ( 1 - P _ { _ { 2 } } \left( \cos { \vartheta } \right) \big ) .
$$

By adding (3.96) to (3.89) we get the expansion for the gravity potential.

# 3.3.3 Geometrical interpretation of the surface spherical harmonics

We now discuss the properties of the surface spherical harmonics (3.84), which describe the behavior of the gravitational potential on the unit sphere. The zero points of these functions divide the surface into regions with alternating signs, bounded by meridians and parallels.

For the order $m = 0 ,$ , we obtain the Legendre polynomials $P _ { _ { I } } \left( \cos \vartheta \right)$ . Because of their independence of the geographical longitude $\lambda ,$ they divide the surface into zones of positive and negative signs: zonal harmonics. These harmonics possess $I$ real zeros in the interval $0 \leq \vartheta \leq \pi .$ For even $I ,$ the sphere is divided symmetrically with respect to the equator $\vartheta = 9 0 ^ { \circ }$ , and the case for odd $I$ results in an asymmetric division. The $P _ { _ { I m } } \left( \cos \vartheta \right)$ for $m \neq 0$ have $( I - m )$ zeros in the interval $0 < \vartheta < \pi .$ Because of the multiplication by $\cos m \lambda$ or $\sin m \lambda ,$ the surface harmonics are longitude dependent, furnishing $2 m$ zeros in the interval $0 \leq \lambda \leq \pi .$ tesseral harmonics (tessera means a square or rectangle). Finally, for $m = 1 ,$ , the dependence on $\vartheta$ disappears, and the sphere is divided into sectors of alternating signs: sectorial harmonics (Fig. 3.11).

![](images/17e241bf572399698a365acff59f15637da86135910c9fcdf8fceb2a1f24b4e5.jpg)  
Fig. 3.11: Spherical harmonics on the unit sphere, with alternating positive (gray) and negative (white) sign.

The amplitudes of the individual terms given by the surface harmonics are determined by the harmonic coeffi cients. For example, the series has only zonal harmonics for an Earth rotationally symmetric with respect to the $Z .$ -axis; the coeffi cients with $m \neq 0$ must all vanish. For a mass distribution symmetric with respect to the equator, the zonal harmonic coeffi cients with odd l must be absent.

Summarizing, we state that the spherical harmonic expansion of the gravitational potential represents a spectral decomposition of the gravitational fi eld. The fi eld is separated into structures of wavelength $3 6 0 ^ { \circ } / I ,$ corresponding to a spatial resolution of $1 8 0 ^ { \circ } / I .$ With increasing height, the fi eld is smoothed by the factor $( \dot { a } / r ) _ { , } ^ { I }$ see (3.89) and the examples in [6.7.3].

# 3.3.4 Physical interpretation of the spherical harmonic coeffi cients

The spherical harmonic expansion has transformed the single volume integral over the Earth’s masses (3.10) into an infi nite series. The harmonic coeffi cients now carry mass integrals for the individual contribution of the corresponding wavelength to the total potential. The lower degree harmonics have a simple physical interpretation.

As already stated above, the zero degree term $( I = 0$ ) represents the potential of a homogeneous or radially layered spherical Earth, see (3.16):

$$
V _ { _ { 0 } } = { \frac { G M } { r } } .
$$

The terms of degree one and two $( I = 1 , 2 )$ ) can be calculated from (3.90) by introducing the harmonic functions ${ P _ { \mathrm { \it I m } } } ( 3 . 8 3 )$ and subsequently transforming the spherical coordinates to Cartesian coordinates using (2.14). For $| = 1$ , this yields

$$
C _ { 1 } = { \frac { 1 } { a M } } \iiint _ { \mathrm { \tiny ~ E a r t h } } ^ { \prime } { \cal Z } ^ { \prime } d m , C _ { _ { 1 , 1 } } = { \frac { 1 } { a M } } \iiint _ { \mathrm { \tiny ~ E a r t h } } ^ { \prime } \ [ X ^ { \prime } d m , { \mathrm { a n d } } S _ { _ { 1 , 1 } } = { \frac { 1 } { a M } } \iiint _ { \mathrm { \tiny ~ E a r t h } } Y ^ { \prime } d m .
$$

As known from mechanics, the integrals divided by the mass $M$ are the coordinates of the center of mass of the Earth. Since we have placed the origin of the coordinate system at the center of mass, we have

$$
C _ { 1 } = C _ { 1 , 1 } = S _ { 1 , 1 } = 0 .
$$

For $I = 2$ , we obtain

$$
\begin{array} { r l } & { C _ { 2 } = \frac { 1 } {  { \frac { d ^ { 2 } } { 2 } } M _ { \mathrm { t o r s f } } ^ { 2 } } \iiint \left[ \mathcal { Z } ^ { 2 } - \frac { X ^ { \prime } + Y ^ { 2 } } { 2 } \right] d m _ { r } } \\ & { C _ { 2 , 1 } = \frac { 1 } {  { \frac { d ^ { 2 } } { 2 } } M _ { \mathrm { t o r s f } } ^ { 2 } } \iiint X \mathcal { Z } d m _ { r } } \\ & { S _ { 3 , 1 } = \frac { 1 } {  { \frac { d ^ { 2 } } { d ^ { 2 } } } M _ { \mathrm { t o r s f } } ^ { 2 } } \iiint Y \mathcal { Z } d m _ { r } } \\ & { C _ { 2 , 2 } = \frac { 1 } { 4  { \frac { d ^ { 2 } } { d ^ { 2 } } } M _ { \mathrm { t o r s f } } ^ { 2 } } \iiint ( X ^ { 2 } - Y ^ { 2 } ) d m _ { r } } \\ & { S _ { 3 , 2 } = \frac { 1 } { 2  { \frac { d ^ { 2 } } { d ^ { 2 } } } M _ { \mathrm { t o r s f } } ^ { 2 } } \iiint X Y ^ { \prime } d m _ { r } . } \end{array}
$$

These expressions are functions of the moments of inertia

$$
\begin{array} { l } { { A = \displaystyle \int \int \int ( \gamma ^ { \prime 2 } + Z ^ { \prime 2 } ) d m , B = \displaystyle \int \int \int ( X ^ { \prime 2 } + Z ^ { 2 } ) d m , } } \\ { { C = \displaystyle \int \int \int ( X ^ { \prime 2 } + Y ^ { \prime 2 } ) d m } } \end{array}
$$

and of the products of inertia

$$
D = \iiint Y ^ { \prime } Z ^ { \prime } d m , \ E = \iiint X ^ { \prime } Z ^ { \prime } d m , \ F = \iiint X ^ { \prime } Y ^ { \prime } d m
$$

with respect to the axes of the global $X , ~ Y , ~ Z \cdot$ system. If we neglect polar motion, the $Z .$ -axis coincides with one principal axis of inertia (maximum moment of inertia). Consequently, we have

$$
D = E = 0 .
$$

$F ,$ on the other hand, would only become zero if the $\chi .$ -axis coincided with one of the equatorial principal axes of inertia. Due to the conventional defi nition of the $\chi$ -axis (Greenwich meridian), $F$ therefore does not vanish.

Using the above expressions for $A , B , C ,$ and $F ,$ the harmonic coeffi cients of second degree may also be formulated as follows:

$$
\begin{array} { l } { { C _ { \scriptscriptstyle 2 } = \displaystyle \frac { 1 } { a ^ { 2 } M } \bigg ( \frac { A + B } { 2 } - C \bigg ) , ~ C _ { _ { 2 , 1 } } = S _ { _ { 2 , 1 } } = 0 , } } \\ { { C _ { _ { 2 , 2 } } = \displaystyle \frac { B - A } { 4 a ^ { 2 } M } , ~ S _ { _ { 2 , 2 } } = \frac { F } { 2 a ^ { 2 } M } . } } \end{array}
$$

$J _ { { \scriptscriptstyle 2 } } = - C _ { { \scriptscriptstyle 2 } }$ is also known as dynamical form factor. It characterizes the polar fl attening of the Earth’s body by the difference between the mean equatorial moment of inertia (with $A \approx B ,$ ) and the polar moment of inertia. As this is the largest deviation from a spherical Earth model, the numerical value for $C _ { 2 }$ is three orders of magnitude larger than the values of the successive coeffi cients. Slight contributions to the ellipsoidal form of the Earth also come from the even zonal harmonics of higher degree, mainly $I = 4$ and $I = 6$ . The coeffi cients $C _ { 2 , 2 }$ and $S _ { 2 , 2 }$ describe the asymmetry of the equatorial mass distribution in relation to the rotational axis (ellipticity or fl attening of the equator) and the torsion of the corresponding principal axes of inertia with respect to the conventional $X _ { - }$ and Y-directions. The values obtained for these coeffi cients have been used for the computation of three-axial ellipsoids, cf. [4.2.1]. If the odd zonal harmonic-coeffi cients differ from zero, the corresponding terms in the expansion of $V$ represent an asymmetric mass distribution with respect to the equatorial plane, cf. [3.3.3]. The main contribution comes from $C _ { _ { 3 ^ { \prime } } }$ and may be geometrically interpreted as a difference in the fl attening for the northern and the southern hemisphere (a “pear-shaped” Earth’s fi gure). Numerical values for the coeffi cients are given in [6.6.2], and actual values for the derived physical quantities of the Earth will be found in [8.1].

By introducing the coeffi cients $C _ { _ { 1 , 0 ^ { \prime } } } \ C _ { _ { 1 , 1 ^ { \prime } } } \ S _ { _ { 1 , 1 ^ { \prime } } }$ and $C _ { 2 , 1 ^ { \prime } }$ $S _ { 2 , 1 }$ as unknowns into the adjustment of satellite orbit observations, (small) deviations of the Earth’s center of mass (geocenter variations) and the polar axis of inertia from the geocentric coordinate system (polar motion) can be detected. This is of importance for the investigation of temporal variations of the Earth’s body.

# 3.4 The geoid

The geoid is of fundamental importance for geodesy, oceanography, and physics of the solid Earth. Due to the present-day demands on accuracy and resolution, the classical defi nition of the geoid must be reconsidered [3.4.1]. In geodesy and oceanography, the geoid serves as a height reference surface for describing continental and sea surface topography [3.4.2], [3.4.3]. Solid Earth physics exploits the geoid as a gravity fi eld representation revealing the distribution of deeper located masses, cf. [8.2.4].

# 3.4.1 Defi nition

The geoid has already been introduced in [1.2] as a refi ned model of the fi gure of the Earth. Defi ned in 1828 by Gauss as the “equipotential surface of the Earth’s gravity fi eld coinciding with the mean sea level of the oceans”, the name “geoid” was only given in 1873 by Listing.

This physical defi nition considers the waters of the oceans as freely-moving homogeneous matter, subject only to the force of gravity and free from variations with time (as ocean tides and time-variable ocean currents). Upon attaining a state of equilibrium, the surface of such idealized oceans would assume a level surface of the gravity fi eld. This ocean surface may be regarded as being extended under the continents, e.g., by a system of conducting tubes, and will then represent a global realization of the geoid.

With the gravity potential value $\boldsymbol { W } _ { 0 ^ { \prime } }$ the equation of the geoid reads as

$$
W = W ( { \boldsymbol { \mathbf { r } } } ) = W _ { 0 } .
$$

It follows from the properties of the gravity potential $W ,$ that the geoid is a closed and continuous surface, cf. [3.1.3]. As it extends partially inside the solid Earth (under the continents), its curvature will display discontinuities at abrupt density changes. Nevertheless, although not being an analytical surface in a global sense, it may be suffi ciently well approximated by a spherical harmonic development, cf. [3.3.2]. With respect to a best-fi tting reference ellipsoid, cf. [4.3], the geoid r.m.s. deviation amounts to $\pm 3 0 \textrm { m }$ ; maximum deviations (geoid heights, also geoid undulations) reach about $\pm 1 0 0 \mathrm { ~ m ~ }$ . The large-scale structures (resolution of about $5 0 0 ~ \mathrm { k m } )$ ) of the geoid (geoid heights above a geocentric reference ellipsoid) are shown in Fig. 3.12, for more detailed information see [6.6.3].

The problem of downward continuation of the gravity fi eld into the Earth’s masses presupposes knowledge about the density distribution of the atmospheric and topographic masses. Geoid calculations consequently depend on the corresponding assumptions (Strykowski, 1998), cf. [6.5.3].

As is well known from oceanography, mean sea level is not an equilibrium surface in the Earth’s gravity fi eld, due to ocean currents and other quasi-stationary effects. In addition, sea level experiences a variety of temporal variations, which cover a wide spectrum. They can be only partially reduced by averaging over time or by modeling. Hence, mean sea level still varies over longer time spans, and a geoid defi nition has to refer to a certain epoch of mean sea level, cf. [3.4.2], [8.3.3], Bosch (2001b).

The geoid as gravity fi eld quantity naturally also is affected by variations with time, and has to be regarded as a time-dependent quantity. We distinguish between the gravimetric tidal effects [3.5.2], and the gravity changes which result from displacements of terrestrial masses [3.5.3], [8.3.5]. The corresponding geoid changes remain at the order of mm/year, but may reach the centimeter order of magnitude over several years. The defi nition of a “cm-geoid” has to take this time-dependence into account.

![](images/08a2208747a301add6cfd360feed90369d384c8e7f6610eaa6ce0459fa777594.jpg)  
Fig. 3.12: Large scale geoid structures: EGM96 spherical harmonic expansion truncated at degree and order 36, contour line interval $5 \textrm { m }$ (after Lemoine et al., 1998).

The gravimetric tides require special consideration. While the periodic part can be modeled to a high degree of accuracy, the treatment of the permanent tidal deformation enters into the defi nition of the geoid. This effect results from the fact that the mean value (time average) of the zonal tide of degree two is not zero, cf. (3.122). There are three different defi nitions possible. The mean geoid includes the direct effect of attraction and the indirect effect of deformation caused by extraterrestrial bodies (mean tidal system). It would coincide with an “undisturbed” mean ocean surface; hence it is of interest for oceanography. For the non-tidal geoid, the total tidal-effect would be eliminated (tide-free system). This would agree with the theoretical demand of geodesy to have no masses outside the boundary surface “geoid”, cf. [6.5.3], but would signifi cantly change the shape of the Earth, and consequently the tide-free system is not acceptable from the geophysical point of view. As the response of the Earth to the permanent tidal part (the indirect effect) is not known, the zero-tide-geoid is preferred in geodesy (zero tidal system). Here, the attraction part is eliminated but the permanent deformation retained. This defi nition takes into account the fact that positioning also refers to a tidal-deformed Earth (IAG resolution, General Assembly Hamburg 1983; Rapp, 1983; Ekman, 1989).

In practice, geodetic products may refer to different tidal reductions. The zero tidal system is well established in gravimetry, while three-dimensional reference coordinates generally are given in a conventional tide-free system, and an interdisciplinary approach with oceanography would require the mean tidal system. Careful studies and reductions to a common standard are therefore required at combination solutions (Mäkinen and Ihde, 2009).

Consequently, a refi ned geoid defi nition is needed at the $^ { \prime \prime } { \mathrm { C } } { \sf m } ^ { \prime \prime }$ accuracy level (Rizos, 1982). By applying a minimum condition on the differences between (global) mean sea level and the geoid (mean sea surface topography, cf. [3.4.2]), the geoid could be defi ned as the equipotential surface which best fi ts mean sea level at a certain epoch (Rapp, 1995a), cf. [3.4.3].

Another choice would be to defi ne the geoid as the level surface which optimally fi ts mean sea level at a selected set of tide gauges used for defi ning the vertical datum of national or continental height systems (Burša et al., 2002), cf. [7.2]. Such a defi nition would lead to only small corrections for the existing height systems but not result in a best fi t over the open oceans. From the relativistic point of view, another approach would be to defi ne the geoid as the surface where clocks have the same proper time (Müller et al., 2008). As discussed in [2.2.1], the defi nition of Terrestrial Time TT requires the geopotential value of the geoid, and a corresponding value is provided by the IERS Conventions. As a consequence, optical atomic clocks with a frequency stability of $1 0 ^ { - 1 7 } - 1 0 ^ { - 1 8 }$ would allow a potential transfer for geoid determination with dm- to cm-accuracy (Burša et al., 2007), cf. also [2.2.1].

# 3.4.2 Mean sea level

The ocean surface does not coincide with a level surface (e.g., the geoid) of the Earth’s gravity fi eld; the deviations are called sea surface topography SST (also ocean surface topography or dynamic ocean topography DOT). Instantaneous SST is affected by temporal variations of long-term, annual, seasonal, and short-term character, occurring at different scales. Averaging the ocean surface over time (at least over one year) and/ or modeling ocean tides provides Mean Sea Level (MSL) for the corresponding time interval. But, even after reducing all time-dependent parts, a (smooth) quasi-stationary SST would remain (mean sea surface or mean dynamic ocean topography). It is caused by nearly constant oceanographic and meteorological effects, which generate ocean currents and ocean surface slopes. The r.m.s. variation of this mean dynamic ocean topography is $\pm 0 . 6$ to $\pm 0 . 7 \textrm { m }$ , and the maximum deviation from the geoid is about $\pm 1 \textrm { m }$ or more (Bosch et al., 2010).

Short term variations of the sea surface (waves) are averaged out in the mean value over time (e.g., at tide gauge observations over one hour) or by the smoothing effect of the “footprints” in satellite altimetry, with spatial extension of several kilometers, cf. [5.2.7].

Ocean tides contribute about $7 0 \%$ to the variability of the sea surface, with maximum partial tides at daily and half-daily periods (Le Provost, 2001). The tidal effects can deviate considerably between the open ocean and shelf areas, adjacent seas, and coastal zones. This is due to unequal water depths and to the fact that the continents impede the free movement of water. On the open sea, the tidal amplitude is less than one meter (r.m.s. variation $\pm 0 . 3$ m), while it can amount to several meters in coastal areas (Bay of Fundy, Nova Scotia: more than $1 5 \mathrm { ~ m ~ }$ ). Oceanic tidal models are based on Laplace’s tidal equations, taking ocean boundaries, bathymetry and tidal friction into account. Early models were constrained to fi t tide gauge observations (Schwiderski, 1980, 1983). The results of ocean-wide satellite altimetry (Chambers, 2009) allowed the development of empirical tidal models (Andersen and Knudsen, 1997; Bosch et al., 2009), and the assimilation of altimetric data into hydrodynamic models (Le Provost et al., 1998). The models solve for about 10 to 15 and more partial tides (annual, semi-annual, monthly, fortnightly, diurnal, semi-diurnal, quarter-diurnal). They are provided either in grid form (from $1 ^ { \circ } \times 1 ^ { \circ }$ to $0 . 2 5 ^ { \circ } \times \ : 0 . 2 5 ^ { \circ }$ and $0 . 1 2 5 ^ { \mathrm { o } } \times 0 . 1 2 5 ^ { \mathrm { o } } )$ or as a spherical harmonic expansion. Ocean tide models have also been derived by including tidal parameters into global gravity modeling (Lyard et al., 2006). The accuracy of the oceanic tidal models amounts to $\pm 1$ to $2 \mathrm { \ c m }$ on the open oceans but is less at shelf areas and close to the coast (Shum et al., 1997).

Sea level fl uctuations of annual, semi-annual, and seasonal character are of meteorological origin (atmospheric pressure, winds, heat exchange between water masses, atmosphere and land), and of oceanographic nature (ocean currents, differences in water density as a function of temperature, salinity and pressure), and are also due to a variable water budget (changing water infl ux, e.g. as a result of polar ice melting, strong precipitation, e.g. through monsoon rains, etc.). The amplitude of these variations is on the order of 0.1 to $1 \textrm { m }$ , and scales are of a few 100 to $1 0 0 0 ~ \mathrm { k m } ,$ , e.g. at meandering ocean streams and eddies (Nerem, 1995; Bosch, 2004). We especially mention the annual oscillation (0.1 to $0 . 2 ~ \mathrm { { m } }$ ) between the water masses of the northern and the southern hemisphere, which is due to different solar heating, and the interannual El Niño phenomenon, cf. [8.3.3]. An interaction between the ocean tides and the ocean circulation has also been found, which is induced by internal tides generated at topographic features as islands or ocean trenches (Garrett, 2003). In addition, a global secular rise of about 1 to $2 \ \mathrm { m m } / \mathrm { a }$ has been observed over the last 100 years (e.g., Douglas, 1997). This trend is expected to increase, reaching eventually $_ { 0 . 6 \mathrm { ~ m ~ } }$ (or even more?) over the $2 1 ^ { \mathrm { s t } }$ century, due to climate changes producing a thermal expansion of the water masses, a melting of the polar ice caps and the glaciers, changing continental hydrology, and isostatic movements (Church et al., 2008). The current rate of a global sea level rise as derived from satellite altimetry is between 3 and $4 \ \mathrm { m m }$ /year, but this trend is superimposed by strong regional variations of different sign, reaching the cm-order of magnitude (Bosch et al., 2010, Cazenave and Llovel, 2010), cf. also [8.3.3].).

Mean sea level can be derived from tide gauge records, satellite altimetry, and oceanographic methods.

Tide gauges (mareographs) continuously record the height of the water level with respect to a height reference surface close to the geoid, cf. [3.4.3]. Averaging the results over long time intervals (month, year) eliminates most variations with time. In order to fully remove the tidal period of a complete lunar cycle (nutation), the record should extend over 18.6 years, cf. [2.3.2]. The precision of the mean monthly and annual values is generally better than $\pm 1 \mathrm { \ c m }$ . These results may be systematically disturbed if the tide gauge location is not directly linked to the open ocean and data is thereby affected by local sea level anomalies (swell in shallow waters, estuary effects at river mouths). In addition, local or regional vertical crustal movements (land sinking due to water or oil pumping, sedimentary subsidence, postglacial uplift, etc.) may act at the tide gauge location and systematically affect (bias) the sea level registration. These movements may reach a few mm/year (Mitchum, 1994). They are now generally observed by means of geodetic space techniques, especially continuous GPS observations (e.g., Becker et al., 2002), cf. [8.3.3].

Tide gauge data are available for almost 2000 stations worldwide, but only a few stations cover a time span of a few centuries (at Amsterdam registrations go back to 1700). The Global Sea Level Observing System (GLOSS) of the International Oceanographic Commission (IOC) defi nes a worldwide Core Network of approximately 300 stations, which is densifi ed by regional and national networks (Woodworth and Player, 2003). In the open oceans, pressure tide gauges contribute in monitoring sea surface variability by exploiting the hydrostatic equation (8.5), but lack connection to continental height systems, e.g., Tolkatchev (1996). Tide gauges along the continental coasts generally have been connected to the local geodetic height control system, thus permitting to determine the deviation of MSL from a zero height reference close to the geoid. Sea level slopes up to several $0 . 1 \ \mathrm { m } / 1 0 0 0 \ \mathrm { k m }$ and more have been detected by this method, cf. [3.4.3].

Satellite altimetry directly delivers sea surface heights with respect to an ellipsoidal reference surface, by regular surveys of the oceans, cf. [5.2.7]. With the exception of the polar regions, satellite altimeters cover the marine areas with repeated tracks (e.g., with a 10 days repetition rate at TOPEX/Poseidon) and permit derivation of mean sea surface heights to an accuracy of 1 to $2 \ \mathrm { c m }$ . Preprocessed sea surface heights for the individual missions are provided by the responsible space agencies like NASA and ESA. Refi ned solutions are derived over a certain time period (e.g., one month or one year) and given in grids of a few minutes of arc; they differ with respect to the used data sets, the evaluated time span, and the evaluation method (Tapley and Kim, 2001). Sea surface topography is obtained by referring these results to a geoid model. If the altimetric solutions for different epochs are compared, sea surface variations with time can be determined which are due to redistribution of oceanic water masses (e.g., Minster et al., 1995), see above and [8.3.3].

Oceanographic methods derive sea surface topography from measurements at sea (Rummel and Ilk, 1995). Steric leveling assumes that equipotential and isobaric surfaces coincide at a certain depth (e.g., $2 0 0 0 \ \mathrm { m }$ ): “level of no motion”. Using water density values derived from salinity, temperature, and pressure data along vertical profi les, the integration of the hydrostatic equation yields the gravity potential difference (or the dynamic height, also geopotential height, cf. [3.4.3]) between two pressure levels, the ocean surface and the reference “level of no motion”. This method is applicable in the deep oceans and was used to compute mean monthly and annual dynamic heights. Geostrophic leveling (dynamic leveling) is based on the hydrodynamic equations and uses observed ocean current velocities. It can also be applied in shelf areas (Sturges, 1974).

![](images/9249968e606008ab12d3027415ee258674b34eca2b65105714e0c3030d767d87.jpg)  
Fig. 3.13: Mean sea surface topography (meter above the geoid) for the period 1993–2008, resolution about $5 0 0 ~ \mathrm { k m }$ , after Bosch et al. (2010).

Sea surface topography models have been developed by oceanographic and altimetric methods. Oceanic models correspond to a spherical harmonic expansion up to degree 36 (or a minimum wavelength of $1 0 ^ { \circ } )$ with an accuracy of a few cm to $_ { 0 . 1 \mathrm { ~ m ~ } }$ (Levitus et al., 1994). Satellite altimetry solutions are based on subtracting geoid heights from altimetric sea surface heights. This can be done straightforward, comparing the sea surface height data with a global geoid model, or by inclusion of the sea surface topography into a common adjustment, together with gravity fi eld and satellite orbit parameters (e.g., Lemoine et al., 1998; Tapley et al., 2003; Savcenko and Bosch, 2008). In the latter case, the separation of the geoid and the ocean topography poses a special problem, and spherical harmonic developments of the sea surface topography remain signifi cantly below the spatial resolution of (satellite-only) gravity fi eld developments $1 ^ { \circ }$ to $2 ^ { \circ }$ resolution and cm-accuracy). Fig. 3.13 shows the quasi-stationary sea surface topography as derived for a limited time span, which clearly reveals the main ocean currents, and an equatorial bulge of roughly a half meter with respect to mid-latitudes (Bosch et al., 2010).

# 3.4.3 The geoid as height reference surface

The geoid is used in geodesy, cartography and geomatics, as well as in geophysics and especially in oceanography as a reference surface for heights and depths (continental and ocean bottom topography, as well as sea surface topography). A point $P$ can be

attributed to a specifi ed level surface by its gravity potential $W$ (Fig. 3.14). With respect to the geoid potential $\boldsymbol { W } _ { 0 ^ { \prime } }$ the “height” of $P$ is given by the negative potential difference to the geoid, which is called the geopotential number $C .$ We get from (3.52)

$$
C = W _ { \circ } - W _ { \circ } = - \intop _ { P _ { \circ } } ^ { P } d W = \intop _ { P _ { \circ } } ^ { P } g d n .
$$

The integral is independent of the path. Hence, $P _ { 0 }$ is an arbitrary point on the geoid. $C$ can be determined from geometric leveling and gravity measurements along any path between $P _ { 0 }$ and $P ,$ cf. [5.5.4].

The geopotential number is an ideal measure for describing the behavior of masses (e.g., water masses) in the gravity fi eld, it satisfi es the fundamental hydrostatic equation, see [8.1]. It could be used as a “height” in several applications, as in hydraulic engineering, oceanography and meteorology. A more general use is limited by the potential unit $\mathsf { m } ^ { 2 } \mathsf { s } ^ { - 2 } ,$ which is in contradiction to the obvious demand for a metric height system that employs the “meter” unit.

In order to achieve a certain agreement with the numerical value of the height in meters, the geopotential unit $1 0 \ m ^ { 2 } \ s ^ { - 2 } ,$ , or ${ \mathrm { k G a l ~ m } } ,$ is also used for the geopotential number. With $g \approx 9 . 8 \ \mathsf { m } s ^ { - 2 } .$ , the values of $C$ are about $2 \%$ smaller than the corresponding height values.

The dynamic height $H ^ { \mathrm { d y n } }$ is obtained by dividing the geopotential number through a constant gravity level ellipsoid at e. Usually the no latitude is used: $\gamma _ { \mathrm { ~ 0 ~ } } ^ { 4 5 }$ ulated for the surface of the  , cf. [4.3]: $4 5 ^ { \circ }$ $\gamma _ { \scriptscriptstyle 0 } ^ { \scriptscriptstyle 4 5 } = 9 . 8 0 6 ~ 1 9 9 ~ \mathrm { { m s ^ { - 2 } } } ,$

$$
H ^ { \mathrm { d y n } } = \frac { C } { \gamma _ { _ { 0 } } ^ { _ { 4 5 } } } .
$$

The surfaces $H ^ { \mathrm { d y n } } =$ const. remain equilibrium surfaces. Hence, points located on the same level surface have the same dynamic height. Unfortunately, a geometric interpretation of the dynamic heights is not possible, and larger corrections are necessary in order to convert leveling results into dynamic height differences, cf. [6.4.1]. Because of this, dynamic heights have not been widely used in geodesy but are used in oceanography, under the assumption of a hydrostatic equilibrium of the water masses, and also in meteorology, with a standard gravity value at sea level $\gamma _ { \scriptscriptstyle 0 } = 9 . 8 0 6 6 5 \mathrm { { m s } ^ { - 2 } , }$ cf. [3.4.2].

![](images/bcc11934287b4f3f5bac30ebb9f87d49b7c131b4ac16dd56866b218e52b1e0eb.jpg)  
Fig. 3.14: Geoid, mean sea level, continental and sea surface topography.

0National or continental height systems, and terrain-data based on them (topographic maps, digital terrain models), use either orthometric or normal heights.

The orthometric height $H$ is defi ned as the linear distance between the surface point and the geoid, reckoned along the curved plumb line (Fig. 3.14). This defi nition corresponds to the common understanding of “heights above sea level”. Expanding the right-hand side of (3.104) in $H$ and integrating along the plumb line from $P _ { 0 }$ ( $H = 0 )$ to $P \left( H \right)$ we obtain

$$
{ \cal H } = \frac { C } { \overline { { { g } } } ^ { \prime } } , \overline { { { g } } } = \frac { 1 } { H } \int _ { 0 } ^ { H } g d H .
$$

$\overline { { g } }$ is the mean gravity along the plumb line, with the consequence that gravity values inside the Earth are required for its calculation. This is performed by introducing a model of the density distribution of the topographic masses, see [6.4.1] for corresponding esti-_ mates of ${ \overline { { g } } } .$ . As the density distribution is known only imperfectly, the accuracy of computed orthometric heights depends on the accuracy of the density model. In addition, points of equal orthometric height deviate slightly from a level surface, which is due to the non-parallelism of the level surfaces, cf. [3.2.1]. These drawbacks are compensated by the fact that orthometric heights represent the geometry of the topographic masses. In addition, the results of geometric leveling, as the most precise height determination method on land, only need small corrections for the transformation into orthometric height differences, cf. [6.4.1].

In order to avoid any hypothesis on the distribution of the topographic masses, normal heights_ $H ^ { N }$ have been introduced and are used in a number of countries. The mean_ gravity $\dot { \bar { g } }$ in (3.106) is now replaced by the mean normal gravity $\bar { \gamma }$ along the normal plumb line, which is only slightly curved, cf. [4.2.3]:

$$
H ^ { N } = \frac { C } { \overline { { { \gamma } } } } , { \overline { { { \gamma } } } } = \frac { 1 } { H ^ { N } } \int _ { 0 } ^ { H ^ { N } }  \ d \gamma
$$

$\bar { \gamma }$ can be calculated in the normal gravity fi eld of an ellipsoidal Earth model, cf. [4.2.2]. The reference surface for the normal heights is the quasigeoid. It is obtained pointwise by drawing the normal heights from the Earth’s surface to the interior. The quasigeoid thus constructed is close to the geoid but not a level surface. It deviates from the geoid on the mm-to-cm order at low elevations and may reach $1 \textrm { m }$ deviation in the high mountains. On the oceans, geoid and quasigeoid practically coincide, cf. [6.1.1].

A global vertical reference surface “geoid” could be based on the determination of a geoid potential value $W _ { 0 }$ derived from sea surface topography SST, cf. [3.4.2]. According to Bruns’ formula (6.97b), SST is proportional to the difference between the gravity potential values on the geoid $W _ { 0 }$ and on the ocean surface $W _ { \mathrm { p ^ { \prime } } }$ i. e., the geopotential number (3.104): $\mathsf { S S T } = ( W _ { \mathrm { 0 } } - W _ { \mathrm { p } } ) / \gamma _ { \scriptscriptstyle P ^ { \prime } }$ with normal gravity $\gamma$ A minimum condition applied on SST then serves for estimating $W _ { 0 } .$ The “vertical coordinates” in this system are given by the potential values $W$ (calculated in the zero-tidal system, cf. [3.4.1]) or the geopotential numbers. As the result would be derived from data collected over a limited (although as long as possible!) time interval, it should refer to a defi ned epoch. Using the results of dedicated satellite gravity fi eld missions, cf. [5.2.8], and recent (and future) satellite altimetry, cf. [5.2.7], such a global vertical reference surface could be realized with cm-accuracy.

The realization of the vertical reference system on the continents requires special consideration. Presently, the zero height surface (vertical datum) of national height systems is defi ned by the mean sea level derived from tide gauge records over a certain time interval (the International Hydrographic Organization defi nes MSL as the average height of the sea surface over a 18.6-year period), and realized through the zero-points of tide gauges. By transferring potential differences (or height differences in the national height system) from the zero-point to the benchmarks of the vertical control network, the vertical datum fi nally is realized by the set of benchmark heights, cf. [7.2]. These local reference surfaces only approximate the geoid or the quasigeoid, due to the effect of sea surface topography and local sea level anomalies, with deviations up to $1 \textrm { m }$ and more, cf. [3.4.2].

As a consequence, a global vertical reference system is actually defi ned and realized only at the accuracy level of a few decimeters, through the $W _ { 0 }$ -values of different SST evaluations (the IERS Conventions 2010 give the value $\mathsf { \bar { \Delta } W } _ { 0 } = 6 2 \mathsf { \Omega } 6 3 6 8 5 6 . 0 \pm 0 . 5 \mathsf { m } ^ { 2 } \mathsf { s } ^ { - 2 } ,$ as a recent standard). On the continents, the present realization of a global vertical system is even worse. This accuracy is signifi cantly less than that of the global geometric reference system, cf. [4.3], and does no longer satisfy the needs of geodesy and oceanography. Basic strategies for the defi nition and realization of a world height system follow the ideas explained above (Rummel and Teunissen, 1988; Rapp, 1995b). These strategies include the determination of the potential offsets of local vertical height systems from a global system (defi ned through the geoid potential), exploiting GNSS positioning at bench marks, and provide fi rst results (Ihde and Sánchez, 2005; Sánchez, 2009).

The adjustment of a continental-wide leveling network connected to MSL of one tide gauge, provides potential differences or heights that refer to one common level surface. By comparing with the mean sea level obtained at different tide gauges, sea level slopes that partially agree with oceanic leveling results have been found. For example, MSL at the Pacifi c coast of the U.S.A. is about $1 \textrm { m }$ higher than at the Atlantic coast (Zilkoski et al., 1995), and the mean Baltic Sea level is estimated to be about $0 . 5 \mathrm { ~ m ~ }$ above MSL of the Mediterranean Sea (Sacher et al., 1999). On the other hand, there are also larger discrepancies of a few $_ { 0 . 1 \mathrm { ~ m ~ } }$ between the results of geometric and oceanic leveling. These can be traced back to differently defi ned reference surfaces, to the particular behaviour of MSL along the coastlines, and to systematic errors in geometric leveling over long distances (Fischer, 1977). It should also be mentioned that older leveling networks have often been adjusted without any gravity reduction, or by substituting actual gravity with normal gravity, thus producing larger systematic errors, cf. [7.2]. A unifi cation of the different vertical datum systems to a world-wide standard thus would also require a uniform treatment of the height measurements, in addition to the vertical shifts to a common global reference surface (see above).

# 3.5 Temporal gravity variations

Gravity changes with time may be divided into effects due to an eventual time dependent gravitational constant and variations of the Earth’s rotation [3.5.1], tidal accelerations [3.5.2], and variations caused by terrestrial mass displacements [3.5.3]. These changes are of global, regional, or local character and occur either at well-known frequencies (tides) or at time scales ranging from secular to episodic (Lambeck, 1988; Mueller and Zerbini, 1989; Timmen, 2010).

# 3.5.1 Gravitational constant, Earth rotation

Based on cosmological considerations, Dirac (1938) postulated a secular decrease of the gravitational constant $G ,$ with relative changes of $\dot { G } / G = - 1 0 ^ { - 1 0 }$ to $- 1 0 ^ { - 1 1 } / \mathrm { a }$ ( $\dot { G } = d G / d t )$ . But even to this day, laboratory experiments and the analysis of long-term observations to artifi cial satellites and the moon have not supported the assumption $\dot { G } \neq 0$ (Gillies, 1987).

A powerful tool for detecting a secular variation of $G$ is lunar laser ranging, as such a variation would change the Earth-moon distance. Recently, the analysis of 40 years of lunar laser ranging data yielded a relative change of $( - 1 \pm 4 ) \times 1 0 ^ { - 1 3 } / \mathrm { a }$ for the gravitational constant, which is not signifi cant (Hofmann et al., 2010).

The Earth’s rotational vector $\boldsymbol { \mathfrak { o } }$ is subject to secular, periodic, and irregular variations, leading to changes of the centrifugal acceleration $\mathbf { Z } ,$ cf. [2.3.4]. In a spherical approximation, the radial component of $\mathbf { z }$ enters into gravity, cf. [3.1.4]. By multiplying (3.35b) with cos $\overline { { \varphi } }$ ${ \overline { { \varphi } } } =$ geocentric latitude), we obtain

$$
Z _ { r } = - \omega ^ { 2 } r \cos ^ { 2 } \overline { { \varphi } } .
$$

Differentiation yields the effect of changes in latitude (polar motion) and angular velocity (length of day) on gravity:

$$
\delta z _ { r } = \omega ^ { 2 } r \sin 2 \overline { { \varphi } } d \overline { { \varphi } } - 2 \omega r \cos ^ { 2 } \overline { { \varphi } } d \omega .
$$

Polar motion does not exceed a few $0 . 1 ^ { \prime \prime } / { \sf a } ,$ , and rotation changes are at the order of a few ms. Hence, corresponding gravity variations on the Earth’s surface $r = 6 3 7 1$ km) remain less than $0 . 1 \mu \mathrm { m } \mathrm { } s ^ { - 2 }$ and $0 . 0 1 \mu \mathrm { m } \mathsf { s } ^ { - 2 } ,$ , respectively. They can be taken into account easily by corresponding models, cf. [5.3.3], [5.4.1].

# 3.5.2 Tidal acceleration, tidal potential

Tidal acceleration is caused by the difference between lunisolar gravitation (and to a far lesser extent planetary gravitation) and orbital accelerations due to the motion of the Earth around the barycenter of the respective two-body system (Earth-moon, Earth-sun, etc.). The periods of these orbital motions are about 28 days for the moon and 365 days for the sun, and the gravimetric tidal effect is at the order of $1 0 ^ { - 7 } g$ (Melchior, 1983; Zürn and Wilhelm, 1984; Wenzel, 1997a).

For a rigid Earth, the tidal acceleration at a given point can be determined from Newton’s law of gravitation and the ephemerides (coordinates) of the celestial bodies (moon, sun, planets). The computations are carried out separately for the individual two-body systems (Earth-moon, Earth-sun, etc.), and the results are subsequently added, with the celestial bodies regarded as point masses.

We consider the geocentric coordinate system to be moving in space with the Earth but not rotating with it (revolution without rotation). All points on the Earth experience the same orbital acceleration in the geocentric coordinate system (see Fig. 3.15 for the Earth-moon system). In order to obtain equilibrium, orbital acceleration and gravitation of the celestial bodies have to cancel in the Earth’s center of mass. Tidal acceleration occurs at all other points of the Earth. The acceleration is defi ned as the difference between the gravitation $\mathbf { b }$ , which depends on the position of the point, and the constant part $\mathbf { b } _ { _ { 0 ^ { \prime } } }$ referring to the Earth’s center:

$$
\mathbf { b } _ { t } = \mathbf { b } - \mathbf { b } _ { 0 } .
$$

![](images/cccf1fdcd71da647d71475fa69829290501bd0089d0945e2742ce8f521d81ef4.jpg)  
Fig. 3.15: Lunar gravitation, orbital acceleration, and tidal acceleration.

The tidal acceleration deforms the Earth’s gravity fi eld symmetrically with respect to three orthogonal axes with origin at the Earth’s center. This tidal acceleration fi eld experiences diurnal and semi-diurnal variations, which are due to the rotation of the Earth about its axis.

If we apply the law of gravitation to (3.110), we obtain for the moon $( m )$

$$
\mathbf { b } _ { t } = \frac { G M _ { m } } { I _ { m } ^ { 2 } } \frac { \mathbf { l } _ { m } } { I _ { m } } - \frac { G M _ { m } } { I _ { m } ^ { 2 } } \frac { \mathbf { r } _ { m } } { I _ { m } } .
$$

Here, $M _ { { \scriptscriptstyle m } }$ is the mass of the moon, and $I _ { \mathrm { { m } } }$ and $r _ { \mathrm { m } }$ are the distances to the moon as reckoned from the calculation point $P$ and the Earth’s center of mass $O _ { \prime }$ respectively. We have $\mathbf { b } _ { t } = \mathbf { 0 }$ for $I _ { \mathrm { { m } } } = r _ { \mathrm { { m } } }$ . Corresponding relations hold for the Earth-sun and Earth-planet systems.

We now make the transition from the tidal acceleration to the tidal potential:

$$
\mathbf { b } _ { t } = \operatorname { g r a d } V _ { t } = \operatorname { g r a d } ( V - V _ { 0 } ) .
$$

In the geocentric system, using spherical coordinates $r _ { m ^ { \prime } } \psi _ { \mathrm { m } }$ (functions of time!), the law of gravitation yields the potential of a point mass according to (3.9):

$$
V = \frac { G M _ { _ m } } { I _ { _ m } }
$$

with

$$
I _ { { \scriptscriptstyle m } } = \big ( r ^ { 2 } + r _ { { \scriptscriptstyle m } } ^ { 2 } - 2 r r _ { { \scriptscriptstyle m } } \cos \psi _ { { \scriptscriptstyle m } } \big ) ^ { \frac { 1 } { 2 } } .
$$

The potential of the homogeneous ${ \bf b } _ { 0 }$ -fi eld is given by multiplying $\mathrm { b } _ { \mathfrak { o } }$ with $r \cos \psi _ { m }$

$$
V _ { _ { 0 } } = { \frac { G M _ { _ { m } } } { r _ { _ { m } } ^ { 2 } } } r c o s \psi _ { m } .
$$

Inserting (3.113) and (3.114) into (3.112), and adding an integration constant, so that $V _ { t } = 0$ for $r = 0$ and $I _ { { \scriptscriptstyle m } } = r _ { { \scriptscriptstyle m } ^ { \prime } }$ we get for the tidal potential

$$
V _ { \mathrm { * } } = G M _ { \mathrm { * } } \left( \frac { 1 } { I _ { \mathrm { * } } } - \frac { 1 } { r _ { m } } - \frac { r \cos \psi _ { m } } { r _ { m } ^ { 2 } } \right) .
$$

The tidal potential, and functionals thereof, can be calculated either from the ephemerides of the celestial bodies or from a spherical harmonic expansion. Tidal potential catalogues are based primarily on the latter method, as the series expansions converge rapidly close to the Earth’s surface $\left( r = R \right) $ , with $r / r _ { m } = 1 / 6 0$ for the moon and a corresponding relation of $1 / 2 3 6 0 0$ for the sun. The results from calculations employing the ephemerides may serve as a control for the tidal potential cataloges.

We develop (3.113b) into a series according to (3.79). When inserting into (3.115), the terms of degree zero and one cancel and we obtain

$$
V _ { _ t } = { \frac { G M _ { _ m } } { r _ { _ m } } } \sum _ { { l = 2 } } ^ { \infty } \biggl ( { \frac { r } { r _ { _ m } } } \biggr ) ^ { { l } } P _ { _ l } ( \cos { \psi _ { _ m } } ) ,
$$

where $P _ { _ { I } } ( \cos \psi _ { _ { m } } )$ are the Legendre polynomials of degree $I .$ The development converges rapidly due to the factor $r / r _ { { \mathrm { m } } ^ { \prime } }$ with the largest contribution $( \approx 9 8 \%$ ) originating from degree two. Restricting ourselves now to $I = 2$ , and inserting $P _ { _ 2 }$ (3.83) in the form

$$
\cos ^ { 2 } \psi _ { m } = \frac { 1 } { 2 } \left( \cos 2 \psi _ { m } + 1 \right) ,
$$

we get the main term of the tidal potential series

$$
V _ { _ t } = { \frac { 3 } { 4 } } G M _ { _ m } { \frac { r ^ { 2 } } { r _ { _ m } ^ { 3 } } } \left( \cos 2 \psi _ { _ m } + { \frac { 1 } { 3 } } \right) .
$$

For $r = R ,$ and neglecting the slight variation of $r _ { m ^ { \prime } }$ the expression before the parentheses is called Doodson’s tidal constant. It is $2 . 6 2 8 \ : \mathrm { \ m } ^ { 2 } \ : \mathrm { s } ^ { - 2 }$ for the moon and $1 . { \dot { 2 } } 0 8 ~ \mathsf { m } ^ { 2 } \mathsf { s } ^ { - 2 }$ for the sun. Hence, the solar tides amount to $4 6 \%$ of the lunar tides.

Differentiating (3.117) generates the tidal acceleration. The radial component (positive outward) is found to be

$$
b _ { r } = { \frac { \partial V _ { t } } { \partial r } } = { \frac { 3 } { 2 } } G M _ { m } { \frac { r } { r _ { m } ^ { 3 } } } \Bigl ( \cos 2 \psi _ { m } + { \frac { 1 } { 3 } } \Bigr ) .
$$

The tangential component (positive in the direction toward the moon) is

$$
b _ { \psi _ { m } } = - \frac { \partial V _ { t } } { r \partial \psi _ { m } } { = } \frac { 3 } { 2 } G M _ { m } \frac { r } { r _ { m } ^ { 3 } } \mathrm { s i n } 2 \psi _ { m } .
$$

Equations (3.117) to (3.119) permit calculation of the tidal effects on the level surfaces, on gravity, and on the plumb line direction for a rigid Earth.

Taking the relation (3.52) between a potential change and the vertical shift of a level surface into account, (3.117) delivers the tidal-induced increase of a level surface. This amounts to $0 . 3 6 \mathsf { m }$ for the moon and $0 . 1 6 \mathsf { m }$ for the sun at $\psi = 0 ^ { \circ }$ and $1 8 0 ^ { \circ } .$ , respectively. At $\psi = 9 0 ^ { \circ }$ and $2 7 0 ^ { \circ }$ , we have a decrease of $0 . 1 8 \mathrm { ~ m ~ }$ and $0 . 0 8 \mathrm { ~ m ~ }$ , respectively. For stationary systems, the level surfaces would experience a corresponding deformation, and freely moving masses of water would assume the form of one of these surfaces (equilibrium tide), Fig. 3.16.

![](images/fbc9fd6aca0ee819ba399606d1b660e834178e466cc140bf293417f2e9089ad2.jpg)  
Fig. 3.16: Tidal acceleration and equilibrium tide.

According to (3.118), gravity changes (opposite sign!) would vary between $- 1 . 1 ~ \mu \mathrm { m } s ^ { - 2 }$ (moon) and $- 0 . 5 ~ { \mu \mathrm { m } } s ^ { - 2 }$ (sun) for $\psi = 0 ^ { \circ }$ (zenithal position); and $+ 0 . { \overset { \cdot } { 5 } } \mu \mathrm { m } \mathsf { s } ^ { - 2 }$ (moon) and $^ +$ $0 . 3 ~ { \mu \mathrm { m } } s ^ { - 2 }$ (sun) for $\psi = 9 0 ^ { \circ }$ and $1 3 5 ^ { \circ }$ . Changes in the direction of the plumb line are given by $\mathrm { b } _ { \psi } / \mathrm { g } ,$ see (3.119). There is no tidal effect at $\psi = 0 ^ { \circ }$ and $9 0 ^ { \circ }$ . Maximum values occur at $\psi = 4 5 ^ { \circ }$ and $1 3 5 ^ { \circ } { } .$ , with fl uctuations of $\pm 0 . 0 1 7 ^ { \prime \prime }$ (moon) and $\pm 0 . 0 0 8 ^ { \prime \prime }$ (sun).

Equation (3.117) provides the dependence of the tidal potential on the zenith angle (and the distance) to the celestial body. The temporal variation of the tidal potential and acceleration is more easily recognized if we change to the Earth-fi xed coordinate __ system $( { \overline { { \Phi } } } , \lambda )$ for the point of calculation and to the equatorial system of astronomy $( \delta ,$ $h )$ for the celestial body, cf. [2.3.1]. Following (2.21), we have for the moon the relation

$$
\cos \psi _ { { m } } = \sin \bar { \varphi } \sin \delta _ { { m } } + \cos \bar { \varphi } \cos \delta _ { { m } } \cos h _ { { m } }
$$

with the hour angle given by (2.22) and (2.23):

$$
h _ { _ m } = \mathsf { L A S T } - \alpha _ { _ m } = \lambda + \mathrm { G A S T } - \alpha _ { _ m } .
$$

Substituting into (3.117) yields Laplace’s tidal equation for the moon (a corresponding equation is valid for the sun):

$$
V _ { \mathrm { \Gamma } } = \frac { 3 } { 4 } \ G M _ { m } \frac { r ^ { 2 } } { r _ { m } ^ { 3 } } \{ ( \frac { 1 } { 3 } - \sin ^ { 2 } \overline { { { \varphi } } } ) ( 1 - 3 \sin ^ { 2 } \delta _ { m } ) +  \qquad  \\  \qquad V _ { \mathrm { \Gamma } } = \frac { 3 } { 4 } \ G M _ { m } \frac { r ^ { 2 } } { r _ { m } ^ { 3 } } \{ \sin 2 \overline { { { \varphi } } } \sin 2 \delta _ { m } \cos h _ { m } + \cos ^ { 2 } \overline { { { \varphi } } } \cos ^ { 2 } \delta _ { m } \cos 2 h _ { m } \} .
$$

The quantities $r _ { m ^ { \prime } } \delta _ { m ^ { \prime } }$ and $h _ { { } _ { r } }$ vary with time, having different periods. The fi rst term, which is independent of the Earth’s rotation, exhibits long-periodic variations (14 days for the moon, half a year for the sun). It also contains a non-periodic part, which only depends on latitude, causing a permanent deformation of the level surfaces including the geoid, cf. [3.4.1]. Using (3.52), and taking the inclination of the ecliptic into account, the geoid is thus lowered by $0 . 1 9 \mathrm { ~ m ~ }$ at the poles and raised by $0 . 1 0 \mathrm { m }$ at the equator (Ekman, 1989). The second term oscillates with diurnal periods because of the daily rotation of the Earth as expressed by the hour angle $h ,$ and the third term introduces semi-diurnal periods. Long-periodic terms enter through the declination $\delta$ and the right ascension $\alpha .$

As seen from (3.122), long-periodic and semi-diurnal tides are symmetric about the equator, while the diurnal tides are antisymmetric. The diurnal tide has its maximum at $\varphi = \pm 4 5 ^ { \circ }$ and vanishes at the equator and the poles, while the semi-diurnal tide reaches its maximum at the equator and is zero at the poles. The long-periodic tides have a maximum at the poles.

Each of the three tidal constituents in (3.122) varies in a complicated way, since they contain products of different time varying functions. However, the ephemerides of the moon and the sun can be expressed as harmonic functions of fi ve fundamental astronomic quantities, considering that these quantities essentially change uniformly with time (Melchior, 1983). Introducing these harmonic series into (3.122) yields a spectral analysis of the tidal potential, and with (3.118) and (3.119), we get a corresponding spectral analysis of the tidal acceleration. Thus, potential and acceleration are represented by the sum of time-dependent cosine functions having constant periods and amplitudes and phases that depend on latitude and height (partial tides). Tab. 3.1 gives the periods and amplitudes of the main gravimetric partial tides for $\varphi = 4 5 ^ { \circ }$ .

Tab. 3.1: Principal gravimetric partial tides for $\overline { { \varphi } } = 4 5 ^ { \circ } , \mathrm { h } = 0$   

<table><tr><td>Symbol</td><td>Name</td><td>Period (solar days/hours)</td><td>Amplitude (nms-2)</td></tr><tr><td colspan="4">Long-periodic waves</td></tr><tr><td>M0</td><td>Const. m tide</td><td>8</td><td>102.9</td></tr><tr><td>S0</td><td>Const. s tide</td><td>8</td><td>47.7</td></tr><tr><td>Ssa</td><td>Declin. tide to S0</td><td>182.62 d</td><td>14.8</td></tr><tr><td>Mm</td><td>Ellipt. tide to M0</td><td>27.55 d</td><td>16.8</td></tr><tr><td>Mf</td><td>Declin. tide to M0</td><td>13.66 d</td><td>31.9</td></tr><tr><td colspan="4">Diurnal waves</td></tr><tr><td>01</td><td>Main diurnal m tide</td><td>25.82 h</td><td>310.6</td></tr><tr><td>P1</td><td>Main diurnal s tide</td><td>24.07 h</td><td>144.6</td></tr><tr><td>Q1</td><td>Ellipt. tide to O1</td><td>26.87 h</td><td>59.5</td></tr><tr><td>K1</td><td>Main diurnal/s decl. tide</td><td>23.93 h</td><td>436.9</td></tr><tr><td colspan="4">Semi-diurnal waves</td></tr><tr><td>M2</td><td>Main m tide</td><td>12.42 h</td><td>375.6</td></tr><tr><td>S2</td><td>Main s tide</td><td>12.00 h</td><td>174.8</td></tr><tr><td>N2</td><td>Ellipt. tide to M2</td><td>12.66 h</td><td>71.9</td></tr><tr><td>K2</td><td>Declin. tide to M2, S2</td><td>11.97 h</td><td>47.5</td></tr><tr><td colspan="4">Ter-diurnal waves</td></tr><tr><td>M3</td><td>Ter-diurn.m tide</td><td>8.28 h</td><td>5.2</td></tr></table>

A fi rst expansion for the moon and the sun was carried out by Doodson (1921). The development by Cartwright and Tayler (1971) and Cartwright and Edden (1973) contains 505 partial tides (uncertainty less than $1 \mathrm { n m } \mathrm { s } ^ { - 2 }$ ) and was recommended by IAG for the computation of the tides of the rigid Earth (Rapp, 1983). Among the more recent tidal cataloges is the development by Hartmann and Wenzel (1995). It is based on a spherical harmonic development to degree 6 (moon) and degree 3 (sun) and includes the effects of Venus, Mars, and Jupiter (four orders of magnitude smaller than the tidal effects of moon and sun). It also takes the fl attening of the Earth into account. This catalogue provides 12 935 partial tides, with an accuracy of $0 . 0 \dot { 0 } 1 \ \mathrm { n m } s ^ { - 2 }$ for the gravimetric tidal effect (Wenzel, 1996).

As the Earth is not a rigid body, it reacts in a different way to the tidal force. The solid Earth behaves mainly as an elastic body: Earth’s body tides (Earth tides). In the oceans, tidal oscillations depend on the ocean-bottom topography, with large differences occurring at the coastlines and at the shelf areas: ocean tides (Zahel, 1997; LeProvost, 2001), cf. [3.4.2]. While the measurement of gravimetric tidal effects will be discussed in [5.4.6], the theory of Earth tides and results of Earth-tide observations are given in [8.3.6].

# 3.5.3 Non-tidal temporal gravity variations

The terrestrial gravity fi eld is affected by a number of variations with time due to mass redistributions in the atmosphere, the hydrosphere, the cryosphere, and the solid Earth’s surface, crust, mantle and core (e.g., Ekman, 1989; Dickey, 2002). These processes take place at different time scales and are of global, regional, and local character. The magnitude of these non-tidal gravity variations depends on the amount of mass shifts and is related to them by the law of gravitation. Generally, gravity variations produced by mass redistributions do not exceed the order of ${ { 1 0 } ^ { - 9 } }$ to ${ \mathrm { 1 0 } } ^ { - 8 } g .$ Of special interest for geodesy are temporal changes of the geoid. They generally remain less than 1 mm/year, but may reach regionally one centimetre and more within a few years (e.g., Kuhn, 2002).

Long-term global effects include postglacial rebound, melting of the ice caps and glaciers, as well as sea level changes induced by global warming; slow motions of the Earth’s core and mantle convection also contribute. Subsidence in sedimentary basins and tectonic uplift are examples of regional effects. Groundwater and soil moisture variations are primarily of seasonal character but may affect larger regions, while volcanic and Earthquake activities are short-term processes of more local extent. Human activities as large building projects, irrigation or the withdrawal of water, oil and gas may also cause gravity changes, but are of a more local character.

Observation and modeling of non-tidal temporal gravity variations started with advanced relative and absolute gravimetry, in the second half of the twentieth century. Repeated satellite orbit analyses early allowed the determination of global gravity fi eld changes, e.g., expressed as a change of the Earth’s oblateness. Dedicated gravity fi eld satellite missions are now able to monitor large- and medium-scale variations, of seasonal and long-term character. Small-scale effects still can be detected only by repeated terrestrial gravity measurements (e.g., Torge, 1993; Wahr, 2009). The continuous registration of gravity allows to monitor a multitude of geodynamic phenomena, from the seconds to decades time scale. More details about the measurement and the evaluation of gravity variations with time will be found in the chapters on gravity measurements [5.2.8], [5.4.1], [5.4.6], and on the results obtained by repeated gravity fi eld determination, especially through dedicated satellite missions [8.3.5].

# 4 The Geodetic Earth Model

A geodetic Earth model is used as a reference for the actual surface and external gravity fi eld of the Earth. It should provide a good fi t to the geoid and to the gravity fi eld, and thus allow the linearization of non-linear geodetic problems. On the other hand, the mathematical formation of the model should be simple and possibly permit calculations by closed formulas. The model should serve as a standard for applications not only in geodesy, surveying, navigation, geoinformation and cartography, but also in astronomy and geophysics.

Based on these considerations, the level ellipsoid has been introduced as geodetic Earth model. It possesses a simple geometry, and coordinate systems that refer to it approximate the gravity fi eld related “natural” coordinates suffi ciently well [4.1]. The ellipsoid’s mass and rotation provide a “normal” gravity fi eld exterior to the ellipsoid, which can be rigorously calculated if the ellipsoid surface is defi ned to be in equilibrium [4.2]. State of the art Earth models are recommended from time to time as a standard and are given the name Geodetic Reference System [4.3].

# 4.1 The rotational ellipsoid

The rotational ellipsoid was introduced as a geometrical fi gure of the Earth in the eighteenth century, cf. [1.3.2]. By fi tting its dimension and orientation to the geoid, it approximates this level surface within about $\pm 1 0 0 \mathrm { ~ m ~ }$ . The geometry of the ellipsoid can be described in a simple manner, together with ellipsoidal surface coordinates and curvature [4.1.1], [4.1.2]. The use of global and local three-dimensional ellipsoidal systems provides an approximation to the corresponding systems of the actual Earth and permits the separation between horizontal position and height [4.1.3].

Geometry and coordinate systems of the ellipsoid are well documented in geodetic literature, e.g., Grossmann (1976), Bomford (1980), Heitz (1988), Heck (2003a).

# 4.1.1 Parameters and coordinate systems

The rotational ellipsoid is generated by rotating the meridian ellipse about its minor axis. Size and shape of the ellipsoid are described by two geometric parameters, the semi-major axis a and the semi-minor axis $b$ (Fig. 4.1). Generally, $b$ is replaced by a smaller quantity, describing the (small) polar fl attening of the ellipsoid, which is more suitable for series expansions. We especially have the (geometrical) fl attening

$$
f = { \frac { a - b } { a } } ,
$$

the fi rst numerical eccentricity

$$
e = { \frac { \sqrt { a ^ { 2 } - b ^ { 2 } } } { a } } ,
$$

![](images/3ba01d52a14c239782f8202e4b16643231961c1996bb1559f963e3d3cc44c3f5.jpg)  
Fig. 4.1: Meridian ellipse.

and the second numerical eccentricity

$$
e ^ { \prime } = \frac { \sqrt { a ^ { 2 } - b ^ { 2 } } } { b } .
$$

The following relations hold among those quantities:

$$
{ \frac { b } { a } } = 1 - f = { \sqrt { 1 - e ^ { 2 } } } = { \frac { 1 } { \sqrt { 1 + e ^ { \prime 2 } } } } = { \frac { e } { e ^ { \prime } } } .
$$

From the geometric defi nition of the ellipse as the curve having a constant value for the sum of the distances $r _ { \mathrm { \tau } }$ and $r _ { 2 }$ to the focal points $F$ (Fig. 4.1)

$$
r _ { 1 } + r _ { 2 } = 2 a , 
$$

we obtain the linear eccentricity as another quantity describing the fl attening:

$$
\varepsilon = { \sqrt { a ^ { 2 } - b ^ { 2 } } } .
$$

We now introduce a spatial Cartesian ${ \overline { { X } } } , { \overline { { Y } } } ,$ ${ \overline { { Z } } } .$ -coordinate system (Fig. 4.2). The origin of the system is situated at the center of the ellipsoid $O$ . The $\bar { Z }$ -axis coincides with the minor axis of the ellipsoid. The equation of the surface of the ellipsoid is then given by

$$
\frac { \overline { { { X } } } ^ { 2 } + \overline { { { Y } } } ^ { 2 } } { a ^ { 2 } } + \frac { \overline { { { Z } } } ^ { 2 } } { b ^ { 2 } } - 1 = 0 .
$$

![](images/98fba58ad144f936369bb8e8fc4e624219d709cb794c422b5a96eda9454e282e.jpg)  
Fig. 4.2: Geodetic coordinates latitude and longitude.

The system of geodetic surface coordinates is defi ned by the ellipsoidal latitude $\varphi$ and longitude $\lambda$ (also geodetic latitude and longitude). _ _ $\varphi$ is the angle measured in the meridian plane between the equatorial plane $( { \overline { { X } } } , { \bar { Y } } .$ -plane) of the ellipsoid and the surface normal at $P .$ Longitude $\lambda$ is the angle measured in the equatorial plane between the zero meridian ${ \bar { X } } .$ -axis) and the meridian plane of $P .$ Here, $\varphi$ is positive northwards and negative southwards, and $\lambda$ is positive as reckoned towards the east. The ellipsoidal merid-_ ian plane is formed by the surface normal and the $\bar { Z }$ -axis. $\varphi$ and $\lambda$ are defi ned to have angular values, but they may also be considered as curvilinear surface coordinates. The coordinate lines of this orthogonal system are the meridians ( $\lambda =$ const.) and the parallels, or circles of latitude, ( $\varphi =$ const.). With

$$
\begin{array} { r } { \overline { { X } } = p \mathrm { c o s } \lambda , \quad \overline { { Y } } = p \mathrm { s i n } \lambda , } \end{array}
$$

we introduce the radius of the circle of latitude

$$
p = \sqrt { \overline { { X } } ^ { 2 } + \overline { { Y } } ^ { 2 } }
$$

as a new variable (Fig. 4.2). Substituting $p$ into (4.4) and differentiating yields the slope of the ellipsoidal tangent at $P$ (Fig. 4.3):

$$
\frac { d \bar { Z } } { d p } = - \bigg \vert \frac { b } { a } \bigg \vert ^ { 2 } \frac { p } { \bar { Z } } = - \cot \varphi .
$$

By combining (4.4) and (4.7), and substituting $p$ with (4.5), the parametric representation of the meridian ellipse follows:

$$
{ \begin{array} { l } { { \overline { { X } } } = { \frac { a ^ { 2 } \cos \varphi \cos \lambda } { ( a ^ { 2 } \cos ^ { 2 } \varphi + b ^ { 2 } \sin ^ { 2 } \varphi ) ^ { \frac { 1 } { 2 } } } } , \quad { \overline { { Y } } } = { \frac { a ^ { 2 } \cos \varphi \sin \lambda } { \left( a ^ { 2 } \cos ^ { 2 } \varphi + b ^ { 2 } \sin ^ { 2 } \varphi \right) ^ { \frac { 1 } { 2 } } } } , } \\ { { \overline { { Z } } } = { \frac { b ^ { 2 } \sin \varphi } { \left( a ^ { 2 } \cos ^ { 2 } \varphi + b ^ { 2 } \sin ^ { 2 } \varphi \right) ^ { \frac { 1 } { 2 } } } } . } \end{array} }
$$

Instead of $\varphi ,$ other latitude parameters are used for special applications. The geocentric latitude $\overline { { \varphi } }$ has already been introduced together with the longitude $\lambda$ and the geocentric distance $r$ as spherical coordinate, cf. [2.5.1]. From Fig. 4.3, the corresponding equation of the ellipse is given by

$$
p = r \cos \overline { { \varphi } } , \quad \overline { { Z } } = r \sin \overline { { \varphi } } ,
$$

where $p$ follows from (4.5), (4.6).

![](images/204887d14d87b98d873f2181987d91775bff19f83a416aee290e9afba8c564b3.jpg)  
Fig. 4.3: Geodetic, reduced, and geocentric latitude.

The reduced latitude $\beta$ is obtained by projecting (parallel to the $\bar { Z }$ -axis) from the ellipse to the concentric circle of radius a (Fig. 4.3). Since the ratio of the elliptical to the circular coordinates is $\frac { b } { a }$ (ellipse as the affi ne image of the circle), we have

$$
p = a \mathrm { c o s } \beta , \quad \bar { Z } = \frac { b } { a } a \mathrm { s i n } \beta = b \mathrm { s i n } \beta .
$$

Using $\beta$ instead of $\varphi$ formally transforms ellipsoidal into spherical formulas, see also [6.3.3].

Comparing (4.9) and (4.10) with (4.7) provides the transformation between $\varphi , { \overline { { \varphi } } } ,$ and $\beta$ :

$$
\tan { \overline { { \varphi } } } = \left( { \frac { b } { a } } \right) ^ { 2 } \tan \varphi = ( 1 - e ^ { 2 } ) \tan \varphi ,
$$

$$
\tan \beta = \frac { b } { a } \tan \varphi = \sqrt { 1 - e ^ { 2 } } \tan \varphi .
$$

A series expansion yields the differences in the angles:

$$
\varphi - \overline { { { \varphi } } } = \frac { e ^ { 2 } } { 2 } \sin 2 { \varphi } + \ldots = 2 ( \varphi - \beta ) .
$$

The maximum difference occurs at $\varphi = 4 5 ^ { \circ } ,$ , with $( \varphi - \overline { { \varphi } } ) = 6 9 0 { } ^ { \prime \prime }$ .

# 4.1.2 Curvature

The meridians and parallels are the lines of curvature of the rotational ellipsoid. The principal radii of curvature are therefore in the plane of the meridian and in the plane of the prime vertical perpendicular to the meridian plane (Fig. 4.4)._ _ _

The curvature of the meridian (curvature radius $M )$ $\dot { \ Z } = \bar { Z } ( p )$ in the $\bar { Z } , p \cdot$ -plane is given by

$$
\frac { 1 } { M } = - \frac { \displaystyle \frac { d ^ { 2 } \bar { Z } } { d p ^ { 2 } } } { \left( 1 ~ + \left( \frac { d \bar { Z } } { d p } \right) ^ { 2 } \right) ^ { \frac { 3 } { 2 } } } .
$$

![](images/3ebec9a74eccd9e414ace091f34372e075dc937dcf2fbf291d75d32c9f315948.jpg)  
Fig. 4.4: Curvature of the rotational ellipsoid.

With (4.7) and its derivative, and taking (4.2) into account, we obtain the meridian radius of curvature

$$
M = { \frac { a \left( 1 - e ^ { 2 } \right) } { \left( 1 - e ^ { 2 } \sin ^ { 2 } \varphi \right) ^ { \frac { 3 } { 2 } } } } .
$$

The plane of a parallel circle (oblique section of the rotational ellipsoid) and the vertical plane in the same tangential direction intersect at point $P$ with the angle $\varphi .$ The theorem of Meusnier (regarding surface curvatures, see, e.g., Stoker, 1969) provides the radius of curvature in the prime vertical:

$$
N = { \frac { p } { \cos \varphi } } .
$$

Because of rotational symmetry, the origin of $N$ is on the spin axis. Inserting (4.6) and (4.8) into (4.14), one obtains

$$
N = { \frac { a } { ( 1 - e ^ { 2 } \sin ^ { 2 } \varphi ) ^ { \frac { 1 } { 2 } } } } .
$$

A comparison of (4.13) and (4.15) shows that $N \geq M .$ At the poles ( $\varphi = \pm 9 0 ^ { \circ } ,$ ), the polar radius of curvature becomes

$$
c = M _ { \mathrm { { 9 0 } } } = N _ { \mathrm { { 9 0 } } } = { \frac { a ^ { 2 } } { b } } .
$$

At the equator $\partial / = 0 ^ { \circ } ,$ ) the values are

$$
M _ { _ 0 } = { \frac { b ^ { 2 } } { a } } , N _ { _ 0 } = a .
$$

The curvature of the ellipsoidal normal section with the geodetic azimuth $\alpha$ is computed according to Euler’s formula by

$$
{ \frac { 1 } { R _ { _ { \alpha } } } } = { \frac { \cos ^ { 2 } \alpha } { M } } + { \frac { \sin ^ { 2 } \alpha } { N } } .
$$

Here, $R _ { \alpha }$ is the radius of curvature. The geodetic azimuth $\alpha$ is defi ned as the angle measured in the horizontal plane between the ellipsoidal meridian plane of $P$ and the vertical plane containing the normal to $P$ and the target point; _ $\alpha$ is reckoned from north in the clockwise direction. The mean curvature $\bar { J }$ is given by

$$
\bar { J } = \frac { 1 } { 2 } \Bigl ( \frac { 1 } { M } + \frac { 1 } { N } \Bigr ) .
$$

The arc lengths of the coordinate lines of the $\varphi ,$ $\lambda$ -system are computed using $M$ and $N .$ . For the arc elements of the meridian and the parallel, respectively, we obtain (Fig. 4.4)

$$
d G = M d \varphi , \quad d L = N \cos { \varphi } d \lambda .
$$

With (4.13), the length of the meridian arc (starting at the equator) becomes

$$
G = \int _ { 0 } ^ { \varphi } M d \varphi = a ( 1 - e ^ { 2 } ) \int _ { 0 } ^ { \varphi } { \frac { d \varphi } { ( 1 - e ^ { 2 } { \sin } ^ { 2 } \varphi ) ^ { \frac { 3 } { 2 } } } } .
$$

Equation (4.21a) can be reduced to an elliptic integral of the second kind, which cannot be evaluated in a closed form (Kutterer, 1998). Practical computations may be

based on numerical integration (e.g., by Simpson’s rule) or on a binomial expansion of the denominator. Subsequent term-by-term integration then yields

$$
G = a ( 1 - e ^ { 2 } ) \biggl ( \left( 1 + { \frac { 3 } { 4 } } e ^ { 2 } + \ldots \right) \varphi - \biggl ( { \frac { 3 } { 8 } } e ^ { 2 } + \ldots \biggr ) \sin 2 \varphi + \ldots \biggr ) .
$$

Short arcs $\left( \Delta \varphi = \varphi _ { _ 2 } - \varphi _ { _ 1 } < 1 ^ { \circ } \right)$ ) can be calculated by a rapidly converging Taylor expansion. Expanding about the middle latitude ${ \varphi } _ { { } _ { M } } = \frac { ( { \varphi } _ { 1 } + { \varphi } _ { 2 } ) } { 2 }$ yields

$$
\Delta G _ { _ { 1 , 2 } } = G _ { _ { 2 } } - G _ { _ { 1 } } = \left| \frac { d G } { d \varphi } \right| _ { \varphi _ { _ M } } \Delta \varphi + . . . . .
$$

According to (4.20), the arc length of a circle of latitude between the geodetic longitudes $\lambda _ { \iota }$ and $\lambda _ { _ 2 }$ is given by

$$
\begin{array} { c } { \displaystyle { \Delta L = \int _ { } ^ { \lambda _ { 2 } } N \cos \varphi d \lambda = N \cos \varphi \big ( \lambda _ { 2 } - \lambda _ { 1 } \big ) . } } \\ { \displaystyle { \ a = 6 \ 3 7 8 \ 1 3 7 \ \mathrm { m } , \ b = 6 \ 3 5 6 \ 7 5 2 \ \mathrm { m } , } } \end{array}
$$

With and $e ^ { 2 } = 0 . 0 0 6 6 9 4 3 8 0$ (for numerical values see [4.3]), we get for the radii of curvature at the poles and at the equator

$$
c = 6 ~ 3 9 9 ~ 5 9 4 ~ \mathrm { m } , \quad M _ { o } = 6 ~ 3 3 5 ~ 4 3 9 ~ \mathrm { m } , \quad N _ { o } = a .
$$

The arc lengths along the meridian and the parallel for $\varphi = 5 0 ^ { \circ }$ are

$$
\begin{array} { l l } { { \Delta G ( \Delta \varphi = 1 ^ { \circ } ) = 1 1 1 2 2 9 \mathrm { m } , \qquad } } & { { \Delta L ( \Delta \lambda = 1 ^ { \circ } ) = 7 1 6 9 6 \mathrm { m } , } } \\ { { \Delta G \bigl ( \Delta \varphi = 1 ^ { \prime } \bigr ) = 1 8 5 3 . 8 \mathrm { m } , \qquad } } & { { \Delta L \bigl ( \Delta \lambda = 1 ^ { \prime } \bigr ) = 1 1 9 4 . 9 \mathrm { m } , } } \\ { { \Delta G \bigl ( \Delta \varphi = 1 ^ { \prime \prime } \bigr ) = 3 0 . 9 0 \mathrm { m } , \qquad } } & { { \Delta L \bigl ( \Delta \lambda = 1 ^ { \prime \prime } \bigr ) = 1 9 . 9 2 \mathrm { m } . } } \end{array}
$$

Local approximations to the ellipsoid use the Gaussian osculating sphere of radius

$$
R _ { _ G } = \sqrt { M ( \varphi ) N ( \varphi ) } .
$$

At the latitude $\varphi ,$ it has the same Gaussian curvature as the ellipsoid.

Global approximations can be based on a sphere with the mean radius

$$
R _ { _ { m } } = { \frac { 1 } { 3 } } ( 2 a + b ) ,
$$

the radius derived from equality of volumes (i.e., volume of sphere equals volume of ellipsoid)

$$
R _ { \scriptscriptstyle V } = \sqrt [ 3 ] { a ^ { 2 } b } ,
$$

or the radius for a sphere having a surface area equal to that of the ellipsoid. The latter one results from an integration over the ellipsoidal surface elements $d G$ and $d L$ (4.20), which after a series expansion yields

$$
R _ { s } = b \Big ( 1 + \frac { 2 } { 3 } e ^ { 2 } + \frac { 3 } { 5 } e ^ { 4 } + \ldots \Big ) ^ { 1 / 2 } .
$$

The numerical values for these three approaches agree within a few meters, which leads to a mean global value of $R = 6 3 7 1 ~ { \mathrm { k m } }$ .

# 4.1.3 Spatial geodetic coordinates

The ellipsoidal surface coordinate system $( \varphi , \lambda )$ can be extended to a spatial system by introducing the height $h$ of the point $P$ above the ellipsoid measured along the surface

![](images/f5fb40fd8fda829893d74cfbd7cd5e61aa5e4c6639b1d9c22e62ef200558c9b4.jpg)  
Fig. 4.5: Spatial geodetic coordinates.

normal (Fig. 4.5). The point $Q$ on the ellipsoid thus is obtained by projecting the point $P$ along the ellipsoidal normal: Helmert projection (Grafarend, 2000, 2001). The spatial coordinates $\varphi , \lambda , h$ are designated as geodetic coordinates.

The coordinate surfaces $\varphi =$ const., $\lambda =$ const., $h =$ const.) of this system are orthogonal. The coordinate lines ( $\varphi$ -line $=$ geodetic meridian, $\lambda$ -line $=$ geodetic parallel, $h$ -line $=$ ellipsoidal normal) represent planar curves.

In (4.8) we substitute the fi rst eccentricity $e ^ { 2 }$ for the semi-minor axis $b ,$ taking (4.15) into account; the coordinate vector for the point $Q$ on the ellipsoid (4.8) then transforms into

$$
{ \bar { \bf r } } _ { \mathrm { Q } } = { \left| \begin{array} { l } { \overline { { X } } _ { Q } } \\ { \overline { { Y } } _ { Q } } \\ { \overline { { Z } } _ { Q } } \end{array} \right| } = N \left| \begin{array} { l } { \cos \varphi \cos \lambda } \\ { \cos \varphi \sin \lambda } \\ { \cos \varphi \sin \lambda } \\ { ( 1 - \mathrm { e } ^ { 2 } ) \mathrm { s i n } \varphi } \end{array} \right|  .
$$

For the point $P ,$ we get according to Fig. 4.5

$$
\begin{array} { r } { \overline { { \bf r } } = \overline { { \bf r } } _ { Q } + h \overline { { \bf n } } , } \end{array}
$$

with the surface normal

$$
\overline { { \boldsymbol { \mathsf { n } } } } = \left| \begin{array} { c } { \cos \varphi \cos \lambda } \\ { \cos \varphi \sin \lambda } \\ { \sin \varphi } \end{array} \right| ,
$$

or

$$
{ \bar { \bf r } } = \left| { \frac { \overline { { X } } } { Y } } \right| = { \left| \begin{array} { l l } { ( N + h ) \cos \varphi \cos \lambda } \\ { ( N + h ) \cos \varphi \sin \lambda } \\ { ( ( 1 - e ^ { 2 } ) N + h ) \sin \varphi } \end{array} \right| } .
$$

The inverse problem can be solved for $\varphi$ and $h$ only by iterative methods. From (4.27) we get (e.g., Heiskanen and Moritz, 1967, p. 183)

$$
\begin{array} { l } { { \displaystyle h = \frac { \sqrt { \overline { { { \chi } } } ^ { 2 } + \overline { { { { \cal V } } } ^ { 2 } } } } { \cos \varphi } - N , ~ \varphi = \arctan \frac { \overline { { { { \cal Z } } } } } { \sqrt { \overline { { { \chi } } } ^ { 2 } + \overline { { { { \cal V } } } } ^ { 2 } } } \Big \vert 1 - e ^ { 2 } \frac { N } { N + h } \Big \vert ^ { - 1 } } } \\ { { \lambda = \arctan \frac { \overline { { { \cal Y } } } } { \overline { { { \chi } } } } . } } \end{array}
$$

The iteration process may start with $h = 0$ , which results in a fi rst approximation for $\varphi ,$ and so on. Close to the Earth’s surface $( h < < N )$ the process converges quickly. Closed formulas, with negligible residual errors on the Earth’s surface, are given by Bowring (1985). Effi cient methods have also been developed for large heights (Borkowski, 1989; Sjöberg, 1999). The transformation (4.28) is a standard problem in satellite geodesy, cf. [6.2.1].

Local ellipsoidal (geodetic) systems are introduced in analogy to the local astronomic systems, cf. [2.5], and represent an approximation to them (Fig. 4.6). With the origin at the point $P ,$ the local system is connected to the ellipsoidal vertical (outer surface normal $\bar { \bf n }$ to the ellipsoid) through the geodetic latitude and longitude (4.26b). The $\bar { Z }$ -axis is directed towards the ellipsoidal zenith, with the ${ \bar { x } } ,$ y -plane being perpendicular to it. The $\bar { x }$ -axis points to the ellipsoidal north (direction of the ellipsoidal meridian), and the $\bar { \gamma }$ -axis points towards east (left-handed system).

A target point $P _ { _ i }$ is described with respect to $P$ by the geodetic (ellipsoidal) azimuth $\alpha ,$ introduced in [4.1.2], the ellipsoidal zenith angle $\zeta ,$ and the straight distance $s$ between $P$ and $P _ { _ { i } }$ The zenith angle is measured in the vertical plane between the ellipsoidal vertical and the connecting line and reckoned positively from the zenith. These polar coordinates can be transformed into the local ${ \bar { x } } ,$ y , ${ \bar { Z } } .$ -system by a relation corresponding to (2.20):

$$
{ \overline { { \mathbf { x } } } } = { \left| \begin{array} { l } { { \overline { { x } } } } \\ { { \overline { { y } } } } \\ { { \overline { { z } } } } \end{array} \right| } = s { \left| \begin{array} { l } { \cos \alpha \sin \zeta } \\ { \sin \alpha \sin \zeta } \\ { \cos \zeta } \end{array} \right| } .
$$

![](images/eacf1ff80537ac1d2b73e2782dc62ddafdf8b42bd74250fba6059463d1b8b64d.jpg)  
Fig. 4.6: Global and local ellipsoidal system.

After applying the refl ection matrix _ _ _ $\mathsf { \pmb S } _ { 2 }$ (2.23), the local system is transformed to the global ${ \bar { X } } , { \dot { \bar { Y } } } ,$ ${ \bar { Z } } .$ -system by the rotation matrices $\mathbf { R } _ { 2 } ( 9 0 ^ { \circ } - \varphi )$ and $\begin{array} { r } { \mathbf { R } _ { 3 } ( 1 8 0 ^ { \circ } - \lambda ) , } \end{array}$ , which correspond to (2.24) and (2.25):

$$
\Delta \overline { { \mathbf { X } } } = \overline { { \mathbf { A } } } \overline { { \mathbf { x } } } ,
$$

with

$$
\Delta \overline { { \mathbf { X } } } = ( \Delta \overline { { X } } , \quad \Delta \overline { { Y } } , \quad \Delta \overline { { Z } } ) ^ { T }
$$

and

$$
\begin{array} { l } { { \overline { { \bf A } } = { \bf R } _ { 3 } ( 1 8 0 ^ { \circ } - \lambda ) { \bf R } _ { 2 } ( 9 0 ^ { \circ } - \varphi ) { \bf S } _ { 2 } \nonumber } } \\ { { { \bf \sigma } = \left| - \sin \varphi \cos \lambda { \bf \sigma } - \sin \lambda { \bf \sigma } \cos \varphi \cos \lambda \right| } } \\ { { { \bf \sigma } \cos \varphi \sin \lambda { \bf \sigma } \cos \lambda { \bf \sigma } \cos \varphi \sin \lambda \nonumber } } \\ { { { \bf c o s } \varphi \qquad { \bf 0 } \quad \qquad \sin \varphi . } } \end{array}
$$

The inversion of (4.32) gives

$$
\overline { { \mathbf { x } } } = \overline { { \mathbf { A } } } ^ { - 1 } \Delta \overline { { \mathbf { x } } } ,
$$

with

$$
\begin{array} { r } { \overline { { \mathbf { A } } } ^ { - 1 } = \overline { { \mathbf { A } } } ^ { \top } = \left( \begin{array} { c c c } { - \sin \varphi \cos \lambda } & { - \sin \varphi \sin \lambda } & { \cos \varphi } \\ { - \sin \lambda } & { \cos \lambda } & { 0 } \\ { \cos \varphi \cos \lambda } & { \cos \varphi \sin \lambda } & { \sin \varphi } \end{array} \right) , } \end{array}
$$

which corresponds to (2.28) and (2.29).

# 4.2 The normal gravity fi eld

A “normal” gravity fi eld may be referenced to the rotational ellipsoid by considering the latter to be a “level” ellipsoid, with mass and rotational velocity. This Earth model is now generally accepted as a geodetic reference system; higher order models generally do not offer any advantage [4.2.1]. The external gravity fi eld of the level ellipsoid can be determined unambiguously from the parameters defi ning it [4.2.2]. The geometry of the normal gravity fi eld is of special interest for geodetic applications [4.2.3].

# 4.2.1 The level ellipsoid, level spheroids

We introduce an ellipsoidal gravity fi eld composed of gravitation and centrifugal acceleration: normal gravity fi eld. It is based upon four parameters: total mass $M$ and angular velocity $\omega ,$ and the geometric parameters a and $f$ of the rotational ellipsoid. In addition, we require the surface of this ellipsoid to be a level surface of its own gravity fi eld. According to the theorem of Stokes-Poincaré, the gravity fi eld then is uniquely defi ned in the space exterior to the ellipsoid.

Theorem of Stokes-Poincaré: If a body of total mass $M$ rotates with constant angular velocity $\omega$ about a fi xed axis, and if $S$ is a level surface of its gravity fi eld enclosing the entire mass, then the gravity potential in the exterior space of $S$ is uniquely determined by $M , \omega ,$ and the parameters defi ning $S$ .

The Earth model defi ned in that way is called a level (or equipotential) ellipsoid. Instead of a, $f , M$ and $\omega ,$ other sets of four independent parameters can be used for its defi nition. If the parameters are given values which correspond to the real Earth, then an optimum approximation to the geometry of the geoid and to the external gravity fi eld is achieved: mean Earth ellipsoid, cf. [4.3]. From the physical point of view, an Earth model would be required which is in hydrostatic equilibrium. All its level surfaces then coincide with the surfaces of equal density and equal pressure. Deviations from this model would indicate stress in the Earth’s body, cf. [8.1].

The theory of the level ellipsoid has been developed by P. Pizetti (1894), C. Somigliana (1929), and others (Heiskanen and Moritz, 1967, p. 64). Equilibrium fi gures have been discussed as physical Earth models since the days of Newton and Clairaut, cf. [1.3.2], see Ledersteger (1956/1969), Moritz (1990).

In the above defi nition of the level ellipsoid, nothing has been stated regarding the interior mass distribution. But from the theory of equilibrium fi gures, it follows that only the homogeneous ellipsoids of MacLaurin exist in equilibrium. On the other hand, the surface of an equilibrium fi gure constructed of shells of equal density, and thus corresponding more to the real structure of the Earth, is not an ellipsoid. Nevertheless, a layered structure of the interior mass of the level ellipsoid that approximates the actual situation, and reproduces suffi ciently well the gravity fi eld of the level ellipsoid, can be found (Moritz, 1968a). The maximum deviation between the level surfaces and the surfaces of equal density are at the order of $f ^ { 2 }$ only, and the differences in stress remain considerably smaller for the model than for the real Earth. The level ellipsoid thus can also serve as a bounding surface for a geophysical Earth model (Marussi et al., 1974).

There have been several attempts to construct Earth models with a better fi t to the geoid and the external gravity fi eld than that provided by the level ellipsoid. A physical approximation consists of reference fi gures derived from truncated spherical harmonic expansions of the gravity potential of the Earth: level spheroids, cf. [3.3.2]. By assuming symmetry about the equator and truncating at degree $I = 2$ (Bruns’ spheroid) and $I = 4$ (Helmert’s spheroid), we obtain surfaces of fourteenth and twenty-second order, respectively. The deviations from the rotational ellipsoid having the same length of the axis are on the order of $f ^ { 2 }$ for $I = 2$ , and $f ^ { 3 }$ for $I = 4$ . From the tesseral harmonics of second degree and order, with the harmonic coeffi cients $C _ { _ { 2 , 2 } }$ and $S _ { _ { 2 , 2 ^ { \prime } } }$ the equatorial principal moments of inertia and their directions can be calculated. The results can be used to derive a triaxial ellipsoid, as another geometrical approximation to the geoid.

First attempts in this direction were made by Helmert (1915) and Heiskanen (1924). They were based on the sparse gravity data available at that time, and spherical harmonic expansions of normal gravity derived from them. Recent results stem from Earth gravitational models obtained from satellite methods. They deliver a difference of about $7 0 \textrm { m }$ between the radii of the equatorial principal axes of inertia (corresponding to an equatorial fl attening of about 1/91 000), where the larger radius is directed to $1 4 . 9 ^ { \circ }$ W longitude (Burša, 1995a; Marchenko, 2009).

These higher order Earth models do not signifi cantly reduce the deviations to the geoid, as compared to the level ellipsoid. In addition, computations related to these surfaces and their gravity fi elds become more complicated. Finally, they are generally not suitable as physical normal fi gures. Although, for instance, triaxial rotational ellipsoids exist as equilibrium fi gures (homogeneous ellipsoids of Jacobi), such ellipsoids would yield a completely unnatural form when using the actual values for the angular velocity and mass of the Earth.

# 4.2.2 The normal gravity fi eld of the level ellipsoid

The external gravity fi eld of the level ellipsoid (normal gravity fi eld) can be modeled by closed formulas in the system of ellipsoidal coordinates $\beta , \lambda ,$ u. The reduced latitude $\beta$ and the geodetic longitude $\lambda$ have been already introduced in [4.1.1]. The third coordinate $u$ is the semi-minor axis of the ellipsoid with constant linear eccentricity $\varepsilon ,$ see (4.3), which passes through the point _______ $P$ (Fig. 4.7). From (4.8) and (4.10), and putting $\sqrt { \boldsymbol { u } ^ { 2 } + \boldsymbol { \varepsilon } ^ { 2 } }$ for the semi-major axis, the transformation from the ellipsoidal coordinates to the Cartesian ones is given by

$$
\begin{array}{c} { \left| \begin{array} { l } { { \overline { { X } } } } \\ { { \overline { { Y } } } } \\ { { \overline { { Z } } } } \end{array} \right| } = u \left( { \sqrt { 1 + \left( { \frac { \mathcal { E } } { U } } \right) ^ { 2 } } } \cos \beta \cos \lambda  \\ { \qquad \sin \beta } \end{array} \right) .
$$

For $\varepsilon = 0 ,$ , the $\beta , \lambda ,$ $u \cdot$ -system with $\beta = 9 0 ^ { \circ } - \vartheta$ and $\boldsymbol { u } = \boldsymbol { r }$ reduces into the system of spherical coordinates (2.13).

We denote the vector of normal gravity by $\gamma$ and the normal gravity potential by $U _ { ☉ }$ In analogy to (3.43), we have

$$
\pmb { \gamma } = \operatorname { g r a d } U .
$$

With respect to the surface normal, $\gamma$ is given in analogy to (3.72) by

$$
\pmb { \gamma } = - \gamma \left( \begin{array} { c } { \cos \varphi \cos \lambda } \\ { \cos \varphi \sin \lambda } \\ { \sin \varphi } \end{array} \right) .
$$

Corresponding to (3.42), $U$ is composed of the gravitational potential $V _ { \phantom { } _ { E } }$ and the potential of the centrifugal acceleration $Z _ { \scriptscriptstyle { E } }$ :

$$
\boldsymbol { U } = \boldsymbol { V } _ { E } + \boldsymbol { Z } _ { E } .
$$

![](images/6e5a459094a897b77b47fc58fafc5dbab3abdc2ae688c318b513af90b5bbf7e8.jpg)  
Fig. 4.7: Level ellipsoid and ellipsoidal coordinates.

The gravitational potential satisfi es Laplace’s differential equation (3.29) in the space exterior to the ellipsoid that contains the total mass.

By expressing Laplace’s equation in ellipsoidal coordinates $\beta , \lambda , u ,$ we get a solution for the potential $U ,$ based on ellipsoidal harmonics. Adding the centrifugal potential (3.38), and taking both rotational symmetry and the condition of the ellipsoid surface as a level surface into account, we obtain a closed expression for the normal gravity potential (Heiskanen and Moritz, 1967, p. 64):

$$
U = \frac { G M } { \varepsilon } \arctan \frac { \varepsilon } { u } + \frac { \omega ^ { 2 } } { 2 } a ^ { 2 } \frac { q } { q _ { 0 } } \biggl ( \sin ^ { 2 } \beta - \frac { 1 } { 3 } \biggr ) + \frac { \omega ^ { 2 } } { 2 } \bigl ( u ^ { 2 } + \varepsilon ^ { 2 } \bigr ) \mathrm { c o s } ^ { 2 } \beta .
$$

Here, $q$ is an auxiliary quantity depending only on the geometric parameters $\varepsilon$ and $u$ . On the ellipsoid surface $\langle u = b \rangle$ ), it is denoted $q _ { o } \mathrm { : }$

$$
q = \frac { 1 } { 2 } \biggl ( \left( 1 \ + \ 3 \frac { u ^ { 2 } } { \varepsilon ^ { 2 } } \right) \mathrm { a r c t a n } \frac { \varepsilon } { u } - 3 \frac { u } { \varepsilon } \biggr ) , \ q _ { 0 } = q _ { u = b } .
$$

Hence, in agreement with the Stokes-Poincaré theorem, cf. [4.2.1], the normal gravity potential is determined by the four parameters a, $b , M , \omega .$ It does not depend on the geodetic longitude. If one puts $u = b$ and $q = q _ { o }$ in (4.38), the potential of the level ellipsoid reads

$$
U _ { _ { 0 } } = { \frac { G M } { \varepsilon } } \arctan { \frac { \varepsilon } { b } } + { \frac { \omega ^ { 2 } } { 3 } } a ^ { 2 } .
$$

The normal gravity $\gamma$ is perpendicular to the level ellipsoid, so that in accordance with (4.36), only the orthogonal component appears in the derivative of $U \left( 4 . 3 8 \right)$ . If the geodetic latitude $\varphi$ is used instead of the reduced latitude $\beta ,$ we obtain the formula of Somigliana (1929) for the normal gravity on the ellipsoid

$$
\gamma _ { _ 0 } = \frac { a \gamma _ { _ \mathrm { a } } \cos ^ { 2 } \varphi + b \gamma _ { _ b } \sin ^ { 2 } \varphi } { \sqrt { a ^ { 2 } \cos ^ { 2 } \varphi + b ^ { 2 } \sin ^ { 2 } \varphi } } .
$$

For numerical computations, the form

$$
\gamma _ { \scriptscriptstyle 0 } = \gamma _ { \scriptscriptstyle a } \ \frac { 1 + k \mathrm { s i n } ^ { \mathrm { 2 } } \varphi } { \big ( 1 - e ^ { 2 } \mathrm { s i n } ^ { \mathrm { 2 } } \varphi \big ) ^ { \frac { 1 } { 2 } } } \mathrm { w i t h } \ k = \frac { b \gamma _ { \scriptscriptstyle b } } { a \gamma _ { \scriptscriptstyle a } } - 1
$$

is more convenient (Moritz, 2000).

Here, the normal gravity, which depends on latitude only, is represented by the four parameters a, $b , \ \gamma _ { \mathrm { a } }$ (normal gravity at the equator), and $\gamma _ { b }$ (normal gravity at the pole). The ellipsoidal parameters a, $b ,$ M, w, $\gamma _ { a ^ { \prime } } \mathrm { ~ } \gamma _ { b }$ appearing in (4.38) and (4.41) are interrelated according to the theorem of Pizetti

$$
2 { \frac { \gamma _ { a } } { a } } + { \frac { \gamma _ { b } } { b } } = { \frac { 3 G M } { a ^ { 2 } b } } - 2 \omega ^ { 2 }
$$

and the theorem of Clairaut

$$
f + \beta = \frac { \omega ^ { 2 } \lambda } { \gamma _ { a } } ( 1 + e ^ { \prime 2 } ) ^ { - \frac { 1 } { 2 } } \left( 1 + e ^ { \prime } \frac { 3 \Bigl ( 1 + \displaystyle \frac { 1 } { e ^ { \prime 2 } } \Bigr ) \Bigl ( 1 - \frac { 1 } { e ^ { \prime } } \arctan { e ^ { \prime } } \Bigr ) - 1 } { \Bigl ( 1 + \displaystyle \frac { 3 } { e ^ { \prime 2 } } \Bigr ) \arctan { e ^ { \prime } } - \frac { 3 } { e ^ { \prime } } } \right) .
$$

Thus, again only four independent parameters remain. In (4.43), besides the second eccentricity $e ^ { \prime }$ and the geometric fl attening $f _ { \prime }$ there is also the gravity fl attening

$$
\beta { = } \frac { \gamma _ { _ { b } } - \gamma _ { _ { a } } } { \gamma _ { _ { a } } } .
$$

Remark: The abbreviation $\beta$ is used for both the reduced latitude and the gravity fl attening; confusion is not to be anticipated.

The normal gravity in the exterior space is obtained by partial differentiation of (4.38). Near the ellipsoid, a Taylor series expansion with respect to the ellipsoidal height is suffi cient, see below.

Application of normal gravity fi eld formulas, (4.38) to (4.43), is often facilitated by series expansions with respect to $f _ { \prime }$ or some other quantity that describes the polar fl attening.

We start with the spherical harmonic expansion of the gravitational potential. Due to the symmetry with respect to the rotational axis (tesseral terms are zero) and the equatorial plane (odd zonal terms are zero), we obtain, upon adding the centrifugal potential (3.96a) expressed in spherical coordinates, the potential of normal gravity in terms of Legendre polynomials, cf. [3.3.2],

$$
U = \frac { G M } { r } \Bigg ( 1 - \sum _ { n = 1 } ^ { \infty } \Bigl ( \frac { a } { r } \Bigr ) ^ { 2 n } J _ { 2 n } P _ { 2 n } ( \cos \vartheta ) \Bigg ) + \frac { \omega ^ { 2 } } { 2 } r ^ { 2 } \sin ^ { 2 } \vartheta .
$$

If $P _ { _ 2 }$ is substituted from (3.83a), the expansion up to $n = ~ 1$ (corresponding to the spherical harmonic degree $I = 2$ ) yields an approximation linear in $f$ :

$$
U = \frac { G M } { r } \left( 1 - \left( \frac { a } { r } \right) ^ { 2 } J _ { 2 } \left( \frac { 3 } { 2 } \mathrm { { C O S } } ^ { 2 } \vartheta - \frac { 1 } { 2 } \right) + \frac { \omega ^ { 2 } } { 2 G M } r ^ { 3 } \mathrm { { s i n } } ^ { 2 } \vartheta \right) .
$$

Solving for $r$ and setting $U = U _ { o }$ gives the radius vector to the level ellipsoid, where we have put $r = a$ on the right-hand side:

$$
r = \frac { G M } { U _ { 0 } } \Bigg ( 1 - J _ { 2 } \Big ( \frac { 3 } { 2 } \mathrm { C O S } ^ { 2 } \vartheta - \frac { 1 } { 2 } \Big ) + \frac { \omega ^ { 2 } a ^ { 3 } } { 2 G M } \mathrm { S i n } ^ { 2 } \vartheta \Bigg ) .
$$

The normal gravity $\gamma$ follows from the derivative of (4.46) with respect to $r$

$$
\gamma = \frac { G M } { r ^ { 2 } } \Bigg ( 1 - 3 \Big ( \frac { a } { r } \Big ) ^ { 2 } J _ { 2 } \left( \frac { 3 } { 2 } \mathrm { c o s } ^ { 2 } \vartheta - \frac { 1 } { 2 } \right) - \frac { \omega ^ { 2 } } { G M } r ^ { 3 } \mathrm { s i n } ^ { 2 } \vartheta \Bigg ) .
$$

If we substitute either $\vartheta = 9 0 ^ { \circ }$ (equator) or $0 ^ { \circ }$ (pole) in (4.47) and (4.48), then we obtain either the semi-major axis a and the equatorial gravity or the semi-minor axis $b$ and the polar gravity of the ellipsoid. Using these values, the geometric fl attening $f$ (4.1a) and the gravity fl attening $\beta ( 4 . 4 4 )$ may be computed according to

$$
f = \frac { 3 } { 2 } J _ { 2 } + \frac { m } { 2 } , \quad \beta = - \frac { 3 } { 2 } J _ { 2 } + 2 m .
$$

Here,

$$
m = \frac { \omega ^ { 2 } a } { \gamma _ { a } }
$$

is the ratio of the centrifugal acceleration to the normal gravity at the equator, a rigorous formula is given by (4.56).

From (4.48) and (4.49), we arrive at an approximation to the theorem of Pizetti (4.42)

$$
G M = a ^ { 2 } \gamma _ { a } \left( 1 - f + \frac { 3 } { 2 } m \right)
$$

and an approximation to Clairaut’s theorem (4.43)

$$
f + \beta = { \frac { 5 } { 2 } } m .
$$

Substituting (4.49) and (4.50) into (4.48), we obtain Newton’s gravity formula, cf. [1.3.2]:

$$
\begin{array} { r } { \gamma _ { \mathrm { 0 } } = \gamma _ { \mathrm { a } } \vert 1 + \beta \sin ^ { 2 } \varphi \vert . } \end{array}
$$

If two $\gamma _ { _ { 0 } }$ gravity values are known on the ellipsoid (gravity reduction problem!) at different geographic latitudes $\varphi ,$ then $\gamma _ { _ { \mathrm { a } } }$ and $\beta$ may be computed from (4.53). With known values for the semi-major axis a and the angular velocity $\omega ,$ (4.50) supplies the quantity $m$ . Finally, Clairaut’s theorem (4.52) yields the geometric fl attening $f _ { \prime }$ which thus can be determined from gravity values. Application of this principle to the real Earth – that is, deriving geometric form parameters from physical quantities – leads to the gravimetric method of physical geodesy, cf. [6.5.1].

The relations above (linear in $f , \beta ,$ and $m _ { \ l }$ ) may also be derived by series expansions of the closed formulas. They had already been found by Clairaut (“Théorie de la Figure de la Terre” 1743). The expansion up to terms of the order $f ^ { 2 }$ yields (IAG, 1971)

$$
\begin{array} { l } { { f = \displaystyle \frac { 3 } { 2 } J _ { 2 } + \frac { m } { 2 } + \frac { 9 } { 8 } J _ { 2 } ^ { 2 } + \frac { 1 5 } { 2 8 } J _ { 2 } m + \frac { 3 } { 5 6 } m ^ { 2 } , } } \\ { { \beta = - f + \displaystyle \frac { 5 } { 2 } m - \frac { 1 7 } { 1 4 } { f m } + \frac { 1 5 } { 4 } m ^ { 2 } , } } \\ { { m = \displaystyle \frac { \omega ^ { 2 } a ^ { 2 } b } { G M } , } } \\ { { \gamma _ { 0 } = \gamma _ { a } \big ( 1 + \beta \mathrm { s i n } ^ { 2 } \varphi + \beta _ { 1 } \mathrm { s i n } ^ { 2 } 2 \varphi \big ) , \beta _ { 1 } = \frac { 1 } { 8 } f ^ { 2 } - \frac { 5 } { 8 } f m . } } \end{array}
$$

One of the fi rst applications of Clairaut’s theorem was made by Helmert (1901). An adjustment of about 1400 free-air reduced gravity values to the gravity formula (4.57) yielded the parameters $\gamma _ { _ { \mathrm { a } } } = 9 . 7 8 0 3 \mathrm { ~ m } s ^ { - 2 }$ and $\beta = 0 . 0 0 5 ~ 3 0 2$ , with a fl attening of $f = 1 / 2 9 8 . 3$ .

The harmonic coeffi cients of second and fourth degree may be computed from $f$ and $m$ as follows:

$$
J _ { 2 } = \frac { 2 } { 3 } f - \frac { m } { 3 } - \frac { 1 } { 3 } f ^ { 2 } + \frac { 2 } { 2 1 } f m , \quad J _ { 4 } = - \frac { 4 } { 5 } f ^ { 2 } + \frac { 4 } { 7 } f m .
$$

For today’s accuracy requirements, an expansion up to $n = 3$ (corresponding to $I =$ 6) is generally adequate. That is, the expansion has to include the terms of the order $f ^ { 3 }$ (Cook, 1959). Developments up to the order $f ^ { 5 }$ have been given by Chen (1982).

Near the Earth’s surface, a Taylor series expansion with respect to the ellipsoidal height $h$ is suffi cient for the derivation of the normal gravity in the exterior space:

$$
\gamma = \gamma _ { \scriptscriptstyle 0 } + \left| \frac { \partial \gamma } { \partial h } \right| _ { \scriptscriptstyle 0 } h + \frac { 1 } { 2 } \left| \frac { \partial ^ { 2 } \gamma } { \partial h ^ { 2 } } \right| _ { \scriptscriptstyle 0 } h ^ { 2 } + \frac { 1 } { 6 } \left| \frac { \partial ^ { 3 } \gamma } { \partial h ^ { 3 } } \right| _ { \scriptscriptstyle 0 } h ^ { 3 } + . . . .
$$

The partial derivative $\frac { \partial \gamma } { \partial h }$ is obtained by applying Bruns’ equation (3.71) to the exterior space:

$$
\frac { \partial \gamma } { \partial h } = - 2 \gamma { \bar { J } } - 2 \omega ^ { 2 } ,
$$

where $\bar { \boldsymbol { J } }$ is the mean curvature of the ellipsoid (4.19). A series expansion up to the order of $f$ leads to the vertical component of the normal gravity gradient

$$
\frac { \partial \gamma } { \partial h } = - 2 \frac { \gamma } { a } \big ( 1 + f + m - 2 f \mathsf { s i n } ^ { 2 } \varphi \big ) .
$$

The second and the third derivative can be derived from a spherical approximation of $\gamma$ where $\partial \gamma / \partial h = \partial \gamma / \partial r$ etc., see (3.17). With

$$
\gamma = \frac { G M } { r ^ { 2 } } , \frac { \partial \gamma } { \partial r } = - 2 \frac { G M } { r ^ { 3 } } = - 2 \frac { \gamma } { r }
$$

we obtain

$$
\frac { \partial ^ { 2 } \gamma } { \partial r ^ { 2 } } = \frac { 6 G M } { r ^ { 4 } } = 6 \frac { \gamma } { r ^ { 2 } } , \frac { \partial ^ { 3 } \gamma } { \partial r ^ { 3 } } = - 2 4 \frac { G M } { r ^ { 5 } } = - 2 4 \frac { \gamma } { r ^ { 3 } } .
$$

Inserting the above into (4.59), with $r = a$ and $\gamma = \gamma _ { _ { 0 ^ { \prime } } }$ leads to the normal gravity as a function of latitude and height:

$$
\gamma = \gamma _ { \scriptscriptstyle 0 } \Big ( 1 - \frac { 2 } { a } ( 1 + f + m - 2 f \mathsf { s i n } ^ { 2 } \varphi ) h + \frac { 3 } { a ^ { 2 } } h ^ { 2 } \Big ) + . . . . ,
$$

where the $h ^ { 3 }$ -term has to be added for higher altitudes. Airborne and satellite applications require rigorous formulas, at which $\gamma$ is derived by differentiating the normal gravity potential (4.38). The results are given in the $\beta , \lambda ,$ u-system, and can be easily transformed into a three-dimensional Cartesian coordinate system (4.35), cf. Hofmann-Wellenhof and Moritz (2005, p. 240 ff.).

With $\gamma = 9 . 8 1 \mathrm { ~ m } \mathrm { s } ^ { - 2 }$ and $a \ = \ 6 3 7 8 \ \mathrm { k m } ,$ , we get $\frac { \partial \gamma } { \partial h } = - 3 . 0 8 6 \mu \mathrm { m } s ^ { - 2 } / \mathrm { m }$ and $\frac { \partial ^ { 2 } \gamma } { \partial h ^ { 2 } } =$ $1 . 5 \times 1 0 ^ { - 6 } \mu \mathrm { m } { s } ^ { - 2 } / \mathrm { m } ^ { 2 }$ . More detailed numerical values are given in [4.3]. In gravity reductions the value $- 3 . 0 8 6 \mu \mathrm { m } s ^ { - 2 } / \mathrm { m }$ is used conventionally.

# 4.2.3 Geometry of the normal gravity fi eld

The geometry of the normal gravity fi eld is represented by the spheropotential surfaces and the normal plumb lines.

The spheropotential surfaces are surfaces of constant normal gravity potential

$$
U = U ( { \bf r } ) = \mathrm { c o n s t . }
$$

With the exception of the surface of the level ellipsoid ${ \cal U } = { \cal U } _ { o } )$ , spheropotential surfaces deviate from ellipsoids and are not parallel to each other. The normal plumb lines intersect the spheropotential surfaces orthogonally. Due to the non-parallelism of the level surfaces, they are slightly curved in the plane of the meridian (Fig. 4.8).

In order to describe the geometry of the normal gravity fi eld, “normal” geodetic coordinates $\varphi ^ { N } , \lambda ^ { N } ,$ $U$ are introduced. They are defi ned in analogy to the “natural” coordinates $\vartheta , \Lambda , W$ of the actual gravity fi eld, cf. [3.2.3]. The normal geodetic coordinates refer to the point $Q ,$ which is related to the surface point $P \left( \Phi , \Lambda , W \right)$ by the conditions:

$$
\varphi _ { _ Q } ^ { N } = \Phi _ { _ P } , \quad \lambda _ { _ Q } ^ { N } = \Lambda _ { _ P } , \quad U _ { _ Q } = W _ { _ P } .
$$

The surface thus defi ned in a point-wise manner approximates the physical surface of the Earth, with deviations less than $1 0 0 ~ \mathrm { { m } }$ and less than one arcmin, respectively. This surface is called the telluroid (Hirvonen, 1960). It is not a level surface of the normal gravity fi eld, but it resembles the Earth’s surface.

The normal geodetic latitude $\varphi ^ { N }$ is the angle measured in the meridian plane between the equatorial plane of the ellipsoid and the direction of the normal plumb line. It differs from the geodetic latitude $\varphi ,$ introduced in [4.1.1], by the small angle $\delta \varphi ^ { N } .$ . This difference is a result of the normal plumb line curvature, see below. The normal geodetic longitude $\lambda ^ { N }$ is equal to the geodetic longitude $\lambda .$ . The normal gravity potential $U$ relates the point $Q$ to the level surface $U = U _ { _ Q }$ .

![](images/638a82b951edb117f38353113e084565750b1f06919f66c88e80ff7c9c1f14a3.jpg)  
Fig. 4.8: Spheropotential surfaces, normal plumb line, normal height.

Instead of $U ,$ the potential difference $U _ { \scriptscriptstyle 0 } - U _ { \scriptscriptstyle Q }$ to the level ellipsoid may be used for that purpose. With $U _ { . Q } = W _ { P ^ { \prime } } . $ and the condition $U _ { 0 } = W _ { 0 ^ { \prime } }$ cf. [6.5.4], we obtain the normal height $H ^ { N }$ already introduced in [3.4.3]:

$$
H ^ { N } = \frac { U _ { 0 } - U _ { Q } } { \bar { \gamma } } = \frac { W _ { 0 } - W _ { P } } { \bar { \gamma } } .
$$

Hence, $H ^ { N }$ is defi ned as the distance between $Q$ and the level ellipsoid measured along the normal plumb line. To a good approximation, $H ^ { N } \mathrm { m a y }$ be measured along the_ ellipsoidal normal passing through the surface point. According to $( 3 . 1 0 7 ) , \overline { { \gamma } }$ is the mean normal gravity between the ellipsoid and $Q$ . Substituting $\gamma$ from (4.63) into (3.107) and integrating yields

$$
\overline { { { \gamma } } } = \gamma _ { _ 0 } \left( 1 - \frac { 1 } { a } \left( 1 + t + m - 2 t \mathrm { s i n } ^ { 2 } \varphi \right) H ^ { N } \right) .
$$

Hence, $\bar { \gamma }$ may be computed rigorously in an iterative manner. Since $C$ can be derived from measurements, the normal height can be determined without any hypothesis. Extending the normal heights downward from the Earth’s surface yields the quasigeoid, which is used as a reference surface for heights, cf. [3.4.3].

The normal geodetic coordinates $\varphi ^ { N } , \lambda ^ { N } , H ^ { N }$ have gained special importance for the direct determination of the physical surface of the Earth according to the theory of Molodensky, cf. [6.5.1], [6.7.2]. Normal heights have been introduced for a number of national height systems, cf. [7.2].

The curvature of the spheropotential surfaces is described by the second derivatives of $U ,$ in analogy to the actual gravity fi eld, see (3.57), (3.58). In the local ellipsoidal system, the curvatures in the direction of the meridian and the parallel are given by

$$
k _ { \frac { \overline { { { x } } } } { \bar { x } } } ^ { N } = - \frac { U _ { \frac { \overline { { { x } } } \overline { { { x } } } } } } { \gamma } , k _ { \frac { \bar { N } } { \bar { y } } } ^ { N } = - \frac { U _ { \frac { \overline { { { y } } \bar { y } } } { \gamma } } } { \gamma } .
$$

The geodetic torsion is zero due to the rotational symmetry of the level ellipsoid:

$$
t _ { \overline { { x } } } ^ { N } = - \frac { U _ { \overline { { x y } } } } { \gamma } = 0 .
$$

On the ellipsoid, the curvature is given by the principal radii of curvature $M$ and $N ,$ see (4.13), (4.14):

$$
k _ { \overline { { { x } } } ( 0 ) } ^ { N } = \frac { 1 } { M } , \quad k _ { \overline { { { y } } } ( 0 ) } ^ { N } = \frac { 1 } { N } .
$$

Following (3.67), and taking the rotational symmetry into account, we get for the_ _ _ _ curvature of the projections of the normal plumb line onto the ${ \overline { { x } } } , { \overline { { z } } } -$ and the ${ \overline { { y } } } ,$ ${ \overline { { Z } } } .$ -plane, respectively:

$$
\kappa _ { \frac { \overline { { { x } } } } { \overline { { { x } } } } } ^ { N } = - \frac { U _ { \frac { \overline { { { x } } } \overline { { { z } } } } { \gamma \mathrm { ~ , ~ } } } } { \gamma \mathrm { ~ , ~ } } \kappa _ { \frac { \overline { { { y } } } } { \overline { { { y } } } } } ^ { N } = - \frac { U _ { \frac { \overline { { { y } } } \overline { { { z } } } } { \overline { { { y } } } \overline { { { z } } } } } } { \gamma } = 0 .
$$

On the level ellipsoid, we have with (4.20)

$$
U _ { \overline { { { x z } } } ( 0 ) } = - \left. \frac { \partial \gamma } { \partial \overline { { { x } } } } \right. _ { 0 } = - \left. \frac { \partial \gamma } { M \partial \varphi } \right. _ { 0 } .
$$

Introducing the derivative $\frac { \partial { \gamma } } { \partial { \varphi } }$ from (4.53) and inserting into (4.71) yields with suffi cient approximation

$$
\kappa _ { \overline { { { x } } } ( 0 ) } ^ { N } = \frac { \beta } { M } \sin 2 \varphi
$$

with gravity fl attening $\beta ( 4 . 4 4 )$ . For the change of the normal gravity along the meridian, we thus get

$$
\left( { \frac { \partial \gamma } { \partial { \bar { x } } _ { \mathrm { { o } } } } } \right) = \gamma { \frac { \beta } { M } } { \sin } 2 \varphi = 8 . 2 \times 1 0 ^ { - 9 } \sin 2 \varphi \mathrm { { m } } { \mathrm { { s } } ^ { - 2 } } / \mathrm { { m } }
$$

which corresponds to $8 . 2 ~ \mathrm { { n m s ^ { - 2 } / m } }$ at $\varphi = 4 5 ^ { \circ }$ . Together with the relation $U _ { \overline { { { z z } } } } = - \frac { \partial \gamma } { \partial \overline { { { z } } } } ,$ , (4.68) to (4.72) completely defi ne the Eötvös tensor (3.69) for the normal gravity fi eld. According to (3.75), the differential transformation from the local to the global geodetic system is also provided by the curvature parameters.

Finally, we derive the differences between the geodetic coordinates $\varphi , \lambda$ and the normal geodetic coordinates $\varphi ^ { N } , \lambda ^ { N }$ :

$$
\varphi = { \varphi } ^ { N } + 8 { \varphi } ^ { N } , \quad \lambda = { \lambda } ^ { N } .
$$

From (4.71) and (4.72) we obtain

$$
d \varphi ^ { N } = - \int \displaylimits _ { 0 } ^ { H ^ { N } } { \kappa _ { \bar { x } } ^ { N } d H ^ { N } } = - \frac { \beta } { M } \sin 2 \varphi H ^ { N } .
$$

And with $\beta = 0 . 0 0 5 3$ and $M \approx a = 6 3 7 1 ~ \mathrm { k m }$ we get

$$
{ \delta \varphi } ^ { N } = - 0 . 0 0 0 ~ 1 7 ^ { \prime \prime } \sin 2 \varphi { \cal H } ^ { N } ,
$$

where $H ^ { N }$ is in meters.

# 4.3 Geodetic reference systems, optimum Earth model

Geodetic reference systems provide numerical values for the parameters of a geodetic Earth model. The systems are recommended by the International Union of Geodesy and Geophysics (IUGG) and represent the best parameter values for a designated epoch. The systems generally serve as a standard over a longer time span for geodesy and related disciplines such as astronomy, cartography, geophysics, engineering, and navigation.

All reference systems are supposed to be geocentric, with the Z-axis coinciding with the Earth’s axis of rotation and the direction of the $\chi .$ -axis pointing to the Greenwich meridian. While the earlier reference systems may have large deviations from the geocentric system, recent reference systems agree at the $^ { \prime \prime } { \mathrm { C } } { \sf m } ^ { \prime \prime }$ -level. The orientation of geodetic systems with respect to the Earth is described by the “Geodetic Datum”, cf. [6.2.2].

In the nineteenth and early twentieth century, the geometric parameters of reference ellipsoids were derived from various terrestrial data sets and then introduced as a reference for national geodetic surveys, cf. [1.3.3]. Normal gravity formulae referred to these ellipsoids have been derived since about 1900 and used for national gravimetric surveys. These regional or local reference systems may be regarded as precursors of the present global systems, which are based on the theory of the level ellipsoid.

Geodetic reference systems based on the theory of the level ellipsoid were fi rst introduced in 1924/1930. At the IUGG General Assembly in Madrid 1924, Hayford’s ellipsoid was introduced as the International Ellipsoid, with the parameters

$$
a = 6 3 7 8 3 8 8 { \mathrm { m } } , \ f = 1 / 2 9 7 . 0 .
$$

The General Assembly in Stockholm (1930) adopted the gravity formula established by $G$ . Cassinis for Hayford’s ellipsoid:

$$
\gamma _ { \scriptscriptstyle 0 } = 9 . 7 8 0 ~ 4 9 \big ( 1 + 0 . 0 0 5 ~ 2 8 8 4 \sin ^ { 2 } \varphi - 0 . 0 0 0 ~ 0 0 5 9 \sin ^ { 2 } 2 \varphi \big ) \mathrm { m } s ^ { - 2 } .
$$

This corresponds to the normal gravity formula (4.57), assuming a level ellipsoid.

The geometric parameters a and f were calculated by J. F. Hayford (1909) from astrogeodetic observations in the U.S.A. In 1928, W. A. Heiskanen determined the equatorial gravity from an adjustment of isostatically reduced gravity values. The international reference system of $1 9 2 4 / 1 9 3 0$ is thus defi ned by the four parameters a, $f , \ \gamma _ { \mathrm { a ^ { \prime } } }$ w. The corresponding ellipsoid has been applied in numerous geodetic surveys; also, the normal gravity formula has found broad acceptance.

At the General Assembly of the IUGG in Luzern (1967), the 1924/1930 reference system was replaced by the Geodetic Reference System 1967 (GRS67), see IAG (1971). It was defi ned by the following parameters:

$$
a = 6 \ 3 7 8 \ 1 6 0 \ \mathrm { m } , \ G M = 3 9 8 \ 6 0 3 \times 1 0 ^ { 9 } \mathrm { m } ^ { 3 } s ^ { - 2 } , \ J _ { 2 } = 1 0 8 2 . 7 \times 1 0 ^ { - 6 } .
$$

The angular velocity of the Earth’s rotation

$$
\omega = 7 . 2 9 2 \ 1 1 5 \ 1 4 6 \ 7 \times 1 0 ^ { - 5 } \mathrm { r a d s } ^ { - 1 } ,
$$

not mentioned in the IUGG resolution, was adopted as the fourth parameter. The reference ellipsoid corresponding to this defi nition was declared a level ellipsoid.

The calculation of the semi-major axis was based on astrogeodetic observations collected over the continents, which were transformed into a uniform system by gravimetric methods.

Observations of space probes yielded the geocentric gravitational constant, which includes the mass of the atmosphere. The dynamic form factor was derived from the orbit perturbations of artifi cial satellites, and the angular velocity of the Earth’s rotation was adopted from astronomy. The GRS67 has been used especially for scientifi c problems and for a few geodetic networks.

At the IUGG General Assembly in Canberra (1979), the Geodetic Reference System 1980 (GRS80) was introduced. It is also based on the theory of the geocentric equipotential ellipsoid, with the defi ning parameters (Moritz, 2000):

$$
{ \begin{array} { l l } { a = 6 ~ 3 7 8 ~ 1 3 7 \mathsf { m } } & { { \mathrm { e q u a t o r i a l ~ r a d i u s ~ o f ~ t h e ~ E a r t h } } } \\ { G M = 3 9 8 ~ 6 0 0 . 5 \times 1 0 ^ { 9 } \mathsf { m } ^ { 3 } s ^ { - 2 } } & { { \mathrm { g e o c e n t r i c ~ g r a v i t a t i o n a l } } } \\ & { { \mathrm { c o n s t a n t ~ o f ~ t h e ~ E a r t h } } } \\ & { ( { \mathrm { i n c l u d i n g ~ t h e ~ a t m o s p h e r e } } ) } \\ { J _ { 2 } = 1 0 8 2 . 6 3 \times 1 0 ^ { - 6 } } & { { \mathrm { d y n a m i c a l ~ f o r m ~ f a c t o r ~ o f ~ t h e } } } \\ & { { \mathrm { E a r t h ~ ( e x c l u d i n g ~ t h e ~ p e r m a n e n t } } } \\ & { { \mathrm { t i d a l ~ d e f o r m a t i o n ) } } } \end{array} }
$$

With $M _ { \mathrm { a t m } } = 0 . 8 8 \times 1 0 ^ { - 6 } M ,$ we have $G M _ { _ { \mathrm { a t m } } } = 0 . 3 5 \times 1 0 ^ { 9 } \mathrm { m } ^ { 3 } \mathrm { s } ^ { - 2 }$ .

With respect to the orientation, it is stated that the minor axis of the reference ellipsoid be parallel to the direction defi ned by the Conventional International Origin and that the primary meridian be parallel to the zero meridian of the BIH adopted longitudes, cf. [2.3].

The system is consistent with the IAU system of astronomical constants, cf. [2.3.1], [2.3.2]. It is now widely used as a reference for geodetic work, in theory as well as in practice.

The equatorial radius of the GRS80 ellipsoid has been derived from laser distance measurements to satellites, satellite altimetry, and Doppler positioning, with an uncertainty of $_ { 0 . 5 \mathrm { ~ m ~ } }$ . The calculation of the geocentric gravitational constant was based on space probes and lunar and satellite laser data ( $\pm 0 . 0 5 \times 1 0 ^ { 9 } \mathrm { { m } ^ { 3 } \mathrm { { s } ^ { - 2 } } }$ ), while the value for the dynamic form factor was taken from global gravity models $\pm 5 \times 1 0 ^ { - 9 } .$ ). Again, the angular velocity of the Earth is a value derived from annual means over the last decades; velocity variations with time do not affect this rounded value (Burša, 1995a).

Numerical values for derived parameters include (Moritz, 2000): Geometric constants, cf. [4.1.1], [4.1.2]:

$b = 6 \ 3 5 6 \ 7 5 2 . 3 1 4 1 \ \mathrm { m }$ $\varepsilon = 5 2 1 ~ 8 5 4 . 0 0 9 7 ~ \mathrm { m }$ $C = 6 \ 3 9 9 \ 5 9 3 . 6 2 5 9 \ \mathrm { m }$ $e ^ { 2 } = 0 . 0 0 6 6 9 4 3 8 0 0 2 2 9 0$ $e ^ { \cdot 2 } = 0 . 0 0 6 7 3 9 4 9 6 7 7 5 4 8$ f = 0.003 352 810 681 18 $1 / t = 2 9 8 . 2 5 7 ~ 2 2 2 ~ 1 0 1$ $G = 1 0 \ 0 0 1 \ 9 6 5 . 7 2 9 3 \ \mathrm { m }$

semi-minor axis   
linear eccentricity (4.3)   
polar radius of curvature (4.16)   
fi rst eccentricity (e) (4.1b)   
second eccentricity (e) (4.1c)   
fl attening (4.1a)   
reciprocal fl attening   
meridian quadrant (4.21a)

Physical constants, cf. [4.2.2]:

normal potential at ellipsoid (4.40)

normal gravity at equator (4.41)

Normal gravity can be computed by the closed formula (4.41) or the series expansion

$$
\gamma _ { _ { 0 } } = \gamma _ { _ { a } } \left( \begin{array} { c } { { 1 + 0 . 0 0 5 \ 2 7 9 \ 0 4 1 4 \mathrm { s i n } ^ { 2 } \varphi + 0 . 0 0 0 \ 0 2 3 \ 2 7 1 8 \mathrm { s i n } ^ { 4 } \varphi } } \\ { { + \ 0 . 0 0 0 \ 0 0 0 \ 1 2 6 2 \mathrm { s i n } ^ { 6 } \varphi + 0 . 0 0 0 \ 0 0 \ 0 0 0 7 \mathrm { s i n } ^ { 8 } \varphi , } } \end{array} \right)
$$

which is accurate to $1 0 ^ { - 3 } \mu \mathrm { m } \mathsf { s } ^ { - 2 }$ . The conventional series (4.57) has an accuracy of $1 ~ { \mu \mathrm { m } } ^ { - 2 }$ :

$$
\gamma _ { \scriptscriptstyle 0 } = 9 . 7 8 0 ~ 3 2 7 \big ( 1 + 0 . 0 0 5 ~ 3 0 2 4 \mathrm { s i n } ^ { 2 } \varphi - 0 . 0 0 0 ~ 0 0 5 8 \mathrm { s i n } ^ { 2 } 2 \varphi \big ) \mathrm { m } \mathrm { s } ^ { - 2 } .
$$

Inserting the values for the GRS80 into (4.63) yields the change of normal gravity with height:

$$
\gamma = \gamma _ { \scriptscriptstyle 0 } - \left( 3 . 0 8 7 7 \times 1 0 ^ { - 3 } - 4 . 3 \times 1 0 ^ { - 6 } { \sin ^ { 2 } \varphi } \right) h + 0 . 7 2 \times 1 0 ^ { - 6 } h ^ { 2 } \mathrm { m } { s ^ { - 2 } }
$$

with $h$ in km. A development accurate to $1 0 \ \mathrm { n m s ^ { - 2 } }$ for heights up to $1 0 ~ \mathrm { k m }$ is given by Wenzel (1989).

According to the defi nition of $G M , \ \gamma _ { \mathrm { { o } } }$ refers to the total mass of the Earth including the atmosphere. If normal gravity values are required on the ellipsoid, or within the range of the atmosphere, the effect of the air masses above the calculation point must be subtracted from $\gamma _ { _ { 0 } }$ . The corresponding reduction amounts to $- 8 . 7 \mu \mathrm { m } \mathsf { s } ^ { - 2 } ( \dot { h } = 0 ) ,$ , $- 4 . 7 \mu \mathrm { m } \ s ^ { - 2 }$ $( h = 5 { \mathrm { k m } } )$ , and $- 0 . 1 \ \mu \mathrm { m } s ^ { \dot { - } 2 } ( h = 3 0 \ \ k m )$ , cf. Ecker and Mittermayer (1969).

There is a lasting discussion to replace the semi-major axis a as one of the defi ning (or primary) parameters of the Geodetic Reference System by the normal potential $U _ { 0 }$ on the level ellipsoid, set equal to the geoid potential value $W _ { 0 }$ (Burša, 1992). As $W _ { 0 }$ has a physical meaning (contrary to a), the whole set of defi ning parameters would be physically welldefi ned. In addition, $W _ { 0 }$ is a relevant quantity at recent problems, as the defi nition of a world height system and as a reference for time defi nition and precise time keeping, under the aspect of General Relativity, cf. [3.4.3] and [2.2.1], respectively. Finally, $W _ { 0 }$ does not depend on the permanent tidal effect, cf. [3.4.1], Burša (1995b). A “geopotential scale factor” $R _ { \mathrm { 0 } } =$ $G M W _ { 0 }$ can be derived from $W _ { 0 ^ { \prime } }$ and used instead of it. The semi-major axis of a best-fi tting ellipsoid can be calculated on the basis of (4.40) and corresponding series developments (Burša et al., 1998). The geopotential value on the geoid is now well determined from longterm satellite altimetry data, cf. [3.4.3].

Optimum values for the Earth model parameters are determined at shorter time intervals and published by the International Association of Geodesy and the International Astronomical Union. The values are derived from least-squares adjustments employing satellite tracking, satellite gravity gradiometry, satellite altimetry, and terrestrial gravi metry, and refer to a level ellipsoid which fi ts best to the geoid. Of special importance are the IERS numerical standards, given in the IERS Conventions (Groten, 2004; Petit and Luzum, 2010). According to these standards, the currently best estimates for the defi ning parameters of a level ellipsoid are as follows:

• The geocentric gravitational constant $G M = ( 3 9 8 ~ 6 0 0 . 4 4 2 ~ \pm ~ 0 . 0 0 1 ) \times 1 0 ^ { 9 } \mathrm { m } ^ { 3 } \mathrm { s } ^ { - 2 }$ including the mass of the atmosphere. This value is derived from orbit analyses of satellites and space probes. A variation of GM with time has not been found.   
The equatorial radius of the Earth $a = 6 3 7 8 1 3 6 . 6 \pm 0 . 1 \ m .$ The radius is derived from an optimum fi t between ellipsoidal heights, as obtained for satellite tracking stations, and from satellite altimetry, applying the minimum condition $\iint N ^ { ' } d \sigma = \operatorname* { m i n }$ . on the geoid heights. It is valid for the zero-frequency as well as for the tide-free system, cf. [3.4.1], and assumed to be constant with time.   
The second-degree zonal harmonic coeffi cient (dynamical form factor) $J _ { , = } \{ ( 1 0 8 2 . 6 2 6 \bar { 7 } \quad \pm \quad 0 . 0 0 0 1 ) \quad \times \quad 1 0 ^ { - 6 }$ in the tide-free system, and $J _ { 2 } =$ $\overline { { 1 } } 0 8 2 . 6 3 5 9 \pm 0 . 0 0 0 1 ) \times 1 0 ^ { - 6 }$ in the zero-tide system. $J _ { 2 }$ is obtained from global gravitational fi eld models. Temporal variations of the dynamical form factor have been signifi cantly determined, cf. [8.3.5]. The mean angular velocity of the Earth’s rotation $\omega = 7 . 2 9 2 \ 1 1 5 \times 1 0 ^ { - 5 } \mathsf { r a d s } ^ { - 1 }$ is provided by the IERS, cf. [2.2.2]. For long-term variations see [8.3.2].

Among the quantities derived from the defi ning parametrs we have

• The geoid potential $W _ { \scriptscriptstyle 0 } \mathrm { = } 6 2 ~ 6 3 6 ~ 8 5 6 . 0 \pm 0 . 5 ~ \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 2 }$ . As discussed above, the potential may also be introduced instead of a as defi ning parameter, and it is also constant with time. The reciprocal fl attening $1 / f = 2 9 8 . 2 5 6 4 2 \pm 0 . 0 0 0 0 1$   
• The normal gravity at the equator $\gamma _ { _ { a } } = 9 . 7 8 0 \ 3 2 8 \pm 0 . 0 0 0 \ 0 0 2 \mathrm { m } \mathrm { s } ^ { - 2 } ,$ , both given in the zero-tide system.

# 5 Methods of Measurement

Modeling of geodetically relevant quantities (especially coordinates, gravity fi eld quantities, and Earth rotation parameters) is based on observations taken on the Earth’s surface and in its exterior space. Different measurement methods are available, delivering geometric or physical quantities. Geometric methods rely primarily on electromagnetic waves and thus are affected by atmospheric refraction [5.1]. The measurement methods may be divided into

observations employing artifi cial satellites as targets (including the moon), sensors or carriers of sensors: satellite observations [5.2], . observations to fi xed stars and extragalactic radio sources: geodetic astronomy [5.3], terrestrial gravity and gravity gradient measurements: gravimetry [5.4], and determination of coordinate differences between points on the surface of the Earth: terrestrial geodetic measurements [5.5].

The measurement methods depend on available technology, where electronics governs data collection and online data-processing (Kahmen, 1978; Schlemmer, 1996). Space techniques now dominate global and regional surveys, while terrestrial methods are mainly used for interpolation in space and time, and at solving more local problems. Accuracy and resolution (spatial and temporal) of the results depend on the state of the art of the respective technique. Limiting factors include calibration errors and instrumental drift, and the elimination or reduction of effects directly disturbing the sensor and the measurement process. We especially mention variations of air temperature, atmospheric pressure, groundwater table, and magnetic fi eld, as well as atmospheric refraction, microseismicity, and local site instabilities. Thus the inherent precision of the respective technique may deteriorate by a factor of two to three or more, when considering the accuracy obtained. For the physical fundamentals of geodetic measurement methods we refer to Heitz and Stöcker-Meier (1998), while Plag and Pearlman (2009) review the present state and the future directions of geodetic observation techniques.

# 5.1 Atmospheric refraction

In practically all geodetic measurements, electromagnetic waves serve as signal carriers; this includes the methods of satellite and terrestrial geodesy as well as geodetic astronomy. From the broad spectrum of electromagnetic waves, the visible light (380 to $7 8 0 ~ \mathrm { n m }$ , corresponding to 7.9 and $3 . 8 \times 1 0 ^ { 1 4 } \mathsf { H z } ,$ respectively), the near infrared (up to $1 ~ { \mu \mathrm { m } }$ ), and the microwave parts ( $1 \textrm { m m }$ to $1 \textrm { m }$ , corresponding to $3 0 0 \mathsf { G H z }$ resp. $3 0 0 \ M \ H z )$ are used. When propagating through the atmosphere, the signals experience changes in velocity and curvature of the path (refraction), depending on the physical state of the atmospheric gas masses [5.1.1]. Signal propagation is different in the troposphere and the ionosphere and has to be treated separately [5.1.2], [5.1.3].

Different methods have been developed in order to eliminate or reduce the effects of atmospheric refraction on geodetic measurements. These include instrument design, observation methodology, and the use of atmospheric models based on data collected on the Earth’s surface and in space. The individual strategies will be discussed in the chapters that pertain to measurement methods, see also Brunner (1984a), De Munck and Spoelstra (1992), Dettmering et al. (2010).

# 5.1.1 Fundamentals

According to Fermat’s principle, the path $s$ of an electromagnetic wave is determined by the condition of a minimum travel time $\Delta t$ of the wave (Moritz and Hofmann-Wellenhof, 1993, p. 158):

$$
\Delta t = \intop _ { \mathrm { { p a t h } } } d t = \intop _ { \mathrm { { p a t h } } } \frac { d s } { v } = \operatorname* { m i n } .
$$

The velocity $V$ differs from the velocity in vacuum $c \left( 2 . 2 \right)$ by the index of refraction $n$ (also called refractive index):

$$
n = { \frac { C } { V } } .
$$

For a gaseous medium, $n > 1$ is proportional to the density of the gas. If the medium is dispersive for a certain spectral domain, $n$ also depends on the wavelength: dispersion. An average value for $n$ near the Earth’s surface is 1.0003. Instead of $n$ , the refractivity

$$
N = ( n - 1 ) \times 1 0 ^ { 6 }
$$

is frequently used.

Inserting (5.2) into (5.1) yields

$$
\Delta t = \frac { 1 } { C } \int \displaylimits _ { \mathrm { p a t h } } ^ { } \ d \boldsymbol { n } d s = \mathrm { m i n } .
$$

By setting

$$
n d s = d \bar { s } ,
$$

(5.4) can also be expressed as a minimum condition for the “electromagnetic” path length (Fig. 5.1):

$$
\bar { s } = \int d \bar { s } = \int n d s = \operatorname* { m i n } .
$$

Solving the variational problem (5.5) yields the path ${ \overline { { S } } } ,$ but requires the knowledge of $n$ along the path.

The effect of refraction on the distance is given by the difference between the actual path length $\bar { s }$ and the straight-line $s$ (chord):

$$
\bar { s } - s = \int _ { \mathrm { \scriptsize { p a t h } } } { n d s - \int _ { 0 } ^ { s } { d s } } = \int _ { 0 } ^ { s } ( { n - 1 } ) d s + \left( \int _ { \mathrm { \scriptsize { p a t h } } } { n d s - \int _ { 0 } ^ { s } { n d s } } \right) .
$$

![](images/d88bc4a0c4970c86c6563605ed4748d4d97451c2e198d2f5a579278af3972110.jpg)  
Fig. 5.1: Ray bending in the atmosphere.

The fi rst term on the right side accounts for the difference in length due to the longer travel time in the atmosphere, while the second term represents the effect of the bending of the ray (Janes et al., 1991).

The refraction effect on curvature can be estimated by assuming that the air density is stratifi ed horizontally. Snell’s law describes the bending of the ray as it passes through layers of varying refractive index, which corresponds to Fermat’s principle:

$$
n \mathrm { s i n } z = \mathrm { c o n s t . }
$$

Or for two points $P _ { \uparrow }$ and $P _ { _ 2 }$ :

$$
\begin{array} { r } { n _ { 1 } \sin z _ { 1 } = n _ { 2 } \sin z _ { 2 } . } \end{array}
$$

Under the above assumption, the angle between the normal to the surface $n = \mathrm { c o n s t }$ . and the tangent to the ray with curvature $1 / r$ (the curvature radius $r$ should not be confused with the corresponding spherical coordinate!) is the zenith angle $Z .$ . Differentiation of (5.7a) yields

$$
\sin z d n + n \cos z d z = 0 .
$$

With

$$
d n = ( { \mathrm { g r a d ~ } } n ) \cdot d \mathbf { s } = | { \mathrm { g r a d ~ } } n | \cos z d s ,
$$

we obtain the curvature

$$
{ \frac { 1 } { r } } = { \frac { d z } { d s } } = - { \frac { \left| { \mathrm { g r a d ~ } } n \right| } { n } } \sin z .
$$

By separating the horizontal and the vertical component of grad $n ,$ we get the curvatures of the ray projected into the horizontal and the vertical planes. The corresponding effects on horizontal and vertical angles are called horizontal (lateral) and vertical refraction, respectively.

Horizontal refraction is about one to two orders of magnitude less than vertical refraction. Neglecting the latter yields a simplifi ed formula for the curvature of vertical refraction:

$$
\frac { 1 } { r } = - \frac { 1 } { n } \frac { d n } { d h } \mathsf { s i n } z ,
$$

where $h$ is the geodetic height, cf. [4.1.3].

In terrestrial geodetic measurements, we have $n \approx 1$ and $Z \approx 9 0 ^ { \circ } ,$ , which leads to

$$
{ \frac { 1 } { r } } = - { \frac { d n } { d h } } .
$$

Instead of $1 / r ,$ the coeffi cient of refraction $k$ is often used. It is defi ned as the ratio between the radius of the Earth $R$ and the curvature radius $r$ :

$$
k = { \frac { R } { r } } = - R { \frac { d n } { d h } } .
$$

The vertical refraction angle $\delta$ is the effect of refraction on observed zenith angles (Fig. 5.2). It results from integrating $1 / r$ resp. dn/dh along the path:

$$
\delta = \frac { 1 } { s } \int _ { 0 } ^ { s } ( s - s _ { i } ) \frac { d n } { d h } d s .
$$

Here, the local vertical gradient of $n$ is weighted according to the distance from the observer; values from closer distances receive a larger weight. For a spherical arc $( r = \mathrm { c o n s t . } )$ ), and taking (5.11) into account, (5.12a) reduces to

$$
\delta = \frac { k } { 2 R } s .
$$

In most geodetic applications, the signal is transferred by a modulation of the carrier wave. This can be regarded as a superposition of a group of waves with different frequencies. While phase velocity $ { V _ { \mathrm { p h ^ { \prime } } } }$ introduced in (5.2), refers to the monochromatic carrier wave, the center of a short wave group (signal energy) propagates with the group velocity

$$
v _ { \mathrm { g r } } = v _ { \mathrm { p h } } - \lambda \frac { d v _ { \mathrm { p h } } } { d \lambda } .
$$

In a dispersive medium, we have $n = n ( \lambda )$ and the velocity dispersion $d \nu _ { \mathrm { p h } } / d \lambda \neq 0$ (Leick, 2004). Taking (5.2) into account delivers the corresponding group refractive index

$$
n _ { \mathrm { g r } } = n _ { \mathrm { p h } } - \lambda \frac { d n _ { \mathrm { p h } } } { d \lambda } = n _ { \mathrm { p h } } + f \frac { d n _ { \mathrm { p h } } } { d f } ,
$$

with frequency $f _ { \prime }$ cf. [5.1.2], [5.1.3].

![](images/4f322a2375bfc3d6565ad00a10df8f3bf97a9f58501d2830aa88012dc159fe8c.jpg)  
Fig. 5.2: Vertical refraction.

For a standard atmosphere with air temperature $2 7 3 . 1 5 \mathrm { K } ,$ air pressure $1 0 1 3 . 2 5 \ \mathsf { h P a } ,$ , humidity $0 . 0 \mathrm { \ h P a }$ and $\mathrm { C O } _ { 2 }$ content $0 . 0 3 7 5 \%$ , the phase refractivity may be calculated as follows (IAG resolution, General Assembly Birmingham, 1999; also CODATA, 2006):

$$
N _ { \mathrm { { p h } } } = \bigl ( n _ { \mathrm { p h } } - 1 \bigr ) 1 0 ^ { 6 } = 2 8 7 . 6 1 5 5 + \frac { 1 . 6 2 8 8 7 } { \lambda ^ { 2 } } + \frac { 0 . 0 1 3 6 0 } { \lambda ^ { 4 } } ,
$$

where $\lambda$ is the carrier wave length in $\mu \mathrm { m }$ , and $n _ { \mathrm { { \mathrm { { p h } } } } }$ is the corresponding phase refractive index. The group refractivity is given by

$$
N _ { \mathrm { g r } } = \left( n _ { \mathrm { g r } } - 1 \right) 1 0 ^ { 6 } = 2 8 7 . 6 1 5 5 + \frac { 4 . 8 8 6 6 0 } { \lambda ^ { 2 } } + \frac { 0 . 0 6 8 0 0 } { \lambda ^ { 4 } } ,
$$

with the group refractive index $n _ { \mathrm { g r } } .$

According to (5.6) and (5.12), the refraction effect on distances and angles depends on the index of refraction and its gradient along the path of the ray, which behave differently in the troposphere than in the ionosphere.

# 5.1.2 Tropospheric refraction

The troposphere is the lower layer of the atmosphere. It extends to a height of about $9 ~ \mathrm { k m }$ at the poles and $1 6 ~ \mathrm { k m }$ at the equator. All weather processes take place in this region, where nearly $9 0 \%$ of the atmospheric masses are concentrated. The tropopause as a boundary layer separates the troposphere from the stratosphere, which extends to about 50 to $6 0 ~ \mathrm { k m }$ . The troposphere, tropopause, and stratosphere are electronically neutral. The index of refraction $n$ depends on temperature $T ,$ pressure $p$ and humidity e. For visible light, the troposphere behaves as a dispersive medium, cf. [5.1.1]. The refractive index decreases with height and becomes nearly 1 at about $4 0 ~ \mathrm { k m }$ . Tropospheric refraction is the combined effect from the ground to this “effective” height. Above 70 to $8 0 ~ \mathrm { k m }$ the atmosphere is ionized, cf. [5.1.3].

The meteorological parameters $T , p ,$ e not only depend strongly on height but also on latitude, land/ocean distribution, topography, vegetation, and local conditions. These variables produce large- to small-scale anomalies of n. Additionally, these parameters experience variations with time which are of long-term, seasonal, daily, and turbulent character. Rapid fl uctuations are especially pronounced close to the Earth’s surface, up to 10 to $3 0 ~ \mathsf { m }$ above the ground (e.g., Bomford, 1980; p. 49 ff.).

Temperature $T$ decreases in the troposphere almost linearly with height $h$ according to $d T / d h \ \approx \ - 0 . 0 0 5 5 ^ { \circ } \mathrm { C } / \mathrm { m } ,$ followed by a slight increase in the stratosphere. Horizontal temperature gradients may reach a few $^ { \circ } \mathrm { C } / 1 0 0 ~ \mathrm { k m }$ . Within the fi rst few hundred meters above the Earth’s surface and especially close to the ground, temperature variations are pronounced, including temperature inversion during night time and convection at noon. Air pressure $p$ decreases exponentially with height. Assuming hydrostatic equilibrium, the vertical pressure gradient depends on density $\rho$ and gravity g. Near the surface of the Earth, this leads to $d p / d h = - \rho g = - 0 . 0 3 4 ~ p / T = - 0 . 1 2 ~ \mathsf { h P a / m }$ at standard conditions ${ \cal T } = 2 8 8 \ \mathsf { K } ,$ $p = 1 0 1 3 ~ \mathrm { h P a } )$ ). Humidity is rather irregularly distributed and concentrated in a layer of a few km above ground, where strong variations also occur with time. It is measured by the water vapour pressure e, which is about 10 to $2 0 \mathrm { \ h P a }$ at mid-latitudes close to the surface. It tends to decrease with height, with $d e / d h \approx - 0 . 0 0 4 \dots 0 . 0 0 8 ~ \mathrm { h P a / m }$ at the lower layers, where we also fi nd pronounced differences between dry and damp air regions.

Global tropospheric models generally assume concentric spherical layers and azimuthal symmetry and neglect variations with time. They are provided by standard atmospheres in the form of vertical profi les for temperature, pressure, and density. The U.S. standard atmosphere (1976) approximates mean mid-latitude conditions for dry air, latitudinal and seasonal departures are given by supplements, NOAA (1966, 1976). Widely used is the COSPAR International Reference Atmosphere (CIRA), Rees et al. (1990).

Empirical relations have been derived between the index of refraction and the meteorological parameters for both light and microwaves (Bomford, 1980, p. 42 ff.).

With atmospheric conditions different from the standard air, cf. [5.1.1], the group refractivity of visible light and near infrared waves in ambient moist air is (IAG resolution, General Assembly Birmingham, 1999):

$$
N _ { \scriptscriptstyle { I } } = \left( n _ { \scriptscriptstyle { I } } - 1 \right) 1 0 ^ { 6 } = \frac { 2 7 3 . 1 5 } { 1 0 1 3 . 2 5 } \frac { p } { T } N _ { \mathrm { g r } } - 1 1 . 2 7 \frac { e } { T } ,
$$

with $T$ in Kelvin, $p$ and $e$ in hPa. Equation (5.17a) is also valid for unmodulated light with the corresponding phase refractivity (5.14).

The refractivity of microwaves (independent of the wavelength) is given by the formula of Thayer (1974)

$$
N _ { { _ m } } = \displaystyle ( n _ { { _ m } } - 1 ) 1 0 ^ { 6 } = 7 7 . 6 0 \frac { p } { T } { - 1 3 \frac { e } { T } } + 3 . 7 8 \times 1 0 ^ { 5 } \frac { e } { T ^ { 2 } } ,
$$

which is practically identical with the formula of Essen and Froome (IAG resolution, General Assembly Berkeley, 1963).

The fi rst term on the right side of (5.17a,b) represents a $\mathrm { \Omega ^ { \prime \prime } d r y ^ { \prime \prime } }$ component of the refractivity. It contributes about $9 0 \%$ to the total tropospheric refraction in the lower $1 5 ~ \mathrm { k m }$ and can be modeled from surface pressure values, assuming hydrostatic equilibrium; these values may be derived from in situ measurements or from numerical weather models. The “wet” component, as expressed by the terms depending on $e$ (especially the last one), is highly variable in space and time and extremely diffi cult to model, it approaches zero at around a height of $1 0 ~ \mathrm { k m }$ . In order to keep the error in the index of refraction less than $1 0 ^ { - 6 }$ , the meteorological parameters in $( 5 . 1 7 \mathrm { a } , \mathrm { b } )$ have to be determined to about $\pm 1 ^ { \circ } \mathrm { C }$ for temperature, $\pm 3 . 5 \mathsf { h P a }$ for pressure, and $\pm 2 5 \mathrm { h P a }$ (light) resp. $\pm 0 . 2 \ \mathrm { h P a }$ (microwaves) for humidity.

Refraction formulas as (5.17a,b) have been developed originally for the reduction of terrestrial measurements, carried out close to the surface of the Earth and characterized by small elevation angles. With the advent of geodetic space techniques, large elevations (up to zenith directions) had to be considered, and the signal path now passed through the complete troposphere (and the ionosphere, cf. [5.1.3]), Gruber et al. (2009), Dettmering et al. (2010). A number of corresponding tropospheric refraction models has been developed since the 1960s (e.g., Hopfi eld, 1969; Saastamoinen, 1972/1973), employing actual weather data or numerical models as input. Starting from the refraction effect on a measured distance, these models concentrate on the fi rst term of (5.6), and distinguish between a $\boldsymbol { ^ { \prime \prime } } \mathrm { d r y ^ { \prime \prime } }$ and a “wet” component for the signal delay (see above). The small ray bending effect inherent in (5.6) can easily be taken into account by a “bending function”, see (5.111). As the dry component approximately follows hydrostatic equilibrium, it can be modeled as a function of hydrostatic pressure; this “hydrostatic” component is nearly identical for visible light and radio frequencies. As an example, the IERS conventions (Petit and Luzum, 2010, p. 135) provide the following formula (according to Saastamoinen, 1972/1973) for the zenith hydrostatic delay of radio waves (in meters):

$$
\Delta s ( z \mathrm { e n i t h } ) _ { \mathrm { h y d r . } } = \frac { 0 . 0 0 2 \ 2 7 7 p } { ( 1 - 0 . 0 0 2 \ 7 \cos 2 \varphi - 0 . 0 0 0 \ 2 8 \ H ) } ,
$$

with $p$ (hPa) atmospheric pressure at the observation site, $\varphi$ latitude and $H \left( \mathsf { k m } \right)$ height above the geoid. This results in a maximum effect of $2 . 3 ~ \mathsf { m }$ , and requires the pressure to be determined with $\pm 0 . 4 \ : \mathrm { h P a }$ for a reduction accuracy of $1 \textrm { m m }$ . The zenithal delay contribution of the wet component amounts to 0.07 ns for white light, and varies between 0 and 2 ns (about $1 0 \%$ of the dry component) for radio waves. Due to its high variability in space and time, this part is diffi cult to model, and generally estimated at the evaluation process. Finally, the tropospheric path delay increases strongly with decreasing elevation angles, reaching about 20 to $3 0 ~ \mathsf { m }$ at an elevation below $5 ^ { \circ }$ elevation; this dependence can be modeled by a tropospheric “mapping function”. A simple relation is given by $1 / { \cos } Z$ for elevation angles that are not too small. Again, the “Saastamoinen-model” offers a good approximation, where the wet component is included now (Hofmann-Wellenhof et al., 2008, p. 135):

$$
\Delta s _ { \mathrm { t r o p } } = { \frac { 0 . 0 0 2 \ 2 7 7 } { \mathrm { c o s } z } } \left( p + \left( { \frac { 1 2 5 5 } { T } } + 0 . 0 5 \right) e - \tan ^ { 2 } z \right) .
$$

With $Z$ zenith angle, $p$ (hPa) pressure, $T ~ ( ^ { \circ } \mathsf { K } )$ temperature, e (hPa) partial pressure of water vapor, the result is given in meters. Improved mapping functions have been developed and are available for optical (laser ranging; Mendes and Pavlis, 2004) and for radio techniques (GPS, VLBI; Niell, 1996; Böhm et al., 2006). The refi nements include the separate treatment of the dry and the wet component, and the consideration of horizontal asymmetry of the refraction fi eld.

Differentiating (5.17a,b) with respect to the height $h$ yields the dependence of the rays’ curvature on the meteorological parameters. Neglecting minor terms and taking (5.16b) into account, we obtain for the surface near layers

$$
\frac { d N _ { _ { I } } } { d h } = - 7 8 \frac { p } { T ^ { 2 } } \Big ( 0 . 0 3 4 + \frac { d T } { d h } \Big ) - \frac { 1 1 } { T } \frac { d e } { d h }
$$

for light. For microwaves, the last term on the right side (“wet component”) changes to

$$
+ \frac { 3 . 7 \times 1 0 ^ { 5 } } { T ^ { 2 } } \frac { d e } { d h } .
$$

In the layers close to the ground, the strong variations of the meteorological parameters in space and time lead to corresponding changes in the coeffi cient of refraction, with pronounced seasonal and day/night variations (Höpcke, 1966). Under average daytime conditions with a clear sky, and for heights between $4 0 \textrm { m }$ and $1 0 0 ~ \mathrm { { m } }$ above the ground, we have for light

$$
k _ { \scriptscriptstyle I } = 0 . 1 3 \mathrm { ~ o r ~ } r _ { \scriptscriptstyle I } = 8 R ,
$$

and for microwaves

$$
k _ { _ { \mathrm { m } } } = 0 . 2 5 \ \mathrm { o r } \ r _ { _ { \mathrm { m } } } = 4 R ,
$$

with $r _ { \parallel }$ and $r _ { \mathrm { m } }$ being the curvature radii of light and microwaves, respectively, and $R$ the mean Earth’s radius.

According to (5.11), the coeffi cient of refraction $k$ has to be determined for light with an accuracy of $2 ^ { \circ } \mathrm { C }$ in temperature, $6 \ \mathrm { h P a }$ in air pressure, and $0 . 0 0 0 2 ^ { \circ } \mathrm { C } / \mathrm { m }$ in the temperature gradient in order to achieve a relative accuracy of $1 \%$ . For microwaves, the admissible errors may be two times larger. The gradient of the water vapor pressure should be determined with $0 . 0 0 5 ~ \mathrm { h P a / m }$ for light and $0 . 0 0 0 1 ~ \mathrm { h P a / m }$ for microwaves. Hence, the most critical parameters are the vertical gradients of temperature and, especially for microwaves, of the water vapor pressure. According to (5.12b), an error of $1 \%$ in $k$ would produce an error in the refraction angle of $0 . 2 { ^ { \prime \prime } }$ over a distance of $1 0 ~ \mathrm { k m }$ and $0 . 4 { ^ { \prime \prime } }$ over $2 5 ~ \mathrm { k m }$ .

The evaluation of space geodetic data (especially VLBI, GPS, DORIS) increasingly contributes to the determination of atmospheric parameters, and the improvement of weather models (including latitude and azimuth dependence, MacMillan and Ma, 1997) and weather forecasting (Gendt et al., 2004). The exploitation of GPS signals (carrier phase observations) is of particular importance. Ground-based GPS techniques are based on the path delays that the signals experience when passing through the atmosphere (Davis et al., 1996). By separating the $\boldsymbol { \mathbf { \mathit { \Omega } } } ^ { \prime \prime } \mathrm { d } \boldsymbol { \mathbf { \mathit { r } } } \boldsymbol { \mathbf { \boldsymbol { y } } } ^ { \prime \prime }$ component from the tropospheric signal delay, the integrated precipitable water vapor content above the observer’s site can be estimated from the “wet” component (Bevis et al., 1992). Permanent GPS networks, cf. [5.2.5], [7.3], supply this meteorological information on global and regional scales, with high temporal resolution and nearly on-line (Poli et al., 2007; Heise et al., 2009). The water vapor content can be determined also from ground-based water vapor radiometers, and the results used for calibrating the spacederived “wet” component (Dodson et al., 1996).

Spaceborne GPS receivers allow atmospheric sounding by radio occultation (Yunck and Melbourne, 1996). This method became possible through the installation of GPS receivers on board Low Earth Orbiters (LEOs), as CHAllenging Minisatellite Payload (CHAMP), and Gravity Recovery And Climate Experiment (GRACE) cf. [5.2.8], and the six satellites of the FORMOSAT-3/COSMIC mission (launched 2006), and is now used operationally by several agencies. Here, the GPS signal is tracked after rising or before setting of the GPS satellite (Fig. 5.3). In connection with a network of ground-based receivers, the observed Doppler shift induced by the relative motion between the LEO and the GPS satellite is used for constructing vertical profi les of atmospheric parameters (from the high atmosphere down to the Earth’s surface) on a global scale, including refractivity, bending angles, temperature and water vapor (Wickert et al., 2010).

![](images/0b84bea7dcce5fcc67d93ae8ce868933031c0e5572040aeefc8a7b4c43bfa7ab.jpg)  
Fig. 5.3: Principle of GPS radio occultation technique.

# 5.1.3 Ionospheric refraction

As part of the higher atmosphere, the ionosphere is characterized by the presence of free, negatively-charged electrons and positive ions. Ionization is caused primarily by the impact of solar ultraviolet radiation and consequently depends on the density of the atmospheric gas and the intensity of the radiation. The ionosphere covers the region between about $6 0 ~ \mathrm { k m }$ and $1 5 0 0 ~ \mathrm { k m }$ above the Earth, with a maximum electron density at a height of 200 to $3 0 0 ~ \mathrm { k m }$ .

The ionosphere acts like a mirror at frequencies below $3 0 ~ M { \sf H z }$ . Radio waves of higher frequencies pass through the ionosphere but experience frequency-dependent effects (dispersive medium). Measurements to targets above the ionosphere are also affected by the electron concentration in the plasmasphere, which extends up to a height of several Earth radii above the equator and does not exist at the poles (Wanninger, 1995; Klobuchar, 1996).

The index of refraction depends primarily on the number $N _ { e }$ of electrons per $\mathsf { m } ^ { 3 }$ electron density. As a fi rst order approximation, the phase refractive index is given by

$$
n _ { \mathrm { { _ { p h } } } } = 1 - K \frac { N _ { e } } { f ^ { 2 } } ,
$$

with the constant $K = 4 0 . 2 8 \ \mathrm { m } ^ { 3 } \mathrm { s } ^ { - 2 }$ and frequency $f .$ Higher terms of the order $1 / f ^ { 3 }$ and $1 / f ^ { 4 }$ also depend on the intensity of the Earth’s magnetic fi eld and the direction of the signal propagation. In daytime, $N _ { e } ~ ( \mathrm { e l / m ^ { 3 } } )$ varies between about ${ 1 0 } ^ { 8 } . . . { 1 0 } ^ { 1 0 }$ (heights from 60 to $9 0 ~ \mathrm { k m } ,$ ) over $1 \dot { 0 } ^ { 1 1 }$ (105 to $1 6 0 ~ \mathrm { k m } )$ to $1 0 ^ { 1 1 } . . . 1 0 ^ { 1 2 }$ (160 to $1 8 0 ~ \mathrm { k m } )$ and $1 0 ^ { 1 2 }$ (300 to $4 0 0 \mathrm { k m }$ ).

As seen from (5.2) and (5.21), the phase velocity is larger than the velocity of light in vacuum, which corresponds to a larger wavelength of the signal compared to vacuum. Since signal propagation follows the group velocity, we insert (5.21) into (5.14) and obtain the group refractive index

$$
n _ { \mathrm { g r } } ^ { } = 1 + K \frac { N _ { e } } { f ^ { 2 } } .
$$

Inserting (5.21) resp. (5.22) into (5.6) delivers the difference between the electromagnetic path length _s and the straight-line connection s. This yields for carrier phase ( nph ) and for range $\left( \begin{array} { l } { n } \\ { \mathrm { ~ g r } } \end{array} \right)$ observations, respectively:

$$
( \bar { s } - s ) _ { _ { \mathrm { p h } } } = - ( \bar { s } - s ) _ { _ { \mathrm { g r } } } = - \frac { K } { f ^ { 2 } } \int _ { 0 } ^ { s } N _ { e } \ : d s ,
$$

where the small effect of the path’s bending has been neglected. The signal delay may result in distance errors between a few meters and about 100 meters (Langley, 1998).

The integral of the electron density along the path is called total electron content (TEC):

$$
\mathsf { T E C } = \int _ { 0 } ^ { s } N _ { e } ( s ) \ d s .
$$

It gives the number of electrons along the signal path between the receiver and the satellite, as measured in a cylindrical column with a cross section of $1 \mathrm { ~ m } ^ { 2 }$ ; its unit is $1 \mathsf { T E C U } = 1 0 ^ { 1 6 }$ electrons $/ \mathrm { m } ^ { 2 }$ . TEC values vary between 1 and $1 0 ^ { 3 }$ TECU along the radio wave path. For a spherically-layered ionosphere, we may introduce the electron content along a vertical column of height $h$ and relate it to the TEC along the path by an oblique factor $F$ (“mapping function”):

![](images/4baaa8c3faee8c7a23ef617f4c4cb348e9e96221b28293aa91784f6d2b2a6b7d.jpg)  
Fig. 5.4: Ionospheric refraction.

$$
{ \mathsf { T E C } } = F { \int _ { 0 } ^ { h } } N _ { e } ( h ) \ d h .
$$

For $Z < 7 0 ^ { \circ }$ , we have $F \approx 1 / { \cos { z _ { i } } } ,$ with zenith angle $Z _ { \mathrm { i } }$ at the subionospheric point $P _ { _ i }$ (Fig. 5.4). $P _ { _ i }$ is located at the “mean height” $h _ { i }$ of the ionosphere (single-layer model), with, e.g., $\dot { h } _ { _ i } = 3 5 0 ~ \mathrm { k m }$ . $Z _ { i }$ can be calculated from $h _ { \scriptscriptstyle i }$ and the zenith angle $Z$ measured from the ground:

$$
\sin z _ { i } = { \frac { R } { R + h _ { _ i } } } \sin z ,
$$

$R$ radius of the Earth.

The electron content in the ionosphere depends on the geographical location (with highest values around the Earth’s magnetic equator) and varies strongly with time. There are pronounced variations of daily, seasonal, and about an 11-year (solar activity cycle) period. Superimposed on these more regular variations are irregular disturbances. Short-term scintillations occur primarily in the equatorial zones but also in the polar and auroral regions (magnetic storms). Traveling ionospheric disturbances of wavelike structure proceed with horizontal speeds between 100 and $1 0 0 0 ~ \mathrm { m / s }$ at scales of some 10 to $1 0 0 0 ~ \mathrm { k m }$ and at periods from several minutes to a few hours. The high spatial and temporal variability of the electron content make modeling and prediction of the ionospheric state diffi cult.

Ionospheric models describe the distribution of $N _ { e }$ in space and time. They are based on the dependency of the ionospheric state on the position of the sun, and derived from satellite and rocket probes. Assuming a spherical shell distribution, they provide, among others, a smoothly varying TEC along vertical profi les and a mapping function for inclined signal propagation. Among these models are the regularly updated International Reference Ionosphere (IRI) of COSPAR and the MSIS Thermosphere Model of the Naval Research Laboratory (Hedin, 1987, 1991; Bilitza and Reinisch, 2008; Bilitza et al., 2011).

Refi ned models include actual data from satellites and terrestrial stations, as well as sunspot numbers (e.g., Kleusberg, 1998). These models may deviate from reality by some $1 0 \% ,$ due to the ionospheric disturbances.

Ionospheric models are of special importance if only one frequency is used for radio signal propagation. By employing two frequencies most of the ionospheric refraction effects are eliminated, due to the dispersion effect, cf. [5.2.4], [5.2.5], [5.2.7]. Ionospheric models developed for positioning and navigation with GPS and Galileo will be discussed in [5.2.5].

As with the troposphere, the GPS (and other GNSS) signals may be exploited for ionospheric remote sensing, as the signal delay provides information on the structure and temporal behavior of the ionosphere. By analyzing the two carrier waves used to eliminate ionospheric refraction, cf. [5.2.5], the total electron content (TEC) along the line of sight from the receiver to the GPS satellite can be measured. The abundance of GPS ground networks (e.g., IGS) and the increasing number of space-based receivers nowadays allows to generate nearly real-time global maps of TEC (Yunck and Melbourne, 1996; Fedrizzi et al., 2001; Schmidt, 2011). The electron content of the upper ionosphere and the plasmasphere can be derived from GPS-signals received by satellite-mounted antennas directed upwards.

# 5.2 Satellite observations

Satellite geodesy utilizes artifi cial satellites and the moon as extraterrestrial targets and/or sensors. For a point-mass Earth model, the orbital motion of a satellite is described by Kepler’s laws [5.2.1]. The deviations of the actual gravitational fi eld from this model and non-gravitational forces create orbital “perturbations” [5.2.2]. Satellites used for geodetic applications differ in design, equipment, and orbital parameters according to the mission purpose and the respective observation techniques [5.2.3]. Classical measurement methods, introduced and employed from the 1960s to the 1980s, demonstrated the effi ciency of satellite geodesy for establishing large-scale geodetic control networks, and for the determination of the long-wave part of the gravitational fi eld. Some of these techniques are still employed at present-day geodetic satellite systems [5.2.4]. Today, the Global Positioning System (GPS) governs threedimensional positioning at all scales, and further Global Navigation Satellite Systems (GNSS) have been developed or are under construction [5.2.5]. Laser distance-measurements to artifi cial satellites and to the moon primarily contribute to the establishment and maintenance of global reference systems, but also to the determination of Earth orientation and, with respect to lunar laser ranging, also to lunar sciences and the theory of gravitation [5.2.6]. By monitoring the ocean surface, satellite altimetry is a powerful tool for the survey of the marine gravity fi eld and for geoid determination [5.2.7], while a high-resolution global gravity fi eld recovery including temporal fi eld variations has been obtained by satellite-to-satellite tracking and gravity gradiometry missions [5.2.8].

The theory of satellite orbits and satellite measurement methods are treated in textbooks and monographs on celestial mechanics (Schneider, 1992/1993/1996; Beutler, 2005), orbital theory (Montenbruck and Gill, 2000; Milani and Gronchi, 2009), and satellite geodesy, e.g., Kaula (1966), Schneider (1988), Seeber (2003).

# 5.2.1 Undisturbed satellite motion

After the satellite has separated from the carrier, it begins its unrestrained revolution about the Earth. We assume the gravitational point mass model (central mass), cf. [3.1.2], and neglect the mass of the satellite with respect to the Earth’s mass. If we also neglect perturbations of non-gravitational type and the effect of other celestial bodies (thus restricting ourselves to a two-body problem), Newton’s second law of motion provides the equation of motion in the gravitational fi eld:

$$
\ddot { \mathbf { r } } = \operatorname { g r a d } { \mathbf { \nabla } } V = - \frac { G M } { r ^ { 2 } } \frac { \mathbf { r } } { r } .
$$

$\boldsymbol { \mathsf { r } }$ is the geocentric position vector of the satellite and $\ddot { \mathbf { r } } = d ^ { 2 } \mathbf { r } / d t ^ { 2 }$ its acceleration, $M$ and $V$ are the mass and the gravitational potential of the Earth, respectively, cf. (3.16). The integration of this vectorial second-order differential equation introduces six integration constants, e.g., position and velocity at a given epoch.

The fundamental theory of the two-body problem is given by celestial mechanics (e.g., Kovalevsky, 1989, for further references see the introduction to this chapter). Such works also address the fundamentals of orbit perturbations, orbit computation, and the treatment of three- and multi-body problems.

Johannes Kepler (1571–1630) derived three laws of planetary motion from the astronomic observations collected by Tycho de Brahe (1546–1601), e.g., Schneider and Müller (2009). When applied to an artifi cial satellite, these laws provide a geometric description of the satellite’s undisturbed central motion around the Earth.

According to Kepler’s laws, the satellite moves in an elliptical orbit. One focal point of the ellipse, with semi-major axis a and fi rst numerical eccentricity $e$ (the abbreviations should not be confused with the corresponding parameters of the Earth ellipsoid), coincides with the center of mass of the Earth. In the orbital system (Fig. 5.5), the position of the satellite is described by the distance $r$ from the center of mass and the true anomaly $\nu .$ The true anomaly is the geocentric angle between the directions to the satellite and perigee. Instead of $\nu _ { \mathrm { { \ell } } }$ the eccentric anomaly $E$ can be used, with the relations

$$
r = a ( 1 - e \mathrm { c o s } E ) , \tan \nu = \frac { \sqrt { 1 - e ^ { 2 } } \sin E } { \cos E - e } .
$$

With Kepler’s third law, the mean (angular) velocity

$$
\overline { { n } } = \sqrt { \frac { G M } { a ^ { 3 } } }
$$

![](images/0e27dbc8443ae8bb20cb2b5bf103513d32e9d420a77d076ff964b1f1a35ee1aa.jpg)  
Fig. 5.5: Satellite orbital system.

is introduced, describing a mean orbital motion. The mean anomaly

$$
\overline { { \cal M } } = \overline { { \cal n } } ( t - T )
$$

represents yet another parameter for describing the satellite’s position in the orbit. It is generally preferred because it increases linearly with time t. $T$ is the epoch of the pas-__ sage through the perigee, the closest approach to the Earth. From $\overline { { M } } ,$ , $E$ can be computed iteratively using Kepler’s equation:

$$
\overline { { { M } } } = E - e s \mathrm { i n } E .
$$

The orbital system is transformed into the space-fi xed equatorial system, cf. [2.3.1], by three rotations (Fig. 5.6). The right ascension of the ascending node $\varOmega$ and the inclination $i$ provide the orientation of the orbital plane in space. The argument of perigee $\omega$ orients the ellipse in the orbital plane. From the result of this transformation, we obtain the geocentric position vector (2.10) as a function of the six Keplerian elements a, e, __ $\varOmega _ { \prime }$ $i , \ \omega ,$ and $\nu$ (or equivalently $E , { \overline { { M } } } ,$ or $\boldsymbol { { \cal T } } )$ :

$$
\mathbf { r } = r \left( \begin{array} { c } { \cos \delta \cos \alpha } \\ { \cos \delta \sin \alpha } \\ { \sin \delta } \end{array} \right) = r \left( \begin{array} { c } { \cos ( \omega + \nu ) \cos \varOmega - \sin ( \omega + \nu ) \sin \varOmega \cos { I } } \\ { \cos ( \omega + \nu ) \sin \varOmega + \sin ( \omega + \nu ) \cos \varOmega \cos { I } } \\ { \sin ( \omega + \nu ) \sin { I } } \end{array} \right) ,
$$

with

$$
r = { \frac { a ( 1 - e ^ { 2 } ) } { 1 + e \cos \nu } } .
$$

The six Keplerian parameters completely describe the orbital motion of the undisturbed satellite. They correspond to the integration constants of the equation of motion (5.27) and are used for the approximation of satellite orbits.

![](images/e494e04d29279edc9d81bcf0574ebc54c3ba92c92a1c0f687d3d9ab00b3e86c1.jpg)  
Fig. 5.6: Orbital and equatorial system.

# 5.2.2 Perturbed satellite motion

The actual orbit of a satellite departs from the Keplerian orbit due to the effects of various “disturbing” forces. This includes the non-spherical parts of the Earth’s gravitation, the gravitational effects of moon and sun, atmospheric air drag, and solar radiation pressure, among others. These disturbing forces cause variations in time in the orbital elements (orbital perturbations) of secular, long- and short-periodic nature. The actual orbit can be viewed as the envelope of Keplerian ellipses, which are given at each instant by the actual orbital elements (osculating ellipses).

In order to account for the complete gravitation of the Earth, the gravitational potential of a spherically symmetric Earth must be amended by the perturbing potential $R$ (not to be confused with the disturbing potential introduced in [6.1.1]):

$$
V = { \frac { G M } { r } } + R .
$$

According to equations (3.89) to (3.91), $R$ can be expressed by a spherical harmonic expansion of the gravitational potential $V$ through the harmonic coeffi cients $J _ { { I m } } , \ K _ { { I m } }$ $( I \geq 2 )$ ) . By substituting (5.33) into (5.27), the equation of motion now reads

$$
\ddot { \boldsymbol { \mathsf { r } } } = - \frac { G M } { r ^ { 2 } } \frac { \boldsymbol { \mathsf { r } } } { r } + \mathrm { g r a d } \ \boldsymbol { R } .
$$

The spherical coordinates $r , \ \vartheta , \lambda \left( 2 . 1 3 \right)$ used in the expansion of $V$ can be replaced by the orbital elements according to (5.28) and (5.32), see also Fig. 5.5. $R$ then is described by the time-variable Keplerian orbital parameters and the harmonic coeffi cients:

$$
R = R \big ( a , e , \varOmega , i , \omega , \overline { { M } } , J _ { _ { I m ^ { \prime } } } K _ { _ { I m } } \big ) .
$$

The second-order differential equation (5.34) can be transformed into a system of fi rst-order differential equations. They represent the time rates of the orbital parameters as a function of partial derivatives of the perturbing potential (i.e., of the harmonic coeffi cients) with respect to them. These fi rst-order differential equations are known as Lagrange’s perturbation equations (Kaula, 1966, p. 29; Seeber, 2003, p. 85 ff.):

$$
\begin{array} { r l } & { \frac { d \vec { a } } { d t } = \frac { 2 } { n \partial } \frac { \partial R } { \partial M } } \\ & { \frac { d \vec { e } } { d t } = \frac { 1 } { n ^ { 2 } \mathrm { e } ^ { 2 } } \frac { R } { \partial x } - \frac { \sqrt { 1 - e ^ { 2 } } } { n \mathrm { d } t } \frac { \partial R } { \partial x } } \\ & { \frac { d \vec { e } } { d t } = - \frac { \cos { \vec { e } } } { n \partial ^ { 2 } \mathrm { i } 1 - e ^ { 2 } \sin { \vec { e } } } \frac { \partial R } { \partial t } + \frac { \sqrt { 1 - e ^ { 2 } } } { n \mathrm { a } ^ { 2 } \mathrm { e } } \frac { \partial R } { \partial e } } \\ & { \frac { d \vec { e } } { d t } = \frac { \cos { \vec { e } } } { n \partial ^ { 2 } \mathrm { i } 1 - e ^ { 2 } \sin { \vec { e } } } \frac { \partial R } { n \partial n } - \frac { 1 } { n ^ { 2 } \mathrm { i } 1 - e ^ { 2 } \sin { \vec { e } } } \frac { \partial R } { \partial \mathrm { i } n } } \\ & { \frac { d \vec { Z } } { d t } = \frac { 1 } { n ^ { 2 } \mathrm { i } \mathrm { e } ^ { 2 } \mathrm { e } ^ { 1 } 1 - e ^ { 2 } \sin { \vec { i } } } \frac { \partial R } { \partial t } } \\ & { \frac { d \vec { W } } { d t } = n - \frac { 1 } { n ^ { 2 } \mathrm { e } ^ { 2 } \mathrm { e } ^ { 3 } \mathrm { e } } - \frac { 2 } { n \mathrm { a } } \frac { \partial R } { \partial x } } \\ & { \frac { d \vec { W } } { d t } = n - \frac { 1 } { n ^ { 2 } \mathrm { e } ^ { 2 } \mathrm { e } ^ { 3 } \mathrm { e } } - \frac { 2 } { n \mathrm { a } } \frac { \partial R } { \partial x } } \end{array}
$$

The infl uence of the gravitation of moon and sun on a satellite can be calculated by corresponding extension of (5.27), which leads to the equation of motion for a four-body problem. As a result, a satellite orbit experiences secular and long-periodic perturbations, which may reach $1 0 0 \mathrm { ~ m ~ }$ and more. In addition, solid Earth and ocean tides, cf. [8.3.6], especially affect low-orbiting satellites. Corresponding corrections are based on the ephemeris of the moon and sun and on Earth and ocean tide models.

Air drag is caused by friction of the satellite with atmospheric particles. It is proportional to the velocity of the satellite and depends on atmospheric density and the effective cross-sectional area to mass ratio. With increasing altitude, the air drag decreases rapidly and approaches zero at about $1 0 0 0 ~ \mathrm { k m }$ . Air drag effects are corrected using high-altitude atmospheric models such as the COSPAR International Reference Atmosphere, or from on-board accelerometer measurements, cf. [5.1.2], [5.2.8].

High-altitude satellites are especially affected by solar radiation pressure due to incident photons. The resulting perturbations depend on the solar fl ux and the attitude of the satellite with respect to the sun, the area to mass ratio, and the refl ectivity. The Earth-refl ected solar radiation pressure (albedo) remains signifi cantly smaller than the direct effect. Modeling of the radiation pressure effects is diffi cult, especially for satellites of complex structure. Electromagnetic interactions with the magnetic fi eld of the Earth occur in the ionosphere; however, they are small and can be considered by corrections. At the now reached level of accuracy, relativistic effects also have to be taken into account (Ries et al., 1991).

Orbit determinations are based on analytical or numerical methods (Boccaletti and Pucacco, 1996/1999; Milani and Gronchi, 2009). For analytical solutions, all acting forces are expressed by rigorous relations and integrated in closed form. A fi rst order approximation is already provided by the solution of (5.35). The position vector at any epoch $t$ is given by the orbital elements at an initial epoch $t _ { \mathrm { 0 ^ { \prime } } }$ the parameters of the gravitational fi eld, and other models of disturbing forces:

$$
\mathbf { r } = \mathbf { r } ( a _ { 0 } , \ e _ { _ { 0 } } , \ \Omega _ { o } , \ i _ { _ { 0 } } , \ \omega _ { _ { 0 } } , \ \overline { { M } } _ { 0 } ; \ G M , \ J _ { _ { I m ^ { \prime } } } \ K _ { _ { I m } } ; . . . ; t ) .
$$

For numerical methods, all forces are calculated for a particular position of the satellite and used as a starting condition for a stepwise integration of the equation of motion (5.34a). Classical astronomic methods for orbit determination are used, as developed by Cowell (integration of the total force) or Encke (integration of the difference to an osculating Kepler ellipse). The numerical integration itself is carried out with conventional methods, fi tting a polynomial to a series of consecutive points. The Runge-Kutta method as a single-step solution uses a Taylor series for extrapolation, while multi-step methods iteratively improve the prediction results, e.g., through Kalman fi lter techniques (Montenbruck and Gill, 2000).

The analytical method is rather laborious, and diffi culties arise at applying it to nongravitational forces. It is well suited for estimating the effects of perturbing forces on the satellite’s orbit and for the planning of satellite missions and projects. Numerical methods are simple and generally applicable. They are used nearly exclusively today. The arc lengths for orbit modeling (parameter estimation by adjustment) vary from a few days at low orbiting satellites to some weeks at high fl ying satellites.

Orbit determination is now also directly possible by spaceborne packages of satellite navigation and positioning systems as GPS or DORIS (Yunck and Melbourne, 1996), this strategy is applied especially at low Earth orbiters, where modeling of perturbations is diffi cult. In contrast to the dynamic approach explained above this kinematic orbit determination does not require any information on the acting forces (gravitation, air drag, solar radiation etc.).

Precise orbit determinations are especially important for positioning and satellite altimetry, but also for satellite gravity missions. With good satellite tracking (within the frame of dedicated networks), and (for the dynamic orbit determination) using precise models of both the gravitational fi eld and the non-gravitational forces, the ephemeris of geodetic relevant satellites can be determined by orbital post-processing with cm-accuracy. By applying adequate models for the perturbing forces, orbit predictions can be carried out and extended from several revolutions of the satellite to days and months, with prediction accuracies varying from some centimeters to some meters. Predicted orbits for individual satellites are published by the responsible agencies, while navigation satellites also transmit their own orbital data, cf. [5.2.4], [5.2.5].

An orbital accuracy of better than one mm can be achieved for high-altitude satellites used for positioning, by truncated versions of existing gravitational fi eld models. For the EGM2008 model, cf. [6.6.3], suggested truncation levels are at degree and order 90 for Starlette (orbital radius about $7 3 0 0 ~ \mathrm { k m }$ ), 20 for Lageos $1 2 3 0 0 ~ \mathrm { k m } )$ ), and 12 for GPS $( 2 6 6 0 0 ~ \mathrm { k m } )$ , Petit and Luzum (2010).

# 5.2.3 Artifi cial Earth satellites

Since the launch of Sputnik I (1957), artifi cial Earth satellites have been used for geodetic purposes such as positioning and the determination of the Earth’s gravity fi eld and rotation parameters. Only a limited number of satellite missions have been designed exclusively for geodetic applications. However, a large number of satellites developed for navigation, remote sensing, and geophysics were and are used extensively also in geodesy.

A satellite can be regarded as a moving target at high altitude and then used for positioning. Because the satellite’s orbit is affected by the gravitational field of the Earth, the satellite may also serve as a sensor for gravitation. Time series of satellite observations finally allow to monitor the time-variable Earth orientation. Satellites may reflect incident light only (passive satellites), or they may carry subsystems on board such as transmitters/receivers, different type sensors, clocks, and computers (active satellites). In the latter case, an energy supply is required, and lifetime is rather limited. Passive satellites have played and play an important role in geodesy, but active satellite missions nowadays support the majority of geodetic applications.

The mean orbital velocity of a satellite moving in an approximately circular orbit $( r = a )$ is given from (5.29) by

$$
{ \overline { { V } } } = a { \overline { { n } } } = \left( { \frac { G M } { r } } \right) ^ { \frac { 1 } { 2 } } .
$$

For a satellite close to the Earth $( h = 8 0 0 ~ \mathrm { k m } )$ , we obtain, with $r = R + h = 7 1 7 0 { \mathrm { k m } } ,$ a velocity of $7 . 5 ~ \mathrm { k m } / s$ . Kepler’s third law yields the period of revolution $U = 2 \pi r / \bar { v } = 1 0 1$ min. For a high-orbiting satellite $( h = 2 0 0 0 0 \mathrm { k m } )$ ) we have $3 . 9 ~ \mathrm { k m } / s$ for velocity and 12 h for the period of revolution. The intersection of the orbital plane with a non-rotating Earth represents a great circle on the Earth’s surface: subsatellite track. The rotation of the Earth causes a western displacement of subsequent satellite orbits (Fig. 5.7), with a shift on the equator given by

![](images/8d469b5a56973a7232d5215272b55636c8a189e98618704eec6521782a19ba56.jpg)  
Fig. 5.7: Subsatellite tracks (inclination $6 0 ^ { \circ }$ ).

$$
\Delta \lambda = 3 6 0 ^ { \circ } { \frac { U } { \ s i d e r e a l \ d a y } } = 1 5 ^ { \circ } U [ h ] = 0 . 2 5 ^ { \circ } U [ \mathsf { m i n } ] .
$$

The latitude range of the subsatellite tracks is determined by the inclination of the satellite.

The following aspects have to be considered during the design (choice of orbital parameters) of satellite missions for geodetic applications:

For positioning and determination of Earth rotation, the network geometry of the ground stations and the satellites plays a primary role. Simultaneous direction measurements from two ground stations to a satellite form a plane, and the intersection of planes provides relative positions within a geometric network (satellite triangulation). Range measurements utilize the intersection of spheres (satellite trilateration), whereas range differences, derived from Doppler-frequency shifts, use the intersection of hyperboloids. If the satellite’s orbit is known with high accuracy, the absolute position of the ground stations can be derived from these relative measurements. Satellites at high altitudes are preferred for positioning and navigation, as they are less infl uenced by gravitational and air drag perturbations.

Exact simultaneous measurements of directions or distances were performed from the 1960s to the 1970s, and led to purely geometric satellite networks, without precise knowledge of the satellite orbits. When simultaneousness could be achieved only approximately, a shortarc orbital fi tting served for interpolation and improvement of the results, cf. [5.2.4].

The orbital analysis of satellites has been early used for the determination of the Earth’s gravitational fi eld. As high-orbiting satellites only sense the long-wave parts of the gravity fi eld, low altitude satellites are required for determining the gravitational fi eld at a higher spatial resolution. This is mainly due to the attenuation factor $( a _ { \mathrm { e } } / r ) ^ { I }$ in the spherical harmonic expansion of the gravitational potential (semimajor axis of