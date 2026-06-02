# Chapter 8 Spectral Analysis

Spectroscopy is at the heart of astrophysics, and indeed, it is usually spectroscopic observations and their interpretation which provide the strongest constraints on the models proposed by astrophysicists. There are a great many examples: energy balance, abundance of molecules, atoms, ions, or other particles, macroscopic or microscopic velocity fields, local physical conditions such as the temperature, the density, the magnetic or electric fields, states of equilibrium or of deviation from equipartition of energy, and so on.

Whether the subject of study is planetary or stellar atmospheres, hot and dilute interstellar media or cool and dense molecular clouds, the intergalactic medium, accretion or thermonuclear processes occurring near the surface of very compact objects, energy generation processes in galactic nuclei, the expansion of the Universe, or the cosmic background radiation, spectroscopy is almost always the main diagnostic tool.

For this reason, the development of spectrometers, using the available photons to maximum advantage, is a constant priority. The combined efforts of astrophysicists and physicists, who are equally interested in this area, have brought spectrographic instrumentation close to perfection, in the sense that it attains or exceeds the limits of resolution imposed by the physical conditions in which the radiation is produced. The main advances today stem from better coupling between spectrometers and detectors, so that spectrometry can now benefit from any progress made in detector development.

The aim of this chapter is therefore to discuss the fairly classical techniques of spectroscopy proper. It begins with a brief survey of the use of spectra in astrophysics, extending the study of radiation in Chap. 3, and introducing the vocabulary and general ideas basic to all spectroscopy. This is followed by some general comments about spectrometers. Then we describe the spectrometry based on interferometric techniques, which plays a fundamental role, right across from the X-ray to the far-infrared region. Its application to the design of astronomical spectrometers is discussed. Radiofrequency spectrometry falls into a category of its own and is treated separately. Gamma-Ray spectrometry (energies above $1 0 \mathrm { \ k e V } ,$ , together with certain X-ray spectrometers (bolometers), use intrinsic energy discrimination by detectors, and this subject is therefore dealt with in Chap. 7 which examines detectors.

# 8.1 Astrophysical Spectra

The radiation received from a source is characterised by its specific intensity $I ( \nu , \pmb \theta )$ , at frequency $\nu$ , and in the direction of observation $\pmb \theta$ . The polarisation of the radiation can also be specified (linear, circular, elliptical, etc., see Sect. 3.1). The spectrum of the source is given by the $\nu$ dependence of $I ( \nu , \pmb \theta )$ . Strictly speaking, the term spectrum, which is used here and is common usage, refers to the spectral density of the electromagnetic field, regarded as time dependent variable, and more often than not, a random time variable.

# 8.1.1 Formation of Spectra

The elementary interaction between radiation and matter (atomic nuclei, atoms, molecules, solid particles, etc.) results in an energy exchange. When the system makes a transition from one state to another, with energies $E _ { 1 }$ and $E _ { 2 }$ , and the probability of photon emission or absorption varies greatly with frequency $\nu$ in the neighbourhood of the transition frequency,

$$
\nu _ { 0 } = \frac { E _ { 2 } - E _ { 1 } } { h } ,
$$

where $h$ is Planck’s constant, the microscopic conditions for the formation of a spectral line are satisfied. This line may be an emission line or an absorption line, depending on the direction of the energy exchange, and the fundamental probabilities are given in detail by nuclear, atomic, molecular, or solid state physics, depending on the nature of the system.

The radiation $I ( \nu )$ received by an observer is the result of a macroscopic summation over a large number of elementary interactions situated either inside the source itself, or, especially in the case of a more distant object, along the whole length of the line of sight. These radiation–matter interactions cause emission, absorption, and elastic or inelastic scattering, depending on the various media encountered, their physical state (solid, gaseous, plasma, etc.), their physical parameters (temperature, pressure, velocity field, etc.), and the local fields (magnetic, gravitational, etc.). The spectrum finally observed thus results from a complex process of radiative transfer. The general transfer equation can be written

$$
I ( \nu ) = \int _ { 0 } ^ { \infty } S ( \nu , x ) \mathrm { e } ^ { - \tau ( \nu , x ) } \mathrm { d } x ,
$$

where $S ( \nu , x )$ is the source function, which characterises the elementary emission at the point $x$ , measured along the line of sight, $\nu$ is the frequency, and $\tau$ is the optical depth between 0 and $x$ ,

$$
\tau ( \nu , x ) = \int _ { 0 } ^ { x } \kappa ( \nu , \xi ) \mathrm { d } \xi ,
$$

with $\kappa ( \nu , \xi )$ the local absorption coefficient for the radiation. Inversion of the transfer equation,1 establishing the local source function $S ( \nu , x )$ at the object, is a fundamental problem in astrophysics, leading as it does from the measured spectrum $I ( \nu )$ to the local conditions which created $S$ .

The great diversity of observed spectra is a consequence of the complexity of radiative transfer processes, in media such as stars, interstellar gases, and molecular clouds, which are themselves diverse.

The spectrum is said to be continuous if the observed function $I ( \nu )$ varies slowly with $\nu$ . The blackbody sky background radiation, the continuous radiation of the Sun, or synchrotron radiation emitted by active galactic nuclei, are all good examples of continuous spectra, in which radiative transfer has attenuated or smoothed away the emissions of discrete transitions on the microscopic scale.

The spectrum is referred to as a line spectrum if it exhibits emission or absorption lines, which means that $I ( \nu )$ varies rapidly over some narrow frequency interval $\Delta \nu \ll \nu $ (Fig. 8.1). The absorption spectrum of a star of advanced spectral type, and hence cold, or the submillimetre emission spectrum of a molecular cloud, are typical examples of line spectra.

# The Main Transitions and Corresponding Frequencies

The quantification of matter systems assigns energy levels $E _ { i }$ , and hence associates spectral transitions with those systems. Depending on its complexity, a semiclassical or quantum mechanical treatment is required to evaluate the probability of a transition between energy levels, or the cross-section of an interaction with radiation. The main transitions which concern astronomical spectroscopy are reviewed in this section, and summarised in Table 8.1. When the radiative transfer is sufficiently simple, the spectrum $I ( \nu )$ received from a source is dominated, at least in a restricted spectral region, by a local source function expressing specific spectral transitions.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/2d9f3de26cfcb85a9ec36e95196681167244776c937a33a7c9c8f521473359cc.jpg)  
Fig. 8.1 Terminology for spectral lines. (a) Arbitrary spectrum. (b) Full width at half maximum of an emission line. (c) Equivalent width of a line. (d) Relative intensity of an absorption line

Electronic Transitions

In the case of the hydrogen atom, or any hydrogen-like atom, the frequencies $\nu _ { 0 }$ radiated when the atom changes energy state are given by the Rydberg formula

$$
\nu _ { 0 } = 2 c R Z ^ { 2 } \frac { m - n } { n ^ { 3 } } ,
$$

where $n$ and $m$ are the principal quantum numbers characterising the two energy states, $R = 1 0 9 7 3 7 . 3 1 \mathrm { c m } ^ { - 1 }$ is the Rydberg constant, and $Z$ is the effective charge Das seen by the electron. This simple expression will now be used to specify some systems undergoing transition, and the energy ranges they involve.

• The Hydrogen Atom. The transitions with n $\iota , m \ : < \ : 5$ , whose energies $h \nu$ lie between 10 and $0 . 1 \ \mathrm { e V }$ for $Z = 1$ , are radiated in the near UV, the visible and Dthe near infrared. These energies correspond to temperatures $T = h \nu / k$ between $1 0 ^ { 5 }$ and $1 0 ^ { 3 } ~ \mathrm { K }$ D, and are therefore characteristic of the outer layers of stars (stellar atmospheres), or ionised hydrogen regions in interstellar space. The spectra of these objects are thus dominated by such transitions. For example, the Lyman $\alpha$ line $\lambda = 1 2 1 . 6 \mathrm { n m }$ of hydrogen appears in the spectra of hot stars, and the Balmer $\alpha$ Dline $( \lambda = 6 5 6 . 3 \mathrm { ~ n m } )$ ) appears in the spectra of ionised nebulas (H II Dregions), and so on.

Table 8.1 Examples of discrete transitions   

<table><tr><td>Transition</td><td>Energy [eV]</td><td>Spectral Region</td><td>Example</td></tr><tr><td>Hyperfine structure</td><td>10-5</td><td>Radiofrequencies</td><td>21 cm hydrogen line</td></tr><tr><td>Spin-orbit coupling</td><td>10-5</td><td>Radiofrequencies</td><td>1667 MHz transitions of OH molecule</td></tr><tr><td>Molecular rotation</td><td>10-²-10-4</td><td>Millimetre and infrared</td><td>1-0 transition of CO molecule at 2.6 mm</td></tr><tr><td>Molecular rotation-vibration</td><td>1-10-1</td><td>Infrared</td><td>Hz lines near 2 μm</td></tr><tr><td>Atomic fine structure</td><td>1-10-3</td><td>Infrared</td><td>Ne II line at 12.8 μm</td></tr><tr><td>Electronic transitions of atoms,molecules and ions</td><td>10-²-10</td><td>Ultraviolet,visible, infrared</td><td>Lyman,Balmer series,etc., of H, resonance lines of CI, HeI,and K,L shell electron</td></tr><tr><td>Nuclear transitions</td><td>&gt;104</td><td>X and γ rays</td><td>lines (Fe XV, O VI) 12C line at 15.11 keV</td></tr><tr><td>Annihilations</td><td>≥104</td><td>yrays</td><td>Positronium line at 511 keV</td></tr></table>

Hydrogen-like Atoms. The Rydberg formula shows that spectra are shifted towards the near or extreme ultraviolet as $Z$ increases, which raises the related energies and temperatures accordingly. It is worth recalling here the special notation used by astrophysicists: a neutral atom carries the label I, e.g., C I, H I, while a once-ionised atom carries the label II, e.g., H II $( \mathrm { H ^ { + } } )$ , Fe II, and so on. This group includes the important lines of helium (the $1 s ^ { 2 } – 1 s 2 p$ transition of He at $\lambda = 5 8 . 4 \ : \mathrm { n m }$ ), of carbon (the $2 p 3 s { - } 2 p 3 p$ transition of the neutral atom, or C I, at $\lambda = 1 0 6 9 . 1 \mathrm { { n m } }$ ), and many others. Ions such as He II, C II, $\mathrm { F e } ^ { n + }$ , etc., also Dundergo this type of transition, the effective charge $Z$ increasing with the degree of ionisation. Their spectral lines are characteristic of hotter regions, including accretion disks in binary systems, the solar corona, and eruptions at the surfaces of stars.

• Molecules. The frequencies of electronic transitions in molecules consisting of several atoms like $\mathrm { H } _ { 2 }$ , CO, and $\mathrm { N H } _ { 3 }$ , radicals like OH and CN, or molecular ions like $\mathrm { H } _ { 2 } \mathrm { O } ^ { + }$ , are given by a more complicated expression than the Rydberg formula, but nevertheless fall into the same energy range, from the near ultraviolet $( 1 0 \mathrm { e V } )$ to the near infrared $\mathrm { ( 0 . 1 ~ e V ) }$ . The principal sites generating such spectra would be the atmospheres $T \approx 3 0 0 0 ~ \mathrm { K } )$ ) and circumstellar envelopes $\mathit { T } \ = \ 1 0 0 0$ to $3 0 0 0 ~ \mathrm { K }$ ) of cold stars, rich in molecules and radicals that are Dstable at low temperatures, and also dense interstellar regions, excited by shock waves.

• Deep Atomic Shells. Transitions involving low electron shells, and hence high effective charges $Z$ , close to the total charge of the nucleus ( $Z = 1 0$ to 100), lead to energies as high as $1 0 \mathrm { k e V } ,$ given the $Z ^ { 2 }$ dependence of $\nu _ { 0 }$ D. Such radiation therefore occurs in the EUV and $\mathrm { X }$ -ray regions, and the associated temperature can reach $1 0 ^ { 8 } ~ \mathrm { K }$ . One of the advantages in observing this radiation is that it is indifferent to any relationship the atom may have with other atoms, for example, whether or not it belongs to a molecule or a solid, and it is also irrelevant whether the atom is neutral or ionised. X-ray radiation is observed in the solar corona, accretion phenomena (close binaries, quasars), and thermonuclear outbursts on stellar surfaces (cataclysmic variable stars).

• Rydberg States. This term refers to high quantum number $( n )$ states of the hydrogen atom or hydrogen-like atoms. Transitions between such states have energies of the order of $1 0 ^ { - 5 } ~ \mathrm { e V } ,$ and are observed at radiofrequencies, for sufficiently dilute media in which the temperature pushes the atoms close to ionisation.

Electronic Fine Structure Transitions

The electron levels have a fine structure springing from the coupling between orbital angular momentum and electron spin. The extra levels produced have characteristic energy differences between $1 0 ^ { - 2 }$ and $1 0 ^ { - 5 } ~ \mathrm { e V } .$ The principal lines $n  m$ are !split into several components, hence the term ‘fine structure’, and there are also transitions between the new sublevels, which are observable in the far infrared or at radiofrequencies. The relative populations of energetically close sublevels are virtually independent of temperature, but highly sensitive to density, and this is the great importance of these lines. Examples are the carbon C I lines at 609 and $3 7 0 \mu \mathrm { m }$ (submillimetre region), C II lines at $1 5 8 ~ { \mu \mathrm { m } }$ , and the oxygen O I lines at 63 and $1 4 5 \mu \mathrm { m }$ , all of which are important in the study of the galactic interstellar medium.

Electronic Hyperfine Structure Transitions

The coupling of electron spin and nuclear spin also leads to the appearance of sub- levels, the transitions here having energies between $1 0 ^ { - 6 }$ and $1 0 ^ { - 5 } \ \mathrm { e V } ,$ which radiate at centimetre radiofrequencies. The best known example is the splitting of the ground state $( n = 1$ ) of hydrogen into two sublevels, separated by $5 . 9 \times 1 0 ^ { - 6 } \mathrm { e V } .$ . D These sublevels are populated even in the cold phase of the interstellar medium, and lead to the important emission line at $2 1 \ \mathrm { c m }$ , corresponding to the radiofrequency 1420.406 MHz. In the same way, the hyperfine structure of the molecular radical OH, present in the interstellar medium and circumstellar media, leads to several lines in the neighbourhood of $1 6 6 7 \mathrm { M H z }$ $\lambda \approx 1 8 \mathrm { c m }$ ).

Molecular Transitions

The movements of molecular structures (rotation, vibration) require less energy than those associated with electronic transitions. Their spectral signatures are thus located in the infrared, submillimetre, and millimetre regions.

The simplest case is a rotating dissymmetric diatomic molecule, possessing therefore a non-zero dipole moment, and moment of inertia $I$ . When quantised, this motion is characterised by a quantum number $J$ and a corresponding energy

$$
E ( J ) = \hbar ^ { 2 } \frac { J ( J + 1 ) } { 2 \cal { I } } .
$$

Radiative transitions $J  J - 1$ , referred to as pure rotational transitions, produce photons of energy $\hbar ^ { 2 } J / I$ .

„As an example, the molecule CO exhibits a fundamental transition 1–0 at wavelength $\lambda = 2 . 6 ~ \mathrm { m m } ~ ( 2 3 0 . 5 3 8 ~ \mathrm { G H z } )$ , as well as all the transitions for higher values of $J$ D, which occur in the submillimetre and far infrared. The same is true for a great number of molecules and radicals to be found in molecular clouds.

Quantising the vibratory motions of the atoms which make up a molecule gives more widely separated energy levels, usually in the range 1 to $1 0 ^ { - 2 } \mathrm { e V } .$ Each of these levels is split into sublevels by the molecular rotation. A whole range of transitions becomes possible, and this gives an appearance of complexity to the vibrational– rotational spectra of molecules, situated in the near and middle infrared $( 1 { - } 1 0 0 \mu \mathrm { m } )$ . Only moderate excitation temperatures are required, in the range 100 to $3 0 0 0 \mathrm { ~ K ~ }$ , and these exist in circumstellar envelopes, and the atmospheres of cold stars, when molecules or radicals like SiO or OH are present. Emission from the OH radical is also present in the Earth’s atmosphere. The hydrogen molecule $\mathrm { H } _ { 2 }$ deserves a special mention: it occurs abundantly, but is symmetrical, and thus displays no pure rotational spectrum. On the other hand, its vibrational–rotational spectrum can be observed in the near infrared $( \lambda \sim 2 \mu \mathrm { m }$ ), in particular during shock wave excitation.

Nuclear Lines

The quantification of the energy states of atomic nuclei leads to levels separated by very large energies, which means that the associated transitions are observed in the gamma-ray region. For example, the excited states of $\boldsymbol { ^ { 1 4 } \mathrm { N } }$ , $^ { 1 2 } \mathrm { C } .$ , and $^ { 1 6 } \mathrm { O }$ produce spectral de-excitation lines around 2.31, 4.43, and $6 . 1 4 \mathrm { M e V } ,$ , respectively.

Other mechanisms may also produce spectral lines. A case in point is the nucleosynthesis of elements, exemplified by cobalt $^ { 6 0 } \mathrm { C }$ lines at 1.33 and $1 . 1 7 \mathrm { M e V } .$ . These can be observed during supernova explosions, but are also produced in the interstellar medium by cosmic rays. Another case is the so-called positronium line, produced at $5 1 1 \mathrm { k e V }$ by electron–positron annihilation.

# Transitions in Solids

