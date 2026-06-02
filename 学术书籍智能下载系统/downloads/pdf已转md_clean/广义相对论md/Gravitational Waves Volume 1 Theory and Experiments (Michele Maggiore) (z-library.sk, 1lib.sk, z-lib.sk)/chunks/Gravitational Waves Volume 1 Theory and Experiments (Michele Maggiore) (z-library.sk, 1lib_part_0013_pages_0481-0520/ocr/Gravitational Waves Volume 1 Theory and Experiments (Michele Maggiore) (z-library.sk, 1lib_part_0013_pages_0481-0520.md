# 8.4.2Spheres as multi-mode detectors

One of the most interesting features of a spherical resonant mass is that it is a multi-mode detector.A resonant cylinder is a single-mode detector because,at each resonant frequency $\omega _ { n }$ ,there is only one longitudinal mode.The output of a resonant cylinder is therefore a single quantity the component of $h _ { i j }$ along the bar axis,say $h _ { x x }$ .This is related to the components $h _ { + }$ and $h _ { \times }$ of the GWand to the direction of arrival of the wave by $h _ { x x } = h _ { + } F _ { + } ( \theta , \phi ) + h _ { \times } F _ { \times } ( \theta , \phi )$ ，where $F _ { + , \times } ( \theta , \phi )$ are the pattern functions of the bar.From this single output we cannot disentangle the information on the GW amplitude from that on the source direction The same signal could be induced by a GW with a smaller amplitude but well oriented with respect to the bar,i.e.impinging transversally on it,or bya GW arriving from a less optimal direction，but with a higher amplitude.Even less can be said as to how this energy is shared between the two polarizations.

Therefore,if we detect a sighal in a single cylindrical bar,in the ab sence of an optical counterpait the best one can do is to guess that the wave came from a more-or-less optimal direction and to guess that $h _ { + } \sim h _ { \times }$ ，and under these assumptions one can estimate the energy flux carried by the wave.Almost nothing can be said about the source location,except that it cannot be too close to the bar's blind direc tion,which is its longitudinal axis.As we will see in later chapters,the situation is similar for a single interferometer,and to improve it substan tially,with bars or interferometers,it is necessary to detect the signa simultaneously in different detectors.

A sphere is completely different from this point of view.At each resonance frequency $\omega _ { n }$ ，corresponding to an $l = 2$ spheroidal mode,it has five degenerate modes coupled to the GWs,and therefore a sphere has five independent outputs.As we have seen in eq. (8.26O),each ol the five modes $\xi _ { n m }$ (with $n$ given and $m = - 2 , \ldots , 2$ ）isdriven only by the spherical component $\tilde { h } _ { m } ( \omega _ { n } )$ of the GW which has the same value of $m$ ．Therefore,monitoring the five $\xi _ { n m }$ we obtain the five quantities $\tilde { h } _ { m } ( \omega _ { n } )$ and,using eq. (8.257)，we can reconstruct the full matrix $\tilde { h } _ { i j }$ at the resonance frequency or,more precisely,in a bandwidth centered around $\omega _ { n }$

The full matrix $\tilde { h } _ { i j }$ contains all the information on the arrival direction and on the amplitude of the two polarizations.In particular,if the excitation of the detector is really due toa GW,rather than to noise it must be possible to rotate the axes of our reference frame so that the new $z$ axis coincides with the propagation direction of the wave. In other words,once we measure the quantities $h _ { m }$ and we construct $h _ { i j }$ as in eq.(8.257),it must exist a rotation $\mathcal { R }$ such that

$$
\mathcal { R } _ { i k } \mathcal { R } _ { j l } h _ { k l } = \left( \begin{array} { c c c } { h _ { + } } & { h _ { \times } } & { 0 } \\ { h _ { \times } } & { - h _ { + } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) _ { i j } .
$$

Then the propagation direction $\hat { \bf n }$ of the GW is obtained applying this rotation to the original $z$ axis,i.e. $n _ { i } = \mathcal R _ { i j } \hat { z } _ { j } = \mathcal R _ { i 3 }$ .Given the original matrix $h _ { i j }$ ,the determination of the incoming direction (in the absence ofnoise) is thereforea straightforward algebraic problem,whose solution is

$$
\begin{array} { c } { \tan \varphi \equiv n _ { y } / n _ { x } = \displaystyle \frac { h _ { 2 2 } h _ { 1 3 } - h _ { 1 2 } h _ { 2 3 } } { h _ { 1 2 } h _ { 1 3 } - h _ { 1 1 } h _ { 2 3 } } \ : , } \\ { \tan \theta \equiv \displaystyle \frac { ( n _ { x } ^ { 2 } + n _ { y } ^ { 2 } ) ^ { 1 / 2 } } { n _ { z } } = \displaystyle \frac { h _ { 1 3 } } { h _ { 1 2 } \cos \varphi - h _ { 1 1 } \sin \varphi } \ : . } \\ { . . . } \end{array}
$$

We have therefore reconstructed the arrival direction,up to a sign ambiguity:we cannot distinguish a wave coming from the direction $\hat { \bf n }$ from a wave coming from $- \hat { \mathbf { n } }$ since if $( \theta , \varphi )$ Satisfy eqs.(8.264) and (8.265) then also $( \pi - \theta , \pi + \varphi )$ satisfy it. (This ambiguity could be fixed measuring tle time delay between two detectors.）We have therefore determined the arrival direction and we can now read the two separate amplitudes $h _ { + }$ and $h _ { \times }$ from eq. (8.263).40

At this stage we have used five qutputs to determine four quantities: the two amplitudes $h _ { + } , h _ { \times }$ (orequivalently,the amplitude $h =$ $( h _ { + } ^ { 2 } + h _ { \times } ^ { 2 } ) ^ { 1 / 2 }$ and the polarization angle $\Psi$ defined by $h = h _ { + } \cos 2 \Psi +$ $h _ { \times } \sin 2 \Psi )$ ,and the two angles $\theta , \phi$ that give the unit vector $\hat { \bf n }$ We still have one unused information. This is a veto that distinguishes GWs from spurious events due to noise. In| fact, given five arbitrary numbers $h _ { m }$ ,the matrix $\textstyle \sum _ { m } h _ { m } y _ { i j } ^ { m }$ is by definition traceless and symmetric,because the $y _ { i j } ^ { m }$ are traceless and symmetric,but this just means that, with an appropriate rotation, we can| bring it to the form

40Of course,once we find arotation that brings $h _ { i j }$ to the form (8.263),any further rotation around the new $z$ axis still leaves $h _ { i j }$ in this form． This further rotation just amounts to a redefinition of the axes with respect to which the two polarizations are defined,and mixes $h _ { + }$ and $h _ { \times }$ as in eq. (2.194).In particular,it can be chosen so that $h _ { \times }$ is set to zero and $h _ { i j }$ becomes diagonal, $h _ { i j } = \mathrm { d i a g } \left( h _ { + } , - h _ { + } , 0 \right)$

$$
\left( \begin{array} { c c c } { { a } } & { { d } } & { { 0 } } \\ { { d } } & { { b } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { c } } \end{array} \right) _ { i j } ,
$$

with $a + b + c = 0$ . That is, we can choose two Euler angles associated to arotation to set to zero the (1,3) and (2,3) elements of the matrix (and of course at this point we can also set $d \neq 0$ with a rotation around the new zaxis).The fact that,after performing such a rotation,we automatically find $c = 0$ and therefore $a = - b$ is instead a specific property of GWs, due to their transverse nature. In conclusion,the five quadrupolar modes of the sphere allow us to determine the source direction $\hat { \bf n }$ (up to a sign ambiguity $\hat { \mathbf { n } }  - \hat { \mathbf { n } }$ ),the two separate amplitudes $h _ { + }$ and $h _ { \times }$ ，and to have a veto that discriminates GWs from noise.

Other vetoes emerge naturally in |a resonant sphere. For instance, from Tables 8.1 and 8.2 we see that the toroidal mode with $l = 2 , n = 1$ is quite close,in frequency, to the spheroidal mode with $l = 2 , n = 1$ Since the former is not coupled to GWs while the latter is the main mode that is monitored for GW detection,an excitation of the latter when the former is not excited would give further confidence on the GW origin of the signal.41

We have seen above that,in the ideal case in which the signal is given uniquely by the GWs,and the noise is negligible,a sphere is able to locate exactly the direction of the source,contrary to a single bar or

4l Toroidal modes have no radial displacement,so to detect them we need transducers coupled to the transverse oscillations of the surface.

a single interferometer that,even in the ideal noiseless limit,have a angular resolution of order $4 \pi$ Of course,in a real situation noise is present,and the angular resolution of the sphere depends on the signal to-noise ratio.We denote by $| \theta _ { 0 }$ and $\phi _ { 0 }$ the actual angles which give the direction of propagation of the wave and by $\theta _ { c }$ and $\phi _ { c }$ the angles computed from the five outputs of a noisy resonant sphere.We introduce the notation $\Delta \theta = \theta _ { c } - \theta _ { 0 }$ and $\Delta \phi = \phi _ { c } - \phi _ { 0 }$ . A useful indicator of the angular resolution is

![](images/bf88045b1f3dc213751ae12f7690e8d9f1e820a900910a054b9d8746e367605d.jpg)  
Fig.8.20 The MiniGRAIL resonant sphere.A few resonant transducers are also visible.

![](images/8f050365a252f1404b3b2326cc5a3d9fb478c29bdd7ccc4e0984b04ea10d7892.jpg)  
Fig.8.21 The strain sensitivity of MiniGRAIL (as of Jan 2005） compared to the prediction of a simplified two-mode model, cooling the detector to a temperature $T = 5 ~ \mathrm { { K } }$ The lowest curve is the sensitivity expected cooling at $T = 8 0 ~ \mathrm { { m K } }$ The final goal is to reach $T = 2 0 ~ \mathrm { { m K } }$

$$
\Delta \Omega \equiv \pi \left[ ( \Delta \theta ) ^ { 2 } + \sin ^ { 2 } \theta _ { 0 } ( \Delta \phi ) ^ { 2 } \right] ,
$$

which is the area of a circle or the unit sphere,centered on the actual source location,and with radius $\delta \hat { \mathbf n } = \hat { \mathbf n } _ { c } - \hat { \mathbf n } _ { 0 }$ ,where $\hat { \bf n } _ { 0 }$ is the unit vectol of the actual propagation direction of the GW and $\hat { \mathbf { n } } _ { c }$ is the direction computed from the noisy outputs. Then it can be shown (Zhou and Michelson 1995,Stevenson 1997) that,if we denote by SNR the signal to-noise ratio in energy,in the limit of large SNR the angular resolution is given by

$$
( { \Delta \theta } ) ^ { 2 } = \sin ^ { 2 } \theta _ { 0 } ( { \Delta \phi } ) ^ { 2 } = \frac { 1 } { \mathrm { S N R } } ,
$$

and therefore

$$
\Delta \Omega = \frac { 2 \pi } { \mathrm { S N R } } .
$$

A spherical resonant mass detector,MiniGRAIL,has been developed at Leiden University,in the Netherlands,and is in its commissioning phase.It is a sphere of $6 8 ~ \mathrm { c m }$ of diameter and a mass $M \simeq 1 . 3$ ton shown in Fig.8.20．At $4 \mathrm { ~ K ~ }$ its spheroidal quadrupolar modes are at $f \simeq 2 9 8 0 ~ \mathrm { H z }$ .The material is an alloy $\mathrm { C u A l 6 \% }$ ，chosen because of its high quality factor $Q \sim 1 0 ^ { 7 }$ atlow $T$ ),high sound velocity $( v _ { s } \simeq 4 1 0 0$ $\mathrm { m } / \mathrm { s } )$ and a sufficient thermal cqnductivity,which already allowed to .col it below $1 0 0 \mathrm { m K }$ .The ultimate goal is to operate it at a thermodynamical temperature $T \simeq 2 0 ~ \mathrm { m K }$ .The|expected bandwidth should be of order $2 3 0 ~ \mathrm { H z }$ ，and possibly higher.|The quadrupole modes are monitored using various transducers, coupled to double-stage SQUID amplifiers. The optimal choice is to have six transducers in the so-called TIGA configuration,see the Further Reading section. The target is to reach a temperature $T = 2 0 ~ \mathrm { { m K } }$ ,and a strain sensitivity $S _ { h } ^ { 1 / 2 }$ of order $1 0 ^ { - 2 2 }$ - $1 0 ^ { - 2 3 } \mathrm { { H z ^ { - 1 / 2 } } }$ The present sensitivity is shown in Fig.8.21.

Since its size is relatively small, MiniGRAIL explores high frequencies. in the $3 \ \mathrm { k H z }$ region. As we will discuss in Vol. 2,this could still be an interesting region for astrophysical signals from compact objects.

# Further reading

·Ahistorical account of GW research can be found in Thorne (1987).For overviews of resonant bars see e.g.Thorne (1987)，Coccia (1997)，Ju，Blair and Zhao (200O) and Bassan (2002).

·Computations of the sensitivity of resonant bars can be found in Pallottino and Plzzella (198l,1984, 1991),Michelson and Taber (1981,1984),and Price (1987).It is interesting to observe that the role of the amplifier noise was first pointed out by two distinguished theorists,Gibbons and Hawking (1971).

·Resonant transducers have beer proposed by Paik (1976).For detailed reviews on passive transducers see Richard and Folkner (1991).Parametric transducer are discussed in Veitch (1991) and in Ju,Blair and Zhao (200o).The dual scheme is proposed in Cerdonio et al. (2001)and Brfant et al. (2003). See also the review Cerdonio (2003).

·For back-action and the quaritum limit in resonant bars see Giffard (1976).Quantum nondemolition measurements are discussed in detail in Caves,Thorne,Drever,Sandberg and Zimmermann (1980)and in Braginsky and Kalili (1992).

·Analysis of the coincidences between the five resonant bars ALLEGRO，AURIGA，EXPLORER, NAUTILUS and NIOBE,andthe relative upper limit on GW bursts,can be found in Allen et al. [IGEC] (2000) and Astone et dl. [IGEC] (2003a). Searches for periodic GWs are reported in Astone et al. [ROG] (2002).

·Descriptions of the detectors can be found in Astone et al.(1997b) for NAUTILUS,Astone et al.(2003b)for EXPLORER,Blair et al.(1995) for NIOBE,Mauceli et al.(1996) for ALLEGRO, M.Cerdonio et al. (1997) and J.-P. Zendri et al. (2002) for AURIGA.

Forinformation on the resonaht bar experiments see the links:

http://sam.phys.lsu.edu   
http://www.auriga.lnl.infn.it   
http://www.romal.infn.it/rog/explorer   
http://www.lnf.infn.it/esperimenti/rog/nautilus

Coordination among the various GW experiments (both resonant masses and interferometers)is provided by the Gravitational Wave International Committee (GWIC)，see the link http://gwic.gravity.psu.edu

·The advantages of a resonant sphere in terms of cross-section and its multi-mode capability were already realized in the 197Os,see Forward (1971), Ashby and Dreitlein (1975) and Wagoner and Paik (1977).Detailed discussion of spherical detectors can be found in Zhou and Michelson (1995),Lobo (1995)and Coccia,Lobo and Ortega (1995).Hollow spheres are studied in Coccia,Fafone,Frossati, Lobo，and Ortega (1998)and Lobo (2002)．The multi-frequency capability of the sphere and the possibility of reconstruction of the chirp mass and orbital parameters of a coalescing binary with a single sphere is discussed in Coccia and Fafone (1996) and Spallicci,Frossati and Krolak (1997).The response of a resonant sphere to GWs in extensions of general relativity is discussed in Bianchi,Coccia,Colacino,Fafone and Fucito (1996） and,for scalar felds,in Bianchi,Brunetti, Coccia,Fucitc and Lobo (1998)and Maggiore and Nicolis (2000).

·A particularly useful configuration of transducers fora spherical detector,the TIGA configuration, was proposed and investigated experimentally in Johnson and Merkowitz (1993) and Merkowitz and Johnson (1995,1997).See also the PhD thesis of Merkowitz (1995).Another configuration requiring only five transducers,but with four of them sensitive to transverse displacements,is proposed in Zhou and Michelson (1995).Detailed discussion of sensitivity and optimal filtering in the presence of multiple transducers is given in Stevenson (1997).

·For MiniGRAIL，see de Waard，Gottardi，van Houwelingen，Schumack，and Frossati (20o3),and the PhD theses of de Waard (2003) and of Gottardi (20o4)．Updated information can be found at http://www.minigrail.nl.Another spherical resonant-mass under development is the “Mario Schenberg”detector of the Brazilian GRAVITON project,see Aguiar (2004).

![](images/144bd2645c6814ecfb9c192faa587ca37a718f22cbb6b39f2e4f38a58b9b6512.jpg)

![](images/c3f08cb92780be4653862259e44c67e3cc78eb38ad1d74442bd4d9e9c781487d.jpg)

9.1 A simple Michelson interferometer   
9.2 Interferometers with Fabry-Perot cavities   
9.3 Toward a real GW interferometer   
9.4 Noise sources   
9.5 Existing and planned detectors

# Interferometers

The idea of interferometric detection of GWs is in principle simple and elegant，and goes back to 1962，when it was first considered by twe Russian theorists,M.Gertsenshtein and V.I. Pustovoit.Weber alsd considered it,and it was then pushed in the late 196Os by R. Forward R.Weiss,R. Drever，and others.In practice,however,a large Gw interferometer is an extremely complex instrument， with many degree of freedom that must be kept under control with extraordinary accuracy Thus,their development up td the present scale has required the build ing up of large collaborations,comparable in size to modern particle physics experiments,as well as more than 30 years of preparation. Fol lowing the general approach of this book,as outlined in the Preface, w will not discuss the interesting history of the development of this idea referring the reader to the Further Reading section for reviews,and we will rather focus on the present understanding of these detectors. W will begin in Section 9.1 with the most naive setting,a simple Michelsor interferometer,and we will then add up successive layers of complex ity in Sections 9.2 and 9.3. Having defined the experimental set-up, we will be able to discuss the principal noise sources in Section 9.4.The existing detectors (LIGO,VIRGO,GEO600 and TAMA) are discussed in Section 9.5.1 while advanced ground-based detectors, as well as the space-borne alternative,are discussed in Section 9.5.2.

![](images/b79ef9a69286c5d4d40595ef9cb5873ef3418074a938c8342d3bb551fff6e0d9.jpg)  
Fig.9.1 The layout of a simple Michelson-type interferometer.

# 9.1A simple Michelson interferometer

A Michelson interferometer,of the type used in the classical Michelson-Morley experiment in 1887 to show the non-existence of the ether, is an extraordinarily accurate instrument for measuring changes in the travel time of light in its arms.The simplest conceptual scheme (which is not exactly the one used historically by Michelson and Morley) is shown in Fig.9.1. It consists of a monochromatic light source,which today is of course a laser,whose light is sent on a beam-splitter which separates the light,with equal probability amplitudes,into a beam traveling in one arms and a beam traveling in a second,orthogonal,arm. At the end of each arm we put totally reflecting mirrors. After traveling once back and forth,the two beams recqmbine at the beam-splitter,and part of the resulting beam goes to a photodetector, that measures its intensity (while a part goes back toward the laser). We denote by $\omega _ { \mathrm { { L } } }$ the frequency of the laser (the subscript L distinguishes it from the frequency $\omega _ { _ \mathrm { g w } }$ of the GWs that we want to detect)，so $k _ { \mathrm { L } } = \omega _ { \mathrm { L } } / c$ and $\lambda _ { \mathrm { L } } = 2 \pi / k _ { \mathrm { L } }$ are the wavenumber and the wavelength of the laser light.It is convenient to use a complex notation for the electromagnetic field.Thus,a given spatial component of the electric field of the input laser light is written as

$$
E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t + i \mathbf { k } _ { \mathrm { L } } \cdot \mathbf { x } } .
$$

We denote by $L _ { x }$ and $L _ { y }$ the length of the two arms,where we have oriented the $\boldsymbol { x }$ and $y$ axis as shown in Fig.9.1. Consider a photon that arrives at the beam-splitter,coming from the laser,at some initial time $t _ { 0 }$ , The part of the electric field that goes into the $x$ arm bounces on the mirror at a distance $L _ { x }$ and arrives back at the beam-splitter at a time $t = t _ { 0 } + 2 L _ { x } / c$ ，while the part that went through the $y$ arm comes back at the beam-splitter at $\dot { t ^ { \prime } } = t _ { \emptyset } + 2 L _ { y } / c$ .Thus,the beam that finally recombines at the beam-splitter at a given observation time $t$ is the superposition of a beam that entered the beam-splitter at a time $t _ { 0 } ^ { ( x ) } = \dot { t } - 2 L _ { x } / c$ and then wenthrough the $\mathscr { X }$ arm,and a beam that enteredteeamsittdftti $t _ { 0 } ^ { ( y ) } = t - 2 L _ { y } / c$ and then went through the $y$ arm.Setting the beam-splitter at ${ \bf x } = 0$ ,the former beam has an initial phase $\mathrm { e x p } \big \{ - i \omega _ { \mathrm { L } } t _ { 0 } ^ { ( x ) } \big \} = \mathrm { \hat { e } x p } \big \{ - i \omega _ { \mathrm { L } } t + 2 i k _ { \mathrm { L } } L _ { x } \big \}$ ，and thelIater $\exp \{ - i \omega _ { \mathrm { L } } t _ { 0 } ^ { ( y ) } \} = \exp \{ - i \omega _ { \mathrm { L } } \bar { t } + 2 i k _ { \mathrm { L } } L _ { y } \}$ .The phase of the fied is conserved during the free propagatlon,while the fields acquire overall factors from reflections and transmission at the mirrors.² So,the two electric fields that recombine at time $\nmid$ at the beam-splitter are given by

$$
E _ { 1 } = - \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t + 2 i k _ { \mathrm { L } } L _ { x } } .
$$

and

$$
E _ { 2 } = + \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t + 2 i k _ { \mathrm { L } } L _ { y } } .
$$

The total electric field is $E _ { \mathrm { o u t } } = E _ { 1 } + E _ { 2 }$ .Writing $2 L _ { x } = \left( L _ { x } + L _ { y } \right) +$ $\left( { { L } _ { x } } - { { L } _ { y } } \right)$ and $2 L _ { x } = \left( L _ { x } + L _ { y } \right) - \left( L _ { x } - L _ { y } \right)$ , we see that

$$
E _ { \mathrm { o u t } } = - i E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t + i k _ { \mathrm { L } } \left( L _ { x } + L _ { y } \right) } \sin [ k _ { \mathrm { L } } ( L _ { y } - L _ { x } ) ] \ ,
$$

and the power measured by the photodetector is proportional to

$$
| E _ { \mathrm { o u t } } | ^ { 2 } = E _ { 0 } ^ { 2 } \sin ^ { 2 } [ k _ { \mathrm { L } } ( L _ { y } - L _ { x } ) ] .
$$

Therefore any variation in the length of a arm results in a corresponding variation of the power at the photodetector. We now discuss how to apply this general idea to GW detection. We saw in Section 1.3.3 thatthe interaction of a GW with adetector can be described in two different languages,i.e.either using the TT frame,or using the proper detector frame.It is quite instructive to understand the functioning of an interferometer in both ways,as we do in the next two subsections.

# 9.1.1 The interaction with GWs in the TT gauge

Recall from Section 1.3.3 that，in the TT gauge,the coordinates are marked by the position of freely falling objects so,even when a GW

1Observe that，until we discuss shot noise,in Section 9.4.1,there is really no need to introduce photons,and the whole discussion could be done purely classically,replacing the word “photon" by“wave-packet”.

2As we will discussin a more general setting in Section 9.2.1,the reflection off a 50-50 beam splitter can be modeled multiplying the amplitude of the incoming electric field by a factor $r =$ $+ 1 / \sqrt { 2 }$ for reflection from one side and $r = - 1 / \sqrt { 2 }$ for reflection from the other side,while the transmission multiplies it by $t = 1 / \sqrt { 2 }$ ，and reflection at the perfectly reflecting mirrors at the end of each arm multiplies the amplitude by $- 1$ ，Thus,overall one beam acquires a factor $( 1 / \sqrt { 2 } ) \times ( - 1 ) \times ( 1 / \sqrt { 2 } ) \stackrel { . } { = } - 1 / 2$ and the other a factor $+ 1 / 2$

is passing,the coordinates of freely falling masses by definition do not change.Of course, the mirrbrs of a ground-based interferometer are not freely falling；rather，the Earth's gravity is compensated by the suspensions.However,as we already discussed in Section 1.3.3,these forces are static,compared tφ the frequency of the GWs that we are searching and,as far as the mbtion in the horizontal plane is concerned the mirors can be taken to bein free fall,i.e.they follow the geodesics of the time-dependent part ofthe gravitational field.3

3Of course,there will also be some nonstatic forces,such as those due to suspension thermal noise or,more generally，to the coupling with the environment,which will provide the background noise,and that will be discussed in Section 9.4.

Thus,in the TT gauge description,the coordinates of the mirrors and of the beam-splitter are not affected by the passage of the wave. We define the origin of the coordinate system as the location of the beamsplitter,while the position of the mirror which terminates the x arm defines the point with coordinates (Lx,O),and the position of the other mirror defines the point with coordinates (O,Ly),and this remains true also when a GW is present.

4The response to GWs with arbitrary direction and polarization will be studied in Section 9.2.3.

In the TT gauge description,the physical effect of the GW is manifested in the fact that it affects the propagation of light between these fixed points.We assume for thle moment that the GW has only the plus polarization,and comes from the z direction.4 In the z = O plane of the interferometer we therefore have

$$
h _ { + } ( t ) = h _ { 0 } \cos { \omega _ { \mathrm { g w } } t } ,
$$

and the space-time interval in ithe TT frame is given by

$$
d s ^ { 2 } = - c ^ { 2 } d t ^ { 2 } + [ 1 + h _ { + } ( t ) ] d x ^ { 2 } + [ 1 - h _ { + } ( t ) ] d y ^ { 2 } + d z ^ { 2 } .
$$

Photons travels along null geodesics,ds² = O,so for the light in the r arm we have,to first order in ho,

$$
d x = \pm d t \left[ 1 - { \frac { 1 } { 2 } } h _ { + } ( t ) \right] ,
$$

where the plus sign holds for the travel from the beam-splitter to the mirror and the minus sign for the return trip. Consider a photon that leaves the beam-splitter at a tiine to.It reaches the mirror,at the fixed coordinate x=Lx,ata time ti obtained integrating eq.(9.8) with the plus sign,

$$
L _ { x } = c ( t _ { 1 } - t _ { 0 } ) - { \frac { c } { 2 } } \int _ { t _ { 0 } } ^ { t _ { 1 } } d t ^ { \prime } h _ { + } ( t ^ { \prime } ) .
$$

Then the photon is reflected and reaches again the beam-splitter at a time t2 obtained integrating eq. (9.8) with the minus sign,between $x = L _ { x }$ and $x = 0$

$$
\begin{array} { l } { { \displaystyle \int _ { L _ { x } } ^ { 0 } d x = - c \int _ { | t _ { 1 } } ^ { t _ { 2 } } d t ^ { \prime } \left[ 1 - \frac 1 2 h _ { + } ( t ^ { \prime } ) \right] , } } \\ { { \displaystyle L _ { x } = c ( t _ { 2 } - t _ { 1 } ) - \frac { c } { 2 } \int _ { t _ { 1 } } ^ { t _ { 2 } } d t ^ { \prime } h _ { + } ( t ^ { \prime } ) . } } \end{array}
$$

Summing eqs.(9.9) and (9.11) we get

$$
t _ { 2 } - t _ { 0 } = { \frac { 2 L _ { x } } { c } } + { \frac { 1 } { 2 } } \int _ { t _ { 0 } } ^ { t _ { 2 } } d t ^ { \prime } h _ { + } ( t ^ { \prime } ) .
$$

For a given value of $t _ { 0 }$ ,the time ofarrival $t _ { 2 }$ after a round trip in the $x$ arm is therefore $t _ { 0 } + 2 L _ { x } / c$ ，plusa correction of order $h _ { 0 }$ .In the upper limit of the integral on the right-hand side we can replace $t _ { 2 }$ by $t _ { 0 } + 2 L _ { x } / c$ ，since the integrand is already $O ( h _ { 0 } )$ and we are anyway neglecting terms $O ( h _ { 0 } ^ { 2 } )$ ,so we get

$$
\begin{array} { c } { { \displaystyle t _ { 2 } - t _ { 0 } = \frac { 2 L _ { x } } { c } + \frac { 1 } { 2 } \int _ { t _ { 0 } } ^ { t _ { 0 } + 2 L _ { z } / c } \} d t ^ { \prime } h _ { 0 } \cos ( \omega _ { \mathrm { g w } } t ^ { \prime } ) } } \\ { { \displaystyle \qquad = \frac { 2 L _ { x } } { c } + \frac { h _ { 0 } } { 2 \omega _ { \mathrm { g w } } } \left\{ \sin [ \omega _ { \mathrm { g w } } ( t _ { 0 } + 2 L _ { x } / c ) ] - \sin \omega _ { \mathrm { g w } } t _ { 0 } \right\} . } } \end{array}
$$

Using the identity $\sin ( \alpha + 2 \beta ) - \sin \alpha = 2 \sin \beta \cos ( \alpha + \beta )$ we can rewrite this as

$$
t _ { 2 } - t _ { 0 } = { \frac { 2 L _ { x } } { c } } + { \frac { h _ { 0 } L _ { x } } { c } } { \frac { \sin ( \omega _ { \mathrm { g w } } L _ { x } / c ) } { ( \omega _ { \mathrm { g w } } L _ { x } / c ) } } \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ] .
$$

