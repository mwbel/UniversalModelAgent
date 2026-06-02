# CHAPTER 6

# SOLUTIONS TO THE APPROXIMATE

# LIOUVILLE EQUATION

The Liouville equation is greatly simplified by a perturbation scheme which is valid for all problems to be treated except polar wandering. The deformation of the Earth is allowed for by various Love numbers.

# 1. Perturbations

The following scheme is convenient as long as the poles of figure and rotation do not wander too far from the reference pole:

$$
\left. \begin{array}{l l l} C _ {1 1} = A + c _ {1 1}, & C _ {2 2} = A + c _ {2 2}, & C _ {3 3} = C + c _ {3 3}, \\ C _ {1 2} = c _ {1 2}, & C _ {1 3} = c _ {1 3}, & C _ {2 3} = c _ {2 3}, \\ \omega_ {1} = \Omega m _ {1}, & \omega_ {2} = \Omega m _ {2}, & \omega_ {3} = \Omega (1 + m _ {3}) \end{array} \right\}, \tag {6.1.1}
$$

where $A, A, C$ are the moments of inertia referred to the principal axes; $\Omega$ is the mean angular velocity of the Earth, $0.729 \times 10^{-4}$ radians per sidereal second; $c_{is} / C, m_i$ and $h_i / (\Omega C)$ are small dimensionless quantities whose products and squares can be neglected. The Liouville equation (3.1.6) then reduces to the simple form

$$
\frac {\dot {m} _ {1}}{\sigma_ {r}} + m _ {2} = \phi_ {2}, \quad \frac {\dot {m} _ {2}}{\sigma_ {r}} - m _ {1} = - \phi_ {1}, \tag {6.1.2}
$$

$$
\dot {m} _ {3} = \dot {\phi} _ {3}, \tag {6.1.3}
$$

where $\sigma_r$ and $\phi_i$ are defined by

$$
\sigma_ {r} = \frac {C - A}{A} \Omega \tag {6.1.4}
$$

and $\begin{array}{r}\Omega^2 (C - A)\phi_1 = \Omega^2 c_{13} + \Omega \dot{c}_{23} + \Omega h_1 + \dot{h}_2 - L_2\\ \Omega^2 (C - A)\phi_2 = \Omega^2 c_{23} - \Omega \dot{c}_{13} + \Omega h_2 - \dot{h}_1 + L_1\\ \Omega^2 C\phi_3 = -\Omega^2 c_{33} - \Omega h_3 + \Omega \int_0^t L_3  \mathrm{d}t \end{array}$

with $(\cdot)$ designating $\mathrm{d} / \mathrm{d}t$ . The left sides of (6.1.2, 3) are determined by astronomic observations, the right sides by geophysical observations. The dimensionless 'excitation function' $\phi_{i}$ contains all

possible geophysical effects on the motion of the Earth.* The evaluation of $\phi_{i}$ is the principal task of this book.

Variations in the l.o.d. are dealt with by (6.1.3). Wobble is dealt with by (6.1.2); $m_1, m_2, 1$ , are the direction cosines of the rotation axis (3.3.1). In the complex system

$$
\mathbf {m} = m _ {1} + i m _ {2}, \quad \boldsymbol {\phi} = \phi_ {1} + i \phi_ {2} \tag {6.1.6}
$$

we have simply $i\frac{\dot{\mathbf{m}}}{\sigma_r} +\mathbf{m} = \boldsymbol {\phi}.$ (6.1.7)

# 2. Free wobble

In the case of free nutation of a rigid Earth, $\Phi = 0$ and $\exp (i\sigma_r t)$ is a solution to (6.1.7). The period $2\pi / \sigma_r$ is about ten months. The role of the Earth's deformation is to increase the period of free nutation by a substantial fraction ( $\sim 40$ per cent). This effect is not altogether obvious and in fact had not been anticipated prior to Chandler's discovery of a 14-month period in the latitude variation (§ 7.1). A qualitative explanation is as follows: for a rigid Earth the frequency of free nutation is proportional to the equatorial bulge (6.1.4); for a deformable Earth it is dependent only on that part of the equatorial bulge which does not adjust to the instantaneous rotation-axis.

Consider the excitation function due solely to rotational deformation. The products of inertia arising from rotational deformation are given by (5.5.1). In terms of the perturbation notation these are

$$
c _ {1 3} = (C - A) \frac {k}{k _ {f}} m _ {1}, \quad c _ {2 3} = (C - A) \frac {k}{k _ {f}} m _ {2}. \tag {6.2.1}
$$

When these expressions are substituted in (6.1.5), one obtains for the excitation function

$$
\psi_ {D} - i \Omega^ {- 1} \dot {\psi} _ {D}, \tag {6.2.2}
$$

where $\psi_{D} = (k / k_{f})\mathbf{m}$ (6.2.3)

is a convenient notation. Equation (6.1.7) becomes

$$
\frac {i \dot {\mathbf {m}}}{\sigma_ {r}} + \mathbf {m} = \psi_ {D} - i \Omega^ {- 1} \dot {\psi} _ {D} \approx \psi_ {D}. \tag {6.2.4}
$$

The approximation depends on $\sigma_r / \Omega = (C - A) / A$ being a small number. The error is 0-1 per cent. Hence (6.2.3) can be interpreted as that part of the excitation function $\Phi$ that is due to rotational deformation. Equations (6.2.3) and (6.2.4) can be written in the form

$$
i \dot {\mathbf {m}} + \sigma_ {0} \mathbf {m} = 0,
$$

which differs from the corresponding equation for a rigid Earth ((6.1.7) with $\phi = 0$ )

$$
i \dot {\mathbf {m}} + \sigma_ {r} \mathbf {m} = 0
$$

