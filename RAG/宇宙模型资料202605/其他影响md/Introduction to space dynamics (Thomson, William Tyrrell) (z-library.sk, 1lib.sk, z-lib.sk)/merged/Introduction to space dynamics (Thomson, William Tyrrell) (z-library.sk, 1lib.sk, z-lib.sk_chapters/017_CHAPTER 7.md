# CHAPTER 7

# 7.l General Equations in Body Coordinates

For rockets and space vehicles it is often necessary to consider the general problem of the spinning body under thrust. The concern here is the body attitude and the motion of the center of mass. We will frst consider problems where the rate of mass variation is small enough to be negligible.

To outline the problem at hand, we willconsider a rigid body and define a set of body-fixed axes $x , y , z$ rotating with angular velocity $\omega$ ,and with the origin coinciding with the center of mass. Although it is always desirable to let the body axes coincide with the principal axes, this is often not possible, so that, in the general case, the moments and products of inertia will be defined as

$$
\begin{array} { r l } { I _ { x } = A \quad } & { { } I _ { x y } = D } \\ { I _ { y } = B \quad } & { { } I _ { x z } = E } \\ { I _ { z } = C \quad } & { { } I _ { y z } = F } \end{array}
$$

The angular momentum (Eq. 5.2-7) in the above notation becomes

$$
\begin{array} { r } { \mathbf { h } = ( A \omega _ { \alpha } - D \omega _ { y } - E \omega _ { z } ) \mathbf { i } + ( B \omega _ { y } - F \omega _ { z } - D \omega _ { x } ) \mathbf { j } } \\ { + ( C \omega _ { z } - E \omega _ { x } - F \omega _ { y } ) \mathbf { k } } \end{array}
$$

and the moment equation about the body axes

$$
\mathbf { M } = [ \dot { \mathbf { h } } ] + \boldsymbol { \omega } \times \mathbf { h }
$$

can be writen out in terms of the components given by Eq. 5.6-3 as

$$
\begin{array} { r } { M _ { x } = ( A \dot { \omega } _ { x } - D \dot { \omega } _ { y } - E \dot { \omega } _ { z } ) + ( C \omega _ { z } - E \omega _ { x } - F \omega _ { y } ) \omega _ { y } } \\ { - ( B \omega _ { y } - F \omega _ { z } - D \omega _ { x } ) \omega _ { z } } \\ { M _ { y } = ( B \dot { \omega } _ { y } - F \dot { \omega } _ { z } - D \dot { \omega } _ { x } ) + ( A \omega _ { x } - D \omega _ { y } - E \omega _ { z } ) \omega _ { z } } \\ { - ( C \omega _ { z } - E \omega _ { x } - F \omega _ { y } ) \omega _ { x } } \\ { M _ { z } = ( C \dot { \omega } _ { z } - E \dot { \omega } _ { x } - F \dot { \omega } _ { y } ) + ( B \omega _ { y } - F \omega _ { z } - D \omega _ { x } ) \omega _ { x } } \\ { - ( A \omega _ { x } - D \omega _ { y } - E \omega _ { z } ) \omega _ { y } } \end{array}
$$

Wenext letthe velocityof the centerof massbe expressed by the equation

$$
\mathbf { v } = v _ { x } \mathbf { i } + v _ { y } \mathbf { j } + v _ { z } \mathbf { k }
$$

and the force as

$$
\mathbf { F } = F _ { x } \mathbf { i } + F _ { y } \mathbf { j } + F _ { z } \mathbf { k }
$$

Since the x, y, $z$ coordinates are rotating with the body, the force components in the $x$ y， $z$ directions are determined from the equation

$$
\mathbf { F } = m \left[ { \frac { d \mathbf { v } } { d t } } \right] + { \boldsymbol { \omega } } \times m \mathbf { v }
$$

to be

$$
\begin{array} { r } { F _ { x } = m ( \dot { v } _ { x } + v _ { z } \omega _ { y } - v _ { y } \omega _ { z } ) } \\ { F _ { y } = m ( \dot { v } _ { y } + v _ { x } \omega _ { z } - v _ { z } \omega _ { x } ) } \\ { F _ { z } = m ( \dot { v } _ { z } + v _ { y } \omega _ { x } - v _ { x } \omega _ { y } ) } \end{array}
$$

If the resultant of the above forces does not pass through the center of mass coinciding with the origin of the $x , y , z ,$ axes, Eqs. (7.1-2) and (7.1-6) become coupled owing to the moment of the force. Also these equations define the motion of the body only in terms of the linear and angular velocities referred to body axes,and their solution and transformation to displacements and angles relative to inertial coordinates are problems of considerable difficulty which can be accomplished only under simplifying assumptions.

# 7.2 Thrust Misalignment

We will consider first a simple problem of a spinning missile with a misalignment of the thrust line. We will assume that the missile is symmetric so that the x, y, z, axes coincide with the principal axes 1,2, 3 with I = I = A and Ig = C. With A = B, we can rotate the 1, 2 axes so that one of these axes, say 1, is perpendicular to the plane containing the thrust and axis 3, as shown in Fig. 7.2-1.

Euler's equation for the missile is then

$$
\begin{array} { c } { { A \dot { \omega } _ { 1 } + ( C - A ) \omega _ { 2 } \omega _ { 3 } = M _ { 1 } } } \\ { { { } } } \\ { { A \dot { \omega } _ { 2 } - ( C - A ) \omega _ { 1 } \omega _ { 3 } = 0 } } \\ { { { } } } \\ { { C \dot { \omega } _ { 3 } = 0 } } \end{array}
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/b3be0e5fd95ce568c703bb7d3517ab53c86a827db96ec4fcd8196e6198977836.jpg)  
Fig.7.2-l. Thrust misalignment resulting in moment $M _ { 1 }$

The third equation tells us that $\omega _ { 3 } = n$ ， a constant. Although $C$ is generally less than $A$ for missiles, we let

$$
\lambda = n { \frac { C - A } { A } }
$$

as in Sec. 5.8-3 and rewrite the first two equations as

$$
\begin{array} { l } { { \displaystyle { \dot { \omega } } _ { 1 } + \lambda \omega _ { 2 } = \frac { M _ { 1 } } { A } } } \\ { { \displaystyle { \dot { \omega } } _ { 2 } - \lambda \omega _ { 1 } = 0 } } \end{array}
$$

For the solution of these equations, we willuse the technique used in Sec. 5.8 of adding $\omega _ { 1 }$ and $\omega _ { 2 }$ in quadrature. Multiplying Eq. 7.2-6 by

i=√-1,adingittEq.7-5dleting=+,et equations for $\omega _ { 1 }$ and $\omega _ { 2 }$ are replaced by one

$$
\dot { \omega } _ { 1 2 } - i \lambda \omega _ { 1 2 } = \frac { M _ { 1 } ( t ) } { A }
$$

Using the method of Laplace transformation, its subsidiary equation becomes

$$
\bar { \omega } _ { 1 2 } ( s ) = \frac { \omega _ { 1 2 } ( 0 ) } { s - i \lambda } + \frac { \bar { M } _ { 1 } ( s ) } { A ( s - i \lambda ) }
$$

and its solution given by its inverse is

$$
\omega _ { 1 2 } ( t ) = \omega _ { 1 2 } ( 0 ) e ^ { i \lambda t } + \frac { 1 } { A } \int _ { 0 } ^ { t } M _ { 1 } ( \tau ) e ^ { i \lambda ( t - \tau ) } d \tau
$$

The separation of this equation to ω1 and ωz is easily accomplished by noting its real and imaginary parts.

# PROBLEMS

1. From Eq. 7.2-6, $\omega _ { 1 } = ( 1 / \lambda ) \dot { \omega } _ { 2 }$ . Substitution into Eq. 7.2-5 results in

$$
\ddot { \omega } _ { 2 } + \lambda ^ { 2 } \omega _ { 2 } = \frac { \lambda } { A } M _ { 1 } ( t )
$$

Solve this equation for $\omega _ { 2 }$ and show that

$$
\omega _ { 2 } ( t ) = \omega _ { 2 } ( 0 ) \cos { \lambda t } + \frac { \dot { \omega } _ { 2 } ( 0 ) } { \lambda } \sin { \lambda t } + \frac { 1 } { A } \int _ { 0 } ^ { t } M _ { 1 } ( \tau ) \sin { \lambda ( t - \tau ) } d \tau
$$

2. From $\omega _ { 1 } = ( 1 / \lambda ) \dot { \omega } _ { 2 }$ and the solution of Prob. 1, determine the solution for $\omega _ { 1 } ( t )$

3. Note that the procedure of Prob. 2 encounters differentiation of an integral.

Let $\phi ( t ) = \int _ { a } ^ { b } F ( \tau , t ) d \tau = \int _ { 0 } ^ { t } M _ { 1 } ( \tau ) \sin \lambda ( t - \tau ) d \tau$ and use

$$
{ \frac { d \phi ( t ) } { d t } } = \int _ { a } ^ { b } { \frac { \partial F } { \partial t } } d \tau + F ( b , t ) { \frac { d b } { d t } } - F ( a , t ) { \frac { d a } { d t } }
$$

The result is

$$
\frac { d } { d t } \int _ { 0 } ^ { t } M _ { 1 } ( \tau ) \sin \lambda ( t - \tau ) d \tau = \lambda \int _ { 0 } ^ { \tau } M _ { 1 } ( \tau ) \cos \lambda ( t - \tau ) d \tau
$$

4. Separate the Eq. 7.2-9, $\omega _ { 1 2 } = \omega _ { 1 } + i \omega _ { 2 } ,$ into its real and imaginary parts and verify the solutions for $\omega _ { 1 }$ and $\omega _ { 2 }$ of Probs. 1, 2, and 3.

5.A symmetric body, $A$ ， $A$ ， $C _ { i }$ ，is damped with moments about the body-fixed axes as follows: M1 =-kω1,M = -kω, Mg= -kωg. Show that the angle between the spin axis, (axis 3) and the angular momentum vector is

$$
\tan \theta = \frac { | \omega _ { 1 2 } ( 0 ) | } { \omega _ { 3 } ( 0 ) } \frac { \mathcal { A } } { C } \exp \bigg [ - \bigg ( \frac { C } { A } - 1 \bigg ) \frac { k t } { C } \bigg ]
$$

6.A symmetrical satellite with moments of inertia $A$ ， $A$ ， $C$ is spinning with angular velocity $\omega$ about the axis of $C$ . If a constant torque $M _ { 1 }$ is applied to the transverse body-fixed pitch axis, show that the angular velocity of the satellite is

$$
\begin{array} { c } { { \omega _ { z } = n } } \\ { { { } } } \\ { { \omega _ { \tt I 2 } ( t ) = \omega _ { \tt I 2 } ( 0 ) e ^ { i \lambda t } - \frac { M _ { 1 } } { i \lambda A } \left( 1 - e ^ { i \lambda t } \right) } } \end{array}
$$

# 7.3 Rotations Referred to Inertial Coordinates

The solution of the previous problem is in terms of body-fixed coordinates which are rotating. In order to transform from the body-fixed coordinates to the inertial coordinates $X , ~ Y , Z$ it is necessry to introduce Euler's angles. From Eq. 3.5-1 the transformation is

$$
\begin{array} { r l } & { \omega _ { 1 } = \dot { \psi } \sin \theta \sin \varphi + \dot { \theta } \cos \varphi } \\ & { \omega _ { 2 } = \dot { \psi } \sin \theta \cos \varphi - \dot { \theta } \sin \varphi } \\ & { \omega _ { 3 } = \dot { \psi } \cos \theta + \dot { \varphi } = n \mathrm { a ~ c o n s t a n t ~ f o r ~ } M _ { 3 } = 0 } \end{array}
$$

Adding $\omega _ { 1 }$ and $\omega _ { 2 }$ in quadrature,

From $\omega _ { 3 }$

$$
\begin{array} { c } { { \omega _ { 1 2 } = \omega _ { 1 } + i \omega _ { 2 } = ( \dot { \theta } + i \dot { \psi } \sin \theta ) e ^ { - i \varphi } } } \\ { { { } } } \\ { { \dot { \psi } = \displaystyle \frac { n - \dot { \varphi } } { \cos \theta } } } \end{array}
$$

which,'substituted into Eq. 7.3-2,reults in

$$
\omega _ { 1 2 } = [ \dot { \theta } + i ( n - \dot { \varphi } ) \tan \theta ] e ^ { - i \varphi }
$$

Although this equation relates the angular velocity about the bodyfixed coordinates in terms of Euler's angles referenced to inertial axes, further simplification generally requires a smallangle approximation for $\theta$ Such an approximation is often justified when dealing with rockets and misiles whose spin axis must not deviate greatly from a fixed direction of flight.

When $\theta$ is small tan $\theta$ can be replaced by $\theta$

$$
\omega _ { 1 2 } = [ \dot { \theta } + i ( n - \dot { \varphi } ) \theta ] e ^ { - i \varphi }
$$

At this point we introduce a complex angle of atack， proposed by H.   
Leon4,5, which uncouples Eq. 7.3-5.

$$
\theta _ { 1 2 } = \theta e ^ { - i \varphi }
$$

Differentiating

$$
\dot { \theta } _ { 1 2 } = ( \dot { \theta } - i \dot { \varphi } \theta ) e ^ { - i \varphi }
$$

Equation 7.3-5 can then be written as

$$
\dot { \theta } _ { 1 2 } + i n \theta _ { 1 2 } = \omega _ { 1 2 }
$$

so that when @1z is a known function of time we have afirst-order ordinary differential equation in 012 to solve. It must be remembered however that the above procedure is limited to problems where $\theta$ is small.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/c52f61157ace623e6ce9bd07295de7f943507ed0ad13a57ff81e4cdb911c7c69.jpg)  
Fig.7.3-l. Velocity components in transverse plane tilted by angle 0.

At this point the significance of the term $e ^ { - i \phi }$ appearing in the various equations should be pointed out. For example, consider Eq. 7.3-2, which is

$$
\omega _ { 1 2 } = \omega _ { 1 } + i \omega _ { 2 } = ( \dot { \theta } + i \dot { \psi } \sin \theta ) e ^ { - i \varphi }
$$

All of the components in this equation lie in the tilted transverse plane which are shown in Fig. 7.3-1.

Writing $e ^ { - i \varphi } = ( \cos \varphi - i \sin \varphi ) , \omega _ { 1 2 }$ becomes

$$
\omega _ { 1 2 } = ( \dot { \theta } \cos \varphi + \dot { \psi } \sin \theta \sin \varphi ) + i ( \dot { \psi } \sin \theta \cos \varphi - \dot { \theta } \sin \varphi )
$$

The real and imaginary parts of this equation are, however, equal to the components of $\dot { \theta }$ and $\dot { \psi }$ sin $\theta$ along axes 1 and 2. Thus the inultiplication of the components $( \dot { \theta } + i \dot { \psi } \sin \theta )$ along the node coordinate system by $e ^ { - i \varphi }$ results in $\omega _ { 1 } + i \omega _ { 2 }$ ,the components along the body-fixed axes rotated through an angle $\boldsymbol { \psi }$ from the node axis. It follows logically then that, if we multiply the components $\omega _ { 1 } + i \omega _ { 2 }$ along the body axes by $e ^ { i \phi }$ ,we should obtain the vector $\omega _ { 1 2 }$ in terms of the node axis components as follows:

$$
( \omega _ { 1 } + i \omega _ { 2 } ) e ^ { i \varphi } = \omega _ { 1 2 } e ^ { i \varphi } = ( \dot { \theta } + i \dot { \psi } \sin \theta ) = \omega _ { \xi \eta }
$$

We can now attach physical significance to the complex angle of attack $\theta _ { 1 2 } = \theta e ^ { - i \varphi }$ .Since $\theta$ is multiplied by $e ^ { - i \varphi }$ ， $\theta _ { 1 2 }$ is resolved into components along the body-fixed axes 1 and 2. (Although an angle is strictly not representable as a vector, we have assumed $\theta$ to be small， thereby justifying its vector presentation.) To restore $\theta$ along its node axis we multiply $\theta _ { 1 2 }$ by $e ^ { i \varphi }$ i.e., $\theta = \theta _ { 1 2 } e ^ { i \varphi }$ .Furthermore,if we wish toexamine $\theta _ { 1 2 }$ in terms of inertial components, we need only to multiply $\theta$ by $e ^ { i \psi }$ (assuming $\psi$ measured in the $X Y$ plane to be equal to that measured in the tilted plane for $\theta$ small), or

