![](images/9ec245092f748ff3eb7183341be138cf24679b9a16fe10e4485b280f24554626.jpg)  
Fig.7.12 Thetime-frequency plane，withbinsoflength $\begin{array} { r l r } { \Delta t } & { { } \ = \ } & { T _ { \mathrm { s t a c k } } } \end{array}$ intimeand $\begin{array} { r l r } { \Delta f } & { { } = } & { 1 / T _ { \mathrm { s t a c k } } } \end{array}$ infrequency. Bins where the power exceeds a given threshold are marked in black.

turbances,which is the case in a real detector.Consider for instance the situation in which instrumental noise gives a very large spike in fre quency,during a relatively shbrt period,e.g.in only one stack.When summing the power,this single disturbance can give a large effect on the total sum，while collapsing all the information to black/white i contributes only to a single pixel.This method can therefore be appropriate when we search for a signal that is small,but is there during the whole observation time,and is embedded in a noise that occasionaly can be much larger than the signal.

The next step is to perforr a pattern recognition procedure in the set of black pixels,to see if some of the black pixels lie along a specified curve.To simplify the setting,suppose that we are searching for straight lines in the $( t , f )$ plane of Fig.7.12.(The generalization to more complex curves is conceptually straightforward.） The set of all straight lines in this plane is parametrized by two parameters $( a , b )$ ,as $t = a f + b$ We denote by $\Sigma$ the manifold described by the parameters $( a , b )$ ；in our example of straight lines of course $\Sigma = \mathbb { R } ^ { 2 }$ ,but the notation is more general. Given a black pixel, we can find the set of points in the manifold $\Sigma$ that are compatible with it;for instance,in our straight lines example if a black pixel is centered at $( t _ { 1 } , f _ { 1 } )$ ,the straight lines consistent with it are those that satisfy $t _ { 1 } = a f _ { 1 } + b$ ,and the corresponding submanifold of $\Sigma$ is the curve $b = a f _ { 1 } - t _ { 1 }$ in the $( a , b )$ plane.More precisely, since the pixels in the $( t , f )$ plane have a finite resolution,we willrather get a bunch of straight lines in $\Sigma ,$ The transformation that,to each black pixel in the $( t , f )$ plane associates a submanifold in $\Sigma$ ，isillustrated graphically in Fig.7.13.

![](images/d2d7703240845e62b2d93ddab0036175dfc6f821a0a0092f76cd0735ebcf418e.jpg)  
Fig.7.13 The map that to each black pixel associates a submanifold in the parameter space $\Sigma$

In the absence of noise,the submanifolds in $\Sigma$ obtained in this way from all the black pixels would have a non-empty intersection,which would define the point in parameter space compatible with the observations.Of course,in the presence of noise the intersection of all the curves will be empty. Still,we can try to recover the most probable value of the parameters in $\Sigma$ as follpws.First,we discretize the manifold $\Sigma$ Let us call $\mathcal { C } _ { 1 }$ the surface in $\ddagger$ obtained from the first black pixel.We then assign $+ 1$ to all the bins in $\Sigma$ that belong to $\mathcal { C } _ { 1 }$ .We repeat the same for the second black pixel,adding $+ 1$ to the the bins in $\Sigma$ that belong to $\mathcal { C } _ { 2 }$ ,and so on for all the $N$ black pixels. In conclusion,we have constructed a map that,to the set of black pixels,associates a histogram in the parameter space $\Sigma$

In the GW detection problein,the manifold $\Sigma$ becomes the parameter space $( \theta _ { s } , \phi _ { s } , \dot { f } _ { 0 } / f _ { 0 } , \ddot { f } _ { 0 } / \dot { f } _ { 0 } , . . . )$ and the straight lines of our example are replaced by the curves in $\mathrm { t h e } \left| ( t , f ) \right.$ plane that describe how $f$ changes with time because of the Doppler effect and of the spindown. The points in parameter space whose number count is above a certain threshold are the candidates for a possible detection and can be further investigated for instance with a coherent search.

# 77 Coalescence of compact binaries

The coalescence of compact binaries, such as BH-BH and NS-NS binaries,isa particularly interesting signal for broad-band GW detectors. This comes from a combination of two facts: frst,we saw in eq. (4.44) that,in the last stages of the inspiral,a binary system can radiate away in GWs up to a few per cent of its tbtal mass.This is a huge amount of energy,so the signal from an inspiral is quite strong,compared to most other GW sources.Second,the inspiral phase can be tracked for many cycles in a broad-band detector. We saw in eq. (4.23) that a groundbased interferometer can follow the inspiral phase of a compact binary system for $O ( 1 0 ^ { 4 } )$ cycles.Thus,matched fltering can be very effective for extracting this signal from the noise.From eq.(7.40) and the discussion below it we see that,in order of magnitude,with matched fltering we can dig into the noise and catch|the signal from a coalescence,even when the typical amplitude of the GW signal inside the interferometer bandwidth is smaller than the noisefoor bya factor $\mathcal { N } _ { c } ^ { 1 / 2 }$ ,where $\mathcal { N } _ { c }$ is the number of cycles for which we are able to track carefully the signal with our template. Thus, we can gain a factor as large as $\bar { \mathcal { N } } _ { c } ^ { 1 / 2 } \sim 1 0 0$ in amplitude,if our template is so good that we can follow closely the signal from the time it enters in theinterferometer bandwidth until the inspiral phase terminates and the two objects merge. Since the GW amplitude is proportional to $1 / r ,$ afactor $O ( 1 0 0 )$ in amplitude means that we gain a factor $O ( 1 0 0 )$ in the maximum distance to which we can detect a source.For these reasons,we will see that interferometers have the potential of detecting coalescing binaries up to distances of order of hundreds of Mpc,and advanced ground-based interferometers could reach a few Gpc.

To exploit this opportunity we must however be able to follow closely the signal with a template.This means,first of all,that for a given value of the parameters of the binary system (time of coalescence,，masses, spins,etc.),one must know the waveform accurately. We already quantifed this requirement in Section 5.6,where we found that we need to compute the post-Newtonian corrections up to 3.5PN order. As we saw in Section 5.6,these remarkable computations have indeed been performed. The second aspect is that we do not know in advance the parameters of the system,and therefore we must scan a potentially large parameter space.

To leading Newtonian order we computed the waveform in eq. (4.29), and the corrections in the restricted post-Newtonian approximation were discussed in Section 5.6. Combining these results with the general expression $h ( t ) = F _ { + } h _ { + } ( t ) + F _ { \times } h _ { \times }$ ，we see that the output $h ( t )$ fora binary inspiral,in the restricted post-Newtonian approximation,is

$$
\begin{array} { r l r } & { } & { h ( t ) = A _ { + } \left[ \displaystyle \frac { \pi f _ { \mathrm { g w } } ( t ) } { c } \right] ^ { 2 / 3 } \cos [ \Phi ( f _ { \mathrm { g w } } ( t ) ) + \Phi _ { 0 } ] ~ } \\ & { } & { + A _ { \times } \left[ \displaystyle \frac { \pi f _ { \mathrm { g w } } ( t ) } { c } \right] ^ { 2 / 3 } \sin [ \Phi ( f _ { \mathrm { g w } } ( t ) ) + \Phi _ { 0 } ] , } \end{array}
$$

55 Explicit expressions for $\Phi ( f _ { \mathrm { g w } } )$ and $f _ { \mathrm { g w } } ( t )$ up to 2PN were given in eq.(5.273)，and in eq.(5.270)or (5.272).

where,as discussed in Section 5.6.3, $\Phi ( f _ { \mathrm { g w } } )$ and $\boldsymbol { f } _ { \mathrm { g w } } ( t )$ are known up to 3.5PN order.55 We have esplicitly displayed the arbitrary constant $\Phi _ { 0 }$ in the phase,equivalent to the arbitrary constant $\omega _ { 0 }$ in eq. (5.265),and we have defined

$$
\begin{array} { l } { \displaystyle { A _ { + } = \frac { 4 } { r } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } F _ { + } ( \theta , \phi ) \frac { 1 + \cos ^ { 2 } \iota } { 2 } } } \\ { \displaystyle { A _ { \times } = \frac { 4 } { r } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } F _ { \times } ( \theta , \phi ) \cos { \iota } . } } \end{array}
$$

Writing $A _ { + } = A \cos \alpha$ and $A _ { \times } { } = A \sin \alpha$ ,with $A = ( A _ { + } ^ { 2 } + A _ { \times } ^ { 2 } ) ^ { 1 / 2 }$ and tan $\alpha = { A _ { \times } } / { A _ { + } }$ ,we can rewrite this as

$$
h ( t ) = A \left[ \frac { \pi f _ { \mathrm { g w } } ( t ) } { c } \right] ^ { 2 / 3 } \cos [ \Phi ( f _ { \mathrm { g w } } ( t ) ) + \varphi ] ,
$$

56Recail also from Section 4.1.4 that, for binaries at cosmological distances, i.e.at a non-negligible redshift $z$ ，the masses $m _ { 1 }$ and $m _ { 2 }$ must be multiplied by $( 1 + z )$ ，and the distance $r$ must be replaced by the luminosity distance $d _ { L } ( z )$

with $\varphi = \Phi _ { 0 } - \alpha$ .56 Thus,in the waveform enter the distance $r$ to the source,its location,specified by the angles $( \theta , \phi )$ which appear in the pattern functions,the orientation of the orbit with respect to the line of sight (two angle,one of which is $\iota$ ,and the other identifies the axes with respect to which the plus and cross polarizations are defned),the reference time $t _ { * }$ at which the signal enters in the detector bandwidth (which appears through $\Phi ( t )$ and $\bar { f } _ { \mathrm { g w } } ( t )$ ),the constant phase $\varphi$ ,the masses of the two stars,and in principle also their spins (which we neglected in eq.(5.273)).So,in total,we have 15 parameters.57 However,a number of simplifications are possible,as we discuss in the next subsection.

# 7.7.1Elimination of extrinsic variables

The variables that can be elimipated from the parameter space are generically called extrinsic.First,we observe that all possible shifts in time of the signal can be obtained at once with a single Fourier transform. Consider in fact the scalar product $( h ( \theta , t _ { * } ) | s )$ between the output $s ( t )$ of the detector and the template $h ( t ; \theta , t _ { * } )$ where,from the parameters $\theta ^ { i }$ ,we singled out explicitly the arrival time $t _ { * }$ ,defined as the time when the hypothetical signal enters into the interferometer bandwidth,say at $f _ { \mathrm { g w } } = 1 0 ~ \mathrm { H z }$ .The waveform $\hslash ( t ; \theta , t _ { * } )$ is obtained from $h ( t ; \theta , t _ { * } = 0 )$ with a time translation,so if we denote by $\tilde { h } ( f ; \theta )$ the Fourier transform of $h ( t ; \theta , t _ { * } )$ at $t _ { * } = 0$ ,the Fourier transform of $h ( t ; \theta , t _ { * } )$ at $t _ { * }$ generic is simply $\tilde { h } ( f ; \theta ) e ^ { i 2 \pi f t _ { * } }$ ．Thus,from the definition (7.46)of the scalar product,we have

$$
( h ( \theta , t _ { * } ) | s ) = 4 \mathrm { R e } \int _ { 0 } ^ { \infty } d f \frac { \tilde { h } ^ { * } ( f ; \theta ) \tilde { s } ( f ) } { S _ { n } ( f ) } e ^ { i 2 \pi f t _ { * } } ,
$$

which is just the Fourier transform of $\tilde { h } ^ { * } ( f ; \theta ) \tilde { s } ( f ) / S _ { n } ( f )$ Thus,performing a single FFT we can immediately locate the value of $t _ { * }$ which gives the highest signal-to-noise ratio. This is of course of great practical importance.Typically we qan expect that,to perform efficiently the matched filtering,the maximum mismatch in arrival time that we can tolerate between the real signal and our template could be,say,of order $\mathrm { 3 \ m s }$ If one should analyze one year of data $( 3 \times 1 0 ^ { 7 } \mathrm { s } )$ computing a different scalar product every $3 \mathrm { m s }$ ,for each value of $\theta$ one should perform $1 0 ^ { 1 0 }$ times the computation of the scalar product $h ( t ; \theta , t _ { * } )$ ,while we see that just a single FFT does the job.58Thus,the arrival time $t _ { * }$ is not really part of the parameter space that must be searched. Figure 7.14 shows the result of a simulation in which the signal corresponding to the coalescence of two BHs,each with a mass of $1 0 M _ { \odot }$ ，ata distance of $1 5 0 ~ \mathrm { M p c }$ ,is injected into the noise of the VIRGO detector. Performing the Fourier transform,we see that we have a spike in correspondence withthe time at which this signal has been injected (in the figure, $t _ { * } = 1$ ， in arbitrary units).

Two more parameters that appear in eq. (7.167),which can be eliminated analytically from the matched fitering procedure,are the amplitude $A$ and the phase $\varphi$ of the signalWe already saw in Section 7.3 that the optimal filter is defined modulo an arbitrary constant,so the overall value of the amplitude $A$ does not enter when we search for the template that maximizes the signal-to-noise ratio. The maximization of the SNR with respect to $\varphi$ can be performed analytically,writing the template (7.170) in the form

$$
h ( t ) = h _ { c } ( t ) \cos \varphi + h _ { s } ( t ) \sin \varphi .
$$

If $s ( t )$ is the detector output,after maximization of the log-likelihood function over the amplitude $A$ ,accordinig to eq.(7.7O) we want to further maximize

$$
\begin{array} { l } { { 2 \log \Lambda = { \frac { ( h | s ) ^ { 2 } } { ( h | h ) } } } } \\ { { \qquad = { \frac { [ ( h _ { c } | s ) + ( h _ { s } | s ) \tan \varphi ] ^ { 2 } } { ( h _ { c } | h _ { c } ) + ( h _ { s } | h _ { s } ) \tan ^ { 2 } \varphi + 2 ( h _ { c } | h _ { s } ) \tan \varphi } } . } } \end{array}
$$

58More precisely,if we have a time series with $N$ samples,computing the integral which defines the scalar product has a computational cost $O ( N )$ ，andif one had to repeat it for all possible arrival times,the overall cost would be $O ( N ^ { 2 } )$ ．With a single FFT,instead, the computational cost is $O ( N \log N )$

![](images/d15dad9b38c198d010ede4ff48365f2e46ba960a4d96c13f90691db390bfe7db.jpg)  
Fig.7.14 The result of a simulation in which the signal due to a BH-BH coalescence,each with a mass of $1 0 M _ { \odot }$ ,at a distance of $1 5 0 ~ \mathrm { M p c }$ ,is injected into the noise of the VIRGO detector.The arrival time is located from the position of the spike in the Fourier transform (7.171),which here is at $t _ { * } = 1$ (Courtesy of A. Vicere.)

This expression is easily maximized analytically with respect to $\tan \varphi$ The result is simpler if we introduce two new templates

$$
\begin{array} { r } { h _ { p } = h _ { c } \cos \phi _ { p } + h _ { s } \sin \phi _ { p } , } \\ { h _ { q } = h _ { c } \cos \phi _ { q } + h _ { s } \sin \phi _ { q } , } \end{array}
$$

where the angles $\phi _ { p }$ and $\phi _ { q }$ are chosen so that $h _ { p }$ and $h _ { q }$ satisfy $\left( h _ { p } | h _ { q } \right) =$ $\boldsymbol { 0 }$ i.e.they are orthogonal with respect to the scalar product $( ~ | ~ )$ In terms of these orthogonal templates the likelihood function,after performing the maximization over the amplitude $A$ and over the phase $p$ takes the simple form

$$
2 \log \Lambda = \frac { ( h _ { p } | s ) ^ { 2 } } { ( h _ { p } | h _ { p } ) } + \frac { ( h _ { q } | s ) ^ { 2 } } { ( h _ { q } | h _ { q } ) } .
$$

Therefore,the maximization with respect to the remaining variables is equivalent to maximizing the sum in quadrature of the outputs of two matched filters.In the absence of signal, the signal-to-noise ratio $\rho$ is therefore a random variable which folows the Rayleigh distributiol (7.87),while in the presence of signal it is a non-central $\chi ^ { 2 }$ distribution with two degrees of freedomIndeed，we see in Fig.7.15 that,in th simulation of Fig. 7.14, $\rho$ follows a Rayleigh distribution (except. course,for the presence of the single spike with $S / N = 8$ at $t _ { * } = 1$ ).59

![](images/3cca96dea724021eb0b50f38cfd0ae0f91184b29ed300ad1219dd16da6caadec.jpg)  
Fig.7.15 The distribution of the signal-to-noise ratio,in the simulation of Fig. 7.14.(Courtesy of A. Vicere.)

59It should also be observed that，for coalescing binaries, non-Gaussian noise should be much less important than for short bursts,since it should be much easier to have an impulsive disturbance that simulates a short burst,rather than a noise that lasts for about 15 minutes,simulating for all this time the behavior of a chirping signal.

# 7.7.2The sight distance to coalescing binaries

The Fourier transform of the chirp amplitude,to Newtonian order, has been computed in Problem $\sharp . 1$ ，while the result in the restricted P approximation,up to 2PN order,is given in eqs. (5.274) and (5.275) Then we find,for the Fourier transform of $h ( t ) = h _ { + } F _ { + } + h _ { \times } F _ { \times }$

$$
\tilde { h } ( f ) = \left( \frac { 5 } { 6 } \right) ^ { 1 / 2 } \frac { 1 } { 2 \pi ^ { 2 / 3 } } \frac { c } { r } \left( \frac { G M _ { c } } { c ^ { 3 } } \right) ^ { 5 / 6 } f ^ { - 7 / 6 } e ^ { i \Psi } Q ( \theta , \phi ; \iota ) ,
$$

where

$$
Q ( \theta , \phi ; \iota ) = F _ { + } ( \theta , \phi ) \frac { \mathbb { I } + \cos ^ { 2 } \iota } { 2 } + i F _ { \times } ( \theta , \phi ) \cos \iota .
$$

60Actually,te expression thatweused for $h _ { + }$ and $h _ { \times }$ assumes a given choice of the axes with respect to which the plus and cross polarizations are defined, which is related to the orientation of the orbit,see page 296．Since a priori we do not know the orientation of the orbit,this will in general differ by an unknown angle $\psi$ from the definition of axes that the experimenter uses to define the pattern functions.Correspondingly, the expressions for $h _ { + }$ and $h _ { \times }$ must be rotated as in eqs.(7.24) and (7.25)，so the function $Q$ is actually $Q ( \theta , \phi ; \iota , \psi )$ .However this $\psi$ dependence,being an orthogonal transformation,does not affect that computation of $\langle | Q | ^ { 2 } \rangle$ performed below.

The phase $\Psi$ is just the quantity denoted $\Psi _ { + }$ in eq. (5.275),and th relative factor $i$ between the two terms in $Q$ is due to the fact thar $\Psi _ { \times } = \Psi _ { + } + ( \pi / 2 )$ .60 Plugging this expression into eq. (7.51)，we ca write the signal-to-noise ratio for a coalescing binary as

$$
\left( \frac { S } { N } \right) ^ { 2 } = \frac { 5 } { 6 } \frac { 1 } { \pi ^ { 4 / 3 } } \frac { c ^ { 2 } } { r ^ { 2 } } \left( \frac { G M _ { c } } { c ^ { 3 } } \right) ^ { 5 / 3 } | Q ( \theta , \phi ; \iota ) | ^ { 2 } \int _ { 0 } ^ { f _ { \mathrm { m a x } } } d f \frac { f ^ { - 7 / 3 } } { S _ { n } ( f ) } ,
$$