in that the frequency of free mutation has been reduced from $\sigma_r$ to

$$
\sigma_ {0} = \sigma_ {r} \frac {k _ {f} - k}{k _ {f}}. \tag {6.2.5}
$$

For the 'equivalent' Earth (§ 5.6), the ratio is

$$
\frac {\sigma_ {0}}{\sigma_ {r}} = \frac {\mu}{1 + \mu} = \frac {2 \cdot 3}{3 \cdot 3} = 0 \cdot 7 0. \tag {6.2.6}
$$

The principal axis of a body with moments and products of inertia $A, A, C; c_{12}, c_{13}, c_{23}$ is inclined (approximately) by $c_{13} / (C - A)$ , $c_{23} / (C - A)$ relative to the reference axis $x_3$ . It follows from (6.2.1) and (6.2.3) that $\psi_D$ designates the inclination of the principal axis of the rotationally deformed equatorial bulge, the 'deformation axis.' The positions where the $\psi_D$ -axis pierces the surface are the deformation poles.

The three models in table 6.1 are instructive: in the case of the 'fluid' Earth, the equatorial bulge adjusts completely to the rotation

Table 6.1   

<table><tr><td>Model</td><td>‘Tidal-effective’ Love number</td><td>Deformation axis</td><td>Nutation frequency</td></tr><tr><td>Rigid Earth</td><td>k=0</td><td>ψD=0</td><td>σ0= σr= 1 cycle in 10 months</td></tr><tr><td>‘Fluid’ Earth</td><td>k=kf</td><td>ψD=m</td><td>σ0=0</td></tr><tr><td>‘Actual’ Earth</td><td>k=0·29</td><td>ψD=0·30 m</td><td>σ0= σr/1·4= 1 cycle in 14 months</td></tr></table>

and there is no rotational stability and no nutation: $\sigma_0 = 0$ . Only that portion of the equatorial bulge that remains frozen during the wobble (about 70 per cent) provides any stability.

# 3. Forced wobble

Consider a wobble induced by any prescribed event. The procedure to be followed is to compute first the excitation function, $\psi(t)$ , as if the Earth were rigid. The effect of rotational deformation is to produce an additional excitation,

$$
\psi_ {D} = \left(k / k _ {r}\right) \mathbf {m}, \tag {6.2.3}
$$

which must be taken into account in addition to the prescribed excitation. If the initially prescribed event does not load the Earth (e.g., winds), then the total excitation function consists of the two oparts

$$
\phi = \psi + \psi_ {D}; \tag {6.3.1a}
$$

if it does load the Earth, then

$$
\phi = \psi + \psi_ {D} + \psi_ {L}, \tag {6.3.1b}
$$

where, in view of § 5.8, $\psi_{L} = k^{\prime}\psi$ (6.3.2)

is an additional excitation arising from load deformation.*

