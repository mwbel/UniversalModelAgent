![](images/18150b1995e22f0f802db9d3fea32780d26b1dad5719bff114c89880399a2620.jpg)  
Fig. A.3 (a) Sampling of a function $f ( x )$ by a Dirac comb. (b) Replication of a function $f ( x )$ by convolution with a Dirac comb

![](images/e175b40c5167026430381fa87aa8c0d1e27e10e7950915ecfc9c4b47100b2859.jpg)  
Fig. A.4 Fourier transforms of trigonometric functions (dashed arrows indicate imaginary quantities)

This distribution plays an important role in the study of signal sampling, for example, when digitising, but also in the study of periodic structures such as interferometer antennas, or the lines of diffraction gratings.

# Trigonometric Functions

As they are not square integrable, trigonometric functions do not have FTs in function space. The Fourier transforms nevertheless exist in the form of distributions (Fig. A.4).

![](images/9ce3f0d0f33826458fea249861069252c840415bade3cc33f1f2c5a6a39bf7d4.jpg)  
Fig. A.5 Fourier transform of the two-dimensional axisymmetric box function

$$
\begin{array} { r c l } { { } } & { { } } & { { \cos \pi x \Rightarrow \displaystyle \frac { 1 } { 2 } \left[ \delta \left( s + \displaystyle \frac { 1 } { 2 } \right) + \delta \left( s - \displaystyle \frac { 1 } { 2 } \right) \right] \quad \mathrm { s y m m e t r i c } \ , } } \\ { { } } & { { } } & { { \sin \pi x \equiv \displaystyle \frac { \mathrm { i } } { 2 } \left[ \delta \left( s + \displaystyle \frac { 1 } { 2 } \right) - \delta \left( s - \displaystyle \frac { 1 } { 2 } \right) \right] \quad \mathrm { a n t i s y m m e t r i c } \ . } } \end{array}
$$

# A.1.4 Important Special Cases in Two Dimensions

# Box Function in Two Dimensions

This function is defined (Fig. A.5) as a constant inside the unit circle and zero outside, with $r ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ :

$$
\pi \left( { \frac { r } { 2 } } \right) = { \left\{ \begin{array} { l l } { 1 r < 1 } \\ { 0 r \geq 1 . } \end{array} \right. }
$$

The FT of this function can be written, with $w ^ { 2 } = u ^ { 2 } + \nu ^ { 2 }$ ,

$$
\pi ( { \frac { r } { 2 } } )  { \frac { J _ { 1 } ( 2 \pi w ) } { w } } ,
$$

where $J _ { 1 } ( x )$ is the Bessel function of order 1. The similarity relation implies

$$
\varPi \left( \frac { r } { 2 a } \right) \varepsilon \equiv a \frac { J _ { 1 } ( 2 \pi a w ) } { w } \ : , \quad a > 0 \ : .
$$

# Dirac Distribution in Two Dimensions

This distribution is defined by

$$
\delta ( x , y ) = \delta ( r ) = \iint _ { \mathrm { p l a n e } } \mathrm { e } ^ { 2 \mathrm { i } \pi r \cdot w } \mathrm { d } w \ ,
$$

and its FT takes the value 1 on the whole plane ${ \pmb w } \in \mathbb { R } ^ { 2 }$ .

# Two-dimensional Sampling Function

This distribution is constructed by repetition of the two-dimensional Dirac function in the plane:

$$
\sqcup ( x , y ) = \sum _ { m = - \infty } ^ { + \infty } \sum _ { n = - \infty } ^ { + \infty } \delta ( x - m , y - n ) .
$$

It is identical to its own Fourier transform

$$
\sqcup ( x , y )  \sqcup ( u , \nu ) .
$$

# Pairs of Frequently Used Fourier Transforms

Figures A.6 and A.7 show graphically some frequently used Fourier pairs in one and two dimensions, respectively.

Note in particular the one-dimensional Gauss function

$$
\mathrm { e } ^ { - \pi x ^ { 2 } }  \mathrm { e } ^ { - \pi s ^ { 2 } } ,
$$

and in two dimensions

$$
\mathrm { e } ^ { - \pi r ^ { 2 } } \gtrless \mathrm { e } ^ { - \pi w ^ { 2 } } ,
$$

which are preserved under Fourier transformation. The similarity relation leads to

$$
\exp [ - \pi ( { \frac { x } { a } } ) ^ { 2 } ]  | a | \exp [ - \pi ( a s ) ^ { 2 } ] ~ .
$$

# A.1.5 Important Theorems

# Convolution

The convolution of two functions (or distributions) is defined by the integral

$$
h ( x ) = f ( x ) \star g ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( x - u ) \mathrm { d } u .
$$

The convolution can be considered as a linear transformation determined by $g ( x )$ and applied to $f ( x )$ . This transformation represents the behaviour of many physical systems which impose a linear operation on the input signal, represented by $f ( x )$ , and lead to the output signal $h ( x )$ (Fig. A.8).

![](images/71dde984faad43bba65e3fdd7f4100a6eb4999c6cfcded4195aa08396e1df919.jpg)  
Fig. A.6 Common Fourier pairs. From Bracewell R.N., The Fourier Transform and Its Applications, McGraw-Hill, New York, 1965. With the kind permission of the McGraw-Hill Book Co

![](images/dc81ff0244c547cc3670db2f359f8f4e31ce56d5aeec60aaa848ee9e124fc47c.jpg)  
Fig. A.7 Common Fourier pairs in two dimensions. From Bracewell R.N., The Fourier Transform and Its Applications, McGraw-Hill, New York, 1965. With the kind permission of the McGraw-Hill Book Co. Note that the FT of $\sin ( \pi y )$ takes purely imaginary values

![](images/dbc06b6618c276400c2ab282926d0e8ee6eadf371e56e9b54f187adc866e8b76.jpg)  
Fig. A.8 Convolution of two functions $f ( u )$ and $g ( u )$

The Fourier transform acts on convolutions in a remarkable way

$$
\begin{array} { c } { { f ( x )  \tilde { f } ( s ) , } } \\ { { } } \\ { { g ( x )  \tilde { g } ( s ) , } } \\ { { } } \\ { { h ( x ) = f ( x ) \star g ( x )  \tilde { f } ( s ) \tilde { g } ( s ) = \tilde { h } ( s ) . } } \end{array}
$$

The convolution of two functions (or distributions) is transformed into the pointwise product of their FTs. The convolution product is commutative, associative and distributive over addition. All results mentioned here extend to higher dimensions. For example,

$$
H ( \pmb { r } ) = F ( \pmb { r } ) \star G ( \pmb { r } ) = \iint F ( \pmb { \rho } ) G ( \pmb { r } - \pmb { \rho } ) \mathrm { d } \pmb { \rho } ,
$$

$$
\tilde { H } ( w ) = \tilde { F } ( w ) \tilde { G } ( w ) \ .
$$

# Correlation

The correlation product or cross- correlation of two real functions (or distributions) is defined by

$$
k ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( u + x ) \mathrm { d } u ,
$$

and its interpretation is straightforward, with the help of Fig. A.9. Note that it differs from the convolution only by a change of sign in the argument of the second function. There is no universally accepted notation for the correlation product. We can write

$$
k = C _ { f g } \quad \mathrm { o r } \quad k = f \otimes g .
$$

![](images/23a5f0c5a898990f82b2c6600defe1ebe53e64f02f0dc3ae7f90fc75d104c7e5.jpg)  
Fig. A.9 The value of the correlation function $k ( x ) = f ( x ) \otimes g ( x )$ , calculated for a particular value of $x$ , is equal to the area shaded

If $f$ and $g$ are complex, the correlation product is defined by

$$
f \otimes g = \int _ { - \infty } ^ { + \infty } f ^ { * } ( u ) g ( u + x ) \mathrm { d } u ,
$$

where the asterisk denotes complex conjugation.

The autocorrelation of a function (or distribution) is given by

$$
k ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) f ( u + x ) \mathrm { d } u .
$$

# Parseval’s (Rayleigh’s) Theorem

This theorem says that a function and its FT have the same norm

$$
\int | f ( x ) | ^ { 2 } \mathrm { d } x = \int \left| \tilde { f } ( s ) \right| ^ { 2 } \mathrm { d } s = \int f f ^ { * } \mathrm { d } x \int \tilde { f } \tilde { f } ^ { * } \mathrm { d } s .
$$

Similarly, for two functions (or distributions),

$$
\int f g ^ { * } \mathrm { d } x = \int \tilde { f } \tilde { g } ^ { * } \mathrm { d } s .
$$

# Spectral Density

The spectral density, or power spectral density of the function $f ( x )$ is the quantity

$$
S _ { f } ( s ) = \left| \tilde { f } ( s ) \right| ^ { 2 } ,
$$

and $\tilde { f } ( s )$ is generally called the spectrum of $f ( x )$ . These terms are sometimes confused. In optics or spectroscopy, what is commonly called the spectrum is in fact a spectral density (see Chap. 5). The spectral density is also very commonly called the power spectrum.

Finally, we call the quantity

$$
\Big | \tilde { f } ( s ) \Big | = \Big \{ \Big [ \mathrm { R e } \tilde { f } ( s ) \Big ] ^ { 2 } + \Big [ \mathrm { I m } \tilde { f } ( s ) \Big ] ^ { 2 } \Big \} ^ { 1 / 2 }
$$

the amplitude spectrum, and the quantity

$$
\arg \tilde { f } ( s ) = \arctan \left( \frac { \mathrm { I m } \tilde { f } ( s ) } { \mathrm { R e } \tilde { f } ( s ) } \right)
$$

the phase spectrum. We collect these definitions together for convenience:

$$
\begin{array} { r l } & { \tilde { f } ( s ) \mathrm { s p e c t r u m ~ , } } \\ & { \left| { \tilde { f } } ( s ) \right| \mathrm { a m p l i t u d e s p e c t r u m ~ , } } \\ & { \arg { \tilde { f } } ( s ) \mathrm { p h a s e s p e c t r u m ~ , } } \\ & { \left| { \tilde { f } } ( s ) \right| ^ { 2 } \mathrm { s p e c t r a l d e n s i t y , ~ p o w e r ~ s p e c t r u m ~ . } } \end{array}
$$

# Autocorrelation (Wiener–Khinchine) Theorem

The Fourier transform of the autocorrelation of $f ( x )$ is the power spectrum of $f ( x )$

$$
\begin{array} { c c c } { { f ( x ) } } & { { } } & { { f ( x ) \otimes f ( x ) \nonumber } } \\ { { \downarrow \uparrow } } & { { } } & { { \downarrow \uparrow } } \\ { { \tilde { f } ( s ) } } & { { } } & { { \left| \tilde { f } ( s ) \right| ^ { 2 } } } \end{array}
$$

The power spectrum $| \tilde { f } ( s ) | ^ { 2 }$ is a real positive quantity. The phase information in the complex function $f ( x )$ j, which is contained in the real and imaginary parts of $\tilde { f } ( s )$ , is lost in the operation of autocorrelation.

# Cross-Power Spectrum and Cross-Correlation

If the functions (or distributions) $f ( x )$ and $g ( x )$ have FTs $\tilde { f } ( s )$ and $\tilde { g } ( s )$ , respec-Qtively, the cross-power spectrum or, better, the cross-spectral density, is defined by

$$
S _ { f g } ( s ) = \tilde { f } ( s ) \tilde { g } ^ { \ast } ( s ) ,
$$

so that $S _ { f g } ( s ) = S _ { g f } ^ { * } ( s )$ ; and the cross-correlation of $f$ and $g$ was defined above. DThen we find the relation

$$
S _ { g f } ( s )  C _ { f g } ( x ) .
$$

# A.2 Physical Quantities and Fourier Transforms

The FT proves to be invaluable for the representation of physical quantities. It can be used to isolate, in a complicated signal, simple (sinusoidal) components which are easy to handle, represent and interpret. However, it should be borne in mind that no information whatever is lost or gained when we go to the Fourier transform space.

Physical quantities, whether represented by functions or by distributions, are restricted in certain ways, and this allows us to develop some of the above ideas.

# Support of $f ( x )$

