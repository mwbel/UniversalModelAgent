over K-1 variables and equating the result to d(E). A simpler alternative is to use the approximate method of Wigner (1957): For P(E) we substitute P[f(E)], where f(E)dE is the number of eigenvalues in the interval dE. The allowed distributions f(E) should be a set of K Dirac δ functions, but in the limit where K→oo we can approximate f(E) by a smooth function. The assumption is that f=d is the distribution that maximizes

$$
\log P [ f ] \simeq \int d E f ( E ) \lambda ( E ) + ( \beta / 2 ) \int d E d E ^ { \prime } f ( E ) f ( E ^ { \prime } ) \log | E - E ^ { \prime } | .
$$

[This neglects correlations inthe second term of(8.47), which,it is hoped, are of short range.] Diferentiating with respect to f, we obtain explicitly

$$
\lambda ( E ) \simeq - ( \beta / 2 ) \int d E ^ { \prime } \overline { { d } } ( E ^ { \prime } ) \log | E - E ^ { \prime } | .
$$

# Exercise

Verify that this expression for ^ makes P(E) invariant with respect to changes in the energy scale.

In the case of the Gaussian ensembles, we have no a priori knowledge of $\langle d ( E ) \rangle$ .Wigner's methodcannowbeappliedto(8.47),resultinginthe integral equation

$$
- ( 4 \sigma ^ { 2 } ) ^ { - 1 } E ^ { 2 } + \beta \int d E ^ { \prime } \langle d ( E ^ { \prime } ) \rangle \log | E - E ^ { \prime } | = \mathrm { c o n s t } ,
$$

with the solution

$$
\langle d ( E ) \rangle = \left\{ \begin{array} { l l } { ( 2 \pi \sigma ^ { 2 } ) ^ { - 1 } ( 4 N \sigma ^ { 2 } - E ^ { 2 } ) ^ { 1 / 2 } , \quad } & { | E | \leq 2 N ^ { 1 / 2 } \sigma } \\ { 0 , \quad } & { | E | \geq 2 N ^ { 1 / 2 } \sigma . } \end{array} \right.
$$

This expression for the mean level density coincides with the exact result for the Gaussian ensembles, obtained by direct integration. This fact reinforces our confidence as to the value of the approximation (8.50 for the Weyl-Balian density.

The semicircular form of the density of states for the Gaussian ensembles usually bears no relation tothe true Weyl density. Evenso,both istributions show level repulsion- $P ( \mathbf { E } )  0$ as two levels approach each other. The similarity between the Weyl-Balian and the Gaussian distributions permits us to fit the latter to the former in a small energy range $d E \propto \hbar$ which is suficient to obtain statistical properties of an individual semiclassical spectrum. The Gaussian distributions have two free parameters - the width and the mean $\dot { E }$ ,taken as zero in (8.47). Thus,choosing $\sigma$

$$
\begin{array} { r } { \overline { { E } } = E - 2 \lambda / \lambda ^ { \prime } ( E ) , \qquad \sigma ^ { 2 } = - \lambda / ( \lambda ^ { \prime } ) ^ { 2 } , } \end{array}
$$

where $\lambda ^ { \prime } = d \lambda / d E$ ,we fit

$$
\lambda ( E ) = - ( 4 \sigma ^ { 2 } ) ^ { - 1 } ( E - \overline { { E } } ) ^ { 2 }
$$

up to the first order in the Taylor expansion about any point inside δE. The only condition is that λ(E)<O, which implies that d(E) should not have any very narrow peak. But this event can always be avoided with a change in energy scale, since the Weyl-Balian distribution with $\lambda ( E )$ given by (8.50) is scale invariant.

The great advantage of fitting the Gaussian distributions to the correct distributions for an ergodic semiclassical spectrum is that many important statistical properties of the former are known exactly. This is the case of the two-level correlation function

$$
Y _ { 2 } ( E _ { 1 } , E _ { 2 } ) \equiv - \frac { P ( E _ { 1 } , E _ { 2 } ) - P ( E _ { 1 } ) P ( E _ { 2 } ) } { P ( E _ { 1 } ) P ( E _ { 2 } ) }
$$

and of higher correlation functions (see Bohigas and Giannoni, 1984,for references). In the case of the Gaussian orthogonal ensemble, $\beta = 1$ ,we obtain the limits

$$
\begin{array} { r l } & { Y _ { 2 } ( r ) \underset { r  0 } { \longrightarrow } 1 - \frac { 1 } { 6 } \pi ^ { 2 } r + \frac { 1 } { 6 0 } \pi ^ { 4 } r ^ { 3 } + \cdots , } \\ & { } \\ & { Y _ { 2 } ( r ) \underset { r  \infty } { \longrightarrow } ( \pi r ) ^ { - 2 } - ( 1 + ( \cos \pi r ) ^ { 2 } ) ( \pi r ) ^ { - 4 } + \cdots , } \end{array}
$$

where

$$
r = | E _ { 2 } ^ { \bot } - E _ { 1 } | \bar { d }
$$

in a region in which $d ( E ) = K P ( ; E )$ can be considered constant. The distribution for the nearest-neighbour spacings has the form

$$
P ( r ) = ( \dot { \beta \pi } ^ { 2 } / 6 ) r ^ { \beta } + \cdots .
$$

We are now in a position to ascertain whether classically ergodic systems have spectra that are also ergodic. The computational eyidence that this is indeed the case has become substantial.Forexample,Bohigas.Ginnoni and Schmit (1984) obtained the histogram for $P ( r )$ jh fig.8.7from the analysis of740levels of Sinai's billiard.Similarcalculations for the stadium as well as other statistics of the spectrum are also Well fitted by the GOE. At the start of this section we restricted this analysis to systems without any special symmetries;therefore,fig8.7 deals with the spectrum for only one-eighthof Sinai'sbilliard (thedesymmetrized biiard).

![](images/01e4439c0c4709b28411eb74c0b01890593b91b67be5f8095faa40af21b6394a.jpg)  
Fig8.7.Histogram of the nearest-neighbour spacings in the spectrum of Sinai's billrard. ashed curvePoisson distribution;solid curve,OE;steped e Sinal's billiard.(Courtesy of O.Bohigas,M.J.Giannoni and C.Schmit.)

![](images/9ccd5b1b832308fb7983735fc5219c625b10ed8e2a67f8769371ad5439d13795.jpg)  
Fig8.8.Nearest-neighbour spacing for the quarter-circle biliardDashed curve, PoisondistrtioleOE;eppdreartecee of O. Bohigas, M. J. Giannoni and C. Schmit.)

![](images/79e7ad4b7fddf132c3aae4c40b25972ff00fa5c590e09defb453fdeec64af3fe.jpg)

As a comparison, figC8.8presents the nearest-neighbour spacing of an integrable billiard - the quarter of a circle. There is no correlation between the way that different regions of the energy shell H(I) = E sweep through the/dense’ lattice of quantized tori in fig7.4. The fluctuations of the spectrum can thus be approximately modelled by the Poisson distribution. There is no level repulsion in this case.

# 8.5 Quantization of the cat map

Consideration of the discrete Poincare map is always helpful in the study of continuous classical systems. However, there is no obvious way to quantize maps directly.The best available option is to consider the classical map as the stroboscopic map of a time-periodic Hamiltonian system and then deal with the period operator $\hat { U } _ { \tau }$ , that is, the evolution operator for the period $\tau$ of the Hamiltonian. This operator is unitary rather than Hermitian, but we can also investigate its eigenvalues and eigenfunctions. In particular we can verify whether its spectrum is ergodic, which in this instance means having the same fluctuation statistics as the circular ensemble of Dyson (1962) with properties similar to those of the Gaussian ensembles. The quantum map that has been most intensively studied is the ‘standard map':

$$
\begin{array} { l } { { p ^ { \prime } = q - K \sin q , } } \\ { { q ^ { \prime } = q + p ^ { \prime } , } } \end{array}
$$

obtained from the periodic Hamiltonian,

$$
H ( p , q , t ) = \frac { p ^ { 2 } } { 2 } + \frac { K } { 2 \pi } \cos q \sum _ { n } \delta ( t - 2 n \pi ) ,
$$

known as the kicked rotor,by Casati,Chirikov,Ford and Izrailev (1979).

Unfortunately the rigorous mathematical basis for quantum timeperiodic systems is less developed than that for time-independent Hamiltonians. Indeed,one of the ways of obtaining such results, known as Howland'std (owlad,98o),sistseiselyf theelio of time by expanding the phase space by two extra dimensions - just the reverse procedure of taking the Poincare section!

An especially simple map to quantize is Arnold's cat map, presented in section 1.4 and used thereafter as a paradigm of classically chaotic motion. It has several unusual characteristics, but it is worthwhile to review briefly the results of Hannay and Berry (198O). In the case of the rotor (8.61), the variable $q$ is an angle with period $2 \pi$ (the phase space is acylinder), so the conjugate variable - the angular momentum -is discretized. In the cat map, with (p,q)=(02,01) in section 1.4,the momentum is also peridic (the phase space is a torus); therefore, the coordinates q are also discrete. The p and q wave functions for this system are necessarily ‘combs’ of equally spaced δ functions modulated by a (complex) periodic amplitude. The coordinate representation is

$$
\langle q | \psi \rangle = \sum _ { k = - \infty } ^ { \infty } \sum _ { n = 1 } ^ { N } a _ { n } \delta \Bigg ( q - \bigg ( \frac { n } { N } + k \bigg ) 2 \pi \Bigg ) ,
$$

with the Fourier transform

$$
 { p } | \psi  = ( { 2 \pi \hbar } ) ^ { - 1 / 2 } \sum _ { k = - \infty } ^ { \infty } \sum _ { n = 1 } ^ { N } a _ { n } \exp \{ { i \hbar ^ { - 1 } 2 \pi \bigg ( \frac { n } { N } + k \bigg ) p \} } .
$$

The periodicity of the momentum must then be

$$
\Delta p = N \hbar ,
$$

so that the area of the torus is quantized as

$$
\Delta p \Delta q = 2 \pi \hbar N .
$$

In other words, the choice $\Delta q = \Delta p = 2 \pi$ determines

$$
\hbar = 2 \pi / N ,
$$

where $N$ is the number of'teeth' in one period of the wave function comb. The semiclasical limit $\hbar  0$ here correspondsto $N  \infty$ .Use of the Poisson identity,

$$
\sum _ { j = - \infty } ^ { \infty } \delta ( t - j ) = \sum _ { k = - \infty } ^ { \infty } \exp ( i 2 \pi k t ) ,
$$

leads to

$$
\langle p | \psi \rangle = \sum _ { j = - \infty } ^ { \infty } \left\{ \sum _ { n = 1 } ^ { N } N ^ { - 1 / 2 } a _ { n } \exp ( i n p ) \right\} \delta \Biggl ( p - \frac { 2 \pi j } { N } \Biggr ) ,
$$

that is,a $\delta$ comb with $N$ teeth in each period.

So far we have studied only the kinematics of the cat map.Its dynamics are based on the propagator corresponding to a linear canonical transformation, studied in section 7.6. The generating function

$$
S ( q , \mathfrak { q } ) = ( \alpha \mathfrak { q } ^ { 2 } + 2 \beta \mathfrak { q } q + \gamma q ^ { 2 } ) / 2
$$

defines the exact quantum propagator

$$
\left. { q } \right. \hat { U } \vert q \rangle = ( - i \beta / 2 \pi \hbar ) ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } S ( \mathsf { q } , q ) \right\} .
$$

The classical map has the form

$$
{ \Bigg [ } { \underset { \mathbb { q } } { \mathbb { p } } } { \Bigg ] } = { \Bigg [ } { \underset { b } { a } } & { d } { \Bigg ] } { \Bigg [ } { \underset { q } { p } } { \Bigg ] } = { \Bigg [ } { - } { \frac { \alpha } { \beta } }  &  { \frac { \beta ^ { 2 } - \alpha \gamma } { \beta } } { \Bigg ] } { \Bigg [ } { \underset { q } { p } } { \Bigg ] } .
$$

Therefore, the propagator can be written as

$$
\langle \mathfrak { q } | \hat { U } | q \rangle = \frac { 1 } { 2 \pi } \bigg ( \frac { i N } { b } \bigg ) ^ { 1 / 2 } \exp \bigg \{ \frac { i N } { 4 \pi b } ( a \mathfrak { q } ^ { 2 } - 2 \mathfrak { q } q + c q ^ { 2 } ) \bigg \} ,
$$

where the constants $N$ a $b$ ， $c$ are all integers.

In order to build up the torus propagator we now have to combine all the contributions of equivalent points $q + 2 \pi m$ to the amplitude at q $( \sqrt { 1 8 } , ( 8 . 9 ) ,$ The contributions of all equivalent points to the propagator at q will be out of phase and therefore cancel if $\mathfrak { q }$ is not on the $\delta$ comb. Conversely points on the $\delta$ comb may receive all contributions in phase. The analysis becomes very simple in the special case where $b = 1$ .Then

$$
\begin{array} { l } { { \displaystyle \langle \mathfrak { q } | \hat { U } | q \rangle _ { \mathrm { t o r u s } } = \frac { 1 } { 2 \pi } ( i N ) ^ { 1 / 2 } \sum _ { m } \exp \left\{ \frac { i N } { 4 \pi } [ a \mathfrak { q } ^ { 2 } - 2 \mathfrak { q } ( q + 2 \pi m ) + c ( q + 2 \pi m ) ^ { 2 } ] \right\} } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 \pi } ( i N ) ^ { 1 / 2 } \exp \left\{ \frac { i N } { 4 \pi } ( a \mathfrak { q } ^ { 2 } - 2 \mathfrak { q } q + c q ^ { 2 } ) \right\} } } \\ { { \displaystyle \qquad \times \sum _ { m } \exp \left\{ i \pi [ N c m ^ { 2 } + 2 ( c Q - \mathfrak { Q } ) m ] \right\} , \qquad ( 8 . 7 ) \exp \left\{ \right\} , \qquad z \in \mathfrak { g } ^ { 2 } , } } \end{array}
$$

