behind this large effort: the measurement by laser interferometric detectors of gravitational waves emitted by compact binary systems involving neutron stars or black holes relies in an essential way on these very accurate theoretical predictions, which allow the extremely weak signals to be distinguished from noise. Data analysis relies on a bank of templates constructed from these waveforms, and cross-correlation of the detector output with the templates can reveal a signal that would otherwise be lost in the noisy data stream. In this way theorists, who build the templates, work hand in hand with experimentalists, who build the detectors, toward the successful measurement of gravitational waves.

# 11.5 Gravitational waves and laser interferometers

Thus far, in this long chapter on gravitational waves, we have said very little about the actual detection of these waves, and indeed we intend to leave it that way. The attempts to detect gravitational waves, from the pioneering experiments carried out by Joseph Weber in the 1960s and 1970s using suspended cylinders of aluminum, to the present international effort involving laser interferometry, pulsar timing, and cosmic microwave background observations, is a story rich in sociology, history, technological development, and bigscience politics. But it is not the main focus of this book. We refer readers who wish to learn more about the detection aspects to a number of excellent resources, listed at the end of this chapter.

Having come this far, however, and having produced the waveforms $h _ { + }$ and $h _ { \times }$ in a ready-to-use form for various sources and in various approximations, our coverage would seem incomplete if we did not make some attempt to connect them with the output of a gravitational-wave detector. It therefore seems appropriate to conclude this chapter by showing how $h _ { + }$ and $h _ { \times }$ can be measured in one of the leading approaches to gravitationalwave detection, laser interferometry.

In its most schematic realization, a laser interferometric gravitational-wave detector works just like the interferometer used by Michelson in the late 1800s to measure the speed of light and search for evidence of an “aether.” The real-life interferometers at the Earth-based LIGO, Virgo, Geo600, and KAGRA observatories, and the one envisioned for a space-based detector (known in 2013 as eLISA), are much more sophisticated than this, but this simple model is adequate and captures the essential physics.

A laser interferometer consists of a laser source, a beam splitter, and two end mirrors mounted on test masses imagined to be freely moving in spacetime (although in reality they can be suspended by thin wires). The arms of the interferometers are taken to be perpendicular to each other, although as we shall see, this is not an essential feature of the design. The laser beam is divided in two at the beam splitter, and each beam travels along one arm of the interferometer, reflects off the test mass, and returns to the beam splitter to be recombined with the other beam. The relative phase of the beams determines whether they produce a bright or dark spot when the recombined beam is measured by a photon detector. Since the initial phases at the beam splitter are identical, the phase difference $\Delta \Phi$ depends on the difference in travel time along the two arms. We can write

$$
\Delta \Phi = 2 \pi \nu ( 2 L _ { 1 } / c - 2 L _ { 2 } / c ) ,
$$

where $\nu$ is the frequency of the laser light, $L _ { 1 }$ and $L _ { 2 }$ are the armlengths, and $2 L _ { 1 } / c$ and $2 L _ { 2 } / c$ are the travel times along each arm (forward and back).

With the origin of the coordinate system placed at the beam splitter, the test mass at the end of the first arm is at a position $\pmb { \xi } _ { 1 } ( t )$ , and the test mass at the end of the second arm is at $\pmb { \xi } _ { 2 } ( t )$ . In the absence of a gravitational wave, the arms would have equal lengths, and we would have $\pmb { \xi } _ { 1 } = L _ { 0 } \pmb { e } _ { 1 }$ and ${ \pmb \xi } _ { 2 } = L _ { 0 } { \pmb e } _ { 2 }$ , in which $L _ { 0 }$ is the unperturbed length of each arm, and $e _ { 1 } , e _ { 2 }$ are unit vectors pointing in the direction of each arm. In the presence of a gravitational wave, the position of each test mass varies with time. Assuming that the armlength $L _ { 0 }$ is much shorter than the wavelength $\lambda$ of the gravitational wave, the displacement is described by Eq. (11.29), and we have

$$
\begin{array} { r } { \xi _ { 1 } ^ { j } = L _ { 0 } \bigg ( e _ { 1 } ^ { j } + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 1 } ^ { k } \bigg ) , } \\ { \xi _ { 2 } ^ { j } = L _ { 0 } \bigg ( e _ { 2 } ^ { j } + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 2 } ^ { k } \bigg ) . } \end{array}
$$

The length of each arm is then given by

$$
\begin{array} { r } { L _ { 1 } = L _ { 0 } \bigg ( 1 + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 1 } ^ { j } e _ { 1 } ^ { k } \bigg ) , } \\ { L _ { 2 } = L _ { 0 } \bigg ( 1 + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 2 } ^ { j } e _ { 2 } ^ { k } \bigg ) , } \end{array}
$$

to first order in $h _ { \mathrm { T T } } ^ { j k }$ , and the phase difference at beam recombination is

$$
\Delta \Phi = \frac { 4 \pi \nu L _ { 0 } } { c } \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) h _ { \mathrm { T T } } ^ { j k } .
$$

If we express the gravitational-wave field as in Eq. (11.6), $h ^ { j k } = ( G / c ^ { 4 } R ) A ^ { j k }$ , this is

$$
\Delta \Phi = \frac { 4 \pi \nu G L _ { 0 } } { c ^ { 5 } R } S ( t ) ,
$$

in which

$$
S ( t ) = \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) A _ { \mathrm { T T } } ^ { j k } ( \tau , N )
$$

is the detector’s response function. We recall that $R$ is the distance to the source, that $N$ is a unit vector pointing from the source to the detector, and that $\tau : = t - R / c$ is retarded time.

To calculate $S ( t )$ we decompose $A _ { \mathrm { T T } } ^ { j k }$ in a transverse basis formed by the unit vectors $e _ { X }$ and $e _ { Y }$ , which are perpendicular to the direction of propagation $e _ { Z } = N$ . This decomposition was detailed back in Sec. 11.1.7, and we use the notation introduced in Sec. 11.2.2. We have that

$$
A _ { \mathrm { T T } } ^ { j k } = \left( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \right) A _ { + } + \left( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \right) A _ { \times } ,
$$

![](images/ddc8ff02c64b35ee74ec034aa32994e032c7f109ea68d292e1fcaf0ba4c82148.jpg)  
Relation between the detector basis $( e _ { 1 } , e _ { 2 } )$ and the transverse basis $( e \chi , e \gamma )$ .

and substitution within Eq. (11.313) produces

$$
S ( t ) = F _ { + } A _ { + } ( t - R / c ) + F _ { \times } A _ { \times } ( t - R / c ) ,
$$

in which

$$
\begin{array} { l } { { F _ { + } : = \displaystyle \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) \big ( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \big ) , } } \\ { { F _ { \times } : = \displaystyle \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) \big ( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \big ) , } } \end{array}
$$

are the detector pattern functions of the laser interferometer, which describe the angular response of the detector to each gravitational-wave polarization. Note that in general, the detector measures a linear superposition of the gravitational-wave polarizations.

To calculate $F _ { + }$ and $F _ { \times }$ we must relate the detector basis $e _ { 1 }$ and $\boldsymbol { e } _ { 2 }$ to the transverse basis $e _ { X }$ and $e _ { Y }$ . We imagine that when viewed from the detector’s vantage point, the source of gravitational waves is situated in a direction $- N = [ \sin \theta \cos \phi$ , sin θ sin $\phi$ , $\cos \theta \dot { } .$ ], described by polar angles $( \theta , \phi )$ defined relative to the detector basis. The vectors $( e _ { 1 } , e _ { 2 } , e _ { 3 } )$ can then be related to $( e _ { X } , e _ { Y } , e _ { Z } )$ by a sequence of simple operations illustrated in Fig. 11.5. From the detector basis we first form an intermediate basis $( e ^ { \prime } { } _ { 1 } , e ^ { \prime } { } _ { 2 } , e ^ { \prime } { } _ { 3 } )$ by performing two elementary rotations. The first is a rotation by an angle $\phi$ around the $e _ { 3 }$ -axis, to align the rotated $e _ { 1 }$ -axis in the direction of $- N$ projected down to the 1-2 plane. The second is a rotation by an angle $\theta$ around the new $\scriptstyle { e _ { 2 } }$ -axis, to align the rotated $\mathbf { \boldsymbol { e } } _ { 3 }$ -axis in the direction of $- N$ . It is easy to show that the detector basis is related to the intermediate basis by

$$
\begin{array} { r l } & { \pmb { e } _ { 1 } = \cos \theta \cos \phi \pmb { e } ^ { \prime } _ { 1 } - \sin \phi \pmb { e } ^ { \prime } _ { 2 } + \sin \theta \cos \phi \pmb { e } ^ { \prime } _ { 3 } , } \\ & { \pmb { e } _ { 2 } = \cos \theta \sin \phi \pmb { e } ^ { \prime } _ { 1 } + \cos \phi \pmb { e } ^ { \prime } _ { 2 } + \sin \theta \sin \phi \pmb { e } ^ { \prime } _ { 3 } , } \\ & { \pmb { e } _ { 3 } = - \sin \theta \pmb { e } ^ { \prime } _ { 1 } + \cos \theta \pmb { e } ^ { \prime } _ { 3 } . } \end{array}
$$

The vectors $\boldsymbol { e } ^ { \prime } { } _ { 1 }$ and $\boldsymbol { e ^ { \prime } } _ { 2 }$ are transverse to the direction of propagation $N = - e _ { 3 } ^ { \prime }$ , but they are not equal to the transverse vectors $\pmb { e } _ { X }$ and $e _ { Y }$ . Indeed, these vectors will in general be

related by a rotation of angle $\psi$ around $N -$ recall the discussion surrounding Eq. (11.41). This rotation is described by

$$
\begin{array} { r c l } { { } } & { { } } & { { e ^ { \prime } { } _ { 1 } = \cos \psi \ e _ { X } + \sin \psi \ e _ { Y } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { e ^ { \prime } { } _ { 2 } = \sin \psi \ e _ { X } - \cos \psi \ e _ { Y } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { e ^ { \prime } { } _ { 3 } = - e _ { Z } , } } \end{array}
$$

and we see that the transformation also includes a reflection across the transverse plane, to bring the third axis in alignment with the direction of propagation. Since each vectorial basis must be right-handed, we get an unusual orientation of the $e _ { Y }$ vector relative to $\boldsymbol { e ^ { \prime } } _ { 2 }$ .

The combined transformation is

$$
\begin{array} { r l r } {  { e _ { 1 } = ( \cos \theta \cos \phi \cos \psi - \sin \phi \sin \psi ) e _ { X } + ( \cos \theta \cos \phi \sin \psi + \sin \phi \cos \psi ) e _ { Y } } } \\ & { } & { ~ - \sin \theta \cos \phi e _ { Z } , } \\ & { e _ { 2 } = ( \cos \theta \sin \phi \cos \psi + \cos \phi \sin \psi ) e _ { X } + ( \cos \theta \sin \phi \sin \psi - \cos \phi \cos \psi ) e _ { Y } } \\ & { } & { ~ - \sin \theta \sin \phi e _ { Z } , } \\ & { e _ { 3 } = - \sin \theta \cos \psi e _ { X } - \sin \theta \sin \psi e _ { Y } - \cos \theta e _ { Z } , } \end{array}
$$

and making the substitutions in Eq. (11.316) returns

$$
\begin{array} { l } { { F _ { + } = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \cos 2 \psi - \cos \theta \sin 2 \phi \sin 2 \psi , } } \\ { { F _ { \times } = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \sin 2 \psi + \cos \theta \sin 2 \phi \cos 2 \psi , } } \end{array}
$$

after simplification. We see that there are directions in the sky, for example $\textstyle \theta = { \frac { \pi } { 2 } }$ and $\textstyle \phi = { \frac { \pi } { 4 } }$ , for which the laser interferometer is unable to detect any wave.

Measurement of gravitational waves with laser interferometry does not require the arms to be perpendicular to each other, as we have taken them to be in this discussion. For the proposed space-based eLISA interferometer, for example, the angle between the arms will be $6 0 ^ { \mathrm { o } }$ . In fact, it can be shown (see Exercise (11.8) that for an interferometer whose arms make an angle $\chi$ , the response function $S ( t )$ is the same as in Eqs. (11.315) and (11.320), but with the overall response reduced by a factor of sin χ . This simple result follows when the arms are oriented symmetrically in the laboratory basis, so that each arm makes the same angle $\begin{array} { r } { \frac { \pi } { 4 } - \frac { 1 } { 2 } \chi } \end{array}$ with respect to the $e _ { 1 }$ and $\boldsymbol { e } _ { 2 }$ axes.

# 11.6 Bibliographical notes

The physics of gravitational waves features a wealth of aspects that could not all be covered in this book, even in such a long chapter. For a more comprehensive treatment the reader is invited to consult the few books devoted entirely to this rich subject, including Saulson (1994), Maggiore (2007), and Creighton and Anderson (2011).

The quadrupole-formula controversy described in $\mathrm { B o x } \ 1 1 . 2$ is related in much more detail in Daniel Kennefick’s wonderful book Traveling at the Speed of Thought, published in 2007; the phrase is due to Eddington (1922), who was referring specifically to the unphysical gauge modes contained in the theory. The Einstein–Rosen paper eventually appeared in 1937 in the Journal of the Franklin Institute, a publication that specializes in engineering and applied mathematics; the identity of the mysterious Physical Review referee was finally revealed by Kennefick in his 2005 Physics Today article. Another reference cited in Box 11.2 is Ehlers et al. (1976), and a useful summary of the controversy is presented in Walker and Will (1980).

The gravitational-wave polarizations corresponding to a binary system in eccentric motion (Sec. 11.2.2) were first calculated by Wahlquist (1987). The elastic deformation of a neutron star and its potential for gravitational-wave emissions (Sec. 11.2.3) has been investigated by a number of researchers; representative papers are Ushomirsky, Cutler and Bildsten (2000) and Owen (2005). Gravitational waves produced during tidal encounters (Sec. 11.2.4) were first studied by Turner (1977) and Will (1983).

Wagoner and Will (1976) were the first to calculate the post-Newtonian corrections to the gravitational-wave signal of a binary system, though with considerably less rigor than displayed in Secs. 11.3 and 11.4. Our calculations are patterned after Will and Wiseman (1996), who actually carry them out through second post-Newtonian order; the final results for the polarizations $h _ { + }$ and $h _ { \times }$ (through 2pn order) are neatly presented in Blanchet et al. (1996). Higher-order post-Newtonian calculations are reviewed in Blanchet (2006), and at the time of writing, the most recent results on $3 . 5 \mathrm { { P N } }$ waveforms were obtained by Faye et al. (2012).

The physics of gravitational-wave detectors, touched upon ever so briefly in Sec. 11.5, is described much more thoroughly in Saulson (1994), Maggiore (2007), and Creighton and Anderson (2011). A nice introduction to the workings of a laser interferometric detector is provided by Black and Gutenkunst (2003).

# 11.7 Exercises

11.1 Consider a gravitational-wave field $h ^ { \alpha \beta }$ in the far-away wave zone, satisfying the harmonic gauge condition. Prove by direct calculation that

$$
R _ { 0 j 0 k } = - { \frac { 1 } { 2 c ^ { 2 } } } \mathrm { ( T T ) } _ { p q } ^ { j k } \partial _ { \tau \tau } h ^ { p q } .
$$

11.2 We know that in the far-away wave zone, the effective energy-momentum pseudotensor falls off at least as fast as $R ^ { - 2 }$ . Thus we can write the relaxed Einstein equation in harmonic gauge in the form

$$
\begin{array} { r } { \boxed { \ d } h ^ { \alpha \beta } = O ( R ^ { - 2 } ) . } \end{array}
$$

Show that the general solution of this equation is given by

$$
h ^ { \alpha \beta } = \frac { { \cal A } ^ { \alpha \beta } ( \tau , N ) } { { \cal R } } + { \cal O } ( R ^ { - 2 } ) ,
$$

where $A ^ { \alpha \beta }$ is an arbitrary function of $\tau = t - R / c$ and the unit vector $N$ . Show that the harmonic gauge condition $\partial _ { \beta } h ^ { \alpha \beta } = 0$ gives rise to the constraint

$$
\partial _ { \tau } { \cal A } ^ { \alpha 0 } - N _ { j } \partial _ { \tau } { \cal A } ^ { \alpha j } = { \cal O } ( R ^ { - 1 } ) .
$$

11.3 An alternative way to study the polarizations of gravitational waves in the far-away wave zone is to focus on the Riemann tensor, and to exploit the fact that the waves, to lowest order in post-Minkowskian theory, propagate along null directions with respect to the background Minkowski spacetime. The idea, following Ted Newman and Roger Penrose, is to express the components of $R _ { \alpha \beta \gamma \delta }$ on a basis of complex null vectors, defined by

$$
\begin{array} { c c } { { \ell ^ { \alpha } : = ( 1 , N ) , } } & { { \quad n ^ { \alpha } : = \frac { 1 } { 2 } ( 1 , - N ) , } } \\ { { m ^ { \alpha } : = \frac { 1 } { \sqrt { 2 } } ( 0 , \vartheta + \mathrm { i } \varphi ) , } } & { { \quad \bar { m } ^ { \alpha } : = \frac { 1 } { \sqrt { 2 } } ( 0 , \vartheta - \mathrm { i } \varphi ) . } } \end{array}
$$

Here $\ell ^ { \alpha }$ is an outgoing null vector tangent to the gravitational waves, $n ^ { \alpha }$ is an ingoing null vector, and $\pmb { \vartheta }$ and $\varphi$ are defined as in Eqs. (11.37) and (11.38). Complex conjugation converts $m ^ { \alpha }$ to $\bar { m } ^ { \alpha }$ and vice versa.

(a) Prove the following properties of the basis vectors:

$$
\begin{array} { c } { { \ell _ { \alpha } = - c \partial _ { \alpha } ( t - R / c ) , \qquad n _ { \alpha } = - \frac { c } { 2 } \partial _ { \alpha } ( t + R / c ) , } } \\ { { \ell _ { \alpha } \ell ^ { \alpha } = n _ { \alpha } n ^ { \alpha } = m _ { \alpha } m ^ { \alpha } = \bar { m } _ { \alpha } \bar { m } ^ { \alpha } = 0 , } } \\ { { \ell _ { \alpha } n ^ { \alpha } = - 1 , \qquad m _ { \alpha } \bar { m } ^ { \alpha } = 1 , } } \\ { { \eta ^ { \alpha \beta } = - 2 \ell ^ { ( \alpha } n ^ { \beta ) } + 2 m ^ { ( \alpha } \bar { m } ^ { \beta ) } . } } \end{array}
$$

(b) Assume that the Riemann tensor in the far-away wave zone can be expressed as ${ \cal R } _ { \alpha \beta \gamma \delta } = A _ { \alpha \beta \gamma \delta } / R + O ( R ^ { - 2 } )$ , in which $A _ { \alpha \beta \gamma \delta }$ is an arbitrary function of retarded time $\tau : = t - R / c$ and the unit vector $N$ . Show that

$$
\partial _ { \mu } R _ { \alpha \beta \gamma \delta } = - { \frac { 1 } { c } } \ell _ { \mu } \partial _ { \tau } R _ { \alpha \beta \gamma \delta } + O ( R ^ { - 2 } ) .
$$

(c) Making use of this differentiation rule, use the linearized Bianchi identities

$$
\partial _ { \epsilon } R _ { \alpha \beta \gamma \delta } + \partial _ { \delta } R _ { \alpha \beta \epsilon \gamma } + \partial _ { \gamma } R _ { \alpha \beta \delta \epsilon } = 0
$$

to show that only the six components $R _ { n p n q }$ can be non-zero, where the indices $( p , q )$ run over the values $\ell , m$ , and $\bar { m }$ . In this notation, for example, $R _ { n \ell n \ell }$ stands for $R _ { \alpha \beta \gamma \delta } n ^ { \alpha } \ell ^ { \beta } n ^ { \gamma } \ell ^ { \delta }$ . You may ignore any constant of integration that arises when integrating with respect to retarded time.

(d) Calculate the Ricci tensor, and show that the vacuum Einstein field equations give rise to the four additional constraints

$$
R _ { n \ell n \ell } = R _ { n \ell n m } = R _ { n \ell n \bar { m } } = R _ { n m n \bar { m } } = 0 .
$$

Show that there are only two unconstrained components, represented by $R _ { n m n m }$ and its complex conjugate (or equivalently, by its real and imaginary parts). These are the gravitational-wave modes, as represented by the Riemann tensor.

(e) Show that the link between the remaining components of the Riemann tensor and the gravitational-wave polarizations is provided by

$$
R _ { n m n m } = - \frac { 1 } { 2 c ^ { 2 } } \partial _ { \tau \tau } h _ { m m } = - \frac { 1 } { 2 c ^ { 2 } } \partial _ { \tau \tau } ( h _ { + } + \mathrm { i } h _ { \times } ) .
$$

11.4 Consider the Landau–Lifshitz formulation of the Einstein field equations, as reviewed in Sec. 6.1.1. Assuming that the Landau–Lifshitz pseudotensor falls off as $R ^ { - 2 }$ in the far-away wave zone, the vacuum field equations can be expressed as

$$
\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu } = { \cal O } ( R ^ { - 2 } ) ,
$$

where $H ^ { \alpha \mu \beta \nu } : = \mathfrak { g } ^ { \alpha \beta } \mathfrak { g } ^ { \mu \nu } - \mathfrak { g } ^ { \alpha \mu } \mathfrak { g } ^ { \beta \nu }$ . We wish to formulate these equations in a gauge g g g gthat is not harmonic. Instead we choose to impose the gauge conditions

$$
h ^ { 0 j } = 0 , \qquad \eta _ { \mu \nu } h ^ { \mu \nu } = 0 ,
$$

in which $h ^ { \alpha \beta } : = \eta ^ { \alpha \beta } - \mathfrak { g } ^ { \alpha \beta }$ .

g(a) Write out the (00), $( 0 j )$ and $( j k )$ field equations explicitly, using the gauge conditions to simplify the expressions. Keep the equations linear in $h ^ { \alpha \beta }$ , and set the right-hand sides equal to zero; the $O ( R ^ { - 2 } )$ residuals are not important for this problem.

(b) Show that the field equations are invariant under a further gauge transformation described by

$$
h ^ { \alpha \beta }  h ^ { \alpha \beta } - \partial ^ { \alpha } \zeta ^ { \beta } - \partial ^ { \beta } \zeta ^ { \alpha } + ( \partial _ { \mu } \zeta ^ { \mu } ) \eta ^ { \alpha \beta } ,
$$

in which $\zeta ^ { \alpha }$ is chosen to preserve the four conditions already adopted.

(c) Show that the residual gauge freedom can be exploited to express the gravitational potentials in the TT gauge. (d) Show that the field equations then reduce to wave equations for $h _ { \mathrm { T T } } ^ { j k }$ .

11.5 In this problem we examine the response of a free particle to a gravitational wave propagating in the $z$ -direction, in the reference frame of an observer. In the absence of other forces, the particle’s motion relative to the observer is governed by Eq. (11.28). Let the particle undergo a small displacement relative to an unperturbed location at a distance $L$ from the observer. This is described by $\xi ^ { j } ( t ) = ( L + \delta \xi ) e ^ { j }$ , in which $\delta \xi$ depends on time, and the direction $e ^ { j }$ is expressed in terms of polar angles $\theta$ and $\phi$ .

(a) Show that

$$
\frac { d } { d t } \delta \xi = \frac { 1 } { 2 } { \cal L } \sin ^ { 2 } \theta \left( \cos 2 \phi \partial _ { \tau } h _ { + } + \sin 2 \phi \partial _ { \tau } h _ { \times } \right) ,
$$

where $h _ { + }$ and $h _ { \times }$ are the gravitational-wave polarizations as measured in the observer’s reference frame.

(b) Letting $h _ { + } = A _ { + }$ cos $\omega t$ and $h _ { \times } = A _ { \times } \sin \omega t$ , calculate $\scriptstyle { \frac { 1 } { 2 } } m \langle ( d \delta \xi / d t ) ^ { 2 } \rangle$ , the timeaveraged kinetic energy of the particle, as a function of $A _ { + }$ , $A _ { \times } , \omega$ , and direction.

(c) The “antenna pattern” of this gravitational-wave detector is defined to be the averaged kinetic energy acquired by the particle for a given orientation relative to the incident wave, divided by the maximum kinetic energy. Plot the antenna pattern as a function of $\theta$ and $\phi$ for each polarization. Present them as parametric plots, either as 3D plots or as 2D plots in various planes. Discuss the properties of the patterns.

11.6 Consider an array of particles that are able to move freely in the $x - y$ plane. A gravitational wave impinges on the plane in the $z$ direction. It is described by polarizations $h _ { + }$ and $h _ { \times }$ defined relative to the $x$ -y- $z$ basis.

(a) Calculate the acceleration field $\ddot { \pmb \xi }$ experienced by the particles. Draw the lines of force in the $x - y$ plane when the wave is a pure $^ +$ polarization, and when it is a pure $\times$ polarization. How does the pattern change when the wave is a linear superposition of each polarization?

(b) Show that the local surface density of the particles is not affected by the gravitational wave, to first order in $h _ { + }$ and $h _ { \times }$ . Hint: Evaluate the divergence of the displacement velocity field, $\boldsymbol { \nabla } \cdot \dot { \boldsymbol { \xi } }$ .

(c) Show that the integral of the acceleration field around a closed path in the $x - y$ plane always vanishes. Conclude that the acceleration field can be expressed as the gradient of a potential $\Phi _ { \mathrm { G W } }$ ,

$$
\ddot { \pmb { \xi } } = \nabla \Phi _ { \mathrm { G W } } .
$$

Determine $\Phi _ { \mathrm { G W } }$ in terms of $h _ { + }$ and $h _ { \times }$ .

11.7 The gravitational analogue of electromagnetic bremsstrahlung is a process in which a body of mass $m _ { 1 }$ passes by a body of mass $m _ { 2 }$ and is scattered by a small angle. This is the limit in which $v ^ { 2 } \gg G m / b$ , where $m$ is the total mass and $^ b$ is the distance of closest approach. We still assume that $v \ll c$ , and in this problem we employ the quadrupole formula to calculate the gravitational waves produced by the encounter.

The process corresponds to a Newtonian hyperbolic orbit with a very large eccentricity $e \gg 1$ . (For $e > 1$ the semimajor axis $a$ is not defined, but the semilatus rectum $p$ is related as always to $h$ , the angular momentum per unit reduced mass, by $h ^ { 2 } = G m p$ .) We introduce the velocity at infinity defined by $v _ { \infty } ^ { 2 } : = 2 \varepsilon$ , where $\varepsilon$ is the conserved energy per unit reduced mass, and we define the impact parameter $b : = p / e$ .

(a) Using the Keplerian orbit formulae derived in Chapter 3, establish the following relations, assuming that the orbit is confined to the $x - y$ plane, and that the orbit’s pericenter is aligned with the $x$ direction (so that $\omega = 0$ ):

$$
\begin{array} { l } { { \displaystyle v _ { \infty } = \sqrt { \frac { G m } { p } } e \biggl [ 1 - \frac { 1 } { 2 } e ^ { - 2 } + O ( e ^ { - 4 } ) \biggr ] , } } \\ { { \displaystyle r = \frac { b } { \cos \phi } \biggl [ 1 - \frac { 1 } { e \cos \phi } + O ( e ^ { - 2 } ) \biggr ] , } } \\ { { \displaystyle v = v _ { \infty } \bigl [ - e ^ { - 1 } \sin \phi , 1 + e ^ { - 1 } \cos \phi , 0 \bigr ] + O ( e ^ { - 2 } ) . } } \end{array}
$$

(b) Integrate the orbital equation for $\phi$ to leading order in $e ^ { - 1 }$ , and show that

$$
\sin \phi = \frac { v _ { \infty } t } { ( b ^ { 2 } + v _ { \infty } ^ { 2 } t ^ { 2 } ) ^ { 1 / 2 } } + O ( e ^ { - 1 } ) , \qquad \cos \phi = \frac { b } { ( b ^ { 2 } + v _ { \infty } ^ { 2 } t ^ { 2 } ) ^ { 1 / 2 } } + O ( e ^ { - 1 } ) .
$$

(c) Using the quadrupole formula, and taking the waves to be propagating in the direction of the vector $N = [ \sin \vartheta \cos \varphi$ , sin $\vartheta$ sin $\varphi$ , cos $\vartheta$ ], show that the gravitational-wave polarizations are given by

$$
h _ { + , \times } = \frac { 2 \eta ( G m ) ^ { 2 } } { c ^ { 4 } b R } { \cal A } _ { + , \times } ,
$$

in which $\eta : = m _ { 1 } m _ { 2 } / m ^ { 2 }$ and

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { + } = - \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \vartheta ) \big [ \cos 2 \varphi ( C _ { 1 } + 2 C _ { 3 } ) + 2 \sin 2 \varphi ( S _ { 1 } + S _ { 3 } ) \big ] } } \\ { ~ - \frac { 1 } { 2 } \sin ^ { 2 } \vartheta C _ { 1 } , } \\ { { \displaystyle { \cal A } _ { \times } = - \cos \vartheta \big [ 2 \cos 2 \varphi ( S _ { 1 } + S _ { 3 } ) - \sin 2 \varphi ( C _ { 1 } + 2 C _ { 3 } ) \big ] } , } \end{array}
$$

where $C _ { n } : = \cos ^ { n } \phi$ and $S _ { n } : = \sin \phi \cos ^ { n - 1 } \phi$ . An unobservable constant contribution to $h _ { + , \times }$ has been dropped.

(d) Plot $A _ { + }$ and $A _ { \times }$ as a function of time in units of $t _ { 0 } = b / v _ { \infty }$ for the following sets of directions (in degrees): $( \vartheta , \varphi ) = ( 0 , 0 )$ , (45, 0), (90, 0), (90, 45), (90, 90), (45, 90), and (60, 54.7), the last point corresponding to a direction in a plane tilted 45 degrees relative to the orbital plane, and 45 degrees from the $y$ -direction in this plane. Running the plots from $t = - 1 0 t _ { 0 }$ to $t = + 1 0 t _ { 0 }$ will reveal the salient features.   
(e) Some of the waveforms have an unusual feature. What is it? Discuss whether it might be observable to any practical gravitational wave detector.

11.8 Show that the angular pattern functions for an interferometer whose arms make an angle $\chi$ with each other are the same as in Eqs. (11.320), but multiplied by sin $\chi$ . Hint: Orient the arms in the 1-2 plane so that each one makes an angle $\textstyle { \frac { \pi } { 4 } } - { \frac { 1 } { 2 } } \chi$ with respect to the $e _ { 1 }$ and $\scriptstyle { e _ { 2 } }$ axes.

In Chapters 8, 9, and 10 we examined gravitational phenomena that take place in the near zone, the region of space which contains the source of the gravitational field, and which is confined to a radius $R$ that is much smaller than $\lambda _ { c }$ , the characteristic wavelength of the emitted radiation. This near-zone physics excluded radiative phenomena, and the dynamics of the system was entirely conservative. In Chapter 11 we moved to the wave zone, situated at a distance $R$ that is much larger than $\lambda _ { c }$ , and studied the gravitational waves produced by processes taking place in the near zone; this wave-zone physics is all about radiative phenomena. In the first part of this chapter we continue our exploration of wave-zone physics by describing how gravitational waves transport energy, momentum, and angular momentum away from their source. These radiative losses imply that the near-zone physics cannot be strictly conservative, and in the second part of the chapter we identify the radiation-reaction forces which produce the required dissipation within the system. This chapter, therefore, is all about the linkage between the near and wave zones.

Radiative losses and radiation reaction are subtle topics in general relativity, and the mathematical description of these phenomena is technically demanding. To ease our entry into this subject, in Sec. 12.1 we first review the situation in the simpler context of flatspacetime electromagnetism. We return to gravity in Sec. 12.2, in which we develop a general description of radiative losses in general relativity. This relies on two major pillars: the Landau–Lifshitz formulation of the Einstein field equations, as reviewed in Chapter 6, and a shortwave approximation, in which the gravitational potentials are expanded in powers of $\lambda _ { c } / R \ll 1$ ; this approximation is quite independent of the post-Newtonian and post-Minkowskian expansions introduced in previous chapters. In Sec. 12.3 we apply the general formalism to slowly-moving systems, thereby incorporating a post-Newtonian expansion within the shortwave approximation. In this context the radiative losses can be computed in terms of the mass and current multipole moments of the matter distribution; at the leading order we obtain the famous quadrupole formula for the rate at which gravitational waves remove energy from the system. In Sec. 12.4 we explore a number of astrophysical implications of these radiative losses.

In Sec. 12.5 we return to the near zone and identify the gravitational potentials that are involved in the dissipative dynamics of the system; these radiation-reaction terms are seen to occur at $2 . 5 \mathrm { { P N } }$ order in a post-Newtonian expansion of the potentials. We apply them to fluid dynamics in Sec. 12.6, and to the motion of an $N$ -body system in Sec. 12.7. In Sec. 12.8 we simplify the description of the radiation-reaction potentials and forces by constructing transformations from the original (harmonic) spacetime coordinates to alternative coordinates; as special cases we shall encounter the Burke–Thorne and Schafer ¨ radiation-reaction gauges. And finally, in Sec. 12.9 we analyze the equations that govern the dissipative dynamics of a binary system of gravitating bodies, focusing on the secular changes that occur in the orbital motion.

# 12.1 Radiation reaction in electromagnetism

Before we mount our direct attack on radiative losses and radiation reaction in gravitating systems, we take a moment to explore these themes in the simpler context of electromagnetism. To keep the discussion as simple as possible we ignore gravity entirely (so that the spacetime is flat), and we assume that the motion of the charged bodies is slow. This restricted situation is sufficient for our purposes: it features all of the essential physics that we shall encounter in the gravitational case, and this physics can be explored without the conceptual and technical difficulties that appear in the gravitational case. We shall describe the major differences between the two cases at the end of this section.

# 12.1.1 System of charged bodies

As in Chapter 9 we examine a system of well-separated bodies moving under the influence of their mutual interactions; each body consists of a perfect fluid described by its mass density $\rho$ , pressure $p$ , and velocity field $\pmb { v }$ . What is new here is that each body also possesses a charge distribution described by a charge density $\rho _ { e }$ and a current density $j _ { e } = \rho _ { e } v$ , and that the interaction between bodies is mediated by electromagnetism instead of gravity.

Once more we work in terms of the center-of-mass variables that were first introduced in Sec. 1.6.5. The mass of body $A$ is $\textstyle m _ { A } : = \int _ { A } \rho d ^ { 3 } x$ , and its center-of-mass is situated at $\begin{array} { r } { \pmb { r } _ { A } : = m _ { A } ^ { - 1 } \int _ { A } \rho \pmb { x } d ^ { 3 } x } \end{array}$ . The velocity vector of body $A$ is $\begin{array} { r } { \pmb { \upsilon } _ { A } : = m _ { A } ^ { - 1 } \int _ { A } \rho \pmb { v } d ^ { 3 } x } \end{array}$ , and its acceleration is given by

$$
m _ { A } \pmb { a } _ { A } : = \int _ { A } \rho \frac { d \pmb { v } } { d t } d ^ { 3 } \pmb { x } .
$$

In addition to these quantities we introduce the body’s total charge

$$
q _ { A } : = \int _ { A } \rho _ { e } d ^ { 3 } x ,
$$

