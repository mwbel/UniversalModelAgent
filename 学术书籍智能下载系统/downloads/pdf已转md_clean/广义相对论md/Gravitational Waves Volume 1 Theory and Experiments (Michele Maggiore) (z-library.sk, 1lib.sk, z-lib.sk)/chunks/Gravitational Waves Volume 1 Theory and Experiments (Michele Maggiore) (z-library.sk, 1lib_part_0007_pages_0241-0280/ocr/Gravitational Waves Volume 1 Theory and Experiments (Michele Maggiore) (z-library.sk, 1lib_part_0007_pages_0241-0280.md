![](images/35fe003cc8fb73df7be15b4ac41819965de1d669ce76df42091d0b526ad54f48.jpg)  
Fig.4.21 The angular distribution of the gravitational radiation in the non-relativistic limit. The scattering plane is $z = 0$ and we have taken $\vartheta _ { s } = \pi / 2$

$\hat { \mathbf { n } } = ( \sin \theta \cos \phi , \sin \theta \sin \phi , \cos \theta )$ . Then，performing explicitly the con traction $\Lambda _ { i j , k l } \tilde { T } _ { i j } ( \omega ) \tilde { T } _ { k l } ^ { * } ( \omega )$ in eq.(3.16),we find

$$
\frac { d E } { d \omega d \Omega } = \frac { G m ^ { 2 } v ^ { 4 } } { \pi ^ { 2 } c ^ { 5 } } \sin ^ { 2 } \vartheta _ { s } \left[ \cos ^ { 2 } \theta + \frac { 1 } { 4 } \sin ^ { 2 } ( \vartheta _ { s } - 2 \phi ) \sin ^ { 4 } \theta \right] .
$$

The emission pattern is shown in Fig.4.21,for the case $\vartheta _ { s } = \pi / 2$ Observe that the radiation is emitted mostly along the $z$ axis,i.e.i the direction perpendicular to|the scattering plane.Integrating over th solid angle $d \Omega = d \cos \theta d \phi$ weget

$$
{ \frac { d E } { d \omega } } = { \frac { 8 G } { 5 \pi c ^ { 5 } } } m ^ { 2 } v ^ { 4 } \sin ^ { 2 } \vartheta _ { s } .
$$

For the corresponding two-body problem, $m$ is the reduced mass, $v$ the relative velocity and $\vartheta _ { s }$ is the scattering angle in the center-of-mass.

Actually,if one is interested only in the radiated energy, integrated over the solid angle,and not in its angular distribution,it can be com puted more quickly observingthat in the non-relativistic approximatiol $\bar { \boldsymbol { T } } _ { i j }$ is independent of the angle (all the angular dependence was in ti terms $\mathbf { k } { \cdot } \mathbf { v }$ and $\mathbf { k } { \cdot } \mathbf { v } ^ { \prime }$ that we dropped),and therefore

$$
\int d \Omega \Lambda _ { i j , k l } \tilde { T } _ { i j } \tilde { T } _ { k l } ^ { * } = \tilde { T } _ { i j } \tilde { T } _ { k l } ^ { * } \int d \Omega \Lambda _ { i j , k l } .
$$

The integral is performed using eq. (3.74),and we get back eq. (4.335

The frequency spectrum found in eq. (4.335) is flat up to the cul off frequency $\omega _ { \mathrm { m a x } } \sim 2 \pi \upsilon / b$ ,and the total radiated energy is obtaine integrating up to $\omega _ { \mathrm { m a x } }$ ，s0

$$
\begin{array} { c } { E _ { \mathrm { r a d } } \sim \displaystyle \frac { 1 6 G m ^ { 2 } } { 5 b } \left( \frac { v } { c } \right) ^ { 5 } \sin ^ { 2 } \vartheta _ { s } } \\ { = \displaystyle \frac { 8 } { 5 } m c ^ { 2 } \left( \frac { R _ { S } } { b } \right) \left( \frac { v } { c } \right) ^ { 5 } \sin ^ { 2 } \vartheta _ { s } , } \end{array}
$$

where $R _ { S } = 2 G m / c ^ { 2 }$ is the Schwarzschild radius of an object of mass $m$ .Therefore the total energy radiated is suppressed,with respect t0 the rest-mass energy $m c ^ { 2 }$ of the particle,both by the by-now familiar factor $( \upsilon / c ) ^ { 5 }$ (compare,e.g.with eqs.(3.319) or (3.340)） and by the ratio $R _ { S } / b$

# Relativistic limit

In the general relativistic case we repeat the same steps using the fil expression for $\tilde { T } ^ { \mu \nu } ( { \bf k } , \omega )$ givenlineq.(4.331),with $p ^ { i } = \gamma m v ^ { i }$ ,and setting ${ \bf k } = \omega \hat { \bf n } / c$ (see eq. (3.16)).We then find

$$
\begin{array} { l } { \displaystyle \frac { d E } { d \omega d \Omega } = \frac { G m ^ { 2 } \gamma ^ { 2 } v ^ { 4 } } { \pi ^ { 2 } } \qquad \quad ( 4 . 3 3 8 } \\ { \displaystyle \qquad \times \left[ f _ { 1 } ( v , \vartheta _ { s } ; \theta , \phi ) - f _ { 2 } ( v , \vartheta _ { s } ; \theta , \phi ) \sin ^ { 2 } \theta + f _ { 3 } ( v , \vartheta _ { s } ; \theta , \phi ) \sin ^ { 4 } \theta \right] , } \end{array}
$$

where

$$
\begin{array} { l } { f _ { 1 } ( v , \vartheta _ { s } ; \theta , \phi ) = a b \sin ^ { 2 } \vartheta _ { s } + \displaystyle \frac { 1 } { 4 } ( a - b ) ^ { 2 } , } \\ { f _ { 2 } ( v , \vartheta _ { s } ; \theta , \phi ) = \displaystyle \frac { a ( a + b ) } { 2 } \cos ^ { 2 } \phi + \displaystyle \frac { b ( a + b ) } { 2 } \cos ^ { 2 } ( \phi - \vartheta _ { s } ) } \\ { \displaystyle \qquad - 2 a b \cos \vartheta _ { s } \cos \phi \cos ( \phi - \vartheta _ { s } ) , } \\ { f _ { 3 } ( v , \vartheta _ { s } ; \theta , \phi ) = \displaystyle \frac { 1 } { 4 } \left[ a \cos ^ { 2 } \phi - b \cos ^ { 2 } ( \phi - \vartheta _ { s } ) \right] ^ { 2 } , } \end{array}
$$

and

$$
\begin{array} { r l r } {  { a \equiv a ( v ; \theta , \phi ) = \frac { \vert 1 } { 1 -  \hat { \mathbf { n } } \cdot \mathbf { v } / c  } } } \\ & { } & { = \frac { 1 } { 1 - ( v / c ) \sin \theta \cos \phi } , } \\ & { } & { b \equiv b ( v , \vartheta _ { s } ; \theta , \phi ) = \frac { 1 } { 1 - \hat { \mathbf { n } } \cdot \mathbf { v } ^ { \prime } / c } } \\ & { } & { = \frac { 1 } { 1 - ( v / c ) \sin \theta \cos ( \phi - \vartheta _ { s } ) } . } \end{array}
$$

h the non-relativistic limit we have $a  1 , b  1$ and,making use of he identities

$$
\begin{array} { c } { { \cos ^ { 2 } \phi + \cos ^ { 2 } ( \phi - \vartheta _ { s } ) - 2 \cos \vartheta _ { s } \cos \phi \cos ( \phi - \vartheta _ { s } ) = \sin ^ { 2 } \vartheta _ { s } , } } \\ { { \cos ^ { 2 } \phi - \cos ^ { 2 } ( \phi - \vartheta _ { s } ) = \sin ( \vartheta _ { s } - 2 \phi ) \sin \vartheta _ { s } , } } \end{array}
$$

e ecover eq.(4.334).Instead,in the ultra-relativistic limit,the factors and $b$ bend the radiation in the direction of the motion (more preisely,ina direction determined bya combination of the initial and final relocity).The resulting pattern function is shown in Fig.4.22 for the case $v = 0 . 8$ .The distribution is tilted in the direction of motion but the adiation is not focused in a very narrow cone,contrary to what happens in electrodynamics.We examine this point in detail in the simpler Eometrical setting of the next subsection.

# 4.4.2 Lack of beaming of GWs from accelerated masses

order to examine this effect eliminating irrelevant complications,let Sconsider an inelastic scattering in which a particle of mass $m$ initially rest, is accelerated in time $\Delta t$ to a velocity $v$ .39

As in the previous problem，we assume that the acceleration is in-Mantaneous and we then cut off the spectrum at $\omega _ { \mathrm { m a x } } \sim 2 \pi / \Delta t$ The mergy-momentum tensor is again given by eq. (4.331)，where now the ist term vanishes (since the initial velpcity is zero) and in the second m $\mathbf { v } ^ { \prime }$ is the final velocity,which we nbw denote by $\mathbf { v }$ .Therefore

$$
\begin{array} { r } { \displaystyle \tilde { T } ^ { i j } ( \omega \hat { \mathbf { n } } / c , \omega ) = \frac { i c \gamma m } { \omega } \frac { v ^ { i } v ^ { j } } { 1 - \hat { \mathbf { n } } \cdot \mathbf { v } / c } } \\ { \displaystyle = \frac { i c \gamma m } { \omega } \frac { v ^ { i } v ^ { j } } { 1 - ( v / c ) \cos { \theta } } . } \end{array}
$$

![](images/6aae9e8d960af4b0c497b770f129385af32a13d940e40d223001c640f03c7822.jpg)  
Fig.4.22 The angular distribution of the gravitational radiation in the relativistic limit.The scattering plane is $z = 0$ and we have taken $\vartheta _ { s } = \pi / 2$ and $v = 0 . 8$

$^ { 3 9 } \mathrm { { I n } }$ principleourformalismisvalid only if we have a closed system,so the total $T ^ { \mu \nu }$ is conserved．However,we can imagine for instance that the particle of mass $m$ is electrically charged, and is accelerated by the electric field inside a capacitor.To this closed system we can apply our formalism.If the arms of the capacitor are infinitely heavy， they do not contribute to the gravitational radiation because a heavy object of mass $M$ ，in the scattering process,acquires a recoil velocity $V \sim$ $1 / M$ and its contribution to $d E / d \omega$ ， according to eq.(4.335)，is $d E / d \omega \sim$ $M ^ { 2 } V ^ { 4 } \stackrel { - } { = } O ( 1 / \bar { M } ^ { 2 } )$ .Thus,in practice we can just consider the particle of mass $m$ on the accelerated trajectory.

From eq. (3.16) we find

![](images/4a98f51fe8288e82fbabb82c1a56043ab7353b2d83fbb26f9e8793181bf272e4.jpg)  
Fig.4.23 The function $p _ { \mathrm { e m } } ( \theta )$ ，in polar coordinates,fora charged particle with acceleration parallel to the velocity,and $v = 0 . 9 9$

$$
\frac { d E } { d \Omega d \omega } = \frac { G m _ { \uparrow } ^ { 2 } \gamma ^ { 2 } } { 2 \pi _ { \uparrow } ^ { 2 } \epsilon ^ { 5 } } \Lambda _ { i j , k l } \frac { v ^ { i } v ^ { j } v ^ { k } v ^ { l } } { \left[ 1 - ( v / c ) \cos \theta \right] ^ { 2 } } .
$$

Using eq. (1.39)and performing the contractions, we get

$$
\frac { d E } { d \Omega d \omega } = \frac { G m ^ { 2 } \gamma ^ { 2 } } { 4 \pi ^ { 2 } c } \left( { \frac { v } { c } } \right) ^ { 4 } \frac { \sin ^ { 4 } \theta } { [ 1 - ( v / c ) \cos \theta ] ^ { 2 } } ,
$$

or

<table><tr><td>dE</td><td>Gm2 4</td></tr><tr><td>dsdw</td><td>(） Pgw(0）， 4π2c</td></tr></table>

where

$$
\overline { { p _ { \mathrm { g w } } ( \theta ) = \gamma ^ { 2 } \frac { \sin ^ { 4 } \theta } { [ 1 - ( v / c ) \cos \theta ] ^ { 2 } } } }
$$

![](images/55827b7bf0f541c760f9ea317c0a91db22824cc04149163faad238d9fae57c0e.jpg)  
Fig.4.24 The function $p _ { \mathrm { g w } } ( \theta )$ fora particle with acceleration parallel to the velocity,and $v = 0 . 9 9$ Observe the difference in shape compared to Fig. 4.23.

describes the angular pattern.It is interesting to compare this resul with the electromagnetic radiation produced by a charged particle suddenly accelerated from rest to velocity $v$ .This is given by (see Jackson 1975,eq. (15.65))

where

$$
\begin{array} { c } { { \displaystyle  \frac { d E } { d \Omega d \omega } | _ { E M } = ( \frac { e ^ { 2 } } { 4 \pi ^ { 2 } c } ) ( \frac { v } { c } ) ^ { 2 } p _ { \mathrm { e m } } ( \theta ) , } } \\ { { \displaystyle  p _ { \mathrm { e m } } ( \theta ) = \frac { \sin ^ { 2 } \theta } { [ 1 - ( v / c ) \cos \theta ] ^ { 2 } } . } } \end{array}
$$

Both the gravitational and the electromagnetic radiations are tilted forward,because of the factor $[ 1 - ( v / c ) \cos \theta ] ^ { 2 }$ in the denominator. However,the different power of $\sin \theta$ in the numerator produces a crucial difference in the overall shape.In fact, $p _ { \mathrm { e m } } ( \theta )$ has a maximum at an angle $\bar { \theta }$ given by $\cos { \bar { \theta } } = v / c \ s o$ for large $\gamma$ $\bar { \theta } \simeq 1 / \gamma$ ；at the same time. the width of this maximum is $\Delta \theta = O ( 1 / \gamma )$ .Therefore,for $\gamma \to \infty$ ,the electromagnetic radiation is not only tilted asymptotically toward the forward direction,but is also beamed into a very narrow cone.

The angular pattern for $G \dot { \mathbb { W } }$ is very different.First of all,the angle $\bar { \theta }$ that maximizes $p _ { \mathtt { g w } } ( \theta )$ is_given by $\cos \bar { \theta } = c ( \gamma - 1 ) / ( v \gamma )$ which,in the large $\gamma$ limit，becomes $\bar { \theta } \simeq ( 2 / \gamma ) ^ { 1 / 2 }$ ；therefore $\bar { \theta }$ goes to zero only as $O ( 1 / \sqrt { \gamma } )$ .Second,and more important,one easily checks from the explicit expression that the width of the maximum of $p _ { \mathtt { g w } } ( \theta )$ is $\Delta \theta =$ $O ( 1 )$ ,to be compared with $\Delta \theta = O ( 1 / \gamma )$ for the electromagnetic case. $p _ { \mathrm { e m } }$ $\gamma ^ { 2 }$ and it drops to values $O ( 1 )$ if we move away from the maximum $\Delta \theta = O ( 1 / \gamma )$ ；for the gravitational radiation,it is still true that i value of $p _ { \mathrm { g w } }$ at its maximum is $O ( \gamma ^ { 2 } )$ just because of the factor $\gamma ^ { 2 }$ in front of it,but it remains $O ( \gamma ^ { \mathbb { 2 } } )$ if we move away from the maximum by a $\Delta \theta = O ( 1 )$

Therefore,even in the limit $\gamma \to \infty$ ,the gravitational radiation is not beamed in a narrow cone,but it is extended over a solid angle comparableto $4 \pi$ .The electromagnetic and gravitational radiation pattern are shown in Figs.4.23 and 4.24,respectively,for $v = 0 . 9 9$ .The origin of the difference is the factor $\sin ^ { 4 } \theta$ in the numerator of eq. (4.348),which reflect the spin-2 nature of the gravitational field, compared to the $\sin ^ { 2 } \theta$ in the numerator of eq. (4.350)，which reflect the spin-1 nature of the electromagnetic field.

To understand this point better,it is instructive to rederive this angular distribution,that we have obtained from a purely classical treatment, using the language of quantum field theory. This can be done evaluating Feynman diagrams such as that in Fig.4.25,that describe the emission of a graviton by an accelerated particle.The angular dependence is asily understood observing that the propagator of the massive particle gives a contribution to the amplitude proportional to

$$
\frac { 1 } { ( p + k ) ^ { 2 } + m ^ { 2 } } = \frac { 1 } { 2 ( p k ) } ,
$$

where $p$ is the final four-momentum of the massive particle and $k$ of the graviton, $( p k )$ denotes the scalar product of the two four-vectors,and we used $p ^ { 2 } = - m ^ { 2 }$ and $k ^ { 2 } = 0$ We write $p ^ { \mu } = ( E _ { p } / c , | \mathbf { p } | , 0 , 0 )$ with $| \boldsymbol { \mathrm { p } } | = E _ { p } \boldsymbol { v } / c ^ { 2 }$ ,while the graviton four-momentum is

$$
k ^ { \mu } = \left( E _ { g } / c , \left| \mathbf { k } \right| \cos \theta , \left| \mathbf { k } \right| \sin \theta , 0 \right) ,
$$

"here $| { \bf k } | = E _ { g } / c$ .Then

$$
\mathrm {  ~ \xi ~ } ( p k ) = - \frac { 1 } { c ^ { 2 } } E _ { p } E _ { k } [ 1 - \mathrm {  ~ \left( ~ } v / c \mathrm {  ~ \right) } \cos \theta ] .
$$

Ihis gives a factor $[ 1 - ( v / c ) \cos \theta ]$ in the denominator,in the amplitude M.and therefore a factor $[ 1 - ( v / c ) \cos \theta ] ^ { 2 }$ in the emission probability, whichis $\sim | { \mathcal { M } } | ^ { 2 }$ ．This is independent of whether the wavy line in g.4.25 is a photon or a graviton, as long as it is a massless particle,and Incidates why, both in $p _ { \mathrm { e m } } ( \theta )$ and in $p _ { \mathrm { g w } } ( \boldsymbol { \theta } )$ ,the angular dependence of e denominators is the same, $[ 1 - ( v / c ) \cos \theta ] ^ { 2 }$

The numerator is instead fixed by the emission vertex. For a photon, le external line carries its wavefunction $\epsilon _ { \mu } ^ { * } ( k )$ .Recall that physical mhotons are transverse, $\epsilon _ { \mu } ( k ) k ^ { \mu } = 0$ With $k ^ { \mu }$ given by eq. (4.352),this ouation has two linearly independent solutions

$$
\epsilon _ { \mu } ^ { ( 1 ) } ( k ) = ( 0 , \sin \theta , - \cos \theta , 0 ) , ~ \epsilon _ { \mu } ^ { ( 2 ) } | ( k ) = ( 0 , 0 , 0 , 1 ) ,
$$

lich corresponds to the two physical polarizations (plus the pure gauge mode $\epsilon ^ { \mu } \sim k ^ { \mu } )$ .The amplitude is proportional to40

$$
\sum _ { \lambda = 1 , 2 } \epsilon _ { \mu } ^ { ( \lambda ) } ( k ) p ^ { \mu } = | { \bf p } | \sin \theta .
$$

lereforein the numerator,in the amplitude,we have a factor $\sin \theta$ ， lich gives a factor $\sin ^ { 2 } \theta$ in $p _ { \mathrm { e m } } ( \theta )$ ,in agreement with eq. (4.350).

![](images/57704c671712adfb569aa6dbe7a37f24bae980930a3d2bfccaaee01ea0ec5168.jpg)  
Fig.4.25 A Feynman diagram corresponding to graviton emission by an accelerated mass. The cross denotes the external field that accelerates the mass. The wavy line represents the graviton.

40The fact that the Lorentz index carried by $\epsilon _ { \mu }$ is saturated by $p ^ { \mu }$ can be obtained writing explicitly the interaction vertex in quantum electrodynamics,but in fact it is evident from the fact that the amplitude must be linear in $\epsilon _ { \mu }$ ，so we cannot saturate the index $\mu$ contracting $\epsilon _ { \mu }$ with a second polarization vector $\epsilon ^ { \mu }$ ，neither we can contract it with $k ^ { \mu }$ ,since $\epsilon _ { \mu } ( k ) k ^ { \mu }$ vanishes.Then $\epsilon _ { \mu } ( k ) p ^ { \mu }$ is the only possible Lorentz scalar.Note also that,according to the Feynman rules of QED,an outgoing photon is actually associated toa factor $\epsilon _ { \mu } ^ { \ast }$ ,but we have chosen a real basis for the polarization vectors.

Similarly,an external graviton line is associated to the polarization tensor $e _ { \mu \nu } ( k )$ of the graviton,and the physical polarizations correspond to the plus and cross polarization tensors $e _ { \mu \nu } ^ { ( + ) } ( k )$ and $e _ { \mu \nu } ^ { ( \times ) } ( k )$ ,that sat isfy the condition $e _ { \mu \nu } ( k ) k ^ { \mu } = 0$ ．As before,the Lorentz indices can be saturated only by $p ^ { \mu }$ ,so this factor contributes to the amplitude $\mathrm { a s ^ { 4 1 } }$

41The computation isfaster if we orient the axes so that the $z$ axis is in the direction of the graviton momentum $\mathbf { k }$ ： and the scattering plane in Fig.4.25 is identified with the $( y , z )$ plane.In this frame $k ^ { \mu } = ( E _ { g } / c ) ( 1 , 0 , 0 , 1 )$ and $p ^ { \mu } = ( E _ { p } / c , 0 , | \mathbf { p } | \sin \theta , | \mathbf { p } | \cos \theta )$ The advantage is that in this frame the polarization tensors have the simple form

$$
e _ { \mu \nu } ^ { + } = \left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { - 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { \mu \nu }
$$

and

$$
e _ { \mu \nu } ^ { \times } = \left( \begin{array} { c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right) _ { \mu \nu } ,
$$

see eq. (1.56).Then $\begin{array} { r l } { e _ { \mu \nu } ^ { + } p ^ { \mu } p ^ { \nu } } & { { } = } \end{array}$ $- | \mathbf { p } | ^ { 2 } \sin ^ { 2 } \theta$ and $e _ { \mu \nu } ^ { \times } p ^ { \mu } p ^ { \nu } = 0$

$$
\sum _ { \lambda = + , \times } e _ { \mu \nu } ^ { ( \lambda ) } ( \not \vert k ) p ^ { \mu } p ^ { \nu } = - \vert { \bf p } \vert ^ { 2 } \sin ^ { 2 } \theta .
$$

This produces a factor $\sin ^ { 4 } \theta$ in the modulus squared of the amplitude and therefore in $p _ { \mathtt { g w } } ( \theta )$ ,in agreement with eq. (4.348).

Coming back to eq. (4.346)and integrating over the solid angle we g

$$
\frac { d E } { d \omega } = \frac { 2 G m ^ { 2 } } { 3 \pi c } \left[ \gamma ^ { 2 } \left( 6 - \frac { 4 v ^ { 2 } } { c ^ { 2 } } \right) - \frac { 3 c } { v } \log \frac { c + v } { c - v } \right] .
$$

In the non-relativistic limit $v \mapsto 0$ ,this reduces to

$$
\frac { d E } { d \omega } \simeq \frac { 8 } { 1 5 \pi c ^ { 5 } } G m ^ { 2 } v ^ { 4 } , ( v / c  0 ) ,
$$

while in the ultra-relativistic limit

$$
\frac { d E } { d \omega } \simeq \frac { 4 } { 3 \pi c } G m ^ { 2 } \gamma ^ { 2 } [ 1 - \frac { 3 \log \gamma ^ { 2 } } { 2 \gamma ^ { 2 } } + { \cal O } ( \frac { 1 } { \gamma ^ { 2 } } ) ] , ( v / c  1 ) .
$$

This spectrum is flat up to the maximum frequency $\omega _ { \mathrm { m a x } } \sim 2 \pi / \Delta t$ ,and the total radiated energy is therefore obtained multiplying by $\omega _ { \mathrm { m a x } }$ ,

# 4.5Solved problems

Problem 4.1. Fourier transform of the chirp signal

In this problem we compute the Fourier transform of the amplitudes given in eqs.(4.31) and (4.32).We consider first $h _ { + }$ ,and we write it in the form

$$
h _ { + } ( t ) \neq A \left( t _ { \mathrm { r e t } } \right) \cos \Phi \left( t _ { \mathrm { r e t } } \right) ,
$$

where

$$
A ( t _ { \mathrm { r e t } } ) = \frac { 1 } { r } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 4 } \left( \frac { 5 } { c ( t _ { c } - t _ { \mathrm { r e t } } ) } \right) ^ { 1 / 4 } \left( \frac { 1 + \cos ^ { 2 } \iota } { 2 } \right) ,
$$

and,in this problem, $t _ { c }$ is thevalue of retarded time at coalescence. The Fourier transform is

$$
\begin{array} { l } { { \displaystyle \tilde { h } _ { + } ( f ) = \int d t A ( t _ { \mathrm { r e t } } ) \cos \Phi \big ( t _ { \mathrm { r e t } } \big ) e ^ { i 2 \pi f t } } \qquad } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } e ^ { i 2 \pi f r / c } \int d t _ { \mathrm { r e t } } A ( t _ { \mathrm { r e t } } ) \left( e ^ { i \Phi ( t _ { \mathrm { r e t } } ) } + e ^ { - i \Phi ( t _ { \mathrm { r e t } } ) } \right) e ^ { i 2 \pi f t _ { \mathrm { r e t } } } } , } \end{array}
$$

and now in the last integral we rename $t _ { \mathrm { r e t } }  t$ .We have not written explicitly the limits of integration since we willcompute this integral with the stationary phase method.Then,all we need is that the stationary point be within the integration domain $t < t _ { c }$ ,and the fact that $A ( t _ { \mathrm { r e t } } )$ diverges at the limit of integration $t - t _ { c }$ becomes irrelevant,as longas the stationary phase method is justified (see below).We take $f > 0$ ,since the value at $f < 0$ can be obtained from $\tilde { h } _ { + } ( - f ) = \tilde { h } _ { + } ^ { * } ( f )$ ．Then,observing that $\dot { \Phi } = \omega _ { \mathrm { g w } } ( t ) > 0$ ，we see that only the term proportional to $e ^ { - i \Phi ( t ) + i 2 \pi f t }$ has a stationary point, while the term proportional to $e ^ { i \Phi ( t ) + i 2 \pi f t }$ is always oscillating fast,and integrates toa negligibly small value.Therefore

$$
\tilde { h } _ { + } ( f ) \simeq \frac { 1 } { 2 } e ^ { i 2 \pi f r / c } \int d t A ( t ) e ^ { i [ 2 \pi f t - \Phi ( t ) ] } .
$$

Since $\log A ( t )$ varies slowly in comparison with $\Phi ( t )$ ，the stationary point t, $( f )$ is determined by the condition $2 \pi f \overset { \cdot } { = } \dot { \Phi } ( t _ { * } )$ ,However $\dot { \Phi } = \omega _ { \mathrm { g w } }$ ，so this condition expresses the rather natural fact that the largest contribution to the Fourier component $\tilde { h } _ { + } ( f )$ with a given $f$ is obtained for the values of $t$ such hat the chirping frequency $\omega _ { \tt G W } ( t )$ is equal tb $2 \pi f$ .Expanding the exponential toorder $( t - t _ { * } ) ^ { 2 }$ we find

$$
\bar { h } _ { + } ( f ) \simeq \frac { 1 } { 2 } e ^ { i 2 \pi f r / c } A ( t _ { * } ) e ^ { i [ 2 \pi f t _ { * } - \Phi ( t _ { * } ) ] } \left( \frac { 2 } { \ddot { \Phi } ( t _ { * } ) } \right) ^ { 1 / 2 } \int _ { - \infty } ^ { \infty } d x e ^ { - i x ^ { 2 } } .
$$

Telaterintegral isaFresnel integral,andis givenby

$$
\int _ { - \infty } ^ { \infty } d x e ^ { - i x ^ { 2 } } = { \sqrt { \pi } } e ^ { - i \pi / 4 }
$$

ee Gradshteynand Ryzhik 1980,8.25). Therefore

where

$$
\begin{array} { l } { { \displaystyle \tilde { h } _ { + } ( f ) = \frac { 1 } { 2 } e ^ { i \Psi _ { + } } A ( t _ { * } ) \left( \frac { 2 \pi } { \ddot { \Phi } ( t _ { * } ) } \right) ^ { 1 / 2 } , } } \\ { { } } \\ { { \displaystyle \Psi _ { + } = 2 \pi f ( t _ { * } + r / c ) - \Phi ( t _ { * } ) - ( \pi / 4 ) . } } \end{array}
$$

Using $2 \pi f = \omega _ { \mathrm { g w } } ( t _ { * } )$ and the explicit expression of $\omega _ { \mathrm { g w } } ( t )$ given in eq. (4.19), we can eliminate $\tau _ { * } = t _ { c } - t _ { * }$ in favor of $f$ obtaining

$$
\tau _ { * } ( f ) = \frac { 5 } { 2 5 6 } ( G M _ { c } / c ^ { 3 } ) ^ { - 5 / 3 } ( \pi f ) ^ { - 8 / 3 } .
$$

Inserting this into the expressions for $A ( \tau )$ ，given in eq.(4.361)，and for $\ddot { \Phi }$ ， btaineddifferentiating twice eq.(4.30),we find

$$
\ddot { \iota } ( t _ { * } ) \left( \frac { 2 \pi } { \ddot { \Phi } ( t _ { * } ) } \right) ^ { 1 / 2 } = \left[ \left( \frac { 5 } { 2 4 } \right) ^ { 1 / 2 } \frac { 1 } { \pi ^ { 2 / 3 } } \right] \frac { c } { r } \bigg ( \frac { G M _ { c } } { c ^ { 3 } } \bigg ) ^ { 5 / 6 } f ^ { - 7 / 6 } \left( \frac { 1 + \cos ^ { 2 } \iota } { 2 } \right) ,
$$

Id therefore we get the result given in the text，see eq. (4.34). Similarly, mserting the value of $t _ { * } = t _ { c } - \tau _ { * }$ given by eq(4.368)into eq.(4.367) we get the phase $\Psi _ { + } ( f )$ given in eq. (4.37).Repeating the same steps for $h _ { \times }$ we get the mne prefactor,apart for the different dependence on $\iota$ and $\Psi \times = \Psi _ { + } + ( \pi / 2 )$ To compute the energy spectrum we need the quantity

$$
| \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } = \frac { 5 } { 2 4 \pi ^ { 4 / 3 } r ^ { 2 } c ^ { 3 } } \frac { ( G M _ { c } ) ^ { 5 / 3 } } { f ^ { 7 / 3 } } g ( \iota ) ,
$$

where the function $g ( \iota )$ is defined in eq.(4.9).Using eq. (4.10)，we se tha the angular average of $| \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( \grave { f } ) | ^ { 2 }$ is

$$
\int \frac { d \Omega } { 4 \pi } | \tilde { h } _ { + } ( f ) | ^ { 2 } + | \tilde { h } _ { \times } ( f ) | ^ { 2 } = \frac { 1 } { 6 \pi ^ { 4 / 3 } r ^ { 2 } c ^ { 3 } } \frac { ( G M _ { c } ) ^ { 5 / 3 } } { f ^ { 7 / 3 } } .
$$

It should be observed that the stationary point approximation that we have used is less and less good as $f$ grows. In fact,as $f$ grows,the stationary point $t _ { * }$ approaches the coalescence time $t _ { c }$ Since the function $A ( t )$ diverges as $t \to t _ { c }$ ,the approximation that $\log A ( t )$ varies slowly in comparison with $\Phi ( t )$ becomes less and less accurate.To check the validity of the stationary point approximation for $\tilde { h } _ { + , \times } ( f )$ ，we compare the total radiated energy computed using the saddle point approximation，eq.(4.43)，with an exact numerical evaluation of the time integral in the inspiral phase.Therefore we start from the exact expression

$$
\Delta E _ { \mathrm { r a d } } = \frac { r ^ { 2 } c ^ { 3 } } { 1 6 \pi G } \int d \Omega \int _ { - \infty } ^ { t _ { * } } d t \left( \dot { h } _ { + } ^ { 2 } + \dot { h } _ { \times } ^ { 2 } \right) ,
$$

which gives the energy radiated up to time $^ { t _ { * } }$ , and we compute numerically the integral.Inserting into this expfesson the GW amplitude given by eq.(4.29) and performing the integral over $d \Omega$ ,we find

$$
\begin{array} { c } { { \Delta E _ { \mathrm { r a d } } = \displaystyle \frac { ( G M _ { c } ) ^ { 1 0 / 3 } } { 2 ^ { 1 / 3 } G c ^ { 5 } } ( G M _ { c } ) ^ { 1 0 / 3 } } } \\ { { \times \displaystyle \int _ { - \infty } ^ { t _ { * } } d t \displaystyle \frac { 1 4 } { 1 5 } \left[ \displaystyle \frac { d } { d t } ( \omega _ { \mathrm { g w } } ^ { 2 / 3 } \cos \Phi ) \right] ^ { 2 } + \displaystyle \frac { 2 } { 3 } \left[ \displaystyle \frac { d } { d t } ( \omega _ { \mathrm { g w } } ^ { 2 / 3 } \sin \Phi ) \right] ^ { 2 } . } } \end{array}
$$

We now compute the time derivatives,taking into account that $\omega _ { \mathrm { g w } }$ depends on $t$ and that $d \Phi / d t = \omega _ { \mathrm { g w } }$ . The result can be written in the form

$$
\Delta E _ { \mathrm { r a d } } \simeq \frac { 5 ^ { 7 / 5 } } { 2 ^ { 3 4 / 5 } } M _ { c } c ^ { 2 } \left[ \frac { 1 } { 1 0 } \left( \frac { 8 } { 5 } \right) ^ { 1 2 / 5 } a _ { 1 } + \left( \frac { 8 } { 5 } \right) ^ { 7 / 5 } a _ { 2 } - \frac { 1 } { 3 0 } \left( \frac { 8 } { 5 } \right) ^ { 1 2 / 5 } a _ { 3 } \right] ,
$$

with

$$
\begin{array} { l } { { a _ { 1 } = \displaystyle \int _ { x _ { * } } ^ { \infty } \frac { d x } { x ^ { 1 7 / 5 } } \left( \frac { 7 } { 1 5 } \cos ^ { 2 } x + \frac 1 3 \sin ^ { 2 } x \right) , } } \\ { { a _ { 2 } = \displaystyle \int _ { x _ { * } } ^ { \infty } \frac { d x } { x ^ { 7 / 5 } } \left( \frac { 7 } { 1 5 } \sin ^ { 2 } x + \frac 1 3 \cos ^ { 2 } x \right) , } } \\ { { a _ { 3 } = \displaystyle \int _ { x _ { * } } ^ { \infty } \frac { d x } { x ^ { 1 2 / 5 } } \sin 2 x . } } \end{array}
$$

The lower limit of the integrals, $x _ { \ast }$ ,is given by

$$
x _ { * } = 2 \left( \frac { 5 G M _ { c } } { c ^ { 3 } } \right) ^ { - 5 / 8 } \tau _ { * } ^ { 5 / 8 } .
$$

Taking $M _ { c } \simeq 1 . 2 1 M _ { \odot }$ (corresponding to two equal masses $M _ { \mathrm { N S } } ~ = 1 . 4 M _ { \odot } )$ , and $\tau _ { * } \simeq 4 . 6$ ms which,according to eq.(4.20),correspond to taking a cutofl at $f _ { \mathrm { m a x } } = 1 ~ \mathrm { k H z }$ we have $x _ { * } \simeq 4 6 . 1$ .Computing numerically the integrals, we find that $a _ { 2 } \simeq 0 . 2 1$ while $a _ { 1 } , a _ { 3 } = O ( 1 0 ^ { - 5 } )$ are negligible. Since $a _ { 1 } , a _ { 3 }$ come from the terms with $\dot { \omega } _ { \mathrm { g w } }$ ,the result could have been obtained more simply neglecting the derivatives of $\omega _ { _ { \mathrm { g } } \ w }$ in eq. (4.373) (this is indeed the reason why the stationary point approximation discussed in the previous problem works well).Putting together the numerical factors,we finally arrive at $\Delta E _ { \mathrm { r a d } } \simeq$ $4 . 2 \times 1 0 ^ { - 2 } M _ { \odot } c ^ { 2 }$ ,in full agreement with eq. (4.43).

![](images/79883332116a32474a336935d59f23cbdc735c4d608c4b3d49250a9b6540b597.jpg)

In this problem we compute the Fourier decomposition of the Keplerian motion and of its second mass moment.Using eqs.(4.63),(4.64) and (4.58) we write

$$
\begin{array} { l } { { { \displaystyle x ( \beta ) = a ( \cos u - e ) , } } } \\ { { { \displaystyle y ( \beta ) = b \sin u , } } } \end{array}
$$

where the dependence of $u$ on $\beta$ is given implicitly by

$$
\beta = u - e \sin u .
$$

As shown between eq. (4.83) and eq. (4.93),we can write

$$
\begin{array} { l } { { \displaystyle x ( \beta ) = \sum _ { n = 0 } ^ { \infty } a _ { n } \cos ( n \beta ) \ : , } } \\ { { \displaystyle y ( \beta ) = \sum _ { n = 1 } ^ { \infty } b _ { n } \sin ( n \beta ) \ : , } } \end{array}
$$

hich can be inverted to give, for $n \neq 0$ ，

$$
\begin{array} { c } { { a _ { n } = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } d \beta x ( \beta ) \cos ( n \beta ) } } \\ { { = \displaystyle \frac { 2 a } { \pi } \int _ { 0 } ^ { \pi } d \beta ( \cos u - e ) \cos ( n \beta ) , } } \end{array}
$$

nd

$$
\begin{array} { c } { { b _ { n } = \displaystyle \frac { 2 } { \pi } \int _ { 0 } ^ { \pi } d \beta y ( \beta ) \sin ( n \beta ) } } \\ { { = \displaystyle \frac { 2 b } { \pi } \int _ { 0 } ^ { \pi } d \beta \sin u \sin ( n \beta ) , } } \end{array}
$$

ile for $n = 0$

$$
a _ { 0 } = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } d \beta x ( \beta ) .
$$

The integrals for $n \neq 0$ can be performed using the integral representation of he Bessel function $J _ { n } ( z )$

$$
J _ { n } ( z ) = \int _ { 0 } ^ { \pi } \frac { d u } { \pi } \cos ( n u - z \sin u ) ,
$$

e e.g.Gradshteyn and Ryzhik 1980,8.411.1). Then we have, for $n \neq 0$

