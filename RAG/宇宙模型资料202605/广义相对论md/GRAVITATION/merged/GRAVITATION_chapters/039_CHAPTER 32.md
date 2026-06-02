# CHAPTER 32

# GRAVITATIONAL COLLAPSE

Now,here,you see,it takes all the running you can do, to keep in the same place.If you want to get somewhere else，you must run twice as fast as that.

# $\pmb { \ S 3 2 . 1 }$ .RELEVANCE OF SCHWARZSCHILD GEOMETRY

The story that unfolded in the preceeding chapter was fantastic! One began with the innocuous looking Schwarzschild line element

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) ,
$$

The roles and relevance of the Schwarzschild geometry

which was derived originally as the external field of a static star. One asked what happens if the star is absent; i.e., one probed the nature of the Schwarzschild geometry when no star is present to generate it. One might have expected the geometry to be that of a point mass sitting at $r = 0$ . But it was not. It turned out to represent a“wormhole” connecting two asymptotically flat universes. Moreover, the wormhole was dynamic. It was created by the “joining together” of two $" r = 0 "$ singularities, one in each universe; it expanded to a maximum circumference of $4 \pi M$ it then recontracted and pinched off, leaving the two universes disconnected once again, each with its own $" r = 0 "$ singularity.

As a solution to Einstein's field equations, this expanding and recontracting wormhole must be taken seriously.It is an exact solution; and it is one of the simplest of all exact solutions. But there is no reason whatsoever to believe that such wormholes exist in the real universe! They can exist only if the expanding universe, ${ \sim } 1 0 \times 1 0 ^ { 9 }$ years ago, was“born” with the necessary initial conditions--with $" r = 0 "$

Schwarzschild singularities ready and waiting to blossom forth into wormholes. There is no reason at all to believe in such pathological initial conditions!

Why, then, was so much time and effort spent in Chapter 31 on understanding the Schwarzschild geometry? (1） Because it illustrates clearly the highly non-Euclidean character of spacetime geometry when gravity becomes strong; (2) because it illustrates many of the techniques one can use to analyze strong gravitational fields; and most importantly(3) because, when appropriately truncated, it is the spacetime geometry of a black hole and of a collapsing star-as well as of a wormhole.

This chapter explores the role of the Schwarzschild geometry in gravitational collapse; the next chapter explores its role in black-hole physics.

# $\$ 32.2$ . BIRKHOFF'S THEOREM

That the Schwarzschild geometry is relevant to gravitational collapse follows from Birkhoff's (l923) theorem: Let the geometry of a given region of spacetime (l) be spherically symmetric,and (2) be a solution to the Einstein field equations in vacuum. Then that geometry is necessarily a piece of the Schwarzschild geometry.The external field of any electrically neutral,spherical star satisfies the conditions of Birkhoff's theorem,whether the star is static, vibrating,or collapsing. Therefore the external field must be a piece of the Schwarzschild geometry.

The uniqueness of the Schwarzschild geometry: Birkhoff's theorem

Birkhoff's theorem is easily understood on physical grounds. Consider an equilibrium configuration that-is unstable against gravitational collapse and that, like all equilibrium configurations (see S23.6), has the Schwarzschild geometry as its external gravitational field. Perturb this equilibrium configuration in a spherically symmetric way,so that it begins to collapse radially. The perturbation and subsequent collapse cannot affect the external gravitational field so long as exact spherical symmetry is maintained. Just as Maxwel's laws prohibit monopole electromagnetic waves, so Einstein's laws prohibit monopole gravitational waves. There is no possible way for any gravitational influence of the radial collapse to propagate outward.

The physics underlying Birkhoff's theorem

Not only is Birkhoff's theorem easy to understand,but it is also fairly easy to prove. Consider a spherical region of spacetime. Spherical symmetry alone is suffcient to guarantee that conditions (i), (ii),and (iii) of Box 23.3 are satisfied, and thus to guarantee that one can introduce Schwarzschild coordinates

Proof of Birkhoff's theorem

$$
\begin{array} { c } { { d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) , } } \\ { { { } } } \\ { { \phi = \phi ( t , r ) , \mathrm { a n d } \ A = A ( t , r ) . } } \end{array}
$$

[See Box 23.3 for proof; and notice that: (1) for generality one must allow $g _ { t t } = - e ^ { 2 \phi }$ and $g _ { \tau } = e ^ { 2 \lambda }$ to be positive or negative (no constraint on sign!): (2) at events where the gradient of the“circumference function” $r$ is zero or null, Schwarzschild coordinates cannot be introduced. The special case $( { \pmb { \nabla } } r ) ^ { 2 } = 0$ is treated in exercise 32.1.]

Impose Einstein's vacuum field equation on the metric (32.2),using the orthonormal components of the Einstein tensor as derived in exercise 14.16:

$$
\begin{array} { r l } & { \quad G _ { \hat { t } \hat { t } } = r ^ { - 2 } ( 1 - e ^ { - 2 A } ) + 2 ( \Lambda _ { \tau } / r ) e ^ { - 2 A } = 0 , } \\ & { \quad G _ { \hat { t } \hat { \tau } } = G _ { \hat { \tau } \hat { t } } = 2 ( \Lambda _ { \ t } / r ) e ^ { - ( A + \phi ) } = 0 , } \\ & { \quad G _ { \hat { r } \hat { \tau } } = 2 ( \phi _ { \star , \tau } / r ) e ^ { - 2 A } + r ^ { - 2 } ( e ^ { - 2 A } - 1 ) = 0 , } \\ & { \quad G _ { \hat { \theta } \hat { \theta } } = G _ { \hat { \phi } \hat { \phi } } = + ( \phi _ { , \tau } + { \phi _ { , \tau } } ^ { 2 } - \phi _ { , \tau } \Lambda _ { , \tau } + \phi _ { , \tau } / r - \Lambda _ { , \tau } / r ) e ^ { - 2 A } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad - ( \Lambda _ { , t t } + { \Lambda _ { , t } } ^ { 2 } - \Lambda _ { , t } \phi _ { , t } ) e ^ { - 2 \phi } = 0 . } \end{array}
$$