![](images/fde828da5c45ef3178f7fe2e6c20416ccb66b9d5c743a36c3518c5edf4fff649.jpg)  
Fig(8.9.jPeriodicity of the torus demands that the contribution of equivalent pointsq+2πm be included in the propagator.

defining the integers

$$
Q = N q / 2 \pi .
$$

If Nc is even, then the exponential in the sum over m is always unity, so the sum diverges.therwise,it vanishes since Nc,being odd,implis an equal number of +1 and -1 terms.Instead of dealing directly with Dirac δ functions (in the case where Nc is odd),it is simpler to work with the discrete propagator

$$
\big < { \mathfrak { q } } | { \hat { U } } | { \mathfrak { q } } \big > _ { D } = \left( \frac { i } { N } \right) ^ { 1 / 2 } \exp \bigg \{ \frac { i N } { 4 \pi } ( a { \mathfrak { q } } ^ { 2 } - 2 { \mathfrak { q } } q + c q ^ { 2 } ) \bigg \} ,
$$

with the normalization

$$
\sum _ { \mathfrak { q } } | \langle { \mathfrak { q } } | { \hat { U } } | q \rangle _ { D } | ^ { 2 } = 1 .
$$

The analysis becomes much more intricate if b is a general integer. In particular,it is not always true that the discrete propagator has the same quadratic exponent as the plane propagator used to construct it. Hannay and Berry (198o) obtain general conditions for quantization: The matrix for the classical map must have the checker board structure

$$
{ \left[ \begin{array} { l l } { \mathsf { e v e n } } & { \mathsf { o d d } } \\ { \mathsf { o d d } } & { \mathsf { e v e n } } \end{array} \right] } \qquad { \mathrm { o r } } \qquad { \left[ \begin{array} { l l } { \mathsf { o d d } } & { \mathsf { e v e n } } \\ { \mathsf { e v e n } } & { \mathsf { o d d } } \end{array} \right] } .
$$

This restriction prevents the quantization of the cat map (1.61) itself, though we can quantize the hyperbolic map with the matrix

$$
{ \left[ \begin{array} { l l } { 2 } & { 3 } \\ { 1 } & { 2 } \end{array} \right] } .
$$

This has $b = 1 ,$ so the discrete propagator is

$$
\langle { \mathfrak { q } } | { \hat { U } } | { \mathfrak { q } } \rangle _ { D } = \left( { \frac { i } { N } } \right) ^ { 1 / 2 } \exp \left\{ { \frac { i N } { 2 \pi } } ( { \mathfrak { q } } ^ { 2 } + { \mathfrak { q } } q + { q } ^ { 2 } ) \right\} .
$$

The elliptic map

$$
\left[ { \begin{array} { r l } { 0 } & { { } - 1 } \\ { 1 } & { { } \quad 0 } \end{array} } \right]
$$

also has $b = 1$ SO

$$
\langle { \sf q } | \hat { U } | { \cal q } \rangle _ { \cal D } = \left( \frac { i } { \cal N } \right) ^ { 1 / 2 } \exp \bigg \{ - \frac { i { \cal N } } { 2 } { \sf q } q ^ { \prime } \bigg \} .
$$

We achieve a better grasp of the quantum cat map from the Wigner function. It was found in section 7.4 that the Wigner function propagates classically in a plane phase space, under the action of a linear map. For $b = 1$ the quantum map has a discrete propagator with the same form as the plane propagator, so the torus Wigner function propagates a classical distribution. A small complication arises from the need generally to include half-integer multiples of $2 \pi / N$ for both the $p$ and the $q$ coordinates, as discussed by Ozorio de Almeida (1984). However, Hannay and Berry (1980) show that these supplementary coordinates can be omitted if $N$ is odd. In this case we can consider Wigner functions defined on the $N \times N$ points of the quantized torus and normalized so that

$$
\sum _ { p , q } W ( p , q ) = 1 ,
$$

All the quantized coordinates are multiples of $2 \pi / N$ ,so the effect of the (integer) linear map is merely to permute the discrete points of the quantized torus. Each of these points has a periodic orbit with a period $n _ { i } \le N ^ { 2 }$ .After $n$ iterations, where $n$ is the minimum common multiple of the $n _ { i }$ ,the map brings any Wigner function back to itself. In other words the quantum map is periodic with period $n ( N )$ Figure $\overline { { 8 . 1 9 } }$ shows all the

![](images/d987756109240c3abe39be2dd52fbc493c596d67a55a32a1f60121440acbc587.jpg)

Fi8 $N = 5$ cycles of the map (8.78) for $N = 5$ . An eigenstate of a quantized map has a Wigner function such that all points on the same periodic orbit have the same amplitude. Except for this restriction,the Wigner functions for the eigenstates of (8.78) bear no obvious relation tothe classical periodic orbits. The five Wigner functions depicted in figC8.11jcorrespond to the same quantum map whose cycles appear in fig 8.10,In fig(8.11 the values of $W$ are proportional to the size of the squares, and negative values appear as black squares. The probability densities for the $q$ and the $p$ representations appear,respectivelybeneath and to the left of each igure.

![](images/7f9500e5200157ed561d05317f2d05a4dff98792475cbf06d6fe1f236453c67a.jpg)  
Fig8.11 Wigner functions for the same map as in fig.8.10.The values of $W$ are proportional to the size of the squares,and negative values appearas black squares. The lines to the left and underneath each figure are the projected probability densities.(Courtesy of J.H. Hannay and M.V. Berry.)

The eigenvalues of the propagator fall on the unit circle. Since the quantum map is periodic, the $N$ eigenvalues have values

$$
\alpha _ { j } = k _ { j } 2 \pi / n .
$$

Figure(8.12jshows the graph of $n ( N )$ computed by Hannay and Berry (1980) for the map (8.78). In contrast, the elliptic map (8.79) has $n = 4$ for all $N \geq 4$ .Thus, there is a marked difference between the spectra of maps corresponding to classically integrable or chaotic motion. However, though $n ( N )$ is highly irregular, computations of $n ( N )$ up to $N = 1 0 ^ { 5 }$ indicate that

$$
n ( N ) \sim C N ,
$$

with $C < 1$ .The serious implication is that generally there are some degenerate levels and there is no chance for there to be level repulsion in the semiclassical limit as $N \to \infty$ . This would be possible if $n ( N ) \propto N ^ { 2 }$ for example. Though the cat map is a paradigm of classically chaotic motion, the quantum cat map does not have an ergodic spectrum. This is the only known counterexample of the rule presented in the previous section. The

![](images/4d0404db18e2f4a107309c36744af947853d2384ae41cddf96f335313b6a426c.jpg)  
Fig(8.12.jThe graph of n(N). (Courtesy of J. H. Hannayand M.V. Berry.)

![](images/bf7a07a6a3a35e02e66f536f43b71a466fb0bceefa938c7c8c114ec2bb87bab4.jpg)

Periodic orbits in quantum mechanics

The quantization of classically integrable systems relies explicitly on the invariant tori that foliate phase space. No distinction is made in the traditional semiclassical theory as to whether the motion on a quantized torus is periodic or only quasi-periodic. A strong perturbation may break up tori with incommensurate frequencies as well as those with periodic orbits. The only surviving smooth invariant manifolds, beyond the energy shell itself, will then be isolated periodic orbits. The semiclassical limit of stationary states must therefore bear some relation to these invariant curves. The uncertainty principle prevents us from attempting to tighten too closely the association between a given orbit and a specific state. In the last resort a state has to rely on a collection of periodic orbits or at least on a periodic orbit dressed with the local motion around it.

The basic instrument for evoking the contribution of periodic orbits is the semiclassical propagator for points that return to their initial positions. The classical orbits determining this propagator are dominated by the periodic orbits, in a way that is explained in section 9.1. On the other hand, the propagator can be represented as a sum over the intensities of the stationary wave functions. A local analysis establishes that individual wave intensities may exhibit strong ‘scars’ along some periodic orbits. Taking the trace of the propagator, we obtain a formula for the density of states as a sum over all the periodic orbits.

Evaluating the trace of the propagator by the method of stationary phase,we obtain in section 9.3 the contribution of each periodic orbit together with the surrounding linearized motion. This works wellfor unstable periodic orbits and hence for ergodic systems.The stationary-phase contributions of stable periodic orbits suffer from a small-denominator problem, reminiscent of the classical theory presented in chapter 4. The solution to this problem is obtained in section 9.4 by substituting the resonant normal forms derived in section 4.4 for the inadequate linearization of the motion. Similar methods allow us to follow the periodic orbit sum through the transition of the breaking of integrability. In the opposite case of clasical sstems with posiive etropythe ombinatio of the uniformity principle of section 3.7 with the periodic orbit sum leads to a partial dynamical explanation of ergodic spectra.

# 9.1 Stationary states and the propagator

The attempt to refine the classical limit of the Wigner function for an ergodic system by means of the pure-state condition in section 8.2 revealed a direct dependence on individual orbits in the energy shell. However, it is not easy to seek orbits with the property that their end points define a chord with a preestablished midpoint! It is more natural to return to the semiclassical propagator presented in section 7.6. Again we find a dependence on individual orbits,but these are defined directly by the variational principle for'the action of paths between two points q and ${ \mathfrak { q } }$

The propagation of a nonstationary semiclassical wave function is tied to the motion of a classical Lagrangian surface. Neither depends on the existence of invariant tori in the classical system.The specific case in which the Lagrangian surface starts out as the plane q = const.defines the semiclassical propagator. Alternatively, the propagator can also be envisaged as the coordinate representation $\langle \mathfrak { q } | \hat { U } | \mathfrak { q } \rangle$ of the evolution operator (7.86). This is a function of the Hamiltonian, so it has the diagonal energy representation

$$
\hat { U } ( t ) = \sum _ { k } | \psi _ { k } \rangle \langle \psi _ { k } | \exp ( - i \hbar ^ { - 1 } E _ { k } t ) .
$$

Returning to the coordinate representation, we obtain

$$
\langle \pmb { \mathfrak { q } } | \hat { U } | \pmb { \mathfrak { q } } \rangle = \sum _ { k } \langle \pmb { \mathfrak { q } } | \psi _ { k } \rangle \langle \psi _ { k } | \pmb { \mathfrak { q } } \rangle \exp ( - i \hbar ^ { - 1 } E _ { k } t ) .
$$

Thecrucial importance ofthis equationis that it ties the sum over unknown stationary states to a familiar semiclassical wave function.

We can easily invert (9.2) by taking its Fourier transform.However, we should proceed with some caution,because this would imply theknowledge of the semiclassical propagator even in the limits $t  \pm \infty$ .For a bound system,the originally plane Lagrangian surface will be infinitely convoluted,in a manner analysedby Berryand Balazs (1979). The caustics then proliferate, destroying the simple semiclassical form of the propagator. For this reason it is safer to multiply the propagator by a hat function (unit near the origin while decaying to zero for $t  \pm \infty$ ）before taking the Fourier transform. This is conveniently defined as the Fourier transform of a member of a family of peaked functions $\delta _ { \lambda } ( E )$ whose limit

as $\lambda \to 0$ is the Dirac $\delta$ function:

$$
\Delta _ { \lambda } ( t ) = \int _ { - \infty } ^ { \infty } d E \delta _ { \lambda } ( E ) \exp ( - i \hbar ^ { - 1 } t E ) ,
$$

so that the width of the hat function $\Delta _ { \lambda } ( t )$ is $\hbar / \lambda$

Convenient choices for δ,(E) are families of normalized Gaussians or Lorentzians. In the latter case $\Delta _ { \lambda }$ is an exponential, so the multiplication of the hat function can be interpreted as the addition of an imaginary part to the energy. In the work of Balian and Bloch (1974) the semiclassical limit is indeed related to the analytic continuation of classical mechanics, but we shall deal here only with real systems, following Gutzwiller (1967, 1971).

The Fourier transform thus becomes

$$
\begin{array} { l } { ( 2 \pi \hbar ) ^ { - 1 } \displaystyle \int _ { - \infty } ^ { \infty } d t \Delta _ { \lambda } ( t ) \langle \pmb { \mathfrak { q } } | \hat { U } | \pmb { \mathfrak { q } } \rangle \exp ( i \hbar ^ { - 1 } t E ) } \\ { \displaystyle = \sum _ { k } \delta _ { \lambda } ( E - E _ { k } ) \langle \pmb { \mathfrak { q } } | \psi _ { k } \rangle \langle \psi _ { k } | \pmb { \mathfrak { q } } \rangle . } \end{array}
$$

For the choice $\lambda \sim \hbar$ the width of the hat does not diverge as $\hbar  0$ We can then safely use the semiclassical propagator,but this leads only to results for averages over a large number of states,since the averge energy level spacing is $( \overline { { { d } } } ) ^ { - 1 } = O ( \hbar ^ { L } )$ To single out isolated states, we must take $\lambda { = } O ( \hbar ^ { L } ) ,$ which requires an extrapolation of the semiclassical propagator. We shallfind that in some cases good results are obtained even in this limit.

Each term on the right side of(9.4) is the density matrix for a pure state $| \psi _ { k } \rangle .$ Taking the Weyl transform of the left side, we obtain a representation of the Wigner function in terms of the individual orbits in the energy shell, just as in section 8.2.It is the existence of this alternative path that permits us to avoid calculating the amplitude of the Wigner function through the iteration of the pure-state condition. Note, however,that this representation in terms of individual orbits exists even for integrable systems,as an alternative to the torus Wigner functions discussed in section 7.5.We shall study the relation between these alternative ‘representations' in the limited context of periodic orbits and the energy spectrum in section 9.4.

Let us consider the case in which ${ \mathfrak { q } } = { \mathfrak { q } }$ ： that is, we have wave intensities on the right side of(9.4). The propagator willthen be a sum of terms - one for each orbit that leaves the point q at t = O and returns after a time t. Since we integrate over alltime, we must also include the zero orbit-the orbit at any point ${ \mathfrak { q } }$ for $t = 0$ This contribution to the integral can be evaluated on its own, because allother orbits that return to ${ \mathfrak { q } }$ do so after a finite time. We found in section 7.6 that the propagator is singular as t→0, so we start from the momentum propagator <qlU|p>. For q→q we can consider H(p.q) to be a function only of the momentum; therefore.

$$
\begin{array} { c } { { \langle { \pmb p } | \hat { U } | { \bf p } \rangle \simeq \langle { \pmb p } | \mathrm { e x p } ( - i \hbar ^ { - 1 } t H ( { \hat { \bf p } } , { \bf q } ) | { \bf p } \rangle } } \\ { { = \mathrm { e x p } \{ - i \hbar ^ { - 1 } t H ( { \bf p } , { \bf q } ) \} \delta ( { \bf p } - { \bf p } ) . } } \end{array}
$$

The propagator is then the double Fourier transform

$$
\begin{array} { l } { { \displaystyle \langle { \pmb { \mathfrak { q } } } | \hat { U } ( t \to 0 ) | { \bf { q } } \rangle = ( 2 \pi \hbar ) ^ { - L } \int d { \bf { p } } d { \bf { p } } \llangle { \bf { p } } \llangle i \hat { U } ^ { - 1 } ( { \bf { p } } \cdot { \bf { q } } - { \bf { p } } \cdot { \bf { q } } ) \} \ ~ } } \\ { { \displaystyle \qquad \cdot \ } } \\ { { \displaystyle = ( 2 \pi \hbar ) ^ { - L } \int d { \bf { p } } \exp \big \{ - i \hbar ^ { - 1 } t H ( { \bf { p } } , { \bf { q } } ) \big \} \exp \big \{ i \hbar ^ { - 1 } { \bf { p } } \cdot ( { \bf { q } } - { \bf { q } } ) \big \} } . } \end{array}
$$

Introducing (9.6) into (9.4),aftertaking ${ \mathfrak { q } } = { \mathfrak { q } }$ ,leads to the contribution of the zero orbits as

$$
( 2 \pi \hbar ) ^ { - L } \int d { \bf p } \delta _ { \lambda } ( E - H ( { \bf p } , { \bf q } ) ) .
$$

We can eliminate allthe other orbits that return to $\mathbf { q }$ by choosing $\hbar \lambda ^ { - 1 }$ ， the width of $\Delta _ { \lambda } ( t ) ,$ ，smaller than the smallst time of return. In the semiclassical limit thischoice iscompatible with taking $\lambda \to 0$ in a classical energy scale; thus,

$$
( 2 \pi \hbar ) ^ { - L } \int d { \bf p } \delta ( E - H ( { \bf p } , { \bf q } ) ) = \sum _ { k } \delta _ { \lambda } ( E - E _ { k } ) | \langle { \bf q } | \psi _ { k } \rangle | ^ { 2 } .
$$

We cannot neglect the width of the peaked function on the right side, though it is of $O ( \hbar )$ since the mean level spacing is of $O ( \hbar ^ { L } )$ However,if we do enforce the limit $\lambda \to 0$ on the right, there results an (unnormalized) wave intensity for the pure state $| \psi _ { k } \rangle$ ,coincident with the projection of the energy shell Wigner function (8.1). We can therefore reinterpret this classical Wigner function as the correct semiclassical Wignerfunctionot for a pure state, but for the mixture of states in the classically narrow energy range $\lambda .$ This result holds for integrable systems as wellas ergodic systems.

Integrating (9.8) over the coordinate q results in

$$
( 2 \pi \hbar ) ^ { - L } \int d { \bf p } d { \bf q } \delta ( E - H ( { \bf p } , { \bf q } ) ) = \sum _ { k } \delta _ { \lambda } ( E - E _ { k } ) ,
$$

the Weyl rule for the density of states. In this form we can explicitly see how it describes a smoothed approximation to the level density. If we reduce the averaging width $\lambda$ beyond $O ( \hbar ) ,$ ,the hat function in (9.4) will no longer avoid the contribution of the finite orbits returning to the point q. These determine fluctuations around the Weyl rule, which will now be examined.

We can use the semiclassical propagators (7.85) directly in the integral (9.4). As the contributions of returning orbits appear only if the width of the hat function is $\hbar \lambda ^ { - 1 } \geq { \cal O } ( \hbar ^ { 0 } )$ ， we can evaluate the integral by stationary phase,considering $\Delta _ { \lambda } ( t )$ to be part of the smooth amplitude. The stationary time is determined by

$$
E + { \frac { \partial \sigma } { \partial t } } ( \mathbf { q } , \mathbf { q } , t ) = E - H ( \mathbf { p } ( \mathbf { q } ) , \mathbf { q } ) = 0 .
$$

The phase of the integral will be

$$
E t _ { E } + \sigma ( \mathbf { q } , \mathbf { q } , t _ { E } ) = S _ { E } ( \mathbf { q } , \mathbf { q } ) , \qquad .
$$

where $t _ { E }$ is the solution of (9.10) and $S _ { E }$ is the reuced ctionat isthe symplectic area subtended by the returning orbit. The contribution of each returning orbit to the wave intensity at $\ P$ therefore has the form

$$
C \left| \left( \frac { \hat { \sigma } ^ { 2 } \sigma } { \partial t ^ { 2 } } \right) ^ { - 1 } \operatorname* { d e t } \frac { \hat { \sigma } ^ { 2 } \sigma } { \partial \mathbf { q } \partial \mathbf { q } } \right| ^ { 1 / 2 } \Delta _ { \lambda } ( t _ { E } ) \exp \big \{ i \hbar ^ { - 1 } S _ { E } ( \mathbf { q } , \mathbf { q } ) \big \} .
$$

There will becomplex conjugate pairsof contributions with $\tau _ { E }$ and $- t _ { E }$ ， since the integration extends between the limits $t  \pm \infty$

Many of these contributions oscillate rapidly with q. Indeed, the phase of these oscillations is given by

$$
\frac { d S _ { E } } { d { \bf q } } = \frac { \partial S _ { E } } { \partial { \bf q } } ( { \bf q } , { \bf q } ) - \frac { \partial S _ { E } } { \partial { \bf q } } ( { \bf q } , { \bf q } ) = { \bf p } ( { \bf q } ) - { \bf p } ( { \bf q } ) .
$$

Thus, the condition for the phase of a returning orbit not to be highly oscillatory is that the returning momentum be identical to the initial momentum-only periodic orbits give stable contributions to the wave intensities!

The best manner of eliminating these rapid oscillations is to average the intensity over a region $D ^ { L }$ where $D \gg 2 \pi \hbar | { \mathfrak { p } } - { \mathfrak { p } } |$ for nonperiodic orbits, as in section 8.1. There remains only the contribution of periodic orbits superimposed on the background Weyl intensity,due to the zero-period orbits. The variations of the averaged wave intensities in the neighbourhood of periodic orbits of chaotic systems were discovered by Heler (1984), who called them scars. If the energy width λ is chosen in such a way as to include only a single return of a periodic orbit,the intensity of its scar will vary sinusodallywith energyaccording to(9.2).Fromtherelation

$$
\partial S _ { E } / \partial E = \tau _ { E }
$$

for the period of the orbit, we find that the wavelength of this oscillation is $2 \pi \hbar / \tau _ { E }$ - very long in comparison with the mean level spacing.

Integrating (9.12) over all q, we obtain the contribution of all periodic orbits to the density of states up to a maximum period of (hl-1). Again these are simple sinusoidal terms for each repetition of the orbit.The two following sections present the calculation of their amplitudes and the phase corrections due to the crossing of caustics. We will then be able to analyse the complete contribution of the multiple iterations of the same orbit.It is instructive to start with the study of simple systems with one freedom before proceeding to a general treatment.

# 9.2 The density of states for systems with one freedom

The closed level curves of the Hamiltonian of a bounded system with one freedom are themselves periodic orbits. A canonical coordinate transformation will not alter the semiclassical results, so it is convenient to use the coordinates (J,0), introduced in section 2.5, where 2πJ is the area inside a periodic orbit and

$$
\dot { \theta } = \partial H / \partial J = \omega ( J )
$$

is a constant, since $H = H ( J )$

The complete action $\sigma ( \Theta , \theta , t )$ supplies the usual relations

$$
\partial \sigma / \partial \Theta = \Im , \qquad \partial \sigma / \partial \theta = - J .
$$

On the other hand, integrating (9.15), we hve

$$
\omega ( J ) = ( \Theta - \theta ) / t .
$$

Therefore

$$
\left| \frac { \partial ^ { 2 } \sigma } { \partial \Theta \partial \theta } \right| = \frac { 1 } { t } \frac { d J } { d \omega } .
$$

Combining this result with

$$
{ \frac { \partial ^ { 2 } \sigma } { \partial t ^ { 2 } } } = - { \frac { \partial E } { \partial J } } { \frac { \partial J } { \partial t } } = \omega { \frac { \partial J } { \partial \omega } } { \frac { \Theta - \theta } { t ^ { 2 } } } ,
$$

for m complete repetitions of the periodic orbit $( \Theta - \theta = m _ { 2 } \pi$ and $t = m \tau$

we obtain the amplitude in (9.12) as

$$
\left| \frac { \partial ^ { 2 } \sigma } { \partial { \sf q } \partial \boldsymbol { q } } { \left( \frac { \partial ^ { 2 } \sigma } { \partial t ^ { 2 } } \right) } ^ { - 1 } \right| ^ { 1 / 2 } = \frac { \tau } { 2 \pi } . \qquad .
$$

Thus,the contributions of each return of the periodic orbit have the same amplitude, in the case of a single freedom. If there is a single orbit witha given energy,the density of states will depend on the phase difference for successive returns of this orbit. It then becomes important to determine the constant in equation (9.12), or at least its phase. Provided that the Hamiltonian has the form $p ^ { 2 } / 2 m + V ( q )$ ，the phase correction for the propagator will be $- \pi / 4 - \mu \pi / 2$ where $\mu$ is the number of caustics crossed by the orbit, according to the discussion in section 7.6. The integral over t furnishes a further $\pi / 4$ times the sign of $\partial ^ { 2 } \sigma / \partial t ^ { 2 }$ ,that is, the sign of $\partial \omega / \partial J .$ It is now important to consider carefully the change of variables $( p , q ) $ $( J , \theta )$ The problem is that this transformation alters the topology of the phase space -in the new variables there is no focal point where $\partial \Theta / \partial J =$ 0, but in the Cartesian coordinates, the return of two neighbouring orbits separated by $\delta E$ entails the crossing of at least one focal point, where $\partial \Theta / \partial p = \partial \Theta / \partial J = 0$ (fig.91) There will be only one point if $\partial \omega / \partial J < 0$ ， whereas $\partial \omega / \partial J > 0$ corresponds to the existence of a pair of focal points for each winding of the orbit. Hence, the total phase correction for $m$ repetitions is $- m \pi$ , whatgver the sign of $\hat { c } \omega / \hat { c } J$

![](images/832472b4361ec5543c77cd416adaffd52df5417d8b6e28fb529e7f12cddc648f.jpg)  
Fig9.1.J The return of two neighbouring orbits separated by δE entails the crossing $\mathrm { F i g } \textcircled { 9 . 1 }$ of at least one focal point. The orbit starting at qo with energy E has focal points at $q _ { 1 }$ and $q _ { 2 }$

The contribution to the density of states of the mth return of the periodic orbit with energy E is the result of integrating (9.12) along the orbit. Since the integrand is independent of $\theta$ ,we obtain

$$
( 2 \pi \hbar ) ^ { - 1 } \tau _ { E } \exp ( i \hbar ^ { - 1 } m S _ { E } - m \pi ) \Delta _ { \lambda } ( m \tau _ { E } ) ,
$$

where m ranges between - o and + oo.We can also include m =0-this is just the Weyl term,as can be seen by integrating the left side of (9.9) and then using (9.14). Taking then the limit λ→0 and summing over all the repetitions with the help of the Poisson identity (8.67) results in the density of states formula

$$
d ( E ) = \hbar ^ { - 1 } \tau _ { E } \sum _ { n } \delta ( \hbar ^ { - 1 } S _ { E } - ( 2 n + 1 ) \pi ) = \sum _ { n } \delta ( E - E _ { n } ) .
$$

The equivalence between the periodic orbit formalism and Bohr-Sommerfeld quantization for one freedom was proved by Berry and Mount (1972) from the Green function

$$
G ( \mathfrak { q } , \mathfrak { q } , E ) = ( i \hbar ) ^ { - 1 } \int _ { 0 } ^ { \infty } d t \exp \left\{ i \hbar ^ { - 1 } ( E + i \varepsilon ) t \right\} \langle \mathfrak { q } | \hat { U } ( t ) | \mathfrak { q } \rangle ,
$$

where $\varepsilon$ is a positive infinitesimal number. The equality

$$
( - \pi ) ^ { - 1 } \operatorname { I m } G ( \mathfrak { q } , \mathfrak { q } , E ) = \sum _ { n } \langle \mathfrak { q } | \psi _ { n } \rangle \langle \psi _ { n } | \mathfrak { q } \rangle \delta ( E - E _ { n } )
$$

can be used as an alternative basis for the treatment of scars and the spectrum. I have avoided this intermediate stepbecause the propgator seems more intuitively accessible. Furthermore, there is the problem of the caustics. For one freedom there is actually an advantage to using the Green function -its caustics coincide with the turning points of the periodic orbit rather than the more subtle focal points of the propagator. However, in the general case the phase corrections are supplied directly by the Morse index, whereas the calculation of the phase of the Green function can be much more complicated. This subject is discussed by Mohring,Levit and Smilansky (1980).

# 9.3 Contribution of stable and unstable orbits

Periodic orbits of a system with two or more freedoms appear typically in one-parameter families. For an integrable system there will be $L - 1$ further parameters, since we then have one-parameter families of periodic tori, but in this section we shall consider only periodic orbits that are isolated on each energy shell. The one-parameter family forms a twodimensional annulus y in phase space. It was shown in section 2.5 that we can make a coordinate transformation (p,q)→(J,0,P,Q) to new canonical coordinates based on theannulus,such that 2πJ is the symplectic area for each orbit and θ = 2π/t. As a consequence of this transformation

$$
 \frac { \partial H } { \partial \mathbf { P } } | _ { \gamma } = \frac { \partial H } { \partial \mathbf { Q } } | _ { \gamma } = 0
$$

and hence

$$
\frac { d \omega } { d { \bf Q } } \bigg | _ { \gamma } = 0 .
$$

Combining this equation with (9.16) and (9.17), which are stil valid on $\gamma$ (i.e., for $\mathbf { P } = \mathbf { Q } = 0$ ,we obtain

$$
\frac { \hat { \partial } ^ { 2 } \sigma } { \partial \theta \partial { \bf Q } } = \frac { \hat { \partial } J } { \partial { \bf Q } } = 0
$$

on each periodic orbit. The full action function for a return to $\mathfrak { q }$ after $m$ windings in the neighbourhood of a periodic orbit thus takes the form

$$
\sigma _ { m } (  { \mathbf { q } } ,  { \mathbf { q } } ) = \int _ { 0 } ^ { 2 \pi m } J d \theta + S _ { m } (  { \mathbf { Q } } ,  { \mathbf { Q } } ) - m \tau H .
$$

The second term is a particular case $\mathbf { a } = \mathbf { Q }$ ）of the transverse action

$$
S _ { m } ( \Omega , { \bf Q } ) = \int _ { { \bf Q } } ^ { \Omega } { \bf P } \cdot d { \bf Q }
$$

taken along the orbit. This is not necessarily the generating function for the Poincare map, since $S _ { m }$ defines a transformation for fixed time. However, the two actions can be identified by choosing the coordinates so that $\dot { \mathbf { Q } } = \dot { \mathbf { P } } = 0$ near the point $\mathbf { q }$ . Along $\gamma$ ,thefirstterm in （9.28)reduces to $2 \pi m J$ but $J$ varies along the orbit if $\mathbf Q \neq 0$

The determinant of $\partial ^ { 2 } \sigma / \partial { \big / } { \mathfrak { q } } \partial { \big . } { \mathfrak { q } }$ factorizes into a longitudinal term, calculated in the previous sectionand a transverse erm:

$$
\left| { \operatorname* { d e t } \frac { \hat { c } ^ { 2 } \sigma } { \hat { \sigma } { \bf q } \hat { \sigma } { \bf q } } \left( \frac { \hat { c } ^ { 2 } \sigma } { \hat { \sigma } t ^ { 2 } } \right) ^ { - 1 } } \right| ^ { 1 / 2 } = \frac { \tau _ { E } } { 2 \pi } \left| { \operatorname* { d e t } \frac { \hat { \sigma } ^ { 2 } S _ { \bf m } } { \hat { \sigma } \Omega \hat { \sigma } { \bf Q } } } \right| ^ { 1 / 2 } .
$$

We can trivially integrate (9.12)over $\theta$ , so the contribution of a periodic orbit to the density of states has the form

$$
( 2 \pi \hbar ) ^ { - 1 } \tau _ { E } A _ { m } \exp \left\{ i ( \hbar ^ { - 1 } m S _ { E } - m \pi - \mu \pi / 2 ) \right\} \Delta _ { \lambda } ( m \tau _ { E } ) .
$$

The amplitude $A _ { m }$ is defined as the traceof the unitary operator $\hat { U } _ { \mathrm { { P } } }$

associated withthe classical Poincare map,as discussed insection 7.6

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { m } = \int d { \bf Q } \langle { \bf Q } | \hat { U } _ { \mathrm { p } } | { \bf Q } \rangle } } \\ { ~ } \\ { { \displaystyle ~ = ( 2 \pi \hbar i ) ^ { - ( L - 1 ) / 2 } \int d { \bf Q } \left. \operatorname* { d e t } \frac { \hat { \partial } ^ { 2 } S _ { m } } { \partial \pm \hat { \bf Q } \partial { \bf Q } } \right. ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } S _ { m } ( { \bf Q } , { \bf Q } ) \right\} } . }  \end{array}
$$

The phase correction in (9.31) has now been separated into two terms. The first,mπ,has already been discussed in section 9.2-each focal oint in the y annulus will be a general focal point, since 0²o/dq dq separates into two blocks. The other phase correction is determined by $\mu _ { m }$ the number of singular points of $\partial ^ { 2 } S / \partial \Omega \partial Q$ traversed by $m$ windings of the periodic orbit.

By construction,the origin is a fixed point of the Poincare map. Its generating function has no linear part,and the quadratic part defines the linearizedmapandthesabilitymatrix.Henceforthwesallelly with the case where $L = 2$

# Exercise

Using (8.71), show tt

$$
\frac { d ^ { 2 } S _ { m } } { d Q ^ { 2 } } ( Q , Q ) = \operatorname * { d e t } ( \mathcal { M } ^ { m } - \mathbf { 1 } ) \frac { \partial ^ { 2 } S _ { m } } { \partial \Omega \partial { \bf Q } } .
$$

In the usual case where $( \partial \Omega / \partial P ) _ { Q } ^ { - 1 } = ( \partial ^ { 2 } S / \partial \Omega \partial Q ) > 0$ ,the sign of the second derivative of $S _ { m }$ will be the opposite of $\operatorname* { d e t } ( \mathcal { M } ^ { m } - \mathbb { 1 } )$ Therefore, $d ^ { 2 } S _ { m } / d Q ^ { 2 } < 0 .$ if ${ \mathcal { M } } ^ { m }$ determines a direct hyperbolic map, whereas $d ^ { 2 } S _ { m } / d Q ^ { 2 } > 0$ in the case of an elliptic map or of a hyperbolic map with a reflexion.

Evaluation of(9.32) by stationary phase is tantamount to approximating $S _ { m }$ by its quadratic terms; therefore,

$$
A _ { m } = \left[ \begin{array} { r } { 1 } \\ { - i } \end{array} \right] | \operatorname* { d e t } ( \mathcal { M } ^ { m } - \mathbf { 1 } ) | ^ { - 1 / 2 } ,
$$

where the prefactor is only 1 in the case of a direct hyperbolic point. In this case the stability matrix will have the eigenvalues $( e ^ { m \alpha } , e ^ { - m \alpha } )$ where $\alpha$ is the Lyapunov exponent, so the amplitude assumes the form

$$
A _ { m } = | 2 \sinh ( m \alpha / 2 ) | ^ { - 1 } ,
$$

first obtained by Gutzwiller (1971). The index $\mu _ { m } = 0$ , provided that the motion is hyperbolic along the entire orbit. For a hyperbolic map with

reflection (Tr.M <-2),the amplitude willbe given by (9.35) if mis even because Hm will then determine a direct hyperbolic map. For m odd, the eigenvalues will be $( - e ^ { m \alpha } , - e ^ { - m \alpha } )$ and therefore

$$
A _ { m } = \{ 2 i \cosh ( m \alpha / 2 ) \} ^ { - 1 } .
$$

The eigenvalues for a linearly stable map have the form $( e ^ { i \beta } , e ^ { - i \beta } )$ ;hence,

$$
A _ { m } = - i | 2 \sin ( m \beta / 2 ) | ^ { - 1 } .
$$

The amplitudes for the three cases above are not valid if $\alpha$ or $\beta$ is very small. For the elliptic point we are also faced with a small-denominator problem in exact analogy to classical mechanics. The singularities in $A _ { m }$ arise for $\beta = 2 n \pi$ .Then the linearized Poincare map for the nth return degenerates into the identity map - the sign of a periodic orbit resonance. The linear approximation thus surrounds the central periodic orbit with a continuum of periodic orbits, contradicting our assumption that the periodic orbit was isolated. It will be shown in section 9.4 that this difficulty can be surmounted by including the nonlinear terms of the resonant normal form studied in section 4.4.

Resonances are zeros of $\partial ^ { 2 } S / \partial \Omega \partial \mathbf { Q }$ for $\mathfrak { Q } = \mathbf { Q }$ .Similar zeros along the orbit lead to phase corrections of $\pi / 2$ . It will be shown at the end of this section that these corrections can be incorporated into a new amplitude

$$
A _ { m } ^ { - 1 } = 2 i \sin ( m \beta / 2 )
$$

(with no modulus sign) within the periodic orbit contribution

$$
( 2 \pi \hbar ) ^ { - 1 } \tau _ { E } A _ { m } \exp \left\{ i m ( \hbar ^ { - 1 } S _ { E } - \pi ) \right\} \Delta _ { \lambda } ( m \tau _ { E } ) .
$$

This formula differs from (9.31) by theabsence of the explicit Morse phase due to tranvesecaustics.Itisalidoanysolatedobitsrting(8) (9.36) or (9.35) for $A _ { m }$ .The unidimensioal psesmπ,troducedbyile (1975), must be t.

For one freedom the periodic orbit is the energy shellitself; then the density of states depends only on successive returns of a single orbit. As the phase spceimensioalityisieased,thereuallypersothe energy shell an infinity of periodic orbits with arbitrarily long period. The sum of the succesive repetitions of a single periodic orbit supplies the total intensity of its scar,which is just (9.39)divided by 2π.The density of states depends collectively on the interference between the total contribution of all the periodic orbits in the shell.

The total contribution of an unstable periodic orbit is absolutely convergent and tends to zero as $\alpha  \infty$ .In the particular case of free motion on a surface of constant negative curvature, the periodic orbit sum is actually exact-it corresponds to the Selberg trace formula (see the review article by Balazs and Voros, 1986). For |mα| large, we can approximate 2 sinh(|mαl/2) by exp(|mαl/2) and hence sum the resulting geometric series. Yet it is precisely the orbits with a small Lyapunov exponent that will have strong scars.So it is preferable to use

$$
{ \frac { 1 } { 2 \sinh ( | m \alpha | / 2 ) } } = { \frac { \exp ( - | m \alpha | / 2 ) } { 1 - \exp ( - | m \alpha | / 2 ) } } = \sum _ { n = 0 } ^ { \infty } \exp \left\{ - ( n + { \frac { 1 } { 2 } } ) | m \alpha | \right\} .
$$

It is now convenient to choose an exponential form for the hat function $\Delta _ { \lambda } ( t )$ The total intensity of a scar is then

$$
{ \mathrm { R e } } ( 2 \pi ^ { 2 } \hbar ) ^ { - 1 } \tau _ { E } \sum _ { n = 0 , m = 1 } ^ { \infty } \exp \big \{ i m [ ( \hbar ^ { - 1 } S _ { E } - \pi ) + i ( n + { \textstyle \frac { 1 } { 2 } } ) { \alpha } + i \hbar ^ { - 1 } \tau _ { E } \lambda ] \big \} .
$$

Summing the geometric series in $m$ ,this becomes

$$
\mathsf { R e } ( 4 \pi ^ { 2 } \hbar ) ^ { - 1 } \tau _ { E } \sum _ { n } \left( - 1 + i \cot \{ 2 ^ { - 1 } [ ( \hbar ^ { - 1 } S _ { E } - \pi ) + i ( n + \frac { 1 } { 2 } \alpha ) + i \hbar ^ { - 1 } \tau _ { E } \lambda ] \} \right) ,
$$

and using the expansion of the cotangent in partial fractions,

$$
\cot z = \sum _ { k = - \infty } ^ { \infty } ( z - k \pi ) ^ { - 1 } ,
$$

the intensity of a scar takes the final form

$$
( 4 \pi ^ { 2 } \hbar ) ^ { - 1 } \tau _ { E } \sum _ { n } \Bigg \{ - 1 + \sum _ { k } \frac { 2 ( n + \frac { 1 } { 2 } ) \alpha + 2 \hbar ^ { - 1 } \tau _ { E } \lambda } { [ \hbar ^ { - 1 } S _ { E } - 2 ( k + \frac { 1 } { 2 } ) \pi ] ^ { 2 } + [ ( n + \frac { 1 } { 2 } ) \alpha + \hbar ^ { - 1 } \tau _ { E } \lambda ] ^ { 2 } } \Bigg \} .
$$

The $n = 0$ term corresponds to a set of Lorentzian peaks in energyfirst obtained by Heller (1984). The energy interval between the peaks is $2 \pi \hbar / \tau _ { E }$ ， using (9.14), and the width of each peak is $\lambda + \hbar ( n + \frac { 1 } { 2 } ) \alpha / \tau _ { E }$ .Even in the limit $\lambda \to 0$ ,we obtain broad peaks - an unstable periodic orbit is not tied to a single eigenenergy. The width of the peak is of $O ( \hbar ) ,$ whereas the level spacing is of $O ( \hbar ^ { L } )$ .The distribution of the positive contributions to the scar intensity among the many states in an energy peak is still not known. Between the peaks the total contribution of the scars is negative, so that for these energies the orbits contribute weak antiscars. Thus, even partially smoothed wave intensities will show multiple oscillatons, corresponding to the scars and antiscars of the myriad periodic orbits, superimposed on the smooth Weyl distribution.

The terms with n >O in (9.44) bring quantitative corrections to the density of states. Further, broader Lorentzians with peaks at the same energies are added. For

$$
( n + \frac { 1 } { 2 } ) x > 2 \pi
$$

the tails of the periodic Lorentzians will begin to superimpose, so that (9.44) loses its usefulness as a representation of the scar intensity, more easily obtained from (9.41). So if (9.45) is satisfied even with $n = 0$ ,the scar intensity is weak and sinusoidal. If (9.45) is satisfied only for $n = 0$ we obtain the Lorentzian profile with a weak sinusoidal correction (with the same maxima as the Lorentzians) due to the $n = 1$ term. For strong scars we have to add other Lorentzians up to the (9.45) limit. It follows that the energy width of a scar does not diminish by approaching a resonance with $\alpha \to 0$ ， Note that very close to this limit the linear approximation on which this whole discussion is based ultimately breaks down.

The intensity of a scar due to a stable periodic orbit can be treated in a similar manner, using the analytic continuation of (9.4O) as proposed by Miller (1975). The orbit intensity is then given formally by

$$
{ \tt R e } { ( 2 \pi ^ { 2 } \hbar ) } ^ { - 1 } \tau _ { E } \sum _ { n = 0 } \sum _ { n = 1 } \exp \big \{ i m [ \hbar ^ { - 1 } S _ { E } - \pi - ( n + { \textstyle \frac { 1 } { 2 } } ) \beta + i \hbar ^ { - 1 } \tau _ { E } \lambda ] \big \} ,
$$

which can be summed over $m _ { s }$ yielding

$$
4 \pi ^ { 2 } \hbar ) ^ { - 1 } \tau _ { E } \sum _ { n = 0 } \left\{ - 1 + \sum _ { k } { \frac { 2 \hbar ^ { - 1 } \tau _ { E } \lambda } { [ \hbar ^ { - 1 } S _ { E } - 2 ( k + { \frac { 1 } { 2 } } ) \pi - ( n + { \frac { 1 } { 2 } } ) \beta ] ^ { 2 } + ( \hbar ^ { - 1 } \tau _ { E } \lambda ) ^ { 2 } } } \right\}
$$

as the scar intensity.Thedensityof states is obtained bymultiplying(9.47) by $2 \pi$ This time wedo obtain quantized energy levels as $\lambda \to 0$ determined by the conditions

$$
S _ { E } = \hbar \{ 2 ( k + \frac { 1 } { 2 } ) \pi + ( n + \frac { 1 } { 2 } ) \beta \} .
$$

The convergenceof (9.47)is justas trickyas theoriginal sum,since the series in n cannot be truncated in this case. Even so the quantization condition (9.48) has a simple interpretation, based on the fact that the motion in the neighbourhood of a stable periodic orbit is at least quasi-integrable. It follows that the energy levels are supplied approximately by the quantization conditions of section 7.3. The orbit is surrounded by thintoriwithacion riablesJand Iespectivelylong the orbit and transverse to it, that is 2πJ = SE for I=O; a neighbouring torus will have a small value of I,and 2πJ will be close to SE. The quantization condition is that both I and J are a half-integer multiple of h, so the periodic orbit itself is not directly tied to a quantum state. Given a torus with J correctly quantized, the action variable for the orbit with the same energy is approximately

$$
J _ { \mathrm { o r b i t } } = ( k + \textstyle { \frac { 1 } { 2 } } ) \hbar + ( n + \textstyle { \frac { 1 } { 2 } } ) \hbar \frac { \partial H / \partial I } { \partial H / \partial J }
$$

for small $n$ .This result agrees with (9.48) because

$$
\frac { \partial H / \partial I } { \partial H / \partial J } = \frac { \dot { \phi } } { \dot { \theta } } = \frac { \beta } { 2 \pi } .
$$

The double infinity of levels given by (9.48) for each stable periodic orbit results from an unwarranted extrapolation of the linear approximation, valid only in the neighbourhood of the orbit. For n suficiently large,the frequencies of the enveloping tori areno longer constantand

![](images/72ff1c3c639696286d30ee64ee7b88f50f0347cf1645aeb60d080d484f328ab0.jpg)

Fig9.2.1f $( \hat { o } \pmb { \Omega } / \hat { o } P ) _ { Q } > 0$ as $m \beta \to 0 ^ { + }$ ,then $( \partial \Omega / \partial P ) _ { Q } < 0$ for $m \beta > \pi$ farther out they may cease to exist. Even so it is encouraging that we return approximately to valid quantization conditions by formally resumming the contributions of isolated periodic orbits.

To close this section,it remains only to justify the simplification achieved by Gutzwiller (1971) of the contribution of the mth return of a periodic orbit into (9.38) and (9.39),in spite of the transverse caustics. We obtained (9.37) under the assumption that $( \partial \Omega / \partial P ) _ { Q } > 0$ .However,fig.9.2sows that if the direction of increasing stability angle $m \beta$ is chosen to confirm this hypothesis as $m \beta \to 0 ^ { + }$ , it is falsified for $m \beta > \pi$ But for $m \beta = \pi$ $\partial ^ { 2 } S / \partial \Omega \partial Q = 0$ ,so we have the first focal point. The consequences of $m \beta$ passing through $\pi$ are then that the prefactor in (9.34) changes from $- i$ to 1,while we must add the first Morse phase correction of $- \pi / 2$ .When $m \beta$ passes through $2 \pi .$ $\partial \Omega / \partial P$ becomes positive again,but now the orse index is 2. Thus, the total contribution never changes phase at the odd-numbered caustics,whereas the phase change at the even caustics is $\pi$

This result, incorporated into (9.38) and (9.39), is in agreement with the general rule that phase changes always accompany traversals through singularities. It is only the even caustics that lead to singular contributions to the density of states. The linearized approximation blows up there because it generates a continuum of periodic orbits with which it is unable to cope.

# 9.4 Amplitude of nonisolated orbits

The foregoing analysis holds only for isolated fixed points of the mth iterationof the Poincaremap.This fact ismadeevidentby thealternative form of the amplitude (9.32):

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { m } = \int d { \bf P } d { \bf Q } \langle { \bf Q } | \hat { U } _ { \mathrm { P } } | { \bf P } \rangle \langle { \bf P } | { \bf Q } \rangle } } \\ { { \displaystyle ~ = ( 2 \pi \hbar ) ^ { - ( L - 1 ) } \int d { \bf P } d { \bf Q } \left| \operatorname* { d e t } \frac { \hat { \partial } ^ { 2 } S _ { m } } { \hat { \partial } { \bf Q } \hat { c } { \bf P } } \right| ^ { 1 / 2 } \exp \left\{ - i \hbar ^ { - 1 } \left[ S _ { m } ( { \bf Q } , { \bf P } ) - { \bf P } \cdot { \bf Q } \right] \right\} } . }  \end{array}
$$

