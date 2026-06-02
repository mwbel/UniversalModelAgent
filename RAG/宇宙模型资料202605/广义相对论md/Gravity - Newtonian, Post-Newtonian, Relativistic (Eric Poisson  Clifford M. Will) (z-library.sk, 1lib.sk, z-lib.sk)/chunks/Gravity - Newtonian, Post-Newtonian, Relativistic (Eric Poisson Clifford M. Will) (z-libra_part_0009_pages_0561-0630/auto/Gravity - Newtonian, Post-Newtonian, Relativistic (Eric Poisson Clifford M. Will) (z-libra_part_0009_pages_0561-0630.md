and

$$
\varphi : = [ - \sin \varphi , \cos \varphi , 0 ] ,
$$

which are orthogonal to $N$ and to each other. The vector $\pmb { \vartheta }$ points in the direction of increasing colatitude on the surface of a sphere, while $\varphi$ points in the direction of increasing longitude; they span the transverse subspace orthogonal to $N$ , which is normal to the sphere. The basis gives us the completeness relations

$$
\delta ^ { j k } = N ^ { j } N ^ { k } + \vartheta ^ { j } \vartheta ^ { k } + \varphi ^ { j } \varphi ^ { k } ,
$$

and it follows from Eq. (11.32) that the transverse projector is given by

$$
P ^ { j k } = \vartheta ^ { j } \vartheta ^ { k } + \varphi ^ { j } \varphi ^ { k } .
$$

This can be inserted within Eq. (11.34) to form the TT projector.

The transverse basis formed by $\pmb { \vartheta }$ and $\varphi$ is not unique. For any longitudinal direction $N$ we may rotate the unit vectors by an angle $\psi$ around $N$ and thereby obtain a new basis $( \vartheta ^ { \prime } , \varphi ^ { \prime } )$ . The operation is described by

$$
\vartheta ^ { \prime } = \cos \psi \vartheta + \sin \psi \varphi , \qquad \varphi ^ { \prime } = - \sin \psi \vartheta + \cos \psi \varphi .
$$

The equations (11.39) and (11.40) are invariant under such a rotation.

Any symmetric, transverse, and tracefree tensor $A _ { \mathrm { T T } } ^ { j k }$ can be decomposed in a tensorial basis that is built entirely from the vectors $\pmb { \vartheta }$ and $\varphi$ . Such a tensor has two independent components, which we denote $A _ { + }$ and $A _ { \times }$ and call the polarizations of the tensor $\bar { A } _ { \mathrm { T T } } ^ { j k }$ . We write

$$
A _ { \mathrm { T T } } ^ { j k } = A _ { + } \big ( \vartheta ^ { j } \vartheta ^ { k } - \varphi ^ { j } \varphi ^ { k } \big ) + A _ { \times } \big ( \vartheta ^ { j } \varphi ^ { k } + \varphi ^ { j } \vartheta ^ { k } \big ) ,
$$

so that $A _ { + }$ represents the $\vartheta - \vartheta$ component of the tensor (and also minus the $\varphi { - } \varphi$ component, in order to satisfy the tracefree condition), while $A _ { \times }$ represents its $\vartheta { - } \varphi$ component. It is easy to check that Eq. (11.42) implies

$$
\begin{array} { l } { { \displaystyle A _ { + } = \frac { 1 } { 2 } \big ( \vartheta _ { j } \vartheta _ { k } - \varphi _ { j } \varphi _ { k } \big ) A _ { \mathrm { T T } } ^ { j k } \ : , } } \\ { { \displaystyle A _ { \times } = \frac { 1 } { 2 } \big ( \vartheta _ { j } \varphi _ { k } + \varphi _ { j } \vartheta _ { k } \big ) A _ { \mathrm { T T } } ^ { j k } \ : . } } \end{array}
$$

Because the tensorial operators acting on $A _ { \mathrm { T T } } ^ { j k }$ are already transverse and tracefree, this can also be written as

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { + } = \frac 1 2 \big ( \vartheta _ { j } \vartheta _ { k } - \varphi _ { j } \varphi _ { k } \big ) { \cal A } ^ { j k } \ : , } } \\ { { \displaystyle { \cal A } _ { \times } = \frac 1 2 \big ( \vartheta _ { j } \varphi _ { k } + \varphi _ { j } \vartheta _ { k } \big ) { \cal A } ^ { j k } \ : , } } \end{array}
$$

in which the projection operators are acting on the original tensor $A ^ { j k }$ instead of its TT part $A _ { \mathrm { T T } } ^ { j k }$ .

Under the rotation of Eq. (11.41) the polarizations of $A _ { \mathrm { T T } } ^ { j k }$ transform according to

$$
A _ { + } ^ { \prime } = \cos 2 \psi A _ { + } + \sin 2 \psi A _ { \times } , \qquad A _ { \times } ^ { \prime } = - \sin 2 \psi A _ { + } + \cos 2 \psi A _ { \times } .
$$

It is easy to verify that Eqs. (11.41) and (11.45) ensure that Eqs. (11.42), (11.43), and (11.44) stay invariant under a rotation of the transverse basis.

Equations (11.44), together with the definitions of Eqs. (11.37) and (11.38), provide an efficient way of extracting the polarizations $A _ { + }$ and $A _ { \times }$ from a general tensor $A ^ { j k }$ . The end results are

$$
\begin{array} { l l } { { \displaystyle { \cal A } _ { + } = - \displaystyle \frac { 1 } { 4 } \sin ^ { 2 } \vartheta ( A ^ { x x } + A ^ { y y } ) + \displaystyle \frac { 1 } { 4 } ( 1 + \cos ^ { 2 } \vartheta ) \cos 2 \varphi ( A ^ { x x } - A ^ { y y } ) } } \\ { { \displaystyle ~ + \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \vartheta ) \sin 2 \varphi A ^ { x y } - \sin \vartheta \cos \vartheta \cos \varphi A ^ { x z } - \sin \vartheta \cos \vartheta \sin \varphi A ^ { y z } } } \\ { { \displaystyle ~ + \displaystyle \frac { 1 } { 2 } \sin ^ { 2 } \vartheta A ^ { z z } } , ~ } & { { ( 1 1 . 4 \cos ^ { 2 } \vartheta ) \cos 2 \varphi ( A ^ { x x } - A ^ { y y } ) } } \\ { { \displaystyle { \cal A } _ { \times } = - \displaystyle \frac { 1 } { 2 } \cos \vartheta \sin 2 \varphi ( A ^ { x x } - A ^ { y y } ) + \cos \vartheta \cos 2 \varphi A ^ { x y } + \sin \vartheta \sin \varphi A ^ { x z } } } \\ { { \displaystyle ~ - \sin \vartheta \cos \varphi A ^ { y z } } . } & { { ~ ( 1 1 . 4 \sin ^ { 2 } \vartheta ) \cos 2 \varphi ( A ^ { x x } - A ^ { x y } ) } } \end{array}
$$

With $A _ { + }$ and $A _ { \times }$ known, $A _ { \mathrm { T T } } ^ { j k }$ can be constructed with the help of Eq. (11.42); the complete listing of components is

$$
\begin{array} { r l } & { { \cal A } _ { \mathrm { T T } } ^ { x x } = - \displaystyle \frac { 1 } { 2 } \big [ \sin ^ { 2 } \vartheta - ( 1 + \cos ^ { 2 } \vartheta ) \cos 2 \varphi \big ] { \cal A } _ { + } - \cos \vartheta \sin 2 \varphi { \cal A } _ { \times } , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { x y } = \displaystyle \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \vartheta ) \sin 2 \varphi { \cal A } _ { + } + \cos \vartheta \cos 2 \varphi { \cal A } _ { \times } , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { x z } = - \sin \vartheta \cos \vartheta \cos \varphi { \cal A } _ { + } + \sin \vartheta \sin \varphi { \cal A } _ { \times } , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { y y } = - \displaystyle \frac { 1 } { 2 } \big [ \sin ^ { 2 } \vartheta + ( 1 + \cos ^ { 2 } \vartheta ) \cos 2 \varphi \big ] { \cal A } _ { + } + \cos \vartheta \sin 2 \varphi { \cal A } _ { \times } , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { y z } = - \sin \vartheta \cos \vartheta \sin \varphi { \cal A } _ { + } - \sin \vartheta \cos \varphi { \cal A } _ { \times } , } \\ & { { \cal A } _ { \mathrm { T T } } ^ { z z } = \sin ^ { 2 } \vartheta { \cal A } _ { + } . } \end{array}
$$

For example, when the wave travels in the $y$ -direction, so that $\begin{array} { r } { \vartheta = \varphi = \frac { \pi } { 2 } } \end{array}$ , we have that $\begin{array} { r } { A _ { + } = \frac { 1 } { 2 } ( A ^ { z z } - A ^ { x x } ) } \end{array}$ and $A _ { \times } = A ^ { x z }$ . We also have $A _ { \mathrm { T T } } ^ { z z } = - A _ { \mathrm { T T } } ^ { x x } = A _ { + }$ and $A _ { \mathrm { T T } } ^ { x z } = A _ { \times }$ as the only non-vanishing components of the transverse-tracefree tensor.

# 11.1.8 Distortion of a ring of particles by a gravitational wave

A useful way to visualize the gravitational-wave polarizations is to examine the geodesic deviations that they generate. Consider an initially circular ring of freely moving particles in an inertial frame. A gravitational wave travels in the $z$ -direction past the ring, which lies in the $x - y$ plane. In this case $\vartheta = 0$ , and we can choose $\varphi = 0$ . Equations (11.47) reveal that $A _ { \mathrm { T T } } ^ { x x } = - A _ { \mathrm { T T } } ^ { y y } = A _ { + }$ and $A _ { \mathrm { T T } } ^ { x y } = A _ { \mathrm { T T } } ^ { y x } = A _ { \times }$ , and the other components vanish. The components are conveniently displayed as a matrix,

$$
\begin{array} { r } { A _ { \mathrm { T T } } ^ { j k } = \left( \begin{array} { c c c } { A _ { + } } & { A _ { \times } } & { 0 } \\ { A _ { \times } } & { - A _ { + } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right) . } \end{array}
$$

![](images/19d92c68c0fd2fa2a569d13e3c5b8e9830c2b3064b9a289ea14fc57da4298e58.jpg)  
× polarization

Effect of the $^ +$ and $\times$ gravitational-wave polarizations on a circular ring of freely falling particles. The wave propagates out of the page, and a complete wave cycle is shown from left to right.

The displacement of a given particle from the center of the ring is given by the solution (11.29) to the geodesic deviation equation. We have

$$
\xi ^ { j } ( t ) = \xi ^ { j } ( 0 ) + { \frac { G } { 2 c ^ { 4 } R } } A _ { \mathrm { T T } } ^ { j k } \xi _ { k } ( 0 ) ,
$$

or

$$
\begin{array} { l } { \displaystyle { x ( t ) = x _ { 0 } + \frac { G } { 2 c ^ { 4 } R } \bigg ( A _ { + } x _ { 0 } + A _ { \times } y _ { 0 } \bigg ) , } } \\ { \displaystyle { y ( t ) = y _ { 0 } + \frac { G } { 2 c ^ { 4 } R } \bigg ( A _ { \times } x _ { 0 } - A _ { + } y _ { 0 } \bigg ) , } } \\ { \displaystyle { z ( t ) = z _ { 0 } , } } \end{array}
$$

in terms of the $( x , y , z )$ components of the deviation vector $\pmb { \xi }$ .

Consider now a pure $^ +$ mode. It is simple to show that a circle of particles of unit radius will be distorted into an ellipse described by

$$
\left( \frac { x } { 1 + \eta _ { + } } \right) ^ { 2 } + \left( \frac { y } { 1 - \eta _ { + } } \right) ^ { 2 } = 1 ,
$$

where $\begin{array} { r } { \eta _ { + } ( t ) = \frac { 1 } { 2 } ( G / c ^ { 4 } R ) A _ { + } ( t ) } \end{array}$ is assumed to be small. As $\eta _ { + } ( t )$ varies between its maximum and minimum value, the ellipse transforms between the shapes shown in the upper panel of Fig. 11.1, passing through a circular shape when $\eta _ { + } ( t ) = 0$ . Similarly, for a pure $\times$ mode the circle will be distorted into an ellipse described by

$$
{ \frac { 1 } { 2 } } \left( { \frac { x + y } { 1 + \eta _ { \times } } } \right) ^ { 2 } + { \frac { 1 } { 2 } } \left( { \frac { x - y } { 1 - \eta _ { \times } } } \right) ^ { 2 } = 1 ,
$$

where $\begin{array} { r } { \eta _ { \times } ( t ) = \frac { 1 } { 2 } ( G / c ^ { 4 } R ) A _ { \times } ( t ) } \end{array}$ . This is the same as the first ellipse, except that it is rotated by 45 degrees. In both cases the area of the ellipse is constant to first order in $\eta$ . The ring is unaffected in the $z$ -direction, a reminder that the waves are transverse.

<table><tr><td>Box 11.1</td><td>Why 45 degrees?</td></tr><tr><td></td><td>It is evident from Fig.11.1 that a rotation of 45 degrees takes a + mode into a × mode and vice versa. This is also clear from Eq.(11.45). Alternatively, we can state that the two modes of polarization are related by a rotation ofπ /4 about the direction of propagation.In electromagnetism,the two modes of polarization are related by a rotation ofπ/2 (think ofthe electricfield pointing along the x-axis versus they-axis).Fundamen- tally this is because electrodynamics is associated witha vector field, while gravity isassociated withatensor field.There is a close connection between the rotation angleand the helicity or spin of the particle that one might associate with the waves: it is given byπ /(2S), where S is the spin of the particle in units of h.Thus for photons (S =1), the angle is 90 degrees.For the putative graviton that is often asociated with gravity (although no fuly quantized theory of gravity exists at present), S =2,leading to the 45 degree angle. For a spin-} particle like an electron, the rotation angle is π,as is wellknown from the Dirac equation.</td></tr></table>

# 11.2 The quadrupole formula

In the preceding section we saw that the gravitational-wave field is described by the transverse-tracefree piece of the potentials $h ^ { j k } = G A ^ { j k } / ( c ^ { 4 } R )$ , and we developed methods to extract these radiative pieces from a known tensor $A ^ { j k }$ . In this section we provide an expression for $A ^ { j k }$ and examine some applications of the resulting formalism.

# 11.2.1 Formulation

The tensor $A ^ { j k }$ was, in fact, calculated back in Chapter 7, in the context of a post-Minkowskian approximation to general relativity. The gravitational potentials were computed for the specific case of a matter distribution consisting of a perfect fluid subjected to a slow-motion condition. The results are summarized in Box 7.7. To leading order in a post-Newtonian expansion in powers of $v _ { c } / c$ we have that $A ^ { j k } = 2 \ddot { \mathcal { T } } ^ { j k }$ , where

$$
\begin{array} { l } { \displaystyle \mathcal { T } ^ { j k } ( \tau ) : = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } ( \tau , \pmb { x } ^ { \prime } ) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } } \\ { \displaystyle = \int \rho ^ { * } ( \tau , \pmb { x } ^ { \prime } ) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } + O ( c ^ { - 2 } ) } \end{array}
$$

is the mass quadrupole moment of the matter distribution. The quadrupole formula for the gravitational-wave field is therefore $h _ { \mathrm { T T } } ^ { j k } = ( 2 G / c ^ { 4 } R ) \ddot { \mathcal { T } } _ { \mathrm { T T } } ^ { j k }$ , in which an overdot indicates differentiation with respect to $\tau$ .

We remark that this result was derived after two iterations of the relaxed Einstein equations. Two iterations were required to ensure that the fluid’s equations of motion incorporate gravity at the Newtonian level. But the quadrupole formula appears to be linear in $G$ , and one might be tempted to think that it could have been derived more simply using linearized theory, as presented in Sec. 5.5. One would be wrong, because in linearized theory the fluid does not respond to gravity, and the domain of validity of the result would be severely limited. The fact that the gravitational-wave field has such a “linearized” look is to some degree coincidental; it has been the source of endless confusion in the literature.

Equation (11.53) displays the leading contribution to $\mathcal { T } ^ { j k }$ in a post-Newtonian expansion. In Sec. 11.3 we obtain higher-order corrections to this expression, but in this section we stick to the lowest-order terms. With this in mind, we choose to reserve the notation $\mathcal { T } ^ { j k }$ for the formal, iterated expression for the quadrupole-moment tensor, and define a Newtonian quadrupole moment by

$$
I ^ { j k } ( \tau ) : = \int \rho ^ { * } ( \tau , x ^ { \prime } ) x ^ { \prime j } x ^ { \prime k } d ^ { 3 } x ^ { \prime } .
$$

The lowest-order gravitational-wave field can then be written as

$$
h _ { \mathrm { T T } } ^ { j k } = \frac { 2 G } { c ^ { 4 } R } \ddot { I } _ { \mathrm { T T } } ^ { j k } ,
$$

in terms of the Newtonian moment. Note that we use $\rho ^ { * }$ as our main density variable instead of the proper density $\rho$ ; since these differ by corrections of order $c ^ { - 2 }$ , we may ignore the difference, but $\rho ^ { * }$ is a more convenient density to use in a relativistic context.

Equation (11.55) is easily turned into a robust order-of-magnitude estimate for the gravitational-wave amplitude $h _ { 0 }$ ; this is defined in such a way that a typical component of $\bar { h } _ { \mathrm { T T } } ^ { j k }$ is of the order of $h _ { 0 }$ . We imagine that the waves are produced by a matter distribution of mass $M$ confined to a volume of radius $r _ { c }$ , and that changes in the matter distribution occur over a time scale $t _ { c }$ ; the source’s characteristic velocity is then $v _ { c } \sim r _ { c } / t _ { c }$ . The quadrupolemoment tensor scales as $M r _ { c } ^ { 2 }$ , and $\ddot { I } ^ { j k }$ is of order $M ( r _ { c } / t _ { c } ) ^ { 2 } \sim M v _ { c } ^ { 2 }$ . Then Eq. (11.55) gives

$$
h _ { 0 } \sim { \frac { G M } { c ^ { 2 } R } } ( v _ { c } / c ) ^ { 2 } ,
$$

and we see that strong waves are produced when a large mass $M$ is involved in a rapid process with $v _ { c } \sim c$ . It is important to understand that $v _ { c }$ characterizes only the part of the motion that deviates from spherical symmetry; a spherical matter distribution would have $I ^ { j k } \propto \delta ^ { j k }$ , $I _ { \mathrm { T T } } ^ { j k } = 0$ , and would not emit gravitational waves. (This conclusion is not limited to the quadrupole approximation. It is an exact consequence of general relativity that a spherically-symmetric matter distribution does not emit gravitational waves. This is the statement of Birkhoff ’s theorem, first encountered in Sec. 5.6.2.) To estimate $h _ { 0 }$ numerically we imagine an astrophysical process that involves a mass $M = 1 0 M _ { \odot }$ situated at a distance $R = 1 { \mathrm { M p c } }$ , which corresponds to the approximate size of the local group of galaxies. Under these conditions Eq. (11.56) gives rise to the estimate

$$
h _ { 0 } \sim 4 . 8 \times 1 0 ^ { - 1 9 } \Biggl ( \frac { M } { 1 0 M _ { \odot } } \Biggr ) \Biggl ( \frac { 1 \mathrm { M p c } } { R } \Biggr ) \bigl ( v _ { c } / c \bigr ) ^ { 2 } .
$$

This exercise reveals that even the most violent events in the universe produce tiny gravitational waves.

To obtain a more precise expression for $h _ { \mathrm { T T } } ^ { j k }$ we must evaluate the time derivatives of the quadrupole-moment tensor and carry out the transverse-tracefree projection. The second operation is simple, and relies on the results displayed in Eqs. (11.44) and (11.46). The first operation relies on a knowledge of the fluid dynamics, which is governed by the Newtonian limit of the equations of hydrodynamics, $\rho ^ { * } d v ^ { j } / d t = \rho ^ { * } \partial ^ { j } U - \partial ^ { j } p$ , where $v ^ { j }$ is the fluid’s velocity field, $U$ the Newtonian gravitational potential, and $p$ the pressure. This is the Euler equation, first encountered in its Newtonian form back in Sec. 1.4, and then in relativistic form in Sec. 7.3.2; refer to Eq. (7.58).

The second derivative of the quadrupole-moment tensor is provided by the virial theorem,

$$
\frac { 1 } { 2 } \ddot { I } ^ { j k } = 2 \mathcal { T } ^ { j k } + \Omega ^ { j k } + P \delta ^ { j k } ,
$$

where

$$
\begin{array} { l } { { \displaystyle { \mathcal T } ^ { j k } = \frac 1 2 \int \rho ^ { * } v ^ { j } v ^ { k } d ^ { 3 } x , } } \\ { { \displaystyle \Omega ^ { j k } = - \frac 1 2 G \int \rho ^ { * } \rho ^ { * \prime } \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } d ^ { 3 } x ^ { \prime } d ^ { 3 } x , } } \\ { { P = \displaystyle \int p d ^ { 3 } x . } } \end{array}
$$

The virial theorem is a direct consequence of the Euler equation; it was first derived in the context of Newtonian mechanics back in Sec. 1.4.3; see Eq. (1.88). It is understood that here, $\mathcal { T } ^ { j k } , \Omega ^ { j k }$ , and $P$ are all functions of retarded time $\tau$ ; inside the integrals $\rho ^ { * } , v ^ { j }$ , and $p$ are functions of $\tau$ and $_ x$ , while $\rho ^ { * \prime }$ is a function of $\tau$ and $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ .

When the virial theorem is inserted in Eq. (11.55), $h ^ { j k }$ is seen to contain terms that are both linear and quadratic in $G$ ; the linear terms come from $2 \mathcal { T } ^ { j k }$ and $P \delta ^ { j k }$ , while the quadratic terms come from $\Omega ^ { j k }$ . The virial theorem implies that in general, the contributions from $2 \mathcal { T } ^ { j k }$ , $\Omega ^ { j k }$ , and $P \delta ^ { j k }$ are all comparable to each other, because the sum of terms must vanish on the average. This indicates that the terms of order $G ^ { 2 }$ in $h ^ { j k }$ are comparable to the terms of order $G$ , and that a proper derivation of the quadrupole formula must be based on a second post-Minkowskian approximation to general relativity. A derivation based on the linearized theory (first post-Minkowskian approximation) would omit the $G ^ { 2 }$ terms and give rise to the wrong answer for the gravitational-wave field. As we observed previously, the additional factor of $G$ does not show up when the field is expressed in terms of $\ddot { I } ^ { j k }$ , but in fact it is hidden within the time derivatives, which demand the use of the Newtonian equations of motion.

An exception to this rule occurs when the fluid dynamics is dominated by pressure gradients and gravity is relatively unimportant. In this case $2 \mathcal { T } ^ { j k }$ and $P \delta ^ { j k }$ are both much larger than $\Omega ^ { j k }$ , and the terms of order $G ^ { 2 }$ can be neglected in $h ^ { j k }$ . In this restricted context the quadrupole formula can be reliably derived on the basis of the linearized theory or a single iteration of the relaxed Einstein equations. One obtains Eq. (11.55), but with the important restriction that the source dynamics cannot involve the gravitational field. Such a derivation would be valid for gravitational waves emitted by a source with negligible self-gravity, such as a rotating dumbbell.

In the formulation of the quadrupole formula given here, the fluid system can be of one continuous piece, or it can be broken up into $N$ separated components; this would represent an $N$ -body system of fluid bodies. When the internal structure of each body can be ignored, we may adopt the point-mass description developed in Sec. 9.6 and set

$$
\rho ^ { * } = \sum _ { A } M _ { A } \delta ( { \pmb x } - { \pmb r } _ { A } ) ,
$$

where $M _ { A }$ is the total mass-energy of the body identified by the label $A$ , and $r _ { A }$ is its position vector evaluated at time $\tau$ . In this case the quadrupole moment tensor reduces to

$$
I ^ { j k } = \sum _ { A } M _ { A } r _ { A } ^ { j } r _ { A } ^ { k } ,
$$

and the dynamics of the system is governed by Newton’s equations of motion. These are $\begin{array} { r } { \pmb { a } _ { A } = - \sum _ { B \neq A } G M _ { B } \pmb { n } _ { A B } / r _ { A B } ^ { 2 } } \end{array}$ , where $r _ { A B } : = r _ { A } - r _ { B } , r _ { A B } : = | \pmb { r } _ { A } - \pmb { r } _ { B } |$ , and ${ \pmb n } _ { A B } : =$ $r _ { A B } / r _ { A B }$ . In this case the virial theorem becomes

$$
\frac { 1 } { 2 } \ddot { I } ^ { j k } = - \frac { 1 } { 2 } \sum _ { A } \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } + \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } ,
$$

where $\pmb { v } _ { A } \mathrel { \mathop : } = d \pmb { r } _ { A } / d \tau$ is the velocity vector of body $A$ . This can be obtained by differentiating Eq. (11.61) and involving the equations of motion, or directly from Eq. (11.58) by exploiting the regularization techniques developed in Sec. 9.6.

# Box 11.2

# The quadrupole-formula controversy

In a remarkable pair of papers published in 1916 and 1918, Einstein calculated the gravitational-wave field and radiated energy of a time-dependent source, such as a rotating dumbbell, for which self-gravity is unimportant. He performed this computation in a slow-motion approximation, using the linearized Einstein equations, and obtained the quadrupole formula (11.55). It is perhaps a slight exaggeration to say that it was all downhill from there, at least until 1979.

It didn’t help that Einstein made a calculational error in his 1918 paper, leading to a wrong factor of 2, discovered later by Eddington. Nor did it help that Eddington, concerned about the gauge freedom available in the description of gravitational waves, wondered in 1922 whether aspects of gravitational waves were physically real or purely coordinate artifacts; as he put it, perhaps they “propagate with the speed of thought.” Although Eddington understood that the gauge-invariant modes were physical and believed that gravitational waves did exist, his remark, taken out of context, had the effect of making the entire subject seem dubious.

To make matters worse, in 1936 Einstein and his young colleague Nathan Rosen (of Einstein–Podolsky– Rosen paradox fame) submitted a paper to The Physical Review with the provocative title $ { { } ^ { \prime \prime } } \mathtt { D } 0$ gravitational waves exist?”. They thought they had found an exact solution of the field equations describing a plane gravitational wave, but because the solution had a singularity, it could not be physically valid, and they concluded that gravitational waves could not exist. The Physical Review sent the paper for review, and the report that came back pointed out that the Einstein–Rosen solution in fact described a cylindrical wave, and that the singularity was merely a harmless coordinate singularity associated with the axis. So the solution was perfectly valid, and in fact it supported the existence of gravitational waves. Einstein was so angry that the journal had sent his paper out to be refereed, a practice that was unfamiliar to him, that he withdrew the paper and never published again in that journal. Shortly thereafter, however, Einstein was convinced by another of his assistants, Leopold Infeld (who had been approached by the anonymous referee), that the referee had been perfectly correct. Einstein rewrote the paper with the opposite conclusion and published it under the title $^ { \prime \prime } 0 \mathsf { n }$ gravitational radiation” (but not in The Physical Review). While there has been plenty of speculation as to the identity of the anonymous referee, it wasn’t until 2005 that our friend Daniel Kennefick was allowed access to the records of the journal and revealed conclusively that the referee was the well-known Princeton and Caltech relativist H.P. Robertson (the co-discoverer of the Robertson–Walker metric for cosmology).

This episode did not end the debate over the existence of gravitational waves. Even if one accepts the validity of Einstein’s prediction that a rotating dumbbell will radiate gravitational waves, the argument was made that a binary-star system would not radiate. After all, each body is moving on a geodesic, and is therefore unaccelerated relative to a local freely falling frame. Without acceleration, the argument went, there should be no radiation. Peter Havas was one of the proponents of this possibility.

Beginning in the late 1940s, numerous attempts were made to calculate the “back reaction” forces that would alter the motion of a binary system in response to the radiation of energy and angular momentum (this is the primary subject of Chapter 12). Yet different workers got different answers.

By 1974, while most researchers in the field accepted the reality of gravitational waves and the validity of the quadrupole formula for slowly moving binary systems, a vocal minority remained skeptical. This “quadrupole-formula controversy” came to a head with the September 1974 discovery of the first binary pulsar by Russell Hulse and Joseph Taylor. It was immediately clear that it would be possible to test the quadrupole formula by exploiting the high-precision timing of the pulsar’s radio signals to measure the slow variation in the orbit induced by the loss of orbital energy to radiation.

But in a letter published in the Astrophysical Journal in 1976, Jurgen Ehlers, Arnold Rosenblum, Joshua ¨ Goldberg, and Peter Havas argued that the quadrupole formula could not be justified as a theoretical prediction of general relativity. They presented a laundry list of theoretical problems that they claimed had been swept under the rug by proponents of the quadrupole formula. Among them were these: people assumed energy balance to infer the reaction of the source to the flux of radiation, but there was no proof that this was a valid assumption; no reliable calculation of the equations of motion that included radiation reaction had (in their opinion) ever been carried out; many “derivations” of the quadrupole formula relied on the linearized theory, which was clearly wrong for binary systems; since higher-order corrections had not been calculated, it was impossible to know if the quadrupole formula was even a good approximation; even worse, higher-order terms were known to be rife with divergent integrals.

There was considerable annoyance among holders of the “establishment” viewpoint when this paper appeared, mainly because it was realized that its criticisms had considerable merit. As a result many research groups embarked on a program to return to the fundamentals and to develop approximation schemes for equations of motion and gravitational radiation that would not be subject to the flaws that so disturbed Ehlers et al. Among the noteworthy outcomes of this major effort was the fully developed post-Minkowskian formalism that forms the heart of this book. Toward the end of his life, Jurgen Ehlers, one of the great relativists of ¨ his time, admitted to one of us (after some prodding, to be sure, and only up to a point!) that the justification of the quadrupole formula was in much better shape than it was in 1976.

Experimentally, the situation was not at all controversial. By 1979, Taylor and his colleagues had measured the damping of the binary pulsar’s orbit, in agreement with the quadrupole formula to about 10 percent; by 2005, the agreement was at the 0.2 percent level. The formula has also been beautifully confirmed in a number of other binary-pulsar systems.

# 11.2.2 Application: Binary system

As a first application of the quadrupole formula, we examine the gravitational waves emitted by a binary system of orbiting bodies. We rely on the Newtonian description of the orbital motion reviewed in Sec. 3.2.

# Orbital motion and gravitational-wave field

The position of the first body, of mass $m _ { 1 }$ , is $r _ { 1 } ( t )$ relative to the system’s barycenter, and its velocity is ${ \pmb v } _ { 1 } ( t )$ ; similarly, the position of the second body, of mass $m _ { 2 }$ , is $r _ { 2 } ( t )$ and its velocity is ${ \pmb v } _ { 2 } ( t )$ . In terms of the separation vector $r : = r _ { 1 2 } = r _ { 1 } - r _ { 2 }$ we have that

$$
r _ { 1 } = \frac { m _ { 2 } } { m } r , \qquad r _ { 2 } = - \frac { m _ { 1 } } { m } r ,
$$

where $m : = m _ { 1 } + m _ { 2 }$ is the total mass of the system. We also have

$$
\pmb { v } _ { 1 } = \frac { m _ { 2 } } { m } \pmb { v } , \qquad \pmb { v } _ { 2 } = - \frac { m _ { 1 } } { m } \pmb { v } ,
$$

where $\pmb { v } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ is the relative velocity vector. For later purposes we introduce the notations

$$
r : = | r | , \qquad n : = r / r ,
$$

together with

$$
\eta : = \frac { m _ { 1 } m _ { 2 } } { ( m _ { 1 } + m _ { 2 } ) ^ { 2 } } ;
$$

this quantity is known as the symmetric mass ratio of the binary system.

Making the substitutions in the quadrupole-moment tensor of Eq. (11.61) reveals tha $I ^ { j k } = \eta m r ^ { j } r ^ { k }$ , and Eq. (11.62) becomes $\begin{array} { r } { \frac { 1 } { 2 } \ddot { I } ^ { j k } = \eta m [ v ^ { j } v ^ { k } - ( G m / r ) n ^ { j } n ^ { k } ] } \end{array}$ . We then obtain

$$
h ^ { j k } = { \frac { 4 G \eta m } { c ^ { 4 } R } } \bigg ( v ^ { j } v ^ { k } - { \frac { G m } { r } } n ^ { j } n ^ { k } \bigg )
$$

for the gravitational potentials created by a binary system. To proceed further we need expressions for $r$ and $\pmb { v }$ .

To describe the orbital motion we introduce first an “orbit-adapted” coordinate system $( x , y , z )$ that possesses the following properties. First, the origin of the coordinates coincides with the system’s barycenter. Second, the orbital plane coincides with the $x - y$ plane, and the $z$ -axis points in the direction of the angular-momentum vector. And third, the $x$ -axis is aligned with the orbit’s major axis, while the $y$ -axis is aligned with the minor axis. The relative orbit is described by the Keplerian equations

$$
r = \frac { p } { 1 + e \cos \phi } , \qquad \dot { \phi } = \sqrt { \frac { G m } { p ^ { 3 } } } ( 1 + e \cos \phi ) ^ { 2 } ,
$$

in which $\phi$ is the angle from the $x$ -axis (also known as the true anomaly). In addition, $p$ is the orbit’s semi-latus rectum, and $e$ is the eccentricity; these orbital elements are constants

of the motion that can be related to the system’s total energy and angular momentum. In the orbit-adapted coordinates $( x , y , z )$ we have that the unit vectors

$$
\pmb { n } = [ \cos \phi , \sin \phi , 0 ] , \qquad \pmb { \lambda } = [ - \sin \phi , \cos \phi , 0 ] ,
$$

form a basis in the orbital plane. In terms of these

$$
\begin{array} { r } { r = r \pmb { n } , \qquad \pmb { v } = \dot { r } \pmb { n } + r \dot { \phi } \pmb { \lambda } , } \end{array}
$$

and the description of the motion is complete. Taking into account Eqs. (11.68) and (11.70), Eq. (11.67) becomes

$$
\begin{array} { l } { { h ^ { j k } = \displaystyle \frac { 4 \eta } { c ^ { 4 } R } \displaystyle \frac { ( G m ) ^ { 2 } } { p } \biggl [ - ( 1 + e \cos \phi - e ^ { 2 } \sin ^ { 2 } \phi ) n ^ { j } n ^ { k } } } \\ { { \qquad + e \sin \phi ( 1 + e \cos \phi ) \bigl ( n ^ { j } \lambda ^ { k } + \lambda ^ { j } n ^ { k } \bigr ) + ( 1 + e \cos \phi ) ^ { 2 } \lambda ^ { j } \lambda ^ { k } \biggr ] . } } \end{array}
$$

The components of $h ^ { j k }$ in the orbit-adapted frame can then be obtained with the help of Eq. (11.69).

# Polarizations

In order to construct the gravitational-wave polarizations $h _ { + }$ and $h _ { \times }$ , it is helpful to introduce, in addition to the original system $( x , y , z )$ , a “detector-adapted” coordinate system $( X , Y , Z )$ that possesses the following properties. First, the origin of the coordinates coincides with the origin of the system $( x , y , z )$ . Second, the $Z$ -axis points in the direction of the gravitational-wave detector, at which the polarizations are being measured. And third, the $X – Y$ plane is orthogonal to the $Z$ -axis and coincides with the plane of the sky from the detector’s point of view, and the $X$ -axis is aligned with the line of nodes, the line at which the orbital plane cuts the reference plane; by convention the $X$ -axis points toward the ascending node, the point at which the orbit cuts the plane from below. The construction was detailed in Sec. 3.2, and we recall that in the original $( x , y , z )$ coordinates, the new coordinate directions are described by

$$
\begin{array} { r l } & { \pmb { e } _ { X } = [ \cos \omega , - \sin \omega , 0 ] , } \\ & { \pmb { e } _ { Y } = [ \cos \iota \sin \omega , \cos \iota \cos \omega , - \sin \iota ] , } \\ & { \pmb { e } _ { Z } = [ \sin \iota \sin \omega , \sin \iota \cos \omega , \cos \iota ] = N . } \end{array}
$$

When viewed in the detector-adapted frame $( X , Y , Z )$ , the inclination angle $\iota$ measures the inclination of the orbital plane with respect to the $X – Y$ plane, while the longitude of pericenter $\omega$ is the angle between the pericenter and the line of nodes, as measured in the orbital plane. A third angle, the longitude of ascending node $\Omega$ , was also introduced back in Sec. 3.2, but it is not needed here; we have set $\Omega = 0$ by convention. The vectors $\pmb { n }$ and $\gimel$ are given by

$$
\pmb { n } = \left[ \cos ( \omega + \phi ) , \cos \iota \sin ( \omega + \phi ) , \sin \iota \sin ( \omega + \phi ) \right]
$$

