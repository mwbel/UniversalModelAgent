# CHAPTER 5

# LOVE NUMBERS AND ASSOCIATED COEFFICIENTS

If the Earth were rigid we could at once apply the Liouville equation (3.1.6) to compute changes in rotation arising from specified geophysical events. For a deformable Earth the equation still holds, but allowance must be made for secondary effects such as the yield of the Earth under superficial loads and the shift in the equatorial bulge resulting from changes in rotation. Such mass shifts surely must be taken into account together with the specified shifts which brought about the disturbance in the first place. In return for this complication, a comparison of geophysical and astronomical observations will give information concerning the elastic (and anelastic) properties of the Earth.

Deformations result from body forces, such as tidal forces or the centrifugal force associated with rotation, and from surface stresses, such as atmospheric pressure or wind drag. A sudden load applied to the surface will initiate elastic waves traveling with speeds of the order of kilometers per second. Fundamental modes of free vibrations of the Earth associated with such waves have periods of the order of one hour. If the period of the forcing function is long compared to this, then it can be assumed that the elastic deformations follow instantly and are given by static considerations. The oceans and fluid core have response times much longer than the free vibrations, and there is some question as to the frequency below which static theory applies.

# 1. The Love numbers* $h, k$ and $l$

Consider the response of the Earth to a disturbing potential $U(r)$ of degree 2; tidal forces of the Moon and Sun, and centrifugal forces

arising from rotation can be written as gradients of such a potential $U$ . The resulting deformation defines the Love numbers as follows: the ground is lifted by $hU_{\text{surface}} / g$ , and the additional gravitational potential at the (displaced) surface arising solely from this redistribution of mass is $kU$ . Thus $1 + k$ is a factor allowing for the attraction of the bulge by itself, and the response by $hU / g$ takes this self-attraction into account. A fluid surface covering the globe would remain equipotential and be lifted by $(1 + k)U / g$ relative to the centre of the Earth and by $(1 + k - h)U / g$ relative to the sea bottom.

In addition to the vertical displacement of the solid surface by $hU / g$ there is a horizontal displacement with components

$$
\frac {l}{g} \frac {\partial U}{\partial \theta}, \quad \frac {l}{g} \frac {1}{\sin \theta} \frac {\partial U}{\partial \lambda}, \tag {5.1.1}
$$

where $\theta$ is colatitude and $\lambda$ east longitude.

The Love numbers are dimensionless parameters which neatly summarize some of the elastic properties of the Earth. Their evaluation belongs to the subject of elasticity. Information comes from a great variety of sources. The great advantage of writing the equation in terms of these parameters is that the equations can readily be adapted to any future improvement of our knowledge concerning the elastic behavior of the Earth.

The most detailed calculations are those by Takeuchi (1950) on the basis of certain distributions of density and elastic properties within the Earth as derived from seismic and other evidence. His results are (Jeffreys, 1952, p. 213)

$$
\begin{array}{l} k _ {T} = 0 \cdot 2 9 0, \\ k _ {T} = 0 \cdot 2 8 1, \end{array} \quad \left. \begin{array}{l l l} h _ {T} = 0 \cdot 5 8 7, & & l _ {T} = 0 \cdot 0 6 8 \\ h _ {T} = 0. 6 1 0, & & l _ {T} = 0 \cdot 0 8 2 \end{array} \right\} \tag {5.1.2}
$$

for two models proposed by Bullen. There are other methods of measuring Love numbers, as will be shown, and for various reasons the results are not immediately comparable (§ 10.4 and § 10.8).

# 2. Rotational deformation

We consider the distortion of the Earth due to any potential, $U$ , of degree 2. The distortion gives rise to an exterior gravitational potential $k(a^{5} / r^{5})U$ , by definition of $k$ . But the gravitational potential near the boundary of a body departing slightly from spherical

symmetry is given by MacCullagh's formula (Jeffreys, 1952: §4.025-2 and 7.04-13). In the present case the deformation is a spherical harmonic of degree 2, and the pertinent terms in MacCullagh's formula can be written $(Gm / r) + V$ , with

$$
V = \frac {G}{2 r ^ {5}} \left[ C _ {1 1} (x _ {2} ^ {2} + x _ {3} ^ {2} - 2 x _ {1} ^ {2}) +.. - 6 C _ {1 2} x _ {1} x _ {2} -.. \right] = k \frac {a ^ {5}}{r ^ {5}} U. \tag {5.2.1}
$$

The dots .. designate two additional terms that are obtained by cyclic rotation of subscripts.

Consider the special case of the centrifugal potential, which equals $\frac{1}{2}\omega^2$ times the square of the distance from the rotation-axis, or

