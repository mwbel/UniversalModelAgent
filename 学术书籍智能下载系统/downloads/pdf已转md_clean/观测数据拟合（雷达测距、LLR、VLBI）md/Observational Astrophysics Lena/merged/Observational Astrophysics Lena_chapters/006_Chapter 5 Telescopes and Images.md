# Chapter 5 Telescopes and Images

The telescope is so often considered as the astronomical tool par excellence that it would be easy to forget that it is just one of the components of an observing system, and that it would serve no purpose without spectrometers or detectors. The aim of this chapter is first of all to examine the double function of the telescope: it must collect, then form an image of the source of that radiation. Naturally, these two aspects are very closely connected. It is to improve the performance of both that astronomers have always striven, and still strive, to build telescopes of ever increasing size, freeing them if necessary from the constraints of the Earth atmosphere by placing them in space. The close relationship between these functions means that the telescope stricto sensu is considered as just one element of an integrated system, whence the design of the telescope is intimately bound to the design of focal instruments such as cameras, spectrometers, and so on.

Image formation is such a central issue when using a telescope that we shall treat it here from the relatively simple viewpoint of geometrical optics, then discuss the limitations of this picture. This elementary approach will suffice to present the main features of instruments (telescopes) comprising a single primary mirror. Even though most of the ideas are quite general and presented, according to the basic principle of this book, independently of the wavelength under consideration, actual realisations of instruments are in fact highly dependent on the wavelength. We shall attempt to give as complete a presentation as possible of this rapidly evolving area, covering the full extent of the electromagnetic spectrum currently accessible to astronomical observation.

The study of the spatial coherence of radiation will be reserved for Chap. 6, along with the resulting theory of diffraction and image formation in the presence of diffraction. Several major applications will be described: the ultimate angular resolution of telescopes, aperture synthesis or coherent combination of several telescopes to form an array, and image degradation by the Earth atmosphere and ways of overcoming it.

Gravitational optics has recently become a promising branch of astrophysics. Although it does not involve the construction of optical systems in the classical sense of the term, the idea of a gravitational telescope rests upon principles which, at least in the simple cases, are very close to those of geometrical optics. This rapidly moving area will thus be included along with discussion of the more conventional aspects of geometrical optics.

# 5.1 Image and Object in Astronomy

The telescope is the instrument which produces an ‘image of the sky’ in order to identify and measure the energy received from space. But what exactly do we mean by this word ‘image’? Indeed, despite the three-dimensional structure of space, the terrestrial observer can only ever perceive a two-dimensional projection of it on the celestial ‘sphere’. The received intensity is the integral of the locally emitted energy, integrated along the line of sight. Unfolding the measured information, in order to reconstruct the local conditions at each point of the line of sight, involves the delicate operation of inverting the integral, an operation included within the more general category of inverse problems.

Throughout this chapter, the 2-component vector quantity $\pmb \theta$ denotes a point of the celestial sphere, which is to say, a direction characterised by two angles. Different reference frames can be used (horizontal, equatorial, galactic, etc.), and these are discussed in Chap. 8. It serves no purpose, in the present context, to specify the particular frame chosen to represent $\pmb \theta$ .

As seen by the observer, each angular direction $\pmb \theta$ in the sky is associated with a monochromatic flux (defined in Chap. 2) of frequency $\nu$ received by the observer:

$$
\begin{array} { r l } { I _ { \nu } ( \pmb \theta ) } & { { } \left[ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } \right] , } \end{array}
$$

which can also be expressed in terms of a number of photons using

$$
N _ { \nu } ( \pmb \theta ) = \frac { I _ { \nu } ( \pmb \theta ) } { h \nu } \quad \left[ \mathrm { p h o t o n s ~ s ^ { - 1 } ~ m ^ { - 2 } ~ s r ^ { - 1 } ~ H z ^ { - 1 } } \right] .
$$

The distribution $I _ { \nu } ( \pmb \theta )$ is the monochromatic image or map of the observed region of the celestial sphere. The $\nu$ -dependence of this map describes numerous physical properties of the source: opacities responsible for absorption or emission by the source, correlation between phenomena of differing energies, excitation of atoms or molecules in the source, magnetic fields, and many others. The flux $I _ { \nu } ( \pmb \theta )$ may also depend on time (variable source) and the detected polarisation (polarised sources).

The observation process degrades $I _ { \nu } ( \pmb \theta )$ in at least four ways:

1. Through imperfections in the realisation of optical surfaces, which leads to geometrical aberrations, and the finite size of telescopes, antennas, and light gatherers used to collect the incident flux, which leads to diffraction. 2. Through the finite number of photons incident during the measurement time, which introduces measurement noise, and leads to imperfect restitution of $I _ { \nu } ( \pmb \theta )$ , relative to a measurement of infinite signal-to-noise ratio.

3. In the case of ground-based observations, through the consequences of crossing the Earth’s heterogeneous and turbulent atmosphere.

4. Through the existence of a finite spectral resolution $8 \nu _ { 0 }$ and a finite angular resolution $\ S \theta _ { 0 }$ , thereby mixing up radiation coming from different directions and having different frequencies.

In the case where $I _ { \nu } ( \pmb { \theta } ) = \delta ( \pmb { \theta } )$ , an intensity distribution characterising a point source, the domain $| \pmb { \theta } | < \ 8 \theta _ { 0 }$ in which the intensity is actually received determines j jthe angular resolution $\ S \theta _ { 0 }$ of the instrument. This notion of resolution, which is so important in analysing the capacities of an instrument, can also be defined when $I _ { \nu } ( \pmb \theta )$ is no longer studied in the space of values of $\pmb \theta$ , but rather in the Fourier conjugate space $w$ . Such is the case for the large group of instruments known as telescope arrays or interferometers (see Chap. 6).

# 5.1.1 The Telescope and Geometrical Optics

Geometrical optics provides the first approximation in telescope design.1 However many mirrors or lenses are used, the maximum energy collecting capacity is always determined by the aperture of the primary mirror or lens, the first optical element encountered by light from the source. This first element is generally followed by other optical elements (secondary or tertiary) which modify the position, the scale, or the quality of the primary image. At the end of the optical path is the focal plane of the telescope, where the final image is formed. This is the image which will be analysed by spectrometers, polarimeters, and other analysis systems, and/or light detection systems.

The aim of this optical configuration is to obtain, for a source located at infinity and for a given aperture, an image that is as anastigmatic as possible, over as wide a field as possible. The system is perfectly anastigmatic when all rays from a direction $\pmb \theta$ converge exactly to a single point $A ( \pmb \theta )$ in the focal plane of the telescope. If a system is approximately anastigmatic, the image is spread out, rays converging to some neighbourhood of $A ( \pmb \theta )$ whose dimension determines the quality of the image at $A$ . The field of the telescope is the region of the focal plane in which the image is sufficiently bright and sufficiently anastigmatic to fulfil the requirements of the instrument. It is clear that the larger the field, the better will be the use of the available photons and the observation time, with the proviso that the analysis and detection systems be capable of fully exploiting all points of this field.

The perfect anastigmatic surface for producing the image of a point at infinity on its axis, is the paraboloid of revolution. It is natural, therefore, that this should be the surface the most commonly used as primary mirror in telescopes. However, this surface used in isolation is not anastigmatic for any points off its axis, and therefore has no field, so it is equally natural that optical systems should be designed which incorporate more than one mirror. By increasing the number of degrees of freedom of the optical combination, these composite systems offer the best compromise possible between the approximately anastigmatic quality of the image, and the field, bearing in mind the requirements of the user. Nevertheless, it is much more expensive to polish a paraboloid than to polish a sphere, so spherical primary mirrors are sometimes used, with the unavoidable extra cost of then correcting for their aberrations.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/d4bbdd3da77086aa47cfa360c4ab24c151fb73ceb3218ebc68c26b83d41fdd5a.jpg)  
Fig. 5.1 (a) Different focal configurations. Pointing of (b) equatorial and (c) altazimuth groundbased telescopes

# Optical Configuration of Telescopes

Figure 5.1 shows some of the most common configurations, used for both groundbased and spaceborne telescopes, and in very varied wavelength domains, whose design specifications will be described later. The figure shows the single mirror configuration (image at the prime focus), and configurations using two or more components (Cassegrain, Nasmyth, and Coude).´

The off-axis configuration is not shown in Fig. 5.1. In this setup, an aspherical primary mirror forms an image outside the incident beam, a method which avoids any obstruction by secondary or tertiary elements, but which is more complex and more costly to construct. We shall see interesting applications of this in Chap. 6.

The focal ratio, aperture ratio, or numerical aperture $f / D$ , where $f$ is the focal length (or equivalent focal length in the case of a combination of several mirrors) and $D$ the diameter of the pupil, is an important parameter in the design and use of a telescope. The prime focus configuration gives a small focal ratio (1.2–2.5), the Cassegrain and Nasmyth configurations give intermediate focal ratios (7–30), and the Coude configuration gives the largest focal ratios´ $( > 5 0 )$ .

The focal ratio of a single spherical mirror is directly related to its radius of curvature $R$ , since $f = R / 2$ . The construction of mirrors of comparable quality Dand large curvature, possessing values of $f / D$ only just greater than unity, leads to technical difficulties in polishing very open mirrors, but is nevertheless the result sought after. Indeed, for equal values of $D$ , smaller values of $f$ mean less cumbersome lengths, less couple on guiding equipment, reduced mechanical inertia, and a more favourable design generally.

The equivalent focal length, obtained after crossing or being reflected by all the optical surfaces in the system, also governs the scale of the image in the final focal plane. This scale, measured in millimetres per second of arc, is directly proportional to the value of $f$ :