The Fourier transform of $f ( x )$ is defined if $f ( x )$ is defined on a support $] - \infty , + \infty [$ . 1 C1A physical quantity is generally only known on a bounded support. For example, a signal $f ( t )$ which is a function of time is only known on a finite time interval $[ - T / 2 , T / 2 ]$ . It is clearly possible to extend $f ( t )$ outside this interval by setting

$$
f ( t ) = 0 \quad \mathrm { f o r } \quad t \in ] - \infty , - \frac { T } { 2 } \bigg [ \quad \mathrm { o r } \quad ] \frac { T } { 2 } , + \infty [ \ .
$$

(This is an example of windowing.) Then we can calculate the FT and find the spectrum without ambiguity if $f ( t )$ is known at all points of the interval, or rather, if $f ( t )$ is known from an infinitely dense sampling. If on the other hand $f ( t )$ is unspecified outside the interval $[ - T / 2 , T / 2 ]$ , we can give no precise information about its spectrum without further assumptions (for example, concerning periodicity, or square-integrability, and the like). The method of windowing described here can be generalised. For example, the width $T$ of the window can be left undetermined, in the case of a function of time. This Fourier analysis on a variable and translatable window (adaptive Fourier analysis) is known as time–frequency analysis. A powerful tool is the Wigner–Ville representation.

# Negative Frequencies

The function $\tilde { f } ( s )$ is also defined on the support $] - \infty , + \infty [$ , and therefore refers to 1 C1negative frequencies. Is it possible to give some physical interpretation of negative frequencies? A physical quantity is real, and all we need to know its FT on the whole of $] - \infty , + \infty [$ are the values taken by the real and imaginary parts of the FT on $[ 0 , + \infty [$ C1, extending these symmetrically and antisymmetrically, respectively. C1The function ${ \ddot { f } } ( s )$ is then Hermitian (even real part, odd imaginary part). Its Fourier transform $f ( x )$ is real. Suppose we wish to carry out a numerical filtering on $f ( x )$ , which amounts to multiplying its FT by a certain function $\tilde { h } ( s )$ . We carry out the operation of pointwise multiplication of $\tilde { f } ( s )$ and $\tilde { h } ( s )$ on the whole support $] - \infty , + \infty [$ , before taking the inverse FT. This is shown in the following diagram.

$f ( x ) \mathop { \mathrm { r e a l } } _ { \downarrow }$ !FT $\begin{array} { l } { { \widetilde { f } ( s ) \ \mathrm { c a l c u l a t e d \ o n \ [ 0 , \infty ] } } } \\ { { \downarrow } } \\ { { \widetilde { f } ( s ) \quad \mathrm { c o m p l e t e d } } } \\ { { \mathrm { o n \ [ 0 , - \infty ] } } } \\ { { \downarrow } } \\ { { \widetilde { f } ( s ) \widetilde { h } ( s ) } } \end{array}$   
#Filtering operation   
.i:e:; convolution/   
$f ( x ) \star h ( x )$ FT

# Power of a Signal

Let $f ( x )$ be some signal, which may be complex; for example, a complex electric field whose amplitude and phase are functions of time.

We define the instantaneous power of the signal as

$$
p ( x ) = f ( x ) f ^ { * } ( x ) .
$$

When the variable $x$ is time and $f$ is a current or a voltage, this definition agrees with the normal usage.

The average power over an interval $X$ centred on $x _ { 0 }$ is defined as

$$
P ( x _ { 0 } , X ) = { \frac { 1 } { X } } \int _ { x _ { 0 } - X / 2 } ^ { x _ { 0 } + X / 2 } f ( x ) f ^ { * } ( x ) \mathrm { d } x \ .
$$

The integral of the instantaneous power is the energy associated with the signal

$$
\int _ { - \infty } ^ { + \infty } p ( x ) \mathrm { d } x ~ .
$$

If the signal is zero outside the interval $X$ , the integral generally converges without problems. If this is not the case, the signal may have an infinite energy, although its average power is finite. For example, the signal

$$
f ( x ) = \cos ( 2 \pi x )
$$

has average power

$$
\langle P \rangle = { \frac { 1 } { 2 } } ,
$$

although its energy is infinite.

The average power of a signal with support $[ - \infty , + \infty ]$ is defined by the limit

$$
\left. P \right. = \operatorname* { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( x ) f ^ { * } ( x ) \mathrm { d } x \ ,
$$

if it exists.

Although the terms energy and power only agree with their usual physical meanings for signals which are functions of time, they are universally used in the senses defined above.

# Power Spectrum of a Signal

Finite Energy Signal

If $f ( x )$ is a signal, we can calculate $\tilde { f } ( s )$ , and the quantity

$$
S _ { f } ( s ) = \tilde { f } ( s ) \tilde { f } ^ { \ast } ( s ) = \left| \tilde { f } ( s ) \right| ^ { 2 } ,
$$

already defined as the spectral density of $f ( x )$ is also called the power spectrum of $f ( x ) . S _ { f } ( s )$ has the dimensions of energy per frequency interval (spectral energy density) and not a power. The designation as the power spectrum or power spectral density (PSD) is nevertheless standard.

The total energy of the signal is clearly

$$
\int _ { - \infty } ^ { + \infty } S _ { f } ( s ) \mathrm { d } s ~ ,
$$

if the integral exists.

Infinite Energy Signal

In this case, $\tilde { f } ( s )$ cannot be calculated. Nevertheless, the autocorrelation function of $f ( x )$ may exist, given by

$$
C _ { f f } ( x ) = \operatorname* { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( u ) f ( x + u ) \mathrm { d } u ,
$$

and the Wiener–Khinchine theorem gives the spectral density of the signal $f ( x )$

$$
{ \cal S } _ { f } ( s ) = \mathrm { F T } \left[ C _ { f f } ( x ) \right] .
$$

Here $S _ { f } ( s )$ is an energy, or a power per frequency interval, which is consistent with previous definitions and makes it appropriate to use the term power spectral density. For example, if we consider a signal in the form of a voltage $\nu ( t )$ , the PSD is measured in $\mathrm { V } ^ { 2 } \mathrm { H z } ^ { - 1 }$ , and the amplitude spectrum in $\mathrm { V H z } ^ { - 1 / 2 }$ .

# Cross-Spectral Density and Cross-Correlation

The definitions and remarks above apply equally to the combination of two functions $f ( x )$ and $g ( x )$ .

For example, in the case of a signal of finite energy, the cross-spectral density is written

$$
S _ { f g } ( s ) = \tilde { f } ( s ) \tilde { g } ^ { \ast } ( s ) ,
$$

and the cross-correlation is

$$
C _ { f g } ( x ) = \int _ { - \infty } ^ { + \infty } f ( u ) g ( u + x ) \mathrm { d } u .
$$

If the energies are infinite, the cross-correlation is the limit

$$
C _ { f g } ( x ) = \operatorname * { l i m } _ { X \to \infty } \frac { 1 } { X } \int _ { - X / 2 } ^ { + X / 2 } f ( u ) g ( u + x ) \mathrm { d } u \ ,
$$

if it exists, and the cross-spectral density is defined by

$$
S _ { f g } ( s ) = \mathrm { F T } \left[ C _ { f g } ( x ) \right] .
$$

# A.3 Wavelets

By Fourier analysis, a signal can be decomposed into periodic functions of infinite support. This is a global transformation which is well-suited to signals with little or no evolution in time, the main example being stationary or quasi-stationary signals. Nevertheless, a physical signal is always defined on a bounded support, its emission being locally defined in time. The most important information is often contained in its non-stationarity (its beginning and end). The same comment could be made about an image bounded in space, or other types of signal, as well as the time signals referred to above. A partial solution is provided by the windowing technique mentioned earlier, which replaces a definition on an infinite support by a definition of the signal including a minimum number of significant coefficients. In a word, it compresses the signal in the most efficient way possible.

Two methods have been specifically developed to represent and analyse this type of signal. They are relevant here, because they are more and more frequently used in astronomy, to process data as varied as observed spectra, images, temporally variable emissions such as solar flares and periodic bursts of a pulsar, and many others. In these methods the time variable can, of course, be replaced by a space coordinate, or several (the two coordinates of an image), or indeed any other variable, such as the wavelength of a spectrum.

The time–frequency representation takes into account the time development of the frequency content of a signal. It gives the instantaneous frequency of the signal and the time dependence of this instantaneous frequency.

The wavelet transform, or time–scale representation, describes the development of a signal relative to some observation scale. Wavelets are oscillating functions, localised in time, unlike the sinusoidal functions of the Fourier transform. They all have the same shape, differing only in the instant of their appearance and in their duration. Wavelets of short duration and small amplitude thus represent very localised components of the signal, which would be missed upon a larger scale examination.

These two methods are particularly useful for classification and morphological analysis, which are all-important in astronomy. A signal (for example, the image of a type of galaxy) will thus have a unique signature on the wavelet transform of the image of a cluster. The relevant information is concentrated, in such a way that, in the Fourier transform, a particular frequency, drowned out by the rest of the signal, will stand out as a spike in its spectrum.

# Appendix B Random Processes and Variables

Noise phenomena, due to the fluctuations of a thermodynamic system or the quantum nature of interactions, impose a practical and theoretical limit on any measurement. Some basic mathematical notions are useful, given the importance of this subject in the book (but see the note at the beginning of Appendix A).

# B.1 Random Variables

# Definition of a Random Variable (r.v.)

Consider a process (for example, dice-throwing or absorption of a photon by the photoelectric effect), which has a number of possible outcomes $\zeta$ . A pre-assigned rule associates a quantity $\mathbf { x } ( \zeta )$ with each outcome. (The r.v. is denoted $\mathbf { X }$ , not to be confused with the notation for a vector $\boldsymbol { x }$ . The difference should be clear from the context. Naturally, a vector can also be a random variable, but we shall not introduce any specific notation to cover this case.) $\mathbf { x } ( \zeta )$ is called a random variable of probability $P ( \zeta )$ , where $P ( \zeta )$ is the probability of getting the result $\zeta$ (Fig. B.1).

We denote by $\{ \mathbf { x } \leq x \}$ the set of outcomes for which the random variable $\mathbf { X }$ has f  ga value no larger than a number $x$ . This set may be empty, or contain just one, or several, or all the outcomes, and each of these cases is called an event. Each event, in turn, has a probability associated with it, so that probability becomes a positive definite function on the set of events, satisfying certain rules to be stated below.

A real random variable is defined when the set $\{ \mathbf { x } \leq x \}$ is an event for any real number $x$ f  g. It is also required that the probabilities of the events $\{ { \bf x } = - \infty \}$ and $\{ { \bf x } = + \infty \}$ should be zero.

D C1gA complex random variable is defined by a process which associates with each outcome $\zeta$ a complex number

$$
{ \bf z } ( \zeta ) = { \bf x } ( \zeta ) + \mathrm { i } { \bf y } ( \zeta ) ,
$$

![](images/3b8d14aca7850afb4a1775b0d93cd1709e2f196e5b04ca262f0ab4402b727330.jpg)  
Fig. B.1 An experiment $\varepsilon$ formed by the set of outcomes $\zeta$ (here discrete), with each of which is associated the value $\mathbf { x } ( \zeta )$ of the r.v. x

in such a way that the functions $\mathbf { X }$ and $\mathbf { y }$ are themselves real random variables. Unless otherwise stated, all random variables in the following are real.

# Distribution Function

Given a real number $x$ , the set $\{ \mathbf { x } \leq x \}$ of all outcomes $\zeta$ such that $\mathbf { x } ( \zeta ) \le x$ , is an event. The probability $P \{ \mathbf { x } \leq x \}$ gof this event is a number depending on $x$ , and therefore a function of $x$ f  g, which we denote by $F _ { \mathbf { x } } ( x )$ , or simply $F ( x )$ if there is no risk of ambiguity regarding the r.v. it refers to. Hence,

$$
F _ { \bf x } ( x ) = P { \bf \{ x \leq }  x  \bf \} .
$$

This is called the distribution function (not to be confused with distributions) of the r.v. x. It has the following properties:

$$
F ( - \infty ) = 0 , \qquad F ( + \infty ) = 1 ,
$$

it is a non-decreasing function of $x$ , i.e.,

$$
F ( x _ { 1 } ) \leq F ( x _ { 2 } ) \qquad { \mathrm { f o r } } \ x _ { 1 } < x _ { 2 } \ ,
$$

and $F ( x )$ is right continuous, i.e.,

$$
F ( x ^ { + } ) = F ( x ) .
$$

# Probability Density

The derivative of the distribution function, in the sense of distributions,

$$
f _ { \mathbf { x } } ( x ) = \frac { \mathrm { d } F _ { \mathbf { x } } ( x ) } { \mathrm { d } x }
$$

is called the density (or density function, or sometimes frequency) of the r.v. x. (The theory of distributions makes differentiation possible even when the function is not continuous. The derivative is then not a function, but a distribution.)

If $F ( x )$ is continuous and differentiable everywhere except at a countable number of values of $x$ , the r.v. is said to be continuous. Attributing arbitrary positive values

![](images/60a54d685d9645af8c89243b935536024f22b41f99d44d0c5d151d13890550f4.jpg)  
Fig. B.2 Probability density function $f ( x )$ and corresponding Poisson . $( a = 3$ / distribution Dfunction $F ( x )$

to $f ( x )$ at the set of values of $x$ (of measure zero) at which $F$ is not differentiable, we can treat $f ( x )$ as a function defined for all $x$ .

If there are a discrete number of outcomes, $F ( x )$ has a staircase appearance, as shown in Fig. B.2. The density is then

$$
f ( x ) = \sum _ { i } p _ { i } \delta ( x - x _ { i } ) \ ,
$$

a succession of Dirac distributions of amplitude $p _ { i }$ , where $p _ { i }$ is the probability of outcome $i$ . We obtain

$$
\frac { \mathrm { d } F ( x ) } { \mathrm { d } x } \bigg | _ { x = x _ { i } } = \big [ F ( x _ { i } ) - F ( x _ { i } ^ { - } ) \big ] \delta ( x - x _ { i } ) .
$$

The probability density is normalised to unity:

$$
\int _ { - \infty } ^ { + \infty } f ( x ) \mathrm { d } x = F ( + \infty ) = 1 .
$$

# Expectation Values

The expectation of any function $\phi$ of the continuous r.v. $\mathbf { X }$ of density $f$ is written

$$
E \{ \phi ( x ) \} = \int _ { - \infty } ^ { + \infty } \phi ( x ) f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

Similarly, if $\mathbf { X }$ is a discrete r.v., taking values $x _ { n }$ with probabilities $p _ { n }$ , then

$$
E \{ \phi ( x ) \} = \sum _ { n } \phi ( x _ { n } ) P _ { n } \ .
$$

In physics, the expectation value of $\phi$ is called the ensemble average and denoted $\langle \phi \rangle$ .

h iBesides having other useful properties, the expectation value is the moment generating operator for the probability measure.

# Moments

Any probability measure is completely described by either its distribution function or its density function, but these both contain more information than we can easily apprehend. A small number of global parameters, called the moments of the distribution, already provide the essential content of the model.

For any whole positive number $k$ , the moment of order $k$ of the r.v. $\mathbf { X }$ is defined by $\mu _ { k } ^ { \prime } = E \{ \mathbf { x } ^ { k } \}$ , and the central moment of order $k$ by $\mu _ { k } = E \{ ( { \bf x } - E \{ { \bf x } \} ) ^ { k } \}$ .

D f gWe always have $\mu _ { 0 } ~ = ~ 1$ D f  f g g. Knowing all the moments (an infinite number) of a Ddistribution function amounts to knowing the distribution function $F ( x )$ .

Mean

The mean value of a continuous random variable $\mathbf { X }$ is

$$
\eta = E \{ \mathbf { x } \} = \int _ { - \infty } ^ { + \infty } x f ( x ) \mathrm { d } x \ ,
$$

where $f ( x )$ is the density of the variable. If $\mathbf { X }$ is a discrete random variable, taking the values $x _ { n }$ with probability $p _ { n }$ , then

$$
E \{ \mathbf { x } \} = \sum _ { n } x _ { n } p _ { n } \mathrm { ~ . ~ }
$$

The quantity $\eta$ gives information about how the density $f ( x )$ is centred. We can also define the most probable value of $x$ , which is that value $x _ { 1 }$ such that $f ( x _ { 1 } )$ is a maximum.

The median of $\mathbf { X }$ is that value $x _ { \mathrm { m } }$ such that

$$
P \{ \mathbf { x } \leq x _ { \mathrm { m } } \} = F ( x _ { \mathrm { m } } ) = 1 / 2 .
$$

Variance

The variance or dispersion is defined as the central moment of order two

$$
\mu _ { 2 } = E \left\{ ( \mathbf { x } - \boldsymbol { \eta } ) ^ { 2 } \right\} = \int _ { - \infty } ^ { + \infty } ( x - \boldsymbol { \eta } ) ^ { 2 } f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

This quantity, usually denoted $\sigma ^ { 2 }$ , describes how the r.v. is concentrated about its mean $\eta$ . Its positive square root is called the standard deviation or root mean square deviation (rms). It follows that

$$
\sigma ^ { 2 } = E \left\{ { \bf x } ^ { 2 } - 2 { \bf x } \eta + \eta ^ { 2 } \right\} = E \left\{ { \bf x } ^ { 2 } \right\} - 2 \eta E \left\{ { \bf x } \right\} + \eta ^ { 2 } = E \left\{ { \bf x } ^ { 2 } \right\} - \eta ^ { 2 } ,
$$

which gives the important relation

$$
\sigma ^ { 2 } = E \left\{ { \bf x } ^ { 2 } \right\} - ( E \left\{ { \bf x } \right\} ) ^ { 2 } .
$$

# Characteristic Function

The characteristic function $\varPhi ( \omega )$ of a random variable $\mathbf { X }$ is the expectation value of the new random variable exp i!x defined in terms of $\mathbf { X }$ . Hence

$$
\phi ( \omega ) = E \left\{ \exp \mathrm { i } \omega \mathbf { x } \right\} = \int _ { - \infty } ^ { + \infty } \mathrm { e } ^ { \mathrm { i } \omega x } f ( x ) \mathrm { d } x \mathrm { ~ . ~ }
$$

This is just the Fourier transform of $f ( x )$

$$
\Phi ( \omega )  f ( x ) .
$$

Similarly, if $\mathbf { X }$ is a discrete random variable

$$
\phi ( \omega ) = \sum _ { k } \mathrm { e } ^ { \mathrm { i } \omega x _ { k } } P \left\{ { \bf x } = x _ { k } \right\} .
$$

# Some Important Random Variables

It can be shown that, given a function $G ( x )$ such that

$$
\begin{array} { c l c r } { { G ( - \infty ) = 0 \ , } } & { { G ( + \infty ) = 1 \ , } } & { { \displaystyle \operatorname* { l i m } _ { x  \infty } G ( x ) = 1 \ , } } \\ { { } } & { { } } & { { } } \\ { { G ( x _ { 1 } ) \leq G ( x _ { 2 } ) \quad \mathrm { i f } \quad x _ { 1 } < x _ { 2 } \ , } } \\ { { } } & { { } } & { { } } \\ { { G ( x ^ { + } ) = G ( x ) \ , } } & { { } } \end{array}
$$

there exists a random process and a random variable defined on it with distribution function $G ( x )$ .

The functions $G ( x )$ below thus define random variables. Indeed, they provide a good approximation to the random behaviour of certain physical quantities.

Normal or Gaussian Distribution

The probability density of the normal distribution is given by

$$
f ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \exp \left[ - \frac { ( x - \eta ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] = N \left( x ; \eta , \sigma ^ { 2 } \right) .
$$

The distribution has two parameters: $\eta$ (position) and $\sigma$ (scale).

The corresponding distribution function is

$$
F ( x ) = \int _ { - \infty } ^ { x } f ( u ) \mathrm { d } u = 0 . 5 + \mathrm { e r f } \left( \frac { x - \eta } { \sigma } \right) ,
$$

where $\operatorname { e r f } ( x )$ denotes the error function, which can be found in tables of functions or programmed.

The parameter $\eta$ is the mean and $\sigma ^ { 2 }$ is the variance of the distribution. The odd moments about the mean are zero, and the even moments about the mean are given by

$$
\mu _ { 2 r } = \frac { ( 2 r ) ! } { 2 ^ { r } r ! } \sigma ^ { 2 r } .
$$

The two parameters $\eta$ and $\sigma$ completely specify the normal distribution. The width half way up to the peak, called the full width at half maximum or FWHM, is given by

$$
\mathrm { F W H M } = 2 \sigma \sqrt { 2 \ln 2 } \approx 2 . 3 5 4 8 \sigma .
$$

The r.v. $\mathbf { y } = ( \mathbf { x } - \eta ) / \sigma$ is a normally distributed r.v. with mean zero and variance D one. It is called the reduced normal r.v.

We shall see later that a great number of physical phenomena lead to quantities which are distributed normally. It is useful to be able to give the interval $[ - Q , + Q ]$ such that the reduced r.v. should lie with probability almost 1 in that interval:

$$
P \left\{ \left| { \frac { \mathbf { x } - \eta } { \sigma } } \right| < Q \right\} = 1 - \alpha .
$$

The parameter $Q$ determines the $( 1 - \alpha )$ confidence interval. Table B.1 gives the values of $Q$ for various values of $\alpha$ .

We deduce that a r.v. distributed as $N ( x ; \eta , \sigma )$ has probability $9 9 . 7 \%$ of lying in the interval $[ \eta - 3 \sigma , \eta + 3 \sigma ]$ Iduring a trial. The $9 9 . 7 \%$ confidence level thus  Ccorresponds to the three sigma rule.

Table B.1 Confidence intervals for the normal distribution   

<table><tr><td>(1-α)[%]</td><td>50.0</td><td>68.3</td><td>90.0</td><td>95.0</td><td>95.4</td><td>99.0</td><td>99.7</td><td>99.9</td></tr><tr><td>Q</td><td>0.6745</td><td>1</td><td>1.64</td><td>1.96</td><td>2</td><td>2.5758</td><td>3</td><td>3.2905</td></tr></table>

Poisson Distribution

The Poisson distribution gives the probability of finding $k$ events in a certain interval (an interval of time, or more generally, a range), when the events are independent of each other, unlimited in number, and occur at a constant rate in time or with a constant spacing over the range (space, for example). The probabilities of the various values of the discrete r.v. $\mathbf { X }$ , which lie in $\{ 0 , 1 , 2 , 3 , . . . \}$ , are given by

$$
P \{ { \bf x } = k \} = { \mathrm e } ^ { - a } \frac { a ^ { k } } { k ! } .
$$

The single parameter $a$ is called the parameter of the distribution. The probability density is given by

$$
f ( x ) = \mathrm { e } ^ { - a } \sum _ { 0 } ^ { \infty } { \frac { a ^ { k } } { k ! } } \delta ( x - k ) \ ,
$$

an infinite series of Dirac distributions. The mean and variance of the Poisson distribution are both equal to $a$ .

$\chi ^ { 2 }$ Distribution

A random variable has a $\chi ^ { 2 }$ distribution if its probability density is

$$
f ( x ) = \left\{ \begin{array} { l l } { \displaystyle { \frac { 1 } { 2 T ( n / 2 ) } } \left( \frac { x } { 2 } \right) ^ { n / 2 - 1 } \mathrm { e } ^ { - 1 / 2 } \mathrm { f o r } x > 0 \ : , \medskip } \\ { 0 \quad \quad \quad \quad \quad \quad \quad \mathrm { f o r } x < 0 \ : . } \end{array} \right.
$$

There is only one parameter, $n$ , which is strictly positive and called the degree of freedom. Note that if $n = 3$ , we obtain the Maxwell distribution in the kinetic theory of gases. The $\varGamma$ Dfunction is tabulated and programmable. The mean and variance of the r.v. are $n$ and $2 n$ , respectively.

The main feature of the $\chi ^ { 2 }$ distribution is as follows: if $\{ \mathbf { x } _ { i } , i = 1 , 2 , \ldots , n \}$ are $n$ f D gindependent random variables with the reduced normal distribution, then the r.v. $\chi$ defined by

$$
\chi ^ { 2 } = \sum _ { i = 1 } ^ { n } \mathbf { x } _ { i } ^ { 2 }
$$

has a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom.

# Central Limit Theorem

Let $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \mathbf { x } _ { 3 } , \ldots , \mathbf { x } _ { n }$ be a sequence of independent random variables with the same density $f _ { \mathbf { x } } ( x )$ , with mean $\eta$ and variance $\sigma ^ { 2 }$ . it can be shown that their arithmetic mean

$$
{ \overline { { \mathbf { x } } } } = { \frac { 1 } { n } } \sum _ { 1 } ^ { n } \mathbf { x } _ { i }
$$

has mean $\mu$ and variance $\sigma ^ { 2 } / n$ . It thus tends to $\mu$ when $n$ tends to infinity (law of large numbers). Furthermore, the central limit theorem (from a German term meaning that it is of central importance in probability theory) states that this variable behaves in the limit as a normal r.v. with mean $\mu$ and variance $\sigma ^ { 2 } / n$ . This result barely depends on the precise nature of the density $f$ . It is only required to have a well-defined mean and variance. There are less restrictive versions of these conclusions, e.g., when the distributions of the $\mathbf { X } _ { i }$ are different but all have a welldefined mean $\mu _ { i }$ and variance $\sigma _ { i } ^ { 2 }$ . The variable $\overline { { \mathbf { X } } }$ then behaves as a normal r.v. with mean $\eta$ and variance $\sigma ^ { 2 }$ given by

$$
\eta = \frac { 1 } { n } \sum \eta _ { i } \quad \mathrm { a n d } \quad \sigma ^ { 2 } = \frac { 1 } { n ^ { 2 } } \sum \sigma _ { i } ^ { 2 } .
$$

As $n \to \infty$ , the density $f _ { \overline { { \mathbf { x } } } } ( x )$ of $\overline { { \mathbf { X } } }$ tends to the normal distribution

$$
f ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \exp \left[ - \frac { ( x - \eta ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right] .
$$

An intuitive idea of the proof of the theorem is obtained by noting that the density $f _ { \overline { { \mathbf { x } } } } ( x )$ is the $n$ -fold convolution

$$
f _ { \overline { { \mathbf { x } } } } ( x ) = f _ { 1 } ( x ) \star f _ { 2 } ( x ) \star \cdot \cdot \star f _ { n } ( x ) ~ .
$$

But the convolution of an increasing number of positive functions, each of which tends to zero at $\pm \infty$ , tends to a Gaussian. This is easy to visualise for an $n$ -fold ˙1convolution of box functions $\varPi ( x )$ .

The central limit theorem is very useful in physics, where the statistical behaviour of a system often results from the accumulation of a large number of independent effects.

# B.2 Random or Stochastic Processes

# Definition

Consider an experiment having a set of possible outcomes $\zeta$ , where $P ( \zeta )$ is the probability. A real or complex function of time $t$ denoted by $\mathbf { x } ( t , \zeta )$ is assigned to each outcome. The family of functions thus created is called a stochastic process (abbreviated to s.p. in the following). $\zeta$ belongs to the set of outcomes of the experiment, and $t$ is a real number in $\mathrm { \Phi } ] - \infty , + \infty [$ . The notation $\mathbf { x } ( t )$ will be used to represent the process. This notation can be considered as representing four different aspects of the process:

(a) A family of functions depending on time (indexed by $\zeta$ ).   
(b) A particular function of time ( $\zeta$ being fixed).   
(c) A random variable (at fixed $t$ , for a set of trial outcomes $\zeta$ ).   
(d) A number (at fixed $t$ , and for fixed $\zeta$ ).

Aspect (c) is clearly a necessary condition if we hope to speak of a random process. The following three examples should motivate these definitions:

• The experiment consists in choosing a molecule of a gas and the quantity $\mathbf { x } ( t )$ is the component of its velocity along a given axis. This component varies in time. • The experiment consists in choosing an oscillator from the production line. The output voltage of the oscillator can be written

$$
{ \bf x } ( t , \zeta ) = { \bf a } ( \zeta ) \sin \omega _ { \zeta } t \ ,
$$

where amplitude and frequency depend on the oscillator. The sequence of output voltages is a stochastic process. Note that in this case the function ${ \bf x } ( t )$ is completely determined for any given outcome, i.e., for any choice of oscillator.

• The experiment consists in throwing a die, and

$$
\begin{array} { r } { { \mathbf x } ( t ) = \left\{ \begin{array} { l l } { \sin t \quad \quad \quad \mathrm { f o r h e a d s } , } \\ { { \mathbf x } ( t ) = 2 t \quad \quad \quad \mathrm { f o r t a i l s } . } \end{array} \right. } \end{array}
$$

The function representing $\mathbf { x } ( t )$ is random, but completely specified after each throw.

Figure B.3 illustrates the various ways of thinking about random processes. $\mathbf { x } ( t )$ is assumed to be real.

![](images/44fe72ad53a193237390f9e5f45bba7a1c16694a8941e012d44209594c473aa7.jpg)  
Fig. B.3 Different representations of a continuous stochastic process $\mathbf { x } ( t )$ . (a) $\mathbf { x } ( t , \zeta )$ is a random function of $t$ . (b) $\mathbf { x } ( t , \zeta )$ is a determinate function of $t$

# Distribution Function

The first order distribution function of the stochastic process ${ \bf x } ( t )$ is

$$
F ( x ; t ) = P \{ { \bf x } ( t ) \leq x \} ,
$$

the probability of the event $\{ \mathbf { x } ( t ) \leq x \}$ , consisting of all the outcomes $\zeta$ such that, at time $t$ , the functions $\mathbf { x } ( t , \zeta )$ gdo not exceed the value $x$ .

The corresponding density function is

$$
f ( x , t ) = \frac { \partial F ( x ; t ) } { \partial x } .
$$

The second order distribution function of the stochastic process ${ \bf x } ( t )$ is defined as follows. For two times $t _ { 1 }$ and $t _ { 2 }$ , the two r.v.s $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ are used to write

$$
F ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) = P \left\{ \mathbf { x } ( t _ { 1 } ) \leq x _ { 1 } , \mathbf { x } ( t _ { 2 } ) \leq x _ { 2 } \right\} .
$$

The corresponding density function is

$$
f ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) = \frac { \partial ^ { 2 } F ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) } { \partial x _ { 1 } \partial x _ { 2 } } .
$$

# Mean of a Stochastic Process

The mean of a stochastic process is the expectation value

$$
\eta ( t ) = E \{ \mathbf { x } ( t ) \} ,
$$

and is generally time dependent.

# Autocorrelation and Autocovariance of a Stochastic Process

The autocorrelation of the stochastic process $\mathbf { x } ( t )$ is the expectation of the product of the random variables $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ , viz.,

$$
R ( t _ { 1 } , t _ { 2 } ) = E \{ \mathbf { x } ( t _ { 1 } ) \mathbf { x } ( t _ { 2 } ) \} = \int _ { - \infty } ^ { + \infty } x _ { 1 } x _ { 2 } f ( x _ { 1 } , x _ { 2 } ; t _ { 1 } , t _ { 2 } ) \mathrm { d } x _ { 1 } \mathrm { d } x _ { 2 } .
$$

The autocovariance of $\mathbf { x } ( t )$ is the mathematical expectation of the product of the random variables $\mathbf { x } ( t _ { 1 } )$ and ${ \bf x } ( t _ { 2 } )$ , viz.,

$$
C ( t _ { 1 } , t _ { 2 } ) = E \{ [ { \bf x } ( t _ { 1 } ) - \eta ( t _ { 1 } ) ] [ { \bf x } ( t _ { 2 } ) - \eta ( t _ { 2 } ) ] \} .
$$

It follows immediately that

$$
\begin{array} { r l } & { C ( t _ { 1 } , t _ { 2 } ) = R ( t _ { 1 } , t _ { 2 } ) - \eta ( t _ { 1 } ) \eta ( t _ { 2 } ) \ , } \\ & { } \\ & { \sigma _ { \mathbf { x } ( t ) } ^ { 2 } = C ( t , t ) = R ( t , t ) - \eta ^ { 2 } ( t ) \ , } \end{array}
$$

and the autocorrelation is equal to the autocovariance for a stochastic process with zero mean. The autocovariance is centred and the autocorrelation is not.

# Stationary Processes

A particularly simple case, which often arises in physics, is one in which the various moments of the r.v. ${ \bf x } ( t )$ are invariant under time translation. The time origin is thus arbitrary, and although the process is time dependent, it is conserved in a probabilistic sense.

A stochastic process $\mathbf { X }$ is said to be stationary if the random variables

$$
\mathbf { x } ( t ) \quad { \mathrm { a n d } } \quad \mathbf { x } ( t + \varepsilon )
$$

have the same statistics, for any $\varepsilon$ . A weaker definition, which is often sufficient in practice, requires the mean of the s.p. to be time independent and the autocorrelation to depend only on the interval $\tau = t _ { 2 } - t _ { 1 }$ and not on $t _ { 2 }$ :

$$
E \{ { \bf x } ( t ) \} = \eta = \mathrm { c o n s t a n t } , \quad E \{ { \bf x } ( t + \tau ) { \bf x } ( t ) \} = R ( \tau ) .
$$

# Spectral Density

The spectral density or power spectrum of a stationary s.p. ${ \bf x } ( t )$ is defined to be the Fourier transform $S ( f )$ , if it exists, of the autocorrelation function $R ( \tau )$ of the process.

# Examples of Stochastic Processes

Bearing in mind the most common applications, two random processes are described here which use the probability distributions discussed previously, namely the normal distribution and the Poisson distribution.

# Normal Process

A process $\mathbf { x } ( t )$ is said to be normal if, for all $n , t _ { 1 } , t _ { 2 } , \ldots , t _ { n }$ , the random variables $\mathbf { x } ( t _ { 1 } )$ ; : : : ; $\mathbf { x } ( t _ { n } )$ have a joint normal distribution. The statistics of a normal s.p. are completely determined by its mean $\eta ( t )$ and autocovariance $C ( t _ { 1 } , t _ { 2 } )$ . Since

$$
E \{ { \bf x } ( t ) \} = \eta ( t ) , \qquad \sigma _ { { \bf x } ( t ) } ^ { 2 } = C ( t , t ) ,
$$

the first order density of the s.p. is given by

$$
f ( x , t ) = \frac { 1 } { \sqrt { 2 \pi C ( t , t ) } } \exp \left\{ - \frac { [ x - \eta ( t ) ] ^ { 2 } } { 2 C ( t , t ) } \right\} .
$$

If the s.p. is stationary, it follows that

$$
E \{ { \bf x } ( t ) \} = \eta , \qquad \sigma _ { \bf x } ^ { 2 } = C ( 0 ) .
$$

The autocorrelation $R ( \tau )$ and the autocovariance $C ( \tau )$ of the s.p. are not determined a priori. There are infinitely many normal stochastic processes, with the same mean $\eta$ and variance $C ( 0 )$ , which differ in the function $C ( \tau )$ for $\tau \neq 0$ .

¤The power spectrum of this process is the Fourier transform of the autocorrelation function,

$$
S ( f ) = \mathrm { F T } [ R ( \tau ) ] \ ,
$$

if it exists (Wiener–Khinchine theorem).

Poisson Process

Consider an interval $[ 0 , T ]$ within which $n$ points are chosen at random. The probability of finding exactly $k$ points within the sub-interval $[ t _ { 1 } , t _ { 2 } ]$ of $[ 0 , T ]$ is given by

$$
P \left\{ k \mathrm { i n } \left[ t _ { 1 } , t _ { 2 } \right] \right\} = C _ { n } ^ { k } p ^ { k } ( 1 - p ) ^ { n - k } = \frac { n ! } { k ! ( n - k ) ! } p ^ { k } ( 1 - p ) ^ { n - k } ,
$$

where

$$
p = \frac { t _ { 2 } - t _ { 1 } } { T } .
$$

Suppose we have

$$
n \gg 1 \quad \mathrm { a n d } \quad \frac { t _ { 2 } - t _ { 1 } } { T } \ll 1 , \quad n  \infty , T  \infty , \frac { n } { T } = \mathrm { c o n s t a n t } .
$$

Then, putting $n / T = \lambda$ , the probability of finding $k$ points in an interval of length $t _ { 2 } - t _ { 1 }$ D, placed anywhere along the time axis, is

$$
P \{ k \ \mathrm { i n } \ ( t _ { 2 } - t _ { 1 } ) \} = \mathrm { e } ^ { - \lambda ( t _ { 2 } - t _ { 1 } ) } { \frac { [ \lambda ( t _ { 2 } - t _ { 1 } ) ] ^ { k } } { k ! } } \ .
$$

We thus obtain a set of point events randomly distributed in time, the probabilities associated with each interval being independent, provided that the intervals do not intersect.

![](images/62f9e018fe0cee258a4e81336b5a28ef5bd3d5b575f515be9e28d2a98e7d44b2.jpg)  
Fig. B.4 $\mathbf { x } ( t )$ is a Poisson process and $\mathbf { y } ( t )$ is a Poisson impulse process

We now define the Poisson process ${ \bf x } ( t )$ in the following way: we set $\mathbf { x } ( 0 ) = 0$ and $\mathbf { x } ( t _ { 2 } ) - \mathbf { x } ( t _ { 1 } )$ equal to the number of points in the interval $[ t _ { 1 } , t _ { 2 } ]$ D. The family of functions resulting from this definition is called the Poisson process (Fig. B.4). At a given time $t$ , the constructions $\mathbf { x } ( t )$ constitute a random variable with a Poisson distribution of parameter $\lambda t$ .

It follows immediately that

$$
\begin{array} { c } { { E \{ { \bf x } ( t _ { \mathrm { a } } ) - { \bf x } ( t _ { \mathrm { b } } ) \} = \lambda ( t _ { \mathrm { a } } - t _ { \mathrm { b } } ) ~ , } } \\ { { { } } } \\ { { E \left\{ \left[ { \bf x } ( t _ { \mathrm { a } } ) - { \bf x } ( t _ { \mathrm { b } } ) \right] ^ { 2 } \right\} = \lambda ^ { 2 } \left( t _ { \mathrm { a } } - t _ { \mathrm { b } } \right) ^ { 2 } + \lambda ( t _ { \mathrm { a } } - t _ { \mathrm { b } } ) ~ . } } \end{array}
$$

As an example of a Poisson process, consider a distant star emitting photons which are collected by a telescope. A photoelectric detector (see Chap. 7) gives an impulse at the arrival of each photon. These impulses are registered by a counter, and the counter reading constitutes a Poisson process ${ \bf x } ( t )$ .

Poisson Impulses

Consider the process $\mathbf { y } ( t )$ ,

$$
\mathbf { y } ( t ) = \sum _ { i } \delta ( t - t _ { i } ) \ ,
$$

formed from a series of Dirac distributions at the random instants $t _ { i }$ described in the last section. The process can be regarded as the limit as $\varepsilon$ tends to zero of the stochastic process

$$
{ \bf z } ( t ) = \frac { { \bf x } ( t + \varepsilon ) - { \bf x } ( t ) } { \varepsilon } ,
$$

where $\mathbf { x } ( t )$ is the Poisson s.p. It is therefore the derivative of $\mathbf { X }$ in the sense of distributions. Then

$$
{ \bf y } ( t ) = \frac { \mathrm { d } { \bf x } ( t ) } { \mathrm { d } t } = \operatorname * { l i m } _ { \varepsilon  0 } { \bf z } ( t ) { \bf \Psi } ,
$$

and in the stationary case

$$
E \{ \mathbf { y } ( t ) \} = \lambda , \quad R ( \tau ) = \lambda ^ { 2 } + \lambda \delta ( \tau ) , \quad C ( \tau ) = \lambda \delta ( \tau ) .
$$

The spectral density $S ( f )$ of the process $\mathbf { y } ( t )$ is the Fourier transform of $R ( \tau )$

$$
S ( f ) = \lambda ^ { 2 } \delta ( f ) + \lambda .
$$

Apart from an impulse at the origin, this spectral density consists of a term independent of the frequency, and is said to have a white spectral density.

# Transformation of a Process

Consider a process ${ \bf x } ( t )$ , and a rule associating a new function $\mathbf { y } ( t )$ with each function $\mathbf { x } ( t )$ . The statistics of $\mathbf { y } ( t )$ can, in general, be deduced from those of ${ \bf x } ( t )$ . There are many applications, when we regard $\mathbf { x } ( t )$ as the input of a system $S$ , and $\mathbf { y } ( t )$ as its output (Fig. B.5). The output s.p. depends partly on the input s.p. and partly on the properties of the system. One important application is filtering (see Sect. 9.1.3).

Example

Consider a stationary and central normal s.p., and the transformation

$$
\mathbf { y } ( t ) = \mathbf { x } ^ { 2 } ( t ) .
$$

The density of $\mathbf { x } ( t )$ is given by

$$
f _ { \mathbf { x } } ( x ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } \mathbf { e } ^ { - x ^ { 2 } / 2 \sigma ^ { 2 } } ,
$$

and it can be shown that the density of the s.p. $\mathbf { y } ( t )$ , which is not a normal s.p., is

$$
f _ { { \bf y } } ( y ) = \frac { 1 } { \sqrt { 2 \pi R ( 0 ) y } } \exp \left[ - \frac { y } { 2 R ( 0 ) } \right] H ( y ) ,
$$

where $R ( \tau )$ is the autocorrelation of $\mathbf { x } ( t )$ and $H$ is the Heaviside step function.

The autocorrelation of the s.p. $\mathbf { y } ( t )$ can be deduced from the relation

$$
E \{ \mathbf { x } ^ { 2 } ( t + \tau ) \mathbf { x } ^ { 2 } ( t ) \} = E \{ \mathbf { x } ^ { 2 } ( t + \tau ) \} E \{ \mathbf { x } ^ { 2 } ( t ) \} + 2 E ^ { 2 } \{ \mathbf { x } ( t + \tau ) \mathbf { x } ( t ) \} ,
$$

which gives

$$
R _ { \mathbf { y } } ( \tau ) = R ^ { 2 } ( 0 ) + 2 R ^ { 2 } ( \tau ) \ .
$$

The variance of $\mathbf { y } ( t )$ is then

$$
\sigma _ { \mathbf { y } } ^ { 2 } = E \{ \mathbf { y } ^ { 2 } ( t ) \} - E ^ { 2 } \{ \mathbf { y } ( t ) \} = 2 R ^ { 2 } ( 0 ) ~ .
$$

# Ergodicity of a Stochastic Process

The ergodicity of an s.p. bears on the question of whether, starting from a single outcome $\mathbf { x } ( t , \zeta )$ of an experiment, it is possible to determine the statistical properties of the stochastic process ${ \bf x } ( t )$ . Put another way, are the mean, variance, autocorrelation, and so on, calculated from a single outcome $x ( t )$ , identical to the same quantities evaluated for the entire set of outcomes as we have defined them above?

It is intuitively clear that such a result can only hold if the process is stationary and if $x ( t )$ takes all possible values in the course of time. Not all stochastic processes will satisfy this condition. Consider the example of the oscillators given above; the variance of the s.p. is not equal to the variance of the voltage measured for a particular outcome.

In a physical process, the time variation of the variable is easily accessible using some measuring device. On the other hand, it is generally difficult to measure a large number of independent outcomes of the s.p. at the same instant $t _ { 0 }$ . Ergodicity is therefore a property which facilitates statistical analysis. (Brownian motion is an example of an ergodic process: it makes no difference whether we take the time average of the velocity of one molecule, or the mean over the whole set of molecules at a given time. The velocity of any molecule will range over all possible values in the course of time.)

Definition. A stochastic process $\mathbf { x } ( t )$ is ergodic if the averages taken over time are equal to the averages taken over the ensemble, that is, the expectation values.

We can establish criteria for the ergodicity of a stationary s.p. by formulating the notion of a time average. Define

$$
\begin{array} { c } { { \displaystyle x _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) \mathrm { d } t \mathrm { ~ , ~ } } } \\ { { \displaystyle \hat { R } _ { T } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ . ~ } } } \end{array}
$$

Then $\mathbf { X } _ { T }$ and $\hat { \mathbf { R } } _ { T } ( \tau )$ are respectively a random variable and a stochastic process, whose values are determined for each outcome $\zeta$ . We wish to establish conditions for the following to hold:

$$
\begin{array} { c } { { \displaystyle \operatorname* { l i m } _ { T  \infty } x _ { T } = \eta = E \{ { \bf x } ( t ) \} ~ , } } \\ { { \displaystyle \operatorname* { l i m } _ { T  \infty } \hat { R } _ { T } ( \tau ) = R ( \tau ) = E \{ { \bf x } ( t ) { \bf x } ( t + \tau ) \} ~ . } } \end{array}
$$

The question is closely related to the following: starting from a physical measurement made over a finite time $T$ and giving the values of one outcome $x ( t )$ of the stochastic process during this interval, is it possible to obtain significant information about the expectation values characterising the s.p., such as the mean, variance, autocorrelation, and so on?

The expressions $x _ { T }$ and $\hat { R } _ { T } ( \tau )$ do not always converge to the corresponding expectation values. This point will be discussed in more detail later (see Sect. B.3), when measurements of random physical quantities are considered.

# Filtering

Frequency Filtering

Consider the linear operation

$$
y ( t ) = \int _ { - \infty } ^ { + \infty } x ( t - \theta ) h ( \theta ) \mathrm { d } \theta
$$

applied to a stationary process $\mathbf { x } ( t )$ , where $h ( \theta )$ is a given function. This convolution is called filtering of the process $\mathbf { x } ( t )$ by the filter $h$ :

$$
y ( t ) = x ( t ) \star h ( t ) .
$$

From the convolution theorem

$$
\tilde { y } ( s ) = \tilde { x } ( s ) \tilde { h } ( s ) ,
$$

where

$$
\tilde { h } ( s ) = \int _ { - \infty } ^ { + \infty } h ( t ) \mathrm { e } ^ { 2 \mathrm { i } \pi s t } \mathrm { d } t
$$

is called the transfer function of the filter and is generally complex. If we set $x ( t ) =$ $\delta ( t )$ , we obtain

$$
\begin{array} { r } { y ( t ) = h ( t ) . } \end{array}
$$

This implies that the function $h ( t )$ is the response of the filter to an instantaneous impulsive input signal. It is also called the impulsive filter response.

The function $| \tilde { h } ( s ) | ^ { 2 }$ is the transfer function for the spectral power, or power, of j jthe filter. It is real and positive, but only gives information about the modification of the amplitude spectrum of the process by the filter. It reveals nothing about modifications to the phase.

Time Filtering

When a process $\mathbf { x } ( t )$ is measured over an interval $[ - T / 2 , T / 2 ]$ , and assumed to be zero outside this interval, this is equivalent to considering a second process $\mathbf { y } ( t )$ such that

$$
{ \bf y } ( t ) = \pi \left( \frac { t } { T } \right) { \bf x } ( t ) .
$$

Such a situation is typical of a physical measurement, where a signal can only be measured during some finite time $T$ . The Fourier transform of the above expression is

$$
\tilde { y } ( s ) = \tilde { x } ( s ) \star T \mathrm { s i n c } ( T s ) \ ,
$$

so that multiplication by the box function in time amounts to a convolution in frequency space. This convolution constitutes a blurring of the spectrum of the original process due to the fact that the signal is only measured for a finite time. It should be noted in particular that all information about frequencies below $1 / T$ is lost.

# B.3 Physical Measurements and Estimates

In this section we discuss physical problems for which the rigorous mathematical theory of probability was developed. In real physical situations, a continuous or discrete quantity is only ever measured finitely often or over a finite time. It is in the nature of things that the results of repeating the same experiment should be different and random in character. As seen in Sect. 7.2, this fluctuation or noise is an apparently unavoidable feature of all physical measurement.

The physicist studying some physical phenomenon, for example a quantity $x$ varying in time, can only do so over some finite period of time $T$ . He can then evaluate the mean, variance, or other attributes, for the resulting discrete or continuous measurements. The same situation would arise if he measured a quantity $y$ (for example, a pressure) a certain number of times. Each measurement would give a different result, and he could once again evaluate a mean and a variance. It could then be said that we are studying the statistics of the phenomenon $x ( t )$ or the quantity $y$ . The change in terminology, from speaking of probabilities to speaking of statistics, is an indication that a priori we do not know whether or not $x ( t )$ or $y$ have the properties of a process or a random variable.

Measurements provide an instance or an observation of the underlying phenomenon. Statistical calculation (of mean, variance, and so on), carried out on the values thus obtained, provides estimators of the mean and variance of the underlying process $\mathbf { x } ( t )$ or random variable $\mathbf { y }$ , insofar as these can be supposed to constitute a correct representation of the physical phenomena. These estimators are themselves fluctuating quantities; a further set of measurements leads to a new value of the estimators. The problem facing the statistician is to evaluate the validity of these estimators with a view to describing some underlying reality.

As physical measurement always involves estimation, it is actually an abuse of language to speak of measuring the moments of a variable or a stochastic process. This abuse is so widespread that we shall also indulge in it, having drawn attention to the problem.

# B.3.1 An Example of Estimation: The Law of Large Numbers

Consider a random variable $\mathbf { X }$ with mean $\eta$ and variance $\sigma ^ { 2 }$ , and an experiment $E _ { n }$ consisting of the $n$ -fold repetition of an identical experiment. The latter leads to $n$ variables $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n }$ , from which the sample mean can be calculated:

$$
{ \overline { { \mathbf { x } } } } = { \frac { 1 } { n } } ( \mathbf { x } _ { 1 } + \mathbf { x } _ { 2 } + \cdots + \mathbf { x } _ { n } ) \ .
$$

We know that

$$
E \{ \overline { { { \bf x } } } \} = \eta , \qquad \sigma _ { \overline { { { \bf x } } } } ^ { 2 } = \frac { \sigma ^ { 2 } } { n } ,
$$

and it can be shown that

$$
P \{ \eta - \varepsilon < \overline { { \mathbf { x } } } < \eta + \varepsilon \} \ge 1 - \frac { \sigma ^ { 2 } } { n \varepsilon ^ { 2 } } .
$$

The experiment $E _ { n }$ is now carried out once, giving a set of values $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ . The quantity

$$
x = { \frac { 1 } { n } } ( x _ { 1 } + x _ { 2 } + \cdots + x _ { n } )
$$

is considered to be a reliable estimate of the mean $\eta$ , for we can be practically certain that the inequality

$$
\eta - \varepsilon < x < \eta + \varepsilon
$$

will hold. Put another way, if we were to repeat the experiment a very large number of times, the quantity $x$ would satisfy these inequalities $9 9 \%$ of the time, provided

$$
1 - \frac { \sigma ^ { 2 } } { n \varepsilon ^ { 2 } } = 0 . 9 9 .
$$

We see that, compared to the rigorous results of probability theory, statistical conclusions suffer from a certain fuzziness.

# B.3.2 Estimating the Moments of a Process

Consider a stationary ergodic process $\mathbf { x } ( t )$ , with mean $\eta$ and autocorrelation $R _ { \bf x } ( t )$ . The physical measurement only provides information concerning a single instance of this process, and only during the time interval $[ 0 , T ]$ . From the measurement, the quantities

$$
\begin{array} { c } { \displaystyle { x _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) \mathrm { d } t \mathrm { ~ , ~ } } } \\ { \displaystyle { \hat { R } _ { T } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ , ~ } } } \end{array}
$$

can be calculated. A priori, these quantities are not equal to $\eta$ and $R _ { \bf x } ( t )$ . They can be regarded as instances of a random variable and a stochastic process, respectively, resulting from a transformation of the s.p. ${ \bf x } ( t )$ . Indeed, these quantities are defined for any given outcome. The physical measurement gives a single value for each and these values are called estimators of $\eta$ and $R _ { \bf x } ( t )$ .

An estimator is said to be unbiased if

$$
E \{ { \bf x } _ { T } \} = \eta , \qquad E \{ { \hat { \bf R } } _ { T } ( \tau ) \} = R _ { \bf x } ( \tau ) .
$$

We can show that, under certain convergence restrictions, the quantities $x _ { T }$ and $\hat { R } _ { T } ( \tau )$ tend to $\eta$ and $\hat { R } _ { \bf x } ( \tau )$ , respectively, as $T$ tends to infinity (see Chap. 9).

# Mean

It can be shown that the variance of the estimate $\mathbf { X } _ { T }$ is given as a function of $T$ by the expression

$$
\sigma _ { \mathbf { x } _ { T } } ^ { 2 } = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } \left[ R _ { \mathbf { x } } ( \tau ) - \eta ^ { 2 } \right] \left[ \pi \left( \frac { \tau } { T } \right) \star \pi \left( \frac { \tau } { T } \right) \right] \mathrm { d } \tau \ .
$$

# Application

Let ${ \bf x } ( t )$ be a stationary r.v. with zero mean $\mathit { \Pi } _ { \mathcal { I } } = 0 \mathit { \Pi } _ { , }$ ) and constant spectral density (i.e., white)

$$
S _ { \bf x } ( f ) = S ( 0 ) = \mathrm { c o n s t a n t } ,
$$

filtered by a low-pass filter

$$
h ( f ) = \pi \left( { \frac { f } { 2 f _ { \mathrm { c } } } } \right) .
$$

After filtering, the process $\mathbf { y } ( t )$ has variance

$$
\sigma _ { \mathbf { y } } ^ { 2 } = R ( 0 ) - \eta ^ { 2 } = R ( 0 ) = \int _ { - \infty } ^ { + \infty } S _ { \mathbf { y } } ( f ) \mathrm { d } f = 2 f _ { \mathrm { c } } S ( 0 ) .
$$

Let us now calculate the variance of the estimate ${ \bf y } _ { T }$ made on the interval $[ 0 , T ]$ :

$$
\begin{array} { l } { { \displaystyle y _ { T } = \frac { 1 } { T } \int _ { 0 } ^ { T } y ( t ) \mathrm { d } t \ : , } } \\ { { \displaystyle \sigma _ { \mathrm { y } _ { T } } ^ { 2 } = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } R _ { \mathrm { y } } ( \tau ) \left[ \pi \left( \frac { \tau } { T } \right) \star \cal I \left( \frac { \tau } { T } \right) \right] \mathrm { d } \tau } } \\ { { \displaystyle \quad = \frac { 1 } { T } \left| \mathrm { F T } [ R _ { \mathrm { y } } ( \tau ) ] \star T [ \mathrm { s i n c } ( T f ) ] ^ { 2 } \right| _ { f = 0 } } } \\ { { \displaystyle \quad = \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } { \cal S } ( f ) \left| \mathrm { s i n c } ( T f ) \right| ^ { 2 } T \mathrm { d } f \ : , } } \end{array}
$$