$$
\begin{array} { l } { { a _ { n } = 2 a \int _ { 0 } ^ { \pi } { \frac { d \beta } { \pi } } \left( \cos \pi - e \right) \cos ( n \beta ) } } \\ { { \ } } \\ { { \ } } \\ { = { \frac { 2 a } { n } } \int _ { 0 } ^ { \pi } { \frac { d \beta } { \pi } } \left( \cos \pi - e \right) { \frac { d } { d \beta } } \sin ( n \beta ) } \\ { { \ } } \\ { { \ } } \\ { = { - \frac { 2 a } { n } } \int _ { 0 } ^ { \pi } { \frac { d \beta } { \pi } } \left[ { \frac { d } { d \beta } } ( \cos u - e ) \right] \sin ( n \beta ) }  \\ { { \ } } \\ { { \ } } \\ { { \ } } \\ { = { - \frac { 2 a } { n } \int _ { 0 } ^ { \pi } { \frac { d u } { \pi } } \left[ { \frac { d } { d u } } ( \cos u - e ) \right] \sin ( n \beta ) } } \\ { { \ } } \\ { { \ } } \\ { { \ } } \end{array}
$$

We now use the identity $2 \sin x \sin y = \cos ( x - y ) - \cos ( x + y )$ and we get

$$
\begin{array} { l } { { a _ { n } = { \displaystyle \frac { a } { n } \int _ { 0 } ^ { \pi } \frac { d u } { \pi } \cos [ ( n - 1 ) u - n e \sin u ] - \cos [ ( n + 1 ) u - n e \sin u ] } } } \\ { { \ = { \displaystyle \frac { a } { n } [ J _ { n - 1 } ( n e ) - J _ { n + 1 } ( \bar { \mu } e ) ] } , \ } } \end{array}
$$

where,in the second line,we used eq.(4.387)．Using the Bessel functiom identity

the result can also be rewriten as

$$
a _ { \eta } ^ { \mathrm { ~ \normalsize ~ } } = \frac { 2 a } { n } J _ { n } ^ { \prime } ( n e ) .
$$

The integral for $a _ { 0 }$ is instead elementary and gives $a _ { 0 } ~ = ~ - ( 3 / 2 ) a e$ The computation for $b _ { n }$ is analogous to that of $a _ { n }$ ，

$$
\begin{array} { l } { { b _ { n } = \displaystyle - \frac { 2 b } { n } \int _ { 0 } ^ { \pi } \displaystyle \frac { d \beta } { \pi } ~ \sin { \ u } \frac { d } { d \beta } \cos ( n \beta ) } } \\ { { { } ~ = \displaystyle \frac { 2 b } { n } \int _ { 0 } ^ { \pi } \displaystyle \frac { d u } { \pi } ~ \frac { d \sin u } { d u } \cos ( n \beta ) } } \\ { { { } ~ = \displaystyle \frac { 2 b } { n } \int _ { 0 } ^ { \pi } \displaystyle \frac { d u } { \pi } ~ \cos u \cos ( n u - n e \sin u ) } } \\ { { { } ~ = \displaystyle \frac { b } { n } \left[ J _ { n - 1 } ( n e ) + J _ { n + 1 } ( n e ) \right] . } } \end{array}
$$

Using the Bessel functions identity

$$
J _ { n + 1 } ( z ) + J _ { n - 1 } ( z ) = { \frac { 2 n } { z } } J _ { n } ( z ) ,
$$

this result can also be rewritten as

$$
b _ { n } = \frac { 2 b } { n e } J _ { n } ( n e ) .
$$

We next compute the Fourier decomposition of $x ^ { 2 } ( \beta ) , y ^ { 2 } ( \beta )$ and $x ( \beta ) y ( \beta ) ,$ ] Since $x ( \beta )$ is even under $\beta \to - \beta$ while $y ( \beta )$ is odd, $x ^ { 2 } ( \beta )$ and $y ^ { 2 } ( \beta )$ are even while $x ( \beta ) y ( \beta )$ is odd,and therefore we can write

