# CHAPTER 3

# 3.l Transformation of Displacements

Consider a case where the position of a particle $p$ in space is defined in terms of thedisplacement vectorrrelative to the movingcoordinates xyz, shown in Fig. 3.1-1. If the displacement of the origin of the moving coordinate system is $\mathbf { R } _ { 0 }$ , the displacement of $P$ relative to the fixed coordinates $X _ { i }$ Y, $Z$ is,

$$
\mathbf { R } = \mathbf { R } _ { 0 } + \mathbf { r }
$$

Letting unit vectors along the fixed and moving axes be designated by i, j, k and $\mathbf { i } ^ { \prime }$ ， ${ \bf { j } } ^ { \prime }$ ， $\mathbf { k } ^ { \prime }$ respectively, the above equation can be writen as,

$$
( X { \bf i } + Y { \bf j } + Z { \bf k } ) = ( X _ { 0 } { \bf i } + Y _ { 0 } { \bf j } + Z _ { 0 } { \bf k } ) + ( x { \bf i } ^ { \prime } + y { \bf j } ^ { \prime } + z { \bf k } ^ { \prime } )
$$

We can determine the component of the above vector in any direction by forming the dot product of the above equation with a unit vector in the desired direction. For example, the $X$ component is obtained by the dot product of theabove equation with i,etc. The three rectangular components along the fixed coordinates are, then,

$$
\begin{array} { l } { { X = X _ { 0 } + x { \bf i } \cdot { \bf i ^ { \prime } } + y { \bf i } \cdot { \bf j ^ { \prime } } + z { \bf i } \cdot { \bf k ^ { \prime } } } } \\ { { \quad Y = Y _ { 0 } + x { \bf j } \cdot { \bf i ^ { \prime } } + y { \bf j } \cdot { \bf j ^ { \prime } } + z { \bf j } \cdot { \bf k ^ { \prime } } } } \\ { { \quad Z = Z _ { 0 } + x { \bf k } \cdot { \bf i ^ { \prime } } + y { \bf k } \cdot { \bf j ^ { \prime } } + z { \bf k } \cdot { \bf k ^ { \prime } } } } \end{array}
$$

where the dot product of the various unit vectors represents the direction cosine between the coordinates.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/8ef5a17d7773e9c884c1186b73f5329a4efb12c685280e3fbf687573eb1ba33e.jpg)  
Fig.3.1-l. Transformation between coordinates x, y, $z$ and X, Y, Z.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/0536f5da30358f25a21695548b37c11cd1a76f7c50c4c347b6c03c0948df5ba7.jpg)  
Fig. 3.l-2. Coordinate transformation in a plane.

For plane motion with $Z = z = 0$ shown in Fig. 3.1-2, the direction cosines involved are,

$$
\begin{array} { l } { \mathbf { i } \cdot \mathbf { i } ^ { \prime } = \cos \theta = \mathbf { j } \cdot \mathbf { j } ^ { \prime } } \\ { \mathbf { i } \cdot \mathbf { j } ^ { \prime } = - \sin \theta = - \mathbf { j } \cdot \mathbf { i } ^ { \prime } } \end{array}
$$

so that Eq. 3.1-3 reduces to,

$$
\begin{array} { r } { X - X _ { 0 } = x \cos \theta - y \sin \theta } \\ { Y - Y _ { 0 } = x \sin \theta + y \cos \theta } \end{array}
$$

A convenient way to express the above equations is by the following matrix equation,\*

$$
{ \begin{array} { r l } { { \boldsymbol { \left[ X - X _ { 0 } \right] } } = { \left[ \begin{array} { l l } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} \right] } { \boldsymbol { \left[ x \right] } } } \\ { { \boldsymbol { \left[ Y - Y _ { 0 } \right] } } = { \left[ \begin{array} { l l } { \cos \theta } & { \quad \cos \theta } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } } \end{array} }
$$

The square matrix with the direction cosines for elements is called the transfer matrix which,inthis case,transforms thebodycoordinates to the fixed inertial coordinates.

To obtain the inverse transformation from the fixed coordinate system to the moving coordinate system, we can start with Eq. 3.1-2 arranged as follows:

$$
( x { \bf i } ^ { \prime } + y { \bf j } ^ { \prime } ) = ( X - X _ { 0 } ) { \bf i } + ( Y - Y _ { 0 } ) { \bf j }
$$