$$
\mathrm { f o c a l ~ s c a l e } = 4 . 8 5 \times 1 0 ^ { - 6 } ~ f \quad \mathrm { m m a r c s e c ^ { - 1 } } ,
$$

where $f$ is in millimetres.

Optimal sampling of images aims to match the detector pixel size $a$ to the size of the element of angular resolution $\delta \theta$ :

$$
f 8 \theta \approx a ~ .
$$

Detectors with small pixels (e.g., photographic plates, or CCD with $a < 1 0 \mu \mathrm { m } ,$ ) can thus easily be placed at the prime focus. Even in this case, increasing diameters and the constant decrease in CCD pixel size often lead to oversampling. When the detector system requires or tolerates narrower beams, or accepts the use of an optical annex to modify the magnification of the image (focal reducer), the detector can be inserted at the Cassegrain or Nasmyth focus. This is the case for photometers, echelle spectrographs, or even Fourier transform spectrometers.

# Optical Aberrations

The compromise between image quality and field means that the image of a geometric point on the source is not a point. This phenomenon is called optical aberration. There are several methods for determining the aberrations of an optical system. In the light ray approximation (geometrical optics), computer ray tracing methods assume some shape for the optical surface (spherical, parabolic, or other aspherical surfaces, such as ellipsoids, hyperboloids or higher order surfaces), and then numerically simulate illumination from a point source $S$ in a given direction $\pmb \theta$ . The distribution of the impact points of the rays in the focal plane represents the energy distribution in the astigmatic image of $S$ , and can be assessed with respect to the allowed tolerance.2

A detailed analysis of aberration, or the methods developed by opticians to overcome it, will not be given here. These are classical topics which can be found in Born and Wolf, Principles of Optics, and also in Lunettes et T´elescopes by Danjon and Couder (Blanchard, Paris, 1983) (see the bibliography). A few remarks will suffice to illustrate the problem. Considering a set of rays coming from a point $A$ of the object and reaching the focal plane after passing through the telescope optics, they will be distributed about some point $A ^ { \prime }$ which would be the ideal image in the absence of any aberration. This scatter of a given ray around $A ^ { \prime }$ is basically a function of two variables. The first is the angular distance $\alpha$ between $A$ and the optical axis; the larger the angle $\alpha$ , which ranges over the field of the instrument, the greater will be the scatter. The second variable is the distance $r$ between the point of impact of the ray on the pupil and the centre of the pupil: the larger this distance is, the greater will be the scatter about $A ^ { \prime }$ . The parameter $\alpha _ { \mathrm { m a x } }$ thus determines the field of the instrument, whilst the maximal value of $r$ in keeping with the required image quality at $A ^ { \prime }$ will determine the maximal diameter $D$ .

The term field refers to the range of values of $\alpha$ such that the image quality there is acceptable. The fully illuminated field refers to that region over which the source $A$ can be displaced without the intensity of the image $A ^ { \prime }$ being reduced by obstructions due to intermediate diaphragms of the optical system. Beyond the fully illuminated field is a region known as the vignetted field, across which the illumination of the focal plane progressively decreases.

When a telescope is being designed, the problem is approached from the other end: first, $D$ and $\alpha _ { \mathrm { m a x } }$ are fixed, and then the optical arrangement (the shape and number of reflecting surfaces, etc.) is sought which best maintains the quality of the images $A ^ { \prime }$ within the angle $\alpha _ { \mathrm { m a x } }$ .

The five primary or Seidel aberrations are:

• Spherical aberration, which only depends on the value $r$ , that is, on the aperture $D$ . In other words, it only depends on the focal ratio $f / D$ of the focal length to the diameter, and is smaller as this ratio is greater, thus favouring narrow optical systems.   
Coma, which depends only on $\alpha$ and occurs even for very small values of $D$ , if $\alpha$ is non-zero.   
• Astigmatism and field curvature, which involve the values of both $f / D$ and $\alpha$ .   
• Distortion, which destroys geometrical similarity between object and image, whilst nevertheless maintaining a one-to-one correspondence between points of the object and points of the image.

Although useful, a study based upon geometrical optics is not sufficient to completely determine the image quality of an optical system, neglecting as it does the phenomenon of diffraction, caused mainly by the finite dimension of the pupils.

It should be added that the anastigmatic character of perfect optical surfaces is not the only factor bearing on image quality. Diffraction comes in again, since mirrors and lenses can never be perfectly polished, and this introduces a further cause of image degradation. This is observed when the size of irregularities on the optical surface becomes comparable with the wavelength of the light in the transverse direction, i.e., along the mirror surface, or in the perpendicular direction. This effect can be measured by quantifying the residual phase perturbations produced on the reflected or refracted wave. Suffice it to say in the present context that polishing defects smaller than the wavelength by a factor of 20 or more have a negligible effect on image quality. Such demanding criteria are commonplace in astronomy, so that only the five main types of aberration mentioned above need be taken into consideration.

One particular case is worth mentioning, however. A telescope, for example, at radiofrequencies, may have been optimised for observation at a certain wavelength $\lambda _ { 0 }$ , maybe in the decimetre or centimetre range. A later use at much shorter wavelengths $\lambda$ , maybe in the centimetre or millimetre range, will generally produce less good images, flaws in the optical path or phase with root mean square deviation $\sigma _ { \phi }$ , induced by reflecting surfaces, notably on the primary mirror, no longer satisfying the condition $\sigma _ { \phi } < \lambda / 2 0$ .

Constructing an instrument always involves a compromise between image quality (approximately anastigmatic) and the field within which this quality will be preserved. The right compromise can be found by taking the following steps: firstly, choosing the geometry of the surfaces (spherical, thus less costly, or aspherical); secondly, choosing the combination of individual components, a larger number offering more degrees of freedom and better optimisation, although at the risk of greater light loss, only partially compensated for by optimal treatment of the surfaces (high reflectivity of mirrors, anti-reflection dioptrics).

These considerations are illustrated in Fig. 5.2, which shows ray tracing by numerical simulation, a method universally used in studying the properties of optical systems. This is the result for a parabolic primary mirror with opening $f / 2$ , slightly deformed in a controlled manner (active optics), associated with an arrangement of three lenses (triplet corrector) close to its prime focus.

The description and analysis of optical aberrations, and likewise, the consequences of inadequately polished optical surfaces, provide a particularly convenient way of introducing a presentation of the local phase errors produced on a wavefront. This analysis cannot, of course, come from the theory of geometrical optics. The formalism of Zernike polynomials is invaluable in the study of general perturbations on wavefronts. In the present case, these perturbations are caused by imperfect or astigmatic optical surfaces, but they may well also be produced when a wave crosses some non-homogeneous medium, and indeed, it is in this context that they will be discussed (see Sect. 6.2).

# The Main Features of a Telescope and Its Optics

The principal parameters characterising a telescope and its optics are as follows:

1. The focal arrangement, illustrated in Fig. 5.1. Note that a single instrument can have several focal points; transformation from one to another simply requires insertion or removal of a mirror. The great advantage of such an arrangement is that focal instrumentation can be located in several different places at any one time, each place having its own focal ratio, or other characteristics.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/6017674c5cc2421e5e853d14f8194d0173f2f4311a78defe8aedb04ad04e163c.jpg)  
Fig. 5.2 Ray tracing by computer. A point source at infinity, placed at various angular distances from the optical axis, illuminates the pupil of a telescope. Each elementary point represented here in the focal plane corresponds to the impact of a ray coming from the same point source but passing through a different point of the pupil. As the calculations also take into account the effects of diffraction, which is a chromatic phenomenon, the final result depends on the wavelength, given on the horizontal axis. The number next to each image gives the radius in arcsec of the disk containing $80 \%$ of the light energy. The scale is given by the circle at the bottom which has radius $0 . 5 { ^ { \prime \prime } }$ . The linear scale in the focal plane is $2 9 2 \ \mathrm { m m } \ \mathrm { d e g r e e } ^ { - 1 }$ . (Simulation by Enard D., Feasibility Study for the $^ { 8 \mathrm { ~ m ~ } }$ European VLT. European Southern Observatory)

2. The scale of the image in each focal plane, generally given in mm per arcsec. This scale has to be adapted to the choice of detector pixel size, unless the instrument placed at the focus itself modifies the scale through a further optical transformation.

3. The focal ratio of the beam, given by the ratio $f / D$ between the equivalent focal length and the primary mirror diameter.

4. The field, in the two senses of the term. Firstly, the area of the focal plane in which the image quality remains acceptable according to whatever criteria have been predefined; and secondly, the area over which the illumination remains uniform (fully illuminated field), or partial (vignetted field).

5. The image quality, which can be quantified in various ways: using the modulation transfer function (MTF, defined in Sect. 6.1.4) at each point; observing the angular diameter of the circle in which a certain fraction $5 0 \%$ or $80 \%$ ) of the energy from a conjugate point source is concentrated around its ideal image; or, finally, by ray tracing (Fig. 5.2). The image quality that is finally achieved is governed by optical design, quality of optical surfaces, diffraction, and also external factors, such as the presence of a medium upstream whose refractive index is not homogeneous (Earth atmosphere).

6. The curvature of the focal plane, which is not necessarily a plane surface, but may indeed produce the best anastigmatic approximation by being curved. This is the case of the Schmidt telescope, whose field can thereby attain several degrees, an unusually large value.

Further specifications could be added to this list, depending on the wavelength region under observation. We return to this in Sect. 5.2, which deals with specific realisations of telescopes.

# 5.1.2 Gravitational Optics

In empty Euclidean space, light rays are described by the geometrical approximation and follow straight lines. When the refractive index $n ( r )$ depends on the space variable, the trajectories are curved, as illustrated by the simple example of atmospheric refraction (see Sect. 2.5).

