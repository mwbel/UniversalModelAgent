![](images/6a1af05197d9b27730abd6d65b9f7283c79c35297f8e3ac56292a0e04f79dbc7.jpg)  
Fig. 1.1 The deformation of a ring of test masses due to the $^ +$ and $\times$ polarization.

The resulting deformation of a ring of test masses located in the $( x , y )$ plane is shown in Fig.1.1. From eq.(1.96) we see that

$$
\partial _ { i } F _ { i } = { \frac { m } { 2 } } \ddot { h } _ { i j } ^ { \mathrm { T T } } \delta _ { i j } ,
$$

$$
\delta y ( t ) = \frac { h _ { \times } } { 2 } x _ { 0 } \sin \omega t .
$$

勿八

$h _ { i j } ^ { \mathrm { T T } }$ is Thus,the Neweonian tre $\mathbf { \nabla } \nabla \cdot \mathbf { F } \ = \ 0$ representation of $\mathbf { F }$ drawing its lines of force in the $( x , y )$ plane (defined so that at each point $( x , y )$ they go in the direction of the force,and their density is proportional to the modulus $| \mathbf { F } |$ of the force). The condition $\mathbf { \nabla } \nabla \cdot \mathbf { F } = 0$ then implies that there are no sources nor sinks for the field lines, just as for the magnetic field in classical electrodynamics. The lines of force in the $( x , y )$ plane obtained from eq. (1.96),for the $h _ { + }$ and for the $h _ { \times }$ polarization, are shown in Figs. 1.2 and 1.3. The symmetry axes of these lines of force have a typical quadrupolar pattern,with the shape of a $^ +$ and of ${ \mathrm {  ~ a ~ } } \times { \mathrm {  ~ s i g n ~ } }$ ,respectively,and this is the origin of the denominations “plus” and “cross” polarizations. Observe that Fig.1.3 is obtained from Fig.1.2 by performing a rotation of 45 degrees, in agreement with eqs. (1.49) and (1.50).

![](images/92222aef19cf6665becf00e4d6335ea4d97690580206d4c98b75f912d9133229.jpg)  
Fig.1.2 The lines of force corresponding to the $^ +$ polarization.The arrows show the direction of the force when sin wt is positive.The force reverses when sin wt is negative.   
Fig.1.3 The lines of force corresponding to the $\times$ polarization.

# 1.4 The energy of GWs

Our next task is to understand the energy and momentum carried by gravitational waves. The fact that GWs do indeed carry energy and momentum is already clear from the discussion of the interaction of GWs with test masses presented above. We have seen that,in the proper detector frame,an incoming GW sets in motion a ring of test masses initially at rest (and, in fact, the action of the waves on nearby test masses can even be described in terms of a Newtonian force,see eq. (1.96), so GWs impart kinetic energy to these masses.If, for instance,we connect these masses together with a loose spring with friction,this kinetic energy will be dissipated into heat. Thus,GWs can do work,and conservation of energy requires that the kinetic energy acquired by the test masses must necessarily come from the energy of the GWs. To get the explicit expression of the energy-momentum tensor of GWs we can follow two different routes,one more geometrical and the other more field-theoretical:

(1） Since,according to general relativity，any form of energy contributes to the curvature of space-time,we can ask whether GWs are themselves a source of space-time curvature.   
(2) We can treat linearized gravity as any other classical field theory, and apply Noether's theorem,the standard field-theoretical tool that answers this question.

In this section we pursue the former approach,while in Section 2.1 we discuss the latter,and we will see that they both lead to the same answer.

# 1.4.1 Separation of GWs from the background

To discuss whether GWs curve the background space-time we must broaden our setting.Until now,we have linearized the Einstein equations expanding around the flat metric $\eta _ { \mu \dot { \psi } }$ . In this setting the definition of GWs is relatively clear: the background space-time is fat,and the small fuctuations around it have been called “gravitational waves”.The terin “waves” is justified by the fact that,inasuitable gauge, $h _ { \mu \nu }$ indeed satisfies a wave equation.However,to study whether GWs generate a curvature,we cannot define them as perturbation over the flat metric I, otherwise we exclude from the beginning the possibility that GWs curve the background space-time.Rather,we must allow the background space-time to be dynamical,which means that we would like to define GWs as perturbations over some curved,dynamical, background metric ${ \hat { g } } _ { \mu \nu } ( x )$ ,and write16

$$
g _ { \mu \nu } ( x ) = \bar { g } _ { \mu \nu } ( x ) + h _ { \mu \nu } ( x ) , \qquad \mid h _ { \mu \nu } \mid \ll 1 .
$$

However,a problem arises immediately. How do we decide which part of $g _ { \mu \nu }$ is the background and which is the fluctuations? In principle,in cq.(1.106) we can move $x$ -dependent terms from $h _ { \mu \nu }$ to $\bar { g } _ { \mu \nu }$ or viceversa. The problem did not arise in linearized theory，where the background Inetric was chosen once and for all to be the constant flat-space metric $1 1 \mu \mu$ ,

As we wil see in this section,this problem is not just an abstract issue of principle. On the contrary, the answer to this question allows us to understand properties of GWs such as their energy-momentum tensor, and to get rid of ambiguities concerning whether GWs can be “gauged away” or not.

In the most general setting,there is no unambiguous way to perform a separation of the type (1.106). The total metric $g _ { \mu \nu } ( x )$ can receive conributions which change,in space and in time,on all possible scales due, tor example,to the time-varying Newtonian gravitational fields of nearby masses in movement.The situation is quite similar to that of waves in he sea.In principle, there is no unambiguous way to state which part of the vertical movement of the surface of the water belongs to a given wave,and which part belongs to a “background”originated by the incoherent superposition of perturbations bf varied origin． Nevertheless, there are obviously situations where a description of the perturbation ofthe sea surface in terms of waves is useful,at least at the level of an effective description.

In particular,a natural splitting between the space-time background and gravitational waves arises when there is a clear separation of scales. For example,a natural distinction occursif,in some coordinate system, we can write the metric as in eq.(1.106)where $\hat { g } _ { \mu \nu }$ has a typical scale

16The condition |hμvl < 1 assumes that we are using a coordinate system where the diagonal elements of $\bar { g } _ { \mu \nu }$ are $O ( 1 )$ ，on the region of space-time in which we are interested.

![](images/110e5d009bf04aea9e66eeb1b1bf80373554ad7a55be995193ec39e3d27eee56.jpg)  
Fig.1.4 A situation that alows us to separate the metric into a low-frequency background and a small high-frequency perturbation. The background is defined as the part with frequencies $f \ll { \bar { f } }$ and the GW as the part with $f \ \bar { \gg } \ \bar { f }$ This definition is largely independent of the precise value of $\bar { f }$

of spatial variation $L _ { B }$ , on top of which small amplitude perturbations are superimposed,characterized by a wavelength $\lambda$ such that

$$
\begin{array} { r } { \dot { { \boldsymbol { \lambda } } } \ll L _ { B } , } \end{array}
$$

where $\dot { \lambda } = \lambda / ( 2 \pi )$ is the reduced wavelength.17 In this case $h _ { \mu \nu }$ has the physical meaning of small ripples on a smooth background.Alternatively,a natural distinction can be made in frequency space,if $\bar { g } _ { \mu \nu }$ has frequencies up to a maximum value $f _ { B }$ ，while $h _ { \mu \nu }$ is peaked around a frequency $f$ such that

$$
f \gg f _ { B } .
$$

In this case $h _ { \mu \nu }$ is a high-frequency perturbation of a static or slowly varying background. The situation (1.108) is illustrated in Fig. 1.4. We will see below that in this case $h _ { \mu \nu }$ ， in a suitable gauge, obeys a wave equation,and as a consequence its characteristic wavelength and frequency, $\lambda$ and $f$ ，are related by $\lambda = c / f$ However, the scales $L _ { B }$ and $f _ { B }$ that characterize the background are a priori unrelated, so the conditions (1.107) and (1.108) are independent,and it suffices that one of them be satisfied.

We can now ask two questions:

· How this high-frequency (or short wavelength) perturbation propagates in the background space-time with metric $\bar { g } _ { \mu \nu }$ . The answer to this question will justify the fact that the perturbation $h _ { \mu \nu }$ is called a gravitational “wave”.   
· How this perturbation affects the background metric itself. The answer to this question will allow us to assign an energy-momentum tensor to GWs.

In the next subsections we will address these two questions.First we remark that,traditionally,the separation of the metric into a smooth background plus fluctuations is discussed using the condition (1.107), and the method is called the short-wave expansion. It should be observed,however,that from the point of view of GW detectors,the condition (1.108) is fulfilled instead.Consider for instance a GW with a frequency $f \sim 1 0 ^ { 2 } { - } 1 0 ^ { 3 } \mathrm { H z }$ ,corresponding to a reduced wavelength $\hbar \simeq$ $5 0 0 { - } 5 0 ~ \mathrm { k m }$ ，which are typical GWs that can be searched by groundbased detectors. The Earth's gravitatibnal potential is not spatially smooth over a scale of tens of kms,compared to the GW perturbation. On the contrary, fuctuations in the metric due to local density variations,mountains,etc.are many orders of magnitude bigger than the expected GWs: the Newtonian gravitational potential at the surface of the Earth is in fact $| h _ { 0 0 } | = 2 G \bar { M _ { \oplus } } / ( R _ { \oplus } c ^ { 2 } ) \sim \bar { 1 0 ^ { - 9 } }$ , while, as we will see, GWs arriving on Earth are expected to have at most $h \sim 1 0 ^ { - 2 1 }$ so even a spatial variation of just one part in $1 0 ^ { 1 2 }$ due to local inhomogeneities, s large compared to the expected GWs.

On the other hand, these Newtonian gravitational fields are essentially static,and it is much more difficult to find important temporal variations at large frequency scales, e.g. at $f \sim 1 ~ \mathrm { { k H z } }$ ,since it requires relatively arge masses moving at these frequencies.A distinction between background and gravitational waves based on the condition $f \gg f _ { B }$ becomes herefore possible.

Indeed,ground-based GW detectors have a size which is much smaller han the wavelength of the GWs that they are searching.A GW with frequency $f \sim 1 0 ^ { 2 } – 1 0 ^ { 3 } \mathrm { H z }$ has a reduced wavelength $\hphantom { 0 } { \chi } \sim 5 0 0 { - } 5 0 \mathrm { k m }$ ,which s much bigger than the size of the detedtor. Therefore,GW detectors do not monitor spatial variations of thegravitational field on lengthscales $L \gg \ast$ .Rather,their output is a time series,which is analyzed in Fourier space looking for temporal variations in their output induced by passing GW.As we will see in Chapter 9,after suitable isolation, the tesidual noise due to seismic motion and Newtonian gravitational fields Bimportant only at lower frequencies,say below $O ( 1 0 )$ Hz.Therefore, we are actually searching for fast temporal variations in the detector butput due to GWs,over a background which is slowly varying in time.

# 1.4.2How GWs curve the background

We therefore consider the situation in which,in some reference frame, we can separate the metric into a background plus fuctuations,as in 4. (1.106),and this separation is based on the fact that there is a clear listinction of scales either in space,in which case eq. (1.107) applies,or time,in which case eq. (1.108) appliesl

As discussed above,our aim is to understand how the perturbation u propagates,and how it affects the background space-time. To adiress these questions,we begin by expanding the Einstein equations fround the background metric $\bar { g } _ { \mu \nu }$ . In the expansion we have two small Mrameters: one is the typical amplitude $h \equiv { \cal O } ( | h _ { \mu \nu } | )$ ,and the second is either $\scriptstyle \sum / L _ { B }$ or $f _ { B } / f$ ,depending on whether eq.(1.107) or eq.(1.108) applies. The situation in which $\dot { \bar { \lambda } } / L _ { B } \ll 1$ and the situation in which $f _ { B } / f \ll 1$ can be treated in parallel,with the appropriate change of notation,and we will refer generically to both cases as the short-wave expansion.

As a first step, we expand to quadratic order in $h _ { \mu \nu }$ . It is convenient to cast the Einstein equations in the form

$$
R _ { \mu \nu } = \frac { 8 \pi G } { c ^ { 4 } } \left( T _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } T \right) ,
$$

where $T _ { \mu \nu }$ is the energy-momentum tensor of matter and $T$ its trace, and then we expand the Ricci tensor to $O ( h ^ { 2 } )$ ，

$$
R _ { \mu \nu } = \bar { R } _ { \mu \nu } + R _ { \mu \nu } ^ { ( 1 ) } + R _ { \mu \nu } ^ { ( 2 ) } + \ldots ,
$$

18To be more precise, we should take into account that $\ddot { R } _ { \mu \nu }$ is non-linear in $\bar { g } _ { \mu \nu }$ If $\bar { k }$ separates the low frequency from the high frequency modes，then $\bar { g } _ { \mu \nu }$ has only modes up to a typical wave-vector $k _ { B } \simeq 2 \pi / L _ { B }$ with $k _ { B } \ \ll$ $\bar { k }$ The Christoffel symbols of the background are quadratic in the background metric and therefore have modes up to $2 k _ { B }$ .Terms quadratic in the Christoffel symbols,such as those which appear in the definition of the Ricci tensor, therefore have modes up to $\sim 4 k _ { B }$ Inany case,if the separation of scales between the background and the GW is clearcut,we still have $4 k _ { B } ~ \ll ~ \bar { k }$ .In this sense $\bar { R } _ { \mu \nu }$ contains only low-frequency modes.

where $\bar { R } _ { \mu \nu }$ is constructed with $\hat { g } _ { \mu \nu }$ only，, $R _ { \mu \nu } ^ { ( 1 ) }$ is Iinear in $h _ { \mu \nu }$ and $R _ { \mu \nu } ^ { ( 2 ) }$ is quadratic in $h _ { \mu \nu }$ .The crucial observation now is the following. The quantity $\bar { R } _ { \mu \nu }$ is constructed from $\bar { g } _ { \mu \nu }$ and therefore contains only lowfrequency modes.18 $R _ { \mu \nu } ^ { ( 1 ) }$ bydefinition is liner in and therefore containsonlyhgh-requencymodes $R _ { \mu \nu } ^ { ( 2 ) }$ isquadratiein $h _ { \mu \nu }$ and therefore contains both high and low frequencies: for instance,in a quadratic term $\sim h _ { \mu \nu } h _ { \rho \sigma }$ a mode with a high wave-vector $\mathbf { k } _ { 1 }$ from $h _ { \mu \nu }$ can combine with a mode with a high wave-vector ${ \bf k } _ { 2 } \simeq - { \bf k } _ { 1 }$ from $h _ { \rho \sigma }$ to give a low wave-vector mode. Therefore the Einstein equations can be split into two separate equations for the low- and high-frequency parts,

$$
\bar { R } _ { \mu \nu } = - [ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { L o w } } + \frac { 8 \pi G } { c ^ { 4 } } \left( T _ { \mu \nu } - \frac 1 2 g _ { \mu \nu } T \right) ^ { \mathrm { L o w } } ,
$$

and

$$
R _ { \mu \nu } ^ { ( 1 ) } = - [ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { H i g h } } + { \frac { 8 \pi G } { c ^ { 4 } } } \left( T _ { \mu \nu } - { \frac { 1 } { 2 } } g _ { \mu \nu } T \right) ^ { \mathrm { H i g h } } .
$$

The superscript “Low”denotes the projection on the low momenta (i.e. long wavelengths） or on the low frequencies，depending on whether eq.(1.107) or eq.(1.108)applies,and similarly for the superscript“High".

The explicit expression for $R _ { \mu \nu } ^ { ( 1 ) }$ is computed in Problem 1.1,and is

$$
R _ { \mu \nu } ^ { ( 1 ) } = { \frac { 1 } { 2 } } \left( \bar { D } ^ { \alpha } \bar { D } _ { \mu } h _ { \nu \alpha } + \bar { D } ^ { \alpha } \bar { D } _ { \nu } h _ { \mu \alpha } - \bar { D } ^ { \alpha } \bar { D } _ { \alpha } h _ { \mu \nu } - \bar { D } _ { \nu } \bar { D } _ { \mu } h \right) ,
$$

where $\bar { D } _ { \mu }$ is the covariant derivative with respect to the background metric. At quadratic order one finds, after some long algebra,

$$
\begin{array} { c } { { { \displaystyle R _ { \mu \nu } ^ { ( 2 ) } = \frac { 1 } { 2 } \bar { g } ^ { \rho \sigma } \bar { g } ^ { \alpha \beta } \left[ \frac { 1 } { 2 } \bar { D } _ { \mu } h _ { \rho \alpha } \bar { D } _ { \nu } h _ { \sigma \beta } + ( \bar { D } _ { \rho } h _ { \nu \alpha } ) ( \bar { D } _ { \sigma } h _ { \mu \beta } - \bar { D } _ { \beta } h _ { \mu \sigma } ) \right. } } } \\ { { { \displaystyle \left. + h _ { \rho \alpha } ( \bar { D } _ { \nu } \bar { D } _ { \mu } h _ { \sigma \beta } + \bar { D } _ { \beta } \bar { D } _ { \sigma } h _ { \mu \nu } - \bar { D } _ { \beta } \bar { D } _ { \nu } h _ { \mu \sigma } - \bar { D } _ { \beta } \bar { D } _ { \mu } h _ { \nu \sigma } ) \right. } } } \\ { { { \displaystyle \left. + ( \frac { 1 } { 2 } \bar { D } _ { \alpha } h _ { \rho \sigma } - \bar { D } _ { \rho } h _ { \alpha \sigma } ) ( \bar { D } _ { \nu } h _ { \mu \beta } + \bar { D } _ { \mu } h _ { \nu \beta } - \bar { D } _ { \beta } h _ { \mu \nu } ) \right] . ( 1 . } } } \end{array}
$$

In the next subsections we will closely examine eqs. (1.1l1) and (1.112). We will see that,from eq. (1.111),we can understand what the energymomentum tensor of GWs is,while eq.(1.112) is a wave equation that describes the propagation of $h _ { \mu \nu }$ on the|background space-time.

First we discuss,from the vantage point of the expansion over a generic curved background,why the expansion qver flat space-time presented in Section 1.1 cannot be promoted to a systematic expansion. Consider first the situation in which there is no|external matter, $T _ { \mu \nu } = 0$ In eqs.(1.111) and (1.1l2) we have equated terms of different orders in the $h .$ expansion. The reason is that wehave a second small expansion parameter, which is $\dot { \lambda } / L _ { B }$ （or $f _ { B } / f$ ；as usual, the two cases can be treated in parallel with just a change of notation,and for definiteness ${ \mathrm { w e u s e } } \dot { \lambda } / L _ { B } , $ ,which can compensate for the smallness in $h$ .The relative strength of these parameters is therefore fixed by the Einstein equations themselves. We use the notation $h = O ( | h _ { \mu \nu } | )$ ,while we take $\bar { g } _ { \mu \nu } = O ( 1 )$ in a limited region of space,we can always set $\bar { g } _ { \mu \nu } = { \cal O } ( 1 )$ with a suitable rescaling of the coordinates).

Since we set $T _ { \mu \nu } = 0$ ,we see from eq.(1.111) that $\bar { R } _ { \mu \nu }$ is determined mlyby $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { L o w } }$ rt $R _ { \mu \nu } ^ { ( 2 ) }$ $1 5$ a sum of terms of order $( \partial h ) ^ { 2 }$ and of terms of order $h \partial ^ { 2 } h$ Let us anficipate that,when we compute the projection onto the low modes,these wo terms give contributions which are of the same order of magnitude, and one finds that $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { L o w } }$ is of order $( \partial h ) ^ { 2 }$ (compare with eqs. (1.125) and (1.133) below)． Then,in order of magnitude,eq.(1.11l） in the Absence of matter fields reads

md expresses the fact that the derivatives of the perturbation $h _ { \mu \nu }$ affect the curvature of the background metric $\bar { g } _ { \mu \nu }$ .The scale of variation of $j _ { \mu \nu }$ is $L _ { B }$ ,while that of $h$ is $\dagger$ ；therefore,in order of magnitude,

$$
\partial \bar { g } _ { \mu \nu } \sim \frac { 1 } { L _ { B } } ,
$$

recall that we took $\bar { g } _ { \mu \nu } = { \cal O } ( 1 ) $ ，while

$$
\partial h \sim { \frac { h } { \dot { \frac { \ d h } { \ d t } } } } .
$$

Since the background curvature $\bar { R } _ { \mu \nu }$ is constructed from the second Jerivatives of the background metric,eq.(1.116) implies that

$$
\bar { R } _ { \mu \nu } \sim \partial ^ { 2 } \bar { g } _ { \mu \nu } \not \sim \frac { 1 } { L _ { B } ^ { 2 } } .
$$

hile eq. (1.117) gives $( \partial h ) ^ { 2 } \sim ( h / \Dot { x } ) ^ { 2 }$ Therefore eq.(1.115) gives the melation

$$
\frac { 1 } { L _ { B } ^ { 2 } } \sim \left( \frac { h } { \bar { \lambda } } \right) ^ { 2 } ,
$$

that is,

$$
h \sim \frac { \mathfrak { X } } { L _ { B } } ,
$$

Consider now the opposite limit where $T _ { \mu \nu }$ is non-vanishing,and the contribution of GWs to the background curvature is negligible compared to the contribution of matter sources.In this case the total background curvature will be much bigger than the contribution of GWs, $1 / L _ { B } ^ { 2 } \sim$ $h ^ { 2 } / \chi ^ { 2 } +$ (matter contribution) $\gg h ^ { 2 } / { \chi } ^ { 2 }$ ,i.e.

19In special cases one can find exact wave-like solutions of the full nonlinear Einstein equations,see,e.g. Misner,Thorne and Wheeler (1973),Section 35.9,and then there is no need to perform a separation between the background and the waves.However,it would be hopeless to look for exact solutions for the gravitational waves emitted by realistic astrophysical sources.

At this point we can understand why the linearized approximation of Section 1.1 cannot be extended beyond linear order.If we force the background metric to be $\eta _ { \mu \nu }$ ,we are actually forcing $1 / L _ { B }$ to be strictly equal to zero,and therefore any arbitrarily small,but finite,value of $h$ necessarily violates the condition $h \lesssim \mathfrak { X } / L _ { B }$ ,and the expansion in powers of $h$ has no domain of validity. This means that the linearized expansion of the classical theory cannot be promoted to a systematic expansion, and if we want to compute higher-order corrections we cannot insist on a flat background metric.

$$
h \ll { \frac { \lambda } { L _ { B } } } , { ( \mathrm { c u r v a t u r e ~ d e t e r m i n e d ~ b y ~ m a t t e r } ) } .
$$

We can also understand from eqs.(1.120) and (1.121) that the notion of GW is well defined only for small amplitudes, $h \ll 1$ If $h$ becomes of order one,eqs.(1.120) and (1.121) tellus that $\scriptstyle \sum \int L _ { B }$ also becomes at least of order one. Since the separation between $\boldsymbol { \lambda }$ and $L _ { B }$ is at the basis of the definition of GWs,when $h$ becomes of order one the distinction between GWs and background vanishes. In a general context, there is nothing like“a GW of arbitrary amplitude”.19

We consider now eq. (1.111). When there is a clear-cut separation between the length-scale $\boldsymbol { \lambda }$ of the GWs and the length-scale $L _ { B }$ of the background,there is a simple way to perform the projection on the longwavelength modes: we introduce a scale $\bar { l }$ such that $\lambda \ll \bar { l } \ll L _ { B }$ ,and we average over a spatial volume with side $\bar { \boldsymbol { l } }$ In this way,modes with a wavelength of order $L _ { B }$ remain unaffected, because they are basically constant over the volume used for the averaging,while modes with a reduced wavelength of order $\boldsymbol { \lambda }$ are oscillating very fast and average to zero.Similarly, if $h _ { \mu \nu }$ is a high-frequency perturbation of a quasi-static background, we can introduce a time-scale $\bar { t }$ which is much larger than the period $1 / f$ of the GW and much smaller than the typical time-scale $1 / f _ { B }$ of the background,and average over this time $\bar { t }$ ,i.e.over several periods of the GW. We can therefore write eq. (1.111) as

$$
\bar { R } _ { \mu \nu } = - \langle R _ { \mu \nu } ^ { ( 2 ) } \rangle + { \frac { 8 \pi G } { c ^ { 4 } } } \langle T _ { \mu \nu } - { \frac { 1 } { 2 } } g _ { \mu \nu } T \rangle ,
$$

where $\langle . . . \rangle$ denotes a spatial average over many reduced wavelengths $\dagger$ if eq. (1.i07) applies, and a temporal average over several periods $1 / f$ of the GW,if rather eq. (1.108) applies.

In the context of general relativity and gravitational-wave physics, the usefulness of introducing some averaging procedure was understood in the 1960s.To put it into a broader theqretical framework,it is useful to realize that what we have done is basically a special case of a general technique,which is known as a renormalization group transformation, and which is nowadays one of the most important tools both in quantum field theory and in statistical physics. The basic idea is to start from the fundamental equations of a theory and to “integrate out”the fuctuations that take place on a length-scale smaller than $l$ ,in order to obtainan effective theory that describes the physics at the length-scale I. These renormalization group transformations can be performed in coordinate space,which is the language that we used above; in momentum space,integrating out the high-momentum modes,in order to get the corresponding low-energy effective action；or in frequency space,in order to eliminate the fast temporal variations and to obtain the effective dynamics of the slowly varying degrees of freedom.

We now define an effctive energy-momentum tensor of matter,that we denote by ${ \bar { T } } ^ { \mu \nu }$ ,from

$$
\langle T _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } T \rangle = \bar { T } ^ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } \bar { T } ,
$$