and form the dot product with i' and j'

$$
\begin{array} { r l } & { x = ( X - X _ { 0 } ) \mathbf { i } \cdot \mathbf { i } ^ { \prime } + ( Y - Y _ { 0 } ) \mathbf { j } \cdot \mathbf { i } ^ { \prime } } \\ & { y = ( X - X _ { 0 } ) \mathbf { i } \cdot \mathbf { j } ^ { \prime } + ( Y - Y _ { 0 } ) \mathbf { j } \cdot \mathbf { j } ^ { \prime } } \end{array}
$$

The above equations in matrix notation become,

$$
\begin{array} { r l } & { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] = \left[ \begin{array} { l l } { \mathbf { i } \cdot \mathbf { i } ^ { \prime } } & { \mathbf { j } \cdot \mathbf { i } ^ { \prime } } \\ { \mathbf { i } \cdot \mathbf { j } ^ { \prime } } & { \mathbf { j } \cdot \mathbf { j } ^ { \prime } } \end{array} \right] \left[ \begin{array} { l } { X - X _ { 0 } } \\ { Y - Y _ { 0 } } \end{array} \right] } \\ & { \qquad = \left[ \begin{array} { l l } { \cos { \theta } } & { \sin { \theta } } \\ { \displaystyle - \sin { \theta } } & { \cos { \theta } } \end{array} \right] \left[ \begin{array} { l } { X - X _ { 0 } } \\ { Y - Y _ { 0 } } \end{array} \right] } \end{array}
$$

which is the inverse of Eq.3.1-5. The transfer matrix is here the inverse of the transfer matrix of Eq. 3.1-5.

$$
{ \left[ \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right] } = { \left[ \begin{array} { l l } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} \right] } ^ { - 1 }
$$

# 3.2 Transformation of Velocities

The velocity of any arbitrary fxed point on the moving coordinate system $_ x$ ，y， $z$ with respect to the fixed-axis system is,

$$
\dot { \bf R } = \dot { \bf R } _ { 0 } + \boldsymbol { \omega } \times { \bf r }
$$

This equation indicates that we can start with the displacement equation in terms of the rectangular components and differentiate, holding $x , y , z$ as

constants. For instance, if we differentiate Eq. 3.1-4, with $_ { x }$ and $y$ held constant, we obtain the velocity equation,

$$
\begin{array} { r l } & { \dot { X } - \dot { X } _ { 0 } = - ( x \sin \theta + y \cos \theta ) \dot { \theta } } \\ & { \dot { Y } - \dot { Y } _ { 0 } = ( x \cos \theta - y \sin \theta ) \dot { \theta } } \end{array}
$$

Comparing with Eq. 3.1-4, these equations can also be written as,

$$
\begin{array} { l } { { \dot { X } - \dot { X } _ { 0 } = - ( Y - Y _ { 0 } ) \dot { \theta } } } \\ { { \dot { Y } - \dot { Y } _ { 0 } = ( X - X _ { 0 } ) \dot { \theta } } } \end{array}
$$

# 3.3 Instantaneous Center

If we define an instantaneous center as a point of zero velocity， we can find its coordinates in the $X Y$ plane by letting $\dot { X } = \dot { Y } = 0$ in Eq. 3.2-3.

$$
\begin{array} { c c c } { { X _ { i o } = X _ { 0 } - \displaystyle \frac { \dot { Y } _ { 0 } } { \dot { \theta } } } } \\ { { { } } } \\ { { Y _ { i e } = Y _ { 0 } + \displaystyle \frac { \dot { X } _ { 0 } } { \dot { \theta } } } } \end{array}
$$

The locus of such points in the fixed plane is the space centrode or the herpolhodecurve.Thelocus of theinstantaneouscenter onthemoving $_ { x y }$ plane is called the body centrode or the polhode curve.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/07a6a3dd1d265f76cf1823c4bdc17fd33ade49f0bb6cf4fd4f9bf299656b6bc2.jpg)  
Fig. 3.3-l. Polhode curve rols on the herpolhode curve.

As an illustration, consider a bar AB, shown in Fig. 3.3-1, the ends of which must move along the vertical and horizontal guides.Placing the moving coordinates $_ { x }$ yasshown withtheorigincoincidingwithpoint $A$ ， $X _ { 0 } = \dot { X } _ { 0 } = 0$ We therefore have,