In a crystalline solid comprising a very great number of atoms (at least a thousand), the regularity from a large distance partially removes the individual properties of its atoms or molecules. The matter–radiation interaction manifests the collective energy transfers of the crystalline array, whose quantised vibrations are called phonons. These energies are necessarily less than the bonding energies within the crystal, which are of the order of $1 \ \mathrm { e V . }$ For this reason, the characteristic spectra of solids lie in the near or far infrared (between 1 and $1 0 0 ~ { \mu \mathrm { m } }$ ). Any given solid has characteristic frequencies depending on the mass of its atoms, the type of bonds between them (ionic or covalent), and so on. In the case of amorphous solids, which do not display the same ordered appearance as crystals, when viewed from a great distance, spectral lines can nevertheless be identified, and indeed, this is because there is some order over short distances. Hence, $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ ice, in crystalline form, has a characteristic emission wavelength near $4 5 ~ { \mu \mathrm { m } }$ and another near $3 . 0 5 ~ { \mu \mathrm { m } }$ , both of which are slightly displaced in amorphous ice.

Some of the transitions associated with solids are particularly important in determining the physical composition of small solid particles or grains, produced in comets, the atmospheres of cold stars, and also in novas. They are abundant in the interstellar medium. Silicates, like $\mathrm { S i O } _ { 4 } \mathrm { M g }$ , have been identified by their transition at $9 . 6 \mu \mathrm { m }$ , and so, too, has water ice, as mentioned earlier.

Between isolated molecules and macroscopic solids are aggregates, which may comprise from ten to several hundred molecules. They may exhibit the beginnings of a crystal structure, but without completely losing the spectral features of their constituent atoms or molecules. Polycyclic aromatic hydrocarbons (PAH), formed by juxtaposition of benzene rings, represent an intermediate stage in the progression towards the crystalline structure of graphite, and are present in the interstellar medium (Fig. 8.2). Their characteristic spectrum consists of lines in the near infrared $( 3 . 3 1 \mu \mathrm { m }$ , and a few others).

# 8.1.2 Information in Spectrometry

In this section we discuss the relation between the spectrum as measured and the information it contains about the physical conditions governing its emission. The aim is not to study how spectra are formed, which involves the transfer equation, but a few elementary notions are useful in understanding the constraints that spectroscopic observation and spectrometers must satisfy.

# Qualitative Features of a Spectrum

The great complexity of the process linking microscopic interactions of welldefined frequency $\nu _ { 0 }$ , and observed spectra $I ( \nu )$ , has already been underlined. Figure 8.1 shows some local views of a spectrum $I ( \nu )$ , and highlights the main empirical characteristics of a spectral line, which must be physically interpreted later.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/48d189240753e630b069ee69978ac3e5f0565f26968f826229963a67c400ed22.jpg)  
Fig. 8.2 The spectra of molecular aggregates. Upper: Observed spectrum of the object HD 44179, a galactic reflection nebula, known as the Red Rectangle. The spectrum was obtained in the near infrared, using a variable passband interference filter. Those lines not originating in atoms or elementary molecules are indicated by their wavelength. (After Russell, 1978). Lower: Emission spectrum of coronene $\mathrm { C } _ { 2 4 } \mathrm { H } _ { 1 2 }$ . The probable identification of the lines as originating from coronene, or a PAH of this type, is made by comparison. From Leger A., Puget J.L., Astron. Ap. ´ 137 L5, 1984. With the kind permission of Astronomy and Astrophysics

A spectrum consists of a continuous part $I _ { \mathrm { c } } ( \nu )$ , varying slowly with $\nu$ (for example, blackbody radiation), and superposed lines. The following definitions will be useful:

• Line Profile. Several parameters are used to represent complex profiles in a simplified way (Fig. 8.1): the full width at half maximum, or at half depth, $\Delta \nu _ { 1 }$ , the half power beam width, or HPBW, and the equivalent width, $\Delta \nu _ { 2 }$ . These convenient parameters are only of use if the line profile is relatively simple. Also used are the core or centre, the flanks or edges, and the wings. Line Intensity. This denotes the total power contained within the line, excluding any contribution from the continuum. The relative intensity measures the contrast between the line and the continuum (Fig. 8.1d). Line Position. This quantity is just the position of the maximum of $I ( \nu )$ , for emission, and the position of the minimum of $I ( \nu )$ , for absorption. It can be given as a frequency $\nu$ (Hz), a wavelength $\lambda$ , a wave number $\sigma = 1 / \lambda$ $( \mathrm { c m } ^ { - 1 }$ or kayser), or an energy $h \nu$ D(eV). If the line is broad or highly asymmetric, it may be preferable to define its position as the frequency corresponding to the full width at half maximum or the HPBW.

• Polarisation of $I ( \nu )$ . The spectrum may not be the same when observed in different polarisations. For example, the spectra $I _ { + } ( \nu )$ and $I _ { - } ( \nu )$ , observed in C two opposite circular polarisations, will be different if the radiation is produced by the Zeeman effect.

Each of these empirical parameters can be used to describe an arbitrary spectrum, in any spectral region, from the gamma-ray region to radiofrequencies.

# Physical Parameters Associated with Lines

The first and most fundamental application of spectroscopy in astrophysics is to identify the presence of some element, molecule, or ion in the emitting region. This science began in 1868, with the spectroscopic discovery of helium in the solar spectrum (Lockyer). Measurement of macroscopic velocity fields is often made concurrently. Smaller spectral shifts, due to gravity or magnetic fields, are supplementary sources of information.

Position of the Line

The position $\nu _ { 0 }$ of the line is related to the transition which produced it, and thus, taking into account the accuracy with which spectroscopic frequencies can be determined in the laboratory, to the well-identified presence of some given constituent. However, a frequency change may have occurred somewhere between emission and reception, and this complicates the identification. We now consider some of the possible causes of such a change.

Doppler Effect. The emitter is in motion relative to the observer, with relative velocity $\nu$ . The resulting change in frequency $\Delta \nu$ , referred to as the Doppler effect, is given by:

$$
\Delta \nu = \left\{ \begin{array} { l } { { \displaystyle \nu _ { 0 } \frac { \nu _ { \parallel } } { c } , \qquad \mathrm { n o n - r e l a t i v i s t i c ~ c a s e ~ } \left( \nu \ll c \right) , } } \\ { { \displaystyle \nu _ { 0 } \left[ 1 - \frac { \left( 1 - { \nu _ { \parallel } ^ { 2 } / c ^ { 2 } } \right) ^ { 1 / 2 } } { 1 - \nu _ { \parallel } / c } \right] , \qquad \mathrm { r e l a t i v i s t i c ~ c a s e } , \ } } \end{array} \right.
$$

where $\nu _ { \parallel }$ is the projection of the velocity along the line of sight. Some types of kmotion are relatively simple, well understood, and easy to correct for, such as the relative motion of the Earth (diurnal or orbital rotation), the motion of a space observatory relative to the Sun, or the motion of the Sun relative to the centre of mass of the Galaxy. Other types of motion are less well understood, such as the relative speed at which a gas jet is ejected from a galaxy, or the local speed of rotation of some element within a molecular cloud. The Local Standard of Rest, or LSR, is therefore defined, choosing if possible the centre of mass of the object under study. After correcting for any trivial effects, the speed $\nu _ { \mathrm { L S R } }$ of the LSR relative to the Earth can be defined, and also the local velocity field relative to the LSR:

$$
\nu _ { \mathrm { l o c a l l } } + \nu _ { \mathrm { L S R \parallel } } = c \frac { \Delta \nu } { \nu _ { 0 } } .
$$

For small speeds $( \nu \ll c )$ , corrections are correspondingly small, and transitions are easy to identify. The speeds can then be deduced. By contrast, for the observation of distant objects, with large cosmological redshift $z = \Delta \nu / \nu$ ; $z \sim 1$ , such as quasars D or galaxies, it may be difficult to identify the spectrum, knowing neither the value of $z$ nor the transition frequency in the laboratory frame.

An original application of the Doppler effect is Doppler imaging. Consider the surface of a rotating star, as seen by a distant observer, who is assumed for simplicity to be in the equatorial plane of the star. The photosphere of the star may contain spots, characterised by their lower temperature and the presence of a magnetic field. Both of these factors influence the profiles of spectral lines emitted by such spots, which thus differ from the profiles of lines emitted in calmer photospheric regions. The speed of rotation, projected along the line of sight, depends on the latitude and longitude of the emitting point, and varies right through the rotation, unless the spot is located at one of the poles. In general, the observer does not have available an instrument capable of resolving such details on the stellar surface, and a single spectrum is obtained which mixes together all the information coming from the various points of the surface. However, this spectrum exhibits an evolution in time, and the profile of any particular line will also evolve. It is then possible to invert, in some sense, the set of profiles obtained over a period of time, and reconstruct the configuration of spots over the stellar surface (their extent, temperature, and even their magnetic field), with the help of several reasonably simple assumptions. A kind of image is thus obtained, without possessing any other information than the spectrum (Fig. 8.3).

Zeeman Effect. When the line $\nu _ { 0 }$ is produced in the presence of a magnetic field, the existence of Zeeman sublevels causes several components to appear, with different frequencies and polarisations. In the simplest case (the normal Zeeman effect), three components appear, with frequencies $\nu _ { 0 }$ (the $\pi$ component) and $\nu _ { 0 } \pm \Delta \nu$ (the $\sigma$ components). The formula for $\Delta \nu$ is

$$
\Delta \nu = \frac { e B } { 4 \pi m } = 1 . 4 \times 1 0 ^ { 1 0 } B ,
$$

where $B \ [ \mathrm { T } ]$ is the magnetic field. The $\pi$ component is linearly polarised in the plane containing the line of sight and the direction of the magnetic field, whereas the $\sigma$ components are elliptically polarised. If $B$ is directed along the line of sight, the $\pi$ component disappears, and the $\sigma$ components are circularly polarised. The Zeeman shift may be much less (by a factor of $5 \times 1 0 ^ { - 3 }$ ) than the width $\Delta \nu$ of the line, as described above, but nevertheless detectable through its polarisation property. The magnetic field of sunspots has been measured using a magnetograph to detect the Zeeman shift of lines at visible frequencies. The interstellar galactic magnetic field has been measured by its Zeeman splitting of the hydrogen $2 1 \ \mathrm { c m }$ line, using the polarisation selectivity of radiofrequency detectors.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/561ddd714fe9a6d43f79eab1d877338d52c0ea9fe5842ef7143bb856b23bb517.jpg)  
Fig. 8.3 Doppler imaging of a T Tauri star. The star V410 Tau is observed in the lithium line $( \lambda = 6 7 0 . 7 ~ \mathrm { n m } )$ ) at different instants. The line profile (bottom) varies in time and is measured by Dthe phase $\phi$ of the rotation of the star, which has period 1.52 days. Using the profiles for various values of $\phi$ , a unique surface brightness distribution can be deduced $( t o p )$ , which clearly shows the spots, at temperature $3 0 0 0 \mathrm { K }$ , on a photosphere at temperature $4 8 0 0 \mathrm { K }$ . The Aurelie spectrometer ´ with the $1 . 2 ~ \mathrm { m }$ telescope at the Observatoire de Haute-Provence (France). Document courtesy of Joncour I., 1994

Einstein Effect. When a photon of frequency $\nu _ { 0 }$ leaves the surface of a massive object, its frequency changes, and this gravitational redshift is given by

$$
{ \frac { \nu _ { 0 } - \nu } { \nu } } = \left( 1 - { \frac { 2 G M } { R c ^ { 2 } } } \right) ^ { - 1 / 2 } - 1 ,
$$

or, in a weak gravitational field,

$$
{ \frac { \Delta \nu } { \nu } } \sim { \frac { G M } { R c ^ { 2 } } } .
$$

This effect is very slight, but nevertheless measurable, in the case of the Sun. It becomes more significant for white dwarfs, and even more so again for neutron stars.

Line Intensity

The integrated intensity (Fig. 8.1c), which measures the total absorption or emission in a line, is a function of the number $N$ of nuclei, atoms, ions, molecules, or solid grains taking part in the transition at $\nu _ { 0 }$ :

$$
\int _ { \mathrm { l i n e } } \left[ I ( \nu ) - I _ { \mathrm { c } } \right] \mathrm { d } \nu = f ( N ) .
$$

This is a linear relation when $N$ is small enough, but ceases to be so when $N$ becomes large and the line is saturated. The theory of the growth curve of lines determines $f ( N )$ , and in particular its linear part, as a function of the characteristic atomic parameters of the $\nu _ { 0 }$ transition. Indeed, we have now arrived at the second fundamental application of spectroscopy, namely, determination of the abundance of a given constituent in the emitting region.

Line Profile

The profile $\phi ( \nu )$ is defined here as a function describing as closely as possible the shape of the line, and normalised to unity:

$$
\int \phi ( \nu ) \mathrm { d } \nu = 1 .
$$

The profile $\phi ( \nu )$ of a line reflects exactly the local physical conditions which produced it.

Doppler Lines

When the atoms, ions, or molecules undergoing transitions are in Maxwellian thermal agitation, at some temperature $T$ , the line profile is primarily determined by the Doppler effect due to that agitation. It is given by a Gaussian function