In general relativity the geometry of space is curved by the distribution of matter, and the trajectories of light rays, or geodesics, are curves which always traverse the local minimal distance.3 Such effects are present in the Universe on different scales, but especially in the vicinity of a black hole, or on the very large scale of clusters of galaxies. A given mass distribution thus produces convergence or divergence effects in light beams, in a way exactly analogous to the effects of variable refractive index in refracting media. The generic term for these effects is gravitational optics. By extension, a gravitational telescope refers to any mass distribution producing this kind of image.

Without going too deeply into the problem, we may consider the simple case of a light ray passing in the vicinity of some mass $M$ . Recall first Fermat’s principle, in differential form:

$$
\delta \int \boldsymbol { n } ( \boldsymbol { r } ) \mathrm { d } \xi = 0 ,
$$

where $\mathrm { d } \xi$ is the length element along the light path. The equation of the trajectory in a medium with variable index follows from Lagrange’s equation,

$$
\frac { \mathrm { d } } { \mathrm { d } \xi } \left[ n ( \boldsymbol { r } ) \frac { \mathrm { d } \boldsymbol { x } } { \mathrm { d } \xi } \right] = \boldsymbol { \nabla } n ( \boldsymbol { r } ) ,
$$

where $x$ is the space coordinate.

In a gravitational field, the condition $\mathrm { d } s ^ { 2 } = 0$ on the generalised distance $s$ is Dsatisfied by the propagation of the light along its trajectory. In a simple metric of

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/d3c5652f0edd1844bc0b7ed6bc9dbde6be505f325f4f6c5a2e3d4270735e7210.jpg)  
Fig. 5.3 Gravitational lens effect due to the cluster of galaxies MS $0 4 4 0 + 0 2 0 3$ , redshift $z = 0 . 1 9$ . C DThe approximately concentric arclets are ‘gravitational images’, created by the cluster of galaxies located beyond it. Left: Image obtained by the Hubble telescope, with a six hour integration time (six orbits), and resolution $0 . 1 { ^ { \prime \prime } }$ (camera WFPC2), sufficient to resolve the thickness of the arclets. Right: Image obtained from ground level by the $3 . 6 \mathrm { ~ m ~ }$ CFH telescope (Hawaii), with angular resolution $0 . 5 { ^ { \prime \prime } }$ and limited by seeing. (Document kindly provided by Hammer F. et al., 1995)

general relativity, the space and time differentials, ${ \mathrm { d } } r$ and $\mathrm { d } t$ , respectively, at distance $r$ from the mass $M$ , are related by the equation

$$
c { \frac { \mathrm { d } t } { \mathrm { d } r } } = 1 + { \frac { G M } { r } } = { \frac { c } { \nu ( r ) } } ,
$$

which thus gives a value $\nu ( r )$ for the apparent speed, in perfect analogy with the effect of a refractive index. This value can be put into Lagrange’s equation, which, upon integration, yields the light paths.

It can thus be understood how a sufficiently large mass distribution may act as a lens, forming an image for the Earth-based observer of some very distant object (Fig. 5.3).

# 5.2 Telescopes

In this section, covering the whole electromagnetic spectrum, we shall examine the specific features of telescopes designed for each given wavelength range. The concept4 was of course first developed for the visible region (by Galileo and Newton in the seventeenth century, Foucault in the nineteenth century, George Hale, Aden Meinel, Raymond Wilson, and others in the twentieth century), then extended to the radio region after 1945. And finally after 1960, it was extended to cover the whole spectrum, observed from the Earth’s surface but also from space.

The discovery or prediction of other information carriers (gravitational waves and neutrinos) has opened the way to speculation about the possibility of building systems, detecting these forms of energy, which fulfil the same role as the classical telescope. This would be an abuse of language at the present rudimentary stage of technical development, in which the tasks of collecting energy, detecting sources, and localising sources in space cannot yet be approached separately. These questions will be approached in Chap. 7, in the context of detection, which remains the main obstacle to observing such signals.

Returning to optical instruments, the quest for maximal collecting area is the common preoccupation in all spectral regions. The limitations, apart from cost, are usually of technological origin. Three basic points are worth remembering:

• The departure of actual optical surfaces from the ideal must remain small compared to the relevant wavelength, in order to obtain the best anastigmatic approximation.   
. When the angular resolution is determined in the most favourable case by diffraction (see Chap. 6), it varies as $\lambda / D$ , where $D$ is the dimension of the primary mirror (or first optical collecting surface). In a global strategy, astronomers of different countries aim in the long term to obtain a uniform angular resolution on the sky, e.g., 0.1 arcsec, in order to be able to compare the properties and morphology of a given object on the same scale and at various wavelengths. However, actually making these different instruments involves a very wide range of sizes and technologies, and the aim of a uniform resolution is almost never achieved.   
The nature of the detection process, which takes place at the focal point of the telescope, determines to a certain extent the design of the telescope.

Because of all these wavelength dependencies, telescope design will be discussed here primarily in terms of the main spectral regions, but distinguishing Earth-based from space observation when necessary. The design of telescope arrays, which significantly improve angular resolutions, will be discussed in Chap 6.

# 5.2.1 Radiotelescopes

Telescopes designed to receive radiofrequency radiation $( 0 . 5 \ \mathrm { m m } \ \lesssim \ \lambda \ \lesssim \ 1 \ \mathrm { k m } )$ are called radiotelescopes or radio dishes. However, the boundary between radio wavelengths (from kilometres to submillimetre) and far infrared wavelengths is not well defined, being somewhere around $0 . 5 \mathrm { m m }$ . Since it does not correspond to any fundamental property, this transition arises rather because of a change in the type of detector from heterodyne detectors to another kind used at shorter wavelengths, i.e., bolometers, then photoconductors, as will be explained in Chap. 7. The transition from one type to the other requires certain modifications in the design and use of the resulting telescopes, so it is logical enough to describe here some of the key features of instruments operating in the radio region.

These radiotelescopes comprise a very big primary mirror $1 0 { - } 1 0 0 \mathrm { m }$ ). It is usually parabolic and the surface accuracy is determined by the operating wavelength. The surface is made from a grid for long wavelengths and continuous panels for shorter wavelengths, with increasing accuracy (/20 environ) for decreasing $\lambda$ . The growing importance of the submillimetre region has led to the construction of better quality mirrors, and even the boundary between radiotelescopes and optical instruments is growing fuzzy. The $1 5 \mathrm { ~ m ~ }$ JCMT radiotelescope (James Clerk Maxwell Telescope) is thus described as the biggest optical telescope in the world (in 2007). The receivers, which also mix strictly radiofrequency detection techniques with optical techniques at the shortest wavelengths (see Sect. 7.4), are placed either directly at the primary focus or at a secondary focus in a Cassegrain setup.

On Earth, the telescope is generally mounted on an altazimuth mount and follows the source in its diurnal motion. At these wavelengths, since sky emission does not vary between day and night, these instruments can operate at all times, whether the sky is cloudy or not. Since the mirrors on these telescopes are robust, they can be built outdoors without a protective dome, which reduces the cost.

More than 20 instruments of this kind with diameters greater than $1 5 \mathrm { ~ m ~ }$ are currently planned or operating around the world (Fig. 5.4). A rather special radiotelescope is the Arecibo radiotelescope in Puerto Rico, which has a primary mirror $3 0 0 \mathrm { ~ m ~ }$ in diameter with a fixed vertical axis. This is a zenith telescope in which the image forms at the focus, but the focus moves as time goes by, so that the receiver must follow the source. The primary mirror of the decimeter wavelength radiotelescope in Nanc¸ay (France), dating from 1961–1964, is rectangular $( 3 0 0 \times 3 5 \mathrm { m } )$ , vertical, but also fixed. It is preceded by a moving plane mirror, which allows a given source to be monitored for longer, and followed by a moving carriage house carrying the receiver.

At radiofrequencies, there are very few multipixel receivers, like photographic plates or CCDs. Obtaining an image of a source with only one pixel available usually means 2D scanning of the source (raster or TV-type scanning), with each pointing direction sampling one pixel of the image. However, at the time of writing (2007), multipixel receivers are being developed, although their capabilities remain modest as yet, both for millimeter wave incoherent imaging (with $1 2 \times 1 2$ bolometer arrays), and for heterodyne detection with a focal plane paved with an array of $5 \times 5$ receiver horns (see Sect. 7.5).

Note also that propagative perturbations in the Earth atmosphere (turbulence in the troposphere or ionosphere), which alters the phase of the waves, only affects observation at wavelengths less than the centimetre.

The angular resolution of radiotelescopes is generally diffraction limited, i.e., at the value $\lambda / D$ , where $D$ is the diameter of the primary mirror (see Sect. 6.1). With $D = 5 0 \mathrm { m }$ , for example, this leads to rather mediocre resolutions, namely 4 arcsec at $\lambda = 1 \mathrm { m m }$ to more than one degree at $\lambda = 1 \mathrm { m }$ . To improve these values, coupled D Darrays of radiotelescopes have been constructed since the 1950s, as discussed in Sect. 6.5.1.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/220b9e755909607da4ae1c2a5dae3e116a99767a4459a44fa8d31156608256c3.jpg)  
Fig. 5.4 (a) Large steerable single-dish radiotelescopes around the world. Existing instruments are plotted against the shortest wavelengths for which they will operate at normal efficiency. Limits imposed by considerations of structural rigidity, and thermal or gravitational distortion, are indicated. These perturbations limit the accuracy with which the desired parabolic shape can be achieved. (Updated version of Blum E.J., Adv. Electron. Electr. Phys. 56, 97, 1981. With the kind permission of the editor.) (b) The Effelsberg radiotelescope (Max Planck Institute, Bonn). The usable part of the mirror is $1 0 0 \mathrm { m }$ in diameter

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/158d7688d891ee599542c3958a261ae63afb13bedce97cdf9ad60a44424c1b5d.jpg)  
Fig. 5.5 Map of one of the regions of intense star formation in Orion, including the Becklin–Neugbauer (BN) object. The map was made in the ammonia $\left( \mathrm { N H } _ { 3 } \right)$ band $\lambda = 1 . 3 \mathrm { c m }$ ) with the DEffelsberg radiotelescope (Germany). The $4 ^ { \prime \prime }$ lobe is shown (half width beam HWB). (a) Constant intensity contours superposed on a photograph. (b) 3D intensity plot. See also the infrared image of the same region in Chap. 7, Fig. 7.35. (After Batrla W. et al., Astr. Ap. 128, 279, 1983. With the kind permission of Astronomy and Astrophysics)

