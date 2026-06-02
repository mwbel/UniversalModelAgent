and we recall again that these quantities are really averages over one period,rather than instantaneous energy and angular momentum losses Using eqs. (4.50) and (4.53) we can rewrite these equations in terms ol the evolution of the semimajor axis $a$ and of the eccentricity $e$ ，

$$
\begin{array} { l } { { \displaystyle \frac { d a } { d t } = - \frac { 6 4 } { 5 } \frac { G ^ { 3 } \mu m ^ { 2 } } { c ^ { 5 } a ^ { 3 } } \frac { 1 } { ( 1 - e ^ { 2 } ) ^ { 7 / 2 } } \left( 1 + \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } \right) , } } \\ { { \displaystyle \frac { d e } { d t } = - \frac { 3 0 4 } { 1 5 } \frac { G ^ { 3 } \mu m ^ { 2 } } { c ^ { 5 } a ^ { 4 } } \frac { e } { ( \mathbb { 1 } - e ^ { 2 } ) ^ { 5 / 2 } } \left( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \right) . } } \end{array}
$$

From eq.(4.117) we see that,if $e = 0$ ，then $d e / d t = 0$ .Therefore a circular orbit remains circular.This could also have been seen directly from eqs. (4.114) and (4.115),pbserving that,for $e = 0$ ,they give

$$
\frac { d \overline { { E } } } { d t } = \omega _ { 0 } \frac { d L } { d t } ,
$$

where $\omega _ { 0 } = ( G m / a ^ { 3 } ) ^ { 1 / 2 }$ is the frequency of the circular motion,see eq.(4.59). Equation (4.118)is just what is needed to maintain the relation between energy and anguiar momentum that holds for circular motion.In fact,for circular orbits,using eq. (4.59),

$$
E = - { \frac { G m \mu } { 2 a } } { \left| = - { \frac { 1 } { 2 } } \left( G m \right) ^ { 2 / 3 } \mu \omega _ { 0 } ^ { 2 / 3 } \right. } ,
$$

while

$$
L = m a ^ { 2 } \omega _ { 0 } = ( G m ) ^ { 2 / 3 } \mu \omega _ { 0 } ^ { - 1 / 3 } ,
$$

and therefore

$$
\begin{array} { r l r } & { } & { \displaystyle \frac { d E } { d t } = - \frac { 1 } { 3 } \big ( G m ) ^ { 2 / 3 } \mu \omega _ { 0 } ^ { - 1 / 3 } \dot { \omega } _ { 0 } , } \\ & { } & { \displaystyle \frac { d L } { d t } = - \frac { 1 } { 3 } \big ( G m ) ^ { 2 / 3 } \mu \omega _ { 0 } ^ { - 4 / 3 } \dot { \omega } _ { 0 } , } \end{array}
$$

from which eq.(4.118）) followslFor $e > 0$ ,eq. (4.117） gives $d e / d t < 0$ instead,and therefore an elliptic orbit becomes more and more circular because of the emission of GWs.

A direct numerical integration of eqs. (4.116) and (4.117) is not as straightforward as one might think. The reason can be seen by putting the equations in dimensionless form.To do so,it is convenient to introduce a length-scale $R _ { * }$ ,from $R _ { * } ^ { 3 } = 4 G ^ { 3 } \mu m ^ { 2 } / c ^ { 6 }$ .We have chosen the numerical factor so that when the masses of the two stars are equal. $m _ { 1 } = m _ { 2 } = M$ ，we have $R _ { * } \ne 2 G M / c ^ { 2 }$ ，s0 $R _ { * }$ becomes equal to the Schwarzschild radius of the stars.We then introduce the dimensionless variable $\tau = c t / R _ { * }$ ,i.e.time measured in units of the light travel time across a distance $R _ { * }$ ，and the dimensionless function $\tilde { a } ( \tau ) = a ( \tau ) / R _ { * }$ . Then eqs. (4.116)and (4.117) read

$$
\begin{array} { l } { { \displaystyle \frac { d \widetilde { a } } { d \tau } = - \frac { 1 6 } { 5 } \frac { 1 } { \widetilde { a } ^ { 3 } } \frac { | 1 } { ( 1 - e ^ { 2 } ) ^ { 7 / 2 } } \left( 1 + \frac { 7 3 } { 2 4 } e ^ { 2 } + \frac { 3 7 } { 9 6 } e ^ { 4 } \right) , \hfill } } \\ { { \displaystyle \frac { d e } { d \tau } = - \frac { 7 6 } { 1 5 } \frac { 1 } { \widetilde { a } ^ { 4 } } \frac { e } { ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } \left( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } \right) . \hfill } } \end{array}
$$

This shows that $\tau = c t / R _ { * }$ is the natural adimensional time-scale in the differential equation. However,for typical solar-mass stars, $R _ { * } \sim 3 ~ \mathrm { k m }$ and $R _ { * } / c = O ( 1 0 ^ { - 5 } )$ s.Therefore,to follow the evolution of the orbit for atime $t \sim 1$ yr,we need to push the integration up to a dimensionless value $\tau \sim 1 0 ^ { 1 2 }$ ,which is numerically diffiecult.

Abetter approach is to combine eqs. (4/116)and (4.117) to get $d a / d e$

$$
\frac { d a } { d e } = \frac { 1 2 } { 1 9 } a \frac { 1 + ( 7 3 / 2 4 ) e ^ { 2 } + ( 3 7 / 9 6 ) e ^ { 4 } } { e ( 1 - e ^ { 2 } ) [ 1 + ( 1 2 1 / 3 0 4 ) e ^ { 2 } ] } .
$$

This equation can be integrated analytically, and gives

$$
a ( e ) = c _ { 0 } \frac { e ^ { 1 2 / 1 9 } } { 1 - e ^ { 2 } } \left( 1 + \frac { 1 2 \mathbb { 1 } } { 3 0 \mathbb { 4 } } e ^ { 2 } \right) ^ { 8 7 0 / 2 2 9 9 } ,
$$

where $c _ { 0 }$ is determined by the initial condition $a = a _ { 0 }$ when $e = e _ { 0 }$ It is convenient to define the function12

<table><tr><td>e12/19 121 g(e)= 1+ 1-e2 304</td><td>870/2299 ，</td></tr></table>

$8 0$ that $a ( e ) = c _ { 0 } g ( e )$ ； $c _ { 0 }$ is fixed by $a _ { 0 } = \rvert _ { c _ { 0 } g ( e _ { 0 } ) }$ ,and therefore

<table><tr><td>g(e) a(e)= ao</td></tr><tr><td>g(ed)</td></tr></table>

In particular, for $e \ll 1$ , we have $g ( e ) \simeq e ^ { 1 2 / 1 9 }$ while, for $e$ close to 1,

$$
g ( e ) \simeq \frac { g _ { 1 } } { 1 - e ^ { 2 } } ,
$$

where $g _ { 1 } = ( 4 2 5 / 3 0 4 ) ^ { 8 7 0 / 2 2 9 9 } \simeq 1 . 1 3 5 2$ A plot of the function $g ( e )$ is shown in Fig. 4.11.

# Orbit circularization

Aconsequence of the above result is that the eccentricity decreases quite fast,so the effect of the back-reaction of GWs is to circularize the orbit. Considera compact binary system,sayaNS-NS binary,that at an initial time has $a _ { 0 }$ very large compared to the radius of the neutron stars,so we ure still very far from coalescence,and an eccentricity $e _ { 0 }$ not particularly amall,neither especially close to one,so that $g ( e _ { 0 } ) = O ( 1 )$ ； let $a$ and $e$ be the values of the semiaxis and eccentricity at a much later time,say when the system is approaching the coalescence phase. Then $e$ will be small and,from eq. (4.128) and the small $e$ limit of $g ( e )$ ,we have

$$
\begin{array} { c } { { a ( e ) \simeq a _ { 0 } \displaystyle \frac { e ^ { 1 2 / 1 9 } } { g ( e _ { 0 } ) } , } } \\ { { { } } } \\ { { e \simeq \displaystyle \left[ \frac { a } { a _ { 0 } } g ( e _ { 0 } ) \right] ^ { 1 9 / 1 2 } . } } \end{array}
$$

![](images/21430a5f31bed85371d9d9e3a525c4812aa3015adfd9ca9afe4322565c05d618.jpg)  
Fig.4.11 The function $g ( e )$ ，ona logarithmic scale,against $e$

12This has nothing todo with the function $g ( n , e )$ defined in eq.(4.108).Both the notation $g ( e )$ for this function and the notation $g ( n , e )$ for the function defined by eq.(4.108) are standard in the literature.

For example,consider the Hulse-Taylor binary pulsar (which will $\mathfrak { b } \mathfrak { e }$ discussed in detail in Chapter 6). Today it has a semimajor axis $a _ { 0 } \simeq$ $2 \times 1 0 ^ { 9 } \mathrm { ~ m ~ }$ and a rather large eccentricity $e _ { 0 } \simeq 0 . 6 1 7$ By the time that the two stars reach a short separation $a$ ,say of the order of a hundred times the radius of the neutron stars, $a = O ( 1 0 ^ { 2 } R _ { \mathrm { N S } } ) \simeq 1 0 ^ { 3 } { \mathrm { k m } }$ , we have $a / a _ { 0 } = O ( 5 \times 1 0 ^ { - 4 } )$ and, since $\vert g ( e _ { 0 } ) = O ( 1 )$ , the eccentricity has become $e \sim ( 5 \times 1 0 ^ { - 4 } ) ^ { 1 9 / 1 2 } \sim 6 \times 1 0 ^ { - 6 }$ .The conclusion is that (unless some external interaction perturbs the binary system), long before the two neutron stars approach the coalescence phase,the ellipticity has become zero to very high accuracy,and the two stars move on a circular orbit which shrinks adiabatically.

# The time to coalescence

We now compute the time to coalescence, $\tau ( a _ { 0 } , e _ { 0 } )$ ,of a binary system that,at an initial time $t _ { 0 } = 0$ ,has semimajor axis $a _ { 0 }$ and eccentricity $e _ { 0 }$ .When $e _ { 0 } = 0$ ,we found the result in eq. (4.26),

$$
\tau ( a _ { 0 } , e _ { 0 } = 0 ) \equiv \tau _ { 0 } ( a _ { 0 } ) = \frac { 5 } { 2 5 6 } \frac { c ^ { 5 } a _ { 0 } ^ { 4 } } { G ^ { 3 } m ^ { 2 } \mu } .
$$

For an elliptic orbit，we canlintegrate eq.(4.116) requiring $a ( t ) = 0$ at $t = \tau ( a _ { 0 } , e _ { 0 } )$ or,equivalently,we can integrate eq. (4.117) requiring $e ( t ) = 0$ at $t = \tau ( a _ { 0 } , e _ { 0 } )$ ， sinde we have seen that at the coalescence e goes to zero. Since the analytic expression for $a ( e )$ is simpler than the form of the inverse function $e ( a )$ ,it is in fact better to use eq. (4.117) so we write

$$
\int _ { 0 } ^ { \tau ( a _ { 0 } , e _ { 0 } ) } d t = - \frac { 1 5 } { 3 0 4 } \frac { q ^ { 5 } } { G ^ { 3 } m ^ { 2 } \mu } \int _ { e _ { 0 } } ^ { 0 } d e \frac { a ^ { 4 } ( e ) ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } { e ( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } ) } ,
$$

that is,

$$
\tau ( a _ { 0 } , e _ { 0 } ) = \frac { 1 5 } { 3 0 4 } \frac { c ^ { 5 } } { G ^ { 3 } m ^ { 2 } \mu } \int _ { 0 } ^ { e _ { 0 } } d e \frac { a ^ { 4 } ( e ) ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } { e ( 1 + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } ) } .
$$

Using eq. (4.128) for $a ( e )$ ,weget

$$
\tau ( a _ { 0 } , e _ { 0 } ) = \tau _ { 0 } ( a _ { 0 } ) { \frac { 4 8 } { 1 9 } } { \frac { 1 } { g ^ { 4 } ( e _ { 0 } ) } } \int _ { 0 } ^ { e _ { 0 } } d e { \frac { g ^ { 4 } ( e ) ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } { e ( 1 + { \frac { 1 2 1 } { 3 0 4 } } e ^ { 2 } ) } } .
$$

Expressing $\tau _ { 0 } ( a _ { 0 } )$ in terms of the orbital period as in eq. (4.27), we can write the result for $\tau _ { 0 } ( a _ { 0 } , e _ { 0 } )$ as

<table><tr><td>To(ao,eo)~9.829 Myr 1hr</td><td>T 8/3 Mo 2/3 Mo F(e0)，</td></tr><tr><td></td><td>(4.136)</td></tr></table>

where $m = m _ { 1 } + m _ { 2 }$ is the total mass, $\mu$ is the reduced mass,

$$
\overline { { F ( e _ { 0 } ) = \frac { 4 8 } { 1 9 } \frac { 1 } { g ^ { 4 } ( e _ { 0 } ) } \int _ { 0 } ^ { e _ { 0 } } d e \frac { g ^ { 4 } ( e ) ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } { e ( \mathrm { 1 } + \frac { 1 2 1 } { 3 0 4 } e ^ { 2 } ) } , } }
$$

and $g ( e )$ is given in eq. (4.127).For example,the Hulse-Taylor binary pulsar has $e _ { 0 } \simeq 0 . 6 1 7$ and $F ( e _ { 0 } ) \simeq 0 . 1 8 4$ ,so its time to coalescence is shorter bya factor $1 / F ( e _ { 0 } ) \simeq 5 . 4$ ,compared to a binary on a circular orbit with the same period. Using the values, $m _ { 1 } = m _ { 2 } \simeq 1 . 4 M _ { \odot }$ and $T _ { 0 } \simeq 7 . 7 5$ hr we obtain the time to cqalescence of the Hulse-Taylor binary pulsar, $\tau ( a _ { 0 } , e _ { 0 } ) \simeq 3 0 0$ Myr.

It can be useful to write some approximate,but more handy expression,for $F ( e _ { 0 } )$ . In the limit $e _ { 0 } \ll 1$ the integrand can be approximated ${ \mathfrak { a s g } } ^ { 4 } ( e ) / e$ ,and $g ( e ) \simeq e ^ { 1 2 / 1 9 }$ ,see eq. (4.127). Then

$$
\begin{array} { l } { { \displaystyle F ( e _ { 0 } ) \simeq \frac { 4 8 } { 1 9 } \frac { 1 } { g ^ { 4 } ( e _ { 0 } ) } \int _ { 0 } ^ { e _ { 0 } } d e e ^ { 4 8 / 1 9 - 1 } } } \\ { { \displaystyle ~ = \frac { 1 } { g ^ { 4 } ( e _ { 0 } ) } e _ { 0 } ^ { 4 8 / 1 9 } \simeq 1 , } } \end{array}
$$

$- 0$ for $e _ { 0 } = 0$ we have $F ( 0 ) = 1$ and we get back the result for circular brbit,eq. (4.27). In the opposite limit $e _ { 0 } \to 1 ^ { - }$ ,the integral in eq.(4.134) is dominated by the region $e \simeq 1$ ,where $g ( e )$ is given by eq.(4.129). Then we get

$$
\begin{array} { l } { { \displaystyle { F ( e _ { 0 } ) \simeq \frac { 4 8 } { 1 9 } \left( \frac { 1 - e _ { 0 } ^ { 2 } } { g _ { 1 } } \right) ^ { 4 } \int ^ { e _ { 0 } } d e \frac { 1 } { [ 1 + ( 1 2 1 / 3 0 4 ) ] } \frac { g _ { 1 } ^ { 4 } } { ( 1 - e ^ { 2 } ) ^ { 4 } } ( 1 - e ^ { 2 } ) ^ { 5 / 2 } } } } \\ { { \displaystyle { \simeq \frac { 7 6 8 } { 4 2 9 } ( 1 - e _ { 0 } ^ { 2 } ) ^ { 4 } \left[ ( 1 - e _ { 0 } ^ { 2 } ) ^ { - 1 / 2 } + { \cal O } ( 1 ) \right] } } } \\ { { \displaystyle { \simeq \frac { 7 6 8 } { 4 2 9 } ( 1 - e _ { 0 } ^ { 2 } ) ^ { 7 / 2 } } . } } \end{array}
$$