$$
\phi ( \nu ) = \frac { 1 } { \sigma ( 2 \pi ) ^ { 1 / 2 } } \exp \left[ - \frac { ( \nu - \nu _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] ,
$$

where the frequency dispersion $\sigma$ is given by

$$
\sigma = \frac { \nu _ { 0 } } { c \sqrt { 2 } } \left( \frac { 2 k T } { m } + V ^ { 2 } \right) ^ { 1 / 2 } ,
$$

and $m$ is the mass of an individual atom, ion, or whatever type of particle is involved. This general expression for $\sigma$ includes both the kinetic effect of the temperature $T$ , and also those effects due to any isotropic microturbulence speeds, whose most likely value is denoted by $V$ .

The full width at half maximum of this profile is called the Doppler width of the profile and is given by

$$
\Delta \nu _ { \mathrm { D } } = \frac { 2 \nu _ { 0 } } { c } \left[ \ln 2 \left( \frac { 2 k T } { m } + V ^ { 2 } \right) \right] ^ { 1 / 2 } = 2 . 3 5 5 6 \tau .
$$

A maser line is formed when a self-amplified stimulated emission process is predominant, a situation which arises, for example, with $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ lines and radical OH lines in the interstellar medium. In this case, the width of the line is reduced compared with the expression given above, the amplification being more intense for frequencies at which the line is already intense. If $\tau _ { 0 }$ is the optical depth at the centre of the line, assumed unsaturated, the width is given by

$$
\Delta \nu = \frac { \Delta \nu _ { \mathrm { D } } } { \sqrt { \tau _ { 0 } } } .
$$

Table 8.2 gives some typical relative widths, for later comparison with the resolution of spectrometers.

When the medium emitting the line manifests additional macroscopic motions, such as large scale rotation, macroturbulence, spherically symmetric expansion or collapse, etc., the line profile carries the signature of these motions and can be interpreted.

# Lines Dominated by Collisions

At sufficiently high pressures, collisions between those particles undergoing transitions and other particles of the medium lead to a further damping effect, which

Table 8.2 Doppler spectral widths (hydrogen atom)   

<table><tr><td>V [km s-1]</td><td>T[K] △v/vo</td></tr><tr><td>0</td><td>1.9×10-6 6×10-5</td></tr><tr><td>0</td><td>104</td></tr><tr><td>0.3</td><td>10 2.7×10-6</td></tr><tr><td>30</td><td>10 2×10-4</td></tr></table>

Table 8.3 Physical and spectroscopic parameters   

<table><tr><td>Type of element</td><td>Line position</td></tr><tr><td>Abundance</td><td>Intensity or equivalent width</td></tr><tr><td>Macroscopic velocity field</td><td>Position and profile</td></tr><tr><td>Temperature,pressure,gravity</td><td>Intensity</td></tr><tr><td>Microscopic velocity field</td><td>Profile</td></tr><tr><td>Magnetic field</td><td>Zeeman components,polarisation</td></tr></table>

broadens the line. The line profile, in this case, is referred to as a Lorentz profile and is given by

$$
\phi ( \nu ) = \frac { 1 } { 2 \pi } \frac { \Delta \nu _ { \mathrm { L } } } { ( \nu - \nu _ { 0 } ) ^ { 2 } + ( \Delta \nu _ { \mathrm { L } } / 2 ) ^ { 2 } } ,
$$

where $\Delta \nu _ { \mathrm { L } } = 1 / \pi \tau$ , and $\tau$ is the mean time between collisions, directly related to Dthe physical conditions described by agitation speed and collision cross-section.

General Case

A more complex profile, called the Voigt profile, results when the Lorentz and Doppler widths are of comparable order. This profile is the convolution of the two previous profiles.

This brief review shows that the profiles of spectral lines are a rich source of information about the physical conditions that prevail in the emitting region (Table 8.3).

# 8.2 Spectrometers and Their Properties

Ideally, a spectrometer is an instrument that can measure and deliver the quantity

$$
I _ { 0 } ( \nu , \pmb \theta )
$$

which describes the intensity received from the source, as a function of the frequency $\nu$ , for each direction $\pmb \theta$ of the object. If the observation is made simultaneously for several values of $\pmb \theta$ , and therefore in several pixels of the image, the instrument is referred to as an imaging spectrometer.

In practice, the spectrometer delivers a quantity $I ( \nu , \pmb \theta )$ differing from $I _ { 0 } ( \nu , \pmb \theta )$ . Indeed, its ability to discriminate between two neighbouring frequencies is never perfect. The detector associated with it, which measures the received intensity, suffers from fluctuations or noise, and the image (or $\pmb \theta$ dependence), if such is provided by the spectrometer, is subject to distortion, aberration, and so on. And, of course, the spectrometer can only provide the values of $I ( \nu , \pmb \theta )$ in the limited frequency range for which it was designed.

A spectrometer and the detector associated with it must therefore be adapted to the type of source (point-like or extended), and the type of spectrum (spectral region, width and intensity of lines), in order to obtain the maximum amount of information in the shortest possible measurement time.

# 8.2.1 Quantities Characterising a Spectrometer

# Spectral Resolution

This fundamental quantity refers to the capacity of the spectrometer to give the frequency dependence of $I ( \nu , \pmb \theta )$ , and is illustrated in Fig. 8.4. It is a direct consequence of the way the spectrometer is designed. We consider here an instrument with no imaging capacity, and therefore limited to one direction $\pmb \theta$ , or to a single image pixel.

The instrumental profile $P ( \nu )$ is the frequency point response of the spectrometer, that is, the quantity $I ( \nu )$ delivered when the incident radiation $I _ { 0 } ( \nu )$ consists of one infinitely narrow line $I _ { 0 } ( \nu ) = \delta ( \nu - \nu _ { 0 } )$ .

D The observed spectrum of a source with general spectrum $I _ { 0 }$ is given, for a linear detector, by the convolution

$$
I ( \nu ) = P ( \nu ) \star I _ { 0 } ( \nu ) .
$$

The equivalent width $\Delta \nu _ { \mathrm { P } }$ of the instrumental profile is defined by

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/a60b252e0e20faf63a9216403726c59cede79dfd52b1fc11b94665ed841ee574.jpg)  
Fig. 8.4 Observation of a spectral line at increasing resolution. (a) $R \sim 0$ . (b) The line appears. (c) The line appears double, but unresolved (blended). (d) The two lines are resolved. (e) The true width of the lines is attained, and line purity can be no further improved by increasing $R$ . The horizontal line shows the instrumental spectral width $\Delta \nu = \nu _ { 0 } / R$ Dused in each observation

$$
\Delta \nu _ { \mathrm { P } } = \frac { \int P ( \nu ) \mathrm { d } \nu } { P ( \nu _ { 0 } ) } .
$$

It is clear that two instrumental profiles of the same equivalent width may have very different shapes, and hence specific advantages and disadvantages. The presence of extended wings would not obstruct the search for faint lines around some principal line, but could impede the exact determination of a continuum.

The resolution criterion is defined as the ability of the spectrometer to distinguish two lines $\displaystyle \delta ( \nu - \nu _ { 1 } )$ and $\displaystyle \delta ( \nu - \nu _ { 2 } )$ , when the signal-to-noise ratio is assumed infinite.  It depends on the exact shape of the profile $P ( \nu )$ . It is assumed, as a convenient approximation, that the minimum separation which can be resolved is

$$
\nu _ { 2 } - \nu _ { 1 } = \Delta \nu _ { \mathrm { P } } ,
$$

and then the spectral resolving power, or simply the spectral resolution, is defined to be the quantity

$$
R = \frac { \nu _ { 0 } } { \Delta \nu _ { \mathrm { P } } } .
$$

A measurement of $I ( \nu )$ , sampled at an interval $\Delta \nu$ , possibly much greater than $\Delta \nu _ { \mathrm { P } }$ , is called a spectral element, or bin. The precise sampling interval to adopt depends on the shape of the instrumental profile $P ( \nu )$ , and a correct application of the sampling theorem (see Sect. 9.1.3). Recall that, applying the latter, there is no point in sampling the measurement points of $I ( \nu )$ at closer frequency intervals, provided that any noise has been adequately filtered.

The distinction between photometry and spectrometry is rather arbitrary, since in both cases a specific part of the spectrum is singled out. There is a general consensus that spectrometry (or spectroscopy) refers to situations in which the spectral resolution $R$ exceeds a few units.

Table 8.4 gives some typical resolutions $R$ of those spectrometers considered later in the chapter. It is instructive to compare these values with the intrinsic widths of spectral lines given in Table 8.2. Observe that, apart from exceptional cases (for example, measurement of the gravitational redshift by the Sun), it serves no purpose to push the resolution beyond $1 0 ^ { 6 }$ . Another special case of major astrophysical importance is the measurement of the radial velocities of stars in order to detect exoplanets. Here, the accuracy required for the velocity is of the order of $1 ~ \mathrm { m } \mathrm { s } ^ { - 1 }$ , i.e., a resolution $R$ of the order of $3 \times 1 0 ^ { 8 }$ (see Sect. 8.3).

# Beam Etendue (Throughput)

A spectrometer can accept a maximum beam etendue or throughput´ $E \ = \ A \varOmega$ , whilst preserving its maximum resolution, where $A$ Dis the area of its dispersive element, and $\varOmega$ is the solid angle of the beam it accepts. The larger the value of the accepted beam etendue, the greater the ´ light gathering power of the spectrometer. Since the beam etendue is conserved during propagation through an ´ optical instrument, the condition for the spectrometer to operate with a telescope of collecting area $A _ { \mathrm { T } }$ , gathering the radiation from a source in the sky subtending a solid angle $\omega$ , is simply

Table 8.4 Resolution of spectrometers. The values given in the table are typical orders of magnitude, and should not be considered as absolute   

<table><tr><td>Spectrometer</td><td>Region</td><td>Typical resolution</td></tr><tr><td>Interference filter</td><td>Visible, IR</td><td>102-103</td></tr><tr><td>Grating</td><td>IR, visible,UV</td><td>10-106</td></tr><tr><td>Bragg crystal</td><td>X ray</td><td>103</td></tr><tr><td>Atomic resonance</td><td>Visible,UV</td><td>107</td></tr><tr><td>Fabry-Pérot</td><td>Visible, IR</td><td>104-106</td></tr><tr><td>Fourier transform</td><td>Visible,IR</td><td>104-106</td></tr><tr><td>Heterodyne</td><td>Radiofrequencies</td><td>&gt;106</td></tr><tr><td></td><td>IR,submillimetre</td><td>&gt;105</td></tr><tr><td>Bolometer (detector)</td><td>X ray</td><td>10²</td></tr><tr><td>Scintillator (detector)</td><td>yray</td><td>103</td></tr></table>

$$
A _ { \mathrm { T } } \omega = A \Omega .
$$

This simple relation shows that a spectrometer with a wide field of view on the sky $( \omega )$ must have either a large dispersive element (large $A$ ), or highly inclined beams (large $\varOmega$ ). All things being equal, the size of the spectrometer must increase with that of the telescope $( A _ { \mathrm { T } } )$ , and this imposes a considerable constraint for optical telescopes exceeding 8 or $1 0 \mathrm { m }$ in diameter.

When radiation is detected coherently, at radiofrequencies, the etendue of the ´ spectrometer is necessarily equal to $\lambda ^ { 2 }$ (see Sect. 6.1.1).

# Transmission

This is defined for each frequency by

$$
t ( \nu ) = \frac { I _ { \mathrm { e x i t } } ( \nu ) } { I _ { \mathrm { e n t r a n c e } } ( \nu ) } ,
$$

and is an important factor in determining the throughput of the spectrometer. It can generally be optimised by adequate preparation of all the optical surfaces, in order to minimise reflection or transmission losses. Despite all these precautions, the total transmission of a spectrometer placed at the Coude focus of a telescope, ´ rarely exceeds $2 - 5 \%$ .

# Signal-to-Noise Ratio

When the spectrometer has been fitted with a detector, the final spectrum $I ( \nu , \pmb \theta )$ is characterised by a signal-to-noise ratio for each spectral element, and in the final result this will determine a confidence interval for any measurements of spectral line parameters.

If the instrumental profile $P ( \nu )$ is accurately known by calibrating the spectrometer with quasi-monochromatic radiation, $I ( \nu )$ can in principle be extracted by deconvolution (see Sect. 9.6), or, at least, the resolution can be somewhat improved. In practice, this cannot usefully be done unless the measurement has a high signalto-noise ratio $( > 1 0 ^ { 2 } )$ .

# 8.2.2 Spectral Discrimination

Spectrometers can be based on a range of different physical principles depending on the spectral region and the desired resolution $R$ . The aim is always to isolate a spectral element of fixed width with minimal contamination by neighbouring spectral elements. This can be achieved in various ways, outlined here and further discussed later:

• Interference Method. The spectral element is isolated by imposing a phase change on the incident wave, then arranging for constructive interference of this wave at the desired frequency and destructive interference at other frequencies. This method is applied over a very broad spectral range from X rays to the far infrared. It uses optical components like interference filters, gratings, or more elaborate systems like Michelson or Fabry–Perot interferometers. ´   
. Resonant Electrical Filters. After reducing the frequency, the electrical signal generated by the incident wave is distributed over a set of filters, each of which selects a spectral interval or element of resolution. This method is used at radiofrequencies on the intermediate frequency (IF) signal, or directly on the signal at very long wavelengths. Digital Autocorrelation. This method exploits the integral transformation property which, by Fourier transform, relates spectral density and autocorrelation (see Appendix A). At radiofrequencies, high performance correlators can be designed because it is easy to digitise the intermediate frequency (IF) signal, thereby allowing very flexible spectral selectivity. Atomic Resonance. In this original approach, highly efficient spectral selectivity is obtained by the response of an atomic vapour to excitation by the incident radiation, since this response occurs in a very narrow spectral region corresponding to the resonance line. Detector Selectivity. As we have seen in Chap. 7, a detector has a certain spectral selectivity, whereby it will be sensitive only in a limited spectral region. Some detectors based on semiconductors have spectral selectivity due to interband

transitions and are used in X-ray spectrometry. Likewise, in $\gamma$ ray astronomy, it is the properties of the detector itself that incorporate the spectroscopic function. For this reason, $\gamma$ ray spectroscopy was discussed in Chap. 7.

# 8.2.3 The Modes of a Spectrometer

The way the spectrometer is coupled to the associated detector(s) leads to the following different arrangements for determining the spectrum $I ( \nu , \pmb \theta )$ . Each has its own specific advantages and is designed to meet specific objectives: different resolutions, different spectral range, different fields of view to be covered, different numbers of objects to be studied simultaneously, and so on. There may also be other constraints, such as mass and volume for a spaceborne instrument, stability of frequency calibration, and so on. There are therefore many different configurations which we shall now review.

Sequential Spectrometer. This analyses, sequentially in time, the successive spectral elements of a single image pixel (i.e., a single point in the field). This is the case in a grating spectrometer, whose rotation scans the spectrum on a single detector. It thus provides a continuous spectrum. In the case of a Fourier spectrometer, it is the Fourier transform of the spectrum or interferogram which is explored step by step, and the spectrum itself is obtained at the end by a Fourier transform of the interferogram.

Multichannel Spectrometer. This combines a dispersive element and a multielement detector. Many spectral elements are recorded simultaneously, spectral scanning is unnecessary, and the gain in time is considerable. However, this only provides the spectrum of a single element of the source. An example is a grating spectrometer in conjunction with a CCD array (e.g., 2048 pixels), each pixel receiving a distinct spectral element. To cover a broad spectral range, echelle gratings are used. This is also the case for a heterodyne spectrometer equipped with a series of filters, receiving the IF signal in parallel, at radiofrequencies, or with a digital autocorrelator.

Imaging Spectrometer. This simultaneously records the same spectral element, of frequency $\nu$ , or even a set of spectral elements covering the relevant spectral range, for all directions $\pmb \theta$ of the observed field. This method is invaluable for efficient observation of extended objects. Various instrumental arrangements lead to a whole range of different ways of achieving this. The method is mainly used in the ultraviolet, visible, and infrared spectral regions, where multipixel detectors are available. The aim is always to maximise efficiency, that is, obtain the largest possible number $M$ of spectral elements across the largest possible number of image pixels, and this in the given measurement time $T$ .

For example, with a Fabry–Perot spectrometer, a single spectral element is´ obtained at a given instant of time in two dimensions of the image (on a CCD detector), then the successive spectral elements are obtained by scanning as time goes by. Alternatively, if the source has well separated emission lines, the two dimensions of the image can be obtained simultaneously with the spectral dispersion of the image. With the Fourier spectrometer, the imaging mode obtains an interferogram, hence a spectrum, for each point of the field of view.

In long-slit spectroscopy, one dimension of the image is explored along the slit, showing the spectral dispersion perpendicular to the slit. This idea is used to give spectral images of the Sun with a spectroheliograph. In a different version, the light from different points of the field is carried optically to a slit by an image slicer.

Finally, this method finds its most developed form in integral field spectroscopy (IFS). The image is sliced up using a microlens array, with one microlens per pixel of the field, and then each micro-image of the pupil is used as the source for a grism spectrograph, or else injected into an optical fibre which transfers the light to the entrance slit of a conventional spectrograph (the so-called argus method, named after the mythological shepherd with a hundred eyes). Another solution is to juxtapose image slicers which redistribute the light over the spectrograph slit, deflecting the light rays from each element of the image in a specific way. These optical components are generally extremely delicate to make. The dispersion angle is judiciously chosen so that the spectra do not overlap on the final CCD detector.

Multi-Object Spectrometer. In an extended field, when there are distinct objects such as stars and galaxies, it is interesting to build a spectrometer that can focus on the radiation emitted by each object in order to carry out spectral analysis, while ignoring the rest of the field. What makes this difficult is that no field is exactly like any other field, so the sampling of the field has to be reconfigured for each new observation. The development of cosmological observations and sky surveys (see Chap. 10) has stimulated this concept of multiple object or multi-object spectroscopy (MOS). It has been implemented on the very large telescopes with a high level of automation and remarkable efficiency. The field can be sampled by optical fibres or slits cut into a mask.

Spectrometers used in astronomy are usually coupled to a telescope which collects light and forms an image. Of particular importance are the focal ratio $f / D$ of the telescope, which can vary from 1 to 100, depending on the type of telescope and the focal point used, and the focal scale $a$ (in $\mu \mathrm { m }$ or mm per arcsec or per arcmin), which follows directly from the equivalent focal length $f$ of the telescope.

The spectrometer is thus designed to be part of a system, as has already been pointed out. Choosing which specific spectrometric combination to use is a complicated process. It depends on the spectral region, the resolution, the number $M$ of spectral elements required, the field to be covered, and, in certain cases, the simultaneous imaging capacity desired, the type of detector available for the relevant spectral region and the kind of noise affecting it, and finally, the size of the telescope to which the spectrometer must be coupled. We shall now give some examples.

# 8.3 Interferometric Spectrometers

This vast category of spectrometers uses interference devices. Spectral discrimination is obtained by introducing phase changes in the incident wave, and arranging for constructive interference to occur at the desired frequency, and destructive interference at all other frequencies.

# 8.3.1 General Criteria

The following parameters are used to compare the various configurations.

• The resolution $R \ : = \ : \nu / \Delta \nu \ : = \ : \lambda / \Delta \lambda$ , where $\Delta \nu$ (or $\Delta \lambda$ ) is the width of the spectral element. The total number $M$ of spectral elements, which gives the number of independent values of $I ( \nu )$ obtained in the measured frequency interval $( \nu _ { 1 } , \nu _ { 2 } )$ .   
. The total measurement time $T$ , which, for a given detector, fixes the signal-tonoise ratio for the measurement of the spectrum.   
. The power received from the source. Two cases arise: a point source, giving a monochromatic flux $e ( \nu )$ [ $\mathrm { W ~ m } ^ { - 2 } \ \mathrm { H z } ^ { - 1 } ]$ , and an extended source, characterised by its specific intensity $B ( \nu ) [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ]$ . The detector, characterised by its noise, the beam etendue it will accept, its ´ number of pixels, and the physical dimension of those pixels.   
. The beam etendue. It can be shown that, for any interferometric instrument, the´ maximum beam etendue that such a spectromete ´ r can accept, while maintaining a resolution $R$ , is

$$
U = Q { \frac { A } { R } } ,
$$

where $Q$ is a dimensionless geometric factor, characteristic of the type of instrument, and $A$ is the area of the dispersive element. The value of $U$ should be compared with the coherence etendue´ $\lambda ^ { 2 }$ , when a point source is the subject of observation. But when the source is extended, the spectrometer has greater light gathering power as $U$ increases, for any given resolution.

By combining these factors, a figure of merit can be defined for each configuration.2 For example, for a given observation time and resolution, the question as to which instrument gives the maximum number of spectral elements with the best signal-tonoise ratio can be answered, or which instrument gives the maximal signal-to-noise ratio and resolution for a single spectral element, and so on.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/a734ebb18bbe599f6e0567db6af8cee4ca72ddc44f39990f2ea0a625524254a9.jpg)  
Fig. 8.5 Principle of the interference filter. A single coating is shown

# 8.3.2 Interference Filters

This device (Fig. 8.5), used from the near ultraviolet to the far infrared, well illustrates the principle of spectral discrimination by multiple wave interference. The filter transmission is maximal for a given wavelength when the interference is destructive for the reflected waves. This implies that, for normal incidence,

$$
\frac { 2 n _ { 1 } ( \lambda _ { 0 } ) e } { \lambda _ { 0 } } + \frac { \pi } { 2 } = 2 k \pi .
$$

The condition is satisfied for a narrow band around $\lambda _ { 0 }$ and for certain other values $\lambda _ { i }$ , which are eliminated by an absorbing filter (transmission or absorption). Interference filters, which may contain more than ten layers, can give resolutions $R$ up to 1 000. This is illustrated by the spectra in Fig. 8.2. In the far infrared, the coatings would become too thick, and are replaced by metal grids.

Thin metal films, combining the interference and the absorption by the material, are used as transmission filters in the extreme ultraviolet $\lambda$ between 10 and $1 0 0 \mathrm { n m }$ ). Layers of aluminium, indium, or silicon, several tens of nanometres thick, constitute a narrow filter $( \lambda / \Delta \lambda \approx 1 )$ ), whose peak transmission can exceed $60 \%$ .

