# CHAPTER 6

# 6.1 Small Oscillations of Gyros

If the gyro or top of Fig. 5.13-1 is given a slight disturbance from its steady state, we can show that the oscilations about the steady values wil be harmonic.

We can begin with Eqs. 5.13-4, which are the moment equations about the node system coordinates shown in Fig. 6.1-1.

$$
\begin{array} { c } { { W l \sin \theta = A \ddot { \theta } + C n \dot { \psi } \sin \theta - A \dot { \psi } ^ { 2 } \sin \theta \cos \theta } } \\ { { 0 = A \ddot { \psi } \sin \theta + 2 A \dot { \psi } \dot { \theta } \cos \theta - C n \dot { \theta } } } \\ { { 0 = C \dot { n } } } \end{array}
$$

Letting the steady-state values of $\theta$ and $\dot { \psi }$ be $\theta _ { 0 }$ and $\dot { \psi } _ { 0 }$ , and designating the deviations about the steady values by $\theta _ { \sim }$ and $\dot { \psi } _ { \sim }$ , the instantaneous values of $\theta$ and $\dot { \psi }$ are,

$$
\begin{array} { c } { { \theta = \theta _ { 0 } + \theta _ { \sim } } } \\ { { \dot { \psi } = \dot { \psi } _ { 0 } + \dot { \psi } _ { \sim } } } \end{array}
$$

For small oscillations we can make the following approximations.

$$
\begin{array} { r } { \dot { \theta } \dot { \psi } = \dot { \theta } _ { \sim } ( \dot { \psi } _ { 0 } + \dot { \psi } _ { \sim } ) \underline { { \simeq } } \dot { \theta } _ { \sim } \dot { \psi } _ { 0 } } \\ { \sin \theta \cong \sin \theta _ { 0 } + \theta _ { \sim } \cos \theta _ { 0 } } \\ { \cos \theta \cong \cos \theta _ { 0 } - \theta _ { \sim } \sin \theta _ { 0 } } \end{array}
$$

Substituting these expressions into the second of Eq. 6.1-1 and neglecting products and squares of the small deviations, we obtain,

$$
A \ddot { \psi } _ { \sim } \sin \theta _ { 0 } + 2 A \dot { \theta } _ { \sim } \dot { \psi } _ { 0 } \cos \theta _ { 0 } - C n \dot { \theta } _ { \sim } = 0
$$

Integrating,

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/c45826147fd4fec208b1a0beaa1fcff3775d6fd1a0be611cb3a7619840fbff1d.jpg)  
Fig. 6.l-l. Angular momentum along node system coordinates.

Likewise,from the first of Eq. 6.1-1, we obtain,

$$
\begin{array} { r } { A \ddot { \theta } _ { \sim } - A ( \dot { \psi } _ { 0 } ^ { 2 } + 2 \dot { \psi } _ { 0 } \dot { \psi } _ { \sim } ) ( \sin \theta _ { 0 } \cos \theta _ { 0 } - \theta _ { \sim } \sin ^ { 2 } \theta _ { 0 } + \theta _ { \sim } \cos ^ { 2 } \theta _ { 0 } ) } \\ { + C n ( \dot { \psi } _ { 0 } + \dot { \psi } _ { \sim } ) ( \sin \theta _ { 0 } + \theta _ { \sim } \cos \theta _ { 0 } ) = W l ( \sin \theta _ { 0 } + \theta _ { \sim } \cos \theta _ { 0 } ) } \end{array}
$$

However, for steady precession $\ddot { \theta }$ is zero, and the steady components of Eq. 6.1-4 are,

$$
- A { \dot { \psi } _ { 0 } } ^ { 2 } \cos \theta _ { 0 } + C n \dot { \psi } _ { 0 } = W l
$$

Thus by striking out these terms in Eq.6.1-4 and introducingEq.6.1-3 to eliminate $\dot { \psi } _ { \sim }$ ,we arrive at the second-order differential equation in $\theta _ { \sim }$ ：

$$
A ^ { 2 } { \ddot { \theta } } _ { \sim } + [ ( C n ) ^ { 2 } - 4 A W l \cos \theta _ { 0 } + A ^ { 2 } { \dot { \psi } } _ { 0 } { } ^ { 2 } ( 1 - \cos ^ { 2 } \theta _ { 0 } ) ] \theta _ { \sim } = 0
$$

The nodding oscilations are therefore sinusoidal with period equal to,

$$
\tau _ { 0 } = \frac { 2 \pi } { \omega _ { 0 } } = \frac { 2 \pi A } { \sqrt { ( C n ) ^ { 2 } - 4 A W l \cos \theta _ { 0 } + A ^ { 2 } \dot { \psi } _ { 0 } { } ^ { 2 } ( 1 - \cos ^ { 2 } \theta _ { 0 } ) } }
$$

If $n$ is very large, the nutation period reduces to,

$$
\tau _ { \theta } \cong { \frac { 2 \pi A } { C n } }
$$

The precession period is also the same since, from Eq. 6.1-3,

$$
\dot { \psi } _ { \sim } = \left( \frac { C n - 2 A \dot { \psi } _ { 0 } \cos \theta _ { 0 } } { A \sin \theta _ { 0 } } \right) \theta _ { \sim }
$$

and $\dot { \psi } _ { \sim }$ is proportional to $\theta _ { \sim }$

When cos $\theta _ { 0 } = 1$ ,we have the sleeping top and,in order for the denominator of Eq. 6.1-6 to be real, $( C n ) ^ { 2 }$ must be greater than $4 A W l .$ Thus, again, we verify the stability requirement for the sleeping top, which is,

$$
n > \frac { 2 } { C } \sqrt { A W l }
$$

# 6.2 Oscillations About Gimbal Axes

Figure 6.2-1 shows the two gimbal gyro with the mass center coinciding with the geometric center of the gimbals. We wish now to write the moment

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/35b116dbab0304cb5ddf7271d87ae31f05c781618db39fcbc82d365bf980659a.jpg)  
Fig. 6.2-l. Symmetric gyro with gimbal axes § and Z.

equations about the gimbal bearing axes. Neglecting again the mass of the gimbals,the moments of inertia about the 5,), &axes are A,A,C,of the wheel.

The angular velocities and angular momentum about the $\xi$ ， $\eta$ ， $\zeta$ axes are the same as in Sec.5.13,and the moment equations about the $\xi$ $\eta$ ， $\zeta$ axes are rewritten in the following form.

$$
\begin{array} { r l } & { M _ { \xi } = A \ddot { \theta } + C n \dot { \psi } \sin \theta - A \dot { \psi } ^ { 2 } \sin \theta \cos \theta } \\ & { M _ { \eta } = A ( \ddot { \psi } \sin \theta + 2 \dot { \psi } \dot { \theta } \cos \theta ) - C n \dot { \theta } } \\ & { M _ { \zeta } = C \frac { d } { d t } ( \dot { \varphi } + \dot { \psi } \cos \theta ) } \end{array}
$$

The moments $M _ { \eta }$ and $M _ { \zeta }$ can be resolved along the vertical $Z$ axis and in the horizontal plane. The $Z$ component is (i.e., $M _ { \zeta } = 0$ ），

$$
\begin{array} { r } { M _ { Z } = M _ { \eta } \sin \theta + M _ { \zeta } \cos \theta = M _ { \eta } \sin \theta } \\ { = A \ddot { \psi } \sin ^ { 2 } \theta + 2 A \dot { \psi } \dot { \theta } \sin \theta \cos \theta - C n \dot { \theta } \sin \theta } \end{array}
$$

These nonlinear equations can be linearized under certain simplifying assumptions. Usually the spin $\dot { \varphi }$ is very large in comparison to $\dot { \psi }$ and $\dot { \theta }$ The spin $\dot { \varphi }$ is then approximately equal to n which is a constant of large magnitude. Neglecting the squares and products of the smaller quantities $\dot { \psi }$ and $\dot { \theta }$ ,the simplified equations of interest are,

$$
\begin{array} { l } { { M _ { \xi } = A \ddot { \theta } + C n \dot { \psi } \sin \theta } } \\ { { M _ { Z } = A \ddot { \psi } \sin ^ { 2 } \theta - C n \dot { \theta } \sin \theta } } \end{array}
$$

Several interesting solutions of the above equations are possible depending on the type of excitation. We can first examine the steady precession condition,

$$
\begin{array} { l } { { \theta = \theta _ { 0 } } } \\ { { \dot { \psi } = \dot { \psi } _ { 0 } } } \\ { { \dot { \theta } = \ddot { \theta } = \ddot { \psi } = 0 } } \end{array}
$$

The above equations then become,

$$
\begin{array} { l } { { M _ { \xi 0 } = C n \dot { \psi } _ { 0 } \sin \theta _ { 0 } } } \\ { { M _ { Z 0 } = 0 } } \end{array}
$$

which requires a constant torque $M _ { \xi 0 }$ about the horizontal gimbal axis, as found previously in Sec. 5.14.

We can now consider the problem where the spin axis under steady precession is given a disturbance by a moment $M _ { \xi } ( t )$

We will assume small oscillations and introduce the equations,

$$
\begin{array} { c c } { { \theta = \theta _ { 0 } + \theta _ { \sim } } } & { { \sin \theta = \sin \theta _ { 0 } + \theta _ { \sim } \cos \theta _ { 0 } } } \\ { { \dot { \psi } = \dot { \psi } _ { 0 } + \dot { \psi } _ { \sim } } } & { { \cos \theta = \cos \theta _ { 0 } - \theta _ { \sim } \sin \theta _ { 0 } } } \end{array}
$$

Again neglectingproductsofthesallocillatrytrms,Eqs.me

$$
\ddot { \theta } _ { \sim } + \frac { C n } { \mathcal { A } } \left( \dot { \psi } _ { 0 } \theta _ { \sim } \cos \theta _ { 0 } + \dot { \psi } _ { 0 } \sin \theta _ { 0 } + \dot { \psi } _ { \sim } \sin \theta _ { 0 } \right) = \frac { M _ { \xi } ( t ) + M _ { \xi 0 } } { A }
$$

$$
\ddot { \psi } _ { \sim } \sin \theta _ { 0 } - \frac { C n } { A } \dot { \theta } _ { \sim } = 0
$$

Eliminatingtheteadystateterms,Eq.6.-4fromtheaboveadeting $C n / A = p$ ,we have the final form of the differential equations for the disturbance about the steady precession:

$$
\begin{array} { c } { { \ddot { \theta } _ { \sim } + p ( \dot { \psi } _ { 0 } \theta _ { \sim } \cos \theta _ { 0 } + \dot { \psi } _ { \sim } \sin \theta _ { 0 } ) = \frac { M _ { \xi } ( t ) } { A } } } \\ { { \ddot { \psi } _ { \sim } \sin \theta _ { 0 } - p \dot { \theta } _ { \sim } = 0 } } \end{array}
$$

The solution of these equations is most conveniently obtained by the use of Laplace transforms with $\theta _ { \sim }$ and $\dot { \psi } _ { \sim }$ as dependent variables.10 Since initially $\theta = \theta _ { 0 } , \hat { \theta } = 0 $ and $\dot { \psi } = \dot { \psi } _ { 0 }$ ， $\theta _ { \sim } ( 0 ) = \dot { \theta } _ { \sim } ( 0 ) = \dot { \psi } _ { \sim } ( 0 ) = 0$ ， and the transform equations are,

$$
\begin{array} { c } { { ( s ^ { 2 } + p \bar { \psi } _ { 0 } \cos \theta _ { 0 } ) \bar { \theta } _ { \sim } ( s ) + ( p \sin \theta _ { 0 } ) \bar { \psi } ( s ) = \displaystyle \frac { \bar { M } _ { \xi } ( s ) } { \cal A } } } \\ { { - p \bar { \theta } _ { \sim } ( s ) + ( \sin \theta _ { 0 } ) \bar { \psi } _ { \sim } ( s ) = 0 } } \end{array}
$$

By Cramer's rule, the equations for $\bar { \theta } _ { \sim } ( s )$ and $\bar { \dot { \psi } } _ { \sim } ( s )$ are,

$$
\begin{array} { r } { \bar { \theta } _ { \sim } ( s ) = \frac { \displaystyle \left| \frac { 1 } { { \cal A } } \bar { \cal M } _ { \varepsilon } ( s ) ~ p \sin \theta _ { 0 } \right| } { \displaystyle \left| ( s ^ { 2 } + p \dot { \psi } _ { 0 } \cos \theta _ { 0 } ) ~ p \sin \theta _ { 0 } \right| } } \\ { \bar { \theta } _ { \sim } ( s ) = \frac { \displaystyle \left| ( s ^ { 2 } + p \dot { \psi } _ { 0 } \cos \theta _ { 0 } ) - \frac { 1 } { 4 } \bar { \cal M } _ { \varepsilon } ( s ) \right| } { \displaystyle \left| ( s ^ { 2 } + p \dot { \psi } _ { 0 } \cos \theta _ { 0 } ) - \frac { 1 } { 4 } \bar { \cal M } _ { \varepsilon } ( s ) \right| } } \\ { \bar { \psi } _ { \sim } ( s ) = \frac { \displaystyle \left| ( s ^ { 2 } + p \dot { \psi } _ { 0 } \cos \theta _ { 0 } ) - \frac { 1 } { 4 } \bar { \cal M } _ { \varepsilon } ( s ) \right| } { \displaystyle \left| ( s ^ { 2 } + p \dot { \psi } _ { 0 } \cos \theta _ { 0 } ) - p \sin \theta _ { 0 } \right| } } \\ { - p ~ s \mathrm { i n } ~ \theta _ { 0 } ~ . } \end{array}
$$

which may be solved for any excitation $M _ { \xi } ( t )$ , and any angle $\theta _ { 0 }$

# Example 6.2-1

When the spin axis is at rest at $\theta _ { 0 } = \pi / 2$ , an impulse is applied to the spin axis, resulting in an impulsive moment Me(t) = M δ(t), where δ(t) is a delta function with the unit per second and $\hat { M }$ is the moment impulse in ib-in. sec. From Eqs. 6.2-8, we have

$$
\begin{array} { c c c } { { \bar { \theta } _ { \sim } ( s ) = \displaystyle \frac { \hat { M } } { \cal A } \displaystyle \frac { 1 } { s ^ { 2 } + p ^ { 2 } } } } \\ { { \overline { { { \psi } } } _ { \sim } ( s ) = \displaystyle \frac { p \hat { M } } { \cal A } \displaystyle \frac { 1 } { s ^ { 2 } + p ^ { 2 } } } } \end{array}
$$

and their time solutions are,

$$
\begin{array} { l l l } { { \displaystyle \theta _ { \sim } ( t ) = \frac { \hat { M } } { A p } \sin p t \quad } } & { { \displaystyle \dot { \theta } _ { \sim } ( t ) = \frac { \hat { M } } { A } \cos p t } } \\ { { \displaystyle \dot { \psi } _ { \sim } ( t ) = \frac { \hat { M } } { A } \sin p t \quad } } & { { \displaystyle \psi _ { \sim } ( t ) = \frac { \hat { M } } { A p } ( 1 - \cos p t ) } } \end{array}
$$

The actual position of the spin axis at any time is then equal to

$$
\begin{array} { l } { \displaystyle \theta ( t ) = \frac { \pi } { 2 } + \frac { \hat { M } } { A p } \sin p t } \\ { \displaystyle \psi ( t ) = \frac { \hat { M } } { A p } ( 1 - \cos p t ) } \end{array}
$$

These results can be interpreted as follows. Assume first that the spin axis is stationary so that $\dot { \psi } _ { 0 } = 0$ . The moment impulse $\hat { M }$ suddenly shifts the angular momentum vector $C n$ along the equator by an angle $\hat { M } / A p = \hat { M } / C n$ . The spin axis however cannot change instantaneously， but develops a downward velocity of $\dot { \theta } _ { \sim } ( 0 ) = \hat { M } / A$ from the equatorial position. Thus the rotation of the spin axis around the new resultant angular momentum vector generates a cone of base radius $\hat { M }$ ,as shown in Fig. 6.2-2. This is, of course, consistent with the conclusions of Sec. 5.8 which indicates that, with zero moment (with a delta function moment, the moment is zero at all $t$ except $t = 0$ ), the angular momentum vector is constant and stationary,and the spin axis will precess around it.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/db2d65dd509d0f570fd607936edc4746569942bec96cb4e920bfe97b24cc6faf.jpg)  
Fig.6.2-2. Motion of spin axis due to delta function impulse (initial moment is zero)