$$
\begin{array} { l } { { \displaystyle { X _ { i c } = - \frac { \dot { Y } _ { 0 } } { \dot { \theta } } } } } \\ { { \displaystyle { Y _ { i c } = Y _ { 0 } } } } \end{array}
$$

which indicates that the locus of the instantaneous center (herpolhode) in the $X Y$ plane is a quarter-circle of radius equal to the length AB.

If for every position of the bar $A B$ a hole is punched through the two planes at the instantaneous center, the set of holes on the moving plane will trace out the polhode curve, which in this case is a half-circle of diameter $A B$ .It is evident,then,that the polhode curve rols without slipping on the herpolhode curve.

# 3.4 Euler's Angles

A point on a rigid body can be defined in terms of body-fixed axes x, y, z. To determine the orientation of the body itself, we now introduce Euler's angles $\psi$ ， $\varphi$ ， $\theta$ which are three independent quantities capable of defining the position of the $_ x$ y, $z$ ,body axes relative to the inertial $X , ~ Y , Z$ axes,as shown in Fig. 3.4-1.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/042b8dbb62a60503a5cec1deda12bb80ff2c34dcb7a9ad58f8a4b00d50221ace.jpg)  
Fig. 3.4-l. Body axes x, y,z defined relative to inertial axes X, Y, Z by Euler's angles 4,Φ,0.

The position of the body axes can be arrived at by three rotations which will also define other coordinates often encountered in rigid body dynamics.

With the $_ { x }$ , y, z, axes coinciding with the $X ,$ Y, $Z$ axes, allow the x, y, z coordinates to rotate about the $Z$ axis through an angle $\psi$ so as to take up the position $\xi ^ { \prime } \eta ^ { \prime } \zeta ^ { \prime }$ , shown in Fig. 3.4-2.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/e906ef9b44a32c454f5b02a5292ba84496e2664ec2b95ebc0371281752edab35.jpg)  
Fig. 3.4-2. Rotation about $z$ axis through angle y.

The relationship between the two coordinates is then given by the transfer matrix

$$
{ \left[ \begin{array} { l } { \xi ^ { \prime } } \\ { \eta ^ { \prime } } \\ { \zeta ^ { \prime } } \end{array} \right] } = { \left[ \begin{array} { l l l } { \cos \psi } & { \sin \psi } & { 0 } \\ { - \sin \psi } & { \cos \psi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] }
$$

We next allow a rotation $\theta$ about the $\xi ^ { \prime }$ axis as shown in Fig. 3.4-3, and let the new position of the $\xi ^ { \prime }$ ， $\eta ^ { \prime }$ ， $\zeta ^ { \prime }$ axes be $\xi , \eta _ { ; }$ $\zeta$ with transfer matrix

$$
{ \left[ \begin{array} { l } { \xi } \\ { \eta } \\ { \zeta } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right] } { \left[ \begin{array} { l } { \xi ^ { \prime } } \\ { \eta ^ { \prime } } \\ { \zeta ^ { \prime } } \end{array} \right] }
$$

Finally we allow a spin $\varphi$ about the axis $\zeta$ , as shown in Fig. 3.4-4, to arrive at the body axes $_ x$ ， y, z. The transfer matrix for this rotation is

$$
{ \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l l l } { \cos \varphi } & { \sin \ \varphi } & { 0 } \\ { - \sin \varphi } & { \cos \varphi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { \xi } \\ { \eta } \\ { \zeta } \end{array} \right] }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/58462be3ae787df80f1f29202ed6474c962101851402709b4742d034dfec21fb.jpg)  
Fig. 3.4-3. Rotation about node axis $\xi ^ { \prime } = \xi$ through angle 0.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/e3f1dd2ea90eaa07d691a4e935a06033f82745d534af8e4d22513814cf16f79c.jpg)  
Fig. 3.4-4. Rotation about $z = \zeta$ axis through spin angle $\varphi$ ·

In arriving at the final position of the body axes, we have encountered four sets of orthogonal axes: $X , \ Y , Z ; \ \xi ^ { \prime } , \ \eta ^ { \prime } , \ \zeta ^ { \prime } ; \ \xi , \ \eta , \ \zeta ;$ and x, y, z. Some of these axes coincide, such as the $Z \zeta ^ { \prime }$ , the $\begin{array} { r } { \zeta _ { z , \pm } } \end{array}$ and the $\xi ^ { \prime } \xi$ ; however both letters will be retained to identify the coordinate system referred to. Of particular interest is the $\xi ^ { \prime } \xi$ axis, called the line of nodes. It represents the intersection of the transverse body plane $x y$ and the horizontal inertial plane $X Y$

