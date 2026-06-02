# CHAPTER 3

# DYNAMICS*

# 1. Fundamental equations

The Eulerian equations of motion in a coordinate system $x_{i}$ ( $i = 1, 2, 3$ ), rotating with angular velocity $\omega_{i}$ relative to coordinates $X_{i}$ fixed in space and coinciding with $x_{i}$ for the moment, are

$$
L _ {i} = \frac {\mathrm {d} H _ {i}}{\mathrm {d} t} + \varepsilon_ {i j k} \omega_ {j} H _ {k}. \tag {3.1.1}
$$

$L_{i}$ are the components of torque, $H_{i}$ those of angular momentum. $\varepsilon_{ijk}$ is the 'alternating' tensor, defined by the following properties:

$$
\left. \begin{array}{l l} \varepsilon_ {i j k} = & 0 \text {i f a n y t w o s u b s c r i p t s a r e e q u a l ,} \quad i = j, i = k, j = k, \\ = + 1 \text {i f s u b s c r i p t s a r e i n e v e n o r d e r ,} & 1, 2, 3, 1, 2 \dots , \\ = - 1 \text {i f s u b s c r i p t s a r e i n o d d o r d e r ,} & 1, 3, 2, 1, 3 \dots . \end{array} \right\} \tag {3.1.2}
$$

By the usual summation convention, in any expression containing a repeated suffix, that suffix is to be given all possible values and the results then added.

Equations (3.1.1) are quite general. They refer, for example, to a system of particles moving among themselves. It is convenient to separate angular momentum into two parts:

$$
H _ {i} = C _ {i j} (t) \omega_ {j} + h _ {i} (t), \tag {3.1.3}
$$

where $C_{ij} = \int_V\rho (x_kx_k\delta_{ij} - x_ix_j)\mathrm{d}V$ (3.1.4)

is the (variable) tensor of inertia for matter contained in a volume $V$ , and $\delta_{ij}$ is the Kronecker delta (or substitution tensor), with the properties $\delta_{ij} = 1$ if $i = j$ , $\delta_{ij} = 0$ if $i \neq j$ . The second part of (3.1.3) designates a relative angular momentum

$$
h _ {i} = \int_ {V} \rho \varepsilon_ {i j k} x _ {j} u _ {k} \mathrm {d} V \tag {3.1.5}
$$

* For a more complete treatment the reader is referred to the classic works of v. Oppolzer (1886), Tisserand (1891), and Klein and Sommerfeld (1903). A treatment by Woolard (1953) has been found helpful.

due to motion $u_{i}$ relative to the $x_{i}$ -system. Substituting (3.1.3) into (3.1.1) leads to

$$
L _ {i} = \frac {\mathrm {d}}{\mathrm {d} t} \left(C _ {i j} \omega_ {j} + h _ {i}\right) + \varepsilon_ {i j k} \omega_ {j} \left(C _ {k l} \omega_ {l} + h _ {k}\right). \tag {3.1.6}
$$

All subsequent inquiries concerning irregularities in rotation take the form of special solutions to (3.1.6). This equation was given by Liouville in 1858 (Routh, 1905: §22), and it will be referred to as the Liouville equation.

# 2. Frames of reference

Routh (1905, § 22) and other textbooks distinguish between the rotating reference-axes in the Eulerian equations (3.1.1) and the 'body axes' from which changes in the body can be described (3.1.4, 5). The two rotating axes can be combined without loss of generality, as we have done, at the expense (possibly) of not making the best use of the symmetry of the situation.

The choice of the rotating $x_{i}$ -system is altogether arbitrary. It could, for example, rotate at some rate in a sense opposite to the Earth's rotation. For convenience the coordinate axes must now be attached to the Earth in some way. In most papers on the subject the coordinate system is said to rotate 'with the Earth'. If the Earth were rigid, there would be no further difficulty. Winds, ocean currents, and the fluid core introduce complications. To get around this difficulty the axes can be attached to the 'solid' Earth. However, there are tidal distortions and, for processes on a geologic timescale, convective motion in the mantle has been postulated; in all events we are faced with relative motion of different parts of the crust. Such motion is known to take place along geologic faults and has been postulated by Wegener on a grandiose scale as a drift of continents with respect to one another.