which we take to be non-vanishing. Each body is assumed to be reflection-symmetric about its center-of-mass, in the sense specified back in Sec. 9.1.2. And each body is assumed to be moving slowly, in the sense that $v _ { A } \ll c$ . This implies that the bodies are situated deep within the near zone, as was first explained back in Sec. 6.3.2.

The total dipole moment of the charge distribution plays an important role in our discussion. This vector is defined by

$$
\pmb { I } _ { e } ( t ) : = \int \rho _ { e } \pmb { x } d ^ { 3 } \boldsymbol { x } ,
$$

and the continuity equation $\partial _ { t } \rho _ { e } + \nabla \cdot \boldsymbol { j } _ { e } = 0$ ensures that its time derivative is given by

$$
\dot { I } _ { e } = \int j _ { e } d ^ { 3 } x .
$$

The total dipole moment can also be expressed as $\begin{array} { r } { I _ { e } = \sum _ { A } \int _ { A } \rho _ { e } ( \pmb { r } _ { A } + \pmb { \bar { x } } ) d ^ { 3 } \pmb { \bar { x } } } \end{array}$ , with $\bar { x }$ denoting the position of a fluid element relative to the center-of-mass of each body. Integration of $\rho _ { e } \bar { x }$ produces zero when the charge distribution is reflection-symmetric about the center-of-mass, and under these circumstances we obtain the simple expression

$$
I _ { e } = \sum _ { A } q _ { A } { \pmb { r } } _ { A }
$$

for the total dipole moment.

The equations that govern the coupled dynamics of the bodies and their electromagnetic field consist of Maxwell’s equations

$$
\begin{array} { l } { \displaystyle \nabla \cdot \boldsymbol { E } = \frac { 1 } { \epsilon _ { 0 } } \rho _ { e } , } \\ { \displaystyle \nabla \cdot \boldsymbol { B } = 0 , } \\ { \displaystyle \nabla \times \boldsymbol { E } = - \frac { \partial \boldsymbol { B } } { \partial t } , } \\ { \displaystyle \nabla \times \boldsymbol { B } = \mu _ { 0 } \boldsymbol { j } _ { e } + \epsilon _ { 0 } \mu _ { 0 } \frac { \partial \boldsymbol { E } } { \partial t } , } \end{array}
$$

in which $E$ is the electric field and $\pmb { B }$ the magnetic field, and the generalization of Euler’s equation given by

$$
\rho \frac { d \pmb { v } } { d t } = - \pmb { \nabla } p + \rho _ { e } ( \pmb { E } + \pmb { v } \times \pmb { B } ) .
$$

The coupling constants $\epsilon _ { 0 }$ and $\mu _ { 0 }$ are related to the speed of light by $\epsilon _ { 0 } \mu _ { 0 } = c ^ { - 2 }$

Substitution of Eq. (12.7) into Eq. (12.1) yields

$$
m _ { A } \pmb { a } _ { A } = \int _ { A } \rho _ { e } \pmb { E } d ^ { 3 } \pmb { x } + \int _ { A } \rho _ { e } \pmb { v } \times \pmb { B } d ^ { 3 } \pmb { x } .
$$

Our first task in this section is to evaluate the right-hand side of Eq. (12.8) to leading order in an expansion in powers of $v _ { A } / c$ , which we shall refer to a “post-Coulombian expansion,” in an obvious analogy with the post-Newtonian expansions of preceding chapters. The answer, of course, is the well known Coulomb law, given by Eq. (12.18) below. We shall, nevertheless, provide a fairly detailed derivation of this equation, because this allows us to establish a number of results used in the derivation of the radiation-reaction force in Sec. 12.1.4.

# 12.1.2 Motion of charged bodies

To obtain $\pmb { a } _ { A }$ we must first compute the fields $E$ and $\pmb { B }$ , and this requires integration of Maxwell’s equations. The homogeneous equations are solved automatically when we

express the fields as

$$
\boldsymbol { E } = - \frac { \partial \boldsymbol { A } } { \partial t } - \nabla \Phi , \qquad \boldsymbol { B } = \nabla \times \boldsymbol { A } ,
$$

in terms of a vector potential $\pmb { A }$ and a scalar potential $\Phi$ . The potentials can be freely altered by a gauge transformation of the form $\Phi  \Phi - \partial _ { t } \chi$ , $\pmb { A }  \pmb { A } + \pmb { \nabla } \chi$ , in which $\chi$ is an arbitrary scalar function; the transformation leaves the fields unchanged. The gauge freedom can be exploited to enforce the Lorenz gauge condition

$$
\pmb { \nabla } \cdot \pmb { A } + \frac { 1 } { c ^ { 2 } } \frac { \partial \Phi } { \partial t } = 0 ,
$$

and in this gauge the inhomogeneous Maxwell equations reduce to the wave equations

$$
\ d \Pi \Phi = - 4 \pi \kappa \rho _ { e } , \qquad \ d \Pi = - \frac { 4 \pi \kappa } { c ^ { 2 } } \pmb { j } _ { e } ,
$$

for the potentials; here $\kappa : = ( 4 \pi \epsilon _ { 0 } ) ^ { - 1 }$ .

The solutions to the wave equations are