and

$$
\lambda = \left[ - \sin ( \omega + \phi ) , \cos \iota \cos ( \omega + \phi ) , \sin \iota \cos ( \omega + \phi ) \right]
$$

when expressed in the detector-adapted coordinates $( X , Y , Z )$ .

Because the gravitational waves propagate from the binary system to the detector along the $Z$ -axis, we may adopt $e _ { X }$ and $e _ { Y }$ as a vectorial basis in the transverse subspace. And having made this choice, the polarizations $h _ { + }$ and $h _ { \times }$ may be computed according to Eq. (11.44); we have that

$$
\begin{array} { r l } & { h _ { + } = \displaystyle \frac { 1 } { 2 } \big ( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \big ) h _ { j k } , } \\ & { h _ { \times } = \displaystyle \frac { 1 } { 2 } \big ( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \big ) h _ { j k } . } \end{array}
$$

Note that this choice of transverse basis differs only in notation from the description given back in Eqs. (11.36), (11.37), and (11.38). In the old notation we have that $N = e _ { Z } , \vartheta = e _ { Y }$ , and $\pmb { \varphi } = - \pmb { e } _ { X }$ ; the old angles are related to the new ones by $\vartheta = \iota$ and $\varphi = { \frac { \pi } { 2 } } - \omega$ .

Inserting Eqs. (11.71), (11.73), (11.74) within Eq. (11.75) reveals that in the selected transverse basis, the gravitational-wave polarizations are given by

$$
h _ { + } = h _ { 0 } H _ { + } , h _ { \times } = h _ { 0 } H _ { \times } ,
$$

where

$$
h _ { 0 } = \frac { 2 \eta } { c ^ { 4 } R } \frac { ( G m ) ^ { 2 } } { p }
$$

is the gravitational-wave amplitude, and

$$
\begin{array} { l } { { H _ { + } = - ( 1 + \cos ^ { 2 } \iota ) \biggl [ \cos ( 2 \phi + 2 \omega ) + \displaystyle \frac { 5 } { 4 } e \cos ( \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \cos ( 3 \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \cos ( 3 \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \cos ( 3 \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \cos ( 2 \phi + 2 \omega ) + } } \\ { { + \displaystyle \frac { 1 } { 2 } e ^ { 2 } \cos 2 \omega \biggr ] + \displaystyle \frac { 1 } { 2 } e \sin ^ { 2 } \iota \bigl ( \cos \phi + e \bigr ) , } } \\ { { H _ { \times } = - 2 \cos \iota \biggl [ \sin ( 2 \phi + 2 \omega ) + \displaystyle \frac { 5 } { 4 } e \sin ( \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \sin ( 3 \phi + 2 \omega ) + \displaystyle \frac { 1 } { 4 } e \sin ( 2 \phi + 2 \omega ) + } } \\ { { + \displaystyle \frac { 1 } { 2 } e ^ { 2 } \sin 2 \omega \biggr ] } } \end{array}
$$

are scale-free polarizations. Plots of $H _ { + }$ and $H _ { \times }$ are displayed in Fig. 11.2.

# Circular motion

When $e = 0$ the orbit is circular, and $\phi$ increases linearly with time, at a uniform rate equal to $\Omega : = \sqrt { G m / p ^ { 3 } }$ . In this case the polarizations simplify to

$$
H _ { + } = - ( 1 + \cos ^ { 2 } \iota ) \cos 2 ( \Omega \tau + \omega ) , \qquad H _ { \times } = - 2 \cos \iota \sin 2 ( \Omega \tau + \omega ) ,
$$

where $\tau : = t - R / c$ is retarded time. We see that the waves oscillate at twice the orbital frequency; this doubling of frequency is a consequence of the quadrupolar nature of the wave.

![](images/9b9f1557c1c9a7befccad2f68a13cf5d23bc8b64711823aaa3a38cbec595d621.jpg)

The polarizations $H _ { + }$ and $H _ { \times }$ as functions of retarded time $\tau$ , in units of the orbital period P. The curves were constructed from Eqs. (11.78), and $\phi$ is related to $\tau$ by integrating Eq. (11.68), which was done numerically. The curves are displayed for an eccentricity $e = 0 . 7$ , an inclination angle $\iota = 3 0 ^ { \circ }$ , and a longitude of pericenter $\omega = 4 5 ^ { \circ }$ . We see that most of the emission takes place near the pericenter, where the orbit is smallest and the motion fastest.

# Numerical estimate

The gravitational-wave amplitude of Eq. (11.77) can also be expressed in terms of the so-called chirp mass

$$
\mathcal { M } : = \eta ^ { 3 / 5 } m = \left( \frac { m _ { 1 } ^ { 3 } m _ { 2 } ^ { 3 } } { m } \right) ^ { 1 / 5 }
$$

and the orbital period

$$
P : = 2 \pi \sqrt { \frac { a ^ { 3 } } { G m } } ,
$$

where $a : = p / ( 1 - e ^ { 2 } )$ is the orbit’s semi-major axis. The expression is

$$
h _ { 0 } = \frac { 2 } { c ^ { 4 } R } ( G \mathcal { M } ) ^ { 5 / 3 } \bigg ( \frac { 2 \pi } { P } \bigg ) ^ { 2 / 3 } \frac { 1 } { 1 - e ^ { 2 } } .
$$

We evaluate this for a binary system of black holes on a very tight orbit, moments before they are about to plunge toward each other and merge into a single, final black hole. We take $m _ { 1 } = 2 5 M _ { \odot }$ and $m _ { 2 } = 2 2 M _ { \odot }$ , so that $\mathcal { M }$ is approximately equal to $2 0 M _ { \odot }$ . We imagine that the orbital period is of the order of $1 0 \mathrm { m s }$ , and that the binary is situated at a distance $R = 1 0 0 \mathrm { M p c }$ , sufficiently far that the probability of occurrence of such an event is reasonable. These numbers give rise to the estimate

$$
h _ { 0 } = \frac { 3 . 0 \times 1 0 ^ { - 2 1 } } { 1 - e ^ { 2 } } \bigg ( \frac { \mathcal { M } } { 2 0 M _ { \odot } } \bigg ) ^ { 5 / 3 } \bigg ( \frac { 1 0 \mathrm { m s } } { P } \bigg ) ^ { 2 / 3 } \bigg ( \frac { 1 0 0 \mathrm { M p c } } { R } \bigg ) ,
$$

and this indicates that gravitational waves from realistic astrophysical events are exceedingly weak. They are not, however, impossible to detect, and the search for such signals is on.

# 11.2.3 Application: Rotating neutron star

As a second application of the quadrupole formula we calculate the gravitational waves emitted by a deformed body that rotates around one of its principal axes. We think of this body as a rotating neutron star, but the calculation applies to any type of rigid body, irrespective of its composition and internal structure.

# General description

The simplest description of the body is given in a “body-adapted” frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ that co-rotates with the body, and in which the quadrupole moment tensor $I ^ { a ^ { \prime } b ^ { \prime } }$ is diagonal. The coordinates are directed along the body’s principal axes, and we assume that $I ^ { a ^ { \prime } b ^ { \prime } }$ does not depend upon time $t$ . We assume also that the body is rotating uniformly around the $z ^ { \prime }$ -axis, with an angular velocity $\Omega$ . The transformation to the non-rotating frame $( x , y , z )$ is given by

$$
\begin{array} { r l } & { x = x ^ { \prime } \cos \Omega t - y ^ { \prime } \sin \Omega t , } \\ & { y = x ^ { \prime } \sin \Omega t + y ^ { \prime } \cos \Omega t , } \\ & { z = z ^ { \prime } . } \end{array}
$$

The components of the quadrupole-moment tensor in the non-rotating frame are given by

$$
I ^ { j k } = \frac { \partial x ^ { j } } { \partial x ^ { a ^ { \prime } } } \frac { \partial x ^ { k } } { \partial x ^ { b ^ { \prime } } } I ^ { a ^ { \prime } b ^ { \prime } } ,
$$

and the transformation implies that $I ^ { j k }$ , unlike $I ^ { a ^ { \prime } b ^ { \prime } }$ , depends on time.

It is customary to encode the three independent components of $I ^ { a ^ { \prime } b ^ { \prime } }$ into the principal moments of inertia

$$
\begin{array} { l } { I _ { 1 } : = \displaystyle { \int \rho ( \pmb { x } ^ { \prime } ) \big ( y ^ { \prime 2 } + z ^ { \prime 2 } \big ) d ^ { 3 } \pmb { x } ^ { \prime } } = I ^ { y ^ { \prime } y ^ { \prime } } + I ^ { z ^ { \prime } z ^ { \prime } } , } \\ { I _ { 2 } : = \displaystyle { \int \rho ( \pmb { x } ^ { \prime } ) \big ( x ^ { \prime 2 } + z ^ { \prime 2 } \big ) d ^ { 3 } \pmb { x } ^ { \prime } } = I ^ { x ^ { \prime } x ^ { \prime } } + I ^ { z ^ { \prime } z ^ { \prime } } , } \\ { I _ { 3 } : = \displaystyle { \int \rho ( \pmb { x } ^ { \prime } ) \big ( x ^ { \prime 2 } + y ^ { \prime 2 } \big ) d ^ { 3 } \pmb { x } ^ { \prime } } = I ^ { x ^ { \prime } x ^ { \prime } } + I ^ { y ^ { \prime } y ^ { \prime } } . } \end{array}
$$

A body with $I _ { 1 } = I _ { 2 } = I _ { 3 }$ is spherically symmetric, and such a body would not emit gravitational waves. A body with $I _ { 1 } = I _ { 2 } \ne I _ { 3 }$ is symmetric about the axis of rotation, and such a body also would not emit gravitational waves. To produce waves the body must be sufficiently deformed, and a convenient measure of the deformation is the ellipticity parameter

$$
\varepsilon : = \frac { I _ { 1 } - I _ { 2 } } { I _ { 3 } } .
$$

As we shall see, the gravitational-wave field is proportional to $( I _ { 1 } - I _ { 2 } ) = \varepsilon I _ { 3 }$ .

The components of the quadrupole-moment tensor in the co-rotating frame are $I ^ { x ^ { \prime } x ^ { \prime } } =$ $\begin{array} { r } { \frac 1 2 ( I _ { 2 } + I _ { 3 } - I _ { 1 } ) , I ^ { y ^ { \prime } y ^ { \prime } } = \frac 1 2 ( I _ { 3 } + I _ { 1 } - I _ { 2 } ) } \end{array}$ , and $I ^ { z ^ { \prime } z ^ { \prime } } = { \scriptstyle \frac { 1 } { 2 } } ( I _ { 1 } + I _ { 2 } - I _ { 3 } )$ . As a consequence of Eq. (11.85), we find that they are given by

$$
\begin{array} { l } { { I ^ { x x } = \displaystyle \frac { 1 } { 2 } I _ { 3 } - \frac { 1 } { 2 } \big ( I _ { 1 } - I _ { 2 } \big ) \cos { 2 \Omega t } , } } \\ { { { } } } \\ { { I ^ { x y } = - \displaystyle \frac { 1 } { 2 } \big ( I _ { 1 } - I _ { 2 } \big ) \sin { 2 \Omega t } , } } \\ { { { } } } \\ { { I ^ { y y } = \displaystyle \frac { 1 } { 2 } I _ { 3 } + \displaystyle \frac { 1 } { 2 } \big ( I _ { 1 } - I _ { 2 } \big ) \cos { 2 \Omega t } , } } \\ { { { } } } \\ { { I ^ { z z } = \displaystyle \frac { 1 } { 2 } \big ( I _ { 1 } + I _ { 2 } - I _ { 3 } \big ) , } } \end{array}
$$

in the non-rotating frame; the components $I ^ { x z }$ and $I ^ { y z }$ vanish. The non-vanishing components of $\ddot { I } ^ { j k }$ are

$$
\begin{array} { l } { { \ddot { I } ^ { x x } = 2 \varepsilon I _ { 3 } \Omega ^ { 2 } \cos 2 \Omega t , } } \\ { { \ddot { I } ^ { x y } = 2 \varepsilon I _ { 3 } \Omega ^ { 2 } \sin 2 \Omega t , } } \\ { { \ddot { I } ^ { y y } = - 2 \varepsilon I _ { 3 } \Omega ^ { 2 } \cos 2 \Omega t . } } \end{array}
$$

These expressions are ready to be inserted within Eq. (11.55) to obtain the gravitationalwave field $h _ { \mathrm { T T } } ^ { j k }$ .

To extract the polarizations $h _ { + }$ and $h _ { \times }$ we adopt the same conventions as in Sec. 11.2.2. We specify the direction of the gravitational-wave detector in the non-rotating frame $( x , y , z )$ by the polar angles $( \iota , \omega )$ , and use the vectors $e _ { X }$ and $e _ { Y }$ of Eqs. (11.72) as a basis in the transverse subspace. In this case, $\iota$ is the angle between the body’s rotation axis and the direction to the detector, and $\omega$ is the angle, at $t = 0$ , between the intersection of the body’s equatorial plane with the plane of the sky and the direction of the body’s long axis. The polarizations are defined as in Eqs. (11.75), and a quick calculation returns the expressions

$$
h _ { + } = \frac { 1 } { 2 } ( 1 + \cos ^ { 2 } \iota ) h _ { 0 } \cos 2 ( \Omega \tau + \omega ) , \qquad h _ { \times } = \cos \iota h _ { 0 } \sin 2 ( \Omega \tau + \omega ) ,
$$

where $\tau : = t - R / c$ is retarded time, and

$$
h _ { 0 } = \frac { 4 G } { c ^ { 4 } R } \varepsilon I _ { 3 } \Omega ^ { 2 }
$$

is the gravitational-wave amplitude.

# Mountain on a spherical star

A simple model of a deformed neutron star features a mountain on the surface of an otherwise spherical body. The body has a mass $M$ and radius $a$ , and for simplicity we take its density to be uniform. The mountain has a mass $m \ll M$ and is situated on the surface at a position determined by the polar angles $( \theta , \phi )$ in the body-adapted frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ ; we model it as a point mass with a mass density $\rho = m \delta ( { \pmb x } ^ { \prime } - { \pmb \xi } )$ , with $\boldsymbol { \xi } : =$ $[ a \sin \theta \cos \phi , a \sin \theta \sin \phi , a \cos \theta ]$ giving the position of the mountain in the co-rotating frame.

It is easy to calculate that the body’s contribution to the moments of inertia is given by

$$
I _ { 1 } ^ { \mathrm { b o d y } } = I _ { 2 } ^ { \mathrm { b o d y } } = I _ { 3 } ^ { \mathrm { b o d y } } = { \frac { 2 } { 5 } } M a ^ { 2 } .
$$

We see that as expected, the body makes no contribution to the ellipticity $\varepsilon$ . The mountain, on the other hand, gives rise to

$$
I _ { 1 } ^ { \mathrm { m o u n t a i n } } - I _ { 2 } ^ { \mathrm { m o u n t a i n } } = - m a ^ { 2 } \sin ^ { 2 } \theta \cos 2 \phi ,
$$

as well as a contribution to $I _ { 3 }$ that is smaller than $I _ { 3 } ^ { \mathrm { b o d y } }$ by a factor of order $m / M \ll 1$ . Neglecting this, we find that the model produces

$$
\varepsilon = - \frac { 5 } { 2 } \frac { m } { M } \sin ^ { 2 } \theta \cos 2 \phi , \quad \quad I _ { 3 } = \frac { 2 } { 5 } M a ^ { 2 } .
$$

These expressions can then be inserted within Eq. (11.91) to calculate the gravitational-wave amplitude.

# Ellipsoid of uniform density

Another model of a deformed neutron star puts it in the shape of an ellipsoid of principal axes $a , b$ , and $c$ . The surface is thus described by the equation

$$
{ \frac { x ^ { \prime 2 } } { a ^ { 2 } } } + { \frac { y ^ { \prime 2 } } { b ^ { 2 } } } + { \frac { z ^ { \prime 2 } } { c ^ { 2 } } } = 1 ,
$$

and we take the body to have a uniform mass density $\rho$ . To carry out the integrations over the star’s interior, it is useful to adopt the ellipsoidal coordinates $( r , \theta , \phi )$ which are related to the original Cartesian coordinates by $x ^ { \prime } = a r \sin \theta \cos \phi , y ^ { \prime } = b r \sin \theta \sin \phi$ , and $z ^ { \prime } = c r \cos \theta$ . The radial coordinate $r$ is dimensionless and ranges from 0 to 1; the polar angles $( \theta , \phi )$ have their usual ranges. The volume element is $d ^ { 3 } x ^ { \prime } = a b c r ^ { 2 } \sin \theta$ drdθdφ in the ellipsoidal coordinates.

The mass of the body is given by $M = ( 4 \pi / 3 ) \rho a b c$ , and a straightforward calculation reveals that the moments of inertia are

$$
\begin{array} { l } { I _ { 1 } = \displaystyle \frac { 1 } { 5 } M ( b ^ { 2 } + c ^ { 2 } ) , } \\ { I _ { 2 } = \displaystyle \frac { 1 } { 5 } M ( a ^ { 2 } + c ^ { 2 } ) , } \\ { I _ { 3 } = \displaystyle \frac { 1 } { 5 } M ( a ^ { 2 } + b ^ { 2 } ) . } \end{array}
$$

This produces an ellipticity given by

$$
\varepsilon = { \frac { b ^ { 2 } - a ^ { 2 } } { b ^ { 2 } + a ^ { 2 } } } .
$$

These expressions can be inserted within Eq. (11.91) to obtain the gravitational-wave amplitude.

# Realistic neutron stars

The degree of deformation of a realistic neutron star is largely unknown, as are the exact mechanisms that would be involved in supporting a long-lived ellipticity $\varepsilon$ . The most popular models feature either a genuine mountain that might reach deep below the crust, a deformation driven and sustained by accretion of matter from a companion, or a deformation created by a large toroidal magnetic field. These models suggest that $\varepsilon < 1 0 ^ { - 6 }$ for conventional models of neutron stars (which involve a solid crust resting on a liquid core), but larger values might be possible for more exotic objects such as quark stars.

A typical neutron star has a mass $M = 1 . 4 M _ { \odot }$ and radius $a = 1 2 { \mathrm { k m } }$ , and this gives rise to a moment of inertia of the order of $\begin{array} { r } { I _ { 3 } = \frac { 2 } { 5 } M a ^ { 2 } = 1 . 6 \times 1 0 ^ { 3 8 } \mathrm { k g } \mathrm { m } ^ { 2 } } \end{array}$ . A fast pulsar rotates with a period $P = 1 0 ~ \mathrm { m s }$ and might be situated at a distance $R = 1$ kpc. Using $\varepsilon = 1 0 ^ { - 6 }$ as a typical value for the ellipticity, Eq. (11.91) gives rise to the estimate

$$
h _ { 0 } \simeq 6 . 8 \times 1 0 ^ { - 2 5 } \Biggl ( \frac { \varepsilon } { 1 0 ^ { - 6 } } \Biggr ) \Biggl ( \frac { I _ { 3 } } { 1 . 6 \times 1 0 ^ { 3 8 } \mathrm { k g } \mathrm { m } ^ { 2 } } \Biggr ) \Biggl ( \frac { 1 0 \mathrm { m s } } { P } \Biggr ) ^ { 2 } \Biggl ( \frac { 1 \mathrm { k p c } } { R } \Biggr ) .
$$

Gravitational waves produced by rotating neutron stars are exceedingly small, but coherent integration of a signal of known frequency over a very long time builds up a signal-tonoise ratio that may exceed the detection threshold of a gravitational-wave detector. (The frequency can be measured in radio waves if the rotating neutron star is a known pulsar.) The search is on!

# 11.2.4 Application: Tidally deformed star

As a third and final application of the quadrupole formula we calculate the gravitational waves emitted during a tidal interaction between a fluid body and a nearby object. For concreteness and simplicity we take the body to be non-rotating and to have a uniform density, and we place the external object on a parabolic trajectory. We work in the moving frame of the body, and ignore the gravitational waves produced by the center-of-mass motion (these were considered previously, in the case of elliptical and circular motion); as we shall see, the tidal gravitational waves are typically much weaker than the waves produced by the orbital motion. The body’s tidal dynamics was studied in some detail back in Sec. 2.5.3, and we begin our discussion with a recollection of the main results.

# Tidal dynamics

The body is assumed to be spherical and in hydrostatic equilibrium in the absence of a tidal interaction; in its unperturbed state it has a mass $M$ , a radius $a$ , and a uniform density $\rho _ { 0 }$ . The body is perturbed by an external object of mass $M ^ { \prime }$ at a position $x ^ { j } = r n ^ { j }$ relative to the body’s center-of-mass. This object produces a tidal potential $\begin{array} { r } { U _ { \mathrm { t i d a l } } = - \frac { 1 } { 2 } \mathcal { E } _ { j k } ( t ) x ^ { j } x ^ { k } } \end{array}$ inside the body, with

$$
\mathcal { E } _ { j k } = \frac { G M ^ { \prime } } { r ^ { 3 } } \big ( \delta _ { j k } - 3 n _ { j } n _ { k } \big ) ,
$$

denoting the tidal quadrupole moment. As we saw back in Sec. 2.5.3, the body’s deformation in response to the perturbation is measured by its mass quadrupole moment $I ^ { \langle j k \rangle } ( t )$ , which, according to Eq. (2.289), is given by

$$
I ^ { \langle j k \rangle } = - \frac { 2 } { 5 } M a ^ { 2 } \mathcal { F } ^ { j k } ,
$$

where

$$
\mathcal { F } ^ { j k } ( t ) : = \frac { 1 } { \omega _ { 2 } } \int _ { - \infty } ^ { t } \mathcal { E } ^ { j k } ( t ^ { \prime } ) \sin \omega _ { 2 } ( t - t ^ { \prime } ) d t ^ { \prime }
$$

is the body’s response function, with

$$
\omega _ { 2 } : = { \sqrt { { \frac { 4 } { 5 } } { \frac { G M } { a ^ { 3 } } } } }
$$

denoting the body’s $f$ -mode frequency for a quadrupole deformation.

# Gravitational waves

Differentiation of Eq. (11.100) gives

$$
\ddot { I } ^ { \langle j k \rangle } = - \frac { 2 } { 5 } M a ^ { 2 } { \mathcal G } ^ { j k } ,
$$

in which

$$
\mathcal { G } ^ { j k } ( t ) : = \frac { 1 } { \omega _ { 2 } } \int _ { - \infty } ^ { t } \ddot { \mathcal { E } } ^ { j k } ( t ^ { \prime } ) \sin \omega _ { 2 } ( t - t ^ { \prime } ) d t ^ { \prime }
$$

is the response function associated with $\ddot { \mathcal { E } } ^ { j k }$ instead of $\mathcal { E } ^ { j k }$ ; two integrations by parts were required to arrive at this result. Substituting this into the quadrupole formula of Eq. (11.55), we find that the gravitational-wave field is given by

$$
h _ { \mathrm { T T } } ^ { j k } ( t , x ) = - \frac { 4 } { 5 } \frac { G M a ^ { 2 } } { c ^ { 4 } R } \mathcal { G } _ { \mathrm { T T } } ^ { j k } ( \tau ) ,
$$

in which $R : = | { \boldsymbol { x } } |$ is the distance to the detector and $\tau : = t - R / c$ is retarded time.

We can use Eq. (11.105) to estimate the magnitude of the gravitational waves produced by a tidal interaction. For an external object of mass $M ^ { \prime }$ at a distance $r$ , the tidal moment scales as $\mathcal { E } _ { j k } \sim G M ^ { \prime } / r ^ { 3 }$ , and it changes over a time scale comparable to $\Omega _ { c } ^ { - 1 }$ , in which $\Omega _ { c } : = \sqrt { G ( M + M ^ { \prime } ) / r ^ { 3 } }$ is a characteristic frequency of the orbital motion. This yields $\ddot { \mathcal { E } } _ { j k } \sim \Omega _ { c } ^ { 2 } \mathcal { E } _ { j k }$ , and substitution within Eq. (11.104) returns the estimate $\mathcal { G } _ { j k } \sim \omega _ { 2 } ^ { - 2 } \ddot { \mathcal { E } } _ { j k } \sim$ $( \Omega _ { c } / \omega _ { 2 } ) ^ { 2 } \mathcal { E } _ { j k }$ . Inserting this within Eq. (11.105), we arrive at

$$
h \sim \frac { G ^ { 2 } ( M + M ^ { \prime } ) M ^ { \prime } } { c ^ { 4 } R } \frac { a ^ { 5 } } { r ^ { 6 } } .
$$

It is useful to compare this with Eq. (11.77), which provides an estimate for the gravitational waves produced by the orbital motion. According to this, we find that the ratio of wave

amplitudes is estimated as

$$
\frac { h _ { \mathrm { t i d a l } } } { h _ { \mathrm { o r b i t a l } } } \sim \frac { M ^ { \prime } } { M + M ^ { \prime } } \biggl ( \frac { a } { r } \biggr ) ^ { 5 } .
$$

The five powers of the ratio of length scales imply that when $r$ is even modestly larger than $a$ , the waves emitted during the tidal interaction are very weak compared with the waves produced by the orbital motion. The waves can be comparable only for very close encounters with $r \sim a$ .

# Parabolic encounter

To give concreteness to these considerations, we examine the tidal interaction that results when the external object is placed on a parabolic trajectory described by setting $e = 1$ in Eq. (11.68). The motion of the external object is parameterized by $p : = 2 r _ { \mathrm { m i n } }$ , in which $r _ { \mathrm { m i n } }$ is the distance of closest approach. It can also be parameterized by the frequency

$$
\Omega : = \sqrt { \frac { G ( M + M ^ { \prime } ) } { p ^ { 3 } } } ,
$$

which is such that the angular velocity $\dot { \phi } _ { \mathrm { m a x } }$ at closest approach is equal to $\dot { \phi } _ { \mathrm { m a x } } = 4 \Omega$ . It is useful to note that

$$
\biggl ( { \frac { \omega _ { 2 } } { \Omega } } \biggr ) ^ { 2 } = { \frac { 3 2 } { 5 } } { \frac { M } { M + M ^ { \prime } } } \biggl ( { \frac { r _ { \mathrm { m i n } } } { a } } \biggr ) ^ { 3 } .
$$

It is straightforward to differentiate Eq. (11.99) twice with respect to time and to insert the result within Eq. (11.104), which must then be evaluated numerically. We extract the gravitational-wave polarizations $h _ { + }$ and $h _ { \times }$ from Eq. (11.105) by adopting the same conventions as in Sec. 11.2.2. We obtain the expressions

$$
h _ { + , \times } = - h _ { 0 } H _ { + , \times } ,
$$

where

$$
h _ { 0 } = 3 \frac { G ^ { 2 } ( M + M ^ { \prime } ) M ^ { \prime } } { c ^ { 4 } R } \frac { a ^ { 5 } } { p ^ { 6 } }
$$

is the gravitational-wave amplitude, and the scale-free polarizations $H _ { + , \times }$ are extracted from $\begin{array} { r } { H ^ { j k } : = \frac 1 3 [ ( M + M ^ { \prime } ) / M ^ { \prime } ] ( \omega _ { 2 } / \Omega ^ { 2 } ) ^ { 2 } \mathcal { G } ^ { j k } } \end{array}$ . These are plotted in Fig. 11.3 for selected values of $\omega _ { 2 } / \Omega$ , and the caption describes their main properties.

# 11.3 Beyond the quadrupole formula: Waves at 1.5pn order

We now embark on a long journey to improve our description of gravitational waves by going beyond the quadrupole formula of Eq. (11.55). This, we recall, is the leading term in an expansion of the gravitational-wave field in powers of $v _ { c } / c$ , where $v _ { c }$ is a characteristic velocity of the source. We shall call this leading term the Newtonian contribution to the gravitational-wave field, and in this section we will compute corrections of order $( v _ { c } / c )$ , $( v _ { c } / c ) ^ { 2 }$ , and $( v _ { c } / c ) ^ { 3 }$ to the quadrupole formula; in other words, we shall calculate $h _ { \mathrm { T T } } ^ { j k }$ through $1 . 5 \mathrm { P N }$ order in a post-Newtonian expansion.

![](images/5e42bfb6d79ed86210b90d42a197e12d6d64c2bb11f451d60b0b36804765a5d7.jpg)  
The polarization $H _ { + }$ as a function of the dimensionless retarded time $\Omega \tau$ , for selected values of the ratio $\omega _ { 2 } / \Omega$ . The curves are displayed for an inclination angle $\iota = 3 0 ^ { \circ }$ , and a longitude of pericenter $\omega = 4 5 ^ { \circ }$ . We see that most of the emission takes place at and after the moment of closest approach $( \tau = 0 )$ ). When $\omega _ { 2 }$ is comparable to $\Omega$ , the parabolic encounter ignites a fluid mode of frequency $\omega _ { 2 }$ which produces a gravitational wave of frequency $\omega _ { 2 }$ . The effect is maximized when the resonant condition $2 \dot { \phi } _ { \mathfrak { m a x } } = 8 \Omega \simeq \omega _ { 2 }$ is met, and the wave is heavily suppressed when $\omega _ { 2 } \gg \Omega$ . In a more realistic model of the tidal interaction, the wave would eventually be damped by dissipative processes taking place inside the body; in our simplified model the fluid mode goes on forever.

We note that the post-Newtonian counting described here differs from the convention adopted back in Sec. 7.4; see Box 7.7. In the original convention the quadrupole terms in the gravitational potentials were given a 1pn label instead of the 0pn label assigned here. The reason for this can be gathered from the following expression for $h ^ { 0 0 }$ ,

$$
h ^ { 0 0 } = { \frac { 4 G } { c ^ { 2 } R } } \biggl [ M + { \frac { 1 } { 2 c ^ { 2 } } } \ddot { \mathcal { Z } } ^ { j k } N _ { j } N _ { k } + \cdot \cdot \cdot \biggr ] ,
$$

which holds in the far-away wave zone. The leading term in this expression is the mass term, and in the old convention this was given a sensible 0pn label. The quadrupole term is smaller than this by a factor of order $( v _ { c } / c ) ^ { 2 }$ , and this was given a 1pn label. Our new convention differs from this because our focus is now different: We are interested only in the spatial components of the gravitational potentials, and these do not contain a mass term. And since the leading term involves the Newtonian quadrupole moment $I ^ { j k }$ , it is convenient to reset the post-Newtonian counter and call the right-hand side of Eq. (11.55) the Newtonian contribution to $h _ { \mathrm { T T } } ^ { j k }$ . Additional terms are labeled $0 . 5 \mathrm { { P N } }$ , 1pn, and $1 . 5 \mathrm { { p N } }$ , and so on. The new convention has the merit of keeping the post-Newtonian orders of $h ^ { j k }$ in step with those of the source, and those of the multipole moments.

For concreteness the calculations will be specialized to a system of $N$ bodies that we assume to be well separated; these are identified by a label $A$ , and body $A$ has a total mass-energy $M _ { A }$ , a position $r _ { A } ( t )$ , and moves with a velocity ${ \pmb v } _ { A } ( t )$ . For simplicity we shall take the bodies to be point masses, and rely on the description given in Sec. 9.6.

# 11.3.1 Requirements and strategy

Our purpose in this first subsection is to identify the tasks that lie ahead: we map the terrain of our journey and plan the calculational strategy. The computations will be long and tedious, and they will occupy us in the remaining nine subsections. The reader who does not wish to follow the details can skip ahead to Box 11.4 and find a summary of our results.

We wish to integrate the wave equation

$$
\Pi h ^ { j k } = - \frac { 1 6 \pi G } { c ^ { 4 } } \tau ^ { j k }
$$

for the spatial components of the gravitational potentials, and evaluate the solution in the far-away wave zone. Here, $\tau ^ { j k } = ( - g ) ( T ^ { j k } + t _ { \mathrm { L L } } ^ { j k } + t _ { \mathrm { H } } ^ { j k } )$ are the spatial components of the effective energy-momentum pseudotensor first introduced in Sec. 6.2.1, decomposed into a material contribution $T ^ { j k }$ , the Landau–Lifshitz pseudotensor $t _ { \mathrm { L L } } ^ { j k }$ , and the harmonicgauge contribution $t _ { \mathrm { H } } ^ { j k }$ . We wish to integrate the wave equation to a degree of accuracy that surpasses what was achieved in Chapter 7; this amounts to constructing a third post-Minkowskian approximation to the exact gravitational potentials. And we wish to extract from $h ^ { j k }$ the transverse-tracefree pieces that truly represent the gravitational-wave field.

Techniques to integrate Eq. (11.113) were developed in Chapter 6 and summarized in Box 6.7. In Sec. 6.3 we learned to express the solution as an integral over the past light cone of the field point $( t , \boldsymbol { x } )$ , which is decomposed as

$$
h ^ { j k } = h _ { \mathcal { N } } ^ { j k } + h _ { \mathcal { W } } ^ { j k } .
$$

The near-zone piece $h _ { \mathcal { N } } ^ { j k }$ comes from the portion of the light cone that lies within the near zone (where $| x ^ { \prime } | < \mathcal { R }$ ), and the wave-zone piece $h _ { \mathcal { W } } ^ { j k }$ comes from the portion that lies in the wave zone (where $| x ^ { \prime } | > \mathcal { R }$ ); the boundary between the zones is arbitrarily positioned at the radius $| { \pmb x } ^ { \prime } | = \mathcal { R } \sim \lambda _ { c }$ . In Sec. 6.3.4 we derived an expression for $h _ { \mathcal { N } } ^ { j k }$ that is valid in the far-away wave zone; this is given by Eq. (6.91), which we copy as

$$
h _ { \mathcal { N } } ^ { j k } = \frac { 4 G } { c ^ { 4 } R } \sum _ { \ell = 0 } ^ { \infty } \frac { 1 } { \ell ! c ^ { \ell } } N _ { L } \bigg ( \frac { d } { d \tau } \bigg ) ^ { \ell } \int _ { \mathcal { M } } \tau ^ { j k } ( \tau , x ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } ,
$$

where $N : = x / R$ is a unit radial vector, $L$ a multi-index that contains a number $\ell$ of individual indices, $N _ { L } : = N _ { j _ { 1 } } N _ { j _ { 2 } } \cdot \cdot \cdot N _ { j _ { \ell } } , x ^ { \prime L } : = x ^ { \prime j _ { 1 } } x ^ { \prime j _ { 2 } } \cdot \cdot \cdot x ^ { \prime j _ { \ell } }$ , and where the domain of integration $\mathcal { M }$ is defined by $| { \boldsymbol { x } } ^ { \prime } | < \mathcal { R }$ .

We consider $h _ { \mathcal { W } } ^ { j k }$ at a later stage. For the time being we focus our attention on $h _ { \mathcal { N } } ^ { j k }$ , and write Eq. (11.115) in a form that showcases the first few terms:

$$
\begin{array} { c } { { \displaystyle h _ { \mathcal { N } } ^ { j k } = \frac { 4 G } { c ^ { 4 } R } \bigg \{ \int _ { \mathcal { M } } \tau ^ { j k } d ^ { 3 } x ^ { \prime } + \frac 1 c N _ { a } \frac { d } { d \tau } \int _ { \mathcal { M } } \tau ^ { j k } x ^ { \prime a } d ^ { 3 } x ^ { \prime } } } \\ { { + \frac 1 { 2 c ^ { 2 } } N _ { a } N _ { b } \frac { d ^ { 2 } } { d \tau ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { j k } x ^ { \prime a } x ^ { \prime b } d ^ { 3 } x ^ { \prime } } } \\ { { + \frac 1 { 6 c ^ { 3 } } N _ { a } N _ { b } N _ { c } \frac { d ^ { 3 } } { d \tau ^ { 3 } } \int _ { \mathcal { M } } \tau ^ { j k } x ^ { \prime a } x ^ { \prime b } x ^ { \prime c } d ^ { 3 } x ^ { \prime } + [ \ell \ge 4 ] \bigg \} , } } \end{array}
$$

where $[ \ell \geq 4 ]$ stands for the remaining terms in the sum over . In keeping with our previous discussion, we say that the first term on the right-hand side of Eq. (11.116) makes a 0pn contribution to $h ^ { j k }$ (together with a correction of 1pn order), the second term makes a $0 . 5 \mathrm { { P N } }$ contribution (together with a correction of $1 . 5 \mathrm { P N }$ order), the third term makes a 1pn contribution, and the fourth term a $1 . 5 \mathrm { { p N } }$ contribution; the $[ \ell \geq 4 ]$ terms contribute at $2 \mathrm { P N }$ and higher orders, and we shall not keep them in the calculation.

To help with the first two integrals we invoke the conservation identities of Eqs. (7.14), which we copy here as

$$
\begin{array} { c } { { \tau ^ { j k } = \displaystyle \frac { 1 } { 2 c ^ { 2 } } \displaystyle \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } \big ( \tau ^ { 0 0 } x ^ { j } x ^ { k } \big ) + \displaystyle \frac { 1 } { 2 } \partial _ { p } \big ( \tau ^ { j p } x ^ { k } + \tau ^ { k p } x ^ { j } - \partial _ { q } \tau ^ { p q } x ^ { j } x ^ { k } \big ) , } } \\ { { \tau ^ { j k } x ^ { a } = \displaystyle \frac { 1 } { 2 c } \displaystyle \frac { \partial } { \partial \tau } \big ( \tau ^ { 0 j } x ^ { k } x ^ { a } + \tau ^ { 0 k } x ^ { j } x ^ { a } - \tau ^ { 0 a } x ^ { j } x ^ { k } \big ) } } \\ { { + \displaystyle \frac { 1 } { 2 } \partial _ { p } \big ( \tau ^ { j p } x ^ { k } x ^ { a } + \tau ^ { k p } x ^ { j } x ^ { a } - \tau ^ { a p } x ^ { j } x ^ { k } \big ) . } } \end{array}
$$

Making the substitutions and introducing some notation to simplify the writing, we find that $h _ { \mathcal { N } } ^ { j \bar { k } }$ can be expressed as

$$
\begin{array} { l } { { h _ { \mathcal { N } } ^ { j k } = \displaystyle \frac { 2 G } { c ^ { 4 } R } \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } \bigg \{ Q ^ { j k } + Q ^ { j k a } N _ { a } + Q ^ { j k a b } N _ { a } N _ { b } + \displaystyle \frac { 1 } { 3 } Q ^ { j k a b c } N _ { a } N _ { b } N _ { c } + [ \ell \geq 4 ] \bigg \} } } \\ { { \quad \quad + \displaystyle \frac { 2 G } { c ^ { 4 } R } \bigg \{ P ^ { j k } + P ^ { j k a } N _ { a } \bigg \} , \eqno ( 1 1 . } } \end{array}
$$

in which the radiative multipole moments are defined by

$$
\begin{array} { l } { { \displaystyle Q ^ { j k } : = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } x ^ { \prime } { } ^ { j } x ^ { \prime } { } ^ { k } d ^ { 3 } x ^ { \prime } } , }  \\ { { \displaystyle Q ^ { j k a } : = \frac { 1 } { c } \int _ { \mathcal { M } } \left( c ^ { - 1 } \tau ^ { 0 j } x ^ { \prime } { } ^ { k } x ^ { \prime } { } ^ { a } + c ^ { - 1 } \tau ^ { 0 k } x ^ { \prime } { } ^ { j } x ^ { \prime } { } ^ { a } - c ^ { - 1 } \tau ^ { 0 a } x ^ { \prime } { } ^ { j } x ^ { \prime } \right) d ^ { 3 } x ^ { \prime } } , }  \\ { { \displaystyle Q ^ { j k a b } : = \frac { 1 } { c ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { j k } x ^ { \prime } { } ^ { a } x ^ { \prime \flat } d ^ { 3 } x ^ { \prime } } , }  \\ { { \displaystyle Q ^ { j k a b c } : = \frac { 1 } { c ^ { 3 } } \frac { d } { d \tau } \int _ { \mathcal { M } } \tau ^ { j k } x ^ { \prime } { } ^ { a } x ^ { \prime \flat } x ^ { \prime \prime } d ^ { 3 } x ^ { \prime } , } } \end{array}
$$

and where

$$
\begin{array} { r l } & { P ^ { j k } : = \displaystyle \oint _ { \partial \mathcal { M } } \left( \tau ^ { j p } x ^ { \prime k } + \tau ^ { k p } x ^ { \prime j } - \partial _ { q } ^ { \prime } \tau ^ { p q } x ^ { \prime j } x ^ { \prime k } \right) d S _ { p } , } \\ & { P ^ { j k a } : = \displaystyle \frac { 1 } { c } \frac { d } { d \tau } \oint _ { \partial \mathcal { M } } \left( \tau ^ { j p } x ^ { \prime k } x ^ { \prime a } + \tau ^ { k p } x ^ { \prime j } x ^ { \prime a } - \tau ^ { a p } x ^ { \prime j } x ^ { \prime k } \right) d S _ { p } , } \end{array}
$$

are surface integrals that also contribute to $h _ { \mathcal { N } } ^ { j k }$ . In the radiative moments, $\tau ^ { j k }$ is expressed as a function of $\tau$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . The same is true within the surface integrals, except for the fact that $x ^ { \prime j }$ is now equal to $\mathcal { R } N ^ { j }$ ; the surface element on $\partial \mathcal { M }$ is $d S _ { j } : = \mathcal { R } ^ { 2 } N _ { j } d \Omega$ . The multipole moments and surface integrals are functions of $\tau$ only.

In the following subsections we will endeavor to calculate the quantities that appear within Eq. (11.118). As was stated previously, we wish to compute $h ^ { j k }$ accurately through $1 . 5 \mathrm { P N }$ order. In a schematic notation, what we want is

$$
h ^ { j k } = { \frac { G } { c ^ { 4 } R } } { \Big ( } c ^ { 0 } + c ^ { - 1 } + c ^ { - 2 } + c ^ { - 3 } + \cdots { \Big ) } ,
$$

in which the leading, $c ^ { 0 }$ term is the 0pn contribution, the correction of order $c ^ { - 1 }$ a $0 . 5 \mathrm { { P N } }$ term, and so on. To achieve this we need to calculate $c ^ { - 2 } \tau ^ { 0 0 } = c ^ { 0 } + c ^ { - 2 } + \cdot \cdot \cdot$ to obtain $Q ^ { j k } = c ^ { 0 } + c ^ { - 2 } + \cdot \cdot \cdot$ , $c ^ { - 1 } \tau ^ { 0 j } = c ^ { 0 } + c ^ { - 2 } + \cdot \cdot \cdot$ to obtain $\mathcal { Q } ^ { j k a } = c ^ { - 1 } + c ^ { - 3 } + \cdot \cdot \cdot$ , and $\tau ^ { j k } = c ^ { 0 } + \cdots$ to obtain $\mathcal { Q } ^ { j k a b } = c ^ { - 2 } + \cdot \cdot \cdot$ and $\mathcal { Q } ^ { j k a b c } = c ^ { - 3 } + \cdot \cdot \cdot$ . And on $\partial \mathcal { M }$ we need to calculate $\tau ^ { j k } = c ^ { 0 } + c ^ { - 2 } + \cdot \cdot \cdot$ to obtain $P ^ { j k } = c ^ { 0 } + c ^ { - 2 } + \cdot \cdot \cdot$ and $P ^ { j k a } = c ^ { - 1 } +$ $c ^ { - 3 } + \cdots$ All in all, this will give us the $1 . 5 \mathrm { P N }$ accuracy that we demand for $h ^ { j k }$ .

Our considerations have so far excluded $h _ { \mathcal { W } } ^ { j k }$ . We postpone a detailed discussion until Sec. 11.3.7, where we compute this contribution to the gravitational potentials. For the time being it suffices to say that ${ h _ { \mathcal { W } } ^ { j k } }$ contributes at $1 . 5 \mathrm { { P N } }$ order. It is therefore needed to achieve the required level of accuracy for $h ^ { j k }$ .

The calculations that follow are lengthy. They are simplified considerably by the observation that ultimately we wish to extract the transverse-tracefree part of $h ^ { j k }$ . It is therefore superfluous to calculate any term that will not survive the TT projection introduced in Sec. 11.1.7. For example, a term in $h ^ { j k }$ that is known to be proportional to $\delta ^ { j k }$ , or to $N ^ { j }$ , will not survive the projection, and does not need to be computed. There are many such terms, and ignoring them is a substantial time saver. As another example, terms in $\boldsymbol { Q } ^ { j k a b }$ that are proportional to $\delta ^ { j a }$ , or $\delta ^ { k a }$ , or $\delta ^ { j b }$ , or $\delta ^ { k b }$ (but not $\delta ^ { a b }$ !), can all be ignored because they produce contributions to $h ^ { j k }$ that are proportional to $N ^ { j }$ or $N ^ { k }$ , and these will not survive the TT projection. To indicate equality modulo terms that do not survive the transverse-tracefree projection, we introduce the notation $\stackrel { \pi } { = }$ , so that

$$
A ^ { j k } \overset { \mathtt { \tiny { T } } } { = } B ^ { j k }
$$

whenever

$$
\left( \mathrm { T T } \right) _ { p q } ^ { j k } A ^ { p q } = \left( \mathrm { T T } \right) _ { p q } ^ { j k } B ^ { p q } .
$$

In other words, $A ^ { j k }$ and $B ^ { j k }$ differ by a tensor $C ^ { j k }$ that contains no TT part: $\left( \mathrm { T T } \right) _ { p q } ^ { j k } C ^ { p q } = 0$ .

An additional source of simplification – an important one – was exploited previously in Sec. 7.4, with a justification provided in Sec. 6.3.3: we are free to ignore all $\mathcal { R }$ -dependent terms in $h _ { \mathcal { N } } ^ { j k }$ , and all $\mathcal { R }$ -dependent terms in $h _ { \mathcal { W } } ^ { j k }$ , because any dependence on the arbitrary cutoff parameter $\mathcal { R }$ (the radius of the artificial boundary between the near zone and the wave zone) is guaranteed to cancel out when $h _ { \mathcal { N } } ^ { j k }$ and $h _ { \mathcal { W } } ^ { j k }$ are added together to form the complete potentials $h ^ { j k }$ . The freedom to discard all $\mathcal { R }$ -dependent terms is another substantial time saver.

# 11.3.2 Integration techniques for field integrals

In the course of our calculations we shall encounter a number of field integrals, a representative example of which is

$$
E ^ { j k } : = \frac { 1 } { 4 \pi } \int _ { \mathcal M } U \partial ^ { j } U x ^ { k } d ^ { 3 } x ,
$$

where $\mathcal { M }$ is the domain of integration $| { \boldsymbol { x } } | < \mathcal { R }$ , and where

$$
U : = \sum _ { A } { \frac { G M _ { A } } { | \pmb { x } - \pmb { r } _ { A } | } }
$$

is the Newtonian potential for a system of point masses. In this subsection we introduce techniques to evaluate such integrals. We will examine the specific case of Eq. (11.124), but the techniques are quite general, and they apply just as well to many similar field integrals.

# Explicit form of $E ^ { j k }$ ; change of integration variables

After evaluating $\partial ^ { j } U$ we find that the field integral can be expressed in the more explicit form

$$
E ^ { j k } = - \sum _ { A } G ^ { 2 } M _ { A } ^ { 2 } E _ { A } ^ { j k } - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } E _ { A B } ^ { j k } ,
$$

where

$$
\begin{array} { l } { { \displaystyle E _ { A } ^ { j k } : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { ( x - r _ { A } ) ^ { j } x ^ { k } } { | x - r _ { A } | ^ { 4 } } d ^ { 3 } x , } } \\ { { \displaystyle E _ { A B } ^ { j k } : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { ( x - r _ { B } ) ^ { j } x ^ { k } } { | x - r _ { A } | | x - r _ { B } | ^ { 3 } } d ^ { 3 } x . } } \end{array}
$$

To evaluate the first integral we make the substitution $\pmb { x } = \pmb { r } _ { A } + \pmb { y }$ and integrate with respect to the new variables $\boldsymbol { y }$ . This leads to

$$
E _ { A } ^ { j k } = \frac { 1 } { 4 \pi } \int _ { \mathcal M } \frac { y ^ { j } y ^ { k } } { y ^ { 4 } } d ^ { 3 } y + \frac { r _ { A } ^ { k } } { 4 \pi } \int _ { \mathcal M } \frac { y ^ { j } } { y ^ { 4 } } d ^ { 3 } y ,
$$

where $y : = | { \boldsymbol { y } } |$ . To evaluate the second integral we use instead $\pmb { x } = \pmb { r } _ { B } + \pmb { y }$ and integrate with respect to $_ { y }$ . This leads to

$$
E _ { A B } ^ { j k } = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - \boldsymbol { r } _ { A B } | } \frac { y ^ { j } y ^ { k } } { y ^ { 3 } } d ^ { 3 } y + \frac { r _ { B } ^ { k } } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - \boldsymbol { r } _ { A B } | } \frac { y ^ { j } } { y ^ { 3 } } d ^ { 3 } y ,
$$

where $\pmb { r } _ { A B } : = \pmb { r } _ { A } - \pmb { r } _ { B }$

# Translation of the domain of integration

Each one of the integrals that appears in Eqs. (11.128) and (11.129) is of the form

$$
\int _ { \mathcal { M } } f ( \boldsymbol { y } ) d ^ { 3 } \boldsymbol { y } ,
$$

where $f$ is a function of the vector $_ { y }$ , which is related to the original variables $\boldsymbol { x }$ by a translation $\boldsymbol { x } = \boldsymbol { y } + \boldsymbol { r }$ , with $r$ independent of $_ x$ . The domain of integration $\mathcal { M }$ is defined by $| x | < \mathcal { R }$ , or $| y + r | < \mathcal { R }$ , and it will be convenient to replace it by the simpler domain $\mathcal { M } _ { y }$ defined by $y : = | y | < \mathcal { R }$ .

To effect this replacement we note that the cutoff radius $\mathcal { R }$ can be assumed to be large compared with $r : = | r |$ . (Recall the discussion of Sec. 6.3.3, in which $\mathcal { R }$ is chosen to be comparable to $\lambda _ { c }$ , the characteristic wavelength of the gravitational radiation. Recall also the discussion of Sec. 6.3.2, in which $\lambda _ { c }$ is shown to be large compared with both $| \pmb { r } _ { A } |$ and $| r _ { A B } |$ , because in a slow-motion situation the matter distribution is always situated deep within the near zone. Conclude from these observations that $r / \mathcal { R } \ll 1$ , as claimed.) The condition that defines $\mathcal { M }$ is $y ^ { 2 } + 2 r \cdot y + r ^ { 2 } < \mathcal R ^ { 2 }$ , and this can be expressed more simply as

$$
y < \mathcal { R } - r \cos { \gamma } + O ( r ^ { 2 } / \mathcal { R } ) ,
$$

when $r / \mathcal { R } \ll 1$ ; here $\gamma$ is the angle between the vectors $\boldsymbol { y }$ and $r$

Switching to spherical polar coordinates $( y , \theta , \phi )$ associated with the vector $\boldsymbol { y }$ , the integral is

$$
\begin{array} { l } { { \displaystyle \int _ { \mathcal { M } } f ( y ) d ^ { 3 } y = \int d \Omega \int _ { 0 } ^ { \mathcal { R } - r \cos \gamma + \cdots } f ( y , \theta , \phi ) y ^ { 2 } d y } } \\ { { \displaystyle \quad = \int d \Omega \int _ { 0 } ^ { \mathcal { R } } f ( y , \theta , \phi ) y ^ { 2 } d y + \int d \Omega \int _ { \mathcal { R } } ^ { \mathcal { R } - r \cos \gamma + \cdots } f ( y , \theta , \phi ) y ^ { 2 } d y , } } \end{array}
$$

where $d \Omega = \sin \theta d \theta d \phi$ is an element of solid angle. In the second line, the first integral is over the domain $\mathcal { M } _ { y }$ , while the second integral is

$$
\int ( - r \cos \gamma ) \mathcal { R } ^ { 2 } f ( \mathcal { R } , \theta , \phi ) d \Omega = - \oint _ { \partial \mathcal { M } _ { y } } f ( y ) \boldsymbol { r } \cdot d \boldsymbol { S }
$$

to first order in $r / \mathcal { R }$ ; here, $d S ^ { j } : = \mathcal { R } ^ { 2 } N ^ { j } d \Omega$ , with $N : = y / y$ , is the surface element on $\partial \mathcal { M } _ { y }$ , the boundary of $\mathcal { M } _ { y }$ described by the equation $y = \mathcal { R }$ .

We have obtained the useful approximation

$$
\int _ { \mathcal M } f ( y ) d ^ { 3 } y = \int _ { { \mathcal M } _ { y } } f ( y ) d ^ { 3 } y - \oint _ { \partial { \mathcal M } _ { y } } f ( y ) r \cdot d S + \cdot \cdot \cdot ,
$$

in which the domain of integration $\mathcal { M } _ { y }$ is defined by $y : = | { \mathbf { y } } | < \mathcal { R }$ , and $\partial \mathcal { M } _ { y }$ is its boundary at $y = \mathcal { R }$ . It is clear that the surface integral in Eq. (11.133) is smaller than the volume integral by a factor of order $r / \mathcal { R } \ll 1$ ; the neglected terms are smaller still.

# Evaluation of E jkA

We now return to the field integral of Eq. (11.128). We begin by working on the first term, which we copy as

$$
{ \frac { 1 } { 4 \pi } } \int _ { \mathcal { M } } { \frac { y ^ { j } y ^ { k } } { y ^ { 4 } } } d ^ { 3 } y .
$$

Inserting this within Eq. (11.133), we find that the volume integral is

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { y ^ { j } y ^ { k } } { y ^ { 4 } } d ^ { 3 } y = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } N ^ { j } N ^ { k } d y d \Omega = \langle \langle N ^ { j } N ^ { k } \rangle \rangle \int _ { 0 } ^ { \mathcal { R } } d y = \frac { 1 } { 3 } \delta ^ { j k } \mathcal { R } ,
$$