where $f _ { \mathrm { m a x } }$ is the value of the GW frequency when the inspiral phas terminates and the two stars merge. An estimate of $f _ { \mathrm { m a x } }$ is $f _ { \mathrm { m a x } } =$ $2 ( f _ { s } ) _ { \mathrm { I S C O } }$ ,where $ { ( f _ { s } ) _ { \mathrm { I S C O } } }$ given in eq.(4.39),and the factor of 2 is valid as long as the emission is dominated by quadrupole radiation. For wave coming from optimal direction (e.g. $F _ { + } = 1$ and $F _ { \times } = 0$ ,and with optimal value of the inclination of the orbit $\cos \iota = 1 $ ），thefunc tion $Q ( \theta , \phi ; \iota ) \ : = \ : 1$ .However,a more appropriate reference value fol $| Q ( \theta , \phi ; \iota ) | ^ { 2 }$ is given by its average over all possible directions and incli nations. Using $\left. F _ { + } ^ { 2 } \right. = \left. F _ { \times } ^ { 2 } \right. = 1 / 5$ for interferometers (see Table 7.1) we get $\langle | Q ( \theta , \phi ; \iota ) | ^ { 2 } \rangle = ( 1 / 5 ) g ( \iota )$ ，where $g ( \iota )$ was defined in eq. (3.338 and its average over the inclination $\iota$ is $4 / 5$ ,see eq. (4.10). Therefore

$$
\langle | Q ( \theta , \phi ; \iota ) | ^ { 2 } \rangle ^ { 1 / 2 } = \frac { 2 } { 5 } ,
$$

where here $\langle \ldots \rangle$ denotes the average over the angles and over the incli nation. Then we rewrite eq.(7.179) as

$$
\begin{array} { l } { { \displaystyle \frac { S } { N } = \frac { 2 } { 5 } \left( \frac { 5 } { 6 } \right) ^ { 1 / 2 } \frac { 1 } { \pi ^ { 2 / 3 } } \frac { c } { r } \left( \frac { G M _ { c } } { c ^ { 3 } } \right) ^ { 5 / 6 } \frac { \langle | Q ( \theta , \phi ; \iota ) | ^ { 2 } \rangle ^ { 1 / 2 } } { ( 2 / 5 ) } } } \\ { { \displaystyle \qquad \times \left[ \int _ { 0 } ^ { f _ { \mathrm { m a x } } } d f \frac { f ^ { - 7 / 3 } } { S _ { n } ( f ) } \right] ^ { 1 / 2 } . } } \end{array}
$$

This relation can be inverted to give the sight distance $d _ { \mathrm { s i g h t } }$ ,i.e.the maximum distance $r$ at which we can see a binary coalescence,once we have chosen a given threshold for $S / N$ 61 assuming an average direction and inclination,

<table><tr><td>2-5 1/2 GMc 5/6 C dsight = π2/3 </td><td>ffmax f-7/371/2 df (S/N)-1 Sn J0</td></tr></table>

We will see in Chapter 9 the numerical values that can be obtained for $d _ { \mathrm { s i g h t } }$ at existing and advanced interferometers.

It is instructive to verify from these expressions that,in order of magnitude,for a coalescing binary the matched filtering procedure gives a $\mathrm { g a i n } \sim \mathcal { N } _ { c } ^ { 1 / 2 }$ .To this end, we assume that $S _ { n }$ has a constant value $S _ { 0 }$ between a minimum frequency $f _ { 0 }$ and $f _ { \mathrm { m a x } }$ ,while it is essentially infinite for $f < f _ { 0 }$ .Then,neglecting all numerical factors (and using for simplicity units $c = 1$ ,and the notation $M = G M _ { c } / c ^ { 3 }$ ),we can perform the integral in eq. (7.181),and we get

$$
\frac { S } { N } \sim \frac { 1 } { r } M ^ { 5 / 6 } S _ { 0 } ^ { - 1 / 2 } f _ { 0 } ^ { - 4 / 3 } .
$$

From eqs.(7.167) and (7.168) we see that the GW amplitude is of order

$$
h _ { 0 } \sim { \frac { 1 } { r } } f _ { 0 } ^ { 2 / 3 } M ^ { 5 / 3 } ,
$$

while,from eq. (4.23),the number of cycles spent in the interferometer bandwidth is

$$
\mathcal { N } _ { c } \sim M ^ { - 5 / 3 } f _ { 0 } ^ { - 5 / 3 } .
$$

Using eq.(7.184) to eliminate $r$ from eq. (7.183)，and eq.(7.185) to eliminate $M$ ,we get

$$
\frac { S } { N } \sim \frac { h _ { 0 } } { ( f _ { 0 } S _ { 0 } ) ^ { 1 / 2 } } \ : \mathcal { N } _ { c } ^ { 1 / 2 } ,
$$

which shows indeed that,in order of magnitude, the signal-to-noise ratio (in amplitude) is larger bya factor $\mathcal { N } _ { c } ^ { 1 7 2 }$ than for a burst with a characteristic frequency $f _ { 0 }$ (compare with eq.(7.107) with $\tau _ { g } = 1 / f _ { 0 }$ and fmax = fo). Of course,a more precise estimate requires the real form of $S _ { n } ( f )$ ,as well as the exact computation of the integral in eq. (7.181). This shows explicitly how the matched filtering procedure allows us to dig deeply into the noise floor,as we discussed already on page 344. Consider in fact the situation in which,after tracking the signal by $\mathcal { N } _ { c } \gg 1 $ cycles， we finally get $S / N$ of order one, so we begin to see the signal. According to eq. (7.186)， this means that $h _ { 0 } / ( f _ { 0 } \bar { S } _ { 0 } ) ^ { 1 / 2 }$ was of order $1 / \mathcal { N } _ { c } ^ { 1 / 2 }$ However, $h _ { 0 } / ( f _ { 0 } S _ { 0 } ) ^ { 1 / 2 }$ is the “instantaneous” value of the signal-to-noise ratio,i.e. the value of $S / N$ over a single cycle.

6l Recall however from page 359 that the signal can combine with the noise either in a constructive or in a destructive way,so the output $\rho$ of the interferometer is a random variable whose average is $S / N$ and which follows,in the presence of signal,a non-central $\chi ^ { 2 }$ distribution with two degrees of freedom. Therefore,at any distance $\mathcal { T }$ there isa probability of missed detection,and the fact that a source is at $r < d _ { \mathrm { s i g h t } }$ does not mean that it will be certainly detected.Conversely,there is also a nonzero probability that the signal from a source at $r > d _ { \mathrm { s i g h t } }$ combines with the noise so that its $\mathbf { \bar { \mathbf { \xi } } } _ { S / N }$ raises above the threshold.

Therefore,the integrated signal-to-noise ratio provided by the matchel filtering procedure can be of brder one or larger,even when the instan taneous signal is deeply buried into the noise.

Finally,an important issue is the precision that can be obtained in th reconstruction of the source parameters. In particular the chirp mass $M _ { c }$ ,that appears in the phase of the waveform, can be estimated ver precisely, since the phase can be followed accurately for $\textstyle { \mathcal { N } } _ { c }$ cycles. Thus any mismatch $\Delta M _ { c }$ between the true value of the source and the value used in our template will beamplifed by a factor $\mathcal { N } _ { c }$ ，and we could expect that

$$
\frac { \Delta M _ { c } } { M _ { c } } \sim \frac { 1 } { \mathcal { N } _ { c } } .
$$

62The precise computation of the errors on the parameters can be done using the explicit expression of the waveform to evaluate the Fisher information matrix defined in eq.(7.74),and then we can compute the errors on the parameters as in eq.(7.75).Using the waveform with the post-Newtonian corrections to the phase and assuming a detection with $S / N ~ = ~ 1 0 $ one finds that,if one knew that the spins of the star are negligible,then $M _ { c }$ could indeed be measured with a precision of $0 . 0 1 { - } 0 . 1 \%$ ，while the reduced mass $\mu$ ，which enters in the post-Newtonian corrections,could be measured to $1 \%$ However,one in general has no a priori information on the spins,and the measurements of masses and spins happen to be strongly correlated．This degrades the accuracy on the mass reconstruction,so one finally obtains $\Delta M _ { c } / M _ { c } \sim 0 . 1 - 1 \%$ (which, however, is still a quite remarkable accuracy and $\Delta \mu / \mu \sim 1 0 - 1 5 \%$ for NS-NS and NS-BH binaries,or $\Delta \mu / \mu \sim 5 0 \%$ for BH-BH binaries with typical BH masses of order $1 0 M _ { \odot }$ Observe that,the larger the mass of the stars,the smaller is the number of cycles in the detector bandwidth,since the coalescence takes place earlier,see eq.(4.39),so the precision in the reconstruction of the parameters is less good. See Cutler and Flanagan (1994) for details.

Given that at a ground-based interferometer $\mathcal { N } _ { c }$ can be of order $1 0 ^ { 3 } – 1 0 ^ { 4 }$ see eq. (4.23),this would give a rather remarkable accuracy $\Delta M _ { c } / M _ { c } \sim$ 10-4-10-3. As for the reduced massμ,it appears in the 1PN corrections to the phase, which are smaler by a factor $O ( v ^ { 2 } / c ^ { 2 } )$ than the leading term,so it can be measured less precisely.62

# 7.8Stochastic backgrounds

In 1965 Penzias and Wilson discovered that the Universe is permeated by the Cosmic Microwave Background (CMB) electromagnetic radiation. This radiation is a relic of the early Universe,and the microwave photons that compose it decoupled from the primordial plasma about $3 \times 1 0 ^ { 5 }$ years after the Big Bang,and since then they have been propagating essentially freely.This discovery，providing direct evidence for the Big Bang,was one of the most significant in the history of cosmology.

Since then,the CMB has been subject to deep investigations.We now know that its spectrum is a perfect black-body (in fact,the most perfect black-body spectrum existinglin nature). This background is,to a first approximation，isotropic.The observation by the COBE satellite of temperature fluctuations over the sky,at the level $\Delta T / T \sim 1 0 ^ { - 5 }$ ,has been one of the most important discoveries in cosmology in the last decades,and the detailed investigation of the multipole moments of these anisotropies by COBE and various other experiments,and particularly by WMAP,has opened up the field of precision cosmology.

There are good reasons to expect that the Universe is permeated also by a stochastic background df GWs generated in the early Universe. Furthermore,a stochastic background of GWs can also emerge from the incoherent superposition of a large number of astrophysical sources, too weak to be detected separately,and such that the number of sources that contribute to each frequency bin is much larger than one.

The mechanisms that can lead to the production of stochastic Gw backgrounds in cosmology and in astrophysics willbe examined in detail in Vol.2. Here we discuss how to characterize such a background in general,and what are the optimal strategies for its detection.

# 7.8.1 Characterization of stochastic backgrounds

Using the plane wave expansion (1.58), wecan write

$$
h _ { i j } ( t , \mathbf { x } ) = \sum _ { A = + , \times } \int _ { - \infty } ^ { \infty } d f \int d ^ { 2 } \hat { \mathbf { n } } \tilde { h } _ { A } ( f , \hat { \mathbf { n } } ) e _ { i j } ^ { A } ( \hat { \mathbf { n } } ) e ^ { - 2 \pi i f ( t - \hat { \mathbf { n } } \cdot \mathbf { x } / c ) } .
$$

We work in the TT gauge, so $h _ { i } ^ { i } = 0$ and $\partial ^ { j } h _ { i j } = 0$ The tensors $e _ { i j } ^ { A } ( \hat { \mathbf { n } } )$ are given in eq.(1.54). A stochastic background is a superposition of waves with all possible propagation directions $\hat { \bf n }$ ，therefore the indices $i , j$ above take the values $1 , 2 , 3$ ,contrary to the case of the GWs emitted from a single far source,where we could label the GW in the TT gauge as $h _ { a b }$ with $a , b .$ ,taking the values $1 , 2$ and labeling the two directions in tle transverse plane.A stochastic background is defined by the fact that the amplitudes $\tilde { h } _ { A } ( f , \hat { \mathbf { n } } )$ arerandom variables,characterized statistically by their ensemble averages.63

We will make the following assumptions on stochastic backgrounds of GWs.

· The background is stationary. This means that all correlators depend only on time differences,and not on the absolute values of time.So,for instance,the two-point correlator $\left. h _ { A } ( t ) h _ { A ^ { \prime } } ( t ^ { \prime } ) \right.$ can depend only on $t - t ^ { \prime }$ ，and not separately on $t$ and $t ^ { \prime }$ .In Fourier space,this means that $\langle \tilde { h } _ { A } ^ { * } ( f ) \tilde { h } _ { A ^ { \prime } } ( f ^ { \prime } ) \rangle$ must be proportional to $\delta ( f - f ^ { \prime } )$ .This assumption is certainly justified.For a background created in cosmological epochs,the typical time-scale on which it can change substantially is of the order of the age of the Universe (for instance,its spectrum changes because it is redshifted).During the duration of the experiment,which is at most a few years, it is very difficult to imagine that the properties of the background could change appreciably.64

·The background is Gaussian. This means that all $N$ -point correlators are reduced to sum and products of the two-point correlator $\left. h _ { A } ( t ) h _ { A ^ { \prime } } ( t ^ { \prime } ) \right.$ (and of the vacuum expectation value $\left. h _ { A } \right.$ that however,as we have seen,can be set to zero).Gaussianity is rooted in the central limit theorem,that states that the sum of a large number of independent events produces a Gaussian stochastic process,whatever the probabillity distribution of the individual events. This assumption is therefore expected to hold to a very good accuracy for cosmological backgrounds.It would not hold for astrophysical backgrounds,if the number of sources that contribute is not that large,and we are on the verge of distinguishing the individual contributions.In this case,further information can be extracted from the higher-poipt correlators.

63An ensemble average is the average over many copies of the system.Our system is in this case the Universe and we do not have many copies of it! Of course,the ergodic assumptions must be used here,and the ensemble average is replaced bya temporal average, compare with Note 3 on page 337.

·The stochastic background is isotropic.Experience with CMB indicates that the early Universe was highly isotropic and,for the photons,temperature fluctuations across the sky are at the level $\Delta T / T \sim 1 0 ^ { - 5 }$ ．It is reasonable to expect that a stochastic background of GWs of cosmological willalso be in a first approximation

64Stationarity also implies that (hA(t)) isa constant so,even if it were nonzero,it would just contribute to the vacuum energy density.As far as we are interested in GWs,that is in the time-dependent part,we can therefore set $\langle h _ { A } \rangle = 0$

isotropic. Of course, after|a first detection of a GW background it will be extremely interesting to investigate its anisotropies and therefore to give up this assumption. In particular,in a cosmo logical background we must expect a dipole term, dominated by the Earth motion in the rest frame of the CMB,while higher multipoles could give extremely interesting information on the early Universe.

We might have to give up|completely the assumption of isotropy when we study stochastic backgrounds of astrophysical origin. In particular a background df galactic origin will not be isotropic. but rather it will be more intense when we look in the direction of the galactic plane, just as the electromagnetic background due to galactic sources gives its characteristic appearance to the Milky Way.We will in fact discuss in Vol. 2 an example of this type, the background created by galactic white dwarf binaries.

Waves coming from diferent directions should be uncorrelated, so $\langle \tilde { h } _ { A } ^ { * } ( f , \hat { \mathbf { n } } ) \tilde { h } _ { A ^ { \prime } } ( \breve { f } ^ { \prime } , \hat { \mathbf { n } } ^ { \prime } ) \rangle$ should be proportional to a Dirac delta over the two-sphere,defined as

$$
\delta ^ { 2 } ( \hat { \bf n } , \hat { \bf n } ^ { \prime } ) = \delta ( \phi - \phi ^ { \prime } ) \delta ( \cos \theta - \cos \theta ^ { \prime } ) ,
$$

where $( \theta , \phi )$ are the polar angles that define $\hat { \bf n }$ Isotropy implies that the proportionality cqnstant must be independent of $\hat { \mathbf { n } }$

· Finally,we assume that the background is unpolarized,as it is natural both in a cosmological context and if it is the result of the superposition of many different astrophysical sources. This means that $\langle \tilde { h } _ { A } ^ { * } ( f , \hat { \mathbf { n } } ) \tilde { h } _ { A ^ { \prime } } ( f ^ { \prime } , \tilde { \mathbf { n } } ^ { \prime } ) \rangle$ must be proportional to $\delta _ { A A ^ { \prime } }$ and the proportionality coefficient must be independent of the polarization index $A$

Under these assumptions, a stochastic background of GWs is uniquely characterized by a single function $S _ { h } ( f )$ ，defined by

$$
\langle \widetilde { h } _ { A } ^ { * } ( f , \hat { \bf n } ) \widetilde { h } _ { A ^ { \prime } } ( f ^ { \prime } , \hat { \bf n } ^ { \prime } ) \rangle = \delta ( f - f ^ { \prime } ) \frac { \delta ^ { 2 } ( \hat { \bf n } , \hat { \bf n } ^ { \prime } ) } { 4 \pi } \delta _ { A A ^ { \prime } } \frac { 1 } { 2 } S _ { h } ( f ) .
$$

The function $S _ { h } ( f )$ is called the βpectral density of the stochastic background，in analogy with the spectral density of the noise defined in Section 7.1. Just as for the noise spectral density, we use the convention that $S _ { h } ( f )$ is single-sided.It has dimensions $\mathrm { H z ^ { - 1 } }$ and satisfies $S _ { h } ( f ) = S _ { h } ( - f )$ . The factor $1 / ( 4 \pi )$ in eq. (7.190) is a choice of normal ization such that

$$
\int d ^ { 2 } { \hat { \mathbf { n } } } d ^ { 2 } { \hat { \mathbf { n } } ^ { \prime } } \langle \tilde { h } _ { A } ^ { * } ( f , { \hat { \mathbf { n } } } ) \tilde { h } _ { A ^ { \prime } } ( f ^ { \prime } , { \hat { \mathbf { n } } ^ { \prime } } ) \rangle = \delta ( f - f ^ { \prime } ) \delta _ { A A ^ { \prime } } \frac { 1 } { 2 } S _ { h } ( f ) .
$$

where, as usual, $d ^ { 2 } { \hat { \mathbf { n } } } = \ d \cos \theta d \phi$ .We see that the factor $1 / 2$ in the definition of $S _ { h } ( f )$ has been inserted so that $S _ { h } ( f )$ is normalized in the same way as the single-sided spectral density of the noise, see eq. (7.6).

$\sum _ { A } e _ { i j } ^ { A } e _ { i j } ^ { A } = 4$ which folows fromthe normalization (1.55)of the pplarization tensor $e _ { i j } ^ { A }$ ，we get

$$
\langle h _ { i j } ( t ) h ^ { i j } ( t ) \rangle = 4 \int _ { 0 } ^ { \infty } d f S _ { h } ( f ) .
$$

The sum over $i , j$ is understood,and $h _ { i j } ( t ) = h _ { i j } ( t , \mathbf { x } = 0 )$ . The spectral density of the signal, $S _ { h } ( f )$ ,is the quantity that allows us to perform a direct comparison with the noise in a detector,which is characterized by $S _ { n } ( f )$ .However,to have a physical understanding it is much more convenient to think in terms of the energy density carried by the stochastic background.According to eq. (1.135),this is related to $h _ { i j }$ by

$$
\rho _ { \mathrm { g w } } = \frac { c ^ { 2 } } { 3 2 \pi G } \langle \dot { h } _ { i j } \dot { h } ^ { i j } \rangle .
$$

In cosmology there is a very natural unit of energy density， that is, the energy density needed for closing the Universe. This critical energy density is

$$
\rho _ { c } = \frac { 3 c ^ { 2 } H _ { 0 } ^ { 2 } } { 8 \pi G } ,
$$

where $H _ { 0 }$ is the present value of theHubble expansion rate. As we mentioned on page 194,the value of $H _ { 0 }$ is usually written as $H _ { 0 } =$ $h _ { 0 } { \times } 1 0 0 \mathrm { k m s ^ { - 1 } M p c ^ { - 1 } }$ ,where $h _ { 0 }$ parametrizes the existing experimental uncertainty and is called the normalized Hubble expansion rate. The most recent determinations give $h _ { 0 } = \stackrel { \vert } { 0 . 7 3 } ( 3 )$ .Numerically,

$$
\rho _ { c } \simeq 1 . 6 8 8 \times 1 0 ^ { - 8 } h _ { 0 } ^ { 2 } \mathrm { e r g c m } ^ { - 3 } .
$$

Normalizing $\rho _ { \tt g w }$ to $\rho _ { c }$ ,the intensity ofa stochastic background of gravitational waves can be characterized by the dimensionless quantity

$$
\Omega _ { \mathrm { g w } } \equiv \frac { \rho _ { \mathrm { g w } } ^ { \dagger } } { \rho _ { c } } .
$$

Using eqs. (7.192) and (7.193)，the energy density can be written as an integral over $d \log f$ of some spectral density, that we denote by65 $d \rho _ { \mathrm { g w } } / d \log f$ ，

$$
\rho _ { \mathrm { g w } } \equiv \int _ { f = 0 } ^ { f = \infty } d ( \log f ) \ \frac { d \rho _ { \mathrm { g w } } } { d \log f } .
$$

We also define

$$
\overline { { \Omega _ { \mathrm { g w } } ( f ) \equiv \frac { 1 } { \rho _ { c } } \bigg \vert \frac { d \rho _ { \mathrm { g w } } } { d \log f } } } ,
$$

$\boldsymbol { \mathrm { s } } 0 \Omega _ { \mathrm { g w } }$ in eq. (7.196) is related to $\Omega _ { \mathrm { g w } } ( f )$ by66

$$
\Omega _ { \mathrm { g w } } = \int _ { f = 0 } ^ { f = \infty } d ( \log f ) \Omega _ { \mathrm { g w } } ( f ) .
$$

65Thereis a slightabuseof notation here.Of course $\rho _ { \mathtt { g w } }$ ,on the left-hand side of eq.(7.197),is independent of the frequency,so its derivative with respect to $f$ orto $\log f$ ,vanishes.On the righthand side, $d \rho _ { \mathrm { g w } } / d \log f$ is not the derivative of $\rho _ { \tt E W }$ with respect to $\log f ,$ but just a notation for the spectral density of $\rho _ { \mathrm { g w } }$ ,which stresses that it is the energy density contained in a logarithmic interval of frequency.

66ereagain thereisalightambigu ity in the notation,because we use the same symbol $\Omega _ { \tt G W }$ for the normalized energy density,on the left-hand side of eq.(7.199),and for its spectral density, on the right-hand side.This notation is however standard in the GW literature, and we will conform to it.

67Unfortunately，we sometime use ho also to denote a GW amplitude.Since the reduced Hubble constant $h _ { 0 }$ will onlyappearinthecombination $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } }$ no confusion is possible.

The fact that we consider the energy per unit logarithmic interval frequency, ${ d \rho _ { \mathrm { g w } } } / { d \log f }$ ,rather than $d \rho _ { \mathrm { g w } } / d f$ , is useful because in th way $\Omega _ { \mathrm { g w } } ( f )$ is dimensionless.

Even if the experimental error on the Hubble expansion rate is b coming smaller and smaller (just a few years ago values of $h _ { 0 }$ betwe 0.4 and 1 where considered possible)，still it is not very convenient normalize $\rho _ { \mathrm { g w } }$ to a quantity, $\rho _ { c }$ ， which is uncertain: this uncertain would appear in all the subsequent formulas,although it has nothingi do with the uncertainties on|the GW background itself. Therefore,om rather characterizes the stochastic GW background with the quantin $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f )$ ,which is independent of $h _ { 0 }$ .67