$$
\begin{array} { l } { \Phi ( t , \pmb { x } ) = \kappa \displaystyle \int \frac { \rho _ { e } ( t - | \pmb { x } - \pmb { x } ^ { \prime } | / c , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ { \pmb { A } ( t , \pmb { x } ) = \displaystyle \frac { \kappa } { c ^ { 2 } } \displaystyle \int \frac { \pmb { j } _ { e } ( t - | \pmb { x } - \pmb { x } ^ { \prime } | / c , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \end{array}
$$

in which the integration domains are limited to the volume occupied by the charge distribution. Techniques to evaluate such retarded integrals in the near zone were developed in Sec. 6.3.4. The main strategy is to express the delayed time dependence of each source function as a Taylor expansion about the current time $t$ . For example, we express the charge density $\rho _ { e }$ as

$$
\begin{array} { l } { \displaystyle \rho _ { e } ( t - | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | / c ) = \rho _ { e } - \frac { 1 } { c } | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | \frac { \partial \rho _ { e } } { \partial t } + \frac { 1 } { 2 c ^ { 2 } } | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | ^ { 2 } \frac { \partial ^ { 2 } \rho _ { e } } { \partial t ^ { 2 } } } \\ { \displaystyle - \frac { 1 } { 6 c ^ { 3 } } | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | ^ { 3 } \frac { \partial ^ { 3 } \rho _ { e } } { \partial t ^ { 3 } } + O ( c ^ { - 4 } ) , } \end{array}
$$

in which each term on the right-hand side is evaluated at time $t$ ; the slow-motion condition ensures that each term is smaller than the preceding one by a factor of order $v _ { A } / c$ .

To leading order in a post-Coulombian expansion (0pc order), the scalar potential is given by $\Phi = U _ { e } + O ( c ^ { - 2 } )$ , where

$$
U _ { e } ( t , \pmb { x } ) = \kappa \int \frac { \rho _ { e } ( t , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime }
$$

is an instantaneous potential of a sort encountered before in the context of Newtonian and post-Newtonian gravity. It is easy to show that the term of order $c ^ { - 1 }$ in $\Phi$ vanishes by virtue of charge conservation. The corresponding expression for the vector potential is of order $c ^ { - 2 }$ and makes no leading-order contribution to the equations of motion; it participates at 1pc order, along with the neglected terms of order $c ^ { - 2 }$ in $\Phi$ .

Substitution of the potentials into Eq. (12.9), and these fields into Eq. (12.8), produces

$$
m _ { A } a _ { A } ^ { j } = - \int _ { A } \rho _ { e } \partial _ { j } U _ { e } d ^ { 3 } x ^ { \prime } + { \cal O } ( c ^ { - 2 } ) ,
$$

an expression that is familiar from Newtonian gravity. As in Chapters 1 and 9 the potential can be decomposed as $U _ { e } = U _ { e , A } + U _ { e , \lnot A }$ , in terms of a piece $U _ { e , A }$ sourced by body $A$ and an external piece $U _ { e , \lnot A }$ sourced by the remaining bodies. As before the body’s self-field does not contribute to the force, and the external potential can be expressed as a Taylor expansion about the center-of-mass $r _ { A }$ – refer to Eq. (9.89). Our assumption that the bodies are well separated allows us to retain only the leading term in this expansion, and we arrive at

$$
m _ { A } a _ { A } ^ { j } = - q _ { A } \partial _ { j } U _ { e , - A } ( t , \pmb { r } _ { A } ) + O ( c ^ { - 2 } ) .
$$

In addition to the post-Coulombian corrections of order $c ^ { - 2 }$ , this expression for the force neglects terms that are smaller by a factor of order $( R _ { A } / r _ { A B } ) ^ { 2 } \ll 1$ , in which $R _ { A }$ is the size of body $A$ while $r _ { A B }$ is the typical inter-body distance.

The remaining steps are also familiar from Chapters 1 and 9. We differentiate the external potential, evaluate the result at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ , and take the limit of well-separated bodies. We arrive at

$$
\partial _ { j } U _ { e , - \it A } ( t , \boldsymbol { r } _ { A } ) = - \sum _ { B \neq A } \kappa q _ { B } \frac { n _ { A B } ^ { j } } { r _ { A B } ^ { 2 } } ,
$$

where ${ \pmb n } _ { A B } : = ( { \pmb r } _ { A } - { \pmb r } _ { B } ) / | { \pmb r } _ { A } - { \pmb r } _ { B } |$ is a unit vector that points from body $B$ to body $A$ , and $r _ { A B } : = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ . Our final expression for the force acting on body $A$ is then

$$
m _ { A } \pmb { a } _ { A } = \sum _ { B \neq A } \frac { \kappa q _ { A } q _ { B } } { r _ { A B } ^ { 2 } } \pmb { n } _ { A B } + O ( c ^ { - 2 } ) ,
$$

a result that can be obtained directly from Newtonian gravity by making the replacements $G  \kappa$ , $m _ { A }  - q _ { A }$ (on the right-hand side of the equation only), and $m _ { B }  q _ { B }$ . Slowmotion electromagnetism, like slow-motion gravity, is characterized by a force that is inversely proportional to the squared distance. The main difference concerns the product of charges: while $m _ { A } m _ { B }$ is necessarily positive in gravity, $q _ { A } q _ { B }$ can be of either sign in electromagnetism; the force can be repulsive as well as attractive.

The (mechanical plus field) energy of the system of charged bodies is given by

$$
E = \sum _ { A } \frac { 1 } { 2 } m _ { A } v _ { A } ^ { 2 } + \sum _ { A } \sum _ { B \neq A } \frac { \kappa q _ { A } q _ { B } } { 2 r _ { A B } } + O ( c ^ { - 2 } ) ,
$$

and it is easy to show that the motion keeps the energy constant: $d E / d t = 0$ . The slowmotion dynamics of charged bodies is conservative.

# 12.1.3 Radiative losses

The system, however, is known to emit electromagnetic waves, and the radiation takes energy away from the system. The rate at which it does so, to leading order in a

post-Coulombian expansion of the radiation, is given by the electric dipole formula,

$$
\mathcal { P } = \frac { 2 \kappa } { 3 c ^ { 3 } } \vert \ddot { I } _ { e } \vert ^ { 2 } + O ( c ^ { - 5 } ) ,
$$

in which $\mathcal { P }$ is the total energy radiated per unit time, and $\ddot { I } _ { e }$ is the electric dipole moment of Eq. (12.5) differentiated twice with respect to time. The terms of order $c ^ { - 5 }$ in Eq. (12.20) are produced by changes in the magnetic dipole moment and electric quadrupole moment of the charge distribution; higher-order terms are produced by changes in higher-order multipole moments. For a system consisting of a single charged body moving on an accelerated trajectory, we have $\ddot { I } _ { e } = q \pmb { a }$ , where $\pmb { a }$ is the acceleration, and this yields the well-known Larmor formula $\mathcal { P } = ( 2 \kappa q ^ { 2 } / 3 c ^ { 2 } ) | \pmb { a } | ^ { 2 }$ .

The radiative losses described by the electric dipole formula are not accounted for in the conservative dynamics described in the preceding subsection. We should expect, however, that a more accurate treatment of the equations of motion would convert the statement $d E / d t = 0$ into something like $d E / d t = - \mathcal { P }$ , which properly expresses conservation of total (mechanical plus field plus radiation) energy in the presence of dissipation. This is our second main task in this section: To identify the radiation-reaction terms in the equations of motion, and to show that these produce (something like) the expected energy-balance equation. The change in the system’s energy will correspond to the rate at which the radiation-reaction forces do work on the bodies. This is expressed mathematically by

$$
\frac { d E } { d t } = \sum _ { A } \pmb { F } _ { A } [ \mathbf { r } \mathbf { r } ] \cdot \pmb { v } _ { A } ,
$$

in which $F _ { A } [ \mathrm { r r } ]$ is the radiation-reaction force acting on body $A$

# 12.1.4 Radiation reaction

Because the radiated power $\mathcal { P }$ scales as $c ^ { - 3 }$ to leading order in a post-Coulombian expansion, our improved treatment of the equations of motion must include terms of order $c ^ { - 3 }$ in order to account for radiation-reaction effects. A systematic post-Coulombian expansion of the equations of motion would therefore commence with Eq. (12.18) at leading order, then incorporate 1pc terms at order $c ^ { - 2 }$ , $1 . 5 \mathrm { { p c } }$ terms at order $c ^ { - 3 }$ , 2pc terms at order $c ^ { - 4 }$ , and so on. Here we shall jump directly from 0pc order to $1 . 5 \mathrm { { p c } }$ order, and bypass the additional conservative terms that appear at 1pc order; we shall not pursue the post-Coulombian expansion beyond this point.

That radiation-reaction terms should appear in the equations of motion with an odd power of $c ^ { - 1 }$ reflects a deep fact about radiating systems, that they necessarily break the time-reversal invariance of the underlying theory. Here the radiation is electromagnetic in nature, and the theory is Maxwell’s electrodynamics. Later in the chapter the radiation is gravitational in nature, and the theory is Einstein’s general relativity. In each case the fundamental theory is time-reversal invariant, but the selected solutions specify a direction for the arrow of time.

In the present context the choice of direction was made in Eqs. (12.12), when we selected the retarded solutions to the wave equations satisfied by the potentials. This choice is physically well motivated: it produces fields that are causally related to the source (the field now depends on the past behavior of the source), it produces waves that are propagating outward, and it produces a transfer of energy away from the source. But to select the retarded solutions is a choice nevertheless, and this choice is not dictated by the fundamental equations of Maxwell’s theory. We could easily make a different choice and adopt instead the advanced solutions to the wave equations. This would produce fields that are in an anti-causal relation with the source (the field now would depend on the future behavior of the source), radiation that is propagating inward, and a transfer of energy towards the source. In terms of radiation reaction, the advanced solutions would give rise to an equation of the form $d E / d t = + \mathcal { P }$ instead of the expected $d E / d t = - \mathcal { P }$ , and this would express the (unphysical) fact that the incoming radiation brings energy to the system. And because $d E / d t$ is related to the radiation-reaction force by Eq. (12.21), we see that the switch from retarded to advanced solutions changes the sign of ${ \cal F } _ { A } ^ { \mathrm { r r } }$ .

These considerations lead directly to the expectation that the radiation-reaction force should involve odd powers of $c ^ { - 1 }$ only, because an advanced solution to the wave equation can be obtained from a retarded solution by making the substitution $c  - c$ . Such a change in the sign of $c$ turns outgoing waves into incoming waves, turns the flow of energy from outward to inward, and changes the sign of the radiation-reaction force. All terms that come with odd powers of $c ^ { - 1 }$ in the potentials $\Phi$ and $\pmb { A }$ therefore contribute to the radiation-reaction force; terms that come with even powers of $c ^ { - 1 }$ do not change sign under the substitution $c  - c$ , and these give rise to the purely conservative part of the force. To leading order in a post-Coulombian expansion, the radiation-reaction force comes from terms that scale as $c ^ { - 3 }$ in $\Phi$ and $\pmb { A }$ .

To obtain the radiation-reaction piece of $\Phi$ we return to Eq. (12.13), pluck out the term of order $c ^ { - 3 }$ , and insert it within Eq. (12.12). Proceeding similarly with $\pmb { A }$ , we get

$$
\begin{array} { l } { { \Phi _ { \mathrm { r r } } = - \displaystyle \frac { \kappa } { 6 c ^ { 3 } } \displaystyle \frac { \partial ^ { 3 } } { \partial t ^ { 3 } } \int \rho _ { e } ( t , x ^ { \prime } ) | x - x ^ { \prime } | ^ { 2 } d ^ { 3 } x ^ { \prime } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle { \cal A } _ { \mathrm { r r } } = - \displaystyle \frac { \kappa } { c ^ { 3 } } \displaystyle \frac { d } { d t } \int j _ { e } ( t , x ^ { \prime } ) d ^ { 3 } x ^ { \prime } + { \cal O } ( c ^ { - 5 } ) . } } \end{array}
$$

Further manipulations using Eqs. (12.3) and (12.4) reveal that the radiation-reaction potentials are given by

$$
\begin{array} { l } { \displaystyle \Phi _ { \mathrm { r r } } = \frac { \kappa } { 6 c ^ { 3 } } \Big ( 2 \boldsymbol { x } \cdot \dddot { \boldsymbol { I } _ { e } } - \dddot { \boldsymbol { I } } _ { e } ^ { k k } \Big ) + O ( c ^ { - 5 } ) , } \\ { \displaystyle } \\ { \displaystyle { A _ { \mathrm { r r } } = - \frac { \kappa } { c ^ { 3 } } \ddot { \boldsymbol { I } } _ { e } + O ( c ^ { - 5 } ) , } } \end{array}
$$

where $\begin{array} { r } { I _ { e } ^ { k k } : = \int \rho _ { e } r ^ { 2 } d ^ { 3 } x } \end{array}$ is the trace of the quadrupole-moment tensor of the charge distribution. In the scalar potential the electric dipole moment $I _ { e }$ is differentiated three times with respect to $t$ ; in the vector potential it is differentiated twice.

The radiation-reaction fields are obtained by inserting the potentials within Eq. (12.9). This yields

$$
E _ { \mathrm { r r } } = \frac { 2 \kappa } { 3 c ^ { 3 } } \dddot { \mathbf { I } } _ { e } + O ( c ^ { - 5 } ) , \qquad B _ { \mathrm { r r } } = O ( c ^ { - 5 } ) .
$$

We see that the magnetic field vanishes at leading order, and that the electric field depends on $t$ only; it is uniform within the distribution of charge. Substitution of the fields into Eq. (12.8) produces

$$
\boldsymbol { F } _ { \boldsymbol { A } } [ \mathrm { r r } ] = \frac { 2 \kappa } { 3 c ^ { 3 } } q _ { \boldsymbol { A } } \overleftrightarrow { \boldsymbol { I } } _ { { e } } + \boldsymbol { O } ( c ^ { - 5 } ) .
$$

This is the radiation-reaction force acting on body $A$ .

# 12.1.5 Energy balance

The total energy of the system is given by Eq. (12.19), and differentiation of the right-hand side with respect to $t$ gives rise to Eq. (12.21), noting that the work done by the conservative piece of the force accounts for the changes in the system’s potential energy. Substitution of Eq. (12.25) produces

$$
\frac { d E } { d t } = \frac { 2 \kappa } { 3 c ^ { 3 } } \dddot { I } _ { e } \cdot \sum _ { A } q _ { A } \pmb { v } _ { A } = \frac { 2 \kappa } { 3 c ^ { 3 } } \dddot { I } _ { e } \cdot \dot { I } _ { e } ,
$$

where we have made use of Eq. (12.5). This can also be expressed as

$$
\frac { d E } { d t } = \frac { d } { d t } \bigg ( \frac { 2 \kappa } { 3 c ^ { 3 } } \ddot { \pmb { I } } _ { e } \cdot \pmb { I } _ { e } \bigg ) - \frac { 2 \kappa } { 3 c ^ { 3 } } \big | \ddot { \pmb { I } } _ { e } \big | ^ { 2 }
$$

by transferring a time derivative from one dipole moment to the other. This, finally, we write in the form

$$
\frac { d E } { d t } = - \frac { d E ^ { \prime } } { d t } - \mathcal { P } ,
$$

where

$$
E ^ { \prime } : = - \frac { 2 \kappa } { 3 c ^ { 3 } } \ddot { \pmb { I } } _ { e } \cdot \pmb { I } _ { e }
$$

has the dimension of an energy, and $\mathcal { P }$ is the radiated power of Eq. (12.20).

Equation (12.28) is our statement of energy balance, the expression of conservation of total (mechanical plus field plus radiation) energy. We see, however, that the statement is not quite the expected $d E / d t = - \mathcal { P }$ ; the additional term $- d E ^ { \prime } / d t$ requires an interpretation.

The statement of Eq. (12.28) forces us to recognize that the exchange of energy between the charged bodies and the electromagnetic field may take different forms. First, the kinetic energy of the bodies may change, and so can the system’s potential energy, as defined by the second term on the right-hand side of Eq. (12.19); these changes are accounted for by the term $d E / d t$ in Eq. (12.28). Second, part of the system’s energy is converted into radiation, which propagates outward and irreversibly leaves the system; this is described by the term $- \mathbb { P }$ in Eq. (12.28). But potential energy and radiation are not the only relevant forms of field energy; there is also a form that stays bound to the system and is reversibly exchanged between the electromagnetic field and the charged bodies. This is what is described by $E ^ { \prime }$ , as defined by Eq. (12.29). Equation (12.28) therefore describes an exchange between all relevant forms of energy: kinetic, potential, radiation, and bound field energy.

There are ways by which the statement of Eq. (12.28) can be simplified and turned into the expected $d E / d t = - \mathcal { P } .$ . One way is to assume that the conservative motion is periodic, or that it begins and ends in a static state, and to average Eq. (12.28) over time. This produces a coarse-grained statement of energy balance,

$$
\langle d E / d t \rangle = - \langle \mathcal { P } \rangle .
$$

The contribution from $d E ^ { \prime } / d t$ no longer appears, because its average is proportional to the total change in $E ^ { \prime }$ over the time interval, and this vanishes at order $c ^ { - 3 }$ under the stated conditions. Another way is to modify the definition of the system’s total energy so that it now includes the bound field energy $E ^ { \prime }$ . The redefinition $E  E + E ^ { \prime }$ obviously turns Eq. (12.28) into the simpler statement $d E / d t = - \mathcal { P }$ .

<table><tr><td>Box 12.1</td><td>Redefining the energy</td></tr><tr><td></td><td>The reader might fel that it is inappropriate to redefine the energy E for the sole purpose of obtaining a desired statement of energy balance. We wish to reassure the reader: there was nothing sacred about the initial definition of the system&#x27;s energy,and a redefinition can be entirely appropriate.It is helpful to recall thatthe energy is not some rigid quantity defined apriori,but that its definition is provided by the dynamics ofthe mechanical system.Fora conservative system,itis whateverfunctionofthe positions and velocities that happens to be conserved. Because the zero point of energy is not fixed (at least at the non-quantum level), the definition is not even unique.</td></tr></table>

Energy is not even conserved for radiative systems, and its definition is even more ambiguous. A good definition of energy would be one that is approximately constant when the radiation can be ignored, and one that accurately reflects the long-term behavior of the system under the damping effects of the radiation leaving the system. The short-term behavior reveals fluctuations caused by a reversible transfer of energy between the system and the field, and an ambiguity arises because it is impossible to decompose the field energy into a piece that is unambiguously associated with the reversible transfer, and another piece that is unambiguously associated with the radiation. The ambiguity, however, is largely irrelevant when the fluctuations are small compared with the dominant contribution to the energy, which is approximately conserved in the short term.

In the electromagnetic case examined here, the Coulombian energy $E$ is of order $m v ^ { 2 } \sim \kappa q ^ { 2 } / r$ , and the field energy $E ^ { \prime }$ can be seen from Eq. (12.29) to be of order $\kappa ^ { 2 } q ^ { 4 } v / ( m c ^ { 3 } r ^ { 2 } ) \sim E ( v / c ) ^ { 3 }$ . This is a small correction that leads to a small ambiguity.

These remarks apply to any dissipative system. They keep their relevance when we turn to gravity, and establish an equivalence between the work done by the radiation-reaction forces and the energy carried away by gravitational waves.

# 12.1.6 Looking ahead: gravity

The remainder of this chapter is devoted to a discussion of radiative losses and radiation reaction in the context of gravity. The conservative dynamics of fluids and bodies moving under a mutual gravitational attraction was explored in Chapters 8, 9, and 10, where the equations of motion were obtained accurately through the first post-Newtonian order. The gravitational waves emitted by these bodies were examined in Chapter 11, and our first order of business in this chapter (Sec. 12.2) is to calculate the rates at which the waves transport energy, linear momentum, and angular momentum away from the system. In the case of radiated energy, we shall derive (Sec. 12.3) the famous quadrupole formula, the gravitational analogue of Eq. (12.20); because there is no dipole radiation in general relativity, the radiated power $\mathcal { P }$ must involve the quadrupole-moment tensor of the mass distribution. Astrophysical consequences of radiative losses are explored in Sec. 12.4. We then (Sec. 12.5) obtain the gravitational potentials – analogous to those of Eqs. $( 1 2 . 2 3 ) -$ that give rise to the gravitational radiation-reaction force, which is computed and applied in Secs. 12.6 through 12.9.

The treatment of the gravitational case involves computations that are much more challenging than those reviewed in this section. The reason for this is two-fold. First, general relativity, even in its weak-field and slow-motion formulation, is intrinsically more complicated than Maxwell’s electrodynamics. And second, the absence of dipole radiation implies that the radiated power scales as $c ^ { - 5 }$ instead of $c ^ { - 3 }$ , which was the scaling observed in electromagnetism. This implies that the radiation-reaction terms in the equations of motion will appear at order $c ^ { - 5 }$ in a post-Newtonian expansion, an order that is far removed from the $c ^ { - 2 }$ order that was achieved back in Chapter 9. In terms of the usual post-Newtonian counting, we are looking for terms of $2 . 5 \mathrm { { P N } }$ order in the equations of motion, while the results obtained in Chapter 9 are accurate only through 1pn order. A systematic treatment of the equations of motion to this order of accuracy would have to provide conservative terms at $2 \mathrm { P N }$ order in addition to the desired terms at $2 . 5 \mathrm { { p N } }$ order. It is a fortunate circumstance, however, that the derivation of the radiation-reaction terms at $2 . 5 \mathrm { { p N } }$ order is insensitive to the details that appear at 2pn order. We may, therefore, bypass the 2pn terms entirely, and jump directly to the radiation-reaction terms that actually interest us. This is analogous to what was observed in the electromagnetic case: the radiationreaction terms at order $c ^ { - 3 }$ could be derived independently of the conservative corrections at order $c ^ { - 2 }$ .

The difficulties associated with radiative losses and radiation reaction in gravity are not just technical in nature. There are also conceptual issues that arise as a consequence of the principle of equivalence. Consider a freely-moving observer in spacetime. As was discussed at length in Chapter 5, such an observer moves without ever noticing a local gravitational field, and would therefore assign a zero value to any proposed measure of gravitational energy flux. This is quite unlike the value that he would assign to the Poynting vector $\mu _ { 0 } ^ { - 1 } E \times B$ , which measures the flux of electromagnetic energy. Given, then, that the principle of equivalence forbids the very existence of a “gravitational Poynting vector,” how is one to calculate the total radiated power P? In electromagnetism one simply integrates the normal component of the Poynting vector over a spherical surface situated in the wave zone, and the result is the electric-dipole formula of Eq. (12.20). A corresponding recipe is harder to identify in general relativity, and any proposed recipe must be handled with care in light of the principle of equivalence. That systems of moving bodies governed by gravitational interactions must lose energy to gravitational radiation is, however, very clear on physical grounds.

# 12.2 Radiative losses in gravitating systems

Our main task in this section is to establish the validity of balance equations for energy, momentum, and angular momentum, and to find expressions for the rates at which gravitational waves carry energy, momentum, and angular momentum away from their source. We pursue a dual goal: to provide a sound foundation for a discussion of radiative losses, and to develop a practical formalism to calculate these losses.

# 12.2.1 Balance equations

Our description of radiative losses in gravitating systems relies on the Landau–Lifshitz formulation of the Einstein field equations reviewed in Sec. 6.1; in particular, it relies on the conservation identities derived in Sec. 6.1.3. These consist of balance equations involving the energy, linear momentum, and angular momentum of the gravitating system. The energy-balance equation was first displayed in Eq. (6.30), which we copy here as

$$
\frac { d E } { d t } = - \mathcal { P } ,
$$

where $E = M c ^ { 2 }$ is the total energy contained in the system, as defined by Eq. (6.36), while

$$
{ \mathcal { P } } : = c \oint _ { \infty } ( - g ) t _ { \mathrm { L L } } ^ { 0 k } d S _ { k }
$$

is the rate at which gravitational waves remove energy from the system. The momentumbalance equation was first displayed in Eq. (6.31), which we copy as

$$
\frac { d P ^ { j } } { d t } = - \mathcal { F } ^ { j } ,
$$

where $P ^ { j }$ is the total momentum of the system, as defined by Eq. (6.37), while

$$
\mathcal { F } ^ { j } : = \oint _ { \infty } ( - g ) t _ { \mathrm { L L } } ^ { j k } d S _ { k }
$$

is the rate at which gravitational waves remove (linear) momentum from the system. And finally, the statement of conservation of angular momentum is

$$
\frac { d J ^ { j k } } { d t } = - \mathcal { T } ^ { j k } ,
$$

where $J ^ { j k }$ is the total angular-momentum tensor, as defined by Eq. (6.38), while

$$
\mathbb { T } ^ { j k } : = \oint _ { \infty } \left[ x ^ { j } ( - g ) t _ { \mathrm { L L } } ^ { k n } - x ^ { k } ( - g ) t _ { \mathrm { L L } } ^ { j n } \right] d S _ { n }
$$

is the rate at which gravitational waves remove angular momentum from the system; Eq. (12.35) is a re-statement of Eq. (6.34). The angular-momentum vector is given by $\begin{array} { r } { J ^ { j } = { \frac { 1 } { 2 } } \epsilon _ { p q } ^ { j } J ^ { p q } } \end{array}$ , and we may define a “gravitational-wave torque vector” by $\begin{array} { r } { \mathcal { T } ^ { j } : = \frac { 1 } { 2 } \epsilon _ { \ p q } ^ { j } \mathcal { T } ^ { p q } } \end{array}$ , so that $d J ^ { j } / d t = - \mathcal { T } ^ { j }$ . In these equations, $t _ { \mathrm { L L } } ^ { \alpha \beta }$ is the Landau–Lifshitz pseudotensor of Eq. (6.5). The surface integrals are evaluated in the limit $R \to \infty$ , and $d S _ { j } = R ^ { 2 } N _ { j } d \Omega$ is an outward-directed surface element; we use the notation of Chapter 11, with $R : = | { \boldsymbol { x } } |$ , $N : = x / R$ , and $d \Omega$ is an element of solid angle in the direction of the unit vector $N$ .

The Landau–Lifshitz formulation of the Einstein field equations supplies a sound foundation for a description of radiative losses because it achieves three essential goals: first, it provides expressions for the radiative fluxes $\mathcal { P }$ , $\mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ ; second, it provides definitions for the total energy $E$ , total momentum $P ^ { j }$ , and total angular momentum $J ^ { j k }$ ; and third, it establishes precise balance equations that describe how $E , \ P ^ { j }$ , and $J ^ { j k }$ change as a result of gravitational-wave emissions. It should be pointed out that this formulation is not unique: a different formulation of the Einstein field equations, based on other variables, other coordinate systems, and a different choice of pseudotensors, may well produce different definitions for $E$ , $P ^ { j }$ , and $J ^ { j k }$ , and different expressions for $\mathcal { P }$ , $\mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ . These differences are of no concern, however, so long as the proposed definitions for $E$ , $P ^ { j }$ , and $J ^ { j k }$ are physically sensible. As we have seen previously in Secs. 7.3.2, 8.4.5, and 8.4.6, the Landau–Lifshitz definitions, when implemented within post-Minkowskian theory or post-Newtonian theory, are physically sensible.

# 12.2.2 The shortwave approximation

We begin by evaluating the gravitational-wave fluxes $\mathcal { P }$ , $\mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ . We wish to do so in a framework that is broader than, but includes, the post-Minkowskian approximation formulated in Chapters 6 and 7. The post-Minkowskian approximation is based on an expansion of the gravitational potentials $h ^ { \alpha \beta }$ in powers of the gravitational constant $G$ . Our approach here is distinct, and our expressions will be accurate to all orders in $G$ . Our approach is based on a different type of approximation, which, following Misner, Thorne, and Wheeler (1973), we term shortwave approximation. It relies on the fact that we are interested in the gravitational potentials in the far-away wave zone, as introduced in Sec. 11.1.1. In this region of spacetime $R$ is much larger than $\lambda _ { c }$ , the characteristic wavelength of the gravitational radiation, and we exploit this fact by using $\lambda _ { c } / R \ll 1$ as an expansion parameter. The shortwave approximation has already been invoked within the context of post-Minkowskian theory in Chapter 7, refer to $\mathrm { B o x } ~ 7 . 7$ , and it has also been invoked independently of the post-Minkowskian approximation back in Sec. 11.1. In this subsection we develop it more systematically.

The shortwave approximation is based on an expansion of the gravitational potentials in powers of $\lambda _ { c } / R$ , where $R : = | { \boldsymbol { x } } |$ is the distance to the system’s center-of-mass. We write

$$
h ^ { \alpha \beta } = ( \lambda _ { c } / R ) f _ { 1 } ^ { \alpha \beta } + ( \lambda _ { c } / R ) ^ { 2 } f _ { 2 } ^ { \alpha \beta } + \cdot \cdot \cdot ,
$$

in which $f _ { n } ^ { \alpha \beta }$ is assumed to be a function of retarded time $\tau : = t - R / c$ and the angles contained in the unit vector $N : = x / R$ . In Sec. 11.1 the shortwave expansion was truncated at leading order; here we keep track of higher-order terms, because they are needed in our computation of the angular-momentum flux $\mathcal { T } ^ { j k }$ . As was pointed out previously, each $f _ { n } ^ { \alpha \beta }$ can be considered to be accurate to all orders in the gravitational constant $G$ . A refined formulation of the approximation would involve the insertion of ln $R$ terms in Eq. (12.37) to accommodate the presence of wave tails in the gravitational potentials, refer to Sec. 11.3.7.

Our considerations below are not affected by these logarithmic terms, and for simplicity we prefer to omit them from the expressions.

The assumed dependence of $f _ { n } ^ { \alpha \beta }$ on retarded time $\tau : = t - R / c$ is motivated by the fact that according to Eq. (6.51), the gravitational potentials must satisfy a wave equation of the form $\Pi h ^ { \alpha \beta } = - ( 1 6 \pi G / c ^ { 4 } ) \tau ^ { \alpha \beta }$ , where $\tau ^ { \alpha \beta }$ is the effective energy-momentum pseudotensor of Eq. (6.52). By virtue of the scaling of $h ^ { \alpha \beta }$ with $\lambda _ { c } / R$ , $\tau ^ { \alpha \beta }$ is guaranteed to be of order $( { \lambda _ { c } } / R ) ^ { 2 }$ , and this implies that the time dependence of $f _ { 1 } ^ { \alpha \beta }$ must be contained in the combination $t - R / c$ . The same dependence is then fed into the remaining terms in the expansion. These considerations rely on the fact that the gravitational potentials are taken to satisfy the harmonic gauge condition of Eq. (6.49), $\partial _ { \beta } h ^ { \alpha \beta } = 0$ .

Differentiation of the potentials is facilitated by employing the identities $\partial _ { j } R = N _ { j }$ and $\partial _ { j } N _ { k } = P _ { j k } / R$ , where $P _ { j k } : = \delta _ { j k } - N _ { j } N _ { k }$ . Recalling that $x ^ { 0 } = c t$ and using these differentiation rules, we obtain

$$
\begin{array} { l } { { c \partial _ { 0 } h ^ { \alpha \beta } = ( \lambda _ { c } / R ) \partial _ { \tau } f _ { 1 } ^ { \alpha \beta } + ( \lambda _ { c } / R ) ^ { 2 } \partial _ { \tau } f _ { 2 } ^ { \alpha \beta } + \dots , } } \\ { { c \partial _ { j } h ^ { \alpha \beta } = - ( \lambda _ { c } / R ) N _ { j } \partial _ { \tau } f _ { 1 } ^ { \alpha \beta } } } \\ { { \qquad - ( \lambda _ { c } / R ) ^ { 2 } \biggl ( N _ { j } \partial _ { \tau } f _ { 2 } ^ { \alpha \beta } + \frac { c } { \lambda _ { c } } N _ { j } f _ { 1 } ^ { \alpha \beta } - \frac { c } { \lambda _ { c } } P _ { j } ^ { k } \frac { \partial f _ { 1 } ^ { \alpha \beta } } { \partial N ^ { k } } \biggr ) + \cdot \cdot \cdot } } \end{array}
$$

The expansion of $c \partial _ { j } h ^ { \alpha \beta }$ contains a number of contributions at second order. It is easy to see that the term involving $f _ { 2 } ^ { \alpha \beta }$ is smaller than the leading term by a factor of order $\lambda _ { c } / R \ll 1$ The terms involving $f _ { 1 } ^ { \alpha \beta }$ are multiplied by $c / \lambda _ { c } = 1 / t _ { c }$ , where $t _ { c }$ is the characteristic time scale associated with changes in the potentials, and $( c / \lambda _ { c } ) f _ { 1 } ^ { \alpha \beta }$ is comparable in size to $\partial _ { \tau } f _ { 1 } ^ { \alpha \beta }$ ; these terms also are smaller than the leading term by a factor of order $\lambda _ { c } / R \ll 1$ .

To leading order in the shortwave approximation we can write that

$$
\partial _ { \mu } h ^ { \alpha \beta } = - \frac { 1 } { c } k _ { \mu } \partial _ { \tau } h ^ { \alpha \beta } + { \cal O } ( \lambda _ { c } ^ { 2 } / R ^ { 2 } ) ,
$$

in which $k _ { \mu } : = ( - 1 , N )$ is a spacetime vector that satisfies the null condition $\eta ^ { \mu \nu } k _ { \mu } k _ { \nu } = 0$ . At this order the only spatial dependence that matters is contained in the overall factor of $R ^ { - 1 }$ and in the proper time $\tau$ ; the dependence contained in the vector $N$ is subdominant, and appears at the next order.

# 12.2.3 Energy and momentum fluxes

To compute $\mathcal { P }$ and $\mathcal { F } ^ { j }$ we insert Eq. (12.39) within the Landau–Lifshitz pseudotensor of Eq. (6.5) and get, after much simplification,

$$
( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta } = \frac { c ^ { 2 } } { 3 2 \pi G } \Big ( \partial _ { \tau } h _ { \mathrm { T T } } ^ { j k } \partial _ { \tau } h _ { j k } ^ { \mathrm { T T } } \Big ) k ^ { \alpha } k ^ { \beta } ,
$$

where $k ^ { \alpha } = ( 1 , N )$ and

$$
h _ { \mathrm { T T } } ^ { j k } = ( \mathrm { T T } ) _ { p q } ^ { j k } h ^ { p q } , \qquad ( \mathrm { T T } ) _ { p q } ^ { j k } : = P _ { p } ^ { j } P _ { q } ^ { k } - \frac 1 2 P ^ { j k } P _ { p q } ,
$$

is the transverse-tracefree piece of the gravitational potentials, as defined back in Sec. 11.1.7. This result is invariant under any gauge transformation (described in Sec. 11.1.5)

that preserves the harmonic gauge conditions $\partial _ { \beta } h ^ { \alpha \beta } = 0$ . The easiest way to establish Eq. (12.40) is therefore to refine the harmonic gauge to the TT gauge of Sec. 11.1.5, in which $h ^ { 0 0 } = O ( \lambda _ { c } ^ { 2 } / R ^ { 2 } )$ , $h ^ { 0 j } = O ( \lambda _ { c } ^ { 2 } / R ^ { 2 } )$ , and $h ^ { j \bar { k } } = h _ { \mathrm { T T } } ^ { j k } + O ( \bar { \lambda _ { c } ^ { 2 } } / \bar { R } ^ { 2 } )$ ; the properties $N _ { j } h _ { \mathrm { T T } } ^ { j k } = 0 = \delta _ { j k } h _ { \mathrm { T T } } ^ { j k }$ simplify the calculations significantly.

The expression of Eq. (12.40) is valid to leading order in an expansion in powers of $\lambda _ { c } / R$ ; it is of second order, and it neglects terms of order $( \lambda _ { c } / R ) ^ { 3 }$ . This expression is sufficiently accurate for substitution within Eqs. (12.32) and (12.34), and we immediately obtain

$$
\mathcal { P } = \frac { c ^ { 3 } } { 3 2 \pi G } \int R ^ { 2 } \Big ( \partial _ { \tau } h _ { \mathrm { T T } } ^ { p q } \partial _ { \tau } h _ { p q } ^ { \mathrm { T T } } \Big ) d \Omega
$$

and

$$
\mathcal { F } ^ { j } = \frac { c ^ { 2 } } { 3 2 \pi G } \int R ^ { 2 } N ^ { j } \left( \partial _ { \tau } h _ { \mathrm { T T } } ^ { p q } \partial _ { \tau } h _ { p q } ^ { \mathrm { T T } } \right) d \Omega .
$$

Because the integral is evaluated in the limit $R \to \infty$ , higher-order terms in the expansion of $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ do not contribute to $\mathcal { P }$ and $\mathcal { F } ^ { j }$ . The expressions of Eqs. (12.42) and (12.43) are exact.

The energy and momentum fluxes can alternatively be expressed in terms of the gravitational-wave polarizations $h _ { + }$ and $h _ { \times }$ introduced in Sec. 11.1.7. These are defined by the decomposition

$$
h _ { \mathrm { T T } } ^ { j k } = h _ { + } \big ( \vartheta ^ { j } \vartheta ^ { k } - \varphi ^ { j } \varphi ^ { k } \big ) + h _ { \times } \big ( \vartheta ^ { j } \varphi ^ { k } + \varphi ^ { j } \vartheta ^ { k } \big )
$$

of the TT field in terms of the transverse basis provided by the unit vectors $\vartheta : =$ [cos $\vartheta$ cos $\varphi$ , co $\boldsymbol { \mathfrak { s o } } \otimes \mathrm { s i n } \varphi , - \sin \vartheta ]$ and $\varphi : = [ - \sin \varphi , \cos \varphi , 0 ]$ ; these were introduced in Eqs. (11.37) and (11.38) and they are orthogonal to $N : = [ \sin \vartheta \cos \varphi , \sin \vartheta \sin \varphi , \cos \vartheta ]$ . After inserting this decomposition within Eqs. (12.42) and (12.43) we obtain

$$
\mathcal { P } = \frac { c ^ { 3 } } { 1 6 \pi G } \int R ^ { 2 } \Big [ \big ( \partial _ { \tau } h _ { + } \big ) ^ { 2 } + \big ( \partial _ { \tau } h _ { \times } \big ) ^ { 2 } \Big ] d \Omega
$$

and

$$
{ \mathcal { F } } ^ { j } = { \frac { c ^ { 3 } } { 1 6 \pi G } } \int R ^ { 2 } N ^ { j } \Bigl [ \bigl ( \partial _ { \tau } h _ { + } \bigr ) ^ { 2 } + \bigl ( \partial _ { \tau } h _ { \times } \bigr ) ^ { 2 } \Bigr ] d \Omega .
$$

These expressions, like Eqs. (12.42) and (12.43), are exact within the shortwave approximation. They are also accurate to all orders in a post-Minkowskian expansion of the potentials in powers of $G$ .

# 12.2.4 Angular-momentum flux

The leading-order expression of Eq. (12.40), unfortunately, is not sufficiently accurate for insertion within Eq. (12.36). This can be seen from that fact that since $( - g ) t _ { \mathrm { L L } } ^ { j k }$ is proportional to $N ^ { j } N ^ { k }$ , the integrand in Eq. (12.36) is proportional to $( N ^ { j } N ^ { k } - N ^ { k } N ^ { j } ) N ^ { n }$ and therefore vanishes. This is actually a fortunate circumstance, because the presence of $x ^ { j } = R N ^ { j }$ within the integral implies that $\mathcal { T } ^ { j k }$ would otherwise diverge in the limit

$R \to \infty$ . The computation of the angular-momentum flux, therefore, requires terms of order $( \lambda _ { c } / R ) ^ { 3 }$ in the expansion of the energy-momentum pseudotensor.

# The result

It is wise to state the final answer before we present this long calculation:

$$
\Im ^ { j k } = \frac { c ^ { 3 } } { 1 6 \pi G } \int R ^ { 2 } \biggl [ h _ { \mathrm { T T } } ^ { j p } \partial _ { \tau } h _ { \mathrm { T T } } ^ { k p } - h _ { \mathrm { T T } } ^ { k p } \partial _ { \tau } h _ { \mathrm { T T } } ^ { j p } - \frac { 1 } { 2 } \partial _ { \tau } h _ { \mathrm { T T } } ^ { p q } \bigl ( x ^ { j } \partial ^ { k } - x ^ { k } \partial ^ { j } \bigr ) h _ { p q } ^ { \mathrm { T T } } \biggr ] d \Omega .
$$

Notice that when $x ^ { j } \partial ^ { k } - x ^ { k } \partial ^ { j }$ acts on the spatial dependence contained in $\tau : = t - R / c$ within $h _ { p q } ^ { \mathrm { T T } }$ , or on the overall $1 / R$ dependence, it produces $x ^ { j } N ^ { k } - x ^ { k } N ^ { j }$ , which vanishes identically; the operation is sensitive only to the angular dependence contained in $N$ within $h _ { p q } ^ { \mathrm { T T } }$ . In terms of the gravitational-wave polarizations we have

$$
\mathcal { T } ^ { j k } = - \frac { c ^ { 3 } } { 1 6 \pi G } \int R ^ { 2 } q ^ { j k } d \Omega
$$

with

$$
\begin{array} { r l } & { q ^ { j k } : = \big ( \partial _ { \tau } h _ { + } \big ) \bigg [ \big ( x ^ { j } \partial ^ { k } - x ^ { k } \partial ^ { j } \big ) h _ { + } - 2 \mathrm { c o s e c } \vartheta \big ( e _ { z } ^ { j } \varphi ^ { k } - \varphi ^ { j } e _ { z } ^ { k } \big ) h _ { \times } \bigg ] } \\ & { \qquad + \big ( \partial _ { \tau } h _ { \times } \big ) \bigg [ \big ( x ^ { j } \partial ^ { k } - x ^ { k } \partial ^ { j } \big ) h _ { \times } + 2 \mathrm { c o s e c } \vartheta \big ( e _ { z } ^ { j } \varphi ^ { k } - \varphi ^ { j } e _ { z } ^ { k } \big ) h _ { + } \bigg ] , } \end{array}
$$

where $\pmb { e } _ { z } : = [ 0 , 0 , 1 ]$ is a constant unit vector that points in the direction of the $z$ axis, relative to which the polar angles $( \vartheta , \varphi )$ are defined. To go from Eq. (12.47) to Eq. (12.48) we had to account for the spatial dependence of the transverse basis vectors. If the polarizations are expressed as functions of $\tau , \vartheta$ , and $\varphi$ , then the non-vanishing components of $q ^ { j k }$ are given explicitly by

$$
\begin{array} { r l } & { q ^ { x y } = \bigl ( \partial _ { \tau } h _ { + } \bigr ) \bigl ( \partial _ { \varphi } h _ { + } \bigr ) + \bigl ( \partial _ { \tau } h _ { \times } \bigr ) \bigl ( \partial _ { \varphi } h _ { \times } \bigr ) , } \\ & { q ^ { y z } = \bigl ( \partial _ { \tau } h _ { + } \bigr ) \bigl ( - \sin \varphi \partial _ { \vartheta } h _ { + } - \cot \vartheta \cos \varphi \partial _ { \varphi } h _ { + } + 2 \cos \sec \vartheta \cos \varphi h _ { \times } \bigr ) } \\ & { \qquad + \bigl ( \partial _ { \tau } h _ { \times } \bigr ) \bigl ( - \sin \varphi \partial _ { \vartheta } h _ { \times } - \cot \vartheta \cos \varphi \partial _ { \varphi } h _ { \times } - 2 \cos \sec \vartheta \cos \varphi h _ { + } \bigr ) , } \\ & { q ^ { z x } = \bigl ( \partial _ { \tau } h _ { + } \bigr ) \bigl ( \cos \varphi \partial _ { \vartheta } h _ { + } - \cot \vartheta \sin \varphi \partial _ { \varphi } h _ { + } + 2 \cos \sec \vartheta \sin \varphi h _ { \times } \bigr ) } \\ & { \qquad + \bigl ( \partial _ { \tau } h _ { \times } \bigr ) \bigl ( \cos \varphi \partial _ { \vartheta } h _ { \times } - \cot \vartheta \sin \varphi \partial _ { \varphi } h _ { \times } - 2 \cos \sec \vartheta \sin \varphi h _ { + } \bigr ) . } \end{array}
$$

The expression of Eq. (12.47) was first obtained by Bryce DeWitt in 1971 while teaching a course on general relativity at Stanford University; his lecture notes, published only recently in 2011, contain very few details. The calculation was later repeated by Kip Thorne, who simply stated the final result in his 1980 review article on multipole expansions. Pending evidence to the contrary, the derivation presented below may well be the only one available in the literature.

# Derivation

We now proceed with the derivation of Eq. (12.47). Terms that give rise to the subdominant, $( { \lambda _ { c } } / { R } ) ^ { 3 }$ piece of $( - g ) t _ { \mathrm { L L } } ^ { j k }$ are displayed in Eq. (12.38); these are the second-order terms in $\partial _ { \mu } h ^ { \alpha \beta }$ generated by $\partial _ { \tau } f _ { 2 } ^ { \alpha \beta }$ , $N _ { j } f _ { 1 } ^ { \alpha \beta }$ , and derivatives of $f _ { 1 } ^ { \alpha \beta }$ with respect to the vector $N$ . In addition to these we have first-order terms in $h ^ { \alpha \beta }$ that enter in the metric $g _ { \alpha \beta }$ , which also appears in the Landau–Lifshitz pseudotensor. A computation of $( - g ) t _ { \mathrm { L L } } ^ { j k }$ that includes all these contributions would be exceedingly tedious. A careful examination, however, reveals that most do not appear in the final result for $\mathcal { T } ^ { j k }$ , because they produce terms proportional to $N ^ { j }$ that cancel out in the end. This analysis allows us to state that $f _ { 2 } ^ { \alpha \beta }$ makes no appearance in the final result, and that corrections of order $\lambda _ { c } / R$ to the Minkowski metric $\eta _ { \alpha \beta }$ are similarly irrelevant. The computation, therefore, can be carried out safely by setting $h _ { \alpha \beta } = ( \lambda _ { c } / R ) f _ { 1 } ^ { \alpha \beta }$ and $g _ { \alpha \beta } = \eta _ { \alpha \beta }$ ; derivatives of $h _ { \alpha \beta }$ , however, must be evaluated accurately to second order in $( \lambda _ { c } / R )$ , beyond the expression displayed in Eq. (12.39). As we saw previously, the computation is simplified by adopting the TT gauge for the gravitational potentials.

A suitable starting point for the computation is

$$
\begin{array} { c } { { ( - g ) t _ { \mathrm { L L } } ^ { j k } = \displaystyle \frac { c ^ { 4 } } { 1 6 \pi G } \bigg ( - \partial ^ { j } h ^ { p q } \partial _ { p } h ^ { k q } - \partial ^ { k } h ^ { p q } \partial _ { p } h ^ { j q } - \partial _ { 0 } h ^ { j p } \partial _ { 0 } h ^ { k p } } } \\ { { + \partial _ { p } h ^ { j q } \partial ^ { p } h ^ { k q } + \displaystyle \frac { 1 } { 2 } \partial ^ { j } h ^ { p q } \partial ^ { k } h _ { p q } \bigg ) , } } \end{array}
$$

which is obtained from Eq. (6.5) and simplified by incorporating the observations made in the preceding paragraph. In particular, $h ^ { j k }$ is taken to be in the TT gauge, so that $N _ { j } h ^ { j k } = 0$ and $\delta _ { j k } h ^ { j k } = 0 .$ In addition, all terms proportional to $\delta ^ { j k }$ were discarded, because they cancel out when inserted within Eq. (12.36).

In Eq. (12.51), the operator $\partial _ { j }$ is understood in the usual way as holding $t$ fixed while differentiating with respect to $x ^ { j }$ . To proceed with the calculation, we express $\partial _ { j }$ acting on a retarded function like $h ^ { p q }$ in the form

$$
\partial _ { j } h ^ { p q } = - ( N _ { j } / c ) \partial _ { \tau } h ^ { p q } + \vec { \partial } _ { j } h ^ { p q } ,
$$

where the operator $\overrightarrow { \mathrm { O } } _ { j }$ bypasses the retarded-time dependence and operates only on the remaining spatial dependence. When $\overrightarrow { \mathrm { O } } _ { j }$ acts on $h ^ { p q }$ , it generates a term of second order in $\lambda _ { c } / R$ , while acting with $\partial _ { \tau }$ produces a first-order term. Keeping our expressions accurate through order $( { \lambda _ { c } } / { R } ) ^ { 3 }$ , we find that Eq. (12.51) becomes

$$
\begin{array} { c } { { \displaystyle - g ) t _ { \mathrm { L L } } ^ { j k } = \frac { c ^ { 3 } } { 1 6 \pi G } \bigg \{ N ^ { j } \big ( \partial _ { \tau } h ^ { p q } \big ) \Big ( \widetilde { \partial } _ { p } h ^ { k q } - \frac 1 2 \widetilde { \partial } ^ { k } h _ { p q } \Big ) + N ^ { k } \big ( \partial _ { \tau } h ^ { p q } \big ) \Big ( \widetilde { \partial } _ { p } h ^ { j q } - \frac 1 2 \widetilde { \partial } ^ { j } h _ { p q } \Big ) } } \\ { { - N ^ { p } \Big [ \big ( \partial _ { \tau } h ^ { j q } \big ) \big ( \widetilde { \partial } _ { p } h ^ { k q } \big ) + \big ( \partial _ { \tau } h ^ { k q } \big ) \big ( \widetilde { \partial } _ { p } h ^ { j q } \big ) \Big ] - \frac { 1 } { R } \big ( h ^ { j q } \partial _ { \tau } h ^ { k q } + h ^ { k q } \partial _ { \tau } h ^ { j q } \big ) \bigg \} } } \end{array}
$$

when we discard terms proportional to $N ^ { j } N ^ { k }$ that eventually cancel out, and exploit the following properties of the TT gauge: $N _ { j } \partial _ { \tau } h ^ { j k } = 0$ and $N _ { j } \eth _ { p } h ^ { j k } = - h ^ { p k } / R$ . Substitution

of Eq. (12.53) into Eq. (12.36) produces

$$
\Im ^ { j k } = \frac { c ^ { 3 } } { 1 6 \pi G } \int R ^ { 3 } \big ( \partial _ { \tau } h ^ { p q } \big ) \bigg [ N ^ { j } \ddot { \Omega } _ { p } h ^ { k q } - N ^ { k } \ddot { \Omega } _ { p } h ^ { j q } - \frac { 1 } { 2 } \big ( N ^ { j } \ddot { \Omega } ^ { k } - N ^ { k } \ddot { \Omega } ^ { j } \big ) h _ { p q } \bigg ] d \Omega .
$$

To bring Eq. (12.54) to the standard form of Eq. (12.47), it is helpful to decompose the differential operator $\overrightarrow { \mathrm { O } } _ { j }$ into longitudinal and transverse pieces according to $\Pr _ { j } =$ $N _ { j } \mathfrak { I } _ { R } + \mathfrak { J } _ { j } ^ { \mathrm { T } }$ , where $\preccurlyeq _ { R } : = N ^ { j } \preccurlyeq _ { j }$ is a partial derivative with respect to $R$ , while $\mathfrak { J } _ { j } ^ { \mathrm { T } } : = P _ { j } ^ { \ k } \mathfrak { J } _ { k }$ is the transverse derivative (related to partial derivatives with respect to $\vartheta$ and $\varphi$ ). Because $N _ { p } h ^ { p q } = 0$ , it is easy to see that $\eth _ { R }$ plays no role in the first two terms of Eq. (12.54). The next step is to integrate these terms by parts. We write

$$
\left( \partial _ { \tau } h ^ { p q } \right) N ^ { j } \ddot { \Omega } _ { p } ^ { \top } h ^ { k q } = \ddot { \Omega } _ { p } ^ { \top } \left( \partial _ { \tau } h ^ { p q } N ^ { j } h ^ { k q } \right) - \partial _ { \tau } \left( \ddot { \Omega } _ { p } ^ { \top } h ^ { p q } \right) N ^ { j } h ^ { k q } - \left( \partial _ { \tau } h ^ { p q } \right) \left( \ddot { \Omega } _ { p } ^ { \top } N ^ { j } \right) h ^ { k q } ,
$$

and observe that in the TT gauge, the harmonic condition $\partial _ { \alpha } h ^ { \alpha q } = 0$ yields

$$
\begin{array} { l } { { \partial _ { p } h ^ { p q } = - N _ { p } \partial _ { \tau } h ^ { p q } + N _ { p } \vec { \partial } _ { R } h ^ { p q } + \vec { \partial } _ { p } ^ { \Gamma } h ^ { p q } } } \\ { { \ \qquad = - N _ { p } R ^ { - 1 } h ^ { p q } + \vec { \partial } _ { p } ^ { \Gamma } h ^ { p q } } } \\ { { \ \qquad = \vec { \partial } _ { p } ^ { \Gamma } h ^ { p q } } } \\ { { \ \qquad = 0 . } } \end{array}
$$

With $\mathfrak { J } _ { p } ^ { \mathrm { T } } N ^ { j } = P _ { p } ^ { j } / R$ we find that

$$
\left( \partial _ { \tau } h ^ { p q } \right) N ^ { j } \vec { \partial } _ { p } ^ { \tau } h ^ { k q } = \vec { \partial } _ { p } ^ { \Gamma } \big ( \partial _ { \tau } h ^ { p q } N ^ { j } h ^ { k q } \big ) - \frac { 1 } { R } \big ( \partial _ { \tau } h ^ { j p } \big ) h ^ { k p } ,
$$

which we insert within Eq. (12.54). The total transverse derivative gives no contribution to the integral (because the angular domain of integration has no boundary), and we finally arrive at Eq. (12.47). At this stage the distinction between $\overrightarrow { \mathrm { O } } _ { j }$ and $\partial _ { j }$ is no longer important, because of the antisymmetry of the second group of terms in Eq. (12.47).

To go from Eq. (12.47) to Eq. (12.48) we substitute Eq. (12.44) within the integral and take into account the fact that the basis vectors $\pmb { \vartheta }$ and $\varphi$ depend on position. A simple calculation shows that their derivatives are given by

$$
\begin{array} { c } { { R \partial _ { k } \vartheta ^ { j } = - N ^ { j } \vartheta _ { k } + \cot \vartheta \varphi ^ { j } \varphi _ { k } , } } \\ { { { } } } \\ { { R \partial _ { k } \varphi ^ { j } = - N ^ { j } \varphi _ { k } - \cot \vartheta \vartheta ^ { j } \varphi _ { k } , } } \end{array}
$$

and $e _ { z }$ appears in Eq. (12.49) by virtue of the identity $\begin{array} { r } { e _ { z } = \cos \vartheta N - \sin \vartheta \vartheta } \end{array}$

The manipulations that lead to Eq. (12.50) involve the relations $x \partial _ { y } - y \partial _ { x } = \partial _ { \varphi }$ , $y \partial _ { z } -$ $z \partial _ { y } = - \sin \varphi \partial _ { \vartheta } - \cot \vartheta \cos \varphi \partial _ { \varphi }$ , and $z \partial _ { x } - x \partial _ { z } = \cos \varphi \partial _ { \vartheta } - \cot \vartheta \sin \varphi \partial _ { \varphi }$ , which are well known from the theory of orbital angular momentum in quantum mechanics.

# 12.2.5 Isaacson’s effective energy-momentum tensor

In a series of two papers published in 1968, Richard Isaacson formulated and developed the shortwave approximation of Sec. 12.2.2. His formulation was more general and ambitious than what was presented there. Instead of limiting his attention to the far-away wave zone of an asymptotically-flat spacetime, Isaacson considered a high-frequency gravitational wave in an arbitrary vacuum region of spacetime in which the radius of curvature $\mathcal { R }$ is large compared to $\lambda _ { c }$ , and developed a systematic expansion of the field equations in powers of $\lambda _ { c } / \mathcal { R }$ . Writing the exact Einstein tensor as $G ^ { \bar { \alpha } \beta } = G _ { 0 } ^ { \alpha \beta } + G _ { 1 } ^ { \alpha \beta } + G _ { 2 } ^ { \bar { \alpha } \beta } + \cdot \cdot \cdot ,$ , where $G _ { 0 } ^ { \alpha \beta }$ is the Einstein tensor of the background spacetime, $G _ { 1 } ^ { \alpha \beta }$ the correction of order $\lambda _ { c } / \mathcal { R }$ , and Gαβ2 the correction of order $( { \lambda _ { c } } / { \mathcal { R } } ) ^ { 2 }$ , he showed that $G _ { 1 } ^ { \alpha \beta } = 0$ produces a linearized propagation equation for the gravitational waves, while

$$
G _ { 0 } ^ { \alpha \beta } = \frac { 8 \pi G } { c ^ { 4 } } T _ { \mathrm { e f f } } ^ { \alpha \beta } : = - G _ { 2 } ^ { \alpha \beta } + \cdot \cdot \cdot
$$

determines how the energy-momentum in the waves affects the background spacetime. After a suitable averaging procedure to eliminate terms that oscillate rapidly, the Isaacson effective energy-momentum tensor $T _ { \mathrm { e f f } } ^ { \alpha \beta }$ can be involved in equations such as Eqs. (12.32), (12.34), and (12.36) to compute fluxes of energy, linear momentum, and angular momentum. Computation of the effective energy-momentum tensor in the far-away wave zone of an asymptotically-flat spacetime actually returns the right-hand side of Eq. (12.40), and therefore leads to the same results as Eqs. (12.42) and (12.43).

There are two reasons why the Isaacson approach fails to provide a complete foundation for the description of radiative losses in gravitating systems. First, while the Isaacson approach correctly reproduces the expressions for $\mathcal { P }$ and $\mathcal { F } ^ { j }$ that we obtained in Sec. 12.2.3, it does not provide definitions for the system’s total energy $E$ and total momentum $P ^ { j }$ . In other words, Isaacson manages to supply the right-hand sides of the balance equations (12.31) and (12.33), but fails to reveal the identity of the left-hand sides. Since the main purpose of obtaining expressions for $\mathcal { P }$ and $\mathcal { F } ^ { j }$ is to involve them in statements of energy and momentum balance, the Isaacson approach falls short of providing a complete package. The second failure of the Isaacson approach has to do with the angular-momentum flux $\mathcal { T } ^ { j k }$ . Isaacson’s effective energy-momentum tensor agrees with Eq. (12.40) in the far-away wave zone of an asymptotically-flat spacetime, but we know from Sec. 12.2.4 that this approximation is too crude to deliver the expression of Eq. (12.47); the flux of angular momentum simply cannot be calculated in the Isaacson approach.

# 12.3 Radiative losses in slowly-moving systems

As was indicated in Sec. 12.2.2, the formalism developed in Sec. 12.2 rests on a shortwave approximation which permits an expansion of the gravitational potentials in powers of $\lambda _ { c } / R \ll 1$ . This approximation scheme is quite independent of the post-Minkowskian and post-Newtonian approximations developed in preceding chapters, and the expressions for $\boldsymbol { \mathcal { P } } , \boldsymbol { \mathcal { F } ^ { j } }$ , and $\mathcal { T } ^ { j k }$ obtained in Secs. 12.2.3 and 12.2.4 have a wide domain of validity.

In this section we impose a slow-motion condition and calculate the gravitational-wave fluxes for situations in which the gravitational-wave field can be expressed as a post-Newtonian expansion. We shall derive ready-to-use expressions for $\mathcal { P }$ , $\mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ that involve multipole moments of the mass and current distribution, and recover the famous quadrupole formula for the rate at which gravitational waves carry energy away from their source. As an application of this slow-motion formalism, we shall examine the radiative losses suffered by a two-body system in bound orbital motion.

# 12.3.1 Leading-order multipole radiation

The gravitational potentials that result from a post-Minkowskian approximation of the field equations were calculated in Chapter 7, and expressions appropriate for the far-away wave zone were listed in Box 7.7. According to these expressions, the potentials are expressed as a multipole expansion,

$$
h ^ { j k } = \frac { 2 G } { c ^ { 4 } R } \biggl [ { \ddot { \mathcal { Z } } } ^ { j k } + \frac { 1 } { 3 c } \bigl ( { \dddot { \mathcal { Z } } } ^ { j k n } + 2 \epsilon ^ { m n j } { \ddot { \mathcal { J } } } ^ { m k } + 2 \epsilon ^ { m n k } { \ddot { \mathcal { J } } } ^ { m j } \bigr ) N _ { n } + O ( c ^ { - 2 } ) \biggr ] ,
$$

automatically incorporating a post-Newtonian expansion in powers of $v _ { c } / c \ll 1$ , with $v _ { c }$ denoting a characteristic velocity of the matter distribution. At the leading post-Newtonian order, the formal moments $\mathcal { T } ^ { j k } , \mathcal { T } ^ { j k n }$ , and ${ \mathcal { I } } ^ { m j }$ can be replaced by their Newtonian expressions defined in terms of the conserved density $\rho ^ { * }$ ; we have the mass quadrupole moment

$$
I ^ { j k } ( \tau ) : = \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x ,
$$

the mass octupole moment

$$
I ^ { j k n } ( \tau ) : = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } d ^ { 3 } x ,
$$

and the current quadrupole moment

$$
J ^ { j k } ( \tau ) : = \epsilon ^ { j a b } \int \rho ^ { * } x ^ { a } v ^ { b } x ^ { k } d ^ { 3 } x .
$$

In these equations, the mass density $\rho ^ { * }$ and the velocity field $\pmb { v }$ are given as functions of retarded time $\tau : = t - R / c$ and the spatial coordinates $\boldsymbol { x }$ . In Eq. (12.60) the term involving the mass quadrupole moment is the leading-order, Newtonian contribution to the gravitational-wave field, while the remaining terms are $0 . 5 \mathrm { { P N } }$ corrections that are smaller by a factor of order $v _ { c } / c \ll 1$ . Our expression for $h ^ { j k }$ neglects corrections of order $( v _ { c } / c ) ^ { 2 }$ and higher.

To properly represent the gravitational-wave field, the potentials of Eq. (12.60) must be subjected to the transverse-tracefree projection introduced in Sec. 11.1.7. According to Eqs. (11.31) and (11.34), we have that

$$
h _ { \mathrm { T T } } ^ { j k } = \left( \mathrm { T T } \right) _ { p q } ^ { j k } h ^ { p q } ,
$$

where

$$
{ ( \mathrm { { r T } ) } ^ { j } } _ { p q } ^ { j k } : = P ^ { j } _ { p } P ^ { k } _ { q } - \frac { 1 } { 2 } { P } ^ { j k } P _ { p q } , \qquad P ^ { j } _ { k } : = \delta ^ { j } _ { k } - N ^ { j } N _ { k } .
$$

To facilitate this projection it is helpful to decompose the multipole moments into their irreducible components, according to

$$
\begin{array} { l } { { { \cal I } ^ { j k } = { \cal I } ^ { \langle j k \rangle } + \displaystyle \frac { 1 } { 3 } \delta ^ { j k } { \cal I } ^ { p p } , } } \\ { { { \cal I } ^ { j k n } = { \cal I } ^ { \langle j k n \rangle } + \displaystyle \frac { 1 } { 5 } \big ( \delta ^ { j k } { \cal I } ^ { n p p } + \delta ^ { j n } { \cal I } ^ { k p p } + \delta ^ { k n } { \cal I } ^ { j p p } \big ) , } } \\ { { { \cal J } ^ { j k } = { \cal J } ^ { \langle j k \rangle } + { \cal J } ^ { [ j k ] } , } } \end{array}
$$

in which the angular brackets indicate the symmetric-tracefree operation first introduced in Sec. 1.5.3, and the square brackets indicate antisymmetrization.

In terms of the irreducible moments we have that the gravitational potentials of Eq. (12.60) can be expressed as

$$
h ^ { j k } \equiv \frac { 2 G } { c ^ { 4 } R } \bigg [ \ddot { I } ^ { \langle j k \rangle } + \frac { 1 } { 3 c } \Big ( \ddot { I } ^ { \langle j k n \rangle } + 2 \epsilon ^ { m n j } \ddot { J } ^ { \langle m k \rangle } + 2 \epsilon ^ { m n k } \ddot { J } ^ { \langle m j \rangle } \Big ) N _ { n } + O ( c ^ { - 2 } ) \bigg ] ,
$$

where the equality sign $\stackrel { \pi } { = }$ , first introduced near the end of Sec. 11.3.1, indicates that terms proportional to $\delta ^ { j k } , N ^ { j }$ , or $N ^ { k }$ have been discarded; these will not survive the TT projection of Eq. (12.64). Note that the gravitational-wave field involves only the STF pieces of the radiative multipole moments.

# 12.3.2 Leading-order fluxes

It is straightforward to insert Eq. (12.67) within the flux formulae of Eqs. (12.42), (12.43), and (12.47), evaluate the angular integrals, and arrive at

$$
\begin{array} { c } { { \displaystyle { \mathcal { P } = \frac { G } { 5 c ^ { 5 } } \ddot { I } ^ { \langle p q \rangle } \ddot { I } ^ { \langle p q \rangle } \enspace , } } } \\ { { \displaystyle { \mathcal { F } ^ { j } = \frac { G } { c ^ { 7 } } \Bigg ( \frac { 2 } { 6 3 } _ { I } ^ { ( \dot { | } p q \rangle } \ddot { I } ^ { \langle p q \rangle } - \frac { 1 6 } { 4 5 } \epsilon _ { \quad p q } ^ { j } \ddot { J } ^ { \langle p r \rangle } \ddot { I } ^ { \langle q r \rangle } \Bigg ) } , } } \\ { { \displaystyle { \Upsilon ^ { j k } = \frac { 2 G } { 5 c ^ { 5 } } \Big ( \ddot { I } ^ { \langle j p \rangle } \ddot { I } ^ { \langle k p \rangle } - \ddot { I } ^ { \langle k p \rangle } \ddot { I } ^ { \langle j p \rangle } \Big ) } . } } \end{array}
$$

We shall sketch the steps leading to these results in a moment, but we first observe that our result for $\mathcal { P }$ is the famous quadrupole formula which relates the energy radiated in gravitational waves to the quadrupole-moment tensor of the matter distribution. (Refer to Box 11.2 for a discussion of the historical controversy that has surrounded this formula.) This scales as $G / c ^ { 5 }$ , and additional contributions from higher-order multipole moments would appear at order $G / c ^ { 7 }$ and higher. Our result for $\mathcal { F } ^ { j }$ involves a coupling between the mass quadrupole and octupole moments, as well as one between the mass and current quadrupole moments; we see that $\mathcal { F } ^ { j }$ scales as $G / c ^ { 7 }$ instead of $G / c ^ { 5 }$ . Our result for the angular-momentum flux can also be expressed in terms of the torque vector $\begin{array} { r } { \mathcal { T } ^ { j } : = \frac { 1 } { 2 } \epsilon _ { \ p q } ^ { j } \mathcal { T } ^ { p q } } \end{array}$ ,

$$
\mathcal { T } ^ { j } = \frac { 2 G } { 5 c ^ { 5 } } \epsilon _ { \ p q } ^ { j } \ddot { I } ^ { \langle p r \rangle } \ddot { I } ^ { \langle q r \rangle } ;
$$

this involves the mass quadrupole moment only, and here also contributions from higherorder moments would appear at order $G / c ^ { 7 }$ and higher.

To obtain Eq. (12.68a) for $\mathcal { P }$ we truncate Eq. (12.67) to its leading-order term, carry out the TT projection of Eq. (12.64), and insert the result within Eq. (12.42). After simplification we obtain

$$
\mathcal { P } = \frac { G } { 2 c ^ { 5 } } \Big ( \delta _ { p r } \delta _ { q s } - 2 \delta _ { p r } \big \{ \big \langle N _ { q } N _ { s } \big \rangle \big \} + \frac { 1 } { 2 } \big \langle \big \langle N _ { p } N _ { q } N _ { r } N _ { s } \big \rangle \big \rangle \Big ) f ^ { p q } f ^ { r s } ,
$$

with $f ^ { j k } : = \overleftarrow { I } ^ { \langle j k \rangle }$ and $\langle \langle \cdot \cdot \cdot \rangle \rangle : = ( 4 \pi ) ^ { - 1 } \int ( \cdot \cdot \cdot ) d \Omega$ indicating an angular average. These are easily evaluated with the help of the identities

$$
\begin{array} { c } { { \displaystyle \left. \left. N _ { j } N _ { k } \right. \right. = \displaystyle \frac { 1 } { 3 } \delta _ { j k } , } } \\ { { \displaystyle \left. \left. N _ { j } N _ { k } N _ { p } N _ { q } \right. \right. = \displaystyle \frac { 1 } { 1 5 } \big ( \delta _ { j k } \delta _ { p q } + \delta _ { j p } \delta _ { k q } + \delta _ { j q } \delta _ { k p } \big ) , } } \\ { { \displaystyle \left. \left. N _ { j } N _ { k } N _ { p } N _ { q } N _ { r } N _ { s } \right. \right. = \displaystyle \frac { 1 } { 1 0 5 } \big ( \delta _ { j k } \delta _ { p q } \delta _ { r s } + \mathrm { d i s t i n c t ~ p e r m u t a t i o n s } \big ) , } } \end{array}
$$

which were established back in Sec. 1.5.3. Making use of the STF properties of $f ^ { j k }$ , we arrive at Eq. (12.68a).

To obtain Eq. (12.68b) from Eq. (12.43) we must include the subleading terms in Eq. (12.67), because a leading-order calculation involves angular integrations of odd products of the radial vector $N$ , which all vanish. After the TT projection we obtain

$$
{ \mathcal { F } } ^ { j } = { \frac { G } { 3 c ^ { 7 } } } \Big ( \delta _ { p r } \delta _ { q s } \big \{ \big ( N ^ { j } N _ { n } \big ) \big \} - 2 \delta _ { p r } \big \{ \big ( N ^ { j } N _ { q } N _ { s } N _ { n } \big ) \big \} + { \frac { 1 } { 2 } } \big \langle \big \langle N ^ { j } N _ { p } N _ { q } N _ { r } N _ { s } N _ { n } \big \rangle \big \} \Big ) f ^ { p q } f ^ { r s n } ,
$$

with $f ^ { j k } : = \overleftarrow { I } ^ { \because \langle j k \rangle }$ and $f ^ { j k n } : = \ddot { I } ^ { \cdots ( j k n ) } + 2 \epsilon ^ { m n j } \ddot { J } ^ { \langle m k \rangle } + 2 \epsilon ^ { m n k } \ddot { J } ^ { \langle m j \rangle } \nonumber$ . After evaluation of the angular integrals and simplification (taking advantage of the STF properties of $f ^ { j k }$ and $f ^ { j k n } )$ , we obtain

$$
\mathcal { F } ^ { j } = \frac { G } { 3 c ^ { 7 } } \bigg ( \frac { 2 2 } { 1 0 5 } f _ { p q } f ^ { p q j } - \frac { 4 } { 3 5 } f _ { p q } f ^ { j p q } \bigg ) ,
$$

which leads directly to Eq. (12.68b).

The computations that lead to Eq. (12.68c) from Eq. (12.47) are similar. Here also we truncate Eq. (12.67) to its leading-order term, and the gravitational-wave field must be differentiated only after the TT projection has been accomplished. (This step is facilitated by invoking the identity $R \partial _ { j } P _ { p q } = - P _ { j p } N _ { q } - P _ { j q } N _ { p } .$ ) The remaining manipulations are straightforward, and we arrive at Eq. (12.68c).

# 12.3.3 Application: Newtonian binary system

As an application of the formalism developed in this section, we calculate the gravitationalwave fluxes P, $\mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ for a binary system consisting of a body of mass $m _ { 1 }$ at position $r _ { 1 } ( t )$ and a body of mass $m _ { 2 }$ at position $r _ { 2 } ( t )$ ; the positions are given in relation to the system’s barycenter, chosen to be at the origin of the spatial coordinates. We describe the mutual gravitational attraction at the leading-order, Newtonian level, and we employ the formulae listed in Eqs. (12.68) and (12.69) to calculate the fluxes. The Keplerian orbital motion was first examined back in Sec. 3.2, and considered again in the context of gravitational-wave emissions in Sec. 11.2.2; the required equations can be found at the beginning of Sec. 11.2.2. The main orbital parameters are the semilatus rectum $p$ and the eccentricity $e$ . The orbital period is

$$
P = 2 \pi \sqrt { \frac { a ^ { 3 } } { G m } } ,
$$

where $a : = { p } / { ( 1 - e ^ { 2 } ) }$ is the semi-major axis and $m : = m _ { 1 } + m _ { 2 }$ . The orbital energy and angular momentum are

$$
E = - \frac { \eta G m ^ { 2 } } { 2 a } , \qquad L = \eta m h e _ { z } ,
$$

where $\eta : = m _ { 1 } m _ { 2 } / m ^ { 2 }$ , $h : = | { \boldsymbol { r } } \times { \boldsymbol { v } } | = { \sqrt { G m p } }$ with $r : = r _ { 1 } - r _ { 2 }$ and $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , and $\pmb { e } _ { z } : = [ 0 , 0 , 1 ]$ is a unit vector normal to the orbital plane. It is useful to note that the equations of motion imply that $v { \dot { v } } = - G m { \dot { r } } / r ^ { 2 }$ and $r \ddot { r } = ( r \dot { \phi } ) ^ { 2 } - G m / r$ , in which $r : = | r | , v : = | \pmb { v } |$ , $\dot { \phi } = h / r ^ { 2 }$ , and an overdot indicates differentiation with respect to time.

The multipole moments that appear in the flux formulae are

$$
\begin{array} { r c l } { { } } & { { } } & { { I ^ { j k } = \eta m r ^ { j } r ^ { k } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { I ^ { j k n } = - \Delta \eta m r ^ { j } r ^ { k } r ^ { n } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { J ^ { j k } = - \Delta \eta m h e _ { z } ^ { j } r ^ { k } , } } \end{array}
$$

where $\Delta : = ( m _ { 1 } - m _ { 2 } ) / m$ . These expressions follow directly from the definitions of Eqs. (12.61), (12.62), and (12.63) when the mass density is given by $\rho ^ { * } = m _ { 1 } \delta ( { \pmb x } - { \pmb r } _ { 1 } ) +$ $m _ { 2 } \delta ( { \pmb x } - { \pmb r } _ { 2 } )$ and the individual positions are expressed in terms of the separation $r$ . The result for $J ^ { j k }$ takes into account the fact that $h \pmb { e } _ { z } = \pmb { r } \times \pmb { v }$ .

Differentiation of the multipole moments and involvement of the Keplerian equations yields

$$
\begin{array} { r l } & { \tilde { j } ^ { ( k ) } = 2 \eta m \left( \nu ^ { j } \nu ^ { k } - \frac { G m } { F ^ { 3 } } , j \nu ^ { k } \right) } \\ & { \quad = 2 \eta m \left( \nu ^ { 2 } - G m / r \right) n ^ { j } \hbar ^ { k } + i \tilde { r } ( \tilde { v } ) \tilde { \sigma } ( n ^ { j } \hbar ^ { k } + \lambda ^ { j } n ^ { k } ) + ( \tilde { v } \tilde { \phi } ) ^ { 2 } \hbar ^ { k } \tilde { \mathcal { H } } \right] } \\ & { \quad = 2 \eta m \frac { G m } { F ^ { 3 } } \left[ - ( 1 + c \cos \phi - e ^ { - 2 } \sin ^ { 2 } \phi ) n ^ { j } n ^ { k } \right. } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad + \left. \epsilon \sin \phi ( 1 + ( \cos \phi ) ( n ^ { j } \hbar ^ { k } + \lambda ^ { j } n ^ { k } ) + ( 1 + e \cos \phi ) ^ { 2 } ) \lambda ^ { j } \hbar ^ { k } \right] , \quad 0 } \\ & { \quad \quad \quad \quad \tilde { j } ^ { ( k ) } = - 2 \eta m \frac { G m } { F ^ { 3 } } \left[ \frac { 2 } { \pi } ( r ^ { j } \nu ^ { k } + \nu ^ { j } \cdot \frac { \lambda ^ { j } } { r ^ { 2 } } - r ^ { k } \epsilon ^ { j } \frac { \lambda } { r ^ { 2 } } ) \right. } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \left. = - 2 \eta m \frac { G m } { F ^ { 3 } } \left[ \tilde { r } ^ { j } n ^ { k } + 2 ( r \phi ) ( \mu ^ { j } \lambda ^ { k } + \lambda ^ { j } n ^ { k } ) \right] } \\ & { \quad \quad \quad \quad \quad - 2 \eta m \frac { G ( m ) ^ { 3 / 2 } } { F ^ { 3 } } ( 1 + e \cos \phi ) ^ { 2 } \left[ e \sin \phi n ^ { j } \hbar ^ { k } + 2 ( 1 + e \cos \phi ) ( n ^ { j } \lambda ^ { k } + \lambda ^ { j } n ^ { k } ) \right] . } \end{array}
$$

$$
\begin{array} { r l } &  \begin{array} { r l } & { = \Delta t \rho \frac { G m } { r ^ { 2 } } \left[ \frac { 2 0 } { r } \left( r ^ { 3 } \dot { r } ^ { 5 } r ^ { 6 } + \kappa ^ { 7 } \dot { r } ^ { 5 } \kappa ^ { 8 } + r ^ { 7 } \dot { r } ^ { 6 } \kappa ^ { 8 } \right) \right. } \\ & { \qquad \left. - \frac { 3 0 \dot { \nu } } { r ^ { 2 } } \left( \nu ^ { 5 } \dot { r } ^ { 6 } \kappa ^ { 5 } + r ^ { 7 } \dot { r } ^ { 6 } \kappa ^ { 5 } + r ^ { 7 } \dot { r } ^ { 6 } \kappa ^ { 6 } \right) - \frac { 3 } { r ^ { 3 } } \left( 3 \nu ^ { 2 } - 1 5 \dot { r } ^ { 2 } + 4 G m / r \right) r ^ { 7 } \dot { r } ^ { 5 } \kappa ^ { 8 } \right] } \\ & { = \Delta t \rho \frac { G m } { r ^ { 2 } } \left[ 3 \left[ 2 r ^ { 2 } - 3 ( \dot { r } \dot { \nu } \dot { \nu } ) ^ { 2 } - 4 G m / r \right] \dot { r } ^ { 7 } \dot { r } ^ { 6 } \kappa ^ { } \right. } \\ & { \qquad \left. + 1 0 ( \dot { r } \dot { r } \dot { \nu } ) ^ { 3 } ( n ^ { 5 } \dot { r } ^ { 6 } \kappa ^ { 5 } + n ^ { 7 } \dot { r } ^ { 6 } n ^ { 4 } + \lambda ^ { 2 } \dot { r } ^ { 6 } \dot { r } ^ { 6 } n ^ { 5 } ) \right. } \\ & { \qquad \left. + 2 0 ( \dot { r } \dot { \nu } \dot { \nu } ) ^ { 2 } ( n ^ { 5 } \dot { r } ^ { 5 } \kappa ^ { 6 } + \kappa ^ { 7 } \dot { r } ^ { 6 } n ^ { 6 } + \lambda ^ { 2 } \dot { r } ^ { 6 } \dot { r } ^ { 8 } n ^ { 7 } ) \right. } \\ & { \qquad \left. + 2 0 ( \dot { r } \dot { \nu } ) ^ { 2 } ( n ^ { 7 } \dot { r } ^ { 6 } \kappa ^ { 5 } + \lambda ^ { 2 } \dot { r } ^ { 6 } \kappa ^ { 7 } ) \right. } \\ &  = \Delta t \rho \frac { G m ^ { 2 } } { r ^ { 3 } } ( 1 + \epsilon \cos \phi ) ^ { 2 } \left[ - 3 ( 7 + 1 0 \dot { \nu } \cos \phi + 5 \epsilon ^ { 2 } \cos ^ { 2 } \phi ) ^ { 2 } \right. \dot { r } ^ { 6 } \end{array} \end{array}
$$

$$
\begin{array} { l } { { \displaystyle { \ddot { J } } ^ { j k } = \Delta \eta m h \frac { G m } { r ^ { 3 } } e _ { z } ^ { j } \left( v ^ { k } - \frac { 3 \dot { r } } { r } r ^ { k } \right) } } \\ { { \displaystyle \quad = - \Delta \eta m h \frac { G m } { r ^ { 3 } } e _ { z } ^ { j } \big [ 2 \dot { r } n ^ { k } - ( r \dot { \phi } ) \lambda ^ { k } \big ] } } \\ { { \displaystyle \quad = - \Delta \eta m \frac { ( G m ) ^ { 2 } } { p ^ { 3 } } ( 1 + e \cos \phi ) ^ { 3 } e _ { z } ^ { j } \big [ 2 e \sin \phi n ^ { k } - ( 1 + e \cos \phi ) \lambda ^ { k } \big ] } , } \end{array}
$$

where $\pmb { n } = [ \cos \phi , \sin \phi , 0 ]$ and $\lambda = [ - \sin \phi$ , $\cos \phi , 0 ]$ are basis vectors in the orbital plane. After symmetrizing $\ddot { \boldsymbol { J } } ^ { j k }$ , making all the moments tracefree, and inserting the results within the flux formulae of Eqs. (12.68) and (12.69), we obtain

$$
\begin{array} { l } { { \displaystyle { \mathbb { P } } = \frac { 3 2 } { 5 } \eta ^ { 2 } \displaystyle \frac { c ^ { 5 } } { G } \bigg ( \displaystyle \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 5 } ( 1 + e \cos \phi ) ^ { 4 } \bigg [ 1 + 2 e \cos \phi + \displaystyle \frac { 1 } { 1 2 } e ^ { 2 } ( 1 + 1 1 \cos ^ { 2 } \phi ) \bigg ] , ~ } } \\ { { \displaystyle \mathcal { F } ^ { x } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \displaystyle \frac { c ^ { 4 } } { G } \bigg ( \displaystyle \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 1 1 / 2 } \sin \phi ( 1 + e \cos \phi ) ^ { 4 } } } \\ { { \displaystyle ~ \times ~ \bigg [ 1 + \displaystyle \frac { 1 7 5 } { 5 8 } e \cos \phi + \displaystyle \frac { 2 } { 2 9 } e ^ { 2 } ( 3 + 4 0 \cos ^ { 2 } \phi ) + \displaystyle \frac { 5 } { 5 8 } e ^ { 3 } \cos \phi ( 2 + 9 \cos ^ { 2 } \phi ) \bigg ] , } } \end{array}
$$

$$
\begin{array} { c } { \displaystyle { \mathcal { F } ^ { y } = - \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \frac { c ^ { 4 } } { G } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 1 1 / 2 } ( 1 + e \cos \phi ) ^ { 4 } \bigg [ \cos \phi - \frac { 1 } { 5 8 } e ( 9 - 1 7 5 \cos ^ { 2 } \phi ) } } \\ { \displaystyle { - \frac { 1 } { 2 9 } e ^ { 2 } \cos \phi ( 1 - 8 0 \cos ^ { 2 } \phi ) + \frac { 1 } { 5 8 } e ^ { 3 } ( 2 + 3 \cos ^ { 2 } \phi + 4 5 \cos ^ { 4 } \phi ) \bigg ] , } } \\ { \displaystyle { \mathcal { T } ^ { x y } = \frac { 3 2 } { 5 } \eta ^ { 2 } m c ^ { 2 } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 7 / 2 } ( 1 + e \cos \phi ) ^ { 3 } \bigg [ 1 + \frac { 3 } { 2 } e \cos \phi - \frac { 1 } { 4 } e ^ { 2 } ( 1 - 3 \cos ^ { 2 } \phi ) \bigg ] , } } \end{array}
$$

![](images/89ab1b90d7c3a65455921f0da8926cd0bd6bf7ceda836f80ab8deb95602fe238.jpg)  
The energy flux ${ \mathcal { P } } _ { \iota }$ in units of $( 3 2 / 5 ) \eta ^ { 2 } ( c ^ { 5 } / 6 ) ( G m / c ^ { 2 } p ) ^ { 5 }$ , as a function of retarded time $\tau$ , in units of the orbital period $P .$ The relation between $\tau$ and the orbital phase $\phi$ is obtained by numerical integration of the Newtonian equations of motion. The orbital eccentricity is set equal to $e = 0 . 7$ , and the gravitational-wave polarizations corresponding to this orbital configuration are displayed in Fig. 11.2. We see that most of the energy is emitted when the orbit is near pericenter, where the motion is fastest.

while $\mathcal { F } ^ { z } = 0$ and $\mathcal { T } ^ { y z } = \mathcal { T } ^ { z x } = 0$ . Plots of $\mathcal { P } , \mathcal { F } ^ { x }$ , and $\mathcal { F } ^ { \nu }$ as functions of time are presented in Figs. 12.1 and 12.2; a plot of $\mathcal { T } ^ { x y }$ would look very similar to $\mathcal { P }$ .

When the orbit is circular (so that $e = 0$ ) the fluxes simplify to

$$
\begin{array} { l } { { \displaystyle { \mathcal { P } } = \frac { 3 2 } { 5 } \eta ^ { 2 } \frac { c ^ { 5 } } { G } ( v / c ) ^ { 1 0 } , } } \\ { { \displaystyle \mathcal { F } ^ { x } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \frac { c ^ { 4 } } { G } ( v / c ) ^ { 1 1 } \sin \phi , } } \\ { { \displaystyle \mathcal { F } ^ { y } = - \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \frac { c ^ { 4 } } { G } ( v / c ) ^ { 1 1 } \cos \phi , } } \\ { { \displaystyle \mathcal { T } ^ { x y } = \frac { 3 2 } { 5 } \eta ^ { 2 } m c ^ { 2 } ( v / c ) ^ { 7 } , } } \end{array}
$$

where $v : = { \sqrt { G m / p } }$ is the orbital velocity. In this case the orbital phase is given by $\phi = \Omega \tau$ , with $\Omega : = \sqrt { G m / p ^ { 3 } }$ denoting the orbital angular velocity. We note that in this case of circular motion, the energy and angular-momentum fluxes are related by $\mathcal { P } = \Omega \mathcal { T } ^ { x y }$ . We also see that the momentum flux is aligned with $\pmb { v }$ when $m _ { 1 } < m _ { 2 }$ (so that $\Delta < 0$ ), and that it is anti-aligned when $m _ { 1 } > m _ { 2 }$ ; the momentum flux is therefore always in the direction of motion of the lighter body.

![](images/a54c9967a64d405f329139df6f932e144a38d497a34d2608d83f9add878df5b9.jpg)

# Fig. 12.2

The momentum fluxes $\mathcal { F } ^ { \boldsymbol { x } }$ and ${ \mathcal { F } } ^ { y } ,$ in units of $- \Delta \eta ^ { 2 } ( c ^ { 4 } / G ) ( G m / c ^ { 2 } p ) ^ { 1 1 / 2 }$ , as functions of retarded time $\tau$ , in units of the orbital period $P . \mathtt { A }$ minus sign is inserted in the unit of momentum flux to reflect the fact that $\Delta < 0$ when $m _ { 1 } < m _ { 2 }$ . As in Fig. 12.1 the orbital eccentricity is set equal to $e = 0 . 7 .$ . We see that most of the momentum is emitted when the orbit is near pericenter. The emission in the $\chi .$ -direction cancels out over a complete orbital cycle, but the emission in the $y -$ -direction builds up coherently.

<table><tr><td>Box 12.2</td><td>Momentum flux and gravitational-wave beaming</td></tr><tr><td></td><td>Our friend Alan Wiseman has proposed a useful electromagnetic analogy to understand why the momentum flux is always in the direction of motion of the lighter body. Because the lighter body has a higher velocity, the energy flux asociated with its motion is beamed in the forward direction, just as the electromagnetic radiation from a rapidly moving body is beamed by relativistic effects.Since energy carres momentum, there is a preferential emission of momentum in the direction ofmotion of the lighter body.This is admittedly an imperfectanalogy,because theenergy flux is predominantly quadrupolar, not dipolar,andthus itcannot have a unique direction associated with it.On the other hand,the momentum flux arises from an interference be- tween the quadrupole moment Ijk and the O.5PN corrections in Eq.(12.67), which depend on the octupole and current quadrupole moments; although the latter are not vectors, they have an odd parity,and they can therefore single out a preferred direction.Scaling the energy flux by mc2,the momentum flux by mc,and taking the ratio gives (Fj /mc)/(P/mc²) ~ v/c, precisely the kind of v/c efect that gives rise to relativistic beaming.</td></tr></table>

Returning to non-circular orbits, it is instructive to average the fluxes over a complete orbital cycle. We define the orbital average of a quantity $f$ by

$$
\left. f \right. : = \frac { 1 } { P } \int _ { 0 } ^ { P } f ( t ) d t ,
$$

where $P$ is the orbital period of Eq. (12.74). This can also be expressed as

$$
\langle f \rangle = ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } ( 1 + e \cos \phi ) ^ { - 2 } f ( \phi ) d \phi
$$

by switching integration variables from $t$ to $\phi$ with the help of the Keplerian equations of motion. Substitution of Eqs. (12.78) into Eq. (12.81) yields

$$
\begin{array} { l } { \displaystyle \langle \mathfrak { P } \rangle = \frac { 3 2 } { 5 } \eta ^ { 2 } \frac { c ^ { 5 } } { G } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 5 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } \bigg ) , } \\ { \displaystyle \langle \mathfrak { F } ^ { x } \rangle = 0 , } \\ { \displaystyle \langle \mathfrak { F } ^ { y } \rangle = - \frac { 5 2 } { 5 } \Delta \eta ^ { 2 } \frac { c ^ { 4 } } { G } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 1 1 / 2 } e ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 1 9 } { 1 3 } e ^ { 2 } + \frac { 3 7 } { 3 1 2 } e ^ { 4 } \bigg ) , } \\ { \displaystyle \langle \mathfrak { T } ^ { x y } \rangle = \frac { 3 2 } { 5 } \eta ^ { 2 } m c ^ { 2 } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 7 / 2 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 7 } { 8 } e ^ { 2 } \bigg ) . } \end{array}
$$