$$
\frac {1}{2} \left[ \omega^ {2} r ^ {2} - \left(\omega_ {i} x _ {i}\right) ^ {2} \right], \quad \omega^ {2} = \omega_ {i} \omega_ {i}, \quad r ^ {2} = x _ {i} x _ {i}.
$$

This can be organized into the terms $\frac{1}{3}\omega^2 r^2 + U$ , where

$$
U = \frac {1}{6} \left[ \omega_ {1} ^ {2} \left(x _ {2} ^ {2} + x _ {3} ^ {2} - 2 x _ {1} ^ {2}\right) +.. - 6 \omega_ {1} \omega_ {2} x _ {1} x _ {2} -. . ] \right. \tag {5.2.2}
$$

is a spherical harmonic of degree 2. The term $\frac{1}{3}\omega^2 r^2$ leads to a purely radial deformation which consists of a contraction near the center of the Earth and an extension in the outer parts (Love, 1927, p. 143). Substitution of (5.2.2) into (5.2.1) yields

$$
C _ {i j} = I \delta_ {i j} + \frac {k a ^ {5}}{3 G} \omega_ {i} \omega_ {j} + \text {c o n s t a n t}, \tag {5.2.3}
$$

where $I = \frac{1}{3} (C_{11} + C_{22} + C_{33})$ is the inertia of the sphere in the absence of rotational deformation. This determines the constant, so that finally

$$
C _ {i j} = I \delta_ {i j} + \frac {k a ^ {5}}{3 G} \left(\omega_ {i} \omega_ {j} - \frac {1}{3} \omega^ {2} \delta_ {i j}\right). \tag {5.2.4}
$$

# 3. The secular Love number

The Love number $k$ in (5.2.4) can be interpreted as a measure of the Earth's yield to centrifugal deformation in the course of its development during the last five billion years or so. Without loss of generality we can place the $x_{3}$ -axis along the rotation vector. Then $\omega_{1} = 0, \omega_{2} = 0, \omega_{3} = \Omega$ , and

$$
C _ {1 1} = C _ {2 2} = A = I - \frac {k _ {s} a ^ {5}}{9 G} \Omega^ {2}, \quad C _ {3 3} = C = I + \frac {2 k _ {s} a ^ {5}}{9 G} \Omega^ {2}, (5. 3. 1)
$$

$$
k _ {s} = \frac {3 G H C}{a ^ {5} \Omega^ {2}}, \tag {5.3.2}
$$

where $H$ is the precessional constant (2.2.1). If all mass were concentrated at the center, $C = 0$ and hence $k_{s} = 0$ . For a homogeneous sphere $C = \frac{3}{8} Ma^2$ , and with $M = 5 \cdot 98 \times 10^{27} \mathrm{~g}$ for the mass of the Earth, one obtains $k_{s} = 1 \cdot 14$ . The correct value lies between these limits. From the value of $H$ and the international gravity formula one obtains (Jeffreys, 1952, p. 145)

$$
C = 0 \cdot 3 3 3 6 M a ^ {2}, \tag {5.3.3}
$$

as compared to $C = 0\cdot 4Ma^2$ for the homogeneous Earth, and thus

$$
k _ {s} = 0. 9 6. \tag {5.3.4}
$$

# 4. The fluid Love numbers

The foregoing calculation of $k$ involves the observed rate of precession and the shape of the ellipsoid derived from gravity measurements. There have been no assumptions concerning the stress-strain relations within the Earth.

We next compute the 'fluid' Love number $k_{f}$ based on the assumption that the Earth is in hydrostatic equilibrium, i.e., that it has the shape of a rotating fluid with a density distribution equal to that of the actual Earth. To a first order the surface ellipticity is then given by

$$
\varepsilon = h _ {f} \left(\frac {1}{2} \Omega^ {2} a / g\right). \tag {5.4.1}
$$

If all the mass were concentrated at the center, $h_f = 1$ and $\varepsilon = 1 / 580$ . For a homogeneous Earth it has been shown by Kelvin that $h_f = \frac{\varepsilon}{2}$ , so that $\varepsilon = 1 / 232$ . The observed ellipticity, 1/297, lies between these values. Using the observed value of $\varepsilon$ gives

$$
h _ {f} = (5 8 0 / 2 9 7) = 1 \cdot 9 6. \tag {5.4.2}
$$

But, for a fluid surface, $h_f = 1 + k_f$ (§ 5.1); thus

$$
k _ {f} = 0. 9 6, \tag {5.4.3}
$$

which is equal numerically to the secular Love number, $k_{e}$

A more precise argument is given by Bullard (1948): from the observed precession and Bullen's distribution of density within the Earth, Bullard obtains $\varepsilon^{-1} = 297\cdot 338 \pm 0\cdot 050$ , assuming hydrostatic