If next we consider an initial steady precession with the spin axis at $\theta _ { 0 } = \pi / 2$ due to a constant moment $M _ { \xi _ { 0 } }$ ,the resultant angular momentum vector h will be above the equator by the moment component Aγo. The moment impulse M will again suddenly shift the resultant h horizontally by an amount M along the latitude λ = Aγo/Cn, as shown in Fig. 6.2-3. At time t = O+,the spin axis will have angular velocity components 0(0) = $\hat { M } / A$ vertically, and $\dot { \psi } _ { 0 }$ horizontally. Their resultant will however be normal to the radial line from the h vector, as shown in Fig. 6.2-3. Thus the h vector of approximate length $C n$ will precess steadily along the latitude $\lambda = A \dot { \psi } _ { 0 } / C n$ with angular velocity $\dot { \psi } _ { 0 }$ while the spin axis will rotate around h in a circle of radius $\sqrt { { \hat { M } } ^ { 2 } + ( A { \dot { \psi } } _ { 0 } ) ^ { 2 } }$ The result is a combined nutation and precession, and the curve described by the spin axis depends on the relative magnitudes of the initial velocity components $\hat { M } / A$ and $\dot { \psi } _ { 0 }$ . This behavior is somewhat similar to the problem of the disturbed top, the difference being that we have here imposed a constant moment about the node axis $\xi$ ，whereas in the problem of the top, the gravity moment will change with 0. For small disturbances, however, the motions are identical.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/ea3fe209591ee070d80d1ba368a0bd164ed1a3626c8ac6c9e640c87ae2a4d8c0.jpg)  
Fig. 6.2-3. Motion of spin axis dues to delta function impulse (initial moment is contant, with steady precession $\dot { \psi } _ { 0 , }$

# PROBLEMS

1. With the axes initially at rest with $\theta = \pi / 2$ ,a constant moment is applied to the $\xi$ axis. Determine its solution.   
2. Repeat Prob. 1 if $M$ is a delta function $\hat { M } \delta ( t )$

3. With the system initially at rest at an angle $\theta _ { 0 }$ ,a constant moment is applied to the $O Z$ axis. Determine its motion,assuming $C n$ to be very large.

4. Consider $C \dot { \varphi }$ to be the only angular momentum of importance for $\dot { \varphi }$ large, and determine the time required for the $\zeta$ axis to rotate from the horizontal to the vertical position due to a constant moment $M _ { Z }$ about the $Z$ axis.

5.A satellite with spin moment of inertia $C$ and equal transverse moment of inertia $B = A$ has at the initial moment three collinear vectors,h, ω,and k, along the spin axis. To change its attitude,an impulsive torque $M _ { x } = \hat { M } \delta ( t )$ is applied to the transverse pitch axis. Determine the relative position of the three vectors immediately after impulse and the subsequent motion of the satellite.

6. Show that the three vectors of Prob. 5 can again be made collinear by applying an equal impulsive torque $M _ { x } = \hat { M } \overline { { { \delta } } } ( t )$ in the same direction after a half-cycle of precession, thereby producing an atitude change of $\tan ^ { - 1 } { ( 2 \hat { M } / C n ) }$ with no precession (see Fig. 6.2-2).Determine the spacing in time of the impulses.

7. It is proposed to change the attitude of the spin axis of a satellite with angular momentum $h \stackrel { = } { = } C n$ by an angle of $9 0 ^ { \mathrm { { \bar { o } } } }$ with a series of $N$ equal impulses, ending up with the h, $\boldsymbol { \omega }$ , and k vectors collinear. Determine the magnitude of the impulses and their time spacing.

8. Starting with Eq. 3.5-4 for the transformation between the body angular velocities $\omega _ { x } , ~ \omega _ { y } , ~ \omega _ { z }$ ， and the Euler angular rates, $\dot { \psi }$ ，， $\dot { \theta }$ ， show that the general solution for the Euler angles are given by the equations,

$$
\begin{array} { l } { \displaystyle \theta = \theta _ { 0 } + \int _ { 0 } ^ { t } ( \omega _ { x } \cos \varphi - \omega _ { y } \sin \varphi ) d t } \\ { \displaystyle \psi = \psi _ { 0 } + \int _ { 0 } ^ { t } \left( \frac { \omega _ { x } \sin \varphi + \omega _ { y } \cos \varphi } { \sin \theta } \right) d t } \\ { \displaystyle \varphi = \varphi _ { 0 } + \int _ { 0 } ^ { t } \dot { \varphi } d t } \end{array}
$$

9. For small oscillations with $\dot { \varphi } =$ constant, discuss the solution for $\theta$ and $\psi$ of Prob. 8 as influenced by the value of $\theta _ { 0 }$ which may be arbitrarily chosen. Why is $\theta _ { 0 } = \pi / 2$ desirable for small angle solutions?

10. With $\theta _ { 0 } = \pi / 2$ intheequationsofProb8solveProbfor $\theta$ and $\psi$ by first determining the angular rates about the body-fixed axes $_ x$ and $y$ ：

11. Assume that the rotor of Fig. 6.2-1 is misaligned so that its normal (axis $z$ makes an angle α with the spin axis ζ. Let x be an axis normal to both z and $\zeta$ ， $y$ the third axis of the x, $y , z$ set,and show that the angular velocities along $_ { x }$ ， $_ y$ ， $\boldsymbol { z }$ ,are;

$$
\begin{array} { r l } & { \omega _ { x } = \dot { \theta } \cos \varphi + \dot { \psi } \sin \theta \sin \varphi } \\ & { \omega _ { y } = - \dot { \theta } \sin \varphi \cos \alpha + \dot { \psi } \sin \theta \cos \varphi \cos \alpha + ( \dot { \varphi } + \dot { \psi } \cos \theta ) \sin \alpha } \\ & { \omega _ { z } = \dot { \theta } \sin \varphi \sin \alpha - \dot { \psi } \sin \theta \cos \varphi \sin \alpha + ( \dot { \varphi } + \dot { \psi } \cos \theta ) \cos \alpha } \end{array}
$$

Since the moments of inertia of the rotor are A, A, C,the angular momentum along x, y, z are; $h _ { x } = A \omega _ { x }$ ， $h _ { y } = A \omega _ { y } ,$ $h _ { z } = C \omega _ { z }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/13647c97093bccc3aad983c9967adaf386f5d9a04a3169ffb03fa83b870ee7e5.jpg)  
Prob. I1

12. Resolve theangular momentum $h _ { x }$ $h _ { y } ,$ $h _ { z }$ of Prob.11alongthe gyrogimbal axes 5, Z, and $5$ assuming $\propto$ to be small (see Fig. 6.2-1).

# 6.3 Gimbal Masses Included (Perturbation Technique)

Referring to Fig. 6.2-1,the moment of inertia of the rotor about the $\xi$ ， n, $\zeta$ axes were $A$ ， $A$ ， $C$ . In addition, we introduce the moment of inertia of the gimbals as follows. The moment of inertia of the inner gimbal about the $\xi$ $\eta$ $\zeta$ axes are $A _ { i }$ $B _ { i } ,$ $C _ { i }$ respectively. The moment of inertia of the outer gimbal about the $O Z$ axis is $C _ { 0 }$

Noting that the $\xi$ ， $\gamma _ { j }$ ， $\zeta$ ， axes rotate with angular speeds $\dot { \theta }$ ， $\dot { \psi }$ sin $\theta$ $\dot { \psi }$ cos $\theta$ , and noting the masses which rotate due to these components, the moment of inertia about the three axes are,

$$
\begin{array} { l } { { I _ { \xi } = A + A _ { i } } } \\ { { \ } } \\ { { I _ { \eta } = A + B _ { i } } } \\ { { \ } } \\ { { I _ { \zeta } = C _ { i } } } \end{array}
$$

The direction cosines of the $O Z$ axis with respect to $\xi$ ， $\gamma _ { j }$ ， $\zeta$ ,are $l _ { Z _ { 5 } ^ { \xi } } = 0$ lzn = sin 0,Izg =cos0, so that the momentof inertia about theZ axis becomes,

$$
\begin{array} { c } { { I _ { Z } = C _ { 0 } + I _ { \xi } { l _ { Z \xi } } ^ { 2 } + I _ { \eta } { l _ { Z \eta } } ^ { 2 } + I _ { \zeta } { l _ { Z \zeta } } ^ { 2 } } } \\ { { \ = C _ { 0 } + ( A + B _ { i } ) \sin ^ { 2 } \theta + C _ { i } \cos ^ { 2 } \theta } } \end{array}
$$

We next determine the angular momenta about the $\xi , \eta , \zeta$ axes, which are,

$$
\begin{array} { r l } & { { \boldsymbol h } _ { \xi } = ( { \boldsymbol A } + { \boldsymbol A } _ { i } ) { \dot { \boldsymbol \theta } } } \\ & { { \boldsymbol h } _ { \eta } = ( { \boldsymbol A } + { \boldsymbol B } _ { i } ) \dot { \psi } \sin { \boldsymbol \theta } } \\ & { { \boldsymbol h } _ { \zeta } = C ( \dot { \varphi } + \dot { \psi } \cos { \boldsymbol \theta } ) + C _ { i } \dot { \psi } \cos { \boldsymbol \theta } } \end{array}
$$

The moment about the $\zeta$ axis can be separated into two parts, thus:

$$
\begin{array} { r l r } {  { M _ { \zeta } = h _ { \zeta } - h _ { \xi } \dot { \psi } \sin \theta + h _ { \eta } \dot { \theta } } } \\ & { } & { = C \frac { d } { d t } ( \dot { \varphi } + \dot { \psi } \cos \theta ) + [ C _ { i } \frac { d } { d t } ( \dot { \psi } \cos \theta ) + ( B _ { i } - A _ { i } ) \dot { \theta } \dot { \psi } \sin \theta ] } \\ & { } & { = { M _ { \zeta } } ^ { \prime } + { M _ { \zeta } } ^ { \prime } \ ~ ( 6 . 3 } \end{array}
$$

where $M _ { \zeta } ^ { \prime } = C ( d / d t ) ( \dot { \varphi } + \dot { \psi } \cos \theta )$ is the moment on the rotor axis, and $M _ { \zeta } { ' }$ is the moment due to the forces exerted on the inner gimbal axis by

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/3b80936996b149f98cce2d5d1dd266cb61d0d80fe3f1654da805ed0e82bb6799.jpg)  
Fig. 6.3-l. Moments on inner gimbal and rotor.

the outer gimbal,as shown in Fig.6.3-1. We will assume $M _ { \zeta } { ' }$ to be zero, in which case the rotor angular momentum will be a constant.

$$
C ( \dot { \varphi } + \dot { \psi } \cos \theta ) = C n = \mathtt { c o n s t a n t }
$$

The angular momentum components along $\xi$ ， $\eta$ ， $\zeta$ , shown in Fig. 6.3-2, can be resolved along the $\xi ^ { \prime }$ ， $\eta ^ { \prime }$ ， $\zeta ^ { \prime }$ axes by noting the vertical and horizontal components of $h _ { \eta }$ and $h _ { \zeta }$ The $h _ { \xi }$ and $h _ { \eta ^ { \prime } }$ components now rotate about the $O Z$ axis with angular speed $\dot { \psi }$ ,as shown in Fig.6.3-2. The components of $\mathbf { h }$ along the $\xi ^ { \prime }$ ， $\eta ^ { \prime }$ ， $\zeta ^ { \prime }$ axes are,

$$
\begin{array} { r l } & { h _ { \xi ^ { \prime } } = ( A + A _ { i } ) \dot { \theta } } \\ & { h _ { \eta ^ { \prime } } = h _ { \eta } \cos \theta - h _ { \zeta } \sin \theta = ( A + B _ { i } ) \dot { \psi } \sin \theta \cos \theta } \\ & { \qquad \quad - ( C n + C _ { i } \dot { \psi } \cos \theta ) \sin \theta } \\ & { h _ { \zeta ^ { \prime } } = h _ { \eta } \sin \theta + h _ { \zeta } \cos \theta + C _ { 0 } \dot { \psi } = ( A + B _ { i } ) \dot { \psi } \sin ^ { 2 } \theta } \\ & { \qquad \quad + ( C n + C _ { i } \dot { \psi } \cos \theta ) \cos \theta + C _ { 0 } \dot { \psi } } \end{array}
$$

We can now write the moment equations about the &' and §' axes as follows:

$$
\begin{array} { r l r } { M _ { \mathcal { T } } = M _ { z } = \dot { h } _ { \mathcal { T } } = ( A + \delta _ { i } ) ( \dot { \nabla } \sin ^ { 2 } \theta + 2 \dot { \psi } ^ { j } \sin \theta \cos \theta ) } & { } & \\ { - ( c n + C _ { i } + C _ { i } \cos \phi ) \dot { \theta } \sin \theta } & { } & \\ { + ( c _ { i } \dot { \nabla } \cos \theta - C _ { i } \dot { \psi } \sin \theta ) \cos \theta + C _ { 0 } \ddot { \psi } } & { } & \\ { = [ C _ { 0 } + C _ { i } \cos ^ { 2 } \theta + ( A + \delta _ { i } ) \dot { \psi } \sin ^ { 2 } \theta ] \ddot { \psi } } & { } & \\ { + 2 ( 4 + B _ { i } - C ) \dot { \psi } \dot { \theta } \sin \theta \cos \theta - C n \dot { \psi } \sin \theta } & { } & \\ { = I _ { \mathcal { T } } \dot { \psi } + \dot { \psi } \frac { d I _ { \mathcal { T } } } { d t } - C n \dot { \theta } \sin \theta } & { } & \\ { = \frac { d } { d t } ( I _ { \mathcal { T } } \dot { \psi } ) - C n \dot { \theta } \sin \theta } & { } & { ( 6 , } \\ { M _ { \mathcal { F } } = \dot { h } _ { \mathcal { F } } - N _ { \phi } \dot { \psi } } & { } & \\ { = ( A + A _ { i } \dot { \psi } ) \dot { \psi } + C n \dot { \psi } \sin \theta } & { } & \\ { + ( C _ { i } - ( A + B _ { i } ) \dot { \psi } ^ { 2 } \sin \theta \cos \theta = 0 ) } & { } & { ( 6 . } \end{array}
$$

We next investigate the problem for which the axes are initially at rest, and the inner gimbal axis in position $\theta _ { 0 }$ is given an initial angular velocity

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/e66fbeee2e1febef825c9b875851ce81113e30ea07b518b4c0941e469cee0428.jpg)  
Fig. 6.3-2. Resolution of angular velocity and angular momentum.

$\dot { \theta } ( 0 ) = \alpha$ ,by an impulsive moment in the form of a delta function about the $\xi$ axis. The time $t = 0$ is referenced to the instant aftei the impulse, in which case $M _ { \xi } = M _ { Z } = 0$ ，and the initial conditions are $\psi ( 0 ) = 0$ ， γ(0) = 0,0(O) = 0, 0(O) = α. We can safely assume that γ(O) = 0, since the initial velocity α results in a gyroscopic moment about the Z axis (through reaction of $\xi$ bearings) which is not impulsive.

With the outer gimbal axis unrestrained, $M _ { Z } = 0$ , and Eq. 6.3-11 can be written as,

$$
d ( I _ { Z } \dot { \psi } ) = C n \sin \theta d \theta
$$

Integrating and noting that $I _ { Z } \dot { \psi }$ at $t = 0$ is zero, we obtain the equation,

$$
I _ { z } \dot { \psi } = - C n ( \cos \theta - \cos \theta _ { 0 } )
$$

We now make the small oscillation approximation,

$$
\begin{array} { c } { { \theta = \theta _ { 0 } + \theta _ { \sim } } } \\ { { \sin \theta \cong \sin \theta _ { 0 } + \theta _ { \sim } \cos \theta _ { 0 } } } \\ { { \cos \theta \cong \cos \theta _ { 0 } - \theta _ { \sim } \sin \theta _ { 0 } } } \\ { { \sin \theta \cos \theta \cong \sin \theta _ { 0 } \cos \theta _ { 0 } + \theta _ { \sim } ( \cos ^ { 2 } \theta _ { 0 } - \sin ^ { 2 } \theta _ { 0 } ) } } \end{array}
$$

and rewrite Eqs. 6.3-2, 6.3-14, and 6.3-12 as Eqs. 6.3-15, 6.3-16, and 6.3-17

$$
\begin{array} { c } { { I _ { Z } = [ C _ { 0 } + ( A + B _ { i } ) \sin ^ { 2 } \theta _ { 0 } + C _ { i } \cos ^ { 2 } \theta _ { 0 } ] } } \\ { { + 2 \theta _ { \sim } ( A + B _ { i } - C _ { i } ) \sin \theta _ { 0 } \cos \theta _ { 0 } } } \\ { { = I _ { 0 } + 2 \theta _ { \sim } ( A + B _ { i } - C _ { i } ) \sin \theta _ { 0 } \cos \theta _ { 0 } } } \end{array}
$$

$I _ { 0 } \dot { \psi } - ( C n \sin \theta _ { 0 } ) \theta _ { \sim } + 2 \theta _ { \sim } \dot { \psi } ( A + B _ { i } - C _ { i } )$ sin $\theta _ { 0 }$ cos $\theta _ { 0 } = 0$

$$
\begin{array} { r l r } {  { ( A + A _ { i } ) \ddot { \theta } _ { \sim } + ( C n \sin \theta _ { 0 } ) \dot { \psi } } } \\ & { } & { + \{ ( C n \cos \theta _ { 0 } ) \theta _ { \sim } \dot { \psi } - ( A + B _ { i } - C _ { i } ) [ \sin \theta _ { 0 } \cos \theta _ { 0 } } \\ & { } & { + \theta _ { \sim } ( \cos ^ { 2 } \theta _ { 0 } - \sin ^ { 2 } \theta _ { 0 } ) ] \dot { \psi } ^ { 2 } \} = 0 , \quad \quad ( 6 } \end{array}
$$

Equations 6.3-16 and 6.3-17 are nonlinear due to the last term in each equation. They can be solved by the perturbation technique $\cdot ^ { 1 , 3 , 8 }$ which will be illustrated by the following simple example. Consider a firstorder nonlinear equation

$$
\dot { y } + a y + b y ^ { 2 } = 0
$$

where the coefficient $b$ of the nonlinear term is a small quantity.We will now consider a similar equation

$$
\dot { y } + a y + \mu b y ^ { 2 } = 0
$$

which differs from the previous equation by an additional factor $\mu$ which may be any positive number. If the solution of Eq. $b$ is found, then the solution of the previous equation, Eq. $a$ , is found by leting $\mu = 1$

We seek now a solution in the form,

$$
y = y _ { 0 } + \mu y _ { 1 } + \mu ^ { 2 } y _ { 2 } + \cdot \cdot \cdot
$$

Substituting $c$ into $^ { b }$ we obtain,

$$
\begin{array} { c } { { ( \dot { y } _ { 0 } + \mu \dot { y } _ { 1 } + \mu ^ { 2 } \dot { y } _ { 2 } + \dot { \mathrm {  ~ \cdot ~ } } \dot { \cdot } \dot { \mathrm {  ~ \cdot ~ } } ) + a ( y _ { 0 } + \mu y _ { 1 } + \mu ^ { 2 } y _ { 2 } + \dot { \mathrm {  ~ \cdot ~ } } \dot { \mathrm {  ~ \cdot ~ } } ) } } \\ { { + \ \mu b ( y _ { 0 } + \mu y _ { 1 } + \mu ^ { 2 } y _ { 2 } + \dot { \mathrm {  ~ \cdot ~ } } \dot { \mathrm {  ~ \cdot ~ } } \dot { \mathrm {  ~ \cdot ~ } } ) ^ { 2 } = 0 } } \end{array}
$$

Rearanging,this equation can be writen in terms ofequal powers of $\mu$ as follows:

$$
\begin{array} { c } { { ( \dot { y } _ { 0 } + a y _ { 0 } ) + \mu ( \dot { y } _ { 1 } + a y _ { 1 } + b { y _ { 0 } } ^ { 2 } ) + \mu ^ { 2 } ( \dot { y } _ { 2 } + a y _ { 2 } + 2 b y _ { 0 } y _ { 1 } ) } } \\ { { \mathrm { } } } \\ { { + \mu ^ { 3 } ( \dot { y } _ { 3 } + \dot { \mathrm {  ~ \cdot ~ } } \dot { \mathrm {  ~ \cdot ~ } } { } ) = 0 } } \end{array}
$$

We note now that, if $\mu = 0$ ,we obtain $y _ { 0 }$ as the solution of the linear equation. The solution $y _ { 0 }$ is called the generating solution,and it can be fited to the initial conditions of the problem. If $\mu$ is allowed to increase from zero, Eq. $e$ can be satisfied only if the coefficients of $\mu$ raised to the various powers are zero. We thus obtain the following equations,

$$
{ \dot { y } } _ { 1 } + a y _ { 1 } + b y _ { 0 } { } ^ { 2 } = 0
$$

$$
{ \dot { y } } _ { 2 } + a y _ { 2 } + 2 b y _ { 0 } y _ { 1 } = 0 , { \mathrm { e t c } } .
$$

which can be solved for $y _ { 1 } , y _ { 2 } ,$ etc.

We will now apply this technique to Eqs. 6.3-16 and 6.3-17, but will carry out the solution only to the first-order correction. Since Eq. 6.3-16 and 6.3-17 already have the symbol $\theta _ { 0 }$ ,we will let the solution to the linear equation (corresponding to $y _ { 0 }$ ）be $\theta _ { 0 0 }$ and $\dot { \psi } _ { 0 0 }$ . The linear equations are then,

$$
\begin{array} { r } { I _ { 0 } \dot { \psi } _ { 0 0 } - ( C n \sin \theta _ { 0 } ) \theta _ { 0 0 } = 0 } \\ { ( A + A _ { i } ) \ddot { \theta } _ { 0 0 } + ( C n \sin \theta _ { 0 } ) \dot { \psi } _ { 0 0 } = 0 } \end{array}
$$

Eliminating $\dot { \psi } _ { 0 0 }$ ,we obtain the equation

$$
\ddot { \theta } _ { 0 0 } + \frac { ( C n \sin \theta _ { 0 } ) ^ { 2 } } { I _ { 0 } ( A + A _ { i } ) } \theta _ { 0 0 } = 0
$$

Letting

$$
\omega = \frac { C n \sin \theta _ { 0 } } { \sqrt { I _ { 0 } ( A + A _ { i } ) } }
$$

the generating solution fitting the initial conditions is,

$$
\begin{array} { l } { { \theta _ { 0 0 } = \displaystyle \frac { \dot { \theta } ( 0 ) } { \omega } \sin \omega t } } \\ { { \dot { \psi } _ { 0 0 } = \displaystyle \frac { C n \sin \theta _ { 0 } } { I _ { 0 } } \biggl [ \frac { \dot { \theta } ( 0 ) } { \omega } \sin \omega t \biggr ] } } \end{array}
$$

We next consider the first-order correction corresponding to $y _ { 1 }$ in Eq.f. From the generating solution we determine the nonlinear terms

$$
\begin{array} { c } { { \theta _ { 0 0 } \dot { \psi } _ { 0 0 } = { \displaystyle \frac { \dot { \theta } ( 0 ) ^ { 2 } C n \sin \theta _ { 0 } } { \omega ^ { 2 } I _ { 0 } } } \sin ^ { 2 } \omega t } } \\ { { { } } } \\ { { \dot { \psi } _ { 0 0 } { } ^ { 2 } = { \displaystyle \left( \frac { C n \sin \theta _ { 0 } } { I _ { 0 } } \right) ^ { 2 } } \left( \frac { \dot { \theta } ( 0 ) } { \omega } \right) ^ { 2 } \sin ^ { 2 } \omega t } } \end{array}
$$

which， substituted into Eqs. 6.3-16 and 6.3-17, results in a new set of differential equations,

$$
\begin{array} { l } { { I _ { 0 } \dot { \psi } _ { 1 } - ( C n \sin \theta _ { 0 } ) \theta _ { 1 } } } \\ { { \ = - \frac { 2 ( A + B _ { i } - C _ { i } ) \sin ^ { 2 } \theta _ { 0 } \cos \theta _ { 0 } } { I _ { 0 } } \frac { C n \dot { \theta } ( 0 ) ^ { 2 } } { \omega ^ { 2 } } \sin ^ { 2 } \omega t } } \end{array}
$$

$$
( A + A _ { i } ) \ddot { \theta } _ { 1 } + ( C n \sin \theta _ { 0 } ) \dot { \psi } _ { 1 } = - ( C n \cos \theta _ { 0 } ) \frac { \dot { \theta } ( 0 ) ^ { 2 } } { \omega ^ { 2 } } \frac { C n \sin \theta _ { 0 } } { I _ { 0 } } \sin ^ { 2 } \omega t
$$

$$
+ \left( A + B _ { i } - C _ { i } \right) \sin \theta _ { 0 } \cos \theta _ { 0 } \bigg ( \frac { \dot { \theta } ( 0 ) C n \sin \theta _ { 0 } } { \omega I _ { 0 } } \bigg ) ^ { 2 } \sin ^ { 2 } \omega t
$$

We will now eliminate $\theta _ { 1 }$ . From Eq. 6.3-16b we obtain

$$
\begin{array} { r l r } {  { \widetilde { \theta } _ { 1 } = ( \frac { I _ { 0 } } { C n \sin \theta _ { 0 } } ) \dddot { \psi } _ { 1 } } } \\ & { } & { + [ \frac { 4 \dot { \theta } ( 0 ) ^ { 2 } ( A + B _ { i } - C _ { i } ) \cos \theta _ { 0 } \sin \theta _ { 0 } } { I _ { 0 } } ] ( \cos ^ { 2 } \omega t - \sin ^ { 2 } \omega t ) \ } \end{array}
$$

Substituting into Eq. 6.3-17b, we obtain the diferential equation for $\psi _ { 1 }$

$$
\begin{array} { r l } {  { \sum _ { C n \sin \theta _ { 0 } } \biggl [ \frac { I _ { 0 } ( A + A _ { i } ) } { C n \sin \theta _ { 0 } } \biggl ] \ddot { \psi } _ { 1 } + ( C n \sin \theta _ { 0 } ) \dot { \psi } _ { 1 } = [ \frac { \dot { \theta } ( 0 ) C n } { \omega } ] ^ { 2 } } } \\ & { \times [ \frac { ( A + B _ { i } - C _ { i } ) \sin ^ { 3 } \theta _ { 0 } \cos \theta _ { 0 } } { I _ { 0 } ^ { 2 } } - \frac { \sin \theta _ { 0 } \cos \theta _ { 0 } } { I _ { 0 } } ] \frac { 1 } { 2 } ( 1 - \cos 2 } \\ & { - \frac { A + A _ { i } } { I _ { 0 } } [ 4 \dot { \theta } ( 0 ) ^ { 2 } ( A + B _ { i } - C _ { i } ) \sin \theta _ { 0 } \cos \theta _ { 0 } ] \cos 2 \omega t \quad ( 6 . 3 - 7 ) } \end{array}
$$

In examining this equation,the solutionof the homogeneous equation for $\dot { \psi } _ { 1 }$ is again harmonic of frequency $\omega$ as given by Eq. 6.3-19. The particular solution will have harmonic terms of frequency $_ { 2 \omega }$ and, in addition, a constant term equal to the constant term on the right side of the equation divided by thecoefficint of $\dot { \psi } _ { 1 }$ On the left side. We are interested in the constant term since it results in a steady drift which rotates the outer gimbal according to the equation y = 𝜑t.

The constant term of the solution is

$$
\dot { \psi } _ { s } = - \frac { \dot { \theta } ( 0 ) ^ { 2 } C n } { 2 \omega ^ { 2 } I _ { 0 } ^ { ~ 2 } \sin \theta _ { 0 } } \left[ \left( A + B _ { i } - C _ { i } \right) \sin ^ { 3 } \theta _ { 0 } \cos \theta _ { 0 } - I _ { 0 } \sin \theta _ { 0 } \cos \theta _ { 0 } \right]
$$

Substituting for $I _ { 0 }$ from Eq. 6.3-15, it reduces to

$$
\dot { \psi } _ { s } = - \frac { \dot { \theta } ( 0 ) ^ { 2 } C n ( C _ { 0 } + C _ { i } ) \cos \theta _ { 0 } } { 2 \omega ^ { 2 } { I _ { 0 } } ^ { 2 } }
$$

It is evident, then, that the outer gimbal oscillates and drifts in a negative direction, a phenomenon referred to as “gimbal walk."6 It should be noted that gimbal walk cannot take place at $\theta _ { 0 } = 9 0 ^ { \circ }$ or if the moment of inertia $C _ { 0 } + C _ { i } )$ is zero.

# PROBLEMS

1. The periodic solution for Eq. 6.3-17c is

$$
\dot { \psi } _ { 1 } = \alpha + \beta \cos { 2 \omega t }
$$

Evaluate the coefficient $\beta$ ·

2. Discuss the solution of a nonhomogeneous equation,

$$
{ \dot { y } } + a y + b y ^ { n } = f ( t )
$$

by the procedure of Sec. 6.3.

3. Solve the nonlinear differential equation,

$$
m { \ddot { y } } + k y - b y ^ { 3 } = F \sin p t
$$

by the perturbation method outlined in Sec. 6.3. The solution with the use of only two terms, $y = y _ { 0 } + \mu y _ { 1 } ,$ is

$$
y _ { \mathrm { \ell } } = \left[ a + \frac { 3 b \alpha ^ { 3 } } { 4 m ( \omega ^ { 2 } - \boldsymbol { p } ^ { 2 } ) } \right] \sin \boldsymbol { p } t - \frac { b \alpha ^ { 3 } } { 4 m ( \omega ^ { 2 } - 9 \boldsymbol { p } ^ { 2 } ) } \sin 3 \boldsymbol { p } t
$$

where

$$
a = { \frac { F } { m ( \omega ^ { 2 } - p ^ { 2 } ) } } \qquad { \mathrm { a n d } } \qquad \omega ^ { 2 } = { \frac { k } { m } } 
$$

4. Show that if only the first term $y = a$ sin $p t$ of Prob. 3 is substituted into the differential equation,the amplitude relationship

$$
{ \frac { 3 b } { 4 m \omega ^ { 2 } } } a ^ { 3 } = \left( 1 \ - { \frac { p ^ { 2 } } { \omega ^ { 2 } } } \right) a - { \frac { F } { m \omega ^ { 2 } } }
$$

is obtained. Letting the ordinate $v = ( 3 b / 4 m \omega ^ { 2 } ) a ^ { 3 }$ be plotted against a, discuss the solution for the amplitude $\boldsymbol { \alpha }$ versus $p / \omega$ ,where $\omega ^ { 2 } = k / m$

5. For the problem of Sec. 6.3, investigate the equation for $\theta$ and establish whether there is a unidirectional motion about the node axis.

# 6.4 The Gyrocompass

The requirement of a gyrocompass is to point north at any latitude at any time. The high-speed, two-gimballed gyro, with a pendulous weight $w$ on the $\eta$ axis to give it moment $w l$ cos $\theta$ about the $\xi$ axis when the axis istiltedabovethehorizonasshowninFig.6.4-1willsatisfythisquire ment.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/88f37f974d759f9f605073f12aad71472dd110885a9c29821264da8394408ced.jpg)  
Fig. 6.4-l. Gyrocompass and angular velocity components.

In Fig.6.4-1,the rotation of the earth from west to east is indicated by the angular rotation vector $\Omega$ pointing in the northerly direction. Its numerical value is $\Omega = 2 \pi / ( 2 4 \times 3 6 0 0 ) = 7 . 2 7 \times 1 0 ^ { - 5 }$ rad/sec. At any latitude λ, $\Omega$ will have components in the meridian plane,equal toΩcosλ horizontally, and $\Omega$ sin λ vertically.

With the $Z$ axis of the gyrocompass in the local vertical direction, in order for the $\zeta$ axis to remain in the meridian plane, and hence point north,the outer gimbal must precess steadily by an amount γ = Ω sin λ and in addition have an angular velocity Ω cos λ about the -n axis perpendicular to the outer gimbal plane. We assume that the gyro is constrained to move in this manner, and investigate the moment requirement satisfying the motion.

Letting $\theta = 9 0 ^ { \circ } - \alpha _ { 0 }$ ，where $\alpha _ { 0 }$ is a small angle above the horizontal plane at latitude $\lambda$ the angular velocities of the $\xi$ ， $\eta _ { i }$ $\zeta$ axes are,

$$
\begin{array} { r l } & { \omega _ { \xi } = 0 } \\ & { \omega _ { \eta } = \Omega ( \sin \lambda \cos \alpha _ { 0 } - \cos \lambda \sin \alpha _ { 0 } ) } \\ & { \omega _ { \zeta } = \Omega ( \sin \lambda \sin \alpha _ { 0 } + \cos \lambda \cos \alpha _ { 0 } ) } \end{array}
$$

Assuming the spin to be very large, we can neglect all other components of $\mathbf { h }$ With $M _ { Z } = 0 , \ \dot { \varphi } = ($ constant. The required moment about the $\xi$ axis,is

$$
M _ { \xi } = ( C \dot { \varphi } ) \omega _ { \eta }
$$

$$
w l \sin \alpha _ { 0 } = C \dot { \varphi } \Omega ( \sin \lambda \cos \alpha _ { 0 } - \cos \lambda \sin \alpha _ { 0 } )
$$

Dividing by sin $\alpha _ { 0 }$ , the required inclination of the spin axis above the horizon is,

$$
\tan \alpha _ { 0 } = \frac { C \dot { \varphi } \Omega \sin \lambda } { w l + C \dot { \varphi } \Omega \cos \lambda }
$$

which depends on the latitude $\lambda$

The moment required for the angular velocity $\Omega$ cos λ about the - $\eta ^ { \prime }$ axis is supplied by the reaction of the bearings on the outer gimbal axis $Z$

# 6.5 Oscillation of the Gyrocompass

If the axis of the gyrocompass is disturbed from the meridian plane, as shown in Fig. 6.5-1, the oscillation which takes place will have two components, one perpendicular to the meridian plane and the other in the meridian plane. Both oscillations will have the same frequency，and so the end of the axis of the gyrocompass will describe an ellipse.

Letting $\psi$ be the angular deviation of the spin axis out of the meridian plane,and α its inclination above the horizontal, we will assume both these angles to be small, in which case the angular velocities about the $\xi$ ， $\gamma _ { j }$ ， $\zeta$ axes will be,

$$
\begin{array} { r l } & { \omega _ { \xi } = - \dot { \alpha } - \Omega \psi \cos \lambda } \\ & { \omega _ { \eta } = \dot { \psi } + \Omega \sin \lambda - \Omega \alpha \cos \lambda } \\ & { \omega _ { \zeta } = ( \dot { \psi } + \Omega \sin \lambda ) \alpha + \Omega \cos \lambda } \end{array}
$$

We will also assume the spin to be large and the angular momentum about the $\xi$ and $\eta$ axes to be negligible in comparison.

$$
\begin{array} { l } { { h _ { \zeta } = C \dot { \varphi } = \mathrm { c o n s t a n t ~ f o r ~ } M _ { \zeta } = 0 } } \\ { { h _ { \xi } = h _ { \eta } = 0 } } \end{array}
$$

The moment equations of interest are then,

$$
\begin{array} { r l } & { M _ { \eta } = - h _ { \zeta } \omega _ { \xi } = C \dot { \varphi } ( \dot { \alpha } + \Omega \psi \cos \lambda ) = 0 } \\ & { M _ { \xi } = h _ { \zeta } \omega _ { \eta } = C \dot { \varphi } ( \dot { \psi } + \Omega \sin \lambda - \Omega \alpha \cos \lambda ) = w l \alpha , } \end{array}
$$

where $w l$ is the mass unbalance of the pendulous weight on the $- \eta$ axis. Rearranging these equations, we have

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/fa9671b0e780dca0d1c9b3df9fae769774bfe91a492641fb03dde2d4e58f8670.jpg)  
Fig.6.5-l. Vector components for the gyrocompass.

Eliminating $\psi$ between these equations,the differential equation for $\propto$ becomes

$$
\ddot { \alpha } + \frac { ( w l + C \dot { \varphi } \Omega \cos \lambda ) ( \Omega \cos \lambda ) } { C \dot { \varphi } } \propto = \Omega ^ { 2 } \sin \lambda \cos \lambda
$$

with the general solution,

$$
\alpha = C _ { 1 } \sin p t + C _ { 2 } \cos p t + \frac { C \dot { \varphi } \Omega \sin \lambda } { w l + C \dot { \varphi } \Omega \cos \lambda }
$$

$$
p = \sqrt { \frac { w l \Omega \cos \lambda + C \dot { \varphi } \Omega ^ { 2 } \cos ^ { 2 } \lambda } { C \dot { \varphi } } } \cong \sqrt { \frac { w l \Omega \cos \lambda } { C \dot { \varphi } } }
$$

From Eq. 6.5-3, the equation for $\psi$ is,

$$
\psi = \frac { - p } { \Omega \cos \lambda } \left( C _ { 1 } \cos p t - C _ { 2 } \sin p t \right)
$$

These equations indicate that the spin axis oscillates horizontally about the meridian plane and vertically about the stationary angle $\alpha _ { 0 }$ given by Eq. 6.4-3. The frequency of oscillation, Eq. 6.5-6 is a function of the latitude l,and is very small due to $C \dot { \varphi }$ in the denominator. The frequency $p$ approaches zero,as the gyrocompass nears the north polar axis, where the reliability of the instrument diminishes.

# High-frequency oscillation

In addition to the slow oscillation given by the foregoing equations, there is a high-frequency oscillation which was not revealed because the angular momentum about $\xi$ and $\eta$ were assumed to be zero. By adding ${ \cal I } _ { \eta } \ddot { \psi }$ and $- I _ { \xi } \ddot { x }$ to Eqs. 6.5-2, we have,

$$
\begin{array} { l } { M _ { \eta } = C \dot { \varphi } ( \dot { \alpha } + \Omega \psi \cos \lambda ) + I _ { \eta } \ddot { \psi } = 0 } \\ { M _ { \xi } = C \dot { \varphi } ( \dot { \psi } + \Omega \sin \lambda - \Omega \alpha \cos \lambda ) - I _ { \xi } \ddot { \alpha } = w l \alpha } \end{array}
$$

Rearranging, and letting,

$$
\begin{array} { l } { { a = C \dot { \varphi } \Omega \cos \lambda } } \\ { { { } } } \\ { { b = w l + C \dot { \varphi } \Omega \cos \lambda } } \end{array}
$$

the above equations become,

$$
\begin{array} { c } { { \displaystyle { \ddot { \psi } + \frac { C \dot { \varphi } } { I _ { \eta } } \dot { \alpha } + \frac { a } { I _ { \eta } } \psi = 0 } } } \\ { { \displaystyle { \ddot { \alpha } - \frac { C \dot { \varphi } } { I _ { \xi } } \dot { \psi } + \frac { b } { I _ { \xi } } \propto \frac { C \dot { \varphi } \Omega \sin \lambda } { I _ { \xi } } } } } \end{array}
$$

Assuming harmonic oscillations, $e ^ { i p t }$ , the natural frequencies are given by the determinant,

$$
\left| \begin{array} { l l l } { - p ^ { 2 } + \frac { b } { I _ { \xi } } } & & { - \frac { C \dot { \varphi } } { I _ { \xi } } i p } \\ { \frac { C \dot { \varphi } } { I _ { \eta } } i p } & & { - p ^ { 2 } + \frac { a } { I _ { \eta } } } \end{array} \right| = 0
$$

or

$$
p ^ { 4 } - \biggl [ \frac { ( C \dot { \varphi } ) ^ { 2 } + a I _ { \xi } + b I _ { \eta } } { I _ { \xi } I _ { \eta } } \biggr ] p ^ { 2 } + \frac { a b } { I _ { \xi } I _ { \eta } } = 0
$$

Since $( C \dot { \varphi } ) ^ { 2 }$ is very much larger than $a I _ { \xi }$ or $b I _ { \eta }$ ， the natural frequency equation simplifies to

$$
p ^ { 2 } = \frac { ( C \dot { \varphi } ) ^ { 2 } } { 2 I _ { \xi } I _ { \eta } } \biggl [ 1 \pm \sqrt { 1 - \frac { 4 a b I _ { \xi } I _ { \eta } } { ( C \dot { \varphi } ) ^ { 4 } } } \biggr ] = \frac { ( C \dot { \varphi } ) ^ { 2 } } { 2 I _ { \xi } I _ { \eta } } \biggl \{ 1 \pm \biggl [ 1 - \frac { 2 a b I _ { \xi } I _ { \eta } } { ( C \dot { \varphi } ) ^ { 4 } } + \cdots \biggr ] \biggr \}
$$

The two frequencies are, therefore,

$$
{ p _ { 1 } } ^ { 2 } = \frac { a b } { ( C \dot { \varphi } ) ^ { 2 } } = \frac { ( w l + C \dot { \varphi } \Omega \cos \lambda ) \Omega \cos \lambda } { C \dot { \varphi } } \quad { p _ { 2 } } ^ { 2 } = \frac { ( C \dot { \varphi } ) ^ { 2 } } { I _ { \xi } I _ { \eta } }
$$

We find then that $p _ { 1 }$ corresponds to Eq. 6.5-6, and an additional highfrequency oscillation of frequency $p _ { 2 }$ is introduced. With $h _ { \xi } = h _ { \eta } = 0$ ， $p _ { 2 } = \infty$ did not enter into the previous solution. The amplitude of the high-frequency oscillation, however, is extremely small, and hence, the slow oscillation at frequency $p _ { 1 }$ is generally the only one detectable.

# Effect of damping

Damping for the slow oscilation of the gyrocompass can be provided by introducing a moment about the $\eta$ axis as follows. We move the pendulous weight $w$ a distance $e$ to the east cf the center line so that its coordinate ( $\xi$ ， $\eta$ ， $\zeta ) = ( - e , - l , 0 )$ . The equation for the moment about the axis is then modifiedas follows:

$$
M _ { \eta } = C \dot { \varphi } ( \dot { \alpha } + \Omega \psi \cos \lambda ) = - w e \alpha
$$

or,

$$
\dot { \alpha } = - \Omega \psi \cos \lambda - \frac { w e \alpha } { C \dot { \varphi } }
$$

Differentiating the equation for $M _ { \xi }$ (second of Eq. 6.5-8 without $I _ { \xi } \ddot { \alpha }$ term), and substituting for $\dot { \alpha }$ from above and $\propto$ from $M _ { \xi }$ ，we arrve at the following differential equation for $\psi$ ：

$$
\ddot { \psi } + \left( \frac { w e } { C \dot { \varphi } } \right) \dot { \psi } + \frac { ( w l + C \dot { \varphi } \Omega \cos \lambda ) \Omega \cos \lambda } { C \dot { \varphi } } \psi = - \frac { w e \Omega \sin \lambda } { C \dot { \varphi } }
$$

The effect of the offset e is then to damp the γ oscillations and shift the equilibrium position totheeast bythe angle,

$$
\psi _ { 0 } = - \frac { w e \tan \lambda } { w l + C \dot { \varphi } \Omega \cos \lambda }
$$

Compass heading error due to vehicle motion

When a vehiclecarrying a gyrocompassmoves ina northerly direction along a meridian with velocity $v$ ,an angular velocity $v / R$ pointing west,

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/92d4ba3de160dfaff9dfbe9e0a7d2092627c77ab9f02273d788fccad5ef09cf9.jpg)  
Fig. 6.5-2. Angular velocities in horizontal plane due to vehicle motion $v$

where $R$ is the radius of the earth, is introduced. By combining this vector with the horizontal component of the earth's rotation $\Omega$ cos 𝜆, the resultant angular velocity in the horizontal plane deviates to the west by an angle

$$
\gamma \cong \frac { v / R } { \Omega \cos \lambda }
$$

and the gyrocompass will now point in the direction of the resultant, introducing a heading error of $\gamma$

If the vehicle is traveling in a direction making an angle $\theta$ with the meridian plane, $v$ can be replaced by $v$ cos $\theta$ to give,

$$
\gamma \cong { \frac { v \cos \theta } { R \Omega \cos \lambda + v \sin \theta } }
$$

where the effect of the component $v$ sin $\theta$ is neglected due to the fact that it is small in comparison to $\Omega$ cos $\lambda$

# PROBLEMS

1. Resolveh = C along the vertical and horizontal directions,so that we have the vector diagram shown. Derive Eq. 6.4-3 from this configuration.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/d40c16c4d5329539c32cb2508383aaed89db7de707d6a4848605f3aea6251825.jpg)  
Prob. I

2. Determine the reactions on theouter gimbal bearings $\xi$ for the gyrocompass of Sec. 6.4 (see Fig. 6.4-1).

3. If the gyrocompass axis $\xi$ is clamped at the angle $\alpha _ { 0 }$ show that the frequency of oscillation becomes,

$$
p _ { 3 } = { \sqrt { \frac { C \dot { \varphi } \Omega \cos \lambda } { I _ { \eta } } } }
$$

4. The following data are given for a gyrocompass.

$$
\begin{array} { l } { C = 3 . 0 \ \mathrm { i n . \ 1 b \ s e c ^ { 2 } } } \\ { A = 1 . 8 0 \ \mathrm { i n . \ 1 b \ s e c ^ { 2 } } } \\ { \dot { \varphi } = 1 0 0 0 \ \mathrm { r a d / s e c } } \\ { w l = 7 5 \ \mathrm { l b \ i n } . } \end{array}
$$

Determine $p _ { 1 } , p _ { 2 } ,$ and $\alpha _ { 0 }$ for any latitude λ.

5. Determine the gyrocompass heading error for a ship traveling at a constant speed of 15 knots in a direction N $2 0 ^ { \circ } \mathrm { E }$ at latitude $\bar { 4 } 8 ^ { \circ } \mathbf { N }$ Would the heading error be different if the ships direction were $\mathrm { ~ N ~ } 2 0 ^ { \circ } \mathrm { ~ W ~ } ^ { \prime }$ 2

6. Derive the equation for the heading error of a gyrocompass,taking into account the latitude component v sin $\theta$ of the carrier vehicle.

7. A gyropendulum is a spherical pendulum with a spinning disk with angular momentum $C n$ along its pendulum length $l _ { i }$ as showninthesketching $A$ be the moment of inertia through $o$ perpendicular to l, show that the moment equations for small angles are,

$$
\begin{array} { l } { { C n { \dot { \varphi } } + A { \ddot { \theta } } = - W l { \theta } } } \\ { { C n { \dot { \theta } } - A { \ddot { \varphi } } = W l { \varphi } } } \end{array}
$$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/9ba66268fcbb9cd003ead9c7cdf6b38608489bae9332ea33afe039f1a2d9f734.jpg)  
Prob.7

8. Showthatthe gyropendulum of Prob.7 has naturalfrequencies given by the equation,

$$
p _ { 1 , 2 } ^ { 2 } = \frac { ( C ^ { 2 } n ^ { 2 } + 2 A W l ) \pm C n \sqrt { C ^ { 2 } n ^ { 2 } + 4 A W l } } { 2 A ^ { 2 } }
$$

Approximate equations for the lower and higher natural frequencies, neglecting the term $A W l / C ^ { 2 } n ^ { 2 } ,$ are,

$$
p _ { 1 } = { \frac { W l } { C n } } \qquad { \mathrm { a n d } } \qquad p _ { 2 } = { \frac { C n } { A } }
$$

9. The gyropendulum of Prob. 7 is mounted on a vehicle traveling in the $_ x$ direction (a great circle) with velocity $v$ ，Show that the pendulum must tilt through a small angle $\varphi$ about the $_ x$ axis according to the equation,

$$
\varphi = { \frac { C n v } { W l R } }
$$

where $R$ is the radius of earth.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/2f9f3107531ee4a61d0d8d6cb5afc1563c05ef8ffd82979f99ab589d0d3ca8ce.jpg)  
Prob.9

10.If the vehicle of Prob. 9 accelerates along the $_ x$ axis so that $d v / d t = a _ { x } ,$ show that

$$
{ \frac { d \varphi } { d t } } = { \frac { C n a _ { x } } { W l R } } \qquad { \mathrm { a n d } } \qquad { \frac { C n } { W l } } = { \sqrt { \frac { R } { g } } }
$$

The lower natural period of the pendulum, according to Prob. 8, now becomes,

$$
\tau _ { 1 } = 2 \pi \frac { C n } { W l } = 2 \pi \sqrt { \frac { R } { g } } = 8 4 . 4 \mathrm { m i n }
$$

which is called the Schuler period, after Max Schuler of Germany， who extensively studied the problem.

# 6.6 The Rate Gyro

High-speed gyros serve as basic elements in many instruments for guidance and control of moving vehicles. Figure 6.6-1 shows the essential elements of a rate gyro. The inner gimbal supporting the spinning wheel is restrained by a spring which permits a limited rotation about the outer gimbal which is fixed in the vehicle.The $Z$ axis about which the vehicle turnsiscalledtheinputaisandtheaisofotationoftheinneiis called the output axis.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/e8d029edccea651a5bd442676f99f0ca1caa13ce0c4f11ab4a551bda9bed4f40.jpg)  
Fig. 6.6-1. Rate gyro.

If the vehicle makes a steady turn about-the input axis at a rate \$, the rate of change of the angular momentum vector $C n$ is $C n { \dot { \psi } }$ ,which requires a moment equal to it about the output axis. This moment is supplied by the torsional spring of stiffness K, as the output axis tilts by a small angle θ, as shown in Fig. 6.6-1. Equating the two moments,we have,

or

$$
C n { \dot { \psi } } = K { \dot { \theta } }
$$

$$
\theta = { \frac { C n } { K } } { \dot { \psi } }
$$

and the output angle θ is proportional to the rate of turn φ of the input axis or the vehicle itself.

The output angle $\theta$ is in general read electrically by a pickoff device. One such deviceis the E-pickoff shown in Fig.6.6-2.The middle leg of the E is supplied by an alternating current, generally of $4 0 0 \ \mathrm { c p s }$ .The two outer legs of the E are wound in opposition, so that when the armature, attached to the output axis, is centered about the middle leg, no voltage appears across the opposed outer coils connected in series. When the armature is displaced due to $\theta$ ， the magnetic flux path is unbalanced, resulting in a voltage reading in the outer coils.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/6090b5d8f0fce30c82ca0b53f765064355b00478041c896deb4cf141377a1272.jpg)  
Fig. 6.6-2. E-pickoff on shaft.