$$
\begin{array} { c } { { \theta e ^ { i \psi } = ( \theta _ { 1 2 } e ^ { i \varphi } ) e ^ { i \psi } } } \\ { { { } } } \\ { { { } = \theta _ { 1 2 } e ^ { i ( \varphi + \psi ) } } } \\ { { { } } } \\ { { { } \cong \theta _ { 1 2 } e ^ { i n \ell } } } \end{array}
$$

where

$$
\varphi + \psi \cong \int ( \dot { \varphi } + \dot { \psi } \cos \theta ) d t \cong n t
$$

# Example 7.3-l

For a body of revolution $A$ ， $A$ ， $C$ , under moment-free condition,the complex angular rate from Eq. 7.2-9 is

$$
\omega _ { 1 2 } = \omega _ { 1 2 } ( 0 ) e ^ { i \lambda t }
$$

where $\lambda = n [ ( C - A ) / A ]$ . Substitution into Eq.7.3-8 results in the differential equation for the complex angle of attack

$$
\theta _ { 1 2 } + i n \theta _ { 1 2 } = \omega _ { 1 2 } ( 0 ) e ^ { i \lambda \ell } ~ .
$$

Letting $\bar { \theta } _ { 1 2 } ( s )$ be the Laplace transform of $\theta _ { 1 2 } ( t )$ , the subsidiary equation becomes

$$
\bar { \theta } _ { 1 2 } ( s ) = \frac { \theta _ { 1 2 } ( 0 ) } { s + i n } + \frac { \omega _ { 1 2 } ( 0 ) } { ( s + i n ) ( s - i \lambda ) }
$$

From its inverse, the solution for $\theta _ { 1 2 } ( t )$ is

$$
\begin{array} { l l r } { { \theta _ { 1 2 } ( t ) = \theta _ { 1 2 } ( 0 ) e ^ { - i n t } + \omega _ { 1 2 } ( 0 ) e ^ { - i n t } \int _ { 0 } ^ { t } e ^ { i ( \lambda + n ) \tau } d \tau } } \\ { { \ } } \\ { { = \theta _ { 1 2 } ( 0 ) e ^ { - i n t } + i \omega _ { 1 2 } ( 0 ) { \frac { e ^ { - i n t } } { n + \lambda } } [ 1 - e ^ { i ( n + \lambda ) t } ] } } \end{array}
$$

\*which is referred to body-fixed axes.

$e ^ { i n t }$ To examine the angle of attack interms of the inertial axes, we multiply by to obtain

$$
\begin{array} { l } { { \displaystyle \theta _ { X Y } ( t ) = \theta _ { 1 2 } ( 0 ) + i \frac { \omega _ { 1 2 } ( 0 ) } { n + \lambda } [ 1 - e ^ { i ( n + \lambda ) t } ] } \ ~ } \\ { { \displaystyle ~ = \left[ \theta _ { 1 2 } ( 0 ) + \frac { \omega _ { 1 2 } ( 0 ) } { n + \lambda } \sin { ( n + \lambda ) t } \right] + i \frac { \omega _ { 1 2 } ( 0 ) } { n + \lambda } [ 1 - \cos { ( n + \lambda ) t } ] } } \end{array}
$$

The real and imaginary components of 01(t) are along the X and Yaxes,the end of the vector 0xy(t） prescribing a circle of radius [ω12(O)l/(n +λ) about the center $\theta _ { 1 2 } ( 0 ) + i [ \omega _ { 1 2 } ( 0 ) \hat { ] } / ( n + \lambda )$ as shown in Fig. 7.3-2.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/fa5c148e0b98d8635c0a5a4e5055c29cc5b06a846b939970a9bdea0b67caec2e.jpg)  
Fig. 7.3-2. Inertial components of angle of attack 0.

# 7.4 Near Symmetric Body of Revolution with Zero Moment

When the geometric axes x, y, z corresponding to yaw, pitch, and spin of a missile are not principal axes, the solution in terms of such body coordinates will require the solving of the general Eq. 7.1-2. These equations do not lead to a simple solution, even for small products of inertia,and it is desirable to take a different approach.

We recognize first that every body has a set of principal axes 1, 2, 3. For the near symmetric body, the principal axis 3 deviates only by a small angle $\beta$ from the spin axis $z$ ，as shown in Fig. 7.4-1. Without loss of generality, the transverse axis $x$ can be chosen normal to the plane $z 0 3 .$ and the other two axes 1 and 2 are defined by the angle $\Phi$ between axis 1 and the transverse axis $x$ which intersects the planes 1, 2 and xy. Since both the 1, 2, 3 and $x , y , z$ axes are body-fixed axes, $\beta$ and $\Phi$ are constants.

If we assume that the principal inertias $I _ { 1 } \cong I _ { 2 }$ ， then elementary solutions are available in terms of principal axes 1,2,3. The motion of the geometric axes x, y, $z$ can then be obtained by a transformation of coordinates with $\beta$ and $\Phi$ known.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/61c032d44248418fe6f68a98b90de75b83b5c5f7d21f36cbf00dab853c75a562.jpg)  
Fig.7.4-l. Principalaxes1,2,3displaced from misile axesx,y, Ais $x$ is normal to plane z03.

We will assume that the moments and products of inertia about the missile axes $x , y , z$ are

$$
\begin{array} { r l } { I _ { x } = A \quad } & { { } I _ { x y } = D } \\ { I _ { y } = B \quad } & { { } I _ { x z } = E } \\ { I _ { z } = C \quad } & { { } I _ { y z } = F } \end{array}
$$

Theyarerelatedtotheprincipalmomentsof inertia $I _ { 1 } , \ I _ { 2 } , \ I _ { 3 }$ by the equations of Sec. 5.4 as follows:

$$
\begin{array} { r l } & { \quad A = l _ { x 1 } ^ { } l _ { 1 } ^ { } + l _ { x 2 } ^ { } l _ { 2 } ^ { } + l _ { x 3 } ^ { } { } ^ { } l _ { 3 } ^ { } = I _ { 1 } \cos ^ { 2 } \Phi + I _ { 2 } \sin ^ { 2 } \Phi } \\ & { \quad B = I _ { 1 } \sin ^ { 2 } \Phi + I _ { 2 } \cos ^ { 2 } \Phi + \beta ^ { 2 } I _ { 3 } } \\ & { \quad C = I _ { 1 } \beta ^ { 2 } \sin ^ { 2 } \Phi + I _ { 2 } \beta ^ { 2 } \cos ^ { 2 } \Phi + I _ { 3 } } \\ & { \quad - D = l _ { x 1 } l _ { y 1 } I _ { 1 } + l _ { x 2 } l _ { y 2 } I _ { 2 } + l _ { x 3 } l _ { y 3 } I _ { 3 } = ( I _ { 1 } - I _ { 2 } ) \sin \Phi \cos \Phi } \\ & { \quad - E = ( I _ { 1 } - I _ { 2 } ) \beta \sin \Phi \cos \Phi } \\ & { \quad - F = ( I _ { 1 } \sin ^ { 2 } \Phi + I _ { 2 } \cos ^ { 2 } \Phi ) \beta - \beta I _ { 3 } } \end{array}
$$

The direction cosines used in the above equations are obtained from the matrix transformation between coordinates x, y, z and 1, 2, 3 with lengths x',y',z' along it (see Sec. 5.4). Since β is small, the approximation sin $\beta = \beta$ and cos $\beta = 1$ is used:

$$
{ \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] } = { \left[ \begin{array} { l l l l } { \cos \Phi } & { - \sin \Phi } & { 0 } \\ { \sin \Phi \cos \beta } & { \cos \Phi \cos \beta } & { - \sin \beta } \\ { \sin \Phi \sin \beta } & { \cos \Phi \sin \beta } & { \cos \beta } \end{array} \right] } { \left[ \begin{array} { l } { x ^ { \prime } } \\ { y ^ { \prime } } \\ { z ^ { \prime } } \end{array} \right] }
$$

If we assume $I _ { 1 } = I _ { 2 } ,$ Eqs.7.4-1reduce to the following

$$
\begin{array} { r l r l } & { A = I _ { 1 } } & & { D = 0 } \\ & { B = I _ { 1 } + \beta ^ { 2 } I _ { 3 } } & & { E = 0 } \\ & { C = \beta ^ { 2 } I _ { 1 } + I _ { 3 } } & & { F = - \beta ( I _ { 1 } - I _ { 3 } ) } \end{array}
$$

and the angle $\beta$ becomes

$$
\beta = \frac { F } { I _ { 3 } - I _ { 1 } }
$$

To solve for the angular velocities， we first write down the transformation from the missile axes to the principal axes, assuming $\beta$ to be small:

$$
\left[ \begin{array} { c } { \omega _ { 1 } } \\ { \omega _ { 2 } } \\ { \omega _ { 3 } } \end{array} \right] = \left[ \begin{array} { c c c } { \cos \Phi } & { \sin \Phi } & { \beta \sin \Phi } \\ { - \sin \Phi } & { \cos \Phi } & { \beta \cos \Phi } \\ { 0 } & { - \beta } & { 1 } \end{array} \right] \left[ \begin{array} { c } { \omega _ { \omega } } \\ { \omega _ { y } } \\ { \omega _ { z } } \end{array} \right]
$$

Adding $\omega _ { 1 }$ and $i \omega _ { 2 }$ ，where $i = \sqrt { - 1 }$ ， we obtain the complex angular velocity

$$
\begin{array} { c } { { \omega _ { 1 2 } = \omega _ { 1 } + i \omega _ { 2 } = [ ( \omega _ { x } + i \omega _ { y } ) + i \beta \omega _ { z } ] e ^ { - i \Phi } } } \\ { { { } } } \\ { { \simeq ( \omega _ { x y } + i \beta n ) e ^ { - i \Phi } } } \end{array}
$$

where .By multiplying Eq. 7.4-6 by $e ^ { i \Phi }$ , this equation may also $\omega _ { z } \cong n$   
be written in the inverse form

$$
\omega _ { x y } = \omega _ { 1 2 } e ^ { i \Phi } - i \beta n
$$

Figure 7.4-2 shows the relationship between the missile axes $_ x$ y， $z .$ the principal axes 1, 2, 3, the inertial axes X, Y, Z,and the line of nodes 5. The missile axis $_ x$ is normal to axes 3 and $z$ , whereas the line of nodes $\xi$ is normal to axes $z$ and $Z$ ，The position of the missile axes $x$ y， $z$ is obtained by starting with the missile spin axis $z$ coinciding with $Z$ and performing three rotations as follows: (1) rotation of $\psi$ about $Z$ ； (2) rotation of $\theta$ about $\xi$ ; and (3) rotation of $\varphi$ about the spin axis $z$ . The principal axes 1,2, 3 are then referenced to the $x , y , z$ axes by the fixed angles $\beta$ and $\Phi$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/d9db6f9ec7bb51489c63f11c28e0d1247240efe260ac434a0466faaee7f69a3f.jpg)  
Fig.7.4-2. Principal axes 1, 2. 3 referred to misile axes x, y、=, which, in turn,are referred to node axis $\xi$ and inertial axes $X , Y , Z .$

From Ex. 7.3-1 we have the solution for the moment-free body in terms of the principal axes with $I _ { 1 } = I _ { 2 } ,$

$$
\begin{array} { l } { { \omega _ { 1 2 } = \omega _ { 1 2 } ( 0 ) e ^ { i \lambda t } } } \\ { { \nonumber } } \\ { { \theta _ { 1 2 } = \theta _ { 1 2 } ( 0 ) e ^ { - i n t } + i \displaystyle \frac { \omega _ { 1 2 } ( 0 ) } { n + \lambda } e ^ { - i n t } [ 1 - e ^ { i ( n + \lambda ) t } ] } } \end{array}
$$

where $\lambda = n [ ( I _ { 3 } - I _ { 1 } ) / I _ { 1 } ]$ . From Eq. 7.4-6, the initial value $\omega _ { 1 2 } ( 0 )$ is found to be

$$
\omega _ { 1 2 } ( 0 ) = [ \omega _ { x y } ( 0 ) + i \beta n ] e ^ { - i \Phi }
$$

Substituting Eq. 7.4-10 intoEq. 7.4-8,and Eq. 7.4-8 into Eq. 7.47, we have

$$
\omega _ { \alpha y } = \omega _ { x y } ( 0 ) e ^ { i \lambda t } - i \beta n ( 1 - e ^ { i \lambda t } )
$$

which transforms the complex angular rate solution to the misile axes x,y,z.

As discussed in Sec. 7.3, 0xv = 0e-i resolves 0 into components along the body-fixed axes x, y. It is also noted (see Fig. 7.4-2) that the angle β is a vector along axis x so that the components of θ and β along the x and y axes are

$$
\begin{array} { r } { ( \theta \cos \varphi + \beta ) - i ( \theta \sin \varphi ) = \theta e ^ { - i \varphi } + \beta } \\ { = \theta _ { \alpha y } + \beta } \end{array}
$$

To reference $\theta _ { x y } + \beta$ to the principal axes 1,2, we multiply by $e ^ { - i \Phi }$ and designate it as $\theta _ { 1 2 }$ ：

$$
\theta _ { 1 2 } = ( \theta _ { x y } + \beta ) e ^ { - i \Phi }
$$

Multiplying Eq. 7.4-13 by $e ^ { \imath \Phi }$ ,we obtain its inverse

$$
\theta _ { x y } = \theta _ { 1 2 } e ^ { i \Phi } - \beta
$$

Substituting for $\theta _ { 1 2 }$ from Eq. 7.4-9,

$$
\theta _ { x y } = \Big \{ \theta _ { 1 2 } ( 0 ) e ^ { - i n t } + i { \frac { \omega _ { 1 2 } ( 0 ) e ^ { - i n t } } { n + \lambda } } [ 1 - e ^ { i ( n + \lambda ) t } ] \Big \} e ^ { i \Phi } - \beta
$$

However, from Eq. 7.4-13,

$$
\theta _ { 1 2 } ( 0 ) = [ \theta _ { x y } ( 0 ) + \beta ] e ^ { - i \Phi }
$$

so by substituting from Eqs. 7.4-10 and 7.4-16 into Eq. 7.4-15,

$$
\begin{array} { l } { { \theta _ { x y } = \theta _ { x y } ( 0 ) e ^ { - i n \theta } + i \frac { \omega _ { x y } ( 0 ) e ^ { - i n \theta } } { n + \lambda } \left[ 1 - e ^ { i ( n + \lambda ) t } \right] } } \\ { { \ + \ \beta \Big \{ e ^ { - i n t } - \frac { n } { n + \lambda } e ^ { - i n \theta } \left[ 1 - e ^ { i ( n + \lambda ) t } \right] - 1 \Big \} } } \end{array}
$$

Equation 7.4-17 expresses the angle $\beta$ between the missile spin axis and the inertial $Z$ axis as a vector in the transverse plane with components along the rotating $x$ and $y$ axes,with $_ { x }$ real and $y$ imaginary. To examine this vector in the transverse inertial plane $X Y ,$ we multiply $\boldsymbol { \vartheta } _ { x y }$ by $e ^ { i n  t }$ to obtain

$$
_ { X Y } = \theta _ { x y } ( 0 ) + i \frac { \omega _ { x y } ( 0 ) } { n + \lambda } \{ 1 - e ^ { i ( n + \lambda ) t } \} + \beta \biggl [ \frac { \lambda } { n + \lambda } - e ^ { \imath n t } + \frac { n } { n + \lambda } e ^ { i ( n + \lambda ) t } .
$$

Comparing Eq. 7.4-18 with Eq. 7.3e, we find that the vector 0 in the inertial plane has an added term due to β. In addition to the precession speed (n + )， the effect of the product of inertia has introduced a component βeint which rotates at the spin speed n. The resull is a motion of the spin axis indicated by a curve, as shown in Fig. 7.4-3.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/925585ef64ea4ee7596628ede977a47c7d4ef05f0c2c460b94e70fe1f00decd0.jpg)  
Fig. 7.4-3. Possible motion of spin axis projected on inertial plane X, Y.

# PROBLEMS

1. Assume that the fuel consumption rate of a given missile with $A = 1 0 C$ is small enough to justify a constant mass analysis. If the thrust misalignment in the body coordinates is a constant and equal to $T e$ ,where $T$ is the thrust parallel to the longitudinal axis, and $e$ is its offset,etermine the equation for the complex angular velocity $\omega _ { 1 2 }$