Iherefore,in this limit the time to coalescence is smaller than for a rcular orbit with the same period,bya factor proportional to $( 1 -$ $( \frac { 2 } { 6 } ) ^ { 7 / 2 }$ This dependence is easily understood from the fact that the wstem spends most of its lifetime near $a \ = \ a _ { 0 }$ ， $\textstyle e \ = \ e _ { 0 }$ ，where the mdiated energy is enhanced by a factor proportional to $( 1 - e _ { 0 } ^ { 2 } ) ^ { 7 / 2 }$ ， ompared to the circular case,see eqs.(4.74) and (4.75). Comparing thelimits $e \to 0$ and $e \to 1 ^ { - }$ ，we see that it is convenient to define a function $G ( e _ { 0 } )$ from

$$
F ( e _ { 0 } ) \equiv G ( e _ { 0 } ) ( 1 + e _ { 0 } ^ { 2 } ) ^ { 7 / 2 } ,
$$

because $G ( e _ { 0 } )$ is a function everywhere close to one.A plot of $G ( e _ { 0 } )$ lom the exact numerical integration of eq. (4.137) is shown in Fig.4.12. We see that $G ( e )$ is always very close to one,within a few per cent at last until $e = 0 . 6$ ,where $G ( e ) \simeq 0 . 9 8 2$ ,and then,approaching $e = 1$ ,it mises to reach the finite value $G ( 1 ) = 7 6 8 / 4 2 5 \simeq 1 . 8 0$

![](images/866c47adf7719c5ab182e299844233d8407925991c255dc2393e608f1ea511d8.jpg)  
Fig.4.12 Thefunction $G ( e )$ ， against $e$ At $e = 1 \ G ( e )$ is finite, $G ( 1 ) = 7 6 8 / 4 2 5 \simeq 1 . 8 0$

# 4.1.4 Binaries at cosmological distances

Until now,we have implicitly assumed that the binary system that coalesces is at a sufficiently small distance from us,so that the expansion of the Universe during the propagation of the GWs from the source to the detector can be neglected. However,some gravitational-wave detec tors,in their advanced stage,have the potential of observing coalescing binaries out to cosmological distances: we will see that advanced ground based interferometers could detect BH-BH coalescences out to distance of order 1-2 Gpc (corresponding to a redshift $z \sim 0 . 2 5 \mathrm { - } 0 . 5$ ，while the space interferometer LISA could detect the coalescence of supermassive black-hole binaries out to redshifts $z \sim 5 \mathrm { - } 1 0$ .Actually， these will be among the most fascinating sources of GW astronomy. The rich cosmological information that could be extracted from such events willbe discussed in Vol.2. Here we prepare the necessary tools,discussing how the signal of a binary inspiral at a cosmological distance is affected by the expansion of the Universe.

First of all, we recalla few elementary notions ofcosmology (see,e.g Chapter 2 of Kolb and Turner (199O) for more details and derivations). also in order to fix our notation. The expert reader might wish to skip this part and move on to page 194.

# A reminder of FRW kinematic

On the Gpc scale,the Universe is to a first approximation isotropic and homogeneous，and is described by the Friedmann-Robertson-Walker (FRW) metric,

$$
d s ^ { 2 } = - c ^ { 2 } d t ^ { 2 } + a ^ { 2 } ( t ) \left[ \frac { \dot { d } r ^ { 2 } } { 1 - | k r ^ { 2 } } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } \right] ,
$$

13Here the word “fat” refers to the geometry of the spatial slices.As a four-dimensional space-time,the FRW metric with $k = 0$ is curved.

where the function $a ( t )$ is called the scale factor and is determined by the Einstein equations.After an appropriate rescaling of the coordinates, $k$ can take the values $k = 0$ (fatUniverse13), $k = + 1$ (closed Universe) or $k = - 1$ (open Universe).We define $a ( t )$ as adimensional,so the dimensions of length are carried by $\boldsymbol { \uparrow }$ .The coordinates $( t , r , \theta , \phi )$ that appear above are called comoving cootdinates. This name reflects the property that a test mass,initially at rest in the comoving frame,remains at a fixed value of its comoving coordinates $r , \theta , \phi$ in spite of the expansion of the Universe. This can be ptoved writing down the geodesic equation in the metric (4.141) (just as we did in Section 1.3,when we understood the physical meaning of the TT gauge). From the $\mu = 0$ component, one finds

14Equation (4.142) also implies a much stronger result. If at $t = t _ { 0 }$ the velocity has an initial value $\mathbf { u } _ { 0 }$ ,the integration of eq. (4.142) gives

so spatial velocities are redshifted by the cosmological expansion.In a Universe which expands forever,even test masses with a non-vanishing initial value of u will eventually come to rest with respect to the observer that uses comoving coordinates.

$$
| \mathbf { u } ( t ) | = \frac { a ( t _ { 0 } ) } { a ( t ) } \left| \mathbf { u } _ { 0 } \right| ,
$$

$$
\frac { d | { \bf u } | } { d t } = - \frac { \dot { a } } { a } | { \bf u } | ,
$$

where $\vert \mathbf { u } \vert ^ { 2 } = g _ { i j } u ^ { i } u ^ { j }$ is the squared modulus of the spatial part of the four-velocity $u ^ { \mu }$ .This equation shows that,in the comoving frame,if at $t = t _ { 0 }$ the modulus of the four-velocity $| \mathbf { u } |$ is zero, then $d | \mathbf { u } | / d t$ also vanishes,so $\lvert \mathbf { u } \rvert$ remains zero at all times.14 This explains why these coordinates are called comoving: they “stretch” themselves，following the expansion of the Universe.If,at anl initial time,a star has comoving spatial coordinates $\left( r _ { 1 } , \theta _ { 1 } , \phi _ { 1 } \right)$ ，and a second star has comoving spatial coordinates $\left( r _ { 2 } , \theta _ { 2 } , \phi _ { 2 } \right)$ ,and if both stars have zero velocity, then at any subsequent time their comoving spatial coordinates will still be $( r _ { 1 } , \theta _ { 1 } , \phi _ { 1 } )$ and $\left( r _ { 2 } , \theta _ { 2 } , \phi _ { 2 } \right)$ ，respectively,and in particular their coordinate distance will be unchanged,in spite of the expansion of the Universe.Comparing with the discussion in Section 1.3.3,we see that comoving coordinates in a FRW space-time play the same role as TT coordinates in the space-time generated by a gravitational wave.

A star at $r = r _ { 1 }$ and a star at $r = r _ { 2 } ^ { \phantom { \dagger } }$ (and with the same values of $\theta$ and $\phi$ ）havea coordinate distance $r \big | = r _ { 2 } - r _ { 1 }$ .Of course,this quantity has no physical meaning,since coordinates are arbitrary in general relativity. The physical spatial distance is the proper spatial distance, $r _ { \mathrm { p h y s } } ( t )$ ，given by

$$
d r _ { \mathrm { p h y s } } ^ { 2 } = g _ { i j } d x ^ { i } d \vec { x } ^ { j } .
$$

$r$ $d r _ { \mathsf { p h y s } } ^ { 2 } = a ^ { 2 } ( t ) d r ^ { 2 } / ( 1 - k \bar { r ^ { 2 } } )$ ad therefore their physical distance is

$$
r _ { \mathrm { p h y s } } ( t ) = a ( t ) \int _ { 0 } ^ { r } \frac { d r } { ( 1 - k r ^ { 2 } ) ^ { 1 / 2 } } .
$$

In particular,fora fat Universe $( k = 0$ wehave $r _ { \mathrm { p h y s } } ( t ) = a ( t ) r$

Consider now a source located at combving distance $r$ ，that emits signals (such as electromagnetic or gravitational waves) which travel at the speed of light,and are later received byan observer located at $r = 0$ Suppose that the source emits a wavecrest at a time $t _ { \mathrm { e m i s } }$ . The signal will be detected by the observer at a time $t _ { \mathrm { o b s } }$ ，which is obtained by imposing $d s ^ { 2 } = 0$ in eq. (4.141). This gives

$$
\int _ { t _ { \mathrm { \tiny { e m i s } } } } ^ { t _ { \mathrm { \tiny { o b s } } } } \frac { c d t } { a ( t ) } = \int _ { 0 } ^ { r } \frac { d r } { ( 1 - k r ^ { 2 } ) ^ { 1 / 2 } } .
$$

Suppose that a second wavecrest is emitted at time $t _ { \mathrm { e m i s } } + \Delta t _ { \mathrm { e m i s } }$ ,and teceived at $t _ { \mathrm { o b s } } + \Delta t _ { \mathrm { o b s } }$ .Then

$$
\int _ { t _ { \mathrm { e m i s } } + \Delta t _ { \mathrm { e m i s } } } ^ { t _ { \mathrm { o b s } } + \Delta t _ { \mathrm { o b s } } } \frac { c d t } { a ( t ) } = \int _ { 0 } ^ { r } \frac { d r } { ( 1 - k r ^ { 2 } ) ^ { 1 / 2 } } .
$$

Observe that the right-hand side is alwaysthe same, since the source is ata fixed comoving distance.Then,taking the difference between these wo quations,the right-hand sides canceland,to linear order in $\Delta t _ { \mathrm { e m i s } }$ ， ene finds

$$
\Delta t _ { \mathrm { o b s } } = \frac { a ( t _ { \mathrm { o b s } } ) } { a ( t _ { \mathrm { e m i s } } ) } \Delta t _ { \mathrm { e m i s } } .
$$

I an expanding Universe,there is therefore a dilatation of the time measured by the observer,with respect td the time of the source. The mdshift of the source, $z$ ,isdefined by

$$
1 + z = \frac { a ( t _ { \mathrm { o b s } } ) } { a ( t _ { \mathrm { e m i s } } ) } .
$$

Equation (4.148) means that the time $t _ { \mathrm { o b s } }$ measured by the observer clock,and the time $t _ { s }$ measured by the source clock are related by

$$
d t _ { \mathrm { o b s } } = ( 1 + z ) d t _ { s } .
$$

As a consequence,any frequency measured by the observer,f(bs) related to the corresponding frequency measured in the source fram $f ^ { ( s ) }$ by

$$
f ^ { \mathrm { ( \mathrm { p b s } ) } } = \frac { f ^ { ( s ) } } { 1 + z } ,
$$

and the wavelengths are related by

$$
\lambda ^ { \mathrm { ( o b s ) } } = ( 1 + z ) \lambda ^ { ( s ) } .
$$

To complete our quick tour pf kinematics in a FRW space-time, need the definition of luminosity distance and the relation between t luminosity distance and the redshift.Let $\mathcal { F }$ be the energy flux (energ per unit time per unit area) measured in the observer's frame,and let be the absolute luminosity of the source,i.e. the power that it radiat in its rest frame,

$$
\mathcal { L } = \frac { d E _ { s } } { d t _ { s } } ,
$$

where $E _ { s }$ is the energy measured in the source proper frame. The luni nosity distance $d _ { L }$ is then defined by

$$
\overline { { \mathcal { F } = \frac { \mathcal { L } } { 4 \pi d _ { L } ^ { 2 } } } } .
$$

In the absence of redshift,the energy $E _ { \mathrm { o b s } }$ measured in the observe frame is the same as the energy $E _ { s }$ measured in the source frame,and $d t _ { \mathrm { o b s } } = d t _ { s }$ ，S0

$$
\frac { d { E } _ { \mathrm { { o b s } } } } { d t _ { \mathrm { { o b s } } } } = \frac { d { E } _ { s } } { d t _ { s } } .
$$

When it arrives at the detector,the energy radiated by an isotropl source is distributed over an area $A = 4 \pi r ^ { 2 }$ ,and therefore

$$
\begin{array} { l } { \displaystyle { \mathcal { F } \mathrm { = } \frac { 1 } { 4 \pi r ^ { \mathrm { 2 } } } \frac { d E _ { \mathrm { { o b s } } } } { d t _ { \mathrm { o b s } } } } } \\ { \displaystyle { \mathrm { = } \frac { 1 } { 4 \pi r ^ { \mathrm { 2 } } } \frac { d E _ { s } } { d t _ { s } } } } \\ { \displaystyle { \mathrm { = } \frac { \mathcal { L } } { 4 \pi r ^ { \mathrm { 2 } } } \mathrm { , } } } \end{array}
$$

which shows that,in the absence of redshift, $d _ { L }$ is just equal to the distance $r$ of the source. In an expanding Universe, however,the energy

observed is redshifted,

$$
E _ { \mathrm { o b s } } = \frac { E _ { s } } { 1 + z }
$$

(the quickest derivation of this result makes use of eq.(4.151),together with the quantum relation $E = \hbar \omega$ ，but this is a kinematic property that can also be derived purely classically)，while $d t _ { \mathrm { o b s } } = ( 1 + z ) d t _ { s }$ Therefore

$$
\frac { d E _ { \mathrm { o b s } } } { d t _ { \mathrm { o b s } } } = \frac { 1 } { ( 1 + z ) ^ { 2 } } \bigg | \frac { d E _ { s } } { d t _ { s } } .
$$

Furthermore,using the FRW metric (4.141),we find that,at time $t$ ,the surface of a sphere with comoving radius $\flat$ is $4 \pi a ^ { 2 } ( t ) r ^ { 2 }$ (independently of $k$ ),so when the radiation arrives at the detector it is spread over an area $A = 4 \pi a ^ { 2 } ( t _ { \mathrm { o b s } } ) r ^ { 2 }$ .Therefore

$$
\mathcal { F } = \frac { \mathcal { L } } { 4 \pi a ^ { 2 } ( t _ { \mathrm { o b s } } ) r ^ { 2 } ( 1 + z ) ^ { 2 } } ,
$$

which means that (setting $t _ { \mathrm { o b s } }$ equal to the present time $t _ { 0 }$ ）

$$
\boxed { \begin{array} { r l } { d _ { L } = ( 1 + z ) a ( t _ { 0 } ) r . } \end{array} }
$$

For small values of the redshift，we can express $d _ { L }$ as a function of $z$ as follows. We perform a Taylor expansion of $a ( t )$ around the present epoch $t = t _ { 0 }$ ，

$$
\frac { a ( t ) } { a ( t _ { 0 } ) } = 1 + H _ { 0 } ( t - t _ { 0 } ) - \frac { 1 } { 2 } q _ { 0 } H _ { 0 } ^ { 2 } ( t - t _ { 0 } ) ^ { 2 } + . . .
$$

where

$$
H _ { 0 } \equiv \frac { \dot { a } ( t _ { 0 } ) } { a ( t _ { 0 } ) } ,
$$

s the Hubble constant (or,more appropriately,the present value of the Hubble parameter $H ( t ) = { \dot { a } } / a$ ，while

$$
\begin{array} { r } { q _ { 0 } \equiv - \frac { \ddot { a } ( t _ { 0 } ) } { a ( t _ { 0 } ) } \frac { 1 } { H _ { 0 } ^ { 2 } } } \\ { = - \frac { a ( t _ { 0 } ) \ddot { a } ( t _ { 0 } ) } { \dot { a } ^ { 2 } ( t _ { 0 } ) } } \end{array}
$$

Bcalled the deceleration parameter.15 Using $a ( t _ { 0 } ) / a ( t ) = 1 + z$ ,eq. (4.161) can be inverted to give perturbatively $( t + t _ { 0 } )$ as a function of $z$ ,while inserting the expansion (4.161) into eq.(4.146) gives $a ( t _ { 0 } ) r$ ,as an expansion in powers of $( t - t _ { 0 } )$ and therefore of $z$ .The result is (see, e.g. Kolb and Turner (1990),pages 41-42 for the explicit calculation)

$$
\frac { \overline { { { H _ { 0 } d _ { L } } } } } { c } = z + { \frac { 1 } { 2 } } ( 1 - q _ { 0 } ) z ^ { 2 } + \dots .
$$

The first term of this expansion just gives the Hubble law $z \simeq ( H _ { 0 } / c ) d _ { L }$ shich states that redshifts are proportional to distances.The term $O ( z ^ { 2 } )$ the correction to the linear law for moderate redshifts.For large redhifts,the Taylor series is no longer appropriate,and the whole expansion

15This name is somewhat unfortunate, since it suggests that presently the expansion of the Universe is decelerating. Rather,we will see below that the evidence from the observation of type Ia supernovae indicates that presently the expansion of the Universe is accelerating,i.e. $q _ { 0 } < 0$

history of the Universe is encoded in a function $d _ { L } ( z )$ . As an example for a fat Universe $\left( k = 0 \right)$ ,eq.(4.146) gives

$$
\int _ { t _ { \mathrm { e m i s } } } ^ { t _ { \mathrm { o b s } } } { \frac { c d t } { a ( t ) } } = r .
$$

Differentiating the relation $1 + z ( t ) = a ( t _ { 0 } ) / a ( t )$ we get

$$
\frac { d t } { a ( t ) } \biggl | = - \frac { 1 } { a ( t _ { 0 } ) } \frac { d z } { H ( z ) } ,
$$

so eq. (4.165) becomes

$$
a ( t _ { 0 } ) \dot { r } = c \int _ { 0 } ^ { z } \frac { d z ^ { \prime } } { H ( z ^ { \prime } ) } ,
$$

where the upper limit in the integral is the redshift $z$ corresponding to the emission time $t _ { \mathrm { e m i s } }$ while,in the lower limit of the integral, we used the fact that at the present time $t = t _ { 0 }$ we have $z = 0$ .Then eq. (4.160) gives

$$
d _ { L } ( z ) = c ( 1 \vert + z ) \int _ { 0 } ^ { z } \frac { d z ^ { \prime } } { H ( z ^ { \prime } ) } ,
$$

or,taking a derivative with respect to $z$

$$
\frac { c } { H ( z ) } { = } \frac { d } { d z } \left( \frac { d _ { L } ( z ) } { 1 + z } \right) .
$$

Thus, from the knowledge of $d _ { L } ( z )$ ， we can get the Hubble parameter $H ( z )$ .This shows that the luminosity distance function $d _ { L } ( z )$ is a very important quantity,which encodes the whole expansion history of the Universe.

16Type Ia supernovae are modeled as carbon-oxygen white dwarfs,in a close binary system.They accrete matter from their companion until their mass reaches a critical value $\simeq 1 . 3 0 M _ { \odot }$ ,and then they explode as supernovae.Since the mass of the star at the moment of the explosion is always the same,the light curves of Type Ia supernovae are sufficiently similar to each other and, after applying corrections that take into account a relation between the shape of the light curve and the peak luminosity, they can be used as standard candles.

From the definition (4.154) we see that,in order to determine the luminosity distance of a source,we need to know both $\mathcal { F }$ and $\mathcal { L }$ Theflux $\mathcal { F }$ is the quantity that is directly measured by the observer.The problem is to know the intrinsic luminosity $\mathcal { L }$ of the source. This is possible if we have a“standard candle”, that is,a source whose absolute luminosity is known. The redshift of an electromagnetic source can be determined from the redshift of its spectral lines,and then we get the corresponding value of $d _ { L } ( z )$ .Up to distances of order $6 0 0 \mathrm { M p c }$ , standard candles are provided by Cepheid variable stars while,at larger cosmological distances，a standard candle is provided by Type Ia supernovae.16 The Hubble constant is usually written as $H _ { 0 } = h _ { 0 } \times 1 0 0 \mathrm { k m } \mathrm { s } ^ { - 1 } \mathrm { M p c } ^ { - 1 }$ and the most recent determination of $h _ { 0 }$ is $h _ { 0 } = 0 . 7 3 \pm 0 . 0 3$ ,while the value of the deceleration parameteris $q _ { 0 } = - 0 . 7 4 \pm 0 . 1 8$

# Propagation of GWs in a FRW Universe

We can now discuss how the waveform produced by a binary inspiral is modified by the propagation across cosmological distances. First of all, we can define a local wave zone,as the region where the distance to the source is sufficiently large so that the gravitational field already has the $1 / r$ behavior characteristic of waves,but|still sufficiently small,so that the expansion of the Universe is negligible. During the propagation of the GW in the local wave zone,the scale factor $a ( t )$ does not change appreciably,so in the local wave zone physical distances can be written as $r _ { \mathrm { p h y s } } = a ( t _ { \mathrm { e m i s } } ) r$ where $r$ is the comoving distance and $t _ { \mathrm { e m i s } }$ is (any) time of emission,17 s0 $r _ { \mathrm { p h y s } }$ differs from $\nmid$ by just a constant normalization factor. Using eq.(4.29) we see that the GW produced by a binary inspiral,at a distance $r _ { \mathrm { p h y s } } = a ( t _ { \mathrm { e m i s } } ) r$ in the local wave zone,can be written as

$$
\begin{array} { l } { { \displaystyle h _ { + } ( t _ { s } ) = h _ { c } ( t _ { s } ^ { \mathrm { r e t } } ) \frac { 1 + \cos ^ { 2 } \iota } { 2 } \cos \left[ 2 \pi \int ^ { t _ { s } ^ { \mathrm { r e t } } } d t _ { s } ^ { \prime } f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \prime } ) \right] \mathrm { , } } } \\ { { \displaystyle h _ { \times } ( t _ { s } ) = h _ { c } ( t _ { s } ^ { \mathrm { r e t } } ) \cos \iota \sin \left[ 2 \pi \int ^ { t _ { s } ^ { \mathrm { r e t } } } d t _ { s } ^ { \prime } f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \prime } ) \right] \mathrm { , } } } \end{array}
$$

where

$$
h _ { c } ( t _ { s } ^ { \mathrm { r e t } } ) = \frac { 4 } { a ( t _ { \mathrm { e m i s } } ) r } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \mathrm { r e t } } ) } { c } \right) ^ { 2 / 3 } .
$$

$t _ { s }$ $t _ { s } ^ { \mathrm { r e t } }$ $f _ { \mathrm { g w } }$ isthe one associatedtothis defiitionoftime,that wedenoteby $f _ { \mathrm { g w } } ^ { ( s ) }$ They are related to the quantities measured by the observer which is at a cosmological distance,very far from the lbcal wave zone,by eqs.(4.150) d (4.151). The dependence of $f _ { \mathrm { g w } } ^ { ( s ) } \ \mathrm { o n } \vert t _ { s }$ is given by eq. (4.19), that werewriteas

$$
f _ { \mathrm { g w } } ^ { ( s ) } ( \tau _ { s } ) = \frac { 1 } { \pi } \left( \frac { 5 } { 2 5 6 } \frac { 1 } { \tau _ { s } } \right) ^ { 3 / 8 } \left( \frac { G M _ { c } } { c ^ { 3 } } \right) ^ { - 5 / 8 } ,
$$

where $\tau _ { s }$ is the time to coalescence measured by the source's clock.

To compute how this waveform propdgates across cosmological distances to reach the observer,we should use eq.(1.179), that describes the propagation of GWs in a curved space-time,specializing it to the FRW metric.Actually,it is instructive to start from a simpler problem, namely the propagation of a scalar perturbation $\phi$ in the FRW metric. Ih this case, the propagation equation is simply $\boldsymbol { \Xi } \phi = 0$ where,on scalar fimctions,the curved-space d'Alembertiah $\Xi = D _ { \mu } D ^ { \mu }$ can be written as

$$
\sqcup = \frac { 1 } { \sqrt { - g } } \partial _ { \mu } \bigl ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } \bigr ) .
$$

Io solve this wave equation in the FRW metric, it is convenient to imtroduce the conformal time $\eta$ ,from

$$
d \eta = \frac { d t } { a ( t ) } ,
$$

17We do not need to track the change of the scale factor during the observed part of the emission process,so we do not need to be more precise about $t _ { \odot \mathrm { m i s } }$

$$
\eta = \int ^ { t } \frac { d t ^ { \prime } } { a ( t ^ { \prime } ) } ,
$$

so the FRW metric reads (limiting ourselves for simplicity to $k = 0$

$$
d s ^ { 2 } = a ^ { 2 } ( \eta ) \left[ - c ^ { 2 } d \eta ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \theta ^ { 2 } + r ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } \right] .
$$

We want to know how a solution which decreases as $1 / r$ evolves in this space-time. We therefore search for spherically symmetric solutions ol the form $\phi ( r , \eta ) = ( 1 / r ) f ( r , \eta ) ,$ The equation $\boldsymbol { \Sigma } \boldsymbol { \phi } = 0$ in this metric then becomes

$$
\begin{array} { l } { { 0 = \partial _ { \mu } ( \sqrt { - g } g ^ { \mu \nu } \partial _ { \nu } ) \phi } } \\ { { { } ~ = - { \displaystyle \frac { 1 } { c ^ { 2 } } } \partial _ { \eta } \left[ a ^ { 2 } ( \eta ) r ^ { 2 } \partial _ { \eta } \phi \right] + \partial _ { r } \left[ a ^ { 2 } ( \eta ) r ^ { 2 } \partial _ { r } \phi \right] } } \\ { { { } ~ = \partial _ { r } ^ { 2 } f - f ^ { \prime \prime } - \displaystyle \frac { 2 \frac { a ^ { \prime } } { a } f ^ { \prime } } { a } f ^ { \prime } , } } \end{array}
$$

where the prime denotes derivation with respect to cn, $f ^ { \prime } = ( 1 / c ) \partial f / \partial n$ It is convenient to search for the solution in the form

$$
f ( r , \eta ) = \frac { 1 } { a ( \eta ) } g ( r , \eta ) .
$$

Then $g ( r , \eta )$ satisfies the equation

$$
\partial _ { r } ^ { 2 } g - g ^ { \prime \prime } + { \frac { a ^ { \prime \prime } } { a } } g = 0 .
$$

18More precisely，we are interested in the evolution in a matter-dominated Universe (since we need that stars already formed!).In this case the FRW scale factor evolves as $a ( \eta ) \sim \eta ^ { 2 }$ and $a ^ { \prime \prime } / a = 2 / \eta ^ { 2 }$ .Instead,inaradiationdominated Universe, $a ( \eta ) ~ \sim ~ \eta$ and $a ^ { \prime \prime } / a = 0$

Now observe that $a ^ { \prime \prime } / a \sim \eta ^ { - 2 }$ ,for dimensional reasons.18 Then we see that eq.(4.180) has the apprqximate solutions

$$
g ( r , \eta ) \simeq e ^ { \pm i \omega ( \eta - r / c ) } ,
$$

as long as $\omega ^ { 2 } \gg 1 / \eta ^ { 2 }$ ,since inthis casein eq.(4.180) the term $( a ^ { \prime \prime } / a ) g \sim$ $g / \eta ^ { 2 }$ is negligible with respeot to $- g ^ { \prime \prime } = \omega ^ { 2 } g$ ，and we are left with & simple wave equation $\partial _ { r } ^ { 2 } g - g ^ { \dot { \prime } \prime } \simeq 0$ .More generally,any function of the form $g ( \eta - r / c )$ is a solution,as long as in Fourier space it contains only frequencies such that $\eta ^ { 2 } \omega ^ { 2 } \gg \natural$ . In conclusion, we have the approximate solution