That $\langle \mathcal { F } ^ { x } \rangle = 0$ and $\langle \mathcal { F } ^ { y } \rangle \neq 0$ reflects the fact that while the orbital motion is reflectionsymmetric across the $x$ -axis, it is asymmetrical with respect to the $y$ -axis: the motion is faster when the orbit crosses the $x$ -axis is at pericenter, and slower when it crosses it at apocenter, moving in the opposite direction. Most of the gravitational waves are emitted near pericenter, where the motion is fastest, and most of the momentum flux is therefore generated near $\phi = 0$ . When $\Delta < 0$ , that is, when $m _ { 1 } < m _ { 2 }$ , we have that $\mathcal { F } ^ { y } > 0$ at pericenter, and the averaged flux also is positive; this is the situation represented in Fig. 12.2. On the other hand, when $\Delta > 0$ and $m _ { 1 } > m _ { 2 }$ , we have that $\mathcal { F } ^ { y } < 0$ at pericenter, and the averaged flux also is negative. The momentum flux vanishes when the masses are equal, and the averaged flux vanishes when $e = 0$ .

Bodies in unbound orbits, with $e \geq 1$ , also radiate energy, momentum, and angular momentum. In this case there is no orbital period and no useful notion of averaged fluxes, but one can calculate the total energy, momentum, and angular momentum radiated during the encounter. These losses raise the interesting possibility of a “gravitational-wave capture,” whereby two bodies in an unbound orbit lose enough energy to end up in a bound orbit. This possibility is explored in Exercise 12.8.

It is tempting to exploit the balance equations in averaged form,

$$
\frac { d E } { d t } = - \langle \mathcal { P } \rangle , \qquad \frac { d L } { d t } = - \langle \mathcal { T } ^ { x y } \rangle ,
$$

to infer the rates at which the orbital elements $a , \ p$ , and $e$ must change in order to reflect the loss of energy and angular momentum to gravitational waves. This crude and tentative analysis is refined in Sec. 12.9, where we calculate how the orbital elements change instantaneously as a result of the action of the gravitational radiation-reaction force.

The rate of change of $a$ is obtained by inserting Eq. (12.75) into the first balance equation. With Eq. (12.82) we obtain

$$
\frac { d a } { d t } = - \frac { 6 4 } { 5 } \eta c \biggl ( \frac { G m } { c ^ { 2 } a } \biggr ) ^ { 3 } \frac { 1 + \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } } { ( 1 - e ^ { 2 } ) ^ { 7 / 2 } } .
$$

Kepler’s third law, $P \propto a ^ { 3 / 2 }$ , allows us to compute how the orbital period changes as a result of the orbital evolution; we find that it decreases according to

$$
\frac { d P } { d t } = - \frac { 1 9 2 \pi } { 5 } \bigg ( \frac { G \mathcal { M } } { c ^ { 3 } } \frac { 2 \pi } { P } \bigg ) ^ { 5 / 3 } \frac { 1 + \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } } { ( 1 - e ^ { 2 } ) ^ { 7 / 2 } } ,
$$

where $\mathcal { M } : = \eta ^ { 3 / 5 } m$ is the chirp mass, as defined in Eq. (11.80). The rate of change of $p$ is obtained by inserting Eq. (12.75) into the second balance equation. Here we obtain

$$
\frac { d p } { d t } = - \frac { 6 4 } { 5 } \eta c \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 7 } { 8 } e ^ { 2 } \bigg ) .
$$

The rate of change of $e$ can then be inferred from the relation $p / a = 1 - e ^ { 2 }$ ; we get

$$
\begin{array} { l } { \displaystyle { \frac { d e } { d t } = - \frac { 3 0 4 } { 1 5 } \eta c \frac { e } { a } \bigg ( \frac { G m } { c ^ { 2 } a } \bigg ) ^ { 3 } \frac { 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } } } \\ { \displaystyle { = - \frac { 3 0 4 } { 1 5 } \eta c \frac { e } { p } \bigg ( \frac { G m } { c ^ { 2 } p } \bigg ) ^ { 3 } ( 1 - e ^ { 2 } ) ^ { 3 / 2 } \bigg ( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \bigg ) . } } \end{array}
$$

We see that radiative losses tend to decrease both the size of the orbit and its eccentricity; in the course of time the orbit shrinks and becomes increasingly circular. The orbital evolution proceeds on a radiation-reaction time scale of the order of

$$
T _ { \mathrm { r r } } = \frac { 1 } { \eta } \bigg ( \frac { G m } { c ^ { 2 } a } \bigg ) ^ { - 5 / 2 } \frac { P } { 2 \pi } ;
$$

this is longer than the orbital period by a factor of order $( v _ { c } / c ) ^ { - 5 } \gg 1$ , where $v _ { c } \sim \sqrt { G m / a }$ is the characteristic orbital velocity.

The evolution equations for $a , p$ , and $e$ can be integrated to give

$$
a = a _ { 0 } ( e / e _ { 0 } ) ^ { 1 2 / 1 9 } \bigg ( \frac { 1 - e _ { 0 } ^ { 2 } } { 1 - e ^ { 2 } } \bigg ) \bigg ( \frac { 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } } { 1 + \frac { 1 2 1 } { 3 0 4 } e _ { 0 } ^ { 2 } } \bigg ) ^ { 8 7 0 / 2 2 9 9 }
$$

and

$$
p = p _ { 0 } ( e / e _ { 0 } ) ^ { 1 2 / 1 9 } \bigg ( \frac { 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } } { 1 + \frac { 1 2 1 } { 3 0 4 } e _ { 0 } ^ { 2 } } \bigg ) ^ { 8 7 0 / 2 2 9 9 } ,
$$

which express $a$ and $p$ as functions of the eccentricity; here $a _ { 0 }$ and $p _ { 0 }$ are respectively the values of $a$ and $p$ when $e = e _ { 0 }$ . When the eccentricity is always small, so that both $e$ and $e _ { 0 }$ are much smaller than unity, these results can be approximated as $a \simeq a _ { 0 } ( e / e _ { 0 } ) ^ { 1 2 / 1 9 }$ or $e \simeq e _ { 0 } ( a / a _ { 0 } ) ^ { 1 9 / 1 2 }$ ; in this approximation $p \simeq a$ .

# 12.4 Astrophysical implications of radiative losses

# 12.4.1 Binary pulsars

For many years, any discussion of losses due to gravitational-wave emissions, such as the one presented in the previous section, was purely academic, because the effects are so

Table 12.1 Orbital parameters of binary pulsars. The parameter a1 sin ι is the projection of the pulsar’s   
semimajor axis along the line of sight. The parameter ˙ω is defined by Eq. (10.17). The parameter γ  is the coefficient [(M1 + 2M2)/m](a3 / Gm)1/2 (GM2/c2 a)e that appears in front of sin u in Eq. (10.135). The   
period derivative P˙ is given by Eq. (12.85). The parameter r is the coefficient GM2/c2 that appears in front of the logarithmic term in Eq. (10.139), and s = sin ι appears within the logarithm. The numbers in parentheses indicate the error in the last digit.

<table><tr><td>Parameter</td><td>PSR 1913+16</td><td>J0737-3039A</td></tr><tr><td>Keplerian parameters</td><td></td><td></td></tr><tr><td>a sint/c (s)</td><td>2.341782(3)</td><td>1.415032(1)</td></tr><tr><td>Eccentricity, e</td><td>0.6171334(5)</td><td>0.0877775(9)</td></tr><tr><td>Orbital period, P (day)</td><td>0.322997448911(4)</td><td>0.10225156248(5)</td></tr><tr><td>Relativistic parameters</td><td></td><td></td></tr><tr><td>Pericenter advance, 𝜔(° yr-1)</td><td>4.226598(5)</td><td>16.8995(7)</td></tr><tr><td>Redshift/time dilation, y&#x27; (ms)</td><td>4.2992(8)</td><td>0.386(3)</td></tr><tr><td>Period derivative, P (10-12)</td><td>-2.423(1)</td><td>-1.25(2)</td></tr><tr><td>Shapiro delay, r (μs)</td><td></td><td>6.2(3)</td></tr><tr><td>Shapiro delay, s</td><td></td><td>0.9997(4)</td></tr></table>

extremely small. The effects of radiative losses on the Earth–Sun or Earth–Moon orbits, for example, are utterly undetectable, as you will discover in Exercise 12.4. The complete absence of experimental evidence bearing on radiative losses was a key ingredient in the persistence of the quadrupole-formula controversy, as reviewed in Box 11.2. All this changed in the fall of 1974.

During the summer of 1974, radio astronomer Joseph H. Taylor and his graduate student Russell Hulse were conducting a systematic search for new pulsars using the Arecibo radio telescope in Puerto Rico. Pulsars are rotating neutron stars that emit a beam of radio waves detectable as a pulse every time the beam crosses a radio receiver. Since the discovery of the first pulsar in 1967, almost 100 had been found by 1974 (nearly 2000 are known today). But this new pulsar, labeled PSR $1 9 1 3 + 1 6$ according to its position on the sky, was different from all the others because its pulse period, nominally about 59 milliseconds, varied by plus or minus 40 microseconds on a roughly eight-hour period. Hulse and Taylor quickly concluded that the variation was a result of the Doppler shift of the period caused by the pulsar’s orbit about an unseen companion. By December they had measured the key orbital elements, the orbital period, the eccentricity, the semi-major axis projected along the line of sight, as well as the relativistic pericenter advance (the current values are listed in Table 12.1).

It was already clear from the first discovery announcement in late September that the binary pulsar would provide an opportunity to test the quadrupole formula. Inserting the measured period $P$ and eccentricity $e$ into Eq. (12.85), and scaling the chirp mass by the solar mass, we find that the orbital period should decrease at a rate of $5 3 . 2 ( { \mathcal { M } } / M _ { \odot } ) ^ { 5 / 3 }$ microseconds per year. Out of an orbital period of almost eight hours, this is a dauntingly small effect, but one that could nevertheless be measured. This required a change of data-analysis strategy, from measuring pulse periods to measuring pulse arrival times (as described in Sec. 10.3.6), and improvements of the instrumentation at the Arecibo telescope, to better handle the effects of interstellar dispersion on the radio signals. After collecting data for a few short years, Taylor and colleagues were able to report the first measurement of the period decrease in December 1979.

The measurement of $d P / d t$ can only be compared with the relativistic prediction when the chirp mass $\mathcal { M }$ is known. Fortunately, the measured pericenter advance of 4.2 degrees per year gives the total mass – refer to Eq. (10.17) – and the arrival-time analysis also yields the combination of masses $( M _ { 1 } + 2 M _ { 2 } ) M _ { 2 }$ via the periodic term in Eq. (10.135). These data produced precise values for the pulsar and companion masses, $( 1 . 4 3 9 8 \pm 0 . 0 0 0 2 ) M _ { \odot }$ and $( 1 . 3 8 8 6 \pm 0 . 0 0 0 2 ) M _ { \odot }$ respectively, and thus a precise prediction of $d P / d t = - ( 2 . 4 0 2 5 3 1 \pm 0 . 0 0 0 0 1 4 ) \times 1 0 ^ { - 1 2 }$ , in beautiful agreement with the measurement.

