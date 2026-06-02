# Chapter 6 Diffraction and Image Formation

In the last chapter, we discussed telescopes as optical devices able to form images in a way that could be explained by geometrical optics, at least to first order in the light intensity distribution. The wave nature of electromagnetic radiation produces diffraction effects that modify this distribution and introduce a fundamental limitation on the angular resolution of telescopes. Since astronomers always want to obtain images containing more and more detail, it is essential to come to grips with these effects, whose amplitude is directly related to the wavelength of the radiation. Using the notion of coherence discussed in Chap. 3 (see Sect. 3.2), we begin by examining the process by which images are formed in the presence of diffraction, and translate the results in terms of spatial frequency filtering.

There are several reasons for improving the angular resolution of observations. The most obvious is to be able to see the details of an object, such as the surface of a planet, solar granulation, circumstellar disks, stellar diameters, etc. The second and absolutely essential reason is to avoid confusion. Galileo’s refracting telescope allowed him to resolve the milky appearance of our own galaxy, the Milky Way, into stars. Aperture synthesis at radiofrequencies allowed the individual identification of radiogalaxies back in the 1950s. The sky background radiation at X-ray wavelengths was discovered by the first observations of the X-ray sky in 1962.1 But it was not until the Chandra space observatory went into operation some 40 years later that this background was resolved into individual sources, viz., active galactic nuclei. Today, one of the key objectives of the Planck space mission is to discern the individual primordial galaxies at submillimetre wavelengths in the extragalactic background radiation (see Sect. 7.4.10).

Having noted that the property of coherence is closely related to the image formation process and image quality, it is natural to examine the loss of coherence occurring when light passes through inhomogeneous media, and in particular the

Earth atmosphere, together with the harmful consequences of such losses for astronomical images (seeing). Here we shall discuss a convenient general formalism for treating such coherence losses.

The recent discovery, in the 1980s, of ways of limiting these effects by adaptive optics is well worth describing, since it has already contributed to many discoveries, and especially to the present and future development of very large Earth-based optical telescopes.

It was with this tool that twentieth century astronomers, in the tradition of ideas due to Fizeau2 and Michelson,3 were able to increase the angular resolution of their instruments almost at will by building telescope arrays, often called interferometers, able to reconstitute images, by means of aperture synthesis, with very high angular resolution, several orders of magnitude higher than the value $\lambda / D$ given by a telescope of diameter $D$ , which as we have seen could not exceed several tens or hundreds of metres.

As we have done for telescopes, we shall discuss the way this method is implemented for each region of the electromagnetic spectrum, from radiofrequencies to X-ray radiation. However, since $\gamma$ -ray imaging methods are closely related to those used for detection and spectral analysis, we shall discuss $\gamma$ -ray imaging in Chap. 7 on detectors.

The last section of this chapter deals with coronagraphy which, with the help of apodisation methods, provides a way of observing, under good conditions, images with a very broad dynamic range, i.e., exhibiting a significant range of fluxes (from $1 0 ^ { 3 }$ to $1 0 ^ { 1 0 }$ ). While it was traditionally used to study the solar corona, coronagraphy has made a comeback as a way of detecting extrasolar planets, which are faint objects and difficult to observe directly, being swamped by the radiation from the star they orbit so close to.

All questions relating to digital image processing will be postponed to the discussion of signal processing in Chap. 9. This is an area that has witnessed a considerable development with progress in computing.

# 6.1 Diffraction by an Arbitrary Aperture

Here we consider the most general case of diffraction of a light wave by an arbitrary aperture. After presenting the basic mathematical tool, which is simple but powerful and provides a way of treating the whole range of physical cases we are likely

to encounter, we discuss the concept of coherent radiation which is essential to understanding image formation.

# 6.1.1 The Zernike Theorem

We now reconsider quasi-monochromatic radiation, introduced in Chap. 3. We have already shown that it can be regarded as coherent over a coherence length $l _ { \mathrm { c } }$ along the wave vector $\pmb { k }$ . We now seek a rough answer to the following question: if this radiation illuminates an extended surface, and with various orientations of the wave vector, over what area and in which directions can it nevertheless be regarded as coherent? Figure 6.1 shows that a spatial displacement $a$ , normal to $\pmb { k }$ and associated with an angular displacement $\theta$ from $\pmb { k }$ , is acceptable provided that

$$
a \theta \sim \lambda .
$$

The associated ´etendue or throughput, which is the product of the beam area and its solid angle, is then

$$
\omega \simeq a ^ { 2 } \theta ^ { 2 } \simeq \lambda ^ { 2 } \ .
$$

The quantity $\lambda ^ { 2 }$ is called the etendue of coherence´ of quasi-monochromatic radiation of wavelength $\lambda$ . The remainder of this section will be devoted to a more rigorous demonstration of this result.

Consider a source of area $A _ { \mathrm { S } }$ , bounded by a closed curve and illuminating a screen (Fig. 6.2). Each point of the source is assumed to emit quasi-monochromatic radiation. Two points (atoms) of the source, separated by a distance much less than the wavelength $\lambda$ , are assumed mutually incoherent. The aim is to determine, at two points 1 and 2 of the screen, the quantity measuring the correlation of the electric fields

$$
\left. \mathbf { V } _ { 1 } ( t ) \mathbf { V } _ { 2 } ^ { * } ( t ) \right. ,
$$

where ${ \bf V } _ { i } ( t ) = { \bf V } ( r _ { i } , t )$ denotes the electric field at the point $\boldsymbol { r } _ { i }$ , and the asterisk Ddenotes complex conjugation.

![](images/d4ade3e5cb524aac4003d35903ba4b89b2b98d253d0ed2f0028962efaea62a94.jpg)  
Fig. 6.1 Coherence in a beam of finite throughput

![](images/7bbe5310b6dbe3bced8d40d39c637bdf25695abda570d731f4ba074d8073f7be.jpg)  
Fig. 6.2 Coherence of the field on a screen illuminated by a source

Decomposing $A _ { \mathrm { S } }$ into elements $\mathrm { d } \sigma _ { m }$ of dimensions much less than $\lambda$ , at distances $R _ { m _ { 1 } }$ and $R _ { m _ { 2 } }$ from points 1 and 2, it follows that

$$
\begin{array} { l } { { \displaystyle \langle { \bf V } _ { 1 } ( t ) { \bf V } _ { 2 } ^ { * } ( t ) \rangle = \big \langle \sum _ { m } { \bf V } _ { m _ { 1 } } ( t ) \sum _ { j } { \bf V } _ { j _ { 2 } } ^ { * } ( t ) \big \rangle } \ ~ } \\ { { \displaystyle ~ = \sum _ { m } \big \langle { \bf V } _ { m _ { 1 } } ( t ) { \bf V } _ { m _ { 2 } } ^ { * } ( t ) \big \rangle + \sum _ { m } \sum _ { j \ne m } \Big \langle { \bf V } _ { m _ { 1 } } ( t ) { \bf V } _ { j _ { 2 } } ^ { * } ( t ) \Big \rangle } \ , } \end{array}
$$

where ${ \bf V } _ { m _ { 1 } }$ represents the contribution of the element $\mathrm { d } \sigma _ { m }$ to $\mathbf { V } _ { 1 }$ . The second term has zero mean.

The complex field ${ \bf V } _ { m } ( t )$ is given by

$$
\mathbf { V } _ { m } ( t ) = A _ { m } \left( t - \frac { R _ { m } } { c } \right) \frac { \exp \big [ - 2 \pi \mathrm { i } \nu _ { 0 } ( t - R _ { m } / c ) \big ] } { R _ { m } } ,
$$

where $\vert A _ { m } \vert$ is the amplitude and arg $A _ { m }$ the phase of the emission from $\mathrm { d } \sigma _ { m }$ . By j jhomogeneity, $A _ { m }$ is a complex vector. However, to simplify the notation, the vector notation is understood in the term $A _ { m }$ .

It now follows that

$$
\langle \mathbf { V } _ { m _ { 1 } } ( t ) \mathbf { V } _ { m _ { 2 } } ^ { * } ( t ) \rangle = \left. A _ { m _ { 1 } } ( t ) A _ { m _ { 2 } } ^ { * } \left( t - \frac { R _ { m _ { 2 } } - R _ { m _ { 1 } } } { c } \right) \right. \frac { \exp \left[ 2 \pi \mathrm { i } \nu _ { 0 } ( R _ { m _ { 1 } } - R _ { m _ { 2 } } ) / c \right] } { R _ { m _ { 1 } } R _ { m _ { 2 } } } ,
$$

and, taking the stationarity of $\mathbf { V }$ into account,

$$
\left. A _ { m _ { 1 } } ( t ) A _ { m _ { 2 } } ^ { * } \left( t - { \frac { R _ { m _ { 2 } } - R _ { m _ { 1 } } } { c } } \right) \right. = \left. A _ { m _ { 1 } } \left( t - { \frac { R _ { m _ { 1 } } } { c } } \right) A _ { m _ { 2 } } ^ { * } \left( t - { \frac { R _ { m _ { 2 } } } { c } } \right) \right. .
$$

If $( R _ { m _ { 1 } } - R _ { m _ { 2 } } ) / c \ll \tau _ { \mathrm { c } }$ (temporal coherence), then

$$
\langle { \bf V } _ { 1 } ( t ) { \bf V } _ { 2 } ^ { * } ( t ) \rangle = \sum _ { m } \langle A _ { m _ { 1 } } ( t ) A _ { m _ { 2 } } ^ { * } ( t ) \rangle \frac { \exp \left[ 2 \pi \mathrm { i } \nu _ { 0 } ( R _ { m _ { 1 } } - R _ { m _ { 2 } } ) / c \right] } { R _ { m _ { 1 } } R _ { m _ { 2 } } } .
$$

Characterising the intensity from $\mathrm { d } \sigma _ { m }$ by

$$
I ( \boldsymbol { r } _ { m } ) \mathrm { d } \sigma _ { m } = \left. A _ { m } ( t ) A _ { m } ^ { * } ( t ) \right. ,
$$

we now obtain

$$
\langle { \bf V } _ { 1 } ( t ) { \bf V } _ { 2 } ^ { * } ( t ) \rangle = \int _ { A _ { \mathrm { S } } } I ( \pmb { r } ) \frac { \exp \big [ \mathrm { i } k ( R _ { 1 } - R _ { 2 } ) \big ] } { R _ { 1 } R _ { 2 } } \mathrm { d } { \pmb { r } } \ ,
$$

where $k = 2 \pi \nu _ { 0 } / c$ and $r$ denotes an arbitrary point of the source S, at distances $R _ { 1 }$ and $R _ { 2 }$ from the points 1 and 2. Finally, the complex degree of coherence can be written

$$
\gamma _ { 1 2 } ( 0 ) = \frac { 1 } { ( \langle | V _ { 1 } | ^ { 2 } \rangle \langle | V _ { 2 } | ^ { 2 } \rangle ) ^ { 1 / 2 } } \int _ { \mathrm { s o u r c e } } I ( \boldsymbol { r } ) \frac { \exp \left[ \mathrm { i } k ( R _ { 1 } - R _ { 2 } ) \right] } { R _ { 1 } R _ { 2 } } \mathrm { d } \boldsymbol { r } \ .
$$

This is the Zernike–Van Cittert theorem. 4

# Special Case: Large Distance from Source to Screen

The result of the theorem greatly simplifies in this case. Using the notation $r ( x , y )$ , $P _ { 1 } ( X _ { 1 } , Y _ { 1 } )$ , and $P _ { 2 } ( X _ { 2 } , Y _ { 2 } )$ in Fig. 6.2, and retaining only first order terms, with $R _ { 1 } \approx R _ { 2 } \approx R$ ,

$$
R _ { 1 } - R _ { 2 } = \frac { ( X _ { 1 } ^ { 2 } + Y _ { 1 } ^ { 2 } ) - ( X _ { 2 } ^ { 2 } + Y _ { 2 } ^ { 2 } ) } { 2 R } \pm \frac { ( X _ { 1 } - X _ { 2 } ) x + ( Y _ { 1 } - Y _ { 2 } ) y } { R }
$$

and

$$
\begin{array} { l } { \gamma _ { 1 2 } ( 0 ) = \exp \mathrm { i } k \left[ ( X _ { 1 } ^ { 2 } + Y _ { 1 } ^ { 2 } ) - ( X _ { 2 } ^ { 2 } + Y _ { 2 } ^ { 2 } ) \right] ^ { 1 / 2 } } \\ { \times \displaystyle \frac { \iint I ( x , y ) \exp \mathrm { i } k \left[ \frac { \left( X _ { 1 } - X _ { 2 } \right) x } { R } + \frac { ( Y _ { 1 } - Y _ { 2 } ) y } { R } \right] \mathrm { d } x \mathrm { d } y } { \iint I ( x , y ) \mathrm { d } x \mathrm { d } y } ~ . } \end{array}
$$

Introducing angular variables, assumed small,

$$
\frac { x } { R } = \alpha \ , \qquad \frac { y } { R } = \beta \ , \qquad \theta = ( \alpha , \beta ) \ ,
$$

which describe the source as seen from the screen, and the reduced conjugate variables of the Fourier transform which bring in the wavelength, the simplified expression of the theorem becomes

$$
| \gamma _ { 1 2 } ( 0 ) | = \left| \frac { \displaystyle { \iint I ( \theta ) \exp \left\{ - 2 \pi \mathrm { i } \left[ \frac { ( X _ { 2 } - X _ { 1 } ) \alpha } { \lambda } + \frac { ( Y _ { 2 } - Y _ { 1 } ) \beta } { \lambda } \right] \right\} ~ \mathrm { d } \theta } } { \displaystyle { \iint I ( \theta ) \mathrm { d } \theta } } \right| .
$$

In the present case, the Zernike–Van Cittert theorem can be stated as follows:

Theorem. If the linear dimensions of a quasi-monochromatic radiation source and the distance between two points of the screen are both small compared with the distance between the source and the screen, the modulus of the complex degree of coherence is equal to the modulus of the spatial Fourier transform of the source intensity, normalised by the total intensity of the source.

# Special Case: Circular Source

Consider a circular source of radius $r _ { 0 }$ and uniform intensity, illuminating a screen. We calculate the complex degree of coherence $\gamma _ { 1 2 } ( 0 )$ . Let $P _ { 1 }$ be the centre of the screen, $P _ { 2 }$ a point at distance $\rho$ from the centre, and $J _ { 1 }$ the Bessel function of the first kind. Then it follows that

$$
\begin{array} { l } { { \displaystyle I ( \theta ) = \Pi \left( \frac { r } { 2 r _ { 0 } } \right) = \Pi \left( \frac { \theta } { 2 \theta _ { 0 } } \right) ~ , \qquad \theta _ { 0 } = \frac { r _ { 0 } } { R } ~ , } } \\ { { \displaystyle | \gamma _ { 1 2 } ( 0 ) | = | \gamma ( \rho , 0 ) | = \left| \frac { J _ { 1 } ( 2 \pi \theta _ { 0 } \rho / \lambda ) } { \pi \theta _ { 0 } \rho / \lambda } \right| = \frac { 2 | J _ { 1 } ( u ) | } { u } ~ . } } \end{array}
$$

Figure 6.3 shows the modulus $| \gamma |$ of the degree of coherence between the centre of j jthe screen and an arbitrary point of the screen at distance $\rho$ . The phase difference is unknown, but is irrelevant provided $\tau \ll \tau _ { \mathrm { c } }$ . The coherence, which takes the value of one at the origin, by definition, decreases in an oscillatory fashion with the distance separating the two points.

# 6.1.2 Coherence Etendue

In the case of a point source at infinity, $r _ { 0 } / R \to 0 , \gamma \to 1$ over the whole screen. ! !Hence, in this limit, the screen is illuminated by a plane quasi-monochromatic wave.

![](images/e79a47a29296372032a1d1507af378f5a21669b4fe5ab3700430bbe7c0173c5a.jpg)  
Fig. 6.3 Coherence of the field produced by a circular source of angular radius $\theta _ { 0 }$

If the source has a finite angular size of radius $\theta _ { 0 }$ , it subtends a solid angle $\varOmega$ at a point of the screen, and some area $S = \pi \rho ^ { 2 }$ of the screen corresponds to a beam etendue ´ $\mathcal { E } ^ { \mathcal { O } }$ given by

$$
\mathcal { E } = S \Omega = \pi \rho ^ { 2 } \pi \theta _ { 0 } ^ { 2 } = \frac { \lambda ^ { 2 } } { 4 } u ^ { 2 } .
$$

Choosing $u = 2$ arbitrarily, so that

$$
\left| \gamma \left( \rho = \frac { \lambda } { \pi \theta _ { 0 } } \right) \right| = \frac { 2 J _ { 1 } ( 2 ) } { 2 } = 0 . 5 7 7 \ : ,
$$

it can be deduced that the coherence on the screen remains significant $( | \gamma | > 0 . 5 7 7 )$ in the etendue´

$$
\mathcal { E } ^ { \mathrm { ~ ~ } } = \lambda ^ { 2 } \mathrm { ~ . ~ }
$$

This is a quantitative demonstration of the rather intuitive argument given earlier. The fundamental result is:

The coherence ´etendue (or throughput) of quasi-monochromatic radiation is $\lambda ^ { 2 }$

# Coherence of the Radiation Received from a Star

Consider a red giant star, of radius $r _ { 0 } = 1 . 5 \times 1 0 ^ { 1 1 } \mathrm { m } .$ , at a distance of $1 0 \mathrm { p c }$ ( $1 { \mathrm { p c } } =$ $3 \times 1 0 ^ { 1 6 } \mathrm { m } )$ ). For this object, $\theta _ { 0 } = 5 \times 1 0 ^ { - 7 } \ \mathrm { r a d } = 0 . 1$ Darcsec. If the star is observed at $\lambda = 0 . 5 \mu \mathrm { m }$ D  D, the value of the coherence radius $\rho$ , on a screen normal to the rays, Don Earth, is

$$
\rho = { \frac { \lambda } { \pi \theta _ { 0 } } } = 3 2 \mathrm { c m } .
$$

In the infrared, at $\lambda = 2 5 ~ \mu \mathrm { m }$ , the radius $\rho$ is increased fifty-fold, an observation Dwhich will be put to good use later on.

The received radiation is thus coherent, in the sense described above, within a circle of radius $\rho ( \lambda )$ . Clearly, this is no longer exact if the radiation is compared at two points within the circle at times differing by $\Delta t$ , such that $\Delta t \gg \tau _ { \mathrm { c } } = 1 / \Delta \nu$ .

The surface of the star plays the part of the plane source. The fact that the star is spherical simply modifies the phase of the elements $\mathrm { d } \sigma _ { m }$ , and this has no effect on the result.

# Reception of Radiofrequencies

A radiofrequency receiver superposes the fields emitted by different parts of the source $( \varOmega )$ and received at different points $( S )$ . This superposition can only be carried out in a coherent way, producing constructive interference and hence a significant field amplitude, if $S \varOmega \lesssim \lambda ^ { 2 }$ .

# 6.1.3 Diffraction at Infinity

Having received the wave at the surface of the screen, we must now examine the consequences of the fact that only a finite part of the wavefront can be analysed in the receiving system. This is indeed what happens at the telescope pupil when the incident wave (generally, plane) encounters the primary mirror, i.e., the mirror truncates the wave when it reflects it.

# Fraunhofer Diffraction

Consider a purely monochromatic wave, emitted at $P _ { 0 }$ , and received at $P _ { 1 }$ , after diffraction by a screen $\mathcal { A }$ (Fig. 6.4). A calculation very similar to the previous one

![](images/cc071b8a3db7fdab0792226f2315a1fb50debeab1776acacfaedaed19a6a1fa0.jpg)  
Fig. 6.4 Fraunhofer diffraction

leads to the Kirchoff–Fresnel relation or integral, 5 giving the complex amplitude of the field at $P _ { 1 }$

$$
\mathbf { V } _ { 1 } ( t ) = \frac { \mathrm { i } } { 2 \lambda } \mathrm { e } ^ { 2 \pi \mathrm { i } \nu t } \iint A ( r ) \mathrm { e } ^ { \mathrm { i } \phi ( r ) } \frac { \exp \big [ \mathrm { i } k ( q + s ) \big ] } { q s } \big [ \cos ( n , q ) - \cos ( n , s ) \big ] \mathrm { d } r \ ,
$$

where the notation is specified in Fig. 6.4, with $A ( r )$ the field amplitude at the screen, which can be taken as constant, and $\phi ( \boldsymbol { r } )$ represents any phase change created by the screen (referred to as a phase mask).6 In general, $\phi = 0$ .

Diffraction observed at a finite distance from the diffracting object is called Fresnel diffraction,7   
and diffraction observed at an infinite distance is called Fraunhofer diffraction.8

We now consider diffraction at infinity, where the linear dimensions of the screen are small compared with $( q , s )$ . Introducing angles $\theta _ { 0 } \ = \ ( x _ { 0 } / p , y _ { 0 } / q ) , \theta _ { 1 } \ =$ $\left( x _ { 1 } / s , \ y _ { 1 } / s \right)$ , and putting $\textbf { \textit { r } } = \textbf { \textit { ( x , y ) } }$ D D, the amplitude of the diffracted field in direction $\pmb \theta$ Dcan be expressed as

$$
\mathbf { V } _ { 1 } ( \pmb \theta _ { 1 } ) = C \iint G \left( \frac { \pmb r } { \lambda } \right) A \left( \frac { \pmb r } { \lambda } \right) \exp \left[ - 2 \pi \mathbf { i } \left( \pmb \theta _ { 1 } - \pmb \theta _ { 0 } \right) \cdot \frac { \pmb r } { \lambda } \right] \frac { \mathrm { d } \pmb r } { \lambda ^ { 2 } } ,
$$

where $C$ is a constant. $r / \lambda$ and $\pmb \theta$ appear as conjugate Fourier variables and $G ( r / \lambda )$ denotes a pupil function, satisfying