We now compute the relation between $S _ { h } ( f )$ and $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f )$ As di cussed in Section 1.4.3,the brackets in eq.(7.i93) denote a time averag However (under the ergodic assumption,see Notes 3and 63), this is jus the ensemble average used above.We can then substitute the plane wav expansion (7.188) into eq. (7.193),and compute the ensemble averag using eq. (7.190). The result is

$$
\rho _ { \mathrm { g w } } = \frac { c ^ { 2 } } { 8 \pi G } \int _ { f = 0 } ^ { f = \infty } d ( \log f ) \ f ( 2 \pi f ) ^ { 2 } S _ { h } ( f ) .
$$

Comparing with the definition (7.197) we get

$$
\frac { d \rho _ { \mathrm { g w } } } { d \log f } = \frac { \pi c ^ { 2 } } { 2 G } f ^ { 3 } S _ { h } ( f ) ,
$$

and

$$
\overline { { { \Omega _ { \mathrm { g w } } ( f ) = \frac { 4 \pi ^ { 2 } } { 3 H _ { 0 } ^ { 2 } } f ^ { 3 } S _ { h } ( f ) . } } }
$$

Finally,it is interesting to express $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f )$ in terms of the number $a$ gravitons per cell of the phase space, $n ( \mathbf { x } , \mathbf { k } )$ .For an isotropic stochas tic background n(x,k) = nf depends only on the frequency (whichi related to the momentum k by |k| = hw/c= 2πhf/c),and not on the direction k.Then,writing d3k = |k/²d|k|dΩ→ 4π(2πh/c)³f²df, an df = fdlog f,and considering that a graviton of frequency f carries an energy $\hbar \omega = \hbar ( 2 \pi f )$ ,we have

$$
\begin{array} { l } { { \displaystyle \rho _ { \mathrm { g w } } = 2 \int \frac { d ^ { 3 } k } { ( 2 \pi \hbar ) ^ { 3 } } \hbar ( 2 \pi f ) n _ { f } } } \\ { { \displaystyle \quad = \frac { 1 6 \pi ^ { 2 } \hbar } { c ^ { 3 } } \int _ { 0 } ^ { \infty } d ( \log f ) f ^ { 4 } n _ { f } , } } \end{array}
$$

where the factor of 2in front of the integral is due to the two helicity states of the graviton. Therefore

$$
\frac { d \rho _ { \mathrm { g w } } } { d \log { f } } = \frac { 1 6 \pi ^ { 2 } \hbar } { c ^ { 3 } } n _ { f } f ^ { 4 } ,
$$

and

$$
h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f ) \simeq 3 . 6 \left( \frac { n _ { f } } { 1 0 ^ { 3 7 } } \right) \left( \frac { f } { \mathrm { 1 k H z } } \right) ^ { 4 } .
$$

As we will see in Vol. 2,this equation is useful in particular when one computes the production of a stochastic background of GWs due to amplification of vacuum fuctuations,since this computation gives directly $n _ { f }$ .

# 7.8.2 SNR for single detectors

The comparison of eqs.(7.6) and (7.191) makes it clear that an isotropic stochastic background of GWs is seen in a detector as an additional source of noise. This poses an important conceptual problem in the identification of a stochastic GW background. In practice what wil happen is that,after a careful modeling of the detector and of its noise sources,one would expect to have a certain value of the spectral density of the noise, $S _ { n } ( f )$ .When the detector is turned on,one measures $\langle s ^ { 2 } ( t ) \rangle$ ， where as usual $s ( t ) = n ( t ) + h ( t )$ with $n ( t )$ the noise and $h ( t )$ the response of the detector to a GW signal. If one observes that $\langle s ^ { 2 } ( t ) \rangle$ is larger than expected, the crucial problem is how to tell whether this is really due to a GW background or,more trivially,to some source of noise that has not been adequately accounted for when estimating $S _ { n } ( f )$ . Similar problems were faced $\mathrm { i n }$ the discovery of the cosmic microwave background;Penzias and Wilson found an excess noise in their antenna (a horn reflector that was meant for satelite communications) and worked hard for one year in order to exclude all possible sources of terrestrial and astrophysical noise,before writing a short paper with the modest title “A Measurement of Excess Antenna Temperature at 4080 $\mathrm { M c / s ^ { 3 } }$ ,and concluding“From a combination of the above,we compute the remaining unaccounted-for antenna temperature to be $3 . 5 \pm 1 . 0 ~ K$ at $\psi \theta \theta M c / s ^ { \prime \prime }$

To cope with this problem,it is clear that in the search for stochastic backgrounds of GWs with a single detector one must set at least a relatively high threshold on the signal-to-noise ratio； for instance,a signal-to-noise ratio $S / N = 5$ on the amplitude could be a typical choice (while lower values of $S / N$ could be used for the only purpose of putting upper bounds). Further handles could come from an anisotropy of the stochastic GW background,if it is due to unresolved galactic sources, since this would produce a sidereal time modulation due to the motion of the detector.Another handle is the possibility that the dependence of the excess noise on the frequency is found to be in agreement with some theoretical prediction from a given cosmological or astrophysical mechanism.

To compute the minimum value of $h _ { 0 } ^ { 2 } \Omega _ { \tt g w }$ that can be measured at a given $S / N$ ,we observe that,if there isno signal,we have (see eq.(7.12))

$$
\langle s ^ { 2 } ( t ) \rangle = \langle n ^ { 2 } ( t ) \rangle = \int _ { 0 } ^ { \infty } d f S _ { n } ( f ) ,
$$

while,if a stochastic GW background is present,there is also a contribution from $h ( t )$ .For each propagation direction $\hat { \bf n }$ we can write $h ( t ) = h _ { + } F _ { + } + h _ { \times } F _ { \times }$ ,and therefore,taking the ensemble average and

averaging also over $\hat { \bf n }$ and over the polarization angle $\psi$

$$
\int \frac { d ^ { 2 } \hat { \bf n } } { 4 \pi } \frac { d \psi } { 2 \pi } \langle h ^ { 2 } \rangle = \left( \int \frac { d ^ { 2 } \hat { \bf n } } { 4 \pi } \frac { d \psi } { 2 \pi } F _ { + } ^ { 2 } \right) \langle h _ { + } ^ { 2 } + h _ { \times } ^ { 2 } \rangle ,
$$

where we used the fact that the angular averages of F² and of F& ar equal,see eq. (7.35). For an isotropic background,the ensemble averag $\left. h ^ { 2 } \right.$ that appears on the left-hand side of eq.(7.207) is independem of the angles n and ,so the angular average gives one. The term o the right-hand side of eq.(7.207),instead,can be written in terms Sh(f）using eq. (7.192) and observing that,for any given propagatioi direction,we have hijhj=2(h²+h²）.Then

$$
\langle h ^ { 2 } \rangle = 2 \langle F _ { + } ^ { 2 } \rangle \int _ { 0 } ^ { \infty } d f S _ { h } ( f ) ,
$$

where,with an abuse of notation,the brackets in $\langle h ^ { 2 } \rangle$ denote the en semble average while the brackets in $ { \langle F _ { + } ^ { 2 } \rangle }$ denotes the average over $d ^ { 2 } \hat { \mathbb { n } }$ and dψ.In eq.(7.37) we have defined the angular efficiency factor F=(F²)+ (F²)= 2(F²),whose value for various detectors are given in Table 7.1. In particular,F=2/5 for interferometers and F=8/15 for resonant bars. Then

$$
\left. h ^ { 2 } ( t ) \right. = F \int _ { 0 } ^ { \infty } d f S _ { h } ( f ) .
$$

So, in the presence of signal,

$$
\begin{array} { l } { { \displaystyle \langle s ^ { 2 } ( t ) \rangle = \langle n ^ { 2 } ( t ) \rangle + \langle h ^ { 2 } ( t ) \rangle } } \\ { { \displaystyle \qquad = \int _ { 0 } ^ { \infty } d f \left[ S _ { n } ( f ) + F S _ { h } ( f ) \right] . } } \end{array}
$$

Therefore,if a stochastic background is present,one simply observes thal (s2(t))is higher than the value expected from the noise,everywhere o just in some frequency range. More precisely, we can compare the output with the expected value of Sn(f） in each frequency bin (with bins of size△f =1/T after an observation time T). To take the binning into account,we replace

68Observe that here S/N is the signalto-noise ratio with respect to the GW amplitude, just as we have defined it for bursts,coalescence and periodic signals.For stochastic backgrounds,what is actually measured is an energy density,and it make sense to introduce the signal-to-noise ratio with respect to the energy density，which is quadratic in the amplitude. If one prefers to reserve the notation $S / N$ for the signal-to-noise ratio in energy,then on the left-hand side of eq.(7.213) one must write $S / N$ rather than $( S / N ) ^ { 2 }$

$$
\int S _ { h } ( f ) d f  \sum _ { i } S _ { h } ( f _ { i } ) \Delta f ,
$$

and

$$
\int S _ { n } ( f ) d f  \sum _ { i } S _ { n } ( f _ { i } ) \Delta f
$$

The signal-to-noiseratioineadh binis therefore $^ { 6 8 }$

$$
\left( \frac { S } { N } \right) ^ { 2 } = F \frac { S _ { h } ( f _ { i } ) \Delta f } { S _ { n } ( f _ { i } ) \Delta f }
$$

Of course the integration time $T$ ，which enters through $\Delta f$ ，canceled in eq.(7.213). Increasing the integration time,we decrease the size of the bins and therefore the noise in each bin,but we equally decrease the signal present in each bin. Therefore,in a single detector,as far as the signal-to-noise ratio is concerned,there is no gain in integrating the signal in time. Either the signal stands out immediately as soon as we switch on the detector,or it will always remain below the noise. If however the signal stands out,integrating it for a longer time we get a more detailed resolution of its frequency dependence.

In conclusion, the minimum value df $S _ { h } ( f )$ measurable with a single detector having a noise spectral density $S _ { n } ( f )$ ,at a given level $S / N$ of signal-to-noise ratio in amplitude, is

$$
[ S _ { h } ( f ) ] _ { \mathrm { m i n } } = S _ { n } ( f ) \frac { ( S / N ) ^ { 2 } } { F } ,
$$

and correspondingly the minimum detectable value of $\Omega _ { \mathrm { g w } }$ is

$$
\overline { { [ \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } } = \frac { 4 \pi ^ { 2 } } { 3 H _ { 0 } ^ { 2 } } f ^ { 3 } S _ { n } ( f ) \frac { ( S / N ) ^ { 2 } } { F } } } .
$$

A very important feature of this expression is the factor $f ^ { 3 }$ It tells us that,if one is able to reacha given level in $S _ { n } ( f )$ at low frequencies,it willbe possible to reach a much better sensitivity in $\Omega _ { \mathrm { g w } } ( f )$ compared to what can be obtained with a similar value of $S _ { n } ( f )$ at high frequencies. Of course,the experimental problems that one has to solve in order to reach a given value of $S _ { n } ( f )$ depend very strongly on the frequency $f$ However, at $f = 1 0 ^ { - 3 } ~ \mathrm { H z }$ the space detector LISA aims at reaching a strain sensitivity $S _ { n } ^ { 1 / 2 } ( f ) = 4 \stackrel {  } { \times } 1 0 ^ { - 2 1 } \mathrm { H z } ^ { - 1 / 2 }$ , while a ground-based $f = 1 0 ^ { 2 } ~ \mathrm { H z }$ hre, $S _ { n } ^ { 1 / 2 } ( f ) = 4 \times 1 0 ^ { - 2 3 } \bar { \mathrm { H z } } ^ { - 1 / 2 }$ $f = 1 0 ^ { 2 } ~ \mathrm { H z }$ $f =$ 10-3 Hz, we lose only four orders in magnitude in Sn(f),but we gain a factor $( 1 0 ^ { 2 } / 1 0 ^ { - 3 } ) ^ { 3 } = 1 0 ^ { 1 5 }$ thanks to $f ^ { 3 }$ Therefore,it is much easier to reach a small level for $[ \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } }$ at low $f$ rather than at high $f$ The otler important question is in what frequency range should we expect that cosmological or astrophysical mechanisms produce an interesting value for $\Omega _ { \mathrm { g w } } ( f )$ ．As we will see in Vol. 2,there is a large variety of possible mechanisms,which can produce stochastic GW backgrounds everywhere from $f = 1 0 ^ { - 1 8 } ~ \mathrm { H z }$ up to $f = 1 0 ^ { 9 } ~ \mathrm { H z }$ Their detection is therefore easier when they are large at low frequencies,since then comparatively high value of the noise spectral density $S _ { n } ( f )$ can be overcompensated by the factor $f ^ { 3 }$ ,and becomes more and more difficult as we go to high frequencies. Numerically，with normalizations useful for LISA, eq. (7.215) gives

$$
\begin{array} { r l r } {  { [ h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } } = 1 . 1 \times 1 0 ^ { - 1 2 } ( \frac { f } { 1 \mathrm { m H z } } ) ^ { 3 } ( \frac { S _ { n } ^ { 1 / 2 } } { 4 \times 1 0 ^ { - 2 1 } \mathrm { H z } ^ { - 1 / 2 } } ) ^ { 2 } } } \\ & { } & { \times ( \frac { 1 / \sqrt { 5 } } { F } ) ( \frac { S / N } { 5 } ) ^ { 2 } . } \end{array}
$$

Using normalization factors appropriate for ground-based interferom ters,we rather have

$$
\begin{array} { l } { { \displaystyle [ h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } } = 0 . 1 2 \left( \frac { f } { 1 0 0 \mathrm { H z } } \right) ^ { 3 } \left( \frac { S _ { n } ^ { 1 / 2 } } { 4 \times 1 0 ^ { - 2 3 } \mathrm { H z } ^ { - 1 / 2 } } \right) ^ { 2 } } } \\ { { \displaystyle \qquad \times \left( \frac { 2 / 5 } { F } \right) \left( \frac { S / N } { 5 } \right) ^ { 2 } . } } \end{array}
$$

In both cases we used a rather high value of the signal-to-noise rati as a reference value, $S / N = 5$ ，according to the discussion above. huge difference between the value $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } \sim 1 0 ^ { - 1 2 }$ in eq.(7.216)and th value $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } \sim 0 . 1$ in eq.(7.217) is due to the fact that LISA can read a value of $S _ { n }$ not far from that of ground-based interferometers,at much lower frequency.