equilibrium. The eccentricity can be independently derived without the assumption of hydrostatic equilibrium, either from gravity observations or from the motion of the Moon. The resultant values, $296\cdot 17 \pm 0\cdot 68$ and $296\cdot 72 \pm 0\cdot 65$ , do not differ significantly from the preceding value. The most recent analysis of gravity observations (Heiskanen, 1957; Heiskanen and Vening Meinesz, 1958) gives $297\cdot 0$ to $297\cdot 2$ , and these are in even better agreement with the hydrostatic value. According to these observations, the shape of the actual Earth does not differ measurably from that of an equivalent rotating fluid. There might be a difference of as much as one-third per cent and in fact the satellite observations indicate that this is so ( $\S$ 12.8). Such a difference, if it were real, would be a certain measure of the Earth's finite strength to resist deformation from stresses, no matter for how long a time these stresses are applied ( $\S$ 12.8). In the case of no finite strength $k_{f} = k_{s}$ exactly for sustained stresses, and there is no stability in the above sense. The question whether $k_{f} \approx k_{s}$ or $k_{f} = k_{s}$ is clearly an important one.

# 5. The tidal-effective Love numbers

From studies of Earth tides and the Chandler wobble one obtains $h = 0 \cdot 59$ , $k = 0 \cdot 29$ . The close agreement with the values (5.1.2) derived by Takeuchi from seismic evidence is to some extent misleading ( $\S$ 10.3). There is a marked contrast with the values $h_s = 1 \cdot 96$ , $k_s = 0 \cdot 96$ obtained from the figure of the Earth. A number of hypotheses may explain the difference, and it is not known which of these (if any) is correct: one hypothesis is based on the relative magnitude of stresses, with the secular Love numbers referring to stress differences above a critical strength, tidal-effective Love numbers to stress differences below the critical strength. A second hypothesis is based on the relative duration of stresses, with the secular Love numbers referring to stresses much more prolonged than some critical duration, tidal-effective Love numbers to stresses much less prolonged than this critical duration. Still another possibility is that the Earth was originally molten and that it now has the figure at the time of congealment. The agreement between $k_s$ and $k_f$ then implies little or no changes in rotation. This is extremely unlikely ( $\S$ 11.9). But there can be no doubt that the Earth responds far differently to

ordinary tide potentials and the annual wobble than it responds to diurnal rotation. We may regard $h, k$ , as the asymptotic case of generalized Love numbers when the frequency is high and the disturbance infinitesimal; $h_{\alpha}, k_{\alpha}$ , as the asymptotic values for low frequency and large amplitude. An example of generalized Love numbers is discussed in § 5.11.

The tidal-effective Love numbers are obtained from an overall response of the planet Earth to potential disturbances; they already allow for the complexities of the core, mantle and yield of oceans. The variation in inertia due to rotational deformation is obtained from (5.2.4). The important terms are the products of inertia, and these become

$$
C _ {i j} = \frac {k}{k _ {f}} \frac {\omega_ {i} \omega_ {j}}{\Omega^ {2}} (C - A), \quad i \neq j, \tag {5.5.1}
$$

making use of the definition (5.3.2) of $k_{s}$ and setting $k_{s} = k_{f}$ . Corresponding expressions for the moments of inertia follow from (5.2.4), (5.3.1), and (5.3.2).

# 6. The 'equivalent' Earth

Kelvin has shown (Jeffreys, 1952, pp. 211, 363-4) that, for an incompressible homogeneous sphere of rigidity $\tilde{\mu}$ ,

$$
h = \frac {5 / 2}{1 + \mu}, \quad k = \frac {3 / 2}{1 + \mu}, \quad l = \frac {3 / 4}{1 + \mu}; \quad \mu = \frac {1 9}{2} \frac {\tilde {\mu}}{\rho g a}. \tag {5.6.1}
$$

Kelvin's solution yields the fluid Love numbers $h_f = 2 \cdot 5$ , $k_f = 1 \cdot 5$ , compared to the observed values $h_f = 1 \cdot 96$ , $k_f = 0 \cdot 96$ for the Earth (there is no observed value for $l_f$ ). For a better fit to actual conditions the simplest procedure is to adopt the relations

$$
h = \frac {h _ {f}}{1 + \mu}, \quad k = \frac {k _ {f}}{1 + \mu}, \tag {5.6.2}
$$

which are of the same form as Kelvin's solution but use the observed values $h_f = 1 \cdot 96$ , $k_f = 0 \cdot 96$ . The usefulness of this model of an equivalent Earth depends on how well the two known values $h$ and $k$ can be computed by an appropriate choice of the single parameter $\mu$ . The set of values

$$
\mu = 2 \cdot 3, \quad h = 0 \cdot 5 9, \quad k = 0 \cdot 2 9 \tag {5.6.3}
$$