In the undamped instrument, the output axis will overshoot the steady angle $\theta$ and oscillate about it. To prevent this undesirable condition, damping is generally provided,and its behavior can be established from the following differential equation,

$$
A { \ddot { \theta } } + c { \dot { \theta } } + K \theta = C n { \dot { \psi } }
$$

where $A$ is the moment of inertia of the wheel and inner gimbal about the output axis, and $c$ the coefficient of viscous damping. Thus the transient

characteristics of the instrument can be obtained from the homogeneous equation,

$$
\Ddot { \theta } + 2 \zeta \omega \Dot { \theta } + \omega ^ { 2 } \Dot { \theta } = 0
$$

where

$$
\begin{array} { c } { \omega = \displaystyle \sqrt { \frac { K } { A } } = \mathrm { u n d a m p e d ~ n a t u r a l ~ f r e q u e n c y } } \\ { \zeta = \displaystyle \frac { c } { c _ { \mathrm { e r } } } = \mathrm { d a m p i n g ~ f a c t o r } } \\ { c _ { \mathrm { e r } } = 2 \sqrt { K A } = \mathrm { c r i t i c a l ~ d a m p i n g } } \end{array}
$$

# 6.7 The Integrating Gyros

If the torsional spring restraining the output is replaced by a viscous damper, the instrument becomes an integrating gyro. Equating the rate of change of angular momentum to the viscous damping torque,