The Effelsberg Radiotelescope (Germany)

The largest steerable dish in existence, this $1 0 0 \mathrm { ~ m ~ }$ diameter instrument has a sufficient surface quality (using metal plates) to operate at wavelengths $\lambda \gtrsim 7 \mathrm { m m }$ . At shorter wavelengths, the energy concentration in the diffracted image becomes inadequate (Fig. 5.4b).

The $3 0 \mathrm { m }$ Millimetre Radiotelescope at Pico Veleta (Spain)

This is a steel structure supporting aluminium panels machined to a nominal precision of $3 5 ~ { \mu \mathrm { m } }$ rms, and which can produce images limited by diffraction to wavelengths in the range 0.87 to $4 \mathrm { m m }$ .

# 5.2.2 Ground-Based Optical Telescopes: Visible and Near Infrared

Telescopes operating in the visible region are the oldest imaging instruments used in astronomy, apart from the human eye, of course. Diameters grew in stages, depending on technological progress made with materials. With the gradual disappearance of the refracting telescope, which effectively ceased to play any important role during the twentieth century, instruments with 5 to $6 \textrm { m }$ mirrors began to appear in the first half of that century, followed by instruments up to $1 0 \mathrm { m }$ in the second half. By 2020–2030, we shall no doubt see instruments reaching $3 0 { - } 5 0 \ \mathrm { m }$ in diameter. The extension to the near and mid-infrared $( \lambda ~ < ~ 3 0 ~ \mu \mathrm { m }$ , approximately) was made in the 1970s, as sensitive detectors became available, and sites were discovered which could provide good atmospheric transmission windows. Tables 5.1 and 5.2 list all visible and infrared optical telescopes on the Earth’s surface with diameter greater than $3 . 5 \mathrm { ~ m ~ }$ at the time of writing (2007), specifying their location.5

It is interesting to invoke several recent developments profoundly affecting some concepts which appeared to have reached their limits. Indeed, the technological difficulties, degradation of images by atmospheric turbulence, and the advent of space travel, seemed for a while at the end of the 1970s to make the further construction of large ground-based telescopes, with diameters greater than $5 { - } 6 \mathrm { m }$ , somewhat improbable. But this point of view rapidly became outdated, for a number of reasons:

• The technological limitations on the construction of very large mirrors have been largely overcome by the use of new materials (e.g., ceramics) and the possibilities of active control leading to a substantial decrease in weight, by building mirrors with segmented surfaces. Methods correcting for the effects of atmospheric turbulence appeared at the end of the 1980s (adaptive optics), preceded by numerical methods correcting images a posteriori (speckle interferometry) developed in the 1970s. Overcoming the effects of turbulence (see Sect. 6.2) meant that full advantage could be taken of improved angular resolution, proportional to the diameter $D$ of the telescope.

Table 5.1 Large ground-based optical telescopes in the northern hemisphere   

<table><tr><td>Latitude</td><td>Altitude [m]</td><td>Site</td><td>Country</td><td>Diameter [m]</td><td>Remarks</td><td>Date</td></tr><tr><td>47N</td><td>2070</td><td>Zelenchuskaya (Caucasus)</td><td>Russia</td><td>6</td><td>Altazimuth mount</td><td>1972</td></tr><tr><td>42°N</td><td>2500</td><td>Xing Long</td><td>China</td><td>4</td><td>LAMOST siderostat</td><td>2007</td></tr><tr><td>37N</td><td>2160</td><td>Calar Alto (Spain)</td><td>Germany and Spain</td><td>3.5</td><td></td><td>1981</td></tr><tr><td>34N</td><td>1706</td><td>Palomar (California)</td><td>USA</td><td>5</td><td>First VLT</td><td>1948</td></tr><tr><td>32°N</td><td>2130</td><td>Kitt Peak, Arizona</td><td>USA</td><td>3.8</td><td>Mayall</td><td>1974</td></tr><tr><td></td><td>3266</td><td>Mt. Graham, Arizona</td><td>USA,Italy, Germany</td><td>2×8.2</td><td>LBT</td><td>2007</td></tr><tr><td>30N</td><td>2076</td><td>Mt.Locke (Texas)</td><td>USA</td><td>9.2</td><td>Hobby-Eberly fixed elevation</td><td>1997</td></tr><tr><td>28N</td><td>2370</td><td>La Palma (Canaries)</td><td>UK</td><td>4.2</td><td>WHT (Herschel)</td><td>1984</td></tr><tr><td></td><td></td><td>Mauna Kea</td><td>Spain</td><td>10.4</td><td>GranTeCan</td><td>2008</td></tr><tr><td>19N</td><td>4200</td><td>(Hawaii)</td><td>UK</td><td>3.8</td><td>Infrared UKIRT</td><td>1979</td></tr><tr><td></td><td></td><td></td><td>Canada, France, Hawaii</td><td>3.6</td><td>CFHT</td><td>1974</td></tr><tr><td></td><td></td><td></td><td>USA (CalTech)</td><td>2×10</td><td>Keck Iand II</td><td>1994</td></tr><tr><td></td><td></td><td></td><td>Japan</td><td>8.4</td><td>Subaru</td><td>1999</td></tr><tr><td></td><td></td><td></td><td>USA (NSF)</td><td>8.0</td><td>Gemini N</td><td>1999</td></tr></table>

Table 5.2 Large ground-based optical telescopes in the southern hemisphere   

<table><tr><td>Latitude</td><td>Altitude [m]</td><td>Site</td><td>Country</td><td>Diameter [m]</td><td>Remarks</td><td>Date</td></tr><tr><td>23°S</td><td>2 650</td><td>C. Paranal (Chile)</td><td>Europe</td><td>4×8.2</td><td>VLT</td><td>1998</td></tr><tr><td rowspan="2">29°S</td><td rowspan="2">2280</td><td rowspan="2">Las Campanas</td><td rowspan="2">USA</td><td>4</td><td>VISTA</td><td>2008</td></tr><tr><td>2×6</td><td>Magellan</td><td>2002</td></tr><tr><td>29°S</td><td>2430</td><td>(Chile) La Silla (Chile)</td><td>Europe (ESO)</td><td>3.6</td><td></td><td>1977</td></tr><tr><td rowspan="3">30°S</td><td rowspan="3">2700</td><td rowspan="3">C.Tololo (Chile)</td><td></td><td>3.5</td><td>NTT</td><td>1989</td></tr><tr><td>USA</td><td>4</td><td>Blanco</td><td>1974</td></tr><tr><td>C.Pachon (Chile) USA</td><td>8.1</td><td>Gemini S</td><td>2001</td></tr><tr><td>32°S</td><td>1500</td><td>Sutherland</td><td>Brazil and USA South Africa</td><td>4.1 11</td><td>SOAR</td><td>2005</td></tr><tr><td>34°S</td><td>1165</td><td>(South Africa) Siding Springs</td><td>and others Australia</td><td>3.9</td><td>SALT AAT</td><td>2005 1974</td></tr></table>

• In high resolution spectrography (Chap. 8), sensitivity depends critically on the diameter $D$ , whilst the luminosity contribution from the sky background is a nuisance but remains acceptable. The need to observe from space is thus less acute than in the case of low resolution photometric or spectral measurements.   
. The cost of space missions is still at least one order of magnitude greater than the cost of building a comparable instrument at ground level. Following the beautiful results of the Hubble telescope, it has now become clear that ground-based and spaceborne observation are complementary and essential. The design of specialised telescopes, e.g., for spectroscopy, results in the development of less costly instruments, but without the flexibility of a conventional telescope. This is the case for the Large Sky Area Multi-Object Fiber Spectroscopic Telescope (LAMOST) at Xing Long in China (2007), which has a fixed primary mirror like the decimetre wavelength radiotelescope in Nanc¸ay, France, or the South African Large Telescope (SALT), which has fixed elevation (2005).

# Construction of Very Large Mirrors