$$
\begin{array} { r l r } {  { \sigma ^ { 2 } ( \beta \| \phi = \sum _ { \ell = 0 } ^ { \infty } A _ { \ell } \cos ( \pi \beta ) , } } \\ & { } & { \times \cos ( \pi \beta ) , } \\ & { } & { \quad \times \frac { \beta } { 2 } ( \beta \| \phi = \sum _ { \ell = 0 } ^ { \infty } B _ { \ell } \cos ( \pi \beta ) , } \\ & { } & { \times \cos ( \pi \beta ) , } \\ & { } & { \quad \times ( \beta \| y ( \beta ) = \sum _ { \ell = 1 } ^ { \infty } C _ { \mathrm { s r i n } ( \pi \beta ) } \| \phi = \sum _ { \ell = 1 } ^ { \infty } C _ { \mathrm { s r i n } ( \pi \beta ) } \| \phi , } \\ & { } & { \quad \times \mathrm { o t } \ \mathrm { s g n } , \ \mathrm { t r a p } \| \phi = 0 , } \\ & { } & { \quad \times \mathrm { o _ { \ell } } \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } d \beta \kappa ^ { 2 } ( \beta ) \cos ( \pi \beta ) } \\ & { } & { \quad \times \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } d \beta \big ( \delta \beta ^ { 2 } ( \beta ) \cos ( \pi \beta ) } \\ & { } & { \quad \times \frac { 2 } { \pi } \int _ { 0 } ^ { \infty } d \beta \big ( \delta \pi ( \beta ) \sin ( \pi \beta ) } \end{array}
$$

which can be inverted

The calculations are similar to those performed above for $a _ { n }$ and $b _ { n }$ ,and the result is

$$
\begin{array} { l } { \displaystyle { A _ { n } = \frac { a ^ { 2 } } { n } \left[ J _ { n - 2 } ( n e ) - J _ { n + 2 } ( n e ) - 2 e \big ( J _ { n - 1 } ( n e ) - J _ { n + 1 } ( n e ) \big ) \right] , } } \\ { \displaystyle { B _ { n } = \frac { b ^ { 2 } } { n } \left[ J _ { n + 2 } ( n e ) - J _ { n - 2 } ( n e ) \right] , } } \\ { \displaystyle { C _ { n } = \frac { a b } { n } \left[ J _ { n + 2 } ( n e ) + J _ { n - 2 } ( n e ) - e \big ( J _ { n + 1 } ( n e ) + J _ { n - 1 } ( n e ) \big ) \right] , } } \end{array}
$$

while $A _ { 0 } = ( 1 + 4 e ^ { 2 } ) / 2$ and $B _ { 0 } = 1 / 2$ .Observe that these coefficients can be rewritten in many equivalent forms using Bessel function identities.

# Further reading

·The radiation from a binary system of two point masses and their frequency spectrum was computed by Peters and Mathews (1963)．TheFourier expansion of the Kepler motion is discussed in Watson (1966). The orbit circularization due to radiation of angular mormentum was computed by Peters (1964).The chirp amplitude was first computed by Clark and Eardley (1977),see also Thprne (1987), Finn and Chernoff (1993)，Cutler and Flanagan (1994).

·The fact that coalescing binaries can be standard candles was discussed by Schutz (1986). The propagation of GWs through a FRW background,in the geometric optics limit,is discussed in Thorne (1983), Section 2.5.4.

·The production of GWs from rotating and precessing rigid bodies is computed in Zimmermann and Szedenits (1979),for axisymmetric bodies and for triaxial bodies with small wobble angle. The radiation from non-axisymmetric bodies rotating and precessing is discussed in Zimmermann (1980) and VanDen Broeck (2005).Rotating fluid stars are studied in Bonazzola and Gourgoulhon (1996).The back-reaction due to wobble radiation is discussed in Bertotti and Anile(1973) and Cutler and Jones (2001).In the latter paper one also finds the correct result for elastic,rather than rigid，neutron stars.

·The production of GWs from a point-like particle falling radially into a black hole is discussed in Davies,Ruffini,Press and Price (1971) and Davis, Ruffini and Tiomno (1972),see also Ohanian and Rufini (1994).The frequency spectrum is computed in Wagoner (1979).Detweiler and Szedenits (1979)show that,allowing for angular momentum of the test mass,can increase the power output by a large factor,and higher multipoles become more important.The suppression due to the tidal disruption of extended sources is computed by Haugan, Shapiro and Wasserman (1982).Early simulations of head-on black-hole collisions were performed by Smarr (1979).

·The radiation produced in the collision between particles is discussed in Weinberg (1972)，Section 10.4. The calculation of the gravitational radiation produced by an accelerated particle,using Feynman diagram techniques,and the fact that the radiation emitted in particle scattering is not beamed,is discussed by Feynman (see Feynman, Morinigo and Wagner 1995,Section 16.4),while our purely classical derivation leading to eq.(4.348) is, as far as we know,original.

· Various examples of production of GWs are discussed in the textbook by Shapiro and Teukolsky (1983),Chapter 16.

5

# GW generation by post-Newtonian sources

5.1 The post-Newtonian expansion 2:   
5.2 The relaxed Einstein equations 2   
5.3 The Blanchet-Damour approach 2   
5.4 The DIRE approach 2   
5.5 Strong-field sources 2   
5.6 PN corrections to inspiraling binaries 2

In Chapter 3 we discussed the generation of GWs assuming that th background space-time can be taken as flat,i.e. that the sources thai produce GWs in their far-feld region contribute negligibly to the space time curvature in their near-ffeld region. We then computed the Gw production as an expansion in $\dot { \boldsymbol { \upsilon } } / c$ where $v$ is some typical internal speed of the source. We saw that the leading term is given by the Einstein quadrupole formula,and that higher-order corrections in $v / c$ can be organized in a multipole expansion. This procedure assumes that the background space-time curvature and the velocity of the source can be treated as independent parameters,so that we can keep the space-time fat,while taking into account the $v / c$ corrections. This is indeed the case when the dynamics of the system is governed by non-gravitationalforces For example,a beam of charged particles accelerated by an externa electric field could reach highlyrelativistic speeds,but stillit contributes negligibly to the background space-time curvature,and for such a soure the formalism developed in Chapter 3 is adequate. For $\upsilon / c \ll 1$ we call compute the corrections in powers of $v / c$ to the leading quadrupole result using the multipole expansion, since in this case the lowest multipoles dominate. Even in the extreme relativistic case,where the multipole expansion becomes useless,we can still compute GW production using the exact formula (3.14). An example of the latter type of computation was given in Section 4.4.

However,the astrophysical systems which are more interesting for GW detection are held together by gravitational forces. In this case the assumption that the velocity of the source and the space-time curvature are independent is no longer valid,and the above formalism cannot $\mathfrak { b e }$ applied.In fact,for a self-gravitating system with total mass $m$ we have $( v / c ) ^ { 2 } \sim R _ { S } / d$ where $\bar { R _ { S } } = \ k \bar { 2 } G m / c ^ { 2 }$ (so $R _ { S }$ has the meaning of the Schwarzschild radius associated to the mass $m _ { \ l }$ and $d$ is the typical size of the system (e.g. its radius,for an isolated source such as a rotating neutron star,or the orbital distance for a binary system). Fora binary system we saw this explicitly in eq.(3.2).1 More generally, the relation $( \upsilon / c ) ^ { 2 } \sim R _ { S } / d$ holds for self-gravitating systems as a consequence of the virial theorem.Since $R _ { S } / d$ is a measure of the strength of the gravitational feld near the source,as soon as we switch on the $v / c$ corrections we must also,for consistency,consider the deviation of the background from fat space-time.

$^ 1 \mathrm { I n }$ this case,the precise numericalfactor is $( v / c ) ^ { 2 } = R _ { S } / ( 2 d )$

In this chapter we discuss how to go beyond the limit of sources moving in flat space-time.For a self-gravitating system such as a binary star,assuming that space-time is flat means that we describe its dylamicsusing Newtonian gravity,rather than general relativity. We will ee that,when dealing witha (moderately)relativistic system,held togetherby gravitational forces,the source must rather be described by a post-Newtonian (PN) formalism.In Section 5.1 we recall the PN expansion in general relativity,and we discusshow to obtain the lowest-order rorrection to the Newtonian equations of motion. GW generation by post-Newtonian sources is described in great detail in Sections 5.2-5.4, and the application to sources with strong gravitational fields,such as meutron stars and black holes,is discussed in Section 5.5.

The results of this chapter have first of all an intrinsic conceptual mterest,since we see here at work the full non-linear structure of general elativity.Furthermore,this formalism is of paramount importance in le computation of the waveform from an inspiraling binary system. I fact,as we will see in Section 5.6.1(and we will further discuss in Chapter 7),a very accurate prediction of the waveform is necessary to extract the GW signal of an inspiraling binary from the experimental lata.This waveform has by now been computed to very high order in c,as we will review in Section 5.6. It is quite remarkable that non-Imear effects in general relativity of apparently very high order,in fact corrections in $v / c$ even up to order $( v / c ) ^ { 7 }$ ,are crucial for the extraction fa coalescing binary signal from the experimental data. Conversely, rompact binary systems might turn out to be a unique laboratory for lesting the non-linear aspects of general relativity.

# 5.1 The post-Newtonian expansion

# 1.1 Slowly moving, weakly self-gravitating sources

he relation between different possible regimes for the sources,dependgon the strength of their self-gravity and on their velocity,is schematall ilustrated in Fig. 5.1. In theplane $( v ^ { 2 } / c ^ { 2 } , R s / d )$ ,the region close o the horizontal axis,where $R _ { S } / d$ is negligible,corresponds to sources hose dynamics is governed by non-gravitational forces,and which can described using the linearized theory developed in Chapter 3.The gion close to the vertical axis corresponds to essentially static bodies, lich are not interesting sources of GWs. Slowly moving,weakly selfavitating sources correspond to the region of the plane where $( v / c ) ^ { 2 }$ $R _ { S } / d$ are comparable,and none of them is too close to one.As we ill see in this chapter,they must be described by a post-Newtonian malism,so they are marked as“PN”in the figure.When $R _ { S } / d$ gets dse to one we are dealing with strong gravity,typically black holes or utron stars,and we have to resort to strong-field methods.

We uow consider a slowly moving and weakly self-gravitating source, ich means that $v / c$ and $R _ { S } / d$ are sufficiently small,² so we can use

![](images/571739a65516bdef4103d94510afe258edd70d666de2c06a334d152bc2ebe0c4.jpg)  
Fig.5.1 The different regimes in the plane $( v ^ { 2 } / c ^ { 2 } , R s / d )$

2The term “slowly moving sources” can be misleading.For instance,we will be interested in applying the formalism to inspiraling compact binaries made of neutron stars or black holes which, in the last stage of their coalescence, can reach values of $\upsilon / c$ as high as $1 / 2$ (in correspondence with the innermost circular orbit,defined by the minimum energy for circular orbits),and in this sense are very relativistic objects.This means that we might need the result to a very high order in $v / c$ .Observe also that the condition $v / c \ll 1$ must be imposed both on the bulk velocities of the objects,such as the orbital velocities of each neutron star in a NS-NS binary system,and also on the internal velocities inside each extended body. This means that we are also requiring that the sources are at most weakly stressed.

them as expansion parameters,and that they are related by $v / c \sim$ $( R _ { S } / d ) ^ { 1 / 2 }$ . We also demand that the matter energy-momentum tensol $T ^ { \mu \nu }$ of the source has a spatially compact support,i.e. that it can be enclosed ina time-like world tube $r \leqslant d$ (more precisely, the statement $r \ \leqslant \ d$ is assumed to hold in lthe harmonic coordinate system defined below),and that the matter distribution inside the source is smooth,i.e that $T ^ { \mu \nu } ( t , { \bf x } )$ is infinitely differentiable over the whole space-time. We will discuss in Section 5.5 the applicability of the formalism to systems containing black holes.

Our aim is to understand hpw to compute systematically the corrections to the results of linearized theory,in an expansion in powers of $v / c$ Just as in electrodynamics,for a non-relativistic source it is convenient to distinguish between the near zone and the far zone. We found in eq.(3.24) that the typical reduced wavelength of the radiation emitted. $\dagger$ ,is larger than the typical size of the source, $d$ ,bya factor of order $c / v$ so,for non-relativistic sources, $d \ll \lambda$ .The near zone is the region $r \ll \ast$ ,and the exterior near zone is the region

$$
\begin{array} { l } { \displaystyle { d < r \ll \dot { x } . } } \end{array}
$$

$^ 3 \mathrm { I n }$ the presence of strong-feld sources,， such as black holes or neutron stars,the near zone can be further separated into a strong-field near zone and a weakfield near zone.The strong-field near zone is the region contained inside balls centered on the sources (e.g. around the two stars in a binary system),and with a radius equal toa few times their Schwarzschild radius.The weak-field near zone is the rest of the near zone, i.e.is the near zone with these strongfield regions excised．We will discuss strong-field sources in Section 5.5.

4When studying the propagation of GWs across cosmological distances,it can be convenient to further distinguish among a local wave zone and a distant wavc zone.The boundary between the two is where become important effects on the propagation of GWs such as deflection or redshift due to the background curvature of the universe,or the gravitational lensing induced by galaxies,etc.These effects have already been studied in Section 1.5,and in the following we will only consider the local wave zone.Technically,this implies that we will consider background spacetimes that are asymptotically flat.

In the near zone retardation effects are negligible,and we basically have static potentials. We will see that in this region the post-Newtonian expansion is the correct tool.3 The far zone (or wave zone) is defined as the region $r \gg \ast$ .4 In the fal zone we have waves, retardation effects are crucial and a different treatment is required.The near and the far region are separated by an intermediate region at $r \sim \lambda$ (which, in electromagnetism,is called the induction zone).

In a first approximation,we|might think that the problem of computing GW generation from a weakly self-gravitating source,in an expansion in $v / c$ has two aspects:

· We must determine the general-relativistic correction to the equations of motion of the sources up to the desired order in $v / c$ using a post-Newtonian expansion. ·Given their motion to the desired order，we must compute the GWs emitted by these Sources. We have seen in Chapter 3 that GW production can be organized in a multipole expansion,which is an expansion in $v / c$ .Thus,we cannot limit ourselves to the quadrupole formula, but we must include a number of higher multipoles,consistent with the order in $v / c$ to which we wish to work.

The real story is however more complex,and these two aspects can not really be separated. In particular,the emission of GWs costs energy which is drained from the source so,beyond a certain order,GWs wil back-react on the matter sources,influencing their equations of motion. Furthermore,because of the non-linearity of general relativity,the gravitational field is itself a sourcefor GW generation,and the GWs which have been computed to a given order in $v / c$ ，at higher orders become themselves a source of further GW production.So,a full-fedged formalism for computing systematically the production of GWs of a selfgravitating source in powers of $v / c$ is necessarily quite complicated.

# 5.1.2 PN expansion of Einstein equations

The post-Newtonian approximation is a basic tool of general relativity,developed already in1916by Einstein himself,by Droste,de Sitter, and Lorentz,and it has produced a number of classical results. Still, when one tries to extend the lowest-order computations to a systematic all-order expansion,or when one wants to use it for computing the generation of GWs,it raises important conceptual (as well as technical) diffculties,and a fully satisfactory formulation emerged only in relatively recent years.

We begin by analyzing the lowest-order post-Newtonian corrections to the motion of the source,neglecting for the moment the back-reaction lue to GWs (as we will see,the back-reaction of GWs on the motion of fhe source does not enter into play at the level of the first and even the vcond PN corrections). As discussed above, we assume that the source i non-relativistic, $v / c \ll 1$ ,and self-gravitating,so that $( R _ { S } / d ) ^ { 1 / 2 } \sim$ v/c.We introduce the small parameter5

$$
\epsilon \sim ( R _ { S } / d ) ^ { 1 / 2 } \sim v / c ,
$$

mnd we also demand that $| T ^ { i j } | / T ^ { 0 0 } = \phi ( \epsilon ^ { 2 } )$ ,i.e. that the source be meakly stressed.For instance,for a fluid with pressure p and energy density $\rho$ ,this means that $p / \rho = { O } \left( { \epsilon } ^ { 2 } \right)$ .We then expand the metric and le energy-momentum tensor in powers of $\epsilon$ . As long as we neglect the mission of radiation,a classical system subject to conservative forces invariant under time reversal.6 Under time reversal $g _ { 0 0 }$ and $g _ { i j }$ are men, while $g _ { 0 i }$ is odd.On the other hard,the velocity $v$ changes sign mder time reversal so,as long as the invariance under time-reversal is preserved, $g _ { 0 0 }$ and $g _ { i j }$ can contain only even powers of $v$ (and therefore of .while $g _ { 0 i }$ can contain only odd powers of $v$ .By inspection of Einstein ations one finds that,to work consistently to a given order in $\epsilon$ if Rexpand $g _ { 0 0 }$ up to order $\epsilon ^ { n }$ we must also expand $g _ { 0 i }$ up to order $\epsilon ^ { n - 1 }$ md $g _ { i j }$ up to $\epsilon ^ { n - 2 }$ .Furthermore,the expansion of $g _ { 0 i }$ starts from $O ( \epsilon ^ { 3 } )$ Ihus the metric is expanded as follows

$$
\begin{array} { r l r } { g _ { 0 0 } = - 1 + ^ { ( 2 ) } g _ { 0 0 } + } & { { } ^ { ( 4 ) } g _ { 0 0 } + } & { ^ { ( 6 ) } g _ { 0 0 } + \ldots , } \\ { g _ { 0 i } = } & { { } } & { ^ { ( 3 ) } g _ { 0 i } + } & { ^ { ( 5 ) } g _ { 0 i } + \ldots , } \\ { g _ { i j } = } & { { } \delta _ { i j } } & { + } & { ^ { ( 2 ) } g _ { i j } + } & { ^ { ( 4 ) } g _ { i j } + \ldots , } \end{array}
$$

${ } ^ { ( n ) } g _ { \mu \nu }$ denotes the terms of order $\epsilon ^ { n }$ in the expansion of $g _ { \mu \nu }$ 7 milarly, we expand the energy-momentum tensor of matter,

$$
\begin{array} { l } { { T ^ { 0 0 } = { } ^ { ( 0 ) } T ^ { 0 0 } + { } ^ { ( 2 ) } T ^ { 0 0 } + \dots , } } \\ { { T ^ { 0 i } = { } ^ { ( 1 ) } T ^ { 0 i } + { } ^ { ( 3 ) } T ^ { 0 i } + \dots , } } \\ { { T ^ { i j } = { } ^ { ( 2 ) } T ^ { i j } + { } ^ { ( 4 ) } T ^ { i j } + \dots . } } \end{array}
$$

can now plug these expansions into the Einstein equations,and Iate terms of the same order in $\epsilon$ .To determine the order of the vari-Sterms we must also take into account that, since we are considering a

5When comparing with results in the literature,observe that some authors define $\epsilon \sim v / c$ ，as we do,while others define $\epsilon \sim ( \upsilon / c ) ^ { 2 }$

6The emission of radiation breaks time reversal invariance through the boundary conditions,since the no-incomingradiation boundary conditions (defined in Note1on page 102)are transformed into no-outgoing-radiation boundary conditions or,in other words,the retarded Green's function under timereversal becomes an advanced Green's function.We will come back to this point below.

7Actually， one could always generate terms with the wrong parity by performing a gauge transformation.So a more accurate statement is that,as long as radiation-reaction effects are neglected，odd terms in goo such as (5)goo (aswellaseven terms in g0i and odd terms in $g _ { i j }$ ）satisfy homogeneous equations,and can be set to zero with a gauge transformation. In contrast,even terms in $g _ { 0 0 }$ (as well as odd terms in $g _ { 0 i }$ and even terms in $g _ { i j }$ satisfy inhomogeneous equations,with the appropriate terms from the expansion of the matter energy-momentum tensor on the right-hand side,so we cannot find a gauge transformation that sets them to zero.See Chandrasekhar and Esposito (1970).

source moving with non-relativistic velocity $v$ ,the time derivatives of th metric generated by this source are smaller than the spatial derivative by a factor $O ( v )$ ，

$$
\frac { \partial } { \partial t } = O ( v ) \frac { \partial } { \partial x ^ { i } } ,
$$

or $\partial _ { 0 } = { \cal O } ( \epsilon ) \partial _ { i }$ .In particular, the d'Alembertian operator,applied the imetric,to lowest order becomes a Laplacian,

$$
- \frac { 1 } { c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial t ^ { 2 } } + \overline { { { \bf v } } } ^ { 2 } = [ 1 + O ( \epsilon ^ { 2 } ) ] { \bf \nabla } { \bf \nabla } ^ { 2 } .
$$

This means that retardation effects are small corrections,and the lowest order solution is given in terms of instantaneous potentials.In the PN expansion we are therefore trying to compute some quantity $F ( t - r / c )$ suchas a given component of the metric,which is intrinsicallya functiol of retarded time $t - r / c$ ，fromits expansion for small retardation,

$$
F ( t - r / c ) = F ( t ) - \frac { r } { c } \dot { F } ( t ) + \frac { r ^ { 2 } } { 2 c ^ { 2 } } \ddot { F } ( t ) + \ldots .
$$

Each derivative of $F$ carries afactor of $\omega$ ,the typical frequency of thi radiation emitted.Since $\omega / c \neq 1 / \hbar$ ，we see that eq.(5.7) isin fact an expansion in powers of $r / \ X$ .Therefore the PNexpansion is valid only the near zone, $r \ll \lambda$ ，and breaks down in the radiation zone $r \gg \ast$ We will examine in detail this breakdown in the far region in the following sections,where we will see explicitly how a naive extrapolation of the PM iterative scheme up to $r = \infty$ leads to divergences.So,the PN expansiol is a formalism that can be used to compute the gravitational field in th nearregion,but must be supplemented by a different treatment of the far-field region,to compute the fields in the radiation zone.

# 5.1.3Newtonian limit

Let us first recall,from elementary general relativity,that the Newtonial limit corresponds to keeping $g _ { \mathrm { 0 0 } } = - 1 + \ O ^ { ( 2 ) } g _ { 0 0 }$ ， $g _ { 0 i } = 0$ and $g _ { i j } = \delta _ { i j }$ i eq.(5.3).In fact,the equation of motion of a test particle with velocity $v$ ,in a gravitational field, is obtained from the geodesic equation

$$
{ \frac { d ^ { 2 } x ^ { i } } { d \tau ^ { 2 } } } = - \Gamma _ { \mu \nu } ^ { i } { \frac { d x ^ { \mu } } { d \tau } } { \frac { d x ^ { \nu } } { d \tau } } .
$$

In a weak gravitational field we write $g _ { \mu \nu } = \eta _ { \mu \nu } + h _ { \mu \nu }$ with $\vert h _ { \mu \nu } \vert \ll 1$ and,in the limit of low velocities,the proper time $\tau$ is the same,to lowest order,as the coordinate time $t$ .Furthermore, $d x ^ { 0 } / d t = c$ while $d x ^ { i } / d t = O ( v )$ ．Then,the leading term in $v / c$ is obtained setting $\mu =$ $\nu = 0$ in eq. (5.8),

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } \simeq - c ^ { 2 } \Gamma _ { 0 0 } ^ { i } } } \\ { { = c ^ { 2 } \left( \frac { 1 } { 2 } \partial ^ { i } h _ { 0 0 } - \partial _ { 0 } h _ { 0 } { } ^ { i } \right) . } } \end{array}
$$

Since we are considering a source moving with non-relativistic velocity, the time derivative of the metric generated by this source is of higher order with respect to the spatial derivatives,so to leading order eq. (5.9) becomes

$$
\frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } = \frac { c ^ { 2 } } { 2 } \partial ^ { i } h _ { 0 0 } .
$$

Writing $h _ { 0 0 } = - 2 \phi$ and defining $U$ by $U = - c ^ { 2 } \phi$ ，we recover the Newtonian equation of motion $\mathbf { a } = \nabla U$ and we see that $U$ is the (signrversed) gravitational potential.8 In a potential $U$ ，the virial theorem lls us that a massive particle moves with a velocity $v ^ { 2 } = O ( U )$ ,s0 $h _ { 0 0 }$ of order $v ^ { 2 } / c ^ { 2 }$ .Comparing with eq. (5.3)， we see that the Newtonian lmit corresponds to $^ { ( 2 ) } g _ { 0 0 } = 2 U / c ^ { 2 }$ ，while all other corrections to the lat metric do not affect the Newtonian equation of motion. Observe in particular that ${ ^ { ( 2 ) } } g _ { i j }$ does not contribute to the Newtonian limit,despite tefacthatitisacorrection $O ( v ^ { 2 } / c ^ { 2 } )$ to the leading term ${ { \bf \Lambda } ^ { ( 0 ) } } g _ { i j } = \delta _ { i j }$ ， justas $^ { ( 2 ) } g _ { 0 0 }$ is a correction $O ( v ^ { 2 } / c ^ { 2 } )$ to the leading term ${ ( 0 ) } _ { g _ { 0 0 } } = { - 1 }$ Ihis is due to the fact that,in the geodesic equation (5.8), $\partial ^ { i } g _ { 0 0 }$ enters through $\Gamma _ { 0 0 } ^ { i }$ ,which is multiplied by $( d x ^ { 0 } / d t ) ^ { 2 } = c ^ { 2 }$ ,while the gradient fthe spatial metric, $\partial ^ { i } g _ { j k }$ ,enters through $\Gamma _ { j k } ^ { i }$ ,which is multiplied by $\mathrm { d } x ^ { j } / d t ) ( d x ^ { k } / d t ) = O ( v ^ { 2 } )$

8It isa nearly universal convention in research papers in general relativity that $U$ denotes the sign-reversed gravitational potential, so that $U > 0$ We will refer to $U$ simply as the potential.

It is worth remarking that here it was crucial that we considered the mopagation of a massive particle with $v / c \ll 1$ .If we rather consider te propagation of a photon in the metric generated by a non-relativistic ource, there is no $v / c$ suppression since $v$ is approximately equal to $c , ^ { 9 }$ id the deviation from fat space in $g _ { 0 0 }$ and in $g _ { i j }$ both contribute to ding order. For instance,the metric generated by a weak and nearly Iitic Newtonian source,in the de Donder gauge, is given by

$$
d s ^ { 2 } \simeq - ( 1 + 2 \phi ) d t ^ { 2 } + ( 1 - 2 \phi ) \delta _ { i j } d x ^ { i } d x ^ { j } ,
$$

9More precisely,v differs fromconlyby terms of order $U / c ^ { 2 }$ where $U$ is given in eq. (5.12) below.

mltere $\phi = - U / c ^ { 2 }$ and

$$
U ( t , { \bf x } ) = \frac { G } { c ^ { 2 } } \int d ^ { 3 } x ^ { \prime } \frac { T ^ { 0 0 } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } .
$$

Ihis is easily proved using eq. (3.8),and observing that for a non-Mativistic source,to leading order in the source velocity，only $T _ { 0 0 }$ conmbutes, so only $\tilde { h } _ { 0 0 }$ is non-vanishingWe neglect retardation effect me we are interested in the near-zone field,and we finally express the sult in terms of $h _ { \mu \nu } = \bar { h } _ { \mu \nu } - ( 1 / 2 ) \eta _ { \mu \nu } \bar { h }$ ） If we study the propagation a photon in such a background,of course both the correction $- 2 \phi$ $\eta _ { 0 0 } = - 1$ and the correction $- 2 \phi \delta _ { i j }$ to $\eta _ { i j } = \delta _ { i j }$ must be taken into rount,and give contributions of the same order.i0

Having established that $g _ { 0 0 } = - 1 + { } ^ { ( 2 ) } g _ { 0 0 }$ $g _ { 0 i } = 0$ and $g _ { i ; j } = \delta _ { i j }$ gives Newtonian approximation to the dynamics of a massive particle, Iblows that the terms $^ { ( 4 ) } g _ { 0 0 }$ $^ { ( 3 ) } g _ { 0 i }$ and ${ ^ { ( 2 ) } } g _ { i j }$ give the first post, $^ { ( 6 ) } g _ { 0 0 } , ~ ^ { ( 5 ) } g _ { 0 i }$ and ${ ^ { ( 4 ) } } g _ { i j }$ s the 2PN approximation, etc.

10When studying the defection of light from the Sun,Einstein at first (in 1911) used the metric

$$
d s ^ { 2 } = - ( 1 + 2 \phi ) d t ^ { 2 } + d { \bf x } ^ { 2 } ,
$$

suggested by the Newtonian limit of a massive particle,and obtained a deflection angle of only one half of the correct value,which is the one obtained from (5.11).Einstein himself obtained the correct deflection angle in 19l5,when he had the final form of his equations.

# 5.1.4 The 1PN order

We now discuss the first post-Newtonian correction.First of all,it is useful to choose from the beginning a gauge condition,since this simplifies drastically the equations.A convenient choice is the De Donder gauge condition,

$$
\partial _ { \mu } ( \sqrt { - g } g ^ { \mu \nu } ) = 0 .
$$

11This name originates from the fact that,in this gauge,the coordinates $x ^ { \rho }$ satisfy

$$
\partial _ { \mu } ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } ) x ^ { \rho } = 0 .
$$