Other transformations between these coordinates can be obtained by the multiplication of two or more transfer matrices. For instance, by substituting Eq. 3.4-1 into Eq. 3.4-2 we obtain the following transformation\* between the $X _ { i }$ ，Y, $Z$ and the $\xi$ ， $\eta _ { i }$ $\zeta$ axes:

$$
{ \begin{array} { r } { { \left[ \begin{array} { l } { \xi } \\ { \eta } \\ { \zeta } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { \cos \theta } & { \sin \theta } \\ { 0 } & { - \sin \theta } & { \cos \theta } \end{array} \right] } { \left[ \begin{array} { l l l } { \cos \psi } & { \sin \psi } & { 0 } \\ { - \sin \psi } & { \cos \psi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] } } \\ { = { \left[ \begin{array} { l l l } { \cos \psi } & { \sin \psi } & { 0 } \\ { - \cos \theta \sin \psi } & { \cos \theta \cos \psi } & { \sin \theta } \\ { \sin \theta \sin \psi } & { - \sin \theta \cos \psi } & { \cos \theta } \end{array} \right] } { \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] } } \end{array} }
$$

Substituting Eq. 3.4-4 into Eq. 3.4-3, we obtain the transformation from the $X Y Z$ axes to the body axes xyz:

$$
{ \begin{array} { r l } { { \left[ \right]} { \begin{array} { l } { x } \\ { y } \\ { z } \end{array} }  = { \left[ \begin{array} { l l } { \left( \cos \phi \cos \psi - \sin \phi \cos \theta \sin \psi \right) } & { \left( \cos \phi \sin \psi \right) } \\ { \left( - \sin \phi \cos \psi - \cos \phi \cos \theta \sin \psi \right) } & { } \\ { \qquad \left( \sin \theta \sin \psi \right) } \\ { \left( \cos \phi \sin \psi + \sin \phi \cos \theta \cos \psi \right) } & { \quad \left( \sin \phi \sin \theta \right) } \\ { \left( - \sin \phi \sin \psi + \cos \phi \cos \theta \cos \psi \right) } & { \quad \left( \cos \phi \sin \theta \right) } \\ { \qquad \left( - \sin \theta \cos \psi \right) } & { \quad \qquad \left( \cos \theta \right) } \end{array} \right] } { \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] } } \end{array} }
$$

The inverse transformation from the $x , y , z$ body axes to the $X$ ,Y, z inertial axes can be obtained in a similar manner by writing Eqs. 3.4-1, 3.4-2 and 3.4-3in the inverse order,i.e.,