The strategy adopted for constructing very large mirrors (with diameters greater than $2 { - } 3 \ \mathrm { m }$ is now to make them lighter, i.e., thinner. Whatever technical solution is used, the primary becomes too light to ensure its own rigidity. Deformation of the mirror under its own weight would lead to significant and unacceptable aberration, and worse, it would vary with the pointing direction.

Two main technological choices have come to the fore:

• Thin single-piece mirrors, e.g., the European $8 . 2 \mathrm { ~ m ~ V L T }$ , or thick but lightened mirrors, e.g., the $8 . 2 \mathrm { m }$ Large Binocular Telescope in Arizona. Segmented mirrors, i.e., made up of small optical surfaces (around $1 \mathrm { m }$ ), arranged side by side and polished in such a way as to reconstitute the desired paraboloid, e.g., the $1 0 \mathrm { m } \mathrm { K e c k }$ Telescope in Hawaii.

Beyond diameters of $8 { - } 1 0 \mathrm { m }$ , for the generation of extremely large telescopes (ELT) of the years 2005–2040, only the segmented solution is considered.

In both cases, the deformation is accepted but corrected in real time by means of mechanical control from behind the monolithic mirror or the segments making up the mirror. These corrections can in part be programmed as a function of temperature, and also the altitude of the mirror, for gravitational effects, but they are mainly deduced from real time analysis of the image of a star, as given by the mirror. This is the principle of active optics (Fig. 5.6). Benefiting from all the resources of real time control provided by computer science, it underpins the development of mirrors for all the large Earth-based optical telescopes both now and in the future, until new, more effective technologies are devised for lightening these structures (perhaps membrane mirrors).

Ground-based telescopes were traditionally mounted on equatorial mounts, but these have now been practically abandoned, being both cumbersome and heavy, and hence expensive. Today they have been replaced by the altazimuth mount, which uses two axes to compensate for diurnal motion and is computer driven. A pointing accuracy of the order of 0.1 arcsec rms is achieved. The disadvantage with this arrangement is that it creates a rotation of the field which must be compensated for by a field derotator.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/39fdbfc0e4c01183c90fbb4d0ca65b08ac8d948e0363a62a7943b43a201b4b12.jpg)  
Fig. 5.6 An example of active optics. The New Technology Telescope (NTT) at the European Southern Observatory, opened in 1989, has a thin, actively supported primary mirror of diameter $3 . 5 \mathrm { { m } }$ . Shown here is the model used to finalise the dorsal assemblage of jacks which control the shape. These act in such a way as to correct for any mechanical (e.g., gravitational, wind) or thermal deformations of frequency less than $1 \ : \mathrm { H z }$ . (Document R. Wilson, European Southern Observatory)

# Features Specific to the Infrared

At ground level, telescopes can be used indifferently in the visible or the infrared. Note that some large instruments have been built specially for the infrared, an example being the $3 . 8 \mathrm { ~ m ~ U K }$ telescope at Mauna Kea (Hawaii), known as UKIRT. Two factors distinguish the optimal design of an infrared instrument, and the same factors are relevant in the submillimetre region:

• A chopping secondary mirror, usually vibrating at a frequency less than $5 0 \mathrm { H z }$ , makes it possible to alternate very quickly between source and sky background as imaged at the detector, and thus to make a differential measurement. This technique, well adapted to single pixel detectors, has developed hand in hand with more sophisticated background subtraction methods, as described in Sects. 2.3.3 and 9.4. It is nevertheless true to say that the chopping frequency should be as high as possible owing to the rapid time evolution of atmospheric emissions. Low thermal pollution. The optics are designed so that the detector receives as little radiation as possible from sources other than the optical surfaces themselves. This aim is achieved by using suitable arrangements of diaphragms and baffles. In addition, the optical surfaces are treated to reduce emissivity, and a good telescope should not have an emissivity greater than a few percent, taking into account all its surfaces. These considerations apply equally to submillimetre and millimetre telescopes, for the same reason, namely, to avoid drowning out the astronomical signal by the thermal background emitted from the optical system itself.

The New Generation of Optical Telescopes

We shall describe several examples out of the dozen or so new generation telescopes going into operation around the year 2000, and one project for the next generation.

The two Keck telescopes, built in 1992, have diameter $1 0 \mathrm { m }$ , the primary mirrors each consisting of 36 independent and actively supported hexagonal segments of $1 . 8 \mathrm { ~ m ~ }$ , separated by $3 \ \mathrm { m m }$ spaces. The focal ratio $f / D$ is equal to 1.75. Several focal points are available: primary, Cassegrain, and Nasmyth. The two telescopes are $B = 7 5 \mathrm { ~ m ~ }$ apart at the summit of Mauna Kea (Hawaii). They can be coupled Dcoherently (interferometry), and the resulting diameter will lead to great sensitivity, and a large angular resolution $( \lambda / B = 2 . 7 5 \times 1 0 ^ { - 3 }$ arcsec at $\lambda = 1 \mu \mathrm { m }$ ).

D  DThe European Very Large Telescope, or VLT, went into operation in 1998. It consists of four independent telescopes with thin single-piece primary mirrors of effective diameter $8 . 2 \mathrm { m }$ . Each is mounted on active supports, $f / D = 1 . 8 \ \mathrm { m }$ , and DNasmyth, Coude, and Cassegrain focal points are available. The four telescopes´ (Fig. 5.7) are located at the corners of a trapezoid at Cerro Paranal (Chile), and this arrangement allows either an independent use or a coherent combination (interferometry). In the latter case, the resolution is determined by the largest possible separation, $B = 1 2 0 \mathrm { m }$ . Four smaller movable telescopes $( 1 . 8 \mathrm { m } )$ complete Dthe interferometric system, providing bases of variable length and orientation up to $2 0 0 \mathrm { m }$ long.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/8dd78344b5a0f53978dc86a185694b262369eb606ae8eb910f09b3fda10a37ca.jpg)  
Fig. 5.7 The European Very Large Telescope (VLT), Cerro Paranal, ( $2 6 3 5 \mathrm { ~ m ~ }$ , Chile). The VLT consists of four $8 . 2 \textrm { m }$ telescopes, and also a complementary network of mobile interferometric telescopes (foreground). Channels allow transportation of light for recombination at a common focal point. (Drawing kindly supplied by the European Southern Observatory)

The Large Binocular Telescope (LBT or Magellan) is based on a hybrid technology, since it uses thick but lightened single-piece active mirrors of $8 . 4 \mathrm { ~ m ~ }$ forming a binocular pair on the same altazimuth mounting. As in the original MultiMirror Telescope (Mount Hopkins, Arizona), which was its predecessor, built in 1976 and including six mirrors on the same mounting, the beams of light can be either coherently or incoherently superposed. The LBT was set up on Mount Graham (Arizona) and saw its first light in 2005.

The Thirty Meter Telescope (TMT) project results from a joint effort by private and public institutions in Canada and the United States. At the time of writing (2006), this planned $3 0 ~ \mathrm { m }$ telescope is the most advanced of a new generation that will no doubt become a reality in the first half of the twenty-first century. Equipped with a primary mirror of diameter $D \ = \ 3 0 \ \mathrm { m }$ comprising 492 individual $1 . 4 ~ \mathrm { m }$ hexagonal mirrors $4 . 5 \mathrm { c m }$ thick, open at $f / 1$ , it will be set up at the Mauna Kea site in Hawaii. As for all instruments in this category, the construction is only justified if the ultimate angular resolution $\lambda / D$ can be achieved, and this will require an extraordinarily high-performance adaptive optics system (see Sect. 6.3).

Europe (European Southern Observatory ESO) has also been studying the idea of a comparable project, namely the European Extremely Large Telescope (E-ELT) of diameter $4 2 \mathrm { m }$ , and this was approved in 2006.

# 5.2.3 Space Telescopes, from Ultraviolet to Submillimetre

By placing a telescope in space, all the obstacles to astronomical observation caused by the day–night cycle and the Earth atmosphere can be entirely avoided, while covering a very broad region of the electromagnetic spectrum from the ultraviolet to the submillimetre.

Space travel offers possibilities ranging from the use of aeroplanes and stratospheric balloons, to space shuttles, low-orbiting space stations (altitude 400– $5 0 0 \mathrm { k m } , \quad$ ), satellites orbiting the Earth at various distances and sometimes stabilised at Lagrange points, probes investigating objects in the Solar System (planets, moons, comets, asteroids, the Sun, etc.), and instruments on or around the Moon.

Onboard telescopes observe deep space, beyond the confines of the Solar System. Apart from the possibilities of in situ investigation, more specific instruments can also provide images of objects, e.g., mapping the surface of Mars from an instrument in Martian orbit. The quest for large diameters, usually justified by the increased sensitivity required of instruments, is limited by technological and economic issues, just as it is for ground-based instruments. These telescopes are remote controlled and highly reliable both for control of acquisition and pointing, for example, and for reception, processing, and transmission of measurement data. For deep space observation, operational and planned missions are genuine space observatories, specifically designed for a given spectral region.

# Ultraviolet

In the ultraviolet, the spectral limits are rather clear. The atmosphere blocks wavelengths below $3 5 0 ~ \mathrm { { n m } }$ (or $3 2 0 ~ \mathrm { { n m } }$ at high altitude sites), and this has made space observation unavoidable, using balloons and rockets in the 1960s and 1970s, and orbiting observatories thereafter. UV space telescopes are distinguished from visible telescopes only by the quality of their optical surfaces (flaws $< \ \lambda / 2 0$ , approximately), and the need for efficient reflecting surfaces $( \mathrm { M g } \mathrm { F } _ { 2 }$ layers). The production of reflecting layers by means of multiple coatings gives acceptable reflectivity (10 to $20 \%$ ) down to near X ray wavelengths $( 1 0 \ \mathrm { n m } )$ , and thus avoids the constraints imposed in the latter spectral region by the need to use grazing incidence devices.

The Orbiting Astronomical Observatory (OAO) satellites provided the first mapping and photometry of the UV sky in the 1970s. They were followed, in 1978, by the remarkably fertile International Ultraviolet Explorer (IUE) (see Fig. 8.9). This instrument remained active for almost 20 years (1978–1996), equipped with a spectrophotometer in the region $1 1 5 { - } 3 2 0 \mathrm { n m }$ .