Observe that the difference $t _ { 2 } - t _ { 0 }$ is a function of the time $t _ { 0 }$ at which the photon left the beam-splitter,because of the term $\cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ]$ Using eq. (9.6),we can also rewrite the above result as

$$
t _ { 2 } - t _ { 0 } = \frac { 2 L _ { x } } { c } + \frac { L _ { x } } { c } h ( t _ { 0 } + L _ { x } / c ) \frac { \sin ( \omega _ { \mathrm { g w } } L _ { x } / c ) } { ( \omega _ { \mathrm { g w } } L _ { x } / c ) } .
$$

The quantity $t _ { 0 } + L _ { x } / c$ which appears in the argument of $h ( t )$ is,to zeroth order in $h _ { 0 }$ ,the value of time $t _ { 1 }$ at which the photon touches the far mirror on the $x$ arm.This result will be easily understood physically in the next subsection,thanks to the Newtonian intuition that we can use in the proper detector frame. The function

$$
\operatorname { s i n c } \left( { \frac { \omega _ { \mathrm { z w } } L } { c } } \right) \equiv { \frac { \sin ( \omega _ { \mathrm { g w } } L / c ) } { ( \omega _ { \mathrm { g w } } L / c ) } }
$$

goes to one when $\omega _ { \mathrm { g w } } L / c \to 0$ .Therefore,when the period of the GW is large compared to $L _ { x } / c$ ,theshift $\Delta t$ in the travel time $t _ { 2 } \sim t _ { 0 }$ ， with respect to the unperturbed value $2 L _ { x } / c$ ，is simply $h ( t _ { 1 } ) L _ { x } / c$ If $\omega _ { \mathrm { g w } } L _ { x } / c \gg 1$ $\Delta t$ is suppressed.This is clearly understood physically: if $\omega _ { \mathrm { g w } } L _ { x } / c \gg 1$ ，during the travel time of the photon $h ( t )$ changes sign many times,so it contributes sometimes positively and sometimes negatively to $\Delta t$ ,and these contributions partially cancel out.A plot of the function $\operatorname { s i n c } ( x )$ is shown in Fig9.2.

In the $y$ arm the analysis is similarbut now the sign of $h ( t )$ is reversed, as we see from eq.(9.7),so we now have

$$
t _ { 2 } - t _ { 0 } = \frac { 2 L _ { y } } { c } - \frac { L _ { y } } { c } h ( t _ { 0 } + L _ { y } / c ) \frac { \sin ( \omega _ { \mathrm { g w } } L _ { y } / c ) } { ( \omega _ { \mathrm { g w } } L _ { y } / c ) } .
$$

![](images/08fa01dad141aaab9a35b92a7640e292560c65e2f59b5f649e93b442730e19ea.jpg)  
Fig.9.2 The function $\begin{array} { r l } { \operatorname { s i n c } ( x ) } & { { } = } \end{array}$ $( 1 / x ) \sin x$ (solid line) and,for comparison，the function $1 / x$ (dashed line).

In practice we willbe interested in the light that comes out of the beam splitter at a given value of the observation time $t$ so it is useful to rewrite these relations holding fixed the value of the time t2 = t at which we observe the light that has recombined at the beam-splitter. and computing the corresponding value of $t _ { 0 }$ .In order to come back at the beam-splitter at time t, the light that went through the x arm must havestarteditsround-tiptraeatatime $t _ { 0 } ^ { ( x ) }$ obtained inverting eq.(9.15) to first order in ho,which means that h(to+Lx/c) is replaced by $h ( t - 2 L _ { x } / c + L _ { x } / c ) = h ( t | - L _ { x } / c )$ s0

$$
t _ { 0 } ^ { ( x ) } = t - \frac { 2 L _ { x } } { c } - \frac { L _ { x } } { c } \dot { h } ( t - L _ { x } / c ) \operatorname { s i n c } \left( \omega _ { \mathrm { g w } } L _ { x } / c \right) ,
$$

and similarly the light that went through the $y$ arm, in order to arrive back at the beam-splitter at the same time t,must have started its round-triptreatit $t _ { 0 } ^ { ( y ) }$ given by

$$
t _ { 0 } ^ { ( y ) } = t - \frac { 2 L _ { y } } { c } + \frac { L _ { y } } { c } h ( t - L _ { y } / c ) \operatorname { s i n c } \left( \omega _ { \mathrm { g w } } L _ { y } / c \right) .
$$

5The superscript (x） on E(x)(t) reminds us that this is the electric field of the light that went through the x-arm, and should not be confused with the xcomponent of the electric field vector. Here we are considering a given spatial component of the electric field.

Again, we use the fact that the phase of the feld is conserved during the free propagation. Setting the origin of the coordinate system at the beam-splitter,and writing the electric field of the light as in eq. (9.1). we see that the light that is at the beam splitter $( \mathbf { x } = 0 )$ at time $t _ { 0 } ^ { ( x ) }$ has a phase $\exp \{ - i \omega _ { \mathrm { L } } t _ { 0 } ^ { ( x ) } \}$ Thefreepropagationalong thearmdoes not change this phase,while reflections and transmisson at the mirrors give an overall factor $\pm 1 / 2$ ,see Note 2 on page 471, so5

$$
\begin{array} { l } { { \displaystyle E ^ { ( x ) } ( t ) = - \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } ^ { ( x ) } } } \ ~ } \\ { { \displaystyle ~ = - \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L _ { x } / c ) + i \Delta \phi _ { x } ( t ) } , } } \end{array}
$$

where

$$
\Delta \phi _ { x } ( t ) = h _ { 0 } \frac { \omega _ { \mathrm { L } } L _ { x } } { c } \mathrm { s i n c } \left( \omega _ { \mathrm { g w } } L _ { x } / c \right) \mathrm { c o s } \left[ \omega _ { \mathrm { g w } } \left( t - L _ { x } / c \right) \right] ,
$$

and similarly the field that went through the $y$ arms, at time $t$ has the form

$$
\begin{array} { l } { { \displaystyle { \cal E } ^ { ( y ) } ( t ) = + \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } ^ { ( y ) } } } } \\ { { ~ = + \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L _ { y } / c ) + i \Delta \phi _ { y } ( t ) } , } } \end{array}
$$

where

$$
\Delta \phi _ { y } ( t ) = - h _ { 0 } \frac { \omega _ { \mathrm { L } } L _ { y } } { c } \mathrm { s i n c } \left( \omega _ { \mathrm { g w } } L _ { y } / c \right) \mathrm { c o s } \left[ \omega _ { \mathrm { g w } } \left( t - L _ { y } / c \right) \right] .
$$

6Except for a small asymmetry,the Schnupp asymmetry,that we will discuss in Section 9.3.2.

In general, $L _ { x }$ and $L _ { y }$ will be made as close as possible, inorder to cancel many common noise in the two arms. Thus, in△x and △y which are already of order $h _ { 0 }$ we simply replace $L _ { x }$ and $L _ { y }$ by $L =$

$( L _ { x } + L _ { y } ) / 2$ ，while in the terms $t - 2 L _ { x } / c$ and $t - 2 L _ { y } / c$ we still take into account any small difference between $L _ { x }$ and $L _ { y }$ ，writing $2 L _ { x } =$ $2 L + \left( L _ { x } - L _ { y } \right)$ and $2 L _ { y } = 2 L - \left( L _ { x } - L _ { y } \right)$ Then

$$
\begin{array} { l } { { \displaystyle E ^ { ( x ) } ( t ) = - \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L / c ) + i \phi _ { 0 } + i \Delta \phi _ { x } ( t ) } \ , } } \\ { { \displaystyle E ^ { ( y ) } ( t ) = + \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L / c ) - i \phi _ { 0 } + i \Delta \phi _ { y } ( t ) } \ , } } \end{array}
$$

where

$$
\phi _ { 0 } = k _ { \mathrm { L } } \big ( L _ { x } - L _ { y } \big ) ,
$$

$\Delta \phi _ { y } = - \Delta \phi _ { x }$ ,and

$$
\begin{array} { r l } & { \Delta \phi _ { x } ( t ) = h _ { 0 } k _ { \mathrm { L } } L \operatorname { s i n c } \left( \omega _ { \mathrm { g w } } L / c \right) \cos [ \omega _ { \mathrm { g w } } ( t - L / c ) ] } \\ & { \qquad \equiv \left| \Delta \phi _ { x } \right| \cos ( \omega _ { \mathrm { g w } } t + \alpha ) , } \end{array}
$$

with $\alpha = - \omega _ { \mathrm { g w } } L / c$ a phase.The total phase difference induced by GWs in the Michelson interferometer is

$$
\Delta \phi _ { \mathrm { M i c h } } \equiv \Delta \phi _ { x } - \Delta \phi _ { y } = 2 \Delta \phi _ { x } .
$$

The total electric field at the output is

$$
\begin{array} { r l } & { E _ { \mathrm { t o t } } ( t ) = E ^ { ( x ) } ( t ) + E ^ { ( y ) } ( t ) } \\ & { \qquad = - i E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L / c ) } \sin [ \phi _ { 0 } + \Delta \phi _ { x } ( t ) ] . } \end{array}
$$

Tle phase $\phi _ { 0 }$ is a parameter that the experimenter can adjust, choosing the best working point for the interferometer,as we will discuss in Section 9.3.2,while $\Delta \phi _ { x } ( t )$ contains the effect of the GW.In the limit $\omega _ { \mathrm { g w } } L / c \ll 1$ ,eq.(9.27) reduces to

$$
\Delta \phi _ { x } ( t ) \simeq h ( t - L / c ) k _ { L } L .
$$

Comparing with eq. (9.26) we see that,in this limit,the effect of the GW on the phase shift is formally equivalent to a change of $L _ { x } - L _ { y }$ given by

$$
\frac { \Delta ( L _ { x } - L _ { y } ) } { L } \simeq h ( t - L / c ) .
$$

The total power $P \sim | E _ { \mathrm { t o t } } | ^ { 2 }$ observed at the photodetector is modulated by the GW signal as

$$
\begin{array} { l } { P = P _ { 0 } \sin ^ { 2 } [ \phi _ { 0 } + \Delta \phi _ { x } ( t ) ] } \\ { \displaystyle = \frac { P _ { 0 } } { 2 } \left\{ 1 - \cos [ 2 \phi _ { 0 } + 2 \Delta \phi _ { x } ( t ) ] \right\} } \\ { \displaystyle = \frac { P _ { 0 } } { 2 } \left\{ 1 - \cos [ 2 \phi _ { 0 } + \Delta \phi _ { \mathrm { M i c h } } ( t ) ] \right\} . } \end{array}
$$

Clearly, we want to have $\Delta \phi _ { \mathrm { M i c h } }$ as Iarge as possible. For a GW of a given frequency wgw, we see from eq.(9.27) that the dependence on L is given by the factor $( \omega _ { \mathrm { L } } L / c ) \mathrm { s i n c } ( \omega _ { \mathrm { g w } } L / c ) = ( \omega _ { \mathrm { L } } / \omega _ { \mathrm { g w } } ) \mathrm { s i n } ( \omega _ { \mathrm { g w } } L / c )$

Thutheoptiallengthofhssiveby $\omega _ { \mathrm { g w } } L / c = \pi / 2$ ie L=Xgw/4. In terms of fgw=wgw/(2π),this gives

$$
L \simeq 7 5 0 \mathrm { k m } \left( \frac { 1 0 0 \mathrm { H z } } { f _ { \mathrm { g w } } } \right) .
$$

7More precisely,for the value ofL given in eq.(9.33),the time shift always keeps the same sign for a photon whose time of time of entry inside the cavity is properly synchronized with the phase of the GW.For larger values,there is at least a partial cancellation,no matter what is the relation between the phase of the GW and the time of entry of the photon.

For such a value of L,the time shift induced by the GW on the light has the same sign all along its rdund trip in a arm,so the effect adds up For longer arms,the GW amplitude inverts its sign during the round trip,so past this moment it starts canceling the phase shift that the light already accumulated.7 Arms of hundreds of kms are impossible to obtain in a ground-based interferometer,for practical and financial reasons.We will see in Section 9.2 how to “fold” this optimal pathlength of the light into an interferometers of manageable size.

It is useful to realize that the effect of the GW on the laser light to generate sidebands in the light propagating in each of the two arms Using eq.(9.27),and making use of the fact that △x is linear in ho,w we can expand E(x)(t) in eq. (9.24) to order h as

$$
\begin{array} { l } { { \displaystyle E ^ { ( x ) } ( t ) = - \frac { 1 } { 2 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } ( t - \mathrm { 2 } L / c ) + i \phi _ { 0 } } \left[ 1 + i | \Delta \phi _ { x } | \cos ( \omega _ { \mathrm { g w } } t + \alpha ) \right] } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } E _ { 0 } e ^ { i \beta } \left[ e ^ { - i \omega _ { \mathrm { L } } } + \frac { i } { 2 } | \Delta \phi _ { x } | e ^ { i \alpha } e ^ { - i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) t } \right. } } \\ { { \displaystyle \qquad \left. + \frac { i } { 2 } | \Delta \phi _ { x } | e ^ { - i \alpha } e ^ { - i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) t } \right] , } } \end{array}
$$

with β an irrelevant constant phase. Thus, beside the original electromagnetic wave at a frequency qL (the“carrier”,in the language of radio engineering)，we have two more electromagnetic waves,at the frequencies $\omega _ { \mathrm { L } } \pm \omega _ { \mathrm { g w } }$ (the“sidebands). The modulus of the amplitude of the sidebands is O(ho) with respect to the carrier,and is given by |△Φxl/2.

8This is correct as far as the fastvarying part of the gravitational field is concerned,while the static gravitational field of the Earth is compensated by the mirror suspensions,and other effects related to the laboratory frame (Coriolis forces,etc.) are negligible because slowly varying，see the detailed discussion in Section 1.3.3.

# 9.1.2 The interactionlin the proper detector frame

It is instructive to compare the above results,obtained in the TT frame with the description obtained using the language of the proper detector frame. Recall from Section 1.3.3 that the proper detector frame is the one implicitly used by the experimenter when he/she thinks about the apparatus. In particular， here coordinates are not marked by frely faling masses,as in the TT gauge,but rather are measured with a rigid ruler. We saw that in the proper detector frame the effect of the passage of a GW is a displacement of the test masses from their original position and,if these test masses are at a distance small compared to the reduced wavelength Xgw of the GW,this displacement is determined by the equation of the geodesic deviation (1.95).At the same time,the space-time metric can be taken as flat,at least in a region of space smal compared to the scale of variation of the gravitational wave,which is its reduced wavelength $\dot { \lambda } _ { \mathrm { g w } }$ .8