While the value of $d P / d t$ reported by Taylor in 1979 had measurement errors of 10 percent, the errors have steadily decreased over time, and they are now at the level of about 0.05 percent. At this level of precision it is necessary to take into account the relative acceleration between the binary pulsar and the solar system caused by the differential rotation of the galaxy. This causes all observed periods in the binary-pulsar system to vary slowly with time. The best estimates of the galactic effect yield a small correction $( d P / d t ) _ { \mathrm { g a l } } = - ( 0 . 0 2 7 \pm 0 . 0 0 5 ) \times 1 0 ^ { - 1 2 }$ , so that the agreement between the observed radiative loss and the prediction of the quadrupole formula can be expressed as

$$
\frac { ( d P / d t ) _ { \mathrm { o b s } } } { ( d P / d t ) _ { \mathrm { G R } } } = 0 . 9 9 7 \pm 0 . 0 0 2 .
$$

This has been widely hailed as definitive, albeit indirect, evidence for the existence of gravitational radiation, and Taylor and Hulse were rewarded for this discovery with the 1993 Nobel Prize in Physics.

Interestingly, while continued observation of the system will provide more precise measurements of $d P / d t$ (the statistical errors on such drifting parameters tend to decrease as $T ^ { - 3 / 2 }$ , where $T$ is the observation time), they will not produce an improved test of the quadrupole formula. This is because the measurement of $d P / d t$ is now limited by our poor understanding of the galaxy’s differential rotation, and the uncertainties associated with it are unlikely to ever be reduced. In fact, the tables can be turned: the assumed validity of the quadrupole formula combined with the observed $d P / d t$ provides a better measure of the relative acceleration than is likely to be obtained by standard astronomical techniques.

Many other binary pulsars have been found since Hulse and Taylor’s discovery, almost 100 to date and counting. One of the most remarkable is the “double pulsar” J0737-3039A&B, discovered in 2003. Whereas a single active pulsar was detected in the Hulse–Taylor system (the companion is believed to be a very old, essentially “dead” pulsar), here both objects, denoted $A$ and $B$ , were detected as pulsars. The orbit is very relativistic, with an orbital period of only a tenth of a day, and a pericenter advance of almost 17 degrees per year (see Table 12.1). The orbit is observed almost edge on, so that in addition to the three relativistic effects measured in the Hulse–Taylor binary pulsar (pericenter advance, redshift-time dilation effect, and period decrease), it is also possible to measure the Shapiro time delay of the signal from the stronger pulsar as it passes by the companion once per orbit. This delivers a precise determination of the masses – $M _ { A } = ( 1 . 3 3 8 1 \pm 0 . 0 0 0 7 ) M _ { \odot }$ and $M _ { B } = ( 1 . 2 4 8 9 \pm 0 . 0 0 0 7 ) M _ { \odot } -$ and the period derivative has already been measured to two-percent accuracy. Ultimately this system will yield a more precise test of the quadrupole formula than did PSR $1 9 1 3 + 1 6$ , partly because the main pulsar has a narrower pulse profile, leading to a more precise timing of the pulse arrivals, but mainly because the system is closer to the Earth and in a favorable location within the galaxy, so that the galactic acceleration is essentially negligible (the acceleration is predominantly transverse to the line of sight). Another remarkable feature of the double pulsar is that it is no longer double: since its discovery the spin axis of the secondary pulsar has shifted in direction, thanks to the relativistic geodetic precession reviewed in Sec. 10.4.3, and as a consequence the pulsar beam is no longer intersecting the Earth. This is another example of a post-Newtonian effect with practical consequences, at least for the radio astronomers who keep observing the double pulsar.

# 12.4.2 Inspiralling compact binaries

In due course, radiative losses bring the two neutron stars of a binary-pulsar system into such close proximity that their orbital periods are measured in fractions of a second rather than hours. At this stage the gravitational waves emitted by the binary system enter the frequency band of a ground-based laser interferometric detector such as LIGO and Virgo, namely the band which lies between approximately $1 0 \mathrm { H z }$ and $1 0 0 0 \mathrm { H z }$ . It is totally pointless to wait around for this to happen, however, because the required time is extremely long. In the limit of small eccentricities, it is straightforward to estimate the inspiral time by integrating Eq. (12.84) from $a$ ’s present value to a final value of effectively zero. The present value and the total mass $m$ can be conveniently expressed in terms of the orbital period $P$ and the observed rate of pericenter advance $\dot { \omega }$ . For the special case of almost equal masses $\eta = 1 / 4$ , this calculation yields

$$
T = \frac { 5 } { 1 2 8 } \left( \frac { 6 \pi } { \dot { \omega } } \right) ^ { 5 / 2 } \left( \frac { 1 } { P } \right) ^ { 3 / 2 } \approx 1 . 9 \times 1 0 ^ { 8 } \left( \frac { 5 ^ { \circ } / \mathrm { y r } } { \dot { \omega } } \right) ^ { 5 / 2 } \left( \frac { 1 \mathrm { d a y } } { P } \right) ^ { 3 / 2 } \mathrm { y r } ,
$$

and we see that for a typical binary pulsar, the inspiral time is of the order of 200 million years. A more eccentric orbit starting with the same $a$ would give rise to a shorter time scale, because of the excess radiative loss induced by the rapidly changing velocities near pericenter (refer to Fig. 12.1).

The important point about this time scale, long as it may seem, is that it is still short compared to the age of typical galaxies like the Milky Way. There is therefore a chance that a binary pulsar born 200 million years ago in a nearby galaxy would be in its final death spiral today, emitting a detectable burst of gravitational waves. Such systems, called “inspiralling compact binaries” (they could also involve black holes), are a highly anticipated source of gravitational waves for detection by the LIGO–Virgo class of interferometers. Based on the small number of relativistic binary pulsars that have been observed to date, it is possible to estimate that one such inspiral could occur once every million years (give or take an order or magnitude) in a galaxy like ours. With detectors capable of measuring gravitational waves in a volume that contains millions of galaxies, as will be the case with advanced versions of the LIGO and Virgo instruments, the number of detectable events becomes interesting.

Another important feature of radiative losses is the circularization of orbits. When the gravitational waves from an inspiralling compact binary enter the frequency band of the LIGO and Virgo instruments, the system’s semi-major axis $a$ is of the order of $1 0 0 0 \mathrm { k m }$ or less, and is therefore much smaller than its initial value $a _ { 0 }$ . Equation (12.89) then implies that the orbital eccentricity will be vanishingly small, irrespective of its initial value. This circumstance greatly simplifies the nature of the expected gravitational-wave signal, and reduces the challenge of devising data-analysis strategies to measure the waves.

Because the interferometers are broad-band detectors, they effectively detect the gravitational wavetrain cycle by cycle, measuring not only the varying strength within each cycle, but also the varying frequency as the inspiral proceeds. Studies of optimal detection strategies have shown that these measurements, particularly of the varying wave frequency or phase, can be very accurate, depending of course on the strength of the signal compared to instrumental noise. To exploit these optimal strategies, one must be able to predict the evolution of the phase to high accuracy, and this requires going beyond the quadrupole formula by incorporating higher-order post-Newtonian corrections in calculations of the gravitational-wave signal.

With this in mind, we now calculate the first post-Newtonian corrections to the fluxes of energy, momentum, and angular momentum emitted by a binary system in circular orbit, and infer the rate at which the orbital frequency changes with time. The gravitational waves emitted by a post-Newtonian binary system in circular motion were calculated in Sec. 11.4.6. There we introduced

$$
\beta : = \left( \frac { G m \Omega } { c ^ { 3 } } \right) ^ { 1 / 3 }
$$

as a meaningful post-Newtonian expansion parameter, defined directly in terms of the total mass $m$ and orbital frequency $\Omega$ . The orbital velocity is then given by $\upsilon / c = \beta [ 1 -$ $\frac { 1 } { 3 } ( 3 - \eta ) \beta ^ { 2 } + O ( \beta ^ { 4 } ) ]$ , and the orbital radius is determined from $G m / ( c ^ { 2 } r ) = \beta ^ { 2 } [ 1 + { \textstyle { \frac { 1 } { 3 } } } ( 3 -$ $\eta ) \beta ^ { 2 } + O ( \beta ^ { 4 } ) ]$ . The gravitational-wave polarizations are expressed as

$$
h _ { + , \times } = \frac { 2 \eta G m } { c ^ { 2 } R } \beta ^ { 2 } H _ { + , \times } ,
$$

with $H _ { + , \times }$ expanded as

$$
H _ { + , \times } = H _ { + , \times } ^ { [ 0 ] } + \Delta \beta H _ { + , \times } ^ { [ 1 / 2 ] } + \beta ^ { 2 } H _ { + , \times } ^ { [ 1 ] } + \Delta \beta ^ { 3 } H _ { + , \times } ^ { [ 3 / 2 ] } + \beta ^ { 3 } H _ { + , \times } ^ { \mathrm { t a i l } } + O ( \beta ^ { 4 } ) ,
$$

where  := (M1 − M2)/m is the dimensionless mass difference. Each contribution H [n]+,× is a function of the inclination angle $\iota$ and of the orbital phase $\Psi : = \Omega \tau + \omega$ , where $\omega$ is a second orientation angle. Explicit expressions appear in Eqs. (11.296) and (11.297).

The most efficient way to compute $\mathcal { P } , \mathcal { F } ^ { j }$ , and $\mathcal { T } ^ { j k }$ is to proceed via Eqs. (12.45), (12.46), and (12.48), which express the fluxes directly in terms of the gravitational-wave polarizations. To reflect the choice of transverse basis made here (and inherited from Sec. 11.2.2), we make the identifications $\vartheta = \iota$ and $\varphi = { \frac { \pi } { 2 } } - \omega$ . Because the time dependence of each polarization is contained in the orbital phase $\Psi$ , derivatives with respect to $\tau$ can be evaluated as $\partial _ { \tau } = \Omega \partial _ { \Psi }$ , and derivatives with respect to $\varphi$ can similarly be expressed as $- \partial _ { \Psi }$ .

Simple computations return

$$
\begin{array} { l } { { \displaystyle { \mathcal { P } } = \frac { 3 2 } { 5 } \eta ^ { 2 } \displaystyle \frac { c ^ { 5 } } { G } \beta ^ { 1 0 } \biggl [ 1 - \biggl ( \frac { 1 2 4 7 } { 3 3 6 } + \frac { 3 5 } { 1 2 } \eta \biggr ) \beta ^ { 2 } + 4 \pi \beta ^ { 3 } + O ( \beta ^ { 4 } ) \biggr ] , } } \\ { { \displaystyle { \mathcal { F } } ^ { x } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \displaystyle \frac { c ^ { 4 } } { G } \beta ^ { 1 1 } \biggl [ 1 - \biggl ( \frac { 4 5 2 } { 8 7 } + \frac { 1 1 3 9 } { 5 2 2 } \eta \biggr ) \beta ^ { 2 } + O ( \beta ^ { 3 } ) \biggr ] \sin \Omega \tau , } } \\ { { \displaystyle { \mathcal { F } } ^ { y } = - \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \displaystyle \frac { c ^ { 4 } } { G } \beta ^ { 1 1 } \biggl [ 1 - \biggl ( \frac { 4 5 2 } { 8 7 } + \frac { 1 1 3 9 } { 5 2 2 } \eta \biggr ) \beta ^ { 2 } + O ( \beta ^ { 3 } ) \biggr ] \cos \Omega \tau . } } \end{array}
$$

We also have that $\mathcal { F } ^ { z } = 0 = \mathcal { T } ^ { y z } = \mathcal { T } ^ { z x }$ , and $\mathcal { T } ^ { x y }$ is related to $\mathcal { P }$ by $\mathcal { P } = \Omega \mathcal { T } ^ { x y }$ . We see that these expressions reduce to Eqs. (12.79) when $\beta \ll 1$ .

We observe that $\mathcal { P }$ contains no correction term at order $\beta$ , in spite of the fact that the gravitational-wave polarizations do possess such terms; a $0 . 5 \mathrm { { P N } }$ correction to the energy flux would have to come from an interaction between the $H ^ { [ 0 ] }$ and $H ^ { [ 1 / 2 ] }$ terms within $H$ , but because these signals are out of phase, the interaction produces no flux. We observe also that $\mathcal { P }$ contains a term at order $\beta ^ { 3 }$ , and such a term has three possible origins. First, it might have originated from an interaction between $H ^ { [ 0 ] }$ and $H ^ { [ 3 / 2 ] }$ , but this produces no flux because these signals also are out of phase. Second, it might have originated from an interaction between $H ^ { [ 1 ] }$ and $H ^ { [ 1 / 2 ] }$ , but this does not contribute for the same reason. The only remaining possibility is an interaction between $H ^ { [ 0 ] }$ and $H ^ { \mathrm { t a i l } }$ ; these signals are in phase, and their interaction does indeed contribute to the energy flux. The $4 \pi \beta ^ { 3 }$ term within Eq. (12.96a) has its origin in the tail effect; it is a wave-propagation correction to the leading-order expression that appears outside the large square brackets.

Taking inspiration from Sec. 12.3.3, we insert the energy flux of Eq. (12.96) within the energy-balance equation $d E / d t = - \mathcal { P }$ to determine the orbital evolution of a post-Newtonian binary system. From Eqs. (10.9) and (10.11) we know that the orbital energy of the two-body system is given by

$$
E = - \frac { 1 } { 2 } \eta m c ^ { 2 } \beta ^ { 2 } \biggl [ 1 - \frac { 1 } { 1 2 } ( 9 + \eta ) \beta ^ { 2 } + O ( \beta ^ { 4 } ) \biggr ] ,
$$

and $d E / d t$ is therefore related to $d \beta / d t$ , the rate of change of the velocity parameter of Eq. (12.93). Solving for this yields

$$
\frac { d \beta } { d t } = \frac { 3 2 } { 5 } \eta \frac { c ^ { 3 } } { G m } \beta ^ { 9 } \biggl [ 1 - \biggl ( \frac { 7 4 3 } { 3 3 6 } + \frac { 1 1 } { 4 } \eta \biggr ) \beta ^ { 2 } + 4 \pi \beta ^ { 3 } + O ( \beta ^ { 4 } ) \biggr ] ,
$$

and integration produces $\Omega$ as a function of time.

We have computed the orbital evolution of a circular binary system through $1 . 5 \mathrm { P N }$ order beyond the leading order, quadrupole-formula expression. This degree of accuracy is not sufficient for the purpose of measuring gravitational waves with the advanced LIGO and Virgo detectors. For this it is proving necessary to calculate the energy flux and the resulting expression for $d \beta / d t$ through $3 . 5 \mathrm { { P N } }$ order beyond the quadrupole formula.

# 12.4.3 “How black holes get their kicks”

[The title of this section is borrowed from a seminal paper on black-hole recoils by Marc Favata, Scott Hughes, and Daniel Holz (2004). It inspired others to title their papers with equally bad puns. Among the notable cases we find Getting a kick out of numerical relativity by Baker et al. (2006), and Total recoil by Gonzalez et al. (2007).]

Another radiative loss with potentially important astrophysical consequences is the radiation of linear momentum and the resulting recoil of the system. This is particularly important for binary inspirals. Because momentum is radiated in the direction of motion of the lighter body, the center-of-mass of the system must recoil in the opposite direction. But this direction is continually changing as the bodies move on their orbits, and the center-ofmass spirals outward from its initial position, with a growing radius and an ever increasing speed as the radiation gains in intensity. Finally, after the bodies have merged and settled down to a stationary state (frequently a rotating black hole), the center-of-mass moves off with whatever velocity it had when the radiation terminated.

This so-called “kick velocity” can easily be estimated for an inspiralling circular orbit. We appeal to Eqs. (12.79b) and (12.79c), which inform us that the center-of-mass must recoil according to

$$
\frac { d { \pmb P } } { d t } = - \pmb \mathcal { F } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \frac { c ^ { 4 } } { G } ( v / c ) ^ { 1 1 } \pmb \lambda ,
$$

where $\lambda = [ - \sin \phi , \cos \phi , 0 ]$ is tangent to the orbit. As we observed back in Eqs. (12.82b) and (12.82c), the averaged momentum flux vanishes when the orbital speed and frequency are constant. During an inspiral, however, the speed and frequency increase with time (over a very long radiation-reaction time scale), and the long-term average does not vanish. Integrating Eq. (12.99) from $t = - \infty$ to the present time using an adiabatic approximation, we find that the final kick velocity is given by (see Exercise 12.7)

$$
V _ { \mathrm { k i c k } } = \frac { 4 6 4 } { 1 0 5 } \Delta \eta ^ { 2 } \left( \frac { G m } { c ^ { 2 } a } \right) ^ { 4 } c { \pmb n } ,
$$

modulo corrections of higher post-Newtonian order. Note that for a given final orbital velocity $v \sim { \sqrt { G m / a } }$ , the kick velocity is independent of the total mass of the system. It is directed along $\pmb { n } = [ \cos \phi , \sin \phi , 0 ]$ , toward the more massive body. It vanishes in the limit of equal masses ( $\triangle = 0$ ) by symmetry.

For a final separation of $a = 1 0 G m / c ^ { 2 }$ , the recoil speed is equal to $1 3 3 \Delta \eta ^ { 2 } \ \mathrm { k m / s }$ . Because Eq. (12.100) is valid only for $G m / c ^ { 2 } a \ll 1$ , it cannot be trusted for smaller separations, but it should continue to give a reliable order-of-magnitude estimate of the recoil. Numerical simulations of the final inspiral of two non-rotating black holes have produced maximum kick velocities of around $1 7 5 ~ \mathrm { k m / s }$ , for the mass ratio that maximizes the coefficient $\Delta \eta ^ { 2 }$ . Such velocities are probably too small to be of astrophysical importance. When the black holes are spinning rapidly, however, with spin axes misaligned relative to each other and to the orbital angular momentum, the simulations have shown that the combination of momentum flux and strong precessions of the orbital plane can result in “superkicks” as high as several thousand kilometers per second. Such velocities are astrophysically relevant for supermassive black-hole binaries, leading possibly to the ejection of the final black hole from the galaxy that hosted the inspiralling progenitor, or at least to a significant displacement of the final hole from the central core of the galaxy. There is now preliminary evidence for situations in which an accreting massive black hole is apparently displaced and moving away from the center of its host galaxy, with a velocity characteristic of a superkick.

# 12.5 Radiation-reaction potentials

In this section and the following ones we return to the near zone and work on obtaining expressions for the radiation-reaction force acting within a matter distribution. The analogous situation in electromagnetism was examined in Sec. 12.1.4, where we explained that the radiation-reaction force arises from terms in the potentials that come with an odd power of the expansion parameter $c ^ { - 1 }$ . In electromagnetism the leading-order term in the radiation-reaction force scales as $c ^ { - 3 }$ , and represents a $1 . 5 \mathrm { { p c } }$ correction to the equations of motion; the scaling reflects the fact that radiative losses are dominated by electric dipole radiation. We recall that we were able to obtain the radiation-reaction force at $1 . 5 \mathrm { { p c } }$ order without having to calculate conservative corrections to the equations of motion at 1pc order.

The situation is similar in gravitation. Here also the radiation-reaction force arises from terms in the potentials that come with odd powers of $c ^ { - 1 }$ in a post-Newtonian expansion. In this case, however, we shall find that the force scales as $c ^ { - 5 }$ to reflect the fact that radiative losses are dominated by mass quadrupole radiation; the radiation-reaction force represents a $2 . 5 \mathrm { { p N } }$ correction to the equations of motion. Conservative corrections at 1pn order were obtained in Secs. 8.4 and 9.3, and we shall see that the computations at $2 . 5 \mathrm { { p N } }$ order are insensitive to corrections at 2pn order; these are not required for our discussion, and they will not be computed.

In this section we calculate the gravitational potentials that give rise to the radiationreaction force. Our final results are summarized in Box 12.3. In Sec. 12.6 we involve these potentials in a calculation of the radiation-reaction force acting within a perfect fluid. In Sec. 12.7 we specialize these results to a system of well-separated bodies. In Sec. 12.8 we examine alternative gauges that simplify the description of radiation reaction, and in Sec. 12.9 we calculate the orbital evolution of a two-body system under radiation reaction.

# 12.5.1 Near-zone potentials

A large part of the work required to identify the potentials responsible for radiation reaction has already been done back in Sec. 7.1.2. There we saw that the potentials are decomposed as $h ^ { \alpha \beta } = h _ { { \mathcal { N } } } ^ { \alpha \beta } + h _ { { \mathcal { W } } } ^ { \alpha \beta }$ , into contributions from a near-zone domain $\mathcal { N }$ and a complementary wave-zone domain $\mathcal { W }$ . The potentials $h _ { \mathcal { N } } ^ { \alpha \beta }$ were expanded in powers of $c ^ { - 1 }$ , up to and including $O ( c ^ { - 7 } )$ for $h _ { \mathcal { N } } ^ { 0 0 }$ , $O ( c ^ { - 6 } )$ for $h _ { \mathcal { N } } ^ { 0 j }$ N, and $O ( c ^ { - 5 } )$ for $h _ { \mathcal { N } } ^ { j k }$ ; judicious use was made of the conservation equations $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ to convert some terms into surface integrals at the boundary of the near zone. In Eqs. (7.15) we obtained the expressions

$$
\begin{array} { r l } { \kappa _ { 1 5 } ^ { \mathrm { t o t } } = } & { \epsilon ^ { \mathrm { g r } } [ \int _ { c } \epsilon ^ { \mathrm { c } } \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 1 - \epsilon ^ { 2 } } \epsilon ^ { \mathrm { i } \epsilon } ] + \frac { 1 } { 2 } \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 3 } \int _ { c } \epsilon ^ { - \mathrm { c } } \epsilon ^ { \mathrm { i } \epsilon } \sin \epsilon \ : \ : \ : \kappa _ { 1 } ^ { \mathrm { t o t } } d \Omega ^ { \epsilon } } \\ & { \quad - \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 3 } \epsilon ^ { 2 } ( \theta + \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 3 } \epsilon ^ { 2 } ) ^ { 2 } \sin ^ { 2 } \epsilon \ : \int _ { c } \epsilon ^ { - \mathrm { c } } \epsilon ^ { \mathrm { i } \epsilon } \ : - \ : \epsilon ^ { - 1 } d \Omega ^ { \epsilon } } \\ & { \quad - \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 1 2 } \epsilon ^ { 2 } ( \theta + \epsilon ^ { \mathrm { i } \epsilon } ) ^ { 2 } \sin ^ { 2 } \epsilon \ : \int _ { c } \epsilon ^ { - \mathrm { c } } \epsilon ^ { \mathrm { i } \epsilon } \ : - \ : \epsilon ^ { - 1 } d \Omega ^ { \epsilon } } \\ & { \quad - \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 1 2 } [ 2 \epsilon \epsilon ^ { \mathrm { i } \epsilon } ] ^ { 2 } ( 2 \epsilon ^ { \mathrm { i } \epsilon } ) ^ { 2 } \sin ^ { 2 } \epsilon \ : ( 4 \epsilon ^ { \mathrm { i } \epsilon } ) ^ { 2 } \sin ^ { 2 } \epsilon \ : ( \theta + \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 3 } \epsilon ^ { 2 } ) \ : ( \theta + \epsilon ^ { \mathrm { i } \epsilon } ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\  \frac { \epsilon ^ { \mathrm { g r } } } { 1 - \epsilon ^ { 2 } } = \frac { \epsilon ^ { \mathrm { g r } } } { 6 } [ \int _ { c } \epsilon ^ { - \mathrm { c } } \frac { \epsilon ^ { \mathrm { i } \epsilon } } { 1 - \epsilon ^ { 2 } } [ \epsilon ^ { \mathrm { g r } } \epsilon + \frac { 1 }  2 \end{array}
$$

In each Poisson integral the components of the effective energy-momentum pseudotensor $\tau ^ { \alpha \beta }$ are expressed as functions of $t$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ , and the integration is over the near-zone domain $\mathcal { M }$ defined by $r ^ { \prime } : = | { \pmb x } ^ { \prime } | < \mathcal { R }$ , where $\mathcal { R }$ is the arbitrary cutoff radius between the near and wave zones. As we explained back in Sec. 6.3.3, we are interested in the $\mathcal { R }$ -independent pieces of each integral.

The various multipole moments that appear in the potentials were defined by Eqs. (7.16); for convenience we list them explicitly here:

$$
\begin{array} { r l } & { T ^ { H } ( t ) : = \displaystyle \int _ { \mathcal { A } } c ^ { - 2 } \tau ^ { \mathrm { a b } } ( t , x ) x ^ { k } x ^ { l } d ^ { 3 } x , } \\ & { T ^ { j ( \mathrm { b } 0 ) } ( t ) : = \displaystyle \int _ { \mathcal { A } } c ^ { - 2 } \tau ^ { \mathrm { a b } } ( t , x ) x ^ { j } x ^ { k } x ^ { l } d ^ { 3 } x , } \\ & { T ^ { H } ( t ) : = \displaystyle \int _ { \mathcal { A } } c ^ { - 2 } \tau ^ { \mathrm { a b } } ( t , x ) x ^ { k } r ^ { 2 } d ^ { 3 } x , } \\ & { T ^ { H } ( t ) : = \displaystyle \int _ { \mathcal { A } } c ^ { - 2 } \tau ^ { \mathrm { a b } } ( t , x ) r ^ { 4 } d ^ { 3 } x , } \\ & { \mathcal { I } ^ { n k } ( t ) : = \displaystyle e ^ { \mathrm { i } n \theta } \int _ { \mathcal { A } } c ^ { - 1 } \tau ^ { \mathrm { a b } } ( t , x ) x ^ { n } x ^ { k } d ^ { 3 } x , } \\ & { \mathcal { M } ^ { i / k m } : = \displaystyle \int _ { \mathcal { A } } c ^ { \mathrm { i } k } ( t , x ) r ^ { 2 } d ^ { 3 } x . } \end{array}
$$

We explained in $\mathrm { B o x } ~ 7 . 1$ how the multipole moments end up appearing in the expansions of hαβN i n powers of $c ^ { - 1 }$ , and how these manipulations give rise to additional boundary terms $h ^ { \alpha \beta } [ \partial \mathcal { M } ]$ . All such boundary terms must be carefully examined, and we assert that at all post-Newtonian orders to be considered in this section, the boundary terms contain no $\mathcal { R }$ -independent pieces, and they can therefore be safely discarded. We shall not prove this assertion here, but you may be comforted with the assurance that each boundary term in Eq. (12.101) was examined by us and shown to make no $\mathcal { R }$ -independent contribution to the potentials.

It was established back in Sec. 7.3.4 that $h _ { \mathcal { W } } ^ { \alpha \beta }$ first makes a contribution at 3pn order in the near zone, and because our considerations in this section are limited to $2 . 5 \mathrm { { p N } }$ order, this can be ignored. The complete near-zone potentials $h ^ { \alpha \beta }$ can therefore be identified with those of Eqs. (12.101).

# 12.5.2 Odd terms in the potentials

The terms that come with an odd power of $c ^ { - 1 }$ within the curly brackets in Eqs. (12.101) will be the focus of our attention; it is these that are responsible for the radiation reaction. We have to keep in mind that while some factors of $c ^ { - 1 }$ appear explicitly in these equations, some are contained implicitly in the source functions $\tau ^ { \alpha \beta }$ . To identify the explicit and implicit odd terms, it is useful to introduce the notation

$$
h ^ { 0 0 } : = \frac { 4 } { c ^ { 2 } } V , \qquad h ^ { 0 j } : = \frac { 4 } { c ^ { 3 } } V ^ { j } , \qquad h ^ { j k } : = \frac { 4 } { c ^ { 4 } } W ^ { j k } ,
$$

for the potentials, and the notation

$$
\tau ^ { 0 0 } : = \varrho c ^ { 2 } , \qquad \tau ^ { 0 j } : = s ^ { j } c \qquad \tau ^ { j k } : = \tau ^ { j k } ,
$$

for the source functions. We next express the post-Newtonian expansion of the potentials as

$$
V = V [ 0 ] + c ^ { - 2 } V [ 2 ] + c ^ { - 4 } V [ 4 ] + O ( c ^ { - 6 } ) + c ^ { - 3 } V [ 3 ] + c ^ { - 5 } V [ 5 ] + O ( c ^ { - 7 } ) ,
$$

$$
\begin{array} { c c } { { V ^ { j } = V ^ { j } [ 0 ] + c ^ { - 2 } V ^ { j } [ 2 ] + O ( c ^ { - 4 } ) + c ^ { - 3 } V ^ { j } [ 3 ] + O ( c ^ { - 5 } ) , } } & { { ( 1 2 ) } } \\ { { { } } } & { { { } } } \\ { { W ^ { j k } = W ^ { j k } [ 0 ] + c ^ { - 2 } W ^ { j k } [ 2 ] + O ( c ^ { - 4 } ) + c ^ { - 1 } W ^ { j k } [ 1 ] + c ^ { - 3 } W ^ { j k } [ 3 ] + O ( c ^ { - 5 } ) , } } & { { } } \end{array}
$$

where we have separated the odd-order terms from the even-order terms, and we express the post-Newtonian expansion of the source functions as

$$
\begin{array} { c } { { \varrho = \varrho [ 0 ] + c ^ { - 2 } \varrho [ 2 ] + c ^ { - 4 } \varrho [ 4 ] + O ( c ^ { - 6 } ) + c ^ { - 5 } \varrho [ 5 ] + O ( c ^ { - 7 } ) , } } \\ { { s ^ { j } = s ^ { j } [ 0 ] + c ^ { - 2 } s ^ { j } [ 2 ] + O ( c ^ { - 4 } ) + c ^ { - 5 } s ^ { j } [ 5 ] + O ( c ^ { - 7 } ) , } } \\ { { \tau ^ { j k } = \tau ^ { j k } [ 0 ] + c ^ { - 2 } \tau ^ { j k } [ 2 ] + O ( c ^ { - 4 } ) + c ^ { - 5 } \tau ^ { j k } [ 5 ] + O ( c ^ { - 7 } ) . } } \end{array}
$$

The expansions of Eqs. (12.105) are directly imported from Eqs. (12.101). The expansions of Eqs. (12.106), however, incorporate an assumption that the odd terms in the source functions begin at order $c ^ { - 5 }$ ; this assumption will be justified below.

When we substitute Eqs. (12.106) into Eqs. (12.101) and read off the various odd potentials from Eqs. (12.105), we find that

$$
\begin{array} { r l } & { \quad V [ 3 ] = - \frac { 1 } { 6 } \frac { \partial ^ { 2 } k ^ { 2 } ( \Omega ) } { \partial t } [ 0 ] , } \\ & { \quad V [ 5 ] = - \mathcal { C } \int _ { \mathcal { L } } \frac { \partial ^ { 3 } k ^ { 2 } } { | x - x | ^ { 2 } } \delta ^ { 3 , \nu } - \frac { 1 } { 6 } \frac { \partial ^ { 2 } k ^ { 2 } ( \Omega ) } { \partial t } [ 0 ] } \\ & { \quad \quad - \frac { 1 } { 1 2 0 } G \left[ ( 4 \pi ^ { 3 } k ^ { 2 } + 2 \pi ^ { 2 } k ^ { 2 } ) \frac { \partial ^ { 3 } k ^ { 4 } ( \Omega ) } { \partial t } - 4 \pi ^ { 5 } \frac { \partial ^ { 4 } k ^ { 2 } ( \Omega ) } { \partial t } [ 0 ] + \frac { \partial ^ { 2 } k ^ { 2 } ( \Omega ) } { 2 } [ 0 ] \right] , } \\ & { \quad V [ 3 ] = \frac { 1 } { 1 8 } G \left\{ 3 k ^ { 4 } \pi ^ { 5 } \tilde { L } ( \Omega ) - \frac { \delta ^ { 2 } k ^ { 4 } ( \Omega ) } { \partial t } ( 0 ] + 2 \pi ^ { 6 } \tilde { L } ^ { 2 } ( \Omega ) \right\} , } \\ & { \quad \quad \psi ^ { \mathcal { R } [ 3 ] } = - \frac { 1 } { 2 } \frac { \partial ^ { 2 } k ^ { 2 } ( \Omega ) } { \partial t ^ { 2 } } [ 0 ] , } \\ & { \quad \quad \psi ^ { \mathcal { R } [ 5 ] } = - \frac { 1 } { 2 } \frac { 1 } { 6 } G ^ { \mathcal { R } [ 5 ] } [ 2 ] - \frac { 1 } { 3 6 } G \left\{ 3 ^ { 2 } k ^ { 2 } \frac { \partial ^ { 3 } k ^ { 4 } } { \partial t } [ 0 ] - 2 \pi ^ { 8 } \frac { \partial ^ { 3 } k ^ { 2 } \tilde { L } ^ { 2 } k ( \Omega ) } { \partial t } [ 0 ] \right. } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

The bracket notation was extended to the multipole moments; for example $\mathcal { T } ^ { j k } [ 0 ]$ is the quadrupole moment constructed from $\varrho [ 0 ]$ , the 0pn piece of the effective mass density. We can now appreciate what was meant by implicit and explicit odd terms: Examining the expression for $V [ 5 ]$ , we see that the terms involving the multipole moments were listed explicitly in Eqs. (12.101), but that the Poisson integral involving $\varrho [ 5 ]$ was present only implicitly; it has now become fully explicit, thanks to the expansions of Eqs. (12.106). For future reference we note that

$$
W [ 1 ] : = \delta _ { j k } W ^ { j k } [ 1 ] = 3 V [ 3 ] = - \frac { 1 } { 2 } G \mathcal { T } ^ { k k } [ 0 ]
$$

is an immediate consequence of Eqs. (12.107).

# 12.5.3 Odd terms in the effective energy-momentum tensor

To proceed we must justify the assumption made in Eqs. (12.106), that the odd terms in $\varrho$ , $s ^ { j }$ , and $\tau ^ { j k }$ begin at order $c ^ { - 5 }$ , and we must obtain an expression for $\varrho [ 5 ]$ . We recall that the effective energy-momentum pseudotensor is defined by Eq. (6.52); it is given by

$$
\tau ^ { \alpha \beta } = ( - g ) \big ( T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } + t _ { \mathrm { H } } ^ { \alpha \beta } \big ) ,
$$

in terms of a material contribution $T ^ { \alpha \beta }$ , the Landau–Lifshitz pseudotensor $t _ { \mathrm { L L } } ^ { \alpha \beta }$ of Eq. (6.5), and the harmonic pseudotensor $t _ { \mathrm { H } } ^ { \alpha \beta }$ of Eq. (6.53).

We begin with an examination of the material contribution. As usual we take the matter distribution to consist of a perfect fluid, and we adopt the set of variables $\mathfrak { m } : = \{ \rho ^ { * } , p , \Pi , \pmb { v } \}$ that was first introduced in Sec. 7.1.1. Here $\rho ^ { * } : = \sqrt { - g } \gamma \rho$ is the conserved mass density, $p$ is the pressure, $\Pi$ is the specific internal energy, and $\pmb { v }$ is the velocity field; we also have that $\rho$ is the fluid’s proper mass density, $g$ is the metric determinant, and $\gamma : = u ^ { 0 } / c$ is determined by the normalization condition $g _ { \alpha \beta } u ^ { \alpha } u ^ { \beta } = - c ^ { 2 }$ for the spacetime velocity field $u ^ { \alpha } : = \gamma ( c , \pmb { v } )$ . We recall that $\rho ^ { * }$ satisfies the continuity equation $\partial _ { t } \rho ^ { * } + \partial _ { j } ( \rho ^ { * } v ^ { j } ) = 0$ , which expresses conservation of rest mass, and that the fluid’s energy-momentum tensor is given by

$$
T ^ { \alpha \beta } = ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) u ^ { \alpha } u ^ { \beta } + p g ^ { \alpha \beta } ,
$$

where $\epsilon = \rho \Pi$ is the proper density of internal energy.

Because the metric enters explicitly in Eq. (12.110), the energy-momentum tensor possesses a dependence upon the gravitational potentials, and it therefore contains terms that are odd in $c ^ { - 1 }$ . To find these we first calculate the metric, which can be obtained from Eqs. (7.23); a short computation reveals that

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + ( \mathrm { e v e n } ) + \frac { 2 } { c ^ { \delta } } \bigl ( V [ 3 ] + W [ 1 ] \bigr ) + O ( c ^ { - 7 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } + ( \mathrm { e v e n } ) + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g ^ { 0 0 } = - 1 + ( \mathrm { e v e n } ) - \frac { 2 } { c ^ { 5 } } \bigl ( V [ 3 ] + W [ 1 ] \bigr ) + O ( c ^ { - 7 } ) , } } \\ { { \displaystyle g ^ { j k } = \delta ^ { j k } + ( \mathrm { e v e n } ) + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle \sqrt { - g } = 1 + ( \mathrm { e v e n } ) + \frac { 2 } { c ^ { 5 } } \bigl ( V [ 3 ] - W [ 1 ] \bigr ) + O ( c ^ { - 7 } ) , } } \end{array}
$$

where (even) designates terms of order $c ^ { - 2 } , c ^ { - 4 }$ , and so on. As a consequence of Eq. (12.101) we find that the odd terms in $g _ { 0 j }$ first appear at order $c ^ { - 6 }$ and can be neglected. (We are aware that 6 is an even number; we stubbornly call it odd because $g _ { 0 j }$ is generated mostly by $h ^ { 0 j } = 4 V ^ { j } / c ^ { 3 }$ , whose leading radiation-reaction piece comes from $V ^ { j }$ [3]. Recall that $g _ { 0 j }$ couples to $v ^ { j } / c$ in the energy-momentum tensor, converting the $c ^ { - 6 }$ into a genuinely odd term of order $c ^ { - 7 }$ .) From these expressions for the metric we obtain

$$
\gamma = 1 + ( \mathrm { e v e n } ) + \frac { 1 } { c ^ { 5 } } \big ( V [ 3 ] + W [ 1 ] \big ) + { \cal O } ( c ^ { - 7 } ) ,
$$

and conclude that odd terms first appear at order $c ^ { - 5 }$ in the energy-momentum tensor. For example, the material contribution to $\varrho$ , given by $c ^ { - 2 } ( - g ) T ^ { 0 0 }$ , is

$$
\varrho _ { \mathrm { m a t t e r } } = \rho ^ { * } \bigg [ 1 + ( \mathrm { e v e n } ) + \frac { 1 } { c ^ { 5 } } \big ( 3 V [ 3 ] - W [ 1 ] \big ) + O ( c ^ { - 7 } ) \bigg ] .
$$

The relation of Eq. (12.108) implies that the $O ( c ^ { - 5 } )$ term actually vanishes, and this means that there is no matter contribution to $\varrho [ 5 ]$ .

We next examine the Landau–Lifshitz pseudotensor. Its definition is provided by Eq. (6.5), and we express it in the schematic form

$$
( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta } = \frac { c ^ { 4 } } { 1 6 \pi G } ( \partial h \partial h ) ^ { \alpha \beta } .
$$

The overall factor of $c ^ { 4 }$ on the right-hand side implies that a term of order $c ^ { - 7 }$ in $( \partial h \partial h ) ^ { 0 0 }$ makes a contribution to $\varrho [ 5 ]$ , a term of order $c ^ { - 8 }$ in $( \partial h \partial h ) ^ { 0 j }$ makes a contribution to $s ^ { j } [ 5 ]$ , and a term of order $c ^ { - 9 }$ in $( \partial h \partial h ) ^ { j k }$ makes a contribution to $\tau ^ { j k } [ 5 ]$ . The various derivatives of the potentials are given by

$$
\begin{array} { r l } & { \partial _ { n } h ^ { ( 0 ) } = \frac { 4 } { c ^ { 2 } } \{ 3 _ { n } V [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - \delta } \partial _ { n } V [ 5 ] + O ( c ^ { - \gamma } ) \} , } \\ & { \partial _ { n } h ^ { ( 0 ) } = \frac { 4 } { c ^ { 3 } } \{ 3 _ { n } V ^ { \gamma } [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - 3 } \partial _ { n } V ^ { \gamma } [ 3 ] + O ( c ^ { - 5 } ) \} , } \\ & { \partial _ { n } h ^ { ( k ) } = \frac { 4 } { c ^ { 4 } } \{ 3 _ { n } W ^ { \beta k } [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - 3 } \partial _ { n } W ^ { \beta k } [ 3 ] + O ( c ^ { - 5 } ) \} , } \\ & { \partial _ { 0 } h ^ { ( 0 ) } = \frac { 4 } { c ^ { 3 } } \{ 3 _ { t } V [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - 3 } \partial _ { t } V [ 3 ] + O ( c ^ { - 5 } ) \} , } \\ & { \partial _ { 0 } h ^ { ( 0 ) } = \frac { 4 } { c ^ { 4 } } \{ 3 _ { t } V ^ { \gamma } [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - 3 } \partial _ { t } V ^ { \beta } [ 3 ] + O ( c ^ { - 5 } ) \} , } \\ & { \partial _ { 0 } h ^ { ( k ) } = \frac { 4 } { c ^ { 5 } } \{ 3 _ { t } W ^ { \beta k } [ 0 ] + O ( c ^ { - 2 } ) + c ^ { - 3 } \partial _ { t } W ^ { \beta k } [ 1 ] + O ( c ^ { - 3 } ) \} . } \end{array}
$$

in which we have included only the required terms; note that $V [ 3 ]$ and $W ^ { j k } [ 1 ]$ do not appear in $\partial _ { n } h ^ { 0 0 }$ and $\partial _ { n } h ^ { j k }$ , because they do not depend on the spatial coordinates.

Referring to Eq. (6.5), we observe that a typical term in $( \partial h \partial h ) ^ { \alpha \beta }$ actually has the form of $g g \partial h \partial h$ . (There are also terms of the form $g g g g \partial h \partial h$ , but they need not be distinguished for the purpose of this argument.) There are two ways of generating terms that contain an odd power of $c ^ { - 1 }$ . The first is to let $\partial h \partial h$ be odd in $c ^ { - 1 }$ , and to keep the factor $g g$ even; the second is to let $g g$ be odd, and to keep $\partial h \partial h$ even.

In the first scenario we need to multiply an even term in one of the factors $\partial h$ by an odd term in the remaining $\partial h$ . Using the expansions of Eqs. (12.115), we find that the dominant scaling of such products is $c ^ { - 8 }$ , and that it is produced by the set

$$
\mathcal { S } _ { 1 } = \left\{ \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { 0 j } , \partial _ { p } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 0 } , \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { j k } \right\} .
$$