where $\bar { T } = \bar { g } _ { \mu \nu } \bar { T } ^ { \mu \nu }$ is the trace.By definition, ${ \bar { T } } ^ { \mu \nu }$ is a purely lowfrequency (or low-momentum) quantity,and is a smoothed form of the matter energy-momentum tensor $T _ { \mu \nu }$ ； for instance,when the separation has been done on the basis of the condition $\dot { \lambda } \ll L _ { B }$ ,we can visulize it as a“macroscopic”(with respect to the scale $\ddagger$ ）version of the nergy-momentum tensor, while $T _ { \mu \nu }$ is the fundamental（“microscopic") quantity.20

We also define the quantity $t _ { \mu \nu }$ as

$$
t _ { \mu \nu } = - \frac { c ^ { 4 } } { 8 \pi G } \langle R _ { \mu \nu } ^ { ( 2 ) } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } R ^ { ( 2 ) } \rangle ,
$$

where

$$
R ^ { ( 2 ) } = \bar { g } ^ { \mu \nu } R _ { \mu \nu } ^ { ( 2 ) } ,
$$

md we define its trace $\mathsf { a s } ^ { 2 1 }$

$$
\begin{array} { l } { { t = \bar { g } ^ { \mu \nu } t _ { \mu \nu } } } \\ { { \displaystyle ~ = + \frac { c ^ { 4 } } { 8 \pi G } \langle R ^ { ( 2 ) } \rangle . } } \end{array}
$$

D go from the first to the_second line,in eq. (1.127)，we used the lact that $\bar { g } ^ { \mu \nu } \langle R _ { \mu \nu } ^ { ( 2 ) } \rangle = \langle \bar { g } ^ { \mu \nu } R _ { \mu \nu } ^ { ( 2 ) } \rangle$ since ${ \bar { g } } ^ { \mu \nu }$ by definition isa purely lowtrequency quantity, as well as the obvious identity $\bar { g } ^ { \mu \nu } \bar { g } _ { \mu \nu } = 4$ .Inserting 4.(1.127) into eq. (1.125) (and using again the fact that $\bar { g } _ { \mu \nu }$ is constant Inder the averaging procedure, so $\langle \breve { g } _ { \mu \nu } { \breve { R } } ^ { ( 2 ) } \rangle = \bar { g } _ { \mu \nu } \langle R ^ { ( 2 ) } \rangle \big )$ we see that

$$
- \langle R _ { \mu \nu } ^ { ( 2 ) } \rangle = \frac { 8 \pi G } { c ^ { 4 } } \left( t _ { \mu \nu } \Big | - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } t \right) .
$$

20In a typical situation,the fundamental energy-momentum tensor $T ^ { \mu \nu }$ generated by a macroscopic matter distribution will already be quite smooth,so it will be approximately constant on the scale used for averaging. In this case

$$
\begin{array} { l } { { \langle T _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } g _ { \mu \nu } T \rangle \simeq T _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } \langle g _ { \mu \nu } \rangle T } } \\ { { \mathrm { } } } \\ { { \mathrm { } = T _ { \mu \nu } - \displaystyle \frac { 1 } { 2 } \bar { g } _ { \mu \nu } T , \qquad \mathrm { } ( 1 . 1 2 \mathrm { } ^ { } } } \end{array}
$$

and therefore $\bar { T } _ { \mu \nu } \simeq T _ { \mu \nu }$ .However,the definition (1.123) copes with the most general situation.

21 Observe hat,since $R _ { \mu \nu } ^ { ( 2 ) }$ is already ,we have

$$
\begin{array} { r } { g ^ { \mu \nu } R _ { \mu \nu } ^ { ( 2 ) } = ( \bar { g } ^ { \mu \nu } + h ^ { \mu \nu } ) R _ { \mu \nu } ^ { ( 2 ) } } \\ { = \bar { g } ^ { \mu \nu } R _ { \mu \nu } ^ { ( 2 ) } + O ( h ^ { 3 } ) } \end{array}
$$

and, since we are working up to $O ( h ^ { 2 } )$ ， it is irrelevant whether we define the traces of $R _ { \mu \nu } ^ { ( 2 ) }$ and of $t _ { \mu \nu }$ contracting with $g ^ { \mu \nu }$ orwith $\bar { g } ^ { \mu \nu }$

So, we can rewrite eq. (1.122) as

$$
\bar { R } _ { \mu \nu } = \frac { 8 \pi G } { c ^ { 4 } } \left( t _ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } t \right) + \frac { 8 \pi G } { c ^ { 4 } } \left( \bar { T } _ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } \bar { T } \right) ,
$$

or, in an equivalent way, 22Recall however that we limited ourselves to an expansion of $R _ { \mu \nu }$ upto quadratic order in $h _ { \mu \nu }$ ，so all higherorder non-linearities in $h _ { \mu \nu }$ have been neglected.We will come back to these non-linear terms in Section 2.2.3 and especially in Chapter 5.

$$
\overline { { { \bar { R } _ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } \bar { R } = \frac { 8 \pi G } { c ^ { 4 } } \left( \bar { T } _ { \mu \nu } + t _ { \mu \nu } \right) . } } }
$$

This can be appropriately called the “coarse-grained” form of the Ein stein equations. These equations determine the dynamics of $\bar { g } _ { \mu \nu }$ ,which is the long-wavelength (or low-frequency) part of the metric, in terms of the long-wavelength (or, respectively, low-frequency) part of the mat ter energy-momentum tensor, $\bar { T } _ { \mu \nu }$ ,and of a tensor $t _ { \mu \nu }$ which does not depend on the external matter but only on the gravitational field itself and is quadratic in $h _ { \mu \nu }$ .22

We can then summarize the results of this analysis as follows.

· At a “microscopic” level, there is no fundamental distinction between a background metric and fluctuations over it. The gravitational field is described by all its modes,and its dynamics is fully accounted for by the Einstein equations (1.3).   
· If some fuctuations $h _ { \mu \nu }$ are clearly distinguishable from the background because their typical length-scale $\star$ is much smaller than the typical length-scale $L _ { B }$ that characterizes the spatial variations of the background, it becomes useful to introduce a “macroscopic" level of description,i.e.an approximate description which is valid at a length-scale $\overrightharpoon { l }$ ，such that $\hat { \lambda } \ll \hat { l }$ (but still $\bar { l } \ll L _ { B }$ .Thisis obtained “integrating out” the short-wavelength degrees of freedom,which,in practice,can be obtained by performing a spatial average of the Einstein equations over a box of size $\vec { l }$ i.e.over several wavelengths $\dot { \boldsymbol { x } }$ If the separation between fluctuations and background is based on the condition $f _ { B } \ll f$ instead,we integrate out the fast-varying degrees of freedom，performing a temporal average over several periods $1 / f$ ， and we are left with an effective dynamics for the slowly varying degrees of freedom.   
· The result of this procedure (which, basically, is a renormalization group transformation) is summarized by eq.(1.130),together with the definitions of $t _ { \mu \nu }$ and $\bar { T } _ { \mu \nu }$ given in eqs.(1.123) and (1.125). The left-hand side of eq.(i.13O) is the Einstein tensor for the   
slowly varying metric $\scriptstyle { \vec { g } } _ { \mu \nu }$ .On the right-hand side we find, not surprisingly,a smoothed version of the matter energy-momentum tensor, $\bar { T } _ { \mu \nu }$ The most interesting aspect of eq.(1.130), however, is that it shows that the effect of GWs on the background curvature is formally identical to that of matter with energy-momentum tensor $t ^ { \mu \nu }$ We

are therefore able to assign an energy-momentum tensor to GWs.

· It is useful to observe that $t _ { \mu \nu }$ comes out automatically in an averaged form. This averaging procedure is not something that is imposed by hand afterwards. It comes out this way because, to derive the effect of GWs on the background,one is passing from a fundamental,“microscopic”，description，to a coarse-grained, “macroscopic”description.

# 1.4.3 The energy-momentum tensor of GWs

We now compute explicitly $t _ { \mu \nu }$ ，using eq. (1.125） with $R _ { \mu \nu } ^ { ( 2 ) }$ given in eq. (1.114). We are interested in the energy and momentum carried by the GWs at large distances from the source (e.g.at the position of the detector),where we can approximate the background space-time as flat. In this case we can simply replace $\bar { D } ^ { \mu }  \vert \partial ^ { \mu }$ in eq. (1.114), so we get

$$
\begin{array} { c } { { { \displaystyle R _ { \mu \nu } ^ { ( 2 ) } = \frac { 1 } { 2 } \left[ \frac { 1 } { 2 } \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } h ^ { \alpha \beta } + h ^ { \alpha \beta } \partial _ { \mu } \partial _ { \nu } h _ { \alpha \beta } \right. } } } \\ { { \left. + h ^ { \alpha \beta } \partial _ { \alpha } \partial _ { \beta } h _ { \mu \nu } + \dot { \partial } ^ { \beta } h _ { \nu } ^ { \alpha } \partial _ { \beta } h _ { \alpha \mu } - \partial ^ { \beta } h _ { \nu } ^ { \alpha } \partial _ { \alpha } h _ { \beta \mu } - \partial _ { \beta } h ^ { \alpha \beta } \partial _ { \nu } h _ { \alpha \mu } \right. } }  \\ { { \left. + \partial _ { \beta } h ^ { \alpha \beta } \partial _ { \alpha } h _ { \mu \nu } - \partial _ { \beta } h ^ { \alpha \beta } \partial _ { \mu } h _ { \alpha \nu } - \frac { 1 } { 2 } \partial ^ { \alpha } h \partial _ { \alpha } h _ { \mu \nu } + \frac { 1 } { 2 } \partial ^ { \alpha } h \partial _ { \nu } h _ { \alpha \mu } \right. } }  \\ { { \left. + \frac { 1 } { 2 } \partial ^ { \alpha } h \partial _ { \mu } h _ { \alpha \nu } \right] . } } \end{array}
$$

As we saw in Section 1.2, the $4 \times 4$ symmetric matrix $h _ { \mu \nu }$ has 10 degrees of freedom,out of which eight are gauge modes and two are physical modes.Correspondingly,in $t _ { \mu \nu }$ one can have in principle contributions both from the physical modes and from the gauge modes. The left-hand side of eq. (1.i30),i.e. the Einstein tensor of the background metric $j _ { \mu \nu }$ ,is of course a quantity that depends on the coordinate system, since it is a tensor. Thus,in principle there is nothing wrong if, on the right-hand side,we have both physical contributions and coordinatedependent contributions,i.e contributions from gauge modes.The issue $1 3$ how to distinguish the contribution to $t _ { \mu \nu }$ due to the physical modes from the contribution of the gauge modes. The former will give the energy-momentum tensor of the GWs,and describe physical effects that cannot be gauged away,while the latter will be associated with ripples i space-times that are due to the choice of the coordinate system,and that can be made to vanish with an apprppriate gauge choice.

The most straightforward way to get the contribution of the physical modes is to make use of the Lorentz gauge condition (1.18). This immediately eliminates four spurious degrees of freedom,leaving us with the wo physical degrees of freedomcontained in $h _ { i j } ^ { \mathrm { T T } }$ and the four gauge modes $\xi _ { \mu }$ which satisfy $\begin{array} { r } { \bigtriangledown \xi _ { \mu } = 0 } \end{array}$ ，as discussed in Section 1.2. We also rhoose the $\xi _ { \mu }$ so that $h = 0$ (so that only three independent gauge modes remain). Then $\bar { h } _ { \mu \nu } = h _ { \mu \nu }$ and the Lorentz gauge condition becomes $a / - h _ { \mu \nu } = 0$

We can now drastically simplify $R _ { \mu \nu } ^ { ( 2 ) }$ in eq. (1.131) observing that, mside the spatial or temporal average,the space-time derivative $\partial _ { \mu }$ can le integrated by parts, neglecting the boundary term.23 Performing in-

23On generic functions,an integration by parts of $\partial _ { t }$ is possible only if we have performed an integral over time, while an integration by parts of $\partial _ { i }$ requires a spatial integral.Recall however that in the Lorentz gauge,outside the source, the equation of motion is a simple wave equation $\square h _ { \mu \nu } = 0$ So,for a solution propagating for instance in the $z$ direction,all quantities are functions of the combination $x ^ { 0 } - z$ where $x ^ { 0 } = c t$ In expressions such as $\begin{array} { r } { \int d z g ( x ^ { 0 } - z ) \partial _ { 0 } f ( x ^ { 0 } - z ) } \end{array}$ we can replace $\partial _ { 0 } f$ with $- \partial _ { z } f$ ，integrate $\partial _ { z }$ by parts and then replace again $\partial _ { z } g$ with $- \partial _ { 0 } g$ ，Therefore,for solutions of the wave equation,a spatial average allows us to integrate by parts not only the spatial derivative but even the time derivative,and similarly fora time average.

Observe also that,in the integration by parts,the boundary terms vanish only when the size of the box used for the integration is infinitely larger than $\star$ A more precise statement is that the non-zero terms are of higher order in $\star / L _ { B }$ .However,we will only need the result to leading order.

tegrations by parts and making use of the gauge conditions $\partial ^ { \mu } h _ { \mu \nu } = 0$ and $h = 0$ and of the equation of motion $\begin{array} { r } { \boxed { \begin{array} { r l r } \end{array} } \begin{array} { r l r } \end{array} } \end{array}$ ，it is immediate to see that all terms in eq.(1.131) collapse to zero except the first two, which are related to each other by an integration by parts, giving

$$
\langle R _ { \mu \nu } ^ { ( 2 ) } \rangle = - \frac { 1 } { 4 } \langle \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } h ^ { \alpha \beta } \rangle ,
$$

while $\langle R ^ { ( 2 ) } \rangle$ vanishes upon integration by parts and using the equation of motion $\boxed { \ d } h _ { \alpha \beta } = 0$ Recalling the factor $- c ^ { 4 } / ( 8 \pi G )$ from eq. (1.125), we finally find

$$
\overline { { { t _ { \mu \nu } = \frac { c ^ { 4 } } { 3 2 \pi G } \langle \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } h ^ { \alpha \beta } \rangle } } } .
$$

We can now verify that the residual gauge modes $\xi _ { \mu }$ do not contribute to this expression. In fact,under the gauge transformation (1.8),the variation of $t _ { \mu \nu }$ is

$$
\begin{array} { l } { { \delta t _ { \mu \nu } = \displaystyle \frac { c ^ { 4 } } { 3 2 \pi G } [ \langle \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } ( \delta h ^ { \alpha \beta } ) \rangle + ( \mu  \nu ) ] } } \\ { { = \displaystyle \frac { c ^ { 4 } } { 3 2 \pi G } [ \langle \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } ( \partial ^ { \alpha } \xi ^ { \beta } + \partial ^ { \beta } \xi ^ { \alpha } ) \rangle + ( \mu  \nu ) ] } } \\ { { = \displaystyle \frac { c ^ { 4 } } { 1 6 \pi G } [ \langle \partial _ { \mu } h _ { \alpha \beta } \partial _ { \nu } \partial ^ { \alpha } \xi ^ { \beta } \rangle + ( \mu  \nu ) ] , } } \end{array}
$$

24The fact that this result holds only to leading order in $\scriptstyle \sum / L _ { B }$ (see Note 23) is not surprising,since it is only in this limit that the notion of GW is well defined. If $\scriptstyle \lambda / L _ { B }$ approaches one, the distinction between the background and the perturbation fades away,and correspondingly one can no longer assign a gauge-invariant energy-momentum tensor to the perturbations.