On a scalar function $\phi$ ,in curved space, we have

$$
\begin{array} { l } { { \Theta \phi \equiv D ^ { \mu } D _ { \mu } \phi \qquad } } \\ { { \qquad = \displaystyle \frac { 1 } { \sqrt { - g } } \partial _ { \mu } ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } ) \phi , } } \end{array}
$$

where $D _ { \mu }$ is the covariant derivative, and a scalar function $\phi$ that satisfies $\square \phi = 0$ ,i.e.

$$
\partial _ { \mu } ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } ) \phi = 0 ,
$$

is called a harmonic function．By (a slightly improper） extension,also the coordinates $x ^ { \rho }$ that satisfy (5.14) are called harmonic coordinates (even if $x ^ { \rho }$ are not four scalar functions indexed by $\rho$ ,so the operator $D ^ { \mu } D _ { \mu }$ on them is not the same as on scalars).

We will use the denominations De Donder gauge condition and harmonic gauge condition as synonymous. Sometimes in the literature the name “De Donder gauge condition”is reserved to the linearized form given in eq.(1.18),while“harmonic gauge condition”is reserved to eq.(5.13).

This is also called the harmonic gauge condition,and the corresponding coordinates are referred to as harmonic coordinates.11

It is now in principle straightforward,even if somewhat long,to insert the expansions (5.3) and (5.4) into the Einstein equations,using eq. (5.5) to establish the order of the various term,and the gauge condition (5.13). expanded to the desired order,to simplify the equations (for the explicit computation,see Weinberg $1 \Lsh 7 2$ ,Section 9.1).For $^ { ( 2 ) } g _ { 0 0 }$ we get the Newtonian equation

$$
\nabla ^ { 2 } [ { ^ { ( 2 ) } g _ { 0 0 } } ] = - \frac { 8 \pi G } { c ^ { 4 } } { ^ { ( 0 ) } T ^ { 0 0 } } ,
$$

while,for the1PN correctionsto the metric,we get

$$
\begin{array} { l } { { \displaystyle \nabla ^ { 2 } [ ^ { ( 2 ) } g _ { i j } ] = - \frac { 8 \pi G } { c ^ { 4 } } \delta _ { i j } \ ^ { \phantom { * } } \ ^ { ( 0 ) } T ^ { 0 0 } , \ ~ } } \\ { { \displaystyle \nabla ^ { 2 } [ ^ { ( 3 ) } g _ { 0 i } ] = \frac { 1 6 \pi G } { c ^ { 4 } } \ ^ { ( 1 ) } T ^ { 0 i } , \ ~ } } \\ { { \displaystyle \nabla ^ { 2 } [ ^ { ( 4 ) } g _ { 0 0 } ] = \partial _ { 0 } ^ { 2 } [ ^ { ( 2 ) } g _ { 0 0 } ] + ^ { ( 2 ) } g _ { i j } \partial _ { i } \partial _ { j } [ ^ { ( 2 ) } g _ { 0 0 } ] - \partial _ { t } [ ^ { ( 2 ) } g _ { 0 0 } ] \partial _ { i } [ ^ { ( 2 ) } g _ { 0 0 } ] } } \\ { { \displaystyle ~ - \frac { 8 \pi G } { c ^ { 4 } } \left\{ ^ { ( 2 ) } T ^ { 0 0 } + ^ { ( 2 ) } T ^ { i i } - 2 \ ^ { ( 2 ) } g _ { 0 0 } ^ { _ { ( 0 ) } } T ^ { 0 0 } \right\} , \qquad ( 1 ) \ , } } \end{array}
$$

where $\begin{array} { r } { \nabla ^ { 2 } = \delta ^ { i j } \partial _ { i } \partial _ { j } } \end{array}$ is the fat-space Laplacian,and the sum over re peated lower (or upper) spatial indices is performed with $\delta _ { i j }$ . The solution of eq.(5.17),with the boundary condition that the metric vanishes at spatial infinity,is

$$
{ } ^ { ( 2 ) } g _ { 0 0 } = - 2 \phi ,
$$

where

$$
\phi ( t , { \bf x } ) = - \frac { G } { c ^ { 4 } } \int d ^ { 3 } x ^ { \prime } \frac { { } ^ { ( 0 ) } T ^ { 0 0 } ( t , { \bf x } ^ { \prime } ) } { | { \bf x } - { \bf x } ^ { \prime } | } ,
$$

s0 $U = - c ^ { 2 } \phi$ is the (positive) Newtonian potential. Similarly, the 1PN eqs. (5.18) and (5.19) are immediately solved,

where

$$
\begin{array} { c } { { \displaystyle { { \bf \rho } ^ { ( 2 ) } g _ { i j } = - 2 \phi \delta _ { i j } { \bf \rho } , } } } \\ { { \displaystyle { { \bf \rho } ^ { ( 3 ) } g _ { 0 i } = \zeta _ { i } { \bf \rho } , } } } \\ { { \displaystyle { } } } \\ { { \zeta _ { i } ( t , { \bf x } ) = - \frac { 4 G } { c ^ { 4 } } \int \frac { d ^ { 3 } x ^ { \prime } } { | { \bf x - x ^ { \prime } } | } { \bf \rho } ^ { ( 1 ) } T ^ { 0 i } ( t , { \bf x ^ { \prime } } ) . } } \end{array}
$$

To solve eq.(5.20) we replace on the right-hand side $^ { ( 2 ) } g _ { 0 0 }$ by $- 2 \phi$ and ${ ^ { ( 2 ) } g _ { i j } }$ by $- 2 \phi \delta _ { i j }$ , we use the identity

$$
\partial _ { i } \phi \partial _ { i } \phi = \frac { 1 } { 2 } { \bf { \nabla } } \nabla ^ { 2 } ( \phi ^ { 2 } ) - \phi { \bf { \nabla } } \nabla ^ { 2 } \phi ,
$$

and we introduce a new potential $\psi$ defined from

$$
{ } ^ { ( 4 ) } g _ { 0 0 } = - 2 ( \phi ^ { 2 } + \psi ) .
$$

Then eq. (5.20） becomes

$$
\nabla ^ { 2 } \psi = \partial _ { 0 } ^ { 2 } \phi + \frac { 4 \pi G } { c ^ { 4 } } \left[ { } ^ { ( 2 ) } T ^ { 0 0 } + { } ^ { ( 2 ) } T ^ { i i } \right] ,
$$

which,again with the boundary condition that $\psi$ vanishes at infinity, has the solution

$$
\psi ( t , { \bf x } ) = - \int { \frac { d ^ { 3 } x ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } } \left\{ { \frac { 1 } { 4 \pi } } \partial _ { 0 } ^ { 2 } \phi + { \frac { G } { c ^ { 4 } } } \left[ \left( { } ^ { ( 2 ) } T ^ { 0 0 } ( t , { \bf x } ^ { \prime } ) + { } ^ { ( 2 ) } T ^ { i i } ( t , { \bf x } ^ { \prime } ) \right] \right\} . \right.
$$

Observe that $\phi$ and $\zeta ^ { i }$ are not independent, since the gauge condition q.(5.13) imposes the constraint

$$
4 \partial _ { 0 } \phi + \nabla \cdot \boldsymbol { \zeta } = 0 .
$$

From the explicit cxpressions (5.22) and (5.25) we see that these are indeed satisfied, because of the conservation of the energy-momentum ensor,expanded to 1PN order.

In agreement with the discussion below eq. (5.6), $\phi , \psi$ and $\zeta _ { i }$ are intantaneous potentials: their value at time $t$ depends on the value of the nergy-momentum tensor at the same time $t$ ,rather than at retarded lime. However,we can re-express the solution in terms of retarded polentials.This is useful both to understand better the structure of the bove solution,and as a starting point for the computation of higher ost-Newtonian orders. We begin by observing that，putting together qs. (5.21) and (5.27), we have

$$
\begin{array} { r l r } & { } & { g _ { 0 0 } = - 1 - 2 \phi - 2 ( \phi ^ { 2 } + \psi ) + O ( \epsilon ^ { 6 } ) \quad } \\ & { } & { = - 1 - 2 ( \phi + \psi ) - 2 \phi ^ { 2 } + O ( \epsilon ^ { 6 } ) . } \end{array}
$$

since $\psi$ is of higher order compared to $\phi$ ,in the last term we are free o replace $\phi ^ { 2 }$ by $( \phi + \psi ) ^ { 2 }$ ,because the additional terms are beyond the PN order anyway. We introduce the quantity

$$
V = - c ^ { 2 } ( \phi + \not \psi ) ,
$$

Thich has the dimension of a velocity squared,so the solution for goo, 1PN order,can be written as

$$
g _ { 0 0 } = - 1 + \frac { 2 V } { c ^ { 2 } } - \frac { 2 V ^ { 2 } } { c ^ { 4 } } + O \left( \frac { 1 } { c ^ { 6 } } \right) .
$$

We will often follw the convention,common in the literature on the W expansion, of writing the remainder as $O ( 1 / c ^ { n } )$ rather than $O ( \epsilon ^ { n } )$ ） i0 this order,this can be written more compactly as

$$
g _ { 0 0 } = - { \epsilon } ^ { - 2 V / c ^ { 2 } } + \phi \left( \frac { 1 } { c ^ { 6 } } \right) .
$$

The potential $\phi$ satisfies

$$
{ \nabla ^ { 2 } } \phi = { \frac { 4 \pi G } { c ^ { 4 } } } { \ v { D } } ^ { ( 0 ) } { T ^ { 0 0 } } ,
$$

see eqs. (5.17) and (5.21), while $\psi$ satisfies eq. (5.28). Thus,

$$
\nabla ^ { 2 } ( \phi + \psi ) = \partial _ { 0 } ^ { 2 } \phi + \frac { 4 \pi G } { c ^ { 4 } } \left[ { } ^ { ( 0 ) } T ^ { 0 0 } + { } ^ { ( 2 ) } T ^ { 0 0 } + { } ^ { ( 2 ) } T ^ { i i } \right] .
$$

To this order, $\partial _ { 0 } ^ { 2 } \phi = \partial _ { 0 } ^ { 2 } ( \phi + \psi )$ , so the above equation can be written in terms of the flat-space d'Alembertian $\Pi = \eta ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu }$ ,as

$$
\begin{array} { l } { { \Theta { \cal { V } } = - { \displaystyle \frac { 4 \pi G } { c ^ { 2 } } } [ ( ^ { ( 0 ) } T ^ { 0 0 } + ^ { ( 2 ) } T ^ { 0 0 } + ^ { ( 2 ) } T ^ { i i } ] } } \\ { { \mathrm { ~ } = - { \displaystyle \frac { 4 \pi G } { c ^ { 2 } } } [ T ^ { 0 0 } + T ^ { i i } ] , } } \end{array}
$$

12Actually，the PNsolutioncould be rewritten equivalently in terms of the advanced integral or of any combination of retarded and advanced Green's functions. What really selects the appropriate Green's function are the boundary conditions.In particular,the retarded Green's function is selected by the no-incoming radiation boundary condition at null infinity.However,we have already seen in eq. (5.7) that the PN expansion only holds in the near region $r \ll \lambda$ and therefore, within the PN expansion,it is not possible to impose boundary conditions at infinity.As we will see below,a different approximation scheme,the post-Minkowskian expansion，will be employed in the external source region $d < r < \infty$ ,and the boundary condition will be consistently imposed on the post-Minkowskian solution,and will select the retarded Green's function. The PN solution and the post-Minkowskian solution will then be matched in the overlap region $d < r \ll \aleph $ .Even if the PN expansion at a given order could be rewritten in many different forms, e.g. in terms of advanced potentials,or of half-advanced and half-retarded potentials,writing it in terms of retarded Green's function makes it possible the matching,since the post-Minkowskian solutions in $d < r < \infty$ will be unambiguously written in terms of retarded potentials,once the no-incoming radiation boundary condition is imposed on it.

where, to 1PN order，we could replace $^ { ( 0 ) } T ^ { 0 0 } + ^ { ( 2 ) } T ^ { 0 0 }$ with the total value of the O0 component of the energy-momentum tensor, $T ^ { 0 0 }$ , and similarly ${ ( 2 ) } _ { T ^ { i i } }$ with $T ^ { i i }$ . Weuse the active gravitational-mass density defined in eq. (3.205). Then the 1PN equation for $g _ { 0 0 }$ can be written as

$$
\mathsf { \Pi } \sqcup _ { V = - 4 \pi G \sigma , }
$$

and therefore $V ( t , { \bf x } )$ can be written as a retarded integral,as12

$$
\overline { { V ( t , { \bf x } ) = G } } \int d ^ { 3 } x ^ { \prime } \frac { 1 } { | { \bf x } - { \bf x } ^ { \prime } | } \sigma ( t - | { \bf x } - { \bf x } ^ { \prime } | / c , { \bf x } ^ { \prime } ) .
$$

This retarded potential can be written in terms of instantaneous potentials expanding $\sigma ( t - | \mathbf x - \mathbf x ^ { \prime } | / c , \mathbf x ^ { \prime } )$ for small retardation effects,

$$
\sigma ( t - | \mathbf x - \mathbf x ^ { \prime } | / c , \mathbf x ^ { \prime } ) = \sigma ( t , \mathbf x ^ { \prime } ) - \frac { | \mathbf x - \mathbf x ^ { \prime } | } { c } \partial _ { t } \sigma + \frac { | \mathbf x - \mathbf x ^ { \prime } | ^ { 2 } } { 2 c ^ { 2 } } \partial _ { t } ^ { 2 } \sigma + \dots ,
$$

and of course,given that we are working to 1PN order,for the moment we can only retain the result $\dot { \phi \mathrm { f } }$ this expansion,truncated to 1PN order. We can proceed similarly for $\dot { g } _ { 0 i }$ and $g _ { i j }$ . Using the“active mass-current density”defined in eq. $( 3 . 2 0 \dot { 6 } )$ ，and observing that in $\zeta _ { i }$ retardation effects are anyway of higher order,we are allowed to rewrite eqs. (5.24) and (5.25),to 1PN order,replacing $\zeta _ { i }$ with $V _ { i }$ defined by

$$
\overline { { V _ { i } ( t , { \bf x } ) = G \int d ^ { 3 } x ^ { \prime } \frac { 1 } { \vert { \bf x - x ^ { \prime } } \vert } \sigma _ { i } ( t - \vert { \bf x - x ^ { \prime } } \vert / c , { \bf x ^ { \prime } } ) , } }
$$

and similarly we can replace $- c ^ { 2 } \phi$ with $V$ in the solution for $g _ { i j }$ ,since again the difference is of higher order.

To summarize,in harmonic|coordinates the 1PN solution can be writ ten in terms of two functions $V$ and $V _ { i }$ as

$$
g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } V - \frac { 2 } { c ^ { 4 } } V ^ { 2 } + O \left( \frac { 1 } { c ^ { 6 } } \right) ,
$$

$$
\begin{array} { l } { { g _ { 0 i } = - \displaystyle \frac { 4 } { c ^ { 3 } } V _ { i } + { \cal O } ( \displaystyle \frac { 1 } { c ^ { 5 } } ) \displaystyle ) , } } \\ { { g _ { i j } = \delta _ { i j } ( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } V ) + { \cal O } ( \displaystyle \frac { 1 } { c ^ { 4 } } ) , } } \end{array}
$$

and $V , V _ { i }$ are given by retarded integrals over the energy-momentum tensor of the source,eqs. (5.39) and (5.41). Observe also that, to this order,the energy-momentum tensor of the source enters only through ihe two combinations $\sigma$ and $\sigma _ { i }$

At large distance from the source,i.e. at $r \gg d$ ，we can expand the potentials $V$ and $V _ { i }$ using

$$
{ \frac { 1 } { \left| \mathbf { x } - \mathbf { x } ^ { \prime } \right| } } = { \frac { 1 } { r } } + { \frac { \mathbf { x } { \cdot } \mathbf { x } ^ { \prime } } { r ^ { 3 } } } + \ldots ,
$$

where $r = | \mathbf { x } |$ ,and we find that the gravitational field at $d \ll r$ (but still vithin the near region, $r \ll \lambda$ ） is expressed in terms of the multipoles f the energy-momentum tensor of the source. We will examine this maltipole expansion in more detail in Section 5.3.2.

# 5.1.5 Motion of test particles in the PN metric

Unce we have the metric in the near zone,we can obtain the equations motion of a particle of mass $m$ which moves in the near zone from e geodesic equation or,equivalently，writing the action in the given irved background,

$$
\begin{array} { l } { { S = - m c \displaystyle \int d t \left( - g _ { \mu \nu } \frac { d x ^ { \mu } } { d t } \frac { d x ^ { \nu } } { d t } \right) ^ { 1 / 2 } } } \\ { { = - m c ^ { 2 } \displaystyle \int d t \left( - g _ { 0 0 } - 2 g _ { 0 i } \frac { v ^ { i } } { c } - g _ { i j } \frac { v ^ { i } v ^ { j } } { c ^ { 2 } } \right) ^ { 1 / 2 } , } } \end{array}
$$

ilextremizing it.We will be particularly interested in the equations of tion for a binary system. If we limit ourselves to the lowest PN cormtions,it is possible to treat the two masses as point-like.13 In curved mce,the energy-momentum tensor of a set of point-like particles with isses $m _ { a }$ and coordinates $x _ { a } ^ { \mu }$ $( a = 1 , 2 )$ is

$$
T ^ { \mu \nu } = \frac { 1 } { \sqrt { - g } } \sum _ { a } \gamma _ { a } m _ { a } \frac { d x _ { a } ^ { \mu } } { d t } \frac { d x _ { a } ^ { \nu } } { d t } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { a } ( t ) ) ,
$$

ich generalizes the flat-space expression (3.121). In a $N$ -body system, metric felt bya particle,labeled as $b$ ,is obtained taking as a source energy-momentum tensorof alltheother particles,i.e.eplacing $\textstyle \sum _ { a }$ Eath in eq. (5.47).14 Expanding the determinant of the metric to rond order and using eqs. (5.21) and(5.23) we get

$$
\begin{array} { c } { { \displaystyle - g = 1 - ^ { ( 2 ) } g _ { 0 0 } + \sum _ { i } { } ^ { ( 2 ) } g _ { i j } } } \\ { { = 1 - 4 \phi . } } \end{array}
$$

13In higher order,some regularization of the Dirac delta becomes necessary. See Section 8 of Blanchet (2006）and the Further Reading for a discussion of the various regularizations which have been used.

14Forradiation reaction,a self-force must also be included.However,we will see below that radiation reaction effects enter only in higher orders,and will be discussed in Section 5.3.5.

Then the expansion of eq. (5.47) (with∑→£a≠b) gives

$$
\begin{array} { l } { { \displaystyle { } ^ { ( 0 ) } T ^ { 0 0 } ( t , { \bf x } ) = \sum _ { a \neq b } m _ { a } c ^ { 2 } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { a } ( t ) ) , } } \\ { { \displaystyle { } ^ { ( 2 ) } T ^ { 0 0 } ( t , { \bf x } ) = \sum _ { a \neq b } m _ { a } ( \frac { | 1 } { \int _ { 2 } } v _ { a } ^ { 2 } + 2 \phi c ^ { 2 } ) \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { a } ( t ) ) , } } \\ { { \displaystyle { } ^ { ( 1 ) } T ^ { 0 i } ( t , { \bf x } ) = c \sum _ { a \neq b } m _ { a } v _ { a } ^ { i } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { a } ( t ) ) , } } \\ { { \displaystyle { } ^ { ( 2 ) } T ^ { i j } ( t , { \bf x } ) = \sum _ { a \neq b } m _ { a } v _ { a } ^ { i } v _ { a } ^ { j } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { a } ( t ) ) . } } \end{array}
$$

