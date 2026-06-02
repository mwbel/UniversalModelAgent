This section is intended for readers with some knowledge of quantum feld theory.In this section and in the next we use units

$$
\hbar = c = 1 .
$$

It can be useful to recall how dimensional analysis works in these units. Since $c = 1$ ， velocities are pure numbers while,dimensionally,

$$
{ \mathrm { e n e r g y } } = { \mathrm { m o m e n t u m } } = { \mathrm { m a s s } } .
$$

Recalling,from the uncertainty principle,that a length times a momentum has dimensions of $\hbar$ ,inunits $\hbar = c = 1$ we also have

$$
\mathsf { l e n g t h } = ( \mathsf { m o m e n t u m } ) ^ { - 1 } = ( \mathsf { m a s s } ) ^ { - 1 } .
$$

Then the dimensions of any quantity can be expressed as positive or negative powers of mass.For example, and energy density is energy/volume $= ( \mathrm { m a s s } ) ^ { 4 }$

# 2.2Gravitons

All astrophysical processes which generate GWs,as well as the interac tion of GWs with detectors,are adequately described in the framework of a classical field theory of gravitation. Nevertheless,it can be instructive to discuss some conceptual issues using the vantage point provided by modern quantum field theory.

In this section we will see that, at the quantum level, gravity must be mediated by a massless particle with helicity $\pm 2$ ,the graviton. Its free action，in fat space-time, is fixed by field-theoretical considerations, and reproduces the linearization of the Einstein action. Consistency with gauge-invariance then requires the introduction of non-linear couplings between the graviton,with three-graviton verticcs, four-graviton vertices,etc., and a full non-linear structure emerges. Finally, we wil briefy mention some of the issues involved in the quantization of gravity and we will discuss why, even lin the absence of a full quantum theory of gravitation, general relativity makes sense as an effective field theory below the Planck scale,and the notion of graviton is well defined.

# 2.2.1 Why a spin-2 feld?

In quantum field theory all interactions are mediated by the exchange of bosons,i.e. particles with integer spin. Since a fat space-time background is an excellent approximation in many situations,it make sense to look for a relativistic quantum field theory living in fat space-time, that in the non-relativistic limit reduces to Newtonian gravity. Such a theory should be mediated by a boson which propagates in this fat space-time.

Gravity is the interaction that in the non-relativistic limit couples to the mass. To obtain such a coupling from a local quantum field theory, we need to couple the field that mediates gravity to a local quantity (i.e a quantity which is function of the space-time point $x$ ）whose spatial integral, in the non-relativistic ilimit, becomes the mass.

Mathematics alone is not sufficient to obtain uniquely a consistent theory that gives back Newton's law. We will also use as guiding principle the deep insight of Einstein that in the full theory of gravitation not only the mass is a source for gravitation but, more generally, all forms of energy. In a local field theory, we therefore look for a coupling between the field that mediates gravity and the energy density.

Since, from the point of view|of Lorentz transformations,energy density is the (O0) component of the energy-momentum tensor, consistency with special relativity requires that we couple our gravitational field to the energy-momentum tensor $\dot { T } _ { \mu \nu } ( x )$ . As long as we work at linearized level,we can neglect the contribution of the gravitational field itself to $T ^ { \mu \nu }$ , so we can take as $T ^ { \mu \nu }$ the energy-momentum tensor of the matter fields only. Since we are assuming a flat background, at linearized level $T ^ { \mu \nu }$ obeys the flat-space conservation law

$$
\partial _ { \mu } T ^ { \mu \nu } = 0 .
$$

We will come back laterto the inclusior ofthenon-linear terms.

The simplest possibility that one can examine is that gravity is mediated by a spin-O boson,described bya scalar field $\phi$ A scalar feld $\phi$ carries no Lorentz index,so the only possibility is that it couples to the trace of the energy-momentum tensor, $T = T _ { \mu } ^ { \mu }$ Therefore the Lagrangian density which describes the dynamics of this hypothetical scalar gravitational field and its coupling to matter,in linearized theory, must be of the form

$$
\mathcal { L } = - \frac { 1 } { 2 } ( \partial _ { \mu } \phi \partial ^ { \mu } \phi + \mu ^ { 2 } \phi ^ { 2 } ) + g \phi T ,
$$

where $g$ is a coupling constant,and $\mu$ is the mass of the scalar field (more generally, we could also add a potential $V ( \phi )$ ,that however does not influence the following discussion).In order to see if this theory reduces correctly to Newtonian gravity in the non-relativistic limit， we can compute the potential induced by the exchange of a $\phi$ boson between two static particles of masses $m _ { 1 }$ and $m _ { 2 } ^ { \mathrm { ~ i ~ } }$ . Let us recall that in quantum feld theory the static interaction potential V(x) is a derived concept, which makes sense only in the non-relativistic limit. To obtain it,one must compute the 2 →2 scattering amplitude Mfi at tree level, taking the initial state equal to the final state,and then the potential is given $b y ^ { 1 0 }$

$$
V ( { \bf x } ) = - \int { \frac { d ^ { 3 } q } { ( 2 \pi ) ^ { 3 } } } { \cal M } _ { f i } ( { \bf q } ) e ^ { i { \bf q } \cdot { \bf x } } .
$$

The energy-momentum tensor $T ^ { \mu \nu }$ is quadratic in the matter felds, so the vertex $g \phi T$ involves two matter-field lines and one $\phi$ boson,and to compute $M _ { f i }$ we must evaluate a Feynman diagram of the type given Fig.2.1 (plus a possible exchange graph for identical particles), with $\{ \boldsymbol { q } = \left( q ^ { 0 } , \mathbf { q } \right)$ ,setting $q ^ { 0 } = 0$ because the potential is obtained in the static limit. In general,the details of the computation depend on the form of ${ \tilde { I } } ( x )$ ,i.e.on the specific type of matter feld considered.However,if the matter field is massive,we can take the non-relativistic limit,and in is limit we can treat T(x) as an external classical field. In this case, the interaction vertex of this theory becomes as shown in Fig.2.2,where the cross denotes the insertion of T(q). Then the diagram of Fig. 2.1 reduces to that shown in Fig.2.3,and the amplitude Mfi is given simply by

where

$$
\begin{array} { c } { { i { \cal M } _ { f i } ( { \bf q } ) = ( - i g ) ^ { 2 } \tilde { T } _ { 1 } ( { \bf q } ) \tilde { D } ( { \bf q } ) \tilde { T } _ { 2 } ( - { \bf q } ) , } } \\ { { { } } } \\ { { D ( q ) = \displaystyle \frac { - i } { q ^ { 2 } + \mu ^ { 2 } } , } } \end{array}
$$

the propagator of the scalar field $\phi$ (recall that we are using the sigmature $\eta _ { \mu \nu } = \left( - , + , + , + \right) )$ ，and $T _ { 1 } , T _ { 2 }$ are the traces of the energyomentum tensor for particles of masses $m _ { 1 }$ and $m _ { 2 }$ ,respectively. In lie static limit, $q ^ { 2 } = - ( q ^ { 0 } ) ^ { 2 } + { \bf q } ^ { 2 } \to { \bf q } ^ { 2 }$ ,and the propagator becomes

$$
D ( { \bf q } ) = \frac { - i } { { \bf q } ^ { 2 } + \mu ^ { 2 } } .
$$

![](images/9b7ca120a1c0488af874bcc9931911d3e8b72432a4056c1b6bcc02f83de0e369.jpg)  
Spin-0   
Fig.2.1 The Feynman diagram that gives the scattering amplitude at tree level.

10See e.g.Maggiore (2005) (Section 6.6 and eqs.(7.56)-(7.59)),for the derivation of this result and for explicit computations of the potential induced by the exchange of scalar or vector particles.

![](images/9d36bd84ddc5f723a862261a62ed0c3d40543f01c4029b7fe7e87f4677792664.jpg)  
Fig.2.2 The Feynman diagram that gives the vertex，when $T ( x )$ is treated as an external field.

![](images/82befc049a9dd20b79a99b8b44ba79fde3bfaeead48f1b882c3feac3fb294ee6.jpg)  
Fig. 2.3 The Feynman diagram that gives the scattering amplitude, when $T ( x )$ is treated as an external field.

11 More precisely, for a particle_ in X1, $T ( { \bf x } ) ~ = ~ - m \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { 1 } )$ ，so $\begin{array} { r } { \tilde { \cal T } ( { \bf q } ) = } \end{array}$ $- m \exp \{ - i \mathbf { q } \cdot \mathbf { x } _ { 1 } \}$ .In the field theoretical language, the factors $\exp \{ - i { \bf q } \cdot { \bf x } _ { 1 } \}$ from $\tilde { T } _ { 1 } ( \mathbf { q } )$ and $\exp \left\{ + i \mathbf { q } \cdot \mathbf { x } _ { 2 } \right\}$ from $\tilde { \cal T } _ { 2 } ( - { \bf q } )$ comes from the wavefunctions of the external legs,and in eq.(2.68) they have already been taken into account by the term $\exp \{ i \mathbf { q } \cdot ( \mathbf { x } _ { 2 } - \mathbf { x } _ { 1 } ) \}$ where ${ \bf x } _ { 2 } - { \bf x } _ { 2 } \equiv { \bf x }$

Equation (2.64) then gives

$$
V ( { \bf x } ) = - i g ^ { 2 } \int \frac { d ^ { 3 } q } { ( 2 \pi ) ^ { 3 } } \tilde { T } _ { 1 } ( { \bf q } ) \tilde { D } ( { \bf q } ) \tilde { T } _ { 2 } ( - { \bf q } ) e ^ { i { \bf q } \cdot { \bf x } } .
$$

For a relativistic classical particle moving on the trajectory ${ \bf x } _ { 0 } ( t )$ the energy-momentum tensor is given by (see,e.g. Landau and Lifshitz. Vol. II 1979)

$$
\begin{array} { r } { T ^ { \mu \nu } ( { \bf x } , t ) = \displaystyle \frac { \mathcal { P } ^ { \mu } p ^ { \nu } } { p ^ { 0 } } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { 0 } ( t ) ) , } \end{array}
$$

where $p ^ { \mu }$ is the four-momentum. Using $p ^ { \mu } p _ { \mu } = - m ^ { 2 }$ and, for a particle at rest,po = m, the trace of the energy-momentum tensor of a heavy source becomes $T ( { \bf x } ) = - m \delta ^ { ( 3 ) } ( { \bf x } )$ ， which in turn gives $\tilde { T } ( \mathbf { q } ) = - m$ ii Therefore

$$
V ( { \bf x } ) = - i g ^ { 2 } m _ { 1 } m _ { 2 } D ( { \bf x } ) .
$$

If the mass $\mu$ vanishes,

$$
\begin{array} { l } { { \displaystyle { \cal D } ( { \bf x } ) = \int \frac { d ^ { 3 } q } { ( 2 \pi ) ^ { 3 } } \frac { - i } { { \bf q } ^ { 2 } } e ^ { i { \bf q } \cdot { \bf x } } } } \\ { { \displaystyle ~ = \frac { - i } { 4 \pi r } , } } \end{array}
$$

where $r = | { \bf x } |$ , and therefore we get the correct Newtonian potential

$$
V ( r ) = - { \frac { G m _ { 1 } m _ { 2 } } { r } } ,
$$

12Obviously,this rules out the possibility that the main contribution to gravity comes from spin-O felds.It says nothing about the possibility that there are additional gravitationally interacting scalar fields,which give small corrections to general relativity either because they are massive or because their gravitational coupling is suppressed with respect to Newton constant $G$ Indeed,additional scalar fields enter in most extensions of general relativity.

once we make the identification $g ^ { 2 } / ( 4 \pi ) = G$ . If instead the mass $\mu$ is non-vanishing，we get a Yukawa potential

$$
V ( { \bf x } ) = - \frac { G m _ { 1 } m _ { 2 } } { r } e ^ { - \mu r } .
$$

This result shows that,as far as|the non-relativistic Newtonian limit is concerned, a spin-O massless scalar field is a viable possibility.

However, a spin-O field fails when we come to the new predictions of this theory of gravitation in the relativistic regime. In particular,we see from eq. (2.23) that the energy-momentum tensor of the electromagnetic field is traceless,

$$
T _ { \mathrm { e m } } = F ^ { \mu \rho } \dot { F } _ { \mu \rho } - { \frac { 1 } { 4 } } \delta _ { \mu } ^ { \mu } F ^ { 2 } = 0 .
$$

Therefore,in this theory， photons do not couple to gravity. Experimentally, the gravitational bending of light rays from massive objects is very well established (it was in fact the first experimental confirmation of general relativity and nowadays,in the form of gravitational lensing. it is a beautiful routine tool in astrophysics). Therefore a spin-O theory of gravitation is ruled out.12

The next possibility is a spir-1 field, just like in electrodynamics. In order to get a long-range potential, we need again a massless field.

but a massless vector field $A _ { \mu }$ can be coupled consistently only if we respect gauge invariance.In electrodynamics this can be obtained with a coupling $A _ { \mu } j ^ { \mu }$ ,imposing that $j ^ { \mu }$ is a conserved current.In fact,under a gauge transformation, $A _ { \mu } \to A _ { \mu } - \partial _ { \mu } \theta$ and,after an integration by parts, the term $- ( \partial _ { \mu } \theta ) j ^ { \mu }  \theta \partial _ { \mu } j ^ { \mu } = 0$ ,so the action is invariant.

Therefore,a coupling between such a Vector feld $A _ { \mu }$ and the energymomentum tensor of the form $A _ { \mu } A _ { \nu } T ^ { \mu \nu }$ is immediately ruled out,because it is not gauge invariant (and furthermore,the simultaneous exchange of two gauge bosons gives a potential $1 / r ^ { 3 }$ rather than $1 / r$ ）A derivative coupling $( \partial _ { \mu } A _ { \nu } ) T ^ { \mu \nu }$ is also not viable,since after integration by parts it gives zero,because of energy-momentum conservation.

If we limit ourselves to the level of first quantization,we could write down a coupling of a vector feld to a point-like particles in the form

$$
\int d ^ { 4 } x A _ { \mu } ( x ) m \frac { d x _ { 0 } ^ { \mu } } { d \tau } \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { 0 } ( t ) ) ,
$$

where $x _ { 0 } ^ { \mu } ( \tau )$ is the particle world-line.However,in quantum field theory the four-vector $j ^ { \mu } ( x )$ that,in the limit of point-like particle,reduces to $m ( d x _ { 0 } ^ { \mu } / d \tau ) \delta ^ { ( 3 ) } ( { \bf x } - { \bf x } _ { 0 } ( t ) )$ ，isa $U ( 1 ) _ { i }$ current. Then $Q \equiv \int d ^ { 3 } x j ^ { 0 }$ is equal to the mass $m$ times (number of particles minus number of antiparticles),so it is not positive definite,and $\textstyle \int d ^ { 3 } x j ^ { 0 }$ cannot be interpreted as the mass (unless we assigna negative gravitational mass to antiparticles).Furthermore,even if we ignore this problem and interpret $j ^ { 0 }$ has a mass density,still this attempt to construct a spin-1 theory of gravity fails because,as we know from classical electromagnetism,the interaction mediated by the photon between two particles of the same charge is repulsive. Technically, this comes out because the term $\tilde { \cal T } _ { 1 } ( { \bf q } ) \tilde { D } ( { \bf q } ) \breve { \tilde { \cal T } _ { 2 } } ( - { \bf q } )$ in eq. (2.68) is now replaced by

$$
\tilde { j } ^ { \mu } ( { \bf q } ) \tilde { D } _ { \mu \nu } ( { \bf q } ) \tilde { j } ^ { \nu } ( - { \bf q } ) ,
$$

where $\tilde { D } _ { \mu \nu } ( q )$ is the propagator of thelmassless vector field $A _ { \mu }$ In momentum space,

$$
\tilde { D } _ { \mu \nu } ( q ) = \frac { - i } { q ^ { 2 } } \eta _ { \mu \nu } .
$$

In the static limit $q ^ { 2 } = - ( q ^ { 0 } ) ^ { 2 } + { \bf q } ^ { 2 } \to { \bf q } ^ { 2 }$ , and the propagator becomes

$$
\tilde { D } _ { \mu \nu } ( { \bf q } ) = \frac { - i } { { \bf q } ^ { 2 } } \eta _ { \mu \nu } .
$$

Because of the factor $\eta _ { \mu \nu }$ ,the propagator of the spatial components $A _ { i }$ is qual to that of a scalar field,but the propagator of $A _ { 0 }$ has the opposite ign.In the non-relativistic limit $j ^ { \mu }  ( j ^ { 0 } , \bar { 0 } )$ .Then in eq. (2.76) only the component $D _ { 0 0 }$ contributes,so we get the opposite sign compared o the scalar case,i.e.a repulsive potentlal between positive masses. In tonclusion,also spin-1 is ruled out.

Values of the spin $j \geqslant 3$ are also ruledout: the need for a long-range Drce requires again a massless field,which can be coupled consistently only to a conserved tensor. Except possibly for total derivative terms. there is no conserved tensor with three or more indices, so massless particles with $j \geqslant 3$ cannot produce long-range forces, neither gravitational nor of any other type.

The only possibility which is left is $j = 2$ , and we examine it in the next section.

# 2.2.2The Pauli-Fierz action

The considerations of the previous section lead us to study the action for a spin-2 massless field. To identify the field that describes a massless particle with helicity $\pm 2$ ，let us first recall some elementary facts about the representations of the Lorentz and Poincaré groups,and their decomposition under representations of the rotation group.

# Massless particles in field theory

The irreducible tensor representations of the Lorentz group are given by tensors that,with respect to anyjpair of indices,are either symmetric and traceless,or antisymmetric.An irreducible representation of the Lorentz group provides of course also a representation of the rotation subgroup $S O ( 3 )$ . However,a representation that is irreducible with respect to the full Lorentz group, will be reducible if we limit ourselves to the rotation subgroup (except for the trivial case of the scalar representation),so it decomposes into the direct sum of irreducible representations of the rotation group. For instance a four-vector $A _ { \mu }$ is an irreducible representation of the Lorentz group,but from the point of view of rotations it decomposes into a scalar $A _ { 0 }$ and a vector $\mathbf { A }$ ，or

$$
A _ { \mu } \in \mathbf { 0 } \oplus \mathbf { 1 } ,
$$

where we denote by $\oplus$ the direct sum of representations,and by s the representation of the rotation group corresponding to spin $s$ $\bf { \zeta } _ { S O } \textbf { 0 }$ is the scalar and 1 is the vector representation). The representation s has dimension $2 s + 1$ , so in particular the scalar is one-dimensional and the vector is a three-dimensional representation. When we consider tensors with two indices,an antisymmetric tensor $A ^ { \mu \nu }$ decomposes as

$$
A _ { \mu \nu } \in { \bf 1 } \oplus { \bf 1 } ,
$$

while a traceless symmetric tensor $S ^ { \mu \nu }$ decomposes as

$$
S _ { \mu \nu } \in { \mathbf { 0 } } \oplus { \mathbf { 1 } } \oplus { \mathbf { 2 } } .
$$