$$
\phi ( r , \eta ) \mathrel { \mathop { \sim } } \frac { 1 } { r a ( \eta ) } g ( \eta - r / c ) .
$$

190bviously，since a(n) evolvesapre ciably only on a cosmological timescale,once we fix $\eta = t$ at one moment of time in the present epoch,we have $\eta = t$ ，with exceedingly good accuracy, over the whole time-scale relevant for GW observation at a detector，so we can write $g ( \eta - r / c ) = g ( t - r / c )$ for all these values of time. For the same reason, $a ( \eta )$ can be written simply as a constant factor $a ( t _ { 0 } )$

We can normalize conformal time so that,at the present epoch, $\eta = t$ Then,the wave observed today at a detector reads19

$$
\phi ( r , t ) \simeq \frac { 1 } { r a ( t _ { 0 } ) } g ( t - r / c ) .
$$

Thus,the propagation of a scalar wave through a FRW background is very simple. Compared to the solution in the absence of cosmological expansion,we just need to replace the factor $1 / r$ with $1 / [ r a ( t ) ]$

Now we can turn to the propagation equation of a tensor perturbation $h _ { \mu \nu }$ ,eq.(1.179).It is in principle straightforward to write down this equation explicitly in the FRW metric (4.177)；we then find that,once we disregard all terms $O ( 1 / \eta ^ { 2 } ) h _ { \mu \nu }$ with respect to the terms $O ( \omega ^ { 2 } ) h _ { \mu \nu }$ ， we get back the same equation that we discussed for scalar perturbations.Of course,this is not surprising. Simply,the condition $\eta ^ { 2 } \omega ^ { 2 } \gg 1$ demands that $\omega$ be large with respect tolthe typical scale of the background space-time and this is nothing but the condition that defines the geometrical optics approximation.In this approximation all massless particles follow null geodesics, independently of their spin,as we saw in Section 1.5.1.

Then we find that, to leading order:

·The two polarizations $h _ { + }$ and $h _ { \times }$ decouple,that is each one satisfes a wave equation which is independent of the other. This means that the propagation does not introduces a mixing among them. For instance,if we observe the binary edge-on ( $\cos \iota = 0 \rangle$ ，wesee from eqs.(4.17O) and (4.171) that ih the local wave zone the GW has only the plus polarization; then even after propagation across a cosmological distance,the wave will still have only the plus polarization. This is as expected,since we already saw in Section 1.5.1 that the polarization tensor of GWs is parallel-propagated along the null geodesics.   
·Both $h _ { + }$ and $h _ { \times }$ satisfy the same equation that we discussed above for a scalar feld.

The conclusion is that,after propagation from the source to the detor, the GW amplitude from an inspiraling binary is still given by . (4.170) and (4.171),but with $h _ { c }$ in eq.(4.172) replaced by

$$
h _ { c } ( t _ { s } ^ { \mathrm { r e t } } ) = \frac { 4 } { a ( t _ { 0 } ) r } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \mathrm { r e t } } ) } { c } \right) ^ { 2 / 3 } ,
$$

long as the geometrical optics approximation is valid. Today this condition is $2 \pi f _ { \mathrm { g w } } \gg t _ { 0 } ^ { - 1 }$ ,where $t _ { 0 }$ is the present age of the Universe, mdl therefore is satisfied with extreme accuracy by all GWs in which we einterested (in fact,by all GWs whose wavelength is smaller than the mtsent Hubble size of the Universe!).More generally,also the condition $\pm f _ { \mathrm { 8 w } } \gg t _ { \mathrm { e m i s } } ^ { - 1 }$ is extremely well satisfied,so the geometrical optics apoximation is excellent for the whole propagation of the GW from the ource to the detector.

In principle eqs.(4.170) and (4.171),together with eq. (4.184),provide l final result.However,it is convenient to express them in terms of time tobs and the GW frequency fgwb measured by the observer, mther than using the time $t _ { s }$ measured by the source and its associated quency.Using eqs. (4.150) and (4.15l)，we see that,in eqs. (4.170) m（4.171）,

$$
\int ^ { t _ { s } ^ { \mathrm { r e t } } } d t _ { s } ^ { \prime } f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \prime } ) = \int ^ { t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } } d t _ { \mathrm { o b s } } ^ { \prime } f _ { \mathrm { g w } } ^ { ( \mathrm { o b s } ) } ( t _ { \mathrm { o b s } } ^ { \prime } )
$$

mce the redshift in $d t$ cancels the redshift in $f$ Writing

$$
f _ { \mathrm { g w } } ^ { ( s ) } = ( 1 + z ) f _ { \mathrm { g w } } ^ { ( \mathrm { o b s } ) } ,
$$

eq. (4.184) becomes

$$
\begin{array} { r } { h _ { c } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) = \displaystyle \frac { 4 } { a ( t _ { 0 } ) r } \left( 1 + z \right) ^ { 2 / 3 } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) } { c } \right) ^ { 2 / 3 } } \\ { = \displaystyle \frac { 4 } { d _ { L } ( z ) } \left( 1 + z \right) ^ { 5 / 3 } \left( \frac { G M _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) } { c } \right) ^ { 2 / 3 } , \left( \right) } \end{array}
$$

where in the second line we expressed the result in terms of the luminosity distance,using eq. (4.16p). We see that, if we define the quantity

$$
\mathcal { M } _ { c } \equiv ( 1 + z ) M _ { c } \Big \vert = ( 1 + z ) \mu ^ { 3 / 5 } m ^ { 2 / 5 } , \qquad 
$$

we get

$$
h _ { c } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) = \frac { 4 } { d _ { L } } \left( \frac { G \mathcal { M } _ { c } } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { g w } } ^ { ( \mathrm { o b s } ) } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) } { c } \right) ^ { 2 / 3 } ,
$$

and therefore the GW amplitude takes the same form as in the absence of cosmological expansion,with the replacements $r  d _ { L }$ and $M _ { c }  \mathcal { M } _ { c }$ In the general case of non-vanishing redshift,we will reserve the name “chirp mass” for $\boldsymbol { \mathcal { M } } _ { c }$ ,rather than for $M _ { c }$ .From eqs. (4.151) and (4.173). we find that the dependence of $f _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } }$ on $t _ { \mathrm { o b s } }$ is given by

$$
\begin{array} { l } { { f _ { \mathrm { g w } } ^ { ( \mathrm { o b s } ) } ( t _ { \mathrm { o b s } } ^ { \mathrm { r e t } } ) = \displaystyle \frac { 1 } { 1 + z } ~ f _ { \mathrm { g w } } ^ { ( s ) } ( t _ { s } ^ { \mathrm { r e t } } ) } } \\ { { ~ = \displaystyle \frac { 1 } { 1 + z } ~ \frac { 1 } { \pi } \left( \frac { 5 } { 2 5 6 } \frac { 1 + z } { \tau _ { \mathrm { o b s } } } \right) ^ { 3 / 8 } \left( \frac { G M _ { c } } { c ^ { 3 } } \right) ^ { - 5 / 8 } } } \\ { { ~ = \displaystyle \frac { 1 } { \pi } \left( \frac { 5 } { 2 5 6 } \frac { 1 } { \tau _ { \mathrm { o b s } } } \right) ^ { 3 / 8 } \left( \frac { G \mathcal { M } _ { c } } { c ^ { 3 } } \right) ^ { - 5 / 8 } , } } \end{array}
$$

20Since $\tau = t _ { \mathrm { c o a l } } ^ { \mathrm { r e t } } - t ^ { \mathrm { r e t } } = t _ { \mathrm { c o a l } } - t$ we $\tau = \tau ^ { \mathrm { r e t } }$ ，and the result can be written just as a function of the observer's time,rather than of the observer's retarded time.

where $\tau _ { \mathrm { o b s } } = ( 1 + z ) \tau _ { s }$ is the time to coalescence measured by the observer'scock.20 Then,eventhedependenceof $f _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } }$ on $t _ { \mathrm { o b s } }$ is formally the same as the relation at $z | = 0$ ，once we replace $M _ { c }  \mathcal { M } _ { c }$ This result is due to the fact that,when $z ~ = ~ 0$ ，both the GW amplitude and the evolution of the frequency with time are determined by the only time-scale of the problem which is $G M _ { c } / c ^ { 3 }$ . What we are actually finding is that,in a cosmological context, this time-scale is redshifted, $G M _ { c } / c ^ { 3 }  ( 1 + z ) G M _ { c } / c ^ { 3 }$ . This is a very natural result,which formally amounts to the replacement $M _ { c }  ( 1 + z ) M _ { c }$

To summarize, the signal received by the observed from a binary inspiral at redshift $z$ ， when expressed in terms of the observer time $t _ { \mathrm { o b s } }$ or equivalently in terms of the time to coalescence measured by the observer, $\tau _ { \mathrm { { o b s } } }$ ,is given by

$$
\begin{array} { l } { { \displaystyle h _ { + } ( \tau _ { \mathrm { o b s } } ) = h _ { c } ( \tau _ { \mathrm { o b s } } ) \frac { 1 + \cos ^ { 2 } \iota } { 2 } ~ \cos \left[ \Phi ( \tau _ { \mathrm { o b s } } ) \right] , } } \\ { { \displaystyle h _ { \times } \left( \tau _ { \mathrm { o b s } } \right) = h _ { c } ( \tau _ { \mathrm { o b s } } ) ~ \cos \iota ~ \sin \left[ \Phi ( \tau _ { \mathrm { o b s } } ) \right] } } \end{array}
$$

where (compare with eq. (4.30)),

$$
\begin{array} { c } { { \displaystyle \Phi ( \tau _ { \mathrm { \tiny { o b s } } } ) = - 2 \left( \frac { 5 G { \mathcal M } _ { c } ( z ) } { c ^ { 3 } } \right) ^ { - 5 / 8 } \tau _ { \mathrm { \tiny { o b s } } } ^ { 5 / 8 } + \Phi _ { 0 } , } } \\ { { h _ { c } ( \tau _ { \mathrm { \tiny { o b s } } } ) = \displaystyle \frac { 4 } { d _ { L } ( z ) } \left( \frac { G { \mathcal M } _ { c } ( z ) } { c ^ { 2 } } \right) ^ { 5 / 3 } \left( \frac { \pi f _ { \mathrm { \tiny { g w } } } ^ { ( \mathrm { \tiny { o b s } } } ) } { c } \Big ( \tau _ { \mathrm { \tiny { o b s } } } \Big ) \right) ^ { 2 / 3 } , } } \end{array}
$$

$$
f _ { \mathrm { g w } } ^ { ( \mathrm { o b s } ) } ( \tau _ { \mathrm { o b s } } ) = \frac { 1 } { \pi } \left( \frac { 5 } { 2 5 6 } \frac { 1 } { \tau _ { \mathrm { o b s } } } \right) ^ { 3 / 8 } \left( \frac { G \mathcal { M } _ { c } ( z ) } { c ^ { 3 } } \right) ^ { - 5 / 8 } .
$$

The latter equation implies also that

$$
\dot { f } _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } } = \frac { 9 6 } { 5 } \pi ^ { 8 / 3 } \left( \frac { G { \mathcal M } _ { c } ( z ) } { c ^ { 3 } } \right) ^ { 5 / 3 } [ f _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } } ] ^ { 1 1 / 3 } .
$$

In other words,we have the following modifications compared to the case $z = 0$ ：

· The observed frequency is redshifted with respect to the frequency imeasured in the source frame, $f ^ { ( \mathrm { o b s } ) } = f ^ { ( s ) } / ( 1 + z )$ .For instance, we saw below eq.(4.4O) that the inspiral of a NS-NS binary system terminates,and the two stars merge,when the intrinsic orbital frequency of the source,in the source frame,is of order $8 0 0 ~ \mathrm { H z }$ This means that,from the point of view of the observer,the orbital frequency of the source will sweep up to a maximum value of order $8 0 0 \mathrm { H z } / ( 1 + z )$ ．For example, for a NS-NS coalescence at $z \simeq 2$ ， the maximum value of the source orbital frequency,in the observer frame,is of order $2 7 0 \mathrm { H z }$ ,and the quadrupole radiation emitted in the inspiral phase will be cutoff at twice this value.

·The overall factor $1 / r$ in the GW amplitude is replaced by $1 / d _ { L } ( z )$ · $M _ { c }$ is replaced by $\dot { \mathcal { M } } _ { c } = ( 1 + z ) M _ { c }$

A very interesting consequence of the above results is the follow-Suppose that we can measure the amplitudes of both polarizations $h _ { + } , h _ { x }$ as well as $\dot { f } _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } }$ The amplitude of $h _ { + }$ is $h _ { c } ( 1 + \cos ^ { 2 } \iota ) / 2$ ,while ihe amplitude of h× is hc cost.From their ratio,we can therefore obtain the value of $\cos \iota$ ,that is,the inclination of the orbit with respect to the line of sight. On the other hand,eq. (4.196) shows that,if we measure htevale of $\dot { f } _ { \mathrm { g w } } ^ { \mathrm { ( o b s ) } }$ chirp mass $\mathcal { M } _ { c }$ .Now in the expression for $h _ { + }$ and $h _ { \times }$ all parameters have been fixed，except $d _ { L } ( z )$ .2i This means that, from the measured vlue of $h _ { + }$ (orof $h _ { \times }$ ) we can now read $\nmid d _ { L }$ .If,at the same time,we can measure the redshift $z$ of the source,we have found a gravitational stanard candle,and we can use it to measure the Hubble parameter $H ( z )$ ， ompare with eq. (4.168).We will discuss in Vol.2 the rich cosmological Iiformation that can be obtained from this type of measurements,as well the methods proposed to have an associated measure of the redshift ither from optical observations or from GW observations themselves), nd the associated experimental uncertainties.

2lObserve that theellpticityof the orbit does not enter since,as we discussed in Section 4.1.3,by the time that the stars approach the coalescence stage,angular momentum losses have circularized the orbit to great accuracy. Therefore it is legitimate to use the results for circular orbits,as we have done in this section,and there is no free parameter associated to the ellipticity.

# 4.2Radiation from rotating rigid bodies

The production of GWs from a rotating rigid body is of great impor tance,in particular for application to isolated neutron stars. In Sec tion 4.2.1 we examine the production of GWs in the simplest situation i.e.the radiation emitted by a rigid body which rotates around one of its principal axes. Then, in Section 4.2.2,we will discuss the more complicated situation where the rotation axis does not coincide with a principal axis,and therefore there is a motion of precession.

Let us first recall, from elementary mechanics (see e.g. Landau and Lifshitz,Vol.I1976),a few basic notions of kinematics of rigid bodies. A rigid body is characterized by its inertia tensor

$$
I ^ { i j } = \int d ^ { 3 } x \rho ( { \bf x } ) ( r ^ { 2 } \delta ^ { i j } - x ^ { i } x ^ { j } ) .
$$

where $\rho$ is the mass density. Since any hermitian matrix can be diag onalized by an appropriate rotation,there exists an orthogonal frame where $I _ { i j }$ is diagonal. The corresponding axes are called the principal axes of the body,and the eigenvalues $I _ { 1 } , I _ { 2 } , I _ { 3 }$ are called the principal moments of inertia.We will refer to the frame where $I _ { i j }$ is diagonal as the“body frame”.Denoting by $x _ { i } ^ { \prime }$ the coordinates in the body frame. we have

$$
\begin{array} { l } { { \displaystyle I _ { 1 } = \int d ^ { 3 } x ^ { \prime } \rho ( { \bf x ^ { \prime } } ) ( { x ^ { \prime } } _ { 2 } ^ { 2 } + { x ^ { \prime } } _ { 3 } ^ { 2 } ) } , } \\ { { \displaystyle I _ { 2 } = \int d ^ { 3 } x \rho ( { \bf x ^ { \prime } } ) ( { x ^ { \prime } } _ { 1 } ^ { 2 } + { x ^ { \prime } } _ { 3 } ^ { 2 } ) } , } \\ { { \displaystyle I _ { 3 } = \int d ^ { 3 } x \rho ( { \bf x ^ { \prime } } ) ( { x ^ { \prime } } _ { 1 } ^ { 2 } + { x ^ { \prime } } _ { 2 } ^ { 2 } ) . } } \end{array}
$$

From these explicit expressions we see that $I _ { 1 } + I _ { 2 } \geqslant I _ { 3 }$ .Therefore each principal moment of inertia must be smaller or equal than the sum of the other two.The identity $I _ { 1 } + I _ { 2 } = I _ { 3 }$ holds only if $\rho ( \mathbf { x } ) \sim \delta ( x _ { 3 } )$ ,that is,for a bidimensional configuration of matter.

A simple geometry is that of an ellipsoid with semiaxes $a , b , c ,$ uniform density,and mass $m$ .In this case,eqs.(4.198)-(4.200) give

$$
\begin{array} { c } { { I _ { 1 } { = } \displaystyle { \frac { m } { 5 } } \left( b ^ { 2 } + c ^ { 2 } \right) , } } \\ { { I _ { 2 } { = } \displaystyle { \frac { m } { 5 } } \left( a ^ { 2 } + c ^ { 2 } \right) , } } \\ { { I _ { 3 } { = } \displaystyle { \frac { m } { 5 } } \left( a ^ { 2 } + b ^ { 2 } \right) . } } \end{array}
$$

If the body rotates with angular velocity $\omega$ , its angular momentum is

$$
{ J } _ { i } = I _ { i j } { \omega } _ { j } .
$$

We denote by $( J _ { 1 } ^ { \prime } , J _ { 2 } ^ { \prime } , J _ { 3 } ^ { \prime } )$ and $( \omega _ { 1 } ^ { \prime } , \omega _ { 2 } ^ { \prime } , \omega _ { 3 } ^ { \prime } )$ the components of the angular momentum and of theangular velocity,respectively,in the body frame. Then ${ { J } _ { 1 } ^ { \prime } } = { { I } _ { 1 } } { { \omega } _ { 1 } ^ { \prime } }$ ， ${ { J } _ { 2 } ^ { \prime } } = { { I } _ { 2 } } { \omega } _ { 2 } ^ { \prime }$ and ${ { J } _ { 3 } ^ { \prime } } = { { I } _ { 3 } } { { \omega } _ { 3 } ^ { \prime } }$ .Observe that the direction

of $\omega$ is different from the direction of $\mathbf { J }$ unless either $I _ { 1 } = I _ { 2 } = I _ { 3 }$ (which holds only for a spherical object) or the rotation is around one of the principal axes,e.g.when, $\omega _ { 1 } ^ { \prime } = \omega _ { 2 } ^ { \prime } = 0$ .The rotational kinetic energy is

$$
E _ { \mathrm { r o t } } = \frac { 1 } { 2 } I _ { i j } \omega _ { i } \omega _ { j } \ ,
$$

$\mathrm { s o }$ in the body frame it is given simply by

$$
E _ { \mathrm { r o t } } = { \frac { 1 } { 2 } } ( I _ { 1 } { \omega _ { 1 } ^ { \prime } } ^ { 2 } + I _ { 2 } { \omega _ { 2 } ^ { \prime } } ^ { 2 } + I _ { 3 } { \omega _ { 3 } ^ { \prime } } ^ { 2 } ) .
$$

If we denote by $\hat { \omega }$ the unit vector in the direction of the axis of rotation, $\mathrm { s o }$ that $\boldsymbol { \omega } = \omega \hat { \boldsymbol { \omega } }$ ,then $E _ { \mathrm { r o t } } = ( 1 / 2 ) I \omega ^ { 2 }$ where $I = I _ { i j } \hat { \omega } _ { i } \hat { \omega } _ { j }$ is called the moment of inertia about the axis of rotation.

# 4.2.1 GWs from rotation around a principal axis

We first consider the situation in which the body rotates rigidly about oue of its principal axes.We denote by $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ the coordinates in the body frame.This reference frame,by definition,is attached to the body and rotates with it.We take the $x _ { 3 } ^ { \prime }$ axis as the axis around which the body rotate,and we denote by $\omega _ { \mathrm { r o t } }$ the corresponding angular velocity. We also introduce a fixed reference frame,with coordinates $\left( x _ { 1 } , x _ { 2 } , x _ { 3 } \right)$ ， oriented so that $x _ { 3 } ^ { \prime } = x _ { 3 }$ ,see Fig.4.13.In both frames,the origin of the axes coincides with the center-of-mass of the body. The two frames are Telated by a time-dependent rotation matrix $\mathcal { R } _ { i j }$ ，

with

$$
\mathcal { R } _ { i j } = \left( \begin{array} { c c c } { \cos \omega _ { \mathrm { r o t } } t } & { \sin \omega _ { \mathrm { r o t } } t } & { 0 } \\ { - \sin \omega _ { \mathrm { r o t } } t } & { \cos \omega _ { \mathrm { r o t } } t } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) _ { i j } .
$$

We denote by $\begin{array} { r } { I _ { i j } ^ { \prime } = \mathrm { d i a g } ( I _ { 1 } , I _ { 2 } , I _ { 3 } ) } \end{array}$ the inertia tensor in the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ wordinate system，and by $I _ { i j }$ its components in the $\left( x _ { 1 } , x _ { 2 } , x _ { 3 } \right)$ frame. Thus, ${ { I } } _ { i j } ^ { \prime }$ is a constant matrix,while $I _ { i j }$ is time-dependent. The fact that the moment of inertia is a tensor implies that

$$
\begin{array} { r } { I _ { i j } ^ { \prime } = \mathcal { R } _ { i k } \mathcal { R } _ { j l } I _ { k l } } \\ { = ( \mathcal { R } I \mathcal { R } ^ { T } ) _ { i j } , } \end{array}
$$