noting that

$$
\Pi \left( \frac { \tau } { T } \right) \star \Pi \left( \frac { \tau } { T } \right) = \Lambda \left( \frac { \tau } { T } \right) , \quad \mathrm { F T } [ R _ { \mathbf { y } } ( \tau ) ] = S ( f ) .
$$

If $T \gg 1 / f _ { \mathrm { c } }$ , a condition that is easily satisfied, $\sigma _ { \mathbf { y } _ { T } } ^ { 2 }$ is approximated by

$$
\sigma _ { \mathbf { y } _ { T } } ^ { 2 } \simeq \frac { 1 } { T } S _ { \mathbf { y } } ( 0 ) ,
$$

and hence

$$
\sigma _ { \mathbf { y } _ { T } } ^ { 2 } \simeq \frac { \sigma _ { \mathbf { y } } ^ { 2 } } { 2 f _ { \mathrm { c } } T } .
$$

The estimate ${ \bf y } _ { T }$ of the mean of the s.p. has indeed a variance tending to zero as $T$ increases.

# Autocorrelation

In a similar way, the estimator of the autocorrelation function is taken to be

$$
\hat { R } ( \tau ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t ) x ( t + \tau ) \mathrm { d } t \mathrm { ~ . ~ }
$$

It can be shown that this estimator is unbiased and that its variance