In the case that Up is the identitythe semiclassical form for <QlUp|P> is exact, since Sm(Q,P)=P·Ω. Near the identity, this representation of the evolution operator has no caustics (hence, the real amplitude). The great advantage is that the Poincare map is here given implicitly by

$$
\frac { \partial S _ { m } } { \partial \boldsymbol { \Omega } } ( \boldsymbol { \Omega } , \mathbf { P } ) = \mathfrak { P } , \qquad \frac { \partial S _ { m } } { \partial \mathbf { P } } ( \boldsymbol { \Omega } , \mathbf { P } ) = \mathbf { Q } ,
$$

so the fixed points correspond to the points of stationary phase in (9.51). If the fixed points are separated by many wavelengths, we can evaluate (9.51) by stationary phase,recovering the results in section 9.3. Otherwise, we must keep the nonquadratic terms of the action Sm needed to describe corectly the fixed points，that is，the periodic orbits that contribute collectively to a single scar or to the density of states.

# Exercise

Deduce (9.51) directly from the mixed representation of the evolution operator

$$
\langle \boldsymbol { \mathfrak { q } } , \boldsymbol { \mathfrak { Q } } | \hat { U } ( t ) | \boldsymbol { q } , \mathbf { P } \rangle = \int d \boldsymbol { q } ^ { \prime } d \mathbf { Q } ^ { \prime } \langle \boldsymbol { \mathfrak { q } } , \boldsymbol { \mathfrak { Q } } | \hat { U } ( t ) | \boldsymbol { q } ^ { \prime } , \boldsymbol { Q } ^ { \prime } \rangle \langle \boldsymbol { q } ^ { \prime } , \mathbf { Q } ^ { \prime } | \boldsymbol { q } , \mathbf { P } \rangle .
$$