and this vanishes since, inside $\langle \ldots \rangle$ ， we can integrate by parts $\partial ^ { \alpha }$ ，and then we can use the Lorentz condition $\partial ^ { \alpha } h _ { \alpha \beta } = 0$ .24 Therefore $t _ { \mu \nu }$ depends only on thephysical modes $h _ { i j } ^ { \mathrm { T T } }$ ,and we can simply replace $h _ { \mu \nu }$ in eq.(1.133) with the metric in the TT gauge.In particular,the gaugeinvariant energy density is

$$
t ^ { 0 0 } = \frac { c ^ { 2 } } { 3 2 \pi G } \langle \dot { h } _ { i j } ^ { \mathrm { T T } } \dot { h } _ { i j } ^ { \mathrm { T T } } \rangle ,
$$

(where the dot denotes $\partial _ { t } = ( 1 / c ) \partial _ { 0 }$ ）or,in terms of the amplitudes $h _ { + }$ and $h _ { \times }$ ，

$$
t ^ { 0 0 } = \frac { c ^ { 2 } } { 1 6 \pi G } \langle \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \rangle .
$$

For a plane wave traveling along the $z$ direction, $h _ { i j } ^ { \mathrm { T T } }$ is a function $t - z / c$ and therefore $t ^ { 0 1 } = t ^ { 0 2 } = 0$ while $\partial _ { z } h _ { i j } ^ { \mathrm { T T } } = - \partial _ { 0 } h _ { i j } ^ { \mathrm { T T } } = + \partial ^ { 0 } h _ { i j } ^ { \mathrm { T T } }$ and therefore

$$
t ^ { 0 3 } = t ^ { 0 0 } .
$$

An alternative way of extracting the gauge-invariant part from $t _ { \mu \nu }$ isto start from the full expression (1.131) without performing any prior gauge fixing,and consider its variation under a linearized gauge transformation (1.8), where now $\xi _ { \mu }$ are generic, rather than being constrained to satisfy $\square \xi _ { \mu } = 0$ . Then,with straightforward algebra one finds that

$$
t _ { \mu \nu }  t _ { \mu \nu } + \partial _ { \rho } U _ { \mu \nu } ^ { \rho } ,
$$

with $U _ { \mu \nu } ^ { \rho }$ some tensor. The additional term is a total divergence,and we would like to trow it away inside the average,as we have done above. Here however we must be careful because,since we have not fixed the Lorentz gauge,the metric now does not satisfy a simple wave equation such as $\square h _ { \mu \nu } = 0$ ．Thus,the argument discussed in Note 23,which allowed us to integrate by parts $\hat { \partial } _ { \rho }$ inside a temporal average,or inside a spatial average,no longer goes through However,we can integrate by parts $\partial _ { \mu }$ inside a space-time average,that we denote as $\langle \langle \ldots \rangle \rangle$ .Then $\langle \langle \partial _ { \rho } U _ { \mu \nu } ^ { \rho } \rangle \rangle$ vanishes and $\langle \langle t _ { \mu \nu } \rangle \rangle$ is gauge invariant (again to leading order in $\star / L _ { B }$ ).Thus,an equivalent way to single out the gauge-invariant part of $t _ { \mu \nu }$ is to average it over space-time,and the result gives again eq. (1.133).25

Finally,observe that in eq.(1.130) the left-hand side is covariantly couserved with respect to $\hat { D } ^ { \mu }$ ,i.e. $\bar { \bar { D } } ^ { \mu } ( \bar { \bar { R } } _ { \mu \nu } - { \textstyle \frac { 1 } { 2 } } \bar { g } _ { \mu \nu } \bar { R } ) = 0$ ,because of the Bianchi identity.Therefore, we have

$$
\overline { { { \bar { D } } ^ { \mu } ( \bar { T } _ { \mu \nu } + t _ { \mu \nu } ) } } = 0 .
$$

The fact that the covariantly conserved quantity is the sum of $\bar { T } _ { \mu \nu }$ and $t _ { \mu \nu }$ , rather than each one separately,reflects the fact that there is in general exchange of energy and momentum between the matter sources and GWs. At large distances from the source the metric approaches the flat-space metric，so $\bar { D } ^ { \mu }$ approaches $\partial ^ { \mu }$ ，while outside the source $\dot { T } _ { \mu \nu } = 0$ .Then,far from the sources,eq.(1.140)reduces to

$$
\partial ^ { \mu } t _ { \mu \nu } = 0 .
$$

The energy flux

Having obtained the energy-momentum tensor carried by the GWs,it is now straightforward to compute the corresponding energy flux,i.e. the energy of GWs flowing per unit time through a unit surface at a large distance from the source. We start from the conservation of the energy-momentum tensor, $\partial _ { \mu } t ^ { \mu \nu } = 0$ ,which implies that

$$
\int _ { V } d ^ { 3 } x ( \partial _ { 0 } t ^ { 0 0 } + \partial _ { i } t ^ { i 0 } ) = 0 ,
$$

where $V$ is a spatial volume in the far region,bounded by a surface $S$ The GW energy inside the volume $V$ is

$$
E _ { V } = \int _ { V } d ^ { 3 } x t ^ { 0 0 } ,
$$

0 eq. (1.142) can be written as

$$
\begin{array} { r } { \frac { 1 } { c } \displaystyle \frac { d E _ { V } } { d t } = - \int _ { V } d ^ { 3 } x \partial _ { i } t ^ { 0 i } } \\ { = - \int _ { S } d A n _ { i } t ^ { 0 i } , } \end{array}
$$

25To make the proof simpler we worked at large distance from the source,where the background metric can be taken as flat.The argument can however be repeated in a generic background $\tilde { g } _ { \mu \nu }$ ，although it becomes technically more involved. In this case one makes use of the fact that,inside a spacetime average,to lowest order in $\scriptstyle \lambda / L _ { B }$ ： (i) Covariant divergences can be integrated by parts discarding the boundary term._In particular，expressions such as $\langle \langle \bar { D } _ { \rho } U _ { \mu \nu } ^ { \rho } \rangle \rangle$ vanish. (ii) Covariant derivative commutes.Then one finds,from the full expression (1.114), that

$$
t _ { \mu \nu }  t _ { \mu \nu } + \bar { D } _ { \rho } U _ { \mu \nu } ^ { \rho } ,
$$

and therefore $\langle \langle t _ { \mu , \nu } \rangle \rangle$ is gauge invariant, to leading order in $\dot { \lambda } / L _ { B }$ Afurther technical subtlety is that,in curved space,the sum of tensors at different points in space-time is not a tensor,so the result of integrating a tensor is also not a tensor.Thus,before integrating over $d ^ { 4 } x ,$ one must carry the tensors $t _ { \mu \nu } ( x )$ back to a single common point using parallel transport along geodesics.Details can be found in the Appendix of Isaacson (1968b),and references therein.

In principle,the same parallel transport procedure should be applied to the spatial and to the temporal averages that we introduced in Section 1.4.2. However，we will always end up computing these averages very far from the sources,where the background spacetime can be taken as fat.

26More precisely， we take as volume $V$ a spherical shell centered on the source but far away from it，so that both its inner boundary $S _ { 1 }$ and its outer boundary $S _ { 2 }$ are in the far region, where the gravitational field is given simply by gravitational waves. Then in eq.(1.l43) we can limit ourselves to the energy-momentum tensor $t ^ { 0 0 }$ of GWs, neglecting the energy-momentum tensor of the quasi-static gravitational fields,as well as the energy-momentum tensor of matter. Therefore the time derivative of $E _ { V }$ is given by two terms: the energy flowing in through $S _ { 1 }$ minus the energy flowing out from $S _ { 2 }$ .We are interested in the energy flux through a unit surface at a given distance from the source (say,in the energy flowing through a unit surface of our detector), which for definiteness we choose to be on the outer surface $S _ { 2 }$ ,so in the following we simply take $S = S _ { 2 }$

where $n ^ { i }$ is the outer normal to the surface and $d A$ is the surface element.26 Furthermore, outside the source, we can impose the TT gauge. Let $S$ be a spherical surface at a large distance $r$ from the source. Its surface element is $d A = r ^ { 2 } d \Omega$ ,and its normal $\hat { n } = \hat { r }$ is the unit vector in the radial direction. Then eq.(1.144) gives

$$
\frac { d E _ { V } } { d t } = - c \int d A t ^ { 0 r } ,
$$

where

$$
t ^ { 0 r } = \frac { c ^ { 4 } } { 3 2 \pi G } \langle \partial ^ { 0 } h _ { i j } ^ { \mathrm { T T } } \frac { \partial } { \partial r } h _ { i j } ^ { \mathrm { T T } } \rangle .
$$

A GW propagating radially outward,at sufficiently large distances $r$ has the general form

$$
h _ { i j } ^ { \mathrm { T T } } ( t , r ) = \frac { 1 } { r } f _ { i j } ( t - r / c ) ,
$$

where $f _ { i j } ( t - r / c )$ is some function of retarded time $t _ { \mathrm { r e t } } = t - r / c$ We will prove this result in Section 3.1,but it is in fact completely analogous to the result for electromagnetic waves.Therefore

$$
\frac { \partial } { \partial r } h _ { i j } ^ { \mathrm { T T } } ( t , r ) = - \frac { 1 } { r ^ { 2 } } f _ { i j } ( t - r / c ) + \frac { 1 } { r } \frac { \partial } { \partial r } f _ { i j } ( t - r / c ) .
$$

On a function of the combination $t - r / c$ we have

$$
\frac { \partial } { \partial r } f _ { i j } ( t - r / c ) = - \frac { 1 } { c } \frac { \partial } { \partial t } f _ { i j } ( t - r / c ) ,
$$

and therefore

$$
\begin{array} { r } { \frac { \partial } { \partial r } h _ { i j } ^ { \mathrm { T T } } ( t , r ) = - \partial _ { 0 } h _ { i j } ^ { \mathrm { T T } } ( t , r ) + O ( 1 / r ^ { 2 } ) } \\ { = + \partial ^ { 0 } h _ { i j } ^ { \mathrm { T T } } ( t , r ) + O ( 1 / r ^ { 2 } ) . } \end{array}
$$

Then, from eq. (1.146),we see that at large distances, $t ^ { 0 r } = + t ^ { 0 0 }$ (which could also have been derived more simply from eq.(1.137)，observing that an observer sitting at large distances from the source sees a plane wavefront),and the energy inside the volume $V$ satisfies

$$
\frac { d E _ { V } } { d t } = - c \int d A t ^ { 0 0 } .
$$

The fact that $E _ { V }$ decreases means that the outward-propagating Gw carries away an energy flux

$$
\begin{array} { r } { \frac { d E } { d A d t } = + c t ^ { 0 0 } \qquad } \\ { = \frac { c ^ { 3 } } { 3 2 \pi G } \langle \dot { h } _ { i j } ^ { \mathrm { T T } } \dot { h } _ { i j } ^ { \mathrm { T T } } \rangle , } \end{array}
$$

or,writing the surface element $d A = r ^ { 2 } d \Omega$

$$
\frac { d E } { d t } = \frac { c ^ { 3 } r ^ { 2 } } { 3 2 \pi G } \int d \Omega \langle \dot { h } _ { i j } ^ { \mathrm { T T } } \dot { h } _ { i j } ^ { \mathrm { T T } } \rangle .
$$

In terms of $h _ { + }$ and $h _ { \times }$ , we can rewrite the result as

$$
\frac { d E } { d A d t } = \frac { c ^ { 3 } } { 1 6 \pi G } \langle \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \rangle .
$$

The total energy flowing through $d A$ between $t = - \infty$ and $t = + \infty$ is therefore27

$$
\frac { d E } { d A } = \frac { c ^ { 3 } } { 1 6 \pi G } \int _ { - \infty } ^ { \infty } d t \langle \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \rangle .
$$

As discussed in the previous section,in|the situations relevant for GW detectors the average $\langle \ldots \rangle$ in eq.(1.155) is a purely temporal average, overa few periods. Then in eq.(1.155) we can first perform the integral over dt from $- \infty$ to $+ \infty$ ,eliminating therefore any time dependence, and the subsequent temporal average is just the average of a constant. Therefore the average in eq.(1.155) can be omitted,and

$$
\frac { d E } { d A } = \frac { c ^ { 3 } } { 1 6 \pi G } \int _ { - \infty } ^ { \infty } d t \left( \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \right) .
$$

Inserting the plane wave expansion of $h _ { + , \times } ( t )$ ,given in eqs. (1.52) and (1.48), we get

$$
\begin{array} { l } { { \displaystyle \frac { d E } { d A } = \frac { c ^ { 3 } } { 1 6 \pi G } \int _ { - \infty } ^ { \infty } d f ( 2 \pi f ) ^ { 2 } \left( \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } \right) } } \\ { { \displaystyle \quad = \frac { \pi c ^ { 3 } } { 4 G } \int _ { - \infty } ^ { \infty } d f f ^ { 2 } \left( | \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } \right) . } } \end{array}
$$

Since the integrand is even under $f  + f$ ,we can restrict it to physical frequencies, $f > 0$ ，writing

$$
\frac { d E } { d A } = \frac { \pi c ^ { 3 } } { 2 G } \int _ { 0 } ^ { \infty } d f f ^ { 2 } \left( | \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } \right) .
$$

Therefore

$$
\frac { d E } { d A d f } = \frac { \pi c ^ { 3 } } { 2 G } f ^ { 2 } \left( | \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } \right) .
$$

We will always use the convention that the energy spectrum $d E / d f$ is the quantity that gives the total energy when it is integrated over the positive frequencies,rather than between $- \infty$ and $+ \infty$ .Writing $d A = r ^ { 2 } d \Omega$ ,and integrating over a sphere surrounding the source,we find the energy spectrum

$$
\frac { d E } { d f } = \frac { \pi c ^ { 3 } } { 2 G } f ^ { 2 } r ^ { 2 } \int d \Omega \left( | \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } \right) .
$$

In the same way we can compute the flux of momentum. The momentum of the GWs inside a spherical shell $V$ at large distances from the source is given bv

$$
P _ { V } ^ { k } = \frac { 1 } { c } \int _ { V } d ^ { 3 } x t ^ { 0 k } .
$$

27The integration over $t$ from $- \infty$ to $+ \infty$ is necessary if we want to resolve all possible frequencies． In an experiment one will integrate a signal only overa certain time interval $\Delta t$ and one has a corresponding resolution in frequency $\Delta f \simeq 1 / \Delta t$ 、

Considering again a GW propagating radially outward, and repeating the same steps leading from eq. (1.142) to eq. (1.154), we get

$$
\begin{array} { r } { c \partial _ { 0 } P _ { V } ^ { k } = \displaystyle \int _ { V } d ^ { 3 } x \partial _ { 0 } t ^ { 0 k } } \\ { = - \displaystyle \int _ { S } d A t ^ { 0 k } , } \end{array}
$$

and therefore the momentum flux carried away by the outward-propagatin GW is

$$
\frac { d P ^ { k } } { d A d t } = + t ^ { 0 k } .
$$

Inserting the expresson (1.133) for $t ^ { 0 k }$ ，we get

$$
\frac { d P ^ { k } } { d t } = - \frac { c ^ { 3 } } { 3 2 \pi G } r ^ { 2 } \int d \Omega \langle \dot { h } _ { i j } ^ { \mathrm { T T } } \partial ^ { k } h _ { i j } ^ { \mathrm { T T } } \rangle .
$$

Observe that, if $t ^ { 0 k }$ is odd under a parity transformation ${ \bf x } \longrightarrow - { \bf x }$ then the angular integral vanishes.

# 1.5Propagation in curved space-time

In the last section we have examined the consequences of the low-modes equation,eq. (1.1ll). We have seen that it determines the dynamics of the background metric $\bar { g } _ { \mu \nu }$ ,and that it allows us to identify the energymomentum tensor of $h _ { \mu \nu }$

We now turn our attention to the high-mode equation (1.1l2). First of all, we examine it in the limiting case of no external matter, $T _ { \mu \nu } = 0$ so eq.(1.1l2) becomes

$$
R _ { \mu \nu } ^ { ( 1 ) } = - [ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { H i g h } } .
$$

We are interested in the leading term in $\scriptstyle \sum / L _ { B }$ (orin $f _ { B } / f$ ; for definiteness we use $\ddagger / L _ { B } )$ . We therefore first perform an order of magnitude estimates of $R _ { \mu \nu } ^ { ( 1 ) }$ and of $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { H i g h } }$ In principle,intheshort-waveex pansion we have two small parameters, $h \equiv { \cal O } ( h _ { \mu \nu } )$ and $\scriptstyle \sum / L _ { B }$ Recall however, from eq.(1.120),that when $T _ { \mu \nu } = 0$ the Einstein equations fix these two scales to the same order of magnitude. Therefore,in this case we have a single small parameter, that we denote by $\epsilon$ ，

$$
\epsilon = { \cal O } ( h ) = { \cal O } ( \vec { \lambda } / L _ { B } ) .
$$

To simplify notation,we use units $\mathit { L } _ { \mathit { B } } = 1$ when we estimate the order of magnitude of the various terms,so that $h \sim \ddagger \sim \epsilon$ From eq. (1.113), the leading term of $R _ { \mu \nu } ^ { ( 1 ) }$ is

$$
R _ { \mu \nu } ^ { ( 1 ) } \sim \partial ^ { 2 } h \sim \frac { h } { \chi ^ { 2 } } \sim \frac { 1 } { \epsilon }
$$

while

$$
R _ { \mu \nu } ^ { ( 2 ) } \sim \partial ^ { 2 } h ^ { 2 } \sim { \frac { h ^ { 2 } } { \chi ^ { 2 } } } \sim 1 .
$$

So $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { H i g h } }$ is at most $O ( 1 )$ andcanbenegletedine5） pared to the leading term of $R _ { \mu \nu } ^ { ( 1 ) }$ ，which is $O ( 1 / \epsilon )$ Thus,if we limit ourselves to the leading term,eq.(1.112) simply becomes

$$
[ R _ { \mu \nu } ^ { ( 1 ) } ] _ { 1 / \epsilon } = 0 ,
$$

where $[ \ldots ] _ { 1 / \epsilon }$ means that we must extract the $O ( 1 / \epsilon )$ part.Equation (1.169) can be written explicitly as

$$
\eta ^ { \rho \sigma } ( \partial _ { \rho } \partial _ { \nu } h _ { \mu \sigma } + \partial _ { \rho } \partial _ { \mu } h _ { \nu \sigma } - \partial _ { \nu } \partial _ { \mu } h _ { \rho \sigma } - \partial _ { \rho } \partial _ { \sigma } h _ { \mu \nu } ) \simeq 0 ,
$$

since the $O ( 1 / \epsilon )$ part is obtained substituting the covariant derivatives with ordinary derivatives,and at the same time $\bar { g } ^ { \rho \sigma }$ in front of the parenthesis can be substituted with $\eta ^ { \rho \sigma }$ ,again to leading order in $\epsilon$ .This is just a propagation equation for the field hμv in a flat background,and it is the same equation that governs the propagation in the linearized theory discussed in Section 1.1,so we can again introduce $\bar { h } _ { \mu \nu } = h _ { \mu \nu } -$ $( 1 / 2 ) \eta _ { \mu \nu } h$ ,impose the Lorentz gauge,and eq.(1.17O) is nothing but

$$
\sqcup _ { h _ { \mu \nu } } \simeq 0 ! ,
$$

where $\Xi = \partial _ { \mu } \partial ^ { \mu }$ is the flat space d'Alembertian. So, this is the same $3 . 5$ eq.(1.24) with the matter energy-momentum tensor $T _ { \mu \nu } = 0$ We therefore discover that the high-frequency equation (1.1l2） is a wave equation for $h _ { \mu \nu }$ .We find that the propagation of GWs at $O ( h )$ is te same as in the linearized theory begause we considered the limit in which GWs are the only source of curvature. We now turn to the more iteresting case in which external matter is present and dominates the cirvature,so the low-frequency equatioh (1.111） becomes

$$
\bar { \bar { \cal R } } _ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } \bar { \cal R } \simeq \frac { 8 \pi G } { | c ^ { 4 } } \bar { \cal T } _ { \mu \nu } .
$$

Toexpand the high-frequency equation (1.112), we recallfrom eq. (1.121) that in this case $h \ll \mathfrak { X } / L _ { B } \ll 1$ ，so the expansions in $h$ and in $\displaystyle \dot { \lambda } / L _ { B }$ are different.We keep only the terms linear in $h$ (terms quadratic in h.in a typical situation involving GWs,are utterly negligible),and we expand the result in powers of $\displaystyle \dot { \lambda } / L _ { B }$ .If we limit only to the leading and ext-to-leading order in /LB,eq. (1.112) becomes simply28