As we wil see in Vol. 2, no cosmological or astrophysical backgroun of GW is expected to exceed $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( \bar { f } ) \sim 1 0 ^ { - 5 }$ ，independently of th frequency. Therefore eqs.(7.216) and(7.217) tell us that LISA has a extremely good sensitivity for stochastic backgrounds of GWs,whil ground-based interferometers,used as single detectors,do not reach a interesting level for stochastic backgrounds. However, having at ou disposal more than one ground-based detector (interferometers or bars we can correlate their outputs,and the sensitivity improves dramatically as we discuss in the next section.

# 7.8.3 Two-detector correlation

# Optimal signal-to-noise ratio

With a single detector,it islimpossible to adapt to stochastic back grounds the matched filtering technique that we studied in Section 7.3 The reason is that, to perform the matched filtering,we need to know th form of the signal, but for stochastic backgrounds the GW signal h( isan unpredictable randomly fluctuating quantity, just like the nois $n ( t )$ . However,if we have two detectors,we can use a modified form @ matched filtering in which,rather than trying to match the output ofi single detector to a predetermined signal $h ( t )$ ，we match the output o one detector to the output of the other.

To implement this idea we proceed as follows.We write the outpu $s _ { k } ( t )$ of the $k$ -th detector as $s _ { k } ( t ) = h _ { k } ( t ) + n _ { k } ( t )$ ，where $k = 1 .$ labels the detector.Observe that the scalar output $h _ { k } ( t )$ depends general on the detector,because different detectors can have a diferem location and/ora different orientation and therefore a different pattem function. We are interested in the situation in which the GW signa $h _ { k } ( t )$ is much smaller than the noise $n _ { k } ( t )$ ,which is the realistic situation for all ground-based detectors,as we have seen in the previous section. Multiplying both sides of eq.(7.188) by the detector tensor $D ^ { i j }$ and using eq. (7.21),we can write the GW signal $h _ { k }$ in the $k$ -th detector as

$$
h _ { k } ( t , { \bf x } _ { k } ) = \sum _ { A = + , \times } \int _ { - \infty } ^ { \infty } d f \int d ^ { 2 } { \hat { \bf n } } { \tilde { h } } _ { A } ( f , { \hat { \bf n } } ) e ^ { - 2 \pi i f ( t - { \hat { \bf n } } \cdot { \bf x } _ { k } / c ) } F _ { k } ^ { A } ( { \hat { \bf n } } ) ,
$$

where $F _ { k } ^ { A }$ are the pattern functions of the $k$ -th detector and $\mathbf { x } _ { k }$ isits location.As always,the size of the detector is taken to be much smaller than $^ { \ddagger }$ ，so we can neglect the spatial variation of the GW over the extension of the detector.Passing to the Fourier transform,we have

$$
\tilde { h } _ { k } ( f ) = \sum _ { A = + , \times } \int d ^ { 2 } \hat { \bf n } \tilde { h } _ { A } ( f , \hat { \bf n } ) e ^ { 2 \pi i f \hat { \bf n } \cdot { \bf x } _ { k } / c } F _ { k } ^ { A } ( \hat { \bf n } ) ,
$$

where we denote $\tilde { h } _ { k } ( f , { \bf x } _ { k } )$ simply as $\tilde { h } _ { k } ( f )$ .To correlate the outputs $s _ { 1 } ( t )$ and $s _ { 2 } ( t )$ of the two detectors we define

$$
Y = \int _ { - T / 2 } ^ { T / 2 } d t \int _ { - T / 2 } ^ { T / 2 } d t ^ { \prime } s _ { 1 } ( t ) s _ { 2 } ( t ^ { \prime } ) Q ( t - t ^ { \prime } ) ,
$$

where $T$ is the total observation time (e.g. one year) and $Q$ a real filter function,analogous to the function $K ( t )$ in Section 7.3. $Y$ is our signal, and we want to maximize its signal-to-hoise ratio.

We limit ourselves to functions $Q ( t - t ^ { \prime } )$ that fall rapidly to zero for large $\vert t - t ^ { \prime } \vert$ . Passing to the Fourier transforms, we get

$$
Y = \int _ { - \infty } ^ { + \infty } d f d f ^ { \prime } d f ^ { \prime \prime } \delta _ { T } ( f - f ^ { \prime \prime } ) \delta _ { T } ( f ^ { \prime } - f ^ { \prime \prime } ) \tilde { s } _ { 1 } ^ { * } ( f ) \tilde { s } _ { 2 } ( f ^ { \prime } ) \tilde { Q } ( f ^ { \prime \prime } ) ,
$$

where

$$
\begin{array} { c } { { \displaystyle \delta _ { T } ( f ) \equiv \int _ { - T / 2 } ^ { T / 2 } d t e ^ { i 2 \pi f t } } } \\ { { \displaystyle = \frac { \sin ( \pi f T ) } { \pi f } , } } \end{array}
$$

and becomes a delta function in the limit $f T \to \infty$ .Even on a relatively short stretch of data with， say, $T = | 1 0 ^ { 3 } \mathrm { ~ s ~ } |$ ，at $f \ = \ 1 0 \ \mathrm { H z }$ we have $f T = 1 0 ^ { 4 }$ . Over the whole useful bandwidth of ground-based detectors we can therefore replace $\delta _ { T } ( f )$ by a Dirac delta,and eq.(7.220) becomes

$$
Y \simeq \int _ { - \infty } ^ { + \infty } d f \tilde { s } _ { 1 } ^ { * } ( f ) \tilde { s } _ { 2 } ( f ) \tilde { Q } ( f ) .
$$

Recall that, in the signal-to-noise ratio $\mathcal { S } / N$ ， $S$ is defined as the ensemble average value of $Y$ when the signal is present,while $N$ is the rms value of Y when the signal is absent. Then,assuming that the noise in the two detectors are not correlated (and averaging also over the polarization angle $\psi$ ），

$$
S = \int _ { - \infty } ^ { + \infty } d f \left. \tilde { h } _ { 1 } ^ { * } ( f ) \tilde { h } _ { 2 } ( f ) \right. \tilde { Q } ( f )
$$

$$
\begin{array} { l } { { \displaystyle = \int _ { - \infty } ^ { + \infty } d f \sum _ { A , A ^ { \prime } } \int d ^ { 2 } { \hat { \bf n } } d ^ { 2 } { \hat { \bf n } } ^ { \prime } \int \frac { d \psi } { 2 \pi } e ^ { - 2 \pi i f ( { \hat { \bf n } } \cdot { \bf x } _ { 1 } - { \hat { \bf n } } ^ { \prime } \cdot { \bf x } _ { 2 } ) / c } } } \\ { { \displaystyle \times F _ { 1 } ^ { A } ( { \hat { \bf n } } ; \psi ) F _ { 2 } ^ { A ^ { \prime } } ( { \hat { \bf n } } ^ { \prime } ; \psi ) \left. { \tilde { h } } _ { A } ^ { * } ( f , { \hat { \bf n } } ) { \tilde { h } } _ { A ^ { \prime } } ( f , { \hat { \bf n } } ^ { \prime } ) \right. { \tilde { Q } } ( f ) . } } \end{array}
$$

Using eq.(7.190),tgeher $\begin{array} { r } { \delta ( 0 ) = \int _ { - T / 2 } ^ { T / 2 } d t = T } \end{array}$ this becomes

$$
S = { \frac { T } { 2 } } \int _ { - \infty } ^ { \infty } d f S _ { h } ( f ) \Gamma ( f ) \tilde { Q } ( f ) ,
$$

where we have defined

<table><tr><td>r(=/ 1</td><td>[F((</td></tr></table>

and $\Delta { \bf x } = { \bf x } _ { 2 } - { \bf x } _ { 1 }$ is the separation between the two detectors.The func tion $\Gamma$ in called the (unnormalized) overlap reduction function. It taks into account the fact that the two detectors can see a different grav tational signal,either because they are at different location or becaus they have a different angular sensitivity.

The difference in location is|reflected in the exponential factor. In par ticular,if $2 \pi f \Delta x / c \gg 1$ ,i.e.if the separation $\Delta x \gg \dagger$ ,this exponential is rapidly oscillating and suppresses strongly the correlation. This reflee the fact that,when $\Delta x \gg \dot { x }$ ，the two detectors are experiencing GW signals that are uncorrelated.

The different angular sensitivity of the two detectors is instead re fected in the term $\mathrm { \Sigma } { \sum } _ { A } F _ { 1 } ^ { A } ( \hat { \mathbf { n } } ) F _ { 2 } ^ { A } ( \hat { \mathbf { n } } )$ .It is also useful to introduce th quantity

$$
F _ { 1 2 } \equiv \int \frac { d ^ { 2 } \hat { \bf n } } { 4 \pi } \int \frac { d \psi } { 2 \pi } \sum _ { A } F _ { 1 } ^ { A } ( \hat { \bf n } ) F _ { 2 } ^ { A } ( \hat { \bf n } ) \Bigg | _ { \mathrm { a l i g n e d } } ,
$$

69For two detectors of the same type this means to orient them in the same way,so in a two-interferometer correlation the arms are taken to be along the $\boldsymbol { x }$ and $y$ axes for both interferometers, and for a two-bar correlation the longitudinal axes of the bars are taken parallel to each other.For the correlation between a bar and an interferometer,we see from the form of the pattern functions given in Table 7.1 that the optimal correlation is obtained aligning the longitudinal axis of the bar with one of the arms of the interferometer.

where the subscript means that we must compute $F _ { 1 2 }$ taking the two detectors to be at the same location and oricnted one relative to the other so that the quantity $F _ { 1 2 }$ is maximized.69 Observe that,if the tw detectors are of the same type e.g. two interferometers or two cylindrical bars, $F _ { 1 2 }$ is the same as the constant $F$ defined in eq. (7.37). The (normalized) overlap reduction function $\gamma ( f )$ is defined as

$$
\gamma ( f ) = \frac { \Gamma ( f ) } { F _ { 1 2 } } .
$$

For instance,for the correlation between two interferometers, $F _ { 1 2 } = 2 / 5 .$ The factor $F _ { 1 2 }$ takes into account the reduction in sensitivity due to the pattern functions,already present in the case of one interferometer,and therefore $\gamma ( f )$ separately takes into account the effect of the separation $\Delta \mathbf { x }$ between the interferometers,and of their relative orientation.Witl this definition, $\gamma ( f ) = 1$ if the separation $\Delta x = 0$ and if the detectors are perfectly aligned.However, the use of $\Gamma ( f )$ is more convenient when we want to write equations that hold independently of what detectors (interferometers,bars,or spheres) are|used in the correlation.

We now find the optimal choice of the filter function $\tilde { Q } ( f )$ that maximizes the signal-to-noise ratio. We need to compute

$$
\begin{array} { r l r } {  { N ^ { 2 } = \big [ \langle Y ^ { 2 } \rangle - \langle Y \rangle ^ { 2 } \big ] _ { h = 0 } } } \\ & { } & { = \int _ { - \infty } ^ { \infty } d f d f ^ { \prime } \tilde { Q } ( f ) \tilde { Q } ^ { * } ( f ^ { \prime } ) } \\ & { } & { \times [ \langle \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 2 } ( f ) \tilde { n } _ { 1 } ( f ^ { \prime } ) \tilde { n } _ { 2 } ^ { * } ( f ^ { \prime } ) \rangle - \langle \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 2 } ( f ) \rangle \langle \tilde { n } _ { 2 } ^ { * } ( f ^ { \prime } ) \tilde { n } _ { 1 } ( f ^ { \prime } ) \rangle ] . } \end{array}
$$

If the noise in the two detectors are uncorrelated,the mixed correlator $\langle \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 2 } ( f ) \rangle$ vanishes,so the second term in brackets is zero,while the frst factorizes $\langle \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 2 } ( f ) \tilde { n } _ { 1 } ( f ^ { \prime } ) \tilde { n } _ { 2 } ^ { * } ( f ^ { \prime } ) \rangle = \langle \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 1 } ( f ^ { \prime } ) \rangle \langle \tilde { n } _ { 2 } ( f ) \tilde { n } _ { 2 } ^ { * } ( f ^ { \prime } ) \rangle$ Then we get

$$
N ^ { 2 } = \int _ { - \infty } ^ { \infty } d f d f ^ { \prime } \tilde { Q } ( f ) \tilde { Q } ^ { * } ( f ^ { \prime } ) \langle \tilde { n } _ { 1 } ^ { * } ( f \vert \tilde { n } _ { 1 } ( f ^ { \prime } ) \rangle \langle \tilde { n } _ { 2 } ^ { * } ( f ^ { \prime } ) \tilde { n } _ { 2 } ( f ) \rangle .
$$

Using

$$
\left. \tilde { n } _ { k } ^ { * } ( f ) \tilde { n } _ { k } ( f ^ { \prime } ) \right. = \delta ( f - f ^ { \prime } ) { \frac { 1 } { 2 } } S _ { n , k } ( f ) ,
$$

where $S _ { n , k } ( f )$ is the noise spectral density of the $k$ -th detector,and using $\delta ( 0 ) = T$ ,we finally get

$$
N ^ { 2 } = \frac { T } { 4 } \int _ { - \infty } ^ { \infty } d f \vert { \tilde { Q } } ( f ) \vert ^ { 2 } S _ { n } ^ { 2 } ( f ) ,
$$

where we have defined the combined noise spectral density

$$
S _ { n } ( f ) = \left[ S _ { n , 1 } ( f ) | S _ { n , 2 } ( f ) \right] ^ { 1 / 2 } .
$$

Equations (7.225) and (7.232) show the same crucial feature that we already observed when we discussed the matched filtering for periodic signals: the signal $S$ increase linearly with the observation time $T$ ,while the noise $N$ increases only as $T ^ { 1 / 2 }$ .Therefore,the signal-to-noise ratio increases with the observation time as $T ^ { 1 / 2 }$ Puting together eqs.(7.225) and (7.232) we have

$$
\frac { S } { N } = T ^ { 1 / 2 } \frac { \int _ { - \infty } ^ { \infty } d f S _ { h } ( f ) \Gamma ( f ) \tilde { Q } ( f ) } { \left[ \int _ { - \infty } ^ { \infty } d f | \tilde { Q } ( f ) | ^ { 2 } S _ { n } ^ { 2 } ( f ) \right] ^ { 1 / 2 } } .
$$

We can now find the flter function $\tilde { Q } ( f )$ that maximizes $S / N$ The procedure is analogous to what we have already done between eqs. (7.45) And (7.51). For any two complex functions $A ( f ) , B ( f )$ we define the positive definite scalar product

$$
( A , B ) = \int _ { - \infty } ^ { \infty } d f A ^ { * } ( f ) B ( f ) S _ { n } ^ { 2 } ( f ) .
$$

Then eq.(7.234) can be rewritten as

$$
{ \frac { S } { N } } = T \llap { / } ^ { 1 / 2 } \frac { \left( \tilde { Q } , \Gamma S _ { h } / S _ { n } ^ { 2 } \right) } { ( \tilde { Q } , \tilde { Q } ) ^ { 1 / 2 } } .
$$

As we already discussed below eq. (7.47),this expression is maximize choosing

$$
\tilde { Q } ( f ) = \mathrm { c o n s t . } \frac { \Gamma ( f ) S _ { h } ( f ) } { S _ { n } ^ { 2 } ( f ) } .
$$

It is important to observe that the optimal filter depends on the sig nal that we are looking for, since $S _ { h } ( f )$ enters eq. (7.237). Pluggin eq.(7.237) into eq.(7.236) we find the optimal signal-to-noise ratio,

$$
\frac { S } { N } = T ^ { 1 / 2 } \left( \frac { \Gamma S _ { h } } { S _ { n } ^ { 2 } } , \frac { \Gamma S _ { h } } { S _ { n } ^ { 2 } } \right) ^ { 1 / 2 } ,
$$

70Observethat，forperiodicsignals and for bursts,as well as fora singledetector search of stochastic backgrounds,we defined the quantity $S / N$ as linear in the GW,i.e.if $\tilde { h } ( f ) $ $\tilde { \lambda \hbar } ( f )$ ，then $( S / N ) ~ \to ~ \lambda ( S / N )$ ，see eq.(7.51) and eq.(7.213).For searches of stochastic backgrounds with twodetector correlations,we have rather defined $S / N$ as linear both in $h _ { 1 } ( t )$ and in $h _ { 2 } ( t )$ and therefore $S / N$ scales overall quadratically in the GW amplitude. If we prefer to use a quantity that is linear in the GW amplitude we can define $\mathrm { S N R } \ = \ ( S / N ) ^ { 1 / 2 }$ ，so SNR is proportional to $T ^ { 1 / 4 }$ .Of course,it isa matter of conventions whether to use SNR or $( S / N )$

or,writing explicitly the scalar product,70

<table><tr><td>S N</td><td>8 s（）] 2T dfr2（f） s 0</td></tr></table>

In particular,foratwo-interferometer correlation, $\Gamma ( f ) = ( 2 / 5 ) \gamma ( f ) \mathrm { a n }$

$$
\left( \frac { S } { N } \right) _ { \mathrm { i n t - i n t f } } = \left[ \frac { 8 } { 2 5 } T \int _ { 0 } ^ { \infty } d f \gamma ^ { 2 } ( f ) \frac { S _ { h } ^ { 2 } ( f ) } { S _ { n } ^ { 2 } ( f ) } \right] ^ { 1 / 2 } .
$$

For two cylindrical bars, instead, $\Gamma ( f ) = ( 8 / 1 5 ) \gamma ( f )$ ,while for the cor relation between an interferometer and a cylindrical bar,from the ex plicit expressions of the pattern functions in Table 7.1，we get again $\Gamma ( f ) = ( 2 / 5 ) \gamma ( f )$

Using eqs.(7.233)and (7.202) we can also rewrite eq.(7.239) as

$$
\frac { S } { N } = \frac { 3 H _ { 0 } ^ { 2 } } { 4 \pi ^ { 2 } } \left[ 2 T \int _ { 0 } ^ { \infty } d f \Gamma ^ { 2 } ( f ) \frac { \Omega _ { \mathrm { g w } } ^ { 2 } ( f ) } { f ^ { 6 } S _ { n , 1 } ( f ) S _ { n , 2 } ( f ) } \right] ^ { 1 / 2 } ,
$$

and in particular,for a two-interferometer correlation,

$$
\left( \frac { S } { N } \right) _ { \mathrm { i n t - i n t } } = \frac { 3 H _ { 0 } ^ { 2 } } { 1 0 \pi ^ { 2 } } \left[ 2 T \int _ { 0 } ^ { \infty } d f \gamma ^ { 2 } ( f ) \frac { \Omega _ { \mathrm { g w } } ^ { 2 } ( f ) } { f ^ { 6 } S _ { n , 1 } ( f ) S _ { n , 2 } ( f ) } \right] ^ { 1 / 2 } .
$$

We can now compare the measurements of stochastic backgrounds performed with the two-detector correlation,to the measurement which uses a single detector,both from the point of view of sensitivity,and of the ability to discriminate true GWs from noise.

Comparison of two-detector and single-detector sensitivities

To compare the sensitivity of a two-detector correlation with the sensitivity of a single detector we assume that we have two identical detectors at a very close distance and with the same orientation,so that $\Gamma ( f )$ becomes equal to the angular efficiency factor $F _ { 1 2 } = F$ .(This is the most favorable situation； however in practice,if the detectors are too close, there will be correlated noise.） To perform an order-of-magnitude estiinate, we approximate eq. (7.239) as

$$
\left( \frac { S } { N } \right) ^ { 2 } \sim \left( 2 T \Delta f \right) F ^ { 2 } \frac { S _ { h } ^ { 2 } } { S _ { n } ^ { 2 } } ,
$$

where $\Delta f$ is the useful bandwidth of the detectors,centered around a frequency $f$ and $S _ { n }$ and $S _ { h }$ are typical values of $S _ { n } ( f )$ and $S _ { h } ( f )$ , respectively,over this bandwidth.Then the minimum detectable value of $S _ { h }$ ,at signal-to-noise level $S / N$ ,is

$$
( S _ { h } ) _ { \mathrm { m i n } } \sim \frac { S _ { \eta } } { ( 2 T \Delta f ) ^ { 1 / 2 } } \frac { ( S / N ) } { F } ,
$$

and therefore

$$
[ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n } } \sim { \frac { 4 \pi ^ { 2 } } { 3 H _ { 0 } ^ { 2 } } } { \frac { f ^ { 3 } S _ { n } } { ( 2 { \cal T } \Delta f ) ^ { 1 / 2 } } } { \frac { ( S / N ) } { F } } .
$$

where $f ^ { 3 }$ is really a typical value of $f ^ { 3 }$ over the bandwidth. Comparing eq. (7.244) with eq. (7.214) we see that,correlating two detectors,we have gained a factor $( 2 T \Delta \bar { f } ) ^ { - 1 / 2 }$ .Numerically,

$$
{ \frac { 1 } { ( 2 T \Delta f ) ^ { 1 / 2 } } } \simeq 1 \times 1 0 ^ { - 5 } \left( \frac { 1 5 0 \mathrm { { H z } } } { \Delta f } \right) ^ { 1 / 2 } \left( \frac { 1 \mathrm { { y r } } } { T } \right) ^ { 1 / 2 } .
$$

Therefore,integrating for one year the output of two detectors with a bandwidth of $1 5 0 ~ \mathrm { H z }$ ,we can improve our sensitivity to $S _ { h }$ ,and therefore to $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } }$ ,by approximately five orders of magnitudes,with respect to the sensitivity of a single detector $7 3$ It is interesting to compare these results with the matched filtering procedure discussed in Section 7.3.In Section 7.3 we took advantage of the fact that we knew the form of the signal,in order to discriminate it from the noise.Here, instead,in a single detector both the signal and the noise have the same statistical properties,but we took advantage of the fact the signals in the two detectors are correlated,while the noise are decorrelated. In particular, the measure of the correlation between the signals in the two detectors is given by the overlap reduction function $\Gamma ( f )$ of eq. (7.226),which shows that the signals are indeed well correlated if the separation between the detectors is much smaller than $\ddagger$ ,and if the detectors are well oriented with respect to each other. Technically,the assumptions that the noise are uncorrelated entered ineq. (7.224),as well as when passing from eq.(7.229) to eq.(7.230),where we neglected the correlator [ $| \tilde { n } _ { 1 } ^ { * } ( f ) \tilde { n } _ { 2 } ( f ) \rangle$

71The precise numbers, of course, can only be obtained once we have the form of $S _ { h } ( f )$ and of $S _ { n } ( f )$ ，carrying out the integral in eq.(7.239).Observe also that in eq.(7.214) appears $( S / N ) ^ { 2 }$ while in eq.(7.244) appears $( S / N )$ ，but this is simply a consequence of the fact that,for the two-detector correlation, we have defined $S / N$ as a quantity quadratic in the GW amplitude,while for a single detector we defined it to be linear in the GW amplitude.Once we choose our criterion for fixing the confidence level,e.g.a signal-to-noise ratio 1.7 in amplitude,the quantity that we are denoting by $( S / N ) ^ { 2 }$ here and the quantity denoted by $S / N$ in eq. (7.214) have the same numerical value.

Recall however that the optimal filter depends on the form of the signal.A stochastic background of cosmological origin,as we will see in Vol.2, is not expected to show strong spectral features in the bandwidth $\Delta f \sim 1 ~ \mathrm { k H z }$ of ground based interferometers,so it should be adequate a simple power-law parametrization,

$$
h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f ) = K f ^ { \alpha }
$$