$$
C n { \dot { \psi } } = c { \dot { \theta } }
$$

or

$$
\theta = { \frac { C n } { c } } \int \dot { \psi } d t = { \frac { C n } { c } } \psi
$$

Thus the output angle $\theta$ is proportional to the integral of the input angular rate which is the input angle itself.

# 6.8 The Stable Platform

The principal function of the stable platform is to maintain a spacefixed angular reference. It is an essential part of an inertial guidance system. The platform makes use of the property of the gyroscope, that a torque about an input axis (excluding the spin axis) produces an angular velocity about the orthogonal (output) axis. In general, three single-degree-offreedom gyros oriented in mutually perpendicular directions are mounted on the platform, as shown in Fig. 6.8-1. The platform,in turn, is mounted on two gimbals which allow it three degrees of angular freedom. If the platform is perfectly balanced and the bearings are frictionless,no torque will be experienced by the platform,and its orientation will be maintained regardless of the motion of the carrier. However, due to unbalance and friction which cannot be eliminated entirely,disturbing torques will be felt by the platform. It is the function of the gyros to sense this disturbance and, through a servo system, counteract the disturbing torque to produce essentially a torque-free system.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/e38b77ca0def2f6bc3051ef6680cc274378567c862ccd4de53d6c1f2148832bd.jpg)  
Fig. 6.8-l. Stable platform for inertial guidance.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/bfcee6475f965f108eaccca096c04146d8952e0daf9284fdd6e904922f122387.jpg)  
Fig. 6.8-2. Single-axis platform to maintain angular orientation about y axis.