# 8.3.3 Grating Spectrometers

The grating spectrometer also uses multiple interference, the difference being that here all the waves, diffracted from a periodic structure, have the same amplitude.

# General Characteristics

Resolution

Let $a$ be the period of the diffracting element, $N$ the number of periods, $i$ and $i ^ { \prime }$ the angles of incidence and diffraction, respectively, $m$ the order, and $\lambda$ the wavelength. The condition for constructive interference is (Fig. 8.6a)

$$
\sin i \pm \sin i ^ { \prime } = m { \frac { \lambda } { a } } \qquad ( \mathrm { g r a t i n g ~ r e l a t i o n } ) ,
$$

where the sign on the left-hand side is $+$ for a reflection grating and  for a transmission grating.

The angular dispersion is obtained by differentiating the grating relation, for fixed $i$ , which gives

$$
\frac { \mathrm { d } i ^ { \prime } } { \mathrm { d } \lambda } = \frac { m } { a \cos i ^ { \prime } } .
$$

The resolution can be deduced from the angular width of the diffraction pattern of the grating, which forms the entrance pupil of the spectrometer,

$$
( \mathrm { d } i ^ { \prime } ) _ { \mathrm { p u p i l } } = \frac { \lambda } { N a \cos i ^ { \prime } } .
$$

Equating $( \mathrm { { d } \it { i ^ { \prime } ) _ { \mathrm { p u p i l } } } }$ with $( \mathrm { d } i ^ { \prime }$ /dispersion gives

$$
\frac { m \mathrm { d } \lambda } { a \cos i ^ { \prime } } = \frac { \lambda } { N a \cos i ^ { \prime } } ,
$$

which implies, finally,

$$
R = m N .
$$

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/9d76e2045f8822738d06ebe8dbfecfe0b32733436fb2dc285b0ed146cfe4eb49.jpg)  
Fig. 8.6 Principle of the diffraction grating

This value, $R = m N$ , is a maximum resolution. Often the actual resolution $R ^ { \prime }$ is Dless, being determined by the width $L$ of the entrance slit of the spectrometer. This is placed at the focal point of a collimating mirror of focal length $f _ { \mathrm { c o l l } }$ (Fig. 8.6b). In the end, for ground-based observation, the choice of $L$ is determined by the seeing, i.e., the width of the image spot at the telescope focus. This is why the collimator of a high-resolution spectrograph must have a very long focal length. The actual resolution is then

$$
R ^ { \prime } = \frac { \sin i \pm \sin i ^ { \prime } } { \cos i ^ { \prime } } \frac { f _ { \mathrm { c o l l } } } { L } .
$$

Another parameter often used is the inverse linear dispersion, expressed in $\mathrm { { \AA m m ^ { - 1 } } }$

$$
D = \frac { \mathrm { d } \lambda } { f _ { \mathrm { c a m } } \mathrm { d } i ^ { \prime } } = \frac { m } { a \cos i ^ { \prime } } ,
$$

where $f _ { \mathrm { c a m } }$ is the focal length of the camera mirror (Fig. 8.11).

Calculation of the Factor $Q$

Because a slit must be used to illuminate the grating (Fig. 8.6b), the beam etendue is ´

$$
U = \beta A \cos i \mathrm { d } i ,
$$

where $A$ is the area of the grating and $\beta$ is the angular height of the slit. At fixed wavelength, the two relations

$$
\cos i \mathrm { d } i + \cos i ^ { \prime } \mathrm { d } i ^ { \prime } = 0
$$

and

$$
\cos i ^ { \prime } \mathrm { d } i ^ { \prime } = m { \frac { \lambda } { R a } }
$$

$$
U = \beta \frac { m \lambda } { a } \frac { A } { R } .
$$

Since

$$
U = Q { \frac { A } { R } } ,
$$

we deduce that $Q \sim \beta$

Aberration by the collimating mirror means that $\beta$ has to be limited to small angles $( 1 0 ^ { - 2 } – 1 0 ^ { - 1 }$ rad), thus limiting the usable etendue, and hence the energy ´ accepted by the spectrometer.

# Blazed Grating

For an arbitrary shape of periodic diffracting structure, energy is diffracted in an essentially uniform manner into the different orders $m$ , and restricting to just one order is inefficient. The directions of constructive interference and specular reflection from the blazed faces of the grating can be made to coincide, for given wavelength and order, by choosing a suitable shape for the periodic structure (Fig. 8.7). The condition to the blaze is (reflection grating)

$$
i - \theta = i ^ { \prime } + \theta , \quad \theta = \frac { i - i ^ { \prime } } { 2 } , \quad m \lambda _ { \mathrm { b } } = 2 a \sin \theta \cos ( i - \theta ) .
$$

The blaze angle $\theta$ is fixed by construction, so that just one blaze wavelength $\lambda _ { \mathrm { b } }$ is associated with each order.

# Echelle Grating

The idea here is to use a very high order of interference $m$ , with a long period $a$ $( \gg \lambda )$ and a large angle of incidence, such that the Littrow condition $i = i ^ { \prime } = \theta$ is satisfied. At the blaze wavelength, the grating relation is (Fig. 8.8)

$$
m \lambda _ { \mathrm { b } } = 2 a \sin i = 2 t ,
$$

and the resolution $R$ is, for a slit of width $L$ and a collimator of focal length $f _ { \mathrm { c o l l } }$

$$
R = 2 \tan \theta { \frac { f _ { \mathrm { c o l l } } } { L } } .
$$

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/b4d05604f0affd6e46aff8423bb85e88baf92407caa9161035742688a1860092.jpg)  
Fig. 8.7 Blazed grating. $\pmb { n }$ is normal to the grating, $\pmb { n } _ { 1 }$ is normal to the blazed faces, and $\theta$ is the blaze angle   
Fig. 8.8 Echelle Grating

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/783fc8a37601f072f2a5bd55511d0681f5af5801b0e732d8a530d7d046f3435b.jpg)  
Fig. 8.9 Echellogram obtained by the International Ultraviolet Explorer (IUE) satellite mission. Spectrum of the A-type supergiant $\alpha$ Cyg, in the range $2 0 0 { - } 3 3 0 ~ \mathrm { n m }$ . Spectral resolution $0 . 0 2 { \mathrm { n m } }$ . The detector is a Vidicon tube, with $7 6 8 \times 7 6 8$ pixels. The dynamic range is 0–256 counts, each level corresponding to an increment of 16 counts. (a) Photo of the whole field. (b) Enlargement showing an emission continuum and an absorption line. (European Space Agency and Praderie F., 1984, private communication)

As $a$ is relatively large, the periodicity can be accurately maintained over a large number of grooves, which leads to high resolution $R = m N$ ) and high dispersion $( \propto m / a )$ .

Example. A square grating of side $5 \ \mathrm { c m }$ has 40 grooves per mm $( a \ : = 2 5 \ : \mu \mathrm { m }$ ), blazed at $\lambda _ { \mathrm { b } } = 4 3 0 \mathrm { n m }$ . For an angle of incidence $i = 6 0 ^ { \circ }$ ,

$$
N = 2 0 0 0 , \quad t = 2 1 . 6 ~ { \mu \mathrm { m } } , \quad m = 1 0 0 , \quad R = 2 \times 1 0 ^ { 5 } .
$$

The orders tend to overlap. The quantity $\Delta \lambda$ defined by

$$
( m + 1 ) \lambda = m ( \lambda + \Delta \lambda ) ,
$$

which implies

$$
\Delta \lambda = \frac { \lambda } { m } ,
$$

is called the free spectral interval. This spectral interval becomes smaller as m increases, so that an extended spectral region cannot be studied without confusion arising between orders. For this reason, a predisperser is introduced. This is a grating or prism whose direction of dispersion is orthogonal to that of the principal grating. Each order is then separated from adjacent orders, and the entire spectrum, or echellogram, appears in the form of parallel bands (Fig. 8.9). An echelle grating is thus ideal for coupling with a two-dimensional detector (CCD), and we shall give several examples below.

Making Gratings

The requirements here are high resolution and broad spectral coverage. Echelle gratings with $a \gg \lambda$ can cover the far ultraviolet $\lambda \gg 5 0 \mathrm { n m } )$ and are only limited by the reflection power of the metal deposits used to make them. Ordinary gratings with $a \gtrsim \lambda$ can be made on large scales $N a \sim 0 . 2 – 0 . 5 \mathrm { m }$ . The grating can be made directly from a photograph of the diffraction pattern by the process of holographic etching. Extremely regular spacings can be obtained. The price to pay is a sinusoidal profile focusing the energy less efficiently than a blazed grating. If necessary, the grating can be deposited on a spherical surface, or even on an aspherical surface, which optimises the quality of the image formed on the detector.

In the infrared (large $\lambda$ ), there is no difficulty in making gratings, but the requirement of high resolution leads to prohibitive sizes, e.g., $R = 1 0 ^ { 6 }$ at $1 0 0 \mu \mathrm { m }$ would lead to $N a = 1 0 0 \mathrm { m }$ !

From the 1990s, it has been known how to make grating arrays in order to increase the effective value of Na. For example, the Ultraviolet Visible Echelle Spectrograph (UVES) of the European VLT uses two plane gratings with a blaze angle of $7 6 ^ { \circ }$ . Holographic gratings can now be made with a non-sinusoidal profile by means of reactive ion etching, whereby the initial sinusoidal profile is modified by ion bombardment.

At X-ray wavelengths $\cdot 0 . 5 \mathrm { - } 1 0 \ \mathrm { n m } )$ , it is still possible to use reflection gratings etched on silicon carbide (SiC) and coated with gold. The European space mission XMM–Newton (1999–2010) carries a reflection grating spectrometer (RGS), whose grating comprises 182 independent and suitably aligned etched plates.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/ae9fb5a028218305c54b2270bf0936bd3fae9209cdd0136b7d412285d7db2fc3.jpg)  
Fig. 8.10 Transmission grating with spacing $3 5 \ \mu \mathrm { m }$ for a grism, made from germanium by anisotropic etching. Mid-infrared camera project for the European VLT. Electron microscope image courtesy of H.U. Ka¨ufl and the Fraunhofer Institut, M¨unich, 1994

# Grisms

The objective prism is a small angle prism (a few arcmin) placed on the entrance pupil. Each star or galaxy image is dispersed in the focal plane on the surface of a CCD detector, whence it becomes possible to carry out low resolution spectral analysis of each object over a wide field. The grism exploits a similar idea, but combines a transmission grating and a prism (Fig. 8.10). Note that only the grating really contributes to dispersion by a grism, the prismatic effect being entirely due to the structure of the grating. A grism is in fact nothing other than a blazed transmission grating.

# Volume Holographic Gratings

However carefully attempts are made to concentrate light in a single order, the efficiency of etched gratings is always reduced by the existence of multiple orders, which it is difficult to control fully. In the volume holographic grating, a thin film of transparent material is placed between two glass plates, and the refractive index of this material is modulated in intensity over a thickness that can also be adjusted. As in a surface grating, the spatial frequency of the modulation determines the diffraction angle (Bragg condition), while the diffracted energy fraction, which depends critically on the properties of the modulation (intensity and thickness), can be made closer to $100 \%$ by making the relevant spectral interval narrower. Such a grating can also be used as a spectral filter, adjusted by varying the angle of incidence.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/a37bac6f2a97cd0f522494e0c6c3aaaf61e3ed2de99def917829242ed43ed873.jpg)  
Fig. 8.11 Grating spectrometer arrangements. (a) Ebert–Fastie mounting with a planar grating. Here, a single mirror plays the role of both collimator and camera. This could also be achieved using two mirrors. (b) Rowland mounting with a concave grating. Rotating the assembly around the entrance slit varies the wavelength of radiation received by the detector. (c) Rowland mounting for the far ultraviolet. The grating operates at grazing incidence $( i = 8 2$ to $8 9 ^ { \circ }$ )

# Astronomical Grating Spectrometers

Figure 8.11 shows some simple arrangements, in which the classic components of a grating spectrometer can be identified: the entrance slit, the collimating mirror, or any equivalent optical device which gives a beam of parallel light (an afocal or collimated beam), the dispersive element, and the mirror, or any other optical device referred to as the camera, which recombines the dispersed image of the field on a one- or two-dimensional detector. It is sometimes possible to combine the collimator and camera functions into a single optical device. A certain number of additional elements can be joined to this basic configuration, such as a predisperser, crossdispersion, and so on. Having obtained the required resolution and field, the main concern is the quality of the optical image, and especially the total transmission, since spectrometers may contain a large number of reflecting surfaces.

A grating spectrometer must be coupled to a detector. Several coupling arrangements exist between dispersive element(s) and detector, depending on the desired resolution $R$ , and whether the detector is one- or two-dimensional (CCD). Some of these arrangements combine spectroscopy and imaging (spectro-imaging), and greatly improve the efficient use of the photons collected.

The various arrangements are as follows:

• One-Dimensional Detector. Only one source and one order. If the image of the source is bigger than the spectrometer slit (high $R$ or large seeing disk), an image slicer is required (fibre optics) and the spectrum obtained will mix together the radiation coming from all points of the source.

• Two-Dimensional Detector. At high resolution, echelle mode (cross dispersion): only one source but several orders of dispersion. At low resolution $( R < 1 0 ^ { 3 }$ ), single-order dispersion: one of the detector dimensions can then be used for $\lambda$ dependence, and the other for spatial dependence along one of the dimensions of the source, i.e., $( x , \lambda )$ -mode. If spatial information is not required, e.g., as happens for a source which is known a priori to be unresolved, the possibility of binning the pixels of a CCD, i.e., associating several pixels together, provides a way of summing several pixels in the direction of the slit and thereby increasing the signal-to-noise ratio (Sect. 7.4.6).