Plugging these expressions into eqs.(5.22)-(5.29) we obtain the metrici which the particle b propagates and,inserting this metric into eq. (5.46) we get its action,Sb. The totalaction of the system is the sum over ll particles,S = ∑b Sb. Expanding the square root in the action and keeping for consistency only terms up to O(u4/c4） gives the first post Newtonian corrections. In terms of the Lagrangian, the result for two-body system is L=Lo+(1/c²)L2,with

$$
L _ { 0 } = { \frac { 1 } { 2 } } m _ { 1 } v _ { 1 } ^ { 2 } \big | + { \frac { 1 } { 2 } } m _ { 2 } v _ { 2 } ^ { 2 } + { \frac { G m _ { 1 } m _ { 2 } } { r } } ,
$$

and

$$
\begin{array} { c } { { L _ { 2 } = { \displaystyle \frac { 1 } { 8 } } m _ { 1 } v _ { 1 } ^ { 4 } + { \displaystyle \frac { 1 } { 8 } } m _ { 2 } v _ { 2 } ^ { 4 } } } \\ { { + { \displaystyle \frac { G m _ { 1 } m _ { 2 } } { 2 r } } \left[ 3 ( v _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 } ) - 7 { \bf v } _ { 1 } { \bf \cdot v } _ { 2 } - ( \hat { \bf r } { \bf \cdot v } _ { 1 } ) ( \hat { \bf r } { \bf \cdot v } _ { 2 } ) - { \displaystyle \frac { G ( m _ { 1 } + m _ { 2 } ) } { r } } \right] } } \end{array}
$$

where r is the separation vectpr between the two particles,r = ram r=r/r. The same computatidn can be repeated for a system of N parti $\hat { \mathbf { r } } = \mathbf { r } / r$ cles,and the result is the famous Einstein-Infeld-Hoffmann Lagrangian L=Lo+(1/c²)L2 with

$$
L _ { 0 } = \sum _ { a } { \frac { \textstyle 1 } { 2 } } m _ { a } v _ { a } ^ { 2 } + \sum _ { a \ne b } { \frac { G m _ { a } m _ { b } } { 2 r _ { a b } } } ,
$$

and

$$
\begin{array} { c } { { \displaystyle { \cal L } _ { 2 } = \sum _ { a } \frac { 1 } { 8 } m _ { a } v _ { a } ^ { 4 } - \sum _ { a \neq b } ^ { } \frac { G m _ { a } m _ { b } } { 4 r _ { a b } } [ 7 { \bf v } _ { a } \cdot { \bf v } _ { b } + ( \hat { \bf r } _ { a b } \cdot { \bf v } _ { a } ) ( \hat { \bf r } _ { a b } \cdot { \bf v } _ { b } ) ] } } \\ { { + \displaystyle \frac { 3 G } { 2 } \sum _ { a } \sum _ { b \neq a } \frac { m _ { a } m _ { b } v _ { a } ^ { 2 } } { \eta _ { a b } } - \frac { G ^ { 2 } } { 2 } \sum _ { a } \sum _ { b \neq a } \sum _ { c \neq a } ^ { } \frac { m _ { a } m _ { b } m _ { c } } { r _ { a b } r _ { a c } } , } } \end{array}
$$

where a = 1,...,N labels the particle,rab is the distance between parl cles a and b,and rab the unit vector from a to b.From this Lagrangin we can derive the equations of motion of a N-particle system, includimg corrections of order u²/c²,i.e. to 1PN order.If one rather performs tl expansion up to 2PN order,the equation of motion of a binary system takes the schematic form

$$
\frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } = - \frac { G m } { r ^ { 2 } } \{ \hat { x } ^ { i } [ 1 + O ( \epsilon ^ { 2 } ) + O ( \epsilon ^ { 4 } ) ]  + \hat { v } ^ { i } [ O ( \epsilon ^ { 2 } ) + O ( \epsilon ^ { 4 } ) ] \} ,
$$

where $m$ is the total mass,x is the relative separation, ${ \hat { x } } ^ { i } = x ^ { i } / r$ ,and $\hat { v } ^ { i }$ is the unit vector in the direction of the relative velocity. The leading term is of course just Newtonian gravity， The terms $O ( \epsilon ^ { 2 } )$ are the 1PN correction to the equations of motion which gives rise,for instance,to the periastron advance of the orbit. The terms $O ( \epsilon ^ { 4 } )$ comes from the 2PN correction. The explicit integration of the 1PN equations of motion for a binary system will be discussed in Chapter 6,on pages 317-320, when we need it for the timing formula of binary pulsars.

# 5.1.6Difficulties of the PN expansion

The straightforward PN expansion that|we have presented,and which was used until,say, the early 198Os,suffers from two serious problems. The first is that,beyond some order,divetgences appear.We will see this explicitly in eq. (5.199),and in the discussion below it.However,it is useful to understand first qualitatively the essence of the problem,which is rooted in the fact that general relativity isa non-linear theory. We are trying to solve iteratively the Einstein equations,that have schematically the form

$$
\begin{array} { r } { \left. \begin{array} { c } { \qquad } \\ { \neg h _ { \mu \nu } = S _ { \mu \nu } [ h ] , } \end{array} \right. } \end{array}
$$

where $S _ { \mu \nu }$ is a source term,that depends both on the matter energymomentum tensor and,non-linearly,on $h _ { \mu \nu }$ (we will see in eq. (5.72) below how to write exactly the Einstein equations in this form).One ould envisage a systematic weak-field,low-velocity expansion as follows. We write

$$
h _ { \mu \nu } = { } ^ { ( 0 ) } h _ { \mu \nu } + { } ^ { ( 1 ) } h _ { \mu \nu } + { } ^ { ( 2 ) } h _ { \mu \nu } + \ldots .
$$

$7 0$ zeroth order， we simply set $^ { ( 0 ) } h _ { \mu \nu } \ = \ 0$ The first-order solution, $1 h _ { \mu \nu }$ ,is obtained setting $h _ { \mu \nu } = 0$ on the right-hand side of eq. (5.58), hile,according to eq. (5.5),on the left-hand side we neglect the timelerivative. Then we get an equation of the form

$$
\bar { \nabla } ^ { 2 } [ ^ { ( 1 ) } h _ { \mu \nu } ] = \left( \mathrm { m a t t e r ~ s o u r c e s } \right) .
$$

This is integrated by making use of the instantaneous Green's function oithe Laplacian,i.e. of the Poisson integral defined ona generic function $( x )$ by

$$
[ \Delta ^ { - 1 } f ] ( { \bf x } ) \equiv - { \frac { 1 } { 4 \pi } } \int _ { \mathbb { R } ^ { 3 } } { \frac { d ^ { 3 } x ^ { \prime } } { \vert { \bf x } - { \bf x } ^ { \prime } \vert } } f ( { \bf x } ^ { \prime } ) ,
$$

where $\Delta \equiv \nabla ^ { 2 }$ )and leads to results such as eq. (5.22). At next order, me insert $^ { ( 1 ) } h _ { \mu \nu }$ into $S [ h ]$ while, in $\square h _ { \mu \nu }$ ,we replace $\partial _ { 0 } ^ { 2 } h _ { \mu \nu }$ by $\partial _ { 0 } ^ { 2 } [ ^ { ( 1 ) } h _ { \mu \nu } ]$ ， othe gravitationalfeld at the next iteration, $^ { ( 2 ) } h _ { \mu \nu } \qquad $ ,is determined by nequation of the form

$$
\bar { \nabla } ^ { 2 } [ ^ { ( 2 ) } h _ { \mu \nu } ] = \left( \mathrm { m a t t e r ~ s o u r c e s } \right) + \left( \mathrm { t e r m s ~ } \mathrm { ( t h a t ~ d e p e n d ~ o n ~ } ^ { ( 1 ) } h _ { \mu \nu } \right) ,
$$

which again one would attempt|to integrate by using the Poisson inte gral.The problem is that, beyond some order, the resulting Poisson inte grals are necessarily divergent.In fact,first of all,even if the source has a compact support,the second term on the right-hand side of eq.(5.62) extends all over the space,raising an issue of convergence at infinity of the Poisson integral. Furthermore,the higher is the PN order,th higher is also the order of the multipoles that contribute.The gravita tional field corresponding to a multipole of order $\it l$ has a factor $( \mathbf { x } \cdot \mathbf { x } ^ { \prime } )$ which comes from the expansion of $1 / | \mathbf { x } - \mathbf { x } ^ { \prime } |$ in eq. (5.45).When w use such a feld as a source for the next iteration, for $\it l$ sufficiently larg we necessarily get a divergence at large $\mathbf { x } ^ { \prime }$ in the retarded intcgral.15

15In the earlier works this problem was somehow swept under the rug. The reason is that divergences start to appear only from 2PN order. Furthermore,up to $2 . 5 \mathrm { P N }$ order,the result can be made finite by using some not well justified trick,consisting in bringing some derivative inside the integrals,to make them finite.In this way,early papers managed to get the lowest-order results that nowadays we know to be correct.However,inexorably divergent integrals appear at 3PN order. Therefore this approach is not consistent,and even the validity of the lowest-order results becomes highly questionable.

This problems turns out to be purely technical. Simply, the correc solution to the Poisson equation is not necessarily given by the Poisson integral (5.61).The correct solution is fixed by the boundary conditions and we will see in Section $5 . 3 . { \frac { \mathrm { \partial } } { \mathrm { \partial } t } }$ that in our problem it is given by i procedure of analytic continuatfon, that reduces to a Poisson integra only when the latter is convergent,and otherwise is different,and i always finite.

The second problem of the “standard” PN expansion is conceptual and is that it cannot take into account the boundary conditions at in finity. This can be understood by observing that,as already discused below eq. (5.7)，in the PN expansion we are trying to reconstruct a retarded field,say of the form

$$
h _ { \mu \nu } = { \frac { 1 } { r } } F _ { \mu \nu } ( t - r / c ) ,
$$

from its expansions for smallretardation, $r / c \ll t$ ，

$$
\frac { 1 } { r } F _ { \mu \nu } ( t - r / c ) = \frac { 1 } { r } F _ { \mu \nu } ( t ) - \frac { 1 } { c } \dot { F } _ { \mu \nu } ( t ) + \frac { r } { 2 c ^ { 2 } } \ddot { F } _ { \mu \nu } ( t ) - \frac { r ^ { 2 } } { 6 c ^ { 3 } } \dddot { F } _ { \mu \nu } ( t ) + \ldots ,
$$

The coefficients of the higher-order terms therefore blow up as $r \to \infty$ This has nothing to do with thereal behavior of the gravitational field at infinity,which should be asymptotically flat,and simply reflects the inadequacy of the PN expansion to study the large $r$ region.

From a mathematical point of view, the PN expansion is an exampleol singular perturbation theory,or asymptotic expansion,i.e. an expansion of a function $F ( r , \epsilon )$ around $\epsilon = 0$ ，

$$
F ( r , \epsilon ) \equiv \sum _ { n } c _ { n } ( r ) \epsilon ^ { n } ,
$$

where the coefficients $c _ { n }$ depend on a second parameter,here $r$ ,and they blow up as $r  \infty$ . So,this expansion is not uniformly valid in $r _ { \mathrm { \ell } }$ and cannot be used at $r  \infty$ .In particular,as we already observed in Note 12,it is impossible to include in the PN expansion the boundary conditions at infinity, such as the no-incoming radiation boundary condition,appropriate for a radiation problem.16

The solution to this difficulty，,as we will discuss in details in the following sections,is to make use of the PN expansion only in the nea region,and to use a different expansion in the far region.Then, the two expansions are matched in an intermediate region,where they are both valid.This procedure is known as“matched asymptotic expansion”. The appropriate boundary conditions at infinity will then be imposed on the solution valid in the far zone.

# 5.1.7The effect of back-reaction

Once we will have developed a systematic and consistent formalism for computing the gravitational field both in the near and in the far region, we will also be able to compute the modification of the equations of motion of the sources, due to the back-reaction of GWs. Before entering imto the technical aspects,however,we can understand with physical arguments what sort of result we should expect.

When we include gravitational radiation the structure of the expansion changes,because invariance under time-reversal is broken by the boundary conditions. To study GWs we impose that there is no incoming radiation at $t = - \infty$ (compare with Note 1 on page l02). Time teversal exchanges outgoing waves with incoming waves,so the argument used above to prove that $g _ { 0 0 }$ and $g _ { i j }$ are even and that $g _ { 0 i }$ is odd $v$ breaks down. Radiation reaction can generate terms in $g _ { 0 0 }$ which re odd in $v$ (and cannot be gauged away） and,correspondingly, even erns in $g _ { 0 i }$ and odd terms in $g _ { i j }$ 17

It is not difficult to understand to whichlorder in $v / c$ radiation reaction ffects should come into play. We saw in Chapter 3 that the power radi-Mted in GWs by a system with typical velocity $v$ is $P \sim G m ^ { 2 } v ^ { 6 } / ( c ^ { 5 } r ^ { 2 } )$ ， where $m$ is a mass scale of the system and $r$ its size,see e.g.eq.(3.339). On the other hand,writing the total energy of the system as the sum fits kinetic and potential energy, $E _ { \mathrm { t o t } } = E _ { \mathrm { k i n } } + V$ ,and using the virial theorem $E _ { \mathrm { k i n } } = - ( 1 / 2 ) V$ we have $E _ { \mathrm { t o t } } \ : = \ : - E _ { \mathrm { k i n } } = - ( 1 / 2 ) m v ^ { 2 }$ If we quate the time derivative of $E _ { \mathrm { t o t } }$ to minus the power radiated in GWs re thercfore get, neglecting numerical factors,

17In higher orders，because of nonlinearities,radiation reaction will also contribute to terms in goo which are even.We will see in eq.(5.186) that an even contribution to $g _ { 0 0 }$ due to backreaction indeed appears at 4PN order. Thus，beyond 4PN order，all terms (even and odd) contain pieces associated to radiation reaction.

$$
\begin{array} { c } { { } } \\ { { \displaystyle - m v \frac { d v } { d t } \sim - \frac { G m ^ { 2 } v ^ { 6 } } { c ^ { 5 } r ^ { 2 } } , } } \\ { { \displaystyle \frac { d v } { d t } \sim \frac { G m } { r ^ { 2 } } \left( \frac { v } { c } \right) ^ { 5 } . } } \end{array}
$$

Ius,we expect that radiation-reaction efects enter eq. (5.57) starting from ${ \cal O } ( v ^ { 5 } / c ^ { 5 } ) = { \cal O } ( \epsilon ^ { 5 } )$ ,so the equation of motion of a binary system hould be of the generic form

$$
\begin{array}{c} \frac { d ^ { 2 } x ^ { i } } { d t ^ { 2 } } = - \frac { G m } { r ^ { 2 } } \left\{ \hat { x } ^ { i } \left[ 1 + O ( \epsilon ^ { 2 } ) + O ( \epsilon ^ { 4 } ) + O ( \epsilon ^ { 5 } ) + O ( \epsilon ^ { 6 } ) \ldots \right] \right.  \\ { \left. + \hat { v } ^ { i } \left[ O ( \epsilon ^ { 2 } ) + O ( \epsilon ^ { 4 } ) + O ( \epsilon ^ { 5 } ) + O ( \epsilon ^ { 6 } ) + \ldots \right] \right\} . } \end{array}
$$

Given that one traditionally uses the power of $( \upsilon / c ) ^ { 2 }$ to label the PN rder, the term $O ( \epsilon ^ { 5 } )$ is called the correction to the equations of motion order 2.5PN, the term $O ( \epsilon ^ { 6 } )$ is the 3PN order,etc.We willsee in the xt sections how to derive these results.

# 5.2The relaxed Einstein equations

First of all, we recast Einstein equations in a form which willbe partic ularly convenient.From the metric $g ^ { \alpha \beta } ( x )$ ，we define the feld $\mathsf { h } ^ { \alpha \beta } ( { \boldsymbol { x } } _ { }$ by

$$
{ \overline { { \mathsf { h } ^ { \alpha \beta } \equiv \bigl | ( - g ) ^ { 1 / 2 } g ^ { \alpha \beta } - \eta ^ { \alpha \beta } , } } }
$$

18The quantity $( - g ) ^ { 1 / 2 } g ^ { \alpha \beta }$ isalso called the“gothic metric”,and denoted by a gothic $g$ ,see Landau and Lifshitz, Vol.II (1979), Section 96.

where,as usual, $g$ is the deteiminant of $g _ { \alpha \beta }$ .This is an exact definition and we are not assuming that $\hslash _ { \alpha \beta }$ is small. Observe that we use the typographical symbol $\hslash _ { \alpha \beta }$ to distinguish it from $h _ { \alpha \beta }$ ，which israther defined by $g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta } + \vert O ( h ^ { 2 } )$ .18 In the limit of small $h _ { \alpha \beta }$ we havw $- g = ( 1 + h )$ ，where $h = \eta ^ { \mu \nu } h _ { \mu \nu }$ ,and $g ^ { \alpha \beta } = \eta ^ { \alpha \beta } - h ^ { \alpha \beta }$ ,s0

$$
\begin{array} { c } { { - \mathsf { h } ^ { \alpha \beta } \simeq \eta ^ { \alpha \beta } \bigl | - ( 1 + h ) ^ { 1 / 2 } \bigl ( \eta ^ { \alpha \beta } - h ^ { \alpha \beta } \bigr ) } } \\ { { = h ^ { \alpha \beta } \bigl | - \frac { 1 } { 2 } \eta ^ { \alpha \beta } h . } } \end{array}
$$

$^ { 1 9 } \mathrm { F o r }$ this reason,in theliterature $\hbar ^ { \alpha \beta }$ is sometimes defined with the opposite sign, i.e. $\mathsf { h } ^ { \alpha \beta } \equiv \eta ^ { \alpha \beta } - ( - g ) ^ { 1 / 2 } g ^ { \hat { \alpha } \hat { \beta } }$ We use the definition (5.69),following the notation of the review Blanchet (2006). This means that,when we compare the results of this chapter with the corresponding linearized limit studied in the previous chapters,we must take into account this overall sign in the GW amplitude.For the same reason,the sign on the right-hand side of eq.(5.72) below is the opposite of that in eq.(1.24).

Thus, $\mathsf { h } ^ { \alpha \beta }$ reduces to the quantity $\bar { h } ^ { \alpha \beta }$ used in linearized theory,se eq. (1.15), except for an overallsign.19 We now impose the de Donder or harmonic,gauge condition(5.13),which in terms of $\mathsf { h } ^ { \alpha \beta }$ reads

In this gauge the exact Einstein equations (1.3) take the Landau-Lifshit form

<table><tr><td>□ha</td><td>16πG 十 QB c4</td><td>，</td></tr></table>

where $\Pi \equiv - \partial ^ { 2 } / \partial t ^ { 2 } + \nabla ^ { 2 }$ is the d'Alembertian in flat space-time. Th quantity on the right-hand side is defined by

$$
\overline { { { \tau ^ { \alpha \beta } \equiv ( - g ) T ^ { \alpha \beta } + \frac { c ^ { 4 } } { 1 6 \pi G } \Lambda ^ { \alpha \beta } , } } }
$$

where $T ^ { \alpha \beta }$ is the matter energy-momentum tensor. The tensor $\Lambda ^ { \alpha \beta }$ does not depend on the matter variables,and is defined by

$$
\Lambda ^ { \alpha \beta } = \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { L L } ^ { \alpha \beta } + ( \partial _ { \nu } \mathfrak { h } ^ { \alpha \mu } \partial _ { \mu } \mathfrak { h } ^ { \beta \nu } - \mathfrak { h } ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } \mathfrak { h } ^ { \alpha \beta } ) ,
$$

where $t _ { L L } ^ { \alpha \beta }$ is caled teLanda-Lifshitzeergmomentmpsedte sor,

$$
\begin{array} { l } { { { \displaystyle \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { L L } ^ { \alpha \beta } = g _ { \lambda \mu } g ^ { \nu \rho } \partial _ { \nu } \mathfrak { h } ^ { \alpha \lambda } \partial _ { \rho } \mathfrak { h } ^ { \beta \mu } + \displaystyle \frac { 1 } { 2 } g _ { \lambda \mu } g ^ { \alpha \beta } \partial _ { \rho } \mathfrak { h } ^ { \lambda \nu } \partial _ { \nu } \mathfrak { h } ^ { \rho \mu } } \ ~ } } \\ { { \displaystyle \qquad - g _ { \mu \nu } ( g ^ { \lambda \alpha } \partial _ { \rho } \mathfrak { h } ^ { \beta \nu } + g ^ { \lambda \beta } \partial _ { \rho } \mathfrak { h } ^ { \alpha \nu } ) \partial _ { \lambda } \mathfrak { h } ^ { \rho \mu } } \ ~ } \\ { { \displaystyle \qquad + \frac { 1 } { 8 } ( 2 g ^ { \alpha \lambda } g ^ { \beta \mu } - g ^ { \alpha \beta } g ^ { \lambda \mu } ) ( 2 g _ { \nu \rho } g _ { \sigma \tau } - g _ { \rho \sigma } g _ { \nu \tau } ) \partial _ { \lambda } \mathfrak { h } ^ { \nu \tau } \partial _ { \mu } \mathfrak { h } ^ { \rho \sigma } } . } \end{array}
$$

Since $t _ { L L } ^ { \alpha \beta }$ depends explitly on the meti $g _ { \mu \nu }$ ,it is a highly on-linear function of $\mathsf { h } _ { \mu \nu }$ .Using the De Donder gauge condition,we see that the last term in eq. (5.74) is a divergence,

$$
\partial _ { \nu } \mathfrak { h } ^ { \alpha \mu } \partial _ { \mu } \mathfrak { h } ^ { \beta \nu } - \mathfrak { h } ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } \mathfrak { h } ^ { \alpha \beta } = \partial _ { \mu } \partial _ { \nu } ( \mathfrak { h } ^ { \alpha \mu } \mathfrak { h } ^ { \beta \nu } - \mathfrak { h } ^ { \mu \nu } \mathfrak { h } ^ { \alpha \beta } ) .
$$