$$
R _ { \mu \nu } ^ { ( 1 ) } = 0 \ / .
$$

Now $\bar { g } _ { \mu \nu }$ is determined by $T _ { \mu \nu }$ and is not close to fat, so $R _ { \mu \nu } ^ { ( 1 ) }$ is a fully bvariant quantity with respect to a non-trivial background metric.As eshowin Problem1.1,inacurved background theequation $R _ { \mu \nu } ^ { ( 1 ) } = 0$ wittenexplicitly,reads

$$
\bar { g } ^ { \rho \sigma } ( \bar { D } _ { \rho } \bar { D } _ { \nu } h _ { \mu \sigma } + \bar { D } _ { \rho } \bar { D } _ { \mu } h _ { \nu \sigma } - \bar { D } _ { \nu } \bar { D } _ { \mu } h _ { \rho \sigma } - \bar { D } _ { \rho } \bar { D } _ { \sigma } h _ { \mu \nu } ) = 0 .
$$

Ihe discussion of this equation parallels exactly that of Section 1.1,

$^ { 2 8 } \mathrm { { I n } }$ fact, in eq. (1.112， $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { H i g h } }$ is negligiblewithrespect to $R _ { \mu , \nu } ^ { ( 1 ) }$ be cause it has one more power of To estimate the order of magnitude of $( T _ { \mu , \nu } \ : - \ : \frac { 1 } { 2 } g _ { \mu \nu } T ) ^ { \mathrm { H i g h } }$ we observe that, if $T _ { \mu \nu }$ is smooth，as we expect for macroscopic matter,its high-frequency part will come from the fact that the energy-momentum tensor $T _ { \mu \nu }$ depends in general on the metric $g _ { \mu \nu }$ ,and therefore will have a high-frequency component $O ( h )$ .Besides,also $g _ { \mu \nu } T ~ =$ $( \bar { g } _ { \mu \nu } + h _ { \mu \nu } ) T$ has a high-frequency part $O ( h )$ which comes from multiplying $\bar { g } _ { \mu \nu }$ with the $O ( h )$ high-frequency part of $T$ and another high-frequency part $O ( h )$ which comes from multiplying $h _ { \mu , \nu }$ with the low-frequency part of $T$ So,

$$
\left( T _ { \mu \nu } - \frac { 1 } { 2 } g _ { \mu \nu } T \right) ^ { \mathrm { H i g h } } = { \cal O } ( h / L _ { B } ^ { 2 } ) .
$$

Instead, $R _ { \mu \nu } ^ { ( 1 ) } \sim \partial ^ { 2 } h \sim h / { \chi ^ { 2 } }$ Then $( T _ { \mu \nu } - \textstyle { \frac { 1 } { 2 } } g _ { \mu \nu } T ) ^ { \mathrm { H i g h } }$ is smalle than $R _ { \mu \nu } ^ { ( 1 ) }$ bya factor $O ( \mathfrak { X } ^ { 2 } / L _ { B } ^ { 2 } )$ and, to leading and next-to-leading order in $\dot { \bar { \lambda } } / L _ { B }$ ，it does not contribute.

29There is a slight notational clash here.The bar over $g _ { \mu \nu }$ denotes the background metric,while over $h _ { \mu \nu }$ it denotes the combination (1.176).

with $\eta _ { \mu \nu }$ replaced by $\bar { g } _ { \mu \nu }$ . The equation becomes simpler introducing $h = \bar { g } ^ { \mu \nu } h _ { \mu \nu }$ and29

$$
\bar { h } _ { \mu \nu } = h _ { \mu \nu } - \frac { 1 } { 2 } \bar { g } _ { \mu \nu } h .
$$

We now impose the gauge condition

$$
\boxed { \begin{array} { c c } { \begin{array} { r l } \end{array} } } \\ { \begin{array} { r l } \end{array} } \end{array}
$$

that we stillcallteLorentzgauge.Intis gaugetheequation $R _ { \mu \nu } ^ { ( 1 ) } = 0$ becomes

$$
\bar { D } ^ { \rho } \bar { D } _ { \rho } \bar { h } _ { \mu \nu } + 2 \bar { R } _ { \mu \rho \nu \sigma } \bar { h } ^ { \rho \sigma } - \bar { R } _ { \mu \rho } \bar { h } _ { \nu } ^ { \rho } - \bar { R } _ { \nu \rho } \bar { h } _ { \mu } ^ { \rho } = 0 .
$$

Outside the matter sources,where $\bar { T } _ { \mu \nu } = 0$ ， the Einstein equation for the background,eq. (1.172),tells us that $\vec { R } _ { \mu \nu } = 0$ More precisely, using $\bar { R } _ { \mu \nu }$ wheterm $[ R _ { \mu \nu } ^ { ( 2 ) } ] ^ { \mathrm { L o w } }$ ${ \bar { R } } _ { \mu \nu } \ _ { - } = { \cal O } ( h ^ { 2 } / \chi ^ { 2 } )$ $h$   
$\bar { R } _ { \mu \rho } \bar { h } _ { \nu } ^ { \rho }$ and $\bar { R } _ { \nu \rho } \bar { h } _ { \mu } ^ { \rho }$ in eq. (1.178).Furthermore, $\bar { R } _ { \mu \rho \nu \sigma } \bar { h } ^ { \rho \sigma } = { \cal O } ( h / L _ { B } ^ { 2 } )$ while $\bar { D } ^ { \rho } \bar { D } _ { \rho } \bar { h } _ { \mu \nu } \stackrel { . } { = } O ( h / \chi ^ { 2 } )$ .Thus, since we have already restricted ourselves to the leading term and next-to-leading term in $\displaystyle \dot { \lambda } / L _ { B }$ (see Note 28) we simply have

$$
\boxed  \begin{array} { c c } { { \begin{array} { r l } { \bar { D } ^ { \rho } \bar { D } _ { \rho } \bar { h } _ { \mu \nu } = 0 . } \end{array} } } \end{array}
$$

Equations (1.177) and (1.179) determine the propagation of GWs in the curved background,in the limit $\mathit { \Pi } ^ { \dag } \ll \mathit { L } _ { B }$ . In conclusion we find that, after separating the Einstein equations into a low-frequency part and a high-frequency part, the low-frequency part describes the effect of GWs and of external matter on the background space-time, while the highfrequency part gives a wave equation in curved space, which describes the propagation of $h _ { \mu \nu }$ . This curved-space equation can be solved using the eikonal approximation of geometric optics, as we now discuss.

# 1.5.1 Geometric optics in curved space

# Electromagnetic waves

30We follow Misner,Thorne and Wheeler (1973), Section 22.5.

We first recall how geometric optics works for electromagnetic waves, in a curved space with metric $\bar { g } _ { \mu \nu }$ .30 The action of the electromagnetic field in this curved space is

$$
S = - \frac { 1 } { 4 } \int d ^ { 4 } x \sqrt { - \bar { g } } \ \bar { g } _ { \mu \alpha } \bar { g } _ { \nu \beta } F ^ { \mu \nu } F ^ { \alpha \beta } ,
$$

and its variation gives the equations of motion

$$
\bar { D } _ { \mu } ( \bar { D } ^ { \mu } A ^ { \nu } - \bar { D } ^ { \nu } A ^ { \mu } ) = 0
$$

(we raise and lower the indices with $\bar { g } _ { \mu \nu }$ ),which generalize thefat-space pair of Maxwell equations $\partial _ { \mu } F ^ { \mu \nu } = 0$ .One imposes on the four-vector potential $A ^ { \mu }$ the curved-space generalization of the Lorentz gauge,

$$
\bar { D } _ { \mu } A ^ { \mu } = 0 .
$$