We also find that the set of products

$$
\begin{array} { r l r } & { } & { \mathcal { S } _ { 2 } = \{ \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { 0 0 } , \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { j k } , \partial _ { p } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 j } , \partial _ { p } h ^ { 0 j } \partial _ { q } h ^ { 0 k } ,  } \\ & { } & {  \partial _ { p } h ^ { 0 j } \partial _ { 0 } h ^ { 0 0 } , \partial _ { p } h ^ { 0 j } \partial _ { 0 } h ^ { k n } , \partial _ { 0 } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 0 } ,  \partial _ { 0 } h ^ { 0 0 } \partial _ { 0 } h ^ { j k } \} } \end{array}
$$

participates at order $c ^ { - 9 }$ .

In the second scenario we let the factors of $g$ supply the odd terms, and we keep $\partial h \partial h$ even. The leading odd terms in $g$ come at order $c ^ { - 5 }$ in $g _ { 0 0 }$ , order $c ^ { - 6 }$ in $g _ { 0 j }$ , and order $c ^ { - 5 }$ in $g _ { j k }$ . The leading even term in $\partial h \partial h$ comes from $\partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { 0 0 }$ at order $c ^ { - 4 }$ . After

multiplication we find that the set

$$
\mathcal { S } _ { 3 } = \left\{ h ^ { 0 0 } \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { 0 0 } , h ^ { j k } \partial _ { p } h ^ { 0 0 } \partial _ { q } h ^ { 0 0 } \right\}
$$

also participates at order $c ^ { - 9 }$ .

The next step is to decide how the various terms listed in $\mathcal { S } _ { 1 } , \mathcal { S } _ { 2 }$ , and $\mathcal { S } _ { 3 }$ enter in the components of the Landau–Lifshitz pseudotensor. A careful examination of Eq. (6.5) reveals that $\mathcal { S } _ { 1 }$ appears only in $( \partial h \partial h ) ^ { 0 j }$ , whose dominant odd term therefore scales as $c ^ { - 8 }$ ; this produces a contribution to $s ^ { j } [ 5 ]$ . It reveals also that $\mathcal { S } _ { 2 }$ and $\mathcal { S } _ { 3 }$ appear in $( \partial h \partial h ) ^ { 0 0 }$ and $( \partial h \partial h ) ^ { j k }$ , whose dominant odd terms scale as $c ^ { - 9 }$ ; this produces a contribution to $\varrho [ 7 ]$ and $\tau ^ { j k }$ [5]. We conclude from all this that the Landau–Lifshitz pseudotensor makes contributions at the expected odd order to the source functions, but that there is no contribution to $\varrho [ 5 ]$ .

Finally we examine the harmonic pseudotensor $( - g ) t _ { \mathrm { H } } ^ { \alpha \beta }$ . A similar sequence of steps allows us to conclude that the leading odd terms make contributions to [5], $s ^ { j } [ 5 ]$ , and $\tau ^ { j k } [ 5 ]$ ; the assumption contained in Eq. (12.106) is now fully justified. The contribution to $\varrho [ 5 ] c ^ { 2 }$ is produced by $- ( c ^ { 4 } / 1 6 \pi G ) h ^ { j k } \partial _ { j k } h ^ { 0 0 }$ on the right-hand side of Eq. (6.53), and from Eqs. (12.105) and (12.107) we find that this is given by

$$
\varrho [ 5 ] = - \frac { 1 } { \pi G } W ^ { j k } [ 1 ] \partial _ { j k } V [ 0 ] = \frac { 1 } { 2 \pi } \dddot { \mathcal { Z } } ^ { j k } [ 0 ] { \partial _ { j k } V [ 0 ] } .
$$

To put this in its final form we recall that the [0] label refers to the Newtonian limit. The quadrupole moment is therefore the Newtonian moment $I ^ { j k }$ , and $V [ 0 ]$ is the Newtonian potential, which was denoted $U$ in previous chapters. What we have obtained, therefore, is

$$
\varrho [ 5 ] = \frac { 1 } { 2 \pi } \overset { . . . } I ^ { \cdot j k } \partial _ { j k } U .
$$

We have also established that no other implicit, odd-order contribution to the effective energy-momentum pseudotensor arises at $2 . 5 \mathrm { { p N } }$ order.

# 12.5.4 Radiation-reaction potentials: Final expressions

With $\varrho [ 5 ]$ in hand, we may now return to Eq. (12.107) and complete the computation of $V [ 5 ]$ . We need to evaluate the Poisson integral

$$
\int _ { \mathcal { M } } \frac { \varrho [ 5 ] } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } \boldsymbol { x } ^ { \prime } ,
$$

in which $\varrho [ 5 ]$ is expressed as a function of $t$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . Making the substitution from Eq. (12.120) gives

$$
\int _ { \mathcal { M } } \frac { \varrho [ 5 ] } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } = \frac { 1 } { 2 \pi } \ddot { I } ^ { j k } \int _ { \mathcal { M } } \frac { \partial _ { j ^ { \prime } k ^ { \prime } } U ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

and to deal with this we appeal to integration by parts. We begin by writing

$$
{ \frac { \partial _ { j ^ { \prime } k ^ { \prime } } U } { | { \pmb x } - { \pmb x } ^ { \prime } | } } = \partial _ { j ^ { \prime } } \bigg ( { \frac { \partial _ { k ^ { \prime } } U } { | { \pmb x } - { \pmb x } ^ { \prime } | } } \bigg ) - \partial _ { k ^ { \prime } } U \partial _ { j ^ { \prime } } { \frac { 1 } { | { \pmb x } - { \pmb x } ^ { \prime } | } } .
$$

Noting that $\partial _ { j ^ { \prime } } | { \pmb x } - { \pmb x } ^ { \prime } | = - \partial _ { j } | { \pmb x } - { \pmb x } ^ { \prime } |$ , this is

$$
{ \frac { \partial _ { j ^ { \prime } k ^ { \prime } } U } { | { \pmb x } - { \pmb x } ^ { \prime } | } } = \partial _ { j ^ { \prime } } \bigg ( { \frac { \partial _ { k ^ { \prime } } U } { | { \pmb x } - { \pmb x } ^ { \prime } | } } \bigg ) + \partial _ { j } \bigg ( { \frac { \partial _ { k ^ { \prime } } U } { | { \pmb x } - { \pmb x } ^ { \prime } | } } \bigg ) .
$$

Applying this trick once more, we obtain

$$
\frac { \partial _ { j ^ { \prime } k ^ { \prime } } U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } = \partial _ { j ^ { \prime } } \bigg ( \frac { \partial _ { k ^ { \prime } } U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } \bigg ) + \partial _ { j k ^ { \prime } } \bigg ( \frac { U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } \bigg ) + \partial _ { j k } \bigg ( \frac { U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } \bigg ) .
$$

Integration yields

$$
\begin{array} { r l } {  { \int _ { \mathcal { M } } \frac { \partial _ { j ^ { \prime } k ^ { \prime } } U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } \boldsymbol { x } ^ { \prime } = \oint _ { \partial \mathcal { M } } \frac { \partial _ { k ^ { \prime } } U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d S _ { j } + \partial _ { j } \oint _ { \partial \mathcal { M } } \frac { U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d S _ { k } } } \\ & { \phantom { \int _ { \partial \mathcal { M } } \frac { \partial _ { j ^ { \prime } k ^ { \prime } } U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d S _ { j } } + \partial _ { j k } \int _ { \mathcal { M } } \frac { U } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } \boldsymbol { x } ^ { \prime } . } \end{array}
$$

Inspection of the surface integrals reveals that they scale as $\mathcal { R } ^ { - 1 }$ and do not give rise to $\mathcal { R }$ -independent contributions to $V [ 5 ]$ . The remaining volume integral is nothing but $- 2 \pi X$ , up to an $\mathcal { R }$ -dependent constant, where $X$ is the post-Newtonian superpotential defined in Box 7.3. Our final expression for the integral is therefore $- 2 \pi \partial _ { j k } X$ .

We have arrived at

$$
\int _ { \mathcal { M } } \frac { \varrho [ 5 ] } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } = - \dddot { I } ^ { j k } \partial _ { j k } X .
$$

This result might have been anticipated on the grounds that the left-hand side is a solution to $\nabla ^ { 2 } ( \mathrm { L H S } ) = - 4 \pi \varrho [ 5 ] = - 2 \ddot { I } ^ { j k } \partial _ { j k } U = \nabla ^ { 2 } ( - \dddot { I } ^ { j k } \partial _ { j k } X ) ,$ , since the superpotential is itself a solution to $\nabla ^ { 2 } X = 2 U$ . The discussion of Box 7.3, however, warns us that integration of each side over a truncated domain $\mathcal { M }$ gives rise to boundary integrals that must be examined closely. In this case we have the happy circumstance that all such integrals give rise to $\mathcal { R }$ -dependent terms that can be ignored. In other circumstances the surface integrals might have made important contributions, and the detailed calculation presented here would have revealed them.

This computation completes the determination of the radiation-reaction potentials. Our results are summarized in Box 12.3.

<table><tr><td>Box 12.3</td><td colspan="2">Radiation-reaction potentials</td></tr><tr><td rowspan="3"></td><td>The gravitational potentials in the near zone can beexpandedas</td><td></td></tr><tr><td>h00 =</td><td>{)</td></tr><tr><td>4 hi = 23 hik =</td><td>{ui +0(-2)+c-3i[3]+0(c-5)}</td></tr></table>

in which $U : = V [ 0 ] , U ^ { j } : = V ^ { j } [ 0 ] ,$ and $P ^ { j k } : = W ^ { j k } [ 0 ]$ are the leading-order, near-zone potentials listed in $8 0 \times 7 . 5 .$ The terms that come with an odd power of $c ^ { - 1 }$ are the radiation-reaction potentials, and they are given by

$$
\begin{array} { r l } & { \quad V [ 3 ] = - \frac { 1 } { 6 } G ^ { - 2 } , } \\ & { \quad V [ 5 ] = G \left[ - \overline { { r } } ^ { - 3 } \partial _ { \alpha } k ^ { \alpha } - \frac { 1 } { 6 } \overline { { c } } ^ { \alpha } z ^ { 2 } \right] - \frac { 1 } { 6 0 } ( e ^ { - x ^ { 2 } y ^ { 2 } } + 2 x ^ { \prime } x ^ { \prime } ) ^ { \beta _ { 0 } } } \\ & { \qquad \quad + \frac { 1 } { 3 0 } \sigma ^ { 2 } ( \overline { { \rho } } + \frac { 1 } { 2 0 } ) ^ { \alpha } \epsilon - \frac { 1 } { 1 2 0 } \overline { { \rho } } ^ { \alpha } \epsilon } \\ & { \quad { r } ^ { - 5 } [ 3 ] = G \left[ \frac { 1 } { 6 } \epsilon ^ { \alpha } \overline { { r } } ^ { \alpha \beta } - \frac { 1 } { 1 8 } \overline { { \rho } } ^ { \alpha \beta } - \frac { 1 } { 6 } \overline { { r } } ^ { \beta \alpha } \right] , } \\ & { \quad { \psi } ^ { \beta _ { 0 } } [ 1 ] = - \frac { 1 } { 2 } G ^ { - 2 } , } \\ & { \quad { \psi } ^ { \beta _ { 0 } } [ 3 ] = G \left[ - \frac { 1 } { 2 } \overline { { r } } ^ { \beta _ { 0 } } [ 2 ] - \frac { 1 } { 1 2 } \epsilon ^ { \alpha } \overline { { r } } ^ { \alpha \beta } + \frac { 1 } { 1 8 } { s } ^ { \beta _ { 0 } } \epsilon ^ { \gamma \beta _ { 0 } } \right. } \\ & { \qquad \left. + \frac { 1 } { 9 } s ^ { \gamma } \left( \overline { { \rho } } ^ { \alpha \beta } + \frac { \gamma \beta \epsilon } { 2 0 } \right) - \frac { 1 } { 3 } \overline { { \gamma } } ^ { \alpha \beta } \right] } \end{array}
$$

They are expressed in terms of the Newtonian multipole moments

$$
\begin{array} { l } { I ^ { j k } : = \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x , } \\ { I ^ { j k n } : = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } d ^ { 3 } x , } \\ { I ^ { j k n } : = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } x ^ { n } d ^ { 3 } x , } \\ { I ^ { j k n } : = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } x ^ { n } d ^ { 3 } x , } \\ { J ^ { j k n } : = \int \rho ^ { * } ( v ^ { j } x ^ { k } - v ^ { k } x ^ { j } ) x ^ { n } d ^ { 3 } x , } \\ { I ^ { j k n } : = \int \left( \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } \right) x ^ { n } x ^ { n } d ^ { 3 } . } \end{array}
$$

These are functions of $t$ , and the number of overdots, or the number within an overlaid bracket, indicates the number of differentiations with respect to $t$ . The potentials also depend on $c ^ { - 2 }  { \boldsymbol { \mathcal { T } ^ { j k } } }$ [2], the post-Newtonian correction to the quadrupole moment; an expression for this is not be required in subsequent calculations. In addition, $V [ 5 ]$ depends on the post-Newtonian superpotential $X$ , defined by

$$
X = G \int \rho ^ { * } | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } ,
$$

in which the mass density $\rho ^ { * }$ is expressed as a function of $t$ and $\mathbf { \Delta } _ { x ^ { \prime } }$ .

# 12.6 Radiation reaction of fluid systems

Our main goal in this section is to calculate the radiation-reaction force density acting within a fluid distribution of conserved mass density $\rho ^ { * }$ , pressure $p$ , and velocity field $\pmb { v }$ . We rely on the formulation of post-Newtonian fluid dynamics initiated in Sec. 8.4, and work to obtain the terms of order $c ^ { - 5 }$ that must be inserted within the post-Newtonian generalization of Euler’s equation,

$$
\rho ^ { * } \frac { d v ^ { j } } { d t } = \rho ^ { * } \partial _ { j } U - \partial _ { j } p + ( \mathrm { e v e n } ) + f ^ { j } [ \mathrm { r r } ] .
$$

The first two terms on the right-hand side govern the Newtonian dynamics of the fluid, (even) designates the conservative corrections at 1pn and $2 \mathrm { P N }$ orders, and $f ^ { j } [ \mathrm { r r } ]$ is the radiation-reaction force density that we wish to obtain.

# 12.6.1 Metric, Christoffel symbols, and matter variables

We first determine the pieces of the metric that are involved in the derivation of the radiationreaction force. These are obtained by inserting the potentials of $\mathrm { B o x } 1 2 . 3$ within Eqs. (7.20). For our purposes here the non-linear terms are important, and after a straightforward computation we obtain

$$
\begin{array} { r l } & { g _ { 0 0 } = - 1 + 2 c ^ { - 2 } U + O ( c ^ { - 4 } ) + 8 c ^ { - 5 } V [ 3 ] + O ( c ^ { - 6 } ) } \\ & { \qquad + 2 c ^ { - 7 } \big ( V [ 5 ] + { \cal W } [ 3 ] \big ) - 2 4 c ^ { - 7 } V [ 3 ] { \cal U } + O ( c ^ { - 8 } ) , } \\ & { g _ { 0 j } = O ( c ^ { - 3 } ) + O ( c ^ { - 5 } ) - 4 c ^ { - 6 } V _ { j } [ 3 ] + O ( c ^ { - 7 } ) , } \\ & { g _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + 4 c ^ { - 5 } \big ( { \cal H } _ { j k } [ 1 ] - \delta _ { j k } { \cal V } [ 3 ] \big ) + O ( c ^ { - 6 } ) , } \\ & { g ^ { 0 0 } = - 1 - 2 c ^ { - 2 } { \cal U } + O ( c ^ { - 4 } ) - 8 c ^ { - 5 } { \cal V } [ 3 ] + O ( c ^ { - 6 } ) } \\ & { \qquad - 2 c ^ { - 7 } \big ( { \cal V } [ 5 ] + { \cal W } [ 3 ] \big ) - 8 c ^ { - 7 } { \cal V } [ 3 ] { \cal U } + O ( c ^ { - 8 } ) , } \\ & { g ^ { 0 j } = O ( c ^ { - 3 } ) + O ( c ^ { - 5 } ) - 4 c ^ { - 6 } { \cal V } ^ { j } [ 3 ] + O ( c ^ { - 7 } ) , } \\ & { g ^ { j k } = \delta ^ { j k } + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) - 4 c ^ { - 5 } ( { \cal W } ^ { j k } [ 1 ] - \delta ^ { j k } { \cal V } [ 3 ] \big ) + O ( c ^ { - 6 } ) , } \\ & { { \cal V } ^ { - g } = 1 + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) - 4 c ^ { - 5 } { \cal V } [ 3 ] + O ( c ^ { - 6 } ) . } \end{array}
$$

To arrive at these results we have taken into account the fact that $W [ 1 ] = 3 V [ 3 ]$ .

The metric allows us to obtain the radiation-reaction terms in the relevant Christoffel symbols, and another straightforward computation returns

$$
\begin{array} { l } { { c ^ { 2 } \Gamma _ { 0 0 } ^ { j } = - \partial _ { j } U + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) - c ^ { - 5 } } } \\ { { \mathrm {  ~ \ x ~ } \left( \partial ^ { j } V [ 5 ] + \partial ^ { j } W [ 3 ] + 4 \partial _ { t } V ^ { j } [ 3 ] - 4 W ^ { j k } [ 1 ] \partial _ { k } U - 8 V [ 3 ] \partial ^ { j } U \right) + O ( c ^ { - 6 } ) , } } \\ { { \mathrm {  ~ \Gamma ~ } ( 1 2 . 1 2 9 ) } } \\ { { c \Gamma _ { 0 k } ^ { j } = O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + 2 c ^ { - 5 } \Big ( \partial _ { j } V _ { k } [ 3 ] - \partial _ { k } V _ { j } [ 3 ] + \partial _ { t } W _ { j k } [ 1 ] } } \\ { { \mathrm {  ~ \Gamma ~ } - \delta _ { j k } \partial _ { t } V [ 3 ] \Big ) + O ( c ^ { - 6 } ) , } } \\ { { \mathrm {  ~ \Gamma ~ } \Gamma _ { k n } ^ { j } = O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + O ( c ^ { - 6 } ) . } } \end{array}
$$

We observe that since the $c ^ { - 5 }$ term in $g _ { 0 0 }$ depends on time only, there is no contribution at order $c ^ { - 3 }$ in $\Gamma _ { 0 0 } ^ { j }$ . This is connected to the fact, discussed back in Sec. 7.3.5, that the $c ^ { - 5 }$ term in $g _ { 0 0 }$ can be removed by the coordinate transformation

$$
t = t ^ { \prime } - \frac { 2 G } { 3 c ^ { 5 } } \ddot { I } ^ { k k } ( t ^ { \prime } ) + { \cal O } ( c ^ { - 7 } ) ,
$$

so that it has no physical effect on the motion of matter. This removal works only at order $c ^ { - 5 }$ ; the transformation generates corrections at order $c ^ { - 7 }$ that depend on $\ddot { I } ^ { \ast k }$ , as can be expected from the presence of $- 8 V [ 3 ] \partial ^ { j } U$ in $\Gamma _ { 0 0 } ^ { j }$ . Similarly, because the $c ^ { - 5 }$ term in $g _ { j k }$ depends on time only, there is no contribution at order $c ^ { - 5 }$ in the purely spatial components of the Christoffel symbols.

We next turn to the matter variables, which were introduced in Sec. 12.5.3. We re-express Eq. (12.112) as

$$
\gamma = 1 + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + 4 c ^ { - 5 } V [ 3 ] + O ( c ^ { - 6 } )
$$

and observe that the terms of order $c ^ { - 5 }$ cancel out in

$$
\gamma \sqrt { - g } = 1 + { \cal O } ( c ^ { - 2 } ) + { \cal O } ( c ^ { - 4 } ) + { \cal O } ( c ^ { - 6 } ) .
$$

From Eq. (12.110) we obtain

$$
\begin{array} { l c r } { { c ^ { - 2 } \sqrt { - g } T ^ { 0 0 } = \gamma \rho ^ { * } + { \cal O } ( c ^ { - 2 } ) + { \cal O } ( c ^ { - 4 } ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { c ^ { - 1 } \sqrt { - g } T ^ { 0 j } = \gamma \rho ^ { * } v ^ { j } + { \cal O } ( c ^ { - 2 } ) + { \cal O } ( c ^ { - 4 } ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \sqrt { - g } T ^ { j k } = \gamma \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + { \cal O } ( c ^ { - 2 } ) + { \cal O } ( c ^ { - 4 } ) } } \\ { { \qquad - 4 c ^ { - 5 } W ^ { j k } [ 1 ] p + { \cal O } ( c ^ { - 6 } ) . } } \end{array}
$$

# 12.6.2 Radiation-reaction force density

The post-Newtonian generalization of Euler’s equation is obtained by invoking the local statement of momentum conservation, as expressed by Eq. (8.111):

$$
\begin{array} { l } { { 0 = c ^ { - 1 } \partial _ { t } \bigl ( \sqrt { - g } T ^ { 0 j } \bigr ) + \partial _ { k } \bigl ( \sqrt { - g } T ^ { j k } \bigr ) } } \\ { { \qquad + \Gamma _ { 0 0 } ^ { j } \bigl ( \sqrt { - g } T ^ { 0 0 } \bigr ) + 2 \Gamma _ { 0 k } ^ { j } \bigl ( \sqrt { - g } T ^ { 0 k } \bigr ) + \Gamma _ { k n } ^ { j } \bigl ( \sqrt { - g } T ^ { k n } \bigr ) . } } \end{array}
$$

After substitution of Eqs. (12.129) and (12.133) and simplification, we obtain

$$
\begin{array} { c } { { 0 = \partial _ { t } \bigl ( \rho ^ { * } v ^ { j } \bigr ) + \partial _ { k } \bigl ( \rho ^ { * } v ^ { j } v ^ { k } \bigr ) - \rho ^ { * } \partial _ { j } U + \partial _ { j } p + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) } } \\ { { - c ^ { - 5 } f ^ { j } [ 5 ] + O ( c ^ { - 6 } ) , } } \end{array}
$$

where

$$
\begin{array} { r } { f ^ { j } [ 5 ] : = \rho ^ { * } \partial _ { j } \big ( V [ 5 ] + W [ 3 ] \big ) + 4 \rho ^ { * } \partial _ { t } V ^ { j } [ 3 ] - 4 \rho ^ { * } v ^ { k } \big ( \partial _ { j } V _ { k } [ 3 ] - \partial _ { k } V _ { j } [ 3 ] + \partial _ { t } W _ { j k } [ 1 ] \big ) } \\ { - 4 \rho ^ { * } W ^ { j k } [ 1 ] \partial _ { k } U - 8 \rho ^ { * } V [ 3 ] \partial _ { j } U + 4 W ^ { j k } [ 1 ] \partial _ { k } p + 4 V [ 3 ] \partial _ { j } p . \qquad ( 1 2 . 1 3 6 \rho ^ { * } \partial _ { t } V ^ { j k } ) } \end{array}
$$

We next involve the continuity equation $\partial _ { t } \rho ^ { * } + \partial _ { k } ( \rho ^ { * } v ^ { k } ) = 0$ and insert the radiationreaction potentials listed in Box 12.3. The end result is the Euler equation of Eq. (12.127), with $f ^ { j } [ \mathrm { r r } ] = c ^ { - 5 } f ^ { j } [ 5 ] + O ( c ^ { - 7 } )$ .

Our final expression for the radiation-reaction force density is

$$
\begin{array} { l } { { \displaystyle f ^ { j } [ \mathrm { r r } ] = \frac { G } { c ^ { 5 } } \bigg ( - \rho ^ { * } \ddot { I } ^ { p q } \partial _ { j p q } X + 2 \rho ^ { * } \ddot { I } ^ { j k } \partial _ { k } U + \frac { 4 } { 3 } \rho ^ { * } \ddot { I } _ { p p } \partial _ { j } U - 2 \dddot { I } ^ { j k } \partial _ { k } p - \frac { 2 } { 3 } \dddot { I } ^ { p p } \partial _ { j } p } } \\ { { \displaystyle \qquad + 2 \rho ^ { * } \ddot { I } ^ { j k } v _ { k } + \frac { 3 } { 5 } \rho ^ { * } \ddot { I } ^ { j k } x ^ { k } - \frac { 1 } { 5 } \rho ^ { * } \ddot { I } ^ { p p } x ^ { j } - \frac { 2 } { 1 5 } \rho ^ { * } \ddot { I } ^ { j p p } - \frac { 2 } { 3 } \rho ^ { * } \ddot { I } ^ { ( j p p } \bigg ) } } \\   \displaystyle \qquad + O ( c ^ { - 7 } ) . \qquad \qquad \quad ( 1 2 . 1 3 \ \end{array}
$$

The various multipole moments that appear in this expression are defined in Box 12.3.

# 12.6.3 Energy balance

Before we apply the radiation-reaction force of Eq. (12.137) to a system of well-separated bodies, we verify that it leads to the expressions of energy, momentum, and angularmomentum balance that were stated back in Sec. 12.2. We begin with energy balance. According to Eq. (12.31), the total energy $E$ of the fluid distribution should vary in time according to

$$
\frac { d E } { d t } = - \mathcal { P } = - \frac { G } { 5 c ^ { 5 } } \dddot { I } ^ { \langle j k \rangle } \ddot { I } ^ { \langle j k \rangle } + { \cal O } ( c ^ { - 7 } ) ,
$$

where the expression for the energy flux $\mathcal { P }$ has been copied from Sec. 12.3.2.

For our purposes here it is sufficient to import an expression for the total energy $E$ that is accurate to the leading, Newtonian order, but it is still necessary to recognize that $E$ also contains terms at 1pn, 2pn, and $2 . 5 \mathrm { { p N } }$ orders. The Newtonian term was computed in Sec. 8.4.5, and according to Eq. (8.134), we have that

$$
E = { \mathcal { T } } + \Omega + E _ { \mathrm { i n t } } + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + c ^ { - 5 } E [ 5 ] + O ( c ^ { - 6 } ) ,
$$

where $\begin{array} { r } { \mathcal { T } : = \frac { 1 } { 2 } \int \rho ^ { * } v ^ { 2 } d ^ { 3 } x } \end{array}$ is the fluid’s total kinetic energy, $\begin{array} { r } { \Omega : = - \frac { 1 } { 2 } \int \rho ^ { * } U d ^ { 3 } x } \end{array}$ its gravitational potential energy, and $\begin{array} { r } { E _ { \mathrm { i n t } } : = \int \rho ^ { \ast } \Pi d ^ { 3 } x } \end{array}$ its total internal energy. The 1pn and $2 \mathrm { P N }$ terms are not required in this discussion, but the $2 . 5 \mathrm { { P N } }$ term is important and its precise identity will be revealed in due course.

We differentiate each term in Eq. (12.139) with respect to time. For the kinetic energy we get $\begin{array} { r } { d \mathcal { T } / d t = \int \rho ^ { * } v _ { j } ( d v ^ { j } / d t ) d ^ { 3 } x } \end{array}$ , in which we substitute the Euler equation of Eq. (12.127); the contribution at order $c ^ { - 5 }$ is $\textstyle \int v _ { j } f ^ { j } [ \operatorname { r r } ] d ^ { 3 } x$ , the rate at which the radiation-reaction force does work on the fluid. For the potential energy we get that $d \Omega / d t$ is given exactly by Eq. (12.144d) below and gives no contribution at order $c ^ { - 5 }$ . For the internal energy we have that $\begin{array} { r } { d E _ { \mathrm { i n t } } / d t = \int \rho ^ { * } ( d \Pi / d t ) d ^ { 3 } x } \end{array}$ , in which we insert the exact statement of the first law of thermodynamics, as stated back in Sec. 8.4; we have that $d \Pi / d t = ( p / \rho ^ { 2 } ) d \rho / d t$ , where $\rho$ is the fluid’s proper-mass density. Because $\rho$ differs from $\rho ^ { * }$ by a factor $\gamma \sqrt { - g }$ that contains no term of order $c ^ { - 5 }$ – refer to Eq. (12.132) – we find that $d E _ { \mathrm { i n t } } / d t$ makes no contribution at $2 . 5 \mathrm { { p N } }$ order. Finally, observing that all $c ^ { 0 } , c ^ { - 2 }$ , and $c ^ { - 4 }$ terms in $E$ are conserved by virtue of the conservative dynamics at 2pn order, we are left with

$$
\int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x + { \frac { d } { d t } } \Big ( c ^ { - 5 } E [ 5 ] \Big ) = - { \frac { G } { 5 c ^ { 5 } } } \ddot { I } ^ { \langle j k \rangle } \ddot { I } ^ { \langle j k \rangle } + { \cal O } ( c ^ { - 7 } )
$$

as a precise statement of energy balance. This equation states that up to an overall change in total energy at $2 . 5 \mathrm { { p N } }$ order, the work done by the radiation-reaction force is equal to the energy radiated by gravitational waves.

In situations in which the Newtonian dynamics of the system is periodic, or when the evolution begins and ends in a static state, Eq. (12.140) can be averaged over time, and the resulting coarse-grained statement of energy balance no longer involves $E [ 5 ]$ . In this formulation we would write

$$
\Big \langle \int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x \Big \rangle = - \frac { G } { 5 c ^ { 5 } } \Big \langle \ddot { I } ^ { \langle j k \rangle } \ddot { I } _ { \langle j k \rangle } \Big \rangle + { \cal O } ( c ^ { - 7 } ) ,
$$

with the angular brackets indicating the averaging procedure. In this coarse-grained statement we recover the expected equality between work done and radiated energy. This statement is obviously less general than the fine-grained statement of Eq. (12.140), and is subjected to the assumption that the initial and final values of $E [ 5 ]$ must be equal.

Before we proceed with the derivation of Eq. (12.140) and the determination of $E [ 5 ]$ we re-introduce the tensorial generalizations of $\tau$ and $\Omega$ ,

$$
\begin{array} { l } { \displaystyle \mathcal { T } ^ { j k } : = \frac 1 2 \int \rho ^ { * } v ^ { j } v ^ { k } d ^ { 3 } x , } \\ { \displaystyle \Omega ^ { j k } : = - \frac 1 2 G \int \rho ^ { * } \rho ^ { * \prime } \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x , } \end{array}
$$

which were first encountered back in Sec. 1.4.3. In terms of these we have that $\mathcal { T } = \delta _ { j k } \mathcal { T } ^ { j k }$ and $\Omega = \delta _ { j k } \Omega ^ { j k }$ . These quantities are involved in a number of helpful identities, including the familiar virial theorem

$$
\frac { 1 } { 2 } \ddot { I } ^ { j k } = 2 \mathcal { T } ^ { j k } + \Omega ^ { j k } + P \delta ^ { j k } ,
$$

with $\textstyle P : = \int p d ^ { 3 } x$ denoting the integrated pressure. Other identities include

$$
\begin{array} { c } { { \dot { \eta } _ { j k } = \displaystyle { \dot { \cal T } _ { j } } { } ^ { * } v _ { ( j } \partial _ { k ) } U d ^ { 3 } x - \displaystyle { \int v _ { ( j } \partial _ { k ) } p d ^ { 3 } x + { \cal O } ( c ^ { - 2 } ) } , } } \\ { { \dot { \Omega } _ { j k } - \dot { \Omega } \delta _ { j k } = \displaystyle { \int \rho ^ { * } v ^ { p } \partial _ { p j k } { \cal X } d ^ { 3 } x } , } } \\ { { \dot { \cal T } = \displaystyle { \int \rho ^ { * } v ^ { j } \partial _ { j } U d ^ { 3 } x - \int v ^ { j } \partial _ { j } p d ^ { 3 } x + { \cal O } ( c ^ { - 2 } ) } , } } \\ { { \dot { \Omega } = - \displaystyle { \int \rho ^ { * } v ^ { j } \partial _ { j } U d ^ { 3 } x } . } } \end{array}
$$

These identities are similar to those encountered previously in Sec. 8.4.4, and it is a simple matter to establish them. For example, Eq. (12.144a) follows directly from the definition of $\mathcal { T } ^ { j k }$ and involvement of Euler’s equation. Equation (12.144c) is obtained by taking the trace of Eq. (12.144a). The derivation of Eq. (12.144b) is more involved, but Eq. (12.144d) follows by taking its trace.

To establish Eq. (12.144b) we begin with the definition of the superpotential, $X =$ $\begin{array} { r l } { G \int \rho ^ { * \prime } | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } } \end{array}$ , from which we obtain

$$
\begin{array} { l } { { \displaystyle \int \rho ^ { * } v ^ { p } \partial _ { p j k } X d ^ { 3 } x = G \int \rho ^ { * } \rho ^ { * } v ^ { p } \partial _ { p j k } | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } d ^ { 3 } x } } \\ { { \displaystyle \qquad = G \int \rho ^ { * } \rho ^ { * } v ^ { p } \partial _ { p ^ { \prime } j k } | x ^ { \prime } - x | d ^ { 3 } x d ^ { 3 } x ^ { \prime } } } \\ { { \displaystyle \qquad = - G \int \rho ^ { * } \rho ^ { * } v ^ { p } \partial _ { p j k } | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } d ^ { 3 } x } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } G \int \rho ^ { * } \rho ^ { * } ( v - v ^ { \prime } ) ^ { p } \partial _ { p j k } | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } d ^ { 3 } x } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } G \frac { d } { d t } \int \rho ^ { * } \rho ^ { * } \partial _ { b } | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } d ^ { 3 } x } } .  \end{array}
$$