In the semiclassical limit,only orbits very close to each other will give a collective contribution; this will happen near a bifurcation of an isolated periodic orbit.The resonant normal forms for generic bifurcations of stable periodic orbits were studied in section 4.4. The complete classification by Meyer (1970) for systems with two freedoms is depicted in fig $\textcircled{4.9}$ In principle, all that is needed is to substitute the quadratic approximation for $S _ { m }$ by the action corresponding to the appropriate normal form. In each case we have to deal with the mth iteration of the Poincaré map in the neighbourhood of a periodic orbit whose stability angle $\beta$ is very close to $2 \pi / m$ For $m = 1$ the integral (9.51) becomes the Airy integral,discused in section 7.2. For $m = 2$ and 3 we obtain higher diffraction catastrophe integrals (the cusp $A _ { 2 }$ for $m = 2$ and the elliptic umbilic $D _ { 4 } ^ { - }$ for $m = 3$ presented in section 6.3. For $m = 4$ the corresponding catastrophe is $X _ { 9 }$ ， the first one with a continuous parameter in the classification of Arnold (1975). This is the parameter $K$ in the function $x ^ { 4 } + y ^ { 4 } + K x ^ { 2 } y ^ { 2 }$ .Figure 4.9 shows both cases depending on whether $K$ is greater or smaller than $^ { - 2 }$

All the cases where $m \geq 5$ are better treated in polar coordinates, for which the amplitude becomes

$$
{ \cal A } _ { m } = ( 2 \pi \hbar ) ^ { - 1 } \int d I d \phi \left| { \frac { \partial ^ { 2 } S _ { m } } { \partial I \partial \phi } } \right| ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } [ S _ { m } ( I , \phi ) - I \phi ] \right\} .
$$