2. When θ, the angle between the principal axis 3 and an inertial axis $Z$ is small, it can be represented as a vector. Along what axis do we represent this vector, and how do we resolve it into components along the rotating body axes with spin velocity $\dot { \mathcal { F } }$ . How do we resolve it into components along the inertial $X Y$ axes.

3. If we assume the velocity vector V of the center of mass of a missile to be fixed in space, determine for the moment-free missile the angle between V and the angular momentum vector h.

4. Defining the angle of attack of a missile as the angle between the longitudinal axis and the velocity vector V, show how this varies for the moment-free missile.

5. For a body of revolution $( A , A , C )$ ,the motion under moment-free conditions is described by a constant precession angle $\theta$ ,the plane containing the angular momentum h, the angular velocity $\boldsymbol { \omega }$ , and the spin axis 3 rotating about the fixed h vector at a rate $\dot { \psi } = C \dot { \varphi } / [ ( A - C ) \cos \theta ] = C n / ( A \cos \theta )$ Show that the results of Example 7.3-1 are consistent with this requirement provided $\theta _ { 1 2 }$ ,the angle of attack is small.

6. If the missile of Prob.1 is spinning at a rate $n = 2 \pi$ rad/sec,determine the complex angle of attack relative to inertial space,and plot the results in the $X Y$ plane.

7. If the geometric axes x, $y , z$ of a near symmetric missile deviates from the principal axes1,2,3bythengles $\beta$ and $\Phi$ ,where $\beta$ is a small angle between the z axis and the principal axis 3, show that the assumption of I1 = I2 results in $\Phi = \pi$ Physically what does this mean?

8. Show that in the general case for sall can be solved for $\beta$ as $\beta$ ,where $\Phi$ may not be $^ { - 7 7 }$ ,Eq. 7.4-1

$$
\beta = { \sqrt { \frac { F D + E ( B - C ) } { F D } } }
$$

9. The principal moment of inertia ratio $I _ { 3 } / I _ { 1 }$ for a near symmetrical satellite is givenas1.20and the principalaxis3is tilted from the geometric ais $z$ by the angle $\beta = 0 . 0 5$ rad. If the spin rate $n = 2 \pi$ rad/sec and $\{ \omega _ { x y } ( 0 ) ] / n =$ $\varkappa _ { 1 0 }$ , determine the complex angle of attack relative to inertial space and show how the geometric axis $z$ is moving in a plane normal to the velocity vector.

10. Using the equation for $\omega _ { 1 2 } ( t )$ of Prob. 6, p. 198,in Eq. 7.3-8 shows that the angle $\theta _ { X Y }$ referred to inertial axes is given by the equation

$$
\theta _ { X Y } = \theta _ { 1 2 } ( 0 ) + \frac { i \omega _ { 1 2 } ( 0 ) } { n + \lambda } [ 1 - e ^ { i ( n + \lambda ) t } ] - \frac { M _ { 1 } } { n \lambda A } \bigg [ \frac { \lambda } { n + \lambda } - e ^ { i n t } + \frac { n } { n + \lambda } e ^ { i ( n + \lambda ) t } \bigg ]
$$

11. Body axes $_ { x }$ ， $y$ ,and $\scriptscriptstyle *$ initially coinciding with the inertial axes $X , ~ Y ,$ and $Z$ are given the following sequence of rotations. Rotation $\theta _ { 3 }$ about $z$ followed by rotation $\theta _ { 2 }$ about the displaced $y$ axis and a rotation $\theta _ { 1 }$ about the final position of the $x$ axis. Derive the transfer matrix expressing the body axes in terms of the inertial axes, and its inverse.

12.Assume angular velocities $\dot { \theta } _ { 3 }$ $\dot { \theta } _ { 2 }$ and $\dot { \theta } _ { 1 }$ about axes $z$ y,and $_ { x }$ in the sequence given by Prob.11,and write the equations for theangular velocities $\omega _ { 1 } , \omega _ { 2 } ,$ and $\omega _ { 3 }$ about the final position of the body axes x, y, z.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/b5ecd9f3ab3ad3597ab57568a44fec7974a24eee83840ca838227a286aeb225b.jpg)  
Prob. 12

13. Referring to the figure of Prob. 12, assume the missile to be symmetric so that $I _ { y } = I _ { z }$ ,and determine the equation for the attitude deviation $\theta _ { 2 } + i \theta _ { 3 }$ of the longitudinal axis due to a constant yawing torque $M _ { z }$

14. A space vehicle of moment of inertia $I _ { 1 }$ $I _ { 2 } ,$ and $I _ { 3 }$ is in a circular orbit with constant angular velocity ωg about the axis 2 to maintain the direction of axis I always tangent to the orbit as shown in the sketch. Assuming small disturbances $\dot { \theta } _ { 1 } ,$ $\check { \theta } _ { 2 } ^ { - }$ ， $\dot { \theta } _ { 3 }$ , derive the differential equation of motion for the torques about the body axes 1, 2, and 3.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/618fb9d853333b2971be3a09d9e5644d761a5e8abd456c41a3776b3ca56ff2e3.jpg)  
Prob.14

15. Assume the body axes 1, 2,and 3 of the space vehicle of Prob. 14 to deviate from the orbit axes $1 ^ { \prime }$ ， $2 ^ { \prime }$ and $3 ^ { \prime }$ by angles $\theta _ { 3 }$ ， $\theta _ { 2 }$ ,and $\theta _ { 1 }$ in the sequence specified in Prob. 11. Using the procedure of Sec. 4.18 and a spherical earth, show that the gravity force on the space vehicle results in torques about the body axes equal to

$$
\begin{array} { l } { { \displaystyle M _ { 1 } = \frac { 3 K } { 2 { R _ { 0 } } ^ { 3 } } \left( I _ { 3 } - I _ { 2 } \right) \sin 2 \theta _ { 1 } \cos ^ { 2 } \theta _ { 2 } } } \\ { { \displaystyle M _ { 2 } = \frac { 3 K } { 2 { R _ { 0 } } ^ { 3 } } \left( I _ { 3 } - I _ { 1 } \right) \sin 2 \theta _ { 2 } \cos \theta _ { 1 } } } \\ { { \displaystyle M _ { 3 } = \frac { 3 K } { 2 { R _ { 0 } } ^ { 3 } } \left( I _ { 1 } - I _ { 2 } \right) \sin 2 \theta _ { 2 } \sin \theta _ { 1 } } } \end{array}
$$

where $K = G n _ { e }$ and $R _ { 0 }$ is distance from the center of earth to the vehicle center of mass

# 7.5 Despinning of Satellites

In the design of satellites it is often necessary to provide means for reducing the spin of a spin-stabilized satellte while in orbit to allow proper functioning of instruments. Figure $7 . 5 \mathrm { - } 1 ^ { \ast }$ shows a simple device,7 used in the Pioneer III lunar probe, which is capable of reducing the spin to zero. It consists of a small mass $m$ on the end of a light cord wrapped around \* To maintain symmetry two such masses are released.

the symmetrical spinning body. With the satelite spinning with speed ωo about its axis of symmetry,the mass m is released. The cord wil now unwind and the angular speed of the satelite will gradually decrease.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/fb22c7ca57f1b10436fb3859ea71718c119bbda9e1c91add2043a8299041b016.jpg)  
Fig.7.5-l. Despinning device for a satellite.

When the cord is completely unwound,it is released and allowed to fly away. By choosing the length of the cord properly, the spin of the satelite can be reduced to any value less than the initial value.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/a0155d22f9cbec890063162f5dd3209883712bffeddfe72b2d3a4f96c7a33c15.jpg)  
Fig. 7.5-2. Unwinding of mass m.

The device may be analyzed as follows. Since $m$ is small, the body may be assumed to spin about the geometric axis of symmetry of the body 0, with moment of inertia I and angular velocity ω. We attach the X, Y coordinate axes to the body and allow a second set of axes x, y to rotate relative to the body so that the y axis always passes through the tangent point of the cord, as shown in Fig. 7.5-2.

We will assume that initially $^ m$ was in contact with the cylinder at the $X$ axis, in which case the Iength of cord extending beyond the tangent point is equal to the arc length $R \phi$ . The position of $m$ is then,

$$
{ \bf r } = R \phi { \bf i } + R { \bf j }
$$

Since the axes $x , y$ are rotating with speed $( \omega + { \dot { \phi } } ) \mathbf { k }$ , the velocity of $m$ is

$$
\begin{array} { l } { { \displaystyle { \mathfrak { v } } = { \dot { \mathfrak { r } } } + ( \omega + { \dot { \phi } } ) { \bf k } \times { \mathfrak { r } } } \ ~ } \\ { { \displaystyle = R { \dot { \phi } } { \dot { \bf i } } + ( \omega + { \dot { \phi } } ) R \phi { \bf j } - ( \omega + { \dot { \phi } } ) R { \dot { \bf i } } } \ ~ } \\ { { \displaystyle = - R \omega { \dot { \bf i } } + R \phi ( \omega + { \dot { \phi } } ) { \bf j } } \ ~ } \end{array}
$$

The angular momentum of the mass $m$ is,

$$
\begin{array} { r l } & { \mathbf { h } = \mathbf { r } \times m \mathbf { v } } \\ & { \mathbf { \epsilon } = ( R \phi \mathbf { i } + R \mathbf { j } ) \times m [ - R \omega \mathbf { i } + R \phi ( \omega + \dot { \phi } ) \mathbf { j } ] } \\ & { \mathbf { \epsilon } = m R ^ { 2 } [ \omega + \phi ^ { 2 } ( \omega + \dot { \phi } ) ] \mathbf { k } } \end{array}
$$

and the total angular momentum is

$$
{ \bf H } = \{ I \omega + m R ^ { 2 } [ \omega + \phi ^ { 2 } ( \omega + \dot { \phi } ) ] \} { \bf k }
$$

The system kinetic energy $T$ is the sum of the kinetic energy of the satellite and $m$ ·

$$
\begin{array} { c } { { T = \frac 1 2 I \omega ^ { 2 } + \frac 1 2 m v ^ { 2 } } } \\ { { = \frac 1 2 I \omega ^ { 2 } + \frac 1 2 m \{ ( R \omega ) ^ { 2 } + [ R \phi ( \omega + \dot { \phi } ) ] ^ { 2 } \} } } \\ { { = \frac 1 2 I \omega ^ { 2 } + \frac 1 2 m R ^ { 2 } [ \omega ^ { 2 } + \phi ^ { 2 } ( \omega + \dot { \phi } ) ^ { 2 } ] } } \end{array}
$$

Since the system has no external forces and no dissipation of energy, the kinetic energy and angular momentum must remain constant and equal to their initial values.Letting the spinrate at $t = 0$ be $\omega _ { \boldsymbol { \rho } }$ ，

$$
T = { \scriptstyle { \frac { 1 } { 2 } } } ( I + m R ^ { 2 } ) \omega _ { 0 } { \scriptstyle { ^ 2 } } = { \scriptstyle { \frac { 1 } { 2 } } } I \omega ^ { 2 } + { \scriptstyle { \frac { 1 } { 2 } } } m R ^ { 2 } [ \omega ^ { 2 } + \phi ^ { 2 } ( \omega + \dot { \phi } ) ^ { 2 } ]
$$

$$
\begin{array} { c }  { { \cal I } ~ = ~ \dot { \hat { \imath } } { } [ \imath ~ + m { \cal K } ^ { \circ } ) \omega _ { 0 } { } ^ { * } ~ = ~ \dot { \hat { \imath } } { } ^ { I } \omega ^ { * } + \dot { \hat { \imath } } { } ^ { m } { \cal K } ^ { \circ } { } [ \omega ^ { * } + \phi ^ { * } ( \omega + \phi } \\ { { } } \\ { { { \cal H } ~ = ( { \cal I } + m { \cal R } ^ { 2 } ) \omega _ { 0 } { } ~ = ~ { \cal I } \omega + m { \cal R } ^ { 2 } [ \omega + \phi ^ { 2 } ( \omega + \dot { \phi } ) ] } } \end{array}
$$

Dividing through by $m R ^ { 2 }$ the two equations become,

where

$$
\begin{array} { c } { { C ( \omega _ { 0 } { } ^ { 2 } - \omega ^ { 2 } ) = \phi ^ { 2 } ( \omega + \dot { \phi } ) ^ { 2 } } } \\ { { C ( \omega _ { 0 } - \omega ) = \phi ^ { 2 } ( \omega + \dot { \phi } ) } } \\ { { { } } } \\ { { C = \displaystyle \frac { I } { m R ^ { 2 } } + 1 } } \end{array}
$$

Dividing the first equation by the second, we find,

$$
\omega + \omega _ { 0 } = \omega + \dot { \phi }
$$

Therefore,

$$
\begin{array} { r } { \omega _ { 0 } = \dot { \phi } } \\ { \omega _ { 0 } t = \dot { \phi } } \end{array}
$$

which tels us that the mass m unwinds at a constant rate. Substituting for $\phi$ and $\dot { \phi }$ in Eq.7.5-9,the spinrate at any time becomes

$$
\omega = \omega _ { 0 } \Big ( \frac { C - \phi ^ { 2 } } { C + \phi ^ { 2 } } \Big ) = \omega _ { 0 } \Big ( \frac { C - { \omega _ { 0 } } ^ { 2 } t ^ { 2 } } { C + { \omega _ { 0 } } ^ { 2 } t ^ { 2 } } \Big )
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/131b36df6a037d67fde59f218334b6b00060b254fa1f82f1b8bb4ef8280a78dc.jpg)  
Fig. 7.5-3. Despining of satellites.

The spin may be reduced to any desired value $\omega _ { f }$ by choosing the proper length of cord, and releasing it when completely unwound. If $l _ { f }$ is the length selected, the terminal value of $\phi$ is,

$$
\phi _ { f } = \frac { l _ { f } } { R }
$$

and from Eq. 7.5-12,

$$
\omega _ { f } = \omega _ { 0 } \bigg ( \frac { C - \phi _ { f } { } ^ { 2 } } { C + \phi _ { f } { } ^ { 2 } } \bigg ) = \omega _ { 0 } \bigg ( \frac { C R ^ { 2 } - l _ { f } { } ^ { 2 } } { C R ^ { 2 } + l _ { f } { } ^ { 2 } } \bigg )
$$

Solving for $l _ { f } ,$ the required length of cord is,

$$
l _ { f } = R \sqrt { C \frac { \omega _ { 0 } - \omega _ { f } } { \omega _ { 0 } + \omega _ { f } } }
$$

If the terminal angular velocity is to be zero, $l _ { f }$ becomes,

$$
\begin{array} { c } { l _ { f } = R \sqrt { C } } \\ { = \sqrt { R ^ { 2 } + \displaystyle \frac { I } { m } } } \end{array}
$$

For symmetry, two cords with masses $\nu _ { 2 m } ^ { \prime }$ can be used as shown in Fig. 7.5-3, the result being the same as that for one mass of value $m$

# Example 7.5-l

The Pioneer III lunar probe was launched with an initial spin rate of $4 0 0 \ \mathrm { r p m }$ It was desired to reduce this to $5 . 5 ~ \mathrm { r p m }$ by using a yo-yo with two weights of 0.2 oz each.

For Pioneer III

$$
\begin{array} { l } { { \displaystyle g I = 9 2 \ \mathrm { l b } \ \mathrm { i n } . ^ { 2 } \ } } \\ { { \displaystyle R = 5 \ \mathrm { i n } . } } \\ { { \displaystyle C = \frac { 9 2 } { ( 0 . 4 / 1 6 ) 5 ^ { 2 } } + 1 = 1 4 8 } } \end{array}
$$

From Eq. 7.5-15 the proper length of cord is,

$$
l = 5 { \sqrt { 1 4 8 { \frac { 4 0 0 - 5 . 5 } { 4 0 0 + 5 . 5 } } } } = 6 0 \mathrm { i n } .
$$

# 7.6 Attitude Drift of Space Vehicles

The attitude of a body of revolution spinning in the absence of external forces is not a constant when energy disspation takes place. Elastic vibrations,induced by gyroscopic action,result in a disspation of energy and a change in the precession cone angle $\theta$ . In this section we examine the effect of energy dissipation on the spinning body and evaluate the time required for a body of given configuration to undergo a specifed change in attitude.8

The moment-free motion of an unsymmetric body with principal moments of inertia $A$ ， $\mathcal { B }$ ， $C$ is an unsteady periodic precession and nutation about the resultant angular momentum vector h fixed in space. Steady rotation is possible only about the principal axis of maximum or minimum moment of inertia, the principal axis of intermediate moment of inertia being unstable.

For a body of revolution $A$ ， $A$ ， $C$ , the moment-free motion is a steady precession of the spin axis at a constant angle $\theta$ about the resultant angular momentum vector h fixed in space. Steady rotation is again possible about the axis of maximum or minimum moment of inertia,and the axis of intermediate moment of inertia does not exist.

In either case, the axis of maximum or minimum moment of inertia is considered to be stable in that,if the spin axis deviates slightly from the resultant angular momentum vector, there is no tendency for this deviation to grow.This statement istrue only fora perfectly rigid body in the absence of external moment.

In an elastic body,deformation between particles willalways take place, resulting in some dissipation of energy. When the dissipation of energy is taken into account, we must revise our statement of stability in that it is possible for a small deviation of the spin axis to grow into a large one and, eventually,to result in a complete change in attitude of the body. For such bodies,only the principal axis of maximum moment of inertia is stable, and the axis of minimum moment of inertia is one of unstable equilibrium.

These facts were actually observed in the Explorer I satelite,6 which was spin-stabilized about the longitudinal axis of minimum moment of inertia. The flexible antennas of the satelite provided an excellent source for energy dissipation, and in one revolution around its orbit (approximately 90 min) the Explorer I was observed to be tumbling at an attitude of 0 = 6O° instead of spinning about its longitudinal axis at 0 = 0. The remedy for this behavior is obviously to shorten thelongitudinaldimensions of the satellite so that the moment of inertia about the longitudinal spin axis is greater than that about the transverse pitch or yaw axis. However, the problem still exists for missiles which are long, slender bodies and inherently unstable about the spin axis. Here the important question is how long can the spinning missile coast in a moment-free condition without an appreciable change in its attitude.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/fc2bd5079121c1475761f677470583894d3716c4fe350d92eeb8a05fd3460767.jpg)  
Fig. 7.6-l. Coordinate system of body axes 1, 2, 3.