where $\mathcal { R } ^ { T }$ is the transpose matrix,and therefore

This gives

![](images/6dcb8ec6225ffd6ad325c1791e465ba1399d5a670162f694c7ec87a02c1e79f4.jpg)  
Fig.4.13 Theprincipalaxes $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ ，which rotate with the rigid body，and the fixed axes $\left( x _ { 1 } , x _ { 2 } , x _ { 3 } \right)$

$$
\begin{array} { r l } & { I _ { 1 2 } = \displaystyle \frac { I _ { 1 } + I _ { 2 } } { 2 } \sin { 2 \omega _ { \mathrm { r o t } } t } , } \\ & { I _ { 2 2 } = I _ { 1 } \sin ^ { 2 } { \omega _ { \mathrm { r o t } } t } + I _ { 2 } \cos ^ { 2 } { \omega _ { \mathrm { r o t } } t } } \\ & { \quad \quad = 1 - \displaystyle \frac { I _ { 1 } - I _ { 2 } } { 2 } \cos { 2 \omega _ { \mathrm { r o t } } t } , } \\ & { I _ { 3 3 } = I _ { 3 } , } \end{array}
$$

22Actually，for a relativisticsource (and in the approximation that the internal gravitational felds are not strong) $\bar { M } ^ { i j }$ is really the second moment of $T ^ { 0 0 } / c ^ { 2 }$ ,i.e.the energy density over $c ^ { 2 }$ .For non-relativistic internal motions, $T ^ { 0 0 } / c ^ { 2 }$ becomes equal to the mass density $\rho$ Otherwise,all the arguments below go through if,in the definition of $I ^ { i j }$ ,we define $\rho$ tobe $T ^ { 0 0 } / c ^ { 2 }$

while $I _ { 1 3 } = I _ { 2 3 } = 0$ . Recall that in the quadrupole approximation thl GW amplitude depends on the second moment of the mass density $M ^ { i j }$ From eq.(4.197) we see that $M ^ { i j }$ differ from $I ^ { i j }$ by an overall minus sign,and for the absence of the trace term.22 However,the trace of tensor is invariant under rotation; in fact，from eq. (4.209),using the cyclic property of the trace and the property of the orthogonal matrice that $\mathcal { R R } ^ { T }$ is equal to the identity matrix,we have $\mathrm { T r } { \cal I } = \mathrm { T r } \left[ { \mathcal R } ^ { T } { \cal I } ^ { \prime } { \mathcal R } \right] =$ $\operatorname { T r } \left[ I ^ { \prime } { \mathcal { R } } { \mathcal { R } } ^ { T } \right] = \operatorname { T r } I ^ { \prime }$ Since ${ \mathrm { T r } } { \dot { I ^ { \prime } } } = I _ { 1 } + I _ { 2 } + I _ { 3 }$ is a constant, we have

$$
\left. M _ { i j } \right. = - I _ { i j } + c _ { i j } ,
$$

where $c _ { i j }$ are constants. In the computation of the GW amplitude only the second time derivative of $\dot { M } _ { i j }$ enters and therefore the explicit value of the constants is irrelevant,and we can write

![](images/2df8a66a5f89b81b234ec28628d133aa1efc7f5cdc9753c045257876f5cb030c.jpg)  
Fig.4.14 The rigid body rotating around the $x _ { 3 }$ axis; $\iota$ is the angle between the line-of-sight and the $x _ { 3 }$ axis.

$$
\begin{array} { l } { { \displaystyle M _ { 1 1 } = - \frac { I _ { 1 } - | I _ { 2 } } { 2 } \cos 2 \omega _ { \mathrm { r o t } } t + \mathrm { c o n s t a n t } \ : , } } \\ { { \displaystyle M _ { 1 2 } = - \frac { I _ { 1 } - | I _ { 2 } } { 2 } \sin 2 \omega _ { \mathrm { r o t } } t + \mathrm { c o n s t a n t } \ : , } } \\ { { \displaystyle M _ { 2 2 } = + \frac { I _ { 1 } - | I _ { 2 } } { 2 } \cos 2 \omega _ { \mathrm { r o t } } t + \mathrm { c o n s t a n t } \ : , } } \end{array}
$$

while $M _ { 1 3 }$ ， $M _ { 2 3 }$ and $M _ { 3 3 }$ are constant. We observe that,in our set ting in which the body rotates around its principal axis $x _ { 3 } ^ { \prime }$ ，thereis a time-varying second mass moment only if $I _ { 1 } \ne I _ { 2 }$ ，which is quite clear geometrically.We also see that $M _ { i j }$ is a periodic function of $2 \omega _ { \mathrm { r o t } } t$ ,sowe already understand that we have production of GWs with a frequency $\omega _ { \mathrm { g w } } = 2 \omega _ { \mathrm { r o t } }$

We can now compute the GW amplitude received by an observer at a distance $r$ ,whose line-of-sight nakes an angle $\iota$ with the direction of the spin of the star,i.e.with the $x _ { 3 }$ axis,see Fig. 4.14. We use eq. (3.72). setting with $\theta = \iota$ and,without loss of generality,we orient the fixed frame $\left( x _ { 1 } , x _ { 2 } , x _ { 3 } \right)$ so that the observer is at $\phi = 0$

Inserting the expressions (4216)-(4.218) for $M _ { i j }$ and taking into account that $\ddot { M } _ { 1 3 } = \ddot { M } _ { 2 3 } = \ddot { M } _ { 3 3 } = 0$ ,eq.(3.72) gives

$$
\begin{array} { r l } & { h _ { + } = \displaystyle \frac { 1 } { r } \frac { 4 G \omega _ { \mathrm { r o t } } ^ { 2 } } { c ^ { 4 } } \big ( I _ { 1 } - I _ { 2 } \big ) \frac { 1 + \cos ^ { 2 } \iota } { 2 } \cos \big ( 2 \omega _ { \mathrm { r o t } } t \big ) , } \\ & { h _ { \times } = \displaystyle \frac { 1 } { r } \frac { 4 G \omega _ { \mathrm { r o t } } ^ { 2 } } { c ^ { 4 } } \big ( I _ { 1 } - I _ { 2 } \big ) \cos \iota \sin \big ( 2 \omega _ { \mathrm { r o t } } t \big ) . } \end{array}
$$

We therefore have a periodic GW, with $\omega _ { \mathrm { g w } } = 2 \omega _ { \mathrm { r o t } }$ . The fact that $h _ { + }$ is proportional to $( 1 + \cos ^ { 2 } \iota ) / 2$ ,while $h _ { \times }$ to $\cos \iota$ ,is the same result that we found for the GW amplitude of a binary system in a circular orbit.

see eq. (3.332). In fact,this is a generic property of eq.(3.72) whenever

It is useful todefine the ellipticity $\epsilon$ by

$$
\epsilon \equiv \frac { I _ { 1 } - I _ { 2 } } { I _ { 3 } } .
$$

For instance,for a homogeneous ellipsoid with semiaxes $a , b$ and $c$ in the limit of small asymmetry, i.e. $a \simeq b$ ,eqs.(4.198)-(4.200) give

$$
\epsilon \simeq \frac { b - a } { a } + O ( \epsilon ^ { 2 } ) .
$$

We write the angular velocity of the source as $\omega _ { \mathrm { r o t } } ~ = ~ 2 \pi f _ { \mathrm { r o t } }$ and we introduce $f _ { \mathrm { g w } } ~ = ~ 2 f _ { \mathrm { r o t } } ,$ which is the frequency of the GW.In terms offgw and of $\epsilon$ ,the result for the GW amplitude found above can be rewritten as

$$
\begin{array} { l } { { \displaystyle h _ { + } = h _ { 0 } \frac { 1 + \cos ^ { 2 } \iota } { 2 } \cos ( 2 \pi f _ { \mathrm { g w } } t ) , } } \\ { { \displaystyle h _ { \times } = h _ { 0 } \cos \iota \sin ( 2 \pi f _ { \mathrm { g w } } t ) , } } \end{array}
$$

where

$$
h _ { 0 } = { \frac { 4 \pi ^ { 2 } G } { c ^ { 4 } } } { \frac { I _ { 3 } f _ { \mathrm { g w } } ^ { 2 } } { r } } \epsilon .
$$

Neutron stars typically have a mass $m \simeq 1 . 4 M _ { \odot }$ and a radius $a \simeq$ 10 km, which gives $I _ { 3 } \simeq ( 2 / 5 ) m a ^ { 2 } \simeq 1 \times 1 0 ^ { 3 8 } \mathrm { k g m ^ { 2 } }$ . The value of the ellipticity depends on the neutron star properties,and in particular on the maximum strain that can be supported by its crust.This is quite mcertain but，as we will discuss in Vol.2,plausible values are in the range e≤10-6,although values as large as ∈ \~10-5 can be considered. Inserting these numerical reference values,and taking a typical galactic distance $r = 1 0$ kpc,eq.(4.224) gives

$$
h _ { 0 } \simeq 1 . 0 6 \times 1 0 ^ { - 2 5 } \left( \frac { \epsilon } { 1 0 ^ { - 6 } } \right) \left( \frac { I _ { 3 } } { 1 0 ^ { 3 8 } \mathrm { k g } \mathrm { m } ^ { 2 } } \right) \left( \frac { \mathrm { 1 0 k p c } } { r } \right) \left( \frac { f _ { \mathrm { g w } } } { \mathrm { 1 k H z } } \right) _ { , \ast } ^ { 2 } .
$$

$h _ { 0 } \sim f _ { \mathrm { g w } } ^ { 2 }$

We next compute the power $P$ radiatedlin GWs, plugging eqs. (4.216)- 4218) into the quadrupole formula (376). Observing that $\ddot { M } _ { 1 1 } =$ $\ddot { 1 } \dot { 1 } _ { 2 2 }$ ,this gives

$$
\begin{array} { c } { { P = \displaystyle \frac { 2 G } { 5 c ^ { 5 } } \langle \dddot { M } _ { 1 1 } ^ { 2 } + \dddot { M } _ { 1 2 } ^ { 2 } \rangle } } \\ { { = \displaystyle \frac { 3 2 G } { 5 c ^ { 5 } } \epsilon ^ { 2 } I _ { 3 } ^ { 2 } \omega _ { \mathrm { r o t } } ^ { 6 } , } } \end{array}
$$

md therefore the rotational energy of the star decreases,because of GW ission.as

$$
\frac { d E _ { \mathrm { r o t } } } { d t } = - \frac { 3 2 G } { 5 c ^ { 5 } } \epsilon ^ { 2 } I _ { 3 } ^ { 2 } \omega _ { \mathrm { r o t } } ^ { 6 } .
$$

Since the rotational energy of & star rotating around its principal axisn is $E _ { \mathrm { r o t } } = ( 1 / 2 ) I _ { 3 } \omega _ { \mathrm { r o t } } ^ { 2 }$ (see eq. (4.206)),ifGW emission were the dominam mechanism for the loss of rotational energy,the rotational frequency a neutron star should decrease as

$$
\dot { \omega } _ { \mathrm { r o t } } = - \frac { 3 2 G } { 5 c ^ { 5 } } \epsilon ^ { 2 } I _ { 3 } \omega _ { \mathrm { r o t } } ^ { 5 } .
$$

Experimentally, from the electromagnetic signal emitted by neutro stars observed as pulsars (see Chapter 6),one rather finds $\dot { \omega } _ { \mathrm { r o t } } \sim - \omega _ { \mathrm { r } } ^ { \mathrm { n } }$ where $n$ ,called the braking index,depends on the specific pulsar typically ranges between 2 and 3,rather than $n = 5$ . This means tha GW emission is not the main energy loss mechanism for a rotating pu sar,and other mechanisms,of electromagnetic nature,dominate.

23In the literature,(α,β,)are usually denote by $( \theta , \phi , \psi )$ ,respectively. However,here we prefer to reserve the notation $( \theta , \phi )$ to denote the angles that describe the angular distribution of the gravitational radiation.

![](images/fb045aef397f8cf12c840e70adae6225d91e32ca13e5e3322296f760bdd68afd.jpg)  
Fig. 4.15 The definition of the Euler angles $( \alpha , \beta , \gamma )$

# 4.2.2GWs from freely precessing rigid bodies

In general,in astronomical objects the rotation axis does not coincid with a principal axis and,as a consequence,the motion of the rigid body is a combination of rotation around a principal axis and precession.A we will see in this section,the precession motion introduces qualitativel new features in the GWs radiated.

To compute the GW production we proceed as in eqs. (4.207)-(4.209) We first introduce a fixed reference frame,with axes $\left( { { x } _ { 1 } } , { { x } _ { 2 } } , { { x } _ { 3 } } \right)$ In this inertial frame the angular moinentum J of the rigid body is conserved and we choose the $x _ { 3 }$ axis in the direction of J. Next we introduce th body frame,i.e.a reference frame attached to the rotating body, wil coordinates $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ ，whose axes coincide with the principal axes o the body. The relation between the two frames is given by the Eule angles $( \alpha , \beta , \gamma )$ defined in Fig.4.15.23

To pass from the fixed frame to the body frame we first perform a counterclockwise rotation by an angle $\beta$ around the $x _ { 3 }$ axis.This brings the $x _ { 1 }$ axis onto an axis which is called the line of nodes (which i the intersection of the $( x _ { 1 } , x _ { 2 } )$ plane with the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } )$ plane). Next we perform a counterclockwise rotation by an angle $\alpha$ around the line nodes.This brings the $x _ { 3 }$ axis onto the $x _ { 3 } ^ { \prime }$ axis.Finally,we perform a counterclockwise rotation by an angle $\gamma$ around the $x _ { 3 } ^ { \prime }$ axis,which brings the line of nodes onto the $x _ { 1 } ^ { \prime }$ axis. Therefore we have $\boldsymbol { x } _ { i } ^ { \prime } = \mathcal { R } _ { i j } \boldsymbol { x } _ { j }$ asi eq.(4.207),but now the rotation matrix is more complicated,

$$
\begin{array} { r } { \mathcal { R } = \left( \begin{array} { c c c } { \cos \gamma } & { \sin \gamma } & { 0 } \\ { - \sin \gamma } & { \cos \gamma } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) \left( \begin{array} { c c c } { \mathbb { I } } & { 0 } & { 0 } \\ { \mathbb { Q } } & { \cos \alpha } & { \sin \alpha } \\ { \mathbb { Q } } & { - \sin \alpha } & { \cos \alpha } \end{array} \right) \left( \begin{array} { c c c } { \cos \beta } & { \sin \beta } & { 0 } \\ { - \sin \beta } & { \cos \beta } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right) , } \end{array}
$$

The motion of the rigid body is specified once we know how $\alpha , \beta$ and1 evolve with time.Let us recall, from elementary mechanics (see again Landau and Lifshitz,Vol.I 1976),how this can be obtained．In the $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ frame,the angular momentum J is conserved (this, of course is not the case in the body frame,which is non-inertial, since it is rotating),and we oriented the $x _ { 3 }$ axis so that ${ \bf { J } } = ( 0 , 0 , J )$ . In the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , x _ { 3 } ^ { \prime } )$ frame,instead,we denote the components of the angular momentum by $( J _ { 1 } ^ { \prime } , J _ { 2 } ^ { \prime } , J _ { 3 } ^ { \prime } )$ .From Fig.4.15 we see that

$$
\begin{array} { r l } & { J _ { 1 } ^ { \prime } = J \sin \alpha \sin \gamma , } \\ & { J _ { 2 } ^ { \prime } = J \sin \alpha \cos \gamma , } \\ & { J _ { 3 } ^ { \prime } = J \cos \alpha . } \end{array}
$$

On the other hand, we can write $\left( J _ { 1 } ^ { \prime } , J _ { 2 } ^ { \prime } , \bar { J } _ { 3 } ^ { \prime } \right)$ in terms of ${ \dot { \alpha } } , { \dot { \beta } }$ and $\dot { \gamma }$ using again Fig.4.15 and observing that，as $\operatorname { a }$ vector,the angular velocity $d \alpha / d t$ is directed along the line of nodes,so its components in the body frame are

$$
\frac { d \alpha } { d t } = \left( \dot { \alpha } \cos \gamma , - \dot { \alpha } \sin \gamma , 0 \right) .
$$

Similarly, $d \beta / d t$ is directed along the $x _ { 3 }$ axis,so its components in the body frame are

$$
\frac { d \beta } { d t } = ( \dot { \beta } \sin \alpha \sin \gamma , \dot { \beta } \sin \alpha \cos \gamma , \dot { \beta } \cos \alpha ) ,
$$

while $d \gamma / d t$ is along the $x _ { 3 } ^ { \prime }$ axis,so in the body frame $d \pmb { \gamma } / d t = ( 0 , 0 , \dot { \gamma } )$ The total angular velocity $\omega$ is the vector $\$ 10$ of these angular velocities, $\omega = d \alpha / d t + d \beta / d t + d \gamma / d t$ ,so its compohents $\omega _ { i } ^ { \prime }$ in the body frame are

$$
\begin{array} { r l } & { \omega _ { 1 } ^ { \prime } = \dot { \alpha } \cos \gamma + \dot { \beta } \sin \alpha \sin \gamma , } \\ & { \omega _ { 2 } ^ { \prime } = - \dot { \alpha } \sin \gamma + \dot { \beta } \sin \alpha \cos \gamma , } \\ & { \omega _ { 3 } ^ { \prime } = \dot { \gamma } + \dot { \beta } \cos \alpha . } \end{array}
$$

In the body frame the inertia tensor is diagonal,with eigenvalues $I _ { 1 } , I _ { 2 }$ and ${ { I } _ { 3 } }$ so ${ { J } _ { 1 } ^ { \prime } } = { { I } _ { 1 } } \omega _ { 1 } ^ { \prime }$ ， ${ { J } _ { 2 } ^ { \prime } } = { { I } _ { 2 } } \omega _ { 2 } ^ { \prime }$ and ${ { J } _ { 3 } ^ { \prime } } = { { I } _ { 3 } } { { \omega } _ { 3 } ^ { \prime } }$ .Comparing eqs. (4.230) and (4.233) we therefore get

$$
\begin{array} { r l } & { \quad I _ { 1 } { \left( \dot { \alpha } \cos \gamma + \dot { \beta } \sin \alpha \sin \gamma \right) } = J \sin \alpha \sin \gamma , } \\ & { \quad I _ { 2 } { \left( - \dot { \alpha } \sin \gamma + \dot { \beta } \sin \alpha \cos \gamma \right) } = J \sin \alpha \cos \gamma , } \\ & { \quad \quad I _ { 3 } { \left( \dot { \gamma } + \dot { \beta } \cos \alpha \right) } = J \cos \alpha . } \end{array}
$$

These are first order equations in the variables $( \alpha , \beta , \gamma )$ ，and are the first integral of the equations of motion provided by the conservation of angular momentum.24 One can now integrate these equations and obtain $\alpha ( t ) , \beta ( t )$ and $\gamma ( t )$ .In the most general case,the result can be written in terms of elliptic functions,and we will get back to it later in this section.However,we first limit ourselves to the simpler case of an nxisymmetric body with $I _ { 1 } = I _ { 2 }$

# Wobble” radiation from an axisymmetric rigid body

We consider an axisymmetric body, whose longitudinal axis $x _ { 3 } ^ { \prime }$ makes all angle $\alpha$ with the angular momentum axis $x _ { 3 }$ .The angle $\alpha$ is often

24They are in fact thefirst integral of the Euler equations for rigid bodies in the absence of external torques,

$$
\begin{array} { r } { I _ { 1 } \dot { \omega } _ { 1 } ^ { \prime } = \omega _ { 2 } ^ { \prime } \omega _ { 3 } ^ { \prime } ( I _ { 2 } - I _ { 3 } ) } \\ { I _ { 2 } \dot { \omega } _ { 2 } ^ { \prime } = \omega _ { 1 } ^ { \prime } \omega _ { 3 } ^ { \prime } ( I _ { 3 } - I _ { 1 } ) } \\ { I _ { 3 } \dot { \omega } _ { 3 } ^ { \prime } = \omega _ { 1 } ^ { \prime } \omega _ { 2 } ^ { \prime } ( I _ { 1 } - I _ { 2 } ) } \end{array}
$$

as we easily verify taking the first derivative of eqs.(4.234)-(4.236)and using eq. (4.233).

called the “wobble” angle,andlthe corresponding GW emission is calle “wobble radiation”.

When $I _ { 1 } \ = \ I _ { 2 }$ ，the analytic solution of eqs. (4.234)-(4.236) is very simple.Multiplying the first equation by $\mathrm { c o s } \gamma$ and the second by sin and subtracting them,we get

$$
{ \dot { \alpha } } = 0 .
$$

This shows that the inclinationlof the $x _ { 3 } ^ { \prime }$ axis with respect to the angular momentum $\mathbf { J }$ is constant．Multiplying the first equation by $\sin \gamma$ and the second by $\cos \gamma$ and summing them,we get

$$
I _ { 1 } \dot { \beta } \sin \alpha = J \sin \alpha .
$$

This shows that, if $\alpha \neq 0$ ，the $x _ { 3 } ^ { \prime }$ axis rotates with a constant angular velocity $\dot { \boldsymbol { \beta } } = \boldsymbol { J } / I _ { 1 }$ about the direction of ${ \bf J }$ .We define

$$
\Omega \equiv \dot { \beta } = \frac { J } { I _ { 1 } } .
$$