where $K$ and $\alpha$ are two parameters,and $\alpha$ could be positive or negative.For each value of $\alpha$ we can construct the optimal filter (the overall constant in the filter is irrelevant,as we have seen,so different values of $K$ give the same filter) and,given the noise spectral density $S _ { n } ( f )$ eq.（7.239） gives $S / N$ as a function of $K$ and $\alpha$ ，and therefore tells us what region of this parameter space can be explored,at a given confidence level. For astrophysical backgrounds,more elaborated parametrizations of $h _ { 0 } ^ { 2 } \Omega _ { \mathrm { g w } } ( f )$ might be necessary at broadband detectors.

# Non-stationary noise

Until now,we have assumed that the noise in the detectors is stationary. and that it can be represented by a fixed function $S _ { n } ( f )$ .However,such an assumption is not realistic,even more considering that we wish to use a very long observation time,of the order of months.Each detector has periods where it is more quiet and periods where,because of envirolmental or other disturbances,itis more noisy. Therefore the function $S _ { n } ( f )$ changes with time,and we must know how to combine periods in which the detectors had different noise. To study this issue we can subdivide the total observation time $I = 1 , \ldots , m$ labelstheitealoftadwith $_ T$ into $_ n$ intervals of length $\textstyle T = \sum _ { I = 1 } ^ { m } T _ { I }$ $T _ { I }$ ,where We choose the $T _ { I }$ so that within each interval the noise of the two detectors can be considered stationary. To each of these intervals we can then apply eq.(7.239),so the value of the optimal signal-to-noise ratio from this interval is

$$
\left( \frac { S } { N } \right) _ { I } ^ { 2 } = 2 T _ { I } \int _ { 0 } ^ { \infty } d f \Gamma ^ { 2 } ( f ) \frac { S _ { h } ^ { 2 } ( f ) } { S _ { n } ^ { 2 } ( f ; I ) } .
$$

Here $S _ { n } ( f ; I )$ is the total noise spectral density during the $\boldsymbol { I }$ -thinterval, $S _ { n } ^ { 2 } ( f ; I ) \ = \ S _ { n , 1 } ( f ; I ) S _ { n , 2 } ( f ; I )$ where $S _ { n , j } \{ f ; I \}$ is the noise spectral density of the $j$ -th detector during the $I -$ -th interval.We now ask how we should combine the $( S / N ) _ { I }$ of the different intervals to form the total optimal signal-to-noise ratio. The correct answer can be guessed observing that the optimal $( S / N ) _ { I } ^ { 2 }$ is linear in $T _ { I }$ ， see eq. (7.248) and, in the limit in which the noise is stationary over the whole observation time $T$ ，we must find that the total optimal signal-to-noise ratio $S / N$ satisfies $\begin{array} { r } { ( S / N ) ^ { 2 } \sim T = \sum _ { I } T _ { I } } \end{array}$ .This fixes uniquely the relation between the total optimal signal-to-noise|ratio $S / N$ and the $( S / N ) _ { I }$ ，

$$
\left( \frac { S } { N } \right) ^ { 2 } = \sum _ { I = 1 } ^ { m } \left( \frac { S } { N } \right) _ { I } ^ { 2 } .
$$

The same result can also be obtained more formally introducing the observable

$$
Y _ { \mathrm { t o t } } = \frac { \sum _ { I } \lambda _ { I } Y _ { I } } { \sum _ { I } \lambda _ { I } }
$$

(where it is understood that the sums fun over $I = 1 , \ldots , m )$ and choosing the variables $\lambda _ { I } > 0$ so that the signal-to-noise ratio of $Y _ { \mathrm { t o t } }$ is maximized.From eq.(7.225),with $T$ replaced by $T _ { I }$ ,we see that the $Y _ { I }$ have a mean value

$$
\begin{array} { r } { S _ { I } \equiv \left. Y _ { I } \right. = \mu T _ { I } , } \\ { \sim \qquad \sim \qquad } \end{array}
$$

where $\mu = \textstyle \int _ { 0 } ^ { \infty }$ df $S _ { h } ( f ) \Gamma ( f ) \tilde { Q } ( f )$ is independent of $I$ For the noise, from eq. (7.232) we have

$$
\begin{array} { c } { { N _ { I } ^ { 2 } = \displaystyle \frac { T _ { I } } { 4 } \int _ { - \infty } ^ { \infty } d f | \breve { Q } ( f ) | ^ { 2 } S _ { n } ^ { 2 } ( f ; I ) } } \\ { { \equiv T _ { I } \sigma _ { I } ^ { 2 } . } } \end{array}
$$

The signal-to-noise ratio $S / N$ of $Y _ { \mathrm { t o t } }$ is obtained by writing

$$
S = \langle Y _ { \mathrm { t o t } } \rangle = \mu \frac { \sum _ { I } \lambda _ { I } T _ { I } } { \sum _ { I } \lambda _ { I } } ,
$$

and

$$
\begin{array} { l } { { N ^ { 2 } = \left[ \langle Y _ { \mathrm { t o t } } ^ { 2 } \rangle - \langle Y _ { \mathrm { t o t } } \rangle ^ { 2 } \right] _ { \mu = 0 } } } \\ { { = \displaystyle \frac { \sum _ { I } \lambda _ { I } ^ { 2 } \sigma _ { I } ^ { 2 } T _ { I } } { ( \sum _ { I } \lambda _ { I } ) ^ { 2 } } , } } \end{array}
$$

where we assumed that noise in different intervals are uncorrelated,so $\langle Y _ { I } Y _ { J } \rangle = \delta _ { I J } N _ { I } ^ { 2 }$ .Therefore

$$
\frac { S ^ { 2 } } { N ^ { 2 } } = \mu ^ { 2 } \frac { ( \sum _ { I } \lambda _ { I } T _ { I } ) ^ { 2 } } { \sum _ { I } \lambda _ { I } ^ { 2 } \sigma _ { I } ^ { 2 } T _ { I } } .
$$

The maximization of this expresson with respect to the $\lambda _ { I }$ can be performed very simply,introducing the ppsitive definite scalar product between two vectors with real components $a _ { I }$ and $b _ { I }$ ，

$$
( a , b ) \equiv \sum _ { I } a _ { I } b _ { I } \sigma _ { I } ^ { 2 } T _ { I } .
$$

Then

$$
\frac { S } { N } = \mu \frac { ( \lambda _ { I } , \sigma _ { I } ^ { - 2 } ) } { ( \lambda _ { I } , \lambda _ { I } ) ^ { 1 / 2 } } .
$$

This expression is maximized if the vectors with components $\lambda _ { J }$ and $\sigma _ { I } ^ { - 2 }$ are parallel, so $\lambda _ { I } = 1 / \sigma _ { I } ^ { 2 }$ (apart from an irrelevant overall constant). Physically, this means that more noisy periods are weighted less.Then the variable $Y _ { \mathrm { o p t } }$ ,whose signal-to-noise ratio is optimal,is given by

$$
Y _ { \mathrm { o p t } } = \frac { \sum _ { I } \sigma _ { I } ^ { - 2 } Y _ { I } } { \sum _ { I } \sigma _ { I } ^ { - 2 } }
$$

and the value of the optimal $\mathbb { S } / N$ is given by

$$
\left( { \frac { S } { N } } \right) ^ { 2 } = \mu ^ { 2 } \vert ( \sigma _ { I } ^ { - 2 } , \sigma _ { I } ^ { - 2 } ) = \mu ^ { 2 } \sum _ { I } { \frac { T _ { I } } { \sigma _ { I } ^ { 2 } } } ,
$$

which，using eqs. (7.251)and (7.252)，is equivalent to eq. (7.249),a expected.Equation （7.239) then becomes

$$
\frac { S } { N } = \left[ 2 \int _ { 0 } ^ { \infty } d f \Gamma ^ { 2 } ( f | ) S _ { h } ^ { 2 } ( f ) \sum _ { I = 1 } ^ { m } \frac { T _ { I } } { S _ { n } ^ { 2 } ( f ; I ) } \right] ^ { 1 / 2 } .
$$

This is equivalent to saying that,in eq. (7.239)，we must make th replacement

$$
\frac { T } { S _ { n } ^ { 2 } ( f ) } \longrightarrow \sum _ { I = 1 } ^ { m } \frac { T _ { I } } { S _ { n } ^ { 2 } ( f ; I ) } .
$$

This way of composing the noise is very natural. It means that noisy periods contribute little to the total signal-to-noise ratio. If we perform the same order-of-magnitude estimate as in eq.(7.245), we conclude that

$$
\frac { 1 } { [ \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } } ^ { 2 } } = \sum _ { I = 1 } ^ { m } \frac { 1 } { [ \Omega _ { \mathrm { g w } } ( f ; I ) ] _ { \mathrm { m i n } } ^ { 2 } } ,
$$

where $[ \Omega _ { \mathrm { g w } } ( f ; I ) ] _ { \mathrm { m i n } }$ is the minimum value of $\Omega _ { \mathrm { g w } }$ detectable using only the data in the $I .$ -th interval,and $[ \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n } }$ is the minimum value of $\Omega _ { \mathrm { g w } }$ detectable combining the $n$ intervals.

# How the background is actually measured

We can now give an example of an operative way of measuring the stochastic background．First of all,one divides the total observation time $T$ into intervals of length $T _ { I }$ ,such that within each interval the detector noise is stationary. This scale is chosen based on observations of the detector noise variatiop，and could typically be of order of one to a few minutes. Within each interval, the spectral density $S _ { n } ( f ; I )$ can be considered constant in time,and is determined experimentally We can now compute the filter function,using the measured value of $S _ { n } ( f ; I )$ and assuming a given form for $\Omega _ { \mathrm { g w } }$ .For instance, $\Omega _ { \tt g w } = \mathrm { c o n s t } .$ can be the simplest choice,or one can use the parametrization (7.247) and repeat the procedure for yarious values of $\alpha$

To have an experimental determination of $S _ { I } = \langle Y _ { I } \rangle$ and of $N _ { I } =$ $[ \langle Y _ { I } ^ { 2 } \rangle - \langle Y _ { I } \rangle ^ { 2 } ] ^ { 1 / 2 }$ one further divides each intervalinto segments of length $\Delta t$ ,labeled byan index $J = 1 , \ldots , n$ ,and with $T _ { I } = n \Delta t$ (with $\Delta t$ much larger than the light travel time between the detectors,which for the two LIGO observatories is about $1 0 ~ \mathrm { m s } )$ . The signal $Y _ { I J }$ relative to the $J$ -th segment of the $I$ -th interval is computed using eq.(7.220),with the time integration running only over the $J$ -th segment of the $I _ { \ l }$ -th interval.72 Observe that the flter function $Q ( t - t ^ { \prime } )$ typically vanishes very fast for $\left| t - t ^ { \prime } \right|$ larger than a few tens of ms,so in practice if $t$ belongs to the

$J$ th interval, the support of $Q ( t - t ^ { \prime } )$ is entirely contained in the $J$ -th interval.

From the set of $Y _ { I J }$ at fixed $I$ ,one can construct the sample mean

$$
S _ { I } = \frac { 1 } { n } \sum _ { J = 1 } ^ { n } Y _ { I J } ,
$$

and the sample variance

$$
N _ { I } ^ { 2 } = \frac { 1 } { n - 1 } \sum _ { J = 1 } ^ { n } ( Y _ { I J } - S _ { I } ) ^ { 2 } ,
$$

of the $I _ { \ l }$ -th interval.We repeat this procedure for all intervals and, according to eq.(7.249),the total signal-to-noise ratio is

$$
\left( { \frac { S } { N } } \right) ^ { 2 } = \sum _ { I = 1 } ^ { m } \left( { \frac { S _ { I } ^ { 2 } } { N _ { I } ^ { 2 } } } \right) .
$$

Ifthis $S / N$ exceeds a predetermined threshold value one can state that a stochastic background is detected,with a confidence level which depends on the threshold used.73

73 A subtle pointis that it can be shown that,if we wait long enough,i.e.if the total observation time is sufficiently large,any predetermined fixed threshold will be exceeded．In other words, in the limit $T \to \infty$ the false alarm probability is $1 0 0 \%$ To havea finite false alarm probability even in the limit $T \to \infty$ ,the value of the threshold must increase with the number of intervals $n$ faster than $\log \log n$

With $N$ detectors we can form $N ( N - 1 ) / 2$ independent two-point correlators

# Multiple-detector correlation

Another interesting question is what happens if we correlate the outputs of $N$ detectors,with $N > 2$ .For simplicity,we assume at first that we have $N$ identical detectors,with the same noise spectral density $S _ { n } ( f )$ ， and all running simultaneously for a time $T$

$$
Y _ { i j } = \int _ { - T / 2 } ^ { T / 2 } d t \int _ { - T / 2 } ^ { T / 2 } d t ^ { \prime } s _ { i } ( t ) s _ { j } ( t ^ { \prime } ) Q ( t - t ^ { \prime } ) ,
$$

with $i < j$ .(If the detectors have different noise spectral densities, then also the filter function dependson $i , j$ ，and we write it $Q _ { i j } ( t -$ 1.）Conceptually, for a stationary stochastic background, there is no dlifference between the situation in which $N ( N - 1 ) / 2$ identical pairs of detectors run for a time $T$ ,and the situation in which a single pair of detectors runs fora time $T _ { \mathrm { t o t a l } } = T \times N ( N - 1 ) / 2$ .In the former case, sampling the output of the detectors at times $t _ { k }$ ,with $k = 1 , \ldots , k _ { \mathrm { m a x } }$ we get a set of values $Y _ { i j } ( t _ { k } )$ ,for each of the $N ( N - 1 ) / 2$ pairs $( i , j )$ .In the latter case we directly get a set of values $Y ( t _ { k } )$ for the single pair considered,with $k$ taking values up to $k _ { \operatorname* { m a x } } \times N ( N - 1 ) / 2$ .In both cases we must then compute the average of $Y$ over all these values,so the result is the same and the difference is just a matter of notation.In conclusion, the signal-to-noise ratio with $N$ identical detectors can be btained from eq.(7.239) making thereplacement

$$
T  \frac { N ( N - 1 ) } { 2 } T .
$$

If we denote by $[ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n , N } }$ the minimum value of $\Omega _ { \mathrm { g w } }$ measurable wil $N$ identical detectors and by $[ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n } , 2 }$ the minimum value of $\Omega _ { \mathrm { g w } }$ de tectable with two detectors,then

$$
[ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n , N } } = \left[ \frac { 2 } { N ( N - 1 ) } \right] ^ { 1 / 2 } [ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n , 2 } } .
$$

In the more realistic case in which the detectors have diferent noise spee tral densities,or have diferent common time of operation,the situatiol is formally identical to the case of non-stationary noise discussed above where the observations taken during a time $T _ { i j }$ by each pair of detector $( i , j )$ ，with $i < j$ ，plays the role of the observations taken during the time intervals labeled by $I$ in eqs.(7.260) to (7.262).Therefore, th signal-to-noise ratio is obtained from eq.(7.239) with the replacement

$$
\frac { T } { S _ { n } ^ { 2 } ( f ) } \left. \sum _ { i < j } \frac { T _ { i j } } { S _ { n } ^ { 2 } ( f ; \langle i j \rangle ) } \right. ,
$$

where $T _ { i j }$ is the common time|of operation of the detectors $i$ and $j$ and $S _ { n } ^ { 2 } ( f ; \langle i j \rangle ) = S _ { n } ( f ; i ) S _ { n } ( f ; j )$ is the product of the spectral densitie of the $i$ -thand $j$ -th detector.The order-of-magnitude estimate of th minimum detectable value of $\Omega _ { \mathrm { g w } }$ ,eq.(7.262)，,becomes

$$
\frac { 1 } { [ \Omega _ { \mathrm { g w } } ( f ) ] _ { \mathrm { m i n , N } } ^ { 2 } } = \sum _ { i < j } \frac { 1 } { [ \Omega _ { \mathrm { g w } } ( f ; \langle i j \rangle ) ] _ { \mathrm { m i n } } ^ { 2 } } .
$$

When all detectors are equal land have the same common time of op eration, $[ \Omega _ { \mathrm { g w } } ( f ; \langle i j \rangle ) ] _ { \mathrm { m i n } }$ becdmes independent of the pair $i , j$ considered,and is the quantity that we denoted by $[ \Omega _ { \mathrm { g w } } ] _ { \mathrm { m i n } , 2 }$ , so we recover eq. (7.268).