The understanding of the dynamics of the stable platform can be obtained by a discussion of the single-axis platform shown in Fig. 6.8-2,4 where the y axis is the input axis and the $x$ axis (rotation of the spin axis) is the output axis. A disturbing torque $T _ { y }$ about the $y$ axis will rotate the spin axis, and, therefore, h through the angle $\theta$ , and the applied torque minus the inertia torque about the $y$ axis must equal the rate of change of the angular momentum h according to the equation,

$$
T _ { y } - J _ { y } \ddot { \phi } _ { y } = h \dot { \theta }
$$

where $J _ { y }$ is the moment of inertia of the platform, and the gyro with its frame about the $y$ axis. In the above equation, small angle approximation is used for the right side which is justified since $\theta$ is seldom allowed to become greater than $1 ^ { \circ }$

The precession $\dot { \theta }$ which is developed by $T _ { y }$ results also in a torque equation about the $_ x$ axis as follows:

$$
- ~ T _ { x } = I _ { x } { \ddot { \theta } } - h { \dot { \phi } } _ { y } = 0
$$

where $I _ { x }$ is the moment of inertia of the gyro and its frame about the $x$ axis.

Using the Laplace transform notation ${ \mathcal { L } } \theta = s { \bar { \theta } } ( s )$ , the two equations can be written as