$$
G ( \boldsymbol { r } ) = \left\{ \begin{array} { l l } { 1 \mathrm { ~ i n s i d e ~ \mathcal { A } ~ } , } \\ { 0 \mathrm { ~ o u t s i d e ~ \mathcal { A } ~ } . } \end{array} \right.
$$

The generality of the notion of pupil function makes it invaluable. If the pupil introduced a phase difference $\phi ( \boldsymbol { r } )$ at the point $r$ , this could be represented by putting $G ( r ) = \exp ( \mathrm { i } \phi ( r ) )$ , rather than $G = 1$ , on $\mathcal { A }$ . This property is used for Dapodisation of a pupil (see Sect. 6.6).

In order to determine $C$ , we use the fact that the energy $E$ coming from $P _ { 0 }$ and passing through the area $\mathcal { A }$ of the pupil is conserved across the diffraction pattern, so that

$$
\iint | \mathbf { V } _ { 1 } ( \pmb \theta _ { 1 } ) | ^ { 2 } \mathrm { d } \pmb \theta _ { 1 } = E .
$$

Given the above Fourier transform, Parseval’s theorem can be written

$$
\iint | \mathbf { V } _ { 1 } ( \pmb { \theta } _ { 1 } ) | ^ { 2 } \mathrm { d } \pmb { \theta } _ { 1 } = | C | ^ { 2 } \iint \left| G \left( \frac { \pmb { r } } { \lambda } \right) \right| ^ { 2 } \frac { \mathrm { d } \pmb { r } } { \lambda ^ { 2 } } ,
$$

and this gives

$$
E = | C | ^ { 2 } { \frac { \mathcal { A } } { \lambda ^ { 2 } } } .
$$

$C$ is determined and the final result is

$$
\mathbf { V } _ { 1 } ( \pmb { \theta } _ { 1 } , t ) = \lambda \left( \frac { E } { \mathcal { A } } \right) ^ { 1 / 2 } \iint _ { \mathrm { s c r e e n } } G \left( \frac { \pmb { r } } { \lambda } \right) \exp \left[ - 2 \pi \mathrm { i } ( \pmb { \theta } _ { 1 } - \pmb { \theta } _ { 0 } ) \cdot \frac { \pmb { r } } { \lambda } \right] \frac { \mathrm { d } \pmb { r } } { \lambda ^ { 2 } } .
$$

This equation is the fundamental result for diffraction at infinity, and forms the basis of the following discussion. It can be stated as:

Theorem. When a screen is illuminated by a source at infinity, the amplitude of the field diffracted in any direction is the Fourier transform of the pupil function characterising the screen, the conjugate variables being the angular direction and the reduced coordinates $r / \lambda$ on the screen.

Note. If a lens with no aberrations is placed behind the screen, all the rays of the same $\pmb \theta _ { 1 }$ converge at the same point of the focal plane of the lens, and the Fourier transform is moved back to a finite distance in this focal plane. It is clearly more convenient, and more common, to observe or measure images in a plane situated at a finite distance.

# Relationship Between Image and Object

Consider an object at infinity made up of a set of point sources $P _ { 0 }$ , emitting quasi-monochromatic radiation, and illuminating a screen (Fig. 6.5). A contour $C$ determines the region of the screen, called the pupil, letting the wave through. Each point of the image is characterised by a direction $\pmb \theta$ , or, if a lens of focal length $f$ and without aberration forms this image on its focal plane, by a position $\pmb { R } = f \pmb { \theta }$ in this Dimage plane. In elementary geometrical optics, there is a one-to-one correspondence between the points of the object and those of the image, and hence the name of the latter.

![](images/63723b65a7f94a04ebe9d4860942f77a603ee2a247dc6a1ffe18c10da0eb07a3.jpg)  
Fig. 6.5 Relationship between image and object

Denote by $K ( \pmb \theta _ { 0 } ; \pmb \theta _ { 1 } )$ the transmission of the system, that is, the complex Iamplitude per unit solid angle round $\pmb \theta _ { 1 }$ , obtained in the image for unit amplitude and zero phase at the point $\pmb { \theta } _ { 0 }$ of the object. Denote by $V$ the complex field amplitude, dropping the time dependence to simplify notation.

Coherent Sources

Consider first a point source at ${ \pmb \theta } _ { 0 } ^ { \prime }$ , so that

$$
V ( \pmb \theta _ { 1 } ) = K ( \pmb \theta _ { 0 } ^ { \prime } ; \pmb \theta _ { 1 } ) , \qquad V ( \pmb \theta _ { 0 } ) = \delta ( \pmb \theta _ { 0 } - \pmb \theta _ { 0 } ^ { \prime } ) .
$$

Then $K ( \pmb { \theta } _ { 0 } ^ { \prime } ; \pmb { \theta } _ { 1 } )$ is the response function of the system, and the image brightness is

$$
\begin{array} { r } { | V ( \pmb \theta _ { 1 } ) | ^ { 2 } = | K | ^ { 2 } . } \end{array}
$$

If the optical system between object and image planes is perfect (without aberration), then

$$
K ( \pmb \theta _ { 0 } ^ { \prime } ; \pmb \theta _ { 1 } ) = K ( \pmb \theta _ { 1 } - \pmb \theta _ { 0 } ^ { \prime } ) ~ ,
$$

and the image of an off-axis source can be found by translation of the image of a source on the axis (isoplanicity). Even in an imperfect system which has been reasonably well corrected for geometrical aberrations, this condition is usually satisfied in some small neighbourhood of a point (domain of isoplanicity), to which we can limit ourselves.

The image of an extended object is obtained by linear superposition

$$
V ( \pmb \theta _ { 1 } ) = \iint _ { \mathrm { o b j e c t } } V _ { 0 } ( \pmb \theta _ { 0 } ) K ( \pmb \theta _ { 1 } - \pmb \theta _ { 0 } ) \mathrm d \pmb \theta _ { 0 } ,
$$

where $V _ { 0 }$ denotes the complex amplitude emitted by the point $\pmb { \theta } _ { 0 }$ of the object. Then the expression obtained for the diffraction at infinity gives

$$
\begin{array} { l } { { \displaystyle { V ( \pmb { \theta } _ { 1 } ) = \iint V _ { 0 } ( \pmb { \theta } _ { 0 } ) K ( \pmb { \theta } _ { 1 } - \pmb { \theta } _ { 0 } ) \mathrm { d } \pmb { \theta } _ { 0 } ~ , } } } \\ { { \displaystyle { K ( \pmb { \theta } ) = \iint G ( \pmb { r } ) \exp \left( - 2 \pi \mathrm { i } \frac { \pmb { r } } { \lambda } { \cdot } \pmb { \theta } \right) \frac { \mathrm { d } \pmb { r } } { \lambda ^ { 2 } } ~ , } } } \end{array}
$$

where $G ( r )$ is the pupil function.

This is a convolution equation, which can be conveniently expressed in the Fourier space, where the variable is the spatial frequency $w$ . Setting

$$
\tilde { V } _ { \mathrm { 0 } } ( \boldsymbol { w } ) = \iint _ { \mathrm { o b j e c t } } V _ { \mathrm { 0 } } ( \pmb { \theta } _ { \mathrm { 0 } } ) \exp ( - 2 \pi \mathrm { i } \pmb { \theta } _ { \mathrm { 0 } } \cdot \boldsymbol { w } ) \mathrm { d } \pmb { \theta } _ { \mathrm { 0 } } ,
$$

and similarly

$$
\tilde { V } ( \pmb { w } ) = \mathrm { F T } \left[ V ( \pmb { \theta } _ { 1 } ) \right] \ , \qquad \tilde { K } = \mathrm { F T } \left[ K \right] \ ,
$$

the convolution equation becomes

$$
\tilde { V } = \tilde { V } _ { 0 } \tilde { K } = \tilde { V } _ { 0 } G \ .
$$

The complex quantity $\tilde { K }$ is the modulation transfer function (MTF) of the amplitude Qfor coherent illumination.

The variable $w$ is dimensionless and conjugate to the angular variable $\pmb \theta$ (rad). It can thus be expressed in rad $^ { - 1 }$ , and considered as a spatial frequency. The amplitude of $\tilde { V } _ { 0 } ( w )$ expresses the effect of the component of frequency $w$ in the object, whilst the phase of $\tilde { V } _ { 0 } ( w )$ expresses the translated position of this component in the image.

The relation simply asserts that the complex amplitude of a Fourier component of the image can be found from that of the object by multiplication by the filter $\tilde { K }$ , which thus acts as a spatial filter. Note that $K$ is itself the Fourier transform of the pupil function, expressed in reduced coordinates $r / \lambda$ . These results are summarised in the example shown in Fig. 6.6.

Incoherent Sources

This is, of course, the more common case, since extended sources of radiation in astrophysics, whether they be thermal or non-thermal, do not manifest large scale spatial coherence.

![](images/30d98ca6dd0fb188d2a7dbb93fdcba2f03969deedc6cbd6588f5e0378274fe55.jpg)  
Fig. 6.6 Spatial frequencies of a grid. The grid, with sinusoidal transmission $G ( r )$ , is illuminated by a plane monochromatic wave. Its diffraction pattern at infinity is brought to the focal plane of a lens. It has three Dirac spikes, the autocorrelation function of the Fourier transform of $G ( r )$ , convoluted by the point source response associated with the finite size of the lens

The method is essentially the same, except that intensities, rather than amplitudes, are added in this case. If there is isoplanicity, it follows that

$$
I ( \pmb \theta _ { 1 } ) = \iint _ { \mathrm { o b j e c t } } I _ { 0 } ( \pmb \theta _ { 0 } ) | K ( \pmb \theta _ { 1 } - \pmb \theta _ { 0 } ) | ^ { 2 } \mathrm d \pmb \theta _ { 0 } .
$$

With the same notations for the Fourier transforms (Appendix A), we obtain

$$
\tilde { I } ( w ) = \tilde { I } _ { 0 } ( w ) \tilde { H } ( w ) \ ,
$$

where $\tilde { I } ( \boldsymbol w )$ and $\tilde { I } _ { 0 } ( w )$ are the Fourier transforms of the image brightness and of the object intensity, respectively. Denoting convolution by $\star$ ,

$$
\tilde { H } ( w ) = \mathrm { F T } \left[ | K | ^ { 2 } \right] = \mathrm { F T } \left[ K K ^ { * } \right] = G ( \lambda w ) \star G ^ { * } ( - \lambda w ) .
$$

Using the result obtained here, the image brightness can be found from the object and pupil structures, when diffraction is the only phenomenon to be taken into account.

# 6.1.4 Spatial Filtering by a Pupil

The image intensity manifests a spectrum of spatial frequencies, resulting from that of the object by a transformation referred to as linear filtering. This filter only depends on the pupil function $G ( r / \lambda )$ (which is complex, in general), expressed as a function of the reduced space variable $w = r / \lambda$ .

# Modulation Transfer Function

We have shown that diffraction by a finite sized pupil amounts to a spatial filtering of the object.

In the special (and common) case of a centrally symmetric pupil, the autoconvolution is just the autocorrelation, and we obtain

$$
\tilde { H } ( w ) = \iint _ { \mathrm { p u p i l p l a n e } } G ( \lambda w + r ) G ^ { * } ( r ) \frac { \mathrm { d } r } { \lambda ^ { 2 } } .
$$

Normalising to the area of the pupil, in the same units, we obtain

$$
\tilde { T } ( w ) = \frac { \tilde { H } ( w ) } { \displaystyle \iint G ( \boldsymbol { r } ) G ^ { * } ( \boldsymbol { r } ) \mathrm { d } \boldsymbol { r } / \lambda ^ { 2 } } .
$$

The function $\tilde { T } ( \boldsymbol { w } )$ is called the intensity modulation transfer function of the system. It is often simply denoted MTF, the context removing any risk of confusion with the amplitude MTF.

The spatial frequency plane, over which ranges $\boldsymbol { w } = \left( u , \nu \right)$ , is often referred to as the $( u , \nu )$ plane. The function $| K | ^ { 2 } = H ( \pmb \theta )$ Dis called the point source response j j Dof the system, or the point spread function (PSF). Clearly, $H ( \pmb \theta )$ depends on the shape of the pupil. There may be sidelobes, of greater or lesser importance, reducing the energy concentration in the central regions of the image. A frequently used approximation, when $H ( \pmb \theta )$ is sufficiently compact and has circular symmetry, is to characterise it by a half power beam width (HPBW), i.e., the angular size $\Delta \theta$ within which half of the beam energy resides. This gives an idea of the order of magnitude of the angular resolution.

Example. Referring to the arrangement shown in Fig. 6.6, if the modulation of the grid $G$ is limited to a pupil of finite width $a$ (a slit pupil), it follows that

$$
G ( \pmb { r } ) = \pi \left( \frac { x } { a } \right) , G \star G ^ { * } = \Lambda \left( \frac { x } { a } \right) , r = ( x , y ) ,
$$

$$
\tilde { T } ( w ) = { \cal A } \left( \lambda \frac { u } { a } \right) \ , w = ( u , \nu ) \ ,
$$

$$
H ( \pmb \theta ) = \mathrm { s i n c } ^ { 2 } \left( \frac a \lambda \pmb \theta _ { x } \right) .
$$

# Image Sampling

An important consequence of the filtering theorem just established is the following: since all physical pupils have a finite size in the pupil plane, the function $T$ must have bounded support. In every direction of the $w$ plane, there is a cutoff frequency $w _ { \mathrm { c } } = ( u _ { \mathrm { c } } ^ { 2 } + \nu _ { \mathrm { c } } ^ { 2 } ) ^ { 1 / 2 }$ . The pupil acts as a low-pass filter on the spatial frequencies of D Cthe object. All other physical dimensions being equal, the spatial frequency cutoff $w _ { \mathrm { c } }$ is lower as the wavelength is higher.

Since the FT of $I ( \pmb \theta )$ has bounded support, $I ( \pmb \theta )$ can be completely determined by a discrete sampling of the $\pmb \theta$ plane. If $w _ { \mathrm { c } }$ is the largest spatial frequency contained in $I ( \pmb \theta )$ , Shannon’s theorem (Sect. 9.1) shows that $I$ can be sampled with a rate at least equal to $\Delta \theta = 1 / 2 w _ { \mathrm { c } }$ . This does not mean that the support of $I ( \pmb \theta )$ is bounded. DNevertheless, in practice, if $I _ { 0 } ( \pmb \theta )$ has bounded support, then so does $I ( \pmb \theta )$ , and a finite number of discrete sampling points will suffice.

Note. Even if $I ( w )$ contains no information about the object for $w ~ > ~ w _ { \mathrm { c } }$ , it can nevertheless include noise at frequencies greater than $w _ { \mathrm { c } }$ . There is no reason why the grain of a photographic plate should have the same cutoff frequency as the optical system which produced the image on the plate.

# Circular Pupils

Circular pupils play such an important role in astronomy that they deserve description. Let $r _ { 0 }$ be the radius of the pupil, which is used for quasi-monochromatic light of wavelength $\lambda$ . Then

$$
G ( r ) = \varPi \left( \frac { r } { 2 r _ { 0 } } \right) .
$$

The pupil is symmetric, hence the MTF is real, the autoconvolution is just the autocorrelation, and

$$
G ( r ) \star G ( r ) = \pi r _ { 0 } ^ { 2 } \left[ \frac { 2 } { \pi } \operatorname { a r c c o s } \left( \frac { r } { 2 r _ { 0 } } \right) - \frac { r } { r _ { 0 } } \left( 1 - \frac { r ^ { 2 } } { 4 r _ { 0 } ^ { 2 } } \right) ^ { 1 / 2 } \right] .
$$

The MTF is

$$
\tilde { T } ( w ) = \frac { 2 } { \pi } \left[ \operatorname { a r c c o s } \left( \frac { \lambda w } { 2 r _ { 0 } } \right) - \frac { \lambda w } { r _ { 0 } } \left( 1 - \frac { \lambda ^ { 2 } w ^ { 2 } } { 4 r _ { 0 } ^ { 2 } } \right) ^ { 1 / 2 } \right] ,
$$

and is shown in Fig. 6.7. Note the cutoff frequency $w _ { \mathrm { c } } ~ = ~ 2 r _ { 0 } / \lambda$ , the circular Dsymmetry, and the gradual attenuation with increasing frequency.

![](images/8f325a81050a690de5374f6831a180bf4a5d546aafbdb592e7c62a03ae54af9f.jpg)  
Fig. 6.7 Modulation transfer function of a circular pupil (Airy). The reduced variable $u \ =$ $2 \pi r _ { 0 } \theta / \lambda$ has been used with $R = r _ { 0 }$

The point source response is the image intensity distribution resulting when the pupil is illuminated by a point source. If $J _ { 1 }$ denotes the Bessel function of the first kind,

$$
I _ { 0 } ( \pmb \theta ) = \delta ( \pmb \theta ) , \qquad I _ { 1 } ( \pmb \theta ) = \left[ \frac { 2 J _ { 1 } ( 2 \pi r _ { 0 } \theta / \lambda ) } { 2 \pi r _ { 0 } \theta / \lambda } \right] ^ { 2 } .
$$

This function is often called the Airy function9 and has a ring-like structure. A telescope of diameter $6 \mathrm { m }$ , used at $\lambda = 0 . 5 \mu \mathrm { m }$ , has cutoff $w _ { \mathrm { c } } = 6 0$ arcsec $_ { ; } { - 1 }$ , whereas a radiotelescope of diameter $1 0 0 \mathrm { ~ m ~ }$ , used at $\lambda ~ = ~ 1 8 ~ \mathrm { c m }$ (OH radical Dline), will cut off spatial frequencies beyond the much lower frequency of 0 $w _ { \mathrm { c } } =$ $3 \times 1 0 ^ { - 3 }$ arcsec $^ { - 1 }$ .

Most telescopes include a central secondary mirror of diameter 0 $D ^ { \prime }$ which partially obstructs the pupil of diameter $D$ . The pupil function is, in this case,

$$
G ( r ) = \left\{ \begin{array} { l l } { { 0 \ \mathrm { f o r } } } & { { r < \displaystyle \frac { D ^ { \prime } } { 2 } \ \mathrm { a n d } \ r > \displaystyle \frac { D } { 2 } \ , } } \\ { { } } & { { } } \\ { { 1 \ \mathrm { f o r } } } & { { r \in \displaystyle \left[ \displaystyle \frac { D ^ { \prime } } { 2 } , \displaystyle \frac { D } { 2 } \right] \ . } } \end{array} \right.
$$

It is then straightforward to calculate the new expressions for the MTF and the point source response.

# The Rayleigh Resolution Criterion

The image of two identical point sources with separation $\theta$ is the incoherent superposition of two identical Airy functions. The limit at which the two sources are separated or resolved is arbitrarily fixed by the condition

$$
\theta > \theta _ { 0 } = 0 . 6 1 { \frac { \lambda } { r _ { 0 } } } ,
$$

the value for which the maximum of one Airy function coincides with the first zero of the other. This angular value is often used to characterise the spatial resolving power or discriminating power of a pupil. This so-called Rayleigh criterion10 is more approximate than the one given by the MTF.

In certain cases, it is possible to resolve two point sources closer than $\theta _ { 0 }$ . Indeed, knowing beforehand that two objects are unresolved, for example, the two components of a double star, and that the measurement is made with an excellent signal-to-noise ratio $( \gtrsim 1 0 0 )$ , then the profile $I _ { 1 } ( \pmb \theta )$ will differ measurably from the profile of a single source, even if the separation of the two components is less than $\theta _ { 0 }$ .

This remark illustrates the importance of knowing a priori some of the properties of an object, when reconstructing that object from an image (see Sect. 9.6).

# Apodisation

The intensity distribution in the point source response can be modified by influencing the pupil function $G ( r )$ , which directly determines it. If $G ( r )$ is replaced, in the region where it equals unity, by a complex transmission $\exp \mathrm { i } \phi ( r )$ , which does not affect the amplitude but simply introduces a position-dependent phase change (a phase mask), a judicious choice of the function $\phi ( \boldsymbol { r } )$ can significantly reduce the secondary lobes of the PSF (the ‘feet’ of the diffraction). But this is at the expense of broadening the central lobe, energy being conserved. This operation is referred to as apodisation (see Problem 6.1), discussed further in Sect. 6.6.

# An Overview of Pupil Diffraction

The various Fourier correspondences between quantities describing image formation are summarised in Table 6.1.

Lunar Occultations. There is one particularly interesting case of diffraction which leads to a high angular resolution and is not related to the size of the telescope. This occurs if an astronomical source is occulted by the lunar limb, when the proper motion of the Moon causes it to pass in front of the source. If it is a point source, the monochromatic wave, diffracted at infinity, produces fringes (screen edge fringes), observable as a variation in the intensity $I _ { 0 } ( t )$ received over time by a telescope. If the source is extended, $I ( t )$ results from the convolution of $I _ { 0 } ( t )$ with the angular profile of the source (integrated in the direction parallel to the edge), in the direction normal to the lunar limb (the time dependence being obtained from the speed at which the Moon scans across). The method can be used to reconstruct the angular profile in one dimension, and with high resolution. The latter is determined by the Fresnel scale of the screen edge diffraction, i.e., $( \lambda / 2 D _ { \mathrm { E a r t h - M o o n } } ) ^ { 1 / 2 }$ , ranging from a few arcsec at radiofrequencies to a few mas $1 0 ^ { - 3 }$ arcsec) in the near infrared. Before the advent of astronomical interferometry, lunar occultations were used to determine the size of radiosources and stellar envelopes in the infrared, e.g., the galactic object $\mathrm { I R C } { + } 1 0 2 1 6$ .

Table 6.1 Quantities related to image formation. Corresponding entries in left- and right-hand columns are Fourier pairs   

<table><tr><td>Source 0(0) Image I(0)</td><td>Spatial spectrum O(w) Spatial spectrum I(w)</td></tr><tr><td>Point spread function PSF(0) I(0)= O(0)+PSF(0)</td><td>Modulation transfer function MTF(w) I(w)= O(w)·MTF(w)</td></tr><tr><td></td><td>Pupil function G(r) (spatial units) Pupil G(λw) (spatial frequency units) Autoconvolution G(λw) * G(-λw)</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>(pupil not centrally symmetric)</td></tr><tr><td></td><td></td></tr><tr><td></td><td>Autocorrelation G(λw)  G(λw)</td></tr><tr><td></td><td>(pupil centrally symmetric)</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>PSF(0)</td><td></td></tr><tr><td></td><td>FTM(w) normalised autoconvolution</td></tr></table>

# Disconnected Pupils and Bandpass Frequency Filtering

In the last section, we described a formalism for determining the MTF and the intensity distribution in the image given by an optical system with entrance pupil of arbitrary shape. These general results were applied to the special case of a circular pupil, for which we may thus determine the limiting angular resolution.

We now examine another case of major importance in astronomy, viz., the case where the pupil comprises two circular apertures, often called sub-pupils, of diameter $d$ , placed at a center-to-center distance $D$ from one another, where $D > d$ , so that the pupil is disconnected.

The MTF of this pupil (Fig. 6.8) is given simply by the quantity $G ( r ) \otimes G ( r )$ , after normalisation. This function $\tilde { T } ( \tilde { w } )$ ˝behaves as a spatial filter, which allows through frequencies close to zero and also a band of frequencies, narrow if $D \gg d$ , centred on the frequency $D / \lambda$ , of maximum width $2 d / \lambda$ . The point source response is the Fourier transform of $G \otimes G$ , that is, a sinusoidal modulation of the intensity, having the Airy function of an individual pupil as envelope (see Fig. 6.8c). In other words, the image of a point source placed at infinity through an optical system with this entrance pupil will be a series of narrow fringes which modulate the intensity of a more spread out Airy function.

![](images/b2c9c73c8c3d6359bfe25d5e6fe0e03d43818567b9bdd64b77c4ff8e394c6ea4.jpg)  
Fig. 6.8 (a) Pupil arrangement used by Michelson and Pease on the $2 . 5 \mathrm { m }$ Mount Wilson telescope (California). (b) The pupil function $G ( r )$ . (c) ${ \tilde { T } } ( w ) = G \otimes G$ , MTF for this pupil

If the object is now given by the intensity distribution $I ( \pmb \theta )$ with spatial spectrum $\widetilde { I _ { 0 } } ( w )$ , the spatial spectrum of the image is simply given by the filtering operation

$$
\widetilde { I } ( \pmb { w } ) = \widetilde { T } ( \pmb { w } ) \widetilde { I _ { 0 } } ( \pmb { w } ) \ .
$$

The Fourier transform of $\widetilde { I } ( w )$ is the intensity distribution $I ( \pmb \theta )$ in the final image.

eNote that the observed quantity $I ( \pmb \theta )$ describes an intensity modulation (fringes), with visibility $\widetilde { I } _ { 0 } ( w ) / \widetilde { I _ { 0 } } ( \mathbf { \dot { 0 } } )$ . Note also that this visibility $\mathcal { V } ( \pmb { w } )$ is a complex quantity. The modulation factor of the fringes is given by the modulus $| \mathcal { V } |$ of this j jcomplex quantity and is equal to unity for a point source. We may thus say that this pupil, acting as a filter, measures the spatial coherence of the incident wave between two points separated by a displacement $\pmb { D }$ .

# Aperture Synthesis

For each value of the vector $\pmb { D }$ separating the apertures (distance and direction), the pupil behaves as a bandpass spatial filter which samples the ${ \boldsymbol w } ( \boldsymbol u , \nu )$ plane of spatial frequencies. It is no longer the image which is sampled point by point, but rather its Fourier transform, with each value of $\pmb { D }$ leading to a value of $\tilde { I } ( w = D / \lambda )$ . In Dcontrast to the case of a circular pupil, which transmits all spatial frequencies with varying degrees of attenuation and thereby produces an image that ‘looks like’ the object, this no longer happens in the present case, where the spatial filtering due to the pupil is much more radical.

The usual notions of angular resolution and field in the image space can be transposed to the frequency space. The highest frequencies are $| \pmb { w } | = D _ { \mathrm { m a x } } / \lambda$ , where $D _ { \mathrm { m a x } }$ j j Ddenotes the maximal separation of the sub-pupils, and the frequency width of a frequency information element is of the order of $\delta w = 2 d / \lambda$ .

Supposing that all values of $w$ between 0 and $D _ { \mathrm { m a x } } / \lambda$ Dhave been sampled, the image can be calculated by

$$
I ( \pmb \theta ) = \mathrm { F T } \left[ \tilde { I } ( \pmb w ) \right] ,
$$

$\tilde { I } ( \boldsymbol w )$ only being known on the bounded support $| w | < D _ { \mathrm { m a x } } / \lambda$ . All the information j jin the image that would have been provided by an aperture of diameter $D _ { \mathrm { m a x } }$ has thus been reconstructed, and this reconstruction of a large pupil from pairs of smaller pupils is referred to as aperture synthesis. We shall discuss the many applications of this later.

Note that, just as it is sufficient to sample an image at a finite number of points when its spatial frequency content is bounded (Shannon’s theorem, see Sect. 9.1.3), so it is sufficient in this case to sample $\tilde { I } ( \boldsymbol w )$ at a discrete set of frequencies $w$ .

Instead of combining the radiation in an image plane common to the two telescopes, it is also possible to coherently superpose the two pupils, a method referred to as pupil plane interferometry. From the point of view of information content, the two methods are strictly equivalent. All information entering the pupil of each telescope is contained in the image, and vice versa. Choosing between one or the other way of analysing coherence is rather a question of experimental convenience, detector layout, and finding the best way to handle image degradation due to atmospheric turbulence (see Sect. 6.4).

# 6.2 The Earth Atmosphere and Coherence Losses

The study of image formation reveals the importance of spatial coherence in this analysis. What happens to the image of a point source at infinity (the simplest case) when the coherence of the incident plane wave is modified by phase perturbations? We shall address this question in the present section, accounting for perturbing phenomena produced by crossing the Earth’s atmosphere. As discussed in Chap. 2, the atmosphere has fluctuating refractive index, due either to non-uniformities in the temperature or the electron density, depending on the wavelength.

Let us examine these effects empirically in the particular case of visible and near infrared wavelengths. There are several different effects (Fig. 6.9). Firstly, scintillation, the variation in brightness observed by the eye, or a very small diameter pupil, which corresponds to the spreading or concentration of the wavefront energy. Note immediately that scintillation is only observed for stars (almost point sources), and not for bright planets, which are extended sources (of the order of 10 arcsec at the most). Secondly, agitation of the image in the focal plane of the instrument, which corresponds to a temporal variation in the angle of the mean tangent plane to the wavefront, an angle which determines the position of the centre of the image. And thirdly, smearing of the image, which leads to image sizes much greater (of the order of 1 arcsec) than would result from diffraction alone, caused by loss of spatial coherence at the entrance pupil. It is this smearing effect that is largely responsible for the loss of angular resolution.

![](images/070dc93a44f4719fdd36d68354525f94f39ad990751278ad6541c22387a7bc0b.jpg)  
Fig. 6.9 The main effects of atmospheric turbulence on images. Shown schematically are the incident plane wave, the turbulent atmospheric region, the light rays normal to the perturbed wavefront, and the pupil (shaded). Also shown is the reduced coherence area $\sigma$

The formalism required to interpret and quantify these familiar observational effects will be developed in the following. This same formalism is also used in adaptive optics to correct for such effects.

A complete analysis is given in Roddier F., The Effects of Atmospheric Turbulence in Optical Astronomy in Prog. Opti. XIX, 281, 1981. This reference gives details and justification for the following calculations. See also Woolf N.J., ARAA 20, 367, 1982 and Roddier F. (Ed.), Adaptive Optics in Astronomy, Cambridge University Press, 1999.

# 6.2.1 Perturbations of the Wavefront

We consider the behaviour of the coherence of a monochromatic wave subjected to the effect of a medium with random refractive index $n ( \boldsymbol { r } , t )$ through which it propagates. The process is treated as stationary and ergodic (see Appendix B), although this may well be unrealistic. Denote by $\tau _ { \mathrm { c } }$ the characteristic correlation time of the refractive index, which would be of the order of a few milliseconds in the troposphere. An observation made over a short time relative to $\tau _ { \mathrm { c } }$ ‘freezes’ the turbulence, and two observations separated by a much greater time than $\tau _ { \mathrm { c } }$ are regarded as independent. Note that the period of the electromagnetic waves considered, i.e., $1 0 ^ { - 9 }$ to $1 0 ^ { - 1 5 } \mathrm { ~ s ~ }$ , is totally negligible relative to $\tau _ { \mathrm { c } }$ .

Consider a plane wave $\psi _ { \infty } = 1$ impinging on a turbulent atmospheric layer of thickness $\Delta h$ 1 D, sufficiently small for diffraction on the turbulent elements to be negligible across $\Delta h$ (Fig. 6.10). The wave is quasi-monochromatic. In the geometrical optics approximation, the wave leaving the layer is given by

$$
\psi _ { h } ( { \pmb x } ) = \exp \mathrm { i } \phi _ { h } ( { \pmb x } ) \ ,
$$

$$
\phi _ { h } ( { \pmb x } ) = k \int _ { h } ^ { h + \Delta h } n ( { \pmb x } , h ) \mathrm { d } h \ , \qquad k = \frac { 2 \pi } { \lambda } \ .
$$

![](images/6981c79470fa6d22b68042709e7dbe6dd0aa03ad0574d1cb6fb2b7984867e1f3.jpg)  
Fig. 6.10 Perturbation of a wavefront by a turbulent layer of thickness $\Delta h$

The phase $\phi _ { h }$ of the wave as it leaves the layer is a random variable, whose spatial statistics are determined by the properties of the random variable $n ( \pmb { x } , h )$ . We assume the phenomenon is ergodic (see Appendix B) whence we may use the same notation for time and space averages. The moments of orders 1 (phase excursions greater than $2 \pi$ ) and 2 are written

$$
\begin{array} { c } { { \langle \psi _ { h } ( { \pmb x } ) \rangle = 0 ~ , } } \\ { { { } } } \\ { { B _ { h } ( { \pmb x } ) = \langle \psi _ { h } ( { \pmb x } + { \pmb \xi } ) \psi _ { h } ^ { * } ( { \pmb \xi } ) \rangle = \langle \exp \mathrm { i } \left[ \phi _ { h } ( { \pmb x } + { \pmb \xi } ) - \phi _ { h } ( { \pmb \xi } ) \right] \rangle ~ , } } \end{array}
$$

where the averages are taken over space. The output phase $\phi _ { h } ( { \boldsymbol { x } } )$ can be regarded as resulting from a large number of perturbations, which are phase independent once $\Delta h \gg L$ , where $L$ is the external scale of the turbulence. The distribution of $\phi _ { h }$ is thus Gaussian (by the central limit theorem), with zero mean.

If $u$ is a real Gaussian random variable with zero mean, it is easily shown that

$$
\langle \exp ( \mathrm { i } u ) \rangle = \langle \cos u \rangle = \exp \left( - \frac { 1 } { 2 } \langle u ^ { 2 } \rangle \right) ,
$$

and consequently

$$
B _ { h } ( { \pmb x } ) = \exp \left[ - \frac { 1 } { 2 } \langle | \phi _ { h } ( { \pmb x } + \xi ) - \phi _ { h } ( \xi ) | ^ { 2 } \rangle \right] = \exp \left( - \frac { 1 } { 2 } D _ { \phi } \right) .
$$

The structure function for the phase has been introduced:

$$
D _ { \phi } ( { \pmb x } ) = \langle | \phi _ { h } ( { \pmb x } + { \pmb \xi } ) - \phi _ { h } ( { \pmb \xi } ) | ^ { 2 } \rangle \ .
$$

This can also be written

$$
D _ { \phi } ( { \pmb x } ) = 2 \langle \phi _ { h } ^ { 2 } ( { \pmb \xi } ) \rangle - 2 \langle \phi _ { h } ( { \pmb \xi } ) \phi _ { h } ( { \pmb x } + { \pmb \xi } ) \rangle ~ .
$$

The expression for the phase as a function of $n$ then gives

$$
\langle \phi _ { h } ( \xi ) \phi _ { h } ( { \pmb x } + \xi ) \rangle = k ^ { 2 } \Delta h \int _ { 0 } ^ { h } \mathrm { d } z \int \langle n ( { \pmb x } + \xi , z + \zeta ) n ( \xi , \zeta ) \rangle \mathrm { d } \xi \mathrm { d } \zeta \ .
$$

Using the expression (see Sect. 2.6) for the structure function of the refractive index in a medium of homogeneous and isotropic turbulence,

$$
D _ { n } ( { \pmb x } , z ) = \left. | n ( { \pmb x } + { \pmb \xi } , z + \zeta ) - n ( { \pmb \xi } , \zeta ) | ^ { 2 } \right. = C _ { n } ^ { 2 } ( | { \pmb x } | ^ { 2 } + z ^ { 2 } ) ^ { 1 / 3 } ,
$$

it follows, after integration, that

$$
D _ { \phi } ( x ) = 2 . 9 1 k ^ { 2 } C _ { n } ^ { 2 } \Delta h x ^ { 5 / 3 } .
$$

Recall that $C _ { n } ^ { 2 }$ is the structure constant for the refractive index.

The spatial correlation function for the complex amplitude, on leaving the turbulent layer, is therefore

$$
\langle \psi _ { h } ( { \pmb x } + { \pmb \xi } ) \psi _ { h } ^ { * } ( { \pmb \xi } ) \rangle = \exp \left( - 1 . 4 5 k ^ { 2 } C _ { n } ^ { 2 } \Delta h x ^ { 5 / 3 } \right) .
$$

Since the turbulent layers may be a long way from the entrance pupil of the instrument, we must determine the effect of propagation on this function. The wave field at zero altitude $( h = 0$ ) results from Fresnel diffraction (i.e., long range) of Dthe wave on leaving the layer. It can be shown that the correlation function $B _ { z } ( { \pmb x } )$ is invariant under Fresnel diffraction (Problem 6.15), and hence

$$
B _ { 0 } ( { \pmb x } ) = B _ { h } ( { \pmb x } ) = \exp \left( - \frac { 1 } { 2 } D _ { \phi } \right) .
$$

Some important conclusions can be drawn from these results.

• A short distance behind the layer, only the phase is perturbed. The effects of this phase perturbation are smearing and image motion. Further away, both phase and amplitude are perturbed, and scintillation then occurs. Fluctuations in the amplitude $| \psi _ { 0 } ( { \pmb x } ) |$ can often be neglected when the turbulence is not very great j j(and we shall quantify this later).

• On leaving the layer, the perturbed wavefront displays a correlation function with a complex amplitude, which gives the random phase distribution. This function $B _ { 0 } ( { \pmb x } )$ has an isotropic profile in the plane which is ‘near Gaussian’, so a correlation length $x _ { \mathrm { c } }$ can be defined by the relation

$$
\frac { \langle \psi _ { h } ( x + x _ { \mathrm { c } } ) \psi _ { h } ^ { * } ( x ) \rangle } { \langle | \psi _ { h } ( 0 ) | ^ { 2 } \rangle } \sim \frac { 1 } { e } ,
$$

so that

$$
x _ { \mathrm { c } } \sim ( 1 . 4 5 k ^ { 2 } C _ { n } ^ { 2 } \Delta h ) ^ { - 3 / 5 } .
$$

Inserting typical values $1 0 ^ { - 1 2 } ~ \mathrm { c m } ^ { 1 / 3 }$ for $C _ { n } ^ { 2 } \Delta h$ , at $\lambda = 0 . 5 \mu \mathrm { m }$ , the correlation length turns out to be $x _ { \mathrm { c } } ~ = ~ 9 . 6 ~ \mathrm { c m }$ D. This implies a significant reduction in Dthe spatial coherence of the incident wave. Recall the earlier calculation (see Sect. 6.1.2) which showed that, for a star of apparent diameter 0.1 arcsec, there is a wavefront whose coherence radius reaches $3 2 \mathrm { c m }$ at this wavelength $0 . 5 \mu \mathrm { m }$ .

• Note the highly chromatic nature of the coherence, $x _ { \mathrm { c } }$ varying as $\lambda ^ { 6 / 5 }$ . The coherence length grows more quickly than $\lambda$ , favouring the infrared over the visible.

• If turbulence extends across the whole depth of the atmosphere, the above formulas can be shown to remain valid, replacing $C _ { n } ^ { 2 } \Delta h$ by the expression

$$
\int _ { 0 } ^ { \infty } C _ { n } ^ { 2 } ( z ) \mathrm { d } z .
$$

The value of this expression is found from the vertical distribution of the turbulence (see Sect. 2.6.1). When this distribution is known, e.g., by means of sounding balloons or SODAR, the effect and hence the relative importance of the different layers can be identified for a given site.

• If the effects described above are transposed to radiofrequencies, e.g., $\lambda = 1 \mathrm { c m }$ , the resulting value of $x _ { \mathrm { c } }$ Dreaches several hundred metres and therefore does not perturb image formation, even for the largest radiotelescope diameters. However, phase fluctuations can arise when combining the signals from two widely separated telescopes in interferometry (see Sect. 6.5.1).

# 6.2.2 The Perturbed Image

In the following discussion, we confine ourselves to phase perturbations, neglecting the amplitude perturbations which lead to scintillation.11 An incident plane wave $\psi _ { \infty } ~ = ~ 1$ reaches the pupil perturbed, in the form $\psi _ { 0 } ( r , t )$ . In the absence of 1 Dperturbation, the image would be limited by diffraction, and would be deduced from the pupil function $G ( r )$ defined above (see Sect. 6.1). As the incident wave is plane, the point source response of the pupil would be obtained, e.g., an Airy function in the case of a circular pupil.

In the perturbed case, it is sufficient, in order to calculate the image, to replace the pupil function by a new instantaneous pupil function, which is now a random complex function of time:

$$
G ( r ) \psi _ { 0 } ( r , t ) ~ .
$$

The point source response is then an intensity distribution given by the Fourier transform of the autocorrelation of this pupil function. The image of a point source is therefore a random intensity distribution in the focal plane, whose characteristic evolution time is given by the atmospheric coherence time $\tau _ { \mathrm { c } }$ .

# Long-Exposure Images

When the measurement time (or integration time, in the case of a photographic plate or photoelectric detector) is much larger than $\tau _ { \mathrm { c } }$ , the observed intensity at each point of the image is simply the mean value of the instantaneous intensity:

$$
\begin{array} { r } { I ( \pmb \theta ) = \langle I _ { 0 } ( \pmb \theta ) \star T ( \pmb \theta , t ) \rangle . } \end{array}
$$

The mean MTF $\langle \tilde { T } \rangle$ is written as the normalised mean autocorrelation function of the pupil

$$
\langle \tilde { T } ( \pmb { w } ) \rangle = \frac { \displaystyle \iint G ( \pmb { s } ) G ( \pmb { s } - \pmb { w } ) \langle \psi ( \pmb { s } , t ) \psi ^ { * } ( \pmb { s } - \pmb { w } , t ) \rangle \deg } { \displaystyle \iint G ^ { 2 } ( \pmb { s } ) \mathrm { d } \pmb { s } } ,
$$

where $\textbf { \textit { w } } = \textbf { \textit { r } } / \lambda$ . The second order moment of the complex amplitude of the Dwavefront is given directly by the mean value of the MTF. Limiting discussion to the simple case of a circular pupil, of diameter $D \ \gg \ x _ { \mathrm { c } }$ , the mean MTF, denoted here by $B _ { 0 } ( w )$ , becomes

$$
\langle \tilde { T } ( w ) \rangle \approx B _ { 0 } ( w ) = \exp \left[ - 1 . 4 5 k ^ { 2 } C _ { n } ^ { 2 } \Delta h \left( \lambda w \right) ^ { 5 / 3 } \right] .
$$

Figure 6.11 illustrates the spatial filtering effect of averaged turbulence. The image has lost its high frequencies. The point source response is the FT of $\langle \tilde { T } \rangle$ , and even h ithough an analytic expression has not been given for the image profile, it can be seen that its angular dimension now has order $\lambda / x _ { \mathrm { c } }$ rather than $\lambda / D$ . In other words, the image is smeared by the loss of spatial coherence over the pupil plane. Furthermore, the time averaging effect has removed the agitation from the image, at least as long as the ergodicity hypothesis is justified.

We conclude immediately that increasing the diameter $D$ of the instrument does not give better resolution than an instrument whose diameter is of the order of $x _ { \mathrm { c } }$ , which means a few centimetres at visible wavelengths! The figure also shows the appearance of a characteristic frequency $r _ { 0 } / \lambda$ , which we now discuss.

The Fried Parameter $r _ { 0 } ( \lambda )$

In order to be able to compare with greater precision the diffraction-limited Airy image, described by the intensity $I _ { \mathrm { A } } ( \pmb \theta )$ , with the long-exposure image $\langle I \rangle$ , we calculate the diameter $r _ { 0 }$ of a diffraction-limited circular pupil which would give an image of the same resolution as the image degraded by passing through the atmosphere. Up to now we have related this quantity intuitively to the width at half-maximum of the spreading function of the image. A better and more quantitive definition of the resolution $\mathcal { R }$ is conventionally taken to be

![](images/c0bc3a875178ba71213879a393dcfb756e423f38e38b1e13a9cd31e973834689.jpg)  
Fig. 6.11 MTF of the perturbed pupil. Continuous curve: ideal MTF. Dashed curve: long exposure

$$
\mathcal { R } = \int \langle \tilde { T } ( \boldsymbol { w } ) \rangle \mathrm { d } \boldsymbol { w } \simeq \int B _ { 0 } ( \boldsymbol { w } ) \mathrm { d } \boldsymbol { w } = \int \mathrm { F T } \left[ I _ { \mathrm { A } } ( \pmb { \theta } ) \right] \mathrm { d } \boldsymbol { w } \mathrm { ~ . ~ }
$$

It can be shown that the quantity $r _ { 0 }$ , also called the Fried parameter12 or the linear dimension of the coherence area (spatial coherence being understood), is given by the expression

$$
r _ { 0 } ( \lambda ) = \left[ 0 . 4 2 3 k ^ { 2 } \int _ { 0 } ^ { \infty } C _ { n } ^ { 2 } ( z ) \mathrm { d } z \right] ^ { - 3 / 5 } = 0 . 1 8 5 \lambda ^ { 6 / 5 } \left[ \int _ { 0 } ^ { \infty } C _ { n } ^ { 2 } ( z ) \mathrm { d } z \right] ^ { - 3 / 5 } .
$$

This quantity can be calculated directly from the turbulence and is sufficient to determine the perturbed image, a spot whose diameter is of order $\lambda / r _ { 0 }$ . The angle $\Delta \theta = \lambda / r _ { 0 }$ is often called the seeing angle, or simply the seeing. It is thus the size Dof star images on a photographic plate or CCD when a long exposure is made.

Note a key point here, namely that $r _ { 0 }$ is highly chromatic, varying as $\lambda ^ { 6 / 5 }$ . For example, $r _ { 0 } ( 0 . 5 ~ \mu \mathrm { m } ) ~ = ~ 1 0 ~ \mathrm { c m }$ implies $r _ { 0 } ( 2 0 ~ \mu \mathrm { m } ) = 8 . 4 ~ \mathrm { m }$ . Hence, a telescope like one of the $8 . 2 \textrm { m }$ D Dtelescopes at the VLT, while highly perturbed in the visible, is almost completely unperturbed in the mid-infrared. Consequently, for a given diameter, a telescope will give images closer to the diffraction limit in the infrared than in the visible.

# Short-Exposure Images

Consider now an instantaneous image, the intensity distribution observed over an integration time which is short compared with $\tau _ { \mathrm { c } }$ . The atmosphere can thus be considered as ‘frozen’ here.

The turbulent medium produces a complex MTF, with a random phase whose mean is zero for frequencies above $r _ { 0 } / \lambda$ . Only the mean value of the modulus of the MTF may be non-zero. Hence,

$$
\begin{array} { c } { { \displaystyle { \langle | \tilde { T } ( \pmb { w } ) | ^ { 2 } \rangle = \frac { 1 } { A ^ { 2 } } \iint \langle \psi ^ { * } ( s ) \psi ( s - \pmb { w } ) \psi ^ { * } ( s ^ { \prime } - \pmb { w } ) \psi ( s ^ { \prime } ) \rangle } } } \\ { { \times G ( s ) G ( s - \pmb { w } ) G ( s ^ { \prime } ) G ( s ^ { \prime } - \pmb { w } ) \mathrm { d } s \mathrm { d } s ^ { \prime } , } } \end{array}
$$

where $s = r / \lambda$ is the running variable in the pupil plane, and $A$ the area of the pupil Din units of $r / \lambda$ . The fourth order moment of the complex amplitude $\psi$ appears. If $| w | \gg r _ { 0 } / \lambda$ , then $\psi ( s )$ and $\psi ( s - w )$ can be regarded as decorrelated, in which j j 	case the expression in $\langle ~ \rangle$ under the integral sign becomes

$$
\langle \rangle = \langle \psi ^ { * } ( s ) \psi ( s ^ { \prime } ) \rangle \langle \psi ( s - w ) \psi ^ { * } ( s ^ { \prime } - w ) \rangle \simeq B _ { 0 } ^ { 2 } ( s - s ^ { \prime } ) .
$$

This leads to

$$
\begin{array} { c } { { \langle | \tilde { T } ( w ) | ^ { 2 } \rangle \simeq \displaystyle \frac { 1 } { A ^ { 2 } } \iint B _ { 0 } ^ { 2 } ( s - s ^ { \prime } ) G ( s ) G ( s - w ) G ( s ^ { \prime } ) G ( s ^ { \prime } - w )  { \mathrm { d } } s  { \mathrm { d } } s ^ { \prime } } } \\ { { \simeq \displaystyle \frac { 1 } { A ^ { 2 } } \int G ( s ) G ( s - w )  { \mathrm { d } } s \int B _ { 0 } ^ { 2 } ( u ) G ( s - u ) G ( s - u - w )  { \mathrm { d } } u ~ . } } \end{array}
$$

Moreover, if the condition $D \gg r _ { 0 } ( \lambda )$ holds, then

$$
\int B _ { 0 } ^ { 2 } ( u ) G ( s - u ) G ( s - u - w ) \mathrm { d } u \sim \int B _ { 0 } ^ { 2 } ( u ) \mathrm { d } u = \sigma B _ { 0 } ^ { 2 } ( \mathbf { 0 } ) = \sigma \ ,
$$

where $\sigma$ is the Fried coherence area, $\sigma = 0 . 3 4 2 ( r _ { 0 } / \lambda ) ^ { 2 }$ .

The remarkable expression

$$
\langle | \tilde { T } ( w ) | ^ { 2 } \rangle \simeq \frac { \sigma } { A } \frac { \displaystyle \int G ( s ) G ( s - w ) \mathrm { d } s } { A } = \frac { \sigma } { A } \tilde { T } _ { 0 } ( w )
$$

is illustrated in Fig. 6.12. $\tilde { T } _ { 0 } ( w )$ is the unperturbed pupil transfer function. High spatial frequencies, between the long-exposure cutoff frequency $r _ { 0 } / \lambda$ and the cutoff frequency $D / \lambda$ of the unperturbed pupil, are transmitted, but attenuated in a constant ratio. Note that the square $\langle | \tilde { T } ( w ) | ^ { \bar { 2 } } \rangle$ is proportional to $\tilde { T } _ { 0 }$ , and not to its square $\tilde { T } _ { 0 } ^ { 2 }$ .

hj j iWhat then is the instantaneous image $I ( \pmb \theta , t )$ of a quasi-point source, such as an unresolved star? The star is unresolved if the wave in the absence of turbulence is coherent on a scale greatly exceeding that of the pupil. $I ( \pmb \theta , t )$ is then the FT of an instantaneous instance of the random quantity $\bar { \tilde { T } } ( \dot { w } )$ . It is a random intensity distribution in the focal plane (Fig. 6.13, see also Fig. 6.28c). The presence of bright and dark speckles reveals the existence of high spatial frequencies. From one image to another, these speckles move randomly, and their superposition over a period of time produces the mean long-exposure image described earlier. This image could also be interpreted as the pattern of the (Fraunhofer) diffraction at infinity of the random phase perturbations produced at the pupil by crossing the turbulent medium.

![](images/3a6b9666e0bd4c81d332b313520c4c234cee3d71bc58b5b6eeaa6ceedf3c0fc3.jpg)  
Fig. 6.12 MTF of the perturbed pupil for short exposure. Note the attenuated but non-zero transmission at high frequencies. The ordinate scale is logarithmic

![](images/bada415c1c199a6ec71ce3bc432815f21e2cdca32f357ee114fde1df7a389008.jpg)  
Fig. 6.13 Speckles. Note the distribution of coherence over the pupil, and the distribution of intensity over the image, as well as the sizes of the various patterns

Laser Speckles. Scattering of a laser beam, which is, of course, coherent, by an irregular surface, gives the same granular appearance when viewed at infinity, because of the random interference of the scattered waves.

In 1970, while observing the image of Betelgeuse $\overset { \cdot } { \alpha }$ Ori) with a large telescope, Antoine Labeyrie13 noted the presence of similar structures and deduced that the high frequency information was being degraded, but was not completely eliminated from the image, whence it might be possible to reconstitute it. This fundamental observation was the starting point for speckle interferometry, followed by a whole series of parallel methods, e.g., shift and add (see Sect. 9.6). It subsequently contributed (as of the 1980s) to the development of adaptive optics, to be discussed in the next section.