The effect of rotational deformation is then to produce a larger excitation (and wobble) than would have obtained on a rigid Earth; the effect of load deformation is to reduce the overall excitation ( $k'$ is negative). One may choose to interpret rotational deformation as positive feedback, load deformation as negative feedback.

It is convenient to define a 'modified excitation',

$$
\Psi = \kappa_ {\text {w o b b l e}} \psi , \tag {6.3.3}
$$

where $\kappa_{\mathbf{wobble}}$ is a 'transfer function' equal to

$$
\kappa_ {\text {w o b b l e}} = \frac {k _ {f}}{k _ {f} - k}, \tag {6.3.4a}
$$

and $\kappa_{\mathrm{wobble}} = (1 + k')\frac{k_f}{k_f - k},$ (6.3.4b)

depending upon whether the prescribed event does not or does load the Earth. The equation (6.1.7) can then be written in the following equivalent forms:

$$
\dot {\mathbf {m}} = i \sigma_ {r} (\mathbf {m} - \boldsymbol {\phi}), \tag {6.3.5}
$$

$$
\dot {\mathbf {m}} = i \sigma_ {0} (\mathbf {m} - \boldsymbol {\Psi}). \tag {6.3.6}
$$

* The excitation axis is then a generalization of the 'principal axis', or 'axis of figure'. If the prescribed excitation, $\psi$ , is due entirely to relative motion, then the deformation axis $\psi_{D}$ is also the principal axis; if it is due entirely to a shift in matter, then the excitation axis $\phi$ is the principal axis.

The two forms differ with respect to frequency and the excitation function. The total excitation, $\pmb{\phi}$ , includes the rotational deformation $\psi_{D}$ , and when this is combined with $\mathbf{m}$ in the sense of §6.2 then $\sigma_{r}$ becomes $\sigma_0$ , and $\phi$ becomes $\Psi$ .

# 4. Transfer function

The transfer function $\kappa$ for the equivalent Earth is obtained from the definitions of $k$ and $k'$ given in (5.6.2) and (5.8.5) respectively. The values are

$$
\kappa_ {\text {w o b b l e}} = \frac {1 + \mu}{\mu} = 1 \cdot 4 3, \tag {6.4.1a}
$$

$$
\kappa_ {\text {w o b b l e}} = 1 \tag {6.4.1b}
$$

depending on whether the prescribed event does not or does load the Earth. In the latter case the amplification from rotational deformation cancels the diminution from load deformation, and the induced wobble is the same as if the Earth were rigid. At first glance the result might appear surprising. But the load deformation enters only insofar as it contributes to the products of inertia, and these are spherical harmonics of degree 2 and of the same form as the rotational deformation.*

For problems involving the l.o.d. the rotational deformation as well as the load deformation acts in a sense to reduce the total excitation as compared to what it would be on a rigid Earth. It can be shown that the rotational deformation is negligible. To maintain symmetry with the wobble notation, it is convenient to write

$$
\phi_ {3} = \Psi_ {3} = \kappa_ {1. o. d.} \psi_ {3}, \tag {6.4.2}
$$

where $\kappa_{\mathrm{l.o.d.}} = 1,$ (6.4.3a)

$$
\kappa_ {1. 0. d.} = 1 + k ^ {\prime} = \frac {\mu}{1 + \mu} \tag {6.4.3b}
$$

depending on whether the prescribed event does not or does load the Earth.

The working rule is then to compute the excitation function, $\psi_{i}$ , as if the Earth were rigid, and to multiply by a factor $\kappa$ as given in table 6.2 to obtain the modified excitation $\Psi_{i}$ . The result can readily

Table 6.2. The transfer function $\kappa$ .   

<table><tr><td></td><td>(a): no load</td><td>(b): load</td></tr><tr><td>wobble</td><td>1·43</td><td>1·00</td></tr><tr><td>l.o.d.</td><td>1·00</td><td>0·70</td></tr></table>

be compared to the astronomic observations by virtue of the relations

$$
\dot {\mathbf {m}} = i \sigma_ {0} (\mathbf {m} - \boldsymbol {\Psi}), \tag {6.4.4a}
$$

$$
\dot {m} _ {3} = \dot {\Psi} _ {3}, \tag {6.4.4b}
$$

which follow from (6.3.6), (6.3.3) and (6.4.2).

The numerical values in table 6.2 must be used with caution. The values are based on the tidal-effective rigidity as obtained from the Chandler wobble (§ 10.3). At high frequencies the values may fail because the response of oceans and core may be frequency-dependent (§ 10.4); at very low frequencies the anelastic deformation of the mantle may play an important role, and the transfer function is then no longer a pure number (§ 5.11, 12.6).

# 5. A geometric interpretation

The effects of rotational and load deformations on wobble can now be summarized geometrically (fig. 6.1). Initially the excitation and rotation poles are taken at the origin of the geographic coordinates, hence $\phi = 0$ , $\mathbf{m} = 0$ . At time 0 the excitation pole is displaced suddenly (in the direction $19^{\circ}$ E. on the figure) by some specified event.

In the upper diagram the Earth is assumed to be rigid, and the pole of rotation $\mathbf{m}$ revolves about the excitation pole $(\pmb{\psi} = \pmb{\Psi} = \pmb{\phi})$ as shown. In the central diagram allowance is made for deformation in the case of an excitation that does not load the Earth $(\pmb{\psi}_{L} = 0)$ . The new feature is that the equatorial bulge adjusts itself to the disturbed position of the pole of rotation; the plane of the bulge

tends to align normal to the rotation axis, but on account of elastic constraint is only about one-third successful: $\psi_{D} = (k / k_{f})\mathbf{m} = 0\cdot 30\mathbf{m}$

![](images/ff7a94a8104be1036b07ef650f455cf7a524843207864927a1069208bbbdfe95.jpg)

![](images/059570f4e3088e982d2590d4fa3639849b0421f07fcb02f9c4f8aff3217f6f3a.jpg)  
Fig. 6.1. The coordinates $x_{1}, x_{3}$ are drawn from the undisturbed poles in the direction of Greenwich and $90^{\circ}$ east of Greenwich, respectively. The disturbed excitation pole $\Psi$ is displaced in the direction $19^{\circ}$ E. The resulting paths of the pole of rotation, $\mathbf{m}$ , are shown for a rigid Earth (top); for a deformable Earth in the case of a non-loading excitation (center), and of a loading excitation (bottom). The initially specified excitation, $\psi$ , is the same for all three cases. The positions of the poles of deformation $\psi_{D}$ , load $\psi_{L}$ , total excitation $\Phi$ , and of the modified excitation $\Psi$ are shown.

![](images/24d492a919687682ac01266da76dd4203c0a63a2571bc971dcee15b8996a4e2d.jpg)

The total excitation pole $\phi = \psi + \psi_{D}$ consists of that part $\psi$ which was computed under the assumption of a rigid Earth plus the additional part $\psi_{D}$ arising from the deformation. The pole of

rotation $\mathbf{m}$ revolves about the mean position\* $\Psi$ of the excitation pole with a radius amplified by a factor $k_{f} / (k_{f} - k) = 1\cdot 43$ as compared to the rigid case, but the separation $\mathbf{m} - \Phi$ between the rotation pole and the instantaneous excitation pole is the same as in the rigid case. The speed of wandering of the rotation pole is proportional to $\mathbf{m} - \Phi$ (6.3.5) and therefore unchanged by the deformation, but the period for a complete revolution is increased from 10 months to 14 months on account of the corresponding increase in radius.

The situation is more complicated if the excitation pole loads the Earth (lower diagram). The excitation $\psi + \psi_L$ after allowing for load deformation is then smaller than the excitation $\psi$ due to the initially prescribed surface loads. This reduction is cancelled by the amplification due to rotational deformation, so that the radius of the circle described by the pole of rotation is now the same as for the rigid Earth. As always, the speed of the wandering pole is proportional $\mathbf{m} - \phi$ . This is reduced by a factor 1·4 as compared to the rigid case, and accordingly the period of revolution increased from 10 to 14 months.

# 6. Sway

Our emphasis has been on the motion of the rotation axis relative to the reference system. If there is no outside torque, the axis that remains truly fixed in space is that of the absolute angular momentum $H_{i}$ , also called the 'invariable' axis. The rotation axis executes a slight 'sway' relative to the invariable axis, and hence the celestial pole is not absolutely fixed relative to Polaris, even in the absence of precession. Observationally, sway is undistinguishable from precession and forced nutation; these all involve variations in the polar distance (or declination) of a star. In our terminology, sway is confined to variations due entirely to events on the planet Earth, whereas precession and nutation depend on attractive forces of Sun, Moon and planets.

* The fact that the modified excitation pole $\Psi$ is also the mean position of the instantaneous pole $\psi$ can be proven as follows. Assuming $\Psi$ to be at the center of the concentric circles prescribed by $\mathfrak{m}$ (radius $\mathcal{R}$ ) and by $\phi$ , we may write $\mathfrak{m} = \Psi + \alpha \mathcal{R}$ , $\Phi = \Psi + \alpha (k / k_f) \mathcal{R}$ , where $\alpha$ is a unit vector. Form $(k / k_f) \mathfrak{m} - \phi$ and allow for (6.2.3). The result is $\psi_p - \phi = \Psi [(k / k_f) - 1]$ . We now make use of (6.3.1), (6.3.2), and (6.3.4) to obtain $\Psi = \kappa \psi$ which in accord with the definition (6.3.3) of $\Psi$ .

The position, with respect to the reference axes, of the invariable pole is

$$
\frac {\mathbf {H}}{C \Omega} = \frac {H _ {1} + i H _ {2}}{C \Omega}.
$$

A line through the Earth's center and the invariable pole retains its direction in space. Dividing both sides of (3.1.3) by $C\Omega$ and applying the perturbation scheme (6.1) gives

$$
\frac {\mathbf {H}}{C \Omega} = \mathbf {m} + H (\boldsymbol {\phi} - \mathbf {m}). \tag {6.6.1}
$$

The precessional constant $H$ (no relation to $\mathbf{H}$ ) is a small quantity; it follows that the invariable and rotation poles are separated by a distance small compared to the displacement of either pole except if $|\mathbf{m}| \ll |\boldsymbol{\Phi}|$ . The condition $|\mathbf{m}| \ll |\boldsymbol{\Phi}|$ applies to frequencies large compared to the frequency, $\sigma_0$ , of free nutation.

# 7. Solutions for various excitation functions

The solution to (6.4.4a) for the wobble due to any excitation $\Psi(t)$ is

$$
\mathbf {m} (t) = \mathrm {e} ^ {i \sigma_ {0} t} \left[ \mathbf {m} _ {0} - i \sigma_ {0} \int_ {- \infty} ^ {t} \boldsymbol {\Psi} (\tau) \mathrm {e} ^ {- i \sigma_ {0} \tau} \mathrm {d} \tau \right], \tag {6.7.1}
$$

where $\mathbf{m}_0$ is an arbitrary complex constant.

Consider first $\Psi(t) = \mathbf{J}H(t)$ , where $H(t)$ is the Heaviside step function. Then $\mathbf{m}_0 = 0$ , $\mathbf{m} = 0$ for $t < 0$ , and

$$
\mathbf {m} = \mathbf {J} (1 - \mathrm {e} ^ {i \sigma_ {0} t}), \quad t \geqslant 0. \tag {6.7.2}
$$

The rotation pole $\mathbf{m}$ describes a circle about the modified excitation pole $\mathbf{J}$ in a period $T = 2\pi /\sigma_0$ (fig. 6.2). The direction is west-to-east, in the same sense as the diurnal rotation and positive in the adopted coordinate system.

As a second example, let $\Psi(t) = \mathbf{N}\delta(t)$ , where $\delta(t)$ is the Dirac function. The solution is

$$
\mathbf {m} = - i \sigma_ {0} \mathrm {N e} ^ {i \sigma_ {0} t}, \quad t \geqslant 0. \tag {6.7.3}
$$

The rotation pole shifts abruptly at time 0, and then revolves positively and $90^{\circ}$ in advance of the previous solution (fig. 6.2).

As a third example, we take the case of a harmonic excitation of any frequency, $\sigma$ :

$$
\boldsymbol {\Psi} = \boldsymbol {\Psi} ^ {c} \cos \sigma t + \boldsymbol {\Psi} ^ {s} \sin \sigma t. \tag {6.7.4}
$$

The four numbers $\Psi_1^c, \Psi_2^c, \Psi_1^s, \Psi_2^s$ determine phase and amplitude of the excitation. It is often convenient to use the alternate forms

$$
\Psi = \Psi^ {+} e ^ {i \sigma t} + \Psi^ {-} e ^ {- i \sigma t} = | \Psi^ {+} | e ^ {i (\sigma t + \lambda^ {+})} + | \Psi^ {-} | e ^ {- i (\sigma t - \lambda^ {-})}. \tag {6.7.5}
$$

The first term in either expression designates positive (west-to-east) motion of the excitation pole around a circle of radius $|\Psi^{+}|$ ; east

![](images/e3e204980e4c6fb189e677cbde383d33c9584293247ce716df73308233283ae0.jpg)

![](images/05c1e486dc3811398df76c119f81b6e508c379184b3bba5eddd581da0d4e3068.jpg)  
Fig. 6.2. Positions of the pole of rotation at times $0, \frac{1}{2} T, \frac{1}{2} T, \frac{1}{2} T$ due to (left) and excitation $\Psi = JH(t)$ , and (right) $\Psi = N\delta(t)$ .

longitude $\lambda^{+}$ at time 0 is given by tan $\lambda^{+} = \arg \Psi^{+}$ . The second term represents a corresponding circular motion in the opposite sense. Linear and circular components are connected by the formulae

$$
\Psi^ {c} = \Psi^ {+} + \Psi^ {-}, \quad \Psi^ {s} = i (\Psi^ {+} - \Psi^ {-}). \tag {6.7.6}
$$

The motion (6.7.5) is elliptical. The semi-major and semi-minor axes have the magnitude

$$
| \Psi^ {+} | + | \Psi^ {-} |, | \Psi^ {+} | - | \Psi^ {-} |,
$$

respectively, and the ellipticity equals

$$
\frac {2 | \Psi^ {-} |}{| \Psi^ {+} | + | \Psi^ {-} |}.
$$

The major axis lies in east longitude $\frac{1}{2} (\lambda^{+} + \lambda^{-})$ and is occupied at a time $t$ so that $\sigma t = \frac{1}{2} (\lambda^{-} - \lambda^{+})$ . Analogous formulae can be written for $\mathbf{m}$ .

The solution consists of two parts: the particular solution

$$
\mathbf {m} = \mathbf {m} _ {0} e ^ {i \alpha_ {0} t} \tag {6.7.7}
$$

shows positive motion with the frequency, $\sigma_0$ , of the free nutation, whereas the forced wobble is given by

$$
\mathbf {m} = \frac {\sigma_ {0} \Psi^ {+}}{\sigma_ {0} - \sigma} \mathrm {e} ^ {i \sigma t} + \frac {\sigma_ {0} \Psi^ {-}}{\sigma_ {0} + \sigma} \mathrm {e} ^ {- i \sigma t}, \tag {6.7.8}
$$

with the forced frequency $\sigma$ . By appropriate superposition of free and forced motion it is, of course, possible to develop complex patterns. This is true particularly if free and forced frequencies are close to each other, as in fact they are for the Chandler motion and the annual wobble. Various examples have been worked out by Wanach (1919), and a few of these have been reproduced by Lambert (1931, p. 256-8). It is more instructive to consider the forced motion by itself. The free motion can be regarded as having been destroyed by friction or separated in the record by suitable analysis.

Fig. 6.3 shows the forced wobble for the case of plane polarization, $|\Psi^{+}| = |\Psi^{-}|$ . In the case of low frequencies (left) the pole of rotation describes an ellipse with the major axis along the axis of the excitation pole. In the asymptotic case of $\sigma \rightarrow 0$ , the two poles oscillate together, $\mathbf{m} \rightarrow \mathbf{\Psi}$ . As the frequency approaches resonance, $\sigma \rightarrow \sigma_0$ , the path of pole of rotation approaches a circle, and the radius becomes infinite (if there is no dissipation). The center diagram is for the case of the annual frequency, which lies slightly above resonance. For even higher frequencies (right) the eccentricity of the path of $\mathbf{m}$ becomes larger again, but in this case with the major axis at right angles to that of $\mathbf{\Psi}$ . As $\sigma \rightarrow \infty$ the wobble becomes vanishingly small. In all events the motion of the pole along its elliptical path is in a positive (west-to-east) sense.

For the case of circular polarization of the excitation pole, whether positive $(\Psi^{-} = 0)$ or negative $(\Psi^{+} = 0)$ , the pole of rotation revolves about a circular path in the same sense as the excitation pole. For $\Psi^{-}$ the two poles are always in phase. The radius of the circle described by the rotation pole equals that of the excitation pole at vanishingly low frequencies, is half as large at resonance, and vanishes at very high frequency (6.7.8). For $\Psi^{+}$ the poles are in phase

![](images/3895f0c13aa453e2363543a18e96cef4e958e3a8eed1a04e695fb95244d1ff4f.jpg)  
Fig. 6.3. The excitation pole oscillates with frequency $\sigma = 2\pi /T$ along a fixed longitude, occupying positions at times $0,\frac{1}{2} T,\frac{1}{2} T,\frac{1}{2} T$ as indicated on the central diagram. The elliptical path of the rotation pole is shown for $\sigma = \frac{1}{2}\sigma_0$ (left); $\sigma = 1\cdot 16\sigma_0 = 2\pi /(1$ year), (center); and $\sigma = 4\sigma_0$ (right), where $\sigma_0 = 2\pi /(1\cdot 2$ years) is the frequency of free nutation.

at low frequency and out of phase at high frequency, with an abrupt transition at resonance. The radius of the circle described by the rotation pole again equals that of the excitation pole at vanishingly low frequency, and is infinitesimal at vanishingly high frequency; at resonance it becomes infinite.

It is desirable to plot the amplitude of the wobble as a continuous function of frequency. The mean square polar excursions are

$$
\begin{array}{l} \langle | \Psi | ^ {2} \rangle = \left\langle \Psi_ {1} ^ {2} + \Psi_ {2} ^ {2} \right\rangle = | \Psi^ {+} | ^ {2} + | \Psi^ {-} | ^ {2} \bigg) \tag {679} \\ \langle | \mathbf {m} | ^ {2} \rangle = \langle m _ {1} ^ {2} + m _ {2} ^ {2} \rangle = | \mathbf {m} ^ {+} | ^ {2} + | \mathbf {m} ^ {-} | ^ {2}, \\ \end{array}
$$

where $\langle \rangle$ designates a time average. But according to (6.7.8)

$$
\mathbf {m} ^ {+} = \frac {\Psi^ {+}}{1 - s}, \quad \mathbf {m} ^ {-} = \frac {\Psi^ {-}}{1 + s},
$$

with $s = \sigma /\sigma_0$ . Hence

$$
\langle | \mathbf {m} | ^ {2} \rangle = \frac {(1 + s ^ {2}) \langle | \Psi | ^ {2} \rangle + 2 s (| \Psi^ {+} | ^ {2} - | \Psi^ {-} | ^ {2})}{(1 - s ^ {2}) ^ {2}}.
$$

The amplitude transmission ratio

$$
I = [ \langle | \mathbf {m} | ^ {2} \rangle / \langle | \Psi | ^ {2} \rangle ] ^ {\frac {1}{2}} \tag {6.7.10}
$$

has the following values for various special cases:

circular positive, $\Psi = \Psi^{+}$ 1- s

circular negative, $\Psi = \Psi^{-}$ 1 1+s

plane polarization, $|\Psi^{+}| = |\Psi^{-}|$ $\frac{\sqrt{1 + s^2}}{1 - s^2}$

random polarization, $\langle |\Psi |^2\rangle = 2\langle |\Psi^{+}|^2\rangle = 2\langle |\Psi^{-}|^2\rangle : \frac{\sqrt{1 + s^2}}{1 - s^2}$

The cases are illustrated in fig. 6.4. At vanishingly low frequency the transmission ratio is unity for all three cases. But it should be recalled that the transmission ratio has been defined with respect to the modified excitation function $\Psi$ . The asymptotic value for the corresponding ratio with respect to the (non-modified) excitation $\psi$ is $\sigma_r / \sigma_0 = 1 \cdot 40$ .

Perhaps the most likely geophysical case is one where the plane of polarization of the excitation function and its phase are randomly distributed. For this case, $I$ is given by the same formula as for plane polarization. This can be demonstrated as follows. The excitation and rotation poles describe wiggly paths. These can be frequency-analyzed, and for each spectral component the relationship is the one given by equation (6.7.9). Consider the record to be divided into

![](images/fd8efa02beca549d4ecf9134c73c2ec0f7bcea9a50e9131dcde92a880c62ffa5.jpg)  
Fig. 6.4. The amplitude transmission, $I$ , as a function of the dimensionless frequency, $s = \sigma / \sigma_0$ . Solid: circular (positive and negative) polarization; dashed: plane and random polarizations.

decades. Frequency components are computed, and an ensemble average is formed from all available decades. Since there is no preference for positive or negative circular polarization, $|\Psi^{+}|$ must equal $|\Psi^{-}|$ in the ensemble average. Equation (6.7.9) then reduces to the case of plane polarization.

# 8. The excitation function

Equations (6.1.5) give the total excitation, including rotational and load deformations. In all practical problems we are forced to evaluate the excitation, $\psi_{i}$ , as if the Earth were rigid, and to allow for the secondary deformation by way of the transfer function.

With this understanding (6.1.5) can be used as written, with $\phi_{i}$ replaced by $\psi_{i}$ .

Equations (6.1.5) are well suited for computing the excitation function whenever changes in relative angular momentum are well separated from changes in the products of inertia. This usually arises whenever one or the other is zero. For example, a flywheel fixed to the ground and rotating at a variable rate gives changes in the relative angular momentum, but not in inertia. In the case of a melting icecap the angular momentum of the flowing water is negligible, but changes in inertia may not be.

Equation (6.1.5) is not convenient if it is desired to separate explicitly the effects arising due to changes in the distribution of matter from those due to relative motion. The reason is that $\dot{c}_{ij}$ and $h_i$ both involve relative motion; moreover, these are of the same order. Equations in 'separated form' have been used by Munk and Groves (1952) to estimate the annual wobble induced by winds and ocean currents.

Equations (6.1.5) can be written

$$
\left. \begin{array}{r l} & {\Omega^ {2} (C - A) \phi} \\ & {\quad = \int_ {V} \Delta \rho \textbf {F} (\text {m a t t e r})   \mathrm {d} V + \int_ {V} \rho \textbf {F} (\text {m o t i o n})   \mathrm {d} V + \textbf {F} (\text {t o r q u e})} \\ & {\Omega^ {2} C \phi_ {3}} \\ & {\quad = \int_ {V} \Delta \rho F _ {3} (\text {m a t t e r})   \mathrm {d} V + \int_ {V} \rho F _ {3} (\text {m o t i o n})   \mathrm {d} V + F _ {3} (\text {t o r q u e})} \end{array} \right\},
$$