Therefore,the simplest tensor that contains a spin-2 is the traceless symmetric tensor, and a spin-2 can be described using $S _ { \mu \nu }$ and imposing conditions that eliminate the extra degrees of freedom. Equation (.81) states that the nine independent components of a traceless symmetric tensor with two indices decompose into a scalar,the three components of a spin-1, and the five ( $[ 2 s + 1$ with $s = 2$ ） components of a spin-2.

Afurther complication arises if we want to describe a massess particle. As we recallin more detail in Problem 2.1,particles are representations of the Poincaré group,and the physically interesting representations of the Poincaré group are of two type. (1)Massive representations,with -PμPμ = m² > 0, labeled by the mass m and by the spin j,which takes integer and half-integer values,j=0,1/2,1,.... The dimension of these representations is 2j+1. (2) Massless representations,PμPμ =0, which are two-dimensional (actually,one-dimensional, but become twodimensional if we also require that they are representations of parity) and are characterized by two helicity states $h = \pm j$ ，

In particular,a massive spin-1 particle has three degrees of freedom, and a massive spin-2 particle has five degrees of freedom. In contrast, a massless particle with j=1 and a massless particle with j= 2 both have only two degrees of freedom,the former with helicities h = ±1, and the latter with h=±2. This means that,in the case of a massless spin-1 field,a four-vector field Aμ contains two redundant degrees of freedom,while for a massless spin-2 feld the nine components of Suv contain seven redundant degrees of freedom. The way to eliminate these spurious degrees of freedom is to introduce a gauge-invariance.For electromagnetism,one imposes that the theory is invariant under

$$
A _ { \mu }  A _ { \mu } - \partial _ { \mu } \theta .
$$

t is a standard textbook exercise to show that we can choose 0(x) so to set Ao = O. A residual gauge-invariance remains,due to the possibility of performing a further transformation with a function 0(x) independent of time and (making use of the Maxwell equation in vacuum VE= O) it can be used to set V·A = 0,so we eliminate also the longitudinal component of a plane wave solution,and we are left with only two degrees of freedom,at least at the classical level. Then,one can quantize the free theory and verify that one obtains a massless particle with two helicity states,the photon.

# The graviton and its action

We want to do the same for a massess particle with $j = 2$ ，that we call the graviton. The strategy is therefore to start from a traceless symmetric tensor,to impose a local invariance,and to write down a Lagrangian that respects this local symmetry. Then (using the equations of motion derived from this Lagrangiah） we can see how many degrees of freedom remain in the theory. In fact,it is even technically simpler to start from a tensor hμv which is symmetric,but not traceless,so from the point of view of Lorentz symmetry it decomposes into the trace and the symmetric traceless part,and from the point of view of rotations ∈0(012).We therefore want to impose an invariance that eliminates eight spurious degrees of freedom.

In order to generalize eq.(2.82) to the case of a feld hμv with two Indices,we must assign a Lorentz index to the function that paramerizes the gauge transformation.Let us call £μ(x） this function.Since we must respect the fact that $\vert h _ { \mu \nu }$ is symmetric in $( \mu , \nu )$ ， the natural generalization of eq. (2.82) is

$$
h _ { \mu \nu } ( x )  h _ { \mu \nu } ( x ) - ( \partial _ { \mu } \xi _ { \nu } + \partial _ { \nu } \xi _ { \mu } ) ,
$$

that we still call a gauge transformation. Observe that this is nothing but the symmetry (1.8) of linearized Einstein gravity, so we are on the good track for recovering the linearization of general relativity.

Next, we want to construct a gauge-invariant action, for the free the ory.Remarkably, the condition of gauge-invariance fixes this action uniquely. In fact,by inspection we see that the possible terms that one can write down, quadratic in $h _ { \mu \nu }$ and with two derivatives, are

$$
\partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } , \quad \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } , \enspace , \enspace \partial _ { \nu } h ^ { \mu \nu } \partial ^ { \rho } h _ { \mu \rho } , \enspace \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h , \quad \partial ^ { \mu } h \partial _ { \mu } h ,
$$

where $h = h _ { \mu } ^ { \mu }$ is the trace of $h _ { ; \mu \nu }$ . Terms of the schematic form haoh are related to those written above by a single integration by parts. Furthermore, the second and third term in eq. (2.84) are related by two integrations by parts, that swaps the two derivatives. Therefore, the most general form of the free agtion is

$$
S _ { 2 } = \int d ^ { 4 } x \left[ a _ { 1 } \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + a _ { 2 } \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } + a _ { 3 } \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h + a _ { 4 } \partial ^ { \mu } h \partial _ { \mu } h \right] ,
$$

where the label in $S _ { 2 }$ stresses that this quantity is quadratic in $h _ { \mu \nu }$ We now impose invariance under the gauge transformation (2.83). This fixes all the coefficients $a _ { 1 } , \dots , a _ { 4 }$ ,except of course for an overall normalization.We then obtain (choosing the normalization α1 = --1/2; the sign is fixed requiring that the energy is positive definite),

$$
S _ { 2 } = \frac { 1 } { 2 } \int d ^ { 4 } x \left[ - \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + \left. 2 \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } - 2 \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h + \partial ^ { \mu } h \partial _ { \mu } h \right. \right] .
$$

This is the Pauli-Fierz action. Comparison with eq. (2.33) shows that we have indeed recovered the Einstein action of linearized theory,after a rescaling

$$
h _ { \mu \nu }  ( 3 2 \pi G ) ^ { - 1 / 2 } h _ { \mu \nu } ,
$$

and taking into account that the last term in eq. (2.33) is equal to the second in eq. (2.86) after swapping the two derivatives with integrations by parts.We have therefore found that the linearized Einstein action is the unique action that describes a free massless particle with helicities $\pm 2$ ,propagating in flat space.

We can now repeat the considerations already made in Sections 1.1 and 1.2,see in particular the discussion around eqs. (1.26) and (1.27): we can use the gauge-invariance (2.83) to choose the Lorentz gauge (1.18). This eliminates four of the 1O degrees of freedom in hμv,and still leaves a residual gauge invariance,i.e.the transformations (2.83) with functions $\xi _ { \mu }$ that satisfy $\square \xi _ { \mu } = 0$ In the vacuum, where $T ^ { \mu \nu } = 0$ using the Lorentz gauge,the equations of motion derived from the linearized

Einstein action are $\square \bar { h } _ { \mu \nu } = 0$ ,and therefore four functions $\xi _ { \mu }$ that satisfy $\square \xi _ { \mu } = 0$ can be used to eliminate four components of $\bar { h } _ { \mu \nu }$ ，sowe remain with two degrees of freedom,and we arrive at the TT gauge, eq. (1.31). The requirements of gauge invariance therefore fixes uniquely the linearized action,and leaves us with|a massless spin-2 field with two transverse degrees of freedom,the graviton.

For the interaction term,we can write

$$
S _ { \mathrm { i n t } } = { \frac { \kappa } { 2 } } \int d ^ { 4 } x h _ { \mu \nu } T ^ { \mu \nu } .
$$

The coupling constant $\kappa$ will be fixed below.Observe that this interaction term is invariant under the gauge transformation (2.83) because, after an integration by parts,the term $( \partial _ { \mu } \xi _ { \nu } + \partial _ { \nu } \xi _ { \mu } ) T ^ { \mu \nu }$ vanishes,using $\partial _ { \mu } T ^ { \mu \nu } = 0$

Just as in electrodynamics,to find the graviton propagator we must add a gauge-fixing term to eq.(2.86),since otherwise the quadratic form is not invertible. The Lorentz gauge car be obtained adding the gaugefixing term

$$
\begin{array} { l } { { S _ { \mathrm { g f } } = - \displaystyle \int d ^ { 4 } x \left( \partial ^ { \nu } \bar { h } _ { \mu \nu } \right) ^ { 2 } } } \\ { { \mathrm { } = - \displaystyle \int d ^ { 4 } x \left( \partial ^ { \nu } h _ { \mu \nu } - \frac { 1 } { 2 } \eta _ { \mu \nu } \partial ^ { \nu } h \right) ^ { 2 } } } \\ { { \mathrm { } = \displaystyle \int d ^ { 4 } x \left( - \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } + \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h - \frac { 1 } { 4 } \partial ^ { \mu } h \partial _ { \mu } h \right) \ : , } } \end{array}
$$

where in thc first term we swapped the derivatives integrating by parts. The overall numerical coefficient in eq.(2.89) has been chosen so that the terms $\partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho }$ and $\partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h$ cancel between $S _ { 2 }$ and $S _ { \mathrm { g f } }$ ,so this choice corresponds to the Feynman gauge in electrodynamics. Putting everything together,we find

$$
\begin{array} { l } { { S = S _ { 2 } + S _ { \mathrm { g f } } + S _ { \mathrm { i n t } } } } \\ { { = \displaystyle \int d ^ { 4 } x \left[ - \frac { 1 } { 2 } \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + \frac { 1 } { 4 } \partial ^ { \mu } h \partial _ { \mu } h + \frac { \kappa } { 2 } h _ { \mu \nu } T ^ { \mu \nu } \right] . } } \end{array}
$$

The equations of motion obtained performing the variation of this action are

$$
\boxed { \bar { h } _ { \mu \nu } } = - \frac { \kappa } { 2 } \bar { { f } } _ { \mu \nu } ,
$$

or,equivalently

$$
\Pi h _ { \mu \nu } = - { \frac { \kappa } { 2 } } \left( T _ { \mu \nu } + { \frac { 1 } { 2 } } \eta _ { \mu \nu } T \right) .
$$

Comparing with eq.(1.24) and taking into account the rescaling (2.87), we get (in the units $c = 1$ that we are using in this section),

$$
\kappa = ( 3 2 \pi G ) ^ { 1 / 2 } .
$$

The graviton propagator

We now find the graviton propagator. Integrating by parts, we have

$$
\int d ^ { 4 } x \left[ - \frac { 1 } { 2 } \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + \frac { 1 } { 4 } \partial ^ { \mu } h \partial _ { \mu } h \right] = \frac { 1 } { 2 } \int d ^ { 4 } x h ^ { \mu \nu } A _ { \mu \nu \rho \sigma } \partial ^ { 2 } h ^ { \rho \sigma } ,
$$

where

$$
A _ { \mu \nu \rho \sigma } = \frac { 1 } { 2 } \left( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } - \eta _ { \mu \nu } \eta _ { \rho \sigma } \right) .
$$

The graviton propagator in this gauge is obtained inverting this matrix. Observe that

$$
A _ { \mu \nu \alpha \beta } A ^ { \alpha \beta } { } _ { \rho \sigma } = \frac { 1 } { 2 } ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } ) .
$$

13Alternatively，we can define the 10 fields $\phi _ { i } , \quad i \quad = \quad 1 , \ldots , 1 0 ,$ by $\begin{array} { r l } { \phi _ { 1 } } & { { } = } \end{array}$ $h _ { 0 0 } , \phi _ { 2 } ~ = ~ h _ { 0 1 } , . . . , \phi _ { 1 0 } ~ = ~ h _ { 3 3 }$ We then write the kinetic term in the form $A _ { i j } \partial _ { \mu } \phi _ { i } \partial ^ { \mu } \phi _ { j }$ ,and we invert the $1 0 \times 1 0$ matrix Aij.

The right-hand side is nothingbut the identity matrix, in the space of tensors symmetric in $( \mu , \nu )$ and in $( \rho , \sigma )$ .Therefore in this space the inverse of $A$ is $A$ itself,13 so the propagatoris given by

$$
\tilde { D } _ { \mu \nu \rho \sigma } ( k ) = { \frac { 1 } { 2 } } ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } - \eta _ { \mu \nu } \eta _ { \rho \sigma } ) \left( \frac { - i } { k ^ { 2 } - i \epsilon } \right) ,
$$

14The overall factor depends of course on the overall normalization of the action，i.e.on the normalization of $h _ { \mu \nu }$ With our choice the field $h _ { 0 0 }$ is not canonically normalized,since its propagator has an extra factor $1 / 2$ with respect to the usual normalization.In contrast,writingΦμv = hμv-$( 1 / 4 ) \eta _ { \mu \nu } h$ ，thefield $\phi _ { \mu \nu }$ is canonically normalized. Observe that $\phi _ { \mu \nu }$ is a pure spin-2 field since it is traceless,while $^ h$ is a spin-O field.

where, as usual, the $i \epsilon$ prescription selects the Feynman propagator. In particular, $\tilde { D } _ { 0 0 0 0 } ( k ) = \hat { - } i / ( 2 k ^ { 2 } )$ and $D _ { 0 0 0 0 } ( r ) = - i / ( 8 \pi r )$ .14 Comparing with eqs.(2.66) and (2.78) we see that the propagator of $h _ { 0 0 }$ has the same sign as the propagator of the scalar field (and the opposite sign of the propagator of $A _ { 0 }$ ），since $( \eta _ { 0 0 } ) ^ { 2 } = + 1$ . Therefore, in the static limit $h _ { 0 0 }$ mediates an attractive gravitational potential. Using the interaction terms (2.88) and repeating the same steps performed for the scalar field, we get

$$
\begin{array} { l } { { \displaystyle V ( { \bf x } ) = - i \frac { \kappa ^ { 2 } } { 4 } \int \frac { d ^ { 3 } q } { ( 2 \pi ) ^ { 3 } } \tilde { \cal T } _ { 1 } ^ { 0 0 } ( { \bf q } ) \tilde { \cal D } _ { 0 0 0 0 } ( { \bf q } ) \tilde { \cal T } _ { 2 } ^ { 0 0 } ( - { \bf q } ) e ^ { i { \bf q } \cdot { \bf x } } } } \\ { ~ = - i \frac { \kappa ^ { 2 } } { 4 } m _ { 1 } m _ { 2 } { \cal D } _ { 0 0 0 0 } ( { \bf x } ) }  \\ { { \displaystyle ~ = - \frac { \kappa ^ { 2 } } { 3 2 \pi } \frac { m _ { 1 } m _ { 2 } } { r } } . } \end{array}
$$

This gives again K = (32πG)1/2in agreement with eq. (2.93) (of course, this numerical value depends on the choice of normalization made for $h _ { \mu , \nu }$ ),and we have recovered the Newtonian limit.

# 2.2.3 From gravitons to gravity

We can now understand,from a field-theoretical point of view, that the simple action (2.90) cannot be the whole story，and that the correct field theory of gravitation must |develop a full non-linear structure. The reason is that,as we have seen, the theory of a massless particle with helicities $\pm 2$ must necessarily be gauge invariant.We have shown that we can use gauge-invariance to impose the Lorentz condition

$$
\partial ^ { \mu } \bar { h } _ { \mu \nu } = 0 ,
$$

and that in this gauge the equations of motion read

$$
\bar { \sqcup } \bar { h } _ { \mu \nu } = - \frac { \kappa } { 2 } { \cal T } _ { \mu \nu } .
$$

Equations (2.99)and (2.100) together imply that the energy-momentum tensor of matter satisfies the fat-space conservation law $\partial _ { \mu } T ^ { \mu \nu } = 0$ In integrated form,this conservation laws reads

$$
\frac { d } { d t } \int _ { V } d ^ { 3 } x T ^ { 0 0 } = - \int _ { V } d ^ { 3 } x \partial _ { i } T ^ { 0 i } ,
$$

and states that any change in the energy of the matter feld in a volume $V$ is due uniquely to the flux of matter feld fowing inside or outside this volume. However,this can be true only as long as we consider $T ^ { \mu \nu }$ as a given classical external source.As soon as we replace it with the energy-momentum tensor of dynamical matter fields,there will necessarily be an exchange of energy and of momentum between matter and the gravitational feld.For instance,there will be gravitational radiation emitted by the matter and going off to infinity,draining energy from the matter sources.Therefore the equation $\partial _ { \mu } T ^ { \mu \nu } = 0$ is untenable in a full dynamical theory,and eq.(2.1oo) cannot be exact.

In the full theory what should be cohserved is not the energy and momentum of the matter alone,but that of matter plus gravitational feld.To remedy this we could try to perform,on the right-hand side of eq. (2.100), the replacement

$$
T _ { \mu \nu }  T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } ,
$$

where $t _ { \mu \nu } ^ { ( 2 ) }$ is the energy-momentum tensor of thegravitons,obtained from the Pauli-Fierz action using the Noether theorem. Using eq. (2.10), we see that a Lagrangian quadratic in $h _ { \mu \nu }$ ，such as the Pauli-Fierz Lagrangian, produces an energy-momentum tensor quadratic in $h _ { \mu \nu }$ ， f the type,symbolically，dhdh. In eq (2.102) we added to $t _ { \mu \nu }$ the uperscript (2) to emphasize that it is quadratic in $h _ { \mu \nu }$ . Then,we are ed to try

$$
\Pi _ { \mu \nu } = - \frac { \kappa } { 2 } ( T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } ) ,
$$

nd the gauge condition $\partial ^ { \mu } \bar { h } _ { \mu \nu }$ is consistent with the conservation of the raviton plus matter energy-momentum tensor,

$$
\partial ^ { \mu } ( T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } ) = 0 .
$$

However,this cannot yet be the end of the story. The equation of motion 12.103) has a term, $( - 1 / 2 ) \kappa t _ { \mu \nu } ^ { ( 2 ) }$ , whic is quadratic in $h _ { \mu \nu }$ (and linear in and to derive it from an action principle,we must add to the action a term cubic in $h _ { \mu \nu }$ and proportional to $\kappa$ . Symbolically (i.e. omiting Lorentz indices), $\dot { t } _ { \mu \nu } ^ { ( 2 ) } \sim \partial h \partial h$ andatermofthistyeintheequatioso motion can be obtained adding to the action a term of the form hdhdh, or,restoring Lorentz indices,

$$
S _ { 3 } = \frac { \kappa } { 2 } \int d ^ { 4 } x h _ { \mu \nu } S ^ { \mu \nu } ( \partial h ) ,
$$

where $S ^ { \mu \nu } ( \partial h )$ should be of the|general form

$$
S ^ { \mu \nu } ( \partial h ) = A ^ { \mu \nu \rho \sigma \alpha \beta \gamma \delta } \partial _ { \rho } h _ { \alpha \beta } \partial _ { \sigma } h _ { \gamma \delta } ,
$$

and the tensor $A ^ { \mu \nu \rho \sigma \alpha \beta \gamma \delta }$ is a product of flat metric factors. At this stage,the action of the matter plus gravitational field must therefore be of the general form

$$
\begin{array} { l } { { S = S _ { 2 } + S _ { \mathrm { g f } } + S _ { \mathrm { i n t } } + S _ { 3 } ~ ( 2 . 1 0 7 ) } } \\ { { { } } } \\ { { = \displaystyle { \int d ^ { 4 } x \left[ - \frac { 1 } { 2 } \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + \frac { 1 } { 4 } \partial ^ { \mu } h \partial _ { \mu } h + \frac { \kappa } { 2 } h _ { \mu \nu } T ^ { \mu \nu } + \frac { \kappa } { 2 } h _ { \mu \nu } S ^ { \mu \nu } ( \partial h ) \right] } . } } \end{array}
$$

![](images/8043fb55da9f4140b0b880ab4b13adf7b163478ae72950aee4a6eb24d391720a.jpg)  
Fig. 2.4 The three-graviton vertex. Two lines carry a contribution proportional to their momentum.

$S ^ { \mu \nu } ( \partial h )$ isnotem in ty-mtion iomdoro $t _ { \mu \nu } ^ { ( 2 ) }$ $h \mu \nu _ { t _ { \mu \nu } ^ { ( 2 ) } ( h ) }$ in the equations of motion,a term

$$
\frac { \delta } { \delta h ^ { \mu \nu } } \left[ h ^ { \alpha \beta } t _ { \alpha \beta } ^ { ( 2 ) } ( h ) \right] = t _ { \mu \nu } ^ { ( 2 ) } \bigl ( h \bigr ) + h ^ { \alpha \beta } \frac { \delta } { \delta h ^ { \mu \nu } } \left[ t _ { \alpha \beta } ^ { ( 2 ) } ( h ) \right] ,
$$

sothereouldbetrauethf $t _ { \alpha \beta } ^ { ( 2 ) } ( h )$ There fore,in the action $h _ { \mu \nu }$ couples to|matter through the energy-momentum tensor of matter，but the coupling to itself is through a different ten-sor.In other words,the equivalence principle means that the energy-momentum tensor of GWs enters on the same footing as the energy momentum tensor of matter in the equations of motion, not in the action.

The cubic term in the action means that gravitons have a non-linear coupling to themselves and,in the language of Feynman graphs, corresponds to a vertex as shown inFig. 2.4. It is instructive to compare this situation with electrodynamics and with Yang-Mills theories. In electrodynamics,the photon mediates the interaction， but carries no electric charge. Therefore it does not couple directly to itself,and it does not contribute to the electric current.In Yang-Mills theories,in-stead, the gauge bosons are charged with respect to the gauge group, and therefore they couple non-linearly to themselves,and in the theory there are three-boson vertices and four-boson vertices. The situation for gravitons is analogous. Here the role of the current is played by the energy-momentum tensor, and the gravitons couple to their own energy momentum tensor (in the equations of motion; or to the corresponding functional $S ^ { \mu \nu } ( \partial h )$ in the action).We see that,with the inclusion of the cubic term in the action, our gauge theory of a massess particle with helicities ±2 begins to resemble to a non-Abelian gauge theory. 1

This suspicion is confirmed observing that the action (2.107) is no longer invariant under the linear gauge transformation (2.83) that was our starting point, since the term $h _ { \mu \nu } T ^ { \mu \nu }$ is invariant only if $\partial _ { \mu } T ^ { \mu \nu } = 0$ which is no longer true.Rather,under the transformation (2.83),

$$
\begin{array} { l } { { \delta \displaystyle \int d ^ { 4 } x \frac { \kappa } { 2 } h _ { \mu \nu } T ^ { \mu \nu } = \kappa \displaystyle \int d ^ { 4 } x ( \partial _ { \mu } \xi _ { \nu } ) T ^ { \mu \nu } } } \\ { { \displaystyle \quad = - \kappa \displaystyle \int d ^ { 4 } x \xi _ { \nu } \partial _ { \mu } T ^ { \mu \nu } } } \\ { { \displaystyle \quad = + \kappa \displaystyle \int d ^ { 4 } x \xi _ { \nu } \partial _ { \mu } t ^ { \mu \nu ( 2 ) } } } \\ { { \displaystyle \quad = - \kappa \displaystyle \int d ^ { 4 } x ( \partial _ { \mu } \xi _ { \nu } ) t ^ { \mu \nu ( 2 ) } . } } \end{array}
$$

However,we have seen that the preserce of a local gauge invariance is crucial to eliminate the spurious degrees of freedom in $h _ { \mu \nu }$ ，and we cannot afford to lose it at higher ordersin $\kappa$ .To remedy this,one can observe that this extra term can be canceled,at $O ( \kappa )$ ，promoting the linear gauge transformation (2.83) to a non-linear transformation of the generic form

$$
h _ { \mu \nu }  h _ { \mu \nu } - ( \partial _ { \mu } \xi _ { \nu } + \partial _ { \nu } \xi _ { \mu } ) + \kappa O ( h \partial \xi ) .
$$

Then the transformation of the graviton kinetic term produces a term $O ( \kappa )$ ,and it is possible to choose the tehsorial structure of the $O ( h \partial \xi )$ term so that it cancels the extra term coming from eq. (2.109). Thus, eq. (2.83) is the gauge symmetry of the theory only at the infinitesimal level,and at the finite level a non-linear gauge transformation emerges, just as in non-Abelian gauge theories.With the hindsight coming from Thefact that we know already that the full theory of gravitation is general relativity, werecognize in eq.(2.110)the expansion up to next-to-leading order of a finite diffeomorphism.

It is clear that the iteration procedure does not stop here,neither in the action nor in the gauge transformation. Once we add to the action the term $S _ { 3 }$ ,which is cubic in $h _ { \mu \nu }$ and proportional to $\kappa$ ,this produces through Noether's theorem） a contribution to the energy-momentum tensor of the graviton again cubic in $h _ { \mu \nu }$ and proportional to $\kappa$ We idusefultdisplaythe powes f $\kappa$ exlitys eenote iy $\kappa t _ { \mu \nu } ^ { ( 3 ) }$ Noether theorem,applied to the action (2.107), now gives

$$
\partial ^ { \mu } ( T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } + \kappa t _ { \mu \nu } ^ { ( 3 ) } ) = 0 .
$$