The normal form for the map $( I , \phi )  ( \Im , \Phi )$ has the generating function

$$
S _ { m } ( I , \Phi ) - I \Phi = \varepsilon I + c I ^ { 2 } + a I ^ { m / 2 } \sin ( m \Phi ) .
$$

The resonance or bifurcation occurs for $\varepsilon = 0$ when satellite fixed points of the Poincare section coalesce with the fixed point at the origin. Figure 9.3 shows the Mexican hat’ shape of the action $S _ { m }$ ,whose relative extrema at the centre and along the rim determine the periodic orbits. Inserting (9.55) into (9.54) and integrating over $\phi$ ,we obtain

![](images/b4fbde585293b59a8fd56b7f5024081872ab5091f57cefce2efd2d3528e99242.jpg)  
Fig9.3The action $S _ { m }$ has the shape of a Mexican hat. If the dimples along the rim are sufficiently small,the rim contributes as a full torus would rather thanas a pair of orbits. If the whole hat is suficiently small,the central periodic orbit cannot be separated from its satellites.

$$
{ \cal A } _ { m } = \hbar ^ { - 1 } \int _ { 0 } ^ { \infty } d I J _ { 0 } ( \hbar ^ { - 1 } a I ^ { m / 2 } ) \exp \big \{ i \hbar ^ { - 1 } ( \varepsilon I + c I ^ { 2 } ) \big \} ,
$$

where $J _ { 0 }$ is the zeroth-order Bessel function.