$$
\begin{array} { c l c r } { { \bar { T } _ { y } ( s ) - J _ { v } s ^ { 2 } \bar { \phi } _ { y } ( s ) = h s \bar { \theta } ( s ) } } \\ { { I _ { x } s ^ { 2 } \bar { \theta } ( s ) = h s \bar { \phi } _ { y } ( s ) } } \end{array}
$$

Eliminating $\bar { \phi } _ { y } ( s )$ , we obtain the equation

$$
\frac { \bar { \theta } ( s ) } { \bar { T } _ { y } ( s ) } = \frac { h / J _ { y } I _ { x } } { s [ s ^ { 2 } + ( h ^ { 2 } / J _ { y } I _ { x } ) ] }
$$

which defines the transfer function between the output $\theta ( s )$ and the input disturbing torque $T _ { y } ( s )$

The angular velocity $\dot { \theta }$ of the gyro relative to the platform is sensed by the electric pickoff, amplified and fed to a servomotor which applies a counter torque $T _ { s }$ opposing the disturbing torque $T _ { y }$ .Generally the platform inertia $J _ { y }$ is large so that the nutation frequency $\sqrt { h ^ { 2 } / J _ { y } I _ { x } }$ (see Eq. 6.3-19) is negligible. The approximate transfer function is then equal to,

$$
\frac { \bar { \theta } ( s ) } { \bar { T } _ { y } ( s ) } = \frac { h } { J _ { y } I _ { x } s ^ { 3 } }
$$

which enables the platform servosystem to be represented by the block diagram of Fig. 6.8-3, where $A ( s )$ is the transfer function of the electric pickoff, amplifier,and the servo motor. With $A ( s )$ known, the stable platform's dynamical behavior can be studied for stability and drift characteristics.

Thethree-axis stable platform can be consideredto be an assembly of three single-axis platforms similar to those of the previous section, but mounted in a single stable unit, as shown in Fig. 6.8-1.4 The analysis is more complex due to coupling between the three rotations. For the discussion of theinertial gunce system,it is sucient toassumetat there is a platform which will successfully maintain a given orientation in space.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/3e611e8f59283e31f2cfcf47977278e177c045811b429685e5d3e5f9729fa2b4.jpg)  
Fig. 6.8-3. Block diagram for the single-axis platform.

# 6.9 Three-Axis Platform (Resolution of Motion)

The analysis of a three-axis platform is more complex owing to coupling between the three rotations and the necessity of resolution of the platform pickoff signals because of nonalignment of the gimbal and platform axes.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/60d5571bf76c19c01a396d1f66410a707877af006b58a57d81c655ac50effdab.jpg)  
Fig. 6.9-l. Coupling in three-axis platform.

Figure 6.9--1 shows the angular momentum vectors of the $x$ y， $z$ gyros. Letting $\theta _ { x } ,$ $\theta _ { y } ,$ $\theta _ { z }$ be the outputs of the $x , y , z$ gyros due to rotations $\phi _ { x }$ $\phi _ { y }$ $\phi _ { z }$ of the input axes, the pickoff of each gyro must be,

$$
\begin{array} { r } { \sigma _ { w } = \theta _ { w } - \phi _ { y } } \\ { \sigma _ { y } = \theta _ { y } + \phi _ { x } } \\ { \sigma _ { z } = \theta _ { z } - \phi _ { y } } \end{array}
$$

With the gimbal axes lined up with the platform axes, the counteracting torques called for by the pickoff signals are of the form,

$$
T _ { s y } ( s ) = A _ { y } ( s ) \ \sigma _ { y } ( s ) = A _ { y } ( s ) [ \theta _ { y } ( s ) + \phi _ { x } ( s ) ]
$$

where $A _ { y } ( s )$ is the transfer function of the $y$ servosystem. Thus the behavior of the single axis platform is modified by the coupling term of the form $A _ { v } ( s ) \phi _ { x } ( s )$ ，

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0003_pages_0141-0210/auto/images/e9402bdff994b5d8d35d8b094800588f38659510bd4284101d6f6878b89489bd.jpg)  
Fig. 6.9-2. Block diagram of three-axis platform

The block diagram of the three-axis platform consists of the three uncoupled circuits of the form shown in Fig. 6.8-3 with additional connectionscorrespondingtothecoupling terms, $- A _ { x } ( s ) \phi _ { y } ( s )$ $A _ { y } ( s ) \ \phi _ { x } ( s )$ and $- A _ { z } ( s ) \phi _ { y } ( s )$ ,as shown in Fig. 6.9-2.