Therefore, consistency with $\partial ^ { \mu } \bar { h } _ { \mu \nu } = 0$ now requires toreplaceeq.(2.103) by

$$
\Pi \bar { h } _ { \mu \nu } = - \frac { \kappa } { 2 } ( T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } + \kappa t _ { \mu \nu } ^ { ( 3 ) } ) .
$$

Ih turn,the action which generates this equation of motion,that has a term cubic in $h _ { \mu \nu }$ and proportional to $\kappa ^ { 2 }$ ,must have an additional term quartic in $h _ { \mu \nu }$ and proportional to $\kappa ^ { 2 }$ ,so also its associated energy-

momentum tensor has a further term quartic in the fields and proportional to $\kappa ^ { 2 }$ ,that we denote by $| \kappa ^ { 2 } t _ { \mu \nu } ^ { ( 4 ) }$ , and then

$$
\Theta \bar { h } _ { \mu \nu } = - \frac { \kappa } { 2 } ( T _ { \mu \nu } + t _ { \mu \nu } ^ { ( 2 ) } + \kappa t _ { \mu \nu } ^ { ( 3 ) } + \kappa ^ { 2 } t _ { \mu \nu } ^ { ( 4 ) } + . . . ) ,
$$

where the dots indicate that the iteration continues to all orders. We recognize the full non-linear structure typical of Einstein gravity, with arbitrarily large powers of $h _ { \mu \nu }$ ,and a non-linear gauge invariance. Indeed,there exists a simple and |explicit resummation algorithm,due to Deser,which gives back the Einstein equations. This algorithm uses the first order Palatini formalism,where the action becomes a cubic polynomial in the variable $\sqrt { - g } g _ { \mu \nu }$ and in the Christoffel symbol (which in a first order formalism are varied independently),and the iteration stops at finite order,see the Further Reading section. So,general relativity can be inferred “bottom up”，i.e. starting from gravitons. However, some aspects of this reconstruction procedure are not unique. In particular the full Einstein action includes a boundary term, since it can be written as

$$
\begin{array} { l } { { \displaystyle S _ { E } = \frac { 1 } { 1 6 \pi G } \int d ^ { 4 } x \sqrt { - g } R } } \\ { { \displaystyle ~ = \frac { 1 } { 1 6 \pi G } \int d ^ { 4 } x \left[ \sqrt { - g } \mathcal { L } _ { 2 } - \partial _ { \mu } K ^ { \mu } \right] , } } \end{array}
$$

where

$$
{ \mathcal { L } } _ { 2 } = g ^ { \mu \nu } \left( { \Gamma } _ { \beta \mu } ^ { \alpha } { \Gamma } _ { \alpha \nu } ^ { \beta } - { \Gamma } _ { \mu \nu } ^ { \alpha } { \Gamma } _ { \alpha \beta } ^ { \beta } \right)
$$