in which $\langle \langle \cdot \cdot \cdot \rangle \rangle : = ( 4 \pi ) ^ { - 1 } \int ( \cdot \cdot \cdot ) d \Omega$ denotes an angular average; the identity $\begin{array} { r } { \langle \langle N ^ { j } N ^ { k } \rangle \rangle = \frac { 1 } { 3 } \delta ^ { j k } } \end{array}$ was established back in Sec. 1.5.3, along with other similar results. This contribution to $E _ { A } ^ { j k }$ can be discarded because it is proportional to $\mathcal { R }$ , and it was agreed near the end of Sec. 11.3.1 that all $\mathcal { R }$ -dependent terms can indeed be ignored. With the understanding that $r$ stands for $r _ { A }$ , the surface integral is

$$
- \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } _ { y } } \frac { y ^ { j } y ^ { k } } { y ^ { 4 } } \boldsymbol { r } \cdot \boldsymbol { d S } = - \frac { 1 } { 4 \pi } \int N ^ { j } N ^ { k } r _ { p } N ^ { p } d \Omega = - r _ { p } \langle \langle N ^ { j } N ^ { k } N ^ { p } \rangle \rangle = 0 .
$$

The neglected terms in Eq. (11.133) are of order $\mathcal { R } ^ { - 1 }$ and smaller, and because they depend on $\mathcal { R }$ , they can be freely discarded. We conclude that the first term in Eq. (11.128) evaluates to zero.

We next set to work on the second term, which involves the integral

$$
{ \frac { 1 } { 4 \pi } } \int _ { \mathcal { M } } { \frac { y ^ { j } } { y ^ { 4 } } } d ^ { 3 } y .
$$

Inserting this within Eq. (11.133), we find that the volume integral is

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal M _ { y } } \frac { y ^ { j } } { y ^ { 4 } } d ^ { 3 } y = \langle \langle N ^ { j } \rangle \rangle \int _ { 0 } ^ { \mathcal R } \frac { d y } { y } = 0 .
$$

It is a fortunate outcome that the logarithmic divergence at $y = 0$ (which occurs because the matter distribution is modeled as a collection of point masses) requires no explicit regularization, because the angular integration vanishes identically. The surface integral is

$$
- \frac { 1 } { 4 \pi } \oint _ { \mathcal { M } _ { y } } \frac { y ^ { j } } { y ^ { 4 } } \pmb { r } \cdot \pmb { d S } = - \frac { r _ { p } } { \mathcal { R } } \langle \langle N ^ { j } N ^ { p } \rangle \rangle = - \frac { 1 } { 3 } \frac { r ^ { j } } { \mathcal { R } } ,
$$

in which $r$ stands for $r _ { A }$ . The additional terms in Eq. (11.133) are smaller by additional powers of $r / \mathcal { R } \ll 1$ , and because they all depend on $\mathcal { R }$ , they can be freely discarded. We conclude that the second term in Eq. (11.128) evaluates to zero.

We have arrived at

$$
E _ { A } ^ { j k } = 0 ,
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded.

To evaluate the right-hand side of Eq. (11.129) we continue to use Eq. (11.133) to express an integral over the domain $\mathcal { M }$ in terms of a volume integral over $\mathcal { M } _ { y }$ and a surface integral over $\partial \mathcal { M } _ { y }$ . We also make use of the addition theorem for spherical harmonics,

$$
\frac { 1 } { | y - r _ { A B } | } = \sum _ { \ell = 0 } ^ { \infty } \sum _ { m = - \ell } ^ { \ell } \frac { 4 \pi } { 2 \ell + 1 } \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } Y _ { \ell m } ^ { * } ( { \pmb n } _ { A B } ) Y ^ { \ell m } ( N ) ,
$$

in which $r _ { < } : = \mathrm { m i n } ( y , r _ { A B } ) , r _ { > } = \mathrm { m a x } ( y , r _ { A B } ) , N : = y / y$ , and $\pmb { n } _ { A B } : = \pmb { r } _ { A B } / r _ { A B } .$ . We insert Eq. (11.139) within the first integral on the right-hand side of Eq. (11.129). Recalling Eq. (11.133), we approximate this by

$$
\begin{array} { r l r } {  { \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - r _ { A B } | } \frac { y ^ { j } y ^ { k } } { y ^ { 3 } } d ^ { 3 } y } } \\ & { } & { = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - r _ { A B } | } N ^ { j } N ^ { k } y d y d \Omega } \\ & { } & { = \sum _ { \ell } \frac { 1 } { 2 \ell + 1 } \int _ { 0 } ^ { \mathcal { R } } d y y \frac { r _ { \ell } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } \sum _ { m } Y _ { \ell m } ^ { * } ( n _ { A B } ) \int Y ^ { \ell m } ( N ) N ^ { j } N ^ { k } d \Omega . } \end{array}
$$

To evaluate the angular integral we express $N ^ { j } N ^ { k }$ as

$$
N ^ { j } N ^ { k } = N ^ { \left. j k \right. } + \frac 1 3 \delta ^ { j k } ,
$$

where $N ^ { \langle j k \rangle }$ is an STF tensor of the sort introduced back in Sec. 1.5.3, and we invoke the identity of Eq. (1.171),

$$
\sum _ { m = - \ell } ^ { \ell } Y _ { \ell m } ^ { * } ( \pmb { n } _ { A B } ) \int Y _ { \ell m } ( \pmb { N } ) N ^ { \langle L ^ { \prime } \rangle } d \Omega = \delta _ { \ell \ell ^ { \prime } } n _ { A B } ^ { \langle L \rangle } .
$$

This produces

$$
{ \frac { 1 } { 4 \pi } } \int _ { \mathcal { M } _ { y } } { \frac { 1 } { | y - r _ { A B } | } } { \frac { y ^ { j } y ^ { k } } { y ^ { 3 } } } d ^ { 3 } y = { \frac { 1 } { 5 } } K ( 2 , 1 ) n _ { A B } ^ { ( j k ) } + { \frac { 1 } { 3 } } K ( 0 , 1 ) \delta ^ { j k } ,
$$

where the radial integrals

$$
K ( \ell , n ) : = \int _ { 0 } ^ { \mathcal { R } } y ^ { n } \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } d y
$$

are evaluated below. This expression must be corrected by the surface integral of Eq. (11.133). We have

$$
\frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } _ { y } } \frac { 1 } { | y - r _ { A B } | } \frac { y ^ { j } y ^ { k } } { y ^ { 3 } } r \cdot d S = \frac { \mathcal { R } r _ { p } } { 4 \pi } \int \frac { 1 } { | y - r _ { A B } | } N ^ { j } N ^ { k } N ^ { p } d \Omega ,
$$

in which $r$ stands for $r _ { B }$ . Because the leading term of $| y - r _ { A B } | ^ { - 1 }$ in an expansion in powers of $r _ { A B } / \mathcal { R } \ll 1$ is equal to $\mathcal { R } ^ { - 1 }$ , the surface integral potentially gives rise to an $\mathcal { R }$ - independent contribution to $E _ { A B } ^ { j k }$ . But this leading term is proportional to $\langle \langle N ^ { j } N ^ { k } N ^ { p } \rangle \rangle = 0$

and we find that the surface integral does not actually contribute. At this stage we have obtained

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - r _ { A B } | } \frac { y ^ { j } y ^ { k } } { y ^ { 3 } } d ^ { 3 } y = \frac { 1 } { 5 } K ( 2 , 1 ) n _ { A B } ^ { ( j k ) } + \frac { 1 } { 3 } K ( 0 , 1 ) \delta ^ { j k }
$$

for the first integral on the right-hand side of Eq. (11.129).

We next set to work on the second integral, and we begin by evaluating

$$
\begin{array} { l } { \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - r _ { A B } | } \frac { y ^ { j } } { y ^ { 3 } } d ^ { 3 } y } \\ { \displaystyle \quad = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - r _ { A B } | } N ^ { j } d y d \Omega } \\ { \displaystyle \quad = \sum _ { \ell } \frac { 1 } { 2 \ell + 1 } \int _ { 0 } ^ { \mathcal { R } } d y \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } \sum _ { m } Y _ { \ell m } ^ { * } ( n _ { A B } ) \int Y ^ { \ell m } ( N ) N ^ { j } d \Omega . } \end{array}
$$

Using Eqs. (11.142) and (11.144), this is

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { \left| y - \pmb { r } _ { A B } \right| } \frac { y ^ { j } } { y ^ { 3 } } d ^ { 3 } y = \frac { 1 } { 3 } K ( 1 , 0 ) n _ { A B } ^ { j } .
$$

This must be corrected by the surface integral of Eq. (11.133), and it is easy to show that in this case also, the result scales as $\mathcal { R } ^ { - 1 }$ and does not contribute. We have therefore obtained $\textstyle { \frac { 1 } { 3 } } K ( 1 , 0 ) n _ { A B } ^ { j }$ for the second integral on the right-hand side of Eq. (11.129).

Collecting results, we find that

$$
E _ { A B } ^ { j k } = \frac { 1 } { 5 } K ( 2 , 1 ) n _ { A B } ^ { \langle j k \rangle } + \frac { 1 } { 3 } K ( 0 , 1 ) \delta ^ { j k } + \frac { 1 } { 3 } K ( 1 , 0 ) n _ { A B } ^ { j } r _ { B } ^ { k } .
$$

# Radial integrals

To complete the computation we must now evaluate the radial integrals defined by Eq. (11.144),

$$
K ( \ell , n ) : = \int _ { 0 } ^ { \mathcal { R } } y ^ { n } \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } d y ,
$$

in which $r _ { < } : = \operatorname* { m i n } ( y , r )$ and $r _ { > } = \operatorname* { m a x } ( y , r )$ , with $r$ standing for $r _ { A B }$

Excluding the case $n = \ell$ , which never occurs in practice, we have

$$
\begin{array} { c } { { \displaystyle K ( \ell , n ) = \frac 1 { r ^ { \ell + 1 } } \int _ { 0 } ^ { r } y ^ { \ell + n } d y + r ^ { \ell } \int _ { r } ^ { \mathcal { R } } y ^ { n - \ell - 1 } d y } } \\ { { \displaystyle = \frac { r ^ { n } } { \ell + n + 1 } - \frac { r ^ { n } } { n - \ell } \Big [ 1 - ( r / \mathcal { R } ) ^ { \ell - n } \Big ] . } } \end{array}
$$

We discard the last term because it depends on the cutoff radius $\mathcal { R }$ , and we conclude that

$$
K ( \ell , n ) = { \frac { 2 \ell + 1 } { ( \ell - n ) ( \ell + n + 1 ) } } | { \pmb { r } } _ { A B } | ^ { n } \qquad ( \ell \neq n ) .
$$

In particular, $\begin{array} { r } { K ( 2 , 1 ) = \frac { 5 } { 4 } r _ { A B } } \end{array}$ , $\begin{array} { r } { K ( 0 , 1 ) = - \frac { 1 } { 2 } r _ { A B } } \end{array}$ , and $\begin{array} { r } { K ( 1 , 0 ) = \frac { 3 } { 2 } } \end{array}$

# Final answer

$E _ { A B } ^ { j k }$

$$
E _ { A B } ^ { j k } = \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { \langle j k \rangle } - \frac { 1 } { 6 } r _ { A B } \delta ^ { j k } + \frac { 1 } { 2 } n _ { A B } ^ { j } r _ { B } ^ { k } .
$$

This, together with Eq. (11.138) for $E _ { A } ^ { j k }$ , can now be inserted within Eq. (11.126). We arrive at

$$
E ^ { j k } = - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } \biggl ( { \frac { 1 } { 4 } } r _ { A B } n _ { A B } ^ { \langle j k \rangle } - { \frac { 1 } { 6 } } r _ { A B } \delta ^ { j k } + { \frac { 1 } { 2 } } n _ { A B } ^ { j } r _ { B } ^ { k } \biggr ) ,
$$

and this can also be expressed as

$$
E ^ { j k } = - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } \bigg ( \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { \langle j k \rangle } - \frac { 1 } { 6 } r _ { A B } \delta ^ { j k } - \frac { 1 } { 2 } n _ { A B } ^ { j } r _ { A } ^ { k } \bigg )
$$

if we interchange the identities of bodies $A$ and $B$ and recall that $\pmb { n } _ { B A } = - \pmb { n } _ { A B }$ . When we add these expressions and divide by 2, we obtain the symmetrized form

$$
E ^ { j k } = - \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } \Bigg ( \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { \langle j k \rangle } - \frac { 1 } { 6 } r _ { A B } \delta ^ { j k } - \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } \Bigg ) .
$$

This becomes

$$
E ^ { j k } = { \frac { 1 } { 4 } } \delta ^ { j k } \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } \vert \pmb { r } _ { A } - \pmb { r } _ { B } \vert
$$

after simplification, and this is our final answer.

# Box 11.3

# Field integrals

Let us retrace the main steps that led us from the definition

$$
E ^ { j k } = \frac { 1 } { 4 \pi } \int _ { \mathcal M } U \partial ^ { j } U x ^ { k } d ^ { 3 } x ,
$$

to its evaluation

$$
E ^ { a b } = { \frac { 1 } { 4 } } \delta ^ { j k } \sum _ { A } \sum _ { B \neq A } G ^ { 2 } { \cal M } _ { A } { \cal M } _ { B } | r _ { A } - r _ { B } | .
$$

These steps will allow us to evaluate many similar field integrals.

After inserting the Newtonian potential and its derivative within the integral, we change the variables of integration from $_ { x }$ to $y = x - r ,$ in which $r$ stands for either $\pmb { r } _ { A } 0 \mathsf { r } \pmb { r } _ { B }$ , depending on the context. We also translate the domain of integration from $\mathcal { M }$ (defined by $| x | < \mathcal { R } )$ ) to $\mathcal { M } _ { y }$ (defined by $| y | < \mathcal { R } )$ , and we make use of the identity

$$
\int _ { \mathcal { M } } f ( y ) d ^ { 3 } y = \int _ { \mathcal { M } _ { y } } f ( y ) d ^ { 3 } y - \oint _ { \partial \mathcal { M } _ { y } } f ( y ) r \cdot d S + \cdot \cdot \cdot ,
$$

in which the surface integral is smaller than the volume integral by a factor of order $| r | / \mathcal { R } \ll 1$ (and the dotted terms are smaller still).

Next we invoke the addition theorem for spherical harmonics,

$$
\frac { 1 } { | y - r _ { A B } | } = \sum _ { \ell = 0 } ^ { \infty } \sum _ { m = - \ell } ^ { \ell } \frac { 4 \pi } { 2 \ell + 1 } \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } Y _ { \ell m } ^ { * } ( { \pmb n } _ { A B } ) Y ^ { \ell m } ( N ) ,
$$

in which $\boldsymbol { r } _ { A B } = \boldsymbol { r } _ { A } - \boldsymbol { r } _ { B } , \boldsymbol { r } _ { < } : = \mathsf { m i n } ( \boldsymbol { y } , \boldsymbol { r } _ { A B } ) , \boldsymbol { r } _ { > } = \mathsf { m a x } ( \boldsymbol { y } , \boldsymbol { r } _ { A B } ) , N : = \boldsymbol { y } / \boldsymbol { y } ,$ and ${ \pmb n } _ { A B } : =$ $r _ { A B } / r _ { A B }$ . After expressing all factors such as $N ^ { L }$ in terms of STF tensors, the angular integrations are carried out with the help of the identity

$$
\sum _ { m = - \ell } ^ { \ell } Y _ { \ell m } ^ { * } ( \pmb { n } _ { A B } ) \int Y _ { \ell m } ( \pmb { N } ) N ^ { \langle L ^ { \prime } \rangle } d \Omega = \delta _ { \ell \ell ^ { \prime } } n _ { A B } ^ { \langle L \rangle } .
$$

We rely also on the following listing of angular averages:

$$
\begin{array} { c } { { \langle \langle N ^ { j } \rangle \rangle = 0 , } } \\ { { \langle \langle N ^ { j } N ^ { k } \rangle \rangle = \displaystyle { \frac { 1 } { 3 } \delta ^ { j k } } , } } \\ { { \langle \langle N ^ { j } N ^ { k } N ^ { p } \rangle \rangle = 0 , } } \\ { { \langle \langle N ^ { j } N ^ { k } N ^ { p } N ^ { q } \rangle \rangle = \displaystyle { \frac { 1 } { 1 5 } } \big ( \delta ^ { j k } \delta ^ { p q } + \delta ^ { j p } \delta ^ { k q } + \delta ^ { j q } \delta ^ { k p } \big ) , } } \end{array}
$$

where $\begin{array} { r } { \langle \langle \cdot \cdot \cdot \rangle \rangle : = ( 4 \pi ) ^ { - 1 } \int ( \cdot \cdot \cdot ) d \Omega ; } \end{array}$ ; these results were obtained back in Sec. 1.5.3.

This leaves us with a number of radial integrations to work out, and these are given by

$$
K ( \ell , n ) : = \int _ { 0 } ^ { \mathcal { R } } y ^ { n } \frac { r _ { < } ^ { \ell } } { r _ { > } ^ { \ell + 1 } } d y = \frac { 2 \ell + 1 } { ( \ell - n ) ( \ell + n + 1 ) } | r _ { A B } | ^ { n } ,
$$

provided that $\ell \neq n$

And at last, after simplification, we obtain our final expression for the field integral. All the while we are justified to throw away any term that contains an explicit dependence on the arbitrary cutoff radius $\mathcal { R }$ .

# 11.3.3 Radiative quadrupole moment

We launch our calculation of the gravitational-wave field with a computation of $\boldsymbol { Q } ^ { j k }$ , the radiative quadrupole moment. According to Eq. (11.119), this is defined by

$$
Q ^ { j k } ( \tau ) : = \frac { 1 } { c ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { 0 0 } ( \tau , { \pmb x } ) x ^ { j } x ^ { k } d ^ { 3 } { \pmb x } ,
$$

in which $\tau : = t - R / c$ is retarded time, and where we suppress the primes on the integration variables to simplify the notation. (It should be kept in mind that $R$ is the distance to the field point, which is distinct from the source point now identified by the vector $_ { x }$ .) We show

below that the radiative quadrupole moment is given by

$$
Q ^ { j k } \stackrel { \pi } { = } \sum _ { A } M _ { A } \biggl ( 1 + \frac { 1 } { 2 } \frac { v _ { A } ^ { 2 } } { c ^ { 2 } } - \frac { 1 } { 2 } \frac { \lfloor U \rfloor _ { A } } { c ^ { 2 } } \biggr ) r _ { A } ^ { j } r _ { A } ^ { k } + { \cal O } ( c ^ { - 4 } ) ,
$$

where

$$
\lfloor U \rfloor _ { A } : = \sum _ { B \neq A } { \frac { G M _ { B } } { r _ { A B } } }
$$

is the partie finie of the Newtonian potential $U ( { \pmb x } )$ evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ . The expression of Eq. (11.156) leaves out terms proportional to $\delta ^ { j k }$ that would not survive the action of the transverse-tracefree projector $\left( \mathrm { T T } \right) ^ { j k } p q$ , as well as $\mathcal { R }$ -dependent terms that can be freely discarded. It is understood that the position vectors $r _ { A }$ , and the velocity vectors ${ \pmb v } _ { A }$ , are evaluated at the retarded time $\tau$ .

According to the discussion of Sec. 11.3.1, to calculate $\boldsymbol { Q } ^ { j k }$ to the required degree of accuracy, we need an expression for $c ^ { - 2 } \tau ^ { 0 0 }$ that includes terms of order $c ^ { 0 }$ (Newtonian, or 0pn) and terms of order $c ^ { - 2 }$ (1pn). Such an expression was obtained back in Sec. 7.3.1 in the case of a matter distribution that consists of a perfect fluid. According to Eq. (7.54a), we have that

$$
c ^ { - 2 } \tau ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi \biggr ) \biggr ] - \frac { 7 } { 8 \pi G c ^ { 2 } } \partial _ { p } U \partial ^ { p } U + { \cal O } ( c ^ { - 4 } ) .
$$