The uniform approximation of this amplitude for allε is furnished by Ozorio de Almeida and Hannay (1987). Here we shall discuss only the qualitative differences between the possible regimes. In the special case when $a = 0$ ,the Bessel function $J _ { 0 } = 1$ (the rim of the ‘Mexican hat’ is smooth). The integral then has a stationary phase for $I = I _ { 0 } = - \varepsilon / 2 c$ ， corresponding to the small torus of periodic orbits in the Birkhoff normal form. There are two regimes: If $\hbar ^ { - 1 } \varepsilon \gg 1$ , the contribution of the torus and the central orbit can be separated. Alternatively, near a bifurcation $( \hbar \varepsilon \ll 1 )$ the torus and the central orbit contribute together. The important point is that these results are not fundamentally altered even if $a \neq 0$ as long as $\hbar ^ { - 1 } a \ll 1$ .Classically the torus of periodic orbits is substituted by a single pair ofstable and unstable orbits,no matter how small the constant $^ a$ ；but in the semiclassical limit $J _ { 0 } \to 1$ smoothly. We can thus describe the semiclassical amplitude in terms of a quasi-torus with action $I _ { 0 }$ .In the regime where $\hbar ^ { - 1 } a \gg 1$ ，we can approximate

$$
J _ { 0 } ( x ) \mathop { \longrightarrow } _ { x \to \infty } { \left( \frac { 2 } { \pi x } \right) } ^ { 1 / 2 } \cos { \left( x - \frac { \pi } { 4 } \right) } ,
$$

accordingtoramowitzandStegun(964).setigthsto(9.),t results a pair of oscillatory integrals.

# Exercise

Show that both integrals,approximated by the stationary-phase method, provideamplitudes corresponding to the satelliteorbits.[Thecontribution of the end point ${ \cal I } = 0$ in(9.56)stlablei

One can readily adapt methods described above to the transition from an integrable to a quasi-integrable system. The main point is to note that the amplitude in section 9.2 and 9.3 was already defined in terms of the partial action-angle variables $( J , \theta )$ forafamily of periodic orbits.Consider now an integrable system with Hamiltonian $H ( \Im )$ It is not usually true that the periodic orbits of a given torus with commensurate frequencies have the same topology as either of the two irreducible circuits,defining the actions J, and J2. However, there always exists a canonical transformation (presented in section 6.4) to new action-angle variables, such that one pair becomes precisely the variables $( J , \theta )$ for the periodic orbit. The remaining conjugate pair $( I , \phi )$ determines the transverse motion. Inverting the equation $H ( J , I ) = E$ ，we obtain the reduced Hamiltonian $J ( I ; E )$ . It was shown in section 2.5 that the orbits are then furnished by Hamilton's equations

$$
\frac { d I } { d ( - \theta ) } = - \frac { \partial J } { \partial \phi } , \qquad \frac { d \phi } { d ( - \theta ) } = \frac { \partial J } { \partial I } .
$$

Now the Poincare map of the full system becomes just the stroboscopic map $( - \theta ) = 2 \pi$ of the reduced system. For an integrable system, $J$ is independent of $\phi$ ,so the flow reduces to a horizontal shear. The generating function for the corresponding stroboscopic map can then be obtained exactly:

$$
m 2 \pi J ( I ; E ) = S _ { m } ( I , \phi ) - I \phi .
$$

The right side of (9.59) is just the phase that has to be inserted in (9.54) for the amplitude to be evaluated. The left side is independent of $\phi$ ,sO we can immediately integrate over this variable, obtaining an amplitude like (9.56) with $a = 0$ ,that is,the amplitude for the Birkhoff normal form near an isolated periodic orbit. This is just as expected, since the Birkhoff normal form is an example of an integrable system. There is, however, a detail that should not be overlooked: In the previous treatment, the overall phase of the contribution was that of the central periodic orbit, even if the stationary torus were to contribute separately， since the torus was assumed to be close to the central orbit. In general it is preferable that the overall phase refer to the periodic orbits in the torus with action $I _ { 0 }$

It is therefore necessary to subtract the difference in phase between the origin and the torus, which is exactly $m 2 \pi J ( I _ { 0 } )$ The torus amplitude is thus

$$
\begin{array} { l } { { A _ { m } = \hbar ^ { - 1 } \displaystyle \int _ { 0 } ^ { \infty } d I \exp \left\{ i \hbar ^ { - 1 } m 2 \pi [ J ( I ) - J ( I _ { 0 } ) ] \right\} } } \\ { { \displaystyle ~ = 2 \pi | m \hbar \frac { \hat { \sigma } ^ { 2 } J } { \hat { \sigma } I ^ { 2 } } ( I _ { 0 } ) | ^ { - 1 / 2 } \exp ( i \nu \pi / 4 ) , } } \end{array}
$$

where $\nu$ is the sign of the second derivative. It is important to note that the torus amplitude is of $O ( \hbar ^ { - 1 / 2 } )$ and therefore larger than that of an isolated periodic orbit.

The amplitudes of periodic tori in the density of states formula for an integrable system were first obtained by Berry and Tabor (1976). The method they used was the inverse of the transformation to the torus quantization conditions, which we made in section 9.2 for the particular case of one freedom.

In the case of a quasi-integrable system with the Hamiltonian $H =$ $H _ { 0 } ( J , I ) + \varepsilon H _ { 1 } ( J , I , \theta , \phi ) ,$ ， we can also define the reduced Hamiltonian

$$
J = J _ { 0 } ( I ; E ) + \varepsilon J _ { 1 } ( I , \phi ; - \theta , E ) .
$$

However,therelationbetweenthereduced Hamiltonianand the generating function is no longer given by (9.59).

# Exercise

Show that up to first order in the perturbation parameter the generating function $s _ { m }$ for the Poincaré map is given by

$$
m 2 \pi \overline { { { J } } } \equiv \int _ { 0 } ^ { \infty m 2 \pi } J ( I , \phi + \omega _ { 0 } \theta ; - m 2 \pi + \theta , E ) d \theta = S _ { m } ( I , \phi ) - I \phi ,
$$

where $\omega _ { 0 } = d J _ { 0 } / d I$ .Near the periodic torus, this definition of $\bar { J }$ is equivalent to that obtained by first averaging the full Hamiltonian $H$ over the fast variable $\theta$ as in section 6.5.

The perturbation adds a periodic term to the phase of the integrand of the amplitude formula. For a simple Chirikov resonance

$$
\begin{array} { r } { \overline { { J } } ( I , \phi ) = J ( I ) + \varepsilon \cos \phi , } \end{array}
$$

we obtain the amplitude

$$
A _ { m } = 2 \pi \left| m \hbar \frac { \hat { \sigma } ^ { 2 } \overline { { J } } } { \partial I ^ { 2 } } ( I _ { 0 } ) \right| ^ { - 1 / 2 } J _ { 0 } ( m 2 \pi \hbar ^ { - 1 } \varepsilon ) \exp { \left( \frac { i \nu \pi } { 4 } \right) } .
$$

Again,the asymptotic form (9.57) of the essel function,for sufficiently large perturbation parameters ε as compared with h, results in distinct contributions for each isolated periodic orbit that survives the destruction of the torus Io.Generally there will be an arbitrary periodic term F(I,Φ) instead of the cosine in (9.63).Integrating first over the action I,we obtain

$$
A _ { m } = \int _ { 0 } ^ { 2 \pi } d \phi \left| m \hat { h } \frac { \hat { d } ^ { 2 } \overline { { { J } } } } { d I ^ { 2 } } \right| ^ { - 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } m 2 \pi [ \overline { { { J } } } ( I ( \phi ) , \phi ) - J ( I _ { 0 } ) ] + \frac { i \nu \pi } { 4 } \right\} ,
$$

where $I ( \phi )$ is defined by $\partial J / \partial I = 0$ . A uniformapproximation to (9.65)is suppliedbyOzoriode Almeida(1986).Thecontributionsof thesurviving periodic orbits willbe isolated only if te phase diference between the maxima and minima of the exponent in (9.65) is much greater than $2 \pi$

$$
\begin{array} { r l } { m \Delta \bar { J } \ll \hbar \quad } & { ( \mathrm { q u a s i - t o r u s } ) , } \\ { m \Delta \bar { J } \gg \hbar \quad } & { ( \mathrm { i s o l a t e d ~ o r b i t s } ) . } \end{array}
$$

It is thus the difference in the symplectic area between a pair of periodic orbits,which survive the destruction ofa periodic torus,that determines whether theorbitscontributeseparatelyorcombine to forma quasi-torus.

The dependence on the number of repetitions in (9.66) and (9.67) seems to entail fundamentally different spectra for integrable systems and quasi-integrable systems -no matter how small the perturbation， the number of contributions satisfying (9.67) will always be infinite. It is therefore necessary to understand more fully the manner in which periodic orbits combine to manufacture the Bohr-Sommerfeld spectrum. Let us consider a quantized torus in an integrable system. The quantization condition, taking into account the Maslov indices, can be expressed in the following way: If all the independent circuits on this torus were periodic orbits,they would all supply zero-phase contributions to the density of states sum.

The quantized torus with frequencies $\omega$ is the limit ofan infinite sequence of periodic tori, with frequencies that approximate $\pmb { \omega }$ arbitrarily well. Therefore, the periodic orbits of these tori have actions that are also good approximations of irreducible circuits on the quantized torus. The sum over infinite asymptotically coherent contributions results in the $\delta$ function of the density of states! Since none of the approximating tori has the exact quantized action, the difference between the quantized action and the approximate action of a given neighbouring torus grows proportionately to m. Thus,it is the first repetitions of the periodic tori that determine the quantization condition of an integrable system.

We conclude that a quasi-integrable system can be quantized by the Bohr-Sommerfeld rules of a neighbouring integrable system as long as (9.66) is satisfied with $m = 1$ for all orbits. This condition is probably still too restrictive for the local use of the torus quantization conditions near a surviving torus of a strong perturbation. The resonances near a surviving torus must become very weak the closer they are to the torus in the way described by Escande (1985). The implication of the foregoing reasoning appears to be that a quantized torus that survives a perturbation continues to contribute a $\delta$ function to the density of states, even if there are regions in phase space where the motion is strongly nonintegrable.

# 9.5 Correlation function for the density of states

Though of great theoretical interest, the periodic orbit sum formula in itself merely relates our ignorance of the density of states to the even more mysterious maze of periodic orbits. We can only attempt to explain the semiclassical fluctuations of the density of states by supplying further information about the distribution of periodic orbits. This is feasible for ergodic systems, because of the uniformity principle conjectured in section 3.6.An important consideration is that these (two-dimensional) systems have no stable periodic orbits: By virtue of the KAM theorem they would be surrounded by thin tori, which prevent most orbits from approaching the stable periodic orbit. Thus, there are no small denominators in the periodic orbit sum, the amplitudes being correctly given in the linearized approximation by (9.34).

The square of these amplitudes is closely related to the period distribution of periodic orbits (3.61) predicted by the uniformity principle, so we choose to work with the two-level correlation function for the fluctuations about the average density of states:

$$
\begin{array} { l } { { \displaystyle \langle \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) \rangle _ { E } = \sum _ { j = 1 } ^ { } ( 2 \pi \hbar ) ^ { - 2 } \langle \tau _ { j } ( E + \varepsilon ) \tau _ { j ^ { \prime } } ( E ) A _ { m j } ( E + \varepsilon ) A _ { m ^ { \prime } j ^ { \prime } } ^ { * } ( E ) } } \\ { { \mathrm { } \ } } \\ { { \displaystyle \qquad \times \exp \left\{ i [ \hbar ^ { - 1 } m S _ { j } ( E + \varepsilon ) - m \pi - \mu _ { m j } \pi / 2 \right. } } \\ { { \displaystyle \left. - \hbar ^ { - 1 } m ^ { \prime } S _ { j ^ { \prime } } ( E ) + m ^ { \prime } \pi + \mu _ { m ^ { \prime } j ^ { \prime } } \pi / 2 \right] } } \\ { { \displaystyle \qquad - \hbar ^ { - 1 } \lambda ( | m \tau _ { j } ( E + \varepsilon ) | + | m ^ { \prime } \tau _ { j } ( E ) | ) \} \rangle _ { E } , \qquad ( \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \forall \mathrm { } \Sigma ^ { \prime } \ \widetilde { C } . } }  \end{array}
$$

where the fluctuation d(E) is defined by (8.28). In the semiclassical limit we can expand Sj(E+ε)=Sj(E)+εtj(E) in the exponent of (9.68), while neglecting ε in the slowly varying terms, as long as ε < O(h). Defining once more a peaked normalized function δ,(E-Eo) centred on E and of width $\Lambda$ (independent of $\hbar$ ),weobtain

$$
\begin{array} { r l r } {  { \langle \tilde { d } ( E ) \tilde { d } ( E + \varepsilon ) \rangle _ { E } } } \\ & { = } & { \sum _ { j m } { ( 2 \pi \hbar ) ^ { - 2 } } \exp \Bigg \{ - i \Bigg [ ( m - m ^ { \prime } ) + \frac { ( \mu _ { m j } - \mu _ { m ^ { \prime } j } ) } { 2 } \Bigg ] \pi \Bigg \} \exp ( i \hbar ^ { - 1 } \tau _ { j } \varepsilon ) } \\ & { \times } & { \displaystyle \int _ { - \infty } ^ { \infty } d E \delta _ { \Lambda } ( E - E _ { 0 } ) \tau _ { j } \tau _ { j } \mathcal { A } _ { m j } \mathcal { A } _ { m ^ { \prime } j ^ { \prime } } ^ { * } \exp \big \{ - \hbar ^ { - 1 } \lambda ( | m \tau _ { j } | + | m ^ { \prime } \tau _ { j ^ { \prime } } | ) \big \} } \\ & { \times } & { \exp \{ i \hbar ^ { - 1 } ( m S _ { j } - m ^ { \prime } S _ { j ^ { \prime } } ) \} , } \end{array}
$$

where the arguments of t,A and S are always E. In general the last exponential willoscillaterapidly if (m,j)≠(m',j'),unless mt(E)=mt(E). This condition for accidental degeneracy of periods may certainly occur, but the evaluation of such terms by the stationary-phase method (considering δ, to be a smooth amplitude) contributes only to O(h1/2), whereas the diagonal terms give contributions of $O ( \hbar ^ { 0 } )$ So the corelation function is

$$
\begin{array} { l } { { \displaystyle \langle \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) \rangle _ { E } } } \\ { { \displaystyle \quad = ( 2 \pi \hbar ) ^ { - 2 } \sum _ { j m } \langle \tau _ { j } ^ { 2 } | A _ { m j } | ^ { 2 } \exp \big \{ \hbar ^ { - 1 } ( i \varepsilon \tau _ { j } - 2 m \lambda | \tau _ { j } | \big \} \rangle _ { E } + O ( \hbar ^ { - 3 / 2 } ) . } } \end{array}
$$

Weare now ina position to introduce the periodicorbit spectralfunction $f ( \tau )$ given by (3.61) into (9.70),which becomes

$$
\langle \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) \rangle _ { E } = ( 2 \pi \hbar ) ^ { - 2 } \Bigg \langle \int _ { - \infty } ^ { \infty } d \tau \lvert \tau \rvert \exp \left\{ \hbar ^ { - 1 } ( i \varepsilon \tau - 2 \lambda \lvert \tau \rvert ) \right\} f ( \tau ) \Bigg \rangle _ { E } .
$$