• Two-Dimensional Detector and Dispersion. In this mode, referred to as integral field spectrometry, spectral information and two-dimensional spatial information $( x , y , \lambda )$ are obtained simultaneously. This arrangement, originally due to the French astronomer G. Courtes, is clearly the one which makes the best use of the\` photons. We shall describe it in much greater detail later.

• Two-Dimensional Detector. One order, low resolution $( R < 1 0 ^ { 3 }$ ), or even high resolution, multi-object. By suitably dividing up the image plane (slit mask, fibre optics), the spectrometer samples the radiation at a limited number of image points, juxtaposing the spectra on the detector.

This subsystem must be adapted to the telescope, both from a mechanical point of view (choosing a focal point to suit its mass and stresses) and from an optical point of view (focal ratio, adaptive optics where necessary).

Associated Detectors

Let $f$ be the equivalent focal length of the exit mirror of the spectrometer. The pixel size of the detector must be no larger than

$$
f \frac { \lambda } { N a \cos i ^ { \prime } }
$$

in the direction of dispersion. Photographic plates have now been replaced either by linear arrays of photoelectric detectors, which contain as many sensitive elements as there are spectral elements to be measured simultaneously, or by 2D detectors (CCDs or infrared arrays) in the imaging modes described below.

The sampling condition (Shannon) requires at least two pixels of size $p$ per resolved spectral element, and hence states that

$$
2 p \leq { f _ { \mathrm { c a m } } } \mathrm { d } i ^ { \prime } = \frac { { f _ { \mathrm { c a m } } } } { R } \frac { \sin i \pm \sin i ^ { \prime } } { \cos i ^ { \prime } } = L \frac { { f _ { \mathrm { c a m } } } } { { f _ { \mathrm { c o l l } } } } \frac { \cos i } { \cos i ^ { \prime } } .
$$

The slit width $L$ thus appears, modified by the ratio of focal lengths and multiplied by an anamorphic factor which depends on the grating.

This can be expressed in another way: if $\alpha$ denotes the angular size of the slit on the sky (for example, the dimension of the seeing), $D$ the diameter of the primary mirror of the telescope, and $D _ { \mathrm { s } }$ the diameter of the spectrometer pupil (equal to the useful size of the grating), then

$$
2 p \leq \alpha D { \frac { f _ { \mathrm { c a m } } } { D _ { \mathrm { s } } } } { \frac { \cos i } { \cos i ^ { \prime } } } .
$$

This leads to the expression

$$
R = 2 \tan \theta { \frac { 1 } { \alpha } } { \frac { D \mathrm { s } } { D } }
$$

for the resolution, assuming the Littrow condition for simplicity.

Application. Returning to the grating used above, with a $D = 4 \mathrm { m }$ telescope, CCD pixels of $p = 1 5 ~ { \mu \mathrm { m } }$ , a Littrow mounting $( i = i ^ { \prime } )$ D), and a camera mirror of $f _ { \mathrm { c a m } } \approx$ $4 \ \mathrm { c m }$ D, the resolution is $R \ : = \ : 4 5 0 0$ Dfor a slit of dimension $\alpha = 1 ^ { \prime \prime }$ , which is the D Ddimension of an average seeing. This is a long way from the intrinsic resolution of the grating. With $D _ { \mathrm { s } } = 2 5 \mathrm { c m }$ (which implies a large grating, of length $5 0 \mathrm { c m }$ ), a resolution of $R = 4 5 0 0 0$ can be attained.

In order to cover a free spectral interval, the detector must contain $n _ { \mathrm { p } }$ pixels, where

$$
n _ { \mathrm { p } } = \frac { \lambda _ { \mathrm { b } } / m } { \lambda _ { \mathrm { b } } / R } = \frac { R } { m } , \qquad n _ { \mathrm { p } } = 2 0 0 0 .
$$

As the free spectral interval is $\lambda / m = 4 . 3 \mathrm { n m }$ , a $2 0 0 0 \times 5 0 0$ pixel detector would allow coverage of D the whole visible spectrum. Note that the information content of a single spectrum is considerable ( $1 0 ^ { 6 }$ pixels, 12 bits per pixel, and hence more than 10 Mbits per spectrum).

Beam Etendue

The elongated shape of a grating spectrometer slit creates difficulties in matching it to a large telescope. Indeed, consider an image formed on the slit. At ground level, atmospheric turbulence defines a pixel size of around $\theta = 0 . 5$ arcsec, in good conditions. If $A _ { \mathrm { T } }$ Dis the aperture of the telescope, the corresponding etendue is´

$$
U = A _ { \mathrm { T } } \theta ^ { 2 } .
$$

This etendue is accepted by the spectrometer if the slit width corresponds to ´ $\theta$ , implying

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/631b10c26e4a6318d72e4122baa3018095f713f4cfc342d692b64775e66e59c6.jpg)  
Fig. 8.12 Image slicer. (a) Seeing disk and spectrometer slit of comparable size. (b) Seeing disk more smeared, so that part of the energy misses the slit. (c) A bundle of optical fibres brings all the energy back to the slit

$$
A _ { \mathrm { T } } \theta ^ { 2 } \sim \frac { A } { R } { \mathrm { d } } i \sim \frac { A } { R ^ { 2 } } .
$$

Putting $A _ { \mathrm { T } } = 1 0 \mathrm { m } ^ { 2 }$ , $A = 1 \mathrm { m }$ , the result is

$$
R \lesssim \frac { 1 } { \theta } \sqrt { \frac { A } { A _ { \mathrm { T } } } } = 1 0 ^ { 6 } .
$$

At ground level, high resolutions thus require very good images and a telescope whose size does not exceed a few metres. For larger telescopes, an image slicer must be used (Figs. 8.12 and 8.17), in order to bring all the energy to the spectrometer slit. In space, or when using adaptive optics on the ground, the image size is limited by diffraction, and not by turbulence, so the problem disappears.

At first sight, grating spectrometers would not appear well suited to obtaining the spectra of extended objects (i.e., several arcsec or arcmin across, depending on the area $A _ { \mathrm { T } }$ of the telescope), if a high resolution, between $1 0 ^ { 4 }$ and $1 0 ^ { 6 }$ , is sought. Below we shall see how imaging spectroscopy has solved this problem in several different ways.

# Echelle Spectrometers

We have already described the underlying idea of the echelle spectrometer. It is important enough in astronomy to justify giving several examples.

High Resolution Spectrograph (HRS)

Figure 8.13 shows the arrangement of the high-resolution spectrograph (HRS) of the Hubble Space Telescope (since 1989), for which the spatial resolution in the image reaches the diffraction limit with $D = 2 . 4 ~ \mathrm { m }$ , while the spectral resolution can reach $1 0 ^ { 5 }$ .

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/7d206fc1533f85f24735235042cacfe26aa96b1a2ae0a4fbf099184bcbb11322.jpg)  
Fig. 8.13 Optical arrangement of the high resolution spectrograph (HRS) of the Hubble Space Telescope. The turret holds a set of six planar holographic gratings $\mathit { a \ } = 0 . 1 6$ to $3 . 1 6 ~  { \mu \mathrm { m } }$ ). In normal operation, the mirrors $C$ Dform the spectrum on detector 1 or 2 (linear Digicon arrays of 512 pixels), the mirrors $E$ are gratings giving the cross-dispersion for the echelle mode. Wavelengths are from 105 to $3 2 0 ~ \mathrm { n m }$ , and resolution from $R = 2 0 0 0$ to $1 0 ^ { 5 }$ . The useful spectral interval is $2 . 5 \mathrm { - } 2 9 ~ \mathrm { n m }$

# HARPS and the Search for Exoplanets

The Doppler shift of the spectral lines of a source such as a star or galaxy determines its radial velocity $\nu$ relative to the Earth. Every spectral line of the source is subject to the same relative shift:

$$
\frac { \Delta \lambda } { \lambda } = \frac { \nu } { c } ,
$$

and this means that the signal-to-noise ratio of a measurement of the velocity $\nu$ can be considerably improved by simultaneously measuring all the lines over a broad spectral range. This nevertheless requires the object to be bright enough to ensure that all the lines can be detected. Developed by the Geneva Observatory (Switzerland)and the Observatoire de Haute-Provence (France) to make systematic measurements of stellar motions in the Galaxy (CORAVEL and CORALIE) in the period 1980–2000), this technique has been widely used in the search for exoplanets associated with other stars, measuring the time dependence of their radial velocities with respect to the Earth. Indeed, the star orbits the common centre of mass of the system. In order to be able to detect planetary companions with the smallest possible masses (a few dozen times the Earth mass), the velocity sensitivity must clearly be as high as possible.

The High Accuracy Radial velocity Planet Searcher (HARPS)3 has been operating on the $3 . 6 \mathrm { ~ m ~ E S O }$ telescope at La Silla (Chile) since 2001. A significant part of the operating time of this telescope is devoted to a systematic search for exoplanets. This is an echelle spectrometer with spectral resolution reaching 90 000 in the broad spectral range from 380 to $6 9 0 ~ \mathrm { n m }$ . In order to maximise stability over time, the spectrometer is held in a fixed position, in a pressure-controlled container, with thermostatic control (Coude room), supplied by two optical fibres´ from the Cassegrain focus of the telescope, one carrying light from the star sampled in the focal plane, and the other light from a standard (thorium–argon) spectral lamp ensuring permanent wavelength calibration. These two sources are dispersed on two CCD arrays $2 0 0 0 \times 4 0 0 0$ pixels), in echelle mode, with 68 orders. The broad spectral interval here requires correction for atmospheric dispersion whenever the star is not at the zenith, and this is done by means of a correcting optical component placed upstream of the transfer fibre.

The HARPS instrument performs exceptionally well for the measurement of radial velocities (Fig. 8.14), and no doubt represents the ultimate limit of what is possible from an Earth-based observatory. The limiting velocity modulation that can be detected is $1 ~ \mathrm { m } \mathrm { s } ^ { - 1 }$ , while the presence of the planet Jupiter modulates the radial velocity of the Sun by about $1 3 ~ \mathrm { m s ^ { - 1 } }$ for an observer located outside the Solar System. Over five years, this instrument has already discovered or confirmed the existence of 12 exoplanets, and results are still coming in.

# Multi-Object Spectroscopy (MOS)

This is a multiplex arrangement, where the spectra of several objects in the field are obtained simultaneously, with a considerable gain in observing time and the possibility of common calibration. For a long time, objective prisms were used for stellar studies. A large prism placed on the entrance pupil, or an image of it, disperses each star image on the detector. There are two drawbacks: one is that the spectra may overlap, and the other is that the sky background adds to each spectrum. The selection of objects prior to dispersion is carried out by a suitable process for slicing up the image plane, viz., a slit mask or optical fibres. This delivers a spectrum $I _ { j } ( \lambda )$ for each object $j$ , although the latter must be small, i.e., no more than a few arcsec. Multi-object spectrometers (MOS) built in this way have extraordinarily high performance levels.

# Slit Masks

For image slicing using a mask, a non-dispersed image of the field is first made on the CCD detector. Then a mask is produced, containing a series of slits adequate for the desired resolution, on the basis of this image. This can be done by photoengraving, for example. The mask is inserted in the image focal plane, and a grism in the following pupil plane. Spectroscopy can then be carried out on a hundred or so sources simultaneously, e.g., with the CFH telescope (Fig. 8.15). The method is well suited to faint sources (galaxy surveys) in fields containing many sources, for example, several hundred sources in a field of 10 arcmin. Sky subtraction is good, so a magnitude limit of around $1 \%$ of the sky magnitude per spatial resolution element is possible (since the sky brightness is measured in square arcsec). There are two drawbacks with this solution: one is that it is not possible to obtain the spectrum of two objects close to one another in the direction of the dispersion, and the other is that the spectra of objects at the edge of the field are truncated at the two ends of the spectral region. Masking was chosen for the Visible Multi-Object Spectrograph (VIMOS) of the VLT.4

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/edc894a4083de5eb6861a5f9e492ecd935a8a6e1b5fbb851d871ee3a3062a325.jpg)  
Fig. 8.14 Performance of the HARPS spectrometer. The signal-to-noise ratio, depending on an exposure of 0.5 to $3 0 \mathrm { \ m i n }$ , is shown on the ordinate as a function of the magnitude $m _ { \mathrm { V } }$ of a star, here of spectral type G8. The horizontal line is the limiting detectable velocity of $1 \mathrm { m } \mathrm { s } ^ { - 1 }$ , below which measurements are no longer significant owing to various fluctuations, including fluctuations in the velocity field of the star’s photosphere. The saturation limit of the CCD due to excess photons is also shown. With the kind permission of the Geneva Observatory

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/d61bf2e267ffe7c37407642ee649f390ed8a5d35132222b8692c4af53ac499f0.jpg)  
Fig. 8.15 Multi-object spectroscopy using slits. One hour exposure with the Canada–France– Hawaii Telescope (CFHT) in a field of $1 0 ^ { \prime }$ . 80 masks were used. Each vertical rectangle corresponds to the sky $( \mathrm { s l i t } = 1 2 ^ { \prime \prime }$ ) plus source spectrum, covering 450 to $8 5 0 ~ \mathrm { n m }$ . Sky emission Dlines and bands (horizontal lines) predominate. The fainter objects $( m _ { \mathrm { I } } = 2 2$ , $m _ { \mathrm { B } } = 2 4$ ) are only D Dvisible after processing and recombining 8 exposures of 1 hour each. (Document due to LeFevre\` O., Canada–France Redshift Survey, 1995)

Optical Fibres

The idea here is straightforward. One end of each multimode fibre is positioned on the selected object in the focal plane, while the other is placed on the entrance slit of the spectrograph. The latter does not therefore need to be fixed to the telescope and move around with it, whence a gain in stability. Some fibres are reserved for measuring the sky background, others for field stars which may in some cases be used for finely tuned pointing. The detector pixels are thus exploited to their maximal potential by juxtaposing individual spectra (see Figs. 8.16 and 8.17).

The fibres can be placed in various ways, either by making holes at suitable positions in a plate and linking the fibres to them, or by displacing each fibre head using a robotic arm, commanded from positions selected on a previously made image of the field (Fig. 8.18). The density of sources accessible in the field is low, several hundred in a field of the order of one degree, because of the space required for the positioning arms. Sky subtraction is less good than for the slit technique, because in that approach the background is measured locally at the ends of the slit, whereas background measurement fibres must be positioned further from the sources. Small scale heterogeneity in atmospheric emission (Sect. 2.6) thus introduces fluctuations in the background and its spectra. The limiting magnitudes that can be reached lie between 17 and 21 at visible wavelengths.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/c02881aa8c6317fdb4e8b353202a67fd4c6eaccfd6c0fc54cbda74abdbd48b66.jpg)  
Fig. 8.16 Multi-object spectroscopy

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/a064d7bf86a0237f6360d5bcf36a135509c396cdbddd10b370d8e81d8e581d73.jpg)  
Fig. 8.17 Multi-object spectroscopy. Spectrograms of various regions in the Orion Nebula M42, showing lines characteristic of H II regions. The detector is a CCD. (After Enard D., $3 . 6 \mathrm { ~ m ~ }$ telescope at the European Southern Observatory)

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/d7195960cbab1a4b0db35706325fd098b5bba50e0fd593daa77333c673d36984.jpg)  
Fig. 8.18 Positioning of optical fibres in a field, using straight robot arms. 400 fibres are fitted to 400 sources, according to two different geometries. (After Lewis et al., in Fiber Optics in Astronomy II, ASP Conf. Ser. 37, 1993)

An interesting idea has been implemented in the GIRAFFE spectrometer set up on the Very Large Telescope in 2006. It combines the multi-object feature, selecting up to 132 galaxies in the field, with the wide-field feature, since each light-sampling head comprises 20 fibres which sample different points of the field. It is thus possible to obtain the spectrum of different regions of a galaxy, useful for making elemental abundance or rotation measurements, for example, and at the same time a large number of galaxies in a total field of 25 arcmin. It can also be combined with low order adaptive optics, guaranteeing a stable image quality, with a PSF of a few hundred milli arcsec.

In the mid-1990s, the slit spectrometer of the $4 . 2 \textrm { m }$ Anglo-Australian Telescope (AAT) (Mount Stromlo, Australia) can position 400 fibres, connected to two spectrographs, in just 2 minutes. The Sloan Digital Survey (see Sect. 10.2) is preparing the spectrometry of all $1 0 ^ { 6 }$ galaxies and $1 0 ^ { 5 }$ quasars in a $\pi$ steradian fraction of the sky. The instrument, which will use 3 000 photographic plates with holes pierced in them for manual installation of the fibres, and has a field of $3 ^ { \circ }$ and 600 fibres. It can reach magnitude $m _ { \mathrm { v } } = 1 7$ .

# Integral Field Spectroscopy

The aim here is to measure the spectral information $I ( \nu , \pmb \theta )$ at every point of the field, rather than at a limited number of previously selected points, as happens in multi-object spectroscopy. This approach is not only relevant to grating spectrometers. Later we shall encounter further illustrations with the Fabry–Perot ´ spectrometer and the Fourier transform imaging spectrometer. A typical setup couples a dispersing element with a microlens array or a long slit (for studying the Sun).

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/c171a949f200a2a93c0f741e9723b15b702733f57d4871f01d66215326bfb53b.jpg)  
Fig. 8.19 Integral field spectrometer with microlens array. Each microlens, placed in a focal plane, slices the field up into elements whose spectrum is then given by a grism. The dispersion angle must be chosen judiciously so that the spectra do not overlap

Microlens Array Spectrometer

An array of microlenses, typically a few hundred micrometres across, is placed in an image plane conjugate to the focal plane with suitable magnification. This forms a set of images of each pixel of the field thereby sampled. These images are dispersed by a grism (transmission grating) and the spectra are detected on a CCD (Fig. 8.19).

There are alternatives to using microlenses to slice up and reconfigure the focal plane. A remarkable example is the SINFONI instrument, set up on the Very Large Telescope in 2004. This operates in00 00 00 00 the near infrared $( 1 . 1 - 2 . 4 5 ~ { \mu \mathrm { m } } )$ ) and can be coupled with adaptive optics.5 It is designed to work at the diffraction limit of an ${ 8 \mathrm { m } }$ telescope so each pixel is necessarily small, and the total field can be anything from $8 ^ { \prime \prime } \times 8 ^ { \prime \prime }$ to $0 . 8 ^ { \prime \prime } \times 0 . 8 ^ { \prime \prime }$ , depending on the available configuration. This field is  divided into 32 slices (image slicing), each of which is then dispersed onto 64 pixels of a HgCdTe detector (see Chap. 7). We thereby obtain $3 2 \times 6 4 = 2 0 4 8$ spectra of the given sky region. The  Dassociated adaptive optics module can use either a natural guide star (NGS), or an artificial guide star generated by laser (LGS) in the upper atmosphere (see Chap. 6), whence it is possible to observe in a sky region without bright reference star.

This idea of slicing up and reconfiguring the field can also be used at submillimetre wavelengths. In the Photodetector Array Camera and Spectrometer (PACS), designed for the Herschel space observatory,6 a field of $5 \times 5$ pixels, each one $9 . 4 ^ { \prime \prime }$ , is sliced and dispersed to form 16 spectral elements on a $1 6 \times 2 5$ array of individual detectors (Ge:Ga, see Sect. 7.4) in the submillimetre bands $5 7 \mathrm { - } 1 0 5 ~ \mu \mathrm { m }$  and $1 0 5 { - } 2 1 0 ~ { \mu \mathrm { m } }$ .

# Solar Spectroscopy

The aim is to obtain a monochromatic image of an extended object, in this case the surface of the Sun, using the high spectral resolution of a grating spectrograph. Replacing the exit slit by a one-dimensional detector (for example, a Reticon or CCD array, which usually has 512 pixels, see Sect. 7.4.5), a slice of the object is obtained at wavelength $\lambda _ { 0 }$ . Displacing the image of the Sun on the entrance slit by an amount equal to the slit width, a second such slice is obtained, and so on. The image of the object at wavelength $\lambda _ { 0 }$ , known as a spectroheliogram, is thus reconstructed (Figs. 8.20 and 8.21).

The magnetograph combines the imaging capacity of the spectroheliograph with analysis of the polarisation. In a chosen spectral line, the Zeeman effect is measured at each point of the image. These measurements can be used to deduce the component of the magnetic field along the line of sight, for the layer of the atmosphere in which the line is formed.

# 8.3.4 Fourier Transform Spectrometer

# Principles and Properties

The Fourier Transform Spectrometer (FTS), also called the Michelson interferometer, is a two-wave interferometer, as opposed to the grating, which causes $N$ waves to interfere (one from each groove of the grating). We shall not employ the term Michelson interferometer here, although it is common, to avoid confusion with the spatial Michelson interferometer used in imaging and described in Sect. 6.4.

![](../chunks/Observational Astrophysics Lena_part_0007_pages_0421-0490/auto/images/7e34787c1967c0a4ba7b7aced33130d7b913c34e16ee859a584f04f13bda0434.jpg)  
Fig. 8.20 Principle of the spectroheliograph. (a) The image of the Sun is scanned by the entrance slit, and the exit slit selects the wavelength $\lambda _ { 0 }$ on a detector array. (b) Monochromatic image at wavelength $\lambda _ { 0 }$


<!-- chunk 0008: pages 491-560 -->
![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/fe116a9ce0d307dcae5a3031e6c4b4ad9d0f52f06ec0c7e4cd95916720eee261.jpg)  
Fig. 8.21 Solar spectroheliogram obtained in the H˛ line. Image courtesy of Henoux J.-C., Observatoire de Paris Meudon, 1985

If $x$ is the difference in the path length (Fig. 8.22) of the two waves, the exit intensity is given by

$$
\tilde { I } ( x ) = \frac { I _ { 0 } } { 2 } ( 1 + \cos 2 \pi \sigma x ) ,
$$

for monochromatic incident intensity $I _ { 0 }$ of wave number $\sigma$ . An arbitrary source whose intensity has a spectral distribution $I _ { 0 } ( \sigma )$ limited to the range $[ \sigma _ { 1 } , \sigma _ { 2 } ]$ , produces the signal

$$
\tilde { I } ( x ) = \frac { 1 } { 2 } \int _ { \sigma _ { 1 } } ^ { \sigma _ { 2 } } I _ { 0 } ( \sigma ) ( 1 + \cos 2 \pi \sigma x ) \mathrm { d } \sigma .
$$

This signal, referred to as an interferogram, is measured by the detector placed at the exit. Up to a constant, it is the Fourier cosine transform of the spectrum of the object. This is spectral multiplexing since, for each value of $x$ , all the spectral elements of the incident spectrum contribute to the signal, each one being coded by a cosine function orthogonal to the others.

Recovering the Source Spectrum

$I _ { 0 } ( \sigma )$ can be recovered by inverse Fourier transformation. After subtracting the mean value

$$
\langle \tilde { I } ( x ) \rangle = \frac { 1 } { 2 } \int _ { \sigma _ { 1 } } ^ { \sigma _ { 2 } } I _ { 0 } ( \sigma ) \mathrm { d } \sigma ,
$$

we obtain

$$
I _ { 0 } ^ { \prime } ( \sigma ) = \mathrm { F T } \left[ \tilde { I } ( x ) - \langle \tilde { I } ( x ) \rangle \right] .
$$

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/d5a2db1fa30dd63f41efaf3d5f983d3b0e22129a81e7687a448ed4fa804bc453.jpg)  
Fig. 8.22 Optics of a Fourier transform spectrometer

If $\tilde { I } ( x )$ were known over the whole interval $x ~ \in ~ ( - \infty , + \infty )$ , $I _ { 0 } ^ { \prime }$ would equal $I _ { 0 }$ . When $\tilde { I } ( x )$ is only known on an interval $[ - x _ { \mathrm { m } } / 2 , + x _ { \mathrm { m } } / 2 ]$ , it can be shown (Problem 8.1) that

$$
I _ { 0 } ^ { \prime } ( \sigma ) = I _ { 0 } ( \sigma ) \star \mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) ,
$$

and the recovered spectrum differs from $I _ { 0 }$ by a degradation in resolution due to this convolution.

Resolution

The interferogram of a monochromatic source $I _ { 0 } ( \sigma ) = \delta ( \sigma - \sigma _ { 0 } )$ is the instrumental profile

$$
\mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) \star \delta ( \sigma - \sigma _ { 0 } ) ,
$$

where $x _ { \mathrm { m } }$ is the maximum optical path length difference. The first zero of the instrumental profile occurs at

$$
\sigma - \sigma _ { 0 } = \pm \frac { 1 } { x _ { \mathrm { m } } } ,
$$

and it is assumed that this value gives the separation at which it is just possible to discriminate between two lines. The resolution is therefore

$$
R = { \frac { \sigma _ { 0 } } { \Delta \sigma } } = x _ { \mathrm { m } } \sigma _ { 0 } .
$$

When high resolutions are sought, the size of the interferometer is determined by the displacement amplitude (equal to $x _ { \mathrm { m } } / 2$ ) of a moveable mirror. This size is therefore $\lambda R / 2$ , and comparable to the size of a grating spectrometer with the same resolution. In a typical application, $\lambda ~ = ~ 0 . 5 ~ { \mu \mathrm { m } }$ , $x _ { \mathrm { m } } ~ = ~ 2 ~ \mathrm { m }$ , and $R = x _ { \mathrm { m } } / \lambda = 4 \times 1 0 ^ { 6 }$ .

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/136741821b8753be724fdc96999617ecfbc1a66fc1a743be64d61f374c971c3f.jpg)  
Fig. 8.23 Field of the interferometer. The area $S$ and the angle $i _ { \mathrm { m } }$ define the beam etendue.´ $S$ is the area of the beam at the lens $L _ { 1 }$ shown in the previous figure

D D It can be shown (Problem 8.2) that the optimum sampling rate for the interferogram is an increment $\Delta x \ : = \ : 1 / 2 \sigma _ { \mathrm { m } }$ , where $\sigma _ { \mathrm { m } }$ is the maximum wave number Dcontained in the source spectrum. A finite number of samples of $\tilde { I } _ { 0 } ( x )$ is thus Qobtained, and a numerical Fourier transform can easily be carried out on them. Note, furthermore, that it is possible to control the sampling by using the interference pattern $\tilde { I } _ { 1 } ( x )$ given by a reference laser whose wave number is precisely known. The wavelength scale of the spectrum $I _ { 0 } ( \sigma _ { \mathrm { m } } )$ is then determined with the same precision, a considerable advantage over the grating spectrometer, which must be calibrated using reference spectra.7

Throughput. The aim here is to establish the maximal beam etendue, beyond which the resolution ´ would be degraded (determination of the $Q$ factor). Referring to Fig. 8.23, let

$$
\Omega _ { \mathrm { m a x } } = \pi i _ { \mathrm { m } } ^ { 2 } .
$$

Those rays inclined at an angle $i$ to the axis contribute

$$
\mathrm { d } \Omega = 2 \pi i \mathrm { d } i
$$

to the solid angle, and the associated variation in path difference is

$$
| \mathrm { d } x | = x ( 0 ) i \mathrm { d } i , \quad \mathrm { u s i n g } \quad x ( i ) = x ( 0 ) \left( 1 - \frac { i ^ { 2 } } { 2 } \right) ,
$$

so that

$$
\mathrm { d } \Omega = \frac { 2 \pi } { x ( 0 ) } \mathrm { d } x .
$$

The power delivered by a source of uniform brightness is thus

$$
\mathrm { d } \phi = S \frac { 2 \pi } { x ( 0 ) } \mathrm { d } x ( i ) \mathcal { C } [ x ( i ) ] ,
$$

where the factor $\mathcal { C }$ expresses the modulation due to the interference of the two waves. For a monochromatic source of unit brightness, the modulated part of the flux $\tilde { I } ( x ) - \langle \tilde { I } ( x ) \rangle$ can be written

$$
\phi [ x ( 0 ) ] = S \frac { 2 \pi } { x ( 0 ) } \int _ { 0 } ^ { \infty } { \cal D } [ x ( i ) ] \cos [ 2 \pi \sigma _ { 0 } x ( i ) ] \mathrm { d } x ( i ) ,
$$

where $D$ is a ‘diaphragm’ function, giving a first approximation to $\mathcal { C }$ :

$$
D = \left\{ { 1 , \quad x ( 0 ) \leq x ( i ) \leq \left( { 1 - \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } } \right) x ( 0 ) , } \right.
$$

It follows that

$$
\begin{array} { l } { { \phi [ x ( 0 ) ] = \displaystyle \frac { 2 \pi S } { x ( 0 ) } \frac { 1 } { 2 } \mathrm { F T } \big [ D [ x ( i ) ] \big ] } } \\ { { \qquad = \displaystyle \frac { \pi S } { x ( 0 ) } \mathrm { s i n c } \left[ \pi \sigma _ { 0 } x ( 0 ) \frac { i _ { \mathrm m } ^ { 2 } } { 2 } \right] \cos 2 \pi \sigma _ { 0 } \left( 1 - \frac { i _ { \mathrm m } ^ { 2 } } { 4 } \right) x ( 0 ) , } } \end{array}
$$

or simply

$$
\phi ( x ) = \frac { \pi S } { x } \operatorname { s i n c } \left( \pi \sigma _ { 0 } x \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } \right) \cos 2 \pi \sigma _ { 0 } x .
$$

The modulation term cos $2 \pi \sigma _ { 0 } x$ is therefore subject to a damping effect which tends to remove the modulation, either for large path differences at given $i _ { \mathrm { m } }$ , or for large fields $i _ { \mathrm { m } }$ at given $x _ { \mathrm { m } }$ .

The modulation is zero for

$$
\pi \sigma _ { 0 } x \frac { i _ { \mathrm { m } } ^ { 2 } } { 2 } = k \pi , \mathrm { i . e . , } x = k \frac { 2 \pi \lambda _ { 0 } } { \Omega } .
$$

The resolution is $R = x _ { \mathrm { m } } / \lambda$ , so the beam etendue is´

$$
U = S \Omega = 2 \pi \frac { S } { R } , \mathrm { i . e . , } Q = 2 \pi .
$$

This result reveals the throughput advantage of the Fourier transform spectrometer: at a resolution equal to that of a grating spectrometer, the throughput is increased by the factor

$$
\frac { 2 \pi } { \beta } \sim 1 0 ^ { 2 } \mathrm { t o } 1 0 ^ { 3 } .
$$

This greatly facilitates the observation of extended sources (that is, sources whose angular dimensions were incompatible with the slit width of the grating spectrometer). Note that this advantage is clearly related to the axisymmetry of this interference arrangement, possessed also by the Fabry–Perot spectrometer. ´

The Holographic Fourier Spectrometer. The moveable mirror is one of the less convenient aspects of the above setup. It has been suggested that one (or both) of the mirrors could be replaced by a grating, tilted in such a way that it acts as a plane mirror for some wavelength $\lambda _ { 0 }$ (Littrow reflection of the grating). Neighbouring wavelengths $\lambda$ are reflected at different angles, and each one of them produces straight-line interference fringes, like the ones produced by an air wedge, on the two-dimensional detector. The amplitude is proportional to the intensity $I ( \lambda )$ and Fourier analysis of the signal restores $I ( \lambda )$ . The name comes from the fact that the frequency $\nu _ { 0 }$ is reduced to zero (uniform flux at the detector) and so produces a holographic effect. (Douglas N. et al., Astroph. Sp. Sci. 171, 307, 1980.)

# The Multiplex Advantage

A simple argument readily establishes the principle here, due to Felgett. Suppose we wish to determine, over a total measurement time $T$ , the spectrum $I _ { 0 } ( \sigma )$ of a source, in the interval $( \sigma _ { 1 } , \sigma _ { 2 } )$ , and with resolution $R$ . The number of spectral elements is $M$ . Suppose that the intensity is comparable in each spectral element (absorption or continuum spectrum, the argument requiring modification in the case of a spectrum comprising a small number of emission lines). Suppose, finally, that the measurement is made by a detector whose intrinsic noise $\sigma _ { \mathrm { D } }$ dominates the other sources. For sequential scanning of the spectrum, the signal-to-noise ratio for each spectral element is

$$
r _ { 1 } = { \frac { I _ { 0 } ( \sigma ) \left( T / M \right) } { \sigma _ { \mathrm { D } } \sqrt { T / M } } } .
$$

For FT spectroscopy, the whole time $T$ is used for each spectral element, and the corresponding ratio is

$$
r _ { 2 } = \frac { 1 } { 2 } \frac { I _ { 0 } ( \sigma ) T } { \sigma _ { \mathrm { D } } \sqrt { T } } ,
$$

the factor $1 / 2$ coming from the light lost at the beam splitter. The multiplex gain is thus $\sqrt { M } / 2$ , and can be very large for extended spectra at very high resolution (Fig. 8.24). Historically, this gain made the FT spectrometer the optimal instrument for infrared observation, in which detector noise dominates, and for which, until the 1990s, no multichannel detectors were available to avoid sequential scanning.

Even though this advantage is now disappearing, with the progress made in detector technology, FT spectroscopy maintains its lead in throughput, in very high resolution (of the order of $1 0 ^ { 5 }$ ), and in rigorous wavelength calibration.

It is worth pointing out that the spectroscopic capacities of the FT spectrometer can be combined with imaging, by placing an array of detectors in the focal plane. The difficulties of data handling, whether related to the storage of measurement data or the calculation of spectra (Problem 8.3), are daunting.

# Astronomical Applications

The FT spectrometer was widely used in the near infrared over the period 1960– 2000, but progress in the sensitivity of 2D detectors has gradually eliminated it from ground-based observation. However, it is still used in space because of its high level of accuracy, compactness, and multiplex facilities.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/7a50c3f7ee3f694317d1528a2bcc0336103b2df7c1529bbb7c4f77a620814715.jpg)  
Fig. 8.24 Progress in resolving the infrared spectrum of Venus, during the historical emergence of Fourier spectroscopy. (a) Grating spectrometer in the atmospheric window around $1 . 6 ~ { \mu \mathrm { m } }$ . Four intense rotational–vibrational bands of the $\mathrm { C O } _ { 2 }$ molecule are visible. (b) Fourier transform spectroscopy with $\Delta \sigma = 0 . 7 \mathrm { c m } ^ { - 1 }$ . (c) The same, with $\Delta \sigma = 0 . 0 8 ~ \mathrm { c m } ^ { - 1 }$ . The $\mathrm { C O } _ { 2 }$ bands are D Dresolved. The apertures of the telescopes used are given. From Connes P., ARAA 8, 209, 1970. Reproduced with the kind permission of the Annual Review of Astronomy and Astrophysics, Vol. 8, $\textcircled { \scriptsize { \mathrm { c } } } 1 9 7 0$ , Annual Reviews Inc

# Ground-Based Applications

In the infrared region observable from the ground, a background of thermal or OH emission is the predominant noise for $\lambda ~ \gtrsim ~ 1 . 5 ~ { \mu \mathrm { m } }$ , thanks to progress in detector technology. The multiplex advantage then disappears (Problem 8.4), but the throughput advantage remains, when the observed infrared sources are extended ${ \gg } 1$ arcsec). Moreover, as the wavelength is long, the need for mechanical precision is less restrictive, and the FTS is relatively easy to build. For this reason, they now equip several large telescopes (Fig. 8.25). When coupled to an array, it then operates as an integral field spectrometer (the BEAR instrument of the CFH telescope in Hawaii, Fig. 8.26).

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/7aa2145ef67c0ed0bd5014852cf592244cf424395b885be4e73a1a7f654a77ae.jpg)  
Fig. 8.25 Fourier transform spectrometer, Canada–France–Hawaii Telescope. The instrument is symmetrical, with signals, $I _ { 1 } ( x )$ and $I _ { 2 } ( x )$ , received at the two infrared detectors. The quantity $( I _ { 1 } - I _ { 2 } ) / ( I _ { 1 } + I _ { 2 } )$ is independent of atmospheric fluctuations. The beam from the visible He–  CNe laser provides reference fringes which control the sampling of the infrared signal. Upper and lower beams are spatially separated. The whole setup is mounted at the Cassegrain focus of the telescope. (After Maillard J.P., Michel G., I.A.U. Colloquium, 67, Reidel, Dordrecht, 1982. With the kind permission of D. Reidel Publishing Company)

# Spaceborne Applications

A nice example here is the ESA’s Herschel mission,8 observing the sky in the far infrared and submillimetre regions from Lagrange point L2 using a cooled $3 . 5 \mathrm { ~ m ~ }$ telescope from 2008. The Spectral and Photometric Imaging Receiver (SPIRE) is a Fourier transform integral field spectrometer (2:6 ), operating simultaneously in the two bands $2 0 0 { - } 3 0 0 ~ { \mu \mathrm { m } }$ and $3 0 0 { - } 6 7 0 ~ { \mu \mathrm { m } }$ , with spectral resolution as high as 1 000.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/4c183e5f2581511a559c96409928cf9e77b649f22396c416af91d673fbb1c73b.jpg)  
Fig. 8.26 Integral field spectroscopy. High spatial and spectral resolution image of helium streamers, obtained with the Fourier spectrometer BEAR on the CFHT (Hawaii) in the HI Brackett $\gamma$ line at $\lambda = 2 . 0 5 8 ~ \mu \mathrm { m }$ , from the minispiral located in the immediate vicinity of the galactic Dcentre. Stellar contributions have been subtracted. The position of $\mathrm { S g r A } ^ { * }$ is marked by $^ +$ . The color coding of velocity is explicit in the insert, where it clearly appears that the spectral line in this particular pixel shows several radial velocities, proving the presence of several clouds with different velocities along the line of sight. Paumard, T. et al., 2001, courtesy of Astronomy & Astrophysics

# 8.3.5 The Fabry–Perot Spectrometer

This spectrometer (or interferometer) combines the throughput advantage of the FT spectrometer $Q = 2 \pi$ ) with a very high spectral resolution, whilst at the same time Dbeing far less bulky than the two previous instruments for the same resolution.9

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/58eaca5423d19d4d9c8610fba52dd32817a41dae4dab7fe366ddd47779fe5f7f.jpg)  
Fig. 8.27 Arrangement of the Fabry–Perot interferometer. (a) In the UV, visible, and near infrared, the plates are made of transparent material. (b) In the far infrared, the plates are self-supporting metallic grids

Principle

Two parallel plates, supposed non-absorbent, have a high reflection coefficient $r$ $( r ~ \lesssim ~ 1 )$ , and transmission $t = 1 - r$ (Fig. 8.27). This is called the Fabry–Perot D etalon (or FP etalon), and is so named because it allows a wavelength calibration by physical measurement of the distance between the plates, or conversely. Neglecting reflection by the faces $R _ { 0 }$ and $R _ { 0 } ^ { \prime }$ , the transmission of the FP etalon, illuminated by monochromatic radiation of wave number $\sigma$ at incidence angle $i$ , results from multiple wave interference and can be expressed by Airy’s formula

$$
I = I _ { 0 } \left( \frac { r } { 1 - r } \right) ^ { 2 } \left[ 1 + \frac { 4 r } { ( 1 - r ) ^ { 2 } } \sin ^ { 2 } ( 2 \pi e \sigma \cos i ) \right] ^ { - 1 } .
$$

At zero incidence, the FP etalon has transmission peaks when

$$
2 \pi e \sigma = m \pi , \quad m { \mathrm { ~ a n ~ i n t e g e r } } ,
$$

which means

$$
\sigma = { \frac { m } { 2 e } } , \quad m { \mathrm { ~ a n ~ i n t e g e r . } }
$$

These peaks are therefore more widely separated as the thickness $e$ is increased. The whole number $m$ is called the order of the interferometer, and $\Delta \sigma = 1 / 2 e$ is the free spectral interval.

At zero incidence, the full width at half maximum $\delta \sigma$ of a transmission peak is given by $I = I _ { 0 } / 2$ , which implies

$$
\sin \left[ 2 \pi e \left( \sigma + \frac { 8 \sigma } { 2 } \right) \right] \sim \pi e 8 \sigma = \frac { 1 - r } { 2 \sqrt { r } } .
$$

This width decreases as the reflection coefficient $r$ increases. Introducing the finesse of the FP by

$$
\mathcal { F } = \frac { \pi \sqrt { r } } { 1 - r } ,
$$

it follows that

$$
\delta \sigma = \frac { 1 } { 2 e \mathcal { F } } .
$$

The resolution is then given by

$$
R = \frac { \sigma } { 8 \sigma } = 2 e \mathcal { F } \sigma = m \mathcal { F } .
$$

This increases with both the finesse and the order.

As the FP has rotational symmetry about its axis, the interference pattern at infinity, when it is illuminated by monochromatic radiation of wave number $\sigma _ { 0 }$ , is a set of concentric rings. Let $\ S i$ be their angular size at half maximum. Then the ring maximum is given by

$$
\cos i = { \frac { m \pi } { 2 \pi e \sigma _ { 0 } } } ,
$$

and the width $\ S i$ is found by solving

$$
{ \frac { 4 r } { ( 1 - r ) ^ { 2 } } } \sin ^ { 2 } \left[ 2 \pi e \sigma _ { 0 } \cos \left( i + { \frac { 8 i } { 2 } } \right) \right] = 1 .
$$

A lens or mirror placed behind the FP forms an image of these rings in its focal plane. The maximum throughput for an FP without loss of resolution follows from an identical calculation to the one carried out above in the case of the FT spectrometer. Once again, if $S$ is the area of the etalon, the result is

$$
U = 2 \pi { \frac { S } { R } } .
$$

Use as a Spectrometer

The FP etalon can be used in different ways (Fig. 8.28). In any arrangement, it must be preceded by a predisperser (another etalon, interference filter, grating, or other), in order to isolate a single free spectral interval $\Delta \sigma$ on the FP.

In a scanning mode, and illuminated by arbitrary monochromatic radiation of spectrum $I _ { 0 } ( \sigma )$ , the FP is followed by a diaphragm isolating the central ring, which is received on the detector. The thickness $e$ is then varied, and the detector signal is proportional to the incident intensity $I _ { 0 } ( \sigma )$ . It is also possible to vary the pressure, and hence the refractive index, of a gas introduced between the plates.

# 8.3.6 The Bragg Crystal Spectrometer (X-Ray Region)

The first extragalactic spectral line observed in the X-ray region was the $2 p { - } 1 s$ line of iron XXIV, in the Virgo, Coma, and Perseus clusters of galaxies by NASA’s OSO-8 satellite. This observation (Fig. 8.29) used the low resolving power of the proportional counter, but demonstrated the potential of X-ray spectroscopy. Developments continued using crystals to produce diffraction, but in the 1980s, these were gradually replaced by conventional diffraction gratings with very close rulings (600 grooves/mm), first by transmission (the European EXOSAT mission), then by reflection (the European mission XMM–Newton, 1999), thereby covering the energy range $0 . 1 { - } 2 \ \mathrm { k e V } .$ In NASA’s Chandra X-ray observatory launched in 1999, the slitless high resolution spectrometer or High Energy Transmission Grating spectrometer $\mathrm { ( H E T G ) ^ { 1 0 } }$ uses a transmission grating formed by depositing gold microrods on a plastic substrate. Whether the disperser is a crystal or a grating, the X-ray spectrometer also includes a camera on which the dispersed image is formed (Sect. 7.4.6).

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/cab9f116309f0c4b208b8357b67a2cf1775a318ec0360df7c2d6eba6fa9a3295.jpg)  
Fig. 8.28 Interferograms of the galaxy NGC 2903, obtained using a scanning Fabry–Perot interferometer in the $\mathrm { H } \alpha$ line $( 6 5 6 . 3 ~ \mathrm { n m } )$ . The variation in order is obtained using piezoelectric wedges, and the free spectral interval is scanned in 24 steps (of which 12 are shown on the figure). Each photon is recorded on a $5 1 2 \times 5 1 2$ matrix by a photon counting camera. The number of photons measured is proportional to the intensity emitted at a given Doppler speed. The radial velocity of hydrogen in the galaxy is thus mapped. The integration time per step was $5 \ \mathrm { m i n }$ . (Observatoire de Marseille, $3 . 6 \mathrm { ~ m ~ C F H }$ telescope, Hawaii, Marcelin M. et al., Astron. Ap. 128, 140, 1983. With the kind permission of Astronomy and Astrophysics)

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/4bd07e40ee836c9744727bc38e8a821cc4335e6ab50478b1735c0e7736953265.jpg)  
Fig. 8.29 X-ray emission from the Virgo, Perseus and Coma clusters of galaxies. The spectral resolution, obtained by a proportional counter, is less than 10, but nevertheless sufficient to show an iron line at $7 \mathrm { k e V . }$ From Serlemitsos P.J. et al., Ap. J. 211, L63, 1977. With the kind permission of the Astrophysical Journal

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/98b6b8e43e8737564d2df974a104b5c6ac2f7929449f27a5d8b0b31b45ebb165.jpg)  
Fig. 8.30 Bragg diffraction. (a) Lattice plane of the crystal, with period $d$ . (b) Concave crystal forming the pseudo-images of a source at infinity

A high resolving power $R \sim 1 0 0 0 )$ can be obtained by means of a crystal, such as lithium fluoride LiF, which functions as a diffraction grating. Bragg diffraction occurs on a crystal of spacing $d$ (Fig. 8.30a), at an angle $\theta$ given by

$$
\sin \theta = { \frac { \lambda } { 2 a } } .
$$

Just as a Rowland mounting (Fig. 8.11) forms an image with a concave grating, a curved crystal produces a series of quasi-anastigmatic monochromatic images from a point source at infinity (Fig. 8.30b). If the crystal surface is part of a spherical surface of centre $C$ , the lattice planes being tangent to the sphere, dispersion is along the $z$ axis and the distance $C I$ to the image $I$ of radiation with wavelength $\lambda$ is given by

$$
C I = { \frac { r } { 2 \sin \theta } } .
$$

The resolution $R$ at which an energy interval $\mathrm { d } E$ can be separated is given by

$$
R = { \frac { E } { \mathrm { d } E } } = { \frac { \lambda } { \mathrm { d } \lambda } } = { \frac { r } { 2 \sin \theta \mathrm { d } z } } .
$$

The spacing of the LiF crystal is $2 . 0 1 \mathrm { ~ \AA ~ }$ , giving $\theta \ : = \ : 2 5 ^ { \circ }$ for an energy $E = 7 . 3 ~ \mathrm { k e V } .$ The resolution $R = 1 0 0 0$ corresponds to $\mathrm { d } z = 1$ Dmm for $r = 1 \textrm { m }$ D. A proportional counter is thus placed on the $z$ axis, to measure both the $z$ D Dcoordinate, and hence the energy, of the photon, as well as the corresponding intensity. The spatial resolution of the proportional counter may indeed limit the spectral resolution of the instrument. As the system is not perfectly anastigmatic for a point source at infinity, extended objects give a series of pseudo-images at different $z$ .

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/0b468e33f1a4b5a3a21ef0c261b92ecbbcb58e6b46a00dfbf16b3f8712b4d2e5.jpg)  
Fig. 8.31 Spectrum of the supernova remnant (SNR) Puppis A, observed with the curved grating spectrometer on the Einstein satellite. Lines due to various ions are identified. Note the profile of the rays, due to the limited resolution of the spectrometer. From Winkler P.F. et al., Ap. J. 246, L27, 1981. With the kind permission of the Astrophysical Journal

Note that such a spectrometer is sensitive to polarisation, since only the component of the electric field parallel to the crystal surface is reflected at the Bragg angle. Between 1978 and 1981, the Einstein satellite (High Energy Astronomical Observatory 2) was equipped with such a spectrometer, and provided a resolution of 50 to $1 0 0 ~ \mathrm { u p }$ to $0 . 4 \mathrm { \ k e V } ,$ , and 100 to 1 000 beyond (Fig. 8.31). Figure 8.32 shows a spectrum obtained 20 years later with the RGS instrument aboard the European XMM–Newton mission.

Finally, note that, as in other wavelength regions, a certain spectral selectivity can be introduced by the detector itself (Sect. 7.4.6), whence no further dispersive system is required.

# 8.4 Radiofrequency Spectrometry

Interference spectrometers use the spectral selectivity which results from interference of a wave with itself. Heterodyne spectrometers achieve this selectivity by interfering the incoming wave with a locally produced wave, and analysing the result in a set of electric filters, or by other methods outlined below. These methods cover the conventional radiofrequency region, from long wavelengths (centimetre to hectometre) down to the shortest, in the millimetre and submillimetre region which we first began to seriously explore at the beginning of the 2000s.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/cbf9cb9027803efb9220c63ceab2dea37071886f00d68d32d786851d4a53687f.jpg)  
Fig. 8.32 Spectrum obtained with the reflection grating spectrometer (RGS) of the Newton mission. Spectrum of the young, active star AB Doradus between 2 and $0 . 3 \mathrm { k e V } .$ There are many ionised iron, magnesium, and neon lines. Image courtesy of J. Sanz-Forcada ESA XMM–Newton mission

The idea of heterodyne detection, from radiofrequencies to mid-infrared, was discussed in detail in Sect. 7.5. It involves a local oscillator (LO) with frequency very close to that of the incident radiation. The frequency change by heterodyning transfers the information carried by the incident wave to a lower frequency region called the intermediate frequency (IF), and this is where spectral analysis and final detection can be carried out. The detector remains limited to a coherence etendue´ $\lambda ^ { 2 }$ and one polarisation direction, but detectors can be juxtaposed to form small arrays $3 \times 3$ or $4 \times 4$ ), thereby speeding up image reception efficiency. Single wavelength  maps are produced either in the spatial frequency plane $w$ or in the image plane $\pmb \theta$ by combining spectral discrimination, the image formation properties discussed in Chaps. 5 and 6, and detector properties discussed in Chap. 7.

# 8.4.1 Spectral Discrimination Methods

Spectral discrimination on the intermediate frequency (IF) signal can be achieved in several ways, which we shall discuss in detail here:

• Using electrical filters connected in parallel and identifying each spectral band. • Using acousto-optical techniques forming a diffraction grating. By purely digital processing of the signal, either by digital correlator or by fast Fourier transform.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/622182e801b470da66804921e98adf2921cdbbf8bf46ab3604cbb8aa4749907d.jpg)  
Fig. 8.33 Typical lines in the radio region 4.5 to $5 \ \mathrm { G H z }$ . (a) Molecular lines of formaldehyde $\mathrm { H } _ { 2 } \mathrm { C O }$ , and formamide $\mathrm { H } _ { 2 } \mathrm { C O N H }$ , and fine structure lines of the OH radical. (b) Recombination lines of hydrogen and helium, $\alpha$ and $\beta$ transition series. Values of the quantum number $n$ are given. A list of transitions and their frequencies is given in AQ, Sects. 2.12, 2.14

Any method will do, whatever the spectral region from submillimetre to metre wavelengths, since they all apply to the IF signal, and not directly to the incident signal. Only the mixing stage can differ here.

Considering the regions from $\lambda = 1 0 0 \mu \mathrm { m }$ $\langle \nu = 3 \mathrm { T H z } \rangle$ to $\lambda = 1 0 \mathrm { c m }$ $( \nu = 3 \mathrm { G H z }$ ), one seeks D D D Dpassbands for the IF stage able to exceed 1 GHz. What is the desired resolution? When a gas has thermal agitation speeds of the order of several $\mathrm { k m ~ s ^ { - 1 } }$ , an emission or absorption line (Fig. 8.33) will have relative width $\Delta \nu / \nu \sim 1 0 ^ { - 5 }$ , implying $\Delta \nu = 1 4 ~ \mathrm { k H z }$ at $\lambda = 2 1 ~ \mathrm { c m }$ , or $1 . 5 ~ \mathrm { M H z }$ at $\lambda = 2 0 0 ~ \mu \mathrm { m }$  D D. There is little point in pushing the spectral resolution to values much above $1 0 ^ { 5 } -$ $1 0 ^ { 6 }$ D, since for one thing the spectral lines are broader, and for another, a very high level of stability would have to be guaranteed for the local oscillator.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/3357a00e6fe6459b47f7a519337e598f2572dd129e6cce1ab1787117ea328456.jpg)  
Fig. 8.34 Set of filters in parallel, and the resulting transfer function. The intermediate frequency signal from the mixer is amplified, then distributed through a series of electrical filters arranged in parallel, each one discriminating a spectral band $B$ and thereby fixing the spectral resolution

# Multichannel Filter Spectrometers

In the second half of the twentieth century, radioastronomy developed on the basis of this method of spectral discrimination, which is now tending to disappear (2007).

Consider the signal at intermediate frequency (IF) leaving the mixer (Fig. 8.34). A set of filters, with transfer functions $H _ { i } ( \nu )$ and passband $B$ , slice the frequency band $\Delta \nu$ into $\begin{array} { r } {  { \boldsymbol { N } } } { \ = \ \Delta  { \boldsymbol \nu } / B }  \end{array}$ channels, over which the IF signal is distributed Din parallel. Each filter is followed by a quadratic detector, then a commutator, which compares the signal with a reference signal (local calibration source, see Sect. 3.4). A linear integrator (e.g., low-pass filter, digital running mean) of equivalent passband $B _ { 0 }$ reduces the variance of the fluctuations, and the resulting noise temperature is given by

$$
T = T _ { \mathrm { s y s t e m } } \left( \frac { B _ { 0 } } { B } \right) ^ { 1 / 2 } ,
$$

where $T _ { \mathrm { s y s t e m } }$ is the system noise temperature defined for $B \ : = \ : B _ { 0 }$ . Note that half Dof the total measurement time is used for calibration, which therefore doubles the noise power. Each of the above operations is carried out digitally.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/6a4c74ab9b8bf50c5cc768f58719589a1dfd94f5318df6e3157e20a2af6194f5.jpg)  
Fig. 8.35 Spectrum of the galactic object W49 OH (a very intense $\textrm { H I I }$ region). Spectral element $B = 2 \mathrm { k H z }$ . Number of channels $N = 1 0 0$ . Central Dfrequencies $\nu _ { 0 } = 1 6 6 5$ and $1 6 6 7 \mathrm { M H z }$ D, respectively (radical OH lines). Note the complex radial velocity structure of the various components of the object

In brief, the source spectrum is found in the frequency interval $\Delta \nu$ around the frequency $\nu _ { 0 }$ , with resolution $R \ = \ \nu _ { 0 } / B$ , averaged over a time interval of about $1 / B _ { 0 }$ .

Multichannel spectrometers (Fig. 8.35) can include up to 512 channels operating in parallel, and the width $B$ of each channel can be made almost arbitrarily narrow, but rarely less than $1 \mathrm { k H z }$ in practice.

# The Acoustic Spectrometer

This second method appeals to a different idea. The intermediate frequency signal excites vibrations in a piezoelectric crystal, which in turn generates an ultrasonic sound wave in a lithium niobate crystal $\left( \mathrm { L i N b } \mathrm { O } _ { 3 } \right)$ ). Other materials (tellurium dioxide or gallium phosphide) can be used to vary the useful band between 0.2 and 2 GHz. Promising tests (2007) aim to replace acoustic excitation of the crystal by laser excitation, keeping the crystal at low temperature $( \sim 4 \mathrm { K } )$ in order to extend the lifetime of metastable states created by the laser radiation. The band could then reach $2 0 \mathrm { G H z }$ .

The fluctuations of the refractive index at successive wavefronts are used to diffract the beam of an optical laser (for example, He–Ne, or a solid-state laser diode). The diffracted energy is distributed across a multichannel linear detector (a 1024 or 2048 pixel CCD array), in which each pixel has a size corresponding to the frequency spread $B$ , or less, if over-sampling is required. The frequency resolution is limited by diffraction and attenuation in the acoustic medium. If the IF signal is monochromatic, all the diffracted energy is concentrated on a single pixel (Bragg reflection), and the spectrum produced by the sequential readout of the diodes is indeed non-zero only on a single element. In the case of a more complicated spectrum, the energy distribution on the diodes is simply proportional to the IF spectrum (Fig. 8.36).

This instrument is particularly compact and low in power consumption (a few watts), factors which make it ideal for use on board a satellite. For example, the European Herschel mission (launch 2008) carries an acousto-optical spectrometer, the Wide Band Spectrometer (HIFI) with four juxtaposed units of $B = 1$ GHz each, to observe in the range 0.5–1.9 THz.

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/8fd77724cad649d51d32a673630c2c6b399d26d2291f1df272a2013bea1d36a0.jpg)  
Fig. 8.36 Principle of the acoustic spectrometer. The inset shows the intensity received by each of the diodes, namely, the spectral density (spectrum) of the IF signal applied to the piezoelectric crystal. For the purposes of clarity, the angle between the incident direction (laser) and the diffracted direction has been grossly exaggerated. In reality, it would not be more than a few degrees. Note that the lens forms the Fourier transform of the diffracted field on the detector (see Sect. 6.1)

Other spectrometers with similar inspiration may come to light in the future, e.g., using surface waves produced on a solid by interference between two lasers, and used to diffract the radiofrequency signal.

# The Autocorrelation Spectrometer

This has become the main method used in radioastronomy observatories, thanks to progress in speed and capacity of digital processing, and the correlator has become a standard tool for radiofrequency spectrometry.

The autocorrelation spectrometer makes use of the integral transformation property relating the Fourier transform of the spectral density to the autocorrelation function (see Appendix A). If $I ( \nu )$ is the spectrum (in fact, a spectral density, as already pointed out) of the time-dependent IF signal $x ( t )$ , then $I ( \nu )$ is also the Fourier transform of the autocorrelation $R ( \tau )$ of $x ( t )$ :

$$
R ( \tau ) = \langle x ( t ) x ( t + \tau ) \rangle .
$$

At the expense of a slight loss of efficiency, when $x ( t )$ is digitised on a small number of bits, the digitisation of $x ( t )$ followed by an autocorrelation calculation can give

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/1baec97f1e448f1207acd262cf51d67bec6012e85c5cc5282e4e732ab20ad5e5.jpg)  
Fig. 8.37 Spectrum of a cold molecular cloud, obtained using the VESPA instrument on the IRAM $3 0 ~ \mathrm { m }$ radiotelescope (Spain) at $8 8 ~ \mathrm { G H z }$ $\lambda = 3 . 4 \ : \mathrm { m m }$ ). Ordinate: Antenna temperature. Abcissa: DFrequency converted to radial velocity. Resolution $B = 3 0 ~ \mathrm { M H z }$ , and $3 . 3 \ \mathrm { k H z }$ (corresponding to a gas velocity width of $1 1 ~ \mathrm { m } \mathrm { s } ^ { - 1 }$ D) in the inserts, showing the hyperfine structure of the line. Document courtesy of G. Paubert and C. Thum

$R ( \tau )$ in real time, and hence also $I ( \nu )$ . Most correlators work on two bits (1 and 0) with efficiency reduced to 0.6, but sometimes on three (1,0, 1), and up to eight bits, whereupon the efficiency reaches 0.85. A correlator can cover up to $2 5 0 \mathrm { M H z }$ , and several correlators can work in parallel to cover a broader range. The spectral resolution $B = 1 / \tau _ { \mathrm { m a x } }$ is determined by the width of the support of $R$ , hence by the Damplitude of the maximum chosen shift $\tau$ .

Note that the technique can be generalised to the cross-correlation of two signals $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ , viz.,

$$
R _ { 1 2 } ( \tau ) = \langle x _ { 1 } ( t ) x _ { 2 } ( t + \tau ) \rangle ,
$$

and this makes it possible to study two perpendicular polarisations, hence giving direct access to the Stokes parameters.

An example is the Versatile Spectrometer Assembly (VESPA) correlator,11 set up on the IRAM $3 0 ~ \mathrm { m }$ millimetre wave radiotelescope in Spain in 2002. It covers an IF band of $4 8 0 ~ \mathrm { M H z }$ , which can be sliced into spectral elements of width $B = 4 0 ~ \mathrm { k H z }$ , while specific modes can increase the spectral resolution up to a maximum of $1 0 ~ \mathrm { k H z }$ , i.e., a velocity resolution of $1 0 \ \mathrm { m s ^ { - 1 } }$ at $\nu = 1 0 0 \mathrm { M H z }$ , as shown in Fig. 8.37. Spectra are often represented as a function of the LSR radial Dvelocity (Sect. 8.1).

Fast Fourier Transform (FFT)

The spectrum of the intermediate frequency (IF) signal can now be calculated directly almost in real time, thanks to the increasing speed of computer calculation. This spectrum is just the source spectrum but translated in frequency by the heterodyne setup. The $1 2 \textrm { m }$ millimetre wave radiotelescope Atacama Pathfinder EXperiment (APEX), set up at the future site of the ALMA millimetre array in Chile (Sect. 6.4), has a processing mode12 with 16 384 spectral channels in a total band of 1 GHz: the resolved bandwidth is thus $B = 6 1 \mathrm { k H z }$ . The $1 0 0 \times 1 1 0 \mathrm { m }$ metre D and centimetre wave radiotelescope at Greenbank (USA) is also equipped with this kind of processing system. The efficiency is excellent in principle since the digitised signal can be treated directly.

# 8.4.2 Submillimetre Spectroscopy

The submillimetre region $5 0 ~ { \mu \mathrm { m } }$ to $1 \ \mathrm { m m }$ ), still largely unexplored at the time of writing (2007), lies between the more conventional optical regions (mid-infrared) and the radiofrequencies. Both for radiation detection and spectroscopy, it usually borrows its observational methods from one or other of these regions. Very rich in spectral lines, particularly of molecular origin, in the interstellar medium, it also contains some quite fundamental lines, such as the neutral carbon C I fine structure line at $4 9 2 \mathrm { G H z }$ and also the fine structure line of $\mathrm { ~ O ~ I ~ }$ at $6 3 ~ { \mu \mathrm { m } }$ .

Observation in this region thus uses optical filters and grating spectrometers with moderate resolution $\left( < 1 0 0 0 \right)$ , as in the PACS instrument of the European Herschel mission (2008–2012) or in the IRS instrument (IRS) of the Spitzer mission (2003– 2008), operating up to wavelengths close to $2 0 0 \mu \mathrm { m }$ . However, the Herschel mission also carries a very high resolution heterodyne spectrometer, the HIFI instrument, covering the range 280–1 910 GHz $( 1 5 7 - 1 0 7 0 ~ \mu \mathrm { m } )$ . It works on the principle, typical to radiofrequency observation, of a local oscillator and mixers with a superconductor–insulator–superconductor (SIS) junction or hot electron bolometers (see Sect. 7.3). Likewise, the airborne telescope SOFIA13 is equipped with a heterodyne spectrometer covering the range $2 5 0 { - } 6 0 0 ~ { \mu \mathrm { m } }$ to study the interstellar medium.14

Consider again the arrangement of a heterodyne instrument (Fig. 8.38), with a laser as local source and using a quantum quadratic detector of efficiency $\eta$ to mix. The IF exit signal has frequency $\nu _ { \mathrm { s } } - \nu _ { \mathrm { 0 } }$ and the exit current at the detector is

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/856371e80242f8bdbca917ba7f6b9b38081d09b9f6598f536e2145a906c3294d.jpg)  
Fig. 8.38 Heterodyne spectrometer, with a laser as local oscillator

$$
i ( t ) \propto \eta \left[ \frac { E _ { 0 } ^ { 2 } } { 2 } + E _ { \mathrm { s } } E _ { 0 } \cos 2 \pi ( \nu _ { \mathrm { s } } - \nu _ { 0 } ) t \right] ,
$$

neglecting the term in $E _ { \mathrm { s } } ^ { 2 } ( E _ { \mathrm { s } } \ll E _ { 0 } )$ , and also the sum frequency term, which is too high for the frequency response of the detector. After filtering (bandwidth $B$ ) and linear integration (equivalent bandwidth $B _ { 0 }$ ), the signal-to-noise ratio is, in power,

$$
\eta \frac { P _ { \mathrm { s } } } { h \nu ( B B _ { 0 } ) ^ { 1 / 2 } } .
$$

Note that, if $B \ = \ B _ { 0 }$ , the expression $\eta P _ { \mathrm { s } } / h \nu B$ is recovered, which means that Dthe minimal detectable power $P$ (signal-to-noise ratio $\mathit { \Theta } = \mathit { \Theta } 1$ ) corresponds to one photoelectron per hertz of the passband (see Sect. 7.2.2).

In the special case when the source is a blackbody of temperature $T$ , and thus of intensity

$$
\frac { 2 h \nu ^ { 3 } } { c ^ { 2 } } \left( \mathrm { e } ^ { h \nu / k T } - 1 \right) ^ { - 1 } \qquad [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ] ,
$$

the beam etendue is´ $\lambda ^ { 2 }$ , because coherence of the incident field is required in this method of measurement. The ideal signal-to-noise ratio is then deduced to be

$$
2 \eta \left( \mathrm { e } ^ { h \nu / k T } - 1 \right) ^ { - 1 } \left( \frac { B } { B _ { 0 } } \right) ^ { 1 / 2 } .
$$

The resolution of such a spectrometer is only limited by the frequency stability of the local oscillator and by the passband $B$ of the filter.

Extension to Mid-Infrared. The boundary between the submillimetre and infrared regions is fuzzy as far as observational techniques are concerned, as already emphasised. As an example, consider an infrared heterodyne spectrometer made in 1983 (Fig. 8.39). The local oscillator is a

Brightness temperature [K]

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/4daa12dbb018f28c92eda2b914c9cfa24f74f08c51e4f47def8c4bfa4431d1cf.jpg)  
Fig. 8.39 Heterodyne spectrometry in the mid-infrared $( 1 0 . 6 ~ \mu \mathrm { m } )$ . Measurement of an ethane $\mathrm { ( C _ { 2 } H _ { 6 } ) }$ line emitted by the atmosphere of Jupiter. Beam etendue ´ $\lambda ^ { 2 }$ , i.e., a field of $2 ^ { \prime \prime }$ for a $1 . 5 \mathrm { m }$ telescope. Rotational lines corresponding to levels $J = 1 6$ and 17 are fitted to a model (dashed Dline), which is corrected for line broadening due to rotation of the planet (continuous line). The estimated $\sigma$ is shown on the left. From Kostiuk T. et al., Ap. J. 265, 564, 1983. With the kind permission of the Astrophysical Journal

$^ { 1 4 } \mathrm { C } ^ { 1 6 } \mathrm { O } _ { 2 }$ laser, emitting at $8 2 9 . 9 3 \mathrm { c m } ^ { - 1 }$ , and the detector is a HgCdTe photoconductor mixer, with passband $\Delta \nu = 1 . 6 \mathrm { G H z }$ The intermediate bandwidth is $B _ { \mathrm { I F } } = 2 5 \mathrm { M H z }$ , and the resolution is $1 0 ^ { 6 }$ .

# 8.5 Resonance Spectrometers

A particularly elegant method of spectrometry is based upon the following principle. An atomic vapour is illuminated by the radiation under study. If this radiation contains photons whose frequency is equal to the characteristic frequency of some atomic transition in the vapour, then those photons will be absorbed. If a transition is chosen such that the lower level is a ground state, therefore highly populated, and the excited level a resonance, so that the probability of excitation is high, the number of absorbable photons can be maximised. This number is then measured by detecting the photons re-emitted in spontaneous de-excitation of the upper level, and the number of these is proportional to the number of incident photons (Fig. 8.40).

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/d8b03f59b57c36143f5e203dd92e2d01f23222a893e2a6901f83df040304db56.jpg)  
Fig. 8.40 Resonance spectrometer. The photons re-emitted by the vapour are measured at photomultiplier 1, while the signal proportional to the incident radiation is measured at photomultiplier 2. The ratio of the two is independent of atmospheric and instrumental fluctuations

A quite general tuning relation is

$$
\frac { V _ { \mathrm { s o u r c e / c e l l } } } { c } + \frac { V _ { \mathrm { s o u r c e } } } { c } = \frac { V _ { \mathrm { v a p o u r } } } { c } + \frac { e B } { 4 \pi m } ,
$$

which includes the thermal speeds of atoms in the source and in the vapour (both small relative to $c$ ), the motion of the source (e.g., the Sun) relative to the detecting cell (fixed to the Earth or a satellite in space), and also a Zeeman shift which may be imposed on the atoms of the vapour by a magnetic field $B$ . By varying $B$ , the profile of the excitation line can be scanned. A vapour at low temperature $T$ has $V _ { \mathrm { v a p o u r } } \ll V _ { \mathrm { s o u r c e } }$ , and the maximum resolving power of such a spectrometer is given by

$$
R \approx { \frac { c } { V _ { \mathrm { v a p o u r } } } } \approx c \left( { \frac { m } { 3 k T } } \right) ^ { 1 / 2 }
$$

where $m$ is the atomic mass of the vapour atoms. At $T = 5 0 0 \mathrm { K }$ , $R \approx 2 \times 1 0 ^ { 5 }$ for sodium vapour.

Although limited to certain favourable circumstances, this type of resonance spectrometer has been successfully used to measure the photospheric oscillations of the Sun and other stars (in the 1980s) when the velocities to be detected are of order cm $\mathrm { s } ^ { - 1 }$ , and also to study the velocity field of interstellar hydrogen.

# Problems

8.1. Resolution of a Fourier Transform Spectrometer. Consider an interferogram $I ( x )$ , taken over the optical path differences 0 to $x _ { \mathrm { m } }$ .

(a) Show that the observed interferogram is simply the product of the full interferogram ( $x$ varying from $- \infty$ to $+ \infty ,$ and a suitable box function. Deduce the 1 C1instrumental profile of the spectrometer.

(b) Show that, by multiplying the observed interferogram by a suitably chosen function, it is possible to modify the instrumental profile. For example, giving up some resolution in order to decrease the wings of the profile. Examine the use of the multiplying functions

$$
\cos \left( { \frac { \pi x } { 2 x _ { \mathrm { m } } } } \right)
$$

and the sawtooth function

$$
1 - { \frac { x } { x _ { \mathrm { m } } } } \quad { \mathrm { i f ~ } } x \leq x _ { \mathrm { m } } , \qquad { \mathrm { a n d } } \quad 0 \quad { \mathrm { i f ~ } } x > x _ { \mathrm { m } } .
$$

This weighting of the interferogram is called apodisation, because it suppresses the ‘feet’ of the instrumental response. It is also possible to apodise a pupil by the use of an appropriate amplitude or phase mask (see Sect. 6.6).

Answer. (a) The observed interferogram is truncated

$$
I ( x ) = I _ { \mathrm { { c } } } ( x ) I I ( x / x _ { \mathrm { { m } } } ) ,
$$

and in the frequency space,

$$
\tilde { I } ( \sigma ) = \tilde { I } _ { \mathrm { c } } ( \sigma ) \star \mathrm { s i n c } ( x _ { \mathrm { m } } \sigma ) .
$$

The instrumental profile is therefore sinc $( x _ { \mathrm { m } } \sigma )$ .

(b) Multiplying the interferogram by a cosine amounts to modifying the instrumental profile of the spectrometer by

$$
\mathrm { F T } \left[ P ( x / x _ { \mathrm { m } } ) \cos { \left( \frac { \pi x } { 2 x _ { \mathrm { m } } } \right) } \right] .
$$

The resulting profile is wider because the high frequencies are filtered, but the feet of the profile are cleaner (Fig. 8.41).

8.2. Sampling in Fourier Transform Spectroscopy. Let $\sigma _ { \mathbf { M } }$ be the highest wave number contained in the source spectrum. What step $\varDelta$ should be chosen for the moveable mirror so that the interferogram for this radiation is optimally sampled (in the sense of Shannon’s theorem)? (It is easily shown that the question amounts to finding the minimum sampling for a sinusoidal function.)

![](../chunks/Observational Astrophysics Lena_part_0008_pages_0491-0560/auto/images/aff5fd5f46c33153ba0b195f811d5d07e7497f28fb1040cc8420bfff02cd0dc4.jpg)  
Fig. 8.41 Example of apodisation. Continuous line: Point source response of a circular pupil (Airy function). Dashed line: Point source response of a circular pupil after apodisation by a sawtooth function. Note the broadening of the central spike and the significant reduction of the wings

8.3. Imaging and Fourier Transform Spectroscopy. The multiplex capability of an FT spectrometer, combined with a digital detector with many pixels, can in principle be used to obtain a large number of monochromatic images of a source simultaneously, at adjacent frequencies. If the aim is to obtain such images over a $1 \times 1$ arcmin field, with an image quality limited by the atmosphere to 0.5 arcsec, and a resolution of $5 \times 1 0 ^ { 4 }$ , calculate the total number of bits of information accumulated in the interferograms, each data point being digitised on 16 bits.

Answer. The resolution requirement imposes on $x _ { \mathrm { m } }$ the condition: $R = \sigma x _ { \mathrm { m } }$ . The sampling of the interferogram requires $\Delta x = 1 / 2 \sigma$ D, whence the number of images $N = x _ { \mathrm { m } } / \Delta x$ D. Moreover, the information in an image is coded on

$$
( 2 \times 6 0 ) ^ { 2 } \times 1 6 = 2 . 3 \times 1 0 ^ { 5 } { \mathrm { b i t s } } .
$$

The digital dynamic range thus obtained with 16 bits is then $2 ^ { 1 6 } \ \sim \ 6 5 0 0 0$ , which corresponds to the usual dynamic range of CCD detectors. So this cube of information is coded on 23 Gbits.

8.4. An FT spectrograph is used in the photometric band $M$ (see Sect. 3.4), with a high-performance detector $\mathrm { ( N E P = 1 0 ^ { - 1 6 } W H z ^ { - 1 / 2 } } ,$ ). Calculate the thermal photon Dnoise due to atmospheric emission. Take its emissivity to be 0.05, and the beam size fixed by a $4 \mathrm { m }$ telescope with a 10 arcsec field of view at the detector. Show that the broadening of the spectral band allowed by the spectrograph (multiplex advantage) would not improve the signal-to-noise ratio.

# Part III Data Analysis
