where $A$ is determined by the equipartition of energy in thermodynamic equilibrium. The latter implies, at low frequencies $\nu \ll ( R C ) ^ { - 1 }$ ,

$$
\frac { S _ { \mathbf { v } } ( \nu ) } { R } = 2 k T ~ ,
$$

and hence

$$
A = 2 k T R \ ,
$$

where $2 k T$ is the power per unit frequency in unpolarised radiation from a blackbody at temperature $T$ , provided the frequencies are low (Rayleigh–Jeans law). The cutoff frequency $( R C ) ^ { - 1 }$ of this thermal noise is associated with the mean free path of the electrons between atoms, and is of the order of $1 0 ^ { 1 3 } ~ \mathrm { H z }$ at $3 0 0 ~ \mathrm { K }$ . After filtering $\mathbf { v } ( t )$ with a filter of frequency bandwidth $\Delta \nu \ll ( R C ) ^ { - 1 }$ , the noise power of the filtered voltage is then given by

$$
\langle \nu ^ { 2 } \rangle = \int _ { - \infty } ^ { + \infty } S _ { \mathbf { v } } ( \nu ) \mathrm { d } \nu = 4 k T R \Delta \nu ,
$$

which is the Nyquist formula.

This formula is particularly useful in determining the thermal noise associated with a detector which behaves like a resistance at temperature $T$ .

# Quadratic Detectors and Thermal Noise

A quadratic detector has been defined as one which delivers, for example, the quantity proportional to the square ${ \bf b } ( t )$ of the process ${ \bf a } _ { 1 } ( t )$ resulting from the filtering of the electric field ${ \bf a } ( t )$ .

The autocorrelation of the stochastic process ${ \bf b } ( t )$ is given by the expression (see Appendix B)

$$
R _ { \bf b } ( \tau ) = R _ { { \bf a } _ { 1 } } ^ { 2 } ( 0 ) + 2 R _ { { \bf a } _ { 1 } } ^ { 2 } ( \tau ) \ .
$$

Taking the Fourier transform of this relation,

$$
S _ { \bf b } ( \nu ) = R _ { { \bf a } _ { 1 } } ^ { 2 } ( 0 ) \delta ( \nu ) + 2 S _ { { \bf a } _ { 1 } } ( \nu ) \star S _ { { \bf a } _ { 1 } } ( \nu ) .
$$

Letting ${ \bf a } _ { 1 } ( t )$ be a stochastic process filtered by a low-pass box-function filter, with cutoff at $\nu _ { \mathrm { c } }$ , it follows that

$$
S _ { \mathbf { a } _ { 1 } } ( \nu ) = k T \pi \left( \frac { \nu } { 2 \nu _ { \mathrm { c } } } \right) , \qquad R _ { \mathbf { a } _ { 1 } } ( \tau ) = 2 k T \nu _ { \mathrm { c } } \operatorname { s i n c } ( 2 \nu _ { \mathrm { c } } \tau ) ,
$$

$$
S _ { \mathbf { b } } ( \nu ) = ( 2 k T ) ^ { 2 } \nu _ { \mathrm { c } } ^ { 2 } \delta ( \nu ) + 2 ( k T ) ^ { 2 } 2 \nu _ { \mathrm { c } } \left( 1 - \frac { \nu } { 2 \nu _ { \mathrm { c } } } \right) ,
$$

![](images/a09c96a379c57068d9053c4d1a5f6eb28cd18bc5d3e7b1eb129c81dbe8d5b0c0.jpg)  
Fig. 7.12 Spectral density of a filtered stochastic process ${ \bf a } ( t )$ , and of its square ${ \bf b } ( t )$

as illustrated in Fig. 7.12. The PSD of the stochastic process ${ \bf b } ( t )$ is no longer white, and its mean no longer zero, as is shown by the non-zero value of $S _ { \mathbf { b } } ( 0 )$ .

Note. A similar method could be used to study the probability distributions of the amplitude and phase of ${ \bf a } _ { 1 } ( t )$ , and of its instantaneous mean power, etc., in those experimental arrangements which involve these quantities.

We now have at our disposal all the tools needed to find variances and autocorrelations associated with thermal noise. These will be used in the next chapter to establish the ultimate limits of receiving systems with respect to this type of noise.

# 7.3 Physical Principles of the Detection of Electromagnetic Radiation

Detection involves a matter–radiation interaction and a transfer of energy towards the matter, which causes it to change state in a measurable way. Clearly, this change of state, which constitutes the signal, must be chosen to correspond to the mean energy $h \nu$ of the detected photons. If it involves too low an energy, the signal will be non-existent or undetectable, but if its energy is too high, the detector may be damaged or destroyed. Figure 7.13 gives an overview of the main interactions used in the detection of photons.

The photoelectric detection of radiation quanta is possible provided that their energies exceed several meV, which means wavelengths less than about $2 0 0 \mu \mathrm { m }$ . At longer wavelengths, thermal fluctuations dominate, so that radiofrequency quanta are hard to detect. This is not, however, a fundamental limitation, and in practice, radiofrequency detectors (in the millimetre and centimetre ranges, and beyond) detect the electric field of the wave directly. Finally, calorimetric detection of radiant energy constitutes a third approach, which is useful in the submillimetre and $\gamma$ ray regions of the spectrum.

![](images/22ffecae56847e53d02a946498ed6ab85f3f57ae2ec77d2225760ec6acc39a31.jpg)  
Fig. 7.13 Physical interactions and detection of radiation

# 7.3.1 Detection of Quanta

Here we discuss the physical principles applied in the detection of individual photons and the production of a measurable signal. Recent developments in microelectronics have profoundly changed, improved, and diversified the processes used by astronomers in their dectectors.

# Photoelectric Emission in Vacuum

The surface of a conducting solid presents a potential barrier which opposes the extraction of electrons from that solid. The height $E _ { \mathrm { s } }$ of this barrier is called the work function of the surface. Only photons with energy greater than this threshold can produce a photoelectron. The first photoelectric cell was devised in 1890 by Elster and Geitel. The work function $E _ { \mathrm { s } }$ depends on the crystal structure and the state of the surface of the material, but is generally around $1 \ \mathrm { e V } ,$ which limits the use of the photoelectric effect in vacuum to detection of wavelengths shorter than the micron (visible, UV, and X ray).

When the photon energy is greater than this threshold, the probability of photoelectron production is the quantum efficiency $\eta$ , defined by

$$
\eta = \frac { \mathrm { m e a n ~ n u m b e r ~ o f ~ p h o t o e l e c t r o n s ~ p r o d u c e d } } { \mathrm { m e a n ~ n u m b e r ~ o f ~ i n c i d e n t ~ p h o t o n s } } .
$$

This probability (Fig. 7.14) can be determined theoretically from the atomic structure of the material and the thickness of the emitting layer. It is generally

![](images/036556c629aa7c67a2b3b9605f740e5145ca053f5f2f93cae4cddf102055e8ad.jpg)  
Fig. 7.14 Quantum efficiency $\eta$ of photocathodes (in $\%$ ): (a) in the visible and near ultraviolet and $\mathbf { ( b ) }$ in the far ultraviolet. The S1 layer is a $\mathrm { A g - O - C s }$ photocathode (1930), and the S20 layer is tri-alkali ${ \mathrm { N a } } _ { 2 } { \mathrm { K S b } }$ (Sommer, 1955). Note the extremely poor response in the red, and excellent response in the far UV

less than unity, unless the photon energies become large compared with the energy differences between levels in the material (i.e., at UV or X wavelengths).

Detectors using the photoelectric effect in vacuum are the photomultiplier, the electronic camera, and image intensifiers.

# The Photoelectric Effect in Solids

Even when the energy of a photon is insufficient to eject an electron from the solid surface, it may nevertheless cause the ionisation of an atom in the solid, thus releasing charge carriers within the crystal lattice, and modifying the electrical conductivity of the material. This photoconducting effect can be used to detect the incident photon (Smith W., 1873).

Photoconducting materials are semiconducting crystals, and electrons within the crystal lattice have a characteristic energy level structure (Fig. 7.15). The conduction band is separated from the valence band by a gap, and the energy difference $E _ { \mathrm { s } }$ associated with this gap is exactly the photoelectric threshold of the material.

The width of this gap depends on the wave vector $\pmb { k }$ of the electrons. Let $E ( k )$ be this width. Its minimum value is $E _ { \mathrm { s } }$ , which is usually between a half and a quarter of its mean value. A photon of energy $E _ { \gamma }$ can transfer an electron of wave vector $\pmb { k }$ into the conduction band, and thus leave a hole in the valence band, if $E _ { \gamma } > E ( k )$ . This pair of charge carriers will move under the effect of an externally applied electric field, producing a current, or photocurrent. A pure crystal which manifests this effect is known as an intrinsic photoconductor (Table 7.2).

![](images/b231cdb7e86ddcb26cebf7a1fc78671b7a769a000483d0743869b84114623a0f.jpg)  
Fig. 7.15 Energy levels in a semiconducting solid. (a) Intrinsic photoconductivity. (b) Extrinsic photoconductivity of a doped semiconductor

Table 7.2 Intrinsic photoconductivity   

<table><tr><td>Material</td><td>Threshold wavelength [μm]</td><td>Working temperature [K]</td><td>Applications</td></tr><tr><td>Germanium Ge</td><td>1.88</td><td>77</td><td>Solar energy</td></tr><tr><td>Silicon Si</td><td>1.14</td><td>300</td><td>Astronomical detectors</td></tr><tr><td>Cadmium sulphide CdS</td><td>0.52</td><td>77 to 150</td><td>Photography (exposure meters)</td></tr><tr><td>Indium antinomide InSb</td><td>5.50 (77 K)</td><td>4 to 77</td><td>Astronomical detectors</td></tr><tr><td>Hg1-xCdxTe</td><td>Varies with x but ≤ 20μm</td><td>20 to 300</td><td>Thermal surveillance and astronomical detectors</td></tr></table>

In an extrinsic photoconductor (Fig. 7.15b), further energy levels appear in the band gap. These are caused by adjoining atoms of impurities within the crystal lattice, at very low concentrations $( \lesssim 1 0 ^ { - 8 }$ ). As these atoms can trap charge carriers, the energy threshold is lowered, and this explains why all infrared detectors, beyond about $\lambda = 5 ~ { \mu \mathrm { m } }$ , make use of extrinsic photoconduction. For example, replacing Done silicon atom (group IV of the periodic table) by one arsenic atom (group V of the same) in the silicon lattice, means adding an atom of similar electronic structure to the other atoms in the lattice, but with one extra, easily removed electron, and it is this extra electron that is responsible for the extrinsic photoconductivity ( $\overset { \cdot } { n }$ -type electron conductivity). Group III atoms inserted into a lattice of group IV atoms will lead to $p$ -type hole conductivity. The threshold can be adjusted, by making a suitable choice of impurity, or dopant, and this selects the wavelength region to which the detector is sensitive (Table 7.3). This idealised picture of photoconductivity should also take into account the effects of temperature and impurities.

Photoconductors are used in two ways: firstly, to measure electric current (photoconduction), and secondly, to measure pulses. In the first case, a flux is measured (photometry), and in the second, the energy of quanta is measured (spectrometry). In both cases, the performance of the photoconductor depends on its conductivity.

The conductivity, in turn, depends on the concentration of charge carriers in the conduction band. At low temperatures, this concentration depends on the temperature, and also the level of impurities, whereas at high temperature, it no longer depends on the level of impurities. For an intrinsic semiconductor, the concentration of charge carriers follows from the law of mass action, and can be written

Table 7.3 Extrinsic photoconductivity   

<table><tr><td>Matrix material: dopant</td><td>Threshold wavelength [μm]</td><td>Working temperature [K]</td></tr><tr><td>Si:As</td><td>24</td><td>&lt;20</td></tr><tr><td>Si:In</td><td>7.4</td><td>77</td></tr><tr><td>Si:Bi</td><td>18.7</td><td>29</td></tr><tr><td>Si:Ga</td><td>17.8</td><td>27</td></tr><tr><td>Ge:Ga</td><td>120</td><td>4</td></tr><tr><td>Ge:Gaa</td><td>195</td><td>4</td></tr></table>

a Threshold decreased by mechanical pressure on the crystal (stressed photoconductor).

$$
n _ { \mathrm { i } } = p _ { \mathrm { i } } \approx T ^ { 3 / 2 } \exp \left( - { \frac { E _ { \mathrm { s } } } { 2 k T } } \right) .
$$

For $k T > 2 \times 1 0 ^ { - 2 } E _ { \mathrm { s } }$ , the current is dominated by thermal excitation of the electrons near the conduction band, and not by photoionisation. This explains why a photoconductor must be cooled to a temperature $T \ll E _ { \mathrm { s } } / k$ , and the temperature must decrease as the energy of the quanta decrease, or if their their flux is low (photometry), or again when higher accuracy is required in the measurement of their energy (spectrometry).

Moreover, the crystals can never be perfectly pure, and it is difficult to go below an impurity level of $1 0 ^ { 1 1 } \mathrm { c m } ^ { - 3 }$ . Some atoms, occurring as an impurity, create energy levels which are very close to the conduction band, and which can be excited by very low temperatures. Even for $T \ll T _ { \mathrm { s } }$ , and in the absence of photons, the current will be non-zero (dark current). Hence, the quality of a photoconducting detector can be represented by the value of its impedance at its working temperature, and in the absence of any illumination (typically, $R \gg 1 \mathrm { G } \Omega$ ).

Only a fraction of incident photons create electron–hole pairs. Indeed, some photons lose their energy by exciting vibrations in the crystal lattice (phonons). This heats the crystal (optical absorption). When the optical depth of the material is sufficient, taking into account the photoabsorption cross-section $( \tau _ { \lambda } \sim 1 )$ , the quantum efficiency $\eta$ of the material is then determined.

The photoelectric effect in solids has become the basis for a large family of detectors used in astronomy: avalanche diodes, photoconducting or photovoltaic infrared detectors, solid-state imagers (also called Reticons, CCDs, or CIDs), blocked impurity band (BIB) detectors, television tubes, and photodiodes.

The Photovoltaic Effect. Junctions

Consider two doped semiconductors, one with impurities giving $n$ -type (electron) conductivity, the other with impurities giving $p$ -type (hole) conductivity. This would be the case for a silicon (group IV) matrix doped respectively with phosporous (group V) and gallium (group III). When put into contact with each other, these form a junction (Fig. 7.16). If two charge carriers, an electron and a hole, are released by an incident photon on the unbiased junction, then the voltage across it changes by an amount

![](images/59dfe3b3a37f28ce2f7f6e3c8aad19cdf9fe582cdc364bdc5f5488296e5b6486.jpg)  
Fig. 7.16 The principle of a junction between two semiconductors

$$
\Delta V = { \frac { e \delta x } { \varepsilon S } } \ ,
$$

where $\ S x$ is the thickness of the junction, $S$ its area, and $\varepsilon$ the electrical permittivity of the material. Absorption of a photon thereby results in a voltage across the junction, and this voltage can be measured by a high impedance circuit. This is the photovoltaic effect, discovered by A. Becquerel in 1839.

# Quantum Wells

Junctions can be made either from the same semiconducting material, but with different dopants in each part, or from two different materials (heterojunctions), in which case the band gap will differ from one side to the other. Starting from gallium arsenide AsGa, aluminium atoms can be inserted in the lattice to make $\mathrm { { A l } } _ { x } \mathrm { { G a } } _ { 1 - x } \mathrm { { A s } }$ . This is compatible with the crystal structure, and the result can be used to make junctions. A thin layer of AsGa sandwiched between two layers of $\mathrm { { A l } } _ { x } \mathrm { { G a } } _ { 1 - x } \mathrm { { A s } }$ has the effect of pushing the conduction band down to the level of AsGa. An electron crossing the junction remains trapped in the AsGa, which is thus a potential well. In such a quantum well, the electron can only have certain discrete and well-defined energies.

Infrared detectors can be made using this principle to construct a series of quantum wells, whose levels correspond in such a way that a photoelectron can pass from well to well by tunnelling, as far as the external electrodes.

![](images/a894dddf0f3ecd96ff660c23dbbd7232cf9cdd07eefdff9748bc511971f86791.jpg)  
Fig. 7.17 Superconductor–insulator–superconductor tunnel effect junction. (a) Energy level structure on either side of the insulator. Occupied states are shaded. The ordinate gives the energy and the abscissa the density of states. The superconductor energy gap is $2 \Delta$ . When $V$ is large enough to place occupied states on the left opposite vacant states on the right, a current can easily flow by the tunnel effect. If $e V < 2 \Delta$ , a photon may nevertheless excite a charge carrier to the energy at which the tunnel effect occurs (assisted tunnel effect). (b) Current–voltage characteristic of the junction. Continuous line: no flux. Dashed line: photons arriving. (Philips T.G., Woody D.P., ARAA 20, 285, 1982. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, 1982, Annual Reviews Inc.)

Photon Counting by Tunnel Effect

Consider a device made by sandwiching a thin insulating film ${ \approx } 1 0 ~ \mathrm { n m }$ ) between two superconducting electrodes. At low temperatures, this forms a junction called a superconductor–insulator–superconductor (SIS) junction. These junctions are commonly used as mixers in radiofrequency receivers (see Sect. 7.5). However, they also have promising applications for direct photon counting from X rays to the near infrared, where they are referred to as superconducting tunnel junctions (STJ).

Figure 7.17 shows how photons can be detected by such a junction.3 When there is no light flux and at temperature zero, a quasiparticle current can only pass through the insulating layer when the applied potential difference exceeds the sum of the gaps of the two superconductors, e.g., niobium, hafnium. If $T > 0$ , a dark current circulates whenever $\ S V \ne 0$ . Absorption of a photon in the superconductor breaks ¤a number of Cooper pairs that is directly proportional to the energy of the photon. This generates quasiparticles, which are then collected as current passing through the junction. The charges collected in this way can be amplified. Furthermore, an avalanche effect occurs because a quasiparticle induced by the photon can couple with a Cooper pair after crossing the insulating barrier, cross it again and be counted once more. Photon counting is a quantum mechanism, contains intrinsic amplification without noise (avalanche), and exhibits a certain spectral selectivity $( \leq 1 0 0 )$ .

# The Photochemical Effect

This effect is the basis of photography (developed by Nicephore Niepce, 1822, and Charles Daguerre, 1829). An incident photon excites an electron of the emulsion into the conduction band, and leaves a positively charged hole. The released electron is recaptured by a defect in the crystal lattice, and attracts a silver ion ${ \mathrm { A g } } ^ { + }$ to the site, thereby forming a neutral silver atom. The process repeats until a small cloud of silver atoms is produced, constituting one pixel, or element, of the latent image. The residual positively charged holes are able to move through thermal effects and then recombine with the silver atoms, which gives back silver ions. The processes of sensitising and hypersensitising photographic plates aim to destroy these residual holes. The production process for the emulsion creates the required defects in the crystal structure of silver chloride (AgCl) grains, by adding a suitable reducing agent (Gurney–Mott theory).

During development of the plate, a considerable amplification is produced, and a single silver atom released by a photon can give up to $1 0 ^ { 9 }$ atoms in the final image. The noise, or grain, of the plate is due to the formation of silver grains at the lattice defects without the action of an incident photon.

The quantum efficiency of a photographic emulsion is low, being of the order of $8 \times 1 0 ^ { - 3 }$ . This is indeed the main drawback of the photochemical effect. The threshold of the photochemical effect is governed by the value of the electron excitation energy in $\mathrm { A g C l }$ , or some other halide of this kind. This limits the sensitivity of plates at the infrared boundary of the visible $\lambda \le 8 0 0 \mathrm { n m }$ .

The detector using the photochemical effect is, of course, the photographic plate. As the bombardment of an emulsion by electrons can produce a latent image by the same process as the one described above, nuclear emulsions have been developed for the purpose of making latent images from electron impacts, and this is the principle of the electronic camera.

# Photoionisation of Gases