Assuming that the outer gimbal axis, originally parallel to the platform $_ x$ axis, is atached to the vehicle,as shown in Fig. 6.9-3,and assuming that the vehicle is roll-stabilized,the motion of the vehicle in pitch and yaw will cause the gimbal axes to deviate from the platform axes. It is evident then that the platform torques $T _ { x } ,$ $T _ { y }$ ， $T _ { z }$ must now be resolved along the displaced gimbal axes where the torque servomotors act. Since the countertorques are proportional to the platform pickoff signals,the proper torques about the new gimbal axes are found by resolution of the platform pickoff signals along the gimbal axes.


<!-- chunk 0004: pages 211-280 -->
With the vehicle roll-stabilized, we first allow the vehicle to nose down through a pitch angle Φy. Lettng the new gimbal axes be indicated by

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/81b72a20dcb7083b956ea4e66ba3932194ba5f0d607c370fed32c27a987920ff.jpg)  
Fig. 6.9-3. Gimbal rotation requires resolution of torque.

primes, the components of the platform pickoff signals along the gimbal axes

$$
\begin{array} { l l } { { \sigma _ { \alpha ^ { \prime } } = \sigma _ { x } \cos \Phi _ { y } - \sigma _ { z } \sin \Phi _ { y } } } \\ { { \sigma _ { y ^ { \prime } } = \sigma _ { y } } } \\ { { \sigma _ { z ^ { \prime } } = \sigma _ { x } \sin \Phi _ { y } + \sigma _ { z } \cos \Phi _ { y } } } \end{array}
$$

Next allow a rotation $\Phi _ { z }$ in yaw about the $z ^ { \prime }$ axis, and resolve $\sigma _ { x ^ { \prime } }$ along the pitch gimbal axis and the new roll axis,

$$
\begin{array} { r l } { \sigma _ { \mathrm { r o l l } } = \sigma _ { x ^ { \prime } } \sec \Phi _ { z } } \\ { \sigma _ { \mathrm { p i t c h } } = - \sigma _ { x ^ { \prime } } \tan \Phi _ { z } } \end{array}
$$

The resulting signal about the new gimbal axes of roll, pitch, and yaw due to both $\Phi _ { y }$ and $\Phi _ { z }$ are, then,

$$
\begin{array} { r l } & { \sigma _ { \mathrm { r o l l } } = ( \sigma _ { x } \cos \Phi _ { y } - \sigma _ { z } \sin \Phi _ { y } ) \sec \Phi _ { z } } \\ & { \sigma _ { \mathrm { p i t c h } } = - ( \sigma _ { x } \cos \Phi _ { y } - \sigma _ { z } \sin \Phi _ { y } ) \tan \Phi _ { z } + \sigma _ { y } } \\ & { \sigma _ { \mathrm { y a w } } = ( \sigma _ { x } \sin \Phi _ { y } + \sigma _ { z } \cos \Phi _ { y } ) = \sigma _ { z } , } \end{array}
$$

which can be expressed in the following matrix notation.

$$
{ \left[ \begin{array} { l } { \sigma _ { \mathrm { r o l l } } } \\ { \sigma _ { \mathrm { p i t c h } } } \\ { \sigma _ { \mathrm { y a w } } } \end{array} \right] } = { \left[ \begin{array} { l l l l } { \cos \Phi _ { y } \sec \Phi _ { z } } & { 0 } & { - \sin \Phi _ { y } \sec \Phi _ { z } } \\ { - \cos \Phi _ { y } \tan \Phi _ { z } } & { 1 } & { \ \sin \Phi _ { y } \tan \Phi _ { z } } \\ { \sin \Phi _ { y } } & { 0 } & { \ \cos \Phi _ { y } } \end{array} \right] } { \left[ \begin{array} { l } { \sigma _ { x } } \\ { \sigma _ { y } } \\ { \sigma _ { z } } \end{array} \right] }
$$

The function of the resolver is then to resolve the platform pickoff signals Ox, Ou, O to thecomponents Orol1, Opitch, Oyaw along the displaced gimbal axes housing the roll, pitch, and yaw servomotors.

# 6.10 Inertial Navigation

Navigation is the science of directing a vehicle to a destination by determining its position. In inertial navigation this task is accomplished without observation of landmarks, celestial bodies or radio beams.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/0362c220b7bac9b3e7d1e08a051639178d61d9dfbff5a02f9725149a76bca78a.jpg)  
Fig. 6.l0-l. Accelerometer and integrator.

A vehicle moving in space possesses six degrees of freedom, three translational and three rotational. Consequently, six sensors are needed. The stable platform discussed in Sec.6.8 offers a reference for the rotational motion, whereas the accelerometer is an instrument capable of detecting translational motion. In fact, the three gyros of the stable platform and the three accelerometers oriented in mutually perpendicular directions can supply allthe information for establishing the motion of a rigid body, and the high degree of accuracy with which this is being done has made inertial navigation a practical reality.2,5,7

Figure 6.10-1 shows a schematic of an accelerometer and integrator. Acceleration along its axis displaces the massagainst the spring according to Newton's equation $F = m a$ ,where $F$ is the spring force. The displacement of the masswhich is proportional to the aeleration is picked off by a potentiometer and integrated to velocity and displacement of the vehicle.

The accelerometers are mounted on a table which is always maintained normal to the local radius of the earth. This is accomplished by means of a computer and a clock which rotates the table relative to the stable platform, as indicated in Fig. 6.10-2. In some cases the accelerometers are mounted directly on the stable platform which is torqued to the normal position.

To obtain an understanding of how the inertial navigator works, we assume that the vehicle starts at the equator and that the plane of the stable platform is horizontal with the arrow pointing in the $N$ polar direction. If the vehicle moves towards the north along a longitude,and the accelerometer table is always kept normal to the geocentric radius $r _ { i }$ the $N { - } S$ accelerometer will measure the acceleration $a _ { x }$ (see Fig. 6.10-2). The proper rate of rotation of the table about the $y$ axis is then $\omega _ { y } = v _ { x } / r ,$ where $v _ { x }$ is determined from the first integral of $a _ { x }$ ，The latitude motor $B$ then rotates the table at a rate $\omega _ { y }$ to keep the $N { - } S$ line on the table normal to $r _ { c }$

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/76079e72326625e37606c296c41a765be95f4f0715a9fa618b4df100d9762f10.jpg)  
Fig. 6.l0-2. Components of an inertial navigator.

Due to rotation of the earth towards the east, the $E \mathrm { - } W$ line of the table must be rotated by the longitude motor $A$ to unwind the earth's rotation. Since during the motion of the vehicle the orientation of the stable platform remains fixed in inertial space (towards the $_ \mathrm { N }$ star) the required rotation of the accelerometer table about the $x$ axis of the stable platform at any latitude is $\Omega$ or $1 5 ^ { \circ } / \mathrm { h r }$

To this rotation must be added the rotation about the platform $x$ axis due to the E-W motion of the vehicle relative to the original longitude. By integrating the output of the E-W accelerometer and dividing by $r$ cos $\lambda$ ， the additional rotation to maintain the E-W line of the table normal to $r$ is $\omega _ { x } = v _ { y } / r$ cos λ.

These computations are performed by a computer which must be an integral part of the inertial system. Thus the inertial navigator must consist of the stable platform, accelerometers with integrators, a computer to compute the proper angular rates of the table due to vehicle motion, a clock to unwind the earth's rotation, and the servomotors to actually carry out these functions.

# 6.1l Oscillation of Navigational Errors

The accelerometers mounted on the vehicle measure only the nongravitational force Fng acting on the vehicle,and therefore one must add to it the gravitational force $\mathbf { F } _ { g }$ in order to determine the total force which determines the acceleration ${ \mathfrak { a } } _ { v }$ of the vehicle.

$$
\mathbf { F } _ { n g } + \mathbf { F } _ { g } = m \mathbf { a } _ { v }
$$

For example if the vehicle is resting on the surface of the earth, the verticle accelerometer will indicate the upward force (thrust) of the ground on the vehicle, or ${ \bf F } _ { n g } = { \bf W }$ . To this must be added the gravitational attraction of the earth on the vehicle $\mathbf { F } _ { g } = - \mathbf { W }$ which results in the zero acceleration of the vehicle.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/99f8e6fd652f0eea7630e26c6b6bba861534da9ef53e20785e09a17a587e3a55.jpg)  
Fig.6.ll-i. Simplified block diagram of gravityand positioncomputation.

Equation 6.11-1 can be expressed entirely in terms of acceleration by dividing by $m$

$$
\mathbf { a } _ { v } = \mathbf { A } _ { n g } + \mathbf { a } _ { g }
$$

where $\mathbf { A } _ { n \theta }$ is the nongravitational (thrust) acceleration indicated by the accelerometers. The vehicle position is then found bya double integration of the vehicle acceleration a, as shown by the simplified block diagram of Fig. 6.11-1. The gravitational acceleration a, which depends only on the position r is computed and added to the output of theaccelerometers to give the vehicle acceleration ${ \mathfrak { a } } _ { v }$

It is evident that an accelerometer error would result in incorrect rotation rates of the accelerometer table which would result in a position error, an incorrect value of a,, and a deviation of the accelerometer table from the normal to the true geocentric radius r. These errors are oscillatory for subsatelite speeds, and we will now investigate their nature.

We will define the correct position of the vehicle by a vector r referenced to inertial coordinates with origin at the center of earth. We will also define another set of coordinates x,y,z with origin coinciding with the correct position of the vehicle and with the $z$ axis parallel to r as shown in Fig.6.11-2. Thus the angular velocity of the vehicle is specified by $\omega _ { x } ,$ ${ \bf \Lambda } _ { x } , ~ \omega _ { y } , ~ \omega _ { z }$ respectively and the xy plane is always normal to the local geocentric radius $\pmb { \tau }$ 。

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/f50e6e24128ac6b5cabaa3ba887f812af807a44d86d33500d6ecf7d71c9ec1f8.jpg)  
Fig. 6.Il-2. Vehicle position indicated by r. Origin of $x _ { i }$ y, z coinciding with vehicle.

We now assume that the position of the vehicle is in error by

$$
\Delta \mathbf { r } = \Delta x \mathbf { i } + \Delta y \mathbf { j } + \Delta z \mathbf { k }
$$

and examine first the error in ${ \mathfrak { a } } _ { g } = - { \mathfrak { g } }$ . Since g is inversely proportional to the square of the distance from the center of the earth, the incorect components of g computed from $\pi + \Delta \mathbf { r }$ are

$$
{ \begin{array} { l } { g _ { z } = - g \left( { \frac { r } { r + \Delta z } } \right) ^ { 2 } = - g \left( 1 - { \frac { 2 \Delta z } { r } } \right) = - g + 2 { \omega _ { 0 } } ^ { 2 } \Delta z } \\ { g _ { \infty } = - g { \frac { \Delta x } { r } } = - { \omega _ { 0 } } ^ { 2 } \Delta x } \\ { g _ { \nu } = - g { \frac { \Delta y } { r } } = - { \omega _ { 0 } } ^ { 2 } \Delta y } \end{array} }
$$

where $- g$ is the correct value and $\omega _ { 0 } { } ^ { 2 } = g / r .$ 1

The acceleration error of the vehicle can be determined from the general equation for acceleration by replacing r by $\Delta \mathbf { r }$ ·