From the definition of covariant derivative, $\bar { D } _ { \mu } \bar { D } ^ { \nu } A ^ { \mu } = \bar { D } ^ { \nu } \bar { D } _ { \mu } A ^ { \mu } +$ $R ^ { \nu } { } _ { \mu } A ^ { \mu }$ ，where $R ^ { \nu } { } _ { \mu }$ is the Riccitensor.The term $\bar { D } ^ { \nu } \bar { D } _ { \mu } A ^ { \mu }$ vanishes because of the gauge condition, so eq. (1.181） becomes

$$
\bar { D } ^ { \rho } \bar { D } _ { \rho } A ^ { \mu } - \bar { R } ^ { \mu } { } _ { \rho } A ^ { \rho } = 0 .
$$

Geometric optics is valid when $\ddagger$ is much smaller than the other lengthscales in the problem. So we must have $\dot { \pi } \ll L _ { B }$ with $L _ { B }$ the typical scale of variation of the background metric,and also $\dot { \lambda } \ll L _ { c }$ ，where $L _ { c }$ is the characteristic length-scale over which the amplitude,polarization or wavelength of the electromagnetic field change substantially. In particular, $\ddagger$ must be much smaller thah the curvature radius of the wavefront.

Under these conditions,we can use the|eikonal approximation,which consists in looking for a solution with a phase $\theta$ rapidly varying, i.e. $\theta$ changes on the scale $\ddagger$ ，while the amplitude changes only on the scale $L _ { B }$ or $L _ { c }$ (whichever is smaller),so it is slowly varying.To perform the expansion systematically it is convenient to write

$$
A ^ { \mu } ( x ) = [ a ^ { \mu } ( x ) + \varepsilon b ^ { \mu } ( x ) + \varepsilon ^ { 2 } c ^ { \mu } ( x ) + . . . ] e ^ { i \theta ( x ) / \varepsilon } ,
$$

where $\varepsilon$ is a fictitious parameter,to be finally set equal to unity, that reminds us that a term to which a factbr $\epsilon ^ { n }$ is attached,is of order $( { \dot { x } } / L ) ^ { n }$ ,where $L$ is the smallest between $L _ { B }$ and $L _ { c }$ . An expansion of the torm (1.184) is just anansatz,and its validity is verified by substituting I in the equations.

Since $R ^ { \mu } { } _ { \rho } A ^ { \rho } = O ( A / L _ { B } ^ { 2 } )$ ，where $A$ isthe typical amplitude of $A ^ { \mu }$ ， while $\bar { D } ^ { \rho } \bar { D } _ { \rho } A ^ { \mu } = { \cal O } ( A / \chi ^ { 2 } )$ ，to leading and next-to-leading order in $\hbar / L _ { B }$ we can neglect $R ^ { \mu } { } _ { \rho } A ^ { \rho }$ ,and the equation of motion is simply

$$
\bar { D } ^ { \rho } \bar { D } _ { \rho } A ^ { \mu } = \rrangle .
$$

Defining the wave-vector $k _ { \mu } \equiv \partial _ { \mu } \theta$ and plugging the ansatz (1.184) into . (1.182) we get,to lowest order,

$$
{ \bar { g } } _ { \mu \nu } k ^ { \mu } a ^ { \nu } = 0 .
$$

from eq. (1.185） we get instead,to lowest order,

Iis is known as the eikonal equation. From this it also follows that $= \tilde { D } _ { \nu } ( k _ { \mu } k ^ { \mu } ) = 2 k ^ { \mu } \tilde { D } _ { \nu } k _ { \mu }$ (recall again that indices are raised and wweredwith $\bar { g } _ { \mu \nu }$ ).Since $\theta$ is a scalar,and on a scalar the covariant derivatives commute， we have $\bar { D } _ { \nu } \partial _ { \mu } \theta = \bar { D } _ { \nu } \bar { D } _ { \mu } \theta = \bar { D } _ { \mu } \bar { D } _ { \nu } \theta = \bar { D } _ { \mu } \partial _ { \nu } \theta$ so we can interchange the indices, $\bar { D } _ { \nu } k _ { \mu } = \bar { D } _ { \mu } k _ { \nu }$ ， and the condition $k ^ { \mu } \bar { D } _ { \nu } k _ { \mu } = 0$ becomes

$$
k ^ { \mu } \bar { D } _ { \mu } k _ { \nu } = 0 .
$$

31Writing ku = dxμ/d>，where λ is the affine parameter along the geodesic, eq.(1.188) gives the geodesic equation, in the form

$$
\frac { d ^ { 2 } x ^ { \mu } } { d \lambda ^ { 2 } } + \Gamma _ { \nu \rho } ^ { \mu } \frac { d x ^ { \nu } } { d \lambda } \frac { d x ^ { \rho } } { d \lambda } = 0 .
$$

This is the geodesic equation in the space-time of the background metric $\bar { g } _ { \mu \nu } , ^ { 3 1 }$ so eq. (1.188)states thatthecurves orthogonal tothesufaces of constant phase (the “rays” of the geometric optics approximation) travel along the null geodesics of $\bar { g } _ { \mu \nu }$

To next-to-leading order in $\varepsilon , \in { \bf q }$ (1.185) gives

$$
2 k _ { \rho } \bar { D } ^ { \rho } a ^ { \mu } + ( \bar { D } ^ { \rho } k _ { \rho } ) a ^ { \mu } = 0 .
$$

It is convenient to introduce the real scalar amplitude $a = ( a ^ { \mu } a _ { \mu } ^ { \ast } ) ^ { 1 / 2 }$ and the polarization vector $e ^ { \mu }$ defined from $a ^ { \mu } = a e ^ { \mu }$ ,s0 $e ^ { \mu } e _ { \mu } ^ { \ast } = 1$ An equation for the scalar amplitude is obtained observing that,on the one hand,one has the trivial identity $k ^ { \mu } \partial _ { \mu } ( a ^ { 2 } ) = 2 a k ^ { \mu } \partial _ { \mu } a$ .On the other hand,on a scalar such as $a ^ { 2 }$ ， $\partial _ { \mu }$ can be replaced by $\bar { D } _ { \mu }$ ，so $k ^ { \mu } \partial _ { \mu } ( a ^ { 2 } ) =$ $k ^ { \mu } \bar { D } _ { \mu } ( a ^ { \rho } a _ { \rho } ^ { * } ) = - ( \bar { D } ^ { \rho } k _ { \rho } ) a ^ { 2 }$ , where we used eq. (1.189). Comparing these two results,we get an equation for the scalar amplitude,

$$
k ^ { \mu } \partial _ { \mu } a = - \frac { 1 } { 2 } ( \bar { D } _ { \mu } k ^ { \mu } ) a .
$$

Finally,to obtain an equation for $e ^ { \mu }$ ，we substitute $a ^ { \mu } ~ = ~ a e ^ { \mu }$ into eq. (1.189) and we use eq. (1.190). This gives

$$
k ^ { \rho } \bar { D } _ { \rho } e ^ { \mu } = 0 .
$$

Expanding the equations to still higher orders we could determine the corrections $b _ { \mu } , c _ { \mu } , \ldots$ to the amplitude in terms of $a _ { \mu }$ .Equations (1.186), (1.187),(1.i88)，(1.190) and (1.191) are the fundamental results of the geometric optics of electromagnetic waves in curved space. Equa-tions (1.187) and (1.188) states that light rays (or photons,in a quantum language) travel along the null geodesics of $\bar { g } _ { \mu \nu }$ . Equation (1.186) states that the polarization vector $e ^ { \mu }$ is orthogonal to the propagation direction, $k _ { \mu } e ^ { \mu } = 0$ ，and eq.(1.191) states that it is parallel-transported along the null geodesics. Finally,eq.(1.190) expresses (in the quantum language) the conservation of the number of photons in the limit of geometric optics. This can be seen rewriting it in the form

$$
\bar { D } ^ { \mu } ( a ^ { 2 } k ^ { \mu } ) = 0 .
$$

This shows that the current $j ^ { \mu } = a ^ { 2 } k ^ { \mu }$ is covariantly conserved. Its associated conserved charge,according to the Noether theorem that we will recall in Section 2.1.1, is the integral of $a ^ { 2 } k ^ { 0 }$ over a spatial surface at constant time. In a plane wave, the energy density is proportional to $| \mathbf { E } | ^ { 2 } + | \mathbf { B } | ^ { 2 } = 2 | \mathbf { E } | ^ { 2 }$ . In the gauge $A _ { 0 } = 0$ ,the electric field is ${ \bf E } = \partial _ { 0 } { \bf A }$ so its amplitude is $k ^ { 0 } a$ ,and the energy density is proportional to $( k ^ { 0 } a ) ^ { 2 }$ Since each photon carries an energy $k ^ { 0 }$ , we see that $k ^ { 0 } a ^ { 2 }$ is proportional to the number density of photons,so eq. (1.192) expresses the fact that, in the limit of geometric optics, the number of photons is conserved.

# Gravitational waves

We can now discuss the eikonal approximation for GWs. We make the ansatz

$$
\bar { h } _ { \mu \nu } ( x ) = [ A _ { \mu \nu } ( x ) + \varepsilon B _ { \mu \nu } ( x ) + \ldots ] e ^ { i \theta ( x ) / \varepsilon } .
$$

Again we define $k _ { \mu } = \partial _ { \mu } \theta$ ，and we write $A _ { \mu \nu } = A e _ { \mu \nu }$ where the polarization tensor $e _ { \mu \nu }$ is normalized as $e ^ { \mu \nu } e _ { \mu \nu } ^ { \ast } = 1$ ，and $A$ is the scalar amplitude. Substituting this ansatz into eqs.(1.177)and (1.179) and repeating basically the same steps as for the electromagnetic case,we find that $k _ { \mu }$ still obeys eqs.(1.187) and (1.188),so gravitons travel along the ull geodesic of $\hat { g } _ { \mu \nu }$ .Just as for photons,the scalar amplitude satisfies

$$
k ^ { \mu } \partial _ { \mu } A = - \frac { 1 } { 2 } ( \bar { D } _ { \mu } k ^ { \mu } ) A ,
$$

which can be written as $\bar { D } ^ { \mu } ( A ^ { 2 } k ^ { \mu } ) = 0$ ，and gives the conservation of the number of gravitons.Finally,the polarization tensor satisfies

$$
\begin{array} { r } { k ^ { \nu } e _ { \mu \nu } = 0 , } \\ { k ^ { \rho } \bar { D } _ { \rho } e _ { \mu \nu } = 0 , } \end{array}
$$

so it is transverse and is paralel-propagated along the null geodesics.

Since gravitons propagate along null geodesics, just as photons, their propagation through curved space-time is the same as the propagation fphotons,as long as geometric optics applies.For instance,they suffer gravitational deflection when passing neara massive body, with the same leflection angle as photons,and they undergo the same redshift in a gravitational potential.32

One practical difference concerning the lensing of gravitational and electromagnetic waves is however worth observing. Both type of waves an in principle be lensed by a large mass situated between the source and the observer. When the different images of the source cannot be resolved we are in the regime of microlensing,where we have a single mage which is magnified. The amplification factor $\mathcal { A }$ in the energy lensity,computed within geometric optics, $\mathrm { i s } ^ { 3 3 }$

$$
\mathcal { A } = \frac { u ^ { 2 } + 2 } { u \sqrt { u ^ { 2 } + 4 } } \approx \frac { 1 } { u } ,
$$

where $u = \beta / \theta _ { E }$ ， $\beta$ is the angle of the source with respect to the observerens axis (see Fig. 1.5), and $\theta _ { E }$ is the Einstein angle,given by

$$
\theta _ { E } ^ { 2 } = \frac { 2 R _ { S } d _ { \mathrm { S L } } } { d _ { \mathrm { O L } } ( d _ { \mathrm { S L } } + d _ { \mathrm { O L } } ) } ,
$$

where $R _ { S }$ is the Schwarzschild radius of the lens and $d _ { \mathrm { S L } }$ and $d _ { \mathrm { O L } }$ are Ihe source-lens and observer-lens distances,respectively. The second quality in eq.(1.197) holds when $u \ll \left| 1 \right.$ ，i.e．when the source,lens Md observer are well aligned,and in this case the amplification factor Blarge.In fact,it even becomes formally infinite if $u = 0$ ,i.e.when the ource,lens and observer are perfectly aligned. However,the geometric

32The redshift of gravitons in a FRW cosmological model will be discussed explicitly in Section 4.1.4.

33See e.g. Binney and Merrifield (1998).

![](images/7c1d52dad3cbb9a008c9616199d55a49e13ccf08e5db2fe94bf6a87870587616.jpg)  
Fig.1.5 The geometry for the lensing of gravitational or electromagnetic waves.

![](images/634e78d3835332df234614c760416a4a0d303fa3bdc079e6e11588c837e7642e.jpg)  
Fig.1.6 The focusing of GWs from a source.

optics approximation breaks down near the caustics,i.e. when the light rays coming from the source cross each other, since there the scale of variation of the wavefront is no longer small compared to .

The actual behavior near the caustics can be obtained taking into ac count diffraction (or, in a quantum language,the uncertainty principle) In order of magnitude the effect can be estimated as follows. Consider a circular ring of rays, which is part of a plane wavefront,arriving with impact parameter $b$ on a star of mass $M$ which acts as a gravitational lens,as in Fig. 1.6. The deflection angle due to the gravitational field of the star is given by the classical Einstein result, $\theta = 2 R _ { S } / b$ where $R _ { S } = 2 G M / c ^ { 2 }$ is the Schwarzschild radius of the star. The whole circular ring of rays with impact parameter $b$ is then focused on a single point,at a focal distance $d _ { F }$ given by $b / d _ { F } = \tan \theta \simeq \theta$ i.e.

$$
d _ { F } \simeq \frac { b ^ { 2 } } { 2 R _ { S } } .
$$

The fact that a one-dimensional surface is focused onto a point is responsible for the formal infinite enhancement of the luminosity. In practice however,diffraction forbids such a perfect focusing. Indeed,when we state that a photon has impact parameter b,we are implicitly assuming that the error $\Delta y$ on its transverse position is smaller than $b$ Then, by the Heisenberg principle,it has an uncertainty on the transverse mo mentum $\Delta k _ { y } \gtrsim \hbar / b$ , and an angular spreading

$$
\Delta \theta _ { s } \simeq \frac { \Delta k _ { y } } { k _ { x } } \gtrsim \frac { \ddagger } { b } .
$$

Propagating to a distance $d _ { F }$ this induces a transverse spread

$$
\Delta y _ { s } \simeq d _ { F } \Delta \theta _ { s } \gtrsim \frac { \dot { x } b } { 2 R _ { S } } .
$$

The focusing is substantial only if $\Delta y _ { s } \ll b$ ，which gives

$$
\begin{array} { r } { \dot { x } \ll 2 R _ { S } . } \end{array}
$$

For a lens with a mass of order $M _ { \odot }$ , this means that a substantial focusing is possible only for waves with $\lambda \ll O ( 6 )$ km,i.e.a frequency $f \gg O ( 1 0 ) ~ \mathrm { k H z } . ^ { 3 4 }$ For electromagnetic waves in the visible spectrum, this condition is very well satisfied,and microlensing is indeed commonly observed. For GWs, however,we will see that no astrophysical source is expected to produce waves with frequencies much larger that $O ( 1 0 ) ~ \mathrm { k H z }$ , and no significant amplification can be obtained for these waves from typical stellar-mass lenses.

# 1.5.2 Absorption and scattering of GWs

Finally, GWs are insensitive to absorption and scattering,during their propagation from astrophysical sources to the observer, because of the smallness of the gravitational cross-section. To make a quantitative

estimate,recall that the mean free path $l$ of a particle scattering off an ensemble of target with number density $n$ and cross-section $\sigma$ ,is given by

$$
l = { \frac { 1 } { n \sigma } } .
$$

For a graviton of energy $E$ ,the scatterting cross-section off a target of mass $m$ is (using units $\hbar = c = 1$ $\sigma \sim G _ { N } ^ { 2 } s$ ，where $s$ is the square of the center-of-mass energy.35 Consider for instance the scatering of a graviton with four-momentum $k ^ { \mu } = (  { \lvert { E } , { 0 } , { 0 } , E } )$ off a nucleon at rest, with four-momentum $p ^ { \mu } = ( m _ { n } , 0 , 0 , 0 ) ,$ where the mass $m _ { n } \sim 1 \mathrm { G e V }$ Then the square of the center-of-mass energy is $s = - ( p + k ) ^ { 2 } = m _ { n } ^ { 2 } +$ $2 m _ { n } E$ Forall astrophysically plausible values of the GW frequency $\int _ { \mathbb { S } ^ { W } }$ , $E = \hbar \omega _ { \mathrm { g w } }$ is totally negligible withrespectto $m _ { n }$ For instance, if $\mathrm { f _ { g w } = 1 \ k H z }$ ,we have $\dot { \hbar \omega } _ { \mathrm { g w } } = \dot { O } ( 1 0 ^ { - 2 1 } ) \big \vert \mathrm { G e V }$ ; so $s \simeq m _ { n } ^ { 2 }$ and

We can now compare the absorption of electromagnetic and of gravitational waves,for instance from the Sun. For photons in a neutral plasma, such as the Sun, the most important process is the Thompson scattering on electrons,which has a cross-section $\sigma = 8 \pi \alpha ^ { 2 } / ( 3 m _ { e } ^ { 2 } )$ ，where $a \simeq 1 / 1 3 7$ is the fine-structure constant,and we use units $\hbar = c = 1$ Inserting the numerical values,we see that the Thomson cross-section lor scattering of photons on electrons is larger than the gravitational tross-section for scattering of gravitons on nucleons,eq. (1.204)，by a huge factor $O ( 1 0 ^ { 8 0 } )$ .The number density $n _ { e }$ of electrons in the Sun which is relevant for computing the electromagnetic mean free path dme to electron-photon scattering) is about the same as the number lensity of protons,relevant to compute the gravitational mean free path de to proton-graviton scattering, so the mean-free path for gravitons m the Sun is larger by a factor $\stackrel { \textstyle \bigcup } { O } \big ( 1 0 ^ { 8 0 } \big )$ compared to that of photons! Using the value of $n _ { e }$ of the Sun,one fnds that the photon mean free path inside the Sun is $O ( 1 )$ cm. Using this value of $\it l$ ,one can show that photon produced by thermonuclear reactions in the Sun core takes about $3 \times 1 0 ^ { 4 }$ yr to reach the surface df the Sun and finally escape.36 For a graviton the mean free path inside the Sun is ${ \cal O } ( 1 0 ^ { 8 0 } )$ cm,which Bhuge even compared to the observable size of the Universe (consider tat $1 \mathrm { G p c } \simeq 3 \times 1 0 ^ { 2 7 }$ cm). Therefore,for a GW the Sun is completely transparent.

35This can be shown most easily using the field-theoretical methods of Chapter 2,observing that the gravitonmatter-matter vertex is proportional to $G _ { N } ^ { 1 / 2 }$ In the Feynman diagram for the graviton-matter scattering there are two such vertices,so the amplitude is proportional to $G _ { N }$ and the crosssection to $G _ { N } ^ { 2 }$ The dependence on $s$ is then fixed by dimensional arguments observing that,in units $\hbar = c = 1$ $G _ { N }$ is an inverse mass squared,as well as from Lorentz invariance,that dictates that the energy dependence is through the Lorentz-invariant quantity $s$ This is the same result that holds (at energies $E \ll M _ { W }$ ）for neutrinos,with the Fermi constant $G _ { F }$ replacing Newton's constant $G _ { N }$

Significant absorption of GWs can take place if the wave impinges on black hole. In this case,we can use the result for the capture cross ection ofarelativistic particle by a black hole with Schwarzschild radius Rs, $\sigma = ( 2 7 / 4 ) \pi R _ { S } ^ { 2 }$ .37 Another possibility is that the GW impinges on meutron star, just with the right frequency to excite one of its normal modes. In this case,the wave interacts coherently with the neutron star while, in the above estimate of scattering in the Sun，we computed he incoherent scattering off the single protons). However,as we see in microlensing experiments,the probability that a compact object lies on he path from an astrophysical source td the Earth is very small.

36See e.g.Exercise 1.2 of Maggiore (2005).

37See e.g. Landau and Lifshitz, Vol. I1 (1979),Section 102.

# 1.6Solved problems

# Problem 1.1. Linearization of the Riemann tensor in curved space

In this problem we compute the Riemann and Ricci tensors, linearized to first order in $h _ { \mu \nu }$ over a generic curved background $\bar { g } _ { \mu \nu }$ .The inversion of $g _ { \mu \nu } = \bar { g } _ { \mu \nu } + h _ { \mu \nu }$ is $g ^ { \mu \nu } = \bar { g } ^ { \mu \nu } - h ^ { \mu \nu } + O ( h ^ { 2 } )$ Then it is straightforward to find that,to $O ( h )$ ,the linearization of the Christoffel symbol gives

38We make use of the identity $[ \bar { D } _ { \nu } , \bar { D } _ { \alpha } ] h _ { \mu } { } ^ { \alpha } = h ^ { \alpha \beta } \bar { R } _ { \alpha \mu \beta \nu } - h _ { \mu } { } ^ { \tau } \bar { R } _ { \tau \nu } ,$ which follows from the definition of covariant derivative， see e.g.Weinberg (1972)，eq. (6.5.3).Pay attention to the fact that Weinberg has the opposite sign convention for the Riemann tensor.

The calculation of the Riemann tensor at a given point $_ x$ is enormously simplified if we perform it in a coordinate system where $\bar { \Gamma } _ { \nu \rho } ^ { \mu } ( x ) = 0$ （paying attention, of course, to the fact that the derivatives of $\bar { \Gamma } _ { \nu \rho } ^ { \mu }$ are non-zero!) We see from eq.(1.205) that in this frame $\Gamma _ { \nu \rho } ^ { \mu } = { \cal O } ( h )$ and therefore the terms $\sim \Gamma \Gamma$ in the Riemann tensor are ${ \dot { \operatorname { \mathcal { O } } } } ( h ^ { 2 } )$ ， so they do not contribute to $O ( h )$ and we simply have $R ^ { \mu } { } _ { \nu \rho \sigma } = \partial _ { \rho } \Gamma _ { \nu \sigma } ^ { \mu } - \partial _ { \sigma } \Gamma _ { \nu \rho } ^ { \mu } + O ( h ^ { 2 } )$ .Furthermore,substituting eq. (1.205） for $\Gamma _ { \nu \rho } ^ { \mu }$ ， we only need to keep the terms where the derivative acts on the background Christoffel symbols $\bar { \Gamma } _ { \nu \rho } ^ { \mu }$ , since_background Christoffel symbols on which no derivative act give zero. Since $\bar { \Gamma } _ { \nu \rho } ^ { \mu } ( x ) = 0$ in the final expression (i.e. after having performed all derivatives) we are free to write derivatives as covariant derivatives with respect to the background,and we obtain an expression valid in all coprdinate systems.

$$
\Gamma _ { \nu \rho } ^ { \mu } = \bar { \Gamma } _ { \nu \rho } ^ { \mu } + \frac { 1 } { 2 } \bar { g } ^ { \mu \sigma } \left( \bar { D } _ { \nu } h _ { \rho \sigma } + \bar { D } _ { \rho } h _ { \nu \sigma } - \bar { D } _ { \sigma } h _ { \nu \rho } \right) .
$$

Then, in the frame where $\bar { \Gamma } _ { \nu \rho } ^ { \mu } ( x ) = 0$ ，we get

$$
\begin{array} { r } { R _ { \mu \nu \rho \sigma } = \bar { R } _ { \mu \nu \rho \sigma } + \frac { 1 } { 2 } ( \bar { D } _ { \rho } \bar { D } _ { \nu } h _ { \mu \sigma } ) + \bar { D } _ { \sigma } \bar { D } _ { \mu } h _ { \nu \rho } - \bar { D } _ { \rho } \bar { D } _ { \mu } h _ { \nu \sigma } - \bar { D } _ { \sigma } \bar { D } _ { \nu } h _ { \mu \rho } } \\ { + h _ { \mu } { ' } \bar { R } _ { \tau \nu \rho \sigma } - h _ { \nu } { ' } \bar { R } _ { \tau \mu \rho \sigma } ) . \qquad ( 1 , 2 ) \qquad \mathrm { ~ a ~ n ~ d ~ } \qquad \rho \to 0 , } \end{array}
$$

We have performed the computation in a special frame. Since, however,the final result is expressed in terms of covariant quantities, this expression holds $R _ { \mu \nu } = g ^ { \alpha \beta } R _ { \alpha \mu \beta \nu } = ( \bar { g } ^ { \alpha \beta } - h ^ { \alpha \beta } ) ( \bar { R } _ { \alpha \mu \beta \nu } + R _ { \alpha \mu \beta \nu } ^ { ( 1 ) } )$ $h _ { \mu \nu }$ is $R _ { \mu \nu } ^ { ( 1 ) } = \bar { g } ^ { \alpha \beta } R _ { \alpha \mu \beta \nu } ^ { ( 1 ) } - h ^ { \alpha \beta } \bar { R } _ { \alpha \mu \beta \nu }$ Then wegy,S

$$
R _ { \mu \nu } ^ { ( 1 ) } = { \frac { 1 } { 2 } } \left( \bar { D } ^ { \alpha } \bar { D } _ { \mu } h _ { \nu \alpha } + \bar { D } ^ { \alpha } \bar { D } _ { \nu } h _ { \mu \alpha } - \bar { D } ^ { \alpha } \bar { D } _ { \alpha } h _ { \mu \nu } - \bar { D } _ { \nu } \bar { D } _ { \mu } h \right) ,
$$

where $h = \bar { g } ^ { \alpha \beta } h _ { \alpha \beta }$ .Observe that $\bar { D } _ { \nu } \bar { D } _ { \mu } h = \bar { D } _ { \nu } \partial _ { \mu } h = \partial _ { \nu } \partial _ { \mu } h - \tilde { \Gamma } _ { \nu \mu } ^ { \rho } \partial _ { \rho } h$ is symmetric under the exchange $\mu  \nu$ and therefore $R _ { \mu \nu } ^ { ( 1 ) }$ is also symmetric, as it should be.

If the background is fat, $\bar { g } _ { \mu \nu } = \eta _ { \mu \nu }$ , the covariant derivatives become ordinary derivatives and therefore commute. If we impose the Lorentz gauge condition $\partial ^ { \mu } \bar { h } _ { \mu \nu } = 0$ ,i.e $\partial ^ { \mu } h _ { \mu \nu } = ( 1 / 2 ) \partial _ { \nu } h$ ，the linearized Ricci tensor takes a very simple form,

$$
R _ { \mu \nu } ^ { ( 1 ) } = - { \frac { 1 } { 2 } } \sqcap h _ { \mu \nu } ,
$$

(flat background).

![](images/627a46b957a56560e2860f8bd680cb20d998006605a51863c0738ec5190398d0.jpg)

Problem1.2.Gaugtranfatiof $h _ { \mu \nu }$ and $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$

In the text we showed that,when the background space-time is $\eta _ { \mu \nu }$ ,theresulting linearized theory has a gauge symmetry given by eq.(1.8)，and that the linearized Riemann tensor $\bar { R } _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ is gauge-invariant.Itisinterestingto see how these results are modified when the background space-time is curved.

Under the coordinate transformation $x ^ { \mu }  x ^ { \prime \mu } = x ^ { \mu } + \xi ^ { \mu } ( x )$ ,the usual transformation law of the metric is

$$
g _ { \mu \nu } ( x )  g _ { \mu \nu } ^ { \prime } ( x ^ { \prime } ) = \frac { \partial x ^ { \rho } } { \partial x ^ { \prime \mu } } \frac { \partial x ^ { \sigma } } { \partial x ^ { \prime \nu } } g _ { \rho \sigma } ( x ) .
$$

Writing $g _ { \mu \nu } ^ { \prime } ( x ) = g _ { \mu \nu } ^ { \prime } ( x ^ { \prime } - \xi )$ and expandingto first order in $\xi$ we have

$$
g _ { \mu \nu } ^ { \prime } ( x ) \simeq \stackrel { \cdot } { g _ { \mu \nu } ^ { \prime } } ( x ^ { \prime } ) - \not \varsigma ^ { \rho } \partial _ { \rho } g _ { \mu \nu } ^ { \prime } .
$$

Combining this with eq.(1.209) we get

$$
g _ { \mu \nu } ^ { \prime } ( x ) = g _ { \mu \nu } ( x ) - ( D _ { \mu } \pounds _ { \nu } + D _ { \nu } \xi _ { \mu } ) ,
$$

where the covariant derivative is

$$
D _ { \mu } \xi _ { \nu } = \partial _ { \mu } \xi _ { \nu } - \Gamma _ { \mu \nu } ^ { \rho } \xi _ { \rho } .
$$

Equation (1.211) gives the lowest-order terni in the small parameter $| D _ { \mu } \xi _ { \nu } |$ Similar to what we have done in linearized theory,we restrict ourselves to $| D _ { \mu } \xi _ { \nu } | \lesssim h$ where $h = O ( | h _ { \mu \nu } | )$ Since $\Gamma _ { \mu \nu } ^ { \rho } = O ( \partial g _ { \mu \nu } ) = O ( 1 / L _ { B } )$ ,where $L _ { B }$ is the typical variation scale of the background metric,the condition $| D _ { \mu } \xi _ { \nu } | \lesssim h$ means that both

$$
| \partial \xi | \lesssim h , \mathrm { a n d } \{ \lesssim h L _ { B } , 
$$

must be satisfied. (We use the notation $\xi \equiv O ( | \xi ^ { \mu } | )$ ） In the case of a fat background metric,discussed in Section 1.1,we have $L _ { B } = \infty$ and therefore we found only the condition $| \partial \xi | \lesssim h$

A generic function $\xi ^ { \mu }$ has both low-frequency and high-frequency modes, without a clear separation between them,and therefore in the transformed metric $g _ { \mu \nu } ^ { \prime } ( x )$ the separation between the background and the GW in general disappears. It is therefore more useful to restrict ourselves to functions $\xi ^ { \mu }$ which maintain a clear-cut separation between low- and high-frequencies. In particular,we can consider a function $\xi ^ { \mu }$ that has only high-frequency modes. We observe that

$$
D _ { \mu } \xi _ { \nu } + D _ { \nu } \xi _ { \mu } = ( \bar { D } _ { \mu } \xi _ { \nu } + \bar { D } _ { \nu } \xi _ { \mu } ) + \xi ^ { \rho } ( \bar { D } _ { \mu } h _ { \nu \rho } + \bar { D } _ { \nu } h _ { \mu \rho } - \bar { D } _ { \rho } h _ { \mu \nu } ) ,
$$

where we have used the expansion (1.205） for the Christoffel symbol. Since $\tilde { \Gamma } _ { \nu \rho } ^ { \mu }$ is a purely low-frequency term，and $\xi ^ { \mu }$ has only high frequencies,the terins $\bar { D } _ { \mu } \xi _ { \nu }$ are purely high-frequency,and therefore contribute to the transformation of $h _ { \mu \nu }$ rather than of $\bar { g } _ { \mu \nu }$ .39 Therefore under such a transformation we have $\bar { g } _ { \mu \nu } ^ { \prime } ( x ) = \bar { g } _ { \mu \nu } ( x )$ and

$$
\boxed { \begin{array} { r l } & { \ddot { h _ { \mu \nu } ^ { \prime } } ( x ) \simeq h _ { \mu \nu } ( x ) - \big ( \bar { D } _ { \mu } \xi _ { \nu } + \bar { D } _ { \nu } \xi _ { \mu } \big ) , } \end{array} }
$$

under the condition that $\xi ^ { \mu }$ contains only high-frequencies and that it satisfies

$$
| \bar { D } _ { \mu } \xi _ { \nu } | \leqslant | h _ { \mu \nu } | .
$$

39Note that,since $| \partial \xi | \lesssim h$ and $| \xi | \lesssim h L _ { B }$ ,the terms $\xi \bar { D } h$ in eq. (1.214) are at most $O ( h ^ { 2 } L _ { B } / \hbar )$ .When the curvature is dominated by matter we found in Section 1.4.2 that $h \ll \dot { \lambda } / L _ { B }$ ， and therefore in eq.(1.214) the term $\xi \bar { D } h$ is negligible with respect to the term $\bar { D } _ { \mu } \xi _ { \nu } ^ { \mathrm { ~ \tiny ~ \cdot ~ } }$ ．In the opposite limit of curvature dominated by GWs we have $h \sim \dot { \lambda } / L _ { B }$ and the term $\xi \bar { D } h$ becomes of the same order as $\cal { D } _ { \mu } \xi _ { \nu }$ ，but not larger；therefore,even in this limit, the order-of-magnitude estimates given below are not affected when neglecting the term $\xi \vec { D } h$ 、

Equation (1.215) has the form of a gauge transformation for a symmetric tensor field $h _ { \mu \nu }$ on a curved space described by $\bar { g } _ { \mu \nu }$ . In this sense,we have a gauge theory for a spin-2 field in a curved background.We next compute how the linearized Riemann tensor transforms under this gauge transformation. We write

$$
R _ { \mu \nu \rho \sigma } = \bar { R } _ { \mu \nu \rho \sigma } + R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } + O ( h ^ { 2 } ) ,
$$

where $\bar { R } _ { \mu \nu \rho \sigma }$ is the Riemann tensor of the background and we raise and lower indices with $\vec { g } _ { \mu \nu }$ . The explicit calculation performed in Problem 1.1 gives

$$
2 R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } = \bar { D } _ { \rho } \bar { D } _ { \nu } h _ { \mu \sigma } + \bar { D } _ { \sigma } \bar { D } _ { \mu } h _ { \nu \rho } - \bar { D } _ { \rho } \bar { D } _ { \mu } h _ { \nu \sigma } - \bar { D } _ { \sigma } \bar { D } _ { \nu } h _ { \mu \rho } + h _ { \mu } ^ { \tau } \bar { R } _ { \tau \nu \rho \sigma } - h _ { \nu } ^ { \tau } \bar { R } _ { \tau \mu \rho \sigma } ,
$$

which generalizes eq. (1.13) to a curved background. Under the gauge trans formation (1.215)thevariation of $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ is given by

$$
\begin{array} { r l } & { \delta R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } = \xi ^ { \tau } \bar { D } _ { \tau } \bar { R } _ { \mu \nu \rho \sigma } + \bar { R } _ { \tau \nu \rho \sigma } \bar { D } _ { \mu } \xi ^ { \tau } - \bar { R } _ { \tau \mu \rho \sigma } \bar { D } _ { \nu } \xi ^ { \tau } } \\ & { \quad \quad \quad \quad \quad + \bar { R } _ { \mu \nu \tau \rho } \bar { D } _ { \sigma } \xi ^ { \tau } - \bar { R } _ { \mu \nu \tau \sigma } \bar { D } _ { \rho } \xi ^ { \tau } . } \end{array}
$$

Thereforeifthebackgroundisnotfat $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ is no longer gauge invariant under the gauge transformations of linearized theory. However,let us estimate the order of magnitude of the various terms.For the background we have

$$
\bar { R } _ { \mu \nu \rho \sigma } \sim \partial ^ { 2 } \bar { g } _ { \mu \nu } \sim { \frac { 1 } { L _ { B } ^ { 2 } } } \ , \qquad \bar { D } _ { \tau } \bar { R } _ { \mu \nu \rho \sigma } \sim \partial ^ { 3 } \bar { g } _ { \mu \nu } \sim { \frac { 1 } { L _ { B } ^ { 3 } } } ,
$$

Equation (1.216) gives instead $\xi \sim h L _ { B }$ ， $\bar { D } \xi \sim h$ and we therefore see that

$$
\delta R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } \sim \frac { h } { L _ { B } ^ { 2 } } .
$$