# Energy considerations of stability

We will now examine the basis for stability from an energy point of view. For a body of revolution with principal moments of inertia A, A, C, as shown in Fig. 7.6-1, the moment-free motion is that of steady precession described by the equations

$$
{ \dot { \psi } } = { \frac { C { \dot { \varphi } } } { \left( A - C \right) \cos \theta } } = { \frac { C } { A } } { \frac { \omega _ { 3 } } { \cos \theta } }
$$

$$
\omega _ { 3 } = \dot { \varphi } + \dot { \psi } \cos \theta
$$

Since the moment is zero, the angular momentum vector h is a constant and we can write for the square of its magnitude the equation

$$
h ^ { 2 } = A ^ { 2 } ( \omega _ { 1 } { } ^ { 2 } + \omega _ { 2 } { } ^ { 2 } ) + C ^ { 2 } \omega _ { 3 } { } ^ { 2 }
$$

We next examine the kinetic energy of rotation, $T$ ， which is given by the equation

$$
2 T = A ( \omega _ { 1 } { ^ { 2 } } + \omega _ { 2 } { ^ { 2 } } ) + C \omega _ { 3 } { ^ { 2 } }
$$

Multiplying Eq. 7.6-3 by $A$ and subtracting from Eq. 7.6-2,

$$
h ^ { 2 } - 2 T A = C ( C - A ) { \omega _ { 3 } } ^ { 2 }
$$

and since $C \omega _ { 3 } = h$ cos $\theta$ , we obtain the relationship for cos $\theta$ in terms of $h$ and $T$ as follows

$$
h ^ { 2 } - 2 T A = { \frac { h ^ { 2 } } { C } } ( C - A ) \cos ^ { 2 } \theta
$$

Equation 7.6-5 indicates that $\theta$ remains constant provided $T$ and h are constant. However energy dissipation under zero external moment is possible, in which case $T$ must decrease while $h$ remains constant. Differentiating Eq. 7.6-5, we obtain

$$
\dot { T } = \frac { h ^ { 2 } } { C } \bigg ( \frac { C } { A } - 1 \bigg ) ( \sin { \theta } \cos { \theta } ) \dot { \theta }
$$

and with $\dot { T }$ a negative quantity, $\dot { \theta }$ is negative for $C / A > 1$ and positive for $C / A < 1$ . Thus the principal axis of minimum moment of inertia is one of unstable equilibrium, and a small deviation of the spin axis will increase due to energy dissipation when $C / A < 1$

# Dissipation of energy

Assuming an elastic body, the energy dissipated per unit volume per cycle of stress can be assumed to be

$$
\frac { \gamma \sigma ^ { 2 } } { 2 E }
$$

where y is a hysteretic damping factor establishing the fraction of the elastic energy which is dissipated as shown by the shaded area in Fig. 7.6-2. Dividing by the time t0 per cycle of stress, and integrating over the entire structure, the rate of energy dissipation can be found. Thus the equation to be solved is of the general form

$$
\int { \frac { \gamma \sigma ^ { 2 } } { 2 E t _ { 0 } } } d V = { \frac { h ^ { 2 } } { C } } \bigg ( { \frac { C } { A } } - 1 \bigg ) ( \sin \theta \cos \theta ) \dot { \theta }
$$

In examining the source of cyclic stressing， free vibrations can be discarded since they will soon damp out. Steady cycling of stress is

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/6feeb8319653d56d40fd5f3d7685abcaaebbca68545740532bac95c3f3e5b4a6.jpg)  
Fig. 7.6-2. Energy dissipated by hysteresis damping.

however induced by the gyroscopic precession， and these stresses are repeated at the rate $\dot { \varphi }$ and $2 \dot { \varphi }$ ,as we will presently show.

The excitation for the cyclic stress is the acceleration. Choosing an arbitrary point on the structure and orienting the plane 1, O, 3 through it, the position vector for the specified point is

$$
\mathbf { r } = \xi \mathbf { i } + z \mathbf { k }
$$

With $\dot { \theta }$ small, the angular velocity and acceleration of the coordinate axes 1, 2, 3 are

$$
\begin{array} { r l } & { \mathbf { \boldsymbol { \omega } } = ( \dot { \psi } \sin \theta \sin \varphi ) \mathbf { \boldsymbol { \mathbf { i } } } + ( \dot { \psi } \sin \theta \cos \varphi ) \mathbf { \boldsymbol { \mathbf { j } } } + ( \dot { \varphi } + \dot { \psi } \cos \theta ) \mathbf { \boldsymbol { \mathbf { k } } } } \\ & { \dot { \mathbf { \boldsymbol { \omega } } } = \dot { \varphi } \dot { \psi } \sin \theta ( \cos \varphi \mathbf { \boldsymbol { \mathsf { i } } } - \sin \varphi \mathbf { \dot { \boldsymbol { \mathsf { j } } } } ) } \end{array}
$$

Substituting into the general vector equation for the acceleration

$$
{ \mathrm {  ~ a ~ } } = { \mathrm {  ~ a _ { 0 } ~ } } + [ { \mathrm {  ~ a ~ } } ] + { \boldsymbol { \omega } } \times ( { \boldsymbol { \omega } } \times { \mathrm {  ~ r ) } } + { \dot { \boldsymbol { \omega } } } \times { \mathrm {  ~ r ~ } } + 2 { \boldsymbol { \omega } } \times [ { \mathrm {  ~ v } } ]
$$

and noting that the following quantities are zero

$$
\mathbf { a } _ { 0 } = [ \mathbf { a } ] = [ \mathbf { v } ] = 0
$$

the result after some algebraic reduction is

$$
\begin{array} { r l } { \mathbf { \Phi } } & { = [ - \xi ( \dot { \varphi } ^ { 2 } + \dot { \psi } ^ { 2 } ) + \xi \dot { \psi } ^ { 2 } \sin ^ { 2 } \theta \sin ^ { 2 } \varphi - 2 \xi \dot { \varphi } \dot { \psi } \cos \theta + z \dot { \psi } ^ { 2 } \sin \theta \cos \theta \sin \varphi ] } \\ { \mathbf { \Phi } } & { + ( \xi \dot { \psi } ^ { 2 } \sin ^ { 2 } \theta \sin \varphi \cos \varphi + z \dot { \psi } ^ { 2 } \sin \theta \cos \theta \cos \varphi ) ] } \\ { \mathbf { \Phi } } & { + ( 2 \xi \dot { \varphi } \dot { \psi } \sin \theta \sin \varphi + \xi \dot { \psi } ^ { 2 } \sin \theta \cos \theta \sin \varphi - z \dot { \psi } ^ { 2 } \sin ^ { 2 } \theta ) \mathbf { k } \quad ( 7 . 6 - 1 3 \cos \theta \cos \varphi ) } \end{array}
$$

A somewhat more convenient form of Eq. 7.6-13 results by eliminating $\dot { \varphi }$ and $\dot { \psi }$

$$
\begin{array} { r l } & { \mathbf { a } = \omega _ { 0 } ^ { 2 } \Big \{ - \xi \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } + \xi \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } \sin ^ { 2 } \theta \sin ^ { 2 } \varphi + \xi \Big [ \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } - 1 \Big ] \cos ^ { 2 } \theta } \\ & { \qquad + z \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } \sin \theta \cos \theta \sin \varphi \Big \} \mathbf { i } } \\ & { \qquad + \omega _ { 0 } ^ { 2 } \Big [ \xi \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } \sin ^ { 2 } \theta \sin \varphi \cos \varphi + z \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } \sin \theta \cos \theta \cos \varphi \Big ] \Big \} } \\ & { \qquad + \omega _ { 0 } ^ { 2 } \Big [ - \xi \Big ( \displaystyle \frac { C } { A } \Big ) \Big ( \displaystyle \frac { C } { A } - 2 \Big ) \sin \theta \cos \theta \sin \varphi - z \Big ( \displaystyle \frac { C } { A } \Big ) ^ { 2 } \sin ^ { 2 } \theta \Big ] \mathbf { k } } \end{array}
$$

Since the only time-varying quantity in Eq. 7.6-14 (assuming $\dot { \theta }$ to be negligible) is $\varphi = { \dot { \varphi } } t$ , it is evident that the cyclic stress is repeated at a rate $\dot { \varphi }$ and $2 \dot { \varphi }$ . It should be pointed out that, for slender bodies like missiles, $C / A$ is small compared to unity,and the predominant variable acceleration term is

$$
\mathbf { a } = 2 \omega _ { 0 } ^ { \ 2 } \xi \left( { \frac { C } { A } } \right) \sin \theta \cos \theta \sin \varphi \mathbf { k }
$$

which is repeated in the time

$$
t _ { 0 } = \frac { 2 \pi } { \dot { \varphi } } = \frac { 2 \pi } { [ 1 - ( C / A ) ] \omega _ { 0 } \cos \theta }
$$

# Example 7.6-l

As an example of the simplest kind, we will consider two solid disks connected by a flexible tube,as shown in Fig.7.6-3. We wil let $C _ { 1 }$ and $A _ { 1 }$ be themoments of inertia of each disk about its own polar and diametric axes. The gyroscopic moment required by each disk is

$$
M _ { g } = C _ { 1 } ( \dot { \varphi } + \dot { \psi } \cos \theta ) \dot { \psi } \sin \theta - A _ { 1 } \dot { \psi } ^ { 2 } \sin \theta \cos \theta
$$

Since the moments of inertia about the center of mass of the body are

$$
\begin{array} { l } { { C = 2 C _ { 1 } } } \\ { { A \cong 2 ( A _ { 1 } + m _ { 1 } l ^ { 2 } ) } } \end{array}
$$

Equation a can be rewritten as

$$
\begin{array} { r } { M _ { g } = \frac { 1 } { 2 } [ C ( \dot { \varphi } + \dot { \psi } \cos \theta ) \dot { \psi } \sin \theta - \mathcal { A } \dot { \psi } ^ { 2 } \sin \theta \cos \theta ] + m _ { 1 } l ^ { 2 } \dot { \psi } ^ { 2 } \sin \theta \cos \theta } \end{array}
$$

Thefirsterm,however,isthemomentabout thecenterofmasswhichiszeroand from which Eq.7.6-1 is obtained. We are thus left with

$$
\begin{array} { c } { { M _ { g } = m _ { 1 } l ^ { 2 } \dot { \psi } ^ { 2 } \sin \theta \cos \theta } } \\ { { = F l \cos \theta } } \end{array}
$$

where $F = m _ { 1 } l { \dot { \psi } } ^ { 2 }$ sin $\theta$ is the centripital force of the precessing disk.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/9930c94bd0269a593845ef4a2de2cd341117b8e4e7e330cdf9ead45e24f60695.jpg)  
Fig.7.6-3. Satelite configuration, displacement,and moment distribution.

The effect of $M _ { g }$ and $F$ on the flexible tube is shown in Fig. 7.6-3. At point z along the tube, measured from the center of mass, the bending moment is

$$
M _ { z } = M _ { g } { \frac { z } { l } }
$$

and the expression for the maximum stress becomes

$$
\begin{array} { c } { { \sigma = \displaystyle \frac { M _ { z } \xi } { I } = m _ { 1 } l ^ { 2 } \dot { \psi } ^ { 2 } \stackrel { z } { l } \stackrel { \xi } { \frac { I } { I } } \sin \theta \cos \theta } } \\ { { = \displaystyle \frac { 1 } { 2 } m l ^ { 2 } \biggl ( \frac { C } { A } \biggr ) ^ { 2 } { \omega _ { 0 } } ^ { 2 } \stackrel { z } { \overline { { { l } } } } \stackrel { \xi } \sin \theta \cos \theta } } \end{array}
$$

which is repeated at the rate given by Eq. 7.6-15. The rate of energy dissipation as given by the left side of Eq. 7.6-8 is then

$$
\frac { \gamma } { 4 8 \pi E } \bigg ( \frac { m l ^ { 2 } \xi } { I } \bigg ) ^ { 2 } V \bigg ( \frac { C } { A } \bigg ) ^ { 4 } \bigg ( \frac { C } { A } - 1 \bigg ) \omega _ { 0 } { } ^ { 5 } \sin ^ { 2 } \theta \cos ^ { 3 } \theta
$$

and the rate of change of the attitude angle $\theta$ becomes

$$
\begin{array} { l } { { \displaystyle \dot { \theta } = \frac { \gamma } { 4 8 \pi E } \bigg ( \frac { m l ^ { 2 } \xi } { I } \bigg ) ^ { 2 } \frac { V } { C } \bigg ( \frac { C } { A } \bigg ) ^ { 4 } \omega _ { 0 } { } ^ { 3 } \sin \theta \cos ^ { 2 } \theta } } \\ { { \mathrm { } = K \sin \theta \cos ^ { 2 } \theta } } \end{array}
$$

A plot of Eq. $f$ is shown in Fig. 7.6-4. Since $\dot { \theta }$ is zero for $\theta = 0$ ,tumbling cannot be initiated unless the initial value of $\theta$ is finite. However $\theta = 0$ is never attainable in practice for many reasons, and $\dot { \theta }$ will build up when $C / A$ is less than unity. By differentiating Eq. $f ,$ $\dot { \theta }$ can be shown to have a maximum at $\theta = \tan ^ { - 1 } 1 / { \sqrt { 2 } } =$ $3 5 ^ { \circ } 2 0 ^ { \prime }$ Due to $\cos ^ { 2 } \theta$ ， $\dot { \theta }$ will diminish to a small value near $\theta = 9 0 ^ { \circ }$ ,and an infinite time will be required to reach this angle.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/2f56737a21e8216e1d250907664fb90e3ad0e7cf55176bdc11f220df7fd40965.jpg)  
Fig.7.6-4. Variation in the rate of tumbling.

For small values of 0, Eq $f$ is approximately equal to

$$
\dot { \theta } = \pmb { K } \theta
$$

and the time required for the attitude angle to change from $\theta _ { 0 }$ to $\theta _ { 1 }$ is

$$
t = \frac { 1 } { K } \ln \frac { \theta _ { 1 } } { \theta _ { 0 } }
$$

# Numerical example

Let the two solid disks be aluminum, $\%$ in. thick and 24 in. diameter, and the flexible tube be0.032 in.stainlessteel,6in.indiameterand $2 4 \mathrm { i n }$ long. The quantities required for the computation of $K$ are:

Assuming $\gamma = 0 . 0 5$ and $\omega _ { 0 } = 5 0 \pi / \mathrm { s e c }$ , the value of $K$ is $6 6 2 \times 1 0 ^ { 6 }$ Thus for the body to undergo an attitude change from $1 ^ { \circ }$ to $1 0 ^ { \circ }$ ,the time required, as calculated from Eq. $h ,$ is

$$
\begin{array} { c l c r } { { t = { \frac { 2 . 3 0 3 } { 6 6 2 } } \times 1 0 ^ { 6 } = 3 4 8 0 \ \mathrm { s e c } } } \\ { { = 5 8 . 0 \ \mathrm { m i n } } } \end{array}
$$

# PROBLEMS

1. A satellite has a moment of inertia of $I = 1 . 2 0$ lb-in.-sec² about its spin axis. It is desired to reduce the initial spin of $2 0 0 ~ \mathrm { r p m }$ to zero by two weights of $\mathcal { Y } _ { 2 0 }$ lb each wrapped around a section having a radius of $1 0 \mathrm { i } \bar { \mathrm n }$ Determine the proper length of cord.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/c12fc6f62fd5ac909f9d31b86501096e3d98f94b28177020dc37fdaab36a5e25.jpg)  
Prob. 2

2. In Prob. 1, determine the speed of the $\scriptstyle { \frac { 1 } { 2 0 } }$ Ib weights as they fly off. As shown in the sketch, the pin holding the string wil slide out when the string goes beyond the tangent to the circle.

3. It is proposed to despin a satellite by four weights of mass m each, hinged by stiff arms as shown in the sketch. Show that the spin is given by

$$
\omega = \frac { \omega _ { 0 } ( C _ { 0 } + 4 m { r _ { 0 } } ^ { 2 } ) } { C _ { 0 } + 4 m ( r _ { 0 } + l \sin \theta ) ^ { 2 } }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/724403e00904803f050be057c2ef8b91613379997a71bb47fd6cb4acb9408e09.jpg)  
Prob.3

4. Determine the i, j, k components of the acceleration of m in Prob. 3.   
5. Verify the relations given by Eq. 7.6-8.   
6. Verify Eq. 7.6-14.

7. Equation 7.6-5 can be written as

$$
T = { \frac { h ^ { 2 } } { 2 C } } { \left[ 1 + { \left( { \frac { C } { A } } - 1 \right) } \sin ^ { 2 } \theta \right] }
$$

Plot $T$ versus $\theta$ for $- \frac { \pi } { 2 } \leq { \theta } < \frac { \pi } { 2 } \mathrm { w h e n } \left( { a } \right) C / { A } > 1 ; \mathrm { \ } ( { b } ) C / { A } < 1 ,$ and discuss its stability.

8. For a symmetric body $A$ ， $A$ ， $C$ acted upon by moments $M _ { 1 }$ ， $M _ { 2 }$ ， $M _ { 3 }$ about body axes 1,2,3, show that the dissipation rate of energy is equal to

$$
\omega _ { 1 } M _ { 1 } + \omega _ { 2 } M _ { 2 } + \omega _ { 3 } M _ { 3 } = \frac { 1 } { 2 } A \frac { d } { d t } ( \omega _ { 1 } ^ { \ : 2 } + \omega _ { 2 } ^ { \ : 2 } ) + \frac { 1 } { 2 } C \frac { d } { d t } { \omega _ { 3 } } ^ { 2 }
$$

9. Show that the hysteretic damping factor $\gamma$ of Eq. 7.6-7 is related to the structural damping factor $\propto$ by the relationship $\alpha = \gamma / 2 \pi$

Hint: The work done per cycle by a damping force $F _ { d }$ for harmonic oscillations is $W = \pi F _ { d } X _ { \mathrm { { i } } }$ where $\chi$ is the amplitude leading the damping force by $9 0 ^ { \circ }$ The structural damping force can be taken as ixkx, where $k$ is the stiffness.

# 7.7 Variable Mass

In the previous sections we have limited our discussion to a constantmass system. In many cases the mass variation rate is large, which requires us to consider the problem of variable mass.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/6205a0d32b891330f4c59808cf6d127dbd93a3853fa9b2f5fee1e634c3e0ff2e.jpg)  
Fig. 7.7-l. Momentum of the system at times t and $t + \Delta t .$

Newton's second law, $\mathbf { F } = { \dot { \mathbf { p } } }$ , which states that force is equal to the time rate of change of momentum, is intended to apply only to a system of definite mass. However, the equation can be applied to a system of varying mass provided the same mass is examined for the change in momentum at two instances of time.

We will consider a mass m moving with velocity v at time t,and assume that our system is accumulating mass continually at a rate m (if the system is Iosing mass as in a rocket, $\dot { m }$ is negative). We willdefine our system to be the mass m + △m at time t as shown in Fig.7.7-1. Its initial momentum at time $t$ is

$$
\mathbf { p } = m \mathbf { v } + \mathbf { v } _ { 0 } \Delta m
$$

where Vo is the initial velocity of △m before it is acquired by m. The momentum at time $t + \Delta t$ is

$$
\begin{array} { c } { \mathbf { p } + \Delta \mathbf { p } = ( m + \Delta m ) ( \mathbf { v } + \Delta v ) } \\ { = m \mathbf { v } + m \Delta \mathbf { v } + \mathbf { v } \Delta m } \end{array}
$$

where the negligible second-order term (△m)(△v) has been omited. Subtracting to determine the change in momentum and dividing by △t, the equation for the variable masssystem becomes,

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/461716170543650747c71195e84a88cdf0bc1d3da9fbe550bf54b2805919204c.jpg)  
Fig. 7.7-2. Forces on a rocket.

Equation 7.7-3 indicates that the force F is expended in accelerating the mass $m$ and changing the momentum of the acquired mas from $\mathbf { v } _ { 0 } \ d m$ to v dm.

For rockets u ${ \frac { d m } { d t } } = \mathbf { T }$ is the thrust exerted by the jet, where ${ \mathfrak { u } } =$ $- ( \mathbf { v } - \mathbf { v } _ { 0 } )$ is the velocity of the gas jet relative to the engine.\* Thus the equation for the rocket in rectilinear motion, Fig. 7.7-2,can be writen as

$$
\mathbf { F } + \mathbf { T } = m { \frac { d \mathbf { v } } { d t } }
$$

where the external forces of gravity and aerodynamic drag can be included in F. If the rocket is not spinning or turning and T acts through the center of mass, the moment on the rocket is zero,and we are concerned only with its translational motion.

# 7.8 Jet Damping (Nonspinning Variable Mass Rocket)

When a nonspinning rocket rotates about a transverse axis, as shown in Fig. 7.8-1, the ejected gas acquires a momentum component $- \dot { m } l \omega$

\* u is the velocity of the jet relative to the nozzle. When it is positive we have a retro-rocket. m is negative for any rocket.

perpendicular to the longitudinal axis, where m is the mass of the rocket at any time,m = dm/dt is its rate of change (m is negative),and lω is the transverse velocity of the nozzle exit due to rotational velocity $\omega$ . Letting the transverse rotational axis coincide at all times with the center of mass and letting the moment of inertia of the rocket about this axis be $I = m k ^ { 2 }$ ， where $k$ is the radius of gyration about the transverse axis, the moment $M$ about this axis must supply the change in angular momentum of the rocket and the ejected mass as follows;

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/1cb0b13f7953d5698b1b9184f2453a91ee4ea83480679656005779977fa5fe12.jpg)  
Fig.7.8-l. Jet damping of nonspinning rocket.

$$
M = { \frac { d } { d t } } I \omega - { \dot { m } } l ^ { 2 } \omega
$$

Substituting for $I$ and carrying out the differentiation,

$$
\begin{array} { c } { { M = I \displaystyle \frac { d \omega } { d t } + \omega \left( m \displaystyle \frac { d } { d t } k ^ { 2 } + k ^ { 2 } \dot { m } \right) - \dot { m } l ^ { 2 } \omega } } \\ { { { } } } \\ { { { } = I \dot { \omega } - \omega \Bigl [ \dot { m } ( l ^ { 2 } - k ^ { 2 } ) - m \displaystyle \frac { d } { d t } k ^ { 2 } \Bigr ] } } \end{array}
$$

Assuming the applied moment $M$ to be zero and ${ \frac { d } { d t } } k ^ { 2 }$ to be negligible (i.e.,burning proceeds radially), this equation can be solved in the following manner :

$$
\begin{array} { c } { { \frac { d \omega } { \omega } = \frac { ( l ^ { 2 } - k ^ { 2 } ) } { I } d m = \left( \frac { l ^ { 2 } } { k ^ { 2 } } - 1 \right) \frac { d m } { m } } } \\ { { \mathrm { l n } \left( \frac { \omega } { \omega _ { 0 } } \right) = \left( \frac { l ^ { 2 } } { k ^ { 2 } } - 1 \right) \mathrm { l n } \frac { m } { m _ { 0 } } } } \\ { { \frac { \omega } { \omega _ { 0 } } = \left( \frac { m } { m _ { 0 } } \right) ^ { \frac { l ^ { 2 } } { k ^ { 2 } } - 1 } } } \end{array}
$$

Thus with an initial angular rate of ωo, the angular speed ω decreases if I/k is greater than unity and increases if l/k is less than unity.Since in

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/dda3636808d8e045f50e712e8a70acb293f40180faf74701ee741095e8aa23f8.jpg)  
Fig. 7.8-2. Change in pitch angular rate of nonspinning rocket due to jet damping.

most configurations $l / k > 1$ , the angular speed decreases and the action of the jet is that of a damper. Figure 7.8-2 shows how the angular speed changes with mass ratio for various values of $l / k$

# 7.9 Euler's Dynamical Equations for Spinning Rockets²

The statement that the force is equal to the time rate of change of momentum can be applied to problems of varying mass provided the momentum of a definite mass is examined for its rate of change. The result is the rate of change of the momentum of the varying mass plus the rate of momentum transfer from the varying mass. The moment of the force about its center of mass is then the time rate of change of the moment of momentum which, can be written as

Consider a general motion of a symmetric rocket with body axes x, y, z fixed in the rocket with the origin at the center of mass. The jet is considered to be ejected through a cluster of nozzles, the center of each being defined by the vector r; = xi + yij - lk,as shown in Fig. 7.9-2.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/a641b4ef2aaedaf398e8f83fff2d374c385680061b9dc26fe83cfe0629ed4257.jpg)  
Fig. 7.9-l. Jet damping of spinning rocket.

With the x, y, $z$ axes coinciding with the principal axes of the rocket, the angular momentum components are

$$
\begin{array} { r } { h _ { x } = I _ { x } \omega _ { x } } \\ { h _ { y } = I _ { y } \omega _ { y } } \\ { h _ { z } = I _ { z } \omega _ { z } } \end{array}
$$

where $I _ { x } , I _ { y } ,$ and $I _ { z }$ are instantaneous values of the principal moments of inertia. The rate of change of the angular momentum of the rocket is

$$
[ \dot { \bf h } ] + \boldsymbol { \omega } \times { \bf h }
$$

which results in the components

$$
\begin{array} { r l } & { { \dot { I } _ { x } } \omega _ { x } + { I _ { x } } { \dot { \omega } _ { x } } + ( { I _ { z } } - { I _ { y } } ) \omega _ { y } \omega _ { z } } \\ & { { \dot { I } _ { y } } \omega _ { y } + { I _ { y } } { \dot { \omega } _ { y } } + ( { I _ { x } } - { I _ { z } } ) \omega _ { x } \omega _ { z } } \\ & { { \dot { I } _ { z } } \omega _ { z } + { I _ { z } } { \dot { \omega } _ { z } } + ( { I _ { y } } - { I _ { x } } ) \omega _ { x } \omega _ { y } } \end{array}
$$

In considering the angular momentum imparted to the jet, the cluster of nozzles is assumed to be symmetrically located relative to the $z$ axis. If all the angular velocities of the missile are zero,the angular momentum imparted to the jet is zero.The velocity of the nozze exit due to ω, @y and $\omega _ { z }$ is shown in Fig. 7.9-2. Multiplying these velocities by their mass rate of flow $\dot { m }$ ,we obtain the linear momentum rates in the direction of the velocities,from which the angular momentum rates can be determined by multiplying with proper distances from the coordinate axes.

For the ith nozzle, the linear momentum rate due to ω, is -m,rω, and its angular momentum rate about the z axis is -mir²ω, where m = dmi/dt (a negative quantity). Summing over all nozzles, the total rate of angular momentum transfer tothe jet,about the $_ z$ axis is

$$
- \omega _ { z } \sum _ { i } \dot { m _ { i } } \boldsymbol { r _ { i } } ^ { 2 } = - \dot { m } \rho ^ { 2 } \omega _ { z }
$$

where

$$
\rho ^ { 2 } = \frac { \displaystyle \sum _ { i } { \dot { m _ { i } } r _ { i } } ^ { 2 } } { \dot { m } }
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/5b21d3c7b4ecbe9cc1d7639a0e0a74b63cacbec605e9caae30289bef0e830295.jpg)  
Fig. 7.9-2. Velocity of nozzle due to pitch and spin.

Due to $\omega _ { x }$ the rate of change of the momentum of the ith jet is

$$
- { \dot { m _ { i } } } \sqrt { l ^ { 2 } + { y _ { i } } ^ { 2 } } \omega _ { x } ,
$$

and its moment is $- \dot { m } _ { i } ( l ^ { 2 } + { y _ { i } } ^ { 2 } ) \omega _ { x }$ Summing over all nozzles, the total rate of change of the angular momentum of the jet about the $_ { x }$ axis is

$$
- \sum _ { i } \dot { m _ { i } } ( l ^ { 2 } + y _ { i } { ^ { 2 } } ) \omega _ { x } = - \dot { m } ( l ^ { 2 } + { \frac { 1 } { 2 } } \rho ^ { 2 } ) \omega _ { x }
$$

In a similar manner, the rate of change of the angular momentum of the jet about the $y$ axis is

$$
- \sum _ { i } \dot { m _ { i } } ( l ^ { 2 } + x _ { i } { ^ { 2 } } ) \omega _ { y } = - \dot { m } ( l ^ { 2 } + { \frac { 1 } { 2 } } \rho ^ { 2 } ) \omega _ { y }
$$

Putting together all these terms, the moment equations become

$$
\begin{array} { r l } & { M _ { x } = I _ { x } \dot { \omega } _ { x } + ( I _ { z } - I _ { y } ) \omega _ { y } \omega _ { z } - \dot { m } ( l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } ) \omega _ { x } + \dot { I } _ { x } \omega _ { x } } \\ & { M _ { y } = I _ { y } \dot { \omega } _ { y } + ( I _ { x } - I _ { z } ) \omega _ { x } \omega _ { z } - \dot { m } ( l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } ) \omega _ { y } + \dot { I } _ { y } \omega _ { y } } \\ & { M _ { z } = I _ { z } \dot { \omega } _ { z } + ( I _ { y } - I _ { x } ) \omega _ { x } \omega _ { y } - \dot { m } \rho ^ { 2 } \omega _ { z } + \dot { I } _ { z } \omega _ { z } } \end{array}
$$

Substituting $I _ { x } = m k _ { x } ^ { \mathrm { ~ 2 ~ } }$ we have ${ \dot { I } } _ { x } = + { \dot { m } } { k _ { x } } ^ { 2 } + m \frac { d } { d t } { k _ { x } } ^ { 2 }$ , and the above equations can be rewritten as