In the near ultraviolet region, the main project of the 1990s and 2000s has been the Hubble Space Telescope, launched in 1989 and expected to remain in operation up until 2010. With a diameter of $2 . 4 ~ \mathrm { m }$ and angular resolution $0 . 1 ^ { \prime \prime }$ (after a few initial difficulties), it covers all wavelengths between 110 and $7 0 0 ~ \mathrm { n m }$ . In 2002, during a visit by NASA astronauts, it was equipped with a new instrument, the Advanced Camera for Surveys (ACS), able to provide images and spectra from the ultraviolet to the very near infrared $( 1 1 5 - 1 1 0 0 \mathrm { n m } )$ ).

Among more specialised missions, we should mention:

• The Far Ultraviolet Spectroscopic Explorer (FUSE) run by NASA and other countries, launched in 1999 but affected by a serious failure in 2006, and covering the region $9 0 . 5 \mathrm { - } 1 1 8 . 7 \mathrm { n m }$ .   
• The Galaxy Evolution Explorer (GALEX), a $3 5 \mathrm { c m }$ telescope launched by NASA in 2003, and covering the region $1 3 5 { - } 2 8 0 \mathrm { n m }$ .

The extraordinary results harvested by the Hubble telescope stimulated the preparation of a successor, namely the James Webb Space Telescope (JWST).6 This observatory will be placed at Lagrange point L2 and carry a $6 . 5 \mathrm { ~ m ~ }$ telescope equipped with a segmented mirror deployed in space (see Fig. 5.8). It will cover the region $0 . 6 { - } 2 7 ~ { \mu \mathrm { m } }$ , so is designed rather as a near infrared telescope than an ultraviolet telescope. However, it will be observing the very remote Universe, where spectral shifts due to expansion $( z \gtrsim 1 )$ ) will bring radiation emitted in the ultraviolet into the visible and near infrared range. Launch is planned for 2013.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/43b719ea3936894918706a1287ab24e0b97cde68eefc9d0ee7c5661d7ca27e20.jpg)  
Fig. 5.8 Artist’s impression of the future $6 . 5 \mathrm { ~ m ~ }$ James Webb Space Telescope, to be placed at Lagrange point L2. The figure shows the alignment of the telescope with the Earth and Sun, and a screen protecting the optical system. Credit NASA

Infrared and Submillimetre

The infrared refers to $1 { - } 1 0 0 \ \mu \mathrm { m }$ and the submillimetre to $0 . 1 { - } 1 ~ \mathrm { m m }$ . Although the near and mid-infrared (up to about $3 0 ~ { \mu \mathrm { m } } ,$ ) can in part be observed from the Earth’s surface, space observation is inevitable beyond that. And even below, certain spectral regions absorbed by the Earth atmosphere (e.g., between 5 and $9 ~  { \mu \mathrm { m } } )$ contain emissions of considerable importance (e.g., the spectra emitted by aggregates of aromatic hydrocarbons). Beyond $3 0 ~ { \mu \mathrm { m } }$ , some useful transmission windows exist at ground level in several exceptional sites, such as the Antarctic, but only space observation can provide systematic and precise data. Nevertheless, the concentration of absorbing molecules (mainly $\mathrm { H } _ { 2 } 0$ ) at low altitudes means that aeroplanes and balloons are less costly for observation than a deep space instrument.

During 1980–2010, a considerable wealth of discoveries has been made by infrared observation in this vast spectral region: emission by cold objects in galaxies, but also the intense radiation associated with star formation, the spectra of primordial galaxies shifted toward the infrared by cosmic expansion, the $2 . 7 ~ \mathrm { K }$ cosmic background radiation, and many others. This success justifies a major effort to prepare space observatories covering the whole of this spectral region. But one of the main difficulties with these instruments comes from the need to cool the telescopes, essential for improving sensitivity and reducing the associated background signal and thermal noise (see Chap. 9). In an aircraft or balloon, this cooling remains modest $- 3 0$ to $- 5 0 ^ { \circ } \mathrm { C } )$ ) given the presence of residual atmosphere.  It will be pushed as far as possible in satellites.

Aircraft. An example here is the telescope of the Kuiper Airborne Observatory (KAO), named after the Dutch astronomer G. Kuiper (1906–1973), which had a diameter of $0 . 9 \mathrm { ~ m ~ }$ , and was carried on an aeroplane (USA). It operated in the stratosphere in a very similar way to a ground-based observatory. Its successor aboard a Boeing 747SP (collaboration between NASA and Germany, flown in 2008) is the Stratospheric Observatory for Infrared Astronomy (SOFIA) shown in Fig. 5.9, equipped with $2 . 5 \mathrm { m }$ mirror and flown at an altitude of $1 4 \mathrm { k m }$ .

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/edab198dc1590e0d9fd43a710737c20364ee82f54a05836f8a66db34ad322d37.jpg)  
Fig. 5.9 The $2 . 5 \mathrm { m }$ submillimeter telescope of the NASA’s Stratospheric Observatory for Infrared Astronomy SOFIA on its Boeing 747-SP aircraft. Insert: The 747-SP flying with the telescope open, during its final tests over California in August 2010 (NASA). Drawing kindly provided by Max Planck Institut f¨ur Extraterrestrische Physik, Garching. Photo NASA

Balloons. Many instruments have been carried aboard stratospheric balloons since the beginning of the 1960s, some reaching diameters of around $1 \textrm { m }$ . Among these missions, one of the most remarkable is BOOMERANG, run by NASA in partnership with many other countries since 1998 and designed to study the cosmological background radiation (imaging and polarisation). The cooled telescope has a $1 . 3 ~ \mathrm { m }$ primary mirror and observes wavelengths7 in the range $1 { - } 2 . 1 ~ \mathrm { m m }$ from a stratospheric balloon flying at an altitude of $4 2 \mathrm { k m }$ above the Antarctic continent.

Satellites. On board a satellite, passive cooling by radiation into space leads to temperatures around 80 or $1 0 0 \mathrm { ~ K ~ }$ . The use of cryogenic fluids or closed circuit refrigerators allows for cooling of optical parts and detectors down to 10 or $2 0 ~ \mathrm { K }$ , sometimes even much lower ( $0 . 1 \mathrm { ~ K ~ }$ for dilution refrigerators), and this totally removes the instrumental background.

The InfraRed Astronomy Satellite (IRAS), launched in 1983, included a $0 . 6 \mathrm { m }$ telescope completely cooled by liquid helium. The Infrared Space Observatory (ISO), which operated from 1995 to 1998, had the same diameter and was cooled in the same way. The optics of the COsmic Background Explorer (COBE), launched in 1992, were also cooled, during the first part of the mission, by liquid helium, whose gradual evaporation limited the period of operation.

Let us briefly describe three major missions over the period 2000–2020, the first two (Spitzer and Herschel) dedicated to a wide range of galactic and extragalactic observations and the third (Planck) specifically designed for detailed observation of the cosmological background:

• The Spitzer observatory8 (a mission originally called SIRTF) includes a cooled $0 . 8 5 \mathrm { m }$ telescope operating in the region $3 { - } 1 8 0 \mu \mathrm { m }$ . It was launched by NASA in 2003 with an expected lifetime of 5 years. It is more sensitive than all previous missions (IRAS, ISO). The Herschel observatory9 (a mission originally called the Far InfraRed Space Telescope FIRST) includes a cooled $3 . 5 \mathrm { ~ m ~ }$ telescope designed to carry out galactic and extragalactic observations in the range $6 0 { - } 6 7 0 ~ { \mu \mathrm { m } }$ , with a lifetime of 3 to 4 years (ESA, launch in 2008). It will be placed at Lagrange point L2. Its focal instruments combine detection techniques specific to the infrared (photoconductors) with others for the radio region (heterodyne, see Sect. 7.5). The Planck observatory10 is mainly designed to study the cosmological background radiation, but its extreme sensitivity means it should be able to address many issues of galactic and extragalactic astronomy. Equipped with a telescope cooled to $2 0 \mathrm { ~ K ~ }$ and detectors operating at $0 . 1 \mathrm { ~ K ~ }$ , covering frequencies $3 0 -$ $8 6 0 ~ \mathrm { G H z }$ in fields of 30 to 5 arcmin, this observatory, also placed at Lagrange point L2, should operate for at least 21 months (launch 2008).

Infrared and submillimetre instrumentation on the surface of the Moon would benefit from the very low temperatures (about $1 0 0 ~ \mathrm { K }$ at the bottom of permanently shaded craters in the polar regions), a natural cryogenic source for cooling the optics. This option is still not seriously envisaged (see Sect. 2.10).

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/c123eed9443b5a4d3782405dec760d0791f2ee6e976f8ae5f204dd3b1abcb914.jpg)  
Fig. 5.10 X-ray sky in galactic coordinates. Upper: X-ray survey by HEAO-I, covering $2 { - } 2 0 \mathrm { k e V }$ (Boldt, 1987). Middle: Survey by ROSAT. Dots denote the brightest of the 100 000 point X-ray sources detected (Voges et al., 2000). Lower: ROSAT survey of diffuse X-ray emission. Energies are colour coded, from red $( 0 . 1 \mathrm { - } 0 . 5 \ \mathrm { k e V } )$ to blue $( 0 . 9 { - } 2 . 4 \ \mathrm { k e V } )$ ) (Snowden et al., 1997). (Figure kindly communicated by G. Hasinger, Garching)

# 5.2.4 X-Ray Telescopes

This concerns photons with energies in the range $( 0 . 1 \mathrm { - } 1 0 \mathrm { k e V } )$ . Since the discovery in 1962 of the first $\mathrm { X }$ -ray source outside the Solar System, X-ray astronomy has progressed enormously, observations being made almost exclusively by instruments in orbit. In 1978, the launch of the Einstein satellite (HEAO-II) resulted in a large quantity of data and, notably, X-ray images (Fig. 7.27). Figure 5.10 gives some idea of the progress that has been made.

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/d3567fe48bbec13069966e042135c5a139f6ea1f945d1443309f18604d761234.jpg)  
Fig. 5.11 Side and front views of a Wolter X-ray telescope. $P$ and $H$ denote parabolic and hyperbolic surfaces of revolution, whose common axis points to the source. See also Fig. 5.12