If the energy of incident photons is high enough $( \gtrsim ~ 1 0 ~ \mathrm { e V } ,$ ultraviolet or $\mathrm { X }$ -ray regions), an atom may be photoionised. The released electrons are then accelerated by an external electric field, and cause further ionisations by collision. The charges collected on the accelerating electrode are measured by a charge amplifier, or electrometer. The operating limit is reached when the multiplier effect leads to a discharge in the gas. Below this limit, the response is linear. It is not strictly correct to speak here of a quantum efficiency in the sense described earlier, for a photon may produce more than one electron, by double ionisation. However, extending the notion, $\eta$ will be used to denote the mean number of electrons obtained per incident photon. This quantity, which may exceed unity, is referred to as the quantum yield. The photoionisation cross-section in a gas is a function of the incident energy $E$ , varying as $E ^ { - 7 / 2 }$ . At around $1 0 \mathrm { k e V } ,$ , it becomes smaller than the Thomson scattering cross-section, and photoionisation is no longer usable.

The noble gases, neon, argon, and xenon, are used because of their high gain, the other common excitation mechanisms, such as rotation or vibration, being absent. An impurity, opaque to the UV radiation emitted by radiative de-excitation of the excited gas atoms, is added to the noble gas, in order to be able to use the energy for further ionisations. These impurities also de-excite the metastable states of the noble gas, by collisions.

The ionisation of gases is the basis of proportional counters. Wire chambers, invented by Georges Charpak,4 are used to detect events in the vicinity of particle accelerators. They are also based upon the photoionisation effect. The difference is that, in this case, the ionisation is not exclusively due to photons.

# Photon–Matter Interaction at High Energy $\mathbf { \Lambda } ( > 1 0 \mathrm { k e V } )$

The interaction of gamma rays with matter produces charged particles $\mathrm { e ^ { + } }$ and $\mathrm { e ^ { - } }$ ), which carry off the photon energy in kinetic form. The information concerning the energy and direction of the gamma photon is transferred to these particles, which interact, in turn, with other matter by ionisation, bremsstrahlung, annihilation, and so on. At low energies, loss of energy by ionisation is the dominant effect, the charged particles creating a series of electron–ion and electron–hole pairs. Most detectors use these charged pairs to detect the passage of a gamma photon, or to measure its energy by the number of charges produced.

The three main interaction processes are photoelectric absorption, Compton scattering, and pair creation.

# Photoelectric Absorption

In this process, all the photon energy $E _ { \gamma }$ goes to an electron in some atom. This interaction tends to occur with the inner shells (which have higher energy). The electron is ejected with kinetic energy equal to the difference between the incident photon energy and the energy required to extract the electron from its shell. As it propagates, the electron ionises atoms along its path. All the ions so formed then de-excite in a series of recombinations. In particular, the ion formed by the initial interaction of the photon de-excites, by emitting an X-ray photon which is characteristic of the shell of the ejected electron $( K , L )$ . If a thin layer of material is used for detection, some of these $\mathrm { X }$ -ray photons escape without further interaction, but in the majority of cases, they are not able to escape, and the totality of the energy of the gamma photon is then transmitted to the medium. The cross-section for the photoelectric interaction thus depends on the incident photon energy, and on the energy of atomic electrons in the medium. Discontinuities are observed at energies corresponding to the various shells of atomic electrons (see Fig. 7.18). However, to a first approximation, this cross-section is given by

![](images/84dea2a499230c880bb46ecb885d6e83d410243554f683c9e2edc3f1e9ac01dc.jpg)  
Fig. 7.18 Mass absorption coefficient as a function of incident photon energy. Note the $K$ shell ionisation discontinuities at low energy, and the energy dependence of the cross-section. (After Gursky H., Schwartz D., $X$ -ray Astronomy, Reidel, Dordrecht, 1974. With the kind permission of D. Reidel Publishing Company)

$$
\sigma _ { \mathrm { p } } = Z ^ { 4 . 5 } E _ { \gamma } ^ { - 3 . 5 } .
$$

Compton Scattering

In Compton scattering, only a part of the incident photon energy is transferred to the electron. The rest of the energy is carried away by the scattered photon, while the scattered electron, as in the case of the photoelectric effect, loses its energy mainly by ionisation of atoms along its trajectory. The scattered photon may also interact with the medium by a further Compton scattering, or by a photoelectric absorption. The directions of the incident and the scattered photon are determined by conservation of energy and momentum. The angle $\theta$ between them is related to the energy $E _ { \gamma }$ of the incident photon, and the energy $E _ { \mathrm { s } }$ of the scattered photon by

$$
\cos \theta = 1 - \frac { m _ { 0 } c ^ { 2 } } { E _ { \mathrm { s } } } + \frac { m _ { 0 } c ^ { 2 } } { E _ { \gamma } } .
$$

Figure 7.19 shows that the various scattering directions are not equiprobable. The dependence of the differential cross-section for the Compton interaction on the scattering angle $\theta$ is given by the Klein–Nishina formula

$$
\frac { \mathrm { d } \sigma _ { \mathrm { c } } } { \mathrm { d } \Omega } = \frac { 1 } { 2 } r _ { \mathrm { e } } ^ { 2 } \frac { E _ { \mathrm { s } } } { E _ { \gamma } } \left( \frac { E _ { \gamma } } { E _ { \mathrm { s } } } + \frac { E _ { \mathrm { s } } } { E _ { \gamma } } - \sin ^ { 2 } \theta \right) ,
$$

![](images/2d6369c8422911c3b53def0a08d38ce196fc146f8e8f4e16ee1c1a3e8116c49b.jpg)  
Fig. 7.19 Microscopic cross-section for Compton scattering, as a function of the scattering angle, at various energies. $r _ { \mathrm { e } }$ is the classical electron radius. The cross-section is given in $\mathrm { r a d } ^ { - 1 }$ , and is therefore an angular differential quantity

where $r _ { \mathrm { e } }$ is the classical electron radius $( r _ { \mathrm { e } } = 2 . 8 2 \times 1 0 ^ { - 1 5 } \mathrm { m } )$ , and $\mathrm { d } \varOmega$ the element of solid angle around direction $\theta$ D . The higher the energy, the more likely it is that the photon will scatter forwards. The total cross-section for the Compton interaction goes approximately as

$$
\sigma _ { \mathrm { c } } \propto Z E ^ { - 1 } .
$$

# Pair Creation

In this process, a high energy photon $E \gg 1 \mathrm { M e V }$ ) interacts with the electric field of a heavy nucleus to create an electron–positron pair. The photon energy is divided between the mass energy of the pair, equal to $1 . 2 2 \mathrm { M e V } _ { \mathrm { : } }$ , and their subsequent kinetic energy. Although the momentum carried by the nucleus ensures conservation of momentum for the reaction, its recoil energy can be neglected. In the centre of mass frame, the electron and positron are emitted in opposite directions. During propagation, they gradually lose their energy, mainly by ionisation, bremsstrahlung, and the Cherenkov effect. When the positron energy is low enough $( \approx 1 \mathrm { \ k e V }$ ), it will annihilate with an electron in the medium, by the inverse reaction, emitting two photons at $5 1 1 \mathrm { k e V }$ in opposite directions. These photons may escape, or they may in turn interact with the medium by Compton scattering or photoelectric absorption.

The cross-section for pair creation varies roughly as $Z ^ { 2 }$ , and is characterised by its threshold of $1 . 2 2 \mathrm { M e V } .$

# Comparison of Processes

The energy dependence of the three interaction processes mentioned above means that each one will be predominant in some energy domain determined by the interaction medium. At low energies, photoelectric absorption dominates, and at high energies, pair creation is the main channel. The energy domain for Compton scattering is situated between the two. Its width is highly dependent on the atomic number $Z$ of the material (Fig. 7.20), increasing for lighter materials. Generally speaking, for equal mass surface densities, light materials tend to scatter, and heavy materials tend to absorb.

Compton scattering and pair creation are the physical processes exploited in scintillation counters or scintillators, as well as in semiconductor detectors. The applications to $\gamma$ ray astronomy will be discussed in Sect. 7.6.

Thermal Effects. Calorimetry

Once the photon energy has been transferred to the solid, which constitutes the detector, and transformed into thermal excitations, the incident radiation is revealed by the slight temperature change it has produced, and which can be measured by the consequent variation in resistivity. In order for this to work correctly, the only condition is that the solid should be as absorbent to photons as possible, not only absorbing incident photons, but also any products of secondary events.

![](images/a45758c76fc21b07a127093324de7a7d2e93b3050ca34d66065ccd18bb0a1231.jpg)  
Fig. 7.20 Energy domains associated with each interaction process between $\gamma$ rays and a material, as a function of its atomic number Z. Curves correspond to loci of equal cross-sections for the two processes they separate

The thermal effect is used in detectors called bolometers, mainly in the infrared and submillimetre regions. It is also used in calorimeters, which measure the energy of $\gamma$ rays.

# 7.3.2 Detection of the Electromagnetic Field

At wavelengths above about $0 . 2 \ \mathrm { m m }$ , no quantum detector in the sense described above, involving release of one photocharge by one incident photon, has yet been devised. Across the whole of the radiofrequency region, other detection processes must be employed to measure the electric field of the incident wave. Its electromagnetic field, or the current it induces in an antenna, are applied to a nonlinear element called a diode or a mixer, usually superposing this field on the field of a local oscillator. The choice of non-linear element and mixer determines the final detection performance. We shall thus postpone discussion of these issues to a full presentation of the various elements.

# 7.4 Astronomical Detectors from X Ray to Submillimetre

Since the 1970s and 1980s, a genuine revolution has transformed the kind of detectors used in astronomy. The driving force here has been the emergence of microtechnologies, contributing to the design of light detectors across the board from X ray to submillimetre wavelengths with levels of sensitivity (quantum efficiencies) that have quickly superseded traditional photography, along with the various systems that had been developed to supplement it. In addition to this new level of performance, direct digitisation of the signal has greatly facilitated transmission, storage, and processing, and it has also brought mechanical advantages by making it easier to equip space observatories or remote missions.

In this context of rapid progress, yesterday’s detectors are often mentioned only for completeness, to describe the historical role they have played and explain references to them in the literature. However, one must not forget the extraordinary wealth of data contained in photographic astronomical archives, collected throughout the twentieth century and available today for the main part in digitised form (see Chap. 10). In the first section here, we consider more traditional detectors, mainly exploiting the generation and transfer of charge in semiconductors and appealing to microelectronics for their fabrication.

Outside this broad spectral range from X ray to submillimetre wavelengths, detectors in the $\gamma$ ray region on the one hand and radiofrequency receivers on the other have not witnessed similar revolutions. Figure 7.21 gives an overview.

![](images/ce93b361e5e4166219477dd2d08f80f38f13a93051d69f11bec873d0ad73ba6a.jpg)  
Fig. 7.21 Astronomical detectors

# 7.4.1 Noise Performance

At the beginning of this chapter, we discussed fundamental physical noise due to the Poissonian nature of the light–matter interaction or the thermodynamics of a thermal equilibrium. Of course, a given detector rarely achieves this ultimate level of performance. The true performance of a detector thus depends on what fluctuations it may add to those of the signal itself (signal noise) and to those of the detector environment (background noise). It is therefore important to qualify these real performance levels since they will influence the final quality of an observation.

# Detector Quantum Efficiency

The detector quantum efficiency (DQE) $\delta$ quantifies this notion. It extends the idea of quantum efficiency $\eta$ already introduced, but should not be confused with it. The definition is

$$
\delta = \mathrm { D Q E } = \frac { \left( \langle \Delta N ^ { 2 } \rangle / \overline { { N } } ^ { 2 } \right) _ { \mathrm { r e a l \ d e t e c t o r } } } { \left( \langle \Delta N ^ { 2 } \rangle / \overline { { N } } ^ { 2 } \right) _ { \mathrm { i d e a l \ d e t e c t o r } } } \ .
$$

It is straightforward to show that, if the detector, of quantum efficiency $\eta$ , introduces no further fluctuations, only the Poisson statistics of the incident photons remains, and

$$
\begin{array} { c } { { \langle \Delta N ^ { 2 } \rangle _ { \mathrm { i d e a l } } = \overline { { { N } } } \ , } } \\ { { \langle \Delta N ^ { 2 } \rangle _ { \mathrm { r e a l } } = \eta \overline { { { N } } } \ , \qquad \overline { { { N } } } _ { \mathrm { r e a l } } = \eta \overline { { { N } } } _ { \mathrm { i d e a l } } \ . } } \end{array}
$$

In this case, $\delta = \eta$ , which justifies the name given to $\delta$ .

DAs well as the fundamental fluctuations linked to the radiation itself, a detector may be subject to amplifier noise and readout noise.

# Amplifier Noise

Some photoelectric detectors (photomultipliers, the avalanche effect in avalanche diodes, or CCDs in the X-ray region) exploit the following sequence of events upon impact by a photon: 1 photon $ \eta$ photoelectrons amplification $\to \eta g$ electrons !measurement. The amplification gain $g$ ! !is a random variable of mean $\overline { { g } }$ and !standard deviation $\sigma _ { g }$ , from one photon impact to another. The noise this creates in the signal is not additive but multiplicative, degrading the DQE by the factor

$$
\left( \frac { 1 + \sigma _ { g } ^ { 2 } } { \overline { { g } } ^ { 2 } } \right) ^ { - 1 } .
$$

# Readout Noise

Some detectors (e.g., CCDs, see Sect. 7.4.6) measure at regular intervals the photocharges accumulated since the last measurement. Each charge transfer is then accompanied by a fluctuation, whose standard deviation is measured in numbers of electrons per reading. This number is the readout noise, or noise equivalent charge (NEC). Being a standard deviation, it will be denoted $\sigma _ { \mathrm { R } }$ , given in rms electron number.

The value of $\sigma _ { \mathrm R }$ for a given device may depend on the rate at which readings are made, and therefore on the integration time $T$ . In general, $\sigma _ { \mathrm R }$ increases as $T$ decreases. However, $\sigma _ { \mathrm R }$ no longer exhibits the standard $T ^ { 1 / 2 }$ dependence of integrated noise (see below).

The DQE is degraded by a factor

$$
\left( \frac { \sigma _ { \mathrm { R } } } { \overline { { g } } \eta \sqrt { \overline { { N } } T } } \right) ^ { 2 } \ ,
$$

so that, in the most general case,

$$
\delta = \eta \left[ \left( 1 + { \frac { \sigma _ { g } ^ { 2 } } { \overline { { { g } } } ^ { 2 } } } \right) + { \frac { \sigma _ { \mathrm { R } } ^ { 2 } } { \overline { { { g } } } ^ { 2 } \eta ^ { 2 } \overline { { { N } } } T } } \right] ^ { - 1 } ,
$$

where $\overline { { N } }$ is the mean photon flux per second, $T$ the readout time, the fluctuations being quadratically additive.

Problem 7.4 concerns the expression for the DQE when the dark current is included, and also an extension of the definition of $\boldsymbol { \delta }$ to the case of an imaging detector, including spatial frequencies.

# 7.4.2 Photographic Plates

Considerable progress has been made in the sensitivity of photographic plates, over the period since their invention, going from a flux of $1 0 ^ { - 4 } \ \mathrm { J } \mathrm { c m } ^ { - 2 }$ as required to print a plate in 1850, to a flux $1 0 ^ { 6 }$ times lower a century later. We can nevertheless consider that it has reached its limit today. The main advantages are simplicity of use, ability to integrate low fluxes over long periods, and, above all, the high number of pixels that can be simultaneously exposed (up to $1 0 ^ { 1 0 }$ ). It is its own mass memory.