According to the uniformity principle,the asymptotic limit of $f ( \tau ) \to 1$ holds for all energies. Thus,the behaviour of the correlation function for small $\hbar ^ { - 1 } \varepsilon$ (so that its Fourier transform depends on the region where $\tau$ is large) will be

$$
\begin{array} { l } { { \langle \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) \rangle _ { E } } } \\ { { \approx ( 2 \pi \hbar ) ^ { - 2 } 2 \operatorname { R e } \displaystyle \int _ { 0 } ^ { \infty } d \tau \tau \exp \{ \hbar ^ { - 1 } ( i \varepsilon - 2 \lambda ) \tau \} \xrightarrow [ ( \lambda / \varepsilon )  0 ] { } - ( 2 \pi ^ { 2 } \varepsilon ^ { 2 } ) ^ { - 1 } . } } \end{array}
$$

To compare this result with the statistical theory of ergodic spectra in section 8.4 we must first sort out the symmetry properties of the Hamiltonian. The deduction of (9.72) made no reference to symmetry, so this limit of the correlation function must be compared with that of the Gaussian unitary ensemble (GUE) with which it agrees. The Gaussian orthogonal ensemble (GOE) applies to ergodic systems with time reversal invariance: H(-p,q)= H(p,q). In this case periodic orbits come in symmetry pairs, except for the negligible proportion that are selfsymmetric. Evidently, both orbits in a symmetry pair have exactly the same symplectic area, so there will be twice the usual number of terms for which exp{ih(mS,-m'S,.)} =1 in the sum (9.69). Since the amplitudes and the periods of a symmetry pair are also identical, we obtain

$$
\langle \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) \rangle _ { E } \xrightarrow [ { ( \lambda / \varepsilon ) \to 0 } ] { } - ( \pi ^ { 2 } \varepsilon ^ { 2 } ) ^ { - 1 }
$$

in agreement with the dominant term of (8.57) - the ensemble average of $- \widetilde { d } ( E ) \widetilde { d } ( E + \varepsilon ) / ( \widetilde { d } ( E ) ) ^ { 2 }$ . It may seem strange that the present result for small energy intervals should correspond to asymptotically large ε in section 8.4,but it must be remembered that $\varepsilon \ll O ( \hbar )$ is not incompatible with $\varepsilon \gg O ( \hbar ^ { 2 } ) \sim 1 / \tilde { d }$ in the semiclassical limit.

The fact that (9.73) agrees only with the asymptotic tail of the GOE correlation function is not necessarily the consequence of a deficiency of the periodic orbit sum for $\lambda \lesssim \bar { d }$ .The exact relation (for arbitrarily small λ) in the case of geodesic motion on a surface with constant negative curvature testifies to this end. There is a problem, however, with the neglected contributions of the accidental period degeneracies in (9.69). In the limit $( \lambda / \bar { d } ) \to 1$ ,the number of‘undamped’ periodic orbits in the periodic sum increases to the extent that accidental period degeneracies may add a significant contribution.

In the original work on the uniformity principle, Hannay and Ozorio de Almeida (1984) deduced the correlation for the density of states in $\hbar ^ { - 1 }$ with fixed energy. Though somewhat unphysical, this has the advantage of dispensing with problems concerning semiclassical scales of the energy spectrum.In the case of billards,analysed by Hannay (1984),the resulting spectrum is equivalent to the spectrum of the momentum (proportional to E1/2). The first use of the uniformity principle directly in the energy spectrum was that by Berry (1985), who worked with the ‘spectral rigidity instead of the two-level correlation function.

It is worthwhile to conclude with a summary of our present partial knowledge concerning the energy spectra of chaotic systems.The common basis is the Weyl density. This large-scale average (△E >h) depends only on zero orbits; it is therefore insensitive to any dynamical feature of the system,except the relation between the volume and the energy of the energy shells.Though corrections are needed in thecaseof billiads,there is strong computational evidence that the Weyl density describes the real averaged spectra of integrable, ergodic and in-between systems. It appears that the spectra of almost all systems with positive entropy have ergodic fluctuations- their local averages (△E h) can be calculated from appropriate ensemble averages.In the case of the two-level correlation function, we can successfully explain part of its form on the basis of the conjecture of the uniform distribution of periodic orbits. Obviously we need similar universal principles to explain further generic properties of the spectra of chaotic systems. So far,it is not clear how far these can be based on the uniformity principle itself, nor is it known whether all local statistical properties of the spectra of chaotic systems are ergodic. It has been computationally verified that the nearest-neighbour spacing (8.59) is usually ergodic in the case of positive entropy. The periodic orbit formalism is probably not the ideal probe for the study of such fine scales of the spectrum. It is in the intermediate range of averages $( \Delta E \sim \hbar )$ that knowledge of a few short periodic orbits leads to a description of the nonuniversal spectral fluctuations.

Of course, there are many other important questions concerning the energy spectrum. Berry (1983) reviews the problem of eigenvalue degeneracies.Broadening our view,we find that comparatively litle is known about the wave functions of chaotic systems. To some extent this also holds for quantum transport, diffusion and other nonstationary phenomena, though their absence from this book in no way reflects the rapid progress being achieved in their study.

# References

Abramowitz,M.and tegun,I.A.(1964).Handbook of Mathematical functions. Washington, DC: U.S.National Bureau of Standards.   
Aguiar, M. A.M.,Malta,C.P.,Baranger,M.andDavies,K.T.R. (1987). Ann. Phys. N.Y. 180,167.   
Arnold,V.I.(1963).Russ. Math. Surv.18,85.   
Arnold,V.I.(1965).AS Transl. Ser. 2,46,213.   
Arnold,V.I(1967). Funct.Anal. Appl.1, 1.   
Arnold,V.I(9).rdinary reialuaios.midgeA:   
Arnold,V.I (1975).Russ.Math.Surv.30,1.   
Arnold, V.I (1978). Mathematical Methods of Classical Mechanics. New York: Springer.   
Arnold,V.I(982).Geometrical ethodsinthe oryofrdinaryifferential uions. New York: Springer.   
Arnold,V.Ind veA.(968).rgodic rolems ofssical ecaics.eading Benjamin.   
Aubry,S(1978). In Solitons and Condensed Matter Physics,ed.A.R.Bishop and T. Schneider. New York: Springer,264.   
Aubry,S.ad Leeron,P..(983).sica 81.   
Balazs,N.L.andVoros,A.(1986).Phys.Rep.143,109.   
Balian,R(1968).Nuov.Cim.57,183.   
Balian,R.and Bloch,C.(1974).Ann.Phys. N.Y85,514.   
Baltes,H.P.and Hilf, E.R.(1978).Spectra of Finite Systems. Manneim: Wissenschaftsverlag.   
BerryM.Vj(1976).Adv.Phys.25,1.   
BerryM.V(1977a).Phil.Trans.Roy.Soc.Lon.287,237.   
Berry,M.V (1977b).J.Phys.A102083   
Berry,M.(98).Inicsinearmicsd.oa.Am.stono. 46, 16.   
Berry,M.V(9a).Inngulris in Wesndas.(es ouchesesin35)ed.. Balian,M.eJ.ermedm:t   
BerryM.V (1981b).Ann.Phs.N.Y.131163.   
BerryM.().Inoicorfetice(essi3), ed.G.IossR.G.H.HellemanandR.Stora.msterdam:Northolland171.   
Berry,M.V(1985).Proc.Roy.Soc.A400229. Berry,M.Vand alas,N.L.(1979).J.Phs.A1,625.   
Berry,M.VHyJ.HodeeidaA..(93).ica2   
BerryM.Vandout,..97).ep.rogr.s.515.   
BerryM.Vandabor.(1976)roc.Roy.Soc34901.   
BerryM.dUil,C.(8rr.Ot   
Berry,M.VandWright,.S.98O).J.h.149.   
Billingsey)icdiokWile Birkhoff, G. D. (1927). Acta ath. 43,1.   
Bohigas,Odoi.J84).Ineaticaladputatioalti NuclearPhics(Lctureotesinics)d.J..eeaJ..G A.Polls.New York:Springer,1.   
Bohigas,O.anoni,.J.ndSchmit,C.(984).Phys.RevLtt.51.   
Bountis,T.C.(98).hsica 3   
Buminovih)   
Casati,G.,Chirikov,B.V.,Ford,J.and Izrailev,F.M.(979).Stochastic Behaviour in Classical and Quantum Hamiltonian Systems (Lecture Notes in Physics 93), ed.G. Casati andJ.FordNewYork:Springer34   
Chirikov,B.V.979).hs.Rep.6   
Collet,P.,,J.doch,H.().ic.   
daSilvaRiter,G.L.OzoriodeAlmeida,A.M.andDouady,R.(1987).Physica29D 181.   
Devaney,R. (979).Ann.N.Y.Acad.Sci168.   
Dirac.P.A.3efQuteOfd University Press.   
Dyson,F.J. (1962).J.Math.Phys.3,140.Reprinted in C.E.Porter,ed.(1965).Statistical Theories of Spectra:Fluctuations.New York:Academic Press.   
Engel,W.(58).th.Ann.69   
Escande,D.F.(1985).ys.ep.121165.   
Feigenbaum978).Jtat.s.925.   
Feigenbu7).Jat..   
Goldstei   
Greene,J.1979).J.ath.hys.   
Greene,J.acy..aldiFegeum,J(98).ic68.   
Gucken)cl BifurcationsofVector Fields.NewYork:Springer.   
Gutzwiller..t.   
Gutzwiller.(7).Jath.   
Hannay,J.98).IhaoticBehaviourinQuantumSytemsed.G.Caatiewrk Plenum Press, 141.   
Hannay,J.H.and Berry,M.V.(198O).Physica1,267.   
HanayJandOzoriodelmeida,A..(1984).J.hs.17429.   
Heller,E.J. (984).Phys.Rev.Lett.53,515.   
Henon,M. (1969). Q.Appl. ath.27,291.   
Herman, M.R. (1979). Publ. Math.IHE,49,5.   
Howland,J8iclodtiriy NotesinPhcs3,ed.J.A.eantoA.W.eandK.acary.： Springer.   
Katok,A.(982).Ergod.Teor.ynam.Syst.21.   
Keller，J5）A   
Khinchin,A(95)teaticalFoudtiosofformationork Dover.   
Khinchin,A.Yal(1963).Continued Fractions.Groningen:Noodof   
KolmogorovA.N.(1954).okl.Akad.auk.98,57.   
Lanford,O.E,I(983).InoticBehiourofeterministicSytems (LesHouhes, Session 36), ed. G.IossR.G. H. elleman andR. tora. Amsterdam: North olnd, 6.   
Lichtenberg.)uic York:Springer.   
Mackay，R.S(3).ica   
Mackay   
Mandelbort,B.(1982).The Fractal Geometry of Nature.San Francisco:Freeman.   
Margulis,G.A.(1969). FunctionalAnalizi Ego Prilozhen 3,89.   
Maslov,V..nd oink,..(98).em-sical Aroimationinm Mechanics. Dordrecht: Reidel.   
Mather,J. N. (1982). Topology 21,457.   
McDonald,S.W.and Kaufman,A.N. (1979). Phys. Rev. Lett. 42,1189.   
Meyer,K.R.(197O). Trans. Am. Math.Soc.149,95.   
Miller,W.H. (1975).J.Chem.Phys.63,996.   
Mohring,K.,Levit, S.and Smilansky， U. (198o).Ann. Phys. N.Y127,198.   
Moser,J.1956).Comm.Pure Appl.Math.9,673.   
Moser,J.(962).J.Nachr.Akad.Wiss.，Gotingen,ath.Phys.11   
Moser,J.(1966).Ann.Scuola Normale Sup.Pisa Ser.320,499.   
Moser,J.(1973).Stable and Random Motions in ynamical Systems.PrincetonNJ: Princeton University Press.   
Moyal,J.E.(1949).Proc.Camb.Phil.Soc.Math.Phys.Sci.45,99.   
Oseledec,V.I.(1968).Trans.Moscow Math.Soc.19,197.   
Ozorio de Almeida,A.M (1982).hysica 110A,501.   
Ozorio de Almeida, A. M(1983). Ann. Phys. N.Y. 145,100.   
Ozorio de Almeida, A. M.(1984). Rev. Bras. Fis.14,62.   
Ozorio de Almeida,A.M(1986).In Quantum Chaos and Statistical Nuclear yics (Lecture Notes in Physjcs 263),ed. T. Seligman. New York: Springer,197.   
Ozorio de Almeida,A. M Coutinho, T.J. S. B.and da Silva Ritter,G. L.S. (1985). Rev. Bras. Fis. 15, 60.   
Ozorio de Almeida, A. M and Hannay, J. H. (1982). Ann. Phys. N.Y 138, 115.   
Ozoriodemeida,A.andHannay,J.H.(987).J.Phys.A205873.   
ParryW.984).god.or.am.t411.   
ParryW.ndlot.).Ann.t   
Peixoto,M.C.and Peixoto,M.M.(1959). Ann. Acad. Bras.Ci31135.   
Peixoto,6).lg   
Percival,.dds8)iotigeit Press.   
Pesin, Ya. (1977).uss.Math. urv.3254.   
Poincare,H9)meosoelseeestess Gauthier-Villars.   
Porter,C.Ed(96)al eofeta:ucasewke Press.   
Poston,Tdrtdi Pitman.   
Ramaswamy,R.and Marcus,R.A.(1981).J.Chem. Phys.74,1385.   
Richens,P.Jy.c.   
SinaiYa.G.1959).Dokl.Akad.Nauk.25.768.   
Sinai,Ya. G.(1968).Transl.A..S.7227.   
SinaiYa.G(197).RussMath.Suro.2517   
Van VleckJ.H.(1928).Proc.Natl.Acad.Sci.UA1417   
Voros,A.(1979). In Stochastic Behaviour in Classical and Quantum Hamiltonian Systems (Lecture Notes in Physics 93),ed. G.Casati and J.Ford. New York: Springer,326.   
Wigner,E.Pl(1932).Phys.Rev.40,749.   
Wigner,E.P(1957).Can.Math.Congr.Proc.174.Reprnted inC.E.Portered.(1965). StatisticalTheories of Spectra:Fluctuations.New York:Academic Press