where $\Delta \rho (x_i,t)$ is the density departure associated with the excitation functions $\phi_{k}(t)$ , and where

matter $F_{1} = -\Omega^{2}x_{1}x_{3}, F_{2} = -\Omega^{2}x_{2}x_{3}, F_{3} = -\Omega^{2}(x_{1}^{2} + x_{2}^{2})$

$\begin{array}{r}\mathbf{\nabla}F_{1} = -2\Omega x_{3}u_{2} + x_{3}\dot{u}_{1} - x_{1}\dot{u}_{3}\\ F_{2} = 2\Omega x_{3}u_{1} + x_{3}\dot{u}_{2} - x_{2}\dot{u}_{3}\\ F_{3} = \Omega (-x_{1}u_{2} + x_{2}u_{1}) \end{array}$ motion

torque $F_{1} = -L_{2}, F_{2} = L_{1}, F_{3} = \Omega \int_{0}^{t}L_{3}\mathrm{d}t$

are functions depending on distribution of matter, relative motion (velocity and acceleration), and on torque, respectively. Spherical coordinates are often convenient. Let $u_{\lambda}, u_{\theta}, u_{r}$ designate eastward,

southward and upward components of velocity, and $\mathrm{d}V = r^2\sin \theta$ $\mathrm{d}\pmb {r}\mathrm{d}\pmb {\theta}\mathrm{d}\lambda$ the differential volume. Then