![](../chunks/Observational Astrophysics Lena_part_0003_pages_0141-0210/auto/images/6542b4b3ead1ed1a40a61e444f03419144cad4f6d96c682f29ede6b38c2f8c03.jpg)  
Fig. 5.12 Aperture of the 7 convergent X-ray telescopes planned for the E-ROSITA mission (launch 2015). Each telescope, with entry diameter $1 6 \mathrm { { c m } }$ , consists of 27 nested mirrors. (Source Max Planck Institute f¨ur Extraterrestrische Physik)

Grazing Incidence Telescopes

As metallic surfaces absorb $\mathrm { X }$ -rays at all but very high incidence angles, the Wolter telescope uses grazing incidence $( \approx ~ 8 9 ^ { \circ }$ ) (Figs. 5.11 and 5.12). Two confocal segments of a paraboloid $P$ and a hyperboloid $H$ form, after two reflections, an image of a source at infinity at their common focus.

To increase the effective area presented to the incident radiation, several mirrors are nested together. The system is perfectly anastigmatic on the axis, has no spherical aberration, and satisfies Abbe’s condition (aplanetism), which means that an image formed from paraxial rays has no coma.

In the Einstein telescope, the collecting area is $3 0 0 ~ \mathrm { c m } ^ { 2 }$ for energies less than $2 \mathrm { k e V } ,$ and decreases to $5 0 \mathrm { c m } ^ { 2 }$ at $3 . 5 \mathrm { k e V } ,$ since only those parts of the mirror at the greatest incidence angles play any role at higher energies. The image quality, greatly inferior to the one which would be imposed by diffraction, is limited by defects in the crystalline structure of the metallic mirror surfaces. These defects disturb the periodicity of the crystalline lattice and cause phase errors at the pupil, and hence a deviation from the ideal image in the focal plane (see Sect. 6.2).


<!-- chunk 0004: pages 211-280 -->
Table 5.3 Image quality of X-ray telescopes. The values given in arcsec are the half power beam widths of the point spread functions. The asterisk indicates that image qualities are given by the radius (arcsec) enclosing $50 \%$ of the energy. See the table of space missions at the end of the book to identify the satellites and their instruments, and also planned missions at the time of writing (2007)   

<table><tr><td rowspan="2">Observatory (satellite)</td><td rowspan="2">Energy [keV]</td><td colspan="4">Distance from optical axis [arcmin]</td></tr><tr><td>0&#x27;</td><td>5&#x27;</td><td>10&#x27;</td><td>20&#x27;</td></tr><tr><td>Einstein</td><td>0.28</td><td>8&quot;</td><td>10&quot;</td><td>25&quot;</td><td>1</td></tr><tr><td></td><td>3</td><td>20&quot;</td><td>25&quot;</td><td>40&quot;</td><td>1</td></tr><tr><td>Exosat*</td><td>1</td><td>18&quot;</td><td>1</td><td>1</td><td>40&quot;</td></tr><tr><td>Rosat (HRI)*</td><td>1</td><td>3&quot;</td><td>3&quot;</td><td>7&quot;</td><td>26&quot;</td></tr><tr><td>XMM</td><td>≤2.5</td><td>20&quot;</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Chandra</td><td>二</td><td>&lt;1&quot;</td><td>2&quot;</td><td>5&quot;</td><td>20&quot;</td></tr></table>

By the mid-1990s, the energy limit had progressed from 1 to around $1 0 0 \mathrm { k e V } ,$ by use of mirrors with multiple coatings, which increase reflectivity (Rosat, XMM, and AXAF missions).

Adaptive optics techniques can be transferred from the infrared and visible to X-ray imaging, in this case to correct for phase defects in the mirrors themselves. By the mid-1990s, there has not yet been any application in astronomy, but correcting mirrors are used in the synchrotron at the European Synchrotron Research Facility (Grenoble, France) in order to improve beam focusing.

Table 5.3 gives the image qualities of several X-ray telescopes, measured by the half-power diameter of the image, in seconds of arc.

Application of aperture synthesis methods to the X-ray region is possible, in principle, but will not be justified until diffraction becomes the limiting factor to resolution in X-ray telescopes, and further progress is required.

The availability of powerful and geometrically well-defined X-ray sources in the laboratory (synchrotron radiation at the ESRF in Grenoble, France, see Chap. 3) has greatly encouraged the development of X-ray optical techniques since 1990: interference mirrors, transmitting Fresnel lenses, reflecting Bragg–Fresnel lenses, and so on. This amounts to a generalised transposition to the nanometre scale of totally classical concepts developed for visible optics, or infrared optics, at the micrometre scale.

# 5.2.5 Gamma-Ray Telescopes

Telescopes in the $\gamma$ ray region $( \geq 1 0 \mathrm { k e V } )$ differ from those at other wavelengths in that it becomes difficult to use mirrors in this energy range, and this for two reasons. To begin with, since the grazing incidence angle, already used in X-ray mirrors, is inversely proportional to the photon energy, the focal length, which is of the order of $1 0 \mathrm { m }$ at $2 0 \mathrm { k e V } ,$ would be of order $5 0 0 \mathrm { m }$ at $1 \ \mathrm { M e V } .$ In addition, the size of tolerable surface defects on the mirrors would also be inversely proportional to the energy.

The first of these two difficulties will soon be solved by flying two satellites in formation, one carrying the mirror and the other the detector. The distance between the two satellites, i.e., the focal length, can then be arbitrarily large. This is the plan for the French–Italian mission SIMBOL-X which, with two satellites a distance $2 0 \mathrm { m }$ apart, is expected to operate up to almost $1 0 0 \mathrm { k e V }$ with multilayer mirrors.11 At the time of writing (2007), developments are underway to try to reduce the second difficulty, with the hope of making mirrors operating up to a few hundred keV. So long as such mirrors are not available, images are formed in the $\gamma$ ray region using other principles.

In the region dominated by the photoelectric effect (see Figs. 7.18 and 7.20), coded masks are generally used. However, in energy ranges dominated by Compton scattering or pair creation, the dynamics of each of these phenomena can be used to estimate the direction of each incident photon and form images. The pair effect gives information about the direction of each photon. Compton scattering generally only allows an event to be localised within a circle drawn on the celestial sphere. In both cases, the telescope and the detector become one. This is why the operation of these rather special telescopes will be postponed until Chap 7.

Here we present the coded mask telescope. Coupled with a photoelectric absorption detector, which gives no information about the direction of the incident photon, it forms images just as other telescopes do. However, mirrors are used in other regions not only to form images, but also to concentrate radiation, and it is this aspect which is the most difficult to replace in the $\gamma$ ray region. Below we shall also discuss other $\gamma$ ray observation setups, such as Bragg lenses or detector arrays carried in space and specially designed for the observation of $\gamma$ ray bursts.

One particular feature of $\gamma$ ray observation is the following: the telescope serves mainly to determine as accurately as possible the position in the sky of a generally unresolved source. This identification is essential when we seek the physical nature of the source, or its association with an object like a star or galaxy observed at a different wavelength. It is less common to obtain maps of resolved objects, and more difficult too, given the necessary image processing.

# Coded Masks

The principle of the stenope or camera obscura is an old one: a hole in a mask allows one to form an image on a screen. Making the hole smaller increases the resolution. Since diffraction becomes negligible in the $\mathrm { X }$ and $\gamma$ ray regions, there is no risk of it degrading the resolution and the hole can be arbitrarily small. However, the smaller the hole, the lower the sensitivity. A mask containing a large number of small holes provides a way around these contradictory constraints. The small size of the holes guarantees a good resolution and their large number a high sensitivity. The image is then a linear superposition of the images given by each hole. The idea is to distribute the holes on the mask, which constitutes the aperture, in such a way that the object can be unambiguously reconstructed from measurements of the intensity distribution in the image. The solution to this problem is provided by the coded mask, whose surface is described by a variable transparency function (Fig. 5.13).

![](../chunks/Observational Astrophysics Lena_part_0004_pages_0211-0280/auto/images/d510838d32ebfc6361f212b02c3b2ccaca3238ec3d26e26f09cd19ca3076c5b6.jpg)  
Fig. 5.13 Different coding methods. (a) An optical system forms an image of an object. This image is decomposed into $p \times q$ pixels and sampled by a succession of masks, the energy being focused on a single detector: $( i )$ sampling by a single hole, positioned successively on each pixel; (ii) sampling by a succession of masks $M _ { i }$ with sinusoidal transmission; (iii) sampling by binary masks with random distribution of holes. (b) Stenope. A two-dimensional detector receives the pseudo-image of the source. (c) Random transmission pupil with two-dimensional detector

Let $P$ be the mask pattern used to modulate the flux of an extended source $S$ Then the distribution $I$ observed on the detector can be written as a convolution

$$
I = P \star S + B \ ,
$$

where $B$ represents the background at the detector. An estimate $S ^ { \prime }$ of the source $S$ can be obtained by applying a decoding function $D$ :

$$
S ^ { \prime } = D \star P \star S + D \star B .
$$

The quality of reconstruction thus depends on the choice of $P$ and $D$ (see Sect. 9.6). In the absence of noise, there must exist a one-to-one correspondence between $S$ and