are in excellent accord with the best estimates of tidal-effective rigidity. Accordingly, this value $\mu = 2\cdot 3$ is a satisfactory measure of the tidal-effective rigidity of the Earth.* By inference we can roughly estimate the fluid Love number $l_{f}$ to be 0-23 as compared to 3/4 for homogeneous Earth; for, with this value and $\mu = 2\cdot 3$ , one obtains

$$
l = \frac {l _ {f}}{1 + \mu} = 0. 0 7 \tag {5.6.4}
$$

in agreement with Takeuchi's calculation.

# 7. Love numbers of degree $n$

We shall have occasion to refer to Love numbers of any degree $n$ . Their definitions are given simply by writing $\dagger U_n$ in place of $U(= U_2)$ in § 5.1. For a homogeneous incompressible sphere the formulae are

$$
h _ {n} = \frac {n + \frac {1}{2}}{n - 1} \frac {1}{1 + \mu N}, \quad k _ {n} = \frac {\frac {3}{2}}{n - 1} \frac {1}{1 + \mu N},
$$

$$
l _ {n} = \frac {\frac {3}{2}}{n (n - 1)} \frac {1}{1 + \mu N}, \tag {5.7.1}
$$

where $N = \frac{2(2n^2 + 4n + 3)}{19n}$ (5.7.2)

For the case $n = 2$ , $N = 1$ and (5.7.1) reduces to (5.6.1).

# 8. Load deformation and the coefficients $h', k'$

Consider the effect of a variable surface load $q(t) \, \mathrm{gcm}^{-2}$ , e.g., a blanket of snow. We are concerned with the term $q_{n}$ of degree $n$ in the surface spherical harmonic expansion of $q$ . The interior potential resulting from a gravitating layer $q_{n}$ is

$$
U _ {n} = \frac {4 \pi G q _ {n} a}{2 n + 1} \left(\frac {r}{a}\right) ^ {n}. \tag {5.8.1}
$$

The deformation is due to two opposing effects. First there is a normal

* Kelvin's famous observation that the effective rigidity of the Earth is nearly that of steel is based on a value $\mu = 4 \cdot 1$ .   
$\dagger$ Thus $U_{n}$ is not a tensor; $\pmb{n}$ is not a tensor subscript. See index of notation.   
$\ddagger$ These formulae for Love numbers are not found in Love's great work on elasticity; they have to be extracted from five equations in five unknowns (Love 1927, Section 177).

stress (positive upwards) $p_n = -g q_n$ which will depress the surface. Then there is the gravitational attraction of the Earth by the snow, and this will raise the ground. By the combined effect of pressure and attraction the surface is raised by $h_n' U_n / g$ and the gravitational potential arising from the distortion is $k_n' U_n'$ . This defines $h_n', k_n'$ . The depression is found to be somewhat larger than the gravitational uplift, and $h_n', k_n'$ are negative, as expected.

The case of an incompressible homogeneous sphere serves as a simple example. It has been shown by Chree (1889) that the effect of any radial stress, $p_n$ , is equivalent to that of a body potential, $U_n = p_n / \rho$ . Writing $p_n = -g q_n$ , $3g = 4\pi G a \rho$ , the combined potentials of the gravitating layer, of the deformation arising from the 'load potential' $p_n / \rho$ , and of the deformation arising from the gravitational attraction are

$$
U _ {n} + k _ {n} \frac {p _ {n}}{\rho} + k _ {n} U _ {u} = U _ {n} (1 + k _ {n} ^ {\prime}),
$$

hence

$$
k _ {n} ^ {\prime} = \left(\frac {p _ {n}}{\rho U _ {n}} + 1\right) k _ {n} = \left(- \frac {2 n + 1}{3} + 1\right) k _ {n} = - \frac {2}{3} (n - 1) k _ {n}, \tag {5.8.2}
$$

and similarly for $h_n'$ . Thus if one has obtained the Love numbers $k_n, h_n$ due to a potential that does not load the Earth, such as the rotational and tidal potential, the response to one that does is given by

$$
h _ {n} ^ {\prime}, k _ {n} ^ {\prime} = \left[ - \frac {2}{3} (n - 1) \right] h _ {n}, k _ {n}. \tag {5.8.3}
$$

Combining this with (5.7.1) gives

$$
h _ {n} ^ {\prime} = - \frac {2}{3} (n + \frac {1}{2}) \frac {1}{1 + \mu N}, \quad k _ {n} ^ {\prime} = - \frac {1}{1 + \mu N}, \tag {5.8.4}
$$

$$
h _ {2} ^ {\prime} = h ^ {\prime} = - \frac {\frac {5}{8}}{1 + \mu}, k ^ {\prime} = - \frac {1}{1 + \mu}. \tag {5.8.5}
$$

At first sight it appears surprising that the two opposing effects of load depression and gravitational uplift are of the same order, $-\frac{5}{8}$ and $+1$ for the case $n = 2$ . The local distortion by loads of limited extent, corresponding to harmonics of high degree $n$ , is determined by load depression rather than gravitational uplift in the