is quadratic in the first derivative of the metric (it is usually called the TT' Lagrangian), and

$$
K ^ { \mu } = \sqrt { - g } \left( { g } ^ { \mu \nu } \Gamma _ { \alpha \nu } ^ { \alpha } - { g } ^ { \alpha \beta } \Gamma _ { \alpha \beta } ^ { \mu } \right) .
$$

The latter term is a total divergence and therefore does not affect the equations of motion.15 However, boundary terms are relevant in the quantum theory, and in particular the boundary term in eq. (2.114) becomes physically relevant in semiclassical quantum gravity, in connection with black hole thermodynamics. It is clear that boundary terms are beyond the reach of the iterative procedure that starts from the Pauli-Fierz action, since at each stage of the procedure we have ambiguities connected with the possibility of dropping boundary terms. For instance, from the very beginning,we might have chosen to retain the third term in eq.(2.84) rather than the second term. More formally, expanding $g _ { \mu \nu } = \eta _ { \mu \nu } + \kappa h _ { \mu \nu } , \mathcal { L }$ $\mathcal { L } _ { 2 }$ has the structure (we drop all Lorentz indices,since we are only interested in the dependence on $\kappa$ ）

$$
\begin{array} { r } { \frac { 1 } { 3 2 \pi G } \displaystyle \int d ^ { 4 } x \sqrt { - g } \mathcal { L } _ { 2 } \sim \frac { 1 } { \kappa ^ { 2 } } \displaystyle \int d ^ { 4 } x \left[ \kappa ^ { 2 } ( \partial h ) ^ { 2 } + \kappa ^ { 3 } h \partial h \partial h + \ldots \right] } \\ { \sim \displaystyle \int d ^ { 4 } x \left[ ( \partial h ) ^ { 2 } + \kappa h \partial h \partial h + O ( \kappa ^ { 2 } ) \right] , ( 2 \kappa ( h ) ^ { 2 } ) } \end{array}
$$

and therefore is analytic in $\kappa$ . On the contrary,

$$
\begin{array} { c } { { \displaystyle { \frac { 1 } { 3 2 \pi G } } \int d ^ { 4 } x \partial _ { \mu } K ^ { \mu } \sim \frac { 1 } { \kappa ^ { 2 } } \int d ^ { 4 } x \partial ^ { 2 } ( \eta + \kappa h ) } } \\ { { \sim \displaystyle { \frac { 1 } { \kappa } } \int d ^ { 4 } x \partial ^ { 2 } h . } } \end{array}
$$

Therefore this term is non-analytic in $\kappa$ and cannot be obtained unambiguously from the resummation of an expansion in powers of $\kappa$ ,without further physical input.

Alternatively we can proceed top-down,starting from Einstein action and expanding it in powers of $h _ { \mu \nu }$ ,obtaining all non-linear interaction terms.Observe that in this section we have given to $h _ { \mu \nu }$ the dimensions of mass that are canonical in field theory,and the dimensionless metric $h _ { \mu \nu }$ is recovered with the rescaling (2.87).Therefore,the expansion that we are performing in this section can be written as

$$
\begin{array} { c } { { g _ { \mu \nu } = \eta _ { \mu \nu } + ( 3 2 \pi G ) ^ { 1 / 2 } h _ { \mu \nu } } } \\ { { = \eta _ { \mu \nu } + \kappa h _ { \mu \nu } , } } \end{array}
$$

where $h _ { \mu \nu }$ has the canonical dimensionl of mass and $\kappa$ ,dimensionally, is the inverse of a mass.Given the cubic,quartic,and higher terms in the action,one can read the corresponding vertices and compute scattering amplitudes using the Feynman rules.For instance,the $2  2$ graviton scattering amplitude is obtained from the $s$ -channel graph of Fig.2.5 (together with the corresponding $u$ -channel and $t$ -channel graphs),and from the four-graviton vertex of Fig.2.6,so this amplitude is $O ( \kappa ^ { 2 } )$ ,i.e. $O ( G )$ 16

# 2.2.4Effective field theories and the Planck scale

In units $\hbar = c = 1$ ,the Newton constant has the dimensions of the inverse of a mass squared,and therefore $\kappa \sim G ^ { 1 / 2 }$ is the inverse of a mass.The fact that the coupling constant $\kappa$ has dimensions of the inverse of mass means that the quantization of gravity should give rise to a non-renormalizable theory.This isexpected first of all on the basis of simple dimensional considerations. For instance,we have seen that the three-graviton vertex has the generic form κhdhdh.The fact that there are two derivatives is dictated by dimensional analysis.In fact, the dimensions of any term in the Lagrangian density $\mathcal { L }$ must be $( \mathrm { m a s s } ) ^ { 4 }$ , so that the action $\int d ^ { 4 } x { \mathcal { L } }$ is dimensionless (recall that in this section we are using units $\hbar = c = 1$ ,and then in particular a length has the dimensions of $\mathrm { ( m a s s ) } ^ { - 1 }$ ,see Note 2).The kinetic term is,symbolically, $( \partial h ) ^ { 2 }$ and since $\partial _ { \mu } = \mathrm { 1 / l e n g t h = \ m a s s }$ ，we see that $h _ { \mu \nu }$ must have dimensions of mass.

The three-graviton vertex therefore must necessarily carry two powers of the momentum: in fact κhhh $\sim ( \mathrm { m a s s } ) ^ { 2 }$ ,and to get something trilinear in $h$ and proportional to $\kappa$ we|must add two derivatives,so we must have something of the form κhahah. In momentum space each

![](images/05d87f782804138db862d10ef54bb50d0cd71d71a1e986fefcf4f90e575230ed.jpg)

![](images/d3fa74e274cd7baa8e94e4dce1330808e31daa015fcaf7c46676733ab2cf19b6.jpg)  
Fig.2.5 A diagram contributing to the $2  2$ graviton scattering amplitude.   
Fig.2.6 The four-graviton vertex.

16The explicit expresson for the threegraviton vertex，and the (discouragingly long) four-graviton vertex can be found in eqs.(2.6) and (2.7) of DeWitt (1967)．To compute a $2  2$ graviton scattering amplitude in the Born approximation it is however sufficient to know the three-graviton vertex with two gravitons on-shell and only one offshell,while in the four-graviton vertex all lines are on-shell. Then in the on-shell lines we can impose $\partial ^ { \nu } h _ { \mu \nu } =$ 0and $\textit { h } = \textit { 0 }$ ，and the vertices becomes more manageable,see Grisaru, van Nieuwenhuizen and $\mathrm { W u }$ (1975).

derivative gives a power of momentum, and we can see, writing explicitly some Feynman graphs,that with more and more insertions of this vertex we get Feynman graphs which (barring cancellations) are more and more divergent. Consider for instance the insertion of an internal graviton line in a Feynman graph, obtained adding two three-graviton vertices on two external lines,and connecting them by a graviton propagator,as in Fig.2.7. Denote by $q ^ { \mu }$ the momentum of this internal line. Adding this internal line we have created a new closed loop, which gives an integration over $d ^ { 4 } q$ .There are three propagators in the loop,and at large $q$ each of them is $\sim 1 / q ^ { 2 }$ . Finally, each of the two vertices gives a factor $q _ { \mu } q _ { \nu }$ . Then, barring cancellations,the insertion of two vertices brings a further factor that,in the ultraviolet,is of order

![](images/3051b5356845486454d71c49f9602e9eb21972c7098cf77d11476c6666c4df22.jpg)  
Fig.2.7 The insertion of an internal graviton line among two external lines. The blob denotes all the remaining (unspecified） part of the Feynman graph.

$$
\kappa ^ { 2 } \int d ^ { 4 } q { \frac { 1 } { ( q ^ { 2 } ) ^ { 3 } } } q _ { \mu } q _ { \nu } q _ { \rho } q _ { \sigma } ,
$$

and so is quadratically divergent. Therefore,adding two vertices we have introduced a new divergence in the graph. Inserting more vertices worsens the situation further and we get stronger and stronger divergencies. The same happens with insertions of the four-graviton vertex, five-graviton vertex,etc.

This lack of renormalizability, however,is not at all a problem as long as we study processes taking place at suffciently small energies. The problem with non-renormalizable theories is a matter of predictivity not of mathematical consistency: in the language of counterterms, the divergences are canceled adding to the Lagrangian terms that have a different functional form,compared to the only term $\scriptstyle { \sqrt { - g R } }$ present in Einstein gravity and, as we increase the number of loops, more and more counterterms are required. For instance, to one-loop order one must add to the Lagrangian a term proportional to $R _ { \mu \nu } R ^ { \mu \nu }$ and a term proportional to R²,to two-loop order we have for instance terms proportional to $R _ { \mu \nu \rho \sigma } R ^ { \rho \sigma \alpha \beta } R _ { \alpha \beta } { } ^ { \mu \nu }$ ,etc.17 Therefore the divergences cannot be reabsorbed into a renormalization of the Newton constant and of the fields. Rather,the coefficients of all these terms have a divergent part which is chosen so that it cancels the divergencies coming from the loops, and a finite part that must be fixed by comparison with experiments. Thus, we end up with a theory which,by definition, is finite, but apparently is left with very little predictive power, since we must fix an infinite number of amplitudes by comparison with experiments.

17More precisely， in the background field method one expands gμv = gμv + $h _ { \mu \nu }$ ,where $\bar { g } _ { \mu \nu }$ is a classical solution of the equations of motion and $h _ { \mu \nu }$ isa quantum field which,in the path integral formulation,is integrated over.After integrating over the quantum fluctuations $h _ { \mu \nu }$ ,we are left with the counterterms evaluated on $\bar { g } _ { \mu \nu }$ For pure gravity，i.e.when we neglect matter fields, $R _ { \mu \nu }$ evaluated on any classical solution $\bar { g } _ { \mu \nu }$ gives zero,and there fore the one-loop divergences disappear. This miracle does not repeat at higher orders,and does not take place even at one loop if we also have matter fields (in pure supergravity the divergencies cancel even at two-loop order, but not to higher orders).

However， this loss of predictivity is not important at low energies. In quantum gravity， we have seen that the coupling constant is $\kappa =$ $( 3 2 \pi G ) ^ { 1 / 2 }$ .Defining the Planck mass $M _ { \mathrm { P l } }$ (in our units $\hbar = c = 1$ by

$$
G = \frac { 1 } { M _ { \mathrm { P l } } ^ { 2 } } ,
$$

we have

$$
\kappa = \frac { ( 3 2 \pi ) ^ { 1 / 2 } } { M _ { \mathrm { P l } } } \ .
$$

The perturbative expansion in quantum gravity, which is an expansion in $\kappa ^ { 2 }$ , is therefore an expansion in powers of $1 / M _ { \mathrm { P l } } ^ { 2 }$ After renormalizing

the theory,each scattering amplitude with $N$ external legs,computed up to order $( \kappa ^ { 2 } ) ^ { n } \sim 1 / M _ { \mathsf { P l } } ^ { 2 n }$ ,has the generic form

$$
A _ { N } ( E ) = A _ { N } ^ { 0 } ( E ) \left( 1 + c _ { 1 } \frac { E ^ { 2 } } { M _ { \mathrm { P l } } ^ { 2 } } + c _ { 2 } \frac { E ^ { 4 } } { M _ { \mathrm { P l } } ^ { 4 } } + \ldots + c _ { n } \frac { E ^ { 2 n } } { M _ { \mathrm { P l } } ^ { 2 n } } \right) ,
$$

For simplicity we assumed that there is only one relevant energy scale $E$ in the amplitude (which in principle depends on all the Lorentz-invariant quantities that one can make with the external momenta). The nonrenormalizability of the theory means that，whatever the value of $N$ ， we can always find a sufficiently large order $n$ in perturbation theory, where a genuinely new divergence appears,which is not automatically cured by the renormalization of Green's functions with a smaller number of external legs.Therefore,the coefficients $c _ { 1 } , c _ { 2 } , \ldots , c _ { n - 1 }$ are finite and calculable once we have renormalized the Green's functions $A _ { M }$ with $M < N$ ,but the coefficient $c _ { n }$ must be fixed by comparison with experiment,and this is the origin of the lack of predictivity.

However, as long as $E \ll M _ { \mathrm { P l } } .$ ，terms suppressed by powers of $E / M _ { \sf P l }$ are completely irrelevant,and the lack of predictivity due to the fact that $c _ { n }$ should be fixed by comparison with experiment is more apparent than real.As long as we study, say, a graviton-graviton scattering process at a center-of-mass energy $E \ll M _ { \mathrm { P l } }$ ,all higher-loop corrections are totally insignificant. Given the huge value of the Planck mass,

$$
M _ { \mathrm { P l } } \simeq 1 . 2 \times 1 0 ^ { 1 9 } \mathrm { G e V } ,
$$

this means that the lowest-order effective action,i.e. classical general relativity,is completely adequate in all “normal”situations.To see the effect of higher-order terms in the perturbative expansion,we should for instance perform a scattering experiment at center-of-mass energies of order $M _ { \mathrm { P l } }$ ,or,equivalently,we should probe the structure of spacetime at length-scale of the order of the Planck length, $l _ { \mathsf { P l } } = 1 / M _ { \mathsf { P l } } \sim$ $1 0 ^ { - 3 3 }$ cm.In accelerator physics,this isbeyond any conceivable future development.Possibly,our best chances of exploring this extremely energetic region is through the observation of some relic of the Big Bang, and in particular stochastic backgrounds|of relic GWs,as we will discuss i Vol.2. However,as long as we consider “normal”astrophysical situations,the lack of predictivity at the Planck scale becomes irrelevant, and general relativity isa totallyadequate low-energy effective field theory. The fact that the expansion (2.123) blows up as $E$ approaches $M _ { \mathrm { P l } }$ signals that at this point a new theory must set in.

# 2.3 Massive gravitons

h Section 2.2 we introduced the notion of graviton,and we saw that it is lescribed by a massless spin-2 field.Froma particle physicist's point of view,one of the most natural extensions of Einstein gravity consists in dding to the graviton a small mass term. However,as we will see in this section,the introduction of a mass term for the graviton turns out to be

This section lies outside the main theme of the book,and can be omitted in a first reading.As in the previous section,we use units $\hbar = c = 1$ 、

quite subtle from a feld-theoretical point of view. In particular the limit $m _ { g }  0$ is very delicate,up to the point that one is led to discuss whether the graviton mass should be identically zero. Before entering into these considerations,however,we discuss at a simpler phenomenological level the bounds on the graviton mass.

# 2.3.1Phenomenological bounds

In general, we expect that a boson with a mass mg should mediate a short-range force which,compared to the massless case,is suppressed by a factor proportional to $\exp \{ - m _ { g } r \}$ . In the case of the graviton, such an exponential would cut off the gravitational interaction at a distance $_ r$ larger than the reduced Compton wavelength Xg= 1/mg (or, reinstating h and c, at distances larger than Xg= h/(mgc)).

However, we know experimentally that our Galaxy is held together by gravitation, which means that, at least up to a scale $r _ { \mathrm { g a l } } \sim 1 0 \mathrm { k p c }$ ,there is no sensible attenuation of the Newton's law, so Xg cannot be much smaller that 10 kpc.Taking,for definiteness,Xg > 2 kpc,this already gives a bound $m _ { g } = 1 / \lambda _ { g } < 3 \times 1 0 ^ { - 2 7 } ~ \mathrm { e V }$

Actually, the experimental bound on the mass of the graviton is even stronger, since we know that the gravitational interaction is not expo-nentially suppressed even at the intergalactic scale. Our Galaxy has a number of small satellite galaxies,bound by the gravitational force, at distances up to $2 6 0 \ \mathrm { k p c . ^ { 1 8 } }$ The Andromeda galaxy， at a distance of 730 kpc, is the nearest giant spiral galaxy,and is approaching the center of mass of our galaxy with a speed u = -119 km/s. The most natural explanation is that the relativeHubble expansion between our Galaxy and Andromeda has been halted and reversed by the mutual gravitational attraction.19 This tels us that Xg cannot be much smaller than, say, $O ( 1 0 0 )$ kpc. On the scale of hundreds of kpc to $1 \ \mathrm { M p c }$ ，galaxies are seen to be distorted gravitationally by their reciprocal interaction, creating bridges and tails in their shapes. On the scale (1-1O) ho Mpc, where $h _ { 0 }$ is the Hubble expansion rate in units of $1 0 0 \ \mathrm { k m } \ \mathrm { s ^ { - 1 } M p c ^ { - 1 } }$ (the current values is ho = O.73 ± O.03),clusters of galaxies are held together by the gravitational attraction,so we can infer that g cannot be much smaller than a few Mpc. Taking,conservatively,

$$
\lambda _ { g } > \mid 3 0 0 h _ { 0 } \mathrm { ~ k p c } ,
$$

results in a bound

$$
m _ { g } < 2 \times 1 0 ^ { - 2 9 } h _ { 0 } ^ { - 1 } \mathrm { e V } .
$$

This bound,of course,refers only to the lightest particle that mediates the gravitational interaction. In some extensions of general relativity, and in particular in theories with extra dimensions,the graviton is accompanied by a whole family of massive excitations (the Kaluza-Klein modes). The bound (2.l26) only refers to the lowest lying state,and says nothing about the possibility of further massive gravitons,whose effect vanishes on much shorter length-scales.

There is however a potential loophole in the above arguments.We saw in eq.(2.98) that the static gravitational potential is determined by $D _ { 0 0 0 0 }$ ,i.e.by the propagator of the component $h _ { 0 0 }$ of $h _ { \mu \nu }$ ，which is a scalar under spatial rotation.Gravitational waves,instead,are described by $h _ { i j } ^ { \mathrm { T T } }$ ，whichisaspin-2tensorunderrotatios.Itisposble to construct consistent models where Lorentz invariance is broken and the masses of scalar,vector and tensor perturbations are different.In particular, $h _ { i j } ^ { \mathrm { T T } }$ canbemassivewhilescalarperturbations (obtainedfrom gauge-invariant combinations of $h _ { 0 0 }$ and of the trace $h$ )remains massless, see the Further Reading.The bounds that we discussed above really refer to the mass of the scalar perturbations,and is the same as the mass of $h _ { i j } ^ { \mathrm { T T } }$ only if Lorentz invariance holds.

Adirect bound on the massofthe tensor mode $h _ { i j } ^ { \mathrm { T T } }$ can be obtained from binary pulsars.A binary neutron star system looses energy because it radiates GWs,and this changes its orbital period.The remarkable agreement between the prediction of general relativity for the orbital change,and the measured value for the binary pulsar PSR B1913+16, is in fact one of the great experimental triumphs of general relativity, and also constitutes the first experimental confirmation of the emission $\theta \mathrm { f } \ : \mathrm { G W s }$ ,and will be discuss in great detail in Chapter 6.

We can understand qualitatively how a bound on the graviton mass emerges from the study of binary pulsars,as follows.The system emits GWs at frequencies of order of its orbital frequency $\omega _ { s }$ .20 Then, first of all we must have $m _ { g } c ^ { 2 } < O ( \hbar \omega _ { s } )$ or,ih the units $\hbar = c = 1$ that we are using in this chapter, $m _ { g } < O ( \omega _ { s } )$ ,otherwise such massive gravitons could not even be emitted. For $m / \omega _ { s }$ small,one finds that the correction $1 0$ the energy radiated in GWs by the source are of order $( m _ { g } / \omega _ { s } ) ^ { 2 }$ ， with respect to the massess case.2i Since the agreement between theory and experiment is of order of $0 . 1 \%$ (see Chapter 6) we must actually have,in order of magnitude, $( m _ { g } / \omega _ { s } ) ^ { 2 } < { \cal O } ( 1 0 ^ { - 3 } )$ .Given that the orbital period of PSR $\mathrm { B } 1 9 1 3 { + } 1 6$ is about $8 \ \mathrm { h r }$ ,we immediately get an order-of-magnitude estimate of the bouhd, $m _ { g } < O ( 1 0 ^ { - 2 0 } )$ eV.A more quantitative analysis of the orbital decay rate of PSR $\mathrm { B } 1 9 1 3 { + } 1 6$ (and also of another binary system that will be discussed in Chapter 6,PSR $B 1 5 3 4 + 1 2$ ）including a mass term for the graviton gives22

$$
m _ { g } < 7 . 6 \times 1 0 ^ { - 2 0 } \mathrm { e V } ,
$$

corresponding to a value of $\lambda _ { g }$ of the order of the size of the solar system. Similar bounds on $m _ { g }$ would also come from the direct observation of te waveform of inspiraling compact binaries with interferometric detectors.23

The issue of the graviton mass has potentially important cosmologlal implications,e.g. in connection with attempts of modifying Einstein gravity at cosmological distances (which is largely motivated by the problem of dark matter and dark ehergy).Furthermore,the whole subject is quite interesting from a field-theoretical point of view.We herefore discuss,in the rest of this section,the field-theoretical probms that arise when we attempt to give a mass to the graviton.

20As we will compute in Section 4.1.2, for PSR $\mathrm { B } 1 9 1 3 + 1 6$ the spectrum of the radiation emitted is actually peaked toward high harmonics of the orbital frequency,because of the large eccentricity of this binary system.

21This comes out repeating the same steps that we willdo in Section 3.1,usinga massive rather than a massless wave equation for $h _ { \mu \nu }$ .Since a massive Klein-Gordon type equation depends $m _ { g } ^ { 2 }$ ,thefrstcorrectiontothera diated energy will also be proportional to the second power of $m _ { g }$

22This analysis has been done by Finn and Sutton (2002) using a mass term for the graviton which actually implies the existence of six degrees of freedom, the five associated to a massive spin-2 graviton plus an additional scalar field, which however is a ghost,i.e.it has the wrong sign of the kinetic energy (see the discussion in Section 2.3.2 below). Different mass terms,and in particular Lorentz-violating mass terms,should however give similar results.

23The basic idea is that,for a massive graviton, the dispersion relation is $\hbar \omega = \gamma m c ^ { 2 }$ ,where $\gamma = ( 1 - v ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 }$ is the usual relativistic factor. Inverting this for $_ v$ and using units $\hbar = c = 1$ ， we get

$$
v ( \omega ) = \sqrt { 1 - \frac { m ^ { 2 } } { \omega ^ { 2 } } } .
$$

In the inspiral amplitude (that will be studied in Section 4.1) the radiation emitted earlier in the inspiral phase is at lower frequencies,and therefore travels slightly slower than the radiation emitted at later times,resulting in a potentially observable distortion of the waveform observed at the detector,see Will (1998).

# 2.3.2 Field theory ofmassive gravitons

# A warm-up: massive photons

We want to understand how to construct a consistent field theory for a massive graviton. As a warm-up exercise, let us first recall what happens in electrodynamics if we add by hand a mass term to the photon. The Lagrangian of a massive photon interacting with a conserved current $j _ { \mu }$ is

$$
\mathcal { L } = - \frac { 1 } { 4 } F _ { \mu \nu } F ^ { \mu \nu } - \frac { 1 } { 2 } m _ { \gamma } ^ { 2 } A _ { \mu } A ^ { \mu } - j _ { \mu } A ^ { \mu } .
$$

24For the purpose of our discussion, it will not be important whether this mass term has been added by hand,or if it results from a Higgs mechanism.

This is known as the Proca Lagrangian and is not gauge-invariant,because of the mass term.24 This is as it should be, because in the massless case gauge invariance reduces the four degrees of freedom of $A _ { \mu }$ to only two degrees of freedom, the two helicity states of the photon,while we want to describe a massive particle,and a massive particle with spin $j = 1$ has $2 j + 1 = 3$ degrees of freedom.Still，in order to describe the three physical degrees of freedom of a massive photon with the four components of $A _ { \mu }$ ，we need to eliminate one degree of freedom. Of course，we cannot do it by imposing the condition $\partial _ { \mu } A ^ { \mu } = 0$ in the above Lagrangian with a gauge-fixing procedure, since there is no gauge symmetry to be fixed. Rather,the condition $\partial _ { \mu } A ^ { \mu } = 0$ is recovered as follows. The equations of motion obtained from (2.129) are

$$
\partial _ { \mu } F ^ { \mu \nu } - m _ { \gamma } ^ { 2 } A ^ { \nu } = j ^ { \nu } .
$$

Acting with $\partial _ { \nu }$ on both sides we find $\partial _ { \nu } \partial _ { \mu } F ^ { \mu \nu } = 0$ ，because $\partial _ { \nu } \partial _ { \mu }$ is symmetric while $F ^ { \mu \nu }$ is antisymmetric, and $\partial _ { \nu } j ^ { \nu } = 0$ because we have coupled $A ^ { \mu }$ to a conserved current. Then, eq. (2.130)implies

$$
m _ { \gamma } ^ { 2 } \partial _ { \nu } A ^ { \nu } = 0 ,
$$

and,if $m _ { \gamma } \neq 0$ ， we get the Lorentz condition $\partial _ { \nu } A ^ { \nu } = 0$ dynamically, and we have eliminated one degree of freedom. In momentum space this gives $k _ { \mu } \tilde { A } ^ { \mu } ( k ) = 0$ . Since for a massive particle the rest frame exists, we can choose the frame where $k ^ { \mu } \equiv ( m _ { \gamma } , 0 , 0 , 0 )$ , so we have eliminated the component $A _ { 0 }$ ,and we remain with the three components of the vector A that describe a massive $\mathrm { s p i n } { - 1 }$ particle,as it should be.25

Still,it can be disturbing to|observe that,apparently, the zero mass limit is discontinuous, because the number of physical degrees of freedom seems to change abruptly from three,for $m _ { \gamma } \neq 0$ ,to two for $m _ { \gamma } = 0$ . To understand this point,let us see what are the polarization states of a massive photon and their coupling to the current $j ^ { \mu }$ . Consider first the propagation of a free massive photon,i.e. eq. (2.130) with $j ^ { \nu } = 0$

$$
\partial _ { \mu } ( \partial ^ { \mu } A ^ { \nu } - \partial ^ { \nu } A ^ { \mu } ) - m _ { \gamma } ^ { 2 } A ^ { \nu } = 0 .
$$

Using $\partial _ { \mu } A ^ { \mu } = 0$ ,which follows from eq. (2.131),this becomes a massive wave equation,

$$
( \ d \Game \partial \ L ) A ^ { \mu } = 0 ,
$$

whose solution is a superposition of plane waves of the form ε(k)eikx with $k ^ { 2 } = - m _ { \gamma } ^ { 2 }$ ,and of their complex conjugates.The condition (2.131) implies

$$
\epsilon _ { \mu } ( k ) k ^ { \mu } = 0 .
$$

We choose a frame where ${ k ^ { \mu } } = ( \omega , 0 , 0 , \ k _ { 3 } )$ with $\omega ^ { 2 } = k _ { 3 } ^ { 2 } + m _ { \gamma } ^ { 2 }$ . In this frame two solution of eq.(2.134) are given by the transverse vectors

$$
\epsilon _ { \mu } ^ { ( 1 ) } ( k ) = ( 0 , 1 , 0 , 0 ) , \epsilon _ { \mu } ^ { ( 2 ) } ( k ) = ( 0 , 0 , 1 , 0 ) ,
$$

which are the same as the usual transverse degrees of freedom of a massless photons.Fora massive photon there is however also a third physical solution

$$
\epsilon _ { \mu } ^ { ( 3 ) } ( k ) = \frac { 1 } { m _ { \gamma } } ( - k _ { 3 } , 0 , 0 , \omega ) .
$$

All three polarization vectors are norinalized so that $\epsilon _ { \mu } \epsilon ^ { \mu } = 1$ To understand what happens to the polarization state (2.136) in the limit $m _ { \gamma }  0$ ,we observe that we can rewriteit in terms of $k _ { \mu } = ( - \omega , 0 , 0 , k _ { 3 } )$ ， as

$$
\epsilon _ { \mu } ^ { ( 3 ) } ( k ) = \frac { 1 } { m _ { \gamma } } k _ { \mu } + \frac { \omega - k _ { 3 } } { m _ { \gamma } } ( 1 , 0 , 0 , 1 ) .
$$

The interaction of this state with the current $j ^ { \mu }$ is proportional to ${ \epsilon } _ { \mu } ^ { ( 3 ) } ( k ) \tilde { j } ^ { \mu } ( k )$ If thecurrentisconserved $k _ { \mu } \widetilde { j } ^ { \mu } ( k ) = 0$ and the frst term in eq.(2.137) does not contribute.In the limit $m _ { \gamma }  0$ ,we expand $\omega = ( k _ { 3 } ^ { 2 } + m _ { \gamma } ^ { 2 } ) ^ { 1 / 2 } \simeq k _ { 3 } + m _ { \gamma } ^ { 2 } / ( 2 k _ { 3 } )$ ,and therefore

$$
\begin{array} { c } { { \epsilon _ { \mu } ^ { ( 3 ) } ( k ) \tilde { j } ^ { \mu } ( k ) = \displaystyle \frac { \omega - k _ { 3 } } { m _ { \gamma } } \left[ \tilde { j } ^ { 0 } ( k ) + \tilde { j } ^ { 3 } ( k ) \right] } } \\ { { \displaystyle \simeq \frac { m _ { \gamma } } { 2 k _ { 3 } } \left[ \tilde { j } ^ { 0 } ( k ) + \tilde { j } ^ { 3 } ( k ) \right] . } } \end{array}
$$

Therefore, in the massless limit,the longitudinal mode of a massive photon decouples,and the limit $m _ { \gamma }  | 0$ is continuous.26 Observe that Current conservation has been crucial to show the decoupling of the longitudinal state.

The continuity of the limit $m _ { \gamma } \neq 0$ ，asfar as physical observables Are concerned,can also be seen from the propagator,as follows. The propagator of the massive photon is found from the quadratic term in the action which,after an integration byparts,reads

$$
S = \frac { 1 } { 2 } \int d ^ { 4 } x A _ { \mu } \left[ \eta ^ { \mu \nu } ( \partial ^ { 2 } - m _ { \gamma } ^ { 2 } ) - \partial ^ { \mu } \partial ^ { \nu } \right] A _ { \nu } .
$$

In momentum space, $\partial _ { \mu } \to i k _ { \mu }$ and we must therefore invert the matrix

$$
M ^ { \mu \nu } ( k ) = - \eta ^ { \mu \nu } ( k ^ { 2 } + m _ { \gamma } ^ { 2 } ) + k ^ { \mu } k ^ { \nu } .
$$

Ile inversion is easily performed writing $M ^ { - 1 }$ in the general form

$$
( M ^ { - 1 } ) _ { \mu \nu } = a ( k ) \eta _ { \mu \nu } + b ( k ) k _ { \mu } k _ { \nu } ,
$$

and fixing $a ( k )$ and $b ( k )$ from ${ \cal M } ^ { \mu \rho } ( M ^ { - 1 } ) _ { \rho \nu } ~ = ~ \delta _ { \nu } ^ { \mu }$ This gives $a =$

$^ { 2 6 } \mathrm { T } _ { 0 }$ illutrate thecontinuityof the physics as $m _ { \gamma }  0$ ,consider the following example.In a thermal ensemble, each degree of freedom contributes to the thermodynamical properties,such as the internal energy or specific heat. For instance,in a relativistic Bose gas at equilibrium,the average energy density is $\rho = ( \pi ^ { 2 } / 3 0 ) g T ^ { 4 }$ ，where $g$ is the number of polarization degrees of freedom．Therefore there is a finite difference between the energy density for massless photons $( g = 2 )$ and massive photons $( g = 3 )$ .Apparently,from a measure of thermal properties of such a gas we should be able to decide whether $m _ { \gamma } ~ = ~ 0$ exactly,or $m _ { \gamma } \neq 0$ However,in the limit $m _ { \gamma } \ \to \ 0$ the longitudinal mode takes an infinite time to reach equilibrium with the thermal bath,because its interactions goes to zero.Therefore any experiment lasting a finite time will only be able either to discover a positive mass or to put an upper limit on it,but not to state that $m _ { \gamma } = 0$ exactly.

27We do not write explicitly the ie pre scription.In all cases,with our choice of signature,it is obtained replacing $k ^ { 2 } \to \bar { k } ^ { 2 } \to i \epsilon$ in the denominators.

$- 1 / ( k ^ { 2 } + m _ { \gamma } ^ { 2 } )$ ， $b _ { \scriptscriptstyle \mathrm { - } \mathrm { - } } = a / m _ { \gamma } ^ { 2 }$ .The propagator is defined by $\tilde { D } _ { \mu \nu } ( k ) =$ $i ( M ^ { - 1 } ) _ { \mu \nu }$ Then27

$$
\tilde { D } _ { \mu \nu } ( k ) = \frac { - i } { k ^ { 2 } + m _ { \gamma } ^ { 2 } } \left( \eta _ { \mu \nu } + \frac { k _ { \mu } k _ { \nu } } { m _ { \gamma } ^ { 2 } } \right) .
$$

The propagator of a massive photon is therefore singular in the limit $m _ { \gamma }  0$ .However, the singularity disappears from physical observables, because the amplitudes are prpportional to

$$
\tilde { j } _ { \mu } ^ { * } ( k ) \tilde { D } ^ { \mu \nu } ( k ) \tilde { j } _ { \nu } ( k ) .
$$

Since the current is conserved, $k ^ { \mu } \tilde { j } _ { \mu } ( k ) = 0$ ，and therefore the terms $k _ { \mu } k _ { \nu } / m _ { \gamma } ^ { 2 }$ in the propagator give zero.We can therefore simply take as propagator of the massive photon the expression

$$
\tilde { D } _ { \mu \nu } ( k ) = \frac { - i } { k ^ { 2 } + m _ { \gamma } ^ { 2 } } \eta _ { \mu \nu } ,
$$

and in the the limit $m _ { \gamma }  0$ we recover smoothly the massless photon propagator (2.77). The whole procedure required that the massive photon is coupled to a conserved current $j ^ { \mu }$

# Massive gravitons

Now that we have understood how to describe a massive photon, we can come back to our original problem，the construction of a field theory for massive gravitons.We start from the Pauli-Fierz action (2.86),and we add a mass term.The most general Lorentz-invariant mass terin that one can add to the Pauli-Fierz action is a combination of the two scalars $h _ { \mu \nu } h ^ { \mu \nu }$ and $h ^ { 2 }$ . Of course both terms break the gauge invariance (2.83)of the massless theory,as it should,since we want to describe the $2 j + 1 = 5$ degrees of freedom of a massive spin-2 particle,while we have seen that gauge invariance reduces them to only two. Nevertheless,a generic symmetric tensor $h _ { \mu \nu } | \mathrm { h a s ~ 1 0 }$ degrees of freedom so we expect that the appropriate number of conditions to reduce it to five emerges dynamically, similarly to what we have found for massive photons.

Of course,for massive gravitons we must start from the Pauli-Fierz action (2.86) before gauge-fixing,since now there is no gauge symmetry to fix.Adding the mass term,and writing also the source term,we have

$$
\begin{array}{c} \begin{array} { c } { { S _ { 2 } = \displaystyle \frac { 1 } { 2 } \int d ^ { 4 } x \left[ \begin{array} { l } { { - \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } } } \\ { { } } \end{array} + 2 \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } - 2 \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h + \partial ^ { \mu } h \partial _ { \mu } h \right.} } \\ { { + c _ { 1 } h ^ { 2 } + c _ { 2 } h _ { \mu \nu } h ^ { \mu \nu } + \tilde { \kappa } h _ { \mu \nu } T ^ { \mu \nu } ] . } } \end{array}    \end{array}
$$

We denote the coupling of the massive theory by $\tilde { \kappa }$ since,as we will see below,it need not be the same as the coupling $\kappa$ introduced in the massless case.We can now obtain the propagator of the massive graviton repeating the same steps performed above for the photon,and we discover that,if we add to the Pauli-Fierz Lagrangian a mass term with coefficients $c _ { \mathrm { l } }$ and $c _ { 2 }$ arbitrary, the resulting propagator in general has ghosts,i.e.poles with the “wrong”sign of the residue,corresponding to degrees of freedom with negative kinetic energy,which generates an instability of the vacuum.The only combination that does not introduces ghosts turns out to be $h _ { \mu \nu } h ^ { \mu \nu } - h ^ { 2 }$ ,which is called the Pauli-Fierz mass term.Then,in linearized theory we are led to consider,as the action describing massive gravitons,

$$
\begin{array} { r } { S _ { 2 } = \displaystyle \frac { 1 } { 2 } \int d ^ { 4 } x \left[ \begin{array} { l } { - \partial _ { \rho } h _ { \mu \nu } \partial ^ { \rho } h ^ { \mu \nu } + 2 \partial _ { \rho } h _ { \mu \nu } \partial ^ { \nu } h ^ { \mu \rho } - 2 \partial _ { \nu } h ^ { \mu \nu } \partial _ { \mu } h } \\ { \qquad } \end{array} \right. } \\ { \displaystyle \qquad + \partial ^ { \mu } h \partial _ { \mu } h + m _ { g } ^ { 2 } ( h ^ { 2 } - h _ { \mu \nu } h ^ { \mu \nu } ) + \tilde { \kappa } h _ { \mu \nu } T ^ { \mu \nu } ] . } \end{array}
$$

Before discussing the propagator obtained from this action,it is instructive to count the number of dynamical degrees of freedom of the theory, to see if they match with the five degrees of freedom of a massive spin-2 particle.We proceed in parallel to what we have done for a massive photon,and we write the equations of motions derived from the action (2.146),

$$
\begin{array} { l } { { \Theta h ^ { \mu \nu } - ( \partial ^ { \nu } \partial _ { \rho } h ^ { \mu \rho } + \partial ^ { \mu } \partial _ { \rho } h ^ { \nu \rho } ) + \eta ^ { \mu \nu } \partial _ { \rho } \partial _ { \sigma } h ^ { \rho \sigma } + \partial ^ { \mu } \partial ^ { \nu } h - \eta ^ { \mu \nu } \Pi h } } \\ { { \nonumber } } \\ { { = - \displaystyle \frac { \tilde { \kappa } } { 2 } T ^ { \mu \nu } + m _ { g } ^ { 2 } ( h ^ { \mu \nu } - \eta ^ { \mu \nu } h ) . \qquad ( 2 . 1 } } \end{array}
$$

Introducing on the left-hand side $\bar { h } _ { \mu \nu } \ : = \ : h _ { \mu \nu } \ : - \ : ( 1 / 2 ) \eta _ { \mu \nu } h$ ，we can also write this as

$$
\bar { \partial } \bar { h } ^ { \mu \nu } + \eta ^ { \mu \nu } \partial ^ { \rho } \partial ^ { \sigma } \bar { h } _ { \rho \sigma } - \partial _ { \rho } \partial ^ { \nu } \bar { h } ^ { \mu \rho } - \partial _ { \rho } \partial ^ { \mu } \bar { h } ^ { \nu \rho } = - \frac { \tilde { \kappa } } { 2 } T ^ { \mu \nu } + m _ { g } ^ { 2 } \big ( h ^ { \mu \nu } - \eta ^ { \mu \nu } h \big ) .
$$

In this form we immediately see that this equation reduces to eq. (1.17) formg $m _ { g } = 0$ .We can now apply $\partial _ { \mu }$ to both sides.The left-hand side gives zero identically,while on the right-hand side $\partial _ { \mu } T ^ { \mu \nu } = 0$ since we are working at linear order and then,as we saw in the previous section, $T ^ { \mu \nu }$ is an external conserved source. Then we get

$$
\overline { { { m _ { g } ^ { 2 } \partial _ { \mu } ( h ^ { \mu \nu } - \eta ^ { \mu \nu } h ) = 0 } } } ,
$$

which is analogous to eq. (2.131). Furthermore, taking the trace of both sides of eq. (2.147), we get

$$
2 \partial _ { \nu } \partial _ { \mu } ( h ^ { \mu \nu } - \eta ^ { \mu \nu } h ) = - \frac { \tilde { \kappa } } { 2 } T - 3 m _ { g } ^ { 2 } h .
$$

When $m _ { g } \neq 0$ ,the left-hand side vanishes because of eq. (2.149),and meget

<table><tr><td>h</td><td>R</td></tr><tr><td></td><td></td></tr></table>

In particular in the vacuum,where $T _ { \mu \nu } = 0$ ，eq.(2.151） gives $h = 0$ and then eq. (2.149) gives $\partial ^ { \mu } h _ { \mu \nu } = 0$ or,equivalently (since $h = 0$ ), $\partial ^ { \mu } { \bar { h } } _ { \mu \nu } = 0$ .So we have five conditions that reduce the i0 components of the symmetric matrix $h _ { \mu \nu }$ to thefive components expected for a massive spin-2 particle. The Pauli-Fierz mass term is actually the only combination for which there is no term proportional to $\sqcap h$ on the left-hand side of eq. (2.151).For all other choices,such a term does appear,so $h$ becomes a propagating degree of freedom,which furthermore turns out to be ghost-like.

# The limit $m _ { g } \to 0$

As soon as we switch on theinteraction,ie.anon-vanishing $T _ { \mu \nu }$ ,the limit $m _ { g }  0$ becomes quite peculiar. In fact,in the limit $m _ { g }  0$ for generic matter field with a non-vanishing trace of the energy-momentum tensor,eq.(2.151） gives $h  \infty$ rather than $h = 0$ as in the free theory.To understand the physical consequences of this result we observe that,inserting eqs.(2.149)and (2.151) (i.e. $\partial _ { \mu } h ^ { \mu \nu } = \partial ^ { \nu } h$ and $h = - \tilde { \kappa } T / ( 6 m _ { g } ^ { 2 } ) )$ into eq. (2.147) we get

$$
\begin{array} { c } { { ( \bigtriangledown - m _ { g } ^ { 2 } ) h _ { \mu \nu } = - \displaystyle \frac { \tilde { \kappa } } { 2 } \left( T _ { \mu \nu } - \frac { 1 } { 3 } \eta _ { \mu \nu } T + \frac { 1 } { 3 m _ { g } ^ { 2 } } \partial _ { \mu } \partial _ { \nu } T \right) } } \\ { { \equiv S _ { \mu \nu } . } } \end{array}
$$

Comparing with eq. (2.92),we see that in the limit $m _ { g }  0$ the left-hand side goes smoothly into the massless limit,but on the right-hand side there are two differences: the coefficient of $\eta ^ { \mu \nu } T$ is $- 1 / 3$ rather than $- 1 / 2$ ,and there is an apparently singular term $\sim ( 1 / m _ { g } ^ { 2 } ) \partial ^ { \mu } \partial ^ { \nu } T$ Both find their origin in the fact that,according to eq. (2.151)，m²h stays finite as $m _ { g }  0$

To see the effect produced by these differences，we can consider the effective matter-matter interaction,which is given by

$$
S _ { \mathrm { e f f } } = \frac { \tilde { \kappa } } { 2 } \int d ^ { 4 } x h _ { \mu \nu } ( x ) T ^ { \mu \nu } ( x ) ,
$$

where $h _ { \mu \nu } ( x )$ is the solution of eq. (2.152),

$$
h _ { \mu \nu } ( x ) = \int d ^ { 4 } x ^ { \prime } \Delta ( x - x ^ { \prime } ) S _ { \mu \nu } ( x ^ { \prime } ) ,
$$

and $\Delta ( x - x ^ { \prime } )$ is a Green's function of the massive Klein-Gordon equation,defined by

$$
\left( \Pi _ { x } - m _ { g } ^ { 2 } \right) \Delta ( x - x ^ { \prime } ) = \delta ^ { ( 4 ) } ( x - x ^ { \prime } ) .
$$

This gives

$$
S _ { \mathrm { e f f } } = \frac { \tilde { \kappa } } { 2 } \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \Delta ( x - x ^ { \prime } ) S _ { \mu \nu } ( x ^ { \prime } ) .
$$

Using the conservation of the energy-momentum tensor we can show that the singular term in $S _ { \mu \nu }$ drops from this expression. In fact,integrating twice by parts,

$$
\begin{array} { c } { { { \displaystyle \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \Delta ( x - \bar { x } ^ { \prime } ) \frac { \partial } { \partial x ^ { \prime } ^ { \mu } } \frac { \partial } { \partial x ^ { \prime } ^ { \nu } } T ( x ^ { \prime } ) } } } \\ { { { \displaystyle = - \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \left[ \frac { \partial } { \partial x ^ { \prime } ^ { \mu } } \Delta ( x - x ^ { \prime } ) \right] \frac { \partial } { \partial x ^ { \prime \nu } } T ( x ^ { \prime } ) } } } \\ { { { \displaystyle = + \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \left[ \frac { \partial } { \partial x ^ { \mu } } \Delta ( x - x ^ { \prime } ) \right] \frac { \partial } { \partial x ^ { \prime } } T ( x ^ { \prime } ) } } } \\ { { { \displaystyle = - \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } \left[ \frac { \partial } { \partial x ^ { \mu } } T ^ { \mu \nu } ( x ) \right] \Delta ( x - x ^ { \prime } ) \frac { \partial } { \partial x ^ { \prime \nu } } T ( x ^ { \prime } ) } } } \\ { { { \displaystyle = 0 . } } } \end{array}
$$

However,the fact that the coefficient of $\eta ^ { \mu \nu } T$ is $- 1 / 3$ rather than $- 1 / 2$ givesa genuine difference in the physical amplitude,

$$
\begin{array} { c } { { S _ { \mathrm { e f f } } = \displaystyle \frac { \tilde { \kappa } } { 2 } \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \Delta ( x - \overline { { { x ^ { \prime } } } } ) [ T _ { \mu \nu } ( x ^ { \prime } ) - \frac { 1 } { 3 } \eta _ { \mu \nu } T ( x ^ { \prime } ) ] } } \\ { { { } } } \\ { { = \displaystyle \frac { \tilde { \kappa } } { 2 } \int d ^ { 4 } x d ^ { 4 } x ^ { \prime } T ^ { \mu \nu } ( x ) \Delta _ { \mu \nu \rho \sigma } ( x - x ^ { \prime } ; m _ { g } ) T ^ { \rho \sigma } ( x ^ { \prime } ) \quad \quad ( } } \end{array}
$$

where

$$
\Delta _ { \mu \nu \rho \sigma } ( x - x ^ { \prime } ; m _ { g } ) = \Delta ( x - x ^ { \prime } ) \left[ \frac 1 2 ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } ) - \frac 1 3 \eta _ { \mu \nu } \eta _ { \rho \sigma } \right] .
$$

The same result,of course,could have been obtained directly inverting the quadratic part of the action to find the propagator,just as we did for the massless graviton and for the massive photons. Repeating steps analogous to those leading to eq. (2.142),we get

$$
\dot { \bar { \jmath } } _ { \mu \nu \rho \sigma } ( k ; m _ { g } ) = \left[ \frac { 1 } { 2 } ( \Pi _ { \mu \rho } \Pi _ { \nu \sigma } + \Pi _ { \mu \sigma } \Pi _ { \nu \rho } ) - \frac { 1 } { 3 } \Pi _ { \mu \nu } \Pi _ { \rho \sigma } \right] \left( \frac { - i } { k ^ { 2 } + m _ { g } ^ { 2 } - i \epsilon } \right) ,
$$

where

$$
\Pi _ { \mu \nu } \equiv \eta _ { \mu \nu } + \frac { k _ { \mu } k _ { \nu } } { m _ { g } ^ { 2 } } .
$$

Since the energy-momentum tensor is| conserved, $k _ { \mu } \tilde { T } ^ { \mu \nu } ( k ) = 0$ and, when contracted with $T ^ { \mu \nu } ( - k ) T ^ { \rho \sigma } ( k )$ ,the above propagator is equivalent to

$$
\bar { D } _ { \mu \nu \rho \sigma } ( k ; m _ { g } ) = [ \frac { 1 } { 2 } ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } ) ] - \frac { 1 } { 3 } \eta _ { \mu \nu } \eta _ { \rho \sigma } ] ( \frac { - i } { k ^ { 2 } + m _ { g } ^ { 2 } - i \epsilon } ) .
$$

Comparing eqs.(2.160) or (2.162) with the massless graviton propaator found in eq. (2.97) we see the following. The terms $k _ { \mu } k _ { \nu } / m _ { g } ^ { 2 }$ that are singular in the masslesslimit,give a vanishing contribution to the physical amplitudes,because hμv is coupled to a conserved energymomentum tensor.This is completely analogous to the situation for a massive photon, where the terms $k _ { \mu } k _ { \nu } / m _ { \gamma } ^ { 2 }$ disappeared because thei photon is coupled to a conserved current.However,there is diference in the numerical coefficient in front of $\eta _ { \mu \nu } \eta _ { \rho \sigma }$ and,unlikely the case of the photon, the propagator (2.162) does not reduces to the massless propagator as $m _ { g } \to 0$ Writing

$$
\displaystyle \frac { 1 } { 2 } \big ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } \big ) - \frac { 1 } { 3 } \eta _ { \mu \nu } \eta _ { \rho \sigma } = \frac { 1 } { 2 } \big ( \eta _ { \mu \rho } \eta _ { \nu \sigma } + \eta _ { \mu \sigma } \eta _ { \nu \rho } - \eta _ { \mu \nu } \eta _ { \rho \sigma } \big )
$$