Isoplanatic Patch

Consider the instantaneous images of the two components 1 and 2 of a binary star, with angular separation $\alpha$ . Each image will exhibit speckles, each corresponding to a wavefront perturbed by slightly different atmospheric layers, depending on the angle $\alpha$ . Indeed, the degree of similarity of the two simultaneous instantaneous MTFs $\widetilde { T } _ { 1 } ( w )$ and $\widetilde { T _ { 2 } } ( w )$ will depend on the value of $\alpha$ . Quantitatively, their average correlation $C _ { T } ( \alpha ) \ \propto \ \left. T _ { 1 } \otimes T _ { 2 } \right.$ over time will give a measure of this similarity. / h ˝ iFor example, the width at half-maximum of $C _ { T } ( \alpha )$ defines the isoplanatic angle $\alpha _ { 0 }$ of the atmosphere in the given state. By a similar calculation to the one leading to $r _ { 0 } ( \lambda )$ , it can be shown that

$$
\alpha _ { 0 } ( \lambda ) = 0 . 3 1 4 { \frac { r _ { 0 } ( \lambda ) \cos \gamma } { \bar { h } } } ,
$$

where the angle $\gamma$ is the zenith distance of the viewing direction and $\bar { h }$ a weighted altitude for the vertical distribution of turbulence. In the simple case where there is only one thin turbulent layer at altitude $h$ , we deduce immediately that, in the vertical direction, $\alpha _ { 0 } ( \lambda ) = r _ { 0 } ( \lambda ) / h$ .

Like $r _ { 0 }$ D, the isoplanatic patch defined by $\alpha _ { 0 }$ is highly chromatic. All things being equal, we understand intuitively that this field will depend on the altitude distribution of the turbulent layers. If the turbulence is limited to layers close to ground level, as happens on Antarctic Dome C, for example, $\alpha _ { 0 }$ will be large. Typical values at $0 . 5 ~ { \mu \mathrm { m } }$ are $\alpha _ { 0 } ~ \approx ~ 5 – 1 0$ arcsec. These considerations are very important in adaptive optics. Indeed, when images are processed after observation, we shall show in Sect. 9.6 how much the processing differs when the effect of the instrument is a simple convolution of the object in the whole observed field (isoplanicity) and when this is not the case (outside this region).

The impact of a turbulent layer or region on propagation, and hence on an image, is not only relevant for propagation through the atmosphere. Radioastronomers have observed interplanetary and interstellar scintillation affecting the intensity received from a source by radiotelescopes. As for the ionosphere, this phenomenon is caused by electron density fluctuations in the interplanetary or interstellar plasma, the intensity of the fluctuation depending on the angular size of the source. It was through such measurements back in 1950 that the first upper limit to the size of the Cygnus A radiosource, discovered slightly earlier, could be obtained.

# Speckle Interferometry

Speckle interferometry14 is a method for restituting the unperturbed image, or some of its characteristics. This method played an important role in the years 1975–1990, but it has now been largely superseded by adaptive optics, to which it made a significant contribution. However, it may make a comeback in ground-based midinfrared observation by large telescopes.

Let $I _ { 0 } ( \pmb \theta )$ be an arbitrary source whose image we wish to determine. The image is given by the convolution

$$
\begin{array} { r } { I ( \pmb \theta ) = I _ { 0 } ( \pmb \theta ) \star T ( \pmb \theta ) ~ , } \end{array}
$$

and hence

$$
\big \langle \big | \tilde { I } ( w ) \big | ^ { 2 } \big \rangle = \big | \tilde { I } _ { 0 } ( w ) \big | ^ { 2 } \Big \langle \big | \tilde { T } ( w ) \big | ^ { 2 } \Big \rangle \ .
$$

If stationarity conditions are satisfied, it suffices to evaluate $\langle | \tilde { T } ( \pmb { w } ) | ^ { 2 } \rangle$ by observing hj j ia point source (in practice, an object that is not resolved by the given telescope) in some arbitrary direction, but at the same $r _ { 0 }$ , in order to be able to write

$$
| \tilde { I _ { 0 } } ( w ) | = \left[ \frac { \langle | \tilde { I } ( w ) | ^ { 2 } \rangle _ { \mathrm { o b s e r v e d } } } { \langle | \tilde { T } ( w ) | ^ { 2 } \rangle _ { \mathrm { o b s e r v e d } } } \right] ^ { 1 / 2 } .
$$

This gives the modulus of the spatial spectrum up to the cutoff frequency $D / \lambda$ of the pupil, assuming only that $\langle | \tilde { T } ( \pmb { w } ) | ^ { 2 } \rangle$ can be found with a good signal-to-noise ratio. hj j iBy the Wiener–Khinchine theorem (see Appendix A), this is equivalent to finding the average autocorrelation function of the image.

In the visible, the resolution at the diffraction limit has been reached by this method. Examples are the separation of binary stars, or the determination of stellar diameters. At $\lambda = 0 . 5 \mu \mathrm { m }$ , the ultimate, i.e., diffraction-limited, resolution of a $5 \mathrm { m }$ telescope attains $D / \lambda = 2 0$ Dmas $\mathrm { 1 ~ m a s = }$ $1 0 ^ { - 3 }$ arcsec). In the infrared, the increase in $r _ { 0 }$ with $\lambda$ Dimplies that the attenuation factor $\pi r _ { 0 } ^ { 2 } / A$ improves, thus increasing the signal-to-noise ratio, where $A$ is the area of the collecting pupil.

Note that this method of restoring just the modulus $| \widetilde I ( w ) |$ is not perfect. It does not restore $I ( \pmb \theta )$ j Q j, for that would require knowledge of both the amplitude and the phase of $\tilde { I } ( \boldsymbol w )$ , unless the object had circular symmetry. This is not relevant, of course, for the separation of a pair of sources. It can be shown that the phase information in arg $\tilde { I } ( \boldsymbol w )$ is also present in the image and can be restored by the appropriate methods.15

Differential speckle interferometry, or simply, differential interferometry, treats sources whose morphology is wavelength dependent, and indeed this is usually the case for astronomical sources. But here we consider the case in which the quantities $O ( \pmb \theta , \lambda _ { 1 } )$ and $O ( \pmb { \theta } , \lambda _ { 2 } )$ differ greatly for two neighbouring wavelengths $\lambda _ { 1 }$ and $\lambda _ { 2 }$ . This is the situation, for example, where a star is observed at wavelength $\lambda _ { 1 }$ , in the continuous photospheric spectrum, and $\lambda _ { 2 }$ is a chromospheric emission line. The two spectra $I ( \pmb { w } , \lambda _ { 1 } , t )$ and $I ( w , \lambda _ { 2 } , t )$ differ greatly in their wavelength dependence, but are totally correlated temporally if measured simultaneously. They can therefore be compared without loss of information in $w$ , and without loss of angular resolution in the final image. The resolution $\lambda / D$ of the telescope can be reached, or even surpassed (super-resolution), if a priori information about the object $O ( \pmb \theta , \lambda )$ is available and the signal-to-noise ratio in spectral measurements is good enough.

# 6.2.3 Effect of the Atmosphere on Interferometry

In an interferometry configuration (see Sect. 6.4), and if the wave is not perturbed, both the phase and the amplitude of the complex quantity $\tilde { I } ( w = D / \lambda )$ can be measured for different values of $w$ D, so that an image of the object can be reconstructed.

For a telescope array, and in particular for a pair of sub-pupils 1 and 2, the problem is to examine how the atmosphere affects the random phase difference $\ S \phi _ { 1 , 2 } ( t ) = \phi _ { 2 } ( t ) - \phi _ { 1 } ( t )$ it produces between the centers of these sub-pupils. Clearly, D in a stationary atmosphere, the mean value $\langle 8 \phi _ { 1 , 2 } ( t ) \rangle$ will be zero. However, the h iphase excursion will be characterised by the variance (or standard deviation):

$$
\langle | \ S \phi _ { 1 , 2 } ( t ) ^ { 2 } | \rangle = \sigma _ { \phi } ^ { 2 } .
$$

For Kolmogorov turbulence, this standard deviation $\sigma _ { \phi }$ increases with the separation of the sub-pupils. It can be shown by the same method as above that it is then given by

$$
\sigma _ { \phi } = 2 . 6 2 \left[ \frac { D _ { 1 , 2 } } { r _ { 0 } ( \lambda ) } \right] ^ { 5 / 6 } .
$$

This standard deviation saturates at a maximal value when this distance $D _ { 1 , 2 }$ exceeds the external scale $\mathcal { L } _ { 0 }$ of the turbulence. This saturation provides a simple way of measuring $\mathcal { L } _ { 0 }$ at a given site. Later we shall see the extent to which this effect, which randomly translates the interference fringes obtained between the subpupils, perturbs ground-based astronomical observation, at both radiofrequencies and optical frequencies. The so-called phase closure methods provide a way of avoiding to some extent the harmful consequences of this phase noise.

Its quantitative effect on the complex MTF is a random phase rotation. The instantaneous MTF becomes

$$
\widetilde { T } ( w ) \mathrm { e x p } [ \mathrm { i } \Delta \varphi _ { 1 , 2 } ( D , t ) ] \ , \qquad \Delta \varphi _ { 1 , 2 } ( D , t ) \mathrm { r a n d o m p h a s e d i f f e r e n c e } \ .
$$

At radiofrequencies, phase fluctuations are mainly introduced into the wavefront by ionospheric irregularities (Fig. 6.14). At millimetre and infrared wavelengths on the one hand, and visible wavelengths on the other, refractive index fluctuations are

![](images/1eb24fcf52d779221e107ae65a51c36380066521f85ee71577d2b66ec12f8861.jpg)  
Fig. 6.14 Phase evolution (in degrees) due to ionospheric fluctuations, at $\lambda = 6$ cm. Note that the standard deviation is small compared with $1 8 0 ^ { \circ }$

dominated by those of water vapour or the air, as already mentioned. However, water vapour is not without influence at radiofrequencies, particularly at short wavelengths (cm and mm).

Many methods have been developed to restore the phase of the signal, degraded by the atmosphere but essential for good image formation (see Sect. 9.6).

# 6.3 Adaptive Optics

The methods of speckle interferometry show that information concerning the high spatial frequencies $( r _ { 0 } / \lambda \le | \pmb { w } | \le D / \lambda )$ of the source is not completely absent j j 
from the image, despite the spatial filtering effect of the atmosphere. Under certain conditions, it is possible to restore spatial frequencies, filtered by the atmosphere, in real time. This is the aim of adaptive optics. 16

The principle is very simple. Consider the deformed wavefront

$$
\begin{array} { r } { \psi ( \boldsymbol { r } , t ) = \psi _ { 0 } \mathrm { e } ^ { \mathrm { i } \phi ( \boldsymbol { r } , t ) } , } \end{array}
$$

given here for a point source at infinity, without modulation of the amplitude $\psi _ { 0 }$ (no scintillation in moderate turbulence), $\phi ( \boldsymbol { r } , t )$ denoting the phase perturbation introduced by the atmosphere. Naturally, it is assumed that this astronomical source is temporally incoherent. Using a mechanical or electro-optical device, a phase conjugation $\phi ^ { \prime } ( \boldsymbol { r } , t )$ is introduced to give a wave

$$
\boldsymbol { \psi } ^ { \prime } ( \boldsymbol { r } , t ) = \boldsymbol { \psi } ( \boldsymbol { r } , t ) \mathrm { e } ^ { - \mathrm { i } \phi ^ { \prime } ( \boldsymbol { r } , t ) } .
$$

If it were possible to make the exact correction $\phi ^ { \prime } = - \phi , \forall r , t$ , the device would be D  8perfect and the image perfectly restored to what would have been observed without the signal having crossed the atmosphere. However, various instrumental limitations mean that a phase error remains:

$$
\ S \phi ( \boldsymbol { r } , t ) = \phi ( \boldsymbol { r } , t ) - \phi ^ { \prime } ( \boldsymbol { r } , t ) .
$$

The result is a corrected image, but exhibiting some deviation from the ideal PSF, which would only be limited by diffraction at the pupil.

The problems encountered in adaptive optics vary widely, from measurement of the perturbed wavefront $\psi ( r , t )$ , to choice of the device producing the phase correction $\phi ^ { \prime }$ , assessment of the final image, choice of reference source, and determination of the ultimate potential of the method. We shall consider each of these in turn.

By endowing the eye with an optical system that could vary its focal length (accommodation), nature achieved the first optical device that could be described as adaptive, while maintaining the quality of the image on the retina. In 1953, the American astronomer Harold Babcock suggested correcting for deformations in solar images by analysing the wavefront and introducing phase corrections in real time. However, he never constructed such a device. In 1957, the Soviet physicist V.P. Linnick made a similar proposal, apparently independently. He had the idea of a segmented correcting mirror, and even the idea of an artificial reference source carried by an aircraft (see below). These suggestions were then left by the wayside for some time, partly because it seemed like an impossible dream, and partly because of the difficulty in carrying out the calculations sufficiently quickly in real time. Around 1970, it was taken up again secretly by the US military, but it was in Europe, stimulated by the recent commitment to the Very Large Telescope, that the first astronomical image — of a binary star — was published with corrections made by adaptive optics in 1990.

Between 1990 and 2006, adaptive optics moved forward quickly, and now equips practically all the major Earth-based telescopes, in particular for their near-infrared observations. Indeed, it has become a key technique for future $3 0 { - } 5 0 \mathrm { m }$ telescopes. In addition, many new ideas are emerging, as we shall see below.

# 6.3.1 Wavefront Measurement

This measurement constitutes the first stage of adaptive optics. For convenience, the wavefront is expanded in terms of a proper basis of vectors of the pupil (usually the primary mirror of the telescope):

$$
\phi ( \boldsymbol { r } , t ) = \sum _ { i = 1 } ^ { \infty } a _ { i } ( t ) \boldsymbol { Q } _ { i } ( \boldsymbol { r } ) \mathrm { ~ , ~ }
$$

where $\mathcal { Q } _ { i }$ are the basis vectors (spatial modes). There are infinitely many such orthonormal bases. One of the most commonly used is the set of Zernike polynomials $Z _ { i }$ , which describe the classical optical aberrations in terms of phase and not in terms of rays, as was done in Sect. 5.1.

The Zernike polynomials are defined by:

$$
\begin{array} { l } { { Z _ { n , m , \mathrm { e v e n } } = \sqrt { n + 1 } \ : R _ { n } ^ { m } ( r ) \sqrt { 2 } \cos ( m \theta ) \ : , \qquad m \neq 0 \ : , } } \\ { { \qquad Z _ { n , m , \mathrm { o d d } } = \sqrt { n + 1 } \ : R _ { n } ^ { m } ( r ) \sqrt { 2 } \sin ( m \theta ) \ : , \qquad m \neq 0 \ : , } } \\ { { \qquad Z _ { 0 , n } = \sqrt { n + 1 } \ : R _ { n } ^ { 0 } ( r ) \ : , \qquad m = 0 \ : , } } \end{array}
$$

Table 6.2 The first few Zernike polynomials and corresponding optical aberrations. By convention, the double index $n , m$ of the Zernike polynomials is replaced here by a single sequential index $i$   

<table><tr><td rowspan="2">Radial degree n</td><td colspan="5">Azimuthal frequency m</td></tr><tr><td>m=0</td><td>m=1</td><td>m=2</td><td>m=3</td><td></td></tr><tr><td>0</td><td>Z=1 Piston</td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td></td><td>Z2 = 2r cosα Z3= 2r sinα Tip-tilt</td><td></td><td></td><td></td></tr><tr><td>2</td><td>Z4 =√3 (2r²-1) Defocus</td><td></td><td>Z5 = √6r² sin 2α Z6 = √6r²cos 2α Astigmatism</td><td></td><td></td></tr><tr><td>3</td><td></td><td>Z= 8(3r³ -2r) sinα Zg= 8(3r³-2r) cos α</td><td></td><td></td><td>Z,= √8r3 sin 3α Z10=√8r3 cos 3α</td></tr><tr><td>4</td><td>Z11 =√5 (6r4 -6r² +1) Spherical</td><td>Coma</td><td>Z12=√10 (4r4 - 3r²) cos 2α Z1 =√10 (4r4 - 3r²) sin 2α</td><td></td><td></td></tr></table>

where

$$
R _ { n } ^ { m } ( r ) = \sum _ { s = 0 } ^ { ( n - m ) / 2 } \frac { ( - 1 ) ^ { s } ( n - s ) ! } { s ! [ ( n + m ) / 2 - s ] ! [ ( n - m ) / 2 - s ] ! } r ^ { n - 2 s } ,
$$

and $m$ is the azimuthal frequency, $n$ the radial degree.

Table 6.2 gives the classification, the formula and the equivalent aberrations in classical optics for the first few Zernike polynomials. By convention, the indices $m , n$ are replaced by a single sequential index. This basis is orthogonal on a circular pupil:

$$
\frac { 1 } { \pi } \iint G ( \pmb { r } ) Z _ { i } Z _ { j } \mathrm { d } \pmb { r } = \delta _ { i j } \qquad \mathrm { w i t h } \quad G ( \pmb { r } ) = \Pi \left( \frac { \ d r } { \ d 2 } \right) .
$$

Note, however, that this orthogonality relation does not strictly hold for a telescope pupil which is partially blocked by a central obstruction, such as a secondary mirror, as is often the case.

Now let $\phi ( r , t ) = \phi ( R \rho , \theta , t )$ , where $R$ is the pupil radius. The coefficients $a _ { i }$ of the expansion of $\phi$ in this basis are given by

$$
a _ { i } ( t ) = \iint G ( \boldsymbol { r } ) \phi ( \rho , \theta , t ) Z _ { i } ( \rho , \theta ) \mathbf { d } \boldsymbol { r } ~ .
$$

![](images/f1276aba075d70dfbd7358e10e2ba8ef470b47cb350e85b32eda3c7f61f80f41.jpg)  
Fig. 6.15 Variance (in rad2) of the Zernike coefficients $\big < a _ { i } ^ { 2 } \big >$ , due to Kolmogorov turbulence with infinite external scale $L _ { 0 }$ , where $i$ h idenotes the number of the polynomial. Also shown is the residual phase error (Noll residual), after perfect correction of the first $N$ modes. The values of $\textstyle \left. a _ { i } ^ { 2 } \right.$ and $\Delta _ { N }$ are expressed in units of $[ D / r _ { 0 } ( \lambda ) ] ^ { 5 / 3 }$ , where $D$ is the pupil diameter, and $r _ { 0 }$ h ithe coherence scale of the atmosphere, at the wavelength $\lambda$ at which the phase is being studied. Recall that, to first order, the phase differences result from differences in optical path, and these are achromatic, i.e., not wavelength dependent, in the Earth atmosphere

In the presence of atmospheric turbulence, the $a _ { i }$ are random variables in time, and ergodic, if the turbulence is stationary. The basis $Z _ { i }$ is not quite adequate for projecting the effects of Kolmogorov turbulence. Indeed, the coefficients $a _ { i }$ are not statistically independent, as can be seen by calculating the covariances $\langle a _ { i } a _ { j } \rangle \neq 0$ for certain pairs of values of $i , j$ h i ¤. It may therefore be necessary to choose another basis (the Karhunen–Loeve polynomials, which preserve the non-correlation of the coefficients).

In fully developed (Kolmogorov) turbulence, the variance of each coefficient can be calculated exactly, together with the variance residue $\Delta _ { N }$ , if it is assumed that the phase conjugation has been achieved perfectly for the values $i \leq N$ :

$$
\Delta _ { N } = \big \langle \big | \phi ^ { 2 } \big | \big \rangle - \sum _ { i = 2 } ^ { N } \big \langle a _ { i } ^ { 2 } \big \rangle = \sum _ { i = N + 1 } ^ { \infty } \big \langle a _ { i } ^ { 2 } \big \rangle \ .
$$

Figure 6.15 gives the variance and the residues for the first few values of $N$ . It can be used to calculate the phase error remaining after correction. For large $N$ ${ \it \Omega } > 1 0$ or 20), there is an asymptotic expression

$$
\Delta _ { N } = 0 . 2 9 4 4 N ^ { - \sqrt { 3 } / 2 } \left( \frac { D } { r _ { 0 } } \right) ^ { 5 / 3 } .
$$

Note, in Fig. 6.15, that the first few modes contain a large part of the total variance. If they are imperfectly corrected, then the higher order corrections become superfluous. This is indeed one of the problems to be faced in the design of an adaptive system.

Angular properties are important. Is it possible to use the wavefront coming from a source situated in a certain direction to correct the image of another source, observed in a different direction? This can also be characterised. If two sources are observed, in directions $\pmb \theta _ { 1 }$ and $\pmb { \theta } _ { 2 }$ , the relevant quantity is the angular decorrelation (anisoplanicity)

$$
\left. a _ { i } ( \pmb { \theta } _ { 1 } , t ) a _ { j } ( \pmb { \theta } _ { 2 } , t ) \right. \ .
$$

The correlation decreases more rapidly as $N$ is large and the wavelength $\lambda$ is short. At $\lambda = 1 ~ { \mu \mathrm { m } }$ , the isoplanatic patch of the first ten polynomials is of the order of D10 arcsec for average turbulence.

Measurement of the perturbed phase requires wavefront analysers, applying quality control principles used when polishing optical elements, with the only difference being that here the analyser must necessarily operate in temporally incoherent light. Such analysers include shearing interferometers, and, more commonly, analysers segmenting the pupil into sub-pupils (Shack–Hartmann), which measure the phase gradient $\nabla \phi$ , curvature analysers, which measure the Laplacian $\Delta \phi$ , and rpyramid analysers with broad dynamic range.

Whatever analysis technique is chosen, it suffices to sample the phase discretely on the wavefront, at $N$ regularly located points on the pupil. The bigger the value of $N$ , the smaller will be the residual phase errors. In practice, if these measurements of $\varphi ( { \bf r } , t )$ are made at a specific wavelength $\lambda _ { 0 }$ , a sampling rate of order $r _ { 0 } ( \lambda _ { 0 } )$ , i.e., $\boldsymbol { N } ~ = ~ ( D / r _ { 0 } ) ^ { 2 }$ , is chosen. For example, for a $1 0 \mathrm { ~ m ~ }$ telescope operating at $\lambda _ { 0 } = 1 ~ \mu \mathrm { m }$ with $r _ { 0 } = 5 0 \ \mathrm { c m }$ , a suitable number of measurement points would be $N = 2 0 ^ { 2 } = 4 0 0$ .

D DNote also that, up to a factor of $2 \pi / \lambda$ , $\varphi ( \boldsymbol { r } , t )$ is achromatic. A favourable consequence of this is that the value of $\lambda _ { 0 }$ used for the measurement can be chosen from considerations of experimental convenience (see below) and the correction can thus be applied at a different wavelength.

Tip–Tilt Correction. Figure 6.15 shows that a significant fraction of the phase error comes from the first two terms $( n = m = 1$ , see Table 6.2), which correspond to the image centroid in the D Dimage plane. This is called a tip–tilt fluctuation. The image could thus be significantly improved by correcting for this fluctuation alone. Indeed, this was done very early on in observations of the Sun, in particular by H. Babcock in 1953. More recently, a posteriori processing techniques for short exposure images (see above and Sect. 9.6) have used image refocusing, which superposes short exposure images after refocusing each of them. This yields images equivalent to a long exposure, but with much better angular resolution.

Tip–tilt can be corrected in real time, using a simple mirror that tilts around two axes and thereby hold the image centroid fixed. The tilt angles are continually reassessed by a tip–tilt sensor. This yields an effective and cheap adaptive optics system, although still somewhat rudimentary. This kind of device, useful whenever $r _ { 0 } \le D$ , has even been commercialised to equip amateur telescopes and significantly improve image quality.

![](images/dc1301946a698ab6a0dd8d7ef79c6b46c9518da40843b9c66cca3391f62dd568.jpg)  
Fig. 6.16 Basic setup in adaptive optics. A computer is placed between analysis and control. The dotted line represents a beam splitter (possibly dichroic), dividing the light between wavefront sensor $\left( \lambda _ { 0 } \right)$ and camera measuring the corrected image $( \lambda )$ . The wavefront sensor does not necessarily operate at the same wavelength as the camera forming the corrected image

# 6.3.2 Phase Correction Devices

The standard setup is shown in Fig. 6.16. A thin mirror, whose surface can be deformed by mechanical actuators, reflects the wave to be corrected. Ideally, this would be the primary mirror, but it has too much inertia and it is not possible to make corrections quickly enough. The possibility, discovered recently (2006), of making the correction on the secondary mirror of the telescope is particularly attractive (Fig. 6.17). Whichever mirror is chosen, by forming an image of the pupil on it, the phase correction $\phi ^ { \prime } ( \boldsymbol { r } , t )$ is calculated by computer from measurements made by the wavefront sensor and introduced by means of a servoloop. Various mirror arrangements can be used, e.g., mirrors with actuators, bimorphic mirrors modifying curvature locally, and microelectromechanical systems (MEMS). The aim is generally to reduce the residual phase error below $\lambda / 4$ (Rayleigh criterion), although some applications such as EXAO (see below and Sect. 6.6) may require a lower value. In terms of the Zernike polynomials, this constraint fixes the highest degree that needs to be corrected.

![](images/18805db1757ba8283f8cc793a76dfc5415d9b5610c28124319cbffe6b380f0ed.jpg)  
Fig. 6.17 The first adaptive secondary mirror, with $N ~ = ~ 3 3 6$ actuators, on the $6 . 5 \mathrm { ~ m ~ M M T }$ Dtelescope (Mt. Hopkins, Arizona). This elegant solution, obtained with a very thin $\mathrm { 1 . 8 ~ m m }$ ) and flexible mirror, reduces the optical complexity of the adaptive optics. Minimising the number of optical surfaces, it also reduces the intrinsic thermal emissivity of the instrument

In the particular case of a Shack–Hartmann sensor with $N$ sub-pupils, the mirror must also have $N$ degrees of freedom and the correction is then acquired up to the polynomial of degree $2 N$ . We thus obtain the expression

$$
N ( \lambda ) \approx \left[ \frac { D } { r _ { 0 } ( \lambda ) } \right] ^ { 2 } ,
$$

which is the number of degrees of freedom here. Note that the $\lambda ^ { 6 / 5 }$ dependence of $r _ { 0 } ( \lambda )$ leads to a very rapid decrease in $N$ with increasing $\lambda$ . Corrections are therefore much easier in the infrared.

A second constraint imposed on the deformable mirror is its passband. Indeed, it is inserted in a servocontrol loop that must respond perfectly to temporal phase variations, which themselves have the characteristic time $\tau _ { \mathrm { c } } ( \lambda _ { 0 } )$ , fixed by the atmosphere and also varying as $\lambda ^ { 6 / 5 }$ . Since a servocontrol system must always have a much broader passband (greater by a factor of 10) than the phenomenon to be corrected, i.e., around $1 0 / \tau _ { \mathrm { c } }$ , the deformable mirror must respond to frequencies of several kHz.

# 6.3.3 The Final Image