matter $\left\{ \begin{array}{l}F_{1} = -r^{2}\Omega^{2}\sin \theta \cos \theta \cos \lambda ,F_{2} = -r^{2}\Omega^{2}\sin \theta \cos \theta \sin \lambda ,\\ F_{3} = -r^{2}\Omega^{2}\sin^{2}\theta \end{array} \right.$

\[
\begin{array}{l}
F_{1} = -2\Omega r \cos \theta (u_{\lambda} \cos \lambda + u_{\theta} \cos \theta \sin \lambda + u_{r} \sin \theta \sin \lambda) \\
+ r(-\dot{u}_{\lambda} \cos \theta \sin \lambda + \dot{u}_{\theta} \cos \lambda) \\
F_{2} = 2\Omega r \cos \theta (-u_{\lambda} \sin \lambda + u_{\theta} \cos \theta \cos \lambda + u_{r} \sin \theta \cos \lambda) \\
+ r(\dot{u}_{\lambda} \cos \theta \cos \lambda + \dot{u}_{\theta} \sin \lambda) \\
F_{3} = -\Omega r \sin \theta u_{\lambda}.
\end{array}
\]

![](images/bd7ca7c8bb571434a5077ef009a71cd3f03caced5d6f840c3edfdc209209299f.jpg)  
Fig. 6.5. The stress component, $p_{mm}$ , normal to the geoid, has a component $p_{mm}(\Omega^2 a / g)\sin \theta$ in the plane normal to the $x_3$ -axis.

The torque can be written as a sum of two terms:

$$
L _ {i} = \int_ {V} \rho \varepsilon_ {i j k} x _ {j} f _ {k} d V + \int_ {S} \varepsilon_ {i j k} x _ {j} p _ {k m} n _ {m} d S.
$$

The first part is due to a body force $f_{k}$ ; for example, gravitational attraction of the equatorial bulge. The second term is due to surface stresses $p_{km}$ in the direction $k$ on a surface element normal to $n_{m}$ . As a special case we consider a smooth geoid whose surface is everywhere normal to local gravity. The radial components of surface stress do not produce a torque. The non-radial components (fig. 6.5) are

$$
\begin{array}{l} p _ {1 m} \approx p _ {\theta m} \cos \theta \cos \lambda - p _ {\lambda m} \sin \lambda + p _ {m m} (\Omega^ {2} a / g) \sin \theta \cos \lambda \\ p _ {2 m} \approx p _ {\theta m} \cos \theta \sin \lambda + p _ {\lambda m} \cos \lambda + p _ {m m} (\Omega^ {2} a / g) \sin \theta \sin \lambda \\ p _ {3 m} \approx - p _ {\theta m} \sin \theta \end{array} ,
$$

where $p_{mm}$ is the component of stress along the normal to the geoid (the summation convention does not apply here). Hence

$$
\left. \begin{array}{l} L _ {1} = a \int_ {S} \left[ - p _ {\theta m} \sin \lambda - p _ {\lambda m} \cos \theta \cos \lambda \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad - p _ {m m} (\Omega^ {2} a / g) \sin \theta \cos \theta \sin \lambda ]   d S \\ L _ {2} = a \int_ {S} \left[ p _ {\theta m} \cos \lambda - p _ {\lambda m} \cos \theta \sin \lambda \right. \\ \qquad \qquad \qquad \qquad + p _ {m m} (\Omega^ {2} a / g) \sin \theta \cos \theta \cos \lambda ]   d S \\ L _ {3} = a \int_ {S} \left[ p _ {\lambda m} \sin \theta \right]   d S \end{array} \right\}.
$$