we see that

$$
\begin{array} { l } { { \displaystyle \operatorname * { l i m } _ { m _ { g } \to 0 } T ^ { \mu \nu } ( - k ) \tilde { D } _ { \mu \nu \rho \sigma } ( k ; m _ { g } ) T ^ { \rho \sigma } ( k ) = T ^ { \mu \nu } ( - k ) \tilde { D } _ { \mu \nu \rho \sigma } ( k ) T ^ { \rho \sigma } ( k ) } } \\ { { { } } } \\ { { \displaystyle \qquad + \frac { 1 } { 6 } T ( - k ) \frac { - i } { k ^ { 2 } } T ( k ) , } } \end{array}
$$

where $\tilde { D } _ { \mu \nu \rho \sigma } ( k )$ is the propagator computed directly in the masless theory,eq. (2.97). The second term on the right-hand side corresponds to the exchange of a massess scalar particle, coupled to the trace of the energy-momentum tensor,and it is because of this additional term that the limit mg →O of the massive theory does not reproduce the result obtained in the massess theory. This is usually referred to as the van Dam-Veltman-Zakharov (vDVZ) discontinuity.28

Having identified the problem in the existence of an unexpected scalar degree of freedom,we can now understand what happened.Recall that a massive spin- $j$ particles has $2 { \dot { \jmath } } + 1$ degrees of freedom, while a massless particle with quantum number $j$ has only two degrees of freedom if $j > 0$ (and if we demand that it is also a representation of parity,beside of Poincaré transformations),and one degree of freedom if j= O.For a massive photon, we saw that the three degrees of freedom,in the massless limit,decompose into the two transverse degrees of freedom of a massless photon,which have helicities $\pm \sharp$ ,plus the longitudinal component. The latter,in the limit my →O,becomes a scalar particle and decouples, since its coupling becomes proportional to $\partial _ { \mu } j ^ { \mu }$ ，which vanishes. The fact that the coupling is to $\partial _ { \mu } j ^ { \underline { { \mu } } }$ is dictated by the fact that this is the only scalar that we can make with jμ and with derivatives,which is linear in the current. The decoupling of the spurious scalar mode is therefore ensured by current conservation.

Similarly,in the limit $m _ { g }  0$ ，the five degrees of freedom of the massive gravition decompose into two states with helicities $\pm 2$ ，which make up a massles graviton, two states with helicities $\pm 1$ ,often termed the graviphoton,and a scalar,called the graviscalar. The graviphoton, being a vector,must be coupled to a four-vector made with $T _ { \mu \nu }$ and possibly with derivatives,and linear in $T _ { \mu \nu }$ ．The only possibility is $\partial _ { \mu } T ^ { \mu \nu }$ .However,this quantity vanishes and therefore the graviphoton decouples.The graviscalar,on the other hand,can couple to the trace of the energy-momentum tensor.This is in general non-zero,and therefore the graviscalar does not decouple. It is,in fact,responsible for the additional term in eq.(2.164) and therefqre for the vDVZ discontinuity.

We can now compare some predictions of the massless and massive theory. Consider first the Newtonian potential in the non-relativistic limit.We found in eq. (2.98) that

$$
V ( { \bf x } ) = - i \frac { \kappa ^ { 2 } } { 4 } m _ { 1 } m _ { 2 } D _ { 0 0 0 0 } ( { \bf x } ) .
$$

In the massless theory, using eq. (2.97), we saw that

$$
\tilde { D } _ { 0 0 0 0 } ( k ) = { \frac { 1 } { 2 } } { \frac { - i } { k ^ { 2 } } } .
$$

This gives $D _ { 0 0 0 0 } ( r ) = - i / ( 8 \pi r )$ s0

$$
V ( { \bf x } ) = - \frac { \kappa ^ { 2 } } { 3 2 \pi } \frac { m _ { 1 } m _ { 2 } } { r } ,
$$

and we recovered the Newtonian potential setting $\kappa ^ { 2 } = 3 2 \pi G$ In the massive theory,instead,we see from eq.(2.162) that

$$
\tilde { D } _ { 0 0 0 0 } ( k ) = \frac { 2 } { 3 } \frac { - i } { k ^ { 2 } + m _ { g } ^ { 2 } } ,
$$

and we get

$$
V ( { \bf x } ) = - { \frac { 4 } { 3 } } \left( { \frac { \tilde { \kappa } ^ { 2 } } { 3 2 \pi } } \right) { \frac { m _ { 1 } m _ { 2 } } { r } } \exp \{ - m _ { g } r \} .
$$