Thus, the proper detector frame description has the advantage of being very intuitive,since in a first approximation we can use the language of flat space-time,and the interaction of the mirrors with GWs is described by the equation of the geodesic deviation,i.e. in terms of Newtonian forces,so we can use our Newtonian intuition.However it must be kept in mind that,contrary to the TT gauge description,which is exact,the proper-frame description is approximate,and is valid only if the test mases are at a distance small compared to the reduced wavelength $\dot { \lambda } _ { \mathrm { g w } }$ of the GW, see cq. (1.97). Since fof a Michelson interferometer the distance between the beam-splitter and the end mirror of an arm is the arm-length $L$ ,the proper detector frame description assumes $L \ll \dot { \lambda } _ { \mathrm { g w } }$ ， that is,

$$
\frac { \omega _ { \mathrm { g w } } L } { c } \ll 1 .
$$

Thus,we cannot expect to recover the full TT gauge result (9.27), which is exact,but only its limit for small values of $\omega _ { \mathrm { g w } } L / c$

We first perform the computationlin the proper detector frame to lowest-order in $\omega _ { \mathrm { g w } } L / c$ .In this limit the space-time metric is exactly fat,see eq.(1.86),while the effect of the GW on the test masses is given by the equation of the geodesic deviation,eq.(1.95).Thus,the situation is reversed compared to the TT gauge description.In the TT gauge,the position of the mirrors is not affected by GWs,while the propagation of light between the mirrors is affected. In the proper detector frame, the mirrors are affected by the GWs,while light propagation is not. We fix the origin of the coordinate system on the beam-splitter so,by definition,the beam-splitter does not imove,and we consider as before a GW with only the plus polarization coming from the $z$ direction, written as in eq. (9.6). The equation of the geodesic equation for the mirror on the $\boldsymbol { \mathscr { x } }$ arm,described by coordinates $( \xi _ { x } , \xi _ { y } )$ ,is then9

$$
\ddot { \xi } _ { x } = \frac { 1 } { 2 } \ddot { h } _ { + } \xi _ { x } ,
$$

while $\xi _ { y } ( t )$ remains zero at all times if $\xi _ { y } ( 0 ) = \dot { \xi } _ { y } ( 0 ) = 0$ Equation (9.36) can be solved perturbatively in $h _ { 0 }$ ；to zeroth order we have $\xi _ { x } = L _ { x }$ ，s0 to $O ( h _ { 0 } )$ we get $\ddot { \xi } _ { x } = ( 1 / 2 ) \ddot { h } _ { + } L _ { x }$ ,which has the solution

$$
\xi _ { x } ( t ) = L _ { x } + \frac { h _ { 0 } \ L _ { x } } { 2 } \cos \omega _ { \mathrm { g w } } t ,
$$

where we choose the integration constants so that the average value of $\xi _ { x }$ over one period of the GW is equal to $L _ { x }$ ,and the average value of the velocity $\dot { \xi } _ { x }$ vanishes.

Since space-time is fat,a photon that starts at the beam-splitter at tiine $t _ { 0 }$ ,moving along the positive $\boldsymbol { x }$ axis,follows the trajectory $x ( t ) =$ $c ( t - t _ { 0 } )$ ,so it rcaches the mirror at a time $t _ { 1 }$ given by $c ( t _ { 1 } - t _ { 0 } ) = \xi _ { x } ( t _ { 1 } )$ This equation is easily solved for $t _ { 1 }$ ，perturbatively in $h _ { 0 }$ .To zeroth orderin $h _ { 0 }$ we get the trivial result $t _ { 1 } = t _ { 0 } + ( L _ { x } / c )$ .Inserting this into $\cos \omega _ { _ \mathrm { 3 W } } t$ in eq. (9.37) (which is already multiplied by $h _ { 0 }$ ，we get

$$
c ( t _ { 1 } - t _ { 0 } ) = L _ { x } + \frac { h _ { 0 } L _ { x } } { 2 } \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ] .
$$

9The fact that here appears the form of $h _ { \mu \nu }$ in the TT gauge,even if we are working in the proper detector frame, is a consequence of the fact that the right-hand side of eq.(9.36) is really $- \bar { c } ^ { 2 } R _ { 1 0 j 0 } \xi ^ { j }$ ,see eq. (1.93).Recall from Section 1.1 that,in linearized theory, the Riemann tensor is invariant under coordinate transformations,so we are free to compute it in the frame that we wish,and in particular we can use the form of $h _ { \mu \nu }$ in the TT gauge.

10This can be shown by observing that the geodesic equation (1.66) for a mirror moving non-relativistically is simply $\ddot { \xi } ^ { i } = - \Gamma _ { 0 0 } ^ { i } ( \xi )$ Expanding it to second order in $\xi$ ，with $\Gamma _ { 0 0 } ^ { i } ( \xi = 0 ) = 0$ we get

$$
\ddot { \xi } ^ { i } = - \xi ^ { j } \partial _ { j } \Gamma _ { 0 0 } ^ { i } - \frac { 1 } { 2 } \xi ^ { j } \xi ^ { k } \partial _ { k } \partial _ { j } \Gamma _ { 0 0 } ^ { i } + O ( \xi ^ { 3 } ) ,
$$

where the derivativesof To are computed at $\xi = 0$ The first term gives the equation of motion that we already used.For a mirror along the $\boldsymbol { x }$ arm $\xi ^ { i } = ( \xi _ { x } , 0 , 0 )$ ，so the_second term is proportional to $\partial _ { 1 } ( \partial _ { 1 } \Gamma _ { 0 0 } ^ { 1 } )$ A plane wave propagating along the $z$ direction is function only of $t$ and $z ,$ and so its Riemann tensor，as wellas (),is independent of $_ x$ and $\partial _ { 1 } ( \partial _ { 1 } \Gamma _ { 0 0 } ^ { 1 } )$ vanishes.

The round-trip time is twice as large, so the photon gets back at the beam-splitter at a time t2 given by

$$
t _ { 2 } - t _ { 0 } = \frac { 2 L _ { x } } { c } + \left| \frac { h _ { 0 } L _ { x } } { c } \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ] \right| .
$$

This coincide with the result that we got in the TT gauge,eq.(9.14), er cept that the function sinc $( \omega _ { \mathrm { g w } } L / c ) \stackrel { \smile } { = } [ \sin ( \omega _ { \mathrm { g w } } L / c ) ] / [ \omega _ { \mathrm { g w } } L / c ]$ has been replaced by one,which is the lowest-order term of its Taylor expansiol. This is as expected, since the proper-frame computation just performed is valid only to lowest order $\mathrm { i n } | \omega _ { \mathrm { g w } } L / c$

It is instructive to compute also the next term in the expansion in $\omega _ { \mathrm { g w } } L / c$ in the proper detector frame,and verify that we correctly recover the next term in the expansion of $\mathrm { s i n c } \left( \omega _ { \mathrm { g w } } L / c \right)$ . In principle, we have two kinds of corrections. (1) Corrections to the equation of motion of the mirrors,since the geodesic equation that we have used is the first term in an expansion in $L / \lambda _ { \mathrm { g w } } = \omega _ { \mathrm { g w } } L / c _ { \mathrm { g w } }$ as it is clear from the derivation leading from eq.(1.66) to eq. (1.71).(2) Correction to the propagation of the photons,since the space-time metric is no longer fat.

Actually,the former type of correction in our problem vanishes at next-to-leading order.10 The fitst correction to the photon propagation can be computed using the metric (1.87). For the propagation along a trajectory with $y = z = 0$ (and therefore with $d y = d z = 0$ ），recalling that the Riemann tensor is antisymmetric in the first and second pair of indices, eq. (1.87) reduces td

$$
d s ^ { 2 } = - c ^ { 2 } d t ^ { 2 } ( 1 + R _ { 0 1 0 1 } x ^ { 2 } ) + d x ^ { 2 } .
$$

We can compute the Riemann tensor using the form of $h _ { \mu \nu }$ in the TT gauge (compare with Note 9) which gives,for a wave with only the plus polarization,

$$
\begin{array} { r } { R _ { 0 1 0 1 } = \displaystyle - \frac { 1 } { 2 c ^ { 2 } } { \ddot { h } } _ { + } } \\ { = \displaystyle \frac { \omega _ { \mathrm { g w } } ^ { 2 } } { 2 c ^ { 2 } } h _ { 0 } \cos { \omega _ { \mathrm { g w } } t } , } \end{array}
$$

see eq.(1.94).Light propagation is obtained imposing $d s ^ { 2 } = 0$ in eq.(9.40)；then,to next-to-leading order,the position $x ( t )$ of a photon propagating along the x arm is obtained integrating

$$
d x = \pm c d t \left[ 1 + \frac { \omega _ { \mathrm { g w } } ^ { 2 } } { 4 c ^ { 2 } } x ^ { 2 } ( t ) h _ { 0 } \cos { \omega _ { \mathrm { g w } } } t \right] ,
$$

while the motion of the mirrors is stillgiven by eq. (9.37).

Consider a photon that leaveβ the beam-splitter at time to and propagates along the positive $x$ direction. To lowest order in $h _ { 0 }$ we have the trivial result x(t)= c(t-to). Inserting this into the right-hand side of eq. (9.42) we find the solution to order $h _ { 0 }$ ，

$$
x ( t ) = c ( t - t _ { 0 } ) + h _ { 0 } \frac { c \omega _ { \mathrm { g w } } ^ { 2 } } { 4 } \int _ { t _ { 0 } } ^ { t } d t ^ { \prime } ( t ^ { \prime } - t _ { 0 } ) ^ { 2 } \cos { \omega _ { \mathrm { g w } } } t ^ { \prime } .
$$

Writing

$$
\begin{array} { r } { \cos \omega _ { \mathrm { g w } } t ^ { \prime } = \cos [ \omega _ { \mathrm { g w } } ( t ^ { \prime } - t _ { 0 } ) + \omega _ { \mathrm { g w } } t _ { 0 } ] \qquad ( 9 . } \\ { = \cos [ \omega _ { \mathrm { g w } } ( t ^ { \prime } - t _ { 0 } ) ] \cos \omega _ { \mathrm { g w } } t _ { 0 } - \sin [ \omega _ { \mathrm { g w } } ( t ^ { \prime } - t _ { 0 } ) ] \sin \omega _ { \mathrm { g w } } t _ { 0 } , } \end{array}
$$

the integral over $t ^ { \prime }$ can be performed exactly. Consistently with the order to which we are working,we then expand the exact result to the first non-trivial order in $\omega _ { \mathrm { g w } } ( t - t _ { 0 } )$ (which,in the final result,will correspond to the first non-trivial order in $\omega _ { \mathrm { g w } } L / \vert c )$ ,and we get

$$
x ( t ) \simeq c ( t - t _ { 0 } ) + h _ { 0 } \frac { c \omega _ { \mathrm { g w } } ^ { 2 } } { 1 2 } ( t - t _ { 0 } ) ^ { 3 } \cos { \omega _ { \mathrm { g w } } t _ { 0 } } .
$$

The time $t _ { 1 }$ at which the photon reaches the mirror is now obtained solving the equation $x ( t _ { 1 } ) = \xi ( t _ { 1 } )$ iteratively in $h _ { 0 }$ .This gives

$$
c ( t _ { 1 } - t _ { 0 } ) = L _ { x } + \frac { h _ { 0 } L _ { x } } { 2 } \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ] - h _ { 0 } \frac { \omega _ { \mathrm { g w } } ^ { 2 } } { 1 2 c ^ { 2 } } L _ { x } ^ { 3 } \cos ( \omega _ { \mathrm { g w } } t _ { 0 } ) .
$$

Observe that (writing $\epsilon \equiv \omega _ { \mathrm { g w } } L _ { x } / c _ { \mathrm { \ell } }$

$$
\begin{array} { r } { \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + L _ { x } / c ) ] = \cos ( \omega _ { \mathrm { g w } } t _ { 0 } ) \cos \epsilon - \sin ( \omega _ { \mathrm { g w } } t _ { 0 } ) \sin \epsilon \qquad ( \Omega \times \cos \epsilon ) } \\ { = [ 1 + O ( \epsilon ^ { 2 } ) ] \cos ( \omega _ { \mathrm { g w } } t _ { 0 } ) + O ( \epsilon ) \sin ( \omega _ { \mathrm { g w } } t _ { 0 } ) , } \end{array}
$$

so n the last term of eq. (9.46), which is already a factor $( \omega _ { \mathrm { g w } } L _ { x } / c ) ^ { 2 }$ smaller than the second term, we can replace $\cos ( \omega _ { \mathrm { g w } } t _ { 0 } )$ by $\cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } +$ $L _ { x } / c ) ]$ ,since thedifferenceisofhigherorderin $\omega _ { \mathrm { g w } } L _ { x } / c$ .Then we finally get

$$
c ( t _ { 1 } - t _ { 0 } ) = { L _ { x } } + \frac { h _ { 0 } { L _ { x } } } { 2 } \cos [ \omega _ { \mathrm { g w } } ( t _ { 0 } + \ddot { L } / c ) ] \left[ 1 - \frac { 1 } { 6 } \left( \frac { \omega _ { \mathrm { g w } } { L _ { x } } } { c } \right) ^ { 2 } \right] .
$$

Writing similarly the equations for the round trip we find that,to this order in $\omega _ { \mathrm { g w } } L _ { x } / c _ { \mathrm { : } }$ the round-trip travel $t _ { 2 } - t _ { 0 }$ is twice $t _ { 1 } - t _ { 0 }$ In the last bracket wc recognize the first twolterms of the expansion

$$
{ \frac { \sin x } { x } } = 1 - { \frac { x ^ { 2 } } { 6 } } + O ( x ^ { 4 } ) .
$$

We have therefore verified that the analysis in the proper detector frame correctly reproduces the leading and the next-to-leading terms of the TT gauge result given in eq. (9.15). It is also clear from this discusson that, while the description in the detector proper frame is more intuitive, since it allows us to think in terms of Newtonian forces acting on the mirrors,and of light propagating (in a first approximation) in the flat space-time of Newtonian physics,still the TT gauge description is much more powerful,since it allows us to get the exact closed form of the dependence on $\omega _ { \mathrm { g w } } L _ { x } / c$ .In the detector proper frame the computation f still higher-order corrections becomes more and more involved and, without the hindsight from the TT gauge analysis,it would be difficult $1 0$ imagine that the whole series resums to such a simple closed form.

# 9.2Interferometers with Fabry-Perot cavities

We have seen in eq. (9.33) that,to measure GWs with frequencies order of a few hundreds Hz, the optimal choice would be an arm-leng $L$ of several hundreds kms. For Earth-based interferometers this is practice impossible (consider,among other things,that the arms of t interferometers must be enclosed in a very high vacuum system, asm will see in the Section 9.4).Taking into account technological and f nancial constraints,LIGO has arms of length $L = 4$ kmand VIRGO $3 ~ \mathrm { k m }$ ，while GEO600 has $L = 6 0 0 \textrm { m }$ and TAMA has $L = 3 0 0 \mathrm { m }$ idea is therefore to “fold”the optical path of light,making it boum back and forth many times in each arm,before recombining the t beams.A solution that was first considered is the so-called“delay line In this case,in each arm the light beam goes back and forth betwe two mirrors along trajectories that do not superimpose,and which mal different spots on the mirrors. However,to reach an effective path leng of order $7 5 0 \mathrm { k m }$ out of arms of order $3 { - } 4 \mathrm { k m }$ we need $O ( 1 0 0 )$ bounces. the delay line scheme,this leads to unpractically large mirrors.11 Thm the solution which has been adopted in LIGO and VIRGO is that transforming each arm into aFabry-Perot cavity. In the next subse tion we will discuss the principles of operation of a Fabry-Perot (F cavity,and in Section 9.2.2 we will discuss its interaction with a Gv and we will see how it improves on the simple Michelson scheme.

11Furthermore, this scheme turns out to be quite sensitive to the problem that some part of the light is scattered inside the interferometer off the nominal path,and this light interferes with the main beam.

![](images/8e067ee58c59c176c5cfc1f57130c17755a22f59e48b916de32ba696a27628e3.jpg)

# 9.2.1 Electromagnetic fields in a FP cavity

# Reflection and transmissidn coefficients

First of all we recal from elementary electromagnetism that,at the in terface between two media with different index of refraction,the relatim between the incoming field $E _ { \mathrm { i n } } ^ { \mathrm { ( } }$ ,the reflected feld $E _ { \mathrm { r e f l } }$ and the trans mitted field $E _ { \mathrm { t } }$ can be written as

$$
\begin{array} { r l r } { E _ { \mathrm { r e f l } } = r E _ { \mathrm { i n } } , \quad } & { { } } & { E _ { \mathrm { t } } = t E _ { \mathrm { i n } } , } \end{array}
$$

![](images/c2203b9692495976af3521ce4ae5d67b9317b0727ac374a5d544cc8570d0bc85.jpg)  
Fig.9.3 The situation in which the incoming field comes from the denser medium.   
Fig.9.4 The situation in which the incoming field comes from the rarer medium.

where $r$ and $t$ are called the reflection and transmission coefficients respectively,and are in general complex numbers.We consider for tle moment the transmission and reflection across a sharp boundary. a sharp boundary there is no physical mechanism that can produce phase shift,so in this limit $r$ and $t$ are real. More precisely, $( r , t )$ an the reflection and transmission coefficients when $E _ { \mathrm { i n } }$ comes from th first medium,say the denser (from the left in Fig.9.3).Similarly, w denote by $r ^ { \prime }$ and $t ^ { \prime }$ the reflection and transmission coefficients whel $E _ { \mathrm { i n } }$ comes from the second medium,i.e. from the right in Fig. 9. Between these coefficients hold useful relations.In particular, since th energy associated to the electric feld is proportional to $| E | ^ { 2 }$ ,and on sharp boundary there are no losses and $r , t$ are real, energy conservatiol

requires

$$
r ^ { 2 } + t ^ { 2 } = 1 ,
$$

and $r ^ { \prime 2 } + t ^ { \prime } ^ { 2 } = 1$ 12 Between $( r , t )$ and $( \boldsymbol { r } ^ { \prime } , t ^ { \prime } )$ we have so-calle reciprocity relations,which can be obtained as follows. Consider the arrangement shown in Fig. 9.5,in which the incoming electric feld arrives from the left,and there is a gap of width $d$ df a less dense medium between two layers of the more dense medium. We denote by $E _ { \mathrm { { c a v } } }$ and $E _ { \mathrm { c a v } } ^ { \prime }$ ,respectively,the right-moving and left-moving electric fields in the gap, close to the first interface. Then,by definition of reflection and transmission coeffcients,at the first interface we have the two relations

$$
\begin{array} { r } { E _ { \mathrm { c a v } } = t E _ { \mathrm { i n } } + r ^ { \prime } E _ { \mathrm { c a v } } ^ { \prime } , } \\ { E _ { \mathrm { r e f l } } = r E _ { \mathrm { i n } } + t ^ { \prime } E _ { \mathrm { c a v } } ^ { \prime } . } \end{array}
$$

We now take the limit $d \to 0$ In this case $E _ { \mathrm { c a v } }$ and $E _ { \mathrm { { c a v } } } ^ { \prime }$ are also the right and left-moving fields,respectively,at the second interface. Thus, we also have the relations

$$
\begin{array} { r } { E _ { \mathrm { t } } = t ^ { \prime } E _ { \mathrm { c a v } } , } \\ { E _ { \mathrm { c a v } } ^ { \prime } = t ^ { \prime } E _ { \mathrm { c a v } } . } \end{array}
$$

On the other hand,if $d \to 0$ ,there is no gap,and we must have

$$
\begin{array} { c } { E _ { \mathrm { t } } = E _ { \mathrm { i n } } , } \\ { E _ { \mathrm { r e f } } = 0 . } \end{array}
$$

Combining the six relations (9.52)-(9.57)we find the two conditions

$$
\begin{array} { c } { { r ^ { \prime } = - r , } } \\ { { t t ^ { \prime } - r r ^ { \prime } = 1 . } } \end{array}
$$

Inserting eqs. (9.58)and (9.51) intoleq.(9.59)we get $t ^ { \prime } = t$ In conclusion, we have

12More precisely,the energy density is actually proportional to E·D,where $\mathbf { D }$ is the displacement vector. If we define the coefficients $r , t$ in terms of $\mathbf { E }$ we should then write $r ^ { 2 } + t ^ { 2 } ( n _ { 1 } / n _ { 2 } ) = 1$ We can however simply reabsorb $n$ into the definition of $\mathbf { E }$ to keep the equations in simpler forms such as eq.(9.51).In any case,the issue is irrelevant for a situation such as that shown in Fig.9.6, where we are interested in the fields in the vacuum,on both sides of the mirror.

![](images/6aab77ca9789bdb68ca91c674f7fea5de7c7b9245c4fa873ab02787356f8542a.jpg)  
Fig.9.5A gap of a less dense medium between two layersof denser media.

For a perfectly reflecting mirror,reflection from the less dense to the more dense medium is associated to a factor $r ^ { \prime } = - 1$ ，while from the denser to the less dense medium we have $r = 1$

# Reflected,transmitted and interior field in a FP cavity

We can now apply the above results to the study of a Fabry-Perot cavity.A Fabry-Perot cavity consists of two parallel mirrors,that for the time being we assume plane and of infinite transverse extent. We consider a component $E _ { \mathrm { i n } }$ of the incoming electric field.Part of the mcoiming field is reflected and partly transmitted，see Fig.9.6.The transmitted field $E _ { \mathrm { c a v } } ( 0 )$ propagates to the far mirror,where it is partl reflected and partly transmitted. The reflected part goes back to the firs mirror,where again it is partly reflected and partly transmitted,and s on.The total reflected,interjor and transmitted felds are therefor determined by the superpositiqn of many beams,corresponding to th multiple bounces.

![](images/11792e22afee739fc43917f7b38db75541165fa7a15fae12461ad8f037c8d915.jpg)  
Fig.9.6 A schematic Fabry-Perot cavity.

13Multiplerefectionsinside the substrate can be suppressed by using antireflection coatings,but are really eliminated only by giving to the external face of the mirror a wedge-shaped form,so aftera few bounces the photon is simply lost,rather than reentering the main beam with a different phase (which would result in noise). It should however be observed that all these couplings of the phase of the light to the geometry of the optics (such as multiple reflections,phase shifts at the coatings, etc.）are channels from which noise can enter.

The light from the laser comes from the left in Fig. 9.6. The mirron are set with their high-reflectivity coating on the interior of the cavity Before reaching the high-reflectivity coating,light enters from the lef face of the mirror and passes lthrough the substrate,so in general i acquires a further complex phase shift,both from the substrate an from the coating,and can also suffer losses.A beam which enters th cavity and,after a number of round-trips,is reflected back, traverse once more this substrate,acquiring a further phase. The importam point,however,is that these phase shifts are the same for all beam independently of the number of bounces made inside the FP cavity, s they just give an overall phase factor,independent of the length L( the cavity,to the reflected (and transmitted) fields.This phase facto is compensated by the experimenter,moving the position of the mirrol until the interference pattern of the interferometer is on the desire working point (the dark fringe,as we will see),so we can simply forge about them.13 We can therefore simply model the two mirrors of th FP cavity stating that,for the|first mirror,we have real reflection and transmission coefficients $r _ { 1 }$ and $t _ { 1 }$ when the incoming ficld propagate from the interior of the mirror toward the cavity,and $r _ { 1 } ^ { \prime } = - r _ { 1 }$ and $t _ { 1 } ^ { \prime } = t _ { 1 }$ when it is going from the cavity toward the mirror.We the take into account the losses in the mirror writing

$$
r _ { 1 } ^ { 2 } + t _ { 1 } ^ { 2 } = 1 - p _ { 1 } ,
$$

![](images/dc5829d526f18c1405ab37f0abfe71d3dea376f24fdc3a6edea4e87ea8005129.jpg)  
Fig.9.7 A symmetric mirror,with a held $A$ coming from the left and a feld $B$ incoming from the right.

where $p _ { 1 }$ (typically of order ofa few parts per million) represents the losses in the first mirror.We similarly introduce coefficients $( r _ { 2 } , t _ { 2 } )$ an $( r _ { 2 } ^ { \prime } = - r _ { 2 } , t _ { 2 } ^ { \prime } = t _ { 2 } )$ for the second mirror, with $r _ { 2 } ^ { 2 } + t _ { 2 } ^ { 2 } = 1 - p _ { 2 }$ againa field that propagates from the cavity toward the mirror and i reflected back gets a factor $- r _ { 2 }$

Other modelizations of the mirrors are possible. In particular,on could treat the reflection and transmission from the two sides of thi mirror symmetrically so that,if a field $A$ is coming from the left,th reflected field is $A _ { R } = z _ { R } A$ and the transmitted field is $A _ { T } = z _ { T } A$ where $z _ { R }$ and $z _ { T }$ are the reflection and transmission coefficients,whid now a priori can be complex because of the finite thickness of the mirror and which satisfy $| z _ { R } | ^ { 2 } + | z _ { T } | ^ { 2 } = 1 - p$ Similarly,if a field $B$ is coming from the right,the reflected field is $B _ { R } = z _ { R } B$ and the transmitted fieln is $B _ { T } = z _ { T } B$ ，with the same ${ \mathrm { \Sigma } } _ { { \mathcal { Q } } _ { R } , z _ { T } } ^ { \rule { 0.3 cm } { 0 ex } }$ ．In the presence of both a field A coming from the left anda field $B$ coming from the right,as in Fig.9.7 we have

$$
B ^ { \prime } = z _ { T } A + z _ { R } B .
$$

Requiring the energy balance $| A ^ { \prime } | ^ { 2 } + | B ^ { \prime } | ^ { 2 } = ( 1 - p ) ( | A | ^ { 2 } + | B | ^ { 2 } )$ we get the condition Re $\left( z _ { R } z _ { T } ^ { * } \right) = 0$ A possible solution is $z _ { R } = i r$ ， $z _ { T } = t$ where $r$ and $t$ are real and satisfy $\dot { r } ^ { 2 } + t ^ { 2 } = 1 - p$

These different modelizations of the mirrors of a cavity of length $L$ can however be compensated by a constant shift $\Delta L$ of some fraction of wavelength. For instance,with the modelization $r ^ { \prime } = - r$ ，wewill find below that a Fabry-Perot cavity resonates at $2 k _ { \mathrm { L } } L = 2 \pi n$ ，with $n$ integer.Repeating the computation for $z _ { R } = i r$ ,equal for both sides, one would rather find resonances at $2 k _ { \mathrm { L } } L = 2 \pi ( n + 1 / 2 )$ . In practice, the experimenter tunes the position of the mirrors until he/she finds a resonance,and all that matters is thebehavior around resonance,which is the same in the two cases,so the modelization chosen for the mirrors becomes irrelevant．Similarly,using $z _ { R } = i r$ and $z _ { T } = t$ ，instead of eq.(9.5) one would find $| E _ { \mathrm { o u t } } | ^ { 2 } = E _ { \mathrm { 0 } } ^ { 2 } \cos ^ { 2 } [ k _ { \mathrm { L } } ( L _ { y } - L _ { x } ) ]$ ,but again the experimenter simply adjusts the lengths $L _ { x }$ and $L _ { y }$ until he/she finds the desired working point,such as the dark fringe.For definiteness,we will always use the modelization leading to eq. (9.60).

We can now compute the reflected and transmitted felds,and the field inside the cavity,as follows.We choose the coordinates so that the left mirror is at $x = 0$ and the right mirror at $x = L$ .From the laser we send light with an electric field of the form $E _ { 0 } \exp \{ - i \omega _ { \mathrm { L } } t + i k _ { \mathrm { L } } x \}$ Let $t = t _ { 0 }$ be the value of time at which a given wave-packet reaches the mirror,at $x = 0$ .Thus,the corresponding electric field is simply

$$
E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } .
$$

Part of this beam will be immediately reflected back from the mirror, with amplitude $+ r _ { 1 }$ ,giving rise to areflected beam with feld

$$
E _ { \mathrm { r e f } } ^ { ( 0 ) } = r _ { 1 } E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } .
$$

This field will interfere with a beaml that was send toward the mirror earlier,which entered the cavity,was reflected back at the second mirror, and then was transmitted from the first mirror,see Fig.9.8.In order to arrive back at the first mirror at the same time $t _ { 0 }$ ,it must have entered the cavityat time $t _ { 0 } - 2 L / c$ .So,its initial amplitude when it entered the mirror for the first time,arriving from the laser,was $E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } \left( t _ { 0 } - 2 L / c \right) }$ ， that is $E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } e ^ { 2 i k _ { \mathrm { L } } L }$ . After transmission from the first mirror it gets afactor $t _ { 1 }$ ,reflection at the second mirror gives a factor $- r _ { 2 }$ and finally transmission from the first mirror giyes again $t _ { 1 }$ . Thus,at time $t _ { 0 }$ the lotal reflected field gets also a contribution