$$
\mathrm { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} = E \left\{ | \hat { \mathbf { R } } ( \tau ) - R _ { \mathbf { x } } ( \tau ) | ^ { 2 } \right\}
$$

tends to zero, when $T$ tends to infinity. For large $\tau$

$$
\operatorname { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} \simeq \frac { 1 } { T } \int _ { - \infty } ^ { + \infty } R _ { \mathbf { x } } ^ { 2 } ( \tau ) \mathrm { d } \tau .
$$

When the process has white spectral density and is limited to frequencies $f < f _ { \mathrm { c } }$ , it follows that

$$
\mathrm { V a r } \{ \hat { \mathbf { R } } ( \tau ) \} \leq \frac { R _ { \mathrm { x } } ^ { 2 } ( 0 ) } { f _ { \mathrm { c } } T } \ .
$$

# Spectral Density

Can the quantity

$$
{ \frac { 1 } { T } } \left| \int _ { 0 } ^ { T } x ( t ) \mathrm { e } ^ { - 2 \pi \mathrm { i } f t } \mathrm { d } t \right| ^ { 2 }
$$

be regarded as an unbiased estimator for the spectral density $S _ { \mathbf { x } } ( f )$ of the process ${ \bf x } ( t ) ?$ This could only be the case if

$$
\operatorname* { l i m } _ { T \to \infty } { \frac { 1 } { T } } \left| \int _ { 0 } ^ { T } x ( t ) \mathrm { e } ^ { - 2 \pi \mathrm { i } f t } \mathrm { d } t \right| ^ { 2 } = S _ { \mathrm { x } } ( f )
$$

and, moreover, the variance of the estimator tends to zero as $T$ tends to infinity. In general, these conditions are not met, the estimator is biased, and care is needed over the limit as $T$ becomes large. We refer to more specialised treatments for further discussion.

The power spectrum can also be estimated by measuring the signal through a filter $\tilde { g } ( f )$ of width $\Delta f$ , centred on the frequency $f _ { 0 }$ . Then

$$
{ \hat { S } } ( f _ { 0 } ) = { \mathrm { e s t i m a t o r ~ o f ~ } } S _ { \mathbf { x } } ( f _ { 0 } ) = { \frac { 1 } { T } } \int _ { 0 } ^ { T } | y ( t ) | ^ { 2 } \mathrm { d } t
$$

![](images/5c01bd532b2acf9c0fa75077d9224b4a30386f76155aebe60edb75f097c26fb0.jpg)  
Fig. B.6 Estimation of the mean and power spectrum of a stochastic process $\mathbf { x } ( t )$ . (a) An instance $x ( t , \zeta )$ of the process. (b) The process $\mathbf { y } ( t )$ obtained from $\mathbf { x } ( t )$ by the low-pass filtering $h ( f )$ , with cutoff frequency $f _ { \mathrm { c } }$ . The high frequencies have disappeared. (c) Physical measurement of $\mathbf { y } ( t )$ over a time $T$ . (d) Autocorrelation function $R _ { \bf x } ( \tau )$ of the process $\mathbf { x } ( t )$ , and autocorrelation function $\hat { R } _ { \bf y } ( \tau )$ of the measurement, Othe dashed curves giving the confidence interval $\sigma _ { \mathrm { c } }$ . The mean $\eta = 0$ of the s.p. $\mathbf { x } ( t )$ , Dand the estimate $y _ { T }$ of this mean . $( y _ { T } \neq 0 )$ /, have also ¤been indicated

with

$$
\tilde { y } ( f ) = \tilde { x } ( f ) .
$$

It can then be shown that

$$
\operatorname { V a r } \{ \hat { \mathbf { S } } ( f _ { 0 } ) \} = \frac { S _ { \mathbf { x } } ^ { 2 } ( f ) } { T \Delta f } .
$$

Figure B.6 illustrates the above discussion.

# Appendix C Physical and Astronomical Constants

The vast majority of physical and astronomical constants required in this book can be found in Allen C.W., Astrophysical Quantities (AQ). A few of the most frequently used quantities are quoted here.

<table><tr><td>Speed of light</td><td>C</td><td>2.999792 458×10m s-1</td></tr><tr><td>Gravitational constant</td><td>G</td><td>6.670 × 10-1 N m² kg-2</td></tr><tr><td>Planck&#x27;s constant</td><td>h</td><td>6.626 20 × 10-34 J s</td></tr><tr><td>Electron charge</td><td>e</td><td>1.602 192 × 10-19 C</td></tr><tr><td>Electron mass</td><td>me</td><td>9.109 56 × 10-31 kg</td></tr><tr><td>Boltzmann&#x27;s constant</td><td>k</td><td>1.380 62 ×10-23 JK-1</td></tr><tr><td>Proton mass</td><td>mp</td><td>1.672 661 × 10-27 kg</td></tr><tr><td>Rydberg constant</td><td>RH</td><td>109 677.576cm-1</td></tr><tr><td>Zeeman shift</td><td>△v/B</td><td>1.399 61 × 10l° Hz T-1</td></tr><tr><td>Wavelength associated with1eV</td><td>20</td><td>1.23985×10-6m</td></tr><tr><td>Frequency associated with1eV</td><td>Vo</td><td>2.417 965 ×1014 Hz</td></tr><tr><td>Temperature associated with1eV</td><td></td><td>11604.8K</td></tr><tr><td>Astronomical unit</td><td>AU</td><td>1.495 979 × 10ll m</td></tr><tr><td>Parsec</td><td>pc</td><td>3.085 678 ×1016 m 3.261 633 light yr</td></tr><tr><td>Mass of Sun</td><td>Mo</td><td>1.989 × 1030 kg</td></tr><tr><td>Radius of Sun</td><td>R</td><td>6.9599×10m</td></tr><tr><td>Luminosity of Sun</td><td>LO</td><td>3.826×1026W</td></tr></table>

# Blackbodies

<table><tr><td>Stefan-Boltzmann constant Planck&#x27;s law</td><td>g = 5.66956×10-8Wm-²K-4 Bx =2hc²λ-5/(ehc/kλT-1) [W m-² m-1 sr-1]</td></tr></table>

# Appendix D Tables of Space Missions

Space missions at all wavelengths, as mentioned in the book.

<table><tr><td>Mission</td><td>Objective</td><td>Launch</td></tr><tr><td>Apollo</td><td>Lunar missions</td><td>1963-1972</td></tr><tr><td>AXAF(Advanced X-ray Astrophysics Facility)</td><td>X-ray observatory</td><td>1999</td></tr><tr><td>Boomerang</td><td>Balloon studying the diffuse cosmological background</td><td>1998</td></tr><tr><td>Cassini-Huygens</td><td>Exploration of Saturn</td><td>1997</td></tr><tr><td>CHANDRA (AXAF)</td><td>X-ray observatory</td><td>1999</td></tr><tr><td>Clementine</td><td>Exploration of the Moon</td><td>1994-1994</td></tr><tr><td>Corot (COnvection ROtation and</td><td>Search for exoplanets and</td><td>2006</td></tr><tr><td>planetary Transits)</td><td>asteroseismology</td><td></td></tr><tr><td>Cos-B (Cosmic ray Satellite)</td><td>y-ray observatory</td><td>1975-1982</td></tr><tr><td>Darwin</td><td>Search for exo-Earths</td><td>2010</td></tr><tr><td>Einstein FUSE (Far Ultraviolet Spectroscopic</td><td>X-ray observatory</td><td>1979</td></tr><tr><td>Explorer)</td><td>UVobservatory</td><td>1999</td></tr><tr><td>Gaia</td><td>Astrometry</td><td>2010</td></tr><tr><td>Galex (Galaxy Evolution Explorer) Glast (Gamma-ray Large Area Space</td><td>UV Observatory</td><td>2003</td></tr><tr><td>Telescope)</td><td>Y-ray observatory</td><td>2008</td></tr><tr><td>Granat</td><td>X-ray observatory</td><td>1989-1998</td></tr><tr><td>GRO (Gamma-Ray Observatory)</td><td>Y-ray observatory</td><td>1991-2000</td></tr><tr><td>HEAO (High Energy Astronomy Observatories)</td><td>High energy observatories</td><td>1979-1981</td></tr><tr><td>Hipparcos-Tycho</td><td>Astrometry</td><td>1989-1993</td></tr><tr><td>HST (Hubble Space Telescope)</td><td>Visible-IRobservatory</td><td>1990</td></tr><tr><td>Integral (International Gamma-Ray</td><td>Xandyobservatory</td><td>2002</td></tr><tr><td>Astrophysics Laboratory) IRAS (Infrared Astronomical Satellite)</td><td>IR observatory</td><td>1983</td></tr></table>