Tle Yukawa potential was of course expected because a massive particle mediates a short-range force. The result however differs also by an overall factor $4 / 3$ from the massless result,and the difference is due to theadditional attractive contribution of the graviscalar.

As far as the Newtonian limit is concerned,one can simply reabsorb Ihis difference setting,in the massive theory,

$$
{ \frac { 4 } { 3 } } \left( \frac { \tilde { \kappa } ^ { 2 } } { 3 2 \pi } \right) = G .
$$

Thus,at $m _ { g } r \ll 1$ ，the correct Newtonian potential is obtained,at the price that the coupling $\tilde { \kappa } ^ { 2 }$ of the massive theory is smaller than the coupling $\kappa ^ { 2 }$ of the massless theory by a factor $3 / 4$ .The problem however comes when we consider the predictions of the massive theory Ithe relativistic regime,in particular when we compute the deflection oflight bya massive object.In the massless theory, the deflection angle f light skimming the surface of the Sun (and first detected,during a total eclipse,by Eddington in 1919),is

$$
\Delta \theta = \frac { 4 G M _ { \odot } } { R _ { \odot } } ,
$$

where $M _ { \odot }$ and $R _ { \odot }$ are the massand radius of the Sun. Since the energy momentum tensor of the electiomagnetic field is traceless,when we re peat the computation in the massve theory,the additional term proportional to $T ( - k ) \left( - i / k ^ { 2 } \right) { \cal T } ( k )$ in eq. (2.164) vanishes. This means that the result for the deflection of light in the massive theory,in the limit $m _ { g }  0$ ,is the same as in the massless theory except that,instead of $\kappa ^ { 2 }$ we have $\tilde { \kappa } ^ { 2 }$ Since ${ \tilde { \kappa } } ^ { 2 } = ( 3 / 4 ) \kappa ^ { 2 }$ ,the prediction for light bending in the limit $m _ { g }  0$ of the massive theory is smaller by a factor $3 / 4$ than the: prediction of the massless theory, i.e.is $\Delta \theta = 3 G M _ { \odot } / R _ { \odot }$ Nowadays the experimental precision on the measurement of the bending of light by the Sun is better than one part in $1 0 ^ { 4 }$ ,and confirms the prediction of the massess theory. Apparently,one then arrives at the amazing conclusion that the mass of the graviton must be eractly zero.

A loophole in the above argjment was found by Vainshtein,considering the validity of the linearized approximation in the massve theory. To study the expansion in $h _ { \mu \nu }$ systematically, we should start from the full Einstein action plus the Pauli-Fierz mass term,

$$
S = \frac { 1 } { 1 6 \pi G } \int d ^ { 4 } x \sqrt { - g } \left[ R + \frac { 1 } { 4 } m _ { g } ^ { 2 } \left( h ^ { 2 } - h _ { \mu \nu } h ^ { \mu \nu } + O ( h _ { \mu \nu } ^ { 3 } ) \right) \right] ,
$$

We then expand $g _ { \mu \nu } = \bar { g } _ { \mu \nu } + \stackrel { . } { h } _ { \mu \nu }$ where ${ \bar { g } } _ { \mu \nu }$ is the appropriate background metric and, to have the canonical normalization for $h _ { \mu \nu }$ ，we finally rescale $h _ { \mu \nu }  ( 3 2 \pi G ) ^ { 1 / 2 } h _ { \mu \nu } = \kappa h _ { \mu \nu }$ .Bosonic matter felds,as usual,are coupled replacing in the matter action all ordinary derivative with covariant derivatives.Actually,one can use any form for the mass term that,in the linearized limit,reduces to the Pauli-Fierz mass term (in particular,we can decide to raise and lower the indices in the mass term with $\eta _ { \mu \nu }$ or with $g _ { \mu \nu }$ . The difference shows up only at cubic and higher-order terms,that are not fixed anyway),so we also included the possibility of non-linear corrections to the Pauli-Fierz mass term.

29We follow here the treatment of Deffayet,Dvali,Gabadadze and Vainshtein (2002),to whom we refer for more details.

To compute the gravitational scattering by a fixed heavy mass $M$ ,we expand around a metric $\bar { g } _ { \mu \nu }$ which is a generalization of the Schwarzschild metric generated by the heavy mass $M$ ，so it is computed from the action (2.172), which includes the graviton mass. Naively one would expect that,if $m _ { g }  0$ ,this metric goes smoothly into the usual Schwarzschild metric computed in standard general relativity,with massless graviton,for all values of $r$ 、However,the explicit computation shows that this is not true.Wecan search for the metric generated by an heavy mass in the theory (2.172),writing29