$$
\begin{array} { r l } & { \mathbf { a } _ { \mathrm { v } } = [ \Delta \ddot { x } + \omega _ { x } \omega _ { y } \Delta y + \omega _ { x } \omega _ { z } \Delta z - ( \omega _ { y } ^ { 2 } + \omega _ { z } ^ { 2 } ) \Delta x + \dot { \omega } _ { y } \Delta z - \dot { \omega } _ { z } \Delta y } \\ & { \qquad + 2 ( \omega _ { y } \Delta \dot { z } - \omega _ { z } \Delta \dot { y } ) ] \mathbf { i } } \\ & { \qquad + [ \Delta \ddot { y } + \omega _ { x } \omega _ { y } \Delta x + \omega _ { y } \omega _ { z } \Delta z - ( \omega _ { x } ^ { 2 } + \omega _ { z } ^ { 2 } ) \Delta y + \dot { \omega } _ { z } \Delta x - \dot { \omega } _ { x } \Delta z } \\ & { \qquad + 2 ( \omega _ { z } \Delta \dot { x } - \omega _ { x } \Delta \dot { z } ) ] \mathbf { j } } \\ & { \qquad + [ \Delta \ddot { z } + \omega _ { x } \omega _ { z } \Delta x + \omega _ { y } \omega _ { z } \Delta y - ( \omega _ { x } ^ { 2 } + \omega _ { y } ^ { 2 } ) \Delta z + \dot { \omega } _ { x } \Delta y - \dot { \omega } _ { y } \Delta x } \\ & { \qquad + 2 ( \omega _ { x } \Delta \dot { y } - \omega _ { y } \Delta \dot { x } ) ] \mathbf { k } \quad \mathrm { ( 6 . 1 1 - 5 } } \end{array}
$$

Substituting these quantities into the error equation,

$$
\Delta \mathbf { a } _ { \mathrm { v } } = \Delta \mathbf { A } + \Delta \mathbf { g }
$$

its component equations can be written as

$$
\begin{array} { r } { \left[ \cfrac { d ^ { 2 } } { d t ^ { 2 } } + { \omega _ { 0 } } ^ { 2 } - { ( { \omega _ { y } } ^ { 2 } + { \omega _ { z } } ^ { 2 } ) } \right] \Delta x = \Delta A _ { x } + \left( 2 { \omega _ { z } } \cfrac { d } { d t } + { \dot { \omega } } _ { z } - { \omega _ { x } } { \omega _ { y } } \right) \Delta y } \\ { - \left( 2 { \omega _ { y } } \cfrac { d } { d t } + { \dot { \omega } } _ { y } + { \omega _ { x } } { \omega _ { y } } \right) \Delta z \quad ( 6 . 1 1 - } \end{array}
$$

$$
\left[ \frac { d ^ { 2 } } { d t ^ { 2 } } + { \omega _ { 0 } } ^ { 2 } - ( { \omega _ { x } } ^ { 2 } + { \omega _ { z } } ^ { 2 } ) \right] \Delta y = \Delta A _ { y } + \left( 2 { \omega _ { x } } \frac { d } { d t } + { \dot { \omega } } _ { x } - { \omega _ { y } } { \omega _ { z } } \right) \Delta z
$$

$$
\begin{array} { r l r } & { } & { \left\lfloor d t ^ { 2 } \right\rfloor ^ { \mathrm { \scriptsize ~ \alpha ~ 1 ~ } \omega _ { 0 } } \quad \mathfrak { o } _ { x } ^ { \mathrm { \tiny ~ ( ~ \omega ~ 1 ~ \omega ~ 2 ~ ) } } \mathrm { \tiny ~ \left. ~ \right.} ^ { \omega _ { z } } = \omega _ { y } ^ { \mathrm { \tiny ~ \alpha ~ 1 ~ } }  ^ { \mathrm { \tiny ~ \omega ~ \wedge ~ } } \left\lfloor ^ { \omega _ { x } } d t ^ { \mathrm { \tiny ~ \alpha ~ 1 ~ } \omega _ { x } } - \omega _ { y } \omega _ { z } \right. } \\ & { } & { \qquad - \left( 2 \omega _ { z } \cfrac { d } { d t } + \dot { \omega } _ { z } + \omega _ { x } \omega _ { y } \right) \Delta x \quad \mathrm { \tiny ~ ( \Omega ~ } } \\ & { } & { \qquad \left. \cfrac { d ^ { 2 } } { d t ^ { 2 } } - 2 \omega _ { 0 } ^ { \mathrm { \tiny ~ \alpha ~ 2 ~ } } - ( \omega _ { x } ^ { \mathrm { \tiny ~ 2 ~ + ~ } } \omega _ { y } ^ { \mathrm { \tiny ~ \alpha ~ 2 ~ } } ) \right. \Delta z = \Delta A _ { z } + \left( 2 \omega _ { y } \cfrac { d } { d t } + \dot { \omega } _ { y } - \omega _ { x } \omega _ { z } \right. } \\ & { } & { \qquad \left. \qquad \quad \mathrm { \cot ~ } \Omega \right. } \end{array}
$$$$
\begin{array} { r l } { \displaystyle \left[ \frac { d ^ { 2 } } { d t ^ { 2 } } - 2 { \omega _ { 0 } } ^ { 2 } - ( { \omega _ { x } } ^ { 2 } + { \omega _ { y } } ^ { 2 } ) \right] \Delta z = \Delta A _ { z } + \left( 2 { \omega _ { y } } \frac { d } { d t } + { \dot { \omega } _ { y } } - { \omega _ { x } } { \omega _ { z } } \right) \Delta x } & { } \\ { - \left( 2 { \omega _ { x } } \frac { d } { d t } + { \dot { \omega } _ { x } } + { \omega _ { y } } { \omega _ { z } } \right) \Delta y } & { ( 6 . 1 1 - \omega _ { x } ) } \end{array}
$$

To interpret these equations, assume the vehicle to be traveling with velocity $v$ in the $y$ direction along a great circle at constant altitude. Then ${ { \omega } _ { y } } = { { \omega } _ { z } } = 0$ ,and $\omega _ { x } = - v / r$ . The above equations reduce to,

$$
\begin{array} { c } { { \left( \frac { d ^ { 2 } } { d t ^ { 2 } } + { \omega _ { 0 } } ^ { 2 } \right) \Delta x = \Delta A _ { x } } } \\ { { { } } } \\ { { \left[ \frac { d ^ { 2 } } { d t ^ { 2 } } + \left( { \omega _ { 0 } } ^ { 2 } - \frac { v ^ { 2 } } { r ^ { 2 } } \right) \right] \Delta y = \Delta A _ { y } + \left( 2 \omega _ { x } \frac { d } { d t } + \dot { \omega } _ { x } \right) \Delta z } } \\ { { { } } } \\ { { \left[ \frac { d ^ { 2 } } { d t ^ { 2 } } - \left( 2 { \omega _ { 0 } } ^ { 2 } + \frac { v ^ { 2 } } { r ^ { 2 } } \right) \right] \Delta z = \Delta A _ { z } - \left( 2 \omega _ { x } \frac { d } { d t } + \dot { \omega } _ { x } \right) \Delta y } } \end{array}
$$

The first two equations have solutions which are harmonic oscillations of frequency $\omega _ { 0 } = \sqrt { g / r }$ and $\sqrt { \omega _ { 0 } ^ { 2 } - ( v ^ { 2 } / r ^ { 2 } ) }$ The solution of the third equation is hyperbolic and $\Delta z$ must diverge.

For ordinary altitudes, the period as computed from $\omega _ { 0 }$ is,

$$
\tau = 2 \pi \sqrt { \frac { r } { g } } = 2 \pi \sqrt { \frac { 3 9 6 0 \times 5 2 8 0 } { 3 2 . 2 \times 6 0 ^ { 2 } } } = 8 4 \mathrm { m i n }
$$

andthe inertial system is often referred toas the84-min Schuler pendulum. As $v$ approaches orbital speeds for satelites, $\omega _ { 0 } ^ { 2 } - ( v ^ { 2 } / r ^ { 2 } )$ will approach zero and the desirable oscillatory nature of the position eror disappears.

In addition, we might mention briefly the error introduced by the deviation from normal of theacceleration table. If the table tiltsby asmall angle $\Phi = \phi _ { x } \mathbf { i } + \phi _ { y } \mathbf { j } + \phi _ { z } \mathbf { k } .$ the error in the accelerometer output will be,

$$
\Phi \times \mathrm { \bf ~ A } = ( \phi _ { y } A _ { z } - \phi _ { z } A _ { y } ) \mathrm { i } + ( \phi _ { z } A _ { x } - \phi _ { x } A _ { z } ) \mathrm { j } + ( \phi _ { x } A _ { y } - \phi _ { y } A _ { x } ) \mathrm { k }
$$

# PROBLEMS

1. An aircraft directional gyro has a spin angular momentum of $h = 3 . 0$ Ib-in./sec.If the drift rate is specified as $0 . 0 1 ^ { \circ } / \mathrm { h r }$ determine the torque producing the drift.   
2. An inertial system is to guide an airplane traveling at a speed of $6 0 0 \ \mathrm { m p h }$ to a destination of 10oo miles with an accuracy of $\%$ mile. Determine the allowable drift rate.   
3. Assume that for the single-axis stable platform of Fig. 6.8-2 there is damping and spring stiffness restraining the rotation of the output axis. Write the equation for the torque about the output axis.   
4. Write the subsidiary equation for the single-axis platform including damping and spring stiffness, and draw the new block diagram.   
5. For the single-axis platform of Prob. 3, determine the transfer function $\theta ( s ) / \phi ( s )$ and discuss the special cases when: (a) damping ${ \it \Delta \phi } = { \it \Delta \theta }$ ； $( b )$ spring stiffness ${ } = 0$ ; (c) damping and spring stiffness $= 0$ . Indicate the type of gyro obtained in each case.   
6. For case (c) of Prob. 5,obtain the transfer function $T _ { s } / T _ { d } ,$ where $T _ { d }$ and $T _ { s }$ are the disturbing torque and the servo countertorque, and discuss the influence of $A ( s )$ on the system.   
7. Obtain the stiffness characteristics of the single-axis platform by examining the transfer functions $T _ { d } ( s ) / \theta ( s )$ and $T _ { d } ( s ) / \phi ( s )$   
8. A three-axis stable platform has gyros mounted as shown in the sketch. Identify which are the $_ x$ ， $y$ ,and $z$ gyros and determine the equations for the pickoff signals, using $\phi _ { i }$ for input and $\theta _ { i }$ for output.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/da59638c11ddcdacffedec199697bbad3c666699ae44326a0863550b4002f334.jpg)  
Prob.8

9. If the three-axis platform has gyros arranged as shown, identify the x, y, and $z$ gyros and determine the equations for the pickoff signals.

![](../chunks/Introduction to space dynamics (Thomson, William Tyrrell) (z-library.sk, 1lib.sk, z-lib.sk_part_0004_pages_0211-0280/auto/images/ca85d6467b2503e247bff68d76bb0b257dcc8868c0bd05a8672b84ed971cf836.jpg)  
Prob.9

10. Draw a block diagram for the dynamics of the platform of Prob. 9.   
11. If the platform of Prob. 9 is mounted on a missile with the roll-stabilized axis along the $_ x$ axis,determine theequations for theresolver signal along the servo roll, pitch,and yaw axes due to angular rotations $\Phi _ { y }$ and $\Phi _ { z }$   
12. An airplane with an inertial navigator is headed in the direction $\textbf { N } 6 0 ^ { \circ }$ W at latitude $3 2 ^ { \circ } \bf N$ at speed $6 0 0 ~ \mathrm { { m p h } }$ . Determine the angular rates about the meridian and latitude axes due to the motion and the required angular rates of the accelerometer table.   
13. A rocket ship guided by an inertial navigator is traveling along a great circle route at constant altitude of 100 miles and at a speed of $1 2 , 0 0 0 \ \mathrm { \ m p h }$ With the horizontal axis $y$ oriented along theflight path,discuss thenatureof the navigational errors and calculate the frequency of the oscillatory error.

# REFERENCES

1. Cunningham,W.J.,Nonlinear Analysis,McGraw-HillBook Co.,New York (1958), p. 125.   
2.Frye,E.,“FundamentalsofInertialGuidance and Navigation,”J.Astronaut.Si., V, No. 1 (1958), 1.   
3. Malkin, I. G.,“Some Problems in the Theory of Nonlinear Oscilations,” Translation SeriesAtomic nergyommision,AEC-tr-3766 (Book 1),Cer1.   
4.Mitsutomi, T.,“Characteristics and Stabilization of an Inertial Platform, Trans. IRE,Aeronauticalandavigational Electroics (June958),905.   
5.O'Donell,C.F.,"Inertial Nvigation,”J.Franklin Istitute,266,Nos.4ad5 (Oct. and Nov. 1958).   
6. Plymale, B.T., and Goodstein, R.,"Nutation of a Free Gyro Subject to an Impulse," J. Appl. Mech.,22, No. 3 (Sept. 1955), 365-366.   
7. Slater, J. M.,and Duncan,D.B.,"Inertial Navigation,Aeronaut. Eng.Review,   
15, No.1 (Jan. 1956).   
8.Stoker,J.J.oinear Vbrations,ntersience ublisers,ew ork(9)98.   
9. Streeter, J. R., “Error Analysis of an Inertial System in Vehicles of High Speed," Master of Science Thesis in Engineering, University of California, Los Angeles (June 1960).   
10.Thomson,W.T.，aplace ransformation (2nd ed.)，Prentice-Hall,nglewood Cliffs, N.J. (1960).   
11. Wrigley,W., Woodbury, R. B.,and Hovorka,J.,"Application of Inertial Guidance Principles" Automatic Control, 7, No. 1, 22 (July 1957).   
12. Pitman,G. R., “Inertial Guidance" John Wiley & Sons, Inc. New York (1962).

# Space Vehicle Motion