$$
\begin{array} { l c r } { { M _ { x } = I _ { x } \dot { \omega } _ { x } + ( I _ { z } - I _ { y } ) \omega _ { y } \omega _ { z } - \bigg [ \dot { m } \Big ( l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } - k _ { z } ^ { 2 } \Big ) - m \frac { d } { d t } k _ { z } ^ { 2 } \bigg ] \omega _ { x } } } \\ { { M _ { y } = I _ { y } \dot { \omega } _ { y } + ( I _ { x } - I _ { z } ) \omega _ { x } \omega _ { z } - \bigg [ \dot { m } \Big ( l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } - k _ { y } ^ { 2 } \Big ) - m \frac { d } { d t } k _ { y } ^ { 2 } \bigg ] \omega _ { y } } } \\ { { M _ { z } = I _ { z } \dot { \omega } _ { z } + ( I _ { y } - I _ { x } ) \omega _ { x } \omega _ { y } - \bigg [ \dot { m } ( \rho ^ { 2 } - k _ { z } ^ { 2 } ) - m \frac { d } { d t } k _ { z } ^ { 2 } \bigg ] \omega _ { z } ( 7 . 9 } } \end{array}
$$

We find, therefore, that the usual Euler's equations are supplemented by additional terms related to jet damping and the variable moment of inertia.

# Example 7.9-l

Consider the moment-free motion of a symmetrical missile, $I _ { x } = I _ { y } = I$ with initial spin velocity $\omega _ { z } ( 0 ) = n$ . We will assume that the fuel burns in such a manner that the variations in $k _ { x }$ ， $k _ { y }$ ,and $k _ { z }$ are negligible.

From the third of Eq. 7.9-8, we obtain

$$
\int { \frac { d \omega _ { z } } { \omega _ { z } } } = \left( { \frac { \rho ^ { 2 } } { { k _ { z } } ^ { 2 } } } - 1 \right) \int { \frac { d m } { m } }
$$

which leads to the solution,

$$
{ \frac { \omega _ { z } } { n } } = \left( { \frac { m } { m _ { 0 } } } \right) { \frac { \rho ^ { 2 } } { k _ { z } ^ { ~ 2 } } } - 1
$$

We now multiply the second of Eq. 7.9-8 by $i = \nu ^ { \top } \overline { { - 1 } }$ and add it to the first equation letting

$$
\omega _ { x } + i \omega _ { y } = \omega _ { x y }
$$

The first two equations of Eq.7.9-8 then reduce to the following, where $\omega _ { z }$ from above has been substituted.

$$
\int \frac { d \omega _ { x y } } { \omega _ { x y } } = \bigg ( \frac { l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } - k ^ { 2 } } { k ^ { 2 } } \bigg ) \int \frac { d m } { m } - i \bigg ( 1 - \frac { k _ { z } { } ^ { 2 } } { k ^ { 2 } } \bigg ) n \int \bigg ( \frac { m } { m _ { 0 } } \bigg ) ^ { \frac { \rho ^ { 2 } } { k _ { z } } - 1 } d t
$$

If we essume $m$ to varylinerlywithtimesohat $m = m _ { 0 } - m ^ { \prime } t$ this quation

$$
\ln \frac { \omega _ { x y } } { \omega _ { x y } ( 0 ) } = \frac { l ^ { 2 } + \frac { 1 } { 2 } \rho ^ { 2 } - k ^ { 2 } } { k ^ { 2 } } \ln \frac { m } { m _ { 0 } } - i \bigg ( 1 - \frac { k _ { z } { } ^ { 2 } } { k ^ { 2 } } \bigg ) n \int _ { 0 } ^ { t } \bigg ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \bigg ) ^ { \frac { \rho ^ { 2 } } { k _ { z } { } ^ { 2 } } - 1 } \ d t
$$

By letting $1 - ( m ^ { \prime } / m _ { 0 } ) t = \xi$ and $[ ( \rho ^ { 2 } / k _ { z } ^ { 2 } ) - 1 ] = K$ ,the last integral is

$$
\begin{array} { c } { { \displaystyle - \frac { m _ { 0 } } { m ^ { \prime } } \int _ { 1 } ^ { 1 - \frac { m ^ { \prime } } { m _ { 0 } } t } \xi ^ { K } d \xi = - \frac { m _ { 0 } } { m ^ { \prime } } \frac { \xi ^ { K + 1 } } { K + 1 } \Biggl | _ { 1 } ^ { 1 - \frac { m ^ { \prime } } { m _ { 0 } } t } } } \\ { { = - \frac { m _ { 0 } } { m ^ { \prime } } \frac { k _ { z } ^ { 2 } } { \rho ^ { 2 } } \biggl [ \biggl ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \biggr ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { 2 } } } - 1 \biggr ] } } \end{array}
$$

and the solution becomes

$$
{ \frac { \omega _ { \alpha y } } { \omega _ { x y } ( 0 ) } } \bigg ( { \frac { m _ { 0 } } { m _ { 0 } - m ^ { \prime } t } } \bigg ) ^ { \frac { l ^ { 2 } + \frac { 1 } { \gamma _ { \Omega } } p ^ { 2 } - k ^ { 2 } } { k ^ { 2 } } } = i n \bigg ( { \frac { m _ { 0 } } { m ^ { \prime } } } \bigg ) \bigg ( \frac { k _ { z } ^ { 2 } } { \rho ^ { 2 } } \bigg ) \bigg ( 1 - \frac { k _ { z } ^ { 2 } } { k ^ { 2 } } \bigg ) \bigg [ \bigg ( 1 - { \frac { m ^ { \prime } } { m _ { 0 } } } t \bigg ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { 2 } } } - 1 \bigg ] ^ { \frac { 1 } { \gamma _ { \Omega } } } ,
$$

or

$$
\begin{array} { r l } { \frac { \omega _ { \alpha y } } { \omega _ { x y } ( 0 ) } = \bigg ( \frac { m _ { 0 } - m ^ { \prime } t } { m _ { 0 } } \bigg ) ^ { \frac { l ^ { 2 } + 1 / 2 \rho ^ { 2 } - k ^ { 2 } } { k ^ { 2 } } } } & { } \\ { \times ~ \exp \bigg \{ - i n \frac { m _ { 0 } } { m ^ { \prime } } \frac { k _ { z } ^ { 2 } } { \rho ^ { 2 } } \bigg ( 1 - \frac { k _ { z } ^ { 2 } } { k ^ { 2 } } \bigg ) \bigg [ 1 - \bigg ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \bigg ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { 2 } } } \bigg ] \bigg \} } & { ( f ) } \end{array}
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/de95b3dcfdfe3527f4a01a73d63348e4478573a224a38c424e336433dd9d329c.jpg)  
Figure 7.9-3 shows how the various terms of Eq.fvary with time. The oscillatory amplitude of @xy diminishes with time due to jet damping,and the frequency of oscillation increases.1.3   
Fig. 7.9-3. Terms of Eq.f.

# 7.10 Angle of Attack of the Missile

The angular velocity $\omega _ { x y }$ is referred to coordinates $x , \ y ,$ which are rotating with the missile. To establish the angle of attack of the missile, it is necessary to determine the Euler angle $\theta$ measured from a fixed inertial axis. For this determination we start with the angular velocities $\omega _ { x } , \omega _ { y } , \omega _ { z }$ expressed in terms of Euler's angles

$$
\begin{array} { l } { \omega _ { x } = \dot { \psi } \sin \theta \sin \varphi + \dot { \theta } \cos \varphi } \\ { \omega _ { y } = \dot { \psi } \sin \theta \cos \varphi - \dot { \theta } \sin \varphi } \\ { \omega _ { z } = \dot { \psi } \cos \theta + \dot { \varphi } } \end{array}
$$

Adding the first two in quadrature, we have

$$
\omega _ { x y } = \omega _ { x } + i \omega _ { y } = ( \dot { \theta } + i \dot { \psi } \sin \theta ) e ^ { - i \varphi }
$$

From Eq. 7.9-b and the third of the above equations, we obtain

$$
n \bigg ( \frac { m } { m _ { 0 } } \bigg ) ^ { ( \rho ^ { 2 } / k _ { z } ^ { ~ 2 } ) - 1 } = \dot { \psi } \cos \theta + \dot { \varphi }
$$

or

$$
\dot { \psi } = \frac { 1 } { \cos \theta } \bigg [ n \bigg ( \frac { m } { m _ { 0 } } \bigg ) ^ { ( \rho ^ { 2 } / k _ { z } ^ { ~ 2 } ) - 1 } - \dot { \varphi } \bigg ]
$$

By substituting into the equation for $\omega _ { x y }$ ,Eq. 7.10-2,

$$
\begin{array} { r } { \omega _ { \alpha y } = \Big \{ \dot { \theta } + i \Big [ n \Big ( \displaystyle \frac { m } { m _ { 0 } } \Big ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { ~ 2 } } - 1 } - \dot { \varphi } \Big ] \tan \theta \Big \} e ^ { - i \varphi } } \\ { \simeq \Big \{ \dot { \theta } + i \Big [ n \Big ( 1 - \displaystyle \frac { m ^ { \prime } } { m _ { 0 } } t \Big ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { ~ 2 } } - 1 } - \dot { \varphi } \Big ] \theta \Big \} e ^ { - i \varphi } } \end{array}
$$

We now introduce the transformation

$$
\theta _ { x y } = \theta e ^ { - i \varphi }
$$

proposed by H. Leon,4 which differentiates into

$$
\dot { \theta } _ { x y } = ( \dot { \theta } - i \dot { \varphi } \theta ) e ^ { - i \varphi }
$$

Thus this equation becomes

$$
\begin{array} { c } { { \displaystyle { \dot { \theta } } _ { x y } + i n \Big ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \Big ) ^ { \frac { \rho ^ { 3 } } { k _ { z } ^ { 2 } } - 1 } \theta _ { x y } = \omega _ { x y } } } \\ { { = \omega _ { x y } ( 0 ) \Big ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \Big ) ^ { \frac { \eta ^ { 3 } + \gamma _ { 2 } \rho ^ { 2 } - k ^ { 2 } } { k ^ { 2 } } } } } \\ { { \times \exp \Big \{ { - i n \frac { m _ { 0 } } { m ^ { \prime } } \frac { k _ { z } ^ { 2 } } { \rho ^ { 2 } } \Big ( 1 - \frac { k _ { z } ^ { 2 } } { k ^ { 2 } } \Big ) \Big [ 1 - \Big ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \Big ) \frac { \rho ^ { 3 } } { k _ { z } ^ { 2 } } \Big ] } \Big \} } } \end{array}
$$

where the previous solution for $\wp _ { x y }$ Eq. $f$ has been substituted.

This equation differs from that of the constant mass missile, first, by the fact that the coefficient of $\theta _ { x y }$ which is $i n$ for the constant mass missile, is now a time function,

$$
i n \bigg ( 1 - \frac { m ^ { \prime } } { m _ { 0 } } t \bigg ) ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { ~ 2 } } - 1 }
$$

and, secondly, by the right-hand forcing term which is also different due to $\omega _ { z }$ slowing down by jet damping and variable mass. The equation is a time-varablelneardretialeuanchanbedfor $\theta _ { x y }$ \*

\* The equation is in the form

with solution

$$
\dot { \theta } _ { x y } + P ( t ) \theta _ { x y } = Q ( t )
$$

$$
\theta _ { x y } = e ^ { - \int P d t } \int Q e ^ { \int P d t } d t + C e ^ { - \int P d t }
$$

The angle $\theta _ { x y }$ is referenced to the rotating body axes $_ x$ $y$ and must be multiplied by $e ^ { i \omega _ { z } t } = \exp \Big \{ i n [ 1 - ( m ^ { \prime } / m _ { 0 } ) t ] ^ { \frac { \rho ^ { 2 } } { k _ { z } ^ { 2 } } - 1 } \Big \} t$ in order to reference with respect to the inertial axes. Thus the complete solution for the angle of attack as a function of time and the variation of mass is possible by the foregoing procedure.

# PROBLEMS

1. Water is flowing out relative to the nozzle shown in the sketch at a speed of 30 ft/sec,and at a rate of 0.10ft/sec for each nozzle. If $R = 1 . 5$ ft and t nozzles are rotated at $6 0 ~ \mathrm { r p m }$ determine the torque necessary.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/8e508e2370dd885207c5df290cdffb369cce9c1b4f2a298d09ffe2c5cc5515b7.jpg)  
Prob. 1

2. The ends of the nozzle of Prob. 1 are bent back $3 0 ^ { \circ }$ so that the sprinkler will rotate by itself. If the resisting torque due to friction is 1.72ft.ib,determine the speed in rpm with which the sprinkler will rotate.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/d0542ba687fa4c54175849cb370e9b8e57b4a205f80b0547713bd1d712321387.jpg)  
Prob. 2

3. A jet engine takes in air at a rate $\dot { m } _ { a }$ ,compresses it,mixes it with kerosene ata rate $\dot { m } _ { \boldsymbol { k } }$ ,and ejects the ignited mixture at a speed $u$ relative to the nozzle. If the jet plane is traveling at a speed of $v$ ,show that the thrust of the engine is

$$
T = \dot { m } _ { k } u + \dot { m } _ { a } ( u - v )
$$

4. A nonspinning rocket of total mass mo, half of which is fuel,is rotating about the pitch axis with an initial angular velocity of O.5 rad/sec. If $l / k$ for the rocket remains constant at 2, determine the pitch rate at burnout.

5. If in Prob. 4 the radius of gyration about the pitch axis decreased with time, would the pitch rate at burnout be larger or smaller ?

6. The ratio of the fuel to the total mass for a particular missile is O.70,and burning takes place with negligible change in the value of l/k = √3. If the rate of fuel consumption is m/mo =1ioo sec-1,and the missile is rotating about a transverse axis without spin, plot the variation in its rotation speed against time.

7.If for the spinning rocket with variable mass, the ratio ${ \rho } / { k _ { z } } = 1$ and the quantity $\rho / k$ is negligible compared to $l / k$ , show that the equation for the complex angular velocity is

$$
\frac { \omega _ { x y } } { \omega _ { x y } ( 0 ) } = \bigg ( \frac { m } { m _ { 0 } } \bigg ) ^ { \frac { l ^ { 3 } } { k ^ { 2 } } - 1 } e ^ { - i \big ( 1 - \frac { k _ { z } ^ { 2 } } { k ^ { 2 } } \big ) n t }
$$

How does this equation differ from that of the nonrotating rocket ?

8. For the case $\rho ^ { 2 } / k _ { z } ^ { \mathrm { ~ 2 ~ } } = 1$ and $k _ { z } ^ { ~ 2 } / k ^ { 2 }$ is negligible compared to unity, the differ-ential equation for the complex angle of attack, (Eq. 7.10-6) reduces to (see also Prob. 7),

$$
\dot { \theta } _ { x y } + i n \theta _ { x y } = \omega _ { x y } = \left( \frac { m } { m _ { 0 } } \right) ^ { \frac { l ^ { 2 } } { k ^ { 3 } } - 1 } \omega _ { x y } ( 0 ) e ^ { - i n t }
$$

Leting $m / m _ { 0 } = 1 - [ ( m ^ { \prime } / m _ { 0 } ) t ] ,$ a closed form solution is possible when $l ^ { 2 } / k ^ { 2 }$ is an integer. Leting $l ^ { 2 } / k ^ { 2 } = 4$ , carry out this solution and show that the motion of the missle longitudinal axis is a converging spiral.

9. Assuming the angle of attack $\theta$ of a spinning missile to be small (angle of attack is measured from the velocity vector $\mathbf { V }$ which can be considered fixed in space) draw the inertial coordinates $X , Y , Z$ ,the node axis $\xi$ ,and the rotat-ing body axes $x , y , z$ ,where ${ \cal Z }$ is the longitudinal axis of the missile at an angle $\theta$ from the vector $\mathbf { V }$ placed along the $Z$ axis. On this diagram show the complex angular velocity $\omega _ { x y } , \omega _ { z }$ , and the resultant angular velocity w.

10. Assuming small angle of attack, determine the inertial components of the angular velocity $\boldsymbol { \omega }$ of Prob. 9, by resolving it along the $Z$ axis and in the $X Y$ plane.

11. If the moment of inertia of the missile about the transverse and longitudinal axes are $A$ and $C$ ,determine thepositionof the angular momentum vector forProb.9,andfind theanglebetween itand thevelocity vector.Howdoes the angular momentum vector vary in the inertial space?

12. Compare the solution for the complex angle of atack $\theta _ { X Y }$ of a missile with constant thrust misalignment $M _ { 1 }$ (Prob.10,Sec.7.4) with that of the near symmetrical missile with principal axis misalignment of $\beta$ .Determine the product of inertia $F$ in termsof themisalignmentmoment $M _ { 1 }$ which will give the same motion.

# 7.ll General Motion of Spinning Bodies with Varying Configuration and Mass

In the previous sections the origin of the body axes always coincided with the mass center. In the most general case,a body under translation and rotation may have relative motion between particles leading to a varying configuration, and may be undergoing a change in mass with time. The origin of the body coordinates attached to the system will then not coincide with the center of mass at all times. Relative motion between particles could take place when motors and other moving parts are present or when the body contains liquids such as fuel. Vibration due to fexibility is another contributing factor. Mass variation would take place owing to jets ejected from the body.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/73c4d03f42d38b0e38a97736697ad72a29eb3c0f64e38d002a9abf1254faf3ee.jpg)  
Fig. 7.Il-l. Body of varying mass and configuration.