Finally,having found that both $\cos \alpha$ and $\dot { \boldsymbol { \beta } }$ are constants,eq. (4.236 shows that even $\dot { \gamma }$ is constant.Equation (4.236),together with $J = I _ { 1 } { \boldsymbol { \beta } } _ { }$ gives

$$
\omega _ { \mathrm { p } } \equiv - \dot { \gamma } = \frac { I _ { 3 } - I _ { 1 } } { I _ { 3 } } \Omega \cos \alpha .
$$

25Using the expression for $\dot { \gamma }$ given in eq. (4.240),we have

$$
\begin{array} { l } { \omega _ { 3 } ^ { \prime } = \dot { \gamma } + \dot { \beta } \cos \alpha } \\ { = ( I _ { 1 } / I _ { 3 } ) \Omega \cos \alpha , } \end{array}
$$

and therefore we can also write

$$
\omega _ { \mathsf { p } } = \frac { I _ { 3 } - I _ { 1 } } { I _ { 1 } } \omega _ { 3 } ^ { \prime } .
$$

The minus sign in the definition $\omega _ { \mathrm { p } } = - \dot { \gamma }$ is chosen so that,for an oblate body $\left( I _ { 3 } \ > \ I _ { 1 , } \right)$ ，which is the normal shape of astrophysical objects. $\omega _ { \mathrm { p } } > 0$ .25 Using eq. (4.233) we see that the components of the angular velocity in the body frame evolve $\mathsf { a s } ^ { 2 6 }$

$$
\begin{array} { r l } & { \omega _ { 1 } ^ { \prime } = a \cos ( \omega _ { \mathrm { p } } t ) , } \\ & { \omega _ { 2 } ^ { \prime } = a \sin ( \omega _ { \mathrm { p } } t ) , } \\ & { \omega _ { 3 } ^ { \prime } = b , } \end{array}
$$

26Observe that，for an axisymmetric body,the orientation of the principal axes in the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } )$ plane is arbitrary. We choose the origin of time so that $\beta ( t ~ = ~ 0 ) ~ = ~ 0$ ，and then we choose the orientation of the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } )$ axes so that,at $t = 0$ ， $\gamma ( 0 ) = \pi { \bar { / 2 } }$ Therefore eq. (4.240） gives $\gamma ( t ) = ( \pi / 2 ) - \omega _ { \mathrm { p } } t$

where $a = \Omega \sin \alpha$ and $b = - \omega _ { \mathrm { p } } + \Omega \cos \alpha$ are constants. This shows that,in the body frame,the angular velocity rotates in the $( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } )$ plane,i.e. precesses around the $x _ { 3 } ^ { \prime }$ axis,with angular velocity $\omega _ { \mathsf { p } }$ This precession is counterclockwise if $\omega _ { \mathsf { p } } > 0$ (which justifies the notation $\boldsymbol { \omega } _ { \flat }$ for $- \dot { \gamma }$ ).Observe that $| I _ { 3 } - I _ { \updownarrow } | \ll I _ { 3 }$ (in a NS,a possible value could be $| I _ { 3 } - I _ { 1 } | / I _ { 3 } \sim 1 0 ^ { - 7 } )$ ,and therefore $| \omega _ { \mathsf { p } } | \ll \Omega$ ．This motion is called free precesson,since it takes place in the absence of external torques just as a consequence of the deviation of the rigid body from spherical symmetry.

We can now compute how the inertia tensor of the rigid body evolves with time,in the fixed frame with coordinates $( x _ { 1 } , x _ { 2 } , x _ { 3 } )$ . As before we denote by $I ^ { \prime }$ the inertia tensor in the body frame,so ${ \boldsymbol { I } } ^ { \prime } = \mathrm { d i a g } \left( I _ { 1 } , I _ { 1 } , I _ { 3 } \right)$ is a constant matrix,while we denote by $I _ { i j }$ the inertia tensor in the fixed frame.Then,as in eq. (4.210), $I _ { i j } = ( \mathcal { R } ^ { T } I ^ { \prime } \mathcal { R } ) _ { i j }$ ，but now $\mathcal { R }$ is given by eq. (4.229).

The explicit computation is simplified observing that,if we write the rotation matrix (4.229) as $\mathcal { R } = A ( \gamma ) B ( \alpha ) C ( \beta )$ ，we see that

$$
\begin{array} { r l } { \mathcal { R } ^ { T } I ^ { \prime } \mathcal { R } = ( C ^ { T } B ^ { T } A ^ { T } ) I ^ { \prime } ( A B C ) } & { { } } \\ { = ( C ^ { T } B ^ { T } ) I ^ { \prime } ( B C ) } \end{array}
$$

because,when $I _ { 1 } = I _ { 2 }$ ,the matrix $A$ commutes with the matrix $I ^ { \prime }$ ,and $A ^ { T } A = 1$ because it is an orthogonal matrix. Therefore,the angle $\gamma$ drops out from $I _ { i j }$ ,and the remaining matrix multiplication gives

$$
\begin{array} { r l } & { I _ { 1 1 } = I _ { 1 } ( \cos ^ { 2 } \beta + \cos ^ { 2 } \alpha \sin ^ { 2 } \beta ) + I _ { 3 } \sin ^ { 2 } \alpha \sin ^ { 2 } \beta } \\ & { \quad = \frac { 1 } { 2 } ( I _ { 1 } - I _ { 3 } ) \sin ^ { 2 } \alpha \cos 2 \beta + \mathrm { c o n s t a n t } , } \\ & { I _ { 1 2 } = \frac { 1 } { 2 } ( I _ { 1 } - I _ { 3 } ) \sin ^ { 2 } \alpha \sin 2 \beta , } \\ & { I _ { 2 2 } = I _ { 1 } ( \sin ^ { 2 } \beta + \cos ^ { 2 } \alpha \cos ^ { 2 } \beta ) + I _ { 3 } \sin ^ { 2 } \alpha \cos ^ { 2 } \beta } \\ & { \quad = - \frac { 1 } { 2 } ( I _ { 1 } - I _ { 3 } ) \sin ^ { 2 } \alpha \cos 2 \beta + \mathrm { c o n s t a n t } , } \\ & { I _ { 1 3 } = - ( I _ { 1 } - I _ { 3 } ) \sin \alpha \cos \alpha \sin \beta , } \\ & { I _ { 2 3 } = ( I _ { 1 } - I _ { 3 } ) \sin \alpha \cos \alpha \cos \beta , } \\ & { I _ { 3 3 } = I _ { 1 } \sin ^ { 2 } \alpha + I _ { 3 } \cos ^ { 2 } \alpha - \cos \alpha \sin \mathrm { t a n t } . } \end{array}
$$

Observe that,since $\gamma$ dropped out and $\alpha$ is constant,the time dependence of these expressions comes uniquely from $\beta$ which,from eq. (4.239), $i s \beta ( t ) = \Omega t$ (recall that we have chosen the origin of time so that $\beta = 0$ $\mathfrak { s t } : = 0$ ,see Note 26).As in eq. (4.215), $M _ { i j } = - I _ { i j }$ ，plus constant terms that give zero upon derivation. Therefore,we get

$$
\begin{array} { r l } & { \ddot { M } _ { 1 1 } = 2 { { \left( { I _ { 1 } } - { I _ { 3 } } \right) } } \Omega ^ { 2 } \sin ^ { 2 } \alpha { \left| { \cos ( 2 \Omega t ) } \right. } , } \\ & { \ddot { M } _ { 1 2 } = 2 { { \left( { I _ { 1 } } - { I _ { 3 } } \right) } } \Omega ^ { 2 } \sin ^ { 2 } \alpha | \sin ( 2 \Omega t ) , } \\ & { \ddot { M } _ { 2 2 } = - 2 { { \left( { I _ { 1 } } - { I _ { 3 } } \right) } } \Omega ^ { 2 } \sin ^ { 2 } \alpha \cos ( 2 \Omega t ) , } \\ & { \ddot { M } _ { 1 3 } = - { { \left( { I _ { 1 } } - { I _ { 3 } } \right) } } \Omega ^ { 2 } \sin \alpha \cos \alpha \sin ( \Omega t ) , } \\ & { \ddot { M } _ { 2 3 } = { { \left( { I _ { 1 } } - { I _ { 3 } } \right) } } \Omega ^ { 2 } \sin \alpha \cos \alpha \cos ( \Omega t ) , } \\ & { \ddot { M } _ { 3 3 } = 0 . } \end{array}
$$

We see that some matrix elements of $\ddot { M } _ { i j }$ Oscillate as $\sin ( 2 \Omega t )$ or $\cos ( 2 \Omega t )$ ， hile others as $\sin ( \Omega t )$ or $\cos ( \Omega t )$ .From this,we already understand lat we will have GW emission at twolfrequencies, $\omega _ { \mathrm { g w } } ~ = ~ 2 \Omega$ and $\ j _ { \mathrm { { w } } } = \Omega$ ．The origin of these factors is easily traced back: since the mly time dependence comes from $\beta ( t )$ ，and $\beta$ describes a rotation in e $\left( { { x } _ { 1 } } , { { x } _ { 2 } } \right)$ plane,the time-dependent part of $I _ { i j }$ has a factor $\sin ( \Omega t )$ $\cos ( \Omega t )$ for each index $i$ or $j$ that take the value 1 or 2,while the lex 3 produces no further time dependence. Then，as far as the me-dependent part is concerned， we have $I _ { 1 1 } \sim \sin ^ { 2 } \Omega t \sim \cos ( 2 \Omega t )$ $\mathrm { ~ : ~ } \sim \cos ^ { 2 } \Omega t \mathrm { ~ \sim ~ } \cos ( 2 \Omega t )$ ， $I _ { 1 2 } \sim \sin ( \Omega t ) \cos ( \Omega t ) \sim \sin ( 2 \Omega t )$ ，while ${ \bf \tau } _ { | 3 } \sim \sin ( \Omega t )$ and $I _ { 2 3 } \sim \cos ( \Omega t )$ .Thus,the fact that,beside the exected radiation at $\omega _ { \mathrm { g w } } = 2 \Omega$ ，we also have radiation at $\omega _ { \mathrm { g w } } = \Omega$ ,isa onsequence of the fact that the motion of precession produces,together with a time-varying value of ${ \bar { J } } _ { i j }$ with $i , j = 1 , 2$ , also a variation in I and $I _ { 1 3 }$

The computation of the GW amplitude radiated in a direction corr sponding to polar angles ( $\displaystyle \boldsymbol { \theta } = \boldsymbol { \downarrow } , \boldsymbol { \phi } = \boldsymbol { 0 } _ { . }$ is now performed using eq. (3.72 We get

$$
\begin{array} { l } { { \displaystyle h _ { + } = \frac { 1 } { r } \frac { G } { c ^ { 4 } } \left[ \ddot { M } _ { 1 1 } - \ddot { M } _ { 2 2 } \cos ^ { 2 } \iota + \ddot { M } _ { 2 3 } \sin 2 \iota - \ddot { M } _ { 3 3 } \sin ^ { 2 } \iota \right] } } \\ { { \displaystyle ~ = A _ { + , 1 } \cos ( \Omega t ) + \left( A _ { + , 2 } \cos ( 2 \Omega t ) \right. } } \\ { { \displaystyle h _ { \times } = \frac { 2 } { r } \frac { G } { c ^ { 4 } } \left[ \ddot { M } _ { 1 2 } \cos \iota - \ddot { M } _ { 1 3 } \sin \iota \right] } } \\ { { \displaystyle ~ = A _ { \times , 1 } \sin ( \Omega t ) + \left. A _ { \times , 2 } \sin ( 2 \Omega t ) \right. , } } \end{array}
$$

where

$$
\begin{array} { r l } & { A _ { + , 1 } = h _ { 0 } ^ { \prime } \sin 2 \alpha \sin \iota \cos \iota , } \\ & { A _ { + , 2 } = 2 h _ { 0 } ^ { \prime } \sin ^ { 2 } \alpha \left( 1 + \cos ^ { 2 } \iota \right) , } \\ & { A _ { \times , 1 } = h _ { 0 } ^ { \prime } \sin 2 \alpha \sin \iota , } \\ & { A _ { \times , 2 } = 4 h _ { 0 } ^ { \prime } \sin ^ { 2 } \alpha \cos \iota . } \end{array}
$$

27Observe that the overall sign of the amplitude depends on the choice of the origin of time,and on the definition of the axes $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ in the plane transverse to the propagation direction,with respect to which the polarizations are defined．With our definition,when $\iota = 0$ these axes are $\hat { \textbf { u } } = \hat { \textbf { x } }$ and ${ \hat { \mathbf { v } } } = { \hat { \mathbf { y } } }$ see page 1l1 and Fig.3.2.In the literature, this computation has been performed choosing $\hat { \bf { u } }$ and $\hat { \mathbf { v } }$ so that,when $\iota = 0$ ， $\hat { \mathbf { u } } = \hat { \mathbf { y } }$ and $\hat { \textbf { v } } = - \hat { \mathbf { x } }$ This is related to our convention by a rotation of the $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ axes in the transverse plane,by an angle $\psi = \pi / 2$ .Under this rotation $h _ { + } \to - h _ { + }$ and $h _ { \times } ~ \to ~ - h _ { \times }$ ，see eq. (2.194),s0 $h _ { 0 } ^ { \prime } \to - h _ { 0 } ^ { \prime }$

and27

$$
h _ { 0 } ^ { \prime } = - { \frac { G } { c ^ { 4 } } } { \frac { ( I _ { 3 } - I _ { 1 } ) \Omega ^ { 2 } } { r } } .
$$

Of course it is understood that,on the right-hand side of eqs. (4.246 and (4.247), $t$ is actually the retarded time.As we already anticipated we have radiation at both $\omega _ { \tt g w } = \Omega$ and at $\omega _ { \mathrm { g w } } = 2 \Omega$

Observe that $A _ { + , 1 } / A _ { \times , 1 } = \cos \iota$ . Therefore from this ratio (or,equiv alently, from $A _ { + , 2 } / A _ { \times , 2 } )$ we get the inclination angle $\iota$ (which,by defini tion, is in the range $0 \leqslant i \leqslant \pi$ Given $\iota$ ,theratio $A _ { + , 1 } / A _ { + , 2 }$ determines theangle $\alpha$ . The overall valuelof the amplitude then fixes $| h _ { 0 } ^ { \prime } |$ If the dis tance to the source is known by other means,we therefore get a measum of $\left| I _ { 1 } - I _ { 3 } \right|$

It is now straightforward td compute the total power radiated.Using eq.(3.76)and observing,from eq.(4.245),that $\ddot { M } _ { 3 3 } = 0$ and $\sum \ddot { M } _ { k k } =$ 0,we get

$$
\begin{array} { r } { P _ { \mathrm { q u a d } } = \cfrac { G } { 5 c ^ { 5 } } \langle \dddot { M } _ { 1 1 } ^ { 2 } + \dddot { M } _ { 2 2 } ^ { 2 } + 2 \dddot { M } _ { 1 2 } ^ { 2 } + 2 \dddot { M } _ { 1 3 } ^ { 2 } + 2 \dddot { M } _ { 2 3 } ^ { 2 } \rangle } \\ { = \cfrac { 2 G } { 5 c ^ { 5 } } ( I _ { 1 } - I _ { 3 } ) ^ { 2 } \Omega ^ { 6 } \sin ^ { 2 } \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) , } \end{array}
$$

where the term $\sin ^ { 2 } \alpha \cos ^ { 2 } \alpha$ is from the radiation at $\omega _ { \mathrm { g w } } = \Omega$ and the term $1 6 \sin ^ { 4 } \alpha$ is from the radiation at $\omega _ { \mathrm { g w } } = 2 \Omega$ .Observe that,in the limit of small $\alpha$ ,the power radiated at $\omega _ { \mathrm { g w } } = \Omega$ is $O ( \alpha ^ { 2 } )$ while the powel radiated at $\omega _ { \mathrm { g w } } = 2 \Omega$ is $O ( \alpha ^ { 4 } )$ ,so for sufficiently small $\alpha$ theradiation at $\omega _ { \mathrm { g w } } = \Omega$ is dominant. The two contributions become equal when $\cos ^ { 2 } \alpha = 1 6 \sin ^ { 2 } \alpha$ i.e.for $\alpha \simeq 0 . 2 4 5 \mathrm { r a d } \simeq 1 4 ^ { \circ }$

# The back-reaction of GWs

We can now compute how the emission of GWs back-reacts on the motion of therigid body.The energy radiated in GWs is supplied by the rotational energy $E _ { \mathrm { r o t } }$ of the rigid body, so

$$
\frac { d E _ { \mathrm { r o t } } } { d t } = - \frac { 2 G } { 5 c ^ { 5 } } ( I _ { 1 } - I _ { 3 } ) ^ { 2 } \Omega ^ { 6 } \sin ^ { 2 } \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) .
$$

The angular momentum radiated (in the quadrupole approximation that we are using) is computed from eq.(3.97),and is supplied by the angular momentum J= (0,0,J) of the rigid body.Setting i= 3 into eq. (3.97), we have

$$
\begin{array} { c } { { \displaystyle \frac { d J } { d t } = - \frac { 2 G } { 5 c ^ { 5 } } \langle \ddot { M } _ { 1 a } \ddot { M } _ { 2 a } - \ddot { M } _ { 2 a } \ddot { M } _ { 1 a } \rangle } } \\ { { = - \displaystyle \frac { 4 G } { 5 c ^ { 5 } } \langle \ddot { M } _ { 1 a } \ddot { M } _ { 2 a } \rangle , } } \end{array}
$$

where we observed that we can replace Qka by Mka Since e3klSkaQla = Ql =O,andsimilarly Qia→Ma,andinthelast line we integrated by part a time derivative, inside the temporal average. Inserting the explicit expressions (4.245)， we get

$$
{ \frac { d J } { d t } } = - { \frac { 2 G } { 5 c ^ { 5 } } } ( I _ { 1 } - I _ { 3 } ) ^ { 2 } \Omega ^ { 5 } \sin ^ { 2 } \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) .
$$

Comparing this result with eq.(4.254),wesee that $d { \cal E } _ { \mathrm { r o t } } / d t = \Omega d J / d t$ SinceΩ= β and J= Iβ (see eq. (4.239)), the above equation gives

$$
\ddot { \beta } = - \frac { 2 G } { 5 c ^ { 5 } } \frac { ( I _ { 1 } - I _ { 3 } ) ^ { 2 } } { I _ { 1 } } \dot { \beta } ^ { 5 } \sin ^ { 2 } \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) .
$$

The equation governing the evolution of $\alpha$ can instead be obtained writing the rotational kinetic energy as in eq. (4.206)，and using ωi = J/I= (J/I)sinαsinγ,w= J/I1 =(J/)sinacosγ,and w = $J _ { 3 } ^ { \prime } / I _ { 3 } = ( J / I _ { 3 } ) \cos \alpha$ ,see eq. (4.230).This gives

$$
E _ { \mathrm { r o t } } = \frac { J ^ { 2 } } { 2 } \left( \frac { \sin ^ { 2 } \alpha } { I _ { 1 } } + \frac { \cos ^ { 2 } \alpha } { I _ { 3 } } \right) .
$$

Taking the time derivative and making use of eq. (4.256) and of $J = I _ { 1 } { \dot { \boldsymbol { \beta } } }$ on the right-hand side,and of eq. (4.254) on the left-hand side,we get

$$
\dot { \alpha } = - \frac { 2 G } { 5 c ^ { 5 } } \frac { ( I _ { 1 } - I _ { 3 } ) ^ { 2 } } { I _ { 1 } } \dot { \beta } ^ { 4 } \sin \alpha \cos \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) .
$$

Equations (4.257) and (4.259) determine the evolution of the angles α Ind β.We see that，because of the back-reaction of GWs,both the Iclination angle α,and the angular velocity β decrease. However,using pqs. (4.256) and (4.259), we see that

$$
\frac { d } { d t } ( J \cos { \alpha } ) = 0 ,
$$

Therefore $J$ decreases and $\alpha$ decreases (i.e. $\cos \alpha$ increases） in such & way that $J \cos \alpha$ stays constant.Since $J \cos \alpha$ is the projection of the angular momentum over the $x _ { 3 } ^ { \prime }$ axis of the body (see eq.(4.230)),we find that the rigid body rotates around its longitudinal axis with a constant angular velocity $\dot { \omega _ { 3 } ^ { \prime } } = \left( J / I _ { 3 } \right) \cos { \alpha }$ ，The rotation of the body around its longitudinal axis is not affected by the GW back-reaction.

To study in more detail the coupled system of equations (4.257) and (4.259),we introduce the dimensionless function

$$
u ( t ) = \dot { \beta } ( t ) / \dot { \beta } _ { 0 } ,
$$

where $\dot { \beta } _ { 0 }$ is the value of ${ \dot { \beta } } ( t )$ at some initial value $t = 0$ ，and we alse introduce the time-scale

$$
\begin{array} { r l r } { \displaystyle \tau _ { 0 } \equiv \left[ \frac { 2 G } { 5 c ^ { 5 } } \frac { ( I _ { 1 } - I _ { 3 } ) ^ { 2 } } { I _ { 1 } } \dot { \beta } _ { 0 } ^ { 4 } \right] ^ { - 1 } } & { } & { ( 4 . 2 ) } \\ & { } & { \displaystyle \simeq 1 . 8 \times 1 0 ^ { 6 } \mathrm { y r } \left( \frac { 1 0 ^ { - 7 } } { ( I _ { 1 } - I _ { 3 } ) / I _ { 3 } } \right) ^ { 2 } \left( \frac { 1 \mathrm { k H z } } { f _ { 0 } } \right) ^ { 4 } \left( \frac { 1 0 ^ { 3 8 } \mathrm { k g } \mathrm { m } ^ { 2 } } { I _ { 1 } } \right) , } \end{array}
$$

![](images/cbc238a9a121c4dd4a01fbda2af29c789719ddd25d506d9335a4045b36eea007.jpg)  
Fig： 4.16 The inclination angle$\alpha ( t )$ ，plotted asa function of$t / \tau _ { 0 }$ ，with initial conditions $\alpha ( 0 ) =$ $0 . 5 , u ( 0 ) = 1$

![](images/d945d7167e5c05189d58c0370099144763d03eb1e823061fcdb707dce7a7d16f.jpg)  
Fig.4.17 The function $u ( t ) = \dot { \beta } / \dot { \beta } _ { 0 }$ , plotted against $t / \tau _ { 0 }$ ，with initial conditions $\alpha ( 0 ) = 0 . 5 , u ( 0 ) = 1$

where $f _ { 0 } = \dot { \beta } _ { 0 } / ( 2 \pi )$ ,and we used as reference for $( I _ { 1 } - I _ { 3 } ) / I _ { 3 }$ and for $I _ { 3 }$ ,values that can be typical for neutron stars. Then eqs. (4.257) and (4.259) become

$$
\begin{array} { r l r } & { \dot { u } = - \displaystyle \frac { 1 } { \tau _ { 0 } } u ^ { 5 } \sin ^ { 2 } \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) , } & \\ & { \dot { \alpha } = \displaystyle - \frac { 1 } { \tau _ { 0 } } u ^ { 4 } \sin \alpha \cos \alpha ( \cos ^ { 2 } \alpha + 1 6 \sin ^ { 2 } \alpha ) , } & \end{array}
$$