(continued)

(continued)   

<table><tr><td>Mission</td><td>Objective</td><td>Launch</td></tr><tr><td>ISO (Infrared Space Observatory)</td><td>IR observatory</td><td>1995-1998</td></tr><tr><td>IUE (International Ultraviolet Explorer)</td><td>UV observatory</td><td>1978-1996</td></tr><tr><td>JWST (James Webb Space Telescope)</td><td>Visible-IR observatory</td><td>2013</td></tr><tr><td>KAO (Kuiper Airborne Observatory)</td><td>Visible-IR observatory</td><td>1993</td></tr><tr><td>Kepler</td><td>Search for exo-Earths</td><td>2009</td></tr><tr><td>LISA (Laser Interferometer Space Antenna)</td><td>Gravitational wave detection</td><td>2018</td></tr><tr><td>Maxim (Microarcsecond X-ray Imaging Mission)</td><td>X-ray observatory</td><td>2020</td></tr><tr><td>OAO (Orbiting Astronomical Observatories)</td><td>UV observatories</td><td>1976</td></tr><tr><td>ODIN</td><td>Submillimetre observatory</td><td>2001</td></tr><tr><td>Opportunity</td><td>Exploration of Mars</td><td>2003</td></tr><tr><td>OSO8 (Orbiting Solar Observatory)</td><td>Y-ray observation of the Sun</td><td>1975-1978</td></tr><tr><td>Planck</td><td>Exploration of diffuse</td><td>2007</td></tr><tr><td>Pronaos (Projet National</td><td>cosmological background Submillimetre balloon</td><td>1994</td></tr><tr><td>d&#x27;AstronOmie Submillimétrique) Rosat (ROentgen SATellite X-ray</td><td>X-ray observatory</td><td>1992-1999</td></tr><tr><td>observatory) Rosetta</td><td>Study of a comet</td><td>2004</td></tr><tr><td>Rosita</td><td>X-ray observatory</td><td>？</td></tr><tr><td>Sas2 (Small Astronomy Satellite)</td><td>y-ray observatory</td><td>1970</td></tr><tr><td>Sigma</td><td>y-ray observatory</td><td>1989</td></tr><tr><td>SIM (Space Interferometry Mission)</td><td>X-ray observatory</td><td>2013</td></tr><tr><td>Skylab</td><td>Space station</td><td>1973-1979</td></tr><tr><td>SOFIA (Stratospheric Observatory For Infrared Astronomy)</td><td>IR and submillimetre</td><td>2004</td></tr><tr><td>Spitzer</td><td>observatory IR observatory</td><td>2003</td></tr><tr><td>STARS</td><td>Stellar photometry</td><td>2002</td></tr><tr><td>SUZAKU</td><td>X-ray observatory</td><td>2005</td></tr><tr><td>TPF(Terrestrial Planet Finder)</td><td>Search for exo-Earths</td><td>2020</td></tr><tr><td>UHURU (SAS-1)</td><td>X-ray observatory</td><td>1970-1973</td></tr><tr><td></td><td></td><td>1990</td></tr><tr><td>Ulysses</td><td>Exploration of the Sun Exploration of Mars</td><td>1975-1976</td></tr><tr><td>Viking Voyager</td><td>Exploration of the Solar</td><td>1977</td></tr><tr><td>WMAP (Wilkinson Microwave</td><td>System Exploration of diffuse</td><td>2001</td></tr><tr><td>Anisotropy Probe) XEUS (X-Ray Evolving Universe</td><td>cosmological background X-ray observatory</td><td>2010</td></tr><tr><td>Spectroscopy Mission) XMM-Newton (X-ray Multi-Mirror Mission)</td><td>X-ray observatory</td><td>1999</td></tr></table>

# Appendix E Webography

# E.1 Main Earth-Based Telescopes

<table><tr><td>Site</td><td>Name</td><td>Type and diameter</td><td>Nationality</td><td>URL</td></tr><tr><td colspan="5">Radio and submillimetre</td></tr><tr><td>Australia</td><td>Australia Telescope Compact</td><td>Radio (6 m × 22 m)</td><td>Australia</td><td>http://www.narrabri. atnf.csiro.au/</td></tr><tr><td>Australia</td><td>Array Mopra Antenna</td><td>Radio (22 m)</td><td>Australia</td><td>http://www.atnf.csiro. au/</td></tr><tr><td>Australia</td><td>Parkes Observatory</td><td>Radio (64 m)</td><td>Australia</td><td>http://www.parkes.atnf. csiro.au/</td></tr><tr><td>Chile</td><td>Atacama Large Millimeter/ Submillimeter Array</td><td>Europe, Japan, USA, Chile</td><td>mm (0.3-9.6)</td><td>http://science.nrao.edu/ alma/index.shtml</td></tr><tr><td>England</td><td>(ALMA) Cambridge Ryle Telescope</td><td>Radio (8×13 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/</td></tr><tr><td>England</td><td>Jodrell Bank Observatory</td><td>Radio (76 m)</td><td>England</td><td>ryle/ http://www.jb.man.ac. uk/</td></tr><tr><td>England</td><td>Cosmic Anisotropy Telescope</td><td>mm (3 × 0.7 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/ cat/</td></tr><tr><td>France</td><td>Nancay Radio Observatory</td><td>Radio (100 m)</td><td>France</td><td>http://www.obs-nancay. fr/</td></tr><tr><td>Germany</td><td>Effelsberg Radio Telescope</td><td>Radio (100 m)</td><td>Germany</td><td>http://www.mpifr-bonn mpg.de/div/ effelsberg/index_e.</td></tr><tr><td>Holland</td><td>Westerbork Synthesis Radio</td><td>Radio (14 × 25 m)</td><td>Holland</td><td>http://www.astron.nl/ radio-observatoryl public/public-0</td></tr><tr><td>India</td><td>Telescope Giant Metrewave Radio Telescope</td><td>Radio (30 × 45 m)</td><td>India</td><td>http://gmrt.ncra.tifr.res. in/</td></tr><tr><td>Japan</td><td>Nobeyama Radio Observatory</td><td>Radio (45 m)</td><td>Japan</td><td>http://www.nro.nao.ac. jp/indextop-e.html</td></tr><tr><td>Mexico</td><td>Large Millimeter Telescope</td><td>mm (50 m)</td><td>Mexico, USA</td><td> http://www.lmtgtm.org/</td></tr><tr><td>Puerto Rico</td><td>Arecibo Observatory</td><td>Radio (305 m)</td><td>USA</td><td>http://www.naic.edu/</td></tr><tr><td>Sweden</td><td>Onsala Space Observatory</td><td>mm (20 and 25 m)</td><td>Sweden</td><td>http://www.oso. chalmers.se/</td></tr><tr><td>USA</td><td>Five College Radio Astronomy</td><td>Radio (14 m)</td><td>USA</td><td>http://donald.phast. umass.edu/~fcrao/</td></tr><tr><td>USA</td><td>Observatory Green Bank</td><td>Radio (45 and 100 m)</td><td>USA</td><td> http://www.gb.nrao.</td></tr><tr><td>USA</td><td>Hat Creek Radio Observatory</td><td>Radio (6 ×6 m)</td><td>USA</td><td>edu/ http://www.hcro.org/</td></tr><tr><td>USA</td><td>Owens Valley Radio</td><td>Radio (6 × 10.4 m)</td><td>USA</td><td>http://www.ovro. caltech.edu/</td></tr><tr><td>USA</td><td>Observatory Very Large Array</td><td>Radio</td><td>USA</td><td>http://www.vla.nrao.</td></tr><tr><td>USA (Hawaii, Mauna</td><td>Caltech Submil- limeter</td><td>(27 × 25 m) mm (10.4 m)</td><td>USA</td><td>edu/ http://www.submm. caltech.edu/cso/</td></tr><tr><td>Kea) USA (Hawaii, Mauna</td><td>Observatory James Clerk Maxwell</td><td>mm (15 m)</td><td>Canada, UK,</td><td>http://www.jach. Hawaii.edu/JCMT/</td></tr><tr><td>Kea) Optical and infrared</td><td>Telescope</td><td></td><td>Holland</td><td></td></tr><tr><td colspan="3">Australia Anglo-Australian Optical (3.9 m)</td><td>Australia,</td><td>http://www.aao.gov.au/</td></tr><tr><td>Australia</td><td>Observatory Mount Stromlo and Siding</td><td>Optical (1.85</td><td>UK Australia</td><td>http://msowww.anu.</td></tr><tr><td>Chile (Cerro</td><td>Spring Observatories Gemini</td><td>and 2.3 m) Optical-IR (8 m)</td><td>USA,UK,</td><td>edu.au/observing/ http://www.gemini.edu/</td></tr><tr><td>Panch6n) and USA (Hawaii)</td><td>Observatory</td><td></td><td>Canada, Chile, Argentina, Brazil</td><td></td></tr><tr><td>Chile (Cerro Tololo)</td><td>Cerro Tololo Interamerican Observatory</td><td>optique (1, 1.5 et 4m)</td><td>USA</td><td>http://www.ctio.noao. edu/ctio.html</td></tr><tr><td>Chile (La Silla)</td><td>La Silla-ESO Facilities</td><td>Optical (1.5,2.2, 3.5,and</td><td>Europe</td><td>http://www.ls.eso.org/</td></tr><tr><td>Chile (Cerro Paranal)</td><td>Very Large Telescope</td><td>3.6 m) Optical (4 × 8 m)</td><td>Europe</td><td>http://www.eso.org/ public/teles-instr/</td></tr><tr><td>Chile</td><td>European Extremely Large</td><td>Optical (42 m)</td><td>Europe</td><td>vlt.html http://www.eso.org/ projects/e-elt/</td></tr><tr><td>England</td><td>(E-ELT) Cambridge Optical Aperture Synthesis</td><td>Optical (4 × 0.4 m)</td><td>England</td><td>http://www.mrao.cam. ac.uk/telescopes/ coast/</td></tr><tr><td>France</td><td>Telescope Observatoire de Haute- Provence</td><td>Optical (1.2, 1.5, and 1.93 m)</td><td>France</td><td>http://www.obs-hp.fr/</td></tr><tr><td>France</td><td>Observatoire Midi-Pyrenées</td><td>Optical (1 and 2 m)</td><td>France</td><td>http://www.obs-mip.fr/</td></tr><tr><td>Italy</td><td>Loiano Telescopes</td><td>Optical (0.6 and 1.5 m)</td><td>Italy</td><td>http://www.bo.astro.it/ loiano/</td></tr><tr><td>Mexico</td><td>Guillermo Haro Observatory</td><td>Optical (2.1 m)</td><td>Mexico</td><td>http://www.inaoep. mx/~astrofi/ cananea/</td></tr><tr><td>South Africa</td><td>South African Astronomical</td><td>Optical (2 m)</td><td>South Africa</td><td>http://www.saao.ac.za/</td></tr><tr><td>Spain (Calar Alto)</td><td>Observatory Calar Alto Observatory</td><td>Optical (3.5 m)</td><td>Germany,</td><td>www.caha.es</td></tr><tr><td>Spain (Canary Islands)</td><td>Telescopio Nazionale</td><td>Optical (3.5 m)</td><td>Spain Italy</td><td>http://www.tng.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Galileo THEMIS Heliographic Telescope for the Study of the Magnetism</td><td>Optical (2 m)</td><td>France, Italy</td><td>http://www.themis.iac. es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Gran Telescopio de Canarias</td><td>Optical (10 m)</td><td>Spain</td><td>http://www.gtc.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Nordic Optical Telescope</td><td>Optical (2.6 m)</td><td>Denmark</td><td>http://www.not.iac.es/</td></tr><tr><td>Spain (Canary Islands)</td><td>Isaac Newton Group</td><td>Optical (4.2, 2.5, and 1 m)</td><td>UK,Holland</td><td>http://www.ing.iac.es/</td></tr><tr><td>USA (Hawaii, Mauna</td><td>Infra-Red Telescope Facility</td><td>IR (3 m)</td><td>USA</td><td>http://irtfweb.ifa. hawaii.edu</td></tr><tr><td>Kea) USA</td><td>Giant Magellan Telescope (GMT)</td><td>Optical (24.5 m)</td><td>USA</td><td>http://www.gmto.org/</td></tr><tr><td>USA</td><td>Thirty Meter Telescope</td><td>Optical (30 m)</td><td>USA</td><td>http://www.tmt.org/</td></tr><tr><td>USA</td><td>(TMT) UK Infra-Red Telescope</td><td>IR (3.8 m)</td><td>UK</td><td>http://www.jach. hawaii.edu/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Air Force Maui Optical Station</td><td>Optical (3.7 m)</td><td>USA</td><td>UKIRT/ http://www.fas.org/ spp/military/ program/track/</td></tr><tr><td>USA</td><td>Apache Point Observatory</td><td>Optical (3.5 m)</td><td>USA</td><td>amos.htm http://www.apo.nmsu. edu/</td></tr><tr><td>USA</td><td>Palomar Observatory</td><td>Optical (1.2, 1.5, and 5 m)</td><td>USA</td><td>http://astro.caltech. edu/observatories/ palomar/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>SUBARU Telescope</td><td>Optical (8.3 m)</td><td>Japan</td><td>http://subarutelescope. org/</td></tr><tr><td>USA</td><td>Lick Observatory</td><td>Optical (3 m)</td><td>USA</td><td>http://www.ucolick. org/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>University of Hawaii Telescope</td><td>Optical (2.2 m)</td><td>USA</td><td>http://www.ifa.hawaii. edu/88inch/88inch. html</td></tr><tr><td>USA</td><td>Hobby Eberly Telescope</td><td>Optical (9 m)</td><td>USA, Germany</td><td>http://www.astro.psu. edu/het/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Canada-France- Hawaii Telescope</td><td>Optical (3.6 m)</td><td>Canada, France, USA</td><td>http://www.cfht. hawaii.edu/</td></tr><tr><td>USA (Hawaii, Mauna Kea)</td><td>Keck Observatory</td><td>Optical (2 ×10m)</td><td>USA</td><td>http://www. keckobservatory. org/</td></tr><tr><td>USA</td><td>Kitt Peak National Observatory</td><td>Optical (0.9,2.1, and 4 m)</td><td>USA</td><td>http://www.noao.edu/ kpno/</td></tr><tr><td>USA</td><td>Large Binocular Telescope Observatory</td><td>Optical (2 × 8.4 m)</td><td>USA, Italy</td><td>www.lbto.org</td></tr><tr><td>USA</td><td>Mount Wilson Observatory</td><td>Optical (1.5, 2.5m)</td><td>USA</td><td>http://www.mtwilson. edu/</td></tr><tr><td>USA</td><td>Multiple Mirror Telescope Observatory</td><td>Optical (6 × 1.8 m)</td><td>USA</td><td>http://cfa-www.harvard. edu/mmt/, http:/l www.mmto.org/</td></tr><tr><td colspan="3">Gravitational waves and neutrinos</td><td></td><td></td></tr><tr><td>Antartic</td><td>Antarctic Muon and Neutrino Detector Array</td><td>mm (13 m X 0.2 m)</td><td>USA</td><td>http://amanda.uci.edu/</td></tr><tr><td>Canada</td><td>Sudbury Neutrino Observatory</td><td>Neutrinos</td><td>Canada, UK, USA</td><td>http://www.sno.phy. queensu.ca/</td></tr><tr><td>Italy</td><td>Virgo Interferometer Laser</td><td>Gravitational waves Gravitational</td><td>France, Italy</td><td>https://wwwcascina. virgo.infn.it/</td></tr><tr><td>USA</td><td>Interferometer Gravitational Wave Observatory</td><td>waves</td><td>USA</td><td>http://www.ligo.caltech. edu/</td></tr></table>

# E.2 Recent Space Missions

<table><tr><td>Name</td><td>Period of activity</td><td>Owners</td><td>Main scientific objective and URL</td></tr><tr><td>AKARI</td><td>2006-2007</td><td>Japan, Europe</td><td>Photometric and spectroscopic observation in the region 2-180 μm in 13 spectral bands.http://www.astro-f. esac.esa.int/</td></tr><tr><td>Cassini-Huygens Mission to Saturn&amp; Titan</td><td>1997-present</td><td>Europe</td><td>Study of Saturn and Titan from the visible to the infrared. http://saturn.jpl.nasa. gov/home/</td></tr><tr><td>Chetra X-ray Observatory</td><td>1999-present</td><td>USA</td><td>Observation of X-ray emissions from high-energy phenomena such as supernovas. http://chandra.harvard.</td></tr><tr><td>COnvection ROtation et planetary Transits (COROT)</td><td>2006-2012 (or beyond)</td><td>France</td><td>edu/ Asteroseismology and search for exoplanets. http://smsc.cnes.fr/ COROT/</td></tr><tr><td>COsmic Background Explorer</td><td>1989-present</td><td>USA</td><td>IR and microwave measurement of diffuse cosmological background. http://lambda. gsfc.nasa.gov/product/cobe/</td></tr><tr><td>(COBE) Far Ultraviolet Spectroscopic Explorer (FUSE)</td><td>1999-2008</td><td>USA, France, Canada</td><td>Exploration of the Universe with high-resolution spectroscopy in the extreme UV. htp://fuse.pha.jhu.edu/</td></tr><tr><td>GALaxy Evolution2003-present EXplorer (GALEX)</td><td></td><td>USA, Korea, France</td><td>UV observation of nearby and remote galaxies. http://www.galex.caltech.edu/</td></tr><tr><td>Global Astrometric Interferometer for Astrophysics (GAIA)</td><td>~2012</td><td>Europe</td><td>Astrometry of around a billion stars in our Galaxy. http://www.rssd.esa.int/gaia/</td></tr><tr><td>High Energy Transient Explorer</td><td>2002-presentI</td><td>USA, Japan, France, Brazil, Italy,</td><td>Detection and localisation of gamma-ray bursts. http://space.mit.edu/HETE/</td></tr><tr><td>Hubble Space Telescope</td><td>1990-present</td><td>India USA</td><td>UV to IR observatory. http://www.stsci.edu/ hst/</td></tr><tr><td>(HST) INTErnational Gamma-Ray Astrophysics Laboratory (INTEGRAL)</td><td>2002-presentEurope</td><td></td><td>Detection of the highest energy phenomena in the Universe. http://sci.esa.int/science- e/www/area/index.cfm?fareaid=21</td></tr><tr><td>Infrared Space Observatory</td><td>1995-1998</td><td>Europe</td><td>Exploration of the IR Universe. http://www. sci.esa.int/iso/</td></tr><tr><td>James Webb Space Telescope</td><td>～2014</td><td>USA</td><td>Optical-IR observatory (successor to HST). http://www.jwst.nasa.gov/</td></tr><tr><td>(JWST) Kepler mission</td><td>2009-2014</td><td>USA</td><td>Detection of exoplanets. http://kepler.nasa. gov/</td></tr><tr><td>PLANCK</td><td>2009-present</td><td>Europe</td><td>Probing anisotropies in the diffuse cosmological background. http://www. rssd.esa.int/index.php?project=PLANCK</td></tr><tr><td>ROSAT</td><td>1990-1999</td><td>Germany, UK, USA</td><td>Global UV exploration of the Universe. http://heasarc.nasa.gov/docs/rosat/rosgof. html</td></tr><tr><td>ROSETTA</td><td>2004-present</td><td>Europe</td><td>Study of the comet 67P/Churyumov-Gerasimenko. http:// www.esa.int/esaSC/120389_index_0_m.</td></tr><tr><td>SOlar and Heliospheric Observatory (SOHO)</td><td>1995-present</td><td>Europe, USA</td><td>Study of the internal structure and atmosphere of the Sun. http://sohowww. nascom.nasa.gov/</td></tr><tr><td>Solar TErrestrial RElations Observatory (STEREO)</td><td>2006-present</td><td>USA</td><td>Study of coronal mass ejections from the Sun using 3D data. http://stp.gsfc.nasa. gov/missions/stereo/stereo.htm</td></tr><tr><td>Spitzer Space Telescope</td><td>2003-present</td><td>USA</td><td>Imaging and spectroscopy between 3 and 180 microns. http://www.spitzer.caltech. edu/</td></tr><tr><td>Stardust</td><td>1999-present</td><td>USA</td><td>Exploration of a comet. http://stardust.jpl. nasa.gov/</td></tr><tr><td>Wilkinson Microwave Anisotropy Probe (WMAP)</td><td>2001-present</td><td>USA</td><td>Mapping the diffuse cosmological background to investigate the formation of the first galaxies.http://map.gsfc.nasa.</td></tr><tr><td>XMM-Newton</td><td>1999-present</td><td>tEurope</td><td>gov/ To study the violent Universe,from the neighbourhood of black holes to the formation of the first galaxies.http:/ www.esa.int/science/xmmnewton, http://xmm.esac.esa.int/</td></tr></table>

# E.3 Databases

<table><tr><td>Nom</td><td>Description</td><td>URL</td></tr><tr><td>Aladin Sky Atlas</td><td>Interactive sky map giving access to digital images of every region of the sky</td><td>http://aladin.u-strasbg.fr/</td></tr><tr><td>Astrophysical CATalogs support System (CATS) of the Special Astrophysical Observatory</td><td>Several astrophysical catalogues, especially in the radio region</td><td>http://cats.sao.ru/</td></tr><tr><td>Atomic Data for Astrophysics</td><td>Data for collisional ionisation and photoionisation,recombination, opacities,etc.</td><td>http://www.pa.uky.edu/~ verner/atom.html</td></tr><tr><td>Besangon Double and Multiple Star Database</td><td>Photometric and spectroscopic data on binary and multiple star systems</td><td>http://bdb.obs-besancon.fr/</td></tr><tr><td>Canadian Astronomy Data Centre</td><td>Storage of ground and space data</td><td>http://cadcwww.dao.nrc. ca/</td></tr><tr><td>(CADC) Cassini-Huygens Mission to Saturn</td><td>Data from the Cassini-Huygens mission</td><td>http://saturn.jpl.nasa.gov/ home/</td></tr><tr><td>&amp;Titan Catalog of Infrared Observations</td><td>Access to published data on more than 10 ooo sources observed in</td><td>http://ircatalog.gsfc.nasa. gov</td></tr><tr><td>Catalogue of Galactic Supernova</td><td>the infrared Catalogue supernova remnants in the Galaxy</td><td>http://www.mrao.cam.ac. uk/surveys/snrs/</td></tr><tr><td>Remnants Center for Earth et Planetary Studies</td><td>Several thousand images of the Solar System</td><td>http://www.nasm.si.edu/ ceps/</td></tr><tr><td>(CEPS) Centre de Donnees de la Physique des</td><td>Data on plasma physics</td><td>http://cdpp.cesr.fr/</td></tr><tr><td>Plasmas Centre de Données Astronomiques de</td><td>Several thousand astronomical catalogues</td><td>http://vizier.u-strasbg.fr/</td></tr><tr><td>Strasbourg Digitized Sky Survey at LEDAS</td><td>Access to the digitised data of the STScI Digitised Sky Surveys</td><td>http://ledas- www.star.le. ac.uk/DSSimage</td></tr><tr><td>ELODIE archive</td><td>DSS and DSS-II More than 16 000 echelle spectrograms obtained with ELODIE at the Observatoire de</td><td>http://atlas.obs-hp.fr/ elodie/</td></tr><tr><td>ESO Science Archive Facility</td><td>Haute Provence Archives from all data obtained with ESO telescopes</td><td>http://archive.eso.org/</td></tr><tr><td>European Asteroidal Occultation</td><td>Observations of stellar occultations by asteroids in Europe since</td><td>http://www.euraster.net/</td></tr><tr><td>Results European Pulsar Network Data</td><td>1997 Measurements of pulsar profiles</td><td>http://www.mpifr-bonn. mpg.de/old_mpifr/div/</td></tr><tr><td>Archive Extrasolar Planets</td><td>Catalogue of all extrasolar planets</td><td>pulsar/data/ http://exoplanet.eu/</td></tr><tr><td>Encyclopedia Galactic Classical</td><td>discovered up to now List of all known population I Cepheids in our Galaxy</td><td>http://www.astro.utoronto ca/DDO/research/</td></tr><tr><td>Cepheid Database High Energy</td><td>Archives from several high energy</td><td>cepheids/ http://heasarc.gsfc.nasa.</td></tr><tr><td>Astrophysics Science Archive Research Center</td><td>space missions</td><td>gov/</td></tr><tr><td>Hypercat</td><td>Interface foracces to several extragalactic databases</td><td>http://www-obs.univ- lyon1.fr/hypercat/</td></tr></table>

(continued)

(continued)   

<table><tr><td>Nom</td><td>Description</td><td>URL</td></tr><tr><td>INTErnational Real-time MAGnetic</td><td>Data and information relating to magnetic observatories</td><td>http://www.intermagnet. org/</td></tr><tr><td>Observatory NETwork InfraRed Science</td><td>DatafromNASA's infrared and</td><td>http://irsa.ipac.caltech.edu/</td></tr><tr><td>Archive Italian Database of</td><td>millimetre missions Around 280 catalogues developed</td><td>http://db.ira.cnr.it/dira2/</td></tr><tr><td>Astronomical Catalogues LEicester Database</td><td>since 1984 by the Astronet group in Italy Access to data from high energy</td><td>http://ledas- www.star.le.</td></tr><tr><td>and Archive Service Libraries of stellar</td><td>space missions like EXOSAT and ROSAT Catalogue of stellar spectra</td><td>ac.uk/ http://www.ucm.es/info/</td></tr><tr><td>spectra McMaster Cepheid</td><td>Photometric and radial velocity data</td><td>Astrof/invest/actividad/ spectra.html http://www.physics.</td></tr><tr><td>Photometry and Radial Velocity Archive</td><td>from galactic and extragalactic Cepheids</td><td></td></tr><tr><td>Minor Planet Center Multimission Archive</td><td>Astrometric data and orbits of comets and small objects A wide range of astronphysical</td><td>http://minorplanetcenter. net/ http://archive.stsci.edu/</td></tr><tr><td>at STScI</td><td>archives,mainly in the optical, near-infrared,and UV regions</td><td>mast.html</td></tr><tr><td>NASA National Space Science Data Center</td><td>36 Tb of digital data from 440 NASA space missions</td><td>http://nssdc.gsfc.nasa.gov/</td></tr><tr><td>NASA/IPAC Extragalactic Database</td><td>Access to a large amount of published extragalactic data</td><td>http://nedwww.ipac. caltech.edu/</td></tr><tr><td>NCSA Astronomy Digital Image Library</td><td>Collection of astronomical images in FITS format</td><td>http://www.dlib.org/dlib/ october97/adil/ 10plante.html</td></tr><tr><td>Open Cluster Database</td><td>Information on more than 100 000 stars belonging to about 500 open clusters</td><td>http://www.univie.ac.at/ webda/</td></tr><tr><td>POLLUX database of stellar spectra</td><td>High-resolution optical stellar spectra</td><td>http://pollux.graal.univ- montp2.fr/</td></tr><tr><td>SDSS</td><td>Access to data from the SDSS extragalactic sky survey</td><td> http://www.sdss.org</td></tr><tr><td>SkyCat</td><td>Tool developed at the ESO for visualising images and accessing astronomical catalogues</td><td>http://archive.eso.org/ skycat/</td></tr><tr><td>TOPbase at CDS: The Opacity</td><td>Energy levels of the most abundant elements in astrophysics</td><td>http://cdsweb.u-strasbg.fr/ topbase/topbase.html</td></tr><tr><td>UK Astronomy Data Centre</td><td>Selection of data obtained by Earth-based telescopes in the UK</td><td>http://casu.ast.cam.ac.uk/ casuadc</td></tr><tr><td>VizieR Catalogue Service</td><td>Access to a complete library of published astronomical</td><td>http://vizier.u-strasbg.fr/</td></tr><tr><td>Washington Double Star Catalog</td><td>catalogues Main astrometric database of double and multiple star systems</td><td>http://ad.usno.navy.mil/ wds/wds.html</td></tr><tr><td>Wide Field Plate Database</td><td>Descriptive information about wide field photographic data stored in several places around the world</td><td>http://www.skyarchive. org/</td></tr><tr><td>XMM-Newton catalogue interface</td><td>Public interface providing access to the catalogue of sources observed byXMM-Newton</td><td>http://xcatdb.u-strasbg.fr/</td></tr></table>

# E.4 Journals

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Acta Astronomica</td><td>http://acta.astrouw.edu.pl/</td></tr><tr><td>Annual Reviews of Astronomy and Astrophysics</td><td>http://www.annualreviews.org/journal/astro</td></tr><tr><td>ASP Conference Series</td><td>http://www.astrosociety.org/pubs/cs/confseries.html</td></tr><tr><td>Astronomical Journal</td><td>http://iopscience.iop.org/1538-3881</td></tr><tr><td>Astronomy&amp; Geophysics</td><td>http://www.blackwellpublishing.com/journals/AAG/</td></tr><tr><td>Astronomy and Astrophysics</td><td>http://www.aanda.org/</td></tr><tr><td>Astrophysical Journal</td><td>http://iopscience.iop.org/0004-637X/</td></tr><tr><td>Astrophysical Journal Supplement</td><td>http://iopscience.iop.org/0067-0049/</td></tr><tr><td>Astrophysics and Space Science</td><td>http://www.wkap.nl/journalhome.htm/0oo4-640X</td></tr><tr><td>Cambridge University Press</td><td>http://www.cup.cam.ac.uk</td></tr><tr><td>Classical and Quantum Gravity</td><td>http://www.iop.org/Journals/cq/</td></tr><tr><td>ESO Publications</td><td>http://www.eso.org/gen-fac/pubs/</td></tr><tr><td>IAU publications</td><td>http://www.iau.org/science/publications/iau/</td></tr><tr><td>Icarus</td><td>http://icarus.cornell.edu</td></tr><tr><td>Journal of Astronomical Data</td><td>http://www.vub.ac.be/STER/JAD/jad.htm</td></tr><tr><td>Journal of Cosmology and Astroparticle Physics</td><td>http://www.iop.org/EJ/journal/JCAP/</td></tr><tr><td>Journal of Optics A :Pure and Applied Optics</td><td>http://www.iop.org/Journals/oa</td></tr><tr><td>Journal of the British Astronomical Association</td><td>http://www.britastro.org/journal/</td></tr><tr><td>Monthly Notices of the Royal</td><td>http://www.blackwellpublishing.com/journal.asp?</td></tr><tr><td>Astronomical Society Nature</td><td>ref=0035-8711 http://www.nature.com/</td></tr><tr><td>Observatory Magazine</td><td>http://www.ulo.ucl.ac.uk/obsmag/</td></tr><tr><td>Optics Express</td><td>http://www.opticsexpress.org/</td></tr><tr><td>Physical Review Letters</td><td>http://prl.aps.org/</td></tr><tr><td>Publications of the Astronomical Society of Australia</td><td>http://www.publish.csiro.au/nid/138.htm</td></tr><tr><td>Publications of the Astronomical Society of Japan</td><td>http://pasj.asj.or.jp/</td></tr><tr><td>Publications of the Astronomical Society of the Pacific.Electronic Edition</td><td>http://www.journals.uchicago.edu/PASP/journal/</td></tr><tr><td></td><td>http://pasp.phys.uvic.ca/</td></tr><tr><td>Science</td><td>http://www.sciencemag.org/</td></tr></table>

# E.5 Bibliographical Research

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Astrophysics Data System</td><td> http://adswww.harvard.edu/</td></tr><tr><td>E-print archive in Astrophysics (astro-ph, arXiv)</td><td>http://arxiv.org/archive/astro-ph/</td></tr></table>

# E.6 Image Sources

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td>APM Galaxy Survey</td><td>About 2 million galaxies</td><td>http://www.nottingham.ac. uk/~ppzsjm/apm/apm. html</td></tr><tr><td>Astronomy Picture of the Day</td><td>A different astronomical image for everyday of the week</td><td>http://antwrp.gsfc.nasa. gov/apod/astropix.html</td></tr><tr><td>Big Bear Solar Observatory CCD Images of</td><td>Images of the Sunat several wavelengths,updated each day Images ofMessier objects obtained</td><td>http://www.bbso.njit.edu/ http://zebu.uoregon.edu/</td></tr><tr><td>Messier Objects Center forEarth and</td><td>with several instruments Alarge collection of images of</td><td>messier.html http://www.nasm.si.edu/</td></tr><tr><td>Planetary Studies Color Stereo Photos</td><td>planets in the Solar System</td><td>ceps/ http://astro.uchicago.edu/</td></tr><tr><td>of Mars from the 2004 Rovers</td><td>Images of the surface of Mars</td><td>cosmus/projects/ marsstereo/</td></tr></table>

(continued)

(continued)   

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td>Digital Archive of Historical Astronomy</td><td>Collection of historical images</td><td>http://www42.pair.com/ infolund/bolaget/ DAHAP/</td></tr><tr><td>Pictures ESO Photo Gallery. Astronomical</td><td>Images obtained with ESO telescopes</td><td>http://www.eso.org/ outreach/gallery/astro/</td></tr><tr><td>Images Galaxy Zoo</td><td>Project for classifying a large</td><td>http://www.galaxyzoo.org/</td></tr><tr><td>Hubble Heritage</td><td>number of nearby galaxies Large collection of images obtained</td><td>http://heritage.stsci.edu/</td></tr><tr><td>Project Hubble Space Telescope</td><td>with the Hubble Space Telescope Images from the Hubble Space</td><td>http://hubblesite.org/ gallery/</td></tr><tr><td>picture gallery Infrared Space Observatory</td><td>Telescope Images from the ISO satellite</td><td>http://iso.esac.esa.int/</td></tr><tr><td>Science Gallery IPAC Image Gallery</td><td>Images fromseveral infrared space</td><td>http://coolcosmos.ipac. caltech.edu/image_</td></tr><tr><td>JPL Planetary</td><td>Images of the Solar System</td><td>galleries/missions_ gallery.html http://photojournal.jpl.</td></tr><tr><td>Photojournal Messier Pages at</td><td>Images of the Messier catalogue</td><td>nasa.gov/ http://www.seds.org/</td></tr><tr><td>SEDS Multiwavelength</td><td>Images of several nearby galaxies at</td><td>messier/ http://astronomy.swin.edu.</td></tr><tr><td>Atlas of Galaxies Multiwavelength</td><td>several wavelengths Images of the Milky Wayat several</td><td>au/staff/gmackie/atlas/ atlas_edu.html http://mwmw.gsfc.nasa.</td></tr><tr><td>Milky Way NASA JSC Digital Image</td><td>wavelengths Images from several NASA missions</td><td>gov/ http://images.jsc.nasa.gov/</td></tr><tr><td>Collection NOAO Image</td><td>Images obtained with the NOAO</td><td>http://www.noao.edu/</td></tr><tr><td>Gallery NSSDC Photo Gallery</td><td>telescope Collection of images classified in terms of the type of astrophysical</td><td>image-gallery/ http://nssdc.gsfc.nasa.gov/ photo_gallery/</td></tr><tr><td>Radio Galaxy and Quasar</td><td>object Images of extragalactic radio sources obtained with the VLA</td><td>photogallery.html http://www.cv.nrao.edu/~ abridle/images.htm</td></tr><tr><td>Images Two Micron All Sky Survey</td><td>Images from the 2MASS survey</td><td>http://www.ipac.caltech. edu/2mass/gallery/</td></tr></table>

# E.7 Education

<table><tr><td>Name</td><td>Description</td><td>URL</td></tr><tr><td colspan="3">Associations and Organisations</td></tr><tr><td>Astronomical Society of the Pacific</td><td>Education in astronomy</td><td>http://www.astrosociety.org/</td></tr><tr><td>European Association for Astronomy Education</td><td>Association with the aim of encouraging and propagating astronomy</td><td>http://www.eaae-astro.org/</td></tr><tr><td>Hands On Universe</td><td>Educational programme for students to learn about the Universe</td><td>http://www.handsonuniverse. org/</td></tr><tr><td colspan="3">Educational Sites</td></tr><tr><td>A website for popularization of Astrophysics and</td><td>Several basis lessons in astronomy</td><td>http://www.astrophysical. org/</td></tr><tr><td>Astronomy A knowledge for extragalactic astronomy and cosmology</td><td>Documents around the theme of extragalactic astronomy</td><td>http://nedwww.ipac.caltech. edu/level5/</td></tr><tr><td>Astrocentral</td><td>Popularisation</td><td>http://www.astrocentral.co. uk</td></tr><tr><td>Atlas of the Universe</td><td>Overview of the Universe on different scales</td><td>http://www. atlasoftheuniverse.com/</td></tr><tr><td>Constellations and Their Stars</td><td>A page for each constellation</td><td>http://www.astro.wisc.edu/~ dolan/constellations/</td></tr><tr><td>Curious About Astronomy?Ask an Astronomer</td><td>Site for asking professional astronomers questions</td><td>http://curious.astro.cornell. edu/</td></tr><tr><td>Falling into a Black Hole</td><td>Some information about the physics of</td><td>http://casa.colorado.edu/~</td></tr><tr><td>Imagine the Universe</td><td>black holes Astronomical site for children</td><td>ajsh/schw.shtml http://imagine.gsfc.nasa.gov/</td></tr><tr><td>Infrared Astronomy Tutorial</td><td>On the subject of infrared astronomy</td><td>http://colcosmos.ipac. caltech.edu/</td></tr><tr><td>MAP Introduction to Cosmology Page</td><td>Introduction to cosmology</td><td>http://map.gsfc.nasa.gov/m_ uni.html</td></tr><tr><td>NASA Spacelink</td><td>NASA's outreach site</td><td>http://www.nasa.gov/ audience/foreducators/ index.html</td></tr><tr><td>Ned Wright's Cosmology</td><td>Lectures on cosmology</td><td>http://www.astro.ucla.edu/~ wright/cosmolog.htm</td></tr><tr><td>Tutorial sci.astro Frequently Asked Questions</td><td>Answers to frequently asked questions</td><td>http://sciastro.astronomy.net/</td></tr><tr><td>Science Fiction Stories Using</td><td>Introduction to astrophysics through science fiction</td><td>http://www.astrosociety.org/ education/resources/scif.</td></tr><tr><td>Good Astronomy Space Time Travel</td><td>Illustrations by simulations of predictions from general relativity</td><td>html http://www.spacetimetravel.</td></tr><tr><td>StarChild</td><td>Basic lessons for children</td><td>http://starchild.gsfc.nasa.gov/</td></tr><tr><td>Windows to the Universe</td><td>General astronomy site</td><td>http://www.windows.ucar. edu/</td></tr><tr><td>History of astronomy</td><td></td><td></td></tr><tr><td>Astronomiae Historia</td><td>General history of astronomy</td><td>http://www.astro.uni-bonn. de/~pbrosche/astoria.html</td></tr><tr><td>Galileo Project</td><td>Information about Galileo</td><td>http://www.rice.edu/Galileo/</td></tr></table>

# E.8 Computing and Astronomy

<table><tr><td>Description</td><td>URL</td></tr><tr><td>Work environment</td><td></td></tr><tr><td>Basic UNIX commands</td><td>http://mally.stanford.edu/~sr/computing/basic-unix.html</td></tr><tr><td>Word processing</td><td></td></tr><tr><td>LTEX</td><td>http://www.latex-project.org/</td></tr><tr><td>An introduction to LTEX</td><td>http://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/</td></tr><tr><td>LIEX mathematical symbols</td><td>http://web.ift.uib.no/Fysisk/Teori/KURS/WRK/TeX/ symALL.html</td></tr><tr><td>Text editors (programming)</td><td></td></tr><tr><td>Emacs</td><td>http://www.gnu.org/software/emacs/</td></tr><tr><td>An introduction to Emacs</td><td>http://www2.lib.uchicago.edu/~keith//tcl-course/emacs- tutorial.html</td></tr><tr><td>IDL under Emacs</td><td>http://idlwave.org/</td></tr><tr><td>Data processing software</td><td></td></tr><tr><td>Matlab</td><td>http://mathworks.com</td></tr><tr><td>Octave (Free version of Matlab)</td><td>http://www.gnu.org/software/octave/</td></tr><tr><td>IDL</td><td>http://www.ittvis.com/index.asp</td></tr><tr><td>An introduction to IDL</td><td>http://nstx.pppl.gov/nstx/Software/IDL/idl_intro.html</td></tr><tr><td>Library of IDL routines astronomy</td><td>http://idlastro.gsfc.nasa.gov/contents.html</td></tr><tr><td>GDL (Free Version of IDL)</td><td>http://gnudatalanguage.sourceforge.net/</td></tr><tr><td>IRAF</td><td>http://iraf.noao.edu/</td></tr><tr><td>Python</td><td>http://www.python.org/</td></tr><tr><td>TOPCAT</td><td>http://www.star.bris.ac.uk/~mbt/topcat/</td></tr><tr><td>Graphics</td><td></td></tr><tr><td>Gnuplot</td><td>http://www.gnuplot.info/</td></tr><tr><td>SuperMongo</td><td>http://www.astro.princeton.edu/~rhl/sm/</td></tr></table>

# E.9 Resources

<table><tr><td>Name</td><td>URL</td></tr><tr><td>Astronomical Internet Resources</td><td>http://www.stsci.edu/resources/</td></tr><tr><td>Astronomy resources on the Internet</td><td>http://www.cv.nrao.edu/fits/www/astronomy.html</td></tr><tr><td>AstroWeb at CDS: yellow-page services</td><td>http://cdsweb.u-strasbg.fr/astroweb.html</td></tr><tr><td>WebStars</td><td>http://heasarc.gsfc.nasa.gov/docs/www_info/webstars. html</td></tr></table>

# Appendix F Acronyms

For improved readability, most of these acronyms will be given in capital letters.

AAT Anglo-Australian Telescope   
ACS Advanced Camera for Surveys   
AIC Achromatic Interferential Coronagraphy   
AIPS Astronomical Image Processing System   
ALMA Atacama Large Millimeter Array   
a.m. ante meridiem   
AMANDA Antartic Muon And Neutrino Detector Array   
AMBER Astronomical Multi-Beam Combiner   
ANTARES Astronomy with a Neutrino Telescope and Abyss environmental Research   
ASIC Application Specific Integrated Circuit   
AVO Astronomical Virtual Observatory   
AXAF Advanced X-ray Astronomical Facility   
BAT Burst Alert Telescope   
BATSE Burst And Transient Source Experiment   
BDL Bureau des Longitudes   
BIB Blocked Impurity Band   
BIH Bureau International de l’Heure   
BIMA Berkeley Illinois Maryland Array   
BIPM Bureau International des Poids et Mesures   
CAD Computer Aided Design   
CARMA Combined Array for Research in Millimeter-wave Astronomy   
CAT Cherenkov Array at Themis   
CCD Charge Coupled Device   
CDA Centre de Donnees Astronomiques (Strasbourg) ´   
CEA Commissariat a l’ \` Energie Atomique (France) ´   
CFHT Canada–France–Hawaii Telescope   
CFRS Canada–France Redshift Survey   
CHARA Center for High Angular Resolution Astronomy   
CIA   
CIAXE   
CIB   
CID INECA

Coronographe Interferom´ etrique Achromatique Ax´ e´ Cosmic Infrared Background Charge Injection Device Consorzio Interuniversitario per il Calcolo Automatico dell’Ita Nord Orientale LV Center-to-Limb Variation MA Channel Multiplier Array MB Cosmic Microwave Background MOS Complementary Metal Oxide Semiconductor NES Centre National d’Etudes Spatiales (France)´ NOC Canadian Network for Observational Cosmology NRS Centre National de la Recherche Scientifique (France) OAST Cambridge Optical Array Synthesis Telescope OB Cosmic Optical Background OBE COsmic Background Experiment OMBO Classifying Objects by Medium Band Observation OROT Convection, Rotation, et Transits planetaires ´ RIRES Cryogenic High Resolution Infrared Echelle Spectrograph SO CalTech Submillimeter Observatory ARA Deutsche Agentur f¨ur Raumfahrt Angelegenheiten (Germany) AT Digital Audio Tape EIMOS Deep Imaging Multi-Object Spectrograph ENIS Deep Near Infrared Survey IMM Differential Monitor IVA Deutsches Interferometer f¨ur Vielkanalphotometrie und Astrometrie Deutsches Luft- und Raumfahrt DORIS Determination d’Orbite et ´ Radiopositionnement Integr ´ e par ´ Satellite QE Detector Quantum Efficiency RO Direct Read Out SB Double Side Band UMAND Deep Underwater Muon And Neutrino Detector VR Direct Voltage Readout BCCD Electron Bombarded Charge Coupled Device BS Electron Bombarded Silicon CU European Currency Unit GO European Gravitation Observatory GRET Energetic Gamma-Ray Experiment Telescope LT Extremely Large Telescope -ELT European Extremely Large Telescope SA European Space Agency SO European Southern Observatory SRF European Synchrotron Research Facility

DLR

ET Ephemeris Time   
EUV Extreme Ultra Violet   
EVN European VLBI Network   
FAME Full Sky Astrometric Mapping Explorer   
FET Field Effect Transistor   
FFT Fast Fourier Transform   
FGRS (2D) Field Galaxy Redshift Survey   
FIRAS Far InfraRed Astronomical Spectrometer   
FIRST Far InfraRed Space Telescope   
FK Fundamental Katalog   
FOC Faint Object Camera (Hubble)   
FORS Focal Reducer and Spectrograph   
FP Fabry–Perot   
FT Fourier Transform   
FTS Fourier Transform Spectrometer   
FU Flux Unit   
FUSE Far Ultraviolet Spectroscopic Explorer   
FWHM Full Width at Half Maximum   
GAIA Global Space Astrometry   
GALLEX Gallium Experiment   
GHz Gigahertz   
GI2T Grand Interferom´ etre\` a deux T\` elescopes´   
GLAO Ground Layer Adaptive Optics   
GLAST Gamma-ray Large Area Space Telescope   
GLONASS GLObal’naya NAvigatsionnaya Sputnikovaya Sistema   
GMRT Giant Meter Radio Telescope   
GNO Gallium Neutrino Observatory   
GPS Global Positioning System   
HALCA Highly Advanced Laboratory for Communications and Astronomy   
HARPS High Accuracy Radial velocity Planet Searcher   
HCRF Hipparcos Celestial Reference Frame   
HDF Hubble Deep Field   
HEAO High Energy Astronomical Observatory   
HEB Hot Electron Bolometer   
HEMT High Electron Mobility Transistor   
HESS High Energy Stereoscopic System   
HETG High Energy Transmission Spectrometer   
HIPPARCOS HIgh Precision PARallax COllecting Satellite   
HPBW Half Power Beam Width   
HRS High Resolution Spectrograph (Hubble Space Telescope)   
HST Hubble Space Telescope   
HURA Hexagonal Uniform Redundant Array   
IAU International Astronomical Union   
IBC Impurity Band Conduction   
IBIS Imager on Board Integral

ICRF ICRS IDL IDRIS

International Celestial Reference Frame   
International Celestial Reference System   
Interactive Data Language   
Institut du Developpement et des Ressources en Infor´   
Scientifique (France)   
Intermediate Frequency   
Institut National des Sciences de l’Univers (France)   
Infrared Optical Telescope Array   
Image Photon Counting System   
Infrared   
Infrared Camera   
Image Reduction and Analysis Facility   
Institut de RadioAstronomie Millimetrique (France) ´   
InfraRed Astronomy Satellite   
Integral Soft Gamma Ray Imager   
Infrared Spatial Interferometer   
Interstellar Medium   
Infrared Space Observatory   
International Space Station   
International Ultraviolet Explorer   
James Clerk Maxwell Telescope   
Julian Day   
Junction Supraconducting Effect Transistor   
James Webb Space Telescope   
Kuiper Airborne Observatory   
Keck Interferometer   
Large Meter Optical Spectroscopy Telescope   
Large Binocular Telescope   
Laser Guide Star   
LIght Detection And Ranging   
Laser Interferometer Gravitational wave Observatory   
Large Interferometric Space Antenna   
Local Oscillator   
Low Frequency Array   
Least Squares   
Local Standard of Rest   
Local Thermodynamic Equilibrium   
Multi Application Curvature Adaptive Optics   
Machine A Mesurer pour l’Astronomie (France) \`   
See WMAP   
Micro Arcsecond X-ray Imaging Mission   
Multi Conjugate Adaptive Optics   
Maximum Entropy Method   
Micro Electro Mechanical System   
Magnetohydrodynamic   
IF   
INSU   
IOTA   
IPCS   
IR   
IRAC   
IRAF   
IRAM   
IRAS   
ISGRI   
ISI   
ISM   
ISO   
ISS   
IUE   
JCMT   
JD   
JSET   
JWST   
KAO   
KI   
LAMOST   
LBT   
LGS   
LIDAR   
LIGO   
LISA   
LO   
LOFAR   
LS   
LSR   
LTE   
MACAO   
MAMA   
MAP   
MAXIM   
MCAO   
MEM   
MEMS   
MHD   
MIDAS M¨unich Interactive Data Analysis System   
MIDI Mid-Infrared Interferometric Instrument   
MIRA Mitaka Optical InfraRed Interferometer   
MIS Metal Insulator Semiconductor   
MISTRAL Myopic Edge-Preserving Image Restoration Method, with Application to Astronomical Adaptive-Optics-Corrected Long-Exposure Images   
ML Maximum Likelihood   
MMT MultiMirror Telescope   
MOS Metal Oxide Semiconductor   
MPG Max-Planck Gesellschaft   
MRO Magdalena Ridge Observatory   
MTF Modulation Transfer Function   
MURA Modified Uniform Redundant Array   
NACO NAOS-Conica   
NAOS Nasmyth Adaptive Optics System   
NASA National Aeronautic and Space Administration (USA)   
NASDA National Air and Space Development Agency (Japan)   
NBS National Bureau of Standards   
NEC Noise Equivalent Charge   
NEF Noise Equivalent Flux   
NEMO Neutrino Ettore Majorana Observatory   
NEP Noise Equivalent Power   
NESTOR Neutrino Extended Submarine Telescope with Oceanographic Research   
NGC New General Catalog   
NGS Natural Guide Star   
NICMOS Near Infrared Camera for Multi-Object Spectrograph   
NOAO National Optical Astronomy Observatory (USA)   
NPOI Navy Prototype Optical Interferometer   
NRAO National RadioAstronomy Observatory (USA)   
NSF National Science Foundation   
NSO National Solar Observatory   
NTT New Technology Telescope   
OAO Orbiting Astronomical Observatory   
OECD Organisation for Economic Cooperation and Development   
OHANA Optical Hawaiian Array for Nanoradian Astronomy   
OVLA Optical Very Large Array   
OVRO Owens Valley Radio Observatory   
PACS Photodetector Array Camera and Spectrometer (Herschel missi   
PAPA Precision Analog Photon Address   
PC Photoconductor   
p.d. Potential difference   
PIAA Phase Induced Amplitude Apodization   
PICSIT Pixelated CsI Telescope (Integral mission)   
PM PhotoMultiplier   
p.m. post meridiem   
PMM Precision Measuring Machine   
POSS Palomar Optical Sky Survey   
POST POlar Stratospheric Telescope   
ppb Parts per billion   
ppm Parts per million   
PSD Power Spectral Density   
PSD Pulse Shape Discrimination   
PSF Point Spread Function   
PSR Pulsar   
PSS Palomar Sky Survey   
QSO QuasiStellar Object (quasar)   
RADAR RAdio Detection and Ranging   
RENATER Reseau National de la Recherche et de la Technologie (France)´   
RF Radiofrequency   
RGS Resolution Grating Spectrometer (X-ray mission)   
RISC Reduced Instruction Set Computer   
rms Root mean square   
ROSAT Roentgen Space Astronomical Telescope   
ROSITA Roentgen Survey with an Imaging Telescope on the ISS   
SAGE Russian American Gallium Experiment   
SALT South African Large Telescope   
SAO Smithsonian Astronomical Observatory   
SCIDAR SCIntillation Detection and Ranging   
SDSS Sloane Digital Sky Survey   
SEC Secondary Electron Conduction   
SERC Science and Engineering Research Council (UK)   
SIM Space Interferometry Mission   
SIN Superconductor Insulator Normal   
SINFONI Spectrograph for Integral Field Observation in the Near Infrared   
SIS Superconductor Insulator Superconductor   
SIT Silicon Intensified Target   
SKA Square Kilometer Array   
SMA SubMillimeter Array   
SNO Sudbury Neutrino Observatory   
SNR SuperNova Remnant   
SNU Solar Neutrino Unit   
SODAR Sonic Detection And Ranging   
SOFIA Stratospheric Observatory for Far Infrared Astronomy   
SOHO Space HelioSpheric Observatory   
SPAN Space Physics Analysis Network   
SPI Spectrometer on Integral $\gamma$ -ray mission)   
SPIRE Spectral and Photometric Imaging Receiver   
SPOT Satellite Probatoire d’Observation de la Terre   
SQUID Superconducting Quantum Interference Device   
SSB Single Side Band   
SSPM Solid State PhotoMultiplier   
STJ Superconducting Tunnel Junction   
STP Standard Temperature Pressure   
TAI Temps Atomique International   
TCP Transmission Control Protocol   
TDRSS Transmission Data and Relay Satellite System   
THz Terahertz   
TIMMI Thermal Infrared MultiMode Instrument   
TMT Thirty Meter Telescope   
TPF Terrestrial Planet Finder   
TV Television   
UCAC USNO CCD Astrograph Catalog   
UHF UltraHigh Frequency   
UKIRT United Kingdom InfraRed Telescope   
USNO United States Naval Observatory   
UT Universal Time   
UTC Universal Time Coordinated   
UV UltraViolet   
UVES UltraViolet Echelle Spectrograph   
VESPA Versatile Spectrometer Assembly   
VIMOS Visible Multiple Object Spectrograph   
VISIR VLT Imager and Spectrometer in the InfraRed   
VLA Very Large Array   
VLBI Very Long Baseline Interferometry   
VLT Very Large Telescope   
VLTI Very Large Telescope Interferometer   
VSOP VLBI Space Observatory Program   
VVDS VIMOS VLT Deep Survey   
WFPC Wide Field Planetary Camera   
WMAP Wilkinson Microwave Anisotropy Probe   
XMM X-ray Multimirror Mission   
ZIMPOL Zurich Imaging Polarimeter   
ZOG Zero Order Grating

# Bibliography

Since this book is intended as a reference, only a very limited number of books or papers have been cited, and then explicitly. The present bibliography, like the webography, supplements these references with books and review articles considered to be of fundamental importance. They are organised here by theme, with headings and subheadings that do not necessarily correspond to chapter titles in the book. We have not included atlases, which can be found in the CFHT bibliography below.

The general bibliographic sources to follow can be consulted by a highly efficient search using key words. These sources sometimes require a password, which must be obtained through a university library:

Base enterBooks.com. Bibliographic search for books, with access in French, English, or Spanish. Online address: www.enterbooks.com.   
Libraries of the European Southern Observatory (ESO). An exceptional collection of books and professional review. Online address: http://libhost.hq.eso.org:8088/uhtbin/webcat. SAO/NASA Database: Astrophysics Data System — Centre de donnees astronomiques de ´ Strasbourg (CDS). Access to all scientific journals for the professional astronomer. Online address: http://cdsads.u-strasbg.fr.   
Bibliographic Data at the Centre national de la recherche scientifique (CNRS) — Institut national des sciences de l’univers (INSU). Access to sources and open archives (HAL, ArXiv). Online address: http://biblioplanets.inist.fr.

Since the tools and methods of astronomical observation are changing fast, many useful references do not feature in didactic works, but appear rather in conference proceedings. The latter provide up-to-date results and original contributions, but do not always have the synoptic value of a textbook, nor the same level of refereeing as in a peer-reviewed journal. However, it is worth listing some particularly important organisations, to be cited generically under the more detailed subject headings below:

Experimental Astronomy. A good refereed review, published by Springer and bringing together publications on experimental aspects of astronomical observation.   
European Astronomical Society Publication Series (EAS). This series began in 2001 and can be accessed online at www.eas-journal.org.   
Astronomical Society of the Pacific Conference Series (ASP). All titles published since 2003 are available as e-books at the address www.aspbooks.org.   
Society of Photographic Instrumentation Engineers (SPIE). Professional and commercial society founded in the USA in 1955. Only the acronym is used today. Among other things, the SPIE Digital Library contains a section entitled Astronomy and Astronomical 0ptics, bringing together a large number of conference proceedings at very different levels but

well up to date, dealing with astronomical observation both on the ground and from space, telescopes, their instrumentation, and so on. The sections entitled Electronic Imaging and Processing and Optics and Electro-optics may also provide useful information. Online address: spiedigitallibrary.aip.org/.

# General References

Annual Review of Astronomy and Astrophysics. Annual Reviews Series. Annual volume published since 1963, containing a dozen review articles, generally excellent. The state of the art in observational techniques and methods is often described. This reference is denoted by ARAA (volume, page, year) in this book and in the bibliographic references below.

The Astronomy & Astrophysics Review, Springer, Berlin. European equivalent of the previous, published since 1989, edited by Th. Courvoisier in the form of several volumes each year. This contains few review articles on observation in astronomy.

The Astronomy & Astrophysics Encyclopædia, Maran S.P. Ed., Van Nostrand, New York, 1992.   
An excellent synopsis, with detailed discussions and bibliography for all astrophysical themes.   
Also discusses the main observational tools.

Encyclopedia of Astronomy and Astrophysics, Murdin, P. Ed., 4 vol., Institute of Physics, London, 2001. High-quality, up-to-date professional encyclopedia, available at http://eaa.crcexpress.com.

ALLEN C.W., Astrophysical Quantities, Cox, A. Ed. Springer, 4th edn., 2000. Defines key quantities and provides numerical values of useful constants. This is a basic reference for any astronomer, denoted by AQ in this book.

HARWIT M., Astrophysical Concepts, Springer, 2000. An excellent reference book, presenting the main physical concepts used in astrophysics.

HEYVAERTS, J., Astrophysique. Etoiles, univers et relativit ´ e, Dunod, Paris, 2006. An excellent ´ astrophysics manual at MSc and doctoral levels, with exercises.

LANG K.R., Astrophysical Formulae, Astronomy & Astrophysics Library, Springer, 3rd edn., 1999, 2 volumes, reprinted in 2006. A compendium of basic physical tools used in the main astrophysical problems. This standard reference is denoted by AF in this book.

PECKER J.C., SCHATZMAN E., Astrophysique gen´ erale, Masson, Paris, 1959. Standard but ´ sometimes out-of-date reference work. The section on observation gives a good description of conventional astronomy in the 1960s.

# Historical Works

HAWKING, S., On the Shoulders of Giants, Running Press, 2003. The main foundational texts of astronomy.

HOCKEY, T. et al. The Biographical Encyclopedia of Astronomers, Springer, 2 volumes, 2007. This book contains more than a thousand biographical descriptions of astronomers, from historical times to the present day.

LANG K.R., GINGERICH O., A Source Book in Astronomy and Astrophysics 1900–1975, Harvard University Press, 1979. Collection of key papers, reporting particularly on the considerable progress made in observational methods and associated discoveries.

VERDET J.P., Astronomie et astrophysique, Larousse, Paris, 1993. Collection of key papers, with comments and historical context.

WALLERSTEIN G., OKE J.B., The First 50 Years at Palomar, 1949–1999, Another View: Instruments, Spectroscopy, and Spectrophotometry in the Infrared, ARAA 38, 113–141, 2000.

Most annual volumes of the ARAA begin with an article in which an eminent astronomer, usually American, gives a personal account of his or her life of research and contributions. These portrayals thus form part of the rich history of twentieth century astronomy.

# Terminology

HECK A., Star Briefs 2001: A Dictionnary of Abbreviations, Acronyms, and Symbols in Astronomy and Related Space Sciences, Kluwer, 2000..

HOPKINS J., Glossary of Astronomy and Astrophysics, University of Chicago Press, 2nd edn., 1980. Rather physically oriented introduction to English and American terminology.

LANG K.R., A Companion to Astronomy and Astrophysics: Chronology and Glossary with Data Tables, Springer, 2006.

Desktop Publishing in Astronomy and Space Sciences, Heck A. Ed., World Scientific Publishing, Singapore, 1992.

HECK A., HOUZIAUX L. Future Professional Communication in Astronomy, Academie royale ´ de Belgique, 2007. Detailed analysis of the way publication has evolved with the advent of digital communications.

# Research Policy in Astronomy

HECK A. Star Guides 2001: A Worldwide Directory of Organizations in Astronomy, Related Space Sciences and Other Related Fields, Kluwer, 2003. An invaluable practical guide to all centres of research and observation, with references, addresses, and so on.

Cosmic Vision 2015–2025, European Space Agency 2008, www.esa.int/esaCP/index.html. Conclusions concerning orientations and choices for the ESA’s astronomical space missions in the specified decade.

Towards a Strategic Plan for European Astronomy, Astronet European Network, 2006. Document available at www.astronet-eu.org, and also published as a book (see next item). The result of a wide-ranging consultation on the aims and means of both ground-based and spaceborne European astronomy.

DE ZEEUW T., A Science Vision for European Astronomy, Astronet, 2007.

WOLTJER L., Europe’s Quest for the Universe, EDP, Paris, 2006. A comprehensive overview of the rebirth of European astronomy in the second half of the twentieth century, both on the ground and in space.

OECD Science, Technology, and Industry Outlook, OECD, Paris, 2010. Annual review of the main trends in public policy in member countries of the OECD.

UNESCO Science Report 2010, UNESCO, Paris, 2010. Global picture of scientific development in the world, and in particular in astronomy.

New Worlds, New Horizons in Astronomy and Astrophysics, National Academies (USA), National Academic Press, 2010. Guidelines for Earth-based and spaceborne astronomy in the USA, prepared every ten years.

JAXA Vision — JAXA 2025. Japan Aerospace Exploration Agency, Tokyo, 2005, available online at www.jaxa.jp/about/2025/index e.html. Prospects for the Japanese space programme.

Les sciences spatiales: Adapter la recherche franc¸aise aux enjeux de l’espace, Academie des´ sciences (France), Report no. 30, ed. by Puget J.L., EDP Sciences, Paris, 2010. Overview of the development of space research in France and Europe.

Long Range Plan 2010 for Canadian Astronomy and Astrophysics, National Research Council of Canada, www.casca.ca/lrp2010/index.php, 2010. Guidelines for Earth-based and spaceborne astronomy in Canada, prepared every ten years.

# Observation in Astrophysics

Modern Technology and Its Influence in Astronomy, Wall J.V. & Boksenberg A. Eds., Cambridge University Press, New York, 1990. Collective work describing trends in imaging and radiation detection.

Compendium of Practical Astronomy, Roth G.D. Ed., Vols. I, II, and III, Springer-Verlag, New York, 1994. Extremely comprehensive textbook built up from individual contributions with many references. The first volume is more specifically devoted to observation, its tools, and its techniques.

BRADT H., Astronomy Methods, Cambridge University Press, 2004.

HARWIT M., Cosmic Discovery: The Search, Scope, and Heritage of Astronomy, MIT Press, 1984. Excellent book, showing in particular how observational capabilities have conditioned astrophysical discovery.

KITCHIN C.R., Astrophysical Techniques, Taylor & Francis, 4th edn., 2003.

Exploring the Cosmic Frontier: Astrophysical Instruments for the 21st Century, Lobanov A.P. et al (Eds.), Springer, 2008.

WILSON T.L., ROHLFS K., HITTEMEISTER S., Tools of Radio Astronomy, 5th edn., Astronomy and Astrophysics Library, Springer-Verlag, New York, 2009.

SMITH R.C., Observational Astrophysics, Cambridge University Press 1995. This book ‘borrowed’ the title of the original book by LENA, P., published by Springer in 1988.

SPIE Digital Library. Instrumentation in Astronomy, CDP27. Two CDROMs presenting a set of particularly significant papers in this area, appearing in the SPIE volumes, 2002.

# Astronomical Photometry

BESSELL M.S., Standard Photometric Systems, ARAA 43, 293–336, 2005.

BUDDING E. & DEMIRCAN O., Introduction to Astronomical Photometry, 2nd edn., Cambridge University Press, 2007.

STERKEN C. & MANFROID J., Astronomical Photometry: A Guide, Kluwer, 1992. Clear and comprehensive reference.

TINBERGEN J., Astronomical Polarimetry, Cambridge University Press, 1996.

# Terrestrial Atmosphere

# Structure and Properties

VALLEY S., Handbook of Geophysics and Space Environnement, McGraw-Hill, New York, 1965. A good general reference for all properties and numerical values associated with the atmosphere and space environment of the Earth.

HOUGHTON J.T., The Physics of the Atmosphere, Cambridge University Press, 1977. Excellent introductory monograph on the physics and dynamics of the atmosphere.

HUMPHREYS W.J., Physics of the Air, Dover Publishing Inc., 1964. Old textbook (1920), but in a more recent edition that contains a good elementary description of many meteorological and atmospheric phenomena.

SALBY M.L. Fundamentals of Atmospheric Physics, International Geophysics Series, Vol. 61, Academic Press, New York, 1996. Excellent didactic book on the fundamental properties of the Earth atmosphere.

# Atmospheric and Interplanetary Radiation

GOODY R.M., Atmospheric Radiation, Cambridge University Press, 1977.

McCORMAC B.M., The Radiating Atmosphere, Reidel, Dordrecht, 1971.

REACH F.E. & GORDON J.L., The Light of the Night Sky, Reidel, Dordrecht, 1973.

Optics of Cosmic Dust, Videen G., Kocifaj M. (Eds.), NATO Workshop, Kluwer, 2002.

Interplanetary Dust, Gr¨un E., Gustafson B.A.S., Dermott S., et al. (Eds.), Springer, 2001.

Scattering in the Atmosphere (Selected Papers on), S.P.I.E. MS 07, 1989. A collection of fundamental articles on atmospheric scattering.

SPIE Digital Library. See the volumes of conference proceedings in the section on Atmospheric Sciences.

# Transmission of Electromagnetic Radiation

Atlases of the solar spectrum obtained with very high resolutions also identify telluric lines.

The Infrared Handbook. US Govt. Print. Off., Washington, 1979. Although outdated, this remains an excellent reference for theory and practice in the region $1 { - } 1 0 0 0 \mu \mathrm { m }$ .

MIGEOTTE M., NEVEN L., SWENSSON J., Le Spectre Solaire de 2.8 a\` $2 3 . 7 ~ \mu \mathrm { m }$ , Mem. Soc.´ Roy. Sc. Liege \` 2, 1957.

DELBOUILLE L., ROLAND G., BRAULT J., TESTERMAN L., Spectre solaire de $1 8 5 0 \ \mathrm { \texthat { a } }$ $1 0 0 0 0 \mathrm { c m } ^ { - 1 }$ , Universite de Li´ ege, 1981.\`

WALLACE L., HINKLE K., LIVINGSTON W., An Atlas of the Photospheric Spectrum (735– $1 1 2 3 \mathrm { n m }$ ), National Solar Observatory, Tucson, 1994.

# Atmospheric Turbulence

The Journal of Atmospheric Sciences contains research directly relating to atmospheric properties.   
For many other references, see also under the heading Adaptive Optics and Radioastronomy.

LESIEUR M., Turbulence in Fluids, 4th edn., revised and updated, Springer, 2007.

LUMLEY J.L. & PANOFSKY H.A., The Structure of Atmospheric Turbulence, Interscience, Paris, 1964.

# Astronomical Sites on Earth

Astronomical Site Evaluation in the Visible and Radio Range, Vernin J., Benkhaldoun Z., Munoz-˜ Tunon C. Eds., ASP Series vol. 266, 2002.˜

ARENA — Large Astronomical Infrastructures at CONCORDIA. Prospects and Constraints for Antarctic Optical & Infrared Astronomy, Candidi M., Epchtein N. Eds., EAS Series vol. 25, EDP, Paris, 2007.

A Vision for European Astronomy and Astrophysics at the Antarctic station CONCORDIA Dome C in the next decade 2010–2020. The ARENA Consortium, Epchtein N. Ed., arena.unice.fr, 2009.

Dome C Astronomy & Astrophysics Meeting, Giard M., Casoli F., Paletou F. (Eds.), EAS Series, vol. 14, EDP, 2005.

The Protection of Astronomical and Geophysical Sites, Kovalevsky J. Ed., Editions Frontieres,\` Gif-sur-Yvette, 1992.

ABAHAMID A., VERNIN J., BENKHALDOUN Z., Seeing, outer scale of optical turbulence, and coherence outer scale at different astronomical sites using instruments on meteorological balloons, Astron. Astrophys. 422, 1123, 2004. Interesting article for site comparisons.

GARSTANG R.H., The status and prospects for ground-based observatory sites, ARAA 27, 19–40, 1989.

# Spaceborne Observation

# Space Missions

This is not the place to give an exhaustive bibliography of spaceborne observation. The reader can consult the initial reports and feasibility studies published by the European Space Agency and other large space agencies (USA, Japan, China, Russia, etc.) whenever a new mission is under study or new guidelines are being established. See the webography for more details.

SPIE Digital Library. See the volumes of conference proceedings in the sections entitled Astronomy, Astronomical Instrumentation, Space Technologies.

# Moon-Based Observation

Towards a World Strategy for the Exploration and Utilization of our Natural Satellite, European Space Agency SP-1170, 1994.

Astrophysics from the Moon, Mumma M.J. & Smith H.J. Eds., AIP Proceedings 207, Amer. Inst.   
Phys., 1990.

# Spatial and Temporal Reference Systems

AUDOIN C., GUINOT B., LYLE S. (transl.), The Measurement of Time: Time, Frequency, and the Atomic Clock, Cambridge University Press, 2001. This book discusses the ideas and techniques involved in time measurement and the establishment of time scales.

GREEN R.M., Spherical Astronomy, Cambridge University Press, 1985. Very good and up-to-date elementary textbook, with vector formulations and taking into account relativistic effects.

KOVALEVSKY J., Modern Astrometry, 2nd edn., Astronomy and Astrophysics Library, Springer-Verlag, 2002. Recent, general work covering in some detail the many aspects of astrometry, such as image formation, instrumentation, and data compression.

KOVALEVSKY J. & SEIDELMAN P.K., Fundamentals of Astrometry, Cambridge University Press, 2004. For advanced students. The most recent textbook on current astrometry, including the most recent conventions of the International Astronomical Union.

MIGNARD F., LES echelles de temps, Introduction aux Eph ´ em´ erides Astronomiques, Connais- ´ sance des temps, Chap. 2, EDP Sciences. Updated annually in Connaissance des temps.

MURRAY C.A., Vectorial Astrometry, Adam Hilger, Bristol, 1983. This book deals above all with the relevant concepts in a very general relativistic framework which makes it difficult to follow. However, the reader’s efforts will be rewarded by the quality of the contents.

VANIER J. and AUDOIN C., The Quantum Physics of Atomic Frequency Standards, Adam Hilger, Bristol, 1989. The most comprehensive book on the physics of frequency standards. High level.

WALTER H.G., SOVERS O.J., Astrometry of Fundamental Catalogues, Springer, 2000. Monograph discussing the underlying ideas and construction of fundamental catalogues, with a detailed presentation of FK5, the Hipparcos Catalogue, and the ICRF with the VLBI technique.

The Hipparcos Mission, SP-1111, European Space Agency, 1989. Three volumes published for the launch of Hipparcos, describing the instrument, preparation and contents of the initial catalogue, and compression methods.

The Hipparcos Catalogue, SP-1200, European Space Agency, 1997. Final publication of the Hipparcos Catalogue. Volume 1 specifies the properties of the catalogue and volume 3 presents all the data processing techniques.

Reference Frames in Astronomy and Geophysics, Kovalevsky J., Mueller I.I. & Kolaczek B. Eds., Kluwer Academic Publishers, 1989. About twenty synoptic papers written by the best specialists, making a real pedagogical effort. The work covers celestial and terrestrial reference systems, the relationships between these systems, and also temporal reference systems.

High-Accuracy Timing and Positional Astronomy, van Paradijs J. & Maitzen H.M. Eds. Lecture Notes in Physics 418, Springer-Verlag, New York, 1993. Excellent didactic book resulting from the European Astrophysical Doctoral Network (EADN).

GAIA: A European Space Project, ESA Publication Series 2, O. Bienayme & C. Turon Eds., EDP´ 2002. Report from a Les Houches School on the GAIA mission and its scientific objectives.

GAIA: Composition, Formation and Evolution of the Galaxy, ESA-SCI(2000)4, 2000. Official document containing the scientific proposal for the GAIA mission, and providing a lot of information about the current situation and issues in stellar and galactic physics.

# Telescopes

BAARS J.W.M., The Paraboloidal Reflector Antenna in Radio Astronomy and Communication.   
Theory and Practice, Springer, 2007.

BELY P., The Design and Construction of Large Optical Telescopes, Springer, 2003. Excellent introductory work on new telescopes in the twenty-first century.

DANJON A. & COUDER A., Lunettes et Telescopes, Blanchard, Pa´ ris, 1983. Re-edition of an excellent classical textbook on visible observation.

KING H.C., The History of the Telescope, Dover Publish. Inc., New York, 2nd edn. 1977. Excellent historical introduction.

KITCHIN C., Solar Observing Techniques, Springer, 2002. Telescopes and instruments for observing the Sun.

LEMAITRE G., Astronomical Optics and Elasticity Theory: Active Optics Methods, Springer, 2010. Basic principles of active optics.

Astronomical Optics (selected papers on), Schroeder D. Ed., MS 73, 1993. A collection of fundamental historical articles on optical astronomy (telescopes, interferometers, turbulence, etc.), from 1920 to the present day.

ROHLFS K. & WILSON T.L., Tools of Radio Astronomy, Springer, 2004. Telescopes and instrumentation used in radio astronomy.

WILSON R.W., Reflecting Telescope Optics I. Basic Design, Theory and Its historical Developments, 2nd revised edn., Springer, 2007.

WILSON R.W., Reflecting Telescope Optics II. Manufacture, Testing, Alignement, Modern techniques, Springer, 2001. Two fundamental works dealing with the design and construction of optical telescopes.

SPIE Digital Library. See the volumes of conference proceedings in the sections entitled Astronomical Instrumentation, Astronomy.

# Optics and Image Formation

BORN M. & WOLF E., Principles of Optics, Pergamon Press, Oxford, 6th edn., 1980. Fundamental reference book, especially for the formalism of geometric or wave optics, the complete theory of diffraction, etc. Also contains the general principles of interferometers, e.g., Michelson, Fabry–Perot, particularly useful in the ultraviolet, visible, infrared, and submillimetre regions.