# Index

action,36,148,157,213 reduced,36,116,131,16,1   
actioge7 139,191   
Airy function,163   
‘almost all points', 61   
angular ometum6   
Anosov s   
Anosov's theorem, 47   
anticaustics,183   
antiscars, 219   
approximts,6,109   
Arnold diffusion,148   
Arnold's cat map21,47 quantized, 2007   
Arnold's net, 147   
attractor,59   
autonomousem Hamiltonian,1   
averagesieef,62 139 ensemble,63 time,19, 61,70,105,139   
averaging,138,142   
Berry chords,174,186,189   
Berry-Voros hyothesis,8,188   
bifurcation,41,9,   
billiards,67,7,14 quantum,191,198 Sinai's, 68,191, 198   
Birkhoff normal form,7-83,89,224   
Bohr-omfeld tion,5 226   
canonical ar oordinates,742,   
canonical tormion,35,41 42, 79, 93,120, 126,140,145, 159,163, 172, 179,191   
cantori,146   
Cantor set,57,103,146

catastrol   
catastrophe theory,133   
caustic,127,131-8,148,160,163,178,183   
214   
central force, 126   
centre,7   
chaotic moion,23,47,48,59,87,97,14,   
146   
circular ensemble200   
classical limit,   
codimension,14   
commutation of matrices,10   
complex conjugate field, 5   
complexiicin5   
configuration space,127,182   
conjugate planes (canonical), 12   
conjugate oints,78   
constant of the motion,11,15,126   
continued fractions,106   
correlation function   
density of states,198,228-31   
wave function,183   
cusp,134   
dense orbit,18,58,148   
density matrix,168,210   
density of states,190-,211213-15,218   
devil's staircase,103   
diffeomsm25,03,   
diffraction catastrophe integrals,163,175   
Diophanine citios,89,145   
dynamical matrix,4,27   
dynamical system,3

eigenfunction, 156   
eigenvalue,3,14,75,79 degeneracy,,14 of propagator, 206 in quantum mechanics,156   
energy conservation,11 resonant,4

heteroclinic oint,4,9 homeomorphism,27,45,46 homoclinic rbit,,4 homocliic t,1,4, homoclinic tangle, 53--5,3-90 Howland's method, hyperbolic invariant set, 8,69

energy shell or surfce,35,72,82- 190,215,230   
energy spectrum ergodic,193,198,200 fluctuations,193 integrable system,165-8,215,226 level repulsion,197 two-level crrelation981   
ensembles of random matrices,196,200, 229   
entropy,64-9,71,191,195   
envelope of trajectories, 137   
equilibrium,3,48,75,79,9,146 hyperbolic,28,45   
ergodic moion,19,62,70,   
ergodic spectrum,193   
exterior algebra, 12

information,66,195   
integrablee1   
integral of the motion, 11   
invariant curves,21,31,86,91,92,9,145   
invariant function,62   
involution,116,126   
irrational numbers,102,104,105-9,144   
islands,93,143

Jordan block,8,16,77

fast variable,76,140,226   
fixed pt,2,21,1,8   
flow,11,16,7   
focal point,   
focus,7   
fold,   
forced oscillation,33,146   
Fourier series,19,79,80,110,122,14   
Fourier transform,161,1,209   
fractal,   
freedom (number of), 11   
frequencies,ationally independet19

KAM theorem,143-52,228 kicked rotor,200 Kolmogoov'sd

Lagrangian, 157   
surface, 116, 121, 132, 148, 157, 177, 187,   
209   
Legendre ransform,131,34,160   
libration, 48,93   
linear map, 11, 14   
linear system, 4, 16   
Liouville distribution,7   
Liouville teorem,1324   
Lyapunov ot,68,

Gaussian orthogonal ensemble (GOE), 196   
Gaussian unitary ensemble (GUE), 196   
generatinguio,79,141,42, 201,223   
generic,15,32,95,133,16 quadratic Hamiltonian, 16 system,1   
genus of a surface, 151   
golden mean, 108   
Green function, 215   
group of tansformations,117,20,170   
Hamiltonian system,11 autonomous,11 matrix, 12, 14   
Hamilton-acobi equation,758   
Hamilto'ss11   
harmonic oscillator, 123,129   
Hartman-oneoem,271,44,74   
Hessian matrix,12   
heteroclinic orbit,48687   
manifold stable,28, 32, 48 unstable, 28, 32, 48   
maps Arnold's cat,21,47,,2 circle,18, 100, 144 generic,95 linear,11,20-3,171, 180,200-7 Poincare,18,30,33,35,48,50,,8, 91,100,144, 147, 200, 222 quadratic,89, 97 quantum, 200 reversible, 44 standard,20 stroboscopic,33,40,20,2 tangent, 25   
Maslov iex   
Maslov method,66,78   
Matrix density,168,210 dynamical, exponential of, 3 Hamiltonian,12 Hermitian,194 Hessian,1 Moyal,176 normal form, 8 random,193-200 rank of, 8 solution, 4 stability,31,71,1 symplectic, 13   
measurable function, 61   
measure, 59-64 invariant, 60, 117 Lebesgue, 60,109 Liouville, 60,72,1 for matrices,194 probability, 60   
Melnikov function,50   
Melnikov ed   
metric,194   
mixing,23,63   
mode number,190   
Morse inex,78,15   
Moyal matrix,176   
multiply periodic motion,122   
Newton's method,1   
node,8,76   
nonwandering oint,61,7   
normal form Birkhoff,7224 for catastrophe theory,134 convergence,77,4 for periodic orbit,78,0,91 for quadratic Hamiltonian16 resonant,92,2   
null surface,116

operator density68,15 evolution,177,,9 momentum,155,156 period, 200 position,155 Weyl,

partition,64

uniform, 19 Peixoto'sheorem,45,47 pendulum,48,93,143 periodic orbit, in cat map,23,89 in circle map,102 density of,2,58,72 families,40 hyperbolic,32 in normal form, 86 quantization, 215-22 sum rule, 71, 73 uniformity,69-73,228 periodic point, 1, hyperbolic,31 perturbis,145053,6, phase space,3 Poincare domain,77 Poincare index,98 Poincare map,18,308,48,50,72,,91 100,144,147,200,222 Poincaresei1,4,5 point of equilibrium, 3 point transformation, 13 Poissonbracket,2116 Poissonit propagator,177-9,201,2913 pseudointegrable sems51 pure-state condition,185-9

quasi-torus,224

random matrices,193-200   
rationally independent frequencies,19   
rectification of vector fields, 24-7   
recurrence,60, 71,87   
reduced sem9,   
reducible curve, 38   
reduction of dimensions,38-44   
resonance Chirikov, 143, 226 condition,75,82,92,141 order of, 75,82, 144   
rotation,48,13   
rotation number,100-2,104,144,147

saddle it, satelliteorbits,95,223 scar,173,212, 218 Schrodinger equation,155 Selberg traceformula,219 semiclassical limit

separable stem28   
separatrix,48,58,85,93,143   
shift, 56   
Siegel domin,   
singularity of vector field,27   
skew rtgol   
skew prouct,12,41,16   
slow variable,140   
Smale's horseshoe,56-9, 89   
small-denominator problem,77,1, 111, 141, 218   
solution, 3 matrix,4   
square well,   
stablemold,   
stadium, 68   
stationreoii 186,212   
stationary ts   
strange attactor,59   
structurallyable stem16,447 103,137   
symbolic rbit,9   
symmetry,42,97   
symplecticaea,,5,16,217,, 189,212,216,230 matrix,13   
symplectic mio5,6   
system autonomous,3,1 dynamical, 3 ergodic, 19 Hamiltonian, 11   
tangent space, 25 map, 25   
theorems Anosov, 47 Birkhoff local ergodic,6171 Birkhoff-oser,3,86 Denjoy,103,105,19 existence and uniqueness, 25 Hartman-Grobman,27-31,44,74 Kolmogorov-Arnold-Moser (KAM), 143-52, 228 Liouville, Liouvilleold,

Peixoto,45,47 Poincare-irkhff, Poincare-rtan integral,64 Poincare recurrence,60,70,117 rectification, 25 Siegel, 78 Smale-Birkhoff homoclinic,58,9 stable mfold,0,31,, Thom,133 time reversal topological equivalence,28,31,45,58,1 torus,17, 20,68,91, 101,115-22,126, 159- 68,172-6, 201 island, 93,143 periodic,91, 93,94,101, 226 torus, ronat,141 turning int,122,16,25

umbilic elliptic,5 hyperbolic,   
unfolding of singularity,136   
uniform approximation,165   
uniformity principle (periodic orbits),69- 73,228   
unitary oio7995

variational principle,7,4 vector field,3,24,27,39 Hamiltonian,16

wandering point, 61   
wave function,155-65 intensity of, projections,169,170,12   
Wentzel-Kramers-Brillouin (WKB) approximation, 160   
Weyl-Balian ensemble, 196   
Weyl rule,1901   
Weyl traom7   
Wigner caustic,7519   
Wigner function,168-76,185-9,04,1 classical2,, crossed, 176

zero orbits,210,230

![](images/f9dd7043eb96b1f9f6e42e8d4090e7ec77bc253bc3cc03db667f8a05d481ee7c.jpg)

![](images/e9dd4efc9fc2311dd798b33b2a258999cd29f3c8e910fc2c58af602c118ef7dc.jpg)

This text introduces the theory of Hamiltonian chaos, outlines the main results in the field, and goes on to consider implications for quantum mechanics.

The study of nonlinear dynamics, and in particular of chaotic systems, is one of the fastest growing and productive areas in physics and applied mathematics. In its first six chapters, this timely book introduces the theory of classical Hamiltonian systems. The aim is not to be comprehensive, but rather to provide a starting point for further investigation. The main focus is on periodic orbits and their neighborhood,since this approach is an especially suitable introduction to the implications of the theory of chaos in quantum mechanics discussed in the last three chapters.

The book will be valuable to all researchers and graduate students in physics or applied mathematics interested in Hamiltonian chaos and its implications for quantum theory.

“... it successfully gives a concise treatment of well-chosen key elements of the field that are suitable for an upper-level graduate physics course." Science

Other titles in the series include:   
Itzykson, C. and Drouffe, J-M.   
Statistical Field Theory,   
Volumes One and Two   
Birrel，N.D.and Davies,P.C.W.   
Quantum Fields in Curved Space   
Collins, J.   
Renormalization   
Penrose,R.and Rindler,W.   
Spinors and Space-time,   
Volumes One and Two.   
Green,M.B., Schwarz, J.H.a   
Witten,E.   
Superstring Theory, Volumes   
One and Two.   
Taylor,J. C.   
Gauge Theories of Weak Interactions   
Polkinghorne, J. C.   
Models of High Energy Processes

# CAMBRIDGE UNIVERSITY PRESS

ISB-N-0-521-38670-5 26240 \$24.95 09/06/90 #HAMILTONIAN SYSTEM