ratio $\frac{2}{3} n$ . This may be the reason why we are unaccustomed to the importance of gravitational uplift when $n = 2$ . The two opposing effects cancel when $n = 1$ , and this is closely related to the fact that an expansion, into spherical harmonics, of the gravity of a spheroid yields no term for $n = 1$ (Jeffreys, 1952, 4-026). This term is equivalent to a rigid body displacement and does not affect surface gravity. For $n = 0$ , $N$ becomes infinite, hence $h_0' = 0$ , $k_0' = 0$ : a uniform load over an incompressible Earth causes no deformation.

# 9. Load deformation, second order

It will be noted that for a fluid Earth $\mu = 0$ , and $k_f' = -1$ . Thus the potential of a surface load after yielding is $(1 + k_f')U = 0$ . The

![](images/0378fb6cb8ccf5c913c285a5f52949ea0f1dbab52d33568f482ef064913bb40d.jpg)  
Fig. 5.1. A layer of density $\rho'$ extends from the surface at $r = a$ to an interface at $r = a - b$ (left). A thickening by $H'$ (center) leads to yielding of the layer by an amount $H$ (right).

inertia terms are proportional to $(1 + k_f')U$ and vanish also. But potential and inertia cannot be identically zero. The inertia of an ocean covered by icebergs is larger than after the bergs have melted. It is necessary to allow for the slight difference in the distances of the icebergs and of the displaced water from the rotation axis.

The undisturbed surface is at a distance $a$ from the Earth's center (fig. 5.1). A block formed out of material from a superficial layer leads to an increase in mass per unit area of $\rho^{\prime}H^{\prime}$ . The center of mass of this block is at a distance $a + \frac{1}{2} H^{\prime}$ from the Earth's center before yielding. Again we are concerned only with surface harmonics of degree 2, so that $q_{2} = \rho^{\prime}H_{2}^{\prime} = \rho^{\prime}H^{\prime}$ . The exterior potential before yielding is

$$
U _ {I} = \frac {4}{8} \pi G r ^ {- 3} \left(\rho^ {\prime} H ^ {\prime}\right) \left(a + \frac {1}{2} H ^ {\prime}\right) ^ {4}.
$$

In the event $(H' / a)$ approaches 0 this reduces to the first order expression (5.8.1) for the case $n = 2$ . After yielding by an amount $H$

we are left with a load (positive or negative) $\rho^{\prime}(H^{\prime} - H)$ at an average distance $a + \frac{1}{2} H^{\prime} - \frac{1}{2} H$ and a load $(\rho^{\prime} - \rho)H$ at $a - b - \frac{1}{2} H$ . The corresponding potential of degree 2 is

$$
\begin{array}{l} U _ {F} = \frac {1}{2} \pi G r ^ {- 3} [ \rho^ {\prime} (H ^ {\prime} - H) (a + \frac {1}{2} H ^ {\prime} - \frac {1}{2} H) ^ {4} \\ + (\rho^ {\prime} - \rho) H (a - b - \frac {1}{2} H) ^ {4} ]. \\ \end{array}
$$

But $-H_{2} = h^{\prime}U_{I} / g$ and $U_{F} = (1 + k^{\prime})U_{I}$ at $r = a$ , by definition of $h^\prime, k^\prime$ . For a homogeneous Earth (except for the surface load) $3g = 4\pi Ga\rho$ and $h^\prime = -\frac{5}{3}(1 + \mu)^{-1}$ ; furthermore $b, H, H'$ are all small compared to $a$ and $H, H'$ small compared to $b$ . One finds after some manipulation

$$
k ^ {\prime} = - \frac {1 - \iota}{1 + \mu}, \quad \iota = 4 \frac {b}{a} \left(1 - \frac {\rho^ {\prime}}{\rho}\right), \quad 1 + \mu = \frac {\rho^ {\prime} H _ {2} ^ {\prime}}{\rho H _ {2}}. \tag {5.9.1}
$$

In the case the load has the same density as the underlying rock, the isostatic factor $\iota$ vanishes, and $k' = -(1 + \mu)^{-1}$ in agreement with the first order calculation (5.8.5). The numerical factor in the expression for $\iota$ does not apply exactly to the Earth since homogeneity has been assumed. For a precise formulation in which conservation of mass is explicit a development along the lines of § 5.12 is indicated.

# 10. Fluid Earth with surface tension

Another case of interest is that of a thin elastic crust over a fluid Earth. Perhaps this case is adequately covered by considering a liquid sphere with a surface tension $\tilde{\pmb{v}}$ over and above that arising from sphericity; presumably the crust is not in tension except when distorted.

Let $U_{2}$ be any second degree disturbing potential. The distorted surface is at $r = a(1 + \varepsilon S_{2})$ , where

$$
S _ {n} = p _ {n} ^ {m} (\cos \theta) (\cos m \lambda , \sin m \lambda), (m = 0 \text {t o} n) \tag {5.10.1}
$$

is the surface spherical harmonic and $p_{n}^{m}$ are the associated Legendre functions (A.1.1). The potentials arising from the excess surface tension and from the distortion of the sphere are

$$
V = - \frac {3 \tilde {v}}{\rho r ^ {2}} a \varepsilon S _ {2}, \quad W = \frac {4}{3} \pi G a ^ {3} \left(\frac {1}{r} + \frac {3 a ^ {2} \varepsilon S _ {2}}{5 r ^ {3}}\right)
$$

respectively. For a homogeneous sphere, $3g = 4\pi G a\rho$ ; $U_{2} + V_{2} + W_{2} =$ constant at the distorted surface, and the terms containing $S_{2}$ give

$$
h = \frac {\left(U _ {2} / g\right) _ {\text {s u r f}}}{a \varepsilon S _ {2}} = - \frac {\left(V _ {2} + W _ {2}\right) _ {\text {s u r f}}}{g a \varepsilon S _ {2}} = \frac {5 / 2}{1 + v}; k = \frac {3 / 2}{1 + v}, \tag {5.10.2}
$$

where

is a dimensionless surface tension which enters in the same way as the dimensionless rigidity $\mu$ in (5.6.1). Similarly $h'$ and $k'$ are obtained from (5.8.5) by replacing $\mu$ with $\pmb{v}$ .

# 11. Love operators and complex Love numbers

In the study of polar wandering and of the damping of the Chandler wobble, we shall refer to solutions where the Earth is considered a Maxwell body or Kelvin-Voigt body ( $M$ or $K - V$ ). In a Maxwell (or elastoviscous) body the total rate of deformation is written as a sum of an elastic and a viscous term (§4.1):

$$
\frac {1}{s} \frac {\mathrm {d} s}{\mathrm {d} t} = \frac {1}{2 \tilde {\mu}} \frac {\mathrm {d}}{\mathrm {d} t} (\tau_ {\text {e l a s t i c}}) + \frac {1}{2 \tilde {\eta} _ {M}} (\tau_ {\text {e l a s t i c}}), \tag {5.11.1}
$$

where $\tilde{\mu}$ is the rigidity, $\tilde{\eta}$ the dynamic viscosity, and $\tau_{\mathrm{elastic}}$ the elastic stress. In a Kelvin-Voigt (or firmoviscous) body the total stress is written as a sum of an elastic stress and a viscous stress:

$$
\tau_ {\text {e l a s t i c}} = 2 \tilde {\mu} \varepsilon + 2 \tilde {\eta} _ {K - V} \frac {\mathrm {d} \varepsilon}{\mathrm {d} t}. \tag {5.11.2}
$$

The Kelvin-Voigt body is distinguished by the fact that there is no permanent strain associated with deformation. The dissipation results from an added stress proportional to the rate of strain; in the Maxwell body the dissipation results from permanent deformation. The Maxwell body is often portrayed as a spring and dashpot in series; the Kelvin-Voigt body as a spring and dashpot in parallel. Love operators can be written for any combinations of springs and dashpots.

Once the elastic problem has been solved, the appropriate

solutions for the M and K-V bodies can be found by replacing the dimensionless rigidity* $\mu$ with the operators

$$
\hat {\mu} _ {M} = \frac {\mu \hat {D}}{\hat {D} + \tau^ {- 1}}, \quad \hat {\mu} _ {K - V} = \mu (1 + \tau \hat {D}), \tag {5.11.3}
$$

respectively. Here $\tau = \tilde{\eta} / \tilde{\mu}$ is the characteristic time constant, and $\hat{D}$ the operator $d/dt$ (Jeffreys and Jeffreys, 1950, chs. 7 and 8). The Love operators

$$
\hat {k} = \frac {k _ {f}}{1 + \hat {\mu}}, \quad k ^ {\prime} = - \frac {1 - \iota}{1 + \hat {\mu}} \tag {5.11.4}
$$

are a convenient notation. For the case of simple harmonic motion $e^{i\sigma t}$ , the operator $\hat{D}$ becomes $i\sigma$ , and $\hat{\mu}, \hat{k}, \hat{k}'$ become the complex numbers $\mu, k, k'$

For elastic waves, the generalized “ $Q$ ” (§4.3) becomes

$$
\frac {1}{Q _ {M}} = \frac {\tilde {\mu}}{\tilde {\eta} _ {M}} \frac {1}{\sigma}, \quad \frac {1}{Q _ {K - V}} = \frac {\tilde {\eta} _ {K - V}}{\tilde {\mu}} \sigma , \tag {5.11.5}
$$

respectively.

# 12. A systematic development

Jeffreys (1952) has emphasized the need for a systematic development of the Love number corrections. Jeffreys (1916) and Rosenhead (1929) end up with a sea surface that is not isobaric and Schweydar (1916) treats an Earth in which mass is not conserved.

The customary scheme is to write

$$
h _ {n} U _ {n} / g, \quad k _ {n} U _ {n}, \quad (1 + k _ {n}) U _ {n} \tag {5.12.1}
$$

for the amount the ground is lifted, the added potential due to the deformation and the final potential, all in terms of an initially prescribed potential $U_{n}$ that does not load the Earth. For a potential, $U_{n}$ that does load, we have introduced the notation

$$
h _ {n} ^ {\prime} U _ {n} ^ {\prime} / g, \quad k _ {n} ^ {\prime} U _ {n} ^ {\prime}, \quad \left(1 + k _ {n} ^ {\prime}\right) U _ {n} ^ {\prime}. \tag {5.12.2}
$$

A tidal potential, $U_{2}$ , or the potential of a snow load, $U' = \sum_{n=0}^{\infty} U_{n}'$ , may serve as examples for the two cases.

The difficulty is that the distortion of the sea bottom causes an ocean tide which gives rise to an additional potential and to additional load deformations, and these are linked in a complicated way to the initial disturbance. It is perhaps better to refer to the 'final' potentials, $V_{n}$ , $V_{n}^{\prime}$ (which include the initially prescribed potentials, $U_{n}$ , $U_{n}^{\prime}$ ) and to define the Love numbers $K_{n}$ , $H_{n}$ , $K_{n}^{\prime}$ , $H_{n}^{\prime}$ such that

$$
H _ {n} V _ {n} / g, \quad K _ {n} V _ {n}, \quad V _ {n}; \quad H _ {n} ^ {\prime} V _ {n} ^ {\prime} / g, \quad K _ {n} ^ {\prime} V _ {n} ^ {\prime}, \quad V _ {n} ^ {\prime} \tag {5.12.3}
$$

have the same meanings as the quantities in (5.12.1) and (5.12.2). It follows that

$$
H _ {n} = \frac {h _ {n}}{1 + k _ {n}}, \quad K _ {n} = \frac {k _ {n}}{1 + k _ {n}}; \quad H _ {n} ^ {\prime} = \frac {h _ {n} ^ {\prime}}{1 + k _ {n} ^ {\prime}}, \quad K _ {n} ^ {\prime} = \frac {k _ {n} ^ {\prime}}{1 + k _ {n} ^ {\prime}}. \tag {5.12.4}
$$

Owing to any initial disturbing potential, the ground is raised by

$$
g ^ {- 1} \sum_ {n = 0} ^ {\infty} \left[ H _ {n} V _ {n} + H _ {n} ^ {\prime} V _ {n} ^ {\prime} \right],
$$

and the sea surface relative to the Earth's center of mass by

$$
g ^ {- 1} \sum_ {n = 0} ^ {\infty} \left[ V _ {n} + V _ {n} ^ {\prime} \right],
$$

$$
\text {s o} \xi = \sum_ {n = 0} ^ {\infty} \xi_ {n} = g ^ {- 1} \mathcal {C} (\theta , \lambda) \sum_ {n = 0} ^ {\infty} \left[ \left(1 - H _ {n}\right) V _ {n} + \left(1 - H _ {n} ^ {\prime}\right) V _ {n} ^ {\prime} \right] \tag {5.12.5}
$$

is the elevation of the sea surface over the sea bottom; here $\mathcal{C}(\theta, \lambda)$ is the 'ocean function' (see § A.1), defined by

$\mathcal{C}(\theta ,\lambda) = 1$ , where there are seas;

$\mathcal{C}(\theta, \lambda) = 0$ , where there is land.

The final potential $V_{n}$ is determined by the initial disturbance and the deformation potentials:

$$
V _ {n} = U _ {n} + K _ {n} V _ {n}, \tag {5.12.6}
$$

whereas $V_{n}^{\prime}$ depends also on the displacement of the sea surface:

$$
V _ {n} ^ {\prime} = U _ {n} ^ {\prime} + K _ {n} ^ {\prime} V _ {n} ^ {\prime} + \frac {3 g}{2 n + 1} \xi_ {n}. \tag {5.12.7}
$$

$V_{\mathfrak{n}}^{\prime}$ must be considered as unknown since this potential depends on the ocean tide $\xi$ which in turn depends in a complicated way on the disturbing potentials.

Equations (5.12.6) and (5.12.7) are solved for $V_{n}$ and $V_{n}^{\prime}$ , and the resulting expressions substituted into (5.12.5):

$$
\sum_ {n = 0} ^ {\infty} \xi_ {n} = g ^ {- 1} \mathcal {C} (\theta , \lambda) \sum_ {r = 0} ^ {\infty} \left(J _ {r} U _ {r} + J _ {r} ^ {\prime} U _ {r} ^ {\prime} \frac {3 g}{2 r + 1} J _ {r} ^ {\prime} \xi_ {r}\right), \tag {5.12.8}
$$

where

$$
J _ {r} = \frac {1 - H _ {r}}{1 - K _ {r}} = 1 + k _ {r} - h _ {r}, J _ {r} ^ {\prime} = \frac {1 - H _ {r} ^ {\prime}}{1 - K _ {r} ^ {\prime}} = 1 + k _ {r} ^ {\prime} - h _ {r} ^ {\prime}.
$$

Equation (5.12.8) displays the complicated dependence of the ocean tide on the initial disturbing potentials $U_r$ and $U_{r'}'$ . Suppose we wish to solve for $s + 1$ harmonics, from $n = 0$ to $n = s$ . Then (5.12.8) gives $s + 1$ equations for $s + 1$ unknown, $\xi_0$ to $\xi_s$ . The corresponding potentials follow from (5.12.6) and (5.12.7). All $4(s + 1)$ Love numbers are presumed to be given from the known properties of the Earth.

A convenient manner of dealing with (5.12.8) is to expand $\mathcal{C}(\theta, \lambda)$ into spherical harmonics (A.1.2),

$$
\mathcal {C} (\theta , \lambda) = \sum_ {n = 0} ^ {\infty} \sum_ {m = 0} ^ {n} \left(a _ {n} ^ {m} p _ {n} ^ {m} \cos m \lambda + b _ {n} ^ {m} p _ {n} ^ {m} \sin m \lambda\right), \tag {5.12.9}
$$

and, similarly,

$$
\xi = \sum_ {a = 0} ^ {\infty} \sum_ {b = 0} ^ {a} \left(y _ {a} ^ {b} p _ {a} ^ {b} \cos b \lambda + z _ {a} ^ {b} p _ {a} ^ {b} \sin b \lambda\right),
$$

$$
U _ {r} = \sum_ {m = 0} ^ {r} \left(u _ {r} ^ {m} p _ {r} ^ {m} \cos m \lambda + v _ {r} ^ {m} p _ {r} ^ {m} \sin m \lambda\right)
$$

and similarly for $U'$ using $u', v'$ . The evaluation of the coefficients $y_{a}^{b}, z_{a}^{b}$ requires the calculation of triple products of the associated function $p_{n}^{m}$ (A.1).

As an important special case, consider the initial potential

$$
U _ {2} = u _ {2} ^ {0} p _ {2} ^ {0}.
$$

The coefficients of the ocean tide are given by

$$
\begin{array}{l} g y _ {2} ^ {0} = J _ {2} u _ {2} ^ {0} \left(a _ {0} ^ {0} + \frac {1}{2} a _ {2} ^ {0} + \frac {3}{4} a _ {4} ^ {0}\right) + 3 g J _ {2} ^ {\prime} \left\{\frac {3}{8} y _ {2} ^ {0} \left(2 a _ {0} ^ {0} + a _ {2} ^ {0} + \frac {3}{4} a _ {4} ^ {0}\right) \right. \\ + \left(\frac {1}{3} \frac {4}{8} \frac {1}{0} y _ {2} ^ {1} a _ {2} ^ {1} + z _ {2} ^ {1} b _ {2} ^ {1}\right) + \frac {1}{7} \left(y _ {2} ^ {1} a _ {4} ^ {1} + z _ {2} ^ {1} b _ {4} ^ {1}\right) + \frac {3}{2} \left(y _ {2} ^ {2} a _ {4} ^ {2} + z _ {2} ^ {2} b _ {4} ^ {2}\right) \\ \end{array}
$$

and similar expressions for $y_2^1, y_2^2, z_2^1, z_2^2$ . The five equations determine

all second degree components of $\xi$ . The coefficients are not independent, since conservation of water requires that

$$
y _ {0} ^ {0} = 0.
$$

For a $p_2^0$ disturbance, we have

$$
g y _ {0} ^ {0} + \frac {1}{8} J _ {2} u _ {2} ^ {0} a _ {2} ^ {0} + \frac {3}{3 0 0} g J _ {2} ^ {\prime} \left\{y _ {2} ^ {0} a _ {2} ^ {0} + \frac {3}{3} \left(y _ {2} ^ {1} a _ {2} ^ {1} + z _ {2} ^ {1} b _ {2} ^ {1}\right) + 6 \left(y _ {2} ^ {2} a _ {2} ^ {2} + z _ {2} ^ {2} b _ {2} ^ {2}\right) \right\}.
$$

For disturbing potentials other than $p_2^0$ , the requirement that the mass of the Earth be conserved is automatically satisfied.