$$
{ \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] } = { \left[ \begin{array} { l l l } { \cos { \psi } } & { - \sin { \psi } } & { 0 } \\ { \sin { \psi } } & { \cos { \psi } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { \xi ^ { \prime } } \\ { \eta ^ { \prime } } \\ { \zeta ^ { \prime } } \end{array} \right] }
$$

\* See Appendix A.

etc. Rules are also available for the direct inversion of matrices. The inverse of Eq. 3.4-5 is

$$
\begin{array} { r } { \left[ \begin{array} { c } { X } \\ { Y } \\ { Z } \end{array} \right] = \left[ \begin{array} { c c } { \left( \cos { \varphi } \cos { \psi } - \sin { \varphi } \cos { \theta } \sin { \psi } \right) } & { 0 } \\ { \left( \cos { \varphi } \sin { \psi } + \sin { \varphi } \cos { \theta } \cos { \psi } \right) } & { 0 } \\ { \left( \sin { \theta } \sin { \varphi } \right) } & { \left( \sin { \theta } \sin { \psi } \right) } \\ { \left( - \sin { \varphi } \cos { \psi } - \sin { \psi } \cos { \theta } \cos { \varphi } \right) } & { \left( \sin { \theta } \sin { \psi } \right) } \\ { \left( - \sin { \varphi } \sin { \psi } + \cos { \varphi } \cos { \theta } \cos { \psi } \right) } & { \left( - \sin { \theta } \cos { \psi } \right) } \\ { \left( \sin { \theta } \cos { \varphi } \right) } & { \left( \cos { \theta } \right) } \end{array} \right] \left[ \begin{array} { c } { x } \\ { y } \\ { z } \end{array} \right] } \end{array}
$$

# 3.5 Transformation of Angular Velocities

Frequently we need to express the angular velocities $\omega _ { x } \ : \omega _ { y } \ : \omega _ { z }$ about the body axes $x$ $z$ in terms of Euler's angles. The transformation may be pursued as follows.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/325480e9c30b39b06009103227680132092e59ed2eccec5bdc67a43b159c2ee3.jpg)  
Fig. 3.5-l. Angular rates of Euler angles.

Resolve the angular velocity $\dot { \psi }$ along the $\zeta$ and $\eta$ axes so that the orthogonal components of $\dot { \psi } , \dot { \varphi } ,$ and $\dot { \theta }$ are $\dot { \theta }$ along $\xi _ { i }$ $\dot { \psi }$ sin $\theta$ along $\eta _ { i }$ and $\dot { \varphi } + \dot { \psi }$ cos $\theta$ along $\zeta _ { i }$ ,as shown in Fig. 3.5-1.

Next resolve the components along the $\xi$ and $\eta$ axes to the $_ x$ and y directions, the result being

$$
\begin{array} { r l } & { \omega _ { x } = \dot { \psi } \sin \theta \sin \varphi + \dot { \theta } \cos \varphi } \\ & { \omega _ { y } = \dot { \psi } \sin \theta \cos \varphi - \dot { \theta } \sin \varphi } \\ & { \omega _ { z } = \dot { \varphi } + \dot { \psi } \cos \theta } \end{array}
$$

or in its inverse form,

$$
\begin{array} { l } { { \displaystyle { \dot { \psi } = \frac { 1 } { \sin \theta } \left( \omega _ { x } \sin \varphi + \omega _ { y } \cos \varphi \right) } } } \\ { { \displaystyle { \dot { \varphi } = \omega _ { z } - \frac { \cos \theta } { \sin \theta } \left( \omega _ { x } \sin \varphi + \omega _ { y } \cos \varphi \right) } } } \\ { { \displaystyle { \dot { \theta } = \omega _ { x } \cos \varphi - \omega _ { y } \sin \varphi } } } \end{array}
$$

Arranged in matrix form, these equations become

$$
{ \left[ \begin{array} { l } { \omega _ { \alpha } } \\ { \omega _ { \nu } } \\ { \omega _ { z } } \end{array} \right] } = { \left[ \begin{array} { l l l } { \sin \theta \sin \varphi } & { 0 } & { \cos \varphi } \\ { \sin \theta \cos \varphi } & { 0 } & { - \sin \varphi } \\ { \cos \theta } & { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { { \dot { \psi } } } \\ { { \dot { \varphi } } } \\ { { \dot { \theta } } } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l } { \dot { \psi } } \\ { \dot { \varphi } } \\ { \dot { \theta } } \end{array} \right] } = { \frac { 1 } { \sin \ \theta } } { \left[ \begin{array} { c c c c } { \sin \varphi } & { \cos \varphi } & { 0 } \\ { - \sin \varphi \cos \theta } & { - \cos \varphi \cos \theta } & { \sin \theta } \\ { \cos \varphi \sin \theta } & { - \sin \varphi \sin \theta } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { \omega _ { x } } \\ { \omega _ { y } } \\ { \omega _ { z } } \end{array} \right] }
$$

# PROBLEMS

1. A point $P$ in the inertial space is defined by itscomponents $X _ { 1 } , ~ Y _ { 1 } ,$ and $Z _ { 1 }$ From $P$ a perpendicular $P N$ is drawn to a line whose direction is specified by the angles $\propto$ ， $\beta$ ,and $\gamma$ Determine the lengths $O N$ and $P N _ { \ell }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/dd837651161b4153388fbf2285071e4338db5a7ad1ed6e54c74cb4cf5d323060.jpg)  
Prob. I

2. Determine the inertial components of a point (3,4, 5) in the rotating coordinate system x,y,z, specified by the Euler angles $\theta \ : = \ : 3 0 ^ { \circ }$ ， $\psi = 4 5 ^ { \circ }$ and $\varphi = 3 0 ^ { \circ }$