A graphical summary of the effect of various events on the excitation pole is given in fig. 6.6. It can be seen that a local counterclockwise circulation has a similar effect as a local defect of mass; both of these circumstances are characteristic of cyclones in the northern hemisphere.

![](images/6cdf68988f58bbe99e91179da42f2e4c0e600d127f9d8873bf3b5de7fcd42636.jpg)  
Fig. 6.6. Disturbances that will place the excitation pole on the meridian of Greenwich $(\psi_{1}$ positive, $\psi_{1} = 0)$ . Perturbations in inertia due to a mass $m$ at $180^{\circ}$ has this effect, as will a positive rate of increase $\mathrm{dm} / \mathrm{dt}$ at $270^{\circ}$ east. The effect of relative angular momentum, h (from a horizontal vortex), and of its time rate of change, $\mathrm{dh} / \mathrm{dt}$ , are also shown. Motion toward $-x_{2}$ and stress toward $-x_{1}$ displace the excitation pole toward $x_{1}$ , regardless in which quarter of the globe they occur.

# 9. Some idealized illustrations

Consider a merry-go-round rotating at a variable angular velocity on the Greenwich meridian at the equator. Then $h_2 = 0$ , $h_3 = 0$ and from (6.1.5)

$$
\psi_ {1} = \frac {h _ {1}}{\Omega (C - A)}, \quad \psi_ {2} = - \frac {\dot {h} _ {1}}{\Omega^ {2} (C - A)}, \quad \psi_ {3} = 0.
$$