For a system of point particles we have that $\begin{array} { r } { \rho ^ { * } = \sum _ { A } M _ { A } \delta ( \pmb { x } - \pmb { r } _ { A } ) } \end{array}$ and $\Pi = 0$ , and the Newtonian potential reduces to $\begin{array} { r } { U = \sum _ { B } G M _ { B } | \pmb { x } - \pmb { r } _ { B } | ^ { - 1 } } \end{array}$ .

This expression for $c ^ { - 2 } \tau ^ { 0 0 }$ is ill-defined for point particles, because the term $B = A$ in $U$ gives rise to a term $\begin{array} { r } { \sum _ { A } G M _ { A } ^ { 2 } | \pmb { x } - \pmb { r } _ { A } | ^ { - 1 } \delta ( \pmb { x } - \pmb { r } _ { A } ) } \end{array}$ in $\rho ^ { * } U$ . This is not defined as a distribution, and such a term gives rise to an ambiguity in the evaluation of the radiative quadrupole moment. We have, however, encountered a similar situation before, and learned how to deal with it. Indeed, suitable regularization methods were developed back in Sec. 9.6, where it was shown that ambiguous integrals can be made well-defined by adopting the regularization prescription

$$
\frac { \delta ( \pmb { x } - \pmb { r } _ { A } ) } { | \pmb { x } - \pmb { r } _ { A } | } \equiv 0 .
$$

The rule removes the offending term in $\rho ^ { * } U$ , and the piece of the Newtonian potential that survives multiplication by $\delta ( \pmb { x } - \pmb { r } _ { A } )$ is the partie finie displayed in Eq. (11.157). With this prescription, our expression for the effective mass density becomes

$$
c ^ { - 2 } \tau ^ { 0 0 } = \sum _ { A } M _ { A } \bigg ( 1 + \frac { v _ { A } ^ { 2 } } { 2 c ^ { 2 } } + \frac { 3 \lfloor U \rfloor _ { A } } { c ^ { 2 } } \bigg ) \delta \big ( { \pmb x } - { \pmb r } _ { A } \big ) - \frac { 1 4 } { 1 6 \pi G c ^ { 2 } } \partial _ { p } U \partial ^ { p } U + O ( c ^ { - 4 } ) .
$$

The radiative quadrupole moment can be decomposed as

$$
Q ^ { j k } = Q ^ { j k } [ { \bf M } ] + Q ^ { j k } [ { \bf F } ] + O ( c ^ { - 4 } ) .
$$

It contains a matter contribution that comes from the delta functions in $\tau ^ { 0 0 }$ , and a field contribution that comes from the term involving $\partial _ { p } U \partial ^ { p } U$ . The matter contribution can be

calculated at once:

$$
\mathcal { Q } ^ { j k } [ \mathbf { M } ] = \sum _ { A } M _ { A } \bigg ( 1 + \frac { v _ { A } ^ { 2 } } { 2 c ^ { 2 } } + \frac { 3 \lfloor U \rfloor _ { A } } { c ^ { 2 } } \bigg ) r _ { A } ^ { j } r _ { A } ^ { k } .
$$

The field contribution is

$$
Q ^ { j k } [ \mathrm { F } ] = - \frac { 1 4 } { 1 6 \pi G c ^ { 2 } } \int _ { \mathcal { M } } \partial _ { p } U \partial ^ { p } U x ^ { j } x ^ { k } d ^ { 3 } x ,
$$

and its computation requires a lot more work.

To evaluate the field integral of Eq. (11.163) we first express the integrand in the equivalent form

$$
\begin{array} { l } { { \partial _ { p } U \partial ^ { p } U x ^ { j } x ^ { k } = \partial _ { p } \big ( U \partial ^ { p } U x ^ { j } x ^ { k } \big ) - \displaystyle \frac { 1 } { 2 } \partial ^ { j } \big ( U ^ { 2 } x ^ { k } \big ) - \displaystyle \frac { 1 } { 2 } \partial ^ { k } \big ( U ^ { 2 } x ^ { j } \big ) } } \\ { { \phantom { \partial _ { p } U \partial ^ { p } U x ^ { j } x ^ { k } } + U ^ { 2 } \delta ^ { j k } - U ( \nabla ^ { 2 } U ) x ^ { j } x ^ { k } , } } \end{array}
$$

which allows us to integrate by parts. We may discard the term $U ^ { 2 } \delta ^ { j k }$ on the grounds that it will not survive the TT projection introduced in Sec. 11.1.7. We may also replace $\nabla ^ { 2 } U$ by $\begin{array} { r } { - 4 \pi G \sum _ { A } M _ { A } \delta ( { \pmb x } - { \pmb r } _ { A } ) } \end{array}$ , and write

$$
\begin{array} { r l } & { \displaystyle \int _ { \mathcal { M } } \partial _ { p } U \partial ^ { p } U x ^ { j } x ^ { k } d ^ { 3 } x \stackrel { \mathrm { \scriptsize ~ m ~ } } { = } \oint _ { \partial \mathcal { M } } U \partial ^ { p } U x ^ { j } x ^ { k } d S _ { p } - \oint _ { \partial \mathcal { M } } U ^ { 2 } x ^ { ( j } d S ^ { k ) } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad + 4 \pi G \sum _ { A } M _ { A } \lfloor U \rfloor _ { A } r _ { A } ^ { j } r _ { A } ^ { k } , } \end{array}
$$

where the notation $\stackrel { \pi } { = }$ was introduced near the end of Sec. 11.3.1, and where $d S ^ { j } =$ $\mathcal { R } ^ { 2 } N ^ { j } d \Omega$ is the surface element on $\partial \mathcal { M }$ . Note that we have once more made use of the regularization prescription of Eq. (11.159). Making the substitution, we obtain

$$
\begin{array} { l } { { \displaystyle Q ^ { j k } [ \mathrm { F } ] \stackrel { \pi } { = } - \frac { 7 } { 2 G c ^ { 2 } } \Big ( { \mathcal R } ^ { 4 } \langle \langle U \partial _ { p } U N ^ { j } N ^ { k } N ^ { p } \rangle \rangle - { \mathcal R } ^ { 3 } \langle \langle U ^ { 2 } N ^ { j } N ^ { k } \rangle \rangle \Big ) } } \\ { { \displaystyle ~ - \frac { 7 } { 2 c ^ { 2 } } \sum _ { A } M _ { A } \lfloor U \rfloor _ { A } r _ { A } ^ { j } r _ { A } ^ { k } , } } \end{array}
$$

in which the angular brackets denote an average over the unit two-sphere.

We must now evaluate the surface integrals, on which $_ { x }$ is set equal to $\mathcal { R } N$ . Recalling that $\mathcal { R }$ is large compared with $r _ { A }$ (refer to Sec. 11.3.2), it is appropriate to expand $U$ in inverse powers of $r : = | { \boldsymbol { x } } |$ before we insert it within the integrals. We have

$$
U = \frac { G m } { r } + \frac { 1 } { 2 } G I ^ { j k } \partial _ { j k } r ^ { - 1 } + { \cal O } ( r ^ { - 3 } ) ,
$$

where $\begin{array} { r } { m : = \sum _ { A } M _ { A } } \end{array}$ is the total mass, and $\begin{array} { r } { I ^ { j k } : = \sum _ { A } M _ { A } r _ { A } ^ { j } r _ { A } ^ { k } } \end{array}$ is the Newtonian quadrupole moment of the mass distribution. It is important to note that the Newtonian dipole moment, $\begin{array} { r } { I ^ { j } : = \sum _ { A } M _ { A } r _ { A } ^ { j } } \end{array}$ , has been set equal to zero. This is allowed, because $I = m R + O ( c ^ { - 2 } )$ , where $\pmb { R }$ is the post-Newtonian barycenter (refer to Sec. 9.3.6), and we work in a coordinate system for which $\pmb { R = 0 }$ . From the expansion of the Newtonian potential we also get

$$
\partial _ { j } U = G m \partial _ { j } r ^ { - 1 } + \frac { 1 } { 2 } G I ^ { k p } \partial _ { j k p } r ^ { - 1 } + { \cal O } ( r ^ { - 4 } ) .
$$

These results indicate that on $\partial \mathcal { M }$ , the potential and its gradient are given schematically by $U = \mathcal { R } ^ { - 1 } + \mathcal { R } ^ { - 3 } + \cdots$ and $\partial _ { j } U = \mathcal { R } ^ { - 2 } + \mathcal { R } ^ { - 4 } + \cdots .$ This implies, for example, that $\mathcal R ^ { 4 } U \partial _ { p } U = \mathcal R + \mathcal R ^ { - 1 } + \cdot \cdot \cdot$ and $\mathcal { R } ^ { 3 } U ^ { 2 } = \mathcal { R } + \mathcal { R } ^ { - 1 } + \cdots .$ . This reveals, finally, that the surface integrals produce no $\mathcal { R }$ -independent contributions to $\boldsymbol { Q } ^ { j k }$ [F].

We have obtained

$$
Q ^ { j k } [ \mathrm { F } ] \stackrel { \mathrm { \scriptsize { ~ \pi ~ } } } { = } - \frac { 7 } { 2 c ^ { 2 } } \sum _ { A } M _ { A } \lfloor U \rfloor _ { A } r _ { A } ^ { j } r _ { A } ^ { k } ,
$$

and combining this with Eq. (11.162), we conclude that the radiative quadrupole moment of Eq. (11.161) is indeed given by Eq. (11.156).

# 11.3.4 Radiative octupole moment

We turn next to computation of $\boldsymbol { Q } ^ { j k a }$ , the radiative octupole moment. According to Eq. (11.119), this is defined by

$$
\begin{array} { r } { Q ^ { j k a } : = A ^ { j k a } + A ^ { k j a } - A ^ { a j k } , } \end{array}
$$

where

$$
A ^ { j k a } ( \tau ) : = \frac { 1 } { c ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { 0 j } ( \tau , \pmb { x } ) x ^ { k } x ^ { a } d ^ { 3 } x .
$$

We show below that this is given by

$$
\begin{array} { l } { { d ^ { j k l } \ a ^ { \dagger \nu } \ } } \\ { { \ } } \\ { { d ^ { j k l } \ } } \\ { { \ } } \\ { { d ^ { j \nu } = \ } { \frac { 1 } { \mathcal { Z } ^ { j } } \sum _ { i } \ \sum _ { \beta \neq i } \ \biggl ( M _ { i } + { \frac { v _ { i } ^ { 2 } } { 2 \epsilon ^ { j } } } \biggr ) \sigma _ { i , i } ^ { j } A _ { i } ^ { \mu } A _ { j } ^ { \nu } } } \\ { { \ } } \\ { { \ } } \\ { { \displaystyle - \frac { 1 } { 2 \epsilon ^ { 3 } } \sum _ { i } \ \sum _ { \beta \neq i } \ \biggl ( M _ { i } M _ { j } \nu A _ { i } ^ { \mu } A _ { \mu } \biggr [ \biggl ( n _ { A \mu } \cdot v _ { i } ) \biggr ) \sigma _ { i , i } ^ { j } B _ { j } ^ { \mu } A _ { i } ^ { \nu } A _ { j } ^ { \alpha } + v _ { i } ^ { j } \mathcal { A } _ { j } ^ { \nu } A _ { i } ^ { \beta } \biggr ] } } \\ { { \ } } \\ { { \displaystyle + \frac { 1 } { 2 \epsilon ^ { 3 } } \sum _ { i } \ \sum _ { \beta \neq i } \ \biggl ( M _ { i } A _ { j } u _ { \mu } \biggr [ \biggl ( n _ { B \mu } \cdot v _ { i } ) \biggr ) \sigma _ { i , i } ^ { j } u _ { i } ^ { \alpha } A _ { j } ^ { \nu } u _ { i } ^ { \alpha } - \mathcal { D } _ { i } ^ { \mu } u _ { i } ^ { \alpha } u _ { i } ^ { \beta } } } \\ { { \ } } \\ { { \displaystyle + \mathcal { D } _ { i } ^ { j } u _ { \phi } ^ { \mu } \biggl ( u _ { \phi } ^ { \mu } \biggr ) \ } } \\ { { \ } } \\ { { \displaystyle - \frac { 1 } { 6 \epsilon ^ { 3 } } \sum _ { i } \ \sum _ { \beta \neq i } \ ( M _ { i } M _ { j } \nu A _ { \mu } ^ { \mu } \biggr [ \biggl ( n _ { A \mu } \cdot v _ { i } ) u _ { i } ^ { \mu } A _ { \mu } ^ { \nu } u _ { i } ^ { \alpha } \biggr ] } } \\ { { \ } } \\   \displaystyle + 1 1 v _ { i } ^ { j } u _ { \mu } ^ { \alpha } u _ { \lambda } ^ { \alpha } \biggr ) \ + \ ( v ^ { - \alpha } ) \mathcal { R } _ { i } ^ { \mu } \end{array}
$$

This expression leaves out terms that would not survive a transverse-tracefree projection, as well as $\mathcal { R }$ -dependent terms that can be freely discarded. It is understood that the position vectors $r _ { A }$ and the velocity vectors ${ \pmb v } _ { A }$ are evaluated at retarded time $\tau$ .

# Matter and field contributions

According to the discussion of Sec. 11.3.1, to calculate $\boldsymbol { Q } ^ { j k a }$ to the required degree of accuracy we need an expression for $c ^ { - 2 } \tau ^ { 0 j }$ that includes terms of order $c ^ { - 1 }$ (0.5pn) and terms of order $c ^ { - 3 }$ (1.5pn). Such an expression was worked out in Sec. 7.3.1 in the case of a matter distribution that consists of a perfect fluid. According to Eq. (7.54b), we have that

$$
\begin{array} { l } { { \displaystyle c ^ { - 2 } \tau ^ { 0 j } = \frac { 1 } { c } \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } \biggr ) \biggr ] } } \\ { { \displaystyle ~ + \frac { 1 } { 4 \pi G c ^ { 3 } } \biggl [ 3 \partial _ { t } U \partial ^ { j } U + 4 \bigl ( \partial ^ { j } U ^ { k } - \partial ^ { k } U ^ { j } \bigr ) \partial _ { k } U \biggr ] + { \cal O } ( c ^ { - 5 } ) . } } \end{array}
$$

For a system of point particles, $\begin{array} { r } { U ^ { j } = \sum _ { B } G M _ { B } v _ { B } ^ { j } / | \pmb { x } - \pmb { r } _ { B } | } \end{array}$ . Our expression for $c ^ { - 2 } \tau ^ { 0 j }$ must be regularized with the help of Eq. (11.159), and the end result is

$$
\begin{array} { l } { { \displaystyle c ^ { - 2 } \tau ^ { 0 j } = \frac { 1 } { c } \sum _ { A } M _ { A } { \upsilon } _ { A } ^ { j } \bigg ( 1 + \frac { { \upsilon } _ { A } ^ { 2 } } { 2 c ^ { 2 } } + \frac { 3 \lfloor U \rfloor _ { A } } { c ^ { 2 } } \bigg ) \delta \big ( { \pmb x } - { \pmb r } _ { A } \big ) } } \\ { { \displaystyle ~ + \frac { 1 } { 1 6 \pi G c ^ { 3 } } \bigg [ 1 2 \partial _ { t } U \partial ^ { j } U + 1 6 \big ( \partial ^ { j } U ^ { k } - \partial ^ { k } U ^ { j } \big ) \partial _ { k } U \bigg ] + { \cal O } ( c ^ { - 5 } ) } , } \end{array}
$$

where $\lfloor U \rfloor _ { A }$ is the partie finie of the Newtonian potential evaluated at $\mathbf { \boldsymbol { x } } = \mathbf { \boldsymbol { r } } _ { A }$ , as given by Eq. (11.157).

The octupole moment contains a contribution ${ \cal Q } ^ { j k a } [ \mathbf { M } ]$ that comes directly from the matter distribution, and another contribution $\boldsymbol { Q } ^ { j k a }$ [F] that comes from the gravitational field. They are obtained from $A ^ { j k a } = A ^ { j k a } [ { \bf M } ] + A ^ { j k a } [ { \bf F } ] + O ( c ^ { - 5 } )$ , which is then substituted into Eq. (11.170). We have introduced

$$
A ^ { j k a } [ { \bf M } ] : = { \frac { 1 } { c } } \sum _ { A } M _ { A } v _ { A } ^ { j } \bigg ( 1 + { \frac { v _ { A } ^ { 2 } } { 2 c ^ { 2 } } } + { \frac { 3 \lfloor U \rfloor _ { A } } { c ^ { 2 } } } \bigg ) r _ { A } ^ { k } r _ { A } ^ { a }
$$

and

$$
{ \cal A } ^ { j k a } [ \mathrm { F } ] : = \frac { 1 } { 4 \pi G c ^ { 3 } } \int _ { \mathcal { M } } \biggl [ 3 \partial _ { t } U \partial ^ { j } U + 4 \bigl ( \partial ^ { j } U ^ { p } - \partial ^ { p } U ^ { j } \bigr ) \partial _ { p } U \biggr ] x ^ { k } x ^ { a } d ^ { 3 } x ,
$$

and the remainder of this subsection is devoted to computation of $A ^ { j k a }$ [F].

# Computation of the field integral: Organization

To simplify our computations we invoke the identity of Eq. (7.40),

$$
\partial _ { t } U + \partial _ { j } U ^ { j } = 0 .
$$

We recall that this is a direct consequence of the statement of mass conservation, ${ \partial _ { t } } { \rho ^ { * } } +$ $\partial _ { j } ( \rho ^ { * } v ^ { j } ) = 0$ . We use the identity to eliminate $\partial _ { t } U$ from Eq. (11.176), which becomes

$$
A ^ { j k a } [ \mathrm { F } ] = \frac { 1 } { G c ^ { 3 } } \Bigl ( - 3 B _ { 1 } ^ { j k a } + 4 B _ { 2 } ^ { j k a } - 4 B _ { 3 } ^ { j k a } \Bigr ) ,
$$

where

$$
\begin{array} { r l r } & { } & { B _ { 1 } ^ { j k a } : = \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \partial ^ { j } U \partial _ { p } U ^ { p } x ^ { k } x ^ { a } d ^ { 3 } x , } \\ & { } & { B _ { 2 } ^ { j k a } : = \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \partial _ { p } U \partial ^ { j } U ^ { p } x ^ { k } x ^ { a } d ^ { 3 } x , } \\ & { } & { B _ { 3 } ^ { j k a } : = \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \partial _ { p } U \partial ^ { p } U ^ { j } x ^ { k } x ^ { a } d ^ { 3 } x . } \end{array}
$$

After integration by parts, which is designed to leave one factor of $U$ undifferentiated, we find that each field integral $B ^ { j k a }$ breaks up into a volume integral $B ^ { j k a } [ \mathcal { M } ]$ and a surface integral $B ^ { j k a } [ \partial \mathcal { M } ]$ . A number of terms are found to be proportional to $\delta ^ { j k }$ , or $\delta ^ { j a }$ , or $\delta ^ { k a }$ . All such terms will not survive a transverse-tracefree projection, and according to our discussion near the end of Sec. 11.3.1, they can all be discarded. If, for example, $B ^ { j k a }$ contains a term $\delta ^ { j k } B ^ { a }$ , then its contribution to $\boldsymbol { Q } ^ { j k a }$ will be of the form $2 \delta ^ { j k } B ^ { a } - \delta ^ { j a } B ^ { k }$ . The first term is a pure trace, and the second term is longitudinal, because it becomes proportional to $N ^ { j }$ after $\boldsymbol { Q } ^ { j k a }$ is multiplied by $N _ { a }$ ; in each case the contribution does not survive the TT projection.

After eliminating all such terms, we find that

$$
\begin{array} { r l r } {  { B _ { 1 } ^ { \jmath \kappa a } \overset { \vartriangle } { = } B _ { 1 } ^ { \jmath \kappa a } [ \mathcal { M } ] + B _ { 1 } ^ { \jmath \kappa a } [ \partial \mathcal { M } ] , } } \\ & { } & \\ & { } & { B _ { 1 } ^ { \jmath k a } [ \mathcal { M } ] : = - \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } U \partial _ { p } ^ { \jmath } U ^ { p } x ^ { k } x ^ { a } d ^ { 3 } x , } \\ & { } & \\ & { } & { B _ { 1 } ^ { \jmath k a } [ \partial \mathcal { M } ] : = \displaystyle \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } U \partial _ { p } U ^ { p } x ^ { k } x ^ { a } d S ^ { j } , \qquad } \end{array}
$$

that

$$
\begin{array} { c } { { \displaystyle B _ { 2 } ^ { j k a } \stackrel { \pi } { = } B _ { 2 } ^ { j k a } [ \mathcal { M } ] + B _ { 2 } ^ { j k a } [ \partial \mathcal { M } ] , } } \\ { { \displaystyle B _ { 2 } ^ { j k a } [ \mathcal { M } ] : = - \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } U \big ( \partial _ { p } ^ { j } U ^ { p } x ^ { k } x ^ { a } + \partial ^ { j } U ^ { k } x ^ { a } + \partial ^ { j } U ^ { a } x ^ { k } \big ) d ^ { 3 } x , } } \\ { { \displaystyle B _ { 2 } ^ { j k a } [ \partial \mathcal { M } ] : = \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } U \partial ^ { j } U ^ { p } x ^ { k } x ^ { a } d S _ { p } , } } \end{array}
$$

and that

$$
\begin{array} { r l } & { \qquad B _ { 3 } ^ { j k a } \stackrel { \mathtt { m } } { = } B _ { 3 } ^ { j k a } [ \mathcal { M } ] + B _ { 3 } ^ { j k a } [ \partial \mathcal { M } ] , } \\ & { B _ { 3 } ^ { j k a } [ \mathcal { M } ] : = - \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } U \big ( \nabla ^ { 2 } U ^ { j } x ^ { k } x ^ { a } + \partial ^ { k } U ^ { j } x ^ { a } + \partial ^ { a } U ^ { j } x ^ { k } \big ) d ^ { 3 } x , } \\ & { B _ { 3 } ^ { j k a } [ \partial \mathcal { M } ] : = \displaystyle \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } U \partial ^ { p } U ^ { j } x ^ { k } x ^ { a } d S _ { p } . } \end{array}
$$

There are many volume integrals to evaluate, but they are all of the form

$$
C ^ { m n p a b } : = - \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } U \partial ^ { m n } U ^ { p } x ^ { a } x ^ { b } d ^ { 3 } x
$$

and

$$
D ^ { m n a } : = - \frac { 1 } { 4 \pi } \int _ { \mathcal M } U \partial ^ { m } U ^ { n } x ^ { a } d ^ { 3 } x .
$$

Specifically,

$$
\begin{array} { r l } & { B _ { 1 } ^ { j k a } [ \mathcal { M } ] = C _ { \textit { p } } ^ { j \textit { p k a } } , } \\ & { B _ { 2 } ^ { j k a } [ \mathcal { M } ] = C _ { \textit { p } } ^ { j \textit { p k a } } + D ^ { j k a } + D ^ { j a k } , } \\ & { B _ { 3 } ^ { j k a } [ \mathcal { M } ] = C _ { \textit { p } } ^ { p \textit { j k a } } + D ^ { k j a } + D ^ { a j k } . } \end{array}
$$

Similarly, the surface integrals are of the form

$$
E ^ { m n a b p } : = \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } U \partial ^ { m } U ^ { n } x ^ { a } x ^ { b } d S ^ { p } ,
$$

with

$$
B _ { 1 } ^ { j k a } [ \partial \mathcal { M } ] = E _ { p } ^ { \ p k a j } , \quad B _ { 2 } ^ { j k a } [ \partial \mathcal { M } ] = E ^ { j p k a } { } _ { p } , \quad B _ { 3 } ^ { j k a } [ \partial \mathcal { M } ] = E ^ { p j k a } { } _ { p } .
$$

The key is therefore the evaluation of the generic volume integrals of Eqs. (11.183) and (11.184), as well as the surface integral of Eq. (11.186). Once these are in hand, the computation of $B _ { 1 } ^ { j k a } , B _ { 2 } ^ { j k a }$ , and $B _ { 3 } ^ { j k a }$ is soon completed, and Eq. (11.178) gives us $A ^ { j k a }$ [F]. Adding the $A ^ { j k a } [ \mathrm { M } ]$ of Eq. (11.175) produces $A ^ { j k a }$ , and from Eq. (11.170) we get our final answer for $\boldsymbol { Q } ^ { j k a }$ .

# Computation of Cmnpab

We follow the general methods described in Sec. 11.3.2. We begin with the differentiation of the vector potential $\begin{array} { r } { U ^ { p } = \sum _ { B } G M _ { B } v _ { B } ^ { p } / | { \pmb x } - { \pmb r } _ { B } | } \end{array}$ , which returns

$$
\begin{array} { c } { { \partial ^ { m n } U ^ { p } = - \displaystyle \sum _ { B } G { \cal M } _ { B } v _ { B } ^ { p } \displaystyle \biggl [ - 3 \displaystyle \frac { ( x - r _ { B } ) ^ { m } ( x - r _ { B } ) ^ { n } } { | x - r _ { B } | ^ { 5 } } + \displaystyle \frac { \delta ^ { m n } } { | x - r _ { B } | ^ { 3 } } } } \\ { { + \displaystyle \frac { 4 \pi } { 3 } \delta ^ { m n } \delta ( x - r _ { B } ) \biggr ] . } } \end{array}
$$

The last term, involving the delta function, does not appear in a straightforward computation of $\partial ^ { m n } U ^ { p }$ , in which one implicitly assumes that $\boldsymbol { x } \neq \boldsymbol { r } _ { B }$ . Without it, however, our expression would be wrong, because it would give rise to $\nabla ^ { 2 } U ^ { p } = 0$ instead of the correct $\begin{array} { r } { \nabla ^ { 2 } U ^ { p } = - 4 \pi G \sum _ { B } M _ { B } \boldsymbol { v } _ { B } ^ { p } \delta ( { \boldsymbol { x } } - { \boldsymbol { r } } _ { B } ) } \end{array}$ . The distributional term is therefore inserted to produce the correct answer when $\mathbf { \boldsymbol { x } } = \boldsymbol { r } _ { B }$ , and to ensure that $U ^ { p }$ satisfies the appropriate Poisson equation. After insertion of $\begin{array} { r } { U = \sum _ { A } G M _ { A } / | \pmb { x } - \pmb { r } _ { A } | } \end{array}$ and some algebra, Eq. (11.183) becomes

$$
\begin{array} { l } { { { \cal C } ^ { m n p a b } = \displaystyle \sum _ { A } G ^ { 2 } { \cal M } _ { A } ^ { 2 } v _ { A } ^ { p } \Big ( \delta ^ { m n } F _ { A } ^ { a b } - 3 F _ { A } ^ { m n a b } \Big ) } } \\ { { { } } } \\ { { \displaystyle ~ + \sum _ { A } \sum _ { B \not = A } G ^ { 2 } { \cal M } _ { A } { \cal M } _ { B } v _ { B } ^ { p } \Bigg ( \delta ^ { m n } F _ { A B } ^ { a b } - 3 F _ { A B } ^ { m n a b } + \frac { 1 } { 3 } \delta ^ { m n } \frac { r _ { B } ^ { a } r _ { B } ^ { b } } { r _ { A B } } \Bigg ) , } } \end{array}
$$

where

$$
\begin{array} { l } { { F _ { \cal A } ^ { m n a b } : = \displaystyle \frac { 1 } { 4 \pi } \int _ { \cal { M } } \displaystyle \frac { ( x - r _ { \cal A } ) ^ { m } ( x - r _ { \cal A } ) ^ { n } } { | x - r _ { \cal A } | ^ { 6 } } x ^ { a } x ^ { b } d ^ { 3 } x \ : , } } \\ { { F _ { \cal A B } ^ { m n a b } : = \displaystyle \frac { 1 } { 4 \pi } \int _ { \cal { M } } \displaystyle \frac { 1 } { | x - r _ { \cal A } | } \displaystyle \frac { ( x - r _ { \cal B } ) ^ { m } ( x - r _ { \cal B } ) ^ { n } } { | x - r _ { \cal B } | ^ { 5 } } x ^ { a } x ^ { b } d ^ { 3 } x \ : , } } \end{array}
$$

and where

$$
F _ { A } ^ { a b } : = \delta _ { m n } F _ { A } ^ { m n a b } , \qquad F _ { A B } ^ { a b } : = \delta _ { m n } F _ { A B } ^ { m n a b } .
$$

The term involving $r _ { B } ^ { a } r _ { B } ^ { b } / r _ { A B }$ in Eq. (11.189) originates from the distributional term in $\partial ^ { m n } U ^ { p }$ ; a similar term involving $r _ { A } ^ { a } r _ { A } ^ { b } / r _ { A A }$ was set equal to zero by invoking the regularization prescription of Eq. (11.159).

We first set to work on $F _ { A } ^ { m n a b }$ . Following the general strategy summarized in Box 11.3, we substitute $\pmb { x } = \pmb { y } + \pmb { r } _ { A }$ inside the integral, and get

$$
\begin{array} { r } { F _ { A } ^ { m n b c } = \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { y ^ { m } y ^ { n } y ^ { a } y ^ { b } } { y ^ { 6 } } d ^ { 3 } y + \frac { r _ { B } ^ { a } } { 4 \pi } \int _ { \mathcal { M } } \frac { y ^ { m } y ^ { n } y ^ { b } } { y ^ { 6 } } d ^ { 3 } y } \\ { + \frac { r _ { B } ^ { b } } { 4 \pi } \displaystyle \int _ { \mathcal { M } } \frac { y ^ { m } y ^ { n } y ^ { a } } { y ^ { 6 } } d ^ { 3 } y + \frac { r _ { B } ^ { a } r _ { B } ^ { b } } { 4 \pi } \displaystyle \int _ { \mathcal { M } } \frac { y ^ { m } y ^ { n } } { y ^ { 6 } } d ^ { 3 } y . } \end{array}
$$

According to Eq. (1) of Box 11.3, each integral over $\mathcal { M }$ can be expressed as a volume integral over the simpler domain $\mathcal { M } _ { y }$ defined by $y : = | { \mathbf { y } } | < \mathcal { R }$ , plus a correction of fractional order $| r _ { B } | / \mathcal { R }$ given by a surface integral over $\partial \mathcal { M } _ { y }$ .

The first integral produces

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { y ^ { m } y ^ { n } y ^ { a } y ^ { b } } { y ^ { 6 } } d ^ { 3 } y = \langle \langle N ^ { m } N ^ { n } N ^ { a } N ^ { b } \rangle \rangle \int _ { 0 } ^ { \mathcal { R } } d y } \\ & { \quad \quad \quad \quad \quad = \displaystyle \frac { 1 } { 1 5 } { \mathcal { R } } \big ( \delta ^ { m n } \delta ^ { a b } + \delta ^ { m a } \delta ^ { n b } + \delta ^ { m b } \delta ^ { n a } \big ) , } \end{array}
$$

where we involve Eq. (4d) of Box 11.3. Because it is proportional to $\mathcal { R }$ , this contribution to $F _ { A } ^ { m n a b }$ can be discarded. The surface integral that corrects this will potentially give rise to an $\mathcal { R }$ -independent contribution, and it should be evaluated carefully. It turns out, however, that it is proportional to $r _ { B } ^ { p } \langle \langle N ^ { m } N ^ { n } N ^ { a } N ^ { b } N _ { p } \rangle \rangle$ , and it vanishes because the angular average of a product of an odd number of vectors $N$ is necessarily zero. The neglected terms in Eq. (1) are of order $\mathcal { R } ^ { - 1 }$ and higher, and we conclude that the first integral in $F _ { A } ^ { m n a b }$ makes no contribution to Cmnpab.

The second and third integrals produce terms such as

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { y ^ { m } y ^ { n } y ^ { b } } { y ^ { 6 } } d ^ { 3 } y = \langle \langle N ^ { m } N ^ { n } N ^ { b } \rangle \rangle \int _ { 0 } ^ { \mathcal { R } } \frac { d y } { y } ,
$$

and this vanishes by virtue of Eq. (4c) of Box 11.3; the logarithmic divergence of the radial integration requires no explicit regularization. The surface integral that corrects this

is easily shown to be of order $\mathcal { R } ^ { - 1 }$ , and we conclude that the second and third integrals do not contribute to Cmnpab.

The fourth integral produces

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { y ^ { m } y ^ { n } } { y ^ { 6 } } d ^ { 3 } y = \langle \langle N ^ { m } N ^ { n } \rangle \rangle \int _ { 0 } ^ { \mathcal { R } } \frac { d y } { y ^ { 2 } } = \frac { 1 } { 3 } \delta ^ { m n } \int _ { 0 } ^ { \mathcal { R } } \frac { d y } { y ^ { 2 } } ,
$$

and this involves a radial integration that is formally divergent. Once more the surface integral does not contribute, and we have obtained

$$
F _ { A } ^ { m n a b } = \frac { 1 } { 3 } \delta ^ { m n } r _ { A } ^ { a } r _ { A } ^ { b } \int _ { 0 } ^ { \mathcal { R } } \frac { d y } { y ^ { 2 } }
$$

for the field integral of Eq. (11.190), modulo $\mathcal { R }$ -dependent terms that can be freely discarded. It is disturbing to see that $F _ { A } ^ { m n a b }$ is proportional to a diverging integral, but it is a fortunate outcome that the combination $\delta ^ { m n } F _ { A } ^ { a b } - 3 F _ { A } ^ { m n a b }$ that appears in $C ^ { m n p a b }$ happens to vanish identically. The divergence does not require explicit regularization, and all in all we find that $F _ { A } ^ { m n a b }$ makes no contribution to $C ^ { m n p a b }$ .

We next set to work on $F _ { A B } ^ { m n a b }$ . Once more we follow the general strategy summarized in Box 11.3, and we substitute $\pmb { x } = \pmb { y } + \pmb { r } _ { B }$ inside the integral. We get

$$
\begin{array} { c } { { F _ { A B } ^ { m n b c } = \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \displaystyle \frac { 1 } { | y - r _ { A B } | } \displaystyle \frac { y ^ { m } y ^ { n } y ^ { a } y ^ { b } } { y ^ { 5 } } d ^ { 3 } y + \displaystyle \frac { r _ { B } ^ { a } } { 4 \pi } \int _ { \mathcal { M } } \displaystyle \frac { 1 } { | y - r _ { A B } | } \displaystyle \frac { y ^ { m } y ^ { n } y ^ { b } } { y ^ { 5 } } d ^ { 3 } y } } \\ { { + \displaystyle \frac { r _ { B } ^ { b } } { 4 \pi } \int _ { \mathcal { M } } \displaystyle \frac { 1 } { | y - r _ { A B } | } \displaystyle \frac { y ^ { m } y ^ { n } y ^ { a } } { y ^ { 5 } } d ^ { 3 } y + \displaystyle \frac { r _ { B } ^ { a } r _ { B } ^ { b } } { 4 \pi } \displaystyle \int _ { \mathcal { M } } \displaystyle \frac { 1 } { | y - r _ { A B } | } \displaystyle \frac { y ^ { m } y ^ { n } } { y ^ { 5 } } d ^ { 3 } y . } } \end{array}
$$

We begin with the first integral, which produces

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - \pmb { r } _ { A B } | } \frac { y ^ { m } y ^ { n } y ^ { a } y ^ { b } } { y ^ { 5 } } d ^ { 3 } y .
$$

To evaluate this we involve Eq. (2) of Box 11.3, and we express $N ^ { m } N ^ { n } N ^ { a } N ^ { b }$ as

$$
\begin{array} { c } { { N ^ { m } N ^ { n } N ^ { a } N ^ { b } = N ^ { \langle m n a b \rangle } + \displaystyle { \frac { 1 } { 7 } \Big ( \delta ^ { m n } N ^ { \langle a b \rangle } + \delta ^ { m a } N ^ { \langle n b \rangle } + \delta ^ { m b } N ^ { \langle n a \rangle } + \delta ^ { n a } N ^ { \langle m b \rangle } } } } \\ { { + \ \delta ^ { n b } N ^ { \langle m a \rangle } + \delta ^ { a b } N ^ { \langle m n \rangle } \Big ) + \displaystyle { \frac { 1 } { 1 5 } \Big ( \delta ^ { m n } \delta ^ { a b } + \delta ^ { m a } \delta ^ { n b } + \delta ^ { m b } \delta ^ { n a } \Big ) } , } } \end{array}
$$