The quality of the final image can only be completely assessed by examining its profile $I ( \pmb \theta )$ , in order to compare it with the profile of the ideal image. Since the correction is never perfect, the profile of the instantaneous image exhibits random fluctuations (residual speckles), whereas these are averaged out in the long exposure image. When the correction is reasonably good, the long exposure profile generally exhibits a core very close to the Airy profile (the diffraction limit), surrounded by a halo due to the non-corrected phase residues $\ S \phi$ (Fig. 6.18). As this residue increases, the proportion of energy in the core is attenuated in favour of the halo, until the classic uncorrected long-exposure image in the presence of seeing is reached (see above). Hence the terms partial and total correction. This correction is quantified by the Strehl ratio $\mathcal { S }$ . The Strehl ratio of the image of a point source is defined as the ratio of the maximal intensity of the corrected image to the maximal intensity of an image limited only by diffraction at the wavelength considered. It is given by

![](images/95c4b613798e56ae12967cec2f6b683cb8cd528b75f14022df123fc795838adb.jpg)  
Fig. 6.18 Image of the unresolved star HIC69495 $\mathrm { \Delta } m _ { \mathrm { V } } = 9 . 9$ ) in the K photometric band $( 2 . 2 \mu \mathrm { m } )$ Dwith a 100 s exposure time, displayed on a logarithmic scale. This (PSF) was obtained using the multi-application curvature adaptive optics (MACAO) system that has equipped each of the $8 . 2 \mathrm { ~ m ~ }$ telescopes of the VLT since 2003. The mirror has deformable curvature and includes $N \ = \ 6 0$ actuators. The Strehl ratio is $\mathcal { S } = 0 . 5 5$ and the image FWHM reaches 0.06 arcsec. D DThis remarkable image clearly shows the three first Airy diffraction rings. Document European Southern Observatory

$$
\mathcal { S } = \frac { \displaystyle \int \tilde { S } ( w ) \mathrm { d } ^ { 2 } w } { \displaystyle \int \tilde { T } _ { \mathrm { d i f f } } ( w ) \mathrm { d } ^ { 2 } w } ,
$$

and varies from 1, for total correction, to less than $1 0 ^ { - 3 }$ , for a highly speckled image.

Figure 6.19 shows the result of an adaptive correction carried out on the image of a double star.

![](images/aca50fe8f65bbdb1b3d7e30f5b9ea7859d8dc0f8f90048bd5a0595ba0c5c53e8.jpg)  
Fig. 6.19 Birth of adaptive optics. Image of a binary system (magnitude $m _ { \mathrm { v } } = 1 3 . 1$ , separation $0 . 5 9 ^ { \prime \prime }$ ) using a $3 . 6 \mathrm { m }$ telescope at wavelength $1 . 6 5 \mu \mathrm { m }$ D (European Southern Observatory, La Silla, Chile). Right: Image affected by atmospheric turbulence (seeing $1 . 7 ^ { \prime \prime }$ ). Left: Corrected image, exposure time $1 0 \mathrm s$ , final resolution $0 . 1 2 ^ { \prime \prime }$ (FWHM), 1 pixel $= 5 0$ mas. Adaptive system Come-On DPlus, 1993. (Picture by Beuzit J.L., Paris Observatory and ESO)

# 6.3.4 Sensitivity and Reference Sources

The operation of the servoloop in an adaptive optics system depends on the quality of information received from the wavefront sensor and transformed into commands to the degrees of freedom of the active mirror. The signal-to-noise ratio of this command is thus critical. Naturally, it depends on the magnitude of the source under observation and the sensitivity of the detector equipping the analyser. There will clearly be a limiting magnitude beyond which it is no longer possible to close the loop. This is the Achilles heel of adaptive optics, limiting its application to relatively bright objects. It led to the development of a laser guide star or artificial reference source. The wavelengths $\lambda _ { 0 }$ and $\lambda$ for analysis and measurement of the image, respectively, can differ, provided that the condition $\lambda _ { 0 } ~ \le ~ \lambda$ is satisfied, in order to correctly measure high spatial frequencies.

The ideal detector, associated with the wavefront sensor, must have a quantum efficiency $\eta$ as close as possible to unity and a response time compatible with the atmospheric turbulence, characterised by correlation times which vary from $\tau _ { \mathrm { c } } \approx 1$ to $1 0 0 \mathrm { m s }$ , depending on the value of $\lambda _ { 0 }$ , and the cause of the turbulence (e.g., wind, convection). Avalanche diodes $\eta \approx 0 . 8 )$ , EB-CCDs in counting mode $\qquad \eta \approx 0 . 0 8 )$ , or rapid low-noise CCDs, which are difficult to make $\eta \approx 0 . 6 )$ , can be used (see Sect. 7.4.6 for more about these detectors).

When specifying an adaptive optics system, the first step is to fix the number of modes one would like to correct at a given wavelength and under given turbulence conditions. This determines the number $N$ of actuators required for the deformable mirror and the number of sub-pupils of the analyser (almost the same). Once the properties of the analyser are established, it is straightforward to calculate the Strehl ratio obtained for a source of given magnitude $m _ { \lambda _ { 0 } }$ . The fainter the source, the more difficult it is to correct the high modes (or spatial frequencies), since the signalto-noise ratio in the measurement of the variance of these modes tends to decrease. Under reasonable hypotheses, Fig. 6.20 shows the correction prospects as a function of the magnitude of the observed object. It can be seen that a high quality correction requires a magnitude $m _ { \mathrm { V } }$ less than 13–14. In fact, taking sensor performances into account, the spectral band R is often chosen for the analyser, rather than V.

![](images/b0d59f469d058c646af1695219b45e28864b5a85b96df4ae683ce5bc853e9605.jpg)  
Fig. 6.20 Sensitivity of adaptive optics. Ordinate: Strehl ratio $\mathcal { S }$ for an image corrected at $\lambda =$ $2 . 2 \mu \mathrm { m }$ (spectral band $K$ ), in average turbulence conditions. Abscissa: Magnitude $m _ { \mathrm { V } }$ Dof the source used by the wavefront analyser (hence analysis wavelength $\lambda _ { 0 } = 0 . 5 5 \mu \mathrm { m } ,$ ). We assume here that Dthe sensor is equipped with a detector with high quantum efficiency (CCD, $\eta = 0 . 6 )$ ) and a very low readout noise $2 \mathrm { e } ^ { - }$ rms). From Gendron E., doctoral thesis, 1995

Note here that the diameter of the telescope is irrelevant. Indeed, the light intensity available in each sub-pupil of the analyser is the determining factor, and that only depends on the value of the Fried parameter $r _ { 0 } ( \lambda )$ .

# Choice of Reference

All the above reasoning is based on the initial assumption that the observed source is a point, or at least, not resolved at the diffraction limit of the telescope. Can adaptive optics be used to correct the image of an extended and resolved source $S$ ? The answer is affirmative, but two cases need to be considered:

• In the immediate vicinity of the source $S$ , there is another source $R$ , called the reference, which is a point source bright enough and close enough to $S$ to ensure that the correlation between the waves $\psi _ { S } ( \pmb { r } , t )$ and $\psi _ { R } ( r , t )$ is good: $R$ is in the isoplanatic patch of $S$ , whose value was specified above, i.e., several tens of arcsec under suitable observing conditions. The wavefront analyser calculates the correction at $\lambda _ { 0 }$ by observing $R$ , and the camera forms the image at $\lambda$ of the chosen object $S$ . When there is no such nearby source, the only solution would be to use $S$ itself as reference. But is that possible when $S$ is resolved? Although this may seem paradoxical, the answer is affirmative, provided that the angular size of $S$ is significantly smaller than the size of the isoplanatic patch. Indeed, $S$ may then be treated as comprising an ensemble of point sources, detected by the analyser and all suffering the same phase perturbation. The measurement made by the analyser does indeed then determine this phase perturbation globally for S. In practice, it is the field accepted by each of the sub-pupils of the analyser (generally 2–3 arcsec) which fixes the maximal acceptable size of $S$ for the adaptive optics system to work properly.

How could adaptive optics be applied to observation of the Sun, which is a very large object? The idea here is to use very small details on the solar surface as reference, provided that they contrast sufficiently with their neighbourhood, e.g., granules, faculae, or spots. The results are spectacular.17

# Artificial Reference: Laser Guide Star

Given the isoplanatic patch for a given wavelength $\lambda _ { 0 }$ , together with the density of stars of adequate magnitude to reach a given value of the Strehl ratio $\mathcal { S }$ , it is easy to show that the sky coverage obtained by an adaptive optics system is low, of the order of a few percent at best. This nevertheless gives access to many valuable observations of stars and galactic objects, although only a small number of extragalactic objects, which are rather faint and rarely come with a bright star that could serve as reference, especially in the vicinity of the galactic pole. It was thus necessary to create an artificial reference star that could be set up at will not far from the object $S$ whose high resolution image is to be obtained.

This idea, first proposed by V.P. Linnik in 1957, then shelved for thirty years, was picked up again by R. Foy and A. Labeyrie (France) in 1987, in the following form. In the Earth atmosphere, there is a layer at an altitude of about $8 0 ~ \mathrm { k m }$ containing a high density of sodium (Na) atoms. These atoms are deposited there, and regularly refreshed, by meteoritic particles bombarding the Earth. If a laser beam of wavlength $\lambda ~ = ~ 5 8 9 . 3 ~ \mathrm { n m }$ is shone from the ground up to this layer, Dit locally excites the sodium resonance transition, which has a particularly high absorption cross-section. The spontaneous emission of atoms returning to their ground state can then be observed from the ground, and provides an almost point source of monochromatic light which is easily picked out from the atmospheric light background by spectral filtering. This source, which is thus like an artificial star, can then be used as reference for a wavefront analyser, provided that the laser power is high enough to give it a sufficient magnitude. Aligned with the telescope, it can be positioned with great accuracy in the immediate vicinity of the observed source. The first truly astronomical laser guide star was set up on the $3 . 5 \mathrm { ~ m ~ }$ Calar Alto telescope (Max Planck Institut f¨ur Astronomie, Spain) in 1996 (the US military having pursued their own investigations in the meantime).

Although the idea of an artificial laser guide star (LGS) is an attractive one, several problems arise in comparison with a natural guide star (NGS):

• The reemitted light must come back through the same turbulent layers as the light emitted by the source $S$ , situated effectively at infinity. But since the sodium layer is at an altitude of $8 0 { - } 9 0 ~ \mathrm { k m }$ , this condition is not entirely satisfied, giving rise to a geometric cone effect which reduces the quality of the correction. This can be partially corrected by using several laser spots in the field. The laser light goes up through the atmospheric layers and the reemitted light comes back down through the same layers, whence the tip–tilt effects on the wavefront are suffered twice in opposite directions and therefore cancel. While these effects dominate the image perturbation, they escape measurement here and are thus left uncorrected. The first method for dealing with this, which is still employed, is to use a natural star to measure those, taking advantage of the large isoplanatic patch associated with tip–tilt (several arcmin), which improves the chances of finding a star there of adequate magnitude. Other, more subtle methods are under investigation, e.g., using photons that are backscattered at different wavelengths in combination with the very slightly chromatic character of the tip–tilt affecting their images. Finally, given the remoteness of the sodium layer, the power required of the laser is very high (typically around $1 0 \mathrm { ~ W ~ }$ continuous wave), and the laser must be carried by the telescope, and accurately aligned parallel to the telescope axis. This is why another kind of artificial star known as a Rayleigh star has been under investigation. These are formed by Rayleigh backscattering from atmospheric molecules in the lower atmosphere. The resulting correction is then only valid for turbulence occurring very close to the telescope aperture.

Despite these limitations, many instruments at the time of writing (2006) are equipped with a laser and adaptive optics, as exemplified by the Keck Telescope (Hawaii) in 2004, the European VLT in 2005 (see Fig 6.21), Gemini South (Chile) in 2007, and others.

![](images/5b499929d089affeb2f28c90d9462ad074360006804d23eefb19c22392bddd85.jpg)  
Fig. 6.21 At the Paranal site in Chile, the Yepun telescope of the VLT is equipped with a laser producing an artificial guide star, used as a reference for NAOS adaptive optics. Image kindly provided by Stefan Seip (astromeeting.de) and insert by T. Ott, ESO

# 6.3.5 New Concepts

The above discussion highlights the principles and difficulties of adaptive optics. Since such systems will be absolutely essential for telescopes with diameters in the range $3 0 { - } 5 0 ~ \mathrm { m }$ , currently planned for ground-based observation, every attempt is being made to improve them in any way possible. The emergence of new potential sites with very different turbulence characteristics, such as the Antarctic (see Sect. 2.8) where turbulence is almost exclusively restricted to the immediate vicinity of ground level, considerably changes the conditions for setting up an adaptive optics system.

# Multi-Conjugate Adaptive Optics (MCAO)

Multi-conjugate adaptive optics (MCAO) is a version of adaptive optics exploiting the fact that the phase error $\varphi ( \boldsymbol { r } , t )$ is the sum total of effects produced in the different atmospheric layers encountered, whence the adaptive optics correction will be improved if the effect of each layer can be corrected by a different deformable mirror, whose surface is optically conjugate to the position of the layer (since these layers are not at infinity, their images thus form at different positions within the telescope). Figure 6.22 shows the general principle and Figure 6.23 a detailed MCAO simulation. In practice, it suffices to correct two or three layers separately by creating the same number of artificial stars (because of the geometric effect) to significantly improve the final correction.

![](images/4bfae75c3b02c3537dfb9d9b87d9209b06d80c76f405e49766a4743602e8024c.jpg)  
Fig. 6.22 General setup for multi-conjugate adaptive optics (MCAO). The two deformable mirrors DM1 and DM2 are optically conjugate to the two atmospheric layers 1 and 2 to be corrected for — usually the layer close to ground level and another higher up, at $8 { - } 1 0 \mathrm { k m }$ — while the wavefronts from the two spatially distinct laser guide stars are analysed by two wavefront sensors (WFS). The calculator uses these measurements to deduce the corrections to be applied to the two mirrors. Diagram kindly provided by F. Rigaut, 2006

![](images/c0a84767ef995bb4eda56e56437b702450b182fd539a228a87e69b5b6f1254ff.jpg)  
Fig. 6.23 Simulation of multi-conjugate adaptive optics operating in spectral band H $\begin{array} { r l } { \lambda } & { { } = } \end{array}$ $1 . 6 5 \mu \mathrm { m }$ D) and designed for the Gemini South telescope (Chile). The field is 150 arcsec (2.5 arcmin). (a) Uncorrected image of star field. (b) Image corrected by conventional adaptive optics. Note the significant anisoplanicity of the correction, with lengthened images as one moves off the axis. (c) Image corrected by multi-conjugate adaptive optics. The quality of the correction is restored practically throughout the field. Document kindly provided by F. Rigaut, 2006

# Ground Layer Adaptive Optics (GLAO)

Ground layer adaptive optics (GLAO) is a version specifically designed to correct for the effects of turbulence close to ground level, noting that in certain sites this largely dominates image degradation. In this case, the isoplanatic patch can be much larger, since to a first approximation it is trivially given by

$$
\alpha _ { \mathrm { i s o } } ( \lambda ) = \frac { r _ { 0 } ( \lambda ) } { H } ,
$$

where $H$ is the altitude of the dominant layer. The correction is clearly more limited here (smaller value of $\mathcal { S }$ ), but the corrected field can easily reach several arcmin. This version of adaptive optics is highly promising for use in the Antarctic (Dome C), where most turbulence occurs very close to ground level, within about $5 0 \mathrm { m }$ at most.

# Multi-Object Adaptive Optics (MOAO)

Multi-object adaptive optics (MOAO) is a technique designed for the study and high-resolution imaging of galaxies, in regions where there are many galaxies in the field of view. It is inspired by the technique of multi-object spectroscopy described in Chap. 8. A corrective microsystem is installed by means of a moving arm on the image of each galaxy.18 Each corrector contains only a small number of actuators, so the correction remains limited, although it may nevertheless represent an order of magnitude in resolution compared with the image obtained without adaptive optics, enough to be able to carry out a spectrographic analysis of different regions of the galaxy, e.g., to determine its rotation. The perturbed phase is measured simultaneously on several stars in the field in order to improve the signal-to-noise ratio, with the correction calculator adapting the latter to each point of the field to be corrected.

# Extreme Adaptive Optics (EXAO)

When the correction gives a Strehl ratio $\mathcal { S }$ greater than about 0.6, the core of the image and also the first rings are practically identical to those of a diffraction-limited image. However, the uncorrected residual phase $\delta \varphi$ produces a halo around the core, with random intensity fluctuations in the instantaneous images. These average out in the long exposure image to produce a uniform halo, with an intensity that is never less than about one thousandth of the peak intensity and which makes it impossible to detect a faint object close to the star, e.g., an exoplanet. Coronagraphy techniques (see Sect. 6.6) aim at such detections, but operate better if the halo is reduced.

To reduce it, the number of corrected Zernike modes must be increased, and hence likewise the number $N$ of sub-pupils and correction actuators. This is what is provided by extreme adaptive optics systems. For example, in the near infrared (spectral bands J, H, and K) and for a $1 0 ~ \mathrm { m }$ telescope, using a mirror with 4 000 actuators (MEMS), it seems possible, over a very small field (about one arcsec), to obtain a value of $\mathcal { S }$ greater than 0.9, and to reduce the halo intensity of a bright star $( m _ { R } \approx 6 - 7 )$ to $1 0 ^ { - 7 }$ at a distance of a few times $\lambda / D$ from the central peak.

Adaptive optics has considerably improved the possibilities for observation using large ground-based visible and near infrared telescopes. Some have even claimed, perhaps with a slight exaggeration, that it represents the greatest revolution in Earth-based optical observation since Galileo. In any case, the growing diameters of telescopes, already over $1 0 ~ \mathrm { m }$ , can now be accompanied by a growth in angular resolution. Apart from the gain in resolution, the possibility of reducing the size of the PSF has many consequences. To name but a few:

• Improved contrast in images of unresolved objects in the presence of a background, and hence a gain in signal-to-noise ratio.   
Coronagraphy.   
Reduced size of spectrometer slits for the same spectral resolution.   
Possibility of injecting the image directly into single-mode optical fibres for interferometric applications.   
• Reduced confusion in rich fields, e.g., globular clusters.

The often highly accurate knowledge of the point source response (PSF) provided by adaptive optics allows elaborate data processing of corrected images such as deconvolution, which can improve the quality. This point will be discussed further in Sect. 9.6.

To end this section, which deals with a rapidly evolving field, let us mention one of the most outstanding results obtained to date: the observation of stellar orbits very close to the center of the Galaxy, leading to a determination of the mass of the black hole which is very likely located there (Fig. 6.24).

![](images/50a24308c4afc2758b83318ae6777f14e5f80264bb5ec7ff3ec90f15739a8be9.jpg)  
Fig. 6.24 Observation of the galactic centre using NAOS adaptive optics on the Very Large Telescope. Image obtained at $\lambda = 3 . 5 ~ { \mu \mathrm { m } }$ (spectral band $\mathrm { ~ L ~ } ^ { \prime }$ ), in a field of $2 1 . 9 \times 2 1 . 9$ arcsec D corrected by adaptive optics. The intensity scale is logarithmic. Insert: Magnification of the central $2 \times 2$ arcsec region around the star S2 $( \bigcirc )$ marked by two dashes in the main image and close to the central radiosource $\mathrm { S g r A ^ { * } }$ $( \sqsubseteq )$ -. The mass of the central black hole has been estimated by monitoring the motion of this star, knowing the distance from the galactic center to the Sun. Document kindly provided by Y. Clenet, in collaboration with R. Genzel, 2004´

# 6.4 Astronomical Interferometry

We saw earlier that two sub-pupils 1 and 2 sampling the wavefront from the source at two points a distance $D$ apart works like a bandpass spatial filter, whence it is possible to measure the Fourier components of the source. By varying $D$ , the spatial spectrum of the source is then explored point by point, whereupon its image can be reconstructed in principle, with a spatial resolution that is then only limited by the maximal value of $D$ .

It was the insuperable limitation imposed by the diameter of the primary mirror of the telescope, for technological (optical and mechanical) reasons, which led to the development of astronomical interferometry. It all began with a remarkable analysis by Hippolyte Fizeau in 1868, followed by the first attempts to measure star diameters by Edouard Stephan in 1874. The latter only obtained an upper limit because his telescope was too small. It was Albert Michelson who first measured the diameters of the the Galilean moons of Jupiter (1891). Then 20 years later at Mt. Wilson (California), Francis Pease succeeded in measuring the diameters of several stars, including Betelgeuse (˛ Ori) (Fig. 6.8). Only the extraordinary talents of Michelson seemed able to overcome the extreme experimental difficulties (due to vibrations) of maintaining the coherence of the light in two optical paths. But after this success, optical interferometry stopped in its tracks for half a century (apart from one particular form, namely homodyne interferometry, discussed below).

During World War II, radar operators noticed that the radar echos reflected from an aircraft varied in amplitude. The reason was that there was interference between the direct signal and a signal reflected by the mirror surface. This phenomenon, well known in optics (Lloyd mirrors), resulted in a maritime interferometer in Australia (1946): with a resolution of 30 arcmin, observation of the Sun showed that the variable emission that had been noticed came from a region that was too small for the emission to be non-thermal.19 This was the beginning of radio interferometry. And it was at radiofrequencies that it continued. In 1946, in Cambridge (UK), Martin Ryle20 was working at decimetre wavelengths, where it was much easier from the experimental point of view to maintain coherence. A series of radio interferometers was used to catalogue the positions of newly discovered radiosources (catalogues 1C–4C). The wavelength decreased gradually from the metre to the centimetre, sensitivity improved, baselines extended to culminate in the Five Kilometer Radiotelescope, and aperture synthesis came gradually into being.

The technique developed very quickly and the harvest of results was rich, resulting in a large family of radiotelescope arrays. Between 1921, when the Mt. Wilson telescope was successfully used in interferometric mode by Michelson and Pease, and 1975, when the young French astronomer Antoine Labeyrie obtained his first fringes from the star Vega, optical interferometry was never completely abandoned. The main problem was to measure star diameters, where almost no progress had been made since the measurements by Pease. The methods of phase closure, optical telescope arrays, pupil masking (already used by Edouard Stephan in 1874) were discussed (D. Currie). In 1970, at the Pulkovo observatory (Crimea, USSR), E.S. Kulagin published a measurement of the orbit of the star Capella made with a Michelson type interferometer, using a $6 \mathrm { m }$ baseline. He thus preceded Labeyrie by a few years. In parallel, the homodyne method was put into practice by Robert Hanbury-Brown and Robert Twiss at Jodrell Bank (UK) in 1956, then in Australia where they measured the diameters of Sirius and a few other bright stars. Finally, in 1972, Jean Gay at the Paris Observatory successfully applied the radiofrequency heterodyne technique in the mid-infrared $( 1 0 . 6 \mu \mathrm { m } )$ ). This approach had also been developed by Charles Townes21 and his students at Berkeley (United States).

This work renewed interest in astronomical interferometry in the optical (visible and infrared) region, leading to considerable progress in angular resolution, and the construction of several arrays by the beginning of the twenty-first century, as we shall describe below.

In the present section, we shall discuss the various forms of astronomical interferometry on the basis of the principles given above. These different forms depend to some extent on the wavelength, but we shall always be able to identify a certain number of common functions: sub-pupils collecting incident radiation, transfer of the amplitude and phase data received by each sub-pupil to a recombination device, correction where necessary for effects due to the different optical paths of the two signals, and detection of the recombined signal, usually in the form of interference fringes, by a suitable detector for the given wavelength.

# 6.4.1 Obtaining an Interferometer Signal

There are several ways to recombine the radiation from the sub-pupils to obtain and measure either the interference pattern or any other quantity containing the same information (Fig. 6.25). The choice of one method rather than another depends on the means applied to detect the radiation (Chap. 7).

# Direct (Fizeau) Interferometry

The spatial frequency filter that constitutes an interferometer is exactly realised by small apertures (diameter $d$ ) forming a pupil mask that covers the primary mirror of a telescope. An image detector like a camera, if there is such a thing at the given wavelength, placed at the focus, measures the resulting fringes. This is the Fizeau configuration. It has the advantage of having a wide field, that of the telescope itself, since the optical paths between each aperture and the focal point remain equal for all points of the field. This can also be achieved with two separate but rigidly joined telescopes, as with the Large Binocular Telescope (LBT) discussed in Sect. 5.2.2, or the planned European space observatory Darwin. Since the two telescopes and their common base are rigidly fixed, so is their pointing and the optical paths from the source to the common focus are identical.

![](images/c45310938c7f5013223a0beeea6fe3b08e9a2369438dca2d0e8865155f0c885b.jpg)  
Fig. 6.25 Different kinds of interferometric combination. $\mathrm { T _ { 1 } }$ and $\mathrm { T } _ { 2 }$ denote two widely separated telescopes. (a) Direct interferometry. The waves travel to the common focus, where an interference pattern (image plane or pupil plane) forms on the detector (Fizeau, Michelson, or densified pupil configurations). (b) Direct interferometry by guided optics, using optical fibres. (c) Homodyne interferometry. Two photomultipliers in photon counting mode deliver currents $i _ { 1 }$ and $i _ { 2 }$ , analysed by a correlator. (d) Heterodyne interferometry (radiofrequencies and mid-infrared). Frequencies of incident waves are changed and a correlator analyses the intermediate frequency (IF) signals

# Direct (Michelson) Interferometry

This is the most commonly used configuration in optical (visible and infrared) interferometers, e.g., the Very Large Telescope Interferometer. A disconnected and independent pair of telescopes of diameter $D$ , constituting two sub-pupils, arranged on a baseline $B$ , collect light which is then transferred by optical train and combined at a common focus. Here the complex coherence of the radiation is measured (Fig. 6.26), after eliminating the optical path difference by a delay line. Since the telescopes are independent, the effect of the Earth’s daily rotation must be corrected for using delay lines, equalising the lengths of the optical paths between the sub-pupils and the common focus.

Like the last method, this one requires an image detector (camera) to analyse the fringes after recombination. The difference here is in the way the beams are transferred from the sub-pupils to the common focus. Before recombination, an exit pupil must be reconstituted that is homothetic to the entrance pupil. The interferometric field of view is generally small (a few arcsec).

Also known as direct interferometry, this setup measures the complex visibility directly, with a spectral band that can be quite broad $( \Delta \lambda / \lambda ~ \le ~ 0 . 1 )$ , i.e., with reduced temporal coherence, or again, with few fringes observable near the zero path length difference (PLD), and therefore high sensitivity. This works best in the near infrared spectral region $( 1 - 1 2 \mu \mathrm { m } )$ , because the properties of atmospheric phase effects are generally more favourable: the seeing size $r _ { 0 }$ , the characteristic time $\tau _ { c }$ , and the isoplanatic patch $\alpha _ { \mathrm { i s o } }$ , all three of which vary as $\lambda ^ { 6 / 5 }$ , whereas the constraints imposed by mechanical and optical accuracy vary as $\lambda$ . This explains why the method is more difficult to use in the visible, and hence still limited in this region.

![](images/3b0f2c2f15e9ffe10d164438d3d2bf3e9d74c962580ae0f79a1a23745068df06.jpg)  
Fig. 6.26 Optical (visible or infrared) interferometry from the ground (Michelson method). The two telescopes point in the direction $\pmb \theta$ . The afocal beams are guided by mirrors or optical fibres, then recombined in a common focal plane $F$ , where various combination schemes can be used (image plane, pupil plane). The complex visibility $\mathcal { V }$ is measured. A continuously variable delay line compensates for the daily rotation of the Earth (variation of the zenith distance $\theta$ ): $F C _ { 2 } - F C _ { 1 } = \Delta L ( t )$ . The random residual differential phase due to the atmosphere applies to the visibility $\mathcal { V }$

# Heterodyne Interferometry

Here the electric fields in the direction $\pmb \theta$ are detected locally behind sub-pupils 1 and 2 (Fig. 6.25d). The amplitude and phase are measured by interfering each with a field produced by a heterodyne local oscillator (see Sect. 7.5.2). The intermediate frequency (IF) signals are easily carried by cable to a common point, or even recorded and recombined later, as in very long baseline interferometry (VLBI). Since the problem is to measure the coherence between the two parts of the incident wavefront sampled by sub-pupils 1 and 2, we only need to calculate the correlation product of these fields in order to determine the complex coherence, which is simply $\widetilde { I } ( w )$ normalised:

$$
\left| \gamma _ { 1 2 } ( \tau ) \right| = \left| \left. E _ { 0 } E _ { 1 } ( t ) \mathrm { e } ^ { 2 \pi \mathrm { i } ( \nu - \nu _ { 0 } ) t } \otimes E _ { 0 } E _ { 2 } ( t + \tau ) \mathrm { e } ^ { - 2 \pi \mathrm { i } ( \nu - \nu _ { 0 } ) ( t + \tau ) } \right. _ { t } \right| .
$$

In contrast with direct combination of the beams, heterodyne combination works first by a change of frequency, which conserves the phase of the signal, at the focus of each telescope, then by recombination of the intermediate frequency (IF) signals in a correlator. Although the aim is the same, i.e., to measure the level of spatial coherence $\gamma _ { 1 2 } ( \tau )$ , there is an important difference between the two methods. In the first case, the usable bandwidth is broad, typically $\Delta \lambda / \lambda \sim 1 0 ^ { - 2 }$ at $\lambda = 0 . 5 \mu \mathrm { m }$ for $r _ { 0 } = 1 0 \mathrm { c m }$  D. In the second case, the bandwidth is limited by the mixer, with value Dup to a few GHz. Going from radiofrequencies towards the infrared and the visible, the relative bandwidth, and hence the detectable energy, decreases, as can be seen from Table 6.3. The sensitivity is thus limited, and all the more so as the wavelength gets shorter.

As for radiofrequencies, the gain in temporal coherence with decreasing relative bandwidth makes it easier to detect the fringes and measure their visibility, even in the presence of large phase differences due to optical path differences caused by mechanical or atmospheric perturbations. This explains the successful use of the heterodyne method in the mid-infrared, especially as $\mathrm { C O } _ { 2 }$ lasers can provide a stable and powerful local oscillator at $1 0 . 6 \mu \mathrm { m }$ .

Table 6.3 Spectral width in interferometry for four different wavelengths. The table gives values of relative spectral width $\Delta \lambda / \lambda = \Delta \nu / \nu$   

<table><tr><td></td><td></td><td>1 mm</td><td>100 μm</td><td>10 μm</td><td>1 μm</td></tr><tr><td>Heterodyne interferometry △v = 300 MHz</td><td></td><td>10-3</td><td>10-4</td><td>10-5</td><td>10-6</td></tr><tr><td>Direct interferometry</td><td>Ground</td><td></td><td></td><td>10-1-10-2</td><td>10-2-10-3</td></tr><tr><td colspan="4">Space</td><td colspan="2">≤1 if desired</td></tr></table>

The heterodyning technique is mainly applied in radiofrequency interferometry (from submillimetre to metre wave) and in the mid-infrared.22 It has not been extended to shorter wavelengths.

# Photon Correlation Measurement

Here the photocurrent is measured directly using sensitive photoelectric detectors placed at the focus of sub-pupils 1 and 2. The time correlation of the two currents can then be measured, transferring them by cable to the correlator (Fig. 6.25c). Zernike’s theorem shows that a measurement of this correlation gives the coherence $| \gamma _ { 1 2 } ( \tau ) |$ j jbetween 1 and 2 directly, and this is indeed the desired quantity. In the 1960s, this method was successfully applied by Hanbury-Brown23 in Australia.24 The future of this so-called homodyne interferometry is relatively limited, being applicable only to measuring the diameters of bright stars, and requiring telescopes with diameters of several metres, while the two apertures can of course be widely separated. Note, however, that the method does not require any special image quality at the focus of the sub-pupils, and does not therefore require adaptive optics. It could one day become relevant again, with the advent of giant telescopes on the one hand, and with the availability of very high bandpass quantum photodetectors (GHz, or even THz).

In practice, then, there are four different interferometric setups, the first two being rather similar. The usual terminology tends to contrast these methods, referred to as interferometric (because they produce fringes rather like Young’s fringes), with conventional imaging as it occurs at the focus of a classical mirror. It has been shown above that there is, in fact, no difference whatsoever, and we might just as well say that any image is the interference pattern formed by the whole set of waves diffracted at the pupil, whether that pupil be connected or not. The only difference is in the frequency filtering imposed by the given pupil: low pass, it provides an image that closely resembles the object; bandpass, the image is made up of interference fringes and no longer resembles the object.

# 6.4.2 Light Transfer

Since an interferometer has two sub-pupils at least several tens or hundreds of metres apart, this raises the problem of transferring light or information without loss of coherence (see Fig. 6.25). As it happens, there are several ways to transfer light, with or without loss of coherence. We shall review these briefly, then consider the use of optical fibres (see Fig. 6.25b), which recent technological progress has extended to all kinds of optical arrangements.

# Diversity of Light Transfer Techniques

Depending on the wavelength and the optical constraints imposed by the given instrumentation, several transfer methods are possible:

• At optical (visible or infrared) wavelengths, conventional setups always involve mirrors or lenses, whatever the wavelength being studied. Transfer should ideally be made in vacuum, so that there is no phase perturbation. This is clearly achieved in space, but would be extremely expensive in ground-based interferometers with baselines of a hundred metres or more. These generally transfer through air, care being taken to avoid thermal instability in light ducts. When heterodyne combination is possible (radiofrequencies or infrared), the IF signal downstream of the frequency change device is easily transported by cables, in which the risks of phase perturbation are very small. Upstream of the frequency change, waveguides provide a way of transferring an electromagnetic signal from one point to another while preserving the phase. This is generally a hollow tube, with rectangular or circular cross-section, and inner walls made from some reflecting metal. It offers an alternative to free propagation in the air. As well as being made to gradually change direction, the radiation can be mixed with other radiation, or coupled with a detection system. Waveguides are commonly used at radiofrequencies. The transverse dimension of a waveguide is comparable with the wavelength of the radiation it can transport, and the propagation of the radiation is described by Maxwell’s equations, taking into account the boundary conditions imposed by the reflecting walls. At the time of writing (2007), technological progress with miniaturisation is such that hollow waveguides can now be made for submillimetre and even mid-infrared applications.

• The recent development of optical fibres preserving the coherence of the wave (single-mode fibres) and behaving like hollow waveguides means that signals can be transported in the visible and infrared regions without loss of phase information from the sub-pupils to the common focus, where the complex coherence can be measured. At the time of writing (2007), this mode of transport is under experimental investigation (’OHANA project, see below), but may replace the conventional mode of transfer using mirrors.

# Optical Fibres

The considerable recent development of these components for telecommunications has allowed many astronomical applications, in interferometry and spectroscopy, in the visible and near infrared regions $\lambda \lesssim 1 0 ~ \mu \mathrm { m } )$ , which justifies the discussion here.

An optical fibre consists of two concentric cylinders, the core and the cladding, made from materials of different refractive index (step-index fibres), or of a single cylinder in which the refractive index varies continuously from the axis outwards (graded-index fibres). When the dimension $a$ of the fibre is large compared with the wavelength of radiation being carried, the geometrical approximation is suitable. On the other hand, when the transverse dimension and the wavelength are of the same order, diffraction must be taken into account, and this case resembles what happens in ordinary waveguides.

The idea of propagation mode is useful. During propagation in the fibre or the waveguide, boundary conditions require a stationary transverse wave (perpendicular to the axis), the moving wave being directed along the axis. The number of modes of propagation is, for given dimensions and given wavelength, the number of different stationary configurations allowed by the fibre. Thus, for $a \gg \lambda$ , the system is said to be multimode, and the geometrical approximation applies. When $a \approx \lambda$ , the single-mode condition can be satisfied.

A single-mode fibre or waveguide has the property of only accepting and propagating one coherence etendue, viz. ´ $\lambda ^ { 2 }$ , and therefore behaves as a spatial filter.

It is useful to define several parameters associated with optical fibres:

• The numerical aperture $\sin \theta$ of a step-index fibre, between core and cladding (of index $n _ { \mathrm { c } }$ and $n _ { \mathrm { c l } }$ , respectively), is given by

$$
\sin \theta = ( n _ { \mathrm { c } } ^ { 2 } - n _ { \mathrm { c l } } ^ { 2 } ) ^ { 1 / 2 } ,
$$

and the angle $\theta$ defines the half-angle at the apex of a cone with axis along the fibre and within which radiation is accepted by the fibre (acceptance angle of the fibre).

• The attenuation of a waveguide or a fibre is measured in decibel $\mathrm { m } ^ { - 1 }$ (or decibel $\mathrm { k m } ^ { - 1 }$ ). It depends on properties of the materials used and describes absorption and reflection losses. These losses can be less than $0 . 1 ~ \mathrm { d B } ~ \mathrm { k m } ^ { - 1 }$ . Fibres which are transparent in the infrared have been developed (fluoride glasses, chalcogenides). Rayleigh scattering in the material of the fibre inevitably limits transmission in the blue and precludes it completely in the ultraviolet.

• The cutoff wavelength of a single-mode fibre is the highest wavelength that can be propagated for a given dimension $a$ .

• The coupling efficiency (as a percentage) measures losses due to mismatching of impedance between free propagation in the air and guided propagation in the fibre. It takes values in the range 40 to $7 5 \%$ .

• The behaviour with respect to polarisation: certain fibres have axial symmetry and transmit all polarisations or natural light equally. If this symmetry is broken (elliptical core, torsion in the fibre), certain polarisations are preferred.

• There is dispersion in optical fibres, since the propagation speed usually depends on the wavelength. This dispersion is a serious drawback when using singlemode fibres to transfer light in the two arms of an interferometer, because it is then essential to have equal lengths of fibre whenever the aim is to observe a source across a relatively broad spectral band. In the future, it should be possible to make fibres without dispersion from photonic crystals.

Single-mode waveguides and optical fibres, which conserve the phase, are invaluable for direct coupling of telescopes used in aperture synthesis (see the discussion of the ’OHANA interferometer below), but also for coupling a single coherence etendue (a single mode) between focal plane and detector, which is the case´ for radiofrequency imaging and also infrared adaptive imaging at the diffraction limit.

At optical wavelengths, multimode fibres are used in the straightforward transportation of light energy between focal plane and instrumentation such as spectrograph and detectors (see Sect. 8.3). However, the transfer rates obtained by telecommunications fibres are already sufficient (2006) to use the fibres to transport the intermediate frequency (IF) signal over very great distances between radiotelescopes operating in very long baseline arrays, making real-time VLBI possible (see below).

# 6.4.3 Temporal Coherence

Up to now we have been assuming monochromatic radiation, and hence maximal temporal coherence. A fixed optical path difference between beams 1 and 2 is in this case of no importance when measuring the visibility $\mathcal { V }$ . However, a real observation requires a finite spectral passband $\Delta \lambda$ , implying a reduced temporal coherence and hence a finite number of fringes near the zero optical path length difference (PLD). One must then ensure that path length differences are equal for the radiation following paths 1 and 2, up to a few $\lambda$ in the case of a broad spectral band, the number of observable fringes being given approximately by $\lambda / \Delta \lambda$ . This is all the more relevant given that the Earth’s rotation continually modifies this path length difference (Fig. 6.26). Any ground-based interferometer, whatever the wavelength it operates at, must include a compensation system, i.e., a delay line, and in some cases fringe tracking, except in the very special and obviously convenient case where the two sub-pupils are placed on the same mount, as in the LBT telescope.

# 6.4.4 Loss of Spatial Coherence

In the ideal picture of an interferometer with two sub-pupils presented above, a measurement of the amplitude and phase of the complex visibility of the

![](images/0b1b22713e738e10b07605fef8f39958acceebb8dfe225b7f221bcb78ed4c7ec.jpg)  
Fig. 6.27 Phase perturbations in aperture synthesis at radiofrequencies. The phase perturbation due to the ionosphere is $\Delta \phi _ { 2 } - \Delta \phi _ { 1 }$

fringes at the common focus provides the desired quantity $\widetilde { I } ( w )$ , the normalised Fourier component of the spatial spectrum of the object. However, there are many limitations to this ideal case in a real astronomical interferometer.

# Atmospheric Phase Noise

We have already seen that the complex visibility $\mathcal { V }$ of the fringes may be affected by a perturbing phase noise due to random fluctuations of the optical path in the Earth atmosphere, along the distinct paths followed by the two beams upstream (Fig. 6.27) or downstream of the sub-pupils. Furthermore, this phase noise is chromatic and hence reduces the temporal coherence of the signal. These effects, predominant at optical wavelengths, disappear in space, and thus constitute one of the main arguments for building space-based interferometers.

# Instrumental Decoherence

Other sources of perturbation may remain, such as vibrations along the optical path, asymmetric polarisation effects, and so on. They have the same result, producing phase noise and loss of coherence, i.e., a reduction in the amplitude, either instantaneous or averaged over time, of the fringe visibility $\mathcal { V }$ .

# Non-Coherent Sub-Pupil

Up to now it has been implicitly assumed that the radiated electric fields collected at sub-pupils 1 and 2 are those of the wave emitted by the source, and hence that a measurement of these fields would exactly reflect the degree of coherence of the source. This is clearly true in space. However, for a ground-based interferometer, it is no longer true unless the size $d$ of the sub-pupil remains less than the Fried length $r _ { 0 } ( \lambda )$ . In the latter case, the coherence of the incident wavefront is maintained over the whole surface of the sub-pupils. This situation is found in practically all radiotelescopes, which are not affected by atmospheric seeing, whatever their diameter. However, very wide aperture antennas (more than $1 0 ~ \mathrm { m }$ ) operating at wavelengths of millimetre order may suffer from seeing, e.g., the IRAM interferometric array in France, and the ALMA array under construction in Chile (see below).

The problem is much more serious at visible and infrared wavelengths. The first generation of optical interferometers (1970–1995) usually operated with telescopes (sub-pupils) smaller than $r _ { 0 }$ , or of the same order (around ten centimetres), which guaranteed the coherence of the incident wave on the sub-pupil. In a much bigger instrument, the images given by each sub-pupil are affected by speckles, and their coherent superposition produces an interference pattern from which it is very difficult to extract a measurement of $\widetilde { I } ( w )$ . The most one could do is to determine its modulus, all phase information having been destroyed by the loss of coherence. Adaptive optics provides a way round this difficulty, so that telescopes of very large diameter can then operate in interferometric mode.

To sum up, the effect of atmospheric turbulence will depend on the relative size $D$ of the sub-pupil and the Fried parameter $r _ { 0 } ( \lambda )$ (see Sect 6.2):

• If $D < r _ { 0 } ( \lambda )$ , the fringe system (Fig. 6.28) appears where the images given by the two sub-pupils are superposed. If there is an elementary adaptive optics device to correct for agitation (tip–tilt stabilisation), the two images remain superposed and the fringe system is observable. However, the differential phase noise between the two sub-pupils will shift the whole pattern randomly as time goes by. If $D \ \gg \ r _ { 0 } ( \lambda )$ , the size of the image spot will be $\lambda / r _ { 0 } ( \lambda )$ and the fringes will be perturbed by speckles (see Sect. 6.2). It then becomes very difficult to analyse the image and determine $\mathcal { V }$ .

When the observed source is bright, this means that there may be enough photons to be able to measure the modulus of the visibility with an acceptable signal-tonoise ratio in a time shorter than the coherence time $\tau _ { \mathrm { c } }$ , whence the atmospheric non-uniformities will not have had time to modify the instantaneous phase between the two beams. On the other hand, if the object is too faint to satisfy this condition, the signal-to-noise ratio on a measurement of duration $\tau$ will be less than unity. In this case, one must take the spectral density of the intensity distribution in each exposure, where the fringes are invisible, i.e., $S _ { \mathrm { i } } ( f )$ , then take the average $\langle S _ { \mathrm { i } } ( f ) \rangle$ h iover all exposures and deduce the modulus of the spectral density of the object at this frequency (Fig. 6.29).

All these factors make it difficult to use ground-based optical interferometry and thus require very careful observing protocols. In addition, the ever present phase noise, whether due to ionospheric perturbations at radiofrequencies or tropospheric perturbations in the infrared and visible, means that only $\lvert \mathcal { V } \rvert$ can be measured. j jWhen the phase is not known, the image of the source cannot then be reconstructed from a set of values of $w$ , except in the special case where one can use information known by other means, e.g., one may know that an object is centrally symmetric, whereupon the phases $\phi ( w )$ must be zero. This limitation has led to the development of phase closure methods (see Sect. 6.4.6).

![](images/a0bf23fc9f0281d971b9b144c77f49064f490045e775244331ce7ec2a3fe8508.jpg)  
Fig. 6.28 Views of the focal plane of an interferometer. (a) Perfect coherence of the wavefronts at the two apertures. Interference is produced in the Airy image given by a single pupil. (b) Coherence of the wavefronts at each pupil, limited by atmospheric turbulence (Fried parameter $r _ { 0 }$ ). Fringes are present in each speckle, with random phase. (c) Interference pattern obtained from two mirrors of the Multi-Mirror Telescope, with centre-to-centre distance $4 . 6 \mathrm { m }$ . $\lambda = 6 0 0 \mathrm { n m }$ , exposure $1 / 6 0 \mathrm { ~ s ~ }$ . DNote the presence of speckles containing fringes. (Photograph courtesy of Hege E.K., Beckers J.)

![](images/ee61491e8ffd698e301b21da46d2c70acc71b54d36d243af2a3446ad3dc9a131.jpg)  
Fig. 6.29 Mean spectral density of a large number of instantaneous images, in a direction normal to the fringes of spatial frequency $f _ { 0 }$ . The spike shows that fringes are present, and the ratio $2 \langle S ( f _ { 0 } ) \rangle / S ( 0 )$ gives the modulus of their visibility at this frequency

# 6.4.5 Calibrating the Instrumental MTF

The instrumental modulation transfer function (MTF) and its consequences in the image, i.e., the point spread function (PSF), are relevant to interferometers and arrays just as they are relevant to telescopes. However, the fact that it is a bandpass system (just one, or several in aperture synthesis) implies certain specific characteristics that we shall examine here. In interferometry, it is often simpler to refer to the modulation transfer function than to consider the PSF.

# Two Sub-Pupils

In order to reconstruct the spectrum $\widetilde { I } ( w )$ of a source $S$ , one must know the MTF of the instrument used to observe it. The ideal way to determine this is to observe a point source $S _ { 0 }$ called a reference source in the sky, and to measure the amplitude and phase of the complex quantity $\widetilde { I } _ { 0 } ( w )$ , i.e., simply the complex visibility $\mathcal { V } _ { 0 }$ for this reference source. Let us suppose for a moment that there are no atmospheric phase perturbations, in which case the reference $S _ { 0 }$ can be distinct from $S$ . But then the angular separation between $S$ and $S _ { 0 }$ must be accurately known in order to correct for the phase introduced by this separation when determining $\mathcal { V } _ { o }$ .

This idea was first applied in radioastronomy interferometry in the 1960s (at decimetre wavelengths), localising $S$ in the sky to within a few arcsec, and reconstructing its image $I ( \pmb \theta )$ by aperture synthesis. Quasars provide radiosources that can be treated as unresolved by the instrument, hence pointlike.

At optical wavelengths and on the ground, one can no longer assume that there are no atmospheric effects. The fringes continually move around under the effects of phase noise. How can one then determine the (complex) instrumental MTF? This is only now possible for its amplitude. By observing the fringe system of a point source $S _ { 0 }$ , one generally obtains a value of $| \mathcal { H } _ { 0 } |$ less than unity, which must be j jmeasured as accurately as possible, and which calibrates coherence losses within the instrument. This source $S _ { 0 }$ can be in a different direction, although preferably close to the direction of S . A more important point is to choose $S _ { 0 }$ with similar magnitude and spectral distribution (colour) to $S$ , in order not to suffer the consequences of any non-linearities in the system.

Finite Angular Size of Reference Star. The angular resolutions achieved by optical interferometers are now less than the mas $1 0 ^ { - 3 }$ arcsec). There are no stars with apparent size smaller than this value and with sufficient magnitude to give a measurable signal. For example, a star like the Sun at $1 0 \ \mathrm { p c }$ would subtend an angle of 1 mas. One must therefore accept a calibration using a resolved star, but with a diameter $\alpha _ { 0 }$ that is assumed known, by virtue of the spectral type and assuming there is no stellar envelope. The visibility at frequency $w ( u , \nu )$ is simply given by the Fourier transform of the uniform brightness distribution of the stellar disk (see Sect. 6.1):

$$
\mathcal { V } _ { 0 } ( u ) = \frac { 2 J _ { 1 } ( \pi \alpha _ { 0 } u ) } { \pi \alpha _ { 0 } u } .
$$

With the achievable measurement ranges, of order $1 0 ^ { 3 }$ or better, the uniform disk assumption gives an incorrect value $\mathcal { V } _ { 0 }$ , because there is generally a darkening of the star from the centre out toward the limb (center-to-limb variation or CLV), which modifies the above expression. One must then make a model of the star which makes a quantitative prediction of the CLV effect, and replace this expression by a hopefully better calculated expression (see Sect. 3.6).

This is a serious limitation. It can give rise to errors in the determination of the instrumental factor $\mathcal { V } _ { 0 }$ , and hence in the visibility $\mathcal { V }$ of the source S. This problem also occurs for a space-based interferometer. However, at radiofrequencies, the angular size of the central emission of quasars or active galactic nuclei (AGN) is less than 0.1 mas, whereas the decimetre wave resolution of a baseline equal to the diameter of the Earth is ‘only’ 2 mas.

# Multiple Sub-Pupils

Return once again to the simple case where there are no atmospheric effects, but consider now a pupil with many sub-pupils covering a certain number of spatial frequencies at a given instant of time. This is the case in radiofrequency aperture synthesis, in an array of telescopes, with either direct coupling or delayed coupling (VLBI). The transfer function (MTF) is the autocorrelation function of this pupil and behaves as a spatial filter transmitting a certain number of frequencies apart from the frequency 0 and its immediate vicinity (which corresponds to the total received power). The array can be dense or dilute, depending on whether the MTF covers a region of the $( u , \nu )$ plane almost entirely or only rather sparsely. In the first case, the image of a point source (PSF) is rather close to an Airy function, and in the second, it will be rather different. The second case is referred to as a dirty beam.

It is easy to see that the image of a somewhat complicated source, convolution of the object by this PSF, will be very hard or even impossible to interpret, because too much information will be lacking about the unmeasured spatial frequencies. These gaps in the spatial filter create unwanted artifacts in the raw image, such as secondary lobes, feet, ghost images, and so on, and can even distort it to the point that it becomes unintelligible. Such an image is sometimes called a dirty map. The PSF and especially the MTF can, as above, be determined by observing an unresolved source.

# Information Restitution: The CLEAN Algorithm

The CLEAN algorithm25 was designed by Jan Hogbom in Holland in 1974 to¨ process images from the Westerbork array, for which the PSF (dirty beam) was too dispersed. Extra information is added to the rather poor information extracted from the measurement, in order to restore an object that is compatible not only with the measurement, but also with an a priori physical idea of the object. It is difficult to be certain that the solution found in this way is necessarily unique. One accepts merely that it is highly probable, given the constraints one introduces regarding the object.26 At the time of writing (2007), these methods have been significantly refined, and will be discussed further in Sect. 9.6.

With the CLEAN algorithm, the constraint is expressed by assuming that the object comprises a series of point sources. This is appropriate for a field filled with unresolved stars or radiogalaxies, for example. Other methods for supplying ‘probable information’ were devised, some of them very powerful. These were applied not only to interferometry, but also to other kinds of signal processing, in spectroscopy, for example. For this reason, the discussion of these issues will be postponed until Chap. 9.

Suppose the intensity $I _ { 0 } ( \pmb \theta )$ of the object consists of a background which is zero almost everywhere, upon which are superposed several localised sources, whose arbitrary intensity profile is to be determined. Let $\tilde { T } ( \boldsymbol { w } )$ be the instrumental profile (MTF), assumed to have been determined independently by observing a point source, and $\tilde { I } ( \boldsymbol w )$ the observation. Define

$$
t _ { 1 } ( w ) = g _ { 1 } \tilde { T } ( w ) \mathrm { e } ^ { 2 \mathrm { i } \pi w \cdot \pmb { \alpha } _ { 1 } }
$$

and choose ${ \pmb { \alpha } } _ { 1 }$ , which is the position of source 1, to minimise the quantity

$$
r _ { 1 } ( w ) = \tilde { I } ( w ) - t _ { 1 } ( w )
$$

by least squares. The weighting factor $g _ { 1 }$ is taken less than or equal to unity. This operation is equivalent to removing the brightest source, assumed pointlike to a first approximation, from the observed area. The procedure is repeated on the residue $r _ { 1 } ( w )$ with $t _ { 2 } ( \pmb { w } )$ , then $t _ { 3 } , \ldots , t _ { i }$ , using as many components $i$ as there are discernible sources in the observed area. It can be shown that $r _ { i } ( w )$ tends to zero, and this implies that the approximation

$$
\hat { \tilde { I } } ( w ) = \sum _ { i } g _ { i } \mathrm { e } ^ { 2 \mathrm { i } \pi w \cdot \pmb { \alpha } _ { i } }
$$

tends to the quantity $\tilde { I } ( \boldsymbol w )$ , which was to be determined. Fourier transforming, a better approximation of the desired image $\tilde { I } ( \pmb \theta )$ is recovered. The method is illustrated in Figs. 6.30 and 6.31. CLEAN is a method which takes account of the boundedness of the image, but not its positivity, the latter being another piece of a priori information that other methods put to use. CLEAN is useful for images consisting of well-separated sources, without a significant continuous background.

# 6.4.6 Phase Closure

The effects of coherence losses due to the atmosphere became significant in radio interferometry as soon as it began to move toward short wavelengths, and later these effects became immediately critical in optical interferometry. To deal with them, Roger Jennison introduced the idea of phase closure in his thesis (1951). The idea was then rediscovered in 1974 by A.E.E. Rogers, and since then, the method has been widely used at radiofrequencies, and was applied for the first time in optical interferometry by John Baldwin (Cambridge, UK) in 1998. It is interesting

![](images/1e6efe2cd09c9210980c47f031fc8c72a9b3efbf99e0739a53861c556905ba1c.jpg)  
Fig. 6.30 Image reconstruction (numerical simulation). The transfer function $\tilde { T } ( \boldsymbol { w } )$ has gaps in its Qspatial frequency coverage, and the point source response (PSF) is not ‘clean’. (a) Reconstruction by inverse FT of $\tilde { I _ { 0 } } ( w ) \tilde { T } ( w )$ . (b) Reconstruction using CLEAN. (c) Reconstruction using the maximum entropy method (see Sect. 9.5). Compare (a), (b), and (c) with the original object $I ( \pmb \theta )$ . From Rogers A.E., Methods of Experimental Physics, Vol 12C. With the kind permission of the editor


<!-- chunk 0005: pages 281-350 -->
![](images/0132fb78730b2e1fb7317a86d15c9452a585bb367d03ac9ee2065f1ed5e95c2f.jpg)  
Fig. 6.31 Image processing using the CLEAN algorithm. The radiosource CygX-3, discovered in 1967 with the first rocket-borne X-ray observations of the sky, is a binary system including a Wolf–Rayet star and a compact variable object (microquasar). Observed with the VLA array at00 frequency $5 \mathrm { G H z }$ , rapid bipolar ejection from the microquasar became clearly visible for the first time (speed 0:5c). The CLEAN process is adapted here to the case of a rapidly varying object, with a final resolution of $0 . 3 { ^ { \prime \prime } }$ and a logarithmic intensity scale. (J. Marti et al., Astron. Astrophys. 375, 476, 2001. With the kind permision of NRAO-AUI)

to note that the idea of phase closure, under the name of structural invariance, was already used in X-ray crystallography back in the 1950s to determine the electron distribution in solids (pointed out by K. Kellermann & J. Moran).

Consider to begin with an array comprising three non-redundant sub-pupils, e.g., arranged at the corners of a triangle. With no atmosphere and a perfect instrument, the phase of the fringes given by each pair of sub-pupils is $2 \pi \lambda ( D _ { i j } { \bf \cdot s } )$ , where $\pmb { S }$ is the unit vector in the direction of the source. Since $\sum { \pmb { D } } _ { i j } = 0$ , the sum of the three Dphases is also equal to zero. If an atmospheric or instrumental perturbation should affect one of the sub-pupils, the sum remains zero, the perturbation adding to one baseline and subtracting from the other. If all the sub-pupils are affected, the result is the same, and the sum of the measured phases is equal to the sum of the true phases from the source. Clearly, the object must be bright enough to be able to measure the fringes (and hence their phase), with a high enough signal-to-noise ratio and over a lapse of time during which the perturbation remains stable, hence shorter than the coherence time $\tau _ { \mathrm { c } }$ of the atmosphere. This is called snapshot mode.

In the case of a non-redundant array of $N$ telescopes, a total of $N ( N - 1 ) / 2$ frequencies is measured, but only $( N - 1 ) ( N - 2 ) / 2$ independent phase closure  relations are obtained, which is thus not enough to reconstruct the $N$ unknown (because perturbed) phases of the object at the measured frequencies. However, if $N$ is large, the fraction of phase information actually recovered, viz., $( N - 2 ) / N$ , tends to $100 \%$ . Since the spectrum of the source $S$ is known in amplitude and almost completely known in phase, high quality images of $S$ can be reconstructed, without a priori assumptions about $S$ . If this process is combined with the CLEAN procedure, i.e., by including a priori information, the reconstructed image can be further improved. This combination is then referred to as a hybrid mapping. An extension of the method has become known as self-calibration.

All of these procedures have their limitations, residues of artifacts due to a poorly corrected PSF. At the time of writing (2006), a residual artifact less than $0 . 1 \%$ is achieved with large radio arrays (VLA, VLBA). The magnificent images of extragalactic objects produced by these arrays are thus obtained through a large collecting area and long exposures (access to faint objects), very long baselines allowing very high angular resolutions, and the high quality of the final PSF thanks to phase closure and numerical image restitution procedures. It is not yet possible in 2007 to boast equivalent performances for interferometry at optical wavelengths, but there is little doubt that progress will be fast given that the problems are very similar.

Pupil Masking. In 1874, Edouard Stephan in Marseille (France) built upon Fizeau’s ideas for reducing the effects of atmospheric perturbations by arranging two small apertures at variable distances apart on a diameter of the mirror of his telescope pointing toward a star. The apertures were only a few centimetres in diameter, hence smaller than the Fried parameter $r _ { 0 }$ . The apertures produced fringes agitated by a random translatory motion (phase noise). He estimated the visibility of the fringes and concluded the observed stars to have diameters smaller than the diffraction limit (0.16 arcsec) of the telescope he was using.

Now suppose there are, not two, but $N$ apertures, all smaller than $r _ { 0 }$ , on the surface of a large primary mirror (or an image of it, reformed downstream). At optical wavelengths, the image of a star is poorly visible, formed from $N$ systems of agitated fringes. This is a fortiori the image of a resolved object. However, if the apertures are non-redundant, Fourier analysis of the instantaneous image (snapshot) will perfectly separate each of the frequencies $w _ { i }$ of the image, and provide its amplitude and phase. The situation is strictly the same as what we have just described at radiofrequencies, and phase closure methods along with information restitution techniques like CLEAN and others can be applied in exactly the same way, to obtain from the source an image of resolution $\lambda / D _ { \mathrm { m i r r o r } }$ , limited only by diffraction (Fig. 6.32). In some cases, this approach can compete with adaptive optics, since the instrumental setup is very simple here (comprising only a mask), whereafter all processing is done numerically.

![](images/e7bababc6219ef617ad3e6b49a0018aaa530b5f2401dfd162cbe871842fca2ed.jpg)  
Fig. 6.32 Image of the LkH˛ 101 circumstellar envelope (accretion), obtained by pupil masking and phase closure on the $1 0 \mathrm { m }$ Keck telescope (Hawaii) at $\lambda = 2 . 2 \mu \mathrm { m }$ . DThe image has been processed using a certain amount of a priori information in order to reveal the central star Herbig Ae-Be (see Sect 9.6). With the kind permission of P. Tuthill. See Tuthill, P. et al., Ap. J. 577, 826, 2002

# 6.5 Astronomical Interferometers

In this section, we shall describe current and future realisations of interferometer arrays in various wavelength ranges, from radiofrequencies, through visible and infrared, to certain projects for X-ray observation. This kind of tool is developing fast, aiming for angular resolutions less than the mas ( $1 0 ^ { - 3 }$ arcsec), or even the $\mu { } \mathrm { a s }$ ( $1 0 ^ { - 6 }$ arcsec). The latter corresponds to a resolution of $1 \ 0 0 0$ AU at a distance of $1 \mathrm { G p c }$ , and requires a baseline of 2 million kilometers at $1 \mathrm { { c m } }$ , or $2 0 0 \mathrm { m }$ at $\lambda = 1 \mathrm { n m } !$ DWe shall also describe some of the observations made using these techniques.

# 6.5.1 Radiotelescope Arrays

Although Stephan and Michelson made their pioneering experiments in the visible prior to 1921, the technique of astronomical interferometry only really developed with the advent of radioastronomy, in the 1950s. This is because the accuracies required of the instrumentation are obviously less stringent than at optical wavelengths, and above all it is easy to transfer the Hertzian antenna signals by cable whilst preserving phase information, so that they can subsequently be recombined. Finally, the frequency bandwidth used is relatively narrow $( \sim 1 0 ^ { 6 }$ to $1 0 ^ { 8 } ~ \mathrm { H z } )$ compared with optical bandwidths $( \sim 1 0 ^ { 1 4 } ~ \mathrm { H z } )$ . The temporal coherence length is therefore large, and this means that it is easier to obtain an interference signal from two coherent signals originating at widely separated antennas.

![](images/f8836191bd388ce61e5771b9e63440f3b8d6e31f46fd3b0fc10298b6b40699b0.jpg)  
Fig. 6.33 Radio interferometry. A pair of antennas with baseline $B$ point in the direction $\pmb \theta ( t )$ of the source. The angles $\psi ( t )$ and $\phi ( t )$ defining $\pmb \theta ( t )$ are functions of time due to the Earth’s rotation. The phase difference between the two antennas can easily be calculated. An additional phase difference $\Delta \phi$ can be introduced electrically (delay line $\tau _ { \mathrm { d } }$ ) and the signals mixed in a correlator which provides the fringe signal. The temporal coherence of the signals is sufficient (the pass band $\Delta \nu$ is small compared with the signal frequency), so there will be many fringes around the zero path length difference

Ground-based radio interferometers27 cover a broad spectrum, from decametre wave $\lambda = 3 0 \mathrm { m }$ corresponds to $1 0 \ \mathrm { M H z }$ ) to millimetre wave $1 ~ \mathrm { m m }$ corresponds to $3 0 0 ~ \mathrm { G H z }$ ). Even though the underlying principles of construction and use are largely the same, the breadth of the region justifies presenting these instruments in subfamilies. An important place is given to very long baseline interferometry (VLBI), which is the only one to appeal to observation from space.

# Obtaining the Interferometric Signal (Radiofrequencies)

A widely separated pair of telescopes (antennas), comprising the two sub-pupils 1 and 2 and forming a baseline of length $\pmb { B } _ { 1 2 }$ , or simply $\pmb { B }$ , are both pointing in the direction $\pmb \theta$ (Fig. 6.33). The electric fields received at their foci, which may be transported locally by a waveguide, first undergo a change of frequency (intermediate frequency or IF) at 1 and 2, whereupon these two IF signals are carried to a correlator which measures their coherence $\gamma _ { 1 2 } ( \tau )$ , or equivalently, the visibility of the fringes. In order to restore the temporal coherence between signals 1 and 2, a delay line can introduce a suitable phase shift $\delta \varphi \ = \ 2 \pi \nu \tau _ { \mathrm { d } }$ . The time delay $\tau$ Dis a function of the length and orientation of the baseline $\pmb { B }$ , and also the diurnal rotation of the Earth. The spatial frequency analysed is determined by the value of the baseline $\pmb { B }$ projected onto a plane normal to the incident wave vector. The sighting angle $\pmb \theta ( t )$ , with components $\psi ( t )$ and $\varphi ( t )$ (Fig. 6.33), induces a time shift which is given as a function of time by

$$
\tau = \tau _ { \mathrm { d } } + \frac { B } { \lambda c } \left[ \cos \varphi ( t ) \cos \psi ( t ) \right] .
$$

The spatial frequency analysed, with components $u$ and $\nu$ , is determined by the projected baseline, and given by

$$
| w | = ( u ^ { 2 } + \nu ^ { 2 } ) ^ { 1 / 2 } = \frac { B } { \lambda } \left[ \sin ^ { 2 } \varphi ( t ) + \sin ^ { 2 } \psi ( t ) \cos ^ { 2 } \varphi ( t ) \right] ^ { 1 / 2 } ~ .
$$

It lies in the direction of the baseline projected onto the plane of the wavefront, i.e., onto the sky. The Earth’s rotation thus gives, for a fixed value of $B$ , a partial sampling of the spatial frequency plane $( u , \nu )$ .

Measuring the phase of the fringes completely fixes the complex Fourier component. These phase measurements can lead to extremely precise results. Over a baseline $B = 1 \mathrm { k m }$ , at $\lambda = 1 \mathrm { c m }$ , a determination of the phase to within 10 degrees, D Dof a source known to be effectively pointlike will fix the angular position of that source in the coordinate system of the base (terrestrial coordinates) to an accuracy of

$$
\delta \theta = \frac { 1 0 } { 3 6 0 } \frac { \lambda } { B } = 0 . 0 6 \mathrm { a r c s e c } .
$$

Radioastronomical interferometry is thus a powerful tool in astrometry.

Note that such a phase measurement is never absolute and that a reference network of point sources across the sky (usually quasars, see Sect. 4.2) is therefore necessary in order to establish reference phases, as explained earlier.

# Aperture Synthesis

Heterodyne detection of radiofrequencies has one remarkable property that does not occur for visible and infrared interferometers. Suppose that, instead of a pair of sub-pupils, we have some number $N$ greater than 2, forming many baselines $\pmb { { B } } _ { i , j }$ between them. The IF signal of an arbitrary antenna $i$ can then be distributed over several correlators, to form all possible correlations $( i , j )$ , making a total of $N ( N - 1 ) / 2$ correlations. Thanks to the local oscillator, this division of the signal can be achieved without reducing the signal-to-noise ratio, as explained in Chap. 7 on detectors (see in particular Sect. 7.5).

![](images/1a4ad1ed4db54d20508bbfa2ea231a49a87b46f6be54e0efaeb0a9ab40f8bb4e.jpg)  
Fig. 6.34 Redundancy of a pupil. Left: A redundant pupil. Several pairs of elements sample the same spatial frequency $w _ { 1 }$ . Right: A non-redundant pupil. Only the pair $A B$ samples $w _ { 1 }$ , the other pairs each sampling different frequencies