This means that the variation of $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ is much smaller than $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ itself, since

$$
R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } \sim \partial ^ { 2 } h \sim \frac { h } { { \chi } ^ { 2 } }
$$

and therefore

$$
\delta R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } \sim \frac { \mathfrak { X } ^ { 2 } } { L _ { B } ^ { 2 } } R _ { \mu \nu \rho \sigma } ^ { ( 1 ) } .
$$

We conclude that $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$ isaoitely $\Upsilon / L _ { B } \ll$   
1. More precisely,its leading term in an expansion in powers of $\scriptstyle \sum \big / L _ { B }$ is gauge   
invariant.Therefore,in the limit $\bar { \lambda } / L _ { B } \ll 1$ ，which was used from the very $h _ { \mu \nu }$ ve ay he $h _ { \mu \nu }$ ing temne fie h as obteiny ran $R _ { \mu \nu \rho \sigma } ^ { ( 1 ) }$   
eq. (1.218).

# Further reading

·Classical textbooks on general relativity are Weinberg (1972)，Misner,Thorne and Wheeler (1973), and Landau and Lifshitz, Vol. II (1979).Among the more recent books，we suggest Hartle (2003) (at a rather introductory level,and with a very physical approach)，and Straumann (2004) (more advanced).

·Fordiscussions of freely falling frames,Riemann and Fermi normal coordinates,TT frame and the proper detector frame,see Misner,Thorne and Wheeler (1973)，Sections 13.6 and 37.2，Hartle (2003), Section 8.4,and Thorne (1983,1987). The metric of an accelerated,rotating observer is com-puted to quadratic order in $x ^ { i }$ by $\mathrm { N i }$ and Zimmermann (1978).

·The energy-momentum tensor of GWs and the short-wave expansion are discussed by Isaacson (1968a，1968b)，Misner，Thorne and Wheeler (1973)，and Thorne (1987).The fact that performing a space-time average one obtains a gaugeinvariant energy-momentum tensor was already discussed in Arnowitt,Deser and Mlsner (1961).

·The geometric optics approximation in curved space-time is discussed in Isaacson (1968a,1968b) and Misner，Thorne and Wheeler (1973)(see in particular Section 22.5 for photons,and Section 35.14 and Exercise 35.15 forgravitational waves).See also Thorne (1983,1987).Diffraction and lensing of GWs is discussed in Bontz and Haugan (1980) and in Section 2.6.1 of Thorne (1983).

·A definition of GWs based on the asymptotics of the gravitational feld at nullinfinity was given by

Bondi,van der Burg and Metzner (1962) and Sachs (1962),and was also important historically for resolving the controversy on the reality of gravitational radiation．A geometric description of the asymptotic fall-off of radiative solutions,using the notion of asymptotically simple space-time，was given by Penrose (1963,1965).

The development of the concept of gravitational wave has a very interesting history. The notion even predates Einstein general relativity (the term "gravitational wave”was used by Poincaré as early as l905,referring to the fact that,even ina gravitational theory, the interaction must propagate at a finite speed).With the advent of general relativity,gravitational waves were introduced by Einstein in 19l6．However,the existence of physical effects associated with them has been questioned many times,with Einstein himself changing his mind more then once. Eddington is associated to the ironic remark that “gravitational waves propagate at the speed of thought”,implying that they are gauge artifact.(Actually, he was referring only to the transverse-longitudinal and longitudinal-longitudinal components of $h _ { i j }$ ,which, indeed，are pure gauge modes. Conccrning the transverse-transverse part,he rather showed that it carries energy,and even corrected an erroneous factor of two in Einstein's early version of the quadrupole formula.） The controversy on the existence of GWs was not settled until the early 1960s.A very interesting book on the history of the research in GWs is Kennefick (2007),see also the review article Kennefick (1997).

# 2

# The field-theoretical approach to GWs

2.1 Linearized gravity and   
classical field theory 53   
2.2 Gravitons 66   
2.3 Massive gravitons 81   
2.4 Solved problems 95

In the previous chapter we investigated GWs using the geometric interpretation which is at the core of general relativity. This geometrical perspective emphasizes that $g _ { \mu \nu } = \bar { g } _ { \mu \nu } + h _ { \mu \nu }$ is the metric of spacetime,and therefore an incoming GW $h _ { \mu \nu }$ induces perturbations in the space-time geometry. In this approach, the interaction of GWs with test masses is described by geometric tools such as the equation of the geodesic deviation,and the energy momentum tensor of GWs is determined by examining how $h _ { \mu \nu }$ contributes to the curvature of the background space-time.

General relativity can also be seen as a classical field theory, to which we can apply all standard field-theoretical methods. In this chapter we therefore go back to linearized gravity, writing $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu }$ ,and we treat it as a classical field theory of the feld $h _ { \mu \nu }$ living in flat space-time with Minkowski metric $\eta _ { \mu \nu }$ . Inthis approach we are actually forgetting that $h _ { \mu \nu }$ has an interpretation in terms of a space-time metric,and instead we treat it as any other field living in flat Minkowski space.

The fact that the beautiful geometric interpretation of $h _ { \mu \nu }$ is hidden is compensated by the fact that we can put the conceptual issues discussed in Chapter 1 into the broader theoretical framework of classical field theory,and compare it to what happens in other field theories,such as classical electrodynamics. The geometric and the field-theoretical perspectives are indeed complementary; some aspects of GW physics can be better understood from the former perspective, some from the latter,and to study GWs from both vantage points results in a deeper overall understanding.

We will begin in Section 2.1.1by recalling a basic tools of classical feld theory, the Noether theorem,and we will see how we can reobtain the results of Chapter 1 using this standard field-theoretical tool. Besides providing a complementary understanding of various conceptual issues, the Noether theorem is also a very practical tool for explicit computa-tions,and in particular we willsee that it also provides the simplest way of deriving another important result, namely the general expression for the angular momentum carried by GWs.

In Section 2.2 we will pursue this field-theoretical approach further, discussing linearized gravity from the point of view of quantum field theory,and we will see how the notion of the graviton emerges. Actually,all astrophysical mechanisms of GW production,as well as the interaction of GWs with a detector,are fully accounted for by classical general relativity. In actual calculations,the notion of the graviton will not surface until we examine some cosmological production mechanisms (in particular,mechanisms related to the amplification of vacuum fluctuations),in Vol.2.Nevertheless,we will see that also at the quantum level,the field-theoretical approach is illuminating for many conceptual aspects.

We will conclude this chapter with a more advanced section,which investigates whether gravitons can have a small mass. This,from the feld-theoretical point of view,seems to be one of the most natural generalizations of Einstein gravity.We willsee however that a field theory describing massive gravitons can have problems of internal consistency which,to date,are not yet fully understqod.

# 2.1 Linearized gravity as a classical field theory

# 2.1.1 Noether's theorem

We begin by recaling some basic facts of classical field theory and in particular Noether's theorem.1 We consider a field theory living in fat space-time,with fields $\phi _ { i }$ ,labeledbyan index $i$ .The action $S$ isthe integral of the Lagrangian density $\mathcal { L }$ ，

$$
S = \int d t d ^ { 3 } x \mathcal { L } ( \phi _ { \dagger } , \partial \phi _ { i } ) .
$$

In our case the felds $\phi _ { i }$ will be the independent components of the metric $h _ { \mu \nu }$ ,but it is uscful to be more general,since we will also be interested in comparing with for instance classical electrodynamics,or any other dlassical field theory.We willdenote collectively the fields $\phi _ { i }$ simply by 0

A transformation of the coordinates and of the fields is an operation that transforms the coordinates $x ^ { \mu }$ into new coordinates $x ^ { \prime \mu }$ ,i.e. $x ^ { \mu } $ $\tau ^ { \mu }$ ,while at the same time the fields,denoted collectively by $\phi ( x )$ ,are transformed into new functions of the new coordinates, $\phi ( x )  \phi ^ { \prime } ( x ^ { \prime } )$ To define the transformation means to state how $x ^ { \prime }$ is related to $x$ and low $\phi ^ { \prime } ( x ^ { \prime } )$ is related to $\phi ( x )$ .For an infinitesimal transformation,we canwrite

$$
\begin{array} { c } { { x ^ { \mu }  x ^ { \prime } { } ^ { \mu } = x ^ { \mu } + \epsilon ^ { a } A _ { a } ^ { \mu } ( x ) , } } \\ { { \phi _ { i } ( x )  \phi _ { i } ^ { \prime } ( x ^ { \prime } ) = \phi _ { i } ( x ) + \epsilon ^ { a } F _ { i , a } ( \phi , \partial \phi ) , } } \end{array}
$$

And the transformation is specified assighing $A _ { a } ^ { \mu } ( x )$ and $F _ { i , a } ( \phi , \partial \phi )$ In general,the function $F _ { i , a }$ depends on the collection of felds $\phi$ and on their derivatives,and will also mix different fields,so the transformation of a single field $\phi _ { i }$ can depend also on all other fields $\phi _ { j }$ with $j \neq i$ The above transformation is parametrized by a set of infinitesimal parameters .with $a = 1 , \ldots , N$