To examine the motion of such a general system,it is advisable to view the problem as a system of particles with the origin of the body axes not coinciding with the center of mass.9\* Such a procedure will account for every conceivable configuration of the system and eliminate the possibility of omitting terms. In spite of this generality, the terms of the equation can be regrouped to more familiar forms of rigid body, jet ejection, center of mass shift, and relative motion.

We define the system by a group of particles within a specified boundary with body coordinates x, y, z moving with the system as shown in Fig. 7.11-1. Variation in mass is ailowed by particles leaving the system through the boundary. The angular momentum of the system about the moving origin O at time $t$ is

$$
\begin{array} { r } { \mathbf { h } _ { 0 } = \sum \mathbf { r } _ { i } \times m _ { i } \dot { \mathbf { R } } _ { i } } \end{array}
$$

where $\mathbf { r } _ { i }$ is drawn from the moving origin 0, and $\dot { \mathbb { R } } _ { i }$ is the absolute velocity

of $m _ { i }$ referenced to the inertial axes $X$ ，Y, $\boldsymbol { \mathscr { L } }$ . If we differentiate this equation, we obtain,

$$
\begin{array} { r } { \dot { \mathbf { h } } _ { 0 } = \sum \mathbf { r } _ { i } \times \displaystyle \frac { d } { d t } \left( m _ { i } \dot { \mathbf { R } } _ { i } \right) + \sum \dot { \mathbf { r } } _ { i } \times m _ { i } \dot { \mathbf { R } } _ { i } } \end{array}
$$

From Fig. 7.11-1, $\mathbf { R } _ { i } = \mathbf { R } _ { 0 } + \mathbf { r } _ { i } ,$ and the last term of Eq. 7.11-2 can be reduced by the following steps,

$$
\begin{array} { r l } & { \sum \dot { \mathbf { r } } _ { i } \times m _ { i } \dot { \mathbf { R } } _ { i } = \sum \dot { \mathbf { r } } _ { i } \times m _ { i } ( \dot { \mathbf { R } } _ { 0 } + \dot { \mathbf { r } } _ { i } ) } \\ & { \qquad = - \dot { \mathbf { R } } _ { 0 } \times \sum m _ { i } \dot { \mathbf { r } } _ { i } = - \dot { \mathbf { R } } _ { 0 } \times m \dot { \bar { \mathbf { r } } } } \end{array}
$$

where $m$ is the total mass at time $t$ ,and r its center of mass relative to the body axes.

Referring to the first term of Eq. 7.11-2, $( d / d t ) ( m _ { i } { \dot { \bf R } } _ { i } )$ is equal to the force applied to the mass $m _ { i }$ , and its cross product with $\mathbf { r } _ { i }$ is the moment about 0. Equation 7.11-2 can then be rewritten as

$$
{ \bf M } _ { 0 } = { \dot { \bf h } } _ { 0 } + { \dot { \bf R } } _ { 0 } \times m { \dot { \bar { \bf r } } }
$$

which states that the moment about an arbitrary point O is equal to the rate of change of the angular momentum ${ \bf h } _ { 0 }$ plus a term depending on the velocity of the origin and the velocity of the center of mass with respect to the origin. It is evident, then, that the moment is equal to the rate of change of the angular momentum only under the following conditions: (1) When O is stationary; (2) when the velocity of the center of mass relative to the origin is zero； or (3) when the two velocities $\dot { \bf R } _ { 0 }$ and $\dot { \overline { { \mathbf { r } } } }$ are parallel.

The moment equation forthe generalsystem can befound directlyfron the equation

$$
\begin{array} { r } { \mathbf { M } _ { 0 } = \sum \boldsymbol { \tau } _ { i } \times \frac { d } { d t } \left( m _ { i } \dot { \mathbf { R } } _ { i } \right) } \end{array}
$$

However, to clarify certain concepts， we will examine the angular momentum at two instances of time and determine $\dot { \mathbf { h } } _ { 0 }$ to be substituted into Eq. 7.11-3.

Figure 7.11-2 shows a mass $m _ { i }$ at time $t$ , which at a later time $t = \Delta t$ occupies a different position (r: + △r) and has separated into two parts, $m _ { i } + \dot { m } _ { i } \Delta t$ and $( - \dot { m } _ { i } \Delta t )$ ， with relative velocity $\mathbf { u } _ { i }$ between them. In separating into two parts, $m$ is decreasing and $\dot { m } = d m / d t$ is a negative quantity. The angular momentum at $t + \Delta t$ is

$$
\begin{array} { c } { { \bf { h } } _ { 0 } + \Delta { \bf { h } } _ { 0 } = \sum { ( { \bf { r } } _ { i } + \Delta { \bf { r } } _ { i } ) } \times ( m _ { i } + \dot { m _ { i } } \Delta t ) ( \dot { \bf { R } } _ { i } + \Delta \dot { \bf { R } } _ { i } ) } \\ { + \sum { ( { \bf { r } } _ { i } + \Delta { \bf { r } } _ { i } ) } \times ( - \dot { m _ { i } } \Delta t ) ( \dot { \bf { R } } _ { i } + { \bf { u } } _ { i } ) } \end{array}
$$

\* $\mathbf { u } _ { i }$ is negative when mass is ejected in the opposite sense to $\dot { \bf R }$ (see p. 221).

and, by neglecting higher order infinitesimals and approaching the limit △h/△t,as (△t → O) the rate of change of the angular momentum becomes

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/5a05f45ea59a8674ac9864f9398c77d0f8b3553efc6b069956b2ae11b4d80d00.jpg)  
Fig. 7.Il-2. Angular momentum of element $m$ at times $t$ and $t + \Delta t$

Substituting Eq. 7.11-6 into 7.11-3, the moment equation becomes

$$
\begin{array} { r } { \mathbf { M } _ { 0 } = \sum \mathbf { r } _ { i } \times \boldsymbol { m } _ { i } \ddot { \mathbf { R } } _ { i } - \sum \mathbf { r } _ { i } \times \dot { \boldsymbol { m } } _ { i } \mathbf { u } _ { i } } \end{array}
$$

which could have been obtained directly from Eq.7.1-4 byrecognizing that $( d / d t ) ( m _ { i } \dot { \bf R } _ { i } ) = m _ { i } \ddot { \bf R } _ { i } - \dot { m } _ { i } { \bf u } _ { i }$ (see Sec. 7.7).\*

We now replace $\ddot { \mathbb { R } } _ { i }$ by the general expression for acceleration,

$$
\ddot { \bf R } _ { i } = \ddot { \bf R } _ { 0 } + \dot { \boldsymbol { \omega } } \times \boldsymbol { \mathrm {  ~ r ~ } } _ { i } + \boldsymbol { \omega } \times ( \boldsymbol { \omega } \times \boldsymbol { \mathrm {  ~ r ~ } } _ { i } ) + [ \ddot { \boldsymbol { \mathrm { r } } } _ { i } ] + 2 \boldsymbol { \omega } \times [ \dot { \boldsymbol { \mathrm { r } } } _ { i } ]
$$

where [r] and $[ \ddot { \mathbf { r } } _ { i } ]$ are velocity and acceleration relative to the moving coordinate system,

$$
\begin{array} { r } { \mathbf { M } _ { 0 } = - \ddot { \mathbf { R } } _ { 0 } \times m \bar { \mathbf { r } } + \sum \mathbf { r } _ { i } \times ( \dot { \boldsymbol { \omega } } \times m _ { i } \mathbf { r } _ { i } ) + \sum \mathbf { r } _ { i } \times \{ \boldsymbol { \omega } \times m _ { i } ( \boldsymbol { \omega } \times \mathbf { r } _ { i } ) \} } \\ { + \sum \mathbf { r } _ { i } \times m _ { i } [ \ddot { \mathbf { r } } _ { i } ] + 2 \sum \mathbf { r } _ { i } \times ( \boldsymbol { \omega } \times m _ { i } [ \dot { \mathbf { r } } _ { i } ] ) - \sum \mathbf { r } _ { i } \times \dot { m } _ { i } \mathbf { u } _ { i } ( 7 . 1 1 - 9 ) } \end{array}
$$

To recognize the moment equation in terms of familiar expressions, we

$\mathbf { \nabla } ^ { \ast } \mathbf { F } = m \frac { d \mathbf { v } } { d t } - \mathbf { u } \frac { d m } { d t } = \mathsf { a p }$ plied external force,therefore $M _ { 0 }$ is the imoment of the externally applied force.

introduce the moment of inertia diadic of Sec. 5.2 and identify the following:

$$
\begin{array} { r l r } {  { \frac { d } { d t } ( \boldsymbol { \mathcal { I } } \cdot \boldsymbol { \omega } ) = \mathcal { I } \cdot \dot { \boldsymbol { \omega } } + \omega \times \mathcal { I } \cdot \boldsymbol { \omega } + [ \dot { \mathcal { I } } ] \cdot \boldsymbol { \omega } } } \\ & { } & { \mathcal { I } \cdot \dot { \boldsymbol { \omega } } = \sum \mathbf { r } _ { i } \times ( \dot { \boldsymbol { \omega } } \times m _ { i } \mathbf { r } _ { i } ) } \\ & { } & { \omega \times \mathcal { I } \cdot \boldsymbol { \omega } = \sum \mathbf { r } _ { i } \times \{ \boldsymbol { \omega } \times m _ { i } ( \omega \times \mathbf { r } _ { i } ) \} } \\ & { } & { [ \dot { \mathcal { I } } ] \cdot \boldsymbol { \omega } = \sum [ \dot { \mathbf { r } } _ { i } ] \times m _ { i } ( \omega \times \mathbf { r } _ { i } ) + \sum \mathbf { r } _ { i } \times ( \omega \times m _ { i } [ \dot { \mathbf { r } } _ { i } ] ) } \\ & { } & { + \sum \mathbf { r } _ { i } \times \dot { m } _ { i } ( \omega \times \mathbf { r } _ { i } ) \quad ~ ( 7 } \end{array}
$$

Supplying the missing terms by adding and subtracting, the moment equation can be writen in the following forms:

$$
\begin{array} { r l } & { \mathbf { M } _ { 0 } = - \ddot { \mathbf { R } } _ { 0 } \times m \bar { \mathbf { r } } + \mathcal { I } \cdot \dot { \boldsymbol { \omega } } + \boldsymbol { \omega } \times \mathcal { I } \cdot \boldsymbol { \omega } } \\ & { \qquad + \sum \mathbf { r } _ { i } \times m _ { i } [ \ddot { \mathbf { r } } _ { i } ] + 2 \sum \mathbf { r } _ { i } \times ( \boldsymbol { \omega } \times m _ { i } [ \dot { \mathbf { r } } _ { i } ] ) - \sum \mathbf { r } _ { i } \times \dot { m } _ { i } \mathbf { u } _ { i } ( 7 . 1 1 - \dot { \mathbf { r } } _ { i } ) } \\ & { \mathbf { M } _ { 0 } = - \ddot { \mathbf { R } } _ { 0 } \times m \bar { \mathbf { r } } + \frac { d } { d t } \mathcal { I } \cdot \boldsymbol { \omega } } \end{array}
$$

$$
\begin{array} { r l r } & { - \sum \left[ \dot { \bf r } _ { i } \right] \times m _ { i } ( { \bf \omega } \times { \bf r } _ { i } ) + \sum { \bf r } _ { i } \times m _ { i } ( { \bf \omega } \times \left[ \dot { \bf r } _ { i } \right] ) + \sum { \bf r } _ { i } \times m _ { i } [ \ddot { \bf r } _ { i } ] } & \\ & { - \sum { \bf r } _ { i } \times \dot { m } _ { i } { \bf u } _ { i } - \sum { \bf r } _ { i } \times \dot { m } _ { i } ( { \bf \omega } \times { \bf r } _ { i } ) } & { ( 7 . 1 1 - 1 2 } \end{array}
$$

A third and a more convenient form can be found by reducing the first two terms of the second line in Eq. 7.11-12 into a single term by the following equation.\*

$$
\begin{array} { c } { \mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) + ( \mathbf { b } \times \mathbf { a } ) \times \mathbf { c } = \mathbf { b } \times ( \mathbf { a } \times \mathbf { c } ) } \\ { \sum \mathbf { r } _ { i } \times m _ { i } ( \mathbf { \omega } \times [ \dot { \mathbf { r } } _ { i } ] ) + \sum m _ { i } ( \mathbf { \omega } \times \mathbf { r } _ { i } ) \times [ \dot { \mathbf { r } } _ { i } ] = \mathbf { \omega } \times \sum \left( \mathbf { r } _ { i } \times m _ { i } [ \dot { \mathbf { r } } _ { i } ] \right) } \end{array}
$$

The third form of the moment equation then becomes

$$
\begin{array} { l } { \displaystyle \mathbf { M } _ { 0 } = - \ddot { \textbf { R } } _ { 0 } \times \mathfrak { m } \bar { \mathbf { r } } + \frac { d } { d t } ( \mathcal { I } \cdot \boldsymbol { \omega } ) } \\ { \displaystyle \qquad + \textbf { \omega } \times \sum \left( \mathbf { r } _ { i } \times \mathbf { \nabla } m _ { i } [ \ddot { \mathbf { r } } _ { i } ] \right) + \sum \mathbf { r } _ { i } \times \mathbf { \nabla } m _ { i } [ \ddot { \mathbf { r } } _ { i } ] } \\ { \displaystyle \qquad - \sum \mathbf { r } _ { i } \times \dot { m } _ { i } \mathbf { u } _ { i } - \sum \mathbf { r } _ { i } \times \dot { m } _ { i } ( \boldsymbol { \omega } \times \mathbf { r } _ { i } ) } \end{array}
$$

The various terms of these equations can now be identified. We have in the first term the effect of the origin of the bodycoordinates not coinciding with the mass center.The terms $\mathcal { I } \cdot \dot { \omega } + \omega \times \mathcal { I } \cdot \omega$ correspond to the

\* This equation results from the application of the relationship

$$
{ \bf a } \times ( { \bf b } \times { \bf c } ) = { \bf b } ( { \bf a } \cdot { \bf c } ) - { \bf c } ( { \bf a } \cdot { \bf b } ) .
$$

$^ \dagger$ See Probs. 18 and 19 p. 111.

usual Euler equation, whereas $( d / d t ) ( \mathcal { I } \cdot \omega )$ includes the additional term [S]·ω which accounts for the rate of change of the inertia diadic resulting from the position change of the particles in relative motion and the variation of mass. The term ∑r X mu, is the thrust misalignment moment,\* while the term $- \sum \mathbf { r } _ { i } \times \dot { m } _ { i } ( \boldsymbol { \omega } \times \mathbf { r } _ { i } )$ is the jet damping due to rotation of the body. All other terms are due to relative motion of particles.Thethreeforms of the momentequation,Eqs.7.11-11,7.112, and 7.11-13 are presented here to show the origin of the various terms, some of which were inserted due to $[ { \dot { \mathcal { S } } } ] \cdot \mathbf { \omega } \mathbf { \omega }$

To complete the discussion, it must be recognized that the external moment may result from the forces not directed through the origin of the body coordinates. The external forces accelerate the instantaneous center of massand change the linear momentum of the ejected particles according to the equation

$$
\begin{array} { r } { \mathbf { F } = m [ \ddot { \mathbf { R } } _ { 0 } + \boldsymbol { \omega } \times ( \boldsymbol { \omega } \times \bar { \mathbf { r } } ) + \dot { \boldsymbol { \omega } } \times \bar { \mathbf { r } } + 2 \boldsymbol { \omega } \times [ \dot { \bar { \mathbf { r } } } ] + [ \ddot { \bar { \mathbf { r } } } ] ] - \sum \dot { m } _ { i } \mathbf { u } _ { i } } \end{array}
$$

Thus, in the general case, the force equations are coupled to the moment equations.

# Example 7.11-1

A space vehicle is moving under a force-free condition. If a motor located at $\mathbf { r } _ { 1 }$ is started, determine its perturbation torque.

The perturbation torque is the contribution from the relative motion terms of Eqs. 7.11-11, 7.11-12, or 7.11-13. We will use the form given by Eq. 7.11-13, which is (with total mass a constant, $\dot { m } = 0$ ）

$$
\begin{array} { r } { M _ { p } = [ \dot { \bar { \mathcal { S } } } ] \cdot \boldsymbol { \omega } + \boldsymbol { \omega } \times \sum ( \boldsymbol { r } _ { i } \times \boldsymbol { m } _ { i } [ \dot { \boldsymbol { \mathbf { r } } } _ { i } ] ) + \sum \boldsymbol { \mathbf { r } } _ { i } \times \boldsymbol { m } _ { i } [ \ddot { \boldsymbol { \mathbf { r } } } _ { i } ] } \end{array}
$$

Owing to the symmetry of the motor rotor, the change in the inertia diadic relative to the body coordinates resulting from the spin of the rotor is zero, which eliminates the first term $[ { \dot { \mathcal { S } } } ] \cdot \omega = 0$

From Fig. 7.11-3,we have,

$$
\begin{array} { c } { \mathbf { r } _ { i } = \mathbf { r } _ { 1 } + \mathsf { \pmb \rho } _ { i } } \\ { \left[ \dot { \mathbf { r } } _ { i } \right] = \mathbf { \omega } _ { 1 } \times \mathsf { \pmb \rho } _ { i } } \\ { \left[ \ddot { \mathbf { r } } _ { i } \right] = \dot { \omega _ { 1 } } \times \mathsf { \pmb \rho } _ { i } } \end{array}
$$

and noting that ∑mp =O for a symmetrical wheel, the equationfor the perturbation torque becomes,

$$
\begin{array} { r } { M _ { p } = \boldsymbol { \omega } \times \left[ \sum \mathsf { p } _ { i } \times ( \boldsymbol { \omega } _ { 1 } \times \boldsymbol { m } _ { i } \mathsf { p } _ { i } ) \right] + \sum \mathsf { p } _ { i } \times ( \dot { \boldsymbol { \omega } } _ { 1 } \times \boldsymbol { m } _ { i } \mathsf { p } _ { i } ) } \end{array}
$$

Since

$$
\begin{array} { r } { \sum _ { \boldsymbol { \rho } _ { i } } \times ( \boldsymbol { \omega } _ { 1 } \times \boldsymbol { m } _ { i } \boldsymbol { \mathsf { \rho } _ { i } } ) = \mathcal { I } _ { 1 } \cdot \boldsymbol { \omega } _ { 1 } = ( C _ { 1 } \boldsymbol { \omega } _ { 1 } ) \mathbf { k } _ { 1 } = \mathbf { h } _ { 1 } } \end{array}
$$

the equation for $\mathbf { M } _ { p }$ can be written as

$$
{ \bf M } _ { p } = [ \dot { \bf h } _ { 1 } ] + \boldsymbol { \omega } \times { \bf h } _ { 1 }
$$

\* Letting $\begin{array} { r } { \mathbf { M } _ { T } = \sum \mathbf { r } _ { i } \times \dot { m } _ { i } \mathbf { u } _ { i } = } \end{array}$ moment of the thrusting jet, the monent acting on the varying mass is $\mathbf { M } _ { 0 } + \mathbf { M } _ { T }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/ffd6b50fce3e768287742b64b255237118c7a48f3ddb268963ca35be1a62dade.jpg)  
Fig.7.ll-3. Perturbation torque due to rotation of wheel.

where $\mathbf { h } _ { 1 }$ is the angular momentum of the rotor wheel. Thus the perturbation torque is the result of the angular acceleration of the wheel, and the precession of the angular momentum vector of the wheel caused by the rotation w of the body coordinates.

# PROBLEMS

1. A uniform rigid bar of length $l$ and mass $m$ is translating with constant velocity $\dot { \mathbb { R } } _ { 0 }$ in a direction normal to its length. At the same time a mass $m _ { 0 }$ is sliding from one end to the other with velocity [r]. Placing bodycoordinates as indicated in the sketch, verify from Eq.7.11-3 that the moment about $o$ is zero. Describe the motion of $o$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/608c879c8774f60c3f49447c6475ff9ac4217629d4975703f6e435e5b5dc8e8c.jpg)  
Prob. 1