with initial conditions $u ( 0 ) \ne 1$ and $\alpha ( 0 ) = \alpha _ { 0 }$ .In this form, it is clear that $\tau _ { 0 }$ is the characteristic time-scale of the problem，and the equations could be recast in a completely dimensionless form introducing a dimensionless variable $x = { t } / { \tau _ { 0 } }$ ，so that $\tau _ { 0 } \dot { u } = \ d u / d x$ and $\tau _ { 0 } \dot { \alpha } =$ $d \alpha / d x$

The asymptotic behavior of the solution can be easily read from eqs. (4.263) and (4.264),making use also of the fact that,as we shown above, $J \cos \alpha$ is a constant of motion.Since $J = I _ { 1 } { \dot { \boldsymbol { \beta } } }$ ，this means that $\dot { \beta } _ { \infty } \cos \alpha _ { \infty } = \dot { \beta } _ { 0 } \cos \alpha _ { 0 }$ ，where the subscripts $\infty$ denotes the value at $t = \infty$ .In terms of $u$ ,this means

$$
u _ { \infty } \cos \alpha _ { \infty } = \cos \alpha _ { 0 } .
$$

Equating to zero the right-hand sides of eqs. (4.263) and (4.264),we see that the possible fixed points of the evolution are either $u = 0$ or $\alpha = 0 , \pi$ .However, the value $\dot { u } _ { \infty } = 0$ is not consistent with eq. (4.265) (unless $\alpha _ { 0 } = \pi / 2$ ； clearly,this is an unstable fixed point, in which an infinitesimal perturbation drives the evolution either toward $\alpha = 0$ or $\alpha = \pi$ ).Therefore the only asymptotic solution,for $\alpha _ { 0 } < \pi / 2$ has $\alpha _ { \infty } = 0$ ：Then,eq.(4.265） shows that $u _ { \infty } = \cos \alpha _ { 0 }$ .Once we realize that $u$ approaches a finite constant $u _ { \infty }$ and that $\alpha \to 0$ ,from eq. (4.264) we see that at large times $\dot { \alpha } \simeq - \alpha / \tau _ { \infty } ,$ and therefore $\alpha ( t )$ approaches zero exponentially, with a time-scale $\tau _ { \infty } = \tau _ { 0 } / u _ { \infty } ^ { 4 }$ ， which is obtained simply replacing $\dot { \beta } _ { 0 }$ with $\dot { \beta } _ { \infty }$ in eq. (4.262).

The numerical integration of eqs. (4.263) and (4.264) is straightforward,and we show in Figs.4.16 and 4.17 the solution for the initial condition $\alpha _ { 0 } = 0 . 5$ ,which confirms the asymptotic behavior found analytically.

In conclusion,on a time-scale given by eq. (4.262)，the rigid body aligns its rotation axis with the direction of the angular momentum $( \alpha  0 )$ ，while the rotational angular velocity $\dot { \beta } = \mathsf { \bar { \Omega } }$ around the $x _ { 3 }$ axis decreases toward the constant value $\Omega _ { 0 } \cos \alpha _ { 0 }$ ，and the rotational velocity around its principal axis $\omega _ { 3 } ^ { \prime } = \Omega \geqslant \alpha$ stays constant.

Finally,it is interesting to compare the frequency $\omega _ { \mathrm { e m } }$ of the electromagnetic pulses of a pulsar,idealized as arotating rigid body,28 with the frequency of the GWs that it emits. If a pulsar rotates around its principal axis with frequency $\Omega$ ,and has $I _ { 1 } \neq I _ { 2 }$ ,which is the case discussed in Section 4.2.1, then $\omega _ { \mathrm { e m } } = \Omega$ , so we can determine $\Omega$ very precisely by electromagnetic observations,and GW emission is at $\omega _ { \mathrm { g w } } = 2 \Omega$ In this case,therefore, we have an accurate prediction of the frequency at which we expect GW emission.

Instead,in the case of “wobble”radiation discussed in this subsection, in the limit of small $\alpha$ ,the axes $x _ { 3 }$ and $x _ { 3 } ^ { \prime }$ almost coincide.If the source of the electromagnetic radiation is some“hot spot” fixed on the star surface then,for a far observer,the hot spot is basically rotating around the $x _ { 3 }$ axis with a total angular velocity $\omega _ { \mathrm { r o t } } = \dot { \beta } + \dot { \gamma } = \Omega - \omega _ { \mathrm { p } }$ see Fig. 4.15, so

$$
\Omega = \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } .
$$

The mean frequency $\omega _ { \mathrm { e m } }$ of repetition of the electromagnetic pulses will be equal to $\omega _ { \mathrm { r o t } }$ ,s0 $\omega _ { \mathrm { e m } } = \Omega - \omega _ { \mathrm { p } }$ . Instead, we saw that wobble gravitational radiation is emitted at $\dot { \omega } _ { \mathrm { g w } } = \Omega$ and at $\omega _ { \mathrm { g w } } = 2 \Omega$ so these two lines are shifted, with respect to $\omega _ { \mathrm { e m } }$ and to $2 \omega _ { \mathrm { e m } }$ ,by the unknown quantities $\omega _ { \mathrm { p } }$ and $2 \omega _ { \mathsf { p } }$ ,respectively. Using eq. (4.240),for the line at $\boldsymbol { \omega } _ { \mathrm { g w } } = \Omega$ ,we have

$$
\omega _ { \mathrm { g w } } \simeq \left( 1 + \frac { I _ { 3 } - I _ { 1 } } { I _ { 3 } } \cos \alpha \right) \omega _ { \mathrm { e m } } .
$$

Since $\left| { I _ { 1 } - I _ { 3 } } \right| / { I _ { 3 } }$ is in general very small,e.g.could be of order $1 0 ^ { - 7 }$ in a neutron star, the diference between the actual GW frequency and the value suggested by electromagnetic observation is small.An axisymmetric astrophysical object is normally expected to be oblate $\left( I _ { 3 } > I _ { 1 } \right)$ ， and in this case $\omega _ { \mathrm { g w } } > \omega _ { \mathrm { e m } }$ For a prolate body $\left( I _ { 3 } < I _ { 1 } \right)$ ,instead,we have $\omega _ { _ \mathrm { { s w } } } < \omega _ { \mathrm { { e m } } }$

# Rotating and precessing triaxial bodies

We now study the radiation emitted byla generic triaxial body. We hoose the axes of the body frame so that $I _ { 1 } < I _ { 2 } < I _ { 3 }$ The timelependent moment of inertia $I _ { i j }$ in the fixed frame is again computed

■

28The discussion below is really specific to our crude modelization of neutron stars as rigid bodies. Real neutron stars are rather mostly fluid in their interior. See the Further Reading section for the results with a more realistic modelization of neutron stars.

from $I _ { i j } = ( \mathcal { R } ^ { T } I ^ { \prime } \mathcal { R } ) _ { i j }$ ，with $\textstyle { \mathcal { R } }$ given by eq. (4.229)，but now the de pendence on $\gamma$ does not cancel,contrary to the case $I _ { 1 } = I _ { 2 }$ discussed above,compare with eq.(4.243).

Once expressed $I _ { i j }$ in terms of $\alpha , \beta , \gamma ,$ to compute the waveform w need the time-dependence of the Euler angles,which can be found for instance in Landau and Lifshitz,Vol.I (1976). The evolution of th components of the angular velocity in the body frame is29

29We assume for definiteness $J ^ { 2 } \ \mathrm { ~  ~ \ s ~ }$ $2 E I _ { 2 }$ ； in this case,in the body frame, the apparent precession of $\mathbf { J }$ is around the $x _ { 3 } ^ { \prime }$ axis;if instead $J ^ { 2 } < 2 E I _ { 2 }$ ,it is around the $x _ { 1 } ^ { \prime }$ axis.

$$
\begin{array} { r l } & { \omega _ { 1 } ^ { \prime } = a \mathrm { c n } ( \tau , m ) , } \\ & { \omega _ { 2 } ^ { \prime } = a \left[ \frac { I _ { 1 } \left( I _ { 3 } - I _ { 1 } \right) } { I _ { 2 } \left( I _ { 3 } - I _ { 2 } \right) } \right] ^ { 1 / 2 } \mathrm { s n } ( \tau , m ) , } \\ & { \omega _ { 3 } ^ { \prime } = b \mathrm { d n } ( \tau , m ) , } \end{array}
$$

$^ { 3 0 } \mathrm { F o r }$ the elliptic functions cn,sn and dn and for the Jacobi theta functions that will appear below,we follow the notation and conventions of Abramowitz and Stegun (1972).

where cn,sn and dn are elliptic functions,30 and $\tau$ is a rescaled tim variable,

$$
\tau = b t \left[ \frac { ( I _ { 3 } - I _ { 2 } ) ( I _ { 3 } - I _ { 1 } ) } { I _ { 1 } I _ { 2 } } \right] ^ { 1 / 2 } .
$$

The parameter $m$ of the elliptic functions is given by

$$
m = \frac { ( I _ { 2 } - I _ { 1 } ) I _ { 1 } a ^ { 2 } } { ( I _ { 3 } - I _ { 2 } ) I _ { 3 } b ^ { 2 } } ,
$$

and $a , b$ are the initial values of $\omega _ { 1 } ^ { \prime }$ and $\omega _ { 3 } ^ { \prime }$ ，

$$
a = \omega _ { 1 } ^ { \prime } ( 0 ) , \quad b = \omega _ { 3 } ^ { \prime } ( 0 ) .
$$

Observe that we have chosenlthe origin of time so that $\omega _ { 2 } ^ { \prime } ( 0 ) = 0$ In the limit $I _ { 1 } = I _ { 2 }$ we have $m \neq 0$ ；since $\mathrm { c n } ( \tau , 0 ) = \cos \tau$ ： $\mathrm { s n } ( \tau , 0 ) = \mathrm { s i n } \tau$ and $\mathrm { d n } ( \tau , 0 ) = 1$ ,inthis limit we recover the result (4.242).The elliptic functions are periodic functions of $\tau$ ，with periodicity $4 K ( m )$ ,where $K ( m )$ it the complete elliptic integral of the first kind.The components of the angular velocity in the body frame are therefore periodic int. with period

$$
T = \frac { 4 K ( m ) } { b } \biggl [ \frac { I _ { 1 } I _ { 2 } } { ( I _ { 3 } - I _ { 2 } ) ( I _ { 3 } - I _ { 1 } ) } \biggr ] ^ { 1 / 2 } .
$$

To compute $I _ { i j }$ ，we need explicitly the time-dependence of the Eulei angles.The solution for $\alpha$ and $\gamma$ is

$$
\begin{array} { l } { \displaystyle \cos \alpha ( t ) = \frac { I _ { 3 } | _ { b } } { J } \mathrm { d n } ( \tau , m ) \mathrm { , } } \\ { \displaystyle \tan \gamma ( t ) = \left[ \frac { I _ { 1 } ( I _ { 3 } - I _ { 2 } ) } { I _ { 2 } ( I _ { 3 } - I _ { 1 } ) } \right] ^ { 1 / 2 } \frac { \mathrm { c n } ( \tau , m ) } { \mathrm { s n } ( \tau , m ) } \mathrm { , } } \end{array}
$$

so they are both periodic with period $T$ . The solution for $\beta$ is instead

$$
\beta ( t ) = \frac { 2 \pi } { T ^ { \prime } } t + \beta _ { 1 } ( t ) ,
$$

where

$$
\begin{array} { l } { { \displaystyle { \frac { 2 \pi } { T ^ { \prime } } = \frac { J } { I _ { 1 } } - \frac { 2 i } { T } \frac { \vartheta _ { 4 } ^ { \prime } ( i \pi c _ { 1 } ) } { \vartheta _ { 4 } ( i \pi c _ { 1 } ) } } } } \\ { { \displaystyle { \quad = \frac { J } { I _ { 1 } } + \frac { 2 b } { K ( m ) } \left[ \frac { ( I _ { 3 } - I _ { 2 } ) ( I _ { 3 } - I _ { 1 } ) } { I _ { 1 } I _ { 2 } } \right] ^ { 1 / 2 } \sum _ { n = 1 } ^ { \infty } \frac { q ^ { n } } { 1 - q ^ { 2 n } } \sinh ( 2 \pi n c _ { 1 } ) . } } } \end{array}
$$

Here $\vartheta _ { 4 }$ is a Jacobi theta function, $c _ { 1 }$ is defined to be any31 solution of the equation ${ \mathrm { s n } } [ 2 i c _ { 1 } K ( m ) , m ] = i I _ { 3 } b / ( I _ { 1 } a )$ ,and

$$
q = \exp \{ - \pi K ( 1 - m ) / K ( m ) \} .
$$

The function $\beta _ { 1 } ( t )$ can be written as aratio of theta functions,

$$
\beta _ { 1 } ( t ) = \frac { \vartheta _ { 4 } \big ( \frac { 2 \pi t } { T } - i \pi c _ { 1 } \big ) } { \vartheta _ { 4 } \big ( \frac { 2 \pi t } { T } + i \pi c _ { 1 } \big ) } ,
$$

and admits the series expansion

$$
\beta _ { 1 } ( t ) = \sum _ { n = 1 } ^ { \infty } \left[ \frac { - 2 q ^ { n } } { n ( 1 - q ^ { 2 n } ) } \right] \left| \sin \left( \frac { 4 \pi n t } { T } \right) \right. .
$$

Observe that $\beta _ { 1 } ( t )$ is periodic with period $T / 2$ .In the problem there are therefore two distinct periodicities, $T$ and $T ^ { \prime }$ ,and we can expect that the frequency spectrum of the gravitational radiation will have two sets of lines.The fact that $\gamma$ is periodic with period $T$ identifies $2 \pi / T$ as the angular frequency associated to precession,so we define

$$
\begin{array} { l } { \displaystyle \omega _ { \mathsf { p } } = \frac { 2 \pi } { T } } \\ { \displaystyle \quad = \frac { \pi b } { 2 K ( m ) } \left[ \frac { ( I _ { 3 } - I _ { 2 } ) ( I _ { 3 } - I _ { 1 } ) } { I _ { 1 } I _ { 2 } } \right] ^ { 1 / 2 } . } \end{array}
$$

The angular frequency associated to rotation around the $x _ { 3 }$ axis is in-$\mathrm { \Delta \ a d ^ { 3 2 } }$

3lSince the eliptic functions and the theta functions have the same periodicity,all solutions for $c _ { 1 }$ are equivalent.

$$
\omega _ { \mathrm { r o t } } = \frac { 2 \pi } { T ^ { \prime } } - \frac { 2 \pi } { T | } .
$$

Given these complicated but explicit solutibns for $\alpha ( t ) , \beta ( t )$ and $\gamma ( t )$ ,one ould in principle plug them into the rotation matrix $\mathcal { R } _ { i j }$ and grind, to obtain the moment of inertia in the fixed frame,and hence the waveform. However,the discrete nature of the spectrum becomes more evident if, ather than working with the exact expressions，we perform a series xpansion for small wobble angle (which is equivalent to expanding in powers of $m$ )and small deviations from axisymmetry.33 The result,up t0 second order in $m$ ,is

$$
\begin{array} { r l } & { h _ { + } = A _ { + , 0 } \cos ( 2 \omega _ { \mathrm { r o t } } t ) } \\ & { \qquad + A _ { + , 1 } \cos [ ( \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } ) t ] + A _ { + , 2 } \cos [ 2 ( \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } ) t ] , } \\ & { h _ { \times } = A _ { \times , 0 } \sin ( 2 \omega _ { \mathrm { r o t } } t ) } \\ & { \qquad + A _ { \times , 1 } \sin [ ( \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } ) t ] + A _ { \times , 2 } \sin [ 2 ( \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } ) t ] , } \\ & { \qquad \quad } \end{array}
$$

32One can also check this result observing that,in the limit of small wobble angle,it gives $\omega _ { \mathrm { r o t } } ~ = ~ \dot { \beta } - \omega _ { \mathsf { p } }$ Since $\dot { \gamma } = - \omega _ { \mathsf { p } }$ ,seeeq. (4.240),we get $\omega _ { \mathrm { r o t } } =$ $\beta + \dot { \gamma } ,$ in agreement with the discussion above eq. (4.266).

33Thiscomputationisperformed inZimmermann (1980）and VanDenBroeck (2005)，see the Further Reading.

where

$$
\begin{array} { r l } & { A _ { + , 0 } = h _ { 0 } \left( 1 / 2 \right) \left( 1 + \cos ^ { 2 } \iota \right) , } \\ & { A _ { + , 1 } = 2 h _ { 0 } ^ { \prime } g ( \alpha _ { 0 } ) \sin \iota \cos \iota , } \\ & { A _ { + , 2 } = 2 h _ { 0 } ^ { \prime } g ^ { 2 } ( \alpha _ { 0 } ) \left( 1 + \cos ^ { 2 } \iota \right) , } \\ & { A _ { \times , 0 } = h _ { 0 } \cos \iota , } \\ & { A _ { \times , 1 } = 2 h _ { 0 } ^ { \prime } g ( \alpha _ { 0 } ) \sin \iota , } \\ & { A _ { \times , 2 } = 4 h _ { 0 } ^ { \prime } g ^ { 2 } ( \alpha _ { 0 } ) \cos \iota . } \end{array}
$$

The amplitudes $h _ { 0 }$ and $h _ { 0 } ^ { \prime }$ are defined as

$$
\begin{array} { l } { { \displaystyle h _ { 0 } = - \frac { 1 } { r } \frac { 4 G \omega _ { \mathrm { r o t } } ^ { 2 } } { c ^ { 4 } } \big ( I _ { 1 } - I _ { 2 } \big ) ~ , } } \\ { { \displaystyle h _ { 0 } ^ { \prime } = - \frac { 1 } { r } \frac { G ( \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } ) ^ { 2 } } { c ^ { 4 } } \left( I _ { 3 } - \frac { I _ { 1 } + I _ { 2 } } { 2 } \right) ~ , } } \end{array}
$$

and

$$
g ( \alpha _ { 0 } ) \equiv { \frac { I _ { 1 } a } { I _ { 3 } b } } .
$$

Using eqs.(4.234) and (4.236),and recalling that we have chosen the origin of time so that $\gamma ( 0 ) = \pi / 2$ ,we see that $I _ { 1 } a / ( I _ { 3 } b ) = \tan \alpha _ { 0 }$ ,where $\alpha _ { 0 } = \alpha ( t = 0 )$ . Therefore, in the limit of small wobble angle $\alpha _ { 0 }$ ，we have $g ( \alpha _ { 0 } ) \simeq \alpha _ { 0 }$

From these expressions we see that,setting $\alpha _ { 0 } ~ = ~ 0$ (and therefore $g ( \alpha _ { 0 } ) = 0 )$ we recover the correct limit of rotation around a principal axis,given in eqs. (4.219), (4.220) and (4.224).34

34Observe that in Section 4.2.1 we choose the origin of time so that，at $t = 0$ theaxis $x _ { 1 } ^ { \prime }$ is aligned with the axis $_ { x _ { 1 } }$ ，i.e. $\gamma ( 0 ) = 0$ ，while here we have chosen $\gamma ( 0 ) ~ = ~ \pi / 2$ .This is the origin of the overall minus sign between eq.(4.224)and eq. (4.285).As discussed in Note 27,we can reabsorb the minus sign in both $h _ { 0 }$ and $h _ { 0 } ^ { \prime }$ rotating by anangle $\pi / 2$ in the transverse plane the axes $( \hat { \mathbf { u } } , \hat { \mathbf { v } } )$ used to define the plus and cross polarizations.

Instead, setting $I _ { 1 } = I _ { 2 }$ (and recalling, from eq. (4.281) and Note 32. that $\Omega = \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } } )$ ，we recoyer the correct limit of precession of an axisymmetric body when $\alpha$ is $\mathrm { \$ { m a l l } }$ ，given in eqs. (4.246)-(4.252)