in terms of the angular STF tensors $N ^ { \langle m n a b \rangle }$ and $N ^ { \langle m n \rangle }$ . We perform the angular integrations with the help of Eq. (3) of Box 11.3, and the remaining radial integrals are in the form of Eq. (5). After some algebra, we obtain the expression

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { 9 } K ( 4 , 1 ) n _ { A B } ^ { \langle m n a b \rangle } + \frac { 1 } { 3 5 } K ( 2 , 1 ) \Big ( \delta ^ { m n } n _ { A B } ^ { \langle a b \rangle } + \mathrm { p e r m u t a t i o n s } \Big ) } } \\ { { + \displaystyle \frac { 1 } { 1 5 } K ( 0 , 1 ) \Big ( \delta ^ { m n } \delta ^ { a b } + \delta ^ { m a } \delta ^ { n b } + \delta ^ { m b } \delta ^ { n a } \Big ) } } \end{array}
$$

for the volume integral. The corresponding surface integral is easily seen to be of order $\mathcal { R } ^ { - 1 }$ , and we arrive at

$$
\begin{array} { c }  { { \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - r _ { A B } | } \frac { y ^ { m } y ^ { n } y ^ { a } y ^ { b } } { y ^ { 5 } } d ^ { 3 } y = \displaystyle \frac { 1 } { 1 8 } r _ { A B } n _ { A B } ^ { \langle m n a b \rangle } + \displaystyle \frac { 1 } { 2 8 } r _ { A B } \Big ( \delta ^ { m n } n _ { A B } ^ { \langle a b \rangle } + \delta ^ { m a } n _ { A B } ^ { \langle n b \rangle } } } \\ { { { \displaystyle + \delta ^ { m b } n _ { A B } ^ { \langle a a \rangle } + \delta ^ { n a } n _ { A B } ^ { \langle m b \rangle } + \delta ^ { n b } n _ { A B } ^ { \langle m a \rangle } + \delta ^ { a b } n _ { A B } ^ { \langle m n \rangle } \Big ) } } } \\ { { { - \displaystyle \frac { 1 } { 3 0 } r _ { A B } \Big ( \delta ^ { m n } \delta ^ { a b } + \delta ^ { m a } \delta ^ { n b } + \delta ^ { m b } \delta ^ { n a } \Big ) \qquad ( 1 1 . 1 9 9 ) } } } \end{array}
$$

after using Eq. (5) of $\operatorname { B o x } 1 1 . 3$ to evaluate the radial integrals.

We next turn to the second and third integrals, which are both approximated by

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - \pmb { r } _ { A B } | } \frac { y ^ { m } y ^ { n } y ^ { a } } { y ^ { 5 } } d ^ { 3 } y .
$$

To evaluate this we involve Eq. (2), and we express $N ^ { m } N ^ { n } N ^ { a }$ as

$$
N ^ { m } N ^ { n } N ^ { a } = N ^ { \langle m n a \rangle } + \frac { 1 } { 5 } \Big ( \delta ^ { m n } N ^ { a } + \delta ^ { m a } N ^ { n } + \delta ^ { n a } N ^ { m } \Big ) ,
$$

in terms of the angular STF tensor $N ^ { \langle m n a \rangle }$ . We carry out the angular integrations with the help of Eq. (3), and the remaining radial integrals are in the form of Eq. (5). After some algebra, we obtain the expression

$$
\frac { 1 } { 7 } K ( 3 , 0 ) n _ { A B } ^ { \langle m n a \rangle } + \frac { 1 } { 1 5 } K ( 1 , 0 ) \bigg ( \delta ^ { m n } n _ { A B } ^ { a } + \delta ^ { m a } n _ { A B } ^ { n } + \delta ^ { n a } n _ { A B } ^ { m } \bigg )
$$

for the volume integral. The corresponding surface integral is once more of order $\mathcal { R } ^ { - 1 }$ , and we arrive at

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - r _ { \mathit { A B } } | } \frac { y ^ { m } y ^ { n } y ^ { a } } { y ^ { 5 } } d ^ { 3 } y = \frac { 1 } { 1 2 } n _ { \mathit { A B } } ^ { \langle m n a \rangle } + \frac { 1 } { 1 0 } \Big ( \delta ^ { m n } n _ { \mathit { A B } } ^ { a } + \delta ^ { m a } n _ { \mathit { A B } } ^ { n } + \delta ^ { n a } n _ { \mathit { A B } } ^ { m } \Big )
$$

after using Eq. (5) to evaluate the radial integrals.

The final step in the computation of $F _ { A B } ^ { m n a b }$ is the evaluation of the fourth integral, which is approximated by

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } _ { y } } \frac { 1 } { | y - \pmb { r } _ { A B } | } \frac { y ^ { m } y ^ { n } } { y ^ { 5 } } d ^ { 3 } y .
$$

After following the same familiar steps, this becomes ${ \textstyle \frac { 1 } { 5 } } K ( 2 , - 1 ) n _ { A B } ^ { \langle m n \rangle } + { \textstyle \frac { 1 } { 3 } } K ( 0 , - 1 ) \delta ^ { m n }$ , and the corresponding surface integral is of order $\mathcal { R } ^ { - 2 }$ . We arrive at

$$
\frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { 1 } { | y - \boldsymbol { r } _ { A B } | } \frac { y ^ { m } y ^ { n } } { y ^ { 5 } } d ^ { 3 } y = \frac { 1 } { 6 r _ { A B } } n _ { A B } ^ { \langle m n \rangle } + \frac { 1 } { 3 } K ( 0 , - 1 ) \delta ^ { m n } ,
$$

and we note that $K ( 0 , - 1 )$ is formally a divergent integral of the sort encountered in Eq. (11.196). We shall see that this divergence requires no explicit regularization, because (as happened before) it eventually drops out of the calculation.

Collecting results, we have obtained

$$
\begin{array} { r l r } { { F _ { 4 B } ^ { \prime \prime \alpha \alpha \beta \alpha \beta } = \displaystyle \frac { 1 } { 1 8 } F _ { 4 B } ^ { \prime \prime } N _ { 4 B } ^ { ( m a \beta ) } } } \\ { { } } & { { + \displaystyle \frac { 1 } { 2 8 } r _ { A \beta } \left( \sin ^ { \alpha m } n _ { A \beta } ^ { ( a \beta ) } + \delta ^ { m a } n _ { \dot { A } B } ^ { ( a \beta ) } + \delta ^ { m b } n _ { \dot { A } B } ^ { ( m a ) } + \delta ^ { m a } n _ { \dot { A } B } ^ { ( m b ) } + \delta ^ { B b } n _ { \dot { A } B } ^ { ( m a ) } + \delta ^ { a b } n _ { \dot { A } B } ^ { ( m a ) } \right) } } \\ { { } } & { { - \displaystyle \frac { 1 } { 3 0 } r _ { A \alpha } \left( \delta ^ { m a } \delta ^ { \alpha b } + \delta ^ { m a } \delta ^ { \dot { B } b } + \delta ^ { m b } \delta ^ { \alpha a } \right) } } \\ { { } } & { { + \displaystyle \frac { 1 } { 1 2 } n _ { A \dot { A } } ^ { ( m a ) } r _ { \dot { B } } ^ { \dot { b } } + \frac { 1 } { 1 0 } \left( \delta ^ { m m } n _ { \dot { A } B } ^ { a } + \delta ^ { m a } n _ { \dot { A } B } ^ { m } + \delta ^ { m m } n _ { \dot { A } B } ^ { m } \right) r _ { \dot { B } } ^ { b } } } \\ { { } } & { { + \displaystyle \frac { 1 } { 1 2 } n _ { A \dot { A } } ^ { ( m b ) } r _ { \dot { B } } ^ { a } + \frac { 1 } { 1 0 } \left( \delta ^ { m m } n _ { \dot { A } B } ^ { b } + \delta ^ { m b } n _ { \dot { A } B } ^ { m } + \delta ^ { m b } n _ { \dot { A } B } ^ { m } \right) r _ { \dot { B } } ^ { a } } } \\ { { } } &  { + \displaystyle \frac { 1 } { 6 r _ { A \dot { A } B } } r _ { \dot { B } } ^ { ( m b ) } r _ { \dot { B } } ^ { a } + \frac { 1 } { 3 } K ( 0 , - 1 ) \delta ^ { m m } r _ { \dot { A } B } ^ { a } P _ { \dot { B } } } \\ { { } } &   + \displaystyle \frac { 1 } { 6 r _ { A \dot { A } B } } r _ { \dot { B } } ^ { ( m b ) } r _  \end{array}
$$

for the field integral of Eq. (11.190), modulo $\mathcal { R }$ -dependent terms that can be freely discarded. The trace of this is

$$
F _ { A B } ^ { a b } = \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { \langle a b \rangle } - \frac { 1 } { 6 } r _ { A B } \delta ^ { a b } + \frac { 1 } { 2 } n _ { A B } ^ { a } r _ { B } ^ { b } + \frac { 1 } { 2 } n _ { A B } ^ { b } r _ { B } ^ { a } + K ( 0 , - 1 ) r _ { B } ^ { a } r _ { B } ^ { b } ,
$$

and we see that, as claimed, the terms involving $K ( 0 , - 1 )$ cancel out in the combination $\delta ^ { m n } F _ { A B } ^ { a b } - 3 F _ { A B } ^ { m n a b }$ that appears in Eq. (11.189); these terms make no contribution to $C ^ { m n p a b }$

We may now substitute Eqs. (11.196), (11.203), and (11.204) into Eq. (11.189). After simplification, our final result is

$$
\begin{array} { l l } { { C ^ { m n p b } = \displaystyle { \sum _ { i } ^ { } \sum _ { \tilde { \theta } , i , \tilde { \theta } ^ { i } } 2 ^ { \nu } M _ { i } M _ { \tilde { \theta } } ^ { \nu } \nu _ { i } ^ { p } \bigg [ - \frac 1 6 T _ { i } \delta \tilde { \theta } ^ { \nu _ { i } } M _ { i } ^ { \nu \tilde { \theta } } } } } \\ { { } } & { { \mathrm { } -  \frac 3 3 T _ { i } \delta ( \tilde { \theta } ^ { \nu _ { i } } \alpha _ { i , \tilde { \theta } } ^ { \nu \tilde { \theta } \tilde { \theta } \tilde { \theta } } ) + \tilde { \theta } ^ { \nu _ { i } } \alpha _ { i , \tilde { \theta } } ^ { \nu \tilde { \theta } \tilde { \theta } \tilde { \theta } } + \tilde { \delta } ^ { \mu n } n _ { i } ^ { ( \mu \nu _ { i } ) } + \tilde { \delta } ^ { \mu \nu } n _ { i } ^ { ( \mu \nu _ { i } ) } + \tilde { \delta } ^ { \mu \nu } n _ { i } ^ { ( \mu \nu _ { i } ) } ) } } \\ { { } } & { { \mathrm { } + r _ { i } \delta ^ { \nu m } ( \frac 1 7 \alpha _ { i , \tilde { \theta } } ^ { \nu \tilde { \theta } \tilde { \theta } } - \frac 1 { 1 5 } \alpha ^ { \mu \tilde { \theta } \tilde { \theta } } ) + \frac 1 { 1 0 } r _ { i } \delta ( \tilde { \theta } ^ { \nu _ { i } } \alpha _ { i } ^ { \nu \tilde { \theta } \tilde { \theta } } + \tilde { \delta } ^ { m b } \tilde { \phi } ^ { \nu \tilde { \theta } \tilde { \theta } } ) } } \\ { { } } &  { \mathrm { } - \frac 1 4 \sigma _ { i , \tilde { \theta } } ^ { ( m n ) \nu } r _ { \tilde { \theta } } ^ { \mathrm { } } - \frac 1 4 n _ { i } ^ { ( m b ) } \nu _ { \tilde { \theta } } ^ { \mathrm { } } - \frac 3 { 1 0 } ( \delta ^ { m } n _ { i } ^ { n } \alpha _ { i , \tilde { \theta } } ^ { \nu \tilde { \theta } } + \delta ^ { m } n _ { i } ^ { \pi } ) r _ { \tilde { \theta } } ^ { \mathrm { } } } \\ { { } } &  { } - \frac 3 { 1 0 } ( \delta ^ { m } n _ { i , \tilde { \theta } } ^  \nu \tilde  \theta \end{array}
$$

# Computation of $D ^ { m n a }$

After inserting the expressions for $U$ and $U ^ { n }$ within Eq. (11.184), we obtain

$$
D ^ { m n a } = \sum _ { A } G ^ { 2 } M _ { A } ^ { 2 } v _ { A } ^ { n } E _ { A } ^ { m a } + \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } v _ { B } ^ { n } E _ { A B } ^ { m a } ,
$$

where

$$
\begin{array} { l } { { \displaystyle E _ { A } ^ { m a } : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { ( x - r _ { A } ) ^ { m } x ^ { a } } { | x - r _ { A } | ^ { 4 } } d ^ { 3 } x , } } \\ { { \displaystyle E _ { A B } ^ { m a } : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { ( x - r _ { B } ) ^ { m } x ^ { a } } { | x - r _ { A } | | x - r _ { B } | ^ { 3 } } d ^ { 3 } x , } } \end{array}
$$

were introduced back in Eqs. (11.127). These integrals were evaluated in Sec. 11.3.2, and we obtained

$$
\begin{array} { l } { { E _ { A } ^ { m a } = 0 , } } \\ { { { } } } \\ { { E _ { A B } ^ { m a } = \displaystyle \frac 1 4 r _ { A B } n _ { A B } ^ { \langle m a \rangle } - \displaystyle \frac 1 6 r _ { A B } \delta ^ { m a } + \frac 1 2 n _ { A B } ^ { m } r _ { B } ^ { a } ; } } \end{array}
$$

these are Eqs. (11.138) and (11.153), respectively. Making the substitutions, we arrive at

$$
D ^ { m n a } = \sum _ { A } \sum _ { B \neq A } G ^ { 2 } M _ { A } M _ { B } v _ { B } ^ { n } \biggl ( \frac { 1 } { 4 } r _ { A B } n _ { A B } ^ { \langle m a \rangle } - \frac { 1 } { 6 } r _ { A B } \delta ^ { m a } + \frac { 1 } { 2 } n _ { A B } ^ { m } r _ { B } ^ { a } \biggr ) .
$$

# Computation of Emnabp

The surface integrals

$$
E ^ { m n a b p } = \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } U \partial ^ { m } U ^ { n } x ^ { a } x ^ { b } d S ^ { p }
$$

are evaluated at $| { \boldsymbol { x } } | = \mathcal { R }$ . On $\partial \mathcal { M }$ the Newtonian potential has the schematic form $\begin{array} { r } { U = \mathcal { R } ^ { - 1 } + \mathcal { R } ^ { - 3 } + \cdot \cdot . . } \end{array}$ , and the vector potential can be similarly expressed as $U ^ { n } =$ $\mathcal { R } ^ { - 2 } + \mathcal { R } ^ { - 3 } + \cdots .$ This implies that $\partial ^ { m } U ^ { n } = \mathcal { R } ^ { - 3 } + \mathcal { R } ^ { - 4 } + \cdot \cdot \cdot .$ . We recall that $U$ does not include an $\mathcal { R } ^ { - 2 }$ term because the Newtonian dipole moment $\begin{array} { r } { I : = \sum _ { \mathcal { A } } M _ { \mathcal { A } } \pmb { r } _ { \mathcal { A } } } \end{array}$ can be set equal to zero, and similarly, $U ^ { n }$ does not contain an $\mathcal { R } ^ { - 1 }$ term because $\begin{array} { r } { \dot { I } ^ { j } = \sum _ { A } M _ { A } v _ { A } ^ { j } = 0 } \end{array}$ . With $\boldsymbol { x } ^ { j } = \mathcal { R } \boldsymbol { N } ^ { j }$ and $d S ^ { j } = \mathcal { R } ^ { 2 } N ^ { j } d \Omega$ , we find that the leading term in the surface integral is of order $\mathcal { R } ^ { 0 }$ , and that it must be evaluated carefully. Further investigation reveals that at this order, $\partial ^ { m } U ^ { n }$ involves an even number of angular vectors $N$ , which implies that the surface integral involves an odd number of such vectors. This guarantees that

$$
E ^ { m n a b p } = 0 ,
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded.

# Computation of $A ^ { j k a }$ [F]

It is now a straightforward task to substitute Eq. (11.205) for $C ^ { m n p a b }$ , Eq. (11.209) for $D ^ { m n a }$ , and Eq. (11.211) for $E ^ { m n a b p }$ into Eqs. (11.185) and (11.187). These results, in turn, can be inserted within Eq. (11.180) for $B _ { 1 } ^ { a b c }$ , Eq. (11.181) for $B _ { 2 } ^ { a b c }$ , and Eq. (11.182) for $B _ { 3 } ^ { a b c }$ . The final step is to substitute these expressions into the right-hand side of Eq. (11.178). The end result, after much simplification, and after discarding terms that will not survive

the TT projection, is

$$
\begin{array} { l } { { \displaystyle { \mathcal { A } } ^ { j k a } [ \Gamma ] \equiv \frac { 1 } { c ^ { 3 } } \displaystyle \sum _ { A } \sum _ { B \neq A } G M _ { A } M _ { B } \Bigg \{ r _ { A B } \Bigg [ - \frac { 1 } { 6 } \big ( n _ { A B } \cdot \mathbf { v } _ { B } \big ) n _ { A B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { a } } } \\ { ~ } \\ { { \displaystyle ~ + \frac { 1 } { 1 2 } n _ { A } ^ { j } \big ( n _ { A B } ^ { k } n _ { B } ^ { a } + v _ { B } ^ { k } n _ { A B } ^ { a } \big ) - \frac { 1 1 } { 6 } v _ { B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { a } \Bigg ] } } \\ { { \displaystyle ~ - \frac { 1 } { 4 } \big ( n _ { A B } \cdot \mathbf { v } _ { B } \big ) n _ { A B } ^ { j } \big ( n _ { A B } ^ { k } r _ { B } ^ { a } + r _ { B } ^ { k } n _ { A B } ^ { a } \big ) + \frac { 7 } { 4 } n _ { A } ^ { j } \big ( v _ { B } ^ { k } r _ { B } ^ { a } + r _ { B } ^ { k } v _ { B } ^ { a } \big ) } } \\ { { \displaystyle ~ - \frac { 7 } { 4 } v _ { B } ^ { j } \big ( n _ { A B } ^ { k } r _ { B } ^ { a } + r _ { B } ^ { k } n _ { A B } ^ { a } \big ) - \frac { 1 } { r _ { A B } } \Bigg [ \frac { 1 } { 2 } \big ( n _ { A B } \cdot \mathbf { v } _ { B } \big ) n _ { A B } ^ { j } r _ { B } ^ { k } r _ { B } ^ { a } } } \\ { { \displaystyle ~ + \frac { 7 } { 2 } v _ { B } ^ { j } r _ { B } ^ { k } r _ { B } ^ { a } \Bigg ] \Bigg \} . \qquad ( 1 1 . 2 1 ) ^ { \mathrm { T r } } , } } \end{array}
$$

# Final answer

Equation (11.212) for $A ^ { j k a } [ \mathrm { F } ]$ and Eq. (11.175) for $A ^ { j k a } [ \mathrm { M } ]$ can finally be combined to form $A ^ { j k a }$ , as defined by Eq. (11.171). After inserting $\textstyle \sum _ { B \neq A } G M _ { B } / r _ { A B }$ for $\lfloor U \rfloor _ { A }$ and additional simplification, we obtain Eq. (11.172). To arrive at this result we rearrange some of the sums in Eq. (11.212) and switch the identities of bodies $A$ and $B$ ; this permutation affects the signs of some terms, because $\pmb { n } _ { B A } = - \pmb { n } _ { A B }$ .

# 11.3.5 Radiative 4-pole and 5-pole moments

Our next step is computation of $\boldsymbol { Q } ^ { j k a b }$ , the radiative 4-pole moment, and $\boldsymbol { Q } ^ { j k a b c }$ , the radiative 5-pole moment. These are defined by Eq. (11.119),

$$
Q ^ { j k a b } ( \tau ) : = \frac { 1 } { c ^ { 2 } } \int _ { \mathcal { M } } \tau ^ { j k } ( \tau , x ) x ^ { a } x ^ { b } d ^ { 3 } x
$$

and

$$
\mathcal { Q } ^ { j k a b c } ( \tau ) : = \frac { 1 } { c ^ { 3 } } \frac { \partial } { \partial \tau } \int _ { \mathcal { M } } \tau ^ { j k } ( \tau , \pmb { x } ) x ^ { a } x ^ { b } x ^ { c } d ^ { 3 } \ b { x } .
$$

We show below that these are given by

$$
\begin{array} { l } { { \displaystyle Q ^ { j k a b } \equiv \frac { 1 } { c ^ { 2 } } \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 c ^ { 2 } } \sum _ { A } \sum _ { B \not = A } \frac { G M _ { A } M _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } } } \\ { { \displaystyle ~ + \frac { 1 } { 1 2 c ^ { 2 } } \sum _ { A } \sum _ { B \not = A } G M _ { A } M _ { B } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } \big ( n _ { A B } ^ { a } n _ { A B } ^ { b } - \delta ^ { a b } \big ) } } \\ { { \displaystyle ~ + O ( c ^ { - 4 } ) } } \end{array}
$$

and

$$
\begin{array} { c } { { \displaystyle Q ^ { j k a b c } \equiv \frac { 1 } { c ^ { 3 } } \frac { \partial } { \partial \tau } \biggl [ \displaystyle \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } r _ { A } ^ { c } - \displaystyle \frac { 1 } { 2 } \sum _ { A } \displaystyle \sum _ { B \neq A } \frac { G M _ { A } M _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } r _ { A } ^ { c } } } \\ { { + \displaystyle \frac { 1 } { 4 } \sum _ { A } \displaystyle \sum _ { B \neq A } G M _ { A } M _ { B } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { ( a } \Big ( n _ { A B } ^ { b } n _ { A B } ^ { c ) } - \delta ^ { b c ) } \Big ) \biggr ] } } \\ { { + O ( c ^ { - 5 } ) . } } \end{array}
$$

The index symmetrization in the last sum of Eq. (11.216) is over the trio of indices abc. We leave the differentiation with respect to $\tau$ unevaluated for the time being; it is advantageous to take care of this at a later stage.

According to the discussion of Sec. 11.3.1, to calculate $\boldsymbol { Q } ^ { j k a b }$ to the required degree of accuracy we need an expression for $\tau ^ { j k }$ that includes terms of order $c ^ { 0 }$ only. According to Eq. (7.54c), we have that

$$
\tau ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + \frac { 1 } { 4 \pi G } \Big ( \partial ^ { j } U \partial ^ { k } U - \frac { 1 } { 2 } \delta ^ { j k } \partial _ { p } U \partial ^ { p } U \Big ) + { \cal O } ( c ^ { - 2 } ) ,
$$

and this becomes

$$
\tau ^ { j k } = \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } \delta \big ( x - r _ { A } \big ) + \frac { 1 } { 4 \pi G } \bigg ( \partial ^ { j } U \partial ^ { k } U - \frac 1 2 \delta ^ { j k } \partial _ { p } U \partial ^ { p } U \bigg ) + O ( c ^ { - 2 } )
$$

for a system of point particles. The matter contribution can be calculated at once:

$$
Q ^ { j k a b } [ { \bf M } ] = \frac { 1 } { c ^ { 2 } } \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } .
$$

The field contribution is

$$
Q ^ { j k a b } [ \mathsf { F } ] = \frac { 1 } { 4 \pi G c ^ { 2 } } \int _ { \mathcal { M } } \partial ^ { j } U \partial ^ { k } U x ^ { a } x ^ { b } d ^ { 3 } x - \frac { 1 } { 8 \pi G c ^ { 2 } } \delta ^ { j k } \int _ { \mathcal { M } } \partial _ { p } U \partial ^ { p } U x ^ { a } x ^ { b } d ^ { 3 } x ,
$$

and the second term, because it comes with a factor $\delta ^ { j k }$ in front of the integral, will not survive a TT projection. The complete 4-pole moment is $Q ^ { j k a b } = Q ^ { j k a b } [ { \bf M } ] + Q ^ { j k a b } [ { \bf F } ] +$ $O ( c ^ { - 4 } )$ .

To evaluate the first integral we employ our usual strategy of integrating by parts so as to leave one factor of $U$ undifferentiated. We find that the integral splits into a volume integral over the domain $\mathcal { M }$ and a surface integral over $\partial \mathcal { M }$ , and that Eq. (11.220) becomes

$$
\begin{array} { r } { Q ^ { j k a b } [ \mathrm { F } ] \stackrel { \mathrm { r } \mathrm { \scriptscriptstyle T } } { = } Q ^ { j k a b } [ \mathrm { F } , \mathcal { M } ] + Q ^ { j k a b } [ \mathrm { F } , \partial \mathcal { M } ] , } \end{array}
$$

where

$$
\begin{array} { r l r } & { } & { \displaystyle \mathcal { Q } ^ { j k a b } [ \mathrm { F } , \mathcal { M } ] : = - \frac { 1 } { 4 \pi G c ^ { 2 } } \int _ { \mathcal { M } } U \partial ^ { j k } U x ^ { a } x ^ { b } d ^ { 3 } x , } \\ & { } & { \displaystyle \mathcal { Q } ^ { j k a b } [ \mathrm { F } , \partial \mathcal { M } ] : = \frac { 1 } { 4 \pi G c ^ { 2 } } \oint _ { \partial \mathcal { M } } U \partial ^ { k } U x ^ { a } x ^ { b } d S ^ { j } . } \end{array}
$$

To arrive at Eq. (11.221) we have discarded additional terms that will not survive a TT projection. For example, a contribution to $\boldsymbol { Q } ^ { j k a b }$ of the form $\delta ^ { j a } A ^ { k b }$ would become $N ^ { j } A ^ { k b } N _ { b }$

after contraction with $N _ { a } N _ { b }$ , and this would make an irrelevant, longitudinal contribution to $h ^ { j k }$ .

To evaluate the volume integral in Eqs. (11.222) we insert the familiar expression for $U$ , as well as

$$
\partial ^ { j k } U = - \sum _ { A } G M _ { A } \bigg [ - 3 { \frac { ( x - r _ { A } ) ^ { j } ( x - r _ { A } ) ^ { k } } { | x - r _ { A } | ^ { 5 } } } + { \frac { \delta ^ { j k } } { | x - r _ { A } | ^ { 3 } } } + { \frac { 4 \pi } { 3 } } \delta ^ { j k } \delta ( x - r _ { A } ) \bigg ] .
$$

Once more we ignore the terms in $\delta ^ { j k }$ , and find that

$$
Q ^ { j k c d } [ \mathsf { F } , \mathcal { M } ] \stackrel { \pi } { = } - \frac { 3 } { c ^ { 2 } } \sum _ { A } G { M } _ { A } ^ { 2 } F _ { A } ^ { j k a b } - \frac { 3 } { c ^ { 2 } } \sum _ { A } \sum _ { B \neq A } G { M } _ { A } { M } _ { B } F _ { B A } ^ { j k a b } ,
$$

where the field integrals F jka b and F jkabB A were introduced in Sec. 11.3.4; they are defined by Eqs. (11.190), and evaluated in Eqs. (11.196) and (11.203). From these results we learn that F jkab is proportional to $\delta ^ { j k }$ and will not survive a TT projection, and that $F _ { B A } ^ { j k a b }$ can be expressed as

$$
\begin{array} { l } { { { \cal F } _ { B A } ^ { j k a b } \stackrel { \pi } { = } \displaystyle \frac { 1 } { 3 6 } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } \big ( 2 n _ { A B } ^ { a } n _ { A B } ^ { b } + \delta ^ { a b } \big ) - \displaystyle \frac { 1 } { 6 } n _ { A B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { ( a } r _ { A } ^ { b ) } } } \\ { { \displaystyle \quad \quad + \displaystyle \frac { 1 } { 6 r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } , } } \end{array}
$$

after discarding terms that will be projected out and further simplification.

Inserting these expressions within $\boldsymbol { \mathcal { Q } ^ { j k a b } [ \mathsf { F } , \mathcal { M } ] }$ , we arrive at