In practice, a large number of antennas are used (an array), paired in such a way that, varying $\pmb { B }$ for each pair, coverage of the $w$ plane can be optimised. If each pair corresponds to a single value of $w$ without any overlapping, the pupil is said to be non-redundant, in contrast to the highly redundant pupil formed by a standard circular aperture (Fig. 6.34). A dedicated computer combines the signals from all the antennas, calculating all the possible correlation functions, after first introducing the dephasing $\tau _ { i , j } ( t )$ required to centre the correlations on a given instant, which amounts to referring all the measurements to a common wave plane. This is the operation known as aperture synthesis.

Since the spatial frequencies filtered by a pair of telescopes is determined by the projection of the baseline $\pmb { B }$ on the sky, the Earth’s rotation varies this quantity as time goes by, thereby increasing the number of spatial frequencies covered in the plane $( u , \nu )$ . This combination of aperature synthesis and the Earth’s rotation is sometimes called aperture supersynthesis.

The image $I ( \pmb \theta )$ of the source is then obtained by a numerical Fourier transformation of $\widetilde { I } ( w )$ . This operation requires sampling of the MTF of the array (see above), and also image processing, to be discussed later (see Sect. 9.6). The extraordinary progress in computer technology since 1980, combined with powerful processing algorithms based on information theory, have made it possible to produce excellent images even though the arrays do not sample the whole range of frequencies up to some cutoff value, in the way that a single circular pupil would.

# Arrays for Metre to Centimetre Observation

The Very Large Array (VLA)

After the arrays in Cambridge (UK) and Westerbork (Netherlands), which played an important role in the development of radio interferometry over the decades

![](images/5eefeabc5ea33ff2ec0b6df8c4ab958797c8c27d3719177418388343f33bc49f.jpg)  
Fig. 6.35 Aerial view of the antennas of the VLA (Very Large Array) aperture synthesis array. The antennas are arranged in the shape of a Y, with the northern branch on the right, the south-eastern branch on the left, and the south-western branch at the top. Each branch includes 24 possible antenna positions at which the 27 mobile antennas can be placed. (NRAO photograph, Associated Universities, with the kind permission of the National Science Foundation)

1960–1980 and remain active today, the VLA of the National Radio Astronomy Observatory (NRAO) in New Mexico (USA) has become the most powerful tool of its kind in the world today at centimetre wavelengths, since it went into operation in 1980. It comprises 27 mobile antennas (Fig. 6.35) with separations up to $3 0 \mathrm { k m }$ , and operates from $\lambda = 4 \mathrm { m }$ down to $\lambda \approx 7 ~ \mathrm { m m }$ , achieving a resolution of 20 mas D at this wavelength (Fig. 6.36). It provides more than 1 000 images $1 0 2 4 \times 4 0 9 6$ pixels) per day of observation and has 512 spectral channels. As commented by the radioastronomer Jim Moran at the Center for Astrophysics in Harvard in 2001:

Since its completion in 1980, the VLA has been used by over 2 000 scientists from hundreds of laboratories and universities around the world for more than 10 000 individual observing programs. It exceeds its design specifications by orders of magnitude in nearly all parameters and remains, today, by far the most powerful radiotelescope in the world, although much of the instrumentation dates from the 1970s.

The Giant Meter Radio Telescope (GMRT)

This instrument, which went into operation in 2001, is located near Pune in Maharashstra (India). The array comprises 30 fixed antennas, each of diameter $4 5 \mathrm { m }$ , of which 14 are within $1 \mathrm { k m } ^ { 2 }$ from the centre, surrounded by 16 others, arranged on the branches of a $\mathrm { Y }$ with baselines up to $2 5 \ \mathrm { k m }$ . With this flexible configuration, a total of $N ( N - 1 ) / 2 = 4 3 5$ different baselines are available, covering a wavelength region from $6 \mathrm { m }$ to $2 1 \mathrm { c m }$ , and reaching a maximal resolution of 2 arcsec.

This instrument was built by India alone and is today the best metre wave array in the world. Apart from its scientific production, it is being used to develop techniques for a future instrument which could be the subject of a very broad international collaboration for the 2020s, namely the Square Kilometric Array (SKA). This would operate in the centimetre and decimetre wave range and could have a collecting area as great as $1 \mathrm { k m } ^ { 2 }$ . An interesting idea is under investigation here. Instead of orienting each antenna of the array individually to point in the direction of the source, the direction $\pmb \theta$ of the maximum point source response of the array (peak of the PSF) is fixed by modifying the phase of the signal received by each antenna, which can thus be flat, horizontal, and fixed, giving what is called a phased array. This technique is highly conventional in the construction of certain radars, and spatial scanning is done without rotating the antenna mechanically, but rather by modulating the phase of the signal emitted or received by each of the elements making it up.

![](images/1abf9d377d414ab9ed4edd39c6d2499b55327ddc9cd5e609a529614f694926c3.jpg)  
Fig. 6.36 The galaxy $\textbf { M } 8 7$ and its jet, about $1 5 \mathrm { { M p c } }$ from the Sun, observed at radiofrequencies. Upper: VLA observations, left at $\lambda = 9 0 ~ \mathrm { c m }$ , right at $\lambda = 2 0 \mathrm { c m }$ . Lower: Observations by theˇ VLBA interferometric array at $\lambda = 7 \mathrm { m m }$ D. Scales are specified on each image. On the lower image, $r _ { \mathrm { s } }$ Dis the Schwarzschild radius of the central black hole, of mass $M = 3 \times 1 0 ^ { 9 } M _ { \odot }$ . Image by Junor, W., Biretta, J., Livio, M., courtesy of NRAO/AUI/NSF

![](images/f75987339eed838db0f41e7ee3a91768e2a1e11eea6a6f195a6921a774c4da4e.jpg)  
Fig. 6.37 A sequence of images of the Sun taken by the Nanc¸ay radioheliograph at $\lambda = 0 . 9 2 { \mathrm { m } }$ Dduring a solar flare. The emission is due to electron beams propagating in the magnetic structures of the corona at speeds of the order of $c / 3$ , and lasts only a few seconds. The white circle marks the edge of the visible disk of the Sun. Image kindly provided by L. Klein and published by Maia, D. et al., Solar Phys. 181, 121–132 (1998)

Another project known as the Low Frequency Array (LOFAR) is also under study at the time of writing (2007) to build an instrument comprising several thousand antennas distributed over more than $1 0 0 \mathrm { k m }$ of baseline. These would be simple and relatively inexpensive, because they would operate at a long wavelength $\lambda = 3 0 \mathrm { m }$ .

Solar Surveillance by Radio Interferometry

The radioheliograph at Nanc¸ay (France) is a metre wave instrument, consisting of two $1 0 \mathrm { m }$ antennas and sixteen $3 \mathrm { m }$ antennas, and operates at $1 6 9 \mathrm { M H z }$ $\langle \lambda = 1 . 7 \ : \mathrm { m }$ ). DThere are 32 possible combinations, giving baselines of lengths varying from 100 to $3 2 0 0 \mathrm { ~ m ~ }$ . The east–west resolution is good $( \sim 1 . 2 ^ { \prime } )$ near the solar equator, and mediocre in the direction of the poles. The solar longitude of an event (a prominence) on the Sun can thus be well determined. Because of the great sensitivity of the detectors, the rapid evolution of solar flares can be followed with a time constant of less than one second, and this allows for correlations to be made between radio emissions and X-ray or EUV emissions observed in the corona from space (Fig. 6.37).

# Millimetre Arrays

The first millimetre interferometers were those at Hat Creek (California), Owens Valley (California), and Nobeyama (Japan). They were followed later by another at the Plateau de Bure in France in the 1980s. Millimetre wave radio interferometry encounters specific difficulties due to atmospheric absorption by $_ { \mathrm { H } _ { 2 } \mathrm { O } }$ , which increases at these wavelengths, and the correlative effects of atmospheric turbulence which begin to make themselves felt. On the other hand, for the same length of baseline $\pmb { B }$ , the resolution increases considerably as compared with centimetre wave observation. The millimetre region is also very rich in astrophysical information, particularly with regard to molecular spectroscopy, not only in the galactic interstellar medium but also in very remote quasars and galaxies. The possible combination of very high angular resolution and high sensitivity inspired an ambitious project at the beginning of the 2000s, with worldwide participation (Europe, USA, and Japan), namely the Atacama Large Millimeter Array (ALMA). The first images should become available around 2010.

Table 6.4 The main millimetre and submillimetre arrays. $N$ number of antennas, $D$ diameter of antennas. Updated in 2007   

<table><tr><td>Organisation and partners</td><td>Year</td><td>Site</td><td>Telescopes N×D</td><td>Baseline [km]</td><td>2min [mm]</td></tr><tr><td>Japan</td><td>1993</td><td>Nobeyama</td><td>6×10m</td><td>≤0.6</td><td>1-3</td></tr><tr><td>CARMA</td><td>2005</td><td>BIMA+OVRO (California)</td><td>9× 6.1m</td><td>≤2</td><td>1.0</td></tr><tr><td>CalTech and others</td><td></td><td>Owens Valley</td><td>6 × 10.4 m</td><td></td><td></td></tr><tr><td>IRAM CNRS/MPG/Spain</td><td>1985</td><td>Plateau de Bure (France)</td><td>6×15m</td><td>≤1</td><td>1.0</td></tr><tr><td>ALMA</td><td>2011</td><td>Chajnantor 5 100 m (Chile)</td><td>50 ×12 m</td><td>14</td><td>0.35</td></tr><tr><td>Europe/USA Smithsonian,Acad. Sinica</td><td>2005</td><td>Mauna Kea 4080 m</td><td>8×6m</td><td>≤0.5</td><td>0.6</td></tr></table>

Table 6.4 shows the very fast development of millimetre interferometry, which now extends to higher frequencies by using very high altitude sites like Mauna Kea in Hawaii and Cerro Chajnantor in Chile, where atmospheric transmission allows observation down to $6 5 0 \mu \mathrm { m }$ $( 4 6 0 \mathrm { G H z } )$ .

The Plateau de Bure Interferometer

This instrument has 6 mobile $1 5 \mathrm { m }$ antennas on an east–west baseline $1 0 0 0 \mathrm { m }$ long (Fig. 6.38). The resolution obtained at $\lambda = 3 ~ \mathrm { m m }$ is of the order of 2 arcsec. The Dsite is chosen for its atmospheric properties (altitude and hygrometry). However, variations in the refractive index of the air due to the humidity lead to phase fluctuations in the wavefront. These fluctuations limit the operating wavelength to $3 \ \mathrm { m m }$ in the summer, while observation at shorter wavelengths $( \lambda ~ \gtrsim ~ 1 ~ \mathrm { m m } )$ is possible in the winter.

# The Combined Array for Research in Millimeter Astronomy (CARMA)

This array in California began observations in 2005. On a baseline of about a kilometre, it brings together two older arrays, BIMA and OVRO, set up by different

![](images/9ddbda88a699f6f8e347ab148c542f8c956d6dc7ab2cbc1388e4e4484c7fcf95.jpg)  
Fig. 6.38 The radio interferometer at the Plateau de Bure (France), operating at millimetre wavelengths

US institutions, whence the name Combined Array for Research in Millimeter Astronomy (CARMA). It includes 23 telescopes of different sizes, from 3.5 to $1 0 . 4 \mathrm { ~ m ~ }$ , now connected to form the highest performing millimetre interferometer in the world, at least until ALMA goes into operation. It illustrates the remarkable flexibility of interferometric combination now achieved at radiofrequencies.

The Atacama Large Millimeter Array (ALMA)

The Atacama Large Millimeter Array (ALMA) is a joint project involving Europe (ESO), the United States (National Science Foundation), and Japan, to build an interferometer covering the Chajnantor plateau, which is about $1 0 ~ \mathrm { k m }$ across and situated at an altitude of $5 1 0 0 \mathrm { ~ m ~ }$ and latitude $2 0 ^ { \circ } \mathrm { S }$ in the Atacama desert in the Chilean Andes. The array will include about 50 mobile antennas of diameter $1 2 \mathrm { m }$ , providing a total collecting area of $5 \ : 0 0 0 \ : \mathrm { m } ^ { 2 }$ and operating down to a wavelength of $3 5 0 ~ { \mu \mathrm { m } }$ $( 9 5 0 ~ \mathrm { G H z } )$ . The sensitivity and image quality of the array and the prevailing atmospheric stability at this altitude will allow a very wide-ranging scientific programme, from exoplanets in the Galaxy to the study of galaxies and quasars in the early Universe (see Fig. 6.39).

# Very Long Baseline Interferometry (VLBI)

To reach the resolutions required by the sizes of radiosources (mas) at radiofrequencies, the only solution is to extend the baseline $B$ to the dimensions of continents. But this means solving the problem of recording IF signals locally and correlating the phases of the incident fields on each aperture, since cable transfer of the signals is no longer feasible. This particular coupling technique is called very long baseline interferometry (VLBI) and has been evolving now since 1967. At the time of writing (2007), extraordinary levels of resolution and flexibility have become possible.

The IF signal is recorded locally with a clock reading (atomic clock or hydrogen maser), the two clocks having been synchronised beforehand. These recordings, originally made on magnetic tape, but today on disk (2006), are then conveyed to a common point some time after the observation and ‘replayed’ in such a way that they interfere in a correlator and produce the interferometric signal (Fig. 6.40). Soon it may be possible to digitise the signal directly and send it by Internet, at least for frequencies below a few GHz.

![](images/1a3a6fda42dd2e8ae538cf58bd574124a96c99008caa87aae6c73dd8e7683a86.jpg)  
Fig. 6.39 Artist’s view of the ALMA interferometric array under construction in 2008 at the Chanjnantor site in Chile, at an altitude of $5 1 0 0 \mathrm { ~ m ~ }$ . The array is represented here at maximal deployment. Insert: Prototype $1 5 \mathrm { m }$ antenna. Document courtesy of the ESO

![](images/eae652d627a1753c7e23048b35ff28bbf813b6ec4c3b2f1ec90a23071232f441.jpg)  
Fig. 6.40 Schematic view of a conventional VLBI arrangement. From Moran J.M., Methods of Experimental Physics, Vol. 12C

Many corrections must be made to ensure that the correlation function effectively measures the coherence of the field at the two points considered. These must deal with effects related to the Earth’s rotation, phase drifts of the clocks, frequency drifts of the local oscillators, and others. The stability of the clocks (better than $1 0 ^ { - 1 4 }$ ) is such that the ultimate limitation for long exposures on intercontinental baselines is imposed by random phase fluctuations due to the Earth’s atmosphere.

The primary clock (see Sect. 4.3) is either a broadcast time signal from the GPS (Global Positioning System) satellite network, accurate to within $0 . 1 ~ \mu \mathrm { s }$ after correction for propagation irregularities introduced by the ionosphere, or a caesium clock reading, with a drift of around $0 . 2 5 ~ { \mu \mathrm { s } }$ per month. The local oscillator is a hydrogen maser, whose phase is locked to the clock, and whose relative phase stability is about $1 0 ^ { - 1 4 }$ over a period of up to $1 0 ^ { 4 } :$ s.

The signal is converted to an intermediate frequency (IF) signal with bandwidth $\Delta \nu \sim 0 . 1 \mathrm { M H \Sigma }$ z, implying a timebase stability of the order of $1 / \Delta \nu \sim 1 0 ^ { - 5 } \mathrm { s }$ .

 VLBI measurements make use of the more or less random locations of the large radiotelescopes around the world. The $w$ plane is thus only partially covered, even though improved by the Earth’s rotation (Fig. 6.41). VLBI resolution at centimetre wavelengths has long held the absolute record $( \gtrsim 1 0 ^ { - 3 }$ arcsec) by comparison with other wavelengths, and it is only recently, since the 1990s, that aperture synthesis in the visible has begun to attain similar angular resolutions.

![](images/f1a26cdc30c2a9c395d89360484314bed2d81ecac5a80dafa5e37f16d95b4850.jpg)  
Fig. 6.41 Partial aperture synthesis by VLBI. Left: Location of North American antennas used. Right: Map of $\mathrm { H } _ { 2 } \mathrm { O }$ maser emission $( \lambda ~ = ~ 1 . 3 5 ~ \mathrm { c m }$ , $\nu = 2 2 . 2 \mathrm { G H z }$ ) from the young galactic Dsource GL 2591, an extremely dense cloud situated at $2 \mathrm { k p c }$ from the Sun. Note the high angular resolution and the beam profile. Inset: Spatial frequency coverage of the $( u , \nu )$ plane, resulting from the pairing of antennas and the Earth’s rotation $\scriptstyle ( u , \nu$ have units $D / 1 0 ^ { 7 } \lambda$ ). The baselines have lengths varying from $2 2 8 \mathrm { - } 3 9 2 9 \mathrm { k m }$ . After Walker et al., Ap. J. 226, 95, 1978. With the kind permission of the Astrophysical Journal

![](images/7a47fbaaa8bba909344dbaa76e93e7f4e05114c4a261889df1e2864125c3bbb9.jpg)  
Fig. 6.42 Worldwide network of radiotelescopes which can be combined in VLBI observations (2007). Regional networks are organised in Europe with the European VLBI Network (EVN), and in the USA with the Very Long Baseline Array (VLBA). Most of the instruments featured here are radiotelescopes, but some are specific to terrestrial geodesy, using VLBI to study continental drift and the deformations of the land masses over time. New instruments are frequently added to this network, e.g., the Antarctic

At the end of the decade 1980–1990, VLBI had been extended to millimetre wavelengths, thus putting large new antennas (30 to $5 0 \mathrm { m }$ ) to good use. In addition, the stability of frequency standards is improving (superconducting cavity oscillators, whose frequency width is thus reduced), the frequency range of recording equipment is increasing $\mathrm { ( > 1 0 0 M H z ) }$ ), and so, too, is the number of spectral channels (up to 1 024, see Sect. 8.4). Resolutions better than $1 0 ^ { - 4 }$ arcsec have been achieved in the millimetre region.

There is a very interesting application of VLBI to continental geodesy. Before the development of the Global Positioning System (GPS) in the 1990s, VLBI was able to detect the slow movements of continental drift over distances of the order of the size of the Earth.

The extension of VLBI to space observation is an interesting prospect. A telescope in a more or less elliptical orbit around the Earth, coupled to ground-based telescopes, would sweep out a large part of the spatial frequency plane during its orbit, and thus lead to measurements of high spatial frequencies, with good coverage of the $( u , \nu )$ plane. The onboard reference phase would be provided by a groundbased clock, of relative stability around $1 0 ^ { - 1 4 }$ , whose signal would be transmitted to the satellite and then returned to the ground by two-way telemetry. Before arbitrarily increasing the resolution, the brightness and compactness of the intended objects of study must be ascertained, so as to be sure that one resolution element does indeed emit sufficient power to stand out from the instrument noise.

The VLBI satellite now called the Space Observatory Project (VSOP then HALCA, Japan) was launched in 1997. Its maximum distance from Earth or apogee is at $2 1 4 0 0 { \mathrm { k m } }$ . Its $1 0 \mathrm { m }$ antenna operates at $\lambda = 6$ and $1 8 \mathrm { { c m } }$ (OH radical band), Dand its signals can be combined with data from terrestrial arrays like the VLBA (US), the European VLBI Network, or the Australian network (Fig. 6.42).

# 6.5.2 Ground-Based Optical Arrays

The three possible kinds of optical (visible and infrared) interferometry were described above, discussing the performance that can be achieved with each: direct, heterodyne, or homodyne combination of the beams delivered by the different telescopes. After abandoning the last around 1980, it was the first of these methods that attracted most interest at the beginning of the 2000s, resulting in the arrays set up around the world at the beginning of the twenty-first century. Figure 6.43 shows how these developments have gradually led to the arrays and networks we find today. However, the homodyne and heterodyne methods may reappear at some point in the future in other configurations, e.g., giant ground-based telescopes, space arrays, wavelengths in the far infrared, and so on.

![](images/fb74f9bbe6a23511a30c9e70002e5c5bf329e4daef221444da5b49f0fc4474c8.jpg)  
Fig. 6.43 Progress with the different approaches to ground-based optical (visible and infrared) interferometry between 1974 and 2006. Systems remaining in activity after this last date are extended with a . Diagram courtesy of Peter Lawson and completed by the authors

Here we examine the arrays based on two of the above methods, viz., heterodyne, then direct, and look at some of the results.

# Optical Interferometry: Infrared Heterodyne Method

The Infrared Spatial Interferometer (ISI) at the University of California, built on Mount Wilson in the 1980s, includes two mobile, $1 . 6 5 \mathrm { m }$ telescopes, with baselines of 4 to $7 0 \textrm { m }$ . Its special feature is that it uses the heterodyne technique at a wavelength of $1 0 . 6 ~ { \mu \mathrm { m } }$ , a $\mathrm { C O } _ { 2 }$ laser providing the local oscillator signal, and a mixer producing an IF signal in the usual way, with maximal frequency band 0.2 to $2 . 8 \ : \mathrm { G H z }$ . The sensitivity of the instrument is thus reduced by the narrowness of this spectral band. Nevertheless, the transfer of IF signals by cable is more convenient, using techniques tried and tested at radiofrequencies, and there exist several hundred stars in dust clouds which are bright enough to provide interference fringes with satisfactory signal-to-noise ratio, so the instrument is indeed a high quality tool (Fig. 6.44). On the other hand, high angular and spectral resolutions can be combined here, an advantage so far unique to this type of instrument, which can achieve a spectral resolution of $5 \times 1 0 ^ { 2 }$ . It has thus been possible to study the formation of ammonia $\mathrm { N H } _ { 3 }$ or silane $\mathrm { S i H _ { 4 } }$ molecules in evolved stellar atmospheres (like $\mathrm { I R C } + 1 0 2 1 6$ ).28

CGround-based heterodyne interferometry is unlikely to be a technique of the future for the reasons already stated. But in space, Table 6.3 shows that there is a crossover with the performance of direct interferometry in the far infrared and submillimetre regions, in particular when studying sources emitting in a spectral band. The future will no doubt tell whether this method can be successfully applied in space for these wavelength regions, which are still the least explored in the electromagnetic spectrum.

# Optical Interferometry: Michelson Method

As soon as optical interferometry came back on the scene in 1975, the idea of telescope arrays which had proved so effective at radiofrequencies became a major objective (Fig. 6.45). The family of optical interferometry arrays has moved forward very quickly since the 1980s, and the main technical problems have been resolved (Fig. 6.43 and Table 6.5). The advent of adaptive optics, which could make very large apertures (up to $1 0 \mathrm { m }$ ) spatially coherent, resulted in the use of large telescopes like VLT and Keck in interferometric mode.

![](images/c34baff480dc2c356e4a8a1e8c3e368871ebf5d18c77a18cb24a444881a112b5.jpg)  
Fig. 6.44 Power spectral density (in arbitrary units) of the interferometer signal (fringes) obtained using the heterodyne interferometer ISI at $\lambda = 1 0 . 6 \mu \mathrm { m }$ on the star $\alpha$ Orionis (Betelgeuse) in 1992. The frequency of the fringes, close to $1 0 0 \mathrm { H z }$ D, is determined by the Earth’s rotation, the position of the source in the sky, and the baseline vector $\pmb { B }$ . During the observation, the atmosphere causes a large and time-variable differential phase between the two optical paths, producing the ‘accordion’, or frequency modulation, effect on the fringes. This significantly widens the peak of the spectral density (by around $2 0 \mathrm { H z }$ ) and correlatively reduces its amplitude. Total observation time $4 . 5 \mathrm { { m i n } }$ . After Townes C.H. et al., Infrared Phys. 35, 1994

The Very Large Telescope Interferometer (VLTI)

The optical interferometer associated with the European Very Large Telescope went into operation in 2001, and at the time of writing (2007) is the most flexible and powerful instrument of its kind. High up on the Cerro Paranal in Chile, the four fixed $8 . 2 \textrm { m }$ telescopes are supplemented by an array of four mobile $1 . 8 \mathrm { ~ m ~ }$ telescopes that can be moved to any of 30 different positions (Fig. 6.46). Each telescope is equipped with adaptive optics. In the interferometric focal plane, the beams from two to at most four telescopes (in 2007), of either diameter, can be made to interfere after being brought by means of delay lines to a path length difference close to zero. Fringe detectors are positioned at the common focus. The first generation of instruments measures fringe visibility in the range $8 \mathrm { - } 1 3 ~ \mu \mathrm { m }$ (MIDI instrument, with spectral resolution up to 230) and $1 { - } 2 . 2 ~ { \mu \mathrm { m } }$ (AMBER instrument, spectral resolution up to 300). In addition, the system can operate in phase closure in order to measure the amplitude and phase of complex visibilities when simultaneously accepting the beams from three telescopes: 254 baselines are possible, extending up to $2 0 0 ~ \mathrm { m }$ , and able to supply up to 3 025 closure relations. A fringe tracker can compensate for random path length differences produced by atmospheric turbulence, provided one uses a bright enough star to ensure that the signal-to-noise ratio is sufficient during the atmospheric coherence time $\tau _ { \mathrm { c } }$ (similar magnitude limits to those for adaptive optics).

![](images/148aa4b448afdc3079a557469ad6607828e5d0edc0c1581d25c2cb772d7e0d47.jpg)  
Fig. 6.45 Artist’s impression of an array of $1 . 5 \mathrm { m }$ telescopes used for visible and infrared aperture synthesis. Note the rails allowing variation of $\pmb { B }$ , and also the common focus where the beams are recombined. The spherical mounting of the telescopes is novel. (Labeyrie A., La Recherche 76, 421, 1976. With the kind permission of La Recherche)

After 2009, a new generation of instruments should allow phase closure with four telescopes, high enough astrometric accuracy (around $1 0 0 ~ \mu \mathrm { a s } )$ for detecting the reflex motion of stars with massive exoplanets, and eventually the possibility of imaging the region close to the central black hole of the Galaxy with a desired astrometric accuracy of a few tens of $\mu { } \mathrm { a s }$ .

# The Keck Interferometer (KI)

Since 2001, the two $1 0 \textrm { m }$ telescopes located at the top of Mauna Kea (Hawaii), which are about $8 0 \textrm { m }$ apart, can be coherently coupled. This interferometer was specifically designed for observing exoplanets, and since 2005 has been equipped with a nulling fringe mode (see Sect. 6.6), which requires the use of high performance adaptive optics.

Table 6.5 Optical interferometric networks. In the uses column, $\lvert \mathcal { V } \rvert$ spectral amplitudes, I imagj jing, S spectroscopy, A astrometry, and N nulling. Data updated as of 2007   

<table><tr><td>Name</td><td>Site</td><td>Number and diameter of telescopes</td><td>Baselines [m]</td><td>Region [μm]</td><td>Uses</td></tr><tr><td>SUSI</td><td>Narrabri (Australia)</td><td>5 × 0.14</td><td>5-640</td><td>0.40-0.75</td><td>I,A</td></tr><tr><td>GI2T (Regain)</td><td>Calern (France)</td><td>2 ×1.5m</td><td>12-65</td><td>0.57-0.70</td><td>,S</td></tr><tr><td>VLT</td><td>Cerro Paranal</td><td>4×8.2m</td><td>20-200</td><td>1-12</td><td>I, S, A, N</td></tr><tr><td>interferometer PTI</td><td>(Chile) Mt. Palomar</td><td>4×1.8m 3 ×0.4m</td><td>110</td><td>2-2.4</td><td>A</td></tr><tr><td>Keck</td><td>(California) Mauna Kea</td><td>2×10m</td><td>85</td><td>2.2-10</td><td>||,N</td></tr><tr><td>interferometer NPOI</td><td>(Hawaii) Flagstaff</td><td>6×0.5m</td><td>2-437</td><td>0.45-0.85</td><td>A</td></tr><tr><td>COAST</td><td>(Arizona) Cambridge</td><td>5 × 0.65 m</td><td></td><td></td><td>I, S</td></tr><tr><td>IOTA</td><td>(UK) Mt. Hopkins</td><td>3×0.45m</td><td>5-38</td><td>1-2.4</td><td>I,S</td></tr><tr><td>CHARA</td><td>(Arizona) Mt. Wilson</td><td>6×1.0 m</td><td>34-331</td><td>0.55-2.4</td><td>I, S</td></tr><tr><td>MIRA</td><td>(California) Mitaka</td><td>2 × 0.3m</td><td>30</td><td>0.8</td><td></td></tr><tr><td>1 and 2 MROI</td><td>(Japan) Magdalena Mt.</td><td>6×1.4m</td><td>7.5-350</td><td>0.6-2.4</td><td>I, A, S</td></tr><tr><td>(2008) LBT</td><td>(New Mexico) Mt. Graham</td><td>2 ×6.5m</td><td>22.8</td><td>1-20</td><td>1,S</td></tr><tr><td>(Fizeau) ISI</td><td>(Arizona) Mt. Wilson</td><td>3 × 1.65 m</td><td>4-70</td><td>10.6</td><td>1,S</td></tr></table>

![](images/72a04d708cb46e2d8e5d2796c69ffc3b697131e87035bef2e167da8b7ff5d868.jpg)  
Fig. 6.46 Three of the mobile $1 . 8 \mathrm { m }$ telescopes of the VLTI, which is the interferometric configuration of the Paranal VLT. Original photo with the courtesy of Pierre Kervella

Optical Arrays and Densified Pupils. Consider a source $S _ { 1 }$ placed on the optical axis of two or more telescopes forming an interferometer. A fringe system is obtained at the common focus. Will a second source $S _ { 2 }$ situated at an angular distance $\alpha$ from $S _ { 1 }$ then be observable? For this to be the case, several conditions must be fulfilled. First of all, it must remain in the field of each telescope, which is usually quite wide. Secondly, the light beam from $S _ { 2 }$ must be able to propagate to the common focus, in particular through the delay lines, without being diaphragmed. This condition determines a maximum value $\alpha _ { \mathrm { m } }$ , which depends on the dimensions of the transfer optics. In the VLT interferometer, $\alpha \approx 2$ arcsec, which is a very small value, resulting from the hectometric optical paths to be travelled between telescope and common focus. One final condition concerns the configuration of the exit pupils, which must be homothetic to the configuration of the entrance pupils in order to ensure the fringe contrast for all $\alpha \leq \alpha _ { \mathrm { m } }$ . The latter condition, long considered intangible, is even referred to as the golden rule of an interferometer.

Now consider the common focal plane when an interferometer comprises several dilute entrance pupils, i.e., the diameter $D$ of the telescopes is very small compared with their separations $B$ , and observe a point source while satisfying the above homothety condition. The diffraction pattern of this telescope array leads to a significant spread of the PSF in the focal plane, making it very difficult to implement any coronagraph technique for eliminating the signal from this source in order to observe any very faint companions in its gravitational sphere. Suppose then that the exit pupil is rearranged, e.g., so that the exit pupils are now in contact with one another. The homothety condition is no longer satisfied, and the field $\alpha _ { \mathrm { m } }$ will be significantly reduced. On the other hand, the exit pupil will be more like that of a single telescope, and the PSF will have a bright central peak surrounded by secondary lobes. It will thus be easy to mask. It is straightforward to show that the reduction of the field is proportional to the rearrangement factor measuring how much the pupils are brought together as compared with the homothetic situation.

This remarkable idea of pupil densification, put forward by Antoine Labeyrie in 2000, led to the notion of hypertelescope. This could include, especially in space, several tens of apertures of metre dimensions, possibly several kilometers apart, but nevertheless delivering, in a tiny field, a highly concentrated interference pattern that would be easier to detect and cancel out if necessary.29

# Optical Interferometry: Fizeau Method

This refers to an arrangement in which delay lines serve no purpose since the equality of the optical path lengths between the different pupils and the common focal plane is satisfied by construction. Here is an example of just such a configuration.

The Large Binocular Telescope (LBT)

This instrument on Mt. Graham (Arizona) has been gradually set in operation since the end of 2005. It consists of two telescopes with diameter $D \ = \ 8 . 4 \ \mathrm { m }$ , fitted on the same altazimuth mount with their optical axes $B ~ = ~ 1 4 . 4 \mathrm { ~ m ~ }$ apart. The instrument thus looks like a conventional telescope, except that the entrance pupil is disconnected, comprising two distinct apertures. The highest observable spatial frequency is therefore $( B + D ) / \lambda$ . The baseline of the two telescopes is always Cnormal to the incident direction, so no delay line is required to compensate — except one of very small amplitude to adjust the zero PLD — and the interferometric field therefore has the same limitations as the normal imaging field of a telescope, i.e., several arcmin, much higher than an interferometer in the Michelson configuration. The mirror train is reduced to the strict minimum, i.e., primary, secondary, tertiary, then a return mirror on each beam is enough to supply the common focus. Alternatively, the two telescopes can be used with two independent instruments, but constrained to observe the same source, or at least the same region of the sky.

Roger Angel30 put forward the interesting idea known as $2 0 + 2 0$ , in which two independent telescopes of diameter $2 0 ~ \mathrm { m }$ each (for example) can move around a circular rail of diameter $B _ { \mathrm { M } }$ . Positioning the two telescopes at the ends of a chord of this circle of length $B \le B _ { \mathrm { M } }$ , arranging for the common focal plane to pass through the middle of this chord, and moving the two telescopes in such a way that the chord is always normal to the azimuth of the line of sight, the result is an interferometer with adjustable baseline $B$ , operating in Fizeau mode, hence without delay line. As in all interferometric setups using large pupils $\left( D \gg r _ { 0 } \right)$ ), the latter must be equipped with adaptive optics to restore coherence of the incident waves.