$$
E _ { \mathrm { r e f l } } ^ { ( 1 ) } = \left[ - t _ { 1 } ^ { 2 } r _ { 2 } e ^ { 2 i k _ { \mathrm { L } } L } \right] E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } .
$$

This beam has a relative amplit ude $- r _ { 2 } t _ { 1 } ^ { 2 } e ^ { 2 i k _ { \mathrm { L } } L }$ compared to the incoming laser field given in eq. (9.64).14 Then,we have the field that entered the cavity at time $t _ { 0 } - 4 L / c$ ,and went twice back and forth in the cavity. It comes out at time $t _ { 0 }$ with an amplitude

$$
E _ { \mathrm { r e f l } } ^ { ( 2 ) } = \left[ - r _ { 1 } r _ { 2 } ^ { 2 } t _ { 1 } ^ { 2 } e ^ { 4 i k _ { \mathrm { L } } L } \right] E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } .
$$

![](images/d8414cb00b4fc567694c95eeb8df41b7c23aadfeefb1a7a959627b0cb5b2c4ac.jpg)  
Fig.9.8 The building up of the reflected field from the interference of the directly reflected beams and of beams that entered the cavity at earlier times and made a number of bounces inside the cavity.For clarity,the various path have been drawn as if they were spatially separated.

14This result is often colloquially explained stating that the field has acquired a phase $e ^ { 2 \cdot i k _ { \mathbf { L } } L }$ from the free propagation,andthe factors $- \gamma _ { 2 } t _ { 1 } ^ { 2 }$ from its various transmissions and refection.This is misleading.Of course, a wave does not acquire any phase factor from its free propagation. Photons in free space propagate along a trajectory $x ( t ) \ = \ x _ { 0 } + c ( t - t _ { 0 } )$ ，so $x ( t ) - c t = x _ { 0 } - c t _ { 0 }$ is a constant,and the phase factor $k _ { \mathrm { L } } x - \omega _ { \mathrm { L } } t = k _ { \mathrm { L } } ( x - c t )$ is also constant along the free propagation．In flat space-time,multiplicative factors and phases are acquired by the amplitude only when there is interaction with matter,i.e.at reflection and transmission from the mirrors,and in our case this gives the factor $- r _ { 2 } t _ { 1 } ^ { 2 }$ The factor $e ^ { 2 i k _ { \mathrm { L } } \breve { L } }$ relative to eq. (9.64) is there because the beam that we are considering entered the cavity earlier, at a time $t _ { 0 } - 2 L / c$ ，and spent a time $2 L / c$ going back and forth in the cavity.Thus,this second beam alreadly had from the start a phase different by a factor $e ^ { 2 i k _ { \mathrm { L } } L }$ ,compared to the field (9.64) that arrives at time $t _ { 0 }$ directly from the laser.

More generally,the feld that entered the cavity at time $t _ { 0 } - n ( 2 L / { \mathfrak { c } } | |$ and performed $n$ round trips comes out at time $t _ { 0 }$ with an amplitude

$$
E _ { \mathrm { r e f l } } ^ { ( n ) } = \left[ - r _ { 1 } ^ { n - \vert 1 } r _ { 2 } ^ { n } t _ { 1 } ^ { 2 } e ^ { 2 n i k _ { \mathrm { L } } L } \right] E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } .
$$

The total reflected feldis therefore given by

$$
\begin{array} { r l } & { E _ { \mathrm { r e f l } } = E _ { 0 } e ^ { - i \omega _ { L } t _ { 0 } } \left[ r _ { 1 } \Big | - t _ { 1 } ^ { 2 } \underset { n = 1 } { \overset { \infty } { \sum } } r _ { 1 } ^ { n - 1 } r _ { 2 } ^ { n } e ^ { 2 n i k _ { L } L } \right] } \\ & { \qquad = E _ { 0 } e ^ { - i \omega _ { L } t _ { 0 } } \left[ r _ { 1 } \Big | - t _ { 1 } ^ { 2 } r _ { 2 } e ^ { 2 i k _ { L } L } \underset { m = 0 } { \overset { \infty } { \sum } } \left( r _ { 1 } r _ { 2 } e ^ { 2 i k _ { L } L } \right) ^ { m } \right] } \\ & { \qquad = E _ { 0 } e ^ { - i \omega _ { L } t _ { 0 } } \left[ r _ { 1 } \Big | - t _ { 1 } ^ { 2 } r _ { 2 } \frac { e ^ { 2 i k _ { L } L } } { 1 - r _ { 1 } r _ { 2 } e ^ { 2 i k _ { L } L } } \right] , } \end{array}
$$

or, using $t _ { 1 } ^ { 2 } = 1 - p _ { 1 } - r _ { 1 } ^ { 2 }$

$$
\boxed { \begin{array} { c } { E _ { \mathrm { r e f l } } = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } \displaystyle \left| \frac { r _ { 1 } - r _ { 2 } ( 1 - p _ { 1 } ) e ^ { 2 i k _ { \mathrm { L } } L } } { 1 - r _ { 1 } r _ { 2 } e ^ { 2 i k _ { \mathrm { L } } L } } . \right. } \end{array} }
$$

The transmited field is computed similarly,

$$
\begin{array} { c } { { E _ { \mathrm { t } } = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } \Big | t _ { 1 } t _ { 2 } \displaystyle \sum _ { n = 0 } ^ { \infty } ( r _ { 1 } r _ { 2 } ) ^ { n } e ^ { i k _ { \mathrm { L } } L ( 2 n + 1 ) } } } \\ { { = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } \displaystyle \frac { t _ { 1 } t _ { 2 } e ^ { i k _ { \mathrm { L } } L } } { 1 - r _ { 1 } r _ { 2 } e ^ { 2 i k _ { \mathrm { L } } L } } . } } \end{array}
$$

The feld inside thecavity,atthe left mirror $( x = 0$ )， again at time $t _ { 0 } ,$ is

$$
\begin{array} { l } { { \displaystyle E _ { \mathrm { c a v } } ( 0 ) = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } ~ t _ { 1 } \sum _ { n = 0 } ^ { \infty } ( r _ { 1 } r _ { 2 } ) ^ { n } e ^ { 2 n { { \it _ { \ a l k } } _ { \mathrm { L } } L } } } } \\ { { \displaystyle ~ = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } ~ \frac { t _ { 1 } } { 1 - { r _ { 1 } r _ { 2 } } e ^ { 2 i k _ { \mathrm { L } } L } } , } } \end{array}
$$

and for the field inside the cavity,at the other mirror,at time $t _ { 0 }$ ,we have $E _ { \mathrm { c a v } } ( L ) = e ^ { i k _ { \mathrm { L } } L } E _ { \mathrm { c a v } } ( 0 )$ . The same results can been obtained also in the following way,which is maybeless vivid physically,but willbe easier to generalize to the situation in which GWs are present.We consider the total reflected, transmitted and cavity fields as shown in Fig.9.6.Then. just as in eqs. (9.52) and (9.53), using $r _ { 1 } ^ { \prime } = - r _ { 1 }$ and $t _ { 1 } ^ { \prime } = t _ { 1 }$ ,at the first mirror we have

$$
\begin{array} { r } { E _ { \mathrm { c a v } } ( 0 ) = t _ { 1 } E _ { \mathrm { i n } } - r _ { 1 } E _ { \mathrm { c a v } } ^ { \prime } ( 0 ) , } \\ { E _ { \mathrm { r e f l } } = r _ { 1 } E _ { \mathrm { i n } } + t _ { 1 } E _ { \mathrm { c a v } } ^ { \prime } ( 0 ) . } \end{array}
$$

Similarly,at the second mirror we have

$$
\begin{array} { r } { E _ { \mathrm { t } } = t _ { 2 } E _ { \mathrm { c a v } } ( L ) , \qquad } \\ { E _ { \mathrm { c a v } } ^ { \prime } ( L ) = - r _ { 2 } E _ { \mathrm { c a v } } ( L ) . } \end{array}
$$

Finally,since the solution inside the cavity is given by plane waves, the feld $E _ { \tt C a v } ( t , x )$ ，which represent aright-moving wave,is proportional to $\exp \{ - i ( \omega _ { \mathrm { L } } t - k _ { \mathrm { L } } x ) \}$ ，while $E _ { \mathrm { c a v } } ^ { \prime } ( t , x )$ ，which represent a left-moving wave, is proportional to $\exp \{ - i ( \omega _ { \mathrm { L } } \} + k _ { \mathrm { L } } x ) \}$ .Thus the cavity felds at $x = L$ and at $x = 0$ ,at equal value bf time,are related by

$$
\begin{array} { r l } & { E _ { \mathrm { c a v } } ( L ) = e ^ { i k _ { L } L } E _ { \mathrm { c a v } } ( 0 ) , } \\ & { E _ { \mathrm { c a v } } ^ { \prime } ( L ) = e ^ { - i k _ { L } L } E _ { \mathrm { c a v } } ^ { \prime } ( 0 ) . } \end{array}
$$

Then we have six equations,eqs. (9.73)-(9.78),that we can solve for the six quantities $E _ { \mathsf { r e f l } } , E _ { \mathsf { t } } , E _ { \mathsf { c a v } } ( 0 ) , E _ { \mathsf { c a v } } ( L ) , E _ { \mathsf { c a v } } ^ { \prime } ( 0 ) , E _ { \mathsf { c a v } } ^ { \prime } ( L )$ ,in terms of $E _ { \mathrm { i n } } = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t }$ .With straightforward algebra we get back the solution found above.For instance,combining eqs. (9.76),(9.77) and (9.78) we get

$$
E _ { \mathrm { c a v } } ^ { \prime } ( 0 ) = - r _ { 2 } \mathrm { e } ^ { 2 i k _ { \mathrm { L } } L } E _ { \mathrm { c a v } } ( 0 ) .
$$

Substituting this into eq. (9.73) we get

$$
\begin{array} { r } { E _ { \mathrm { c a v } } ( 0 ) = t _ { 1 } E _ { \mathrm { i n } } + r _ { 1 } r _ { 2 } e ^ { 2 i k _ { \mathrm { L } } L } E _ { \mathrm { c a v } } ( 0 ) , } \end{array}
$$

from which the solution (9.72) for $E _ { \mathrm { c a v } } ( 0 )$ follows,and similarly we get $E _ { \mathrm { r e f } }$ and $E _ { \mathrm { t } }$

# Resonant FP cavities

We see that the reflected,transmitted and interior fields are all proportional to the factor $1 \dot { / } [ 1 - r _ { 1 } r _ { 2 } \dot { e } ^ { 2 i k _ { \mathrm { L } } L } ]$ When $2 k _ { \mathrm { L } } L = 2 \pi n$ ，with $n = 0 , \pm 1 , \pm 2 , . . .$ ,this factor becomes $1 / ( 1 - r _ { 1 } r _ { 2 } )$ and,if the reflection coefficients $r _ { 1 }$ and $r _ { 2 }$ are close to one,this is large.We therefore have a set of resonances.Physically this means that, for $2 k _ { \mathrm { L } } L = 2 \pi n$ thevarious beams that bounce back and forth interfere constructively,so the feld inside the cavity raises to a very large value. Correspondingly, the transmitted field also gets large.As for the reflected feld,for assessing its strength we must also take into account the dependence on $k _ { \mathrm { L } } L$ of the numerator,which describes the interference between the field that is reflected after having entered the cavity and made one or more round trips,and the field that is immediately reflected.We first consider the power $P _ { t } \sim | E _ { \mathrm { t } } | ^ { 2 }$ of the transmitted field (or,equivalently,of the interior feld, $E _ { \mathrm { { c a v } } }$ ,since $| E _ { \mathrm { t } } |$ and $| E _ { \mathrm { c a v } } | |$ differ just by a constant factor $t _ { 2 }$ ). From eq. (9.71),

$$
| E _ { \mathrm { t } } | ^ { 2 } = E _ { 0 } ^ { 2 } \frac { t _ { 1 } ^ { 2 } t _ { 2 } ^ { 2 } } { 1 + ( r _ { 1 } r _ { 2 } ) ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos 2 k _ { \mathrm { L } } L } .
$$

This is plotted,as afunction of $2 k _ { \mathrm { L } } L$ , in Fig.9.9.Writing $k _ { \mathrm { L } } = \omega _ { \mathrm { L } } / c$ the distance between the maxima is

$$
\Delta \omega _ { \mathrm { L } } = \frac { \pi c } { L } .
$$

This is called the free spectral range of the cavity. Expanding the denominator in eq. (9.81) to quadratig order around a resonance,we find

![](images/19555137966a7f7c0932b9787e55ff2c7cf1cb3d6c0f9eb53c39240883b80e6a.jpg)  
Fig.9.9 $| E _ { \mathrm { t } } | ^ { 2 }$ ,in units of $\left( E _ { 0 } t _ { 1 } t _ { 2 } \right) ^ { 2 }$ ， as a function of $2 k _ { \mathrm { L } } L$ for $r _ { 1 } r _ { 2 } = 0 . 8$

that the full width of the peaks at half maximum is

$$
\delta \omega _ { L } \geq \frac { c } { L } \frac { 1 - r _ { 1 } r _ { 2 } } { \sqrt { r _ { 1 } r _ { 2 } } } .
$$

The finesse $\mathcal { F }$ of the cavity is defined as the ratio of the free spectral range to the full width at half maximum, $\mathcal { F } \equiv \Delta \omega _ { \tt L } / \delta \omega _ { L }$ ,s0

$$
\mathcal { F } = \frac { \pi \sqrt { r _ { 1 } r _ { 2 } } } { 1 - r _ { 1 } r _ { 2 } } .
$$

To understand the physical meaning of these results it is useful to com pute the storage time,i.e. the average time spent by a photon inside the cavity.For simplicity we take $r _ { 2 } ~ \simeq ~ 1$ ，so each photon has an amplitude probability $A ( n )$ of making $n$ round trips,and finally comes out from the first mirror. Recall that the number density of photons is proportional to the modulus squared of the electric feld so the factors $- r _ { 1 }$ and $- r _ { 2 }$ acquired at the reflections from the mirrors are the quantum-mechanical probability amplitudes,while their squared modulus is a probability. Thus,the amplitude for performing $n$ round-trips and then coming out from the first mirror is given by $A ( n ) = t _ { 1 } ^ { 2 } ( - 1 ) ^ { n } ( - r _ { 1 } ) ^ { n - 1 } = \mathrm { c o n s t a n t } \times r _ { 1 } ^ { n }$ ，since each reflection at the far mirror has a probability amplitude $^ { - 1 }$ and at the first mirror $\left( - r _ { 1 } \right)$ Thus,if a photon enters the cavity, the probability that it comes out after $n$ round-trips is

$$
p ( n ) = \frac { r _ { 1 } ^ { 2 n } } { \sum _ { n = 1 } ^ { \infty } r _ { 1 } ^ { 2 n } } ,
$$

where the denominator normalizes the total probability to one. The average number of round-trips is therefore

$$
\sum _ { n = 1 } ^ { \infty } n p ( n ) = { \frac { 1 } { 1 - r _ { 1 } ^ { 2 } } } .
$$

