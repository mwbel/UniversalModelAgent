# CHAPTER 4

# DEFORMATION

The real difficulty of our subject concerns the deformation of the Earth under prescribed stresses. For problems involving wobble with periods of the order of one year or shorter, it is customary to allow for a purely elastic deformation of the Earth by the introduction of the appropriate Love numbers. The next chapter is devoted to this topic. By this choice of notation various problems can be solved with considerable ease; but this ease is deceptive inasmuch as it hides the fact that the corresponding problem in elasticity had to be first solved to make the Love number available. For the damping of the Chandler wobble and problems involving a longer time-scale than one year, the importance of the deformation problem becomes explicit, and some deviation from perfect elasticity in the Earth's mantle may have to be allowed for. The choice of a meaningful anelastic stress-strain model involves much speculation, to say the least. Precise solutions are hardly possible and probably not worthwhile at the present state of the art. But some general statements concerning rotational stability can be made from energy considerations.

The problem of stress and strain plagued Kelvin and George Darwin. Kelvin assumed the Earth could be treated as an elastic body even for long-period deformations, while Darwin assumed that the Earth behaves plastically, even for small stresses. Today the situation is identical to that of 1900, and proponents of the Darwin and of the Kelvin view can be found. There are few problems in geophysics in which less progress has been made.

# 1. Stress, strain and deformation

A fiber is stretched by the application of an external force. On release of the external force the fiber may return at once to its original length, or it may return very slowly, or it may assume a new, greater, length. If the fiber returns at once to its initial length on the release of the external stress, then the response is termed

elastic. Whether or not a given material responds elastically to a given external force depends not only on the nature of the material but also on the magnitude of the external force and possibly on its duration.

In discussing the general problem of the deformation of solids, it is essential to distinguish between the elastic (or recoverable) strain and the total deformation (Eckart, 1948). In one-dimensional problems, such as the deformation of a fiber by an external force applied parallel to its length, the elastic strain $\varepsilon$ is defined as

$$
\varepsilon = \frac {s - g}{g},
$$

where $s$ is the actual distance between two points of the fiber, and $g$ is the distance between the same two points at an instant after removal of external forces.

The rate of change of one-dimensional elastic strain is

$$
\frac {\mathrm {d} \varepsilon}{\mathrm {d} t} = (1 + \varepsilon) \left(\frac {1}{s} \frac {\mathrm {d} s}{\mathrm {d} t} - \frac {1}{g} \frac {\mathrm {d} g}{\mathrm {d} t}\right). \tag {4.1.1}
$$

$\frac{\mathrm{d}s}{\mathrm{d}t}$ is the actual rate at which two points in the fiber move apart. $\frac{\mathrm{d}g}{\mathrm{d}t}$ is the rate of change of the length between the two points at zero external force. $\frac{1}{s}\frac{\mathrm{d}s}{\mathrm{d}t}$ is termed the rate of (total) deformation while $\frac{1}{g}\frac{\mathrm{d}g}{\mathrm{d}t}$ is the rate of anelastic deformation. The rate of deformation nearly equals the rate of elastic strain, provided the strain and the rate of anelastic deformation are small:

$$
\frac {\mathrm {d} \varepsilon}{\mathrm {d} t} \approx \frac {1}{s} \frac {\mathrm {d} s}{\mathrm {d} t} \quad \text {f o r} \quad \left\{ \begin{array}{l} \varepsilon \ll 1 \\ \frac {1}{g} \frac {\mathrm {d} g}{\mathrm {d} t} \ll \frac {1}{s} \frac {\mathrm {d} s}{\mathrm {d} t}. \end{array} \right.
$$

The classical theory of infinitesimal elasticity is based on these two assumptions.

The rate of elastic strain (4.1.1) vanishes if the rates of total deformation and of anelastic deformation both vanish, or if the rate of total deformation equals the rate of anelastic deformation:

$$
\frac {1}{s} \frac {\mathrm {d} s}{\mathrm {d} t} = \frac {1}{g} \frac {\mathrm {d} g}{\mathrm {d} t}.
$$

In the latter case the length of the fiber changes at a finite rate, yet the elastic strain remains constant. The rate of total deformation may vanish so that there is no motion, yet the elastic strain may change provided the rate of anelastic deformation is finite.

The notion of the anelastic rate of deformation can be carried over into three dimensions (Eckart, 1948; Knopoff and MacDonald, 1958). The relations are relatively simple if the elastic strains are small compared with unity. In Earth problems the total elastic strain is often very large because of high hydrostatic pressure. However, the large total strain can be thought of as made up of two parts, a large initial strain due to self attraction of the material elements and a small strain due to small changes in the forces acting on the system. We will be interested only in the effect of the small superimposed strains. Since the concept of total deformation plays no role in the development, there is no limit on the magnitude of the deformation. We require only that the superimposed elastic strain be small.

In three dimensions the total rate of deformation $d_{ij}$ is defined by

$$
d _ {i j} = \frac {1}{2} \left(\frac {\partial u _ {i}}{\partial x _ {j}} + \frac {\partial u _ {j}}{\partial x _ {i}}\right),
$$

where $u_{i}$ are the velocity components and $d_{ij}$ is a symmetric tensor. The elastic strain is defined by

$$
\varepsilon_ {i j} = \frac {1}{2} (\delta_ {i j} - g _ {i j}),
$$

where $g_{ij}$ is the metric tensor of the material in the relaxed state, free from external stress. The rate of anelastic deformation $a_{ij}$ is then

$$
a _ {i j} = d _ {i j} - \frac {\mathrm {d} \varepsilon_ {i j}}{\mathrm {d} t}
$$

provided the elastic strains are small. A material is termed anelastic if $a_{ij} \neq 0$ .

The total stress $p_{ij}$ acting on matter within the Earth consists of three parts:

$$
p _ {i j} = - p \delta_ {i j} + \tau_ {i j} + s _ {i j}.
$$

$p$ is the hydrostatic pressure; $\tau_{ij}$ is the elastic stress, given by

$$
\tau_ {i j} = \lambda \varepsilon_ {k k} \delta_ {i j} + 2 \mu \varepsilon_ {i j},
$$

where $\lambda$ and $\mu$ are elastic constants; $s_{ij}$ is the frictional stress. The form of $s_{ij}$ depends on the frictional model. For example, in a Kelvin-Voigt body (§ 5.11) $s_{ij}$ is assumed to depend on the rate of deformation, according to

$$
s _ {i j} = \lambda_ {\mathbf {K} - \nu} d _ {k k} \delta_ {i j} + 2 \mu_ {\mathbf {K} - \nu} d _ {i j}.
$$

The only stress acting on an Earth in hydrostatic equilibrium is the hydrostatic pressure. The magnitude of the pressure at any point within the Earth is determined by the distribution of density within the Earth. In all problems we will assume the Earth initially in hydrostatic equilibrium, $p_{ij} = -p_0\delta_{ij}$ , and then examine small deviations from this equilibrium condition:

$$
p _ {i j} = - p _ {0} \delta_ {i j} + \lambda \varepsilon_ {k k} \delta_ {i j} + 2 \mu \varepsilon_ {i j} + s _ {i j}.
$$

The description of the relation between stress and deformation is incomplete unless we describe the dependence of the rate of anelastic deformation on the stress. The exact nature of this dependence is not at all clear. There are, however, certain limiting conditions imposed by experimental studies. There is no anelastic deformation resulting from a hydrostatic stress, provided the material is homogeneous (Bridgman, 1949, p. 149). The rate of anelastic deformation should thus be independent of the hydrostatic pressure. If the applied stresses are non-hydrostatic, then behavior of the material depends on the magnitude of the stress differences. For stress differences below a critical value (ranging in rocks from $10^{2}$ to $10^{4}$ bars) crystalline solids behave elastically in short-time laboratory experiments. Stresses exceeding critical stress difference lead to fracture or plastic flow. The response of crystalline materials to small stresses imposed for long periods of time is a subject of some controversy, and the existence of a finite strength for such prolonged stresses cannot be considered as established by experiment.

In a Maxwell body (§ 5.11) the relation between the rate of anelastic deformation and the elastic stress is

$$
a _ {i j} = \lambda_ {M} \tau_ {k k} \delta_ {i j} + 2 \mu_ {M} \tau_ {i j}.
$$

The experimentally imposed requirement that $a_{ii} = 0$ results in $\lambda_{M} = -\frac{2}{3}\mu_{M}$ , hence

$$
a _ {i j} = 2 \mu_ {M} \left(\tau_ {i j} - \frac {1}{3} \tau_ {k k} \delta_ {i j}\right). \tag {4.1.2}
$$

Such a relation implies that permanent or plastic deformation is possible even for vanishingly small non-hydrostatic stresses. If the material shows finite strength, (4.1.2) is valid only for stress differences exceeding some critical value. We adopt the convention of labeling the three principal stresses of the tensor $\tau_{ij}$ as $\tau_1, \tau_2, \tau_3$ , with $\tau_1 \leqslant \tau_2 \leqslant \tau_3$ . For materials with finite strength $\tau_0$ , the deformation tensor $a_{ij}$ is given by (4.1.2) only if $|\tau_3 - \tau_1| > \tau_0$ ; otherwise $a_{ij} = 0$ . This simple criterion will be sufficient for the problems discussed in this book. Many other criteria are possible (Nadai, 1950).

# 2. Energy and stability

The kinetic energy of the planet Earth is

$$
K = \frac {1}{2} \int_ {V} \rho U _ {i} U _ {i} \mathrm {d} V,
$$

where $U_{i}$ are the components of the velocity relative to the fixed space-axes $X_{i}$ and $V$ is a volume enclosing that part of the universe which we regard as the Earth. In terms of the components of velocity $u_{i}$ relative to the rotating axes $x_{i}$ , the kinetic energy is

$$
\begin{array}{l} K = \frac {1}{2} \int_ {V} \rho u _ {i} u _ {i} \mathrm {d} V + \int_ {V} u _ {i} \varepsilon_ {i j k} \omega_ {j} x _ {k} \mathrm {d} V + \frac {1}{2} \int_ {V} \rho [ \omega_ {l} ^ {2} x _ {l} ^ {2} - (\omega_ {l} x _ {l}) ^ {2} ] \mathrm {d} V \\ = k + \omega_ {i} h _ {i} + \frac {1}{2} H _ {i} H _ {j} \left(C _ {i j}\right) ^ {- 1}, \tag {4.2.1} \\ \end{array}
$$

where $C_{ik}(C_{kj})^{-1} = \delta_{ij}$ . In stability problems it is convenient to refer to Tisserand's axes (§ 3.2), for then $\omega_i h_i$ vanishes and all the energy of relative motion is contained in the relative kinetic energy $k$ , a positive definite quantity. A growth of a disturbance will manifest itself in the increase of $k$ . If the Earth can be considered free from the action of external forces, the total angular momentum is constant, and the total kinetic energy can change only through changes in $k$ and in the moment of inertia $C_{ij}$ .

The principle of conservation of energy applied to a rotating body free of internal heat sources and thermally and mechanically isolated from the rest of the universe leads to

$$
\frac {\mathrm {d}}{\mathrm {d} t} (k + W) = - \int_ {V} \tau_ {i j} a _ {i j} \mathrm {d} V - \int_ {V} s _ {i j} \mathrm {d} _ {i j} \mathrm {d} V, \tag {4.2.2}
$$

where $W = H_{i}H_{i}(C_{ij})^{-1} + P + E$

and $P$ is the potential energy associated with body forces, $E$ the elastic energy. The rate of change of elastic energy consists of two parts:

$$
\frac {\mathrm {d} E}{\mathrm {d} t} = - \int_ {V} \frac {1}{\rho} p _ {0} \frac {\mathrm {d} p}{\mathrm {d} t} \mathrm {d} V + \int_ {V} \tau_ {i j} \frac {\mathrm {d} \varepsilon_ {i j}}{\mathrm {d} t} \mathrm {d} V.
$$

The first part designates the effect of compression; the second part, the effect of the perturbation stresses $\tau_{ij}$ .

The terms on the right of (4.2.2) represent the energy dissipated by anelastic deformation and frictional resistance, respectively. By the second law of thermodynamics both dissipation terms are positive, thus

$$
\frac {\mathrm {d}}{\mathrm {d} t} (k + W) \leqslant 0.
$$

The stability characteristics of an anelastic rotating body are contained in this equation. We give the following results without proof.

(1) A freely rotating solid, free from frictional stresses and rotating with an angular velocity such that the maximum stress difference is less than the strength of the solid. Then $s_{ij} = 0$ , $a_{ij} = 0$ ; hence $\frac{\mathrm{d}}{\mathrm{d}t} (k + W) = 0$ and $k + W =$ constant. At equilibrium the relative kinetic energy $k$ vanishes and $W$ is a constant, zero, say:

$$
k = 0, \quad W = 0 a t e q u i l i b r i u m.
$$

The motion is perturbed through the action of an internal heat source or by an external force. Then $k$ or $W$ or both are nonvanishing, and

$$
k + W = \text {c o n s t a n t}.
$$

$W$ is an absolute minimum provided the rotation-axis coincides with the axis of greatest moment of inertia; $k$ is positive definite and cannot increase indefinitely at the expense of $W$ . A small perturbation can lead only to harmonic motion with energy periodically interchanged between kinetic, rotational, potential, and elastic energy. The system is totally stable.

(2) Friction, with $W$ an absolute minimum. For small motions conservation of energy leads to

$$
k + W = \text {c o n s t a n t} - \alpha t,
$$

where $\alpha$ is a positive constant. The effect of friction is to damp out the perturbations, and the motion is said to be secularly stable (Lyttleton, 1953). Anelasticity does not alter the conditions for secular stability and contributes only to the dissipation.

(3) $W$ not an absolute minimum (e.g., rotation about the axis of least moment of inertia). Without anelasticity, a slight perturbation will lead to oscillations (possibly damped) about the equilibrium position, and the motion is said to be ordinarily stable. With anelasticity present a perturbation will grow at a rate initially described by

$$
k + W = \text {c o n s t a n t} - \beta t,
$$

where $\beta$ is a positive constant, with $W$ decreasing until it finally reaches an absolute minimum. Such secular instability (in the sense used by Lyttleton) can arise in anelastic materials, provided a given disturbance results in non-vanishing elastic stresses and rates of anelastic deformation.

As a simple example, consider a planet in free rotation about the axis of greatest moment of inertia such that $W$ is an absolute minimum. The external form of the planet is assumed in equilibrium with the angular velocity of rotation. A meteorite lands on the planet at some point other than the equator. The mean position of the rotation axis is slightly displaced and $W$ is no longer an absolute minimum (the moment of inertia is maximized only if the added mass is at the greatest possible distance from the rotation-axis). The small displacement of the rotation axis creates stresses within the planet, and no further displacement of the axis will occur if the elastic stresses nowhere exceed the strength of the material, i.e., $a_{ij}$ is everywhere zero. If $a_{ij}$ does not vanish, even for small stresses, then the body is secularly unstable, and a large motion will result with the equatorial bulge adjusting to the changing (with respect to the mean axis) position of the rotation axis (§ 12.6, 12.8).

# 3. Generalized $Q$

In many problems we will use the 'specific dissipation function'

$$
\frac {1}{Q} = \frac {1}{2 \pi E} \oint \frac {\mathrm {d} E}{\mathrm {d} t} \mathrm {d} t \tag {4.3.1}
$$

as a dimensionless measure of the rate at which energy is dissipated in a vibrating system. Here $\oint (\mathrm{d}E / \mathrm{d}t)dt$ is the energy dissipated over a complete cycle, and $E$ is the peak energy stored in the system during a cycle. The quantity $1 / Q$ is particularly useful in discussions of observational data since it does not depend on the detailed mechanism by which energy is dissipated.

Consider the case of a linear, damped oscillator:

$$
\frac {\mathrm {d} ^ {2} x}{\mathrm {d} t ^ {2}} + 2 \alpha \frac {\mathrm {d} x}{\mathrm {d} t} + \sigma_ {0} ^ {2} x = \sigma_ {0} ^ {2} a \cos \sigma t.
$$

The specific dissipation turns out to be

$$
\frac {1}{Q} = \frac {2 \alpha}{\sigma_ {0}} \frac {\sigma}{\sigma_ {0}} \tag {4.3.2}
$$

and depends therefore on frequency. For the special case of a forced oscillation at resonance frequency, $\sigma = \sigma_0$ , we write

$$
\frac {1}{Q _ {0}} = \frac {2 \alpha}{\sigma_ {0}}, \tag {4.3.3}
$$

and this corresponds to the usual definition in electrical circuit theory. Accordingly, $Q_0a$ is the amplitude at resonance. The sharpness of resonance is indicated by

$$
\frac {1}{Q _ {0}} = \frac {2 \Delta \sigma}{\sigma_ {0}}, \tag {4.3.4}
$$

where $\sigma_0 \pm \Delta \sigma$ are the circular frequencies at the half-power points (amplitude $2^{-\frac{1}{2}} Q_0 a$ ). The phase lag $\phi$ is given by

$$
\tan \phi = \frac {\sigma \sigma_ {0}}{\sigma^ {2} - \sigma_ {0} ^ {2}} \frac {1}{Q _ {0}} = \frac {\sigma^ {2}}{\sigma^ {2} - \sigma_ {0} ^ {2}} \frac {1}{Q}. \tag {4.3.5}
$$

The free oscillation decays according to

$$
e ^ {- \alpha t} \cos \sigma_ {0} t. \tag {4.3.6}
$$