We swap the identities of the integration variables to go from the first to the second line, and to go to the third line we observe that $\partial _ { j ^ { \prime } } | { \pmb x } - { \pmb x } ^ { \prime } | = - \partial _ { j } | { \pmb x } - { \pmb x } ^ { \prime } |$ . We symmetrize the expressions in the fourth line, and in the fifth line we invoke an integral identity derived in $\mathrm { B o x } 8 . 4$ . The final result of Eq. (12.144b) follows after evaluating the remaining derivatives.

Returning to Eq. (12.140), we insert the force density of Eq. (12.137) and involve the identities of Eq. (12.144) to evaluate the integrals. We simplify our expressions by setting $\begin{array} { r } { \int \rho ^ { * } v ^ { j } d ^ { 3 } x + O ( c ^ { - 2 } ) = P ^ { j } = 0 } \end{array}$ , and obtain

$$
\begin{array} { l } { { { \displaystyle { \frac { c ^ { 5 } } { G } } \int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x = - \ddot { T } _ { j k } \bigl ( 2 \dot { \mathcal { T } } ^ { j k } + \dot { \Omega } ^ { j k } \bigr ) + { \frac { 1 } { 3 } } \ddot { T } _ { p p } \bigl ( 2 \dot { \mathcal { T } } + \dot { \Omega } \bigr ) } } } \\ { { { } + { \frac { 3 } { 1 0 } } { I } ^ { ( j k } \dot { I } ^ { j k } - { \frac { 1 } { 1 0 } } \overset { ( s ) } { I } ^ { p p } \dot { I } ^ { p p } + 4 { \frac { d } { d t } } \Bigl ( \ddot { I } ^ { j k } { T } ^ { j k } \Bigr ) } } \end{array}
$$

for the rate of work done. With the virial theorem of Eq. (12.143) we can express this as

$$
\begin{array} { l } { { { \displaystyle \frac { c ^ { 5 } } { G } \int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x = - \frac { 1 } { 2 } \dddot { I } ^ { j k } \ddot { I } ^ { j k } + \frac { 1 } { 6 } \dddot { I } ^ { p p } \ddot { I } ^ { p p } + \frac { 3 } { 1 0 } \dddot { I } ^ { j k } \dot { I } ^ { j k } - \frac { 1 } { 1 0 } \dddot { I } ^ { 0 p } \dot { I } ^ { p p } } } } \\ { { { } } } \\ { { { \displaystyle ~ + 4 \frac { d } { d t } \Bigl ( \ddot { I } ^ { j k } \dot { T } ^ { j k } \Bigr ) } , } } \end{array}
$$

and we simplify it further by distributing the time derivatives. We write, for example,

$$
\stackrel { \scriptscriptstyle ( 5 ) } { I } { } ^ { j k } \dot { I } { } ^ { j k } = \frac { d } { d t } \Big ( \ddot { I } { } ^ { j k } \dot { I } { } ^ { j k } - \ddot { I } { } ^ { j k } \ddot { I } { } ^ { j k } \Big ) + \ddot { I } { } ^ { j k } \ddot { I } { } ^ { j k } ,
$$

and obtain the final expression

$$
\begin{array} { l } { { \displaystyle { \frac { 5 } { \tilde { r } } } \int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x = - \frac { 1 } { 5 } \dddot \cal T ^ { j k } \ddot { \cal T } ^ { j k } + \frac { 1 } { 1 5 } \dddot \cal T ^ { j p p } \ddot { \cal I } ^ { p p } + \frac { d } { d t } \biggl ( 4 \ddot { \cal I } ^ { j k } { \cal T } ^ { j k } + \frac { 3 } { 1 0 } \ddot { \cal I } ^ { j k } \dot { \cal I } ^ { j k } - \frac { 1 } { 1 0 } \stackrel { ( i ) } { \cal I } ^ { p p } \dot { \cal I } ^ { p p } } } \\ { { \displaystyle ~ - \frac { 3 } { 1 0 } \ddot { \cal I } ^ { j k } \ddot { \cal I } ^ { j k } + \frac { 1 } { 1 0 } \ddot { \cal I } ^ { p p } \ddot { \cal I } ^ { p p } \biggr ) } } \end{array}
$$

for the rate at which the radiation-reaction force does work on the fluid.

After simplification achieved by expressing $I ^ { j k }$ in terms of its trace and tracefree pieces, we find that we do indeed recover the energy-balance statement of Eq. (12.140). The

total-derivative term in Eq. (12.149) implies that

$$
c ^ { - 5 } E [ 5 ] = - { \frac { G } { c ^ { 5 } } } { \bigg ( } 4 { \ddot { I } } ^ { j k } { \mathcal { T } } ^ { j k } + { \frac { 3 } { 1 0 } } { \overset { ( 4 ) } { I } } ^ { ( j k ) } { \dot { I } } ^ { ( j k ) } - { \frac { 3 } { 1 0 } } { \ddot { I } } ^ { ( j k ) } { \ddot { I } } ^ { ( j k ) } { \bigg ) }
$$

is the $2 . 5 \mathrm { { P N } }$ contribution to the total energy.

# 12.6.4 Momentum balance

We next turn to momentum balance, and verify that the radiation-reaction force density of Eq. (12.137) is compatible with the statement of Eq. (12.33),

$$
\frac { d P ^ { j } } { d t } = - \mathcal { F } ^ { j } = O ( c ^ { - 7 } ) ;
$$

the scaling of the momentum flux $\mathcal { F } ^ { j }$ with $c ^ { - 7 }$ was obtained in Sec. 12.3.2. The most important observation here is that $P ^ { j }$ is conserved at $2 . 5 \mathrm { { p N } }$ order; radiation reaction acts on the total momentum at $3 . 5 \mathrm { { P N } }$ order.

According to Eq. (8.145), the total momentum of the fluid distribution is given by

$$
P ^ { j } = \int \rho ^ { * } v ^ { j } d ^ { 3 } x + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + c ^ { - 5 } P ^ { j } [ 5 ] + O ( c ^ { - 6 } ) ,
$$

with $c ^ { - 5 } P ^ { j } [ 5 ]$ denoting the contribution at $2 . 5 \mathrm { { P N } }$ order. Differentiation with respect to $t$ and substitution of Eq. (12.127) gives rise to

$$
\int f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x + \frac { d } { d t } \Bigl ( c ^ { - 5 } P ^ { j } [ 5 ] \Bigr ) = O ( c ^ { - 7 } ) ,
$$

which is our precise statement of momentum balance. We must verify that the integrated radiation-reaction force is equal to a total time derivative, and the computation reveals the identity of $P ^ { j } [ 5 ]$ .

To evaluate the integral we require the identities

$$
\begin{array} { c } { { { \displaystyle \int \rho ^ { * } \partial _ { j } U d ^ { 3 } x = 0 , } } } \\ { { { \displaystyle \int \rho ^ { * } \partial _ { j p q } X d ^ { 3 } x = 0 , } } } \\ { { { \displaystyle \int \partial _ { j } p d ^ { 3 } x = 0 . } } } \end{array}
$$

The first is familiar; it was encountered back in Sec. 1.4.3 and then again in Sec. 8.4.4, and its demonstration proceeds by inserting the Newtonian potential and noting that the integrand is odd in the integration variables $\boldsymbol { x }$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . The second identity is new, but it follows after a similar sequence of steps. The third identity also is familiar, and it follows by applying Gauss’s theorem and noting that $p = 0$ on any closed surface that bounds the distribution of matter.

Integration of Eq. (12.137) yields

$$
\int f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x = - \frac { 2 } { 1 5 } \frac { G m } { c ^ { 5 } } \bigg ( \sp { ( 5 ) } _ { I } j p p + 5 \sp { ( 4 ) } _ { J } j p p \bigg ) + O ( c ^ { - 7 } ) ,
$$

where $\begin{array} { r } { m : = \int \rho ^ { * } d ^ { 3 } x } \end{array}$ is the total material mass, and where the multipole moments $I _ { j k n }$ and $J _ { j k n }$ are defined in $\mathrm { B o x } \ 1 2 . 3$ . To arrive at this expression we have used the fact that since $P ^ { j }$ is conserved at $2 . 5 \mathrm { { p N } }$ order, we may work in the center-of-mass frame and set $\textstyle \int \rho ^ { * } x ^ { j } d ^ { 3 } x = O ( c ^ { - 5 } )$ and $\textstyle \int \rho ^ { * } v ^ { j } d ^ { 3 } x = O ( c ^ { - 5 } )$ . The integrated radiation-reaction force is indeed a total time derivative, and from its expression we deduce that the $2 . 5 \mathrm { { p N } }$ contribution to the total momentum is

$$
c ^ { - 5 } P ^ { j } [ 5 ] = { \frac { 2 } { 1 5 } } { \frac { G m } { c ^ { 5 } } } \Big ( _ { I } ^ { ( 4 ) } { j p p } + 5 \dddot { J } ^ { j p p } \Big ) .
$$

We conclude that Eq. (12.137) is indeed compatible with the precise statement of momentum balance.

# 12.6.5 Angular-momentum balance

Finally we examine the statement of angular-momentum balance, which is provided by Eq. (12.35),

$$
\frac { d J ^ { j k } } { d t } = - \Im ^ { j k } = - \frac { 2 G } { 5 c ^ { 5 } } \Big ( \ddot { I } ^ { j p } \dddot { I } ^ { k p } - \ddot { I } ^ { k p } \dddot { I } ^ { \dot { J } P } \Big ) + { \cal O } ( c ^ { - 7 } ) ,
$$

where the expression for the angular-momentum flux $\mathcal { T } ^ { j k }$ has been copied from Sec. 12.3.2; it is easy to show that the result displayed here is equivalent to that of Eq. (12.68c), in spite of the fact that our expression omits the STF projection of the quadrupole-moment tensor. The total angular-momentum tensor of the fluid distribution is given by

$$
J ^ { j k } = \int \rho ^ { * } \left( x ^ { j } v ^ { k } - v ^ { j } x ^ { k } \right) d ^ { 3 } x + O ( c ^ { - 2 } ) + O ( c ^ { - 4 } ) + c ^ { - 5 } J ^ { j k } [ 5 ] + O ( c ^ { - 6 } ) ,
$$

with $c ^ { - 5 } J ^ { j k } [ 5 ]$ denoting the contribution at $2 . 5 \mathrm { { p N } }$ order. The precise statement of angularmomentum balance is

$$
\int \left( x ^ { j } f ^ { k } [ \mathrm { r r } ] - x ^ { k } f ^ { j } [ \mathrm { r r } ] \right) d ^ { 3 } x + { \frac { d } { d t } } { \Big ( } c ^ { - 5 } J ^ { j k } [ 5 ] { \Big ) } = - { \frac { 2 G } { 5 c ^ { 5 } } } { \Big ( } { \ddot { I } } ^ { j p } { \ddot { I } } ^ { k p } - { \ddot { I } } ^ { k p } { \ddot { I } } ^ { j p } { \Big ) } + O ( c ^ { - 7 } )
$$

and in this we must substitute Eq. (12.137).

To evaluate the integral on the left-hand side we require the identities

$$
\begin{array} { c } { { { \displaystyle \int \rho ^ { * } x ^ { j } \partial _ { k } U d ^ { 3 } x = \Omega _ { j k } , } } } \\ { { { \displaystyle \int \rho ^ { * } x ^ { j } \partial _ { k p q } X d ^ { 3 } x = \Omega _ { j k } \delta _ { p q } + \Omega _ { j p } \delta _ { k q } + \Omega _ { j q } \delta _ { k p } - 3 \Omega _ { j k p q } } , } } \\ { { { \displaystyle \int \rho ^ { * } \partial _ { k } p d ^ { 3 } x = - \delta _ { j k } P } , } } \\ { { { \displaystyle \int \rho ^ { * } x ^ { j } v ^ { k } d ^ { 3 } x = \frac { 1 } { 2 } ( { \dot { I } } ^ { j k } + J ^ { j k } ) + { \cal O } ( c ^ { - 2 } ) , } } } \end{array}
$$

in which $\Omega _ { j k }$ is the tensorial quantity defined by Eq. (12.142),

$$
\Omega _ { j k p q } : = - \frac { 1 } { 2 } G \int \rho ^ { * } \rho ^ { * \prime } \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } ( x - x ^ { \prime } ) ^ { p } ( x - x ^ { \prime } ) ^ { q } } { | x - x ^ { \prime } | ^ { 5 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x ,
$$

and $\textstyle P : = \int p d ^ { 3 } x$ is the integrated pressure. The first identity is familiar from the proof of the virial theorem presented back in Sec. 1.4.3, and the second follows after a similar sequence of steps. The third identity is an immediate consequence of integration by parts, and the fourth follows directly from the definitions of $I ^ { j k }$ and $J ^ { j k }$ .

After substitution of Eq. (12.137) and involvement of the identities we obtain

$$
\int x ^ { j } f ^ { k } [ \mathrm { r r } ] d ^ { 3 } x = \frac { G } { c ^ { 5 } } \bigg ( \frac { 3 } { 5 } I ^ { j p } I ^ { 5 p } + \dot { I } ^ { j p } I ^ { 4 p } + J ^ { j p } I ^ { 4 p } \bigg ) ,
$$

up to a number of terms that are symmetric in the pair of indices $j k$ . This becomes

$$
\int x ^ { j } f ^ { k } [ \mathrm { r r } ] d ^ { 3 } x = - { \frac { 2 G } { 5 c ^ { 5 } } } \ddot { I } ^ { j k } \ddot { \bar { I } } ^ { k p } + { \frac { G } { 5 c ^ { 5 } } } { \frac { d } { d t } } \bigg ( 3 I ^ { j p } \dot { I } ^ { k p } + 2 \dot { I } ^ { j p } \ddot { I } ^ { k p } + 5 J ^ { j p } \ddot { I } ^ { k p } \bigg )
$$

after distributing the time derivatives. Comparing with Eq. (12.159), we conclude that the statement of angular-momentum balance is indeed satisfied, and deduce that the $2 . 5 \mathrm { { p N } }$ contribution to the total angular-momentum tensor is

$$
\begin{array} { l } { { c ^ { - 5 } J ^ { j k } [ 5 ] = - { \displaystyle \frac { G } { 5 c ^ { 5 } } } \Big [ 3 \big ( I ^ { j p } \ddot { I } ^ { 4 p } - I ^ { k p } \ddot { I } ^ { 4 p } \big ) + 2 \big ( \dot { I } ^ { j p } \ddot { I } ^ { k p } - \dot { I } ^ { k p } \ddot { I } ^ { \cdots { p } p } \big ) } } \\ { { \qquad + 5 \big ( J ^ { j p } \ddot { I } ^ { \ast p } - J ^ { k p } \ddot { I } ^ { \ast p } \big ) \Big ] . } } \end{array}
$$

In this expression $J ^ { j k }$ stands for the Newtonian piece of the angular-momentum tensor, obtained from Eq. (12.158) by ignoring all contributions at higher post-Newtonian orders.

# 12.7 Radiation reaction of $N$ -body systems

We now specialize the results of the preceding section to a case in which the fluid distribution consists of $N$ well-separated bodies. We wish to calculate the radiation-reaction force acting on the center-of-mass of each body, and in order to achieve this we shall exploit the techniques developed back in Chapter 9.

# 12.7.1 N bodies

As in Sec. 9.1 we assign to each body a label $A = 1 , 2 , \dotsc , N$ , and for each body we define the center-of-mass variables

$$
\begin{array} { l } { { { \displaystyle m _ { \cal A } : = \int _ { \cal A } \rho ^ { * } d ^ { 3 } x , } } } \\ { { { \displaystyle r _ { \cal A } : = \frac { 1 } { m _ { \cal A } } \int _ { \cal A } \rho ^ { * } x d ^ { 3 } x , } } } \\ { { { \displaystyle v _ { \cal A } : = \frac { 1 } { m _ { \cal A } } \int _ { \cal A } \rho ^ { * } v d ^ { 3 } x , } } } \\ { { { \displaystyle a _ { \cal A } : = \frac { 1 } { m _ { \cal A } } \int _ { \cal A } \rho ^ { * } \frac { d v } { d t } d ^ { 3 } x ; } } } \end{array}
$$

the domain of integration is the region of space occupied by body $A$ . We calculate the radiation-reaction force $F _ { A } [ \mathrm { r r } ]$ acting on body $A$ by inserting Eq. (12.127) within $\pmb { a } _ { A }$ ; we find

$$
F _ { A } [ \mathrm { r r } ] = m _ { A } \pmb { a } _ { A } [ \mathrm { r r } ] = \int _ { A } f [ \mathrm { r r } ] d ^ { 3 } x ,
$$

in which $f [ \mathrm { r r } ]$ is the radiation-reaction force density of Eq. (12.137).

To evaluate this we proceed as in Sec. 9.1.5 and decompose the Newtonian potential $U$ and the post-Newtonian superpotential $X$ into internal and external pieces. We have, for example, $U = U _ { A } + U _ { \lnot A }$ , with

$$
U _ { A } = G \int _ { A } { \frac { \rho ^ { * } ( t , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } } d ^ { 3 } x ^ { \prime }
$$

denoting the internal piece of the Newtonian potential, and

$$
U _ { \neg { A } } = \sum _ { B \not = A } G \int _ { B } \frac { \rho ^ { * } ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime }
$$

denoting its external piece. As in Sec. 9.3 we exploit the assumption that the bodies are well separated to express each external potential as a Taylor expansion about the center-of-mass $r _ { A }$ ; we ignore the multipole structure of the body and retain only the leading term in the expansion. The internal potentials require no approximation, and for these we invoke the identities of Eq. (12.154),

$$
\begin{array} { r } { \displaystyle \int _ { A } \rho ^ { * } \partial _ { j } U _ { A } d ^ { 3 } x = 0 , } \\ { \displaystyle \int _ { A } \rho ^ { * } \partial _ { j p q } X _ { A } d ^ { 3 } x = 0 , } \\ { \displaystyle \int _ { A } \partial _ { j } p d ^ { 3 } x = 0 , } \end{array}
$$

which imply that the internal potentials and the pressure make no contribution to the radiation-reaction force.

Following through with the computations, we quickly obtain

$$
\begin{array} { l } { { a _ { \cal A } ^ { j } [ \mathrm { r r } ] = { \displaystyle \frac { G } { c ^ { 5 } } } \biggl ( - \ddot { \cal I } ^ { p q } \partial _ { j p q } X _ { \neg { \cal A } } + 2 \ddot { \cal I } ^ { j k } \partial _ { k } U _ { \neg { \cal A } } + { \displaystyle \frac { 4 } { 3 } } \ddot { \cal I } ^ { p p } \partial _ { j } U _ { \neg { \cal A } } + 2 \stackrel { ( \mathrm { 4 } ) } { \cal I } ^ { j k } v _ { A } ^ { k } } } \\ { { \qquad + { \displaystyle \frac { 3 } { 5 } } \stackrel { ( 5 ) } { \cal I } ^ { j k } r _ { A } ^ { k } - { \displaystyle \frac { 1 } { 5 } } \stackrel { ( 5 ) } { \cal I } ^ { p p } r _ { A } ^ { j } - { \displaystyle \frac { 2 } { 1 5 } } \stackrel { ( 5 ) } { \cal I } ^ { j p p } - { \displaystyle \frac { 2 } { 3 } } \stackrel { ( \mathrm { 4 } ) } { \cal J } ^ { j p p } \biggr ) + { \cal O } ( c ^ { - 7 } ) , } } \end{array}
$$

in which it is understood that the external potentials are evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ after differentiation. For a more concrete expression we must evaluate the external potentials. These manipulations are familiar from Sec. 9.3.4, and we arrive at

$$
\begin{array} { c } { { \displaystyle \partial _ { j } U _ { \neg A } = - \sum _ { B \not = A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } n _ { { } _ { A B } } ^ { j } , } } \\ { { \partial _ { j p q } X _ { \neg A } = - \displaystyle \sum _ { B \not = A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } \left( n _ { A B } ^ { j } \delta _ { p q } + n _ { A B } ^ { p } \delta _ { j q } + n _ { A B } ^ { q } \delta _ { j p } - 3 n _ { A B } ^ { j } n _ { A B } ^ { p } n _ { A B } ^ { q } \right) , } } \end{array}
$$

in which $r _ { A B } : = r _ { A } - r _ { B }$ , $r _ { A B } : = | r _ { A B } |$ , and $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B }$ ; we take the liberty of expressing the material mass $m _ { A }$ in terms of the total mass-energy $M _ { A }$ of Eq. (9.23), noting that the difference is of order $c ^ { - 2 }$ and therefore affects the radiation-reaction force at order $c ^ { - 7 }$ only.

Making the substitutions returns our final expression for the radiation-reaction force (per unit mass) acting on body $A$ :

$$
\begin{array} { r } { a _ { A } ^ { j } [ \mathrm { r r } ] = \displaystyle \frac { G } { c ^ {  { \bar { s } } } } \bigg ( - 3 \overleftrightarrow { I } ^ { p q } \sum _ { B \not = A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } n _ { A B } ^ { j } n _ { A B } ^ { p } n _ { A B } ^ { q } - \frac { 1 } { 3 } \overleftrightarrow { I } ^ { p p } \sum _ { B \not = A } \frac { G M _ { B } } { r _ { A B } ^ { 2 } } n _ { A B } ^ { j } } \\ { + 2 _ { \vphantom { \frac { ( 4 ) } { ( } } J ^ { 4 ) } } ^ { ( 4 ) k } v _ { A } ^ { k } + \frac { 3 } { 5 } \overbrace { I ^ { \langle j k \rangle } } ^ { 4 \rangle } r _ { A } ^ { k } - \frac { 2 } { 1 5 } \overbrace { I ^ { j p p } } ^ { ( 5 ) } - \frac { 2 } { 3 } \overleftrightarrow { J } ^ { ( j p p } \bigg ) + O ( c ^ { - 7 } ) . } \end{array}
$$

To complete the evaluation of $\pmb { a } _ { A } [ \mathrm { r r } ]$ we should calculate the time derivatives of all the multipole moments that occur in Eq. (12.172). Because the end result is long and unwieldy, we postpone the pursuit of these details until we specialize our discussion to a two-body system.

# 12.7.2 Two bodies

We next apply the general results of the preceding subsection to the case $N = 2$ . Because the total momentum $P$ of the system is conserved at order $c ^ { - 5 }$ , we may set it equal to zero and work in the barycentric frame in which $r _ { 1 } = ( M _ { 2 } / m ) r + O ( c ^ { - 2 } )$ and $r _ { 2 } =$ $- ( M _ { 1 } / m ) \pmb { r } + O ( c ^ { - 2 } ) ,$ , where $m : = M _ { 1 } + M _ { 2 }$ and $r : = r _ { 1 } - r _ { 2 }$ . Equation (12.172) then provides the radiation-reaction acceleration of the relative orbit, $\pmb { a } [ \mathrm { r r } ] : = \pmb { a } _ { 1 } [ \mathrm { r r } ] - \pmb { a } _ { 2 } [ \mathrm { r r } ]$ ; we get

$$
a ^ { j } [ \mathrm { r r } ] = \frac { G } { c ^ { 5 } } \biggl [ - \frac { G m } { r ^ { 2 } } \Bigl ( 3 \ddot { I } ^ { p q } n ^ { p } n ^ { q } + \frac { 1 } { 3 } \ddot { I } ^ { p p } \Bigr ) n ^ { j } + 2 ^ { ( 4 ) } n ^ { k } v ^ { k } + \frac { 3 } { 5 } \ddot { I } ^ { \langle j k \rangle } r ^ { k } \biggr ] + { \cal O } ( c ^ { - 7 } ) ,
$$

where $r : = | r |$ and ${ \pmb n } : = { \pmb r } / r$ . We observe that the multipole moments $I _ { j p p }$ and $J _ { j p p }$ no longer appear in this expression; as we saw back in Sec. 12.6.4, their role is limited to providing a contribution to the total momentum at $2 . 5 \mathrm { { P N } }$ order.

The mass quadrupole moment is $I ^ { j k } = \eta m r ^ { j } r ^ { k }$ , where $\eta : = { M _ { 1 } M _ { 2 } } / { m ^ { 2 } }$ is the symmetric mass ratio, and to evaluate its derivatives we rely on the Keplerian dynamics reviewed in Sec. 3.2. From the Newtonian equation of motion $\pmb { a } = - G m \pmb { n } / r ^ { 2 }$ we deduce that $v \dot { v } =$ $- G m { \dot { r } } / r ^ { 2 }$ and $r \ddot { r } = v ^ { 2 } - { \dot { r } } ^ { 2 } - G m / r$ , up to corrections of order $c ^ { - 2 }$ , and a straightforward computation reveals that

$$
\begin{array} { c } { { \tilde { I } ^ { j k } = - 2 \eta m \displaystyle \frac { G m } { r ^ { 2 } } \Big [ 2 \Big ( n ^ { j } v ^ { k } + v ^ { j } n ^ { k } \Big ) - 3 \dot { r } n ^ { j } n ^ { k } \Big ] , } } \\ { { \overset { ( a ) } { \underset { J ^ { j k } } { = } } = - 2 \eta m \displaystyle \frac { G m } { r ^ { 3 } } \Big [ - 9 \dot { r } \Big ( n ^ { j } v ^ { k } + v ^ { j } n ^ { k } \Big ) + 4 v ^ { j } v ^ { k } } } \\ { { + \left( 1 5 \dot { r } ^ { 2 } - 3 v ^ { 2 } - G m / r \right) n ^ { j } n ^ { k } \Big ] , } } \\ { { \overset { ( b ) } { \underset { J ^ { j k } } { = } } = - 2 \eta m \displaystyle \frac { G m } { r ^ { 4 } } \Big [ 4 \Big ( 1 5 \dot { r } ^ { 2 } - 3 v ^ { 2 } + G m / r \Big ) \Big ( n ^ { j } v ^ { k } + v ^ { j } n ^ { k } \Big ) } } \\ { { - 3 0 \dot { r } v ^ { j } v ^ { k } + 1 5 \dot { r } \Big ( 3 v ^ { 2 } - 7 \dot { r } ^ { 2 } \Big ) n ^ { j } n ^ { k } \Big ] . } } \end{array}
$$

Making the substitutions in Eq. (12.173), we eventually arrive at our final expression for the radiation-reaction acceleration:

$$
a [ \mathrm { r r } ] = \frac { 8 } { 5 } \eta \frac { ( G m ) ^ { 2 } } { c ^ { 5 } r ^ { 3 } } \biggl [ \biggl ( 3 v ^ { 2 } + \frac { 1 7 } { 3 } \frac { G m } { r } \biggr ) \dot { r } n - \biggl ( v ^ { 2 } + 3 \frac { G m } { r } \biggr ) v \biggr ] .
$$

We return to this expression in Sec. 12.9, when we examine the orbital motion of a binary system under the action of the radiation-reaction force.

# 12.8 Radiation reaction in alternative gauges

The radiation-reaction force density of Eq. (12.137), and the body forces of Eqs. (12.172) and (12.175), are expressed in a harmonic coordinate system in which the spacetime metric takes the form of Eq. (12.128). The metric and the resulting expressions for the radiationreaction force appear to be more complicated than they need to be. For example, the metric involves the multipole moments $\mathcal { T } ^ { j k }$ [2], $I ^ { j k n p }$ , and $M ^ { j k n p }$ , but these make no appearance in the radiation-reaction force. As another example, $f ^ { j } [ \mathrm { r r } ]$ involves the multipole moments $I _ { j p p }$ and $J _ { j p p }$ , in spite of the fact that they produce no physical consequences; as we saw, their role is limited to providing a contribution to the total momentum $P$ at $2 . 5 \mathrm { { P N } }$ order. In view of this unnecessary complexity, it is worthwhile to seek coordinate transformations that could simplify the form of the metric and of the radiation-reaction force. To explore this freedom is our purpose in this section. We shall identify two radiation-reaction gauges that offer an optimum of simplicity: the famous Burke–Thorne gauge of Eq. (12.198) below, and the Schafer gauge ¨ of Eq. (12.199).

# 12.8.1 Coordinate transformation

We follow the general framework of Sec. 8.3 and consider a class of coordinate transformations described by

$$
\begin{array} { c } { { t = \bar { t } + c ^ { - 5 } \alpha ( \bar { t } , \bar { x } ^ { j } ) + c ^ { - 7 } \beta ( \bar { t } , \bar { x } ^ { j } ) + O ( c ^ { - 9 } ) , } } \\ { { { } } } \\ { { x ^ { j } = \bar { x } ^ { j } + c ^ { - 5 } h ^ { j } ( \bar { t } , \bar { x } ^ { k } ) + O ( c ^ { - 7 } ) , } } \end{array}
$$

in which $( \bar { t } , \bar { x } ^ { j } )$ are the new coordinates, $( t , x ^ { j } )$ are the old harmonic coordinates, and $\alpha$ , $\beta$ , and $h ^ { j }$ are functions that will be determined in the course of our investigation. The transformation impacts the metric in the way described by Eq. (8.34). When we insert the metric of Eq. (12.128) and read off the terms of relevant orders in the post-Newtonian expansion, we find that the radiation-reaction terms become

$$
\begin{array} { r l } & { \bar { g } _ { 0 0 } [ 5 ] = 2 \bigl ( - \partial _ { \bar { t } } \alpha + 4 V [ 3 ] \bigr ) , } \\ & { \bar { g } _ { 0 0 } [ 7 ] = 2 \bigl ( - \partial _ { \bar { t } } \beta + V [ 5 ] + W [ 3 ] - \Delta U [ 5 ] \bigr ) + 4 U \bigl ( \partial _ { \bar { t } } \alpha - 6 V [ 3 ] \bigr ) , } \\ & { \bar { g } _ { 0 j } [ 4 ] = - \partial _ { \bar { t } } \alpha , } \\ & { \bar { g } _ { 0 j } [ 6 ] = 2 U \partial _ { \bar { t } } \alpha - \partial _ { \bar { t } } \beta + \partial _ { \bar { t } } h _ { j } - 4 V _ { j } [ 3 ] , } \\ & { \bar { g } _ { j k } [ 5 ] = \partial _ { \bar { j } } h _ { k } + \partial _ { \bar { k } } h _ { j } + 4 \bigl ( W _ { j k } [ 1 ] - \delta _ { j k } V [ 3 ] \bigr ) . } \end{array}
$$

The original radiation-reaction potentials are listed in Box 12.3, and

$$
c ^ { - 5 } \Delta U [ 5 ] : = \bar { U } - U
$$

is the difference between the Newtonian potential $\bar { U }$ expressed in terms of the new coordinates $( \bar { t } , \bar { x } ^ { j } )$ and the original Newtonian potential $U$ .

We see from Eqs. (12.177) that the transformation produces a new radiation-reaction term in $\bar { g } _ { 0 j }$ , at order $c ^ { - 4 }$ . This term is undesirable, and we eliminate it by demanding that $\alpha$ be independent of the spatial coordinates $\bar { x } ^ { j }$ . To complete the determination of $\alpha$ we also choose to eliminate $\bar { g } _ { 0 0 } [ 5 ]$ , another undesirable term at $1 . 5 \mathrm { { P N } }$ order. This can be achieved by setting $\partial _ { \bar { t } } \alpha = 4 V [ 3 ]$ , or

$$
\alpha ( \bar { t } ) = - \frac { 2 } { 3 } G \ddot { I } ^ { p p } .
$$

In this expression the mass quadrupole moment is expressed as a function of the new time variable $\bar { t }$ . The transformation $\begin{array} { r } { t = \bar { t } - \frac { 2 } { 3 } ( G / c ^ { 5 } ) \ddot { I } ^ { p p } ( \bar { t } ) + O ( c ^ { - 7 } ) } \end{array}$ is the one displayed in Eq. (12.130).

To calculate $\Delta U [ 5 ]$ we rely on the discussion of Sec. 8.3.6, in which a “boosted” Newtonian potential $\bar { U }$ was obtained as a result of a post-Galilean transformation of the coordinate system. The original Newtonian potential is

$$
U ( t , \mathbf { x } ) = G \int \frac { \rho ^ { * } ( t , \mathbf { x } ^ { \prime } ) } { | \mathbf { x } - \mathbf { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

where it is understood that the source point $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ is simultaneous with the field point $_ x$ in the harmonic reference frame. The new potential is defined to be

$$
\bar { U } ( \bar { t } , \bar { { \boldsymbol { x } } } ) = G \int \frac { \bar { \rho } ^ { * } ( \bar { t } , \bar { { \boldsymbol { x } } } ^ { \prime } ) } { | \bar { { \boldsymbol { x } } } - \bar { { \boldsymbol { x } } } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } ,
$$

with $\bar { x } ^ { \prime }$ and $\bar { x }$ simultaneous in the new reference frame. Because the relation between $t$ and $\bar { t }$ is independent of the spatial coordinates at order $c ^ { - 5 }$ , simultaneity in one frame implies simultaneity in the other frame, and we find that $( x - x ^ { \prime } ) ^ { j } = ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } + c ^ { - 5 } \Delta h ^ { j }$ , where

$$
\Delta h ^ { j } : = h ^ { j } ( \bar { t } , \bar { x } ) - h ^ { j } ( \bar { t } , \bar { x } ^ { \prime } ) .
$$

Noting also that $\rho ^ { * } d ^ { 3 } x ^ { \prime } = \bar { \rho } ^ { * } d ^ { 3 } \bar { x } ^ { \prime } -$ refer to Eq. (8.92) – we find that the original potential can be expressed as

$$
U = G \int \frac { \bar { \rho } ^ { * } } { | \bar { \boldsymbol { x } } - \bar { \boldsymbol { x } } ^ { \prime } | } \bigg ( 1 - \frac { 1 } { c ^ { 5 } } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } \Delta h _ { j } } { | \bar { \boldsymbol { x } } - \bar { \boldsymbol { x } } ^ { \prime } | ^ { 2 } } \bigg ) d ^ { 3 } \bar { x } ^ { \prime } .
$$

In view of Eq. (12.178), this means that

$$
\Delta U [ 5 ] = G \int \bar { \rho } ^ { * } ( \bar { t } , \bar { x } ^ { \prime } ) \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } \Delta h _ { j } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime }
$$