$$
\begin{array} { l } { { \displaystyle Q ^ { j k a b } [ \mathrm { F } , \mathcal { M } ] \equiv - \frac { 1 } { 1 2 c ^ { 2 } } \sum _ { { \cal A } } \sum _ { B \neq { \cal A } } G { \cal M } _ { { \cal A } } { \cal M } _ { B } r _ { \cal A B } n _ { A B } ^ { j } n _ { A B } ^ { k } \big ( 2 n _ { A B } ^ { a } n _ { A B } ^ { b } + \delta ^ { a b } \big ) } } \\ { { \displaystyle ~ + \frac { 1 } { 2 c ^ { 2 } } \sum _ { { \cal A } } \sum _ { B \neq { \cal A } } G { \cal M } _ { { \cal A } } { \cal M } _ { B } n _ { A B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { ( a } r _ { \cal A } ^ { b ) } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 c ^ { 2 } } \sum _ { { \cal A } } \sum _ { B \neq { \cal A } } \frac { G { \cal M } _ { { \cal A } } { \cal M } _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { \cal A } ^ { a } r _ { \cal A } ^ { b } . } } \end{array}
$$

This expression can be simplified. We examine the second line, which we write as

$$
{ \frac { 1 } { 4 c ^ { 2 } } } \sum _ { A } \sum _ { B \neq A } G M _ { A } M _ { B } n _ { A B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { a } r _ { A } ^ { b } + ( a  b ) .
$$

By rearranging the sums, we see that this is also

$$
\frac { 1 } { 4 c ^ { 2 } } \sum _ { A } \sum _ { B > A } G M _ { A } M _ { B } n _ { A B } ^ { j } n _ { A B } ^ { k } \big ( n _ { A B } ^ { a } r _ { A } ^ { b } + n _ { B A } ^ { a } r _ { B } ^ { b } \big ) + ( a  b ) ,
$$

or

$$
{ \frac { 1 } { 4 c ^ { 2 } } } \sum _ { A } \sum _ { B > A } G M _ { A } M _ { B } n _ { A B } ^ { j } n _ { A B } ^ { k } n _ { A B } ^ { a } \bigl ( r _ { A } ^ { b } - r _ { B } ^ { b } \bigr ) + ( a  b ) .
$$

The term within brackets is $r _ { A B } n _ { A B } ^ { b }$ , and we see that the second line in $\boldsymbol { \mathcal { Q } ^ { j k a b } [ \mathsf { F } , \mathcal { M } ] }$ can be joined with the first. Our final expression is

$$
\begin{array} { c } { { Q ^ { j k a b } [ \mathrm { F } , \mathcal { M } ] \stackrel { \pi } { = } \displaystyle \frac { 1 } { 1 2 c ^ { 2 } } \sum _ { A } \sum _ { B \neq A } G { \cal M } _ { A } { \cal M } _ { B } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } \big ( n _ { A B } ^ { a } n _ { A B } ^ { b } - \delta ^ { a b } \big ) } } \\ { { - \displaystyle \frac { 1 } { 2 c ^ { 2 } } \sum _ { A } \sum _ { B \neq A } \frac { G { \cal M } _ { A } { \cal M } _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

Moving on to the surface integral of Eq. (11.222), we recall our previous work in Sec. 11.3.3, in which $U$ had the schematic structure $U = \mathcal { R } ^ { - 1 } + \mathcal { R } ^ { - 3 } + \cdots$ when evaluated on $\partial \mathcal { M }$ , while its gradient is given by $\partial ^ { k } U = \mathcal { R } ^ { - 2 } + \mathcal { R } ^ { - 4 } + \cdot \cdot \cdot$ With $x ^ { a } = \mathcal { R } N ^ { a }$ and $d S ^ { j } = \mathcal { R } ^ { 2 } N ^ { j } d \Omega$ , these statements imply that $\boldsymbol { \mathcal { Q } ^ { j k a b } [ \mathsf { F } , \partial \mathcal { M } ] }$ contains terms at orders $\mathcal { R }$ , $\mathcal { R } ^ { - 1 }$ , and so on, but that there is no $\mathcal { R }$ -independent contribution. For this reason, we may set

$$
\begin{array} { r } { Q ^ { j k a b } [ \mathsf { F } , \partial \mathcal { M } ] = 0 , } \end{array}
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded.

Collecting results, we find that the radiative 4-pole moment is given by the expression displayed back in Eq. (11.215). The computation of the radiative 5-pole moment is accomplished by following the same familiar steps. We shall not labor through the details here, but simply state that the final answer is the expression displayed back in Eq. (11.216).

# 11.3.6 Surface integrals

At this stage we have computed all the radiative multipole moments that contribute to $h _ { \mathcal { N } } ^ { j k }$ through $1 . 5 \mathrm { { P N } }$ order. The multipole expansion of Eq. (11.118), however, also involves a pair of surface integrals, $P ^ { j k }$ and $P ^ { j k a }$ , which are defined by Eqs. (11.120). Our task in this subsection is to evaluate them. We shall find that they make no contributions to $h _ { \mathcal { N } } ^ { j k }$ .

We begin with

$$
P ^ { j k } : = \oint _ { \partial \mathcal { M } } \bigl ( \tau ^ { j p } x ^ { k } + \tau ^ { k p } x ^ { j } - \partial _ { q } \tau ^ { p q } x ^ { j } x ^ { k } \bigr ) d S _ { p } ,
$$

in which $\tau ^ { j k }$ is expressed as a function of $\tau$ and $_ x$ , and where we suppress the primes on the integration variables to simplify the notation. The effective stress tensor $\tau ^ { j k }$ is given to leading order by Eq. (11.218), and this reduces to

$$
\tau ^ { j k } \overset { \mathtt { r } \mathtt { r } } { = } \frac { 1 } { 4 \pi G } \partial ^ { j } U \partial ^ { k } U + O ( c ^ { - 2 } )
$$

when it is evaluated on $\partial \mathcal { M }$ , where the matter contribution vanishes. This expression, however, is not sufficient to achieve the required degree of accuracy for the surface integrals (as specified back in Sec. 11.3.1); for this we must also incorporate terms of order $c ^ { - 2 }$ . An improved expression can be obtained from Eqs. (7.49) and (7.52). In this we substitute the near-zone gravitational potentials of $\mathrm { B o x } 7 . 5$ , and we obtain

$$
\begin{array} { c } { { \tau ^ { j k } \overset { \pi } { = } \displaystyle \frac { 1 } { 4 \pi G } \partial ^ { j } U \partial ^ { k } U + \displaystyle \frac { 1 } { 4 \pi G c ^ { 2 } } \bigg [ 2 \partial ^ { ( j } U \partial ^ { k ) } \psi + \partial ^ { ( j } U \partial ^ { k ) } \partial _ { t t } X + 8 \partial ^ { ( j } U \partial _ { t } U ^ { k ) } } } \\ { { - 4 \big ( \partial ^ { j } U _ { p } - \partial _ { p } U ^ { j } \big ) \big ( \partial ^ { k } U ^ { p } - \partial ^ { p } U ^ { k } \big ) \bigg ] + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

after discarding all terms proportional to $\delta ^ { j k }$ , for the usual reason that they will not survive a TT projection. This expression involves our old friends the Newtonian potential $U$ and the vector potential $U ^ { j }$ , but it involves also the post-Newtonian potentials $\psi$ and $X$ that were first introduced in Sec. 7.3. These were evaluated for a system of point masses in Sec. 9.6; refer to Eqs. (9.268), (9.270), and (9.272).

To calculate $P ^ { j k }$ we also need $\partial _ { q } \tau ^ { p q }$ , which we express as $- c ^ { - 1 } \partial _ { t } \tau ^ { 0 p }$ by involving the conservation identities $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ . With Eq. (11.174), this is

$$
\partial _ { q } \tau ^ { p q } = \frac { 1 } { 4 \pi G c ^ { 2 } } \frac { \partial } { \partial \tau } \Biggl [ 3 \partial _ { q } U ^ { q } \partial ^ { p } U - 4 \bigl ( \partial ^ { p } U ^ { q } - \partial ^ { q } U ^ { p } \bigr ) \partial _ { q } U \Biggr ] ,
$$

in which we have inserted the identity $\partial _ { t } U + \partial _ { q } U ^ { q } = 0$ . The derivative operator can be taken outside of the surface integral.

From the explicit expressions obtained in Sec. 9.6 for $U , U ^ { j } , \psi$ , and $\partial _ { t t } { X }$ , we observe that each one of these quantities has the schematic form $| { \pmb x } | ^ { - 1 } + | { \pmb x } | ^ { - 2 } + \cdots$ when expanded in inverse powers of $| x |$ . It follows that when $\partial ^ { j } U , \partial ^ { j } \psi , \partial _ { t t } ^ { j } X , \partial ^ { k } U ^ { j }$ , and $\partial _ { t } U ^ { j }$ are evaluated on $\partial \mathcal { M }$ , they each have the schematic form $\mathcal { R } ^ { - 2 } + \mathcal { R } ^ { - 3 } + \cdots$ This means that $\tau ^ { j k } = O ( \mathcal { R } ^ { - 4 } )$ , and it follows that a quantity such as $\tau ^ { j p } x ^ { k } d S _ { p }$ must scale as $\mathcal { R } ^ { - 1 }$ ; this does not give rise to an $\mathcal { R }$ -independent contribution to the surface integral. A similar argument reveals that $\partial _ { q } \tau ^ { p q } = { \cal O } ( \mathcal { R } ^ { - 5 } )$ , so that $\partial _ { q } \tau ^ { p q } x ^ { j } x ^ { k } d S _ { p }$ scales as $\mathcal { R } ^ { - 1 }$ ; this also makes no contribution. We conclude that

$$
P ^ { j k } = 0 ,
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded.

We next evaluate

$$
P ^ { j k a } : = \frac { 1 } { c } \frac { \partial } { \partial \tau } \oint _ { \partial \mathcal { M } } \left( \tau ^ { j p } x ^ { k } x ^ { a } + \tau ^ { k p } x ^ { j } x ^ { a } - \tau ^ { a p } x ^ { j } x ^ { k } \right) d S _ { p } ,
$$

using the effective stress tensor displayed in Eq. (11.231). Relative to $P ^ { j k }$ , this surface integral involves an additional power of $\boldsymbol { x }$ , and therefore an additional power of $\mathcal { R }$ ; because $P ^ { j k }$ was seen to be of order $\mathcal { R } ^ { - 1 }$ , there is a chance that the surface integral might contain an $\mathcal { R }$ -independent contribution. As we shall see presently, however, this does not happen, and as a matter of fact,

$$
P ^ { j k a } = 0 ,
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded. This conclusion emerges as a result of a closer examination of the terms that make up $\tau ^ { j k }$ . It was stated previously that at leading order, $\partial ^ { j } U , \partial ^ { j } \psi , \partial _ { t t } ^ { j } X , \partial ^ { k } U ^ { j }$ , and $\partial _ { t } U ^ { j }$ all scale as $\mathcal { R } ^ { - 2 }$ when they are evaluated on $\partial \mathcal { M }$ , so that $\tau ^ { j k } = O ( \mathcal { R } ^ { - 4 } )$ . With the four powers of $\mathcal { R }$ that are contained in the position vectors and the surface element, we find that the integral does indeed scale as $\mathcal { R } ^ { 0 }$ . It can be verified, however, that $\partial ^ { j } U , \partial ^ { j } \psi , \partial _ { t t } ^ { j } X , \partial ^ { k } U ^ { j }$ , and $\partial _ { t } U ^ { j }$ are all proportional to a product of an odd number of angular vectors $N$ . This implies that $\tau ^ { j k }$ involves an even number of such vectors, and this, in turn, implies that the integrand in Eq. (11.234) contains an odd number of angular vectors. Integration gives zero, and we have established the statement of Eq. (11.235).

# 11.3.7 Tails: Wave-zone contribution to the gravitational waves

We departed on our long journey to calculate the gravitational-wave field back in Sec. 11.3.1, and all the while we have focused our attention on the near-zone piece $h _ { \mathcal { N } } ^ { j k }$ . We have ignored the wave-zone piece $h _ { \mathcal { W } } ^ { j k }$ , except to announce that it makes a relevant contribution at $1 . 5 \mathrm { { P N } }$ order. In this subsection we make amends and calculate this final contribution to the gravitational-wave field, which is generated entirely by field energy situated in the wave zone. We shall show that it is given by the so-called tail integral

$$
h _ { \mathcal { W } } ^ { j k } \stackrel { \pi } { = } \frac { 4 G } { c ^ { 4 } R } \frac { G M } { c ^ { 3 } } \int _ { 0 } ^ { \infty } \stackrel { ( 4 ) } { I } ^ { ( j k ) } ( \tau - \zeta ) \left( \ln \frac { \zeta } { \zeta + 2 R / c } + \frac { 1 1 } { 1 2 } \right) d \zeta ,
$$

which involves the entire past history of the system, from the infinite past at $\zeta = \infty$ to the current (retarded) time at $\zeta = 0$ . The wave-zone contribution depends on $M$ , the total gravitational mass of the system, as well as $I ^ { j k }$ , the Newtonian quadrupole moment of the matter distribution; in Eq. (11.236) the quadrupole moment is made tracefree and differentiated four times with respect to its argument. Recalling our discussion near the end of Sec. 11.3.1, we see that $h _ { \mathcal { W } } ^ { j k }$ is a correction of order $c ^ { - 3 }$ relative to the leading, quadrupole term in $h ^ { j k }$ ; the wave-zone contribution to the gravitational-wave field is therefore a term of $1 . 5 \mathrm { P N }$ order. In the course of our calculations we shall discover that $h _ { \mathcal { W } } ^ { j k }$ comes about because the gravitational waves propagate not in the fictitious flat spacetime of post-Minkowskian theory, but in a physical spacetime that is curved by the presence of a mass $M$ .

# Wave-zone integrals

We begin our derivation of Eq. (11.236) by recalling that back in Sec. 6.3.5, we devised a method to calculate $h _ { \mathcal { W } } ^ { j k }$ when $\tau ^ { j k }$ can be expressed as a sum of terms of the form

$$
\tau ^ { j k } [ \ell , n ] = \frac { 1 } { 4 \pi } \frac { f ( \tau ) } { R ^ { n } } N ^ { \langle L \rangle } ,
$$

in which $f$ is an arbitrary function of $\tau , n$ is an arbitrary integer, and $N ^ { \langle L \rangle }$ is an angular STF tensor of degree $\ell$ of the sort introduced back in Sec. 1.5.3. According to Eq. (6.105), $h _ { \mathcal { W } } ^ { j k }$ is then a sum of terms of the form

$$
h _ { \mathcal { W } } ^ { j k } [ \ell , n ] = \frac { 4 G } { c ^ { 4 } R } N ^ { ( L ) } \bigg \{ \int _ { 0 } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , R ) + \int _ { \mathcal { R } } ^ { \infty } d s f ( \tau - 2 s / c ) B ( s , R ) \bigg \} ,
$$

where

$$
A ( s , R ) = \int _ { \mathcal R } ^ { R + s } { \frac { P _ { \ell } ( \xi ) } { p ^ { n - 1 } } } d p , \qquad B ( s , R ) = \int _ { s } ^ { R + s } { \frac { P _ { \ell } ( \xi ) } { p ^ { n - 1 } } } d p ,
$$

in which $P _ { \ell }$ is a Legendre polynomial of argument $\xi = ( R + 2 s ) / R - 2 s ( R + s ) / ( R p )$ .   
We shall rely on these results in the remainder of this subsection.

# Construction of the source term

The wave-zone contribution to $h ^ { j k }$ is obtained by evaluating the integrals displayed in Eq. (11.238), and this relies on a decomposition of $\tau ^ { j k }$ into irreducible pieces of the form of Eq. (11.237). Our first order of business, therefore, is to obtain an appropriate expression for the effective stress tensor; this expression must be valid everywhere in the wave zone.

The source term is constructed from the gravitational potentials, and wave-zone expressions for these were obtained in Sec. 7.4. According to the summary presented in $\mathrm { B o x } 7 . 7$ , we have

$$
\begin{array} { l } { { { h ^ { 0 0 } = { \displaystyle \frac { 4 G } { c ^ { 2 } } } \biggl [ \frac { M } { R } + \frac { 1 } { 2 } \partial _ { j k } \biggl ( \frac { \mathcal { D } ^ { j k } } { R } \biggr ) + \cdots \biggr ] } , } } \\ { { { h ^ { 0 j } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ - \frac { 1 } { 2 c } \mathcal { I } ^ { j k } \frac { N _ { k } } { R ^ { 2 } } - \frac { 1 } { 2 c } \partial _ { k } \biggl ( \frac { \dot { \mathcal { Z } } ^ { j k } } { R } \biggr ) + \cdots \biggr ] } , } } \\ { { { h ^ { j k } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ \frac { 1 } { 2 c ^ { 2 } } \frac { \ddot { \mathcal { Z } } ^ { j k } } { R } + \cdots \biggr ] } . } } \end{array}
$$

The potentials are expressed in terms of $R : = | { \boldsymbol { x } } | , N : = { \boldsymbol { x } } / R$ , and the multipole moments that were introduced back in Sec. 7.1.2. For a system of $N$ bodies, and to lowest pn order, we have the total gravitational mass $\begin{array} { r } { M = \sum _ { A } M _ { A } + O ( c ^ { - 2 } ) } \end{array}$ , the angular-momentum tensor $\begin{array} { r } { \mathcal { T } ^ { j k } = \sum _ { A } M _ { A } ( v _ { A } ^ { j } r _ { A } ^ { k } - r _ { A } ^ { j } v _ { A } ^ { k } ) + O ( c ^ { - 2 } ) } \end{array}$ , and the quadrupole moment

$$
{ \mathcal { T } } ^ { j k } ( \tau ) = \sum _ { A } M _ { A } r _ { A } ^ { j } r _ { A } ^ { k } + O ( c ^ { - 2 } ) .
$$

These expressions are obtained from the equations listed in $\mathrm { B o x } 7 . 7$ by specializing them to a system of point masses. The mass and angular momentum are conserved quantities, while $\mathcal { T } ^ { j k }$ depends on retarded time $\tau : = t - R / c$ . For the rest of this discussion we replace the formal post-Minkowskian moment $\mathcal { T } ^ { j k }$ with its Newtonian expression $\begin{array} { r } { I ^ { j k } = \sum _ { A } M _ { A } r _ { A } ^ { j } r _ { A } ^ { k } } \end{array}$ .

The post-Newtonian order of each term in Eqs. (11.240) was identified in Box 7.7: relative to $G M / ( c ^ { 2 } R )$ , each term involving $I ^ { j k }$ is of 1pn order, and the term involving the angular-momentum tensor is also of 1pn order; the expressions are therefore truncated at 1pn order, and the neglected terms are of $1 . 5 \mathrm { { P N } }$ order. The rules to count post-Newtonian orders in wave-zone potentials were derived back in Sec. 7.2.3. It is useful to recall that in the wave zone, $R$ is larger than $\lambda _ { c }$ , the characteristic wavelength of the gravitational radiation; it follows that if $\dot { \boldsymbol { r } } _ { c }$ is a characteristic length scale of the source, then $r _ { c } / R \sim r _ { c } / \lambda _ { c } \sim v _ { c } / c$ , where $v _ { c }$ is the source’s characteristic velocity.

In the wave zone, away from the matter distribution, the effective stress tensor $\tau ^ { j k }$ is made up of the Landau–Lifshitz pseudotensor $( - g ) t _ { \mathrm { L L } } ^ { j k }$ and the harmonic-gauge contribution $( - g ) t _ { \mathrm { H } } ^ { j k }$ . Sufficiently accurate expressions for these quantities were obtained in Sec. 7.3.1. The leading term comes from the Landau–Lifshitz pseudotensor of Eq. (7.48); this is

$$
\frac { c ^ { 4 } } { 6 4 \pi G } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 } ,
$$

where we ignore the term proportional to $\delta ^ { j k }$ because, as we observed many times before, it will not survive a TT projection. Using Eq. (11.240), we find that this is equal to

$$
\frac { G } { 4 \pi } \biggl [ \frac { M ^ { 2 } } { R ^ { 4 } } N ^ { j } N ^ { k } - \frac { M } { R ^ { 2 } } N ^ { ( j } \partial _ { p q } ^ { k ) } \biggl ( \frac { I ^ { p q } } { R } \biggr ) + \cdot \cdot \cdot \biggr ] .
$$

It is easy to show that relative to $G M ^ { 2 } / R ^ { 4 }$ , the second term is of order $( v _ { c } / c ) ^ { 2 }$ , and the neglected terms are smaller by an additional power of $v _ { c } / c$ . Take, for example, the term that arises when $R ^ { - 1 }$ is differentiated three times. This is of the schematic form $( M / R ^ { 2 } ) ( I / R ^ { 4 } )$ , and relative to $M ^ { 2 } / R ^ { 4 }$ this is of order $( r _ { c } / R ) ^ { 2 } \sim ( r _ { c } / \lambda _ { c } ) ^ { 2 } \sim ( v _ { c } / c ) ^ { 2 }$ . As another example, take the term that arises when $I ^ { p q }$ is differentiated three times. This is of the schematic form $( M / R ^ { 2 } ) ( \stackrel { \cdot \cdot \cdot } { I } / c ^ { 3 } R )$ , and relative to $M ^ { 2 } / R ^ { 4 }$ this is of order $r _ { c } ^ { 2 } R / ( c t _ { c } ) ^ { 3 } \sim ( r _ { c } / \lambda _ { c } ) ^ { 2 } \sim ( v _ { c } / c ) ^ { 2 }$ .

We wish our expression for $\tau ^ { j k }$ to be as accurate as what was displayed previously. In particular, we want to be sure that our expression contains all occurrences of terms involving a product of $M$ with $I ^ { j k }$ or its derivatives; all such terms contribute at order $( v _ { c } / c ) ^ { 2 }$ relative to $G M ^ { 2 } / R ^ { 4 }$ , and they must all be included. A careful examination of Eq. (7.49) reveals that the relevant terms are contained in

$$
\begin{array} { r } { ( - g ) t _ { \mathrm { L L } } ^ { j k } = \cfrac { c ^ { 4 } } { 1 6 \pi G } \bigg [ \cfrac { 1 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 } + \partial ^ { j } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 k } + \partial ^ { k } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 j } } \\ { + \cfrac { 1 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h _ { p } ^ { p } + \cfrac { 1 } { 4 } \partial ^ { k } h ^ { 0 0 } \partial ^ { j } h _ { p } ^ { p } + \cdot \cdot \cdot \bigg ] , } \end{array}
$$

and that the additional terms are smaller by additional powers of $v _ { c } / c$

A careful examination of Eq. (7.53) reveals that

$$
( - g ) t _ { \mathrm { H } } ^ { j k } = { \frac { c ^ { 4 } } { 1 6 \pi G } } \Bigl [ - h ^ { 0 0 } \partial _ { 0 0 } h ^ { j k } + \cdot \cdot \cdot \Bigr ]
$$

is also a relevant term. It is easy to see why: after writing $\partial _ { 0 0 } = c ^ { - 2 } \partial _ { \tau \tau }$ , we find that this contribution to $\tau ^ { j k }$ is schematically

$$
\frac { c ^ { 2 } } { G } h ^ { 0 0 } \partial _ { \tau \tau } h ^ { j k } \sim \frac { G } { c ^ { 4 } } \frac { M ^ { ( 4 ) } } { R ^ { 2 } } ,
$$

in which the label (4) indicates that the quadrupole moment tensor is differentiated four times with respect to proper time $\tau$ . We have that $d ^ { 4 } I ^ { j k } / d \tau ^ { 4 } \sim M r _ { c } ^ { 2 } / t _ { c } ^ { 4 }$ , $R > \lambda _ { c } = c t _ { c }$ , and all this implies that this term is of order $( v _ { c } / c ) ^ { 2 }$ relative to $G M ^ { 2 } / R ^ { 4 }$ .

This is the first time that $( - g ) t _ { \mathrm { H } } ^ { \alpha \beta }$ explicitly enters a computation. As we saw back in Sec. 6.2.1, this contribution to $\tau ^ { \alpha \beta }$ comes from the difference between $\partial _ { \mu \nu } H ^ { \alpha \mu \beta \nu }$ and $- \sqsubset h ^ { \alpha \beta }$ on the left-hand side of the Landau–Lifshitz formulation of the Einstein field equations. It is this term that informs us that the gravitational waves are propagating not in flat spacetime, but in a curved spacetime whose metric $g _ { \alpha \beta }$ must be obtained self-consistently from the gravitational potentials (refer to Box 6.3). It is this contribution to $\tau ^ { \alpha \beta }$ , therefore, that reveals the differences between the light cones of the mathematical flat spacetime and those of the physical curved spacetime. And as we shall see, it is this term that generates the tail integral of Eq. (11.236).

Collecting results, we find that the appropriate starting expression for the source term is

$$
\begin{array} { c }  { \tau ^ { j k } = { \displaystyle { \frac { c ^ { 4 } } { 1 6 \pi G } } \biggl [ \frac { 1 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 } + \frac { 1 } { c } \partial ^ { j } h ^ { 0 0 } \partial _ { \tau } h ^ { 0 k } + \frac { 1 } { c } \partial ^ { k } h ^ { 0 0 } \partial _ { \tau } h ^ { 0 j } } } \\ { { + \displaystyle { \frac { 1 } { 4 } } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h _ { ~ p } ^ { p } + \frac { 1 } { 4 } \partial ^ { k } h ^ { 0 0 } \partial ^ { j } h _ { ~ p } ^ { p } - \frac { 1 } { c ^ { 2 } } h ^ { 0 0 } \partial _ { \tau \tau } h ^ { j k } + \cdot \cdot \cdot \biggr ] . } } \end{array}
$$

We must now turn this into something more concrete, a set of expressions that are ready for insertion within Eq. (11.238).

# Evaluation of the source term

The first step is to insert Eqs. (11.240) within Eq. (11.245). We need

$$
\begin{array} { r c l } { { } } & { { } } & { { \partial ^ { j } h ^ { 0 0 } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ - \frac { M } { R ^ { 2 } } N ^ { j } + \frac { 1 } { 2 } \partial _ { p q } ^ { j } \biggl ( \frac { I ^ { p q } } { R } \biggr ) + \cdots \biggr ] , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { \partial _ { \tau } h ^ { 0 j } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ - \frac { 1 } { 2 c } \partial _ { p } \biggl ( \frac { \tilde { I } ^ { j p } } { R } \biggr ) + \cdots \biggr ] , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \partial ^ { j } h _ { p } ^ { p } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ - \frac { 1 } { 2 c ^ { 2 } } \frac { \tilde { I } } { R ^ { 2 } } N ^ { j } + \cdots \biggr ] , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \partial _ { \tau \tau } h ^ { j k } = \displaystyle \frac { 4 G } { c ^ { 2 } } \biggl [ \frac { 1 } { 2 c ^ { 2 } R } \biggr _ { T } ^ { ( j ) k } + \cdots \biggr ] , } } \end{array}
$$

in which $\ddot { I } : = \ddot { I } ^ { p p }$ . After some algebra, we obtain

$$
\begin{array} { c } { { \tau ^ { j k } = \displaystyle \frac { G M } { 4 \pi R ^ { 2 } } \bigg [ \displaystyle \frac { M } { R ^ { 2 } } N ^ { j } N ^ { k } - N ^ { ( j } \partial _ { p q } ^ { k ) } \bigg ( \displaystyle \frac { I ^ { p q } } { R } \bigg ) + \displaystyle \frac { 4 } { c ^ { 2 } } N ^ { ( j } \partial _ { p } \bigg ( \displaystyle \frac { \ddot { I } ^ { k ) p } } { R } \bigg ) } } \\ { { + \displaystyle \frac { 1 } { c ^ { 2 } } \bigg ( \displaystyle \frac { \ddot { I } } { R ^ { 2 } } + \displaystyle \frac { 1 } { c } \displaystyle \frac { \ddot { I } } { R } \bigg ) N ^ { j } N ^ { k } - \displaystyle \frac { 2 } { c ^ { 4 } } \displaystyle \bar { I } ^ { j k } + \cdot \cdot \cdot \bigg ] . } } \end{array}
$$

The next step is to evaluate the derivatives. We recall that $\partial _ { j } R = N _ { j }$ and $\partial _ { j } N _ { k } =$ $R ^ { - 1 } ( \delta _ { j k } - N _ { j } N _ { k } )$ . We recall also that $I ^ { j k }$ depends on the spatial coordinates through $\tau = t - R / c$ , so that $\partial _ { p } I ^ { j k } = - c ^ { - 1 } \dot { I } ^ { j k } N _ { p }$ . Using these rules, we find that

$$
\partial _ { p } \bigg ( \frac { \ddot { I } ^ { j k } } { R } \bigg ) = - \bigg ( \frac { \ddot { I } ^ { j k } } { R ^ { 2 } } + \frac { 1 } { c } \frac { \ddot { I } ^ { j k } } { R } \bigg ) N _ { p }
$$

and

$$
\begin{array} { c } { { \partial _ { p q } ^ { j } \bigg ( \displaystyle \frac { I ^ { p q } } { R } \bigg ) = - \bigg ( 1 5 \displaystyle \frac { I ^ { p q } } { R ^ { 4 } } + \frac { 1 5 } { c } \displaystyle \frac { \dot { I } ^ { p q } } { R ^ { 3 } } + \frac { 6 } { c ^ { 2 } } \displaystyle \frac { \ddot { I } ^ { p q } } { R ^ { 2 } } + \frac { 1 } { c ^ { 3 } } \displaystyle \frac { \ddot { I } ^ { p q } } { R } \bigg ) N ^ { j } N _ { p } N _ { q } } }  \\ { { + \bigg ( 3 \displaystyle \frac { I ^ { p q } } { R ^ { 4 } } + \frac { 3 } { c } \displaystyle \frac { \dot { I } ^ { p q } } { R ^ { 3 } } + \frac { 1 } { c ^ { 2 } } \displaystyle \frac { \ddot { I } ^ { p q } } { R ^ { 2 } } \bigg ) \big ( N ^ { j } \delta _ { p q } + \delta _ { p } ^ { j } N _ { q } + \delta _ { q } ^ { j } N _ { p } \big ) . } } \end{array}
$$

With these results, Eq. (11.247) becomes

$$
\begin{array} { c } { { \tau ^ { j k } = \displaystyle \frac { G M ^ { 2 } } { 4 \pi R ^ { 4 } } N ^ { j } N ^ { k } + \displaystyle \frac { G M } { 4 \pi R ^ { 2 } } \biggl [ \biggl ( 1 5 \frac { I ^ { p q } } { R ^ { 4 } } + \frac { 1 5 } { c } \frac { \dot { I } ^ { p q } } { R ^ { 3 } } + \frac { 6 } { c ^ { 2 } } \frac { \dot { I } ^ { p q } } { R ^ { 2 } } + \frac { 1 } { c ^ { 3 } } \frac { \dot { I } ^ { p q } } { R } \biggr ) N ^ { j } N ^ { k } N _ { p } N _ { q } } } \\ { { - \left( 3 \frac { I } { R ^ { 4 } } + \frac { 3 } { c } \frac { \dot { I } } { R ^ { 3 } } - \frac { 1 } { c ^ { 3 } } \frac { \ddot { I } } { R } \right) N ^ { j } N ^ { k } } } \\ { { - \left( 3 \frac { I ^ { j p } } { R ^ { 4 } } + \frac { 3 } { c } \frac { \dot { I } ^ { j p } } { R ^ { 3 } } + \frac { 3 } { c ^ { 2 } } \frac { \dot { I } ^ { j p } } { R ^ { 2 } } + \frac { 2 } { c ^ { 3 } } \frac { \ddot { I } ^ { j p } } { R } \right) N ^ { k } N _ { p } } } \\ { { - \left( 3 \frac { I ^ { k p } } { R ^ { 4 } } + \frac { 3 } { c } \frac { \dot { I } ^ { k p } } { R ^ { 3 } } + \frac { 3 } { c ^ { 2 } } \frac { \dot { I } ^ { k p } } { R ^ { 2 } } + \frac { 2 } { c ^ { 3 } } \frac { \ddot { I } ^ { k p } } { R } \right) N ^ { j } N _ { p } - \frac { 2 } { c ^ { 4 } } \ O ^ { \{ j k } } + \cdots \biggr ] . }  \end{array}
$$

The final step is to express the angular dependence of $\tau ^ { j k }$ in terms of STF tensors $N ^ { \langle L \rangle }$ . We involve the definition of Eq. (1.155), and write $N ^ { j } N ^ { k } N ^ { p } N ^ { q }$ in terms of $N ^ { \langle j k p q \rangle }$ , $N ^ { j } N ^ { k } N ^ { p }$ in terms of $N ^ { \langle j k p \rangle }$ , and $N ^ { j } N ^ { k }$ in terms of $N ^ { \langle j k \rangle }$ . After discarding all terms proportional to $\delta ^ { j k }$ , our final expression for the effective stress tensor is

$$
\begin{array} { l }  { \displaystyle { \tau ^ { j k } = \frac { G M ^ { 2 } } { 4 \pi R ^ { 4 } } N ^ { ( j k ) } + \frac { G M } { 4 \pi R ^ { 2 } } \Bigg [ \bigg ( 1 5 \frac { I _ { p q } } { R ^ { 4 } } + \frac { 1 5 } { c } \frac { \dot { I } _ { p q } } { R ^ { 3 } } + \frac { 6 } { c ^ { 2 } } \frac { \dot { I } _ { p q } } { R ^ { 2 } } + \frac { 1 } { c ^ { 3 } } \frac { \ddot { I } _ { p q } } { R } \bigg ) N ^ { ( j k p q ) } } } \\ { { \displaystyle ~ + ~ \bigg ( - \frac { 6 } { 7 } \frac { I } { R ^ { 4 } } - \frac { 6 } { 7 c } \frac { \dot { I } } { R ^ { 3 } } + \frac { 6 } { 7 c ^ { 2 } } \frac { \dot { I } } { R ^ { 2 } } + \frac { 8 } { 7 c ^ { 3 } } \frac { \ddot { I } } { R } \bigg ) N ^ { ( j k ) } } } \\ { { \displaystyle ~ + ~ 2 \bigg ( \frac { 9 } { 7 } \frac { I _ { p } ^ { ( j ) } } { R ^ { 4 } } + \frac { 9 } { 7 c } \frac { \dot { I } _ { p } ^ { ( j ) } } { R ^ { 3 } } - \frac { 9 } { 7 c ^ { 2 } } \frac { \ddot { I } _ { p } ^ { ( j ) } } { R ^ { 2 } } - \frac { 1 2 } { 7 c ^ { 3 } } \frac { \ddot { I } _ { p } ^ { ( j ) } } { R } \bigg ) N ^ { ( k ) p ) } } } \\ { { \displaystyle ~ - ~ \frac { 6 } { 5 c ^ { 2 } } \frac { \ddot { I } ^ { ( j k ) } } { R ^ { 2 } } - \frac { 6 } { 5 c ^ { 3 } } \frac { \dot { I } ^ { ( j k ) } } { R } - \frac { 2 } { c ^ { 4 } } \binom { 1 0 k } { c ^ { 3 } } + \cdots \Bigg ] . \quad ( 1 1 . 2 5 ) } } \end{array}
$$

This expression is a sum of terms that have the structure of Eq. (11.237). For example, the first group of terms inside the square brackets has $\ell = 4$ , and it consists of four terms with $n = 6 , n = 5 , n = 4$ , and $n = 3$ ; for each one of these contributions we can easily read off the appropriate function $f$ .

We shall keep in mind that it is the last term of Eq. (11.251), the one involving four derivatives of $I ^ { \langle j k \rangle } ( \tau )$ , that originated from $( - g ) t _ { \mathrm { H } } ^ { j k }$ . It is this term that will reveal the differences between the light cones of the mathematical flat spacetime and those of the physical curved spacetime.

# Evaluation of the wave-zone integrals

Each term $\tau ^ { j k } [ \ell , n ]$ in Eq. (11.251) makes a contribution to the gravitational-wave field $h ^ { j k }$ given by Eq. (11.238). To see how these integrals are evaluated, we shall work through the representative case of $\ell = 0$ and $n = 3$ .

We begin by extracting the relevant piece of $\tau ^ { j k }$ from Eq. (11.251). Comparing with Eq. (11.237), we find that in this case the function $f$ is given by

$$
f ( \tau ) = - \frac { 6 } { 5 } \frac { G M } { c ^ { 3 } } \ddot { I } ^ { \langle j k \rangle } .
$$

We next evaluate the functions $A$ and $B$ . With $\ell = 0$ and $n = 3$ , the computations are elementary, and the results are

$$
A ( s , R ) = \frac { 1 } { \mathcal { R } } - \frac { 1 } { R + s } , \qquad B ( s , R ) = \frac { 1 } { s } - \frac { 1 } { R + s } .
$$

We now set to work on the integrals that appear in Eq. (11.238). The first is

$$
F _ { A } : = \int _ { 0 } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) A ( s , R ) = \int _ { 0 } ^ { \mathcal { R } } d s f ( \tau - 2 s / c ) \bigg ( \frac { 1 } { \mathcal { R } } - \frac { 1 } { R + s } \bigg ) ,
$$

and we rewrite it as

$$
F _ { A } = { \frac { 1 } { \mathcal { R } } } \int _ { 0 } ^ { \mathcal { R } } f ( \tau - 2 s / c ) d s - \int _ { 0 } ^ { \mathcal { R } } f ( \tau - 2 s / c ) d \ln ( R + s ) .
$$

After integrating the second term by parts, our final expression is

$$
\begin{array} { c } { { F _ { A } = - f ( \tau - 2 \mathcal { R } / c ) \ln ( R + \mathcal { R } ) + f ( \tau ) \ln R + \displaystyle \frac { 1 } { \mathcal { R } } \int _ { 0 } ^ { \mathcal { R } } f ( \tau - 2 s / c ) d s } } \\ { { - \displaystyle \frac { 2 } { c } \int _ { 0 } ^ { \mathcal { R } } \dot { f } ( \tau - 2 s / c ) \ln \displaystyle \frac { R + s } { s } d s - \displaystyle \frac { 2 } { c } \int _ { 0 } ^ { \mathcal { R } } \dot { f } ( \tau - 2 s / c ) \ln s d s . } } \end{array}
$$

The second integral is

$$
F _ { B } : = \int _ { \mathcal R } ^ { \infty } d s f ( \tau - 2 s / c ) B ( s , R ) = \int _ { \mathcal R } ^ { \infty } d s f ( \tau - 2 s / c ) \bigg ( \frac { 1 } { s } - \frac { 1 } { R + s } \bigg ) ,
$$

and we rewrite it as

$$
F _ { B } = - \int _ { \mathcal { R } } ^ { \infty } f ( \tau - 2 s / c ) d \ln { \frac { R + s } { s } } .
$$

Integration by parts yields

$$
F _ { B } = f ( \tau - 2 \mathcal { R } / c ) \ln \frac { R + \mathcal { R } } { \mathcal { R } } - \frac { 2 } { c } \int _ { \mathcal { R } } ^ { \infty } \dot { f } ( \tau - 2 s / c ) \ln \frac { R + s } { s } d s ,
$$

assuming that $f ( \tau - 2 s / c )$ goes to zero sufficiently rapidly as $s \to \infty$ to ensure that there is no boundary term at $s = \infty$ . (Physically, this condition implies that the system is only weakly dynamical in the infinite past.)

The sum of $F _ { A }$ and $F _ { B }$ is

$$
\begin{array} { l } { \displaystyle { F = - f ( \tau - 2 \mathcal { R } / c ) \ln \mathcal { R } + f ( \tau ) \ln R + \frac { 1 } { \mathcal { R } } \int _ { 0 } ^ { \mathcal { R } } f ( \tau - 2 s / c ) d s } } \\ { \displaystyle { \phantom { \frac { 2 } { 1 } } - \frac { 2 } { c } \int _ { 0 } ^ { \mathcal { R } } \dot { f } ( \tau - 2 s / c ) \ln s d s - \frac { 2 } { c } \int _ { 0 } ^ { \infty } \dot { f } ( \tau - 2 s / c ) \ln \frac { R + s } { s } d s . } } \end{array}
$$

This result is exact, but to simplify it we exploit the fact that we may remove from this all $\mathcal { R }$ -dependent pieces. As a formal tool to achieve this, we express $f ( \tau - 2 s / c )$ and its derivative as an infinite Taylor series in powers of $s$ , and we evaluate the two integrals from $s = 0$ to $s = \mathcal { R }$ . We find that they combine to give $f ( \tau )$ , plus terms that can be discarded because they come with explicit factors of $\mathcal { R }$ . After also expanding $f ( \tau - 2 \mathcal { R } / c )$ in powers

of $\mathcal { R }$ , we find that

$$
F = f ( \tau ) \Big [ 1 + \mathrm { l n } ( R / \mathcal { R } ) \Big ] - \frac { 2 } { c } \int _ { 0 } ^ { \infty } \dot { f } ( \tau - 2 s / c ) \ln \frac { R + s } { s } d s ,
$$

modulo $\mathcal { R }$ -dependent terms that can be freely discarded. This still contains a logarithmic dependence on $\mathcal { R }$ , but it could be removed by writing $\ln ( R / \mathcal { R } ) = \ln ( R / r _ { 0 } ) + \ln ( r _ { 0 } / \mathcal { R } )$ and discarding the second term. This alternative expression would then contain a dependence on an arbitrary constant $r _ { 0 }$ , and it is perhaps preferable to stick with the original form, in spite of the residual $\mathcal { R }$ -dependence.

The final answer is obtained by inserting our expressions for $f ( \tau )$ and $F$ within Eq. (11.238). We get

$$
h _ { \mathcal { W } } ^ { j k } [ 0 , 3 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ - \frac { 6 G } { 5 c ^ { 3 } } \Big [ 1 + \ln ( R / \mathcal { R } ) \Big ] \ddot { I } ^ { \langle j k \rangle } + \frac { 1 2 } { 5 } K ^ { j k } \bigg \} ,
$$

in which the tail integral

$$
K ^ { j k } ( \tau , R ) : = \frac { G } { c ^ { 4 } } \int _ { 0 } ^ { \infty } I ^ { ( j k ) } ( \tau - 2 s / c ) \ln \frac { R + s } { s } d s
$$

must be left unevaluated. Note that the tail integral involves the entire past history of the system, from the infinite past (at $s = \infty$ ) to the current retarded time (at $s = 0$ ). We shall see what fate awaits the logarithmic term $\ln ( R / \mathcal { R } )$ in $h _ { \mathcal { W } } ^ { j k } [ 0 , 3 ]$ , when this contribution to $h _ { \mathcal { W } } ^ { j k }$ is combined with others.

The same techniques are employed to calculate all other contributions to $h _ { \mathcal { W } } ^ { j k }$ . We shall not labor through the details here, but simply list the final results:

$$
\begin{array} { l l } { { } } & { { h _ { \mathcal { F } } ^ { i , k } [ 0 , 2 ] = \frac { 4 G M } { c ^ { 4 } R } \{ - 2 K ^ { i k } \} , } } \\ { { } } & { { } } \\ { { h _ { \mathcal { F } } ^ { i , k } [ 0 , 3 ] = \frac { 4 G M } { c ^ { 4 } R } \{ - \mathsf { G } G \} [ \mathsf { 1 } + \ln ( R / R ) \bigg ] \widetilde { T } ^ { i j k } + \frac { 1 2 } { 5 } K ^ { i k } \} , } } \\ { { } } & { { } } \\ { { h _ { \mathcal { F } } ^ { i , k } [ 0 , 4 ] = \frac { 4 G M } { c ^ { 4 } R } \{ \mathsf { \overline { { S } } } G \} [ \frac { 3 } { 2 } + \ln ( R / R ) \bigg ] \widetilde { T } ^ { i / ( k ) } - \frac { 1 2 } { 5 } K ^ { i j } \} , } } \\ { { } } & { { } } \\ { { h _ { \mathcal { F } } ^ { i , k } [ 2 , 3 ] = \frac { 4 G M } { c ^ { 4 } R } \{ - \frac { 2 G } { 7 c ^ { 3 } } \gamma _ { \gamma } \} N ^ { i / k } + ( j \circ k ) , } } \\ { { } } & { { } } \\ { { h _ { \mathcal { F } } ^ { i , k } [ 2 , 4 ] = \frac { 4 G M } { c ^ { 4 } R } \{ - \frac { 3 G } { 2 8 c ^ { 3 } } \gamma _ { \gamma } ^ { i } \} N ^ { i / k + 1 } + ( j \circ k ) , } } \\ { { } } & { { } } \\ { { h _ { \mathcal { F } } ^ { i , k } [ 2 , 5 ] = \frac { 4 G M } { c ^ { 4 } R } \{ \frac { G } { c ^ { 2 } } [ \frac { 4 7 } { 1 0 0 } + \frac { 3 } { 3 5 } \ln ( R / R ) ] \widetilde { T } _ { p } ^ { i } - \frac { 6 } { 3 5 } K _ { p } ^ { T } \} N ^ { i / 6 1 } + ( j  k ) , } } \end{array} \qquad \mathrm { ( 1 ) }
$$