We see that, to zeroth-order lin $g ( \alpha _ { 0 } )$ , we find the line at $\omega _ { \mathrm { g w } } = 2 \omega _ { \mathrm { r o t } }$ due to rotation around a principal axis.To order $g ( \alpha _ { 0 } )$ emerges a line at $\omega _ { \mathrm { g w } } = \omega _ { \mathrm { r o t } } + \omega _ { \mathrm { p } }$ , and to order $g ^ { 2 } ( \alpha _ { 0 } )$ we get a further line at $\omega _ { \mathrm { g w } } =$ $2 \omega _ { \mathrm { r o t } } + 2 \omega _ { \mathrm { p } }$ .If we expand to higher order in $g \big ( \alpha _ { 0 } \big )$ ，we find two sets of lines at frequencies,respectively,

and

$$
\begin{array} { r } { \omega _ { \mathrm { g w } } = 2 \omega _ { \mathrm { r o t } } + 2 k \omega _ { \mathrm { p } } \mathrm { , } } \\ { \omega _ { \mathrm { g w } } = \omega _ { \mathrm { r o t } } + ( 2 k + 1 ) \omega _ { \mathrm { p } } \mathrm { , } } \end{array}
$$

with $k = 0 , 1 , 2 , \ldots$ ，whose intensity is suppressed by increasing powers of $g ( \alpha _ { 0 } )$