Equation (32.3b） guarantees that $\varLambda$ is a function of $r$ only,and equation (32.3a) then guarantees that $\varLambda$ has the same form as for the Schwarzschild metric:

$$
\varLambda = - \frac { 1 } { 2 } \ln | 1 - 2 M / r | .
$$

Equations (32.3c,d) then become two equivalent equations for $\pmb { \phi } ( t , r )$ -equivalent by virtue of the Bianchi identity, $\pmb { \nabla } \pmb { \cdot } \pmb { G } = 0$ whose solution is

$$
\phi = \frac { 1 } { 2 } \ln | 1 - 2 M / r | + f ( t ) .
$$

Here $f$ is an arbitrary function. Put expressions (32.4) into the line element (32.2); thereby obtain

$$
d s ^ { 2 } = - e ^ { 2 { \it f } ( t ) } \bigg ( 1 - { \frac { 2 M } { r } } \bigg ) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

Then redefine the time coordinate

$$
t _ { \mathrm { n e w } } = \int e ^ { t ( t ) } d t ,
$$

and thereby bring the line element into the Schwarzschild form

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

Conclusion: When the spacetime surrounding any object has spherical symmetry and is free of charge,mass,and all fields other than gravity, then one can introduce coordinates in which the metric is that of Schwarzschild. Conclusion restated in coordinate-free language: the geometry of any spherically symmetric vacuum region of spacetime is a piece of the Schwarzschild geometry (Birkhoff's theorem). Q.E.D.

# Exercise 32.1. UNIQUENESS OF REISSNER-NORDSTRM GEOMETRY [Track 2]

Prove the following generalization of Birkhoff's theorem.Let the geometry of a given region of spacetime(l) be sphericaly symmetric,and (2) be a solution to the Einstein field equations

with an electromagnetic field as source. Then that geometry is necessarily a piece of the Reissner-Nordstrom geometry [equation (31.24b)] with electric and magnetic fields,as measured in the standard static orthonormal frames

$$
E = ( Q _ { e } / r ^ { 2 } ) \pmb { e } _ { \hat { r } } , \qquad \pmb { B } = ( Q _ { m } / r ^ { 2 } ) \pmb { e } _ { \hat { r } } , \qquad Q = ( { Q _ { e } } ^ { 2 } + { Q _ { m } } ^ { 2 } ) ^ { 1 / 2 } .
$$

[Hints:(l） First consider regions of spacetime in which $( \pmb { \nabla } r ) ^ { 2 } \neq 0$ ,using the same methods as the text uses for Birkhof's theorem. The result is the Reissner-Nordstrom solution. (2)Any region of dimensionality less than four,in which $( \boldsymbol { \nabla } r ) ^ { 2 } = 0$ (e.g.,the Schwarzschild radius),can be treated as the join between four-dimensional regions with $( \pmb { \nabla } r ) ^ { 2 } \neq 0$ Moreover,the geometry of such a region is determined uniquely by the geometry of the adjoining four-dimensional regions (“junction conditions"; $\ S 2 1 . 1 3 )$ .Since the adjoining regions are necessarily Reissner-Nordstrom (step l),then so are such “sandwiched”regions. (3) Next consider four-dimensional regions in which $\forall r = d r$ is null and nonzero. Show that in such regions there exist coordinate systems with

$$
d s ^ { 2 } = - 2 \Psi ~ d r { d t } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta ~ d \phi ^ { 2 } ) ,
$$

where $\Psi = \Psi ( r , t )$ .Show further that the Ricci tensor for this line element has an orthonormalized component

$$
R _ { \hat { \theta } \hat { \theta } } = 1 / r ^ { 2 } ,
$$

whereas the stress-energy tensor for a spherically symmetric electromagnetic feld has

$$
8 \pi T _ { \hat { \theta } \hat { \theta } } = 8 \pi \bigg ( T _ { \hat { \theta } \hat { \theta } } - \frac { 1 } { 2 } g _ { \hat { \theta } \hat { \theta } } T \bigg ) = Q ^ { 2 } / r ^ { 4 } , Q = \mathrm { c o n s t . }
$$

These quantities, $R _ { \hat { \pmb \theta } \hat { \pmb \theta } }$ and $8 \pi T _ { \hat { \theta } \hat { \theta } }$ ，must be equal (Einstein's field equation) but cannot be because of their different $\pmb { r }$ -dependence. Thus,an electromagnetic field cannot generate regions with ${ \pmb d } { \pmb r } \neq 0$ ， ${ \pmb d } { \pmb r } \cdot { \pmb d } { \pmb r } = 0$ .(4）Finally,consider four-dimensional regions in which $\pmb { d r = 0 }$ .Denote the constant value of $r$ by $^ { a }$ ，and show that any event can be chosen as the origin of a locally well-behaved coordinate system with

$$
\begin{array} { c } { { d s ^ { 2 } = a ^ { 2 } ( - d \widetilde { \tau } ^ { 2 } + e ^ { 2 \lambda } d z ^ { 2 } + d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) , } } \\ { { \lambda = \lambda ( \widetilde { \tau } , z ) , \qquad \lambda ( \widetilde { \tau } = 0 , z ) = 0 , \qquad \dot { \lambda } ( \widetilde { \tau } = 0 , z ) = 0 . } } \end{array}
$$

[Novikov-type coordinate system; see $\ S 3 1 . 4 . ]$ Show that,in the associated orthonormal frame, spherical symmetry demands

$$
{ \cal E } = ( Q _ { e } / a ^ { 2 } ) \pmb { e } _ { z } , \qquad { \cal B } = ( Q _ { m } / a ^ { 2 } ) \pmb { e } _ { \hat { z } } , \qquad { \cal Q } \equiv ( Q _ { e } ^ { \ 2 } + Q _ { m } ^ { \ 2 } ) ^ { 1 / 2 } ,
$$

and that the Einstein feld equations then require $Q = { \pmb a }$ and $e ^ { \lambda } = \cos \mp$ ,so that

$$
d s ^ { 2 } = Q ^ { 2 } ( - d { \widetilde { \tau } } ^ { 2 } + \cos ^ { 2 } { \widetilde { \tau } } d z ^ { 2 } + d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

(5)This solution of the field equations [sometimes called the“Bertotti(1959)-Robinson(l959a) Electromagnetic Universe.”and explored in this coordinate system by Lindquist (1960)] is actually the throat of the Reissner-Nordstrom solution for the special case $Q = M .$ Verify this claim by performing the following coordinate transformation on the Reissner-Nordstrom throat region [equation (31.24b) with $Q = M$ and $| r - Q | \ll Q ]$ ：

$$
r - \ : Q = Q e ^ { - z } \cos \tilde { \tau } , \qquad t = Q e ^ { z } \tan \tilde { \tau } .
$$

(6)Thus,each possible case leads either to no solution at all,or to a segment of the Reissner-Nordstrom geometry. Q.E.D.| Note: The missing case. $( \boldsymbol { \nabla } r ) ^ { 2 } = 0$ in the text's proof of Birkhof's theorem. is resolved by noting that, for $\varrho = 0$ ，steps (3） and (4)above lead to no solutions at all. We thank G. F. R.Ellis for pointing out the omission of the case $( { \pmb { \nabla } } r ) ^ { 2 } = 0$ in the preliminary version of this book.

# \$32.3. EXTERIOR GEOMETRY OF A COLLAPSING STAR

Consider a star that is momentarily static, but will subsequently begin to collapse. Its space geometry at the initial moment of Schwarzschild coordinate time, $t = 0$ ， has two parts: in the exterior, vacuum region $( r > R > 2 M )$ ,it is the Schwarzschild geometry (Birkhoff's theorem!)； but in the star's interior, it is some other,totally different geometry. Whatever the interior geometry may be, it has an embedding diagram at time $t = 0$ which is qualitatively like that of Figure 23.1. (For discussion and proof of this, see $\ S 2 3 . 8 .$ ） Notice that the star's space geometry is obtained by discarding the lower universe of the full Schwarzschild geometry (Figure 31.5,a), and replacing it with a smooth “bowl’on which the matter of the star is contained.

Gravitational collapse analyzed by examining the star's exterior,Schwarzschild geometry

To follow the subsequent collapse of this star in the Schwarzschild coordinate system,or in the Kruskal-Szekeres coordinate system, or in an ingoing Eddington-Finkelstein coordinate system,one can similarly discard that part of the coordinate diagram which lies inside the star's surface,and keep only the exterior Schwarzschild region. (See Figure 32.1.） In place of the discarded interior Schwarzschild region, one must introduce some other coordinate system,line element, and diagram that correctly describe the interior of the collapsing star.

From truncated coordinate diagrams (such as Figures 32.1,a,b,c), one can readily discover and understand the various peculiar features of collapse through the gravitational radius.

The gravitational radius as a point of no return,and the "crushing" at $r = 0$

(l）No matter how stiff may be the matter of which a (spherical) star is made, once its surface has collapsed within the gravitational radius,the star will continue to collapse until its surface gets crushed in the singularity at $\boldsymbol r = 0$ .This one discovers by recalling that the star's surface cannot move faster than the speed of light, so its world line must always make an angle of less than 45 degrees with the $v \cdot$ -axis of the Kruskal-Szekeres diagram.

(2) No signal (e.g., photon) emitted from the star's surface after it collapses inside the gravitational radius can ever escape to an external observer. Rather, all signals emitted from inside the gravitational radius get caught and destroyed by the collapse of the surrounding geometry into the singularity at $r = 0$ as space“pinches off” around the star.

(3) Consequently,an external observer can never see the star after it passes the gravitational radius; and he can never see the singularity that terminates its col-lapse-unless he chooses to fall through the gravitational radius himself and pay the price of death for the knowledge gained.

Does this mean that the collapsing star instantaneously and completely disappears from external view as it reaches the gravitational radius? No, not according to the analysis depicted in Figure 31.1,c: Place an astrophysicist on the surface of a collapsing star,and have him send a series of uniformly spaced signals to a distant astronomer, at rest at $r \gg 2 M ,$ to inform him of the progress of the collapse. These signals propagate along null lines in the spacetime diagram of Figure 31.lc. The signals originate on the world line of the stellar surface, and they are received by the distant astronomer when they intersect his world line, $r =$ constant $\gg M .$ As the star collapses closer and closer to its gravitational radius, $R = 2 M ,$ the signals,which are sent at equally spaced intervals according to the astrophysicist's clock,are received by the astronomer at more and more widely spaced intervals. The astronomer does not receive a signal emitted just before the gravitational radius is reached until after an infinite amount of time has elapsed; and he never receives signals emitted after the gravitational radius has been passed. Those signals, like the astrophysicist who sends them,after brief runs get caught and destroyed by the collapsing geometry in the singularity,at $r = 0$ .It is not only the star that collapses. The geometry around the star collapses.

Hence,to the distant astronomer, the collapsing star appears to slow down as it approaches its gravitational radius: light from the star becomes more and more red-shifted. Clocks on the star appear to run more and more slowly. It takes an infinite time for the star to reach its gravitational radius;and, as seen by the distant astronomer, the star never gets beyond there.

The redshift of signals emitted just before passage through the gravitational radius

The optical appearance of a collpsing star was first analyzed mathematically, giving main attention to radially propagating photons, by J. R. Oppenheimer and H. Snyder (l939). More recently a number of workers have reexamined the problem [see,e.g., Podurets (1964),- Ames and Thorne (1968) and Jaffe (1969)]. The most important quantitative results of these studies are as follows. In the late stages of collapse,when the distant astronomer sees the star to be very near its gravitational radius,he observes its total luminosity to decay exponentially in time

Optical appearance of the collapsing star

$$
\small { \cal L } \propto \exp \left( - \frac { 2 } { 3 \sqrt { 3 } } \frac { t } { 2 M } \right) .
$$

Simultaneously， photons that travel to him along radial trajectories arrive with exponentially increasing redshifts

$$
z = \varDelta \lambda / \lambda \propto e ^ { t / 4 M } .
$$

However,the light from the star is dominated in these late stages, not by photons flying along radial trajectories from near the gravitational radius, but by photons that were deposited by the star in unstable circular orbits as its surface passed through $r = 3 M$ (see $\ S 2 5 . 6$ and Box 25.7).As time passes, these photons gradually leak out the diffuse spherical shell of trapped photons at $r = 3 M$ and fly off to the distant observer, who measures them to have redshift $z \approx 2$ .Consequently,in the late stages of collapse the star's spectral lines are broadened enormously, but they are brightest at redshift $z \approx 2$

![](images/871b40708e54f90f1952b9b2e5d9f0a59debd978e0bafa0c44855d966c88e4eb.jpg)  
Figure 32.1. The free-fall collapse of a star of initial radius $R _ { i } = 1 0 ~ M$ as depicted alternatively in(a) Schwarzschild coordinates,(b） Kruskal-Szekeres coordinates,and (c) ingoing Eddington-Finkelstein coordinates (see Box 31.2).The region of spacetime inside the collapsing star is grey,that outside it is white.Only thegeometry of the exterior region is that of Schwarzschild.The curve separating the grey and white regions is the geodesic world line of the surface of the collapsing star (equations [31.l0]or [32.10] with $r _ { \mathrm { m a x } } = R _ { i } = 1 0 ~ M )$ .This world line is parameterized by proper time, $\tau .$ ，asmeasured by an observer who sits on the surface of the star; the radial light cones,as calculated from $d s ^ { 2 } = 0 .$ are attached to it.

![](images/9bac75ea663b83324cc44b565fa22b1f0bd998d3e22bb6b7f74b965007dd0949.jpg)

Notice that,although the shapes of the light cones are not all the same relative to Schwarzschild coordinates orrelative to Eddington-Finkelstein coordinates,theyareallthesamerelative to Kruskal-Szekeres coordinates.This is because light rays travel along 45-degree lines in the $_ { u , v }$ -plane $( d v = \pm d u )$ ， but they travel along curved paths in the $^ { r , t }$ plane and $r , \mathbf { \bar { \mathcal { V } } }$ -plane.

The Kruskal-Szekeres spacetime diagram shown here is related to the Schwarzschild diagram by equations (31.l3) plus a translation of Schwarzschild time: $t \longrightarrow t + 4 2 . 8 \ M$ The Eddington-Finklestein diagram is related to the Schwarzschild diagram by

$$
{ \widetilde { V } } = t + r ^ { * } = t + r + 2 M \ln | r / 2 M - 1 |
$$

(see Box 31.2).

It is evident from these diagrams that the free-fall collpse is characterized by aconstantly diminishing radius,which drops from $R = 1 0 M$ to $R = 0$ in a finite and short comoving proper time interval, $\begin{array} { r } { \pmb { \mathscr { \Delta } } \tau = 3 5 . 1 \ M . } \end{array}$ The point $R = 0$ and the entire region $r \simeq 0$ outside the star make up a physical“singularity”at which infinite tidal gravitational forces-according to classical,unquantized general relativity-can and do crush matter to infinite density (see end of $\ S 3 1 . 2$ ；also $\ S 3 2 . 6 )$

![](images/5525233796b0c85a20c6c2c2cae65813da3ebddc6ee050a3d0aeb579b4d038ed.jpg)

The Eddington-Finkelstein diagram depicts a series of photons emitted radially from the surface of the collapsing star,and received by an observer at $r = R _ { \mathrm { i n i t i a l } } = 1 0 ~ M .$ The observer eventually-receives all photons emitted radially from outside the gravitational radius;allphotons emited after the star passes through its gravitational radius eventually get pulled into the singularity at $\boldsymbol r = 0$ and any photon emitted radially at the gravitational radius stays at the gravitational radius forever.

Non-free-fall collapse is similar to the collapse depicted here. When pressure gradients are present, only the detailed shape of the world line of the star’s surface changes.

Notice how short is the characteristic $^ e$ -folding time for the decay of luminosity and for the radial redshift:

$$
\begin{array} { r l } & { \tau _ { \mathrm { c h a r } } = 2 M \approx 1 \times 1 0 ^ { - 5 } ( M / M _ { \odot } ) \mathrm { s e c } } \\ & { \qquad = \binom { \mathrm { l i g h t - t r a v e l ~ t i m e ~ a c r o s s ~ a ~ f l a t - s p a c e } } { \mathrm { d i s t a n c e ~ e q u a l ~ t o ~ t h e ~ g r a v i t a t i o n a l ~ r a d i u s } } . } \end{array}
$$

Here $M _ { \odot }$ denotes one solar mass.

# EXERCISE

# Exercise 32.2. REDSHIFTS DURING COLLAPSE

(a)Let a radio transmitter on the surface of a collapsing spherical star emit monochromatic waves of wavelength $\lambda _ { e }$ : and let a distant observer,at the same $\pmb \theta , \pmb \phi$ ,as the transmitter,receive the waves. Show that at late times the wavelength received varies as

![](images/dff4a25de00c6e175a8612ee7f5c312baab296da3a815b6488f751b458a11328.jpg)

The rest of this chapter is Track 2. No.previous Track-2 material is needed as preparation for it, but it is needed as preparation for (1) the Track-2 part of Chapter 33 (black holes),and (2) Chapter 34 (singularities and global methods).

$$
\lambda _ { \mathrm { { r e c } } } / \lambda _ { \mathrm { { e m } } } \propto e ^ { t / 4 M }
$$

[equation (32.6)], where $t$ is proper time as measured by the distant observer.

(b) [Track 2] Use kinetic theory for the outgoing photons (conservation of density in phase space:Liouville's theorem; $\ S 2 2 . 6 \}$ to show that the energy flux of the radiation received (e $\mathtt { r g s / c m ^ { 2 } s e c } )$ varies as

$$
F \propto e ^ { - t / M } .
$$

(c) Suppose that nuclear reactions at the center of the collapsing star generate neutrinos of energy $E _ { e }$ ,and that these neutrinos flow freely outward (negligible absorption in star). Show that the energy of the neutrinos received by a distant observer decreases at late times as

$$
E _ { \mathrm { r e c } } / E _ { e } \propto e ^ { - t / 4 M } .
$$

(d) Show that the flux of neutrino energy dies out at late times as

$$
F \propto e ^ { - t / 2 M } .
$$

(e)Explain in elementary terms why the decay laws (32.8a) and (32.9a) for energy are the same, but the decay laws (32.8b) and (32.9b) for energy flux are different.

(f) Let a collapsing star emit photons from its surface at the black-body rate

$$
\frac { d N } { d \tau } = \Big ( 1 . 5 \times 1 0 ^ { 1 1 } \frac { \mathrm { p h o t o n s } } { \mathrm { c m } ^ { 2 } \mathrm { s e c } \mathrm { K } ^ { 3 } } \Big ) \times \Big ( \mathrm { s u r f a c e ~ a r e a } \Big ) \times \Big ( \mathrm { t e m p e r a t u r e } \Big ) ^ { 3 } .
$$

Let a distant observer count the photons as they pass through his sphere of radius $r \gg M .$ Let him begin his count (time $t = 0$ ）when he sees (via photons traveling radially outward) the center of the star's surface pass through the radius $r = 3 M$ Show that,in order of magnitude,the time he and his associates must wait,until the last photon that will ever get out has reached them,is

$$
t = ( M / M _ { \odot } ) [ 8 \times 1 0 ^ { - 4 } + 5 \times 1 0 ^ { - 5 } \log _ { 1 0 } ( T _ { 1 1 } M / M _ { \odot } ) ] \ \mathrm { s e c o n d s } ,
$$

where $T _ { 1 1 }$ is the star's surface temperature in units of $1 0 ^ { 1 1 } \textbf { K }$

# $\$ 32.4$ . COLLAPSE OF A STAR WITH UNIFORM DENSITY AND ZERO PRESSURE

When one turns attention to the interior of a collapsing star and to the precise world line that its surface follows in the Schwarzschild geometry, one encounters rather complicated mathematics. The simplest case to treat is that of a“star”with uniform density and zero pressure;and,indeed,until recently that was the only case which had been treated in detail. The original-and very complete-analysis of the collapse of such a uniform-density “ball of dust” was given in the clasic paper of Oppenheimer and Snyder (l939).More recently,other workers have discussed it from slightly different points of view and using different coordinate systems. The ap-proach taken here was devised by Beckedorff and Misner (1962).

Because no pressure gradients are present to deflect their motion, the particles on the surface of any ball of dust must move along radial geodesics in the exterior Schwarzschild geometry.For a ball that begins at rest with finite radius, $R = R _ { \mathrm { i } }$ ， at time $t = 0$ ,the subsequent geodesic motion of its surface is given by equations (31.10):

The collapse,from rest, of a uniform-density ball of "dust":

$$
R = ( R _ { i } / 2 ) ( 1 + \cos \eta ) ,
$$

$$
\begin{array} { r l } & { t = 2 M \ln \Big | \frac { ( R _ { i } / 2 M - 1 ) ^ { 1 / 2 } + \tan { ( \eta / 2 ) } } { ( R _ { i } / 2 M - 1 ) ^ { 1 / 2 } - \tan { ( \eta / 2 ) } } \Big | } \\ & { ~ + ~ 2 M ( R _ { i } / 2 M - 1 ) ^ { 1 / 2 } [ \eta + ( R _ { i } / 4 M ) ( \eta + \sin { \eta } ) ] . } \end{array}
$$

(1）world line of ball's surface in exterior Schwarzschild coordinates

Here $R$ is the Schwarzschild radial coordinate (i.e., $4 \pi R ^ { 2 }$ is the star's surface area) at Sch warzschild time $t .$ This world line is plotted in Figure 32.1 for $R _ { i } = 1 0 M ,$ in terms of Schwarzschild coordinates,Kruskal-Szekeres coordinates,and Eddington-Finkelstein coordinates. The proper time read by a clock on the surface of the collapsing star is given by equation (31.10b):

$$
\tau = ( R _ { \dot { \ i } } ^ { 3 } / 8 M ) ^ { 1 / 2 } ( \eta + \sin \eta ) .
$$

Note that the collapse begins when the parameter $\eta$ is zero ( $\mathbf { \mathcal { R } } = R _ { i }$ ， $t = \tau = 0 $ ； and it terminates at the singularity $( R = 0 , \eta = \pi )$ after a lapse of proper time,as measured on any test particle falling with the dust, equal to

$$
\begin{array} { r } { \varDelta \tau = \pi ( R _ { i } ^ { 3 } / 8 M ) ^ { 1 / 2 } . } \end{array}
$$

It is interesting,though coincidental, that this is precisely the time-lapse required for free-fall collapse to infinite density in Newtonian theory [see equation (25.27'), Figure 25:3, and associated discussion].

What is the behavior of the interior of the ballof dust as it collapses? A variety of different interiors for pressureless dust can be conceived (exercise 32.8). But here attention focuses on the simplest of them: an interior that is homogeneous and isotropic everywhere,except at the surface-i.e.,an interior locally identical to a dust-filled Friedmann cosmological model $( \mathbf { B } 0 \mathbf { x } 2 7 . 1 )$ . Is the Friedmann interior to be“open” $( k = - 1 )$ ，“flat” $( k = 0 )$ ，or“closed” $( k = + 1 )$ ？ Only the closed case

(2)interior of ball is identical to a portion of a closed Friedmann universe

is appropriate, since one has already demanded [equation (32.lO)] that the star be at rest initially (initial rate of change of density equals zero;“moment of maximum expansion").

Using comoving hyperspherical coordinates, $x , \theta , \phi$ ,for the star's interior,and putting the origin of coordinates at the star's center,one can write the line element in the interior in the familiar Friedmann form

$$
d s ^ { 2 } = - d \tau ^ { 2 } + a ^ { 2 } ( \tau ) [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ] .
$$

Here $a ( \tau )$ is given by the familiar cycloidal relation,

$$
\begin{array} { c } { { a = \displaystyle \frac { 1 } { 2 } a _ { m } ( 1 + \cos \eta ) , } } \\ { { } } \\ { { \displaystyle \tau = \displaystyle \frac { 1 } { 2 } a _ { m } ( \eta + \sin \eta ) ; } } \end{array}
$$

and the density is given by

$$
\rho = ( 3 a _ { m } / 8 \pi ) a ^ { - 3 } = ( 3 / 8 \pi a _ { m } { } ^ { 2 } ) \biggl [ \frac { 1 } { 2 } ( 1 + \cos { \eta } ) \biggr ] ^ { - 3 }
$$

(3） the join between Friedmann interior and Schwarzschild exterior

[see equations (1),(9),(4),and (5) of Box 27.1,with $\eta$ replaced by $\eta + \pi ]$

There is one possible dificulty with this interior solution. In the cosmological case, the solution was homogeneous and isotropic everywhere. Here homogeneity and isotropy are broken at the star's surface-which lies at some radius

$$
\chi = \chi _ { 0 }
$$

for all $\pmb { \tau }$ ，as measured in terms of the hyperspherical polar angle $x { \mathrm { . } }$ a comoving coordinate (first picture in Box 27.2). At that surface (i.e., three-dimensional world tube enclosing the star's fluid) the interior Friedmann geometry must match smoothly onto the exterior Schwarzschild geometry. If the match cannot be achieved, then the Friedmann line element (32.11) cannot represent the interior of a collapsing star. An example of a case in which the matching could not be achieved is an interior of uniform and nonzero pressure,as well as uniform density. In that case there would be an infinite pressure gradient at the star's surface,which would blow off the outer layers of the star, and would send a rarefaction wave propagating inward toward its center.The uniform distribution of density and pressure would quickly be destroyed.

For the case of zero pressure,the match is possible.As a partial verification of the match,one can examine the separate and independent predictions made by the interior and exterior solutions for the star's circumference, $C = 2 \pi R$ as a function of proper time $\boldsymbol { \mathsf { \tau } }$ at the star's surface. The external Schwarzschild solution predicts the cycloidal relation,

$$
\begin{array} { c } { C = 2 \pi R = 2 \pi ( R _ { \mathrm { i } } / 2 ) ( 1 + \cos { \eta } ) , } \\ { \tau = ( R _ { \mathrm { i } } { } ^ { 3 } / 8 M ) ^ { 1 / 2 } ( \eta + \sin { \eta } ) } \end{array}
$$

[equations (32.1O)]. The interior Friedmann solution predicts a similar cycloidal relation:

$$
C = 2 \pi R = 2 \pi a \sin \chi _ { 0 } = 2 \pi \bigg ( \frac { 1 } { 2 } a _ { m } \sin \chi _ { 0 } \bigg ) ( 1 + \cos \eta ) ,
$$

$$
\tau = \frac { 1 } { 2 } a _ { m } ( \eta + \sin \eta ) .
$$

The two predictions agree perfectly for al time if and only if

$$
\begin{array} { c } { { R _ { \mathrm { i } } = a _ { m } \sin \chi _ { 0 } , } } \\ { { \displaystyle } } \\ { { M = \frac { 1 } { 2 } a _ { \mathrm { m } } \sin ^ { 3 } \chi _ { 0 } . } } \end{array}
$$

A more complete verification of the match is given in exercise 32.4.

For further insight into this idealized model of gravitational colapse,see Box 32.1.

# ExerciSe 32.3. EMBEDDING DIAGRAMS AND PHOTON PROPAGATIONFOR COLLAPSING STAR

Verify in detail the features of homogeneous collapse described in Box 32.1.

# Exercise 32.4. MATCH OF FRIEDMANN INTERIOR TO SCHWARZSCHILD EXTERIOR

The Einstein field equations are satisfied on a star's surface if and only if the intrinsic and extrinsic geometries of the surface's three-dimensional world tube are the same,whether measured on its interior or on its exterior (see $\ S 2 1 . 1 3$ for proof and discussion).Verify that for the collapsing star discussed above, the intrinsic and extrinsic geometries match at the join between the Friedmann interior and the Schwarzschild exterior. [Hints: (a) Use $\eta , \theta , \phi ,$ as coordinates on the world tube of the star's surface,and show that the intrinsic geometry has the same line element

$$
d s ^ { 2 } = a ^ { 2 } ( \eta ) [ - d \eta ^ { 2 } + \sin ^ { 2 } \chi _ { 0 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ] ,
$$

whether measured in the Schwarzschild exterior or in the Friedmann interior.(b) Show that the extrinsic curvature of the world tube has the same components

$$
K _ { \eta \eta } = K _ { \eta \theta } = K _ { \eta \phi } = K _ { \theta \phi } = 0 ,
$$

$$
K _ { \theta \theta } = K _ { \phi \phi } / \sin ^ { 2 } \theta = - a ( \eta ) \sin \chi _ { 0 } \cos \chi _ { 0 } ,
$$

whether measured in the Schwarzschild exterior or in the Friedmann interior.]

# Exercise 32.5. STARS THAT COLLAPSE FROM INFINITY

(a） Patch together a truncated Schwarzschild geometry and the geometry of a truncated “flat” $( k = 0 )$ ,dust-filled Friedmann universe to obtain a model of a star that collapses from rest at an infinite initial radius.[Hint: The world line of the star's surface in the Schwarzschild geometry is given by equations (31.2).]

(b） Similarly patch together a truncated Schwarzschild geometry and the geometry of a truncated “open" $( k = - 1$ ),dust-filled Friedmann universe to obtain a star which collapses from infinity with finite initial inward velocity.

(continued on page 857)

# Box 32.1 AN IDEALIZED COLLAPSING STAR WITH FRIEDMANN INTERIOR AND SCHWARZSCHILD EXTERIOR

(See $\$ 32.4$ and exercises 32.3 and 32.4 for justification of the results described here.)

# Initial State

(1) Take a Friedmann universe ofradius $a = a _ { m }$ at its moment of maximum expansion, $\eta = 0$ ; and slice off and discard the region $x _ { 0 } < x \le \pi$ ,where $\boldsymbol { \chi } _ { 0 }$ is some angle less than $\pi / 2$ . (2) Take a Schwarzschild geometry of mass $M = ( a _ { m } / 2 ) \sin ^ { 3 } x _ { 0 }$ at the moment $t = 0$ ； and slice off and discard the region $r < R _ { i } = a _ { m } \sin \chi _ { 0 }$ .(3) Glue the remaining pieces of Friedmann and Schwarzschild geometry together smoothly along their cut surfaces.The resultant object will be a momentarily static star of uniform density $\rho _ { i } = 3 / ( 8 \pi { a _ { m } } ^ { 2 } )$ ，of mass $M = ( a _ { m } / 2 ) \sin ^ { 3 } \chi _ { 0 } ,$ and of radius $R _ { \mathrm { i } } =$ $a _ { m } \sin \chi _ { 0 } .$

# Subsequent Evolution

Release this star from its intial state,and let it collapse in accord with Einstein's field equations.The interior,truncated Friedmann universe and the exterior,truncated Schwarzschild geometry will evolve just as though they had never been cut up and patched together; and this evolution will preserve the smoothness of the match between interior and exterior!

# Details of the Collapse

Probe the details of the collapse using sequences of embedding diagrams (histories $A B C D$ and $A W X Y$ ),and using photons that propagate radially outward (photons $\alpha , \beta , \gamma , \delta , \epsilon )$ . The example shown here has $\chi _ { 0 } = 0 . 9 6$ and $R _ { i } / M = 2 / \sin ^ { 2 } \chi _ { 0 } = 3$

![](images/8b325aa7fdbc3769872ed185108a5bf7c41262c9adef2144d856853a53951640.jpg)

# History of Collapse as Probed by Hypersurfaces ABCD:

(1） Initial configuration, $A - A ^ { \prime } - A ^ { \prime \prime }$ ，isthat constructed by. cutting and sewing at times $\eta = t = 0$   
(2) Each subsequent configuration has as its interior a slice of constant Friedmann time $\eta$   
(3） The interior remains always a spherical cup of half-angle $x _ { 0 }$ ； but it contracts from radius $\pmb { R } = \pmb { R _ { i } } = \pmb { a _ { m } }$ sin $\chi _ { 0 }$ to $R = 0$ as time increases.   
(4)The matter in the star is all crushed simultaneously to infinite density when $R$ reaches zero, and the external Schwarzschild “funnel” develops a cusp-like singularity at that point.   
(5)As time increases further,this cusp pulls the region $r < 2 M$ of the funnel into $r = 0$ so fast that the outward-traveling photon $\delta$ is gobbled up and crushed.

![](images/99f1a2e9ed7b43effe840992eb2c3a4a5b9be97e6b141c15622f409b4cfb96e9.jpg)

These embedding diagrams must be rotated about the vertical axes in order to become 2-dimensional surfaces analogous to Figure 23.1.

# History as Probed by Hypersurfaces AWXY

(l） Initial configuration, $A - A ^ { \prime } - A ^ { \prime \prime }$ ，is again that constructed by cutting and sewing at $\eta = t = 0$

(2） Subsequent hypersurfaces are very different from $\boldsymbol { \eta } = \mathsf { c o n s t }$

(3)As time passes, a neck develops in the geometry just outside the surface of the star.

(4） This neck becomes tighter and tighter and then pinches off, leaving the star completely isolated from the rest of the universe,and leaving a deadly cusp-like singularity in the exterior geometry where the star used to be.

(5）The isolated star, in its own little closed universe, continues to contract until it is crushed to infinite density,while the external geometry begins to develop another neck and the cusp quickly gobbles up photon 8.

![](images/a3acdef738aa02f1653c73bdef10b0870a1e565ac4b5e19486b1f2d31a0c6662.jpg)

The extreme difference between histories ABCD and AWXY dramatizes the “many-fingered time” of general relativity. The hypersurface on which one explores the geometry can be pushed ahead faster in time in one region,at the option of the party of explorers. Thus whether one region of the star collapses first, or another, or the entire star collapses simultaneously,is a function both of the spacetime geometry and of the choice of slicing. The party of explorers has this choice of slicing at their own control, and thus they themselves to this extent govern what kind of spacelike slices they will see as their exploration moves forward in time. The spacetime geometry that they slice, however, is in no way theirs to control or to change. To the extent that their masses are negligible and they serve merely as test objects, they have no influence whatsoever on the spacetime. It was fixed completely by the specification of the initial conditions for the collapse.In brief, spacetime is four-dimensional and slices are only three-dimensional (and in thepictures here look only two-dimensional or one-dimensional). Any one set of slices captures only a one-sided view of the whole story. To see the entire picture one must either examine the dynamics of the geometry as it reveals itself in varied choices of the slicing or become accustomed to visualizing the spacetime geometry as a whole.

# \$32.5. SPHERICALLY SYMMETRIC COLLAPSE WITH INTERNAL PRESSURE FORCES

So far as the external gravitational field is concerned, the only difference between a freely collapsing star and a collapsing, spherically symmetric star with internal pressure is this: that the surfaces of the two stars move along different world lines in the exterior Schwarzschild geometry. Because the exterior geometry is the same in both cases,the qualitative aspects of free-fall collapse as described in the last section can be carried over directly to the case of nonnegligible internal pressure.

An important and fascinating question to ask is this: can large internal pressures in any way prevent a collapsing star from being crushed to infinite density by infinite tidal gravitational forces? From the Kruskal-Szekeres diagram of Figure 32.1,b, it is evident that, once a star has passed inside its gravitational radius $( R < 2 M )$ ,no internal pressures,regardless of how large they may be,can prevent the star's surface from being crushed in a singularity. The surface must move along a time-like world line,and all such world lines inside $r = 2 M$ hit $r = 0$ Although there is no such theorem now available, one can reasonably conjecture that, if the surface of a spherical configuration is crushed in the $r = 0$ singularity,the entire interior must also be crushed.

The details of the interior dynamics of a spherically symmetric collapsing star with pressure are not so well-understood as the exterior Schwarzschild dynamics. However,major advances in one's understanding of the interior dynamics are now being made by means of numerical computations and analytic analyses [see Misner (1969a) for a review). In these computations and analyses, no new features (at least, no unexpected ones) have been encountered beyond those that occurred in the simple uniform-density, free-fall collapse of the last section.

# Exercise 32.6. GENERAL SPHERICAL COLLAPSE: METRIC IN COMOVING COORDINATES

# EXERCISES

Consider an inhomogeneous star with pressure,undergoing spherical collapse. Spherical symmetry alone is enough to guarantee the existence of a Schwarzschild coordinate system $( t , r , \theta , \phi )$ throughout the interior and exterior of the star [see equation (32.2) and preceding discussion]. Label each spherical shell of the star by a parameter $\pmb { a }$ ,which tells how many baryons are contained interior to that shell. Then $r ( a , t )$ is the world line of the shell with label a. The expression for these world lines can be inverted to obtain $a ( t , r )$ ,the number of baryons interior to radius $r$ at time t. Show that there exists a new time coordinate $\widetilde { t } ( t , r )$ ， such that the' line element (32.2),rewritten in the coordinates $( \widetilde { t } , a , \theta , \phi )$ has the form

$$
d s ^ { 2 } = - e ^ { 2 \widetilde { \phi } } \ : d \widetilde { t } ^ { 2 } + \biggl [ \frac { ( \partial r / \hat { \sigma } a ) _ { \widetilde { t } } d a } { \Gamma } \biggr ] ^ { 2 } + r ^ { 2 } d \varOmega ^ { 2 } ,
$$

$$
\begin{array} { r } {  { \widetilde { \phi } } =  { \widetilde { \phi } } (  { \widetilde { t } } , a ) , \qquad r = r (  { \widetilde { t } } , a ) , \qquad r = r (  { \widetilde { t } } , a ) . } \end{array}
$$

These are “comoving, synchronous coordinates” for the stellar interior.

# Exercise 32.7. ADIABATIC SPHERICAL COLLAPSE: EQUATIONS OF EVOLUTION [Misner and Sharp (1964)]

Describe the interior of a collapsing star by the comoving,synchronous metric (32.19), by the number density of baryons $_ n$ ,by the total density of mass-energy $\pmb { \rho }$ ,and by the pressure $\pmb { p }$ .The 4-velocity of the star's fluid is

$$
\pmb { u } = e ^ { - \widetilde { \phi } } \hat { c } / \hat { c } \widetilde { t } .
$$

since the fluid is at rest in the coordinate system.Let a dot denote a proper time derivative as seen by the fluid-e.g.,

$$
\dot { n } \equiv { \pmb u } [ n ] = e ^ { - \widetilde \phi } ( \partial n / \widetilde \partial \widetilde t ) _ { \alpha } ;
$$

andlet a prime denote a partial derivative with respect to baryon numbere.g.

$$
\begin{array} { r } { n ^ { \prime } \equiv ( \hat { c } n / \hat { \partial } a ) _ { \tilde { t } } . } \end{array}
$$

Denote by $U$ the rate of change of $( 1 / 2 \pi ) \times$ (circumference of shell), as measured by a man riding in a given shell:

$$
U \equiv { \dot { r } } ;
$$

and denote by $m ( \widetilde { t } , a )$ the “total mass-energy interior to shell $\pmb { a }$ at time $\widetilde { t }$

$$
m ( \widetilde { t } , a ) \equiv \int _ { 0 } ^ { a } 4 \pi r ^ { 2 } \rho ( \widetilde { t } , a ) r ^ { \prime } d a .
$$

(See Box 23.1 for discussion of this method of localizing mass-energy.） Assume that the collapse is adiabatic (no energy flow between adjacent shels; stress-energy tensor entirely that of a perfect fluid).

(a) Show that the equations of collapse [baryon conservation, (22.3); local energy conservation,(22.1la)； Euler equation, (22.13)；and Einstein field equations (ex.14.l6)] can be reduced to the following eight equations for the eight functions $\tilde { \phi } , \Gamma , r , n , \rho , p , U , m \colon$

$$
\dot { \boldsymbol { r } } = \boldsymbol { U }
$$

$$
{ \frac { ( n r ^ { 2 } ) } { n r ^ { 2 } } } \simeq - { \frac { U ^ { \prime } } { r ^ { \prime } } }
$$

$$
\frac { \dot { \rho } } { \rho + p } \approx \frac { \dot { n } } { n } ,
$$

$$
\dot { U } = - { \frac { \Gamma ^ { 2 } } { \rho + p } } { \frac { p ^ { \prime } } { r ^ { \prime } } } - { \frac { m + 4 \pi r ^ { 3 } p } { r ^ { 2 } } }
$$

$$
p = p ( n , \pmb { \rho } )
$$

$\widetilde { \phi } ^ { \prime } = - p ^ { \prime } / ( \rho + p ) , \widetilde { \phi } = 0$ at star's surface (source equation for $\pmb { \mathcal { \tilde { \phi } } }$ ）；

$$
m ^ { \prime } = 4 \pi r ^ { 2 } \rho r ^ { \prime } , \qquad m = 0 \mathrm { ~ a t ~ } a = 0 ,
$$

$$
\boldsymbol { { \Gamma } } = \mathrm { s i g n } ( \boldsymbol { { r } } ^ { \prime } ) ( 1 + U ^ { 2 } - 2 m / r ) ^ { 1 / 2 }
$$

(b) The preceding equations are in a form useful for numericalcalculations.[For particular numerical solutions and for the handling of shocks,see May and White (1966).J For analytic work it is often useful to replace (32.22b) by

$$
n = { T } / ( 4 \pi r ^ { 2 } r ^ { \prime } ) ,
$$

and (32.22d) by

$$
\dot { m } = - 4 \pi r ^ { 2 } p U .
$$

Derive these equations.

(c) Explain why equations $( 3 2 . 2 2 { \bf g } )$ and (32.22d') justify the remarks made in Box 23.1 about localizability of energy.

# ExerciSe 32.8. ANALYTIC SOLUTIONS FOR PRESSURE-FREE COLLAPSE [Tolman (1934b); Datt (1938)]

Show that the general solution to equations (32.22) in the case of zero pressure can be generated as follows.

(a) Specify the mass inside shell a, $m ( a )$ ； by equation (32.22d), with $\pmb { p } = 0$ , it will no1 change with time t.

(b) Assume that allthe dust particles have rest mases $\pmb { \mu }$ that depend upon radius, $\mu ( a )$ ： so

$$
\rho = \mu n .
$$

(c） Calculate $r$ from the equation

$$
T = m ^ { \prime } / \mu ;
$$

it will be independent of $\widetilde { t } .$

(d) Specify an initial distribution of circumference $2 \pi r$ as function of $\pmb { a }$ and solve the dynamic equation

$$
\left( { \frac { \partial r } { \partial { \bar { t } } } } \right) ^ { 2 } - { \frac { 2 m ( a ) } { r } } = \Gamma ^ { 2 } ( a ) - 1
$$

to obtain the subsequent evolution of $r ( \widetilde t , a )$ . Notice that this equation has identically the same form as in Newtonian theory!

(e) Calculate the remaining quantities of interest from the algebraic equations

$$
\begin{array} { c } { { d s ^ { 2 } = - \widetilde { d t ^ { 2 } } + ( r ^ { \prime } d a / { \cal T } ) ^ { 2 } + r ^ { 2 } d \Omega ^ { 2 } , } } \\ { { \ } } \\ { { \rho = \mu n = m ^ { \prime } / ( 4 \pi r ^ { 2 } r ^ { \prime } ) , } } \\ { { \ } } \\ { { \widetilde { \phi } = 0 , ~ U = \partial r / \widetilde { d t } . } } \end{array}
$$

[Note: In this solution,successive “shells” may pass through each other, producing a surface of infinite density as they do $( r ^ { \prime } \longrightarrow 0$ where $m ^ { \prime } \neq 0$ ， since there is no pressure built up to stop shell crossing. When this happens, the coordinate system becomes pathological ${ \bf \Pi } _ { a }$ no longer increases monotonically outward),but spacetime remains well-behaved. The surface of infinite density (l） produces negligible tidal forces on neighboring dust particles; and (2) like the surface layers of $\ S 2 1 . 1 3$ , it is an idealization that gets smeared down to finite density by finite pressure.]

# Exercise 32.9. COLLAPSE WITH UNIFORM DENSITY

Recover the Friedmann-Schwarzschild solution for collapse with uniform density and zero pressure by specifying appropriate forms for $m ( a )$ and $r ( a )$ in the prescription of exercise 32.8.In the interior of the star,give the dust particles nonzero rest masses, $\mu = \mathsf { c o n s t a n t } \neq 0$ ； in the exterior give them zero rest masses, $\mu = 0$ ("imaginary dust particles” in vacuum). Reduce the resulting metric (32.23d) to that of Friedmann inside the star,and to that of Novikov for the Schwarzschild geometry outside the star [equations (31.12)].

# \$32.6． THE FATE OF A MAN WHO FALLS INTO THE SINGULARITY AT $\pmb { r } = \pmb { 0 }$

The-effect of tidal forces on the body of aman falling into the $r = 0$ singularity:

Consider the plight of an experimental astrophysicist who stands on the surface of a freely falling star as it collapses to $R = 0$

As the collapse proceeds toward $R = 0$ ,the various parts of the astrophysicist's body experience different gravitational forces. His feet, which are on the surface of the star, are attracted toward the star's center by an infinitely mounting gravitational force; while his head,which is farther away, is accelerated downward by a somewhat smaller, though ever rising force. The difference between the two accelerations (tidal force) mounts higher and higher as the collapse proceeds, finally becoming infinite as $R$ reaches zero.The astrophysicist's body,which cannot withstand such extreme forces,suffers unlimited stretching between head and foot as $R$ drops to zero.

But this is not all. Simultaneous with this head-to-foot stretching,the astrophysicist is pulled by the gravitational field into regions of spacetime with ever-decreasing circumferential area, $4 \pi r ^ { 2 }$ . In order to accomplish this, tidal gravitational forces must compress the astrophysicist on all sides as they stretch him from head to foot. The circumferential compression is actually more extreme than the longitudinal stretching;so the astrophysicist, in the limit $R \longrightarrow 0$ ， is crushed to zero volume and indefinitely extended length.

The above discussion can be put on a mathematical footing as follows.

There are three stages in the killing of the astrophysicist: (l) the early stage, when his body successfully resists the tidal forces; (2) the intermediate stage,when it is gradually succumbing; and (3） the final stage,when it has been completely overwhelmed.

During the early stage,one can analyze the tidal forces by means of the equation of geodesic deviation, evaluated in the astrophysicist's orthonormal frame $\hat { \omega ^ { \tau } } , \omega \hat { \rho }$ ， $\omega ^ { \hat { \theta } } , \omega ^ { \hat { \phi } }$ (see $\ S 3 1 . 2 )$ . In this frame, the nonvanishing components of the Riemann curvature tensor are given by equations (31.6):

$$
\begin{array} { l l } { { R _ { \hat { \tau } \hat { \rho } \hat { \tau } \hat { \rho } } = - 2 M / r ^ { 3 } , \quad } } & { { R _ { \hat { \tau } \hat { \theta } \hat { \tau } \hat { \theta } } = R _ { \hat { \tau } \hat { \phi } \hat { \tau } \hat { \phi } } = M / r ^ { 3 } , } } \\ { { R _ { \hat { \theta } \hat { \phi } \hat { \theta } \hat { \phi } } = 2 M / r ^ { 3 } , \quad } } & { { R _ { \hat { \rho } \hat { \theta } \hat { \rho } \hat { \theta } } = R _ { \hat { \rho } \hat { \phi } \hat { \rho } \hat { \phi } } = - M / r ^ { 3 } . } } \end{array}
$$

The equation of geodesic deviation says that two freely moving particles, momentarily at rest in the astrophysicist's local inertial frame, and separated by the 3-vector

$$
\pmb { \xi } = \xi ^ { \hat { j } } \pmb { e } _ { \hat { j } } ,
$$

must accelerate apart with a relative acceleration given by

$$
\begin{array} { l } { { { \cal D } ^ { 2 } \xi ^ { \hat { j } } / d \tau ^ { 2 } = - R ^ { \hat { j } } { } _ { \hat { \tau } \hat { k } \hat { \tau } } \xi ^ { \hat { k } } = - R _ { \hat { j } \hat { \tau } \hat { k } \hat { \tau } } \xi ^ { \hat { k } } } } \\ { { \ = - R _ { \hat { \tau } \hat { j } \hat { \tau } \hat { k } } \xi ^ { \hat { k } } . } } \end{array}
$$

Using the components (32.24a) of the curvature tensor,one sees that

$$
\begin{array} { l } { { { \cal D } ^ { 2 } \xi ^ { \hat { \rho } } / d \tau ^ { 2 } = + ( 2 M / r ^ { 3 } ) \xi ^ { \hat { \rho } } , } } \\ { { { \cal D } ^ { 2 } \xi ^ { \hat { \theta } } / d \tau ^ { 2 } = - ( M / r ^ { 3 } ) \xi ^ { \hat { \theta } } , } } \\ { { { \cal D } ^ { 2 } \xi ^ { \hat { \phi } } / d \tau ^ { 2 } = - ( M / r ^ { 3 } ) \xi ^ { \hat { \phi } } . } } \end{array}
$$

To apply these equations to the astrophysicist's body,idealize it (for simplicity) as a homogeneous rectangular box of mass $\mu \approx 1 6 5$ pounds $\approx 7 5 \mathtt { k g } ,$ of length $\iota \approx 7 0$ inches $\approx 1 . 8  { \mathrm { m } }$ in the $\pmb { e } _ { \hat { \pmb { \rho } } }$ direction,and of width and depth $w \approx 1 0$ inches $\approx 0 . 2 \ \mathrm { m }$ in the $\pmb { e } _ { \hat { \theta } }$ and $\pmb { e } _ { \hat { \phi } }$ directions. Then calculate the stresses that must be set up in this idealized body to prevent its particles from moving along diverging (and converging） geodesics.

From the form of equations (32.24), it is evident that the principal directions of the stress will be $\mathbf { \Delta } _ { \mathcal { C } _ { \rho } } , \mathbf { \Delta } _ { \mathcal { C } _ { \theta } }$ and $\pmb { e } _ { \hat { \phi } }$ (i.e., in the $\mathbf { \mathcal { e } } _ { \hat { \rho } } , \mathbf { \mathcal { e } } _ { \hat { \theta } } , \mathbf { \mathcal { e } } _ { \hat { \phi } }$ basis,the stress tensor will be diagonal). The longitudinal component of the stress, at the astrophysicist's center of mass, can be evaluated as follows. A volume element of his body with mass $d \mu$ ， located at a height $\pmb { h }$ above the center of mass (distance $h$ measured along $\pmb { e } _ { \hat { \pmb { \rho } } }$ direction） would accelerate with $a = ( 2 M / r ^ { 3 } ) h$ away from the center of mass, if it were allowed to move freely.To prevent this acceleration, the astrophysicist's muscles must exert a force

$$
d F = a d \mu = ( 2 M / r ^ { 3 } ) h d \mu .
$$

This force contributes to the stress across the horizontal plane $( e _ { \hat { \theta } } \wedge e _ { \hat { \phi } }$ plane) through the center of mass. The total force across that plane is the sum of the forces on all mass elements above_it (which is also equal to the sum of the forces on the mass elements below it):

$$
\begin{array} { r l } & { F = \int _ { ( \mathrm { r e g i o n a b o v e p l a n e } ) } a d \mu = \int _ { 0 } ^ { t / 2 } \biggl ( \frac { 2 M h } { r ^ { 3 } } \biggr ) \biggl ( \frac { \mu } { \ell w ^ { 2 } } \biggr ) ( w ^ { 2 } d h ) } \\ & { \quad = \displaystyle \frac { 1 } { 4 } \frac { \mu M \ell } { r ^ { 3 } } . } \end{array}
$$

The stress is this force divided by the cross-sectional area $w ^ { 2 }$ ，with a minus sign because it is a tension rather than a pressure:

$$
T _ { \hat { \rho } \hat { \rho } } = - \frac { 1 } { 4 } \frac { \mu M \ell } { w ^ { 2 } r ^ { 3 } } \approx - 1 . 1 \times ~ 1 0 ^ { 1 5 } \frac { M / M _ { \odot } } { ( r / 1 ~ \mathrm { k m } ) ^ { 3 } } \frac { \mathrm { d y n e s } } { \mathrm { c m } ^ { 2 } } .
$$

The components of the stress in the $\pmb { e } _ { \hat { \pmb { \theta } } }$ and $\pmb { e } _ { \hat { \phi } }$ directions at the center of mass are, similarly,

$$
T _ { \hat { \theta } \hat { \theta } } = T _ { \hat { \phi } \hat { \phi } } = + \frac { 1 } { 8 } \frac { \mu M } { \downarrow r ^ { 3 } } \approx + 0 . 7 \times 1 0 ^ { 1 3 } \frac { M / M _ { \odot } } { ( r / 1 \mathrm { k m } ) ^ { 3 } } \frac { \mathrm { d y n e s } } { \mathrm { c m } ^ { 2 } } .
$$

(Recall that one atmosphere of presure is $1 . 0 1 \times 1 0 ^ { 6 } ~ \mathrm { d y n e s / c m ^ { 2 } . }$

The human body cannot withstand a tension or pressure of $\gtrsim 1 0 0$ atmospheres $\approx 1 0 ^ { 8 }$ dynes/ $\mathrm { c m ^ { 2 } }$ without breaking.Consequently，an astrophysicist on a freely collapsing star of one solar mass will be killed by tidal forces when the star's radius is $R \sim 2 0 0 ~ \mathrm { k m } \gg 2 M \approx 3 ~ \mathrm { k m } .$

By the time the star is much smaller than its gravitational radius,the baryons of the astrophysicist's body are moving along geodesics: his muscles and bones have completely given way. In this final stage of collapse,the timelike geodesics are curves along which the Schwarzschild“time"-coordinate, $t ,$ ,is almost constant [cf. the narrowing down of the light cones near $r = 0$ in Figure 32.1,a; also equation (31.2) in the limit $r \ll 2 M ]$ . The astrophysicist's feet touch the star's surface at one value of t-say $t = t _ { f }$ -while his head moves along the curve $t = t _ { h } > t _ { f } .$ Consequently, the length of the astrophysicist's body increases according to the formula

$$
\begin{array} { r } { \ell _ { \mathrm { a s t r o p h } } = [ g _ { t t } ( R ) ] ^ { 1 / 2 } [ t _ { h } - t _ { f } ] = [ 2 M / R ] ^ { 1 / 2 } [ t _ { h } - t _ { f } ] } \\ { \propto R ^ { - 1 / 2 } \propto ( \tau _ { \mathrm { c o l l a p s e } } - \tau ) ^ { - 1 / 3 } . \qquad } \end{array}
$$

Here $\tau = [ - \int ^ { R } | g _ { r r } | ^ { 1 / 2 } d r + \mathrm { c o n s t a n t }$ ] is proper time as it would be measured by the astrophysicist if he were still alive,and $\pmb { \tau _ { \mathrm { c o l l a p s e } } }$ is the time at which he hits $r = 0$ The gravitational field also constrains the baryons of the astrophysicist's body to fall along world lines of constant $\pmb \theta$ and $\phi$ during the final stages of collapse. Consequently, his cross-sectional area decreases according to the law

$$
\mathcal { A } _ { \mathrm { a s t r o p h } } = [ g _ { \theta \theta } ( R ) g _ { \phi \phi } ( R ) ] ^ { 1 / 2 } \varDelta \theta \ A \phi \propto R ^ { 2 } \propto ( \tau _ { \mathrm { c o l l a p s e } } - \tau ) ^ { 4 / 3 } .
$$

By combining equations (32.26a,b),one sees that the volume of the astrophysicist's body decreases,during the last few moments of collapse,according to the law

$$
\mathcal { V } _ { \mathrm { a s t r o p h } } = \mathit { \Omega } \mathit { \Omega } \mathit { \Omega } \mathit { \Omega } _ { \mathrm { a s t r o p h } } \mathcal { C } _ { \mathrm { a s t r o p h } } \propto \mathit { R } ^ { 3 / 2 } \propto ( \tau _ { \mathrm { c o l l a p s e } } - \tau ) .
$$

This crushing of matter to infinite density by infinitely large tidal gravitational forces can occur not only on the surface of the collapsing star, but also at any other point along the $r = 0$ singularity outside the surface of the star.Hence,any foolish rocketeer who ventures below the radius $r = 2 M$ of the external gravitational field is doomed to destruction.

For further discussion of spacetime singularities, and of the possibility that quan-tum gravitational effects might force a reconsideration of the singularities predicted by classical gravitation theory,see Chapter 30, $\ S 3 4 . 6$ ,and Chapter 44.

# \$32.7． REALISTIC GRAVITATIONAL COLLAPSE-AN OVERVIEW

Instability, implosion, horizon,and singularity;these are the key stages in the spherical collapse of any star. Instability: The star, having exhausted its nuclear fuel, and having contracted slowly inward, begins to squeeze its pressure-sustaining electrons or photons onto its atomic nuclei; this softens the equation of state, which induces an instability [see, e.g., $\ S 8 1 0 . 1 5$ and 11.4 of Zel'dovich and Novikov (1971)

for details]. Implosion: Within a fraction of a second the instability develops into a full-scale implosion; for realistic density distributions,the stellar core falls rapidly inward on itself, and the outer envelopes trail along behind [see,e.g., the numerical calculations of Colgate and White (1966), Arnett (l966,1967), May and White (1966), and Ivanova, Imshennik,and Nadezhin (l969)). Horizon: In the idealized spherical case,the star's surface falls through its gravitational radius ("horizon”；end of communication with the exterior; point of no return). From the star's vantage point this happens after a finite, short lapse of proper time. But from an external vantage point the star requires infinite time to reach the horizon, though it becomes black exponentially rapidly in the process [e-folding time $\sim M { \sim } 1 0 ^ { - 5 } ( M / M _ { \odot } )$ sec]. The result is a“black hole",whose boundary is the horizon (gravitational radius), and whose interior can never communicate with the exterior. Singularity: From the star's interior vantage point, within a short proper time interval $\Delta \tau \sim M \sim 1 0 ^ { - 5 } ( M / M _ { \odot } )$ sec after passing through the horizon,a singularity is reached (zero radius,infinite density,infinite tidal gravitational forces).

Does this basic picture-instability,implosion, horizon, singularity-have any relevance for real stars? Might complications such as rotation, nonsphericity, magnetic fields,and neutrino fluxes alter the qualitative picture? No, not for small initial perturbations from sphericity.Perturbation theory analyses described in Box 32.2 and exercise 32.1O show that realistic,almost-spherically symmetric collapse, like idealized collapse,is characterized by instability, implosion, horizon;and Penrose (1965b; see $\ S 3 4 . 6 \}$ proves that some type of singularity then follows.

Summary of 1972 knowledge about realistic, nonspherical collapse:

(1） horizon

Highly nonspherical collapse is more poorly understood, of course. Nevertheless, a number of detailed calculations and precise theorems point with some confidence to two conclusions: (l) horizons (probably) form when and only when a mass $M$ gets compacted into a region whose circumference in EVERY direction is $\mathcal { C } \lesssim 4 \pi M$ (Box 32.3);(2) the external gravitational field ofa horizon (black hole),after all the“dust” and gravitational waves have cleared away, is almost certainly the Kerr-Newman generalization of the Schwarzschild geometry (Chapter 33).If so, then the external field is determined uniquely by the mass, charge, and angular momentum that went “down the hole.”(This nearly proved theorem carries the colloquial title“A black hole has no hair.")

(2)black hole

The interior of the horizon, and the endpoint (if any) of the collapse are very poorly understood today. The various possibilities will be reviewed in Chapter 34. That a singularity occurs one can state with much certainty,thanks to theorems of Penrose, Hawking,and Geroch. But whether all, only some, or none of the collapsing matter and fields ultimately encounter the singularity one does not know.

(3） singularity

# Exercise 32.1O. PRICE'S THEOREM FOR A SCALAR FIELD [See Price (1971,1972a),also Thorne (1972), for more details than are presented here.]

# EXERCISES

A collapsing spherical star,with an arbitrary nonspherical “scalar charge distribution,” generates an external scalar field $\pmb { \phi }$ . The vacuum field equation for $\pmb { \phi }$ is $\sqcap \phi = \emptyset _ { : \alpha } { } ^ { \alpha } = 0$ Ignore the back-reaction of the field's stress-energy on the geometry of spacetime.

(continued on page 868)

Box 32.2 COLLAPSE WITH SMALL NON-SPHERICAL PERTURBATIONS [based on_detailed calculations by Richard H. Price (1971,1972a,b)]

# A. Density Perturbations

1.When star begins to collapse, it possesses a small nonspherical“lump” in its density distribution.

2. As collapse proceeds, lump grows larger and larger [instability of collapse against small perturbations-a phenomenon well known in Newtonian theory; see, e.g., Hunter (l967); Lin, Mestel, and Shu (1965).

3. The growing lump radiates gravitational waves.

4. Waves of short wavelength $( \lambda \ll M )$ ，emitted from near horizon $( r - 2 M \lesssim M )$ , partly propagate to infinity and partly get backscattered by the“background” Schwarzschild curvature of spacetime. Backscattered waves propagate into horizon (surface of black hole; gravitational radius) formed by collapsing star.

5. Waves of long wavelength $( \lambda \gg M )$ ，emitted from near horizon $( r - 2 M \leq M )$ ，get fully backscattered by spacetime curvature; they never reach out beyond $r \sim 3 M$ they end up propagating “down the hole.”

6.Is lump on star still there as star plunges through horizon,and does star thereby create a deformed (lumpy) horizon? Yes, according to calculations.

7.But external observers can only learn about existence of “final lump” by examining deformation (quadrupole moment) in final gravitational field.That final deformation in field does not and cannot propagate outward with infinite speed (no instantaneous“action at a distance"). It propagates with speed of light, in form of gravitational waves with near-infinite wavelength (infinite redshift from edge of horizon to any external radius). Deformation in final field, like any other wave of long wavelength, gets fully backscattered by curvature of spacetime at $r \lesssim 3 M ;$ ：it cannot reach external observers. External observers can never learn of existence of final lump. Final external feld is perfectly spherical, lump-free, Schwarzschild geometry！

![](images/52883a460f7cd2a21190b788be6490090362fc8498a7088e5c67b01877c0704d.jpg)

# C. Perturbations in Electromagnetic Field

8. Even in region of backscatter $( 2 M < r \lesssim 3 M )$ ， final external field is lump-free.Backscattered waves, carrying information about existence of final lump,interfere destructively with outgoing waves carrying same information. Result is destruction of all deformation in external field and in horizon!

9.Final black hole is a Schwarzschild black hole!

# B. Perturbations in Angular Momentum

1. When star begins to collapse, it possesses a small,nonzero intrinsic angular momentum ("spin") S.

2. As collapse proceeds, $s$ is conserved (except for a tiny, negligible change due to angular momentum carried off by waves; that change is proportional to square of amplitude of waves, i.e., to square of amplitude of perturbations in star, i.e., to $S ^ { 2 }$

3. Consequently, external field always and everywhere carries imprint of angular momentum $s$ (on imprints,see Chapter l9).There is no need for that imprint to propagate outward from near horizon. Moreover, it could not so propagate even if it tried, because of the conservation law for $s$ (absence of dipole gravitational waves; see $\ S \ S 3 6 . 1$ and 36.10).

1. Star possesses a magnetic field generated by currents in its interior,and an electric field due to an arbitrary internal charge distribution; and electromagnetic radiation is emitted by its hot matter. For simplicity, $s$ is assumed zero.

2.Evolution of external electromagnetic feld is similar to evolution of perturbations in external gravitational field. Distant observer can never learn “final” values of changeable quantities (magnetic dipole moment, electric dipole moment, quadrupole moments,...). Final values try to propagate out from horizon,carried by electromagnetic waves of near-infinite wavelength. But they cannot get out: spacetime curvature reflects them back down the hole； and they superpose destructively with their outgoing counterparts, to produce zero net field.

3.By contrast with all other quantities, which are changeable, the electric monopole moment, (total flux of electric field; equal to $4 \pi$ times total electric charge) is conserved. It never changes from before star collapses, through'the. collapse stage,into the quiescent black-hole stage.

4.Hence, the final external electromagnetic field is a spherically symmetric coulomb field

4.Hence, the final external field is that of an undeformed, slowly rotating black hole:

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } d \Omega ^ { 2 }
$$

$$
- \left( { \frac { 4 S \sin \theta } { r ^ { 2 } } } \right) \left( r \sin \theta d \phi \right) d t .
$$

rotational imprint, see exercise 26.1;also Chapter 19.

Here the polar axis has been oriented along $s$

and the final spacetime geometry is that of Reissner and Nordstrom (charged black hole; see exercises 31.8 and 32.1):

$$
\begin{array} { c } { { d s ^ { 2 } = - \left( 1 - \frac { 2 M } { r } + \frac { Q ^ { 2 } } { r ^ { 2 } } \right) d t ^ { 2 } } } \\ { { \nonumber } } \\ { { \displaystyle + \frac { d r ^ { 2 } } { ( 1 - 2 M / r + Q ^ { 2 } / r ^ { 2 } ) } + r ^ { 2 } d \Omega ^ { 2 } . } } \end{array}
$$

# D. Generalization; Price's Theorem

1. Let the star generate a“zero-rest-mass,integerspin field.”[“Zero rest mass” refers to the quantized particles associated with the classical field. Classically it means the field has a Coulomb-law $( 1 / r )$ fall off at large distances.The spin also is a property of the quantized particles; classically it is most easily visualized as describing the symmetries of a monochromatic plane wave under rotations about the direction of propagation; see $\ S 3 5 . 6$ A scalar feld has spin zero; an electromagnetic field has spin one: Einstein's gravitational field has spin two; .... Of such fields,only gravitational $( s = 2 )$ and electromagnetic $( s = 1 )$ ）are known to exist in the real universe. See, e.g., Dirac (1936),Garding (l945), Bargmann and Wigner (l948),Penrose (l965a), for further discussion.]

2. Let the spin- $\boldsymbol { \mathfrak { s } }$ field be sufficiently weak that its stress-energyperturbsthestar'sexternal, Schwarzschild geometry only very slightly.

3.R'esolve the external field into spherical harmonics (scalar spherical harmonics for $s = 0$ ； vector spherical harmonics for $s = 1$ ; tensor spherical harmonics for $s \geq 2 ^ { . }$ )；and label the spherical harmonics by the usual integer l( $\lambda =$ 0 for monopole; $\ell = 1$ for dipole; $\ell = 2$ for quadrupole; etc.).

4.All multipole felds with $\iota < s$ are conserved during the collapse (theorem from classical radiation theory).A scalar field $( s = 0 )$ ）conserves nothing. The electromagnetic field $( s = 1$ conserves only its monopole parts (electric Coulomb field,and vanishing magnetic Coulomb field).The gravitational field $( s = 2 )$ conserves its monopole part (with imprint equal to mass), and its dipole parts (with imprints measuring the angular momentum,and the standard gravitational dipole moment-which vanishes if coordinate system is centered on star).

5.For $\ell \geq s ,$ and only for $\ell \geq s$ ,radiation is pos-sible (scalar waves can have any multipolarity; electromagnetic waves must be dipole and higher; gravitational waves must be quadrupole and higher; see $\ S 3 6 . 1$ ).

6. Price's theorem states that,as the nearly spherical star collapses to form a black hole,all things that can be radiated (all multipoles $\ell \geq s )$ get radiated completely away-in part “off to infinity”;in part “down the hole”("what is permitted is compulsory"). The final field is characterized completely by its conserved quantities (multipole moments with $\ell < s )$

7.For proof of Price's theorem in the case of a scalar field, see exercise 32.10.

# E. Generalization to Nonclassical Fields

See Hartle (1971,1972) and Teitelboim $( 1 9 7 2 \ b , 0 )$ for neutrino fields；Bekenstein (l972a,b） and Teitelboim (l972a) for pion fields.

# Box 32.3 COLLAPSE IN ONE AND TWO DIMENSIONS

# A. The Question

To produce a black hole (horizon from which nothing can emerge), must one compact matter strongly in all three spatial dimensions,to circumferences $\mathcal { C } \lesssim 4 \pi M$ (quasispherical compaction); or is it sufficient to compact only in one or two dimensions?

# B． The Answer for One Dimension

Consider,as an example readily generalized, the gravitational collapse of a spheroid of dust (zero pressure). Let the spheroid be highly Newtonian $( r > > > 2 M )$ in its initial, momentary state of rest; and let it be slightly flattened (oblate).In Newtonian theory， any homogeneous, nonrotating spheroid of dust remains homogeneous as it collapses;but its deformations grow [see,e.g., Lin, Mestel,and Shu (l965） for details].Hence,the spheroid of interest implodes to form a pancake of infinite density but finite mass per unit surface area.The final kinetic-energy of the dust particles is roughly equal to their final potential energy:

$$
\begin{array} { r l } & { \frac { 1 } { 2 } v ^ { 2 } \sim \frac { M } { ( { \mathcal { C } } / 2 \pi ) } } \\ & { M = \mathrm { m a s s ~ o f ~ s p h e r o i d } , } \\ & { { \mathcal { C } } = \mathrm { c i r c u m f e r e n c e ~ o f ~ f i n a l ~ p a n c i } } \end{array}
$$

Consequently, so long as $\mathcal { C } / 2 \pi \gg 2 M ,$ the collapse velocities remain much smaller than light,and the gravitational energy remains much smaller than the rest mass-energy. This means that for $\mathcal { C } / 2 \pi \gg$ $2 M _ { : }$ the Newtonian analysis is an excellent ap-proximation to general relativity all the way down to the pancake endpoint. Hence,no horizon can form,hardly any gravitational waves are emitted, and the whole story is exceedingly simple and fully Newtonian.However, since the pancake endpoint is not a singularity of spacetime (see the remarks at end of exercise 32.8), the evolution can proceed beyond it;and as $\mathcal { C }$ contracts to $\lesssim 4 \pi M ,$ the evolution will become very complicated and highly relativistic (see the “collapse, pursuit, and plunge scenario” of Figure 24.3).

# C. The Answer for Two Dimensions

Consider, as an example not so readily general-ized, the gravitational collapse of a homogeneous prolate spheroid of dust, initially highly Newtonian.Such a spheroid collapses to form a thin “thread”or “spindle”[see Lin,Mestel, and Shu (1965)].Assume.that the spheroid is still Newtonian when its threadlike state is reached.It then has a length l,a mass per unit length $\lambda = M / \ell \ll 1$ ,and a rapidly contracting equatorial radius $R \ll \ell$ .Subsequently, each segment of the thread collapses radially as though it were part of an infinite cylinder. [Ignore the instability of breakup into “beads";see,e.g.，Hunter (1967), Chandrasekhar (l968).] The radial collapse velocity approaches the speed of light and the gravitational energy approaches the rest mass-erergy only when the thread has become exceedingly thin, $R \lesssim R _ { \mathrm { c r i t } } \sim \ell$ exp $( - 1 / 4 \lambda )$ . At this stage, relativistic deviations from Newtonian collapse come into play. Thorne (l972） and Morgan and Thorne (l973) have analyzed the relativistic effects using an idealized infinite-cylinder model. The results are very different from either the spherical case or the pancake case. The collapsing cylinder emits a large flux of gravitational waves; but they are powerless to halt the collapse. The collapse proceeds inward to a thread-like singularity,without the creation of any horizon (no black hole!).

# D． Objection to the Answer, a Reply, and a Conjecture

One can object that the collapses of both pancake and cylinder can be halted short of their endpoints, especially that of the pancake.As the thickness of

# Box 32.3 (continued)

the pancake approaches zero, the vertical pull of gravity remains finite,but the pressure gradient caused by any finite pressure goes to infinity. Hence, pressure halts the collapse. Subsequently the rim of the pancake contracts toward the relativistic regime ${ \bar { \mathcal { C } } } / 2 \pi \lesssim 2 M .$ In the collapse of a cylinder according to Newtonian theory,with a pressure-density relation $\boldsymbol { p } \propto \boldsymbol { \rho } ^ { \gamma }$ , the gravitational acceleration $a _ { g }$ and pressure-buoyancy acceleration $a _ { p }$ vary as

$$
a _ { g } = - 2 \lambda / R , a _ { p } \sim \rho ^ { - 1 } ( p / R ) \propto \rho ^ { \gamma - 1 } / R .
$$

Hence, for $\gamma > 1$ (the most common realistic case) pressure halts the collapse, but for $\gamma < 1$ it does not.Whether this is true also after the relativistic domain is reached, one does not yet know.

Actually,the ability of pressure to halt the collapse is of no importance to the issue of black holes and horizons.The important thing is that in oblate collapse with final circumference $\mathcal { C } \gg 4 \pi M ,$ and also in prolate collapse with final thread length $\ell \gg 2 M ,$ no horizons are created. This,coupled with the omnipresent horizons in nearly spherical collapse (Box 32.2) suggests the following conjecture [Thorne (l972)): Black holes with horizons form when and only when a mass $M$ gets compacted into a region whose circumference in EVERY direction is ${ \mathcal { C } } \lesssim 4 \pi M .$ (Like most conjectures, this one is sufficiently vague to leave room for many different mathematical formulations!)

(a)Resolve the external field into scalar spherical harmonics, using Schwarzschild coordinates for the external Schwarzschild geometry:

$$
\phi = \sum _ { i } \frac { 1 } { r } \Psi _ { i } ( t , r ) Y _ { t m } ( \theta , \phi ) . \nonumber \ \ l _ { - \ - } \ \ l _ { - } \ .
$$

Show that the vacuum field equation reduces to

$$
- \Psi _ { t , t t } + \Psi _ { i , r ^ { * } r ^ { * } } = \Big ( 1 - \frac { 2 M } { r } \Big ) \Big ( \frac { 2 M } { r ^ { 3 } } + \frac { \ell ( \ell + 1 ) } { r ^ { 2 } } \Big ) \Psi _ { t } ,
$$

where $r ^ { * }$ is the“tortoise coordinate” of $\ S 2 5 . 5$ and Figure 25.4:

$$
r ^ { * } = r + 2 M \ell \mathrm { \ n } ( r / 2 M - 1 ) .
$$

Notice that (32.27b) is a flat-space, one-dimensional wave equation with effective potential

$$
V _ { \mathrm { e f f } } ( r ) = \bigg ( 1 - { \frac { 2 M } { r } } \bigg ) \bigg ( { \frac { 2 M } { r ^ { 3 } } } + { \frac { \ell ( \ell + 1 ) } { r ^ { 2 } } } \bigg ) .
$$

Part of this effective potential $[ \ell ( \ell + 1 ) / r ^ { 2 } ]$ is the“centrifugal barrier,”and part $[ 2 M / r ]$ is due to the curvature of spacetime. Notice the similarity of this effective potential for scalar waves,to the effective potentials for particles and photons moving in the Schwarzschild geometry,

$$
\begin{array} { r } { ( \widetilde { V } ^ { 2 } ) _ { \mathrm { p a r t i c l e s } } = ( 1 - 2 M / r ) ( 1 + \widetilde { L } ^ { 2 } / r ^ { 2 } ) , } \\ { ( B ^ { - 2 } ) _ { \mathrm { p h o t o n s } } = ( 1 - 2 M / r ) r ^ { - 2 } \quad \quad } \end{array}
$$

(Boxes 25.6 and 25.7). The scalar-wave potential. like the photon potential, is positive for all $r > 2 M .$ It rises,from O at $r = 2 M ,$ to a barrier summit; then falls back to O at $r = \infty$

(b) Show that there exist no physically acceptable, static scalar-wave perturbations of a Schwarzschild black hole.[More precisely,show that all static solutions to equation (32.27b) become infinite at either the horizon $( r = 2 M ,$ $r ^ { * } = - \infty .$ orat radial infinity.] This suggests that somehow the black hole formed by collpse must divest itself of the star's external scalar field before it can settle down into a quiescent state.

(c) The general solution to the wave equation (32.27b) can be written in terms of a Fourier transform.For waves that begin near the horizon, propagate outward, and are partially transmitted and partially reflected (“rightward-propagating waves")， show that the general solution is

$$
\Psi _ { t } ( t , r ^ { * } ) = \int _ { - \infty } ^ { \infty } A ( k ) R _ { k } ^ { t } ( r ^ { * } ) e ^ { - \mathrm { i } k t } \ : d k ,
$$

where

$$
\begin{array} { r l r } & { } & { d ^ { 2 } R _ { k } ^ { \ell } / d r ^ { * 2 } = [ - k ^ { 2 } + V _ { \mathrm { e f f } } ( r ) ] R _ { k } ^ { \ell } , \quad } \\ & { } & { R _ { k } ^ { \ell } = e ^ { \mathrm { i } k r ^ { * } } + \Gamma _ { k } ^ { ( R ) } e ^ { - \mathrm { i } k r ^ { * } } \quad \mathrm { a s ~ } r ^ { * } \longrightarrow - \infty , } \\ & { } & { R _ { k } ^ { \ell } = T _ { k } ^ { ( R ) } e ^ { \mathrm { i } k r ^ { * } } \quad \mathrm { a s ~ } r ^ { * } \longrightarrow \infty . \quad } \end{array}
$$

Show that the “reflection and transmission coeffcients for rightward-propagating waves,” ${ \cal T } _ { k } ^ { \left( R \right) }$ and $T _ { \star } ^ { ( R ) }$ ,have the following asymptotic forms for $| \boldsymbol k | \ll 1 / M$ (short wave number; long wavelength):

r@ = -1+ α2Mik, T 1 -1(2Mi)+1 (32 个 个 produces complete reflection and complete no transmission destructive interference in limit $k \longrightarrow 0$ ： in limit $k \longrightarrow 0$ ; see see Box 32.2 for detailed discussion of Box 32.2 ,consequences

where $\pmb { \alpha }$ and $\beta$ are constants of order unity. Give a similar analysis for waves that impinge on a Schwarzschild black hole from outside ("leftward-propagating waves").

(d) Show that,as the star collapses into the horizon,the world line of its surface in $( t , r ^ { \ast } )$ coordinates is

$$
r ^ { * } = R ^ { * } ( t ) \equiv - t - R _ { 0 } ^ { * } \exp { ( - t / 2 M ) } + \mathrm { c o n s t . } ,
$$

where ${ R _ { 0 } } ^ { * }$ is related to the magnitude $^ { a }$ of the surface's 4-acceleration ( ${ \bf \chi } _ { a } > 0$ for outward 4-acceleration） by

$$
{ R _ { 0 } } ^ { * } = ( 8 M / e ) \bigg \{ 1 + 1 6 M a \bigg [ M a + \bigg ( M ^ { 2 } a ^ { 2 } + \frac { 1 } { 8 } \bigg ) ^ { 1 / 2 } \bigg ] \bigg \} .
$$

Thus,the world line of the surface appears to become null near the horizon $\left( t + r ^ { * } \equiv \widetilde { V } = \right.$ constant); of course,this is due to pathology of the coordinate system there. Show,further, that the scalar field on the star's surface ( $\tilde { \bar { V } } =$ constant) must vary as

$$
\Psi _ { t } = Q _ { t 0 } + Q _ { t 1 } e ^ { - \widetilde { U } / 4 M } , \qquad \widetilde { U } \equiv t - r ^ { * } .
$$

when the star is approaching the horizon $( t \longrightarrow \infty , r ^ { * } \longrightarrow - \infty , \widetilde { U } \longrightarrow \infty ) ,$ , in order that the rate of change of $\Psi _ { \mathbf { f } }$ be finite as measured on the star's surface. Notice that $Q _ { 1 0 }$ is the “final value” of the scalar field on the star's surface. It can be regarded as an outgoing wave with zero wave number (infinite wavelength); and, consequently, $i t$ gets completely and destructively refected by the effctive potential [see equation (32.28d): also Box 32.2].Conclusion:All multipoles of the scalar field die out at finite $r ^ { * }$ as $t \longrightarrow \infty$ .(Price's theorem for a scalar field.) For a more detailed analysis,including the rates at which the multipoles die out. see Price (1971,1972a) or Thorne (1972).

Exercise 32.11. NEWMAN-PENROSE “CONSTANTS" [See Press and Bardeen (1971), Bardeen and Press (1972). and Piir (1971) for more details than are presented here.]

Wheeler (1955) showed that Maxwell's equations for an l-pole electromagnetic field residing in the Schwarzschild geometry can be reduced to the wave equation

$$
- \Psi _ { i , t t } + \Psi _ { i , r ^ { * } r ^ { * } } = \bigg ( 1 - \frac { 2 M } { r } \bigg ) \frac { \ell ( \ell + 1 ) } { r ^ { 2 } } \Psi _ { i }
$$

[electromagnetic analogue of (32.27b)]. After this equation has been solved. the components of the electromagnetic field can be obtained by applying certain differential operators to $\Psi _ { \ell } ( t , r ^ { * } ) Y _ { t m } ( \theta , \phi )$

(a) Show that the general solution to the electromagnetic wave equation (32.30) for dipole $( \ell = 1 )$ fields,with outgoing-wave boundary conditions at $r ^ { * } \longrightarrow + \infty$ ,has the form

$$
\Psi _ { \mathrm { i } } \equiv f _ { \mathrm { 0 } } ( \widetilde { \cal U } ) \pm \frac { f _ { \mathrm { 1 } } ( \widetilde { \cal U } ) } { r } \pm \frac { f _ { \mathrm { 2 } } ( \widetilde { \cal U } ) } { r ^ { 2 } } \pm \ _ { \cdot } : : : : ,
$$

where

$\boldsymbol { \widetilde { U } } = \boldsymbol { t } - \boldsymbol { r } ^ { * }$ is “retarded time", and

$$
f _ { 1 } ^ { \prime } = f _ { 0 } , ~ f _ { 2 } ^ { \prime } = 0 , ~ \ldots , ~ f _ { n } ^ { \prime } = - \frac { ( n + 1 ) ( n - 2 ) } { 2 n } f _ { n - 1 } + ~ ( n - 2 ) M f _ { n - 2 } .
$$

When spacetime is flat $M = 0 )$ ，this solution becomes

$$
\Psi _ { 1 } = f _ { 1 } { ' } ( \widetilde { U } ) + f _ { 1 } ( \widetilde { U } ) { , } ^ { \prime } r .
$$

[The $1 / r$ fall-off of the radiation field $f _ { 1 } ^ { \prime } ( \widetilde { U } )$ has been factored out of $\Psi _ { 1 }$ see the scalar-wave function (32.27a).] The terms $f _ { 2 } ( \widetilde { \boldsymbol { U } } ) / / r ^ { 2 } +$ ...，which are absent in flat spacetime,are attributabie to backscatter of the outgoing waves by the curvature of spacetime. They are sometimes called the “tail” of the waves.

(b) Show that the general static dipole field has the form (32.3la) with

$$
\begin{array} { l } { { ( f _ { 0 } ) _ { \mathrm { s t a t i e } } = 0 ; \qquad ( f _ { 1 } ) _ { \mathrm { s t a t i e } } \equiv D = \mathrm { d i p o l e ~ m o m e n t } ; } } \\ { { \qquad ( f _ { 2 } ) _ { \mathrm { s t a t i e } } = \displaystyle { \frac { 3 } { 2 } } M D ; \ldots . . . } } \end{array}
$$

(c) Consider a star (not a black hole!) with a dipole field that is initially static.At time $t = 0$ , let the star suddenly change its dipole moment to a new static value $D ^ { \prime }$ Equations (32.31b) demand that $f _ { 2 }$ be conserved ["Newman-Penrose (1965) constant"].Hence, $f _ { 2 }$ will always exhibit a value, ${ } _ { \mathrm { 2 } } ^ { \mathrm { 3 } } M D ;$ ，corresponding to the old dipole moment; it can never change t0 ${ } _ { 2 } ^ { 3 } M D ^ { \prime }$ .This is a manifestation of the tail of the waves that are generated by the sudden change in dipole moment. To understand this tail effect more clearly,and to discover an important flaw in the above result, evaluate the solution (32.3l) for retarded time $\widetilde { U } > 0$ ， using the assumptions

(1） field has static form (32.32) for $\widetilde { U } < 0$ ，

Put the answer in the form

$$
\Psi _ { 1 } = \frac { D ^ { \prime } } { r } + \frac { \frac { 3 } { 2 } M D } { r ^ { 2 } } + \sum _ { n = 3 } ^ { \infty } \frac { 2 M ( D ^ { \prime } - D ) ( - 1 ) ^ { n + 1 } ( n + 1 ) \widetilde { U } ^ { n - 2 } } { ( 2 r ) ^ { n } } + O \bigg ( \frac { M ^ { 2 } } { r ^ { 3 } } , \frac { M ^ { 2 } \widetilde { U } } { r ^ { 4 } } \bigg ) .
$$

(The terms neglected are small compared to those kept for all $\boldsymbol { \widetilde { U } } / \boldsymbol { r } ,$ so long $\arcsin \gg M .$ ） Evidently, so long as the series converges the Newman-Penrose “constant” (coeficient of $1 / r ^ { 2 } )$ remembers the old $_ D$ value and is conserved, as claimed above. Show,however, that the series diverges for $\widetilde { U } > 2 r$ -i.e.,it diverges inside a sphere that moves outward with asymptotically $\textstyle { \frac { 1 } { 3 } }$ the speed of light.Thus,the Newman-Penrose “constant"is well-defined and conserved only outside the $^ { 6 6 } \frac { 1 } { 3 }$ speed-of-light cone.”

(d) Sum the series in (32.34) to obtain a solution valid even for $\widetilde { U } > 2 r$ ：

$$
\Psi = \frac { D ^ { \prime } } { r } + \frac { 3 } { 2 } \frac { M D ^ { \prime } } { r ^ { 2 } } - \frac { 2 M ( D ^ { \prime } - D ) } { r } \frac { ( \widetilde { U } + 3 r ) } { ( \widetilde { U } + 2 r ) ^ { 2 } } + O \left( \frac { M ^ { 2 } } { r ^ { 3 } } \right)
$$

$$
\qquad \quad = \frac { D ^ { \prime } } { r } + \frac 3 2 \frac { M D ^ { \prime } } { r ^ { 2 } } + O \biggl ( \frac { M } { \widetilde { U } r } , \frac { M ^ { 2 } } { r ^ { 3 } } \biggr ) \qquad \mathrm { f o r } \ \widetilde { U } \geqslant r \geqslant M .
$$

From this result conclude that at fixed $r$ and late times the electromagnetic field becomes asymptotically static, and the Newman-Penrose “constant” assumes the new value ${ } _ { 2 } ^ { 3 } M D ^ { \prime }$ appropriate to the new dipole moment.