# Fibre Interferometry: Optical Hawaiian Array for Nanoradian Astronomy (’OHANA)

In fact, the acronym ’OHANA suggested by the French astronomer Jean-Marie Mariotti (1955–1998) has a double meaning, since it is also the Hawaiian word for ‘family’.

It is easy to understand how the need to transport the beams from each telescope to the common focus using a set of mirrors makes it practically impossible to achieve very long baselines, i.e., of hectometric order or more, on the ground. This stumbling block is avoided by extracting the light from the focus of each telescope and transferring it to the common focus by a single-mode optical fibre, which propagates the phase of the wave while preserving its temporal coherence (see Sect. 6.4.2). By choosing fibres of equal length from each telescope to the common focus, one can be sure that the optical paths are equal, and of course without atmospheric effects. It remains to obtain a zero path length difference using a variable delay line, as in a Michelson setup. Demonstrated in 2006 in the near infrared between the two Keck telescopes on Mauna Kea (Hawaii),31 this promising idea would make it possible, by coupling all the large telescopes located on this peak (Fig. 6.47), to obtain images of the cores of active galactic nuclei (AGN) like NGC1068 with resolutions as high as $2 0 0 \mu \mathrm { a s }$ .

![](images/c7efd180502996e5bf64c9dd095b8cd0cac990c6926a83918d39cfa9a82d353c.jpg)  
Fig. 6.47 Concentration of optical telescopes at the Mauna Kea site in Hawaii. The idea of fibre optic coupling can be used to connect two or more of these telescopes interferometrically, directly extracting light from Coude or Cassegrain focal points. The possible interferometric baselines are´ indicated on the left, while the insert on the upper right compares the arrangement of the four $8 . 2 \mathrm { m }$ telescopes of the VLT. Dotted circles show the first two configurations implemented in the first decade after 2000. From Mariotti J.M., 1995 and Perrin, G., 2006. Map due to the Institute for Astronomy, Honolulu. Altitudes are given in feet, where 1 foot $= 0 . 3 0 5 \mathrm { m }$

# Some Results from Optical Interferometry

Since the 2000s, optical interferomety has become a rapidly expanding technique in astronomy thanks to results that could be obtained in no other way. To see an example of this, consider Fig. 6.48, which shows the astrometric performance obtained in the 1970s with the first optical interferometers. The aim there was to measure stellar diameters, and the diameters of the orbits in close binary star systems from which the star masses could be deduced.

Figure 6.49 shows the accuracy that could be achieved in 2006 in the measurement of a visibility, and the way its wavelength dependence could be used to accurately specify the radial intensity distribution of a stellar atmosphere. In the example chosen here, the interferometric observation of Cepheid variables, crucial for determining distances in the Universe, provides a way of refining the accuracy of this fundamental length scale.

![](images/8e2b34fdf7be0cb106ff588ec31e4caf505ab50613602f864d4461cd61367f04.jpg)  
Fig. 6.48 Astrophysical and astrometric applications of aperture synthesis in the visible. Observations of the double system Capella $\scriptstyle ( { \alpha }$ Aurigae) A and B. Circles mark the two component stars, resolved and shown with their apparent diameters. X marks positions predicted for B on its orbit (Finsen). Shading indicates measured positions of B at different epochs (projections of baselines on the sky are shown at the same Julian dates, which are marked). Note the excellent resolution in the direction of the baseline, and the poor resolution in the perpendicular direction. Measurements obtained at the Plateau de Calern, France, with two $2 5 \mathrm { c m }$ telescopes. From Blazit A. et al., Ap. J. 217, L55, 1977. With the kind permission of the Astrophysical Journal

# 6.5.3 Space-Based Optical Interferometry

The difficulties caused by the Earth’s atmosphere, like those due to the Earth’s rotation (the need for continuously variable delay lines), have been sufficiently emphasised to show why space looks such a good place to set up optical interferometers, observing from the visible to the far infrared. But one should not underestimate the difficulties of quite another order raised by this undertaking: the need for telescopes flying in formation as soon as baselines exceed about ten metres and a supporting beam can no longer be used; variation of baselines to sample spatial frequencies; and holding optical paths to within a fraction of a wavelength. This is why, despite many proposals and projects, the spaceborne optical interferometers will not appear before 2010–2020. Two of these missions, currently under study, will be discussed here.

![](images/7df5a1ac8d1e143e75a2131f5280f77adc497c595b4700b6fbc29238ff9bc6de.jpg)  
Fig. 6.49 First demonstration of the presence of interstellar matter around the Cepheid star $l$ Carinae, using optical interferometry. The measured visibility (squared modulus) $\mathcal { V } ( \lambda ) ^ { 2 }$ is plotted versus $\lambda$ , in the atmospheric window around $\lambda = 1 0 ~ \mu \mathrm { m }$ . The VLTI works here with two $8 . 2 \textrm { m }$ telescopes, on a baseline $D = 4 0 ~ \mathrm { m }$ D, which sets the spatial frequency $D / \lambda$ at each $\lambda$ . At these wavelengths, the accuracy on $\mathcal { V } ( \lambda ) ^ { 2 }$ is limited by atmospheric and thermal noise. The star, with a photospheric radius of $2 . 7 0 \ \mathrm { m a s }$ , is practically unresolved, while the measured $\mathcal { V } ( \lambda ) ^ { 2 }$ shows the presence of a resolved envelope of ${ 8 \pm 3 }$ milliarcsec radius. Such envelopes are due to the periodic ˙ejection of matter by the pulsating star. The two curves (continuous and dashed) correspond to two different interferometric calibrations, using an unresolved star without envelope. Document Kervella, P. et al., Astron. Astroph. 448, 623 (2006)

# The Space Interferometry Mission (SIM) and NASA’s PlanetQuest

This astrometric mission aims to study extrasolar planets and at the same time to make exceptionally accurate measurements of the parallax of stars in the Galaxy.32

A 9-m beam, which can be oriented in space, will carry a series of $3 0 \mathrm { c m }$ telescopes that can be combined to form several interferometers. The common focal plane will be equipped with a CCD detector on which the fringes will form, in the spectral region $0 . 4 \mathrm { - } 0 . 9 ~ \mu \mathrm { m }$ . The instrument, placed in orbit around the Sun, will gradually move away from the Earth during its 5 year mission.

The key feature of the Space Interferometry Mission (SIM) is its high angular resolution. The diffraction limited resolution $\lambda / D$ is 20 mas. However, two factors allow the system to improve considerably on this limit. The first is instrumental stability since, in the absence of any atmosphere, the fringes are stable to better than $\lambda / 1 0 0$ for several minutes, allowing long time integrations, and hence extreme sensitivity (limiting magnitude $m _ { \mathrm { V } } = 2 0$ ). The second factor is that it can operate Din differential mode, comparing the positions of two nearby objects by the observed fringe shifts they each produce. This is how SIM can achieve resolutions in the range $1 { - } 4 \mu \mathrm { a s }$ . This mission could be launched in the decade from 2010.

In order to detect extrasolar planets, SIM would not observe the planet directly directly, since it would be too faint, but rather would measure the angular distance between the star $S$ thought to hold the planet and a distant reference star $S _ { \mathrm { R } }$ . Over time, the angle between $S$ and $S _ { \mathrm { R } }$ will vary for several reasons, i.e., proper motion of the stars and different parallaxes, but it will also vary if $S$ carries a planet, orbiting like $S$ around the centre of mass of the system. With a sensitivity of a few $\mu { } \mathrm { a s }$ , it will be possible to detect planets with comparable or even smaller masses than the Earth, after eliminating the two other effects, which can be determined independently.

To measure the distance of a star in the Galaxy, SIM will measure its parallax during the year, by simultaneous and oft-repeated observation of a reference star belonging to a reference grid distributed across the whole sky. With an ultimate resolution of $4 ~ \mu \mathrm { a s }$ , equal to the parallax of an object at a distance of $2 5 0 \mathrm { k p c }$ , SIM will be able to reach stars almost throughout the whole Galaxy with a very high level of accuracy.

With these two goals, SIM will complement the Corot and Kepler missions in search of exoplanets and also the GAIA mission for astrometry (see Sect. 4.2).

# ESA’s Darwin Mission

First proposed in 1993, just before the discovery of the first extrasolar planet in 1995, this mission33 exploits the technique of nulling interferometry This will be discussed in detail later (Sect. 6.6), in the context of coronagraphy techniques. For the moment, we shall just describe the array of telescopes, each with diameter $3 { \mathrm { - } } 4 \mathrm { m }$ , placed in a plane perpendicular to the line of sight as shown in Fig. 6.50. At the common focus, a dark interference fringe is formed at the position of the star, while the interference remains constructive at the suspected position of the planet, leading to a maximum amount of light, which must then be distinguished from the noise background, or the exozodiacal light, if there is any, due to dust present in the planetary system (as in our own Solar System). The instrument will operate in the wavelength range $6 . 5 \mathrm { - } 1 8 ~ \mu \mathrm { m }$ , in order to maximise the contrast between the star and the planet on the one hand, and in order to fall within the spectral region containing the spectral signature of ozone $\mathrm { O } _ { 3 }$ on the other. A low spectral resolution ( $R = 2 0$ ) suffices to reveal the presence of this molecule, which in turn indicates Dthe presence of oxygen. Placed at Lagrange point L2, it is relatively easy to protect it against radiation from the Earth, the Sun, and the Moon, since, viewed from L2, these three bodies remain more or less aligned all the time.

![](images/8fc8949d943c93662b6fd307ec36ce3d0a170f528c52fc077d427ee4712e9b73.jpg)  
Fig. 6.50 Artist’s view of a possible configuration for the ESA’s Darwin mission. A fleet of four independent satellites, each carrying a telescope and flying in formation, constitutes an interferometer. The interferometric signal is produced and processed by a fifth spacecraft, at which the four beams from the others are made to converge. It also provides the communications link with the Earth and the necessary energy via its solar panels. The whole system is placed at Lagrange point L2. Since its design in 1990, the configuration has been continually improved, in particular, by reducing the number of telescopes and hence the cost. (European Space Agency, 2007)

# Interferometry and X-Ray Radiation

It is already difficult at visible wavelengths to maintain the equality of optical paths at a small fraction of the wavelength. So how could one go about doing this at wavelengths a thousand times shorter, in the nanometre range, in order to resolve the X-ray emission produced in the immediate neighbourhood of a black hole? This is the challenge faced by the MAXIM space mission,34 under study at NASA. The environment of the black hole in the galaxy M87 (see Fig. 6.36), with estimated mass $M = 1 0 ^ { 8 } M _ { \odot }$ , is a bright $\mathrm { X }$ -ray source. The black hole has a Schwarzschild radius of $1 0 ^ { 1 1 } \mathrm { ~ m ~ }$ ˇ, which would require a resolution of $0 . 0 5 ~ \mu \mathrm { a s }$ at the distance of $1 8 \mathrm { { M p c } }$ to resolve it.

Young fringes have already been obtained with X rays in the laboratory,35 a natural consequence of their wave nature. In space, considering X rays of $1 \ \mathrm { k e V }$ $( \lambda \approx 1 \ \mathrm { n m } )$ , an angular resolution of $2 0 0 ~ \mu \mathrm { a s }$ could be achieved with a baseline of $B ~ = ~ 1 ~ \mathrm { m }$ , and telescopes with collecting areas of $1 0 0 ~ \mathrm { c m } ^ { 2 }$ would provide a Dcomparable sensitivity to the Einstein and Rosat missions. But the difficulty here lies in the detection of the fringes. On the one hand, their separation must be increased by interfering the beams (two or more, depending on the number of pupils used) over a very small angle. To obtain an fringe spacing of $1 0 0 ~ { \mu \mathrm { m } }$ with $\mathrm { X }$ rays of wavelength $1 \ \mathrm { n m }$ , the necessary amplification is $1 0 ^ { 5 }$ , which thus requires an angle of $1 0 ^ { - 5 }$ rad. The distance between the structure carrying the mirrors and the focal plane is therefore $1 0 ^ { 5 } B$ , or at least $1 0 0 \mathrm { k m }$ . As in the Darwin or LISA missions, the problem is to achieve highly accurate navigation of independent satellites (formation flight), here between the structure carrying the mirrors and the one carrying the detectors. At the same time, sufficient spectral selectivity is needed so that it is not necessary to obtain zero PLD in order to find the fringes: a spectral resolution of $1 0 ^ { 2 }$ to $1 0 ^ { 3 }$ is required to achieve this, leading to fringes that could be observed over several millimetres.

In a second stage, the baseline could be extended by further separating the satellites carrying each of the collecting mirrors. These ambitious missions involve complex technological development and are unlikely to see the light of day before 2020–2030.

# 6.6 High Dynamic Range Imaging (HDRI)

When imaging certain astronomical objects, there are some special cases in which the contrast in brightness between different regions of the field of view is extremely high, varying by a factor of as much as $1 0 ^ { 1 0 }$ . This is the case, for example, with the solar corona in the vicinity of the photosphere, circumstellar disks or exoplanets not far from a star, and active galactic nuclei. The generic term coronagraphy refers to all those methods aiming to obtain the image of a faint field around a very bright source by effectively masking the latter. These methods are also called high contrast imaging or high dynamic range imaging (HDRI).

# 6.6.1 Coronagraphy and Apodisation

In the case of an almost point source such as a star or active galactic nucleus, surrounded by structure of some kind separated by only a very small angle, e.g., disks or planets, high angular resolution is required, and adaptive optics and interferometry become essential. The dynamic range can be considerable, even as high as $1 0 ^ { 9 } – 1 0 ^ { 1 0 }$ .

Coronagraphy comes from the Latin word corona, meaning crown. Indeed, the technique was invented by Bernard Lyot,36 when attempting to image the solar corona in the years 1940–1950, by masking the solar disk, a million times brighter than the corona, in order to reveal the corona’s flamboyant activity.

Following the work by Lyot, who had the extremely powerful idea of putting a mask, not only in the focal plane, but also in the plane conjugate to the pupil, the only notable innovation over several decades was conceived by Jacquinot.37 He had the idea of reducing the amplitude of the feet of the diffraction pattern of the bright source by modulating the transmission by the pupil. This is the basic idea of apodisation, already mentioned briefly in Sect. 6.1.

It was only at the beginning of the 2000s, following the discovery of the first extrasolar planets, that this technique suddenly came back into the fore. The aim of forming the image of such planets in orbit around their star became a powerful driving force, resulting in an explosion of new concepts. It is important to realise just how difficult this is. The problem is to capture and identify, at a typical angular distance of 0.1 arcsec from a star, the photons from a companion that is $1 0 ^ { 1 0 }$ times (25 magnitudes) less bright, these values corresponding to the case of a system like the Sun–Earth system at a distance of $1 0 \ \mathrm { p c }$ from the observer (a frequently used case study).

# The General Problem

In almost all imagined solutions, the rule is to mask or otherwise extinguish the bright source, because the smallest leak of its photons would be disastrous. In addition, the wings of the diffraction pattern, which extend a long way, are sources of photon noise. Using the Fourier formalism, we first express the problem in complete generality, considering the optical system shown in Fig. 6.51 (lower). The entrance pupil modulates the amplitude of the incident wave, a phase and/or amplitude mask is placed in the focal plane on the axis of the bright source, and an image is once again formed on a pupil diaphragm, in order to block any residual diffracted light.

![](images/a17ccda7dca474b710d58bc8db24fe55a5c435a17ade2ed35f48bd47d4325dff.jpg)  
Fig. 6.51 Configuration of the Lyot coronograph. Light goes from left to right. Top: Without a stop in pupil C, the wings of the PSF appear in the final image plane D because of the diffracted light (edge rays). Bottom: The introduction of a stop in the reimaged pupil C blocks this contribution. The lens placed in the first focal plane B reimages the pupil, while the second lens in C provides the final focal plane image D. Source C. Aime & R. Soummer

Let $u ( x , y )$ be the amplitude in the pupil plane (1 in the pupil and 0 outside, if there is no modulation). Then the amplitude in the focal plane is $\nu ( x , y ) = \tilde { u } ( x , y )$ , where $\tilde { u }$ is the Fourier transform of $u$ D Q. Applying the focal mask amounts to writing

$$
\nu ( x , y ) = \widetilde u ( x , y ) \left[ 1 - M ( x , y ) \right] ,
$$

where $M$ is a complex quantity whose modulus $( \leq 1 )$ and argument describe the attenuation and phase shift introduced by the mask, respectively. In particular, $M$ equals unity where the mask is opaque and $M \ = \ 1 - \exp \mathrm { i } \pi \ = \ 2$ where the mask introduces a phase shift of $\pi$ D  D. In the conjugate pupil plane, the amplitude then becomes

$$
w = \tilde { \nu } = ( u - u \star \tilde { M } ) \times D ~ ,
$$

where $D$ is the diaphragm function. The amplitude $w$ thus results from the difference between the direct wave and the diffracted wave, a difference to which the pupil diaphragm is then applied.

The general problem raised by high dynamic range imaging is to make $w$ zero or minimal within the diaphragm. If we consider the space of free parameters represented by the modulation of the amplitude of the wave transmitted by the pupil, the modulations of the amplitude and phase of the wave transmitted by the focal plane, the amplitude of the wave transmitted by the pupil diaphragm and the shape of the latter, it is easier to understand how so many different solutions could have been put forward. However, we may consider two main families of solutions based on this scheme: those playing on the focal mask, referred to under the heading of coronagraphy, and those seeking to reconfigure the PSF, either on a bounded support, or by processing the residual faint regions in the final field, which come under the heading of apodisation.

Finally, the general heading of interferometric techniques will cover all other solutions, using a more sophisticated optical setup than the one shown in Fig. 6.52 and aiming explicitly to produce destructive interference to extinguish the bright source.

![](images/b6f2da8551564c89bc6365a72dfe8cb36100791f3d552b9db461a9608df1e7b4.jpg)  
Fig. 6.52 Example of the progression of light in a coronagraphic system. This basic Lyot scheme offers many possible variations and improvements, discussed in the text. From top to bottom: Uniform wave amplitude on the entrance pupil. Effect of an occulting mask in the first focal plane. Effect of a Lyot stop in the second pupil plane. Final image in the second focal plane. From R. Galicher

# Coronagraphy

The problem faced by Lyot when viewing the solar corona was to considerably reduce the light from the Sun’s disk, diffracted and scattered by all the optical defects.

The Lyot Coronagraph

The first and most natural idea is to place an opaque mask in the focal plane, slightly larger than the image of the solar photosphere. What Lyot then noted was that the diffraction by the mask itself, but also by all the tiny defects in the optical system, such as dust or phase defects, was the source of a significant diffuse background.

Indeed, consider an opaque particle of diameter $d$ in the focal plane. It diffracts a wave coming from a given direction into a solid angle of characteristic half-angle $\theta \ = \ \lambda / d$ . For example, if $d$ is of the order of the size of the diffraction spot, Di.e., $f \lambda / D$ ( $f$ being the focal length of the telescope and $D$ its diameter), then $\theta = D / f$ , i.e., the same angle as the geometrical beam. The convolution of the two Dsolid angles (geometrical and diffracted) means that a significant part of the light ends up outside the geometrical beam (of the order of $7 5 \%$ in our example). If an opaque mask containing a circular hole slightly smaller than the geometric pupil is placed in the plane conjugate to the pupil plane, then most of this diffracted light gets blocked, while light from another point of the field, not affected by our particle, will follow the path predicted by geometrical optics and will go through almost unaffected. Figure 6.51 shows this configuration.

Let us examine this result using the Fourier formalism introduced above. In the expression

$$
w = \mathrm { F T } \left( \nu \right) = \left( u - u \star \tilde { M } \right) \times D \ ,
$$

$D$ and $M$ are box or top-hat functions, equal to unity within the radius of the mask or diaphragm and zero outside. $\tilde { M }$ is a cardinal sine function which gets broader as the mask gets smaller. The left-hand side of Fig. 6.52 shows the evolution of the wave amplitude in successive planes, and in particular the different components of the amplitude in the pupil plane C: the direct wave (Fig. 6.52e), the wave diffracted by the mask (Fig. 6.52f), and their difference before (Fig. 6.52g) and after (Fig. 6.52h) inserting the mask. We see that the maximum intensity (modulus squared of the amplitude) is concentrated at the radius of the image of the pupil in the form of a bright ring. This is precisely what caught Lyot’s attention. We thus understand why the pupil diaphragm must be slightly smaller than the geometric image of the pupil if the diffracted light is to be effectively blocked.

The Roddier & Roddier Coronagraph38

Franc¸ois and Claude Roddier had the idea of replacing the amplitude focal mask by a phase mask, i.e., a transparent mask producing a path length difference as a function of its thickness. If this difference is equal to $\lambda / 2$ , it then introduces a phase shift of $\pi$ , in other words a change in the sign of the amplitude.

The relation established for the Lyot mask becomes

$$
\nu ( x , y ) = \tilde { u } ( x , y ) \left[ 1 - 2 M ( x , y ) \right] ,
$$

and in the conjugate pupil plane,

$$
w = \mathrm { F T } \left( \nu \right) = \left( u - 2 u \star \tilde { M } \right) \times D \ .
$$

If the size of the phase mask is chosen judiciously (radius $0 . 5 3 \lambda / D$ ), the level of extinction will be high and the amplitude of $w$ can be further reduced with respect to the Lyot solution. The increased efficiency of this solution can be interpreted by considering that the incident wave has been divided into two parts, with approximately equal integrated amplitudes, one undergoing a phase shift of $\pi$ , whereupon the destructive interference of these two waves produces the desired extinction effect.

![](images/c56d6ab2842afbd1dbb90dae3eb68001dbdd10a650e8df9502f0acde6dbf657d.jpg)  
Fig. 6.53 Four-quadrant phase mask coronagraph. In the focal plane, the image of the star to be extinguished is placed at the centre of symmetry of the mask. (a) The phase mask (schematic). (b) Function to be integrated to obtain the amplitude in the pupil. It can be shown that the integral is zero, however far off centre the disk may be

Rouan Coronagraph39

This solution is also based on the phase mask idea, producing destructive interference once again. The mask, which affects the whole focal field, is formed by juxtaposing four quadrants, two of which, in diagonally opposite positions, produce a phase shift of $\pi$ (Fig. 6.53a). It can then be shown that a source perfectly centered at the meeting point of the four quadrants will be totally extinguished, i.e., $w = 0$ Duniformly in the pupil, the diffracted light being rejected entirely outside the pupil.

The full pupil condition, in particular without central obstruction of the telescope, must nevertheless be satisfied for this to work. This is one of the desired cases where $w = 0$ . Indeed, the term $u \star \tilde { M }$ reduces here to the convolution product of the pupil Dfunction and $1 / x y$ , which is simply the integral of the function $1 / x y$ over a region corresponding to an off-centre disk, as shown in Fig. 6.53b. Exploiting the power of a point with respect to a circle, there is an elegant proof due to Jean Gay (2002) that this integral must be strictly zero, however far off centre the disk may be.

Several coronagraphs based on this idea have already been installed in telescopes: two devices operating at $2 . 2 ~ { \mu \mathrm { m } }$ on the NACO adaptive optics system of the VLT, and three others in the mid-infrared instrument (MIRI) camera, one of the four focal instruments of the James Webb Space Telescope (JWST) developed by NASA in collaboration with Europe. The latter instrument (expected launch in around 2014) is designed for direct detection of giant extrasolar planets in the $1 1 - 1 6 \mu \mathrm { m }$ range. The instrument known as spectropolarimetric high-contrast exoplanet research or SPHERE, expected to equip the VLT in 2012, is designed for an analogous purpose but at shorter wavelengths, and uses similar components.

Notch Filter Mask

This solution also uses a focal mask, but here it is the transmission that is modulated by what is known as a notch filter mask, whose radial transmission varies as $1 - \sin r / r$ . It can then be shown that $\tilde { M }$ is a box function and that its convolution with $u$ is flat over a large region which covers part of the pupil. The quantity $( u - u \star \tilde { M } )$ is thus zero over the main part of the pupil, as required, except for a ring-shaped region on which the pupil diaphragm is applied. Note that this mask can also be designed to modulate in just one dimension.

There are several limitations to the use of focal masks:

• To arrange for $u$ and $u \star \tilde { M }$ to be as similar as possible (the condition for cancelling w), $\tilde { M }$ must be as close as possible to a $\boldsymbol { \delta }$ function, i.e., it must have a very narrow support. This in turn means that the focal mask, its Fourier conjugate, must have a very broad support, which is barely compatible with the fact that the aim is to form an image of the field as close as possible to the central source. The four-quadrant phase mask is an exception here, and for this reason is rather large, since it extends over the whole field, while conserving good ‘transmission’ close to the axis. • The formalism used here assumes that the wavefront is perfectly plane, which is never the case in practice due to optical defects and atmospheric perturbations. In particular, it is absolutely essential to use adaptive optics for ground-based observation, because the PSF of the bright source must be quasi-coherent and must be maintained very accurately on the axis of the focal mask. This is therefore the main limitation of coronagraphs in use at the time of writing (2007), including those soon to be used in space. Ways of reducing the consequences of this limitation will be discussed below.

In phase mask systems, the phase shift introduced by the mask is not independent of the wavelength, since it is generally achieved using a slab of thickness $e$ and refractive index $n$ $( \phi = 2 \pi e n / \lambda$ ). This means that it will only be effective in a narrow spectral band centered on Dthe wavelength $\lambda = 2 e n$ .

Various solutions have been suggested to make the $\pi$ phase shift achromatic in the latter case. Undoubtedly one of the most promising, proposed by Mawet and coworkers, is to use a zero order grating (ZOG). Such components are obtained using nanotechniques, etching grooves of width smaller than the wavelength (so-called sub-lambda grooves) on a substrate. It can be shown that these gratings have birefringent properties with a different refractive index between the ordinary and extraordinary axes which can be made linear in . This amounts to having an achromatic phase shift between two perpendicular polarisations. The idea then is to etch grooves in one direction on two opposite quadrants, and perpendicular grooves on the other two quadrants. Whatever the polarisation state of the incident light, the desired $\pi$ phase shift is indeed introduced.

Following the same line of thinking, a very elegant solution is the achromatic groove phase mask (AGPM). This picks up the ZOG idea except that the sub-lambda grooves have circular symmetry. The effect of the differential path length difference between two perpendicular polarisations is indeed obtained, as with the four-quadrant ZOG, but the effect of the boundary between the quadrants disappears, which is a non-negligible advantage. Figure 6.54 illustrates the solutions based on the ZOG.

# Apodisation

In this family of techniques, the idea is to play rather on the function $u$ in the equation $w = \mathrm { F T } \left( \nu \right) = \left( u - \epsilon u \star \tilde { M } \right)$ . There are two aims:

• To ensure that the feet of the PSF of the bright source do not extend too far, or at least decrease more abruptly than in a classical Airy disk (in which the intensity decreases on average as $\theta ^ { - 3 }$ ). To round off the profile $u$ of the pupil so that it matches as well as possible the profile of the diffracted wave, i.e., the convolution product $u \star \tilde { M }$ . Indeed, just as we have seen that a narrow focal mask implies $\tilde { M }$ with wide support, so the convolution product is described by a function closer to a bell shape than a top hat.

Non-Circular Pupil

A first solution is to consider particular shapes of aperture so that, in one or more selected directions, the profile of the PSF decreases much faster than the Airy disk. This is the case with a square pupil: indeed, in the directions corresponding to the diagonals, the brightness profile of the PSF varies as $\theta ^ { 4 }$ , whereas it only decreases as $\theta ^ { 2 }$ in any other direction. Another solution, put forward by Kasdine and Spergel, is to consider apertures of Gaussian shape. Figure 6.55 shows such a pupil along with the corresponding PSF and the brightness profile in the optimal direction. Other combinations in which several different Gaussian profiles are juxtaposed are also possible.

![](images/41c41d43c43a3263d342bcc6c08c84ff4e0c9801c9fa32f9ca235849e4676e57.jpg)  
Fig. 6.54 ZOG version of the four-quadrant phase mask coronagraph. The quadrants are etched with grooves with spacing $p < \lambda$ using nanotechniques. The shape birefringence introduced in this way produces the desired $\pi$ phase shift between quadrants, as illustrated by the two configurations of the electric field components. Source: D. Mawet

![](images/ab52ad7c82da705e07c47e2298c87f45b174764ebf7a04d2d4728285efa27570.jpg)  
Fig. 6.55 The Kasdine–Spergel coronagraph. Left: the pupil shape; center: the point spread function; right: a cut along the $\mathbf { X }$ -direction revealing the very low level of residual light on each side of the main core

For all these solutions, the high contrast part of the field, i.e., the part in which faint structures might be sought, is rather limited. In particular, it must be possible to rotate the telescope about its optical axis in order to explore the whole environment of the bright source.

# Variable Transmission Pupil Mask

If $M$ is an indicator function (taking values 1 or 0), Aime and Soummer have shown that the equation $w = ( u - \epsilon u \star \tilde { M } ) \times D = 0$ can be construed as an eigenvalue D problem with solution the pair $[ u = \phi , \varLambda ]$ , where the eigenvalue, if it exists, is $\varLambda = 1 / \epsilon$ D. Such solutions exist for the Roddier–Roddier coronagraph $( \epsilon = 2$ ) for Da circular or rectangular aperture. The function $\varPhi$ Dis then a particular mathematical function, viz., a linear or circular prolate spheroidal function, respectively. In the case of a Lyot coronagraph $( \epsilon = 1 )$ ), there is no exact solution, but approximate Dsolutions can be defined using these same functions, solutions which become more efficient as the mask gets larger. What is remarkable in this case is the fact that the amplitude of the wave diffracted by the mask is proportional to the amplitude in the entrance pupil. The process can thus be reiterated by introducing a series of focal mask/pupil diaphragm pairs, each introducing the same reduction factor for the stellar light. The extinction then increases exponentially with the number of stages. This idea is under investigation for the SPHERE instrument to equip the VLT, as mentioned earlier.

The difficulties in making masks where the transmission varies according to a precise law may be overcome by using high-energy beam sensitive (HEBS) materials. These can become opaque in a stable manner under the effects of high energy electron bombardment. A narrow electron beam can be computer controlled to scan a HEBS film deposited on a glass slab in order to obtain a mask with very precise transmission profile.

In this same family of apodising pupil masks, a very elegant solution is phase induced amplitude apodization (PIAA), suggested by Olivier Guyon. To get round the fact that the resolution and equivalent transmission are degraded in conventional amplitude modulation (since a pupil mask necessarily absorbs light), Guyon suggested playing on the shape of the optical surfaces to concentrate or dilute the light rays in the exit pupil of an afocal system, as shown in Fig. 6.56. The apodisation effect on the PSF is the same as for a pupil mask but without the drawbacks. The collecting area of the primary mirror of the telescope is fully exploited.

Optical surfaces capable of producing the desired brightness distributions are highly aspherical, and since the optical arrangement no longer respects the Gauss conditions, the useful field becomes very small. However, this is not a serious problem, since the structures sought, e.g., exoplanets, are always very close in angular terms to the optical axis of the bright source. Moreover, by using an identical but reversed optical system after passing through a coronagraphic mask — a simple Lyot mask is perfectly suitable, since the resulting PSF has bounded support — the isoplanicity properties of the field can be reestablished. The main difficulty with this solution is in producing specific aspherical surfaces, whose radius of curvature must vary by several orders of magnitude along a diameter.

![](images/2ababaeba0200a1ba275bdfd29e9481bf00e9ef5c3c66f2feeecf1cbc3dc31e7.jpg)  
Fig. 6.56 The Guyon PIAA coronagraph. The pupil is reshaped thanks to aspheric optics. Source: O. Guyon

# Interferometric Solutions

Although inspired by Lyot’s idea, devices using phase masks already exploit the principle of destructive interference of the wave coming from the bright source. In this last part, we discuss methods aiming explicitly to produce such destructive interference, but without resorting to the focal mask/pupil diaphragm scheme originally proposed by Lyot.

Achromatic Interferential Coronagraph (AIC)

It was in fact just such a method, proposed by the French astronomers Jean Gay and Yves Rabbia, that triggered new interest in coronagraphy at the end of the 1990s. Achromatic interferential coronagraphy (AIC) exploits a Michelson interferometer to make the wave from the bright source interfere destructively with itself. The novelty here is to reverse the wave in one arm of the interferometer by passing it through the focal point of an optical system. Only the wave strictly on the axis will remain parallel to its counterpart in the other arm and hence be able to interfere uniformly and destructively with the latter, while a wave at a small angle of incidence $\theta$ , e.g., coming from a nearby companion, will meet its counterpart in the recombination output at an angle $2 \theta$ , preventing any effective interference. Moreover, recalling that the effect of passing through a focal point is to introduce a phase shift of $\pi$ , i.e., a change of sign of the amplitude, the two arms of the interferometer can be of strictly equal length, which simplifies the design, but above all allows destructive interference whatever the wavelength, a significant advantage which justifies calling the device achromatic.40