1We refer the reader to the textbook Maggiore (2005)，Section 3.2,for further details and proofs.Note that in the present book,in order to follow the most common convention in general relativity,we are using the signature $\eta _ { \mu \nu } = ( - , + , + , + )$ whilein Maggiore (2005） we use $\eta _ { \mu \nu } = ( + , - , - , - ) ,$ which is the most common convention in quantum feld theory.This is the origin of some sign differences between that textbook and the following equations.

Equations (2.2) and (2.3) define a symmetry transformation if they leave the action S(Φ) invariant,for anyΦ.A symmetry transformation is called global if it leaves the|action invariant when the parameters e are constant,and local if it leaves invariant the action even when $\epsilon ^ { a }$ are allowed to be arbitrary functions of $x$

Noether's theorem states that,for each generator of a global symmetry transformation, that is,for each of the parameters $\epsilon ^ { a }$ with $a = 1 , \ldots , N$ there is a current ${ j _ { \alpha } ^ { \mu } }$ (which is|a functional of the felds $\phi$ ）which,when evaluated on a classical solution of the equations of motion cl,is conserved,i.e.satisfies

$$
\left( \partial _ { \mu } \ j _ { a } ^ { \mu } \right) | _ { \phi = \phi ^ { \mathrm { c l } } } = 0 .
$$

The corresponding charges $Q _ { a }$ are defined as the spatial integral of the $\mu = 0$ component of the currents

$$
Q _ { a } \equiv \int d ^ { 3 } x j _ { a } ^ { 0 } ( { \bf x } , t ) .
$$

Current conservation (in the sense of eq. (2.4)) implies that Q& is conserved (in the sense that it is time-independent). In fact

$$
\begin{array} { c } { { \displaystyle \partial _ { 0 } Q _ { a } = \int d ^ { 3 } x \partial _ { 0 } j _ { a } ^ { 0 } ( { \bf x } , t ) } } \\ { { \displaystyle = - \int d ^ { 3 } x \partial _ { i } j _ { a } ^ { i } ( { \bf x } , t ) . } } \end{array}
$$

This is the integral of a total divergence,and it vanishes if we assume a sufficiently fast decrease of the fields at infinity. More generally,in a finite volume the variation of the charge is given by a boundary term representing the incoming or outgoing flux.

The explicit form of the current can be written in ful generality in terms of the Lagrangian density $\mathcal { L }$ of the theory and of the functions $A _ { \alpha } ^ { \mu } ( x )$ and $F _ { i , \alpha } ( \phi , \partial \phi )$ that define the symmetry transformation (2.2). (2.3),and is given by

$$
j _ { a } ^ { \mu } = \frac { \partial \mathcal { L } } { \partial ( \partial _ { \mu } \phi _ { i } ) } \left[ A _ { a } ^ { \nu } ( x ) \partial _ { \nu } \phi _ { i } - F _ { i , a } ( \phi , \partial \phi ) \right] - A _ { a } ^ { \mu } ( x ) \mathcal { L } .
$$

The simplest application of this very general machinery is to the symmetry under space-time translations,and leads us to energy-momentum tensor. Under space-time translations we have $x ^ { \mu }  x ^ { \prime } { } ^ { \mu } = x ^ { \mu } + \epsilon ^ { \mu }$ ,and by definition al felds transform as $\phi _ { i } ^ { \prime } ( x ^ { \prime } ) = \phi _ { i } ( x )$ ,independently of their properties under Lorentz transformations; that is,a point $P$ has the coordinate $_ x$ in a frame and the coordinate $x ^ { \prime }$ in the translated frame, but the functional form of the felds changes so that the numerical values of the felds at the point P is invariant. So we write the transformation as

$$
\begin{array} { c } { { x ^ { \mu }  x ^ { \prime } { } ^ { \mu } = x ^ { \mu } + \epsilon ^ { \mu } } } \\ { { = x ^ { \mu } + \epsilon ^ { \nu } \delta _ { \nu } ^ { \mu } , } } \end{array}
$$

$$
\phi _ { i } ( x )  \phi _ { i } ^ { \prime } ( x ^ { \prime } ) = \phi _ { i } ( x ) .
$$

Observe that the index $^ a$ appearing in $\epsilon ^ { \alpha }$ in this case is a Lorentz index. Comparing with eqs. (2.2) and (2.3), we see that $A _ { \nu } ^ { \mu } = \delta _ { \nu } ^ { \mu }$ and $F _ { i , a } = 0$

The four conserved currents $\theta ^ { \mu } { } _ { \nu } \equiv - j _ { ( \nu ) } ^ { \mu }$ form a Lorentz tensor, known as the energy-momentum tensor.Using eq.(2.7) and raising the $\nu$ index, $\theta ^ { \mu \nu } = \eta ^ { \nu \rho } { \theta ^ { \mu } } _ { \rho }$ we get²

$$
\theta ^ { \mu \nu } = - \frac { \partial \mathcal { L } } { \partial ( \partial _ { \mu } \phi _ { i } ) } \partial ^ { \nu } \phi _ { i } + \eta ^ { \mu \nu } \mathcal { L } .
$$

Equation (2.4) becomes

$$
\partial _ { \mu } \theta ^ { \mu \nu } = 0 ,
$$

on the solutions of the classical equations of motion. The conserved charge associated to space-time translations is,by definition,the fourmomentum $P ^ { \nu }$ ,and therefore³

$$
\begin{array} { l } { { \displaystyle c P ^ { 0 } \equiv \int d ^ { 3 } x \theta ^ { 0 0 } , } } \\ { { \displaystyle c P ^ { i } \equiv \int d ^ { 3 } x \theta ^ { 0 i } . } } \end{array}
$$

This is the definition of four-momentum in classical field theory. A feld configuration,solution of the equations of motion, carries an energy $E = c P ^ { 0 }$ and a spatial momentum $P ^ { i }$ which can be calculated using eqs. (2.10), (2.12) and (2.13).

Observe that in general relativity the|energy-momentum tensor of matter,defined by eq. (1.2),is automatically symmetric in the two indices $\mu , \nu$ ，since it is obtained by taking the functional derivative of the action with respect to the symmetric tensor $g _ { \mu \nu }$ .In contrast,the energy-momentum tensor defined from Nbether's theorem,eq.(2.10),is not necessarily symmetric in the two indices $\mu , \nu$

In fact,it is important to understand that the formal machinery of the Noether theorem，without some further physical input,is unable to uniquely fix the energy-momentum tensor,and more generally the Noether currents. For instance,consider what happens if we add a total four-divergence to the Lagrangian density,

$$
\begin{array} { r } { { } } \\ { { \mathcal { L } ^ { \prime } = \mathcal { L } + \partial _ { \mu } K ^ { \mu } ( \phi ) . } } \end{array}
$$

A total divergence,when integrated oven $d ^ { 4 } x$ ， gives a boundary term. The equations of motion of the classical theory are obtained from a variation of the action,holding fixed the value of the fields on the boundaries. Therefore the equations of motion obtained from the variation of the action $\begin{array} { r } { S ^ { \prime } = \int d ^ { 4 } x \mathcal { L } ^ { \prime } } \end{array}$ are the same as those obtained from the variation of $\begin{array} { r } { S = \int d ^ { 4 } x \mathcal { L } } \end{array}$ ,so these two Lagrangians define the same classical field theory.However,the currents obtained from eq.(2.7) using $\mathcal { L } ^ { \prime }$ or using $\mathcal { L }$ are in general different，and their difference is such that $j ^ { 0 }$ changes by a total spatial divergence,so that the charge in eq. (2.5) changes by a boundary term. Therefore the Noether currents are not uniquely defined; however, the Noether charges,computed integrating over a spatial volume $V$ ，are well defined if,and $\phi \mathrm { n l y }$ if,the felds inside $V$ go to zero sufficiently fast when we approach the boundaries of $V$ ，so that

$^ 2 \mathrm { { I n } }$ order to minimize the number of factors of $c$ in the equations,we have defined the fat-space Lagrangian density $\mathcal { L }$ from

$$
S = \int d t d ^ { 3 } x { \mathcal { L } } ,
$$

rather than from $\begin{array} { r c l } { { S } } & { { = } } & { { \int d ^ { 4 } x { \mathcal L } } } \end{array}$ as done,instead,in Landau and Lifshitz, Vol.II (1979)．Recalling that，dimensionally,an action is $\left( { \mathrm { e n e r g y } } \right) \times$ (time),in this way $\mathcal { L }$ has the same dimensions as $\theta ^ { \mu \nu }$ ,i.e.energy/volume. With our notation,for instance,the Lagrangian density of the electromagnetic field is $( - 1 / 4 ) F _ { \mu \nu } F ^ { \mu \nu }$ ，rather than $( - 1 / 4 c ) F _ { \mu \nu } F ^ { \mu \nu }$

3The factor $c$ provides the correct dimensions,recalling that $P ^ { 0 } = E / c$ see the Notation.

all boundary terms can be neglected, and the ambiguity in the currents becomes irrelevant.

To illustrate this point,before computing the energy-momentum tensor of GWs it is instructive to recall what happens in the more familiar case of classical electrodynamics. In this case the Lagrangian density is

$$
{ \mathcal L } _ { \mathrm { e m } } = - \frac { 1 } { 4 } F _ { \mu \nu } F ^ { \mu \nu } ,
$$

where $F _ { \mu \nu } = \partial _ { \mu } A _ { \nu } - \partial _ { \nu } A _ { \mu }$ With our signature $\eta _ { \mu \nu } = ( - , + , + , + )$ the relation of Fμv to the electric and magnetic fields is F0i = Ei and Fij = eijk Bk.Equation (2.10） gives

$$
\theta _ { \mathrm { e m } } ^ { \mu \nu } = - \frac { \partial \mathcal { L } _ { \mathrm { e m } } } { \partial ( \partial _ { \mu } \mathcal { A } _ { \rho } ) } \partial ^ { \nu } A _ { \rho } + \eta ^ { \mu \nu } \mathcal { L } _ { \mathrm { e m } } .
$$

The functional derivative is easily computed,

$$
\begin{array} { c } { { { \displaystyle { \frac { \partial } { \partial ( \partial _ { \mu } A _ { \rho } ) } } \left( - { \frac { 1 } { 4 } } F _ { \alpha \beta } F ^ { \alpha \beta } \right) = - { \frac { 1 } { 2 } } F ^ { \alpha \beta } { \displaystyle { \frac { \partial F _ { \alpha \beta } } { \partial ( \partial _ { \mu } A _ { \rho } ) } } } } } } \\ { { = - F ^ { \alpha \beta } { \displaystyle { \frac { \partial ( \partial _ { \alpha } A _ { \beta } ) } { \partial ( \partial _ { \mu } A _ { \rho } ) } } } } } \\ { { = - F ^ { \mu \rho } . } } \end{array}
$$

Therefore

$$
\theta _ { \mathrm { e m } } ^ { \mu \nu } = F ^ { \mu \rho } \partial ^ { \nu } A _ { \rho } - \frac { 1 } { 4 } \eta ^ { \mu \nu } F ^ { 2 } .
$$

At first sight, this result is surprising. Recallin fact that classical electrodynamics is invariant under gauge transformations,

$$
A _ { \mu } \longrightarrow A _ { \mu } - \partial _ { \mu } \theta ,
$$

as we can see observing that under eq. (2.19) Fμv is invariant,and therefore also the Lagrangian (2.15） is invariant. However,the energymomentum tensor (2.18) depends on Aμ not only through the gaugeinvariant combination Fμv，but also through the term dAp,which is not invariant, and under gauge transformations $\theta _ { \mathrm { e m } } ^ { \mu \nu }$ changes as

$$
\theta _ { \mathrm { e m } } ^ { \mu \nu } \longrightarrow \theta _ { \mathrm { e m } } ^ { \mu \nu } - F ^ { \mu \rho } \partial ^ { \nu } \partial _ { \rho } \theta .
$$

Apparently，we seem to be driven to the conclusion that the energy density 0oo of the electromagnetic|field (as well as the momentum density 00i） is not gauge invariant. To deal with this problem, one first of all rewrites the energy-momentum tensor as follows,

$$
\begin{array} { r l } { { \displaystyle \theta _ { \mathrm { e m } } ^ { \mu \nu } = F ^ { \mu \rho } ( \partial ^ { \nu } A _ { \rho } - \partial _ { \rho } A ^ { \nu } + \partial _ { \rho } A ^ { \nu } ) - \frac { 1 } { 4 } \eta ^ { \mu \nu } F ^ { 2 } } } & { { } } \\ { { } } & { { } } \\ { { \displaystyle = ( F ^ { \mu \rho } F ^ { \nu } { } _ { \rho } - \frac { 1 } { 4 } \eta ^ { \mu \nu } F ^ { 2 } ) + F ^ { \mu \rho } \partial _ { \rho } A ^ { \nu } } } & { { } } \\ { { } } & { { } } \\ { { \displaystyle = ( F ^ { \mu \rho } F ^ { \nu } { } _ { \rho } - \frac { 1 } { 4 } \eta ^ { \mu \nu } F ^ { 2 } ) + \partial _ { \rho } ( F ^ { \mu \rho } A ^ { \nu } ) . } } \end{array}
$$

(In the last line we used the equation of motion $\partial _ { \rho } F ^ { \mu \rho } = 0$ ）Therefore we have

$$
\theta _ { \mathrm { e m } } ^ { \mu \nu } = T _ { \mathrm { e m } } ^ { \mu \nu } + \partial _ { \rho } C ^ { \rho \mu \nu }
$$

where

$$
T _ { \mathrm { e m } } ^ { \mu \nu } = F ^ { \mu , \rho } { F ^ { \nu } } _ { \rho } - { \frac { 1 } { 4 } } \eta ^ { \mu \nu } F ^ { 2 } ,
$$

while $C ^ { \rho \mu \nu } = F ^ { \mu \rho } A ^ { \nu }$ is a tensor antisymmetric in the indices $( \rho , \mu )$ Now, $T _ { \mathrm { e m } } ^ { \mu \nu }$ (which is sometimes called the"improved”energy-momentum tensor）is a gauge-invariant quantity,and its OO component gives the usual form of the energy density,4

$$
T _ { \mathrm { e m } } ^ { 0 0 } ( x ) = \frac { 1 } { 2 } ( { \bf E } ^ { 2 } + { \bf B } ^ { 2 } ) ( x ) .
$$

The term $\partial _ { \rho } C ^ { \rho \mu \nu }$ instead is not gauge invariant,and we would like to get rid of it. The argument that is used to discard it is based on the following observations:

·If $\theta _ { \mathrm { e m } } ^ { \mu \nu }$ is conserved, also $T _ { \mathrm { e m } } ^ { \mu \nu }$ is coniserved: in fact

$$
\partial _ { \mu } \partial _ { \rho } C ^ { \rho \mu \nu } = 0
$$

automatically, whenever $C ^ { \rho \mu \nu }$ is antisymmetric under $\rho  \mu$ as is our case.

Thediference between the charge $c P ^ { \nu }$ computed with $\theta _ { \mathrm { e m } } ^ { \mu \nu }$ and that computed with $T _ { \mathrm { e m } } ^ { \mu \nu }$ is given bly

$$
\int _ { V } d ^ { 3 } x \partial _ { \rho } C ^ { \rho 0 \nu } = \int _ { V } d ^ { 3 } x \partial _ { i } C ^ { i 0 \nu } .
$$

where we used the fact that $C ^ { 0 0 \nu } \left| = 0 \right.$ ，which follows again from the antisymmetry of $C ^ { \rho \mu \nu }$ under $\rho _ { \rvert }  \mu$ . This is the integral of a divergence,and vanishes if the fields go to zero sufficiently fast at the boundaries of the volume $V$ .Therefore the four-momentum $P ^ { \nu }$ computed with $\theta _ { \mathrm { e m } } ^ { \mu \nu }$ is equal tothat computed with $T _ { \mathrm { e m } } ^ { \mu \nu }$ and is gauge invariant.

What we learn from this example is that the expression for the energymomentum tensor derived from the Noether theorem,eq.(2.1O),is not necessarilya physical observable (in the case of electromagnetism it is mot even gauge-invariant!).5 Rather, it is just a mathematical expres-Sion that，when integrated over space,gives unambiguously the total mergy and momentum of a classical feld configuration,as long as this held configuration goes to zero suffciently fast on the boundaries of the Integration region.

Equivalently,instead of speaking of the total energy of a localized object，we can divide by the volume and say that the expression in .(2.10) is a quantity that can be used to compute the average value fthe energy-momentum tensor over a region of space sufficiently large, 6 that all boundary terms vanish,and any ambiguity related to total livergences disappears. Then,for instance,from eq. (2.22) we have

$$
\langle \theta _ { \mathrm { e m } } ^ { 0 0 } \rangle = \langle T _ { \mathrm { e m } } ^ { 0 0 } \rangle + \langle \partial _ { i } C ^ { i 0 0 } \rangle ,
$$

4The use of the Lagrangian (2.15) implies that we are using Heaviside-Lorentz units (also called rationalized C.g.s.unit） for the electric charge；in unrationalized units the factor $( - 1 / 4 )$ in eq.(2.15）becomes $( - 1 / 1 6 \pi )$ ，and the factor $1 / 2$ in eq.(2.24) becomes $1 / ( 8 \pi )$

5 Another way of understanding the existence of such an ambiguity in a gauge theory is the fact that，in principle, one can allow that the gauge field,under space-time translations,does not go simply into itself,as in eq. (2.9),but into a configuration related by an arbitrary gauge transformation.

where the bracket represents the average. On a volume such that bound-ary terms give zero, we have $\bar { \langle } \partial _ { i } C ^ { i 0 0 } \rangle \stackrel { - } { = } 0$ and therefore the average is unambiguously defined,

$$
\begin{array} { r l r } { \langle \theta _ { \mathrm { e m } } ^ { 0 0 } \rangle = \langle T _ { \mathrm { e m } } ^ { 0 0 } \rangle } & { } & \\ { = \displaystyle \frac { 1 } { 2 } \langle { \bf E } ^ { 2 } + { \bf B } ^ { 2 } \rangle . } & { } & \end{array}
$$

Whether one of the many equivalent integrands, in the expression for cP0,can be promoted to a physical observable, thereby providing a definition of a local energy density, is a physical question that cannot be answered using only the mathematics of the Noether theorem, without any additional physical input.We will discuss this issue at the end of the next section，and we will see that in fact the answer is in general different in electromagnetism and in general relativity.

# 2.1.2 The energy-momentum tensor of GWs

Now we can return to our original problem,which was the computation of the energy carried by GWs. We consider a wave-packet with reduced wavelengths centered around a value . In this case,according to the discussion above, the Noether theorem can give us an unambiguous answer for the energy density of the wave-packet,averaged over a box centered on the peak of the wave-packet,and with size $L \gg \dot { x }$ In this case the field is negligible on the boundaries and, using eq. (2.10),

$$
t ^ { \mu \nu } = \langle - \frac { \partial \mathcal { L } | } { \partial ( \partial _ { \mu } h _ { \alpha \beta } ) } \partial ^ { \nu } h _ { \alpha \beta } + \eta ^ { \mu \nu } \mathcal { L } \rangle ,
$$

where $\langle . . . \rangle$ is a spatial average over several reduced wavelength (which, for plane waves, is the same as a temporal average over several periods), and L is the Lagrangian that governs the dynamics of huv.

As discussed in the previous subsection,the Noether theorem instead gives us an ambiguous answer' if we ask what is the local energy and momentum density. Actually, we already saw in Section 1.4 that the final form of the energy-momentum tensor of GWs is indeed expressed as an average over several reduced wavelengths (or over several periods),and that this comes from a very fundamental reason,i.e. in order to discuss the back-reaction of GWs on ithe background，we need to perform a coarse-graining of the Einstein equations. Thus,we already know that it will not be possible to do better than this,and we cannot define a local expression for the energy and momentum density. Nevertheless, it is interesting to understand the reason also from a purely field-theoretical point of view; this will be discussed at the end of this section. First,we compute $t ^ { \mu \nu }$ from eq. (2.29),and we check that it agrees with the result that we derived in Section 1.4.

In order to use eq. (2.29) (and also to derive the angular momentum of GWs from Noether's theorem),we need the Lagrangian L or,equivalently, the action governing theldynamics of the field $h _ { \mu \nu }$ . To reproduce the Einstein equations to linear order in $h _ { \mu \nu }$ we must expand the Einstein action to quadratic order in $h _ { \mu \nu }$ ,while the linear term in the action vanishes,as always when we expand around a classical solution (in this case around the flat metric $\eta _ { \mu \nu }$ ,since we consider Einstein equations in vacuum).We therefore start from the full Einstein action,

$$
S _ { E } = \frac { c ^ { 3 } } { 1 6 \pi G } \int d ^ { 4 } x \sqrt { - g } R ,
$$

and we expand $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu }$ .We observe that

$$
R = g ^ { \mu \nu } R _ { \mu \nu } = \left( \eta ^ { \mu \nu } - h ^ { \mu \nu } + { \cal O } ( h ^ { 2 } ) \right) \left( R _ { \mu \nu } ^ { ( 1 ) } + R _ { \mu \nu } ^ { ( 2 ) } + { \cal O } ( h ^ { 3 } ) \right) ,
$$

where $R _ { \mu \nu } ^ { ( 1 ) }$ is Iiner in $h$ and $R _ { \mu \nu } ^ { ( 2 ) }$ is quadratic in $h$ $R _ { \mu \nu } ^ { ( 1 ) }$ and $R _ { \mu \nu } ^ { ( 2 ) }$ can be obtained by specializing eqs.(1.113)and (1.114) to a flat background metric $\eta _ { \mu \nu }$ ．The expansion of $\scriptstyle { \sqrt { - g } }$ can be computed by writing $g _ { \nu } ^ { \mu } =$ $\delta _ { \nu } ^ { \mu } + h _ { \nu } ^ { \mu } \equiv ( I + H ) _ { \nu } ^ { \mu }$ ，where $I$ is the identity matrix and $H$ a matrix whose elements are $h _ { \nu } ^ { \mu }$ Since $g _ { \mu \nu } = \eta _ { \mu \rho } \dot { g } _ { \nu } ^ { \rho }$ and $\operatorname* { d e t } \eta _ { \mu \rho } = - 1$ ，we have $- g = \operatorname* { d e t } ( I + H )$ .Using the identity $\log ( \operatorname* { d e t } A ) = \operatorname { T r } ( \log A )$ valid for any non-degenerate matrix $A$ ,and expanding the logarithm,

$$
\begin{array} { l } { { \operatorname * { d e t } ( I + H ) = \exp \{ \log \operatorname * { d e t } ( I + H ) \} } } \\ { { \ = \exp \{ \mathrm { T r } \log ( I + H ) \} } } \\ { { \ = \exp \{ \mathrm { T r } [ H + O ( H ^ { 2 } ) ] \} } } \\ { { \ = 1 + \mathrm { T r } H \Big | + O ( H ^ { 2 } ) } } \\ { { \ = 1 + h + \mathcal { O } ( h _ { \mu \nu } ^ { 2 } ) \ , } } \end{array}
$$

where $h = h _ { \mu } ^ { \mu } = \eta ^ { \mu \nu } h _ { \mu \nu }$ is the trace of $h _ { \mu \nu }$ . Since we are expanding over fat space,the lowest non-zero term in $R$ isalready $O ( h )$ ,see eq. (2.31), so the terms $O ( h ^ { 2 } )$ in $\sqrt { - g }$ give a contribution to the action $O ( h ^ { 3 } )$ ,and can be neglected.Performing straightforward algebra we then obtain, after some integration by parts,

$$
\begin{array} { l l } { { S _ { E } = - \displaystyle \frac { c ^ { 3 } } { 6 4 \pi G } \int d ^ { 4 } x } } & { { \left[ \partial _ { \mu } h _ { \alpha \beta } \partial ^ { \mu } h ^ { \alpha \beta } - \partial _ { \mu } h \partial ^ { \mu } h \right. } } \\ { { } } & { { } } \\ { { } } & { { \left. + 2 \partial _ { \mu } h ^ { \mu \nu } \partial _ { \nu } h - 2 \partial _ { \mu } h ^ { \mu \nu } \partial _ { \rho } h _ { \nu } ^ { \rho } \right] } } \end{array}
$$

and the corresponding Lagrangian density is (see Note 2)

$$
{ \mathcal { L } } = - { \frac { c ^ { 4 } } { 6 4 \pi G } } [ \partial _ { \mu } h _ { \alpha \beta } \partial ^ { \mu } h ^ { \alpha \beta } - \partial _ { \mu } h \partial ^ { \mu } h + ] 2 \partial _ { \mu } h ^ { \mu \nu } \partial _ { \nu } h - 2 \partial _ { \mu } h ^ { \mu \nu } \partial _ { \rho } h _ { \nu } ^ { \rho } ] .
$$

We can now compute $t ^ { \mu \nu }$ ,using eq. (2.29). We evaluate the result directly in the gauge

$$
\partial ^ { \mu } h _ { \mu \nu } = 0 , h _ { \nu } = 0 .
$$

Therefore,after computing the derivative $\delta { \mathcal L } / ( \partial _ { \mu } h _ { \alpha \beta } )$ in eq. (2.29),we impose the gauge condition (2.35).We observe that the second, third and fourth terms in brackets ineq. (2.33) are quadratic in quantitiesthat will be set to zero by the gauge fixing and,after taking the functional derivative, they give contributibns which are linear in h or in duhμv,and therefore vanish when we impose eq. (2.35). So the only non-vanishing contribution comes from the term $\partial _ { \mu } h _ { \alpha \beta } \partial ^ { \mu } h ^ { \alpha \beta }$ ,and we get

$$
\left. \frac { \partial \mathcal { L } } { \partial ( \partial _ { \mu } h _ { \alpha \beta } ) } \right| _ { \partial ^ { \mu } h _ { \mu \nu } = h = 0 } = - \frac { c ^ { 4 } } { 3 2 \pi G } \partial ^ { \mu } h ^ { \alpha \beta } .
$$

We next evaluate the term (L) in eq. (2.29), in our gauge. We recall that inside the average we are free to perform integration by parts (com-pare with Note 23 on page 35). Then, since in our gauge $h _ { \mu \nu }$ satisfies the equations of motion $\square h _ { \mu \nu } = 0$ ，even the term $\partial _ { \mu } h _ { \alpha \beta } \partial ^ { \mu } h ^ { \alpha \beta }$ gives zero because, after an integration by parts, it becomes $- h _ { \alpha \beta } \bigtriangledown h ^ { \alpha \beta }$ and vanishes upon use of the equations of motion, so $\langle \mathcal { L } \rangle = 0$

In conclusion,we obtain

$$
t ^ { \mu \nu } = \frac { c _ { \scriptscriptstyle 1 } ^ { 4 } } { 3 2 \pi G } \left. { \partial ^ { \mu } h ^ { \alpha \beta } \partial ^ { \nu } h _ { \alpha \beta } } \right. .
$$

As expected, the result agrees with eq. (1.133).

We can now come back to the problem of the localization of the energy of GWs. In the field-theoretical description, the issue is whether one of the many equivalent integrands, in the expression for $P ^ { 0 }$ can be promoted to a physical observable, thereby providing a definition of a local energy density. In electromagnetism there is a very natural candidate,the tensor Tμ of eq. (2.23)， which is conserved and gauge invariant,so it can be sensible to identify $( 1 / 2 ) ( \mathbf { E } ^ { 2 } + \mathbf { B } ^ { 2 } )$ with the local energy density of the electromagnetic field. No such answer is possible for the gravitational field. The quantity $\partial ^ { \mu } h ^ { \alpha \beta } \partial ^ { \nu } h _ { \alpha \beta }$ which appears inside the average in eq. (2.37) is not gauge-invariant. It is futile to search for another local expresson, whose integral gives the energy, but which is already gauge invariant before integration: the equivalence principle tells us that, at a given point, we can always find a locally inertial frame (see Section 1.3.2),such that at the point in question the gravitational field vanishes. Therefore any candidate expression for a local energy density can always be set to zero at a given point with a coordinate transformation, so it cannot be gauge invariant. This is an important difference between gravity and electromagnetism. In electromagnetism, at least if we consider a slowly varying electromagnetic field,it makes sense to assign to each point a local energy density $( 1 / 2 ) ( \mathbf { E } ^ { 2 } + \mathbf { B } ^ { 2 } )$

When we consider waves,however，concerning energy localization there is no real diffrence between gravity and electromagnetism. In both cases,all that can be really measured is the energy averaged over several wavelengths or periods. This can be understood even more easily at first by looking at the problem quantum-mechanically even if, as we will see below,the argument is really classical.

From the quantum point of view, a plane wave describes a collction of massless quanta (gravitons with helicity $h = \pm 2$ for gravitation, and photons with helicity $\pm 1$ in electrodynamics). Consider a collection of such free particles.To determine the energy of this system in a volume V we must know how many quanta of the field are within $V$ at a given time,and the energy of each. If we take a volume with sides smaller than the reduced wavelength $\dagger$ of a photon orof a graviton,in order to know whether a given photon (or graviton) is inside the box we must measure its position with an error $\Delta x < \dot { x }$ and then,by the uncertainty principle, we have $\Delta p > \hbar / \hbar$ ，which is larger than the momentum $p = \hbar / \chi$ of a quantum with reduced wavelength $\dagger$ .Thus,we have completely lost information about the momentum p of the particle,and therefore (given that we are considering free particles described by simple plane waves), we lost information about its energy $E _ { \mathrm { i } } = c | \mathbf { p } |$ ，which means that we cannot localize the energy density better than to a few wavelengths. Alternatively,we can localize the energy in space if we delocalize it in time,according to $\Delta E \Delta t { \gtrsim } h$ Clearly photons and gravitons do not show any differcnce in this respect.6 In fact，even if we phrased it in a quantum language, this argument is really classical,and follows from the fact that the position $\mathscr { X }$ of the peak of a classical wave-packet,and its typical wave-vector $k$ satisfy $\Delta x \Delta k \geqslant 1$ ,and in this form is simply a property of the Fourier transform.In quantum theory,one identifies the momentum $\mathbf { p }$ with $\hbar \mathbf { k }$ ,and $\Delta x \Delta k \geqslant 1$ becomes $\Delta x \Delta p \geqslant \hbar$

In conclusion the field-theoretical approach,based on Noether's theorem,gives us an unambiguous recipe for computing a spatial (or a temporal) average of the energy-momentum tensor of GWs. The fact that, for GWs,we cannot do better than this,i.e. that the energy of GWs camnot be localized in space (or in time) with a precision better than a few wavelengths (or a few periods) can be understood as a consequence f the equivalence principle,but it is in fact also a general property of any wave governed by a massless wave equation, which at the quantum level translates into a limitation required by the uncertainty principle.

# 2.1.3 The angular momentum of GWs

We next compute the angular momentum carried by GWs. Angular momentum is the conserved charge associated to invariance under spatial rotations. A symmetric tensor $h _ { \mu \nu }$ , from the point of view of spatial rotations, decomposes into $h _ { 0 0 }$ and the spatial trace $h _ { i } ^ { i }$ ，which are both scalars under rotation and therefore are spin-O fields, $h _ { 0 i }$ which is a spatial vector and therefore has spin 1,and a traceless symmetric tensor ,which is a spin-2 field and has five degrees of freedom. To describe the GW we go to the TT gauge, so we have $h _ { 0 \mu } = 0$ and we are left only ithe field $h _ { i j } ^ { \mathrm { T T } }$ which satisfies $( h ^ { \mathrm { T T } } ) _ { i } ^ { i } = 0$ and $\partial ^ { i } h _ { i j } ^ { \mathrm { T T } } = 0$ compare ith eq. (1.31). Observe that $h _ { i j } ^ { \mathrm { T T } }$ has only two degrees of freedom, orresponding to a massless particle with helicity $\pm 2$ .7 As before, the lst three terms in eq. (2.33) give a contribution to the Noether current hat vanishes when,after taking the functional derivatives,we impose he gauge fixing condition. Then， for the purpose of computing the Voether current in this gauge,we can use as Lagrangian the first term

6The fact that,as a quantum feld theory,general relativity is not renormalizable plays no role here.As long as we are at energies much smaller than the Planck mass,linearized theory can be promoted to a well defined effective quantum field theory,describing weakly interacting gravitons,as we discuss in more detail in Section 2.2.

7As we will recall in Section 2.2.2 and in Problem 2.1,the physical representation of the Poincaré group are of two types: massive representations,characterized by their spin $j$ and having $2 j + 1$ states,and massless representations,which have a quantum number $j$ but only two states,corresponding to helicities $h = \pm j$ We will use the name “spin- $j$ field”to denote generically a field that can describe either a massive particle with spin $j$ or a massless particle with helicities $h = \pm j$ (in which case,it will be subject to constraints that eliminate the extra states,see Section 2.2)．The name“spin- $j$ particle" will however be reserved to a massive particle with spin $j$ and therefore $2 j + 1$ degrees of freedom.A massless particle with quantum number $j$ will be referred toas $^ { \mathrm { a } } \mathrm { a }$ massless particles with helicity $\pm j ^ { \gamma }$

in eq. (2.33),and we can keep only the physical degrees of freedom $h _ { i j } ^ { \mathrm { T T } }$

$$
\mathcal { L } = - \frac { c ^ { 4 } } { 6 4 \pi G } \partial _ { \mu } h _ { i j } ^ { \mathrm { T T } } \partial ^ { \mu } h _ { i j } ^ { \mathrm { T T } } .
$$

A rotation of three-dimensional space is described by a $3 \times 3$ orthogonal matrix $\mathcal { R }$ ，which transforms the coordinates according to $x ^ { i }  \mathcal { R } ^ { i j } x ^ { j }$ (observe that, since our signature is $( - , + , + , + )$ ， we do not need to be careful about raising or lowering spatial indices). An infinitesimal rotation can be written as

$$
\mathcal { R } ^ { i j } = \delta ^ { i j } + \omega ^ { i j } ,
$$

and the condition that $\mathcal { R }$ is an orthogonal matrix gives $\omega ^ { i j } = - \omega ^ { j i }$ Therefore rotations can be parametrized by the three independent quantities $\omega ^ { 1 2 } , \omega ^ { 1 3 }$ and $\omega ^ { 2 3 }$ ，which play the role of the parameters $\epsilon ^ { a }$ in eqs.(2.2) and (2.3). So,for rotations eqs. (2.2) and (2.3) become

$$
\begin{array} { r c l } { { } } & { { } } & { { x ^ { i }  x ^ { i } + \displaystyle \sum _ { k < l } \omega ^ { k l } A _ { k l } ^ { i } ~ , } } \\ { { } } & { { } } & { { ~ h _ { i j } ^ { \mathrm { T T } }  h _ { i j } ^ { \mathrm { T T } } + \displaystyle \sum _ { k < l } \omega ^ { k l } F _ { i j , k l } ~ , } } \end{array}
$$

and the sum goes over the independent parameters $\boldsymbol { \omega } ^ { k l }$ with $k < l$ identifes the feld Observe that, in $F _ { i j , k l }$ $h _ { i j } ^ { \mathrm { T T } }$ andtreorepatholehatthndex ,the first pair of indices, $( i , j )$ , is the label that $i$ had in eq. (2.3),while the second pair $( k , l )$ plays the role of the index $a$ in eq. (2.3). In particular, $F _ { i j , k l }$ is symmetric with respect to the pair $( i , j )$ and can be taken to be antisymmetric with respect to the pair $( k , l )$ .

The total angular momentum carried by the GWs is then given by

$$
J ^ { i } = { \frac { 1 } { 2 } } \epsilon ^ { i j k } J _ { k l } .
$$

where $J _ { k l }$ is the conserved charge associated to rotations in the $( k , l )$ plane,

$$
J _ { k l } = { \frac { 1 } { c } } \int d ^ { 3 } x j _ { k l } ^ { 0 } ,
$$

(the factor $1 / c$ provides the correct dimensions) and Noether's theorem gives

$$
j _ { k l } ^ { 0 } = \frac { \partial \mathcal { L } } { \partial ( \partial _ { 0 } h _ { i j } ^ { \mathrm { T T } } ) } \left[ A _ { k l } ^ { \nu } \partial _ { \nu } h _ { i j } ^ { \mathrm { T T } } - F _ { i j , k l } \right] - A _ { k l } ^ { 0 } \mathcal { L } .
$$

To find the explicit form of $A _ { k l } ^ { \nu }$ and $F _ { i j , k l }$ we compare the generic formulas (2.40) and (2.41) with the actual transformation properties of $x ^ { i }$ and $h _ { i j } ^ { \mathrm { T T } }$ under infinitesimal rotations; $A _ { k l } ^ { i }$ is easily computedobserving that

$$
\begin{array} { r l } { { } } & { { \displaystyle x ^ { i } \to \mathcal { R } ^ { i j } x ^ { j } = x ^ { i } + \omega ^ { i j } x ^ { j } } } \\ { { } } & { { = x ^ { i } + \displaystyle \sum _ { k \ < l } \omega ^ { k l } ( \delta ^ { i k } x ^ { l } - \delta ^ { i l } x ^ { k } ) , } } \end{array}
$$

so,comparing with eq. (2.40),

$$
A _ { k l } ^ { i } = \delta ^ { i k } x ^ { l } - \delta ^ { i l } x ^ { k } .
$$

$A _ { k l } ^ { 0 }$ $A _ { k l } ^ { 0 } = 0$

The quantity $F _ { i j , k l }$ is determinedbythe propertiesof $h _ { i j } ^ { \mathrm { T T } }$ under rotations. Since $h _ { i j } ^ { \mathrm { T T } }$ is aspatial tensor,it transforms as

$$
\begin{array} { r l } & { h _ { i j } ^ { \mathrm { T T } } \to R _ { i } ^ { \textit { k } } R _ { j } ^ { \textit { l } } h _ { k l } ^ { \mathrm { T T } } } \\ & { \quad \quad = h _ { i j } ^ { \mathrm { T T } } + { \omega _ { j } } ^ { \textit { l } } h _ { i l } ^ { \mathrm { T T } } + { \omega _ { i } } ^ { \textit { k } } h _ { k j } ^ { \mathrm { T T } } } \\ & { \quad \quad = h _ { i j } ^ { \mathrm { T T } } + \displaystyle \sum _ { k < l } { \omega ^ { k l } \big ( \delta _ { i k } h _ { j l } ^ { \mathrm { T T } } - \delta _ { i l } h _ { j k } ^ { \mathrm { T T } } + \delta _ { j k } h _ { i l } ^ { \mathrm { T T } } - \delta _ { j l } h _ { i k } ^ { \mathrm { T T } } \big ) } . } \end{array}
$$

Comparing eqs. (2.41) and (2.47), we see that

$$
\begin{array} { r } { F _ { i j , k l } = \delta _ { i k } h _ { j l } ^ { \mathrm { T T } } - \delta _ { i l } h _ { j k } ^ { \mathrm { T T } } + \delta _ { j k } h _ { i l } ^ { \mathrm { T T } } - \delta _ { j l } h _ { i k } ^ { \mathrm { T T } } . } \end{array}
$$

We can now plug these results into eq. (2.44). We also observe that

$$
\begin{array} { r l r } {  { \frac { \partial \mathcal { L } } { \partial ( \partial _ { 0 } h _ { i j } ^ { \mathrm { T T } } ) } = - \frac { c ^ { 4 } } { 3 2 \pi G } \partial ^ { 0 } h _ { i j } ^ { \mathrm { T T } } } } \\ & { } & { = + \frac { c ^ { 3 } } { 3 2 \pi G } \dot { h } _ { i j } ^ { \mathrm { T T } } , } \end{array}
$$

and (renaming the indices $( i , j ) \to ( a , b )$ we get

$$
j _ { k l } ^ { 0 } = \frac { c ^ { 3 } } { 3 2 \pi G } \left[ - \dot { h } _ { a b } ^ { \mathrm { T T } } ( x ^ { k } \partial ^ { l } - x ^ { l } \partial ^ { k } ) h _ { a b } ^ { \mathrm { T T } } + 2 \dot { h } _ { a b } ^ { \mathrm { T T } } ( \delta _ { b l } h _ { a k } ^ { \mathrm { T T } } + \delta _ { a l } h _ { b k } ^ { \mathrm { T T } } ) \right] .
$$

From eqs. (2.43),(2.44) and (2.42),the total angular momentum of the GW is therefore

$$
J ^ { i } = \frac { c ^ { 2 } } { 3 2 \pi G } \int d ^ { 3 } x \left[ - \epsilon ^ { i k l } \dot { h } _ { a b } ^ { \mathrm { T T } } x ^ { k } \partial ^ { l } h _ { a b } ^ { \mathrm { T T } } + 2 \epsilon ^ { i k l } h _ { a k } ^ { \mathrm { T T } } \dot { h } _ { a l } ^ { \mathrm { T T } } \right] .
$$

Io understand the physical meaning of the two terms in bracket, it is Iseful to recall the analogous results for spin-O and spin-1 fields. For a real scalar field,applying Noether's theorem,one finds that the angular momentum carried by a field confguration $\phi$ is

$$
J ^ { i } = - \epsilon ^ { i k l } \int d ^ { 3 } x ( \partial _ { \boldsymbol { \phi } } \phi ) x ^ { k } \partial ^ { l } \phi .
$$

We see that this has the same structure a\$ the first term in eq. (2.51) (afer rescaling $h _ { a b } ^ { \mathrm { T T } }$ by a factor $( 3 2 \pi G / c ^ { 3 } ) ^ { 1 / 2 }$ as we willsee inSectin 2.2 tis recaingivesto $h _ { a b } ^ { \mathrm { T T } }$ thestadardedheicao The physical meaning of this term can be understood observing that, fr a real feld $\phi$ satisfying the massless Klein-Gordon equation $\boldsymbol { \Sigma } \boldsymbol { \phi } = 0$ ，

$^ 8 \mathrm { F o r }$ explicitprofs，see Maggiore (2005)，Section 3.3.1 for spin-0 fields, and Section 4.3.1 for the electromagnetic field． Pay attention to the fact that this reference uses the opposite metric signature (following the most common convention used in field the ory，while here we are following the most common convention used in general relativity),and units $\hbar = c = 1$

one can define the scalar product between two field configurations $\phi$ and $\phi ^ { \prime }$ ：

$$
\langle \phi | \phi ^ { \prime } \rangle = { \frac { i } { 2 } } \int d ^ { 3 } x \ \phi \stackrel {  } { \partial _ { 0 } } \phi ^ { \prime } ,
$$

where, on any two functions $f$ and $g$ we define $\partial _ { \mu }$ by $f \stackrel {  } { \partial _ { \mu } } g \equiv f \partial _ { \mu } g -$ $( \partial _ { \mu } f ) g$ Since $\phi$ and $\phi ^ { \prime }$ are functions of $t$ and $\mathbf { x }$ and in eq. (2.53) we integrate over $d ^ { 3 } x$ ，the result is a priori still a function of time. However, this scalar product is actually time-independent,if $\phi _ { 1 } , \phi _ { 2 }$ are solutions of the Klein-Gordon equation. It is then not so surprising that the conserved charges of the scalar field theory can be expressed as expectation values of suitable operators,with respect to this scalar product.

Consider in particular $\hat { L } ^ { i } \ne - i \epsilon ^ { i k l } x ^ { k } \partial ^ { l }$ ， which is the orbital angular momentum operator (in units of $\hbar$ ).The expectation value of this operator,with respect to the scalar product (2.53), is

$$
\begin{array} { l } { { \displaystyle \langle \phi | \hat { L } ^ { i } | \phi \rangle = \frac { i } { 2 } \int d ^ { 3 } x \left[ \phi \hat { L } ^ { i } \partial _ { 0 } \phi - ( \partial _ { 0 } \phi ) \hat { L } ^ { i } \phi \right] } } \\ { { \displaystyle ~ = \frac { 1 } { 2 } \epsilon ^ { i k l } \int d ^ { 3 } x ~ \big [ \phi x ^ { k } \partial ^ { l } \partial _ { 0 } \phi - ( \partial _ { 0 } \phi ) x ^ { k } \partial ^ { l } \phi \big ] } } \\ { { \displaystyle ~ = - \epsilon ^ { i k l } \int d ^ { 3 } x ( \partial _ { 0 } \phi ) x ^ { k } \partial ^ { l } \phi , } } \end{array}
$$

where,going from the second to the third line, we integrated by parts $\partial ^ { l }$ in the first term. Comparing with eq. (2.52) we see that the total angular momentum carried by|a scalar field configuration $\phi$ is equal to the expectation value of the orbital angular momentum operator ${ \hat { L } } ^ { i }$ with respect to this scalar product,

$$
J ^ { i } = \langle \phi | \hat { L } ^ { i } | \phi \rangle .
$$

Observe also that, for a scalar feld,there is no additional contribution, and the total angular momentum is given by the expectation value of the orbital angular momentum| operator.

Consider now the spin-1 case. If one computes, using Noether's theorem,the angular momentum carried by the electromagnetic field in the radiation gauge,where the electromagnetic field is transverse, $\partial _ { i } A ^ { i } = 0$ ， and satisfies $\boxed { \ l } A ^ { i } = 0$ ,one finds

$$
J ^ { i } = \int d ^ { 3 } x \left[ - \epsilon ^ { i k l } ( \partial _ { 0 } A _ { j } ) x ^ { k } \partial ^ { l } A _ { j } + \epsilon ^ { i k l } A _ { k } \partial _ { 0 } A _ { l } \right] .
$$

Again, since the equation of motion is $\square A _ { i } = 0$ , we can define a scalar product

$$
\langle A | A ^ { \prime } \rangle = \frac { i } { 2 } \int d ^ { 3 } x \ A _ { i } \ \stackrel {  } { \partial _ { 0 } } \ A _ { i } ^ { \prime } ,
$$

which is conserved on the solutions of the equation of motion. Then. we see that the first term in eq. (2.56) is again the expectation value of $\hat { L } ^ { i } = - i \epsilon ^ { i k l } x ^ { k } \partial ^ { l }$ with respect to this scalar product, so it is the contribution from the orbital angular momentum. In the derivation based on the Noether theorem,this term is determined by the transformation of the coordinates $x ^ { i }$ under spatial rotations,(i.e.it comes from the term proportional to $A _ { a . } ^ { \nu }$ in eq. (2.7)),so it is clear that it has the same structure for all fields,independently of their spin. The second term instead depends on the specific properties of the field under spatial rotations (i.e. it comes from the term proportional to $F _ { i , a }$ in eq.(2.7)) and therefore it is the spin part. Defining

$$
S ^ { i } = \epsilon ^ { i k l } \int d ^ { 3 } x A _ { k } \partial _ { 0 } A _ { l } ,
$$

the explicit computation9 shows that,in second quantization,the circular polarizations states of the photons are eigenvectors of the helicity operator S·p (where $\hat { \bf p }$ is the unit vector in the direction of propagation), with eigenvalues $\pm 1$ ,as required for a massless particle described by a vector field.

We can now understand the meaning of the two terms in eq. (2.51). Since hTT satisfies $\bigtriangledown h _ { a b } ^ { \mathrm { T T } } = 0$ ,the conserved scalar product is defined as in the Klein--Gordon or in the electromagnetic case,

$$
\langle h | h ^ { \prime } \rangle = { \frac { i } { 2 } } \int d ^ { 3 } x \ h _ { \alpha b } ^ { \mathrm { T T } } \ \stackrel {  } { \partial _ { 0 } } \ h _ { \ a b } ^ { \prime \mathrm { T T } } .
$$

Ater rescaing $h _ { a b } ^ { \mathrm { T T } }  ( 3 2 \pi G / c ^ { 3 } ) ^ { 1 / 2 } h _ { a b } ^ { \mathrm { T T } }$ (wich,as we will se i sec tion 2.2.2, is the rescaling needed to give to $h _ { \mu \nu }$ the canonical normalization to the kinetic term in the action) the first term in eq.(2.51) is he expectation value of the orbital angular momentum operator with respect to this scalar product,while the term 2eiklhTThTT is the spin contribution.The factor of 2 in this term correctly reproduces the fact that the gravitational field has spin two,and therefore gravitons are eigenvectors of the helicity with eigenvalues $\pm 2$

In the previous section we learned that the Noether currents cannot be localized better than a few wavelengths,so the physical density of angular momentum, $j ^ { i } / c$ ,is the integrahd of eq. (2.51),averaged over a few wavelengths,

9Ssee Maggiore (2005)，pages 98-99.

$$
\frac { 1 } { c } j ^ { i } = \frac { c ^ { 2 } } { 3 2 \pi G }  - \epsilon ^ { i k l } \dot { h } _ { a b } ^ { \mathrm { T T } } x ^ { k } \partial ^ { l } h _ { a b } ^ { \mathrm { T T } }  + 2 \epsilon ^ { i k l } \dot { h } _ { a l } ^ { \mathrm { T T } } h _ { a k } ^ { \mathrm { T T } }  .
$$

Consider now a GW propagating outward from a source. At time $t$ we consider a portion of the wave front,at radial distance $r$ from the source,and covering a solid angle $d \Omega$ .At time $t + d t$ this portion of the wave front has swept the volume $d ^ { 3 } x = \rvert \boldsymbol { r } ^ { 2 } d \boldsymbol { r } d \Omega = \boldsymbol { r } ^ { 2 } ( c d t ) \boldsymbol { \bar { d } } \Omega$ Since the angular momentum per unit volume is $( j ^ { i } / c )$ ,the angular momentum carried away by the GW is $d J ^ { i } = r ^ { 2 } ( c d t ) d \Omega \left( j ^ { i } / c \right)$ . Therefore the rate of angular momentum emission due to GWs is

<table><tr><td>d.Ji c3 r2d2-chT dt 32πG</td><td>+2chTTTT hak</td></tr><tr><td></td><td></td></tr></table>