Since each round-trip lasts for a time $2 L / c$ ,the storage time ofthe cavity. i.e. the average time spent inside by a photon,is

$$
\tau _ { s } \equiv \frac { 2 L } { c } \frac { 1 } { 1 - r _ { 1 } ^ { 2 } } .
$$

If $r _ { 1 }$ is close to one we can write $1 - r _ { 1 } ^ { 2 } = ( 1 - r _ { 1 } ) ( 1 + r _ { 1 } ) \simeq 2 ( 1 - r _ { 1 } )$ and we can express the storage time in terms of the finesse,as

$$
\tau _ { s } \simeq \frac { L } { c } \frac { \mathcal { F } } { \pi } .
$$

We see that,in the limit of high finesse,light is trapped in the FP cavity for a long time. If we illuminafe the cavity and then we suddenly shut off the laser at $t \ : = \ : 0$ ， light will still continue to come out from the cavity fora long time.According to eq.(9.85),the intensity of the light coming out after $n$ round trips is proportional to $r _ { 1 } ^ { 2 n } = \exp \{ n \log r _ { 1 } ^ { 2 } \}$ For $r _ { 1 }$ close to one, $\log r _ { 1 } ^ { 2 } = \log [ 1 - ( 1 - r _ { 1 } ^ { 2 } ) ] \simeq - ( 1 - r _ { 1 } ^ { 2 } )$ Therefore the intensity of light decreases with $n$ as $\exp \{ - n \big ( 1 - r _ { 1 } ^ { 2 } \big ) \}$ .Since the light that performs $n$ round trips comes out at time $t = ( 2 L / c ) n$ ,for $r _ { 1 }$ close to one and $r _ { 2 } = 1$ the intensity of the|reflected light decreases with time as $\exp \{ - t ( c / 2 L ) ( 1 - r _ { 1 } ^ { 2 } ) \} = \exp \{ - t / \tau _ { s } \}$ ，with $\tau _ { s }$ given in eq. (9.87), confirming the interpretation of $\tau _ { s }$ asa storage time.

We consider now the reflected feldlWe write $E _ { \mathrm { r e f l } } = | E _ { \mathrm { r e f l } } | e ^ { - i \omega _ { \mathrm { L } } t } e ^ { i \phi }$ and we find from eq. (9.7O) that the phase $\phi$ can be written as $\phi =$ $\phi _ { 1 } - \phi _ { 2 }$ ，where

$$
\begin{array} { r l } & { \tan \phi _ { 1 } = - \displaystyle \frac { r _ { 2 } \left( 1 - p _ { 1 } \right) \sin \left( 2 k _ { \mathrm { L } } L \right) } { r _ { 1 } - r _ { 2 } \left( 1 - p _ { 1 } \right) \cos \left( 2 k _ { \mathrm { L } } L \right) } , } \\ & { \tan \phi _ { 2 } = \displaystyle - \frac { r _ { 1 } r _ { 2 } \sin \left( 2 k _ { \mathrm { L } } L \right) } { 1 - r _ { 1 } r _ { 2 } \cos \left( 2 k _ { \mathrm { L } } L \right) } . } \end{array}
$$

A plot of $\phi$ as a function of $2 k _ { \mathrm { L } } L$ is|shown in Fig.9.10.Two aspects of this graph are interesting.First,away from the resonances (which, as we have seen,are at $2 k _ { \mathrm { L } } L = 2 \pi n$ ），, $\phi$ is almost flat as a function of $2 k _ { \mathrm { L } } L$ ,and is basically equal to zero (imod $2 \pi$ ).So,here the phase of the reflected light is insensitive to changes in the length $L$ of the cavity or of the frequency of the laser light.However,close to the resonances this dependence suddenly becomes very sharp.Writing $2 k _ { \mathrm { L } } L = 2 \pi n + \epsilon$ and expanding for small $\epsilon$ ,eqs.(9.89) and(9.90) give (setting for simplicity $r _ { 2 } = 1$ and $p _ { 1 } = 0$ and neglecting $O ( \epsilon ^ { 2 } )$ ） $\partial \phi / \partial \epsilon = ( 1 + r _ { 1 } ) / ( 1 - r _ { 1 } )$ or, taking $r _ { 1 }$ close to one,

$$
\overline { { \frac { \partial \phi } { \partial \epsilon } \simeq \frac { 2 \mathcal { F } } { \pi } } } .
$$

We can compare this with the result (9.2) for one arm of a simple Michelson interferometer which,in the present notation,reads $\phi = \epsilon$ When $r _ { 1 }$ is close to one,the sensitivity of a $\mathrm { F P }$ cavity to changes in $2 k _ { \mathrm { L } } L$ isenhanced by the large factor $( 2 / \pi ) \mathcal { F }$ ,compared to the arm ofa Michelson interferometer.

The result for generic values of $r _ { 1 } , r _ { 2 }$ (but still such that $\mathcal { F } \gg 1$ can be conveniently written observing that, for large $\mathcal { F }$ ,eq.(9.84) can be inverted to give

$$
r _ { 1 } r _ { 2 } = 1 - \frac { \pi } { \mathcal { F } } + O \left( \frac { \pi ^ { 2 } } { \mathcal { F } ^ { 2 } } \right) .
$$

We define $p$ from

$$
( 1 - p _ { 1 } ) r _ { 2 } ^ { 2 } = \left( 1 - p \right) ,
$$

and we introduce the coupling rate $\sigma$

$$
\begin{array} { r }  \boxed { \begin{array} { r l } & { \sigma = \frac { p \mathcal { F } } { \pi } . } \\ & { } \end{array} } \end{array}
$$

From the condition $r _ { 1 } ^ { 2 } = 1 - p _ { 1 } ^ { 2 } - t _ { 1 } ^ { 2 } < 1 - p _ { 1 }$ it follows that $r _ { 1 } ^ { 2 } r _ { 2 } ^ { 2 } < 1 - p$ and for small $p$ (typical values in VIRGO and LIGO are $p \sim 2 \times 1 0 ^ { - 5 }$ ）

![](images/e467e16dd909703fa81bbdfe8b84f5ac21f720537db94cd0e22ba4c37cd71a84.jpg)  
Fig.9.10 The phase $\phi$ of the refected field,as a function of $2 k _ { \mathrm { L } } L ,$ setting $r _ { 1 } ~ = ~ 0 . 9$ ， $r _ { 2 } ~ = ~ 1$ ， $p _ { 1 } ~ = ~ 0$ We have defined $\phi$ so that it is a continuous function of $2 k _ { \mathrm { L } } L$ rather than reporting it always to the interval $[ 0 , 2 \pi ]$

we have $r _ { 1 } r _ { 2 } < 1 - ( p / 2 )$ .Using eq.(9.92) we then obtain

$$
1 - \frac { \pi } { \mathcal { F } } < 1 - \frac { p } { 2 } ,
$$

which, in terms of $\sigma$ ，gives $\sigma < 2$ Since of course $\sigma > 0$ ,we have

$$
\begin{array} { r } { 0 \ll \sigma < 2 . } \end{array}
$$

Writing $2 k _ { \mathrm { L } } L = 2 \pi n + \epsilon$ and expanding for small $\epsilon$ eqs.(9.89)and (9.90) become tan $\phi _ { 1 } = ( \mathcal { F } \epsilon / \pi ) / ( 1 - \sigma )$ and $\tan \phi _ { 2 } = - \mathcal F \epsilon / \pi$ so $\phi _ { 2 } =$ $- \pi + \arctan ( \mathcal { F } \epsilon / \pi )$ For $\phi = \phi _ { 1 } - \phi _ { 2 }$ we get

$$
\overline { { \phi = \pi + \arctan \left[ \frac { \mathcal { F } \epsilon } { \pi } \frac { 1 } { \mathcal { T } - \sigma } \right] + \arctan \left[ \frac { \mathcal { F } \epsilon } { \pi } \right] } } .
$$

When $\sigma > 1$ this is rewriten more conveniently as

$$
\phi = \arctan \left[ \frac { \mathcal { F } \epsilon } { \pi } \frac { 1 } { \vert \sigma - 1 \vert } \right] + \arctan \left[ \frac { \mathcal { F } \epsilon } { \pi } \right] .
$$

15This at first sight can be surprising. If for instance $r _ { 1 } ~ = ~ 0 . 9 9$ almost all the incoming light is reflected back immediately and is not so intuitive that the total reflected field can be zero. What happens is that the small amount of light that enters the cavity eventually builds up a sufficiently strong interior cavity field,and the part of it that finally leaks back from the first mirror has a large enough amplitude, and the appropriate phase,to cancel the promptly reflected feld.

![](images/dd0ab4a9012a7a84863808923fd83cc21bf8aac728722d96491a27571f042983.jpg)  
Fig.9.11 The phase $\phi$ of the refected field,as a function of $\epsilon =$ $2 k \mathtt { L } L - 2 \pi n$ ,for an overcoupled cavity with $\sigma = 0 . 0 5$ (solid line） and for an undercoupled cavity with $\sigma =$ 1.05 (dashed line).

Observe from eq. (9.70) that,at theresonances,the reflected electri feld is

$$
E _ { \mathrm { r e f l } } = E _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } \frac { r _ { 1 } - r _ { 2 } \left( 1 - p _ { 1 } \right) } { 1 - r _ { 1 } r _ { 2 } } .
$$

In particular, if $r _ { 1 } = r _ { 2 } ( 1 - p _ { 1 } )$ at resonance there is no refected ligit from the cavity. Physically,what happens is that the light that is immediately reflected back interferes destructively with the light that is reflected after one or more round trips in the cavity.15 This situation is called the optimal (or criticdl） cavity coupling. Of course,it is op timal from the point of view of the transmitted field since,except for the losses,all incident light finally leaks out from the second miror. For the arms of a GW interferometer,we willsee that we are interested in the reflected signal and therefore we do not want this situation. I $r _ { 1 } > r _ { 2 } \big ( 1 - p _ { 1 } \big )$ the cavity is undercoupled,while for $r _ { 1 } < r _ { 2 } ( 1 - p _ { 1 } )$ the cavity is overcoupled.In terms df the coupling rate,using the definition (9.94) and neglecting $O ( \pi ^ { 2 } / \mathcal { F } ^ { 2 } )$ in eq. (9.92), we have

$$
\frac { r _ { 1 } - r _ { 2 } ( 1 - p _ { 1 } ) } { 1 - r _ { 1 } r _ { 2 } } = \frac { \sigma - 1 } { r _ { 2 } } ,
$$

so optimal coupling corresponds to $\sigma = 1$ ，while for $0 \textless \sigma \textless 1$ the cavity is overcoupled,and for $1 < \sigma < 2$ the cavity is undercoupled. Observe that Fig.9.10 refers to an overcoupled cavity. For undercoupled cavities, instead,the region where the phase of the reflected field is very sensitive to changes in $2 k _ { \mathrm { L } } L$ becomes smaller and smaller,and disappears completely when $\sigma \to 2$ A comparison of $\phi$ as a function $0 . 1$ $\epsilon$ for $\sigma < 1$ and for $\sigma > 1$ is shown in Fig.9.11. Clearly,the sensitivity to a change of $2 k _ { \mathrm { L } } L$ is higher for an overcoupled cavity.For the arms $\mathrm { o f }$ VIRGO and LIGO,the losses are such that $p \sim 2 \times 1 0 ^ { - 5 }$ and the finesse is $\mathcal { F } \simeq 5 0$ for VIRGO and $\mathscr { F } \simeq 2 0 0$ for LIGO, so we have $\sigma \sim 3 \times 1 0 ^ { - 4 }$ for VIRGO and $\sigma \sim 1 0 ^ { - 3 }$ for LIGO. Therefore these cavities are wel overcoupled.

# 9.2.2 Interaction of a FP cavity with GWs

We have seen that the effective storage time of light,which in the arm of a Michelson interferometer is $2 L / c$ becomes $( L / c ) \mathcal { F } / \pi$ in a Fabry-Perot cavity,i.e. is enhanced bya factor $\mathcal { F } / ( 2 \pi )$ ,and the sensitivity to a phase shift is enhanced by a factor $( 2 / \pi ) \mathcal { F }$ .Since we finally measure a phase shift,we can expect that the same response to GWs of a Michelson interferometer with arm-length of hundreds of kms,as would be optimal for GWs with frequency $\bar { f _ { \mathrm { g w } } } = O ( 1 0 ^ { 2 } ) , \mathrm { H z }$ ,should be obtained replacing thearms by Fabry-Perot cavities with a length of a few kms,and a finesse ${ \mathcal { F } } = O ( 1 0 ^ { 2 } )$ .Thus,our next approximation toward a realistic GW interferometer is as in Fig. 9.12. In this section we study the response of a FP interferometer to GWs,and we will see that the above expectation is indeed correct.

We want to compute how the reflected field of a FP cavity is affected by an incoming GW.We consider a FP cavity oriented along the $\mathscr { X }$ axis and a GW with only the plus polarization propagating along $z$ ，asin eq.(9.6).We begin with a description in the proper detector frame.As we saw in Section 9.1.2,in this frame we can easily obtain the result to lowest order in $\omega _ { \mathrm { g w } } L / c$ by making use of the fact that,even in the presence of GWs, light propagates along the geodesics of flat spacetime,while the mirrors are shaken bya force exerted by GWs,so that their motion is given in eq. (9.37). Therefore the length $L$ of the cavity changes as

$$
\Delta L _ { x } ( t ) = \frac { L h _ { 0 } } { 2 } \cos { \omega _ { \mathrm { g w } } t } .
$$

This induces a change $\Delta \phi _ { x }$ in the pliase $\phi _ { x }$ of the feld reflected from the cavity along the $x$ arm,which is obtained from eq.(9.91),i.e.from $\Delta \phi _ { x } = ( 2 \mathcal { F } / \pi ) \epsilon$ ，setting $\epsilon = 2 k _ { \mathrm { L } } \Delta L$ ：

$$
\begin{array} { l } { \displaystyle \Delta \phi _ { x } \simeq \frac { 4 \mathcal { F } } { \pi } k _ { \mathrm { L } } \Delta L } \\ { \displaystyle = \frac { 2 \mathcal { F } } { \pi } k _ { \mathrm { L } } L h _ { 0 } \cos \omega _ { \mathrm { g w } } t . } \end{array}
$$

The phase shift of a FP cavity along the $y$ arm is obtained reversing the sign of $h _ { 0 }$ (see eq.(9.7)),so the total phase shift in the Fabry-Perot interferometer of Fig. 9.12 is $\Delta \phi _ { \mathrm { F P } } = \Delta \phi _ { x } - \Delta \phi _ { y } = 2 \Delta \phi _ { x }$ .We write $\Delta \phi _ { \mathrm { F P } } ( t ) = | \Delta \phi _ { \mathrm { F P } } | \cos \omega _ { \mathrm { g w } } t$ ，S0

$$
\left| \Delta \phi _ { \mathrm { F P } } \right| = \frac { 4 \mathcal { F } } { \pi } k _ { \mathrm { L } } L h _ { 0 } .
$$

This is the change of phase that would be induced in a Michelson interferometer with arm-length $( 2 / \pi ) \mathcal { F } L$ .Similar to what happens in a Michelson interferometer,we expect tliat,when the storage time $\tau _ { s }$ given in eq.(9.88) becomes comparable to the period of the GW,the sensitivity degrades because we are summing over contributions with both positive and negative sign,so the above result is really the lowest order in an expansion in $\omega _ { \mathrm { g w } } \tau _ { s }$ . To compute the result for $\omega _ { \mathrm { g w } } \tau _ { s }$ generic,we already know from our discussion in Section 9.1.2 that we cannot wor in the proper detector frame,and we must rather switch to a TT gaug description.

![](images/33c03a119d57916e6fbab715e3ee4eb3b8d890af31680b3c1d9e04bb169ec88a.jpg)  
Fig.9.12 The layout of an interferometer with Fabry-Perot cavities.

First，it is useful to observe that，for a FP cavity，we can repea without any modification the derivation done in eq. (9.34) for an arim o a Michelson interferometer,and we again conclude that,if a GW induce a phase shift $\Delta \phi _ { x } ( t ) = | \Delta \phi _ { x } | \cos \omega _ { \mathrm { g w } } \bar { t }$ in the field reflected froma cavity along the $x$ axis,this produces in the reflected field sidebands witl frequencies $\omega _ { \mathrm { { L } } } \pm \omega _ { \mathrm { { g w } } }$ and an amplitude,relative to the carrier, whose modulus is $| \Delta \phi _ { x } | / 2$ in each sideband. Thus,to compute the phase shif $| \Delta \phi _ { x } |$ of the reflected field,toall order in $\omega _ { \mathrm { g w } } \tau _ { s }$ , we can compute in the TT gauge the amplitude of the sidebands of the reflected field.This can be done generalizing the computation of pages 483-485 as follows.

Consider the electric field coming on the first mirror of the cavity from the laser,as in Fig.9.8. This incoming field is monochromatic,an oscillates as $e ^ { - i \omega _ { \mathrm { L } } t }$ .When it enters the cavity and bounces once back and forth,besides acquiring the usual transmissionand reflection coeffcients when a GW is present it also aqquires a phase modulation, so that when it comes back to the first mirrpr it consists of the carrier at frequency $\omega _ { \mathrm { L } }$ plus the two sidebands at $\omega _ { \mathrm { L } } \pm \omega _ { \mathrm { g w } }$ .These three monochromatic fields are partly reflected,with the usual coefficient $- r _ { 1 }$ ,and can make one more round trip in the cavity,and so on. So,we need to know how a generic feld with carrier plu\$ sidebands is modified by a round trip. We therefore consider a right-moving electromagnetic field which,at the left mirror, has the time-dependence

$$
A ( t ) = A _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t } + \frac { 1 } { 2 } h _ { 0 } A _ { \mathrm { 1 } } e ^ { - i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) t } + \frac { 1 } { 2 } h _ { 0 } A _ { 2 } e ^ { - i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) t } ,
$$

while we denote by $B ( t )$ the right-moving field at the end of the round trip,

$$
B ( t ) = B _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t } + \frac { 1 } { 2 } h _ { 0 } B _ { \mathrm { l } } e ^ { - i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) t } + \frac { 1 } { 2 } h _ { 0 } B _ { 2 } e ^ { - i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) t } .
$$

If we denote by $t$ the time at which the field terminates its round-trip. the time $t _ { 0 }$ at which it started is given by (compare with eq.(9.18))

$$
t _ { 0 } = t - \frac { 2 L } { c } - \frac { L } { c } h _ { 0 } \cos [ \omega _ { \mathrm { g w } } ( t - L / c ) ] \mathrm { s i n c } ( \omega _ { \mathrm { g w } } L / c ) .
$$

16Recall that the superposition of carrier and sidebands given in eqs. (9.104) and (9.105) derives from the expansion of a phase factor,see eqs. (9.24) and (9.34).

Since during free propagation the phase is unchanged， we must have (apart from the reflection coeficients at the mirrors that we will add separately) $B ( t ) = A ( t _ { 0 } )$ 16 that is

$$
B ( t ) = A _ { 0 } e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } + \frac { 1 } { 2 } h _ { 0 } A _ { 1 } e ^ { - i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) t _ { 0 } } + \frac { 1 } { 2 } h _ { 0 } A _ { 2 } e ^ { - i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) t _ { 0 } } .
$$

Using eq. (9.106)and developing to first order in $h _ { 0 }$ ，

$$
\begin{array} { r l r } {  { e ^ { - i \omega _ { \mathrm { L } } t _ { 0 } } = e ^ { - i \omega _ { \mathrm { L } } ( t - 2 L / c ) } } } \\ & { } & { + \frac { 1 } { 2 } h _ { 0 } i k _ { \mathrm { L } } L \operatorname { s i n c } { ( \omega _ { \mathrm { g w } } L / c ) e ^ { i ( 2 \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) L / c } e ^ { - i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) t } } } \\ & { } & { + \frac { 1 } { 2 } h _ { 0 } i k _ { \mathrm { L } } L \operatorname { s i n c } { ( \psi _ { \mathrm { g w } } L / c ) e ^ { i ( 2 \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) L / c } e ^ { - i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) t } } . } \end{array}
$$

Again to order $h _ { 0 }$ ，we can simply replace the terms $h _ { 0 } e ^ { - i ( \omega _ { \mathrm { L } } \pm \omega _ { \mathrm { g w } } ) t _ { 0 } }$ in eq.(9.107） by $h _ { 0 } e ^ { - i ( \omega _ { \mathrm { L } } \pm \omega _ { \mathrm { g w } } ) ( t - 2 L / c ) }$ Collecting terms with the same time dependence in eq.(9.107) and comparing with eq.(9.105) we get a matrix relation $B _ { i } = X _ { i j } A _ { j }$ (with $i = 0 , 1 , 2$ )，where

$$
{ \bf X } = \left( \begin{array} { c c c } { { X _ { 0 0 } } } & { { 0 } } & { { 0 } } \\ { { X _ { 1 0 } } } & { { X _ { 1 1 } } } & { { 0 } } \\ { { X _ { 2 0 } } } & { { 0 } } & { { X _ { 2 2 } } } \end{array} \right) .
$$

The diagonal elements describe the free propagation of the carrier and of the sidebands,while the $X _ { 1 0 }$ and $X _ { 2 0 }$ term describe the fact that a round-trip of the carrier produces further contributions to the sidebands. Using eq.(9.108),the explicit expression of the matrix elements is

$$
\begin{array} { r l } & { X _ { 0 0 } = e ^ { 2 i \omega _ { \mathrm { L } } L / c } , } \\ & { X _ { 1 1 } = e ^ { 2 i ( \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } ) L / c } , } \\ & { X _ { 2 2 } = e ^ { 2 i ( \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } ) L / c } } \\ & { X _ { 1 0 } = i k _ { \mathrm { L } } L \operatorname { s i n c } \left( \omega _ { \mathrm { g w } } \underline { { L } } / c \right) e ^ { i \left( 2 \omega _ { \mathrm { L } } - \omega _ { \mathrm { g w } } \right) L / c } , } \\ & { X _ { 2 0 } = i k _ { \mathrm { L } } L \operatorname { s i n c } \left( \omega _ { \mathrm { g w } } \underline { { L } } / c \right) e ^ { i \left( 2 \omega _ { \mathrm { L } } + \omega _ { \mathrm { g w } } \right) L / c } . } \end{array}
$$