This is the (non-modified) excitation computed from the point of view of the momentum approach.

The torque exerted on the support consists of the d'Alembert torque, $L_{1} = -\dot{h}_{1}$ , associated with the angular acceleration of the merry-go-round, and the gyroscopic torque $L_{2} = -\Omega h_{1}$ . When these components are substituted into (6.1.5) the foregoing expressions for $\psi_{i}$ result, as of course they must.

Here the distinction between the momentum approach and torque approach is trivial. In geophysical cases it is not. Two investigations concerning the effect of motion in the core on the l.o.d., one using the momentum approach, the other the torque approach, obtained results that differ by a factor $10^{5}$ ( $\S 11.12$ ). The choice is essentially a matter of instrumentation: is it easier to measure the variable velocity of the merry-go-round, or the torque exerted on the foundation?

As a second example, consider the wobble induced by a hula dancer of mass $m$ on the geographic north pole, moving her center of mass by an amount $l_{1} = b \sin \sigma t$ (not necessarily small) along the meridian of Greenwich. Then $c_{23} = 0$ , $h_{1} = 0$ , and

$$
c _ {1 3} = - m a b \sin \sigma t, \quad h _ {2} = m a b \sigma \cos \sigma t.
$$

The excitation function is given by

$$
\psi_ {1} = \frac {m a b}{C - A} \left(1 - \frac {\sigma^ {2}}{\Omega^ {2}}\right) \sin \sigma t, \quad \psi_ {2} = \frac {2 m a b}{C - A} \frac {\sigma}{\Omega} \cos \sigma t. \tag {6.9.1}
$$