$$
d s ^ { 2 } = - e ^ { \nu ( \rho ) } d t ^ { 2 } + e ^ { \sigma ( \rho ) } d \rho ^ { 2 } \big | + e ^ { \mu ( \rho ) } \rho ^ { 2 } ( \delta \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

When the graviton is massless,the function $\mu ( \rho )$ can be set to zero using coordinate invariance.In the theory (2.172),however,the reparametrization invariance is broken,and $\mu ( \rho )$ must be kept.One then performs the substitutions

$$
r \equiv \rho e ^ { \mu / 2 } , \ : \ : \ : \ : e ^ { \lambda } \equiv \left( 1 + \frac { \rho } { 2 } \frac { d \mu } { d \rho } \right) ^ { - 2 } e ^ { \sigma - \mu } . \nonumber
$$

The standard Schwarzschild solution of the massless theory corresponds to

$$
\begin{array} { l } { \displaystyle \nu ( \boldsymbol { r } ) = - \lambda ( \boldsymbol { r } ) = \log \left( \mathrm { \ddot { f } } - \frac { R _ { S } } { r } \right) } \\ { = - \frac { R _ { S } } { r } - \frac { 1 } { 2 } \left( \frac { R _ { S } } { r } \right) ^ { 2 } + \dots , } \\ { \displaystyle \mu ( \boldsymbol { r } ) = 0 . } \end{array}
$$

In the theory with massive graviton one rather finds,up to next-toleading order in $G$ (therefore in $R _ { S }$ ），

$$
\begin{array} { l } { { \nu ( r ) = - \displaystyle \frac { R _ { S } } { r } \left[ 1 + { \cal O } \left( \frac { R _ { S } } { m _ { g } ^ { 4 } r ^ { 5 } } \right) + \ldots \right] \ : , } } \\ { { \lambda ( r ) = \displaystyle \frac { 1 } { 2 } \ : \frac { R _ { S } } { r } \left[ 1 + { \cal O } \left( \frac { R _ { S } } { m _ { g } ^ { 4 } r ^ { 5 } } \right) + \ldots \right] \ : , } } \\ { { \mu ( r ) = - \displaystyle \frac { 1 } { 2 } \ : \frac { R _ { S } } { m _ { g } ^ { 2 } r ^ { 3 } } \left[ 1 + { \cal O } \left( \displaystyle \frac { R _ { S } } { m _ { g } ^ { 4 } r ^ { 5 } } \right) + \ldots \right] \ : . } } \end{array}
$$

If we limit ourselves to leading order,we observe that $\lambda ( r )$ is smaller by a factor $1 / 2$ compared to the result in the massless theory. This is the origin of the vDVZ discontinuity.However, the surprise comes looking at the corrections,since they blow up if $m _ { g } \  \ 0 !$ In other words,in the massive theory the linearized expansion becomes invalid if we send $m _ { g }  0$ at fixed $r$ .This does not mean that linearized theory is completely useless:if we define the Vainshtein radius $R _ { V }$ ，

$$
R _ { V } = \left( R _ { S } \lambda _ { g } ^ { 4 } \right) ^ { 1 / 5 } ,
$$

where $\lambda _ { g } ~ = ~ 1 / m _ { g }$ ，we see that the corrections are proportional to $\{ R _ { V } / r \} ^ { 5 }$ Therefore linearized theory is valid at $r \gg R _ { V }$ .We take $\lambda _ { g } > 2 0 0 ~ \mathrm { k p c }$ ,inagreement with eq.(2125) (with $h _ { 0 } \simeq 0 . 7$ )，and we consider the scattering of light from the Sun,which has $R _ { S } \sim 3 ~ \mathrm { k m }$ Then we get $R _ { V } ~ > ~ 4 0$ pc,i.e. $R _ { V }$ is at least $1 0 ^ { 7 }$ times larger than the Earth-Sun distance. Therefore,theNewtonian potential found in eq. (2.169),and the result for the light deflection in the massive theory discussed below eq.(2.169),are simply not applicable at the solar system scale.

On the other hand, in the opposite limit $r \ll R _ { V }$ ,it is possible to lind a consistent expansion of the Schwarzschild solution in powers of mg that,to lowest order,reproduces the Schwarzschild solution of the massless theory, of the form30

$$
\begin{array} { l } { \displaystyle \nu ( \boldsymbol { r } ) = - \frac { R _ { S } } { r } + O \left( m _ { g } ^ { 2 } \sqrt { R _ { S } r ^ { 3 } } \right) , } \\ { \lambda ( \boldsymbol { r } ) = + \frac { R _ { S } } { r } + O \left( m _ { g } ^ { 2 } \sqrt { R _ { S } r ^ { 3 } } \right) , } \\ { \mu ( \boldsymbol { r } ) = \sqrt { \frac { 8 R _ { S } } { 1 3 r } } + O ( m _ { g } ^ { 2 } r ^ { 2 } ) . } \end{array}
$$

30The existence of such a solution depends on the specific form of the nonlinear corrections to the Pauli-Fierz mass term,see Damour,Kogan and $\mathrm { P a } \mathrm { - }$ pazoglou (2003).

31For example, consider the function $f ( \epsilon , x ) ~ = ~ e ^ { - \epsilon / x }$ If we expand it in powers of $\epsilon$ at fixed $_ x$ we get $\textstyle f ( \epsilon , x ) =$ $1 - ( \epsilon / x ) + ( 1 / 2 ) ( \epsilon / x ) ^ { 2 } + . . . .$ Of course, this expansion is not suitable for studying the limit $x  0$ ，since the various terms are more and more singular.However,if one knows the full resummed expression $e ^ { - \epsilon / x }$ ，one realizes that,for $\epsilon > 0$ ,the limit $x \to 0 ^ { + }$ exists, and is in this case zero.In our case the role of $\epsilon$ is played by $R _ { S }$ and the role of $_ x$ by $m _ { g }$

Therefore,at $r \ll R _ { V }$ ， therelis no mass discontinuity. To prove that there is no mass discontinuity altogether, one should be able to resum the whole perturbative expansion (2.177-2.179), which is valid at $r \gg R _ { V }$ , and it is in principle possible that,in the resummed expression, there is no singularity as $m _ { g }  0 . ^ { 3 1 }$ If one can show that such a resummed solution,as we approach $r \sim R _ { V }$ ,matches smoothly the solution (2.181)- (2.183),which is valid at $r \ll \left| R _ { V } \right|$ ，we have constructed a solution with a smooth limit $m _ { g } \ \to \ 0$ ，valid for all $r$ .Observe also that, since the linearized theory does not apply at the solar system scale, there is no need to require $\tilde { \kappa } ^ { 2 } = ( 3 / 4 ) \kappa ^ { 2 }$ .On the contrary, since at $r \ll R _ { V }$ the expansion in $m _ { g }$ reproduces smoothly the massless limit，we must choose $\tilde { \kappa } = \kappa$ ，and all the results of the massive theory， from the Newtonian potential to the light deflection,go smoothly into those of the massless theory. At $r \gg R _ { V }$ , instead, where linearized theory can be trusted, we get a gravitational potential

$$
V ( r ) = - \frac { 4 } { 3 } \frac { \vert G m _ { 1 } m _ { 2 } } { r } \exp \{ - m _ { g } r \} ,
$$

since we have fixed $\tilde { \kappa } \ : = \ : \kappa$ .In conclusion, in this scenario, inside the Vainsthein radius a tiny graviton mass has negligible effects, while at $r \gg R _ { V }$ the graviscalar becomes effective,and gives a further attractive contribution to the gravitational potential.

To prove that this what actually happens requires to show that the solutions found in the regimes $r \ll R _ { V }$ and $r \gg R _ { V }$ do match. This is a non-trivial problem,because the solution (2.181)-(2.183) is obtained from an expansion in $m _ { g }$ while the solution (2.177)-(2.179) is non-analytic in $m _ { g }$ , since we have seen that it diverges as $m _ { g }  0$ Conversely, the solution (2.177)-(2.179) is obtained performing an expansion in $G$ ，while the solution $( 2 . 1 8 1 ) \ – ( 2 . 1 8 3 )$ is non-analytic in $G$ since $\mu ( r ) \sim \sqrt { R _ { S } } \sim \sqrt { G }$ .Put it differently,the difficulty of the problem is that,as we approach $R _ { V }$ from the large distance region, the graviscalar becomes strongly coupled,and perturbation theory breaks down.

Numerical studies of the inward continuation of asymptotically fat solutions indicate that,for small $m _ { g }$ , they end up in a singularity at finite radius,rather then matching a continuous solution inside the Vainshtein radius. It is possible however that the matching takes place not for asymptotically fat solution but for asymptotically De Sitter solution. This would be physically acceptable, given the experimental evidence for a cosmological constant,and also because for $m _ { g }$ sufficiently small the value of $R _ { V }$ can be larger than the Hubble radius,in which case the form of the solution at $r \gg R _ { V }$ is not physically relevant.

A further complication is that,in curved space, the trace degre of freedom $h$ ,which in linearized theory is eliminated through eq. (2.151). becomes dynamical again, so we have six degrees of freedom rather than five,and furthermore it is a ghost.In fact,in the theory with action (2.172),i.e. full Einstein gravity supplemented by a mass term,the linearized equation of motion (2.i47) is replaced by

$$
G _ { \mu \nu } = \frac { \tilde { \kappa } } { 4 } T _ { \mu \nu } - \frac { 1 } { 2 } m _ { g } ^ { 2 } [ d h _ { \mu \nu } + b h \eta _ { \mu \nu } + { \cal O } ( h _ { \mu \nu } ^ { 2 } ) ] ,
$$

where $G _ { \mu \nu }$ is the full Einstein tensor,rather than its linearization that appears in eq.(2.147),and we also allowed for a generic mass term, including higher-order corrections (the Pauli-Fierz mass term corresponds to $a = - b = 1$ ).Using the Bianchi identity $D ^ { \mu } G _ { \mu \nu } = 0$ as well as the covariant conservation of the energy-momentum tensor,we get the four conditions

$$
m _ { g } ^ { 2 } D ^ { \mu } [ a h _ { \mu \nu } + b h \eta _ { \mu \nu } + Q ( h _ { \mu \nu } ^ { 2 } ) ] = 0 ,
$$

which replace their linearized version $( 2 . 1 4 9 )$ and again allow us to eliminate four degrees of freedom.The elimination of these degrees of freedom is therefore a consequence of the Bianchi identity, or,equivalently,of the invariance of the Einstein--Hilbert action under diffeomorfisms.On the other hand, the elimination of $h$ in linearized theory,eq. (2.151),is not ensured by any symmetry,but is a consequence of the fine-tuning in the mass term that leads to the Pauli-Fierz combination.Then,this constraint does not survive in curved space,and $h$ becomes dynamical again and it can be shown to be ghost-like,see the Further Reading section for discussions.

Thus,presently the issue of the consistehcy of a field theory of massive gravitons is not settled.If,in some form,a continuous solution indeed exists,then the limit $m _ { g }  0$ is smoothl and it make sense to deform Einstein gravity by adding a small mass term for the graviton,with a value bounded experimentally by (2.126).Otherwise,one should accept the (rather odd) conclusion that the graviton mass must be identically zero.We finally observe that it is possibleto add mass terms that break Lorentz invariance (which indeed emerge quite naturally if one breaks spontaneously the diffeomorfism invariance of general relativity),and in this case there are neither ghosts nor the vDVZ discontinuity. Again, we refer the reader to the Further Reading section.

# 2.4Solved problems

# Problem 2.1. The helicity of gravitons

We have seen that,for a given propagation direction ,a GW is described by $\phantom { - } 1 2 \times 2$ matrix in the plane orthogonal to $\hat { \bf n }$ ，with matrix elements given in terms of the amplitudes $h _ { + }$ and $h _ { \times }$ of the two polarization. The Lorentz transformations that leave invariant the propagation direction $\hat { \bf n }$ are the rotations around the $\hat { \bf n }$ axis and the boosts in the $\hat { \bf n }$ direction.Under these operations $1 4$ and $h _ { \times }$ will therefore transform between themselves.In this problem,we compute explicitly the transformation of $h _ { + } |$ and $h _ { \times }$ under rotations around then axis and under boosts in the $\hat { \bf n }$ directiqn.

In general, under a Lorentz transformatidn $x ^ { \mu }  x ^ { \prime \mu } = \Lambda ^ { \mu } { } _ { \nu } x ^ { \nu }$ ，a tensor $h _ { \mu \nu }$ transforms as

$$
h _ { \mu \nu } ( x )  h _ { \mu \nu } ^ { \prime } ( x ^ { \prime } ) = \Lambda _ { \mu } { } ^ { \rho } \Lambda _ { \nu } { } ^ { \sigma } h _ { \rho \sigma } ( x ) .
$$

Choosing $\hat { \bf n } = \hat { \bf z }$ ,a rotation around the $z$ axis and a boost along $z$ are written

respectively as

$$
\Lambda = \left( \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { \left\lfloor \begin{array} { c c c } { { 0 } } & { { 0 } } \\ { { 0 } } & { { \cos \psi } } & { { - \sin \psi } } & { { 0 } } \\ { { 0 } } & { { \sin \psi } } & { { \cos \psi } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right. } } & { { \pmod { 1 } } } \end{array} \right)
$$

and

$$
\Lambda = \left( \begin{array} { c c c } { { \cosh \eta } } & { { 0 } } & { { - \sinh \eta } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \\ { { - \sinh \eta } } & { { 0 } } & { { \cosh \eta } } \end{array} \right) \qquad ( \mathrm { b o o s t } )
$$

where $\Lambda$ denote the matrix whole elements are ${ \Lambda _ { \mu } } ^ { \nu }$ ； $\psi$ is the rotation angle and $\eta$ is related to the velocity $v$ of the boost by $v = \operatorname { t a n h } \eta$ Writing eq. (2.187) in the TT gauge we have

where

$$
\begin{array} { r } { \big ( h _ { a b } ^ { \mathrm { T T } } \big ) ^ { \prime } ( x ^ { \prime } ) = ( \begin{array} { l l } { h _ { + } ^ { \prime } } & { h _ { \times } ^ { \prime } } \\ { h _ { \times } ^ { \prime } } & { - h _ { + } ^ { \prime } } \end{array} ) _ { a b } e ^ { i k x } , } \\ { ( \begin{array} { l l } { h _ { + } ^ { \prime } } & { h _ { \times } ^ { \prime } } \\ { h _ { \times } ^ { \prime } } & { - h _ { + } ^ { \prime } } \end{array} ) _ { a b } \overset {  } { = } \big ( \Lambda _ { a } ^ { \textit { c } } \Lambda _ { b } ^ { \textit { d } } ( \begin{array} { l l } { h _ { + } } & { h _ { \times } } \\ { h _ { \times } } & { - h _ { + } } \end{array} ) _ { c d } \big ) _ { c b } } \end{array}
$$

and $a , b$ take the value 1,2. Since $k x = k ^ { \prime } x ^ { \prime }$ ,where $k ^ { \prime }$ is the four-momentum in the new frame,we can also rewrite eq.(2.190) as

$$
( h _ { a b } ^ { \mathrm { T T } } ) ^ { \prime } ( x ^ { \prime } ) = \left( \begin{array} { c c } { { h _ { + } ^ { \prime } } } & { { h _ { \times } ^ { \prime } } } \\ { { h _ { \times } ^ { \prime } } } & { { - h _ { + } ^ { \prime } } } \end{array} \right) _ { a b } e ^ { i k ^ { \prime } x ^ { \prime } }
$$

or, since $x ^ { \prime }$ is generic,

$$
( h _ { a b } ^ { \mathrm { T T } } ) ^ { \prime } ( x ) = \left( \begin{array} { c c } { { h _ { + } ^ { \prime } } } & { { h _ { \times } ^ { \prime } } } \\ { { h _ { \times } ^ { \prime } } } & { { - h _ { + } ^ { \prime } } } \end{array} \right) _ { a b } e ^ { i k ^ { \prime } x } .
$$

Using eq. (2.191),with ${ \Lambda _ { a } } ^ { \mathrm { ~ c ~ } }$ givenl by the $2 \times 2$ submatrix made by the second and third rows and columns of eq.(2.188),and performing the matrix multiplication, we get

<table><tr><td></td><td>h&#x27;+=h+cos2-hx sin2， h&#x27;=h+sin 2+hx cos 2.</td></tr></table>

Under boosts,the matrix ${ \Lambda _ { a } } ^ { c }$ (i.e.the $2 \times 2$ submatrix made by the second and third rows and columns of eq.(2.189)) is just the $2 \times 2$ identity matrix, so $h _ { + } ^ { \prime } = h _ { + }$ and $h _ { \times } = h _ { \times } ^ { \prime }$ .ThelGW amplitudes $h _ { + }$ and $h _ { \times }$ are therefore invariant under boosts.

From eq.(2.194) we see that,under rotations around the $z$ axis, the combinations $h _ { \times } \pm i h _ { + }$ transform as

$$
( h _ { \times } \pm i h _ { + } ) \Bigl |  e ^ { \mp 2 i \psi } ( h _ { \times } \pm i h _ { + } ) . \Bigr |
$$

To understand the meaning of this transformation law,we recall some basic results from the theory of representations of the Poincaré group (see,e.g. Maggiore 2OO5,Chapter 2).The Poincaré group has two types of physically interesting representations:

massive representation,which are labeled by the mass m,with-PμPμ = $m ^ { 2 } > 0$ (where $P ^ { \mu }$ is the four-momentum)and by the spin $j$ ,which (in units of $\hbar$ )can take integer or half-integer values, $j = 0 , 1 / 2 , 1 , \ldots$ The representation with spin j has dimension 2j+1.Physically,this follows from the fact that for a massive particle exists the rest frame,and in the rest frame the component along the $z$ axis of the spin, fora particle with spin $j$ ,can take the $2 j + 1$ possible values $j _ { z } = - j , - j + 1 , \dots , j$ So,in particular,a massive spin-1 particle has three degrees of freedom and a massive spin-2 particle has five degrees of freedom.

massless representation,which are characterized by $P _ { \mu } P ^ { \mu } = 0$ and by a quantum number j,which again can be integer or half-integer.For massless particles the rest frame does hot exist and the previous argument about the existence of 2j+1 states does not go through.Rather, these representations are one-dimensional,and are characterized by a definite value of the helicity,which is defined as the projection of the total angular momentum on the direction of motion, 32

$$
h = \mathbf { J } { \cdot } { \hat { \mathbf { n } } } .
$$

The total angular momentum is the sum of orbital and spin angular momenta,J=L+S.Of course L·n= (x×p)·n=0 since p= |pln, and therefore the helicity is equal to the projection of the spin on the direction of motion, $h = \mathbf { S } { \cdot } \hat { \mathbf { n } }$

Under a rotation by an angle $\psi$ around the direction of motion a helicity eigenstate $| h \rangle$ transforms as

$$
| h \rangle  e ^ { i h \psi } | h \rangle .
$$

Massless representations can have either $h = + j$ or $h = - j$ Each of these possibilities,separately,provides a one-dimensional representation of the Poincaré group: the states with $h = \pm j$ do not mix between them under (proper） spatial rotations,boosts nor translations.However,under a parity transformation  changes sign,while the angular momentum is a pseudovector and is unchanged.Therefore the helicity isa pseudoscalar,i.e.it changes sign under parity，h →-h.For this reason,ina theory which conserves parity (like gravity or electromagnetism）it is more convenient to define particles as representations of the Poincaré group and of parity,thatis,to assemble the two Poincaré representations with h=±j and to consider them as two polarization states of the same particle. The photon is then defined asa massless particle with two helicity states h=±1,while the graviton is defined as a massless particle with two helicity states h = ±2. On the contrary,since weak interactions violate parity,in the limit in which the neutrinos can be taken as massless (there is nowadays evidence for a small neutrino mass from oscillation experiments),we reserve the name neutrino to the one-dimensional massless Poincaré representation with $h = - 1 / 2$ ，while the antineutrino is defined as the representation with $h = + 1 / 2$ .33

In the light of these results,we see that eq.(2.195),together with the fact that $h _ { i j } ^ { \mathrm { T T } }$ Tsatisfies the massless Klein-Gordon equation QhTT = 0, means that the quanta of the gravitational field are massless particles,and the combinations hx干ih+are the helicity eigenstatesand have helicities±2,respectively.

32The symbol $h$ is traditionally use for the helicity,and of course it should not be confused with the GW amplitudes $h _ { + }$ and $h _ { \times }$

33The fact that,foreach massless representation with a given helicity, there isa corresponding representation with the opposite helicity is a consequence of the CPT symmetry,which is present in any Lorentz-invariant quantum feld theory with a hermitian Hamiltonian.

![](images/03c0196be907337b518d9835a7f27dd6ebb1da43deff5cbd363804b2609b0cdf.jpg)

# Problem 2.2. Angular momentum and parity of graviton states

In this problem we examine the possible angular momentum states of the graviton. Let us first recall how such an analysis works for the photon,fol lowing Landau and Lifshitz，Vol.IV(1982)，Section 6． After choosing the radiation gauge $A _ { 0 } ~ = ~ 0$ and $\mathbf { v \cdot A } = \mathrm { ~ 0 ~ }$ ，a photon is described by a vector $\mathbf { A } ( \mathbf { x } )$ or,in momentum space,by $\tilde { \mathbf { A } } ( \mathbf { k } )$ , subject to the transversality condition $\mathbf { k } \cdot { \tilde { \mathbf { A } } } ( \mathbf { k } ) = 0$ Let us at first neglect the transversality condition.The vector character of $\tilde { \mathbf { A } } ( \mathbf { k } )$ then corresponds to spin $s = 1$ ,and the total angular momentum $j$ of a photon is given by the combination of $s = 1$ and of the orbital angular momentum $\boldsymbol { l }$ ，with the usual composition rule of angular momenta in quantum mechanics.This means that a state with $j = 0$ can be obtained in only one possible way,li.e. combining the spin $s = 1$ with $\begin{array} { r } { l = 1 } \end{array}$ while there are three states for $\mathrm { e a c h } | \ r _ { j } \neq 0$ ,which are obtained with $l = j , j \pm 1$ (for the purpose of this counting we consider a state with momentum $j$ as one single state,regardless of the $2 j + 1$ possible components of $j _ { z }$ ）

To understand what is the paritly of these states it is convenient to write explicitly their wavefunction. Just as the angular dependence of a scalar function can be expanded in terms of the (scalar） spherical harmonics $Y _ { l m } ( \theta , \phi )$ , the angular dependence of a vector function $\mathbf { A } ( \mathbf { x } )$ can be expressed in vector spherical harmonics.As we will discuss in more detail in Section 3.5.2,see in particular eq.(3.247),these can be written as

$$
{ \bf Y } _ { j j _ { z } } ^ { l } ( \theta , \phi ) = \sum _ { l _ { z } = - l } ^ { l } \sum _ { s _ { z } = 0 , \pm 1 } \sqrt { 1 l s _ { z } l _ { z } \vert j j _ { z } \rangle Y _ { l l _ { z } } ( \theta , \phi ) } \xi ^ { ( s _ { z } ) } .
$$

where $\pmb { \xi } ^ { ( s _ { z } ) }$ is the wavefunction of a spin-1 particle with a given value $s _ { z }$ of the projection of the spin on the $z$ axis,and $\langle 1 l s _ { z } l _ { z } | j j _ { z } \rangle$ are the Clebsch-Gordan coefficient necessary to combine a spin state $\left| s s _ { z } \right.$ with $s = 1$ and an orbital angular momentum state $| l l _ { z } \rangle$ ,so to obtain a total angular momentum $| j j _ { z } \rangle$ In terms of the unit vectors $\mathbf { e } _ { x } , \mathbf { e } _ { y }$ and $\mathbf { e } _ { z }$ of a Cartesian reference frame, the explicit form of the spin wavefunction is

$$
{ \pmb \xi } ^ { ( \pm 1 ) } = \mp \frac { 1 } { \sqrt { 2 } } \left( { \bf e } _ { \pm } \pm i { \bf e } _ { y } \right) , ~ { \pmb \xi } ^ { ( 0 ) } = { \bf e } _ { z } .
$$

34In general, we can define parity either changing the sign of vectors with respect to a fixed reference frame,or reversing the orientation of the axes of the reference frame while keeping the vectors fixed.Here we adopt the latter point of view.

Consider a parity transformation,defined so that it changes the sign of the orientation of the axes of the reference frame, $\mathbf { e } _ { i } \longrightarrow - \mathbf { e } _ { i }$ .34 Under this transformation,the state (2.198) picks a factor $P = ( - 1 ) ^ { l + 1 }$ ，where the $( - 1 ) ^ { l }$ comes from the transformation of the scalar spherical harmonics and the further minus sign comes from the spin wavefunction. Thus,we can summarize as follows the possible states before imposing the condition $\mathbf { k } \mathbf { \cdot } \tilde { \mathbf { A } } ( \mathbf { k } ) = 0$

$$
\begin{array} { l } { { j = 0 : \quad \mathrm { o n e ~ s t a t e } , \quad \quad ( l = 1 , \stackrel {  } {  } + ) , } } \\ { { j = 1 : \quad \mathrm { t h r e e ~ s t a t e s } , \quad ( l = 0 , \stackrel {  } {  } - ) , ( l = 1 , P = + ) , ( l = 2 , P = - ) , } } \\ { { j = 2 : \quad \mathrm { t h r e e ~ s t a t e s } , \quad ( l = 1 , P = + ) , ( l = 2 , P = - ) , ( l = 3 , P = + ) , } } \end{array}
$$

and similarly we have three states for all higher values of $j$ We now impose the transversality condition $\mathbf { k } \cdot \tilde { \mathbf { A } } ( \mathbf { k } ) \big | = 0$ This means that we remove a longitudinal state of the form $\tilde { \mathbf { A } } ( \mathbf { k } ) = \phi ( \mathbf { k } ) \mathbf { k }$ . The number of states of this form is therefore the same as the number of states of a scalar particles with wavefunction $\phi ( \mathbf { k } )$ (or,equivalently,of the scalar degree of freedom described by $\mathbf { v \cdot A } )$ . When we develop $\phi$ in spherical harmonics,the total angular momentum $j$ of such a state is equal to the order $l$ of the spherical harmonic,and its parity is $P = ( - 1 ) ^ { j }$ .Thus,at each level $j$ we must remove from eq.(2.200） one spurious state, with $P = ( - 1 ) ^ { j }$ ．Therefore at level $j = 0$ we end up with no physical states,while at all higher levels we end up with two physical states of opposite parity. This shows that for the photon there can be no monopole radiation,because there is no physical photon state with $j = 0$ ，while for all other values of $j$ we have two physical states.For instance,the states with $j = 1$ correspond to an electric dipole photoh $P = -$ andamagnetic dipole photon $( P = +$

Having understood the argument for the photon,we can adapt it to the graviton．The graviton is described by a ${ \dot { 2 } } \times 2$ traceless symmetric tensor $\hat { h } _ { i j } ( \mathbf { k } )$ subject to the transversality condition $k ^ { i } \tilde { h } _ { i j } ( \mathbf { k } ) = 0$ ，Again,we neglect at frst the transversality condition.A symmetric traceless tensor corresponds to spin $s = 2$ ,while the parity on a true tensor is $P = ( - 1 ) ^ { l }$ .Then,combining the orbital angular momentum with the spin $s = 2$ ，we have the following states

$$
\begin{array} { r l r } { j = 0 : } & { \mathrm { o n e ~ s t a t e , } } & { \left( l = 2 , P = + \right) } \\ { j = 1 : } & { \mathrm { t h r e e ~ s t a t e s , } } & { \left( l = 1 , P = - \right) , \left( l = 2 , P = + \right) , \left( l = 3 , P = - \right) } \\ { j = 2 : } & { \mathrm { f i v e ~ s t a t e s , } } & { \left( l = 0 , P = + \right) , \left( l = 1 , P = - \right) , \left( l = 2 , P = + \right) , } \\ & { } & { \left( l = 3 , P = - \right) , \left( l = 4 , P = + \right) . } \end{array}
$$

Similarly forall higher $j$ there are five states,two with $P = +$ ，twowith $P = -$ and one more with $P = ( - 1 ) ^ { j }$ ．We now impose the transversality condition. The most general traceless symmetric tensor which does not satisfy the transversality condition has the form

$$
\tilde { h } _ { i j } ( { \bf k } ) = a _ { i } ( { \bf k } ) k _ { j } + a _ { j } ( { \bf k } ) k _ { i } + b ( { \bf k } ) ( k _ { i } k _ { j } - \frac { 1 } { 3 } \delta _ { i j } | { \bf k } | ^ { 2 } ) ,
$$

with $k ^ { i } a _ { i } ( { \bf { k } } ) = 0$ ,in order to respect the condition of zero trace.The most general spurious state is therefore parametrized bya scalar $b$ and bya transverse vector $a _ { i }$ Exactly as with the scalat $\phi$ found above,expanding $b$ in spherical harmonics we have one state for each $j$ ，with parity $P = ( - 1 ) ^ { j }$ This eliminates the state with $j = 0$ in eq:(2.201)，while at level $j = 1$ it leaves us with one state with $P = + 1$ and one with $P = - 1$ ,and atall higher jlevelswe are left with two states with $P = + 1$ and two with $P = - 1$ Finally,we must remove the spurious states described by $a _ { i } ( \mathbf { k } )$ .However this is vector,transverse to $\mathbf { k }$ ,and therefore its states are the same as the photon states discussed above. There is no state at $\dot { \boldsymbol { \jmath } } = 0$ ,and two states,with opposite parity,at all other $j$ level.This remove the two states which were left at $j = 1$ ,and leaves us with two states,with opposite parity,at all higher levels. In conclusion,for the graviton,

j=0: no state,   
$j = 1$ ： no state,   
$j = 2 , 3 , \dots$ :two states,one with $P = +$ one with $P = -$

Therefore, for gravitational wave there cani be no monopole nor dipole raliation,since these would correspond to gravitons with $j = 0$ and $j = 1$ spectively. We will come back to the multipole expansion of gravitational aves in Section 3.5.2，where we will show how to express the two states allowed for $j \geqslant 2$ in terms of tensor spherical harmonics,and we will verify gain that states with $j = 0$ or $j = 1$ are not allowed.

# Further reading

· For the quantum field-theoretical approach to gravitation see the Feynman Lectures on Gravitation by Feynman,Morinigo,and Wagner(1995) (which collects lectures given by Feynman in 1962-63)，and also DeWitt (1967) and Veltman (1976).For explicit computations of graviton-graviton scattering see Grisaru,van Nieuwenhuizen and Wu (1975).

· The possibility of deriving Einstein equation from an iteration of linearized theory is discussed,among others,by Gupta (1954),Kraichnan (1955),Feynman,Morinigo,and Wagner (1995),and Ogievetsky and Polubarinov (1965)．An explicit and elegant iteration leading from the equations of motion of linearized theory to the full Einstein equations was performed by Deser (197O） using a first order Palatini formalism.The ambiguity concerning boundary terms is discussed by Padmanabhan (2004).

· Phenomenological limits on the graviton mass are discussed by Goldhaber and Nieto (1974).The discontinuity as the graviton mass goes to zero was found by Iwasaki (197O)，van Dam and Veltman (1970）and Zakharov (1970).Massive gravitons have been further discussed by Boulware and Deser (1972)．The fact that linearized theory becomes singular as $m _ { g }  0$ was discovered by Vainshtein (1972).The radiation of massive gravitons in linearized theory is discussed by van Niewenhuizen (1973).Discussions of the fate of the discontinuityare given in Deffayet,Dvali,Gabadadze and Vainshtein (2002） and in Arkani-Hamed,Georgi and Schwartz (2003)．The difficulty of performing the matching to an asymptotically fat solution,and the possibility of matching to a De Sitter solution,is discussed in Damour,Kogan and $\mathrm { P a }$ - pazoglou (2Oo3).The fact that beyond linearized theory the trace $h$ becomes a ghost is discussed by Boulware and Deser (1972) and,in full generality,by Creminelli,Nicolis,Papucci and Trincherini (2005）.

·Lorentz-violating mass terms for $h _ { \mu \nu }$ are discussed in Arkani-Hamed,Cheng,Luty and Mukohyama (2004)，Rubakov (2004） and Dubovsky,Tinyakov and Tkachev (2005).In this case the mass of the scalar perturbations can be zero while the mass of the graviton $h _ { i j } ^ { \mathrm { T T } }$ canbenozerondtod on the graviton mass derived from the Yukawa falloff of the gravitational potential only refer to the scalar sector.Furthermore,these models do not sufferlof the vDVZ discontinuity and do not have ghosts.

A bound on the mass that refers directly to $h _ { i j } ^ { \mathrm { T T } }$ can be obtained from pulsar timing,as recognized in Damour and Taylor (1991) and discussed quantitatively in Finn and Sutton (2002). The possibility of bounding the mass of $h _ { i j } ^ { \mathrm { T T } }$ from the observation of inspiraling compact binaries is discussed in Will (1998)and Larson and Hiscock (2000).

# Generation of GWs in linearized theory

We now consider the generation of GWs in the context of linearized theory.This means that we assume that the gravitational field generated by the source is sufficiently weak,so that an expansion around flat spacetime is justified.For a system held together by gravitational forces, this implies that the typical velocities inside the source are small. For instance,in a gravitationally bound two-body system with reduced mass $\mu$ and total mass $m$ ,we have $E _ { \mathrm { k i n } } = - \mathrm { ( 1 / 2 ) } \dot { U } _ { \mathrm { : } }$ i.e.

$$
{ \frac { 1 } { 2 } } \mu v ^ { 2 } = { \frac { 1 } { 2 } } { \frac { { \cal \vec { G } } \mu m } { r } } ,
$$

and therefore

$$
\frac { v ^ { 2 } } { c ^ { 2 } } = \frac { R _ { \mathcal { S } } } { 2 r } ,
$$

where $R _ { S } = 2 G m / c ^ { 2 }$ is the Schwarzschild radius associated to a mass m. A weak gravitational field means $\dot { R } _ { S } / r \ll 1$ and therefore $v \ll c$ Thus,for a self-gravitating system，weak felds imply small velocities. On the other hand,for a system whose dynamics is determined by mon-gravitational forces,the weak-feld expansion and the low-velocity expansion are independent，and in this case it makes sense to consider weak-field sources with arbitrary velocities,as we do in this chapter.This will allow us to understand, in the simple setting of a fat background space-time (and therefore Newtonian or at most specialrelativistic dynamics for the sources),how GWs are produced.In Section 3.1 we will derive the formulas for GW production valid in fat Epace-time,but exact in $v / c$ .Then,expanding the exact result in powers of $v / c$ ，we will see that for small velocities the GW production can be organized in a multipole expansion (Section 3.2). In Section 3.3 we discuss in detail the lowest order term, which is the quadrupole radiation.In Section 3.4 we discuss the next-to-leading terms,i.e. the massctupole and the current quadrupole radiation,and in Section 3.5 we present the systematic multipole exparision to all orders,using first the fomalism of symmetric-trace-free (STF) tensors,and then the spherial tensors formalism. Finally,in a Solved Problems section we discuss ome applications of this formalism and we collect additional technical material.

The most interesting astrophysical sources of GWs, such as neutron Stars, black holes or compact binaries,are self-gravitating systems.In

![](images/b5532b9837ed7b5fbfd9326768efaa8f331d7d9387791f7161179ece2f9a8ab5.jpg)

3.1 Weak-field sources with arbitrary velocity 102

3.2 Low-velocity expansion105

3.3 Mass quadrupole 109

3.4 Mass octupole and current quadrupole

3.5 Systematic multipole expansion

3.7 Solved problems 156

this case, if we want to compute corrections in $v / c ,$ we must take into account that,because of eq. (3.2),space-time cannot be considered flat beyond lowest order,and therefore the dynamics of the sources can no longer be described by Newtonian gravity. The corresponding formalism is the GW generation from pqst-Newtonian sources,which will be the subject of Chapter 5.Still, the results derived in the present chapter will be useful also as a first step toward the understanding of the post-Newtonian results.

1More precisely，the retarded Green's function is selected by imposing the Kirchoff-Sommerfeld“no-incomingradiation”boundary conditions,i.e. one imposes

# 3.1Weak-field sources with arbitrary velocity

In linearized theory the startirg point is eq.(1.24),that we recall here,

$$
\bigtriangledown \bar { h } _ { \mu \nu } \Big | = - \frac { 1 6 \pi G } { c ^ { 4 } } T _ { \mu \nu } ,
$$

where $T _ { \mu \nu }$ is the energy-momentum tensor of matter.Recall also that we are in the Lorentz gauge, $\partial ^ { \mu } { \bar { h } } _ { \mu \nu } = 0$ ，and that $T _ { \mu \nu }$ satisfies the flat-space conservation law $\partial ^ { \mu } \mathcal { T } _ { \mu \nu } = 0$ Equation (3.3) is linear in $h _ { \mu \nu }$ and can be solved by the method of Green's function: if $G ( x - x ^ { \prime } )$ isa solution of the equation

$$
\begin{array} { r } { \ b { \Omega } _ { x } G ( x - x ^ { \prime } ) = \delta ^ { 4 } ( x - x ^ { \prime } ) , } \end{array}
$$

(where $\sqsubseteq _ { x }$ is the d'Alembertian operator with derivatives taken with respect to the variable $x$ ),then the corresponding solution of eq. (3.3) is

$$
\bar { h } _ { \mu \nu } ( x ) = - \frac { 1 6 \pi G } { c ^ { 4 } } \int d ^ { 4 } x ^ { \prime } G ( x - x ^ { \prime } ) T _ { \mu \nu } ( x ^ { \prime } ) .
$$

The solution of eq. (3.4) depends of course on the boundary conditions that we impose.Just as in electromagnetism,for a radiation problem theappropriate solution is the retarded Green's function,1

$$
G ( x - x ^ { \prime } ) = - \frac { 1 } { 4 \pi | { \bf x } - { \bf x } ^ { \prime } | } \delta ( x _ { \mathrm { r e t } } ^ { 0 } - { x ^ { \prime } } ^ { 0 } ) ,
$$

$$
\operatorname * { l i m } _ { t  - \infty } [ \frac { \partial } { \partial r } + \frac { \partial } { c \partial t } ] ( r \bar { h } _ { \mu \nu } ) ( { \bf x } , t ) = 0 ,
$$

where the limit is taken along any surface $c t + r = \mathrm { c o n s t a }$ nt，together with the condition that $r \bar { h } _ { \mu \nu }$ and $r \partial _ { \rho } \bar { h } _ { \mu \nu }$ be bounded in this limit.Physically, this means that there is no incoming radiation at past null infinity.

where ${ x ^ { \prime } } ^ { 0 } = c t ^ { \prime }$ $x _ { \mathrm { r e t } } ^ { 0 } = c t _ { \mathrm { r e t } }$ ,and

$$
t _ { \mathrm { r e t } } = t - \frac { | { \bf x } - { \bf x } ^ { \prime } | } { c }
$$

is called retarded time.Then the solution of eq.(3.3) is

$$
\bar { h } _ { \mu \nu } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \int d ^ { 3 } x ^ { \prime } \frac { 1 } { | { \bf x } - { \bf x } ^ { \prime } | } T _ { \mu \nu } \left( t - \frac { | { \bf x } - { \bf x } ^ { \prime } | } { c } , { \bf x } ^ { \prime } \right) .
$$

Outside the_source we can put this solution in the TT gauge using eq. (1.40), $h _ { i j } ^ { \mathrm { T T } } = \Lambda _ { i j , k l } h _ { k l } = \Lambda _ { i j , k l } \bar { h } _ { k l }$ (in the last equalityweused the

property (1.38) of the Lambda tensor).|Therefore,outside the source,

$$
h _ { i j } ^ { \mathrm { T T } } ( t , { \bf x } ) = \frac { 4 G } { c ^ { 4 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) \int d ^ { 3 } x ^ { \prime } \frac { 1 } { | { \bf x } - { \bf x } ^ { \prime } | } T _ { k l } \left( t - \frac { | { \bf x } - { \bf x } ^ { \prime } | } { c } , { \bf x } ^ { \prime } \right) ,
$$

where we use the notation $\hat { \textbf { x } } = \hat { \textbf { n } }$ ，and we will also denote $| { \bf x } | = r$ Observe that $h _ { i j } ^ { \mathrm { T T } }$ depends only the integrals of the spatial components $T _ { k l }$ The underlying reason that allowed us to eliminate $T _ { 0 k }$ and $T _ { 0 0 }$ is that they are related to $T _ { k l }$ by the conservation of the energy-momentum tensor.² If we denote by $d$ the typical radius of the source,at $r \gg d$ we can expand

$$
| \mathbf { x } - \mathbf { x } ^ { \prime } | = r - \mathbf { x } ^ { \prime } \cdot \hat { \mathbf { n } } + O \left( \frac { d ^ { 2 } } { r } \right) ,
$$

see Fig. 3.1. We are particularly interested in the value of $h _ { i j } ^ { \mathrm { T T } }$ at large distances from the source,where the detector is located,so we take the limit $r \to \infty$ at fixed ${ t , } ^ { 3 }$ and we retain only the leading term in eq. (3.9). This isa term $O ( 1 / r )$ ,obtained setting $\left| \mathbf { x } - \mathbf { x } ^ { \prime } \right| = r$ in the denominator f eq. (3.9), so at large distances

$$
h _ { i j } ^ { \mathrm { T T } } ( t , { \bf x } ) = \frac { 1 } { r } \frac { 4 G } { c ^ { 4 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) \int d ^ { 3 } x ^ { \prime } T _ { k l } \left( t - \frac { r } { c } + \frac { { \bf x } ^ { \prime } \cdot \hat { \bf n } } { c } , { \bf x } ^ { \prime } \right) ,
$$

plus terms $O ( 1 / r ^ { 2 } )$ that we neglect. We now write $T _ { k l }$ in terms of its Fourier transform,4

$$
T _ { k l } ( t , { \bf x } ) = \int \frac { d ^ { 4 } k } { ( 2 \pi ) ^ { 4 } } \tilde { T } _ { k l } ( \omega , { \bf k } ) e ^ { - i \omega t + i { \bf k } \cdot { \bf x } } .
$$

Then

$$
\begin{array} { l } { { \displaystyle \int d ^ { 3 } x ^ { \prime } T _ { k l } \left( t - r / c + { \bf x ^ { \prime } } \cdot \hat { \bf n } / c \right) } \ ~ } \\ { { \displaystyle = \int d ^ { 3 } x ^ { \prime } \int \frac { d \omega } { 2 \pi c } \frac { d ^ { 3 } k } { ( 2 \pi ) ^ { 3 } } \tilde { T } _ { k l } ( \omega , { \bf k } ) e ^ { - i \omega ( t - r / c ) } e ^ { i ( { \bf k } - \omega \hat { \bf n } / c ) \cdot { \bf x ^ { \prime } } } } \ ~ } \\ { { \displaystyle = \int \frac { d \omega } { 2 \pi c } \frac { d ^ { 3 } k } { ( 2 \pi ) ^ { 3 } } \tilde { T } _ { k l } ( \omega , { \bf k } ) e ^ { - i \omega ( t - r / c ) } \left( 2 \pi \right) ^ { 3 } \delta ^ { ( 3 ) } \left( { \bf k } - \omega \hat { \bf n } / c \right) } \ ~ } \\ { { \displaystyle = \int \frac { d \omega } { 2 \pi c } \tilde { T } _ { k l } \left( \omega , \omega \hat { \bf n } / c \right) e ^ { - i \omega ( t - r / c ) } } , } \end{array}
$$

and we get

<table><tr><td>1 4G 8 hT(tx) = Aij,k(n) r c5 18</td><td>Tl(wwn/c)e-iw(t-r/e).</td></tr><tr><td></td><td></td></tr></table>

2Indeed，when performing the multipole expansion below， the lowestorder result will be re-expressed in terms of $\pmb { T } ^ { 0 0 }$ only,using again energymomentum conservation.

![](images/25b851b8d02204a9c131973f95f556d4f5c2f0e7c7bf3ed88205c711a70d8218.jpg)  
Fig.3.1 A graphical illustration of the relation given in eq. (3.10).

$^ 3 \mathrm { { I n } }$ linearized theory, GWs are studied at spatial infinity,i.e. $r  \infty$ at fixed $t$ We will see in Chapter 5 that,beyond linearized theory, it can be more convenient to work at future null infinity,i.e. $r  \infty$ with $t - r / c$ fixed.

$^ 4 \mathrm { O u r }$ convention on the factors of $c$ is that the four-dimensional wave-vector is $k ^ { \mu } = ( \omega / c , \mathbf { k } )$ ，and therefore $d ^ { 4 } k =$ $( 1 / c ) d \omega d ^ { 3 } k$ Since $x ^ { \mu } ~ = ~ ( c t , \mathbf { x } )$ ，we then have $k _ { \mu } x ^ { \mu } = - \omega t + \mathbf { k } \mathbf { \cdot x }$ .Observe that $\mathbf { k }$ has dimensions of the inverse of length.The spatial momentum of a particle with wave-vector $\mathbf { k }$ is $\mathbf { p } = \hbar \mathbf { k }$

In general,the Fourier components of the energy-momentum tensor of the source will be large around a typical value $\omega _ { s }$ ,and the characteristic speed at which there is a bulk movement of mass across the source is $v \sim \omega _ { s } d$ 、For the moment we have made no assumption on the relative values of $\omega _ { s }$ and $d$ ，and in particular we have not assumed $\omega _ { s } d \ll c$ Therefore eq.(3.14) is valid both for relativistic and for non-relativistic sources,as long as linearized theory applies,and we are at a sufficiently large distance $r$ from the source.

From eq. (1.156)， setting $d \ddot { A } = r ^ { 2 } d \Omega$ ，we see that the total energy radiated per unit solid angle is

$$
\frac { d E } { d \Omega } = \frac { r ^ { 2 } c ^ { 3 } } { 3 2 \pi G } \int _ { - \infty } ^ { \infty } d t \dot { h } _ { i j } ^ { \mathrm { T T } } \dot { h } _ { i j } ^ { \mathrm { T T } } .
$$

$^ 5 \mathrm { T } _ { 0 }$ compare with Weinberg(1972)， Section 10.4,observe that we define the Fourier transform with respect to frequency using $d \omega / ( 2 \pi )$ (see eq.(3.12),or the Notation section)while Weinberg uses $d \omega$ ；on the other hand,we both use $d ^ { 3 } k / ( 2 \pi ) ^ { 3 }$ in the spatial Fourier transform.Therefore our $\tilde { \cal T } ( \omega , { \bf k } )$ is equal to $2 \pi \tilde { T } ^ { \mathrm { W e i n b e r g } } ( \omega , \mathbf { k } )$

Inserting here the expression (3.14),using $\tilde { T } ( - \omega , - \mathbf { k } ) = \tilde { T } ^ { * } ( \omega , \mathbf { k } )$ and the property (1.37) of the Lambda tensor,we find5

$$
\frac { d E } { d \Omega } = \frac { G } { 2 \pi ^ { 2 } c ^ { 7 } } \Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) \int _ { 0 } ^ { \infty } d \omega \omega ^ { 2 } \tilde { T } _ { i j } ( \omega , \omega \hat { \mathbf { n } } / c ) \tilde { T } _ { k l } ^ { * } ( \omega , \omega \hat { \mathbf { n } } / c ) ,
$$

and the energy spectrum is therefore

$$
\frac { d E } { d \omega } = \frac { G \omega ^ { 2 } } { 2 \pi ^ { 2 } c ^ { 7 } } \int d \Omega \Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) \tilde { T } _ { i j } ( \omega , \omega \hat { \mathbf { n } } / c ) \tilde { T } _ { k l } ^ { * } ( \omega , \omega \hat { \mathbf { n } } / c ) .
$$

6Of course,at the latest this divergence is cutoff by the back-reaction due to GW emission. For example,a spinning neutron star with non-vanishing ellipticity emits GWs.The energy of these waves is taken from the rotational energy of the star which therefore gradually slows down,as we will compute in detail in Section 4.2. (Actually,in this case electromagnetic effects dominate and slow down the neutron star even earlier.)

A typical source will radiate for a characteristic time $\Delta t$ In the idealized case of an exactly monochromatic source, the radiation lasts for $\Delta t = \infty$ and the total radiated energy is formally divergent. Thus,for a monochromatic source the instantaneously radiated power is a more useful quantity. For such a source,radiating at a frequency $\omega _ { 0 }$ , we write $\tilde { T } _ { i j } ( \omega , \bar { \bf k } )$ (for positive $\omega$ as

$$
\tilde { T } _ { i j } ( \omega , \mathbf { k } ) = \theta _ { i j } ( \omega , \mathbf { k } ) 2 \pi \delta ( \omega - \omega _ { 0 } ) ,
$$

and eq.(3.16)becomes

7More precisely,we have seen in Chapter1 that the GW energy is only defined by averaging over a few periods, so this is really the average power radiated over one period of the source motion.

$$
\frac { d E } { d \Omega } = \frac { G \omega _ { 0 } ^ { 2 } } { \pi c ^ { 7 } } \Lambda _ { i j , k l } ( \hat { \mathbf { n } } ) \theta _ { i j } ( \omega _ { 0 } , \omega _ { 0 } \hat { \mathbf { n } } / c ) \theta _ { k l } ^ { * } ( \omega _ { 0 } , \omega _ { 0 } \hat { \mathbf { n } } / c ) T .
$$

We have used $2 \pi \delta ( \omega = 0 ) = T ,$ where $T$ is the total (formally infinite) time. Dividing by $T$ we obtain the power radiated instantaneously,7

$$
\frac { d P } { d \Omega } = \frac { G \omega _ { 0 } ^ { 2 } } { \pi c ^ { 7 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) \theta _ { i j } \big ( \omega _ { 0 } , \omega _ { 0 } \hat { \bf n } / c ) \theta _ { k l } ^ { * } \big ( \omega _ { 0 } , \omega _ { 0 } \hat { \bf n } / c \big ) .
$$

The total power is obtained by integrating over $d \Omega$ To perform the integration one can use the idehtities

$$
\int \frac { d \Omega } { 4 \pi } n _ { i } n _ { j } = \frac { 1 } { 3 } \delta _ { i j } ,
$$

$$
\int \frac { d \Omega } { 4 \pi } n _ { i } n _ { j } n _ { k } n _ { l } = \frac { 1 } { 1 5 } \left( \delta _ { i j } \delta _ { k l } + \delta _ { i k } \delta _ { j l } + \delta _ { i l } \delta _ { j k } \right) .
$$

These identities,as well as their generalization to an arbitrary number of $n ^ { \prime } s$ ，can be found as follows.For an odd number of $n _ { i }$ the integral vanishes because the integrand is odd under parity.For an even number $_ { \mathrm { ~ o f ~ } n }$ ,we use the fact that the tensor $n _ { i _ { 1 } } n _ { i _ { 2 } } \dots n _ { i _ { 2 l } }$ is totally symmetric and therefore its integral can only depend on the totally symmetrized product of Kronecker deltas.Once the tensor structure is fixed,the overall constant is obtained by contracting all indices.This gives

$$
\int { \frac { d \Omega } { 4 \pi } } n _ { i _ { 1 } } \ldots n _ { i _ { 2 l } } = { \frac { 1 } { ( 2 l + 1 ) ! ! } } \left( \delta _ { i _ { 1 } i _ { 2 } } \delta _ { i _ { 3 } i _ { 4 } } \ldots \delta _ { i _ { 2 l - 1 } i _ { 2 l } } + \ldots \right) ,
$$

where the final dots denote all possiblelpairing of indices.

# 3.2 Low-velocity expansion

Just as in electrodynamics,the equations for the generation of radiation are greatly simplified if the typical velocities inside the source are small compared to the speed of light.If $\omega _ { s }$ is the typical frequency of the motion inside the source and $d$ is the source size,the typical velocities inside the source are $v \sim \omega _ { s } d$ .The frequency $\omega$ of the radiation will also be of order8 $\omega _ { s }$ and therefore $\omega \sim \omega _ { s } \sim \nu / d$ In terms of $\dot { \lambda } = c / \omega$ ，

$$
\quad \ : \dot { x } \sim \frac { c } { v } d . \nonumber \ :
$$

In a non-relativistic system, $v \ll c$ and the reduced wavelength of the radiation generated is much bigger thah the size of the system:

$$
\begin{array} { r } { \boxed { \begin{array} { r c l } { \mathrm { ~ } } & { \mathrm { ~ n o n - r e l a t i v i s t i c ~ s o u r c e s } } & { \implies } & { \lambda \gg d . } \end{array} } } \end{array}
$$

When the reduced wavelength is much bigger than the size of the system, it is physically clear that we do not need to know the internal motions f the source in all its details,but onlly the coarse features matter,so the emission of radiation is governed by the lowest multipole moments.9

8Apart from numerical factors which depend on the multipole moment involved and on the details of the motion of the source.We will see below that for a non-relativistic system the dominant contributions come from the lowest multipoles,and for these the numerical factors are $O ( 1 )$ ；for instance, we will see that a source performing a simple harmonic oscillation at frequency wgemits quadrupole radiation $\omega = 2 \omega _ { s }$

To perform the multipole expansioh for gravitational radiation we start from the expression of $h _ { i j } ^ { \mathrm { T T } }$ at spatial infinitygivenineq.(3.1), that we recall here,

$$
h _ { i j } ^ { \mathrm { T T } } ( t , { \bf x } ) = \frac { 1 } { r } \frac { 4 G } { c ^ { 4 } } \Lambda _ { i j , k l } ( \hat { \bf n } ) \int d ^ { 3 } x ^ { \prime } T _ { k l } \left( t - \frac { r } { c } + \frac { { \bf x } ^ { \prime } \cdot \hat { \bf n } } { c } , { \bf x } ^ { \prime } \right) ,
$$

and we write $T _ { k l }$ in terms of its Fourier transform,

$$
T _ { k l } \left( t - { \frac { r } { c } } + { \frac { { \bf x } ^ { \prime } \cdot \hat { \bf n } } { c } } , { \bf x } ^ { \prime } \right) = \int { \frac { d ^ { 4 } k } { ( 2 \pi ) ^ { 4 } } } \hat { T } _ { k l } ( \omega , { \bf k } ) e ^ { - i \omega ( t - r / c + { \bf x } ^ { \prime } \cdot \hat { \bf n } / c ) + i { \bf k } \cdot { \bf x } ^ { \prime } } .
$$

For a non-relativistic source, $\tilde { T } _ { k l } ( \omega , \mathbf { k } ) _ { i } ^ { \scriptscriptstyle | }$ is peaked around a typical frequency $\omega _ { s }$ (or around a range of frequencies,with maximum value $\omega _ { s }$ ），

$^ { 9 } \mathrm { A }$ typicalexampleistheelectro magnetic radiation from the hydrogen atom．The velocity of the electron inside the hydrogen atom is $v / c \sim \alpha$ ， where $\alpha \simeq 1 / 1 3 7$ is the fine-structure constant,and the reduced wavelengths of the transitions between the levels of the hydrogen atom are of order $\bar { \lambda } \sim$ $r _ { B } / \alpha$ ，where $r _ { B }$ is the Bohr radius. Since $\alpha \ll 1$ ，we have $\mathit { \Pi } ^ { \ddag } \gg \mathit { \Delta } r _ { B }$ ，and the multipole expansion is adequate.