In a sense,this result is disappointing. We have seen in eq. (7.245 that，passing from a single detector to a two-detector correlation We gain a factor $1 / ( 2 T \Delta f ) ^ { 1 / 2 }$ in the minimum detectable value of $\Omega _ { \mathrm { g w } }$ . Fot $T = 1$ yr and $f = 1 0 0 ~ \mathrm { H z }$ ,this means and improvement by a factor $1 0 ^ { 5 }$ in sensitivity. Passing from $N = 2$ to $N = 3$ detectors, instead, we see from eq. (7.268) that we gain pnly a further factor $\sqrt { 3 }$

This is very different from the situation for bursts discussed in Sec tion 7.5.3. In the case of bursts,the noise that compete with the signal consists of large,relatively rare fuctuations. At any given moment the probability that,in a single detector and within a given time window,say of order few tens of ms,a fluctuation with a signal-to-noise ratio above a large threshold takes place,is a small number $\epsilon \ll 1$ .The probability that a second detector has a simultaneous independent fuctuation above this threshold,within the same window,is $O ( \epsilon ^ { 2 } )$ ，the probability of a three-detector coincidence is $O ( \epsilon ^ { 3 } )$ ,etc. Then,for bursts,the gain in statistical significance passing from a single detector to a two-detector coincidence is that same as the gain passing from a two-detector to a three-detector coincidence.The crucial point is that for bursts,after matched filtering,we are left with short events with a large value of $S / N$ ,which are rare.

In contrast,for stochastic backgrounds we are never confronted with rare events. At any given moment the GW stochastic signal is always much below the noise,and is never responsible for large fluctuations of the output.There are no rare events to be searched in coincidence,and the only advantage of using more detector pairs is that the total amount of data available increases,which means that we have a longer effective observation time.

The situation does not change substantially if,rather than two-point correlators,we consider $M$ -point correlators,with $M$ smaller than or equal the number of detectors $N$ .For instance,with four detectors we can consider a four-point correlator $\langle s _ { 1 } ( f ) s _ { 2 } ( f ) s _ { 3 } ( f ) s _ { 4 } ( f ) \rangle$ .Repeating the same steps as above,one finds again that the signal-to-noise ratio (always defined to be quadratic in the GW signal,in order to compare with the same quantity as in two-detector case) scales as $\sqrt { T }$

On the other hand,an advantage of multiple-detector correlations is that it might be casier to suppress correlated environmental noise, especially if the various detectors are|not close to each other.

# Correlated noise and signal chopping

Equation (7.239) shows that a true $\mathrm { G W }$ signal has a signature that in principle could allow us to distinguish it from the noise: increasing the observation time, the signal-to-noise ratio in the presence of a real GW signal must increase as T1/2.

Actually,this is a signature that only allows us to distinguish a stochastic GW background from uncorielated noise in the two detectors. Unfortunately,any residual correlated noise would still mimic the behaviorof areal GW signal. The problem is therefore how to make sure that correlated noise are negligible,and this can be a hard task,particularly for very long integration times.If two detectors are at the same site, or very close,their overlap reduction function is maximized,but we will certainly have correlated environmental noise.We have seen that the overlapreduction function suppresses the GW correlation if the detector separation is $\Delta x \gg \dot { x }$ .For instance,at $f = 5 0 ~ \mathrm { H z }$ ， $\dot { \bar { \lambda } } \simeq 1 0 0 0 \ \mathrm { k m }$ Most nvironmental disturbances will decorrelate on a much shorter lengthscale,so it is possible that two detectors at a suitable distance are stil correlated as far as the GW background is concerned,but they have megligible correlated noise.However,beyond a given sensitivity level, seismic noise or propagating electromagnetic disturbances might still give important correlated noise,and this is a difficult issue that will lave to be carefully studied experimentally.

An interesting option offered by the two-detector correlation is the posibility of chopping the signal. Chopping is a general term for measurements in which we switch our detector between the quantity that we want to measure and a reference quantity. It is a very powerful experimental technique,that exploits the fact that in many situations one can measure with a much better precision the variation of a quantity rather han the quantity itself because,taking the difference,many uncertain-

74The classcal example of this technique was the Dicke radiometer,which was developed by Dicke during World War II for application to microwave radars，and measured the radiation temperature of a radio source (i.e. the temperature of a black body having the same radio brightness).A direct measurement was difficult: the signal needed a large amplification,and fluctuations in the amplifer gain resulted in large errors.To overcome this difficulty，in the Dicke radiometer the receiver switches quickly between the source and a carefully calibrated black body,whose temperature was chosen to be of the order of the value expected for the source. To tell when these temperatures were equal was much easier than to obtain a direct determination of the source temperature. The same principle of comparing with a reference black body was used by the FIRAS spectrometer on board of the COBE satellite to measure the blackbody spectrum of CMB.To measure the CMB anisotropies,i.e. the variation of the black-body temperature over the sky,the principle used by the DMR detector on COBE and by the subsequent high-precision experiments such as WMAP is to compare the temperatures between two points in the sky.

ties,e.g.calibration uncertainties, cancel out.74 In particular,one ca compare the measurement in a situation where the signal is expected to the situation where a null answer should come out.

At first sight,it appears that a measurement of this type is imposi ble for a stochastic backgrounds of GWs,since the background is alway there,and gravitational forces cannot be screened.It seems therefore impossible to compare the output of a detector when no stochastic Gw background acts on it,with the output when the background is acting o it.Remarkably,this is no longer true when we consider a two-detectol correlation．In fact,changing the relative orientation of the two de tectors,the factor $\begin{array} { r } { \sum _ { A } F _ { 1 } ^ { A } ( \hat { \mathbf { n } } ) \vert F _ { 2 } ^ { A } ( \hat { \mathbf { n } } ) } \end{array}$ in eq. (7.226) changes,and it i therefore possible to modulate the signal. To illustrate this point,w compute $F _ { 1 2 }$ for a bar-interferometer correlation.Using Table 7.1 and eqs.(7.31) and(7.32)we see that,for $\psi$ generic,the pattern function of an interferometer are

$$
\begin{array} { r } { F _ { + } ^ { ( \mathrm { i n t f } ) } ( \theta , \phi ; \psi ) = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \cos 2 \psi - \cos \theta \sin 2 \phi \sin 2 \psi , } \\ { F _ { \times } ^ { ( \mathrm { i n t f } ) } ( \theta , \phi ; \psi ) = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \sin 2 \psi + \cos \theta \sin 2 \phi \cos 2 \psi . } \end{array}
$$

The pattern functions of the bar for $\psi$ generic can also be obtained from Table 7.1 and eqs.(7.31) and (7.32).We must however pay attention to the fact that in Table7.1,the variable denoted by $\theta$ for resonant bars is the angle measured from its longitudinal axis,while for an interferometer with arms along the $x$ and $y$ axes，we denoted by $\theta$ the polar angle measured from the $z$ axis,so these two angles are not the same unless the bar is vertical. If instead the bar lies in the $x , y$ plane,at an angle $\alpha$ with the $y$ axis,and we denbte by $\theta$ the polar angles measured from the $z$ axis,then the pattern fuhctions of the bar become

$$
\begin{array} { r l r } { { \cal F } _ { + } ^ { \mathrm { ( b a r ) } } ( \theta , \phi ; , \psi ) } & { = \left[ - \cos ^ { 2 } \theta \cos ^ { 2 } ( \phi - \alpha ) + \sin ^ { 2 } ( \phi - \alpha ) \right] \cos 2 \psi } & { } \\ { + [ \cos \theta | \sin 2 ( \phi - \alpha ) ] \sin 2 \psi } & { } \\ { { \cal F } _ { \times } ^ { \mathrm { ( b a r ) } } ( \theta , \phi ; , \psi ) } & { = \left[ - \cos ^ { 2 } \theta \cos ^ { 2 } ( \phi - \alpha ) + \sin ^ { 2 } ( \phi - \alpha ) \right] \sin 2 \psi } & { } \\ { - [ \cos \theta | \sin 2 ( \phi - \alpha ) ] \cos 2 \psi . } & { ( ) } \end{array}
$$

From this it follows that

$$
\int \frac { d \hat { \bf n } } { 4 \pi } \frac { d \psi } { 2 \pi } \sum _ { A } F _ { A } ^ { ( \mathrm { b a r } ) } F _ { A } ^ { ( \mathrm { i n t } \mathrm { \Delta } ) } = - \frac { 2 } { 5 } \cos 2 \alpha .
$$

(The overall sign of $F _ { 1 2 }$ is irrelevant since $\Gamma ( f )$ enters quadratically in the signal-to-noise ratio.） We see that the correlation is maximum when the bar is aligned with one of he interferometer arms (i.e. when $\alpha = 0$ or $\alpha = \pi / 2$ ).In contrast,when $\alpha = \pi / 4$ we have $F _ { 1 2 } = 0$ .Therefore in this configuration the signal obtained from the interferometer-bar corre lation vanishes.Even if GWs cannot be screened,the “composite detector” whose output is the correlation between a bar and an interferometer can be set in the “off source”position! We can then compare the result in this confguration with the result when the resonant bar is parallel to one of the interferometer arms,which is the position that maximizes the correlation. This chopping strategy has been used in the LIGO-ALLEGRO correlation． The ALLEGRO resonant bar (which has now terminated its activity) was located relatively close to the LIGO observatory in Livingston,and was mounted on a platform that allowed to rotate it easily. (After a rotation,data taking of good quality resumed in just half an hour.）The bar was therefore taken for a few months in the“off source”position,and then rotated to the“on source”position for a few more months.

# Further reading

·Fora textbook discussion of matched filtering and of detection of signals in noise see Wainstein and Zubakov (1962） and McDonough and Whalen (1995).For matched filtering and optimal signalto-noise ratio for GW bursts see Thorne (1987),and Saulson (1994),Chapter 4.Statistical aspects of parameter estimation are discussed in Finn (1992) and in Cutler and Flanagan (1994)，where the multiple detector case is also treated. Fora review of data analysis for interferometric GW detector see Viceré (2000).

·Books on probability and statistics typically cover many shelves in anyphysics library,and recommendation are very much subjective.Foran elementary but very practical introduction to statistics (tuned to the needs of particle physicists,but quite useful also in the GW context),see Lyons(1986).A concise and useful summary is given in the sections on probability and statisticsof the Review of Particle Properties,in Yao et al. [Particle Data Group] (2006).A very nice discussion of Bayesian vs. frequentist method,in the context of particle physics, is given in Cousins (1995).A discussion of the frequentist vs. Bayesian approach in the GW context is given in appendixA of Cutler and Flanagan (1994).

·The analysis of bursts of unknown shape using band-pass filtering is discussed ini Flanagan and Hughes (1998a，1998b)，in the context of the merging phase of black hole binaries.Timefrequency techniques are further discussed in Anderson and Balasubramanian (1999)，Anderson, Brady,Creighton and Flanagan (20oi) and Viceré (2002)．An algorithm based on clusters of pixels in the time-frequency domain (termed TFCLUS-TERS) is presented in Sylvestre (2002)．A book on the use of wavelets in physics is van den Berg (1999)．Application of wavelets to the analysis of GW bursts can be found in Klimenko,Yakushin, Rakhmanov and Mitselmakher (2004) and Klimenko and Mitselmakher (2004) (the WaveBurst algorithm).

·Some sources,such as accreting neutron or quark stars,as well as neutron stars stressed by large interior magnetic fields (magnetars),could emit repeatedly small bursts of GWs,with very characteristic correlations,both in energy and in time,among the different bursts,typical of systems displaying self-organized criticality. These correlations could give a further handle in their data analysis.These "GW bursters”are discussed in Coccia,Dubath and Maggiore (2004) and Dubath,Foffa,Gasparini, Maggiore and Sturani (2005).

· The search strategy for GW bursts using the three LIGO interferometers is discussed in Abbott et al. [LSC] (2004b)． The sensitivity of a network of interferometers for reconstructing the source position is studied in Gürsel and Tinto (1989)．Searches for GW bursts using coincidences between up to five resonant bars are described in Astone et al. [IGEC] (2003a)．Results with correlations among three bars,with improved sensitivities,are reported in Astone et al.[IGEC2] (2007).

·Introductory discussions of the search strategies for periodic signals can be found in Saulson (1994), Section 14.6 and Schutz (1991).More detailed analysis are given in Brady,Creighton,Cutler and

Schutz(1998)and in Brady and Creighton (2000). The application of the Hough transform to periodic GWs is discussed in Krishnan et al. (2004). A search for periodic GWs from a single specific Source,using the LIGO and GEO detectors, is described in Abbott et al.[LSC] (2004a). Limits on 28 isolated pulsar using the LIGO S2 run are given in Abbott et al.[LSC] (2005b).

· The importance of post-Newtonian corrections for the data analysis of coalescing binaries is emphasized in Cutler et al. (1993).Detailed discussions of data analysis procedure and parameter extraction for coalescences is given in Cutler and Flanagan (1994)，Poisson and Will (1995)，Kr6lak,Kokkotas and Schäfer (1995) and Flanagan and Hughes (1998a)．For computations of the waveform with the PN formalism,see the Further Reading section in Chapter 5.

· Optimal template placement for inspiraling compact binaries is discussed in Owen (1996) and Owen and Sathyaprakash (1999). A comparison of ten plates for binary inspiral is given in Damour,Iy and Sathyaprakash (20o1). A particularly usef family of templates for BH-BH inspiral have be proposed by Buonanno,Chen and Vallisneri (2003 A description of the LIGO search strategy for o alescehces can be found in Abbott et al. LSG (2005a).

· The optimal SNR in a two-detector corelatiot and the overlap reduction function are discussedi Michelson (1987)，Christensen (1992） and Flan gan (1993).A detailed discussion of signal proces ing strategies for stochastic backgrounds of GWsi given In Allen and Romano (1999). Signal choppin is discussed in Finn and Lazzarini (2001).Stocha tic backgrounds of GWs are reviewed in Maggion (2000).The search strategy of LIGO for stochasti backgtounds of GWs is discussed in Abbott et [LSC] (2004d) and (2005c).

# Resonant-mass detectors

The history of experimental GW physics began with resonant-mass detectors. The pioneer was Joseph Weber who,in the 196Os,developed the concept and built the first resonant bars.In the course of the subsequent four decades,resonant-mass detectors operated by various groups have reached sensitivities better than Weber's original bars by about four orders of magnitudes in energy.Still,we will see in this chapter that these sensitivities could allow the detection bf only relatively strong signals in our Galaxy or at most in our immediate galactic neighborhood, which are expected to be rare.To gain access to sources at large extragalactic distances it is necessary to build large interferometers,which will be the subject of the next chapter.

The passage from resonant detectors to interferometers implies a jump from“small-scale” experiments,performed by groups which can be as small as half a dozen people, to “Big Science”，with collaborations of hundreds of people and financial costs which are higher by factors $O ( 1 0 ^ { 2 } - 1 0 ^ { 3 } )$ . As we willsee in the next chapter,such a jump is justified by the formidable discovery potentialof interferometers and especially advanced interferometers.We nevertheless begin our discussion of experiments with resonant-mass detectors,both because they still have the possibility of detecting rare or unexpected events,and also because their study is instructive in itself. Our emphasis will be on aspects that have an intrinsic conceptual interest,such as understanding how a GW interacts with a macroscopic piece of matter,and on how it is possible to detect vibrations of a macroscopic body which are incredibly small,with amplitude many orders of magnitude smaller than the size of a nucleus. We will see that,by themselves,resonant detectors are remarkable instruments; it is possible to measure vibrations in a two-ton object,such as a typical bar,which corresponds to just a few tens of phonons,and variations $\Delta L$ of their length $L$ ,with $\Delta L / L \sim 1 0 ^ { - 1 9 } – 1 0 ^ { - 1 8 }$

# 8.1 The interaction of GWs with an elastic body

# 8.1.1 The response to bursts

A typical bar is a cylinder of length $L | \simeq 3 \ \mathrm { m }$ and radius $R \simeq 3 0 ~ \mathrm { c m }$ ,s0 in a first approximation we can treat its vibrations as one-dimensional. We orient the bar along the $x$ axis,with the end-faces at $\pm L / 2$ ,and we study the dynamics of a volume element $d V$ of the bar originally located

![](images/a740992f9661441012b18f29245ead156a351b10f693a9662d43ced6e59fee90.jpg)

8.1 The interaction of GWs   
with an elastic body 415   
8.2 The read-out system 427   
8.3 Noise sources 436   
8.4 Resonant spheres 459

at a position $x$ .In the properdetector frame introduced in Section 1.3.3 under the action of the GW this volume element will be displaced to new position $\boldsymbol { x } + \boldsymbol { u } ( t , \boldsymbol { x } )$ ,with $\ u ( t , x ) \ll x$ .In this section we consider th response to a GW burst of duration $\tau _ { g }$ much smaller than the relaxatid time of the bar.As we will \$ee in more detail later,fora typical ba this relaxation time is of order 6OO s,and the approximation $\tau _ { g } \ll 6 0 0$ s is excellent for astrophysical bursts,which can have $\tau _ { g } = O ( 1 )$ ms. this case we can neglect dissipative effects in the bar during the passag of the burst,and we know from elasticity theory1 that the longitudina elastic oscillations of the material are governed by a wave equation,

$$
d m \left( \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - v _ { s } ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } \right) = d F _ { x } ( t , x ) ,
$$

where dm is the mass of the volume $d V$ considered, $d F _ { x }$ is the $\boldsymbol { x }$ compo nent of the force exerted by the gravitational wave on the mass dm,an $\boldsymbol { v } _ { s }$ is the speed of sound in the material,related to the Young moduu $Y$ and to the density $\rho$ by $v _ { s } ^ { 2 } = Y / \rho$

Before proceeding with the formalism,we observe that eq. (8.1) appropriate only if the effect of GWs on the bar can be approximatel bya Newtonian force rather |than by the full equations of general rel ativity.We saw in Chapter $^ { 1 }$ that the effect of GWs on test masse can be approximated by a Newtonian force,and is expressed by tli equation of the geodesic deviation (1.95),only if the spatial separatiol between test masses (and therefore,in our case,the size $\boldsymbol { L }$ of the bar is much smaller than the typical scale of variation of the GWs,whichi turn is equal to the reduced wavelength $\dagger$ of the waves.Otherwise, expansion performed in the derivation of the equation of the geodesi deviation breaks down,and afull general relativistic treatment become necessary.As we will see in this chapter,the fundamental mode of tl bar resonates at the frequency $\omega _ { 0 } = \pi v _ { s } / L$ ,and the bar is sensitive t GWs with frequencies of the order of its resonance frequency. Then, relation between the length $\bar { L }$ of the bar and the reduced wavelengtl $\dagger$ of the GW that it searches is $L / \dot { x } \simeq \pi v _ { s } / c$ Of course,in any avail able material $\mathit { v } _ { s } \ll { c }$ .For instance,in aluminum at low temperatures $v _ { s } \simeq 5 . 4 ~ \mathrm { k m / s }$ and ${ \pi v _ { s } } / { c } \simeq \Theta \times 1 0 ^ { - 5 }$ . Therefore for resonant bars th approximation $L / \dot { \bar { x } } \ll 1$ is excellent and we can use the equation of the geodesic deviation to discuss their interaction with GWs.

Using eq.(1.95) we can write the Newtonian force in the proper de tector frame in terms of the expression of $h _ { i j }$ in the TT frame,

$$
d F _ { i } = \frac 1 2 \ddot { h } _ { i j } ^ { T T } x ^ { j } d m ,
$$

with $\boldsymbol { x } ^ { j } = \left( \boldsymbol { x } + \boldsymbol { u } , 0 , 0 \right)$ Singe $u = O ( h )$ ，to linear order in $h$ we can simply set $\boldsymbol { x } ^ { j } = ( x , 0 , 0 )$ onthe right-hand side of eq. (8.2). In this chapter the GW will always be expressed in the TT gauge and, to mak the notation lighter,we omit the label TT from $h _ { i j }$ .Then we hav $d F _ { x } ( t , z ) = ( 1 / 2 ) x \ddot { h } _ { x x } d m$ ,and eq.(8.1) becomes

$$
\frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } - v _ { s } ^ { 2 } \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } = \frac { 1 } { 2 } x \ddot { h } _ { x x } .
$$

The appropriate boundary conditions are

$$
\left( \frac { \partial u } { \partial x } \right) \bigg | _ { x = \pm L / 2 } = 0 ,
$$

and express the fact that there is no fux of elastic energy flowing outside the bar. Equations (8.3) and (8.4) determine the elastic deformation of the bar produced by the GW.Again from elasticity theory we know that the energy stored in the elastic deformations is given by

$$
E = \int d m \frac { 1 } { 2 } \left[ \left( \frac { \partial u } { \partial t } \right) ^ { 2 } + v _ { s } ^ { 2 } \left( \frac { \partial u } { \partial x } \right) ^ { 2 } \right] .
$$

The mode expansion compatible with|the boundary conditions (8.4)is

$$
u ( t , x ) = \sum _ { n = 0 } ^ { \infty } \xi _ { n } ( t ) \sin [ \frac { \pi x } { L } ( 2 n + 1 ) ] + \xi _ { n } ^ { \prime } ( t ) \cos [ \frac { \pi x } { L } ( 2 n + 2 ) ] .
$$

Substituting into eq. (8.3) we get

$$
\sum _ { n = 0 } ^ { \infty } [ \ddot { \xi } _ { n } + \omega _ { n } ^ { 2 } \xi _ { n } ] \sin [ \frac { \pi x } { L } ( 2 n + 1 ) ] + [ \ddot { \xi } _ { n } ^ { \prime } + \omega _ { n } ^ { \prime } { } ^ { 2 } \xi _ { n } ^ { \prime } ] \cos [ \frac { \pi x } { L } ( 2 n + 2 ) ] = \frac { 1 } { 2 } x \ddot { h } _ { x x } ,
$$

with

$$
\omega _ { n } = \frac { \pi v _ { s } } { L } ( 2 n + 1 ) , \qquad \left| \omega _ { n } ^ { \prime } = \frac { \pi v _ { s } } { L } ( 2 n + 2 ) \ . \right.
$$

Using the orthogonality relations

$$
\begin{array} { l } { { \displaystyle \int _ { - L / 2 } ^ { L / 2 } d x ~ { \sin } [ \frac { \pi x } { L } ( 2 n + 1 ) ] { \sin } [ \frac { \pi x } { L } ( 2 m + 1 ) ] = \frac { L } { 2 } \delta _ { n , m } , \hfill } } \\ { { \displaystyle \int _ { - L / 2 } ^ { L / 2 } d x ~ { \sin } [ \frac { \pi x } { L } ( 2 n + 1 ) ] { \cos } [ \frac { \pi x } { L } ( 2 m + 2 ) ] = 0 , \hfill } } \end{array}
$$

we find from eq. (8.7)

while

$$
\begin{array} { c } { { \displaystyle \ddot { \xi } _ { n } + \omega _ { n } ^ { 2 } \xi _ { n } = \frac 1 L \ddot { h } _ { x x } \int _ { - L / 2 } ^ { L / 2 } \left. d x x \sin [ \frac { \pi x } L ( 2 n + 1 ) ] \right. } } \\ { { { } } } \\ { { { } = \displaystyle \frac { ( - 1 ) ^ { n } } { ( 2 n + 1 ) ^ { 2 } } \ \frac { 2 L } { \pi ^ { 2 } } \ddot { h } _ { x x } , } } \\ { { { } } } \\ { { { } \ddot { \xi } _ { n } ^ { \prime } + \omega _ { n } ^ { \prime } { } ^ { 2 } \xi _ { n } ^ { \prime } = \displaystyle \frac 1 L \ddot { h } _ { x x } \int _ { - L / 2 } ^ { L / 2 } \left. d x x \cos [ \frac { \pi x } L ( 2 n + 1 ) ] \right. } } \\ { { { } } } \\ { { { } = 0 . } } \end{array}
$$

The latter integral vanishes because the integrand is odd under $x \to - x$ and therefore the modes $\xi _ { n } ^ { \prime }$ do not couple to GWs.2 We now restrict to the fundamental mode $\xi _ { n }$ with $n = 0$ ，whose dynamics is governed by the equation

$$
\ddot { \xi } _ { 0 } + \omega _ { 0 } ^ { 2 } \xi _ { 0 } = \frac { 2 L } { \pi ^ { 2 } } \ddot { h } _ { x x } ,
$$

2Physically this can be understood re calling，from Section 1.3.1,that the equation of the geodesic deviation de scribes displacements from a fixed point $x \ = \ 0$ .Therefore,by definition，the volume element located at the origin does not move.In the case of a bar this means that,as long as we are interested only in its response to GWs, we can further impose the boundary condition $\xi ( x = 0 , t ) = 0$ The function $\sin [ \pi x ( 2 n + 1 ) / L ]$ satisfies it and therefore the modes $\xi _ { n } ( t )$ are allowed, while $\cos [ \pi x ( 2 n + 2 ) / L ]$ does not vanish at $x = 0$ and therefore $\xi _ { n } ^ { \prime } ( t ) = 0$ Of course,this result is specific to the form (8.2) of the force exerted by GWs. More specifically, it is a consequence of the spin-2 nature of the gravitational field,which is described by a traceless symmetric tensor with two indices hTT, so to obtain $d F _ { i }$ we are forced to saturate one index with $x ^ { j }$

with

$$
\omega _ { 0 } = \frac { \pi v _ { s } } { L } .
$$

To obtain the elastic energy of this mode we replace $u ( t , x )$ in eq. (8.5) with $\xi _ { 0 } ( t ) \sin ( \pi x / L )$ .For a uniform bar of mass $M$ we have $d m =$ $( M / L ) d x$ ,and we can perform the integral over $\boldsymbol { \mathscr { X } }$ ,obtaining

$$
E = \frac { M } { 4 } ( \dot { \xi } _ { 0 } ^ { 2 } + \omega _ { 0 } ^ { 2 } \xi _ { 0 } ^ { 2 } ) .
$$

3This value of the effective mass simply reflects the normalization of the normal modes.Here we have chosen $\sin [ \pi x ( 2 n + 1 ) / L ]$ as normal modes, which are normalized as in eq. (8.9). If we rather choose as normal modes $\Psi _ { n } = \sqrt { 2 } \sin [ \pi x ( 2 n + 1 ) / L ]$ and we expand $\begin{array} { r } { { \boldsymbol u } ( { \boldsymbol x } , t ) ~ = ~ \sum _ { n } { \boldsymbol a } _ { n } ( t ) \Psi _ { n } ( { \boldsymbol x } ) } \end{array}$ ，then $\xi _ { n } ( t ) = \sqrt { 2 } a _ { n } ( t )$ and the effective mass of $a _ { n } ( t )$ is $M$ rather than $M / 2$ In Section 8.4,when we discuss resonant spheres,we will in fact adopt the latter normalization.

$^ 4 \mathrm { S e e }$ e.g.Landau and Lifshitz, Vol.I (1976),eq. (22.12).

Equations (8.13) and (8.15) show that the fundamental mode of a thi cylindrical bar of mass $M$ and length $L$ is formally identical toa har monic oscillator with frequency $\omega _ { 0 }$ and mass $m _ { 0 } = M / 2$ ，driven by force $F ( t ) = ( 2 / \pi ^ { 2 } ) m _ { 0 } L \ddot { h } _ { x x }$ .Comparing with eq. (8.3),we see that thi istheforceexerted byGWsonaoscilltorwithanfeivemass m and an effective length $l = ( 4 / \pi ^ { 2 } ) L$

An oscillator of mass $m _ { 0 }$ subject to an external impulsive force $F ($ absorbs from it an energy $E _ { s }$ (the label $s$ stands for“signal"） given by

$$
E _ { s } = \frac { 1 } { 2 m _ { 0 } } \bigg \| \int _ { - \infty } ^ { \infty } d t F ( t ) e ^ { - i \omega _ { 0 } t } \bigg \| ^ { 2 } .
$$

The energy transferred to the fundamental mode of the bar by a GW burst is obtained using $F ( t ) = ( 2 / \pi ^ { 2 } ) m _ { 0 } L \ddot { h } _ { x x }$ with $m _ { 0 } = M / 2$ ，s0

$$
E _ { s } = \frac { M L ^ { 2 } } { \pi ^ { 4 } } \left| \int _ { - \infty } ^ { \infty } d t \ddot { h } _ { x x } ( t ) e ^ { - i \omega _ { 0 } t } \right| ^ { 2 } .
$$

By definition,a burst is described by a function $h ( t )$ which goes to zero very fast at $t \to \pm \infty$ .We can therefore integrate by part twice the above expression,and we get

$$
\begin{array} { l } { \displaystyle { E _ { s } = \frac { M L ^ { 2 } ( 2 \pi f _ { 0 } ) ^ { 4 } } { \pi ^ { 4 } } \left| \int _ { - \infty } ^ { \infty } d t h _ { x x } ( t ) e ^ { - i 2 \pi f _ { 0 } t } \right| ^ { 2 } } } \\ { \displaystyle { \phantom { \frac { M L ^ { 2 } ( 2 \pi f _ { 0 } ) ^ { 4 } } { \pi ^ { 4 } } } = 1 6 M L ^ { 2 } f _ { 0 } ^ { 4 } | \tilde { h } _ { x x } ( f _ { 0 } ) | ^ { 2 } . } } \end{array}
$$

5Observe that this relation is completely independent of the shape of the burst，and $E _ { s }$ depends only on the Fourier component of the GW at the bar's resonance frequency $f _ { 0 }$ This is a consequence of the fact that the duration of the burst $\tau _ { g }$ is much smaller than the dissipation time so,as far as the absorption of energy from a burst is concerned,the resonance can be considered infinitely narrow.

Therefore the value of $| \tilde { h } _ { x x } ( f _ { 0 } ) | ^ { 2 }$ can be obtained measuring the energy $E _ { s }$ deposited in the bar,5

$$
\overline { { | \tilde { h } _ { x x } ( f _ { 0 } ) | } } = \frac { 1 } { 4 L f _ { 0 } ^ { 2 } } \sqrt { \frac { E _ { s } } { M } } .
$$

It is interesting to see how an elastic bar,once excited bya GW,evolves in time.If we are interestedin the long-time behavior of the signal we must take into account that the energy $E _ { s }$ absorbed by the bar will be slowly dissipated by internal frictions.As we mentioned before, this dissipation takes place on a time-scale of about $6 0 0 ~ \mathrm { s } .$ ，which is much longer than the duration of aburst.Therefore,while the absorption of energy froma GW burst is extremely well described by eq.(8.13),to study the subsequent time development of the signal we must generalize this equation to

$$
\ddot { \xi } _ { 0 } + \gamma _ { 0 } \dot { \xi } _ { 0 } + \omega _ { 0 } ^ { 2 } \xi _ { 0 } \vert = \frac { 2 L } { \pi ^ { 2 } } \ddot { h } _ { x x } ,
$$

where $\gamma _ { 0 }$ describes the effect of dissipation on the mode $\xi _ { 0 }$ A very important parameter is the quality factor of the bar (or,more precisely, of the mode $\xi _ { 0 }$ ） $Q _ { 0 }$ ,defined by6

$$
Q _ { 0 } = \frac { \omega _ { 0 } } { \gamma _ { \uparrow } } .
$$

Experimentally, values of $Q _ { 0 }$ of order $\mathsf { b } \times \mathsf { 1 0 ^ { 6 } }$ (and even up to $2 \times 1 0 ^ { 7 }$ ） are obtained in bars at cryogenic temperatures,which corresponds, for $f _ { 0 } \sim 9 0 0 ~ \mathrm { H z }$ ,to a relaxation time $1 / \gamma _ { \mathrm { 0 } } ^ { } \sim 6 0 0 \mathrm { s }$

Equation (8.20)is easily solved going in Fourier space,

$$
\dot { \zeta } _ { 0 } ( \omega ) = { T } _ { 0 } ( \omega ) \tilde { h } _ { x x } ( \omega ) ,
$$

where7

$$
T _ { 0 } ( \omega ) = { \frac { 2 L } { \pi ^ { 2 } } } { \frac { \omega ^ { 2 } } { \omega ^ { 2 } + \omega _ { 0 } ^ { 2 } + i \gamma _ { 0 } \omega } }
$$

is called the transfer function for the imode $\xi _ { 0 }$ .The form of $| T _ { 0 } ( \omega ) | ^ { 2 }$ is shown in Fig.8.1. We write $\omega ^ { 2 } - \omega _ { 0 } ^ { 2 } + i \gamma _ { 0 } \omega = ( \omega - \bar { \omega } _ { + } ) ( \omega - \bar { \omega } _ { - } )$ with

$$
\bar { \omega } _ { \pm } = \pm \sqrt { \omega _ { 0 } ^ { 2 } - ( \gamma _ { 0 } / 2 ) ^ { 2 } } - i \frac { \gamma _ { 0 } } { 2 } .
$$

In a typical bar $\gamma _ { 0 }$ is smaller than $\omega _ { 0 }$ by a factor $Q _ { 0 } = O ( 1 0 ^ { 6 } )$ so the second term in the square root is completely negligible and

$$
\bar { \omega } _ { \pm } \simeq \pm \omega _ { 0 } \Bigl | \bar { i } \frac { \gamma } { 2 } . \Bigr |
$$

Then eq. (8.22) gives

$$
\xi _ { 0 } ( t ) = \frac { 2 L } { \pi ^ { 2 } } \int _ { - \infty } ^ { \infty } \frac { d \omega } { 2 \pi } \frac { \omega ^ { 2 } \tilde { h } _ { x x } ( \omega ) } { ( \omega - \bar { \omega } _ { + } ) ( \omega - \bar { \omega } _ { - } ) } e ^ { - i \omega t } .
$$

As an example, we consider the case of a Dirac delta perturbation,

$$
\begin{array} { r } { h _ { x x } ( t ) = h _ { 0 } \ d \tau _ { g } \delta ( t ) . } \\ { \qquad \quad \mathrm { ~ } } \end{array}
$$

As discussed below eq. (7.99),this carl be taken as a crude description of a burst of amplitude $h _ { 0 }$ and duration $\tau _ { g }$ .For the Dirac delta perturbation, the Fourier transform $\tilde { h } _ { x x } ( \omega ) \stackrel { } { = } h _ { 0 } \tau _ { g }$ is a constant and

$$
\xi _ { 0 } ( t ) = { \frac { 2 L } { \pi ^ { 2 } } } h _ { 0 } \tau _ { g } \int _ { - \infty } ^ { \infty } \frac { d \omega } { 2 \pi } \frac { \omega ^ { 2 } } { ( \omega - \bar { \varphi } _ { + } ) ( \omega - \bar { \omega } _ { - } ) } e ^ { - i \omega t } .
$$

For $t < 0$ we can close the contour in the upper half-plane and, since $\bar { \omega } _ { \pm }$ both lies below the real axis,see eq. (8.24),we get zero,as required by causality. For $t > 0$ we close the contour in the lower half-plane,where we pick the contribution of the two poles at $\omega = \bar { \omega } _ { \pm }$ ,and we get

$$
\xi _ { 0 } ( t ) \simeq - \frac { 2 L } { \pi ^ { 2 } } h _ { 0 } \omega _ { 0 } \tau _ { g } e ^ { - \gamma _ { 0 } t / 2 } \sin \omega _ { 0 } t .
$$

We therefore have damped oscillations,and we see that,even if the GW burst lasts only a few ms,the bar continues to ring for a very long time, of order $1 0 ~ \mathrm { m i n }$

6In later sections we will meet other quality factors,like that of the transducer，or the total mechanical quality factor of the bar-transducer system. To avoid confusion，we denote by $Q _ { 0 }$ (rather than simply by $Q$ ，asusually done in the literature) the quality factor of the mode $\xi _ { 0 }$

7The sign of the factor $i \gamma _ { 0 } \omega$ depends onour conventions on the Fourier transform (see the Notation).Often in the literature the opposite convention on the Fourier transform is used, $\begin{array} { r } { F ( t ) = \int [ d \omega / ( 2 \pi ) ] \tilde { F } ( \omega ) e ^ { + i \omega t } } \end{array}$ and then $T _ { 0 } ( \omega ) = ( 2 L / \pi ^ { 2 } ) \omega ^ { 2 } / ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } - i \gamma _ { 0 } \omega )$

![](images/ed5eec35096255a24f82f0ee5bdf793ae299a18f226f74ad0a057b4db23e8a50.jpg)  
Fig.8.1 The logarithm of the function $| ( \pi ^ { 2 } / 2 L ) T _ { 0 } ( \omega ) | ^ { 2 }$ ,against $\omega / \omega _ { 0 }$ ， for $Q _ { 0 } = 1 0 ^ { 3 }$

# 8.1.2 The response to periodic signals

We have seen that the fundamental mode of a resonant bar has an in trinsic time-scale $\tau _ { 0 } = 1 / \gamma _ { 0 } \sim 1 0 \ \mathrm { m i n }$ ，which is the time on whichif dissipates its elastic energy due to internal frictions.GW bursts haw a typical duration of the orderof the ms,and therefore dissipatione fectsare completely negligible as long aswe are interested in the tota energy absorbed from the GWlFor this reason,we could compute tli energy absorbed by the bar duringa burst setting $\gamma _ { 0 } = 0$ ，and the basic equation (8.19) is independent of $\gamma _ { 0 }$

For a periodic signal at the resonant frequency $\omega _ { 0 }$ the situation different.Operatively,a periodic signal is just a wave-packet with fre quencies around the resonant frequency $\omega _ { 0 }$ of the bar,sufficiently narro in frequency space,so that its temporal duration is much longer thal $1 / \gamma _ { 0 } \simeq 1 0$ min.In the limiting case of an exactly monochromatic waw the temporal duration of the signal becomes infinite.If an ideal har monic oscillator,with no losses,is driven by an exactly periodic foro at its resonant frequency,its amplitude (and therefore the energy it ab sorbs) grows indefinitely. In a real harmonic oscillator there is a dampin force proportional to $\gamma _ { 0 } \dot { \xi } _ { 0 }$ which becomes larger and larger as $\dot { \xi } _ { 0 }$ grows until the losses become so large that they compensate for the energ absorbed by the external source.At this point a stationary regime i reached.

To study the response of the fundamental mode of the bar to periodi signals we must therefore use eq.(8.2O).We consider a wave propagatin along the $z$ axis,

$$
h _ { x x } ( t ) = h _ { 0 } \mathrm { R e } \left[ e ^ { - i \omega ( t - z / c ) } \right] ,
$$

where $h _ { 0 }$ is a real constant and Re denotes the real part. The barl located in the plane $z = 0$ ，s0

$$
\ddot { \xi } _ { 0 } + \gamma _ { 0 } \dot { \xi } _ { 0 } + \omega _ { 0 } ^ { 2 } \xi _ { 0 } = - \frac { 2 L h _ { 0 } \omega ^ { 2 } } { \pi ^ { 2 } } \mathrm { R e } \left[ e ^ { - i \omega t } \right] ,
$$

and a particular solution of this inhomogeneous equation is

$$
\begin{array} { l } { { \displaystyle \xi _ { 0 } ( t ) = \frac { 2 L h _ { 0 } \omega ^ { 2 } } { \pi ^ { 2 } } \operatorname { R e } \left[ \frac { e ^ { - i \omega t } } { \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } + i \gamma _ { 0 } \omega } \right] } } \\ { { \displaystyle = \frac { 2 L h _ { 0 } \omega ^ { 2 } } { \pi ^ { 2 } } \frac { ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) \cos \omega t - \gamma _ { 0 } \omega \sin \omega t } { ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } \omega ^ { 2 } } . } } \end{array}
$$

The energy of this solution is|found from eq. (8.15).If $\omega = \omega _ { 0 }$ it time-independent,and is given by

$$
\begin{array} { c } { { E = \displaystyle \frac { { \cal M } } { 4 } ( \dot { \xi } _ { 0 } ^ { 2 } + \omega _ { 0 } ^ { 2 } \xi _ { 0 } ^ { 2 } ) } } \\ { { = \displaystyle \frac { 1 } { \pi ^ { 4 } } { \cal M } L ^ { 2 } h _ { 0 } ^ { 2 } \omega _ { 0 } ^ { 2 } Q _ { 0 } ^ { 2 } , } } \end{array}
$$

where $Q _ { 0 } = \omega _ { 0 } / \gamma _ { 0 }$ . This shows that eq.(8.32) describes an equilibrium state where the energy absorbed by the wave is compensated by the losses due to friction. For an ideal oscillator, $Q _ { 0 }  \infty$ and therefore $E  \infty$ .A bar which initially is not excited and which is then hit by a wave-packet centered around $\omega _ { 0 }$ ,with a spread of frequencies $\Delta \omega \ll \omega _ { 0 }$ ， reaches asymptotically this solution after a transient time of order $1 / \gamma _ { 0 }$ At $\omega = \omega _ { 0 }$ eq.(8.32） becomes

$$
\xi _ { 0 } ( t ) = - \frac { 2 L } { \pi ^ { 2 } } \frac { h _ { 0 } \omega _ { 0 } } { \gamma _ { 0 } } \sin \omega _ { 0 } t .
$$

Comparing this with the situation inwhich the bar is hit by a Dirac delta excitation,eq.(8.29) we see that,frst ofall,there is no exponential decay $\exp \{ - \gamma _ { 0 } t / 2 \}$ ,since the periodic wave continuously feeds energy into the bar,compensating for the internal losses.And,second,the overall amplitude is much larger since $\tau _ { g } \sim 1$ ms is now replaced by $1 / \gamma _ { 0 } \sim 6 0 0 ~ \mathrm { s }$ Physically this is clearly understood:a burst excites the bar only for the short time $\tau _ { g }$ ,while under a periodic perturbation the amplitude of the oscillation keeps increasing for a time $1 / \gamma _ { 0 }$ ,until the rate of losses due to dissipation becomeequal to the rate at which energy is feed in by the GW,and an equilibrium regime is established.

# 8.1.3 The absorption cross-section

Equation (8.32) in principle characterizes completely the response of a bar to a monochromatic wave.However,it is instructive to express this result in terms of the cross-section of the bar for GW absorption.8 The power absorbed by an oscillator with velocity $\dot { \xi } _ { 0 }$ subject to a force $F ( t )$ is $F ( t ) \dot { \xi } _ { 0 }$ . In our case,recalling that the effective mass of the mode $\xi _ { 0 }$ is $M / 2$ ,the force is

$$
\begin{array} { l } { { \displaystyle { \cal F } = \frac { M } { 2 } \frac { 2 L } { \pi ^ { 2 } } \ddot { h } _ { x x } } } \\ { { \displaystyle ~ = - \frac { M L h _ { 0 } \omega ^ { 2 } } { \pi ^ { 2 } } \cos \omega t } , } \end{array}
$$

md,using eq. (8.32),

8We limit ourselves for the moment to a wave with pure $^ +$ polarization, propagating in a direction perpendicular to the bar.See page 425 for the most general result.

$$
F ( t ) \dot { \xi } _ { 0 } = 2 M \left( \frac { L h _ { 0 } \omega ^ { 2 } } { \pi ^ { 2 } } \right) ^ { 2 } \frac { \omega ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) \sin \omega t \cos \omega t + \gamma _ { 0 } \omega ^ { 2 } \cos ^ { 2 } \omega t } { ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } \omega ^ { 2 } } .
$$

Since the energy of the incoming waves is defined as an average over several cycles，we are more interested in the average power absorbed over a cycle,

$$
\begin{array} { r l r } {  { \frac { d E _ { \mathrm { a b s } } } { d t } \equiv \langle F ( t ) \dot { \xi } _ { 0 } \rangle } } \\ & { } & { = \frac { M L ^ { 2 } h _ { 0 } ^ { 2 } } { \pi ^ { 4 } } \frac { \gamma _ { 0 } \omega ^ { 6 } } { ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } \omega ^ { 2 } } . } \end{array}
$$

I particular,at the resonance frequency

$$
\frac { d E _ { \mathrm { a b s } } } { d t } = \frac { 1 } { \pi ^ { 4 } } M L ^ { 2 } h _ { 0 } ^ { 2 } \omega _ { 0 } ^ { 3 } Q _ { 0 } .
$$

Comparing with eq.(8.33) we see that at the resonant frequency (a once we have reached the statidnary regime,where the solution for ab initially at rest approaches (8.32)) $d E _ { \mathrm { a b s } } / d t = \gamma _ { 0 } E$ .Of course $d E _ { \mathrm { a b s } }$ depends both on the properties of the bar and on the intensity of i incoming radiation.A quantity that characterizes uniquely the detecta is the absorption cross-section $\sigma _ { \mathrm { a b s } } ( \omega )$ ，defined by

$$
\frac { d E _ { \mathrm { a b s } } } { d t } = \sigma _ { \mathrm { a b s } } ( \omega ) \frac { d E _ { \mathrm { i n } } } { d A d t } ,
$$

where $\omega$ is the frequency of the incoming monochromatic wave and I is the incoming energy, so $d E _ { \mathrm { i n } } / d A d t$ is the energy arriving per unit tin onaunit area,againaveraged overa few cycles,aswe always do fortl energy of a wave.We consider a GW propagatingalong the $z$ direction with $h _ { + } = h _ { x x } = h _ { 0 } \cos \omega t$ and $h _ { \times } = 0$ .Then,using eq. (1.155),

$$
\frac { d E _ { \mathrm { i n } } } { d A d t } = \frac { c ^ { 3 } h _ { 0 } ^ { 2 } \omega ^ { 2 } } { 3 2 \pi G } ,
$$

(where we used $\langle \cos ^ { 2 } \omega t \rangle = 1 / 2$ ),and therefore

$$
\sigma _ { \mathrm { a b s } } ( \omega ) = \frac { 3 2 \gamma _ { 0 } G M L ^ { 2 } } { \pi ^ { 3 } c ^ { 3 } } \frac { \omega ^ { 4 } } { ( \omega ^ { 2 } - \omega _ { 0 } ^ { 2 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } \omega ^ { 2 } } .
$$

9Numerically， setting $M \ = \ 2 2 7 0 \ \mathrm { k g } .$ $L = 3 \mathrm { ~ m ~ }$ $f _ { \mathrm { 0 } } = 1 ~ \mathrm { k H z }$ and $Q = 1 0 ^ { 6 }$ we get $\sigma _ { \mathrm { a b s } } ( \omega _ { 0 } ) \simeq 3 \times 1 0 ^ { - 1 8 } \mathrm { c m } ^ { 2 }$ ，which can be written as $\sigma _ { \mathrm { a b s } } ( \omega _ { 0 } ) = \pi r ^ { 2 }$ ,with $r \simeq 1 0 ^ { - 9 }$ cm.It is amusing to see that, evcn at the resonance,the cross-section for absorption of GWs of a whole twoton bar is of order of the cross-section of a hard sphere (i.e.a sphere that absorbs with unit probability everything that arrives within its radius $\boldsymbol { r }$ ）with a typical atomic size.This reflects of course the weakness of the gravitational interaction.

At the resonance frequency we have9

$$
\sigma _ { \mathrm { a b s } } ( \omega _ { 0 } ) = \frac { 3 2 G M L ^ { 2 } \omega _ { 0 } Q _ { 0 } } { \pi ^ { 3 } c ^ { 3 } } .
$$

The cross-section at resonance, however, is not really the best indicatd of the detector sensitivity. Consider for instance a wave-packet who Fourier modes $\tilde { h } ( \omega )$ are approximately constant over a narrow interv $\omega _ { 1 } < \omega < \omega _ { 2 }$ which includes the resonance frequency of the bar $\omega _ { 0 }$ Tl response of a bar to this wave-packet is determined by the integral d the cross-section

$$
\int _ { \omega _ { 1 } } ^ { \omega _ { 2 } } \frac { d \omega } { 2 \pi } \sigma ( \omega ) .
$$

Since the cross-section is peaked around the resonance frequency $\omega _ { 0 }$ ,t0 compute this integral we can approximate $\sigma ( \omega )$ using

$$
\frac { \omega ^ { 4 } } { ( \omega - \omega _ { 0 } ) ^ { 2 } ( \omega + \omega _ { 0 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } \omega ^ { 2 } } \simeq \frac { \omega _ { 0 } ^ { 2 } } { 4 ( \omega - \omega _ { 0 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } } .
$$

10Observe that we extended the integral from $- \infty$ to $+ \infty$ .The error that we are introducing is negligible because the contribution to the integral from the region $| \omega - \omega _ { 0 } | \gg \gamma _ { 0 }$ is very small. For the same region,the detailed form of the incoming wave-packet is not important.

This approximation is the leading term in an expansion in $\gamma _ { 0 } / \omega _ { 0 } = 1 / Q _ { 0 }$ Since Qo >1,toa very good accuracy we have10

$$
\int _ { \omega _ { 1 } } ^ { \omega _ { 2 } } \frac { d \omega } { 2 \pi } \sigma ( \omega ) \simeq \frac { 3 2 \gamma _ { 0 } G M \dot { L } ^ { 2 } } { \pi ^ { 3 } c ^ { 3 } } \int _ { - \infty } ^ { \infty } \frac { d \omega } { 2 \pi } \frac { \omega _ { 0 } ^ { 2 } } { 4 ( \omega - \omega _ { 0 } ) ^ { 2 } + \gamma _ { 0 } ^ { 2 } } .
$$

Then, to leading order in $1 / Q _ { 0 }$ ,we find

$$
\begin{array} { c } { { \displaystyle \Sigma _ { 0 } \equiv \left| \int _ { - \infty } ^ { \infty } \frac { d \omega } { 2 \pi } \sigma _ { \mathrm { a b s } } ( \omega ) \right. } } \\ { { \displaystyle \qquad = \frac { 8 G M L ^ { 2 } \omega _ { 0 } ^ { 2 } } { \pi ^ { 3 } c ^ { 3 } } . } } \end{array}
$$

Using eq. (8.14) we can express $\omega _ { 0 }$ in terms of the speed of sound in the material, $\omega _ { 0 } = \pi v _ { s } / L$ ,and then

<table><tr><td>£</td><td>8GM = T</td><td>（Us） C C</td><td>2</td></tr></table>

This shows that the result depends only on the mass $M$ of the bar,and on the speed of sound in the material. Numerically, for an aluminum bar with mass M= 2270 kg,£0 ≈4.4 ×10-21cm² Hz.11

Observe that the integrated cross-section is independent of $Q _ { 0 }$ ，because the peak value of $\sigma ( \omega )$ is proportional to $Q _ { 0 }$ ,but such a large value is obtained only over a range $\Delta \omega \sim 1 / Q _ { 0 }$ ，SO $Q _ { 0 }$ cancels in $\int d \omega \sigma ( \omega )$ More precisely,from the explicit expressions we see that the integrated cross-section is related to the cross-section at the peak by

$$
\Sigma _ { 0 } = \frac { \gamma _ { 0 } } { 4 } \sigma _ { \mathrm { a b s } } ( \omega _ { 0 } ) .
$$

Naively,one might then think that the value of $Q _ { 0 }$ is not relevant for the performance of the detector.Howeverwhat really matters for detection is the ratio between the signal and the noise.In Section 8.3 we will discuss the possible sources of noise and we will appreciate the importance of having a large $Q _ { 0 }$

We will see below that,despite the fact that a resonant bar is a macroscopic object,weighting more than two tons,one is able to detect bar's oscillations which are so small that $\dot { \mathfrak { a } }$ classical treatment is no longer adequate,and it is instead appropriate to describe them in terms of the number of phonons that are excited.12 It is therefore instructive to verify that the cross-section (8.46) is recovered in a quantum treatment of the fundamental mode $\xi _ { 0 }$

We have seen that the variable $\xi _ { 0 }$ describes a harmonic oscillator of mass $m _ { 0 } = M / 2$ and frequency $\omega _ { 0 }$ .According to the standard rules of quantum mechanics,we promote it to an operator and we write

$$
\xi _ { 0 } = \left( \frac { \hbar } { M \omega _ { 0 } } \right) ^ { 1 / 2 } \left( a + a ^ { \dagger } \right) ,
$$

with $a , a ^ { \dagger }$ the creation and annihilation operators,and $[ a , a ^ { \dagger } ] = 1$ (compare with eqs.(8.171) and (8.172) below). The free Hamiltonian of the quantum oscillator is given by the familiar expression $H _ { 0 } = \hbar \omega _ { 0 } ( a ^ { \dag } a +$ $1 / 2 )$ and acts on the harmonic oscillator states labeled by $| n \rangle$ . In a quantum field theory interpretation,the state vector $| n \rangle$ describes a collection of $\boldsymbol { \eta }$ phonons,each one with frequency $\omega _ { 0 }$ .To compute the cross-section we study the interaction of this quantum harmonic oscillator with the classical external force given in eq. (835),13

$$
\begin{array} { r } { \dot { F } ( t ) = - ( 1 / \pi ^ { 2 } ) M L h _ { 0 } \omega ^ { 2 } \cos \omega t . } \end{array}
$$

We define the interaction Hamiltonian from $F = - \partial H _ { \mathrm { i n t } } / \partial \xi _ { 0 }$ In the quantum treatment the interaction Hamiltonian is then

11Usingeq. (8.),itigo to repeat the above computation for the $n$ -th longitudinal mode $\xi _ { n }$ ofthe bar.Its resonance frequency is $\begin{array} { r l } { \omega _ { n } } & { { } = } \end{array}$ $( 2 n + 1 ) \omega _ { 0 }$ ，and for the cross-section, integrated around $\omega _ { \mathscr { n } }$ ，weget

$$
\Sigma _ { n } = \frac { 1 } { ( 2 n + 1 ) ^ { 2 } } \Sigma _ { 0 } .
$$

Thus,the first excited mode of the bar which couples to GWs ( $\xi _ { n }$ with $n = 1$ is ata frequency $f _ { 1 } ~ = ~ 3 f _ { 0 }$ ，andits integrated cross-section $\Sigma _ { 1 }$ is smaller bya factor of 9 compared to the integrated cross-section $\Sigma _ { 0 }$ of the fundamental mode.

$^ { 1 2 } \mathrm { I n }$ particular,we willdiscuss inSec tions 8.3.3 and 8.3.4 that the ultimate limitation of resonant bars,unless one uses quantum non-demolition techniques,is given by the so-called “standard quantum limit",where we are detecting single-phonon transitions induced by the GW.

13Any detectable GW isexceedingly classical, so we only need to use a quantum description for the oscillator.

$$
H _ { \mathrm { i n t } } = { \frac { 1 } { \pi ^ { 2 } } } M L h _ { 0 } \omega ^ { 2 } \xi _ { 0 } \cos \omega t
$$

$$
= \frac { 1 } { \pi ^ { 2 } } ( M L h _ { 0 } \omega ^ { 2 } \cos { \omega t } ) \left( \frac { \hbar } { M \omega _ { 0 } } \right) ^ { 1 / 2 } \left( a + a ^ { \dagger } \right) .
$$

We assume that before the afrival of the GW the oscillator $\xi _ { 0 }$ is in its ground state $| 0 \rangle$ .To first order in perturbation theory,the interaction Hamiltonian (8.52) induces transitions to the state |1),with a transition amplitude

$$
\begin{array} { c } { { T _ { 0 \to 1 } = - \displaystyle \frac { i } { \hbar } \int _ { - \infty } ^ { \infty } d t \displaystyle e ^ { - i \omega _ { 0 } t } \langle 1 | H _ { \mathrm { i n t } } | 0 \rangle } } \\ { { = - i \displaystyle \frac { { \cal M } L h _ { 0 } \omega _ { 0 } ^ { 2 } } { 2 \pi ^ { 2 } ( \hbar M \omega _ { 0 } ) ^ { 1 / 2 } } 2 \pi \delta ( \omega - \omega _ { 0 } ) , } } \end{array}
$$

where we have taken $\omega _ { 0 } > 0 , \omega > 0$ .The probability that a transition takes place at any time is $| \mathcal { T } _ { 0  1 } | ^ { 2 }$ .We regularize the time interval restricting to $- T / 2 < t < T / 2$ ,and therefore the transition rate is

$$
\operatorname * { l i m } _ { T  \infty } \frac { 1 } { T } | T _ { 0  1 } | ^ { 2 } = \frac { M L ^ { 2 } h _ { 0 } ^ { 2 } \omega _ { 0 } ^ { 3 } } { 2 \pi ^ { 3 } \hbar } \delta ( \omega - \omega _ { 0 } ) ,
$$

where we used the fact that,on afinite time nterval $- T / 2 < t < T / 2$

$$
2 \pi \delta ( \omega ) = \int _ { - T / 2 } ^ { T / 2 } d t e ^ { i \omega T } ,
$$

and therefore 2πδ(w = O)=Tl In each transition is absorbedan energy $\hslash \omega _ { 0 }$ ,therefore the energy absqrbed per unit time is

$$
\frac { d E _ { \mathrm { a b s } } } { d t } = \frac { M L ^ { 2 } h _ { 0 } ^ { 2 } \omega _ { 0 } ^ { 4 } } { 2 \pi ^ { 3 } } \delta ( \omega - \omega _ { 0 } ) .
$$

$F ( t )$

$$
\sigma _ { \mathrm { a b s } } = { \frac { 3 2 G M L ^ { 2 } f _ { 0 } ^ { 2 } } { \pi c ^ { 3 } } } \delta ( f - f _ { 0 } ) .
$$

Of course， having neglected the decay width of the excited quantum state,the cros-section is a Dirac delta rather than a curve with the Breit-Wigner shape (8.41). Tp compare with the clasical calculation, it is simpler to consider the integral of gabs around the resonance,and from eq. (8.57) we get

$$
\int d f \sigma _ { \mathrm { a b s } } = { \frac { 3 2 G M L ^ { 2 } f _ { 0 } ^ { 2 } } { \pi c ^ { 3 } } } ,
$$

in agreement with eq. (8.46).It is not difficult to check that the same result is obtained if the initial state of the oscilator is a generic state $| n \rangle$ rather than $| 0 \rangle$ .(Observe that in this case the quantity relevant for the absorption of energy is $| T _ { n  n + 1 } | ^ { 2 } - | T _ { n  n - 1 } | ^ { 2 } )$

# Angular sensitivity and pattern functions

We have seen that the output of a resonant bar with its axis along the $\scriptstyle { \mathcal { X } }$ direction is determined by the valuelof $h _ { x x } ( t )$ .More generally,if we denote by1 the unit vector in the direction of the longitudinal axis of the bar,the scalar output is $h ( t ) = \hat { l } ^ { i } \hat { l } ^ { j } h _ { i j } ( t )$ . Comparing with eq. (7.1) we see that the detector tensor of the bar is

$$
D ^ { i j } = { \hat { l } } ^ { i { \hat { l } } j } .
$$

Since $h _ { i j }$ is traceless,we can equivalently choose to define $D ^ { i j }$ in the traceless form $D ^ { i j } = \hat { l } ^ { i } \hat { l } ^ { j } - ( 1 / 3 ) \delta ^ { i j }$ .We now compute the pattern functions,defined in Section 7.1, for a cylindrical bar. The geometry is illustrated in Fig.8.2. We denote by $\hat { \bf n }$ the unit vector in the propagation direction of the GW，with polar angles $( \theta , \phi )$ .We use as polar axis the longitudinal axis of the bar, $\operatorname { s o } \ \theta$ is the angle between $\hat { \bf n }$ and the $x$ axis and,because of the cylindrical symmetry of the bar,we can take $\phi = 0$ without loss of generality.In Fig.8.2,we have a reference frame $( x , y , z )$ ,where the bar is along $\scriptstyle { | x | }$ axis and the $y$ axis is perpendicular to the plane of the page,in the downward direction． Since we have set $\phi = 0$ 、the source is in the $( x , z )$ plane.We introduce a second reference frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ such that the propagation direction $\hat { \bf n }$ of the GW coincides with the $z ^ { \prime }$ axis,and the $y ^ { \prime }$ axis is parallel to the $y$ axis. Therefore the plane defined by the $( x , z )$ axis is the same as the plane defined by the $( x ^ { \prime } , z ^ { \prime } )$ axes (and is the plane of the page).The $( x , z )$ axes are obtained from the $( x ^ { \prime } , z ^ { \prime } )$ axis performing a counterclockwise rotation by an angle $\alpha = ( \pi / 2 ) - \theta$ around the $y$ axis. In the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame the GW has the form

$$
h _ { i j } ^ { \prime } = \left( \begin{array} { c c c } { { h _ { + } } } & { { h _ { \times } } } & { { 0 } } \\ { { h _ { \times } } } & { { - h _ { + } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { i j } ,
$$

where $h _ { + , \times }$ are defined with respect to the $( x ^ { \prime } , y ^ { \prime } )$ axes.To find the form of this GW in the $( x , y , z )$ frame,we must compute how this tensor transforms under the rotation that brings the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame onto the $( x , y , z )$ frame.This rotation is described by the matrix

$$
\mathcal { R } = \left( \begin{array} { c c c } { { \cos \alpha } } & { { \emptyset } } & { { \sin \alpha } } \\ { { 0 } } & { { \bot } } & { { 0 } } \\ { { - \sin \alpha } } & { { \emptyset } } & { { \cos \alpha } } \end{array} \right) ,
$$

with $\sin \alpha = \cos \theta$ and $\cos \alpha = \sin \theta .$ The components of the tensor $h _ { i j }$ in the $( x , y , z )$ frame are obtained| from the components $h _ { i j } ^ { \prime }$ in the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame by $h _ { i j } = \mathcal { R } _ { i k } \mathcal { R } _ { j l } h _ { k l } ^ { \prime }$ Then

$$
\begin{array} { r l } & { h _ { x x } = \mathcal { R } _ { 1 k } \mathcal { R } _ { 1 l } h _ { k l } ^ { \prime } } \\ & { \quad \quad = h _ { + } [ ( \mathcal { R } _ { 1 1 } ) ^ { 2 } - ( \mathcal { R } _ { 1 2 } ) ^ { 2 } ] + 2 h _ { \times } \mathcal { R } _ { 1 1 } \mathcal { R } _ { 1 2 } } \\ & { \quad \quad = h _ { + } \sin ^ { 2 } \theta . } \end{array}
$$

Then we find $F _ { + } ( \hat { \mathbf { n } } ; \psi = 0 ) = \sin ^ { 2 } { \theta }$ and $F _ { \times } ( \hat { \mathbf { n } } ; \psi = 0 ) = 0$ .The label $\upsilon = 0$ in $F _ { + , \times }$ refers to the fact that these are the values of the pattern

![](images/308e17f138c8c61d8f17274507d79eaa89cad99f025fc3bd8637e078e7235e08.jpg)  
Fig.8.2 The relation between the $( x , y , z )$ and the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ reference frames.