$$
h _ { \mathcal { W } } ^ { j k } [ 2 , 6 ] = \frac { 4 G M } { c ^ { 4 } R } \Bigg \{ \frac { G } { c ^ { 3 } } \Bigg [ { - \frac { 9 7 } { 7 0 0 } - \frac { 3 } { 3 5 } \ln ( R / \mathcal { R } ) } \Bigg ] \because x ^ { j } _ { p } + \frac { 6 } { 3 5 } K _ { ~ p } ^ { j } \Bigg \} N ^ { \langle p k \rangle } + ( j  k ) ,
$$

$$
h _ { \mathcal { W } } ^ { j k } [ 4 , 3 ] = \frac { 4 G M } { c ^ { 4 } R } \left\{ \frac { G } { 2 0 c ^ { 3 } } \dddot I _ { p q } \right\} N ^ { \langle j k p q \rangle } ,
$$

$$
\begin{array} { l } { { { \displaystyle h _ { \scriptscriptstyle \psi } ^ { j k } [ 4 , 4 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { G } { 3 0 c ^ { 3 } } \dddot { I } _ { p q } \bigg \} N ^ { \langle j k p q \rangle } , } } } \\ { { { \displaystyle h _ { \scriptscriptstyle \psi } ^ { j k } [ 4 , 5 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { G } { 4 2 c ^ { 3 } } \dddot { I } _ { p q } \bigg \} N ^ { \langle j k p q \rangle } , } } } \\ { { { \displaystyle h _ { \scriptscriptstyle \psi } ^ { j k } [ 4 , 6 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { G } { 5 6 c ^ { 3 } } \dddot { I } _ { p q } \bigg \} N ^ { \langle j k p q \rangle } . } } } \end{array}
$$

To arrive at these results we have freely discarded all $\mathcal { R }$ -dependent terms, except when the dependence is logarithmic. In some cases we have also removed terms that fall off as $R ^ { - 2 }$ , $R ^ { - 3 }$ , or faster, because these are negligible in the far-away wave zone.

From the preceding listing of results we find that the sums of contributions for $\ell = 0$ , $\ell = 2$ , and $\ell = 4$ are

$$
\begin{array} { l } { { \displaystyle h _ { \mathcal { W } } ^ { j k } [ \ell = 0 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { 3 G } { 5 c ^ { 3 } } \dddot { I ^ { \langle j k \rangle } } - 2 K ^ { j k } \bigg \} , } } \\ { { \displaystyle h _ { \mathcal { W } } ^ { j k } [ \ell = 2 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ - \frac { 1 3 G } { 2 8 c ^ { 3 } } \dddot { I } _ { ~ p } ^ { j } N ^ { \langle p k \rangle } + ( j  k ) \bigg \} , } } \\ { { \displaystyle h _ { \mathcal { W } } ^ { j k } [ \ell = 4 ] = \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { G } { 8 c ^ { 3 } } \dddot { I } _ { p q } N ^ { \langle j k p q \rangle } \bigg \} . } } \end{array}
$$

Note that the logarithmic terms have all canceled out, and that the tail integral $K ^ { j k }$ appears only within the $\ell = 0$ contribution. Tracing the origin of the tail integral, we see that it comes from $\tau ^ { j k } [ 0 , 2 ]$ , the term in $\tau ^ { j k }$ that involves four derivatives of the Newtonian quadrupole moment. This term, the last one in Eq. (11.250), originates from $( - g ) t _ { \mathrm { H } } ^ { j k }$ , and as we have observed previously, it reveals the differences between the light cones of the mathematical flat spacetime and those of the physical curved spacetime. The tail integral, therefore, informs us that the gravitational waves are propagating in a curved spacetime instead of the fictitious flat spacetime of post-Minkowskian theory.

# Final answer

Adding the contributions from $\ell = 0$ , $\ell = 2$ , and $\ell = 4$ , we find that the wave-zone piece of the gravitational-wave field is given by

$$
h _ { \mathcal { W } } ^ { j k } = \frac { 4 G M } { c ^ { 4 } R } \Bigg \{ \frac { 3 G } { 5 c ^ { 3 } } \dddot { I } ^ { \langle j k \rangle } - 2 K ^ { j k } - \frac { 1 3 G } { 2 8 c ^ { 3 } } \bigg ( \dddot { I } _ { ~ p } ^ { j } N ^ { ( p k ) } + \dddot { I } _ { ~ p } ^ { k } N ^ { \langle p j \rangle } \bigg ) + \frac { G } { 8 c ^ { 3 } } \dddot { I } _ { p q } N ^ { \langle j k p q \rangle } \Bigg \} .
$$

From this we may remove any term that will not survive a TT projection. For example, we may use

$$
\dddot { I ^ { j } { } _ { p } } N ^ { \langle p k \rangle } = \dddot { I ^ { j } { } _ { p } } \bigg ( N ^ { p } N ^ { k } - \frac { 1 } { 3 } \delta ^ { p k } \bigg ) \stackrel { \mathrm { \scriptsize ~ m ~ } } { = } - \frac { 1 } { 3 } \dddot { I } ^ { \langle j k \rangle }
$$

and

$$
\dddot { I } _ { p q } N ^ { \langle j k p q \rangle } \equiv \frac { 2 } { 3 5 } \dddot { I } ^ { \ddot { \langle j k \rangle } }
$$

to simplify the expression, which becomes

$$
h _ { \mathcal { W } } ^ { j k } \overset { \mathtt { r } } { = } \frac { 4 G M } { c ^ { 4 } R } \bigg \{ \frac { 1 1 G } { 1 2 c ^ { 3 } } \ddot { I } ^ { \langle j k \rangle } - 2 K ^ { j k } \bigg \} .
$$

To arrive at the final form of Eq. (11.236), we substitute Eq. (11.263) for the tail integral and clean things up by setting $\begin{array} { r } { s = \frac { 1 } { 2 } c \zeta } \end{array}$ , thereby adopting $\zeta$ as a new integration variable. This gives us

$$
h _ { \mathcal { W } } ^ { j k } \equiv \frac { 4 G ^ { 2 } M } { c ^ { 7 } R } \Bigg \{ \frac { 1 1 } { 1 2 } \dddot { I } ^ { \langle j k \rangle } ( \tau ) + \int _ { 0 } ^ { \infty } \ddot { I } ^ { \langle j k \rangle } ( \tau - \zeta ) \ln \frac { \zeta } { \zeta + 2 R / c } d \zeta \Bigg \} ,
$$

and it is easy to show that this is equivalent to Eq. (11.236).

# 11.3.8 Summary: Gravitational-wave field

Our computation of the gravitational-wave field generated by an $N$ -body system is now essentially complete. For easy reference we copy in Box 11.4 the main results obtained in the preceding five subsections.

<table><tr><td>Box 11.4</td><td>Gravitational-wave field to 1.5PN order</td></tr><tr><td></td><td>The gravitational potentials hjk are decomposedaccording to h=h+h， (1) and the near-zone piece is expressed as the multipole expansion h(t,x）=Rat²1 2G d² {0+gN+/N, s</td></tr><tr><td></td><td> in which R := |x|,N := x/R,and τ := t - R/cis etardedtime. Theradiative multipole moments</td></tr><tr><td>are given by A Qjka = Ajka + Akja - Aajk, 1∑Ma(1+ Ajka = c A 1 ∑∑</td><td>=∑Ma（1+）-∑∑ GMAMBp²r +O(c-4), 1 rab A B≠A 贤 u&#x27;ragra</td></tr></table>

(continued overleaf)

$$
\begin{array} { l } { { \displaystyle - \frac { 1 } { 6 c ^ { 3 } } \sum _ { \lambda } \displaystyle { \sum _ { \beta \neq \lambda } G { \cal M } _ { \cal A } M _ { \cal B ^ { \prime } \lambda \beta } } \Biggl [ \displaystyle ( { n _ { \perp \kappa } \cdot v _ { \lambda } } ) { n _ { \lambda \beta } ^ { \prime } n _ { \lambda \beta } ^ { \star } n _ { \lambda \beta } ^ { \circ } } - \displaystyle { 1 1 } { n _ { \lambda \beta } ^ { \prime } n _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } n _ { \lambda } ^ { \circ } } } } \\ { { \mathrm { } } } \\ { { \displaystyle \qquad + 1 { \mathrm { I } v _ { \lambda } ^ { \prime } n _ { \lambda \beta } ^ { \ast } n _ { \lambda \beta } ^ { \circ \prime } n _ { \lambda \beta } ^ { \circ } } \Biggr ] + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle Q ^ { \beta \mu \lambda \nu } \equiv \frac { 1 } { c ^ { 2 } } \sum _ { \lambda } { { \cal M } _ { \cal A } v _ { \lambda } ^ { \prime } n _ { \lambda \beta } ^ { \ast } v _ { \lambda \alpha } ^ { \prime } } { n _ { \lambda } ^ { \beta } } } } \\ { { \mathrm { } } } \\  { \displaystyle \qquad - \frac { 1 } { 2 c ^ { 2 } } \sum _ { \lambda } \displaystyle { \sum _ { \beta \neq \lambda } \frac { G { \cal M } _ { \cal A } { \cal M } _ { \cal B } } { r _ { \lambda \beta } } { n _ { \lambda \beta } ^ { \prime } n _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } } { n _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } } } { \displaystyle { \sum _ { \lambda } ( v _ { \lambda } ^ { \prime } d _ { \lambda \beta } ) } { n _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } } { n _ { \lambda \beta } ^ { \circ } ( v _ { \lambda \beta } ^ { \circ } n _ { \lambda \beta } ^ { \circ } - \delta ^ { \prime } ) } } } \\   \displaystyle + \frac { 1 } { { \mathrm { I } 2 c ^ { 2 } } } \sum _ { \lambda } \displaystyle  G { \cal M } _ { \cal A } { \cal M } _ { \cal B ^ { \prime } \lambda \beta }  n _ { \lambda \beta } ^ { \prime } n _ { \lambda \beta } ^ { \circ } n _  \end{array}
$$

$$
\begin{array} { c } { { \displaystyle Q ^ { j k a b c } \equiv \displaystyle \frac { 1 } { c ^ { 3 } } \displaystyle \frac { \partial } { \partial \tau } \biggl [ \sum _ { A } M _ { A } v _ { A } ^ { j } v _ { A } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } r _ { A } ^ { c } - \displaystyle \frac { 1 } { 2 } \sum _ { A } \sum _ { B \ne A } \frac { G M _ { A } M _ { B } } { r _ { A B } } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { a } r _ { A } ^ { b } r _ { A } ^ { b } r _ { A } ^ { c } } } \\ { { + \displaystyle \frac { 1 } { 4 } \sum _ { A \ { B \ne A } } G M _ { A } M _ { B } r _ { A B } n _ { A B } ^ { j } n _ { A B } ^ { k } r _ { A } ^ { ( a } \left( n _ { A B } ^ { b } n _ { A B } ^ { c ) } - \delta ^ { b c } \right) \biggr ] + { \cal O } ( c ^ { - 5 } ) . } } \end{array}
$$

They are expressed in terms of the mass-energy $M _ { A }$ of each body, its position $r _ { A }$ , and velocity ${ \pmb v } _ { A } ;$ all ${ \mathsf { p } } 0 -$ sition and velocity vectors are evaluated at the retarded time $\tau$ , and the radiative moments are functions of $\tau$ only. We us $\mathring { \iota } r _ { A B } : = | r _ { A } - { \boldsymbol { r } } _ { B } |$ to denote the distance between bodies $A$ and $B$ , and $\mathbf { \delta } _ { \pmb { n } _ { A B } } =$ $( r _ { A } - r _ { B } ) / r _ { A B }$ is a unit vector that points from body $B$ to body $A$ . With this listing of radiative multipole moments, the multipole expansion is accurate through $1 . 5 \mathrm { P N }$ order.

The wave-zone piece is given by the tail integral

$$
h _ { \mathcal { W } } ^ { j k } ( t , x ) \overset { \pi } { = } \frac { 4 G } { c ^ { 4 } R } \frac { G M } { c ^ { 3 } } \int _ { 0 } ^ { \infty } \overset { ( 4 ) } { I } ^ { ( j k ) } ( \tau - \zeta ) \bigg ( \ln \frac { \zeta } { \zeta + 2 R / c } + \frac { 1 1 } { 1 2 } \bigg ) d \zeta ,
$$

which involves the entire past history of the system. It depends on the total gravitational mass of the system, $\begin{array} { r } { M = \sum _ { A } M _ { A } + O ( c ^ { - 2 } ) } \end{array}$ , as well as the Newtonian quadrupole moment of the matter distribution, $\begin{array} { r } { I ^ { j k } = \sum _ { A } M _ { A } r _ { A } ^ { j } r _ { A } ^ { k } , } \end{array}$ which is made tracefree and differentiated four times with respect to its argument. The wave-zone piece makes a contribution at $1 . 5 \mathrm { P N }$ order to the gravitational-wave field.

The computation is essentially complete, but much work remains to be done to turn these expressions into something more concrete. First, the derivatives with respect to $\tau$ must be evaluated, and this will require a large effort. Second, the projection to the transverse subspace must be fully carried out, because our multipole moments still contain pieces that can be removed by acting with $\left( \mathrm { T T } \right) ^ { j k } p q$ . The ultimate goal is to obtain the polarizations $h _ { + }$ and $h _ { \times }$ expressed entirely in terms of the positions $r _ { A }$ and velocities ${ \pmb v } _ { A }$ . We shall proceed toward this goal in the following section.

# 11.4 Gravitational waves emitted by a two-body system

To simplify the task of producing concrete expressions for $h _ { + }$ and $h _ { \times }$ , we choose at this stage to specialize our discussion to a binary system of orbiting bodies. The system will therefore involve the masses $M _ { 1 }$ and $M _ { 2 }$ , the positions $r _ { 1 }$ and $r _ { 2 }$ , and the velocities ${ \pmb v } _ { 1 }$ and ${ \pmb v } _ { 2 }$ . The dynamics of the binary system is described by the post-Newtonian equations of motion obtained back in Sec. 9.3.7.

# 11.4.1 Motion in the barycentric frame

We work in the post-Newtonian barycentric frame $\mathbf { \nabla } \cdot \mathbf { R } = \mathbf { 0 } $ ), and according to Eqs. (9.141), the position vector of each body is given by

$$
\begin{array} { l } { { \pmb { r } _ { 1 } = \displaystyle \frac { M _ { 2 } } { m } \pmb { r } + \frac { \eta \Delta } { 2 c ^ { 2 } } \bigg ( \upsilon ^ { 2 } - \frac { G m } { r } \bigg ) \pmb { r } + O ( c ^ { - 4 } ) , } } \\ { { \pmb { r } _ { 2 } = - \displaystyle \frac { M _ { 1 } } { m } \pmb { r } + \frac { \eta \Delta } { 2 c ^ { 2 } } \bigg ( \upsilon ^ { 2 } - \frac { G m } { r } \bigg ) \pmb { r } + O ( c ^ { - 4 } ) . } } \end{array}
$$

They are expressed in terms of the separation vector $r : = r _ { 1 2 } : = r _ { 1 } - r _ { 2 }$ and the relative velocity $\pmb { v } : = \pmb { v } _ { 1 2 } : = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ ; these have magnitudes $r = | \boldsymbol { r } |$ and $v = | v |$ , respectively. We have re-introduced the mass parameters

$$
\begin{array} { l } { m : = M _ { 1 } + M _ { 2 } , } \\ { \displaystyle \eta : = \frac { M _ { 1 } M _ { 2 } } { ( M _ { 1 } + M _ { 2 } ) ^ { 2 } } , } \\ { \Delta : = \displaystyle \frac { M _ { 1 } - M _ { 2 } } { M _ { 1 } + M _ { 2 } } . } \end{array}
$$

Differentiation of Eqs. (11.271) returns the velocity vector of each body:

$$
\begin{array} { l } { { \displaystyle v _ { 1 } = \frac { M _ { 2 } } { m } \pmb { v } + \frac { \eta \Delta } { 2 c ^ { 2 } } \bigg [ \Big ( \pmb { v } ^ { 2 } - \frac { G m } { r } \Big ) \pmb { v } - \frac { G m } { r } \dot { \pmb { r } } \pmb { n } \bigg ] + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle v _ { 2 } = - \frac { M _ { 1 } } { m } \pmb { v } + \frac { \eta \Delta } { 2 c ^ { 2 } } \bigg [ \Big ( \pmb { v } ^ { 2 } - \frac { G m } { r } \Big ) \pmb { v } - \frac { G m } { r } \dot { \pmb { r } } \pmb { n } \bigg ] + O ( c ^ { - 4 } ) , } } \end{array}
$$

where ${ \dot { r } } : = n \cdot v$ is the radial component of the velocity vector, and ${ \pmb n } : = { \pmb r } / r$ is a unit vector that points from body 2 to body 1. To arrive at these expressions we have involved the relative acceleration $\pmb { a } : = \pmb { a } _ { 1 } - \pmb { a } _ { 2 }$ , which according to Eq. (9.142) is given by

$$
\begin{array} { c } { { \displaystyle { a = - \frac { G m } { r ^ { 2 } } n - \frac { G m } { c ^ { 2 } r ^ { 2 } } \left\{ \left[ ( 1 + 3 \eta ) v ^ { 2 } - \frac { 3 } { 2 } \eta \dot { r } ^ { 2 } - 2 ( 2 + \eta ) \frac { G m } { r } \right] n \right. } } } \\ { { \left. - \ 2 ( 2 - \eta ) \dot { r } v \right\} + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

# 11.4.2 Radiative multipole moments

We make the substitutions within the radiative multipole moments of Box 11.4 and simplify the resulting expressions. The sums that appear in these equations must be specialized to two bodies, and in these we set $r _ { 1 2 } = r _ { 2 1 } = r$ and ${ \pmb n } _ { 1 2 } = - { \pmb n } _ { 2 1 } = { \pmb n }$ . In the course of these (lengthy, but straightforward) computations we encounter various functions of $M _ { 1 }$ and $M _ { 2 }$ that can be rewritten in terms of the mass parameters of Eqs. (11.272). For example, it is easy to show that

$$
\begin{array} { l } { { \displaystyle \frac { M _ { 1 } ^ { 2 } + M _ { 2 } ^ { 2 } } { ( M _ { 1 } + M _ { 2 } ) ^ { 2 } } = 1 - 2 \eta , } } \\ { { \displaystyle \frac { M _ { 1 } ^ { 3 } + M _ { 2 } ^ { 3 } } { ( M _ { 1 } + M _ { 2 } ) ^ { 3 } } = 1 - 3 \eta , } } \\ { { \displaystyle \frac { M _ { 1 } ^ { 4 } - M _ { 2 } ^ { 4 } } { ( M _ { 1 } + M _ { 2 } ) ^ { 4 } } = \Delta ( 1 - 2 \eta ) , } } \end{array}
$$

and we make many such substitutions while simplifying our expressions.

We obtain

$$
\begin{array} { r l } { \varphi ^ { \mathrm { i d } } - \varphi \eta \Bigg | \Big | + \frac { 1 } { 2 } \Bigg ( 1 - \sin \theta \frac { \psi } { \psi } \Bigg ) ^ { 2 } - \frac { 1 } { 2 } \Bigg ( 1 - 2 \sin \theta \frac { \psi } { \psi } + \theta + G ^ { \zeta } \eta ^ { \zeta } \Bigg ) \Bigg | \psi ^ { \mathrm { i d } } + \eta ^ { \mathrm { i d } } } & { } \\ { \varphi ^ { \mathrm { i d } } - \theta ^ { \zeta } \eta ^ { \mathrm { i d } } \Bigg ) ^ { 2 } } & { = \frac { \sin \theta } { \psi } \Bigg \{ \psi ^ { \mathrm { i d } } - \theta ^ { \zeta } \eta ^ { \mathrm { i d } } - \psi ^ { \mathrm { i d } } \psi ^ { \mathrm { i d } } \Bigg \} \psi ^ { \mathrm { i d } } + \frac { G ^ { \zeta } \eta ^ { \mathrm { i d } } } { \psi ^ { \mathrm { i d } } } } \\ & { \qquad - \bigg [ \frac { \sqrt { 3 } } { 2 } \Big ( 1 - 2 \sin \theta \frac { \psi } { \psi } \Big ) ^ { 2 } + \frac { \sqrt { 3 } } { 2 } \Big ( 1 + 2 \sin \theta \frac { \psi } { \psi } \Big ) ^ { 2 } \sin ^ { 2 } \psi ^ { \mathrm { i d } } - \mu ^ { \zeta } \eta ^ { \zeta } \Bigg ] \psi ^ { \mathrm { i d } } } \\ & { \qquad + \bigg [ \frac { \sqrt { 3 } } { 2 } \Big ( 1 - 8 \sin \theta \frac { \psi } { \psi } \Big ) ^ { 2 } + \frac { \sqrt { 3 } } { 2 } \Big ( 1 + 2 \sin \theta \frac { \psi } { \psi } \Big ) ^ { 2 } \sin ^ { 2 } \psi ^ { \mathrm { i d } } + \frac { \sqrt { 3 } } { 2 } \bigg ] \psi ^ { \mathrm { i d } } } \\ &  \qquad + \frac { \sqrt { 3 } } { 2 } \left( 1 - 6 \sin \theta \frac { \psi } { \psi } \right) ^ { 2 } \sin ^ { 2 } \psi ^ { \mathrm { i d } } + 2 \theta + \frac { \sqrt { 3 } } { 2 } \bigg ] \psi ^ { \mathrm { i d } } \\ { \varphi ^ { \mathrm { i d } } - \varphi ^ { \mathrm { i d } } \Bigg \{ 1 } & { \cos \theta ^ { \zeta } \eta ^ { \zeta } , } \\ &  \qquad - \frac { 1 } { 2 } \sin \theta \cos \theta ^ { \zeta } \eta ^ { \zeta } \Bigg \} \\ &  \qquad - \frac { 1 } { 3 } \frac { \sin \theta }  \psi \end{array}
$$

We observe that in order to simplify the writing, we have replaced the qualified equality sign $\stackrel { \pi } { = }$ (“equal after a TT projection”) by the usual equality sign.

# 11.4.3 Computation of retarded-time derivatives

The near-zone contribution to $h ^ { j k }$ is given by Eq. (2) of Box 11.4, and in this we must insert the radiative multipole moments displayed in the preceding subsection; the computation involves taking two retarded-time derivatives of these moments. Similarly, the wave-zone contribution to $h ^ { j k }$ is given by Eq. (3) of Box 11.4, and this involves taking four retardedtime derivatives of $I ^ { j k } = \eta m r ^ { j } r ^ { k }$ . Our immediate task in this subsection is to compute these derivatives.

The general strategy is clear. The radiative multipole moments of Eqs. (11.276) are expressed explicitly in terms of the position and velocity vectors, and these are functions of the retarded time $\tau$ . Differentiating with respect to $\tau$ therefore involves taking derivatives of the position and velocity vectors. Differentiating $r$ gives $\pmb { v }$ , and differentiating $\pmb { v }$ gives $\pmb { a }$ , the post-Newtonian acceleration vector of Eq. (11.274). After making this substitution, the result is once more expressed in terms of $r$ and $\pmb { v }$ , and is ready for further differentiation.

More concretely, consider the task of computing $\ddot { Q } ^ { j k }$ . The quadrupole moment is a function of $r$ at order $c ^ { 0 }$ , and a function of $r$ and $\pmb { v }$ at order $c ^ { - 2 }$ . Taking a first derivative with respect to $\tau$ produces terms in $r$ and $\pmb { v }$ at order $c ^ { 0 }$ , and terms in $r , \ v$ , and $\pmb { a }$ at order $c ^ { - 2 }$ . In the post-Newtonian term we can substitute the Newtonian expression for the acceleration vector, $\pmb { a } = - G m \pmb { r } / r ^ { 3 } + O ( c ^ { - 2 } )$ , because the error incurred occurs at order $c ^ { - 4 }$ in $\dot { Q } ^ { j k }$ . The end result is a function of $r$ and $\pmb { v }$ at order $c ^ { 0 }$ , another function of $r$ and $\pmb { v }$ at order $c ^ { - 2 }$ , and neglected terms at order $c ^ { - 4 }$ . Taking a second derivative introduces the acceleration vector at orders $c ^ { 0 }$ and $c ^ { - 2 }$ . In the Newtonian term we must now substitute the post-Newtonian expression for the acceleration vector, because its pn term will influence the $c ^ { - 2 }$ piece of $\ddot { Q } ^ { j k }$ ; but we are still allowed to insert the Newtonian acceleration within the $c ^ { - 2 }$ piece of the second derivative. The end result for $\ddot { Q } ^ { j k }$ is a function of $r$ and $\pmb { v }$ at order $c ^ { 0 }$ , and another function of $r$ and $\pmb { v }$ at order $c ^ { - 2 }$ .

Derivatives of other multipole moments are computed in a similar way. These computations are tedious and lengthy, but they are completely straightforward. They are aided by the identities

$$
v \dot { v } = - \frac { G m } { r ^ { 2 } } \dot { r } + O ( c ^ { - 2 } ) , \qquad r \ddot { r } = v ^ { 2 } - \dot { r } ^ { 2 } - \frac { G m } { r } + O ( c ^ { - 2 } ) ,
$$

which are consequences of the Newtonian expression for the acceleration vector.

We display the final results:

$$
\begin{array} { c } { { \displaystyle { \ddot { Q } ^ { j k } = 2 \eta m \left( v ^ { j } v ^ { k } - \frac { G m } { r } n ^ { j } n ^ { k } \right) } } } \\ { { + \displaystyle { \frac { \eta m } { c ^ { 2 } } \left[ \left[ - \frac { 1 } { 2 } ( 7 + 2 \eta ) v ^ { 2 } + \frac { 3 } { 2 } ( 1 - 2 \eta ) \dot { r } ^ { 2 } + \frac { 1 9 } { 2 } \frac { G m } { r } \right] \frac { G m } { r } n ^ { j } n ^ { k } \right. } } } \\ { { + \left[ ( 1 - 3 \eta ) v ^ { 2 } - ( 1 - 2 \eta ) \frac { G m } { r } \right] v ^ { j } v ^ { k } + ( 3 + 2 \eta ) \frac { G m } { r } \dot { r } \left( v ^ { j } n ^ { k } + n ^ { j } v ^ { k } \right) \Bigg ] } } \\ { { + O ( c ^ { - 4 } ) , } } \end{array}
$$

$$
\begin{array} { r l } { \iota _ { 1 } ^ { \mathrm { o u t } } } & { \times \delta _ { 1 } ^ { ( 2 ) } \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ { \iota _ { 2 } ^ { \mathrm { o u t } } } & { \times \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 3 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 2 } , } \\ & { + \left[ \frac { \partial \alpha _ { 1 } } { \partial x } \right] ^ { 3 } , } \\ & { - \left[ \alpha _ { 2 } - \alpha _ { 2 } \right] ^ { 3 } , } \\ & { + \left[ \alpha _ { 2 } - \alpha _ { 3 } \right] ^ { 2 } , } \\ & { + \left[ \alpha _ { 3 } - \alpha _ { 3 } \right] ^ { 3 } , } \\ & { + \left[ \alpha _ { 4 } - \alpha _ { 4 } \right] ^ { 4 } , } \\ & { \left[ \alpha _ { 4 } - \alpha _ { 5 } \right] ^ { 4 } , } \\ { \theta _ { 5 } ^ { ( 4 ) } } & { \times \left[ \alpha _ { 4 } - \alpha _ { 5 } \right] ^ { 2 } , } \\ & { + \left[ \alpha _ { 5 } - \alpha _ { 6 } \right] ^ { 4 } , } \\ & { + \left[ \alpha _ { 7 } - \alpha _ { 5 } \right] ^ { 6 } , } \\ { \theta _ { 7 } ^ { ( 4 ) } } & { \times \left[ \alpha _ { 1 } - \alpha _ { 7 } \right] ^ { 2 } , } \\ & { + \left[ \alpha _ { 1 } - \alpha _ { 2 } \right] ^ { 2 } , } \\ & { + \left[ \alpha _ { 2 } - \alpha _ { 3 } \right] ^ { 2 } , } \\ & { - \left[ \alpha _ { 1 } - \alpha _ { 2 } \right] ^ { 3 } , } \\ & { - \left[ \alpha _ { 2 } - \alpha _ { 3 } \right] ^ { 2 } , } \\ & { - \left[ \alpha _ { 2 } - \alpha _ { 3 } \right] ^ { 2 } , } \\ &  -  \end{array}
$$

$$
\begin{array} { r l } & { \quad - \frac { \eta } { \gamma } ( 1 - \eta ) _ { m } ^ { \prime \prime } - \frac { \eta } { \gamma } \frac { \eta } { \gamma } \frac { \epsilon } { \epsilon } \eta ^ { \prime \prime } \epsilon ^ { \prime \prime } } \\ & { = - \frac { \eta } { \gamma } \frac { 1 } { 3 } ( 1 - \eta ) _ { m } ^ { \prime \prime } \frac { \epsilon } { \epsilon } \eta ^ { \prime \prime } \epsilon ^ { \prime \prime } + \epsilon ^ { \prime \prime } \eta ^ { \prime \prime } \epsilon ^ { \prime \prime } - \epsilon ^ { \prime \prime } \eta ^ { \prime } \epsilon ^ { \prime \prime } - \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime } \eta ^ { \prime } } \\ & { \quad + \lambda ^ { ( 1 ) } - \eta \epsilon ) _ { m } ^ { \prime \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \lambda ^ { ( 1 ) } - \lambda ^ { ( 1 ) } \frac { \epsilon } { \gamma } \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime } \epsilon ^ { \prime \prime } } \\ & { \quad - \frac { \eta } { \gamma } ( 1 - \eta ) _ { m } ^ { \prime \prime } \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \lambda ^ { ( 1 ) } \epsilon ^ { ( 1 ) } + \frac { \eta } { \gamma } \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime } \epsilon ^ { \prime \prime } - \lambda ^ { ( 1 ) } \frac { \epsilon } { \gamma } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \epsilon ^ { \prime \prime \prime } } \\ &  \quad + \frac { \eta } { \gamma } \epsilon ^ { \prime \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \lambda ^ { ( 1 ) } \epsilon ^ { \prime \prime } \epsilon ^ { \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } + \frac { \eta } { \gamma } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime \prime } \epsilon ^ { \prime } \epsilon ^ { \prime } \epsilon ^  \ \end{array}
$$

(continued overleaf)

$$
\begin{array} { r l r } {  { + \frac { 2 } { 3 } ( 1 - 2 \eta ) \frac { G m } { r } w ^ { 3 } \nu ^ { 5 } ( \nu ^ { 7 } \nu ^ { 8 } \tau ^ { 8 } + \alpha ^ { 4 } \nu ^ { 8 } \nu ^ { 6 } + \nu ^ { 8 } \nu ^ { 7 } ) } }  \\ & { } & { + \frac { 1 } { 2 } ( 1 - 2 \eta ) \frac { G m } { r } ( \nu ^ { 6 } \nu ^ { 4 } + \nu ^ { 6 } ) ( \nu ^ { 1 0 } \nu ^ { 8 } \tau ^ { 4 } + \nu ^ { 6 } \nu ^ { 6 } + \nu ^ { 6 } \nu ^ { 7 } ) } \\ & { } & { - 8 ( 1 - 2 \eta ) \nu ^ { 4 } z ^ { 3 } \nu ^ { 6 } \nu ^ { 6 } \nu ^ { 7 } - \frac { 9 } { 2 } ( 1 - 2 \eta ) \frac { G m } { r } \nu ^ { 3 } \nu ^ { 7 } ( \nu ^ { 6 } \nu ^ { 6 } + \nu ^ { 1 0 } \nu ^ { 6 } + \nu ^ { 8 } \nu ^ { 6 } ) } \\ & { } & { + \frac { 3 } { 2 } ( 1 - 2 \eta ) \frac { G m ^ { 2 } } { r } w ^ { 3 } \nu ^ { 4 } \nu ^ { 6 } \nu ^ { 6 } + \frac { 9 } { 4 } ( \nu ^ { 1 0 } \eta ^ { 2 } - 1 ) \nu ^ { 1 1 } z ^ { 3 } + 1 0 ^ { 2 } \frac { G m ^ { 2 } } { r } \nu ^ { 1 1 } z ^ { 3 } \mu ^ { 6 } \nu ^ { 4 } + \nu ^ { 1 1 } z ^ { 3 } } \\ & { } & { + \frac { 3 } { 2 } ( 1 - 2 \eta ) \frac { G m ^ { 2 } } { r } w ^ { 4 } \nu ^ { 6 } \nu ^ { 4 } + \frac { 9 } { 4 } ( 3 \eta ^ { 2 } - 1 ) \nu ^ { 1 2 } z ^ { 3 } + 1 0 ^ { 2 } \frac { G m ^ { 2 } } { r } \nu ^ { 1 1 } z ^ { 3 } \mu ^ { 6 } \nu ^ { 4 } ) } \\ & { } &  - \frac { 1 } { 4 } \Big ( 3 \nu ^ { 3 } - \nu ^ { 5 } z ^ { 3 } + \frac { G m ^ { 2 } } { r } \Big ) \frac { G m } { r } \Big ( \nu ^ { 2 } \nu ^ { 4 } + \nu ^ { 5 } \nu ^ { 5 } \Big ) \mu ^ { 1 2 } \\ & { } &  - \frac { 3 } { 4 } \Big ( 3 z  \end{array}
$$

In addition, we have that

$$
\begin{array} { c } { { \stackrel { \scriptscriptstyle ( 4 ) } { I ^ { j k } } = 2 \eta m \displaystyle \frac { G m } { r ^ { 3 } } \biggl [ \biggl ( 3 v ^ { 2 } - 1 5 \dot { r } ^ { 2 } + \frac { G m } { r } \biggr ) n ^ { j } n ^ { k } + 9 \dot { r } \bigl ( v ^ { j } n ^ { k } + n ^ { j } v ^ { k } \bigr ) - 4 v ^ { j } v ^ { k } \biggr ] } } \\ { { + O ( c ^ { - 2 } ) . } } \end{array}
$$

# 11.4.4 Gravitational-wave field

We may now substitute Eqs. (11.278) and (11.279) into Eqs. (2) and (3) of $\mathrm { B o x } 1 1 . 4$ and obtain the gravitational-wave field. These computations are straightforward, and we express the result as

$$
\begin{array} { c } { { h ^ { j k } ( t , { \bf x } ) = { \displaystyle \frac { 2 \eta G m } { c ^ { 4 } R } } \bigg [ { \cal A } ^ { j k } [ 0 \mathrm { p N } ] + { \cal A } ^ { j k } [ 0 . 5 \mathrm { p N } ] + { \cal A } ^ { j k } [ 1 \mathrm { p N } ] } } \\ { { + { \cal A } ^ { j k } [ 1 . 5 \mathrm { p N } ] + { \cal A } ^ { j k } [ \mathrm { t a i l } ] + { \cal O } ( c ^ { - 4 } ) \bigg ] , } } \end{array}
$$

in which we group terms according to their post-Newtonian order (the last term, with the label “tail,” is also of $1 . 5 \mathrm { { P N } }$ order). We have

$$
\begin{array} { r l } & { ~ \mathcal { A } ^ { j k } [ 0 \mathrm { P N } ] = 2 \left[ v ^ { j } v ^ { k } - \displaystyle \frac { G m } { r } n ^ { j } n ^ { k } \right] , } \\ & { ~ { d } ^ { j k } [ 0 . 5 \mathrm { P N } ] = \displaystyle \frac { \Delta } { c } \left[ 3 \displaystyle \frac { G m } { r } ( n \cdot N ) \big ( v ^ { j } n ^ { k } + n ^ { j } v ^ { k } - \dot { r } n ^ { j } n ^ { k } \big ) \right. } \\ & { ~ \left. ~ + ( v \cdot N ) \bigg ( - 2 v ^ { j } v ^ { k } + \displaystyle \frac { G m } { r } n ^ { j } n ^ { k } \bigg ) \right] , } \end{array}
$$

(continued overleaf)

$$
\begin{array} { r l } { \mathcal { A } ^ { k } [ \{ 1 : e \} ] = } & { \frac { 1 } { c } \Bigg | \frac { 1 } { \Delta x } \Bigg \{ \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi \xi \xi ^ { k } \Bigg \} , } \\ & { + \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi \xi \xi ^ { k } \Bigg \} = } \\ & { + \frac { 3 } { c } \frac { \partial } { c } \frac { \partial } { \partial x } \Bigg \{ \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { \xi } { c } \frac { \partial \xi \xi \xi ^ { k } } { \partial x } \xi ^ { k } } \\ & { + \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi \xi \Bigg \} = } \\ & { + \frac { 3 } { c } \frac { \partial } { \partial x } \Bigg \{ \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi ^ { k } \Bigg \} = } \\ & { + \frac { 3 } { c } \frac { \partial } { \partial x } \Bigg \{ \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi \xi ^ { k } \Bigg \} = } \\ & { + \frac { 3 } { c } \frac { \partial } { \partial x } \Bigg \{ \Gamma _ { \mu } ^ { k } \left( \Delta \xi \right) = } & { \frac { 3 } { c } \frac { \partial } { \partial x } \xi \xi ^ { k } \Bigg \} = } \\ & { + \left( y - 1 \frac { 3 } { c } y \xi ^ { k } - \frac { 3 } { c } \frac { \partial ^ { 2 } \xi \xi ^ { k } } { \partial x } \right) \Bigg \{ 1 - 1 6 x \xi ^ { k } \left( - 4 y \xi \xi ^ { k } \left( - 4 x \xi ^ { k } \right) \right) \xi \xi \xi ^ { k } \Bigg \} \mathrm { , ~ } } \\ &  + \left( y - 1 \frac { 3 } { c } y ^ { k } - \frac { 3 } { c } \frac { \partial ^ { 2 } \xi ^ { k } } { \partial x } \right) \xi \xi ^ { k } \end{array}
$$