![](../chunks/Observational Astrophysics Lena_part_0004_pages_0211-0280/auto/images/149b8f6265bcc9f49e4be9aa966ed810fdf57591cb9efce4f275a0fce849b1d1.jpg)  
Fig. 5.14 Example of a coded mask based on the HURA principle (Hexagonal Uniformly Redundant Array)

$S ^ { \prime }$ , which amounts to requiring that $D \star P = \delta$ . Furthermore, the background effect Dshould preferably be uniform in the deconvoluted image. Mask patterns $P$ which satisfy these two requirements are said to be optimal. Several different types of optimal pattern are shown in Figs. 5.14 and 5.15.

It can be shown that the efficiency of a coded mask is optimal when the mask transmits around $50 \%$ , but this optimum is not critical, for any transparency between 30 and $70 \%$ gives excellent results. The sensitivity of a coded mask telescope also depends on the ratio of the size $s _ { \mathrm { e } }$ of the elements of the mask to the spatial resolution $r _ { \mathrm { s } }$ of the detector, i.e., the capacity of the detector to sample the image of the mask. In practice, a ratio $s _ { \mathrm { e } } / r _ { \mathrm { s } }$ greater than 2–3 ensures an acceptable imaging efficiency. The angular resolution of a coded mask telescope is directly related to the size $s _ { \mathrm { e } }$ of the mask elements and the distance $d$ between the mask and the detector:

$$
\theta = \arctan \frac { s _ { \mathrm { e } } } { d } \ .
$$

For a fixed distance between mask and detector, and if we impose the imaging efficiency, this sensitivity is thus directly dependent on the spatial resolution of the detector.

More often than not, the basic pattern of the mask covers the same area as the detector, and the mask is composed of a partial repetition of this pattern around a complete central pattern. The field of the telescope depends on the extent of the repetition. Sensitivity is not uniform across the whole field of view, but is directly related to the coded fraction, that is, the fraction of the detector illuminated by a basic mask pattern (even incomplete). In order to characterise the field of view of a coded mask telescope, three limits can be identified: the fully-coded limit, the semicoded limit, and the zero-coded limit. If there is no repetition of the basic pattern, that is, if the mask has the same size as the detector, the field fully coded is zero, and the field at half-sensitivity will be equal to the solid angle subtended by the mask at the detector.

![](../chunks/Observational Astrophysics Lena_part_0004_pages_0211-0280/auto/images/8fc162dfb40b44ba9d71190cf980f43949f449e9037931ce6040ca473401dd69.jpg)  
Fig. 5.15 Image restitution by coded mask. Top left: Image recorded by the $\gamma$ ray telescope of the Sigma instrument (Granat mission 1989–1997). Top right: Image corrected for pixel uniformity defects. Bottom right: Pattern of the Sigma coded mask. Bottom left: Deconvolution of the image top right reveals the Crab Nebula as viewed between 75 and $1 5 0 \mathrm { k e V }$

In the French telescope Sigma, on board the Russian satellite Granat (1989–1997), the mask was of the Uniformly Redundant Array (URA) type, composed of $4 9 \times 5 3$ tungsten elements, each measuring $0 . 9 4 \times 0 . 9 4 \times 1 . 5 \mathrm { c m } ^ { 3 }$ . It was placed at $2 . 5 \mathrm { ~ m ~ }$  from a crystal scintillator (NaI) $\gamma$ -ray  camera and had a theoretical separating power of the order of $1 3 ^ { \prime }$ . The $\gamma$ -ray camera consisted of a NaI disk with diameter $5 7 \mathrm { c m }$ and thickness $1 . 2 \mathrm { c m }$ , and 61 hexagonal photomultiplier tubes (see Sect. 7.6). The location of an interaction was determined by the relative amplitudes of the photomultiplier impulses, to an accuracy of within a few millimetres. The principle of the $\gamma$ -ray camera came from applications in medicine. For orbiting instruments, the accuracy in locating events is reduced by the presence of charged particles. Indeed, the signal corresponding to a proton is such that it disturbs measurements for more than $1 0 0 ~ { \mu \mathrm { s } }$ , a lapse of time comparable with the average time between the arrivals of two protons. Consequently, measurements are always perturbed.

As observed above, masks are designed to give a uniform noise level in the deconvoluted image. This design assumes a uniform noise level at the detector, which is never actually the case. In addition, the pixels of an image never all have the same sensitive area. These two sources of non-homogeneity in the background must therefore be corrected for before deconvoluting the image. Figure 5.15 illustrates the results of such a treatment on data from Sigma.

The imaging telescope IBIS carried aboard the European satellite Integral (launched in 2002), is equipped with a MURA (Modified URA) type coded mask comprising $5 3 \times 5 3$ tungsten elements, each measuring $1 . 1 2 \times 1 . 1 2 \times 1 . 6 \mathrm { c m } ^ { 3 }$ . Placed at $3 . 2 \mathrm { m }$ from two $\gamma$ ray cameras that work together  to ensure efficient detection of photons with energies in the range from $1 5 \ \mathrm { k e V }$ to $1 0 \ \mathrm { M e V } .$ , this mask has a separating power of 12 arcmin. ISGRI, the first of the two cameras, is a new generation instrument comprising 16 384 CdTe semiconductor crystals of dimensions $4 \times 4 \times 2 ~ \mathrm { m m } ^ { 3 }$ , each detecting photons in the range from $1 5 \ \mathrm { k e V }$ to $1 \ \mathrm { M e V }$   with a resolution of the order of $7 \%$ at $1 0 0 \ \mathrm { k e V . }$ The second layer comprises 4 096 scintillating crystals of caesium iodide (CsI) of dimensions $9 . 2 \times 9 . 2 \times 3 0 ~ \mathrm { m m } ^ { 3 }$ , from which the signal is collected by photodiodes. In this way,  a passing proton perturbs only one pixel of ISGRI or PICSIT, and the average time between the passage of two protons is greater than one second. Note that such a large number of measurement channels can only be envisaged in association with dedicated integrated electronics (Application Specific Integrated Circuits, or ASIC) and data compression (see Sect. 9.1.3). The processing of images produced by ISGRI is discussed in Sect. 9.3.4.

# Bragg Lenses

Bragg diffraction (see Sect. 8.3.6) can in principle be applied in the $\gamma$ ray region. Using diffraction in the bulk of a crystal lattice, this avoids the problems relating to the surface state of a mirror. Furthermore, it requires a shorter focal length than with a mirror ${ \approx } 2 0 ~ \mathrm { m }$ at $5 0 0 \mathrm { k e V }$ ). The focusing it produces should in principle offer excellent sensitivity.

A Bragg lens can be made from small crystals ${ \approx } 2 ~ \mathrm { c m }$ placed on concentric circles and oriented in such a way that the crystal planes diffract the photons towards a focal point. Several serious problems are nevertheless encountered. Two of these are intrinsic. The Bragg diffraction condition implies a very narrow field of view ( ${ \approx } 3 5$ arcsec at $E = 5 0 0 \mathrm { k e V } )$ ) and a very narrow spectral dynamic range ${ \approx } 6  { \mathrm { k e V } }$ at $E = 5 0 0 \mathrm { k e V } ,$ D ). These limitations can be reduced either by using crystals in which Dthe atoms are not perfectly aligned on the lattice, or by using various types of crystal or various crystal planes for diffraction. Unfortunately, the resulting improvements in the field and spectral dynamics are obtained at the expense of the sensitivity. Moreover, the orientation of the mirrors must be adjusted and maintained with very great accuracy, of the order of a few arcsec, a real challenge for a spaceborne experiment which is likely to undergo significant vibration during launch.

# Gamma-Ray Burst Telescopes

A $\gamma$ ray burst is an intense flash of $\gamma$ rays, with a luminosity that generally exceeds all other sources in the sky. Some of these are known to be caused by supernova explosions. Any $\gamma$ ray telescope can, of course, detect a burst produced within its field of view, these bursts being extremely bright given the sensitivity of instruments. However, even after five years of operation, the Sigma telescope operating in the 1990s did not detect a single such event in the partially coded field of view of its mask. This is a consequence of the rarity of these events, for the main part, since they occur at the rate of about once per day over the whole sky. Quite clearly, the main requirement to be made of a $\gamma$ ray burst telescope is that it should survey the whole sky at once.

The BAT instrument (Burst Alert Telescope), carried aboard the SWIFT satellite launched in 2004 and dedicated to $\gamma$ ray burst observation, comes close to meeting this objective. It is a coded mask telescope, similar to SIGMA or IBIS, except that it has a field of view of 2 steradians, whence it can detect and accurately locate a hundred or so bursts each year.

Before the advent of these high performance imaging telescopes, other techniques were used to locate bursts. Although they did not use an imaging method in the strict sense of the term, these telescopes are presented here because they do not locate a source by measuring the direction of each photon, as happens in the Compton, pair creation, or Cherenkov telescopes discussed in Sect. 7.6.

# Satellite Networks

A network of satellites equipped with detectors can constitute a $\gamma$ ray burst telescope, provided that each can date events to within 1 millisecond. Knowing the position of each satellite at the moment its detector is triggered, the position of the source (the burster) can be found. The accuracy of this method, known as triangulation, depends on the number of satellites used, their distances, and their relative orientations. This is a relatively old method, but has provided, since 1995, the most accurate results.

# Weighting Telescope

This is an extremely simple system, consisting only of detectors, which are oriented to cover the whole sky. It is based on the idea that a burst, when it occurs, is the brightest source in the sky, which means that the counting rate of any detector during the burst depends only upon its orientation relative to the source (the burster). Schematically, the direction of the burster is estimated by weighting the various lines of sight of the detectors according to their counting rates. The BATSE telescope, on board the Compton Space Observatory (1990–2000), was the first telescope of this type.