![](images/00493fefe1af14e4636cbe8072174a21a6706bbf445574b1d77a7448c02ca7d3.jpg)  
Fig. 7.22 Left: Microphotometry of a photographic or electronographic plate. The light source L emits a ray, received by the photosensitive cell C. The intensity i measured, together with the $x$ and $y$ coordinates, read by a position sensor, are digitised. L performs a two-dimensional raster scan. Right: Isophotes of the jet emerging from the quasar 3C 273 obtained by digitising the plate. Note the oscillation of the jet around its mean direction. Picture courtesy of Wlerick ´ G., Lelievre G., Canada–France–Hawaii telescope, wide field electronic camera, U filter (near\` ultraviolet), exposure $1 6 5 \mathrm { m i n }$ , 1984

The drawbacks are its non-linearity, its rather restricted dynamic range, the grain effect, and also the need to use a microdensitometer (Fig. 7.22) to transform analogue information, stored in the form of blackening on the plate, into digital information, which can then be processed quantitatively. This point by point scanning process is still used by the modern scanner to digitise documents.

In order to set up digital archives of photographic records like those described in Chap. 10, machines have been built to measure and digitise astronomical photographic plates. These machines, which were developed in the 1990s, are capable of processing enormous numbers of pixels. Examples are MAMA, or Machine $\grave { a }$ Mesurer pour l’Astronomie, in France, and COSMOS, in the United Kingdom.

The registered signal is measured by the density of the emulsion. If the pixel being examined by microdensitometer transmits a fraction $I / I _ { 0 }$ of the incident radiation, the density $d$ is defined by

$$
d = - \log _ { 1 0 } { \frac { I } { I _ { 0 } } } .
$$

The photographic plate remains a useful detector but, despite its high number of pixels (up to $\sim 1 0 ^ { 1 0 }$ ), it has now been superseded by CCD arrays which, at the time of writing (2007), can count up to $1 0 ^ { 8 }$ pixels.

# 7.4.3 Photomultipliers and Classical Cameras: X Ray, UV, and Visible

Once again, these detectors played an important role over the period 1950–1990, but were then completely superseded by CCDs and similar detectors. They worked by photon counting.

# Photomultipliers (PM)

For many years regarded as the ideal detector, the photomultiplier (abbreviated to PM) consists of an evacuated tube containing a series of electrodes, the first of which is exposed to the radiation. When a photoelectron is released, it is extracted from the photocathode by means of a first dynode, or positive electrode, creating secondary electrons by impact. These are in turn accelerated, causing further electrons to be released, and the process continues. The final current is measured with a charge amplifier or electrometer. The photomultiplier nevertheless remains widely used in high energy $\gamma$ -ray) detectors, where it detects the photons induced by interactions and counts them (see below).

Based on the photoelectric effect, there is no sensitivity threshold, and indeed the photomultiplier can detect a single quantum. It is perfectly linear up to the point where the flux is high enough to cause an electron cascade, which destroys the electrodes. Its sensitivity is limited to the region 20 to $1 2 0 0 \ \mathrm { n m }$ , by cascade effects in the far UV, and the photocathode response in the near IR. Figure 7.14 gives the response and the quantum efficiency. The PM has almost no spectral selectivity, and its response time is extremely short (the transit time of the electrons between dynodes, which is several nanoseconds). It clearly has no multichannel capabilities (except for certain configurations, which channel the photoelectrons and can discriminate between points of the photocathode), and the response of the photocathode may vary somewhat across its surface. These characteristics are summarized in Table 7.4.

At non-zero temperatures, thermoelectronic emission from the cathode produces accelerated electrons, even when there are no incident photons. Richardson’s law gives the value of the current density $j$ extracted at temperature $T$ , for an extraction potential of $E _ { \mathrm { s } } / e$ :

$$
\begin{array} { l } { { \displaystyle j = \frac { 4 \pi e k ^ { 2 } } { h ^ { 3 } } \left( 1 - \rho _ { \mathrm { e } } \right) T ^ { 2 } \exp \left( - \frac { E _ { \mathrm { s } } } { k T } \right) } } \\ { { \displaystyle = 1 . 2 \times 1 0 ^ { 6 } \left( 1 - \rho _ { \mathrm { e } } \right) T ^ { 2 } \exp \left( - \frac { E _ { \mathrm { s } } } { k T } \right) \mathrm { A m } ^ { - 2 } , } } \end{array}
$$

where $\rho _ { \mathrm { e } }$ is the coefficient of reflection, measuring the probability of the electrodes recapturing an emitted electron. At $T = 3 0 0 \mathrm { K }$ , and for $S = 1 \mathrm { c m } ^ { 2 }$ , $E _ { \mathrm { s } } = 1 \mathrm { e V } ,$ it follows that $I = j S = 0 . 2 \mathrm { n A }$ . D DThis is a large dark current. For comparison, with $\eta = 0 . 5$ D D, a flux of one photon per second would produce a current of $0 . 8 \times 1 0 ^ { - 1 9 }$ A (Table 7.4).

The dark current decreases rapidly with $T$ (if the photomultiplier is cooled with dry ice or a Peltier refrigerator). It also decreases when $E _ { \mathrm { s } }$ increases (this concerns UV photocathodes). Although the mean value $\begin{array} { l l l } { \langle j S \rangle } & { = } & { \left. i _ { \mathrm { B } } \right. } \end{array}$ of the dark current can be subtracted from the hmeasurements, its fluctuations $\langle \ S i _ { \mathrm { B } } ^ { 2 } \rangle = 2 e \langle i _ { \mathrm { B } } \rangle \Delta f$ , where $\Delta f$ is the passband of the electric filter h i D h iwhich follows the PM, set a fundamental limit to the sensitivity (Problem 7.1).

Table 7.4 Photomultipliers   

<table><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Format</td><td>Up to 8×8pixels</td></tr><tr><td>Quantum efficiency</td><td>0.43 (Ag-O-Cs at 800 nm) to 0.1</td></tr><tr><td>Spectral response</td><td>Wide</td></tr><tr><td>Temporal response</td><td>Nanosecond</td></tr><tr><td>Size</td><td>About 10 cm² (cathode)</td></tr><tr><td>Noise</td><td>Dark current OB ~ 10 counts Hz-1/2</td></tr><tr><td>Polarisation</td><td>Insensitive</td></tr></table>

With the above current, and taking $\Delta f = 1 \ : \mathrm { H z }$

$$
\langle \ S i _ { \mathrm { B } } ^ { 2 } \rangle ^ { 1 / 2 } = 9 \times 1 0 ^ { - 1 5 } \mathrm { A H z ^ { - 1 / 2 } } .
$$

The signal can be measured in various ways.

• By integration of charge: a filter circuit (resistor and capacitor), or an integrating circuit (running mean), provides a continuously variable analogue voltage. By counting photon arrivals: a counter registers each burst of electrons, whatever their number and whatever the duration of the burst. The signal is digitised, and the intensity and duration of the pulses can be used to protect against unwanted signals.

# Other Photon Counting Detectors

Much effort has been made to combine the advantages of the photoelectric effect in vacuum and the detection of 2D images. Here we give a brief overview of the sometimes imaginative systems devised through 1950–1990, but which have for the main part been superseded by CCDs (see below).

Electronic Camera (or Electronographic Tube)

Invented and first exploited by A. Lallemand, the electronic camera consists of a photocathode on which an image $I ( x , y )$ is formed. The photoelectrons produced are accelerated by electron optics with electrostatic or magnetic focusing, and then an electron image is formed on a high contrast photographic plate (nuclear emulsion). The camera can operate at extremely low levels of intensity. Indeed, it does not exhibit the threshold effect of the normal photographic plate, and can almost detect single photoelectrons. The time integration capacity in long exposures is excellent (there is no fogging), and the advantages for astronomical photography are clear, particularly for faint objects, such as quasars, which require an accumulation of long exposures (Fig. 7.22).

Image Intensifiers Using Microchannel Plates

The input for an image intensifier is an image, formed by a low flux of photons, at a certain wavelength. The output from such device consists of an image with the same number of pixels. Each output pixel behaves as a source of photons, whose number is proportional to the number of incident photons, but whose wavelength is different. The system is therefore characterised by a gain g.

![](images/76e8689a3c65489acf671def8cdb2015d219d3089da7e071d857c10a632ec891.jpg)  
Fig. 7.23 (a) Microchannel in a semiconductor, constituting one element of a microchannel plate. The incident photon releases a photoelectron, which is accelerated by the field $E$ , and multiplied by successive electronic collisions. The phosphor is excited at the exit and emits a large number of photons. (b) The phosphor emits across a wide solid angle and this requires fibre optic coupling. Each fibre is in contact with the phosphor and transmits the photons corresponding to one pixel to the CCD detector. The figure shows straight channels to simplify, but in general they are curved in order to prevent ion movement

The microchannel plate or channeltron is an intensifier, exploiting the photoelectric effect in solids. The photoelectrons are guided and multiplied in a channel with accelerating voltage gradient (Fig. 7.23). The final impact is on a phosphor, which emits in the visible. The incident photons may be visible, ultraviolet, or soft X rays. Several microchannel plates can be arranged in series, in order to increase the amplification factor.

A microchannel plate has no information storage capacity, and so could not be used alone. Hence it is coupled to a CCD, and the two together are referred to as an intensified CCD.

# Photon Counting Television

Inspired by the tubes developed for commercial television in the 1950s, many improvements were brought to bear to increase their sensitivity, to arrive at a genuine photon counting device (Fig. 7.24). A whole series of astronomical detectors was thereby developed.

Vidicon Tubes and Derivatives. Television tubes use the photoelectric effect in silicon. Released photoelectrons are stored in a layer of microcapacitors, which are periodically recharged (25 times a second) by a scanning electron beam, the Vidicon tube. The recharge current of the microcondenser is modulated by the light intensity. Passing through the charge resistance of the target, it produces a potential difference, which is the video signal, at a frequency of a few tens of MHz. The readout noise is high $( \sigma \sim 2 \times 1 0 ^ { 3 }$ electrons pixel $^ { - 1 } \mathrm { H z } ^ { - 1 / 2 }$ ), and is easily observed on the TV screen: the background, in the absence of any signal, appears as a random pattern of white on black, like snow.

![](images/062c1905c36161a93b188e2142850258b49914a08a435e0e990c288d5a2b4545.jpg)  
Fig. 7.24 Photon counts, as they appear on the TV screen of a Nocticon tube (exposure $2 5 ~ \mathrm { m s }$ ). Note the variable gain, manifested by the varying brightness of the events. Note also the noise events, fainter and easy to discriminate. The image is read on a $5 1 2 \times 5 1 2$ CCD array. Each event is digitally centered. (Observatoire de Marseille, image due to Boulesteix J. in the 1980s)

In the secondary electron conduction tube or SEC tube, the photoelectrons are accelerated onto a target where they produce a secondary emission of electrons. The latter are read by standard TV scanning. The gain of around 1 000 is obtained at the cost of high non-linearity.

In the silicon intensified target (SIT) tube, or the electron bombarded silicon (EBS) tube, the photoelectrons are accelerated onto a silicon target at sufficiently high energy to create several thousand electron–hole pairs upon each impact. These are then collected by an array of junctions or diodes. The electric field of the diode separates them and they discharge a microcapacitor, which is then recharged by the scanning electron beam. An analogous principle is used in the electron bombarded CCD (EB-CCD).

The Photon Counting Camera. The image photon counting system (IPCS) combines the linearity and sensitivity of the electronographic camera with the convenience of the TV camera, and a capacity for digital storage of information, which can be processed at a later date. It was developed by Alec Boksenberg5 in Cambridge (UK), and was soon being widely used in astronomical observatories, until it was replaced by CCDs. A photon counting camera was designed and made in Europe to equip the Hubble Space Telescope in the 1990s. This camera, the Faint Object Camera (FOC), was used to make the first deep sky observations with this telescope, before being replaced in orbit by CCD detectors, installed by astronauts during servicing missions.

This camera includes an image intensifier : photons incident on the photocathode generate photoelectrons, which are accelerated and focused magnetically onto a phosphor. The latter re-emits photons upon each impact. The amplification process is repeated in three successive stages, to give a final gain of $1 . 3 \times 1 0 ^ { 5 }$ .

The intensifier is followed by optics. The image, formed on the output phosphor of the intensifier, is re-formed by an objective on the entry side of a cylindrical bundle of optical fibres, which define each pixel with great precision. The photons are then channelled onto the photocathode of an EBS television tube. Each photon impact is converted into a pulse in the output video signal, and the timing of each pulse is used to determine exactly which event should be assigned to which pixel in the image. The digitised video signal increases by one the number of photons so far counted in the pixel.

This sequence of devices had many advantages: the system involved almost no noise, reading was non-destructive, the $5 1 2 \times 5 1 2$ pixel format was good at the time, and photon impacts could be accurately localised. Figure 7.24 gives an example of the instantaneous image obtained using a photon counting camera.

Other versions of the photon counting camera were developed during the 1980s, such as the connection of two image intensifiers in series, followed by a CCD. Another idea couples an electronic camera (photocathode with acceleration of the photoelectrons) to a CCD operating in an unusual but effective way: bombarded by the accelerated electrons, each pixel releases a large number of charges which are then read by the readout circuit (EB-CCD, or electron bombarded CCD).

# Avalanche Photodiodes

Consider a junction which is strongly biased in the opposite direction, and hence non-conducting. The diode material being silicon, an incident photon generates a photoelectron. The very high bias (several $\mathrm { \Delta V _ { \mathrm { \ : \mu } m } } ^ { - 1 }$ ) accelerates this electron, which photoionises in series the Si atoms it encounters. The process is amplified by avalanche multiplication until a current pulse is created across the poles of the diode. This current pulse may reach $1 0 ^ { 9 }$ charges, which is easy to detect above the intrinsic noise of the diode. Count rates can reach $1 0 ^ { 6 }$ photocharges per second.

This device has a very fast response, reaching several nanoseconds. The photoimpulses can thus be counted individually, a pause of several hundred nanoseconds being required to restore the charges (quenching). A promising application may be the study of radiation coherence by correlation.

The great advantage of these ‘solid-state photomultipliers’ is that they can work in counting mode (and therefore with the limit imposed by the Poisson noise of the signal), whilst benefiting from the excellent quantum efficiency of silicon $( > 0 . 6 )$ . An extension of this idea to the near infrared, using germanium, can be envisaged. Their limitation is two-fold. Firstly, the diodes are cumbersome and it is difficult to assemble them into arrays, although arrays containing several units or several tens of units became available by the 2000s, and it may be that $1 0 0 0 \times 1 0 0 0$ arrays will appear one day. Secondly, the recombination of charges produces a flash of light, and although this presents no problem when limited to a single diode, it soon becomes problematic in the case of arrays, because it leads to cross talk between neighbouring pixels.

Compared with photomultipliers, which are their close relatives, they are still limited by the smaller dimensions of their photosensitive zone. Nevertheless, they are fast developing, and sizes up to $2 0 0 ~ \mathrm { m m } ^ { 2 }$ have been achieved. In 2007, these detectors face serious competition from L3- CCDs (see below).

# 7.4.4 X-Ray Detection (0.1–10 keV)

Here we discuss a family of photon counting detectors developed hand in hand with the emergence of X-ray astronomy, and which in the 2000s have gradually been superseded by CCD detectors, presented later.

# Proportional Counters

Figure 7.25 gives a schematic view of a proportional counter. The window enclosing the gas must be thin, and it is the specific combination of the absorption properties of this window and those of the gas which determines the spectral response of the counter. Table 7.5, which is not exhaustive, thus specifies the spectral ranges that can be covered. Note the extreme thinness of the windows, and the properties of the ionisation thresholds in the absence of the window.

The energy resolution is, like the quantum efficiency, determined by the combination of the gas properties (photoelectric cross-section of the gas) and those of the window (Fig. 7.26). This resolution is determined by the Poisson statistics of the photoelectrons, and is thus proportional to ${ \sqrt { E } } .$ In general,

$$
\Delta E _ { \mathrm { k e V } } \approx 0 . 4 \sqrt { E _ { \mathrm { k e V } } } ~ ,
$$

the proportionality factor dropping to 0.2 in gas scintillation proportional counters (GSPC).

![](images/58a5964ee790f73d1f96829698496d5769e50a333d68f012d652ca1c1451cb0e.jpg)  
Fig. 7.25 Exploded view of a proportional counter

Table 7.5 Proportional Counters   

<table><tr><td>Window</td><td>Thickness [μm]</td><td>Gas filling</td><td>Spectral response [nm]</td></tr><tr><td>Beryllium</td><td>125</td><td>Neon or argon</td><td>0.02-0.8</td></tr><tr><td>Aluminium</td><td>6</td><td>Neon</td><td>0.02-0.6 and 0.8-1.6</td></tr><tr><td>Mylar</td><td>6</td><td>Nitrogen or helium</td><td>0.02-1.5 and 4.4-6</td></tr><tr><td>Nitrocellulose</td><td>0.1</td><td>Argon</td><td>&lt;30</td></tr><tr><td>No window</td><td>1</td><td>Helium</td><td>&lt;50.43</td></tr><tr><td>No window</td><td>1</td><td>Xenon</td><td>&lt;102.21</td></tr><tr><td>Lithium fluoride</td><td>1000</td><td>Ethyl bromide</td><td>104-120</td></tr><tr><td>Quartz (silicon)</td><td>1000</td><td>Tri-n-propyl amine</td><td>160-171.5</td></tr></table>

![](images/cedde8b5b0bf0669ad844d1d9ef4af52ea8f28d02ad9b587ecab5099185e67e6.jpg)  
Fig. 7.26 Quantum efficiency of a proportional counter filled with argon (column density $5 . 4 \mathrm { m g } \mathrm { c m } ^ { - 2 }$ ). The effect of different windows is shown. From Giacconi R. and Gusky H., $X$ -Ray Astronomy, Reidel, Dordrecht, 1974. With the kind permission of D. Reidel Publishing Company

The proportional counter has no intrinsic noise, but suffers from amplification noise (gains of the order of $1 0 ^ { 3 } – 1 0 ^ { 5 }$ ). Only the statistics of the signal, whether it be the source or a background signal, can therefore create fluctuations, and this alone will determine the signal-to-noise ratio. This idea was extended in the 1970s to the position sensitive proportional counter, which equipped the camera of the Einstein satellite, launched in 1978.

# Microchannel Plates

Already described in the context of image intensifiers used in the detection of visible and ultraviolet radiation (see Sect. 7.4.3), this device can be used to make multichannel detectors, without energy resolution, for energies up to several keV. Figure 7.27 shows an image obtained with such a detector on the Exosat satellite, launched in 1982, the first X-ray satellite of the European Space Agency.

# 7.4.5 Solid-State Imagers

These detectors exploit the photoelectric effect in solids. Their multichannel character results from integrating elementary photoconducting pixels into an integrated array, which includes a readout circuit. State-of-the-art microelectronics is used in their manufacture. They have developed considerably since their introduction in 1970 and the trend continues, with improved performance in sensitivity, dynamic range, format, miniaturisation, reliability, and integrated intelligence. They produce a digital output signal which is easy to process and have a temporal integration capacity.

![](images/da696558ddc963d397b7726dec84065693c81b1a6496be6192dadcf118701685.jpg)  
Fig. 7.27 Historical X-ray image of the supernova remnant Cassiopea A, obtained with the microchannel camera (Channel Multiplier Array, or CMA) on the European satellite Exosat. Spectral band $0 . 1 { - } 2 \mathrm { k e V } .$ Spatial resolution 18 arcsec, on the optical axis. (Picture provided by the Exosat Observatory, European Space Agency, 1985)

These detectors are known generically as solid-state imagers. The term covers many variations, such as Reticons, charge coupled devices (CCDs), and charge injection devices (CIDs). At visible wavelengths, it is the CCD exploiting the photoconductivity of silicon which has taken the lead since the end of the 1980s. For infrared detection, microelectronic integration techniques have made it possible to superpose a suitable photosensitive material for the given wavelength and readout circuits, thus constructing the equivalent of a CCD at these wavelengths. Finally, recent developments, in the 2000s, have created a competitor for the CCD, namely the CMOS (complementary metal oxide semiconductor) detector.

The strategy in solid-state imagery is to accept a gain close to unity, but to reduce the readout noise $\sigma _ { \mathrm { R } }$ to near zero, so that the detector quantum efficiency ı attains the value of the photoelectric quantum efficiency $\eta$ . The trend is also to make the latter tend toward unity.

# 7.4.6 Charge Coupled Device (CCD)

The basic structure of a charge coupled device is a metal–oxide–semiconductor (MOS) capacitance. It is a capacitance consisting of an insulator sandwiched between a metal electrode and a semiconductor exhibiting the photoelectric effect (Fig. 7.28). The insulator may be formed by direct oxidation of the semiconductor ( $\mathrm { S i O } _ { 2 }$ on silicon), or it may be deposited by vaporisation, sputtering, or condensation in the vapour phase. The semiconductor is usually silicon.

![](images/c750034d4495e563d110c5b0dd30229d3ea503f7d80b5d3c756da86534f34d30.jpg)  
Fig. 7.28 Metal–oxide–semiconductor (MOS) capacitance. The voltage applied at the upper electrode acts on mobile charges in the $n$ -type semiconductor. For $V > 0$ , the majority carriers $( \mathrm { e } ^ { - } )$ accumulate at the surface under the insulator. For $V < 0$ , the majority carriers $( \mathrm { e } ^ { - } )$ are repelled far from the surface, creating a depopulated or depletion zone, without mobile charges, which is thus insulating. For $V \ll 0$ , a positively charged inversion layer is formed at the surface, and this is a potential well for the minority carriers ( $^ +$ holes). The photocharges caused by incident photons $( h \nu )$ C modify the surface potential. The lower electrode can be made transparent to radiation, freeing the upper part for the electrical connections of the readout circuit

The applied potential difference creates an electric field which modifies the charge distribution in the semiconductor. A potential well appears, capable of storing in the capacitance any photocharges released in the semiconductor by an incident photon, as well as any thermally excited mobile charges. This last phenomenon makes it necessary to cool solid-state imagers, in order to reduce the thermally generated signal.

Each pixel of the CCD comprises a capacitance of this kind, and the full set of pixels is organised in a 2D array forming the detector array of $N \times M$ pixels which specifies the $N \times M$ format of the CCD. Once the charges have accumulated, the CCD contains a readout circuit, using field effect transistors (FET) that function as switches and also a clock, which transfers the charges of a given column one after the other into an output series register and then, having done this, moves on to the next column, until all the stored charges have been read. The charges are transformed into successive voltage pulses by the series register, and these are amplified then digitised in a synchronised way by the clock controlling readout. The CCD controller oversees the electronic functions. Photosites have been gradually reduced in size with progress in silicon etching techniques, to reach a few micrometres.

Figure 7.29 illustrates the idea of charge transfer driven by a clock-controlled variation of potential at successive electrodes in rows and columns. The output signal is thus a video-type signal, in which each pulse is proportional to the stored photocharge. The image can then be generated at the standard TV rate of 25 frames per second (in Europe), but it can also be read at an arbitrarily slow rate (long exposures).

![](images/ddfa0d63d2a9e75a749146dd6fc1337323b21d582913a96648d918d85e2a9737.jpg)  
Fig. 7.29 Principle of charge transfer in the CCD detector. Each pixel is defined by three electrodes. Electrons are represented by balls, which move within the potential wells created by the electrodes, and evolve in time. (After Fauconnier T., doctoral thesis, University of Paris VII, 1983)

When all functions, i.e., release of photocharges, storage, and transfer to the output register, are handled within the same pixel, the CCD is said to be full frame. However, it also possible to separate these functions in the so-called frame transfer $C C D$ . A $2 N \times N$ array is divided into two parts, with one $N \times N$ piece used to generate the charges and the other $N \times N$ piece storing them. If the transfer from one to the other is very fast $\mathit { \Theta } _ { \prec \phantom { \infty } 1 0 }$ ms for a $1 \mathrm { k } \times 1 \mathrm { k }$ format, the time depending on the number of rows), the use of time is optimal, since the charges can be read out while the exposure is still underway. This doubles the size of the final array, which may complicate image formation when a large focal plane is to be covered by CCDs placed side by side.

# Quantum Efficiency. Thinned CCDs

Impressive progress has been made with the quantum efficiency of CCDs in the visible wavelengths $( 4 0 0 { - } 9 0 0 ~ \mathrm { n m } )$ . Figure 7.30b shows efficiencies almost equal to unity in the extreme red, and greater than $50 \%$ in the blue. Most of the loss of efficiency is due to reflection losses. There is a great reduction in sensitivity when CCDs are used in the blue $\leq 4 0 0 \ \mathrm { n m }$ ) and ultraviolet, because silicon can absorb photons at these wavelengths.

![](images/a141bc568903b18aff5619f22c3c66328f0a78163dd175dd6b8f6b1c4ac5563d.jpg)  
Fig. 7.30 (a) Schematic cross-section of a thinned CCD. The limited extent of the potential wells is shown, as is the depletion zone that the photocharges must reach. (b) DQEs for front illumination and for anti-reflectance treatment. (After Lesser M., 1994)

The electrodes placed on the front face absorb the radiation. This led to the idea of illuminating the CCD from behind, so that the radiation would only encounter silicon immediately effective in photoelectric conversion. However, as a CCD was around $3 0 0 ~ { \mu \mathrm { m } }$ thick, the photocharges had to cover such a distance before encountering the potential wells, whose extension under the electrodes barely exceeds $1 0 ~ { \mu \mathrm { m } }$ , that the charges would never be able to recombine. Illuminating the CCD from behind therefore required the CCD to be thinned down, to a thickness of about $1 5 ~ { \mu \mathrm { m } }$ . A compromise must be found between the capture of photocharges and their generation, which requires a photon path in the silicon that increases with the wavelength. Thinning is thus necessary in the blue, and of course for UV and $\mathrm { X }$ -ray detection, but unfavourable for the high quantum efficiency in the red. It is impossible to make silicon wafers of this thickness directly. A standard CCD is thus turned round, with its front face stuck onto a suitable substrate, and then its back face is thinned by mechanical or chemical processes, passivated (antioxidant treatment), and treated to reduce reflection losses (Fig. 7.30a).

# Readout Noise

The transfer of photocharges and ensuing amplification are accompanied by two sources of noise, whose (quadratic) sum is generally observed. On the one hand, there is a fluctuation in this number of charges. This has thermal origins and depends on the capacitance storing the charges. On the other hand, there is a further fluctuation $\sigma _ { \mathrm R }$ due to transfer and amplification of the signal, called the readout noise of the CCD. Each of these terms is reduced by cooling the CCD, generally to the temperature $7 7 ~ \mathrm { K }$ of liquid nitrogen.

The ultimate readout noise depends on the read rate. Indeed, the noise level decreases as the CCD is read more slowly, going as $1 / f$ in the amplification stages. But increasing formats implies reading a larger number of pixels, and this has consequences for the readout noise, which has decreased at the time of writing (2007) to a few photocharges (1–2 electrons rms) at rates of 50 kilopixels per second (or 20 s to read a $1 0 2 4 \times 1 0 2 4 \mathrm { C C D } )$ . Very high readout rates $\leq 1$ Mpixels per  second) are sought for certain applications, such as image or wavefront reading in times less than the coherence time of atmospheric turbulence (e.g., in adaptive optics). The objective is a noise $\sigma _ { \mathrm { R } } ~ \approx ~ 2$ electrons rms for a readout rate of the order of 1 Mpixel per second. Another solution to the problem of increasing the readout rate, without increasing the readout noise, consists in having parallel exits, by dividing the CCD into 2, 4, or 8, with a separate exit for each part.

For a fixed number of generated photocharges, let us evaluate the number of charges read. Just as it was possible to characterise the thermal noise output by a resistance $R$ at temperature $T$ (see Sect. 7.2.2), in terms of a power $4 k T R \Delta f$ , it can be shown that, across a capacitance $C$ , the charge $q$ has variance

$$
\sigma _ { q } ^ { 2 } = k T C \Delta f .
$$

This is therefore the fundamental limit of the noise across $C$ . Assuming a capacitance of 50 femtoF, below which it is difficult to go, this gives $\sigma _ { q } = 4 6 \mathrm { e } ^ { - }$ at $7 7 ~ \mathrm { K }$ , and $1 0 \mathrm { e } ^ { - }$ at $4 \mathrm { K }$ . It is thus useful Dto reduce this capacitance, but that in turn would reduce the maximum amount of charge that couldbe stored, whence a lower flux would saturate the CCD.

Concerning the maximum charge that can be stored by this capacitor under a voltage $V$ , namely $C V$ , a value of $V = 1$ gives $6 . 2 5 \times 1 0 ^ { 6 } \mathrm { e } ^ { - }$ per pF. There is thus a simple relation for the dynamic D range of this capacitor, in the absence of any other source of noise which would reduce it:

$$
\mathrm { d y n a m i c ~ r a n g e } = V { \sqrt { \frac { C } { k T } } } .
$$

An important property of CCDs is their linearity up to a high charge storage capacity, around $1 0 ^ { 6 }$ charges per pixel in the best cases. This makes possible very long exposures of faint objects, with no increase in readout noise (Problem 7.11).

Table 7.6 CCD detectors. The table gives mean values, open to improvement in the future-  

<table><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Dynamic range</td><td>≤ 10 charges pixel-1</td></tr><tr><td>Quantum efficiency</td><td>η ≥ 0.8 between 500 and 900 nm</td></tr><tr><td>Spectral response</td><td>Normal CCD: 400-1100 nm Thinned CCD: soft X ray (0.1-50 keV)</td></tr><tr><td>Temporal response</td><td>Around 50 ms</td></tr><tr><td>Format</td><td>Up to 2 048 × 4096 pixels</td></tr><tr><td>Noise</td><td>Readout Or ~ 2-5 erms depending on rate</td></tr><tr><td>Information storage</td><td>Digital, destructive readout</td></tr></table>

Very long exposures nevertheless increase the chances of superposing a further type of noise in addition to readout noise, for example, due to the impact of cosmic rays, which is random and may saturate a pixel. Such events can occur both in space and at ground level, particularly during solar flares, or during a crossing of the South Atlantic anomaly (see Sect. 2.9.2). They then contribute to background noise. A specific treatment of the pixels can reduce this noise for spaceborne CCDs (see below).

# CCD Formats

At the time of writing (2007), the $2 0 4 8 \times 4 0 9 6$ format is a technological limit that would appear to be rather hard to improve upon, given the great difficulty involved in maintaining uniformity over surfaces including several tens of millions of pixels. In 2007, it is commonplace to make CCDs with format $1 0 2 4 \times 1 0 2 4$ (usually denoted by $1 \mathrm { k } \times 1 \mathrm { k } )$ ), but $4 \mathrm { k } \times 4 \mathrm { k }$  is possible. Beyond this, it is easy to place CCDs side  by side in order to construct large arrays. The present trend is therefore towards the tiling of focal planes by juxtaposition, which can give formats up to $8 \mathrm { k } \times 8 \mathrm { k }$ , or $8 1 9 2 \times 8 1 9 2$ . There is, of course, a dead space between the CCDs, which can be reduced to the area of a few dozen pixels. If one of the four sides of the CCD is reserved for electrical contacts, then juxtaposition can make a $4 \times 2$ array.

For example, the Megacam camera of the Canada–France–Hawaii telescope comprises 40 thinned CCDs, each with format $2 \mathrm { k } \times 4 . 5 \mathrm { k }$ , laid side by side to cover a total field of 1.4 degrees with $3 . 6 \times 1 0 ^ { 8 }$ pixels. The size of the CCDs is $1 3 . 5 \mu \mathrm { m }$ . Each exposure lasts at most $2 0 \mathrm { s }$ (to avoid risk of saturation) and provides 0.77 Gbits of data. A specific processing centre called Terapix (see Chap. 10) has been set up to process this considerable volume of information (Table 7.6).

# Dark Current

Thermal generation of charges in the CCD creates a signal, even when there is no illumination. This signal, mainly produced by traps at the $\mathrm { S i } { - } \mathrm { S i O } _ { 2 }$ interface, must therefore be calibrated on average and subtracted from the signal, an exercise referred to as doing a dark frame subtraction. The dark current decreases with temperature. It can be significantly reduced by means of a charge sloshing or dithering mode, which modulates readout voltages faster than the lifetime of surface states.

# The Low Light Level CCD (L3-CCD)

As the name suggests, the low light level CCD or L3-CCD is one that operates at low light levels. Here the readout noise becomes negligible, up to high readout rates $( \sim \mathrm { ~ 1 ~ k H z } )$ ). This is achieved by virtue of a multiplicative avalanche effect in the transfer register which transforms the incident photoelectron into a charge packet. A gain of around 500 is possible, making this L3-CCD a promising detector, operating in photon counting mode. It looks like becoming a serious competitor for the avalanche photodiode.

# CCDs for X-Ray Detection

By thinning, the sensitivity of the CCD can be extended as far as X rays. The European mission XMM–Newton (1999–2010) is equipped with two cameras, each using 7 CCDs with format $6 0 0 \times 6 0 0$ . A third camera uses $1 2 \mathrm { C C D s }$ , laid side by side, each containing $6 4 \times 1 8 9$ pixels. The CCDs are used either in full-frame mode or in frame transfer mode, so as to minimise the readout noise and maximise the useful exposure time.6 Analogous setups are in preparation for the future German mission ROSITA (around 2010), with quantum efficiencies exceeding 0.8 for X rays in the range $0 . 2 { - } 2 0 \mathrm { k e V } .$

The pn-CCD differs from conventional CCDs by the structure of its transfer registers, here formed by p–n junctions in the silicon. This ensures low sensitivity to undesirable hard radiation like $\gamma$ rays or cosmic rays, but also fast charge transfer and high charge storage capacity.7

Finally, the CCDs used in the X-ray region have a certain spectral selectivity, i.e., an intrinsic energy resolution, of $\Delta E \sim 1 0 0 \mathrm { e V }$ for $E < 1 \mathrm { k e V } ,$ and $\Delta E \sim 1 4 0 \mathrm { e V }$ for $E \sim 6 \ \mathrm { k e V } .$  Indeed, a photon with energy in the $\mathbf { k e V }$  range releases a large number of photocharges, a number which then becomes a measure of the incident photon energy. To measure the energy of each photon, it is thus essential to read the CCD before another photon causes a release of photocharges at the same place. A summary of the CCD performances is given in Table 7.6.

# The CCD Controller

This electronic device is an essential element in the use of CCDs. It generates the clock signals and controls the charges and their transfer:

• It modifies the readout frequency (also called the pixel frequency), depending on whether the readout noise must be minimised (slow frequency) or not.   
• It modifies the gain, that is the number of electrons per level of digitisation, depending on the strength of the signal and the required dynamic range.   
It can read the CCDs in binning mode, in which adjacent pixels are summed according to a predefined geometry $2 \times 2$ , $4 \times 4$ , etc.). In this case, spatial  resolution is lost, but the signal-to-noise ratio is improved, since the signal is increased for the same level of readout noise. This mode, which reduces the volume of data collected and the readout time, is useful for making adjustments in order to take into account variable image quality in photometry, if a high spatial resolution is not required, and so on.   
• It also provides a windowing mode, in which a subset of pixels is selected within a window of the array.

As an example of the way CCD pixels are manipulated, let us consider a device proposed for the detection of an exoplanet which measures the tiny differential polarisation over time of the radiation recieved from the star–planet system when the planet orbits around the star. Indeed, the stellar radiation scattered by the atmosphere of the exoplanet is polarised, and depends on the phase angle. The polarisation of the incident signal is analysed very rapidly $( 1 \mathrm { k H z } )$ , then transformed into an intensity variation. The image is formed on a CCD in which every other column is masked. The masked columns are used to store the photocharges generated in the first column and transferred to the second at the fast rate of the modulation. After many cycles, the difference between the two columns indicates the presence of a possible polarisation. This is the so-called ZIMPOL technique, proposed by Schmid, H.M. et al., and described at the website saturn.ethz.ch/instrument/zimpol.

# 7.4.7 The Hybrid CMOS Detector

CMOS stands for complementary metal oxide semiconductor and refers to a whole family of 2D detectors, also fabricated by conventional techniques of microelectronics, but based on a different idea to the CCD. In this case, each pixel comes with its own readout and amplification transistors (3 or 4 in all). These transistors take up some space on the sensitive surface and this reduces the filling factor of the array, whence it may be necessary to use microlens arrays to improve photon gathering in the image. Furthermore, the CMOS technology is not amenable to rear illumination, which would avoid absorption of a fraction of the radiation by the surface layers. Instead of transferring the charges to registers as in a CCD, a clock device addresses the pixels of the array one by one to read the signal.

![](images/c488312a080ccb8763ce9db76ba2c96d87cc26db69849eb41324145afe256f94.jpg)  
Fig. 7.31 Growing formats of imaging detectors in the near and mid-infrared using CMOS technology. Ordinate: Number of pixels on the detector. The straight line shows a doubling every 18 months (known as Moore’s law). Figure established in 2004, courtesy of Hodapp K.W., Hall D.N., University of Hawaii

This technique was first developed for the near infrared, in order to make imaging detectors beyond the photoconductivity of silicon. It was subsequently extended to the mid- and far infrared in the middle of the 1990s. Based on the photovoltaic effect, these detectors couple a photodiode, made from a material that is photosensitive at the desired wavelength, with a readout circuit made from silicon, the whole thing being in a large format array. They are sometimes called hybrid arrays since they employ two different materials hybridised together. Since the 1980s, these arrays led to the rapid development of astronomical imaging in the infrared region (Fig. 7.31).

It is interesting to situate these advances with respect to the history of astronomical exploration in the infrared region, which developed slowly at first, then leapt forward, largely due to the quality of the available detectors, as can be seen from Fig. 7.32, for the period up to 2000.

The very low energies involved (a fraction of an electron-volt) make it necessary to cool the devices, in order to avoid the thermal generation of charges (dark current). The temperature ranges from $7 7 \mathrm { K }$ (liquid nitrogen), at the lower wavelengths $( \leq 2 . 5 ~ \mu \mathrm { m } )$ , and from 4 to $2 0 ~ \mathrm { K }$ , at the longer wavelengths, where the band gap is narrower (Fig. 7.33). The use of consumable cryogenic liquids, such as ${ \bf N } _ { 2 }$ and He, is gradually giving way, on Earth and in space alike, to closed circuit cryogenic systems (Joule–Thomson refrigerators).

![](images/736e715819a58fdc2bda22a663daa1a71f8761e3a0356ab03f589a4e4b7543cd.jpg)  
Fig. 7.32 Progress in infrared detection. The Edison tasimeter (Eddy A., J. Hist. Astr. 3, 187, 1972) was remarkably sensitive for its day $( \mathrm { N E P } \approx 1 0 ^ { - 8 } \mathrm { W } \mathrm { H z } ^ { - 1 / 2 } )$ . The thin continuous curve represents a mean sensitivity obtained with single pixel detectors. The dashed curve shows the arrival of array detectors (CID and CCD), and the formats are given. The readout noise $\sigma _ { R }$ is given by the thick continuous curve, with a brief indication of trends in performance levels beyond 2000 for different wavelength regions: $\bullet = 1 - 2 . 5 \mu \mathrm { m }$ , $\circ = 2 . 5 { - } 5 { \mu \mathrm { m } }$ , $\vartriangle { \ d t } = 5 \ – 2 0 \ \mu \ m$

![](images/f0e6c11c19a22f88f33d23b0c0aa5d447b3ebc53759902df9ebd1285701795cf.jpg)  
Fig. 7.33 Operating temperature of CMOS arrays at different wavelengths. Different regions are covered by silicon Si, then InGaAs, $\mathrm { H g C d T e }$ , InSb, and S:As. Courtesy of Hodapp K.W., Hall D.N., University of Hawaii

# Visible Region

CMOS technology competes with CCDs in this region, coupling a silicon diode with the pixel transistors, also fabricated in the same silicon substrate (see Table 7.7).

Table 7.7 Comparing CCDs and CMOS devices. From Hodapp K.W., Hall D.N.B, Institute of Astronomy, Hawaii, 2005   

<table><tr><td>Property</td><td>CCD</td><td>Hybrid CMOS</td></tr><tr><td>Resolution</td><td>&gt; 4k×4k</td><td>4k × 4k (under development)</td></tr><tr><td>Pixel (μm)</td><td>10-20</td><td>18-40 (&lt;10 under development)</td></tr><tr><td>Domaine spectral</td><td>400-1000 nm</td><td>400-1000 (Si PIN)</td></tr><tr><td>Noise</td><td>Several e-rms</td><td>Same with multiple sampling</td></tr><tr><td>Shutter</td><td>Manual</td><td>Electronic</td></tr><tr><td>Consumption</td><td>High</td><td>10 times lower</td></tr><tr><td>Sensitivity to radiation</td><td>Sensitive</td><td>Barely sensitive</td></tr><tr><td>Control electronics</td><td>High voltage clock</td><td>Low voltage</td></tr><tr><td>Special modes</td><td>Binning</td><td>Windowing</td></tr><tr><td></td><td>Adaptive optics</td><td>Random access</td></tr><tr><td></td><td></td><td>High dynamic range</td></tr></table>

The popular invention known as the webcam is equipped with detectors using this technology.

# Near and Mid-Infrared

The hybrid $\mathrm { H g C d T e }$ arrays originally commercialised under the trade name NIC-MOS, which stands for Near Infrared Camera and Multi-Object Spectrometer, were designed for the Hubble Space Telescope with a $1 0 2 4 \times 1 0 2 4$ format in the 1990s (Fig. 7.33). They are now called Hawaii detectors and have become more or less universal for the spectral bands J, H, and K, to be found on all the major groundbased and spaceborne telescopes (see Figs. 7.34 and 7.35).

The format and readout noise of these detectors have seen constant improvement and they now have excellent noise performance in the region $1 { - } 2 . 5 \mu \mathrm { m }$ , viz., $\sigma _ { \mathrm { R } } \approx 1 0 \mathrm { e } ^ { - }$ . At the time of writing (2006), formats of $6 1 4 4 \times 6 1 4 4$ have been achieved with $1 0 \mu \mathrm { m }$ pixels. They contain 248 million field effect transistors (FET). Thermal charge generation (dark current) is low, which means that, in the absence of background radiation, exposures of several tens of minutes are feasible. It can also be read quickly, in several tens of milliseconds, an invaluable asset in adaptive optics or optical interferometry, where rates are linked to the evolution times of atmospheric turbulence. The storage capacity of the potential wells is not very high (around $1 0 ^ { 5 }$ photocharges), and this limits use to long exposures with high incident fluxes or in the presence of a significant background signal (spectral bands J and H).

Hybrid InSb (indium antimonide) arrays, commercialised under the trade name Aladdin, pick up from there, up to the photoconductivity limit of thise material, in formats reaching $5 1 2 \times 4 0 9 6$ on one of the CRIRES focal instruments of the European Very Large Telescope.

Hybrid Si:As arrays, in a $2 5 6 \times 2 5 6$ format, then bridge the gap to the groundbased observation window of the $_ \mathrm { N }$ band around $\lambda = 1 0 \mu \mathrm { m }$ (the VISIR instrument Dof the VLT). They work in BIB mode described below. The IRAC camera of the Spitzer space mission launched in 2003 is also equipped with this detector, operating at $5 . 8 \mathrm { - } 8 \mu \mathrm { m }$ . The imaging photometer (MIP) of this mission comprises a $1 2 8 \times 1 2 8$ Si:As array, observing around $\lambda = 2 4 \mu \mathrm { m }$ . It also works on the blocked impurity Dband (BIB) principle discussed below.

![](images/5b769b3b15f64cdcf3a08d6664401dbe93cf3026aacc6162c02f62d316d70be5.jpg)  
Fig. 7.34 The Orion nebula observed in 2001 with the European Very Large Telescope and the ISAAC instrument. This image is put together using images taken in three different spectral bands (J, H, and K) and is in fact a $3 \times 3$ array of individual images, with the $1 0 2 4 \times 1 0 2 4$ format of the $\mathrm { H g C d T e }$ detector. Field $7 ^ { \prime } \times 7 ^ { \prime }$ , pixel $0 . 1 5 ^ { \prime \prime }$ . North is at the top and east on the left. Source ESO and M. McCaughrean

The same hybridisation scheme can be used with Si:Sb, for which photoconductivity extends up to $4 0 ~ { \mu \mathrm { m } }$ , in $2 5 6 \times 2 5 6$ formats, for use in space. The IRS spectrometer of this same mission is equipped with a $1 2 8 \times 1 2 8$ format camera.

# Blocked Impurity Band (BIB) Detectors

Two opposing requirements must be balanced when an extrinsic photoconductor is used in a detector: the level of dopant should be low in order to ensure a high resistivity, but it should be sufficient to maintain an adequate quantum efficiency when absorbing photons. The principle of the blocked impurity band (BIB) is to separate these two requirements spatially, in the material of the photoconductor, so that each can be optimised. An added benefit is an amplification effect, which improves noise performance.

![](images/de65d792f704b7aa998871d56ae94e3831f741a796fcbb315868f4f4d1c5dcce.jpg)  
Fig. 7.35 An image obtained with a NICMOS detector, on the $1 \textrm { m }$ telescope at the European Southern Observatory (La Silla, Chile). Field $1 2 ^ { \prime } \times 1 2 ^ { \prime }$ in the central region of Orion, showing molecular cloud and star formation region. The same region has been shown at radiofrequencies in Fig. 5.5. Wavelength and spectral band J $( 1 . 2 \mu \mathrm { m } )$ . Image format $7 8 0 \times 7 8 0$ , although the solidstate device includes only $2 5 6 \times 2 5 6$ pixels, the telescope being displaced by offsets of one third of a pixel and the image reconstructed by interpolation. Total exposure time $9 \times 1$ s. (Photo by Copet E., DENIS programme, 1995)

Consider the material Si:As, silicon doped with arsenic, with a band gap which situates the photoelectric effect in the region $\lambda \le 2 3 ~ \mu \mathrm { m }$ . The photosensitive layer (Fig. 7.36) is highly $n$ - doped, implying a good quantum efficiency, and also a small volume, which makes the detector less sensitive in an environment of high energy particles (e.g., in space, see Sect. 2.9.2). This layer is preceded by a thin blocking layer, made of a pure material, which ensures a high resistivity between the two electrodes. A photoelectron released in the sensitive layer drifts in the electric field, towards the blocking layer. A strong field can then transmit enough energy for the photoelectron to produce secondary electrons, by ionising collisions. This does not happen in the blocking layer, for the material there is too pure, and the ionisation energy is therefore high (around 1 eV). Amplification can reach a factor of ten. This is presented in detail by Rieke G.H., Detection of Light: from the Ultraviolet to the Submillimetric, 2nd edn., Cambridge 2003, and the discussion here follows closely.

![](images/9698803d631444e49fa7b5084ed2e2a7e2f88ae0c6f84e07aa1fe4cc93293ad1.jpg)  
Fig. 7.36 Schematic cross-section of a BIB detector. The electron is released in the photosensitive layer and drifts towards the blocking layer. The electrodes are on either side. Here, the BIB is illuminated from the front. (After Rieke G.H., 1994)

The amplification technique in the BIB detector is pushed a step further in the solidstate photomultiplier or SSPM. One difficulty with the BIB is that the amplification zone, situated at the interface of the blocking and photosensitive layers, is not very clearly defined. If this role is assigned specifically to a third layer, a significant cascade effect is obtained, in which a single electron may generate a current peak of 40 000 charges. Further, this current pulse is very brief, lasting only a few nanoseconds, if followed by high speed electronics. The detector then operates as a photon counter, and is able to discriminate events which are highly fluctuating in time. This constitutes, in the infrared domain, a property already mentioned for silicon avalanche diodes.

# Detection in the Far Infrared

The only photoconductor that can be used beyond $4 0 \mu \mathrm { m }$ is the material Ge:Ga, with a sensitivity region extendable to $2 1 0 \mu \mathrm { m }$ by applying pressure (stressed detector). However, the stressing device requires space and microelectronic techniques are no longer applicable, whence hybridisation is carried out pixel by pixel. This in turn reduces the available format sizes. These detectors equip the imaging photometer of the Spitzer mission (format $2 \times 2 0$ ), the PACS instrument of the European space mission Herschel (format $5 \times 5$ ), and the FIFI instrument of the airborne telescope SOFIA (format $2 5 \times 1 6$ ).

# Quasi-Optical Coupling

At wavelengths lying between the far infrared and millimetre, diffraction phenomena become significant, for the size of the detectors becomes comparable with the order of magnitude of the wavelength. In order to better concentrate the energy on the detector, guides are used in quasi-optical mode, which means that they operate somewhere between the classical image formation by a lens (see Chap. 5) and the standard waveguide (see Sect. 6.4). This is illustrated in Fig. 7.37, for detection in the range 100 to $2 4 0 \mu \mathrm { m }$ .

![](images/1d51f40c2b4ffbca99c83e4c3480e8c54ce052dcc04c5eb8c895c6110ed3d64b.jpg)  
Fig. 7.37 Quasi-optical arrangement of a detector array $( 5 \times 5 )$ , in gallium-doped germanium, operating at $\lambda < 2 4 0 \mu \mathrm { m }$ . (After Geis N., doctoral thesis, Max Planck Institut f¨ur Extraterrestrische Physik, 1991)

# 7.4.8 Observing Conditions in the Infrared

The radiation received at the detector includes the signal from the source and also the signal from the thermal background. The latter may be due to the optics of the telescope itself, if it is not cooled, or to the thermal background of the atmosphere. These two components can be reduced or even totally eliminated, when the detector is placed in space and equipped with cooled optics. Except in the latter case, the readout noise of the detector does not need to be reduced below the thermal noise generated by the background signal.

Two spectral regions thus stand out clearly, particularly for ground-based observations: wavelengths less than about $1 . 8 ~  { \mu \mathrm { m } }$ , where the background signal is negligible and the reduction of readout noise can be pushed to its limit. Beyond this point, the fluorescence of atmospheric OH radical enters the picture, as discussed in

Sect. 2.3, followed by a significant rise in the thermal background radiation. This region does not therefore require extreme performance with regard to the readout noise $\sigma _ { \mathrm { R } }$ .

In space, the absence of thermal background, and the very limited background due to a fully cooled telescope and optics, require the readout noise to be as low as possible.

An Instrument from the 1990s: The ISO Satellite. It is interesting to consider the progress achieved by describing the performance of the long wavelength observations $( 5 { - } 1 7 . 8 ~ \mu \mathrm { m } )$ of the ISO satellite, which was designed in the mid-1980s, launched in 1995, and exhausted its cryogenic fluid in 1998 (a joint project backed by the USA, GB, and ND). This camera (ISOCAM) was equipped with a $3 2 \times 3 2$ array made with Si:Ga hybridised on Si, and had a readout device that prefigured the CMOS system. (This was called direct voltage readout or DVR, which no longer transferred the charges, but read the amplified voltages on each pixel in sequence.) The readout noise $\sigma _ { \mathrm R }$ was approximately $1 8 0 \mathrm { e } ^ { - }$ rms, lower than the background noise, the integration time was at most $1 0 0 \mathrm { m s }$ before saturation by the residual thermal background, and the pixels had a storage capacity of $1 0 ^ { 6 }$ charges. This camera, which provided the first quality images in the near infrared with the $3 2 \times 3 2$ format (with two arrays, HgCdTe and Si:Ga), produced an extraordinary crop of new results.

The important development of the ISO satellite camera in France between 1985 and 1993 had many spinoffs. It is interesting to see how a single idea can be adapted to different contexts. At ground level, the thermal background is very much higher than that which prevails in space, for a cooled telescope. A solid-state device, based on the same principles, but with a storage capacity of $1 0 ^ { 7 }$ charges per pixel, was devised to equip the camera of a ground-based telescope (the TIMMI camera of the $3 . 5 \mathrm { ~ m ~ N T T }$ at the European Southern Observatory). It originally had a format of $1 2 8 \times 1 2 8$ but, after extension to a format of $2 5 6 \times 2 5 6$ and a change of dopant from Ga to As,  it equipped the Very Large Telescope (VLT), operating in the atmospheric transmission window between 8 and $1 2 \mu \mathrm { m }$ . It is interesting to compare the performance of the same detector at ground level (high background signal) and in space, with totally cooled optics (low background signal).

Even earlier, before the advent of detector arrays, NASA’s Infrared Astronomical Satellite (IRAS), which was the first to map the infrared sky, throughout the year 1983, carried individual detectors arranged side by side (Fig. 7.38).

# 7.4.9 Development of Solid-State Imaging Arrays

As in the case of many other astronomical detectors, many parameters are required to completely characterise these detectors. Three examples are listed here:

• The Maximum Storage Capacity of Photocharges per Pixel. This is an important quantity when faint sources are sought in the vicinity of some bright object. Saturation by the bright object determines the dynamic range of the detector. Furthermore, as already mentioned, the wells can be very quickly saturated, in a few milliseconds, by any thermal background radiation, so that it is pointless trying to extract the signal, after subtraction of this background. The solution is therefore to increase the capacity, which may reach a few times $1 0 ^ { 6 }$ or $1 0 ^ { 7 }$ photocharges per pixel. The Dependence of R on the Readout Rate. The faster the readout, the larger $\sigma _ { \mathrm { R } }$ becomes, and this may be harmful in rapid readout applications, such as optical interferometry, adaptive optics, and speckle interferometry, in which wavefront and image vary on the time-scale of atmospheric turbulence. The same is true for rapidly varying sources, such as pulsars and bursts.

![](images/ae9589b001327a5b755bd14d0ced968b53fc6b1c88a272db38abdf1e4a644a30.jpg)  
Fig. 7.38 A historic mission: the focal plane of the IRAS satellite $6 0 \mathrm { c m }$ telescope (1983). The individual detectors are arranged to obtain the maximum accuracy in locating a source as it crosses the focal plane. The visible sensors locate the field by detecting stars known in the visible, as they pass across. From Neugebauer G. et al., Ap. J. 278, L1, 1984. With the kind permission of the Astrophysical Journal

• The Format. The trend is towards larger formats. Although technology is unlikely to provide formats greater than $4 0 9 6 \times 4 0 9 6$ per unit of a detector array at affordable prices,8 the technique of juxtaposing solid-state imagers to form arrays can increase the useful format, and thus give a better use of the field at the telescope focus.

# Noise Equivalent Power

A photoconductor, operating at a temperature $T$ , has a non-zero resistance, even in the absence of illumination, because of the thermal release of charge carriers. The thermodynamic fluctuations in this resistance at temperature $T$ , called Johnson noise, are generally negligible compared with other noise sources.

Each incident photon produces $\eta$ electron–hole pairs, rather than $\eta$ electrons, as happens in the vacuum photoelectric effect, and so the quantum noise, due to the signal or the thermal background, has twice the variance.

The dominant source of noise from the detector itself is usually due to the transistor in the first stage of amplification. Denoting the detector response by $R \ [ \mathrm { V } \mathrm { W } ^ { - 1 } ]$ , and the noise of this transistor by $\sigma _ { \mathrm { R } } ~ [ \mathrm { V } \mathrm { H z } ^ { - 1 / 2 } ]$ , the noise equivalent power of the transistor, often used to characterise the detector (see Sect. 7.2.1), is given by

$$
{ \mathrm { N E P } } = \sigma _ { \mathrm { R } } / R \qquad { \mathrm { [ W H z ^ { - 1 / 2 } ] } } ~ .
$$

Typical values are $1 0 ^ { - 1 6 } – 1 0 ^ { - 1 7 } \mathrm { ~ W H z } ^ { - 1 / 2 }$ . Table 7.8 summarises some common properties of solid-state devices used in the near and mid-infrared.

# 7.4.10 Bolometers

In this type of detector, the energy of the incident photon is no longer used to excite the quantum jump of an electron into the conduction band. Instead, it is directly converted into thermal agitation, either of the crystal lattice, or of the free electron gas, if this is indeed decoupled from the lattice (the hot electron bolometer). These detectors therefore measure the temperature variation in either the crystal lattice or the electron gas, by a change in electrical resistance. They played a very important role in the development of infrared astronomy over the period 1960–1990, and then, considerably improved, continued to do so in the 2000s in the submillimetre region, where the fact that they have no intrinsic spectral selectivity gives them a significant advantage over heterodyne detection. With the use of microelectronic and multiplexing techniques, large format arrays can be made for both ground-based and spaceborne telescopes.

# Standard Germanium Bolometer

The germanium bolometer doped with gallium (Ga) is shown schematically in Fig. 7.39. The idea is to measure a slight change in resistance due to a rise in temperature of the material. Developed in the 1960s by F. Low,9 it covered the near and mid-infrared (infrared photometry or spectrophotometry) and led to many discoveries. A semiconductor crystal is used here, cooled to $2 { \mathrm { - } } 4 \mathrm { K }$ by liquid helium.

Table 7.8 Infrared solid-state devices   

<table><tr><td>Spectral range</td><td>Depends on material and dopant</td></tr><tr><td>Threshold</td><td>One quantum</td></tr><tr><td>Dynamic range</td><td>104-107 photocharges</td></tr><tr><td>Quantum efficiency</td><td>Generally &gt; 0.5</td></tr><tr><td>Temporal response</td><td>≤1ms</td></tr><tr><td>Integration time</td><td>About1O min if limited by thermal generation</td></tr><tr><td>Readout noise</td><td>About 1O ms if limited by thermal background</td></tr><tr><td>Storage</td><td>10-500 e- depending on device</td></tr><tr><td>Format</td><td>1024×1024→ 4096× 4096 (4k× 4k)</td></tr><tr><td>Operating temperature</td><td>77K(≤2.5 μm)→4K(longλ)</td></tr><tr><td>Special features</td><td>Addressable pixels</td></tr></table>

![](images/c38d7eaf5b858dbbc2dbe8b397849509aa37b1175f5e6aca597722771f8374c7.jpg)  
Fig. 7.39 The germanium bolometer (Ge:Ga). The resistivity of the semiconductor crystal varies rapidly with temperature $( \rho ~ \propto ~ T ^ { - 2 } )$ . A blackened shield efficiently $( \sim 1 0 0 \% )$ absorbs the / incident photons. The cross-section is improved by surrounding the crystal by a reflecting sphere. The crystal (of heat capacity $C$ ) is linked to the thermostat by wires (of heat conductance G). The time constant is $\tau \sim C / G$ . A bias $V _ { 0 }$ is applied across the resistor $R _ { \mathrm { { C } } }$ . The variation of the resistance $\Delta R _ { \mathrm { B } }$ of the bolometer, caused by the heating, is transformed into a signal $\Delta V = \Delta R _ { \mathrm { B } } / R _ { \mathrm { C } } + R _ { \mathrm { B } }$ . The solid angle within which radiation is received is controlled by a D Clow temperature screen

The bolometer can be considered to comprise two thermally coupled parts which are to be optimised separately. One is a radiation absorber, and the other a resistance serving as thermometer. The noise in this type of bolometer is thermal, and corresponds to its operating temperature $T$ (Johnson noise of the resistance and phonon noise leading to thermal energy). Noise equivalent powers from NEP $\sim$ $\mathrm { \overline { { 1 0 ^ { - 1 5 } } } ~ W } \mathrm { H z } ^ { - 1 / 2 }$ at $T = 2 \mathrm { ~ K ~ }$ to $1 0 ^ { - 1 6 }$ W $\mathrm { H z } ^ { - 1 / 2 }$ at $T = 0 . 3 \mathrm { ~ K ~ }$ are achieved with this type of device.

This conventional bolometer has witnessed considerable improvements.10 An example is the array equipping the European space mission Herschel (launch 2008) to cover the spectral region $6 0 { - } 2 1 0 ~ { \mu \mathrm { m } }$ . This array contains 2 560 silicon bolometers, arranged into $1 6 \times 1 6$ subsystems and operating at a temperature of $0 . 3 \ \mathrm { K }$ , obtained by a $^ 3 \mathrm { H e }$ dilution refrigerator. The NEP reaches $1 0 ^ { - 1 6 }$ W $\mathrm { H } z ^ { - 1 / 2 }$ , comparable with the noise induced by the thermal background in the observed beam etendue, whence there is no point in attempting further improvements. The signals, ´ produced by individual amplifiers, are multiplexed in order to reduce the number of connecting wires.

# Superconducting Bolometer

Here a superconducting material such as an Nb–Si alloy is held very close to the critical temperature at which the resistivity depends sensitively on the temperature. If energy in input by absorption of incident radiation, the resistance is altered. The resulting change in the current induces a magnetic field which is measured by a superconducting quantum interference device (SQUID). The operating temperature is close to $0 . 1 \mathrm { ~ K ~ }$ , obtained using a $^ 3 \mathrm { H e }$ refrigerator. These cooling systems can operate in closed circuit, and provide an elegant solution when long lifetimes are required for space missions, without depending on a cryogenic fluid which would eventually be used up. The NEP can be of the order of $1 0 ^ { - 1 7 } \mathrm { ~ W } \mathrm { H z } ^ { - 1 / 2 }$ , and improves as the temperature is lowered.

One difficulty lies in coupling the bolometer surface with the incident radiation. Indeed, it must be similar in size to the wavelength, while having a heat capacity, which determines the time constant of the bolometer, as low as possible. Finally, it is desirable to construct $N \times N$ bolometer arrays to obtain images efficiently.

The $1 0 . 4 \mathrm { ~ m ~ }$ telescope of the Caltech Submillimeter Observatory $( \mathrm { C S O } ) ^ { 1 1 }$ in Hawaii is equipped with a linear array of 24 thermal (Si) bolometers operating at a temperature of $0 . 3 \mathrm { K }$ obtained by a $^ 3 \mathrm { H e }$ dilution refrigerator. Atmospheric windows at 0.35, 0.45, and $0 . 8 7 \mathrm { m m }$ are accessible in broad band photometry $( \Delta \lambda / \lambda \sim 0 . 1 )$ . The CSO is also equipped with a hexagonal bolometer array $( 1 1 \times 1 1 )$ ) operating at 1.2 and $2 . 1 \mathrm { m m }$ (BOLOCAM).

The European space mission Planck, launched in 2008, is designed to study the cosmological blackbody radiation and its spatial structure. It seeks maximal sensitivity and imaging capacity at submillimetre wavelengths, using a $1 . 5 \mathrm { ~ m ~ }$ telescope cooled to $6 0 ~ \mathrm { ~ K ~ }$ . The High Frequency Instrument12 (HIFI) uses $4 \times 4$ and $8 \times 8$ bolometer arrays cooled to $0 . 1 \mathrm { ~ K ~ }$ to cover the range  100–857 GHz in six bands at low spectral resolution $( \sim 0 . 3 )$ . Cooling is carried out in several stages: hydrogen desorption, then Joule–Thomson expansion to reach $4 \mathrm { K }$ , then $^ 3 \mathrm { H e }$ dilution. The NEP can reach around $\mathrm { \dot { 1 } 0 ^ { - 1 7 } \ W H z ^ { - 1 / 2 } }$ .

In less than three decades, the spectacular progress made in bolometer design has made them invaluable submillimetre detectors, both on the ground and in space (see Fig. 7.40).

# Hot Electron Bolometer

In a very pure material like InSb $\sim 3 \times 1 0 ^ { 1 3 }$ carriers $/ \mathrm { c m } ^ { 3 }$ ) at low temperatures $( \sim 4 \ : \mathrm { K } )$  , a fraction of the conduction electrons remain free and interact weakly with the crystal lattice. Photon absorption by electrons raises their temperature and quickly modifies the resistivity of the material. This is photoconductivity by free carriers, exploited in the hot electron bolometer (HEB).13 However, the resistivity is proportional to the incident energy, hence also to the square of the electric field, whence the system functions as a mixer, and is frequently used as such in the radiofrequency range (see Sect. 7.5).

![](images/6c0cf9cdd4acc828a3ff6a854db19f2752463379f14f7210bda7819765a8ce61.jpg)  
Fig. 7.40 A particularly difficult measurement using a bolometer: the continuum emission of the $2 . 7 ~ \mathrm { K }$ cosmological background near its maximum. The $2 . 7 ~ \mathrm { K }$ and $2 . 9 \mathrm { ~ K ~ }$ Planck functions have been plotted with the following measurements: (a) using a $0 . 3 \mathrm { ~ K ~ }$ bolometer $\mathrm { ( N E P \sim }$ $1 0 ^ { - 1 5 } \mathrm { W } \mathrm { H z } ^ { - 1 / 2 }$ ), Woody and Richards measured the spectrum from a balloon at altitude $4 0 ~ \mathrm { k m }$ ; (b) the result of a similar measurement, made by Gush from a rocket between 150 and $3 7 0 ~ \mathrm { k m }$ altitudes. The shaded areas correspond to the error bars given by the authors. (After Weiss R., ARAA 18, 489, 1980. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, $\circledcirc$ 1980, Annual Review Inc.) These historical results have been considerably -improved by the COBE satellite, since 1990, then by the BOOMERANG and WMAP missions at the beginning of the 2000s

# X-Ray Bolometer

At the high energies characteristic of X rays $\mathrm { ( > 0 . 1 ~ k e V }$ ), the energy delivered is enough to produce a temperature pulse in the bolometer, indicating the arrival of individual photons. The amplitude of the pulse can be used to determine the energy. This is therefore a detector with an intrinsic spectral selectivity, invaluable for spectroscopic applications. Since the energy threshold and spectral resolution are proportional to the volume of the detector, small detectors are favoured. This is also advantageous in imaging, which requires small pixels. On the other hand, detection efficiency depends on the thickness of the detector.

A diamond crystal of several $\mathrm { m m } ^ { 3 }$ , cooled to below $0 . 1 ~ \mathrm { K }$ , is thermally coupled to a germanium component, whose conductivity varies sensitively with temperature (Fig. 7.41). If X-ray photon arrivals are separated by time intervals greater than the time constant of the bolometer, which is of millisecond order, individual events can be discriminated. An energy resolution of a few $\mathrm { e V }$ can be achieved with these detectors in the laboratory at the time of writing (2007).

![](images/2975e0464dba1e713cf4e430380d6701c6a5efcae351ddedd58e6086d1839f3d.jpg)  
Fig. 7.41 (a) Schematic view of a doped germanium bolometer. At the centre, the germanium resistance, stuck on the absorbing diamond disk. (b) Display of the time constant of the bolometer, after absorbing the energy of a photon (or any other absorbed particle). (c) Spectrum for emission of $\alpha$ particles by a radioactive material, with $T _ { \mathrm { b o l } } = 1 . 3 \ : \mathrm { K }$ . Data kindly provided by Coron N., 1985

# 7.5 Astronomical Detectors: Radiofrequencies

The principle of radiofrequency detection using non-linear elements as mixers, with a frequency change, then detection, was first developed at metre wavelengths, and then extended gradually down to centimetre, millimetre, and finally submillimetre wavelengths, at which point it joined up with quantum and thermal detection techniques (photoconductors and bolometers, respectively, which were discussed earlier). Frequency-changing techniques are sometimes successfully applied in infrared spectroscopy, using photoconductors as mixers (see Sect. 8.4).

In this section, we begin by discussing concepts which apply across the whole radiofrequency region, before examining some practical realisations and the performance of detection systems they use.

# 7.5.1 General Features

Here we discuss how to convert the incident electric field into current, either directly or by frequency change, then describe the noise characteristics affecting the signal produced by the measurement, taking into account the thermal nature of the received radiation, both from the source and from the environment of the telescope.

# The Conversion of Field into Current

The wave, focused at the focal point of a telescope, enters a horn, which matches the vacuum impedance to that of a waveguide. The latter selects a polarisation. The wave is guided into a resonant cavity, which defines a passband $\Delta \nu$ , through its selectivity $Q = \nu / \Delta \nu$ , close to the frequency $\nu$ of the radiation (Fig. 7.42).

# Received Power. Antenna Temperature

Consider first the simple case of a thermal source of radiation, of emissivity $\varepsilon _ { \nu }$ and temperature $T$ . The power reaching the non-linear element is given by

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \frac { 1 } { 2 } \varepsilon _ { \nu } B _ { \nu } ( T ) \eta _ { \nu } \mathcal { E } ,
$$

where $\mathcal { E } ^ { \mathcal { O } }$ is the beam etendue sampled, and the factor of´ $1 / 2$ comes from the selection of one polarisation. $\eta _ { \nu }$ denotes the total transmission, and $B _ { \nu } ( T )$ is the Planck function. It is assumed that the arrangement is as in Fig. 7.42a above.

It was shown, in Chap. 6, that the beam etendue ´ $\mathcal { E }$ is limited by the coherence of the radiation, and must be taken as equal to $\lambda ^ { 2 }$ . In other words, for a given telescope area $S$ , the field on the sky, which is imposed by coherence, is given by the solid angle $\omega = \lambda ^ { 2 } / S$ . Any radiofrequency receiver is intrinsically limited to analysis of Da single pixel, with field equal to $\omega$ . (In aperture synthesis, the receiver is limited to one ‘Fourier space pixel’, rather than one pixel in the image plane.)

The power per frequency interval is then

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \frac { 1 } { 2 } \varepsilon _ { \nu } \eta _ { \nu } \lambda ^ { 2 } B _ { \nu } ( T ) \ ,
$$

![](images/b9a1ea6fecb9b251d40001b122c7e5d740d7992c3d3f9143c77411505f03aa51.jpg)  
Fig. 7.42 Three receiver configurations for radio waves. In the first arrangement (a), a coil, normal to the magnetic field vector for example, is excited by induction and transforms the field into a current, which is transported by coaxial cable. A variation on this arrangement consists in directly exciting the non-linear element by the electric field. In the second arrangement $\mathbf { ( b ) }$ , an amplifier is placed on the waveguide axis and amplifies the wave before it excites the coil, or is detected. In the third arrangement (c), a local oscillator, of frequency $\nu _ { 0 }$ , superposes its field on that of the incident signal, by means of a coupler. The summed field is then applied to the non-linear element. An amplifier can be incorporated into this arrangement

and, in the case of blackbody radiation $\mathbf { \xi } _ { \mathcal { E } _ { \nu } } = 1 \mathbf { \xi } _ { \mathcal { E } }$ ), in the Rayleigh–Jeans approximation,

$$
\frac { \mathrm { d } P _ { \nu } } { \mathrm { d } \nu } = \eta _ { \nu } k T ~ .
$$

The received power is then simply given by a temperature, known as the antenna temperature, which is independent of the transmission of the system.

If the source is:

1. optically thick at the wavelength considered,   
2. at a temperature justifying use of the Rayleigh–Jeans approximation for the frequency considered $( h \nu \ll k T$ ),   
3. sufficiently extended to fill the field of lobe $\omega$ of the instrument,   
4. in local thermodynamic equilibrium,

then the antenna temperature $T _ { \mathrm { A } }$ is also the physical temperature of the radiation from the source. In the case of a non-thermal source, or one with an arbitrary intensity function, the power received at the telescope is clearly given by

$$
\mathrm { d } P _ { \nu } = k T _ { \mathrm { A } } ( \nu ) \mathrm { d } \nu ~ ,
$$

where $T _ { \mathrm { A } }$ is the antenna temperature measured at the frequency $\nu$

# Noise Temperature

In practice, even when an instrument is pointed towards a region containing no sources of radiation, and at zero temperature, a non-zero current is measured, whose power is also non-zero. There are several causes of this residual signal:

• Residual thermal emission from the atmosphere (see Sect. 2.3.2), the telescope, and the waveguide.   
Contribution from the thermal emission of the ground, detected in the sidelobes of the diffraction pattern.   
• Thermal noise generated in the detector itself (for example, fluctuations in the tunnelling current, in the AsGa diode).

The fields of these different sources are incoherent, and therefore add quadratically, so that the equation for the total noise power as the sum of the powers gives

$$
T _ { \mathrm { n o i s e } } = T _ { \mathrm { a t m o s p h e r e } } + T _ { \mathrm { l o b e s } } + T _ { \mathrm { d e t e c t o r } } ,
$$

even if the ‘temperatures’ do not correspond to actual physical temperatures. They merely represent the power from which the signal must be distinguished. The first two terms are highly dependent on wavelength, for the same is true of atmospheric emission and diffraction. They are usually around $1 0 0 \mathrm { K }$ for Earth-based telescopes, and around $1 0 \mathrm { K }$ for space telescopes. In the best of cases, the limit will be imposed by $T _ { \mathrm { d e t e c t o r } }$ , also known as the system temperature, which cannot be less than the physical temperature of the detector, and indeed, it is generally much higher than this value.

Consider now each of the configurations in Fig. 7.42a, b, and c, and their total noise temperatures, excluding contributions from the antenna and atmospheric emission:

$$
\begin{array} { r l } & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { q u a d r a t i c ~ d e t e c t o r } } \ . } \\ & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { a m p l i f i e r } } + T _ { \mathrm { m i x e r } } / \mathrm { g a i n } \ . } \\ & { T _ { \mathrm { n o i s e } } = T _ { \mathrm { R F ~ a m p l i f i e r } } + T _ { \mathrm { m i x e r } } / \mathrm { R F ~ a m p l i f i e r ~ g a i n } } \\ & { + T _ { \mathrm { I F ~ a m p l i f i e r } } + T _ { \mathrm { I F ~ m i x e r } } / \mathrm { I F ~ a m p l i f i e r ~ g a i n } \ . } \end{array}
$$

Case (c) has been written in the most general case of heterodyne detection.

The critical factor in each case is the mixer, whose noise temperature varies from a few tens to a few thousands of degrees kelvin (Fig. 7.43). The key features will be discussed below.

Note that the best receivers approach the quantum limit (Problem 7.9). At frequencies below $1 0 0 \mathrm { G H z }$ (centimetre or metre), the RF signal must be amplified, and this use of an amplifier reduces $T _ { \mathrm { n o i s e } }$ to between $5 0 \ \mathrm { K }$ (6 to $2 1 \ \mathrm { c m }$ ) and

![](images/517b1e1f50bf43bf9b1c5183e4bc8561c532614a6829920140fde558c1936929.jpg)  
Fig. 7.43 Noise temperature of mixers used in radioastronomy. $( + )$ Schottky diodes at $3 0 0 \mathrm { K }$ , $( \times )$ cooled Schottky diodes, $( \diamond )$ C  SIS junctions, ( ) hot electron bolometer (HEB). All these detectors have an intrinsically wide passband $\mathrm { ( > 1 0 0 M H z }$ ), except the bolometer. The straight line indicates the limit $h \nu = k T _ { \mathrm { n } }$ . (After Philips T.G., Woody D.P., ARAA 20, 285, 1982. Reproduced with the Dkind permission of the Annual Review of Astronomy and Astrophysics, Vol. 20, $\textcircled{9} 1 9 8 0$ , Annual Reviews Inc.) The initial values given in the figure $T _ { \mathrm { n } } \geq 1 0 0 \mathrm { K } )$ - are those of the mid-1980s. By the mid-1990s, little progress had been made in the region below $5 0 0 \mathrm { G H z }$ , the greatest being a factor of 2 for SIS junctions. By the mid-2000s (black symbols), SIS junctions are still being improved, e.g., $T _ { \mathfrak { n } }$ in the range $5 0 – 1 5 0 \mathrm { K }$ for the detectors of the $3 0 \mathrm { m }$ IRAM telescope or those of the HIFI instrument on board the European mission Herschel (launch 2008) beyond 1 THz, whereas the hot electron bolometer takes this mission beyond 1 THz, viz., $\lambda = 3 3 0 \mu \mathrm { m }$ . (Values for 2007 with the courtesy of G. Beaudin)

$3 0 0 ~ \mathrm { K }$ $( 1 . 3 ~ \mathrm { c m } )$ . These values are typical of receivers for the aperture synthesis radiotelescope known as the Very Large Array (VLA) in New Mexico.

By pointing the receiver alternately at the source and at a neighbouring point of the sky, assumed empty of sources, two values of the antenna temperature can be measured:

$$
T _ { \mathrm { s y s t e m } } + T _ { \mathrm { s o u r c e } } \quad \mathrm { a n d } \quad T _ { \mathrm { s y s t e m } } .
$$

On averaging, the difference of these gives the desired quantity, subject to fluctuations in each of the terms.

# Minimum Detectable Power and Signal-to-Noise Ratio

Figure 7.44 shows the simplest possible detection scheme. It can be used at metre wavelengths for low signal frequencies $\mathit { \Theta } ^ { ' } < 1 0 0 \ : \mathrm { M H z }$ ). Following the antenna, the

![](images/4564a1c89512a313185a40317c5856bf5a2c67ca291e132d76395cd0e6739862.jpg)  
Fig. 7.44 Simple detection scheme (referred to as video detection) for the field of an electromagnetic wave

cavity, behaving as a bandpass filter, isolates a frequency band $\Delta \nu _ { \mathrm { s } }$ in the signal, centered on a frequency $\nu _ { \mathrm { s } }$ .

It is assumed, to simplify the calculation, that the non-linear element has the effect of transforming the signal $x ( t )$ into the quantity

$$
y ( t ) = x ( t ) ^ { 2 } , \mathrm { c u r r e n t } i ( t ) \propto E ( t ) ^ { 2 } .
$$

In practice, the transformation may be slightly different, for example,

$$
y ( t ) = \left| x ( t ) \right| , \qquad \mathrm { c u r r e n t } i ( t ) \propto \left| E ( t ) \right| ,
$$

but the conclusions would be similar. It will suffice to consider the appropriate transformation of the random variable ${ \bf x } ( t )$ , which is assumed to be a Gaussian process, with white spectral density, characterised by a noise temperature $T ( \mathrm { n o i s e } ) = T _ { \mathrm { n } }$ . The current $i ( t )$ is then filtered by a filter (Fig. 7.45) of passband $( \varepsilon , \ f _ { \mathrm { c } } )$ D, which excludes zero. Finally, the signal is recorded in digital or analogue form.

The result giving the power spectrum of the square of a random process, which is described in Appendix B, can be applied, noting that $\Delta \nu _ { \mathrm { s } } \ll \nu _ { \mathrm { s } }$ (for example, in the case of a centimetre receiver, $\nu _ { \mathrm { s } } \sim 1 0 ^ { 1 0 } \ \mathrm { H z }$ , and $\Delta \nu _ { \mathrm { s } } \sim 1 0 ^ { 7 } ~ \mathrm { H z } )$ ). The PSD of the signal is then given by the convolution

$$
S _ { \mathrm { s } } ( \nu ) \simeq ( 2 k T _ { \mathrm { n } } ) ^ { 2 } \Delta \nu _ { \mathrm { s } } \left[ \delta \left( \nu - \frac { f _ { \mathrm { c } } } { 2 } \right) + \delta \left( \nu + \frac { f _ { \mathrm { c } } } { 2 } \right) \right] \star \varPi \left( \frac { \nu } { f _ { \mathrm { c } } } \right) ,
$$

for $f _ { \mathrm { c } } \ll \Delta \nu _ { \mathrm { s } }$ . Fourier transforming gives the autocovariance $C _ { \mathrm { s } } ( \tau )$ , and finally

$$
\begin{array} { r } { \sigma _ { \mathrm { s } } ^ { 2 } = C _ { \mathrm { s } } ( 0 ) = ( 2 k T _ { \mathrm { n } } ) ^ { 2 } 2 \Delta \nu _ { \mathrm { s } } f _ { \mathrm { c } } . } \end{array}
$$

The signal due to the source is obtained simply by putting $T _ { \mathrm { n } } = 0$ ,

$$
\mathrm {  ~ \ s i g n a l } = \langle \boldsymbol { s } ( t ) \rangle = \langle E _ { \mathrm { \mathrm { s o u r c e } } } ^ { 2 } ( t ) \rangle = \sigma _ { \mathrm { E } } ^ { 2 } = 2 k T _ { \mathrm { s o u r c e } } \Delta \nu _ { \mathrm { s } } ,
$$

and the signal-to-noise ratio is then

$$
\frac { 2 k T _ { \mathrm { s o u r c e } } \Delta \nu _ { \mathrm { s } } } { 2 k T _ { \mathrm { n } } ( 2 \Delta \nu _ { \mathrm { s } } f _ { \mathrm { c } } ) ^ { 1 / 2 } } = \frac { T _ { \mathrm { s o u r c e } } } { T _ { \mathrm { n } } } \left( \frac { \Delta \nu _ { \mathrm { s } } } { 2 f _ { \mathrm { c } } } \right) ^ { 1 / 2 } .
$$

![](images/e87f45445998fe7b098c1da04f5cf5f3bc31bad04ab35a58c893cd1a5e1a4575.jpg)  
Fig. 7.45 Spectral densities: (a) of the filtered incident signal at $\nu _ { \mathrm { s } }$ , (b) after quadratic detection, only the low frequency part being shown, (c) after low frequency filtering, on an expanded scale. The bandpass filter cuts out zero frequency, and hence the impulse at the origin. Since $f _ { \mathrm { c } } \ll \Delta \nu _ { \mathrm { s } }$ , the PSD is almost constant across the whole filter width

The bandpass $f _ { \mathrm { c } }$ of the filter is related to the integration time $\tau$ by an equation of the form

$$
f _ { \mathrm { c } } \tau = \alpha , \qquad \alpha \sim 1 .
$$

The exact value of the coefficient $\alpha$ depends on the transfer function of the filter used. The general rule stating that the signal-to-noise ratio only increases as the square root of the measurement time is once again satisfied. Moreover, this ratio only increases as the square root of the passband $\Delta \nu _ { \mathrm { s } }$ . Indeed, when $\Delta \nu _ { \mathrm { s } }$ increases, the signal increases, but then so does the noise power.

The unwanted contributions from atmospheric emission and instrumental noise can be eliminated by pointing the antenna at two neighbouring points of the sky, and taking the difference, so that the minimum detectable power is, for a signal-to-noise ratio equal to one,

$$
P _ { \mathrm { m i n } } = k T _ { \mathrm { n } } \left( \frac { 2 f _ { \mathrm { c } } } { \Delta \nu _ { \mathrm { s } } } \right) ^ { 1 / 2 } \Delta \nu _ { \mathrm { s } } \quad [ \mathrm { W } ] \ .
$$

In the model considered here, it was assumed that the same filter $\Delta \nu _ { \mathrm { s } }$ was applied to all components of $i ( t )$ , namely, the signal due to the source, the signal from instrumental emission, and the signal due to the fluctuations of the detector. If this were not the case, it would be a simple matter to modify the argument.

# 7.5.2 Heterodyne Detection

This is the method now most commonly used on radiotelescopes, both on the ground and in space, from the submillimetre to the metre wave region. It was presented briefly in Fig. 7.42c. Here we shall discuss the different components required, together with the underlying physical principles and the way they are implemented.

Figure 7.46 gives a more detailed overview of the successive operations to which the incident signal is subjected. Its frequency is first changed by superposition, without loss of information, at a quadratic detector, of the signal field at frequency $\nu _ { \mathrm { s } }$ , and the field of a local oscillator at frequency $\nu _ { 0 }$ . The current output by the mixer is then, up to proportionality,

$$
i ( t ) \propto E _ { 0 } ( t ) E _ { \mathrm { s } } ( t ) ~ .
$$

It therefore depends linearly on the field $E _ { \mathrm { s } } ( t )$ , and has a component at the frequency $( \nu _ { 0 } - \nu _ { \mathrm { { s } } } )$ . This current, which is called the intermediate frequency (IF) signal, is then amplified and filtered, before being detected again and averaged by the exit filter of width $f _ { \mathrm { c } }$ . The first advantage of this setup (Fig. 7.46) is the possibility of precisely controlling the filtering after the IF stage, which allows a spectral analysis of the signal. The second advantage is the amplification of the signal due to the mixing of the two frequencies. If the local oscillator produces a strictly coherent field, the current $i ( t )$ can be made large compared with all noise sources within the receiver, leaving only those fluctuations originating in the signal itself. This argument fails for wavelengths at which quantum noise in the local oscillator can no longer be neglected. In the end, the noise properties of the system as a whole are determined by those of the amplifier(s) and the mixer. The spectral properties are determined by the feasibility and stability of the local oscillator, the operating frequency and frequency bandwidth of the mixer, and then the properties of the spectral analysis stages to be described later (see Sect. 8.4).

The mixer does not in itself differentiate between two signal frequencies which are symmetrical about the frequency $\nu _ { 0 }$ of the local oscillator. This confusion can perturb the measurement (analysis of a spectral line), in which case a filter can be placed before the mixer to block frequencies $\nu \ < \ \nu _ { 0 }$ . This is referred to as single sideband reception or SSB reception, as opposed to double sideband reception or DSB reception. In the latter case, the signal-to-noise ratio is clearly reduced by a factor of $\sqrt { 2 }$ (Problem 7.8), but the spectral coverage is doubled.

The intermediate frequency stage, after the mixer, and the ensuing stages are independent of $\nu _ { \mathrm { s } }$ and $\nu _ { 0 }$ . They depend only on the difference $\nu _ { 0 } - \nu _ { \mathrm { { s } } }$ . The heterodyne setup is thus applicable at all wavelengths, provided that one has a suitable local oscillator, amplifier, and mixer for the chosen frequency, sensitivity, and spectral characteristics of the source under investigation.

# Local Oscillator

The role of this subsystem is to provide a coherent signal, hence with stable frequency, without noise, at a frequency $\nu _ { 0 }$ very close to the frequency $\nu _ { \mathrm { s } }$ of the signal. In addition, the power supplied must be large enough to ensure if possible that the signal after mixing exceeds the noise of the mixer. The three requirements made of a local oscillator are thus: matched frequency, sufficient power, and absence of noise.

![](images/11506bf460a24e5dd0956400ce40309fcd33f5faa7bf6830ec512ae2a0047500.jpg)  
Fig. 7.46 Successive stages of a single sideband (SSB) heterodyne receiver. (a) Subsystems. (b) The time dependent signal. (c) Spectral density of the signals. Note the image frequency $\nu _ { \mathrm { I } }$ eliminated by the filter $\Delta \nu$

![](images/85d0a9f168bb9d7c207e5da1c6fa24ed8df9d20c0dc933e931a8d47a81f08299.jpg)  
Fig. 7.47 Frequency regions covered by molecular lasers between 150 and $8 5 0 \mathrm { G H z }$ $( 0 . 3 5 { - } 2 \mathrm { m m } )$ ) (frequencies indicated by vertical arrows) and mixers whose bandwidth would be $\pm 5 \ : \mathrm { G H z }$ . The ˙shaded area shows frequencies that can be reached by using these lasers as local oscillators. (After Roeser H.P. et al., Astron. Astrophys. 165, 287, 1986)

Let us mention briefly two types of local oscillator which played an important role in the development of radioastronomy throughout the second half of the twentieth century.

The klystron is a wave generator that was used for $\nu _ { 0 } \lesssim 1 8 0 \mathrm { G H z }$ . Capable of supplying high power $( 2 5 { - } 1 0 0 ~ \mathrm { m W } )$ ), it was developed mainly for telecommunications and radar.

The carcinotron is a wave generator, working on the following principle. A beam of electrons, of the same kinetic energy, move parallel to a grill. Modulation of the grill potential creates a variable electric field, whose frequency is related to the grill spacing. This can emit a few tens of mW up to $1 0 0 0 \mathrm { G H z }$ , and is a high quality source, but cumbersome and power-consuming, and impossible to send into space, for example.

Harmonic generators are frequency doublers or multipliers, using a non-linear element, such as a Schottky diode, excited by a klystron. The non-linear element then radiates the harmonics 2, 3, . . . , of the excitation frequency. The power obtained can reach several mW, up to around $5 0 0 \mathrm { G H z }$

Molecular lasers offer great spectral purity and stability, together with a very large number of lines, covering not only the submillimetre, but also the far and middle infrared $2 0 ~  { \mu \mathrm { m } }$ and beyond). The available power is from 0.1 to $1 \mathrm { m W } .$ . The main drawback is that they provide only spectral lines at discrete frequencies, which may not be close to the frequency $\nu$ under study (see Fig. 7.47).

Modern oscillators (2007) are Gunn effect generators. A solid-state diode is designed so that its current–voltage characteristic in a certain region has negative resistance $( \mathrm { d } V / \mathrm { d } I < 0 )$ ). With direct current, the diode begins to oscillate and the desired frequency $\nu _ { 0 }$ is obtained by placing the diode in a resonant cavity at this frequency, from which it is extracted by a waveguide. These diodes are made with semiconducting materials like GaAs (from a few $\mathrm { G H z }$ to $1 0 0 \ \mathrm { G H z }$ ), then gallium nitride (up to THz). Once they had become the standard local sources, they greatly facilitated the development of submillimetre astronomy, e.g., on the California Submillimeter Observatory14 (CSO) in Hawaii, or the HIFI instrument on board the Herschel space mission.

Another possible configuration has a powerful amplifier after the diode, in fact a high electron mobility transistor (HEMT) described further below, then a frequency multiplier producing a harmonic at the desired frequency. Noise temperatures lower than $1 0 0 \mathrm { K }$ can be achieved at $3 0 0 \mathrm { G H z }$ , and lower than $1 0 0 0 \mathrm { K }$ at $7 0 0 \mathrm { G H z }$ .

Other methods for making oscillators are under development at the time of writing (2007), using Josephson junctions,15 laser beats, up to very high frequencies (THz), or beyond and up to the mid-infrared, the quantum cascade laser (QCL).

In conclusion, we have presented a rather general radiofrequency detection setup, and we have shown that, in practice, a wide range of configurations is possible on this basis (see Table 7.9).

# Amplifiers

In most radiofrequency detection systems, the non-linear element is a significant source of noise. It is useful, therefore, to amplify the signal of frequency $\nu _ { \mathrm { s } }$ , or the IF signal $\nu _ { \mathrm { I F } } = \nu _ { 0 } - \nu _ { \mathrm { s } }$ , before detection.

D The principle of the various types of amplifiers is as follows. Energy is extracted from a local radiation source and transferred to the incident wave, in proportion with the incident energy, and in phase with the incident field. A coherent amplification effect is obtained, and the signal-to-noise ratio is improved as long as the amplifier gain remains less than

$$
g = { \frac { T _ { \mathrm { n } } } { T _ { \mathrm { a } } } } \ ,
$$

where $T _ { \mathrm { a } }$ is the noise temperature at the amplifier input, and $T _ { \mathfrak { n } }$ the noise temperature of the detection element.

Table 7.9 Radiofrequency reception. RF radiofrequency, IF intermediate frequency   

<table><tr><td>Component parts</td><td>RF amplifier Local oscillator</td></tr><tr><td></td><td>Non-linear RF element IF amplifier, filter(s),and correlator</td></tr><tr><td></td><td>IF detector (transistor)</td></tr><tr><td>Geometrical properties</td><td>Single pixel, fixed étendue λ² Small arrays (N≤10)</td></tr><tr><td>Polarisation</td><td>One polarisation detected</td></tr><tr><td>Spectral properties</td><td></td></tr><tr><td></td><td>Intrinsically wideband components</td></tr><tr><td></td><td>Post-IF spectral selectivity</td></tr><tr><td>Noise</td><td>Close to the thermodynamic limit</td></tr><tr><td></td><td></td></tr><tr><td></td><td>imposed by the system temperature</td></tr><tr><td></td><td></td></tr><tr><td>Temporal response</td><td>No particular limit</td></tr></table>

The modern method of amplification, which can be applied either directly to the incident RF signal or to the intermediate frequency (IF) signal, uses so-called high electron mobility transistors (HEMT). These are field-effect transistors based on a heterojunction, i.e., two semiconducing materials with different bandgaps. For example, the ODIN space mission (Sweden, Canada, Finland, and France), launched in 2001 and still running in 2007, includes a $1 . 1 \mathrm { m }$ radiotelescope and focal systems operating between 180 and $5 2 0 \mathrm { G H z }$ , with IF amplifiers based on this idea.

Here we briefly mention some of the systems developed over the period 1950–2000.

The parametric amplifier exploits the following idea. Consider an oscillator represented, for example, by a circuit with a resistor $R$ , an inductance $L$ , and a capacitance $C$ , in which one of the elements determining the resonant frequency, e.g., $C$ , can be varied. Let $\omega _ { 0 }$ be the original frequency, and $2 \omega _ { 0 }$ the frequency of modulation of $C$ . Assuming low damping, that is

$$
Q = \frac { 1 } { \omega _ { 0 } R C } \gg 1 ,
$$

the oscillator equation is

$$
\ddot { x } + \frac { 1 } { \tau } \dot { x } + \omega _ { 0 } ^ { 2 } ( 1 - \varepsilon \sin 2 \omega _ { 0 } t ) x = 0 ,
$$

with

$$
C = C _ { 0 } ( 1 - \varepsilon \sin 2 \omega _ { 0 } t ) , \quad \varepsilon \ll 1 , \quad L C _ { 0 } \omega _ { 0 } ^ { 2 } = 1 , \quad \tau = \frac { L } { R } .
$$

Seeking a solution of the form

$$
x = f ( t ) \sin \omega _ { 0 } t \ ,
$$

it follows that

$$
f ( t ) = K \exp \left( \frac { \varepsilon \omega _ { 0 } } { 2 } - \frac { 1 } { 2 \tau } t - \frac { \varepsilon } { 4 } \sin { 2 \omega _ { 0 } t } \right) \sim K \exp \left( \frac { \varepsilon \omega _ { 0 } } { 2 } - \frac { 1 } { 2 \tau } \right) .
$$

Amplification occurs if the two conditions

$$
\varepsilon > \frac { 1 } { \omega _ { 0 } \tau } \quad \mathrm { a n d } \quad \varepsilon \ll 2 + \frac { 1 } { \omega _ { 0 } \tau }
$$

are simultaneously satisfied. This is indeed possible, when the selectivity $Q$ is much greater than unity, as we assumed.

The system is only linear in a restricted amplitude range. An appreciable gain can be obtained. Power is transferred to the signal by modulation of the capacitance $C$ . It therefore comes from the oscillator which modulates this capacitance at the frequency $2 \omega _ { 0 }$ . In practice, the variable capacitance, sometimes called a Varactor, is a Schottky junction barrier (see below), whosecapacitance depends on the applied voltage by the relation

$$
C = C _ { 0 } \left( 1 - \frac { V } { V _ { 0 } } \right) ^ { - n } ,
$$

where $0 . 3 \lesssim n \lesssim 0 . 5$ . The typical noise temperature of a cooled parametric amplifier is 10 to $2 0 \mathrm { K }$ .

The idea of the maser amplifier is to use an external power source to populate the excited levels of a solid or gas beyond the population which would correspond to thermodynamic equilibrium. The stimulated emission produced by the incident radiation is in phase with that radiation, and in the same direction, so that amplification occurs.

![](images/d1a9921683dbecc18a51fb5a9e545e7ac0413093f6ef1e44527b7e1de987ecd7.jpg)  
Fig. 7.48 Energy states in a ruby maser, as a function of the applied magnetic field

A ruby maser is a crystal of alumina $\mathbf { A l } _ { 2 } \mathbf { O } _ { 3 }$ , in which $0 . 0 5 \%$ of the $\mathrm { A l } ^ { 3 + }$ ions are replaced by chromium ions ${ \mathrm { C r } } ^ { 3 + }$ . The combined effect of the $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ lattice electric field and an external magnetic field creates four energy levels (Fig. 7.48) for the electron spin $S = 3 / 2$ of the ${ \mathrm { C r } } ^ { 3 + }$ ion.

DMagnetic dipole transitions are possible between these levels. The maser can be pumped by a local oscillator (Fig. 7.48) at the frequency $( E _ { 4 } - E _ { 2 } ) / h$ , and it will then emit the energy $( E _ { 4 } - E _ { 3 } )$ (stimulated emission). The crystal must be cooled so that the differences of population are significant:

$$
{ \frac { E _ { 3 } - E _ { 1 } } { h } } \quad ( { \mathrm { a t ~ } } B = 0 ) = 1 1 . 4 6 { \mathrm { ~ G H z } }
$$

corresponds to a temperature

$$
T = \frac { E _ { 3 } - E _ { 1 } } { k } = 0 . 5 5 \mathrm { K } .
$$

The typical noise temperature of a maser amplifier lies between 15 and $5 0 ~ \mathrm { K }$ .

The Rydberg maser uses states close to the ionisation continuum of the hydrogen atom. The energy difference between two of these states is given by

$$
\Delta E = R \left[ \frac { 1 } { n ^ { 2 } } - \frac { 1 } { ( n + 1 ) ^ { 2 } } \right] \sim R n ^ { - 3 } ,
$$

for $n \gg 1$ . For $n \sim 3 0$ , the energy difference corresponds to millimetre wavelengths. Electrical  dipole transitions between these levels are easy to excite, and the amplification principle is as before.

# Mixers

We said above that there were two key factors in the design of a mixer, i.e., the spectral bandwidth $B$ it accepts and the noise temperature that characterises it. All things being equal, the desired value of $B$ increases with the frequency $\nu _ { \mathrm { s } }$ of the incident signal. This observation means that simpler mixing techniques are possible at frequencies below $8 0 \ : \mathrm { G H z }$ $\lambda \gtrsim 4 ~ \mathrm { m m }$ ). Today, HEMT transistors can be used, operating at ever higher frequencies and able to amplify then detect IF signals, while maintaining a sufficiently broad spectral bandwidth $B$ .

At higher frequencies, viz., millimetre and submillimetre, the predominant mixer is the SIS superconducting junction and the hot electron mixer (HEB). The Schottky diode is still used, but performs less well with regard to noise.

![](images/0d3a4f4c8112b506e643f77025c9d69a90d0d9dd7b72e5db22fb096653b865db.jpg)  
Fig. 7.49 Electron microscope image of a SIS junction made at the Paris Observatory (LERMA) for the frequency band 385–500 GHz of the European telescope ALMA in Chile. Document courtesy of LERMA

SIS Junction

The underlying principle of the superconductor–insulator–superconductor (SIS) junction has already been mentioned in Sect. 7.3. The circulation of a quasiparticle current in the insulator is a non-linear effect, as can be seen from the current–voltage characteristic of the junction shown in Fig. 7.17. It can thus be used as a frequency mixer.16 Since the interaction between the radiation and the material occurs by quanta, the theoretical noise temperature limit is very low, viz., $T _ { 0 } ~ = ~ h \nu / k$ . At $1 0 0 ~ \mathrm { G H z }$ , we have $T _ { 0 } ~ = ~ 5 ~ \mathrm { K }$ , whereas the best diodes reach $T _ { \mathrm { n } } ~ \approx ~ 2 0 ~ \mathrm { K }$ , and at $1 \ \mathrm { T H z }$ , $T _ { \mathrm { n } } ~ \approx ~ 1 0 0 0 ~ \mathrm { K }$ . This favourable factor means that a low power local oscillator can be used, and it can even be integrated into the diode. However, the intrinsic capacitance of the geometry (see Fig. 7.49) does not authorise a use exceeding the THz range.

The high frequency behaviour depends on the product of the resistance and the capacitance of the junction. At the time of writing (2007), Nb(niobium)– $\mathrm { A l O } _ { 2 }$ (alumina)–PbBi junctions are used up to $1 . 2 \mathrm { T H z }$ $\lambda = 0 . 3 5 \mathrm { m m }$ ).

DSIS junctions are small and can thus be arranged in small format 2D arrays to make multipixel image detectors at radiofrequencies. For example, the $3 0 \mathrm { m }$ IRAM telescope is equipped with a $3 \times 3$ array, fed by juxtaposed horns (which reduces the filling factor), and the James Clerk Maxwell Telescope (JCMT) in Hawaii has a $4 \times 4$ array, operating at $\lambda = 8 0 0 \mu \mathrm { m }$ .

Hot Electron Mixer

We have already seen how the free electron gas in a very pure InSb semiconductor is heated by incident radiation, modifying its resistivity when this energy is transferred to the crystal lattice, and thereby constituting a hot electron bolometer (HEB). However, this change in resistivity, proportional to the incident energy, is thus proportional to the square of the electric field incident on the material, whence it can function as a mixer.

In this case, a nanoscale superconducting bridge made from niobium nitride (NbN) and connecting two gold electrodes17 The signal (source and local oscillator) is focused on this bridge by a lens or quasi-optical waveguide. Heterodyne mixing results from the purely resistive transition between the superconducting and normal states, induced when the RF signal heats the material. A broad IF bandwidth (up to $B = 2$ GHz) is obtained by reducing the volume of the NbN film to give the lowest Dpossible thermal time constant. A noise temperature of $T _ { \mathrm { n } } = 7 5 0 ~ \mathrm { K }$ is obtained at $1 . 5 \mathrm { T H z }$ , rising to $3 0 0 0 \mathrm { K }$ at $3 \ \mathrm { T H z }$ Din double sideband (DSB) mode.

Schottky Diode

This non-linear component, also called a Schottky barrier, 18 was long considered the ideal radiofrequency mixer. It has gradually been superseded by detectors coming closer to the quantum noise limit, such as those we have just described. However, it remains widely used when the signal is strong enough not to be significantly degraded by the mixer noise. This is the case, for example, when a millimetre wave instrument is used to observe the Earth atmosphere from space, or the surface of Mars from a probe in orbit around the planet. The signal, similar to a blackbody at around $2 5 0 \mathrm { K }$ , is then strong enough.

The aim here is to outline the effects of contact between a metal and a semiconductor. Figure 7.50 illustrates the phenomena resulting from such a contact. In equilibrium, the majority charge carriers in the semiconductor move away from the contact area, in such a way that the Fermi levels in the metal coincide with those in the semiconductor. A barrier, or depletion zone, emptied of majority charge carriers, appears in the semiconductor. A simple calculation shows that the width of this barrier is given by the expression

$$
x _ { \mathrm { b } } = \left( \frac { 2 \varepsilon | V _ { 0 } | } { N e } \right) ^ { 1 / 2 } ,
$$

where $\varepsilon$ is the permittivity of the material, $V _ { 0 }$ is the difference between Fermi levels, and $N$ is the carrier number density. For $\varepsilon = 1 6 \varepsilon _ { 0 }$ , $V _ { 0 } = 0 . 5 \ V$ , $N = 1 0 ^ { 1 6 } \mathrm { c m } ^ { - 3 }$ , this gives ${ x _ { \mathrm { b } } = 0 . 3 \ \mu \mathrm { m } }$ .

D D D DThe current–voltage characteristic of the junction or diode is shown in Fig. 7.51. In the absence of any applied voltage, a current may nevertheless cross the junction, either because the thermal energy of the electrons is large enough to allow them to cross the potential barrier, or because, having insufficient energy, they still manage to cross it by tunnelling. At low temperatures $\begin{array} { r } { T \ll 3 0 0 \mathrm { K } , } \end{array}$ , this latter effect dominates, and the characteristic can be written

![](images/a7282319d3702371ff6e837305356db441465c89790b2e8d50b2aeefdcffa16b.jpg)  
Fig. 7.50 Contact between a metal and an $n$ -type semiconductor. The dashed line represents the Fermi level in each material. The ordinate is the electrostatic potential

![](images/77c8f4cfba1836aa6f4e6da410472aeb5cb1ec17093e8d7dcbd0dfa149b9f8db.jpg)  
Fig. 7.51 Current–voltage behaviour of a metal/n-type semiconductor. A positive voltage increases the potential barrier, and the current is decreased

$$
I \sim I _ { \mathrm { s } } \exp \left( \frac { e V } { E _ { \infty } } \right) ,
$$

where $I _ { \mathrm { s } }$ is the saturation current, and $E _ { \infty } \propto x _ { \mathrm { b } } ^ { - 1 } \propto N ^ { 1 / 2 }$ .

If $\Delta f$ / /is the frequency passband of the filter which follows the diode, the current $i$ will produce a fluctuation (see Sect. 7.2)

$$
\langle \Delta i ^ { 2 } \rangle = 2 e i \Delta f \ ,
$$

and the corresponding noise power is (Problem 7.2)

$$
P = { \frac { R \langle \Delta i ^ { 2 } \rangle } { 4 } } = { \frac { \mathrm { d } V } { \mathrm { d } I } } { \frac { 2 e i \Delta f } { 4 } } .
$$

This power can be characterised by a noise temperature, using the power spectrum of thermal noise (see Sect. 7.2). It follows that

$$
P = k T _ { \mathrm { d } } \Delta f = { \frac { 1 } { 2 } } { \frac { \mathrm { d } V } { \mathrm { d } I } } e i \Delta f ,
$$

implying

$$
T _ { \mathrm { d } } = \frac { E _ { \infty } } { 2 k } .
$$

The noise temperature $T _ { \mathrm { d } }$ characterises the intrinsic quality of the diode.

In practice, the semiconductor used is highly doped gallium arsenide (AsGa). A thin layer of lower dopant concentration is formed on the surface by molecular epitaxy, and this surface is then put into contact with the metal.

Epitaxy is the name for the process which consists in growing a thin layer of different composition on the surface of a monocrystalline structure, in such a way that the layer has the same crystal structure as the substrate. This process is commonly used in microelectronics, for example, to deposit doped silicon onto pure silicon. The layer is deposited by condensation of a vapour, or crystallisation of a liquid.

The drive to reduce noise requires low operating temperatures $( \lesssim 2 0 ~ \mathrm { K } )$ , and low dopant levels in the epitaxial layer, in order to reduce tunnelling. Moreover, the thickness of this layer must not exceed that of the depletion zone, for this would introduce extra resistance.

There is a high frequency limit to the response of these diodes. Beyond $3 0 0 \mathrm { G H z }$ $\lambda < 1 \mathrm { m m } )$ ), the intrinsic capacitance of the diode creates a resistance–capacitance filter which reduces the response. Certain processes have been devised to reduce this capacitance to $1 . 5 \times 1 0 ^ { - 1 5 } \mathrm { F } ,$ thereby extending the domain of operation up to $7 0 0 \mathrm { G H z }$ .

# Wide Band Receiver

Heterodyne detection has intrinsic spectral selectivity by spectral analysis of the IF signal (see Chap. 8). However, the total received power, limited only by the passband $B$ of the mixer, can be measured directly at the mixer output, hence with very low spectral selectivity. An example is shown in Fig. 7.52.

# 7.5.3 The Diversity of Radioastronomy

Radiofrequency detection covers a vast spectral region which today links up with the infrared via the submillimetre region. Needless to say, this involves a wide range of different technologies for the components used in observing systems. Table 7.9 sums up the basic properties of detectors, on the basis of which many different observational combinations are possible.

![](images/29aa462ae90f85752a2a1d9dcd1ba9c573f55fe412a3839fb7a6e6c69f8f9cfe.jpg)  
Fig. 7.52 Wide band receiver. A measurement of the power radiated by the planet Venus at $\lambda = 6 ~ \mathrm { c m }$ , with the $4 2 . 6 \mathrm { ~ m ~ }$ radiotelescope at Kitt Peak (Arizona). The planet is alternated with Dthe sky background in its neighbourhood (E, W, N, S). CAL denotes a calibration (Sect. 3.5.1). The selected polarisation is in the N–S direction. The size $\theta$ of the planet is small compared with the field of coherence, and the deviation is proportional to $\textstyle \int _ { \Delta \nu } B _ { \nu } ( T _ { \mathrm { v e n u s } } ) \pi \theta ^ { 2 } \mathrm { d } \nu / 4$

As in other wavelength regions, the observing system couples an Earth-based or spaceborne telescope, sometimes part of an array (see Sect. 6.5.1), with these receivers, associated with a spectroscopic capacity to be examined in detail in Chap. 8. These different components are arranged and combined as dictated by the desired observation and the given astrophysical problem. By visiting the websites of radioastronomy observatories, the reader will be able to confirm the extreme diversity and wealth of possible combinations, put together in each case to optimise the observation. Here are some examples:

• Detection of a very faint extragalactic radio source, using a large collecting area, a spectral band $\Delta \nu _ { \mathrm { s } }$ as wide as possible, and an integration time as long as possible. Analysis of the very rapid variations of a pulsar, in order to determine the period, the spectral band again being wide, but the integration time short (less than one millisecond). Analysis of solar flares, in which the rapid variations of the emission depend on the frequency, and high spectral selectivity and temporal response must be achieved, whilst maintaining the signal-to-noise ratio. Analysis of the spectral line profile of an interstellar molecule, which requires very high spectral resolution $( \nu _ { \mathrm { s } } / \Delta \nu _ { \mathrm { s } } \sim 1 0 ^ { 5 } )$ , using the kind of spectrometer described in more detail in Sect. 8.4. Measurement of the angular size and imaging of a radiosource. This requires the use of an interferometer array, with comparison of the phase of a wave at two spatially separated receivers, in order to obtain information about the size of the source. The spectral resolution is not necessarily high, unless the emission is spectrally narrow, e.g., an emission line.

Figure 7.53 shows schematically the various configurations that can be associated with such problems. A fourth dimension could be added, to show the frequency of the received signal.

# 7.6 Observing Systems for Gamma-Ray Astronomy

In this high energy region, which we shall define as having a lower limit of the order of $1 0 \ \mathrm { k e V }$ $( \lambda \sim 0 . 1 \ \mathrm { n m } )$ ), continuing on from the X-ray region, the notions of telescope, detector, and spectrometer considered up to now to be independent entities tend to merge into a single system which fulfills all these functions. This is mainly because, in contrast to other wavelengths, there are no mirrors available that could form images from incident $\gamma$ radiation. The lower limit, clearly fixed in the years 1970–2000 at around $1 0 \mathrm { k e V }$ by the limits to the possible use of mirrors, is tending to move toward ever higher energies, and will no doubt exceed a few hundred keV in the near future, while the $\mathrm { X }$ -ray region moves up to higher energies by means of its own techniques. This illustrates the somewhat arbitrary but merely practical nature of the way the electromagnetic spectrum has been divided up for the purposes of this book. At the very highest energies, the $\gamma$ ray region continues to move upwards, and now extends beyond $1 0 \mathrm { T e V } .$ .

![](images/eeee4b94cf89fbf038915b43adf137e6ba4f6f8a386526310c53480ca337894c.jpg)  
Fig. 7.53 The diversity of observing combinations in radioastronomy. Domains of application are only given up to an order of magnitude. A fourth dimension is needed to represent frequency, but each subject identified is treated successively over the whole frequency range from $1 \ \mathrm { T H z }$ to at least $1 0 0 \mathrm { M H z }$

In Chap. 5, we presented certain features of image formation at $\gamma$ ray wavelengths which tended rather to resemble those of conventional telescopes. Here we bring together the notions which for other wavelength regions have been distributed throughout the first part of this chapter on detectors and Chap. 8 on spectrometers. In addition, we shall retain the term telescope, which is commonly used to refer to the whole system receiving, detecting, and analysing the $\gamma$ radiation energy from astronomical sources. Such systems began to appear naturally enough at the beginning of the 1960s, in particle or nuclear physics laboratories which have their own traditions of instrumentation. In particular, since the 1990s, a field known as astroparticle physics has come into being, bringing together the problems of high energy astrophysics, where the relevant mechanisms involve the nuclei of atoms rather than their electronic shells. Instrumentation for observing astronomical sources emitting at such energies has also been developing at a considerable rate.

It should be said, however, that, despite immense progress accomplished since the 1970s in the $\gamma$ ray region, angular resolutions remain less good than in other spectral regions at the time of writing (2007), and most sources must still be considered as unresolved by today’s instruments. But considerable progress has been made in levels of sensitivity for the detection of faint sources, spectral resolution, and the very high energy frontier. We shall thus discuss the question of spatial resolution, then spectral resolution, both being closely related to the type of detector used. Tables 7.10 and 7.11 give an overview. Each of these devices is then used in a specific instrument, generally carried in space, although occasionally exploiting the Earth atmosphere as detector.

Table 7.10 Detection in ” ray astronomy   

<table><tr><td>Interaction</td><td>Type of detector</td><td>Energy range</td><td>Imaging</td></tr><tr><td rowspan="3">Photoelectric absorption</td><td>CdTe crystal</td><td>10 keV-1MeV</td><td>Coded mask and segmented imager (104 pixels)</td></tr><tr><td>Scintillators</td><td>100keV-10MeV</td><td>Coded mask and segmented imager (10³ pixels)</td></tr><tr><td>Ge crystal</td><td>10keV-10MeV</td><td>Coded mask and segmented imager (10 pixels)</td></tr><tr><td>Compton scattering</td><td>Scintillators or CdTe+ CsI Si+ Ge Si + CdTe</td><td>100keV-10MeV</td><td>Intrinsic and/or coded mask</td></tr><tr><td>Pair effect</td><td>Spark chamber then Si trackers</td><td>20MeV-300GeV</td><td>Intrinsic</td></tr><tr><td>Pair effect (air shower formation and Cherenkov radiation)</td><td>Photomultiplier tubes</td><td>100 GeV-100TeV</td><td>Intrinsic</td></tr></table>

Table 7.11 Main instruments for ” ray astronomy   

<table><tr><td>Mission</td><td>Date</td><td>Energy range</td><td>Instrument</td><td>Separating power</td><td>Spectral resolution E/△E</td></tr><tr><td>HEAO-1</td><td>1977-1979</td><td>80keV-2MeV</td><td>A4-MED</td><td>17°</td><td>4</td></tr><tr><td>HEAO-3</td><td>1979-1981</td><td>50keV-10MeV</td><td>HRGRS</td><td>30°</td><td>500</td></tr><tr><td>COS-B</td><td>1975-1982</td><td>50MeV-10 GeV</td><td></td><td>0°</td><td>2</td></tr><tr><td>GRANAT</td><td>1989-1998</td><td>30keV-1MeV</td><td>SIGMA</td><td>20&#x27;</td><td>5-10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20keV-10MeV</td><td>BATSE</td><td>5°</td><td>10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20keV-10MeV</td><td>OSSE</td><td>3.8°×11.4°</td><td>10</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>1-30 MeV</td><td>Comptel</td><td>2-4°</td><td>10-20</td></tr><tr><td>CGRO</td><td>1991-2000</td><td>20MeV-30 GeV</td><td>EGRET</td><td>1-50</td><td>5</td></tr><tr><td>INTEGRAL</td><td>2002-</td><td>15keV-1MeV</td><td>IBIS/ISGRI</td><td>12&#x27;</td><td>3-30</td></tr><tr><td>INTEGRAL</td><td>2002-</td><td>15keV-8MeV</td><td>SPI</td><td>2.6°</td><td>50-500</td></tr><tr><td>AGILE</td><td>2007-</td><td>10MeV-10 GeV</td><td>LAT</td><td>0.1-3°</td><td>10</td></tr><tr><td>GLAST</td><td>2008-</td><td>10 MeV-100 GeV</td><td>LAT</td><td>0.1-3°</td><td>10</td></tr><tr><td>Telescope</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Whipple</td><td>1989-2000</td><td>500GeV-5TeV</td><td></td><td>0.5°</td><td>5</td></tr><tr><td>HEGRA</td><td>1993-2002</td><td>500 GeV-10 TeV</td><td></td><td>20&#x27;</td><td>5</td></tr><tr><td>CAT</td><td>1996-2002</td><td>200 GeV-10 TeV</td><td>1</td><td>20&#x27;</td><td>5</td></tr><tr><td>HESS</td><td>2003-</td><td>100 GeV-100TeV</td><td></td><td>10&#x27;</td><td>7</td></tr><tr><td>MAGIC</td><td>2004-</td><td>50GeV-50TeV</td><td>1</td><td>18&#x27;</td><td>7</td></tr></table>

# 7.6.1 Spatial Resolution of Gamma-Ray Sources

Here we discuss several types of $\gamma$ ray telescopes, in the sense of generalised system using different physical processes to determine the direction of the incident radiation.

# Compton Telescope

In the energy region extending from several hundred keV to several MeV, the interactions of $\gamma$ rays with matter are dominated by Compton scattering1 (see Sect. 7.3.1). An acceptable measurement of the incident photon energy can only generally be made in this region by instigating a series of interactions which end in a photoelectric absorption, and such a succession of interactions can only be guaranteed by a detector of a certain thickness. This kind of detector, bombarded by radiation belt protons (see Sect. 2.9.2) and cosmic rays, suffers from a great deal of noise. If it is split into two separate parts and only those events simultaneously triggering the two parts are retained, almost all background events are eliminated, because these events generally only trigger one of the two detectors. On the other hand, a large proportion of events undergoing Compton scattering is conserved. Consequently, a significant background reduction is obtained, usually by more than an order of magnitude, and this can procure a considerable gain in terms of signalto-noise ratio if the system is designed to favour the Compton scattering of photons along the telescope axis. The nature and size of the first part of the detector must be chosen so as to maximise the probability of single Compton scattering (low atomic number $Z$ of the material). In contrast, the second detector must maximise absorption (high $Z$ , high mass), in order to ensure total absorption of energy.

Equipped with a collimator, such a Compton telescope can give an image of the whole celestial sphere by scanning. This is analogous to the technique used in the HEAO1-A4 experiment (1977– 1979), but operating at higher energies. If the detectors are position sensitive, such scanning is not necessary, but one is faced with a classic dilemma: a large aperture results in high sensitivity but poor angular resolution, while a small aperture guarantees good angular resolution at the expense of the sensitivity. As we saw in Sect. 5.2.5, the coded mask provides a solution to this problem and can be profitably applied here. The idea is then analogous to the Sigma experiment: imaging would be of comparable quality, being linked to coded mask techniques, but at higher energies (greater than $1 \mathrm { M e V } _ { \cdot }$ ).

Still considering the case of position sensitive detectors, it is also possible to use the ballistics of the Compton interaction to restrict the direction at which the photons arrive (scattering angle) and deduce the position of the source statistically. In this case, imaging performance depends on the spectral resolution of the two detectors and the distance between them. However, efficiency decreases rapidly with this distance and a compromise must be found between sensitivity and angular resolution. This latter method is used in the COMPTEL experiment aboard the Compton

Gamma-Ray Observatory (GRO) which flew from 1991 to 2000. The distance of about $1 . 2 ~ \mathrm { m }$ between the two detectors leads to a separating power of around 5 degrees. It is also possible in the case of very closely positioned detectors to use both a coded mask for imaging and also Compton ballistics for a further background reduction. One then selects only those events for which all calculated incident directions lie within the solid angle subtended by the mask at the point of first interaction. This method is used by the IBIS instrument carried on board the INTEGRAL mission (launched in 2002).

The spectral performance of this type of telescope with regard to sensitivity and imaging are governed by the energy resolution of the weakest of the two detectors.

# Pair Effect Telescope

Beyond energies of a few MeV, the pair effect dominates the interactions between photons and matter (see Sect. 7.3.1). The photons are detected in two stages: first conversion, i.e., pair creation, then measurement of the electron and positron trajectories, from which the direction of the incident $\gamma$ ray can be deduced.

Indeed, in the center of mass system, the electron and positron are emitted in opposite directions, while in the laboratory system, they are emitted in the direction of the photon, modified by the recoil motion of the nucleus responsible for the electric field in which electron–positron production occurred. Up to this recoil, the directions of the electron and positron are related to the direction of the incident photon.

Pair creation becomes more efficient in stronger electric fields. In matter, it occurs in the electric fields of atomic nuclei, and the strength of these fields depends on the number of protons in the nucleus. This is why materials with high atomic number (high $Z$ ) provide the most efficient conversion (see Fig. 7.20), and lead is usually used for this purpose. On the other hand, good conversion efficiency also requires a thick converter, and the electrons will tend to scatter more (Moliere scattering) \` as the atomic number of the converter material and thickness of the converter are increased. This means that electrons leaving a thick converter are likely to have lost all memory of the direction of the incident $\gamma$ ray.

This difficulty has given rise to the basic design of the pair effect telescope. In order to limit electron scattering, thin plates of lead are used, inserted between devices able to measure the electron trajectories. Good conversion efficiency is guaranteed by using many plates, while the fact that they are thin ensures an accurate measurement of electron and positron trajectories (Fig. 7.54). The latter are measured using techniques developed for particle accelerators, such as spark chambers up until the mid-2000s in missions like SAS-2, COS-B, Compton/EGRET (Energetic Gamma Ray Telescope), and silicon strip trackers in the future, e.g., in the Gamma ray Large Area Space Telescope (GLAST) mission (launch 2008).

The angular resolution of such a telescope thus depends on the photon energies, since the error resulting from electron scattering increases as the energy decreases, being a few degrees at $5 0 \mathrm { M e V } ,$ , and only a few tens of arcmin in the GeV range and beyond. The photon energies, generally measured using a calorimeter absorbing the pair, can also be estimated from the observed scattering of the electron and positron. The event rate is high, but events due to celestial $\gamma$ rays are rather rare, and observation times and data processing are thus very long (of the order of a month). The production of $\mathrm { e ^ { + } e ^ { - } }$ pairs is an unambiguous signature of $\gamma$ rays with energies greater than a few MeV. This signature provides an efficient way of rejecting the background, whence pair effect telescopes can claim relatively good sensitivity: $\approx$ $1 0 ^ { - 7 } \mathrm { c m } ^ { - 2 } \mathrm { s } ^ { - 1 }$ in one month of observation by EGRET.

![](images/2e841e2c5273a8b5faea1cfbdedf9c0bdccf0628140589e7fef4a989f1ecd7b6.jpg)  
Fig. 7.54 Telescopes for $\gamma$ -ray observation. Top right: The telescope carried by COS-B, one of the first $\gamma$ -ray observation satellites (1975–1982). The plates of the spark chamber can be seen, and also the scintillators (shaded) placed around the main detector as anticoincidence devices, which are designed to detect and eliminate the background signal due to charged particles. The scintillators $B _ { 1 }$ , $C$ and $B _ { 2 }$ trigger the chamber, and the calorimeter $E$ measures the energy of the particles. PMT stands for photomultiplier tube. Top left: View of an event (pair formation) in the spark chamber. From Paul J., 1979, private communication. See also Bignami et al., Sp. Sci. Instrum. 1, 245, 1975. With the kind permission of D. Reidel Publishing Company. Bottom: Schematic diagram of the Fermi Large Area Telescope (LAT). The telescope has dimensions $1 . 8 ~ \mathrm { m } \times 1 . 8 ~ \mathrm { m } \times 0 . 7 2 ~ \mathrm { m }$ . The required power and the mass are $6 5 0 \mathrm { W }$ and $2 7 8 9 \mathrm { k g }$  , respectively. From Atwood W.B. et al., Ap. J. 697, 1071, 2009

# Spark Chambers

In a spark chamber, $\gamma$ rays interact by pair effect in plates made from a high $Z$ material. Alternatively, charged sheets of wires are inserted between the plates. A created electron and positron ionise a gas (neon) and a spark is produced in the gas between the electrodes formed by the sheets of wires. The trajectories of the particles are thus materialised (Fig. 7.54) and recorded either photographically or using a vidicon tube (see Sect. 7.4).

# Silicon Strip Tracking Systems

Once again, converter plates are used for pair creation, but the gas and wires are replaced by grids of silicon detectors (Fig. 7.54). The electron or positron ionises the silicon encountered along their trajectories. The resulting electrons and holes migrate under the effect of the electric field toward the electrodes and induce a current pulse at the terminals of these electrodes. The track followed by the pair can be reconstructed by analysing the coincidence signals in the tracker ensemble.

# Atmospheric Cherenkov Telescope

A 1 TeV photon entering the Earth atmosphere interacts with it at an altitude of around 10 kilometres, producing an electron–positron pair. The electron quickly generates high energy $\gamma$ rays by inverse Compton scattering, while the positron annihilates to emit a further two high energy $\gamma$ rays. These $\gamma$ rays will in turn create $\mathrm { e ^ { + } e ^ { - } }$ pairs and the process repeats, generating an air shower. The electrons in the shower are relativistic, moving a speed $\nu$ close to the speed of light in vacuum, and in fact faster than the speed of light in the atmosphere $( c / n$ , where $n$ is the refractive index of the atmosphere). The result is a very brief flash of blue Cherenkov emission,20 lasting only a few nanoseconds, emitted along a cone with axis close to the direction of the $\gamma$ ray which originated the shower and with greater apex angle $\theta$ for higher values of the speed $\nu$ of the electrons. In fact, co $\mathfrak { s } \theta = c / \nu n$ . At an altitude of around $1 0 0 0 \mathrm { m }$ D, an electromagnetic shower contains only Cherenkov photons and extends over about a kilometre.

![](images/441487c00be8d7845310352e3d78a66d8f712e0742f4d4837d2f043005d68c5e.jpg)  
Fig. 7.55 Two of the four light collectors forming the HESS instrument in the Namibian desert. Photo courtesy of the HESS collaboration and CEA/DAPNIA

There are two techniques for measuring Cherenkov air showers. In the more popular imaging technique — used, for example, in the High Energy Stereoscopic System (HESS), set up in Namibia in $2 0 0 4 ^ { 2 1 }$ (see Fig. 7.55) — each Cherenkov cone, reflected by a parabolic mirror, forms an ellipse in the focal plane of the mirror. The dispersion in the directions and speeds of the electrons produces ellipses with different centers and different sizes, forming a relatively uniform quasi-elliptical spot. This feature is used to distinguish electromagnetic showers from hadronic showers, which produce much less regular spots. The orientation of the ellipse is related to the direction of the initial $\gamma$ ray. By measuring the angular distribution of the Cherenkov light, $9 9 \%$ of the cosmic ray protons can be rejected, and at the same time angular resolutions of a tenth of a degree can be achieved. The detection threshold with this technique is of the order of a few hundred GeV.

The second, so-called sampling technique consists in measuring as accurately as possible the shape of the blue light wavefront by means of fine spatial sampling and accurate time measurements. This wavefront is almost spherical for an electromagnetic shower and more spread out for a hadronic shower. This technique, which requires an array of optical reflectors with large collecting area, has been developed by reusing former solar energy production units. This is exemplified by the CELESTE experiment, set up since 2000 at the Themis power generating site in´ the French Pyren´ ees. At the present time, sampling s´ ystems are less sensitive than imagers, but have an energy detection threshold ten times lower.

Whatever technique is used, the brevity and colour of the Cherenkov emission necessitates photomultiplier tubes as detecting element (see Sect. 7.4.3).