Thus, we can also rewrite eq. (5.72) as

$$
\mathtt { O h } ^ { \alpha \beta } = + \frac { 1 6 \pi G } { c ^ { 4 } } \left[ ( - g ) ( T ^ { \alpha \beta } + t _ { L L } ^ { \alpha \beta } ) + \partial _ { \mu } \partial _ { \nu } \chi ^ { \alpha \beta \mu \nu } \right] ,
$$

where

$$
\chi ^ { \alpha \beta \mu \nu } = \frac { c ^ { 4 } } { 1 6 \pi G } ( \mathsf { h } ^ { \alpha \mu } \mathsf { h } ^ { \beta \nu } \vdash \mathsf { h } ^ { \mu \nu } \mathsf { h } ^ { \alpha \beta } ) .
$$

The important point is that eqs.(5.71) and (5.72) are an exact way of recasting the Einstein equations (subject to the assumption that all of space-time can be covered by a harmonic coordinate system),and no approximation has been made yet.20

Compare this with the standard form of Einstein equations,

$$
G _ { \alpha \beta } = \frac { 8 \pi G } { c ^ { 4 } } T _ { \alpha \beta } ,
$$

where

$$
G _ { \alpha \beta } = R _ { \alpha \beta } - \frac { 1 } { 2 } g _ { \alpha \beta } R
$$

the Einstein tensor. Because of the Bianchi identity $D _ { \beta } G ^ { \alpha \beta } = 0$ ， 4.(5.79)implies automatically the covariant conservation of the matter mergy-momentum tensor,

$$
D _ { \beta } T ^ { \alpha \beta } = 0 .
$$

I turn,eq. (5.81) is an equation of motion for the matter variables. lus,Einstein equations automatically fix the motion of matter. Ein-Mein equations are completely equivalent to eq. (5.72) together with 0.(5.71). However,from a mathematical point of view it makes peretly sense to first solve eq.(5.72) without requiring, for the moment, at eq.(5.71) be satisfied.Then eq. (5.72),alone,does not constraint he dynamics of the matter variables. In principle,we could assign ourelves an arbitrary time dependence to $T ^ { \alpha \beta }$ ,and the equation would still be well defined. For this reason,the 10 tensor components of eq. (5.72) e called the relaxed Einstein equations;we have relaxed the condition mat the matter variables obey their equations of motion. Of course, lis condition must be recovered when,on|the solutions of eq. (5.72), we mpose eq. (5.71),since the two equations,together,are equivalent to e Einstein equations. Indeed,the gauge condition (5.71) implies that satisfies the conservation law

$$
\partial _ { \beta } \tau ^ { \alpha \beta } = 0 ,
$$

ith an ordinary，rather than covariant derivative,and this turns out be fully equivalent to eq. (5.81). Thus,if we first solve eq. (5.72),

20At first sight eq. (5.72) is surprising, since it seems to suggest that $\mathsf { h } _ { \mu \nu }$ propagates along the light-cone offlat spacetime,because on the left-hand side we have the flat-space d'Alembertian. Actually,this is not true because in $\Lambda ^ { \alpha \beta }$ we have the term $\mathsf { h } ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } \mathsf { h } ^ { \alpha \beta }$ ，which has two derivatives acting on a field $\mathsf { h } ^ { \alpha \beta }$ .If we wanted to write the equation so that all terms with two derivatives acting on $\hbar ^ { \alpha \beta }$ are on the left-hand side,the term $\mathsf { h } ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } \mathsf { h } ^ { \alpha \beta }$ should also go on the left-hand side,so the total differential operator acting on $\hslash ^ { \alpha \beta }$ is not a simple flat-space d'Alembertian． Still, eq.(5.72) is a legitimate way of writing the Einstein equations,which is particularly convenient because the flat space d'Alembertian is easily inverted.

then eq.(5.71) can be seen as the condition that imposes the equation of motion on the matter variables. Imposing the no-incoming-radiation boundary conditions (defined in Note 1 on pagc 102),cq. (5.72) can be formally integrated in terms of the retarded Green’s function (3.6), just as we did in linearized theory (see eq. (3.8)),and we get

$$
\begin{array} { l }  { \displaystyle { \mathsf h } ^ { \alpha \beta } ( t , { \bf x } ) = - \frac { 4 G } { c ^ { 4 } } \int { d ^ { 4 } x ^ { \prime } \frac { \tau ^ { \alpha \beta } ( t ^ { \prime } , { \bf x } ^ { \prime } ) \delta ( t ^ { \prime } - t + | { \bf x } - { \bf x } ^ { \prime } | / c ) } { | { \bf x } - { \bf x } ^ { \prime } | } } } \\ { { \displaystyle ~ = - \frac { 4 G } { c ^ { 4 } } \int \frac { d ^ { 3 } x ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } \tau ^ { \alpha \beta } ( t - | { \bf x } - { \bf x } ^ { \prime } | / c , { \bf x } ^ { \prime } ) . } } \end{array}
$$

On this solution,we can then Impose the gauge condition (5.82),whicl is equivalent to requiring that the matter sources satisfy the equations of motion in the metric gμv:

Contrary to the result (3.5),(3.6) of linearized theory,in eq. (5.83 $\tau ^ { \alpha \beta }$ is itself a functional of $\hbar ^ { \alpha \beta }$ and of its derivatives, so for the mo ment we have simply converted the differential equation (5.72) into al integro-differential equation for $\hbar ^ { \alpha \beta }$ . Finding an exact solution of such an equation is hopeless for all realistic astrophysical sources,and we must resort to approximation methods.The crucial observation is that different approximations must be employed,depending on whether we are in the near or in the far zone. In the near zone,the solution for $\mathsf h _ { \mu }$ will be given in terms of instantaneous potential,and retardation effects can be treated as small corrections.In the far region the post-Newtonial approximation breaks down,arld we will rather have gravitational waves so retardation effects will of cdurse be crucial.

The fact that different exparjsions must be used in the near and in thi far region,in itself is not differeht from what happens in electrodynamics The great difference is that electrodynamics is a linear theory,governe by a wave equation of the form $\sqcup A _ { \mu } = - ( 4 \pi / c ) J _ { \mu }$ ，where the source $J _ { \mu }$ depends only on the matter fields,and not on $A _ { \mu }$ itself. However, eq.(5.72) or in eq.(5.83),the ffeld $\mathsf { h } _ { \mu , \nu }$ appears even on the right-hand side; thus,the gravitational field itself generates gravitational waves and if we compute iteratively to a sufficiently high order,we will find that th GWs compute at a given order generate themselves more GWs at highel orders. This is an unavoidable consequence of the non-linear structure of general relativity. At the technical level this is reflected in the facl that,even if the matter energy-momentum tensor $T ^ { \alpha \beta }$ is localized in space,the total source $\tau ^ { \alpha \beta }$ is not confined to a compact region, buti extends over allof space-time.As a result,a correct treatiment is quite complicated (and a naive treatment of the integral in eq. (5.83) typically results in the divergences which plagued early attempts, see Note 15 Nowadays these problems have been solved,and the generation of Gw from post-Newtonian sources has been computed to very high PN order thanks to the quite remarkable work of two groups,one composed Blanchet, Damour and coworkers,and one of Will,Wiseman and Pati. Below we discuss these two approaches.

# 5.3The Blanchet-Damour approach

In the problem of computing GWs from anon-relativistic,self-gravitating source with typical velocity $v$ there are two length-scales:the size $d$ of the source (which,fora binary system,is the orbital radius),and the length $\mathcal { R }$ that determines the boundary of the near zone,see eq.(5.1). According to eq. (3.24), ${ \dot { \bar { \lambda } } } = ( c / v ) d$ so,for non-relativistic sources, $\lambda \gg d$ ， and therefore the near zone extends up to a radius $\mathcal R \gg d$ In the region $r < \mathcal { R }$ the gravitational field can be computed using the post-Newtonian formalism.However,as we have seen in the previous section, the post-Newtonian approach breaks down at $r > \mathcal { R }$

On the other hand， outside the matter source $( r > d )$ the energymomentum tensor of matter vanishes,and the only contribution to $\tau ^ { \alpha \beta }$ ineq. (5.73) comes from the gravitational field itself. If the gravitational feld inside the matter source is weak,which (for the moment） is an assumptions of the method,already at $r = d$ space-time will not deviate much from flat and, as $r$ increases,it willapproach Minkowski space-time more and more. Thus,over the whole region $d < r < \infty$ we can solve the vacuum Einstein equations using a post-Minkowskian expansion,that akes into account iteratively the deviaton from flat space-time. Since the post-Minkowskian expansion is valid for $d < r < \infty$ and the post-Newtonian for $0 < r < \mathcal { R }$ ,the two expansions have an overlapping region of validity, $d < r < \mathcal { R }$ . The strategy of the Blanchet-Damour formalism btherefore to use the post-Newtonian expansion in the near region, the post-Minkowskian expansion outside the source,and to match them in the intermediate region. In the following subsections we discuss these steps.

# 5.3.1 Post-Minkowskian expansion outside the source

We first consider the external domain $d _ { \tau } < r < \infty$ .Since we are outie the source,the energy-momentum tensor of matter vanishes,and e must solve the vacuum Einstein equations. By assumption,we are onsidering sources whose self-gravity is weak. Thus, in a frst approxmation the metric in the external domain is just $\eta _ { \mu \nu }$ ，i.e.we have Minkowski space-time. At a distance $r$ ,the corrections to the Minkowski metric will be given as an expansion in $\not R _ { S } / r$ where,as in Section 5.1.1, $\ell _ { 5 } = 2 G m / c ^ { 2 }$ and $m$ is a characteristic mass of the system. Since $R _ { S }$ is proportional to $G$ ,the post-Minkowskian expansion can be written as an xpansion in powers of $G$ .We use as basic variable ${ \mathsf { h } } ^ { \alpha \beta } = { \sqrt { - g } } g ^ { \alpha \beta } - \eta ^ { \alpha \beta }$ choose the De Donder gauge,and wewrite

$$
\sqrt { - g } g ^ { \alpha \beta } = \eta ^ { \alpha \beta } + { \cal G } \mathsf { h } _ { 1 } ^ { \alpha \beta } + { \cal G } ^ { 2 } \mathsf { h } _ { 2 } ^ { \alpha \beta } + \dots ,
$$

$$
\mathsf { h } ^ { \alpha \beta } = \sum _ { n = 1 } ^ { \infty } G ^ { n } \mathsf { h } _ { n } ^ { \alpha \beta } .
$$

We now plug this expansion into the relaxed Einstein equations (5.72) with $T ^ { \alpha \beta } = 0$

$$
\bar { \Psi } \mathfrak { h } ^ { \alpha \beta } = \Lambda ^ { \alpha \beta } ,
$$

and we equate terms of the same order in $G$ .The tensor $\Lambda ^ { \alpha \beta }$ depends on $g _ { \mu \nu }$ ,which is a highly non-linear functional of $\mathsf { h } _ { \mu \nu }$ ,so it contains all possible powers of $\mathsf h _ { \mu \nu }$ ,starting from terms quadratic in $\mathsf { h }$ Thus,we can write

$$
\Lambda ^ { \alpha \beta } = N ^ { \alpha \beta } [ \mathsf { h } , \mathsf { h } ] + M ^ { \alpha \beta } [ \mathsf { h } , \mathsf { h } , \mathsf { h } ] + L ^ { \alpha \beta } [ \mathsf { h } , \mathsf { h } , \mathsf { h } , \mathsf { h } ] + O ( \mathsf { h } ^ { 5 } ) ,
$$

and $N ^ { \alpha \beta } , M ^ { \alpha \beta }$ , etc.can be found from the explicit expression of $\Lambda ^ { \alpha \beta }$ with long but straightforward computations.For instance

$$
\begin{array} { l } { { { \displaystyle N ^ { \alpha \beta } [ { \bf h } , { \bf h } ] = - \mathsf { h } ^ { \mu \nu } \partial _ { \mu } \partial _ { \nu } { \bf h } ^ { \alpha \beta } } + \frac { 1 } { 2 } \partial ^ { \alpha } { \sf h } _ { \mu \nu } \partial ^ { \beta } { \sf h } ^ { \mu \nu } - \frac { 1 } { 4 } \partial ^ { \alpha } { \sf h } \partial ^ { \beta } { \sf h } } \qquad \quad ( 5 . 8 \mathsf { ) } }  \\ { { \displaystyle \qquad - \partial ^ { \alpha } { \sf h } _ { \mu \nu } \partial ^ { \mu } { \sf h } ^ { \beta \nu } - \partial ^ { \beta } { \sf h } _ { \mu \nu } \partial ^ { \mu } { \sf h } ^ { \alpha \nu } + \partial _ { \nu } { \sf h } ^ { \alpha \mu } ( \partial ^ { \nu } { \sf h } _ { \mu } ^ { \beta } + \partial _ { \mu } { \sf h } ^ { \beta \nu } ) } } \\ { { \displaystyle \qquad + \eta ^ { \alpha \beta } \left[ - \frac { 1 } { 4 } \partial _ { \rho } { \sf h } _ { \mu \nu } \partial ^ { \rho } { \sf h } ^ { \mu \nu } + \frac { 1 } { 8 } \partial _ { \mu } { \sf h } \partial ^ { \mu } { \sf h } + \frac { 1 } { 2 } \partial _ { \mu } { \sf h } _ { \nu \rho } \partial ^ { \nu } { \sf h } ^ { \mu \rho } \right] } , } \end{array}
$$

$^ { 2 2 } \mathrm { F o r }$ theexplicitexpressionof $M ^ { \alpha \beta } [ \mathsf { h } , \mathsf { h } , \mathsf { h } ]$ see eq. (1.6)of Blanchet (1995).

where,on the right-hand side, $\mathsf { h } = \eta _ { \alpha \beta } \mathsf { h } ^ { \alpha \beta }$ , and all indices are raised and lower with the Minkowski metric $\eta _ { \mu \nu }$ .22 Since $\Lambda ^ { \alpha \beta }$ starts from a term quadratic in $\mathsf { h } ^ { \alpha \beta }$ ,and therefore proportional to $G ^ { 2 }$ ,to order $G$ we simply have

$$
\begin{array} { r } { \mathsf { D } \mathsf { h } _ { 1 } ^ { \alpha \beta } = 0 , } \end{array}
$$

and,to higher orders, we get

$$
\begin{array} { r l } & { \Theta \mathsf { h } _ { 2 } ^ { \alpha \beta } = N ^ { \alpha \beta } [ \mathsf { h } _ { 1 } , \mathsf { h } _ { 1 } ] , } \\ & { \Theta \mathsf { h } _ { 3 } ^ { \alpha \beta } = M ^ { \alpha \beta } [ \mathsf { h } _ { 1 } , \mathsf { h } _ { 1 } , \mathsf { h } _ { 1 } ] + N ^ { \alpha \beta } [ \mathsf { h } _ { 1 } , \mathsf { h } _ { 2 } ] + N ^ { \alpha \beta } [ \mathsf { h } _ { 2 } , \mathsf { h } _ { 1 } ] , } \end{array}
$$

and so on,together with the gauge conditions

$$
| \partial _ { \beta } \mathsf { h } _ { n } ^ { \alpha \beta } = 0 .
$$

We write generically the $n$ -thlequation in the form

$$
\begin{array} { r } { \Theta \mathsf { h } _ { n } ^ { \alpha \beta } = \Lambda _ { n } ^ { \alpha \beta } [ \mathsf { h } _ { 1 } , \mathsf { h } _ { 2 } , \ldots , \mathsf { h } _ { n - 1 } ] , \qquad ( r > d ) , } \end{array}
$$

where we have recalled that the above equations are valid only in tle exterior region $r > d$

# General solution of the linearized vacuum equation

We consider first the linearized equation (5.89).We want to find the most general solution,in order to be able to perform later the matching with the near-region post-Newtonian solution. The most general solution of eq.(5.89) in the region $r > d$ (with $d$ any strictly positive constant),can be written in terms of retarded multipolar waves,

$$
{ \sf h } _ { 1 } ^ { \alpha \beta } = \sum _ { l = 0 } ^ { \infty } \partial _ { L } \left[ \frac { 1 } { r } K _ { L } ^ { \alpha \beta } ( t - r / c ) \right] ,
$$

where we have used the multi-index notation introduced in Section 3.5.1, and the tensors $K _ { L } ^ { \alpha \beta }$ aretraceesandsmetricitsecttothe indices $i _ { 1 } , \dots , i _ { l }$ From the fact that $K _ { L } ^ { \alpha \beta }$ is a function of $u = t - r / c$ it follows that $\Pi ( K _ { L } ^ { \alpha \beta } ( u ) / r ) = 0$ and,since thefatspacedembrtian commutes with $\partial _ { L }$ ,eq.(5.94) is a solution of eq.(5.89). Since the set of STF tensors $K _ { L } ^ { \alpha \beta }$ ,with allpossibl rank $l$ , provide a complete set of representation of the rotation group, this is the most general solution. Observe that this solution is acceptable since we are in the domain $r > d$ so we have excluded $r = 0$ from the domain where it is required to hold. Otherwise all multipoles in eq. (5.94) would become singular.

Equation (5.94) is the most general solution of eq.(5.89),but in general it does not fulfll the De Donder gauge condition. The tensor $\hat { K } _ { L } ^ { \alpha \beta }$ is symmetric in the Lorentz indices $\alpha , \beta \left| _ { \mathrm { s 0 } } \right.$ ，foreach $L$ ,it has 10 tensor components. Imposing the gauge condition $\partial _ { \beta } \mathsf { h } _ { 1 } ^ { \alpha \beta } = 0$ reduces the number of independent tensor components to six,and one finds that the most general solution of the equation of motion and gauge condition,in the external region,has the form

$$
\mathsf { h } _ { 1 } ^ { \alpha \beta } = k _ { 1 } ^ { \alpha \beta } + \partial ^ { \alpha } \varphi _ { 1 } ^ { \beta } + \partial ^ { \beta } \varphi _ { 1 } ^ { \alpha } - \eta ^ { \alpha \beta } \partial _ { \mu } \varphi _ { 1 } ^ { \mu } ,
$$

where te components of $k _ { 1 } ^ { \alpha \beta }$ are given by

$$
\begin{array} { l } { { \displaystyle { k _ { 1 } ^ { 0 0 } = - \frac { 4 } { c ^ { 2 } } \sum _ { l \geqslant 0 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { 1 } { r } { \cal I } _ { L } ( u ) \right] \ , \ } \ ~ ( 5 . 9 6 ) } } \\ { { \displaystyle { k _ { 1 } ^ { 0 i } = \frac { 4 } { c ^ { 3 } } \sum _ { l \geqslant 1 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 1 } \left[ \frac { 1 } { r } { \cal I } _ { i L - 1 } ^ { ( 1 ) } ( u ) + \frac { l } { l + 1 } \epsilon _ { i a b } \partial _ { a } \left( \frac { 1 } { r } { \cal J } _ { b L - 1 } ( u ) \right) \right] } \ , \ ~ } } \\ { { \displaystyle { k _ { 1 } ^ { i j } = - \frac { 4 } { c ^ { 4 } } \sum _ { l \geqslant 2 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 2 } \left[ \frac { 1 } { r } { \cal I } _ { i j L - 2 } ^ { ( 2 ) } ( u ) + \frac { 2 l } { l + 1 } \partial _ { a } \left( \frac { 1 } { r } \epsilon _ { a b ( i ) } { \cal J } _ { j b L - 2 } ^ { ( 1 ) } ( u ) \right) \right] } . \ ~ } } \end{array}
$$

We have used the notation

$$
f ^ { ( n ) } ( u ) \equiv { \frac { d ^ { n } f } { d u ^ { n } } } ,
$$

to denote the $n$ -th derivative with respect to retarded time.23 The ten-8T $k _ { 1 } ^ { \alpha \beta }$ depends on two families of symmetric and traceless multipole moments,

d

$$
\begin{array} { r l } & { \mathrm { I } _ { L } ( u ) = \{ \mathrm { I } , \mathrm { I } _ { i } , \mathrm { I } _ { i j } , \mathrm { I } _ { i j k } , \dots \} , } \\ & { } \\ & { \mathrm { J } _ { L } ( u ) = \{ \mathrm { J } _ { i } , \mathrm { J } _ { i j } , \mathrm { J } _ { i j k } , \dots \} , } \end{array}
$$

hich are arbitrary functions of retarded time,except that the gauge mndition requires that I, $\mathrm { I } _ { i } ^ { ( 1 ) }$ and ${ \bf J } _ { i }$ are time-independent.This exresses the conservation of the total mass $\mathrm { M } \equiv \mathrm { I }$ of the system,of the otal linear momentum $\mathrm { P } _ { i } \equiv \mathrm { I } _ { i } ^ { ( 1 ) }$ andof thetotal angularmomentum $\mathrm { S } _ { i } \equiv \mathrm { J } _ { i }$ .24 The moments $\mathrm { I } _ { L }$ and $\mathbb { J } _ { \boldsymbol { \xi } }$ are mass-type and currentype moments,respectively, just as in the multipole expansion of linarized theory, discussed in Section 3.5.The explicit powers of $c$ in

23We also made use of the notation introduced on page 134,so in particular $\partial _ { L - 2 } \equiv \partial _ { i _ { 1 } } \dots \partial _ { i _ { l - 2 } }$ $I _ { i j L - 2 } \equiv$ $I _ { i j i _ { 1 } \dots i _ { l - 2 } }$ ，and round brackets around indicesdenote the symmetrization, $a _ { ( i j ) } \equiv ( 1 / 2 ) ( a _ { i j } + a _ { j i } )$ .On the righthand side,we freely raised or lowered the spatial indices with $\delta _ { i j }$

24 We further impose the condition that the metric is stationary in the far past, i.e.that all $\mathrm { I } _ { \mathit { L } }$ and $\mathrm { J } _ { L }$ are constants for $t ~ \leqslant ~ - T$ with $T ~  ~ \infty$ This is expected to be basically equivalent to the no-incoming radiation boundary condition,but offers some technical advantages.With this boundary condition,the requirement that $\mathrm { I } _ { i } ^ { ( 1 ) }$ be constant implies that also the center-ofmass variable ${ \mathrm { X } } _ { i } ~ = ~ { \mathrm { I } } _ { i } / { \mathrm { I } }$ is constant, rather than a priori linearly varying in time.

eqs.(5.96) follow from the choice of dimensions $[ \mathrm { I } _ { L } ] = [ \mathrm { m a s s } ] \times [ \mathrm { l e n g t h } ]$ and $[ \mathrm { J } _ { L } ] = [ \mathrm { m a s s } ] \times [ \mathrm { v e l o c i t y } ] \times [ \mathrm { l e n g t h } ] ^ { l }$ . These are chosen in anticipa tion of the fact that $\mathrm { I } _ { L }$ and $\mathrm { J } _ { \mathit { L } }$ will be related to the mass and curreu multipoles of the source.The “mass dipole” $\mathrm { I } _ { i }$ can be set to zero shifting the origin of the coordinate system.

The function $\varphi _ { 1 } ^ { \mu }$ can be written in terms of four STF moments $\textrm { W } _ { L }$ $\mathrm { X } _ { L } , \mathrm { Y } _ { L }$ and $\mathrm { Z } _ { L }$ ，

$$
\begin{array} { l } { { \displaystyle \varphi _ { 1 } ^ { 0 } = \frac { 4 } { c ^ { 3 } } \sum _ { l \geqslant 0 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { 1 } { r } \mathrm { W } _ { L } ( u ) \right] \ : , } } \\ { { \displaystyle \varphi _ { 1 } ^ { i } = - \frac { 4 } { c ^ { 4 } } \sum _ { l \geqslant 0 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { i L } \left[ \frac { 1 } { r } \mathrm { X } _ { L } ( u ) \right] \qquad } } \\ { { \displaystyle \qquad - \frac { 4 } { c ^ { 4 } } \sum _ { l \geqslant 1 } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L - 1 } \left[ \frac { 1 } { r } \mathrm { Y } _ { i L - 1 } ( u ) + \frac { l } { l + 1 } \epsilon _ { i a b } \partial _ { a } \left( \frac { 1 } { r } \mathrm { Z } _ { b L - 1 } ( u ) \right) \right] \ : . } } \end{array}
$$

25When comparing with eq. (3.204),re call that in the linearized limit $\mathsf { h } _ { \mu \nu }$ reduces to $- \hat { h } _ { \mu \nu }$ ,see Note 19,and also that a factor $G$ has been explicitly extracted from $\mathsf { h } _ { 1 } ^ { \mu \nu }$ ,see eq. (5.84).

The appearance of the function $\varphi _ { 1 } ^ { \alpha }$ in eq.(5.95) reflects the fact tha eq.(5.89） is invariant under linearized gauge transformations, $x ^ { \alpha }$ $x ^ { \alpha } + \varphi _ { 1 } ^ { \alpha } ( x )$ ,compare with eq(1.19). One might be tempted to dis card $\varphi _ { 1 } ^ { \alpha }$ as pure gauge modes(which would give back the result thal we found for linearized theory,see eq. (3.204)),25 but this would not be corect.Ourimistousethesolutio5.95)for $\mathsf { h } _ { 1 } ^ { \alpha \beta }$ as a starting poin struct a solution of the full,rather than linearized,Einstein equations Taking as starting point two different solution for $\mathsf { h } _ { 1 }$ which differ by s linearized gauge transformation $\varphi _ { 1 }$ will produce,through the iterative procedure,two solutions of the full Einstein equations that are not re lated by the full non-linear invariance under diffeomorfisms of general relativity,and which therefore are not physically equivalent.So,beyond linear level the two sets of multipole moments $( \mathrm { I } _ { L } , \mathrm { J } _ { L } , \mathrm { W } _ { L } , \mathrm { X } _ { L } , \mathrm { Y } _ { L } , \mathrm { Z } _ { L }$ and $( \mathrm { I } _ { L } , \mathrm { J } _ { L } , 0 , 0 , 0 , 0 )$ are not gauge-equivalent.Rather,the six multipole moments $( \mathrm { I } _ { L } , \mathrm { J } _ { L } , \mathrm { W } _ { L } , \mathrm { X } _ { L } , \mathrm { Y } _ { L } , \mathrm { Z } _ { L } )$ are gauge-equivalent to a reduced sel $( \mathrm { M } _ { L } , \mathrm { S } _ { L } , 0 , 0 , 0 , 0 )$ ,in which $\mathrm { M } _ { L } = \mathrm { I } _ { L }$ and $\mathrm { S } _ { L } = \mathrm { J } _ { L }$ only to lowest order,and more generally $\mathrm { M } _ { L }$ and $\mathrm { S } _ { L }$ depend on all the six moments $\left( \mathrm { I } _ { L } , \mathrm { J } _ { L } , \mathrm { W } _ { L } , \mathrm { X } _ { L } , \mathrm { Y } _ { L } , \mathrm { Z } _ { L } \right)$ . For example, for the quadrupole moment one finds that $M _ { i j }$ starts to differ from $I _ { i j }$ at $O ( 1 / c ^ { 5 } )$ ,i.e.at 2.5PNorder,

26We include in eq.(5.102) a sign correction pointed out in Arun,Blanchet, Iyer and Qusailah (2004)，see their eq. (3.8).

27They_are also called the"“source multipole moments”，see the review Blanchet (2006)．The term “algorithmic multipole moments”used in the original papers stresses that they are intermediate quantities that allow us to connect，via a well defined algorithm, properties of the source to the “multipole moments at infinity",to be defined later. The term “source moments” stresses that they have explicit closedform expressions as integrals over the source,see below.

$$
\mathrm { M } _ { i j } = \mathrm { I } _ { i j } + \frac { 4 G } { c ^ { 5 } } \left[ \mathrm { W } ^ { ( 2 ) } \big \vert _ { i j } - \mathrm { W } ^ { ( 1 ) } \mathrm { I } _ { i j } ^ { ( 1 ) } \right] + O \left( \frac { 1 } { c ^ { 7 } } \right) ,
$$

where $\mathrm { W }$ is $\mathrm { W } _ { L }$ for $l = 0$ The six sets of moments $\left( \mathrm { I } _ { L } , \dots , \mathrm { Z } _ { L } \right)$ are referred to as “algorithmic multipole moments".27

# Iteration of the solution. Multipolar post-Minkowskian expansion

We have found above the most general solution of the linearized equatiol (5.89),together with $\partial _ { \beta } \mathsf { h } _ { 1 } ^ { \alpha \beta } = 0$ , in the domain $r > d$ Next we wam to plug this solution into the right-hand side of eq. (5.9O),and solve the resulting equation for $\mathsf { h } _ { 2 }$ ,and so on.The general problem is therefore how to integrate a wave equation suchas eq.(5.93)，when the source term $\Lambda _ { n }$ has been determined by the previous recursive level.

Given the function $\Lambda _ { n }$ ,the problem amounts to inverting the $\sqsubseteq$ operator.Physicists are well accustomed tolsome possible solutions for the mversion of the d'Alembert operator: the retarded and the advanced Green's functions,familiar from classical electrodynamics,or the Feynman propagator,which is a basic object in quantum field theory. However,from a mathematical point of view,the inversion of the $\sqcap$ operator has many other possible solutions,which depend on the boundary conditions of the problem.

In the problemat hand the retarded Green's function is simply not the correct solution (and even less any other combination of retarded and advanced Green's functions). The point is that the use of the retarded lor of the advanced） integral requires the knowledge of $\Lambda _ { n }$ over all of pace,while eq.(5.93) is valid only for $r > d$ ．Observe that,since we ire outside the source,we can write each $\mathsf { h } _ { n }$ in a multipole expansion, which is an expansion valid for $d / r < 1 , \mathsf { s o } \ \Lambda _ { n }$ in eq.(5.93) is composed f the product of many multipole expansions. If we naively extended 4. (5.93) down to $r = 0$ ，we would find that the right-hand side of 4. (5.93) is highly singular at $r = 0$ ahd,if we make the convolution ith the retarded Green's function, the retarded integral diverges.

The appropriate solution has been found by Blanchet and Damour, ith a clever mathematical procedure.First,we observe that we are f-Ially interested in computing to some fnite order in the PN expansion, Md to each given order only a finite number of multipoles contribute. Tlis means that,outside the source,we do not really need the exact ex-$\mathsf { h } _ { 2 } ^ { \alpha \beta } , \mathsf { h } _ { 3 } ^ { \alpha \beta }$ etctl some finite order,that depends on the order of the PN expansion that wish to compute. It is therefore very convenient (in fact,technically evitable) to perform a multipole expansion of the post-Minkowskian ulution,up to a given finite order,and to iterate not $\mathsf { h } _ { 1 } ^ { \alpha \beta }$ but rather (truncated） multipole expansion. This method is therefore called the ltipolar post-Minkowskian (MPM) expansion.

Since, in the MPM computation of $\mathfrak { h } _ { n } ^ { \alpha , \beta }$ with $n$ given,only a maximum umber of multipoles are relevant,we gan find a positive real number sufficiently large, so that $r ^ { B } \Lambda _ { n } ^ { \alpha \beta }$ is regular at the origin.Thus,the rtarded integral

$$
I _ { n } ^ { \alpha \beta } ( B ) \equiv \Pi _ { \mathrm { r e t } } ^ { - 1 } \left( r ^ { B } \Lambda _ { n } ^ { \alpha \beta } \right)
$$

well defined， where wedenoted by $\bigstar _ { \mathrm { r e t } } ^ { - 1 }$ the convolution with the rerded Green's function,28

$$
( \boldsymbol { \Omega } _ { \mathrm { r e t } } ^ { - 1 } f ) ( t , { \bf x } ) \equiv - \frac { 1 } { 4 \pi } \int _ { { \mathbb R } ^ { 3 } } \frac { d ^ { 3 } { x } ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } f \big ( t - | { \bf x } - { \bf x } ^ { \prime } | / c , { \bf x } ^ { \prime } \big ) .
$$

w.it can be proved that $I _ { n } ^ { \alpha \beta } ( B )$ admits a unique analytic continuation the complex $B$ -plane,except at some integer values of $B$ and,when $\mapsto 0$ ,develops some multipole poles.Thus,near $B = 0$ we can write

28 We also impose the boundary condition in the form given in Note 24.In the retarded integral, the integration is actually over $d ^ { 4 } x$ ，along the past null light cone.As $r  \infty$ along the past null light cones, $t$ goes toward $- \infty$ s0 this boundary condition forces $\Lambda _ { n } ^ { \alpha \beta }$ to become strictly zero beyond some value of $\boldsymbol { r }$ ，Therefore there is no problem of convergence of the integral at $r \to \infty$

$I _ { n } ^ { \alpha \beta } ( B )$ in a Laurent expansiot,

$$
I _ { n } ^ { \alpha \beta } ( B ) = \sum _ { p = p _ { 0 } } ^ { \infty } B ^ { p } \iota _ { n , p } ^ { \alpha \beta } ,
$$

where $p _ { 0 } ~ \in ~ \mathbb { Z }$ If $p _ { 0 } ~ < ~ 0$ there are poles. Applying the fat-spac d'Alembertian to both sides of this equation and using eq. (5.103)w get

$$
r ^ { B } \Lambda _ { n } ^ { \alpha \beta } = \sum _ { p = p _ { 0 } } ^ { \infty } B ^ { p } \Pi _ { n , p } .
$$

Writing $r ^ { B } = e ^ { B \log r }$ , expanding the exponential,and equating_term with the same powers of $B$ we find that,for $p _ { 0 } \leqslant p \leqslant - 1$ ， $\Pi _ { t _ { n , p } } ^ { \alpha \beta } = 0 ,$ while for $p \geqslant 0$

$$
\Pi _ { n , p } ^ { ~ \alpha \beta } = \frac { ( \log r ) ^ { p } } { p ! } \Lambda _ { n } ^ { \alpha \beta } .
$$

29Morepreciselyin thedefinitionof the $\mathrm { F P } _ { B = 0 }$ operation,eq.(5.108),for dimensional reasons we use $( r / r _ { 0 } ) ^ { B }$ rather than $r ^ { B }$ The constant $r _ { 0 }$ is arbitrary,and will cancel from physical quantities,as we will see in Section 5.3.4.For the moment，we set $r _ { 0 } = 1$ ,to simplify the notation.

In particularthe term with $p = 0$ ,i.e $u _ { n } ^ { \alpha \beta } \equiv \iota _ { n , p = 0 } ^ { \alpha \beta }$ n,p=0，satisfies u $\begin{array} { r } { \bigsqcup u _ { n } ^ { \alpha \beta } = } \end{array}$ $\Lambda _ { n } ^ { \alpha \beta }$ soweedi other words,a solution of eq. $\left( ( 5 . 9 3 ) \right.$ is given by the coefficient of $B ^ { 0 }$ i the Laurent expansion (5.105).This is called the finite part at $B = 0 \mathrm { { o l } }$ the retarded integral,and denoted as $\mathrm { F P } _ { B = 0 }$ ， $\mathrm { 8 0 } ^ { 2 9 }$

<table><tr><td>品</td><td>=FPB=0{□re1[rBA]}.</td></tr></table>

We can write this even more compactly introducing the symbol $\mathcal { F } \mathcal { P }$ defined on any function $f ( x )$ by

$$
\mathcal { F P } \Pi _ { \mathrm { r e t } } ^ { - 1 } f \equiv \mathrm { F P } _ { B = 0 } \left\{ \bigtriangledown _ { \mathrm { r e t } } ^ { - 1 } \left[ r ^ { B } f \right] \right\} .
$$

This finite part operation is a prescription which makes well-defined the otherwise divergent retarded integral. The important point is that it is not just a prescription superimposed by hand on a would-be divergent quantity. Rather,we have seen explicitly that it is a correct way to find a solution of eq. (5.93),validin the region $r > d$ .Observe that，when the retarded integral of a function $f$ is well-defined, $\mathcal { F P } \Pi _ { \mathrm { r e t } } ^ { - 1 } f$ reduces simply to $\begin{array} { r } { \bigtriangledown _ { \mathrm { r e t } } ^ { - 1 } f } \end{array}$

Actually,eq.(5.108) is justone particular solution of the inhomoge neous equation (5.93). The most general solution is obtained adding the general solution of the homogeneous equation $\begin{array} { r } { \bigsqcup \mathsf { h } _ { n } ^ { \alpha \beta } = 0 } \end{array}$ Indeed, the solution (5.1O8) in general will not satisfy automatically the harmonic gauge condition. So,the solution that we are looking for is really of the form

$$
\mathsf { h } _ { n } ^ { \alpha \beta } = u _ { n } ^ { \alpha \beta } + v _ { n } ^ { \alpha \beta } ,
$$

30The explicit expression is somewhat involved,and can be found in Blanchet (2006),eqs.(41) and (42).

$v _ { n } ^ { \alpha \beta }$ ut $\partial _ { \alpha } v _ { n } ^ { \alpha \beta } \ : = \ : - \partial _ { \alpha } u _ { n } ^ { \alpha \beta }$ $u _ { n } ^ { \alpha \beta }$ tion $v _ { n } ^ { \alpha \beta }$ can be determined exactly.30Theconclusion is that the MPM expansion provides a well-defined algorithm for computing the post-Minkowskian corrections,in principle to arbitrary order.

At this stage,the multipole moments $\left( \mathrm { I } _ { L } , \mathrm { J } _ { L } , \mathrm { W } _ { L } , \mathrm { X } _ { L } , \mathrm { Y } _ { L } , \mathrm { Z } _ { L } \right)$ (or， equivalently, $\mathrm { M } _ { L }$ and $\mathrm { S } _ { \mathit { L } }$ ）know nothing about the properties of the source,since they simply parametrize the most general solution of the vacuum Einstein equation. We will determine them in terms of properties of the source,matching the MPM result to the multipole expansion of the post-Newtonian result, in the region $d < r < \mathcal { R }$ ，where both the post-Minkowskian and the post-Newtonian formalism are applicable.

# 5.3.2 PN expansion in the near region

We now consider the near region. The 1PN solution,in harmonic coordinates,has already been given in the Sectlon 5.1.4.First of all, it is useful to re-express it in terms of the variable $\hbar ^ { \mu \nu }$ ,defined in eq.(5.69),rather than in terms of $g ^ { \mu \nu }$ .31 In terms of $\mathsf { h } ^ { \mu \nu }$ the solution at the Newtonian level is particularly simple, $\mathsf { h } ^ { 0 0 } = - 4 V / \mathsf { q } ^ { 2 } + O ( 1 / c ^ { 4 } )$ ， ${ \mathsf { h } } ^ { 0 i } = O ( 1 / c ^ { 3 } )$ and $\hbar ^ { i j } = O ( 1 / c ^ { 4 } )$ Wecannow plugthissolutionintotherighthand side f eq. (5.72). This gives

31Recall that hμv denotes the combination (5.69),and is not simply the deviation from the flat metric $g ^ { \mu \nu } - \eta ^ { \mu \nu }$ The relation between $\mathsf { h } ^ { \mu \nu }$ and $g ^ { \mu \nu }$ is therefore non-linear.

$$
\begin{array} { l } { { \displaystyle \mathtt { D h } ^ { 0 0 } = \frac { 1 6 \pi G } { c ^ { 4 } } \left( 1 + \frac { 4 V } { c ^ { 2 } } \right) T ^ { 0 0 } - \frac { 1 4 } { c ^ { 4 } } \partial _ { k } V \partial _ { k } V + { \cal O } \left( \frac { 1 } { c ^ { 6 } } \right) , } } \\ { { \displaystyle \mathtt { D h } ^ { 0 i } = \frac { 1 6 \pi G } { c ^ { 4 } } T ^ { 0 i } + { \cal O } \left( \frac { 1 } { c ^ { 5 } } \right) , } } \\ { { \displaystyle \mathtt { D h } ^ { i j } = \frac { 1 6 \pi G } { c ^ { 4 } } T ^ { i j } + \frac { 4 } { c ^ { 4 } } \left\{ \partial _ { i } V \partial _ { j } V - \frac { 1 } { 2 } \delta _ { i j } \partial _ { k } V \partial _ { k } V \right\} + { \cal O } \left( \frac { 1 } { c ^ { 6 } } \right) . } } \end{array}
$$

The solution of these equations is

$$
\begin{array} { l } { { \displaystyle { \mathfrak { n } } ^ { 0 0 } = - \frac { 4 } { c ^ { 2 } } V + \frac { 4 } { c ^ { 4 } } ( W - 2 V ^ { 2 } ) + O \left( \frac { 1 } { c ^ { 6 } } \right) , } } \\ { { \displaystyle { \mathfrak { h } } ^ { 0 i } = - \frac { 4 } { c ^ { 3 } } V _ { i } + O \left( \frac { 1 } { c ^ { 5 } } \right) , } } \\ { { \displaystyle { \mathfrak { h } } ^ { i j } = - \frac { 4 } { c ^ { 4 } } W _ { i j } + O \left( \frac { 1 } { c ^ { 6 } } \right) } , } \end{array}
$$

here $V$ , $V _ { i }$ are given in eqs. (5.39) and (5.41). $W _ { i j }$ is a new retarded otential, defined by

$$
\begin{array}{c} \begin{array} { l } { { \displaystyle W _ { i j } ( t , { \bf x } ) = G \int d ^ { 3 } x \frac { 1 } { | { \bf x } - { \bf x } ^ { \prime } | } \left[ \sigma _ { i j } + \frac { 1 } { 4 \pi G } ( \partial _ { i } V \partial _ { j } V \right.} \end{array}  }  \\ { { \displaystyle \left. - \frac { 1 } { 2 } \delta _ { i j } \partial _ { k } V \partial _ { k } V ) \right] ( { \bf x } ^ { \prime } , t - | { \bf x } - { \bf x } ^ { \prime } | / c ) , } } \end{array}
$$

where $\sigma _ { i j } = T ^ { i j }$ .This is the same as the 1PN solution given in eqs.(5.42)- 644),writen in termsof $\mathsf { h } ^ { \mu \nu }$ rather than $g ^ { \mu \nu }$ ,except that this iterative ocedure automatically gives $\mathsf { h } _ { i j }$ up to $\mathcal { O } ( 1 / c ^ { 6 } )$ (which is needed to itmte consistently the solution to higher orders),rather than just up to $( 1 / c ^ { 4 } )$ as in eq. (5.44). Observe that the integrals in the definition of and $V _ { i }$ are convergent since the source,and therefore $\sigma$ and $\sigma _ { i }$ ,have a umpact support. The integrand in the definition of $W _ { i j }$ rather depends on the function $V$ and does not have a compact support. However,from eq. (5.39),we find that,when $| { { \bf { x } } ^ { \prime } } |  \infty$ ，

$$
V \left( t - { \frac { | \mathbf { x } - \mathbf { x } ^ { \prime } | } { c } } , \mathbf { x } ^ { \prime } \right) \to { \frac { G M } { | \mathbf { x } ^ { \prime } | } }
$$

where

$$
M = \int d ^ { 3 } { \bf y } \sigma ( { \bf y } , - \infty ) + O ( 1 / c ^ { 2 } )
$$

is the initial mass of the sourcelFrom this,we can check that the integra defining the potential $W _ { i j }$ is convergent.

# Multipolar PN expansion

We can now introduce another important ingredient of the method,the “multipolar post-Newtonian expansion”,which combine the PN expan sion with the multipole expansion.

The post-Newtonian expansion is valid both inside the source $( r < d )$ and in the external near zone $d < r < \mathcal { R }$ . In the external near zone we can then expand each post-Newtonian order in a multipole expansion since the expansion parameter of the multipole expansion is $d / r$ Thi gives rise to the “multipolar post-Newtonian expansion”,and provide crucial simplifications when performing the matching with the solution in the far region. To 1PN order,we just need the multipole expansiol of the potentials $V$ and $V _ { i }$ . This can be written in full generality as

$$
\begin{array} { l } { { \displaystyle V ( t , { \bf x } ) = G \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { 1 } { r } F _ { L } ( t - r / c ) \right] , } } \\ { { \displaystyle V _ { i } ( t , { \bf x } ) = G \sum _ { l = 0 } ^ { \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { 1 } { r } G _ { i L } ( t - r / c ) \right] . } } \end{array}
$$

Using eqs.(3.184),(3.185) and (3.188),together with the fact that I and $V _ { i }$ satisfy $\square V = - 4 \pi G \sigma$ and $\Pi V _ { i } = - 4 \pi G \sigma _ { i }$ (see eqs. (5.39) and (5.41)), we get

$$
\begin{array} { l } { { \displaystyle F _ { L } ( u ) = \int d ^ { 3 } y \hat { y } _ { L } \left. \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) \sigma ( u + z | { \bf y } | / c , { \bf y } ) \right. , } } \\ { { \displaystyle G _ { i L } ( u ) = \int d ^ { 3 } y \hat { y } _ { L } \left. \int _ { - 1 } ^ { 1 } d z \delta _ { l } ( z ) \sigma _ { i } ( u + z | { \bf y } | / c , { \bf y } ) \right. , } } \end{array}
$$

where $u = t - r / c$ ,and the function $\delta _ { l } ( z )$ is defined in eq. (3.189).

# The PN expansion to arbitrary order

We now tackle the problem of finding the PN solution to all orders. W write the PN expansion of $\mathsf { h } _ { \mu \nu }$ in the form

$$
{ \mathsf h } ^ { \mu \nu } = \sum _ { n = 2 } ^ { \infty } \frac { 1 } { c ^ { n } } { \mathsf \Omega } ^ { ( n ) } { \mathsf h } ^ { \mu \nu } ,
$$

where we have extracted explicitly the powers of $1 / c$ ,to help the bookkeeping (just as we did with $G$ in the post-Minkowskian expansion).32 Similarly, we expand the effective energy-momentum tensor $\mathrm { a s } ^ { 3 3 }$

$$
\tau ^ { \mu \nu } = \sum _ { n = - 2 } ^ { \infty } \frac { 1 } { c ^ { n } } \left| ^ { ( n ) } \tau ^ { \mu \nu } \right. .
$$

Inserting this into the relaxed Einstein equations,and equating terms with the same powers of $c$ ，we get a recursive set of Poisson-type equationls,

$$
\nabla ^ { 2 } [ ^ { ( n ) } \mathsf { h } ^ { \mu \nu } ] = 1 6 \pi G [ ^ { ( n - 4 ) } \tau ^ { \mu \nu } ] + \partial _ { t } ^ { 2 } [ ^ { ( n - 2 ) } \mathsf { h } ^ { \mu \nu } ] .
$$

We could now try to solve these equations using the Poisson integral 5.61).However,as we already discussed in Section 5.1.6,beyond some value of $n$ the resulting Poisson integrals diverge.This does not mean that eq.(5.126) admits no solution,but simply that the Poisson integral is not the correct one. The problem here is purely technical,and consists ifinding the correct inversion of the Laplacian. The Poisson integral B the right solution only when the boundary condition is that the field vanishes at spatial infinity；otherwise,the solution is different.As an bvious example, consider the equation

$$
\nabla ^ { 2 } U = - \rho ,
$$

where $\rho$ is constant all over space (physically,this equation gives a model fNewtonian cosmology). If we attempt to solve for $U$ using the Poisson itegral (5.61),we find a divergent resuit. However,ona function $U ( r )$ ，

$$
\nabla ^ { 2 } U = \frac { 1 } { r } \frac { \partial ^ { 2 } } { \partial r ^ { 2 } } [ r U ( r ) ] ,
$$

O we see immediately that $U ( r ) = ( - 1 / 6 ) \rho r ^ { 2 }$ is a solution. In this case, was simply not appropriate to impo\$e the boundary condition that ) vanishes at infinity, since the source $\rho$ does not vanish either.

I our case the problem is similar,but more subtle. The point is at we cannot enforce the boundary conditions at infinity within the PN expansion, because this expansion becomes singular as $r  \infty$ ，as esaw in Section 5.1.6. The correct way to incorporate the boundary mditions is to match the PN solution in the near zone to the post-Minkowskian solution in the external source region,and to impose the -incoming radiation boundary conditions on the post-Minkowskian mlution.

A possible strategy is therefore to find one particular solution of the of equations (5.l26). This is the same as a particular solution of the axed Einstein equation (5.72),which is an inhomogeneous equation, the most general solution is obtained adding an arbitrary solution of homogeneous equation $\square \mathsf { h } ^ { \mu \nu } = 0$ (subject to a regularity condition the origin,see below). This homogeneous solution will then be fixed itching the PN solution to the post-Minkowskian solution. Once we

32However in this case one finds that, starting from 4PN order, $( n ) _ { \mathsf { h } } \mu \nu$ has also a logarithmic dependence on $c$ and the expansion contains arbitrary powers of ${ \log c }$

33Observe that this expansion starts from $n = - 2$ ，since $\tau ^ { \mu \nu }$ has dimension of $\rho c ^ { 2 }$

have found a particular solution of eq. (5.126),the addition of an arbi trary solution of the homogeneous equation provides the most general solution in the near region, while in the previous section we found, with the post-Minkowskian expansion, the most general solution in the exter nal source region. Thus,the matching condition will admit a solution.

A particular solution of the set of equations (5.126) has been found by Poujade and Blanchet using a variant of the analytic continuatiol technique discussed in Section 5.3.1. Given a function $f ( \mathbf { x } )$ ,we consider the integral

$$
[ \Delta ^ { - 1 } ( r ^ { B } f ) ] ( { \bf x } ) = - \frac { 1 } { 4 \pi } \int _ { { \mathbb R } ^ { 3 } } \frac { d ^ { 3 } x ^ { \prime } } { | { \bf x } - { \bf x } ^ { \prime } | } | { \bf x } ^ { \prime } | ^ { B } f ( { \bf x } ^ { \prime } ) .
$$

34Observe that here the factor $| \mathbf { x } ^ { \prime } | ^ { B }$ regularizes the divergence at infinity, while in the analytic continuation technique discussed in Section 5.3.1 it regularizes the divergence at the origin.For this reason, here we start from $B$ large and negative，while in Section 5.3.1 we started from $B$ large and positive. More precisely,one assumes that the source is extended and made of some perfectly regular (i.e. $C ^ { \infty }$ ）distribution of fluid.We then separate the original Poisson integral into a part from $r = 0$ up to a finite value,say to the boundary $\mathcal { R }$ of the near zone,and a part from $r = \mathcal { R }$ to $r = \infty$ .The inner integral converges (assuming that $f$ is a smooth function of the source),and no factor $| \mathbf { x } ^ { \prime } | ^ { B }$ is inserted there,while the outer integral is regularized by the insertion of the factor $\mathbf { \bar { \rho } } _ { \mathbf { X ^ { \prime } } \mid B }$ By the uniqueness of the analytic continuation,the result is the sum of the near zone and far zone integrals.

If we take $B$ sufficiently large and negative,the factor $| \mathbf { x } ^ { \prime } | ^ { B }$ regularize any potential divergence of the integral at $| { \bf x } ^ { \prime } |  \infty$ 34 Equation (5.129 then defines a function of $B$ ,for $B$ sufficiently large and negative. On can then prove that this function admits a unique analytic continuation to the complex $B$ -plane,except for $B = 0$ ,where it can develop multipole poles and can be written in aLaurent expansion. The coefficient $u$ of $B ^ { 0 }$ is again denoted by $\mathrm { F P } _ { B = 0 }$ ，

$$
\begin{array} { r } { u = \mathrm { F P } _ { B = 0 } \left\{ \Delta ^ { - 1 } [ r ^ { B } f ] \right\} . } \end{array}
$$

With the same argument used on page 258 for the inversion of the d'Alembertian operator,we can now show that $u$ satisfies $\nabla ^ { 2 } u = f$ S0 $u$ provides a well-defined inversion of the Laplacian. When the Poissol integral converges $\mathrm { F P } _ { B = 0 } \{ \Delta ^ { - 1 } [ r ^ { B } f ] \}$ is the same as $\Delta ^ { - 1 } f$ .Therefore we recover the lowest-order results obtained in the early works on the PN expansion. However, now all higher-order terms are manifestly finite and calculable.

We denote by an overbar the expansion of a quantity up to $n$ -th orden in the PN expansion, e.g.

$$
\bar { \mathsf { h } } ^ { \mu \nu } = \sum _ { m = 2 } ^ { n } \frac { 1 } { c ^ { m } } { \mathsf { \Omega } } ^ { ( m ) } \mathsf { h } ^ { \mu \nu } ,
$$

Taking the sum over $n$ of both sides of eq. (5.126)，we see that th particular solution that we have found can also be written compactly a

$$
\overline { { { \mathsf { h } } _ { \mathrm { p a r t } } ^ { \mu \nu } = \frac { 1 6 \pi G } { c ^ { 4 } } \mathcal { F } \mathcal { P } \sqcup _ { \mathrm { r e t } } ^ { - 1 } \bar { \tau } ^ { \mu \nu } } } .
$$

To this solution we must add the most general solution of the homoge neous equation,subject to the condition of regularity at the origin. Thi has the form

$$
\mathsf { h } _ { \mathrm { h o m } } ^ { \alpha \beta } = \frac { 1 6 \pi G } { c ^ { 4 } } \sum _ { l = 0 } ^ { + \infty } \frac { ( - 1 ) ^ { l } } { l ! } \partial _ { L } \left[ \frac { \mathcal { R } _ { L } ^ { \alpha \beta } ( t - r / c ) - \mathcal { R } _ { L } ^ { \alpha \beta } ( t + r / c ) } { 2 r } \right] ,
$$

where $\mathcal { R } _ { L } ^ { \alpha \beta } ( u )$ are arbitrary functions of $u$ ,and are STF tensors in tl indices $i _ { i } \ldots i _ { l }$ .The fact that this is asolution follows from the fact that for any function $f ( u )$ ，where $u = t - r / c$ ,we have $\sqcup [ f ( u ) / r ] = 0$ ，and similarly $\begin{array} { r } { \bigstar [ \beta ( v ) / r ] = 0 } \end{array}$ ，where $\boldsymbol { v } = \boldsymbol { t } + \left| \boldsymbol { r } \right| \boldsymbol { c }$ .The inclusion of all STF tensor provides a full set of representations of the rotation group,so for instance the first term in eq.(5.133) gives the most general retarded solution.The condition of regularity at $r = 0$ fixes the antisymmetric combination of retarded and advanced waves.Observe that,under time $\mathsf { h } _ { \mathrm { h o m } } ^ { \alpha \beta }$ term gives a correction to the leading term of the radiation reaction force.

# 5.3.3 Matching of the solutions

In the external source region, $d < r < \infty$ ,we have found the solution in the form of a post-Minkowskian expansion,eq. (5.85).For $d / r < 1$ the multipole expansion is applicable,\$o we could write the solution for $\mathsf { h } _ { 1 }$ in terms of the multipole moments $\left( \mathrm { I } _ { L } , \mathrm { J } _ { L } , \mathrm { W } _ { L } , \mathrm { X } _ { L } , \mathrm { Y } _ { L } , \mathrm { Z } _ { L } \right)$ or, equivalently,in termsof $( \mathrm { M } _ { L } , \mathrm { S } _ { L } )$ .Through the iterative procedure that we have discussed,all higher-order terms $\mathsf { h } _ { 2 } , \mathsf { h } _ { 3 } , \ldots$ are then determined, in the form of a multipole expansion.

On the other hand,in the region $0 < r < \mathcal { R }$ ,with $\mathcal { R }$ is the boundary of the near region,we have found the solution in terms of a post-Newtonian expansion. Since we are considering a souirce with $v \ll c$ ,wehave $\mathcal { R } \gg d$ nd the region of validity of the PN expansion overlaps with the region ef validity of the post-Minkowskian expansion.In the post-Minkowskian scheme,the moments $\left( \mathrm { I } _ { L } , \dots , \mathrm { Z } _ { L } \right)$ are quantities that parametrize the most general vacuum solution,but for the moment know nothing about he specific source under consideration! In PN solution,on the contrary,the energy-momentum tensor of the source enter explicitly,see $1 9$ (5.132). Comparing these two solutions in the overlapping region, we can therefore fix the multipole moments $\left( \mathrm { I } _ { L } , \dots , \mathrm { Z } _ { L } \right)$ in terms of the energy-momentum tensor of the source.

To perform this matching we observe that,in the overlap region $\smash { i < r < \mathcal { R } }$ ，we have $d / r < 1$ so each term of the post-Newtonian expansion can be in turn re-expanded in powers of $d / r$ ,i.e.ina multipole expansion.This is the multipolar post-Newtonian expansion discussed I Section 5.3.2. On the other hand,again in the overlap region,each term of the multipolar post-Minkowskiah expansion can be expanded in post-Newtonian way, i.e. in powersof $v / c$ ．A crucial point is that the $\boldsymbol { n }$ -th term of the post-Minkowskian expansion,i.e.the term $\mathsf { h } _ { n } ^ { \alpha \beta }$ in . (5.85), when expanded ina PNfashion,is such that36

$$
\mathfrak { h } _ { n } ^ { 0 0 } = O \left( \frac { 1 } { c ^ { 2 n } } \right) , \quad \mathfrak { h } _ { n } ^ { 0 i } = O \left( \frac { 1 } { c ^ { 2 n + 1 } } \right) , \quad \mathfrak { h } _ { n } ^ { i j } = O \left( \frac { 1 } { c ^ { 2 n } } \right) .
$$

This means that, to work to a given order in the PN expansion，we need to take into account only a finite number of iterations of the post-Minkowskian expansion.For example,suppose that we want to perform computation to 2PN order,i.e.that we want to compute the correction

35Furthermore,the fact that it is a solution of the homogeneous equation means that a source is not needed to sustain this field,which again leads to an interpretation in terms of a pure radiation field. It is well known already in classical electrodynamics that the antisymmetric combination of advanced and retarded waves is associated with radiation reaction．See，e.g．Poisson (1999) for a review.

${ } ^ { 3 6 } \mathrm { F o r }$ the proof see Blanchet and Damour (1986),eq. (5.5).

${ \cal O } ( 1 / c ^ { 4 } )$ to the Newtonian metric. This means that we ned $g _ { 0 0 }$ upto $O ( 1 / c ^ { 6 } )$ ， $g _ { 0 i }$ to $O ( 1 / c ^ { 5 } )$ ,and $g _ { i j }$ to $O ( 1 / c ^ { 4 } )$ ,included. Equation (5.134) shows that we need to compute $\mathsf { h } _ { n }$ up to $n = 3$ ,i.e.that we must perform two iterations of the linearized solution $\mathsf { h } _ { 1 }$

Comparing the multipolar post-Newtonian expansion with the PN re-expansion of the post-Minkowskian solution,allows us to fix the multipole moments $\left( \mathrm { I } _ { L } , \dots , \mathrm { Z } _ { L } \right)$ in terms of the energy-momentum tensor of the source.Remarkably,it is possble to compute them analytically for any l,and formally to arbitrary order in the PN expansion. For IL and $\mathrm { J } _ { L }$ one finds37

37For the proof,see Section 5 of the review Blanchet (2006)．For the explicit expression of the moments $( \mathrm { W } _ { L } , { \mathrm X } _ { L } , { \mathrm Y } _ { L } , { \mathrm Z } _ { L } )$ ，which are needed only when performing computations to relatively high order,see eqs.(87)-(90) of Blanchet (2006).

$$
\begin{array} { l } { { \mathrm { I } _ { L } ( u ) = \mathcal { F P } \displaystyle \int d ^ { 3 } x \displaystyle \int _ { - 1 } ^ { 1 } d z \{ \delta _ { l } ( z ) \hat { x } _ { L } \Sigma - \frac { 4 ( 2 l + 1 ) \delta _ { l + 1 } ( z ) } { c ^ { 2 } ( l + 1 ) ( 2 l + 3 ) } \hat { x } _ { i L } \Sigma _ { \mathrm { i } } ^ { ( 1 ) }  } } \\ { { \displaystyle \qquad + \frac { 2 ( 2 l + 1 ) \delta _ { l + 2 } ( z ) } { c ^ { 4 } ( l + 1 ) ( l + 2 ) ( 2 l + 5 ) } \hat { x } _ { i j L } \Sigma _ { i j } ^ { ( 2 ) } \} ( u + z | { \bf x } | / c , { \bf x } ) ~ , ~ ( 5 . . } }  \\ { { \displaystyle  \mathbb J _ { L } ( u ) = \mathcal { F P } \displaystyle \int d ^ { 3 } x \displaystyle \int _ { - 1 } ^ { 1 } d z \{ \delta _ { l } \langle u \rangle _ { L - 1 } \} a \Sigma _ { b } } } \\ { { \displaystyle \qquad - \frac { ( 2 l + 1 ) \delta _ { l + 1 } ( z ) } { c ^ { 2 } ( l + 2 ) ( 2 l + 3 ) } \hat { x } _ { L - 1 \rangle a c } \Sigma _ { b c } ^ { ( 1 ) } \} ( u + z | { \bf x } | / c , { \bf x } ) ~ . ~ ( 5 . } } \end{array}
$$

We have defined

$$
\begin{array} { c } { { \Sigma = \displaystyle \frac { \bar { \tau } ^ { 0 0 } + \bar { \tau } ^ { i i } } { c ^ { 2 } } \ : , } } \\ { { \Sigma _ { i } = \displaystyle \frac { \bar { \tau } ^ { 0 i } } { c } \ : , } } \\ { { \Sigma _ { i j } = \bar { \tau } ^ { i j } \ : , } } \end{array}
$$

where $\bar { \tau } ^ { i i } \equiv \delta _ { i j } \bar { \tau } ^ { i j }$ ， $\tau ^ { \mu \nu }$ is given in eq. (5.73),the bar overa quantity denotes its PN expansion up to the desired order,and the integration in $d ^ { 3 } x$ is over the whole space $\mathbb { R } ^ { 3 }$ The function $\delta _ { l } ( z )$ has been defined in eq. (3.189),and the remaining notation is explained on page 134 and in eq. (5.97).

Comparing with eqs. (3.207) and (3.208)，we see a truly remarkable fact:despite all complications of the non-linear theory，the full nonlinear result for $\mathsf { h } _ { 1 } ^ { \mu \nu }$ ,to all orders inthePNerpansion,is obtained from the result of linearized theory simply replacing $T ^ { \mu \nu }$ with $\tau ^ { \mu \nu }$ , and inserting the $\mathcal { F P }$ prescription.38

The integration over $z$ is computed,in an expansion in powers of $1 / c$ using eq. (3.209). In particular,to 1PN order one finds from the above equations that the mass quadrupole $I _ { i j }$ (i.e. $\mathrm { I } _ { L }$ with $l = 2$ ）is given by

$$
\begin{array} { l } { { \displaystyle I _ { i j } ( u ) = \int d ^ { 3 } x \hat { x } _ { i j } \bar { \sigma } ( u , { \bf x } ) + \frac { 1 } { 1 4 c ^ { 2 } } \frac { \partial ^ { 2 } } { \partial u ^ { 2 } } \int d ^ { 3 } x \hat { x } _ { i j } | { \bf x } | ^ { 2 } \bar { \sigma } ( u , { \bf x } ) } } \\ { { \displaystyle \quad - \frac { 2 0 } { 2 1 c ^ { 2 } } \frac { \partial } { \partial u } \int d ^ { 3 } x \hat { x } _ { i j k } \bar { \sigma } ^ { 0 k } ( u , { \bf x } ) + { \cal O } \left( \frac { 1 } { c ^ { 4 } } \right) , \qquad ( \bar { \bf u } \nabla ^ { 4 } ) \quad \quad \quad } } \end{array}
$$

with $\sigma$ and $\sigma ^ { k }$ defined in eqsl (3.205)and (3.206). According to the notation introduced on page 134, $\hat { x } _ { i j } = x _ { i } x _ { j } - ( 1 / 3 ) \delta _ { i j } | \mathbf { x } | ^ { 2 }$ , and similarly for $\hat { x } _ { i j k }$ Observe that，for the massquadrupole，to1PN order the integral is over a function with compact support,so the $\mathcal { F P }$ prescription is not necessary.It is remarkable that,to 1PN order，this generalrelativistic result is actually identical to the linearized gravity result obtained from eq.(3.207).That is,for $I _ { i j }$ at 1PN order,we do not even need to make the replacement $T _ { \mu \nu } \to \tau _ { \mu \nu }$ ,since the contribution due to the gravitational field in $\tau _ { \mu , \nu }$ actually cancels out.

The second aspect of the matching problem is that it allows us to fix the funtions $\dot { \mathcal { R } } _ { L } ^ { \alpha \beta }$ The result is

$$
\mathcal { R } _ { L } ^ { \alpha \beta } ( u ) = \frac { 1 } { 2 \pi } \mathcal { F P } \int d ^ { 3 } x ^ { \prime } \hat { x } _ { L } ^ { \prime } \int _ { 1 } ^ { + \infty } d z \delta _ { l } ( z ) \mathcal { M } ( \tau ^ { \alpha \beta } ) ( u - z | \mathbf { x } ^ { \prime } | / c , \mathbf { x } ^ { \prime } ) ,
$$

where $\mathcal { M } ( \tau ^ { \alpha \beta } )$ denotes the multipole expansion of $\tau ^ { \alpha \beta }$ .This homogeueous term is associated with radiatipn reaction effects at 4PN order,due to the so-called tail effects,that will be examined in detail in Section 5.3.4.We will also see that the leading radiation reaction term appears at 2.5PN order (indeed,we already understood this from eq. (5.67))，,so this homogeneous term describes a 1.5PN correction to the leading term of the back-reaction force.

There is one more comment to be made on the validity of the whole lormalism that we have discussed. A crucial point of the whole proredure is the existence of a region where the domain of validity of the post-Minkowskian expansion, $d < r < \infty$ ，overlaps with the domain of validity of the PN expansion, $0 < r < \mathcal { R }$ .If this were not the rase,the general form of the post-Minkowskian solution would still be valid, since it is the most general solution of the vacuum Einstein equations.However,we would not be able to connect the multipole moments ${ \mathfrak { I } } _ { L } , { \mathrm { J } } _ { L } , \dots , { \mathrm { Z } } _ { L }$ that parametrize it,to the properties of the source.As we saw，the PN expansion breaks downat distances $r \sim \mathfrak { X } \sim ( c / v ) d$ Since for a material source $v / c < 1$ ,one might hope that there is always at least a small overlap between the near zone and the external region.However we have seen,already at the level of linearized theory, that a source oscillating at a frequency $\displaystyle { \dot { \omega } _ { s } }$ emits quadrupole radiation at frequency $\omega = 2 \omega _ { s }$ ,while its mass octupole and current quadrupole radiation is at $\omega = \omega _ { s }$ and at $\omega = 3 \omega _ { s }$ ,and a multipole of order $n$ distributes its radiation among a set of lines in frequency,up to a maximum frequency nws.In a computation to n-th PN order,we must include multipoles up to order $\sim n$ ，which therefore generate GWs with frequencies up to $\omega _ { n } = O ( n ) \omega _ { s }$ ,and,correspondingly,reduced wavelength $\dot { \bar { \lambda } } _ { n } = O ( 1 / n ) \dot { \bar { \lambda } } _ { 0 }$ ，where $\dot { x } _ { 0 } \sim ( c / v ) d$ If $\eta$ is larger than $O ( c / v )$ ,it is no louger true that $\dag _ { n } \gg d$ ,and for GWs of such wavelengths the near zone m longer overlaps with the exterior regidn,so we cannot compute them with this formalism．At the same time,while for $v / c \ll 1$ the lowest multipoles dominate, this is no longer true when $v / c$ approaches one, $8 0$ the contributions that we are unable to compute are also no longer negligible.

In other words,for a system with typical velocity $v$ ，we can compute