The visible nulling coronagraph (Lyon, 2005) is a further variation on the theme of destructive interference. This idea, which also exploits a Michelson interferometer, is analogous to the AIC in many ways. The main difference is that one of the two beams is not reversed but simply translated a distance $B$ (brought to the level of the entrance pupil, i.e., the diameter of the telescope): the pupils overlap significantly in a cat’s eye pattern. The phase shift $\pi$ which ensures destructive interference on one of the two interferometer outputs is introduced by adjusting the optical path difference in one of the arms. The effect of translating one pupil relative to the other is then analogous to the effect obtained in a nulling interferometer comprising two telescopes whose baseline would simply be $B$ . The field of view of the telescope is modulated by a series of fringes, alternately dark (extinguished) and bright (transmissive), placing the bright source that needs to be attenuated on a dark fringe. The further advantage with this setup is that the operation can be repeated by injecting the dark output into a similar interferometer, but applying the separation/translation operation in a perpendicular direction. The extinction profile then goes as $\theta ^ { 4 }$ , which attenuates the star more efficiently. Figure 6.57 shows how this works. Note, however, that this kind of optical system is difficult to implement in practice.

To end this discussion of single-pupil interferometric solutions, let us describe two methods which complement the other instruments invented to extinguish the bright source. The main limitation that must be faced by all these solutions when they are eventually set up and required to achieve the extreme levels of performance involved in detecting extrasolar planets, such as those mentioned in the introduction, will be the extreme difficulty in distinguishing a true planet from a speckle due to residual, even very small, defects in the optics. Indeed, even defects of the order of ten picometres on the wavefront of a very large telescope could very easily simulate an Earth-sized planet!

# Self-Coherent Camera

This instrument, proposed by Pierre Baudoz, exploits the fact that stellar and planetary photons are not coherent. If the final coronagraphic image is made to interfere with a beam of pure stellar light extracted upstream, the residual speckles will be modulated by a fringe system, while the spot formed by any planet will not be. A careful analysis of these fringes by Fourier transform methods would then provide a way, at least in principle, of removing any ambiguity.

![](images/13c8cadb5c6c2fbcd7495784ed3db806e656614aebdc48980d246e5ce345f5fb.jpg)  
Fig. 6.57 Visible nulling coronagraph due to Lyon and Shao based on a Michelson interferometer with a shear of one beam with respect to the other. ${ \boldsymbol { \mathrm { S } } } =$ beam splitter, $\mathbf { M } =$ dihedral mirror

Speckle Cancellation

Another way of reducing residual speckles, proposed by Traub and Borde (2005), ´ would be to measure them, and then cancel them using a deformable mirror. To begin with, a carefully chosen series of very small amplitude wave forms is applied to this mirror, of the same dimensions as residual defects in the wavefront after passing through whatever form of coronagraph has been used. Then, by analysing the resulting series of images and using a little linear algebra, it is possible to reconstruct the right form of wave to apply to the mirror in order to correct these residual defects. After a few iterations, the process should converge.

This solution is based on a remarkable property of the electric field in the pupil after passing through a coronagraph: to a first approximation, it is directly proportional to the perturbed phase $\varPhi$ , because in the truncated expansion of the input amplitude, viz., $\exp \mathrm { i } \phi \approx 1 + \mathrm { i } \phi$ , only the first term vanishes as a result of the action of the coronagraph. Put another way, a perfect coronagraph can only extinguish the coherent part of the image of the bright source.

# Conclusion

Which of these methods will meet the challenge of forming an image of a planet orbiting around a main sequence star? At the time of writing (2007), no one would be able to reply to this question. The development of such instruments is likely to remain highly active in the coming years. Looking beyond the design of theoretically excellent optical systems, the problem of implementing them in the real world has become a major preoccupation. A clear consensus has already been reached on one key point: only a complete system comprising telescope $^ +$ extreme adaptive optics $^ +$ Cfocal instrument, dedicated at the outset to this aim, will ever Cobtain the image of details of a sister planet to our own.

# 6.6.2 Nulling Interferometry

Here we discuss a variant of coronagraphy. The idea is still to use interference properties to reduce the extreme intensity contrast between two very close objects, usually a star and a planet, in order to study the fainter of the two. However, in this case, the solution is interferometric recombination of the beams from several telescopes. The term nulling interferometer could then be replaced by coronagraphic interferometer, as we shall in Sect 9.6.

# Basic Idea

The method of nulling interferometry suitably complements conventional coronagraphy. Indeed, the latter is a technique that is essentially applicable to the visible and near infrared regions. This is because it is only at these wavelengths that the angular resolution of a large telescope is of the same order of magnitude as the angle subtended by a typical planetary orbit of 1 AU at a distance of $1 0 \mathrm { p c }$ . While life does provide spectral signatures in this region of the visible — basically, through oxygen and the chlorophyll function — the star–planet intensity contrast remains extremely high, typically of the order of $1 0 ^ { 1 0 }$ .

On the other hand, in the mid-infrared region, this contrast is much more favourable, being of the order of $1 0 ^ { 6 . 5 }$ . Furthermore, a set of less ambiguous biological signatures than those observable in the visible has been identified. These are provided by ozone at $9 . 7 \mu \mathrm { m }$ , carbon dioxide, and water vapour (see Fig. 6.58). It has been shown that the simultaneous presence of these three signatures could constitute a very strong indication that life is present, at least in a form similar to life on Earth. The quest to identify this trio has been made the cornerstone of ESA’s Darwin programme (see above), while NASA’s TPF-I programme will pursue a similar aim, but today, both projects have been shelved.

![](images/68b3bdc4e6ce157b43301c9ea41700417351f9400cac8bea34ddcee7687ef563.jpg)  
Fig. 6.58 The mid-infrared spectrum of the Earth shows three spectral signals due to ozone, carbon dioxide, and water vapour which, if observed together, would constitute a biosignature that is in principle unambiguous. Upper: Observed and modelled infrared spectra of the Earth viewed from a distance. Lower: Laboratory spectra of various atmospheric components. See also Fig. 9.20

An angular resolution of 0.1 arcsec at $1 5 \mathrm { \ \mu \mathrm { m } }$ implies either a monolithic telescope of diameter $3 0 \mathrm { ~ m ~ }$ , whose feasibility in space is far from obvious, or an interferometer with a baseline longer than $3 0 ~ \mathrm { m }$ . The second option has been favoured for the Darwin project proposed back in 1996 by Alain Leger and cowork- ´ ers, based on the assumption that spacecraft could fly in stable and reconfigurable formations without excessive difficulty. However, the problem of dazzle by light from the star remains just as critical as ever with an interferometer, whence it is still essential to apply some blocking procedure analogous to coronagraphy.

![](images/3fdc68ce5084fd5bcc1b621fe70980552770e70ea14d50d667f0d42ea20689c7.jpg)  
Fig. 6.59 Principle of nulling interferometry, as proposed by Bracewell. Values for the baseline $D$ , the wavelength $\lambda$ , and the separation $\theta$ are given as examples. Left: Schematic of the interferometer, with a $\pi$ phase shift introduced in one arm. Right: The on-axis star is extinguished by the dark fringe, while the off-axis planet remains observable. Source: M. Ollivier

# The Bracewell Interferometer

The solution to this difficult problem was put forward by Ronald Bracewell41 as early as 1978, in a seminal paper, where he describes the principle of nulling interferometry. The idea, illustrated in Fig. 6.59, is to produce interference fringes, projected on the sky, by interferometrically recombining the beams from two telescopes a distance $B$ apart. If we can arrange for the star to lie on a dark fringe and for the fringe spacing to correspond to the distance between the star and the supposed planet, then the contrast is optimal.

However, it would be of little use to work at a single wavelength, because the planet is extremely faint and the spectral information required lies in a vast wavelength range, from 5 to $1 7 ~ { \mu \mathrm { m } }$ for the Darwin instrument. In a conventional interferometer, only the bright central fringe, the one corresponding to zero optical path difference, would be common to all wavelengths, while the fringe systems of different wavelengths would overlap and interfere mutually for every other position in the sky. The powerful idea put forward by Ronald Bracewell was to insert a phase shift of $\pi$ that did not depend on the wavelength, i.e., an achromatic phase shift, in one arm of the interferometer. This produces a dark fringe common to all the fringe systems. If this is placed on the star, efficient extinction becomes possible, without being limited to any spectral band.

The measured signal is the sum of the flux from the planet(s), light residues from the star, and local zodiacal light in the observed planetary system. The latter is generally called the exozodi. It corresponds to scattering of radiation from the star by a disk of micron-sized dusts left over from the protoplanetary disk, and constitutes a powerful source, much brighter than the planets themselves.

To distinguish the fraction intrinsic to the planet, its signal must be modulated. Bracewell suggested rotating the interferometer about the line of sight. The planet then follows a trajectory on the fringe system projected onto the sky, so that it is sometimes visible, sometimes extinguished, in such a way that only the signal modulated at the rotation frequency and agreeing with the expected pattern reflects the contribution from the planet.

# Difficulties

Several difficulties arose when more detailed studies of Bracewell’s ideas were carried out, with a view to detecting exoplanets. It will be instructive to give a brief analysis of these difficulties.

Non-Infinitesimal Angular Size of the Star

Even if it cannot strictly resolve the disk of the photosphere, the nulling interferometer allows photons from its most peripheral regions to escape. Indeed, the extinction zone is not a box shape, but a parabolic function of the angular distance, represented by a truncated expansion of $1 - \cos \theta$ . Naturally, very few of these photons get through, but the planet–star contrast is such that they are nevertheless predominant, and their statistical noise becomes a prohibitive limitation. Even more efficient extinction is thus required, going as $\theta ^ { n }$ with $n > 2$ . It can be shown that more than two telescopes are needed to achieve this.

Several configurations have been found, more or less empirically, to achieve this aim. One of the simplest is Angel’s cross. This produces a nulling function going as $\theta ^ { 4 }$ . It uses four telescopes placed at the ends of a cross, and introduces a $\pi$ phase shift in one of the two telescopes in each branch of the cross.

Other setups use telescopes of different sizes. Finally, one can also consider configurations where the phase shift is not $\pi$ but a fraction of $2 \pi$ , as in the three-telescope configuration studied a few years ago for the Darwin project. Recently, it has been shown that an arbitrary power $\theta ^ { n }$ can be obtained by combining $2 ^ { n }$ telescopes and associating a $\pi$ phase shift with half of them, chosen using a binary sequence known as the Prouhet–Thue–Morse sequence.´ 4 4 This sequence has the property that no finite subsequence is repeated more than twice consecutively in the sequence.

Achromatic $\pi$ Phase Shift

To obtain a signal of significant magnitude, a broad enough spectral interval must be analysed, and this requires a device that can obtain the $\pi$ phase shift as achromatically as possible throughout the interval. In 2007, several ideas are being explored and have been demonstrated in the laboratory:

![](images/7f89714195bbd2151b6da9b62f978cacee8d9310bd42b228afb0fe7efc87e201.jpg)  
Fig. 6.60 Various methods to produce an achromatic phase shift in a nulling interferometer. Left: using plates of different optical index (see text); center: using a periscopic setup to reverse the electric field direction; right: crossing the focus of a spherical mirror. Source: Y. Rabbia

• A first solution is to insert a set of transparent plates in each arm of the interferometer, choosing the materials and thicknesses so that the dependence of the path length difference on the wavelength is linear over the whole of the relevant spectral region. The phase difference is then achromatic. . A second solution exploits a property of Fresnel reflection on a mirror at $4 5 ^ { \circ }$ , viz., only the electric field component lying in the plane of the mirror undergoes a change of sign. The idea is to have the beam reflect on two symmetric pairs of periscopes (set of three successive mirrors at incidence $4 5 ^ { \circ }$ ), in such a way that the two components $s$ and $p$ of the electric field end up undergoing a reversal on one channel as compared with the other, as shown in the central part of Fig. 6.60. The third idea is to make use of the particular property that an electromagnetic wave undergoes a $\pi$ phase shift when it passes through a focal point. It is enough to arrange that the beam pass through the focal point of a spherical mirror in just one arm of the interferometer in order to obtain an achromatic $\pi$ phase shift.

Note that the last two solutions can only achieve phase shifts equal to $\pi$

Separating Planetary and Exozodi Light Signals

The symmetry of revolution of the exozodi light would only correspond to a planetary system viewed face on, which is a highly improbable configuration. Consequently, the elliptical brightness distribution of the exozodi generally produces a modulation by the fringe system, analogous to that of a planet. This is where the choice of interferometer configuration becomes crucial. Depending on the structure of the fringe system, or rather the maxima and minima of the transmission map, the signal modulations produced either by an isolated object like a planet or by a centrally symmetric structure like the exozodi will be more or less distinct. In 2007, investigations aim to identify the configurations that could best discriminate the two.

Temporal Stability of Stellar Flux Cancellation

This last difficulty is perhaps the most serious. Indeed, any deviation of the phase shift from $\pi$ , even very small, would produce very large relative fluctuations in leaks of stellar light, and these would largely dominate photon noise from the exozodiacal light, the latter fixing the fundamental detection limit. This question is very carefully considered in simulation experiments.

# Problems

6.1. Show that, for quasi-monochromatic radiation,

$$
| \gamma _ { 1 2 } ( \tau ) | = | \gamma _ { 1 2 } ( 0 ) | \quad \mathrm { i f } \quad \tau \ll \tau _ { \mathrm { c } } ,
$$

where $\tau _ { \mathrm { c } }$ is the correlation time. Set $V ( t ) = f ( t ) \exp ( 2 \pi \mathrm { i } \nu _ { 0 } t )$ , with $f ( t )$ slowly varying.

Answer. With the suggested notation,

$$
{ \cal T } _ { 1 2 } ( \tau ) = \langle V _ { 1 } ( t ) V _ { 2 } ^ { * } ( t + \tau ) \rangle = \langle f _ { 1 } ( t ) f _ { 2 } ^ { * } ( t + \tau ) \exp ( - 2 \pi \mathrm { i } \nu _ { 0 } \tau ) \rangle \ .
$$

The quasi-monochromatic approximation, $\tau \ll \tau _ { \mathrm { c } }$ , then implies $f _ { 2 } ( t + \tau ) \approx f _ { 2 } ( t )$ , whence

$$
\begin{array} { r } { T _ { 1 2 } ( \tau ) = T _ { 1 2 } ( 0 ) \exp ( - 2 \pi \mathrm { i } \nu _ { 0 } \tau ) \ . } \end{array}
$$

Taking the modulus and normalising, the result follows.

6.2. Consider an interference experiment with quasi-monochromatic light (Young’s slits) and express the visibility $\mathcal { V }$ of the fringes as a function of the fields $V _ { 1 } ( t )$ and $V _ { 2 } ( t )$ of the two sources. Show that

$$
| \gamma _ { 1 2 } ( \tau ) | = \mathcal { V } .
$$

Answer. At the point $Q$ observed and at time $t$ , the amplitude of the observed field is obtained from the superposition of the two sources

$$
V ( Q , t ) = V _ { 1 } ( t - \tau _ { 1 } ) + V _ { 2 } ( t - \tau _ { 2 } ) \ ,
$$

where $\tau _ { 1 }$ and $\tau _ { 2 }$ are the respective times taken by the light between the sources and the point $Q$ .

The observed intensity is $I ( \boldsymbol { Q } , t ) = \langle V ( \boldsymbol { Q } , t ) V ^ { * } ( \boldsymbol { Q } , t ) \rangle$ , which gives

$$
I ( \boldsymbol { \mathcal { Q } } , t ) = I _ { 1 } ( \boldsymbol { \mathcal { Q } } , t - \tau _ { 1 } ) + I _ { 2 } ( \boldsymbol { \mathcal { Q } } , t - \tau _ { 2 } ) + 2 \mathrm { R e } \langle V _ { 1 } ( t - \tau _ { 1 } ) V _ { 2 } ^ { * } ( t - \tau _ { 2 } ) \rangle ~ .
$$

The assumption that the light is quasi-monochromatic gives

$$
\tau _ { 1 } \ \mathrm { a n d } \ \tau _ { 2 } \ll \tau _ { \mathrm { c } } = 1 / \Delta \nu
$$

which allows simplification of the previous relation. Putting $\tau = \tau _ { 1 } - \tau _ { 2 }$

$$
I ( Q , t ) = \left[ I _ { 1 } ( Q , t ) + I _ { 2 } ( Q , t ) \right] + 2 \sqrt { I _ { 1 } ( Q , t ) I _ { 2 } ( Q , t ) } \mathrm { R e } \bigl ( \gamma _ { 1 2 } ( \tau ) \bigr ) .
$$

Finally, as $Q$ moves, the value of $\tau$ changes, so that the intensity exhibits fringes of visibility given by

$$
\frac { 2 \sqrt { I _ { 1 } ( \mathcal { Q } , t ) I _ { 2 } ( \mathcal { Q } , t ) } } { I _ { 1 } ( \mathcal { Q } , t ) + I _ { 2 } ( \mathcal { Q } , t ) } \left| \gamma _ { 1 2 } ( \tau ) \right| .
$$

In the simple case when $I _ { 1 } ( Q , t ) = I _ { 2 } ( Q , t )$ , this gives visibility $| \gamma _ { 1 2 } ( \tau ) |$ .

6.3. Check that the coherence degree of order $n$ of a quasi-monochromatic wave obeys

$$
| \gamma _ { n } ( \tau ) | = 1 .
$$

6.4. A source is in the form of a grid of brightness

$$
I ( \pmb \theta ) = I _ { 0 } \sin 2 \pi \frac { \theta _ { x } } a .
$$

(a) What is the spatial spectrum $\tilde { I } ( \boldsymbol w )$ of this grid?

(b) An astronomical source (a young star forming, or the nucleus of a galaxy) has profile

$$
I ( \theta ) = I _ { 0 } \exp \left( - \frac { \theta ^ { 2 } } { 2 a ^ { 2 } } \right) , \quad a = 0 . 1 \mathrm { a r c s e c } .
$$

What is its spatial spectrum?

(c) An optically thin circumstellar envelope around a star, is such that the brightness of the whole ensemble is given by

$$
I ( \theta ) = I _ { 0 } \exp \left( - \frac { \theta ^ { 2 } } { 2 a ^ { 2 } } \right) + I _ { 1 } \delta ( \theta - \theta _ { 0 } ) \ , \quad a = 0 . 1 \mathrm { a r c s e c } \ .
$$

The radius of the star is $1 0 ^ { 1 2 }$ cm and its distance $4 0 0 \ \mathrm { p c }$ $\mathrm { 1 p c } = 3 \times 1 0 ^ { 1 8 } \mathrm { c m } )$ The envelope extends out $1 0 ^ { 1 5 }$ D cm all round. What is its spatial spectrum?

(d) A double star is such that one component has twice the intensity of the other. What is its spatial spectrum?

In each of the four cases, analyse the filtering effect on the image produced by pupils of increasing size, for some fixed wavelength.

Answer. The spatial spectra are just the Fourier transforms of the intensities.

(a) For the grid,

$$
\tilde { I } ( w ) = { \frac { \mathrm { i } } { 2 } } I _ { 0 } { \frac { a } { 2 } } \left\{ \delta \left[ { \frac { a } { 2 } } \left( u - { \frac { 1 } { 2 } } \right) , \nu \right] - \delta \left[ { \frac { a } { 2 } } \left( u + { \frac { 1 } { 2 } } \right) , \nu \right] \right\} \ .
$$

(b) For the Gaussian source,

$$
\tilde { I } ( w ) = I _ { 0 } \sqrt { 2 \pi } a \exp \left( - 2 \pi ^ { 2 } a ^ { 2 } w ^ { 2 } \right) .
$$

(c) For the circumstellar envelope, using the result in (b) and linearity of the Fourier transform,

$$
\tilde { I } ( w ) = I _ { 0 } \sqrt { 2 \pi } a \exp \left( - 2 \pi ^ { 2 } a ^ { 2 } w ^ { 2 } \right) + I _ { 1 } \exp \left( - 2 \mathrm { i } \pi \theta _ { 0 } w \right) .
$$

(d) For the binary system,

$$
\begin{array} { r } { I ( \pmb \theta ) = 2 I _ { 1 } \delta ( \pmb \theta ) + I _ { 1 } \delta ( \pmb \theta - \pmb \theta _ { 0 } ) , } \end{array}
$$

which implies

$$
\tilde { I } ( w ) = I _ { 1 } \left[ 2 + \exp ( - 2 \mathrm { i } \pi \theta _ { 0 } w ) \right] .
$$

The modulus thus exhibits fringes.

The effect of the limited size of the pupil is to cut off spatial spectra at the spatial frequency $D / \lambda$ . In the image plane, the restored image is the convolution of the image source with the PSF, an Airy function which spreads as the pupil diminishes.

6.5. Consider an object $I ( \pmb \theta )$ whose spatial spectrum is circularly symmetric (e.g., a star or a solar granulation). Show that all the spatial information can be obtained by a simplified telescope whose pupil is limited to a slit:

$$
G ( r ) = \pi \left( \frac { x } { D } \right) \pi \left( \frac { y } { a } \right) , \quad D \gg a ,
$$

replacing a conventional telescope of diameter $D$ .

6.6. A telescope ${ \cal D } { = } 3 . 6 \mathrm { m }$ ) forms an image of a source at wavelength $\lambda { = } 0 . 5 \mu \mathrm { m }$ . Its focal ratio is $f / D = 1 0 0$ . What is the optimal sampling rate $x$ Dfor the image, if Dit is effectively limited by diffraction? The grain of the detecting photographic plate creates white detector noise up to a frequency corresponding to a grain size of $3  { \mu \mathrm { m } }$ .

Show that the choice of a finite sampling rate $x$ has the effect of increasing the noise spectral density in the frequency domain containing the useful information.

6.7. A star appears as a disk, assumed to have uniform surface brightness, at the wavelength $\lambda _ { 0 }$ :

$$
I ( \pmb \theta ) = I _ { 0 } \varPi \left( { \frac { \theta } { \theta _ { 0 } } } \right) \ .
$$

Calculate its spatial spectrum. Show that, if the image is formed by a pupil of diameter $D$ such that $\theta _ { 0 } = \alpha \lambda _ { 0 } / D$ , $( \alpha \ : < 1 )$ ), then the determination of $\tilde { I } ( w )$ on $( 0 , w _ { \mathrm { c } } )$ nevertheless gives $\theta _ { 0 }$ , provided that it is assumed a priori that the star is a uniformly bright disk (super-resolution).

Answer. The spatial spectrum of the star is

$$
\tilde { I } ( w ) = { \frac { I _ { 0 } } { \pi \theta _ { 0 } w } } J _ { 1 } ( \pi \theta _ { 0 } w ) \ .
$$

The central peak of the Bessel function $J _ { 1 }$ extends to greater spatial frequencies than those sampled by the mirror. Therefore, only a truncated sampling of this function is available, and moreover, it is affected by a certain degree of noise. This sampling can be used to determine the value of $\theta _ { 0 }$ , using least squares or cross-validation fitting methods, provided that the form of $\tilde { I } ( \boldsymbol w )$ is known a priori. In the object plane, this means that the size of the structure is smaller than the diffraction size.

6.8. Michelson Interferometer. Consider a pupil consisting of two circular apertures of diameter $d$ , with separation vector $\pmb { D }$ , where $d \gg D$ , and an object of spectrum $\tilde { I } ( \boldsymbol w )$ , observed at the zenith, at wavelength $\lambda$ .

(a) Write the transfer function $\tilde { T } ( \boldsymbol { w } )$ and approximate it in terms of Dirac distributions. (b) Express the visibility of the fringes as a function of $\tilde { I } ( \boldsymbol w )$ .

Answer. The transfer function is the autocorrelation of the pupil. We consider here the limiting case of two pointlike openings,

$$
G ( w ) = \delta ( { \bf 0 } ) + \delta \left( { \frac { \cal D } { \lambda } } \right) .
$$

Then, for any other shift than 0 and $\pm { \pm } \pm \lambda$ , the product $G ( w + r / \lambda ) G ^ { * } ( r / \lambda )$ is zero, whence the approximation is

$$
\tilde { T } ( w ) = \delta ( { \bf 0 } ) + { \frac { 1 } { 2 } } \delta \left( w - { \frac { \cal D } { \lambda } } \right) + { \frac { 1 } { 2 } } \delta \left( w + { \frac { \cal D } { \lambda } } \right) .
$$

The spatial spectrum of the object after this filtering is thus

$$
\hat { I } ( \mathbf { 0 } ) + 0 . 5 \hat { I } ( { \cal D } / \lambda ) + 0 . 5 \hat { I } ( - { \cal D } / \lambda ) ,
$$

so that, in the symmetric case, fringes of visibility $\hat { I } ( { \cal D } / \lambda ) / \hat { I } ( \mathbf { 0 } )$ are produced.

6.9. The intensity interferometer (Hanbury-Brown, ARAA 6, 13, 1968) is based on the following principle: two telescopes, separated by a distance $x$ , receive photons $\lambda = 0 . 5 \mu \mathrm { m } ,$ ) from the same source, on two photomultipliers delivering currents $I _ { 1 } ( t )$ and $I _ { 2 } ( t )$ .

(a) Show that the cross-correlation function of the two currents, formed in a correlator which introduces a delay $\tau$ , and given by

$$
C ( \tau ) = \langle I _ { 1 } ( t ) I _ { 2 } ( t + \tau ) \rangle ~ ,
$$

contains information about the spatial structure of the observed object. Use the complex degree of coherence of the radiation as an intermediate step.

(b) Before correlation, $I _ { 1 }$ and $I _ { 2 }$ are filtered by two low-pass electric filters, with transfer functions $H ( f ) ~ = ~ \varPi \left( f / 2 \Delta f \right)$ . If $\Delta f \sim 1 0 ^ { 6 } ~ \mathrm { H z }$ , what error is D tolerable along the cables bringing each signal to the correlator? Compare with the precision required in a Michelson interferometer, at the same wavelength, and with the spectral interval $\Delta \lambda = 1 \mathrm { n m }$ .

6.10. Consider a parabolic mirror forming an image on its axis of a point at infinity.

(a) The mirror deviates slightly from a true paraboloid by an error described by $\varepsilon ( r ) = \varepsilon _ { 0 } \cos ( 2 \pi x / a ) , a = D / n , \varepsilon _ { 0 } = \lambda / 5$ , where $n \gg 1$ . Show that, as D D D 	far as the image is concerned, this is as if the pupil function $G ( r )$ had been replaced by a new complex pupil function $G ^ { \prime } ( r )$ (a phase mask). Deduce the point source response (image of a point) of the imperfect mirror.

(b) Answer the same question if $\varepsilon ( r )$ is now a random function with constant power spectrum up to some characteristic frequency $s _ { 0 } = 1 / 1 0 \lambda$ .

D(c) Why is the criterion for mirror surface quality taken as $\sigma _ { \varepsilon } < \lambda / 2 0$ , where $\sigma _ { \varepsilon }$ is the standard deviation of the surface error?

(d) Why is the spatial spectrum of the random variable $\varepsilon ( r )$ important?

6.11. Calculate the coherence length for the electromagnetic signal transmitted by each antenna of a radio interferometer operating at $\lambda ~ = ~ 1 8 ~ \mathrm { c m }$ , and receiving a frequency bandwidth $\Delta \nu \ : = \ : 1 \ : \mathrm { M H z }$ D from the incident radiation. Is this length Daffected by the change in frequency brought about by means of a local oscillator on each antenna?

Answer. The autocorrelation of the field is the Fourier transform of its power spectrum. Hence, if this is truncated over a width $\Delta \nu$ , the corresponding coherence time is $\tau _ { \mathrm { c } } = \Delta \nu ^ { - 1 }$ . The coherence length is therefore $l _ { \mathrm { c } } = c \tau _ { \mathrm { c } } = c / \Delta \nu = 3 ~ \mathrm { m }$ . D D D DThis is not affected by any frequency change brought about by local oscillators.

6.12. Consider $N$ antennas, intended to be aligned in an aperture synthesis arrangement. The intervals between antennas are chosen to be multiples of some length $a$ . For each value of $N$ between 2 and 6, inclusive, find the distances which give the non-redundant pupil with the best coverage of spatial frequency, by combination of pairs of antennas. Bearing in mind the rotation of the Earth, should the configuration be arranged east–west or north–south?

6.13. An object is observed in the visible $\langle \lambda = 0 . 5 \mu \mathrm { m } \rangle$ , with spectral resolution $R = \lambda / \Delta \lambda$ increasing from 1 to $1 0 ^ { 5 }$ D. At ground level, the sky background produces Da continuous emission of 1 rayleigh $\textrm { \AA } ^ { - 1 }$ (Sect. 2.3). In a plot of telescope diameter $D$ , from 1 to $2 0 \mathrm { m }$ , against the magnitude $V$ of the object, trace, for different spectral resolutions $R$ , the loci of the points at which the noise from the sky background is equal to the signal noise. Take the field to be 1 arcsec, and the quantum efficiency multiplied by the total transmission to be 0.5. What conclusions can be drawn for the use of large telescopes in obtaining high spectral resolution?

6.14. An infrared telescope is used at the diffraction limit, at wavelength $\lambda \ =$ $1 0 0 ~ { \mu \mathrm { m } }$ , with spectral resolution $\lambda / \Delta \lambda ~ = ~ 1 0$ D. Calculate the power received Dat the focus, in the beam etendue corresponding to the diffraction limit, taking ´ $T _ { \mathrm { m i r r o r } } = 3 0 0 ~ \mathrm { K }$ , emissivity $\mathcal { E } ^ { \mathrm { ~ ~ } } = 0 . 1$ , and using the Rayleigh–Jeans approximation. D DCompare this with the sensitivity of a detector with noise equivalent power $\left( { \mathrm { N E P } } \right) =$ $1 0 ^ { - 1 \bar { 6 } }$ W $\mathrm { H } z ^ { - 1 / 2 }$ D(the definition of the NEP is given in Sect. 7.1). What can be concluded from this comparison?

Answer. The beam etendue is written´ $S \varOmega$ , where the solid angle observed satisfies $\begin{array} { l l l } { \Omega } & { = } & { ( \lambda / D ) ^ { 2 } } \end{array}$ at the diffraction limit, and this implies a beam etendue of´ $\pi \lambda ^ { 2 } / 4$ , regardless of the telescope diameter. Moreover, the flux of a blackbody at temperature $T$ is

$$
B _ { \nu } ( T ) = 2 k T / \lambda ^ { 2 } \qquad [ \mathrm { W } \mathrm { m } ^ { - 2 } \mathrm { s r } ^ { - 1 } \mathrm { H z } ^ { - 1 } ]
$$

in the Rayleigh–Jeans approximation.

In order to make the comparison with the sensitivity of the detector, calculate the received power per beam etendue, in ´ $\mathrm { V } \ \mathrm { H z } ^ { - 1 / 2 }$ , at the wavelength and resolution under consideration $\bar { \Delta } \nu = c \Delta \lambda / \lambda ^ { 2 }$ ):

$$
\frac { \varepsilon 2 k T } { \lambda ^ { 2 } } \frac { \pi \lambda ^ { 2 } } { 4 } \sqrt { \frac { c \Delta \lambda } { \lambda ^ { 2 } } } = \frac { \varepsilon \pi k T } { 2 } \sqrt { \frac { c } { R \lambda } } = 3 . 4 \times 1 0 ^ { - 1 6 } \mathrm { W H z ^ { - 1 / 2 } } \ .
$$

Therefore, with the given observational characteristics, detector sensitivity is not the limiting factor.

6.15. Invariance of the Complex Amplitude Correlation Function in Fresnel Diffraction. Let $\psi _ { z } ( \pmb { x } )$ be the complex amplitude of a wavefront at position $z .$ , with $\boldsymbol { x }$ the position variable in the wave plane. Show that the complex amplitude at the position 0 is given by the convolution

$$
\psi _ { 0 } ( \mathbf { x } ) = \psi _ { z } ( \mathbf { x } ) \star { \frac { 1 } { \mathrm { i } \lambda z } } \exp \left( \mathrm { i } \pi { \frac { x ^ { 2 } } { \lambda z } } \right) ~ .
$$

Answer. The method used in this chapter can also be applied here, ensuring the conservation of energy. Show that

$$
{ \cal B } _ { 0 } ( x ) = \langle \psi _ { 0 } ( \xi ) \psi _ { 0 } ^ { * } ( x + \xi ) \rangle = { \cal B } _ { z } ( x ) = \left. \psi _ { z } ( \xi ) \psi _ { z } ^ { * } ( x + \xi ) \right. .
$$

The convolution is converted into a multiplication by Fourier transform.

6.16. The Fried Parameter. Assuming the expression $I _ { \mathrm { A } } ( \pmb \theta )$ , given in this chapter, for the Airy image of a circular pupil, calculate the exact value of the Fried parameter $r _ { 0 } ( \lambda )$ , by carrying out the integration

$$
\int B _ { \mathrm { 0 } } ( \boldsymbol { w } ) \mathrm { d } \boldsymbol { w } = \int \tilde { T } _ { \mathrm { A } } ( \boldsymbol { w } ) \mathrm { d } \boldsymbol { w } , \qquad \tilde { T } _ { \mathrm { A } } ( \boldsymbol { w } ) = \mathrm { F T } \left[ I _ { \mathrm { A } } ( \pmb { \theta } ) \right] ,
$$

and with $B _ { 0 } ( w )$ equal to the long-exposure MTF. [The resulting $r _ { 0 } ( \lambda )$ is given in the text.]

6.17. The star T Tauri is observed as two sources in the near infrared. One of these sources also emits in the visible, and the other at radiofrequencies. The latter is separated by a distance 0.9 arcsec along the north–south axis, and the intensity ratio is $\alpha$ .

Show that a knowledge of $| \tilde { I } ( w ) |$ from speckle interferometry is not enough in j jitself to show which source is the more northerly. (Dyck H.M. et al., Ap. J. 255, L103, 1982.)