Fora Fabry-Perot cavity along the $y$ axis the same expressions hold, inverting the sign of $h _ { 0 }$ (see eq.(9.7)) or,equivalently,inverting the sign of $X _ { 1 0 }$ and of $X _ { 2 0 }$

This result allows us to generalize eq.(9.80) to the case when GWs are present, simply replacing the factors $e ^ { 2 i k _ { \perp } L }$ with the matrix $\mathbf { X }$ Thus, we can write the fields $\bar { \boldsymbol { B } } = \left( B _ { 0 } , B _ { 1 } , B _ { 2 } \right)$ inside the cavity,at $x = 0$ ,in matrix form as

$$
\begin{array} { r } { \boldsymbol { \mathcal { B } } = t _ { 1 } \boldsymbol { \mathcal { A } } _ { \mathrm { i n } } + r _ { 1 } r _ { 2 } \mathbf { X } \boldsymbol { \mathcal { B } } , } \end{array}
$$

where $\mathcal { A } _ { \mathrm { i n } } = \left( E _ { 0 } , 0 , 0 \right)$ .The solution is

$$
\begin{array} { r } { \beta = ( { \bf 1 } - r _ { 1 } r _ { 2 } { \bf X } ) ^ { - 1 } t _ { 1 } \mathcal { A } _ { \mathrm { i n } } . } \end{array}
$$

This is the right-moving field at the first mirror (the equivalent of what we denoted by $E _ { \tt c a v } ( 0 )$ in the absence of GWs,see Fig.9.6). The leftmoving field $E _ { \mathrm { c a v } } ^ { \prime } ( 0 )$ in Fig.9.6) in the absence of GWs is obtained from $E _ { \mathrm { c a v } } ( 0 )$ using eq. (9.79). In the presence of GWs,we have seen that the factor $e ^ { 2 i k _ { \tt L } L }$ is replaced by the matrix X,acting on the vector space of the amplitude of the carrier and of the sidebands,so the left-moving feld is now

$$
B ^ { \prime } = - r _ { 2 } { \bf X } B ,
$$

and the total reflected field,which includes also the promptly reflected part, is given by

$$
\begin{array} { r l } & { \mathcal { A } _ { \mathrm { r e f } } = r _ { 1 } \mathcal { A } _ { \mathrm { i n } } - t _ { 1 } r _ { 2 } \mathbf { X } \mathcal { B } } \\ & { \qquad = [ r _ { 1 } - r _ { 2 } ( 1 - p _ { 1 } ) \mathbf { X } ] ( \mathbf { 1 } - r _ { 1 } r _ { 2 } \mathbf { X } ) ^ { - 1 } \mathcal { A } _ { \mathrm { i n } } , } \end{array}
$$

which replaces eq. (9.70). Setting $\mathcal { A } _ { \mathrm { i n } } = ( 1 , 0 , 0 )$ ， we can now compute $A _ { \mathrm { { r e f l } } } \equiv \left( A _ { 0 } , A _ { 1 } , A _ { 2 } \right)$ .According to eq. (9.34),and taking into account

the factor ho/2 in the definition (9.104),the phase shift |△x| in a singl Fabry-Perot cavity along the x axis,is given by

$$
\frac { 1 } { 2 } | \Delta \phi _ { x } | = \frac { 1 } { 2 } h _ { 0 } \left| \frac { \mathcal { A } _ { 1 } } { \mathcal { A } _ { 0 } } \right| .
$$

We are interested in particular in the situation when the FP cavity i locked on resonance, so $e ^ { 2 i k _ { \mathrm { L } } L } | = 1$ In this case,with straightforan matrix algebra (easily performed with the help of any symbolic manip ulation program) we get

$$
\frac { \mathcal { A } _ { 1 } } { \mathcal { A } _ { 0 } } = X _ { 1 0 } e ^ { 2 i \omega _ { \mathrm { g w } } L / c } \frac { r _ { 2 } ( 1 - p ) - r _ { 1 } ^ { 2 } r _ { 2 } } { \left( e ^ { 2 i \omega _ { \mathrm { g w } } L / c } - r _ { 1 } r _ { 2 } \right) \left[ r _ { 2 } \left( 1 - p \right) - r _ { 1 } \right] } ,
$$

S0

$$
\begin{array} { r l r } {  { | \Delta \phi _ { x } | = h _ { 0 } k _ { L } L \operatorname { s i n c } ( \omega _ { \mathrm { g w } } L ) | c ) \frac { r _ { 2 } ( 1 - r _ { 1 } ^ { 2 } - p ) } { [ r _ { 2 } ( 1 - p ) - r _ { 1 } ] } \frac { 1 } { | e ^ { 2 i \omega _ { \mathrm { g w } } L / c } - r _ { 1 } r _ { 2 } | } } } \\ & { } & { = h _ { 0 } k _ { L } L \operatorname { s i n c } ( \omega _ { \mathrm { g w } } L ) \frac { r _ { 2 } ( 1 - r _ { 1 } ^ { 2 } - p ) } { [ r _ { 2 } ( 1 - p ) - r _ { 1 } ] } } \\ & { } & { \times \frac { 1 } { [ 1 + ( r _ { 1 } r _ { 2 } ) ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos ( 2 \omega _ { \mathrm { g w } } L / c ) ] ^ { 1 / 2 } } . } \end{array}
$$