is our final expression for the change in the Newtonian potential at order $c ^ { - 5 }$ .

# 12.8.2 Two-parameter family of radiation-reaction gauges

To proceed with this exploration of coordinate transformations, we restrict our considerations to radiation-reaction gauges in which

$$
\begin{array} { l } { { \bar { g } _ { 0 j } [ 6 ] = 0 , } } \\ { { \bar { g } _ { j k } [ 5 ] = 2 a G \ddot { I } ^ { \ddot { \langle j k \rangle } } + 2 b \delta _ { j k } G \ddot { I } ^ { \ddot { \langle p p \rangle } } , } } \end{array}
$$

where $a$ and $^ b$ are dimensionless parameters that can be chosen freely. As we shall see, the choice of Eq. (12.185) does not fully exhaust the coordinate freedom, and additional choices will be made to specify the form of $\bar { g } _ { 0 0 } [ 7 ]$ .

According to Eq. (12.177) and the potentials of $\mathrm { B o x } ~ 1 2 . 3$ , to achieve the required form for $\bar { g } _ { j k }$ [5] we need $h ^ { j }$ to be a solution to

$$
\partial _ { \bar { \jmath } } h _ { k } + \partial _ { \bar { k } } h _ { j } = 2 ( 1 + a ) G \ddot { \bar { I } } ^ { \langle j k \rangle } + 2 b \delta _ { j k } G \ddot { \bar { I } } ^ { \langle p p } .
$$

A sufficiently general solution is

$$
\begin{array} { r } { G ^ { - 1 } h _ { j } = f _ { j } + \big [ ( 1 + a ) ^ { \cdots ( j k ) } + b \delta _ { j k } \ddot { I } ^ { p p } \big ] \bar { x } ^ { k } , } \end{array}
$$

in which $f _ { j }$ is an arbitrary function of $\bar { t }$ that will be specified at a later stage. To achieve the required form for $\bar { g } _ { 0 j }$ [6] we need $\beta$ to be a solution to

$$
G ^ { - 1 } \partial _ { \bar { I } } \beta = \dot { f } _ { j } + \frac { 2 } { 9 } I ^ { j p p } + \frac { 4 } { 9 } \ddot { J } ^ { j p p } + \biggl [ \biggl ( \frac { 1 } { 3 } + a \biggr ) \ddot { I } ^ { ( j k ) } + \biggl ( b - \frac { 2 } { 9 } \biggr ) \delta _ { j k } \acute { I } ^ { ( j p p } \biggr ] \bar { x } ^ { k } ,
$$

and in this case we find that

$$
\begin{array} { l } { { G ^ { - 1 } \beta = \gamma + \Big ( \dot { f } _ { j } + \frac { 2 } { 9 } I ^ { \{ j p p } } + \frac { 4 } { 9 } \dddot { J } ^ { j p p } \Big ) \bar { x } ^ { j } }  \\ { { \qquad + \frac { 1 } { 2 } \bigg [ \bigg ( \frac 1 3 + a \bigg ) _ { I } ^ { \{ j \} } { } ^ { k } + \bigg ( b - \frac { 2 } { 9 } \bigg ) \delta _ { j k } { } ^ { ( 4 ) } { } ^ { p p } \bigg ] \bar { x } ^ { j } \bar { x } ^ { k } , } } \end{array}
$$

in which $\gamma$ is an arbitrary function of $\bar { t }$ .

We next incorporate these results in a computation of $\bar { g } _ { 0 0 } [ 7 ]$ . The first step is to insert Eq. (12.187) within Eq. (12.184), which yields

$$
\Delta U [ 5 ] = ( 1 + a ) G \ddot { I } ^ { \langle j k \rangle } \bar { U } _ { j k } + b G \ddot { I } ^ { \langle p p } \bar { U } ,
$$

where

$$
\bar { U } ^ { j k } : = G \int \bar { \rho } ^ { * } \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } d ^ { 3 } \bar { x } ^ { \prime } .
$$

We bring this to its final form of

$$
\Delta U [ 5 ] = - ( 1 + a ) G \ddot { I } ^ { \ddot { \langle j k \rangle } } \partial _ { \bar { \jmath } \bar { k } } \bar { X } + b G \ddot { I } ^ { \ddot { \jmath } p p } \bar { U }
$$

by invoking the identity $\partial _ { j k } X = \delta _ { j k } U - U _ { j k }$ ; here $\bar { X }$ is the superpotential expressed in terms of the new coordinates.

Making the substitutions in Eq. (12.177), we find that $\bar { g } _ { 0 0 } [ 7 ]$ contains a term independent of the spatial coordinates that can be eliminated by choosing

$$
\gamma = - \frac { 2 } { 3 } \ddot { \mathcal { Z } } ^ { p p } [ 2 ] - \frac { 1 } { 1 2 0 } \overset { ( 4 ) } { I } ^ { p p q q } - \frac { 1 } { 9 } \ddot { M } ^ { p p q q } .
$$

It also contains a term linear in $\bar { x } ^ { j }$ that can be eliminated by choosing

$$
f _ { j } = - \frac { 2 } { 1 5 } { \ddot { I } } ^ { { \dot { \jmath } } { p p } } - \frac { 2 } { 3 } { \ddot { J } } ^ { j p p } .
$$

At this stage the coordinate freedom is exhausted, and the resulting expression for $\bar { g } _ { 0 0 } [ 7 ]$ i s

$$
\bar { g } _ { 0 0 } [ 7 ] = 2 a G \ddot { I } ^ { \langle j k \rangle } \partial _ { \bar { j } \bar { k } } \bar { X } - 2 b G \ddot { I } ^ { \because p p } \bar { U } - \biggl [ \biggl ( \frac { 2 } { 5 } + a \biggr ) G ^ { \langle \bar { 5 } \rangle } ( b ) + b \delta _ { j k } G ^ { [ 9 p p } \biggr ] \bar { x } ^ { j } \bar { x } ^ { k } .
$$

The calculation of the metric in the new coordinate system is now complete.

To summarize, the two-parameter family of radiation-reaction gauges is described by the metric

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } \big ( U + \mathcal { U } \big ) + O ( c ^ { - 9 } ) , } } \\ { { \displaystyle g _ { 0 j } = O ( c ^ { - 8 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } + 2 \mathcal { V } _ { j k } + O ( c ^ { - 7 } ) , } } \end{array}
$$

with the radiation-reaction potentials

$$
\begin{array} { l } { { \mathcal U = \displaystyle \frac { G } { c ^ { \flat } } \bigg \{ a \ddot { I } ^ { ( j k ) } \partial _ { j k } X - b \stackrel { \dddotp } { I } ^ { p p } U - \frac { 1 } { 2 } \bigg [ \bigg ( \frac 2 5 + a \bigg ) \stackrel { ( s ) } { I } ^ { ( j k ) } + b \delta _ { j k } \stackrel { ( s ) } { I } ^ { p p } \bigg ] x ^ { j } x ^ { k } \bigg \} , } } \\ { { \mathcal V } _ { j k } = \displaystyle \frac { G } { c ^ { \flat } } \Big ( a \ddot { I } ^ { ( j k ) } + b \delta _ { j k } \ddot { I } ^ { p p } \Big ) . } \end{array}
$$

This expression for the metric omits all terms of 1pn and 2pn orders that have nothing to do with radiation reaction. To simplify the notation we have removed the (now redundant) overbars on the coordinates and potentials.

Two special cases are especially interesting and simple. When we set $a = b = 0$ we find that the radiation-reaction potentials become

$$
\begin{array} { c } { { \mathcal { U } = - \displaystyle \frac { G } { 5 c ^ { 5 } } { I ^ { \langle j k \rangle } x ^ { j } x ^ { k } } , } } \\ { { \mathcal { V } _ { j k } = 0 ; } } \end{array}
$$

this choice defines the Burke–Thorne radiation-reaction gauge. This gauge is especially attractive, because it encapsulates all radiation-reaction effects in a $O ( c ^ { - 5 } )$ correction to the Newtonian potential. On the other hand, when we set $\textstyle a = - { \frac { 2 } { 5 } }$ and $b = 0$ we find that all terms involving the mass quadrupole moment differentiated five times disappear, and we are left with

$$
\begin{array} { c } { { \displaystyle \mathcal { U } = - \frac { 2 G } { 5 c ^ { 5 } } \ddot { I } ^ { \langle j k \rangle } \partial _ { j k } X , } } \\ { { \displaystyle v _ { j k } = - \frac { 2 G } { 5 c ^ { 5 } } \ddot { I } ^ { \langle j k \rangle } ; } } \end{array}
$$

this choice defines the Schafer radiation-reaction gauge ¨ .

# 12.8.3 Radiation-reaction force

The computation of the radiation-reaction force density $f ^ { j } [ \mathrm { r r } ]$ in the two-parameter family of radiation-reaction gauges proceeds just as in Sec. 12.6. In this case we have that ${ \sqrt { - g } } =$ $1 + \mathcal { V } + O ( c ^ { - 7 } ) , \gamma = 1 + O ( c ^ { - 7 } )$ , and the components of the energy-momentum tensor are

$$
\begin{array} { r l } & { c ^ { - 2 } \sqrt { - g } T ^ { 0 0 } = \rho ^ { * } + O ( c ^ { - 7 } ) , } \\ & { c ^ { - 1 } \sqrt { - g } T ^ { 0 j } = \rho ^ { * } v ^ { j } + O ( c ^ { - 7 } ) , } \\ & { \sqrt { - g } T ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } - \bigl ( 2 \mathcal { V } ^ { j k } - \delta ^ { j k } \mathcal { V } \bigr ) p + O ( c ^ { - 7 } ) . } \end{array}
$$

We use the notation $\mathcal { V } : = \delta ^ { j k } \mathcal { V } _ { j k }$ and continue to omit all terms of 1pn and $2 \mathrm { P N }$ orders that have nothing to do with radiation reaction. The relevant Christoffel symbols are

$$
\begin{array} { c } { { c ^ { 2 } \Gamma _ { 0 0 } ^ { j } = - \partial _ { j } \big ( U + \mathcal { U } \big ) + 2 \mathcal { V } ^ { j k } \partial _ { k } U + O ( c ^ { - 7 } ) , } } \\ { { { } } } \\ { { c \Gamma _ { 0 k } ^ { j } = \partial _ { t } \mathcal { V } _ { j k } + O ( c ^ { - 7 } ) , } } \\ { { { } } } \\ { { \Gamma _ { k n } ^ { j } = O ( c ^ { - 7 } ) . } } \end{array}
$$

Making the substitutions in the momentum-conservation equation of Eq. (12.134), we arrive at the post-Newtonian Euler equation of Eq. (12.127), with

$$
f ^ { j } [ \mathrm { r r } ] = \rho ^ { * } \partial _ { j } \mathcal { U } - 2 \rho ^ { * } v ^ { k } \partial _ { t } \mathcal { V } _ { j k } - 2 \mathcal { V } ^ { j k } \big ( \rho ^ { * } \partial _ { k } U - \partial _ { k } p \big ) - \mathcal { V } \partial _ { j } p .
$$

When we next insert the radiation-reaction potentials of Eqs. (12.197), we obtain

$$
\begin{array} { l } { { f ^ { j } [ \mathrm { r r } ] = \displaystyle \frac { G } { c ^ { \dot { s } } } \bigg \{ a \ddot { \cal I } ^ { ( p q ) } \rho ^ { * } \partial _ { j p q } X - 2 a \stackrel { \cdots ( i \rlap / ) } { \cal I } ^ { ( j k ) } \big ( \rho ^ { * } \partial _ { k } U - \partial _ { k } p \big ) - b \stackrel { \cdots ( \rlap / ) } { \cal I } ^ { p p } \big ( 3 \rho ^ { * } \partial _ { j } U + \partial _ { j } p \big ) } } \\ { { \qquad \quad - 2 \rho ^ { * } \bigg ( a \stackrel { \mathrm { ( 4 ) } } { \cal I } ^ { ( j k ) } + b \delta _ { j k } \stackrel { \mathrm { ( 4 ) } } { \cal I } ^ { p p } \bigg ) v ^ { k } - \rho ^ { * } \bigg [ \bigg ( \frac 2 5 + a \bigg ) \stackrel { \mathrm { ( 5 ) } } { \cal I } ^ { ( j k ) } + b \delta _ { j k } \stackrel { \mathrm { ( 5 ) } } { \cal I } ^ { p p } \bigg ] x ^ { k } \bigg \} } } \end{array}
$$

as our final expression for the radiation-reaction force density.

The force simplifies considerably in the Burke–Thorne gauge:

$$
f ^ { j } [ \mathrm { r r } ] = - \frac { 2 G } { 5 c ^ { 5 } } \rho ^ { * } \overset { ( 5 ) } { I } ^ { ( j k ) } x ^ { k } .
$$

While its expression is more complicated in the Shafer gauge, it is nevertheless useful¨ because the number of time derivatives acting on the quadrupole-moment tensor goes down from five to four. This can be a great advantage in numerical work, because the estimation of derivatives on a finite grid generates numerical noise that can be minimized with a smaller number of derivatives. In some applications the term involving four derivatives can be small compared with terms containing three derivatives; this occurs, for example, when the system undergoes small oscillations and $v ^ { 2 }$ is small compared with $U$ (contrary to what might be expected from the virial theorem).

We next calculate the radiation-reaction force acting on the center-of-mass of each body $A$ within an $N$ -body system. The steps involved are virtually identical to those encountered previously in Sec. 12.7, and we arrive at

$$
\begin{array} { l } { { { a _ { \cal A } ^ { j } [ \mathrm { r r } ] = { \displaystyle \frac { G } { c ^ { 5 } } \Bigg \{ a \ddot { \cal I } ^ { \langle p q \rangle } \partial _ { j p q } X _ { {  } { \cal A } } - 2 a \ddot { \cal I } ^ { \langle j k \rangle } \partial _ { k } U _ { {  } { \cal A } } - 3 b \stackrel {  } { \cal I } ^ { \langle p p } \partial _ { j } U _ { {  } { \cal A } } } } } \\ { { { { } } } } \\ { { - 2 \Big ( a \stackrel { ( 4 ) } { \cal I } ^ { \langle j k \rangle } + b \delta _ { j k } \stackrel { ( 4 ) } { \cal I } ^ { \langle p p } \Big ) v _ { { \cal A } } ^ { k } - \biggl [ \biggl ( \frac { 2 } { 5 } + a \biggr ) \stackrel { ( 5 ) } { \cal I } ^ { \langle j k \rangle } + b \delta _ { j k } \stackrel { ( 5 ) } { \cal I } ^ { p p } \biggr ] r _ { { \cal A } } ^ { k } \Bigg \} , } } } \end{array}
$$

where $U _ { \neg A }$ and $X _ { \neg A }$ are the potentials produced by the bodies external to $A$ , evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ after differentiation. Taking care of these manipulations, we obtain our final expression

$$
\begin{array} { l } { { { a _ { \cal A } ^ { j } [ \mathrm { r r } ] = { \displaystyle \frac { G } { c ^ { 5 } } } \Bigg \{ 3 \sum _ { B \not = A } { \displaystyle \frac { G M _ { B } } { r _ { A B } ^ { 2 } } } \Big ( a \stackrel { \cdots \langle { \it p q } \rangle } { { \cal n } } n _ { A B } ^ { p } n _ { A B } ^ { q } + b \stackrel { \cdots \langle \dot { \it I } ^ { p p } \Big ) } { { \cal n } } n _ { A B } ^ { j } } } } \\ { { { - 2 \Big ( a \stackrel { ( 4 ) } { \cal I } ^ { ( j k ) } + b \delta _ { j k } \stackrel { ( 4 ) } { { \cal I } ^ { p p } } \Big ) v _ { A } ^ { k } - \biggl [ \biggl ( \displaystyle \frac { 2 } { 5 } + a \biggl ) \stackrel { ( 5 ) } { { \cal I } ^ { ( j k ) } } + b \delta _ { j k } \stackrel { ( 5 ) } { { \cal I } ^ { p p } } \biggr ] r _ { A } ^ { k } \biggr \} , } } } \end{array}
$$

in which $r _ { A B } : = r _ { A } - r _ { B } , r _ { A B } : = | \pmb { r } _ { A B } |$ , and $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B }$

The reduction to a two-body system produces

$$
\begin{array} { l }  { { \alpha } ^ { j } [ \mathrm { r r } ] = { \displaystyle \frac { G } { c ^ { 5 } } } \Bigg \{ 3 { \displaystyle \frac { G m } { r ^ { 2 } } } \Big ( a { \ddot { I } } ^ { ( p q ) } n ^ { p } n ^ { q } + b { \ddot { I } } ^ { p p } \Big ) n ^ { j } } \\ { { { } } } \\ { { { } - 2 \Big ( a { \ddot { I } } ^ { ( j k ) } + b \delta _ { j k } { \cal I } ^ { ( q ) p } \Big ) v ^ { k } - \Bigg [ \bigg ( { \textstyle \frac { 2 } { 5 } } + a \bigg ) { \ddot { I } } ^ { ( j k ) } + b \delta _ { j k } { \cal I } ^ { ( s ) p } \Bigg ] r ^ { k } \Bigg \} } } \end{array}
$$

for the relative acceleration $\pmb { a } [ \mathrm { r r } ] : = \pmb { a } _ { 1 } [ \mathrm { r r } ] - \pmb { a } _ { 2 } [ \mathrm { r r } ]$ . Completing the calculation with the help of Eqs. (12.174), we finally arrive at

$$
\begin{array} { r l r }   { a [ \mathrm { r r } ] = \frac { 8 } { 5 } \eta \frac { ( G m ) ^ { 2 } } { c ^ { 5 } r ^ { 3 } } \Bigg \{ \bigg [ \bigg ( 1 8 + 1 5 a - \frac { 4 5 } { 4 } b \bigg ) v ^ { 2 } + \bigg ( \frac { 2 } { 3 } - \frac { 1 0 } { 3 } a + \frac { 2 5 } { 4 } b \bigg ) \frac { G m } { r } } \\ & { } & { - \bigg ( 2 5 + 2 5 a - \frac { 7 5 } { 4 } b \bigg ) \dot { r } ^ { 2 } \bigg ] \dot { r } n - \bigg [ \bigg ( 6 + \frac { 3 5 } { 6 } a - \frac { 5 } { 2 } b \bigg ) v ^ { 2 } } \\ & { } & { - \bigg ( 2 + \frac { 3 5 } { 6 } a - \frac { 5 } { 2 } b \bigg ) \frac { G m } { r } - \bigg ( 1 5 + \frac { 3 5 } { 2 } a - \frac { 1 5 } { 2 } b \bigg ) \dot { r } ^ { 2 } \bigg ] v \Bigg \} . } \end{array}
$$

In the Burke–Thorne gauge $\overset { \cdot } { a } = \overset { b } { b } = 0$ ) the relative acceleration reduces to

$$
a [ \Gamma \Gamma ] = \frac { 8 } { 5 } \eta \frac { ( G M ) ^ { 2 } } { c ^ { 5 } r ^ { 3 } } \biggl [ \biggl ( 1 8 v ^ { 2 } + \frac { 2 } { 3 } \frac { G M } { r } - 2 5 \dot { r } ^ { 2 } \biggr ) \dot { r } n - \biggl ( 6 v ^ { 2 } - 2 \frac { G M } { r } - 1 5 \dot { r } ^ { 2 } \biggr ) v \biggr ] ,
$$

while in the Schafer gauge  ¨ $( a = - 2 / 5$ , $b = 0$ ) we have

$$
a [ \mathrm { r r } ] = \frac { 8 } { 5 } \eta \frac { ( G M ) ^ { 2 } } { c ^ { 5 } r ^ { 3 } } \biggl [ \biggl ( 1 2 v ^ { 2 } + 2 \frac { G M } { r } - 1 5 \dot { r } ^ { 2 } \biggr ) \dot { r } n - \biggl ( \frac { 1 1 } { 3 } v ^ { 2 } + \frac { 1 } { 3 } \frac { G M } { r } - 8 \dot { r } ^ { 2 } \biggr ) v \biggr ] .
$$

In addition to these choices, it is interesting to note that the settings $a = - 2 / 3$ and $b = 4 / 9$ produce

$$
a [ \mathrm { r r } ] = \frac { 8 } { 5 } \eta \frac { ( G M ) ^ { 2 } } { c ^ { 5 } r ^ { 3 } } \biggl [ \biggl ( 3 v ^ { 2 } + \frac { 1 7 } { 3 } \frac { G M } { r } \biggr ) \dot { r } n - \biggl ( v ^ { 2 } + 3 \frac { G M } { r } \biggr ) v \biggr ] ,
$$

the same expression as in Eq. (12.175); the two-parameter family of radiation-reaction gauges can therefore reproduce the original expression for the relative acceleration, which was obtained in the harmonic gauge. It should be kept in mind that while the relative accelerations do correspond when $a = - 2 / 3$ and $b = 4 / 9$ , the coordinate systems do not coincide, and the radiation-reaction potentials are quite different in the two gauges. This selection of parameters is often called the Damour–Deruelle gauge.

# 12.8.4 Balance equations

To finish our discussion of the two-parameter family of radiation-reaction gauges, we verify that the radiation-reaction force density of Eq. (12.203) is compatible with the statements of energy, momentum, and angular-momentum balance.

We begin with energy balance, and follow the developments of Sec. 12.6.3. Here the precise statement of energy balance is more complicated than in Eq. (12.140), because $\rho \neq \rho ^ { * }$ in the two-parameter family of radiation-reaction gauges. Instead we have that

$$
\rho = ( 1 - \mathcal { V } ) \rho ^ { * } + O ( c ^ { - 7 } ) ,
$$

up to corrections of 1pn and 2pn orders, and the presence of $\mathcal { V }$ affects the statement of the first law of thermodynamics. The exact formulation, we recall, is $d \Pi / d t = ( p / \rho ^ { 2 } ) d \rho / d t$ , and this implies that

$$
\rho ^ { * } \frac { d \Pi } { d t } = ( 1 + \mathcal { V } ) \frac { p } { \rho ^ { * } } \frac { d \rho ^ { * } } { d t } - p \partial _ { t } \mathcal { V } + O ( c ^ { - 7 } ) ,
$$

where we use the fact that $\mathcal { V }$ depends on time only. The continuity equation satisfied by $\rho ^ { * }$ allows us to replace $d \rho ^ { * } / d t$ with $- \rho ^ { * } \partial _ { j } v ^ { j }$ , and integrating over the volume occupied by the fluid, we obtain

$$
\frac { d E _ { \mathrm { i n t } } } { d t } = ( 1 + \mathcal { V } ) \int v ^ { j } \partial _ { j } p d ^ { 3 } x - P \partial _ { t } \mathcal { V } + O ( c ^ { - 7 } )
$$

for the rate of change of the fluid’s internal energy; here $\textstyle P : = \int p d ^ { 3 } x$ is the integrated pressure. The terms in $\mathcal { V }$ contribute to the change in total energy at $2 . 5 \mathrm { { p N } }$ order, and instead of Eq. (12.140) we find that

$$
\int v _ { j } f ^ { j } [ \mathrm { r r } ] d ^ { 3 } x + \mathcal { V } \int v ^ { j } \partial _ { j } p d ^ { 3 } x - P ~ \partial _ { t } \mathcal { V } + \frac { d } { d t } \Big ( c ^ { - 5 } E [ 5 ] \Big ) = - \frac { G } { 5 c ^ { 5 } } \dddot { I } ^ { \langle j k \rangle } \ddot { I } ^ { \langle j k \rangle } + O ( c ^ { - 7 } ) .
$$

is the precise statement of energy balance in the two-parameter family of radiation-reaction gauges. The integrals can be evaluated in the same way as in Sec. 12.6.3, and after some calculations we confirm that the radiation-reaction force density of Eq. (12.203) is indeed compatible with energy balance. In the course of this computation we also find that

$$
\begin{array} { c } { { c ^ { - 5 } E [ 5 ] = { \displaystyle \frac { G } { c ^ { 5 } } } \Bigg [ 4 a ~ \overleftrightarrow { I } ^ { \langle j k \rangle } \uparrow ^ { j k } + { \displaystyle \frac { 1 } { 2 } } \Bigg ( \frac 2 5 + a \Bigg ) \Big ( \overbrace { I } ^ { ( 4 ) } j k ) ~ \overleftrightarrow { I } ^ { \langle j k \rangle } - \overleftrightarrow { I } ^ { \langle j k \rangle } \overleftrightarrow { I } ^ { \langle j k \rangle } \Bigg ) } } \\ { { + b ~ \overleftrightarrow { I } ^ { \langle p p } \big ( 4 7 + 3 P \big ) + { \displaystyle \frac { 1 } { 2 } } b \left( \overbrace { I } ^ { ( 4 ) } p \thinspace j ^ { q q } - \overleftrightarrow { I } ^ { \langle p p } \thinspace \overleftrightarrow { I } ^ { q q } \right) \Bigg ] } } \end{array}
$$

is the appropriate expression for the $2 . 5 \mathrm { { p N } }$ contribution to the total energy.

The statement of momentum balance requires no modification from Eq. (12.153), and the computations carried out in Sec. 12.6.4 can easily be adapted to the two-parameter family of radiation-reaction gauges. We confirm that the radiation-reaction force density of Eq. (12.203) is indeed compatible with momentum balance, and that

$$
c ^ { - 5 } P ^ { j } [ 5 ] = 0
$$

in these gauges; there is no contribution to the total momentum at $2 . 5 \mathrm { { p N } }$ order.

The same statements apply to the expression of angular-momentum balance. Here also the precise statement of Eq. (12.159) requires no modification, and here also we find that it is compatible with Eq. (12.203). The $2 . 5 \mathrm { { p N } }$ contribution to the total angular-momentum tensor is given by

$$
\begin{array} { l } { { c ^ { - 5 } J ^ { j k } [ 5 ] = { \displaystyle \frac { G } { c ^ { 5 } } } \bigg [ \bigg ( { \textstyle \frac { 2 } { 5 } } + a \bigg ) \Big ( I ^ { j p } I ^ { ( 4 ) } I ^ { \ast p } - I ^ { k p } I ^ { ( 4 ) } I ^ { p } \Big ) + a \Big ( J ^ { j p } \ddot { I } ^ { \ast p } - J ^ { k p } \ddot { I } ^ { \ast p } \Big ) } } \\ { { - { \displaystyle \frac { 2 } { 5 } } \Big ( \dot { I } ^ { j p } \ddot { I } ^ { \ast p } - \dot { I } ^ { k p } \ddot { I } ^ { \ast p } \Big ) \bigg ] } } \end{array}
$$

in the two-parameter family of radiation-reaction gauges.

# 12.9 Orbital evolution under radiation reaction

In this last section of Chapter 12 we describe how the radiation-reaction force of Eq. (12.208) affects the orbital motion of a two-body system. The system’s dynamics is dominated by the Newtonian gravitational attraction between the two bodies, and the radiation-reaction force creates a perturbation. We wish to determine the effect of this perturbing force over a time scale that is much longer than the orbital period; we are primarily interested in the secular effects of the radiation-reaction force. The Newtonian dynamics was investigated in detail back in Sec. 3.2, and a formalism to describe perturbed Keplerian orbits, based on osculating elliptical orbits and evolving orbital elements, was introduced in Sec. 3.3; our analysis in this section employs this formalism as an essential foundation.

# 12.9.1 Evolution of orbital elements

We return to Eq. (12.208) and substitute Keplerian expressions for $r : = r _ { 1 } - r _ { 2 }$ and $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , which we decompose as $\boldsymbol { r } = \boldsymbol { r } \boldsymbol { n }$ and $\pmb { v } = \dot { r } \pmb { n } + ( r \dot { \phi } ) \pmb { \lambda }$ , with $\dot { \phi }$ denoting the orbital angular velocity. The unit vectors $\pmb { n }$ and $\gimel$ are tangent to the orbital plane and mutually orthogonal; in Cartesian coordinates $( x , y , z )$ oriented in such a way that the orbital plane coincides with the surface $z = 0$ , we have that $\pmb { n } = [ \cos \phi , \sin \phi , 0 ]$ and $\lambda = [ - \sin \phi , \cos \phi , 0 ]$ , where $\phi ( t )$ is the angle between $r$ and the $x$ -axis. The Keplerian relations are

$$
r = \frac { p } { 1 + e \cos f } , \qquad \dot { r } = \sqrt { \frac { G m } { p } } e \sin f , \qquad r \dot { \phi } = \sqrt { \frac { G m } { p } } ( 1 + e \cos f ) ,
$$

where $p$ is the semi-latus rectum, $e$ the eccentricity, $f : = \phi - \omega$ the true anomaly, and $\omega$ the longitude of pericenter. The orbital period is

$$
P = \frac { 2 \pi } { \sqrt { G m } } { \left( \frac { p } { 1 - e ^ { 2 } } \right) } ^ { 3 / 2 } ,
$$

and $p / ( 1 - e ^ { 2 } )$ is the semi-major axis.

Making the substitutions in Eq. (12.208) returns

$$
a [ \mathrm { r r } ] = \frac { 8 } { 5 } \eta \frac { ( G m ) ^ { 7 / 2 } } { c ^ { 5 } p ^ { 9 / 2 } } ( 1 + e \cos f ) ^ { 3 } \big [ ( e \sin f ) A n - ( 1 + e \cos f ) B \lambda \big ] ,
$$

with

$$
\begin{array} { c } { { d : = \displaystyle \frac { 4 4 } { 3 } + \frac { 3 5 } { 3 } a - 5 b + e \bigg ( \frac { 8 0 } { 3 } + \frac { 1 2 5 } { 6 } a - \frac { 5 5 } { 4 } b \bigg ) \cos { f } } } \\ { { \displaystyle + e ^ { 2 } \bigg [ 2 + \frac { 5 } { 3 } a + \frac { 5 } { 2 } b + \bigg ( 1 0 + \frac { 1 5 } { 2 } a - \frac { 4 5 } { 4 } b \bigg ) \cos ^ { 2 } { f } \bigg ] , } } \\ { { \displaystyle B : = 4 + e \bigg ( 1 0 + \frac { 3 5 } { 6 } a - \frac { 5 } { 2 } b \bigg ) \cos { f } } } \\ { { \displaystyle - e ^ { 2 } \bigg [ 9 + \frac { 3 5 } { 3 } a - 5 b - \bigg ( 1 5 + \frac { 3 5 } { 2 } a - \frac { 1 5 } { 2 } b \bigg ) \cos ^ { 2 } { f } \bigg ] . } } \end{array}
$$

We recall that $a$ and $b$ are parameters that specify the choice of radiation-reaction gauge. In the Burke–Thorne gauge we set $a = 0$ and $b = 0$ , in the Schafer gauge we set ¨ $\textstyle a = - { \frac { 2 } { 5 } }$ and $b = 0$ , and the assignments $a = - 2 / 3$ and $b = 4 / 9$ produce the harmonic-gauge expression for the radiation-reaction force.

The effect of a perturbing force on the Keplerian orbital elements $p , e$ , and $\omega$ was described in detail back in Sec. 3.3. In this description, the orbital motion is described at all times by the Keplerian relations of Eq. (12.219), but the orbital elements acquire a time dependence from the perturbing force. This description is exact, and the method of