3. Using body-fixed axes along a bar of length l whose ends slide along a smooth vertical wall and horizontal floor, determine the acceleration of its midpoint.   
4. One end A of a bar AB moves along a vertical wall while some intermediate point slides over the corner of a step a distance $s$ from the wall. Derive the equation for the herpolhode and polhode curves.(Use fixed coordinates through the corner $o$ ,and let $\bar { Z }$ ， $\boldsymbol { Y } ,$ be coordinates of the space centrode.)

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/de6778b9dafa1d7459b59c143332ca1c3d3f75f8d171ba05caab3035191da1c5.jpg)  
Prob.4

5. The center of a wheel of radius $R$ is moving to the right with velocity $v _ { 0 }$ while the angular speed of the wheel is $\omega _ { 0 }$ in the counterclockwise direction. Using body-fixed axes x', y’and inertial axes X, Yas shown, determine the polhode and herpolhode curves.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/6bbded52a9b66f212c011caad522c3b2074c896725ed66ed064463257aef1cd1.jpg)  
Prob.5

6. The ends of a link of length I = kR moves along the circumference and the diameter of a circle of radius R. Determine the instantaneous center as a function of the angle 0.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/938a42a23593fef16fcdd7690919547e03983b9b8c94d18a89cb1f6e6513d3c5.jpg)  
Prob.6

7. A rod moves in a vertical plane, with the lower end along the horizontal and an intermediate point resting against a small pin at height $h$ Determine the instantaneous center as a function of $\theta$ and plot the polhode and herpolhode curves.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/a081df66a3c3d6144320714586ca01631690cc47b7d44a33302c458526e0c1a3.jpg)  
Prob.7

8. At a given instant a man in a parachute is 6O ft above a $2 0 ^ { \circ }$ inclined hillside.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/ef42b00d705deb8e58b85e90d09c2b49cbbabf11228ba512a83bd4fc9354d645.jpg)  
Prob.8

If his horizontal and vertical velocities are constant and equal to 10 ft/sec and 20 ft/sec respectively, determine his coordinate as a function of time: (a)in the X, Y system; (b) in the x,y system. Determine the time and place of landing on the hillside.

9.A convenient coordinate system for surface navigation on earth is the longitude-latitude system with the origin coinciding with the moving vehicle shown in the sketch. The $x , y$ axes lie in the horizontal plane along the latitude and longitude lines. Show that the angular velocities along the coordinates are

$$
{ \boldsymbol { \omega } } = - \lambda { \boldsymbol { \mathrm { i } } } + ( { \dot { \varphi } } + \Omega ) \cos \lambda { \boldsymbol { \mathrm { j } } } + ( { \dot { \varphi } } + \Omega ) \sin \lambda { \boldsymbol { \mathrm { k } } }
$$

where the i, j, k vectors are along the $x , y , z$ directions, and $\Omega$ is the earth's rotational speed.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/563d42ff5dd40c737c4f436b8ab0f5f031cf07c631a358961b2b7685b4f9a217.jpg)  
Prob.9

10. For the system of Prob. 9, determine the $x$ ， $y$ , z components of the acceleraion

11. A satellite $s$ circles the earth with the orbit plane making an angle $\propto$ with the earth's equatorial plane. The $X$ axis is oriented so that it passes through the intersection of the orbit and equatorial planes. The position of the satellite at any time can be given in terms of $\boldsymbol { r } _ { g } ,$ the distance from the earth's certer, γ the angle of the meridian plane measured from the X axis, and λ, the latitude; the corresponding coordinates of an observation station $O$ are $R _ { 0 }$ ， $\psi _ { 0 } ,$ and $\lambda _ { 0 }$

$( a )$ Determine the angle $\varphi$ measured from the $X$ axis to $r _ { s }$ in the plane of the orbit, in terms of $\psi _ { s } , \lambda _ { s } ,$ and α.

$( b )$ Determine the cosine of the angle between $R _ { 0 }$ and $r _ { g } ,$ and the straight-line distance between $o$ and $S _ { \mathrm { { \ell } } }$ Use $h$ for altitude.

(c) Determine the direction cosine of the line $o s$ relative to X, Y, Z.

(d) Determine the direction cosine of the line OS relative to a coordinate system x,y,z, with the origin at the observation station as shown.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0001_pages_0001-0070/auto/images/09b0b1593a2b5d2e3714fec14a55ef66cc84738260483da3a3154477fa768086.jpg)  
Prob. I1