The example illustrates two points. The three terms in (6.9.1) are in the ratio $1:(\sigma /\Omega):((\sigma /\Omega)^2$ ; for excitation frequencies small compared to $\Omega$ the term depending on the distribution of matter is dominant. Secondly, $\dot{c}_{13}$ and $h_2$ contribute equally to $\psi_{2}$ , and this illustrates our remark that in (6.1.5) the effects of distribution in matter are not well separated from those due to relative motion. Here the

wobble has been derived from considerations involving angular momentum of the Earth-dancer system. We can obtain identical results by considering the dancer as outside the planet Earth, and exerting a variable torque on the Earth by virtue of her motion.

As a third example, we compute the effect of firing a cannon ball of mass $m$ with sufficient speed to escape the Earth's gravitational field. Suppose the cannon is located on the Greenwich meridian at some colatitude $\theta$ , firing south along a tangent to the surface. Then $\lambda = 0$ , $u_{\lambda} = 0$ , $u_{r} = 0$ , and

$$
c _ {1 3} = - m a ^ {2} \sin \theta \cos \theta H (t), \quad \dot {c} _ {1 3} = - m a ^ {2} \sin \theta \cos \theta \delta (t).
$$

The quantity $\rho u_{\theta}$ is zero just before the firing, when the resting cannon ball is part of the planet Earth, and zero after the firing when it is no longer a part. Hence

$$
\dot {h} _ {2} = m a u _ {\theta} \delta (t).
$$

Substituting term by term, the excitation function becomes

$$
\psi_ {1} = - \frac {m a ^ {2} \sin \theta \cos \theta}{C - A} H (t) + \frac {m a u _ {\theta}}{\Omega^ {2} (C - A)} \delta (t);
$$

$$
\psi_ {2} = \frac {m a ^ {2} \sin \theta \cos \theta}{\Omega (C - A)} \delta (t).
$$

The ratio of $\psi_{2}$ to the second term in $\psi_{1}$ is $\Omega a$ sin $\theta$ cos $\theta /u_{\theta}$ , and is small since the escape velocity $u_{\theta} = 11\cdot 3\mathrm{km~sec}^{-1}$ far exceeds $\Omega a = 0\cdot 46\mathrm{km~sec}^{-1}$ . Accordingly $\psi_{2}$ can be neglected. Each term in $\psi_{1}$ is associated with a circular motion of the pole of rotation. For the term containing $H(t)$ the pole revolves with a radius $R$ about a position displaced by $R$ from its original position; for the spike function the pole revolves with radius $R^{\prime}$ about the original position. According to (6.7.2, 3)

$$
R = \frac {m a ^ {2} \sin \theta \cos \theta}{(C - A)}, \quad R ^ {\prime} = \frac {\sigma_ {0} m u _ {\theta} a}{\Omega^ {2} (C - A)}.
$$

The ratio

$$
\frac {R}{R ^ {\prime}} = \frac {a \Omega}{u _ {\theta}} \frac {\Omega}{\sigma_ {0}} \sin \theta \cos \theta = (0. 0 4 1) (4 2 0) \sin \theta \cos \theta = 1 7 \sin \theta \cos \theta
$$

is large except very near the equator and the poles. Hence if we are to fire a projectile at escape velocity the most effective means of

moving the pole is to place the cannon at $\theta = 45^{\circ}$ and to fire the largest possible projectile that can be removed from the Earth's gravitational field.* But then it is easier and equally effective to fire the projectile to the equator (or poles), and there are cheaper ways of moving matter than by ballistics. The polar displacement (in radians) is of the order of the ratio of the displaced mass to the mass of the equatorial bulge, and presumably small.

* Jules Verne has given a detailed discussion of turning the Earth by such means in an inaccessible book, 'Sens dessus dessous' (Verne, 1889, pp. 152, 187, 200) and we are indebted to Monsieur I. H. P. Eyries of the Service Central Hydrographique for tracing this book in the French National Library. Jules Verne reports great interest on the part of le Gouvernement de Washington in a report by the engineers of the 'North Polar Practical Association' to fire a projectile of 180,000 tons in order to displace the pole $23^{\circ}$ and so to remove the obliquity of the ecliptic. Subsequently the French engineer Pierdeux discovered that the Earth's equatorial bulge had been neglected in the original calculations and, when this is allowed for, he obtained a polar displacement of 3 microns. Setting $m = 1 \cdot 8 \times 10^{11} \mathrm{~g}$ and $\theta = 45^{\circ}$ gives

$$
R a = \frac {\frac {1}{2} m a ^ {3}}{C - A} = 0. 1 \text {m i c r o n},
$$

or one thirtieth of Pierdeux's result. The story has a modern sequel. During the 1956 U.S. Presidential election the vice-presidential candidate, Senator Estes Kefauver, reported that the Earth's axis would be displaced by $10^{\circ}$ as a result of hydrogen bomb tests. Suppose an energy of $10^{24}$ ergs could be available to fire a projectile at escape velocity. Its mass is $10^{24} / \frac{1}{2} u^3 = 1\cdot 6\times 10^{12}\mathrm{g},$ or roughly ten times that reported by Jules Verne, and the resulting displacement is then 1 micron. After seventy years, the government in Washington still refuses to recognize the existence of the equatorial bulge.