Clearly we require a set of rigid axes that are kinematically defined so as not to impose any restraints on the deforming Earth. There are a number of possible choices.

(1) Tisserand's mean axes of body are defined so that $h_i = 0$ . Thus if winds, ocean currents, and all other relative motion ceased, these axes would rotate with the resulting frozen body. An alternate

and equivalent definition is instructive. For a rigid body rotating with angular velocity $\omega_{i}$ the velocity of any particle in space is $(\mathrm{d}X_{i} / \mathrm{d}t) = \varepsilon_{ijk}\omega_{j}X_{k}$ . For a deformable body we can select some value of $\omega_{i}$ , say $\tilde{\omega}_{i}$ , which makes

$$
\int_ {V} \rho \left(\frac {\mathrm {d} X _ {i}}{\mathrm {d} t} - \varepsilon_ {i j k} \omega_ {j} X _ {k}\right) ^ {2} \mathrm {d} V
$$

a minimum. For the $\bar{\omega}_{i}$ -axes it can be shown that $h_{i} = 0$ , so that $\bar{\omega}_{i}$ is the angular velocity of the mean axes. Jeffreys (1952, p. 206) refers his calculations to the mean axes.

(2) The principal axes, or axes of figure, are defined so that the products of inertia $C_{ii}, i \neq j$ , vanish. Darwin (1877) chose the principal axes for his treatment of polar wandering.

The derivation in §3.1 refers to any set of rigid rotating axes, and thus includes the mean axes and principal axes as special cases. The conditions $h_i = 0$ and $C_{ij} = 0$ , $i \neq j$ , respectively, lead to considerable simplifications of (3.1.6). These are the obvious choices for mathematical simplicity. But there are disadvantages to these fundamental axes. Winds and other relative motion rotate the mean axes slowly relative to the observatories, and it may be necessary to correct the observed values. The principal axes also shift relative to the observatories. Moreover, Jeffreys's choice of the mean axes makes it awkward to include the effects of relative motion, and he does ignore such effects. The variable angular momentum of the atmosphere shifts the mean axes relative to the equatorial bulge and accordingly would produce variations in $C_{ij}$ even if the Earth were rigid. We have found it expedient to use

(3) the 'geographic' axes which are attached in a 'prescribed way' to the observatories. There are difficulties due to relative motion of the observatories. For many problems the relative motion can be neglected. Stations of the International Latitude Service have moved rather well together, the attempt having been made to locate them away from active faults. If the relative motion is not negligible, then we choose a set of rigid axes which are attached in some prescribed way to the observatories. Geophysical observations, astronomical observation, the relative motion of the observatories, equations (3.1.1-6), everything is referred to these axes. We may wish to

contemplate a least-squares fit to stakes driven in the ground at suitable intervals over the whole Earth, a procedure that avoids a bias from the positioning of observatories and gets rid of tidal distortions to a first order.

For all three systems only the motion of the axes has been defined. The choice remains of determining the position. It is convenient to place the origin at the Earth's center of mass so that $\int \rho x_{i} \, \mathrm{d}V$ vanishes, to align the $x_{3}$ -axis reasonably well with the axis of figure (or rotation), to draw the $x_{1}$ -axis through the meridian of Greenwich, and the $x_{2}$ -axis towards $90^{\circ}$ east of Greenwich.

# 3. Further discussion of the Liouville equation

The reader will find references to half a dozen papers where incorrect results have been obtained because of the misinterpretation or omission of terms in the fundamental relation (3.1.6). To avoid such pitfalls, it may be worth while to discuss further what the terms mean and what they do not mean.