To conclude this section，we should stress that all results discussed above have been obtained for rigid bodies. For application to neutron stars,a more realistic modeling of the neutron star interior (e.g.a fluid body with an elastic crust） is hecessary. We will come back to realistic neutron stars in Vol. 2.

# 4.3Radial infall into a black hole

In this section we compute the GWs produced when an object falls radially into a black hole.We will start from the simple case of the infall ofa point-like particle.In principle,ina full computation we should treat GWsas perturbations over the curved black hole space-time,rather than using the expansion over flat space-time of the linearized theory that we have discussed until now.As we will see,however,the lowfrequency part of the spectrum can be computed within our formalism, and the frequency at which the approach breaks down can be estimated. This allows us to perform,in a rather simple setting，this instructive computation. Next we will consider what happens when a real star, ratherthan a point-like object,falls intp a black hole.We will see that the star can be disrupted by the tidal force of the black hole,and as a result the radiation emitted by the various parts of the body adds up incoherently. Beside its intrinsic interest,this problem will then allow us to appreciate the difference between cdherent and incoherent emission of gravitational radiation.

# 4.3.1 Radiation from an infalling point-like mass

We then begin by computing the radiation generated by a point-like particle of mass $m$ which fallsradially intoa black hole of mass $M$ ，with $m \ll M$ .We make a number of simplifying assumptions.First of all,we Compute the GW production using the @quations of linearized theory.In principle this is not correct,since in linearized theory we expand around the flat-space metric,while here we should rather expand around the Schwarzschild metric. Second，we use the Newtonian equation of motion,rather than the geodesics of general relativity in the Schwarzschild metric.Thus,if the particle comes from the positive direction of the $z$ axis,starting with zero velocity at infinity,we write

$$
\frac { 1 } { 2 } m { \dot { z } } ^ { 2 } - \frac { G m M } { z } = 0
$$

and therefore

$$
\dot { z } = - c \left( \frac { R _ { S } } { z } \right) ^ { 1 / 2 } ,
$$

where $R _ { S } = 2 G M / c ^ { 2 }$ is the Schwarzschild radius of the black hole. Third,we assume that most of the radiation is emitted when the particle i non-relativistic,and therefore we use the quadrupole formula.

In the last part of the trajectory,close to the black hole horizon,all these assumptions break down．In particular,eq.(4.291） is certainly not valid close to the horizon,and it is also incompatible with the nonrelativistic assumption,since it formally gives $\dot { z } = - c$ at $z = R _ { S }$ . However,at sufficiently large distances the flat-space Newtonian approximation is correct,and these approximations become legitimate.Thus,we first compute the radiation emitted from $z = + \infty$ until a value $z = R$

As long as $R \gg R s$ our approximations are justifed. We wil th discuss the extrapolation $R \to R _ { S }$

We first compute the total radiated power,using eq. (3.76) andd serving that, in our problem, we have only one non-vanishing compone of $M _ { i j }$ ， $M _ { 3 3 } = m z ^ { 2 } ( t )$ . Then

$$
\begin{array} { l } { { \displaystyle P _ { \mathrm { q u a d } } = \frac { 2 } { 1 5 } \frac { G } { c ^ { 5 } } \langle \ddot { M } _ { 3 3 } ^ { 2 } \rangle } } \\ { { \displaystyle \quad = \frac { 2 } { 1 5 } \frac { G m ^ { 2 } } { c ^ { 5 } } \langle ( 6 \dot { z } \ddot { z } + 2 z \ddot { z } ) ^ { 2 } \rangle . } } \end{array}
$$

The total radiated energy, in the quadrupole approximation,is therefo

$$
E = \frac { 2 } { 1 5 } \frac { G m ^ { 2 } } { c ^ { 5 } } \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t ( 6 \dot { z } \ddot { z } + 2 z \ddot { z } ^ { \cdot } ) ^ { 2 } ,
$$

35 As we will see below,the frequency spectrum is peaked at $\omega = O ( c / R _ { S } )$ so the typical period of the GW is of the order of the light travel time across the Schwarzschild radius $R _ { S }$ .Therefore the integral over time from-oo to tmax is actually an integration over many periods of the typical gravitational radiation.

where the integration over $t$ make superfluous the time average35 and $t _ { \mathrm { m a x } }$ is defined by $z ( t _ { \operatorname* { m a x } } ) \ d t = R$ We write $d t = d z / \dot { z }$ and, usi eq. (4.291), $\Ddot { z } \ = \ - c ^ { 2 } R _ { S } / ( 2 z ^ { 2 } )$ and $\ddagger { ' } = \ - ( c ^ { 3 } / R _ { S } ^ { 2 } ) ( R _ { S } / z ) ^ { 7 / 2 }$ . Then setting $u = z / R s$ ,we get

$$
\begin{array} { l } { { E = \displaystyle \frac { 2 } { 1 5 } \frac { G m ^ { 2 } } { R _ { S } } \int _ { R / R _ { S } } ^ { \infty } d u u ^ { - 9 / 2 } } } \\ { { \ = \displaystyle \frac { 4 } { 1 0 5 } \frac { G m ^ { 2 } } { R _ { S } } \left( \frac { R _ { S } } { R } \right) ^ { 7 / 2 } . } } \end{array}
$$

Of course,the radiation increases if $R$ decreases. If we extrapolate the result down to $R = R _ { S } = 2 G M / c ^ { 2 }$ we get

$$
E = { \frac { 2 } { 1 0 5 } } m c ^ { 2 } \left( { \frac { m } { M } } \right) \simeq 0 . 0 1 9 m c ^ { 2 } \left( { \frac { m } { M } } \right) .
$$

This extrapolation turns out tobe remarkably close to the result ob tained with the expansion over the Schwarzschild metric, using the gen eral relativistic equations of motion and performing the full relativistic computation of GW production rather than using the quadrupole formula.The result of this calculation $3 6$ is in fact

36 See Davies,Ruffni,Pressand Price (1971).We will discuss this computation in Vol. 2.

$$
E \simeq 0 . 0 1 0 m c ^ { 2 } \left( \frac { m } { M } \right) .
$$

Observe that the energy radiated in GWs is smaler than the rest energy $m c ^ { 2 }$ of the particle, by a factor $\dot { m } / M$

The fact that the quadrupole approximation works quite wel means that,despite the fact that in the last part of the trajectory the particle becomes relativistic,stillthe total power is dominated by the quadrupole and in general by the lowest multipoles. Since the radiation emitted at high multipoles is beamed intoa narrow forward cone,while at low multipoles it is distributed on a large solid angle,the fact that the low multipoles dominate means that,in the radial infall into a black hole, there is no beaming of gravitational radiation. We will see a similar phenomenon when we study the gravitational radiation emitted by an accelerated particle,in Section 4.4.This is in sharp contrast with the electromagnetic case where instead,when the source reaches relativistic velocities,the high multipoles dominate,and the radiation is beamed.

We can also use eq.(4.296) to give an estimate of the energy radiated in GWs in the head-on collision of two black holes of equal mass $M$ In this case,we substitute $m$ with the reduced mass $M / 2$ and we get $E \sim$ $2 . 5 \times 1 0 ^ { - 3 } M c ^ { 2 }$ ,which is quite close to the result $E \simeq ( 1 - 2 ) \times 1 0 ^ { - 3 } M c ^ { 2 }$ obtained from numerical simulations.

We now wish to compute the frequency spectrum of the radiation emitted. In principle,in order to compute the Fourier transform of a function of time $F ( t )$ ，we need to know $F ( t )$ on the whole interval $- \infty < t < \infty$ However,our Newtonian trajectory (4.291） is a good approximation to the exact general relativistic geodesic only up to a maximum value of rime $t _ { \mathrm { m a x } }$ such that $z ( t _ { \operatorname* { m a x } } ) \equiv R \gg R _ { S }$ ;beyond $t _ { \mathrm { m a x } }$ it becomes at first a poor approximation to the correct result and finally it even becomes completely meaningless physically,since it formallygives $| \dot { z } | > 1$ and ${ z < R _ { S } }$ .Therefore,within our non-relativistic Newtonian approximation, we cannot compute the full form bf the spectrum. However,we mow that a system with typical size $d$ and typical velocity $v$ radiates GWs with a reduced wavelength ${ \mathfrak { X } } \sim d ( c / v )$ ,see eq.(3.24).When the particle approaches the horizon,the size of the relevant length-scale of te particle-black hole system, for computing the time-varying part of te mass moment,is of order $R _ { S }$ ,and $v \sim c$ ,and therefore $\smash { \frac { \ d } { \lambda } } \sim R _ { S }$ .On the other hand,when the particle is at $R \gg R _ { S }$ ,the length-scale which anters in the time-varying quadrupole moment is of order $R$ and $v \ll c$ s the system radiates at $\dot { x } \sim R ( \dot { c } / v ) \gg R \gg R _ { S }$

This means that,with the Newtonian part of the trajectory,we can reliably compute the part of the spectrum with $\vec { \lambda } \gg R _ { S }$ ，or $\omega R s \ll c$ since this radiation is generated when the particle is at large distance fom the black hole. The complete spectrum will be peaked at $\omega R _ { S } \sim c$ ， but the radiation at these frequencies is generated close to the horizon where a full general-relativistic computation is necessary. Finally, the pectrum will be necessarily cutoff exponentially for $\omega R _ { S } \gg c$ ，since there is no length-scale smaller than $R _ { S } |$ in the problem.

To compute the spectrum at $\omega R s \ll c$ we can therefore use eq. (4.291). The solution of this equation of motion is

$$
z ^ { 3 / 2 } ( t ) - z ^ { 3 / 2 } ( t _ { 0 } ) = \frac { 3 } { 2 } R _ { S } ^ { 1 / 2 } c ( t _ { 0 } - t ) .
$$

Defning $\hat { t }$ from $( 3 / 2 ) R _ { S } ^ { 1 / 2 } c \bar { t } \equiv z ^ { 3 / 2 } ( t _ { 0 } ) \not | + ( 3 / 2 ) R _ { S } ^ { 1 / 2 } c t _ { 0 }$ ,eq. (4.297) becomes $z ^ { 3 / 2 } ( t ) = ( 3 / 2 ) R _ { S } ^ { 1 / 2 } c ( \bar { t } - t )$ $\mathrm { A t } | t = - \infty$ we have $z ( t ) = + \infty$ while the minimum value $z ( t ) = R$ is reached at a finite time

$$
t _ { \mathrm { m a x } } = \bar { t } - \frac { 2 R ^ { 3 / 2 } } { 3 c R _ { S } ^ { 1 / 2 } } .
$$

We further introduce the variable $\tau = \bar { t } - t$ ,s0

$$
z ( \tau ) = \left( { \frac { 3 } { 2 } } R _ { S } ^ { 1 / 2 } c \tau \right) ^ { 2 / 3 } ,
$$

and $c \tau$ ranges over the interval $2 R ^ { 3 / 2 } / ( 3 R _ { S } ^ { 1 / 2 } ) \ < \ c \tau \ < \ \infty$ Equ tion (4.292) gives

$$
{ \cal E } = \frac { 2 G } { 1 5 c ^ { 5 } } \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t \stackrel { . . . } { M } _ { 3 3 } ^ { 2 } .
$$

Writing $M _ { 3 3 } ( t )$ in Fourier transform one obtains

$$
E = \frac { 2 G } { 1 5 c ^ { 5 } } 2 \int _ { 0 } ^ { \omega _ { \mathrm { m a x } } } \frac { d \omega } { 2 \pi } \omega ^ { 6 } | \tilde { M } _ { 3 3 } ( \omega ) | ^ { 2 } { , }
$$

37The contribution from negative frequencies gives the factor of 2 in front of the integral.

where,as discussed above, $\omega _ { \mathrm { m a x } } \ll c / R s$ is the frequency for which ou ignorance of the trajectory beyond $t _ { \mathrm { m a x } }$ becomes important.37 However here we must be careful because

$$
\tilde { M } _ { 3 3 } ( \omega ) = m \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t z ^ { 2 } ( t ) e ^ { i \omega t }
$$

diverges， since as $t  - \infty$ we have $z ( t ) \to + \infty$ Fortunately， this divergence is harmless:it simply reflects the fact that the size of the particle-black hole system,and therefore its quadrupole moment,goe to infinity. However this divergent part of the quadrupole moment is static since,from eq. (4.291),as $z  \infty$ we have $\dot { z }  0$ ,and thereforeit does not contribute to GW production.To dispose of this divergence the simplest way is to consider the Fourier transform of $\ddot { M } _ { 3 3 } ( t )$ rather than of $M _ { 3 3 } ( t )$ ，since in $\ddot { M } _ { 3 3 } \dot { ( t ) }$ the static term has been eliminated. Therefore,instead of eq.(4.3oi),we write

$$
E = \frac { 4 G } { 1 5 c ^ { 5 } } \int _ { 0 } ^ { \omega _ { \mathrm { m a x } } } \frac { d \omega } { 2 \pi } \omega ^ { 2 } | \tilde { \dot { M } } _ { 3 3 } ( \omega ) | ^ { 2 } .
$$

Using eq. (4.299) we find

$$
\begin{array} { c } { { \displaystyle \ddot { M } _ { 3 3 } ( t ) \equiv 2 m ( z \ddot { z } + \dot { z } ^ { 2 } ) } } \\ { { \displaystyle \stackrel { } { = } m \left( \frac { 2 R _ { S } c ^ { 2 } } { 3 \tau } \right) ^ { 2 / 3 } , } } \end{array}
$$

and, recalling that $- \infty < t < | t _ { \mathrm { m a x } } |$ corresponds to $\tau _ { \mathrm { m i n } } < \tau < \infty$ with $\tau _ { \mathrm { m i n } } \equiv 2 R ^ { 3 / 2 } / ( 3 c R _ { S } ^ { 1 / 2 } )$ ，

$$
\tilde { \ddot { M } } _ { 3 3 } ( \omega ) = m \left( \frac { 2 R _ { S } c ^ { 2 } } { 3 } \right) ^ { 2 / 3 } \int _ { \tau _ { \mathrm { m i n } } } ^ { \infty } d \tau \tau ^ { - 2 / 3 } e ^ { - i \omega \tau } .
$$

Defining $u = \omega \tau$

$$
\tilde { \ddot { M } } _ { 3 3 } ( \omega ) = m \omega ^ { - 1 / 3 } \left( \frac { 2 R _ { S } c ^ { 2 } } { 3 } \right) ^ { 2 / 3 } \int _ { \omega \tau _ { \mathrm { m i n } } } ^ { \infty } d u u ^ { - 2 / 3 } e ^ { - i u } .
$$

The computation is valid down to $R$ of order a few times $R _ { S }$ ,s0 $\tau _ { \mathrm { m i n } } =$ $O ( R _ { S } / c )$ and,in the limit $\omega R _ { S } \ll c$ ，which is the limit in which our computation is justified,the leading term is obtained approximating the

lower limit of the above integral with zerol Then we get an Euler Gamma function

$$
\int _ { 0 } ^ { \infty } d u u ^ { - 2 / 3 } e ^ { - i u } = e ^ { - i \pi / 6 } \Gamma \left( 1 / 3 \right) ,
$$

as one can see rotating the contour to the negative imaginary semiaxis of the complex $u$ -plane,and eq. (4.303) gives

$$
\begin{array} { l } { \displaystyle \frac { d E } { d \omega } = \frac { 2 G } { 1 5 \pi c ^ { 5 } } \omega ^ { 2 } | \tilde { \tilde { M } } _ { 3 3 } ( \omega ) | ^ { 2 } } \\ { \displaystyle = \left( \frac { 2 } { 3 } \right) ^ { 7 / 3 } \frac { \Gamma ^ { 2 } ( 1 / 3 ) } { 5 \pi } \frac { G m ^ { 2 } } { c } \left( \frac { \omega R _ { S } } { c } \right) ^ { 4 / 3 } } \\ { \displaystyle \simeq 0 . 1 7 7 \frac { G m ^ { 2 } } { c } \left( \frac { \omega R _ { S } } { c } \right) ^ { 4 / 3 } , \qquad \quad ( \omega R _ { S } \ll c ) . } \end{array}
$$

To study the spectrum when $\omega R _ { S } / c$ is not small we need the full generalrelativistic computation，but we expect from the physical arguments presented above that it must reach a maximum at $\omega R _ { S } / c = O ( 1 )$ ，and will be cutoff exponentially when $\omega R s / c \gg 1$ ，Indeed,the numerical results of Davies,Ruffini,Press and Price (1971) show that the spectrum reaches a maximum at $\omega R s / c \simeq 0 . 6 4$ and then is cutoff exponentially, with an empirical law $d E / d \omega \sim \exp \left\{ - \kappa \omega R s / c \right\}$ with $\kappa \simeq 5$

# 4.3.2 Tidal disruption of a real star falling into a black hole.Coherent and incoherent radiation

We have seen in the previous subsection that,within the non-relativistic Newtonian approximation, we can correctly reproduce the order of magmitude of the power radiated in the radial infall of a point-like particle mto a BH,and we can compute the spectrum for $\omega R s \ll 1$ .The inclusion of the full non-linearities of general relativity amounts only to a corection of about a factor of two in the total power,compare eqs. (4.295) d (4.296).

$\mathrm { A }$ point-like particle is however an idealization,and in astrophysical plications we are rather interested in the infall of an extended object like a main sequence star,a white dwarf or a neutron star.We will see mthis subsection that in this case,because of the tidal disruption of the ras it falls into the BH, the radiation can be emitted incoherently,and Iis can reduce the production of GWs by many orders of magnitudes.

To understand qualitatively the differehce between coherent and incoerent radiation,observe that in eq. (4.295) we found a radiated energy $\bar { E } \sim m ^ { 2 } / M$ ,where $M$ is the BH mass and $m$ is the mass of the infalling Mrticle (or,more precisely, the reduced mass of the particle-BH sysm.but we are assuming $m \ll M$ ).Ifwe describe an extended object mass $m$ as a collection of $N$ particles of mass $\delta m$ and $m = N \delta m$ ,we Terefore find that,if the $N$ constituents radiate coherently as a single bject of mass $m$ ,the radiated energy is

$$
E ^ { ( \mathrm { c o h e r e n t } ) } \sim \frac { m ^ { 2 } } { M } = N ^ { 2 } \frac { ( \delta m ) ^ { 2 } } { M } .
$$

This $N ^ { 2 }$ dependence can also be understood observing that the to tal amplitude of the GW is the sum of the separate amplitudes,s $h _ { \mathrm { t o t } } = \mathrm { \hat { Z } } _ { i = 1 } ^ { N } h _ { i }$ where $i$ labtheetst ent radiation the various terms in this sum have the same phase, s $h ^ { \mathrm { t o t } } = { \cal O } ( N )$ and the radiated energy $E \sim \dot { h } _ { \mathrm { t o t } } ^ { 2 }$ is $O ( N ^ { 2 } )$ For incoher ent radiation,the mixed terms in $( \sum _ { i } { \dot { h } } _ { i } ) ^ { 2 }$ interfere destructively and we are only left with the diagbnal terms $\textstyle \sum _ { i } { \dot { h } } _ { i } ^ { 2 }$ .Therefore in this $\cos \theta$ the energy is $N$ times the energy radiated by a single constituent,

![](images/fe4872da19be91d95da5f0afff820a5770c894fb685b26a4e3d2eaecc294ebe0.jpg)  
Fig.4.18 The estimate of the tidal radius discussed in the text.

$$
E ^ { \mathrm { ( i n c o h e r e n t ) } } \sim N \frac { ( \delta m ) ^ { 2 } } { M } = \frac { 1 } { N } \frac { m ^ { 2 } } { M } ,
$$

and the incoherent radiation is smaller by a factor $N$ with respect t coherent radiation. Observe that,in the limit $N \to \infty$ with $m$ fixed,th incoherent radiation even goes to zero.

Whether a distribution of sources radiates coherently or incoherentl depends on the wavelength of the GW that we consider and on the lineal size $a$ of the system. If $a \ll \frac { 1 } { \lambda }$ ,the phase of the GW does not chang appreciably over the whole source and the radiation is coherent,whilei $a \gg \dagger$ the phases from the single constituents oscillate strongly over th system and the mixed terms in $( \sum _ { i } { \dot { h } } _ { i } ) ^ { 2 }$ average to zero,so the radiatiol is incoherent. The transition between these two regimes is governed by a form factor which,for the problem of the infall of a star into a black hole (BH),will be computed Helow.

To perform this computatioh,we need first of all to understand how the shape of an infalling star is distorted by the tidal gravitational field of the black hole.A star is an object held together by self-gravity. A first crude estimate of the tidal radius $r _ { \mathrm { t i d a l } }$ ,i.e.of the star-BHdistance where the tidal force exerted by the BH is strong enough to disrupt the star,can be obtained as follows.We model a star of mass $m$ as two particle of mass $m / 2$ ,orbiting each other in a circular orbit of radius $0 .$ and we consider a BH of mass $M$ at a distance $r$ from the center of the star,see Fig.4.18.Then the tidal force which tends to disrupt the stal is

$$
{ \begin{array} { r l } & { F _ { \mathrm { t i d a l } } = { \frac { G M ( m / 2 ) } { ( r - a ) ^ { 2 } } } - { \frac { G M ( m / 2 ) } { ( r + a ) ^ { 2 } } } } \\ & { ~ \simeq 2 G M m { \frac { a } { r ^ { 3 } } } . } \end{array} }
$$

The system is broken apart if this force is larger than the gravitational attraction between the two bodies of mass $m / 2$ ,so if

$$
2 G M m { \frac { a } { r ^ { 3 } } } > { \frac { G ( m / 2 ) ^ { 2 } } { ( 2 a ) ^ { 2 } } } ,
$$

which gives $r < r _ { \mathrm { t i d a l } } \simeq 3 . 2 ( M / m ) ^ { 1 / 3 } a$ .The numerical coefficient depends of course on our crude schematization of the extended object. If we rather model the star as an incompressible spheroid of mass $m _ { i }$ mean radius $a$ and constant density,the tidal radius becomes (see Chandrasekhar 1969,Section 56)

$$
r _ { \mathrm { t i d a l } } \simeq 2 . 2 ( M / m ) ^ { 1 / 3 } a .
$$

We denote by $a$ the radius of the star when it is far from the BH,and by $a _ { h }$ the value of its radial size by the time that the star is close to the BH horizon. We can estimate the order of magnitude of $a _ { h }$ ,using the Newtonian trajectory (4.297) for a particle falling radially along the $z$ axis,

$$
z ( t ) = \left[ z _ { 0 } ^ { 3 / 2 } + \frac { 3 } { 2 } R _ { S } ^ { 1 / 2 } c ( | t _ { 0 } - t ) \right] ^ { 2 / 3 } .
$$

Taking the variation with respect to $z _ { 0 }$ we see from this equation that two points that at time $t _ { 0 }$ are separated by a radial distance $\delta z _ { 0 }$ ,at time tare separated by $\delta z ( t ) = [ z _ { 0 } / z ( t ) ] ^ { 1 / 2 } \delta z _ { 0 } .$ We take as $t _ { 0 }$ the time when the starcrosses the tidal radius,and is therefore still undeformed.Then rear the horizon the star is an elipsoid with semimajor axis $a _ { h }$ given by

$$
a _ { h } = \left( \frac { r _ { \mathrm { t i d a l } } } { R _ { S } } \right) ^ { 1 / 2 } a .
$$

The evolution of the shape of the star as it plunges toward the BH shown in Fig.4.19. The effect of the tidal distortion can be quite dramatic.For instance,a main sequence star of $1 M _ { \odot }$ has a radius $a \simeq$ $7 \times 1 0 ^ { 5 } ~ \mathrm { k m }$ If it falls into a BH witha mass $1 0 M _ { \odot }$ and therefore $R _ { S } \simeq 3 0 ~ \mathrm { k m }$ ,eq. (4.313) gives $r _ { \mathrm { t i d a l } } \simeq 4 . 7 a$ and $( r _ { \mathrm { t i d a l } } / \dot { R } _ { S } ) ^ { 1 / 2 } \sim 3 0 0$

We know from the previous subsection that most of the radiation is mitted when the star is close to the horizon and therefore when it has size $a _ { h }$ in the radial direction. From thediscussion at the beginning of tis subsection we know that a source whose larger dimension is of order will radiate coherently only the wavelengths which satisfy $\dag \gg a _ { h }$ ,or $\langle \langle c | a _ { h }$ .Therefore the parameter which governs the loss of coherence

$$
A ( \omega ) \equiv \frac { \omega a _ { h } } { c } = \frac { \omega a } { c } \left( \frac { r _ { \mathrm { t i d a l } } } { R _ { S } } \right) ^ { 1 / 2 } .
$$

For frequencies such that $A ( \omega ) \gg 1$ we have incoherent radiation while rfrequencies that satisfy $A ( \omega ) \ll 1$ the radiation is coherent. In the furmal limit $a  0$ we have $A ( \omega ) \to 0$ and we get back the point-like ssult.

As we mentioned in the previous subsection,the point-like spectrum peaked at $\omega = \bar { \omega } \simeq 0 . 6 4 c / R _ { S }$ ，Therefore，when $0 . 6 4 / R _ { S } \ll 1 / a _ { h }$ ， mly the high-frequency tails of the point-like spectrum are suppressed gcause of incoherent emission. These high frequency tails contributed myway negligibly to the total power even in the point-like case,since saw that they were already exponentially suppressed. Therefore, wten $0 . 6 4 / R _ { S } \ll 1 / a _ { h }$ the total power is practically the same as in le point-like case. On the contrary,if $0 . 6 4 / R _ { S } \gg 1 / a _ { h }$ ，incoherent mission suppresses the radiation in the region which includes the peak, id where most of the power is concentrated,and the total radiated wer becomes a negligible fraction of the point-like case.Defining $\bar { A } =$ $\bar { \omega } a _ { h } / c = 0 . 6 4 a _ { h } / R _ { S }$ and using eqs. (4.315)and (4.313), we find

![](images/b4f43460b6292d34523a3b691933a334536daff6d6f2dfd147a2d359523c5178.jpg)  
Fig.4.19 An infalling star of radius $a$ is tidally deformed by the black hole when it enters within the tidal radius $\boldsymbol { r } _ { \mathrm { t i d a l } }$ .By the time the horizon is approached, the the star is an ellipsoid with semimajor axis $a _ { h }$

Table 4.1 Suppression of gravitatiqnal radiation for stars falling radially intoa bladk hole,for different values of the mass $M$ of the black hole.In all cases the mass @ the star is taken to be $m = 1 M _ { \odot }$ Adapted from Table 1of Haugan, Shapiro and Wasserman (1982).   

<table><tr><td>Stellar type</td><td>a(km)</td><td>M/Mo (Ttida1/Rs)1/2</td><td>A</td></tr><tr><td>Main sequence</td><td>7×105</td><td>10 300</td><td>3×105</td></tr><tr><td rowspan="4">White dwarf</td><td></td><td>103 70 106 7</td><td>500</td></tr><tr><td>104 10</td><td></td><td>1</td></tr><tr><td></td><td>40 103</td><td>430</td></tr><tr><td>106</td><td>8 1</td><td>7 0.01</td></tr><tr><td rowspan="3">Neutron star</td><td>10</td><td>10 1.3</td><td>0.4</td></tr><tr><td></td><td>103 1</td><td>7×10-3</td></tr><tr><td>106</td><td>1</td><td>10-5</td></tr></table>

$$
\bar { A } \simeq \frac { a } { R _ { S } } \biggl | \left( \frac { M } { m } \right) ^ { 1 / 9 } ,
$$

and,if $\bar { A } \gtrsim 1$ , we have a strong suppresson of the total radiated power. In Table 4.1 we show the dilatation factor $( r _ { \mathrm { t i d a l } } / R _ { S } ) ^ { 1 / 2 }$ and the parameter $\bar { A }$ for a range of different stars.Observe,from eq. (4.317), that for a given mass $m$ the suppression is more important for stars with large radius $a ,$ ,since they are less compact and have less self-gravity to resist the tidal force of the black hole,and also it is more important for lower BH masses,because the smaller gravitational attraction at & fixed distance is overcompensated by the decrease in Schwarzschild radius,so tidal stripping takes place at shorter radial distances,where the gravitational field is stronger.

From eq. (4.317) and Table|4.1 we see for instance that a $1 M _ { \odot }$ main sequence star produces significant GWs only if it falls into a supermassive BH with mass $\bar { M { \bf \Phi } } > \vert O ( 1 0 ^ { 6 } ) M _ { \odot }$ .For a white dwarf we need $M > O ( 1 0 ^ { 4 } ) M _ { \odot }$ ，while for a neutron star our equation suggest that i is needed $M > O ( 3 ) M _ { \odot }$ .Actually,a neutron star is so compact and has such a large rigidity that we certainly cannot treat it as a dust ball. We will examine in more detail black hole-neutron star coalescences in Vol. 2.

Having understood the physics with relatively simple arguments,we can now be more quantitative and compute the form factor.We found below eq. (4.297) that the solution of the Newtonian equation of motion for a particle falling along the $z$ axis which at $t = t _ { 0 }$ has $z ( t ) = z _ { i }$ ,can be written as

$$
z ^ { 3 / 2 } ( t ; \bar { t } _ { \dot { \imath } } ) = \frac { 3 } { 2 } R _ { S } ^ { 1 / 2 } c ( \bar { t } _ { i } - t ) ,
$$

with $\bar { t } _ { i }$ defined by

$$
\bar { t } _ { i } = t _ { 0 } + \frac { 2 z _ { i } ^ { 3 / 2 } } { 3 c R _ { S } ^ { 1 / 2 } } .
$$

Therefore, for a swarm of $N$ particles of equal mass $\delta m$ ,eq. (4.302) gives

$$
\tilde { M } _ { 3 3 } ( \omega ) = \delta m \sum _ { i = 1 } ^ { N } \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t z ^ { 2 } ( t ; \bar { t } _ { i } ) e ^ { i \omega t } .
$$

Since $z ( t ; \bar { t } _ { i } )$ depends only on the combination ${ \bar { t } } _ { i } - t$ , inside each integral we can shift the integration variable $t  \dot { t } + \bar { t } _ { i }$ .For large $t _ { \mathrm { m a x } }$ this does not change appreciably the upper integration limit,and we get

$$
\begin{array} { l } { \displaystyle \tilde { M } _ { 3 3 } ( \omega ) = \delta m \sum _ { i = 1 } ^ { N } \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t z ^ { 2 } ( t ; 0 ) e ^ { i \omega ( t + \bar { t } _ { i } ) } } \\ { \displaystyle = \left[ ( \delta m ) N \int _ { - \infty } ^ { t _ { \mathrm { m a x } } } d t z ^ { 2 } ( t ; 0 ) e ^ { i \omega t } \right] \left[ \frac { 1 } { N } \sum _ { i = 1 } ^ { N } e ^ { i \omega \bar { t } _ { i } } \right] . } \end{array}
$$

Since $( \delta m ) N$ is the total mass of the system,the first bracket gives the valme of ${ \cal M } _ { 3 3 } ( \omega )$ in the point-like approximation.38 The second bracket sthe form factor,and we denote it by $F ( \omega )$ ，

$$
F ( \omega ) = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } e ^ { i \omega \bar { t } _ { i } } .
$$

l eq. (4.319) we choose $t _ { 0 }$ as the time when the center-of-mass of the tarcrosses the tidal radius,so it is stillan undeformed sphere. At $t = t _ { 0 }$ he i-th constituent is located at $z _ { i } = r _ { \mathrm { t i } } | { \bf { \bar { a } } } | + \delta z _ { i }$ ，with $- a < \delta z _ { i } < a$ d $| \delta z _ { i } | \ll r _ { \mathrm { t i d a l } }$ .Then eq.(4.319）becomes

$$
\begin{array} { r l } & { \bar { t } _ { i } = t _ { 0 } + \frac { 2 \left( r _ { \mathrm { t i d a l } } + \delta z _ { i } \right) ^ { 3 / 2 } } { 3 c R _ { S } ^ { 1 / 2 } } } \\ & { \quad \simeq \left[ t _ { 0 } + \frac { 2 r _ { \mathrm { t i d a l } } ^ { 3 / 2 } } { 3 c R _ { S } ^ { 1 / 2 } } \right] + \left( \frac { r _ { \mathrm { t i d a l } } } { \dot { R } _ { S } } \right) ^ { 1 / 2 } \frac { \delta z _ { i } } { c } . } \end{array}
$$

Ie term in bracket does not depend onl the index $i$ and gives just a mnstant phase in eq. (4.322),which cancels when we take the modulus quuared. Then

$$
F ( \omega ) = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \mathrm { e x p } \{ i \omega ( r _ { \mathrm { t i d a l } } \mathord { \left/ { \vphantom { r _ { \mathrm { t i d a l } } } } \right. \kern - delimiterspace } R _ { S } ) ^ { 1 / 2 } \delta z _ { i } / c \} .
$$

Ising to the continuum limit we get,for a system of uniform density,

$$
F ( \omega ) = \frac { 1 } { V } \int _ { V } d ( \delta z ) d ^ { 2 } x _ { \perp } \exp \{ i \omega ( r _ { \mathrm { t i d a l } } / R _ { S } ) ^ { 1 / 2 } \delta z / c \} ,
$$

merethe integration is over the volume $V$ of the system at time $t _ { 0 }$ ， hen it is an undeformed sphere or radius $a$ and $V = ( 4 / 3 ) \pi a ^ { 3 }$ At

38 As we discussed in the previous subsection,the integral in $\check { M } _ { 3 3 } ( \omega )$ isactually divergent.For the purpose of computing the form factor this is irrelevant;we can repeat the argument with $\tilde { \ddot { M } } _ { 3 3 } ( \omega )$ ，which converges，or we can just regularize the integral in $\tilde { M } _ { 3 3 } ( \omega )$ ， since anyway the form factor factorizes.

fixed $\delta z$ the radius of the circle in the transverse direction is given b $| x _ { \perp } | ^ { 2 } = a ^ { 2 } - ( \delta z ) ^ { 2 } = a ^ { 2 } ( 1 - \psi ^ { 2 } )$ ，where we have written $\delta z = a u$ with -1<u < 1. Then the integration over the transverse plane of the sphere at fixed $\mathcal { U }$ gives $\pi a ^ { 2 } ( 1 + u ^ { 2 } )$ ，and

![](images/a4bfc5723ed5fde177357b3de752cf59c5776e700001494072d5b7c4988a88ba.jpg)  
Fig.4.20 The form factor $F ( A ( \omega ) )$ ， plotted as a function of $\begin{array} { r l } { A } & { { } = } \end{array}$ (wa/c)(rtida1/Rs)1/2.

$$
F ( \omega ) = \frac { 1 } { ( 4 / 3 ) \pi a ^ { 3 } } \pi a ^ { 3 } \int _ { - 1 } ^ { 1 } d u ( 1 - u ^ { 2 } ) \exp \{ i ( \omega a / c ) ( r _ { \mathrm { t i d a l } } / R _ { S } ) ^ { 1 / 2 } u \} .
$$

We see that the combination $A ( \omega ) = ( \omega a / c ) ( r _ { \mathrm { t i d a l } } / R _ { S } ) ^ { 1 / 2 }$ appears i the exponential and governs the form factor, as we expected from th physical arguments presented above.Then

$$
\begin{array} { l } { \displaystyle { F ( \omega ) = \frac { 3 } { 4 } \int _ { - 1 } ^ { 1 } d u ( 1 - u ^ { 2 } ) e ^ { i A ( \omega ) u } } } \\ { \displaystyle { = \frac { 3 } { A ^ { 2 } ( \omega ) } \left[ \frac { \sin A ( \omega ) } { A ( \omega ) } - \cos A ( \omega ) \right] . } } \end{array}
$$

The form factor $f$ is shown inFig.4.20 as a function of $A$ Since $d E / d { \updownarrow }$ is proportional to |M33(ω)|²,the spectrum for a real star is related the point-like spectrum by

$$
\left( \frac { d { \cal E } } { d \omega } \right) ^ { \mathrm { r e a l \ s t a r } } = | { \cal F } ( \omega ) | ^ { 2 } \left( \frac { d { \cal E } } { d \omega } \right) ^ { \mathrm { p o i n t - l i k e } } .
$$

# 4.4Radiation from accelerated masses

In electrodynamics,a prototype example is the radiation emitted b an accelerated charge.In this section we examine the correspondin! gravitational radiation emitted by an accelerated mass.Beside possibl applications to astrophysical situations,this exercise is quite instructiv by itself,and in particular it will allow us to understand that,while elec tromagneticradiation fromaccelerated particles is beamed ina narrow cone in the forward direction,this is not the case for the GWs producel byan accelerated mass.

# 4.4.1GWs produced in elastic collisions

We begin by considering the gravitational radiation produced during the elastic deflection of an object by a fixed scattering center (or,equiva lently,a two-body collision in the center-of-mass frame).We denote the initial and final four-momenta of the object by $p ^ { \mu }$ and $p ^ { \prime } { } ^ { \mu }$ ,respectively

The energy-momentum tensor of a particle of mass $m$ is given i eq. (3.121). In principle, given the interaction between the object and the scattering center,and the initial conditions,we should compute the classical trajectory $x _ { 0 } ^ { \mu } ( t )$ ，plug it in eq. (3.121),and then perform the Fourier transform.However,in general this is neither practically feasible nor really necessary. We can instead approximate the collision $8 0$ instantaneous, and we consider an elastic scattering,so ${ p ^ { \prime } } ^ { 0 } = p ^ { 0 }$ Then we write, using eq. (3.120),

$$
T ^ { \mu \nu } ( { \bf x } , t ) = { \frac { p ^ { \mu } p ^ { \nu } } { \gamma m } } \delta ^ { ( 3 ) } ( { \bf x } - { \bf v } t ) \theta ( - t ) + { \frac { p ^ { \prime \mu } p ^ { \prime \nu } } { \gamma m } } \delta ^ { ( 3 ) } ( { \bf x } - { \bf v } ^ { \prime } t ) \theta ( t ) ,
$$

where $\theta ( t )$ is the step function: $\theta ( t ) = 1$ if $t > 0$ and $\theta ( t ) = 0$ if $t < 0$ In a collision that lasts for a time △t are generated frequencies up to $\ddot { \omega } _ { \mathrm { m a x } } \sim 2 \pi / \Delta t$ and therefore，when we approximate the collision as instantaneous,we are introducing spurious contributions at arbitrarily ligh frequencies.To recover the correct physical result it is sufficient to estimate the time $\Delta t$ actually taken by the colision.In a collision with impact parameter $b$ and relative velocity $\flat$ ,we have $\Delta t \sim b / v$ ,and we must cutoff the spectrum at $\omega _ { \mathrm { m a x } } \sim 2 \pi v / b$ At $\omega \ll \omega _ { \mathrm { { m a x } } }$ the spectrum is well reproduced by the instantaneous approximation.

The four-dimensional Fourier transform of (4.329) is

$$
\begin{array} { l } { { \displaystyle { \tilde { T } } ^ { \mu \nu } ( { \bf k } , \omega ) = \int _ { - \infty } ^ { \infty } c d t \int d ^ { 3 } x T ^ { \mu \nu } ( { \bf x } , t ) e ^ { i \omega t - i { \bf k } \cdot { \bf x } } \ ~ ( 4 . 3 } } \\ { { \displaystyle ~ = \frac { p ^ { \mu } p ^ { \nu } } { \gamma m } \int _ { - \infty } ^ { 0 } c d t e ^ { i \omega t - i { \bf k } \cdot { \bf v } t } + \left| \frac { p ^ { \prime \mu } p ^ { \prime \nu } } { \gamma m } \int _ { 0 } ^ { \infty } c d t e ^ { i \omega t - i { \bf k } \cdot { \bf v } ^ { \prime } t } . \right. } } \end{array}
$$

li the frst integral we add a factor $\epsilon t$ at the exponent, with $\epsilon \to 0 ^ { + }$ ,to ssure the convergence at $t = - \infty$ ,while in the second we add $- \epsilon t$ to sure the convergence at $t = + \infty$ Then

$$
\tilde { T } ^ { \mu \nu } ( { \bf k } , \omega ) = \frac { c } { i \gamma m } \left[ \frac { p ^ { \mu } p ^ { \nu } } { \omega - { \bf k } { \cdot } { \bf v } - i \epsilon } - \frac { p ^ { \prime \mu } p ^ { \prime \nu } } { \omega - { \bf k } { \cdot } { \bf v } ^ { \prime } + i \epsilon } \right] .
$$

Ithe particle which is being deflected is npt massess, the denominators Ie never zero and we can set $\epsilon = 0$ .We compute first in the nonrelativistic limit and then in the general case.

# Non-relativistic limit

Ithis case in thc denominators we approximate $\gamma \simeq 1$ and we neglect he terms $\mathbf { k } { \cdot } \mathbf { v }$ and $\mathbf { k } { \cdot } \mathbf { v } ^ { \prime }$ , so we find simply

$$
\tilde { T } _ { i j } ( \omega ) \simeq - { \frac { i c } { m \omega } } ( p _ { i } p _ { j } - p _ { i } ^ { \prime } p _ { j } ^ { \prime } ) .
$$

We use a reference frame where the scattering plane is the $( x , y )$ plane; te initial velocity is $\mathbf { v } = v ( 1 , 0 , 0 )$ and the final velocity is

$$
\mathbf { v } ^ { \prime } = v \left( \cos \vartheta _ { s } , \sin \vartheta _ { s } , 0 \right) ,
$$

vtere $\vartheta _ { s }$ is the scattering angle and $| { \bf v } ^ { \prime } | = | { \bf v } | = v$ since we are condering elastic scattering. Let $( \theta , \phi )$ be the polar angles which idenuy the direction of the unit vector $\hat { \bf n }$ in this frame (i.e.the angles t describe the angular distribution of the gravitational radiation), so