If we set $p = 0$ and $r _ { 2 } ~ = ~ 1 1$ (e.g. the present value for VIRGO is $r _ { 2 } \simeq 0 . 9 9 9 9 5$ ）and we take $r _ { 1 }$ iclose to one,the first fraction becomes simply $1 + r _ { 1 } \simeq 2$ . So, we write

$$
\frac { r _ { 2 } ( 1 - r _ { 1 } ^ { 2 } - p ) } { \left[ r _ { 2 } ( 1 - p ) - r _ { 1 } \right] } = 2 [ 1 + \epsilon ( r _ { 1 } , r _ { 2 } , p ) ] ,
$$

where,in the typical experimental situation, $\epsilon ( r _ { 1 } , r _ { 2 } , p ) \ll 1$ Then

$$
\left| \Delta \phi _ { x } \right| = h _ { 0 } 2 k _ { L } L \left[ 1 + \epsilon ( r _ { 1 } , r _ { 2 } , p ) \right] \frac { \mathrm { s i n c } \left( \omega _ { \mathrm { g w } } L / c \right) } { \left[ 1 + ( r _ { 1 } r _ { 2 } ) ^ { 2 } - 2 r _ { 1 } r _ { 2 } \cos ( 2 \omega _ { \mathrm { g w } } L / c ) \right] ^ { 1 / 2 } } .
$$

The dependence on $\omega _ { \mathrm { g w } } L / c$ can be simplified observing that we want to have $\mathcal { F } L / c$ comparable to the wavelength of the GW, so $\mathcal { F } \omega _ { \mathrm { g w } } L / c =$ $O ( 1 )$ .However, we achieve thislby using a large value of $\mathcal { F }$ ,s0 $\omega _ { \mathrm { g w } } L / c \mathrm { i s }$ much smaller than one in the region where the interferometer operates. For instance, if $f _ { \mathrm { g w } } = 1 0 0 ~ \mathrm { H z }$ and $L = 4 ~ \mathrm { k m }$ ， $\omega _ { \mathrm { g w } } L / c \sim 1 0 ^ { - 2 }$ We can therefore replace sinc $( \omega _ { \mathrm { g w } } L / c ) | \simeq 1$ in the numerator,and we expand $\cos ( 2 \omega _ { \mathrm { g w } } L / c )$ in the denominator. Then we get

$$
\begin{array} { r l r } {  { | \Delta \phi _ { x } | \simeq h _ { 0 } 2 k _ { \mathrm { L } } L \frac { 1 + \epsilon ( r _ { 1 } , r _ { 2 } , p ) } { 1 - r _ { 1 } r _ { 2 } } \frac { 1 } { [ 1 + \frac { r _ { 1 } r _ { 2 } } { ( 1 - r _ { 1 } r _ { 2 } ) ^ { 2 } } ( 2 \omega _ { \mathrm { g w } } L / c ) ^ { 2 } ] ^ { 1 / 2 } } } } \\ & { } & { \simeq h _ { 0 } 2 k _ { \mathrm { L } } L \frac { \mathcal { F } } { \pi } \frac { 1 } { [ 1 + ( \dot { 4 } \pi f _ { \mathrm { g w } } \tau _ { s } ) ^ { 2 } ] ^ { 1 / 2 } } , \qquad ( 9 } \end{array}
$$

where,inthelastline,wewrotetheresultintermsofthefine $\mathcal { F }$ given in eq. (9.84),and of the storage time $\tau _ { s }$ of the cavity， given in eq. (9.87),and we neglected in the numerator terms that are small when

$r _ { 2 } , r _ { 1 }  1$ . The phase shift of a FP cavity along the $y$ arm is obtained changing the sign of $h _ { 0 }$ ，s0 $\Delta \phi _ { y } = - \Delta \phi _ { x }$ ，and the difference between them is $\Delta \phi _ { \mathrm { F P } } = \Delta \phi _ { x } - \Delta \phi _ { y } = 2 \Delta \phi _ { x }$

We rewrite the result introducing the so-called pole frequency,

$$
\overline { { f _ { p } \equiv \frac { 1 } { 4 \pi \tau _ { s } ^ { * } } } } ,
$$

or, from eq. (9.88),

$$
f _ { p } \simeq \frac { c } { 4 \mathcal { F } \mathit { k } } .
$$

For initial LIGO, $L = 4 ~ \mathrm { k m }$ and $\mathcal { F } \simeq \lvert 2 0 0$ this gives $f _ { p } \simeq 9 0 ~ \mathrm { H z }$ For VIRGO, $L = 3 ~ \mathrm { k m }$ and $\mathcal { F } \simeq 5 0$ s0 $f _ { p } \simeq 5 0 0 ~ \mathrm { H z }$ .The phase shift in a Fabry-Perot interferometer can then be written as

$$
\overline { { | \Delta \phi _ { \mathrm { F P } } | \simeq h _ { 0 } \frac { 4 \mathcal { F } } { \pi } k _ { \mathrm { L } } L \frac { 1 } { \sqrt { 1 + ( f _ { \mathrm { g w } } / f _ { p } ) ^ { 2 } } } } } .
$$

For $f _ { \mathrm { g w } } \ll f _ { p }$ we recover the result found in the proper detector frame, eq. (9.103)， as expected.17 At $f _ { \mathrm { g w } } \gg | f _ { p }$ ，eq. (9.123) shows that the sensitivity degrades linearly with $f _ { \mathrm { g w } }$ This formula holds as long as $\omega _ { \mathrm { g w } } L / c \ll 1$ ,i.e

$$
\begin{array} { l } { \displaystyle { f _ { \mathrm { g w } } \ll \frac { c } { 2 \pi L } } } \\ { \displaystyle { \simeq 1 2 \mathrm { k H z } \left( \frac { 4 \mathrm { k m } } { L } \right) . } } \end{array}
$$

Above this frequency thefactor sinc $( \omega _ { \mathrm { g w } } L / c )$ in eq. (9.119) can no longer be approximated by one,and cuts theresponse further,reflecting the fact that in each round-trip the GW changes sign.

In Fig.9.13 we show the function $1 / \ [ 1 + ( f _ { \mathrm { g w } } / f _ { p } ) ^ { 2 } ] ^ { 1 / 2 }$ , and we compare it with the function $| \mathrm { s i n c } \left( f / f _ { p } \right) |$ ,which is the corresponding quantity fora Michelson interferometer whbse length $L _ { \mathrm { M i c h } } = ( 2 / \pi ) \mathcal { F } L$ is chosen so that,in the limit $f _ { \mathrm { g w } }  0$ ,its response function is the same as a FP cavity of length $L$ and finesse $\mathcal { F }$ .

It is useful to write eq. (9.123) in the form

$$
\begin{array} { r } { \dot { \mathbf { \sigma } } } \\ { \vert \Delta \phi _ { \mathtt { F P } } \vert = h _ { 0 } T _ { \mathtt { F P } } ( f ) , } \end{array}
$$

where (writing $k _ { \mathrm { L } } = 2 \pi / \lambda _ { \mathrm { L } }$ ）

$$
\overline { { T _ { \mathrm { F P } } ( f ) \simeq \frac { 8 \mathcal { F } L } { \lambda _ { \mathrm { L } } } \frac { 1 } { \sqrt { 1 + ( f _ { \mathrm { g w } } / f _ { p } ) ^ { 2 } } } } } ,
$$

is the transfer function of an interferometer with Fabry-Perot cavities.

![](images/c908c74ac5efd8e6a047661c494aa6ffcc685b5dee055f6272bef9a7ba241ed0.jpg)  
Fig.9.13 A plot of the function $[ 1 + ( f / f _ { p } ) ^ { 2 } ] ^ { - \bar { 1 } / 2 }$ ,(solid line)，compared to the function $\left| \operatorname { s i n c } \left( f / f _ { p } \right) \right|$ (dashed line).We have taken $f _ { p } =$ $9 0 ~ \mathrm { H z }$

17Recall that eq. (9.91),and therefore eq.(9.103),were obtained in the limit $r _ { 2 } = 1$ , $p = 0$ and $\boldsymbol { r } _ { 1 }$ close to one.If we keep $\boldsymbol { r } _ { 1 }$ generic,still setting $r _ { 2 } = 1$ and $p = 0$ ,in eq.(9.91) the overall factor of 2 is replaced by $1 + r _ { 1 }$ and the same result is obtained from eq. (9.117).

# 9.2.3Angular sensitivity and pattern functions

Until now we have restricted burselves to a GW with plus polarization propagating along the $z$ axis. We now compute the response of an interferometer to GWs with arbitrary direction and polarization. A discussed in Section 7.2,this is encoded in the pattern functions $F _ { + } ( \theta , \phi )$ and $F _ { \times } ( \theta , \phi )$ .We first consider the limit $\omega _ { \mathrm { g w } } L / c \ll 1$ In this case we can use the proper detectpr frame,so the motion of the mirrors if governed by the geodesic equation,

$$
\ddot { \xi } ^ { i } = \frac { 1 } { 2 } \ddot { h } _ { i j } \xi ^ { j } .
$$

For the mirror located at $\xi ^ { j } = \left( L , 0 , 0 \right)$ , we are interested in its displace ment along the $x$ direction,which is given by

![](images/37564ff5057a7e17a7bbc8c1acfa259a0f399f0c9e2be61ae0662c592d16e81e.jpg)  
Fig.9.14 The geometry used in the computation of the pattern functions.The arms of the interferometer are along the $x$ and $y$ axes.

18When comparing with the calculation for resonant bars on page 425,observe that here we define $\theta$ as the angle from the $z$ axis,rather than from the $_ x$ axis.

$$
\ddot { \xi } _ { x } = \frac { 1 } { 2 } \ddot { h } _ { x x } L .
$$

This equation governs the change in the length of the $x$ -arm of a Michel son interferometer,as well as the change in the length of a FP cavity lying along the $x$ axis. For the mirror located at $\xi ^ { j } = ( 0 , L , 0 )$ ,we are rather interested in its displacement along the $y$ direction, which is given by

$$
\ddot { \xi } _ { y } = \frac { 1 } { 2 } \ddot { h } _ { y y } L .
$$

The relative phase shift between the $\mathscr { X }$ and $y$ arms is therefore driven by $( 1 / 2 ) ( \ddot { h } _ { x x } - \ddot { h } _ { y y } )$ .When the wave comes from the $z$ direction we have $h _ { x x } = h _ { + }$ and $h _ { x x } = - h _ { + }$ ，s0 $( 1 / 2 ) ( h _ { x x } - h _ { y y } ) = h _ { + }$ ，but in the most general situation we must replace $h _ { + }$ by $( 1 / 2 ) ( h _ { x x } - h _ { y y } )$ in the computations of the phase shift in a Michelson or in a FP interferometer performed in the previous sections. In other words,the detector tensor (defined in eq.(7.1)) for an interferometer with arms along the $\hat { \bf x }$ and y directions is

$$
D _ { i j } = \left| \frac { 1 } { 2 } ( \hat { \mathbf { x } } _ { i } \hat { \mathbf { x } } _ { j } - \hat { \mathbf { y } } _ { i } \hat { \mathbf { y } } _ { j } ) \right| .
$$

We compute $h _ { x x }$ and $h _ { y y }$ in terms of $h _ { + } , h _ { \times }$ for a wave coming from arbitrary direction. The computation is similar to that performed for resonant bars on page 425. THe geometry is illustrated in Fig.9.14: we have a frame $( x , y , z )$ such that the arms of the interferometer are along the $x$ and $y$ axes.We introduce a second reference frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ such that the propagation direction of the GW coincides with the $z ^ { \prime }$ axis. With respect to the $( x , y , z )$ frame, the $z ^ { \prime }$ axis has polar angles $\theta$ and $\phi$ , defined as in the figure.18

The polarizations $h _ { + }$ and $h _ { \times }$ are defined with respect to the $( x ^ { \prime } , y ^ { \prime } )$ axes, so in the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame the GW has the form

$$
h _ { i j } ^ { \prime } = \left( \begin{array} { c c c } { { h _ { + } } } & { { h _ { \times } } } & { { 0 } } \\ { { h _ { \times } } } & { { - h _ { + } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { i j } .
$$

The rotation that brings the $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ frame onto the $( x , y , z )$ frame is given by a rotation by an angle $\theta ^ { | }$ around the $y$ axis followed by a rotation by an angle $\phi$ around the $z$ axis,i.e.

$$
\mathcal { R } = \left( \begin{array} { c c c } { \cos \phi } & { \sin \phi } & { 0 } \\ { - \sin \phi } & { \cos \phi } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c c } { \cos \theta } & { 0 } & { \sin \theta } \\ { 0 } & { 1 } & { 0 } \\ { - \sin \theta } & { 0 } & { \cos \theta } \end{array} \right) .
$$

The GW in the $( x , y , z )$ frame is then given by the transformation law ofa tensor with two indices, $h _ { i j } = \mathcal { R } _ { i k } \mathcal { R } _ { j l } h _ { k l } ^ { \prime }$ .From this we obtain

$$
\begin{array} { r } { h _ { x x } = h _ { + } ( \cos ^ { 2 } \theta \cos ^ { 2 } \phi - \sin ^ { 2 } \phi ) + 2 h _ { \times } \cos \theta \sin \phi \cos \phi , } \\ { h _ { y y } = h _ { + } ( \cos ^ { 2 } \theta \sin ^ { 2 } \phi - \cos ^ { 2 } \phi ) - 2 h _ { \times } \cos \theta \sin \phi \cos \phi , } \end{array}
$$

$$
\frac { 1 } { 2 } ( h _ { x x } - h _ { y y } ) = \frac { 1 } { 2 } h _ { + } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi + h _ { \times } \cos \theta \sin 2 \phi ,
$$

and therefore

$$
\begin{array} { l } { { F _ { + } ( \theta , \phi ) = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \theta ) \cos 2 \phi \ : , } } \\ { { F _ { \times } ( \theta , \phi ) = \cos \theta \sin 2 \phi . } } \end{array}
$$

We see that GW interferometers have blind directions.For instance, for a GW with plus polarization,the direction with $\phi = \pi / 4$ is blind, since $F _ { + } = 0$ .This is due to the fact that this wave produces the same displacement in the $x$ and in the $y$ aim,so the differential phase shift vanishes. If we change the definition of the axes with respect to which the polarizations $h _ { + }$ and $h _ { \times }$ are defined,rotating them by an angle $\phi$ in the $( x ^ { \prime } , y ^ { \prime } )$ plane,the pattern functions transform as in eq. (7.30).

Equation (9.136) has been obtained in the limit $\omega _ { \mathrm { g w } } L / c \ll 1$ To compute the pattern functions for $\omega _ { \mathrm { g w } } L / c$ generic we must perform the computation in the TT gauge, so we should repeat the computation leading to eq. (9.15) for a GW coming from arbitrary direction. Consider the arm of a simple Michelson interferometers,with the beam splitter at $x = 0$ and the far mirror at $x = L _ { x }$ (or a FP cavity with mirrors at $x = 0$ and $x = L _ { x }$ ).Then eq.(9.9) is replaced by

$$
L _ { x } = c ( t _ { 1 } - t _ { 0 } ) - \frac { c } { 2 } \int _ { t _ { 0 } } ^ { t _ { 1 } } d t ^ { \prime } h _ { x x } ( t ^ { \prime } , { \bf x } ) .
$$

If we denote by $\hat { \bf n }$ the propagation direction of the GW,we have $h _ { x x } ( t ) =$ $h _ { \tt T C O S } [ \omega _ { \tt B W } ( t - \hat { { \bf n } } { \cdot } { \bf x } / c ) ]$ ， and we must evaluate $\mathbf { x }$ on the trajectory ${ \bf x } ( t )$ of the photon, so along the $\mathscr { X }$ arm we have

$$
h _ { x x } ( t ) = h _ { x x } \cos \left[ \omega _ { \mathrm { g w } } \left( t - \frac { n _ { x } x ( t ) } { c } \right) \right] ,
$$

which replaces eq. (9.6)．To lowest order in $h _ { x x }$ the trajectory of photon is just the unperturbed one,so inside the cosine we can s $x ( t ) = c ( t - t _ { 0 } )$ ，while $\hat { \bf n }$ can be written in terms of the angles $\theta , \phi$ 8 $\hat { \mathbf { n } } = ( \sin \theta \cos \phi , \sin \theta \sin \phi , \cos \theta )$ .Therefore,beside the dependence m $( \theta , \phi )$ in $h _ { x x }$ and $h _ { y y }$ ,that we already computed in eqs.(9.133) an (9.134),there is also an angular dependence through the term $n _ { x }$ eq.(9.138),and a similar term $\phi _ { y }$ for the $y$ arm. In particular,eq. (9.137 becomes

$$
\begin{array} { l } { { \displaystyle { \cal L } _ { x } = c ( t _ { 1 } - t _ { 0 } ) - \frac { c } { 2 } h _ { x x } \int _ { t _ { 0 } } ^ { t _ { 1 } } d t ^ { \prime } } } \\ { { \displaystyle ~ \times \cos \left[ ( 1 - \sin \theta \cos \phi ) \omega _ { \mathrm { g w } } t ^ { \prime } + \omega _ { \mathrm { g w } } t _ { 0 } \sin \theta \cos \phi \right] . } } \end{array}
$$

The return trip can be treated similarly, with the unperturbed photol trajectory given now by $\boldsymbol { x } ( t ) = \boldsymbol { L } - \boldsymbol { c } ( t - t _ { 1 } )$ , so eq. (9.11) is replaced h

$$
\begin{array} { l } { { \displaystyle L _ { x } = c ( t _ { 2 } - t _ { 1 } ) - \frac { c } { 2 } h _ { x x } \int _ { t _ { 1 } } ^ { t _ { 2 } } d t ^ { \prime } } \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } \left( 9 \right. }  \\ { { \displaystyle \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x } \times \left. \cos \left[ ( 1 + \sin \theta \cos \phi ) \omega _ { \mathrm { g w } } t ^ { \prime } - \omega _ { \mathrm { g w } } ( t _ { 1 } + L / c ) \sin \theta \cos \phi \right] \right. } \phantom { x x x x x x x x x x x x x x x x x x } } \end{array}
$$

Summing the two equations we get

$$
\begin{array} { c } { { t _ { 2 } = t _ { 0 } + \displaystyle \frac { 2 L _ { x } } { c } + \displaystyle \frac { 1 } { 2 } h _ { x x } \int _ { t _ { 0 } } ^ { t _ { 0 } + L _ { x } / c } d t ^ { \prime } \cos [ \omega _ { - } t ^ { \prime } + \phi _ { 0 } ] } } \\ { { + \displaystyle \frac { 1 } { 2 } h _ { x x } \int _ { t _ { 0 } + L _ { x } / c } ^ { t _ { 0 } + 2 L _ { x } / c } d t ^ { \prime } \cos [ \omega _ { + } t ^ { \prime } - \phi _ { 2 } ] , } } \end{array}
$$

where we introduced the short hand notation

$$
\begin{array} { r l } & { \omega _ { \pm } = \omega _ { \mathrm { g w } } \big ( 1 \pm \sin \theta \cos \phi \big ) , } \\ & { \phi _ { 0 } = \omega _ { \mathrm { g w } } t _ { 0 } \sin \theta \cos \phi , } \\ & { \phi _ { 2 } = \omega _ { \mathrm { g w } } t _ { 2 } \sin \theta \cos \phi , } \end{array}
$$

and in the limits of the integral,as well as in $\phi _ { 2 }$ , we can use $t _ { 1 } = t _ { 0 } + L _ { x } /$ and $t _ { 2 } = t _ { 0 } + 2 L _ { x } / c$ .For the $y$ arm we have similar expressions,witl $L _ { y }$ replacing $L _ { x }$ and $n _ { y } = \sin \theta \sin \phi$ replacing $n _ { x } = \sin \theta \cos \phi$

It is now in principle straightforward to perform the integrals and compute how $t _ { 2 } - t _ { 0 }$ depends on the propagation direction of the Gw Carrying out the integrals,however,we see that all terms which depend on $\theta , \phi$ are multiplied by the factor $\omega _ { \mathrm { g w } } L _ { x } / c$ .For instance, $\theta$ and $\phi$ enter in terms such as

$$
\operatorname { s i n c } \left[ { \frac { \omega _ { \mathrm { g w } } L _ { x } } { 2 c } } ( 1 \pm \sin \theta \cos \phi ) \right] .
$$

For a FP interferometer we saw that $\omega _ { \mathrm { g w } } L _ { x } / c$ is small, typically $O ( 1 0 ^ { - 2 } )$ in LIGO and VIRGO,and therefore the function sinc in eq. (9.145)i essentially unity,and its depehdence on $\theta$ and $\phi$ is negligible,at least as long as the condition (9.124) is satisfied.Then,we can neglect the dependence on the GW direction in the travel time $t _ { 2 } - t _ { 0 }$ and the only angular dependence comes from $h _ { x x }$ and $h _ { y y }$ ,as computed in eqs.(9.133) and (9.134)，so for the pattern function we can use，to a very good approximation,the expressions given in eq. (9.136).

# 9.3 Toward a real GW interferometer

In this section we discuss a numbet of issues that are more technical, but are important for understanding how a real interferometer works.

# 9.3.1Diffraction and Gaussian beams

Until now we have considered idealized FP cavities with mirrors of infnite transverse extent,so we could neglect any dependence of the electric feld on the transverse coordinates.For a cavity along the $x$ axis,we have then treated the interior electric field as a plane wave,with a dependence on $x , t$ of the form $\mathrm { e x p } \{ - i \omega _ { L } ( t \pm x / c ) \}$ ，and no dependence on the transverse coordinates $\mathbf { x } _ { \perp } \neq ( y , z )$ .Of course,in practice the mirrors have a finite extent,and the beam has a profile in the transverse direction.

Abeam of finite transverse extent is subject to diffraction.If,at some point in space,a photon of wavelength $\lambda _ { \mathrm { L } }$ (and therefore longitudinal momentum $p = \hbar / \chi _ { L }$ ）is localized within a transverse width $\Delta \mathbf { x } _ { \bot } =$ $a$ ,by the Heisenberg principle it has an uncertainty on the transverse momentum $\Delta p _ { \perp } \sim \hbar / a$ ,so the beam will widen,filling a cone of angle $\Delta \theta = \Delta p _ { \perp } / p \sim \pmb { \chi } _ { L } / a$ After traveling a longitudinal distance $\boldsymbol { \mathscr { X } }$ the beam has become larger,in the transverse direction,by $x \Delta \theta \sim x \dot { x } _ { L } / a$ As long as $x \mathrm { \lambda } _ { L } / a \ll a$ we are in the regime of Fresnel diffraction,and the broadening of the beam is negligible.When $x \ d \mathrm { x } _ { L } / a \gg a$ ,or,in terms of $k _ { L } = 1 / \mathfrak { X } _ { L }$ ，

$$
x \gg k _ { \mathrm { L } } a ^ { 2 } ,
$$

we are in the regime of Fraunhofer diffraction,and the beam has become much broader than its original size.For interferometers such as LIGO and VIRGO,the wavelcngth of the laser is typically

$$
\lambda _ { \mathrm { L } } \simeq 1 \mu m .
$$

The border between these regimes is at $a = ( x \Re ) ^ { 1 / 2 }$ which,for $x =$ $4 \mathrm { k m }$ and $\lambda _ { \mathrm { L } } = 1 \mu \mathrm { m }$ ，gives $a \simeq 2 . 5$ cm.This means that,for a laser beam whose initial width is smaller that $2 . 5 \mathrm { { c m } }$ ,the broadening of the beam becomes important already after a single one-way trip through the cavity. Furthermore for cavities with a finesse $O ( 1 0 0 )$ ,as we need for GW detection,the beam is supposed to perform $O ( 1 0 0 )$ round trips and,if the mirrors were flat,at each one-way trip the beam would widen further,as illustrated in Fig. 9.15,and would be finally dispersed on a region of transverse size larger than the mirrors.

Thus,it is clear that diffraction effects are important,and the naive scheme of a narrow beam (as typically obtained from a laser) bouncing between two flat mirrors cannot work.As a first step,we must understand in more detail the propagationbf a beam of finite transverse extent over large distances. The tool that we need is the paraxial propagator, that we introduce in the next subsection.

![](images/6c512131b2f28102aa2f92c8bf89a594ef7722ed9a3a3daff14c301ea42242b7.jpg)  
Fig.9.15 The widening of a beam due to diffraction as it bounces between two flat mirrors.

# The paraxial propagator

A given spatial component of the electric field, propagating in the vac uum,obeys the equation

$$
\left[ - \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + { \bf \nabla } \nabla ^ { 2 } \right] E ( t , { \bf x } ) = 0 .
$$

We take a single monochromatic component,which we write in complex notation as $\Breve { E ^ { \prime } } ( t , \mathbf { x } ) = E ( \mathbf { x } ) e ^ { - i \omega _ { \mathrm { L } } t }$ ，s0 $E ( \mathbf { x } )$ satisfies

$$
\begin{array} { r } { [ \nabla ^ { 2 } + k _ { \mathrm { L } } ^ { 2 } ] E ( \mathbf { x } ) = 0 . } \end{array}
$$

We want to compute the propagation across a long distance in the direction,so $x$ is the longitudinal coordinate and $\mathbf { x } _ { \perp } = ( y , z )$ are the transverse coordinate,and we search for solutions of the form

$$
E ( \mathbf { x } ) \equiv \mathcal { E } ( x ; y , z ) e ^ { i k _ { \mathrm { L } } x } ,
$$

where $\mathcal { E } ( x ; y , z )$ is a slowly varying function of $x$ ,in the sense that

$$
| \partial _ { x } \mathcal { E } | \ll k _ { \mathrm { L } } | \mathcal { E } | .
$$

Therefore $\begin{array} { r } { E ( t , \mathbf { x } ) = \mathcal { E } ( x ; y , z ) \exp \left\{ - i \omega _ { \mathrm { L } } t + i k _ { \mathrm { L } } x \right\} } \end{array}$ is in a first approxima tion a plane wave,with a slower dependence on $x$ ，which manifests itseli only on scales $x \gg \lambda _ { \mathrm { L } }$ .Plugging the ansatz(9.150) into eq.(9.149) we get

$$
\begin{array} { r } { \pmb { \nabla } _ { \perp } ^ { 2 } \mathcal { E } + 2 i k _ { \mathrm { L } } \partial _ { x } \mathcal { E } + \partial _ { x } ^ { 2 } \mathcal { E } = 0 , } \end{array}
$$

where $\pmb { \nabla } _ { \perp } ^ { 2 } = \partial _ { y } ^ { 2 } + \partial _ { z } ^ { 2 }$ .Because of the condition (9.151),we can neglect $\partial _ { x } ^ { 2 } \mathcal { E }$ with respect to $k _ { \mathrm { L } } \partial _ { x } \mathcal { E }$ ,so in this approximation we write

$$
\nabla _ { \perp } ^ { 2 } \mathcal { E } + 2 i k _ { \mathrm { L } } \partial _ { x } \mathcal { E } = 0 .
$$

We now perform the Fourier transform with respect to the transverse variables,

$$
\mathcal { E } ( x ; y , z ) = \int \frac { d p _ { y } } { 2 \pi } \frac { d p _ { z } } { 2 \pi } \tilde { \mathcal { E } } ( x ; p _ { y } , p _ { z } ) e ^ { i p _ { y } y + i p _ { z } z } .
$$

In terms of $\tilde { \mathcal { E } } ( x ; p _ { y } , p _ { z } )$ ,eq.(9153) reads

$$
\begin{array} { r } { - ( p _ { y } ^ { 2 } + p _ { z } ^ { 2 } ) \tilde { \mathcal { E } } ( x ; p _ { y } , p _ { z } ) + 2 i k _ { \mathrm { L } } \partial _ { x } \tilde { \mathcal { E } } ( x ; p _ { y } , p _ { z } ) = 0 . } \end{array}
$$

The $x$ dependence can be integrated,and we get

$$
\tilde { \mathcal { E } } ( x ; p _ { y } , p _ { z } ) = \tilde { \mathcal { E } } ( x = 0 ; p _ { y } , p _ { z } ) \exp \left\{ - i \frac { p _ { y } ^ { 2 } + p _ { z } ^ { 2 } } { 2 k _ { \mathrm { L } } } x \right\} .
$$

Then eq.(9.154) becomes

$$
\mathcal { E } ( x ; y , z ) = \int \frac { d p _ { y } } { 2 \pi } \frac { d p _ { z } } { 2 \pi } \tilde { \mathcal { E } } ( x = 0 ; p _ { y } , p _ { z } ) e ^ { i p _ { y } y + i p _ { z } z - i \frac { p _ { y } ^ { 2 } + p _ { z } ^ { 2 } } { 2 k _ { \mathrm { L } } } x }
$$

$$
\begin{array} { l } { { \displaystyle = \int \frac { d p _ { y } } { 2 \pi } \frac { d p _ { z } } { 2 \pi } \left[ \int d y ^ { \prime } d z ^ { \prime } \tilde { \varepsilon } ( x = 0 ; y ^ { \prime } , z ^ { \prime } ) e ^ { - i p _ { y } y ^ { \prime } + i p _ { z } z ^ { \prime } } \right] } } \\ { { \displaystyle \quad \times e ^ { i p _ { y } y + i p _ { z } z - i \frac { p _ { y } ^ { 2 } + p _ { z } ^ { 2 } } { 2 k _ { \perp } } x } } } \\ { { \displaystyle = \int d y ^ { \prime } d z ^ { \prime } \tilde { \varepsilon } ( x = 0 ; y ^ { \prime } , z ^ { \prime } ) } } \\ { { \displaystyle \quad \times \int \frac { d p _ { y } } { 2 \pi } \frac { d p _ { z } } { 2 \pi } e ^ { i p _ { y } ( y - y ^ { \prime } ) + i p _ { z } ( z - z ^ { \prime } ) - i \frac { p _ { y } ^ { 2 } + p _ { z } ^ { 2 } } { 2 k _ { \perp } } x } } } .  \end{array}
$$

The integrals over $d p _ { y }$ and $d p _ { z }$ are Fresnel integrals,that we already met in eq. (4.365),so we finally get

$$
\mathcal { E } ( x ; y , z ) = \int d y ^ { \prime } d z ^ { \prime } G ( x ; y - y ^ { \prime } , z - z ^ { \prime } ) \tilde { \mathcal { E } } ( x = 0 ; y ^ { \prime } , z ^ { \prime } ) ,
$$

where

$$
G ( x ; y - y ^ { \prime } , z - z ^ { \prime } ) = { \frac { - i k _ { \mathrm { L } } } { 2 \pi x } } \exp \biggl \{ i { \frac { k _ { \mathrm { L } } } { 2 x } } \left[ ( y - y ^ { \prime } ) ^ { 2 } + ( z - z ^ { \prime } ) ^ { 2 } \right] \biggr \}
$$

is called the paraxial propagator. Equations (9.158) and (9.159) allow us to compute the field at $\boldsymbol { x }$ generic,once we have its value on a transverse surface $x = 0$

# Fraunhofer diffraction

As a first application，we consider a|plane wave of infinite transverse extent that arrives on an aperture $\boldsymbol { \mathrm { \Sigma } }$ on a plane opaque screen and we compute the image on another screen at a large distance $\boldsymbol { \mathscr { x } }$ ，and at transverse coordinates $( y , z )$ ,seeFig.9.16.Then，at $x \ = \ 0$ we have $\tilde { \mathcal { E } } ( x = 0 ; y ^ { \prime } , z ^ { \prime } ) = \tilde { \mathcal { E } } _ { 0 }$ if $( y ^ { \prime } , z ^ { \prime } )$ are inside the aperture $S$ and zero otherwise, so

$$
\begin{array} { l } { { \displaystyle { E ( x , y , z ) = \frac { - i k _ { \mathrm { L } } } { 2 \pi x } \ \tilde { \mathcal { E } _ { 0 } } e ^ { i k _ { \mathrm { L } } x } \int _ { S } d y ^ { \prime } d z ^ { \prime } \exp \left\{ i \frac { k _ { \mathrm { L } } } { 2 x } [ ( y - y ^ { \prime } ) ^ { 2 } + ( z - z ^ { \prime } ) ^ { 2 } ] \right\} } } } \\ { { \displaystyle { \vphantom { \frac { - i k _ { \mathrm { L } } } { 2 \pi x } \tilde { \mathcal { E } _ { 0 } } \exp \left\{ i k _ { \mathrm { L } } \left[ x + \frac { y ^ { 2 } + z ^ { 2 } } { 2 x } \right] \right\} } } } } \\  { \displaystyle { \phantom { \frac { - i k _ { \mathrm { L } } } { 2 \pi x } \ \tilde { \mathcal { E } _ { 0 } } e ^ { i k _ { \mathrm { L } } x } \int _ { S } d y ^ { \prime } d z ^ { \prime } \exp \left\{ - i \frac { k _ { \mathrm { L } } } { x } ( y y ^ { \prime } + z z ^ { \prime } ) + i \frac { k _ { \mathrm { L } } } { x } [ { y ^ { \prime } } ^ { 2 } + z ^ { \prime } { } ^ { 2 } ) \right\} . } } } \end{array}
$$

Fraunhofer diffraction is defined by the condition (9.146),where a is the sizeof the aperture. In this limit,we can neglect the term $k _ { \mathrm { L } } ( { y ^ { \prime } } ^ { 2 } + { z ^ { \prime } } ^ { 2 } ) / x$ in the exponential. Furthermore we observe that,if $y ^ { 2 } + z ^ { 2 } \ll x ^ { 2 }$ ，the term $x + ( y ^ { 2 } + z ^ { 2 } ) / 2 x$ in the first exponential is just the first-order expansion of the distance $r = ( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 }$ from the observatio point to the center of the aperture,since

![](images/ff8929e707bc285acfedf1951326e56174a727dd15b2df5c7fff0c67eeea835c.jpg)  
Fig.9.16 An aperture $S$ ona opaque screen. The plane of the opaque screen is parametrized by coordinates $( y ^ { \prime } , z ^ { \prime } )$ The image is observed on a screen at a distance $x$ ， parametrized by coordinates $( y , z )$

$$
\left( x ^ { 2 } + y ^ { 2 } + z ^ { 2 } \right) ^ { 1 / 2 } = x \left( 1 + \frac { y ^ { 2 } + z ^ { 2 } } { x ^ { 2 } } \right) ^ { 1 / 2 }
$$

Similarly, to lowest order we can replace $1 / x$ with $1 / r$ in eq. (9.160) Then we get the well-known formula for the Fraunhofer diffraction b an aperture,

$$
E ( x , y , z ) = \frac { - i \tilde { \mathcal { E } } _ { 0 } k _ { \mathrm { L } } } { 2 \pi } \frac { e ^ { i k _ { \mathrm { L } } r } } { r } \int _ { S } d y ^ { \prime } d z ^ { \prime } e ^ { - i k _ { \mathrm { L } } ( y y ^ { \prime } + z z ^ { \prime } ) / r } .
$$

Consider for example a circular aperture of radius $a _ { \scriptscriptstyle }$ .In this case the inte gral can be performed exactly in terms of the Bessel function $J _ { 1 }$ Writing $y = \rho \cos \varphi , z = \rho \sin \varphi$ ,and sirhilarly $y ^ { \prime } = \rho ^ { \prime } \cos \varphi ^ { \prime } , z ^ { \prime } = \rho ^ { \prime } \sin \varphi ^ { \prime }$ we get

19This result was first derived by Airy in the 19th century,and this intensity distribution is known as the Airy pattern. L

![](images/2f3be87ea8de8b869465d5df659fc6e28ffdc3bb3d004b63e9a83a4aaefd6940.jpg)  
Fig.9.17 The function $2 J _ { 1 } ( x ) / x$

$$
\begin{array} { l } { { \displaystyle \int _ { S } d y ^ { \prime } d z ^ { \prime } e ^ { - i k _ { \mathrm { L } } ( y y ^ { \prime } + z z ^ { \prime } ) / r } = \displaystyle \int _ { 0 } ^ { a } \rho ^ { \prime } d \rho ^ { \prime } \int _ { 0 } ^ { 2 \pi } d \varphi ^ { \prime } e ^ { - i ( k _ { \mathrm { L } } / r ) \rho \rho ^ { \prime } \cos ( \varphi - \varphi ^ { \prime } ) } } } \\ { { \displaystyle \qquad = \displaystyle 2 \pi \int _ { 0 } ^ { a } \rho ^ { \prime } d \rho ^ { \prime } J _ { 0 } ( k _ { \mathrm { L } } \rho \rho ^ { \prime } / r ) } } \\ { { \displaystyle \qquad = \displaystyle \frac { 2 \pi a r } { k _ { \mathrm { L } } \rho } J _ { 1 } ( k _ { \mathrm { L } } \rho a / r ) \cdot \qquad ( 9 . 1 \qquad \quad } } \end{array}
$$

Writing $\rho / r = \sin \theta$ and recalling that $\mathrm { l i m } _ { u \longrightarrow 0 } J _ { 1 } ( u ) / u = 1 / 2$ ，we see that the intensity of light,which is proportional to the squared modulus of the electric field,is distributed in the scattering angle $\theta ~ \mathrm { { a . s ^ { 1 9 } } }$

$$
I ( \theta ) = I ( 0 ) \left[ \frac { 2 J _ { 1 } ( k _ { \mathrm { L } } a \sin \theta ) } { k _ { \mathrm { L } } a \sin \theta } \right] ^ { 2 } ,
$$

A plot of the function $2 J _ { 1 } ( x ) / { x }$ is shown in Fig. 9.17. $I ( \theta )$ has its first zero at $k _ { \mathrm { L } } a \sin \theta \simeq 3 . 8$ .Taking this as an estimate of the angular width $\Delta \theta$ of the beam we get (for $\smash { \dot { \lambda } \ll a }$ ） $\Delta \theta \simeq 3 . 8 \dot { \lambda } / a$ ，which is consistent with the uncertainty principle bound,but does not saturate it.

# Propagation of Gaussian beams

Consider now a beam that，at $x = 0$ ，has a Gaussian profile in the transverse direction,

$$
\begin{array} { r } { \mathcal { E } ( x = 0 ; y , z ) = \mathcal { E } _ { 0 } e ^ { - ( y ^ { 2 } + z ^ { 2 } ) / w _ { 0 } ^ { 2 } } . } \end{array}
$$

Its profile at $x$ generic can be computed by inserting this initial value into eqs.(9.158) and (9.159). The resulting integrals can be computed exactly,without resorting to the Fraunhofer approximation,using

$$
\int _ { - \infty } ^ { \infty } e ^ { - ( 1 + i a ^ { 2 } ) y ^ { 2 } } = \frac { \sqrt { \pi } } { ( 1 + a ^ { 2 } ) ^ { 1 / 4 } } \exp \left\{ - \frac { i } { 2 } \arctan a \right\} ,
$$

where $a$ is a real constant.The result, written in terms of $E ( x , y , z ) =$ $e ^ { i k _ { \mathrm { L } } x } \mathcal { E } ( x ; y , z )$ ,is

$$
\begin{array} { l }  \displaystyle { E ( x , y , z ) = \frac { \mathcal { E } _ { 0 } } { \sqrt { 1 + x ^ { 2 } / b ^ { 2 } } } e ^ { - { ( y ^ { 2 } + z ^ { 2 } ) } / { w ^ { 2 } ( x ) } } } \\ { \displaystyle { \phantom { \frac { 1 } { 1 } } \times \exp \left\{ i k _ { \mathrm { L } } \left[ x + \frac { y ^ { 2 } + z ^ { 2 } } { 2 R ( x ) } \right] - i \arctan ( x / b ) \right\} , } } \end{array}
$$

where the Rayleigh range $b$ is defined by

$$
b = { \frac { 1 } { 2 } } k _ { \mathrm { L } } \omega _ { 0 } ^ { 2 } ,
$$

the width $w ( x )$ is given by

$$
w ( x ) = w _ { 0 } \sqrt { 1 + { x ^ { 2 } } / { b ^ { 2 } } } ,
$$

and the curvature radius $R ( x )$ is

$$
R ( x ) = x + { \frac { b ^ { 2 } } { x } } .
$$

This shows that a beam which at $x = 0$ has a Gaussian profile, remains Gaussian at all $\boldsymbol { x }$ ，witha $x$ -dependent width given by eq. (9.169). Observe that, since $w _ { 0 }$ is the initial tran\$verse size, $b$ given in eq. (9.168) is the parameter that separates the Fresnel regime (at $x \ll b$ ）from the Fraunhofer regime (at $x \gg b$ ),compare with eq.(9.146). In agreement with the discussion above eq. (9.146),at $| x | \ll b$ we find that there is no appreciable widening of the beam,while at $| x | \gg b$ the width increases linearly, $w ( x ) \simeq w _ { 0 } | x | / b$ ,as demanded by the uncertainty principle.Using the definition (9.i68) of the Rayleigh range $b$ ，we get

$$
w ( x ) \simeq \frac { | x | \lambda _ { \mathrm { L } } } { \pi w _ { 0 } } , \qquad ( | x | \gg b ) .
$$

Actually Gaussian beams saturate thq uncertainty principle, i.e. they have the minimum possible spreading.

The term arctan $( x / b )$ in eq. (9.167)lis called the Gouy phase,and is an extra phase factor compared to tlie plane wave propagation. The surfaces of constant phase are obtained requiring that

$$
k _ { \mathrm { L } } \left[ x + \frac { y ^ { 2 } + z ^ { 2 } } { 2 R ( x ) } \right] + \arctan ( x / b )
$$

be constant.For a typical GW interferometer, with $\lambda _ { \mathrm { L } } = 1 \mu \mathrm { m }$ and $w _ { 0 }$ of order of a few cm, $b$ is of order of several hundred meters. Thus, if we want to compute the surfaces of constant phase in a region close to a point on the optical axis,i.e. ina region with coordinates $( x =$ $x _ { 0 } + \delta x , y = \delta y , z = \delta z )$ ，with $\delta x , \delta y , \delta z$ of the order of a few $\mathrm { c m }$ ,we can neglect the variation of $R ( x )$ and of the Gouy phase, so at a given $x _ { 0 }$ we simply have the condition

![](images/0ffc00482772ad4881ec937ca1296a1d6306b13cba29e4e170b1b0dfbef1ab8d.jpg)  
Fig.9.18 A surface of constant intensity of the Gaussian beam (solid line) and surfaces of constant phase (dashed lines).

20The solution (9.167) holds also at $ { \boldsymbol { { x } } } \ < \ 0$ ；in this case both the term $k _ { \mathrm { L } } \boldsymbol { x }$ and $R ( x )$ in the exponential change sign,and the radius of curvature is as shown in the figure.

![](images/2f9e7ceace4e43a416718575736492b36f96a2b638cc91d08ad7752ccc176f22.jpg)  
Fig. 9.19 A wavefront (dashed lines） that propagates toward a spherical mirror is reflected back and focused toward the waist.After passing the waist it expands again toward the other mirror.

![](images/26b26e1e7326b77921f36a8e3d2512945756671be87e7324e80c2e020e15131d.jpg)  
Fig.9.20 The scheme of an interferometer with Fabry-Perot cavities, with Gaussian beams and spherical mirrors.

$$
\delta x + \frac { \delta y ^ { 2 } + \delta z ^ { 2 } } { 2 R ( x _ { 0 } ) } = \mathrm { c o n s t a n t } .
$$

This equation describes a portionlof spherical surface with radius $R ( x _ { 0 } )$ as we can check immediately by expanding the equation $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = R ^ { 2 }$ around $x \ = \ R + \delta x , y \ = \ \delta y , z \ = \ \delta z$ Therefore the wavefronts of a Gaussian beam are spherical to an excellent approximation (as long as the transverse distances are much smaller than $b = \ O ( 1 0 ^ { 2 } ) \ \mathrm { m } )$ ,and $R ( x )$ is their curvature radius. The shape of the beam is therefore as shown in Fig. 9.18.20 The characteristic length $w _ { 0 }$ ， which determines the transverse size at $x = 0$ ,is called the waist of the beam.

When the beam bounces many times between two mirrors,we want to avoid that at each trip it widens further,as in Fig.9.15. This can be obtained shaping the mirrors so that their surfaces match exactly surfaces of constant phase of the beam. For Gaussian beams we have seen that the wavefronts are spherical, so we must use spherical mirrors. When the expanding wavefront of a Gaussian beam reaches a spherical mirror located at a position $x _ { 0 }$ and with radius of curvature $R ( x _ { 0 } )$ ,its direction of propagation is reversed,and the beam is focused back and converges toward the waist at $x = \mid 0$ ,before re-expanding again for $x < 0$ If we have another spherical mirror at $x = - x _ { 0 }$ the beam bounces back and forth between them,and at each reflection its wavefronts are forced to converge back toward the waist,as shown in Fig. 9.19,so the beam does not increment its transverse size at each bounce.

Gaussian beams have two advantages over other shapes. First, thev have the minimum spreading compatible with the uncertainty principle. Second, their wavefronts are spherical,and mirrors with a spherical shape are easy to manufacture. For these reasons, they are the choice used in present GW interferometers. Thus,we can replace the scheme given in Fig. 9.12 with the more realistic scheme of Fig. 9.20. Alternatively, rather than using two spherical mirrors with the waist in the middle of the cavity, we can put a flat mirror in the position of the waist and,at a distance $L$ ,a spherical mirror with curvature radius $R = L + b ^ { 2 } / L$ .Presently, the former option is used in LIGO and the latter in VIRGO.With the waist of the beam chosen in the middle of the cavity, the value of $w ( x )$ at the position of the mirrors $x = \pm L / 2$ is given by

$$
w ^ { 2 } ( \pm L / 2 ) \biggl | = w _ { 0 } ^ { 2 } + { \frac { \not { x } _ { L } ^ { 2 } L ^ { 2 } } { w _ { 0 } ^ { 2 } } } .
$$

In order to be able to use mirrors of manageable size, we want to have $w ( \pm L / 2 )$ small.Minimizing eq.(9.173） with respect to $w _ { 0 }$ we find the optimal value of the waist,

$$
w _ { 0 } ^ { \mathrm { o p t i m a l } } | = ( \Upsilon _ { L } L ) ^ { 1 / 2 } .
$$

For arms of length $L = 4 ~ \mathrm { k m }$ and a wavelength of the laser light $\lambda _ { \mathrm { L } } \simeq$ $1 . 0 \mu \mathrm { m }$ this gives $w _ { 0 } \simeq 2 . 5 \ \mathrm { c m }$ ,to which corresponds a value $w ( L / 2 ) =$ $( 2 \Sigma \Sigma , L ) ^ { 1 / 2 } \simeq 3 . 6$ cm.A suitable mirror radius for such a beam can therefore be $O ( 1 0 )$ cm.21 Observe that, since the waist $w _ { 0 }$ is much larger than the wavelength $\star _ { L }$ ,the paraxial approximation that we have used is well justified.

The Gaussian beams that we have considered are by definition solutions of the paraxial evolution equation (9.153),since we obtained them evolving an initial condition on the surface $x = 0$ with the paraxial propagator. Of course,we can also verify this by direct substitution in the equation.Actually,the Gaussian beam is just one of many possible solutions.As can be checked by direct substitution into eq.(9.153),there is a complete orthonormal set of solutions called the Hermite-Gauss modes, given by

$$
\begin{array} { r } { u _ { m n } ( x , y , z ) = \displaystyle \frac { c _ { m n } } { \sqrt { 1 + x ^ { 2 } / b ^ { 2 } } } e ^ { - ( y ^ { 2 } + z ^ { 2 } ) \left/ w ^ { 2 } ( x ) \right. } H _ { m } \left( \frac { y \sqrt { 2 } } { w ( x ) } \right) H _ { n } \left( \frac { z \sqrt { 2 } } { w ( x ) } \right) } \\ { \times \exp \left\{ i k _ { \mathrm { L } } \left[ x + \frac { y ^ { 2 } + z ^ { 2 } } { 2 R ( x ) } \right] - i ( m + n + 1 ) \arctan ( x / b ) \right\} , } \end{array}
$$

where $c _ { m n }$ are normalization constants and $H _ { n } ( \xi )$ are the Hermite polynomials, defined by

$$
H _ { n } ( \xi ) = e ^ { \xi ^ { 2 } } \left( - \frac { d } { d \xi } \right) ^ { n } e ^ { - \xi ^ { 2 } } .
$$

In particular, $H _ { 0 } ( \xi ) = 1$ ， $H _ { 1 } ( \xi ) = 2 \xi$ and $H _ { 2 } ( \xi ) = 4 \xi ^ { 2 } - 2$ For these modes,both the electric and magnetic fields are transverse to the propagation direction, just as plane wave inl free space,so they are also denoted as $\mathrm { T E M } _ { m n }$ modes.Comparing with eq.(9.167) we see that the Gaussian beam is just the mode $\mathrm { T E M _ { 0 0 } }$ .In Figs.9.21-9.23 we show the intensity uml² of the modes TEMo0，TEMo1and TEM11.Alternativelyone can use as a basis the so-called Laguerre-Gauss modes $\mathrm { L G } _ { m n }$ ,which are written in terms of Laguerre polynomials.The fundamental mode $\mathrm { L G } _ { 0 0 }$ is again the Gaussian beam.

Since the Gouy phase for the mode $\mathrm { T E M } _ { m n }$ is $( m + n + 1 ) \arctan ( x / b )$ see eq.(9.175),the resonance condition in a FP cavity depends on $( m , n )$ The laser emits predominantly in the $\mathrm { T E M _ { 0 0 } }$ mode,with a contamination typically less than 1O% from higher modes (mostly TEMo1 and $\mathrm { \ T E M _ { 1 0 } }$ .To eliminate these residualhigher modes,which would not be resonant and would just produce ndise，before sending it to the beam splitter the laser beam is sent into a Fabry-Perot cavity operated in transmission，called the mode-cleaner.Since the Gouy phase for the mode $\mathrm { T E M } _ { m n }$ depends on $( m , n )$ ,wecan choose the length of the mode cleaner so that only the $( 0 , 0 )$ mode is in resonance and is efficiently transmitted.

$^ { 2 1 } \mathrm { A }$ smallspot allows usto keepdown the mirror size.However,it also results in large intensity gradients,in region of high intensity of the electromagnetic field,inducing thermal deformations of the mirrors that must be compensated.An alternative possibility,that has been studied for advanced interferormeters,is the use of so-called “mesa beams”,i.e.beams witha fat profile,which average more effectively over these thermoelastic fluctuations, see Bondarescu and Thorne (2006).

![](images/ee626a3a907d447e5bc717592c324e5426d7385d48c9d9973050926ef425537a.jpg)

![](images/b7d49d6fc3468fbba544119378cb0868bbb34adc5440ba98ce34ebb5767897d9.jpg)  
Fig.9.21 The intensity of the mode $\mathrm { T E M _ { 0 0 } }$ as a function of the transverse variables $( y , z )$ ，atagiven $\mathcal { X }$ (in units such that $w ( x ) = \sqrt { 2 } ,$ .

![](images/ef2a8632d14c2821daa101c92839fce468811f76871cc4f455ce33ce63433cd2.jpg)  
Fig.9.22 The same as Fig.9.21, for the mode $\mathrm { T E M _ { 0 1 } }$   
Fig. 9.23 The same as Fig.9.21,for the mode $\mathrm { T E M _ { 1 1 } }$

# 9.3.2Detection at the dark fringe

![](images/3fbd303243dfb6eedaf0891e1a44643f7c14ba3e1293947e904248087699d494.jpg)  
Fig.9.24 The power $P ( \phi ) / P _ { 0 }$ The naive working point is marked as 1, and the dark fringe as 2.

# Michelson interferometer

We have seen that the passage of a GW in an interferometer, whethe of the simple Michelson type or with Fabry-Perot cavities in the arms produces a phase shift $\Delta \phi _ { \mathrm { g w } } ( t )$ .We now ask how to extract this phas from the output of the detector.The issue,as we will discuss in ti section,is quite non-trivial. The origin of the problem can be seen a follows.We consider first for simplicity a Michelson interferometer. saw in eq.(9.32) that the power atits output is given by $P ( \phi ) = P _ { 0 } \sin ^ { 2 }$ where $\phi = \phi _ { 0 } + \Delta \phi _ { \mathrm { g w } } ( t )$ and $\phi { \big \vert }$ is a phase that can be adjusted a will by the experimenter.A plot of $P ( \phi ) / P _ { 0 }$ is shown in Fig.9.24 Naively,one might think from this figure that the best working point fol the interferometer is at $\phi _ { 0 } = \pi / 4$ since there the derivative $\partial P / \partial \phi _ { 0 }$ is maximum,and the sensitivity to asmall displacement Φo → Φo+△Φgw( due to the passage of a GW is highest. Unfortunately,such a strategy would be doomed to failure.In fact,at this working point we are also very sensitive to fluctuations in the power $P _ { 0 }$ of the laser.Since that we measure is the power $P \vert = \ \bar { P } _ { 0 } \sin ^ { 2 } \phi$ at the photodetector,it is impossible to tell whether a given variation in the measured power is due a variation $\phi _ { 0 } \to \phi _ { 0 } + \Delta \phi _ { \mathrm { g w } } ( t )$ induced by the passage of GW,or to a variation $P _ { 0 }  P _ { 0 } + \Delta P _ { 0 } ( t )$ due to a fuctuation in the laser power. In particular,a GW with frequency $f _ { \mathrm { g w } } = O ( 1 0 ^ { 2 } – 1 0 ^ { 3 } )$ Hz induces variations in the power $\dot { \boldsymbol { \mathrm { I } } }$ with a frequency $f = 2 f _ { \mathrm { g w } }$ ,which therefore must be compared with the power fuctuations of the laser in the same frequency range.With present lasers,the latter turns out to be much larger than the signal that we expect from GWs.

From a more general point of view,whenever we are looking for very small effects a sound experimental strategy is to build a null instrument that is an instrument that,when the signal is absent,records a zero output.This makes the instrument insensitive to calibration uncertainties that would otherwise overwhelm the tiny signal that we are searching. A prototype of a null instrument is the Dicke radiometer that we discussed in Note 74 on page 412. At the naive operation point marked as 1in Fig.9.24,the interferometer is not a null instrument.Even in the absence of a GW,the photodetector measures a large power. In this state. small variations in the power due to GWs should be read against this large DC contribution,and would be overwhelmed by its fuctuations.

This suggests that the best working point should be the dark fringe. marked as the point 2 in Fig.9.24. There the output in the absence ol GWs is zero,and we are insensitive to fuctuations in the laser power. Unfortunately,at the dark fringe not only $P = 0$ ,but even $\partial P / \partial \phi = 0 .$ Since $\Delta \phi _ { \mathrm { g w } } = O ( h )$ ,this means that at the dark fringe the change in the output power induced by GWs is $\Delta P = O ( h ^ { 2 } )$ .Given that we expect GWs with amplitude $h$ at most $O ( 1 0 ^ { - 2 1 } )$ , an effect quadratic in $h$ is $0 . \dot { 1 }$ course invisible.So,apparently the choice is between operation points where the response of the interferometer is linear in $h$ but we have a large DC contribution whose fluctuations overwhelm the signal,and an operation point where we have no DG contribution,but no sensitivity to GWs either.

There is however a very elegant way out of this dilemma.The idea is to apply a phase modulation to the input laser light.22 This can be obtained by passing the incident beam through a Pockels cell,which is a crystal or a block of dielectric material whose index of refraction depends on an applied electric field, $| E _ { \mathrm { a p p l } } = \ : | E _ { \mathrm { a p p l } } | \cos \Omega _ { \mathrm { m o d } } t$ The speed of the response that can be obtained with appropriate materials is quite high,and the index of refraction oscillates with the frequency fmod = Ωmod/(2π),for values of fmod up to tens of MHz. Passing through a material with a time-varying index of refraction,the laser beam acquires a time-varying phase,so the beam which reaches the beam-splitter has the form

$$
E _ { \mathrm { i n } } = E _ { 0 } e ^ { - i \left( \omega _ { \mathrm { L } } t + \Gamma \sin { \Omega _ { \mathrm { m o d } } t } \right) } ,
$$

where $\Gamma$ is called the modulation index,or the modulation depth.This expression can be expanded in Fourier modes as

22 Another possible solution would be to control so well the laser fluctuations,that a detection scheme of the type discussed above becomes possible (typically at a working point which is slightly displaced from the dark fringe). This solution is under investigation for Advanced LIGO.

$$
E _ { \mathrm { i n } } = E _ { 0 } [ J _ { 0 } ( \Gamma ) e ^ { - i \omega _ { \mathrm { L } } t } + J _ { 1 } ( \Gamma ) e ^ { - i ( \omega _ { \mathrm { L } } + \Omega _ { \mathrm { f m o d } } ) t } - J _ { 1 } ( \Gamma ) e ^ { - i ( \omega _ { \mathrm { L } } - \Omega _ { \mathrm { m o d } } ) t } + . . . ] ,
$$

where $J _ { n }$ are Bessel functions and the dots denote terms with frequencies wL ± nΩmod，with n = 2,3,... For Γ < 1 this expression can be simplified using $J _ { 0 } ( \Gamma ) \simeq 1 - ( \Gamma ^ { 2 } / 4 )$ and $J _ { 1 } ( \Gamma ) \simeq \Gamma / 2$ .(In the limit $\Gamma \ll 1$ this expansion is obtained more simply expanding directly eq. (9.177) in powers of Γ). Therefore, the effect of the phase modulation is to generate sidebands.23 For small $\Gamma$ ,higher sidebands are suppressed by higher powers of Γ,so we will limit olrselves to the carrier,which has frequency $\omega _ { \mathrm { L } }$ and wavenumber $k _ { \mathrm { L } } = \omega _ { \Sigma } ^ { \mathrm { d } } / c$ ,and to the first two sidebands, with frequencies

$$
\omega _ { \pm } = \omega _ { \mathrm { L } } \pm \frac { \ d } { \Omega _ { \mathrm { m o d } } } ,
$$

and wavenumbers

$$
k _ { \pm } = \frac { \omega _ { \pm } } { c } = 2 \pi \left( \frac { 1 } { \lambda _ { \mathrm { L } } } \pm \frac { 1 } { \lambda _ { \mathrm { m o d } } } \right) .
$$

Consider now what happens to the garrier and to the sidebands in a Michelson interferometer with arms of length $L _ { x }$ and $L _ { y }$ .For the carrier the incoming electric field hasamplitude $E _ { 0 } J _ { 0 } ( \Gamma )$ so,from the discussion in Section 9.1,the electric field at theoutput of the interferometer is

$$
( E _ { \mathrm { o u t } } ) _ { c } = \frac { 1 } { 2 } ( r _ { 1 } e ^ { 2 i k _ { \mathrm { L } } L _ { x } } - r _ { 2 } e ^ { 2 i k _ { \mathrm { L } } \Delta _ { y } } ) E _ { 0 } J _ { 0 } ( \Gamma ) e ^ { - i \omega _ { \mathrm { L } } t } ,
$$

where $r _ { 1 } , r _ { 2 }$ are the reflectivities of the two end-mirrors.Taking perfectly reflecting mirrors, $r _ { 1 } = r _ { 2 } = - 1$ ，we have

$$
\begin{array} { r l r } & { } & { ( E _ { \mathrm { o u t } } ) _ { c } = - i E _ { 0 } J _ { 0 } ( \Gamma ) e ^ { - i \omega _ { \mathrm { L } } t + i k _ { \parallel } \left( L _ { x } + L _ { y } \right) } \sin [ k _ { \mathrm { L } } ( L _ { x } - L _ { y } ) ] } \\ & { } & { = - i E _ { 0 } J _ { 0 } ( \Gamma ) e ^ { - i \omega _ { \mathrm { L } } t + i k _ { \parallel } \left( L _ { x } + L _ { y } \right) } \sin \left[ 2 \pi \frac { L _ { x } - L _ { y } } { \lambda _ { L } } \right] , } \end{array}
$$

$^ { 2 3 } \mathrm { F o r } \ \lambda _ { \mathrm { L } } = 1 \mu \mathrm { m }$ we have $\omega _ { \mathrm { L } } / ( 2 \pi ) \simeq$ $3 0 0 ~ \mathrm { T H z }$ ，while typically $\Omega _ { \mathrm { m o d } } / ( 2 \pi ) \simeq$ $3 0 ~ \mathrm { M H z }$ so $\Omega _ { \mathrm { m o d } } \ll \omega _ { \mathrm { L } }$