$$
\begin{array}{c} \begin{array}{c} \begin{array} { r l } { \Phi ^ { * } [ [ \begin{array} { l l l l } { \mathbf { y } } & { 1 } & { - \mathbf { y } } & { \rho ^ { * } } \\ { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} ] } \\ { \Phi ^ { * } [ [ \begin{array} { l l l l } { \mathbf { y } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} ] } & { \Phi ^ { * } [ [ \begin{array} { l } { \mathbf { y } } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} ] } \\ { \Phi ^ { * } [ [ \begin{array} { l l l l } { \mathbf { y } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} ] } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} ]  \\ { \Phi ^ { * } [ [ \begin{array} { l } { \mathbf { y } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \end{array} ] } & { 0 } \\ { \Phi ^ { * } [ [ \begin{array} { l l l l } { \mathbf { y } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} ] } & { 0 } \end{array} ]  & { \Phi ^ { * } [ [ \begin{array} { l } { \mathbf { x } } \\ { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} ] } \\ { \Phi ^ { * } [ [ \begin{array} { l } { \mathbf { y } } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} ] } & { 0 } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle { \cal A } ^ { j k } [ \mathrm { t a i l } ] = \frac { 4 G m } { c ^ { 3 } } \int _ { 0 } ^ { \infty } \left[ \frac { G m } { r ^ { 3 } } \biggl [ \biggl ( 3 v ^ { 2 } - 1 5 \dot { r } ^ { 2 } + \frac { G m } { r } \biggr ) n ^ { j } n ^ { k } + 9 \dot { r } \bigl ( v ^ { j } n ^ { k } + n ^ { j } v ^ { k } \bigr ) \right. } } \\ { { \displaystyle \left. \qquad - 4 v ^ { j } v ^ { k } \right] \biggr ] _ { \tau - \zeta } \biggl [ \mathrm { l n } \biggl ( \frac { \zeta } { \zeta + 2 R / c } \biggr ) + \frac { 1 1 } { 1 2 } \biggr ] d \zeta . \qquad ( 1 \mathrm { ~ f ~ r ~ e ~ c ~ e ~ s ~ } ) } } \end{array}
$$

The gravitational-wave field is expressed in terms of the separation vector $r = r _ { 1 } - r _ { 2 }$ , the relative velocity $\pmb { v } = \pmb { v } _ { 1 } - \pmb { v } _ { 2 }$ , the radial velocity ${ \dot { r } } = \pmb { n } \cdot \pmb { v }$ , and the mass parameters $m =$ $M _ { 1 } + M _ { 2 }$ , $\eta = M _ { 1 } M _ { 2 } / m ^ { 2 }$ , and $\Delta = ( M _ { 1 } - M _ { 2 } ) / m$ . In addition, $h ^ { j k }$ depends on distance $R : = | { \boldsymbol { x } } |$ , retarded time $\tau = t - R / c$ , and on the angular vector $N : = x / R$ that specifies the direction from the barycenter to the field point $_ x$ . In the tail integral the terms within the large round brackets are evaluated at $\tau - \zeta$ instead of $\tau$ , and the integration from $\zeta = 0$ to $\zeta = - \infty$ involves the entire past history of the two-body system.

# 11.4.5 Polarizations

Our final task is to carry out the projection to the transverse subspace, and extract the gravitational-wave polarizations

$$
\begin{array} { r } { h _ { + , \times } = \displaystyle \frac { 2 \eta G m } { c ^ { 4 } R } \bigg [ A _ { + , \times } [ 0 \mathrm { P N } ] + A _ { + , \times } [ 0 . 5 \mathrm { P N } ] + A _ { + , \times } [ 1 \mathrm { P N } ] } \\ { + A _ { + , \times } [ 1 . 5 \mathrm { P N } ] + A _ { + , \times } [ \mathrm { t a i l } ] + O ( c ^ { - 4 } ) \bigg ] } \end{array}
$$

from Eq. (11.280). We adopt the same conventions as in Sec. 11.2.2. We re-introduce the “orbit-adapted” coordinate system $( x , y , z )$ and express $\pmb { n }$ in terms of $\phi ( \tau )$ , the (retarded) angular position of the relative orbit. The expression is $\pmb { n } = [ \cos \phi , \sin \phi , 0 ]$ , and to this we adjoin another basis vector $\lambda = [ - \sin \phi , \cos \phi , 0 ]$ , which also lies in the fixed orbital plane. We express the relative position and velocity vectors as

$$
\begin{array} { r } { r = r \pmb { n } , \qquad \pmb { v } = \dot { r } \pmb { n } + r \dot { \phi } \pmb { \lambda } , } \end{array}
$$

where $r ( \tau )$ is the (retarded) distance between the two bodies. And we re-introduce the directions

$$
\begin{array} { r l } & { \pmb { e } _ { X } = [ \cos \omega , - \sin \omega , 0 ] , } \\ & { \pmb { e } _ { Y } = [ \cos \iota \sin \omega , \cos \iota \cos \omega , - \sin \iota ] , } \\ & { \pmb { e } _ { Z } = [ \sin \iota \sin \omega , \sin \iota \cos \omega , \cos \iota ] = N , } \end{array}
$$

which depend on the polar angles $( \iota , \omega )$ that specify the direction of the detector relative to the $( x , y , z )$ system. We use $e _ { X }$ and $e _ { Y }$ as a vectorial basis in the subspace transverse to the direction of propagation, and let

$$
\begin{array} { r } { h _ { + } = \frac { 1 } { 2 } \big ( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \big ) h _ { j k } , } \\ { h _ { \times } = \frac { 1 } { 2 } \big ( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \big ) h _ { j k } , } \end{array}
$$

denote the gravitational-wave polarizations. The construction extends to each $A _ { + }$ and $A _ { \times }$ defined by Eq. (11.282).

The manipulations that return $h _ { + }$ and $h _ { \times }$ from Eqs. (11.280) and (11.281) are straightforward, but as usual they are long and tedious. The expressions that result from $A ^ { j k } [ 0 \mathrm { P N } ]$ are simple, and they can easily be displayed here:

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { + } [ 0 { \bf P } { \bf N } ] = \frac { 1 } { 2 } \big [ \dot { r } ^ { 2 } + ( r \dot { \phi } ) ^ { 2 } - ( G M / r ) \big ] S ^ { 2 } } } \\ { ~ } \\ { { \displaystyle ~ + \frac { 1 } { 2 } \big [ \dot { r } ^ { 2 } - ( r \dot { \phi } ) ^ { 2 } - ( G M / r ) \big ] ( 1 + C ^ { 2 } ) \cos 2 \psi } } \\ { { \displaystyle ~ - \dot { r } ( r \dot { \phi } ) ( 1 + C ^ { 2 } ) \sin 2 \psi , } } \\ { { \displaystyle { \cal A } _ { \times } [ 0 { \bf P } { \bf N } ] = \big [ \dot { r } ^ { 2 } - ( r \dot { \phi } ) ^ { 2 } - ( G M / r ) \big ] C \sin 2 \psi + 2 \dot { r } ( r \dot { \phi } ) C \cos 2 \psi } , } \end{array}
$$

where $S : = \sin \iota , \ C : = \cos \iota$ , and $\psi : = \phi ( \tau ) + \omega$ . The polarizations associated with $A ^ { j k }$ [tail] are also relatively simple:

$$
\begin{array}{c} \begin{array} { r l } & { \begin{array} { r l } & { A _ { + } [ \mathrm { n a i l } ] = \frac { G m } { c ^ { 3 } } S ^ { 2 } \displaystyle \int _ { 0 } ^ { \infty } [ \frac { G m } { r ^ { 3 } } [ 2 \dot { r } ^ { 2 } - ( r \dot { \phi } ) ^ { 2 } + ( G M / r ) ] \biggr | _ { \tau = - \tau } \Xi d \xi } \\ & { \qquad + \frac { G m } { c ^ { 3 } } ( 1 + C ^ { 2 } ) \displaystyle \int _ { 0 } ^ { \infty } [ \frac { G m } { r ^ { 3 } } [ 2 \dot { r } ^ { 2 } + 7 ( r \dot { \phi } ) ^ { 2 } + ( G M / r ) ] \cos { 2 \psi } ] _ { \tau = - \tau } \Xi d \xi } \end{array} } \\ & { \qquad - 1 0 \frac { G m } { c ^ { 3 } } ( 1 + C ^ { 2 } ) \displaystyle \int _ { 0 } ^ { \infty } [ \frac { G m } { r ^ { 3 } } \dot { r } ( r \dot { \phi } ) \sin { 2 \psi } ] _ { \tau = - \tau } \Xi d \xi , \qquad ( 1 1 . 2 8 \times \tau ) } \\ & { \qquad + \frac { G m } { c ^ { 3 } } C \displaystyle \int _ { 0 } ^ { \infty } [ \frac { G m } { r ^ { 3 } } [ 2 \dot { r } ^ { 2 } + 7 ( r \dot { \phi } ) ^ { 2 } + ( G M / r ) ] \sin { 2 \psi } ] _ { \tau = \xi } \Xi d \xi } \\ & { \qquad + 2 0 \frac { G m } { c ^ { 3 } } C \displaystyle \int _ { 0 } ^ { \infty } [ \frac { G m } { r ^ { 3 } } \dot { r } ( r \dot { \phi } ) \cos { 2 \psi } ] _ { \tau = \xi } \Xi d \xi , } \end{array}  \end{array}
$$

where

$$
\Xi : = \ln \left( \frac { \zeta } { \zeta + 2 R / c } \right) + \frac { 1 1 } { 1 2 } .
$$

The expressions for the remaining polarizations are much, much larger, and we shall not display them here.

# 11.4.6 Specialization to circular orbits

# Circular motion

In this subsection we make a further specialization to circular orbital motion. This is defined by the condition

$$
\dot { r } = 0 ,
$$

so that the two bodies move while maintaining a constant relative separation. This is undoubtedly a restriction on all possible motions, but more than this, Eq. (11.289) is also an approximation, because as the system loses energy to gravitational radiation (an effect examined in Chapter 12), the orbital separation slowly decreases, and $\dot { r }$ should actually be negative even for orbits that are otherwise circular. But because this radiation-reaction effect appears at $2 . 5 \mathrm { { p N } }$ order in the equations of motion, we are justified to neglect it here.

The post-Newtonian motion of a binary system in circular orbit was described back in Sec. 10.1.2. There we showed that the angular velocity $\Omega : = \dot { \phi }$ of an orbit of radius $r$ is a constant given by

$$
\Omega ^ { 2 } = \frac { G m } { r ^ { 3 } } \biggl [ 1 - ( 3 - \eta ) \frac { G m } { c ^ { 2 } r } + { \cal O } ( c ^ { - 4 } ) \biggr ] .
$$

This is a post-Newtonian generalization of the usual Keplerian relation $\Omega ^ { 2 } = G m / r ^ { 3 }$ . (When radiation-reaction effects are included, $r$ slowly decreases, and this causes $\Omega$ to slowly increase.) It follows that the orbital velocity $v = r \Omega$ is given by

$$
v ^ { 2 } = { \frac { G m } { r } } \biggl [ 1 - ( 3 - \eta ) { \frac { G m } { c ^ { 2 } r } } + { \cal O } ( c ^ { - 4 } ) \biggr ] .
$$

# Post-Newtonian expansion parameter

The post-Newtonian expansion of the gravitational-wave field is formally an expansion in powers of $c ^ { - 1 }$ , but physically it is an expansion in powers of a dimensionless quantity such as $v / c$ . There are many such quantities that could be adopted as an expansion parameter. Equations (11.290) and (11.291) suggest, for example, that $\sqrt { G m / ( c ^ { 2 } r ) }$ could be selected, and this would indeed be a valid substitute for $v / c$ . Another choice is

$$
\beta : = \left( \frac { G m \Omega } { c ^ { 3 } } \right) ^ { 1 / 3 } ,
$$

which has the important advantage of being defined in terms of the orbital frequency $\Omega$ . As we shall see below, $\Omega$ is intimately related to the frequency of the gravitational waves, and it can therefore be measured directly. This is unlike $v$ or $r$ , which are coordinate-dependent variables that cannot be measured. It is easy to show, using Eqs. (11.290) and (11.291), that

$$
\upsilon / c = \beta \biggl [ 1 - \frac { 1 } { 3 } ( 3 - \eta ) \beta ^ { 2 } + O ( \beta ^ { 4 } ) \biggr ]
$$

and

$$
{ \frac { G m } { c ^ { 2 } r } } = \beta ^ { 2 } \biggl [ 1 + { \frac { 1 } { 3 } } ( 3 - \eta ) \beta ^ { 2 } + O ( \beta ^ { 4 } ) \biggr ] .
$$

We shall henceforth adopt $\beta$ as a meaningful post-Newtonian parameter, and re-express the gravitational-wave polarizations of Eq. (11.282) as expansions in powers of $\beta$ .

# Gravitational-wave polarizations

The polarizations produced by a binary system in circular orbit are obtained by following the general recipe described in Sec. 11.4.5, making use of Eqs. (11.289), (11.293), and

(11.294). After expanding in powers of $\beta$ and evaluating the tail integrals (as detailed below), we arrive at

$$
\begin{array} { l } { \displaystyle h _ { + , \times } = \frac { 2 \eta G m } { c ^ { 2 } R } \bigg ( \frac { G m \Omega } { c ^ { 3 } } \bigg ) ^ { 2 / 3 } H _ { + , \times } , } \\ { \displaystyle H _ { + , \times } : = H _ { + , \times } ^ { [ 0 ] } + \Delta \beta H _ { + , \times } ^ { [ 1 / 2 ] } + \beta ^ { 2 } H _ { + , \times } ^ { [ 1 ] } + \Delta \beta ^ { 3 } H _ { + , \times } ^ { [ 3 / 2 ] } + \beta ^ { 3 } H _ { + , \times } ^ { \mathrm { t a i l } } + O ( \beta ^ { 4 } ) , } \end{array}
$$

where

$$
\begin{array} { r l } & { \bar { H } _ { + } ^ { ( q ) } = - ( 1 + \mathcal { C } ^ { 2 } ) \cos 2 9 , } \\ & { \bar { H } _ { 1 } ^ { ( 1 1 2 ) } = - \frac { 1 } { 8 } S ( 5 + G ^ { \prime } ) \cos 9 + \frac { 9 } { 8 } S ( 1 + \mathcal { C } ^ { \prime } ) \cos 3 \Psi , } \\ & { \bar { H } _ { + } ^ { ( 1 1 ) } = \frac { 1 } { 6 } \bigg [ ( 1 9 + \mathcal { C } ^ { 2 } - 2 \mathcal { C } ^ { \mathrm { c } } ) - ( 1 9 - 1 1 \mathcal { C } ^ { 2 } - 6 \mathcal { C } ^ { \mathrm { c } } ) \eta \bigg ] \cos 2 9 } \\ & { \qquad - \frac { 4 } { 3 } ( 1 - 3 \eta ) S ^ { 3 } ( 1 + \mathcal { C } ^ { 2 } ) \cos 4 9 , } \\ & { \bar { H } _ { + } ^ { ( 3 2 ) } = \frac { 1 } { 1 2 0 } \sum _ { \alpha = 0 } ^ { 8 } \bigg [ ( 5 7 + 6 0 G ^ { \prime } - \mathcal { C } ^ { \mathrm { c } } ) - 2 ( 4 9 - 1 2 G ^ { \prime } - \mathcal { C } ^ { \mathrm { c } } ) \eta \bigg ] \cos 8 \Psi } \\ & { \qquad - \frac { 9 } { 1 2 0 } S \Big [ ( 7 3 + 4 0 G ^ { \prime } - 9 \mathcal { C } ^ { \mathrm { c } } ) - 2 ( 2 5 - 8 G ^ { 2 } - 8 G ^ { 2 } - 9 G ^ { 2 } ) \eta \Big ] \cos 3 \Psi } \\ & { \qquad + \frac { 6 2 5 } { 3 8 4 } ( 1 - 2 \eta ) S ^ { 3 } ( 1 + \mathcal { C } ^ { 2 } ) \cos 5 \Psi , } \\ & { \bar { H } _ { + } ^ { ( q ) } = - 4 ( 1 + \mathcal { C } ^ { 2 } ) \bigg \{ \frac { \pi } { 2 } \cos 2 9 + \big [ \gamma + \ln ( 4 \Omega R _ { \angle } / c ) \big ] \sin 2 \Psi \bigg \} . } \end{array}
$$

and

$$
\begin{array} { r l } & { H _ { x } ^ { ( 2 ) } = - 2 C \sin 2 \Psi , } \\ & { H _ { x } ^ { ( 1 ) / 2 } = - \frac 3 4 S C \sin \Psi + \frac 9 4 S C \sin 3 \Psi , } \\ & { H _ { x } ^ { ( 2 ) } = \frac 1 4 S \bigg [ ( 1 7 - 4 S ^ { 2 } ) - ( 1 3 - 1 2 S ^ { 2 } ) \bigg ] \sin 2 \Psi } \\ & { \qquad - \frac 8 S ( 1 - 3 \eta _ { x } ) S ^ { 2 } C \sin 4 \Psi , } \\ & { H _ { x } ^ { ( 2 ) / 2 } = \frac 1 9 S C \bigg [ ( 6 S - 5 S ^ { 2 } ) - 2 ( 2 3 - 5 C ^ { 2 } ) \eta _ { x } \bigg ] \sin \Psi } \\ & { \qquad - \frac 6 6 S \bigg [ C ( E ^ { 2 } - 1 S ^ { 2 } ) - 2 ( 1 9 - 1 5 C ^ { 2 } ) \eta _ { y } \bigg ] \sin 3 \Psi } \\ & { \qquad + \frac { 6 2 S } { 1 3 2 } ( 1 - 2 \eta _ { x } ) S ^ { 2 } C \sin 5 \Psi , } \\ & { H _ { x } ^ { ( 4 ) } = - 8 C \bigg \{ \frac { 2 } { 3 } \frac { S } { 3 } \sin 2 \Psi - [ \gamma + \ln ( 4 2 R B / c ) ] \cos 2 \Psi \bigg \} . } \end{array}
$$

where

$$
\Psi : = \phi + \omega = \Omega ( t - R / c ) + \omega .
$$

![](images/9140f6f8fac0f822766cebc189d63a2dd2871dad27c74123465265bc67f56c31.jpg)  
The polarizations $H _ { + }$ and $H _ { \times }$ as functions of retarded time $\tau$ , in units of the orbital period $P .$ The curves are displayed for a mass ratio M $_ { 1 } / M _ { 2 } = 1 0 ,$ a post-Newtonian parameter $\beta = 0 . 4 ,$ , an inclination angle $\iota = 8 5 ^ { \circ }$ , and a longitude of pericenter $\omega = 0 ^ { \circ }$ .

We recall that $m = M _ { 1 } + M _ { 2 }$ , $\eta = M _ { 1 } M _ { 2 } / m ^ { 2 }$ , $\Delta = ( M _ { 1 } - M _ { 2 } ) / m$ , $C : = { \cos { \iota } }$ , and $S : =$ sin ι. Equations (11.296) and (11.297) imply that at leading order in a post-Newtonian expansion, the gravitational wave oscillates at twice the orbital frequency; the post-Newtonian corrections contribute additional frequencies and the signal is therefore modulated. See Fig. 11.4 for an illustration.

The tail terms listed in Eqs. (11.296) and (11.297) are interesting. They involve the mathematical constants $\pi$ and $\gamma \simeq 0 . 5 7 7 2$ (Euler’s number), and they also involve a logarithmic term that depends on $\Omega R / c$ . The tail terms are best interpreted as giving rise to a correction to $\Psi$ , the quantity that determines the phase of the gravitational wave. Indeed, it is a simple matter to show that the Newtonian and tail contributions to $h _ { + }$ and $h _ { \times }$ can be combined and expressed as

$$
\begin{array} { r l } & { H _ { + } ^ { [ 0 ] } + \beta ^ { 3 } H _ { + } ^ { \mathrm { t a i l } } = - ( 1 + C ^ { 2 } ) \big ( 1 + 2 \pi \beta ^ { 3 } \big ) \cos 2 \Psi ^ { * } , } \\ & { H _ { \times } ^ { [ 0 ] } + \beta ^ { 3 } H _ { \times } ^ { \mathrm { t a i l } } = - 2 C \big ( 1 + 2 \pi \beta ^ { 3 } \big ) \sin 2 \Psi ^ { * } . } \end{array}
$$

These expressions involve an amplitude correction equal to $2 \pi \beta ^ { 3 }$ , and a new phase function given by

$$
\Psi ^ { * } = \Psi - 2 \beta ^ { 3 } \big [ \gamma + \ln ( 4 \Omega R / c ) \big ] = \Omega \bigg ( t - R / c - \frac { 2 G m } { c ^ { 3 } } \ln { \frac { 4 \Omega R } { c } } + \mathrm { c o n s t a n t } \bigg ) .
$$

It is this shifted phase function that informs us, at long last, that the radiation propagates not along the mathematical light cones of Minkowski spacetime, but along the true, physical light cones of a curved spacetime. Indeed, the logarithmic term in Eq. (11.300) represents the familiar Shapiro time delay, the extra time required by a light wave, or a gravitational wave, to climb up a gravitational potential well created by a distribution of matter with total mass $m$ . This effect was studied back in Sec. 10.2.5, and apart from irrelevant constant factors, the term $( { 2 G m } / { c ^ { 3 } } ) \ln R$ can be seen to originate from Eq. (10.100), in the special case in which the wave travels in the radial direction, so that $r _ { \mathrm { { o b s } } } + r _ { \mathrm { { o b s } } } \cdot k = 2 r _ { \mathrm { { o b s } } }$ .

# Evaluation of the tail integrals

We must still evaluate the tail integrals, and show that they lead to the results displayed in Eqs. (11.296) and (11.297). We start with Eqs. (11.287), which we specialize to circular orbits by involving Eqs. (11.289), (11.293), and (11.294). After conversion to the notation of Eq. (11.295), we find that

$$
\begin{array} { l } { { \displaystyle H _ { + } ^ { \mathrm { t a i l } } = 8 ( 1 + C ^ { 2 } ) \Omega \int _ { 0 } ^ { \infty } \cos ( 2 \Psi - 2 \Omega \zeta ) \biggl [ \ln \displaystyle \frac \zeta { \zeta + 2 R / c } + \frac { 1 1 } { 1 2 } \biggr ] d \zeta , } } \\ { { \displaystyle H _ { \times } ^ { \mathrm { t a i l } } = 1 6 C \Omega \int _ { 0 } ^ { \infty } \sin ( 2 \Psi - 2 \Omega \zeta ) \biggl [ \ln \displaystyle \frac \zeta { \zeta + 2 R / c } + \frac { 1 1 } { 1 2 } \biggr ] d \zeta . } } \end{array}
$$

To evaluate this we change the variable of integration to $y : = 2 \Omega \zeta$ and introduce $k : =$ $4 \Omega R / c$ to simplify the notation. The tail integrals become

$$
\begin{array} { l } { { \displaystyle H _ { + } ^ { \mathrm { t a i l } } = 4 ( 1 + C ^ { 2 } ) \int _ { 0 } ^ { \infty } \cos ( 2 \Psi - y ) \biggl [ \ln \frac { y } { y + k } + \frac { 1 1 } { 1 2 } \biggr ] d y , } } \\ { { \displaystyle H _ { \times } ^ { \mathrm { t a i l } } = 8 C \int _ { 0 } ^ { \infty } \sin ( 2 \Psi - y ) \biggl [ \ln \frac { y } { y + k } + \frac { 1 1 } { 1 2 } \biggr ] d y . } } \end{array}
$$

Expanding the trigonometric functions, this is

$$
\begin{array} { r l } & { H _ { + } ^ { \mathrm { t a i l } } = 4 ( 1 + C ^ { 2 } ) \big ( J _ { \mathrm { c } } \cos 2 \Psi + J _ { \mathrm { s } } \sin 2 \Psi \big ) , } \\ & { H _ { \times } ^ { \mathrm { t a i l } } = 8 C \big ( J _ { \mathrm { c } } \sin 2 \Psi - J _ { \mathrm { s } } \cos 2 \Psi \big ) , } \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle { J _ { \mathrm { c } } : = \int _ { 0 } ^ { \infty } \cos ( y ) \biggl [ \ln \frac { y } { y + k } + \frac { 1 1 } { 1 2 } \biggr ] d y , } } \\ { \displaystyle { J _ { \mathrm { s } } : = \int _ { 0 } ^ { \infty } \sin ( y ) \biggl [ \ln \frac { y } { y + k } + \frac { 1 1 } { 1 2 } \biggr ] d y . } } \end{array}
$$

These integrals are ill-defined, because the function within square brackets behaves as ${ \frac { 1 1 } { 1 2 } } - k / y$ for large $y$ , and the constant term prevents the convergence of each integral. This, however, is an artificial problem that comes as a consequence of our (unphysical) approximation $\Omega =$ constant. In reality, the two-body system undergoes radiation reaction, and $\Omega$ slowly decreases as $\zeta$ increases toward $\infty$ . (Recall that $r$ decreases as time increases, which causes $\Omega$ to increase as time increases; but recall also that the tail term integrates towards the past, so that $\Omega$ decreases as $\zeta$ increases.) This effect does not alter substantially the logarithmic portion of the integral, but it is sufficient to ensure the convergence of the constant term.

The integrals can be defined properly by inserting a convergence factor within the integrand. Alternatively, and this practice is consistent with what was done back in Sec. 11.3.7, we can integrate by parts and simply discard an ambiguous (and unphysical) boundary term at $y = \infty$ . Proceeding along those lines, we find that our integrals are equivalent to

$$
\begin{array} { l } { { J _ { \mathrm { { c } } } = - \displaystyle \int _ { 0 } ^ { \infty } \frac { k \sin y } { y ( y + k ) } d y , } } \\ { { J _ { \mathrm { { s } } } = \displaystyle \int _ { 0 } ^ { \infty } \frac { k ( \cos y - 1 ) } { y ( y + k ) } d y , } } \end{array}
$$

which are well defined. They can even be evaluated in closed form:

$$
\begin{array} { l } { { J _ { \mathrm { c } } = - { \displaystyle \frac { \pi } { 2 } } + { \displaystyle \frac { \pi } { 2 } } \cos k + \mathrm { C i } ( k ) \sin k - \mathrm { S i } ( k ) \cos k } } \\ { { \displaystyle ~ = - { \displaystyle \frac { \pi } { 2 } } + { \cal O } ( k ^ { - 1 } ) } , } \\ { { \displaystyle J _ { \mathrm { s } } = - \gamma - \ln k - \frac { \pi } { 2 } \sin k + \mathrm { C i } ( k ) \cos k + \mathrm { S i } ( k ) \sin k } } \\ { { \displaystyle ~ = - \gamma - \ln k + { \cal O } ( k ^ { - 2 } ) } , } \end{array}
$$

where $\gamma$ is Euler’s constant, $\operatorname { C i } ( k )$ is the cosine integral, and $\mathrm { S i } ( k )$ is the sine integral (defined, for example, in Sec. 5.2 of Abramowitz and Stegun’s Handbook of Mathematical Functions (1975)). The approximate forms neglect terms of order $k ^ { - 1 } = ( 4 \Omega R / c ) ^ { - 1 } \sim ( \lambda _ { c } / R )$ and smaller, and these are small by virtue of the fact that the gravitational-wave field is evaluated in the far-away wave zone, where $R \gg \lambda _ { c }$ .

Collecting results, we find that

$$
\begin{array} { r l } & { H _ { + } ^ { \mathrm { t a i l } } = - 4 ( 1 + C ^ { 2 } ) \bigg \{ \displaystyle \frac { \pi } { 2 } \cos 2 \Psi + \left[ \gamma + \ln ( 4 \Omega R / c ) \right] \sin 2 \Psi \bigg \} , } \\ & { H _ { \times } ^ { \mathrm { t a i l } } = - 8 C \bigg \{ \displaystyle \frac { \pi } { 2 } \sin 2 \Psi - \left[ \gamma + \ln ( 4 \Omega R / c ) \right] \cos 2 \Psi \bigg \} , } \end{array}
$$

and these expressions have already been presented in Eqs. (11.296) and (11.297).

# 11.4.7 Beyond 1.5pn order

The calculations of this section were long and arduous, but as it turns out, they were merely child’s play. At the time of writing, the gravitational waves for binary systems in circular motion have been calculated all the way out to $3 . 5 \mathrm { { P N } }$ order, and this is a much, much larger challenge. At 2pn order, for example, one finds not only the expected “standard” corrections of order $\beta ^ { 4 }$ , but also tail contributions generated by the $0 . 5 \mathrm { { P N } }$ order terms. At $2 . 5 \mathrm { { P N } }$ order one finds tails generated by the 1pn terms, 1pn corrections to the $1 . 5 \mathrm { { P N } }$ tail terms, as well as standard $2 . 5 \mathrm { { P N } }$ terms. At 3pn order there are, in addition to the standard terms, tails generated by the normal $1 . 5 \mathrm { { P N } }$ terms, $1 . 5 \mathrm { { P N } }$ corrections to the $1 . 5 \mathrm { { P N } }$ tail terms, and completely new “tails of tails” terms: tails generated by the $1 . 5 \mathrm { { P N } }$ tails. These formidable calculations have been carried out by a number of groups around the world, at an enormous cost of labor and sweat (perhaps even blood). There was a strong motivation behind this large effort: the measurement by laser interferometric detectors of gravitational waves emitted by compact binary systems involving neutron stars or black holes relies in an essential way on these very accurate theoretical predictions, which allow the extremely weak signals to be distinguished from noise. Data analysis relies on a bank of templates constructed from these waveforms, and cross-correlation of the detector output with the templates can reveal a signal that would otherwise be lost in the noisy data stream. In this way theorists, who build the templates, work hand in hand with experimentalists, who build the detectors, toward the successful measurement of gravitational waves.

# 11.5 Gravitational waves and laser interferometers

Thus far, in this long chapter on gravitational waves, we have said very little about the actual detection of these waves, and indeed we intend to leave it that way. The attempts to detect gravitational waves, from the pioneering experiments carried out by Joseph Weber in the 1960s and 1970s using suspended cylinders of aluminum, to the present international effort involving laser interferometry, pulsar timing, and cosmic microwave background observations, is a story rich in sociology, history, technological development, and bigscience politics. But it is not the main focus of this book. We refer readers who wish to learn more about the detection aspects to a number of excellent resources, listed at the end of this chapter.

Having come this far, however, and having produced the waveforms $h _ { + }$ and $h _ { \times }$ in a ready-to-use form for various sources and in various approximations, our coverage would seem incomplete if we did not make some attempt to connect them with the output of a gravitational-wave detector. It therefore seems appropriate to conclude this chapter by showing how $h _ { + }$ and $h _ { \times }$ can be measured in one of the leading approaches to gravitationalwave detection, laser interferometry.

In its most schematic realization, a laser interferometric gravitational-wave detector works just like the interferometer used by Michelson in the late 1800s to measure the speed of light and search for evidence of an “aether.” The real-life interferometers at the Earth-based LIGO, Virgo, Geo600, and KAGRA observatories, and the one envisioned for a space-based detector (known in 2013 as eLISA), are much more sophisticated than this, but this simple model is adequate and captures the essential physics.

A laser interferometer consists of a laser source, a beam splitter, and two end mirrors mounted on test masses imagined to be freely moving in spacetime (although in reality they can be suspended by thin wires). The arms of the interferometers are taken to be perpendicular to each other, although as we shall see, this is not an essential feature of the design. The laser beam is divided in two at the beam splitter, and each beam travels along one arm of the interferometer, reflects off the test mass, and returns to the beam splitter to be recombined with the other beam. The relative phase of the beams determines whether they produce a bright or dark spot when the recombined beam is measured by a photon detector. Since the initial phases at the beam splitter are identical, the phase difference $\Delta \Phi$ depends on the difference in travel time along the two arms. We can write

$$
\Delta \Phi = 2 \pi \nu ( 2 L _ { 1 } / c - 2 L _ { 2 } / c ) ,
$$

where $\nu$ is the frequency of the laser light, $L _ { 1 }$ and $L _ { 2 }$ are the armlengths, and $2 L _ { 1 } / c$ and $2 L _ { 2 } / c$ are the travel times along each arm (forward and back).

With the origin of the coordinate system placed at the beam splitter, the test mass at the end of the first arm is at a position $\pmb { \xi } _ { 1 } ( t )$ , and the test mass at the end of the second arm is at $\pmb { \xi } _ { 2 } ( t )$ . In the absence of a gravitational wave, the arms would have equal lengths, and we would have $\pmb { \xi } _ { 1 } = L _ { 0 } \pmb { e } _ { 1 }$ and $\pmb { \xi } _ { 2 } = L _ { 0 } \pmb { e } _ { 2 }$ , in which $L _ { 0 }$ is the unperturbed length of each arm, and $e _ { 1 } , e _ { 2 }$ are unit vectors pointing in the direction of each arm. In the presence of a gravitational wave, the position of each test mass varies with time. Assuming that the armlength $L _ { 0 }$ is much shorter than the wavelength $\lambda$ of the gravitational wave, the displacement is described by Eq. (11.29), and we have

$$
\begin{array} { r } { \xi _ { 1 } ^ { j } = L _ { 0 } \bigg ( e _ { 1 } ^ { j } + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 1 } ^ { k } \bigg ) , } \\ { \xi _ { 2 } ^ { j } = L _ { 0 } \bigg ( e _ { 2 } ^ { j } + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 2 } ^ { k } \bigg ) . } \end{array}
$$

The length of each arm is then given by

$$
\begin{array} { r } { L _ { 1 } = L _ { 0 } \bigg ( 1 + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 1 } ^ { j } e _ { 1 } ^ { k } \bigg ) , } \\ { L _ { 2 } = L _ { 0 } \bigg ( 1 + \frac { 1 } { 2 } h _ { \mathrm { T T } } ^ { j k } e _ { 2 } ^ { j } e _ { 2 } ^ { k } \bigg ) , } \end{array}
$$

to first order in $h _ { \mathrm { T T } } ^ { j k }$ , and the phase difference at beam recombination is

$$
\Delta \Phi = \frac { 4 \pi \nu L _ { 0 } } { c } \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) h _ { \mathrm { T T } } ^ { j k } .
$$

If we express the gravitational-wave field as in Eq. (11.6), $h ^ { j k } = ( G / c ^ { 4 } R ) A ^ { j k }$ , this is

$$
\Delta \Phi = \frac { 4 \pi \nu G L _ { 0 } } { c ^ { 5 } R } S ( t ) ,
$$

in which

$$
S ( t ) = \frac { 1 } { 2 } \big ( e _ { 1 } ^ { j } e _ { 1 } ^ { k } - e _ { 2 } ^ { j } e _ { 2 } ^ { k } \big ) A _ { \mathrm { T T } } ^ { j k } ( \tau , N )
$$

is the detector’s response function. We recall that $R$ is the distance to the source, that $N$ is a unit vector pointing from the source to the detector, and that $\tau : = t - R / c$ is retarded time.

To calculate $S ( t )$ we decompose $A _ { \mathrm { T T } } ^ { j k }$ in a transverse basis formed by the unit vectors $e _ { X }$ and $e _ { Y }$ , which are perpendicular to the direction of propagation $e _ { Z } = N$ . This decomposition was detailed back in Sec. 11.1.7, and we use the notation introduced in Sec. 11.2.2. We have that

$$
A _ { \mathrm { T T } } ^ { j k } = \left( e _ { X } ^ { j } e _ { X } ^ { k } - e _ { Y } ^ { j } e _ { Y } ^ { k } \right) A _ { + } + \left( e _ { X } ^ { j } e _ { Y } ^ { k } + e _ { Y } ^ { j } e _ { X } ^ { k } \right) A _ { \times } ,
$$