(1) $L_{i}$ is an exterior torque acting on the body contained within the volume $V$ . The surface enclosing this volume can be chosen at will. For example, in considering the effect of winds we may exclude the atmosphere, in which case there will be an exterior torque resulting from wind stress; or we may include the entire planet Earth and set $L_{i} = 0$ . The torque approach and the momentum approach lead, of course, to identical results (see §6.9 for some sample calculations), the choice depending on instrumentation: is it easier to measure the wind stress or the angular momentum of the atmosphere?   
(2) $L_{i}$ are the components of torque along the rotating axes $x_{i}$ . The torque exerted by steady winds blowing along a fixed longitude has components that do not vary in time, $L_{i} \neq f(t)$ . A torque fixed in space, on the other hand, produces components that do vary in time with diurnal frequency $\Omega$ . For example, radiation pressure from a fixed star must differ slightly over the Earth's two hemispheres, and the resulting torque will have variable components such as $L_{1} = \cos \Omega t$ , $L_{2} = \sin \Omega t$ .   
(3) The derivation has referred only to a time 0 when the rotating $x_{i}$ -system and the fixed $X_{i}$ -system coincided for the moment. At

this instant the components $L_{i}, h_{i}$ , and $C_{ij}$ in the $x_{i}$ and $X_{i}$ -systems are the same, and the derivation can refer to the inertial frame of reference $X_{i}$ in the usual way. But for any subsequent time, $t'$ , the derivation is identical provided a fixed $X_{i}'$ -system is chosen which coincides with the rotating $x_{i}$ -system at time $t'$ . With the understanding that components of torque, momentum, and inertia are always taken along the $x_{i}$ -system, equations (3.1.6) are valid for all times.

(4) The interpretation of $\mathrm{d}C_{ij} / \mathrm{d}t$ and $\mathrm{d}h_i / \mathrm{d}t$ requires consideration. It is easier, and safer, first to perform the integrations (3.1.4, 5) inherent in the definitions of $C_{ij}$ and $h_i$ , and then to differentiate the time-dependent integrals. As previously stated, the integrals are taken over a volume enclosed by some material surface $S$ . If the differentiation is to be performed first, then certain complications arise due to distortion of $S$ with time. If the enclosing surface is fixed relative to the reference coordinates, $S = S(x_i)$ , one must allow for the flux of inertia and relative angular momentum through the boundary $S$ .   
(5) The quantities $h_i$ and $C_{ij}$ depend on the fields of density $\rho(x_k, t)$ and relative velocity $u_i(x_k, t)$ . In our equations $\rho$ and $u_i$ appear as independent variables. There are, of course, restraints imposed by the conservation of mass, momentum and energy and by the equations of state. For example, there can be no change in the density field $\rho(t)$ unless there is some motion $u_i(t)$ . It would be possible to transform the equations so that the conservation principles are automatically satisfied. We have taken the point of view that for each geophysical application the fields of $\rho$ and $u_i$ are to be specified in accordance with the proper physical laws, but there is nothing to prevent the reader from working out examples which imply, for example, creation and destruction of matter.   
(6) With $L_{i}$ , $h_{i}$ , and $C_{ij}$ thus specified, the equations can be solved for the angular velocity $\omega_{i}(t)$ of the reference system $x_{i}$ relative to the fixed system $X_{i}$ . Let $y_{i}$ designate a coordinate system rotating with the same angular velocity $\Omega = (\omega_{i}\omega_{i})^{\frac{1}{2}}$ as the $x_{i}$ -system, but with $y_{3}$ directed always along the axis of instantaneous rotation. Then

$$
x _ {i} = \frac {\omega_ {i}}{\Omega} y _ {3}, \tag {3.3.1}
$$

so that $\omega_{s} / \Omega$ are the direction cosines of the rotation axes relative to the reference axes. In all problems except polar wandering we align the $x_{3}$ -axis nearly parallel to the $y_{3}$ -axis so that $\mathrm{d}\omega_3 / \mathrm{d}t$ is nearly the acceleration in the diurnal rotation and $\omega_{1},\omega_{2}$ the components of wobble.