2. The center of mass of a uniform rigid bar of length Iis moving with constant velocity $\dot { \bf R }$ along a straight line, while the bar rotates with constant angular velocity $\boldsymbol { \omega }$ Placing body axes as shown, verify from Eq. 7.11-3 that the moment about $o$ is zero.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/48d7226ec6d38e7ec71b97308a47f7113ca8b5b6e2d943ac8f480e07abf10bb6.jpg)  
Prob.2

3. For a system of particles which is not changing in mass, write the equation forthe moment about its center of mass when relative motion betweeen particles is allowed.

4. Consider a constant-mass system such as a satellite in orbit,and assume body axes x,y, $z$ through its center of mass and coinciding with the principal axes. There is a motor on the pitch axis $_ x$ a distance $x _ { 0 }$ from $O$ with its axis of rotation parallel to the $\mathcal { Y }$ axis. Let the rotor moment of inertia be $\boldsymbol { I _ { y } } ^ { \prime }$ and that of the entire satelite including the motor to be $A$ $A$ $C$ about x,y,z respectively. If the motor is started with angular acceleration $\dot { \omega } _ { 1 }$ ,define the terms in Eq. 7.11-11 which apply to the problem,and write the components of the moment equation.

5. Show that the angular momentum of a group of particles about an arbitrary origin is equal to

$$
{ \bf h } _ { 0 } = - \dot { \bf R } _ { 0 } \times m \bar { \bf r } + \int { \bf r } \times ( { \bf \omega } \times { \bf r } ) d m + \int { \bf r } \times [ \dot { \bf r } ] d m
$$

where $\mathcal { I } \cdot \omega = \int \mathbf { r } ~ \times ~ ( \omega ~ \times ~ \mathbf { r } ) ~ d r$ n and[r]is the velocity relative to the rotat-ing body axes.

6. Show that the terms of the equation

$$
\frac { d } { d t } \left( \boldsymbol { \mathcal { S } } \cdot \boldsymbol { \omega } \right) = \boldsymbol { \mathcal { S } } \cdot \dot { \boldsymbol { \omega } } + \boldsymbol { \omega } \times \boldsymbol { \mathcal { I } } \cdot \boldsymbol { \omega } + [ \dot { \boldsymbol { \mathcal { I } } } ] \cdot \boldsymbol { \omega }
$$

can be identified as

$$
{ \begin{array} { r l } & { \qquad { \mathcal { S } } \cdot { \dot { \boldsymbol { \omega } } } = { \int } \mathbf { r } \times { \dot { \boldsymbol { \omega } } } \times \mathbf { r } d m } \\ & { \qquad \quad } \\ & { \qquad \cup \times { \mathcal { I } } \cdot \boldsymbol { \omega } = { \int } \mathbf { r } \times [ \boldsymbol { \omega } \times ( \boldsymbol { \omega } \times \mathbf { r } ) ] d m } \\ & { \qquad \quad } \\ & { \qquad [ { \dot { \mathcal { I } } } ] \cdot \boldsymbol { \omega } = { \int } \mathbf { r } \times ( \boldsymbol { \omega } \times [ \dot { \mathbf { r } } ] ) d m + { \int } [ \dot { \mathbf { r } } ] \times ( \boldsymbol { \omega } \times \mathbf { r } ) d m + { \int } \mathbf { r } \times ( \boldsymbol { \omega } \times \mathbf { r } ) d \dot { m } } \end{array} }
$$

7. Show that

$$
\begin{array} { l } { \displaystyle \frac { d } { d t } \int _ { \mathbf { r } } \times [ \dot { \mathbf { r } } ] d m = \int _ { \mathbf { r } } \times [ \ddot { \mathbf { r } } ] d m + \int _ { \mathbf { r } } \times ( \mathfrak { o } \times [ \dot { \mathbf { r } } ] ) d m + \int ( \mathfrak { o } \times \mathbf { r } ) } \\ { \displaystyle \qquad \times [ \dot { \mathbf { r } } ] d m + \int _ { \mathbf { r } } \times [ \dot { \mathbf { r } } ] d \dot { m } } \end{array}
$$

Combining the results of Prob. 5 and 6, two of the terms add to give $2 \int \mathbf { r } \times ( { \boldsymbol { \omega } } \times [ { \dot { \mathbf { r } } } ] ) ~ c$ dm,whiletheterms $\int \left( \omega \times \mathbf { r } \right) \times \left[ \dot { \mathbf { r } } \right] d m$ cancel each other. Now clarify the interpretation of Eqs. 7.11-9, 7.11-10, 7.11-11, and 7.11-12.

8. Write the component equations for the two terms

$$
\begin{array} { r } { - \sum [ \dot { \mathbf { r } } _ { i } ] \times m _ { i } ( \boldsymbol { \omega } \times \mathbf { r } _ { i } ) + \sum \mathbf { r } _ { i } \times m _ { i } ( \boldsymbol { \omega } \times [ \dot { \mathbf { r } } _ { i } ] ) } \end{array}
$$

of Eq. 7.11-12.

9. Write out the component terms of $[ \dot { \mathcal { F } } ] \cdot \omega$ and show that they represent the time derivative of $\mathcal { P } \cdot \boldsymbol { \omega }$ relative to the body coordinates. Identify the parts due to relative motion of the particles and those due to mass variation.

10. Show that ${ \mathcal { S } } = \sum m _ { i } ( \mathbf { r } _ { i } \cdot \mathbf { r } _ { i } { \boldsymbol { \mathcal { E } } } - \mathbf { r } _ { i } \mathbf { r } _ { i } )$ ,where $\mathcal { E } = \mathbf { i } \mathbf { i } + \mathbf { j } \mathbf { j } + \mathbf { k } \mathbf { k }$ is a unit diad. Showalso that

$$
\begin{array} { r } { [ \dot { \mathcal { S } } ] = \sum \dot { m } _ { i } ( \mathbf { r } _ { i } \cdot \mathbf { r } _ { i } \boldsymbol { \mathcal { O } } - \mathbf { r } _ { i } \mathbf { r } _ { i } ) + \sum m _ { i } ( \dot { \mathbf { r } } _ { i } \cdot \mathbf { r } _ { i } \boldsymbol { \mathcal { O } } + \mathbf { r } _ { i } \cdot \dot { \mathbf { r } } _ { i } \boldsymbol { \mathcal { O } } - \dot { \mathbf { r } } _ { i } \mathbf { r } _ { i } - \mathbf { r } _ { i } \dot { \mathbf { r } } _ { i } ) } \end{array}
$$

11. Derive Eqs. 7.9-7 and 7.9-8 as a special case of the general equation, Eq. 7.11-12. State the restrictions imposed on Eq. 7.11-12 in arriving at the above equations.

12. A symmetrical spinning satelite in orbit has moments of inertia A, A, $C$ about the $x , y , z$ axes (including $m _ { 0 }$ at position $\zeta = 0$ ),as shownin thesketch.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/78b53b2e0581c8bb7117f57f331202fd47c88f7d5bd1e993b68eb1267edfcbd9.jpg)  
Prob.12

If the mass mo is restricted to move in thezdirection and hasarestoring spring stifness of $k$ with viscous damping $c$ showthatthediferentialequaonsof motion are:

Moment:

$$
\begin{array} { r l } & { \mathbf { M } _ { 0 } = \mathbf { i } \bigg \{ ( \mathcal { A } + m _ { 0 } \zeta ^ { 2 } ) \dot { \omega } _ { x } + ( C - A - m _ { 0 } \zeta ^ { 2 } ) \omega _ { y } \omega _ { z } - m _ { 0 } x _ { 0 } \zeta \dot { \omega } _ { z } - m _ { 0 } x _ { 0 } \zeta \omega _ { z } \omega _ { y } } \\ & { \qquad \quad + 2 m _ { 0 } \zeta \dot { \omega } _ { z } - \frac { \mathbf { m } _ { 0 } ^ { 2 } } { m } [ 2 \zeta \omega _ { z } + \zeta ( \dot { \omega } _ { x } - \omega _ { y } \omega _ { z } ) ] \zeta \bigg \} } \\ & { + \mathbf { i } \bigg \} \big ( \mathcal { A } + m _ { 0 } \zeta ^ { 2 } ) \dot { \omega } _ { y } - ( C - A - m _ { 0 } \zeta ^ { 2 } ) \omega _ { x } \omega _ { z } + m _ { 0 } x _ { 0 } \zeta ( \omega _ { z } ^ { 2 } - \omega _ { z } ^ { 2 } ) - m _ { 0 } x _ { 0 } \zeta } \\ & { \qquad \quad + 2 m _ { 0 } \zeta \dot { \zeta } \omega _ { y } - \frac { m _ { 0 } ^ { 2 } } { m } [ 2 \zeta \dot { \omega } _ { x } - \zeta ( \dot { \omega } _ { y } - \omega _ { z } \omega _ { z } ) ] \zeta \bigg \} } \\ & { + \mathbf { k } ( C \dot { \omega } _ { z } - m _ { 0 } x _ { 0 } \zeta \dot { \omega } _ { z } + m _ { 0 } x _ { 0 } \zeta \omega _ { y } \omega _ { z } - 2 m _ { 0 } x _ { 0 } \zeta \omega _ { z } ) } \end{array}
$$

Force on mass $m _ { 0 }$ in $\boldsymbol { \kappa }$ direction:

$$
\begin{array} { c } { { F _ { z } = m _ { 0 } [ \ddot { \zeta } - x _ { 0 } \dot { \omega } _ { y } + x _ { 0 } \omega _ { x } \omega _ { z } - \zeta ( { \omega } _ { x } { } ^ { 2 } + { \omega } _ { y } { } ^ { 2 } ) ] + { \displaystyle \frac { m _ { 0 } { } ^ { 2 } } { m } } \left[ \zeta ( { \omega } _ { x } { } ^ { 2 } + { \omega } _ { y } { } ^ { 2 } ) - \ddot { \zeta } \right] } } \\ { { + c \dot { \zeta } + k \zeta = 0 } } \end{array}
$$

Acceleration of origin:

$$
\begin{array} { l } { { \displaystyle { \ddot { \bf R } } _ { 0 } = - \frac { m _ { 0 } } { m } [ 2 \zeta \omega _ { y } + \zeta ( \dot { \omega } _ { y } + \omega _ { x } \omega _ { z } ) ] \mathbf { i } + \frac { m _ { 0 } } { m } [ 2 \dot { \zeta } \omega _ { x } + \zeta ( \dot { \omega } _ { x } - \omega _ { y } \omega _ { z } ) ] } } \\ { ~ } \\ { { \displaystyle ~ + \frac { m _ { 0 } } { m } [ \zeta ( \omega _ { x } { } ^ { 2 } + \omega _ { y } { } ^ { 2 } ) - \zeta ] \mathbf { k } } } \end{array}
$$

# REFERENCES

1. H. J. Cohen,"The Effect of Jet Damping on the Motion of the Able-1 Third Stage," Space Technology Laboratories Interoffice Correspondence (April 15,1960).   
2. Ellis, J. W., and C. W. McArthur, "Applicability of Euler's Dynamical Equations to Rocket Motion," ARS Jour., 29, No. 11 (Nov. 1959), 863-864.   
3. Jarmolow, K.,"Dynamics of a Spinning Rocket with Varying Inertia and Applied Moment," J. Appl. Phys.,28, No.3 (1957),308-313.   
4. Leon, H.,"Angle of Attack Convergence of a Spinning Missile Descending Through the Atmosphere," J. Aero/Space Sci., 25, No. 8 (Aug. 1958), 480-484.   
5. Leon,H.,"Spin Dynamics of Rockets and Space Vehicles in Vacuum," TR 59-0000 00787, Space Technology Laboratories (Sept. 16,1959).   
6. Pilkington,W.C.,"Vehicle Motion as Inferred from Radio-Signal-Strength Records," External Publication No. 551, Jet Propulsion Laboratory, Pasadena,Calif. (Sept.5, 1958).   
7. Reiter,G.,Space Technology Laboratories Memo (June 17,1959).   
8. Thomson, W. T.,and G.S.Reiter,“Attitude Drift of Space Vehicles,"J. Astronaut. Sci., VII, No. 2 (1960),29--34.   
9. Roberson, R. E., “Torques on a Satellite Vehicle from Internal Moving Parts," J. Appl. Mech., 25, No.2 (June 1958), 196-200.

# Performance and Optimization