12. A vehicle moving relative to the earth is located in terms of its position vector r from the center of earth. Place the $x$ y， $z$ axes with the origin coinciding with the moving vehicle, but with $z$ parallel to r. If the angular velocity of the x,y, z coordinate axes is $\omega = \omega _ { x } \mathbf { i } + \omega _ { y } \mathbf { j } + \omega _ { z } \mathbf { k }$ ，show that the x, y, z components of the absolute acceleration of the vehicle are,

$$
\begin{array} { r l } & { a _ { x } = \omega _ { x } \omega _ { z } r + \dot { \omega } _ { y } r + 2 \omega _ { y } \dot { r } } \\ & { a _ { y } = \omega _ { y } \omega _ { z } r - \dot { \omega } _ { x } r - 2 \omega _ { x } \dot { r } } \\ & { a _ { z } = \ddot { r } - ( \omega _ { x } { } ^ { 2 } + \omega _ { y } { } ^ { 2 } ) r } \end{array}
$$

13. Letting the direction cosines of a rotating coordinate system x, y， z be specified by

$$
\left| \begin{array} { l l l } { l _ { X x } } & { l _ { Y x } } & { l _ { Z x } } \\ { l _ { X y } } & { l _ { Y y } } & { l _ { Z y } } \\ { l _ { X z } } & { l _ { Y z } } & { l _ { Z z } } \end{array} \right|
$$

where $\iota _ { X y }$ is the cosine of the angle between $X$ and $y$ ,determine the equations for the unit vectors i', $\mathbf { j } ^ { \prime }$ ， $\mathbf { k } ^ { \prime }$ ,along x, $y , z$ ,in terms of the unit vectors i, j,k, along $X , ~ Y , Z$

14. If the $_ { x }$ ， $y$ ， $z$ coordinate system is rotating with angular velocity $\omega = \omega _ { x } \mathbf { i } ^ { \prime } +$ $\omega _ { y } { \bf j } ^ { \prime } + \omega _ { z } { \bf k } ^ { \prime }$ ,show that the velocities of the unit vectors are

$$
\begin{array} { l } { { \displaystyle { \frac { d } { d t } } { \bf i } ^ { \prime } = \omega _ { z } { \bf j } ^ { \prime } - \omega _ { y } { \bf k } ^ { \prime } } } \\ { { \displaystyle { \frac { d } { d t } } { \bf j } ^ { \prime } = \omega _ { x } { \bf k } ^ { \prime } - \omega _ { z } { \bf i } ^ { \prime } } } \\ { { \displaystyle { \frac { d } { d t } } { \bf k } ^ { \prime } = \omega _ { y } { \bf i } ^ { \prime } - \omega _ { x } { \bf j } ^ { \prime } } } \end{array}
$$

15.From Probs.13 and 14,show that the rate of change of the direction cosines between the $X , ~ Y , Z$ and $_ x$ ， $_ y$ ， $z$ axesis,

$$
\begin{array} { r l } & { i _ { X x } = \mathbf { i } ^ { \prime } \cdot \mathbf { i } = \omega _ { z } \mathbf { j } ^ { \prime } \cdot \mathbf { i } - \omega _ { \ast } \mathbf { k } ^ { \prime } \cdot \mathbf { i } } \\ & { \qquad = \omega _ { z } l _ { X y } - \omega _ { y } l _ { X z } } \\ & { i _ { Y x } = \omega _ { z } l _ { Y y } - \omega _ { y } l _ { Y z } } \end{array}
$$

etc. Complete the other seven equations.

16. The following relationship for the unit vector $\mathbf { k } ^ { \prime }$ can be written.

$$
\mathbf { k } ^ { \prime } = \mathbf { i } ^ { \prime } \times \mathbf { j } ^ { \prime } = { \left| \begin{array} { l l l } { \mathbf { i } } & { \mathbf { j } } & { \mathbf { k } } \\ { l _ { X x } } & { l _ { Y x } } & { l _ { Z x } } \\ { l _ { X y } } & { l _ { Y y } } & { l _ { Z y } } \end{array} \right| } = l _ { X z } \mathbf { i } + l _ { Y z } \mathbf { j } + l _ { Z z } \mathbf { k }
$$

This equation leads to the scalar equation

$$
l _ { X z } = l _ { Y \alpha } l _ { Z y } - l _ { Y y } l _ { Z x }
$$

and two others. Complete the nine scalar relationships of this type.

17. Derive the matrix Eq. 3.4-7.

# Particle Dynamics (Satellite Orbits)
